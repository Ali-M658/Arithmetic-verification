<!-- Round 8 B-c referee report: returned text saved verbatim; the reviewer could not write files -->

The tool refused to write `REPORT.md` (subagents may not write report files), so the full report is below for you to save. I recommend minor revision. I found no mathematical error in Sections 2, 5, 6 or Appendix A, and I reproduced every constant I tested. The two major issues are that the abstract's headline N values are uncertified, and that the paper overlaps heavily with the companion paper [31].

My scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/B-c-selberg-zeta-analyst/scratch/code/` (`consts.py`, `env.py`, `cor63f.py`, `exact.py`). One reproduction did not finish: I stopped the Corollary 6.3 check for A = 4π/3, M = 12 because it was too slow. That one value (N = 7415) is not independently checked; the other four Corollary 6.3 values are.

---

# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

**Journal:** Annals of Global Analysis and Geometry
**Referee B-c:** Selberg trace formula, heat-trace asymptotics with explicit constants
**Assigned part:** Section 2, Section 5, Section 6 (Lemma 6.1, Theorem 6.2, Corollary 6.3, Remarks 6.4–6.5) and Appendix A.
- I also checked the Section 3 results that Section 6 uses: Lemmas 3.1 and 3.3 and Theorem 3.2, all proved in A.3.
- I checked Lemma 4.5 in passing, because Theorem 6.2 depends on it.

Page numbers are those printed on the PDF. I read the rendered pages (110 and 200 dpi) before reporting any formula or typographical point.

## 1. Summary

The paper proves an effective inverse-spectral result. Take closed orientable hyperbolic 2-orbifolds with area ≤ A, systole ≥ ε and cone orders ≤ M. Then the first N eigenvalues, each known to within δ, determine the signature, and Theorem 6.2 gives N and δ explicitly. The decision rule picks the σ in Sig(A, M) that minimises |Σ_{j<N} e^{−λ̃_j t*} − G_σ(t*)|.

The proof in my part runs as follows:
- **Trace formula.** The heat trace splits as G_σ + Hyp (Theorem 2.1).
- **Expansion.** The small-t expansion of G_σ has enveloping (alternating) remainders with explicit bounds (Proposition 2.3).
- **First difference.** At the first heat invariant where two signatures differ, the difference has an explicit rational lower bound (Lemma 3.3), and that index is at most k* = min(⌊A/π⌋+4, M).
- **Gap.** Lemma 6.1 turns this into a gap Θ(t) between signature terms, valid for t ≤ t1.
- **Error terms.** Closed geodesics are controlled by Lemma 2.2(ii) together with the count C* of Lemma 4.5. The spectral tail is controlled by Proposition 5.2.
- **Corollary 6.3** replaces the heat-invariant gap by a gap computed at a moderate time.

## 2. Significance

**What is good:**
- The theorem is correct (see §3). It is a clean, honest effective version of a compactness argument, and it is well placed relative to Buser–Courtois, Dryden–Strohmaier, Doyle–Rossetti and Garbin–Jorgenson.
- The enveloping-remainder treatment of the cone and area terms (Proposition 2.3) is neat. It bounds the truncation error of the heat expansion with explicit constants and signs at every t > 0, not only as t ↓ 0. I consider it the most useful technical contribution of my part.
- Lemma 3.3 isolates the integrality behind the separation cleanly.
- The paper is unusually candid about what is proved and what is only computed.

**Weaknesses:**
- The a-priori constants are of no practical use. In Table 3, δ ranges from 10⁻⁹ to 10⁻²⁷⁸ and N reaches 4 × 10³⁰.
- The practically meaningful numbers (Corollary 6.3, and Section 7) rest on floating-point quadrature or on uncertified eigenvalue data.
- The ingredients are standard: the trace formula with elliptic terms, small-t asymptotics, packing, and counting from the heat trace. The new inputs (Lemma 4.5, Lemma 3.3, the explicit envelopes) are modest.
- Much of Sections 2–3 and all of Appendix A duplicate the simultaneously submitted companion paper [31] (see M2).

Overall: correct and careful, of moderate significance for AGAG.

## 3. Correctness and what I recomputed

I checked every proof in my part line by line and found no mathematical error.

### Checked by hand

- **Theorem 2.1.**
  - The normalisation of the identity, elliptic and hyperbolic terms matches Hejhal's.
  - I fetched Dryden–Strohmaier (arXiv:math/0504571v2). Their eq. (1) is stated for h entire of uniform exponential type (g in C_c^∞), with the elliptic sum over R_c^l, 1 ≤ l ≤ m−1, and θ = πl/m. The paper describes [1] accurately.
  - E_m(t) tends to Σ_j csc²(πj/m)/(4m) = (m²−1)/(12m), the known cone-point coefficient.
- **Lemma A.1.**
  - The eigenvalue count via η_T is correct.
  - For imaginary r_j = iy, η_T(r_j) = 2 Re ψ̂(iy−T)², which is real and bounded. So "contributes O(1)" is legitimate, but the paper does not say this.
  - The dominated-convergence steps are correct.
- **Lemma 2.2(i)** is correct: the Dirichlet domain lies in B̄(x̃0, diam).
- **Lemma 2.2(ii)** is correct.
  - φ is monotone on [ℓ, ∞).
  - The integration by parts against n_O works, and x/(x−t) ≤ ℓ/(ℓ−t) on that range.
  - The logarithmic derivative of B_C in ℓ is as stated; the bracket ℓ/2t − (1+ℓ)/ℓ is ≥ 0 exactly when t ≤ ℓ²/(2(1+ℓ)).
  - The all-t bound follows from the maxima 2√t e^{−1/2} and 9t/2 and from Σ e^{−2ℓ(γ)} ≤ 2Ce^{−ℓ}.
- **Proposition 2.3 (proof on p. 31)** is correct.
  - The beta-integral moments, g_k = (−1)^k (2k)!/(k! 4^k) φ_k, and b_l = Σ_{k≤l} g_k (−1/4)^{l−k}/(l−k)! all check.
  - All terms have sign (−1)^K, so the bound is exactly |b_K| t^K.
  - The closed form of μ_k checks; I re-derived it from (1−2^{1−s})Γ(s)ζ(s).
- **Lemmas A.2 and A.3** are correct: the cotangent identity, the leading coefficient a_l, and p_l(1) = 0.
- **Lemmas 3.1 and 3.3 and Theorem 3.2 (proved in A.3)** are correct.
  - Lemma 3.1: the padding and triangularity arguments check.
  - Theorem 3.2(i): the parity argument (Lemma A.4 plus e_{κ−1} = e_κ Σ 1/x) and |U|+|V| ≤ 2(⌊A/π⌋+4) check.
  - Theorem 3.2(ii): the Vandermonde reduction checks.
  - Lemma 3.3(ii): the formula for d_k checks.
- **Lemma 5.1 and Proposition 5.2** are correct, including Area ≥ π/21.
- **Lemma 6.1 and Theorem 6.2** are correct. Each step checks:
  - 1 + 2t/(ε−t) ≤ 3 on (0, t2];
  - B* is increasing on (0, t2], since t2 < ε²/2;
  - B* ≤ Θ/8 reduces to y ≥ y0 via e^{−y/2} y^p ≤ (2p/e)^p;
  - Θ* ≤ 1/24, so Λt* ≥ 2 log 64;
  - N > e·Z_O(1/Λ);
  - the tail is exactly Θ*/8;
  - the total error Θ*/8 + Θ*/8 + Θ*/(8e) is less than 3Θ*/8, against a gap of more than 5Θ*/8.
- **Corollary 6.3** is a valid abstraction of that proof.
- **Lemma 4.5** (used as an input): I found no problem.

### Recomputed (mpmath at 30–60 digits)

1. The closed form for φ_k(m) agrees with direct Taylor coefficients of Φ_m for m = 2, 3, 7, 12 and k ≤ 3, to within 10⁻⁵⁸.
2. For l ≤ 4, p_l is even, of degree 2l+2, with p_l(1) = 0 and leading coefficient a_l. The values are a_0..a_3 = 1/12, 1/360, 1/2520, 1/10080.
3. The two formulas for α_k (Bernoulli-polynomial and moment) agree for k < 20. The values are α_0..α_4 = 1, −1/3, 1/15, −4/315, 1/315.
4. The enveloping property of Proposition 2.3 holds in all 210 test cases against direct quadrature of E_m and of (4π/Area)·I:
   - m in {2, 3, 5, 8, 12};
   - t in {10⁻³, 10⁻², 0.1, 0.5, 2};
   - K ≤ 6.

   |b_K(m)| is strictly increasing in m for K < 8 and m < 40.
5. Examples: d_2((0;4,4,4), (0;3,4,6)) = −1/12. For O(2,8,8) against O(3,3,12), c_2 agrees and d_3 = 25/12.
6. Table 3 (p. 15): all eight rows reproduce to the printed precision (k*, C*, t1, t3, Θ*, Λ, N, δ and the binding constraint). The minimum defining t1 is attained at k = k* in every row.
7. Other claims reproduced:
   - C* lies in [4×10⁵, 7×10¹⁰] (p. 12).
   - log₁₀(πe^{3D}/A) lies in [196.5, 29325.4] (p. 12), and Table 2 matches.
   - At A = 10π, M = 3, using k* = n* would give N = 4.19 × 10¹⁸ (p. 15).
   - For A = 4π/3, M = 3, N grows by a factor 5.24, 5.13, …, 4.62 per halving of ε below 0.42, and C* scales like ε⁻⁴ (p. 15).
8. Corollary 6.3 (p. 14), recomputed by double-precision quadrature over Sig(A, M) on a 121-point time grid. This is uncertified, like the paper's own computation, and agrees up to grid resolution.

   | Class | Signatures in Sig(A, M) | N (mine) | N (paper) |
   |---|---|---|---|
   | A = π/2, M = 8 | 27 | 245 | 244 |
   | A = π/2, M = 12 | 48 | 286 | 283 |
   | A = 4π/3, M = 3, ε = 2.6339 | 8 | 141 | 139 |
   | A = 4π/3, M = 3, ε = 0.6940 | 8 | 2627 | 2605 |

9. **A rigorous class-specific variant.** In Lemma 6.1, replace δ_k by the exact least first difference over the pairs in the finite set Sig(A, M). These differences are rational. Take Θ(t) = ½ min_k δ_k t^{k−2} and keep the rest of Corollary 6.3. No quadrature is needed.

   | Class | Least first differences | N (rigorous variant) | N (Theorem 6.2) | N (Corollary 6.3, uncertified) |
   |---|---|---|---|---|
   | A = π/2, M = 12 | d_1 ≥ 3.8×10⁻⁴, d_2 ≥ 1/12, d_3 ≥ 25/12 | 6.3×10⁵ | 6.8×10⁹ | 283 |
   | A = 4π/3, M = 3, ε = 0.694 | — | 2887 | 4.3×10⁴ | 2605 |
   | A = 4π/3, M = 12, ε = 0.694 (281 signatures) | — | 5.4×10⁶ | 7.4×10¹² | 7415 (not reproduced) |

## 4. FATAL issues

None.

## 5. MAJOR issues

**M1 (abstract pp. 1–2, p. 3, Corollary 6.3 on p. 14, p. 22).**
- **Problem.** The abstract says "the same theorem gives N of order 10² to 10⁴". That rests on Corollary 6.3, whose gap hypothesis is checked only by floating-point Gauss–Legendre quadrature.
- **Why it matters.** A headline number in a pure-mathematics abstract should not rest on an uncertified computation, especially when certification is cheap:
  - only a few dozen smooth, exponentially decaying one-dimensional integrals are needed, at a single t;
  - the gaps are about 10⁻³ to 10⁻¹, so little precision is required;
  - the other hypotheses are closed-form.
- **Resolution, either of:**
  - certify the gaps by interval quadrature (Arb's `acb_calc_integrate`, or mpmath.iv with tail bounds);
  - use the exact-rational route of §3 item 9, which is rigorous with no quadrature and gives 2887 against the uncertified 2605 for the M = 3 class.

  Otherwise the abstract should mark these figures as numerical.

**M2 (Table 1 on pp. 5–6; Sections 2–3; Appendix A on pp. 30–32).**
- **Problem.** About six pages of statements and proofs are reproduced from the simultaneously submitted companion [31]. The paper declares the overlap openly, but [31] has only a placeholder identifier, so I could not compare the two.
- **Resolution.** Provide [31] to the editor and referees, and state which version of the proofs is authoritative. Then either keep the appendix with an explicit statement of the overlap, or trim it to the parts that genuinely differ.

## 6. MINOR issues

- **m1 (p. 13, definition of Θ).** Θ(t) = ½γ* t^{k*−2} uses γ* = min_k δ_k, which includes δ_1 = 1/(2L_M). But the proof of Lemma 6.1 gives ½δ_k t^{k−2} at the actual first-difference index.
  - For M = 12, δ_1 = 1/55440 is binding.
  - Using Θ(t) = ½ min_k δ_k t^{k−2} improves Θ* and δ in Table 3 by factors of 22 (A = π/2) and 5.5 (A = 4π/3); N barely changes.
  - Remark 6.4(a) alludes to this; adopt it or say why not.
- **m2 (p. 7).** "On this range B_C decreases with ℓ" is ambiguous, because the range depends on ℓ. State it for fixed t, on the set of ℓ with t ≤ ℓ²/(2(1+ℓ)).
- **m3 (p. 30, Lemma A.1).** The proof is too compressed. Please add:
  - for imaginary r_j, η_T(r_j) is real and bounded;
  - the count #{λ_j ≤ x} = O(x) implies Σ_j min(1, |r_j|⁻³) < ∞;
  - Lemma 2.2(i) gives summability on the hyperbolic side.

  Alternatively, cite a version of the trace formula for the standard admissible class with elliptic elements (for instance Hejhal [34]). That class contains the heat function directly, which makes Lemma A.1 unnecessary.
- **m4 (p. 7).** "Hyperbolic conjugacy classes, so oriented" is inaccurate when Γ has order-2 elements. A rotation by π about a point on the axis gives [γ] = [γ⁻¹]. The formula and the counts are unaffected, since the centraliser is still ⟨γ_0⟩; adjust the wording.
- **m5 (p. 8).** For t > 0 the remainders never vanish, so "or vanishes" can be dropped. Also state that φ_k is extended to real m > 1 by the closed form of Lemma A.2; this is where "increasing in m" makes sense.
- **m6 (p. 14).** Corollary 6.3 uses B*, which is defined only inside the proof of Theorem 6.2. Define B* in a statement. Also spell out that Θ must bound every pairwise gap at the single time t, and that Θ ≤ 8 is used only to get Hyp ≤ 1 inside Z♯.
- **m7 (p. 14).** The example "an over-estimate of λ_j by up to δe^{λ_j t*}" is valid only termwise. Reword it as "if every term satisfies …".
- **m8 (p. 15).** "|b_K(M)| grows roughly like K!(M/π)^{2K}": the ratio |b_K(M)|/(K!(M/π)^{2K}) decays polynomially in K (from 0.99 to 0.11 over K = 0 to 10 at M = 12). Add "up to a factor polynomial in K".
- **m9 (p. 13).** n ≤ n* is crude: genus g contributes n ≤ ⌊A/π⌋ + 4 − 4g. An optional remark would make clear that Q is a worst case.

## 7. Presentation

- **P1. Symbol overloading.** Please disambiguate:
  - ε (systole), ϵ (Lemma A.1) and ϵ_j (eigenvalue errors);
  - δ and δ_k;
  - p (the polynomials p_l, the exponent k* − 3/2, the points p̃);
  - N (eigenvalue count, and the number of variables in Lemma A.4);
  - L (number of heat invariants, L_M, L_σσ′, and a length);
  - ℓ (systole bound, and an interval length in Proposition 8.3);
  - φ (the function in the proof of Lemma 2.2, and the coefficients φ_k).
- **P2.** The Table 1 caption is inconsistent about where Lemma 2.2 is proved.
- **P3 (p. 31).** Display the identity (4π/Area)·I(t) = e^{−t/4}(1/t − J(t)); it is the crux of (b).
- **P4 (p. 14).** Split the proof of Theorem 6.2 into three displayed estimates, so the 3Θ*/8 budget is visible.
- **P5.** The decision rule needs G_σ to accuracy about Θ* (10⁻¹⁸ to 10⁻²⁷²). The discussion on p. 15 should become a remark placed right after Theorem 6.2.

## 8. Recommendation

**Minor revision**, provided the editor is satisfied on M2.
- **Confidence in correctness: high.** I checked every proof and reproduced Table 3, the envelopes and four of the five Corollary 6.3 values.
- **Confidence in significance: moderate.** If M1 is resolved with certified class-level N values, I would support acceptance.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Certify the Corollary 6.3 gaps by interval quadrature, or use the exact-rational first differences (rigorous, e.g. N = 2887 for A = 4π/3, M = 3, ε = 0.694). Otherwise label the abstract's figures as numerical. |
| M2 | Provide [31]; state the overlap and the authoritative version; trim the appendix or keep it with that declaration. |
| m1 | Use Θ(t) = ½ min_k δ_k t^{k−2}, or justify the cruder form. |
| m2 | State the monotonicity of B_C for fixed t, with the ℓ-dependent range explicit. |
| m3 | Add the three justifications, or cite a version of the trace formula covering the heat function. |
| m4 | Fix "oriented" for classes with [γ] = [γ⁻¹]. |
| m5 | Drop "or vanishes"; say how φ_k is extended to real m. |
| m6 | Define B* in a statement; spell out the hypotheses of Corollary 6.3. |
| m7 | Reword the over-estimate example. |
| m8 | Qualify the growth statement for \|b_K(M)\|. |
| m9 | Optional remark on the crude bound n ≤ n*. |
| P1–P5 | Notation and layout changes as listed. |
