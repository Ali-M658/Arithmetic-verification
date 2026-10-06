# referee-round-1: pre-submission referee round for The Journal of Geometric Analysis

Purpose: decide whether `paper/jga` is ready to submit. Gate: no confirmed MAJOR or FATAL issue from
any reviewer, and every recommendation "minor revision" or "accept". This round is new relative to
`review/referee-sim/` (round 0; personas there: spectral geometer, geometric analyst, number theorist,
numerical analyst, handling editor). Only files under `review/referee-round-1/` were written; the
manuscript, figures, code and data are unchanged.

## Input (git-ignored in `_input/`)

Built at repository commit `8d0761533d1026102668a5a39ad6d49991beab56` with `latexmk -pdf`
(`paper/jga/` for the manuscript and supplement, `paper/arith/` for the note); 0 LaTeX errors.
pdfTeX embeds a creation date, so a rebuild gives different hashes.

| file | role | pages | SHA-256 |
|---|---|---|---|
| `_input/manuscript.pdf` | manuscript (all five reviewers) | 35 | `b098f5ca0b63147665c94d8e4d9739dcdf26973a66f03fe1b9af39abbb37fee6` |
| `_input/supplement.pdf` | electronic supplement (all five) | 8 | `3ff4e56e31e2376dbc8b460052e65720d5c9139230e379078f96b3bb1e735f16` |
| `_input/note.pdf` | disclosed companion note (editor only) | 12 | `8c0e507a1a7ff5f9409422bb010174f97234d458e4195b83a656c71bb10d8d7b` |

Each reviewer saw only the PDFs it was assigned: no repository, proofs, scripts, earlier reviews, or
account of how the paper was produced. Each could fetch published literature headlessly and run its
own code in its own git-ignored `scratch/`. Placeholders (author contributions, AI-use statement,
Zenodo DOI) were declared known and not counted.

## Personas

| folder | persona |
|---|---|
| `a-inverse-spectral-sceptic/` | (a) senior spectral geometer working on inverse problems, sceptical that the topic matters |
| `b-trace-formula-analyst/` | (b) analyst expert in the Selberg trace formula and heat kernels on hyperbolic surfaces and orbifolds |
| `c-pte-combinatorialist/` | (c) combinatorialist expert in Prouhet-Tarry-Escott and equal-power-sum problems |
| `d-jga-rigour-referee/` | (d) geometric analyst who reviews for JGA regularly; rigour, completeness of proofs, citation accuracy |
| `e-handling-editor/` | (e) JGA handling editor: desk rejection versus review (scope, significance, length, overlap with the companion note) |

Each folder holds `REPORT.md`. The synthesis is [`VERDICT.md`](VERDICT.md).
