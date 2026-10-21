# referee-round-9: three panels (Paper A and Paper B for AGAG, the note for Integers)

Purpose: review the three papers again after the round-8 fixes (commit `3ea3cd3`), each decided separately
against the stop condition:

* **Paper A**: `paper/jga/manuscript.tex` with `supplement.tex`, "How much of a hyperbolic orbifold does
  heat hear?", for the Annals of Global Analysis and Geometry (AGAG);
* **Paper B**: `paper/eigen/manuscript.tex`, "Finitely many eigenvalues determine the signature of a
  hyperbolic orbifold", for AGAG;
* **the note**: `paper/arith/integers/note.tex` (generated from `paper/arith/note.tex`), "Triples with equal
  sum and equal reciprocal sum", for *Integers*.

**Length is out of scope.** No reviewer, editor or synthesis comments on length or suggests cutting; any
such remark is excluded from the verdicts.

**Stop condition (per paper).** Every referee (the editor excluded) recommends accept or minor revision,
the editor sends the paper to review, and no confirmed FATAL or MAJOR item remains.

## Inputs

Built with latexmk from `3ea3cd3` (zero errors, zero undefined references, no overfull box), copied to the
git-ignored `_input/`:

| file | pages | SHA-256 |
|---|---|---|
| `A-manuscript.pdf` | 61 | `548954ad41230f2b3f5920dc75c664709e5c2ecfe188ac117a6d62df5911b13b` |
| `A-supplement.pdf` | 17 | `1ece814a068f5fbb519595a2d81e43e2df935eb6ac9e08f6ece696d52a1c77d5` |
| `B-manuscript.pdf` | 38 | `38e6a37ba6c8a62f47de0570e5e64da547ee2566f2f085da733916b390a7cc6b` |
| `N-note-integers.pdf` | 24 | `69bf137aac70af869e469a9cd0a725a26ec0682d01a4e922cfa29882dba7e702` |

Each reviewer received only its own paper's PDFs (the editors also the other two manuscripts, labelled as
disclosed related manuscripts), no repository access and no earlier reviews. Each could fetch published
literature headlessly (no browser, no email address or personal data in any request) and run its own
code in its own git-ignored `scratch/`, with packages only in virtual environments there. Each was told:
"Review for <journal>. Be as harsh and rigorous as the strictest referee this journal uses; find every
reason not to accept, and say plainly what is good. Do not comment on length. Treat the marked
placeholders as known. Read rendered page images before reporting a typographical, sign or figure error."
Panels ran one after another (A, then B, then N); the five reviewers of a panel ran in parallel.

## Personas

All fifteen personas are new relative to every earlier round (`review/referee-sim/`, `referee-round-1/`
to `referee-round-8/`). This is the last round allowed by the four-round limit (rounds 6 to 9).

Panel A (Paper A, AGAG):

| folder | persona |
|---|---|
| `A-a-editor-singular-heat-asymptotics/` | (a) AGAG handling editor whose research is heat-kernel asymptotics on singular spaces (cones, edges, stratified spaces); scope, significance, physical framing, overlap |
| `A-b-fixed-point-heat-kernel/` | (b) analyst of fixed-point (Lefschetz, Donnelly) contributions to heat traces and of the Selberg trace formula with elliptic terms; checks Section 2, Appendix B and Section 6 with Appendix C |
| `A-c-equal-sums-analytic-number-theorist/` | (c) analytic number theorist on equal sums of like powers, the Prouhet-Tarry-Escott problem and counting their solutions; checks Section 3, Section 4 and Appendices A and D |
| `A-d-hyperbolic-polygon-geometer/` | (d) geometer of hyperbolic polygons and triangle groups (explicit trigonometry, tilings, closed geodesics); checks Section 5, Appendix E and the supplement's geometric and numerical sections |
| `A-e-proof-completeness-auditor/` | (e) rigour, citations and figures referee who audits each proof for completeness, each citation at statement level, each figure and table against its caption, and every cross-reference |

Panel B (Paper B, AGAG):

| folder | persona |
|---|---|
| `B-a-editor-effective-geometric-analysis/` | (a) AGAG handling editor whose research is effective bounds in geometric analysis (explicit constants from compactness arguments); scope, significance, honesty of the numerical claims |
| `B-b-moduli-compactness-geometer/` | (b) geometer of moduli spaces of hyperbolic orbifolds, Mumford-Bers compactness and thick-thin decompositions; checks Sections 3, 4 and 8 |
| `B-c-eigenvalue-counting-tails/` | (c) analyst of eigenvalue counting functions, heat-trace tails and Weyl laws with explicit constants; checks Sections 2, 5, 6 and the appendix |
| `B-d-ball-arithmetic-certification/` | (d) numerical analyst on certified computation in ball and interval arithmetic (Arb, validated quadrature, eigenvalue enclosures); checks Section 7, Proposition 6.4 and every numerical claim |
| `B-e-logical-dependency-auditor/` | (e) rigour, citations and figures referee: the logical dependency of every result on its hypotheses and sources, citations at statement level, tables and figures |

Panel N (the note, Integers):

| folder | persona |
|---|---|
| `N-a-editor-elementary-number-theory/` | (a) Integers editor whose research is elementary and combinatorial number theory; scope, significance, novelty |
| `N-b-elliptic-surfaces-mordell-weil/` | (b) arithmetic geometer on elliptic surfaces, Mordell-Weil lattices and torsion in families; checks Sections 2, 3 and 5 |
| `N-c-rational-points-on-surfaces/` | (c) Diophantine geometer on rational points of bounded height on surfaces (del Pezzo surfaces, conic bundles, Manin's conjecture); checks Sections 1, 4 and 6.4 |
| `N-d-experimental-mathematics/` | (d) experimental and computational number theorist on exhaustive searches and their honest statistical description; checks Section 6 and every computation |
| `N-e-integers-copy-and-proof-editor/` | (e) rigour and citations referee: every proof step, every citation at statement level, Integers house style |
