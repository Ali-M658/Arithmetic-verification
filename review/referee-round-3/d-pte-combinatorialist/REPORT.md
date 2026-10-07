<!-- The reviewer's write was refused by the harness ('Subagents should return findings as text'); this file is the reviewer's returned final message, saved verbatim from the task transcript by the main session. -->

I could not write the report file. The harness refused the write because subagents must return findings as text. The full report is below, and no file exists at `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-3/d-pte-combinatorialist/REPORT.md`. My scratch code and data are in `.../d-pte-combinatorialist/scratch/`.

---

# Referee report (PTE / equal-power-sum review): "How much of a hyperbolic orbifold does heat hear?"

Submitted to the Annals of Global Analysis and Geometry. Reviewer role: combinatorialist and computational number theorist (Prouhet-Tarry-Escott problem and equal-power-sum problems). I read manuscript.pdf (48 pp.) and supplement.pdf (15 pp.) only, plus published literature fetched for citation checks. The placeholders (author contributions, AI-use statement, Zenodo DOI) are treated as known and not counted.

I did not review the spectral-theoretic Sections 4, 7 and 8, the elliptic-curve rank argument, or the analysis behind Theorem 1.3. My checks cover every statement that uses or claims equivalence with PTE, and the exhaustive searches.

## 1. Summary

The paper asks how many small-time heat invariants c_1, c_2, ... of a closed orientable hyperbolic 2-orbifold with cone points are needed to determine its signature (genus g and multiset of cone orders m_i).

The central mechanism is exact. At curvature -1 the j-th invariant is an affine function of the area plus a sum of cone terms b_{j-2}(m_i). By Lemma 2.10 the cone term is a triangular combination of the odd power sums P_1, ..., P_{2j-3} and the reciprocal sum R = sum 1/m_i. So H_L(O) = H_L(O') exactly when the "areas" 2g-2+n-R agree and P_{2k-1}-R agrees for k < L.

Two orbifolds of different signature therefore share H_L exactly when Z = U* + (-V*) is an "L-configuration". Z is an even-size multiset of nonzero rationals with no pair {z,-z}, with sum z^j = 0 for odd j <= 2L-3 and sum 1/z = 0. Its minimal size is T(L).

The results are:

- **Separation (Thm 3.4).** T(L) >= 2L+2, hence H_{floor(Area/pi)+4} determines the signature.
- **Descartes bound (Thm 3.8).** |imbalance| <= |Z| - 2L.
- **Doubling (Prop 3.9).** From two n-multisets with equal odd power sums one builds a configuration of size 6n whose reciprocal sums also agree.
- **Growth (Thm 3.11, Prop 3.12).**
  - N(2L-2) <= T(L) <= 6 min{(L-1)^2+1, N(2L-3)}.
  - So f(A) = max Kmult grows like A^alpha (0 < alpha <= 1) iff N(k) = O(k^{1/alpha}). In particular f is linear iff N(k) = O(k).
  - Unconditionally the growth exponent lies in [1/2, 1].
- **Explicit data.**
  - The minimal pair (2,8,8)/(3,3,12) is the first collision for triangle orbifolds.
  - T(2)=6 and T(3)=8, with upper bounds T(4..7) <= 14, 18, 24, 40.
  - Exhaustive integer-witness searches: n=4 with orders <= 440, and n=5 with orders <= 120.
- **Open questions.** Whether T(L) = 2L+2 for all L, whether a genus-changing collision of size 8 exists at L = 3, and whether integer witnesses exist for n >= 5.

## 2. Significance

For AGAG readers this is a clean, new, quantitative answer to a natural inverse-spectral-type question. It gives the first explicit finite count I know of for closed orientable hyperbolic orbifolds, and it shows that "audibility by finitely many invariants" is non-uniform in the area.

The PTE link is the most interesting feature. The reduction is exact and elementary. The paper says it "relocates the growth question to PTE rather than settling it", and I agree.

New on the PTE side, against the literature I checked (Chen's survey arXiv:2506.11429, Melzak 1961, Croot-Mao-Yip arXiv:2609.05061, and Borwein-Ingalls as quoted by those sources):

- the Descartes-rule bound |iota| <= |Z| - 2L, which is correct and neat;
- the doubling identity P_j(U) - P_j(V) = (1 - 2^{j+1})(P_j(X) - P_j(Y)). It removes the exponent -1 discrepancy for free, so the reciprocal-sum constraint costs only a constant factor. This is what makes the equivalence with N(k) true;
- the separation bound;
- the explicit pairs of sizes 14, 18, 24, 40;
- the observation that Chen's (-1,1,3) ideal solutions are exactly the T(3)=8 configurations;
- the exhaustive n=4 and n=5 searches.

From a PTE viewpoint nothing new is learned about N(k) itself. T(L) is a PTE-type object (Chen's type (-1,1,3,...,2L-3)) within a factor 6 of the ordinary problem. This is a good application of PTE to geometry, not a contribution to PTE.

## 3. Correctness and what I recomputed

I used exact arithmetic (Python Fraction and sympy) or exact-key hashing in C++ with exact post-verification. Wherever a control was meaningful I planted one.

### Reduction from heat invariants to odd power sums

1. I recomputed the p_l from Lemma 2.6, (4) and (5), and the alpha_k from Prop 2.7.
   - Formula (7) is reproduced exactly: p_0 = (m^2-1)/12, p_1 = m^4/360 + m^2/36 - 11/360, p_2 = m^6/2520 + m^4/720 + m^2/180 - 37/5040.
   - alpha_0..4 = 1, -1/3, 1/15, -4/315, 1/315.
   - The p_l are even polynomials of degree 2l+2 with positive top coefficient, for l <= 8. This is the triangularity of Lemmas 2.8 and 2.10.
2. Lemma 2.6's closed form agrees with numerically differentiated sums Phi_m(u) to 15 digits, for m = 2, 3, 5, 7 and Taylor orders 0 to 3.
3. I checked the expansion against the trace-formula terms themselves.
   - Cone term E_m(t) of Thm 2.3, by 30-digit quadrature, against sum_{l<K} b_l(m) t^l. The residual scales as t^K (halving t divides it by 2^K) for K = 4, 6, 8 and m = 2, 3, 5.
   - The identity term against sum alpha_k t^k scales the same way.
   - So, given Theorem 2.3, the coefficients used in Section 3 are right.
4. I recomputed the shared-invariant count of every explicit pair two ways: from the c_j via (6) up to j = 9, and from (area, Psi_k = P_{2k-1} - R).
   - All 20 pairs printed in full in Table S1 (genus, equal-count, cone-count, Prouhet L = 2, 3) share exactly the stated L. Their areas are equal and their order sets are disjoint.
   - The main-text pairs also agree: (2,8,8)/(3,3,12), (3,10,15,30)/(4,5,21,28), (1;15)/(0;3,3,5,5), (1;15,15,15)/(0;3,3,5,7,7,21), and the 7-versus-8 cone pair.
   - The sizes 6, 8, 14, 18, 24, 40 (equal count) and 16, 20, 26, 40 (genus) match Example 3.13(iii) and the T(L) table.
5. The Prouhet squares for L >= 4 are not printed. I rebuilt them from the Table S1 caption recipe.
   - L = 4, 5, 6 give 63+65, 255+257 and 1023+1025 cone points, genus 1 versus 0.
   - They have equal area (s = 63, 255, 1023 up to tiny corrections) and share exactly L invariants.
   - The "p, q of 45 and 46 digits" claim for L = 4 matches.

### Proof checks

6. **Thm 3.4.** Correct. Parity of T follows from (13), the reciprocal sum kills e_{T-1}, and the mirror argument forces U* = V* = empty.
7. **Thm 3.8 (Descartes).** I rederived the sign-change bookkeeping and it holds. The count (T-2L)/2 of nonzero odd-degree coefficients is right, as is "each odd-degree coefficient ends at most two odd gaps". The bound is attained at L = 2, |Z| = 6.
8. **Prop 3.9 (doubling).** Correct, including exponent j = -1 and the hyperbolicity check for n = 2.
9. **Lemma A.1 (pigeonhole).** The vector count is at most n^{L-1} M^{(L-1)^2}, using P_j in [n, nM^j]. The bound M > n! n^{L-1} is right.
10. **Prop A.2 and Thm 3.11(c).** The combination Z(c) + lambda Z(c') with lambda = -rho(c')/rho(c) cancels the reciprocal sum (that of lambda Z(c') is rho(c')/lambda). The area bound 8 pi N(2L-3) <= 16 pi L^2, from N(2L-3) <= 2L^2, is right.
11. **Thm 3.11(a),(b),(d) and Prop 3.12.** These follow. N is nondecreasing, which is what the "iff" statements need. The cases L < 2 in (b) are covered by f >= 3.
12. **Thm C(1).** This is Chen's Identity 9 with m = 3. I located it in the survey, and the correspondence with Chen's n+1 = set size is exact. Thm C(2) (Jacobian rank n-1) and the disjointness of witnesses (Theorem A applied to the reduced pair) are correct.
13. I found no error in any PTE-related statement of Section 3.

### Exhaustive searches

14. **n = 4, orders in [2,440], equal (R, P1, P3).** I enumerated about 1.6e9 multisets with a modular 64-bit key and verified all collisions exactly.
    - I found 193 pairs, 107 primitive, no triple sharing a key, and P5 different in every pair.
    - Primitive counts with largest order <= 84, 130, 220, 440 are 8, 16, 33, 107, exactly the paper's numbers.
    - The eight at most 84 are Chen's (A.685)-(A.692).
    - The six exceptions in Section S1 are genuine pairs.
    - Using the supplement's definition of "pencil splitting", exactly those six of the 107 primitive pairs have none, so "all but six come from a pencil" is correct.
15. **n = 5, all 216,071,394 multisets with orders in [2,120], key (P1, P3, P5, R).** There are 0 collisions. Control: dropping P5 from the key at bound 40 gives 43 collisions. "No witness at most 120" is confirmed.
16. **Remark 3.14, size-(3,5) search, entries at most 220.**
    - The number of 5-multisets of {1..220} with gcd 1 is 4,325,115,770 (Moebius-checked).
    - My long-double discriminant count of those whose cubic has three positive real roots is 29,494,902, exactly the paper's figure.
    - I did not rely on the paper's filter for rationality. I required the cubic to split completely modulo each of 12 primes in 223..277 (above every order, using a table of all splitting triples). Fifteen of the 4.3e9 candidates survive, and all 15 are irreducible over Q by exact factorisation.
    - So no 5-multiset with entries <= 220 and gcd 1 has an all-rational partner triple, and the paper's statement holds.
    - Separately, an integer-partner search with V <= 110 (partner entries up to 550) has no hits, and a control that drops R from the key does hit.
    - The example {1,1,1,1,7} with partner roots {0.2664, 4.2830, 6.4506} is correct.
17. **Theorem 1.2.**
    - Collisions in (S1,R) among hyperbolic triads with sum <= 60 begin at S1 = 18, with (2,8,8)/(3,3,12). There is none for S1 <= 17.
    - There are 83 hyperbolic triads with 10 <= S1 <= 18.
    - (S1,R,P3) is injective on this range.
    - For k = 1..5 the only triads with the key of (2k,8k,8k) are it and (3k,3k,12k).
18. **Figure 3 and the "525 classes".**
    - Genus <= 1, at most 4 cone points of order <= 12, area 2 pi s <= 2 pi (7/5): exactly 525 distinct areas.
    - I enumerated the complete classes by Egyptian-fraction search with no order bound, and computed the maximum Kmult per class from 14 invariants.
    - 504 classes contain an order above 12, as stated.
    - The maximum Kmult is 3. The distribution is 17 classes with K=1, 311 with K=2, 197 with K=3, and the first K=3 class is s = 1/4. This matches the plotted dots.
    - Diamonds and squares sit at (s, L+1) for the Table S1 pairs. The solid curve floor(2s)+4 and the dashed curve floor(sqrt((s-1)/3))+2 match Cor 3.5 and Thm 3.11(a).

### Literature

19. [34] (arXiv:2609.05061) exists, and its introduction supports "ideal solutions known only for 2 <= k <= 9 and k = 11". [20] (arXiv:2506.11429v1, 368 pp.) exists.
    - It lists A.685-A.692 under type (-1,1,3), attributed to Chen in 2017.
    - It gives the (-1,1,3,5) identity (3.33) with no numerical solution, as the supplement says.
    - It has no ideal-solution entry of type (-1,1,3,5).
20. Melzak's note writes K(n) < (n^2+4)/2, attributes it to Wright, and calls it "the best bound known so far" in 1961. The paper's "[32, p. 234]" is accurate but it is a 1961 secondary report (see m1).
21. I could not retrieve Borwein-Ingalls. So "[5, Props 2-3]", "[5, §6, Problem 3]" and "[5, p. 9]" are unverified by me. They are consistent with how Melzak and Croot-Mao-Yip quote the same bounds.

## 4. MAJOR issues

**M1. The upper bounds in the T(L) table for L >= 4, and the genus-changing pairs, are given by data alone, with no construction and a citation that does not match.**

- **Location.** Example 3.13(iii); the T(L) table (p. 16); Table S1.
- **Issue.**
  - The sizes 14, 18, 24, 40 rest on pairs with up to 36-digit orders. The text says only "from symmetric ideal solutions [5, p. 9], [33] and equal sums of odd powers [20, A.1.33]".
  - Chen's A.1.33 is type (1,3,5,7,9), five odd exponents. That covers at most L = 6, since odd sums up to 2L-3 = 9. L = 7 needs six exponents and is not covered.
  - Nothing says how the reciprocal-sum condition is met for L = 4..7.
  - For an ideal solution (X,Y) of degree 2L-3 with f(c) = prod(x_i+c) and g(c) = prod(y_i+c), f - g is a constant delta. The numerator of rho(c) is then -delta g'(c), so rho(c) = 0 iff g'(c) = 0. A rational critical point of g is a non-generic coincidence. How it is obtained (a parametric family, or a search) is the heart of the construction and is missing.
- **My side experiment.** Among 815 ideal degree-5 pairs with entries <= 64, only 6 are not symmetric about their centre, and none has a rational critical point of g. This suggests why a size of 12 for L = 4 is hard, and how special 14 is.
- **Resolution.**
  - State, for each L in 4..7, the exact construction: which ideal or odd-power solution, which shift or scaling, and how the rational root of rho was found.
  - Fix the A.1.33 attribution.
  - Say what was searched for T(4) <= 12. Problem 2 asserts T(4) in [10,14] without saying whether 12 or 10 was attempted.

**M2. The exclusion in Remark 3.14 (and so the "undecided" status of Tg(3) in {8,10}) is argued by an under-described floating-point filter.**

- **Location.** Remark 3.14; S1 ("a filter in floating point with rigorous inclusion disks"); S8(ii).
- **Issue.**
  - A V is rejected "only when three rational roots are excluded" by disks with errors "bounded by 64 eps times further safety factors". The arithmetic is long double, which the supplement itself says is binary64 on the platform.
  - The cubic's coefficients involve R with denominators up to lcm(1..220), about e^220. If the roots are rational their heights are not a priori bounded. A binary64 disk cannot exclude rational points of unbounded height.
  - The criterion actually used is not stated, and "rigorous" rests on ad hoc safety factors.
- **Status.** My independent verification (item 16) supports the conclusion, so I believe it is true. As written, though, the exhaustiveness cannot be demonstrated by a reader.
- **Resolution.** State the exact necessary condition behind the filter and prove it sound, or replace it by an exact certificate. The modular-splitting test I used is simple to describe and sound, and it reproduces the paper's counts.

**M3. The PTE side is positioned with too little of its own literature, and several "known" statements rest on an unrefereed survey and a 1961 note.**

- **Location.** Sections 1.2 and 3.3; Example 3.13; Problems 1-4; the reference list.
- **Issue.**
  - The equivalence "N(k) = O(k) iff f is linear" is set against N(k) <= k(k+1)/2+1 and "Wright's improvement (k^2+4)/2", the latter via a 1961 note. No modern source for the state of upper bounds is given.
  - The classical and computational literature for the problem actually studied (odd-exponent equal sums, symmetric solutions, multigrade chains, GPTE types (-1,1,3,...)) is reached only through Chen's 368-page arXiv preprint.
  - There is no heuristic discussion of T(L). Is T(L) = 2L+2 plausible for large L? What do N(k) = k+1 for k <= 9 and k = 11 suggest? The reader cannot judge what the "open" statements mean.
- **Resolution.**
  - Add the original sources: Wright, Hua and Wooley for the quadratic bounds and Vinogradov-type counting; Letac and Borwein-Lisonek-Percival for ideal solutions; Gloden or Dorwart-Brown for odd multigrade chains.
  - State what is known for odd-exponent systems.
  - Add a short data-driven discussion of T(L).
  - Reduce reliance on the survey.

## 5. MINOR issues

- **m1. Attribution of "N(k) <= (k^2+4)/2".** Melzak writes the strict inequality and attributes it to Wright, calling it the best known in 1961. Cite Wright (1935) directly, keep the strict inequality, and give a post-1961 source for "no bound o(k^2) is known". Location: Thm 3.10 discussion, [32].
- **m2. Unrefereed sources for data.** A.685-A.692, identity (3.27), the ideal-type lists and the (-1,1,3,5) identity all come from [20] (arXiv v1). The paper does recompute the witnesses; say so in the text, and cite the original discoverers.
- **m3. Figure 3 marker key.** The caption does not say that diamonds are the genus, equal-count and cone-count pairs and squares are the Prouhet pairs. Say which Table S1 kind each marker denotes.
- **m4. Problem 4 versus Problem 2.**
  - Problem 4 for n = 5 is exactly the balanced case of T(4) = 10. In general it is the balanced case T(n-1) = 2n.
  - In Chen's notation it asks for an ideal solution of type (-1,1,3,...,2n-5), for which his classification (about 296 types) has no entry at n = 5.
  - The paper should say so, since this gives readers the right literature handle.
- **m5. Strength of the n = 5 evidence.** Orders up to 120 is very small next to the n = 4 witnesses (smallest max order 84, typical 100-400) and next to comparable ideal solutions. Chen's A.266 of type (1,3,5,7) has orders up to 55, and type (-7,-5,-3,-1) needs 9-digit numbers. "No witness at most 120" is almost no evidence about existence. The text calls the problem open, but should add a count heuristic or not emphasise the bound (Remark 3.2).
- **m6. Undefined vocabulary.** "Pencil of quartics", "witness" and "primitive" are used in Remark 3.2 but defined only in the supplement.
- **m7. Sharpness of Thm 3.8.** The bound |iota| <= |Z| - 2L is attained at L = 2. Say whether it is expected to be sharp for L >= 3; the open size-8 case of Remark 3.14 is exactly where it is not known to be sharp. Also note that the bound does not depend on N(k).
- **m8. Constants.** The factors 6, 4 and N(2L-3) <= 2L^2 are all non-optimal. Add "(constants not optimised)" next to the explicit bounds in Thm 1.1(ii).
- **m9. Additive constant in Prop 3.12.** The bounds (pi/2)(T-8) <= Amin(L) < 2 pi T carry an additive constant. "f is, up to constants in A, the inverse of T" therefore holds only for large L.
- **m10. "Ideal" for T(L).** "Ideal configuration" and "imbalance" should be defined where first used, and tied once to genus difference.
- **m11. Typography.** Cosmetic only: in Fig. 2(a) the tick labels "-3" and "-2" are very close. I checked the rendered pages at 130-400 dpi. The signs, the T(L) table and Figures 2 and 3 are correct. The "¡" characters seen in plain-text extraction are an artefact of the minus glyph, not an error in the PDF.

## 6. Presentation

The paper is long (48 pp. plus a 15-page supplement) but well organised. The PTE material sits in Sections 3.1-3.3 and Appendix A, and the roadmap is useful. The PTE statements are precise and the proofs I checked are tight. The key objects (configuration, imbalance, T(L), Amin) are introduced in a sensible order, and Figure 2 conveys the mirror argument well.

Improvements to make:

- add a short "known versus new" summary for the PTE side in Section 1.2, where it is now spread over several paragraphs;
- define the Remark 3.2 vocabulary in the main text (m6);
- make the T(L) table self-contained by citing a construction per entry (M1);
- give Figure 3 a marker legend (m3).

The English is clear and the references are consistent. The data statement is specific, and the supplement lists the exact searches, which made my independent recomputation possible.

## 7. Recommendation

**Minor revision**, with about 70% confidence, judged on the PTE and equal-power-sum content only.

I found no mathematical error. All my exhaustive recomputations reproduce the paper's numbers exactly. They cover the n=4 search to 440, the n=5 search to 120, the (3,5) search to 220, the triangle claims, the 525 classes, all explicit pairs, and the Prouhet squares for L = 4..6. The weaknesses are in exposition and provenance, not in correctness.

| Issue | What resolves it |
|---|---|
| M1 | State the construction behind each T(L) upper bound for L = 4..7 and the genus pairs, including how rho(c) = 0 is achieved. Fix the A.1.33 attribution. State what was searched for T(4) <= 12. |
| M2 | State the filter's exact criterion in Remark 3.14 and replace "rigorous inclusion disks" by a provably sound or exact certificate. The modular-splitting test of item 16 works. |
| M3 | Add classical and recent PTE sources for the bounds and odd multigrades, a short heuristic discussion of T(L), and less reliance on Chen's unrefereed survey. |
| m1-m11 | The local fixes listed above. |

From my side, acceptance hinges on M1 and M2 only. Provided the spectral sections are sound, I would support acceptance after these revisions.

**Report path:** I could not create `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-3/d-pte-combinatorialist/REPORT.md`; the complete report text is above.
