# referee-round-10: three panels (Paper A and Paper B for AGAG, the note for Integers)

Purpose: review the three papers again after the round-9 fixes and the round-10 additions, which the authors
authorised as one extra round beyond the four-round limit:

* **Paper A**: a proof of the parametric heat expansion (Lemma E.1, Appendix E), which removes the
  condition on Proposition 2.14 for l ≥ 3 and on Proposition 2.17(ii) for L ≥ 4;
* **Paper B**: Section 7 retitled as an illustration, not a proof;
* **the note**: Choudhry 2011 read (from an archived copy of the publisher's PDF) and compared, with check 9e.

The three papers are:

* **Paper A**: `paper/jga/manuscript.tex` with `supplement.tex`, "How much of a hyperbolic orbifold does
  heat hear?", for the Annals of Global Analysis and Geometry (AGAG);
* **Paper B**: `paper/eigen/manuscript.tex`, "Finitely many eigenvalues determine the signature of a
  hyperbolic orbifold", for AGAG;
* **the note**: `paper/arith/integers/note.tex`, "Triples with equal sum and equal reciprocal sum", for *Integers*.

**Length is out of scope.** No reviewer, editor or synthesis may comment on length or suggest cutting; any
such remark is excluded from the verdicts.

**Stop condition (per paper).** Every referee (the editor excluded) recommends accept or minor revision,
the editor sends the paper to review, and no confirmed FATAL or MAJOR item remains.

## Inputs

Built with latexmk (zero errors, zero undefined references, no overfull box) and copied to the git-ignored
`_input/`:

| file | pages | SHA-256 |
|---|---|---|
| `A-manuscript.pdf` | 65 | `76dd221da1a5b77e92a0f3676ca358e8ea37ce6a5783e8882bed24791f127436` |
| `A-supplement.pdf` | 19 | `a39882d6fbbee5ad066be28748df2f2f9aa3a00bc7eeb55f58bc0918717ceafa` |
| `B-manuscript.pdf` | 41 | `e09e0639d1d58fdec5214c4903ec5b45f50287f3b57dddcddb490c0fa29888de` |
| `N-note-integers.pdf` | 25 | `b99057fbe7e7064b9259646efafce4a01c3c73b7ce2d2b5ef270e1009499f204` |

The rules for reviewers are as in round 9:
* Each reviewer received only its own paper's PDFs. The editors also received the other manuscripts, labelled as disclosed related manuscripts.
* No reviewer had repository access or saw an earlier review.
* Reviewers could fetch published literature headlessly and run their own code in their git-ignored `scratch/`.
* Each was given the same instruction as in round 9.
* Panels ran one after another.

## Personas

All fifteen are new relative to every earlier round.

Panel A (Paper A, AGAG):

| folder | persona |
|---|---|
| `A-a-editor-global-analysis-generalist/` | (a) AGAG handling editor, a generalist in global analysis on manifolds; scope, significance, physical framing, overlap with the disclosed manuscripts |
| `A-b-parametrix-heat-kernel-analyst/` | (b) analyst of heat-kernel parametrices and their uniformity in parameters; checks Section 2, Appendices B and E, and every use of Donnelly's expansion |
| `A-c-diophantine-power-sums-referee/` | (c) number theorist on systems of equal power sums and their counting; checks Sections 3 and 4 and Appendices A and D |
| `A-d-fuchsian-triangle-groups/` | (d) specialist in Fuchsian triangle groups and the geometry of their orbifolds; checks Section 5, Appendix F and the supplement's geometric sections |
| `A-e-proof-dependency-tracer/` | (e) rigour, citations and figures referee; traces every main result to the proofs and sources it depends on, and checks figures, tables and cross-references |

Panel B (Paper B, AGAG):

| folder | persona |
|---|---|
| `B-a-editor-spectral-geometry-generalist/` | (a) AGAG handling editor, a generalist in spectral geometry; scope, significance, the honesty of the numerical claims |
| `B-b-orbifold-trace-formula-analyst/` | (b) analyst of the Selberg trace formula for orbifolds with elliptic terms; checks Sections 2, 3 and the appendix |
| `B-c-weyl-law-remainder-analyst/` | (c) analyst of Weyl laws, counting-function remainders and explicit tail bounds; checks Sections 4 to 6 and 8 |
| `B-d-computer-assisted-proof-referee/` | (d) referee of computer-assisted proofs (interval arithmetic, validated numerics); checks Proposition 6.5, Tables 3 and 4 and Section 7 |
| `B-e-citation-and-claims-auditor/` | (e) rigour, citations and figures referee; checks every claim against its proof or source, and the tables and figures |

Panel N (the note, Integers):

| folder | persona |
|---|---|
| `N-a-editor-integers-handling/` | (a) Integers handling editor in classical number theory; scope, significance, novelty, the treatment of prior work |
| `N-b-elliptic-curves-group-law/` | (b) specialist in rational points and group laws on plane cubics; checks Sections 2, 3 and 5 |
| `N-c-diophantine-equations-classical/` | (c) specialist in classical Diophantine equations (symmetric systems, multigrade equations); checks Sections 1, 4 and 6.4 |
| `N-d-computational-enumeration-referee/` | (d) computational number theorist; checks Section 6 and every computation by rerunning it |
| `N-e-rigour-and-references-checker/` | (e) rigour and references referee; checks every proof step, every citation at statement level and Integers house style |
