# Numerical methods behind Section 7 of the eigen paper (and Figure E1)

Everything below is read from the code and reports named, with `file:line` references, so that
the paper's "Numerical methods" subsection can be written from it. Nothing here was recomputed by
a solver: the spectra are the committed ones. What was computed for the revision (systoles,
diameters, the test itself) is in `instances.py` and `practice.py` of this directory and is
summarised in `practice.md`.

## 1. Model of H² and the geometry

- **Model.** Poincaré disc. The eigenproblem is `−Δ_E u = λ w u` with `w(z) = 4/(1−|z|²)²`, by conformal
  covariance of the Laplacian in two dimensions (`numerics/geometry.py:14-17`, `numerics/solve.py:3-4`).
  The orbifold O(p,q,r) is the double of the triangle T, so spec(O) = spec_N(T) ⊔ spec_D(T) with
  multiplicity (proof: `numerics/REPORT.md:61-127`; the same for polygons and with the two mirror symmetries:
  `numerics/moduli/REPORT.md:99-148`).
- **Triangles.** Vertex of angle π/p at 0, the vertex of angle π/q on the positive real axis, the third
  on the ray arg z = π/p; side lengths from the hyperbolic law of cosines (`numerics/geometry.py:25-53`).
  The two radial sides are straight; the third side is the circle orthogonal to |z| = 1 through the two
  outer vertices, entered into netgen as a rational quadratic spline (`spline3`) whose control point is
  the intersection of the tangents, i.e. an **exact circular arc** (`geometry.py:59-70, 138-152`).
  Checks to 1e-12 (achieved 1e-40): angles from tangent vectors, side lengths by integrating
  2|dz|/(1−|z|²), area by polar quadrature against Gauss–Bonnet (`geometry.py:72-135`; `numerics/REPORT.md:205-216`).
- **Family O_τ** (τ is ϑ of the papers). The Lambert quarter L = OPVY of the quadrilateral Q: right
  angles at O = 0, P = tanh(a/2), Y = i tanh(b/2), angle π/3 at V; east side the circle with centre
  coth a, radius 1/sinh a; north side centre i coth b, radius 1/sinh b; sinh a sinh b = cos(π/3) = 1/2 and
  **τ = log(sinh a / sinh b)**, sinh a = √½ e^{τ/2}, sinh b = √½ e^{−τ/2}; τ ∈ {0, 0.4, …, 2.8}
  (`numerics/moduli/REPORT.md:50-97`, line 76 for τ). Both arcs are exact rational quadratic splines
  (`numerics/moduli/solve_moduli.py:63-75`).

## 2. Discretisation

- **Elements.** NGSolve `H1` (continuous Lagrange) of polynomial order p; stiffness ∫∇u·∇v, mass
  ∫ w u v with quadrature order raised by 2p (`bonus_intorder=2*order`) because w is rational
  (`numerics/solve.py:38-55`; family `numerics/moduli/solve_moduli.py:104-117`). FEM area of the curved mesh
  exact to ≤ 2e-14 (triangles, `numerics/REPORT.md:229`), ≤ 4e-15 (family, `moduli/REPORT.md:232-233`).
- **Curved elements.** Yes: `mesh.Curve(p)`, geometry order = element order (`geometry.py:187`,
  `solve_moduli.py:100`).
- **Mesh.** Uniform *hyperbolic* size h, i.e. Euclidean size h(1−|z|²)/2, imposed by
  `MeshingParameters(maxh=h/2, grading=0.2)` and `RestrictH` on a 60×60 barycentric sample of the
  triangle plus 200 points on the arc (`geometry.py:155-188`); for L an 80×80 sample plus 300 points per
  arc (`solve_moduli.py:78-101`). **There is no grading towards the small-angle vertices** (π/8, π/12,
  π/3): the reports argue it is not needed because every corner is regular — at a corner of angle π/k
  with equal conditions the eigenfunctions extend by reflection to smooth Z_k-invariant functions, and
  in the mixed sectors of L the exponents are integers (`numerics/REPORT.md:288-298`,
  `moduli/REPORT.md:135-144`); observed: h-rates 13–19 (triangles) and 16–24 (family) at p = 10, and
  geometric p-convergence (factors 145–350, resp. 309–543, from p = 8 to 10)
  (`numerics/REPORT.md:278-283`, `moduli/REPORT.md:268-275`).
- **Levels** (h, p): (0.1, 10), (0.07, 8), (0.07, 12), (0.07, 10) and production **(0.05, 10)**
  (`numerics/solve.py:187`, `solve_moduli.py:46`); production dofs for O(2,8,8) Neumann: 35 641
  (`numerics/REPORT.md:252-263`).
- **Boundary conditions.** Triangles: Neumann (natural) and Dirichlet on all three sides
  (`solve.py:35`). Family: eight sectors ⟨outer⟩⟨x⟩⟨y⟩ ∈ {N,D}³ on L — the condition of Q's sides
  (N for spec_N(Q), D for spec_D(Q)) on the two arcs, and N (even) or D (odd) on the two mirror segments
  (`solve_moduli.py:1-15, 51-61`; `moduli/REPORT.md:123-133`); spec(O_τ) is the union of the eight.
  The reduction was checked against Q solved whole at τ = 0.8 (1206 N and 1203 D eigenvalues, same
  counts, ≤ 1.6e-10 relative; `moduli/REPORT.md:288-297`).

## 3. Eigensolver and windows

- **Shift-invert Lanczos** (ARPACK via `scipy.sparse.linalg.eigsh`, `sigma` shift, `which="LM"`,
  `tol=0` i.e. machine precision), one sparse LU (`splu`, COLAMD ordering) of A − σM per shift, **k = 200
  eigenvalues per window** (`numerics/solve.py:58-72`).
- **Windows, family (and Figure E1):** `eigenvalues_robust`, doubly covered slicing: each window's
  "inner" part is 80% of its radius; the next shift is placed so that every eigenvalue below the final cut
  lies in the inner part of **two** independent windows; values are clustered at relative tolerance
  1e-9, a cluster's multiplicity is the largest count any covering window reports, and clusters seen by
  fewer than all covering windows are counted as ARPACK misses and repaired (`solve.py:75-155`). Family:
  NEV = 700 per sector, 723–730 eigenvalues per sector, λ_max ≥ 1.63e4; **0 misses** in the final suite
  (`solve_moduli.py:47`, `moduli/REPORT.md:234-248`, `moduli/data/summary.json` "arpack_misses_repaired").
- **Windows, triangles: the committed triangle spectra were NOT produced by the double-window routine.**
  They come from the earlier single-window slicing (each window certifies its radius; consecutive windows
  overlap; each eigenvalue from one window), now kept unused in `numerics/legacy/single_window.py`
  (`numerics/REPORT.md:232-247`; Paper A's supplement says the same, `paper/jga/supplement.tex:258, 295`).
  NEV = 1300 per triangle and condition (`solve.py:189`). The double-window rerun of the four problems
  (`numerics/rerun_double_window.py`, pinned NGSolve 6.2.2607, one problem at a time) was run on
  2026-10-10: eigenvalues in `numerics/data/double_window/`, record
  `numerics/data/rerun_double_window_comparison.json`. Counts below the common cut agree in all four
  problems, the largest relative difference is 1.4e-14, every value is within err_conservative, and no
  ARPACK miss was repaired. `theory/eigen/practice_double_window.py` reruns the test on the recomputed
  lists (same counts: 18/20 and 25/29) and records what one deleted or duplicated eigenvalue does
  (`data/practice_missing.csv`: (C1) concludes a wrong signature in 19 of 24 cases).
- **Multiplicities.** Counted with multiplicity by the clustering above (family, E1). In the family,
  τ = 0 has the extra rotation symmetry; e.g. λ_1 = 4.122413 is degenerate between the sectors NND and NDN
  (`moduli/REPORT.md:341-344`); being in different sectors, the two copies are computed in different
  problems, so neither can be lost to a cluster. Cross-level exact counts (below) also cover multiplicities.

## 4. Error estimates: what ε_j is

- **ε_j = err_estimate = max(|λ(0.05,10) − λ(0.07,12)|, 1e-14·max(λ,1))**, the disagreement of the
  production level and the p = 12 level on the coarser mesh, two discretisations that agree to ~1e-11
  relative; λ_0 = 0 exactly with ε_0 = 0 (Neumann / NNN sector) (`numerics/eigdata.py:5-16, 59-71`;
  family `numerics/moduli/analysis.py:76-89`). A second, conservative measure
  err_conservative = |λ(0.05,10) − λ(0.07,10)| is stored alongside (same lines).
- **It is an estimate, not an enclosure** (`numerics/REPORT.md:474-481`, `moduli/REPORT.md:418-420`).
  What is rigorous about conforming FEM with exact geometry is that the discrete values are upper bounds;
  the curved elements reproduce the arc exactly only up to the geometric approximation of order p, and the
  quadrature of w is inexact, so not even that is strictly guaranteed here. Observed: convergence from above
  for all modes (triangles) and > 99% of modes (family) (`numerics/REPORT.md:298`, `moduli/REPORT.md:274`).
- Sizes: triangles, first 500 per condition: ≤ 2.9e-11 relative (estimate), ≤ 1.2e-8 (conservative)
  (`numerics/REPORT.md:278-286`); over the complete range λ ≤ 1.6e4 used in Section 7, ≤ 7.4e-8 relative
  (O(2,8,8)) and ≤ 4.7e-9 (O(3,3,12)) (computed from the CSVs). Family, first 300 per sector: ≤ 1.3e-10
  (8.3e-9 conservative) (`moduli/REPORT.md:270-271`). In the test, Σ_{j<N} ε_j is negligible: replacing
  err_estimate by err_conservative changes no count (`data/practice.csv`, rows `epsc`).
- The first 41 values λ̃_j, ε_j of each triangle orbifold, with their source file and index, are in
  `data/triangle_spectra_first41.csv`.

## 5. Completeness (no eigenvalue missing below a stated λ)

- **Triangles, trace test.** For 0.0015 ≤ t ≤ 0.05 (60 points), the computed Z_N + Z_D (all ≈ 2850
  computed eigenvalues plus a Weyl-type tail bound) is compared with the identity + elliptic terms of the
  trace formula, the closed geodesics being < 1e-12 for t ≤ 0.03; agreement 7.1e-13 against an error budget
  (eigenvalue errors + tail) of ≤ 1.5e-11 (`numerics/REPORT.md:348-361`, `numerics/data/heat_trace_checks.csv`:
  at t = 0.0015 difference 4.69e-13, bound 1.465e-11). A missing eigenvalue λ lowers the computed trace by
  e^{−λt}; at t = 0.0015 this would exceed 1.465e-11 + 4.7e-13 whenever **λ < ln(1/1.51e-11)/0.0015 ≈ 1.66e4**.
  Hence "no eigenvalue below about 1.6e4 is missing" (`paper/jga/supplement.tex:287`); an inserted spurious
  eigenvalue is excluded the same way. This is conditional on the error budget (estimated ε_j, and the tail
  bound, which assumes the counting function beyond the computed range stays below the two-term Weyl law
  plus twice its largest observed excess: `numerics/REPORT.md:377-389, 478-481`). The Weyl residual of the
  counting function (mean ≤ 0.003, rms 0.66–0.70 over ≥ 1420 eigenvalues per condition,
  `numerics/REPORT.md:328-346`) and the exact rerun of the (3,3,12) Neumann spectrum on a second machine
  (all 1434 agree to 1.0e-12, `moduli/REPORT.md:257-264`) support it; neither is a proof.
- **Family.** (i) Double window coverage with 0 disagreements (§3); (ii) **exact agreement of the
  eigenvalue counts of the three accurate levels below 0.8 × the least λ_max of the five levels, and of
  all five below 0.5 ×**, per sector (asserted, `numerics/moduli/analysis.py:65-75`; this assert caught the
  first-pass single-window runs that were one eigenvalue short, `moduli/REPORT.md:279-286`); (iii) trace test:
  for t ≥ 0.0025 up to the geodesic-free time, |Z − I − 4E_3| ≤ 1.2e-12 against a budget ≤ 2.2e-11
  (`moduli/REPORT.md:313-324`, `analysis.py:301-319`), which detects a missing eigenvalue below
  ln(1/2.3e-11)/0.0025 ≈ **9.8e3**; and Z = I + 4E_3 + H with the enumerated geodesics to 1.2e-12 up to
  t = 0.33 (`moduli/REPORT.md:330-333`).
- **What Section 7 uses as "complete".**
  - Triangles: λ ≤ 16 000 (the trace-test range): **2002** eigenvalues for O(2,8,8), **2001** for O(3,3,12).
  - Family, "full" spectra (`numerics/moduli/data/convergence.csv`, all computed eigenvalues of every
    sector): λ ≤ 0.8 × least sector maximum, 13 076–13 360, **4357–4451** eigenvalues (the range of
    (ii)); the trace test alone covers λ < 9.8e3.
  - Family, "120" spectra (`numerics/moduli/data/eigenvalue_flow_sectors.csv`, the first 120 per sector,
    which the current manuscript used): λ ≤ least sector maximum, 2438–2564, **815–856** eigenvalues.

## 6. Where the eigenvalue counts of the two papers come from

| quantity | value | source |
|---|---|---|
| computed per triangle and condition | 1425 (2,8,8 N), 1420 (D); 1434 (3,3,12 N), 1420 (D); up to λ ≈ 21 736–21 893 (N), 23 775–23 808 (D) | `numerics/data/eigenvalues_*_{N,D}.csv` |
| "about 2850 per orbifold" (Paper A, supplement) | 2845 and 2854: the union of N and D, everything computed | `paper/jga/supplement.tex:258`, `numerics/REPORT.md:248-250` |
| union below min(λ_max^N, λ_max^D) (complete by the solver's own windows) | 2719 and 2741, λ ≤ 21 736 / 21 893 | computed |
| "about 2000, complete below 1.6e4" (Paper B, §7) | 2002 and 2001: the union cut at λ = 16 000, the trace-test range | `practice.py` (`LAM_COMPLETE_TRIANGLE`) |
| family: "about 5450 per orbifold up to 1.6e4" (Paper A, moduli report) | 5451–5572 below the least sector maximum (5805–5815 computed in all) | `moduli/REPORT.md:246-248`, `convergence.csv` |
| family: "815–856" (Paper B, current §7) | first 120 per sector merged, below the least sector maximum | `eigenvalue_flow_sectors.csv` |
| family in the revised §7 | 4357–4451 below 0.8 × least sector maximum | `practice.py:family_spectra` |

So both papers describe the same computed spectra; the numbers differ only in the cut. A consistent
wording: "about 2850 eigenvalues computed per triangle orbifold, of which the about 2000 below 1.6×10⁴ are
certified complete by the trace test" — avoiding "certified": "of which no eigenvalue below 1.6×10⁴ can be
missing without violating the trace test".

## 7. The test itself (`practice.py`)

- Criteria (C1) and (C2) of Theorem 7.1 exactly as stated; E_N(t) with H of Lemma 2.3 (first bound for
  s ≤ ℓ²/(2(1+ℓ)), the all-t bound otherwise), β = max over S of Σ b_0(m_i), λ̃_N − ε_N in the tail
  (`practice.py:149-205, 289-345`).
- **inf over s:** s = t·u, 240 log-spaced u ∈ [1e-8, 1]; for all N at once the grid minimum of
  μ(s − t) + log(A/4πs + β + H(s)), μ = λ̃_N − ε_N, by a query on the lower convex hull; any s gives an upper
  bound for the infimum, so this E_N is valid; at each reported count N*, N* − 1, N* − 2, … are re-tested
  with the infimum by bounded Brent minimisation in log s, and N* is confirmed that way
  (`practice.py:157-205, 395-438`).
- **t-grid:** 400 log-spaced t ∈ [0.002, 1] plus 300 in [1e-5, 0.002), then 61 log-spaced points in the
  bracket of every grid point attaining the minimum (`practice.py:71, 395-438`). Reported: the least N,
  the t-window where it is attained, its midpoint.
- **G_σ(t):** float64 composite Gauss–Legendre (16 nodes per panel of width ½ on [−220, 300] for E_m;
  identity term in the split form with the closed part e^{−t/4}/t), asserted against 30-digit mpmath to
  ≤ 1e-12 (achieved 2.1e-15) at t ∈ {1e-5, 1e-3, 0.03, 0.4, 1} (`practice.py:78-146`). Gaps in the
  examples are ≥ 1e-3, so this accuracy is far from limiting; it is not interval arithmetic.
- **Inputs:** systole lower bounds and diameters from `instances.py` (complete enumeration at 40 and 50
  digits; see `practice.md`).

## 8. Figure E1, O(2,3,m)

`figures/gen/gen_e1_cusp.py`: the same solver (`numerics/solve.py`, `eigenvalues_robust`, k = 30, NEV = 12
per condition) on Triangle(m, 2, 3), i.e. the vertex of angle π/m at the centre of the disc (lines 7-12,
73-79); 21 orders m = 7 … 4096 (line 43); **two levels (h, p) = (0.1, 8) and (0.07, 10)**, the second
plotted (line 44); 521–5149 dofs at the coarse and 1646–10 806 at the fine level (over m and N/D; `figures/data/e1_cusp_eigs.csv`).
The two levels agree for λ_1 … λ_6 to **at most 2.27e-10 relative** (126 values; `e1_cusp_spectrum.csv`,
column rel_diff; asserted ≤ 1e-6 at line 101). This is a convergence indicator, not an error bound.
Same uniform hyperbolic mesh, no grading at the π/m vertex; m = 8192 gave a spurious double eigenvalue and
m = 16384 failed in the mesher (lines 14-16).
