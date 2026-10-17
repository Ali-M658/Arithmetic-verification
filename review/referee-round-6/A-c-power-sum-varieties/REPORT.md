<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Referee report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

The tool refused to write `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/A-c-power-sum-varieties/REPORT.md`, so the complete report is below. My recomputation scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/A-c-power-sum-varieties/scratch/code/`.

Coverage: Section 3 in full (3.1 moment problem, 3.2 heat data of a signature, 3.3 bounded cone orders, 3.4 the Prouhet–Tarry–Escott connection), Appendix A, and Supplement S1–S2. I read the rest of the paper to see how Section 3 is used, and I checked the cone polynomials of Section 2.2–2.3 because every result in Section 3 depends on them through Lemma 2.10. Page numbers are those of the manuscript PDF. Before reporting any formula or figure item I looked at the rendered pages (pp. 3, 16–17, 20–22, 24–26 and 40, and supplement pp. 2–3).

## Summary

Section 3 reduces the question "how many heat invariants determine the signature" to the algebra of a signed multiset. Write U\*, V\* for the cone orders of the two orbifolds, padded by entries 1 and with common elements removed. Two orbifolds share c₁,…,c_L exactly when Z = U\* ⊎ (−V\*) has vanishing reciprocal sum and vanishing odd power sums up to degree 2L−3 (Lemma 2.10, Lemma 3.3). The section then proves the following.

- **Theorem A.** n odd power sums together with R recover n orders.
- **Theorem B.** The linear system for e₁,…,eₙ has determinant equal to a signed Hurwitz/Orlando form.
- **Theorem C.** This gives the fibre structure of n−1 invariants, with integer witnesses for n = 3, 4.
- **Theorem 3.4 (separation).** If the signatures differ, |U\*|+|V\*| ≥ 2L+2, which gives Corollary 3.5.
- **Theorem 3.8 (bounded orders).** With cone orders at most M, the answer is M within Sig≤M and M+1 against all of Sig, uniformly in the area. Both values are attained by explicit pairs built from Lagrange weights at the nodes a², and the proof uses a sign-change argument for moments.
- **Theorem 3.11 (Descartes bound).** A pair with a change of genus costs |ι| ≤ |Z| − 2L.
- **Proposition 3.12 (doubling), Theorem 3.13, Theorem 3.14 (growth) and Proposition 3.15.** Together these sandwich the least L-configuration size as N(2L−2) ≤ T(L) ≤ min(6(L−1)²+6, 4N(2L−3)). The consequences are √A-type lower bounds for f(A), and the statement that power-law lower growth of f is equivalent to a power-law upper bound on the Prouhet–Tarry–Escott function N(k).

Appendix A proves these bounds by pigeonhole and by shifting a PTE solution. Supplement S1–S2 contain the searches, the explicit pairs, the area classes of Figure 3, and the strata/triad data of Section 5.

## Significance

**What is good.**
- Section 3 is correct; I found no false statement among its theorems.
- It is written with unusual care about what is proved and what was found by computer.
- Every explicit pair I recomputed is right.
- The cleanest new mathematics:
  - The exact, area-free answer M+1 for bounded orders (Theorem 3.8). The Lagrange-weight construction of extremal pairs in (ii)/(iv) is elegant, and the sign-change argument in (iii) is the right proof.
  - The Descartes bound (Theorem 3.11) on genus-changing pairs.
  - The identification of the conditioning determinant of the recovery system with Orlando's form (Theorem B).
- The "What is elementary and what is not" paragraph (p. 5) is commendable.

**What limits the significance.**
- Mathematically, Section 3 is elementary algebra of power sums: Newton's identities, Vandermonde determinants, a classical sign-change lemma and Descartes' rule. The geometry enters only through the triangular structure of Lemma 2.10.
- Much of it is close to known PTE material:
  - "Odd symmetric systems" [3, §3].
  - Chen's Identity 9 is the forward direction of Theorem C(1).
  - Chen's 2017 search gives all eight primitive n = 4 witnesses with orders ≤ 84 (I checked (A.685)–(A.692) in arXiv:2506.11429).
  - Steinig's theorem is the model for Theorem A.
- The growth theory proves unconditionally only c√A ≤ f(A) ≤ A/π + 4.
- The equivalence with N(k) (Theorem 1.1(ii)) is correct but shallow. It is a two-sided sandwich obtained from two short constructions: Z, −Z is a PTE solution, and shift-and-combine. It relocates the question; it does not narrow the gap between √A and A. The authors say so ("without settling it", p. 6), but the paragraph on p. 5 still presents Theorem 1.1 as "the weight of the paper" (see M1).
- For AGAG, the value of Section 3 is that it makes the heat-invariant count completely explicit and gives exact answers in the bounded-order regime. The PTE "connection" is a reformulation, not progress on either side.

I confirmed against a 2026 source (Croot–Mao–Yip, arXiv:2609.05061, §1) that no bound N(k) = o(k²) is known; the best known bound is still k(k+1)/2 + 1. So the paper's statements about what is open are accurate.

## Correctness and what was recomputed

I re-derived every proof in my coverage line by line. All of my code is independent of the authors' deposit, which I did not open. Arithmetic is exact (Python `Fraction`/sympy, C with 64/128-bit integers).

**Cone polynomials (prerequisite for Lemma 2.10).**
- I computed pₗ from (4)–(5): σᵢ from the series of u/sin u, Bernoulli numbers, and the k-sum.
- p₀, p₁, p₂ agree with (8).
- p₃ agrees with the K³ term of Remark 2.12(b) after expansion.
- For l ≤ 11: pₗ(1) = 0, deg pₗ = 2l+2, and the leading coefficient is |B₂ₗ₊₂|/(2(l+1)!(2l+1)) (Lemma 2.8).
- α₀,…,α₄ = 1, −1/3, 1/15, −4/315, 1/315 as stated.

**Shared-invariant counts, done two ways.** For each pair I counted shared invariants directly from cₖ = αₖ₋₁·Area/4π + Σ bₖ₋₂(mᵢ), and separately via Lemma 3.3 (equal area plus Ψₖ). The two counts agreed in every case, and so do the authors' claims:
- Theorem C(3): {2,8,8}/{3,3,12} and {3,10,15,30}/{4,5,21,28}. R, P₁, P₃, P₅ are exactly as printed; they share exactly 2 and 3 invariants respectively.
- Theorem 1.2(ii): (0;2¹⁰)/(1;4⁴), area 6π, share exactly c₁, c₂.
- Example 3.6: (1;15)/(0;3,3,5,5), area 2π·14/15, Ψ₁ = 224/15, |U\*|+|V\*| = 6.
- Example 3.17(i)–(ii), including the doubling of [1,5,5] = [2,3,6].
- (0;5,5,5)/(0;2,2,2,10) share exactly 2 (p. 40); (2;)/(0;2⁸) share exactly 1 (p. 21).
- All 20 rows of Table S1 whose cone lists are printed. These are the genus, equal-count and cone-count pairs for L = 2,…,7, and the Prouhet rows L = 2, 3. In each, the areas are equal, the printed exact s agrees, and the shared count equals the stated L.
- The values |U\*|+|V\*| = 6, 8, 14, 18, 24, 40 (equal count) and 16, 20, 26, 40 (genus) confirm both rows of the table on p. 25.
- I also rebuilt the L = 4, 5 genus pairs and the L = 4, 5 equal-count pairs from the recipes of S1 via Lemma 3.16 (shift, scale by τ, delete ±pairs, scale to coprime integers). All four reproduce Table S1 exactly, and every piece has the stated vanishing odd power sums.

**Theorem 3.8.**
- I implemented the Lagrange-weight construction of (ii) for M = 2,…,9:
  - C = 6, 120, 2520, 362880, 19958400, …
  - (ν(2), ν(3)) = (−16, 9) for M = 3; (ν(2), ν(3), ν(4)) = (28, −27, 8) for M = 4.
  - The areas of the least-g pairs are 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054}, exactly as on p. 21.
  - For M ≤ 6 the pairs share exactly M−1 invariants.
- For (iv): (M, X) = (2, 4) gives (w₁, w₂, w₄) = (1/45, −1/36, 1/180), C = 180, ν = (10, −4), s = 2, and shared count 2. The cases (2, 3), (3, 5), (4, 7) give shared counts 2, 3, 4 = M.
- I re-proved (i)–(iv) by hand, including the run-counting in (iii). It is correct; the run containing the point 1 lies at the left end because 1 cannot be in both U\* and V\*.

**Theorem B.** I built M symbolically from (12) for random and repeated-order multisets, n = 2,…,6. In every case M solves for the true e, and det M = (−1)^{n(n+1)/2} ∏_{i<j}(mᵢ+mⱼ)/∏mᵢ.

**Remark 3.2 / S1, n = 4 (exhaustive search, C, orders in [2, 440]).**
- 193 witnesses, 107 primitive; no triple collision.
- Primitive witnesses with maximum order ≤ 130, 220, 440: 16, 33, 107.
- The eight with maximum ≤ 84 are exactly Chen's (A.685)–(A.692).
- I independently tested for a pencil splitting (e₁(A) = e₁(B) = 0, e₃, e₄ equal). Exactly 14, 30, 101 of these primitive witnesses have one, and the six without one are the six listed in S1.
- All of this agrees with the paper.

**Remark 3.2, n = 5.** I enumerated all 216,071,394 multisets in [2, 120] (the count agrees). There is no witness.

**Remark 3.18 / S1 (size-8 genus configurations).**
- The cubic formula e₃ = (P₃ − e₁³)/(3 − 3e₁R) is correct. The real example {1,1,1,1,7} → {0.2664, 4.2830, 6.4506} is correct.
- The count 4,325,115,770 of gcd-1 five-multisets with entries ≤ 220 agrees with the Möbius formula.
- I wrote an independent modular filter with different primes (101–137): reject when x^p ≢ x mod q_V, and accept conservatively when the discriminant vanishes mod p.
- For entries ≤ 100: 88,329,299 multisets, 703 survivors. Exact factorisation shows none of their cubics has a rational root.
- So I confirm the exclusion up to 100. I did not repeat it up to 220.
- The soundness argument (p-integrality of rational roots of a monic cubic whose coefficients have denominators prime to p) is correct.

**Appendix A and Theorem 3.14 / Proposition 3.15.** I re-derived the following and found no error:
- the pigeonhole count of Lemma A.1;
- Proposition A.2;
- the constants 2π(3(L−1)²+1), 6πC(2L)^β, 8πN(2L−3), 16πL² and 12πL²;
- the small-area fall-backs (Example 3.6; (0;5,5,5)/(0;2,2,2,10));
- the formula f(A) = 1 + max{L : A_min(L) ≤ A};
- the o(A) dichotomy, including the parity bookkeeping 2Lᵢ−3 ≤ kᵢ ≤ 2Lᵢ−2.

N(k+1) ≥ N(k) and T(L) ≤ T(L+1) hold as claimed. Since N(2L−3) ≤ N(2L−2), the sandwich does give N(2L−2) ≤ T(L) ≤ 4N(2L−2), which justifies the "constant factor" remark on p. 25.

**Area classes (Figure 3 / S1).**
- I wrote an independent enumerator of complete equal-area classes with unbounded orders.
- s = 1/4 has 7 signatures and maximum K_mult 3, attained by O(2,8,8)/O(3,3,12).
- s = 2/5, 1/2, 1, 7/5 have maximum 3. s = 1/42 has 1.
- For s = 22/15 (outside the 525 classes) the maximum is 4, from the n = 4 witness, which is consistent with "no class with s ≤ 7/5 reaches 4".
- I started a full recount of the 525 classes and a check of Theorem 3.8(iii) on every pair in the classes s = k/60, k ≤ 120. Neither had finished when I wrote this report, so I make no claim about them beyond the classes listed above.

**S2 (strata and triads; exhaustive C enumeration of all hyperbolic triads with S ≤ 4800).**
- Exactly 38 collision-free sums in [18, 4800]; the list agrees with Proposition S2.1 term by term.
- No collision for S ≤ 17. S = 557 has 25,575 triads.
- Triad counts for 10 ≤ S ≤ 18 sum to 83 (Table S3).
- The first collisions of adjacent strata for p = 2,…,14 are 18, 38, 20, 117, 34, 62, 64, 42, 109, 66, 188, 94, 69, with the colliding pairs of Table S2.
- The first non-adjacent collision is (5,15,15)/(7,7,21) at S = 35.
- In exact arithmetic:
  - S\*(p) for p = 2,…,14 agrees with Theorem 5.4.
  - The gap values 1/840, 1/2310, 1/10296 and −7/936, −1/72, −19/3960, −1/180, −76/15015, −1/231, −17/4680 agree.
  - The closed form gap_p(3p+7) = −2(p²−5p−30)/(p(p+1)(p+3)(p+4)(p+5)) holds for p ≤ 29.
  - gap = 0 occurs only at p = 2 (S = 18) and p = 4 (S = 20), consistent with Proposition S2.2.
- I also checked parts of Theorem 5.8: ψ maps E: y² = x(x+9)(x+384) into C₂₇/₂ (exact remainder 0); E ≅ LMFDB 90.c3 with u = 2 (c₄ and c₆ ratios 16 and 64); LMFDB lists rank 0 and torsion Z/2×Z/6; #E(F₇) = #E(F₁₁) = 12; and the twelve listed points lie on E.

**Proved versus found by computer.** The labelling is honest. Every search result in my coverage (Remarks 3.2 and 3.18, the minimal areas for M = 3, 4, the 525 classes, Proposition S2.1, the size-10 4-configuration search) is listed in S8 as computer-only. As far as I can see none of them is used in a proof. The one exception in wording is m1 below.

## FATAL

None. I found no false or unsupported main result in Section 3, Appendix A or S1–S2.

## MAJOR

**M1 (pp. 5–6, Section 1.2, and Theorem 3.14/Proposition 3.15): novelty and weight are overstated, and attributions are missing.**

The text says "The weight of the paper is elsewhere: Theorem 1.1 makes the questions of linear growth and of power lower bounds equivalent to an open problem of Diophantine analysis." In fact:

- (a) The equivalence is the sandwich N(2L−2) ≤ T(L) ≤ 4N(2L−3). The left inequality is one line (Z, −Z is a PTE solution, p. 22). The right inequality is a shift-and-combine construction (Proposition A.2 with Lemma 3.16). The equivalence gives no new information on N or on f. The only unconditional growth content is the pigeonhole bound √A, which comes from the classical pigeonhole bound for PTE.
- (b) Theorem 3.4 and its configuration form (|Z| ≥ 2L+2) are the odd-symmetric analogue of the classical bound N(k) ≥ k+1 and are proved the same way, by Newton's identities. Section 1.2 lists Theorem 3.4 among what is "new on this side" without saying this.
- (c) Lemma 3.7 (a measure with L vanishing moments has at least L sign changes) is classical. See, e.g., Pólya–Szegő, Problems and Theorems II, Part V, or Karlin–Studden on Chebyshev systems. It is presented without citation as "the mechanism behind Descartes' rule of signs".
- (d) Theorem C(1) is Chen's Identity 9 with m = 3, and the n = 4 witnesses are Chen's. This is acknowledged, which is good. The Problem 4 phrasing (an ideal solution of type (−1, 1, 3, …, 2n−5)) is also Chen's language and should say so.

The authors should restate on p. 5 that the substantive new results in Section 3 are Theorem 3.8 (exact and uniform), Theorem 3.11 and Theorem B. They should describe Theorem 1.1(ii) as a reformulation of the growth question rather than its "weight", and add the missing classical citations.

**M2 (Figure 3 caption and p. 26 text versus Table S1): the open squares are misdescribed.**

The caption calls the open squares "doubled Prouhet pairs", and p. 26 says they are "the pairs that Proposition 3.12 gives from Prouhet's solutions, for L = 2,…,6". This is false according to the supplement's own recipe (Table S1 caption, "Prouhet" rows).

- The plotted pairs are genus-changing pairs (genus 1 against genus 0, with cone counts 3/5, 15/17, 63/65, 255/257, 1023/1025). They are built from the Thue–Morse sets by the shift-and-combine construction of Theorem 3.14(c)/Lemma 3.16, not by Proposition 3.12.
- I checked the L = 2 row: the recipe with p = 2, q = 7 (A′ and B′ exchanged) gives exactly (1;2,14,35)/(0;6,7,7,10,21).
- Proposition 3.12 can only produce genus-0 pairs of equal size. For example, doubling Prouhet's degree-1 solution {1,4}/{2,3} gives a pair at s ≈ 1.92, not 12/5.
- The plotted squares also sit at s ≈ 2.4, 15, 63, 255, 1023, whereas Proposition 3.12 applied to Prouhet's solutions would give s < 3·2^{2L−3}−2.
- In addition, the squares for L ≥ 4 cannot be reproduced from the paper and supplement: their cone lists are only in the repository, identified by hashes, and p and q are not given.

The caption, the p. 26 text and the S1 wording ("Prouhet squares") need correcting. The construction should be stated in terms of the paper's own results, with p and q given or a formula for them.

## MINOR

- **m1 (p. 40, proof of Theorem 3.14(b)).** "O(2,8,8) has area π/2 and K_mult = 3". Only K_mult ≥ 3 is needed, and that is proved (Theorem C(3)). Equality is not proved in the paper; it rests on the class enumeration of S1. It is true: I enumerated the 7 signatures of area π/2. Either write "≥ 3" or add the two-line enumeration of that class.
- **m2 (p. 24, before Proposition 3.15).** "f(A) ≥ L+1 for A > A_min(L)" should be "for A ≥ A_min(L)", since A_min is attained, as the proof says.
- **m3 (p. 22, the paragraph after Definition 3.10, and Lemma 3.3).** The paddings U, V and the integer d are defined only after equal area is assumed. So "share their first L heat invariants exactly when Z = U\*⊎(−V\*) is an L-configuration with imbalance 2(g′−g)" is circular as an "iff". Define d := R(m′) − R(m) for any pair, and state the criterion as: d ∈ Z, d = 2(g′−g) + n′ − n, and Z is an L-configuration.
- **m4 (p. 22, Definition 3.10).** "The proof of Theorem 3.4 uses only these conditions." That proof ends with positivity (U\* = V\* and then disjointness). For a configuration the contradiction is instead Z = −Z against the "no pair {z, −z}" condition. Say so explicitly.
- **m5 (p. 23, proof of Theorem 3.11).** "Each odd gap ends at a coefficient of odd degree" should read: each gap between consecutive nonzero coefficients whose degrees have different parity has exactly one endpoint of odd degree, and each odd-degree coefficient is an endpoint of at most two gaps. The bound is right; the sentence is imprecise.
- **m6 (p. 17, proof of Theorem B, "Collecting").** The sign ς_n = (−1)^{n(n+1)/2} is asserted "with the signs" but not tracked; det ∂ₘe = ±∏(mᵢ − mⱼ) and the other "±" factors are left open. I verified the sign numerically for n ≤ 6, but the proof should carry the signs explicitly. It should also say which normalisation of Hur_{n−1} in [40] makes (11) hold without sign.
- **m7 (Theorem 3.14(b)).** "β > 0" should be "β ≥ 1" (N(k) ≥ k+1). The parenthetical "C ≥ N(1) = 2" is not used.
- **m8 (Lemma A.1).** "with n ≤ (L−1)²+1" — the pigeonhole is applied at n = (L−1)²+1. State it that way, or note that smaller n is not claimed.
- **m9 (Theorem 1.2(ii), p. 4).** "at every area, and M+1 cannot be lowered" can be misread as "cannot be lowered at any area". At small areas fewer invariants suffice (Corollary 3.9(c): equality only once the area reaches that of a pair of (iv)). Say "cannot be lowered uniformly in the area".
- **m10 (p. 25).** "Every pair of Example 3.17(iii) is of this form: its two pieces are ideal or equal-sum solutions". The L = 4 equal-count pieces are 7-element sets with vanishing odd sums of degree ≤ 5 (odd size, not ideal PTE solutions in the usual sense). Classify the pieces precisely.
- **m11 (S1, Table S1).** For L ≥ 6 the exact areas are only "in the data file". Since the cone lists are printed, either print the exact s or give a checksum next to each. The approximations "12 − 7.85×10⁻³¹" and similar cannot be checked from the page.
- **m12 (p. 26, Remark 3.18; Problem 3).** Say explicitly that a 3-element side containing 1 and 5-element sides containing 1 are covered (they are, since the search starts at entries 1 and allows rational roots). Also say that "scaled to coprime integers" refers to V alone, not to the whole configuration. As written a reader may take the bound 220 to apply to all orders of the pair.
- **m13 (Section 3.4, p. 25).** The table of bounds on T(L) has no number or caption, and the upper-bound row should cite Table S1 and not only Example 3.17.

## Presentation

- **P1.** Symbols are reused within Section 3 and Appendix A:
  - ν is a measure (Lemma 3.7, Theorem 3.8(iii)) and also a multiplicity difference ν(a).
  - κ is |U\*|+|V\*| (Theorem 3.4) and also the constant in Theorem C(1).
  - C is a class (Definition 2.2), the cone sums Cₗ, and the scaling constant of Theorem 3.8.
  - 𝒯 (tanh series) and T(L) (minimal configuration size) are easily confused.
  - ϱ is both the reciprocal sum and the remainder ϱ(t) of Appendix B.
  - a is both a node and the coefficient aₗ; the authors have to warn about this in the statement of Theorem 3.8.
- **P2.** Theorem 3.8 bundles four results, a construction with a footnote-style warning about notation, and a long example paragraph. Split (ii) and (iv) into a separate proposition with its example.
- **P3.** Example 3.6's "a handle costs no more invariants than a cone point" is not a precise statement; remove it or make it precise.
- **P4.** Figure 2 illustrates the symmetry argument for two pairs but adds little; the colour coding of (b) (black/grey, "with a padding 1") is hard to read.
- **P5.** The statement of Theorem 3.13 carries a long parenthetical about genera ("smaller genus at most 2 … adding equally many handles"). Move it to the proof.
- **P6.** Mixed numbering (Theorems A–C next to 3.x, with 1.x restated as 3.x) is managed by the map on p. 7. A single numbering would still be easier to follow.
- **P7.** Sections S1–S2 are dense running text with recipes inline. A short table of pieces (P, B, shift c, τ) would make Table S1 reproducible at a glance.

## Recommendation

**Minor revision** for the parts I covered: Section 3, Appendix A and S1–S2.
- Confidence that the mathematics in my coverage is correct: high. Every proof was re-derived, and every explicit pair and search result I recomputed agreed with the paper.
- Confidence in the significance judgement: medium. Whether an essentially algebraic Section 3, together with a reformulation of the growth question in PTE terms, carries enough weight for AGAG depends on the analytic sections, which I did not referee. Read alone, Section 3 is sound, honest and modest, and its presentation of its own weight should be adjusted (M1).

## What resolves each issue

- **M1:** Rewrite the "What is elementary and what is not" paragraph and Section 1.2. Name Theorem 3.8, Theorem 3.11 and Theorem B as the new algebraic results, describe Theorem 1.1(ii) as a reformulation, and cite the classical sources for Lemma 3.7 and for the N(k) ≥ k+1 analogue behind Theorem 3.4.
- **M2:** Correct the Figure 3 caption, the p. 26 text and the S1 label: the squares are genus pairs from Theorem 3.14(c)/Lemma 3.16 applied to Thue–Morse pieces. Give p and q (or their formula) for L ≥ 4, so that the plotted points can be checked without the repository. Alternatively, replace them with genuine Proposition 3.12 doublings.
- **m1:** Write "K_mult ≥ 3", or include the 7-signature enumeration of area π/2.
- **m2:** Change ">" to "≥".
- **m3:** Define d and the paddings for arbitrary pairs and state the criterion without assuming equal area.
- **m4:** Add the one sentence for configurations (Z = −Z contradicts the no-pair condition).
- **m5:** Reword the gap-counting sentence.
- **m6:** Track the signs in the proof of Theorem B and fix the Hurwitz normalisation.
- **m7, m8:** Change β > 0 to β ≥ 1; state Lemma A.1 with n = (L−1)²+1.
- **m9:** Say "uniformly in the area".
- **m10:** Classify the pieces precisely.
- **m11:** Print the exact s (or checksums) for L ≥ 6.
- **m12:** Clarify the scope of the search bound.
- **m13:** Number and caption the table, citing Table S1.
- **P1–P7:** Rename the clashing symbols, split Theorem 3.8, and tabulate the S1 recipes.
