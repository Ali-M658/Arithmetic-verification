# The old repository: what to do once the new repositories are public

For the owner of `github.com/Ali-M658/Arithmetic-verification` (A. Agadi).

The three papers no longer point to this repository. Their code and data now live in three new repositories, each archived at Zenodo:

- https://github.com/pa1aash/heat-invariants-orbifolds (Paper A)
- https://github.com/pa1aash/eigenvalues-orbifold-signature (Paper B)
- https://github.com/pa1aash/equal-sum-reciprocal-triples (the arithmetic note)

## What to do, and when

**When:** after all three new repositories are public and their Zenodo DOIs exist. Doing it earlier gains nothing and leaves readers of the current drafts with no repository.

Choose one of the following:

1. **Make the repository private** (Settings > General > Danger Zone > Change repository visibility > Make private). This removes public access to the current files and to the whole history, including the third-party files listed below. Forks made while it was public are not removed.
2. **Archive it** (Settings > General > Danger Zone > Archive this repository). This makes it read-only, but it stays public, and so does its history. Archive it only if a public read-only copy is wanted, and preferably make it private first. A private repository can also be archived.

Before either step, optionally add one line at the top of the README pointing to the three new repositories.

## Why the history matters

Commit "Stop tracking third-party texts" removed the files below from the tree of `main`. Copies stay on the authors' machines and are git-ignored, so they cannot be committed again. But **the files remain in the history** of `main` and `remote-remediation`, here and on GitHub. Anyone who can read the repository can still get them from the commits that added them (`e731eca`, `6181dc7`, `b7c3ebf`, `16adcd9`).

The same holds for the PDF of Uçar's thesis, `research/raw/spectral-invariants-for-polygons-and.pdf`. It was added in `e731eca` and removed from the tree in `ede344b`, but it is still in the history (see `REPO-DECISIONS.md`, item (b)). Its arXiv licence is granted to arXiv only, so the authors have no right to redistribute it.

As long as the repository is public, these files remain publicly redistributed. Making it private ends that without rewriting history. The other route, rewriting history with `git filter-repo`, is described in `REPO-DECISIONS.md` item (b). It needs a force-push and the agreement of everyone with a clone, and it is not needed if the repository is made private.

## The files removed from the tree

Each one contains the full or nearly full text of a third-party work. The source is the URL it was fetched from, as recorded in the file.

| file | work | source |
|---|---|---|
| `research/notes/unsolved-problems-in-number-theory-pdf-1o9si23bb6dg.md` | R. K. Guy, *Unsolved Problems in Number Theory*, 3rd ed., Springer 2004 (book) | vdoc.pub (an unauthorised mirror) |
| `research/notes/spectral-invariants-for-polygons-and.md` | E. Uçar, *Spectral invariants for polygons and orbisurfaces*, dissertation, HU Berlin (thesis) | edoc.hu-berlin.de |
| `research/notes/190500259-the-heat-kernel-on-curvilinear-polygonal-domains-in-surfaces-2.md` | Nursultanov–Rowlett–Sher, *The heat kernel on curvilinear polygonal domains in surfaces*, arXiv:1905.00259 | ar5iv |
| `research/notes/the-heat-kernel-on-curvilinear-polygonal-domains-in-surfaces-annales-mathmatique.md` | the same paper, published version, *Ann. Math. Québec* | doi.org/10.1007/s40316-024-00237-4 |
| `research/notes/the-spectral-geometry-of-hyperbolic-and-spherical-manifolds-analogies-and-open-p.md` | Lauret–Linowitz, *The spectral geometry of hyperbolic and spherical manifolds: analogies and open problems*, arXiv:2305.10950 | arxiv.org/html |
| `research/notes/170101874-heat-trace-expansion-on-manifolds-with-conic-singularities-2.md` | *Heat trace expansion on manifolds with conic singularities*, arXiv:1701.01874 | ar5iv |
| `research/notes/the-heat-trace-for-domains-with-curved-corners.md` | *The heat trace for domains with curved corners*, arXiv:2512.04422 | arxiv.org/html |
| `research/notes/181206119-schueth-corner-contributions-ar5iv-fulltext.md` | D. Schueth, *On the corner contributions to the heat coefficients of geodesic polygons*, arXiv:1812.06119 | ar5iv |
| `research/notes/inverse-spectral-problems-for-collapsing-manifolds-i-uniqueness-and-stability-fu.md` | *Inverse spectral problems for collapsing manifolds I*, arXiv:1209.5875 | arxiv.org/pdf |
| `research/notes/inverse-spectral-problems-for-collapsing-manifolds-ii-quantitative-stability-of.md` | *Inverse spectral problems for collapsing manifolds II*, arXiv:2404.16448 | arxiv.org/pdf |
| `research/notes/the-steklov-spectrum-of-convex-polygonal-domains-i-spectral-finiteness-the-journ.md` | *The Steklov spectrum of convex polygonal domains I*, *J. Geom. Anal.* | link.springer.com (10.1007/s12220-025-01922-8) |
| `research/notes/do-the-hodge-spectra-distinguish-orbifolds-from-manifolds-part-2.md` | *Do the Hodge spectra distinguish orbifolds from manifolds? Part 2*, arXiv:2311.00337 | arxiv.org/html |
| `research/notes/151004637-on-the-arithmetic-dimension-of-triangle-groups-2.md` | *On the arithmetic dimension of triangle groups*, arXiv:1510.04637 | ar5iv |
| `research/notes/heat-coefficients-of-surfaces-with-curved-conical-singularities.md` | *Heat coefficients of surfaces with curved conical singularities*, arXiv:2511.22255 | arxiv.org/html |
| `research/notes/251122255-heat-coefficients-of-surfaces-with-curved-conical-singularities.md` | the same paper | ar5iv |
| `research/notes/heat-coefficients-of-surfaces-with-curved-conical-singularities-annals-of-global.md` | the same paper, published version, *Ann. Global Anal. Geom.* | link.springer.com (10.1007/s10455-025-10024-1) |
| `research/notes/asymptotic-expansion-of-the-heat-kernel-for-orbifolds-full-text-arxiv08053148-pd.md` | Dryden–Gordon–Greenwald–Webb, *Asymptotic expansion of the heat kernel for orbifolds*, arXiv:0805.3148 | arxiv.org/pdf |
| `research/notes/isospectrality-for-orbifold-lens-spaces-full-text-arxiv170501412v2.md` | *Isospectrality for orbifold lens spaces*, arXiv:1705.01412 | arxiv.org/pdf |
| `research/notes/11034372-doyle-rossetti-fulltext.md` | Doyle–Rossetti, *Laplace-isospectral hyperbolic 2-orbifolds are representation-equivalent*, arXiv:1103.4372 | ar5iv |
| `research/notes/any-three-eigenvalues-do-not-determine-a-triangle-full-text-arxiv191106758v2.md` | Gómez-Serrano–Orriols, *Any three eigenvalues do not determine a triangle*, arXiv:1911.06758 | arxiv.org/pdf |
| `research/notes/171100577-spectral-geometry-of-surfaces-with-curved-conic-singularities-2.md` | *Spectral geometry of surfaces with curved conic singularities*, arXiv:1711.00577 | ar5iv |
| `research/notes/220613013-continuity-of-the-roots-of-a-polynomial-2.md` | *Continuity of the roots of a polynomial*, arXiv:2206.13013 | ar5iv |
| `review/audit/stability/holtz_tyaglov_0912.4703.txt` | Holtz–Tyaglov, *Structured matrices, continued fractions, and root localization of polynomials*, arXiv:0912.4703 | arxiv.org/pdf |
| `review/round1-fixes/citations/crootmaoyip2026_arxiv_html.md` | Croot–Mao–Yip, *The Prouhet–Tarry–Escott problem for subsets with small doubling in integral domains*, arXiv:2609.05061 | arxiv.org/html |
| `theory/eigen/sources/arxiv_1809.07309.txt` | Gongopadhyay–Mishra–Tiwari, *On generalized Jørgensen inequality in SL(2,C)*, arXiv:1809.07309 | arxiv.org/pdf |

No verification stage and no manuscript reads these files. The stages that could be affected were rerun after the removal and pass.

Files that were looked at and kept: publisher landing pages that give only the title, abstract and metadata, Crossref records, a table of contents, short verbatim quotes in the research notes and source registers, web articles (Wikipedia, MathWorld, Eppstein, MathPages), the colour-map tables in `figures/style/third_party/`, and the journal templates and class files, which are distributed under their own licences.
