<!-- Provenance: reviewer (c) could not write files; this is its returned report text, saved verbatim by the orchestrating session (its run was interrupted by a connection error and resumed once to finish and return the report). -->

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (submitted to The Journal of Geometric Analysis)

Referee profile: combinatorial number theory, specifically the Prouhet–Tarry–Escott (PTE) problem and equal sums of like powers.

## 1. Summary

The paper looks at closed orientable hyperbolic 2-orbifolds with cone points. It asks how many heat invariants c_1, …, c_k are needed to determine the signature (the genus and the multiset of cone orders).

**The reduction.** At curvature −1, c_1 gives the area and each further c_j adds exactly one new odd power sum of the orders, P_{2j−3}, offset by the reciprocal sum R (Lemma 2.10). Comparing two orbifolds therefore becomes a problem about one signed multiset Z = U* ⊎ (−V*). In Z, the reciprocal sum and the low odd moments vanish. The paper calls Z an L-configuration.

**Main results.**
- **Separation (Theorem 3.4).** Any configuration has |Z| ≥ 2L+2. Consequently K_mult ≤ ⌊Area/π⌋+4 (Corollary 3.5).
- **Descartes bound (Theorem 3.8).** The imbalance satisfies |ι(Z)| ≤ |Z| − 2L.
- **Doubling (Proposition 3.9).** The construction X ⊎ 2Y ⊎ 2Y versus Y ⊎ 2X ⊎ 2X gives the following:
  - no uniform bound on the number of invariants needed;
  - the growth function satisfies f(A) ≳ √A;
  - for 0 < α ≤ 1, f(A) ≳ A^α if and only if N(k) ≲ k^{1/α}, where N is the PTE size function. In particular f is linear if and only if N(k) = O(k).
- **Spheres with n cone points.** For spheres with n cone points, the vector I_n = (R, P_1, …, P_{2n−3}) determines the orders (Theorem A). The paper gives the linear system and its Hurwitz-type determinant (Theorem B), and describes the fibres of I_{n−1} (Theorem C). It exhibits integer witnesses for n = 3 and n = 4.
- **Triangle orbifolds.**
  - Two invariants suffice when the order sum is at most 17. They first fail at (2,8,8) versus (3,3,12).
  - That pair is isolated: C_{27/2} is a rank-0 elliptic curve with torsion Z/2 × Z/6.
  - Exactly 38 sums in [18, 4800] are collision-free.
  - Three invariants always suffice.
- **Other material.** The paper also contains:
  - a quantitative locality theorem with sharpness;
  - stability estimates for recovering the orders (Lipschitz at simple orders, Hölder of exponent 1/k at k-fold orders);
  - numerical spectra and a blind recovery.

## 2. Significance and novelty

**What is good.** This is careful and honest work. Every claim in my area that I could check is correct, and the computations reproduce exactly. The paper is unusually clear about what is classical ("None of this is new", "classical in substance") and about what is a-posteriori rather than certified.

The parts I consider genuinely new and worth having:
- **Separation and the explicit bound.** The bound ⌊Area/π⌋+4 comes from a clean mirror argument (Theorem 3.4).
- **The Descartes imbalance bound** (Theorem 3.8).
- **The doubling trick.** It disposes of the reciprocal-sum constraint for free, since the factor 1 − 2^{j+1} vanishes at j = −1. This gives the √A lower bound using only odd-power pigeonholing, with n ≤ (L−1)²+1 rather than ~2L².
- **The triangle analysis.** The first failure at sum 18, the strata/overlap theory, the 38 collision-free sums, and the isolation of (1:4:4) and (1:1:4) on C_{27/2} form a tidy, complete story.

**On the PTE headline.** The abstract says linear growth of f "is equivalent to the open question whether N(k) = O(k)". I checked both directions and the equivalence is genuine, not merely an analogy. It is, however, a soft equivalence:
- it holds only at the level of polynomial exponents;
- it passes through the minimal configuration size, which the paper never names;
- it rests on two elementary reductions: (Z, −Z) is a PTE solution of degree 2L−2, and the doubling construction.

So it relocates the growth question; it does not open a new line of attack. The paper does say "relocates rather than settles", which I appreciate.

**Prior art.** Several PTE-side statements are less new than the main text implies (see Major 1):
- the n = 4 witness, and in fact all eight primitive witnesses with maximum order at most 84;
- the pair criterion of Theorem C(1);
- the "pencil" mechanism.

All of these are in Chen's 2025 survey [45], or are classical.

**Fit for JGA.** The geometric-analysis content (trace formula, locality, divergence of the expansion) is acknowledged as classical in substance. The new mathematics is mostly elementary algebra and arithmetic. For a geometric-analysis journal the significance is moderate. The manuscript runs to 37 pages plus a 12-page supplement and spans five loosely coupled themes, which dilutes it.

## 3. Correctness: what I recomputed, how, and the results

All of this was done independently, in exact integer or rational arithmetic unless stated. My own code is in my scratch folder (Python/sympy, C with 128-bit integer comparisons, and PARI via cypari2 in a local virtual environment). I also rendered and inspected the figure pages and every formula-dense page I relied on.

**1. Heat coefficients (Proposition 2.7, Lemma 2.8, Lemma 2.10, eq. (9)).**
- I implemented (4) and (5) from scratch.
- p_0, p_1, p_2 agree with (7), and p_3 = x⁸/10080 + x⁶/3780 + x⁴/2160 + x²/945 − 19/10080.
- α_0, …, α_5 = 1, −1/3, 1/15, −4/315, 1/315, −4/3465.
- (9) holds for several triads.
- The triangular structure of Lemma 2.10 holds.

**2. Explicit witness pairs.** For every printed pair I computed the heat invariants c_j directly and counted how many leading coefficients agree. This covers Theorem C(3), Examples 3.6 and 3.12, (0;5,5,5)/(0;2,2,2,10), and every printed row of Table S1: genus, equal-count and cone-count rows for L = 2…7, and Prouhet rows L = 2, 3.
- In every case the shared count equals the claimed L exactly. All pairs are hyperbolic and disjoint, with equal areas.
- The areas match the table (for example 41149074301/5878522650 for the L = 4 genus row).
- |U*|+|V*| is 16, 20, 26, 40 for the genus pairs with L = 4–7, as stated, and 10 for (1;15,15,15)/(0;3,3,5,7,7,21), as stated.
- Theorem C(3) numbers: R = 3/4, P_1 = 18, P_3 = 1032 versus 1782; and R = 8/15, P_1 = 58, P_3 = 31402, P_5 = 25159618 versus 21298618. All confirmed.

**3. Prouhet rows with L = 4 and 5.** These lists are not printed, so I rebuilt the construction from the caption of Table S1.
- **As literally written the construction cannot work.** With σ₁ = (1; qU₀ ∪ pB′) the reciprocal condition forces p/q < 0.
- **With A′ and B′ swapped everything reproduces exactly:**
  - p and q have 45/46 digits (L = 4) and 208/208 digits (L = 5);
  - s = 63 − 2.25·10⁻⁴⁵ and 255 − 1.02·10⁻²⁰⁷;
  - the cone counts are 63/65 and 255/257;
  - the shared count is exactly L;
  - the printed L = 2 and L = 3 rows ((1;2,14,35) and the 15/17-element lists) are reproduced verbatim by the swapped version.

  So this is a typo in the caption (Minor 1).

**4. Remark 3.2 and Supplement S1, n = 4.** Exhaustive search over 4-multisets in [2, 440], grouped by P_1, keyed on P_3 with R compared by exact cross-multiplication:
- 193 pairs, 107 primitive.
- Primitive pairs with largest order at most 130, 220, 440: 16, 33, 107. All pairs at the same bounds: 19, 53, 193.
- No key is shared by three multisets. All pairs are disjoint, with P_5 different.

Pencil splittings (my own enumeration): 17 witnesses (14 primitive) at bound 130, and 49 (30 primitive) at bound 220. The two primitive non-pencil witnesses up to 130 are exactly (16,16,74,74; 11,37,44,88) and (11,21,99,99; 9,51,51,119). All counts confirmed.

**5. n = 5.**
- All 216,071,394 multisets in [2, 120]: no witness, confirmed.
- A planted control (dropping the P_5 key) recovers collisions, so the search can find them.
- I extended the search to [2, 200]: 2,733,664,990 multisets, still no witness.

**6. Remark 3.13, shape (3,5), entries up to 220.**
- The number of gcd-1 5-multisets is 4,325,115,770, confirmed both by Möbius inversion and by direct enumeration.
- 29,494,902 have three positive real partner roots, matching the paper exactly.
- My filter differs from the authors'. I used a necessary condition (the discriminant of the integer cubic must be a square modulo 12 primes near 2³¹), with a float pre-filter tolerant to rounding. It left 7,250 candidates. Exact factorisation over Q showed all 7,250 are irreducible (for example (1,1,7,9,35) gives a cyclic cubic). Conclusion: no size-8 genus pair in range, confirmed.
- The {1,1,1,1,7} partner is {0.2664, 4.2830, 6.4506}, as stated.

**7. Proofs checked line by line.**
- Lemma 3.1; Theorem A (including the multiplicity bookkeeping); Theorem C(1) and C(2); Lemma 3.3; Theorem 3.4; Corollary 3.5.
- Theorem 3.8. The argument is correct: odd-degree gaps are charged to odd-degree nonzero coefficients, at most (T−2L)/2 of them, each ending at most two gaps.
- Proposition 3.9 (including (1 − 2^{j+1}) = 0 at j = −1, hyperbolicity for n = 2, and distinctness via 2x*); Theorem 3.10; Lemma B.1 (Σ_{j≤L−1}(2j−1) = (L−1)²); Proposition B.2.
- Theorem 3.11 (a)–(e), both directions of (d). The constants work: N(2L−3) ≤ (2L−3)(L−1)+1 ≤ 2L², the floor choices, and the small-area fallbacks via (2,8,8), Example 3.6 and (5,5,5)/(2,2,2,10).
- I found no gap.

**8. Theorem B.** I built M symbolically from (11) for n = 2, 3, 4, 5. In each case the true e solves the system, and det M equals ς_n ∏_{i<j}(m_i+m_j)/∏_i m_i at three test points.

**9. Triangle orbifolds.**
- Exhaustive C search over all S ≤ 4800. The collision-free sums in [18, 4800] are exactly the 38 listed. There are 4783 sums in total (= 4745 + 38). S = 557 has 25,575 triads. No collisions occur below 18.
- Table S2: all 13 rows reproduced (x*, S*, first collision and pair).
- Theorem 5.4's "if and only if" verified for p < 40, S < 800.
- Formula (14), gap_p(3p+7), the three odd-parity gaps 1/840, 1/2310, 1/10296, and the seven values at S*+1 all confirmed.
- 83 triads with 10 ≤ S_1 ≤ 18, confirmed.
- First non-adjacent-strata collision is (5,15,15)/(7,7,21) at S = 35, confirmed.

**10. Theorem 5.10.**
- ψ maps E into C_{27/2}: the polynomial remainder modulo E is 0.
- φ∘ψ = id on the 11 affine points.
- disc E = 2¹⁸3⁸5⁶ and #E(F_7) = #E(F_11) = 12.
- PARI: ellrank gives [0,0], elltors gives Z/6 × Z/2, analytic rank 0, conductor 90.
- I brute-forced the local 2-descent claims: mod 5 for d_1 ∈ {±2, ±3} on E, and 3-adically for d_1 ∈ {3, 5, 15} on E′.
- A brute-force search of primitive points with coordinates up to 60 finds only the 12 listed points.

**11. Section 6 and 7 algebra.**
- The amp values are 2, 14, 498, 4062, 56230/3, and the P_3 row is (−18, −120, −360), as stated.
- d_3, d_4, d_5 = 25/12, −1775/24, 153025/48 (d_6 = −150503225/864).
- The algebra of Proposition 6.6(i) and Remark 6.7 checks.

**12. Figure 3.**
- There are 525 areas, as stated.
- I enumerated each complete class with no bound on the orders. 504 classes contain orders above 12, as stated.
- The largest K_mult per class is 1, 2 or 3, distributed 17 / 311 / 197, with maximum 3. This is consistent with the dots in the figure.

**13. Literature checks.**
- Wooley, Theorem 13.1 (W(k,h) ≤ ½k(k+1)+1): correct as cited.
- Melzak 1961: the pigeonhole bound, (n²+4)/2, and the non-constructive exact formula are all present as described.
- Croot–Mao–Yip: confirms that ideal solutions are known only for k ≤ 9 and k = 11.
- I found no subquadratic bound for N(k) in recent arXiv work, so "all known bounds are quadratic" stands.
- I could not access Borwein–Ingalls to check its problem numbering.

**Not recomputed (outside my competence or my tools):** the trace-formula analysis (Lemmas 2.4–2.5, Appendix A), Theorems 4.4–4.5, the Rouché and certificate constants of Section 6 and Proposition S3.1, and the finite-element spectra.

## 4. MAJOR issues

**M1. Prior art on the PTE side is not credited in the main text, and novelty is overstated.**

*Where:* Theorem C(1) and C(3), Remark 3.2, Section 1.1 ("What we add …"), Example 3.12(i).

*What the record shows:*
- Chen's survey [45], §A.5.8, lists [3,10,15,30] =_k [4,5,21,28] for k = −1, 1, 3 as (A.685), a 2017 computer search. It also lists seven more solutions (A.686)–(A.692).
- These eight are exactly the eight primitive witnesses with maximum order at most 84 that the authors' own exhaustive search (and mine) finds.
- Chen's Identity 9, with Corollary 3.4 ((3.27)–(3.28) with m = 3, exponents −1, 1, 3, …, 2n−3), is precisely the pair criterion of Theorem C(1): Q(z) − Q(−z) = 2κz³. Chen's (3.33) is the formula for that constant when n = 5.
- The "pencil splitting" is a variant of the classical way to build PTE solutions from two integer-rooted polynomials whose difference has a prescribed lacunary shape. Chen notes explicitly that the (−1,1,2,3) solution [−5,10,15,30] = [−3,4,21,28] (B.179), whose e_3 vanishes and so which differs only in the constant term, transforms into (A.685).

*Current state:* the supplement mentions (A.685) and (3.33) in passing. The main text credits none of this, and presents "Integer sharpness for n = 3, 4" and the pair criterion without attribution.

*Fix:* credit these in the theorem statements. Recalibrate "What we add". I would say the genuinely new PTE-side items are:
- the separation bound T ≥ 2L+2;
- the Descartes imbalance bound;
- doubling;
- the growth equivalence;
- the exhaustive counts.

Theorem A should also be framed accurately. For positive orders, which is all the geometry needs, it is a special case of Steinig-type uniqueness for n distinct exponents. Its added content is the extension to complex multisets with multiplicity, and the Hurwitz/Orlando determinant.

**M2. The headline equivalence should be stated through the quantity that actually governs f, with explicit constants.**

*Where:* Theorem 1.1(ii), Section 3.3, Theorem 3.11, Problem 1.

*Why it matters:* The proofs implicitly show that f is, up to constant factors, the inverse of T(L), the minimal size of an L-configuration:
- T(L) ≤ 2⌊A/π⌋+8 whenever f(A) ≥ L+1;
- a configuration of size T is realised with area below roughly πT (or 4π when the genus-1 side is needed);
- N(2L−2) ≤ T(L) ≤ 6((L−1)²+1), and T(L) ≤ 4N(2L−3) for genus-changing configurations.

Stating this makes three things clear:
1. exactly what is equivalent to what;
2. that the PTE link is only exponent-level;
3. that Problems 2 and 3 are the first unknown cases of an "ideal configuration" question (whether T(L) = 2L+2), the direct analogue of ideal PTE solutions.

From the paper's own tables:

| L | lower bound 2L+2 | best known T(L) |
|---|---|---|
| 2 | 6 | 6 |
| 3 | 8 | 8 |
| 4 | 10 | 14 |
| 5 | 12 | 18 |
| 6 | 14 | 24 |
| 7 | 16 | 40 |

*Fix:* define T(L); prove A_min(L) ≍ T(L) with explicit constants; add the table; restate Problems 1–3 in terms of T(L). This would make the PTE section a real contribution to the PTE literature, not only a translation.

**M3. Scope, focus and fit.**

*Where:* the whole paper and the supplement.

*Why it matters:* the manuscript combines five themes:
- the asymptotic expansion (re-derived; "none of this is new");
- the combinatorics of the signature;
- triangle arithmetic, including an elliptic-curve descent;
- the classical locality made quantitative;
- stability analysis plus finite-element numerics and a blind recovery.

Each theme is competently done, but the geometric-analysis novelty is thin. The new content is mainly algebraic, arithmetic and computational, and the 49 pages bury it.

*Fix:* tighten around Sections 3 and 5, with Theorem 1.3 as a short section. Move Section 4 (classical) and most of Section 7 into a remark or the supplement. Alternatively, make a convincing case to the editor that the combinatorial core fits JGA. I leave the fit question to the editor; as written, I would not recommend acceptance without this streamlining.

## 5. MINOR issues

1. **Supplement, Table S1 caption.** "σ₁ = (1; qU₀ ∪ pB′), σ₂ = (0; qV₀ ∪ pA′)" has A′ and B′ swapped. As written, the reciprocal condition forces p/q < 0. With the swap, all Prouhet rows reproduce (Section 3, item 3).
2. **Table S1, L = 6 Prouhet row.** "1023 − 0.00 × 10⁰" is a formatting underflow; print the actual exponent of the deficit.
3. **Remark 3.2 counting conventions.** State that "witness" means an unordered pair of disjoint multisets, and that the 17/49 counts include non-primitive witnesses. Give the matching exhaustive totals (19 and 53) so the pencil and exhaustive counts can be compared. State that no key is shared by three multisets.
4. **Evidence value of the n = 5 and (3,5) searches.** A naive height count calibrated on n = 4 predicts the observed ~H² growth there (19, 53, 193 at H = 130, 220, 440). The same count predicts ~H⁻¹ for n = 5. So bounded searches are weak evidence either way, and solutions, if any, will likely come from structure. Add such a heuristic, and consider structured searches: parametrise Q(z) = E(z²) + κz³ with all integer roots, or use Chen's (3.33). My extension to orders ≤ 200 (2.73·10⁹ multisets) also found nothing; the authors could cite such an extension.
5. **Remark 3.13.** A discriminant-squareness test modulo a few primes is a rigorous necessary condition that reduces the candidates to about 7·10³ (versus 220,428). It is worth mentioning as an independent second check.
6. **Section 3.3.** Please quote the Borwein–Ingalls problems verbatim ("Problem 3", "Problem 4"). I could not verify the numbering. Also give both parity forms of Wright's bound.
7. **Theorem 3.8.** Relate it to the classical fact that a real-rooted polynomial cannot have long runs of vanishing coefficients (Descartes/Newton), and cite accordingly.
8. **Example 3.12(iii).** Give the recipe for each row: which solutions, which shifts c, c′ and which λ. As it stands, 40-digit lists appear without a reproducible construction in the text.
9. **Theorem 3.10.** Clarify "the smaller of which can be any integer g ≥ 1". Smaller genus 0 also occurs.
10. **Proposition 6.2.** The stated diagonal formula omits F₀₀ = −1/2.
11. **Notation overload:**
    - e_k is used for elementary symmetric functions, for the descent exponents e₁, e′₁, and for the integer e in M, e;
    - e₂ = XY+YZ+ZX is used in Theorem 5.10;
    - σ denotes both the signature and the coefficients σ_i;
    - ψ_k and the map ψ;
    - φ_p, φ and ϕ_k.
12. **Repository paths** in Appendix C and the supplement ("review/audit-2/…", "review/round1-fixes/…") expose internal process names. Use neutral paths.
13. **Example 3.12(ii).** Note that [1,5,5] = [2,3,6] is a (1,3) solution, not a PTE solution of degree 3.

## 6. Presentation, figures and captions

The writing is dense but precise. Theorem statements are carefully hedged, and the separation between certified and a-posteriori results is exemplary. The roadmap helps. The introduction's prior-work section is long and still misses Chen's relevant entries (Major 1).

Figures (checked on rendered pages at 110 and 300 dpi):
- **Fig. 1.** The caption says "reaches the largest order … at the darkest tip", but panel (a) has two order-8 tips; say "at the tips of largest order". At high zoom the colour-bar label "4πt 𝔥_t(x,x)" shows the t and 𝔥 glyphs touching.
- **Fig. 2.** Correct: X* and −X* match U* = {2,8,8}, V* = {3,3,12} and U* = {1,15}, V* = {3,3,5,5}. However, panel (a) uses teal/orange and panel (b) black/grey, with no key. Use one colour convention and state it.
- **Fig. 3.** Consistent with my recomputation (dots at K_mult 1–3; bounds drawn correctly, with the dashed curve starting at s = 4). Add a legend; the caption carries all the decoding.
- **Fig. 4(b).** The vertical axis is non-linear (it appears to be a square-root scale); say so.
- **Fig. 5.** Captioned "tilings of the hyperboloid" but drawn as perspective discs; state the projection.
- **Fig. 6.** Consistent with Table S2. Say what the thin dotted connectors denote.
- **Fig. 7.** The slopes 1, ½, ⅓, ½ are visibly correct.
- **Fig. 8.** Fine.
- **Tables 1, S1–S6.** Clear, apart from Minor 1 and Minor 2.

## 7. Recommendation

**Major revision.**

Every combinatorial, arithmetic and computational claim in my area is correct and exactly reproducible. That includes all witness pairs and their exact shared counts, all four exhaustive searches (which I extended), the 38 collision-free sums, Table S2, and the rank and torsion of C_{27/2}. The growth equivalence is genuinely an equivalence, in both directions.

The revision is needed for three reasons:
1. proper attribution of the PTE-side results that already appear in Chen's survey (A.685–A.692, Identity 9) or are classical, with corresponding recalibration of the novelty claims;
2. restating the PTE connection through the minimal configuration size T(L) with explicit constants, which would make it a sharper and more useful result;
3. substantial streamlining for a geometric-analysis venue.

Confidence: high for Sections 3 and 5 and Appendix B, where I recomputed everything. Moderate overall, because I did not independently verify the analytic Sections 2.1, 4 and 6 or the numerics of Section 7.
