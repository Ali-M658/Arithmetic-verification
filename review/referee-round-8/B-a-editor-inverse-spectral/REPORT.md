<!-- Round 8 B-a editor report: returned text saved verbatim; the reviewer could not write files -->

I've decided to send the manuscript to review, and my own recommendation is major revision. I could not save the report to `REPORT.md` (writing it there was refused), so the full report follows. I found no mathematical error and no fatal issue. Every table entry I recomputed came out the same, within time-grid effects. The weaknesses are about significance and framing, not correctness. The checking scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/B-a-editor-inverse-spectral/scratch/code/` (`coeffs.py`, `thm62.py`, `test71.py`, `cor63.py`, `corrupt.py`, `robust.py`). One slip on my side: I briefly wrote a Crossref response to `/tmp/cr.json` instead of the scratch folder, and deleted it.

---

# Editor's report — Annals of Global Analysis and Geometry

**Manuscript:** "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (36 pp.)
**Disclosed related manuscripts:** "How much of a hyperbolic orbifold does heat hear?" (AGAG, 58 pp. + 16 pp. supplement; called "the companion" below), and "Triples with equal sum and equal reciprocal sum" (Integers).
**Handling editor's field:** inverse spectral problems and spectral rigidity on surfaces.

Page numbers refer to the submitted PDF. I read the rendered pages (pdftoppm, 110 dpi) before raising any typographical, sign or figure point. The placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) are treated as known.

## 1. Summary

Let Sig be the closed orientable hyperbolic 2-orbifolds whose singular points are cone points, and let C(A, ε, M) be those with area ≤ A, systole ≥ ε and cone orders ≤ M. The paper's results are:

- **Theorem 1.1 / 6.2 (pp. 2, 13–14).** There are explicit N(A, ε, M) and δ(A, ε, M) with this property: if the first N eigenvalues of O ∈ C(A, ε, M) are known to within δ, with none omitted and multiplicities counted, then σ(O) is the unique σ ∈ Sig(A, M) that minimises |Σ_{j<N} e^{−λ̃_j t∗} − G_σ(t∗)|. Here G_σ is the identity-plus-elliptic part of the Selberg trace formula. The proof has three parts:
  - a quantitative separation of the G_σ, using the integrality of the first differing heat invariant (Lemma 3.3) and enveloping remainders (Prop. 2.3);
  - a count of closed geodesics in terms of A, ε and M alone (Lemma 4.5), from a cone-point separation lemma and a packing argument (Lemmas 4.2–4.3, Thm 4.4);
  - a heat-trace tail bound (Prop. 5.2).
- **Corollary 6.3 (p. 14).** The same conclusion holds with the gap min |G_σ − G_σ′| supplied by computation instead of by Lemma 6.1. Evaluated numerically (not certified), this gives N ≈ 10²–10⁴ for the classes of the examples. The fully proved constants of Table 3 run from N ≈ 4×10⁴ to 3.8×10³⁰ and δ ≈ 10⁻⁹ to 10⁻²⁷⁸.
- **Theorem 1.2 / 7.1 (pp. 3, 17).** An a-posteriori test with criteria (C1) and (C2). It is run on ten computed spectra: O(2,8,8), O(3,3,12) and eight members of a (0;3,3,3,3) family. The errors are estimates, not enclosures, and the lists are assumed complete. The test singles out the true signature with N = 18 to 847.
- **Theorem 1.3, Props 8.2–8.3, Cor. 8.5 (pp. 4, 24–26).** The family O(2,3,m) has area < π/3, a uniform systole bound ℓ_{2,3} = 0.56206… (proved with Jørgensen's inequality), and λ_j ≤ ¼ + π²(j+1)²/h_m². So the order bound M cannot be dropped, and any valid rule needs N ≳ log M / log log M at fixed accuracy.
- **Section 8.2.** A collar/pinching proposition (Prop. 8.6) and an open problem on whether the systole bound is needed (Problem 1).

## 2. Significance and scope

**Scope.** The paper is within AGAG's scope. It concerns inverse spectral geometry of 2-orbifolds through the Selberg trace formula, and AGAG has published the directly relevant orbifold work (Stanhope 2005; Rossetti–Schueth–Weilandt 2008), both cited.

**Significance.** It is real but modest, and the framing promises more than the paper delivers.

- **The qualitative statement is soft.** That finitely many eigenvalues determine the signature within C(A, ε, M) follows in a few lines from Mumford–Bers compactness plus Dryden–Strohmaier / Doyle–Rossetti, as the authors show on p. 3. The signature is determined by the heat invariants, which are local data. This is much weaker than the stated model, Buser–Courtois (full isospectrality from finitely many eigenvalues).
- **The contribution is effectivity, and the proved constants are not informative.** N up to 3.8×10³⁰ and δ down to 8.7×10⁻²⁷⁸ (Table 3) say nothing about the true N; the paper says so itself (p. 15). The informative numbers (10²–10⁴) are not proved (Corollary 6.3, "computed, not certified").
- **What is new is limited:**
  - the explicit diameter bound and closed-geodesic count for cone orbifolds in terms of (A, ε, M) (Thm 4.4, Lemma 4.5): elementary, but useful and, as far as I know, not in the literature in this form;
  - the uniform systole bound for O(2,3,m) with an explicit constant (Prop. 8.2) and the resulting lower bound for N in terms of M (Cor. 8.5);
  - a carefully documented numerical consistency check.
- **Elliptic degeneration is not new.** Its spectral side (eigenvalues accumulating above ¼) is due to Garbin–Jorgenson and earlier work, all cited.

**What is good, plainly:**

- The mathematics I checked is correct, and the proofs are complete down to elementary hyperbolic geometry.
- The paper separates proved from computed statements more carefully than most submissions.
- Every table entry I recomputed is reproduced.
- The paper reports an experiment against its own method: one missing or duplicated eigenvalue makes (C1) choose a wrong signature in 19 of 24 cases (p. 18). That candour is welcome.
- The code and data statement is exemplary.

For AGAG readers this is a competent, honest paper whose main theorem is a computability statement. Whether it reaches the journal's bar depends on M1–M4. In particular, a certified small N for real classes would make the effective statement a contribution rather than a formality.

## 3. Correctness, and what I recomputed

**Proofs checked line by line; all correct:**

- Lemma 2.2(i)–(ii), both bounds.
- Lemma 3.3, and its extremal example (0;4,4,4), (0;3,4,6) with d₂ = −1/12.
- Theorem 3.2(i)–(ii), including the parity argument and the Vandermonde step.
- Lemmas 4.1–4.3, Theorem 4.4 (including the closed form), Lemma 4.5, Lemma 5.1, Prop. 5.2.
- Lemma 6.1 and Theorem 6.2. I checked on the rendered p. 14 that the inequality reads e^{−y}y^p ≤ (γ∗/16ϖ)(ε²/4)^p; the text layer of the PDF garbles it. The error budget Θ∗/8 + Θ∗/8 + Θ∗/(8e) < 3Θ∗/8 holds.
- Prop. 8.2 (systole via folding and Jørgensen): ℓ_{2,3} = 0.5620668…, as printed.
- Prop. 8.3 and identity (3) for w = sinh and w = cosh.
- Cor. 8.5 and Remark 8.4, including the finiteness for A < π/3.
- Prop. 8.6: the λ₁ bound sinh a/((a²+2) sinh a − 2a cosh a) is exact for the stated test function.

**Numerical checks:**

- **Proposition 2.3 (enveloping remainders).**
  - I computed φ_k(m) from the defining sum, then b_l(m), α_k and a_l.
  - The closed form of Lemma A.2 agrees (difference 0 at 40 digits).
  - b₀ = (m²−1)/(12m) and α₀..₃ = 1, −1/3, 1/15, −4/315 are confirmed.
  - The leading-coefficient ratio for a_l tends to 1.
  - Against 40-digit quadrature of E_m(t) and I(t) (m = 3, 8; t = 0.01, 0.1; K = 0..3), every remainder has the stated sign and lies within the stated bound.
- **Table 2.** Reproduced to all printed digits. The closed form A/π·max(4M, M²)·max(4/ε, 10M/3) is a valid upper bound in every cell.
- **Table 3.** Every entry reproduced: C∗, t₁, t₃, Θ∗, Λ, N, δ and the binding constraint.
  - For example, (π/2, 1.8626, 8) gives N = 3.4×10⁸, δ = 3.07×10⁻²¹; (10π, 1, 12) gives N = 3.75×10³⁰, δ = 8.65×10⁻²⁷⁸.
  - The minimum defining t₁ is attained at k = k∗ in every row, as Remark 6.4(a) says.
  - The factor of about 5 per halving of ε is reproduced (4.95, 5.13, 5.01, 4.90, 4.81).
  - t₃ starts to bind between ε = 0.45 and 0.43, so "ε ≤ 0.42" is true but is not the threshold.
- **Table 4 and other constants.**
  - C∗ values reproduced: 4.0×10⁵ and 9.5×10⁹ at A = 4π/3, and 3.5×10⁹ at A = π/2, M = 12.
  - Systole closed forms match ℓ rounded down: 2 arccosh(1+cos π/4) = 2.2567679 and 2 arccosh(½+cos π/12) = 1.8626041.
  - diam P = arccosh(cot² π/8) = 2.44845, matching.
  - 4b at ϑ = 0 equals 2.633915, matching.
  - The p. 25 value 2 arccosh((1+2cos(2π/7))/2) = 0.9839866 is confirmed.
- **Corollary 6.3 (computed gap).** I wrote an independent trapezoid evaluation of G_σ and an independent enumeration of Sig(A, M) (27, 48, 8 and 281 signatures). Results:
  - (π/2, M = 8) and (π/2, M = 12): N = 244 and 283, exactly as printed;
  - (4π/3, M = 3): 143 and 2601, against printed 139 and 2605;
  - (4π/3, M = 12): 7591, against printed 7415.

  The differences come from my coarser time grid. That I found 2601 < 2605 shows the reported values are grid-dependent optima.
- **Table 6, triangle rows (from the 40 eigenvalues of Table 5).** I implemented Theorem 7.1 independently, with both the instance diameter count and C∗. All six counts and their window midpoints agree with Table 6:
  - (C1) with the diameter bound: 18 (t ≈ 0.0563) and 25 (t ≈ 0.0411);
  - (C2) with the diameter bound: 20 and 29;
  - (C1) with C∗: 24 (0.0430) and 36 (0.0295).
- **Robustness (p. 18 (v)).** Inflating the errors to max(ϵ_j, 10⁻³λ̃_j) leaves 18 and 25 unchanged. At 10⁻², the O(2,8,8) count becomes 21, as printed. The O(3,3,12) count (printed 43) needs more than the 40 eigenvalues in Table 5, and I find none up to 38, which is consistent.
- **Corruption experiment (p. 18 (iv)).** Deleting or duplicating λ̃₁, λ̃₂, λ̃₃, λ̃₅, λ̃₈ or λ̃₁₂ makes (C1) choose a wrong signature in exactly **19 of 24** cases, as stated. Examples:
  - in O(2,8,8), deleting λ̃₁ gives (0;2,2,2,4) at N = 9;
  - in O(3,3,12), duplicating λ̃₁₂ gives (0;2,8,8) at N = 26.

  In 18 of the 19 wrong cases in my run, the wrong answer fires at a smaller N than the true count.
- **References.** All DOI-bearing references resolve on Crossref to the cited title, journal, volume and pages. Uçar's thesis has a DataCite DOI and was not checked.

**Conclusion.** No mathematical error found; all statements are correct as stated, and all numbers reproduce.

## 4. FATAL issues

None. I looked specifically for the following, and none is present:

- a wrong sign or exponent in Theorem 6.2;
- a gap in the separation argument;
- a mismatch in the elliptic normalisation of the trace formula;
- a failure of the geodesic count;
- numbers that do not reproduce.

## 5. MAJOR issues

**M1. The headline effective numbers are unproved, and the proved ones carry no information (abstract pp. 1–2; p. 3; Cor. 6.3 p. 14; Table 3 p. 15).**

- The abstract and introduction lead with "N of order 10² to 10⁴". That comes from Cor. 6.3, with the gap evaluated by floating-point quadrature and not certified.
- The proved numbers (Table 3) are N ≈ 4×10⁴ to 3.8×10³⁰ with δ ≈ 10⁻⁹ to 10⁻²⁷⁸.
- Certification is cheap. It needs a rigorous lower bound for the gap over a finite list of signatures at one rational t: a few hundred one-dimensional integrals of functions analytic in a strip, routine in interval quadrature. My float evaluation took under a minute.
- *Resolution:* certify the gap for the quoted classes and state the proved N and δ as a proposition. Otherwise, remove "10²–10⁴" from the abstract and introduction. Report the time used, not "the best time of a grid".

**M2. Overlap with the companion, and whether this should be a separate paper (Table 1 p. 6; §§2–3; Appendix A pp. 30–32; §7.1).**

- Eight companion results are restated and reproved here. Lemma 2.2 repeats the companion's Lemmas 2.4–2.5 with nearly the same proof text.
- The spectra, the description of the computations, and the code deposit are shared.
- The two unpublished manuscripts depend on each other:
  - the companion's Remark 2.6, Prop. 4.2 and Remark B.4 use this paper's Lemma 4.5 and the certified systole of §7.1;
  - this paper uses the companion throughout §§2–3.
- All of this is disclosed, and no main proof is circular.
- The new material here is Section 4, Prop. 5.2 (elementary), the assembly in Section 6, the test of Section 7, and Section 8. The companion's Lemma B.3 already recovers heat invariants from finitely many heat-trace values with a proved error under the same a-priori bounds; moving from there to eigenvalues is the tail bound of Prop. 5.2.
- *Resolution:*
  - a cover-letter justification for two papers rather than one;
  - shrink Appendix A to precise statements with pointers to the companion, keeping only what is needed to check Lemmas 3.3 and 6.1;
  - extend Table 1 to the reverse dependencies;
  - at least one common referee for both manuscripts.

**M3. Physical framing: what finite spectral data can and cannot detect (pp. 1–2, 4; §7 (iv) p. 18; §8).**

- The drum and experiment language suggests a protocol for measured data, but the hypotheses are not spectral and the accuracy is not physical.
- **None of A, ε or M can be read off finitely many eigenvalues.**
  - Theorem 1.3 proves this for M.
  - Problem 1 leaves ε open.
  - The paper is silent on A. It should say whether an area bound can be inferred from finite spectral data, as known or open.
- **The required accuracy is absolute and far below any measurement**: δ ≤ 10⁻⁹ even in the mildest proved case.
- **"None omitted, multiplicities counted" is the decisive hypothesis, and the method fails silently without it.**
  - I reproduced the 19 wrong conclusions out of 24, almost all at smaller N than the true count.
  - Per the companion, the O_ϑ family has a double λ₁ at ϑ = 0, exactly the kind of eigenvalue a measurement would merge.
  - The scan protocol on p. 18 has no proof.
- *Resolution:*
  - recast the paper as a computability statement and separate the spectral inputs from the geometric ones;
  - give a version robust to omissions. The statistic Σ e^{−λ̃t} does not depend on the order of the eigenvalues, so the hypothesis can be stated for multisets, and an omitted λ costs exactly e^{−λt}. Omissions above some level Λ₀ would then be tolerated, and omissions below it detected, because no signature passes;
  - label the scan protocol as heuristic, verified on 24 corrupted lists.

**M4. Section 7 contains no theorem about the computed orbifolds, although one is within reach (pp. 17–23).**

- The errors are differences of two discretisations, not enclosures. Completeness rests on a trace comparison whose Weyl-law tail is an estimate, not a bound.
- The counts are unchanged at 10⁻³ relative error. So a rigorous instance needs only about 20–40 eigenvalue enclosures at about 10⁻³ relative accuracy, with certified indices.
- The tools are standard: conforming upper bounds on the exact domain, Liu–Oishi or Carstensen–Gedicke lower bounds (both cited on p. 18), and inertia counts for completeness. With the certified systole and a certified G_σ (M1), O(2,8,8) with N = 18 (λ̃₁₈ ≈ 136) would become a proved instance of Theorem 7.1.
- *Resolution:* supply one certified instance, or explicitly demote §7 to an illustration.

**M5. The dependence on M and k∗ is far from sharp, and Remark 6.4 suggests a theorem is available (pp. 13, 15–17, 26).**

- The proved N grows at least exponentially in M, through lcm(1, …, M), δ₁ = 1/(2L_M) and |b_K(M)|. The lower bound of Cor. 8.5 is only log M / log log M.
- Remark 6.4(a) observes that in every class enumerated, no two signatures first differ beyond k = 3. Theorem 6.2 instead uses k∗ = min(⌊A/π⌋+4, M), which reaches 12 in Table 3, and this accounts for most of the 10³⁰.
- *Resolution:* either prove a sharper separation in a regime that covers the examples, or state in the introduction that the constants of Theorem 6.2 say nothing about the size of the least N. Recasting Theorem 6.2 in terms of the exact finite quantities of Remark 6.4(a) would help either way.

## 6. MINOR issues

- **m1 (pp. 3, 17).** "A stronger criterion, (C2)" is ambiguous. (C2) is a stronger hypothesis that implies (C1), not a stronger conclusion.
- **m2 (pp. 2, 13, 17, 21, 23).** Two indexing conventions for N: Theorem 6.2 uses N eigenvalues; Theorem 7.1 and Table 6 use N+1. Table 6 puts both in adjacent columns, and Fig. 1's "N = 21" sits beside Table 6's 20. Use one convention throughout.
- **m3 (p. 16, Fig. 1).** The figure uses a 61-point time grid that differs from §7.1's, so its N does not match Table 6. It has no legend, and the y-label covers only some of the curves.
- **m4 (p. 24, Fig. 2).** No in-figure legend. The caption ratio "56 to 2.7×10¹¹" is correct (4.3×10⁴/767 and 7.44×10¹²/28).
- **m5 (pp. 26–27).** The statement λ_j(O(2,3,m)) → ¼ "grants" Garbin–Jorgenson's condition (b). Either verify it or label the statement conditional everywhere, including the Fig. 3 caption.
- **m6 (p. 15).** "ε ≤ 0.42": t₃ already binds at 0.43, and the threshold lies between 0.43 and 0.45.
- **m7 (p. 14).** The Cor. 6.3 values are grid optima; a slightly different grid gives 2601 instead of 2605. Report the time used.
- **m8 (pp. 23–24).** Jørgensen's inequality for non-elementary discrete subgroups of PSL(2,ℝ) is classical. Citing [42] after noting that ⟨A, B⟩ is non-elementary is enough; the reproof adds nothing.
- **m9 (p. 20).** "A margin of at least 5×10⁻⁸" is the minimum over the ten examples, not a property of rounding down at the sixth decimal (for O(3,3,12), 1.862604055 → 1.862604). Say so.
- **m10 (p. 18 (iv), p. 20).** "Rejects all 24 lists" and "no window miss found" are empirical observations. Label them as such where they appear.
- **m11 (ref. [32]).** The disclosed Integers note carries an "INTEGERS 26 (2026) #A1" header, but it is cited here as a preprint. Make the status consistent across the three manuscripts.
- **m12 (p. 3).** The bi-Lipschitz continuity argument, with energy factor [K⁻², K²], uses that the dimension is two. Say so.
- **m13 (p. 4).** "The analogue of their conjecture" overstates the parallel. Use the "loose sense" qualification of p. 28 at first mention.
- **m14 (p. 16).** State the enumeration of Remark 6.4(a) as an observation, with its range and script. Since the companion shows that later first differences occur at larger area, say where it must fail.

## 7. Presentation

- **P1. Notation clashes.** Rename:
  - ε (systole) against ϵ_j (eigenvalue errors), which meet in the same formulas in Theorem 7.1;
  - δ (accuracy) against δ_k (separations);
  - Λ (Theorem 6.2) against Λ_N (Prop. 8.3);
  - t₁, t₂, t₃, which are critical times here but sample times in the companion's Lemma B.3.
- **P2. Dense sentences.** Several sentences carry nested parenthetical qualifications (p. 3, p. 5, p. 14, p. 18). Several proofs compress multiple steps into one sentence (Lemma 2.2(ii), Lemma 4.1(H3), Prop. 8.2). Display the key inequalities.
- **P3. The abstract reads as a list of caveats.** State the theorem, the role of each hypothesis, the necessity of M, and the status of the numerics, each once.
- **P4. Typesetting.**
  - The MSC line has stray spaces before commas (p. 2).
  - File names in the data statement lose their underscores ("make tables.py", "theorem e.py", "computed gap.py", p. 29).
  - The two-column Table 5 is dense.
- **P5. Figures.** Figures 1 and 2 need legends. Figure 3 is clear and well chosen.
- **P6. Table 1** is a good device. Extend it to the reverse dependencies.

## 8. Overlap and consistency with the disclosed manuscripts

**Companion (AGAG).**

- *Results:* §§2–3 restate the companion's results, and Appendix A reproves them; Lemma 2.2 is nearly verbatim (M2). This is declared in Table 1 and on p. 5.
- *Data:* the spectra are the same computations, also declared.
- *Mutual citation:* each unpublished manuscript uses the other's results, but neither main theorem depends on the other.

**Numbers that are consistent across both papers and the supplement:**

- λ₁ = 3.838887 and 3.499847; Dirichlet λ₁ = 73.663812 and 72.365158;
- 2002 and 2001 eigenvalues below 1.6×10⁴;
- the error budgets 1.5×10⁻¹¹ and 2.2×10⁻¹¹, and the error-estimate definitions;
- d₃ = 25/12;
- c₂ = 67/48, which equals the Integers note's (S + R − 2)/12 with S = 18, R = ¾.

**Claims to reconcile:**

- The supplement says the triangle spectra take "each eigenvalue … from one window". This paper reports a two-window recomputation (p. 19).
- The supplement says "no eigenvalue below about 1.6×10⁴ is missing", as if proved. This paper rightly says the same evidence cannot see a missing eigenvalue paired with a nearby spurious one, and that completeness is not proved (p. 20). The companion should adopt this paper's wording.
- The two papers use different completeness ranges for the family: in the supplement, 5451–5572 eigenvalues below the least sector maximum; here, 4357–4451 below 0.8 times it. One sentence should explain why.

**Integers note.** No shared results. It supplies only the motivating coincidence (S, R) = (18, ¾), stated consistently.

## 9. Editorial decision and recommendation

- **Decision: send to review.** The paper is in scope, sound as far as I could check, fully reproducible, and honest about its numerics. Its weaknesses concern significance and framing, which are for referees to weigh, not grounds for a desk rejection.
- **Referees.** One in inverse spectral geometry and trace formulas, and one in validated eigenvalue numerics. At least one should be shared with the companion.
- **My recommendation: major revision.**
  - Confidence in the correctness assessment: high (proofs checked, all tables reproduced).
  - Confidence in the recommendation: moderate.
  - If the revision certifies the gap (M1) and gives one proved instance of Theorem 7.1 (M4), I would expect to recommend acceptance. If only the framing (M3) and overlap (M2) are addressed, the significance question rests with the referees.

## 10. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Certify the Cor. 6.3 gap in interval arithmetic; state proved N and δ, or remove "10²–10⁴" from the abstract and introduction; report the time used. |
| M2 | Cover-letter justification for two papers; Appendix A reduced to statements plus pointers; Table 1 extended to reverse dependencies; a shared referee. |
| M3 | Recast as a computability statement; say which inputs are spectral and whether an area bound can be inferred from finite data; a multiset, omission-robust version of Theorems 6.2 and 7.1; label the scan protocol heuristic. |
| M4 | A certified instance (eigenvalue enclosures with index plus certified G_σ) for O(2,8,8), or explicitly demote §7 to an illustration. |
| M5 | A sharper separation in a stated regime, or an explicit statement that the constants carry no information; recast with the exact finite quantities. |
| m1–m14 | Local edits as listed. |
| P1–P6 | Rename clashing symbols; display key inequalities; restructure the abstract; fix MSC, file names and figure legends. |
| Overlap | Bring the companion supplement's window and completeness wording in line with this paper; make the Integers note's citation status consistent. |
