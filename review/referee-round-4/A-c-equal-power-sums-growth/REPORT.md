<!-- Saved verbatim by the main session from the reviewer's returned text: the harness refused the reviewer's own write. Scripts and logs it cites are in its git-ignored scratch/. -->

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (Annals of Global Analysis and Geometry)

**Referee's area:** analytic and computational number theory, equal power sums (Prouhet–Tarry–Escott (PTE), ideal and symmetric solutions, N(k)).
**Charge:** (1) the growth results, meaning the lower and upper bounds on the area dependence f(A) and their relation to PTE (Theorem 1.1(ii), Section 3.4, Proposition 3.14, Appendix A); (2) Theorem 3.7 (bounded cone orders), including whether its bounds are sharp, checked by my own computations. I read the rendered pages 1, 3, 14–19 and 33, plus the full extracted text of the manuscript and the supplement. The placeholders (author contributions, AI-use statement, Zenodo DOI) are treated as known and are not counted against the paper.

## Summary

The paper considers closed orientable hyperbolic 2-orbifolds with cone points. It asks how many heat invariants c_1, …, c_k determine the signature (g; m_1, …, m_n). At curvature −1, c_j adds one odd power sum P_{2j−3} of the cone orders to the area and to R = Σ 1/m_i (Lemma 2.10). So comparing two orbifolds becomes an odd-power PTE system with a reciprocal constraint. The results in my remit are:

- **Corollary 3.5.** The first ⌊A/π⌋+4 invariants always suffice.
- **Theorem 3.13 / Theorem 1.1(ii).** f(A) := max K_mult over area ≤ A satisfies c√A ≤ f(A) ≤ A/π+4. For 0<α≤1, f(A) ≥ cA^α holds if and only if N(k) = O(k^{1/α}). In particular f is linear if and only if N(k) = O(k).
- **Proposition 3.14.** The minimal configuration size T(L) is within constant factors of N.
- **Theorem 3.7.** Inside Sig_{≤M}, M invariants suffice and M−1 do not. Against all of Sig, an orbifold with orders ≤ M needs at most M + ⌈½ log(2⌊A/π⌋+8)⌉ invariants.

## Significance

Recasting "how many heat invariants" as an odd-power PTE problem with a reciprocal side condition is natural and cleanly done. The growth equivalence (Theorem 3.13(d)) is stated honestly: it is a genuine two-way equivalence with the open question N(k) = O(k), not a mere "relation". The paper does not claim more than it proves about N. From the number-theoretic side the content is modest. The lower bound is a pigeonhole argument (Lemma A.1) followed by the doubling trick (Proposition 3.11), and Proposition 3.14 shows the geometric problem is the PTE problem up to constants. That is useful precisely because it shows the geometry adds nothing to the growth question.

Theorem 3.7(i)–(ii) is the sharpest and most satisfying statement in my remit. However, its "against all orbifolds" part (iii), which the abstract and Theorem 1.1(iii) use to say that growth "is carried by large cone orders", is not sharp. An elementary sign-change argument replaces M + ⌈½ log(…)⌉ by M+1, and M+1 is attained (M1). This strengthens the authors' message, but the headline statements have to change.

## Correctness and what was recomputed

All computations are in `scratch/`, in exact rational arithmetic (Python `fractions`, with `sympy` used only for Bernoulli numbers and the series of u/sin u). No package was installed. Output logs are `scratch/out_*.txt`.

1. **Cone polynomials, independently re-implemented** (`heat.py`, from (4)–(5)). The values of α_0..α_4 and p_0, p_1, p_2 match (7).
   - Lemma 2.8 checked for l < 12: the leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)), p_l(1)=0, evenness, and positivity at sampled m > 1.
   - Formula (9) checked on four triads.
   - d_3, d_4, d_5 = 25/12, −1775/24, 153025/48 (Section 7) reproduced. c_3(2,8,8) = −1601/480 and c_3(3,3,12) = −867/160 agree with Table S6.
   - Independent numerical check (`check_Em.py`, mpmath, 40 digits): E_m(t) from the integral of Theorem 2.3 agrees with Σ_{l≤5} b_l(m)t^l for m = 3, 5, 8. The residual scales like t^6, as it should.
2. **Theorem 3.7(ii), M = 2, …, 9** (`thm37.py`). I recomputed w_a, the least C, ν(a), s, the least genus, both signatures and the areas. In every case:
   - the two signatures are distinct and have equal area;
   - they share exactly c_1, …, c_{M−1};
   - c_M(g;m) − c_M(g+s/2;m') = (−1)^M C a_{M−2} exactly, with the stated sign.

   The M=3 and M=4 examples on p. 15 are reproduced exactly: (1;3^9)/(0;2^16) of area 12π, and (0;2^28,4^8)/(1;3^27) of area 36π. Areas/2π for M = 2..9 are 2, 6, 18, 190, 442, 3998, 8838, 77054.
3. **Minimality claim on p. 15, recomputed** (`minarea.py`). I exhaustively enumerated every signature with orders ≤ M and area ≤ the claimed minimum and grouped them by (c_1, …, c_{M−1}).
   - For M = 3 and M = 4, the least-area collision is exactly the paper's pair (12π and 36π), as claimed.
   - The M = 2 remark ((0;2^5) and (1;2) share c_1) is confirmed.
   - For M = 5..8 I used the fact, from the proof of (i), that the kernel is 1-dimensional and that ν_0 is primitive (gcd 1 in all cases). Searching over multiples, genera and small common add-ons, the construction of (ii) again has the least area. This is a structured search, not an exhaustive one.
4. **The sharp form of 3.7(iii)** (M1; `signchange.py`):
   - (a) For M = 2..7, exact heat coefficients show orbifolds O ∈ Sig_{≤M} sharing exactly M invariants with some O' ∈ Sig, so K_mult(O;Sig) = M+1 is attained. One example is (0;2^10) against (1;4,4,4,4), of area 6π.
   - (b) A brute-force sanity check over all 24,701 signatures with orders ≤ 24, genus ≤ 2 and area ≤ 4π found no violation of K_mult(O;Sig) ≤ M+1.
5. **All 20 explicit pairs of Table S1** (`tableS1.py`, parsed from the supplement text). For every pair I recomputed exactly:
   - the area;
   - the exact number L of shared invariants, via power sums with Lemma 3.3, and for L ≤ 4 also via the heat coefficients themselves;
   - |U*|+|V*|.

   Everything agrees with Table S1, with Example 3.16, and with the T(L) table on p. 19 (upper bounds 14, 18, 24, 40). Theorem 3.4 (|U*|+|V*| ≥ 2L+2) holds in every case. The sign-change inequality of M1 also holds in every case (`out_signs.txt`), and it is attained, for example by (1;15,15,15) against (0;3,3,5,7,7,21).
6. **Proofs checked by hand.** I checked the following line by line and found them correct:
   - Lemma A.1: the count n^{L−1}M^{(L−1)^2} < M^n/n!.
   - Proposition 3.11: the identity P_j(U) − P_j(V) = (1−2^{j+1})(P_j(X)−P_j(Y)) including j = −1, hyperbolicity for n = 2, and distinctness via 2x*.
   - Proposition A.2: the imbalance formula.
   - Theorem 3.13(a)–(d): the floor and threshold arithmetic, and N(2L−3) ≤ 2L².
   - Proposition 3.14: the passage to the infimum, and N(2L−2) ≤ T(L) via (Z, −Z).
   - Theorem 3.7(i)–(iii): the Vandermonde determinant, the Lagrange-weight identity, and the inequality 2M+(k−3)(k+1) > 0.
   - Theorem 3.12.

   Spot checks: Theorem C(3) power sums, Example 3.6 (Ψ_1 = 224/15, area 2π·14/15), and the partner triple of {1,1,1,1,7} in Remark 3.17.
7. **Literature** (saved in `scratch/lit/`).
   - Borwein–Ingalls [5], author's preprint: Proposition 3 (N(k) ≤ ½k(k+1)+1), the quadratic bounds and Hua's M(k) ≲ k² log k (p. 5), and Problem 3 "Prove N(k) ≤ o(k²)" with "No progress on questions 3 and 4 has been made for many years" (pp. 25–26) are all as cited.
   - Croot–Mao–Yip [37] confirm that the best general bound on Wright's W(k,2) is Wooley's k(k+1)/2+1. So "all known bounds on N(k) are quadratic" is correct.
   - Caley's thesis attributes the ½(k²−3), ½(k²−4) bounds to Melzak (see m1).

**Verdict on my charge.** Every growth statement is correct as stated. Theorem 3.7(i) and (ii) are correct, and (ii) is sharp in the sense claimed. Theorem 3.7(iii) and Corollary 3.8(b),(c) are correct but far from sharp (M1). I found no mathematical error in the material under my charge.

## MAJOR issues

**M1. Theorem 3.7(iii), Corollary 3.8(b),(c), Theorem 1.1(iii) and the abstract: the logarithm is unnecessary. The sharp bound is M+1, independent of the area.** (Pages 1–3, 14–15 and 17; Section 3.3.)

*Claim.* Let O ∈ Sig_{≤M} and let O' ∈ Sig have a different signature and share c_1, …, c_L with O. Then L ≤ M. Hence K_mult(O;Sig) ≤ M+1 for every O ∈ Sig_{≤M} and every area. This bound is attained for every M ≥ 2.

*Proof.* Take the paddings U, V of Lemma 3.3 and put μ(x) = mult_U(x) − mult_V(x) on the positive integers. μ ≢ 0, since otherwise the signatures agree. Let ν be the signed measure placing mass μ(x)/x at y = x². By (13),

Σ ν(y) y^k = Σ μ(x) x^{2k−1} = 0 for k = 0, 1, …, L−1,

where k = 0 is the reciprocal sum. A finitely supported nonzero signed measure that annihilates all polynomials of degree ≤ L−1 has at least L sign changes along its ordered support. Otherwise, a polynomial of degree ≤ L−1 with roots between the sign blocks has the sign of ν on its support and pairs positively with ν. This is Laguerre's/Descartes' rule, as in Steinig [16].

Every support point x > M comes from cone orders of O' only, so all such points have the same sign. Hence the number of sign changes is at most #(supp μ ∩ [1,M]) ≤ M, and therefore L ≤ M.

If O' is also in Sig_{≤M}, the same count gives at most M−1 sign changes. That is Theorem 3.7(i), with a one-line proof.

*Sharpness.* Take the pair of Theorem 3.7(ii) at level M+1. Its side that does not contain the order M+1 lies in Sig_{≤M} and shares exactly M invariants with the other side. I verified this exactly for M = 2..7 (`out_signchange.txt`): for example (0;2^16) against (1;3^9), and (1;3^27) against (0;2^28,4^8). A smaller instance for M = 2 is (0;2^10) against (1;4^4), of area 6π.

For this last example the paper's bound gives 2 + ⌈½ log 20⌉ = 4, while the truth is 3. Since 2⌊A/π⌋+8 ≥ 8, the paper's ⌈½ log(2⌊A/π⌋+8)⌉ is always at least 2. So the paper's bound exceeds the truth by at least one for every area, and by more as the area grows.

*Consequences that must be changed:*
- **Corollary 3.8(b).** It becomes: K_mult(O;Sig) ≥ L+1 implies that the largest cone order of O is at least L, with no area term.
- **Corollary 3.8(c).** It becomes: f_M(A) ≤ M+1 for all A, with equality once A is at least the area of the low side of the level-(M+1) pair. The p. 17 sentence "with orders at most M the count grows at most logarithmically in the area" is then wrong in spirit: the count is bounded.
- **Theorem 1.1(iii) and the abstract.** "M plus a logarithm of the area suffice" should read "M+1 suffice, and M+1 is attained".

The same count gives a second area-independent bound worth stating: L ≤ 2d_O + 1, where d_O is the number of distinct cone orders of O. The reason is that each block of O-side points creates at most two sign changes, and the padding block at x = 1 creates at most one. Hence K_mult(O;Sig) ≤ 2d_O + 2. This bound is attained by (1;15^3) against (0;3,3,5,7,7,21). It says that large K_mult needs many *distinct* orders, not only large ones, which fits the paper's narrative.

The first claim of Theorem 3.7(iii), which bounds the orders of O', remains of independent interest. Theorem 3.7(i)–(ii) is unaffected.

## MINOR issues

- **m1. The quadratic bound on N(k) (p. 17, Section 3.4).** The paper attributes N(k) ≤ ½(k²−4) (k even) and ½(k²−3) (k odd) to Wright [32] "as reported in [5, p. 7]". [5] does print these bounds, but without attribution to [32]; it says they are "discussed in [22] and [15]". Caley (PhD thesis, Waterloo 2012) attributes them to Melzak (1961). As printed, the bounds are false for k = 2, 3: they give 0 and 3, while N(k) ≥ k+1. So they hold only for k beyond some point. Please check the primary source, attribute the bound correctly, and state its range of validity. The results are unaffected.
- **m2. "for many years" (p. 17).** This quotes a 1994 statement. Date it ("as of 1994"), and add that later surveys ([20], [37]) record no subquadratic bound. Croot–Mao–Yip state that Wooley's k(k+1)/2+1 is the best known bound for Wright's W(k,2).
- **m3. "The true growth exponent, between ½ and 1, is open" (Theorem 1.1(ii), p. 3).** f need not have an exponent. Please say "liminf/limsup of log f/log A". Proposition 3.14 also gives the converse direction, which the paper does not state: a lower bound N(k) ≥ ck^{1/α} gives f(A) = O(A^α), via A_min(L) ≥ (π/2)(T(L)−8) ≥ (π/2)(N(2L−2)−8). In particular f(A) = o(A) if and only if N(k)/k → ∞. Stating both directions would make "f is the inverse of N up to constants" precise.
- **m4. Proposition 3.14 (p. 17).** The upper bound T(L) ≤ 6 min((L−1)²+1, N(2L−3)) can be tightened to T(L) ≤ min(6((L−1)²+1), 4N(2L−3)). The genus construction in the proof of Theorem 3.13(c) already gives |Z| ≤ 4N(2L−3). The factor 6 is needed only for the pigeonhole branch, because Proposition A.2 requires all powers, not only odd ones.
- **m5. Theorem 3.7(ii) "M cannot be lowered" (pp. 14–15).** Sharpness holds only at very large areas: area/2π = 2, 6, 18, 190, 442, 3998, 8838, 77054 for M = 2..9, which I computed. Below these areas, K_mult(O;Sig_{≤M}) ≤ M−1. Please state the areas, and the (verified) fact that for M = 3, 4 they are the least possible. My structured search suggests the same for M = 5..8, given that the kernel is one-dimensional with primitive generator. Say whether you claim this.
- **m6. "log" (Theorems 1.1(iii) and 3.7(iii), Corollary 3.8).** "log" is never defined. The proof uses log(1+y) ≥ 2y/(2+y), so it is the natural logarithm. If M1 is adopted this point disappears.
- **m7. Corollary 3.8(b) (p. 15).** "Its largest cone order" is undefined when O has no cone points. Also, in Theorem 3.7(iii) the hypothesis "L ≥ 2" belongs to the first assertion only.
- **m8. Notation clash (Appendix A, p. 33).** In Lemma A.1, M denotes the size of the box {1, …, M}, which clashes with M as the cone-order bound in Section 3.3. Theorem 3.7(iii) also bounds |U| by 2⌊A/π⌋+8, whereas the proof of Corollary 3.5 gives |U| ≤ ⌊A/π⌋+4.
- **m9. The T(L) table header on p. 19.** "2L+2 ≤ T(L)" and "T(L) ≤" are row labels, which read oddly. Label the rows "lower bound (Thm 3.4)" and "upper bound (Example 3.16)".

## Presentation (figures and captions included)

- The growth section is dense but logically ordered. Definitions of f, f_g, f_n, T, T_g and A_min are scattered over pp. 2, 17, 18 and 20; a short notation table would help.
- **Figure 3 (p. 19).** It is readable, and its caption states the open gap correctly. If M1 is adopted, the text near it should say that the bounded-order count is ≤ M+1.
- **Figure 2 (p. 14).** It is clear and correctly labelled. Its colour coding is explained in the text, not in the caption; the caption should say which colour is which orbifold.
- **The abstract (p. 1)** runs onto p. 2, and its mathematics is set in bold. This is a template artifact.
- **Supplement Table S1.** Several areas are given only as floats such as "5 − 3.27×10^{−11}", with exact values deferred to a data file. My exact recomputation matches them, but the exact rationals should be printed for at least the L ≤ 5 rows.

## Recommendation

**Major revision**, from the perspective of my charge. Confidence: high on the mathematics, moderate on the editorial weight. Nothing I checked is wrong. But one headline statement (abstract, Theorem 1.1(iii), Theorem 3.7(iii), Corollary 3.8) is superseded by a short, sharp, area-free bound that the authors should adopt. The growth/PTE equivalence is correct and honestly stated. Theorem 3.7(i)–(ii) is correct and sharp as claimed, verified for M up to 9, with minimal areas verified exhaustively for M = 3, 4.

## What resolves each issue

- **M1:** Replace Theorem 3.7(iii) by "K_mult(O;Sig) ≤ M+1 for O ∈ Sig_{≤M}, attained" (keeping the bound on the orders of O' if desired), using the sign-change proof above or an equivalent one. Then:
  - revise Corollary 3.8(b),(c), Theorem 1.1(iii), the abstract, and the sentences on pp. 5 and 17;
  - optionally add the bound K_mult(O;Sig) ≤ 2d_O + 2;
  - cite the classical Descartes/Laguerre sign rule for measures (for example Steinig [16] or Pólya–Szegő).
- **m1:** Verify Wright [32] and Melzak (1961), correct the attribution, and give the range of k for which the bound holds.
- **m2:** Date the quote and cite the later surveys.
- **m3:** Reword the "exponent" sentence and add the converse direction from Proposition 3.14.
- **m4:** Replace 6N(2L−3) by 4N(2L−3), citing the proof of Theorem 3.13(c).
- **m5:** List the sharpness areas, and state precisely what minimality is proved or computed.
- **m6:** Define log as the natural logarithm, or drop it under M1.
- **m7:** Handle O without cone points in Corollary 3.8(b), and attach "L ≥ 2" to the first claim of Theorem 3.7(iii).
- **m8:** Rename the box size in Lemma A.1, and use |U| ≤ ⌊A/π⌋+4.
- **m9:** Relabel the rows of the T(L) table.
- **Presentation:** Add the colour key to the Figure 2 caption, print exact areas in Table S1 for L ≤ 5, and fix the abstract layout.
