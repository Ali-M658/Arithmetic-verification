<!-- Round 10, A-d, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

I could not save the report: the write to REPORT.md was refused (subagents are not allowed to create report files). The full report is below. My scratch code is in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/A-d-fuchsian-triangle-groups/scratch/code/.

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (submitted to AGAG)

**Referee D.** My expertise is Fuchsian triangle groups and the geometry of hyperbolic orbifolds: explicit trigonometry, closed geodesics, and the trace formula with elliptic terms.

**Scope of this report.**
- **Manuscript:** Section 5 (pp. 37–44), Section 6 (pp. 45–48) and Appendix F (pp. 59–60), plus the parts of Appendix C (pp. 55–56) and Appendix D (p. 56) that these sections use.
- **Supplement:** Sections S2–S6 (pp. 7–15) and the matching parts of S8.
- **Statements I relied on:** eq. (10), Lemma 2.11, Lemma 3.6, Theorems 3.2, 3.3 and 3.7, Corollary 4.1 and Problem 5.
- The placeholders (author contributions, AI-use statement, Zenodo DOIs, preprint identifiers) are treated as known.
- Every page reference below was checked against the rendered page image.

## 1. Summary of the part reviewed

**Section 5: triangle orbifolds.** By eq. (10), the first two heat invariants of O(p,q,r) carry exactly key₂ = (S₁, R), and c₃ adds P₃. The section proves the following.
- **Corollary 5.1.** Three invariants determine a triangle orbifold among all triangle orbifolds.
- **Proposition 5.2 and Corollary 5.3.** Against all of Sig, a rival that shares c₁, c₂, c₃ must be a sphere with four cone points (a ≤ b ≤ c ≤ d, a ∈ {2,3}, disjoint from {p,q,r}). So four invariants always suffice. Whether three suffice is equivalent to a Diophantine system (Problem 5).
- **Strata analysis (Lemmas 5.4–5.5, Theorems 5.6–5.7).** Triads of a fixed sum are grouped by their least order p. This gives:
  - key₂ is injective for S₁ ≤ 17 (Theorem 5.8);
  - the minimal collision is O(2,8,8) / O(3,3,12) at S₁ = 18. It is unique, of least area, and the unique least-area pair even among all pairs in Sig sharing c₁, c₂ (Theorem 5.9).
- **Theorem 5.10.** Collisions of two triads with Λ = S₁R are positive rational points on the Bremner–Guy–Nowakowski cubic C_Λ. C_{27/2} is an elliptic curve with Mordell–Weil group Z/2 × Z/6 and rank 0 (a hand 2-isogeny descent, Appendix F). So the scaled pairs O(2k,8k,8k), O(3k,3k,12k) collide with no third triangle orbifold.

**Section 6: stability.** This studies the algebraic map from (c₁,…,cₙ) to the real cone orders of a sphere with n cone points. It has three layers:
1. a triangular front end (Proposition 6.1, with amplification constants amp_r);
2. the linear system of Theorem 3.3, with the Hurwitz factorisation of Lemma C.1;
3. Rouché's theorem.

The results are:
- Lipschitz recovery at simple orders and Hölder-1/k recovery at k-fold orders (Theorem 6.2, constants in Appendix C), with sharpness statements (Propositions 6.3–6.4);
- an explicit rounding threshold δ_thm (Theorem C.4) and an a-posteriori criterion (Corollary 6.5);
- in supplement S3, a sharper exact-arithmetic certificate (Proposition S3.1) and Table S4.

**Supplement S4–S6.** These are numerical illustrations:
- finite-element spectra of the minimal pair, about 2850 eigenvalues each;
- a fit of D(t) = Z_{O(2,8,8)} − Z_{O(3,3,12)} that recovers d₃ and d₄;
- a blind recovery of both signatures from three fitted coefficients;
- a one-parameter family of signature (0;3,3,3,3) whose heat traces agree up to the closed-geodesic terms.

## 2. Significance

**What is good.**
- Section 5 answers, precisely and correctly, the question Dryden–Gordon–Greenwald–Webb left informal in their Rem. 5.16: how weak c₂ is on the triangular pillows.
- Corollary 5.3 (four invariants against all of Sig) is clean and honest. Its reduction of the "three invariants" question to Problem 5 is exact.
- Theorem 5.9's last assertion, that the minimal pair is the unique least-area pair in the whole of Sig, is a nice touch.
- Theorem 5.10 is a tidy use of arithmetic geometry for a spectral statement.
- Section 6 and Appendix C are careful and fully explicit. As far as I could recompute them, they are numerically exact.
- The supplement's numerics are well documented and self-critical: every place where something is "validated, not proved" is flagged.

**Reservations.** These are developed in M1 and M2.
- Once eq. (10) is in hand, the triangle part is elementary arithmetic. The authors themselves call Theorem 1.4(i)–(ii) "in substance a finite verification" of 83 triads (p. 43). Theorem 5.6 for general p and Proposition D.1 are used by no main result.
- The one genuinely geometric open point of the section, whether three invariants suffice against all of Sig, is left open as Problem 5, with only modest searches.
- Section 6 analyses the stability of an algebraic recovery map on real orders. Its link to the heat trace (Corollary 6.5) needs a proved data error δ₁. By the authors' own Remark B.6, such a δ₁ cannot be obtained from computed spectra.

Neither reservation is a correctness issue. Both bear on how much these sections add for an AGAG reader.

## 3. Correctness, and what I recomputed

Unless noted, I recomputed in exact rational arithmetic (sympy and Python Fractions). **Every number I checked agrees with the manuscript.**

### Section 5 (pp. 37–44)

- **Eq. (10).** I rebuilt p₀–p₃ from (4) and (5) and the area coefficients α_k. They give eq. (10) and (8).
- **Minimal pair data.** The exact values are:
  - key₂ = (18, 3/4), and P₃ = 1032 versus 1782;
  - c₂ = 67/48;
  - d₃ = 25/12, d₄ = −1775/24, d₅ = 153025/48;
  - exact c₃ = −1601/480 and −867/160.
- **p. 38.** O(5,5,5) and (0;2,2,2,10) do share c₁ and c₂, with area 4π/5.
- **Proposition 5.2, case analysis.** Every case is correct:
  - the five-point families {2,2,2,2,x} and {2,2,2,3,x} for x = 3, 4, 5, with (p+q+r)R equal to 1 + 6/x, 10/6, 11/12 and 12/30;
  - the (1;m) case;
  - a ∈ {2,3};
  - disjointness via Theorem 3.7 with L = 3, since |U*| + |V*| ≤ 6 < 8.
- **Corollary 5.3.** The proof is correct.
- **Searches after Corollary 5.3.** I re-ran both: {2,2,c,d} with d ≤ 1000, and b ≥ 3 with c ≤ 11 and d ≤ 20000.
  - For each candidate I solved exactly for e₁, e₂, e₃ of {p,q,r} and tested for integer roots ≥ 2 (619,593 candidates; I discarded those with S₁R < 9).
  - There is no solution, as the paper states. The claim c ≤ 11 is right.
- **Lemma 5.4 and the formulas used in Theorem 5.6.** I verified symbolically:
  - eq. (15);
  - φ_p − τ_p = −(p−1)(S−3p−2)(S−x*)/(…);
  - φ′_p;
  - gap_p(3p+7) = −2(p²−5p−30)/(p(p+1)(p+3)(p+4)(p+5)).
- **Specific gap values.** All exact:
  - the gaps 1/840, 1/2310 and 1/10296;
  - the seven negative gaps at S*(p)+1, from −7/936 to −17/4680;
  - gap₂(9) = gap₂(10) = 1/12, R⁻₁₈,₃ = 101/168 and R⁻₁₉,₃ = 7/12.
- **Theorem 5.6, brute force.** For every S ≤ 600, the actual overlap of adjacent strata agrees with the criterion S ≥ S*(p) whenever S ≥ 3p+3. There are no exceptions.
- **Table S2.** Reproduced exactly: all 13 first collisions, and the gap is 0 only for p = 2 and p = 4.
- **Non-adjacent strata.** The first collision joining non-adjacent strata is (5,15,15) / (7,7,21) at S = 35, as stated.
- **Table S3.**
  - There are 83 triads, with counts 1, 3, 6, 7, 9, 11, 13, 15, 18 for S₁ = 10, …, 18.
  - I parsed the printed table: all 83 values of R are correct.
  - The only coincidence is the bold pair.
- **Computation S2.1.** My independent exact integer-key enumeration up to S = 4800 gives exactly the 38 collision-free sums listed. S = 557 has 25,575 triads, as stated.
- **Theorem 5.9.**
  - The majorisation bound is correct: 2/3 + 1/(S−6) ≤ 3/4 exactly when S ≥ 18.
  - Of the four-cone-point signatures, only (0;2,2,2,3) (area π/3) and (0;2,2,2,4) (area π/2) have area at most π/2.
  - Their paddings give (p+q+r)R = 20/3 and 27/4, both below 9, so they are excluded.
- **Fig. 7.** The dots and circles match the exact first overlaps and first collisions, for example (19, 7/12), (38, 19/42), (34, 0.3095), (62, 0.221) and (117, 0.244).

### Theorem 5.10 and Appendix F (pp. 44–45, 59–60)

- **The model.** ψ maps E into C_{27/2}, and φ∘ψ = id on E. I checked both symbolically, modulo the equation of E. Also:
  - φ(1:4:4) = (−24, 360);
  - ψ(216, ±5400) = (1:0:0) and (0:1:0);
  - Δ(E) = 2¹⁸3⁸5⁶.
- **Torsion.**
  - #E(F₇) = #E(F₁₁) = 12, and also #E(F₁₃) = 12.
  - All eleven affine points lie on E. The group law gives three points of order 2, (16, ±400) of order 3, and six points of order 6.
  - The tangent line is a flex: x³ + 393x² + 3456x − (21x+64)² = (x−16)³.
- **Points of C_{27/2}.** The twelve listed points lie on C_{27/2} and are distinct.
- **LMFDB.** I fetched the page for 90.c3 (Cremona label 90c6). Its minimal model [1,−1,1,−3002,63929] has c₄ = 144081 = c₄(E)/2⁴ and c₆ = −54586521 = c₆(E)/2⁶. LMFDB lists rank 0 and torsion Z/2 ⊕ Z/6, so the isomorphism claim is correct.
- **Appendix F descent.** I checked it line by line and it is correct:
  - c′ = −786 and d′ = 3²5⁶;
  - on E, the mod-5 argument for d₁ ∈ {±2, ±3};
  - the 2-torsion points map to the classes 1, 6, −1, −6;
  - on E′, the cases d₁ = 3, 5, 15, including the mod-9 step: 5w² − w + 2 ≡ 6 for w ∈ {1, 4, 7};
  - hence e₁ = 2, e′₁ = 0, and the rank is 0.
- **Not rechecked.** I did not rerun PARI's `ellrank` (PARI is not installed here). The hand descent and LMFDB make this unnecessary.
- **Isolation beyond triangle orbifolds.** For k ≤ 8, no non-triangle orbifold shares c₁, c₂ with O(2k,8k,8k).
  - By Lemma 3.6 the only candidates are spheres with four or five cone points and genus-1 orbifolds with two cone points.
  - The same search does find O(5,5,5) / (0;2,2,2,10), so the code detects such pairs.
  - See m2.

### Section 6 and Appendix C (pp. 45–48, 55–56)

- **Proposition 6.1.** amp₀,…,amp₄ = 2, 14, 498, 4062, 56230/3, and P₃ = −18c̃₁ − 120c̃₂ − 360c̃₃.
- **Lemma C.1 and Theorem 3.3.** I verified B = YM, det B = (−1)^{n(n−1)/2} ∏(mᵢ+mⱼ), and det M = ς_n ∏(mᵢ+mⱼ)/∏mᵢ exactly for (2,8,8), (3,5,7,11) and (2,3,4,9,13).
- **Theorem C.2.**
  - (a): the Hadamard argument and the row-sum bound 2^{n−1} are correct.
  - (b): the majorant argument is correct.
  - ζ₃, ζ₄, ζ₅ = 1, 79/3, 14048/15.
- **Theorems C.3 and C.4.** The Rouché constants are right: |q̃ − q| < 2^{1−n}3ⁿε. The third term of δ_thm is exactly the condition r_a ≤ 1/2.
- **Corollary 6.5.** The logic is correct.
- **Table S4, δ_thm column.** I recomputed it for all eleven multisets using the exact cond. All values match the table, for example (2,8,8): 3.80e−7 and (2,2,2,2,3): 2.72e−12. The largest exact cond is 3.5109, matching "at most 3.511" (p. 56).
- **Table S4, δ_up column.** I recomputed δ_up for (2,8,8), (3,3,12), (4,4,4), (2,3,7) and (7,7,7) by an independent multistart minimisation. I get 2.4849e−3, 4.5883e−3, 5.0358e−4, 6.5869e−3 and 8.2721e−5. These agree with the table after its rounding up. I found no failure below δ_cert, which is an independent consistency check of Proposition S3.1.
- **Table S4, other columns.** All δ_cert/|c_j| entries are reproduced to the printed digit. In every row ε_cert ≥ min_j δ_cert/|c_j|.
- **Ratios quoted on p. 47.** δ_up/δ_thm ranges over roughly 539 to 1.86×10⁸, and δ_up/δ_cert over 1.03 to 6.72, as quoted.
- **Proposition S3.1.** For (2,2,2,2,3), sech²U = 1 − 121z² + 9328z⁴ − 601472z⁶ is correct.
- **Propositions 6.3(i) and 6.4.** Correct: δR = s²/(4(64−s²)), δP₃ = 48s², and the constant 498 + 42a².
- **Table S6.**
  - Solving the n = 3 system from the printed estimates gives roots 2 and 8 ± 0.00502i for specimen A, and 2.99154, 3.00851, 11.99995 for specimen B.
  - The exact c₃ lies within the printed error bars.
  - The quoted margins of about 100 and 20 are consistent with δ_cert.

### Section 4 and supplement S4–S6

- **Closed geodesics.** Enumerating words of length ≤ 9 in explicit SL(2,R) generators gives these shortest lengths, exactly as in S4:
  - (2,8,8): 2.2568, 2.8816, 3.0571;
  - (3,3,12): 1.8626, 2.9807, 3.4027.
- **Size of the geodesic term.** For O(3,3,12) it is 4.0e−13 at t = 0.0293, 8.0e−13 at t = 0.03 and 2.7e−15 at t = 0.025, as stated.
- **Sign change of D(t).**
  - The exact elliptic difference (by quadrature of Theorem 2.3) peaks at about 0.048 near t = 0.12–0.2 and is still +0.044 at t = 0.36.
  - Adding the five shortest geodesics, each with multiplicity 2, makes D change sign between t = 0.34 and 0.36.
  - This confirms "solely because of the geodesics" and the shape of Fig. 5(a).
- **Bolza and Weyl checks.**
  - The Bolza covering of O(2,8,8) is consistent: χ = −1/4.
  - "Four characters" at the π/3 corner is correct.
  - The Weyl law, with triangle area π/4 and perimeter 5.505, gives about 1421 Neumann eigenvalues below 21,700 and about 1419 Dirichlet eigenvalues below 23,800, matching 1420–1440. About 2001 orbifold eigenvalues lie below 1.6×10⁴.
- **(0;3,3,3,3) family.** The Lambert relation sinh a sinh b = 1/2 gives 4b(0) = 2.634 and 4b(2.8) = 0.694.
- **Introduction.** The scales are correct: 0.546, (π/12)² = 0.0685 and ℓ²/4 = 0.867.
- **Not recomputable.** The finite-element spectra, the completeness claims and the fits cannot be recomputed from the manuscript. They are used in no proof.

**Conclusion on correctness.** I found no mathematical error in Section 5, Section 6, Appendices C (as used), D or F, or in any number of Tables S2–S4 and S6.

## 4. FATAL

None.

## 5. MAJOR

**M1 (pp. 38–44, 48; Problem 5): the geometric question of Section 5 is left open, and what is proved is elementary.**
- With (10) in hand, Theorems 5.7–5.9 reduce to injectivity of (S₁, R) on 83 triads.
- The strata machinery (Lemma 5.5 and Theorem 5.6 for general p, Proposition D.1, Fig. 7, Table S2) is, by the authors' own statement on p. 43, used by no main result.
- The geometric statement that the section builds towards is left as Problem 5: whether c₁, c₂, c₃ determine the signature of a triangle orbifold among all of Sig (K_mult ≤ 3). The evidence is searches with d ≤ 1000 and d ≤ 20000. I reproduced them, but they are modest.

What resolves this, in order of preference:
- (a) a proof for a natural sub-family. The case {2,2,c,d} looks accessible: there R(p,q,r) = 1/c + 1/d, p+q+r = c+d+3, Σp³ = c³+d³+15, and S₁R ≥ 9 already forces d ≳ 7.8c;
- (b) a reduction of Problem 5 to a finite check;
- (c) failing both, re-weight the abstract and introduction so that "four against all of Sig" is the main geometric result, the triangle-internal counts are presented as elementary, and the general-p strata results are marked as structural where they are stated.

**M2 (pp. 45–48, Appendix C, S3, S5): the geometric content of Section 6 is thin, and its link to the heat trace is not usable as stated.**
- Lipschitz and Hölder-1/k recovery follow from invertibility of M plus Rouché, as for any polynomial root problem. What is new is the explicit constants and the certificate.
- The geometric payoff is Corollary 6.5. It needs a proved δ₁, which the authors say (p. 47, Remark B.6) requires times shorter than computed spectra resolve.
- The accuracies required are severe:
  - δ_cert/|c₃| = 7.0e−4 for (2,8,8);
  - δ_cert/|c₃| = 3.6e−7 for (3,10,15,30);
  - δ_thm is as small as 2.7e−12.
- The S5 blind recovery uses heuristic error bars and is "easy by design".

What resolves this:
- either give one end-to-end statement for the minimal pair: which times and which accuracy of Z(t) Lemma B.5 needs to certify δ₁ ≤ δ_cert(2,8,8) = 2.3e−3, and how far that is from what the computed spectra deliver;
- or reframe Section 6 in its opening paragraph as a statement about the algebraic recovery map, not about orbifolds.

## 6. MINOR

- **m1 (p. 42, proof of Theorem 5.9).** "A pair of genus-0 signatures with three cone points and area π/2" should read "area at most π/2".
- **m2 (p. 5, Theorem 1.4(iii); p. 44; abstract).** "Isolated" means isolated among triangle orbifolds. For k = 1, Theorem 5.9 already gives isolation in all of Sig, and my search finds no non-triangle orbifold sharing c₁, c₂ with O(2k,8k,8k) for k ≤ 8. Either state the triangle-only scope in the abstract, or prove the stronger statement; for each k the candidate set is finite.
- **m3 (pp. 41–42).** The proof of Lemma 5.5(ii) forward-references the sign computations (a), (b) in the proof of Theorem 5.6. Put the two sign facts for p = 2 in a lemma placed before Lemma 5.5.
- **m4 (p. 43 vs p. 42).** The paper says no main result depends on Theorem 5.6 for general p. Yet the proof of Theorem 5.7 invokes S ≥ S*(p) ≥ x*(p) ≥ 18 for all p. Rewrite that proof for p ≤ 6 only.
- **m5 (p. 44, "Rank").** Give the full change of variables [u, r, s, t] to [1,−1,1,−3002,63929], not just "u = 2"; r, s, t are nonzero because a₁ = a₃ = 1. Also cite the Cremona label 90c6.
- **m6 (p. 45, "Torsion").** Add a precise citation for injectivity of reduction on torsion, e.g. Silverman, AEC VII.3.1 / VIII.7.1.
- **m7 (pp. 59–60, Appendix F).**
  - State that "5 | e" includes e = 0, the points at infinity of the quartic.
  - State that n₁ counts the image of E(Q) in Q*/Q*², torsion included.
  - Rename c, d, e, M, N, n₁ and O: they clash with the heat invariants c_j, the cone orders c, d, the elementary symmetric functions e_k, the matrix M of Section 6, and the orbifold O.
- **m8 (p. 47, Fig. 8).** The axis label ‖m̃ − m‖_∞ does not match the dist (minimum over permutations) used in the text. Use the same symbol.
- **m9 (supplement p. 12).** The printed numbers give a d̂₂ deviation of 0.52 of its error bar, not "0.53". Either give the unrounded bar or recompute.
- **m10 (supplement p. 14, S6).** Replace the "annulus whose double is a torus" argument with the standard fact that an anticonformal involution of the sphere fixes either a single circle or nothing. Also make the Möbius normalisation precise: four concyclic points in cyclic order can be moved to the vertices of an inscribed rectangle.
- **m11 (supplement p. 13).** "c₃ differ by 2.0833 ± 1.6e−4": the printed estimates give 2.0832818. Print 2.08328, so the 5e−5 deviation from 25/12 is visible.
- **m12 (p. 40).** State whether the search uses the filter S₁R ≥ 9, and give the number of candidates examined.

## 7. Presentation

- **P1 (supplement pp. 7–8).** Proposition S3.1 is split by Tables S2 and S3. Place the tables after the proposition.
- **P2 (p. 39, Fig. 6).** Name the vertex at the centre of the "distance at most 2.4" cap.
- **P3 (p. 44).** O is used for both the orbifold and the base point (1:−1:0). E is used for both the elliptic curve and the elliptic term E(t) of Theorem 2.3. Use different letters.
- **P4 (p. 40).** Turn the parenthetical about R⁺_{S,2} into a sentence after Lemma 5.4.
- **P5 (p. 38).** Write "equal area (equivalently equal R)".

## 8. Recommendation

For my assigned parts: **minor revision** on correctness and exposition, with **high confidence**. I independently reproduced every number in Sections 5–6, Appendices C (as used), D and F, and Tables S2–S4 and S6, and found no error.

M1 and M2 are significance and framing concerns for the editor, not defects in the proofs. Without progress on Problem 5 or an end-to-end statement for M2, Sections 5–6 are a correct but modest contribution. Together with the rest of the manuscript, this would support **major revision** rather than acceptance at AGAG.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Prove Problem 5 for {2,2,c,d}, or reduce Problem 5 to a finite check; otherwise re-weight the claims in the abstract and introduction. |
| M2 | Give an end-to-end Lemma B.5 certificate for the minimal pair, or reframe Section 6 as concerning the algebraic recovery map. |
| m1 | Write "area at most π/2". |
| m2 | Restrict "isolated" to triangle orbifolds, or prove isolation in all of Sig. |
| m3 | Move the p = 2 sign facts into a lemma before Lemma 5.5. |
| m4 | Rewrite the proof of Theorem 5.7 for p ≤ 6. |
| m5 | Give [u,r,s,t] and the label 90c6. |
| m6 | Add the precise citation. |
| m7 | Add the two clarifying sentences; rename the clashing letters. |
| m8 | Make the axis label match dist. |
| m9 | Give the unrounded bar or recompute. |
| m10 | Replace the argument as indicated. |
| m11 | Print 2.08328. |
| m12 | State the S₁R ≥ 9 filter and the candidate count. |
| P1–P5 | As indicated. |
