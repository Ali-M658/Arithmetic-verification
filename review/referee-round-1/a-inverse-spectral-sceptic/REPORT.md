*Provenance: the reviewer subagent could not write files ("subagents should return findings as text"); this is its returned text, saved verbatim by the orchestrating session.*

RECOMMENDATION: Major revision (confidence: high on correctness of what I recomputed, moderate on fit and novelty).

I could not write REPORT.md. The Write tool refused it ("subagents should return findings as text"), so the full report is below.

MAJOR issues:
- M1. "How many invariants" is a non-canonical, prefix-based measure, and the growth law is only reduced to an open PTE problem. The "exact threshold at sum 17" is a first failure, not a threshold.
- M2. Theorem 1.3 (stability) concerns an algebraic map on non-geometric data and is not a spectral stability statement. For integer orders it is only a rounding threshold.
- M3. Positioning and novelty claims are not substantiated, and Philippe [17] is misdescribed.

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (J. Geom. Anal.)

Reviewer persona: inverse-spectral sceptic. The placeholders (author contributions, AI-use statement, Zenodo DOI) are not counted.

## 1. Summary

For a closed orientable hyperbolic 2-orbifold with signature (g; m_1..m_n), the paper re-derives the heat coefficients c_j from the Selberg trace formula (Prop. 2.8). They depend only on the area and on one polynomial in each cone order. So c_1 is the area, and each further c_j adds one odd power sum P_{2j-3} of the orders. Comparing two orbifolds becomes an odd-power-sum Prouhet–Tarry–Escott (PTE) problem.

- **Thm 1.1:**
  - The first floor(A/π)+4 invariants determine genus and cone-order multiset.
  - No area-independent number works.
  - f(A) >= cA^α iff N(k) <= Ck^{1/α}, so linear growth iff N(k)=O(k).
  - For spheres with n cone points, n invariants suffice and n−1 do not near distinct reals. Integer counterexamples exist for n=3,4.
- **Thm 1.2:** for triangle orbifolds:
  - Two invariants suffice when p+q+r <= 17.
  - The first failure is {(2,8,8),(3,3,12)}.
  - Three invariants always suffice.
  - The failure is isolated, via a rank-0 elliptic curve with E(Q) of order 12.
- **Sect. 4:** the heat expansion depends only on the signature (classical). An explicit bound t^{-1/2}e^{-ℓ²/4t} is given for the shape-dependent remainder, with sharpness.
- **Thm 1.3:** conditioning of the algebraic map c → orders.
  - Lipschitz at simple orders.
  - Hölder 1/k at k-fold orders, sharp for general data.
  - The exponent 1/2 is sharp in two special real-order cases.
- **Sect. 7 and supplement:** finite-element spectra of O(2,8,8), O(3,3,12) and a family (0;3,3,3,3).

## 2. Significance and novelty

**References I verified (arXiv/Crossref):**
- Dryden–Strohmaier, arXiv math/0504571. The Laplace spectrum determines the length spectrum and the number of singular points of each order.
- Stanhope, arXiv math/0301357.
- Dryden, arXiv math/0411290.
- Uçar's thesis, arXiv 1711.03405. It gives all heat invariants for constant-curvature orbisurfaces.
- Doyle–Rossetti, arXiv 1103.4372.
- Chen's PTE survey, arXiv 2506.11429.
- Croot–Mao–Yip, arXiv 2609.05061. This treats Wright's generalisation of PTE, not N(k)=o(k²), so it is a tangential citation.
- Schueth, AGAG (Crossref DOI exists).
- Philippe, Ann. Inst. Fourier 2008. The title and abstract concern triangle groups (2,p,q) only.
- Linowitz–Voight and Bremner–Guy–Nowakowski exist as cited.
- Classics the paper does not cite: Brooks–Perry–Petersen (Crelle 426, 1992), Sunada (Ann. Math. 1985), Zelditch (MRL 1999), Hezari–Zelditch (Ann. Math. 2022), Osgood–Phillips–Sarnak (JFA 1988).

**What is new:**
- the area-based count floor(A/π)+4 and its equivalence with N(k);
- the exact triangle-orbifold first failure and its elliptic-curve isolation;
- the explicit trace-formula bound on the shape-dependent remainder.

I found no earlier occurrence of any of these.

**The sceptic's view:**
1. After Prop. 2.8 (known from Uçar, DGGW and Schueth) and Prop. 4.1 (classical), the problem is finite-dimensional Diophantine algebra. There is almost no geometric analysis. The only analytic content is Thm 4.4, which the authors call classical in substance.
2. "Finitely many heat invariants do not see moduli" is trivial in constant curvature.
3. The resource measure is a prefix of the heat sequence, and it is not canonical. For triangle orbifolds 12c_2+2 = S_1+R with S_1 an integer and 0<R<1, so c_2 alone determines (S_1,R) and c_1 is redundant. Integrality lets one coefficient carry several power sums.
4. The growth is only reduced to the open N(k)=O(k). The gap between √A and A is not narrowed beyond classical PTE bounds. The small-L data (Example 3.12: f >= L+1 already at A/2π ≈ 2L−3) suggest linear growth but prove nothing.
5. The strong known results (the spectrum determines the cone orders; all heat invariants do, per Uçar) are acknowledged. What remains is a quantitative and arithmetic contribution, genuine but narrow. Its fit for J. Geom. Anal. is doubtful.

## 3. Correctness: what I recomputed

I found no mathematical error in the theorems. The items below are what I reran.

**Heat coefficients.**
- I rebuilt p_l and α_k from (4)–(5) with sympy.
- I reproduced (7) and (9). For (2,8,8) and (3,3,12): c_1 = 1/8, c_2 = 67/48, c_3 = −1601/480 and −867/160.
- The differences d_3 = 25/12, d_4 = −1775/24, d_5 = 153025/48 match the paper.
- I integrated the elliptic term E_m(t) numerically (mpmath) from the stated Selberg formula. The residual against the 6-term series scales like t^6, so (5) is the correct asymptotic series of that term.
- I checked the closed form of Φ_m (Lemma 2.7) numerically.
- I could not independently check the trace formula itself (taken from Dryden–Strohmaier/Hejhal). Its constant term does match the known DGGW c_2 = χ/6 + Σ(m²−1)/(12m).

**Triangle collisions.**
- I enumerated all hyperbolic triads in exact rational arithmetic.
- There is no collision for p+q+r <= 17. The only collision at sum 18 is {(2,8,8),(3,3,12)}.
- The collision-free sums up to 2500 are exactly the paper's list (the largest is 557, and there is none in (557,2500]).
- I did not extend this to 4800.
- The first-collision examples I looked at agree with Table S3.
- Stratum overlap thresholds S*(p), p=2..40 and S<500, show no mismatch with Thm 5.4.

**Elliptic curve (Thm 5.10).**
- All 12 listed points lie on C_{27/2}.
- ψ maps E into C symbolically.
- The point orders 2, 3, 6 are confirmed by the group law.
- #E(F_7) = #E(F_11) = 12.
- My own 2-isogeny descent (local-solubility search) gives n_1 = 4 and n_1' = 1, so rank 0. This is conditional on my p-adic search, but the paper's mod-5 argument for E also checks by hand.
- Hence E(Q) ≅ Z/2 × Z/6.

**Theorem B.** I checked det M = (−1)^{n(n+1)/2} ∏(m_i+m_j)/∏m_i, and that the true e solves (11). This was exact, for n=2,3,4 and several integer multisets.

**Stability tables.**
- The amplification row sums (2, 14, 498, 4062, 56230/3) and P_3 = −18c̃_1 − 120c̃_2 − 360c̃_3 are reproduced.
- I ran the recovery chain at all sign corners. Orders are recovered at δ_cert for (2,8,8), (3,3,12), (3,10,15,30) and (2,3,7).
- At least one corner fails just above δ_up. The Table 1 values are reproduced.
- I did not verify the proof of Prop. 6.9 or δ_thm.

**Witnesses.**
- Thm C(3), Ex. 3.6 and Ex. 3.12(i),(ii) share exactly the claimed number of invariants.
- A C++ exhaustive search for n=4 with orders <= 440 finds exactly 107 primitive witnesses. Exactly 6 of them have no pencil splitting, including (16,16,74,74)/(11,37,44,88).
- For n=5 with orders <= 120, there are 216,071,394 multisets and no witness. This matches the paper.

**Hand checks.** These were Lemma 2.4, Lemma 2.6, Thm A, Thm 3.4, Cor. 3.5, Prop. 3.9, Thm 3.8 (Descartes), Thm 3.11(b)–(e) and the Rouché step of Thm 6.5. I found no error. The Remark 3.13 example {1,1,1,1,7} has one partner triple of positive reals (roots ≈ 0.266, 4.283, 6.451), not "three partners".

**Not recomputed:**
- the FEM spectra and the Section 7 fits;
- the pencil-configuration counts 15/35/25/61;
- Example 3.12(iii) (L=4..7);
- the proof of Prop. 6.9;
- Prop. 5.9 for S in (2500, 4800].

## 4. MAJOR issues

**M1. "How many invariants" is a non-canonical measure, and the growth question is not resolved (Thm 1.1(ii), Thm 1.2, abstract).**
- Problem:
  - K_mult counts a prefix of the heat sequence. With integer orders, c_2 alone determines (S_1,R) for triangle orbifolds, and c_1 is redundant.
  - The sum p+q+r is not a geometric parameter. Two invariants suffice again at many larger sums (19, 21–25, 27–30, 33, 41, ..., verified to 2500), so "the exact threshold at which two invariants stop sufficing" overstates a first-failure statement.
  - f(A) is pinned only between ~√A and A/π+4. Linear growth is shown equivalent to the open N(k)=O(k). That is a reduction, not a growth theorem.
- Why it blocks acceptance: the abstract and Theorems 1.1/1.2 present sharp thresholds and a growth law that the paper does not establish.
- Resolution:
  - State plainly that the growth is open and equivalent to a PTE problem.
  - Replace "threshold" by "first failure".
  - Discuss prefix counts versus arbitrary subsets of coefficients, for example whether c_2 alone suffices for triangle orbifolds.
  - Justify the choice of resource measure.

**M2. Theorem 1.3 (stability) does not address the geometric inverse problem (Sect. 6, abstract, Remark 6.1).**
- Problem:
  - The Hölder exponents 1/k concern data that are not heat invariants of any orbifold. The extremal data for k>=3 are not realizable, as the authors admit.
  - For realizable real-order data, 1/2 is shown sharp only for a double order and for all-equal orders. "Real orders" are never tied to a geometric object. Cone surfaces with non-integer 2π/m would need Schueth-type coefficients, or the claim should be declared algebraic.
  - For orbifolds the orders are integers, so the geometric content is a discrete rounding threshold (Thm 6.8), where Hölder exponents play no role.
  - The constants depend on the unknown true orders (a-posteriori only).
  - The error model is on c_1..c_n, not on eigenvalues. Extracting c_j from a spectrum is ill-posed. The series diverges like l!(144/π²)^l at order 12, as the authors note. The tolerances in Table 1 (down to ~1e-7 relative for n=4 and ~1e-5 relative for n=5) show how demanding the input is.
- Why it blocks acceptance: "we prove stability estimates for recovering cone orders" and "no earlier quantitative stability estimate" suggest a spectral stability result that is not proved.
- Resolution:
  - Present Sect. 6 as the conditioning of an algebraic map.
  - Separate the geometric part (integer rounding) from the formal part.
  - Either add a bound from eigenvalue or trace errors to c_j errors, or drop the novelty claim.

**M3. Positioning and novelty claims (Sect. 1.1).**
- Problem:
  - "First explicit finite number", "first sharp threshold" and "no earlier quantitative stability estimate" are asserted without a systematic search shown.
  - Philippe [17, Thm A] is described as showing that "a hyperbolic triangle group is determined by its length spectrum, in practice by its first two or three lengths". The cited paper treats triangle groups (2,p,q) only. The "first two or three lengths" claim is not supported by its abstract.
  - [39] is used to support the openness of N(k)=o(k²), but it concerns Wright's generalisation.
  - Context for an inverse-spectral readership is missing:
    - Brooks–Perry–Petersen compactness and finiteness (the route of Stanhope and Dryden);
    - Sunada-type and arithmetic isospectral constructions;
    - Zelditch and Hezari–Zelditch heat/wave-invariant inverse results;
    - the Wolpert and Osgood–Phillips–Sarnak side of the "heat versus whole spectrum" dichotomy.
- Why it blocks acceptance: the key comparison with the length-spectrum literature is misdescribed, and the "first" claims are unsubstantiated.
- Resolution: correct the Philippe description, add the missing context, and temper or document the "first" claims.

## 5. MINOR issues

- **m1.** Remark 4.7: the "weak orbifold substitute for Wolpert's theorem" along a "Thurston length coordinate" is asserted without a precise definition or proof. The argument is short (the coordinate is itself a length and must lie in the countable length spectrum). It should be given.
- **m2.** Sect. 7 and the supplement. The "certified" blind recovery rests on a-posteriori eigenvalue errors (not enclosures) and heuristic error bars. The authors admit that the double-window recomputation was not run and that the missing-eigenvalue test is blind above ~1.6e4. They also say the recovery test is "easy by design". None of this is used in a proof. Either run the recomputation or say "validated" instead of "certified".
- **m3.** Data availability points to GitHub Ali-M658/Arithmetic-verification, whose owner is not an author. The manuscript mentions `bash code/run all.sh`, and the supplement an internal path (theory/revision/collision witnesses.csv). Provenance and naming should be made consistent.
- **m4.** Prop. 5.9 is computational for S <= 4800. The paper does not say whether finiteness of the collision-free sums is expected or proved (I checked only to 2500).
- **m5.** Lemma 2.5 re-proves admissibility of the heat function in the trace formula. This is standard. It is correct but adds length.
- **m6.** Remark 3.13: "admits three positive real partners" should read "a partner triple of positive reals".
- **m7.** Fig. 2 shows exact K_mult only for s <= 7/5, while the axis runs to 1000. The caption should say that beyond that only bounds and constructed pairs appear.
- **m8.** The upper bound floor(A/π)+4 is likely far from sharp, and the small-L data point toward linear growth. The paper should say which way the evidence points.

## 6. Presentation

- **P1.** The paper is long (35 pages plus a supplement) and mixes four subjects (trace formula, PTE algebra, elliptic curves, numerics). The arithmetic of Sect. 5 and the stability section could be separate papers. The companion [20] is "in preparation", and Sect. 5 leans on it for context.
- **P2.** Sect. 6 notation (I_n, Ψ_k, key2, Ξ_μ, cond, ζ_n, r_n) is heavy. A summary table would help.
- **P3.** Fig. 2 (log axis, mixed markers) is hard to read. Fig. 1 is clear.
- **P4.** The Introduction should say early that the problem reduces to power sums of the orders and that no spectral input beyond Prop. 2.8 is used.
- **P5.** I found no formula typos in what I checked. For example, the d in Lemma 3.3 is correct as printed. The apparent sign error in plain-text extraction is an artefact.
- **P6.** In its favour, the paper is internally consistent and uses exact arithmetic. It states its limitations honestly and flags where claims are only a-posteriori.

## 7. Recommendation

**Major revision.** Confidence is high on correctness of what I recomputed and moderate on fit and novelty.

What is good:
- the closed-form derivation of the heat coefficients, which is independent and correct;
- the clean reduction to an odd-power-sum problem;
- the explicit area-based upper bound;
- the verified triangle-orbifold first failure with its elliptic-curve isolation;
- the correct equivalence of linear growth with N(k)=O(k);
- every computational claim I reran reproduced.

What would resolve the issues:
- **M1:** reframe the thresholds and the growth law honestly. Address the prefix-count convention.
- **M2:** restate or extend Thm 1.3 so that it concerns spectral data. Otherwise confine it explicitly to the algebraic map and the integer rounding threshold.
- **M3:** correct the Philippe description, add the missing literature, and substantiate or temper the "first" claims.
- Consider whether the arithmetic content belongs in a number-theory venue, with the geometric content condensed.
