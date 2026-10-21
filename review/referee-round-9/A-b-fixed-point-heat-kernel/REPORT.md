<!-- Round 9 A-b referee report: returned text saved verbatim; the reviewer could not write files -->

I could not save the report: writing REPORT.md was refused, so the full report is below. My verification scripts are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/A-b-fixed-point-heat-kernel/scratch/ (check1b.py to check8.py, with a local venv). Literature fetched headlessly from arXiv is in scratch/lit/: Schueth 1812.06119 and 2511.22255, Dowker hep-th/9406002, Fursaev hep-th/9405143.

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

**Scope.** This report covers:
- Section 2 (heat invariants, cone terms, Section 2.4 with Conjecture 2.13 and Propositions 2.14 and 2.16);
- Appendix B (Lemma B.1, proof of Proposition 2.8, Proposition B.2, Lemma B.3, Lemma B.4, Remark B.5);
- Section 6 with Appendix C;
- the supplement sections these depend on (S3 with Proposition S3.1 and Table S4; S7 on variable curvature).

The marked placeholders are treated as known. Page numbers are those of the manuscript PDF; "S-p." means a page of the supplement. I read the rendered pages before reporting any typographical, sign or figure item.

## 1. Summary

**Section 2.**
- Section 2 derives the small-time heat expansion of a closed orientable hyperbolic 2-orbifold with cone points directly from the Selberg trace formula.
- The elliptic terms are put in closed form through Φ_m(u) = (cot u − m cot mu)/(4m sin u) (Lemma 2.7), which gives every coefficient (Proposition 2.8, (5)).
- Uçar's triangular structure, one new odd power sum per order (Lemma 2.11), turns the first n invariants into an affine image of (R, P_1, …, P_{2n−3}).

**Appendix B.**
- It proves the expansion, with area and cone truncations that envelop their remainders with opposite signs. This gives the bound (6).
- Lemma B.3 gives the factorial growth of the cone coefficients.
- Lemma B.4 gives a proved error for c_1, …, c_N read from finitely many values of the heat trace. Remark B.5 shows that this is usable only at very short times.

**Section 2.4 (variable curvature).**
- Conjecture 2.13 gives the structure of the cone terms and their top coefficient, with a derivation in outline.
- Proposition 2.14 proves the part of each cone term that is linear in the curvature.
- Proposition 2.16 shows that the counts lose their meaning outside constant curvature. Equal c_2 suffices for metrics with equal H_L (ii), and O(2,8,8), O(3,3,12) carry metrics, flat near the cone points, whose invariants agree to all orders (iii).

**Section 6 and Appendix C.** These give a perturbation analysis of the map from (c_1, …, c_n) to the orders of a sphere with n cone points. It has three layers: a triangular front end, a Hurwitz-factorised linear system, and Rouché's theorem. The thresholds are explicit (δ_thm), with a sharper certificate in Proposition S3.1 (δ_cert).

## 2. Significance

**Strong parts.**
- The trace-formula derivation with signed, enveloping remainders (Proposition B.2 and (6)) is clean and self-contained, and (6) is genuinely useful.
- Proposition 2.14 is a correct, short and new all-order statement about the linear part of the cone terms.
- Proposition 2.16(ii) is a neat and correct obstruction: in variable curvature c_2 does not even determine χ.

**Weaker parts.**
- Conjecture 2.13 is unproved, and much of its stated content is either proved elsewhere in the paper or is Fursaev's structure (M1).
- Proposition 2.16(iii) is close to trivial once one notes that flat cone points contribute only to c_2.
- Section 6 is careful numerical analysis of an algebraic map. Its geometric content, a separation threshold for integer orders, cannot be reached from computed spectra, by the paper's own Remark B.5 (M3).
- The "new" label for the closed form with remainders and for Lemma B.3 is overstated (m1).

## 3. Correctness, and what I recomputed

I found **no mathematical error** in any statement I checked. All checks were done in exact rational arithmetic (sympy) or at 30–60 digits (mpmath).

**Section 2.1.**
- Theorem 2.3: the normalisation is correct, and the elliptic term tends to (m²−1)/(12m) as t → 0.
- Lemma B.1: correct line by line, including the η_T counting test and the bound ψ̂ ≥ 1/2 for ϵ ≤ 1.
- Lemma 2.4: correct.
- Lemma 2.5: I re-derived the integration by parts and the bound on the tail integral. The endpoint identity 1 + 2t/(ℓ−t) = (2+3ℓ)/(2+ℓ) and the logarithmic derivative in ℓ hold. C_hyp in (3) is correct.

**Section 2.2 and Appendix B.**
- Lemma 2.7 agrees with the defining sum to 1e−40 at m = 7, and (4) agrees with the Taylor coefficients for k ≤ 7.
- p_0, p_1, p_2 agree with (8), and the leading coefficients agree with Lemma 2.9 for l ≤ 3.
- I recomputed α_0, …, α_5 = 1, −1/3, 1/15, −4/315, 1/315, −4/3465. The identity-term residual equals α_6 t⁵ at t = 0.05 and t = 0.02.
- Schueth's Theorem 4.1 and Remark 4.2 (arXiv 1812.06119, with Δ = −div grad) agree with b_0, b_1 and with the K² part of b_2.
- Proposition B.2: the algebra is correct, and I checked it numerically.
  - Part (a): m ∈ {2, 3, 8, 12}, K ≤ 4, t ∈ {0.01, 0.05}.
  - Part (b): K ≤ 5, t ∈ {0.01, 0.05, 0.3}.
  - Signs and bounds hold in every case. The deduction of (6) is right.
- The (2;2) claim at t = 0.05 (p. 12) is true but narrow: the remainder after c_1, c_2 is 1.0775e−3, against c_3 t = 1.0417e−3.
- Lemma B.3: the principal parts and A_m are correct.
  - The ratio of |b_l(m)| to the asymptotic formula is 1.054, 1.013, 1.006 at m = 2 for l = 10, 40, 80.
  - At m = 8 it is 0.992, 0.998, 0.999.
- The moment formula in the proof of Proposition 2.8 is correct.

**Section 2.3.** Formula (10), Proposition 2.12, the constant-curvature-K version of the expansion and |K| = −χ/(2c_1) are all correct.

**Section 2.4.**
- **Proposition 2.14.** I redid the Duhamel integral and got −2l·l!·4^l t^l C^{−2l−2}. The linear part of (−Δ)^{l−1}K for the test metric is −4^l (l!)² ε, so λ_l = 2C^{−2l−2}/(l−1)!. The SO(2)-trace argument is right.
  - Independent check at l = 2: −2Π_3(m)ΔK is exactly the ΔK term of Schueth's Theorem 4.1.
  - At l = 1 it reproduces her a_1.
- **Remark 2.15(b).**
  - The K³ coefficient equals p_3(m)/m, with p_3 = (m²−1)(m²+3)(3m⁴+2m²+19)/30240.
  - The Δ²K coefficient equals Π_4(m) = (m²−1)(m²+11)(3m⁴+10m²+227)/(3628800 m). This holds exactly and numerically at m = 2, 3, 5, 9, 14.
  - The top coefficients match β_{3,4}.
- **Conjecture 2.13(ii) formula.** I computed 4^l l! [v^{2l}](f⁻¹)′ independently for K̄ = k_0 + k_1 r² + k_2 r⁴ with the radial Laplacian. It gives β_{1,2} = 2K, β_{2,3} = 12K² − 2ΔK and β_{3,4} = 120K³ − 42KΔK + Δ²K, as stated.
- **Proposition 2.16(ii).**
  - I redid the Gaussian moment (π/t)(2/t² + (2s−1)²|ζ|²/t + s²(1−s)²|ζ|⁴).
  - The bracket defining ω_n equals (−1)^n n(n−1) n!/(2n+1)! exactly for n = 2, …, 7, and ω_2 = 1/30 gives (1/60π)∫K².
  - The bump, scaling, Vandermonde and cylinder argument is correct.
  - The example (0;2⁸) / (0;3,3,3), both with c_2 = 2/3, is correct.
- **Proposition 2.16(i) and (iii).** Both are correct.

**Section 6 and Appendix C.**
- **Proposition 6.1.** F reproduces c exactly. The absolute row sums of F⁻¹ are 2, 14, 498, 4062, 56230/3, and P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3 holds.
- **Theorem 3.3 and Lemma C.1.** These were verified exactly on five multisets: the system solves for e, det M is as stated, B = YM, and det B is as stated.
- **ζ_n.** ζ_3 = 1, ζ_4 = 79/3, ζ_5 = 14048/15.
- **Proofs of C.2–C.4.** The proofs re-derive correctly.
- **δ_thm.** All eleven values in Table S4 are reproduced from Theorem C.4: 3.803e−7, 1.189e−7, 4.492e−7, 9.354e−7, 9.973e−8, 4.021e−11, 3.147e−11, 1.487e−9, 4.744e−10, 2.031e−9, 2.7298e−12. The maximal cond is 3.5109.
- **Proposition S3.1.** The proof is correct. My rational re-implementation gives δ_cert = 2.3417e−3 (2,8,8), 4.0402e−3 (3,3,12), 3.6588e−3 (2,3,7) and 4.5392e−4 (4,4,4), matching Table S4. Test (i) alone gives only about 2.7e−4 for (2,8,8).
- **δ_up(2,8,8).** My independent search gives 2.4849e−3, against 2.485e−3 in the table.
- **Propositions 6.3(i), 6.4 and Corollary 6.5.** The algebra is correct, but see m6.

**Remark B.5.**
- Q_3 = 303.6, and 16·Q_3 ≈ 4.86e3 matches "4.9 × 10³ τ".
- τ ≈ 7.8e−11 and η ≤ 2.07e−19 are reproduced.
- The N = 8 values are reproduced: 3.6e−3 with 5.0e−13, and 1.54e−2 with 1.32e−8, smallest time 6e−5.
- arccosh(cot²(π/8)) = 2.4485.
- A word search in the triangle groups gives systoles 2.25677 for O(2,8,8) and 1.8626 for O(3,3,12), so ℓ²/4 = 0.867 as on p. 3.

## 4. FATAL

None.

## 5. MAJOR

**M1. Status and content of Conjecture 2.13 (pp. 15–17).**
- **Problem.** A two-page "Derivation in outline" ends with the proof symbol □. It admits three steps that are not carried out:
  1. that Donnelly's coefficient depends on dΦ_p only through (I − dΦ_p)⁻¹;
  2. the identification of the radial jet;
  3. uniformity of the inversion and of Laplace's method.
- **Much of the stated content is already proved or not new.**
  - In (ii), the linear part (2/(l−1)!)(−Δ)^{l−1}K follows from Proposition 2.14, since only Π_{l+1} carries m^{2l+1}.
  - The constant-curvature value (2l)!/l!·K^l follows from Proposition 2.8 and Lemma 2.9.
  - For rotationally symmetric germs, (i) is Fursaev's structure (3.26) in [16]. His c_n(α) of (3.27), at α = 2π/m, is the sum defining Π_n(m).
  - What is genuinely conjectural is (i) for non-symmetric germs and the nonlinear part of the formula β_{l,l+1} = 4^l l! [v^{2l}](f⁻¹)′.
- **The evidence is narrow.** Remark 2.15 checks only rotationally symmetric germs with l ≤ 3. For such germs, step 2 is vacuous and d(x, Φx) depends only on r and ϑ. So a proof of (i)–(ii) for rotationally symmetric germs at every l looks within reach.
- **Request.**
  - Either prove that case, or demote the outline to a remark without □.
  - Restate the conjecture so that only the unproved part is conjectural.
  - Credit Fursaev for the symmetric structure.

**M2. Asserted, not proved, steps in the new analytic proofs (Proposition 2.14, pp. 17–18; Proposition 2.16(ii), pp. 19–20).**
- **(a) Exchange of limits.** Both proofs differentiate in a parameter (ε, or θ to second order) under the small-t asymptotic expansion. "The coefficients are polynomials in the jet, so the ε-derivative may be taken coefficientwise" does not justify this exchange. It needs a remainder O(t^L) that is uniform and analytic (or C²) in the parameter, or a citation of a parametric Donnelly / Minakshisundaram–Pleijel expansion. The same applies to identifying the θ²-coefficient of the Duhamel trace with that of Ω_l.
- **(b) The trace used in Proposition 2.14.** Rot*_ϑ e^{−tΔ_ε} is not trace class on L²(ℝ²). Please define the trace used (the integral ∫ h(x, Rot x) dx, or the trace of the difference from ε = 0), and show that its expansion is the fixed-point term at 0 plus O(t^∞).
- **Assessment.** Both points are standard and almost certainly true, but these two propositions are advertised as new (p. 6), so the proofs should contain the lemma.

**M3. Overstated geometric meaning of Section 6 (pp. 5, 44–47; Appendix C).**
- **The exponents concern non-geometric data.** The Lipschitz and Hölder-1/k statements (Theorem 6.2, Propositions 6.3 and 6.4, Fig. 8) are about the map on real orders. By the paper's own disclaimer on p. 12, b_l at non-integral m is "an algebraic device".
- **The geometric content is out of reach.** For orbifolds the only geometric content is the integer separation threshold (Theorem C.4, or δ_cert with Corollary 6.5). Remark B.5 shows that a proved δ_1 ≤ δ_cert needs trace values at times below about 6e−5 with accuracy about 1e−8. The computed spectra fix the trace only for t ≥ 1.5e−3, and S5 is "validated, not proved".
- **Wording on p. 5.** The claim that Section 6 "says how accurately the invariants must be known for the counts to be usable, the quantitative side of what heat diffusion can detect" overstates this.
- **Placement of Proposition S3.1.** Corollary 6.5 and Fig. 8 rely on Proposition S3.1, whose proof is one dense paragraph (S-p. 8–9). It is correct (I re-derived it and reproduced its numbers). But a result a corollary of the paper depends on should be proved in the paper, or the corollary restricted to δ_thm.
- **Request.**
  - Reframe Section 6 and the Introduction.
  - Move Proposition S3.1 with a full proof into Appendix C, or drop it from Corollary 6.5.

## 6. MINOR

- **m1 (pp. 6, 11–12, 51). Novelty claims.** The claim that "the closed form with remainders of Proposition 2.8 [and] the growth of its cone coefficients (Lemma B.3) … are new" overstates.
  - The cot-sum identity is classical, and Fursaev's c_n(α) is the same generating function.
  - The signs come from the Taylor remainder of e^{−x}.
  - Lemma B.3 is Darboux's method at the nearest poles.
  - Suggest "a self-contained derivation with signed remainders".
- **m2 (p. 7). Dowker citation.** "Dowker computed one further coefficient [17]" is factually wrong. Dowker's letter (hep-th/9406002) states that its object is "to present a simpler derivation of Fursaev's expression": it re-derives Fursaev's a_{α,2} (b_1 in 2D) and computes nothing further. Also, "Fursaev showed" (pp. 7, 15) should read "derived", since [16] is a physics derivation.
- **m3 (p. 16). Definition of the radial jet.** Define precisely what "β_{l,i} … evaluated on the radial part of the jet" means: the curvature jet of dr² + f² dθ², and which Laplacian. In my computation Δ²K(p) carries a −(8/3)k_0k_1 correction relative to the flat (∂²)², so the convention affects the coefficient −42 in β_{3,4}.
- **m4 (p. 20). Gluing in Proposition 2.16(iii).** Say that the glued genus-g piece agrees with the flat cone metric of angle 2πα_0 on a collar. Say where the flat cylinder sits: a cone annulus is not a cylinder, so the transition must lie inside the fixed piece. Say that n and n′ may differ.
- **m5 (p. 20). Proposition 2.16(ii).**
  - The bumps adjust Ω_1, …, Ω_L, although H_L needs only l ≤ L−2. This is harmless, but should be said or the range reduced.
  - Fix the sign of E: as written, E must equal c(O′) − c(O).
- **m6 (p. 45). Proposition 6.4.** The hypothesis |d_i| ≤ a allows an order a + d_i = 0, at which R and the invariants are undefined. It should be |d_i| < a.
- **m7 (p. 52). Remark B.5, uniform versus row bounds.** The numbers 4.9e3 τ, 7.8e−11 and 2.07e−19 use the uniform bound. With the row bounds δ_{1,j}, which the remark itself uses for N = 8, they become about 1.14e3 τ, τ ≲ 3.3e−10 and η ≲ 4.6e−19. Please say so.
- **m8 (p. 52). The choice µ_0 = 12.** "µ_0 = 12, the largest order of its competitor" confuses. Lemma B.4 needs an a-priori bound on the orders of the orbifold whose trace is read, valid for whichever orbifold is the true one.
- **m9 (p. 13). Remark 2.10.** The comparison with Uçar rests on a script. Please name which of Uçar's displayed formulas fixes his sign convention for κ.
- **m10 (p. 18). Lower KΔK coefficients in Remark 2.15(b).** These rest on a single unpublished computation. Give an independent check (for example an explicit rotationally symmetric germ), or state the formula only up to those coefficients.
- **m11 (p. 52). Inputs to Lemma B.4.** Lemma B.4 needs n (genus 0, n cone points) and an a-priori bound on the orders, which c_1, …, c_n do not supply. Say this in the statement, not only on p. 44.

## 7. Presentation

- **P1 (pp. 12, 19). Italic statements carry discussion.** The statement of Proposition 2.8 includes literature discussion (Schueth, Fursaev) and the derivation of (6)–(7). The statement of Proposition 2.16 ends with a long paragraph of consequences. Move both into remarks.
- **P2 (p. 16).** "Derivation in outline … □" should be a remark without the proof symbol.
- **P3. Notation overloading in Section 2 and Appendix B.** Rename some of these:
  - T: the tanh series, the cylinder length, the trigonometric polynomial T(ϑ), and T(L);
  - C: 2 sin(ϑ/2), the class 𝒞, constants, and C_l(m);
  - ρ: the stabiliser generator, ρ_K, the radius in Lemma B.3, elements of SO(2), and ρ_u;
  - e_n: elementary symmetric functions, and the series coefficients on p. 16;
  - g: the genus, the test function, and the metric.
- **P4 (p. 46). Figure 8.**
  - The caption says three multisets, but there are four curves (the dotted realisable-data curve).
  - There is no legend.
  - The y-label ‖m̃ − m‖_∞ should be dist(m̃, m), the permutation-minimised distance defined on p. 44.
- **P5 (p. 15).** The no-circularity remark ("Section 3 is used only in Proposition 2.16 …") sits in the middle of the definition of the radial jet. Move it to the end of that paragraph.
- **P6 (pp. 11–12).** State next to (6) that the two remainders have opposite signs, (−1)^K for the cone terms and (−1)^{K+1} for the area term. At present the reader must reach Proposition B.2 to see why (6) is a maximum rather than a sum.

## 8. Recommendation

**Major revision** for the assigned parts. None of the issues needs new mathematics beyond a short uniformity lemma (M2).

Every formula, constant and table entry I could recompute is correct:
- α_k, p_l, Π_4, ω_n and β_{l,l+1};
- the enveloping remainders and the growth asymptotics;
- the amplification constants and ζ_n;
- all eleven δ_thm, four δ_cert, δ_up(2,8,8), and the numbers in Remark B.5.

Schueth's independently computed b_2 confirms Proposition 2.14 at l = 1, 2.

The reasons not to accept the paper as it stands:
- an unproved conjecture is presented in proof format, and its genuinely conjectural content is not separated out (M1);
- two exchange-of-limits steps are missing from the new analytic proofs (M2);
- the geometric significance of the stability section is overstated (M3);
- the Dowker citation is wrong (m2).

**Confidence:** high on the correctness of the checked statements; moderate on the novelty assessment of Section 2.2.

## 9. What resolves each issue

- **M1.** Prove Conjecture 2.13(i)–(ii) for rotationally symmetric germs at every l (Laplace's method in polar coordinates), or recast the outline as a remark without □. Restate the conjecture with only its unproved content, and credit Fursaev (3.26)–(3.27).
- **M2.** Add a lemma giving the fixed-point and heat expansions with remainders uniform and analytic (or C²) in the parameter. Use it in Proposition 2.14 and Proposition 2.16(ii). Define the trace used in Proposition 2.14.
- **M3.** Reframe p. 5 and the opening of Section 6. Put Proposition S3.1 with a full proof in Appendix C, or restrict Corollary 6.5 to δ_thm.
- **m1.** Temper the novelty claims and cite Fursaev's c_n(α).
- **m2.** Correct the Dowker sentence, and change "showed" to "derived" for Fursaev.
- **m3.** Define the radial-jet evaluation precisely.
- **m4, m5.** Add the collar/cylinder details; fix the index range and the sign of E.
- **m6.** Change the hypothesis to |d_i| < a.
- **m7, m8.** Say which bound the N = 3 numbers use and give the row-bound values; clarify µ_0.
- **m9–m11.** Make the textual additions indicated.
- **P1–P6.** Editorial.
