*Provenance: the reviewer subagent could not write files or hand back (Write and SubagentHandback refused); this is its final message, recovered verbatim by the orchestrating session from the reviewer's transcript (line 398 of agent-ac56058f91b5737e5.jsonl).*

**RECOMMENDATION: MINOR REVISION** (about 85% confident that the mathematics is correct as stated; about 60% on editorial fit and novelty for JGA).

**MAJOR issues: none found.** I found no error or gap in any stated theorem, and I recomputed nearly everything that could be checked. I would make m1–m6 below conditions of acceptance. Several of them are real inaccuracies, not typos.

Both the `Write` tool and `SubagentHandback` refused delivery, so REPORT.md was not written and the full report is below. Placeholders (author contributions, AI statement, Zenodo DOI) are treated as known and not counted.

**Method note.**
- I read only the two PDFs, with `pdftotext` and the page images of pp. 16, 22, 24–26.
- I fetched literature headlessly from Crossref, arXiv and the Semantic Scholar API. zbMATH returned 503.
- My code and downloads are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-1/d-jga-rigour-referee/scratch/`.
- One side effect outside the scratch folder: I ran `pip install cypari` (PARI bindings), which went into the user's Python site-packages.
- I did not open the GitHub repository named in the Data statement.

---

## 1. Summary of the paper

For a closed orientable hyperbolic 2-orbifold O with signature (g; m_1,…,m_n), the heat trace has an expansion Z_O(t) ∼ Σ_{j≥1} c_j t^{j−2}. The paper re-derives from the Selberg trace formula that:
- c_1 = Area/4π;
- for j ≥ 2, c_j is a fixed function of the area plus a sum over cone points of a polynomial in m_i and 1/m_i;
- the j-th invariant is, modulo lower ones, an affine function of one new odd power sum P_{2j−3} = Σ m_i^{2j−3} (R = Σ 1/m_i is already in c_1).

Comparing two signatures with equal H_L = (c_1,…,c_L) becomes a moment problem for U ⊎ (−V), a signed multiset whose odd power sums vanish. This is a symmetric Prouhet–Tarry–Escott (PTE) system with the extra condition Σ 1/z = 0.

Main results:
1. **Thm 1.1(i).** The first ⌊Area/π⌋+4 heat invariants determine genus and cone-order multiset among all closed orientable hyperbolic 2-orbifolds. No area-independent number works.
2. **Thm 1.1(ii).** Let f(A) = max Kmult over orbifolds of area ≤ A. Then ⌊√((A/2π−1)/3)⌋+2 ≤ f(A) ≤ A/π+4. Moreover f(A) ≥ cA^α iff N(k) ≤ Ck^{1/α}, where N(k) is the least size of a degree-k PTE solution. So linear growth of f is equivalent to the open question N(k) = O(k).
3. **Thm 1.1(iii).** For spheres with n cone points, n invariants suffice (Thm A, via Newton identities and Orlando's formula). Near n distinct positive reals, n−1 never suffice. For n = 3, 4 this fails already at integer orders: {2,8,8} vs {3,3,12}, and {3,10,15,30} vs {4,5,21,28}.
4. **Thm 1.2.** For triangle orbifolds O(p,q,r) the first two invariants are equivalent to (S_1, R) = (p+q+r, Σ1/p). They determine the orbifold if p+q+r ≤ 17. The unique first failure is O(2,8,8) vs O(3,3,12) at sum 18. It is isolated: the cubic C_{27/2} has rank 0 and 12 rational points. The third invariant always separates.
5. **Thm 1.3 and Section 6.** Stability of the recovery chain (triangular front end, Hurwitz-type linear system, root finding). It is Lipschitz at simple orders and Hölder-1/k at k-fold orders, sharp for general data. For realisable data the exponent is 1/2 at a double order and when all orders are equal. There are explicit rounding thresholds (Table 1).
6. **Section 4.** Every c_j depends only on the signature. The difference of two traces of one signature is O(t^{−1/2}e^{−ℓ²/4t}) with an explicit constant, and the leading term is attained.
7. **Section 7 and supplement.** Finite-element spectra of O(2,8,8), O(3,3,12) (about 2850 eigenvalues each) and of a family in (0;3,3,3,3). These illustrate the above; nothing in them is used in a proof.

---

## 2. Significance and novelty

I checked the neighbouring literature; everything below was fetched.

**Known background, all consistent with how the paper cites it.**
- Dryden–Strohmaier, Canad. Math. Bull. 52 (2009) 66–71 (Crossref abstract): the spectrum determines the length spectrum and the number of singular points of each order.
- Uçar, thesis, HU Berlin 2017, arXiv:1711.03405. Cor. 4.21(iv) and Cor. 4.23 are as quoted. His Thm 3.40 argument uses the limit ν→∞ of the whole sequence of invariants (I read it), so there is genuinely no finite count there. The paper's priority claim for an explicit finite number looks correct.
- Dryden–Gordon–Greenwald–Webb, Michigan Math. J. 56 (2008) 205–238. The quoted sentence "does not seem sufficiently strong to distinguish among these triangular pillows" is verbatim (Remark 5.16).
- Grieser–Maronna (Notices 2013, arXiv:1208.3163): area, perimeter and Σ(1/angle) determine a Euclidean triangle, as stated.
- Linowitz–Voight (arXiv:1408.2001, Thm A): isospectral non-isometric pairs of signature (0;2,2,2,2,2,3,4), as cited.
- Schueth (arXiv:1812.06119): cone contributions to the t² coefficient, as cited.
- Chen, PTE survey (arXiv:2506.11429): the entry A.685 ([3,10,15,30]=[4,5,21,28], type (−1,1,3)) and the identity (3.33) for type (−1,1,3,5) are there as stated.
- Croot–Mao–Yip (arXiv:2609.05061, 4 Sep 2026) exist. They say ideal solutions are known only for k ≤ 9 and k = 11, and quote the pigeonhole bound k(k+1)/2+1 and Wooley's Thm 13.1. This supports "all known bounds are quadratic".
- Laurens (arXiv:2206.09050) Lemma 3.2 is the uniqueness-from-n-power-sums statement credited to Steinig.

**Uncited related work.** Abreu–Dryden–Freitas, "Hearing the weights of weighted projective planes", Ann. Global Anal. Geom. 33 (2007/08), doi 10.1007/s10455-007-9092-6 (arXiv:math/0608462). They use heat invariants of orbifolds with three isolated singularities to recover the weights. The setting is different (dimension 4), but it is the closest published precedent for "finitely many heat invariants determine the orders of the singular points" and should be cited. Richardson–Stanhope (arXiv:1910.03224) is also nearby.

**Assessment.**
- The algebraic core (Newton identities, Orlando's formula, the mirror/Descartes arguments of Thm 3.4 and 3.8) is elementary. The uniform bound ⌊A/π⌋+4 is easy once Uçar's formula is available.
- The new and interesting parts are: the two-way equivalence between the growth of the needed number and the PTE problem (Thm 3.11(b)–(d)); the sharp triangle threshold with its arithmetic explanation (Thm 5.4–5.10); the quantitative locality bound.
- The stability section is a careful but routine application of Newton/Hurwitz and Rouché.
- The headline question "how fast must the number grow" is answered only between √A and A, and the gap is equivalent to an open problem. The paper says so openly.
- The extremal examples have huge numbers of cone points (n of order L²). Typical orbifolds of small area need at most 3 invariants (Fig. 2). The paper could discuss how atypical the worst case is.
- Fit for JGA: spectral geometry with number-theoretic flavour, and the number theory is the more original half. An editor who wants substantial analysis may see it as borderline. Mathematically it is sound and honest.

---

## 3. Correctness: what I recomputed

Everything agreed with the paper unless marked ✗.

**Section 2 (heat coefficients).**
- α_0..α_5 = 1, −1/3, 1/15, −4/315, 1/315, −4/3465 from the paper's formula; the paper's α_0..α_4 match.
- p_0, p_1, p_2 from (4)–(5) match (7).
- Taylor coefficients of Φ_m(u) vs the closed form (Lemma 2.7) at m = 2, 3, 5, 8 agree to about 1e−29.
- E_m(t) from Thm 2.3 vs Σ(−1)^l p_l(m)t^l/m for m = 2, 3, 8: agreement to the expected asymptotic accuracy (3e−15 for m=2, 1e−12 for m=3).
- I(t)·t vs Σα_k t^k at t = 0.01: 1e−13.
- c_2 and c_3 in (9) checked.
- d_3, d_4, d_5 = 25/12, −1775/24, 153025/48 for (2,8,8) minus (3,3,12).
- c_3(2,8,8) = −1601/480 and c_3(3,3,12) = −867/160 are consistent with Table S2.

**Analysis (Sections 2 and 4).** I re-derived by hand Lemmas 2.4, 2.5, 2.6 and Thm 4.4(b): the counting bound, the Stieltjes integration by parts, the constant C(A,ℓ,D), the monotonicity of B in ℓ and D, and the eigenvalue-counting trick in Lemma 2.5. I found no gap.

**Section 3.**
- Thm B verified symbolically (the linear system, its solution, and det M = ς_n ∏(m_i+m_j)/∏ m_i) for seven multisets, n = 3, 4, 5, including repeated orders.
- Re-derived Thm A, Thm 3.4 (mirror argument, parity of T), Thm 3.8 (Descartes argument, gap by gap), Prop 3.9 (including the x* argument and hyperbolicity), Lemma A.1, Prop A.2 and the arithmetic of Thm 3.11(a)–(e). The thresholds 3(L−1)²+1, 16πL² and 12πL² follow. N is non-decreasing, which the converse in (d) needs.
- Exact shared-invariant counts, all as claimed:

| Pair | Shared invariants | Area/2π |
|---|---|---|
| (2,8,8) / (3,3,12) | 2 | 1/4 |
| (3,10,15,30) / (4,5,21,28) | 3 | 22/15 |
| (1;15) / (0;3,3,5,5) | 2 | 14/15 |
| (1;15,15,15) / (0;3,3,5,7,7,21) | 3 | 14/5 |
| (0;4,4,5,5,6,12,12) / (0;2,2,2,3,10,10,10,10) | 3 | 113/30 |
| (0;5,5,5) / (0;2,2,2,10) | 2 | 2/5 |
| (0;16,16,74,74) / (0;11,37,44,88) | 3 | 547/296 |

  Also confirmed: R = 45/296, P_1 = 180, P_3 = 818640 for the last pair; for Thm C(3), P_3 = 1032 vs 1782 and P_5 = 25159618 vs 21298618.
- Remark 3.13: {1,1,1,1,7} has the three-element positive real partner {0.2664, 4.2830, 6.4506}.

**Remark 3.2 (computer searches).**
- Exhaustive n = 4 search over integer orders in [2,440] with equal (R,P_1,P_3): exactly **107** primitive witnesses, **6** with no pencil splitting, and the smallest is (16,16,74,74)/(11,37,44,88). All three claims confirmed.
- Exhaustive n = 5 search over orders ≤ 120: exactly **216,071,394** multisets enumerated (= C(123,5), the paper's number), and no two share (R,P_1,P_3,P_5). Confirmed.
- ✗ The pencil counts "15 / 35 / 25 / 61" were not reproduced. With A, B of integers, e_1 = 0, equal e_3 and e_4, four entries of each sign in A ⊎ (−B), and all entries ≤ 130, I get 14 distinct primitive witnesses (17 with multiples included). For ≤ 220 I get 30 primitive (49 with multiples). The paper may be counting splittings or something else, but under the definitions as written the numbers do not match (m6). I did not test the "25 and 61" variant.

**Section 5 (triangles).**
- Independent C enumeration of all hyperbolic triads with S ≤ 4800, exact reduced fractions: exactly the 38 collision-free sums of Prop 5.9 (19, 21–25, 27–30, 33, 41, 44, 46–51, 59, 65, 67, 81, 99, 115, 119, 123, 125, 173, 199, 203, 223, 235, 243, 251, 307, 329, 557). The other 4745 sums all carry a collision. S = 557 has 25575 triads.
- S ≤ 17 has no collision; the first collisions are at S = 18, 20, 26. There are 83 triads with 10 ≤ S ≤ 18 and R is injective within each sum except for the one pair.
- Thm 5.4 (S*(p)) agrees with a direct convex-hull overlap test for all S ≤ 600, p ≤ 40. Table S3 (first collision, p ≤ 14) is reproduced exactly.
- Symbolic checks of identities (a) and (c) in the proof of Thm 5.4, the numerator of φ_p′, formula (14), and the listed gap values (−7/936, −1/72, …, 1/840, 1/2310, 1/10296).
- Thm 5.10: φ∘ψ = id on E symbolically; disc E = 2^18 3^8 5^6; all 12 points lie on E with orders 6, 3, 2 as stated; #E(F_7) = #E(F_11) = 12; rank 0 by PARI (`ellrank` gives [0,0], analytic rank 0, conductor 90); torsion Z/2 × Z/6; a search with |X|,|Y|,|Z| ≤ 60 on C_{27/2} finds exactly the 12 stated points.

**Section 6.**
- amp_0..amp_4 = 2, 14, 498, 4062, 56230/3 and the row P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3, from F^{−1}.
- ζ_3, ζ_4, ζ_5 = 1, 79/3, 14048/15.
- δ_thm reproduced for (2,8,8), (3,3,12), (2,3,7), (4,4,4), (7,7,7), (3,3,4,4), (3,10,15,30), (2,2,2,3): all eight rows agree with Table 1.
- δ_up, minimised independently over polynomials with a tie root: (2,8,8) 2.485e−3, (3,3,12) 4.588e−3, (2,3,7) 6.587e−3, (4,4,4) 5.036e−4, (7,7,7) 8.272e−5, (2,2,2,3) 2.520e−4, (5,5,5,5) 3.826e−5, (3,3,4,4) 1.194e−4. All agree with Table 1 and are consistent with δ_cert < δ_up.
- Thm 6.4(b): random tests on five multisets gave error/bound ≤ 0.054, so the bound is valid and conservative.
- The Rouché constants in Thm 6.5, the algebra behind Thm 6.8, Prop 6.6(i) (δR, δP_3) and Remark 6.7 (the inequality and the constant 498+42a²) check out.

**Fig. 2 reconstruction.** I enumerated all signatures with s = Area/2π ≤ 7/5 (genus 0 and 1) and counted distinct areas. With all orders ≤ 12 the count is exactly **525**. Orders ≤ 11 give 504, ≤ 13 give 707, and with no bound the number is infinite. See m1.

**Not recomputed.**
- The finite-element spectra (Sec. 7, S1–S3, Fig. 5): I cannot re-run NGSolve here.
- The rational-arithmetic certificate δ_cert of Prop 6.9.
- Example 3.12(iii), L = 4..7 (the pairs are not displayed), and the Fig. 2 diamond and square data.
- Remark 2.10's "compared exactly for l ≤ 40".
- Full texts of [5], [13], [19], [33], [38] (not openly accessible) and the content of [12].

---

## 4. MAJOR issues

None. I could not find an error in any stated theorem, and the proofs I reproduced hold. The paper's own disclosures about the numerics (a-posteriori error bars, no double-window recomputation) are honest. The items below must be corrected, but none changes a theorem.

---

## 5. MINOR issues

**m1. Fig. 2, its caption, and the text at line 438 ("exact Kmult of small signatures").** The caption says "for each of the 525 area classes with s ≤ 7/5 (a class is the set of all signatures with that area)". The number of area classes is infinite (for example (0;2,3,m) has s = 1/6 − 1/m for every m ≥ 7). 525 is exactly the number of distinct areas among signatures with all orders ≤ 12, a restriction the caption never states.

Why it matters: any two signatures of equal area already share c_1, so Kmult ≥ 2 for every class with at least two members. Allowing competitors with orders up to 48 or 100 changes Kmult for 282 resp. 342 of the 525 classes (for example s = 1/10: 1 becomes 2). If the dots were computed with competitors restricted to orders ≤ 12, they underestimate Kmult and "exact" is wrong. If competitors were unrestricted, the class count and caption are wrong. The maximum plotted value (3) is unaffected.

Fix: state the order bound and the competitor range, and recompute the dots against the full finite set of signatures of the same area.

**m2. Remark 4.7, pp. 18–19 (l. 525–528).** "Along a Thurston length coordinate all but countably many points have heat traces different from a given one" is stated without proof, with no definition of "a Thurston length coordinate", and as a "weak orbifold substitute for Wolpert's theorem". It is plausible (real-analyticity of the length spectrum in Fenchel–Nielsen coordinates) but unproved. Give the argument for a precisely stated claim, or delete.

**m3. Intro, l. 104–106, citation [17].** "Philippe showed that a hyperbolic triangle group is determined by its length spectrum." The title and Crossref abstract of [17] (Ann. Inst. Fourier 58 (2008) 2659–2693) concern triangle groups (2,p,q), i.e. with a right angle ("groupes de triangles ayant un angle droit"). The statement is over-general.

**m4. Lemma 3.3, l. 342, sign of d.** The paper has d = R(m′) − R(m) = 2(g′−g) + n − n′. From (12), 2g+n−R(m) = 2g′+n′−R(m′) gives d = 2(g′−g) + **n′ − n**. The rest of the lemma (|V|−|U| = 2(g−g′) and |U|+|V| = 2max(…)) is consistent only with the corrected sign; I checked this.

**m5. Thm 5.10, proof, l. 641–643 (descent for E).** The mod-5 argument for d_1 ∈ {±2,±3} lists three cases (right side ≡ d_1, ≡ d_1^{−1}, or ≡ 3M²e²). It omits the case 5 ∤ Me, where the right side is d_1 + d_1^{−1} + 3M²e² ≡ ±3. That is also a non-residue mod 5, so the claim stands, but the printed proof is incomplete. Add the case and mention the independent rank-0 confirmation.

**m6. Unverifiable computational statements.**
- (a) Remark 3.2: "15 witness configurations … at most 130, 35 … at most 220 (25 and 61 …)". I get 14 / 30 distinct primitive witnesses (17 / 49 with multiples). Please define "configuration".
- (b) Example 3.12(iii) (L = 4..7) and the Fig. 2 diamonds and squares rest on solutions named in other papers ([5, p. 9], [41, p. 2], [37, A.1.33], [41]). The pairs themselves are not written down. For L = 6 the solution A.1.33 has equal odd power sums, but it is not clear from the text how R is made equal, so "area < 2π·10" cannot be reconstructed. Please list the explicit pairs, with areas and shared counts, in the supplement.
- (c) Appendix B says searches were "repeated independently, floating point only rejecting where certified", which is too vague to check. The reproducibility statement points to a GitHub account whose name matches no author. Make sure the archived deposit contains the 783 collision witnesses, the Remark 3.2 and 3.13 search programs, and the Fig. 2 and 3 data.

**m7. Abstract and statements that do not match the body.**
- (a) Abstract: "the sharp exponent is 1/2 at a double order and when all n ≥ 2 orders are equal". Thm 1.3 and Remark 6.7 say k = n ≥ 3 (n = 2 is not a hyperbolic sphere, and the n = 2 all-equal case is the double-order case).
- (b) Abstract and Thm 1.1(iii): "near n distinct positive reals n−1 never do" concerns non-geometric real orders. For integer orders it is known only for n = 3, 4 (Problem 3 is open). A reader may take the abstract as a geometric statement.
- (c) Abstract: "the exact threshold at which two invariants stop sufficing, cone-order sum 17". Sum 17 is only the first failure. By Prop 5.9, two invariants again suffice for every orbifold of sum 19, 21–25, 27–30, and so on. Say that failure is for particular orbifolds at particular sums.

**m8. "Certified" for numerics.** In Table S2 and the S2 text, the blind recovery is "certified", with the certificate "rigorous given the error bars". The same paragraph calls the error bars heuristic, not standard errors. The eigenvalue errors are a-posteriori agreements between two discretisations, not enclosures; single-window slicing is acknowledged to miss eigenvalues; a double-window recomputation "has not been run". Qualify "certified" wherever it appears, or complete the double-window run. Nothing in any proof depends on it.

**m9. Scope of the stability theorem.** Thm 1.3 is for a genus-0 sphere with known n, and its constants C_a depend on the unknown true orders (a-posteriori logic, Remark 6.1). The uniqueness in Thm 1.1(i) for general (g,n) comes with no recovery procedure, since (g,n) is not known in advance. Say so in the introduction. The 1/2 exponent for realisable data is settled only at a double order and when all orders are equal; mixed clusters (e.g. a triple order among n ≥ 4) are not covered.

**m10. Citation details.** All 38 DOIs I resolved through Crossref match authors, title, venue, volume and pages. Small discrepancies:
- [34] (Schueth, AGAG 69(1), art. 2): issued 2025 online vs "(2026)" volume year; arXiv title says "conic", the published one "conical".
- [35]: 2019 in the paper vs Crossref 2020.
- [40]: 2018 online vs 2019 volume.
- [12]: Crossref page range "1033–1033".
- [10]: the Crossref lookup fails, but doi.org resolves to edoc.hu-berlin.de/handle/18452/19142.

I could not check the precise claims about Chang–DeTurck [12] ("a finite but non-uniform count for Euclidean triangles and their Dirichlet eigenvalues"), Bremner–Guy–Nowakowski [19, p. 117 and the §4 table], Borwein–Ingalls Props 1–3 and Problems 3–4 [5], and Melzak/Wright's (k²+4)/2 [38]. For [19]: BGN's Λ is an integer, while the paper's Λ = 27/2 is not, so state exactly what is quoted from [19].

**m11. Thm 4.4 usefulness.** The constant carries e^{3D}, and the admissible range is t ≤ ℓ²/(2(1+ℓ)), where e^{−ℓ²/4t} is only e^{−(1+ℓ)/2} at the right end. As the paper says, the bound is loose; say clearly that it is qualitative.

---

## 6. Presentation

- **P1.** About 35 pages of dense mathematics plus a supplement, with seven strands (trace formula, algebra, PTE growth, rigid case, elliptic curve, stability, numerics). Moving Section 6's certificates, Table 1 and most of Section 7 to the supplement, and the elliptic-curve proof to an appendix, would improve readability.
- **P2.** Overloaded notation: D is the diameter, D_k the Hurwitz determinants, D(t) the trace difference; Pn (spheres) vs P_k (power sums); 𝔱_k(n), 𝔯_n, r_a, r.
- **P3.** Theorems A, B, C are lettered inside numbered sections, and "Theorem 1.1 is proved in Corollary 3.5 and Theorems 3.10, 3.11, A, C" is a long roadmap. A single numbering and a dependency table would help.
- **P4.** The abstract is nearly a page and states eight results; shorten.
- **P5.** Fig. 1 is clear. Fig. 3 (log axes) is hard to read at print size. The Fig. 2 caption is overloaded and misleading (m1). Fig. 4 mixes real and non-real data curves.
- **P6.** Line numbers (and "1 1 Introduction") are left over from the review template.
- **P7.** Table 1's last column, "δ_cert/|c_j|", needs a one-line explanation of how it relates to ε_cert.
- **P8.** The proof of Thm 3.11 is in Appendix A, which makes the key statement hard to audit; it belongs in Section 3.

What is good: the derivation of the heat coefficients is self-contained and cross-checked against Uçar and Schueth; the mirror/Descartes arguments are correct and sharp (Example 3.6 attains Thm 3.4); the 2-descent and torsion computations are right; every exact-arithmetic claim I could test (Prop 5.9, Table S3, Table S4, the Remark 3.2 searches) reproduces; the limitations are stated candidly.

---

## 7. Recommendation

**Minor revision.** The mathematics is correct and the headline theorems are true as stated. Conditions for acceptance:

| Issue | What would resolve it |
|---|---|
| m1 | Make Fig. 2 and its text consistent with the definition of Kmult: state the order bound and competitor range, and recompute if needed |
| m2 | Prove or delete the claim in Remark 4.7 |
| m3 | Correct the description of Philippe's theorem to triangle groups with a right angle |
| m4 | Fix the sign of d in Lemma 3.3 |
| m5 | Add the missing case in the 2-descent, pointing to the independent rank-0 confirmation |
| m6 | Define "configuration", give the explicit pairs behind Example 3.12(iii), Fig. 2 and Remark 3.2, and make sure the deposited repository contains the search programs and data |
| m7–m9 | Align the abstract with the body; qualify "certified" and the scope of the stability theorem |

A second round is not needed if m1–m6 are fixed. Whether a paper with this elementary an analytic core is a JGA paper is for the editor; I would lean to accept after revision, on the strength of the PTE equivalence, the sharp triangle threshold and the verified arithmetic.

Confidence: about 85% on correctness; about 60% on the novelty and fit assessment.