<!-- Referee B-d: returned text saved verbatim; the reviewer could not write files -->

I couldn't write the report to `REPORT.md` (the write was refused), so the full report is below. My recommendation is **major revision**. Every number I could recompute matches, and the framing of estimates against proved bounds is honest. Three claims are wrong as stated or not yet shown: the robustness claim (v), the comparison with Theorem 6.2, and the conclusion drawn in (iv) about completeness. All three can be fixed with cheap computations.

My recomputation scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/B-d-maass-form-computation/scratch/code/`.

---

# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (AGAG)

**Referee remit:** Section 7 (the a-posteriori test, Theorem 7.1), its numerical methods, error estimates and completeness checks, Tables 3–6 and Figures 1–3, and every statement the numerical conclusions depend on. The placeholders are treated as known.

## 1. Summary

The paper proves an effective result. In the class C(A, ε, M), the first N eigenvalues, each known to within δ, determine the signature, and N and δ are explicit (Theorem 6.2). The order bound cannot be dropped (Theorem 1.3). Section 7 turns the same mechanism into an a-posteriori test (Theorem 7.1): at one time t, the truncated heat trace is compared with each signature term G_σ(t), within an error budget E_N(t). That budget has three parts: a closed-geodesic bound, a spectral tail bound and an eigenvalue-perturbation term.

The test is run on finite-element spectra of ten orbifolds whose signature is known by construction: O(2,8,8), O(3,3,12) and eight members O_ϑ of signature (0;3,3,3,3). With the class-level geodesic count C*, criterion (C1) holds with N = 24 to 842; Theorem 6.2 would need 4×10⁴ to 7×10¹². The paper says plainly that the eigenvalue errors are estimates, that completeness is assumed and that the systole bounds are floating-point. It calls the results consistency checks, not determinations.

## 2. Significance

Theorem 7.1 is a short, correct consequence of the trace formula and Lemmas 2.2 and 5.1. Checking computed spectra against the heat trace is not new: Strohmaier–Uski [21] do it, and Booker–Strömbergsson–Venkatesh [22] certify Maass forms rigorously. What is new is using the check to tell signatures apart, and comparing it quantitatively with the a-priori constants. As written, Section 7 proves nothing about any orbifold. Its value is to show how pessimistic Theorem 6.2 is. M2 argues that a fully certified determination for the two triangle orbifolds is within easy reach, which would turn Section 7 into a result.

## 3. Correctness and what I recomputed

I used only the PDF and my own code (SciPy quadrature, mpmath at 40–50 digits), not the authors' deposit.

**Proofs checked line by line, no error found:**
- Lemma 2.2(ii), both bounds.
- The proof of Theorem 6.2: the y₀ argument, the tail bound, the perturbation bound and the 3/8 margin.
- Lemma 6.1.
- Theorem 7.1, including (C2) ⇒ (C1).
- The normalisation of the elliptic terms: numerically E_m(t) → b₀(m) and (E_m − b₀)/t → b₁(m) for m = 2, 8, 12.

**Recomputed and found to agree:**
1. **Table 3 (p. 14):** all 8 rows and every column (k*, C*, t₁, t₃, Θ*, Λ, N, δ, the binding constraint) match exactly. Also correct:
   - α₀–α₃ and a₀–a₃;
   - dropping k* ≤ M at A = 10π, M = 3 moves N from 4.19×10¹⁸ to 1.08×10⁶;
   - the "factor about 5 per halving of ε, decreasing towards 4" claim: I get 5.24, 5.13, …, 4.67, with C* growing by a factor approaching 16.
2. **Signature sets S:** sizes 6, 3 and 10, matching |S| in Table 6. The coefficient d₃ = 25/12 is right.
3. **Table 4 (p. 18):**
   - C*: 3.5×10⁹, 4.0×10⁵ and 9.5×10⁹, all correct.
   - Systoles: the closed forms 2.25676793 and 1.86260406, and 4b for the family. All are rounded down with margins of at least 5.5×10⁻⁸, so the stated "at least 5×10⁻⁸" holds.
   - 2 diam P from the vertex coordinates: agrees to the printed precision (but see m1).
4. **Table 6 (p. 21), triangle rows, rerun from the 40 eigenvalues in Table 5:**

   | | (C1), Δ | (C2), Δ | (C1), C* |
   |---|---|---|---|
   | O(2,8,8): mine | 18 (0.0564) | 20 (0.0556) | 24 (0.0430) |
   | O(2,8,8): paper | 18 (0.0565) | 20 (0.0556) | 24 (0.0432) |
   | O(3,3,12): mine | 25 (0.0412) | 29 (0.0402) | 36 (0.0296) |
   | O(3,3,12): paper | 25 (0.0412) | 29 (0.0402) | 36 (0.0295) |

   No wrong signature is ever singled out.
5. **Robustness claims (p. 17):**
   - One deleted or duplicated eigenvalue gives a wrong (C1) answer in **19 of 24** cases with the diameter count, as stated. With C* it is 22 of 24.
   - Setting ε_j = max(ε_j, rλ̃_j): the counts 18 and 25 are unchanged at r = 10⁻⁴, and nothing passes at r = 10⁻³ for N ≤ 40. Both agree with the paper.
6. **Completeness numbers (p. 19):**
   - The smallest gap |G_σ − G_σ₀| at t = 0.0015 is 2.969×10⁻³, consistent with "at least 2.96×10⁻³".
   - The detection thresholds λ < 1.662×10⁴ and λ < 9.82×10³ are right.
7. **Weyl-law consistency:**
   - Predicted counts at λ_c: 2001.4 against 2002 and 2001 in Table 4 for the triangles; 4454 against 4451 and 4359 against 4357 for ϑ = 0 and 2.8.
   - Predicted λ̃₈₄₇ ≈ 2539, matching "up to about 2540".
8. **Ratios:** exact a-priori N values are 43 188, 7.4356×10¹² and 6.8176×10⁹. "56 to 2.7×10¹¹" is 56.3 and 2.66×10¹¹, and "at most 1.7" is 1.66. All correct.
9. **Independent check of Table 5, not in the paper.** For t between 0.07 and 0.2, the spectral tail beyond λ̃₄₀ is negligible, so Z₄₀(t) − G_σ(t) should equal the geodesic term. Divided by the contribution of one oriented primitive class at the systole length, it gives **2.000** for O(3,3,12) (t = 0.1, 0.15) and **2.005** for O(2,8,8) (t = 0.1). That is exactly one unoriented systole geodesic in each case. This independently confirms the completeness and accuracy of the 40 tabulated eigenvalues, the systole values and the normalisation of the geodesic term.
10. **Section 8 numbers:**
    - ℓ₂,₃ = 0.56206.
    - 2 arccosh((1 + 2 cos(2π/7))/2) = 0.98399.
    - At m = 4096 the rescaled λ₁ is 1.163, consistent with "between 6% and 16% above".

## 4. FATAL

None.

## 5. MAJOR

**M1. The completeness evidence is tied to the known signature, and statement (iv) misses what the test itself detects (pp. 17, 19).**
The paper's own experiment shows that one wrong eigenvalue misleads the test 19 times out of 24. Yet completeness rests on:
- one trace comparison at t = 0.0015 against the **true** signature;
- agreement between the single-window and two-window solves, which use the same discretisation;
- for O_ϑ above 9.8×10³, agreement of eigenvalue counts across discretisations.

I reran all 24 corrupted lists. In **every** case, at some N between 9 and 30 and some t, **no** signature in S passes. By Theorem 7.1 that cannot happen for a correct, complete list. So the claim that "a user who raises N until (C1) holds would stop at the wrong answer" is incomplete: carrying on flags the corruption without using the signature.

Requested:
- (a) A decision protocol that does not depend on the signature: accept σ only if some signature passes at every (N, t) up to the end of the trusted range, and σ is the only one ever singled out. Report it for all ten examples.
- (b) Sylvester inertia counts of K − sM at the window boundaries. The factorisations already exist, so this is free.
- (c) The completeness residual as a function of t over [10⁻³, 10⁻¹], against every σ ∈ S, rather than at one time.

**M2. The perturbation term is needlessly crude, claim (v) is an artefact of it, and a certified result is within reach (pp. 16–17).**
Theorem 7.1 uses t Σε_j. The sharper term t Σ ε_j e^{−(λ̃_j−ε_j)t} is valid; the proof already notes this, and the completeness budget already uses it. With the sharp term:

| r | O(2,8,8): (C1) Δ / (C2) Δ / (C1) C* | O(3,3,12): (C1) Δ / (C2) Δ / (C1) C* |
|---|---|---|
| ε_j as printed | 18 / 20 / 24 | 25 / 29 / 36 |
| 10⁻³ | 18 / 21 / 24 | 25 / 29 / 37 |
| 10⁻² | 21 / – / 32 | none ≤ 40 |

So "for r = 10⁻³ the criterion fails" says something about the crude bound, not about the data. It also means that relative enclosures of about 10⁻³ for the first 25–40 eigenvalues are enough. That is routine for the guaranteed lower-bound methods the paper cites (Liu–Oishi [36], Carstensen–Gedicke [37]), and bounds by index also certify completeness. Add a validated G_σ, an interval version of the systole enumeration and outward rounding in E_N, and the signatures of O(2,8,8) and O(3,3,12) would be **proved**. I ask the authors to do this or explain why it cannot be done. In either case, use the sharp term and redo Table 6 and statement (v).

**M3. The comparison with Theorem 6.2 is not like-for-like (abstract, p. 3, p. 21, Fig. 2 caption).**
The test chooses only among signatures of the **exact** area (|S| = 3, 6 or 10). Theorem 6.2 chooses among all of Sig(A, M), where the worst-case area separation δ₁ = 1/(2L_M) governs (for M = 12, γ* = δ₁). The quoted factors of 10² to 2.7×10¹¹ therefore mix knowing the area exactly with using the data.

I ran the test over all 48 signatures of area ≤ π/2 with orders ≤ 12, using only the area upper bound and the diameter count. (C1) still holds:
- N = 20 for O(2,8,8), against 18 with the area known;
- N = 32 for O(3,3,12), against 25.

The nearest competitors are (2,6,11) and (2,7,9). So the authors' attribution is probably right, but the paper must show it. Run this for all ten examples and use those counts in the comparison, or both sets. This also removes input (i) from the list of limitations.

## 6. MINOR

- **m1 (p. 18, Table 4).** The column is labelled as proved bounds, but 4.671 is below 4.67119 (ϑ = 0.4) and 5.820 is below 5.82020 (ϑ = 1.6). Round up, or state that unrounded values are used. The effect is negligible.
- **m2 (p. 17, (iv)).** Say which geodesic count the "19 of 24" uses: Δ gives 19, C* gives 22.
- **m3 (p. 17, (v)).** Robustness is shown only for the Δ counts. The headline C* counts change at r = 10⁻⁴ under the crude term: 24 becomes 25, and O(3,3,12) has no (C1) at N ≤ 40.
- **m4 (p. 15, Fig. 1).** With the coarse choice s = kt/20, (C2) already holds at N = 20 on t ∈ [0.0546, 0.0565], and N = 21 holds on [0.048, 0.0585]. The difference from Table 6 comes from the figure's coarse time grid, not from refining s. Correct the sentence and state the time grid.
- **m5 (p. 21).** "2×10⁸ for the triangle orbifolds" is actually 1.9–2.8×10⁸. "(λ̃_N − ϵ_N)t of about 8 to 11" is 7.7–8.4 for the triangles.
- **m6 (p. 20).** The range of the s/t grid and the "61 points around each minimiser" refinement are not specified.
- **m7 (p. 19).**
  - The worst-case rounding error of summing 2850 terms totalling about 83 is roughly 3×10⁻¹¹, above the 1.5×10⁻¹¹ budget. Use compensated summation and state a bound.
  - The quadrature error is 1.7×10⁻¹³ absolute; say so.
- **m8 (p. 19).** The convergence evidence is delegated to the companion paper's supplement; include a small h/p convergence table here.
  - Justify (0.07, 12) as the comparison level against the production level (0.05, 10).
  - Plot ε_j/λ̃_j against j over the complete range.
  - Say that for the lowest eigenvalues ε_j measures solver and rounding noise, not discretisation error.
- **m9 (p. 20, Table 5).** Eigenvalues are printed to 6 decimals next to ε_j ≈ 10⁻¹². I confirm the 6-decimal values reproduce every triangle count; say so, or print more digits.
- **m10 (p. 18).** Define "clusters resolved at relative 10⁻⁹" and explain how multiplicities are counted. For example, the D4 symmetry at ϑ = 0 gives exact double eigenvalues that fall into different sectors.
- **m11 (p. 3).** "For order bounds M = 3 and M = 12 alike" applies only to the family; the triangle orbifolds need M ≥ 12.
- **m12 (p. 22, Fig. 2).** Say whether the diamonds are (C1) or (C2). The headline C* counts are not plotted, and N_obs is not tabulated anywhere.
- **m13 (Remark 6.3(c)).** Report the geodesic-side check of item 9 above, and use the enumerated geodesics up to length 4 to sharpen H(t).
- **m14 (p. 20).** The N versus N + 1 convention differs between the test and Theorem 6.2. Use one convention, or state it in the caption of Table 6 and Fig. 2.

## 7. Presentation

- **P1 (p. 20, Table 5).** The heading "O(3,3,12)" sits over O(2,8,8)'s ε/BC columns, and the vertical rule collides with "N|21".
- **P2 (p. 21, Table 6).** The time entries have inconsistent significant figures (e.g. 0.084 next to 0.0856).
- **P3 (p. 15, Fig. 1).** The y-axis label |G_σ₀(t) − G_σ(t)| also covers the bound curves; use a neutral label and a legend.
- **P4 (p. 17).** Add a small table marking each of the five inputs as proved, estimated or assumed for each example.

## 8. Recommendation

**Major revision.** Confidence is high on correctness, because every number I could check reproduces; moderate-to-high on the recommendation.

**What is good:**
- Theorem 7.1 is correct.
- Table 3 reproduces to every digit, Table 4 is correct, and the triangle rows of Table 6 reproduce including the time windows.
- The framing is honest, and the right robustness and deletion experiments were run.
- The independent trace check in item 9 strongly confirms the tabulated spectra.

**Why not accept as is:**
- Statement (v) reflects a crude bound, not the data (M2).
- The headline comparison mixes knowing the exact area with using the data (M3).
- The completeness evidence is tied to the known signature, and the paper misses that its own test flags corrupted lists without it (M1).

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Report a protocol that doesn't depend on the signature; give inertia counts; show the completeness residual as a function of t against all of S; revise (iv). |
| M2 | Use the sharp perturbation term; redo Table 6 and (v); either certify the two triangle orbifolds (eigenvalue enclosures at about 10⁻³, validated G_σ, interval systole) or explain why not. |
| M3 | Run the test over Sig(A, M) with only an area upper bound; use those counts (or both sets) in the abstract, §7.2 and Fig. 2, or reword the attribution. |
| m1–m14 | As stated in each item. |
| P1–P4 | As stated in each item. |

---

The scripts behind each result are `thm62.py` (Table 3), `test71.py` (Table 6), `test71_sharp.py` (M2), `test_areaub.py` (M3), `test_delete.py` and `test_detect.py` (M1, m2), `trace40.py` (item 9) and `fig1.py` (m4).
