# Referee report: "How much of a hyperbolic orbifold does heat hear?"

Submitted to *The Journal of Geometric Analysis*. Referee role: spectral geometer. My focus is the heat invariants and cone coefficients, the use of Uçar [8] and of Dryden–Gordon–Greenwald–Webb [3], Theorems A–C, the signature results (Section 3), the shape results (Section 4) and novelty. I read the whole manuscript. As instructed, I treated the placeholders (author contributions, AI-use statement, Zenodo DOI) as known and did not count them as defects. I did not consult the authors' repository.

All my computations are in my scratch folder (`heat.py`, `heat2.py`, `front.py`, `thmB.py`, `enum.py`, `overlap.py`, `descent.py`, `cubic.py`, `prouhet.py`). "Verified" below means I recomputed the item independently, not that I only read the proof.

---

## 1. Summary

The paper takes the small-time heat trace of a closed orientable hyperbolic 2-orbifold O, Z_O(t) ~ Σ_j c_j t^{j-2}. It asks how many coefficients c_j are needed to determine (a) the signature (g; m_1,…,m_n) and (b) the isometry class.

**Input (Prop. 2.4, Lemma 2.5).** The input is Uçar's constant-curvature formula. A cone point of order m contributes (−1)^l p_l(m)/m at order t^l. Here p_l is an even polynomial of degree 2l+2 with p_l(1)=0 and nonzero leading coefficient. So c_j adds one new odd power sum P_{2j−3} of the orders. For a sphere with n cone points, c_1,…,c_n form an invertible affine image of I_n = (R, P_1, P_3, …, P_{2n−3}), where R is the reciprocal sum.

**Signature results.**
- Theorem A: I_n is injective on n-multisets of complex numbers with no two summing to 0. Hence K_mult(O; P_n) ≤ n.
- Theorem B: a linear system for the elementary symmetric functions, with determinant ±∏_{i<j}(m_i+m_j)/e_n.
- Theorem C: n−1 invariants never suffice over the reals, and integer witnesses exist for n=3,4.
- Theorem 3.6 / Cor. 3.7: a moment argument on the signed padded multiset gives the uniform bound K_mult(O; Sig) ≤ ⌊Area/π⌋+4.
- Theorem 3.10: Prouhet–Thue–Morse constructions show that no uniform bound exists, with logarithmic lower growth (Cor. 3.12).

**Shape results (Section 4).** Every c_j depends only on the signature. Through the Selberg/Dryden–Strohmaier trace formula, two orbifolds of the same signature have heat traces that differ by O(t^{−1/2} e^{−ℓ²/4t}), where ℓ is the smaller systole, and this rate is attained.

**Triangle orbifolds (Section 5).**
- c_1, c_2 are equivalent to (S_1, R).
- An interval-overlap analysis of "strata" shows that c_1, c_2 determine O(p,q,r) when p+q+r ≤ 17. The first failure is O(2,8,8) vs O(3,3,12).
- c_3 always suffices.
- A rank-0 computation on the cubic (X+Y+Z)(XY+YZ+ZX) = (27/2)XYZ shows that no third orbifold joins the minimal pair.

**Other sections.**
- Section 6: stability estimates for recovering the orders from perturbed c_j.
- Section 7: finite-element spectra that illustrate the predictions.
- Section 8: arithmetic of two-coefficient collisions (scaling, dual pairs, counts, classes of every size).

## 2. Significance and novelty

**What is good.** The paper is careful and unusually explicit, and almost every concrete number I recomputed is right (Section 3 below). The organizing idea is clean: each extra power of curvature switches on one more odd power sum, so comparing two orbifolds becomes an odd moment problem for one signed multiset. The following are, as far as I can tell, genuinely new and of interest to spectral geometers:
- the uniform count ⌊Area/π⌋+4 (Cor. 3.7) and the matching statement that no fixed number suffices (Thm 3.10), with the Prouhet construction;
- the exact threshold 17/18 for triangle orbifolds and the isolation of the minimal pair (Thms 5.13, 5.14, 5.16);
- the determinant formula of Theorem B.

**What is not new, or is overstated.**

1. **Theorem 4.1 / Theorem 1.2(i)–(ii) are not new results.**
   - Uçar's Theorem 4.20 [8], which the paper itself uses in Prop. 2.4, already writes every heat coefficient of a constant-curvature orbisurface as an explicit function of the area and the cone orders. Theorem 4.1 is that statement specialised to K = −1.
   - For surfaces the underlying observation goes back to McKean (H. P. McKean, "Selberg's trace formula as applied to a compact Riemann surface", CPAM 25 (1972), 225–246): the heat invariants of a closed hyperbolic surface depend only on the genus.
   - The paper should present Theorem 4.1 and Cor. 4.5 as known or immediate, not as one of four headline theorems.
2. **Theorems 4.9–4.10 and Cor. 4.11 are standard consequences of the Selberg trace formula.**
   - The difference of two heat traces of the same signature equals the difference of the hyperbolic terms.
   - Its leading behaviour is governed by the shortest length at which the weighted length spectra differ. This is the mechanism behind Huber's theorem, which Dryden–Strohmaier [6] extended to orbisurfaces.
   - The explicit constant in Thm 4.9(b) and the remark that t^{−1/2} cannot be dropped are pleasant but routine. None of this is cited as standard.
3. **Theorem A is a modest variant of a classical fact.** The odd power sums p_1, p_3, …, p_{2n−1} of n complex numbers determine the multiset modulo insertion or deletion of pairs {a, −a}, because the signed union has an even characteristic polynomial. Theorem A replaces p_{2n−1} by the reciprocal sum, and the proof is the same parity argument. The paper says the positive case is "classical in substance" (§1.1) but claims as new the complex case under ∏(m_i+m_j) ≠ 0. The authors should state the classical odd-power-sum statement, cite a source, and describe the novelty accurately.
4. **The triangle threshold (Section 5) is elementary.** Its content is an inequality analysis of Egyptian-fraction triples with fixed sum. It is correct (Section 3 below), but its geometric depth is limited.

**Literature checks I could and could not do.** Network access to arXiv was mostly unavailable to me, so I could not check the following verbatim:
- DGGW [3] Rem. 5.16, Thms 5.14–5.15, Prop. 5.22 and (5.7);
- the numbered items of Uçar's thesis [8]: (4.25), Thm 4.20, Cors 4.21(iv), 4.23, Thm 3.40;
- the Doyle–Rossetti quotation [7, §3, p. 8].

To make up for this, I recomputed the cone coefficients independently (Section 3). So the *mathematics* taken from [8] is confirmed, even though the *citations* are not. I did confirm the following:
- Schueth's paper [24] (arXiv:1812.06119) computes cone contributions at order t², consistent with the paper's use of it for p_2.
- There is an **erratum to [3]**: Dryden, Gordon, Greenwald, Webb, *Michigan Math. J.* 66 (2017), 221–222. The manuscript neither cites nor discusses it, although Prop. 2.4 and Thm 4.1 rest on [3, Thm 4.8, Def. 4.7] (see m6).

## 3. Correctness, claim by claim (my area)

**Section 2: heat invariants and cone coefficients**

| Item | What I did | Result |
|---|---|---|
| (4)–(5), Prop. 2.4, (7): α_k and p_0…p_3 | Implemented Uçar's (4)–(5) in exact arithmetic | α_0…α_6 = 1, −1/3, 1/15, −4/315, 1/315, −4/3465, 382/675675. p_0, p_1, p_2 agree with (7). **Verified.** |
| Independent check of the cone terms b_l(m) = (−1)^l p_l(m)/m | Expanded the elliptic term E_m(t) of Thm 4.6 in t, using even derivatives of 1/(2 sin(a/2)) at a = 2πj/m. 40-digit precision, l ≤ 8, m ∈ {2,…,8,12} | Agreement to 3·10^{−40}. **Verified independently of [8].** |
| Smooth coefficients α_k | Expanded the identity term with the moments of Remark 4.12 | Identical to (5) through t^5. **Verified.** |
| Lemma 2.5 (even, degree 2l+2, p_l(1)=0, leading coefficient \|B_{2l+2}\|/(2(l+1)!(2l+1))) | Exact check for l ≤ 8; read the proof | **Verified** for l ≤ 8. The proof for all l is correct *given* formula (4) from [8] (see M2). |
| Lemmas 2.6, 2.7, Cor. 2.9, (8)–(11), the spherical (2,3,5) value 271/360, the flat values in Remark 2.11(a) | Hand and exact computation | **Verified.** |
| Remark 2.11(b): the t^0 coefficient determines the good spherical orbisurfaces | Exact check over S², S²(n,n), S²(2,2,n) for n < 400, and the Platonic cases | No coincidences. **Verified** in that range. |
| Remark 2.12: positivity, asymptotics A_l(m)(1+π²/(2m²(2l−1))), Borel radius π²/m_max² | p_l(m) > 0 for l ≤ 30, m ≤ 12. The ratio to the stated asymptotic is 1 + O(l^{−2}), e.g. 1.0002 at m=2, l=30 | **Consistent.** The claim "genus 10^4, smooth part dominates for l ≤ 8" checks, with crossover at l = 9. The proofs are only "in the repository" (see M3). |
| Lemma 2.10 | Exact computation, e.g. p_1/x = ψ_1/36 + ψ_2/360 | **Verified.** |

**Section 3: signature results**

| Item | What I did | Result |
|---|---|---|
| Theorem A | Read the proof line by line | **Correct.** |
| Theorem B: system (14) and det M = ς_n ∏(m_i+m_j)/e_n | Built M symbolically. Checked that the true e solves it and that the determinant formula holds, for n = 2…6 and 15 random multisets, some with repeats | **Verified.** |
| Remark 3.2, Theorem C(1)–(2) | Read the proofs | **Correct.** |
| Theorem C(3) values: R, P_1, P_3, P_5 for both pairs | Exact computation | **Verified.** Each pair shares exactly n−1 invariants. |
| Lemma 3.5, Thm 3.6, Cor. 3.7, Thm 3.8 | Checked the proofs, including the padding identity \|U\|+\|V\| = 2 max(n+g−g′, n′+g′−g) and the parity step "T even ⇒ T ≥ 2L+2" | **Correct.** |
| Prop. 3.9, Thm 3.10(a),(b), Remark 3.11 sizes, Cor. 3.12 | Implemented both constructions | **Verified**; details below the table. |
| Example 3.13 | Exact computation | **Verified**: the pairs share exactly 2 and exactly 3 invariants. |

Details for Thm 3.10:
- (a): L = 2, 3, 4 give 3/5, 15/17 and 63/65 cone points. Each pair shares exactly L invariants, all entries are ≥ 2, and the area bound holds.
- (b): k = 2, 3, 4 give 5/6, 23/24 and 95/96 cone points, each sharing exactly k. The k = 2 pair is (0;4,4,4,6,6) vs (0;2,2,2,3,8,8).
- The entries in (a) grow very fast: the minimum entry is about 1.6·10^8 already at L = 3. This deserves a remark (see m8).

**Section 4: shape results**

| Item | What I did | Result |
|---|---|---|
| Thm 4.6, Lemma 4.7 | Checked the elliptic and hyperbolic weights against the standard Selberg normalization; the leading elliptic term reproduces (m²−1)/(12m). Checked the approximation argument | **Correct**, apart from m7. |
| Lemma 4.8, Thm 4.9(b),(c) | Re-derived the integration by parts and the erfc step. ∫_ℓ^∞ e^x φ_t = 2tℓ e^{ℓ/2} e^{−ℓ²/4t}/((ℓ−t)√(4πt)), exactly as stated. Checked the monotonicity condition t ≤ ℓ²/(2(1+ℓ)) | **Verified.** |
| Thm 4.10, Cor. 4.11 | Read the proofs | **Correct** (standard; see Section 2). |
| Props 4.2–4.4, Cor. 4.5 | Read the proofs | **Correct.** Prop. 4.4 could be replaced by a two-line argument (see m11). |

**Section 5: triangle orbifolds**

| Item | What I did | Result |
|---|---|---|
| Prop. 5.2 / (18), Thm 5.3, Cor. 5.4–5.5 | Exact computation | **Correct.** The nonvanishing argument is convoluted (m2). |
| Lemmas 5.6–5.10, Thm 5.11 | Brute force over p ≤ 40 and 3p+3 ≤ S < 3p+120 of the claim "strata p, p+1 overlap ⟺ S ≥ S*(p)" | **0 mismatches.** The algebra in parts (a) and (c) also checks. |
| Thms 5.12, 5.13, 5.14, Prop. 5.15 | Exhaustive enumeration of hyperbolic triads with S ≤ 1000 | **Verified** to S = 1000 (the paper claims 4800); details below the table. |
| Table 1 (first adjacent collisions, p ≤ 14); first non-adjacent collision (5,15,15)/(7,7,21) at S = 35; "2793 of 3067" | Enumeration | **All verified.** |
| Table B1 (83 triads and their R) | Enumeration | **Verified.** |
| Thm 5.16: rank 0, torsion of order 12, positive points | Own full 2-descent (PARI was not available), plus a point search | **Verified**; details below the table. |

Details for Thms 5.12–5.14 and Prop. 5.15:
- The only collision with S ≤ 18 is (2,8,8)/(3,3,12).
- Endpoint tangencies occur only at (p,S) = (2,18) and (4,20).
- The collision-free sums with 18 ≤ S ≤ 1000 are exactly the 38 listed, the largest being 557.

Details for Thm 5.16:
- The model Y² = X³+393X²+3456X = X(X+9)(X+384) has full 2-torsion.
- **Full 2-descent:** the 2-Selmer group has order 4 = \|E[2]\|, with classes (1,1), (6,1), (−1,−15), (−6,−15). So the rank is 0 unconditionally.
- (−24, 360) lies on E.
- 6 base points plus 6 positive points make 12, consistent with torsion of order 12.
- A search of C_{27/2} up to 120 finds only (1:4:4), (1:1:4) and their permutations.

**Section 8: arithmetic of collisions**

| Item | What I did | Result |
|---|---|---|
| Prop. 8.2 discriminant | Symbolic computation | 2^{12}Λ²(Λ−9)(Λ−1)³, and the shift to the BGN model. **Verified.** |
| Thm 8.9: P = (4:9:18) lies on C_{155/12}, and nP ≠ O for n ≤ 12 | Exact chord-and-tangent with base point (1:−1:0) | **Verified.** **But** the stated "3P = (162833463 : 287876366 : 723926268)" is wrong as written. I obtain 3P = (162833463 : 723926268 : 287876366); the printed triple is a coordinate permutation, which is a different point (see m1). |
| Table 4 | Exact computation | Sums, R and Λ **verified** for all four classes. |
| Table 5 up to S = 600: N = 3067, N_cl = 2977, 1714 primitive, largest class 4 | Enumeration | **Verified** at all checkpoints ≤ 600. |
| Thm 8.7 constant c_iso = 3 log 2/(2π²); Appendix A constant 3/(128π⁴) | Re-derived | **Verified.** |

**Sections 6–7: stability and computed spectra**

| Item | What I did | Result |
|---|---|---|
| Prop. 6.2: rows of F^{−1} and amp_0…amp_4 = 2, 14, 498, 4062, 56230/3 | Exact computation | **Verified.** |
| Lemma 6.3, Thm 6.4, Lemma 6.5, Thm 6.6, Thm 6.9 | Read the proofs. Checked that the third term of δ_thm makes r_a ≤ 1/2 | **Correct** as far as I checked (Rouché constants, Hadamard step). I did not recompute Table 2. |
| Prop. 6.7(i): the changes for (2,8,8) | Exact computation | **Correct**, but printed in two different forms (m10). |
| Section 7: predicted d_3, d_4, d_5 | Exact computation | d_3 = 25/12, d_4 = −1775/24, d_5 = 153025/48. **Verified.** |
| Table 3: exact c_3 values −3.3354167 and −5.41875 | Exact computation | Both estimates lie within their error bars. **Consistent.** |
| Figure 1 caption: value 1 − t/3 off the cone points, m at a cone point | Analytic check | **Correct.** |

**Net.** I found no mathematical error in the main theorems. The only computational misstatement I found is m1.

## 4. MAJOR issues

**M1. Novelty is overstated in Section 4 and for Theorem A, and the headline structure misrepresents what is new.**
- *Location:* Theorem 1.2, Theorem 4.1, Cor. 4.5, Thms 4.9–4.11; §1.1 on Theorem A ("What is new here is the complex case …").
- *Problem:*
  - Theorem 1.2(i)–(ii) follows immediately from Uçar's Theorem 4.20, and for surfaces from McKean 1972.
  - Theorems 4.9–4.10 are the standard Selberg-trace-formula mechanism behind Huber's theorem.
  - Presenting these as one of four main theorems ("Heat does not hear the shape") inflates the contribution.
  - Theorem A is the classical fact that odd power sums determine a multiset up to ± pairs, with p_{2n−1} replaced by R.
- *Resolution:*
  - Demote Theorem 1.2 to a proposition or remark, attributed to [8] and McKean.
  - Cite the standard trace-formula argument for the exponentially small difference.
  - State and cite the classical odd-power-sum fact, and rephrase what is new in Theorem A.
  - Keep in the introduction only Theorems 1.1, 1.3, B, and possibly the sharpness statements of C.

**M2. The load-bearing input (Lemma 2.5 for all l) rests on an unpublished thesis, and the paper wrongly dismisses its own trace-formula route as not independent.**
- *Location:* Prop. 2.4, Lemma 2.5, Lemma 2.10, Remark 4.12 ("this is a cross-check … not an independent proof").
- *Problem:* All of Section 3 (Thms A, 3.6, 3.10, Cor. 3.7) needs three facts for *every* l: p_l has degree exactly 2l+2, its leading coefficient is nonzero, and p_l(1) = 0.
  - These come only from formula (4) of Uçar's PhD thesis [8, (4.25)], which has not been refereed as a journal article.
  - I confirmed the formula independently through l = 8 by expanding the elliptic term of Theorem 4.6, with agreement to 40 digits. So I believe it is correct. But a JGA paper should not rest on an unrefereed formula for all l without proof.
  - The authors already have the tools for a self-contained proof. The coefficient of t^l in E_m(t) is an explicit finite sum Σ_j csc(πj/m)·(d/da)^{2i}[csc(a/2)/2] evaluated at a = 2πj/m.
  - Remark 4.12 says this route is "not independent" because Lemma 4.7 uses the leading Weyl term of [3]. That does not follow: using a Weyl-type bound to justify convergence is not circular for the *values* of the coefficients.
  - The paper also relies on [3, Thm 4.8, Def. 4.7] but neither cites nor discusses the 2017 erratum to [3] (Michigan Math. J. 66 (2017) 221–222).
- *Resolution:*
  - Give a self-contained proof of Lemma 2.5 from the elliptic term of the trace formula: polynomiality in m, parity, degree, leading coefficient, and vanishing at m = 1. Keep [8] as corroboration. A polynomial-identity argument for the finite cosecant sums (e.g. Berndt–Yeap [25] or generating functions) should suffice.
  - Correct Remark 4.12.
  - Cite the erratum to [3] and state that it does not affect the results used.

**M3. Scope, length and proof standards: computational claims are stated as theorems, and some proofs sit outside the paper.**
- *Location:* Remark 2.12 ("The proofs are in the repository"); the last sentence of Thm 5.13 (38 collision-free sums up to 4800); Thm 3.10 / Remark 3.11 "each shares exactly"; the Section 8 counts; Sections 6.5 and 7.
- *Problem:* The manuscript is 56 pages.
  - Roughly a third (Sections 5.4, 8, Appendix A) is the arithmetic of the cubic (X+Y+Z)(XY+YZ+ZX) = ΛXYZ. Another substantial part (Sections 6.5, 7) is numerical illustration. Neither is geometric analysis.
  - Remark 2.12 states new results (determination by any tail, the Borel radius) whose proofs are not in the paper.
  - Theorem 5.13 includes a statement ("exactly 38 … largest 557" up to 4800) that is purely the output of an enumeration. I checked it to S = 1000.
  - The Section 7.1 spectra were computed with a solver that the authors themselves found can miss eigenvalues, and the planned recomputation "has not yet been run" (Section 7.1 Limitations, Appendix C).
- *Resolution:*
  - Remove Remark 2.12, or include its proofs.
  - Move enumeration-only statements out of theorem environments into clearly labelled computational results, and describe the algorithm in the paper.
  - Run the announced recomputation before resubmission.
  - Strongly consider splitting the paper into two:
    - a spectral-geometry paper (Sections 2–5 with a condensed Section 6), suitable for JGA;
    - a separate number-theory note on two-coefficient collisions (Sections 5.4, 8, Appendix A, Tables 4–5), which fits a number-theory or experimental-mathematics venue.

**M4. The stability claims in the abstract and in Theorem 1.4 overstate the sharpness and the spectral meaning.**
- *Location:* the abstract ("Hölder of exponent 1/k at k-fold orders, and both rates are sharp"); Theorem 1.4; Prop. 6.7(ii); Remark 6.8; Remark 6.1.
- *Problem:*
  - For k ≥ 3, sharpness of the exponent 1/k is shown only for arbitrary data vectors produced by polynomials with complex roots (Prop. 6.7(ii)).
  - For data that are actual heat invariants of real multisets near a triple order, the exponent is 1/2 (Remark 6.8). For mixed clusters nothing is claimed.
  - More fundamentally, the error model is on the c_j. The paper concedes (Remark 6.1) that there is no rigorous link from spectral data (eigenvalues) to errors in the c_j.
  - In a spectral-geometry journal, readers will take "approximate coefficients" to mean "approximate spectral data", and the paper gives no theorem of that kind.
- *Resolution:*
  - State in the abstract and in Theorem 1.4 that sharpness of 1/k refers to arbitrary perturbations of the invariant vector, and that realizable perturbations at a triple order give exponent 1/2.
  - Then do one of two things:
    - prove a quantitative statement from finitely many eigenvalues, with explicit tail control, down to the c_j (even under an assumed Weyl-remainder bound); or
    - reframe Section 6 explicitly as conditioning of the algebraic inverse problem, and shorten it.

## 5. MINOR issues

- **m1 (Section 8.3, after Thm 8.9).**
  - *Problem:* "3P = (162833463 : 287876366 : 723926268)" is wrong as printed. With base point O = (1:−1:0) and P = (4:9:18) on C_{155/12}, exact chord-and-tangent gives 3P = (162833463 : 723926268 : 287876366). The printed triple lies on the curve but is a different point: a coordinate permutation of 3P.
  - *Resolution:* correct the coordinates, or say "up to permutation".
- **m2 (proof of Prop. 5.2).**
  - *Problem:* the proof reads "the denominator is nonzero by Proposition 5.1 (equality there would need p=q=r, and then S_1R = 9 ≠ 1)". This is roundabout: S_1R ≥ 9 > 1 settles it directly.
  - *Resolution:* replace the parenthetical with that one-line argument.
- **m3 (Theorem 1.2(iii) / Thm 4.9(b)).**
  - *Problem:* "C is explicit", but the constant πe^{3δ}ℓe^{ℓ/2}/(A(1−e^{−ℓ})) depends on the diameter δ. The diameter is neither spectral nor a function of the signature.
  - *Resolution:* say so in Theorem 1.2.
- **m4 (§1.1, "it answers the question left open in [3, Rem. 5.16]").**
  - *Problem:* as quoted, DGGW say only that c "does not seem sufficiently strong to distinguish among" the hyperbolic pillows. The paper shows that c distinguishes exactly the pillows with p+q+r ≤ 17 and fails beyond. That precisely answers one reading of the remark, but it is not "the" open question.
  - *Resolution:* tone the claim down and quote the remark in full.
- **m5 (Theorem 1.1(ii), Cor. 3.12).**
  - *Problem:* the lower bound is logarithmic and the upper bound is linear in Area. The phrase "no fixed number of coefficients suffices" is right, but the log/linear gap appears only in Problem 1.
  - *Resolution:* state the gap explicitly in the introduction.
- **m6 (the [3] erratum).**
  - *Problem:* the erratum to [3] is neither cited nor discussed.
  - *Resolution:* cite and discuss DGGW, *Erratum*, Michigan Math. J. 66 (2017) 221–222 (see M2).
- **m7 (Lemma 4.7).**
  - *Problem:* the lemma quotes "uniform exponential type" from [6] but checks no decay hypothesis.
  - *Resolution:* state the exact class of test functions for which [6, eq. (1)] is proved (evenness, holomorphy in a strip, decay), and verify each hypothesis for h_ϱ.
- **m8 (Theorem 3.10(a)).**
  - *Problem:* the entries of the construction are astronomically large; I computed a minimum entry of about 1.6·10^8 already at L = 3. The area bound 2π(4^{L−1}−1) is fine, but the reader is not told this.
  - *Resolution:* add a remark that these orbifolds have enormous cone orders.
- **m9 (Section 7.1).**
  - *Problem:* the claim that the fit window and degree were chosen "without reference to the prediction" is informal.
  - *Resolution:* either document the protocol in the paper or drop the σ-comparisons.
- **m10 (Prop. 6.7(i)).**
  - *Problem:* δR is printed as 2s²/(8(64−s²)) in the statement and as s²/(4(64−s²)) in the proof. The two are equal.
  - *Resolution:* use one form throughout.
- **m11 (Prop. 4.4).**
  - *Problem:* the proof via Thurston's coordinates and invariance of domain is heavier than needed.
  - *Resolution:* use the short argument instead. Teich(O) has positive dimension and the modular group acts with countable orbits, so the moduli space is uncountable.
- **m12 (Remark 3.3).**
  - *Problem:* "In is injective there [on the diagonals]" does not say where this is proved. The sign convention of the Jacobian formula is also not aligned with Theorem B.
  - *Resolution:* point to Theorem A explicitly, and state the Jacobian formula with a sign convention consistent with Theorem B's ς_n.

## 6. Presentation

- **p1 (introduction and overall structure).**
  - *Problem:* the four "main theorems" of the introduction, Theorems A, B and C, and the numbered theorems in Sections 3–8 together make the logical structure hard to follow.
  - *Resolution:* add a single table mapping each statement in the introduction to the section result that proves it.
- **p2 (notation throughout).**
  - *Problem:* the notation load is heavy: c_j, Φ_j, C_l, Ψ_k and I_n; K_iso and K_mult. In particular, P_n (a class of orbifolds) clashes with P_k (a power sum).
  - *Resolution:* rename the class.
- **p3 (§6.2, definition of t_k(n)).**
  - *Problem:* several displayed formulas lose their structure in the PDF text layer, for example "artanh(w) sec²(n+1) artanh w".
  - *Resolution:* parenthesize it as artanh(w)·sec²((n+1) artanh w).
- **p4 (Figures 1, 3, 7, 8(b)).**
  - *Problem:* Figures 3, 7 and 8(b) carry information that is largely arithmetic.
  - *Resolution:* cut them if the paper is split (M3). Figure 1 is attractive and can stay; its caption already says the rendering is stylised.
- **p5 (Remark 2.12).**
  - *Problem:* "genus 10^4" renders ambiguously in the text layer as "genus 104".
  - *Resolution:* typeset it as 10^{4}.
- **p6 (Section 1.1).**
  - *Problem:* Section 4 is claimed as new without the classical background.
  - *Resolution:* cite McKean (1972) and add a short paragraph on the classical Selberg-trace-formula picture before claiming Section 4.
- **p7 (throughout).**
  - *Problem:* the paper repeatedly says "to our knowledge, the first…".
  - *Resolution:* remove or justify each such statement once the novelty claims are corrected.

## 7. Recommendation

**Major revision.** Confidence: **medium-high.**

The mathematics I checked is correct, and I could independently recompute and confirm an unusually large share of it. This includes:
- the cone coefficients through t^8, via the trace formula;
- Theorem B;
- the threshold 17/18;
- Tables 1, B1 and 5 (to S = 600);
- the rank-0 result, by my own full 2-descent.

The genuinely new spectral content is nice but moderate: the uniform ⌊Area/π⌋+4 bound and its unboundedness, the triangle threshold and its isolation, and Theorem B. It sits in a 56-page manuscript that:
- presents known trace-formula facts as headline theorems (M1);
- rests its key lemma on an unpublished thesis while dismissing its own independent route (M2);
- mixes in substantial number theory, numerics and repository-only proofs (M3);
- overstates the sharpness of the stability results (M4).

In my view, a focused, self-contained spectral-geometry paper of perhaps 25–30 pages, with the arithmetic split off, would be publishable in JGA.

---

*Saved by the coordinating session: this subagent could not write files, so the report came back as text and was saved verbatim. The coordinator removed only the hand-back note addressed to itself, and shortened the absolute path of the scratch folder.*
