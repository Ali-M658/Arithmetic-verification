<!-- Round 9 A-e referee report: returned text saved verbatim; the reviewer could not write files -->

Writing REPORT.md was refused, so the full report is below.

# Referee report (rigour, citations and figures): "How much of a hyperbolic orbifold does heat hear?"

Submitted to the Annals of Global Analysis and Geometry. Materials: the manuscript (61 pp.) and its electronic supplement (17 pp.). The marked placeholders (author contributions, AI-use statement, Zenodo DOIs, preprint identifiers) are taken as known.

## Summary

The paper studies closed orientable hyperbolic 2-orbifolds with cone points. It asks for the least number K_mult of short-time heat invariants c_1, c_2, ... that determines the genus and the multiset of cone orders.

- **Analytic input.** The geometric input is the Selberg trace formula. From it the paper derives a closed form of the heat expansion at curvature −1 (Prop. 2.8, App. B). Its truncations envelop the area and cone series (Prop. B.2), with an explicit bound on the closed-geodesic term (Lemmas 2.4–2.5) and an explicit extrapolation lemma (Lemma B.4). Uçar's triangular structure (Lemma 2.11) then reduces everything to odd power sums of the cone orders together with the reciprocal sum.
- **Algebraic results.**
  - The exact bounded-order answer M+1 (Thm 3.11).
  - Separation by Newton's identities (Thm 3.7, Cor. 3.8).
  - A Descartes bound on the change of genus (Thm 3.15).
  - The equivalence of the growth of f(A) with the Prouhet–Tarry–Escott quantity N(k) (Thm 3.18, Prop. 3.19).
  - A complete treatment of triangle orbifolds, including an elliptic curve of rank 0 that isolates the minimal pair (Thm 5.9 with a hand descent in App. E).
  - A stability theory with explicit constants (Sec. 6, App. C).
- **Variable curvature.** Section 2.4 shows the counts are a constant-curvature phenomenon (Props. 2.14, 2.16; Conj. 2.13 is clearly labelled as a conjecture).

## Significance

- **Scope of the new results.** Several of the main theorems are elementary once Lemma 2.11 is available. They rest on Newton's identities, Vandermonde/Lagrange weights, Descartes' rule and Chebyshev sign changes, and the authors say so honestly in "What is elementary and what is not". The genuinely new content is:
  - the exact area-free answer M+1 with explicit witnesses;
  - the Descartes cost of a change of genus;
  - the clean reduction of the growth question to N(k);
  - the arithmetic isolation of the minimal pair;
  - the enveloping-remainder form of the expansion;
  - the variable-curvature obstruction (Prop. 2.16(iii)), which shows that the questions are meaningful only at constant curvature.
- **Theorem 1.2 adds no new bound.** It is a reformulation that relocates the growth question to an open Diophantine problem, as the authors state.
- **Fit for the journal.** This is a careful, honest, well-scoped contribution to inverse spectral geometry of orbifolds, suitable for AGAG in scope.

## Correctness and what I recomputed

I read every proof that a main result depends on. Using my own exact (sympy/rational) and high-precision (mpmath) code, I recomputed the following. Each item is my finding first, with its location in the paper.

**Expansion and cone coefficients (Section 2)**
- **Closed form of Φ_m and the coefficients (4)–(5).** Lemma 2.7 and Prop. 2.8: checked numerically.
- **The cone polynomials (8).** p_0, p_1, p_2 and p_3 agree with (8) and with the K³ coefficient in Remark 2.15(b). The leading coefficients |B_{2l+2}|/(2(l+1)!(2l+1)) agree (Lemma 2.9).
- **The area coefficients.** α_0, ..., α_4 = 1, −1/3, 1/15, −4/315, 1/315 agree with the stated formula.
- **Agreement with Uçar.** Remark 2.10's identity mΦ_m^{(2k)}(0) = 2·4^k k! m c_{S_k}(π/m) holds for m = 2, 3, 7 and k ≤ 3.
- **Triangle invariants (10).** The formula for c_3 and the difference d_3, d_4, d_5 = 25/12, −1775/24, 153025/48 for the minimal pair are correct.
- **Elliptic term and Remark 4.3.**
  - The two forms of E_m (Thm 2.3 and the integral of g_t against k_m in Remark 4.3) agree to 30 digits.
  - The Fourier identity used in Remark 4.3 holds.
  - The truncated series matches E_m at small t.
- **Remainder bound (6).** It holds for O(2,8,8) at t = 0.01 and t = 0.05 with K = 0, ..., 3. The claim that for (2;2) at t = 0.05 the remainder after c_1, c_2 exceeds c_3 t is correct: 1.078e−3 against 1.042e−3.
- **Lemma B.3.** The ratio |b_l(m)| / (A_m (πl)^{−1/2} l! (m/π)^{2l}) tends to 1 for m = 2, 3, 12 (l = 20 and 60).
- **Lemma 2.5.** I re-derived it by hand: the integration by parts, the constant C_hyp in (3), the monotonicity in ℓ and the range condition are all correct. Lemma 2.4 and Lemma B.1 are also correct.
- **Lemma B.4 and Remark B.5.** With the uniform bound: δ_1 ≈ 4.86e3 τ, the threshold τ < 7.8e−11, and η ≤ 2.07e−19 at τ = 1e−11. With N = 8 times: δ_thm is met up to τ ≈ 3.6e−3 and δ_cert up to τ ≈ 1.5e−2. The diameter bound 2·arccosh(cot²(π/8)) = 4.897 is correctly justified.
- **Intro and Section 4 numbers.**
  - Flat-cone values: 4πt h_t = 1.785 at r_0 and 1.00025 at 3r_0.
  - √0.02 / sin(π/12) = 0.546.
  - Closed-geodesic sizes for O(3,3,12): about 7.9e−13 at t = 0.03, 4.0e−13 at t = 0.0293 and 2.7e−15 at t = 0.025.

**Variable curvature (Section 2.4)**
- **Prop. 2.14.** Recomputed the Duhamel integral: it gives −2l·l!·4^l t^l C^{−2l−2}, hence λ_l = (2/(l−1)!) C^{−2l−2}.
- **Conj. 2.13(ii) and Remark 2.15.** Consistent with (5): the leading coefficient of b_l at constant curvature, the term −m⁵ΔK/15120, the Δ²K coefficient of b_3 (checked at m = 2), and the top KΔK coefficient.
- **Prop. 2.16.** The closed form of ω_n agrees with its defining sum for n = 2, ..., 8. The examples (0;2⁸) and (0;3,3,3) both have c_2 = 2/3. The exponent count in (iii) is right.

**Section 3**
- **Theorem 3.3.** det M = ς_n Π_{i<j}(m_i+m_j)/Π m_i, and the system returns the true e, for n = 3, 4, 5 (exact).
- **Lemma C.1.** B = YM and the formula for det B hold (exact, n = 3, 4, 5).
- **Prop. 6.1 and the constants of App. C.**
  - amp_0..amp_4 = 2, 14, 498, 4062, 56230/3.
  - P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3.
  - ζ_3, ζ_4, ζ_5 = 1, 79/3, 14048/15.
  - The front end reproduces c_1..c_5.
- **Theorem 3.11.**
  - The least-g areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} for M = 2..9 are correct.
  - So are ν = (−16, 9) and (28, −27, 8).
  - For M ≤ 6, the pairs share exactly c_1..c_{M−1}, and the difference in c_M equals (−1)^M C a_{M−2}.
  - Part (iv) is checked for (M, X) = (2,4), (3,5), (3,7), (4,6), (4,9): exactly c_1..c_M are shared and the difference in c_{M+1} matches.
- **Exact shared counts and areas (all correct).**
  - Thm 1.1(ii) pair (0;2¹⁰), (1;4⁴).
  - Example 3.9.
  - Theorem 3.4(3): P_3 = 1032 / 1782; P_5 = 25159618 / 21298618.
  - Example 3.21(i)–(ii).
  - Every Table S1 pair I tested: genus L = 4, 5; equal count L = 4, 5, 6; cone count L = 4–7; Prouhet L = 2, 3. The exact s values match.
- **Proofs re-derived by hand.** Thms 3.2, 3.7, 3.15, Lemmas 3.6, 3.14, Prop. 3.16, Thm 3.17, Thm 3.18(a)–(d), Prop. 3.19, Lemma A.1 and Prop. A.2: all correct.

**Section 5**
- **Strata (Thm 5.5).** Table S2 is reproduced exactly: x*(p), S*(p) and the first collisions for p ≤ 14. The equivalence "overlap ⇔ S ≥ S*(p)" holds for p < 40 and S < 300. All gap values in the proof are correct, as are the closed form for gap_p(3p+7) and the factorisations of φ_p − τ_p and φ_p′.
- **Table S3 and Computation S2.1.** The 83 triads are reproduced. I checked the collision-free sums up to S = 600 (not to 4800), and the list of 38 agrees with Computation S2.1. S = 557 has 25575 triads.
- **Theorem 5.9.**
  - ψ maps E into C_{27/2}, and φ∘ψ = id on E.
  - Δ_E = 2¹⁸3⁸5⁶, and #E(F_7) = #E(F_11) = 12.
  - The twelve points lie on E; the tangent at (16,400) meets E with multiplicity 3.
  - C_{27/2} is nonsingular and contains the twelve listed points.
  - Every congruence in the hand 2-descent of Appendix E is correct (mod 5 for d_1 ∈ {±2, ±3}; mod 3 and 9 on E′).
  - E ≅ LMFDB 90.c3 = Cremona 90c6 (via Cremona's ecdata, since LMFDB blocked headless access). Its c_4, c_6 and j match after u = 2, with rank 0 and torsion Z/2 × Z/6.
- **Prop. 5.2 and Thm 5.8.** Re-derived; correct.

**Supplement**
- The Table S4 ratio column and the δ_cert/|c_j| column are correct.
- Table S6 is consistent with the exact c_2, c_3.
- C(123,5) = 216,071,394, and the Möbius count is 4,325,115,770.
- The partner triple {0.2664, 4.2830, 6.4506} of {1,1,1,1,7} is correct.

**Figures.** I read the rendered pages (Figs. 1–8, Tables 2, S1–S6). Each figure agrees with its caption and the text:
- the X*, −X* positions in Fig. 2;
- the diamonds and squares at the s-values of Table S1 in Fig. 3;
- the first-collision circles at (20, 1/2), (34, .31), (38, .45), (62, .22), (117, .24) in Fig. 7;
- the slopes 1, 1/2, 1/3, 1/2 and the δ_cert diamonds in Fig. 8;
- the truncation shapes and the sign change near 0.36 in Fig. 5(a).

**Citations.** I fetched and checked at statement level about 35 sources. All load-bearing citations are correct, including:
- Dryden–Strohmaier eq. (1), elliptic term and Thm 1.1 / Prop. 3.3;
- DGGW Thm 4.8, (5.7), (5.13) ("twelve times" is exact), Rem. 5.16 (quote exact) and Thm 5.15;
- Garbin–Jorgenson Thm 2.5 and Rems 2.6–2.7;
- Schueth 2019 Thm 4.1 and Rem. 4.2, with the same sign convention for Δ;
- Uçar Thm 3.40 (quote exact, p. 98) and Thm 4.20 / (4.35);
- Borwein–Ingalls Props 2–3, p. 7, §6 Problem 3 (quote exact) and pp. 9–10, 25;
- Chen (A.685), (3.27)–(3.28), §8.1 P1 and A.1.6;
- Coppersmith et al. (ideal solutions known for degrees k ≤ 9 and 11; their (5));
- Holtz–Tyaglov (1.37) and Thm 1.17;
- Laurens (Steinig attribution);
- Cremona §3.3 p. 70 and (3.6.2);
- Thurston Cor. 13.3.7;
- Linowitz–Voight Thm A;
- Doyle–Rossetti Thm 1;
- Fursaev (3.26)–(3.28);
- Bordag–Kirsten–Dowker (6.4) and Nursultanov–Rowlett–Sher Rem. 6.6;
- Grieser–Maronna Thm 1;
- Philippe Thm 3.1;
- Strohmaier–Uski: exactly 42 multiplicity-one Bolza eigenvalues below 998, as the supplement says.

The attribution slips I found are listed under MINOR.

## FATAL

None.

## MAJOR

None. I found no error in any proof that a main result depends on, and no number I recomputed is wrong.

## MINOR

- **m1 (p. 5, Thm 1.3(ii); p. 28, Thm 3.15; p. 27, Lemma 3.14).** The range of L is not stated.
  - Lemma 3.14 assumes L ≥ 2, but Thm 1.3(ii) is stated for every L and is proved through L-configurations (Def. 3.13).
  - The Descartes argument works verbatim for L = 1, and the statement is true there.
  - **Fix:** state "L ≥ 1" and note that Lemma 3.14(b) holds for L = 1, or restrict to L ≥ 2.
- **m2 (p. 39, proof of Prop. 5.2).** "which leaves {2,2,2,2,x} and {2,2,2,3,x} with 3 ≤ x ≤ 5" reads as if the range applied to both families. For the first family x ≥ 2 is arbitrary; the computed bound 1 + 6/x covers all x, so the proof is correct.
  - **Fix:** say "{2,2,2,2,x} (any x ≥ 2) and {2,2,2,3,x} with 3 ≤ x ≤ 5".
- **m3 (p. 17, attribution of Dowker [17]).** "Dowker computed one further coefficient [17]" (also p. 12 and p. 15) is inaccurate. Dowker's letter gives "a simpler derivation of Fursaev's expression" and states "These values agree with those of Fursaev".
  - **Fix:** "Dowker gave an independent derivation of the second coefficient [17]".
- **m4 (p. 7, [22]).** "the singular set, through the Hodge Laplacian [22]" overstates Gittins et al. Their Thm 1.1 says the 0- and 1-spectra together distinguish orbifolds whose singular sets have codimension ≤ 3 from manifolds; the singular set itself is not recovered.
  - **Fix:** reword along those lines.
- **m5 (pp. 8, 43, Bremner–Guy–Nowakowski [36]).** Their p. 117 remark on reciprocal pairs is stated for integer n. The phrase "which holds for every rational Λ" is the authors' (correct) extension, not BGN's.
  - **Fix:** say "the argument of their remark ... holds verbatim for rational Λ".
- **m6 (p. 13, Remark 2.10).** The citation "[18, Thm 4.20(ii), (4.33)–(4.34)]" places (4.33)–(4.34) in the theorem. In Uçar's thesis they are in Cor. 4.19(ii) on p. 137; Thm 4.20 refers to (4.33). Likewise (4.25) is in Prop. 4.17, indexed c^S_ℓ(π/k).
  - **Fix:** cite "[18, Cor. 4.19(ii), (4.33)–(4.34); Thm 4.20]". Also note that Uçar's Cor. 4.21(iv) and Cor. 4.23 assume the curvature κ ≠ 0 is known (p. 7). This is harmless here but should be said.
- **m7 (p. 9, Def. 2.1).** "[8, Def. 3.1, Thm 3.2]" for the area formula: Dryden–Strohmaier's Def. 3.1 is the orbifold Euler characteristic and Thm 3.2 is Gauss–Bonnet, so Area = −2πχ is a consequence, not a statement there.
  - Similarly Thurston's area formula is in the text preceding Thm 13.3.6, and "13.3.4" is also the number of a proposition.
  - Similarly [2, (5.8)] covers corner reflectors only; mirror edges enter through (5.11)–(5.12).
  - **Fix:** adjust these pinpoints.
- **m8 (p. 12, Schueth [25] p. 2).** "Schueth discusses these all-order formulas" follows a sentence naming Donnelly, DGGW and Uçar. On p. 2 Schueth discusses only Uçar's all-order formulas; DGGW are cited there for the structure and for b_1.
  - **Fix:** "Schueth discusses Uçar's all-order formulas [25, p. 2]".
- **m9 (p. 12 and p. 15, Schueth [24]).** The equation labels (2.3), (2.4), (3.2), (3.4), (3.5) match the published AIF version only; arXiv:1812.06119 numbers equations (1)–(21).
  - Also: "she notes that the first two were already computed in [2, Ex. 5.6] (with Prop. 5.5 and (5.10) there)". The parenthesis is the authors' addition, since Schueth cites only "[9, 5.6]".
  - **Fix:** make the parenthesis visibly the authors' own.
- **m10 (p. 29, Croot–Mao–Yip [48]).** [48] writes P(k,2) for N(k).
  - **Fix:** add "(P(k,2) in their notation)" so that a reader can check the pinpoint.
- **m11 (p. 31, Chen [33]).** The sentence attributes (A.313) to Chen (2000) and (A.314)–(A.316) to Wróblewski (2009); that is correct. A.1.17 and A.1.26 are credited in Chen's survey to Gloden, Letac and others.
  - **Fix:** if Table S1 uses pieces from those sections, cite the original finders as given there.
- **m12 (p. 9, [44]).** I could not access the DGGW erratum (Project Euclid blocks headless access), so I cannot confirm that it bears on (5.7).
  - **Fix:** state in one clause what the erratum corrects, so that the reader knows whether c_2 is affected.
- **m13 (p. 36 and Section S4).** The main text rounds 3.4×10⁻¹⁴ up to "4×10⁻¹⁴".
  - **Fix:** print 3.4×10⁻¹⁴ as in the supplement.
- **m14 (Section 2.1).** The extension of the trace formula from h = ĝ, g ∈ C_c^∞, to the heat function (Lemma B.1) is correct and complete. Dryden–Strohmaier state eq. (1) for h entire of uniform exponential type, which is equivalent by Paley–Wiener.
  - **Fix:** a half-sentence noting this would remove any doubt.

## Presentation

- **P1 (supplement pp. 7–8).** The statement of Proposition S3.1 is split by the floats Table S2 and Table S3; its tests (i), (ii) appear on the next page after the tables.
  - **Fix:** keep the statement together, e.g. with [H] floats or by moving the tables.
- **P2 (p. 37, Fig. 5(b)).** The circles lie about one order of magnitude above ten times the plotted budget. The text explains that circles are drawn at the first sampled time past the threshold.
  - **Fix:** state the sampling grid in t in the caption or in Section S6, so that the reader can check the circle positions.
- **P3 (p. 31, Example 3.21 / Table S1).** The proof of the shared counts L for the large pairs is "exact computation". I re-verified several of them independently; they are correct.
  - **Fix:** say in the text that the shared counts follow from Lemma 3.6 and the stated vanishing power sums, with the program only checking them. This makes clear that no statement rests on unproved computation.
- **P4.** Generally the paper is precise to the point of density. Nearly every paragraph carries caveats about what is proved, validated or computed. This is admirable for rigour, but the introduction (pp. 2–7) would benefit from separating the statements of results from the meta-commentary.

## Recommendation

**Minor revision.**

Confidence is high for the mathematics and the numbers: I independently recomputed essentially every number and re-derived every proof that a main result depends on. Confidence is moderate on the significance judgement.

## What resolves each issue

- **m1, m2, m13, m14:** one-line edits to the statements or text.
- **m3–m11:** the specific rewordings and pinpoint corrections given under each item.
- **m12:** one clause describing the erratum.
- **P1–P3:** layout and caption changes.

No new mathematics is required.

---

My verification scripts are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/A-e-proof-completeness-auditor/scratch/code/ and the fetched sources are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/A-e-proof-completeness-auditor/scratch/cites/.
