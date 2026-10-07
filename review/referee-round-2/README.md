# referee-round-2: second pre-submission referee round for The Journal of Geometric Analysis

Purpose: decide whether `paper/jga` is ready to submit. Gate: no confirmed MAJOR or FATAL issue from
any reviewer, and every recommendation "minor revision" or "accept". Only files under
`review/referee-round-2/` were written in this round; the manuscript, figures, code and data are
unchanged by it.

## Input (git-ignored in `_input/`)

Built from the sources of commit `d7ed90d` (the figure-restore revision: F1, F2, F6 and the
admissibility lemma back in the paper; two-sentence captions) with `latexmk && latexmk` in
`paper/jga/` and `latexmk note.tex` in `paper/arith/`; 0 LaTeX errors, 0 undefined references or
citations, 0 overfull boxes. pdfTeX embeds a creation date, so a rebuild gives different hashes.

| file | role | pages | SHA-256 |
|---|---|---|---|
| `_input/manuscript.pdf` | manuscript (all five reviewers) | 37 | `8ca2260dece299c882aa67e77ead98bd716f003ad9ab243994ab4d5c62b155c1` |
| `_input/supplement.pdf` | electronic supplement (all five) | 12 | `0b7bb3d8094145bd8d174a2b1cf00ca12ce07b669500bb7525bd693280b06b36` |
| `_input/note.pdf` | related manuscript disclosed by the authors (editor only) | 12 | `148103e22532e8a5dc67e9f3fd49781e515c20fae474a9c20a64384d43fb1441` |

Each reviewer was a separate subagent told to open only the PDFs it was assigned: no repository,
proofs, scripts, earlier reviews, records of the revision, or account of how the paper was produced.
Each could fetch published literature headlessly (arXiv, Crossref, zbMATH Open, author pages; no
browser, no personal data sent) and run its own code in its own git-ignored `scratch/` (package
installs only in a virtual environment there). Each was told: "Review for The Journal of Geometric
Analysis. Be rigorous and demanding; find every reason not to accept, and say plainly what is good.
Treat the marked placeholders (author contributions, AI-use statement, Zenodo DOI) as known and do
not count them as defects. Read rendered page images, not only extracted text, before reporting a
typographical, sign or figure error."

## Personas

The five roles are those the brief prescribes; the individuals are new. Round 0
(`review/referee-sim/`) used a spectral geometer, a geometric analyst, a number theorist, a numerical
analyst and a handling editor; round 1 (`review/referee-round-1/`) used a generic inverse-spectral
sceptic, a trace-formula analyst, a PTE combinatorialist, a JGA rigour referee and a handling editor.
Round 2 gives each role a different background and reading habit:

| folder | persona |
|---|---|
| `a-isospectral-constructor/` | (a) senior spectral geometer on inverse problems, known for constructing isospectral non-isometric manifolds and orbifolds (Sunada, transplantation) and for wave-trace and length-spectrum results; sceptical that counting heat invariants matters when the full spectrum is available |
| `b-orbifold-trace-formula-analyst/` | (b) analyst of the Selberg trace formula for cofinite groups with elliptic elements and of small-time heat asymptotics at cone points; checks that every proof the main results depend on is complete where it appears, treating unproved "standard" steps as gaps |
| `c-equal-power-sums-combinatorialist/` | (c) combinatorial number theorist who computes PTE, ideal and symmetric solutions and multigrades; exacting about "equivalent to an open problem" versus "related", and about search bounds and counting conventions |
| `d-jga-regular-referee/` | (d) geometric analyst (PDE on conical and singular spaces) who referees for JGA several times a year; rigour, completeness of proofs, citations spot-checked against sources, figures checked one by one against captions |
| `e-jga-handling-editor/` | (e) JGA editorial-board member in global analysis and spectral geometry deciding desk rejection versus review: scope, significance, length, figures, overlap with the disclosed companion note; gives a desk-reject probability |

Each folder holds `REPORT.md`. The synthesis is [`VERDICT.md`](VERDICT.md).
