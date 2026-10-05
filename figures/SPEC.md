# SPEC: format of the nine figures

Every value below was read from a fetched source on 2026-10-04, or measured. The value is
followed by its source. Third-party pages and PDFs were kept in the git-ignored
`figures/_fetched/`. `figures/style/figstyle.py` holds these values as constants.

## 1. Journal requirements (The Journal of Geometric Analysis, Springer)

**Source.** The JGA "Submission guidelines" page,
<https://link.springer.com/journal/12220/submission-guidelines>, section "Artwork and
Illustrations Guidelines". link.springer.com answers headless requests with a JavaScript
challenge, so the page was read from the Internet Archive capture of 2025-12-04
(<https://web.archive.org/web/20251204070959/https://link.springer.com/journal/12220/submission-guidelines>).

| item | requirement (quoted or exact) | our value |
|---|---|---|
| figure width | "For small-sized journals, the figures should be 119 mm wide and not higher than 195 mm." (Large-sized journals: 84 mm or 174 mm, height up to 234 mm.) | **119 mm wide, height ≤ 195 mm.** JGA is a small-sized journal, see below. |
| line art | "All lines should be at least 0.1 mm (0.3 pt) wide"; bitmap line art at least 1200 dpi | thinnest line 0.35 pt; line art is vector |
| halftone | at least 300 dpi | not used alone |
| combination art (halftone with lettering or line drawing) | at least 600 dpi | **Blender panels: 600 dpi at final size**, vector lettering on top |
| colour | RGB, 8 bits per channel; the main information must survive black-and-white printing | RGB; every figure is checked in greyscale (CIE L*) |
| formats | vector: EPS preferred; halftone: TIFF; fonts embedded | **PDF with embedded fonts** (the standard for a LaTeX submission); EPS copies on request with `pdftops -eps` |
| lettering | "Helvetica or Arial", "about 2–3 mm (8–12 pt)", minimal size variance, no titles or captions in the figure | **8 pt ticks, 9 pt axis titles and panel letters**; font: see section 2 |
| panel parts | lowercase letters (a, b, c) | "(a)", "(b)" in the top-left corner of each panel |
| captions | in the manuscript text, not in the figure; every element identified in the caption | `figures/captions.tex` |
| accessibility | "Patterns are used instead of or in addition to colors"; lettering contrast at least 4.5:1 | two cues per series (hue + line style or marker fill); ink L* 15 on white (contrast > 15:1) |

**Why 119 mm: JGA is a small-sized journal.** The open-access JGA article
doi:10.1007/s12220-025-02246-3 (publisher PDF, Internet Archive capture of the
link.springer.com PDF) has 155 × 235 mm pages. Its text spans x = 17.9 to 136.9 mm, a text
block of 119 mm, measured with PyMuPDF. That matches the "small-sized" rule.

**Departure from the guideline's font.** The guideline suggests Helvetica or Arial. The
author's figure rules require one font matching the manuscript's math font. `paper/main.tex`
uses the `article` class with no font package, so that font is Computer Modern. The figures use
Computer Modern (matplotlib's bundled `cmr10` and the `cm` math set), embedded as TrueType
(`pdf.fonttype 42`). Sizes stay within 8 to 12 pt, as the guideline asks.

## 2. Style constants (figures/style/figstyle.py)

| constant | value |
|---|---|
| width | 119 mm for every figure; height chosen per figure, ≤ 195 mm |
| font | Computer Modern, 8 pt ticks, 9 pt axis titles, 9 pt panel letters |
| line weights | hair 0.35 pt, thin 0.5 pt, axis 0.6 pt, regular 0.9 pt, heavy 1.4 pt |
| markers | 3.0, 4.2, 5.5 pt |
| raster | 600 dpi at final size (combination art) |
| metadata | creator, producer and creation date removed from every PDF; software tag removed from every PNG |
| in-figure text | axis titles, tick labels and panel letters only; everything else is in the caption |

## 3. Colour sources and licences

All tables are fetched by `figures/style/fetch_third_party.py`. The extracted tables are
committed to `figures/style/third_party/`, with the source URLs and SHA-256 hashes in
`SOURCES.json`. `--check` re-fetches and compares. No colour value is typed by hand.

| material | source | licence | citation |
|---|---|---|---|
| Scientific colour maps 8.0.1 (batlow, lajolla, lipari, oslo and others) | Zenodo record 8409685, `ScientificColourMaps8.zip`, SHA-256 `fe8ccf8e…fc02c` | MIT (Zenodo record metadata) | F. Crameri, *Scientific colour maps*, version 8.0.1, Zenodo (2023), doi:10.5281/zenodo.8409685; F. Crameri, G. E. Shephard, P. J. Heron, "The misuse of colour in science communication", *Nat. Commun.* 11 (2020) 5444, doi:10.1038/s41467-020-19160-7 |
| viridis | github.com/BIDS/colormap, `option_d.py` (the table that became matplotlib's viridis) | CC0 1.0 (`LICENSE.txt` of the same repository) | N. Smith, S. van der Walt, E. Firing, "viridis" (2015), BIDS/colormap |
| CVD simulation matrices (protanopia, deuteranopia, tritanopia; severity 1.0) | Table 1 of the authors' page, <https://www.inf.ufrgs.br/~oliveira/pubs_files/CVD_Simulation/CVD_Simulation.html> | published research data, used to check our figures and not redistributed in the figures | G. M. Machado, M. M. Oliveira, L. A. F. Fernandes, "A physiologically-based model for simulation of color vision deficiency", *IEEE TVCG* 15(6) (2009) 1291–1298, doi:10.1109/TVCG.2009.113 |

The matrices act on linear RGB (sRGB decoded by IEC 61966-2-1). The greyscale check uses CIE
L* (CIE 15:2004, D65). Both are in `figures/style/colourtools.py`.

If the chosen palette is a Crameri map, the paper should cite Crameri (2023) and Crameri et al.
(2020) in the acknowledgements or in the caption of F1.

## 4. Palette rules (figures/style/palette.json)

**Chosen palette: E (batlow-lajolla), set at gate G6 on 2026-10-05.**
- Sequential map: Crameri lajolla, reversed.
- (2,8,8): batlow at 0.20, `#185562`, L* 33.
- (3,3,12): batlow at 0.70, `#e09651`, L* 68.
- Pair separation ΔE: 78 normal, 75 deuteranopia, 63 protanopia, 77 tritanopia.

**Rules for the final figures (author, G6):**
1. The sequential map is only for continuous scalar fields: heat-kernel colourings,
   densities and colour bars. Ordered categories, such as the F7 strata, use a neutral grey
   ramp built from the L* neutrals. The pillow hues are then the only chromatic elements of a
   plot.
2. A pillow hue is never drawn on top of a heat-coloured surface. A curve on a rendered surface
   (for example the shortest geodesics in F6) uses the dark pillow hue or neutral ink, whichever
   contrasts more with the surface. It never uses the light hue.
3. The F9 lower bound is the exact count of the isosceles family, which is a rigorous lower
   bound at every S. The caption states its (c_iso + o(1)) S log S growth. No asymptotic curve
   is drawn.

**General rules:**

- One sequential, perceptually uniform map for every heat-kernel or density colouring, Blender
  included. It is reversed so that a larger value carries more ink ("darker = larger").
- One pair of hues for the two central pillows: (2,8,8) is the dark hue and (3,3,12) the light
  hue, both sampled from the fetched tables at the stated positions. The candidates were chosen
  so that the pair differs by at least 27 in L* (greyscale-safe) and by at least 50 in ΔE under
  each dichromat simulation.
- Neutrals are defined by their L*: ink 15, dark 40, mid 62, light 82, faint 92, render
  background 97.
- Light tones of a hue (F2's mirror triangle) are the hue mixed 55% with white.

## 5. Blender renders

Workbench engine with 2 threads. Two passes are rendered: a flat, unlit pass with the exact
vertex colours, and a studio-lit pass of a uniform grey surface. `figstyle.shade` multiplies
them, with the shading allowed to darken by at most 30% (F1, whose surface brightness is the colour
scale, uses 10%). There is no specular highlight,
outline, cavity, shadow or depth of field. The background is neutral (L* 97), and the
'Standard' view transform keeps the colours as computed.

**Machine-safety guard** (`src/blender_jobs.py`, used for every render):

- Before each render, run `memory_pressure -Q` and read "System-wide memory free percentage".
  Render only if it is at least 20%. Otherwise re-check every 2 minutes, for at most 30
  minutes, then report and stop (`MemoryBusy`).
- Blender runs with `--threads 2`, one render at a time, never in parallel.
- A render that runs longer than 10 minutes is stopped and reported (`RenderTimeout`).

Swap use is not the signal. On macOS swap stays allocated after the memory pressure has passed,
so the earlier rule (wait while `sysctl vm.swapusage` exceeds 75%) blocked renders on an idle
machine. It was replaced on 2026-10-05.
