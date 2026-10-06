*Provenance: the reviewer subagent could not write files ("the tool refused"); this is its returned text, saved verbatim by the orchestrating session.*

RECOMMENDATION: MINOR REVISION (confidence about 80% on technical correctness; moderate on venue fit and novelty).

MAJOR issues: none. I found no genuine error, gap or must-fix overclaim in any proof or numerical claim I could test, and I list nothing as MAJOR so as not to inflate. Conditions for acceptance are minor items m1-m4 below.

The write to REPORT.md was refused by the tool, so the full report is below.

# Referee report (trace-formula / heat-kernel analyst): "How much of a hyperbolic orbifold does heat hear?" (J. Geom. Anal.)

Placeholders (author contributions, AI-use statement, Zenodo DOI) are treated as known and not counted.

## 1. Summary of the paper

For a closed orientable hyperbolic 2-orbifold O with signature (g; m_1..m_n), the Selberg trace formula with elliptic terms applied to the heat function gives Z_O(t) = I(t) + E(t) + Hyp(t). The hyperbolic part is O(t^{-1/2} e^{-l^2/4t}), so the whole asymptotic expansion sum c_j t^{j-2} depends only on the signature. Cone-point coefficients are obtained in closed form (Lemma 2.7, Prop. 2.8, Bernoulli numbers). The j-th invariant adds exactly one new odd power sum sum_i m_i^{2j-3}; c_1 = Area/4pi; the reciprocal sum R enters via c_1.

From this the authors derive:
- **Thm 1.1(i), Cor. 3.5.** The first floor(Area/pi)+4 invariants determine genus and cone orders, via a Newton-identity "mirror" argument (Thm A, Thm 3.4). No area-independent number exists (Prouhet-type constructions, Prop. 3.9, Thm 3.10).
- **Thm 1.1(ii), Thm 3.11.** A sqrt-type lower bound and a linear upper bound for f(A), with the two-sided equivalence f(A) >= cA^alpha iff N(k) <= Ck^{1/alpha}, where N(k) is the Prouhet-Tarry-Escott (PTE) size function.
- **Thm 1.1(iii), Thm C.** Spheres with n cone points are determined by n invariants. n-1 invariants fail near any n distinct positive reals, and on integers for n = 3, 4.
- **Thm 1.2, Sect. 5.** For triangle orbifolds, two invariants are equivalent to (sum S, reciprocal sum R). The first collision is (2,8,8) ~ (3,3,12) at S = 18. Its isolation, and that of the scalings k(2,8,8), k(3,3,12), is proved by showing the cubic C_{27/2} is an elliptic curve of rank 0 with torsion Z/2 x Z/6. Three invariants always suffice.
- **Sect. 4.** Same-signature orbifolds have identical expansions. The trace difference is bounded by an explicit constant times t^{-1/2} e^{-l^2/4t}, and this is attained when weighted length spectra first differ at l.
- **Sect. 6, Thm 1.3.** Stability of (c_1..c_n) -> orders, via the triangular map F, the Hurwitz-type system of Thm B and root perturbation. It is Lipschitz at simple orders and Hölder-1/k at k-fold orders, with sharpness statements and explicit rounding thresholds (Table 1).
- **Sect. 7 / supplement.** FEM spectra of the pair confirm the trace formula to about 1e-13, with a "blind" recovery.

## 2. Significance and novelty

**Classical content.** The trace formula in the form used is Dryden-Strohmaier, arXiv math/0504571, eq. (1). I checked it: the elliptic term 1/(2m sin theta) int e^{-2 theta r}/(1+e^{-2 pi r}) h(r) dr, theta = pi l/m, 1 <= l <= m-1, matches the paper's E_m. Locality of the heat expansion is classical (Donnelly; Dryden-Gordon-Greenwald-Webb (DGGW); Ucar), and the paper says so. The cone coefficients were known (DGGW for l <= 1, Schueth, Ucar for all l). Dryden-Strohmaier and Doyle-Rossetti (arXiv 1103.4372; abstract verified) already show the spectrum determines the number of cone points of each order.

**New content.** I searched arXiv for earlier finite-count results and found none. The nearest are Abreu-Dryden-Freitas-Godinho (math/0608462) and Richardson-Stanhope (1910.03224), which use heat invariants but give no count. What is new:
- the explicit uniform number floor(A/pi)+4;
- the reduction of area-dependence to an odd-power-sum / PTE problem, with the two-sided f ~ N equivalence;
- the exact triangle threshold 17 with the isolation proof;
- the quantitative stability and locality estimates.

These are real but modest. The count is an elementary Newton-identity argument, the triangle statement is number theory, the trace-formula content is standard, and the Thm 4.4 constant is weak (it carries e^{3D}). The paper is coherent and honest. Its geometric-analysis core is thin for the venue, and it combines four loosely connected threads in 35 pages.

**Literature verification.** Crossref/arXiv metadata of 17 cited items match (Dryden-Strohmaier CMB 52; Stanhope AGAG 27; Wooley PLMS 118; Coppersmith et al. Math. Comp. 93; Troyanov TAMS 324; Wolpert Ann. Math. 109; Melzak CMB 4; Ostrowski Acta 72; Garbin-Jorgenson Kodai 43; Schueth AIF 69 and AGAG 69; DGGW and erratum; others). arXiv:2506.11429 (Chen) and arXiv:2609.05061 (Croot-Mao-Yip, Sept 2026) exist. Wooley [40, Thm 13.1] is quoted correctly (W(k,h) <= k(k+1)/2 + 1). Not accessible to me: Borwein-Ingalls, Bremner-Guy-Nowakowski, Ucar's thesis, Allouche-Shallit and Chen's internal numbering, so page-level and theorem-level citations to these are unchecked.

## 3. Correctness: what I recomputed (own code, scratch folder)

**Heat expansion.**
- Direct 40-digit quadrature of E_m(t) at t = 0.01 for m = 2, 3, 8 against sum b_l(m) t^l. Agreement is to the size of the next asymptotic term.
- The identity term against sum alpha_k t^k agrees to 2e-18.
- Closed forms (4)-(5) were verified: p_0..p_3, alpha_0..alpha_5 = 1, -1/3, 1/15, -4/315, 1/315, -4/3465, the leading coefficients |B_{2l+2}|/(2(l+1)!(2l+1)), and p_l(1) = 0.
- Eq. (9) and c_2 = 67/48 for (2,8,8) and (3,3,12) hold exactly. d_3, d_4, d_5 = 25/12, -1775/24, 153025/48 hold exactly. The supplement's blind c_3 estimates agree with exact -1601/480 and -867/160.

**Hand re-derivations (no gap found).**
- Lemmas 2.4, 2.5, 2.6, including the constant C, the bound 1 + 2t/(l-t) <= (2+3l)/(2+l), and the log-derivative sign of B.
- Thm A, Lemma 3.1, Thm 3.4, Cor. 3.5, Thm 3.8 (Descartes bound), Prop. 3.9, Lemma A.1, Prop. A.2, Thm 3.11(a)-(e). In Prop. 3.9 the factor 1-2^{j+1} vanishes at j = -1, so reciprocal sums match automatically; this is correct.

**Thm B.** Exact rational check that the true e solves M e = b and det M = (-1)^{n(n+1)/2} prod(m_i+m_j)/prod m_i, for 8 multisets with n = 2..5, including repeated orders.

**Examples.** Exact shared-invariant counts:
- (1;15) vs (0;3,3,5,5): exactly 2.
- (0;3,10,15,30) vs (0;4,5,21,28): exactly 3.
- (1;15,15,15) vs (0;3,3,5,7,7,21): exactly 3.
- (0;4,4,5,5,6,12,12) vs (0;2,2,2,3,10,10,10,10): exactly 3.
- (0;5,5,5) vs (0;2,2,2,10): exactly 2.
- (0;16,16,74,74) vs (0;11,37,44,88): 3, with the stated P_1, P_3, R.
- Thm C(3) values P_3 = 1032/1782 and P_5 = 25159618/21298618 are correct.

**Triangle orbifolds (exact integer-reduced rationals).**
- All hyperbolic triads with S <= 1300: no collision for S <= 17; the only collision at S = 18 is (2,8,8) ~ (3,3,12).
- The 38 collision-free sums of Prop. 5.9 are reproduced exactly, and there are none above 557 up to 1300.
- There are 83 triads with 10 <= S <= 18, and 25575 at S = 557.
- Table S3 (S*(p) and first collisions, p = 2..14) is reproduced. "Overlap iff S >= S*(p)" holds for p <= 14, S < 500. Spot-checked odd-parity gaps (1/840 etc.).
- The paper's claim to 4800 is internally consistent (4783 sums = 3962 + 783 + 38), but I reproduced only S <= 1300.

**Thm 5.10.**
- psi maps the 12 listed points of E to C_{27/2}, and the polynomial identity psi(E) in C holds.
- The discriminant is 2^18 3^8 5^6, and #E(F_p) = 12 for p = 7, 11, 13.
- A brute-force search finds only the six permutations among primitive points with entries < 200.
- The 2-descent local steps were recomputed (d_1 = +-2, +-3 insoluble mod 5 on E; d_1 = 3, 5, 15 insoluble mod 9 or 27 on E'). Rank 0 follows from Cremona's formula.

**Section 6.**
- Row sums of F^{-1} give amp_0..amp_4 = 2, 14, 498, 4062, 56230/3 and P_3 = -18c_1 - 120c_2 - 360c_3. Prop. 6.6(i) values and Remark 6.7's identity d^2(3a+d) are correct.
- Exact cond = ||M(m-hat)^{-1}||_inf is 1.0 for triangles, with maximum 3.5109 on the Table-1 multisets ((2,2,2,2,3)), matching "3.511" and well below the Hadamard-type bound in 6.4(a).
- Independent optimisation of the failure threshold delta_up gives 2.485e-3 for (2,8,8) and 5.036e-4 for (4,4,4). These agree with Table 1 exactly.

**Computational remarks.**
- The n = 5 exhaustive search (orders 2..120, 216,071,394 multisets, exact (R, P_1, P_3, P_5)) finds no witness, as claimed.
- For the pencil count "15 witness configurations with entries <= 130" I get 17 distinct witness pairs (14 primitive). The convention for 15 is not defined.
- The exhaustive n = 4 search to 440 (claimed 107 primitive witnesses) did not finish in time, so it is unverified.
- Fig. 2: the "525 area classes" is exactly the number of distinct areas s <= 7/5 realised with all orders <= 12. Computing the full classes (orders unrestricted, Egyptian-fraction enumeration) gives K_mult = 1, 2, 3 for 17, 311, 197 classes, consistent with the plotted dots.
- Remark 3.13: {1,1,1,1,7} has the unique partner {0.266, 4.283, 6.451}.

**Not recomputed.** FEM spectra and Section 7 / supplement numerics (eigenvalue accuracy, Bolza benchmark, trace fits, closed-geodesic enumeration); the closed form of Thm 6.8 (garbled in the PDF text); the certificates delta_cert of Prop. 6.9; collision witnesses beyond S = 1300; the n = 4 count to 440.

## 4. MAJOR issues

None. See the header line above.

## 5. MINOR issues

**m1. Real orders have no stated geometric meaning.** Location: abstract, Thm 1.1(iii), Thm C(2), Thm 1.3, Prop. 6.6(i), Rem. 6.7.
- Problem: these speak of heat invariants "of positive real orders" and of "n-1 never suffice near n distinct positive reals". Prop. 2.8 uses sum_{j=1}^{m-1} and is valid only for integer m. For real m the objects are hyperbolic cone surfaces of angle 2pi/m, whose coefficients need Schueth 2025 or a separate argument. The claims concern a formal polynomial continuation. For actual orbifolds (integer orders) the discrete rounding thresholds carry the content. Integer sharpness for n >= 5 is open (Problem 3).
- Resolution: declare these results formal, or justify the geometric reading, and align the abstract.

**m2. Philippe [17] is misquoted.** The introduction says "a hyperbolic triangle group is determined by its length spectrum". The cited result (Ann. Inst. Fourier 58, 2008; abstract verified via Crossref) is for (2,p,q) triangle groups only. The minimal pair includes (3,3,12), which is not of this type. Resolution: add the hypothesis.

**m3. Sign typo in Lemma 3.3.** It states d = R(m')-R(m) = 2(g'-g)+n-n'. From (12) it is 2(g'-g)+n'-n. Check: (1;15) vs (0;3,3,5,5) gives d = 1, not -5. The padding rule and |U|+|V| are right with the correct sign.

**m4. "Certified" rests on heuristic error bars; Thm 1.3 is stability of an algebraic map only.**
- Location: Sect. 7, S2, Table S2.
- The certificate rests on error bars the authors call heuristic (least-squares fits to a divergent asymptotic series, a-posteriori eigenvalue errors, no double-window recomputation of the spectra). The blind test is acknowledged to be easy.
- No theorem controls eigenvalue error -> c_j error.
- Resolution: qualify the wording and say clearly in the abstract and Remark 6.1 that the spectral step is not covered.

**m5. Constants depend on the unknown true orders** (Thm 6.5, 6.8; acknowledged in Remark 6.1). An a-priori version, given n and a bound on mu, would strengthen the result.

**m6. Fig. 2 caption.** It does not say the classes are restricted to areas realised with orders <= 12 (the class membership itself is correct).

**m7. BGN citation.** The minimal pair is placed at Lambda = 27/2, while [19] treats integer Lambda. I could not check "[19, p. 117]". Please clarify.

**m8. Wording.** "{1,1,1,1,7} admits three positive real partners" reads as three partners; there is one partner with three positive entries.

**m9. Counting conventions.** "15 / 35 pencil configurations" and "107 primitive witnesses" are not reproducible without a definition (I get 17 pairs, 14 primitive, at bound 130).

**m10. Provenance.** [20] is "in preparation"; say whether any proof depends on it. The repository account (Ali-M658) matches no author; please clarify.

**m11. Remark 4.7 / [8].** The restriction "genus at least one" for [8, Thm 5.1] seems to understate Dryden's finiteness result (the abstract of arXiv math/0411290 states it for hyperbolic orbisurfaces generally). Please check.

## 6. Presentation

- **P1.** Notation clashes: P_n (class of n-cone-point spheres) vs P_k (power sums), so P_3 means two things in Sections 3 and 5. Also S_1 vs S; D (diameter) vs D(t) vs Hurwitz D_k; c, c_j and DGGW's invariant c; l as systole vs length function.
- **P2.** The lettered Theorems A-C sit among numbered ones, so the reader depends on the roadmap.
- **P3.** Length and focus: 35 pages of heat expansion, PTE growth, elliptic-curve descent, perturbation theory and FEM numerics. Move the descent or Prop. 5.9/Table S3 and the stability numerics to the supplement or a companion. Remarks 3.2 and 3.13 are search-log material.
- **P4.** Thm 6.4(a) and Thm 6.8 constants are hard to read in the PDF text; typeset them unambiguously.
- **P5.** Fig. 2: say that points above s = 1.4 are constructed pairs, not computed K_mult. Fig. 3-4 captions are dense.
- **P6.** The PDF shows a doubled "1 1 Introduction" heading and line-numbering artefacts.

## 7. Recommendation

**Minor revision**, confidence about 80% on correctness and moderate on venue fit and novelty. Trace-formula content is classical; new content is arithmetic and perturbation-theoretic. Resolutions:
- m1: state the real-order results as formal, or justify them for cone surfaces.
- m2, m3, m7, m8, m11: correct the quoted statements and the sign.
- m4, m5, m6, m9, m10: qualify "certified", clarify conventions and provenance.
- P1, P3: fix notation and consider splitting or trimming the paper.

The core (Sect. 2-5) is correct and the arithmetic claims I could reproduce hold.

---
**Addendum (from the reviewer's later final message):** the exhaustive n = 4 search to 440 finished and gives 107 primitive witnesses, matching the paper; the item marked "unverified" in section 3 is therefore confirmed. Recommendation unchanged (minor revision, no MAJOR issues).
