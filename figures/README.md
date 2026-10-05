# figures/

The nine figures of "How much of a hyperbolic orbifold does heat hear?". Each figure has one
script. A script asserts every number it shows against committed data, or against an exact
computation, before it draws anything. Run with `--check` to get the assertions alone.

| Figure | Paper section | Script | Data | Output |
|---|---|---|---|---|
| F1 pillows coloured by the heat-kernel diagonal | Introduction | `src/F1.py` (+ `src/pillow_mesh.py`, `src/render_pillow.py`) | `numerics/data/heat_kernel_diagonal.npz`, `numerics/data/heat_trace_difference.csv` | `out/F1.pdf` (Blender raster, 600 dpi, vector colour bar) |
| F2 triangle-group tilings on the hyperboloid | 2 | `src/F2.py` | exact: `numerics/geometry.py` (triangle) and the reflection group | `out/F2.pdf` |
| F3 the mirror argument of Theorem S | 3 | `src/F3.py` | exact: `theory/signatures/sig_common.py` | `out/F3.pdf` |
| F4 coefficients needed against area | 3 | `src/F4.py` | `data/f4_area_classes.csv`, `data/f4_construction.csv` | `out/F4.pdf` |
| F5 two timescales | 4, 7 | `src/F5.py` | `numerics/data/heat_trace_difference.csv`, `numerics/moduli/data/trace_differences.csv`, `numerics/moduli/data/summary.json`; exact `d_j` from `theory/stability/stab_common.py` | `out/F5.pdf` |
| F6 moduli family and eigenvalue flow | 4, 7 | `src/F6.py` (+ `src/quad_mesh.py`, `src/render_pillow.py`) | `numerics/moduli/data/geometries.json`, `eigenvalue_flow_orbifold.csv`, `eigenvalue_flow_sectors.csv` | `out/F6.pdf` (Blender raster, 600 dpi, vector plot) |
| F7 least-order strata in the (S, R) plane | 5 | `src/F7.py` | `data/f7_strata.csv`, `data/f7_overlap.csv` | `out/F7.pdf` |
| F8 recovery error against coefficient error | 6 | `src/F8.py` | `data/f8_recovery.csv`, `data/f8_thresholds.csv`, `theory/stability/threshold_results.json` | `out/F8.pdf` |
| F9 the curve C_{27/2} and the degeneracy count | 8 | `src/F9.py` | `theory/diophantine/data/{per_S,groups}.csv`, `exponent_fits.txt`, `families.txt` | `out/F9.pdf` |

Every `out/Fn.pdf` has a `out/Fn.png` preview. The captions are in `captions.tex`, one macro per
figure (`\figcapOne` … `\figcapNine`).

## Rebuild

Use the interpreter of the suite (`requirements.txt`, which pins matplotlib and pillow).

```bash
python3 figures/gen/gen_f4_area_classes.py      # F4 data (about 1-2 min)
python3 figures/gen/gen_f7_strata.py            # F7 data
python3 figures/gen/gen_f8_recovery.py          # F8 data (under a minute)
python3 figures/src/build_vector.py             # F2-F5, F7-F9, and the F1/F6 assertions
python3 figures/src/F1.py                       # Blender (blender on PATH), cached in figures/build/
python3 figures/src/F6.py
python3 figures/src/contact_sheet.py            # the G6 palette proof (figures/proofs/)
```

`code/run_all.sh` runs the first four commands. The stages are "figures data F4 F7 F8" and
"figures vector F2-F5 F7-F9". The rebuilt CSVs, PDFs and PNGs must be byte-identical to the
committed ones. The F1 and F6 renders are skipped by the suite, with a reason, and their data
assertions still run.

Blender renders run one at a time, with 2 threads and the Workbench engine. Before each render
`memory_pressure -Q` is read: the render starts only if the system-wide memory free percentage
is at least 20%. Otherwise it re-checks every 2 minutes and gives up after 30 minutes. A render
that runs longer than 10 minutes is stopped (`src/blender_jobs.py`, SPEC section 5).

## Layout

| path | content |
|---|---|
| `gen/` | generators of the missing figure data (F4, F7, F8). They import the theory scripts unchanged and assert against their committed outputs |
| `data/` | the generated CSVs (registered in `DATA-MANIFEST.md`) |
| `src/` | one script per figure, plus the mesh builders, the Blender render script and the contact sheet |
| `style/` | the style system. `palette.json` is the single palette definition; `figstyle.py` is the matplotlib side and `blender_palette.py` the Blender side; `colourtools.py` does CIELAB, colour-vision-deficiency simulation and greyscale; `third_party/` holds the fetched colour tables (`fetch_third_party.py --check`) |
| `out/` | the figures |
| `proofs/` | the G6 contact sheet and `CANDIDATES.md` |
| `SPEC.md` | journal requirements (with sources), style constants, colour licences, palette rules |
| `REFERENCES.md` | the study of published figures |
| `REVIEW.md` | the referee-style review of the figure set and how each finding was handled |
| `build/`, `_fetched/` | not committed: meshes, renders and fetched third-party material |

## Faithfulness notes

- **Stylised shapes.** The 3D shapes of F1 and F6 are not isometric embeddings. Each sheet is
  the polygon in Poincaré-disk coordinates, which is conformal, so the cone angles are exact,
  lifted by √u with −Δu = 1. The colours and the drawn geodesic are exact data on that shape.
- **Withdrawn density law.** No figure shows the withdrawn c·S² density law. F9(b) shows the
  empirical S(log S)^𝔮 fit and the exact isosceles-family count, which is a rigorous lower
  bound at every S, as `review/audit/G5-VERDICT.md` and SPEC section 4, rule 3 require.
- **F4 lower bound.** The lower bound of F4 (Corollary N1) is drawn only where its hypothesis
  A ≥ 6π holds.
