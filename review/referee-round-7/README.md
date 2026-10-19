# referee-round-7: three panels (Paper A and Paper B for AGAG, the note for Integers)

Purpose: review the three papers again after the round-6 fixes (commit `bf40fae`), each decided separately
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

Built with latexmk from `bf40fae` (zero errors, zero undefined references, no overfull box), copied to the
git-ignored `_input/`:

| file | pages | SHA-256 |
|---|---|---|
| `A-manuscript.pdf` | 55 | `10217dfc8bc793e6e890f85ffdfd058e23736bc61a905fe130f9204e7d9609c7` |
| `A-supplement.pdf` | 16 | `5cec343fd6dca0af6a14732dfb4e3977bdbe454cda00b11695a2582f6545380c` |
| `B-manuscript.pdf` | 34 | `7e4bd973cc1169055ffed84ce1659f6eef8796f6e2bfe86baba58952bc0f6c46` |
| `N-note-integers.pdf` | 19 | `dadfabfe72c1e21cd512d6924fbfec7987e93f4e558165f091bfeeb8b7eb28ad` |

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
to `referee-round-6/`).

Panel A (Paper A, AGAG):

| folder | persona |
|---|---|
| `A-a-editor-polygon-heat/` | (a) AGAG handling editor whose research is heat asymptotics on polygonal and curvilinear domains (corner contributions, Kac's problem) and inverse spectral problems for planar domains; scope, significance, physical framing, overlap |
| `A-b-brownian-cone-probabilist/` | (b) probabilist on Brownian motion and heat kernels through Feynman-Kac and path expansions on cones, orbifolds and variable-curvature surfaces; checks Section 2, the variable-curvature propositions and the appendices they use |
| `A-c-symmetric-functions-algebraist/` | (c) algebraic combinatorialist on symmetric functions, resultants, Hurwitz and Orlando determinants and Newton identities; checks Section 3, the Prouhet-Tarry-Escott and moment results and their appendix |
| `A-d-trace-formula-computation/` | (d) spectral analyst and computational geometer on the Selberg trace formula with elliptic terms and on length spectra of triangle groups; checks Sections 4-5, the rigid case, the family, and the computations of the supplement |
| `A-e-attribution-historian/` | (e) rigour, citations and figures referee specialising in priority and attribution: every citation at statement level against its source, older literature included, every figure against its caption, numbering and cross-references |

Panel B (Paper B, AGAG):

| folder | persona |
|---|---|
| `B-a-editor-spectral-gap/` | (a) AGAG handling editor whose research is spectral gaps and small eigenvalues of hyperbolic surfaces (Selberg's 1/4, random covers); scope, significance, honesty of the numerical claims |
| `B-b-systole-collar-geometer/` | (b) geometer of systoles, collars and Bers constants; checks Sections 4 and 8 (diameter, counting of closed geodesics, cusp-like orders, the systole question) |
| `B-c-explicit-formula-analyst/` | (c) analyst of explicit formulas and Paley-Wiener test functions in the trace formula and of rigorous trace-formula verification; checks Sections 2, 5, 6 and Appendix A |
| `B-d-maass-form-computation/` | (d) computational number theorist computing Maass forms and Laplace spectra (Hejhal's method, validated numerics); checks Section 7 and the numerical methods |
| `B-e-springer-copyeditor/` | (e) rigour, citations and figures referee who copy-edits for a Springer Nature mathematics journal: template conventions, numbering, cross-references, statement-level citation checks, figures and captions |

Panel N (the note, Integers):

| folder | persona |
|---|---|
| `N-a-editor-partitions/` | (a) Integers editor whose research is partitions and multiplicative problems (divisor-sum averages); scope, significance, novelty |
| `N-b-torsion-modular-curves/` | (b) arithmetic geometer on torsion of elliptic curves over Q and modular curves X_1(N) (Kubert's families); checks Sections 2, 3 and 5 |
| `N-c-symmetric-systems/` | (c) specialist in symmetric Diophantine systems and multigrade equations, including equal sums of like powers with negative exponents; checks Sections 1.4, 3, 4 and 6.4 |
| `N-d-points-of-bounded-height/` | (d) computational number theorist on counting rational points of bounded height (Manin-type numerics, accumulating subvarieties) and on the statistics of count data; checks Sections 4 and 6 and every computation |
| `N-e-proof-reader/` | (e) rigour and citations referee: quantifiers, every proof step, every citation at statement level, Integers house style |
