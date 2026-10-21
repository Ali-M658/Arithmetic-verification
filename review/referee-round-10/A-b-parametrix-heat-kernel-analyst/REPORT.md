<!-- Round 10, A-b, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

Writing to REPORT.md was refused (subagents may not write report files), so the full report is below.

# Referee report for AGAG: "How much of a hyperbolic orbifold does heat hear?"

**Referee B: heat-kernel parametrices (Levi, Minakshisundaram–Pleijel, Donnelly) and their uniformity in parameters**

**Scope.** I was asked to cover Section 2 (pp. 9–21), Appendix B (pp. 50–54), Appendix E (pp. 57–59) and every use of Donnelly's fixed-point expansion. That means Remark 2.15, Propositions 2.14 and 2.17, Lemma E.1, and Supplement S7 together with the variable-curvature part of S8. I checked every proof in that range line by line. I read rendered page images (pdftoppm) for pages 9–21 and 50–59 before reporting anything typographical. I did not assess Sections 3, 5 and 6, or the arithmetic, beyond the places where Section 2 feeds into them. The placeholders (author contributions, AI-use statement, DOIs, preprint identifiers) are taken as known.

---

## 1. Summary

Section 2 does four things:

1. It derives the full small-time expansion of the heat trace of a closed hyperbolic 2-orbifold from the Selberg trace formula alone (Theorem 2.3, Lemma B.1, Proposition 2.8). The cone coefficients come in closed form through Φ_m(u) = (cot u − m cot mu)/(4m sin u) (Lemma 2.7).
2. It shows that the truncated area series and the truncated cone series each **envelop** their integrals for every t > 0, with remainders of opposite sign (Proposition B.2). This gives the explicit bound (6).
3. It bounds the hyperbolic (closed-geodesic) term explicitly by the systole and the diameter (Lemmas 2.4 and 2.5). It adds Darboux-type growth of the cone coefficients (Lemma B.3), an optimal truncation (Proposition B.4) and a proved extraction of c_1, …, c_N from finitely many trace values (Lemma B.5, Remark B.6).
4. In variable curvature (Section 2.4), it:
   - proves the part of the fixed-point cone coefficient that is linear in the jet of K (Proposition 2.14: λ_l(m) = 2Π_{l+1}(m)/(l−1)!);
   - proves an extension/obstruction result (Proposition 2.17), including metrics on O(2,8,8) and O(3,3,12), flat near the cone points, with all heat invariants equal;
   - supports both with a parametric (in ε) version of Donnelly's expansion, proved by following the Levi parametrix and Volterra series uniformly in the parameter (Lemma E.1).

   A conjecture on the full cone term (Conjecture 2.13) is stated, its derivation is outlined (S7), and it is checked by computer algebra (Remark 2.16).

## 2. Significance

**What is good.** The analytic part is careful, honest about what it proves and what it does not, and in my range essentially correct.

- Getting the whole constant-curvature expansion, *with signed remainders valid for all t > 0*, from the trace formula alone is clean. It is more useful than the usual O(t^K) statement: (6) is a genuinely uniform-in-t bound, and Lemma B.5 turns it into an effective procedure.
- Proposition B.4 identifies the true scale (π/m)² of the cone series and gives an exponentially small optimally truncated error. To my knowledge this is not in the literature in this form.
- The linear-in-the-jet formula of Proposition 2.14 and the all-orders collision of Proposition 2.17(iii) are neat. Proposition 2.17(iii) answers the natural question of whether the counts survive outside constant curvature.

**What is not new.** Proposition 2.8 itself is Uçar's expansion at K = −1 (the authors say so). The enveloping property is the elementary sign of the Taylor remainder of e^{−x} integrated against a positive weight. Lemma E.1 is the standard parametrix with parameters carried along. The second-variation constants ω_n are the leading quadratic terms of the heat invariants, which are classical (see M3).

The analytic novelty is therefore real but modest. It is accurately described in parts of §1.2 and overstated in the list "(a) Analytic" (p. 7).

## 3. Correctness, and what I recomputed

Everything below was recomputed independently in exact (sympy) or 40–60-digit (mpmath) arithmetic. The scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/A-b-parametrix-heat-kernel-analyst/scratch/code/check1.py` to `check6.py`.

| Item (page) | What I checked | Result |
|---|---|---|
| Lemma 2.7 and (4) (p. 12) | Closed form of Φ_m. Taylor coefficients of Φ_m against (4) for m = 2, 3, 5, 7 and k ≤ 3 (40 digits). Positivity and monotonicity. | Correct |
| Prop. 2.8: α_k (p. 12) | Bernoulli-polynomial formula against the μ_k formula of App. B, both giving 1, −1/3, 1/15, −4/315, 1/315, −4/3465. Identity term against direct quadrature at t = 0.05 (agreement 1e−11, i.e. at the truncation level). Moment ∫r^{2k+1}/(e^{2πr}+1) via η(s)Γ(s). | Correct |
| (5), (8), Lemma 2.9 (p. 13) | p_0, p_1, p_2 as printed. Factorisations p_1 = (m²−1)(m²+11)/360 and p_2 = (m²−1)(2m⁴+9m²+37)/5040. Leading coefficient \|B_{2l+2}\|/(2(l+1)!(2l+1)) for l ≤ 5. | Correct |
| Remark 2.10 (p. 14) | Uçar normalisation mΦ_m^{(2k)}(0) = 2·4^k k! m c_k^S(π/m), symbolically for k ≤ 4. | Correct |
| (10) (p. 14) | c_1, c_2, c_3 for triangles. d_3 = 25/12 for the minimal pair (P_3 = 1032 vs 1782). | Correct |
| Lemma 2.4 (p. 11) | Dirichlet-domain packing argument. | Correct |
| Lemma 2.5 (p. 11) | Integration by parts. The bound ∫_ℓ^∞ x e^{x/2−x²/4t} ≤ (2tℓ/(ℓ−t)) e^{ℓ/2−ℓ²/4t}. The log-derivative in ℓ and its sign on the range. The constant (2+3ℓ)/(2+ℓ) at the endpoint. | Correct |
| Lemma B.1 (pp. 50–51) | Counting via η_T (the Fourier pair, the bound η_T(iy) = 2 Re ψ̂(iy−T)², and η_T ≥ 1/4). Dominated convergence on both sides. | Correct |
| Proof of Prop. 2.8 (p. 51) | Euler beta integral ∫F_a e^{sr} = [2 sin((a−s)/2)]^{−1}. Moment identity Σ_j m_{2k}(2θ_j)/(2m sin θ_j) = (2k)!φ_k/4^k. Elliptic-term normalisation (reproduces b_0 = (m²−1)/(12m)). | Correct |
| Prop. B.2 (p. 52) | Checked by hand that every piece of the decomposition has sign (−1)^K (cone) or (−1)^{K+1} (area), and that the moduli sum exactly to \|b_K\|t^K and \|α_{K+1}\|t^K. Then verified numerically, with E_m and I computed by quadrature, for m ∈ {2, 3, 8, 12}, t ∈ {0.01, 0.05, 0.3, 1}, K ≤ 5: every sign and every bound holds. | Correct |
| "(2;2) at t = 0.05" (p. 13) | Remainder after c_1, c_2 is 1.0775e−3; c_3 t = 1.0417e−3. | True, with a 3% margin (m11) |
| Lemma B.3 (pp. 52–53) | Principal parts at ±π/m give A_m = (2π sin(π/m))^{−1}. Next singularity at 2π/m. Ratio \|b_l\| / [A_m (πl)^{−1/2} l! (m/π)^{2l}] = 1.0165, 1.0062 (m = 3, l = 10, 25) and 0.989, 0.996 (m = 12). | Correct |
| Prop. B.4 (p. 53) | Algebra checked. Numerically, \|b_K\|t^K is below the bound for m = 12, t ∈ {0.06, 0.02, 0.005}, with sup_k φ_k/(A_m x^k) = 1.615. | Correct |
| Lemma B.5 (pp. 53–54) | Derivation of δ_{1,j}; the role of A_0 and of the monotonicity of B in ℓ and diam. | Correct |
| Remark B.6 (p. 54) | Recomputed every printed number. Uniform bound 4.858e3 τ, τ < 7.82e−11, η ≤ 2.07e−19. Row bounds 1.139e3 τ, τ < 3.34e−10, η ≤ 4.61e−19. N = 8: τ_thm = 3.597e−3 with η ≤ 5.00e−13 at τ/2; τ_cert = 1.540e−2 with η ≤ 1.32e−8 at τ/2, smallest time 6.0e−5. Partial rescan of the negative claim: with a = 10^{−3}, N = 3 … 16, geometric and Chebyshev nodes over 24 values of T, the best δ_1 is 1.28, far above δ_cert = 2.341e−3. | Every printed value reproduced; the negative claim is consistent |
| Prop. 2.12 (p. 15) | Scaling, I_j invariance, \|K\| = −χ/(2c_1). Ω_1 = (1/60π)∫K² against Gilkey's a_4 in 2D. | Correct |
| Conj. 2.13(ii) (p. 17) | At constant curvature, 4^l l! [v^{2l}](1−κv²)^{−1/2} = (2l)!/l! κ^l. This matches the leading coefficient of p_l, since \|B_{2l+2}\|(2l)!/((2l+2)! l!) = \|B_{2l+2}\|/(2(l+1)!(2l+1)). The linear part 2/(l−1)! follows from f = r − ∫(r−s)K̄ s ds. β_{1,2}, β_{2,3}, β_{3,4} are consistent. | Correct |
| Prop. 2.14 (p. 17) | Gaussian integral −2l·l!·4^l t^l C^{−2l−2}. Linear part −4^l(l!)²ε of (−Δ)^{l−1}K. Hence λ_l = 2C^{−2l−2}/(l−1)!. Independent cross-checks: (i) 2KΠ_2(m) = K(m²−1)(m²+11)/(360m) = K p_1(m)/m exactly, so β_{1,1} = 0 and l = 1 agrees with DGGW; (ii) Π_4(m) equals the Δ²K coefficient (m²−1)(m²+11)(3m⁴+10m²+227)/(3628800m) of Remark 2.16(b) for m = 2, 3, 5, 8, 12; (iii) top coefficients of b_3 (m⁷: 1/10080, −1/28800, 1/1209600) agree with β_{3,4}\|B_8\|/8!. | Correct |
| Remark 2.16(b) (p. 18) | K³ term equals p_3(m)/m = (m²−1)(m²+3)(3m⁴+2m²+19)/(30240m) symbolically. At weight 6 the SO(2)-invariants are K³, KΔK, Δ²K and \|∇K\|², and ∇K(p) = 0 at a cone point. So the rotationally symmetric computation determines b_3 for every germ, every m ≥ 2. | Consistent |
| Prop. 2.17(ii) (p. 19) | Second-order Dyson term (t²/2)∫_0^1 tr(B e^{−(1−s)tA} B e^{−stA}) ds, which the paper has correctly. Gaussian moment formula (π/t)(2/t² + (2s−1)²\|ζ\|²/t + s²(1−s)²\|ζ\|⁴). Bracket for ω_{l+1} equals the closed form (−1)^n n(n−1)n!/(2n+1)! exactly for l = 1 … 8. **Independent check:** integrating the quadratic-in-derivative terms of Gilkey's a_6 for a surface gives ∫u_3 dA ∋ −(1/70)∫\|∇K\|² dA, which is exactly what ω_3 = −1/140 predicts. | Correct |
| Prop. 2.17(ii)–(iii) (pp. 19–20) | Examples (0;2⁸) and (0;3,3,3): both have c_2 = 2/3. For the minimal pair, Σ(1−1/m) = 9/4 and Σ(m−1/m) = 69/4 on both sides. Flat metric exponent sum −2 at ∞. Generalised Vandermonde and scaling argument. | Correct |
| Lemma E.1 (pp. 57–59) | Every step: uniform normal-coordinate radius, (E1), the transport identity for Q, (E2), the Volterra bound (2m)^i C^m V^{m−1} t^{mN−1}/(m−1)!, identification h^ε = H by Duhamel (the signs check), the rotation case via x = √t z, oddness, the identification with Donnelly's B_k. | Correct, modulo m5 and m6 |

**Bottom line on correctness.** I found no false mathematical statement in Section 2, Appendix B or Appendix E. The issues below are gaps in rigour at the interface between the global trace and the localised parametrix, one missing bridging argument, and overstated novelty.

---

## 4. FATAL

None.

## 5. MAJOR

**M1. The identification of the trace-formula cone terms with Donnelly's local fixed-point coefficients is used but never proved (pp. 16, 18–19, 50).**

Appendix B states (p. 50) that "no result of the paper rests … on the locality theorem of [1], [2, Thm 4.8]". Proposition 2.8 accordingly defines b_l(m) as the expansion coefficients of the elliptic term E_m of the Selberg trace formula.

Section 2.4 then uses a *different* object, Donnelly's local term b_l(p) = (1/m)Σ_j B_l(γ^j). It asserts that "at constant curvature K … b_l(p) = K^l p_l(m)/m, as in (5)" (p. 16). The proof of Proposition 2.17(i) (p. 19) fixes the constant in front of K_0^l by "pl(m)/m, as Proposition 2.8 shows at K_0 = −1". The list of what is proved about Conjecture 2.13 counts "the value at constant curvature (Proposition 2.8 with [19, Thm 4.20])" (p. 16).

Proposition 2.8 does not show this. It shows that the *sum over cone points* of the E_m-coefficients, plus the area term, equals c_j. To get the per-point statement one needs two facts:

- (a) the identity term per unit area is the diagonal of the heat kernel of H², so Ω_l = α_{l+1} Area/4π at K = −1;
- (b) a separation argument, for instance comparing signatures (g; m) and (g; m, m), both in Sig for g ≥ 2, to get b_l^{TF}(m) = b_l^{Don}(m) for each m.

Alternatively one can cite Uçar's per-point computation, which rests on locality. The fix is a short paragraph, but as written Proposition 2.17(i) has a gap. The paper's own claim of independence from locality makes the gap visible.

*Resolves:* add the bridging lemma with (a) and (b) above, or state explicitly that Section 2.4 uses [2, Thm 4.8] and [19, Thm 4.20] for the per-point identification.

**M2. The Duhamel steps in Propositions 2.14 and 2.17(ii) pass between the localised T(ε, t) and a global operator trace without proof (pp. 17, 19).**

Lemma E.1 proves that the expansion of T(ε, t) = ∫χ(x) h_t^ε(x, Rx) dA_ε can be differentiated term by term in ε. It does *not* prove that ∂_ε T(0, t) equals 2t tr(Rot_ϑ^* ψΔ_0 e^{−tΔ_0}) up to O(t^∞). The proof of Proposition 2.14 asserts this with "Duhamel's formula gives, up to O(t^∞)" and a parenthetical remark about trace class. The θ²-step of Proposition 2.17(ii) does the same with the second-order Dyson term.

Three things are needed:

- (i) the kernel identity ∂_ε k_t^ε(x, y) = −∫_0^t [e^{−(t−s)Δ_0} (∂_ε Δ_ε) e^{−sΔ_0}](x, y) ds on the non-compact R². Here k^ε = h^ε σ_ε is the kernel with respect to dx, the measure dA_ε also depends on ε, and one needs to be able to differentiate under ∫χ … dx;
- (ii) the off-diagonal estimate showing that the region where χ ≠ 1 contributes O(t^∞). This needs χ = 1 on a *neighbourhood* of supp ζ_0 (the text says "on the support of ζ_0"; the same applies to supp ψ in 2.17(ii)), so that both Gaussian factors in the Duhamel kernel are exponentially small there;
- (iii) cyclicity, using that Rot^* commutes with e^{−sΔ_0}, to collapse the s-integral into 2t tr(⋯).

None of this is hard. (i) follows from the Volterra representation h^ε = E + E#Φ of Step 3 of Lemma E.1, or from standard Gaussian bounds for the Duhamel kernel. But these are the only places where the paper's new variable-curvature results touch analysis, so they must be written out. The same applies to the identity-case statement "the θ² coefficient … is the t^l coefficient of the θ² part of the heat trace" on p. 19.

*Resolves:* add a lemma, for instance as part (ii) of Lemma E.1, stating and proving: for g_ε = e^{2εψ}|dx|² with ψ ∈ C_c^∞ and χ = 1 on a neighbourhood of supp ψ, ∂_ε^i T(0, t) equals the i-th Dyson term of the global trace up to O(t^∞), for i = 1, 2.

**M3. Missing classical literature, and overstated novelty of the analytic results (pp. 7, 19–20, 57).**

- (a) The second-variation constants ω_n of Proposition 2.17(ii) are the leading quadratic terms of the heat invariants. Their integrated form is computed for every order and dimension in **T. Branson, P. Gilkey, B. Ørsted, "Leading terms in the heat invariants", Proc. AMS 109 (1990) 437–450 (doi:10.1090/S0002-9939-1990-1014642-X)**. In mathematical physics they are the "form factors" of covariant perturbation theory (Barvinsky–Vilkovisky; Avramidi), which use exactly the moments ∫_0^1 (s(1−s))^n ds = (n!)²/(2n+1)! that appear on p. 20. I checked ω_2 and ω_3 against Gilkey's a_4 and a_6, and they agree. The authors' derivation is correct but should be presented as a re-derivation, with these references, and the closed form compared with BGØ.
- (b) Lemma E.1: smooth dependence of the Levi parametrix and the heat coefficients on parameters is standard. Examples are the variational formulas of Gilkey's *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem* (the smeared invariants a_n(F, D) and their conformal variations) and the parameter-dependent constructions in Berline–Getzler–Vergne, Ch. 2. "We have not found it stated in this form" (p. 57) may be literally true for the fixed-point version with a cut-off on R². However, §1.2(a) lists the "linear part of the cone terms … (Proposition 2.14, with Lemma E.1)" as new, and Gilkey and BGV are not cited anywhere. Please cite them, and say precisely what in E.1 goes beyond them (the rotation case with the cut-off and the identification with B_k).
- (c) Proposition B.2 is correct and useful, but the enveloping comes from the one-line sign of the Taylor remainder of e^{−x} against a positive weight. Listing it first among "What is new, in brief (a) Analytic" (p. 7) overstates it. The optimal truncation (B.4) and the explicit Lemma B.5 are the better claims.

*Resolves:* cite BGØ 1990, Gilkey's monograph and BGV (and optionally Avramidi and Barvinsky–Vilkovisky); compare ω_n with BGØ; reword the novelty list on p. 7.

## 6. MINOR

- **m1 (p. 16, Section 2.4 opening; p. 18, Remark 2.16).** Sign conventions in the variable-curvature formulas. Δ is the non-negative Laplacian, but "ΔK", "K∆K" and "−(1/15120) m⁵ ΔK (Schueth)" are quoted with Schueth's convention, which is not stated. Please state Schueth's sign convention where her t² coefficient is quoted, so the reader can check that the sign agrees with λ_2 = 2Π_3 (leading term m⁵/15120).
- **m2 (p. 19, proof of 2.17(i)).** Given M1, also say why b_l(p) for a germ that is only *locally* of constant curvature K_0 (with ∇^j K = 0 to the stated order) equals the global constant-curvature value. The current wording ("the only monomial left is a constant times K_0^l") is right but relies on the per-point identification.
- **m3 (p. 19, statement of 2.17(i)).** The hypothesis Ω_l(O) = Ω_l(O′) for l ≥ −1 already includes Ω_0 = χ/6, so "then χ(O) = χ(O′)" is assumed rather than concluded. The proposition is then close to Lemma 2.11 plus locality. Please say so, or drop the χ conclusion.
- **m4 (p. 18, Remark 2.15).** The sentence "as d(x, Rot_ϑ x) is bounded below where χ ≠ 1 near 0 and χ has compact support" is garbled. Presumably: "since d(x, Rot_ϑ x) ≥ c > 0 on supp χ outside a neighbourhood of 0, where χ = 1".
- **m5 (p. 58, Lemma E.1 Step 2).** The cut-off terms F are bounded by C_i t^{−3−i} e^{−c/t} after i ε-derivatives, not C t^{−3} e^{−c/t}. This is harmless but should be stated. In Step 3, the Leibniz count should also include the density in the outer E#Φ.
- **m6 (p. 59, end of E.1).** In the identification with Donnelly's B_k, the capped rotation-invariant sphere has a *second* fixed point. Say explicitly that Donnelly's coefficient is the contribution of the fixed point 0 alone and depends only on the jet there, which the construction shows. Also say that R being an isometry of g_ε is used only in this last step.
- **m7 (p. 54, Remark B.6).** The a priori inputs ℓ_0 = 2.2567 and D = 4.897 are those of O(2,8,8). The text says μ_0 must bound "whichever orbifold's trace is read", and the same is true of ℓ_0 and D. The competitor O(3,3,12) has the *smaller* systole (ℓ ≈ 1.87 by p. 3) and a different diameter. The numbers are unaffected, since B_0 is negligible at these times; I checked that this remains so with ℓ_0 = 1.86, D = 5 at t ≈ 1.5e−2. But the logical statement should use bounds valid for every candidate.
- **m8 (p. 50, Lemma B.1).** "ψ̂(r) ≥ cos(ϵr)" needs |ϵr| ≤ π/2. That holds under ϵ ≤ 1 and |r| ≤ 1, but please say so.
- **m9 (p. 13).** Lemma B.3 is stated for every ρ < 2. For m = 2, Φ_2(u) = 1/(8 cos u), whose next pole is at 3π/2, so any ρ < 3 works. This is optional, but it is a nice sanity check worth a footnote.
- **m10 (p. 18, Remark 2.16(b)).** "For every m ≥ 2" is justified for *all* germs, not only rotationally symmetric ones, by the weight-6 invariant count (K³, KΔK, Δ²K, |∇K|², with ∇K(p) = 0). Please add that sentence; otherwise the reader assumes the formula is proved only for rotationally symmetric germs.
- **m11 (p. 13).** The (2;2) illustration holds by about 3% (1.0775e−3 against 1.0417e−3). Please give the numbers so the reader sees that the statement is robust.

## 7. Presentation

- **P1 (throughout Section 2 and the appendices).** Several symbols carry two or three meanings within a few pages:
  - K: curvature, and the truncation index in (6), B.2 and B.4;
  - χ: Euler characteristic, and the cut-off in Remark 2.15, Proposition 2.14 and E.1;
  - C: 2 sin(ϑ/2), and generic constants (including the C of Lemma B.3/B.4 in the same proof as A_m);
  - ρ: radius ratio (B.3), normal-coordinate radius (E.1), and an element of SO(2) (2.14);
  - I: the identity term, the moments I_n (2.17), the vector 𝓘_n (9), and the derivative order in E.1;
  - ε/ϵ: the metric parameter, the systole bound in Remark 2.6, and the support in B.1.

  For a paper whose Section 2.4 mixes all of these, please rename (for example, truncation order J and cut-off η).
- **P2 (pp. 15–21).** Section 2.4 interleaves proved statements, a conjecture, an outline (S7), and computer-algebra checks. The labelling is honest, but a short table ("proved / conjectured / machine-checked, l ≤ …") at the start of 2.4 would help the reader. The paragraph after Proposition 2.17 about which Section 3 theorems "hold for pairs in that class … with Area read as −2πχ" is hard to parse and could be moved to a remark.
- **P3 (p. 16).** "Of the steps it does not carry out in full, the dependence of the fixed-point coefficient on dΦ_p only through (I − dΦ_p)^{−1} is Donnelly's theorem" reads as if that dependence were one of the unproved steps. Reword it: "The dependence … is Donnelly's theorem; two steps are not carried out: …".
- **P4 (p. 17, proof of 2.14).** One sentence would make the factor 2t in ∂_ε T = 2t tr(Rot^* ψΔ_0 e^{−tΔ_0}) transparent: ∂_εΔ_ε|_0 = −2ψΔ_0, and Rot^* commutes with e^{−sΔ_0}, so the Duhamel s-integral collapses by cyclicity.

No typographical, sign or figure errors were found on the rendered pages in my range. Every displayed formula I recomputed matches.

## 8. Recommendation

**Minor revision**, as far as Section 2, Appendices B and E and the uses of Donnelly's expansion are concerned. My confidence is high (about 85%) that, once M1–M3 are addressed, these parts are correct and publishable. I did not referee Sections 3 and 5–7.

The mathematics in my range is correct. Every formula and number I recomputed agrees, including all of Remark B.6 and independent cross-checks against Gilkey's a_6, DGGW and Uçar. M1 and M2 are gaps in rigour that need a paragraph or a short lemma each, not new ideas. M3 is a literature and novelty issue that changes how the analytic contribution should be presented, not whether it is right.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | A lemma identifying the per-point E_m coefficients with Donnelly's b_l(p) at curvature −1: H² diagonal plus comparison of (g; m) with (g; m, m). Alternatively, state that Section 2.4 uses [2, Thm 4.8] and [19, Thm 4.20]. |
| M2 | Lemma E.1(ii): ∂_ε^i T(0, t) equals the i-th Dyson term of the global trace up to O(t^∞), for i = 1, 2, with χ = 1 on a neighbourhood of supp ψ. Proved via the Volterra representation or Gaussian bounds for the Duhamel kernel. |
| M3 | Cite Branson–Gilkey–Ørsted 1990 (and form-factor literature), Gilkey's monograph and BGV. Compare ω_n with BGØ. Reword §1.2(a). |
| m1–m11 | As stated in each item. All are one-sentence fixes. |
| P1–P4 | Rename the clashing symbols. Add a status table at the start of 2.4. Reword p. 16 as in P3. Add the sentence in P4. |
