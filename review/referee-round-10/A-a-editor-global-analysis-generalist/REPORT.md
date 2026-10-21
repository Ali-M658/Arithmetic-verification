<!-- Round 10, A-a (editor), returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

I could not save the report: the write to `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/A-a-editor-global-analysis-generalist/REPORT.md` was refused ("subagents should return findings as text"). The full report is below. My decision is to send the paper to review, and my recommendation is major revision, with moderate confidence.

# Handling editor's report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

I wrote this as a generalist in global analysis on manifolds. I used only the manuscript (65 pp.), the supplement (19 pp.), the two disclosed related manuscripts, published literature fetched with curl (arXiv, OpenAlex, LMFDB), and my own computations. The scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/A-a-editor-global-analysis-generalist/scratch/code/`.

## Summary

The paper studies closed orientable 2-orbifolds of curvature −1 whose singular points are cone points (the class Sig). It asks how many heat invariants c1, …, ck are needed to fix the signature, that is, the genus and the multiset of cone orders.

- **Method.** It rederives the closed-form heat expansion from the Selberg trace formula, with signed remainders (Prop. 2.8, App. B). It then uses Uçar's triangular structure (Lemma 2.11): each new coefficient adds one new odd power sum of the orders. This turns the question into one about the odd power sums and the reciprocal sum of a signed multiset.
- **Bounded orders (Thm 1.1 / 3.11).** If every cone order is at most M:
  - the first M invariants separate within the class of such orbifolds;
  - the first M+1 separate against all of Sig, uniformly in the area;
  - both numbers are sharp, shown by Lagrange-weight constructions;
  - the upper bound against all of Sig comes from a sign-change (Descartes) argument.
- **Growth (Thm 1.2 / 3.18, Prop. 3.19).** Without an order bound, the largest number needed at area at most A, f(A), lies between about √A and A/π + 4. Each power-growth statement about f is equivalent to a statement about N(k), the least size of a Prouhet–Tarry–Escott solution of degree k. The paper says plainly that this is a reformulation of an open problem, not a solution.
- **Collisions (Thm 1.3).**
  - The determinant of the linear recovery system is given in closed form (Orlando/Hurwitz).
  - A Descartes-type bound limits how much the genus can change between two orbifolds sharing L invariants.
- **Triangle orbifolds (Thm 1.4, §5).**
  - Three invariants determine a triangle orbifold among triangle orbifolds.
  - Four determine its signature among all of Sig.
  - O(2,8,8) and O(3,3,12) are the least collision. They are also the least-area pair in all of Sig sharing c1 and c2.
  - The pair is isolated because the plane cubic C_{27/2} has rank 0 and torsion Z/2×Z/6. The rank comes from a 2-isogeny descent done by hand (App. F).
- **Variable curvature (§2.4).**
  - A conjecture on the structure of the cone terms (Conj. 2.13).
  - A proof of the part linear in the curvature jet (Prop. 2.14), via a parametric form of Donnelly's expansion (Lemma E.1).
  - A construction (Prop. 2.17): the minimal pair carries metrics, flat near the cone points, whose heat invariants agree to all orders.
- **Other material.** A stability theorem for recovering orders from approximate invariants (§6, App. C). Numerical illustrations from finite-element spectra (§4, Suppl. S4–S6), consistently labelled as not proofs.

## Significance and novelty

**What is good:**
- The question is natural and squarely in the inverse spectral geometry of orbifolds, a topic AGAG publishes (Stanhope 2005; Rossetti–Schueth–Weilandt 2008; Abreu–Dryden–Freitas–Godinho 2008; Schueth 2026).
- Attribution is unusually careful:
  - Uçar for the coefficients and the triangular mechanism;
  - Dryden, Gordon, Greenwald and Webb (DGGW) for c2;
  - Laurens and Karlin–Studden for the sign-change argument;
  - Bremner–Guy–Nowakowski for the cubic;
  - an explicit list of statements resting on computer search.
- As far as I can tell, these are new:
  - the exact area-free answer M+1, with matching constructions (Thm 3.11(ii)–(iv));
  - the Descartes bound on the imbalance (Thm 3.15);
  - the dictionary between pairs of orbifolds and "L-configurations", with the T(L)/N(k) sandwich (Prop. 3.19);
  - the least-area statement in all of Sig (Thm 5.9);
  - the linear part of the cone terms at every order in variable curvature (Prop. 2.14);
  - Lemma E.1, a parametrix lemma uniform in a parameter, which I have not seen stated in this form.

**Literature search.** I searched arXiv and OpenAlex for heat invariants with orbifolds or orbisurfaces, curved conical singularities, and Prouhet–Tarry–Escott with spectral. No prior work answers the question of a fixed finite number against all of Sig. The closest items are all cited, or harmless:
- Uçar (arXiv 1711.03405): the whole sequence of heat invariants determines the orders;
- DGGW;
- Schueth (AIF 2019; AGAG 2026);
- Richardson–Stanhope (arXiv 1910.03224, local orientability): not cited, but it does not overlap.

One relevant paper is not cited: Suleymanova, arXiv 1711.00577, on curved conic singularities, which bears on §2.4.

**Reservations (the main obstacle to acceptance):**
- Once Uçar's triangular structure is granted, the counting theorems are elementary algebra of odd power sums: Newton's identities, Vandermonde/Lagrange interpolation, and Descartes' rule. The authors say as much on pp. 5–6.
- The analytic input (trace formula, coefficients) is classical. The genuinely analytic novelties are secondary to the main theorems: the signed remainders, the optimal truncation, Prop. 2.14 and Lemma E.1.
- The growth theorem settles no exponent.
- The authors themselves call the triangle results "in substance a finite verification" (p. 43).
- The global-analysis content that would justify AGAG over a combinatorics or number-theory venue is therefore thin relative to the paper's ambitions.

## Correctness, and what I recomputed

I found no mathematical error in any main result. Every main result (Thms 1.1–1.4, Cor. 1.5) is proved in full. None depends on Conjecture 2.13, the companion manuscript, or numerics. The open parts are stated as open: the exact growth exponent, Problem 5, and Tg(3).

**Checked by hand:**
- Thm 3.2, Thm 3.7, Lemma 3.10.
- Thm 3.11(i)–(iv) and Cor. 3.12.
- Thm 3.15, including the count of parity-changing gaps.
- Prop. 3.16 (the reciprocal sums cancel because 1 − 2⁰ = 0).
- Lemma A.1 and Prop. 3.19.
- Both directions of Thm 1.2(ii).
- Prop. 5.2 (the rivals with five cone points) and Cor. 5.3.
- Thm 5.9, including the least-area claim in all of Sig:
  - At area π/2 the triads with R = 3/4 are (2,5,20), (2,6,12), (2,8,8), (3,3,12), (3,4,6) and (4,4,4). Only the minimal pair shares its order sum.
  - The other area-π/2 signature, (0;2,2,2,4), has no triangle partner sharing c1 and c2.
- Lemma 2.4, Lemma B.1, and the structure of the proof of Thm 5.10.
- Prop. 2.17(iii). The construction needs a cap of negative total curvature when α0 > 1, and such a cap exists.

**Recomputed in exact or high-precision arithmetic:**
1. **Cone and area coefficients.** I recomputed p0–p3 and α0–α5 from (4)–(5), and checked the closed form of Φm in Lemma 2.7. p1 and p2 match (8), and p3/m matches the K³ term of Remark 2.16(b).
2. **Expansion against the trace formula.** I compared quadrature of Em(t) (m = 2, 3, 8, 12) and I(t) with the truncated series. The residuals have the predicted order. As the paper says, they deteriorate for m = 12 at t = 0.01.
3. **Heat invariants of the stated pairs.**
   - c2(2,8,8) = c2(3,3,12) = 67/48.
   - d3, d4, d5 = 25/12, −1775/24, 153025/48.
   - Each of these pairs shares exactly the stated number of invariants: (0;2¹⁰)/(1;4⁴); (5,5,5)/(0;2,2,2,10); (1;15)/(0;3,3,5,5); Example 3.21(i)–(ii); the M = 3, 4 pairs of Thm 3.11(ii); and (2;)/(0;2⁸).
   - Prop. 2.17(ii): the two example signatures both have c2 = 2/3.
4. **Thm 3.11 constants.** C = 6, 120, 2520, 362880 for M = 2–5. Least-genus areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} for M = 2–9.
5. **Triads.**
   - There are 83 hyperbolic triads with 10 ≤ S1 ≤ 18.
   - The first collision is (2,8,8)/(3,3,12) at S = 18.
   - The first collision across non-adjacent strata is (5,15,15)/(7,7,21) at S = 35.
   - Up to S = 600 there are exactly 38 collision-free sums, the last being 557. This agrees with the 38 claimed up to 4800, but I did not run the range above 600.
6. **Elliptic curve (Thm 5.10).**
   - All twelve listed points lie on E, and ψ maps them into C_{27/2}.
   - The discriminant is 2¹⁸3⁸5⁶.
   - #E(F7) = #E(F11) = 12.
   - j(E) = j(90.c3), and LMFDB lists 90.c3 with rank 0 and torsion [2,6].
7. **Systoles.** Enumerating words of length ≤ 11 gives 2.2568 for O(2,8,8) and 1.8626 for O(3,3,12). So ℓ²/4 ≈ 0.87 on p. 3 is correct.
8. **Stability constants.**
   - amp0–amp4 = 2, 14, 498, 4062, 56230/3, and the P3 row of F⁻¹ is (−18, −120, −360).
   - Remark B.6 reproduces: δ1 ≈ 4.9×10³τ with the uniform bound and ≈ 1.14×10³τ with the row bounds; τ ≲ 7.8×10⁻¹¹; and η ≤ 2.07×10⁻¹⁹ at τ = 10⁻¹¹.
9. **Prop. 2.14.** I redid the Duhamel computation and got λl = 2C^{−2l−2}/(l−1)!. This reproduces b1 = 2KΠ2 exactly and β2,3 = 12K² − 2ΔK. The rendered p. 17 is correct (the text extraction garbles it).
10. **Fig. 1 claim.** On the flat cone of order 12, at distance √t/sin(π/12) the value of 4πt·h is about 1.79, and it is within 1% of 1 beyond three times that distance. Correct.

**Physical framing.** It is accurate in substance:
- Locality (Kac's principle) holds.
- A cone point's influence extends to about √t/sin(π/m), from the Gaussian factor exp(−r²sin²(πj/m)/t).
- The trace on any interval of times determines the spectrum (real-analyticity plus Laplace-transform uniqueness).
- The series is asymptotic, not convergent: b_l grows like l!(m/π)^{2l}, and optimal truncation leaves an error of order e^{−π²/(m²t)}. This is consistent with the wave-trace poles at ±2πi/m in Remark 4.3.
- Closed geodesics enter only at order e^{−ℓ²/4t}, and orbifold cone points are non-diffractive.
- The paper correctly says the counts belong to the coefficient sequence, not to the duration of an experiment.
- Remark B.6 (which I checked) shows that a proved route from heat-trace values to c3 needs times of about 10⁻⁴ or less and accuracy of about 10⁻⁸, beyond the computed spectra.

The remaining framing problem is the title and abstract (M2), not any false statement.

## FATAL

None.

## MAJOR

**M1. Significance and depth for AGAG (pp. 5–9).** After Lemma 2.11 the main theorems are short applications of Newton, Vandermonde/Lagrange and Descartes to odd power sums. The growth theorem settles no exponent (pp. 6, 30). The triangle results are a finite check made conceptual. The authors must argue that the contribution is to global analysis, or foreground the analytic novelties: Prop. 2.14 with Lemma E.1, the signed remainders and optimal truncation, and Prop. 2.17.
*Resolves:* a revised introduction separating the analytic from the combinatorial content and arguing fit. Better still, strengthen §2.4, for example by proving Conj. 2.13(i) for rotationally symmetric germs; Suppl. S7 nearly does this.

**M2. Title and headline framing (title; abstract pp. 1–2; pp. 2–3).** Read literally, "How much … does heat hear?" is already answered:
- the heat trace on any interval is the spectrum;
- the spectrum determines the signature (Dryden–Strohmaier; Doyle–Rossetti).

The paper is about how many asymptotic coefficients are needed, as p. 3 concedes. The abstract also opens with heuristics and a caveat ("proved recoveries … use times shorter than computed spectra resolve") that obscure the results.
*Resolves:* retitle in terms of heat invariants, for example "How many heat invariants determine a hyperbolic orbifold?". State the theorems first in the abstract, with at most one sentence of caveat.

**M3. Heterogeneity and focus (§§2.4, 4, 6; Apps C, E; Suppl. S3, S5–S7).** The paper combines five near-independent strands:
- (a) power-sum counts and growth;
- (b) triangle orbifolds and an elliptic curve;
- (c) variable curvature, with a partial proof of a conjecture;
- (d) stability and recovery thresholds;
- (e) finite-element numerics.

Strand (d) is standard root perturbation, and by the paper's own Remark B.6 it cannot be applied to any computed spectrum. Strand (e) only illustrates proved facts and is shared with the companion. The certificate used for the sharper thresholds (Prop. S3.1) is a proved statement that exists only in the supplement.
*Resolves:* make (a)–(c) the paper. Move (d) and (e) to the supplement or the companion. Either bring Prop. S3.1 into the main text or stop using it.

**M4. Overlap with the disclosed manuscripts (pp. 7, 9; companion App. A; note §6).** The overlap is disclosed and is not duplicate publication of results, but:
- The eigenvalue companion reproves §§2–3 of this paper in its Appendix A. Its Lemma A.1 is essentially this paper's Lemma B.1, word for word.
- The two papers share the same finite-element spectra.
- Thm 5.10 is proved here by hand and reproved in the note by machine.
- The triad enumeration up to 4800 is the same computation as the note's.

*Resolves:* state the submission status of the companion and the note in the cover letter and §1. Remove the verbatim proofs from the paper that is not primary. Prove Thm 5.10 in one paper only and cite it in the other.

**M5. The variable-curvature headline (abstract p. 2; Prop. 2.17(iii), pp. 19–21).**
- The all-orders agreement claim in the abstract is correct. But it rests on a simple mechanism: an exactly flat orbifold cone point contributes only to c2, and the metrics are chosen so that every order-dependent term beyond c2 vanishes. That shows the question needs a curvature normalisation; it does not show some subtle instability.
- Prop. 2.17(i) needs the non-spectral hypothesis Ωl(O) = Ωl(O′).
- Conj. 2.13 rests on an outline (S7) with two acknowledged gaps (p. 16) and on computations for l ≤ 3 only.

*Resolves:* reword the abstract and p. 21, keep the conjecture strictly separate from proved statements, and ideally prove the symmetric case.

## MINOR

- **m1 (p. 4, Thm 1.2(ii); pp. 30–31).** Part of Thm 1.2(ii) is argued inside the italic statement of Prop. 3.19 rather than in a proof: the direction "f(A) = O(A^α) if and only if N(k) ≥ ck^{1/α}", and the o(A) statement. Thm 3.18(d), cited as the proof, contains only the lower-bound equivalence. Put the full equivalence in Thm 3.18 and give the argument as a proof.
- **m2 (p. 2).** The abstract places "isolated by an elliptic curve of rank 0" right after "unique pair of least area in the whole class". Isolation (Thm 5.10) is proved only among triangle orbifolds. For k = 1 it also holds in all of Sig by Thm 5.9, but not for O(2k,8k,8k) with k ≥ 2. Say so.
- **m3 (§2.4 and references).** Cite Suleymanova, arXiv 1711.00577, next to Schueth.
- **m4 (p. 26).** The letter a denotes both the interpolation nodes and, with a subscript, the leading coefficients a_l. The text flags the clash; rename one of them instead.
- **m5 (pp. 30–31, 47).** "N nondecreasing" is used in several proofs. State once, with its one-line reason (a solution of degree k+1 is one of degree k), before its first use.
- **m6 (p. 54, Remark B.6).** The remark uses the systole bound ℓ0 = 2.2567 certified in the companion; my enumeration gives 2.2568, so it is consistent. State that this is the only input from the companion and that no theorem uses it.
- **m7 (p. 12, Prop. 2.8; p. 45, Thm 6.2).** The caveat that b_l at non-integer m is only an algebraic device should be repeated in the statement of Thm 6.2.

## Presentation

- **P1 (pp. 1–2).** The abstract is dense and largely about what is not proved. Rewrite it as question, theorems, one caveat.
- **P2 (pp. 5–9).** Several sentences run ten lines or more and mix attribution, logic and bookkeeping (p. 5 on §6; pp. 6–7 on the companion). The paragraphs "What is elementary" (pp. 5–6) and "What is new" (p. 7) partly repeat each other; merge them.
- **P3 (pp. 15–21).** §2.4 reads as a separate paper. It is full of forward references and needs its own "no circularity" remark. Move it after §3 or into its own final section.
- **P4 (Fig. 1, p. 3; Fig. 4(a), p. 35).** Both figures are stylised drawings on surfaces that are not isometric to the orbifolds, and Fig. 4(a) shows genus-0 orbifolds with four cone points as smooth cylinders with no cone points marked. Mark the cone points, or use isometric disc pictures as Fig. 6 does.
- **P5.** I read the rendered Figs 2, 3, 5, 7 and 8; they agree with the text. Fig. 2 matches its multisets, Fig. 3 its bounds at s = 4 and s ≈ 2000, Fig. 5(a) the sign change near t ≈ 0.36, and Fig. 7 its dots and circles. I found no sign, typographical or figure errors.
- **P6.** The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) are treated as known.

## Overlap with the related manuscripts

- **Eigenvalue companion.**
  - Its main theorems are distinct: explicit N and δ for finitely many eigenvalues, a geodesic count without a diameter bound, and the cusp-like behaviour of O(2,3,m).
  - It reuses this paper's §§2–3 (its Table 1) and reproves them in its Appendix A, near-verbatim in places.
  - The spectra are shared.
  - The cross-dependencies are confined to remarks (Remarks 2.6 and B.6 here).
  - The shared statements are consistent between the two papers.
- **Note on triples (formatted for INTEGERS).**
  - It covers the arithmetic of the cubic pencil C_Λ: torsion, lower bounds on the number of collisions, Schinzel-type large classes, and an enumeration to 6000.
  - Its Λ = 27/2 data (Selmer classes ±1, ±6; rank 0; torsion Z/2×Z/6) agree with Thm 5.10 and App. F here.
  - The overlap is limited to Thm 5.10 and the shared enumeration, both disclosed.
- **Consistency.** I found no inconsistency among the three manuscripts in the numbers I checked: systoles, eigenvalue ranges, the Λ = 27/2 data and the c2 formula.

## Editorial decision and recommendation

- **Editorial decision: send to review.** The paper is in scope for AGAG, carefully argued, correct as far as I could check, and every main claim is proved. Neither correctness nor scope justifies a desk rejection.
- **Referees should be asked specifically about M1:** whether the analytic content, beyond Uçar's mechanism, is enough for AGAG.
- **Recommendation: major revision.** Confidence is moderate: high on correctness, moderate on significance.
- If the revision cannot show a more substantial global-analysis contribution (M1, M3, M5), I would lean to rejection. In that case I would suggest the power-sum and triangle-orbifold core go to a journal with a combinatorial or number-theoretic readership.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Introduction that separates the analytic from the combinatorial content and argues fit. Strengthen the analytic results: Prop. 2.14, Lemma E.1, and a proof of the symmetric case of Conj. 2.13. |
| M2 | Retitle in terms of heat invariants; abstract states the theorems first, with one caveat sentence. |
| M3 | Restrict the paper to strands (a)–(c). Move §6/App. C and the numerics to the supplement or the companion. Bring Prop. S3.1 into the main text or stop using it. |
| M4 | State the submission status of both related manuscripts. Delete duplicate proofs from the non-primary paper. Prove Thm 5.10 in one place only. |
| M5 | State the flat-cone mechanism plainly and keep Conj. 2.13 separate from proved statements, or prove its symmetric case. |
| m1–m7 | As stated against each item. |
| P1–P4 | Rewrite the abstract and introduction; move §2.4; mark cone points in or replace the schematic figures. |
