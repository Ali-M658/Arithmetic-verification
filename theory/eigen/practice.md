# The a-posteriori test of Theorem 7.1 on the computed spectra

Scripts: `instances.py` (geometric inputs, writes `data/instances.csv`; about 1.5 min) and `practice.py`
(the test, writes `data/practice.csv`, `data/practice_t.csv`, `data/practice_inputs.csv`,
`data/triangle_spectra_first41.csv`, `data/table2.csv`; about 3 min). Both read `numerics/` and write
nothing there; both are deterministic (two runs give byte-identical CSVs) and raise on a failed check.
Methods, with file:line references for the spectra: `METHODS.md`.

    .venv/bin/python theory/eigen/instances.py && .venv/bin/python theory/eigen/practice.py

What is and is not rigorous. The systole lower bounds and the diameter bounds B1, B2 are proved (complete
enumeration in 40- and 50-digit arithmetic; an elementary argument). The eigenvalue errors ε_j are
a-posteriori estimates (agreement of two discretisations), not enclosures, and completeness of each list
rests on the trace test and the solver checks of `METHODS.md` §5. So every count below is "the criterion of
Theorem 7.1 holds with the estimated ε_j and the stated complete range", not a certificate.

## The test

O of area A, signature in S = {signatures of area A with orders ≤ M}, systole ≥ ℓ, diameter ≤ Δ,
β = max_{σ∈S} Σ b₀(m_i), computed λ̃_0 ≤ … ≤ λ̃_N with errors ε_j. With H the bound of Lemma 2.3 and
Z̃_N(t) = Σ_{j<N} e^{−λ̃_j t},

E_N(t) = H(t) + inf_{0<s≤t} e^{−(λ̃_N−ε_N)(t−s)} (A/4πs + β + H(s)) + t Σ_{j<N} ε_j,

- **(C1)** exactly one σ ∈ S has |Z̃_N(t) − G_σ(t)| ≤ E_N(t);
- **(C2)** σ has it and E_N(t) < ½ min_{σ'≠σ} |G_σ(t) − G_σ'(t)|.

**N_test(C)** = the least N for which (C) holds at some t (N eigenvalues in the sum, plus λ̃_N in the
tail). Computed on 400 log-spaced t in [0.002, 1] and 300 in [10⁻⁵, 0.002), refined by 61 points in the
bracket of each minimising grid point; inf over s on a 240-point log grid via a lower-convex-hull query,
then re-checked with bounded Brent minimisation at the reported count (any s gives a valid bound). The
conclusion was σ₀ in every case where (C1) or (C2) held (asserted).

**N_obs** (the manuscript's definition, made precise): the least N such that |Z̃_{N'}(t) − G_σ₀(t)| <
½ gap(t) for every N' from N to the end of the complete range, minimised over the same t-grid.
**N_rule**: the least N from which on the nearest-signature rule argmin_σ |Z̃_{N'}(t) − G_σ(t)| returns σ₀.
Both use the true signature and the data (the true closed-geodesic term), so neither is a decision rule;
N_rule is unstable (it is 1 at t ≈ 0.81 for the family at M = 3, where Z̃_1 = 1 happens to be nearest to
G_σ₀). Recommendation: keep N_obs only with this definition and the t, or drop both.

## Inputs (per example)

Area: π/2 for the triangles, 4π/3 for the family. ε of the systole = the computed value rounded down at 6
decimals (40-digit value minus lower bound ≥ 5.5×10⁻⁸ in every case, against a round-off below 10⁻³⁰).

| orbifold | systole (computed) | lower bound ℓ | 2nd length | diam P = true diam O | B1 = 2 diam P | B2 | D(A,ℓ,M) | complete range: λ ≤ / N |
|---|---|---|---|---|---|---|---|---|
| O(2,8,8) | 2.25676793 | 2.256767 | 2.881637 | 2.448452 | 4.896905 | 2.448873 | 1125.4 (M=12) | 16000 / 2002 |
| O(3,3,12) | 1.86260406 | 1.862604 | 2.980681 | 2.158170 | 4.316340 | 2.318716 | 1125.4 (M=12) | 16000 / 2001 |
| O_τ, τ=0.0 | 2.63391579 | 2.633915 | 3.133598 | 2.292432 | 4.584863 | 3.400218 | 150.94 (M=3), 3001.2 (M=12) | 13360 / 4451 |
| τ=0.4 | 2.20269529 | 2.202695 | 2.820281 | 2.335597 | 4.671195 | 3.175616 | same | 13341 / 4448 |
| τ=0.8 | 1.83130274 | 1.831302 | 2.574392 | 2.460809 | 4.921618 | 3.074003 | same | 13315 / 4437 |
| τ=1.2 | 1.51573792 | 1.515737 | 2.387417 | 2.656991 | 5.313982 | 3.090188 | same | 13274 / 4424 |
| τ=1.6 | 1.25042850 | 1.250428 | 2.249219 | 2.910102 | 5.820204 | 3.208924 | same | 13266 / 4424 |
| τ=2.0 | 1.02912884 | 1.029128 | 2.058258 | 3.206447 | 6.412895 | 3.409558 | same | 13199 / 4400 |
| τ=2.4 | 0.84559363 | 0.845593 | 1.691187 | 3.534403 | 7.068806 | 3.671392 | same | 13155 / 4387 |
| τ=2.8 | 0.69399455 | 0.693994 | 1.387989 | 3.884871 | 7.769742 | 3.976964 | same | 13076 / 4357 |

- **Systole.** Complete enumeration with a displacement cutoff (`instances.py`, docstring item 1): every
  closed geodesic of length ≤ L = 4 has a representative g with d(x₀, gx₀) ≤ L + 2r (x₀ the Klein centroid
  of P, r = max_{y∈P} d(x₀, y)); all tiles of the reflection tiling within L + 3r were enumerated
  breadth-first (2617–36142 tiles). The systole is the least length found; it is ≤ L. The family systole is
  4b (asserted to 10⁻³⁰), the length of the common perpendicular of the north and south sides run up one
  sheet and down the other; its second length is 2×systole for τ ≥ 2.0. Note: the manuscript's 2.256768
  for O(2,8,8) is the systole **rounded up** (true value 2.2567679299); 2.634 and 0.694 (Table 2) are also
  rounded up (2.6339158, 0.6939946). 1.862604 and 1.8626 for O(3,3,12) are valid lower bounds.
- **`numerics/moduli` enumeration** (`geodesics.py:164-230`, the family systoles in `geometries.json`)
  is complete in the same sense: base point the centre of Q, r_P = d(0, V), kept elements with
  d(o, go) ≤ ℓ_max + 2r_P, pruned at ℓ_max + 3r_P, ℓ_max = 6.5 — the same displacement-cutoff argument,
  in float64. Its systoles agree with the 40-digit ones to < 10⁻¹² (asserted).
- **Diameter.** True diam O = diam P (the largest vertex distance; for the triangles the longest side,
  between two cone points) in all ten cases: the search over pairs in opposite copies (grid + Nelder–Mead,
  f(x,y) = min_{z∈∂P} d(x,z) + d(z,y)) found nothing larger. Rigorous bounds: B1 = 2 diam P (a vertex v is
  common to both copies: d(x, y') ≤ d(x,v) + d(v,y) ≤ 2 diam P; same copy ≤ diam P) — this is the
  manuscript's "twice the longest side" and `geometries.json`'s `diam_O_upper_bound`; and B2 = max(diam P,
  2 max_v d(z, v)) for one point z ∈ ∂P (the same argument through z), with z chosen to minimise
  max_v d(z,v). For O(2,8,8), B2 = 2.4489 exceeds the true diameter by 4×10⁻⁴.
- **D(A, ε, M)** of Theorem 4.4 with ε = ℓ. For the family it does not depend on ℓ (d₀ = arccosh(1 +
  2/(π²M²)) < ℓ/2 for every member).

## Results (instance inputs Δ = B1, ε_j = err_estimate, full committed spectra)

| orbifold | M | \|S\| | N_test(C1) (t) | N_test(C2) (t) | λ̃_N at C2 | N_obs (t) | Thm 6.2 N |
|---|---|---|---|---|---|---|---|
| O(2,8,8) | 12 | 6 | 18 (0.0565) | 20 (0.0556) | 148.4 | 3 (0.27) | 6.82×10⁹ |
| O(3,3,12) | 12 | 6 | 25 (0.0412) | 29 (0.0402) | 227.3 | 3 (0.23) | 6.82×10⁹ |
| O_τ, τ=0.0 | 3 | 3 | 24 (0.0897) | 28 (0.0858) | 88.1 | 3 (0.45) | 43188 |
| τ=0.4 | 3 | 3 | 36 (0.0626) | 43 (0.0609) | 127.9 | 3 (0.40) | 43188 |
| τ=0.8 | 3 | 3 | 58 (0.0424) | 67 (0.0407) | 202.6 | 4 (0.29) | 44943 |
| τ=1.2 | 3 | 3 | 94 (0.0277) | 106 (0.0268) | 318.2 | 5 (0.20) | 67872 |
| τ=1.6 | 3 | 3 | 156 (0.0176) | 177 (0.0171) | 530.1 | 9 (0.13) | 103136 |
| τ=2.0 | 3 | 3 | 265 (0.0110) | 296 (0.0107) | 890.1 | 15 (0.082) | 157376 |
| τ=2.4 | 3 | 3 | 451 (0.00685) | 500 (0.00668) | 1502.9 | 25 (0.052) | 240781 |
| τ=2.8 | 3 | 3 | 767 (0.00425) | 848 (0.00415) | 2539.5 | 43 (0.033) | 368973 |
| τ=0.0 | 12 | 10 | 28 (0.0856) | 33 (0.0840) | 99.5 | 4 (0.37) | 7.44×10¹² |
| τ=0.4 | 12 | 10 | 43 (0.0607) | 48 (0.0592) | 145.3 | 4 (0.33) | 7.44×10¹² |
| τ=0.8 | 12 | 10 | 67 (0.0407) | 77 (0.0396) | 227.7 | 6 (0.22) | 7.44×10¹² |
| τ=1.2 | 12 | 10 | 106 (0.0268) | 122 (0.0260) | 362.9 | 9 (0.15) | 7.44×10¹² |
| τ=1.6 | 12 | 10 | 177 (0.0170) | 201 (0.0165) | 604.0 | 14 (0.10) | 7.44×10¹² |
| τ=2.0 | 12 | 10 | 295 (0.0107) | 332 (0.0104) | 1000.0 | 23 (0.065) | 7.44×10¹² |
| τ=2.4 | 12 | 10 | 499 (0.00667) | 557 (0.00651) | 1668.7 | 38 (0.042) | 7.44×10¹² |
| τ=2.8 | 12 | 10 | 847 (0.00415) | 933 (0.00406) | 2801.8 | 63 (0.027) | 7.44×10¹² |

Every λ̃_N used lies below 2802, well inside the trace-test range (λ < 9.8×10³ for the family, 1.66×10⁴
for the triangles). With ε_j = err_conservative the counts are the same (triangles checked in the CSV).
The t-windows (columns `tlo_*`, `thi_*` of `data/practice.csv`) are 0.3–21% wide in t (narrowest for the smallest systoles); for O(3,3,12), C1 holds
with N = 25 for t ∈ [0.0375, 0.0452] — referee d's 25 at t ≈ 0.039.

**The manuscript's 21 and 39** were C2-type counts (E_N < gap/2) on the 17-point grid; on the fine grid C2
gives 20 and 29, and C1, the theorem's own criterion, 18 and 25 — exactly referee d's independent values
(17–18 / 20 and 25 / 29).

### Other diameter inputs (C1 / C2)

| orbifold | M | Δ = B2 | Δ = true diam | Δ = D(A,ℓ,M) (class level) |
|---|---|---|---|---|
| O(2,8,8) | 12 | 12 / 13 | 12 / 13 | > 2001; Weyl estimate 5611 / 5869 (t ≈ 3.75×10⁻⁴) |
| O(3,3,12) | 12 | 17 / 19 | 15 / 19 | > 2000; Weyl 8619 / 8985 (t ≈ 2.56×10⁻⁴) |
| τ=0.0 | 3 | 19 / 24 | 16 / 17 | **855 / 924** (t = 0.00375) |
| τ=0.4 | 3 | 28 / 31 | 22 / 24 | **1269 / 1363** (t = 0.00263) |
| τ=0.8 | 3 | 40 / 46 | 33 / 40 | **1911 / 2047** (t = 0.00182) |
| τ=1.2 | 3 | 60 / 69 | 53 / 63 | **2900 / 3099** (t = 0.00124) |
| τ=1.6 | 3 | 94 / 109 | 88 / 101 | > 4423; Weyl 4412 / 4718 |
| τ=2.0 | 3 | 153 / 174 | 148 / 169 | > 4399; Weyl 6761 / 7212 |
| τ=2.4 | 3 | 252 / 288 | 245 / 279 | > 4386; Weyl 10384 / 11051 |
| τ=2.8 | 3 | 425 / 480 | 415 / 472 | > 4356; Weyl 15967 / 16955 |
| τ=0.0 | 12 | 24 / 28 | 17 / 21 | > 4450; Weyl 23498 / 24794 |
| τ=0.4 | 12 | 33 / 36 | 25 / 30 | Weyl 34551 / 36399 |
| τ=0.8 | 12 | 46 / 54 | 40 / 46 | Weyl 51398 / 54064 |
| τ=1.2 | 12 | 69 / 81 | 64 / 73 | Weyl 77150 / 81040 |
| τ=1.6 | 12 | 109 / 125 | 101 / 116 | Weyl 116576 / 122275 |
| τ=2.0 | 12 | 174 / 201 | 169 / 193 | Weyl 176883 / 185282 |
| τ=2.4 | 12 | 286 / 329 | 279 / 320 | Weyl 268845 / 281286 |
| τ=2.8 | 12 | 479 / 539 | 469 / 530 | Weyl 409805 / 428208 (t ≈ 1.3×10⁻⁵) |

**Weyl estimate** (when no N ≤ N_complete − 1 works): λ̃_N → 4πN/A, ε_j = 0 beyond the computed range (the
computed ε_j summed in full), and Z̃_N(t) → G_σ₀(t), so that (C2) becomes E_N < gap/2 and (C1) E_N < gap;
minimised over 600 log-spaced t in [10⁻⁹, 1] plus refinement. Checked against the actual counts wherever
both exist (22 cases with B1 or D): within 8% for N < 100, 1.1% for N ≥ 100 and 0.6% for N ≥ 400.

**Like-for-like (referee a, M2).** With the class-level diameter bound D(A, ε, M) in place of the instance
bound, the counts rise from 18–29 to about 5.6–9.0×10³ for the triangles (beyond the 2000 computed), and
for the family from 24–848 to 855–1.7×10⁴ (M = 3; within the computed range for τ ≤ 1.2) and to
2.3×10⁴–4.3×10⁵ (M = 12). Theorem 6.2's own N is 6.8×10⁹ (triangles), 4.3×10⁴–3.7×10⁵ (family, M = 3) and
7.4×10¹² (M = 12). So most of the gap between "21" and "6.8×10⁹" is the instance diameter (e^{3Δ} with Δ = 4.9
against 1125); with class constants the a-posteriori route still saves a factor 10⁶ (triangles) and
2×10⁷–3×10⁸ (family, M = 12) over Theorem 6.2, but at M = 3 only a factor 20–50.

## The member τ = 2.8 (systole 0.694)

- With the **120-per-sector spectra the manuscript used** (815 eigenvalues, λ ≤ 2438): (C2) fails at every
  t in [10⁻⁵, 1] for M = 3 and M = 12, as the manuscript says; but **(C1) succeeds for M = 3 with N = 767**
  (t ∈ [0.00424, 0.00426]). For M = 12 neither criterion succeeds within 815; the Weyl estimate is 848 (C1)
  and 934 (C2), i.e. about 4% and 15% beyond the range.
- With the **full committed spectra** (`numerics/moduli/data/convergence.csv`, 4357 eigenvalues complete to
  13076), the test succeeds: M = 3: 767 (C1), 848 (C2); M = 12: 847 (C1), 933 (C2), at t ≈ 0.0041–0.0043.
  The Weyl estimates from the 815-eigenvalue data predicted 847/848 and 933/934: off by at most 1.
- Why it needs so many: H(t) carries e^{3Δ} = e^{23.3} (Δ = B1 = 7.77) and Gaussian decay e^{−ℓ²/4t} with
  ℓ = 0.694, so H(t) < gap/2 forces t ≲ 0.0045; the tail term then needs λ̃_N t ≳ 10.5–11.5, λ̃_N ≈ 2500–2800,
  and by Weyl N ≈ Aλ/4π = λ/3 ≈ 850–930. With Δ = B2 (3.98) the counts drop to 425/480 (M = 3).
- So "nine of ten" is true only of the manuscript's 815-eigenvalue lists under (C2); under (C1), or with the
  committed full spectra under either criterion, all ten succeed.

## Table 2 of the manuscript (`data/table2.csv`)

Recomputed with systole lower bounds (2.633915 for 2.634, 0.693994 for 0.694; 1.8626 is a valid lower
bound for O(3,3,12)): every printed entry is unchanged at the printed precision except row 2, t₁ =
6.8486×10⁻⁹ (printed 6.9×10⁻⁹; asserted in `practice.py`). The ε column should read 2.6339 and 0.6939 (or
"2.634⁻", "0.694⁻") instead of 2.634 and 0.694. Full-precision row values: see `data/table2.csv`.

## Files

| file | content |
|---|---|
| `data/instances.csv` | per example: systole (computed, lower bound), second length, tiles, r, diam P, B1, B2, max opposite-copy distance, true diameter, D(A,ℓ,3), D(A,ℓ,12) |
| `data/practice.csv` | per example × M × diameter input (B1, B2, true, D) × ε_j (estimate; conservative for the triangles) × data set (full; for the family also the 120-per-sector lists): N_complete, λ_complete, N_test(C1), N_test(C2) with t, t-window, λ̃_N, Weyl estimates, N_obs, N_rule (B1 only), nearest competitor, Theorem 6.2's N and t_* |
| `data/practice_t.csv` | N_test(C1), N_test(C2), N_obs, N_rule, gap, log₁₀ H for every grid t (B1, full data) |
| `data/practice_inputs.csv` | the per-example input table of the paper (area, ℓ, B1, B2, true diameter, D, M, \|S\|, β, complete range, basis) |
| `data/triangle_spectra_first41.csv` | λ̃_j, ε_j (= err_estimate), err_conservative, boundary condition and source file/index, j = 0..40, both triangle orbifolds |
| `data/table2.csv` | Table 2 with the corrected ε |
