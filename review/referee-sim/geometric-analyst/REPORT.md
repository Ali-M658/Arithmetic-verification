# Referee report (Geometric Analyst): "How much of a hyperbolic orbifold does heat hear?"

Submitted to *The Journal of Geometric Analysis*. Input: the 56-page manuscript PDF only. As instructed, the placeholders (author contributions, AI-use statement, Zenodo DOI) are not counted as defects.

My scratch scripts are coeffs.py, tf_check.py, stab.py, dup.py, dup2.py and misc.py. ms.txt is the extracted manuscript text and ds.pdf/ds.txt is the Dryden–Strohmaier paper. Network access from the sandbox was blocked. Only the Dryden–Strohmaier paper could be fetched, through WebFetch.

## 1. Summary

The paper studies the small-time heat-trace coefficients c_j(O) of a closed orientable hyperbolic 2-orbifold O of signature (g; m_1,…,m_n). Starting from the constant-curvature heat coefficients of Uçar's thesis [8] (Prop. 2.4), the authors observe the following:
- c_1 is the area.
- A cone point of order m contributes (−1)^l p_l(m)/m at order t^l, where p_l is an even polynomial of degree 2l+2 with p_l(1)=0 (Lemma 2.5).
- Hence the first k coefficients are a triangular affine image of (area, R, P_1, P_3, …, P_{2k−3}), with R = Σ 1/m_i and P_j = Σ m_i^j (Lemma 2.10).

Comparing two orbifolds therefore becomes a moment problem for a signed multiset. From this the paper derives:
- **Signature results (Section 3).** The first ⌊Area/π⌋+4 coefficients determine the signature within all of Sig (Cor. 3.7). No uniform number suffices (Thm 3.10, via Prouhet–Thue–Morse). For spheres with n cone points, n coefficients suffice (Thm A), with an explicit linear system and determinant (Thm B) and sharpness (Thm C).
- **Shape (Section 4).** Every c_j depends on the signature alone (Thm 4.1), so K_iso = ∞ off triangle orbifolds (Cor. 4.5). Through a heat-kernel version of the Selberg trace formula (Thm 4.6, Lemma 4.7), the difference of two heat traces within one signature is the difference of hyperbolic terms. It is bounded by C t^{-1/2} e^{-ℓ²/4t}, with ℓ the smaller systole (Thm 4.9), and the rate is attained when the length spectra first differ at ℓ (Thm 4.10, Cor. 4.11).
- **Triangle orbifolds (Section 5).** Two coefficients determine O(p,q,r) when p+q+r ≤ 17. The first failure is (2,8,8) versus (3,3,12) at sum 18, and that pair is isolated (rank-0 cubic, Thm 5.16).
- **Stability (Section 6).** Recovering the cone orders from perturbed coefficients is Lipschitz at simple orders and Hölder-1/k at k-fold orders. Explicit constants are given (Thms 6.4, 6.6), together with a closed-form exact-recovery threshold δ_thm (Thm 6.9) and a sharper rational-arithmetic certificate (Prop. 6.10, Table 2).
- **Numerics and arithmetic.** Section 7 compares the predictions with finite-element spectra. Section 8 studies two-coefficient collisions as rational points on the cubics of Bremner–Guy–Nowakowski.

## 2. Significance and novelty

**What is good.**
- The paper is carefully written and, in my area, I found no mathematical error.
- Every constant I recomputed matches (Section 3 of this report).
- Theorem B (the odd-power-sum Newton system with the closed-form determinant ς_n ∏(m_i+m_j)/∏m_i) and its Hurwitz factorisation (Lemma 6.3) are pleasant and correct.
- The stability analysis of Section 6 is unusually honest. Exponents are proved sharp, the closed-form and certified thresholds are separated, the certified thresholds are compared with constructed failures, and the paper says clearly that the error model is on heat invariants, not eigenvalues (Remark 6.1).
- The exact threshold 17 / minimal pair (2,8,8) ~ (3,3,12) answers a question raised in Dryden–Gordon–Greenwald–Webb [3, Rem. 5.16] (as quoted by the authors). It is a genuinely new, if modest, result.

**Comparison with the literature I could check.**
- **Dryden–Strohmaier [6]** (arXiv:math/0504571, which I read): Thm 1.1 says the Laplace spectrum of a compact orientable hyperbolic orbisurface determines the length spectrum and the number of cone points of each order, and conversely. Their eq. (1) is the Selberg trace formula with identity, hyperbolic and elliptic terms, for h even entire of uniform exponential type. The elliptic term is Σ_R (2m(R) sin θ(R))^{-1} ∫ e^{-2θr}(1+e^{-2πr})^{-1} h(r) dr. This is exactly what the manuscript uses in Thm 4.6, and the manuscript cites [6] correctly.
- **The heat function as a test function.** The heat function e^{-t(1/4+r²)} is not of exponential type, but it is admissible in the classical Selberg class (h even, holomorphic in |Im r| ≤ 1/2+ε, h(r) = O((1+|r|)^{-2-ε})). The classical treatments of cocompact Fuchsian groups with elliptic elements (Selberg 1956; Hejhal, LNM 548; Iwaniec's monograph) cover this class. Lemma 4.7 is therefore correct but unnecessary, and the sentence "for torsion-free groups the heat function is known to be admissible [29]; for orbifolds, Lemma 4.7 extends the formula" understates the literature.
- **Section 4 as a whole** consists of routine consequences of known formulas:
  - That the heat invariants of a constant-curvature orbisurface depend only on area and cone orders (Thm 4.1) follows immediately from DGGW [3] and is explicit in Uçar [8, Thm 4.20].
  - That moduli enter only through e^{-ℓ²/4t} terms and that the leading geodesic term governs the difference (Thms 4.9–4.10) is the standard heat-trace reading of the Selberg/Huber formula (McKean 1972 for surfaces).
  - The geometric-analysis content of the paper is thus the least novel part, and it should be presented as such.
- **Uçar [8].** I could not retrieve the thesis (arXiv:1711.03405) through the network available to me. However, I re-derived its formulas independently from the trace formula (see Section 3), so the numerical content of (4) is not in doubt for the orders I checked.

**Overall.** The paper is a solid, careful contribution, but much of it is either classical in substance (Section 4, the positive-real case of Thm A) or computational and arithmetic (Sections 5 and 8). For a JGA readership, the most interesting new mathematics is the quantitative counting (Cor. 3.7, Thm 3.10), Theorem B and the stability theory. The paper is long (56 pp.) for its weight, and its fit to JGA rather than a journal in spectral theory or experimental mathematics is debatable.

## 3. Correctness (my area in detail, the rest spot-checked)

Recomputations were done in my scratch folder with sympy/mpmath/numpy.

| Item | What I checked | Result |
|---|---|---|
| (4)–(5), (7) | Implemented (4) and (5) exactly. They reproduce p_0, p_1, p_2 of (7), and α_0…α_4 = 1, −1/3, 1/15, −4/315, 1/315. | Verified |
| Lemma 2.5 | For l ≤ 7: p_l even, degree 2l+2, p_l(1)=0, leading coefficient \|B_{2l+2}\|/(2(l+1)!(2l+1)). | Verified (finite range; all-l proof rests on (4); see M2) |
| Prop. 2.4 vs Thm 4.6 (independent check) | Expanded the identity and elliptic terms of the trace formula using ∫ r^{2b} e^{-ar}(1+e^{-2πr})^{-1} dr = ∂_a^{2b}[1/(2 sin(a/2))] and the moments of Remark 4.12, and compared with α_k (k ≤ 6) and b_l(m) (l ≤ 5, m ∈ {2,3,4,5,6,7,8,12,13}). | Agreement to 4×10^{-40}. Verified |
| Remark 4.12 moments | ∫_0^∞ r^{2k+1}/(e^{2πr}+1) dr = (1−2^{-2k-1})(−1)^k B_{2k+2}/(4(k+1)), checked by quadrature for k=0,1,2; ∫_R e^{-ar}/(1+e^{-2πr}) dr = 1/(2 sin(a/2)) checked analytically. | Verified |
| Cor. 2.9, (8)–(11), Remark 2.11(a,b) | Flat t^0 coefficients 0, 1/2, 2/3, 3/4, 5/6; (2,3,5) t^0 coefficient 271/360; χ(S²(2,2,n)) = χ(S²(2n,2n)) = 1/n. | Verified |
| Thm 4.6 | Normalisation g_t = (2π)^{-1}∫h_t e^{-iru}; identity, elliptic and hyperbolic terms against DS eq. (1); centraliser of a hyperbolic element in a Fuchsian group with torsion is cyclic, so the ℓ(γ_0) weight is right. | Verified |
| Lemma 4.7 | Paley–Wiener; dominated convergence on the hyperbolic side; ∫\|r\|\|f̂_ϱ\| ≤ ‖f_ϱ‖₁ + 2‖f_ϱ'''‖₁ (the paper's 2‖·‖+2‖·‖ is a valid upper bound); λ<1/4 terms; Σ min(1,\|r_j\|^{-3}) < ∞ from #{λ≤x} ≤ e·Z(1/x) = O(x). | Verified (but unnecessary; see M1) |
| Lemma 4.8 | Generic x_0, Dirichlet domain inside the ball of radius diam(O), representative axis meeting F, d(x_0,γx_0) ≤ ℓ+2δ, disjoint translates in B(x_0, x+3δ), 2π(cosh u−1) ≤ πe^u. | Verified |
| Thm 4.9(a) | I and E depend only on area and orders; Hyp ≥ 0. | Verified |
| Thm 4.9(b) | Redid each step: 2 sinh(x/2) ≥ e^{x/2}(1−e^{-ℓ_i}); φ_t decreasing for t ≤ ℓ_i²/2; Stieltjes integration by parts (the boundary term vanishes since n(ℓ_i^-)=0); completed square and erfc bound giving ∫_{ℓ}^∞ e^x φ_t = (2tℓ/(ℓ−t)) e^{ℓ/2−ℓ²/4t}/√(4πt) as an upper bound (I re-derived the exact identity ∫ x e^{-(x-t)²/4t} = 2t e^{…} + t√(πt) erfc(…)); monotonicity in ℓ_i ≥ ℓ for t ≤ ℓ²/(2(1+ℓ)). | Verified. The constant is explicit but depends on the diameter (M3) |
| Thm 4.9(c) | Ratio g_t/g_{t_1} and monotonicity in ℓ(γ) ≥ ℓ. | Verified |
| Thm 4.10, Cor. 4.11 | Grouping by length; the tail beyond L′ is O(e^{-(L′²−L*²)/4t}) relative to the leading term (the boundary term at L′ has a favourable sign); uniqueness of the Laplace transform; (iii) w_1(ℓ_1) > 0 = w_2(ℓ_1). | Verified |
| Prop. 4.2 | dim Teich = −3χ(X_O)+2k+l = 6g−6+2n (Thurston 13.3.7); zero exactly for (0;3) among hyperbolic signatures, otherwise ≥ 2 and even. | Verified |
| Prop. 4.3 | Uniqueness of the curvature −1 cone metric in a conformal class (Troyanov, χ(S,β) < 0 ⇔ Σ(1−1/m_i) > 2); uniqueness of the conformal structure of a 3-pointed sphere. | Verified (standard; m13) |
| Prop. 4.4, Cor. 4.5 | Invariance of domain argument plus countable length set. | Correct, but see m3 for a one-line proof |
| Cor. 3.7, Thm 3.6 | Parity argument; n+g−g′ ≤ n+4g ≤ Area/π+4. | Verified |
| Thm 3.10(a), Cor. 3.12 | Sizes 2^D+1, area bound s < 2^D−1 = 4^{L−1}−1, choice of L. | Verified |
| Prop. 6.2 | F^{-1} rows (−2), (2,12), (−18,−120,−360), (30,252,1260,2520), (−70/3,−240,−1680,−6720,−10080); amp = 2, 14, 498, 4062, 56230/3; diagonal magnitudes 2, 12, 360, 2520, 10080. | Verified |
| Thm B, Lemma 6.3 | det M = (−1)^{n(n+1)/2}∏(m_i+m_j)/∏m_i, the solution equals e, and det B = (−1)^{n(n−1)/2}∏(m_i+m_j), exact for six multisets with n = 3, 4, 5 (including a non-integer one). | Verified |
| t_k(n), ζ_n | t_1 = 1, t_3 = 1/3+(n+1)²; ζ_3 = 1, ζ_4 = 79/3, ζ_5 = 14048/15. | Verified |
| Thm 6.4(a),(b) | Hadamard step (every column of B̂ contains ê_0 or ê_1 ≥ 1); tanh/tan majorant argument; residual and δM bounds; ‖(M+δM)^{-1}‖ ≤ 2 cond. | Verified |
| Lemma 6.5, Thm 6.6, Thm 6.9 | Rouché bound with \|z\| ≤ 3/2; the constants 2^{1−k}3^n and 2^{2−k}3^n; the third term of δ_thm forces r_a ≤ 1/2; disjoint discs. | Verified |
| Table 2, δ_thm column | Recomputed all 11 values from the closed form. | All agree (my values: 3.803e-7, 1.189e-7, 4.021e-11, 3.147e-11, 4.492e-7, 9.354e-7, 9.973e-8, 1.487e-9, 4.744e-10, 2.031e-9, 2.730e-12; printed values are rounded down) |
| cond and Hadamard ranges (p. 37) | cond ∈ [1.000, 3.511]; Hadamard bound ∈ [11.9, 4425.1]. | Text says "between 1 and 3.5" and "12 to 4425" (m1) |
| Table 2, δ_up column | Own Nelder–Mead search over monic polynomials with a root or complex pair at a ± 1/2. | Reproduced 2.485e-3 (2,8,8), 4.588e-3 (3,3,12), 6.587e-3 (2,3,7), 5.036e-4 (4,4,4) |
| Table 2, δ_cert column | Not reproducible from the paper: Prop. 6.10 step 3 is not specified. Each printed δ_cert is below the δ_up I reproduced. | Could not check (M4) |
| Prop. 6.7 | δR = s²/(4(64−s²)), δP_3 = 48s²; limits of s/‖δc‖^{1/2}: 2.7385 (2,8,8), 4.4630 (3,3,12), 2.0446 (3,3,4,4). | Verified |
| Section 7 predictions | d_3 = 25/12, d_4 = −1775/24, d_5 = 153025/48; c_1 = 1/8 and c_2 = 67/48 for both; c_3 = −1601/480 and −867/160, consistent with Table 3. | Verified |
| Remark 6.8 | Inequality 3aΣd_i² + Σd_i³ ≥ 2aΣd_i² for \|d_i\| ≤ a. | Verified |

## 4. MAJOR issues

**M1. The geometric-analysis results of Section 4 are classical or immediate, and are presented as new.** (Thm 1.2, Thms 4.1, 4.6, Lemma 4.7, Thms 4.9–4.10; pp. 3, 19–26.)
- Thm 4.1 ("every heat invariant is a function of the signature alone") follows at once from the known constant-curvature formulas of DGGW [3] and Uçar [8, Thm 4.20]. The paper itself says "The formula is Proposition 2.4."
- The heat trace formula (Thm 4.6) holds directly in the classical Selberg admissible class (holomorphy in |Im r| ≤ 1/2+ε with polynomial decay), which contains e^{-t(1/4+r²)}. This is standard for cocompact Fuchsian groups with elliptic elements (Selberg; Hejhal LNM 548; Iwaniec), so Lemma 4.7 is not needed.
- Thms 4.9–4.10 are the standard reading of that formula: the leading hyperbolic term g_t(ℓ) ∝ t^{-1/2}e^{-ℓ²/4t}.
- *Resolution:* cite the classical admissible-class trace formula and drop or shorten Lemma 4.7 (or keep it as a remark). State explicitly that Thm 4.1 is a known corollary. Present 4.9–4.10 as an explicit, quantitative packaging of the standard argument, crediting McKean/Huber-type heat-trace analysis. Adjust the abstract and Theorem 1.2 accordingly.

**M2. The all-order structure that drives Section 3 rests on a formula quoted from an unpublished PhD thesis, and is checked only to finite order.** (Prop. 2.4, (4), Lemma 2.5, Lemma 2.10; pp. 7–10; Remark 4.12.)
- Every result of Section 3 (Thm A, Cor. 3.7, Thms 3.6 and 3.10) needs, for every l, that p_l is even of exact degree 2l+2 with p_l(1)=0. The proof of Lemma 2.5 is a manipulation of (4), taken from [8, (4.25)].
- Remark 4.12 cross-checks only through t^{14} (identity) and t^5 (elliptic, seven values of m), and calls itself "not an independent proof" because Lemma 4.7 uses the leading term of [3, Thm 4.8].
- The circularity is avoidable. The Weyl bound #{λ ≤ x} = O(x) needed in Lemma 4.7 follows independently (e.g. Dirichlet–Neumann bracketing, or the trace formula with a positive compactly supported test function). With it, the trace formula gives b_l(m) for all l in closed form: the coefficient of t^l in E_m is
  Σ_{j=1}^{m−1} (2m sin(πj/m))^{-1} Σ_{a+b=l} ((−1/4)^a/a!) ((−1)^b/b!) ∂_a^{2b}[1/(2 sin(a/2))] evaluated at a = 2πj/m.
  I implemented exactly this and it reproduces (4)–(7) to 40 digits for l ≤ 5 and nine values of m.
- *Resolution:* prove Prop. 2.4 at curvature −1 self-containedly via the trace formula, including the evenness, degree and p_l(1) = 0 statements of Lemma 2.5 for all l (for example via the generating function in a of the csc-derivative sums). Alternatively, give a complete verification of (4) within the paper rather than relying on a thesis.

**M3. The constant in Theorem 1.2(iii)/4.9(b) depends on the diameter, a dependence the introduction hides, and the sharpness statement needs qualification.** (Thm 1.2(iii) on p. 3: "C is explicit"; Thm 4.9(b) on p. 24; abstract: "this rate is attained".)
- The constant πe^{3δ}ℓe^{ℓ/2}/(A(1−e^{-ℓ})) contains e^{3δ}, with δ = max diameter. The diameter is neither a signature quantity nor a function of the systole. It blows up as the systole shrinks (δ ≳ log(1/ℓ)), so e^{3δ} behaves like a negative power of ℓ. The authors themselves find (b) "loose because of its factor e^{3δ}" (p. 44).
- Theorem 1.2(iii) should state the dependence C = C(A, ℓ, diam). Better, Lemma 4.8 should be replaced by a counting bound for closed geodesics whose constant depends only on area, systole and cone orders (for example via a thick–thin decomposition), so that C depends on (σ, ℓ) only. I have not checked whether such a bound with explicit constants appears in the orbifold literature; the authors should either prove it or keep the diameter and say so in Thm 1.2.
- "Attained" holds only when the first length at which w_1 ≠ w_2 equals ℓ (for example when ℓ_1 ≠ ℓ_2). When ℓ_1 = ℓ_2 with equal weights, the difference is O(t^{-1/2}e^{-L_*²/4t}) with L_* > ℓ, and the bound in terms of ℓ is not sharp. The abstract and Thm 1.2(iii) should say this.
- *Resolution:* state the dependencies in Thm 1.2(iii). Either improve the counting lemma or remove "explicit" from the introduction. Qualify "attained" in the abstract.

**M4. Proposition 6.10 is not specified completely enough to be checked, so the certified thresholds (Table 2, column δ_cert; Table 3, "certified") cannot be verified from the paper.** (pp. 40–42.)
- Step 3 ("bound the residual |r| … its part r_rem beyond first order, and |δM|") does not say how r_rem is bounded.
- Test (ii) uses D_I e = −M^{-1}J and p_c^{(l)}, but does not say how these enter the rational computation. The set of radii ϱ_0 is listed, but the per-order choice is not.
- The proof sketch for steps 1–5 is fine. My own δ_up searches reproduce the printed δ_up values, and every printed δ_cert lies below them, which is consistent. But the δ_cert numbers, and hence the claimed ratios of 1.03–6.72, rest on code. Similarly, Remark 2.12 ends "The proofs are in the repository." A journal paper cannot defer proofs to a repository.
- *Resolution:* give the explicit bounds of step 3 (formulas for |r|, r_rem and |δM| in terms of |δU| and the tangent majorant), or move Prop. 6.10 and Table 2's δ_cert column to an appendix with complete formulas. Either prove the claims of Remark 2.12 in the paper or delete them.

## 5. MINOR issues

- **m1 (p. 37).** "The exact cond is between 1 and 3.5 on every test multiset, against a Hadamard bound of 12 to 4425." I get cond = 3.511 for (2,2,2,2,3) and a Hadamard bound of 11.9 for (3,3,12). Change to "1 and 3.52" and "11.9 to 4426", or round outward.
- **m2 (Prop. 6.7(i), p. 38 vs its proof p. 39).** The statement gives δR = 2s²/(8(64−s²)) and the proof gives s²/(4(64−s²)). They are equal, but one form should be used throughout.
- **m3 (Prop. 4.4, p. 21).** The invariance-of-domain / Thurston-coordinates argument, including the special case (0;2,2,2,3), is correct but heavy. Isometry classes are the orbits of the countable (finitely generated) orbifold mapping class group on Teich(O) ≅ R^{6g−6+2n}, so there are uncountably many. Replace it with this one-line proof, or keep the current argument as a remark.
- **m4 (p. 25).** "Pairs with ℓ_1 ≠ ℓ_2 exist in every signature with moduli in which the systole varies on Teichmüller space." The systole always varies when dim Teich > 0: pinch a curve, or for the (0;2,2,2,3) case shrink the order-2 segment. Drop the qualifier and give the one-line argument.
- **m5 (Thm 4.6 proof, p. 23).** "The function h_t is not of exponential type. For torsion-free groups the heat function is known to be admissible [29]." This is misleading (see M1). DS [6] cite the classical sources; cite the admissible-class version.
- **m6 (Remark 4.12, p. 25).** "Expanding e^{-tr²} under the integrals" needs one line of justification. Split tanh(πr) = 1 − 2/(e^{2π|r|}+1); the remaining kernels decay exponentially, so the Taylor remainder (tr²)^N/N! is dominated.
- **m7 (Thm 4.9(b) proof, p. 24).** The monotonicity condition actually needed is x/2t ≥ 1/x + 1/2. Say that x/2t ≥ 1/ℓ+1 implies it.
- **m8 (Thm 1.4, Thms 6.6, 6.9).** The thresholds and constants are functions of the unknown true m (cond, r_n, Π̂_a). For actual recovery the logic must be a posteriori: recover a candidate, then certify at the candidate, as in Section 6.5. Say this in Theorem 1.4 and Section 6.4. Also call C_a "computable" rather than "explicit", since it contains cond = ‖M(Î)^{-1}‖_∞, or give the closed-form Hadamard version of 6.4(a) in Thm 1.4.
- **m9 (Abstract; Thm 1.4).** "Hölder of exponent 1/k at k-fold orders, and both rates are sharp." Sharpness at k ≥ 3 holds for arbitrary data vectors, not for data coming from real multisets (Remark 6.8 gives exponent 1/2 there). Qualify this in the abstract.
- **m10 (Section 6 scope).** The stability theory covers genus 0 with n known only. Cor. 3.7 (all of Sig) has no stability counterpart, and n is not determined by c_1. State this limitation in Section 1.
- **m11 (Table 3; Section 6.5).** "Certified" relies on eigenvalue error bars that are a-posteriori agreements, not enclosures (Remark 6.1, Section 7.1 Limitations). Put "conditional on the error bars" in the caption of Table 3.
- **m12 (Section 7.1, Limitations).** "A recomputation of all four spectra with the double-window solver … has not yet been run." Run it before resubmission, or explain why it is unnecessary.
- **m13 (Prop. 4.3).** State that the 3-pointed sphere has a unique conformal structure (so φ is conformal between the two orbifold conformal structures), and give the exact Troyanov statement (existence and uniqueness for χ(S,β) < 0 with K ≡ −1). Note also that the result follows from dim Teich = 0, which the paper mentions after the proof.
- **m14 (Lemma 4.8 / Thm 4.9).** Counting all hyperbolic classes rather than primitive ones is correct. Add a sentence noting that ℓ(γ_0) ≤ ℓ(γ) is where non-primitive classes are absorbed.
- **m15 (Cor. 4.11, last sentence).** The ε-statement is immediate from 4.9(b) and adds little. Consider removing it.

## 6. Presentation issues

- **p1.** The paper is long (56 pp.) and mixes four very different papers: heat invariants and moment problems, the trace formula, the arithmetic of the cubics C_Λ, and finite-element numerics. For JGA, consider moving Section 8 and most of Section 7 to a companion paper or a supplement, and shortening Section 4 (see M1).
- **p2.** Symbols are overloaded:
  - δ is both the diameter (Thms 4.8–4.9) and the data error (Section 6).
  - T is the tanh series, the Prouhet classes T_0/T_1, the torsion point T_2 and T_L in Problem 1.
  - ℓ is the systole and L the number of coefficients; ϱ is both the cutoff scale and the residual in Prop. 6.10.
  Rename (for example diam for diameter, Θ for the tanh series).
- **p3.** Lettered (A, B, C) and numbered theorems are interleaved, and Section 1.1 refers to "Theorem A" before it is defined. Use one scheme, or add a roadmap table.
- **p4 (Prop. 6.10 proof).** "M(Ĩ) = M(I+X)" should read M(Ĩ) = M(I)(I+X).
- **p5 (Thm 1.2(iii)).** List the quantities C depends on (see M3).
- **p6 (Fig. 1, p. 4).** Explain in one line why 4πt h_t(x,x) → m at a cone point of order m (the m elements of the isotropy group each contribute (4πt)^{-1}).
- **p7.** Several formulas in the PDF render poorly in text extraction (for example (4), the statement of Thm 6.4(a)). This is not an issue for the printed version, but check accessibility.
- **p8 (Section 1.1).** "To our knowledge this is the first explicit finite number of heat coefficients…" Soften this, given M1, and keep the priority claims to Cor. 3.7 and Theorem 1.3.

## 7. Recommendation

**Major revision. Confidence: medium.**

In my area I found no mathematical error. Every constant, identity, coefficient and threshold I recomputed is correct, including:
- the heat coefficients, re-derived independently from the trace formula;
- the determinant identities of Theorem B and Lemma 6.3;
- all eleven δ_thm values;
- the δ_up values I could construct;
- the sharpness ratios of Proposition 6.7.

The stability analysis is careful and honest.

Revision is still needed for four reasons:
- The geometric-analysis core (Section 4) is classical and should be presented as such (M1).
- The all-order structure behind Section 3 rests on a thesis formula that the trace formula could prove directly (M2).
- The "explicit" constant in the shape theorem hides a diameter dependence and the sharpness claim needs qualification (M3).
- The certified thresholds and Remark 2.12 depend on code and proofs not given in the paper (M4).

None of these is likely to be fatal, but together they materially change how the contribution should be presented, and its fit for JGA should be reconsidered after shortening.

*Note on the literature check:* network access from the sandbox was blocked. Through WebFetch I could confirm Dryden–Strohmaier's Thm 1.1 and eq. (1). I could not retrieve Uçar's thesis or DGGW, so the citations [3, Rem. 5.16; Thms 5.14–5.15] and [8, (4.25), Thm 4.20] were not checked against the sources. The content of (4) was instead verified independently.

---

*Saved by the coordinating session: this subagent could not write files, so the report came back as text and was saved verbatim. The coordinator removed only the hand-back note addressed to itself.*
