# referee-round-3: third pre-submission referee round for the Annals of Global Analysis and Geometry

Purpose: decide whether `paper/jga` is ready to submit to AGAG after the wave-2 revision
(`paper/jga/WAVE2-CHANGES.md`: Section 4, Theorem 4.13, the two appendices restored, Table S1,
neutral paths). Gate (see `VERDICT.md`): (i) no confirmed MAJOR or FATAL issue; (ii) every theme that
recurred in earlier rounds (significance, length, attribution, proofs outside the paper) judged
resolved; (iii) the AGAG editor sends the paper to review with desk-reject probability at most 10%;
(iv) at least four of five reviewers recommend minor revision or accept, and no remaining "major" is
about substance. Only files under `review/referee-round-3/` were written in this round.

## Input (git-ignored in `_input/`)

Built from the sources of commit `09f9019` (the commit that adds Section 4 and the appendices;
`bb5bcb3` and later change only the suite, the data manifest and this directory) with
`latexmk && latexmk` in `paper/jga/` and `latexmk note.tex` in `paper/arith/`; 0 LaTeX errors, 0
undefined references or citations, no overfull box above 1 pt (one of 0.8 pt in the manuscript).
pdfTeX embeds a creation date, so a rebuild gives different hashes. The PDF metadata carry the title,
the six authors and the keywords, and no other attribution.

| file | role | pages | SHA-256 |
|---|---|---|---|
| `_input/manuscript.pdf` | manuscript (all five reviewers) | 48 | `c829fee3c0979fc1c93fa7c08a53fd9e426cc1de97db5ccaf190047968cd7325` |
| `_input/supplement.pdf` | electronic supplement (all five) | 15 | `1a499896595d3e820d1a603ab64d049e51f4db930eed6c85c809b3b2df1027aa` |
| `_input/note.pdf` | disclosed related manuscript (the editor only) | 12 | `9850992e107d6ef0791da03553ec9f663a53de145db7a95cdf902233ef6409d2` |

Each reviewer was a separate subagent told to open only the PDFs it was assigned: no repository,
proofs, scripts, earlier reviews, records of the revision, or account of how the paper was produced.
Each could fetch published literature headlessly (no browser, no personal data or address sent) and run
its own code in its own git-ignored `scratch/` (package installs only in a virtual environment there).
Each was told: "Review for Annals of Global Analysis and Geometry. Be rigorous and demanding; find every
reason not to accept, and say plainly what is good. Treat the marked placeholders (author
contributions, AI-use statement, Zenodo DOI) as known. Read rendered page images, not only extracted
text, before reporting a typographical, sign or figure error." The report format is: summary;
significance; correctness and what was recomputed; MAJOR; MINOR; presentation; recommendation with
confidence; what resolves each issue.

## Personas

All five are new relative to rounds 0-2 (`review/referee-sim/`, `referee-round-1/`,
`referee-round-2/`), which used a journal editor for JGA, spectral and trace-formula analysts of other
profiles, a PTE combinatorialist and a JGA regular referee.

| folder | persona |
|---|---|
| `a-agag-handling-editor/` | (a) AGAG editorial-board member handling the submission: scope, significance for this journal's readership, length, presentation, overlap with the disclosed companion note; gives a desk-reject probability |
| `b-orbifold-spectral-geometer/` | (b) spectral geometer on orbifold heat invariants and isospectrality in the Dryden-Gordon-Greenwald-Webb-Stanhope line; checks novelty against that literature and every statement on heat coefficients and signatures |
| `c-hyperbolic-trace-formula-analyst/` | (c) analyst of the Selberg trace formula, heat kernels and eigenvalue counting on hyperbolic surfaces; checks Theorem 4.13 and every proof a main result depends on |
| `d-pte-combinatorialist/` | (d) combinatorialist and computational number theorist on Prouhet-Tarry-Escott and equal-power-sum problems; checks every PTE statement, search and table |
| `e-rigour-and-citations/` | (e) rigour-and-citations referee: proofs, every figure against its caption, numbering and notation, every citation fetched and checked |

Each folder holds `REPORT.md`. The synthesis is [`VERDICT.md`](VERDICT.md).
