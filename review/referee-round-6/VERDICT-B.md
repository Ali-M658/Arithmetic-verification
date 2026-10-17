# VERDICT-B: referee round 6, Paper B ("Finitely many eigenvalues determine the signature of a hyperbolic orbifold", AGAG)

Reports: `B-a-editor-quantum-chaos/`, `B-b-cone-manifold-geometer/`, `B-c-prime-geodesic-analyst/`,
`B-d-hp-fem-a-posteriori/`, `B-e-mathscinet-reviewer/` (each `REPORT.md`, verbatim). No length remark
needed excluding.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| B-a editor (quantum chaos) | **SEND TO REVIEW**; provisional major revision | about 85% no fatal error; 60% the paper can reach the bar |
| B-b cone-manifold geometer | major revision | high (correctness), medium-high (M1) |
| B-c prime-geodesic analyst | major revision | high (correctness), medium (significance) |
| B-d hp-FEM a-posteriori | major revision | high (recomputations, M2, m1) |
| B-e MathSciNet reviewer | major revision | high (checks), moderate (recommendation) |

**Stop condition: NOT MET.**

No reviewer found a false statement. Every table was reproduced by at least two reviewers (Tables 2, 3, 4,
6 in full; the triangle rows of Table 6 and the 19-of-24 completeness ablation exactly).

## FATAL

None.

## MAJOR (deduplicated; checked against the repository)

| id | issue | raised by | status | evidence / resolution |
|---|---|---|---|---|
| B1 | The main theorem rests on results stated without proof and taken from the companion (Theorem 2.1 admissibility, Lemma 2.2 count and first bound, Proposition 2.3, Lemma 3.1, Theorem 3.2); the paper cannot be verified from refereed material. | B-c M1, B-e M1-M2, B-a M3 | **CONFIRMED** | Table 1 of the paper lists them as imported. Resolution: prove them in an appendix of this paper (the counting bound is replaced by B2's new lemma, proved here; Proposition 2.3, the cone-polynomial structure, Lemma 3.1 and Theorem 3.2 with their proofs; admissibility of the heat function by the standard conditions). |
| B2 | The factor e^{3 diam} in the closed-geodesic count is not needed: Lemmas 4.2-4.3 give a count n_O(x) ≤ K(A,ε,M) e^x with K polynomial in A, M, 1/v_0; the diameter-based count drives t_3 and the class-level failures of Section 7, and the sentence on p. 11 that a count without the diameter "does not transfer directly" is unfounded. | B-b M1, B-c M2, B-a M1 (part) | **CONFIRMED** | Proof: maximal 4r_0-separated set Y (|Y| ≤ A/v_0 by Lemma 4.3), base points moved to cone points within r_0, orbit points of distinct cosets 2ρ_1 apart (Lemma 4.2, (H1)), every closed geodesic within 5r_0 of a base point; n_O(x) ≤ (A/v_0) M (cosh(x+10r_0+ρ_1)−1)/(cosh ρ_1−1). For A = π/2, M = 12, ε = 1.8626 the constant is about 3.5×10^9, against π e^{3D}/A ≈ e^{3375}. Resolution: new lemma; Theorem 6.2, Table 3, the class-level column of Table 6 and Figures E2-E3 recomputed by their scripts; the diameter bound stays as a separate result (used for the finiteness remark of Section 1 and Table 2). |
| B3 | The heat function is not the natural test function: a test function with Fourier transform supported below the systole removes the geodesic term; the paper should adopt it or explain why the heat function is kept, and should not attribute the cost to "knowledge of the geometry". | B-a M1 | **ANSWERED IN PART (after B2)** | With B2 the geodesic cost is polynomial in A, M, 1/ε. A compactly supported test function still needs a bound for the spectral tail, which the proof takes from the heat trace (Proposition 5.2), so the geometric input does not disappear. Resolution: Remark 6.4 (rem:testfn) compares the two routes: a test function with Fourier transform supported below the systole removes the geodesic term and t_3, but the separation of the signatures and the tail bound (Proposition 5.2, through Lemma 2.2) remain; the remark does not attribute the method to any paper. The sentence on the geometry is removed (B5). |
| B4 | "Decides" in the abstract, Section 1, Section 7.2 and the Fig. caption overstates what is shown: the criterion of Theorem 7.1 holds with estimated errors, for lists assumed complete; "four of ten" holds only at M = 3. | B-d M1, B-a M5, B-e m6, B-a m6 | **CONFIRMED** | Abstract and §7.2 wording. Resolution: reword everywhere; report the M dependence; numbers recomputed after B2. |
| B5 | "Most of the gap between the test and Theorem 6.2 is knowledge of the geometry" (p. 19) is contradicted by Table 6: the data factor dominates except at M = 3. | B-d M2, B-a M1 | **CONFIRMED** | Table 6: geometry factor ≈ 3×10² (triangles), 21-840 (family); data factor ≈ 10^6, 10^7-3×10^8 (M = 12), 23-50 (M = 3). Resolution: rewrite with both factors per row, after B2's recomputation. |
| B6 | Completeness, the input the conclusions depend on, has the weakest support: the trace check uses only the true signature and one time; inertia counts of the factorisations would certify discrete completeness; the error model is misdescribed (the discrete domain is a polynomial approximation, so no min-max upper bound even in exact arithmetic; the low ε_j are at rounding level); the robustness of the counts to the eigenvalue errors is not quantified. | B-d M3-M4, B-a M5, B-e m7 | **CONFIRMED** (statements); inertia counts are **not available** without re-solving | Resolution: state the domain approximation and the rounding level honestly; run the completeness trace comparison against every σ ∈ S and report the margins; quantify the robustness margin by the existing test code; state the inertia-count route as what would certify discrete completeness, not done here. |
| B7 | Significance beyond compactness; Theorem 1.3's content is largely [14, Thm 5.3] plus pigeonhole; the new input is the uniform systole bound. | B-a M2, B-e (significance) | **CONFIRMED** (presentation) | Resolution: state the contribution precisely; credit [14]; name Proposition 8.2's systole bound as the new geometric input; check what [14, Thm 5.3] states (B-e m4). |
| B8 | Uniform accuracy hypothesis is wasteful; the perturbation bound discards e^{-t min(a,b)}. | B-a M4, B-d m3, B-e m7 | **CONFIRMED** | Resolution: use |e^{-at}−e^{-bt}| ≤ t|a−b|e^{−t min(a,b)} in Theorem 7.1 (the completeness budget already uses it) and remark that Theorem 6.2's hypothesis may be weakened accordingly. |

## MINOR and presentation, with disposition

| id | item | raised by | disposition |
|---|---|---|---|
| b1 | Lemma 4.2's 1/M not intrinsic; v_0's 1/M | B-b m1 | fix: one sentence (not intrinsic; Jørgensen for elliptic pairs gives an order-free bound when an order is at least 7) |
| b2 | thick-thin diameter speculation unproved, Dryden-Parlier excludes order 2 | B-b m2, B-a m10 | fix: removed (unnecessary after B2) |
| b3 | certify systoles by closed forms / interval arithmetic | B-b m3, B-a m11, B-d m10 | fix: closed forms for O(2,8,8), O(3,3,12) checked; family 4b stated as numerical (Proposition 8.5 proves ℓ ≤ 4b only) |
| b4 | 2 diam P factor 2; diam O = diam P not proved | B-b m4, P3 | fix: "computed diameters" |
| b5 | "diameters growing like log m": only lower bound proved | B-b m5 | fix |
| b6 | quasi-isometries → bi-Lipschitz | B-b m6, B-e m5 | fix |
| b7 | where σ* loses | B-b m7 | fix: one sentence |
| b8 | both halves of the collar | B-b m8 | no change (constant only) |
| b9 | lower bound ℓ in Lemma 2.2 / Theorem 7.1 | B-b m9 | fix |
| b10 | admissibility sentence contradictory; elliptic convention and E_m(0+) check | B-c m1 | fix |
| b11 | Proposition 2.3(a) two-line proof; monotonicity | B-c m3 | fix (with B1) |
| b12 | Theorem 3.2(ii) Vandermonde proof | B-c m4, B-e | fix (with B1) |
| b13 | A used for class bound and common area | B-c m5, B-e P5 | fix |
| b14 | δ_1 = 1/(2 lcm) crude; individual δ_k | B-c m6 | remark only (changes logarithms) |
| b15 | max instead of sum in the margin; least area in Sig(A,M) | B-c m7 | remark only |
| b16 | "any rational t ≤ t* may replace it": constants must be recomputed; remark on K; computability cost | B-c m8, B-a m7 | fix |
| b17 | indexing of N (λ̃_0..λ̃_{N-1} vs λ̃_0..λ̃_N) | B-c m9, B-e m1, B-a m5 | fix: one convention stated |
| b18 | "attained" for k = 2 only | B-c m10 | fix |
| b19 | Fig. E2 (Fig. 1) does not match the text (N = 20 vs 21, half-gap vs gap, grid times) | B-d m1 | check the generating script; fix text or figure data |
| b20 | one-sided acceptance interval | B-d m2 | remark |
| b21 | completeness budget formula | B-d m3 | fix |
| b22 | "(λ̃_N−ϵ_N)t of about 11" | B-d m4, B-e m2 | fix ("about 8-11") |
| b23 | enumerated short geodesics in H | B-d m5 | remark |
| b24 | wrong-signature check over all N | B-d m6 | fix: run and report |
| b25 | family completeness details | B-d m7 | fix |
| b26 | mixed Dirichlet-Neumann corners | B-d m8 | fix: one sentence |
| b27 | completeness hypothesis explicit; ordering hypothesis unused | B-d m9 | fix |
| b28 | Strohmaier-Uski "follows the idea of" | B-e m3 | fix |
| b29 | [14, Thm 5.3] log Q vs log m; Hejhal page | B-e m4, B-a m2 | check the source; fix |
| b30 | Mumford [3, Cor. 3] numbering | B-e m9 | check the source |
| b31 | C_l undefined; Theorem 3.2 citation vs Table 1 | B-e m10 | fix |
| b32 | bibliography [33] GTM 91, [23], [10] | B-e m11 | fix after checking records |
| b33 | software versions; e^{3D} overflow handling; scripts for Figs | B-e m8 | fix |
| b34 | "no finite part of the spectrum bounds the orders" | B-a m1 | fix |
| b35 | λ_j → 1/4 via [14] | B-a m2 | check; fix |
| b36 | Buser-Courtois analogy qualified | B-a m3 | fix |
| b37 | "(C1) is the theorem's own conclusion" | B-a m4 | fix |
| b38 | missing references: Linowitz-McReynolds-Pollack-Thompson; Friedman-Jorgenson-Kramer; verified eigenvalue methods | B-a m8, B-d M4 | fix with fetched records |
| b39 | [5] preprint status | B-a m9 | fix |
| b40 | notation clashes (Γ, ε/ϵ, ℓ, p, a, Q, O, σ*) | B-b P2, B-c P1, B-e P5, B-a P1 | fix the gap Γ(t) → g(t), σ* → ℓ_{2,3} |
| b41 | captions too long; Fig. E1 panel labels inside the figure; Fig. E3 marker offsets; N_obs column | B-e P1-P3, B-a P5, B-d P1, P4, P5 | captions shortened; N_obs column added; offsets stated in the text (figure kept); panel letters are kept: the project's figure specification (`figures/SPEC.md`) permits axis titles, tick labels and panel letters and nothing else inside a figure |
| b42 | P1 (H2) asymptotic case proof | B-b P1 | fix |
| b43 | Theorem 6.2 definitions as a list; caveats collected | B-c P2, B-a P6 | fix |

## Plan

B1 and B2 change mathematics: new counting lemma, Theorem 6.2 restated with the count constant, appendix with
the proofs of the results previously imported; each gets a script with asserts and a blind subagent check.
Then recompute Table 3, Table 6 and Figures E2-E3 through their scripts, and rewrite §§1, 6.2, 7.2 with the
new numbers and the honest wording of B4-B6.

## After the fixes

Blind check of the mathematical changes (`blind-check-B/REPORT.md`): Lemma 2.2, Lemma 4.5 with Lemmas 4.2-4.3,
Theorem 6.2 with all rows of Table 3, Appendix A and Theorem 7.1 VERIFIED. Three statements of Section 7 were
out of date and are corrected: the paragraph on estimated counts (no count of Table 6 is an estimate any more;
replaced by "both criteria hold within the complete range"); "a factor of at most 1.6" (1.66 at
vartheta = 2.8, M = 3; now "at most 1.7 in either direction"); "at least 3.0e-3" (2.97e-3 in
`theory/eigen/data/practice_checks.csv`; now 2.96e-3, rounded down). Also: "about 800 eigenvalues, below
lambda 2800" replaced by the range from Table 6 (461 to 847, lambda_N up to 2540); "19 of 24" now says
"at the first N"; the parenthetical on weighted errors is restricted to over-estimates.
