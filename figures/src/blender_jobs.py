"""Run Blender renders one at a time, with the machine-safety guard of SPEC section 5.

Before every render: read `sysctl vm.swapusage`; while swap use exceeds 75%, wait (30 s steps).
If it stays above 75% for WAIT_LIMIT seconds, give up and raise SwapBusy, so the caller can go on
with other work and come back. Renders are cached in figures/build/ and redone only when an input
is newer than the image. Never run in parallel; 4 threads; Workbench engine.
"""
import subprocess
import time
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
BUILD = ROOT / "figures" / "build"
WAIT_LIMIT = 20 * 60


class SwapBusy(RuntimeError):
    pass


def swap_fraction():
    out = subprocess.check_output(["sysctl", "-n", "vm.swapusage"]).decode()
    tot = float(out.split("total =")[1].split("M")[0])
    used = float(out.split("used =")[1].split("M")[0])
    return used / tot if tot else 0.0


def wait_for_swap(limit=0.75):
    t0 = time.time()
    while (f := swap_fraction()) > limit:
        if time.time() - t0 > WAIT_LIMIT:
            raise SwapBusy(f"swap use {f:.0%} above {limit:.0%} for {WAIT_LIMIT // 60} min")
        print(f"swap use {f:.0%} > {limit:.0%}: waiting", flush=True)
        time.sleep(30)


def render(script, args, out, inputs):
    """blender -b --factory-startup --threads 4 -P script -- *args, writing `out` (cached)."""
    out = Path(out)
    deps = [Path(p) for p in inputs] + [Path(script), ROOT / "figures/style/palette.json",
                                         ROOT / "figures/style/blender_palette.py"]
    if out.exists() and all(out.stat().st_mtime > p.stat().st_mtime for p in deps):
        return out
    wait_for_swap()
    subprocess.run(["blender", "-b", "--factory-startup", "--threads", "4", "-P", str(script), "--", *map(str, args)],
                   check=True, stdout=subprocess.DEVNULL)
    assert out.exists(), out
    return out


def two_pass(mesh, stem, extra, inputs=()):
    """Colour pass and shading pass of render_pillow.py, combined by figstyle.shade()."""
    import figstyle as fs
    from PIL import Image
    script = ROOT / "figures/src/render_pillow.py"
    paths = {}
    for kind in ("colour", "shade"):
        p = BUILD / f"{stem}_{kind}.png"
        paths[kind] = render(script, [mesh, p, *extra, "--pass", kind], p, [mesh, *inputs])
    img = fs.shade(paths["colour"], paths["shade"])
    out = BUILD / f"{stem}.png"
    Image.fromarray((img * 255).round().astype(np.uint8)).save(out)
    return out


def crop(img, pad=10):
    bg = img[2, 2]
    r, c = np.where(np.abs(img[..., :3] - bg[:3]).sum(-1) > 0.02)
    return img[max(r.min() - pad, 0):r.max() + pad, max(c.min() - pad, 0):c.max() + pad]
