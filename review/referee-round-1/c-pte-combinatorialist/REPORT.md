*Provenance: the reviewer subagent could not write files ("Subagents should return findings as text"); this is its returned text, saved verbatim by the orchestrating session.*

RECOMMENDATION: MINOR REVISION (confidence 0.8 on correctness of what I could check; 0.5 on fit/significance for JGA).
MAJOR issues: none established. I found no genuine error in the PTE-related mathematics or in any exact computation I could redo. Two near-major framing items are listed as m1 and m2 and should be fixed before acceptance.

NOTE: my attempt to write /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-1/c-pte-combinatorialist/REPORT.md was refused by the tool layer ("Subagents should return findings as text"), so the full report is below. My scratch code and outputs are in .../c-pte-combinatorialist/scratch/.

======================================================================
REPORT: "How much of a hyperbolic orbifold does heat hear?" (Gang et al.), Journal of Geometric Analysis
Referee C (combinatorics / PTE). Read only manuscript.pdf and supplement.pdf. The marked placeholders were treated as known.

## 1. Summary of the paper

For a closed orientable hyperbolic 2-orbifold with signature (g; m_1..m_n), the heat invariants c_j depend only on the area and on the cone orders. The area enters through c_1 = Area/4pi and a universal sequence alpha_k. Each cone point enters through an explicit even polynomial p_l(m)/m. The coefficients are derived from the Selberg trace formula with a self-contained admissibility lemma (Sect. 2, Prop. 2.8). The key observation (Lemma 2.11) is that c_{l+2} brings in exactly one new odd power sum P_{2l+1}. It does so in the combination Psi_k = P_{2k-1} - R, with R = sum 1/m_i.

"First L heat invariants agree" is therefore equivalent to "equal area and Psi_k(m) = Psi_k(m') for k < L". This is a moment problem for the signed multiset m (+) (-m').

Main results:
- **Thm A, Thm 3.4, Cor 3.5.** A Newton-identity parity argument shows n invariants determine the cone orders of a sphere with n cone points. In general, two different signatures sharing H_L force |U*|+|V*| >= 2L+2, so floor(Area/pi)+4 invariants determine genus and cone orders.
- **Thm 3.10, 3.11.** No area-independent number exists. With f(A) the worst-case number needed up to area A, the paper proves a sqrt-type lower bound (pigeonhole plus a "doubling" trick that makes R free) and the upper bound A/pi+4. It also proves: f(A) >= cA^alpha for all large A iff N(k) <= C k^{1/alpha}, where N(k) is the least size of a Prouhet-Tarry-Escott solution of degree k. In particular f is linear iff N(k) = O(k).
- **Thm 3.8** (a Descartes bound |iota(Z)| <= |Z|-2L) and the open case T_3 in {8,10}.
- **Thm 1.2 (Sect. 5).** For triangle orbifolds the first two invariants are equivalent to (R, S_1 = p+q+r).
  - They separate all triangle orbifolds of sum <= 17.
  - The minimal failure is O(2,8,8) ~ O(3,3,12) at sum 18.
  - Three invariants always suffice.
  - Collisions are rational points on (X+Y+Z)(XY+YZ+ZX) = Lambda XYZ.
  - For Lambda = 27/2 the elliptic curve has rank 0 and E(Q) = Z/2 x Z/6, so the minimal pair is isolated up to scaling.
- **Sect. 4.** Heat invariants depend only on the signature, so K_iso = infinity off triangle orbifolds. The paper gives an explicit bound |Z_1 - Z_2| <= C t^{-1/2} e^{-ell^2/4t} for two orbifolds of one signature, with exponent and prefactor attained.
- **Sect. 6.** A recovery map (triangular map, a Hurwitz-type linear system with det = prod(m_i+m_j)/prod m_i, then root finding) with perturbation estimates. These are Lipschitz at simple orders and Holder 1/k at k-fold orders. They are sharp for arbitrary data, and exponent 1/2 is sharp for realisable data at a double order or when all orders agree. Certificates for integer orders are included.
- **Sect. 7 and supplement.** Finite-element spectra for O(2,8,8), O(3,3,12) and a (0;3,3,3,3) family. These are not used in proofs.

## 2. Significance and novelty

**What is good.**
- The reduction to an explicit moment problem is clean and the extra datum per coefficient is identified correctly.
- Thm 1.1(i) is rigorous and gives a genuinely explicit uniform number.
- The equivalence with N(k) is correct in both directions (I re-derived all four implications). The doubling trick of Prop. 3.9 (X -> X (+) 2Y (+) 2Y makes the reciprocal sum agree automatically) avoids an exponential loss.
- The threshold 17 and the isolation of (2,8,8)/(3,3,12) are correct and checkable.
- The paper is honest about open problems (Problems 1-3, Remark 6.1, the status of the numerics).
- The trace-formula derivation of the coefficients is independent of Donnelly, DGGW and Ucar.

**Literature I verified (arXiv / Crossref / zbMATH Open).**
- Borwein-Ingalls, L'Enseign. Math. 40 (1994) 3-27, Zbl 0810.11016 is a PTE survey with open problems. It is the right source for N(k) >= k+1 and the quadratic upper bound. I did not check problem numbering or page-level attributions.
- Wooley, Proc. LMS 118 (2019) 942-1016 (arXiv:1708.01220), Thm 13.1: W(k,h) <= k(k+1)/2+1 for all k, the exact-degree variant. The manuscript's statement is correct. Wooley also notes ideal solutions are known for 2<=k<=9 and k=11.
- Croot-Mao-Yip, arXiv:2609.05061 (Sept 2026) exists. It treats Wright's variant in integral domains and restates that P(k,2)=k+1 is open and k(k+1)/2+1 is the best bound. It supports openness but does not address o(k^2) itself.
- Chen, arXiv:2506.11429: entry A.685 is exactly [3,10,15,30]^k = [4,5,21,28]^k, k=-1,1,3. I found no numerical 5+5-term example of type (-1,1,3,5) in the type list, consistent with the paper's remark. Ex. 2.36 uses four terms.
- The following exist with the bibliographic data given (Crossref): Coppersmith-Mossinghoff-Scheinerman-VanderKam (Math. Comp. 2024), Bremner-Guy-Nowakowski (1993), Korobov-Bugaevskaya, Melanova-Sturmfels-Winter, Laurens, Schueth (AGAG 69, 2026), Melzak (CMB 4, 1961), Philippe (Ann. Inst. Fourier 58, 2008).
- Philippe's theorem concerns (2,p,q) triangle groups only (title and abstract checked); see m4.
- Not verifiable: I could not retrieve the text of Melzak, Borwein-Ingalls or Hardy-Wright. So "Wright's improvement N(k) <= (k^2+4)/2 (1935)", the page numbers 233/234, and the problem numbering "[5, Problem 3/4]" are unverified.

**Limits of novelty.**
- Thm A repackages Steinig/Laurens/Newton parity, and the paper says so.
- "f linear iff N(k)=O(k)" is a correct exponent-level equivalence. The unconditional content is the sqrt(A) lower bound by pigeonhole. The gap between sqrt(A) and A is exactly the open PTE problem, so the growth question is relocated, not decided.
- Sect. 5 is a finite computation plus one rank-0 elliptic curve. Sect. 6 is polynomial-root perturbation theory. Sect. 7 is numerics. The collision arithmetic is partly deferred to a companion "in preparation" [20]. A geometric-analysis readership will mainly value Sect. 2-4.

## 3. Correctness, and what I recomputed

I re-derived by hand: Lemma 3.1, Thm A, Lemma 3.3, Thm 3.4, Cor 3.5, Thm 3.8, Prop 3.9, Thm 3.10, Thm 3.11(a)-(e), Prop A.2, Lemma A.1, Thm C(1)-(2). All hold.
- Thm 3.11(b): Z and -Z solve PTE of degree 2L-2, since even sums agree trivially and odd sums vanish up to 2L-3.
- Thm 3.11(c)/(d): they use only monotonicity N(k) <= N(k+1) and translation invariance.
- The genus construction (combine Z(c) with a rescaled Z(c') of imbalance 0 to kill the reciprocal sum) is correct.
- The pigeonhole count in Lemma A.1 gives n <= (L-1)^2+1, better by a factor of about 2 than Hardy-Wright for this odd-power system.

**Own computations** (Python/sympy/mpmath/Fractions and C, in my scratch folder):

1. **Witnesses (exact).**
   - {2,8,8} vs {3,3,12}: R=3/4, P1=18, P3=1032 vs 1782.
   - {3,10,15,30} vs {4,5,21,28}: R=8/15, P1=58, P3=31402, P5=25159618 vs 21298618.
   - {16,16,74,74} vs {11,37,44,88}: R=45/296, P1=180, P3=818640.
   - The splitting A={-30,-3,5,28}, B={-21,-4,10,15} of Remark 3.2 has e1=0 and equal e3, e4.
   - Examples 3.6 and 3.12(i),(ii): areas 2pi*14/5 and 2pi*22/15 confirmed, and (1;15) vs (0;3,3,5,5) share exactly c_1,c_2 with |U*|+|V*|=6.
   - (5,5,5) vs (2,2,2,10) share exactly two invariants.
   - Prop 3.9 with X={1,4}, Y={2,3} gives (0;4,4,4,6,6) and (0;2,2,2,3,8,8), with equal R and P1 and P3 = 1075 vs 625.

2. **Exhaustive searches.**
   - n=4, orders in [2,440]: 1,568,797,230 multisets, grouped by sum and sorted by (P3, hash of R mod 2^61-1), with all hits re-verified exactly. Result: 193 witness pairs and 107 primitive ones (as claimed), none with a common element.
   - Exactly 6 primitive witnesses admit no "pencil splitting". The smallest is (16,16,74,74)/(11,37,44,88), as stated. I tested all 4+4 splittings with e1=0 and equal e3, e4.
   - n=5, orders in [2,120]: 216,071,394 multisets (the paper's number), no collision of (R,P1,P3,P5), as claimed. Hash collisions could only create false positives, never hide a true collision.

3. **Pencil counts (Remark 3.2).** The counts "15 / 35 / 25 / 61" are NOT reproduced by my natural reading (A,B 4-multisets of nonzero integers, sum 0, equal e3,e4, A (+) (-B) with four entries of each sign, A != +-B). I get 17 distinct witnesses with entries <= 130 (14 primitive) and 49 (30 primitive) for <= 220. Counting (A,B) pairs I get 66 and 180. The definition needs to be made precise (m6).

4. **Remark 3.13 (T_3).**
   - Shape (3,5) is forced by Thm 3.8 (confirmed).
   - I searched all 5-multisets of positive integers with entries <= 220 (4,493,032,544 of them) for an integer 3-multiset V with the same P1, P3, R. I solved the cubic via e3 = (P3-e1^3)/(3-3 e1 R) in double precision and verified exactly. Result: no solution, matching the paper. The formula was checked on a planted example.
   - For {1,1,1,1,7} the partner V is unique, with roots 6.4506, 4.2830, 0.2664 (all positive). The paper's "three positive real partners" should read "a partner of three positive reals".

5. **Theorem B.** I built M from (11) with tanh and solved symbolically for (2,8,8), (3,10,15,30), (2,3,7,11,13). The solution equals the true e_k and det M = (-1)^{n(n+1)/2} prod(m_i+m_j)/prod m_i (12.5, 25740, -311040000/11). Confirmed.

6. **Heat coefficients.**
   - From (4)-(5) with sympy: p_0..p_3 match (7). alpha_0..alpha_4 = 1, -1/3, 1/15, -4/315, 1/315.
   - The supplement's d_3 = 25/12, d_4 = -1775/24, d_5 = 153025/48 are reproduced, and (9) is consistent with (7).
   - mpmath evaluation of the trace-formula elliptic term E_m(t) (m=3,5,12; t=0.01,0.02) differs from the 3-term series by an amount scaling like t^3 with the predicted b_3. So the closed form and the trace formula are consistent.
   - The Prop. 6.2 constants amp = 2, 14, 498, 4062, 56230/3 and P3 = -18c1-120c2-360c3 are reproduced from F^{-1}.

7. **Triangle orbifolds (Sect. 5), exact reduced fractions.**
   - No collision for sums 3-17. At 18 only (2,8,8)/(3,3,12). Next collisions at 20, 26, 31, ..., and the non-adjacent (5,15,15)/(7,7,21) at 35.
   - **Prop. 5.9 is fully reproduced.** For 18 <= S <= 4800, exactly the 38 listed sums are collision-free, the other 4745 collide, and S=557 has 25,575 triads.
   - Table S3 (S*(p) and first collisions, p=2..14) is reproduced exactly. The 83 triads of Table S4 were counted.
   - The shortest closed geodesics 2.2568 and 1.8626 of the supplement are reproduced from the reflection groups.

8. **Theorem 5.10.**
   - phi o psi = id on E (sympy). My reading of the garbled phi is -16 e_2/Z^2 and (8(X-Y)/Z)(-4 e_2/Z^2 - 54). It reproduces phi(1:4:4) = (-24,360).
   - C_{27/2} is nonsingular. The 12 listed points lie on it. disc E = 2^18 3^8 5^6. #E(F_7) = #E(F_11) = 12. The tangent y = 21x+64 meets E only at x=16 (triple).
   - Using my own local-solubility search (heuristic, not a proof), the 2-isogeny Selmer groups have sizes 4 ({+-1,+-6}) and 1, so rank 0. No PARI/Sage was available and I did not check a database.

9. **Section 6.** The first-term formula for delta_thm (Thm 6.8) reproduces four Table 1 entries: 3.803e-7 for (2,8,8); 1.189e-7 for (3,3,12) (printed 1.18e-7, rounded down as the caption says); 9.354e-7 for (4,4,4); 4.492e-7 for (2,3,7). Prop. 6.6(i) and the algebra of Remark 6.7 are confirmed.

10. **Lemma 2.6.** The key integral inequality was verified numerically (ratio <= 1 over a range of t and ell) and follows analytically because x/(-h') is decreasing. The constant C of (3) follows.

11. **Figure 2.** The caption's "525 area classes with s <= 7/5" is reproduced only by restricting to genus 0 and 1 signatures with ALL cone orders <= 12; this cutoff is not stated.
    - With that cutoff the exact K_mult histogram is 329 classes with K=1, 166 with K=2, 30 with K=3 (max 3), consistent with the dots, and the (2,8,8)/(3,3,12) class has K=3.
    - Area classes contain members of larger order: s=1/4 contains (2,5,20); s=2/5 contains (2,11,110).
    - My full-class (uncapped) recomputation did not finish, so I cannot say whether the cap changes any dot.

**Not recomputed:**
- the finite-element spectra, fits and error budgets (Sect. 7, S1-S3);
- delta_cert and delta_up, the ratios of Table 1, and Prop. 6.9 certificates;
- the Hadamard bound of Thm 6.4(a);
- the pairs of Example 3.12(iii) for L=4..7 (not written out; they rest on cited ideal symmetric solutions);
- the pencil counts (item 3);
- the texts of Melzak, Borwein-Ingalls, Hardy-Wright.

## 4. MAJOR issues

None established. I looked for them in particular in: the PTE equivalences (Thm 3.11), the doubling construction, Thm 3.4/3.8, the genus construction, Appendix A, and every number I could recompute. All checked out. See m1 and m2 for the two items I consider closest to major.

## 5. MINOR issues

**m1 (framing of the PTE equivalence; should be fixed).**
- Location: abstract; Thm 1.1(ii); Thm 3.11(b)-(d); Sect. 3.3.
- Problem: "linear iff N(k)=O(k)" is correct but reads as a classification of the growth rate in terms of a classical problem. The governing quantity is really T_L, the least size of a real L-configuration (Def. 3.7). T_L satisfies T_L >= 2L+2, a stronger constraint than PTE (even size, reciprocal condition, Descartes). The unconditional content is the pigeonhole exponent 1/2 for odd power sums, obtained from n ~ L^2 via the paper's own Lemma A.1, not from known PTE constructions. Known ideal solutions feed f only through n -> 3n and translation.
- Resolution: a short paragraph and an abstract sentence saying this. Add that the data in Fig. 2 (roughly linear for L <= 7) are consistent with, but do not test, N(k)=k+1 for non-ideal k.

**m2 (stability theorem scope; should be fixed).**
- Location: Thm 1.3, abstract, Thm 6.5, Remark 6.1.
- Problem: all thresholds and constants (delta_thm, C_a, cond, Xi_mu, Pi_a, r_n) are evaluated at the true unknown orders. Genus 0 and a known n are assumed but are not in the statement or abstract. The error model is on c_1..c_n, not on eigenvalues. Passing from spectra to c_j needs fitting a divergent asymptotic series, and the supplement's error bars are explicitly heuristic.
- Resolution: restate Thm 1.3 and the abstract with these hypotheses. Add a uniform-in-class corollary, e.g. integer orders with max <= mu and n fixed (separation >= 1/mu is available). Soften "we prove stability estimates".

**m3 (sign error in Lemma 3.3).** d = R(m') - R(m) is printed as 2(g'-g)+n-n'. From (12) it equals 2(g'-g)+n'-n. Check: (1;15) vs (0;3,3,5,5) has d=1, but the printed formula gives -5. The later formulas |V|-|U| = 2(g-g') and |U|+|V| = 2max(n+g-g', n'+g'-g) are correct only with the corrected sign.

**m4 (misstated citation).** Sect. 1.1 says "Philippe showed that a hyperbolic triangle group is determined by its length spectrum". Ref [17] proves this only for (2,p,q) triangle groups (groups with a right angle). (3,3,12) is not of that type.

**m5 (Theorem 3.8, last sentence).** "|U*|+|V*| = 2L+2 implies |g-g'| = 1" holds only when g != g'. For g = g' the minimum 2L+2 is attained (Example 3.12(i): (0;3,10,15,30) vs (0;4,5,21,28), L=3, size 8). Put the hypothesis inside the sentence.

**m6 (Figure 2 and ambiguous counts).**
- Fig. 2: state the order cutoff (12) and whether larger-order members of each class were included; infinitely many area classes lie below 7/5, e.g. (0;2,3,m).
- Remark 3.2: define "witness configuration" (primitive? up to swapping A,B? up to A -> -A?) so the counts 15/35/25/61 can be reproduced, and list the configurations in the supplement.
- Abstract vs Thm 1.3: the abstract says "n >= 2 orders equal", Thm 1.3 says k = n >= 3 (n=2 is not a hyperbolic sphere).

**m7 (triangle threshold is relative to triangles).**
- The abstract's "threshold ... cone-order sum 17" compares only with other triangle orbifolds (n=3 known).
- Within Sig, two invariants already fail at sum 15: (5,5,5) and (0;2,2,2,10) share exactly c_1,c_2, a pair the paper itself uses in Appendix A. Say this in the abstract and Thm 1.2.

**m8 (scope).**
- The results are for closed orientable cone-point orbifolds. A non-orientable orbifold with crosscaps has the same heat series form (area and cone orders only). Heat therefore does not hear orientability, and genus is determined only inside Sig.
- Add "orientable, without reflectors" to the abstract and one remark.

**m9 (realisable vs. general data).** The 1/k exponent is sharp only for data that are not heat invariants of real multisets when k >= 3 (Prop 6.6(ii)). For realisable data with a k-fold order inside n > k orders, the exponent is open. Put this in the abstract and theorem statement, not only in the text.

**m10 (loose citations).**
- Chen: Ex. 2.36 is four-term; cite the relevant identity for the 5+5 case precisely.
- [39] (Croot-Mao-Yip) concerns Wright's variant in integral domains. For "N(k) = o(k^2) open" also cite [5] and [37].
- Re-check "Wright's (k^2+4)/2", the Melzak page numbers and the numbering of Borwein-Ingalls' Problems 3 and 4 against the originals (unverified by me).
- For Ucar's thesis and Dryden-Strohmaier, state the normalisation correspondence once (curvature sign, the (-1)^l).

**m11 (reproducibility).** The key computations (Prop 5.9 and its 783 explicit collisions; the searches of Remarks 3.2 and 3.13) live in an external repository. Add search bounds and checksums to the supplement. All the searches I redid agree with the paper.

## 6. Presentation

- **P1.** The paper is long (35 pp.) and carries five themes. Consider moving Sect. 5.1-5.2 and Sect. 6 to a companion paper (one is already announced) or compressing Sect. 6.
- **P2.** Thm 1.1 mixes a count (i), growth (ii) and sphere results (iii). Separate what is unconditional from what is equivalent to an open problem.
- **P3.** Notation collisions: mu (max order / multiplicity), D (diameter / difference D(t)), Psi_k, I_n, H_L, K_mult, K_iso, T_L, f, f_g, f_n. "Disjoint" and "no pair {z,-z}" are used interchangeably in Def. 3.7 and Remark 3.2.
- **P4.** Ensure the displayed formulas of Thm 5.10 (phi) and Thm 6.8 are legible in print (they extract garbled).
- **P5.** Cryptic phrases: Fig. 3 "joined across integer S"; Table 1 "rounded so that it keeps its meaning".
- **P6.** In Sect. 3.3, display the L=2,3 minimal examples as explicit signed multisets Z.
- **P7.** The figures are well designed, with perceptually uniform colours. Fig. 2 would be clearer with the numerical values of the lower bound and the cutoff stated.

## 7. Recommendation

**Minor revision.** The central mathematics (Sect. 2-5, Appendix A) is correct. I could reproduce essentially every exact computation: witnesses, exhaustive searches to 440 (n=4) and 120 (n=5), the T_3 negative search to 220, the full 4800-sum collision census, Table S3, the elliptic-curve data, the Hurwitz determinant, the heat coefficients, and part of Table 1. The remaining reasons not to accept as is:
- framing and scope (m1, m2, m7-m9);
- a displayed sign error and a misstated citation (m3, m4);
- an ambiguous theorem clause and unclear counts or captions (m5, m6);
- the breadth of the paper relative to one article, and moderate novelty of Sect. 5-6.

Resolving m1 and m2 means rewriting the abstract, Thm 1.1(ii) and Thm 1.3 and adding short remarks, not new mathematics. Resolving the rest means corrections of statements and captions. Confidence: 0.8 on correctness of what I checked; 0.5 that the current form is best placed at JGA (splitting into a heat-invariant/PTE paper and an arithmetic/numerical companion would improve it).
