# referee-round-4: pre-submission referee round for the Annals of Global Analysis and Geometry, two papers

Purpose: decide, separately, whether each of two papers is ready to submit to AGAG:

* **Paper A**: `paper/jga/manuscript.tex` with `supplement.tex`, "How much of a hyperbolic orbifold does
  heat hear?";
* **Paper B**: `paper/eigen/manuscript.tex`, "Finitely many eigenvalues determine the signature of a
  hyperbolic orbifold" (split off Section 4 of the round-3 manuscript).

The companion arithmetic note is `paper/arith/note.tex`. Gate (per paper; see `VERDICT-A.md`,
`VERDICT-B.md`): (i) no confirmed MAJOR or FATAL issue; (ii) every theme that recurred in earlier rounds
(significance, length, attribution, proofs outside the paper, overstated numerics) resolved for that
paper; (iii) the AGAG editor sends it to review with desk-reject probability at most 10%; (iv) at least
four of five reviewers recommend minor revision or accept, with no remaining "major" about substance.
If (i)-(iii) hold and (iv) fails only because a reviewer's "major" rests on writing-level items, the
paper is WRITING-ONLY. Only files under `review/referee-round-4/` were written in this round.

## Input (git-ignored in `_input/`)

Built from the sources of commit `defccde` with `latexmk` (run twice) in `paper/jga/` and
`paper/eigen/` and `latexmk note.tex` in `paper/arith/`; 0 LaTeX errors and 0 undefined references
or citations in all four logs; one overfull box of 0.8 pt in Paper B, none in the others. pdfTeX
embeds a creation date, so a rebuild gives different hashes. The PDF metadata carry the title, the six
authors and (for the three main documents) the keywords, and no other attribution.

| file | role | pages | SHA-256 |
|---|---|---|---|
| `_input/paperA-manuscript.pdf` | Paper A (all Panel A reviewers; Panel B editor) | 39 | `73d9c26dc31bda9061726de9a3ffd34f39b00e161f98a6b65af3153e46b42aee` |
| `_input/paperA-supplement.pdf` | Paper A supplement (as above) | 14 | `e1fd189bbe91ef436330099da6b33849140d4cb0ad6c3e564dff3d8a1f9ab9bb` |
| `_input/paperB-manuscript.pdf` | Paper B (all Panel B reviewers; Panel A editor) | 23 | `79de431c4b186cf0a5ac92a7d7e6dec3796203253ce9bcd298ca0839a6aa862d` |
| `_input/arith-note.pdf` | disclosed related manuscript (both editors only) | 12 | `be7a612de9fb13e582a31ee96316e6bced3ae2a9468ff63ae067e9261ef7ead7` |

Each reviewer was a separate subagent that received byte-identical copies of only its own PDFs in
`<folder>/scratch/input/` and was told to open nothing else: no repository, scripts, data, earlier
reviews, records of the revision, or account of how the papers were produced. Each editor received the
other two manuscripts, labelled as related manuscripts disclosed by the authors. Each reviewer could
fetch published literature headlessly (no browser, no email address or personal data in any request)
and run its own code in its own git-ignored `scratch/` (package installs only in a virtual environment
there). The panels ran one after the other. Each reviewer was told: "Review for Annals of Global
Analysis and Geometry. Be rigorous and demanding; find every reason not to accept, and say plainly what
is good. Treat the marked placeholders (author contributions, AI-use statement, Zenodo DOI) as known.
Read rendered page images, not only extracted text, before reporting a typographical, sign or figure
error." The report format is: summary; significance; correctness and what was recomputed; MAJOR; MINOR;
presentation (figures and captions included); recommendation (accept / minor / major / reject) with
confidence; what resolves each issue.

## Personas

All ten are new relative to rounds 0-3 (`review/referee-sim/`, `referee-round-1/` to
`referee-round-3/`). Those used: handling editors for JGA and AGAG reading as generic editors; spectral
geometers on inverse problems, isospectral constructions and the DGGW-Stanhope line; analysts of the
Selberg trace formula; PTE combinatorialists focused on searches and tables; a geometric analyst and
JGA regular referee; a number theorist and a numerical analyst (round 0); a rigour-and-citations referee.
Here each role is given a different research background and reading habit.

### Panel A (Paper A)

| folder | persona |
|---|---|
| `A-a-editor-stratified-analyst/` | (a) AGAG editorial-board member whose research is index theory and heat asymptotics on conical and stratified spaces; has desk-rejected collections of loosely related results and dressed-up compactness arguments; judges scope, significance for AGAG readers, length and overlap with the disclosed Paper B and note; gives a desk-reject probability |
| `A-b-equivariant-heat-invariants/` | (b) spectral geometer on orbifold heat invariants through equivariant expansions (Donnelly's formula, singular-strata contributions, the Dryden-Gordon-Greenwald-Webb-Stanhope-Sutton line); asks whether each result follows quickly from known expansions |
| `A-c-equal-power-sums-growth/` | (c) analytic and computational number theorist on PTE, ideal and symmetric solutions, multigrades and N(k); checks the growth results and the sharpness of Theorem 3.7 by building extremal examples |
| `A-d-asymptotic-analyst/` | (d) analyst of small-time heat and trace-formula expansions with explicit remainders (Mellin, Euler-Maclaurin, enveloping series, stability estimates); checks the heat-expansion appendix, the stability section and every proof a main result depends on |
| `A-e-citation-auditor/` | (e) rigour-and-citations referee who reviews for zbMATH and MathSciNet: every citation against its source at statement level, bibliographic data, cross-references, every figure against its caption, every step resting on a computation or outside material |

### Panel B (Paper B)

| folder | persona |
|---|---|
| `B-a-editor-comparison-geometer/` | (a) AGAG editorial-board member in Riemannian comparison geometry and spectral convergence; same remit as A-a, for Paper B, with Paper A and the note as disclosed related manuscripts |
| `B-b-thick-thin-geometer/` | (b) hyperbolic geometer expert in thick-thin decompositions, collars and cusps, and Jorgensen-type discreteness inequalities; checks the diameter bound and the O(2,3,m) cusp argument |
| `B-c-heat-kernel-counting-analyst/` | (c) analyst of heat-kernel bounds and eigenvalue-counting estimates (Weyl laws with explicit remainders, Buser-type bounds); checks the constants of Theorem E and every remainder bound |
| `B-d-numerical-eigen-analyst/` | (d) numerical analyst of Laplace eigenvalue computation (finite elements, method of particular solutions, a-posteriori estimators versus validated enclosures); checks the computations behind the figures and the a-posteriori certificate, and whether "certify"/"certified" is justified |
| `B-e-rigour-referee/` | (e) rigour-and-citations referee for Paper B: proofs, citations at statement level, cross-references, figures against captions |

Each folder holds `REPORT.md`. As in round 3, the harness refused every reviewer's own write, so the
main session saved each report verbatim from the reviewer's returned text, with a provenance comment
on its first line (the only change: the HTML entities for `<` and `>` that the transport introduced were written back as `<` and `>`).
The reviewers' scripts, fetched sources and page renders are in their git-ignored `scratch/`. All ten
reviewers finished; none was left running. The syntheses are [`VERDICT-A.md`](VERDICT-A.md) and
[`VERDICT-B.md`](VERDICT-B.md).
