"""Mechanical part of the per-figure checklist (figures/REVIEW.md, section 1).

    python3 figures/src/checklist.py [F1 F2 ...]

For each figures/out/Fn.pdf: page width 119 mm and height <= 195 mm (SPEC.md); every font
embedded; no creator, producer or date metadata; the thinnest stroked line >= 0.3 pt; and
the list of every text string, which a reader then compares with "axis titles, tick
labels, panel letters". It also writes figures/build/check_Fn.png: the preview as seen with
deuteranopia, with protanopia and in greyscale (CIE L*), for viewing.
"""
import sys
from pathlib import Path

import fitz
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "figures" / "style"))
import colourtools as ct  # noqa: E402

OUT = ROOT / "figures" / "out"
BUILD = ROOT / "figures" / "build"


def check(name):
    doc = fitz.open(OUT / f"{name}.pdf")
    page = doc[0]
    w, h = page.rect.width / 72 * 25.4, page.rect.height / 72 * 25.4
    assert abs(w - 119) < 0.5 and h <= 195.5, (name, w, h)
    md = {k: v for k, v in doc.metadata.items() if v and k not in ("format", "encryption")}
    assert not md, (name, md)
    fonts = page.get_fonts(full=True)
    for f in fonts:
        assert f[1] not in ("n/a",) and doc.extract_font(f[0])[3], (name, "font not embedded", f)
    widths = [d["width"] for d in page.get_drawings() if d.get("width") and d["type"] in ("s", "fs")]
    thin = min(widths) if widths else None
    assert thin is None or thin >= 0.3 - 1e-6, (name, thin)
    words = sorted({s["text"].strip() for b in page.get_text("dict")["blocks"] for l in b.get("lines", [])
                    for s in l["spans"] if s["text"].strip()})
    from PIL import Image
    img = np.asarray(Image.open(OUT / f"{name}.png").convert("RGB")) / 255.0
    sims = [ct.simulate(img, "deuteranopia"), ct.simulate(img, "protanopia"), ct.grey(img)]
    gap = np.ones((img.shape[0], 12, 3))
    sheet = np.concatenate([sims[0], gap, sims[1], gap, sims[2]], axis=1)
    BUILD.mkdir(exist_ok=True)
    Image.fromarray((np.clip(sheet, 0, 1) * 255).astype(np.uint8)).save(BUILD / f"check_{name}.png")
    print(f"{name}: {w:.1f} x {h:.1f} mm, {len(fonts)} embedded fonts, thinnest line {thin:.2f} pt, text: {words}")


if __name__ == "__main__":
    names = sys.argv[1:] or sorted(p.stem for p in OUT.glob("F*.pdf"))
    for n in names:
        check(n)
