<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Referee report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

*Writing REPORT.md was refused (subagents may not write report files), so the complete report follows here. My scratch code is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/A-d-arithmetic-fuchsian/scratch/code/`.*

**Coverage.** Sections 4, 5 and 6 of the manuscript in full, and Supplement S3–S7. I read Sections 1–3 and Appendix B only to see how these parts use them. Page numbers are those printed in the manuscript PDF; "S p." means the supplement. Before reporting anything about typography or figures, I rendered and looked at manuscript pages 27–38 and supplement pages 7–17.

## Summary

**Section 4: heat invariants do not see the moduli.**
- Corollary 4.1: every non-triangle signature has uncountably many isometry classes with the same heat expansion.
- Theorem 4.2(a) bounds the difference of the heat traces of two orbifolds with the same signature by C_hyp t^{-1/2} e^{-ℓ²/4t}.
- Theorem 4.2(b) gives the Huber–McKean leading term of that difference.
- Computed spectra illustrate both. There are about 2850 eigenvalues for each of O(2,8,8) and O(3,3,12), and eight members of a (0;3,3,3,3) family.

**Section 5: triangle orbifolds.**
- c1 and c2 are equivalent to (S1, R), and c3 adds P3. So three invariants determine O(p,q,r) among triangle orbifolds (Corollary 5.1).
- Lemmas 5.2–5.3 and Theorems 5.4–5.7 sort triads into strata by least order. They show that the first collision of (c1, c2) is O(2,8,8) and O(3,3,12) at cone-order sum 18, and that it is the only collision there.
- Theorem 5.8: collisions with Λ = S1·R = 27/2 are rational points on the cubic C_{27/2}. This cubic is isomorphic over Q to E: y² = x(x+9)(x+384), with rank 0 and E(Q) ≅ Z/2 × Z/6. Hence the scaled pair (2k,8k,8k), (3k,3k,12k) collides with no third triangle orbifold.

**Section 6: stability of the algebraic map (c1,…,cn) → cone orders of a sphere.**
- The constants are explicit, in three layers.
- The map is Lipschitz at simple orders and Hölder with exponent 1/k at k-fold orders. This is sharp for arbitrary data.
- For data that are heat invariants of real orders, the exponent is 1/2 at a double order and when all orders are equal.
- Corollary 6.5 is an a-posteriori criterion, with exact-arithmetic certificates in S3.

**The supplement** supplies the constants and certificates (S3), the finite-element spectra with an error budget (S4), a "blind" recovery (S5), the (0;3,3,3,3) family (S6), and a 2-isogeny descent done by hand (S7).

**Verdict on my sections.** I found no mathematical error in Sections 4–6 or S3–S7. Every proof that a main result rests on goes through, and every number I recomputed agreed. The problems are of four other kinds:
- the analytic substance of these sections, and the novelty they claim;
- a real gap between the "stability" theorem and actually hearing the orders from heat (M1);
- overlap with two companion manuscripts submitted at the same time (M3);
- a few statements that say more than the numerics behind them show.

## Significance

**What is good.**
- **The elliptic-curve argument is clean and correct.** Reducing isolation to C_Λ(Q) at Λ = 27/2 uses the scale invariance of Λ. The explicit birational model is right. The 2-isogeny descent in S7 is short, complete and checkable by hand. Theorem 1.4(iii) is a precise, true and attractive statement.
- **The minimal pair is genuinely minimal.** It is also minimal by area, which the paper does not say (m6).
- **Section 6's constants are explicit and reproducible.** The exact-arithmetic certificate (Proposition S3.5) is within a factor 1.03–6.72 of a constructed failure. I reproduced every failure threshold δ_up and closed-form threshold δ_thm in Table S4 for the n = 3 cases.
- **Numerics are labelled honestly throughout.** S4–S6 and Section 4 say repeatedly that eigenvalue errors are a-posteriori agreements, not enclosures, and that nothing there is used in a proof. This is exemplary.

**What is weak, as global analysis and geometry.**
- **Section 4 contains nothing new in substance.** The authors themselves say "classical in substance" (p.27) and "the sharp part … is classical" (p.29).
  - Corollary 4.1 is a count of Teichmüller dimension plus the countability of Out(Γ).
  - Theorem 4.2(a) is Lemma 2.5 applied to each orbifold, followed by |Hyp₁ − Hyp₂| ≤ max Hypᵢ.
  - Theorem 4.2(b) is the Huber–McKean leading term.
  - The only new item is the explicit constant. By the authors' own numbers (p.29, S6) it overestimates the true difference by factors of 4.4×10⁶ to 10¹⁰, because of the factor e^{3 diam} in Lemma 2.4.
- **Section 5.1 is elementary.** Theorems 5.5–5.7 are equivalent to a finite check on the 83 hyperbolic triads with S1 ≤ 18 (the paper says so on p.33). Theorem 5.4, the general first-overlap sum S*(p), is correct but no main result needs it.
- **Section 5.2 is number theory.** It is a correct rank-0 computation, which LMFDB 90.c3 confirms. Its geometric content is the observation that collisions are points on C_Λ.
- **Section 6 is conditioning analysis of polynomial root-finding** (Rouché, Hadamard, a Neumann-series certificate). Its input is assumed to be the heat invariants themselves, with an error. How that error would arise from a heat trace is explicitly not analysed (p.36, p.38, end of Appendix B). See M1.

The weight of the paper for AGAG must therefore rest on Sections 2–3, which are outside my coverage. Sections 4–6 are correct and carefully executed supporting material. They are not, by themselves, a contribution at the journal's level.

## Correctness and what was recomputed

All of this was recomputed independently with sympy, mpmath, cypari2/PARI, numpy and scipy, without the authors' deposit.

**Theorem 5.8 (the elliptic curve).**
- ψ maps E into C_{27/2}: C(ψ) reduces to 0 modulo the equation of E.
- φ∘ψ = id_E as rational maps, using φ as printed on p.35. Its y-coordinate is 8(X−Y)/Z · (−4e₂/Z² − 54).
- ψ has no base points, and C_{27/2} has no singular point.
- Disc(E) = 2¹⁸3⁸5⁶; the conductor is 90.
- The minimal model is [1,−1,1,−3002,63929]. This is identical to the LMFDB page for 90.c3, which I fetched.
- PARI `ellrank` returns [0,0,0] and `elltors` returns Z/6 × Z/2. #E(F₇) = #E(F₁₁) = 12.
- All eleven affine points listed lie on E, with the stated orders. The tangent at (16,400) is y = 21x + 64, and the residual cubic is (x−16)³.
- φ(1:4:4) = (−24,360). ψ maps the twelve points of E onto the twelve listed points of C_{27/2}.
- **Agrees.**

**S7 (the descent).** I checked every congruence by hand:
- the mod-5 non-residue argument for d₁ ∈ {±2, ±3} on E;
- the sign argument for d₁ < 0 on E′;
- the 3-adic arguments for d₁ = 3, 5, 15 on E′, including 5w² − w + 2 ≡ 6 (mod 9) for w ∈ {1, 4, 7}.

Also d′ = 3²5⁶ and c′ = −786, so the rank is 2 + 0 − 2 = 0. **Agrees.**

**Section 5.1.**
- Enumeration gives 83 hyperbolic triads with 10 ≤ S1 ≤ 18 and none with S1 < 10. The only collision with S ≤ 18 is {(2,8,8), (3,3,12)}.
- gap₃(18) = 1/840, gap₇(28) = 1/2310, gap₈(31) = 1/10296.
- The gaps at S*(p)+1 for p = 2,…,8 are −7/936, −1/72, −19/3960, −1/180, −76/15015, −1/231, −17/4680.
- The closed form for gap_p(3p+7) holds for p ≤ 15. The factorisation of φ_p − τ_p and the formula for φ_p′ both check.
- S*(p) is as stated for 2 ≤ p ≤ 15, and the gap stays ≤ 0 up to S = 1500.
- Every row of Table S2 is reproduced.
- The first collision between non-adjacent strata is (5,15,15), (7,7,21) at S = 35.
- Proposition S2.1: my enumeration finds exactly the listed collision-free sums with S ≤ 600 and no others. **I did not finish the exhaustive check for 600 < S ≤ 4800 within my time budget**, so that range is not independently verified. The only listed sum above 600 is none (the largest is 557), so the open part is the claim that no collision-free sum lies in 601–4800.
- The pairs (0;5,5,5), (0;2,2,2,10) and (0;2¹⁰), (1;4,4,4,4) share c1 and c2.
- **Agrees.**

**Section 4 and S4 (trace-formula terms).**
- p₀, p₁, p₂ from (4)–(5); the leading coefficients of p_l for l ≤ 5; p_l(1) = 0; α₀,…,α₄ = 1, −1/3, 1/15, −4/315, 1/315.
- For the pair: c1 = 1/8 and c2 = 67/48 for both; c3 = −1601/480 and −867/160; P3 = 1032 and 1782.
- d₃ = 25/12, d₄ = −1775/24, d₅ = 153025/48.
- I computed E_m(t) by quadrature of the integral in Theorem 2.3 for m = 3, 8, 12. The truncation remainders alternate in sign and are bounded by the next term, as Proposition B.2 says. The exact difference D(t) matches d₃t + d₄t² + d₅t³ as t → 0.
- Shortest geodesics by word enumeration: 2.2568, 2.8816, 3.0571 for (2,8,8) and 1.8626, 2.9807, 3.4027 for (3,3,12). These match S4.
- The geodesic contributions 7.9×10⁻¹³ at t = 0.03 and 2.7×10⁻¹⁵ at t = 0.025 match S4. D(t) changes sign near t ≈ 0.35, consistent with "near 0.34".
- For the (0;3,3,3,3) family, enumerating words of length ≤ 5 confirms that 4b(ϑ) is the shortest geodesic at ϑ = 0, 0.8, 1.6, 2.8.
- **Agrees.**

**Section 6 and S3.**
- F⁻¹ has the rows used in the text, for example P3 = −18c̃₁ − 120c̃₂ − 360c̃₃. amp₀,…,amp₄ = 2, 14, 498, 4062, 56230/3.
- The identity c = F·I_n + h₀ holds exactly, and system (12) returns e exactly.
- det M = ς_n ∏(mᵢ+mⱼ)/e_n. Lemma S3.1's B = YM, with det B = (−1)^{n(n−1)/2} ∏(mᵢ+mⱼ), holds for n = 3, 4, 5.
- ζ₃ = 1, ζ₄ = 79/3, ζ₅ = 14048/15.
- The closed-form threshold δ_thm for (2,8,8), (3,3,12), (2,3,7), (4,4,4), (7,7,7) is 3.80e−7, 1.18e−7, 4.49e−7, 9.35e−7, 9.97e−8, as in Table S4.
- The constructed failure threshold δ_up, by direct minimisation, is 2.4849e−3, 4.5883e−3, 6.5869e−3, 5.0358e−4, 8.2721e−5, as in Table S4.
- For each of these five multisets I tested 20,008 data vectors in the certified box (all 8 corners plus random points). Rounding recovered the true orders every time. This is consistent with the certificate but does not re-prove it.
- Proposition 6.3(i): δR = s²/(4(64 − s²)) and δP3 = 48s² are confirmed. The inequalities in Proposition 6.4 check.
- The proofs of Theorems S3.2–S3.4 and Proposition S3.5 are correct as written.
- **Agrees.**

**S5 (blind recovery).**
- Solving from the Table S6 estimates gives roots 2.0000 and 8.0000 ± 0.00502i for A, and 2.99154, 3.00851, 11.99995 for B, as reported.
- Enumerating triads consistent with the estimated c1, c2 gives exactly {(2,8,8), (3,3,12)}. The margins of about 100 and 20 against the certified threshold are consistent.
- **Agrees.**

**Proofs checked line by line:**
- Corollary 4.1;
- Theorem 4.2, including the tail argument in (b) with the dropped boundary term;
- Lemma 2.5, including the monotonicity in ℓ and the constant C_hyp;
- Corollary 5.1, Lemmas 5.2–5.3, Theorems 5.4–5.8;
- Proposition 6.1, Theorem 6.2, Propositions 6.3–6.4, Corollary 6.5;
- Lemma S3.1, Theorems S3.2–S3.4, Propositions S3.5 and S2.2, and S7.

**Evidence versus proof.** The paper keeps these apart well. The exceptions are m1–m3 and m11.

## FATAL

None. Within Sections 4–6 and S3–S7, Theorem 1.4 (all parts), Corollary 4.1, Theorem 4.2, Theorem 5.8 and Theorem 6.2 with its supplement constants are correct as stated.

## MAJOR

**M1. Theorem 6.2 is about exact heat invariants, not about heat (pp.35–38, Theorem 6.2, Corollary 6.5; Appendix B p.42; S5).**
- The Abstract (p.1) and Introduction (p.5) present Section 6 as recovering the cone orders "from approximate c₁,…,cₙ".
- But δ₁, the proved error of the data, "must come with the data". The paper says three times that for data read off a heat trace it does not supply δ₁ (p.36, p.38, p.42).
- So Corollary 6.5 cannot be applied to any heat trace, and S5 is, as the authors concede, validated rather than proved.
- The tools to close this gap are already in the paper. (6) and Proposition B.2 give sign-alternating remainders for every t > 0, and Lemma 2.5 bounds Hyp(t) explicitly.
- What is needed is a lemma: given Z_O at finitely many times with proved errors, and a-priori bounds µ ≤ µ₀, ℓ ≥ ℓ₀, diam ≤ D, output a proved δ₁ for c₁,…,cₙ.
- Section 6 also assumes genus 0 and a known n (p.36), which a heat trace does not supply. The relation to Theorem 1.3(ii) should be discussed.

**M2. Novelty and attribution in Section 4 (p.5; pp.27–29; Corollary 4.1, Theorem 4.2).**
- The Introduction (p.5) lists Theorem 4.2 among "three analytic results [that] carry the counts". No count in the paper depends on it.
- Its new content is the constant C_hyp, which overestimates by 10⁶–10¹⁰.
- Part (a) is Lemma 2.5 applied twice. Part (b) is classical (Huber, McKean). Corollary 4.1 is a standard dimension count.
- These should become attributed Propositions or Remarks and be removed from the list of the paper's analytic results. Alternatively, prove a genuinely new version, for example one whose constant depends only on the signature and the systole rather than the diameter.
- The companion manuscript [7] is said to contain a diameter bound (p.6). If it is used, the dependence must be explicit.

**M3. Overlap with two companion manuscripts submitted at the same time (pp.5–6, 34; S4, S2.1).** This is for the editor, before acceptance.
- The computed spectra of Sections 4–5 are shared with [7] (p.5; S4).
- The enumeration behind Proposition S2.1 is "also that of the companion note [33]" (p.34), and [33] cites Theorem 5.8 (p.6).
- The main text quotes two unrefereed results of [33] as fact (p.34): the lower bound (3/(128π⁴) + o(1)) X (log X)² for the number of colliding pairs, and that classes of every size occur infinitely often.
- I cannot judge how results are divided among the three papers, or whether Theorem 5.8 or the S2 enumerations appear in [33] in substantially the same form.
- Required: the editor should obtain [7] and [33]; the paper should state exactly which results and data are shared; the statements quoted from [33] should be removed or marked as unrefereed and unused.

## MINOR

- **m1 (p.27; S6).** "Strictly decreasing systoles 4b(ϑ), so they are pairwise non-isometric." That the systole is 4b(ϑ) is asserted without proof. Prove it, or argue non-isometry another way, for example from the separation of λ₁. My word enumeration supports the claim.
- **m2 (p.29).** "Agrees with the exact difference of the elliptic terms … which tests every order of the cone expansion at once." Agreement with the exact elliptic integral tests the spectra and Theorem 2.3. It does not test the coefficients b_l of the divergent asymptotic series; only the fit of d₃ and d₄ does. Rephrase.
- **m3 (p.29).** Three claims are stated as deductions without proof: ϕ_k(m) = A_m(m/π)^{2k}(1 + O(4^{−k})); |b_l(m)| ~ C_m l^{−1/2} l! (m/π)^{2l}; and that truncating at the smallest term leaves an error of order e^{−π²/(µ²t)}. Prove them or label them heuristic.
- **m4 (Theorem 4.2, p.28).** State that w_O counts the classes of γ and γ⁻¹ separately. S4's "multiplicities 1.997 … two orientations" depends on this convention.
- **m5 (Theorem 1.4(i), Corollary 5.1).** The comparison class is Sig₀,₃ only, and p.31 shows that two invariants fail earlier against all of Sig. Does K_mult(O(p,q,r); Sig) ≤ 3 hold? Theorem 1.2(ii) gives only max order + 1. My search found no 4-point sphere with orders ≤ 90 sharing c1–c3 with a triangle orbifold with orders ≤ 90. State the answer as proved, open, or observed.
- **m6 (Theorems 1.4(ii), 5.7).** The minimal pair is also the unique collision of least area, the more natural measure since c1 = Area/4π. Proof: a collision with R ≥ 3/4 must join strata 2 and 3, and stratum 3 has R ≤ 2/3 + 1/(S−6), which forces S ≤ 18. Up to S = 800 the next largest R among collisions is 37/60, at (2,15,20), (3,4,30).
- **m7 (proof of Theorem 5.8, p.35).** Add that ψ is a morphism (25x ± y and x − 216 never vanish together on E) and that ψ∘φ = id follows from birationality. I checked both.
- **m8 (Lemma 5.3(ii), p.32).** "(2,5,S−7) has R > 7/10" needs S ≥ 12. This holds since S ≥ 18; say so.
- **m9 (Lemma S3.1, S p.9).** The columns of B are implicitly indexed j = 1,…,n. With j = 0,…,n−1 the formula is wrong. State the indexing.
- **m10 (Table S4 caption).** "A root, or a complex pair, of real part a ± 1/2": the pair must be non-real. Otherwise δ_up = 0 for adjacent orders such as (2,3,7), because {2,3} has mean 2.5. I ran into exactly this.
- **m11 (S4 "Prediction").** "The orbifold with the smaller P3 has the larger heat trace" holds only for small t; D changes sign near t ≈ 0.34.
- **m12 (Proposition S2.1).** A purely computational statement proved by a "Method" should not be called a Proposition. Call it a Computation or Observation, consistent with S8.
- **m13 (Proposition 6.4, p.37).** The remark about n = 1 concerns a non-hyperbolic case. Say it is algebraic only, or delete it.
- **m14 (Theorem 6.2).** It is stated for n ≥ 2, but hyperbolic spheres need n ≥ 3. Say that n = 2 is algebraic only.
- **m15 (S4, S5).** The claims of blindness cannot be checked by a referee. Put the protocol in the supplement, or describe the selection rule without the word "blind".

## Presentation

- **P1 (Section 4).** Theorems and numerical illustrations are interleaved, sometimes within one paragraph. Put the numerics in a labelled subsection, for example "Numerical illustration, not used in proofs".
- **P2 (Section 5.1).** Say at the start that Theorems 5.5–5.7 amount to the finite check of Table S3, and that Theorem 5.4 is structural explanation not needed for Theorem 1.4.
- **P3 (Figures 5(a) and 7).** In Figure 5(a) the three grey truncation curves are hard to tell apart; label them directly. In Figure 7 the p = 5 circle (S = 117) sits on the right edge of the frame, and dots and circles are drawn only for p = 2,…,7 although bands go to p = 8. Say so in the caption.
- **P4 (Figure 8).** The axis label ‖m̃ − m‖∞ differs from the text's dist(m, m′) = min over permutations of the max difference. Use one notation.
- **P5 (p.35).** The display of φ is easy to misread; I first dropped a minus sign and φ∘ψ failed. Write the y-coordinate as −8(X−Y)(4e₂ + 54Z²)/Z³.
- **P6 (Figure 6, pp.30–31).** The hyperboloid has no "circular rim". Say which compact disc is drawn.
- **P7.** Define the informal notation key₂ once, in display form.

## Recommendation

**Major revision.**
- Confidence is high that the mathematics of Sections 4–6 and S3–S7 is correct: every main statement was re-derived and every recomputed number agreed.
- Confidence is moderate in the overall recommendation, because the paper's significance for AGAG rests on Sections 2–3, which I did not review.
- On my sections the paper is not rejectable for error. It needs M1 (close the gap to heat, or correct the framing), M2 (re-attribute and demote the classical material) and M3 (overlap cleared by the editor).

## What resolves each issue

- **M1:** Add a lemma extracting c₁,…,cₙ, with a proved δ₁, from finitely many values of Z_O, using (6), Proposition B.2 and Lemma 2.5 under stated a-priori bounds. Otherwise reframe Section 6 and the Abstract as conditioning of the algebraic inverse map. Discuss the assumptions of known n and genus 0.
- **M2:** Demote Corollary 4.1 and Theorem 4.2 to attributed statements, and drop them from p.5's list. Alternatively, prove a constant that does not depend on the diameter.
- **M3:** Give [7] and [33] to the editor, state precisely what is shared, and remove or flag the p.34 statements from [33].
- **m1:** A proof of the systole, or another argument for non-isometry.
- **m2:** Rephrase.
- **m3:** Prove or label heuristic.
- **m4:** State the orientation convention.
- **m5:** Add a statement about Sig.
- **m6:** Add minimality by area, with the two-line proof above.
- **m7:** Add one sentence.
- **m8:** Add the justification S ≥ 18.
- **m9:** State the column indexing.
- **m10:** Insert "non-real".
- **m11:** Add "for small t".
- **m12:** Relabel.
- **m13, m14:** Clarify that these cases are algebraic only.
- **m15:** Include the protocol, or reword.
- **P1–P7:** Editorial changes as described.
