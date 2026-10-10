<!-- Saved verbatim by the main session from the final message of reviewer A-c: the harness refused the reviewer's own write. Text from the report's first heading on; the reviewer's preceding cover note was dropped. -->
# Referee report: "How much of a hyperbolic orbifold does heat hear?" (Annals of Global Analysis and Geometry)

**Remit of this report.** I cover Section 3 in full:
- §3.1, the moment problem (Lemma 3.1, Theorems A–C, Remark 3.2);
- §3.2, heat data of a signature (Lemma 3.3, Theorem 3.4, Corollary 3.5, Example 3.6);
- §3.3, bounded cone orders (Lemma 3.7, Theorem 3.8, Corollary 3.9);
- §3.4, the Prouhet–Tarry–Escott section (Definition 3.10 to Remark 3.18, including Theorem 3.14 and Proposition 3.15);
- Theorem 1.1 and Theorems 1.2–1.3 as stated in the introduction;
- Appendix A;
- the supplement material that Section 3 relies on (Section S1, Table S1, Section S8).

I read the rendered pages (manuscript pp. 1–5, 14–25 and 36–38; supplement pp. 1–6) as well as the extracted text. Sections 2 and 4–6 are outside my remit. I used the formulas of Section 2 (eqs. (5), (7), (8), Lemma 2.10) only as inputs to my own computations.

---

## Summary

Section 3 turns "do two hyperbolic 2-orbifolds share their first L heat invariants?" into a moment problem. The question becomes whether the signed multiset Z = U* ⊎ (−V*) has:
- zero reciprocal sum, and
- zero odd power sums up to exponent 2L−3.

Z is formed from the cone orders, padded by entries 1. A single parity fact runs through the section: a configuration with vanishing low odd moments and |Z| ≤ 2L is symmetric. This is Newton's identities plus e_{κ−1} = e_κ Σ 1/z. From it the authors derive the following.
1. **Theorems A and B.** Recovery of n cone orders on a sphere from (R, P_1, …, P_{2n−3}), with the determinant ±∏(m_i+m_j)/∏m_i.
2. **Theorem C.** Sharpness of that recovery.
3. **Theorem 3.4.** A separation bound |U*|+|V*| ≥ 2L+2.
4. **Corollary 3.5.** The area bound ⌊A/π⌋+4.
5. **Theorem 3.8.** The exact, area-free answer M+1 for orders at most M. The proof combines:
   - a Vandermonde/Lagrange-weight construction;
   - a sign-change (Descartes-type) argument applied to the measure Σ±x^{−1}δ_{x²}.
6. **Theorem 3.11.** A Descartes bound on the imbalance, which prices a change of genus.
7. **Theorem 3.14 and Proposition 3.15.** The growth of f(A) is identified, up to constants, with the inverse of the least size T(L) of an "L-configuration". T(L) is in turn sandwiched as N(2L−2) ≤ T(L) ≤ 4N(2L−3), where N is the Prouhet–Tarry–Escott function. So f(A) ≥ cA^α holds exactly when N(k) = O(k^{1/α}).

The constructions use:
- the pigeonhole principle (Lemma A.1);
- shifting a PTE solution to create an imbalance (Proposition A.2);
- a doubling trick (Proposition 3.12);
- the combination of two pieces with opposite reciprocal sums (Lemma 3.16).

## Significance

What is good, stated plainly:
- **Theorem 3.8 is a genuinely nice result.** It is exact, area-free and attained. Part (iii) gives a uniform bound min(M+1, 2d_O+2, ⌊A/π⌋+4) by a clean sign-change argument. Part (iv) shows it is sharp for every M ≥ 2 with explicit pairs.
- **Theorem B and Theorem 3.11 are elegant.** Theorem B identifies the conditioning of the linear recovery with Orlando's form of a Hurwitz determinant. Theorem 3.11 is a Descartes argument that prices a genus change.
- **The relocation of the growth question is honest and correct (Proposition 3.15).** It moves the question to the PTE function N(k) without overclaiming, and the authors say clearly that nothing about N is settled.
- **The upper bounds on T(4..7) are well done.** They rest on explicit pairs, and the recipes in Table S1 reproduce exactly (see below).

Novelty is modest. Each step uses classical tools: Newton's identities, Lagrange interpolation weights, Descartes' rule, pigeonhole and Prouhet-type shifts. The equivalence with N(k) = O(k) relocates an open problem rather than making progress on it. The two-sided sandwich of T(L) between values of N is new to me, and so are the realisation of every configuration by an orbifold pair and the exact M+1. As a contribution to the inverse spectral theory of orbifolds, Section 3 is a solid and correct piece of work.

## Correctness and what was recomputed

All computations used exact integer or rational arithmetic, in my own scripts written from scratch in a scratch folder. I used:
- the cone polynomials p_l built from (4)–(5);
- the coefficients α_k of Proposition 2.7;
- c_j from (7).

My code reproduces (8) (p_0, p_1, p_2), α_0..α_4 = 1, −1/3, 1/15, −4/315, 1/315, and the leading coefficients |B_{2l+2}|/(2(l+1)!(2l+1)) of Lemma 2.8 for l ≤ 4. It also reproduces c_1, c_2, c_3 of (10) for O(2,8,8) and O(3,3,12).

**Theorem B.** I built the system (12) literally, from the series of tanh(Σ_{k odd} P_k z^k/k), with the equations ordered as printed.
- The true e solves it.
- det M = (−1)^{n(n+1)/2} ∏_{i<j}(m_i+m_j)/∏m_i, sign ς_n included.
- Tested for n = 2, 3, 4, 5, on random rational and repeated multisets with mixed signs.
- Correct.

**Proofs read line by line.**
- Lemma 3.1, Theorem A (including the multiplicity argument), Theorem C(1)–(2), Lemma 3.3 (including d, the paddings, (14) and |U|+|V| = 2max(…)), Theorem 3.4 and Corollary 3.5: all correct.
- Lemma 3.7 and Theorem 3.8(i)–(iv): correct, including the Lagrange-weight identities, the c_M and c_{M+1} differences, and the sign of w_X.
- Corollary 3.9, Theorem 3.11, Proposition 3.12 (including the j = −1 case, the hyperbolicity and the distinctness via 2x*) and Theorem 3.13: correct.
- Lemma 3.16, Lemma A.1, Proposition A.2 and the proofs of Theorem 3.14(a)–(d): correct.
- Proposition 3.15: correct.

I checked that the "equivalent to" claims are genuine equivalences with the quantifiers right:
- **Theorem 3.14(d) and Theorem 1.1(ii)** compare "f(A) ≥ cA^α for all large A, for some c" with "N(k) ≤ Ck^{1/α} for all k, for some C". This is a correct two-way implication.
- **f = Θ(A) ⇔ N(k) = O(k)** is correct.
- **f(A) = o(A) ⇔ N(k)/k → ∞** is also correct. It does not follow by negating the previous equivalence. It needs the inverse relation between f and A_min together with π/2(T−8) ≤ A_min < 2πT and the monotonicity of N and of A_min. I checked that argument; see m2.

**Theorem 3.8(ii), (iv) and the numbers after it.** For M = 2, …, 9 I recomputed the Lagrange weights, the least C, ν(a), s and the least g.
- I confirm (ν(2), ν(3)) = (−16, 9), s = −2, giving (1; 3⁹) against (0; 2¹⁶), area 12π.
- I confirm (28, −27, 8) for M = 4, giving (0; 2²⁸, 4⁸) against (1; 3²⁷), area 36π.
- I confirm the full list of areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054}.
- For each M ≤ 9 the pair shares exactly c_1, …, c_{M−1}, and c_M differs by exactly (−1)^M C a_{M−2}.
- For (iv) I checked (M, X) = (2,4), (2,5), (3,5), (3,7), (4,6), (5,9). Each pair shares exactly c_1..c_M, the c_{M+1} difference equals (−1)^M C a_{M−1}, and X ∈ m′.
- For (M, X) = (2, 4) I reproduce the printed weights (1/45, −1/36, 1/180), C = 180, ν = (10, −4) and s = 2.
- I confirm the surface example (2; ) against (0; 2⁸), and (0; 2⁵) against (1; 2) sharing c_1.

**Minimality claim for M = 3, 4.** I ran an independent exhaustive search over all signatures with orders ≤ M below the stated area. There is no pair with orders ≤ 3 sharing c_1, c_2 with area < 12π. There is no pair with orders ≤ 4 sharing c_1, c_2, c_3 with area < 36π. At those areas the printed pairs are the only ones. Confirmed.

**Brute-force test of Theorem 3.8(iii) and Theorem 3.11.**
- Search space: all signatures of genus ≤ 2 with ≤ 6 cone points of orders 2..24.
- Equal-area pairs agreeing in Ψ_1, Ψ_2: 149 pairs, each sharing exactly 3 invariants; none shares 4.
- None violates L ≤ min(M, 2d+1) on either side.
- None violates |U*|+|V*| ≥ max(2L+2, 2L+2|g−g′|).

**Theorem C(3), Remark 3.2 and the literature claims about Chen's survey.**
- I recomputed R, P_1, P_3, P_5 for {2,8,8}/{3,3,12} and {3,10,15,30}/{4,5,21,28}. All printed values are correct.
- Q(z) − Q(−z) = 2κz³ with κ = −772200, consistent with Chen's C = 772200 for (A.685).
- My exhaustive search of 4-multisets with orders in [2, 84] finds 9 witnesses, 8 of them primitive, and no triple collisions. The 8 primitive ones are exactly (A.685)–(A.692) of Chen's §A.5.8 (arXiv:2506.11429v1), which I fetched and read. Allowing entries 1 changes nothing up to 84.
- The following attributions to Chen are correct: Identity 9 with m = 3, eqs. (3.27)–(3.28), as the forward direction of Theorem C(1); (3.33) for type (−1,1,3,5); §8.1 P1 ("ideal solutions of degrees n = 10 and n ≥ 12"); A.1.6 ([1,5,5] = [2,3,6] is (A.48)); A.1.17 (A.178); A.1.26 (A.266); A.1.33 (A.313–A.315).
- One attribution is imprecise; see m6.

**Table S1 and Example 3.17.** I parsed every pair printed in Table S1 (genus pairs, equal-count pairs and cone-count pairs for L = 2..7; Prouhet pairs for L = 2, 3) and recomputed c_1, …, c_{L+2} exactly.
- Every pair shares exactly the stated L.
- Areas agree, and the printed exact values of s agree.
- |U*|+|V*| = 14, 18, 24, 40 for the equal-count pairs and 16, 20, 26, 40 for the genus pairs, as stated in Example 3.17(iii).
- The areas lie just below 2π·{5, 7, 10, 18}.
- Example 3.17(i)–(ii), Example 3.6 and the f_n example (0;5,5,5)/(0;2,2,2,10) are correct.

**Lemma 3.16 recipes.** I rebuilt the following pairs from the recipes in S1 (shift, τ = −ϱ(B)/ϱ(P), cancel pairs, scale to coprime integers, realise):
- the L = 4 and L = 5 genus pairs;
- the L = 4, 5, 6 equal-count pairs.

They agree digit for digit with Table S1. The upper-bound row of the T(L) table (6, 8, 14, 18, 24, 40) is therefore fully substantiated. The lower-bound row 2L+2 is Theorem 3.4.

**Remark 3.18.**
- The cubic q_V = z³ − e_1z² + Re_3z − e_3 with e_3 = (P_3 − e_1³)/(3(1 − e_1R)) follows correctly from Newton's identities. The denominator never vanishes, because e_1R ≥ 25 by AM–HM.
- The real partner of {1,1,1,1,7} is {0.26636, 4.28304, 6.45060}, as printed.
- I ran an independent search, much smaller than the authors' bound of 220, over all 3,026,663 five-multisets V with gcd 1 and entries ≤ 50. It used a different filter: a root modulo 12 primes above 50, followed by exact factorisation of the 28,997 survivors. It finds no V with three positive rational partners. This is consistent with the authors' claim.

**Literature on N(k).**
- The bounds k+1 ≤ N(k) ≤ ½k(k+1)+1 are correct.
- So are Wright's slightly better quadratic bound, the absence of any known o(k²) bound, and ideal solutions being known exactly for k ≤ 9 and k = 11. These agree with the secondary literature I could access.
- Hua's k² log k-type bounds concern Tarry's exact-degree variant and do not bear on N; the paper correctly does not cite them.
- I could not obtain the text of Borwein–Ingalls [3] (L'Enseignement Math. 40, 1994). The pinpoints "Props. 2–3", "§2, p. 6", "p. 7", "Problem 3 of §6", "pp. 9, 25" and the quoted phrase "has been made for many years" are therefore unverified by me (m7).

**Conclusion of the checks.** I found no mathematical error in Section 3 or Appendix A. The issues below are a misstatement in the abstract and gaps in exposition.

---

## MAJOR issues

**M1. The abstract misstates the main growth theorem (p. 1, Abstract).** This is a genuine misstatement, though not an error in any theorem. The abstract says f "grows … like a power A^α of the area exactly when the Prouhet–Tarry–Escott function satisfies N(k) = O(k^{1/α})".
- **What the paper proves.** Theorem 1.1(ii) and Theorem 3.14(d) prove only the one-sided statement: f(A) ≥ cA^α for large A ⇔ N(k) ≤ Ck^{1/α}.
- **Why the natural reading is false.** "Grows like A^α" naturally means f ≍ A^α. Under that reading the statement is false as written, or at least asserts something open. With α = ½, N(k) = O(k²) is known, so the abstract would assert f(A) ≍ √A. That contradicts the paper's own sentence "Whether f grows like a power of A at all is open" (p. 3).
- **A second inconsistency.** N(k) = O(k^{1/α}) also holds for every α < ½. The abstract would then assert that f grows like A^α for all those α simultaneously.
- **Why it matters.** The abstract is what most readers will quote, and here it states something stronger than what is proved.
- **The fix is one word**, e.g. "at least like a power A^α exactly when N(k) = O(k^{1/α})". The authors could also add the converse half: "and at most like A^α when N(k) ≥ ck^{1/α}".
- **Same imprecision on p. 5.** The sentence on p. 5, "Theorem 1.1 makes the growth question equivalent to an open problem", should say which growth question: linear growth, or lower power bounds.

I have no further major issues within my remit.

## MINOR issues

**m1. Proof of Theorem 3.11 (p. 21): a gap in exposition.**
- **What the count needs.** The count "at most (κ−2L)/2 coefficients of odd degree are nonzero" needs κ − 1 > 2L − 3. Otherwise e_{κ−1} is one of the e_k already counted, and the count is off by one.
- **Where that comes from.** κ ≥ 2L+2 follows from the "short configuration is symmetric" step of Theorem 3.4. But Theorem 3.4 is stated for orbifold pairs, not for arbitrary L-configurations (rational, with no pair {z,−z}).
- **Requested fix.** State the configuration version explicitly, either as a lemma after Definition 3.10 or as a line in the proof: every L-configuration has |Z| ≥ 2L+2.
- **Same issue elsewhere.** The lower bound T(L) ≥ 2L+2 in Proposition 3.15 and the table on p. 23 rely on the same point.

**m2. "f(A) = o(A) iff N(k)/k → ∞" (Theorem 1.1(ii), p. 3; Proposition 3.15, p. 22): a gap in exposition.**
- **The problem.** This is introduced with "in particular" after one-sided implications. Logically it does not follow from "f ≥ cA^α ⇔ N = O(k^{1/α})" plus "N ≥ ck^{1/α} ⇒ f = O(A^α)": negating the first gives "liminf f/A = 0 ⇔ limsup N/k = ∞", not o(A) ⇔ N/k → ∞.
- **Why it is nevertheless true.** It does follow from:
  - the full sandwich π/2(T(L)−8) ≤ A_min(L) < 2πT(L);
  - A_min(f(A)−1) ≤ A;
  - f(A) ≥ L+1 for A > A_min(L);
  - N(2L−2) ≤ T(L) ≤ 4N(2L−3) ≤ 4N(2L−2);
  - the monotonicity of N and of A_min.
- **Requested fix.** Please write out these three or four lines.

**m3. Proof of Theorem 3.14(c), p. 38: "(also when every entry of W is 1 and g_0 = 2)" is vacuous.**
- **Why.** If every entry of W is 1, then |W| − R(W) = 0. Equal area then forces the other side, of genus g_0 + |ι|/2 ≥ 3, to have |V| − R(V) = 4 − 2g′ < 0, which is impossible.
- **Consequence.** Either drop the parenthesis or say the case cannot occur. The same remark applies to "also when every entry of W is 1" in the proof of Proposition 3.15 (p. 23).

**m4. Theorem 3.13, statement (p. 21).** "The smaller of which can be any prescribed integer g ≥ 2 (the pairs constructed have smaller genus at most 2 …)" reads oddly.
- **What is proved.** For every g ≥ 2 there is a pair whose smaller genus is g.
- **What a reader may infer.** That g = 0, 1 are impossible, which is not claimed. Please rephrase.
- **Related request.** Say whether genus-changing pairs with smaller genus 0 exist for every L. The construction of Theorem 3.14(c) seems to give smaller genus 0 whenever |W| − R(W) > 2, which is the generic case.

**m5. Definition of a witness (Remark 3.2, p. 16, and Section S1).** A witness is defined as a pair of n-multisets of positive integers, but the searches run over orders in [2, 440].
- **Why it matters.** A pair containing an entry 1 would correspond to spheres with different numbers of cone points.
- **Requested fix.** Define a witness with entries ≥ 2, or say that 1 is allowed and treated as padding.
- **My check.** Allowing 1 changes nothing up to 84.

**m6. Attribution on p. 23.** "Equal sums of odd powers from [30, A.1.17, A.1.26, A.1.33], the last found by Wróblewski in 2009 according to that survey."
- **What the survey says.** Within A.1.33, the solution [7,91,173,269,289,323] = [29,59,193,247,311,313] is (A.313). Chen's survey (p. 64) attributes it to Chen in 2000. Only (A.314)–(A.316) are attributed to Wróblewski, 2009.
- **Why it matters here.** Table S1 uses (A.313) as the B-piece of the L = 6 genus pair, and (A.314)/(A.315) for the L = 6 equal-count pair.
- **Requested fix.** Please make the attribution precise and cite equation numbers rather than section numbers.

**m7. Borwein–Ingalls pinpoints (pp. 3, 6, 21–22).** I could not access [3] to check the following:
- "§2, p. 6" (definition of N);
- "Props. 2–3" (k+1 ≤ N(k) ≤ ½k(k+1)+1);
- "p. 7" (Wright, Melzak);
- "Problem 3 of §6" and the quotation "has been made for many years";
- "pp. 9, 25" (Letac, Gloden);
- "Prop. 3" in the proof of Theorem 3.13.

The mathematical content quoted agrees with the secondary literature. Please re-verify each pinpoint and the exact wording of the quotation against the published pages.

**m8. Theorem 3.8(ii) (p. 18).** It would help to say why s is an integer once ν(a) is: s = Σν(a) + C·w_1, since Σ_a w_a = 0. "Least positive integer C for which … s is an even integer" then makes clear what is being required. Currently a reader has to rederive this to see that C exists and to reproduce the printed values (which I did).

**m9. Section 3.4, the converse realisation (p. 20): a gap in exposition.** "With U = Z_{>0}, V = −Z_{<0} and all entries 1 removed, signatures (g;U) and (g′;V)." The 1s are removed from the signatures but must be kept as paddings when Lemma 3.3 is applied. Please write (g; U∖{1}) and (g′; V∖{1}), and say that U, V are the paddings. Proposition 3.12 does exactly this.

**m10. Unclear sentence (p. 23).** "Those of size 10 built from two odd symmetric 5-sets with equal e_4, e_5 do not exist with entries at most 200." It is not clear what an "odd symmetric 5-set" is, which construction is meant, or why equal e_4, e_5 is the relevant condition.
- **Requested fix.** Please define these terms or drop the sentence.
- **Classification.** It is a search statement and should also be listed in S8 among "statements that rest on computer search alone". At present it is not listed there.

**m11. Theorem 3.14(b) (p. 22).** The bound ½(A/6πC)^{1/β} uses N(2L−3) ≤ C(2L−3)^β ≤ C(2L)^β, which tacitly needs β > 0 (stated) and C ≥ 1 (true, since N(1) = 2). It also needs "for all k ≥ 1" to include k = 2L−3. That is fine, but a half-line would remove any doubt.

## Presentation

These concern figures, captions, notation and exposition, not length.

- **Figure 2 (p. 18).** I checked it against the rendered page. Discs at X* = {2,8,8,−3,−3,−12} and rings at −X* in (a); X* = {1,15,−3,−3,−5,−5} in (b). The figure matches the text and illustrates the mirror argument well. The caption could say that stacked markers denote multiplicity.
- **Figure 3 (p. 24).**
  - The figure is informative.
  - The dashed curve "from s = 4 on" corresponds to A ≥ 8π, as in Theorem 3.14(a); saying so in the caption would help.
  - The legend lives only in the running text. Please put the meaning of the dots, diamonds, squares and the split disc in the caption.
- **Notation clash.** In Theorem 3.8 the letter a is a node or cone order, while a_l (a_{M−2}, a_{M−1}) is the leading coefficient of p_l (Lemma 2.8). On p. 19, "Σ_a w_a p_{M−2}(a) = (−1)^M C a_{M−2}" is genuinely confusing on first reading. Please rename one of them; for example, call the leading coefficient λ_l.
- **Unused notation.** Table 1 lists T(L) and ι, but not T_g(L), A_min(L), f_g or f_n, which recur in §3.4 and Problem 3. The pair ϱ (reciprocal sum, Lemma 3.16, A.2) versus R (reciprocal sum of orders) could also be unified or listed.
- **Mid-section definitions.** f_g and f_n are defined in a paragraph between Theorem 3.13 and Theorem 3.14. Since Theorem 3.14(c)–(d) are stated for them, a displayed definition would be clearer.
- **Inconsistent use of "ideal".** The p. 23 definition ("An L-configuration of the least size 2L+2 allowed by Theorem 3.4 is ideal") should be reconciled with Problem 4's "balanced ideal (n−1)-configuration" and with Chen's use of "ideal" for type (−1,1,3,…).
- **Proposition 3.15.** Please state the inequality f(A) ≤ L for A < A_min(L) separately rather than inside "so that …" (p. 22). It is used essentially in m2.
- **Recovery map.** Theorem C(1)'s κ is the constant C of Chen's Identity 9 up to sign. Saying so would let a reader move directly between the two sources.

## Recommendation

**Minor revision** for the parts in my remit (Section 3, Appendix A, Theorem 1.1 and the supporting supplement material). Confidence: high.

- I verified every proof in Section 3 and Appendix A line by line.
- I recomputed exactly every numerical claim I could reach. That includes the constructions of Theorem 3.8 up to M = 9, all pairs printed in Table S1 and the recipes behind them, the eight primitive n = 4 witnesses, and a smaller-range reproduction of the size-8 genus-pair exclusion.
- I found no mathematical error.
- The one substantive point (M1) is a misstatement in the abstract. It must be corrected, but it does not affect any theorem.

## What resolves each issue

| Issue | What resolves it |
|---|---|
| M1 | Rephrase the abstract: "grows at least like A^α exactly when N(k) = O(k^{1/α})", optionally adding the converse half "and O(A^α) when N(k) ≥ ck^{1/α}". Make the p. 5 sentence name the precise growth question. |
| m1 | Add the statement "every L-configuration has \|Z\| ≥ 2L+2" (proof as in Theorem 3.4), and cite it in Theorem 3.11 and Proposition 3.15. |
| m2 | Write out the short argument for f = o(A) ⇔ N(k)/k → ∞ from the sandwich bounds and monotonicity. |
| m3 | Delete, or mark as impossible, the "every entry of W is 1 (and g_0 = 2)" case in the proofs of Theorem 3.14(c) and Proposition 3.15. |
| m4 | Rephrase Theorem 3.13 so that it says exactly what is constructed, and comment on smaller genus 0. |
| m5 | Define witnesses with entries ≥ 2, or state how 1s are treated. |
| m6 | Correct the attribution of (A.313) versus (A.314)–(A.316), and cite equation numbers. |
| m7 | Re-verify every Borwein–Ingalls pinpoint and the quotation against the printed paper. |
| m8 | Add one line explaining that s = Σν(a) + Cw_1, and hence why the least C exists. |
| m9 | Write (g; U∖{1}), (g′; V∖{1}) and refer to U, V as paddings. |
| m10 | Define the construction in the "size 10 … entries at most 200" sentence or remove it, and list it in S8 if kept. |
| m11 | Add a half-line to the proof of Theorem 3.14(b). |
| Presentation | Rename the leading coefficient a_l; extend Table 1; make the Figure 3 caption self-contained; display the definitions of f_g, f_n; reconcile "ideal". |

---

My scripts and page renders are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-5/A-c-pte-moment-problem/scratch/` (`code/`, `renders/`), and Chen's survey is in `scratch/lit/`.

Sources used for the literature checks:
- [Chen, A survey of the Prouhet–Tarry–Escott problem and its generalizations (arXiv:2506.11429)](https://arxiv.org/pdf/2506.11429)
- [Borwein–Lisoněk–Percival, Computational investigations of the PTE problem](https://www.ams.org/mcom/2003-72-244/S0025-5718-02-01504-1/)
- [The PTE problem for Gaussian integers (arXiv:1011.1262)](https://arxiv.org/pdf/1011.1262)
- [Caley thesis](https://uwspace.uwaterloo.ca/bitstream/10012/7205/1/Caley_Timothy.pdf)
- [MathWorld: Prouhet–Tarry–Escott problem](https://mathworld.wolfram.com/Prouhet-Tarry-EscottProblem.html)
