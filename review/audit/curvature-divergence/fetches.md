# Retrieval log (curvature / divergence referee)

All retrieval headless (curl, desktop browser User-Agent header; arXiv export API). Texts extracted with pymupdf.

| item | how | result | used for |
|---|---|---|---|
| arXiv metadata 2109.03897, 2606.21909 | `export.arxiv.org/api/query?id_list=...` | `sources/arxiv_meta.xml`; both exist: Dunne, "Borel Summation and Analytic Continuation of the Heat Kernel on Hyperbolic Space"; Li–Li–Tang, "Heat Kernel and Resurgence" | DV.5 citations |
| Dunne arXiv:2109.03897 | `arxiv.org/pdf/2109.03897` | `sources/dunne_2109.03897.{pdf,txt}`. Eq. (21)–(25): diagonal H^2 kernel ~ e^{-t/4}/(2 pi^{3/2} t) sum (-1)^n eta(2n) Gamma(n+1/2)(t/pi^2)^n; text after (21): Borel singularities become poles on the negative real axis as rho -> 0 | DV.5: nearest singularity at distance pi^2, negative axis (H^2) |
| Li–Li–Tang arXiv:2606.21909 | `arxiv.org/pdf/2606.21909` | `sources/llt_2606.21909.{pdf,txt}`. Example 2.30 (S^2, d=0): Sing of the Borel transform of tau e^{-tau/4} Z_{S^2} = {k^2 pi^2 : k >= 1} | DV.5: S^2 nearest singularity pi^2, positive axis |

Gaps (not chased, accepted standing gaps per instructions): Donnelly 1976 (structure theorem behind
Uçar Thm 4.20 and DGGW Thm 4.8 / §5), Steinig 1971, Drury–Marshall 1987.

Gap noted but not chased: a literature search for prior statements of CU.3 Part 4 (flat cone spheres /
doubled triangles sharing heat invariants) and of Lemma 2 (invariant spherical harmonics under finite
rotation groups; classical Molien-type count). See REVIEW.md, CU.2 and CU.3.
