"""Blender render of one stylised pillow coloured by the heat-kernel diagonal.

    blender -b --factory-startup --threads 4 -P figures/src/render_pillow.py -- \
        MESH.npz OUT.png [--palette A] [--res 1200x900] [--vmin V] [--vmax V] [--view az,el]

--pass colour renders the exact vertex colours (flat, unlit); --pass shade renders a uniform grey
surface under the studio light. figstyle.shade() combines the two with a fixed, mild weight, so
the shading shows the shape without changing the colour scale by more than that weight.
MESH.npz is written by pillow_mesh.py. The colour of a vertex is the palette's sequential map at
(log ratio - vmin)/(vmax - vmin), ratio = 4 pi t h_t(x,x); vmin, vmax are passed so that several
renders share one scale. The camera is orthographic. Not part of the verification suite.
"""
import math
import sys
from pathlib import Path

import bpy
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "figures" / "style"))
from blender_palette import Palette, setup_scene, srgb_to_linear  # noqa: E402


def args():
    a = sys.argv[sys.argv.index("--") + 1:]
    opt = {"--palette": None, "--res": "1200x900", "--vmin": None, "--vmax": None, "--view": "-35,32", "--pass": "colour"}
    pos = []
    i = 0
    while i < len(a):
        if a[i] in opt:
            opt[a[i]] = a[i + 1]
            i += 2
        else:
            pos.append(a[i])
            i += 1
    return pos, opt


def main():
    (mesh_path, out), opt = args()
    pal = Palette(opt["--palette"])
    d = np.load(mesh_path)
    V, F, ratio = d["vertices"], d["faces"], d["ratio"]
    lr = np.log(ratio)
    vmin = float(opt["--vmin"]) if opt["--vmin"] else float(lr.min())
    vmax = float(opt["--vmax"]) if opt["--vmax"] else float(lr.max())
    assert lr.min() >= vmin - 1e-9 and lr.max() <= vmax + 1e-9, "value outside the shared scale"

    bpy.ops.wm.read_factory_settings(use_empty=True)
    rx, ry = (int(v) for v in opt["--res"].split("x"))
    sc = setup_scene(bpy, pal, rx, ry)

    V = V - V.mean(axis=0)
    me = bpy.data.meshes.new("pillow")
    me.from_pydata(V.tolist(), [], F.tolist())
    me.update()
    col = me.color_attributes.new("heat", "FLOAT_COLOR", "POINT")
    rgb = srgb_to_linear(pal.sequential((lr - vmin) / (vmax - vmin)))
    col.data.foreach_set("color", np.c_[rgb, np.ones(len(rgb))].ravel())
    me.color_attributes.active_color = col
    me.shade_smooth()
    # sharp corners: crease the cone points so the subdivision keeps them
    crease = me.attributes.new("crease_vert", "FLOAT", "POINT")
    vals = np.zeros(len(V))
    bnd = d["boundary"]
    big = bnd[ratio[bnd] > 0.9 * d["orders"].min()]
    vals[big] = 1.0
    crease.data.foreach_set("value", vals)
    ob = bpy.data.objects.new("pillow", me)
    sc.collection.objects.link(ob)
    mod = ob.modifiers.new("subdiv", "SUBSURF")
    mod.levels = mod.render_levels = 2

    az, el = (math.radians(float(v)) for v in opt["--view"].split(","))
    cam_data = bpy.data.cameras.new("cam")
    cam_data.type = "ORTHO"
    R = float(np.max(np.linalg.norm(V[:, :2], axis=1)))
    cam_data.ortho_scale = 2.25 * R
    cam = bpy.data.objects.new("cam", cam_data)
    dist = 10 * R
    cam.location = (dist * math.cos(el) * math.sin(az), -dist * math.cos(el) * math.cos(az), dist * math.sin(el))
    sc.collection.objects.link(cam)
    con = cam.constraints.new("TRACK_TO")
    target = bpy.data.objects.new("target", None)
    sc.collection.objects.link(target)
    con.target = target
    con.track_axis = "TRACK_NEGATIVE_Z"
    con.up_axis = "UP_Y"
    sc.camera = cam
    if opt["--pass"] == "colour":          # exact vertex colours: no lighting at all
        sc.display.shading.light = "FLAT"
    else:                                  # shading only: a uniform grey surface under studio light
        sc.display.shading.color_type = "SINGLE"
        sc.display.shading.single_color = (0.8, 0.8, 0.8)
    sc.render.filepath = str(Path(out).resolve())
    bpy.ops.render.render(write_still=True)


if __name__ == "__main__":
    main()
