<!-- Referee B-e: returned text saved verbatim; the reviewer could not write files -->

Writing to REPORT.md was refused, so the full report follows as this message. I found no mathematical error, and I reproduced every constant in Tables 2 and 3 independently. My recommendation is **major revision** (about 70% confidence). The main reasons not to accept are significance, overlap with the companion paper [30], and two gaps in attribution.

# Referee report: rigour, citations and figures

**Manuscript:** "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (34 pp., submitted to *Annals of Global Analysis and Geometry*)
**Role:** rigour, citations and figures referee, and Springer Nature copy-edit.
**Treated as known:** the placeholders for author contributions, the AI-use statement, the Zenodo DOI and the preprint identifiers of [30] and [31].

Page numbers below are those of the PDF. I checked every typographical, sign and figure point against page images rendered at 110 and 200 dpi.

## 1. Summary

The paper works in the class C(A, ε, M) of closed orientable hyperbolic 2-orbifolds with area at most A, systole at least ε and cone orders at most M. It proves that the first N eigenvalues, each known to within δ, determine the signature, and it gives N and δ explicitly (Theorems 1.1 and 6.2).

The ingredients are:
- the Selberg trace formula applied to the heat kernel (Theorem 2.1, Lemma A.1);
- enveloping remainders for the cone and area terms (Proposition 2.3);
- an integrality bound at the first heat invariant where two signatures differ (Lemma 3.3), using Theorem 3.2 from the companion paper [30];
- a count of closed geodesics in terms of A, ε and M only (Lemmas 4.2–4.5);
- tail bounds on the eigenvalue sum (Section 5).

Section 7 gives an a-posteriori test (Theorem 7.1) and runs it on ten computed spectra. Section 8 shows the order bound cannot be dropped: O(2,3,m) has a systole bound uniform in m, proved through Jørgensen's inequality (Proposition 8.2), and arbitrarily many eigenvalues below any level above 1/4 (Proposition 8.3, Remark 8.4). It also asks whether the systole bound is needed (Problem 1).

## 2. Significance

**What is good:**
- The paper is honest about what it proves, and every proof I read is complete and correct.
- The constants are traceable, and I reproduced all of them.
- Proved statements are kept carefully apart from numerical estimates.
- Lemma 4.5 (counting closed geodesics without a diameter bound) is clean.
- The uniform systole bound for O(2,3,m) via Jørgensen is a neat argument.

**Reasons against acceptance in the present form:**
1. **The qualitative statement is not new in substance.** Compactness (Mumford–Bers) together with spectral determination of the signature (Dryden–Strohmaier, Doyle–Rossetti) gives it, as the authors themselves show on pp. 2–3.
2. **The effective constants cannot be used.** Table 3 has N up to 3.8 × 10^30 and δ down to 8.7 × 10^-278.
3. **Section 7 is not a theorem about any orbifold.** The systoles are not certified, the errors are estimates rather than enclosures, and completeness of the eigenvalue lists is not proved. The authors say so themselves: the ten examples are "consistency checks … not proved determinations".
4. **Theorem 1.3 adds little to Garbin–Jorgenson's elliptic-degeneration results.** It adds only a systole bound uniform in m and a pigeonhole step (M3).
5. **There is substantial overlap with the companion manuscript [30].** Sections 2–3 and Appendix A restate and reprove its results (M1).

For AGAG this is borderline: correct and carefully done, with modest mathematical novelty.

## 3. Correctness, and what I recomputed or verified

All computations were done independently with mpmath at 60 digits.

**Heat-coefficient constants:**
- α_k: the Bernoulli-polynomial formula (p. 8) and the moment formula (p. 29) give identical values. Both reproduce 1, −1/3, 1/15, −4/315; α_4 = 1/315.
- The closed form for Φ_m in Lemma A.2 matches the Taylor coefficients of the defining sum (m = 7, k = 2).
- b_0(m) = (m²−1)/(12m) and p_l(1) = 0.
- The leading coefficient a_l matches the computed leading coefficient of p_l for l ≤ 3. The computation in Lemma A.3 is correct.

**Proofs read line by line and found correct:**
- Lemma 2.2(i)–(ii): B_C, its monotonicity in ℓ, and the global bound (both maxima, and the constant e^{17t/4−1/2}).
- Proposition 2.3(a)–(b): all signs and moduli.
- Lemma 3.1, Theorem 3.2(i)–(ii) (parity/Newton step and Vandermonde step), Lemma 3.3, Lemma 4.1.
- Lemma 4.2 (defect ≥ π/(abc) and the final 2/(π²M²)), Lemma 4.3, Theorem 4.4 with its closed form, Lemma 4.5.
- Lemma 5.1 (the minimal-area cases), Proposition 5.2, Lemma 6.1.
- Theorem 6.2. y_0 follows exactly from e^{-y}y^p ≤ (γ_*/16ϖ)(ε²/4)^p, the 3/8 versus 5/8 margin holds, and so does Λt_* ≥ 1.
- Theorem 7.1, including that (C2) implies (C1).
- Lemma 8.1. I checked the recursion by hand and the commutator trace identity numerically: tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r and bc = −sin²(φ/2)cosh² r.
- Proposition 8.2: side lengths via (H3), and ℓ_{2,3} = 2 arsinh(½(37/12)^{-1/2}) = 0.56206 (using 2s_∞ = log 3).
- Identity (3), Propositions 8.3 and 8.5 (∫_0^a ρ² cosh ρ dρ = (a²+2)sinh a − 2a cosh a), Lemmas A.1, A.2 and A.4.

**Tables and numerical claims recomputed:**
- **Table 2 (p. 12):** all 12 entries agree, e.g. 56.60, 150.94, 639.97, 1132.03.
- **Table 3 (p. 14):** every entry of all 8 rows agrees after rounding: C_*, t_1, t_3, Θ_*, Λ, N, δ and the binding constraint. The 10π, M = 12 row gives N = 3.75e30 and δ = 8.65e−278.
- **"About 4 × 10^18" (p. 15):** without the cap k_* ≤ M, the 10π, M = 3 row gives N = 4.19e18.
- **Growth as ε → 0 (p. 15):** the factor per halving of ε is 5.2, 5.1, 5.0, 4.9, 4.8, and C_* ~ ε^-4, as stated.
- **Last column of Table 6:** 6.82e9, 4.32e4 and 7.44e12, consistent with Table 3, the abstract and Section 7.2.
- **Ratio claims:** the Fig. 2 caption's "56 to 2.7 × 10^11" is 43188/767 and 7.436e12/28. "At most 1.7" is 767/461 = 1.66. The other factors on p. 21 and every count quoted in the text match Table 6.
- **Systoles:** 2 arccosh(1 + cos π/4) = 2.2567679 and 2 arccosh(½ + cos π/12) = 1.8626041. The family systoles equal 4b (ϑ = 0, 0.4 and 2.8 checked). The O(2,3,7) value is 0.983986.
- **Section 7.1 arithmetic:** 1.66 × 10^4, 9.8 × 10^3 and ≈ 2 × 10^8 budgets are right. The ϵ_j in Table 5 are 12–16 × the 10^-14 λ_j floor. λ̃_N ≈ 2540 and (λ̃_N − ϵ_N)t of about 8–11 are right. The diameters in Table 4 are half of 2 diam P.
- **Worked examples:** d_2((0;4,4,4),(0;3,4,6)) = −1/12, so the bound is attained. In Fig. 1, d_3 = 25/12, and the black curve starts at 2.1e−3.

**Citations fetched and checked at statement level:**
- [1] (eq. (1), Thm 1.1, Thm 3.2, Prop. 3.3)
- [2, Thm A]
- [5, Thm 1]
- [11, Main Thms 1–2]
- [12]
- [14, Thm 5.3, Cor. 5.5, Thm 5.7, Ex. 5.8]
- [15, Rem. 2.7, (2.8), Thm 6.5]
- [21, §7]
- [27, Thm 4.8]
- [28, Thms 3.40, 4.20, Cor. 4.21]
- [44]

All 46 DOIs resolve, and the metadata match apart from the points in P11. I could not obtain [3], [4], [6], [16], [18], [19], [41], or the published [21] and [29].

## 4. FATAL

None.

## 5. MAJOR

**M1. Overlap with [30] and dependence on an unidentified preprint (pp. 5–6, 28–30, Table 1).**
- Seven results of [30] are restated, and Appendix A reproves them "with the arguments of [30]".
- [30] is submitted at the same time and has only a placeholder identifier.
- The computations in Section 7 are the same as in [30].
- The convergence evidence for the error estimates ϵ_j is only "in the supplement of [30]" (p. 19).

This is a redundant-publication question for the editors and a verifiability problem for referees.

*Resolution:*
- Supply [30] and its identifier, and declare the overlap in the cover letter.
- Shorten or justify Appendix A.
- Put the h/p convergence evidence in this paper or its deposit.

**M2. Uçar's results are not credited (pp. 2–4, 8).**
[28, Cor. 4.21(iv)] proves that, at constant curvature κ ≠ 0 without mirrors, κ and the spectrum determine the multiset of cone orders. His proof uses the same triangular structure of the heat invariants that this paper uses. The paper cites [28] only for the closed form (Thm 4.20) and "the mechanism" (Thm 3.40), and credits spectral determination of the signature to [1] and [5] only.

*Resolution:*
- Cite [28, Cor. 4.21] wherever heat-invariant determination of the signature is mentioned.
- Delimit what Theorem 3.2 and Lemma 3.3 add, which is quantitative.

**M3. Elliptic degeneration (pp. 4–5, 25).**
(a) [14, Thm 5.3] concerns the weighted counting functions for 0 ≤ w ≤ 3/2. The unweighted growth c_0(T) log Q is [14, Thm 5.7], which is the right citation for "grows without bound".
(b) [14, Ex. 5.8] treats Hecke triangle families explicitly. It attributes the accumulation of spectral data to Selberg, citing [16, p. 579]. The paper's citation of [16] has no locator.
(c) On p. 25 the authors say that convergence λ_j → 1/4 "would follow if [14, Cor. 5.5] applied … which we have not checked". Whether O(2,3,m) is an elliptically degenerating family in the sense of [14] is a definitional check, and [14, Ex. 5.8] suggests that it is.
(d) The novelty of Theorem 1.3 is then the uniform systole bound (Proposition 8.2) plus pigeonhole. It should be presented as such.

*Resolution:*
- Fix the locators to [14, Thm 5.7] and [16, p. 579], and cite [14, Ex. 5.8].
- Check whether O(2,3,m) satisfies the hypotheses of [14], and either state the consequence or explain why it fails.
- Restate the novelty claim for Theorem 1.3.

**M4. Statements resting on unproved continuity (pp. 2–3, 26).**
The compactness argument and the intermediate-value argument after Proposition 8.5 both assert that λ_j is continuous on moduli space. The justification given is "bi-Lipschitz orbifold maps … with constants near 1", without proof or reference. The compactness argument also takes "a positive minimum 2δ", which hits a boundary case: data within δ of both spectra only gives |λ_j(O) − λ_j(O′)| ≤ 2δ.

*Resolution:*
- Prove or cite continuity of λ_j. For the quadrilaterals Q_{k,b} an explicit bi-Lipschitz map is elementary; give it.
- Use 3δ or strict inequalities.

## 6. MINOR

- **m1 (p. 12, end of proof of Lemma 4.5).** "≤ K e^x" uses an undefined K; it should be C_*. Also mention that cosh y − 1 ≤ e^y/2 is where the factor ½ in C_* comes from.
- **m2 (pp. 6, 8).** Theorem 3.2 cites "[30, Cor. 3.5, Thm 3.8]", but Table 1 says "Thm 3.8(i)". Part (ii) then has no locator in [30].
- **m3 (p. 12).** "Theorem 4.4 is used for the finiteness statement of Section 1": no proof in the paper uses Theorem 4.4. Theorem 6.2 uses C_*, and Theorem 7.1 uses instance diameters bounded directly. State its actual role: Table 2, the remark on [12], and the contrast with Proposition 8.2.
- **m4 (p. 17, item (v)).** "The counts are insensitive to them" is too strong, since the criterion fails throughout the complete range at r = 10^-3. Write "insensitive to relative perturbations up to 10^-4".
- **m5 (p. 16, Theorem 7.1).** "in particular none of λ_0..λ_N is omitted" reads as a consequence. It is a hypothesis; say so.
- **m6 (p. 7).** "the same normalisation" as [15, (2.8)]: [15] sums over primitive γ and n ≥ 1 with ℓ_γ/(sinh(nℓ_γ/2)√(16πt)). The two forms agree, but say that the hyperbolic term is rewritten.
- **m7 (p. 4).** [27] has an erratum (Michigan Math. J. 66 (2017), doi:10.1307/mmj/1488510034). Cite it, and state that it does not affect the case used here.
- **m8 (pp. 9, 23).** Beardon [35] is cited for the hyperboloid model and for T being a fundamental domain of the reflection group. Give section locators, or cite something more suitable (e.g. Ratcliffe, Ch. 3).
- **m9. Locators I could not verify.** Please check these against the published versions:
  - [3, Cor. 3];
  - [6, (1.1)] and [6, pp. 523–524] (the first pages of the article);
  - [18, p. 264] and [19, p. 67] (both first pages);
  - [21, §7] (arXiv numbering);
  - [25, Lemma 6.6.4].
- **m10 (p. 25).** List the 21 values of m used for Fig. 3.
- **m11 (p. 17).** For Sylvester's law of inertia, say it applies to the generalised eigenproblem Ku = λMu. The letter M there collides with the order bound.
- **m12 (p. 5).** "Lemma 3.3 … a direct consequence of [30, Lemmas 2.10 and 3.3]" sits uneasily with "nothing else here is taken from it".

## 7. Presentation, figures and Springer Nature conventions

- **P1 (Fig. 1, p. 15).** The figure content follows the rule (axis titles and tick labels only), but the y-axis title |G_{σ0}(t) − G_σ(t)| describes only the grey curves, not the dashed and dotted bounds.
  - The caption does not identify the line styles.
  - The shading is for N = 21 only. The N = 100 window, roughly 0.025–0.055, is visibly wider and is not shaded.
  - Suggested caption, two sentences: "Gaps between the signature term of O(2,8,8) and its five competitors (solid), with the closed-geodesic bound (dashed) and the tail-and-perturbation terms for N = 21 and 100 (dotted). Shading marks the times at which, for N = 21, half the nearest gap exceeds their sum."
- **P2 (Fig. 2, p. 22).** The marker code (open/filled, diamond/square/circle, colours) is explained only in the text, and "a reference count" in the caption is opaque.
  - The plotted test counts use the instance diameter (Table 6, "(C1), Δ"). The headline class-level counts of the abstract (24–842) are not plotted. Plot them, or say in the caption which count is shown.
  - Mention the horizontal displacement of the markers in the caption.
- **P3 (Fig. 3, p. 26).** The text calls the bounds in panel (a) "thin dashed", but they render as dotted (checked at 200 dpi), the same style as the j² levels in panel (b).
  - Panel (a) has no x-axis title.
  - The caption's "fall towards it" should stay observational, as p. 25 says.
- **P4 (pp. 12, 18).** The Table 2 and Table 4 captions carry data and method. Move these into the tables or the text.
- **P5 (p. 1).** Affiliations lack the postal detail Springer Nature requires (organisation, street, city, postcode, state, country). The ORCID block is not part of the sn-jnl front matter.
- **P6 (p. 2).** The MSC line has spaces before the commas: "58J50 , 35P15 , 30F35 , 57R18".
- **P7. Notation collisions.**
  - A: area and the matrix in Lemma 8.1.
  - M: order bound and mass matrix.
  - p: k_* − 3/2, the polynomials p_l, the FE order and points.
  - L: number of invariants, the lcms, enumeration length, translation length.
  - ℓ: systole, ℓ(γ), and the interval length in Proposition 8.3.
  - ε versus ϵ_j: hard to distinguish in print.
  - H: 𝓗(s), H_L(σ), ℍ², H¹.
  - P: polygon, power sums, union of tiles.
  - R: reciprocal sum and radius.
  - K: truncation index, stiffness matrix, and the stray K of m1.
  - q: potential in (3) and a point.
  - N: eigenvalue count, x_1..x_N in Lemma A.4, Neumann in Table 5.
  - δ and δ_k.
- **P8.** Use "a posteriori" and "a priori" consistently.
- **P9 (p. 27).** Add "Consent to participate", "Consent for publication" and "Materials availability" items (Not applicable).
- **P10.** Theorem 1.2 refers to criterion (C2) before it is defined.
- **P11. Reference list style.**
  - [16] "Vol. 2" against [33] "Vol. I".
  - A full stop precedes the DOI in [16], [28], [33] and [40] only.
  - [25] lacks its DOI, 10.1007/978-0-8176-4992-0.
  - [38] needs a version and year.
  - Check whether [5] and [8] have been published.
  - For [22], write "Art. ID 71281".
- **P12 (p. 4).** Split the long "Relation to prior work" paragraph into sub-paragraphs; this will make the M2 and M3 fixes easier to check.

## 8. Recommendation

**Major revision**, confidence about 70%. Correctness is not in doubt: I reproduced all of Tables 2 and 3 and every derived claim, and the proofs I read are complete. Rejection would rest on significance (M1, Section 2), which I leave to the editor.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Identify [30], declare the overlap, reduce or justify Appendix A, include the convergence evidence. |
| M2 | Cite [28, Cor. 4.21] and delimit what Theorem 3.2 and Lemma 3.3 add. |
| M3 | Correct to [14, Thm 5.7] and [16, p. 579], cite [14, Ex. 5.8], check the hypotheses of [14] for O(2,3,m), restate the novelty of Theorem 1.3. |
| M4 | Prove or cite continuity of λ_j (give the explicit map for Q_{k,b}), fix the 2δ boundary case. |
| m1–m12 | Local fixes as listed; check the m9 locators against the published versions. |
| P1–P3 | Revise axis titles, line styles and captions within the two-sentence limit. |
| P4–P12 | Copy-edit to Springer Nature conventions. |

Scripts and fetched sources are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/B-e-springer-copyeditor/scratch/code/ and /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/B-e-springer-copyeditor/scratch/src/.
