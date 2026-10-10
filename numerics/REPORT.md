# The listening experiment: computed spectra of O(2,8,8) and O(3,3,12)

## Outcome

**CONFIRMED within error.** The computed spectra of O(2,8,8) and O(3,3,12) give
the difference of heat traces D(t) = Z₍₂,₈,₈₎(t) − Z₍₃,₃,₁₂₎(t). Fitting
D(t)/t = c₁ + c₂t + … over t ∈ [0.0015, 0.012]:

| | fitted | predicted (exact) | deviation |
|---|---|---|---|
| c₁ (from the P₃ difference, eq. (5)) | **2.0833320 ± 0.0000031** | 25/12 = 2.0833333 | −1.3e-6 (−0.4σ) |
| c₂ (from the P₅ difference, Schueth Thm 4.1) | **−73.9551 ± 0.0062** | −1775/24 = −73.9583 | +0.0033 (+0.5σ) |

The uncertainty is the larger of two quantities:

- the worst-case effect of the eigenvalue errors on the fit;
- the change in the fitted value when one more polynomial term is added (model
  truncation).

With the much more conservative coarse-mesh error bars, the uncertainties are
1.4e-5 and 0.028, and the deviations are −0.09σ and +0.12σ.

**The answer to the title question for this pair.** The area and a₀ coincide.
Neither the fit's 1/t term nor its constant can separate the two pillows: both
come out equal to within fit error. The t¹ coefficient separates them,
2.0833 ≈ 25/12, with the sign predicted by K = −1: the pillow with smaller
P₃ = Σm³ has the larger trace. So heat hears the cone orders at the third
coefficient, exactly as Theorem C states.

**Stronger than the fit.** For t ≤ 0.03, the computed D(t) agrees pointwise
with the exact difference of the Selberg elliptic (cone-point) terms to 4e-13,
against an error budget of ≤ 3e-11. That checks every order of the cone
expansion at once, not just c₁ and c₂.

**Benchmark.** Strohmaier–Uski list 42 multiplicity-one Bolza eigenvalues below
998. All 42 are reproduced by the (2,3,8) triangle, to ≤ 5.7e-11 relative,
which is the precision of the published digits.

**Compute.** Everything ran locally on an 8-core M1. Steps 3–5 took about 1.5 h
of solver time on a machine shared with three other jobs (load average
15–75). **RunPod is not needed.**

Two departures from the brief, both forced by the mathematics and explained in
§5:

- **The fit range is t ∈ [0.0015, 0.012], not [0.02, 0.5].** The cone-point
  series is asymptotic with factorially growing coefficients:
  c₃ ≈ 3.2e3, c₄ ≈ −1.7e5, … At t = 0.02 the terms c₁t, c₂t², c₃t³ are 0.042,
  −0.030 and +0.026, so no truncated polynomial represents D there. In
  addition, closed geodesics contribute up to about 0.1 by t = 0.5. The
  computed D(t) is still reported on [0.0015, 0.5] (data/heat_trace_difference.csv),
  together with the exact elliptic prediction that holds over the whole range.
- **The bare three-term fit c₁t + c₂t² + c₃t³ is biased** by the omitted
  orders on any usable window. On [0.0015, 0.004] it gives c₁ = 2.0815 and
  c₂ = −71.6. It is reported for transparency (headline.json), but it is not
  the estimator.


---

## 1. The doubling principle

**Claim.** Let T be the hyperbolic triangle with angles π/p, π/q, π/r and let
O = O(p,q,r) be the pillow, the metric double of T: two copies T, T′ glued
isometrically along ∂T. Then the Laplace spectrum of O is the union, with
multiplicity, of the Neumann spectrum and the Dirichlet spectrum of T.

**Proof.** Let σ : O → O be the involution exchanging the two sheets. It fixes
∂T pointwise and is an isometry of O. Away from the three vertices, ∂T is a
union of smooth geodesic arcs in the interior of the smooth surface
O° = O ∖ {cone points}, and near such an arc σ is the reflection in that
geodesic.

*Form domain.* The Laplacian of the closed orbifold O is the self-adjoint
operator of the quadratic form Q(f) = ∫_O |∇f|² dA on H¹(O), the completion of
C^∞(O) in the H¹ norm. A point has zero H¹-capacity in dimension 2, so
H¹(O) = H¹(O°): nothing is imposed at the cone points. The spectrum is discrete
because O is compact.

*Splitting.* σ preserves dA, Q and H¹(O), so H¹(O) = H¹₊ ⊕ H¹₋ into σ-even and
σ-odd parts. The two parts are orthogonal in L² and also for Q: the cross term
∫∇f₊·∇f₋ changes sign under σ, so it vanishes. Hence the operator is the
orthogonal sum Δ₊ ⊕ Δ₋ of the operators of Q restricted to H¹₊ and to H¹₋.

*Identification.* Restriction to T maps H¹₊ onto H¹(T) and H¹₋ onto H¹₀(T),
with ‖f‖²_O = 2‖f|_T‖²_T and Q(f) = 2 Q_T(f|_T):

- An odd f has traces on ∂T from the two sides that are negatives of each
  other. They also agree, because f ∈ H¹ has no jump across an interior curve.
  So the trace is 0 and f|_T ∈ H¹₀(T).
- Conversely, the even (odd) extension of u ∈ H¹(T) (u ∈ H¹₀(T)) has equal
  traces on both sides of each edge. By the gluing lemma for Sobolev functions
  across a Lipschitz interface it lies in H¹(O°) = H¹(O).

So, up to the common factor 2, the restricted forms are the Neumann form on
H¹(T) and the Dirichlet form on H¹₀(T). Their operators are the Neumann and
Dirichlet Laplacians Δ_N and Δ_D of T. Restriction composed with 1/√2-scaled
extension is unitary, so Δ_O ≅ Δ_N ⊕ Δ_D, and the spectra coincide with
multiplicity. ∎

*Remarks.*

1. No regularity at the vertices is used. Pointwise, the even extension of a
   Neumann eigenfunction is an orbifold eigenfunction: in the orbifold chart at
   a vertex of angle π/k, it is the function obtained by reflecting u
   repeatedly across the two sides, a Z_k-invariant function on a disk.
2. The same argument gives the heat kernels by the method of images,
   K_{N/D}(x,y;t) = K_O(x,y;t) ± K_O(x,σy;t) for x, y ∈ T, so that
   Z_O = Z_N + Z_D.
3. Two published results use the identical identity:
   - Uçar's proof of Corollary 4.18 writes the Dirichlet and Neumann kernels of
     a hemisphere as K ∓ K∘σ.
   - Uçar's Theorem 4.10, eq. (4.7), proves Z_{M/Z_k} − Z_{M/D_k} = Z_Ω^{Dir}
     for a spherical lune Ω of angle π/k. That is the spherical analogue of
     Z_O − Z_N = Z_D here.

   [Uçar, PhD thesis, HU Berlin 2017, DOI 10.18452/18463, arXiv:1711.03405,
   pp. 123–126 and 135.]
4. The paper's own description of O(p,q,r) as the double of the triangle
   (paper/main.tex, §1) is the geometric input. The claim above is what turns
   it into a statement about spectra.

Numerically, the principle is used only in the form Z_O(t) = Z_N(t) + Z_D(t).
It is tested directly in §4(d): the computed Z_N + Z_D reproduces the exact
Selberg identity + elliptic terms of the *orbifold* O to about 1e-12. The
Bolza benchmark (§4(b)) tests the analogous statement for the (2,3,8)
triangle and a genus-2 surface that covers it.

## 2. Predictions (exact rationals)

Sources:

- paper/main.tex eqs. (1)–(5);
- review/hyperresearch/Q2-cone-coefficients.md;
- re-read from the fetched originals:
  - Schueth, Ann. Inst. Fourier 69 (2019), arXiv:1812.06119, Theorem 4.1 and
    Remark 4.2;
  - Uçar, thesis, eqs. (4.25), (4.33), (4.35).

**Conventions.**
- Eigenvalues of the positive Laplacian.
- Z(t) = Σ_j e^{−λ_j t} ~ (4πt)^{−1} Σ_ℓ a_ℓ^{sm} t^ℓ + Σ_cones Σ_ℓ b_ℓ(C) t^ℓ.
- K = κ = −1.
- D(t) = Z_{(2,8,8)}(t) − Z_{(3,3,12)}(t).

**Power sums.**

| | R = Σ1/m | S₁ = Σm | P₃ = Σm³ | P₅ = Σm⁵ |
|---|---|---|---|---|
| (2,8,8) | 1/2+1/8+1/8 = 3/4 | 18 | 8+512+512 = 1032 | 32+32768+32768 = 65568 |
| (3,3,12) | 1/3+1/3+1/12 = 3/4 | 18 | 27+27+1728 = 1782 | 243+243+248832 = 249318 |

**t⁻¹.** Area = 2π(1 − R) = π/2 for both pillows, so Area/(4πt) = 1/(8t).
The smooth coefficients a_ℓ^{sm} are fixed multiples of the area, so they
cancel in D at every order.

**t⁰.** By eq. (3), a₀ = (S₁ + R − 2)/12 = (18 + 3/4 − 2)/12 = **67/48** for both
pillows. So D has no t⁰ term.

**t¹ (eq. (5) at K = −1).**

Σb₁ = −P₃/360 − S₁/36 + 11R/360.

With ΔS₁ = ΔR = 0:

c₁ = −(1032 − 1782)/360 = 750/360 = **25/12 ≈ 2.0833333**.

**t² (Schueth, Theorem 4.1, at K² = 1, Δ_g K = 0).**

Σb₂ = (P₅ − R)/2520 + (P₃ − R)/720 + (S₁ − R)/180.

c₂ = (65568 − 249318)/2520 + (1032 − 1782)/720
   = −183750/2520 − 750/720
   = −875/12 − 25/24
   = **−1775/24 ≈ −73.958333**.

**Sign.** D(t) = +2.0833 t − 73.958 t² + … So the (2,8,8) pillow has the larger
heat trace at small t. P₃ enters b₁ with K = −1, so the pillow with the
*smaller* P₃ has the larger t¹ coefficient.

**Cross-checks** (asserted in theory.py and validate.py):

1. Uçar's general formula (4.25)+(4.33) reproduces eq. (2)/(4) (DGGW §5.6,
   Schueth Rem. 4.2) at ν = 0, 1 and Schueth Thm 4.1 at ν = 2, exactly, for
   every order 2 ≤ k < 40.
2. The exact elliptic term of the Selberg trace formula for orbisurfaces
   [Dryden–Strohmaier, arXiv:math/0504571, eq. (1)] is
   E_k(t) = Σ_{l=1}^{k−1} (2k sin θ_l)^{−1} ∫ e^{−2θ_l r} (1 + e^{−2πr})^{−1} e^{−t(1/4+r²)} dr,
   with θ_l = πl/k. Its Taylor coefficients at t = 0 equal Uçar's b_ν(k) at
   κ = −1 to 1e-15, for ν ≤ 4 and k ∈ {2, 3, 8, 12}. This independently fixes
   the sign convention, since b_ν carries (−1)^ν.

**Higher orders** (Uçar's closed form, used only for diagnostics):

c₃ = 153025/48 ≈ 3188.0, c₄ ≈ −1.742e5, c₅ ≈ 1.177e7, c₆ ≈ −9.56e8.

The ratios |c_{ν+1}/c_ν| ≈ 35, 43, 55, 68, 81 grow linearly in ν. The
cone-point series is asymptotic, not convergent, and is dominated by the
order-12 cone: b_ν(12) grows like ν!·(144/π²)^ν. At t = 0.02 the terms
c₁t, c₂t², c₃t³ are 0.042, −0.030, +0.026: no truncation of the series
describes D(t) there.

## 3. Geometry and solver

**Placement** (geometry.py). Vertex A (angle π/p) is at 0, B (angle π/q) is on
the positive real axis, and C (angle π/r) is on the ray arg z = π/p. Vertex
radii are tanh(d/2), with the side lengths d from the hyperbolic law of cosines
for angles. The third side is the arc of the circle |z − z₀| = ρ through B and C
with |z₀|² = 1 + ρ², i.e. orthogonal to the unit circle.

These checks do not use the law of cosines, and each is asserted to 1e-12
(achieved: 1e-40):

- all three angles are recomputed from the constructed tangent vectors;
- the side lengths come from integrating 2|dz|/(1 − |z|²);
- the area comes from polar quadrature of w = 4/(1 − |z|²)².

| triangle | area | perimeter L | sides (a = BC, b = AC, c = AB) |
|---|---|---|---|
| (2,8,8) | π/4 = 0.785398163… | 5.505594287 | 2.4484525, 1.5285709, 1.5285709 |
| (3,3,12) | π/4 | 5.380127319 | 2.1581701, 2.1581701, 1.0637871 |
| (2,3,8) | π/24 | 1.988511684 | 0.8607063, 0.7642855, 0.3635199 |

**Discretisation** (solve.py). The problem is −Δ_E u = λ w u. It is solved
with NGSolve H¹ elements of order p on a netgen mesh:

- the mesh has uniform *hyperbolic* size h, i.e. Euclidean size h(1 − |z|²)/2;
- the geodesic side is an exact rational quadratic spline, curved to order p;
- the FEM area of the curved mesh is exact to ≤ 2e-14;
- Dirichlet = all three sides essential, Neumann = natural.

**Eigenvalues by spectral slicing.**

- Each slice is a shift-invert Lanczos (ARPACK) at shift σ, using one sparse LU
  of A − σM (COLAMD ordering), with k = 200 eigenvalues per slice.
- Each slice certifies every eigenvalue within its radius ρ.
- Consecutive windows are forced to overlap, and each eigenvalue is taken from
  exactly one slice. The list is therefore complete with multiplicity. The
  Weyl check (§4c) confirms that no eigenvalue is missing.
- **Superseded by the consolidation (S9b).** The routine described in the three bullets above
  (single-window slicing) can silently drop an eigenvalue that ARPACK misses inside a window; the
  moduli experiment found this (`moduli/REPORT.md` §4a). It is no longer used anywhere under
  `numerics/`: `solve.py:eigenvalues_robust` (every eigenvalue covered by two independent windows,
  ARPACK misses counted and repaired) is the only eigensolver, and the old routine is kept, unused,
  in `legacy/single_window.py`. The committed `data/eigenvalues_*.csv` were produced with the old
  routine; the four production problems were rerun with the new one on 2026-10-10 (eigenvalues in
  `data/double_window/`), and the comparison is in `data/rerun_double_window_comparison.json`: same counts
  below the common cut, largest relative difference 1.4e-14, no ARPACK miss repaired.
- About 1420–1440 eigenvalues are computed per triangle and boundary
  condition, up to λ ≈ 21 700 (Neumann) and 23 800 (Dirichlet). The pillows
  therefore have about 2850 eigenvalues each, to λ ≈ 21 700.

**Levels and wall time** (solver only, under load):

| level (h, p) | ndof, (2,8,8) N | role |
|---|---|---|
| (0.1, 10) | 9 071 | h-sweep |
| (0.07, 8) | 11 277 | p-sweep |
| (0.07, 10) | 17 526 | h- and p-sweep; conservative error bar |
| (0.07, 12) | 25 147 | p-sweep; error estimate |
| **(0.05, 10)** | 35 641 | **production** |

The production level took 4–16 min per problem. The whole suite took about
1.5 h of solver time.

## 4. Validation

All checks are asserts in validate.py; run with `python validate.py`. The output
of the committed run ends with ALL VALIDATION CHECKS PASSED.

### (a) Convergence and error per eigenvalue

The error estimate of each production eigenvalue is
|λ(0.05,10) − λ(0.07,12)|. These are two independent discretisations whose
agreement (≈1e-11) is about 1000× tighter than the next coarser levels. As a
worst-case bound, |λ(0.05,10) − λ(0.07,10)| is also carried in every table and
propagated separately.

| | max rel. error, first 500 (estimate / conservative) | rel. error @1000 | h-rate at p = 10 | error ratio p = 8 → 10 |
|---|---|---|---|---|
| (2,8,8) N | 1.7e-11 / 9.0e-9 | 4.5e-9 | 13.4 | 199 |
| (2,8,8) D | 2.9e-11 / 1.2e-8 | 5.9e-8 | 13.0 | 145 |
| (3,3,12) N | 8.5e-13 / 1.2e-9 | 1.1e-9 | 18.8 | 350 |
| (3,3,12) D | 2.6e-12 / 5.4e-9 | 4.0e-11 | 18.8 | 325 |

The target of 1e-8 relative for the first 500 is met with a margin of 300× or
more. Even the conservative bound stays ≤ 1.2e-8.

**No corner singularity.**

- The empirical h-convergence of eigenvalues is h^13 to h^19 at p = 10. The
  p-convergence is geometric: a factor 150–350 per two orders. (The h-rates
  are pre-asymptotic medians over mid-spectrum modes. The netgen meshes at
  different h are not nested.)
- A singular corner exponent would cap the rate at an h-independent algebraic
  order and flatten the p-convergence. Neither occurs. This is what the
  reflection argument predicts: at a corner of angle π/k the eigenfunctions
  extend by reflection to smooth Z_k-symmetric functions.
- All modes converge monotonically from above, as conforming Galerkin requires.

### (b) Benchmark: Bolza surface (Strohmaier–Uski)

Reference: Strohmaier & Uski, *An algorithm for the computation of eigenvalues,
spectral zeta functions and zeta-determinants on hyperbolic surfaces*,
Comm. Math. Phys. 317 (2013), arXiv:1110.2150. Ancillary file
eig-bolza-refined0-1000.txt: 1000 eigenvalues, the first 500 "to a precision
of 12 digits" (§7).

The Bolza surface covers the (2,3,8) orbifold. Every eigenvalue of the
(2,3,8) triangle with a sign character of its reflection group therefore
appears in Bolza's spectrum.

- The relation (r_ab r_bc)³ = 1 at the π/3 corner forces equal signs on the
  sides ab and bc. That leaves four characters: N, D, M1 (D on ab and bc),
  and M2 (D on ac).
- These one-dimensional characters should account exactly for the
  multiplicity-one Bolza eigenvalues.

Result (data/bolza_benchmark.csv):

- Bolza has 42 multiplicity-one eigenvalues below 998.
- Our four triangle problems produce exactly 42 eigenvalues in that range:
  N 15, D 6, M1 10, M2 11.
- They match one-to-one, worst relative difference **5.7e-11**. For example,
  23.0785584813814 against 23.0785584813816, and 222.371124207113 against
  222.371124207114.
- There are no unmatched values in either direction.

### (c) Weyl law

Two-term Weyl law with constant, for each triangle:

N_{N/D}(λ) ≈ Aλ/(4π) ± Lλ^{1/2}/(4π) + a₀/2, with A = π/4 and a₀/2 = 67/96.

- The boundary terms follow from Uçar Cor. 4.18 (β_ν).
- The constant follows because the dihedral corners contribute half the cone
  terms equally to N and D (Uçar Thm 4.20(iii)), and Z_N + Z_D has constant
  a₀ (paper eq. (3)).

| | mean of N − Weyl₃ | rms | mean of N − area term only, last 100 eigenvalues |
|---|---|---|---|
| (2,8,8) N / D | −0.000 / −0.000 | 0.66 / 0.70 | +65.1 / −66.6 |
| (3,3,12) N / D | −0.003 / +0.000 | 0.66 / 0.68 | +63.5 / −64.9 |

The residual is centred on zero with O(1) fluctuations over 1420+
eigenvalues: no eigenvalue is missing or duplicated. Without the boundary term
it drifts by ±L√λ/(4π) ≈ ±65.

### (d) The individual heat traces

| | area from free fit of Z | a₀ from fit of Z − Area/(4πt) | a₁ fit / exact | max \|Z − (Selberg identity + elliptic)\|, t ≤ 0.03 |
|---|---|---|---|---|
| (2,8,8) | 1.5707963316 (π/2 = 1.5707963268) | 1.3958333171 (67/48 = 1.3958333333) | −3.33539 / −1601/480 = −3.33542 | 7.1e-13 |
| (3,3,12) | 1.5707964223 | 1.3958327089 | −5.4176 / −867/160 = −5.4188 | 7.1e-13 |

The error budget is ≤ 1.5e-11 (eigenvalue errors plus truncation tail).

- **Selberg identity + elliptic.** The identity term
  Area/(4π) ∫ r tanh(πr) e^{−t(1/4+r²)} dr plus the elliptic terms of all cone
  points are the exact trace minus closed-geodesic terms, which are below
  1e-12 for t ≤ 0.03. Agreement to 7e-13 checks the solver and the doubling
  principle together.
- **Mirror term.** Z_N − Z_D agrees with the mirror term
  L e^{−t/4}/(4√(πt)) (Uçar Cor. 4.18) to 1.8e-13 for t ≤ 0.012.
- **Exponentially small extra terms in Z_N − Z_D.** Beyond t ≈ 0.02, the
  difference picks up a term e^{−d²/4t} with d ≈ 1.50 for (2,8,8) and 1.65
  for (3,3,12). These are orientation-reversing (side-to-side bounce)
  orbits, e.g. the altitude orbit of length 2 × 0.764 = 1.529 in (2,8,8).
  They cancel in Z_N + Z_D.
- **Closed geodesics.** Z − (identity + elliptic) for t ∈ [0.06, 0.5] is
  fitted by the trace formula's hyperbolic term, using the shortest enumerated
  lengths. The leading multiplicity comes out as **1.997** for ℓ = 2.2568
  (2,8,8) and **1.9998** for ℓ = 1.8626 (3,3,12): one geodesic, two
  orientations. This confirms that no shorter closed geodesic exists.

## 5. The heat trace and its difference

**Truncation tail** (rigorous in spirit). For each triangle and boundary
condition,

Σ_{λ>Λ} e^{−λt} ≤ −n e^{−Λt} + t ∫_Λ^∞ e^{−λt} N_up(λ) dλ,

with N_up = Aλ/(4π) ± L√λ/(4π) + C_up. C_up is twice the largest observed
excess of N(λ) over the two-term law, plus 10. The integral is in closed form
via Γ(3/2, Λt).

At t = 0.0015 the tail is ≤ 7.6e-13, against c₁t = 3.1e-3.

**Eigenvalue errors.** Propagated as t Σ err_j e^{−(λ_j−err_j)t}. Over the fit
window the total error in D is ≤ 2.9e-11 (conservative: ≤ 3.9e-10).

**Asserted preconditions over the fit window:**

- tail < 1e-9 c₁t;
- eigenvalue error < 1e-6 c₁t;
- geodesic terms < 1e-12 c₁t.

**Closed geodesics.**

- The shortest lengths are 2.2568, 2.8816, 3.0571 for (2,8,8) and 1.8626,
  2.9807, 3.4027 for (3,3,12). They come from enumerating triangle-group words
  of length ≤ 10, and their multiplicities are confirmed by the data (§4d).
- Using the trace formula with multiplicity 8 per length, the geodesic term is
  at most **3.4e-31** over [0.0015, 0.012], 5e-19 at t = 0.02, and about 0.1
  at t = 0.5.
- In the computed D(t), the departure from the exact elliptic difference is
  −7.6e-8 at t = 0.05, −2.0e-4 at 0.1, −1.2e-2 at 0.2 and −5.5e-2 at 0.5. It is
  dominated by the ℓ = 1.8626 geodesic of (3,3,12).
- D(t) itself changes sign at t ≈ 0.34, solely because of geodesics. The exact
  elliptic difference stays positive.

**Why the fit window is small t.**

- The coefficients grow like ν!(m_max²/π²)^ν.
- For t ≳ 0.03, c₁t + c₂t² is already the wrong sign (−0.0025 at
  t = 0.029, while D = +0.031).
- By t ≈ 0.05, geodesic terms are at the 1e-7 level and rising.

**Fit.**

- The model is D(t)/t = Σ_{ν=1}^{n} c_ν t^{ν−1}, least squares with
  column-scaled Vandermonde.
- The scan covers 9 windows inside [0.0015, 0.012] and n = 2…11, written to
  data/fits.csv.
- **Data error** for a configuration is the worst-case change of each
  coefficient under any perturbation of the data within its error bound,
  |pinv| · err.
- **Model error** is the change from n − 1 to n.
- The reported configuration minimises max(data, model) — chosen without
  reference to the predictions: window [0.0015, 0.012], n = 10.
- Neighbouring configurations agree:
  - c₁ ∈ [2.083329, 2.083333] across the eight best configurations;
  - c₂ ∈ [−73.957, −73.950].
- **Calibration.** The same fit applied to the exact elliptic difference (no
  noise) recovers c₁ to ~1e-6 and c₂ to ~0.005 in this window. These are the
  `*_on_exact_elliptic` columns of fits.csv. So the method itself is not the
  limiting factor.

**Verdict: CONFIRMED.** c₁ is within 0.4σ and c₂ within 0.5σ of the exact
rational predictions 25/12 and −1775/24.

## 6. Exports (numerics/data/)

| file | content |
|---|---|
| eigenvalues_{2-8-8,3-3-12}_{N,D}.csv | index, λ (production), error estimate, conservative error, λ at (0.07,12) and (0.07,10) |
| convergence.csv | per-eigenvalue differences across all levels |
| bolza_benchmark.csv | the 42 matched benchmark eigenvalues |
| weyl.csv | windowed counting-function residuals |
| heat_trace_checks.csv | Z_FEM against Selberg identity + elliptic, Z_N − Z_D against mirror term, with error bounds |
| heat_trace_difference.csv | t ∈ [0.0015, 0.5]: Z of both pillows, D, error components (eigenvalues, tail), c₁t and c₁t + c₂t² predictions, exact elliptic prediction, residual, geodesic bound |
| fits.csv | all fit configurations, with the same fits on the exact elliptic difference |
| headline.json | headline numbers, verdict, 3-term fits, error budgets |
| heat_kernel_diagonal.npz | pillow heat-kernel diagonal K(t,x,x) at t = 0.005, 0.01, 0.02 (see below) |

**heat_kernel_diagonal.npz.**

- Evaluated at the vertices of a fine triangulation of each triangle (2128
  for (2,8,8), 2119 for (3,3,12)); points and triangles are included.
- Coordinates are in the Poincaré disk; normalisation is hyperbolic, with
  ∫K dA = Z.
- Contains K_pillow = (K_N + K_D)/2 and the triangle kernels.
- Built from 1420–1440 eigenfunctions per condition at level (0.07, 10).
- Sanity checks:
  - interior values equal (4πt)^{−1}(1 − t/3) (e.g. 15.889 at t = 0.005);
  - at a cone point of order k, values approach k/(4πt) (190.7 at the
    order-12 point at t = 0.005).

Not committed: raw solver runs (numerics/runs/, regenerated by
`python solve.py suite` and `python solve.py bench`) and the fetched papers
(numerics/refs_cache/, regenerated by fetch_refs.sh).

## 7. Limitations

- **The error estimate is not a rigorous bound.** The per-eigenvalue estimate
  is an a-posteriori agreement of two independent discretisations, not a
  certified enclosure. The conservative alternative (coarse-mesh difference)
  bounds it with a large margin, and the verdict is unchanged under it.
- **The tail bound is conditional.** It assumes the counting function beyond
  the computed range stays below the two-term Weyl law plus twice the largest
  observed excess. This is standard and generous (the observed rms is 0.7),
  but not proven.
- **Geodesic enumeration is by word length (≤ 10).** It is confirmed for the
  shortest length by the data (multiplicity 2.00). Its role here is only to
  show geodesic terms are below 1e-30 in the fit window, which holds for any
  ℓ_min ≳ 0.5.
- **Mesh rates are approximate.** The netgen meshes are not nested, so the
  quoted h-rates are approximate. The p-sweep is on a fixed mesh and is
  clean.
- **c₃ is tested only as a by-product.** At the headline configuration the fit
  gives c₃ = 3184.5 ± 5.2 (data error only), against the predicted
  153025/48 = 3188.0. Across the stable configurations it ranges over
  3180–3188, with model error comparable to the deviation. c₄ and higher are
  not tested. The pointwise agreement of D(t) with the exact elliptic
  difference to 4e-13 is the stronger all-orders statement, but it uses the
  trace formula as the prediction rather than the paper's coefficients.
- **The principle is tested only in combination.** The doubling principle is
  proved (§1). Numerically it is tested in combination with the trace formula
  (§4d), not in isolation.

## 8. Reproduce

```
python3.13 -m venv numerics/.venv && numerics/.venv/bin/pip install -r numerics/requirements.txt
cd numerics && ./fetch_refs.sh                 # literature + Bolza data (headless)
.venv/bin/python geometry.py                   # geometry checks
.venv/bin/python solve.py bench                # (2,3,8) benchmark runs, ~20 s
.venv/bin/python solve.py suite                # 4 problems x 5 levels, ~1-1.5 h on 8-core M1
.venv/bin/python validate.py                   # Step 4, all asserts
.venv/bin/python validate_committed.py         # the same checks from the committed CSVs only; no NGSolve, no solver runs
.venv/bin/python heat_trace.py                 # Step 5: fits, CSVs, headline.json
.venv/bin/python heat_trace.py kernel          # Step 6: heat_kernel_diagonal.npz, ~30 min
```
