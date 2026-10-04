"""Gate G6 contact sheet: every palette candidate on the same three test panels, as seen with
normal vision, with deuteranopia, with protanopia and in greyscale.

    python3 figures/src/contact_sheet.py [--no-render]

Test panels, all from committed data:
  (i)   a Blender render of O(3,3,12) coloured by 4 pi t h_t(x,x) at t = 0.02
        (numerics/data/heat_kernel_diagonal.npz, through pillow_mesh.py and render_pillow.py);
  (ii)  (Z(t) - c_1/t - c_2)/t for O(2,8,8) and O(3,3,12) in the pillow hue pair
        (numerics/data/heat_trace_difference.csv); both curves tend to c_3 as t -> 0;
  (iii) the least-order strata in the (S, R) plane, p = 2..8, S <= 80 (figures/data/f7_strata.csv),
        the collision (2,8,8) ~ (3,3,12) at S = 18 in the hue pair, and the first collisions.
Writes figures/proofs/contact-sheet.pdf and .png (candidates A-D top to bottom; in each block
the rows are normal, deuteranopia, protanopia, greyscale) and figures/proofs/candidate-<K>-<name>.png.
The candidates are named only in the file names and in figures/proofs/CANDIDATES.md.

Asserted: c_1 = 1/8 and c_2 = 67/48 for both pillows and c_3 = -1601/480, -867/160 (exact, from
theory/stability/stab_common.heat_direct); the plotted quantity at the smallest t equals c_3 + c_4 t to
0.2% of c_3; the strata table reproduces S*(p) overlap and the collision at (18, 3/4).
"""
import os
import subprocess
import sys
import time
from fractions import Fraction as Fr
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path[:0] = [str(ROOT / "figures" / "style"), str(ROOT / "theory" / "stability")]
import colourtools as ct  # noqa: E402
import figstyle as fs  # noqa: E402
from stab_common import heat_direct  # noqa: E402

import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.backends.backend_agg import FigureCanvasAgg  # noqa: E402

BUILD = ROOT / "figures" / "build"
PROOFS = ROOT / "figures" / "proofs"
T_INDEX = 2                           # t = 0.02
DPI = 300


def swap_ok(limit=0.75):
    out = subprocess.check_output(["sysctl", "-n", "vm.swapusage"]).decode()
    tot = float(out.split("total =")[1].split("M")[0])
    used = float(out.split("used =")[1].split("M")[0])
    return used / tot <= limit, used / tot


def render(key):
    """Blender render of the (3,3,12) pillow for palette candidate `key` (one job at a time)."""
    out = BUILD / f"contact_render_{key}.png"
    mesh = BUILD / f"mesh_3-3-12_t{T_INDEX}.npz"
    if out.exists() and out.stat().st_mtime > mesh.stat().st_mtime:
        return out
    for _ in range(60):                       # machine safety: wait (up to 30 min) while swap use > 75%
        ok, frac = swap_ok()
        if ok:
            break
        print(f"swap use {frac:.0%} > 75%: waiting before the render", flush=True)
        time.sleep(30)
    assert ok, f"swap use {frac:.0%} stayed above 75%: not starting Blender"
    lo = min(float(np.log(np.load(BUILD / f"mesh_{k}_t{T_INDEX}.npz")["ratio"]).min()) for k in ("2-8-8", "3-3-12"))
    hi = float(np.log(12.0))
    for kind in ("colour", "shade"):
        subprocess.run(["blender", "-b", "--factory-startup", "--threads", "4", "-P", str(ROOT / "figures/src/render_pillow.py"),
                        "--", str(BUILD / f"mesh_3-3-12_t{T_INDEX}.npz"), str(out).replace(".png", f"_{kind}.png"),
                        "--palette", key, "--res", "1000x800", "--view", "-20,62", "--vmin", repr(lo), "--vmax", repr(hi),
                        "--pass", kind], check=True, stdout=subprocess.DEVNULL)
    from PIL import Image
    img = fs.shade(str(out).replace(".png", "_colour.png"), str(out).replace(".png", "_shade.png"))
    Image.fromarray((img * 255).round().astype(np.uint8)).save(out)
    return out


def data_ii():
    import csv
    rows = list(csv.DictReader((ROOT / "numerics/data/heat_trace_difference.csv").open()))
    t = np.array([float(r["t"]) for r in rows])
    out = {}
    for sig, col in (((2, 8, 8), "Z_2_8_8"), ((3, 3, 12), "Z_3_3_12")):
        c1, c2, c3, c4 = heat_direct(sig, 4)
        assert (c1, c2) == (Fr(1, 8), Fr(67, 48))
        Z = np.array([float(r[col]) for r in rows])
        y = (Z - float(c1) / t - float(c2)) / t
        assert abs(y[0] - float(c3 + c4 * Fr(t[0]))) < 0.002 * abs(float(c3)), (sig, y[0], c3, c4)
        out[sig] = (t, y, c3)
    assert out[(2, 8, 8)][2] == Fr(-1601, 480) and out[(3, 3, 12)][2] == Fr(-867, 160)
    return out


def data_iii(smax=80):
    import csv
    rows = [r for r in csv.DictReader((ROOT / "figures/data/f7_strata.csv").open()) if int(r["S"]) <= smax]
    ov = list(csv.DictReader((ROOT / "figures/data/f7_overlap.csv").open()))
    assert ov[0]["first_collision_S"] == "18" and ov[0]["first_collision_R"] == "3/4"
    strata = {}
    for r in rows:
        strata.setdefault(int(r["p"]), []).append((int(r["S"]), float(r["R_min_float"]), float(r["R_max_float"])))
    return strata, [(int(o["p"]), int(o["first_collision_S"]), float(o["first_collision_R_float"])) for o in ov
                    if int(o["first_collision_S"]) <= smax]


def strip(key, render_png, d2, d3):
    """One candidate's three test panels as an RGB array (119 mm x 42 mm at DPI)."""
    fs.use(key)
    A, B = fs.PILLOW["2,8,8"], fs.PILLOW["3,3,12"]
    fig = fs.figure(42)
    canvas = FigureCanvasAgg(fig)
    ax1 = fig.add_axes([0.03, 0.04, 0.27, 0.84])
    im = plt.imread(render_png)[..., :3]
    bg = im[2, 2]
    rows_, cols_ = np.where(np.abs(im - bg).sum(-1) > 0.02)
    pad = 12
    im = im[max(rows_.min() - pad, 0):rows_.max() + pad, max(cols_.min() - pad, 0):cols_.max() + pad]
    ax1.imshow(im)
    ax1.set_axis_off()
    ax2 = fig.add_axes([0.42, 0.22, 0.22, 0.66])
    for sig, col, ls in (((2, 8, 8), A, "-"), ((3, 3, 12), B, "-")):
        t, y, _ = d2[sig]
        ax2.plot(t, y, color=col, lw=fs.LW["heavy"], ls=ls)
    ax2.set_xscale("log")
    ax2.set_xlim(1.5e-3, 0.5)
    ax2.set_xlabel(r"$t$")
    ax2.set_ylabel(r"$(Z(t)-c_1/t-c_2)/t$")
    ax3 = fig.add_axes([0.75, 0.22, 0.24, 0.66])
    strata, firsts = d3
    ps = sorted(strata)
    for p in ps:
        S, lo, hi = (np.array(v) for v in zip(*strata[p]))
        c = fs.SEQ(0.12 + 0.76 * (p - ps[0]) / (ps[-1] - ps[0]))
        ax3.plot(S, lo, color=c, lw=fs.LW["regular"])
        ax3.plot(S, hi, color=c, lw=fs.LW["regular"])
    for p, S1, R1 in firsts[1:]:
        ax3.plot([S1], [R1], marker="o", ms=fs.MARKER_PT["small"], mfc="none", mec=fs.GREY["ink"], mew=fs.LW["thin"])
    S1, R1 = firsts[0][1], firsts[0][2]
    ax3.plot([S1], [R1], marker="o", ms=fs.MARKER_PT["large"], fillstyle="left", mfc=A, mfcalt=B,
             mec=fs.GREY["ink"], mew=fs.LW["hair"])
    ax3.set_xlim(10, 80)
    ax3.set_ylim(0.1, 1.0)
    ax3.set_xlabel(r"$S$")
    ax3.set_ylabel(r"$R$")
    for ax, s in ((ax1, "a"), (ax2, "b"), (ax3, "c")):
        fs.letter(ax, s, dx_pt=-8 if ax is ax1 else -34)
    fig.set_dpi(DPI)
    canvas.draw()
    img = np.asarray(canvas.buffer_rgba())[..., :3] / 255.0
    plt.close(fig)
    return img


def main():
    os.environ.pop("FIG_PALETTE", None)
    keys = list(fs.PALETTE["candidates"])
    if "--no-render" not in sys.argv:
        subprocess.run([sys.executable, str(ROOT / "figures/src/pillow_mesh.py"), str(T_INDEX)], check=True,
                       stdout=subprocess.DEVNULL)
        renders = {k: render(k) for k in keys}
    else:
        renders = {k: BUILD / f"contact_render_{k}.png" for k in keys}
    d2, d3 = data_ii(), data_iii()
    blocks = []
    PROOFS.mkdir(parents=True, exist_ok=True)
    from PIL import Image
    for k in keys:
        s = strip(k, renders[k], d2, d3)
        variants = [s, ct.simulate(s, "deuteranopia"), ct.simulate(s, "protanopia"), ct.grey(s)]
        gap = np.ones((int(0.012 * s.shape[0] * 4), s.shape[1], 3))
        block = np.concatenate(sum(([v, gap] for v in variants), [])[:-1], axis=0)
        name = fs.PALETTE["candidates"][k]["name"]
        Image.fromarray((np.clip(block, 0, 1) * 255).astype(np.uint8)).save(PROOFS / f"candidate-{k}-{name}.png")
        blocks.append(block)
    sep = np.ones((int(0.25 * blocks[0].shape[0] / 4), blocks[0].shape[1], 3))
    sheet = np.concatenate(sum(([b, sep] for b in blocks), [])[:-1], axis=0)
    img = Image.fromarray((np.clip(sheet, 0, 1) * 255).astype(np.uint8))
    img.save(PROOFS / "contact-sheet.png")
    h_mm = sheet.shape[0] / DPI * 25.4
    fig = plt.figure(figsize=(fs.WIDTH_MM * fs.MM, h_mm * fs.MM))
    fig.add_axes([0, 0, 1, 1]).imshow(sheet, interpolation="none")
    fig.axes[0].set_axis_off()
    fs.save(fig, PROOFS / "contact-sheet.pdf", dpi=DPI)
    print(f"contact sheet: {len(keys)} candidates x 4 views, {sheet.shape[1]}x{sheet.shape[0]} px; all assertions passed")


if __name__ == "__main__":
    main()
