# Numerical methods behind Section 7 of the paper (and Figure 3)

This file documents how the computed spectra used in Section 7 were obtained and checked, with references
to the programs of this repository. The spectra are the committed ones in `numerics/data/` and
`numerics/moduli/data/`. The inputs of the test (systoles, diameters) and the test itself are computed by
`theory/eigen/instances.py` and `theory/eigen/practice.py`.

## 1. Model of H² and the geometry

- **Model.** Poincaré disc. The eigenproblem is `−Δ_E u = λ w u` with `w(z) = 4/(1−|z|²)²`, by conformal
  covariance of the Laplacian in two dimensions (`numerics/geometry.py`, `numerics/solve.py`).
  The orbifold O(p,q,r) is the double of the triangle T, so spec(O) = spec_N(T) ⊔ spec_D(T) with
  multiplicity. The same holds for polygons, and with the two mirror symmetries of the family.
- **Triangles.** The vertex of angle π/p is at 0, the vertex of angle π/q on the positive real axis, and
  the third on the ray arg z = π/p; side lengths come from the hyperbolic law of cosines
  (`numerics/geometry.py`).
  - The two radial sides are straight.
  - The third side is the circle orthogonal to |z| = 1 through the two outer vertices. It is entered into
    netgen as a rational quadratic spline (`spline3`) whose control point is the intersection of the
    tangents, i.e. an **exact circular arc**.
  - Checks to 1e-12 (achieved 1e-40): angles from tangent vectors, side lengths by integrating
    2|dz|/(1−|z|²), and area by polar quadrature against Gauss–Bonnet.
- **Family O_ϑ.** The Lambert quarter L = OPVY of the quadrilateral Q:
  - right angles at O = 0, P = tanh(a/2), Y = i tanh(b/2), and angle π/3 at V;
  - east side the circle with centre coth a and radius 1/sinh a; north side centre i coth b, radius
    1/sinh b;
  - sinh a sinh b = cos(π/3) = 1/2 and **ϑ = log(sinh a / sinh b)**, so sinh a = √½ e^{ϑ/2} and
    sinh b = √½ e^{−ϑ/2}; ϑ ∈ {0, 0.4, …, 2.8}.

  Both arcs are exact rational quadratic splines (`numerics/moduli/solve_moduli.py`).

## 2. Discretisation

- **Elements.** NGSolve `H1` (continuous Lagrange) of polynomial order p (`numerics/solve.py`;
  `numerics/moduli/solve_moduli.py` for the family).
  - Stiffness ∫∇u·∇v and mass ∫ w u v, with the quadrature order raised by 2p (`bonus_intorder=2*order`)
    because w is rational.
  - The FEM area of the curved mesh is exact to ≤ 2e-14 (triangles) and ≤ 4e-15 (family).
- **Curved elements:** `mesh.Curve(p)`, geometry order equal to element order.
- **Mesh.** Uniform *hyperbolic* size h, i.e. Euclidean size h(1−|z|²)/2.
  - It is imposed by `MeshingParameters(maxh=h/2, grading=0.2)` and `RestrictH` on a 60×60 barycentric
    sample of the triangle plus 200 points on the arc; for L, an 80×80 sample plus 300 points per arc.
  - **There is no grading towards the small-angle vertices** (π/8, π/12, π/3). None is needed because every
    corner is regular: at a corner of angle π/k with equal conditions the eigenfunctions extend by
    reflection to smooth Z_k-invariant functions, and in the mixed sectors of L the exponents are integers.
  - Observed at p = 10: h-rates 13–19 (triangles) and 16–24 (family), and geometric p-convergence, with
    factors 145–350 and 309–543 respectively from p = 8 to 10.
- **Levels** (h, p): (0.1, 10), (0.07, 8), (0.07, 12), (0.07, 10) and production **(0.05, 10)**. The
  production level of O(2,8,8) Neumann has 35 641 degrees of freedom.
- **Boundary conditions.**
  - Triangles: Neumann (natural) and Dirichlet on all three sides.
  - Family: eight sectors ⟨outer⟩⟨x⟩⟨y⟩ ∈ {N,D}³ on L. The two arcs carry the condition of Q's sides (N for
    spec_N(Q), D for spec_D(Q)); the two mirror segments carry N (even) or D (odd). spec(O_ϑ) is the union of
    the eight.
  - The reduction was checked against Q solved whole at ϑ = 0.8: 1206 N and 1203 D eigenvalues, the same
    counts, agreeing to ≤ 1.6e-10 relative.

## 3. Eigensolver and windows

- **Shift-invert Lanczos.** ARPACK via `scipy.sparse.linalg.eigsh` (`sigma` shift, `which="LM"`, `tol=0`,
  i.e. machine precision). One sparse LU (`splu`, COLAMD ordering) of A − σM per shift, and **k = 200
  eigenvalues per window** (`numerics/solve.py`).
- **Windows, family (and Figure 3):** `eigenvalues_robust`, a doubly covered slicing (`numerics/solve.py`).
  - Each window's "inner" part is 80% of its radius. The next shift is placed so that every eigenvalue
    below the final cut lies in the inner part of **two** independent windows.
  - Values are clustered at relative tolerance 1e-9. A cluster's multiplicity is the largest count that any
    covering window reports. Clusters seen by fewer than all covering windows are counted as ARPACK misses
    and repaired.
  - Family: NEV = 700 per sector, giving 723–730 eigenvalues per sector with λ_max ≥ 1.63e4, and **0 misses**
    (`numerics/moduli/data/summary.json`, "arpack_misses_repaired").
- **Windows, triangles.** The committed triangle spectra were produced by an earlier single-window slicing,
  kept in `numerics/legacy/single_window.py`: each window certifies its radius, consecutive windows overlap,
  and each eigenvalue comes from one window. NEV = 1300 per triangle and condition.
- **The double-window recomputation** reran the four triangle problems with `eigenvalues_robust`
  (`numerics/rerun_double_window.py`, NGSolve 6.2.2607, one problem at a time).
  - The eigenvalues are in `numerics/data/double_window/` and the comparison record is
    `numerics/data/rerun_double_window_comparison.json`.
  - Counts below the common cut agree in all four problems. The largest relative difference is 1.4e-14,
    every value is within err_conservative, and no ARPACK miss was repaired.
  - `theory/eigen/practice_double_window.py` reruns the test on the recomputed lists, with the same counts
    (18/20 and 25/29). It also records what one deleted or duplicated eigenvalue does: in
    `theory/eigen/data/practice_missing.csv`, (C1) concludes a wrong signature in 19 of 24 cases.
- **Multiplicities** are counted by the clustering above (family, Figure 3).
  - In the family, ϑ = 0 has an extra rotation symmetry. For example λ_1 = 4.122413 is degenerate between the
    sectors NND and NDN. The two copies lie in different sectors, so they are computed in different
    problems and neither can be lost to a cluster.
  - The exact cross-level counts (Section 5 below) also cover multiplicities.

## 4. Error estimates: what ε_j is

- **ε_j = err_estimate = max(|λ(0.05,10) − λ(0.07,12)|, 1e-14·max(λ,1))**, the disagreement of the
  production level and the p = 12 level on the coarser mesh (`numerics/eigdata.py`; for the family,
  `numerics/moduli/analysis.py`).
  - The two discretisations agree to about 1e-11 relative.
  - λ_0 = 0 exactly, with ε_0 = 0 (Neumann, NNN sector).
  - A second, conservative measure, err_conservative = |λ(0.05,10) − λ(0.07,10)|, is stored alongside.
- **It is an estimate, not an enclosure.**
  - Conforming FEM with exact geometry gives discrete values that are upper bounds. Here the curved
    elements reproduce the arc exactly only up to the geometric approximation of order p, and the quadrature
    of w is inexact, so not even that is strictly guaranteed.
  - Observed: convergence from above for all modes (triangles) and for over 99% of modes (family).
- **Sizes.**
  - Triangles, first 500 per condition: ≤ 2.9e-11 relative (estimate), ≤ 1.2e-8 (conservative).
  - Triangles, over the complete range λ ≤ 1.6e4 used in Section 7: ≤ 7.4e-8 relative for O(2,8,8) and
    ≤ 4.7e-9 for O(3,3,12) (from the CSV files).
  - Family, first 300 per sector: ≤ 1.3e-10 (8.3e-9 conservative).
  - In the test, Σ_{j<N} ε_j is negligible: replacing err_estimate by err_conservative changes no count
    (`theory/eigen/data/practice.csv`, rows `epsc`).
- The first 41 values λ̃_j, ε_j of each triangle orbifold, with their source file and index, are in
  `theory/eigen/data/triangle_spectra_first41.csv`.

## 5. Completeness (no eigenvalue missing below a stated λ)

- **Triangles, trace test** (`numerics/data/heat_trace_checks.csv`).
  - For 0.0015 ≤ t ≤ 0.05 (60 points), the computed Z_N + Z_D (all about 2850 computed eigenvalues plus a
    Weyl-type tail bound) is compared with the identity and elliptic terms of the trace formula. The closed
    geodesics contribute < 1e-12 for t ≤ 0.03.
  - The agreement is 7.1e-13, against an error budget (eigenvalue errors plus tail) of ≤ 1.5e-11. At
    t = 0.0015 the difference is 4.69e-13 and the bound 1.465e-11.
  - A missing eigenvalue λ lowers the computed trace by e^{−λt}. At t = 0.0015 this would exceed
    1.465e-11 + 4.7e-13 whenever **λ < ln(1/1.51e-11)/0.0015 ≈ 1.66e4**. Hence no eigenvalue below about
    1.6e4 is missing, and an inserted spurious eigenvalue is excluded the same way.
  - This is conditional on the error budget: the estimated ε_j, and the tail bound, which assumes that the
    counting function beyond the computed range stays below the two-term Weyl law plus twice its largest
    observed excess.
  - Two further checks support it, though neither is a proof. The Weyl residual of the counting function
    has mean ≤ 0.003 and rms 0.66–0.70 over ≥ 1420 eigenvalues per condition. An exact rerun of the
    (3,3,12) Neumann spectrum on a second machine agrees for all 1434 eigenvalues to 1.0e-12.
- **Family.**
  1. Double-window coverage with 0 disagreements (Section 3).
  2. **Exact agreement of the eigenvalue counts** per sector: of the three accurate levels below 0.8 × the
     least λ_max of the five levels, and of all five below 0.5 × (asserted in `numerics/moduli/analysis.py`).
  3. A trace test for t ≥ 0.0025 up to the geodesic-free time: |Z − I − 4E_3| ≤ 1.2e-12 against a budget
     ≤ 2.2e-11. It detects a missing eigenvalue below ln(1/2.3e-11)/0.0025 ≈ **9.8e3**.
  4. Z = I + 4E_3 + H with the enumerated geodesics, to 1.2e-12 up to t = 0.33.
- **What Section 7 uses as "complete":**
  - Triangles: λ ≤ 16 000, the trace-test range. This gives **2002** eigenvalues for O(2,8,8) and **2001**
    for O(3,3,12).
  - Family, "full" spectra (`numerics/moduli/data/convergence.csv`, all computed eigenvalues of every
    sector): λ ≤ 0.8 × the least sector maximum, i.e. 13 076–13 360, giving **4357–4451** eigenvalues (the
    range of check 2). The trace test alone covers λ < 9.8e3.
  - Family, "120" spectra (`numerics/moduli/data/eigenvalue_flow_sectors.csv`, the first 120 per sector):
    λ ≤ the least sector maximum, i.e. 2438–2564, giving **815–856** eigenvalues.

## 6. Eigenvalue counts

| quantity | value | source |
|---|---|---|
| computed per triangle and condition | 1425 (2,8,8 N), 1420 (D); 1434 (3,3,12 N), 1420 (D); up to λ ≈ 21 736–21 893 (N), 23 775–23 808 (D) | `numerics/data/eigenvalues_*_{N,D}.csv` |
| computed per triangle orbifold | 2845 and 2854: the union of N and D | the same files |
| union below min(λ_max^N, λ_max^D), complete by the solver's own windows | 2719 and 2741, λ ≤ 21 736 / 21 893 | the same files |
| complete below 1.6e4 (Section 7) | 2002 and 2001: the union cut at λ = 16 000, the trace-test range | `theory/eigen/practice.py` (`LAM_COMPLETE_TRIANGLE`) |
| family, below the least sector maximum | 5451–5572 (5805–5815 computed in all) | `numerics/moduli/data/convergence.csv` |
| family, first 120 per sector merged, below the least sector maximum | 815–856 | `numerics/moduli/data/eigenvalue_flow_sectors.csv` |
| family, below 0.8 × the least sector maximum | 4357–4451 | `theory/eigen/practice.py` (`family_spectra`) |

## 7. The test itself (`theory/eigen/practice.py`)

- **Criteria.** (C1) and (C2) of Theorem 7.1 exactly as stated. E_N(t) uses H of Lemma 2.2 (the first bound
  for s ≤ ℓ²/(2(1+ℓ)), the all-t bound otherwise), β = max over S of Σ b_0(m_i), and λ̃_N − ε_N in the tail.
- **The infimum over s.**
  - s = t·u, with 240 log-spaced u ∈ [1e-8, 1].
  - For all N at once, the grid minimum of μ(s − t) + log(A/4πs + β + H(s)), μ = λ̃_N − ε_N, is found by a
    query on the lower convex hull. Any s gives an upper bound for the infimum, so this E_N is valid.
  - At each reported count N*, the counts N* − 1, N* − 2, … are re-tested with the infimum by bounded Brent
    minimisation in log s, and N* is confirmed that way.
- **The t-grid.** 400 log-spaced t ∈ [0.002, 1] plus 300 in [1e-5, 0.002), then 61 log-spaced points in
  the bracket of every grid point attaining the minimum. Reported: the least N, the t-window where it is
  attained, and its midpoint.
- **G_σ(t).**
  - Float64 composite Gauss–Legendre: 16 nodes per panel of width ½ on [−220, 300] for E_m. The identity
    term is used in the split form with the closed part e^{−t/4}/t.
  - It is asserted against 30-digit mpmath to ≤ 1e-12 (achieved 2.1e-15) at t ∈ {1e-5, 1e-3, 0.03, 0.4, 1}.
  - Gaps in the examples are ≥ 1e-3, so this accuracy is far from limiting. It is not interval arithmetic.
- **Inputs.** Systole lower bounds and diameters from `theory/eigen/instances.py`, by complete enumeration
  at 40 and 50 digits.

## 8. Figure 3, O(2,3,m)

`figures/gen/gen_e1_cusp.py` uses the same solver (`numerics/solve.py`, `eigenvalues_robust`, k = 30,
NEV = 12 per condition) on Triangle(m, 2, 3), i.e. with the vertex of angle π/m at the centre of the disc.

- **Orders and levels.** 21 orders m = 7 … 4096, each at two levels, (h, p) = (0.1, 8) and (0.07, 10); the
  second is plotted.
- **Size.** 521–5149 degrees of freedom at the coarse level and 1646–10 806 at the fine level, over m and
  N/D (`figures/data/e1_cusp_eigs.csv`).
- **Agreement.** The two levels agree for λ_1 … λ_6 to **at most 2.27e-10 relative** (126 values;
  `figures/data/e1_cusp_spectrum.csv`, column rel_diff; the script asserts ≤ 1e-6). This is a convergence
  indicator, not an error bound.
- **Mesh and limits.** The same uniform hyperbolic mesh, with no grading at the π/m vertex. m = 8192 gave a
  spurious double eigenvalue, and m = 16384 failed in the mesher.
