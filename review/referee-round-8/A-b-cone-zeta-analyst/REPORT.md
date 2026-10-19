# Referee report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

**Referee B: cone heat expansions and zeta analysis.** I covered Section 2 (constant-curvature heat invariants, cone terms, variable curvature), Appendix B (the heat expansion from the trace formula), Section 6 (stability) with Appendix C, and Sections S3, S5 and S7 of the supplement. I did not referee Sections 3–5. Where my sections cite them (Theorem 3.3, Lemma 3.6) I checked only the parts my sections use. Page numbers are the printed numbers of the manuscript, or "S" pages of the supplement. I read every typographical or sign point below on rendered page images (300 dpi PNGs) before reporting it. The scripts are in `scratch/code/` (c1–c10).

## Summary

For closed hyperbolic 2-orbifolds my part of the paper does the following.

- **Section 2 and Appendix B.**
  - Derives the full small-time heat expansion in closed form from the Selberg trace formula (Proposition 2.8).
  - Proves that the area series and the cone series each have enveloping remainders of opposite signs (Proposition B.2). This gives the explicit two-sided bound (6).
  - Bounds the closed-geodesic term explicitly (Lemmas 2.4, 2.5).
  - Proves the triangular "one new odd power sum per order" structure (Lemmas 2.9, 2.11).
  - Turns all this into a proved extrapolation of c₁,…,cₙ from n values of the heat trace (Lemma B.3, Remark B.4).
- **Section 2.4.** Treats variable curvature. Proposition 2.13 gives the structure of the cone terms; the proof is an outline. Proposition 2.15 gives extension and obstruction results, including all-order coincidence of the heat invariants of O(2,8,8) and O(3,3,12) under metrics that are flat near the cone points.
- **Section 6 and Appendix C.** Show that inverting c₁,…,cₙ to the cone orders of a sphere with n cone points is Lipschitz at simple orders and Hölder-1/k at k-fold orders. The constants are explicit up to one matrix norm, and Theorem C.4 gives a rounding threshold δ_thm. A sharper exact-arithmetic certificate is Proposition S3.1.

## Significance

The analytic content of Section 2 and Appendix B is classical in substance: the trace-formula derivation of the orbifold heat expansion goes back to the 1980s, and Uçar has all the coefficients. What is new and useful:

- the closed form of Lemma 2.7 and of (4)–(5);
- the opposite-sign enveloping property (Proposition B.2), which I had not seen stated and which turns an asymptotic series into a two-sided inequality valid for every t > 0;
- the clean, fully explicit hyperbolic-term bound.

Section 2.4 is the most interesting part to a variable-curvature specialist, but its main structural statement (Proposition 2.13) is only proved in outline. Proposition 2.15(iii) is correct but nearly tautological: flat cone points contribute only at order t⁰.

The stability results of Section 6 are a careful but standard Rouché-type perturbation analysis of a finite-dimensional algebraic inverse problem. Their value lies in being explicit and in matching the experiments, not in depth.

For AGAG the analytic part is a sound, modest contribution. I find no error in any proof I checked. My objections concern the status of Proposition 2.13 and one quantitative claim in the abstract that my computations contradict as stated.

## Correctness: what I recomputed

Everything below agrees with the manuscript unless flagged.

1. **Lemma 2.7.** The closed form for Φ_m holds numerically to 10⁻³⁹ for m = 2, 3, 7, 12. The Taylor coefficients (4) agree with the series of (cot u − m cot mu)/(4m sin u) exactly, for k ≤ 4 and m = 3, 5.
2. **Lemma 2.9 and (8).**
   - p₀, p₁, p₂ as printed. p₂ = (m²−1)(2m⁴+9m²+37)/5040.
   - p_l(1) = 0, and the leading coefficient is |B₂ₗ₊₂|/(2(l+1)!(2l+1)) for l ≤ 4.
   - α₀,…,α₄ = 1, −1/3, 1/15, −4/315, 1/315.
3. **Remark 2.14(b).**
   - At K = −1 the stated b₃ equals −p₃(m)/m exactly.
   - The coefficient of m⁷ in the K∆K term is −1/28800, which equals −42·|B₈|/8!.
   - The coefficient of ∆²K equals (m²−1)(m²+11)(3m⁴+10m²+227)/(3628800m), which is Π₄(m) (numerically, m ≤ 9).
   - 2Π₂ = p₁/m.
   - Together these confirm Proposition 2.13(ii)–(iii) at l = 1 and l = 3.
4. **Proposition 2.13(ii).**
   - From f″ = −K̄f, with K̄ = k₀ + k₁r² + k₂r⁴ + k₃r⁶, by series inversion I get β₁,₂ = 2K, β₂,₃ = 12K² − 2∆K and β₃,₄ = 120K³ − 42K∆K + ∆²K. Here ∆K(p) = −4k₁ and ∆²K(p) = −8k₀k₁/3 + 64k₂ in the rotationally symmetric metric.
   - The constant-curvature value is (2l)!/l!·Kˡ, as printed on p. 15.
5. **Proposition 2.13(iii).** I evaluated the Duhamel integral symbolically:
   2t∫|x|²ˡ(4πt)⁻¹e^{−C²|x|²/4t}(1/t − C²|x|²/4t²)dx = −2l·l!·4ˡ·tˡ·C^{−2l−2} for l ≤ 5.
   λ_l = 2C^{−2l−2}/(l−1)! follows.
6. **Proposition 2.15(ii).** I recomputed ω_n independently, by completing the square in the Fourier form of the second-order Duhamel term: ω₂,…,ω₆ = 1/30, −1/140, 1/1260, −1/16632, 1/288288. These match (−1)ⁿn(n−1)n!/(2n+1)!. The example (0;2⁸) / (0;3,3,3) gives equal c₂ = 2/3.
7. **Theorem 2.3 and Proposition 2.8.** I evaluated E_m(t) and the identity term by quadrature (40 digits) for m = 2, 5, 12, t ∈ {0.01, 0.05, 0.3, 1} and K ≤ 5. Every truncation remainder has the sign claimed in Proposition B.2 and is bounded by the next term. |b_K(m)| is increasing in m.
8. **The (2;2) example on p. 12.** The remainder after c₁, c₂ at t = 0.05 is 1.0775×10⁻³, against c₃t = 1.0417×10⁻³, so the claim holds.
9. **Lemmas 2.4 and 2.5.**
   - Rederived both integrations by parts.
   - The range condition t ≤ ℓ²/(2(1+ℓ)) and the bound (ℓ+t)/(ℓ−t) ≤ (2+3ℓ)/(2+ℓ) hold, with equality at the end of the range.
   - B and C_hyp·t^{−1/2}e^{−ℓ²/4t} agree there (4.8235×10⁶ for O(2,8,8)).
10. **Lemma B.1 and the proof of Proposition B.2.** Checked line by line, including the moment formula ∫₀^∞ r^{2k+1}/(e^{2πr}+1) dr, the sign bookkeeping of every cross term, and the Euler beta integral.
11. **Lemma B.3 and Remark B.4.**
    - Q₃ = 303.63.
    - δ₁/t₃ = 4858 (printed: 4.9×10³).
    - The largest admissible t₃ is 7.83×10⁻¹¹ (printed: 7.8×10⁻¹¹).
    - At t₃ = 10⁻¹¹ the bound on η is 2.073×10⁻¹⁹ (printed: 2.07×10⁻¹⁹).
    - B₀ is negligible even for ℓ₀ = 0.01.
    - The diameter bound D = 4.897 and the longest side arccosh(cot²(π/8)) = 2.4485 are correct.
12. **Proposition 6.1 and Proposition 6.4.**
    - amp₀,…,amp₄ = 2, 14, 498, 4062, 56230/3.
    - Row 2 of F⁻¹ is (−18, −120, −360).
    - The identity Σd_i²(3a+d_i) is correct.
    - In Proposition 6.3(i), δR = s²/(4(64−s²)) and δP₃ = 48s².
13. **Lemma C.1 and Theorem 3.3.** B = YM and det B = (−1)^{n(n−1)/2}∏(m_i+m_j) hold in exact arithmetic for n = 3, 4, 5, 6, but only with the column index of B running over 1..n (see m1). Also det M·e_n = ς_n∏(m_i+m_j).
14. **Theorem C.2 and Table S4.**
    - ζ₃, ζ₄, ζ₅ = 1, 79/3, 14048/15.
    - I recomputed δ_thm with exact cond for all eleven multisets of Table S4. All agree after downward rounding: 3.80e−7, 1.18e−7, 4.02e−11, 3.14e−11, 4.49e−7, 9.35e−7, 9.97e−8, 1.48e−9, 4.74e−10, 2.03e−9, 2.72e−12.
    - max cond = 3.5109, consistent with "at most 3.511".
15. **Recovery map.**
    - For (2,8,8), (3,3,12), (4,4,4), (7,7,7) and (2,3,7) I ran the recovery on all 27 sign/zero patterns and 20,000 random points of the box of radius δ_cert. Rounding never failed.
    - Within the box of radius δ_up, an optimiser pushes a root's real part to distance 0.50001–0.50004 from the true order. This is consistent with "nearly sharp".

## FATAL

None.

## MAJOR

**M1 (pp. 14–17, 19; abstract; p. 6). Proposition 2.13 is a proposition with an outline proof.**
The authors themselves list three steps that are not carried out (p. 15):
- the reduction of Donnelly's fixed-point coefficient to dependence on (I − dΦ_p)⁻¹ only;
- the identification of the radial part of the jet with the jet of dr² + f²dθ² modulo terms quadratic in the non-radial modes;
- uniformity in ϑ of the inversion s ↦ r and of Laplace's method.

The second and third are exactly where a careful proof can fail:
- The pole-order argument needs the O(ϑ) error in B_l(Φ) = C^{−2l−2}(X_l + O(ϑ)) to be uniform in u and in the jet.
- The step "every smooth function of (x, Φx) that vanishes to second order on the diagonal is C²r² times a series with coefficients trigonometric polynomials in ϑ" (p. 16) needs a statement about the remainder, not just the formal series.

My checks (items 3–5) confirm the formulas, but formulas are not proofs. The text also uses the proposition in substance:
- the abstract, p. 6 ("identifies its coefficient");
- the summary on p. 19 ("the cone orders still enter through at most one new odd power per order, for large enough orders");
- Proposition 2.15(i), which relies on the universality of B_l in the jet (Donnelly). That part is fine on its own.

AGAG cannot publish an unproved proposition.
*Resolution:* either give complete proofs of the three steps, or relabel 2.13 as a conjecture or "formal computation" with (ii)–(iii) as verified identities for l ≤ 7, and remove the claim from the abstract.

For (iii) alone a complete proof is close at hand. The Duhamel argument is rigorous once one notes that the fixed-point coefficient is linear in the germ to first order, and that a linear SO(2)-invariant form on ∇^{2l−2}K is a multiple of (−∆)^{l−1}K. Only the symmetry modulo quadratic terms needs a line. Part (iii) could therefore be kept as a proposition and the rest demoted.

**M2 (abstract; p. 3; Remark B.4, p. 50; Section 6, p. 42; Corollary 6.5). The claim that a proved c₃ "needs t of order 10⁻¹¹" is an artifact of the method.**
The abstract says that reading c₃ off values of the trace with a proved error "needs t of order 10⁻¹¹". That is a property of one particular estimator, not of the problem:
- it uses Lemma B.3 with exactly n = 3 nodes (t₃, t₃/2, t₃/4);
- it uses the crude target δ_thm = 3.8×10⁻⁷ rather than the authors' own rigorous δ_cert = 2.341×10⁻³.

The proof of Lemma B.3 works verbatim with n′ ≥ n nodes, by (6) with K = n′ − 1 and c₁,…,c_{n′} as unknowns. With row-wise bounds for the rows of c₁–c₃ and µ₀ = 12, A₀ = π/2, ℓ₀ = 2.2567, D = 4.897 as in Remark B.4, I find (script c9.py):
- **Target δ_thm, 9 geometric nodes:** the largest node can be t = 5.6×10⁻³, with η ≤ 6.7×10⁻¹³. Compare t ≈ 10⁻¹¹ and η ≈ 2×10⁻¹⁹ in the paper.
- **Target δ_cert, 7 geometric nodes:** the largest node can be t = 5.6×10⁻³, with η ≤ 1.8×10⁻⁸.

So the "of order 10⁻¹¹" statement is false as a necessity claim. The geometric node sets used here reach down to about 9×10⁻⁵, which computed spectra with λ_max ≈ 2×10⁴ cannot supply. If the nodes are restricted to the fit window [0.0015, 0.04] of Section S4, no configuration I tried (up to 12 equispaced nodes; script c10.py) meets either target. The paper's practical conclusion — that computed spectra do not give a proved δ₁ — therefore survives, but for a different reason: the spectral cutoff at small t, not the expansion.

*Resolution:*
- State Lemma B.3 for n′ ≥ n nodes with row-wise bounds.
- Rewrite the abstract and introduction sentence as a statement about this lemma, or replace it with the correct trade-off: what is needed is a trace accurate to about 10⁻⁸ at times of order 10⁻⁴–10⁻², which computed spectra of the stated size cannot supply, because the trace at those times needs eigenvalues beyond 2×10⁴.
- In Corollary 6.5 and Remark B.4, use δ_cert, which is rigorous, rather than δ_thm.

**M3 (Section 6, Theorems 6.2, C.4; Table S4). "Explicit" constants that are not explicit, and a lossy bound.**
δ_thm(m) and C_a(m) contain cond = ‖M(Î)⁻¹‖∞. My recomputation reproduces Table S4 only with the exact cond, and (a) is not used there. That is acceptable, but then the threshold is "computable", not "closed form". The explicit bound of Theorem C.2(a) is lossy by large factors: 76.8 vs 1 for (2,8,8); 39,317 vs 2.34 for (3,10,15,30); 117,183 vs 3.51 for (2,2,2,2,3).

δ_thm is in turn 5×10² to 2×10⁸ below δ_up. So the closed-form route to Theorem 6.2 is of little use, and every quantitative use in the paper goes through Proposition S3.1. S3.1 is relegated to the supplement and stated in a compressed form that I could not verify in full in reasonable time; I verified it only empirically, item 15.

*Resolution:* say in Theorems 6.2 and C.4 that the stated δ_thm uses the exact cond and is not the closed form. Better, move Proposition S3.1, with a readable proof, into Appendix C, since it is the result actually used (Table S4, Corollary 6.5, Section S5).

## MINOR

- **m1 (p. 51, Lemma C.1).** The column range of B is not specified. With columns 0..n−1 (the convention used for Y), B ≠ YM. With columns j = 1..n, matching the unknowns e_j, the lemma is correct (verified for n = 3–6). State j = 1,…,n.
- **m2 (p. 52, Theorem C.3).** ŝep_a = min_{b≠a}|â − b̂| is undefined when m has one distinct value, e.g. (4,4,4), (7,7,7) in Table S4. Set it to +∞ by convention.
- **m3 (p. 12, after (6)).** The (2;2) example is correct (item 8), but it shows only that the remainder exceeds the next term, which here happens because c₄ > 0. Say explicitly what "not enveloped" means (sign and magnitude), and give a case where the sign of the remainder differs from that of the next term, if one exists.
- **m4 (p. 14, Proposition 2.12 and the sentence before it).** "For K > 0 from the polynomial dependence of the coefficients on the jet of the curvature" is a one-line hand-wave. Either cite Uçar alone for K > 0 or give the argument.
- **m5 (p. 18, Proposition 2.15(ii), proof).** The bumps are used to adjust Ω₁,…,Ω_L, but H_L involves only Ω_l for l ≤ L − 2. This is harmless but confusing. Say so, or restrict to l ≤ L − 2.
- **m6 (p. 19, Proposition 2.15(iii)).** The interesting content is that flat cone points contribute only at order t⁰ and that c₂ is topological. Say so plainly; the statement "carry metrics whose heat invariants agree at every order" reads stronger than it is.
- **m7 (p. 50, Lemma B.3).** ‖V⁻¹‖∞ couples all rows. A row-wise bound for each c_j is sharper and costs nothing.
- **m8 (p. 50, Remark B.4).** "t₃ ≤ 7.8×10⁻¹¹": the exact threshold is 7.83×10⁻¹¹, consistent with downward rounding, but say "about".
- **m9 (p. 43, Proposition 6.3(ii)).** "within O(s^k)" should name the norm (on I_n, hence on c via F) and note that n is fixed.
- **m10 (p. 44, Corollary 6.5).** It assumes genus 0 and known n. Repeat these hypotheses in the statement, since the corollary is the one a reader will use.
- **m11 (Table 1, p. 9).** Πᵢ and β_{l,i} are listed as "§2.4", but Πᵢ is defined only inside a long paragraph on p. 15. Give it a displayed definition.

## Presentation

- **P1 (pp. 10–11 and 48–49).** The proofs of Lemma 2.5 and Proposition B.2 are written as run-on inline formulas. In the extracted text, the logarithmic derivative on p. 11 and the cross terms on p. 49 are nearly unreadable. Display the key identities.
- **P2 (p. 15).** The paragraph before Proposition 2.13 mixes motivation, the list of unproved steps, a non-circularity remark about Section 3, and literature. Split it, and put the list of unproved steps immediately before the outline proof.
- **P3 (p. 45, Figure 8).** The caption does not say which curve is which multiset; that is only in the text on p. 44. The y-axis label ‖m̃ − m‖∞ differs from "dist" (minimum over permutations) used in the text. Add a legend or put the key in the caption, and align the label.
- **P4.** "Enveloping" is used on pp. 6, 12 and 49 for two-sided bounds with sign. Define it once.

## Recommendation

**Major revision.** Confidence: high for the parts I checked (Section 2, Appendices B–C, Section 6, and the related supplement sections); I did not assess Sections 3–5.

Every proof in my part that is presented as complete is correct, and I recomputed all the constants and numbers involved. The revision needed:
- prove Proposition 2.13 or demote it (M1);
- correct the abstract and introduction claim about the times and accuracies needed, and generalise Lemma B.3 (M2);
- be honest about what is explicit in Section 6 and move the certificate into the paper (M3).

None of these affects the constant-curvature counting results that the paper is mainly about.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Full proof of the three listed steps; or relabel as conjecture/formal computation, keep (iii) with a complete proof, and drop the claim from the abstract. |
| M2 | Lemma B.3 for n′ ≥ n nodes with row-wise bounds. Use δ_cert. Replace "needs t of order 10⁻¹¹" by the actual trade-off: the obstruction is the spectral cutoff at small t, plus the lack of eigenvalue enclosures. |
| M3 | Label δ_thm as computable (exact cond); move Proposition S3.1 with a readable proof into Appendix C. |
| m1–m11 | As stated in each item. |
| P1–P4 | Display the key identities; restructure p. 15; add a legend to Figure 8; define "enveloping" once. |
