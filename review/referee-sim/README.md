# referee-sim: simulated peer review for The Journal of Geometric Analysis (gate G7)

Five simulated referees each reviewed the built manuscript independently. Each was given only the
PDF: no repository, proof files, scripts, earlier reports, or account of how the paper was
produced. Each was allowed to fetch published literature headlessly and to run its own code in a
git-ignored scratch folder. This session wrote reviews only; the manuscript, figures, code and data
are unchanged.

## Input

| item | value |
|---|---|
| source | `paper/jga/manuscript.tex` at commit `8a9ebf0` (origin/main) |
| build | `latexmk -pdf -outdir=build` in `paper/jga/` (0 LaTeX errors) |
| PDF given to the referees | `review/referee-sim/_input/manuscript.pdf` (git-ignored) |
| SHA-256 | `236500606921bb46bccf904d62f7033beef8912ddbe781fe40e4229dd7049223` |
| pages | 56 |

The SHA-256 is of this particular build. pdfTeX writes the creation date into the file, so a rebuild
of the same source gives a different hash.

## Reports

| folder | role |
|---|---|
| `spectral-geometer/REPORT.md` | (a) heat invariants of orbifolds, cone coefficients, Theorems A-C, signatures, novelty |
| `geometric-analyst/REPORT.md` | (b) locality, trace-formula extension, exponential bound, Teichmüller dimension, stability |
| `number-theorist/REPORT.md` | (c) triangular-pillow threshold, degeneracy curve, isolation, counting, revised conjecture |
| `numerical-analyst/REPORT.md` | (d) eigenvalue computations, Bolza benchmark, error budgets, experiments, reproducibility |
| `handling-editor/REPORT.md` | (e) scope, significance, exposition, references, guidelines, desk-reject probability |

The synthesis, with each FATAL and MAJOR issue checked against the repository, is
[`G7-VERDICT.md`](G7-VERDICT.md).

Each referee's `scratch/` folder holds its recomputations. These folders are git-ignored.
