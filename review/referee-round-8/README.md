# referee-round-8: three panels (Paper A and Paper B for AGAG, the note for Integers)

Purpose: review the three papers again after the round-7 fixes (commit `cdf2b27`), each decided separately
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

Built with latexmk from `cdf2b27` (zero errors, zero undefined references, no overfull box), copied to the
git-ignored `_input/`:

| file | pages | SHA-256 |
|---|---|---|
| `A-manuscript.pdf` | 58 | `5c10e8c12d3aa64ed2f588292714ba33ee329ca39878edb5b511c80cb6c3991a` |
| `A-supplement.pdf` | 16 | `e616559d7712b0ce2bb54c04ba704cec553bf920d878de37ded40c4e616469ac` |
| `B-manuscript.pdf` | 36 | `10ffafe3cb87eb44370ea837021602aecb6acf763d62f3056beabb6087ab6f45` |
| `N-note-integers.pdf` | 22 | `948ce0c2f8dae027d6ab2e4c8daa0d9d96b0510008dc9e37e4c3187eec9e3eef` |

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
to `referee-round-7/`).

Panel A (Paper A, AGAG):

| folder | persona |
|---|---|
| `A-a-editor-orbifold-isospectrality/` | (a) AGAG handling editor whose research is spectral invariants and isospectrality of orbifolds (heat invariants of singular strata, isospectral orbifolds with different singularities); scope, significance, physical framing, overlap |
| `A-b-cone-zeta-analyst/` | (b) analyst of zeta-regularised determinants and heat expansions on manifolds with conical singularities (Cheeger, Brüning-Seeley, Mellin calculus) and of variable-curvature Riemannian invariants; checks Section 2, the variable-curvature results, Appendix B and Section 6 with Appendix C |
| `A-c-quadrature-moment-theorist/` | (c) approximation theorist on moment problems, Gauss quadrature, Chebyshev systems and their algebraic side (power sums, Prouhet-Tarry-Escott); checks Section 3, Section 4 and Appendices A and D |
| `A-d-teichmuller-orbifold-moduli/` | (d) geometer of Teichmüller and moduli spaces of hyperbolic orbifolds and of arithmetic triangle groups and their length spectra; checks Section 5, Appendix E and the supplement's searches, spectra and blind recovery |
| `A-e-lemma-by-lemma-verifier/` | (e) rigour, citations and figures referee who verifies each lemma line by line, each citation at statement level and each figure against its caption, cross-references and numbering throughout |

Panel B (Paper B, AGAG):

| folder | persona |
|---|---|
| `B-a-editor-inverse-spectral/` | (a) AGAG handling editor whose research is inverse spectral problems and spectral rigidity on surfaces (length spectrum versus Laplace spectrum, finiteness of isospectral sets); scope, significance, honesty of the numerical claims |
| `B-b-fuchsian-signature-geometer/` | (b) geometer of Fuchsian groups and their signatures (Riemann-Hurwitz, Gauss-Bonnet, fundamental domains, thick-thin decompositions of orbifolds); checks Sections 3, 4 and 8 |
| `B-c-selberg-zeta-analyst/` | (c) analyst of the Selberg zeta function, Weyl laws with remainder and heat-trace asymptotics with explicit constants; checks Sections 2, 5, 6 and the appendix |
| `B-d-validated-eigenvalue-numerics/` | (d) numerical analyst on validated eigenvalue computation (interval arithmetic, method of particular solutions, a-posteriori inclusion bounds); checks Section 7 and every numerical claim |
| `B-e-statement-citation-auditor/` | (e) rigour, citations and figures referee: every statement against its proof and hypotheses, every citation at statement level, tables and figures against captions, numbering |

Panel N (the note, Integers):

| folder | persona |
|---|---|
| `N-a-editor-additive-combinatorics/` | (a) Integers editor whose research is additive combinatorics and sums of unit fractions; scope, significance, novelty |
| `N-b-descent-heights/` | (b) arithmetic geometer on descent, Mordell-Weil ranks and canonical heights of elliptic curves over Q; checks Sections 2, 3 and 5 |
| `N-c-parametric-diophantine/` | (c) classical Diophantine analyst on parametric solutions of symmetric systems (multigrade identities, Euler-type parametrisations, Schinzel's method); checks Sections 1, 3, 4 and 5 |
| `N-d-exact-enumeration-algorithms/` | (d) computational number theorist on the correctness and completeness of exhaustive enumerations and on fitting growth exponents to count data; checks Section 6 and every computation |
| `N-e-integers-proof-reader/` | (e) rigour and citations referee: every proof step and quantifier, every citation at statement level, Integers house style |
