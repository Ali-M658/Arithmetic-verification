# referee-round-6: three panels (Paper A and Paper B for AGAG, the note for Integers)

Purpose: review the three papers, each decided separately against the stop condition below:

* **Paper A**: `paper/jga/manuscript.tex` with `supplement.tex`, "How much of a hyperbolic orbifold does
  heat hear?", for the Annals of Global Analysis and Geometry (AGAG);
* **Paper B**: `paper/eigen/manuscript.tex`, "Finitely many eigenvalues determine the signature of a
  hyperbolic orbifold", for AGAG;
* **the note**: `paper/arith/integers/note.tex` (generated from `paper/arith/note.tex` by
  `make_integers.py`), "Triples with equal sum and equal reciprocal sum", for *Integers*.

**Length is out of scope.** No reviewer, editor or synthesis comments on length or suggests cutting; any
such remark is excluded from the verdicts.

**Stop condition (per paper).** Every referee (the editor excluded) recommends accept or minor revision,
the editor sends the paper to review, and no confirmed FATAL or MAJOR item remains.

## Changes made before this round's build

The standing cross-citation rule (A cites B and the note, B cites A and the note, the note cites A, each as
a preprint with a preprint-identifier placeholder) was not yet met. Before the build:

* `paper/jga/references.bib`: the entries for the note and for Paper B, previously "Companion manuscript"
  and "Companion manuscript, submitted", are now "Preprint, [PLACEHOLDER: preprint identifier]".
* `paper/eigen/references.bib`: Paper A's entry now reads "Preprint, [PLACEHOLDER: preprint identifier]";
  a new entry `companionN` cites the note in the same form.
* `paper/eigen/manuscript.tex`, start of the paragraph on shared computations (Section 1): one new sentence,
  "The two triangle orbifolds O(2,8,8) and O(3,3,12) have the same area π/2 and the same first two heat
  invariants, since their orders have the same sum 18 and the same reciprocal sum 3/4; such coincidences
  of sum and reciprocal sum are the subject of the companion note [companionN]". Checked exactly with
  rational arithmetic: both triples have S = 18, R = 3/4, area 2π(1 − R) = π/2 and constant term
  (S + R − 2)/12 = 67/48.
* `paper/arith/references.bib` and `paper/arith/integers/make_integers.py`: Paper A's entry now reads
  "preprint, [PLACEHOLDER: preprint identifier]"; `note.tex` was regenerated.

## Input (git-ignored in `_input/`)

Built from commit `42a61d9` plus the changes above, with a forced `latexmk -g` followed by `latexmk` in
`paper/jga/` and `paper/eigen/`, and `latexmk -g` in `paper/arith/integers/`. All logs show 0 LaTeX
errors, 0 undefined references or citations and no overfull box above 1 pt (Paper B has one of less than
1 pt). The PDF metadata carry the title and the six authors and no other attribution. pdfTeX embeds a
creation date, so a rebuild gives different hashes.

| file | role | pages | SHA-256 |
|---|---|---|---|
| `_input/paperA-manuscript.pdf` | Paper A (Panel A; Panel B and N editors) | 47 | `89cc388df956b9c304926dcaf411612efbc22650477b05da1d4e60d535dd13d0` |
| `_input/paperA-supplement.pdf` | Paper A supplement (as above) | 19 | `81953c707e85521a427e4a967b92cd5c36c3360eda2eeed28b1f4fd92ec29a7a` |
| `_input/paperB-manuscript.pdf` | Paper B (Panel B; Panel A and N editors) | 29 | `037e98e7c46c835cc5a50057f9b34c2e9cd8840afc9d957af2bf6caaab23101b` |
| `_input/note-integers.pdf` | the note, Integers version (Panel N; Panel A and B editors) | 16 | `26c71cf893d631e6da37cbf702dc628124f70c4bfa445b086019540288fe3266` |

## Procedure

Each reviewer was a separate subagent given byte-identical copies of only its own paper's PDFs in
`<folder>/scratch/input/` and told to open nothing else: no repository, scripts, data, earlier reviews or
record of the revision. Each editor also got the other two manuscripts, labelled as related manuscripts
disclosed by the authors. Reviewers could fetch published literature headlessly (no browser, no email
address or personal data in any request) and run their own code in their own git-ignored `scratch/`, with
packages only in a virtual environment there. The three panels ran one after another. Each reviewer was
told: "Review for <journal>. Be as harsh and rigorous as the strictest referee this journal uses; find
every reason not to accept, and say plainly what is good. Do not comment on length. Treat the marked
placeholders as known. Read rendered page images before reporting a typographical, sign or figure error."
The placeholders named to the reviewers were the author-contribution statement, the AI-use statement, the
Zenodo DOIs and the preprint identifiers. Report format: summary; significance; correctness and what was
recomputed; FATAL; MAJOR; MINOR; presentation; recommendation (accept / minor / major / reject) with
confidence; what resolves each issue. Editors also state whether they send the paper to review or
desk-reject it.

## Personas

All fifteen personas are new relative to every earlier round (`review/referee-sim/`, `referee-round-1/`
to `referee-round-5/`).

### Panel A (Paper A, AGAG)

| folder | persona |
|---|---|
| `A-a-editor-wave-trace/` | (a) AGAG handling editor whose research is wave-trace invariants and the length spectrum (Duistermaat-Guillemin-type trace formulas, wave invariants of polygons and billiards); scope, significance, physical framing, overlap with the disclosed Paper B and note; decision to send to review or desk-reject |
| `A-b-conical-defect-physicist/` | (b) mathematical physicist on heat-kernel coefficients and zeta-regularised quantities on spaces with conical defects (cosmic strings, wedges, the Sommerfeld-Carslaw kernel) in constant and variable curvature; checks Section 2 in full, including Section 2.4, Appendix B and Supplement S8 |
| `A-c-power-sum-varieties/` | (c) real algebraic geometer on power-sum and Vandermonde varieties, Newton identities and truncated moment problems; checks Section 3, the Prouhet-Tarry-Escott connection, Appendix A and Supplement S1-S2 |
| `A-d-arithmetic-fuchsian/` | (d) analyst of arithmetic Fuchsian groups and the Selberg trace formula for triangle groups (elliptic and hyperbolic terms, small eigenvalues); checks Sections 4-6, including Theorem 5.8 and its descent, and Supplement S3-S7 |
| `A-e-reproducibility-referee/` | (e) rigour, citations, figures and numerical-reproducibility referee with a background in scientific computing: every citation at statement level, every cross-reference, every figure against its caption and the tables, every numerical claim against its stated method |

### Panel B (Paper B, AGAG)

| folder | persona |
|---|---|
| `B-a-editor-quantum-chaos/` | (a) AGAG handling editor whose research is quantum chaos and semiclassical spectral statistics on hyperbolic surfaces: same remit as A-a, for Paper B, with Paper A and the note as disclosed related manuscripts |
| `B-b-cone-manifold-geometer/` | (b) geometer of hyperbolic cone-manifolds and cone-angle deformations (collars around cone points, discreteness criteria, injectivity radius); checks Sections 4 and 8 and every geometric input of Sections 5-6 |
| `B-c-prime-geodesic-analyst/` | (c) analytic number theorist on the prime geodesic theorem and explicit trace-formula estimates for Fuchsian groups; checks Sections 2, 3, 5 and 6 and recomputes the constants of the main effective theorem |
| `B-d-hp-fem-a-posteriori/` | (d) numerical analyst of a-posteriori error estimation for eigenvalue problems (residual estimators, Kato-Temple and Lehmann bounds, hp-finite elements); checks Section 7, the test and whether its inputs and claims are stated honestly |
| `B-e-mathscinet-reviewer/` | (e) rigour, citations and figures referee who writes MathSciNet reviews and checks statements against their sources: hypotheses and quantifiers, cross-references, every citation at statement level, every figure against its caption |

### Panel N (the note, Integers)

| folder | persona |
|---|---|
| `N-a-editor-unit-fractions/` | (a) Integers editor whose research is unit fractions and Erdős-type problems in combinatorial number theory: scope, significance, fit for Integers, overlap with the disclosed Papers A and B; decision to send to review or desk-reject |
| `N-b-elliptic-ranks/` | (b) arithmetic geometer on ranks of elliptic curves in families, descent and Mordell-Weil groups; checks Sections 2 and 3 and every rank, torsion and model claim |
| `N-c-surfaces-diophantine/` | (c) specialist in Diophantine equations in several variables through the geometry of surfaces (rational and elliptic surfaces, unirationality, Hilbert irreducibility, parametric families); checks Sections 4 and 5 |
| `N-d-certified-enumeration/` | (d) computational number theorist on exhaustive enumerations and their certification (search bounds, duplicate handling, growth fits); checks Section 6 and recomputes the counts |
| `N-e-rigour-citations/` | (e) rigour and citations referee: hypotheses and quantifiers, every proof step, every citation at statement level, notation and cross-references |

Each folder holds `REPORT.md`. Where the harness refused a reviewer's own write, the main session saved the
report verbatim from the reviewer's final message, with a provenance comment on its first line.
