<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Referee report: "How much of a hyperbolic orbifold does heat hear?" (Annals of Global Analysis and Geometry)

Remit: rigour, citations, figures and numerical reproducibility. I read the manuscript (47 pp.) and the electronic supplement (19 pp.) in full, and I viewed every figure as a rendered page image (110 dpi, with Figs 3 and 6 also at 300–400 dpi). Under the rules of this review I did not open the authors' code and data deposit. Every computational claim below was therefore checked by independent recomputation from the formulas and data printed in the paper and supplement. My scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/A-e-reproducibility-referee/scratch/comp/`. The tool refused to write REPORT.md, so this message is the complete report.

## Summary

The paper studies closed orientable 2-orbifolds of curvature −1 with cone points. It asks for the least number of heat invariants c₁, c₂, … that determines the genus and the cone orders (K_mult), and how that number grows with area. The main results are as follows.

- **Theorem 1.1.** Square-root lower and linear upper bounds for f(A). Equivalence of power-law lower bounds f(A) ≥ cA^α with the Prouhet–Tarry–Escott bound N(k) = O(k^{1/α}), through the minimal configuration size T(L) (Proposition 3.15).
- **Theorem 1.2.** For cone orders at most M, the sharp area-free count M+1, proved by a sign-change (Descartes-type) argument.
- **Theorem 1.3.** Newton/Hurwitz algebra: n invariants suffice on spheres with n cone points; det M = ±∏(mᵢ+mⱼ)/∏mᵢ; and a Descartes bound on genus changes.
- **Theorem 1.4.** Three invariants determine a triangle orbifold, and two first fail on O(2,8,8)/O(3,3,12), a pair isolated by the rank-0 curve C₂₇/₂.
- **Corollary 1.5.** The area bound ⌊A/π⌋+4.

Around these the paper gives:
- a self-contained all-order heat expansion with enveloping remainders (Proposition 2.7, Appendix B);
- a variable-curvature section (Propositions 2.11 and 2.13);
- a quantitative locality theorem (Theorem 4.2);
- a stability theorem for recovering the orders (Theorem 6.2);
- finite-element illustrations (Section 4, S4–S6).

I found no false main result. Every formula, constant, example pair and table entry I recomputed agrees with the paper. My objections are:
- one citation that the cited source contradicts;
- a figure whose caption and text misidentify what is plotted;
- the placement in the ESM of the only proof of a stated main-text theorem;
- a set of smaller numerical-reporting, bibliographic and notational defects.

## Significance

The new content is threefold:
- explicit, sharp, finite counts of heat invariants;
- an honest reduction of the growth question to the open N(k) = O(k) problem of the Prouhet–Tarry–Escott (PTE) theory;
- a complete treatment of the triangle family, including an elliptic-curve isolation of the minimal pair.

Much of the mechanism is elementary algebra (Newton's identities, Vandermonde, Descartes) applied to Uçar's coefficients. The authors say this candidly in "What is elementary and what is not", which I appreciate. The geometric-analytic content for this journal sits in Proposition 2.7/Appendix B, Section 2.4 and Theorem 4.2. These are careful and correct as far as I could test them. The paper is well within scope. Its value is clarity and sharpness rather than depth of new analysis; the editor and the other referees should weigh that.

What is good:
- The proofs are short and, in the places I tested, exactly right.
- Every number in the paper that I could reproduce is reproduced to the last digit.
- Computer-search statements are separated from proofs and listed (S8).
- The illustrative numerics state honestly that they are not enclosures.

## Correctness and what was recomputed

**Heat expansion (Section 2, Appendix B)**
- I recomputed φ_k(m) from (4) and checked it against the closed form Φ_m of Lemma 2.6 numerically (agreement to 10⁻²⁵).
- I recomputed p₀,…,p₄ from (5), and α₀,…,α₅. All values in (8) and after Lemma 2.8 agree.
- For l ≤ 4 the following hold: p_l(1) = 0, deg p_l = 2l+2, and the leading coefficient is |B₂ₗ₊₂|/(2(l+1)!(2l+1)).
- The constant-curvature b₃ of Remark 2.12(b) equals −p₃/m, which factors exactly as (m²−1)(m²+3)(3m⁴+2m²+19)/30240. The Δ²K coefficient of Remark 2.12(b) equals Π₄(m), checked for m = 2, 3, 5, 7, 12.
- The top coefficients of Remark 2.12(b) match |B₈|/8!·β₃,₄ with β₃,₄ = 120K³ − 42KΔK + Δ²K.
- p₁/m = 2Π₂(m) holds identically. Schueth's −m⁵ΔK/15120 follows from Proposition 2.11(iii).
- I re-derived by hand the Duhamel computation in the proof of Proposition 2.11(iii), the value −2l·l!·4ˡ tˡ C^{−2l−2}, and λ_l = 2C^{−2l−2}/(l−1)!. I also checked the ω₂ normalisation in Proposition 2.13(ii) against u₂ = K²/15.
- **Proposition B.2 (enveloping remainders).** I evaluated E_m(t) and I(t) by quadrature of the trace-formula integrals (40 digits). The sign (−1)^K and the modulus bound hold for m ∈ {2, 3, 8, 12}, t ∈ {10⁻³, 10⁻², 0.05, 0.3} and 0 ≤ K ≤ 5 (E). They also hold for t ∈ {10⁻³, 0.05, 0.5, 2} and K ≤ 6 (I).
- **Lemma 2.5.** I re-derived the bound and the constant (3), including (1+2t/(ℓ−t)) ≤ (2+3ℓ)/(2+ℓ) at t = ℓ²/(2(1+ℓ)).
- **Lemma B.1.** I checked the counting argument.
- **Equation (10)** for (2,8,8), (3,3,12) and (2,3,7): it agrees with the general c_j. c₂ = 67/48 for the minimal pair.
- d₃ = 25/12, d₄ = −1775/24 and d₅ = 153025/48 are all reproduced exactly.

**Section 3**
- **Theorem B.** I verified symbolically that the true e solves (12) and that det M = (−1)^{n(n+1)/2} ∏(mᵢ+mⱼ)/∏mᵢ, for n = 2, …, 6, including a non-integer multiset.
- **Proposition 6.1.** I rebuilt **F** and recovered amp₀,…,amp₅ = 2, 14, 498, 4062, 56230/3 (and 303654/5). The row P₃ = −18c̃₁ − 120c̃₂ − 360c̃₃ also checks.
- **Theorem C(3).** I recomputed (R, P₁, P₃, P₅) for both pairs.
- **Theorem 3.8.** I recomputed C, ν(a) and s for M = 2, …, 9 and found the least g. The areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} all agree.
- I checked c_M differences (−1)^M C a_{M−2} for M = 2, 3, 4, and the (iv) example (0;2¹⁰)/(1;4⁴), including C = 180, ν = (10, −4), s = 2, equal c₁,c₂ and Δc₃ = 1/2.
- Minimality of the areas 12π and 36π for M = 3, 4: exhaustive enumeration, no smaller pair.
- **Examples 3.6 and 3.17, (0;2⁵)/(1;2), surfaces (2;)/(0;2⁸), and (0;5,5,5)/(0;2,2,2,10)**: shared counts and areas all agree.
- **Table S1, all 20 printed pairs.** I parsed every pair. The exact area and the exact number of shared invariants (via Lemma 3.3 and the Ψ_k) agree in every case, including the exact fractions printed for L ≤ 5. I also rebuilt the L = 4 genus pair and the L = 4 equal-count pair from the recipes in S1 (Lemma 3.16 with the stated pieces and shifts). Both come out exactly as printed.
- **The 525 area classes of Figure 3.** I re-enumerated them: 525 areas, 33,946 signatures, class maxima 1/2/3 in 17/311/197 classes, first maximum-3 class s = 1/4. All agree.
- **Remark 3.2.** An exhaustive n = 4 search with orders ≤ 130 found 16 primitive witnesses. The eight with orders ≤ 84 are (A.685)–(A.692), and the two of the 16 without a pencil splitting are those listed in S1. The search-space counts C(123,5) = 216,071,394 and Σμ(d)C(⌊220/d⌋+4,5) = 4,325,115,770 also check.
- **Remark 3.18.** I confirmed the real partner triple of {1,1,1,1,7}. I checked the soundness argument of the modular filter (primes > 220 cannot divide the denominators, and rational roots of a p-integral monic cubic are p-integral).
- **Theorems 3.4, 3.11, 3.13, 3.14 and Proposition 3.15, Lemma A.1, Proposition A.2.** I checked these line by line, including the constants 2L², 16π, 12π, 4N(2L−3) and 6(L−1)²+6, and the f(A) = 1 + max{L : A_min(L) ≤ A} bookkeeping.

**Section 5**
- Table S3: 83 triads, with R distinct within each sum except at 18.
- Theorems 5.4–5.7: x*(p), S*(p) for p = 2, …, 29, and every gap value quoted (1/840, 1/2310, 1/10296; −7/936, …, −17/4680; the closed form at 3p+7).
- The first adjacent collisions of Table S2 for p ≤ 14.
- The first non-adjacent collision (5,15,15)/(7,7,21).
- Proposition S2.1: the 38 collision-free sums, reproduced up to S = 1500 (all 38 are ≤ 557; the paper goes to 4800). S = 557 has 25,575 triads.
- 1/3 + 60/224 = 101/168 = max_{S≥18} R⁻_{S,3}, as used in the proof of Lemma 5.3.
- **Theorem 5.8 (with PARI/GP 2.17.2 in a local venv, plus sympy).**
  - ψ maps E into C₂₇/₂, and φ∘ψ = id modulo the equation of E.
  - Δ(E) = 2¹⁸3⁸5⁶, conductor 90, minimal model [1,−1,1,−3002,63929] = LMFDB 90.c3.
  - Torsion is Z/6×Z/2. The orders of all eleven listed points are correct, and the flex y = 21x+64 checks.
  - #E(F₇) = #E(F₁₁) = 12.
  - ellrank gives [0,0], and the analytic rank is 0.
  - All twelve projective points lie on C₂₇/₂.
  - I re-checked by hand every local computation of the 2-isogeny descent in S7 (mod 5 on E; mod 3 and mod 9 on E′). It is correct.

**Section 6 and S3**
- ζ₃ = 1, ζ₄ = 79/3, ζ₅ = 14048/15.
- I re-derived the radii in Theorem S3.3 and the threshold in Theorem S3.4 from Rouché.
- **Table S4.** All ratios and the claimed ranges (1.03–6.72, and 5×10² to 2×10⁸) agree, as do the relative columns. I recomputed δ_up by local optimisation for the five n = 3 rows: 2.4849e−3, 4.5883e−3, 6.5869e−3, 5.0358e−4, 8.2721e−5. These match the table, rounded up.
- I checked the stated values in Propositions 6.3(i) and 6.4.
- **Table S6.** Recovering from the printed estimates gives roots 2, 8 ± 0.00502i and 2.99154, 3.00851, 11.99995, as printed.

**Section 4 and Figure 5**
- I evaluated the exact elliptic difference D_ell(t) by quadrature: 0.04672 (t=0.1), 0.04825 (t=0.2), 0.04022 (t=0.5). It matches the dashed curve of Fig. 5(a).
- The truncations d₃t, d₃t+d₄t² and d₃t+d₄t²+d₅t³ match the grey curves.
- The geodesic term of O(3,3,12), with ℓ = 1.8626 and two orientations, is 7.81×10⁻¹³ at t = 0.03 and 2.64×10⁻¹⁵ at t = 0.025, as stated in S4.
- The systoles 4b(ϑ) = 2.634 → 0.694 and the emergence times ℓ²/(4·24.5) ≈ 0.0049 to 0.050 agree with the circles of Fig. 5(b).

**Not checkable within my remit:** the finite-element spectra themselves, the n = 4 search to 440, the n = 5 search, the Remark 3.18 search, Proposition S2.1 between 1500 and 4800, and the Prouhet rows with L ≥ 4 (whose cone lists are only in the deposit).

**Citations.** I checked these at statement level against the sources, mostly arXiv versions:
- [2] Thm 4.8, Ex. 5.3, Prop. 5.5, (5.7), Ex. 5.6, (5.10), (5.13), Rem. 5.16 (exact quote), Thms 5.14–5.15
- [3] p.6 definition of N(k), Props 2–3, p.7, §6 Problem 3 (exact quote), pp. 9, 10, 25
- [4] eq. (1), Thms 1.1, 3.2, Prop. 3.3
- [5] Thm 1
- [6] Thm A and the following sentence
- [13] Thms 4.20, 3.40 and pp. 98–99 (exact quote), Cors 4.21(iv), 4.23, (4.25)
- [14] Main Thms 1–2
- [19] Rem. 4.2, Thms 4.1, 3.7, (6), (7), (15), (16), Rem. 3.2
- [23] Thm 1
- [26] Lemma 3.2
- [27] Prop. 24
- [29] (A.685)–(A.692), Identity 9 / (3.27)–(3.28), (3.33), §8.1 P1, A.1.6, A.1.17, A.1.26, A.1.33
- [31] Thm 3.1
- [34] 13.3.4–13.3.6, Cor. 13.3.7
- [35] Rems 2.6–2.7, (2.8)
- [40] (1.37), Thm 1.17
- [46] (5)
- [47] §1
- [50] proof of Thm 4.5
- [53] 90.c3
- [55] §3.3 p.70 and S7's §3.6 / (3.6.2)
- S-[8] the Bolza list: exactly 42 multiplicity-one eigenvalues below 998.

All of these are verified except as reported under M1 and m4–m8. I could not obtain the cited locations of [24], [28], [32] p.117, [48] pp. 2064/2069, Ostrowski (S-[2],[3]), [8] (4.42), [9] (6.4) or [12] Rem. 6.6. The DOIs of all other references resolve via Crossref to the stated metadata, with the exceptions in m8.

## FATAL

None. No main result is false or unsupported as far as I can determine. Every quantitative statement I could recompute is correct.

## MAJOR

**M1 (p. 10, Proposition 2.7, sentence after (5); citation [20]).** The manuscript says the extension of b_l to real m "is algebraic only, since for a cone of non-integral angle and nonzero curvature the heat expansion has a different form [20]". The cited source says the opposite. On p. 2 of [20] (arXiv:2511.22255) Schueth writes that for rotationally symmetric cones "it plays no role at all whether n = 1/f′(0) > 0 is a natural number or not … these b_ℓ(C) depend rationally on f′(0)". In her account the form of the expansion changes (half-integer powers, logarithms) only when f″(0) ≠ 0, which a constant-curvature cone of any angle does not satisfy. The paper does not use this sentence in any proof, but as written it attributes to a source a statement that the source contradicts.

**M2 (p. 26, Figure 3 caption and text; Table S1, pp. S5–S6).** The open squares are described in two ways: as "doubled Prouhet pairs" in the caption, and in the text as "the pairs that Proposition 3.12 gives from Prouhet's solutions, for L = 2, …, 6". Proposition 3.12 produces genus-0 pairs of area < 2π(3n−2), with n = 2^{2L−3} for the Prouhet–Thue–Morse solution. The plotted squares are something else. They sit at s = 12/5, ≈15, ≈63, ≈255, ≈1023 = 4^{L−1} − 1. They are the "Prouhet" rows of Table S1, which are genus-changing pairs (1; …) against (0; …), built from two Thue–Morse pieces by Lemma 3.16, i.e. the construction in the proof of Theorem 3.14(c). Example: L = 2 is (1;2,14,35) against (0;6,7,7,10,21). The plotted positions agree with Table S1 (I checked all 22 diamond and square positions against the exact areas). So it is the description that is wrong. A reader who follows the text to reproduce the squares will get different pairs.

**M3 (Theorem 6.2, pp. 36–37; Theorem 5.8, p. 35; Proposition S2.2, cited p. 34).** The only proof of Theorem 6.2 is in the electronic supplement: its constants δ₀, C_a and δ_thm, and Lemma S3.1 and Theorems S3.2–S3.4. The proof in the paper is a pointer. The same holds for the hand descent behind the rank statement of Theorem 5.8 (S7), though LMFDB and PARI confirm it independently, and for the tangency statement Proposition S2.2 used in Section 5.1. At Springer the ESM is neither copy-edited nor typeset, and readers of the archival article may not have it. A theorem stated in the article should have its proof in the article.

## MINOR

**m1 (p. 29 and S4, "Prediction"/"Result" and validation (ii)).** The agreement windows are inconsistent:
- The main text says that for t ≤ 0.025 the computed D agrees with the exact elliptic difference to 4×10⁻¹³. S4 says the same 4.0×10⁻¹³ holds on 0.0015 ≤ t ≤ 0.03.
- At t = 0.03, S4 itself (and my recomputation from the stated geodesic lengths) puts the closed-geodesic contribution of O(3,3,12) at ≈7.8×10⁻¹³. With exact spectra, D − D_ell would then be ≈ −7.8×10⁻¹³ there.
- Likewise, S4(ii) has each trace agreeing with I+E to 7.1×10⁻¹³ on [0.0015, 0.03], while Hyp ≈ 7.8×10⁻¹³ at the right end.

Either Hyp was subtracted before these agreements were measured, or the agreements hide a discretisation error of a few 10⁻¹³ at t = 0.03. Please state which, and use one window throughout.

**m2 (Table S5 and S4 "Convergence").** The quantity |λ(0.05,10) − λ(0.07,10)| is called a "conservative bound", but for low modes it is smaller than the error estimate. For example, (2,8,8) D j=1 gives 1.4e−13 against 1.3e−11, and N j=1 gives 8.5e−14 against 5.9e−13. The "conservative" error budgets of S4–S6 should use the maximum of the available differences.

**m3 (Data and code availability, p. 39; S8).** Four points:
- "One command reruns every check" is contradicted by S8: the run-all script does not rerun the n = 4 search or the Remark 3.18 search, and presumably not the finite-element spectra either. Please qualify the claim, and give hardware and run times for the expensive steps.
- The NETGEN/NGSolve/ARPACK versions should be stated in the supplement, not only "pinned in the deposit".
- The blind-recovery protocol (S5) is dated by a commit to the authors' own repository, and git timestamps are author-controlled. An externally timestamped deposit (e.g. a Zenodo version) would make the "committed before any result" claim checkable.
- Some printed claims depend on deposit-only files: the cone lists of the Prouhet rows with L ≥ 4, the exact areas for L ≥ 6, and the recipes. This is acceptable once the Zenodo DOI exists, but each such file should be named in Table S1.

**m4 (p. 6, [18]).** Theorem 1 of Abreu–Dryden–Freitas–Godinho needs the spectra on 0- and 1-forms, or the 0-spectrum together with the Euler characteristic. The authors state that they cannot prove it from the 0-spectrum alone. "Heard by heat or by the spectrum" overstates this.

**m5 (p. 6 and p. 12, [2, Thms 5.14–5.15]).** These are for closed orientable orbifolds. Say "orientable" in "the type of an orbifold with χ ≥ 0" and in "at K = 0, +1 the t⁰ coefficient already determines the orbifold type".

**m6 (p. 25, provenance of the pieces; Table S1 recipes).** The L = 6 genus piece ±{18,245,331,471,508} against ±{103,189,366,452,515} is Borwein–Lisoněk–Percival's own ideal symmetric solution (so attributed in [46]). The text credits [48] only with "Gloden's and Letac's solutions … [48, pp. 2064, 2069]". Please attribute each piece explicitly.

**m7 (p. 6 and Theorem C(1), [29, Identity 9]).** Chen states Identity 9 for integer sets of size > 1. Theorem C(1) is for complex multisets with n ≥ 2. Say "the forward direction, for integer multisets, is …". Similarly, [3, §3] defines only the *ideal* odd symmetric systems explicitly, so Problem 4's "odd symmetric system in the sense of [3, §3]" extends that definition.

**m8 (Bibliography).**
- [21]: the second editor is "de Gier, J.", not "Gier, J.".
- [9] and [10] are the same author but appear as "Dowker, S." and "Dowker, J.S.".
- [3] was received in 1992, so "the authors wrote in 1994" (p. 23) should say "in 1994 the authors noted".
- [56]: confirm the version (8.0.1) against the Zenodo record.

**m9 (p. 5).** "The computed spectra of Sections 4 and 5". Section 5 contains no computed spectra; they appear in Sections 1 (Fig. 1) and 4.

**m10 (Table 1, p. 7).** Three entries point to the wrong place:
- T(L) is not defined in Definition 3.10; it is defined in the text before Proposition 3.15 (p. 24).
- a_l (without second index) is introduced in Theorem 3.8(ii), not Lemma 2.8.
- T_g(L) (Remark 3.18) is missing.

**m11 (p. 6).** "Only finitely many signatures have a given area (Corollary 3.5)". Corollary 3.5 bounds n + 4g but does not state finiteness. Add the one-line argument (bounded n and g plus finiteness of Egyptian-fraction representations).

**m12 (Figure 8).** The axis label is ‖m̃ − m‖∞, but the quantity is the matching distance dist defined on p. 36. Use dist.

**m13 (Figure 4).** The text calls panel (a) "schematic, not isometric", but the caption does not. Figure 1's caption does say "stylised".

**m14 (Fig. 5(b) vs S6).** The emergence threshold is "ten times the error budget" in Section 4 but "10³ times the noise" in S6 for the ratio test. Say explicitly that these are two different thresholds.

**m15 (p. 32, proof of Lemma 5.3(ii)).** Write the bound as 101/168 = R⁻_{18,3}, attained at (3,7,8), the maximum of R⁻_{S,3} for S ≥ 18, and say why it is the maximum. "1/3 + 60/224" is opaque.

**m16 (p. 14, Proposition 2.13(ii)).** The example (0;3,3,3) has χ = 0. This is legitimate in the variable-curvature setting, but the rest of the paper is hyperbolic. Say so, so the reader does not think a hyperbolic example is meant.

## Presentation

**P1 (notation).** Many symbols carry two or three meanings, and Table 1 does not resolve them:
- M: integer bound and bold matrix **M**.
- C: the constant in Theorems 1.1/3.8, 2 sin(ϑ/2), C_l(m), C_hyp, C_a, and the curve C_Λ.
- a: node, distinct order, a_l, a_{l,k}.
- s: the integer in Theorem 3.8, the ratio Area/2π, and the parameter in Proposition 6.3.
- χ: Euler characteristic and the polynomial χ_m.
- κ: |U\*|+|V\*|, the constant in Theorem C(1), and curvature in the proof of Proposition 2.11.
- T: tanh series, T(L), triangle, cylinder length.
- ϱ: reciprocal sum, cutoff in Lemma B.1, remainder in Proposition B.2.
- ν: measure and multiplicity difference.
- Φ: Φ_m, isometry, and Φ(e, I).
- E: elliptic term, elliptic curve, vector in Proposition 2.13 and Proposition S3.5.
- S: sign-change count, sum, S₁ = P₁ (a redundant duplicate of P₁).
- L: number of invariants and perimeter in S4.

The authors' own disclaimer in Theorem 3.8(ii) ("the letter a without subscript is a node …") is a symptom of this.

**P2 (captions).** All captions have at most two sentences and no figure carries in-plot annotations, which complies with the house style. But the first sentences of Figs 3, 5 and 8 run to roughly 40–55 words, which is not "short". Move the detail to the text.

**P3 (forward references).** Section 2.4 relies on (13), Lemma 3.3 and Theorems A, 3.4, 3.8, 3.11 before they are stated. Either move Proposition 2.13 after Section 3 or state the needed equivalence locally.

**P4 (compression).** Some proofs are written at a density that makes checking slow, though in each case I could complete them:
- Proposition 2.11, "Pole order";
- Proposition 2.13(ii), "If": the inverse-function step, and the fact that the bumps do not touch the cone terms or Ω₀;
- Theorem 3.11, the gap-counting sentence.

One more sentence each would help.

**P5.** The signposting is exemplary: "What is elementary", the list of computer-only statements, and the "validated, not proved" language.

## Recommendation

**Minor revision.** My confidence is high for the parts within my remit, which I estimate at 85%.

I find no mathematical error. The three MAJOR items are textual and do not affect the mathematics:
- M1: a citation contradicted by its source;
- M2: a mis-described figure series;
- M3: a main-text theorem proved only in the ESM.

They must nonetheless be fixed before acceptance. The numerical illustrations are honest about their status and reproduce to the stated precision where I could test them. The remaining issues are reporting inconsistencies (m1, m2) and housekeeping.

## What resolves each issue

| Issue | What resolves it |
|---|---|
| M1 | Delete the clause, or replace it with what [20] actually says: for rotationally symmetric cones b_ℓ depends rationally on the cone angle; a different form of the expansion (half-integer powers, logarithms) arises only when f″(0) ≠ 0. Keep "algebraic only" as the authors' own caution, uncited. |
| M2 | Recaption the squares, e.g. "open squares: genus-changing pairs built by Lemma 3.16 from Prouhet–Thue–Morse pieces (Table S1)", and change the sentence on p. 26 to match. Alternatively, plot the Proposition 3.12 pairs and make Table S1 list those. |
| M3 | Move the core of S3 (Lemma S3.1, Theorems S3.2–S3.4) into an appendix of the paper, or restate Theorem 6.2 qualitatively in the main text with full proof there. Move S7 (about one page) into Appendix C, or state in Theorem 5.8 that the rank is taken from the ESM proof and LMFDB/PARI. Promote Proposition S2.2 into Section 5.1, or cite it only as a remark. |
| m1 | State whether Hyp was subtracted. Report max\|D_comp − D_ell − (Hyp₁ − Hyp₂)\| as a function of t, on one window, in both the paper and S4. |
| m2 | Define err_j as the maximum of the h- and p-differences, and recompute the budgets. |
| m3 | Qualify "one command"; give run times and hardware; list software versions in S8; deposit a timestamped protocol; name the deposit files in Table S1. |
| m4–m7 | Add the qualifications and attributions listed. |
| m8 | Correct the bibliography entries. |
| m9–m16 | Make the one-line edits indicated. |
| P1 | Rename to remove the clashes listed above (e.g. 𝔪 for the bound, Γ_Λ for the curve, σ for the sign-change count, s_A for the area ratio, h_m for the polynomial), drop S₁, and extend Table 1. |
| P2–P4 | Shorten the captions, reorder Section 2.4 or localise it, and expand the three compressed steps. |
