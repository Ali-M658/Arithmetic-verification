# Blind check of the round-6 changes to Paper B (returned text, saved verbatim; the checker could not write files)

I couldn't write REPORT.md because the write was refused, so the full findings are below. Every proof in the six items holds, and every constant I recomputed matches the paper. The only problems are three discrepancies in the prose and numbers of Section 7; nothing in the mathematics is wrong.

I worked only from the PDF, with pages rendered to read formulas exactly, and my own code in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/blind-check-B/scratch/code/` (`heat.py`, `num.py`, `consts.py`, `test71.py`, `runtri.py`, `deldup.py`).

## 1. Lemma 2.2: VERIFIED

**(i)** The Dirichlet domain at a point with trivial stabiliser is a fundamental domain of area Area(O) and lies in B̄(x̃0, diam). A representative whose axis meets F at ỹ satisfies d(x̃0, γx̃0) ≤ 2d(x̃0, ỹ) + ℓ(γ) ≤ ℓ(γ) + 2 diam. The translates γF are disjoint and lie in B(x̃0, x + 3 diam), whose area is at most π e^{x+3diam}. So the count is at most π e^{x+3diam}/Area(O).

**(ii)**
- **Starting bound.** It uses ℓ(γ0) ≤ ℓ(γ), e^{−t/4} ≤ 1, and 2 sinh(x/2) ≥ e^{x/2}(1 − e^{−ℓ}) for x ≥ ℓ. All correct.
- **φ is decreasing.** (log φ)′ is decreasing in x and is negative at x = ℓ once t < ℓ²/(2 − ℓ). The stated range t ≤ ℓ²/(2(1+ℓ)) lies strictly inside that.
- **Integration by parts.** The boundary terms vanish because n_O(ℓ−) = 0 and n_O·φ → 0.
- **Remaining integral.** The identity x e^{x/2−x²/4t} = −(2tx/(x−t)) d/dx e^{x/2−x²/4t} holds, t < ℓ on the range, and x/(x−t) ≤ ℓ/(ℓ−t). Together these give exactly B_C.
- **Monotonicity in ℓ.** I recomputed the logarithmic derivative and it matches the paper. The bracket is ≥ 0 exactly on the range, so B_C decreases in ℓ.
- **Lower bound ℓ for the systole.** The proof needs only n_O = 0 below ℓ and the sinh inequality, so any lower bound works without the monotonicity.
- **Bound for all t.** The maxima are at x = 2√t (value 2√t e^{−1/2}) and at x = 6t (value e^{9t/2}). Also Σ e^{−2ℓ(γ)} ≤ 2C e^{−ℓ}, and 9/2 − 1/4 = 17/4. This gives the constant 2C/(√π(1 − e^{−ℓ})) · e^{17t/4 − 1/2 − ℓ}.
- **Sanity check.** On the Table 5 data, Z − G_true is positive and far below the bound.

## 2. Lemma 4.5, with Lemmas 4.2–4.3: VERIFIED

**Lemma 4.2.**
- If X > 1, then cosh h = X ≤ cosh d, so d ≥ ε/2.
- If X < 1, the defect is at least π/(abc) and cos((θ−α−β)/2) ≥ sin(π/2M) ≥ 1/M. This gives cosh d − 1 ≥ 2/(π²cM) ≥ 2/(π²M²).

**Lemma 4.3.** Both cases hold, with ε ≥ 2d0 = 4r0 ≥ 2ρ1. It supplies exactly the v0 that Lemma 4.5 uses.

**Lemma 4.5, step by step.**
- The maximal 4r0-separated set gives disjoint 2r0-balls, so |Y| ≤ A/v0.
- After moving to a cone point within r0, every point is within 5r0 of some b. Repeated b's only over-count.
- Separation of orbit points of distinct cosets by 2ρ1:
  - Cone-point case: γb̃ is another elliptic point, at distance ≥ 2r0 ≥ 2ρ1.
  - Regular case: hyperbolic elements move b̃ by ≥ ε ≥ 2ρ1, and elliptic ones by ≥ 2ρ1 via (H1).
- Orbit count: the disjoint ρ1-balls lie in B(b̃, R + ρ1), so the count is at most M(cosh(R + ρ1) − 1)/(cosh ρ1 − 1).
- Displacement: d(b̃, γb̃) ≤ 2·5r0 + ℓ(γ) ≤ x + 10r0. Distinct classes give distinct γ.
- The final inequality ≤ K e^x follows from cosh u − 1 ≤ e^u/2.

**K for A = π/2, ε = 1.8626, M = 12.**

| Quantity | Value | Note |
|---|---|---|
| d0 | 0.0530454 | the order term binds |
| r0 | 0.0265227 | |
| ρ1 | 0.00686533 | |
| v0 | 1.48073e−4 | the ρ1 branch is the smaller one |
| **K** | **3.5454 × 10⁹** | |

This matches Table 3 (3.5e9) and Table 4. All eight K values in Table 3 reproduce, as does the text's range of 4 × 10⁵ to 7 × 10¹⁰ (I get 4.01e5 to 7.09e10). Table 2 also reproduces.

## 3. Theorem 6.2: VERIFIED; all eight rows of Table 3 recomputed

**Definitions.**
- The factor 3 in ϖ needs t ≤ ε/2, and t2 ≤ ε/2 holds.
- B* increases for t < ε²/2.
- I re-derived the condition B* ≤ Θ/8 as e^{−y} y^p ≤ (γ*/16ϖ)(ε²/4)^p with p = k* − 3/2 > 0. The bound max y^p e^{−y/2} = (2p/e)^p shows it holds for every y ≥ y0, so for every t ≤ t3.
- At t = t3 itself, B*(t3)/(Θ(t3)/8) is between 1e−20 and 3e−8 across the rows.

**Tail and perturbation.**
- Θ* ≤ 1/8, so Hyp ≤ 1 and Z♯ is valid for s ≤ t*.
- Λt* ≥ 2 log 64 > 1, so N > eZ_O(1/Λ).
- The tail with s = t*/2 equals exactly Θ*/8, the perturbation is at most Θ*/(8e), and the total is < 3Θ*/8 against a gap of Θ*.
- The Θ*/16 decision-rule margin and replacing t* by a rational t ≤ t* both hold.

**Parenthetical on the weakened hypothesis.** It is correct as stated. The gloss "allows errors growing like e^{λj t*}" is accurate only for over-estimates, or when t*·|error| = O(1). This is a minor wording point.

**Table 3.** Every printed column matches in all eight rows, and the "binds" column is right: t1 everywhere except ε = 0.1, where t3 binds; t2 never binds. Two examples:

| Row | K | t1 | t3 | Θ* | Λ | N | δ |
|---|---|---|---|---|---|---|---|
| π/2, 1.8626, M = 12 | 3.545e9 | 6.849e−9 | 1.11e−2 | 4.23e−22 | 2.01e10 | 6,817,584,874 | 4.17e−25 |
| 2π, 0.1, M = 3 (t3 binds) | 8.06e7 | 7.76e−4 | 3.48e−5 | 4.83e−8 | 1.68e6 | 2.281e6 | 2.80e−11 |

The Theorem 6.2 values quoted in Table 6 (6.8e9, 4.3e4, 7.4e12) are right, because t1 binds for every ℓ listed there.

## 4. Appendix A: VERIFIED, every proof

- **Lemma A.1 (admissibility).** η_T is supported in [−2ϵ, 2ϵ], which gives #{λ ≤ x} = O(x). The domination comes from Lemma 2.2(i), so there is no circularity, and the bound |f̂_X| ≤ ϵ_X min(1, |r|⁻³) works.
- **Lemma A.2 (closed form of Φm).**
  - The cotangent identity and the Bernoulli signs are correct.
  - Numerically, the closed form and the direct sum agree to about 1e−38 for m = 2, 3, 5, 7, 12.
  - The Taylor coefficients match mφk for k ≤ 4.
- **Proposition 2.3(a).**
  - The beta integral, the moment identity and g_k are correct.
  - b_l agrees with the definition through p_l.
  - All remainder terms have sign (−1)^K, so the moduli add to exactly |b_K| t^K.
- **Proposition 2.3(b).**
  - The three remainder pieces all have sign (−1)^{K+1}.
  - μ_k = (1 − 2^{−2k−1})(−1)^k B_{2k+2}/(k+1) holds; I checked it via the Dirichlet eta function.
  - The closed form of α_k equals the recursion in exact arithmetic: 1, −1/3, 1/15, −4/315, 1/315, −4/3465.
- **Numerical checks of Proposition 2.3.**
  - The sign and size of the remainder hold numerically for m ∈ {2, 3, 7, 12}, t ∈ {0.01, 0.1, 0.5} and K ≤ 5 in (a), and for t up to 2 and K ≤ 6 in (b).
  - |b_K(m)| is strictly increasing in m for K ≤ 7 and m ≤ 20.
- **Lemma A.3 (cone polynomials).** For l ≤ 4, p_l is even with rational coefficients, of degree 2l + 2, with p_l(1) = 0, leading coefficient a_l, and the exact ψ-expansion. The triangular basis is correct.
- **Lemma 3.1.** R(U) − R(V) = 0; the paddings and P_{2k−1} = Ψ_k + R are correct.
- **Lemma 3.3.** The examples check out: d2 = −1/12 for (0;4,4,4) against (0;3,4,6), and d3 = 25/12 for O(2,8,8) against O(3,3,12).
- **Parity lemma.** Correct: every product of power sums in e_j with j odd contains an odd index.
- **Theorem 3.2(i).**
  - κ is even because |V*| − |U*| = 2(g − g′).
  - The odd e_j vanish, so U* = V* = ∅.
  - **Use of |U| + |V| = n + n′ + |d|:** this equals 2 max(n + g − g′, n′ + g′ − g) in both signs of d. That is at most 2(⌊A/π⌋ + 4) because n + g − g′ ≤ n + 4g ≤ A/π + 4. Correct.
- **Theorem 3.2(ii).** The Vandermonde column-reduction argument is correct.

## 5. Section 7: Theorem 7.1 VERIFIED; three discrepancies in the text

**Theorem 7.1 with a general C.** The proof uses only n_O ≤ Ce^x, through H, so it holds for any valid C. (C2) implies (C1).

**Rerun from the Table 5 eigenvalues.** I reran the test on the triangle orbifolds:
- The set S is the 6 signatures of area π/2 with orders ≤ 12, enumerated myself.
- The diameter bounds 2 diam P = 4.89690 and 4.31634 are in closed form, and K = 3.545e9.
- The errors ϵj were inflated by 5e−7 to cover the 6-decimal rounding.

| Orbifold | Criterion | Mine (time) | Table 6 (time) |
|---|---|---|---|
| O(2,8,8) | (C1), Δ | 18 (0.0564) | 18 (0.0565) |
| O(2,8,8) | (C2), Δ | 20 (0.0557) | 20 (0.0556) |
| O(2,8,8) | (C1), K | 24 (0.0430) | 24 (0.0432) |
| O(3,3,12) | (C1), Δ | 25 (0.0412) | 25 (0.0412) |
| O(3,3,12) | (C2), Δ | 29 (0.0403) | 29 (0.0402) |
| O(3,3,12) | (C1), K | 36 (0.0296) | 36 (0.0295) |

No wrong signature was ever singled out. For the family (Oϑ), the signature sets (|S| = 3 and 10) and the Table 4 systoles (4b) and 2 diam P values all reproduce. Their eigenvalues are not in the PDF, so their counts could not be rerun.

**Robustness sentence: verified.** With r = 1e−4 the counts stay at 18 and 25. With r = 1e−3, (C1) fails for every N ≤ 39, which is as far as the printed data go.

**"19 of 24" deletions/duplications.** I reproduce 19/24 if "conclude" means the first N at which (C1) singles out a signature. If it means at any N, I get 23/24, so the wording should say "first".

**Discrepancies.**
- **Stale paragraph (§7.1, "The test").** It says Table 6 gives estimates where the criterion fails, and cites 4412 and 4423 for ϑ = 1.6, M = 3. Table 6 has no estimates: every count is ≤ 933, inside the complete ranges (Nc ≥ 4357). For ϑ = 1.6, M = 3 the counts are 156, 177 and 121. The paragraph does not match the current tables and should be removed or rewritten.
- **"Factor of at most 1.6".** The improvement from knowing the diameter is at most 44/28 = 1.57, so that direction holds. But at ϑ = 2.8, M = 3 the counts are 767 (Δ) against 461 (K), a factor of 1.66. Read as a bound on how much the counts change in either direction, "at most 1.6" is slightly false. It should say "at most 1.7" or name the direction.
- **"At least 3.0 × 10⁻³".** The nearest gap at t = 0.0015 is 2.9686e−3 (checked by 30-digit quadrature). The figures "about 2 × 10⁸ budgets", λ < 1.66 × 10⁴ and 9.8 × 10³ are correct.

**Loose but not false.**
- The gap to Theorem 6.2 is "10² to 2 × 10³" at M = 3 and "10¹⁰ to 2 × 10¹¹" for the family at M = 12; both are right. For the triangles, "2 × 10⁸" is loose: the ratios are 1.9e8 and 2.8e8.
- The Figure 2 caption's "56 to 2.7 × 10¹¹" is correct.
- "About 800 eigenvalues, below λ ≈ 2800": Weyl's law gives λ_N ≈ 3N, and it is accurate on the Table 5 data. So λ_842 ≈ 2500, and λ ≈ 2800 would correspond to about 930 eigenvalues.
- "(λ̃_N − ϵ_N)t of about 8 to 11" is consistent: 7.7 to 8.4 for the triangles.

## 6. "How large are N and δ": VERIFIED

- **k\* capped at M, at A = 10π, ε = 1, M = 3.** Uncapped (k\* = 14) gives N = 4.19e18; capped (k\* = 3) gives N = 1.084e6. Both match the text.
- **t3 binds for small ε (A = 4π/3, M = 3).** t3 overtakes t1 between ε = 0.45 and 0.43, so it binds for all ε ≤ 0.42.
- **Growth per halving of ε.** Successive halvings from 0.42 multiply N by 5.24, 5.13, 5.01, 4.90, 4.81 and 4.74. Further down the factor is 4.55 near ε = 5e−4, 4.37 near 5e−6 and 4.25 near 5e−9. So "about 5, slowly decreasing towards 4" is correct.
- **K of order ε⁻⁴.** Kε⁴ tends to 4096 as ε → 0.
- **N ≈ (eA/2πt\*)·log(8Z♯/Θ\*).** At A = 4π/3 this gives 43170, against the exact 43190.

## Summary

| # | Item | Verdict |
|---|---|---|
| 1 | Lemma 2.2 | VERIFIED |
| 2 | Lemma 4.5 (with 4.2–4.3); K = 3.5454e9 | VERIFIED, matches Tables 3 and 4 |
| 3 | Theorem 6.2; Table 3 | VERIFIED, all 8 rows reproduce; minor wording in the parenthetical |
| 4 | Appendix A | VERIFIED |
| 5 | Theorem 7.1 and Section 7 statements | VERIFIED, with 3 discrepancies: the stale "estimates / 4412 / 4423" paragraph, "at most 1.6" against 1.66, and "at least 3.0e−3" against 2.97e−3 |
| 6 | "How large are N and δ" | VERIFIED |
