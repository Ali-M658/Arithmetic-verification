<!-- Round 9 B-a editor report: returned text saved verbatim; the reviewer could not write files -->

I could not save the report to REPORT.md (the write was refused for subagents), so the full report is below. In short: I recommend sending it to review, and my own recommendation is major revision, with medium confidence. I found no fatal error. Every number I recomputed matches the manuscript (scripts check1–check5.py in .../B-a-editor-effective-geometric-analysis/scratch/). Five issues need fixing (M1–M5), the biggest being that the examples prove nothing although a rigorous determination looks reachable.

# Handling editor's report: AGAG submission

**Title:** Finitely many eigenvalues determine the signature of a hyperbolic orbifold (38 pp.)
**Disclosed related submissions:** "How much of a hyperbolic orbifold does heat hear?" (AGAG, 61 pp. plus a 17 pp. supplement); "Triples with equal sum and equal reciprocal sum" (Integers, 24 pp.)
**Placeholders treated as known:** author contributions, AI-use statement, Zenodo DOI, preprint identifiers.

## 1. Summary

The paper takes a closed orientable hyperbolic 2-orbifold O with area at most A, systole at least ε and cone orders at most M. It proves that the first N eigenvalues, each known to within δ and with none omitted, determine the signature (g; m_1,…,m_n). The numbers N and δ are given by closed formulas (Theorem 1.1 = Theorem 6.2). The mechanism has six parts:

- **Trace formula.** The Selberg trace formula is extended to the heat function (Thm 2.1, Lemma A.1).
- **Enveloping remainders.** The identity and elliptic terms have enveloping Taylor remainders (Prop. 2.3).
- **Integrality.** At the first heat invariant where two signatures differ, the difference is an integer multiple of an explicit rational (Lemma 3.3). With orders at most M, this happens at index k ≤ min(⌊A/π⌋+4, M) (Thm 3.2).
- **Closed geodesics.** They are counted from A, ε and M alone, by separating cone points and packing balls (Lemmas 4.2–4.5).
- **Spectral tail.** It is controlled from the heat trace (Prop. 5.2).
- **Decision rule.** The signature is the one minimising |Σ_{j<N} e^{−λ̃_j t*} − G_σ(t*)|.

The closed-form constants are hopeless: up to 4×10^30 eigenvalues and accuracies down to 10^−277 (Table 4). The authors say so plainly. The practical version is different. Corollary 6.3 replaces the heat-invariant gap with the actual gap over the finite set Sig(A, M), certified in Arb ball arithmetic at one moderate time. This gives Prop. 6.4: for six explicit classes, N = 139 to 387 182 eigenvalues with δ ≈ 10^−4 to 10^−6 suffice (Table 3).

Section 8 has two parts:

- **Orders (Thm 1.2, Prop. 8.2–8.3, Cor. 8.5).** The order bound cannot be dropped. O(2,3,m) has area below π/3 and a systole bounded below uniformly in m (via Jørgensen's inequality), and it acquires arbitrarily many eigenvalues near 1/4. As a result, N must grow at least like log M / log log M.
- **Systole.** Whether a systole bound is needed is left open (Problem 1). It is discussed through a pinching family (Prop. 8.6).

Section 7 gives an a-posteriori test (Thm 7.1) and runs it on finite-element spectra of O(2,8,8), O(3,3,12) and eight orbifolds of signature (0;3,3,3,3). The eigenvalue errors are estimated, not enclosed, and the lists are assumed complete. The authors call these consistency checks, not determinations.

**What is good.** The mathematics is careful, and as far as I could check it is correct. Every displayed number I recomputed agrees with the paper (Section 3 below). The paper is unusually honest about what is proved, what is certified, what is only estimated, and what finite data cannot detect. The certified-gap route (Cor. 6.3 / Prop. 6.4) is a clean way to turn a compactness statement into usable numbers. Theorem 1.2 is a tidy, explicit obstruction.

## 2. Scope and significance

**Scope.** Inverse spectral geometry of orbifolds is squarely within AGAG's remit. The journal published Stanhope [12] and Rossetti–Schueth–Weilandt [14], both cited. Computer-assisted certification is acceptable for this journal if the certified statement is reviewable.

**Significance.** It is moderate. The hard qualitative input, that the spectrum, and indeed finitely many heat invariants, determines the signature, is already in the literature: Dryden–Strohmaier, Doyle–Rossetti, Uçar, and the companion paper [31]. Given that input, the effective statement is assembled from standard estimates:

- Taylor remainders of the identity and elliptic terms;
- a packing count of closed geodesics;
- a Weyl-type tail bound from the heat trace.

Each is done carefully, but none is deep. The companion [31, Lemma B.4] already recovers heat invariants from finitely many values of the heat trace, with a proved error, under the same a-priori bounds. The present paper adds three things: the passage from heat-trace values to eigenvalues (the tail, §5), the diameter-free count (Lemma 4.5), and the integrality gap (Lemma 3.3). Lemma 3.3 is itself, as the authors note, "a direct consequence of [31, Lemmas 2.11 and 3.6]".

What effectivity buys in practice is limited:

- **Theorem 6.2 is useful only for showing that the constants exist.** Its constants are astronomically large.
- **The usable statements are instance computations.** Prop. 6.4 covers six classes, and Section 7 proves nothing.
- **The novelty of Theorem 1.2 is narrow.** Garbin–Jorgenson [15, Thm 5.7] already give eigenvalue accumulation under elliptic degeneration. What is new is a uniform systole bound and the pigeonhole lower bound, both short arguments.

A strict referee could reasonably judge the paper below AGAG's bar on significance. I do not think a desk rejection is warranted, for four reasons:

- the problem is natural;
- the work is correct;
- the certified-instance idea is genuinely useful;
- the M-dependence question (Cor. 8.5 against the upper bound) is a real open problem the paper identifies.

The authors must, however, sharpen what the reader learns beyond [31] plus standard estimates (see M1).

## 3. Correctness, and what I recomputed

I read every proof except the full details of Lemma 8.1 (Jørgensen's argument, which is classical). I found no mathematical error. I verified these steps line by line:

- Lemma 2.2(ii), including the logarithmic derivative and the e^{17t/4} bound.
- Lemma 3.3 (both parts) and Theorem 3.2 (the parity/Newton argument and the Vandermonde argument).
- Lemmas 4.1–4.3 and Theorem 4.4, including the closed form. arccosh(1+x) ≥ √(2x/(1+x)) gives d_0 ≥ min(ε/2, 0.6/M).
- Lemma 4.5.
- Lemma 5.1 (case analysis) and Prop. 5.2.
- Lemma 6.1 and the full proof of Theorem 6.2. The y_0 inequality, the requirements Λt* ≥ 1 and 1/Λ ≤ t*, and the 3Θ*/8 margin all check out.
- Theorem 7.1, including (C2) ⇒ (C1).
- Prop. 8.2: ℓ_{2,3} = 2 arsinh(½(37/12)^{−1/2}) = 0.56206, cosh d(v_2,v_3) = 2cos(π/m)/√3, and the cone-ball argument.
- Prop. 8.3 and the identity (3), where q = ½ − w′²/(4w²).
- Cor. 8.5.
- Prop. 8.6: the Rayleigh quotient sinh a/((a²+2) sinh a − 2a cosh a).
- The continuity argument on p. 3 (the factor K^{±4} is right in dimension 2).

I recomputed the following independently in Python/mpmath and SymPy. These are my own scripts, not the authors' deposit, which I did not run.

1. **Heat coefficients.** α_0..α_4 = 1, −1/3, 1/15, −4/315, 1/315. p_0..p_3 exactly; leading coefficients a_l = 1/12, 1/360, 1/2520, 1/10080 as stated; p_l(1) = 0. The φ_k against a direct Taylor expansion of Φ_5.
2. **Enveloping property (Prop. 2.3).** Checked numerically for E_3 and E_7 (K = 0..3) and for I (K = 0..2) at t = 0.01. The signs alternate and every modulus is below the stated bound.
3. **Examples.** The example of Remark 6.5: (0;2^4,7^7) and (0;4^6,8^4) have area 12π, equal padded P_1 and P_3 (57 and 2433), and different P_5. d_2 = −1/12 for (0;4,4,4) and (0;3,4,6). d_3 = 25/12 for (0;2,8,8) and (0;3,3,12).
4. **Table 4, all eight rows.** C*, t_1 (attained at k = k* in every row, as claimed), t_2, t_3, Θ*, Λ, N, δ and the binding constraint all agree within the stated rounding. Supporting claims also agree:
   - "C* between 4×10^5 and 7×10^10";
   - "πe^{3D}/A between 3×10^196 and 2×10^29325" (I get 10^196.53 and 10^29325.38);
   - "at A = 10π … N from about 4×10^18" (I get 4.19×10^18);
   - the factor per halving of ε, 5.2 falling to below 4.7;
   - Fig. 2's "56" (43 190 / 767).
5. **Table 2.** All twelve values of D agree.
6. **Table 3 (Prop. 6.4), all six rows.** I enumerated Sig(A, M) and got the same cardinalities 27, 48, 8, 8, 281, 12. I computed every G_σ(t) at the stated t by 30-digit quadrature (not ball arithmetic). The minimal gaps agree with Θ to every printed digit. They are 0.0158823, 0.0065273, 0.152029, 0.165511, 0.0013739, 0.166649, attained respectively by:
   - (0;3,3,8)/(0;3,4,5);
   - (0;2,4,10)/(0;2,5,7);
   - (0;2,2,2,2,3)/(0;3,3,3,3);
   - (0;2^5)/(0;2,3,3,3);
   - (0;5,5,10)/(0;4,8,8);
   - (0;2^5)/(0;2,3,3,3).

   B* ≤ Θ/8, t ≤ t_2 and Λt ≥ 1 hold in every row. N matches exactly in all six rows, and δ agrees to the last printed digit or within 1 in it. One margin is thin: in row 3, B* = 0.0179 against Θ/8 = 0.0190.
7. **Table 7, the eight triangle-orbifold entries.** I reran Theorem 7.1 from scratch on the eigenvalues and error estimates printed in Table 6. I used the instance diameter bounds 4.897 and 4.317 and C* = 3.545×10^9, with S equal to the 6 equal-area signatures or the 48 signatures of Sig(π/2, 12). I reproduce exactly (C1),Δ = 18 and 25, (C2),Δ = 20 and 29, (C1),C* = 24 and 36, and (C1),Sig = 24 and 36. The window midpoints also agree (0.0565/0.0556/0.0432 and 0.0412/0.0402/0.0295). No wrong signature was accepted at any (N, t) in my scan.
8. **Other numbers.** The closed-form systoles and the diameters 2 diam P of the triangle orbifolds check out. So do the hyperbolic term 2.8×10^−10 and the bound H = 6.8×10^−3 at t = 0.0562 (p. 24), and the "2×10^8 budgets" and λ < 1.66×10^4 thresholds (p. 22). The shared spectra agree with the companion's supplement.

What I could not check:

- the finite-element spectra themselves;
- the interval-arithmetic systole certification;
- the Arb code behind Prop. 6.4.

My recomputation supports the certified values, but it is not a check of the certification.

## 4. FATAL issues

None. I found no error that invalidates a stated theorem, proposition or table.

## 5. MAJOR issues

**M1. The contribution beyond [31] and standard estimates is not made clear (pp. 2–6, 16).** Section 6 combines three ingredients:

- separation of signatures from [31] (Lemma 3.3 is "a direct consequence of [31, Lemmas 2.11 and 3.6]");
- the recovery mechanism of [31, Lemma B.4], used with eigenvalues instead of trace values;
- a Weyl-type tail.

Theorem 6.2's numbers are, by the authors' own account, irrelevant in practice.

- *Resolves:* a precise statement, near Thm 1.1, of what is new and why it is not a routine corollary. This might be the diameter-free count, the comparison against all of Sig(A, M), or the certified-gap method. Say plainly that the closed-form theorem matters only to show that the constants exist, or strengthen the content (see M3: a two-sided M-growth picture).

**M2. The examples prove nothing, although rigour appears within reach (pp. 18–25, Tables 5–7, Fig. 2).** Section 7 establishes only that estimated spectra, assumed complete, are consistent with the trace formula of the known signature. The completeness evidence is partly circular: it uses the trace formula of the true signature (p. 22). The authors' own sensitivity test (p. 20, item (v)) shows the counts survive errors inflated to 10^−2 relative (N = 21 and 43). So a rigorous determination of O(2,8,8) or O(3,3,12) needs only:

- index-wise enclosures of roughly the first 20–45 eigenvalues of each Neumann/Dirichlet triangle problem, at about 10^−3 relative accuracy;
- validated G_σ (already available in Arb);
- outward rounding in E_N.

The authors themselves sketch the method (p. 20). The curved geodesic sides are a real but modest complication. A paper titled "Finitely many eigenvalues determine…" should contain at least one actual determination.

- *Resolves:* either (a) one rigorous instance, for example O(2,8,8) with the instance diameter bound, with completeness proved independently of the signature; or (b) a clear demotion of Section 7 to an illustration, with the abstract and introduction rebalanced. I strongly prefer (a).

**M3. The dependence on M is mis-described, and an easy improvement is missed (pp. 14, 17, 28).**

- **Where N's growth in M actually comes from.** P. 28 says Theorem 6.2 gives "an N that grows much faster with M, through L_M and |b_K(M)|". In fact N depends on L_M only logarithmically, through log(1/Θ*) and y_0. At fixed A, once M ≥ n*, k* = n* is fixed and t_1 ≍ a_{k*−2}/|b_{k*−1}(M)| ≍ M^{−(2k*−1)}. So N = O_{A,ε}(M^{2⌊A/π⌋+7} log M), polynomial in M. Table 4 is consistent: from M = 8 to 12 at A = π/2, N grows by about 20 ≈ 1.5^7 × log factor.
- **δ_1 can be improved.** In Lemma 3.3(i), L_{σσ′} is the lcm of at most 2n* orders, each at most M, so L_{σσ′} ≤ min(L_M, M^{2n*}). This makes δ polynomial in M at fixed A as well, not of size e^{−M}.
- *Resolves:* state the polynomial upper bound explicitly, set it against Cor. 8.5's log M / log log M, correct the p. 28 sentence, and optionally use min(L_M, M^{2n*}).

**M4. The framing of what finite spectral data can detect should use the paper's own stronger statement (pp. 1–4, 15–16).** The hypotheses of Thm 1.1 and Table 3 are a uniform absolute δ and no omission. These are physically unrealistic: at the top of the list, Table 3's δ amounts to relative accuracy of about 10^−7 to 10^−10. Yet the proof gives much more.

- **Weighted errors.** The parenthetical remark on p. 15 allows the j-th eigenvalue to be wrong by δe^{λ_j t*}. Since e^{Λt*/2} = 8Z♯(t*/2)/Θ*, eigenvalues in the upper half of the list need only crude accuracy.
- **Omissions.** Omissions or duplications above roughly Λ/2 change the sum by at most about Θ*/(8Z♯) each. So the rule tolerates a controlled number of them if the hypothesis is phrased for multisets rather than indices. This matches the p. 20 experiments, where only omissions among λ_1…λ_12 fooled the test.
- *Resolves:* put the weighted hypothesis into Thm 6.2 / Prop. 6.4. Report in Table 3 the accuracy needed as a function of λ. Add a multiset version tolerating K omissions above an explicit level. Rewrite the p. 4 paragraph quantitatively, and qualify or drop "measurement" in the abstract.

**M5. The computer-assisted proof of Prop. 6.4 is not reviewable from the paper (pp. 15–16).** The paper does not give, for each class:

- the minimising pair;
- the enclosure of the minimal gap;
- the enclosures of B*(t), Λt and N;
- the completeness argument for the enumeration of Sig(A, M) (cite n + 4g ≤ A/π + 4 there).

The row-3 margin (B* = 0.0179 against Θ/8 = 0.0190) is thin enough that the reader deserves to see it.

- *Resolves:* an appendix table of these enclosures (my non-rigorous values are in §3.6 above). Referees should run certified_gap.py.

## 6. MINOR issues

- **m1 (pp. 17, 20).** The two tables round C* differently. C*(π/2, ·, 12) = 3.545×10^9 is printed 3.5e9 in Table 4 and 3.6×10^9 in Table 5. C*(4π/3, ·, 3) = 4.010×10^5 is printed 4.0e5 and 4.1×10^5. Table 5 evidently rounds up; state the rounding direction.
- **m2 (p. 3).** "4×10^4 to 7×10^12": the values are 4.32×10^4 and 7.44×10^12, and elsewhere N is rounded up (7.5e12).
- **m3 (p. 3).** The claim that nearby orbifolds are related by K-bi-Lipschitz maps with K → 1 needs a reference or a proof sentence. Cite continuity of eigenvalues on moduli space.
- **m4 (refs).** Dai–Wei, "Finite part of spectrum and isospectrality", Contemp. Math. 173 (1994), is missing. Referees should check for later effective versions.
- **m5 (p. 18, Fig. 1).** The caption calls both tail curves "dotted"; one is dash-dotted, and neither is labelled N = 21 or N = 100.
- **m6 (p. 21).** The discretisations (0.05, 10) and (0.07, 12) are not nested, and neither is clearly the more accurate. Give errors against a finer reference for a few eigenvalues.
- **m7 (pp. 12–13).** Theorem 4.4 is "used in no proof of a main result". Downgrade it to a Proposition, or justify the label.
- **m8 (p. 28).** Say whether Judge's monotonicity [18] applies to the observed decrease in m; the conformal class changes with m.
- **m9 (p. 30).** Problem 1(b): say whether anything proved already excludes a negative answer with N fixed.
- **m10 (p. 16).** The unproved existence of K in the truncation paragraph is not used. Prove it or drop the paragraph.

## 7. Presentation

- **P1. Indexing convention.** "The test with N uses N + 1 eigenvalues" (Thm 7.1, Table 7) clashes with "N eigenvalues" in Theorem 6.2. The paper has to warn about this three times (pp. 3, 23, 24). Use one convention throughout.
- **P2. Notation clashes.**
  - ε (systole) and ϵ_j (errors) are nearly indistinguishable in print.
  - ℓ is the systole bound, a geodesic length, and an interval length in the proof of Prop. 8.3.
  - A is the area bound and also the hyperbolic matrix in Lemma 8.1.
  - δ is the accuracy, and δ_k are the separations.
- **P3. Prose density.** Long sentences carry several semicolon-separated claims (pp. 2–6, 16–17, 24). Key definitions are buried mid-sentence (Sig(A, M) on p. 2; S on p. 19). Display them.
- **P4. Caveats repeated.** The status caveats appear in the abstract and on pp. 3, 18, 20 (twice), 23 and 25. Consolidate them into one "Status of the computations" paragraph.
- **P5. Rendering.** I checked the rendered pages: pp. 8, 9, 14–15, 17, 18, 25 and 29 render correctly. I found no typographical, sign or figure error beyond m5.

## 8. Overlap with the disclosed manuscripts

- **Companion (heat invariants, AGAG).**
  - *What is shared.* Sections 2–3 restate results whose primary place is [31] (Table 1, p. 6), and Appendix A reproves them. Every cited result exists in [31] with the stated content. Thm 3.2(ii) agrees with [31, Thm 3.11(i)] ("M invariants within Sig_{≤M}"; [31] says M + 1 against all of Sig, which is consistent). The papers also share the computed spectra (identical values), the code deposit, and the proof of Lemma 2.2(i).
  - *Text overlap.* Measured as shared 10-word sequences, it is about 9%. Nearly all of it is front matter, references, declarations and the Lemma 2.2(i) proof.
  - *Cross-references.* Each paper uses the other's results only in remarks, and I found no circularity.
  - *Assessment.* The overlap is fully disclosed and handled honestly. The editorial concern is the marginal content of this paper over [31] (M1). Give referees both manuscripts.
- **Integers note.** The overlap is negligible (about 0.7%, all boilerplate), and nothing here depends on it.

## 9. Editorial decision and recommendation

- **Decision:** **send to review.** No desk rejection: the paper is in scope, correct as far as I can check, honest, and its numbers reproduce. Its significance is debatable and should be judged by specialists.
- **Suggested referees:**
  - one inverse-spectral/orbifold specialist, ideally also given the companion [31];
  - one validated-numerics specialist, asked to run the deposit's certified_gap.py and certify_systoles.py.
- **My own recommendation:** **major revision.** Confidence: **medium.** My confidence in correctness is high; my confidence in the significance judgement is medium. A referee who weighs significance more heavily could reasonably recommend rejection. The revision should at least address M1, M3 and M4 and settle M2 one way or the other.

## 10. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Explicit statement of the advance over [31, Lemma B.4] plus standard estimates. Say that the closed-form Theorem 6.2 matters only to show that the constants exist. Ideally add the two-sided M-growth result (M3). |
| M2 | One rigorous determination (index-wise enclosures of modest accuracy, completeness independent of the signature, validated G_σ, outward rounding), or demotion of Section 7 with the abstract and introduction rebalanced. |
| M3 | State N = O_{A,ε}(M^{2⌊A/π⌋+7} log M). Correct the p. 28 sentence about L_M. Optionally use L_{σσ′} ≤ min(L_M, M^{2n*}). |
| M4 | Weighted accuracy hypothesis in the theorem and Table 3; a multiset version tolerating omissions above an explicit level; rewritten framing paragraph and abstract wording. |
| M5 | Appendix table of certified enclosures per class; cite the enumeration bound; referees run the deposit. |
| m1–m10 | As stated item by item. |
| P1–P5 | Unify the N convention, remove the notation clashes, display key definitions, consolidate the caveats, label Fig. 1. |
