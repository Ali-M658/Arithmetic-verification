# referee-round-5: final pre-submission review for the Annals of Global Analysis and Geometry, two papers

Purpose: final pre-submission review of two papers for AGAG, each decided separately:

* **Paper A**: `paper/jga/manuscript.tex` with `supplement.tex`, "How much of a hyperbolic orbifold does
  heat hear?";
* **Paper B**: `paper/eigen/manuscript.tex`, "Finitely many eigenvalues determine the signature of a
  hyperbolic orbifold".

The companion arithmetic note is `paper/arith/note.tex`.

**Length is out of scope.** The authors have settled the length of both papers. Every reviewer and editor
was told not to comment on length or suggest cutting, shortening, splitting or moving material, and each
editor was told not to use length in the desk-reject estimate. The syntheses ignore any such remark and
list it nowhere.

Submission gate (per paper; see `VERDICT-A.md`, `VERDICT-B.md`): **READY** if (i) there is no confirmed
FATAL item and no confirmed MAJOR item concerning correctness, rigour or a claim the paper does not
support; and (ii) the AGAG editor sends the paper to review with desk-reject probability at most 15%,
estimated without regard to length. Remaining items about significance, scope or taste do not block.
Otherwise **NOT READY**, with the blocking items. Only files under `review/referee-round-5/` were written
in this round.

## Input (git-ignored in `_input/`)

Built from the sources of commit `3134dbd` with a forced `latexmk -g` (run twice) in `paper/jga/` and
`paper/eigen/` and `latexmk -g note.tex` in `paper/arith/`. All four logs show 0 LaTeX errors and 0
undefined references or citations. Paper B has one overfull box of 0.8 pt (line 349); the others have
none. pdfTeX embeds a creation date, so a rebuild gives different hashes. The PDF metadata carry the
title and the six authors, and no other attribution.

| file | role | pages | SHA-256 |
|---|---|---|---|
| `_input/paperA-manuscript.pdf` | Paper A (all Panel A reviewers; Panel B editor) | 44 | `b63f31263c85877f03b3382e003d9ee26d55ebef9b127c53d5608b0850de557e` |
| `_input/paperA-supplement.pdf` | Paper A supplement (as above) | 18 | `5f60f34ae749af47fc4159d014deee1f26c9ea5b08bfd10215d77f4d15026f44` |
| `_input/paperB-manuscript.pdf` | Paper B (all Panel B reviewers; Panel A editor) | 26 | `f336065d7ab719032c53b29a26b89979d36d77e556209d494d78fa29092594bc` |
| `_input/arith-note.pdf` | disclosed related manuscript (both editors only) | 12 | `5efda1093fce97e1f261f1eeacbc89e52b25bf589b7dca4604491ab4f03cf1a0` |

Each reviewer was a separate subagent that got byte-identical copies of only its own PDFs in
`<folder>/scratch/input/` and was told to open nothing else: no repository, scripts, data, earlier
reviews, records of the revision, or account of how the papers were produced. Each editor got the
other two manuscripts, labelled as related manuscripts disclosed by the authors. Each reviewer could
fetch published literature headlessly (no browser, no email address or personal data in any request)
and run its own code in its own git-ignored `scratch/`, with packages installed only in a virtual
environment there. The panels ran one after the other. Each reviewer was told: "Review for Annals of
Global Analysis and Geometry. Be rigorous and demanding; find every reason not to accept, and say
plainly what is good. Do not comment on the length of the paper or suggest cutting, shortening,
splitting or moving material: length is out of scope. Treat the marked placeholders (author
contributions, AI-use statement, Zenodo DOI) as known. Read rendered page images, not only extracted
text, before reporting a typographical, sign or figure error." Report format: summary; significance;
correctness and what was recomputed; MAJOR; MINOR; presentation (figures, captions, notation,
exposition; not length); recommendation (accept / minor / major / reject) with confidence; what
resolves each issue.

## Personas

All ten personas are new relative to rounds 0-4 (`review/referee-sim/`, `referee-round-1/` to
`referee-round-4/`). Those rounds used: JGA and AGAG handling editors whose research was generic,
stratified-space index theory or comparison geometry; spectral geometers on inverse problems,
isospectral constructions, the DGGW-Stanhope line and equivariant heat invariants; trace-formula and
heat-kernel counting analysts; PTE combinatorialists and an analytic number theorist on N(k); an
asymptotic analyst; a thick-thin and Jorgensen-inequality geometer; a finite-element and particular-
solutions numerical analyst; and rigour-and-citations referees for JGA and zbMATH. This round keeps the
brief's five roles per panel but gives each a different research background and reading habit.

### Panel A (Paper A)

| folder | persona |
|---|---|
| `A-a-editor-aga-handling/` | (a) AGAG handling editor whose research is spectral theory on moduli spaces of hyperbolic surfaces (random surfaces, Weil-Petersson volumes, spectral gaps in large genus): scope, significance for AGAG readers, presentation, overlap with the disclosed Paper B and note; gives a desk-reject probability without regard to length |
| `A-b-conic-heat-invariants/` | (b) analyst of heat invariants of singular spaces and conic singularities (Cheeger's cones, Brüning-Seeley, Kokotov, polygon corner contributions, Donnelly and DGGW orbifold expansions); checks Section 2 in full, including the variable-curvature Section 2.4 |
| `A-c-pte-moment-problem/` | (c) Prouhet-Tarry-Escott and truncated-moment-problem specialist (power-sum Jacobians, finite-moment uniqueness, N(k)); checks Section 3, Theorem 3.8 and its sharpness, the growth equivalence (Theorem 3.14, Proposition 3.15, Theorem 1.1) and Appendix A |
| `A-d-appendix-analyst/` | (d) analyst of quantitative uniqueness and conditional stability for inverse problems, with a background in triangle groups; checks every appendix, Sections 4-6 and every proof a main result depends on |
| `A-e-rigour-citations-figures/` | (e) rigour, citations and figures referee: a geometer who has been technical editor of a Springer journal and reads statements as a proof-assistant user would; every citation at statement level, every cross-reference, every figure against caption and data |

### Panel B (Paper B)

| folder | persona |
|---|---|
| `B-a-editor-aga-handling/` | (a) AGAG handling editor whose research is determinants of Laplacians and compactness of isospectral sets (the Osgood-Phillips-Sarnak line): same remit as A-a, for Paper B, with Paper A and the note as disclosed related manuscripts |
| `B-b-hyperbolic-geometer/` | (b) hyperbolic geometer on Fuchsian groups and Teichmüller spaces of orbifolds (signatures, collars around geodesics and cone points, thick-thin decomposition, systoles); checks Sections 4 and 8 |
| `B-c-spectral-analyst/` | (c) spectral analyst on heat kernels, eigenvalue counting and the Selberg trace formula with elliptic terms, using explicit test-function methods; checks Sections 2-6 and recomputes the constants of Theorem 6.2 |
| `B-d-numerical-analyst/` | (d) numerical analyst in validated numerics (interval arithmetic, rigorous eigenvalue enclosures of Plum-Nakao type, reproducibility); checks Section 7, the a-posteriori test, and whether its inputs and claims are stated honestly |
| `B-e-rigour-citations-figures/` | (e) rigour, citations and figures referee who formalises statements in Lean and edits for a society journal: hypotheses and quantifiers, cross-references, every citation at statement level, every figure against its caption |

Each folder holds `REPORT.md`. The harness refused every reviewer's own write. The main session therefore
extracted each report verbatim from the reviewer's final message in its task transcript, keeping the text
from the report's first heading on. A provenance comment is on each report's first line, and no transport
entities occurred. Reviewers' scripts, fetched sources and page renders are in their git-ignored
`scratch/`. All ten reviewers finished, and none was left running.

## Outcome

| paper | recommendations (a editor; b; c; d; e) | editor's desk-reject probability | gate |
|---|---|---|---|
| A | major (provisional); minor; minor; minor (conditional); minor | 30% | **NOT READY**: A1 abstract, A2 §2.4 sketches, A3 heat-trace link; editor above 15% |
| B | major (provisional); minor; minor (conditional on companion); major; minor (conditional on companion) | 25% | **NOT READY**: B1 completeness and certification statements in §7; editor above 15% |

No reviewer found a mathematical error in either paper. Every blocking item can be fixed in the text. The
syntheses are [`VERDICT-A.md`](VERDICT-A.md) and [`VERDICT-B.md`](VERDICT-B.md).
