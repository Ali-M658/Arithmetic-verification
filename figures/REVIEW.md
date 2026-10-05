# REVIEW: checks of the nine figures and the referee-style review

## 1. Per-figure checklist

Every figure was rendered, looked at as a PNG, and checked against the list below.
`figures/src/checklist.py` runs the mechanical items. It writes deuteranopia, protanopia and
greyscale views of each figure to `figures/build/check_Fn.png`, and those were looked at too.

| item | how it is checked |
|---|---|
| legible at print size | 119 mm wide (asserted from the PDF). Ticks 9 pt, so log exponents are 6.3 pt; axis titles and panel letters 10 pt (SPEC.md). Thinnest line ≥ 0.35 pt, asserted (journal minimum 0.3 pt) |
| colour-blind and greyscale | Only the two pillow hues are chromatic. Their ΔE is ≥ 63 under every dichromat simulation and their L* differs by 35. Every series that carries a hue also differs by weight, line style or marker. Ordered categories use grey ramps |
| no forbidden text | Every text string of each PDF is listed by `checklist.py`: only tick labels, axis titles, panel letters, and glyph fragments of Computer Modern math |
| consistent typography and hues | One style module (`figstyle.py`) and one palette file (`palette.json`) for every figure |
| numbers asserted against data | Each `src/Fn.py` asserts before drawing (see its docstring). `run_all.sh` reruns all of them |
| metadata | No creator, producer or date in any PDF and no software tag in any PNG, asserted |

Results, vector figures. F2, F3, F4, F5, F7, F8 and F9 pass every item. F1 and F6 are in
section 3.

## 2. Referee-style review (vector figures)

A separate reviewer was given only `figures/out/` and `captions.tex`. It critiqued F2–F5 and
F7–F9 as a referee would; F1 and F6 did not exist yet. It made 23 findings. Each finding is
listed with what was done about it.

| # | fig | finding (short) | disposition |
|---|---|---|---|
| 1 | F5 | The circles sit above the noise kink, not at it. | **Kept the position, fixed the caption.** A circle marks the emergence time of `numerics/moduli/REPORT.md`: the first t where the predicted difference exceeds 10 × (budget + 10⁻¹²). The caption now says this. |
| 2 | F5 | "Thin dashed" prediction and "dotted" budget look alike. | **Fixed.** The budget is now a shaded region, and the caption says the prediction coincides with the data above the noise. |
| 3 | F9 | The isosceles curve starts at S ≈ 70, although (2,8,8) and (3,3,12) are isosceles. | **Fixed; this was a real error.** The curve had kept only the multiples k ≥ 4 of the notes' counting argument. It now counts every hyperbolic pair of the family (base pair D₁,₄ = {(2,8,8), (3,3,12)}). The script asserts 2917 pairs with S ≤ 4800, as `families.py` reports, and still checks the k ≥ 4 subset against `families.txt`. |
| 4 | F7 | It is unclear which stratum each dot and circle belongs to. | **Fixed.** A dashed line joins each first-overlap dot to the first-collision circle of the same pair. |
| 5 | F7 | Strata 5–8 tangle; too many greys. | **Fixed in part.** The R axis is now logarithmic, which separates the low strata, and the dots are larger. All seven strata are kept (the brief asks for p = 2..8). |
| 6 | F4 | The log y-axis to 3000 squashes the data; K can't be read. | **Fixed.** The y-axis is linear 0–10 with integer ticks, and the upper bound runs off the top. |
| 7 | F2 | The oblique hyperboloid view distorts angles; the pillow is tiny; moiré at the rim. | **Fixed in part.** The brief asks for the hyperboloid model, so it stays. The cap radius went from 2.8 to 2.4, which contains both pillows (farthest vertex 2.158) with a margin of at least 0.2, asserted. The pillow is now large and the rim moiré is gone. The caption names the view (oblique orthographic). |
| 8 | F3 | "U = {1,15} padded by one order 1" is ambiguous. | **Fixed.** The caption now reads "U = {1,15}, i.e. 15 padded by one order 1", and it names the tones (black, grey). |
| 9 | F3 | Cramped rows; "0" has no tick; labels nearly touch. | **Fixed.** More space before (b), a tick at 0, and each row is ticked only at its own points. |
| 10 | F5 | A divergent series has no "sum". | **Fixed.** The caption now says "cone-point contribution of the trace formula" and "partial sums of its small-t expansion". |
| 11 | F5 | The dashed curve is hidden under D; the partial-sum greys are too close. | **Fixed.** The cone-point curve is drawn on top in a light tone, and the ramp now runs from light to dark. |
| 12 | F8 | Diamonds sit at different heights; δ_cert is a δ value. | **Fixed.** The caption says the diamonds sit on each curve at δ = δ_cert, and that the certificate is nearly sharp for (2,8,8) and (4,4,4). The δ_cert values are asserted equal to `threshold_results.json`. |
| 13 | F8 | No y tick near 10⁰. | **Fixed.** y ticks every two decades, up to 10⁰. |
| 14 | F4 | K_mult and Sig are not defined in the caption; the x label disagrees with the caption. | **Fixed.** K_mult is defined in one clause, and the x label is now "s = Area/2π". |
| 15 | F4 | Overplotted dots; the lower bound starts at s = 3. | **Bound fixed, dots kept.** The caption gives the hypothesis A ≥ 6π for the start at s = 3. The dots are not jittered: every class value is an integer, and jitter would misplace them. |
| 16 | F4/F7/F9 | s and S clash. | **Not changed.** Both are the paper's notation (theory/CONVENTIONS.md: s = Area/2π, S = Σ mᵢ). |
| 17 | F4/F7/F9 | "Split disc" is undefined, and is missing from F9's caption. | **Fixed.** "Split disc (half dark, half light)" is defined in each caption, and F9's caption mentions it. |
| 18 | F9 | Emphasis reversed (N thin); c undefined. | **Fixed.** N(S) is heavy, the isosceles count thin, and c is "fitted". |
| 19 | F9 | The q fit spans less than a decade. | **Fixed (wording).** The caption calls it an empirical fit. The ±0.5 comes from the block-bootstrap of `exponent_fits.txt`. |
| 20 | F2 | "Dark/light tone" clashes with the pillow-pair meaning. | **Fixed.** The caption now says "deep shade" and "pale shade" of the pillow's hue. |
| 21 | F7 | Circle at the frame edge; small dots; integer S. | **Fixed.** x runs to 126, the dots are larger, and the caption says the bounds are joined across integer S. |
| 22 | all | Ticks 8 pt, exponents 5.6 pt. | **Fixed.** Ticks are 9 pt (exponents 6.3 pt), and titles and letters 10 pt. Exponents stay below 8 pt because mathtext fixes superscripts at 0.7 of the font size. Superseded in part by row 24. |
| 23 | F3/F4/F5 | Long caption sentences. | **Partly.** Each caption is still at most three sentences, and the F3 argument is shorter. The rest is left to the author's edit of the text. |
| 24 | F4/F5/F8/F9 | Log axes: exponents are 6.3 pt. | **Fixed where the range allows.** Plain decimal labels (`figstyle.decimal_log_ticks`), all 9 pt: F4 x (0.1 to 1000), F5 x in both panels (0.01, 0.1), F9(b) x (100, 1000) and y (0.01 to 10). F7 and the F1 colour bar already had plain labels. **Powers kept** on F5(b) y (10⁻¹⁵ to 1) and on both F8 axes (10⁻¹⁴ to 10⁻¹, 10⁻¹⁴ to 10). There, decimals would run to 16 digits. These exponents are the only tick text below 8 pt (6.3 pt). |

## 3. F1 and F6 (Blender)

**Rendered on 2026-10-05, 10:05–10:20 IST**, under the new machine-safety guard (SPEC section 5:
`memory_pressure -Q` free ≥ 20%, `--threads 2`, one render at a time, 10-minute limit). Memory
free was 34–54% at every check. Each figure took under 30 s.

The swap-based guard blocked five attempts between 03:32 and 06:35 IST at 87–95% swap. Swap
stays allocated on macOS after the memory pressure has passed, so it was the wrong signal, and
it was replaced. An orphaned `python3 -` process (PID 65651, from an earlier render attempt in
`figures/src`) was stopped before rendering.

**Two render bugs, fixed before the figures could be built.**
- **Unparseable bounds:** under numpy 2, `repr(np.float64)` is `'np.float64(…)'`, which
  `render_pillow.py` cannot parse. The colour-scale bounds are now passed as plain floats.
- **Silent script failures:** Blender exited 0 after a Python error. It now runs with
  `--python-exit-code 1`.
- **Stale cache:** the render cache now includes the arguments (`.args` stamp), so a changed
  argument re-renders.

**Own check against SPEC and palette E.**
- Palette E holds: F1 uses only the lajolla sequential map, with no pillow hue on the heat
  surface. The F6 geodesic is ink, chosen by rule 2 (contrast 11.2 against 6.1 for the dark hue).
- `checklist.py F1 F6`: 119 mm wide, fonts embedded, thinnest line ≥ 0.5 pt.

The first renders had three faults, all fixed:

| # | Fig | Finding | Resolution |
|---|-----|---------|------------|
| O1 | F1 | Colour-bar label clipped at the bottom edge. | **Fixed.** The bar and panels moved up. |
| O2 | F1, F6 | Renders sat in visible grey boxes (the L* 97 render ground). | **Fixed.** `blender_jobs.crop_common` paints the flat ground white. |
| O3 | F1, F6(a) | F1's two pillows were framed at different scales; F6(a) objects were small in large tiles. | **Fixed.** F1 passes one `--ortho` scale for both pillows. Both figures crop to one common box size, each object centred, so one scale is kept. |

**Referee pass** (a separate agent given only `F1.png`, `F6.png` and the two captions):

| # | Fig | Finding | Resolution |
|---|-----|---------|------------|
| R1 | F6(b) | Sectors cannot be told apart, so "only lines of different sectors cross" cannot be checked. | **Caption reworded, figure kept.** The caption now says crossing lines belong to different sectors (an explanation, not a claim to verify). Coding eight sectors would need eight hues or dash styles, which breaks the grey-only rule for non-pillow data (SPEC section 4). Small multiples would lose the one-panel spectral flow. |
| R2 | F6(b) | The headline fall of λ₁ (4.12 → 0.43) is about 3% of a linear 0–120 axis. | **Fixed.** The y axis is square-root (ticks 0, 1, 5, 10, 20, …, 120), and λ₁ is a heavy ink line; the other branches are mid grey. The caption names both. |
| R3 | F1 | The 3-D shading darkens the surface, so it cannot be read against the colour bar. | **Fixed.** F1 uses shading weight 0.10 instead of 0.30, so the brightness change is at most 10%. Some shading is kept to show the puffed shape. |
| R4 | F1 | Cone points are not labelled with their orders; the darkest tip is a sliver. | **Caption.** SPEC section 2 allows no in-figure text beyond axes and letters, so the caption names the sharp dark tips (orders 8, 12) and the blunt corners (orders 2, 3). The narrow dark tip is how the kernel concentrates at t = 0.02, and is kept. |
| R5 | F1 | Each pillow looks like one flat triangle. | **Caption.** "Seen from above (only the upper sheet shows)". |
| R6 | F6(a) | Members are not labelled with ϑ and length. | **Caption.** "From left to right"; in-figure text is excluded by SPEC section 2. |
| R7 | F6(a) | The four cone points are not marked. | **Caption.** "The four corners are the cone points". |
| R8 | F6 | Nothing links (a) to (b); "all eight moduli have grid lines". | **Caption.** The referee is wrong that all eight have lines: they are drawn only at the four ϑ of (a). The caption now says so. |
| R9 | F1 | The bar starts at 1 and clips the interior value 0.993. | **Not changed.** The bar starts at the data minimum, 0.9934 (`F1.data()`), so nothing is clipped. A tick at 6 was added. |
| R10 | F1 | Fraktur 𝔥 on the bar, plain h in the caption. | **Not changed.** The caption uses `\mathfrak h`; the referee was shown a plain-text copy. |
| R11 | F1 | Dead space; label (b) far from its pillow. | **Partly.** Each pillow is centred in an equal column (O3). The letters stay at the fixed column corner (SPEC section 2). |

## 4. Suite

`PYTHON=.venv/bin/python code/run_all.sh --quick`, in a fresh venv built from
`requirements.txt`, on 2026-10-05: **36 passed, 0 failed, 9 skipped** (52 min, under a load
average of about 10). The new stages are "figures data F4 F7 F8" (PASS), "figures vector F2-F5
F7-F9" (PASS, byte-identical rebuild of the committed PDFs and PNGs) and "figures Blender
renders F1 F6" (SKIP, with its reason).

Rerun on 2026-10-05 after the decimal log-axis labels (row 24), same venv: **36 passed, 0 failed,
9 skipped** (28 min). "figures vector F2-F5 F7-F9" passes with the new F4, F5 and F9 PDFs and PNGs.
DATA-MANIFEST.md is unchanged (`admin/build_data_manifest.py --check`: current).
