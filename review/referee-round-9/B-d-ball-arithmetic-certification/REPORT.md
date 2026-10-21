<!-- Round 9 B-d referee report: returned text saved verbatim; the reviewer could not write files -->

I could not save the report to REPORT.md because writing the file was refused, so the full report follows. My verdict is minor revision, with high confidence for the numerical side. I recomputed every table entry in my remit and found no numerical error that affects a stated result. Proposition 6.4 is correct and reproducible from the paper's description. The main gaps are in how the computations are documented and how far the eigenvalue evidence is from proof. My scripts are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/B-d-ball-arithmetic-certification/scratch/code/ (sig.py, cert.py, consts.py, test71.py, robust.py, misc.py).

# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Submitted to: Annals of Global Analysis and Geometry
Scope of this report: Section 7 (the a-posteriori test, Theorem 7.1, and §7.1 on numerical methods), Corollary 6.3 and Proposition 6.4 with Table 3 (the gap certified in ball arithmetic), and every numerical claim, table and figure. I comment on the analytic sections only where a numerical claim depends on them. The marked placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) are treated as known. Page numbers are those of the PDF. Every typographical, sign or figure point below was checked on rendered page images (pdftoppm), not only on extracted text.

## Summary

The paper proves that among closed hyperbolic 2-orbifolds of area at most A, systole at least ε and cone orders at most M, the first N eigenvalues, each known to within δ, determine the signature. N and δ are explicit (Theorem 6.2). The closed-form constants are astronomically large (Table 4: N up to 3.8e30). The paper therefore adds Corollary 6.3, which replaces the heat-invariant lower bound on the gap by the gap itself evaluated at one time. Proposition 6.4 certifies this in Arb ball arithmetic for six classes (Table 3), giving N = 139 to 7416 for the classes of the examples, and 387182 for an extra class with ε = 0.1. Section 7 gives an a-posteriori test (Theorem 7.1) and runs it on finite-element spectra of O(2,8,8), O(3,3,12) and eight orbifolds of signature (0;3,3,3,3). The paper states plainly that these runs use estimated errors and lists assumed to be complete, and that they are consistency checks, not determinations.

## Significance

The numerical side contributes two things. The first is a rigorous, small, checkable computer-assisted statement, Proposition 6.4, which turns an effective but useless bound (Theorem 6.2) into numbers of practical size. The second is a well-designed, honestly labelled consistency test. The certification is a sound use of validated quadrature. Separating the a-priori constants (Table 4), the certified class-level numbers (Table 3) and the data-dependent counts (Table 7) makes clear where the loss in Theorem 6.2 comes from: from Lemma 6.1, not from the data (p. 24). That analysis is worth publishing.

## Correctness, and what I recomputed

I independently recomputed, from the formulas in the manuscript alone and without the authors' code, essentially every number in my remit. My setup was a virtual environment with python-flint 0.9.0 (Arb) and mpmath at 40 digits. Every number I checked agrees.

1. **Sig(A, M).** I enumerated all hyperbolic signatures with area in (0, A] and orders at most M. The counts are 27, 48, 8, 8, 281 and 12, matching the |Sig(A,M)| column of Table 3. The six signatures of area π/2 with orders at most 12 are (2,6,12), (2,8,8), (3,3,12), (3,4,6), (4,4,4) and (2,2,2,4), as in Fig. 1 and Table 7.

2. **Proposition 6.4 / Table 3, certified in Arb.**
   - Method: at 200 bits, with acb.integral on finite intervals, I enclosed I(t) via the split r·tanh(πr) = |r| − 2|r|/(e^{2π|r|}+1) and each E_m(t). Tails were added to the radii, using the exponential tail bounds described on p. 15.
   - Gap enclosures: the certified minimum gaps over Sig(A,M) are 0.0158823, 0.0065273, 0.1520293, 0.1655108, 0.0013739 and 0.1666487, with radii below 1e-39. Each Θ in Table 3 is a correct rounded-down lower bound. The minimising pairs are, for example, (2,3,8)/(2,4,5), (2,4,10)/(2,5,7) and (5,5,10)/(4,8,8). For all three M = 3 classes the minimising pair is (2^5)/(2,3,3,3); its gap tends to 1/6, the difference of Σ b0.
   - Hypotheses of Corollary 6.3: all hold at the stated t with the stated Θ.
     - t ≤ t2 holds in every row.
     - B*(t) ≤ Θ/8 holds in every row. The pairs (B*, Θ/8) are (8.0e-6, 2.0e-3), (7.1e-5, 8.2e-4), (1.793e-2, 1.900e-2), (1.671e-2, 2.069e-2), (1.406e-4, 1.716e-4) and (1.394e-2, 2.082e-2).
     - Λt ≥ 1 holds easily: Λt ranges from 12.5 to 27.9.
   - N and δ: I get exactly N = 244, 283, 139, 2605, 7416 and 387182, and δ = 1.167e-4, 4.273e-5, 5.899e-4, 4.867e-4, 2.488e-6 and 2.141e-4. The table's δ values are correctly rounded down.
   - Choice of t: a scan over t (floating point) gives best N of 140, 2666, 389554 and 244 for four of the rows. The stated times really are near-optimal.
   - Conclusion: **Proposition 6.4 is correct as stated.** I reproduced it in under a minute from the description in the paper, which says a good deal for the description.

3. **Table 4.** All entries reproduce: C*, t1, t3, Θ*, Λ, N, δ and the binding constraint. For example, row 1 gives N = 339877849 (3.4e8 rounded up), and row 8 gives N = 3.75e30 and δ = 8.65e-278. Other claims on p. 17 also reproduce:
   - "4e18 to 1.1e6 at A = 10π": I get 4.19e18 with k* = 14, against 1.084e6.
   - "t1 attained at k = k*" holds in every row.
   - "t3 binds from ε = 0.44 down, for A = 4π/3, M = 3": I get 0.44.
   - The halving factors run 5.239, 5.127, 5.008, 4.902, 4.812, 4.737, 4.673, matching "from 5.24 to below 4.7 over seven halvings".
   - On p. 12, πe^{3D}/A runs from 10^196.5 to 10^29325.4, matching "3e196 to 2e29325".

4. **Table 2.** All twelve D values reproduce.

5. **Table 5.**
   - The closed-form systoles are 2.25676793, 1.86260406 and 4b(ϑ) = 2.63391579, 2.20269529, 1.83130274, 1.51573792, 1.25042850, 1.02912884, 0.84559363 and 0.69399455. Every tabulated ℓ is a correct round-down, and the smallest margin is 5.5e-8 (O(3,3,12)), confirming "at least 5e-8".
   - From the hyperboloid vertex coordinates, 2 diam P for the family is 4.584863, 4.671195, 4.921618, 5.313982, 5.820204, 6.412895, 7.068806 and 7.769742. All are correctly rounded up in Table 5. The triangle diameters 2.448 and 2.158 are also correct.
   - The C* values match Table 4 up to rounding; see m1.
   - Weyl's law is consistent with the (λc, Nc) pairs: Nc ≈ (A/4π)λc gives 2000 and 4453, against 2002/2001 and 4451.

6. **Table 7, triangle rows, recomputed from the Table 6 data.** Table 6 gives λ̃0..λ̃40 and ε_j, which is enough for every triangle count, since the largest is N = 36. I used the grid of §7.1 without the local refinement.
   - O(2,8,8): (C1),Δ = 18 at 0.0565; (C2),Δ = 20 at 0.0556; (C1),C* = 24; (C1),Sig(A,M) = 24.
   - O(3,3,12): 25 at 0.0414; 29 at 0.0401; 36; 36.
   - All eight counts agree with Table 7. Window midpoints agree to the third digit, with the remaining difference coming from the grid refinement.
   - At no grid time and no N ≤ 40 did either criterion select a wrong signature.

7. **Robustness claims of §7(iv)–(v), recomputed from the Table 6 data.**
   - With ε_j replaced by max(ε_j, rλ̃_j), the counts stay at 18 and 25 for r = 1e-3. For r = 1e-2, O(2,8,8) needs 21. For O(3,3,12) no N ≤ 39 passes, which is consistent with the stated 43.
   - Deleting or duplicating one of λ̃1, λ̃2, λ̃3, λ̃5, λ̃8, λ̃12 makes (C1) conclude a wrong signature at its first decision in exactly 19 of the 24 cases (9 for O(2,8,8), 10 for O(3,3,12)), as claimed, always at N ≤ 26.

8. **Further checks on the triangle data.**
   - Nobs = 3 for both triangle orbifolds, checked for N′ ≤ 41.
   - The raw data are consistent with the trace formula including the geodesic term. At t = 0.08, Σ e^{−λ̃t} − G_true = 2.0e-7 for O(2,8,8), against 1.95e-7 predicted by the two systole classes alone.
   - The figure on p. 24, Hyp ≈ 2.8e-10 at t = 0.0562, is reproduced.

9. **Ratios and ranges in the text.**
   - "56 to 2.7e11" (Fig. 2 caption): 43188/767 = 56.3 and 7435635783983/28 = 2.66e11.
   - "Factor 10^2 to 2e3; 1.9 to 2.8e8; 10^10 to 2e11" (p. 24) reproduces.
   - "Factor of at most 1.7" (diameter count against C* count): the maximum is 767/461 = 1.66.
   - "6 to 12" (p. 24 to 25): the ratios run 5.65 to 11.8.
   - (λ̃_N − ε_N)t = 7.7 and 8.4 for the triangle orbifolds.

10. **Other numerical claims.**
    - d3 = 25/12 for (2,8,8) against (3,3,12).
    - d2 = −1/12 for (4,4,4) against (3,4,6).
    - (0;2,2,2,2,7^7) and (0;4^6,8^4): both have area 12π, the same Σb0 (54) and the same Ψ2 (2430), and a different Ψ3.
    - ℓ_{2,3} = 0.56206.
    - The O(2,3,7) and modular systoles, 0.983986 and 1.9248.

The rendered pages contain no numerical error that affects a stated result. The issues below concern how complete the certificate's description is, how informative the error estimates are, and the gap between "estimated" and "certified" in Section 7. That gap is the paper's main practical weakness, and it is much easier to close than the paper suggests.

## FATAL

None.

## MAJOR

**M1 (pp. 15–16, Proposition 6.4 and Table 3): the computer-assisted proof is not fully specified in the paper.** Proposition 6.4 is a theorem whose proof is a computation. As written, the proof paragraph (p. 15) leaves out several things a reader needs in order to check it without the deposit:

- (a) How Sig(A, M) is enumerated, and why the enumeration is complete. Lemma 5.1(i) gives n + 4g ≤ A/π + 4, which suffices, but the paper should say that the list is generated from it, and give the list or its size per class. The sizes are in Table 3; the generation is not.
- (b) That the tail bounds (≤ e^{-80}) are added to the ball radii and not merely "bounded". The tail intervals R used should also be stated.
- (c) That C*, ϖ, B*(t), t2, Z♯, Λ, N and δ are evaluated in ball arithmetic. It should also say that N is the floor of an enclosure that does not straddle an integer (or is rounded up), and that δ is rounded down. Table 3, unlike Table 4, does not say how N and δ are rounded. I checked that the printed δ values are rounded down.
- (d) The certified margins. Table 3 should include columns for B*(t), Θ/8 and Λt, and name the minimising pair. Some margins are thin: in row 3, B* = 0.01793 against Θ/8 = 0.01900, a margin of 6%. A reader should see this without rerunning the code.
- (e) The Arb/FLINT version, alongside python-flint 0.9.0, and the integration tolerances.

Since the deposit identifier is a placeholder, the paper must stand on its own here. *Resolution:* about half a page plus three columns in Table 3. I emphasise that I found the claim correct.

**M2 (pp. 19–22, §7(iv) and §7.1, completeness): the one hypothesis that decides the outcome is left unproved, although a proof for the discrete problem is nearly free.** The paper shows, and I confirmed from Table 6, that one missing or duplicated eigenvalue makes (C1) choose a wrong signature in 19 of 24 cases. Yet completeness rests on three things: a single heat-trace comparison against the true signature, the agreement of single- and two-window runs, and count agreement between discretisations. The authors already compute one sparse factorisation of K − sM per window (p. 21). The inertia of an LDLᵀ factorisation at each window boundary, which MUMPS, PARDISO and CHOLMOD-type LDLᵀ all report, counts the discrete eigenvalues below s exactly (Sylvester's law of inertia). This would turn "no window miss found" into a proof that the computed list is complete for the discrete problem. The paper mentions this on p. 20 and then says "We have not done this". For the purpose the paper itself names, it is the cheapest available improvement.

Two related points:

- (i) The completeness budget on p. 22 uses "a Weyl-law estimate of the tail beyond the computed range", which is not a bound. The paper's own index-free inequality, Σ_{λ>Λc} e^{−λt} ≤ e^{−Λc(t−s)} Z_O(s) with Z_O(s) ≤ A/(4πs) + β + H(s), gives a rigorous tail bound that does not presuppose completeness. With Λc = 2.2e4 and t = 0.0015, I obtain 3.5e-11, against the Weyl estimate of about 4e-13. The detection threshold then moves from 1.66e4 to about 1.58e4. This is just below the 1.6e4 cut, so the cut, or t, would need a small adjustment. The budget becomes rigorous apart from floating-point summation.
- (ii) The completeness check is run against the true signature. This is harmless for a consistency check, but it should be said in (iv), not only implied.

*Resolution:* add inertia counts, at least for the triangle problems, and replace the Weyl estimate by the rigorous bound; or explain why either is not possible.

**M3 (pp. 20–21, §7(v), "Error estimates"): the ε_j used in the test do not estimate discretisation error over the range where most of them are reported.**
- In Table 6, every ε_j is 10 to 20 times the floor 1e-14·λ_j; for example, λ̃1 = 3.838887 has ε = 6e-13. The paper itself says that here "the difference reflects the solver and rounding rather than the discretisation".
- The two "independent discretisations" (h, p) = (0.05, 10) and (0.07, 12) share the geometry representation, the quadrature rule for w and the solver. Any error common to both is invisible to their difference: rational-quadratic sides, curved elements of order p, and a weight w integrated by quadrature.
- The paper is honest that these are estimates. But the claim that the test "holds with the estimated errors" is then close to "holds with ε_j ≈ 0". The informative statement is the robustness one (r ≤ 1e-3 leaves the counts unchanged), which I confirmed.

*Resolution:* in the main text, give the convergence table for at least the first 40 eigenvalues of one triangle orbifold. It is currently in the companion's supplement, whose identifier is a placeholder. Also state explicitly that for N ≤ 40 the ε_j are at rounding level and the test's conclusion does not depend on them.

**M4 (pp. 3, 20, 23–25): a rigorous instance is within reach, and the paper should either do one or say concretely why not.**
- Proposition 6.4 says that for O(2,8,8) and O(3,3,12), in the class π/2, ε = 1.8626, M = 12, the first 283 eigenvalues known to within 4.27e-5 absolute decide the signature. At λ_283 ≈ 2300 that is a relative accuracy of about 2e-8.
- For the family at M = 3, ϑ = 0, the requirement is 139 eigenvalues to within 5.9e-4.
- The authors' estimated errors are about 1e-11 relative, three to six orders below what is needed.
- Guaranteed two-sided enclosures at this accuracy for a few hundred eigenvalues are routine for polygonal domains: Liu–Oishi, Carstensen–Gedicke (refs. [41, 42]), and Plum/Behnke-type homotopy methods. The curved hyperbolic sides and the weight w need care, but the problem is a weighted Laplacian on a fixed polygon in the disc.
- Such an instance would turn the paper's "consistency checks, not proved determinations" into one proved determination from finitely many computed eigenvalues. That is the paper's stated aim, and it would remove the main caveat in the abstract.

I do not make this a condition of acceptance, but the discussion on p. 20 should say how far the existing δ budget is from the estimated errors. At present the reader is left to think certification would be hopeless, when the opposite is true.

## MINOR

- **m1 (pp. 17, 20).** C* is rounded inconsistently between Table 4 and Table 5. C*(π/2, ·, 12) = 3.545e9 appears as 3.5e9 in Table 4 and 3.6e9 in Table 5. C*(4π/3, ·, 3) = 4.01e5 appears as 4.0e5 and 4.1e5. Table 5 apparently rounds up and Table 4 to nearest, and neither caption says so. Unify the rounding, or state it in both captions.
- **m2 (p. 17, Fig. 1 text).** "For N = 21, at the times 0.050 and 0.056 of the figure's grid ... On the finer time grid of Section 7.1, (C2) holds already with N = 20." On the figure's own grid, with the figure's s-grid s = kt/20, the shaded condition already holds for N = 20 at t = 0.0562. I get H + tail + perturbation = 0.01988 against a half-gap of 0.02035. The sentence implies that N = 20 needs the finer grid. Reword, or explain how the figure's criterion differs.
- **m3 (p. 22, §7.1 "The test").** Every count is the least N on a time grid and an s-grid, so a property of the grid. On a continuous t, a smaller N could pass. Say this once. Also report the smallest relative margin among the reported (N, t) decisions, which by construction lie at the edge of their windows. Without it, "far below every margin" (p. 23) about the floating-point and quadrature errors is not checkable.
- **m4 (p. 22).** The grid of s/t in [1e-8, 1] includes s = t, while Theorem 7.1 takes 0 < s < t. This is harmless, since the bound still holds at s = t, but state it or drop the endpoint.
- **m5 (p. 22, "Systoles and diameters").** The breadth-first enumeration prunes a tile wP when the lower end of d(x0, wx0) exceeds L + 3r. The paper should state why pruning does not disconnect a needed tile. The reason: every tile crossed by a segment from x0 to a point of B(x0, L + 2r) itself meets that ball, so it is kept. It should also state that the translation lengths are computed from interval traces, as ℓ = 2 arccosh(|tr|/2), over the even-length (orientation-preserving) elements.
- **m6 (p. 21).** The triangle spectra used are the single-window ones; the two-window recomputation is used only to confirm. Since the two-window lists exist, are stated to be at the same production level, and give the same counts, make them the primary data.
- **m7 (p. 22).** "Agrees with I + E ... to 4.7e-13 at t = 0.0015, within an error budget of 1.5e-11". The budget excludes floating-point summation of about 2850 terms. With compensated summation this could be bounded at once; please do so, or bound it.
- **m8 (p. 28, Fig. 3).** "Two mesh levels agree to at least 2.3e-10 relative" is the only accuracy statement for the O(2,3,m) data up to m = 4096. At m = 4096 the cone tip is a thin cusp-like region of radius h_m ≈ 7.2, where uniform meshes are problematic. State the meshes or grading used for large m, and whether the area check of p. 21 (2e-14) was also done there.
- **m9 (p. 15).** The tail on the identity side is described as "∫_R^∞ 4re^{−2πr}dr". This is only correct after the split r·tanh(πr) = |r| − 2|r|/(e^{2π|r|}+1), with the |r| part done in closed form, which the text does not say. Add one clause.
- **m10 (pp. 15–16).** Table 3 lists ε to six decimals (1.8626, 2.633915, 0.693994), while Table 4 uses 2.6339 and 0.6939. The classes therefore differ slightly. This is harmless, since t1 binds and C* does not depend on ε here, but say so or use the same values.

## Presentation

- **P1 (p. 16, Table 3).** Add the certified quantities requested in M1(d), and the rounding conventions as in the Table 4 caption.
- **P2 (p. 24, Table 7).** The caption is hard to parse. Splitting it into "columns 5–7: least N and window midpoint for ..." and "column 8: ..." would help. State that the midpoints are of a refined grid.
- **P3 (p. 18, Fig. 1).** The shaded band is a single grey bar at about t = 0.05–0.056 and is hard to see. The curves for N = 21 and N = 100 are not labelled on the plot, and the reader cannot tell which dotted curve is which, or which grey curve is which competitor apart from the darkest. Add direct labels.
- **P4 (p. 25, Fig. 2).** The open and filled markers are shifted left and right of the systole, which makes the x-positions slightly misleading at systole resolution. A note in the caption, not only the text, would help. The caption's "reference count" should be named Nobs there.
- **P5 (p. 31).** The data statement is thorough and lists the programs used. Once the DOI is in, add the commit hash, and the run time of certified_gap.py (about a minute in my reimplementation).

## Recommendation

**Minor revision.** This is for the parts in my remit. I have high confidence in the numerical verdict, because I recomputed every table entry in my remit and all the derived ratios.

Proposition 6.4 is correct, and its certificate is sound and reproducible. Tables 2–5 and 7 (triangle rows) and the figures' numbers agree with my independent computations. The paper is unusually honest about what is certified and what is estimated. What remains:

- M1 is a matter of documentation and must be fixed.
- M2 and M3 concern how the numerical evidence is presented, and can be addressed with modest effort. Inertia counts and a rigorous tail bound are cheap.
- M4 is a recommendation that would substantially strengthen the paper's practical claim.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Specify how Sig(A,M) is generated, how tails enter the radii, the ball evaluation and rounding of all constants including N and δ, and the versions and tolerances. Add B*, Θ/8, Λt and the minimising pair to Table 3. |
| M2 | Sylvester inertia counts at the window boundaries, at least for the triangle problems. Replace the Weyl tail estimate with the index-free bound e^{−Λc(t−s)}(A/4πs + β + H(s)), and adjust the complete range (about 1.58e4 at t = 0.0015). State that the completeness check uses the true signature. |
| M3 | Put a convergence table in the paper. State that the ε_j for low eigenvalues are at rounding level and that the conclusions rest on the robustness check. |
| M4 | Either certify one instance with two-sided enclosures against the δ of Table 3, or state concretely, for example "4.3e-5 needed against 1e-11 estimated", how far existing methods are from doing so and what blocks them. |
| m1 | Unify the rounding of C* between Tables 4 and 5, or state it in both captions. |
| m2 | Correct or explain the Fig. 1 sentence about N = 20 needing the finer grid. |
| m3 | State that the counts depend on the grid, and report the smallest decision margin. |
| m4 | Note that s = t is harmless, or drop the endpoint. |
| m5 | Add the pruning-connectivity argument and the interval trace-to-length step. |
| m6 | Make the two-window lists the primary data. |
| m7 | Bound the floating-point summation error, for example with compensated summation. |
| m8 | Describe the meshes and accuracy checks for large m. |
| m9 | Add the clause about the split of r·tanh(πr). |
| m10 | Explain or unify the ε values between Tables 3 and 4. |
| P1–P5 | Edits to captions and figures. |
