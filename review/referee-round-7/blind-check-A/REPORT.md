<!-- Blind check A (round 7): returned text saved verbatim; the reviewer could not write files -->

# Blind check A: "How much of a hyperbolic orbifold does heat hear?"

I could not save the report as `REPORT.md`: the write was refused, so the full report is below. I used only the manuscript and supplement PDFs. Before reporting any formula I read the relevant pages as images at 110 dpi: manuscript pp. 11, 14–17, 25–29, 34–35, 37, 49–50 and supplement pp. 11–12. My scripts and outputs are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/blind-check-A/scratch/code/`, with the computed length spectra in `scratch/lenspec_*.npy`.

All eleven items check out mathematically. I found two small numerical errors and two places where the wording overstates what is proved:

- **Supplement, Section S4:** it says twice that D changes sign "near t = 0.34". I computed the zero at t = 0.3592, which agrees with the main text.
- **Remark B.4:** the condition on η is stated as "only if η ≤ 2×10⁻¹⁹", but the exact condition is η ≤ 2.07×10⁻¹⁹.
- **After Proposition 2.12:** the sentence that small metric changes destroy an equality of heat invariants is too broad (c₂ never changes), and it cites a flat-background argument that does not apply.
- **Proposition 2.13(ii):** b_l is a Laurent polynomial in m, not a polynomial.

## Summary

| # | Item | Verdict |
|---|------|---------|
| 1 | Prop. 2.12 (unknown constant curvature), its proof, and the paragraph after it | Proposition and proof **VERIFIED**; the instability sentence is a minor **GAP** |
| 2 | Remark 2.6 (a count without the diameter) | **VERIFIED**, with one condition on what the companion's count counts |
| 3 | Lemma 3.14 (a)–(c) and its proof; tests of (c) | **VERIFIED** |
| 4 | Theorem 3.15 (Descartes bound), restated hypothesis and conclusion | **VERIFIED** |
| 5 | Prop. 3.16 (Doubling): is L ≥ 2 needed and sufficient? | **VERIFIED**: needed (the statement is false for L = 1) and sufficient |
| 6 | Theorem 3.11: closed form of a·w_a, proportionality of ν(a), worked examples | **VERIFIED** |
| 7 | f(A) = O(A^α) if and only if N(k) ≥ c·k^{1/α} | **VERIFIED** |
| 8 | Section 5: the bounds ≤ 5 and ≤ 4; O(5,5,5) and (0;2,2,2,10) share c₁, c₂ | **VERIFIED** |
| 9 | Remark B.4: D, ℓ₀, δ₁, the thresholds, the ℓ₀ ≥ 0.01 claim | **VERIFIED**, except a minor **ERROR** in the η wording |
| 10 | Section 4: the three factor ranges, the sign change of D, Remark 4.3 | **VERIFIED** (the diameter-free column cannot be checked); **ERROR** in the supplement's sign-change time |
| 11 | Paragraph before Prop. 2.13; whether (ii) is well posed | Outline honestly labelled; (ii) well posed (minor wording); two minor overstatements |

## 1. Proposition 2.12 (Unknown constant curvature): VERIFIED; instability sentence: minor GAP

**Scaling.** Let O₁ be O with the metric |K|g. Then:
- **Laplacian:** Δ_{O₁} = |K|⁻¹Δ_g, so Z_{O₁}(s) = Z_O(s/|K|), which is the same as Z_O(t) = Z_{O₁}(|K|t).
- **Curvature:** the metric |K|g has curvature K/|K| = −1.
- **Coefficients:** comparing the expansions gives c_j(O) = |K|^{j−2}·c_j(O₁).
- **c₂:** the factor is |K|⁰, so c₂ does not depend on K.
- **Scale-invariant quantities:** I_j = c_j·c₁^{j−2} is scale invariant, because the factors |K|^{j−2} and |K|^{−(j−2)} cancel.
- **Curvature from c₁:** by Gauss–Bonnet c₁(O₁) = −χ/2, and c₁(O) = c₁(O₁)/|K|, so |K| = −χ/(2c₁(O)).

**Criterion.**
- **Equivalence:** I_j(σ) = c_j(σ)·(−χ(σ)/2)^{j−2}. The factor (−1/2)^{j−2} is common to both sides, so I_j(σ) = I_j(σ′) is equivalent to c_j(σ)χ(σ)^{j−2} = c_j(σ′)χ(σ′)^{j−2}.
- **Converse:** choose |K| and |K′| with c₁(σ)/|K| = c₁(σ′)/|K′|. This is always possible because both c₁ are positive. Then c_j = I_j·c₁^{2−j} agrees for 2 ≤ j ≤ L.
- **L = 1:** the condition is vacuous and the conclusion is trivially true, which is consistent.

**The paragraph after the proposition.**
- **Correct statements:**
  - With equal χ the criterion reduces to c_j(σ) = c_j(σ′).
  - Different χ "may" collide; this is not asserted to happen.
  - Theorems 1.1 and 1.2 and Corollary 1.5 hold at any known K < 0, because every c_j scales by the same factor on both sides.
  - Nothing is claimed for an unknown curvature.
- **The instability sentence has two problems (minor GAP):**
  - **Wrong citation:** it cites the proof of Prop. 2.15(ii), but that proof places the bumps in a *flat* disc and uses a flat-background variation. A curvature −1 orbifold has no flat region.
  - **Too strong:** it says an equality of heat invariants is destroyed by arbitrarily small changes. That is false for c₂, which equals χ/6 + Σ(mᵢ² − 1)/(12mᵢ) for every metric. This matters for the minimal pair, whose shared invariants are c₁ and c₂.
- **What is true:** an equality involving c₁ (the area) or some c_j with j ≥ 3 is destroyed. A direct argument: Ω₁ = (1/60π)∫K² dA, because u₂ = K²/15 plus a divergence. By Cauchy–Schwarz, ∫K² strictly increases under any area-preserving perturbation away from the cone points that makes K non-constant. The cone terms do not change, so c₃ moves.
- **Suggested correction:** limit the claim to c₁ and c_j, j ≥ 3 (c₂ is topological), and replace the citation by this ∫K² argument or call Prop. 2.15(ii) its flat-background analogue.

## 2. Remark 2.6 (A count without the diameter): VERIFIED

The proof of Lemma 2.5 uses the counting function in only three places:
- **n_O(ℓ−) = 0.** This follows from the definition of the systole, not from Lemma 2.4.
- **One integration by parts.** Since φ is decreasing on the range, ∫_{[ℓ,∞)} φ dn_O = −∫ n_O·φ′.
- **The bound n_O(x) ≤ C·eˣ.** This turns the integral into C·(e^ℓ·φ(ℓ) + ∫ eˣφ), and it also makes the boundary term at infinity vanish.

With φ(x) = x·e^{−x/2 − x²/4t}, this is exactly the expression in the proof, with C = π·e^{3 diam}/Area. That C comes from the second inequality in Lemma 2.4. Nothing else in Lemma 2.5 uses the diameter.

The monotonicity of B in ℓ holds for any fixed C, because the log-derivative computation treats C as a constant. Prop. 4.2(a) also goes through with one common C_*(A, ε, M), taking ε as the smaller systole. So any such C, including the companion's C_*, can replace π·e^{3 diam}/Area.

**One implicit condition, which I cannot check without the companion:** its n_O must count the same objects as Lemma 2.4 — all hyperbolic conjugacy classes, primitive or not, with [γ] and [γ⁻¹] counted separately — for all x ≥ ℓ. The remark should say "the same counting function".

## 3. Lemma 3.14 (Configurations and pairs): VERIFIED

**(a)** The symmetry step in Theorem 3.7 uses only three facts: odd power sums vanish for j ≤ 2L − 3, Σz⁻¹ vanishes, and all entries are nonzero.
- **Short configurations are symmetric:** if |Z| ≤ 2L, Newton's identities make Q(z) = ∏(z − x) even, so Z = −Z with multiplicities.
- **Contradiction:** since Z is nonempty, Z = −Z means Z contains a pair {z, −z}, which a configuration excludes.
- **Conclusion:** |Z| ≥ 2L + 1, and since |Z| is even, |Z| ≥ 2L + 2.

**(b)**
- **Z is a configuration:** U* and V* are disjoint, so Z has no pair {z, −z}. Z is nonempty because the signatures differ. The power sums and Σz⁻¹ vanish by (14).
- **Imbalance:** ι = |U*| − |V*| = 2(g′ − g). This is correct, as the rendered page confirms.
- **Size bound:** |Z| ≤ 2·max(n + g − g′, n′ + g′ − g). Since g′ ≥ 0, n + g − g′ ≤ n + 4g, and n + 4g ≤ ⌊Area/π⌋ + 4. So |Z| ≤ 2⌊Area/π⌋ + 8.

**(c)**
- **Scaling:** harmless, because all conditions are homogeneous.
- **Disjointness:** U and V are disjoint because Z has no pair {z, −z}.
- **Equal area:** 2g + |U| = 2g′ + |V| is exactly g′ = g + ι/2. Entries 1 add nothing to the area, and R(U) = R(V) because Σz⁻¹ = 0.
- **Distinct signatures:** if U∖{1} = V∖{1}, disjointness forces both to be empty. Then U and V lie in {1} and one of them is empty, so Σz⁻¹ = ±|Z| ≠ 0, a contradiction.
- **Shared invariants:** U and V are paddings satisfying (14), so the converse in Lemma 3.6 gives equal c₁, …, c_L.
- **"Exactly L":** the difference of c_{L+1} equals a_{L−1,L}·Σz^{2L−1}, and a_{L−1,L} ≠ 0, so "exactly L" holds if and only if Σz^{2L−1} ≠ 0.
- **Area bounds:** if the smaller genus is 0, the area is 2π(|W| − 2 − R(W)) < 2π(|W| − 2). Otherwise the area at genus g₀ − 1 is ≤ 0, so the area at g₀ is ≤ 4π.

**Tests of (c).** All in exact rational arithmetic. I also recomputed c₁ through c₆ independently from the cone polynomials (5).

| Pair | ι | Σz^{2L−1} | Area | Shared invariants |
|---|---|---|---|---|
| (0;2,8,8) / (0;3,3,12), L = 2 | 0 | −750 | π/2 | exactly 2 (c₃ = −1601/480 vs −867/160; d₃ = 25/12) |
| (1;15) / (0;3,3,5,5), padding {15,1}, L = 2 | −2 | 3072 | 2π·14/15 | exactly 2 |
| (0;3,10,15,30) / (0;4,5,21,28), L = 3 | 0 | 3 861 000 | 2π·22/15 | exactly 3 |
| (1;15,15,15) / (0;3,3,5,7,7,21), L = 3 | −2 | −1 843 200 | 2π·14/5 | exactly 3 |
| (0;4,4,5,5,6,12,12) / (0;2,2,2,3,10,10,10,10), L = 3 | – | – | 2π·113/60 | exactly 3 |

All four areas are below 2π(|W| − 2), as part (c) claims.

## 4. Theorem 3.15 (Descartes bound): VERIFIED

I re-derived the proof:
- **Odd coefficients:** the odd-degree coefficients that vanish are those with k ≤ 2L − 3 and k = κ − 1, and these indices are distinct because κ ≥ 2L + 2. So at most κ/2 − L odd-degree coefficients are nonzero.
- **Sign changes:** V⁺ + V⁻ ≤ κ.
- **Odd gaps:** each gap between consecutive nonzero coefficients of different parity has exactly one odd-degree endpoint, so there are at most κ − 2L such gaps.
- **Descartes' rule:** all roots are real and nonzero, so the inequalities are equalities. Hence |ι| ≤ κ − 2L.

**Restated hypothesis.** Suppose |Z| = |U*| + |V*| = 2L + 2, with the padding entries 1 counted. Then:
- |ι| ≤ 2.
- ι = 2(g′ − g) is nonzero when g ≠ g′, so |ι| = 2 and |g − g′| = 1.
- The sizes are therefore {L, L + 2}.

Example 3.9 is consistent: U* = {15, 1} has size 2 = L and V* has size 4 = L + 2. The phrase "paddings by 1 included" is the right clarification.

## 5. Proposition 3.16 (Doubling): L ≥ 2 is needed and sufficient (VERIFIED)

**Needed.** For L = 1 the power-sum condition is vacuous, and the statement is false.
- **Counterexample:** X = {1}, Y = {2} gives U = {1, 4, 4}, i.e. (0;4,4). Its sum Σ(1 − 1/m) = 3/2 < 2, so it is not hyperbolic.
- **Second example:** X = {1}, Y = {3} gives (0;6,6), which is also not hyperbolic.
- **What still holds:** equal area and distinctness are fine for L = 1; only hyperbolicity fails.
- **Alternative fix:** assuming n ≥ 2 instead would also make the statement true.

**Sufficient.** With L ≥ 2, equal P₁ and X ≠ Y force n ≥ 2. The rest of the proof checks out:
- **n ≥ 3:** the 2n entries of 2X ⊎ 2X are all ≥ 2, so Σ(1 − 1/v) ≥ n > 2.
- **n = 2:** Y cannot be {1, 1}, so V has five entries ≥ 2. The same argument applies to U.
- **Power sums:** P_j(U) − P_j(V) = (1 − 2^{j+1})(P_j(X) − P_j(Y)) for every j, including j = −1.
- **Distinctness:** the multiplicity of 2x* in U minus V is −2ν(x*), which is nonzero.
- **Cone counts:** 3n − mult_X(1) and 3n − mult_Y(1).

## 6. Theorem 3.11 closed form: VERIFIED

**Closed form.**
- **Products:** ∏_{b≠a}(a − b) = (−1)^{M−a}(a − 1)!(M − a)! and ∏_{b≠a}(a + b) = (M + a)!/(2a·a!).
- **Weights:** a·w_a = (−1)^{M−a}·2a³/((M − a)!(M + a)!). I checked this exactly at every node for M = 2, …, 9.
- **Proportionality:** multiplying by (2M)! gives ν(a) ∝ (−1)^{M−a}·a³·C(2M, M − a); the ratio is constant for each M.
- **Existence of C:** Σw_a = 0 gives s = Σν(a) + C·w₁, so a suitable C exists.

**Worked examples.** I computed the least C directly.

| M | C | ν | s | Least-g pair | Area |
|---|---|---|---|---|---|
| 3 | 120 | (−16, 9) | −2 | (1; 3⁹) vs (0; 2¹⁶) | 12π |
| 4 | 2520 | (28, −27, 8) | 2 | (0; 2²⁸, 4⁸) vs (1; 3²⁷) | 36π |

- **Areas for M = 2, …, 9:** the least-g areas are 2π times 2, 6, 18, 190, 442, 3998, 8838, 77054. All match.
- **Part (iv), M = 2, X = 4:**
  - (w₁, w₂, w₄) = (1/45, −1/36, 1/180), C = 180, ν = (10, −4), s = 2.
  - The orbifolds (0; 2¹⁰) and (1; 4⁴) both have area 6π.

  All match.

## 7. Theorem 1.2(ii) / Proposition 3.19: VERIFIED

**If N(k) ≥ c·k^{1/α}, then f(A) = O(A^α).**
- **Attainment:** f(A) ≥ L + 1 holds exactly when A ≥ A_min(L), because the infimum is attained.
- **Bound on A_min:** combining T(L) ≤ 2A_min/π + 8 with T(L) ≥ N(2L − 2) ≥ c(2L − 2)^{1/α} gives L = O(A^α).

**If f(A) ≤ C·A^α, then N(k) ≥ c·k^{1/α}.**
- **A_min grows:** A_min(L) → ∞, so the bound on f applies for large L, and f(A_min(L)) ≥ L + 1.
- **Upper bound on A_min:** A_min(L) < 2πT(L) ≤ 8πN(2L − 3).
- **Odd k:** these give N(2L − 3) ≥ c′·L^{1/α}.
- **Even k:** N is nondecreasing, so N(2L − 2) ≥ N(2L − 3).
- **Small k:** finitely many are absorbed into c.

**The o(A) statement.** f(A) = o(A) if and only if N(k)/k → ∞ is also correct.

T ≤ 4N(2L − 3) is legitimate: Proposition A.2 needs equal power sums of every exponent up to 2L − 3, and a Prouhet–Tarry–Escott solution of that degree provides them.

## 8. Section 5 claims: VERIFIED

**The bounds.**
- **Floor:** the area of O(p,q,r) is 2π(1 − R) with 0 < R < 1, so ⌊Area/π⌋ = ⌊2(1 − R)⌋ ≤ 1. Corollary 3.8 then gives K_mult ≤ 5.
- **R > 1/2:** the floor is 0, so the bound is 4.

**The pair O(5,5,5) and (0;2,2,2,10).**
- **Area:** both are 2π·2/5.
- **c₂ input:** Σ(m − 1/m) = 72/5 on both sides.
- **Exact values:** c₁ = 1/5 and c₂ = 17/15 for both.
- **c₃ differs:** −107/75 vs −242/75, so they share exactly two invariants.
- **Consistency:** this agrees with the ≤ 4 bound, since R = 3/5 > 1/2.

## 9. Remark B.4: VERIFIED, with one minor ERROR in the η wording

The rendered page confirms the times are t₃, t₃/2, t₃/4.

- **D = 4.897.** The (2,8,8) triangle has sides 2.448452 (opposite the right angle) and 1.528571 (twice), so the longest side is arccosh(cot²(π/8)) = 2.448452. Twice that is 4.896905, which rounds up to 4.897; rounding up is the safe direction. The argument is correct:
  - A geodesic triangle is convex, so every point is within the longest side of each vertex.
  - The vertices lie in both copies of the double.
  - So d(x, y) ≤ d(x, v) + d(v, y) ≤ 4.897.
- **ℓ₀ = 2.2567.** My own enumeration gives systole 2.25677 for O(2,8,8): one closed geodesic, two orientations. So 2.2567 is a correct lower value, rounded down; it rests on floating point, as the remark says.
- **δ₁.**
  - **Inputs:** Q₃ = max(½|α₃|, 3|b₂(12)|) = 303.6267.
  - **Matrix norm:** for the nodes t₃/4, t₃/2, t₃, the matrix norm ‖V⁻¹‖_∞ is exactly 16/t₃².
  - **Result:** δ₁ = 16·Q₃·t₃ = **4858.0·t₃**, so "≈ 4.9×10³ t₃" is correct.
- **Threshold on t₃.** δ₁ ≤ 3.80×10⁻⁷ is equivalent to t₃ ≤ 7.822×10⁻¹¹, so "t₃ ≤ 7.8×10⁻¹¹" is correct and conservative.
- **Threshold on η (minor ERROR).** At t₃ = 10⁻¹¹ the condition is exactly η ≤ 2.071×10⁻¹⁹. The text says the bound "holds only if η ≤ 2×10⁻¹⁹", which is literally false for η between 2.00 and 2.07 ×10⁻¹⁹. **Correction:** "if and only if η ≤ 2.07×10⁻¹⁹", or replace "only if" by "if".
- **Same value for every ℓ₀ ≥ 0.01.** The range condition t_k ≤ ℓ₀²/(2(1 + ℓ₀)) = 4.95×10⁻⁵ holds. At t₃ = 7.8×10⁻¹¹ and ℓ₀ = 0.01, B₀ is about 10^{−139186}, and B₀ decreases as ℓ₀ grows. The claim is correct at these times.

## 10. Section 4: VERIFIED (diameter-free column not checkable); ERROR in the supplement

**The three factor ranges.** I built the family (0;3,3,3,3) exactly. In the Klein model the quadrilateral is the rectangle |x| ≤ tanh a, |y| ≤ tanh b, with sinh a·sinh b = 1/2. The systole 4b runs from 2.634 down to 0.694, matching Section S6.
- **Diameters:** the quadrilateral's diameter is its diagonal: 2.2924 at ϑ = 0, 2.3356 at ϑ = 0.4, 3.8849 at ϑ = 2.8. The diameter of the double, computed numerically, equals it.
- **Why the ratios can be checked:** for a fixed pair and time, the bound depends on the diameter only through e^{3 diam}. So the ratio of the proved-bound factor to the computed-diameter factor must be exp(3·(2·diamQ − diam_double)).

| Pair | Predicted ratio | Reported ratio |
|---|---|---|
| ϑ = 0 and 0.4 | 1.10×10³ | 4.4×10⁶ / 4.0×10³ = 1.10×10³ |
| pairs with ϑ = 2.8 | 1.15×10⁵ | 1.0×10¹⁰ / 8.8×10⁴ = 1.14×10⁵ |

So the first two columns are mutually consistent. This also confirms that "twice the diameter of the quadrilateral" is a valid diameter bound, by the same vertex argument as in item 9.

**The diameter-free column (4.1×10⁵ to 1.9×10⁶)** cannot be checked without the companion's C_*. If the extremal pairs are the same, it implies C_* ≈ 8.5×10⁴ at systole bound 2.20 and ≈ 1.9×10⁶ at 0.69. That is plausible but unconfirmed.

**The sign change of D.** I computed D(t) independently from the trace formula.
- **Elliptic part:** E₂ + 2E₈ − 2E₃ − E₁₂ from the integral in Theorem 2.3.
- **Hyperbolic part:** a complete weighted length spectrum up to length 6, which I enumerated in both triangle groups.
  - **Lengths:** they match the supplement — 2.2568, 2.8816, 3.0571 for (2,8,8) and 1.8626, 2.9807, 3.4027 for (3,3,12).
  - **Multiplicities:** each shortest geodesic has weight w/ℓ = 2, consistent with the supplement's fitted 1.997 and 1.9998.
  - **Truncation:** cutting the spectrum at 5.5 instead of 6 changes D(0.36) by only 10⁻¹⁰.

| t | D(t) |
|---|---|
| 0.341 | +3.28×10⁻³ |
| 0.350 | +1.61×10⁻³ |
| 0.360 | −1.39×10⁻⁴ |

- **The zero:** **t = 0.3592**, so the main text's "near t ≈ 0.36, between 0.341 and 0.360" is correct.
- **Elliptic part alone:** stays positive (about 0.044), so the reversal is caused by the geodesics, as stated.
- **Small-t check:** D(0.001) = 2.0124×10⁻³, against 2.0126×10⁻³ from the series.
- **Geodesic term of O(3,3,12):**
  - 2.64×10⁻¹⁵ at t = 0.025;
  - 3.96×10⁻¹³ at t = 0.0293;
  - 7.81×10⁻¹³ at t = 0.03.

  These match the stated values.
- **ERROR (supplement only):** Section S4 twice says D "changes sign near t = 0.34" (under "Prediction" and under "Closed geodesics"). **Correction:** "near t = 0.36 (between the sampled times 0.341 and 0.360)".

**Remark 4.3 (the wave trace).**
- **Kernel:** symmetrising the elliptic integrand and applying ∫e^{iru}·cosh(br)/cosh(πr) dr = 2cos(b/2)cosh(u/2)/(cos b + cosh u), with b = π − 2πj/m, gives exactly k_m(u) = (1/2m)·Σ cosh(u/2)/(cosh u − cos(2πj/m)).
- **Numerical check:** E_m(t) = ∫g_t·k_m holds to 20 digits for m = 2, 3, 8, 12 at t = 0.05 and 0.3.
- **Equivalent form:** the stated form with sinh²(u/2) + sin²(πj/m) is the same up to a constant.
- **Poles:** the nearest ones are simple, at ±2πi/m, including m = 2.
- **Growth:** the stated l!(m/π)^{2l} is consistent after the Gaussian moments.
- **Attribution:** I could not check that this form "is Garbin and Jorgenson's [37, Thm 2.5, Rem. 2.6]", because the source is not available to me.

## 11. Proposition 2.13 and the paragraph before it

**The outline is honestly labelled.**
- **The proof's heading:** it is marked as an outline.
- **The three steps not carried out:** the paragraph names all three — the reduction through (I − dΦ_p)⁻¹ = ½I + ½cot(ϑ/2)J (I checked this is the correct inverse for a rotation), the radial-jet identification, and uniformity in ϑ.
- **Use elsewhere:** the paragraph says no main result uses the proposition, and the Introduction ("proved in outline") is consistent with that.

**Minor points:**
- **"Confirmed by computation for l ≤ 3" is a little generous.**
  - **Remark 2.14(b):** its b₃ computation uses a radial curvature (K = k₀ + k₁r² + k₂r⁴, per Section S7(b)). It tests part (i) only for rotationally symmetric germs, not the radial-reduction step.
  - **Remark 2.14(c):** it tests non-radial jets only in the linear part.
  - **Suggested wording:** "confirmed for l ≤ 3 on rotationally symmetric germs, and in the linear part for l ≤ 7 on general germs".
- **Two overstatements elsewhere:**
  - The paragraph after Prop. 2.15 says Prop. 2.13 "show[s]" the one-new-power structure; "indicate" would be accurate for an outlined result.
  - Section 1.2 calls the top and linear coefficients "new" without saying the proof is outlined.

**Restated (ii) is well posed, with one wording fix.**
- **Why it is well posed:** for a fixed radial jet the β_{l,i} do not depend on m, and the identity holds for infinitely many integers m. So the m^{2l+1} coefficient is uniquely determined. It comes only from Π_{l+1}, whose top coefficient is |B_{2l+2}|/(2l + 2)!.
- **Wording fix:** b_l(p) is a Laurent polynomial in m (odd powers from m^{2l+1} down to m⁻¹), not a polynomial. Say "Laurent polynomial", or "read m·b_l(p) as a polynomial in m".
- **Rendered formulas:**
  - **Top coefficient:** β_{l,l+1} = 4^l·l!·[v^{2l}](f⁻¹)′ gives (2l)!/l!·K^l at constant curvature, so β₁,₂ = 2K, β₂,₃ = 12K² and β₃,₄ = 120K³. This agrees with Lemma 2.9.
  - **Linear part:** 2/(l − 1)!·(−Δ)^{l−1}K matches −2ΔK at l = 2 and Δ²K at l = 3.
  - **Supplement:** it gives the same formula, so all are consistent.

## Errors and corrections, collected

1. **Supplement, Section S4 (two places):** replace "near t = 0.34" by "near t = 0.36 (between the sampled times 0.341 and 0.360)". The computed zero is 0.3592.
2. **Remark B.4:** replace "holds only if η ≤ 2×10⁻¹⁹" by "if and only if η ≤ 2.07×10⁻¹⁹", or change "only if" to "if".
3. **Paragraph after Prop. 2.12 (GAP):** exclude c₂ from the instability claim, since it is topological. Replace the citation of the flat-background proof of Prop. 2.15(ii) by a curved-background argument, such as the ∫K² argument for Ω₁.
4. **Prop. 2.13(ii) (wording):** say "Laurent polynomial", or "read m·b_l(p) as a polynomial in m".
5. **Optional precision:**
   - **Remark 2.6:** state that the companion's count is of the same objects as Lemma 2.4.
   - **Paragraph before Prop. 2.13:** say the l ≤ 3 confirmation is for radial germs.
   - **"Show(s)" for Prop. 2.13:** change to "indicate(s)".
