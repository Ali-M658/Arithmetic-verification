<!-- Saved verbatim by the main session from the reviewer's returned text: the harness refused the reviewer's own write. Scripts listed at the end are in its git-ignored scratch/. -->

# Referee report

**Manuscript:** "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (23 pp.)
**Journal:** Annals of Global Analysis and Geometry
**Referee focus (as assigned):** the constants of the main finitely-many-eigenvalues theorem, and every remainder bound it rests on: the heat-trace tail beyond the N-th eigenvalue, the eigenvalue-counting bound, the bound on the geodesic term, the truncation of the small-time expansion, and how N and the tolerance δ are derived from them. My brief calls this theorem "Theorem E". In the manuscript it is Theorem 1.1 (p. 2), stated with full constants as Theorem 6.2 (pp. 12–13). I use the manuscript's numbering throughout.

The marked placeholders (author contributions, AI-use statement, Zenodo DOI; pp. 20–21) are treated as known and are not counted against the paper.

---

## Summary

Take a closed orientable hyperbolic 2-orbifold with cone points only, area at most A, systole at least ε and cone orders at most M. The paper shows that the first N eigenvalues, each known to within δ, determine its signature, where N and δ are given by closed formulas (Theorem 6.2).

The mechanism is as follows.
- **Trace formula.** The Selberg trace formula for the heat function (Theorem 2.1, with Appendix A) splits Z_O(t) into a part G_σ(t) that depends only on the signature, plus a positive geodesic term Hyp(t).
- **Enveloping expansions.** Both the area integral and the cone integrals have enveloping small-t expansions with explicit remainders (Propositions 2.6, 2.7, inequality (4)).
- **Integrality.** The first heat invariant at which two signatures differ is an integer multiple of an explicit rational (Lemma 3.5), and it occurs at index at most min(⌊A/π⌋+4, M) (Theorems 3.3, 3.4).
- **Gap.** These give a lower bound Γ(t) for |G_σ − G_σ'| at small t (Lemma 6.1).
- **Error terms.** At one time t*, the geodesic term is controlled through a diameter bound (Theorem 4.4, Lemma 2.3), the eigenvalues beyond the N-th through a counting/tail bound (Proposition 5.2), and the data errors through a Lipschitz bound.

The paper adds two further results:
- an a-posteriori certificate (Theorem 7.1), applied to computed spectra (Table 3);
- a proof that the order bound M cannot be dropped: the orbifolds O(2,3,m) have arbitrarily many eigenvalues near 1/4 (Propositions 8.2, 8.3, Remark 8.4).

**My bottom line on the assigned charge:** I re-derived every remainder bound in the chain leading to Theorem 6.2 and found no mathematical error. I independently re-implemented all the formulas of Sections 2–6 at 50 digits, and I reproduce every entry of Tables 1 and 2 and the comparisons in the text. The main remaining weaknesses are elsewhere:
- **Section 7 (certificate).** The rigour of the certificate's numerical inputs is not documented.
- **Decision rule.** The paper does not say how the rule of Theorems 1.1/6.2 is actually evaluated.
- **Efficiency.** Several avoidable losses make the a-priori constants astronomically large.

## Significance

**What is good.**
- The question, an effective form of Dryden–Strohmaier's theorem that the spectrum determines the signature, is natural and fits AGAG.
- The analytic part is clean and self-contained. Exact enveloping (sign-alternating) remainders for both the area integral and the cone integrals are a nice, correct and reusable device (Props. 2.6, 2.7). They are more than one usually sees in heat-invariant papers, where remainders are typically only O(t^K).
- Lemma 3.5 (the first difference is an integer multiple of a_{k−2}, or of 1/(2·lcm)) is the right arithmetic input.
- The O(2,3,m) family (Section 8.1) is a convincing demonstration that the order bound is needed for the statement itself, not just for the method.
- The paper is unusually honest about the size of its constants.

**What limits significance.**
- The a-priori constants are of purely theoretical value: N up to 3.8×10^30 and δ down to 8.7×10^−278 (Table 2, last row). This comes largely from choices made in the method rather than from the problem itself (see m11, m12 below).
- The effective statement is essentially a careful bookkeeping of standard ingredients (trace formula, packing bound for the diameter, Chebyshev-type counting). Its novelty lies in the arithmetic of Section 3 and in the explicit envelopes.
- No lower bound for the minimal admissible N is offered; the authors acknowledge this on p. 14.
- The certificate (Section 7) is the part with practical value, but it is also the part whose numerical claims cannot be checked from the manuscript (M1).

Overall the significance is moderate and adequate for the journal, provided the claims about certification are made verifiable.

## Correctness and what was recomputed

All computations were done in my own scripts in `scratch/` (mpmath 1.3, 50 digits unless noted), written from the formulas in the manuscript only. I did not look at the authors' repository.

### 1. Trace formula (Thm 2.1, p. 4; App. A, p. 21)

I fetched Dryden–Strohmaier, arXiv math/0504571v2 (saved as `scratch/ds.pdf`) and compared its eq. (1) term by term with Theorem 2.1:
- identity term Area/(4π)∫ r tanh(πr) h;
- hyperbolic weight ℓ(γ0)/(2 sinh(ℓ(γ)/2));
- elliptic weight 1/(2m sin θ) ∫ e^{−2θr}/(1+e^{−2πr}) h, with θ = πj/m.

The normalisations agree. As a cross-check, the cone constant term E_m(0+) = b_0(m) = (m²−1)/(12m) agrees with the known orbifold heat invariant. The area coefficients α_0..α_3 = 1, −1/3, 1/15, −4/315 reproduce, and μ_0 = 1/12.

Appendix A: I checked the approximation argument line by line. This covers the O(T+1) local count from a test function with Fourier support in [−2ϵ,2ϵ], the bound #{λ_j ≤ x} = O(x), the summability Σ min(1,|r_j|^{−3}) < ∞, and the treatment of imaginary r_j. It is correct.

### 2. Geodesic count and geodesic term (Lemma 2.2, Lemma 2.3, pp. 4–5)

- **Lemma 2.2.** I re-derived the Dirichlet-domain packing bound n_O(x) ≤ 2π(cosh(x+3 diam)−1)/Area. It is correct.
- **Lemma 2.3, first bound.** I re-derived it by Stieltjes integration by parts twice: the boundary term φ(X)n(X) → 0, −φ′ ≥ 0 on [ℓ,∞) on the stated range, and the bound ∫_ℓ^∞ x e^{x/2−x²/4t} dx ≤ (2tℓ/(ℓ−t)) e^{ℓ/2−ℓ²/4t} via x/(x−t) ≤ ℓ/(ℓ−t). I obtain exactly B(ℓ,diam,t).
- **Monotonicity of B.** I re-derived the logarithmic derivative in ℓ: 1/ℓ + 1/2 − ℓ/(2t) − e^{−ℓ}/(1−e^{−ℓ}) − 2t/(ℓ²−t²). This matches the paper, and it is negative on t ≤ ℓ²/(2(1+ℓ)).
- **Second (all-t) bound.** The maxima at x = 2√t and x = 6t are correct, and so is the constant 2√π e^{3diam} e^{17t/4−1/2−ℓ}/(Area(1−e^{−ℓ})).

### 3. Small-time expansion and its truncation (Lemmas 2.4, 2.5, Props. 2.6, 2.7, eq. (4), Lemma 2.8, pp. 5–7)

**Analytic checks.**
- The closed form of Φ_m: at m = 7, u = 0.1, the definition, the closed form and the 30-term series (2) agree to 48 digits.
- The bound ϕ_k(m) ≤ (m/4)(2m/π)^{2k} holds for k < 15 and 2 ≤ m < 20.
- I re-derived the moment identity via Euler's beta integral and the identification Σ_j m_{2k}(2θ_j)/(2m sin θ_j) = (2k)!4^{−k}ϕ_k(m).
- I re-derived both envelope proofs, including the sign bookkeeping of the cross terms, and the leading coefficient a_l = |B_{2l+2}|/(2(l+1)!(2l+1)).

**Numerical check of the envelopes.** I computed E_5(t) and (4π/Area)I(t) by quadrature for t = 0.05 and t = 0.3 and K = 0..4. In every case the remainder has the claimed sign (−1)^K (cone) or (−1)^{K+1} (area), and modulus below |b_K(5)|t^K and |α_{K+1}|t^K respectively. Example: E_5(0.05), K = 3: remainder −7.71×10^−4, bound 1.08×10^−3.

### 4. Heat invariants of a signature (Section 3)

- **Lemma 3.1.** I checked the triangular change of basis p_l(x)/x = Σ a_{l,k} ψ_k(x).
- **Theorem 3.3.** I checked the evenness argument, including that κ is even: |U|−|V| = 2(g′−g).
- **Theorem 3.4.** I checked the Vandermonde reduction.
- **Lemma 3.5.** I checked the sign (−1)^k = (−1)^l and the claim |d_1| ≥ 1/(2L).
- **Examples.**
  - (0;4,4,4) vs (0;3,4,6): d_2 = −1/12.
  - (0;2,8,8) vs (0;3,3,12) (p. 14): equal R = 3/4 and P_1 = 18, and d_3 = a_1(1782−1032) = 750/360 = 25/12. Confirmed.
- **Enumerations.** I enumerated the signatures of area π/2 with orders ≤ 12 and get exactly six: (2,6,12), (2,8,8), (3,3,12), (3,4,6), (4,4,4), (0;2,2,2,4); (2,5,20) is excluded. For area 4π/3 with orders ≤ 3 I get three: (0;3,3,3,3), (0;2,2,2,2,3), (1;3). These match |S| in Table 3.

### 5. Diameter (Lemmas 4.1–4.3, Thm 4.4, pp. 9–11)

I checked (H1)–(H3), the defect estimate in Lemma 4.2 (cosh d − 1 ≥ 2/(π²cM)), the two cases of Lemma 4.3, and the packing argument and closed form of Theorem 4.4 (arccosh(1+x) ≥ √(2x/(1+x)) gives d_0 ≥ min(ε/2, 0.6/M)).

**Table 1** is reproduced to all printed digits by the exact formula 4r_0A/v_0:

| (A, ε) | M = 3 | M = 12 | M = 100 |
|---|---|---|---|
| (π/2, 1) | 56.6 | 1125 | 6.37×10^5 |
| (4π/3, 1) | 150.9 | 3001 | 1.70×10^6 |
| (4π/3, 0.1) | 640 | 3184 | 1.70×10^6 |
| (10π, 1) | 1132 | 2.25×10^4 | 1.27×10^7 |

For comparison, the closed form gives 60, 2880, 1.67×10^6, etc., so it is never below the exact formula.

The diameter claims in the Table 1 caption also check out. "Twice the longest side" gives 2·arccosh(cot²(π/8)) = 4.894 < 4.9 for O(2,8,8) and 2·2.1608 = 4.32 < 4.4 for O(3,3,12).

### 6. Counting and tail (Lemma 5.1, Prop. 5.2, pp. 11–12)

- The case analysis Area ≥ π/21 and n + 4g ≤ Area/π + 4 is correct.
- E_m ≤ b_0(m) and I(t) ≤ e^{−t/4}Area/(4πt) are correct.
- The Chebyshev-type count #{λ_j ≤ x} ≤ e Z(1/x) and the tail bound e^{−Λ(t−s)}Z(s) are correct, including the index convention "N ≥ eZ(1/Λ) ⇒ λ_j > Λ for j ≥ N" with λ_0 = 0.

### 7. The gap and Theorem 6.2 (pp. 12–13)

**Lemma 6.1.** Re-derived; correct, including the case k = 1 (different areas).

**Theorem 6.2.** I re-derived:
- ϖ, using π/Area ≤ 21 and 1 + 2t/(ε−t) ≤ 3 for t ≤ t_2 ≤ ε/2;
- that B_* is increasing on (0, t_2] (t_2 < ε²/2);
- the equivalence B_* ≤ Γ/8 ⇔ e^{−y}y^p ≤ γ_*(ε²/4)^p/(16ϖe^{3D}), and the sufficiency of y ≥ y_0 through e^{−y/2}y^p ≤ (2p/e)^p;
- Λt_* = 2 log(8Z♯/Γ_*) ≥ 1, so that 1/Λ ≤ t_* and Z_O(1/Λ) ≤ Z♯(1/Λ);
- the tail term e^{−Λt_*/2}Z♯(t_*/2) = Γ_*/8 exactly;
- the perturbation term ≤ Γ_*/(8e);
- the final margin 3Γ_*/8 < 5Γ_*/8.

The proof is correct as written, under its hypothesis λ̃_j ≥ 0.

**Table 2** is reproduced to every printed digit, including the "binds" column. My values (t_2 is not printed in the paper, but I computed it and it never binds):

| A | ε | M | k_* | D | t_1 | t_2 | t_3 | N | δ | binds |
|---|---|---|---|---|---|---|---|---|---|---|
| π/2 | 1.8626 | 8 | 4 | 402.2 | 1.14e−7 | 0.606 | 3.54e−4 | 3.40e8 | 3.07e−21 | t_1 |
| π/2 | 1.8626 | 12 | 4 | 1125 | 6.85e−9 | 0.606 | 1.28e−4 | 6.82e9 | 4.17e−25 | t_1 |
| 4π/3 | 2.634 | 3 | 3 | 150.9 | 9.32e−4 | 0.955 | 1.86e−3 | 4.32e4 | 1.48e−9 | t_1 |
| 4π/3 | 0.694 | 3 | 3 | 150.9 | 9.32e−4 | 0.142 | 1.29e−4 | 3.69e5 | 1.73e−10 | t_3 |
| 4π/3 | 0.694 | 12 | 5 | 3001 | 2.70e−11 | 0.142 | 6.67e−6 | 7.44e12 | 4.06e−41 | t_1 |
| 2π | 0.1 | 3 | 3 | 960 | 7.76e−4 | 4.55e−3 | 4.31e−7 | 2.40e8 | 2.67e−13 | t_3 |
| 10π | 1 | 3 | 3 | 1132 | 3.30e−4 | 0.25 | 3.66e−5 | 1.14e7 | 5.61e−12 | t_3 |
| 10π | 1 | 12 | 12 | 2.251e4 | 2.50e−27 | 0.25 | 1.85e−6 | 3.75e30 | 8.65e−278 | t_1 |

**Claims in the text of p. 13.**
- "At A = 10π [without Theorem 3.4] N ≈ 4×10^18." Confirmed: k_* = 14 gives N = 4.19×10^18.
- t_3 ≈ ε²/(24D) and N ≈ eA/(2πt_*)·log(8Z♯/Γ_*). Consistent with the formulas.

**ε-scaling (pp. 14, 20).** At A = 4π/3, M = 3, I get N = 1.03×10^8, 9.17×10^8, 8.05×10^9 and 7.03×10^10 for ε = 0.1, 0.05, 0.025, 0.0125. The ratios are 8.86, 8.79 and 8.73 (see m7).

### 8. Systoles used as ε

Enumerating words of length ≤ 10 in the triangle groups (`scratch/systole.py`) gives the following shortest closed geodesics (upper bounds on the systole):

| Orbifold | Shortest closed geodesic found |
|---|---|
| O(3,3,12) | 1.862604 |
| O(2,8,8) | 2.256768 |
| O(2,3,7) | 0.98399 |

So the value ε = 1.8626 in Table 2 is the systole of O(3,3,12), the smaller of the two triangle orbifolds. Since t_1 binds in those rows, the a-priori N is the same at either systole, which is consistent with Table 3 and Figure 2.

### 9. Figure 1 (p. 14)

I recomputed |G_{(2,8,8)} − G_σ| by quadrature for the five competitors:
- t = 0.001: 0.164, 0.00201, 0.415, 0.498, 0.747;
- t = 1: the (3,3,12) curve (0.0294) and the (2,6,12) curve (0.0252) nearly meet, as plotted.

The dashed curve is reproduced by Lemma 2.3 with ℓ = 2.2568 and Δ = 4.9: B = 8.3×10^−7, 4.3×10^−4 and 2.8×10^−2 at t = 0.04, 0.05 and 0.06, matching the plot. I cannot check the dotted (tail) curves or Table 3 without the eigenvalue data.

### 10. Section 8 (outside my charge, spot checks only)

- σ_* = 2 arsinh((2√(37/12))^{−1}) = 0.56206.
- h_m ≥ log(m/2π).
- Identity (5) and the two values of q.
- The Rayleigh-quotient bounds of Props. 8.3 and 8.5.
- For m = 4096, h_m = 7.173: the bound is 1.017 > λ_1 = 0.473, and h_m²(λ_1−1/4)/π² = 1.16, matching Fig. 3(b).
- For m = 7: bound 133 > 44.89, rescaled value 1.35.

### Overall verdict on correctness within my charge

I found no error in any remainder bound, nor in the derivation of t_1, t_2, t_3, t_*, Γ_*, Λ, N or δ, and the printed constants are reproduced exactly.

---

## MAJOR issues

**M1. The a-posteriori numerics are presented as certified, but the paper does not document or justify the inputs that Theorem 7.1 requires (Section 7, pp. 14–16; Table 3; Fig. 2; Abstract p. 1; p. 3).**

Theorem 7.1 is a correct theorem (I re-derived it). But its conclusion "σ(O) = σ" holds only if all of the following are rigorous:
- (a) **Error bounds.** |λ̃_j − λ_j(O)| ≤ ϵ_j for each j ≤ N, index by index and with multiplicity.
- (b) **Completeness.** The lower bound λ_N ≥ λ̃_N − ϵ_N, which drives the tail term. A conforming Rayleigh–Ritz/FEM computation gives upper bounds λ_j ≤ λ_j^h index-wise. It does not give lower bounds, so "completeness" is exactly what it cannot deliver without an extra argument (e.g. Lehmann–Goerisch, Kato–Temple with a separation estimate, Liu–Oishi or Carstensen–Gedicke guaranteed lower bounds). For the doubled triangle and quadrilateral orbifolds one must also merge the Dirichlet and Neumann lists of the polygon without losing an eigenvalue.
- (c) **A lower bound ℓ for the systole.** Word enumeration, as one would naturally do and as I did, gives an upper bound on the systole, not a lower one. A lower bound needs a finite-enumeration argument with a proven cut-off, e.g. via Lemma 2.2: every class with ℓ(γ) ≤ L has a representative with d(x_0,γx_0) ≤ L + 2Δ. The systoles quoted for O_ϑ (2.634 down to 0.694) come without any such argument.
- (d) **An upper bound Δ for the diameter.** For O_ϑ the value "at most 7.8" (Table 1 caption) has no argument.
- (e) **Geometry and rounding.** Geometry errors (the sides are hyperbolic geodesics, i.e. circular arcs in the disc or half-plane model, so curved elements or exact mappings are needed) and floating-point error must be included in ϵ_j.

The manuscript says only that the spectra were "computed with high-order finite elements and error estimates" (p. 15). For Fig. 3 it says the "two mesh levels … agree to 2.3×10^−10", which is an agreement check, not an enclosure. Unless (a)–(e) hold, the abstract's "certifies the signature of a computed spectrum from 21 to 750 eigenvalues" and the N_apr column of Table 3 are not certified results. Moreover, no number in Table 3 can be checked from the manuscript.

**M2. The decision rule of Theorems 1.1/6.2 is said to be computable and checkable (p. 2), but how to evaluate G_σ(t_*) to the required accuracy is never addressed (Theorem 1.1, p. 2; Theorem 6.2, p. 13).**

The rule compares Σ_{j<N} e^{−λ̃_j t_*} with G_σ(t_*), where G_σ is defined by oscillatory/improper integrals (Theorem 2.1). The margins in the proof are 3Γ_*/8 against 5Γ_*/8. So G_σ(t_*) must be evaluated with absolute error below Γ_*/8, for instance:
- Table 2 row 1: Γ_* = 2.6×10^−18 while G_σ(t_*) ≈ A/(4πt_*) ≈ 1.1×10^6, i.e. about 25 significant digits;
- last row: Γ_* = 1.8×10^−272 while G_σ(t_*) ≈ 3×10^27, i.e. about 300 significant digits.

The paper's own envelopes solve this, but the paper does not say so. By (4), choosing K with t_*^K(A|α_{K+1}|/4π + n_*|b_K(M)|) ≤ Γ_*/16 makes the truncated series a rigorous evaluation. Without this sentence the "explicit function G_σ" is explicit but not evaluable with error control.

In addition:
- Theorem 1.1 omits the hypothesis λ̃_j ≥ 0 that Theorem 6.2 uses for |e^{−at} − e^{−bt}| ≤ t|a−b|. With λ̃_j ≥ −δ the bound acquires a factor e^{δt_*}, harmless here, but the two statements must agree.
- Theorem 1.2 (p. 3) likewise omits the nonnegativity assumed in Theorem 7.1.

---

## MINOR issues

**m1.** Theorem 6.2, p. 13: in δ = min{1/t_*, Γ_*/(8eNt_*)} the first entry is never active, since Γ_* ≤ 1 < 8eN. It plays no role in the proof. Remove it or say why it is there.

**m2.** Lemma 2.3, p. 5, says "Let ℓ be the systole", but the lemma is applied with ℓ a lower bound (proof of Thm 6.2, p. 13; Thm 7.1, p. 14). The proof works verbatim for any 0 < ℓ ≤ ℓ(O): n_O vanishes below ℓ, and 2 sinh(x/2) ≥ e^{x/2}(1−e^{−ℓ}) for x ≥ ℓ. With that restatement the monotonicity-in-ℓ claim is not needed for Theorem 6.2.

**m3.** Eq. (4), p. 7:
- The bound follows from the triangle inequality, so "since all b_K(m_i) have the sign (−1)^K" is unnecessary.
- Conversely, the area remainder has sign (−1)^{K+1} and the cone remainders sign (−1)^K (Props. 2.6, 2.7). The bound could therefore be max(A|α_{K+1}|/4π, Σ|b_K(m_i)|) instead of the sum.
- Similarly, in Theorems 6.2 and 7.1, Hyp > 0 and −Σ_{j≥N} e^{−λ_j t} < 0 have opposite signs, so the max of those two error terms suffices rather than their sum.

These are small gains, but free.

**m4.** Lemma 3.5 proof, p. 9: the notation "C_l = Σ b_l" is undefined. Write "Σ_i b_l(m_i)".

**m5.** P. 11, after Table 1: "in no row of Table 2 is [the diameter] the binding constraint through t_1" is meaningless, since t_1 does not depend on D. Rephrase, e.g. "D enters t_* only through t_3, which binds only for M = 3 in Table 2".

**m6.** P. 13: "Two constraints compete for t_*" — and t_2 never binds in Table 2 (my values 0.142 to 0.955 and 4.55×10^−3 against t_* ≤ 9.3×10^−4). Say so explicitly. Also add a t_2 or t_* column, or at least Γ_* and Λ, so that N and δ can be checked from the table. My values: Γ_* = 2.6e−18, 4.2e−22, 1.3e−6, 1.8e−7, 1.8e−37, 6.0e−10, 5.1e−8, 1.8e−272.

**m7.** P. 14: "N grows by a factor near 8 per halving of ε". My recomputation at A = 4π/3, M = 3 gives ratios 8.86, 8.79 and 8.73 for ε from 0.1 down to 0.0125. Say "about 9, tending slowly to 8".

**m8.** P. 20 asserts "The N of Theorem 6.2 grows like ε^{−3} log(1/ε) as ε → 0 once t_3 binds", while p. 14 says these are "observations on the formulas, not proved asymptotics". Either prove it or hedge consistently. The upper bound is immediate from the formulas: D ≍ A·max(4M,M²)/(πε), y_0 ≍ 6D, t_3 ≍ ε³, and log(8Z♯/Γ_*) ≍ (k_*−2) log(1/ε).

**m9.** Section 7, p. 15: the definition of N_obs is unclear. At which t is "the data lie within half the nearest gap" judged, and against which quantity? State it as a formula.

**m10.** Theorem 7.1 (p. 14) assumes the area A known exactly and takes S to be signatures of area A. In Table 3, S is "all signatures of the same area with orders at most M", which presupposes knowing both A and M.
- Say how A is determined from finitely many approximate eigenvalues, or that it is assumed.
- Note that Theorem 6.2 needs neither assumption.

**m11.** Proposition 5.2 and the perturbation step of Theorem 6.2: the bound |e^{−at} − e^{−bt}| ≤ t|a−b| ignores the decay of e^{−λ_j t_*}. Using |e^{−at} − e^{−bt}| ≤ t|a−b|e^{−min(a,b)t}, the perturbation is at most t_*δe^{δt_*}Z_O(t_*) ≤ t_*δe^{δt_*}Z♯(t_*). This allows δ of order Γ_*/(8e t_* Z♯(t_*)), a gain of a factor ≈ N/Z♯(t_*) ≈ 2e log(8Z♯/Γ_*). That is about 10^2 to 10^4 across Table 2. Alternatively, it allows a relative tolerance. Optional, but it cheaply improves the most unrealistic constant.

**m12.** Lemma 6.1, Section 6: k_* and γ_* are worst-case values over all pairs. Since Sig(A,M) is a finite, explicit set, the true first-difference index and the minimal |d_k| can be computed exactly. Example, A = 4π/3, M = 3:
- every same-area pair already differs at k = 2, with |G_σ − G_σ'| ≈ 0.166 at t_1;
- different areas give |d_1| ≥ 1/12;
- so k_* = 2 and γ_* = 1/12 instead of 3 and 1/360.

My recomputation with these values gives t_1 = 0.017 and N = 1.08×10^4, against 4.32×10^4 in Table 2. In the numerical test, the actual gaps at t_1 exceed Γ(t_1) by a factor 1.3×10^5 to 5.1×10^5. At least remark on this. More substantially, for fixed (A,M) the whole of Lemma 6.1 can be replaced by a verified finite computation of min_{σ≠σ'}|G_σ(t) − G_σ'(t)| at a moderate t. Figure 1 shows gaps around 10^−2 at t = 0.05, versus Γ ≈ 10^−18 at t_* in Table 2. That is the real reason the a-priori N is so large.

**m13.** Table 2, p. 13: the choice ε = 1.8626 for A = π/2, M = 8 is unexplained. It is the systole of O(3,3,12), which has order 12 > 8. Likewise, 2.634 and 0.694 are the extreme systoles of O_ϑ. Say this in the caption. Also state that the D column is the exact 4r_0A/v_0, not the closed form of Theorem 4.4.

**m14.** P. 12, Proposition 5.2: the factor e in #{λ_j ≤ x} ≤ eZ(1/x) comes from evaluating at time 1/x. Optimising over the time, #{λ_j ≤ x} ≤ inf_s e^{sx}Z(s), gives a smaller constant. With Z ≈ A/(4πs) the gain is only the factor e itself, so this is minor and optional.

**m15.** Section 1, p. 2 (compactness paragraph): the second compactness step ("then a δ > 0 by compactness again") deserves one more clause. δ = ½·min over the compact product of max_{j<N}|λ_j − λ'_j|, which is positive by continuity.

**m16.** Abstract and p. 3: "from 21 to 750 eigenvalues" and "4×10^4 to 7×10^12" mix two classes (M = 3 and M = 12) and two families. A one-line clarification would help.

---

## Presentation (figures and captions included)

I viewed rendered pages 2–17, 19 and 20 at 110 dpi. I found no sign error or typographical error in any displayed formula that I checked against my derivations.

**Figure 1 (p. 14).**
- No legend. Only the darkest grey curve is identified in the text. The two dotted curves (N = 21 and N = 100) are not distinguished, and neither are the other four competitors.
- The caption says the signature is decided where half the nearest gap "exceeds both errors"; the text says "exceeds the sum of both errors". Theorem 7.1 requires the sum, so fix the caption.
- State the diameter bound used for the dashed curve. Δ = 4.9 reproduces it.

**Figure 2 (p. 16).**
- The open diamonds (N_apr, M = 3) appear to be hidden beneath the filled ones; only one diamond series is visible. Offset or use different markers.
- The two coloured triangle-orbifold markers (orange near systole 1.86, teal near 2.26) are not keyed in the caption. Say which is O(3,3,12) and which is O(2,8,8).
- State that the squares for M = 12 are constant because t_1 binds.

**Figure 3 (p. 19).**
- In panel (b) the dotted horizontal lines are at j² = 1, 4, …, 36, i.e. the conjectured limits. The proven bounds of Prop. 8.3 are (j+1)² in this scaling. The caption should say this.
- In panel (a) the text calls the bounds "thin dashed", but they render as dotted.

**Fonts.** Text in all three figures extracts as garbage; for example, the Fig. 1 axis label extracts as "jG¾0 (t) ¡ G¾ (t)j". This points to Type-3 fonts or fonts with nonstandard encoding. Embed proper fonts for accessibility and searchability.

**Tables.**
- Table 2 would be self-checking with Γ_* and Λ added (m6).
- Table 3 should be accompanied by, at minimum, one fully worked instance of Theorem 7.1. For example, O(2,8,8) with N = 21, giving t, s, λ̃_N, ϵ_N, Σϵ_j, H(t), the tail term, the perturbation term and the nearest gap.

---

## Recommendation

**Minor revision**, bordering on major if M1 cannot be answered by rigorous enclosures.

- **Confidence: high** for Sections 2–6. I re-derived every bound and reproduced every constant of Tables 1 and 2 independently.
- **Confidence: medium** for Section 7. The theorem is correct, but its numerical application cannot be verified from the manuscript.

---

## What resolves each issue

**Major issues**

| Issue | What resolves it |
|---|---|
| M1 | Either (i) document guaranteed two-sided enclosures for λ_0..λ_N: the method for the lower bounds, the treatment of the curved geodesic boundary, rounding control, and the merging of the Dirichlet/Neumann lists with multiplicity. Add a rigorous systole lower bound (finite enumeration with a proven cut-off, e.g. via Lemma 2.2) and a proven diameter bound for O_ϑ. Include one fully worked instance (see Presentation). Or (ii) if the enclosures are not rigorous, replace "certificate/certifies/certified" in the abstract, p. 3, Section 7, Table 3 and Fig. 2 by wording such as "the criterion of Theorem 7.1 is satisfied by the computed spectra with the estimated errors". |
| M2 | Add a sentence and a formula showing that (4), with K chosen so that t_*^K Q(K) ≤ Γ_*/16, evaluates G_σ(t_*) within the margin. Add λ̃_j ≥ 0 to Theorem 1.1 and Theorem 1.2, or replace λ̃_j by max(λ̃_j, 0) in the rule. |

**Minor issues**

| Issue | What resolves it |
|---|---|
| m1 | Delete 1/t_* from δ or explain it. |
| m2 | Restate Lemma 2.3 for any 0 < ℓ ≤ ℓ(O). |
| m3 | Drop the sign remark or use max instead of sum (optional improvement). |
| m4 | Define the notation C_l. |
| m5 | Rephrase the sentence on p. 11. |
| m6 | State that t_2 never binds; add Γ_*, Λ (and t_2 or t_*) to Table 2. |
| m7 | Correct "near 8" to "about 9, tending to 8", or give the computed ratios. |
| m8 | Prove the ε^{−3}log(1/ε) upper bound in one line, or hedge on p. 20 as on p. 14. |
| m9 | Give a formula for N_obs. |
| m10 | State how A (and M) are obtained in Theorem 7.1, or that they are assumed. |
| m11 | Optionally use the decay-weighted Lipschitz bound to enlarge δ. |
| m12 | Remark that k_*, γ_* can be computed exactly on the finite set Sig(A,M), and discuss the much smaller N that a verified finite gap computation at moderate t would give. |
| m13 | Explain the origin of the ε values in Table 2 and state that D is the exact formula. |
| m14 | Optional: note inf_s e^{sx}Z(s) in Proposition 5.2. |
| m15 | Add the clause defining δ in the compactness argument. |
| m16 | Clarify the ranges quoted in the abstract and on p. 3. |

**Presentation:** add legends and keys to Figs. 1 and 2, fix the "both errors"/"sum" discrepancy in the Fig. 1 caption, make the hidden markers in Fig. 2 visible, describe the reference lines in Fig. 3(b), embed proper fonts in the figures, and add a worked certificate instance next to Table 3.

---

My scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-4/B-c-heat-kernel-counting-analyst/scratch/`:
- `consts.py`, `run1.py`, `run2.py`, `run3.py`: constants, expansion checks, Tables 1–2
- `fig1.py`: the Figure 1 curves
- `lemma61.py`, `sharpk.py`: the Lemma 6.1 gap test and the exact-k_* comparison
- `systole.py`: triangle-group systoles
- `ds.pdf`: the Dryden–Strohmaier paper (arXiv math/0504571v2)
