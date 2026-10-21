<!-- Round 10, B-a (editor), returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

Writing REPORT.md was refused (subagents may not write report files), so the full report is below.

# Handling editor's report: AGAG submission "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Editor's field: spectral geometry, generalist. I read all 41 pages and checked the rendered pages before reporting anything typographical or about a figure (pp. 2, 4, 9, 15–19, 27, 31, 35 at 110–200 dpi). I compared the paper with the three disclosed manuscripts, recomputed every table I could from the paper's own formulas and data, and ran a literature search on arXiv, Semantic Scholar and Crossref. As instructed, the placeholders (author contributions, AI-use statement, Zenodo DOIs, preprint identifiers) are treated as known. I did not open the GitHub code deposit and did not rerun the finite-element computations. My scripts are in .../B-a-editor-spectral-geometry-generalist/scratch/code/: recompute.py and test71b.py.

---

## 1. Summary

Let O be a closed orientable hyperbolic 2-orbifold with cone points, and let C(A, ε, M) be the class with area ≤ A, systole ≥ ε and cone orders ≤ M.

- **Theorem 1.1 / 6.2 (pp. 2, 15).** Explicit N and δ exist such that the first N eigenvalues of any O in C(A, ε, M), each known to within δ (with none omitted), determine its signature. The rule is to minimise |Σ_{j<N} e^{−λ̃_j t*} − G_σ(t*)| over the finite set Sig(A, M). The proof combines:
  - the Selberg trace formula;
  - signed (enveloping) remainders for the identity and cone terms;
  - an integrality lemma for the first heat invariant at which two signatures differ (Lemma 3.3);
  - a count of closed geodesics in terms of A, ε and M only, by cone-point separation and packing (Lemmas 4.2–4.5);
  - a Weyl-type tail bound (Proposition 5.2).

  The closed-form constants are astronomical (Table 5: up to N ≈ 4×10^30 and δ ≈ 10^−277).
- **Corollary 6.4 / Proposition 6.5 (pp. 16–17).** This is a computer-assisted proof. For six specific classes the gap between signatures is certified directly in Arb ball arithmetic at a moderate time. This gives N = 139 to 7416 (and 3.9×10^5 for one class with ε = 0.1), with δ between 5.9×10^−4 and 2.5×10^−6.
- **Theorem 1.2 / Proposition 8.2–Corollary 8.5 (pp. 4, 28–30).** The order bound cannot be dropped. The triangle orbifolds O(2,3,m) have area < π/3, systole ≥ ℓ_{2,3} = 0.56206 uniformly in m (by Jørgensen's inequality), and λ_j ≤ 1/4 + π²(j+1)²/h_m². Pigeonhole then shows that a rule valid up to order M at a fixed accuracy needs N ≳ log M / log log M.
- **Theorem 7.1 and Section 7.** An a-posteriori test, run on computed spectra of O(2,8,8), O(3,3,12) and eight members of (0;3,3,3,3). The paper labels these consistency checks, not determinations.
- **Section 8.2.** Whether the systole bound is needed is left open (Problem 1).

## 2. Significance and novelty

**What is good.**
- The question is natural: what finite, approximate spectral data can detect.
- The paper is mathematically careful. Every step of the main argument is proved, and the constants are genuinely explicit.
- It is unusually honest about status. Proved, computer-assisted and illustrated results are separated almost everywhere (pp. 3–4, 20–24).
- The explicit cone-point separation (Lemma 4.2), the diameter-free geodesic count (Lemma 4.5), the integrality lemma (Lemma 3.3) and the uniform systole bound for O(2,3,m) (Proposition 8.2) are clean and reusable.
- The certified instances (Proposition 6.5) are a real, checkable theorem, and I reproduced them (Section 3).

**Novelty search.** On arXiv, Semantic Scholar and Crossref I found no prior effective or finite-data result on the signature of hyperbolic orbifolds. The closest work is:
- Buser–Courtois (cited);
- elliptic degeneration (Garbin–Jorgenson, Judge, Hejhal; cited);
- the trace-formula and consistency ("bootstrap") programmes that bound hyperbolic surface and orbifold spectra from finite data. These are *not* cited: Kravchuk–Mazáč–Pal, arXiv:2111.12716 (which treats 2-orbifolds explicitly); Bonifacio, arXiv:2107.09674; Fortier Bourque–Petri, arXiv:2302.02540.

**Reservations about significance.** These are substantial; see M1–M3.
- The main theorem makes compactness effective by bookkeeping standard tools. The closed-form constants are of no use, as the authors say themselves (p. 3).
- The practical content is a computer-assisted statement for six classes.
- Theorem 1.2 is close to classical. Its eigenvalue bound is an instance of Cheng's comparison theorem, and its pigeonhole consequence is elementary.
- The same pigeonhole argument also settles negatively a question the paper leaves open (whether the area bound is needed; see M3). This suggests the "necessity" part of the paper has not been fully thought through.

Overall I judge the paper a solid, correct, specialised contribution of moderate significance. It is within AGAG's scope (spectral geometry of orbifolds; AGAG has published Stanhope and Rossetti–Schueth–Weilandt on orbifold spectra).

## 3. Correctness, and what I recomputed

**Proofs checked line by line, with no error found:**
- Theorem 6.2. This includes the derivation of y₀: the condition B*(t) ≤ Θ(t)/8 reduces to e^{−y}y^p ≤ (γ*/16ϖ)(ε²/4)^p, and the rendered y₀ on p. 15 is correct. The tail and perturbation budgets 1/8 + 1/8 + 1/(8e) < 1/2 also check.
- Lemma 6.1, Lemma 2.2(i)–(ii) (both bounds on Hyp), Lemma 3.3, Theorem 3.2(ii) (the Vandermonde argument), Lemma 4.2 (the defect estimate), Lemmas 4.3 and 4.5, the closed form of Theorem 4.4, Lemma 5.1 and Proposition 5.2.
- Theorem 7.1, Lemma 8.1 (the Jørgensen recursion), Proposition 8.2 (the folding argument and the trace identity), Propositions 8.3 and 8.7 (Rayleigh quotients; the λ₁ bound sinh a/((a²+2)sinh a − 2a cosh a) re-derived), Corollary 8.5, and Lemma A.2.

**Recomputations.** I wrote independent code (mpmath 1.3.0 at 40 digits plus exact sympy rationals for b_l, a_l, α_k). It is not ball arithmetic.

1. **Table 2 (p. 13).** All twelve entries of D(A, ε, M) reproduce, e.g. 56.6, 1125, 6.37×10^5, and 640 for ε = 0.1.
2. **Table 5 (p. 18).** All eight rows (k*, C*, t₁, t₃, Θ*, Λ, N, δ and the binding constraint) reproduce to the stated rounding. Examples: N = 3.40×10^8, 6.82×10^9 (printed as 6.9×10^9, rounded up), 4.32×10^4, 7.44×10^12, 2.28×10^6, 1.08×10^6 and 3.75×10^30; δ = 8.65×10^−278 in the last row. Section 4's ranges for C* (4×10^5 to 7×10^10) follow.
3. **Tables 3–4 (p. 17).** I enumerated Sig(A, M) and got the same cardinalities: 27, 48, 8, 8, 281, 12. I evaluated every G_σ(t) by quadrature.
   - The least gaps agree with Table 4 to all digits printed, e.g. 0.01588232, 0.006527298, 0.1520293 and 0.001373851.
   - The minimising pairs I found ((0;2,3,8)/(0;2,4,5), (0;2^5)/(0;2,3^3), (0;5²,10)/(0;4,8²)) are the tied pairs the text announces on p. 16.
   - B*(t), Θ/8 and Λt agree. The tightest margin is 0.017933 against 0.019004, as stated.
   - N = 244, 283, 139, 2605, 7416 and 387182, and δ, agree exactly.
4. **Table 8, triangle rows (p. 26), from the eigenvalues printed in Table 7.** I implemented E_N(t) and criteria (C1)/(C2) as written, on the paper's time and s-grids, with ε_j floored at 5×10^−7 to cover the 6-decimal rounding. Every value matches the paper:

   | | (C1), Δ | (C2), Δ | (C1), C* | (C1), Sig(π/2,12) |
   |---|---|---|---|---|
   | O(2,8,8) | 18 | 20 | 24 | 24 |
   | O(3,3,12) | 25 | 29 | 36 | 36 |

   - The (C1), Δ windows are centred at 0.0565 and 0.0414, as printed.
   - |S| = 6 and |Sig(π/2,12)| = 48.
   - No wrong signature is singled out at any N ≤ 39.
5. **Spot checks:**
   - ℓ_{2,3} = 0.56206.
   - The systole of O(2,3,7) is 0.983986.
   - The closed forms 2 arccosh(1+cos π/4) = 2.2568 and 2 arccosh(1/2 + cos π/12) = 1.8626.
   - The diameters arccosh(cot² π/8) = 2.4485 and 2.1588.
   - H = 6.8×10^−3 against Hyp = 2.8×10^−10 at t = 0.0562 (p. 25).
   - The Fig. 2 ratio range 56 to 2.7×10^11.
   - Remark 6.6(a): the minimum defining t₁ is at k = k* in every row.
   - The ε-scaling on p. 18 (A = 4π/3): t₃ binds below ε = 0.444, and the per-halving factors run 5.239 → 4.673.
   - The 12π example in Remark 6.6: P₁ = 57 and P₃ = 2433 for both padded multisets, while P₅ differs (117777 vs 137217).

**What I could not check.** The finite-element spectra themselves, the interval-arithmetic systole enumeration, and the code deposit. The paper says all eigenvalue errors are estimates, not enclosures; I agree with that characterisation.

**Honesty of the numerical claims.** This is largely exemplary, and almost every statement carries its status. Proved: Theorems 1.1, 1.2, 6.2 and 7.1, and the propositions of Section 8. Computer-assisted: Proposition 6.5 and the certified systole bounds. Illustrated: Table 8, Figs. 1–3, and the completeness and error estimates. There are two exceptions, M2 and M4.

## 4. FATAL issues

None. I found no mathematical error in the parts I checked, and the certified instances reproduce.

## 5. MAJOR issues

**M1. The main theorem's contribution beyond bookkeeping is not argued (pp. 2–3, 5, 15–18).**
- The non-effective statement follows from compactness (p. 3).
- The closed-form N, δ "matter only to show that explicit constants exist" (p. 3) and are unusable (Table 5).
- Corollary 6.4, run at a moderate time, already yields everything practical.

Mathematically, the content of Theorem 6.2 is that a positive, computable gap exists at some explicit time. That gap is guaranteed by Lemma 6.1, and the rest is standard estimates. A referee will ask why an AGAG reader should value the closed forms over the simpler statement "N and δ are computable by a terminating certified procedure".

*Resolution.*
- State as the main theorem an algorithmic or computable version: for every (A, ε, M) the certified procedure of Corollary 6.4 terminates, with termination guaranteed by Lemma 6.1. Keep Theorem 6.2 as the existence bound.
- Explain what in Sections 4–6 is new as mathematics: the diameter-free geodesic count, the integrality gap and the explicit separation.
- Position the work against the trace-formula bootstrap and linear-programming literature (m6).

**M2. The comparison of the lower and upper bounds in M compares different regimes (abstract p. 2; p. 3; Corollary 8.5 and Remark 8.6, p. 30).**
- The lower bound N ≳ log M/log log M holds at **fixed** δ.
- The polynomial upper bound of Theorem 6.2 comes with δ shrinking like M^{−26} (at A = π/2).
- At δ = M^{−c}, Corollary 8.5's inequality (⌊Λ_N/δ⌋+1)^{N−1} ≥ M − 6 already holds at N = 2, so the lower bound is vacuous in the theorem's regime.

The heat-trace mechanism cannot work at fixed δ in any case. With |λ̃_j − λ_j| ≤ δ for all j < N, the perturbation is about δ·t·Z(t) ≈ δ·A/4π, which does not shrink with t, while every gap is at most about 1/24. So "between the lower bound log M/log log M ... and this polynomial we do not know the true growth" (p. 30) suggests a gap that the paper has not set up. The abstract repeats the juxtaposition.

*Resolution.* Do one of the following:
- state Corollary 8.5 jointly in (M, δ) and compare the two bounds at the same δ; or
- say explicitly that the lower bound is vacuous when δ decays polynomially, and that existence of any N(M) at fixed δ is open.

In either case, remove the juxtaposition from the abstract.

**M3. The area bound is also necessary, and the paper calls this open (p. 4, "we know of no bound for the area in terms of finitely many eigenvalues"; p. 5, "Whether the bound on the area can be dropped ... we do not know").** It follows from the same pigeonhole argument as Theorem 1.2, with Cheng's eigenvalue comparison (S.-Y. Cheng, Math. Z. 143 (1975) 289–297) in place of Proposition 8.3:
- For a closed surface with curvature −1 and diameter d, Cheng gives λ_k ≤ λ_1^D(B_{H²}(d/2k)).
- Since area ≤ 2π(cosh d − 1), the diameter tends to ∞ with the area.
- So for fixed N the first N eigenvalues of closed surfaces of growing genus stay in a bounded box.
- For every ε > 0 there are infinitely many genera with a surface of systole ≥ ε (Buser–Sarnak).
- Pigeonhole then gives, for every ε, M, N and δ, two members of C(∞, ε, M) of different signatures whose first N eigenvalues agree to within δ.

Cheng's bound also re-derives the qualitative eigenvalue bound of Proposition 8.3, provided its orbifold version is justified. So the new element of Theorem 1.2 is essentially the uniform systole bound of Proposition 8.2.

*Resolution.*
- Add this statement (or explain why it fails), and cite Cheng.
- Revise "what finite spectral data can detect" (p. 4) and the abstract accordingly: both the order bound and the area bound are necessary, and only the systole question is open.
- Recalibrate the novelty claimed for Theorem 1.2 (pp. 4–6).

**M4. Section 7 never determines a signature, and its completeness evidence depends on the signature (pp. 20–27).**
- Completeness of the triangle spectra below about 1.56×10^4 rests on agreement of the computed trace with I + E *of the true signature* at t = 0.0015 (p. 23). That comparison with roughly 2000 eigenvalues is itself a much stronger signature test than Table 8, and it presupposes completeness ("which is what the comparison probes").
- The Table 8 counts (18–847) measure the crudeness of H. The paper says so (H exceeds Hyp by 2.4×10^7, p. 25), and N_obs = 3 for both triangle orbifolds (p. 27).
- So the abstract's sentence "An a-posteriori version of the argument passes on ten computed spectra" advertises a statement with little mathematical content.

*Resolution.* Do one of the following:
- (preferred) Give one rigorous end-to-end instance, for example O(2,8,8) in the class of Proposition 6.5: index-wise enclosures of the first 283 eigenvalues to 4.27×10^−5 (Liu–Oishi or Carstensen–Gedicke type lower bounds plus conforming upper bounds, as the paper itself outlines on p. 22). This would turn the paper's title into a theorem about an actual orbifold.
- Otherwise:
  - make the completeness protocol signature-free, i.e. accept only if exactly one σ ∈ S matches at t = 0.0015, and say so;
  - use Remark 6.6(c) (summing the enumerated geodesics), which is cheap and would make the counts reflect the problem rather than the bound H;
  - remove the Section 7 result from the abstract, or reduce it to one clause.

**M5. Refereeing needs the certificate and the companion material (pp. 16–17, 33–34; Appendix A).**
- Proposition 6.5 is a computer-assisted proof whose code lives only in an external repository; the Zenodo record is a placeholder.
- Sections 2–3 and Appendix A reprove results of the simultaneously submitted companion.

*Resolution (editorial).*
- Require an archived, versioned snapshot of `certified_gap.py` and its environment at resubmission, accessible to referees. The paper's description on p. 16 is good enough to re-implement, as I did.
- Send the paper to a referee who also sees the companion, or at least instruct the referee to check Appendix A in full rather than relying on the companion.

## 6. MINOR issues

- **m1 (p. 16, Corollary 6.4).** The hypothesis "0 < Θ ≤ 8" is correct (it makes Hyp ≤ Θ/8 ≤ 1 enter Z♯) but reads like a typo for the 1/8 of Theorem 6.2. Say why 8.
- **m2 (pp. 22–23).** "λ_c" in Table 6 (the completeness cut, 16000) and "Λ_c" in the text (the largest computed value, ≈ 2.17×10^4) are different quantities with near-identical symbols. Rename one.
- **m3 (pp. 3, 20, 26, 27).** Off-by-one conventions:
  - Theorem 6.2's N counts eigenvalues, while Theorem 7.1's N uses N+1 of them.
  - Fig. 2 plots both as "number of eigenvalues".
  - The "further factor of about 6 to 12" (p. 26) compares across the two conventions.

  Unify, for instance by restating Theorem 7.1 with N eigenvalues.
- **m4.** Overloaded notation:
  - ε (systole), ϵ_j (errors) and ϵ (Lemma A.1);
  - p (k* − 3/2, the FEM order, a point, the polygon P);
  - ℓ (systole, ℓ(γ), the interval length in Proposition 8.3);
  - A (area bound and the matrix in Lemma 8.1);
  - Λ, Λ_N, Λ_c, Λ_o;
  - δ_k and δ.
- **m5 (pp. 2–3).** "δ ... to about 2×10^−6": the smallest δ in Table 3 is 2.48×10^−6, so say 2.5×10^−6.
- **m6 (pp. 5–6, 20).** Missing citations:
  - Kravchuk–Mazáč–Pal, arXiv:2111.12716 (rigorous spectral bounds for 2-orbifolds from finite consistency data);
  - Bonifacio, arXiv:2107.09674;
  - Fortier Bourque–Petri, arXiv:2302.02540 (trace-formula linear programming with test functions supported below the systole, which is exactly the route of Remark 6.7);
  - Cheng 1975 (see M3);
  - the 2017 erratum to Dryden–Gordon–Greenwald–Webb, Michigan Math. J. 66 (2017) 221–222, alongside [30]. The companion cites it; this paper does not.
- **m7 (pp. 24–25, Table 7).** An external benchmark is available and unused. Bolza/C₈ = O(2,8,8), so λ₁(O(2,8,8)) must equal Bolza's λ₁ = 3.83888725884 (Strohmaier–Uski). The companion's supplement (§S4(iii)) makes this comparison; cite it here.
- **m8.** The completeness statements differ between the two manuscripts.
  - Here (pp. 23–24): single omissions are detectable only below 1.563×10^4 and 1.576×10^4, and 48 and 29 eigenvalues rest on the double-window agreement alone.
  - Companion supplement §S4: "2002 and 2001 lie below 1.6×10^4, the range in which the trace test ... would detect a single missing or spurious eigenvalue".

  Harmonise them. This paper's version is the accurate one.
- **m9 (ref. [32]).** The disclosed note is typeset with an INTEGERS 26 (2026) header but is cited as a preprint. State its actual status.
- **m10 (p. 24).** ϵ_j = |λ_j(0.05,10) − λ_j(0.07,12)|. Say which discretisation is believed more accurate and why the difference bounds the production error even heuristically. The meshes are not nested.
- **m11 (p. 26, Table 8).** "Geometric middle of the window" presupposes a contiguous window. State that the windows are intervals (they are, in my recomputation of the triangle rows).
- **m12 (p. 4, Theorem 1.2).** State the range j ≥ 1 and give ℓ_{2,3} = 0.56206 in the statement; 0.5620 is a rounding of it.
- **m13 (p. 30, Remark 8.6).** "The computed exponents per doubling approach 9 and 26": give the range of M used.
- **m14 (ref. [16]).** Crossref dates L'Enseignement 64 to 2019 (volume year 2018). Check the year.

## 7. Presentation

- **P1 (p. 2).** Theorem 1.1 is not self-contained ("the numbers N and δ of Theorem 6.2"). Give their shape and order of magnitude in the statement, or state the computable version (M1).
- **P2.** The prose is very dense, with long sentences carrying many nested qualifications. Examples: the prior-work paragraph (pp. 5–6), item (iv) on p. 21, and the completeness paragraph (pp. 23–24). Split sentences and use lists.
- **P3.** Collect in one place (a short table) what is proved, what is computer-assisted (Proposition 6.5, the systole bounds) and what is illustrated (Section 7, Figs. 1–3). The paper repeats "not proved" and "an observation" at many separate points.
- **P4. Figures.**
  - Fig. 1 (p. 19) has no legend; its curves are identified only in the text.
  - Fig. 2's marker scheme (p. 27) is explained only in the body. Its y-axis label hides the off-by-one (m3).
  - Fig. 3(b) (p. 31): the dotted levels at j² are described only in the text.

  The rendered figures are otherwise legible and consistent with the text: the shading at t ≈ 0.050–0.056, d₃t = 25t/12 at t = 10^−3, and λ₁ = 44.89 → 0.473.
- **P5.** The title states an unconditional result. Given Theorem 1.2 and M3, add "under a priori bounds" or similar.
- **P6.** The abstract has many hedged clauses. Lead with the theorem, then the certified instances, then the necessity result.

I found no typographical, sign or figure errors in the rendered pages I inspected. The apparent anomalies in a text extraction ("Θ ≤ 8", "A = 3" on p. 18) are correct, or are fraction rendering (4π/3), when viewed as images.

## 8. Overlap with the disclosed manuscripts

- **Heat-invariants companion (65 pp. plus supplement).** Sections 2–3 and Appendix A here (pp. 7–10, 34–37) restate, with proofs, the companion's:
  - Theorem 2.3 and Lemma B.1;
  - Lemmas 2.4–2.5, 2.7, 2.9, 2.11 and 3.6;
  - Corollary 3.8 and Theorem 3.11(i);
  - Proposition B.2.

  This is disclosed precisely in Table 1 and on p. 6, and it reciprocates the companion's own description (its p. 6). Both papers share the computed spectra, Table 7's data (also in the supplement) and the code deposit. The companion's Remarks 2.6 and B.6 use this paper's Lemma 4.5 and its certified systoles; no main proof depends on the other paper. The genuinely distinct material here is Sections 4–8 and Lemma 3.3. I regard the overlap as acceptable and properly disclosed. Proposition 6.5's certified gaps, the diameter-free count and the elliptic-degeneration results are not in the companion.
- **Consistency.** The shared numbers agree: λ₁ = 3.838887 and 3.499847; the 1.4×10^−14 double-window agreement; 2 diam P = 4.897; the family ranges 4357–4451. "M heat invariants" here versus "M+1" in the companion's abstract is consistent (signatures with orders ≤ M versus all of Sig). The single discrepancy is m8.
- **Equal-sum note.** It shares only the motivation, (2,8,8)/(3,3,12) having equal sum and reciprocal sum. There is no textual or result overlap.

## 9. Editorial decision and recommendation

- **Editorial decision:** **send to review.** The paper is in scope, technically sound as far as I could check, and fully reproducible at the level of its tables, so there are no grounds for desk rejection. It should go to one referee in spectral geometry and trace formulas, who also sees the companion (M5), and preferably to a second with computer-assisted-proof experience for Proposition 6.5.
- **My recommendation:** **major revision.**
  - Confidence that the checked mathematics and tables are correct: high.
  - Confidence in the level of the recommendation: moderate (about 0.6). A strict referee could reasonably recommend rejection on significance grounds (M1, M3) unless the revision either sharpens the main theorem's value or supplies one rigorous end-to-end determination (M4).

## 10. What resolves each issue (checklist)

| Issue | Resolution |
|---|---|
| M1 | Lead with a computable/terminating-procedure theorem; state what is new as mathematics; position against the trace-formula bootstrap and linear-programming literature. |
| M2 | Compare the lower and upper bounds at the same δ, or state that Corollary 8.5 is vacuous for δ = M^{−c}; remove the abstract juxtaposition; note that fixed-δ existence is open. |
| M3 | Add the area-necessity statement via Cheng plus pigeonhole (or refute it); update pp. 4–5 and the abstract; recalibrate Theorem 1.2's novelty. |
| M4 | Ideally one rigorous enclosed instance; otherwise a signature-free completeness protocol, the Remark 6.6(c) improvement, and Section 7 removed from or minimised in the abstract. |
| M5 | Archived certificate code accessible to referees; a referee who has the companion, or a full check of Appendix A. |
| m1–m14 | As itemised in Section 6. |
| P1–P6 | As itemised in Section 7. |
