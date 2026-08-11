# Q5 venue set — The Journal of Geometric Analysis, 2019–2026

**Method (matters for the sourcing rule):** every record below was retrieved from the
Crossref REST API filtered to the JGA journal ISSN, not written from memory and not taken
from a secondary listing. Query used:

```
https://api.crossref.org/journals/1050-6926/works
  ?query.bibliographic=<term>
  &filter=from-pub-date:2019-01-01,until-pub-date:2026-12-31
```

Crossref confirms the journal identity as *Journal of Geometric Analysis*,
ISSN `1050-6926` (print) / `1559-002X` (electronic), publisher Springer-Verlag.
Twenty terms were swept: orbifold, heat trace, heat kernel, conical singularity, cone
singularity, inverse spectral, isospectral, spectral determination, heat invariants, cone
points, triangle eigenvalue, polygon spectrum, corner heat, Steklov polygon, hearing the
shape, orbifold spectrum Laplacian, singular set spectrum, spectral rigidity, cone angle
metric, Laplacian eigenvalues surface. 73+46 unique DOIs returned; the twelve below are
the ones actually in this manuscript's area.

Every DOI, volume, issue, page range and article number below came back from Crossref.
Where Crossref returns an article number rather than a page range (Springer's current
practice), that is recorded as `art N` — it is not a missing page range.

## The twelve

| # | DOI | Year | Vol/Iss | Pages / Art | Title | Authors |
|---|---|---|---|---|---|---|
| 1 | `10.1007/s12220-021-00611-6` | 2021 | 31(10) | 9433–9468 | Approximating Orbifold Spectra Using Collapsing Connected Sums | Farsi, Proctor, Seaton |
| 2 | `10.1007/s12220-025-01922-8` | 2025 | 35(3) | art 91 | The Steklov Spectrum of Convex Polygonal Domains I: Spectral Finiteness | Dryden, Gordon, Moreno, Rowlett, Villegas-Blas |
| 3 | `10.1007/s12220-025-01984-8` | 2025 | 35(6) | art 171 | Isospectral CR Manifolds with Respect to the Kohn Laplacian | Gutierrez, Lauret, Rossetti |
| 4 | `10.1007/s12220-021-00717-x` | 2021 | 31(12) | 12347–12374 | Spectral Determinant on Euclidean Isosceles Triangle Envelopes | Kalvin |
| 5 | `10.1007/s12220-019-00339-4` | 2020 | 31(3) | 2238–2295 | Robin Spectral Rigidity of the Ellipse | Vig |
| 6 | `10.1007/s12220-019-00326-9` | 2019 | 31(2) | 1821–1854 | Stability in the Inverse Steklov Problem on Warped Product Riemannian Manifolds | Daudé, Kamran, Nicoleau |
| 7 | `10.1007/s12220-023-01348-0` | 2023 | 33(9) | art 284 | Heat Kernel Estimate in a Conical Singular Space | Huang, Zhang |
| 8 | `10.1007/s12220-018-00137-4` | 2019 | 30(1) | 337–389 | The Heat Asymptotics on Filtered Manifolds | Dave, Haller |
| 9 | `10.1007/s12220-019-00248-6` | 2019 | 30(4) | 4427–4452 | Inverse Spectral Theory for Perturbed Torus | Isozaki, Korotyaev |
| 10 | `10.1007/s12220-022-01164-y` | 2023 | 33(4) | art 116 | Spectral Analysis of the Kohn Laplacian on Lens Spaces | Fan, Kim, Plzak, Shors, Sottile, Zeytuncu |
| 11 | `10.1007/s12220-023-01269-y` | 2023 | 33(8) | art 242 | Two-Term Spectral Asymptotics in Linear Elasticity | Capoferri, Friedlander, Levitin, Vassiliev |
| 12 | `10.1007/s12220-025-02300-0` | 2026 | 36(2) | art 58 | Existence and Non-uniqueness of Cone Spherical Metrics with Prescribed Singularities on a Compact Riemann Surface with Positive Genus | Feng, Song, Xu |

## Why these three matter most

- **#2 (Dryden–Gordon–Rowlett et al., 2025)** is the single strongest venue precedent.
  Emily Dryden and Carolyn Gordon are two of the four authors of DGGW 2008 — the
  manuscript's central analytic input — and they published a *spectral finiteness*
  result for polygonal domains in this exact journal in 2025. Same authors, same journal,
  adjacent problem, current. This is simultaneously the best venue evidence and the
  strongest referee signal in the set.
- **#3 (Gutierrez–Lauret–Rossetti, 2025)** puts an isospectrality paper by Rossetti — a
  co-author of the manuscript's cited RSW 2008 — in JGA in 2025.
- **#6 (Daudé–Kamran–Nicoleau, 2019)** is a *stability* theorem for an inverse spectral
  problem, in JGA. It is the direct venue precedent for the planned Q4 section and
  establishes that JGA publishes quantitative-stability inverse-spectral work.

## Near-miss records retained for the venue-shape argument

These are JGA 2019–2026 papers in adjacent territory, useful for characterizing what the
journal publishes but not close enough for the twelve:

- `10.1007/s12220-021-00614-3` (2021, 31(9) 9199–9240) Chang, Khalil, Schulze — Analysis on Regular Corner Spaces
- `10.1007/s12220-023-01208-x` (2023, 33(5)) Tschanz — The Steklov Problem on Triangle-Tiling Graphs in the Hyperbolic Plane
- `10.1007/s12220-025-01990-w` (2025, 35(5)) Hassannezhad, Métras, Perrin — Geometric Bounds for Low Steklov Eigenvalues of Finite Volume Hyperbolic Surfaces
- `10.1007/s12220-022-00890-7` (2022, 32(5)) Jollivet, Sharafutdinov — Steklov Zeta Function of a Planar Domain
- `10.1007/s12220-024-01597-7` (2024, 34(5)) Rong — Burns-Krantz Type Rigidity for Domains With Corners

## Outstanding for this question

Crossref returns bibliographic metadata but not page counts or article length. To
characterize "typical shape" (length, asymptotic vs exact, how much computation) the
depth investigator must open the actual articles. Page ranges above give length directly
for records 1, 4, 5, 6, 8, 9; records 2, 3, 7, 10, 11, 12 carry article numbers only and
need the publisher page for a page count.
