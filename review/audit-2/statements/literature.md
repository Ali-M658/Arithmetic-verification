# G5-bis audit: statements under review, group `literature`

Literature: every attribution a PTE theorem depends on

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.



## Context files you may read (previously audited statements, no proofs)

- (none)

## External inputs

- Fetched sources are in review/audit-2/sources/ (run fetch_sources.sh; unreachable files are instrument gaps). You may also read the raw fetched source files of theory/pte/sources/ (the *.pdf, *.txt, *.htm files listed in theory/pte/sources/SHA256SUMS) but NOT theory/pte/sources/NOTES.md, theory/pte/LITERATURE.md or any other file of theory/pte. Where the same document exists in both places, check the hashes agree or note that they do not.
- Borwein-Ingalls (e-periodica, L'Enseignement Math. 40 (1994) 3-27), Borwein-Lisonek-Percival (Math. Comp. 72), Melzak (Canad. Math. Bull. 4 (1961)), Wooley and Chen's web pages must be re-fetched by you or copied from theory/pte/sources with a hash check; record every HTTP result. No browser.

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.


## Group: literature

### LIT.0. The attribution claims (composed table, see below)

Source: generated (literature) (verbatim).

Each claim says: *a statement S is made by source X at the stated place*. Verify S against the fetched text of X:
exact wording, exact hypotheses (degree versus size, k versus k+1, integers versus rationals, 'ideal' versus
'symmetric'), exact place (page, proposition, entry number). Grade each claim CONFIRMED / CONFIRMED WITH CORRECTION
(give the correction) / NOT FOUND / CONTRADICTED / SOURCE UNREACHABLE. A claim that is a *negative* statement
(for instance 'no bound o(k^2) is known') is graded against the most recent sources you can fetch.

Notation used by the paper: [A] =_k [B] means two distinct multisets of integers of a common size n with equal power sums
P_j for j = 1..k. N(k) is the least such n. A solution is ideal if n = k+1. Degree k, size n.

Where a PTE theorem of the paper uses the claim is given in brackets.

**Borwein-Ingalls, 'The Prouhet-Tarry-Escott problem revisited', L'Enseignement Math. (2) 40 (1994) 3-27**
- B1. Defines N(k) as the least size of a solution of degree k (p. 6) [all of section 4].
- B2. Proposition 1 of that paper [state what it says; the paper cites 'Props. 1-3'].
- B3. Proposition 2: N(k) >= k+1 [Lemma 1.5(3), Theorem 4.2].
- B4. Proposition 3: N(k) <= k(k+1)/2 + 1, proved by pigeonhole [Lemma 1.5(2), Theorem 3.4, Theorem 4.2(b)].
- B5. p. 7: the bounds of Wright [22] and Melzak [15] are 'slightly stronger' and only improve to
  N(k) <= (k^2-3)/2 for k odd and N(k) <= (k^2-4)/2 for k even [remark after Theorem 4.2].
- B6. p. 7: Hua's bound M(k) <= (k+1)(log((k+2)/2)/log(1+1/k) + 1) ~ k^2 log k concerns the exact-degree quantity M(k)
  (degree exactly k), of order k^2 log k [context only].
- B7. Section 6, problem 3: 'Prove N(k) <= o(k^2)' is listed as open, and the paper says no progress has been made
  'for many years'; also 'The big prize is to find ideal solutions of all degrees' [Theorem 4.2 and the Remark on exponents].
- B8. p. 8: the definition of an odd symmetric solution: sum alpha_i^j = 0 for j = 1,3,5,...,k-1 (with B = -A)
  [Proposition 2.3(a) uses 'odd ideal symmetric solution of size 2L-1'].
- B9. p. 6, Lemma 2: the Prouhet step [A]=_k[B] implies [A, B+M] =_{k+1} [A+M, B] [context].
- B10. p. 9 table and p. 25: the explicit symmetric ideal solutions: size 4 {+-3,+-11}/{+-7,+-9}; size 6 {+-4,+-9,+-13}/{+-1,+-11,+-12};
  size 8 {+-2,+-16,+-21,+-25}/{+-5,+-14,+-23,+-24}; the perfect 7-set {-51,-33,-24,7,13,38,50} (and four more); Letac's two 9-sets
  {-98,-82,-58,-34,13,16,69,75,99} and {-169,-161,-119,-63,8,50,132,148,174}; Letac's size-10 solution [witnesses, L=4,5].
- B11. p. 4: Prouhet's 1851 general solution ('n^{k+1} numbers separable into n sets') and Wright's 1959 account [context].
- B12. Proposition 4: rational points of x^2 y^2 - 13 x^2 - 13 y^2 + 121 = 0 give size-10 ideal symmetric solutions (Smyth) [context].

**Melzak, 'A note on the Tarry-Escott problem', Canad. Math. Bull. 4 (1961) 233-237**
- M1. Records Wright's bound K(n) <= (n^2+4)/2 as the best bound known so far (pp. 233-234); state what n and K(n) mean there and
  whether this is the same bound as B5 (translate degree/size conventions carefully).
- M2. Table 1 (p. 237) gives individual numerical upper bounds for n <= 29; no asymptotic improvement.

**Wooley**
- W1. Ann. of Math. 175 (2012) 1575-1627 ('Vinogradov's mean value theorem via efficient congruencing'), Theorem 1.3: W(k,h) <= k^2 + k - 2 (the hypotheses on h).
- W2. Proc. LMS 118 (2019) 942-1016 ('Nested efficient congruencing and relatives of Vinogradov's mean value theorem'), Theorem 13.1:
  W(k,h) <= k(k+1)/2 + 1. State what W(k,h) is and whether W(k,2) is N(k) or the exact-degree M(k).

**Croot-Mao-Yip, arXiv:2609.05061** (p. 1)
- C1. 'Using a pigeonhole principle argument one can easily see that P(k,m) <= k(k+1)/2+1', with P(k,2) = N(k).
- C2. 'It is an open problem to determine if P(k,2) = k+1; it is only known that P(k,2) = k+1 when 2 <= k <= 9 and k = 11.'
- C3. The paper names no bound on N(k) better than quadratic [the most recent source the paper cites].

**Coppersmith-Mossinghoff-Scheinerman-VanderKam (CMSV), arXiv:2304.11254, Math. Comp. 93 (2024) 2473-2501**
- D1. p. 2: 'Ideal solutions in the PTE problem over Z are known for n <= 10 and n = 12' (n is the size); size 11 is open.
- D2. 'No new integral solutions are found for 9 <= n <= 16' [searches].
- D3. The size-12 solution of Kuosa-Meyrignac-Chen (1999), +-{22,61,86,127,140,151} / +-{35,47,94,121,146,148} (CMSV (5)); Letac's two 9-sets (CMSV (3)).
- D4. Consistency: D1 and C2 describe the same set of ideal solutions (size n <-> degree k = n-1).

**Borwein-Lisonek-Percival, 'Computational investigations of the PTE problem', Math. Comp. 72 (2003) 2063-2070**
- P1. p. 2063: 'Parametric ideal solutions are known for n = 1,...,8 and n = 10'.
- P2. p. 2064: Gloden's two-parameter family of size 7; p. 2069: Letac's 9-sets and two further size-10 solutions
  +-{71,131,180,307,308}/+-{99,100,188,301,313} and +-{18,245,331,471,508}/+-{103,189,366,452,515}.

**Chen Shuwen, 'A survey of the Prouhet-Tarry-Escott problem and its generalizations', arXiv:2506.11429 (2025), and eslpower.org**
- S1. Appendix A.1.6, A.1.17, A.1.26, A.1.33 (equal sums of odd powers, exponents 1,3,...,2L-3 for L = 3,4,5,6):
  [1,5,5]=[2,3,6]; [1,13,17,23]=[3,9,21,21]; [3,19,37,51,53]=[9,11,43,45,55]; [7,91,173,269,289,323]=[29,59,193,247,311,313].
  Check that each entry number is the one that lists exactly this solution, its exponent set, and the stated attributions
  (A.48 'smallest solution by computer search' for [1,5,5]=[2,3,6]; Moessner 1939; Gloden; Xeroudakes-Moessner; Lander;
  Choudhry; Chen 2000 = A.313; Wroblewski 2009 = A.314-A.316, three further non-negative solutions and one with a negative entry).
- S2. eslpower.org, Theorem 3 (page TarryPrb.htm): if [a_1..a_m] = [b_1..b_m] for k = 1,3,...,2n-1 then
  [T+a_i, T-b_i] = [T+b_i, T-a_i] for k = 1,2,...,2n [Proposition 2.2 is attributed to this lifting].
- S3. Negative exponents (survey section 1.4 and Appendix A.5): '33 distinct types with k_1 < 0 and k_n > 0'; type (-1,1): [4,10,12]=[5,6,15];
  type (-1,1,3): [3,10,15,30]=[4,5,21,28] (A.685); type (-1,1,5): [81,374,585,891]=[85,286,702,858].
- S4. The type (-1,1,3,...,2L-3) for L >= 4 does not appear in the survey, and neither does an unequal-size version [negative claim; the paper
  says its system is 'not tabulated'].
- S5. Non-symmetric ideal solutions have been discovered only for degrees n <= 7 (survey p. 13) [context].
- S6. A.1.21, A.1.35: Chernick's two-parameter symmetric families of sizes 5 and 7 [context].

**Others**
- O1. Caley (arXiv:1011.1262, p. 2): the k log k statement concerns the 'easier Waring' number v(k), not N(k) [so it is not a bound on N(k)].
- O2. Choudhry (arXiv:2207.12726, 2022): polynomial parametrisations are counted 'only when k <= 7'; and BLP's 'parametric' (P1) means something
  different [context].
- O3. Prouhet-Thue-Morse: nothing to check beyond B11.
- O4. The statement 'No retrieved source contains an O(k log k) bound for N(k)': search the fetched texts and the web (arXiv listing, Semantic Scholar)
  for any bound N(k) = o(k^2) published after 1994 and report what you find. This is the adversarial search for the 'open problem' claim:
  a single counterexample makes Theorem 4.2's commentary and Remark (What the exponent means) wrong.

