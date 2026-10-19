<!-- N-c referee (symmetric systems), round 7: returned text saved verbatim; the reviewer could not write files -->

I wasn't allowed to write `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/N-c-symmetric-systems/REPORT.md` (subagents may not write report files), so the full report is below. My recommendation is minor revision. Every proof and number I checked in my part is correct; the three major issues are about literature, credit and how the constants are presented. My code is in `scratch/code/` and the sources I fetched are in `scratch/lit/`.

# Referee report: "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

**My part:** Lemma 1 (§2), §1.4, §3 (including Remark 1), §4 and §6.4. I read the rest only where my sections depend on it (Proposition 2, Lemma 2, equation (2)). Page numbers are those of the PDF. I read the rendered pages 1, 2, 4, 5, 7–12 and 16–18.

## Summary

A coincidence is a pair of positive rational points on one fibre C_Λ of the Γ1(6) Beauville pencil, after rescaling to a common sum. In my part:
- **Lemma 1:** both triples of a coincidence are admissible.
- **Proposition 3:** reciprocation is translation by T2.
- **Corollary 1:** this gives the dual family of pairs.
- **Theorem 1:** the torsion is Z/6, Z/12 or Z/2×Z/6, and the positive torsion points are exactly the isosceles triples and the geometric progressions, with their orders.
- **Theorem 2:** N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X.
- **Theorem 3:** N(X) ≥ (3/(128π⁴) + o(1)) X (log X)².
- **§6.4:** a heuristic links Question E to rational surfaces in the variety of pairs, which is birational to the fibre square of the rational elliptic surface.

## Significance

The question is natural and suits the journal. It is the reciprocal analogue of Guy's problem D16 and has a clean orbifold motivation. All the mathematics in my part is correct, but the results are modest:
- **Theorem 1:** (i)–(iii) are in substance the standard torsion computation for the universal elliptic curve over X1(6).
- **Theorems 2 and 3** count explicit subfamilies and fall far below the data:
  - the isosceles copies number 2917 at X = 4800, against N(4800) = 102 719;
  - at y = 600, c_A·y·log y ≈ 3.7, against the 423 dual primitive pairs I recomputed.

The value of the note lies in the counting function, the clean structure of §3, the honest data and the precise formulation of Question E.

## Correctness and what I recomputed

Everything below was recomputed with sympy and exact rational arithmetic; no PARI or Sage was available.

1. **Lemma 1 (p. 5).**
   - I re-derived the list of triples with R ≥ 1 and both discriminants.
   - The rendered page confirms R(2,2,5) = 6/5 and R(2,3,4) = 13/12.
   - Brute force over all triples with S ≤ 200, least entry ≥ 1: no class contains a triple with R ≥ 1.
   - Correct, apart from m1.
2. **Weierstrass model (used throughout §3).**
   - Symbolically, the forward map lands on E_Λ, the inverse lands on C_Λ, and the composition is the identity.
   - a² − 4b = (Λ−9)(Λ−1)³.
   - (1:4:4) maps to (−6, 45) at Λ = 27/2.
3. **Proposition 3.**
   - I checked the proof.
   - With an exact group law, ι(P) = P + T2 holds for six points on five fibres (Λ = 27/2, 68/5, 155/12, 71/7, 1849/120).
4. **Permutation action (p. 8).**
   - The three transpositions act as P ↦ −P, P ↦ (1:0:−1) − P and P ↦ (0:1:−1) − P.
   - The cyclic permutations act as P ↦ P ± (0:1:−1).
   - Confirmed on the same points.
5. **Corollary 1.** Sums, reciprocal sums, the condition b² = ac and the (1,4,4) example all check out.
6. **Theorem 1.**
   - I re-derived (i)–(iii), including the converse in (iii).
   - On C_{49/4} with G = (1:2:4): G has order 12, 2G = (0:1:−1) + T2, and the six orderings are kG for k = 1, 3, 5, 7, 9, 11 exactly as stated. 3G = (1:4:2) and 9G = (4:1:2) have order 4.
   - (1:4:4) and (4:1:4) have order 6 and (4:4:1) has order 2.
7. **The data claims in §3 and §6 (S ≤ 600), by full enumeration.**
   - N(X) at X = 18, 100, …, 600 is 1, 92, 386, 840, 1496, 2210, 3067.
   - N_cl(X) is 1, 92, 380, 822, 1468, 2158, 2977.
   - The primitive-class counts and the largest class sizes match Table 2.
   - The local exponents at 400, 500 and 600 are 1.954, 1.993 and 1.868.
   - There are 1753 primitive pairs, of which 423 are dual and 1330 are not.
   - For none of the 1330 does P′ ∓ P have order ≤ 12.
   - 507 of the sums 19 ≤ S ≤ 600 carry a primitive class.
   - The classes at S = 36, 136 and 408 match the text and Table 1.
8. **Theorem 2.**
   - I checked g, primitivity, the determinant-3 map, the area (log 2)/6, the Möbius step (#U/8), the weights 3/4 and 3/4, c_iso = 0.105346, the partial summation, and the injectivity via Λ.
   - There are 506 pairs D_{u,v} with S ≤ 4800 (c_iso·4800 = 505.66).
   - The copies number 2917 = 0.6077X at X = 4800.
   - (count − c_iso X log X)/X is −0.2860 to −0.2863 for 10⁴ ≤ X ≤ 4·10⁷.
9. **Lemma 4 and Theorem 3.**
   - I checked e1, e2, the pair, W and the three geometric-progression conditions.
   - Also the multiplicity ≤ 6, the box inequalities, UV = y/(4α²) and the error O(y^{7/8} log y).
   - c_A = 3/(32π⁴), the final constant 3/(128π⁴), and 128π⁴c_iso/3 = 437.8 are right.
   - Correct as stated; see M2.
10. **§6.4.**
    - 189 lines confirmed.
    - The birational identification of the variety of pairs and the twelve graph surfaces are correct.
11. **MacLeod.** R/r = (Λ − 1)/4 is correct.

**Literature checked against the sources:**
- Schinzel 1996, pp. 587–588: ✓
- Nguyen Xuan Tho 2021, Theorem 1.1 (4 | n, Hilbert symbols, same curve E_n): ✓
- Ulas 2013, Theorem 3.1 and Corollary 3.4: ✓
- Moreland–Zieve, MacLeod, Cha et al., Youmbai–Zargar–Voznyy: ✓
- Crossref bibliographic data for Kelly, Cha et al., Youmbai et al., Bremner–NXT and Schoen: ✓

**Not verifiable headlessly:**
- the Bremner–Guy–Nowakowski quotes and pages (the AMS server returns a bot challenge);
- Bremner–NXT Theorems 8, 9 and 14;
- Beauville's Tableau;
- Schoen's Proposition 7.1;
- Mazur's "Chapter III, Corollary (5.2), p. 156".

## FATAL

None.

## MAJOR

**M1 (p. 4): the literature on equal sums of like powers with negative exponents is missing.**
- The system is the three-term case of Σxᵏ = Σyᵏ for k ∈ {−1, 1}, which has a literature of its own.
- Cite and position the note against A. Choudhry, "Equal sums of like powers, both positive and negative", *RMJM* 41(3) (2011) 737–763, and the classical multigrade sources (Gloden; Dickson's *History* II). I could not retrieve Choudhry's full text.
- Corollary 1's dual identity and the isosceles family may well be classical parametric solutions; if so they must be credited.
- Also cite Choudhry, *RMJM* 43(3) (2013) 763–792 in the equal-product paragraph.
- The novelty sentence "As far as we know … are new" cannot stand until this is checked.

**M2 (pp. 1, 3, 12): the constant in Theorem 3 is a proof artefact, yet the abstract and Theorem B advertise it.** Three arbitrary choices produce it:
- (a) Using ⌊X/S⌋ ≥ X/(2S) where ⌊X/S⌋ ≥ (1−ε)X/S is available for S ≤ εX: factor 2.
- (b) Taking M = y^{1/8} where any M = y^θ with θ < 1/6 works: factor 4/3.
- (c) Counting in a box instead of the full region W ≤ y, whose area is y·log(α²/β)/(2(α²−β)) against y/(4α²): about a factor 3.7–3.9.

Together these improve the constant roughly tenfold, and "log X > 438" becomes about 44. Either state Theorem 3 and Theorem B(ii) as ≫ X(log X)² and drop the 438 comparison, or optimise the constant.

**M3 (pp. 3, 8–9): Theorem A should be credited as the universal-curve-over-X1(6) computation.**
- The pencil is Beauville's Γ1(6) family and Λ is a Hauptmodul: the cusps Λ = ∞, 0, 1, 9 have widths 6, 3, 2, 1, matching I6, I3, I2, I1.
- A = (1:0:0) is the universal point of order 6.
- Then (ii) and (iii) are lifts along X1(2,6) → X1(6) (degree 2, Λ = (2t² + 5t + 2)/t) and X1(12) → X1(6) (degree 4, Λ = (r + 1 + 1/r)²). These are Kubert's parametrisations.
- Say so and cite Kubert, and soften "We determine the torsion". Only (iv) is genuinely new.

## MINOR

- **m1 (p. 5):** "(2, 3, c′) with c′ ≤ 5" should be 3 ≤ c′ ≤ 5. The claimed negative discriminant (c′+4)(24 − 22c′ − c′²)/(6 − c′) equals +1 at c′ = 1. Add one clause justifying "sum 9 and one is (3, 3, 3)".
- **m2 (p. 8):** "α = −1" needs α² = 1 and the fact that −1 is the unique automorphism of order 2, which also holds when j = 0 or 1728. The fixed-point argument should say "over Q̄".
- **m3 (p. 9, proof of Theorem 1(iv)):** "the orderings of (1, r, r²) and of its dual (r², r, 1)" is misleading. The dual is itself an ordering, and the cosets G + Z/6 and P0 + Z/6 have six points each, not twelve.
- **m4 (pp. 9–10):** Remark 1 is labelled a sketch but §6.4 relies on it. Give the short full case analysis, or weaken its use. "Every other polynomial family" should read "every other family by forms of one degree".
- **m5 (p. 11):** the constant −0.286 is numerical. I reproduce −0.2860 to −0.2863, but −0.2852 at X = 4800. Derive it in closed form or label it empirical.
- **m6 (p. 12):** the integral's lower limit 2 should be 18⁻, as in Theorem 2. Make the use of S_D ≤ X in the floor bound explicit.
- **m7 (p. 12, optional):** state the expected order of the dual family, for example via a heuristic on the gcd cancellation, or prove it. It looks within reach and would strengthen §4.
- **m8 (pp. 16–17):** the X^{3/2} implication is rigorous, so state it as a proposition. "With a positive real point" must become "whose positive real points contain a nonempty open set". Add the remark that a Calabi–Yau threefold is not uniruled: then only surfaces with d = 2 can beat X^{1+o(1)}, which sharpens the reformulation of Question E.
- **m9 (p. 4):** Sadek–El-Sissi work with distinct positive integers, not rationals. In arXiv 1303.6705v2 the cited results are Proposition 2.6 and Theorem 2.7, not 2.7 and 2.8; check the published numbering.
- **m10 (p. 17):** I could not verify Schoen's Proposition 7.1. Name the variety as the self-fibre product of the Γ1(6) Beauville surface; to my knowledge it has a rigid, modular Calabi–Yau resolution (Meyer, *Modular Calabi–Yau Threefolds*, 2005). Confirm the exact statement and locator.
- **m11:** check the Mazur locator (the theorem is Theorem (8) of the Introduction) and add Silverman, AEC, Theorem VIII.7.5.
- **m12 (p. 4):** give a page reference for Bremner–Guy–Nowakowski's "every n ≥ 16" expectation.

## PRESENTATION

- **P1 (abstract):** "and already the number of classes" is unclear; see also M2.
- **P2 (Lemma 4):** "conic of pairs" is undefined.
- **P3:** move Remark 1 to §6.4, where it is used.
- **P4 (p. 8):** move the 1753/423/1330 data from the structural discussion to §6.1.
- **P5 (p. 12):** state the coprimality condition on (q, r) in words.
- **P6:** the double naming "Theorem A (Torsion, Theorem 1)" is cumbersome.

## Recommendation

**Minor revision.** Confidence is high on correctness, since every proof in my part and every numerical claim listed above reproduces. Confidence is moderate on the verdict: if M1 shows the parametric families or counts of them are already in print, the novelty claims shrink and the verdict becomes major revision.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Cite and position against Choudhry and the classical multigrade literature; say which families are classical; adjust the novelty sentence. |
| M2 | Restate as ≫, or optimise the constant; remove the "438" comparison. |
| M3 | One paragraph on the universal curve over X1(6), citing Kubert; reword the abstract and Theorem A. |
| m1–m12 | As described above. |
| P1–P6 | Editorial. |

---

## Addendum returned by the reviewer after its Mazur download finished (verbatim)

The Mazur download has now finished, and it changes m11 from "please check" into a real citation error.

**Revised m11 (p. 8, Theorem 1(i)).** The cited Corollary (5.2), p. 156, of Mazur 1977 only says that a rational point on an elliptic curve over Q has order at most 10 or exactly 12. That is not enough for Theorem 1(i): it does not rule out Z/2 × Z/12, which contains Z/6 and whose points all have order at most 12. The list of the 15 possible torsion groups is Theorem (5.1) on the same page, also stated as Theorem (8) in the Introduction. Theorem 1(i) should cite Theorem (5.1). The other use of the corollary, in the §3 paragraph on the 1330 non-dual pairs ("no order ≤ 12, hence infinite order"), is correct as cited. I would still add Silverman, AEC, Theorem VIII.7.5 as a secondary reference.

Mazur therefore moves out of the "not verifiable" list. The rest of the report and the recommendation (minor revision) are unchanged.
