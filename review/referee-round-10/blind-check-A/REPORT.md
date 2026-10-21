<!-- Round 10 blind check of the Paper A changes: returned text saved verbatim; the reviewer could not write files -->

I checked all six items against the PDF only (pdftotext plus rendered pages). I found no errors and no substantive gaps. A few wording slips remain, listed below. The scripts are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/main/scratch/blind-A/ (omega.py, gap.py, b6.py, scan.py, c5.py, c5cert.py, thm.py).

**1. Lemma E.2 and its uses in Prop 2.14, Prop 2.17(ii) and Remark 2.15: CORRECT.**
- **Step 1.** Self-adjointness of Δ_ε = e^{-2εψ}Δ_0 on L²(dA_ε) holds. The kernel with respect to dx is k^ε = h^ε e^{2εψ(y)}, and T = ∫χ k^ε(x,Rx) dx follows because ψ∘R = ψ.
- **Step 2.** The contour Γ is fine and so is the bound ‖Δ_0R_z‖ ≤ c_Γ. The condition c_Γ(e^{2ε_0‖ψ‖∞} − 1) ≤ 1/2 does give absolute convergence of the series expanded in ε. C_1 and C_2 are correct.
- **Step 3.** The divided differences and the Hermite–Genocchi formula are correct: the simplex has area 1/2 and [a,b,c] has the factor t². γ̂_1 and γ̂_2 are correct with f̂ = ∫e^{-ix·ξ}f, and the kernel normalisation (2π)^{-2} is right.
- **Step 5.** [a,b] = −∫e^{-(t−r)a}e^{-rb} dr is correct, and so is the substitution r = t(1−s_0), q = ts_2. The localised Dyson kernels and their signs are correct. The O(t^∞) bound off a δ-neighbourhood of S is valid.
- **Step 6.** x·ξ − Rx·η = x·(ξ − R^Tη) holds and the Gaussian approximate identity works. I re-derived three identities:
  - [a,a] = −te^{-ta}.
  - ∫γ_1 = −t∫w_1 q_t(x,Rx) = 2t∫ψ q_t(x,Rx).
  - [a,b,a] = t²∫(1−s)e^{…}; after symmetrisation the weight becomes 1/2, so 2∫γ_2 = D_2(t), using ŵ_2(0) = 2∫ψ², |ŵ_1|² = 4|ψ̂|² and ζ → ξ−ζ.
- **The factor 2t** is right.
- **Prop 2.14.** I recomputed ∫|x|^{2l} q_t(x,Rx) dx = −l·l!·4^l t^{l−1} C^{−2l−2}. The linear part of (−Δ)^{l−1}K(0) is −4^l(l!)²ε, so λ_l(ϑ) = 2C^{−2l−2}/(l−1)!. Averaging with C = 2 sin(πj/m) gives (2/(l−1)!)Π_{l+1}(m). Cross-checks:
  - At K = −1, b_1(m) from (5) equals −2Π_2(m), for example −4/27 at m = 3.
  - The leading m⁵ coefficient for l = 2 is 1/15120, which matches Schueth.
- **Prop 2.17(ii).**
  - The first variation (2πt)^{-1}∫ψ is correct.
  - The θ²/2·D_2 bookkeeping with w_1 = −2θψ, w_2 = 2θ²ψ² is correct.
  - The Gaussian identity π/t(2/t² + (2s−1)²|ζ|²/t + s²(1−s)²|ζ|⁴) is exact (checked symbolically in sympy).
  - The three-term formula for ω_{l+1} and the Parseval step are correct.
  - The −t·tr(w_2…) term is O(t^{-1}).

**2. Lemma E.1 as used: CORRECT.**
- The uniform Levi parametrix bounds (E1)–(E3) hold, including the Volterra bound (2m)^i C^m V^{m−1} t^{mN−1}/(m−1)!.
- The identification H = h^ε via Duhamel is correct.
- The rotation-case Laplace expansion holds: Ψ_ε ≥ c|z|², the derivative bound (1+|z|)^{3n+2i}e^{−c|z|²} is right, and odd orders vanish because F_j(ε,−s,z) = F_j(ε,s,−z).
- The identification with Donnelly's B_k via a rotation-invariant cap is fine at referee level.
- The hypotheses match both uses: g_ε flat outside supp ψ, and χ = 1 near supp ψ (or near supp ζ_0).

**3. Remark 2.18 and the closed form ω_n = (−1)^n n(n−1) n!/(2n+1)!: CORRECT.**
- **Against the proof's sum.** In exact arithmetic, the three-term sum in the proof of 2.17(ii) equals the closed form for l = 1..11.
- **Against the Branson–Gilkey–Ørsted route.** The route in the remark reproduces the closed form exactly when the linear part of u_k is k·k!/(2k+1)!·(−Δ)^{k−1}scal. That coefficient matches Gilkey: 1/6 for k = 1, 12/360 = 1/30 for k = 2, 18/7! = 1/280 for k = 3.
- **Independent check, n = 2.** From a_4 = (1/360)(5R² − 2|Ric|² + 2|Rm|²), the surface value is u_2 = K²/15. This gives ω_2 = 1/30, which matches.
- **Independent check, n = 3.** I integrated the quadratic derivative terms of Gilkey's a_6 in dimension 2 and got ∫u_3 = −(72/7!)∫|∇K|² + cubic terms. This gives ω_3 = −1/140, which matches the closed form −36/5040. The a_6 coefficients came from memory, not a source in hand; an exact match is still strong confirmation.

**4. Lemma 5.5 and its use in Lemma 5.6 and Theorem 5.7: CORRECT.**
- The factorisation of φ_p − τ_p is exact (sympy). The odd-parity excess 4/((S−p)((S−p)²−1)) > 0, and x*(2) = 18.
- Lemma 5.6:
  - gap_2(9) = gap_2(10) = 1/12.
  - R⁻_{18,3} = 101/168, attained at (3,7,8).
  - R⁻_{19,3} = 7/12 < 101/168 < 7/10.
- Theorem 5.7:
  - φ_p′ = −(S−3p−4)(3S−5p−4)/((S−p)²(S−2p−2)²) is correct.
  - gap_p(3p+7) is correct for p = 2..14.
  - The odd-parity values 1/840, 1/2310, 1/10296 are correct.
  - The values at S*+1 (−7/936, …, −17/4680) are correct.
- I also brute-forced the strata overlaps directly for p = 2..29. The first overlap is S*(p) as stated, and overlaps persist after it.

**5. Proposition C.5: CORRECT.**
- **Proof steps.**
  - The bound on the tanh perturbation through tan coefficients is valid because U ≥ 0 coefficientwise.
  - The residual satisfies r_j = Σ(T̃−T)_{2i+1}e_{2j−2i}, r_{n−1} = (R̃−R)e_n, and |M̃−M| ≤ Δ_M.
  - The J entries s_{2i+2−2k}/(2k−1) and J_{n−1,0} = −e_n are correct.
  - The decomposition ẽ − e = G(c̃−c) + ξ′ with |ξ′| ≤ |M⁻¹|ρ^rem + AE is correct.
  - The Rouché tests (i) and (ii) are sound.
- **Front end.** amp = 2, 14, 498, 4062, 56230/3 is correct, and so is P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3. The diagonal entries of F match. F·I + h_0 reproduces c(2,8,8) exactly. sech²U for (2,2,2,2,3) is 1 − 121z² + 9328z⁴ − 601472z⁶, as printed.
- **Thresholds, recomputed in exact rational arithmetic.**
  - Implementing C.5 for (2,8,8) with uniform δ gives δ_cert = 2.34171e−3, and the printed 2.341e−3 is correctly rounded down.
  - Theorem C.4 gives δ_thm(2,8,8) = 3.8028e−7, matching the printed 3.80e−7, with exact cond = 1 and ζ_3 = 1. ζ_4 = 79/3 and ζ_5 = 14048/15 also check.

**6. Remark B.6 with ℓ_0 = 1.8626, D = 4.897: CORRECT.** All printed numbers reproduce.

| Quantity | Recomputed | Printed |
|---|---|---|
| D = 2·arccosh(cot²(π/8)) | 4.89690 | 4.897 |
| Longest side of the (3,3,12) triangle | 2.1582 | 2.158 |
| Area of both orbifolds | π/2 | π/2 |
| Q_3 (from |α_3| = 0.012698, b_2(12) = 101.209) | 303.63 | n/a |
| Q_8 (from b_7(12) ≈ −9.16e10) | 2.75e11 | n/a |
| N = 3, uniform bound | 4858τ | ≈ 4.9e3 τ |
| N = 3, τ threshold (uniform) | 7.822e−11 | about 7.8e−11 |
| N = 3, η threshold at τ = 1e−11 (uniform) | 2.071e−19 | 2.07e−19 |
| N = 3, row bounds | 1138.6τ | ≈ 1.14e3 τ |
| N = 3, τ threshold (row bounds) | 3.34e−10 | about 3.3e−10 |
| N = 3, η threshold (row bounds) | 4.61e−19 | 4.6e−19 |
| N = 8, τ threshold for δ_thm | 3.597e−3 | about 3.6e−3 |
| N = 8, η threshold for δ_thm at τ/2 | 5.004e−13 | about 5.0e−13 |
| N = 8, τ threshold for δ_cert | 1.540e−2 | about 1.5e−2 |
| N = 8, η threshold for δ_cert at τ/2 | 1.320e−8 | about 1.3e−8 |
| Smallest time | 6.0e−5 | below 1e−4 |

- The values for three times are the same for ℓ_0 = 0.01 and 2.2567.
- My scan of geometric and Chebyshev grids with N ≤ 16 agrees with "none meets δ_cert for a ≥ 1e−3" (best δ is about 1.31) and "none meets δ_thm for a ≥ 3e−4" (best about 2.96e−6). This is a plausibility check only, because the paper does not specify T or the scan design.

**Wording errors and small gaps (none affects a result).**
1. **Remark B.6, diameter.** "A point of the double is within that distance of a vertex" only gives diam ≤ 3L. The 2L bound needs "within that distance of every vertex (or of a fixed vertex)". That is true, since distance from a vertex is convex on the triangle and so at most the longest side.
2. **Remark B.6, systole.** "The term B_0 is negligible for every ℓ_0 ≥ 1.1" is overstated. At ℓ_0 = 1.1 the δ_cert thresholds move from 1.540e−2 to 1.462e−2 and from 1.320e−8 to 1.258e−8. They still round to the printed 1.5e−2 and 1.3e−8, but only just; at ℓ_0 = 1.0 the τ threshold is 1.26e−2. Say "unchanged at the printed precision" or raise 1.1 to about 1.5.
3. **Lemma E.2, Step 5.** "The integrands are bounded uniformly in q, r" is false for the factor p_{r−q}(z,z′) as q → r. It becomes true after integrating z′ (∫p = 1), which is how the estimate is actually used.
4. **Lemma E.2, Step 3.** The second bound, 4t|ŵ_1||ξ−η|², is integrable only on the region |η| < 2|ξ−η|. Say so.
5. **Lemma E.2, Step 6.** For R = Rot_ϑ, the dominating function G_i comes from |(R^T−I)η| = C|η| and the Schwartz decay of ŵ, not literally from "the bounds of Step 3".
6. **Prop 2.14.** C is used without being defined there; add C = 2 sin(ϑ/2). The normalisation b_l(p) = (1/m)Σ_j B_l(γ^j) behind "averaging" should be stated.
7. **Remark 2.15.** "Likewise for the heat trace without the rotation": that expansion starts at t^{-1} (d = 1 in Lemma E.1).
8. **Prop 2.17(ii).** "Expanding the exponential" gives an asymptotic expansion, not a convergent one. The Taylor remainder plus the Schwartz decay of ŵ_1 justifies it; one clause would suffice.
9. **Prop C.5, proof.**
   - |ẽ−e| ≤ E uses (I−A)^{-1} = ΣA^k ≥ 0.
   - Invertibility uses ρ(X) ≤ ρ(|X|) ≤ ρ(A).
   - The Rouché lower bound in (i) needs r_0 < |a−b|, which holds automatically since r_0 ≤ 1/2 and distinct integer orders differ by at least 1.
10. **Remark 2.18.** ∂_θZ(t) = 2t·tr(ψΔ_θe^{−tΔ_θ}) is formal on ℝ², because the trace is not trace class there. Read it on a closed surface or in localised form; as a remark this is acceptable.

**Overall verdict.** All six items are correct. Every printed constant I recomputed matches: ω_n, λ_l, the Section 5 gaps and S*(p), amp, ζ_n, δ_thm(2,8,8) = 3.80e−7, δ_cert(2,8,8) = 2.341e−3, and all Remark B.6 numbers. Only the minor wording fixes above are needed, with (1) and (2) the most worth correcting.
