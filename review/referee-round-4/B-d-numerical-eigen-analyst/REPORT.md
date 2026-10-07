<!-- Saved verbatim by the main session from the reviewer's returned text: the harness refused the reviewer's own write. Its code (Python venv with numpy/scipy/mpmath/scikit-fem) is in its git-ignored scratch/. -->

# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Submitted to Annals of Global Analysis and Geometry. Referee (d): numerical analysis of the eigenvalue computations and of the a-posteriori certificate.

## Summary

The paper proves an effective version of the Dryden–Strohmaier theorem. Theorem 1.1 / Theorem 6.2 (pp. 2, 12–13) gives explicit numbers N and δ in terms of A, ε and M. If an orbifold has area at most A, systole at least ε and cone orders at most M, then its first N eigenvalues, each known to within δ, determine its signature. The mechanism is a lower bound for the gap |G_σ(t) − G_σ'(t)| between the signature parts of the Selberg heat trace. That bound comes from enveloping remainders (Props 2.6, 2.7), from integrality of the first differing heat invariant (Lemma 3.5, Theorem 3.4), and from a diameter bound (Theorem 4.4) that controls the geodesic term. The resulting N run from 10^4 to 10^30 (Table 2).

Section 7 turns the same mechanism into an a-posteriori test, Theorem 7.1 (= Theorem 1.2). The paper applies it to finite-element spectra of O(2,8,8), O(3,3,12) and eight orbifolds of signature (0;3,3,3,3). It reports that the test "succeeds" with 21 to 750 eigenvalues (Table 3, Fig. 2). Section 8 shows that the bound on the orders cannot be dropped (O(2,3,m), with numerical illustration in Fig. 3), and it leaves open whether the systole bound is needed.

My charge is the numerics. In brief:
- **The mathematics I checked is sound and well executed.** This covers Theorem 7.1 as a conditional statement, Tables 1–2, the heat invariants, and Figures 1 and 3.
- **The computed spectra are not certified, so "certify/certified" is not justified.** The computed inputs have not been shown to satisfy the hypotheses of Theorem 7.1. The paper says the eigenvalue errors are "error estimates", but the theorem needs error bounds. Completeness of the computed list is asserted, not proved. The systole inputs are not shown to be lower bounds.
- **The test cannot detect a missing or extra eigenvalue.** On my own spectra of the same orbifolds, deleting one eigenvalue, or adding one, makes the test "succeed" with a wrong signature.
- **The fix is feasible.** The required accuracy is modest: relative 10^-4 suffices for the triangle orbifolds. So a genuinely certified version, with guaranteed lower bounds, is within reach.

## Significance

The theoretical contribution is real but modest. The qualitative statement follows from compactness, as the authors say on p. 2. The value added is explicit constants, which are astronomically large, and the clean integrality mechanism (Lemma 3.5) behind them.

For a numerical analyst the interesting part is Theorem 7.1. It is a practical, data-driven sufficient condition that needs 10^2 to 10^11 times fewer eigenvalues than the a-priori bound. If it were coupled with guaranteed eigenvalue enclosures and a rigorous systole bound, it would be a computer-assisted proof of the signature from a finite spectrum, and a nice one. As submitted it is a well-designed heuristic experiment presented in the vocabulary of a proof.

Section 8.1 (high orders behave like cusps) is a good addition, and Fig. 3 is a clear illustration of it.

## Correctness and what was recomputed

All code is in my folder `scratch/`. I worked in a Python venv with numpy/scipy/mpmath/scikit-fem, independently of the authors' repository, which I did not open.

1. **Heat invariants (Section 2, eq. (3), Lemma 3.5).** I implemented ς_i, φ_k(m) from (2), g_k, b_l(m), μ_k (closed form via ζ) and α_k in 40-digit mpmath.
   - α_0..α_3 = 1, −1/3, 1/15, −4/315 (p. 6). Confirmed.
   - b_0(m) = (m²−1)/(12m) (Lemma 5.1). Confirmed.
   - c_1..c_5 for all six signatures of area π/2 with orders ≤ 12.
   - O(2,8,8) vs O(3,3,12): c_1 and c_2 agree, and d_3 = 25/12. This confirms p. 14 ("d_3 t = 25/12 t").
   - (0;4,4,4) vs (0;3,4,6): d_2 = −1/12, as stated after Lemma 3.5 (p. 9).

2. **Table 2 (p. 13): all eight rows recomputed from the formulas of Section 6 and Theorem 6.2.** I recomputed k_*, D, t_1, t_3, N, δ and the binding constraint. All agree to the printed precision except t_1 in row 2 (A = π/2, ε = 1.8626, M = 12): I get 6.849 × 10^-9, which rounds to 6.8 × 10^-9, not 6.9 × 10^-9. N = 6.82 × 10^9 and δ = 4.2 × 10^-25 agree. Also confirmed:
   - The claim on p. 13 that without Theorem 3.4, N at A = 10π, M = 3 would be "about 4 × 10^18": I get 4.19 × 10^18.
   - The "factor near 8 per halving of ε" (p. 14): at A = 4π/3, M = 3, the ratios I get are 9.03, 8.94, 8.86, 8.79, 8.73 for ε = 0.4 → 0.0125.

3. **Table 1 (p. 11).** All twelve values of D(A,ε,M) = 4r_0A/v_0 reproduced. The closed-form bound of Theorem 4.4 is above each of them.

4. **The sets S of Table 3.** By hand enumeration: |S| = 6 (area π/2, M = 12), 3 (area 4π/3, M = 3) and 10 (area 4π/3, M = 12). All three confirmed.

5. **Diameter inputs.** Twice the longest side:
   - O(2,8,8): 2 arccosh(cot²(π/8)) = 4.897 (< 4.9).
   - O(3,3,12): 4.316 (< 4.4).
   
   Both are consistent with the caption of Table 1.

6. **Systoles.** I enumerated the reflection group in the Tits representation in SO(2,1) for word length ≤ 18, using tr = 1 + 2cosh ℓ.
   - O(3,3,12): 1.86260. This is the ε of Table 2.
   - O(2,8,8): 2.25677.
   - O(2,3,7): 0.98399, which is ≥ σ_* = 0.56206 (Prop. 8.2).
   
   This also identifies the two coloured markers in Fig. 2: orange at 1.86 is O(3,3,12), teal at 2.26 is O(2,8,8). These numbers are upper bounds on the systole (see M2).

7. **My own eigenvalues.**
   - **Method.** The orbifold spectrum is the union of the Neumann and Dirichlet spectra of the triangle. I used the Klein model, where the geodesic triangle is exactly straight-sided. The weak form is ∫(1−|x|²)^{-1/2}(∇u·∇v − (x·∇u)(x·∇v)) = λ∫(1−|x|²)^{-3/2}uv. I used conforming P4 Lagrange elements, two uniform refinement levels (33k and 132k dofs per problem), shift-invert Lanczos, and 120 eigenpairs per boundary condition.
   - **O(2,8,8):** λ_1..λ_6 = 3.838887, 8.249555, 18.658820, 23.078558, 36.238392, 40.115892. The two levels differ by at most 2 × 10^-6 over the first 40.
   - **O(3,3,12):** λ_1..λ_6 = 3.499847, 11.569825, 14.938686, 24.118238, 37.822226, 40.423926. The two levels differ by at most 3 × 10^-3 over the first 40, because eigenfunctions concentrate near the order-12 vertex.
   - **O(2,3,7):** λ_1 = 44.88835, matching "44.89" (p. 18).
   - **O(2,3,4096):** computed separately in geodesic polar coordinates about the order-m vertex. λ_1 = 0.47275, matching "0.473". λ_1..λ_6 all lie below the bounds of Prop. 8.3. The rescaled values h_m²(λ_j − 1/4)/π² are 1.16, 4.51, 9.91, 17.30, 26.67, 38.00, consistent with Fig. 3(b).

8. **Trace-formula consistency (independent check of Theorem 2.1 and of G_σ).** I computed G_σ(t) by quadrature, cross-checked against mpmath to 10^-15. At t = 0.1, with Z the heat trace of my computed spectrum:

   | orbifold | Z_computed(t) − G_σ(t) | prediction from two systolic classes ℓ g_t(ℓ)/(2 sinh(ℓ/2)) |
   |---|---|---|
   | O(2,8,8) | 4.194 × 10^-6 | 4.200 × 10^-6 |
   | O(3,3,12) | 2.587 × 10^-4 | 2.593 × 10^-4 |

   Both differences are consistent with exactly two conjugacy classes at the systole. The remaining discrepancy has the sign and size expected from the finite-element upper bounds. So G_σ, the geodesic term and my spectra are mutually consistent. The authors could use this check themselves.

9. **Theorem 7.1 applied to my spectra.** S is the six signatures of area π/2. I used ℓ = the systole values above, Δ = twice the longest side, ε_j = 10^-6, and t on a geometric grid from 0.002 to 1.

   | orbifold | "exactly one σ passes" (first criterion) | "E_N < half the nearest gap" (second criterion) | paper's N_apr |
   |---|---|---|---|
   | O(2,8,8) | N = 17–18, t ≈ 0.054 | N = 20, window for N = 21 is t ∈ [0.048, 0.057] | 21 |
   | O(3,3,12) | N = 25, t ≈ 0.039 | N = 29 | 39 |

   - O(2,8,8): the N = 21 window matches the shaded band of Fig. 1, and with Δ between 4.3 and 5.5 the count ranges over 17–21.
   - O(3,3,12): I could not obtain 39 with any reasonable choice of Δ (4.3–5.5) or ℓ (down to 1.75); the counts range over 25–35. The paper's number is conservative relative to mine, so this is not a correctness problem, but it cannot be reproduced from the text (M3).
   - The bound H(t) is extremely pessimistic. At t = 0.1, H = 108 against a true Hyp(0.1) = 4 × 10^-6, because of the factor e^{3Δ}. This, not the eigenvalue accuracy, is what forces t ≲ 0.05.

10. **Sensitivity to ε_j and to completeness (the key numerical finding).**
    - **ε_j.** With ε_j = r·λ̃_j, the test still succeeds up to r = 3 × 10^-4 (O(2,8,8)) and r = 10^-4 (O(3,3,12)). It fails entirely at r = 10^-3. The perturbation term tΣε_j dominates first.
    - **One eigenvalue deleted (ε_j = 10^-6).** The test "succeeds" with a wrong signature:

      | orbifold | eigenvalue deleted | "certified" signature |
      |---|---|---|
      | O(3,3,12) | λ_1 | (0;2,2,2,4) |
      | O(3,3,12) | λ_3 | (0;2,2,2,4) |
      | O(3,3,12) | λ_5 | (0;3,4,6) |
      | O(2,8,8) | λ_1 | (0;2,2,2,4) |
      | O(2,8,8) | λ_3 | (0;3,4,6) |
      | O(2,8,8) | λ_5 | (0;3,3,12) |

    - **One spurious eigenvalue inserted** (at 5 or at 30): (0;2,6,12) is "certified" in both cases.

11. **Prop. 8.5.** In the Klein model, Q_{k,b} is the Euclidean rectangle [−tanh b, tanh b] × [−tanh a, tanh a]. I computed λ_1, λ_2, λ_3 of O_{k,b} for k = 3, 4 and b ∈ {0.05, 0.15, 0.3, 0.6}. All lie below the stated bounds; the bound for λ_1 is within a factor of about 2–3.

**Conclusion on correctness.**
- **Theorem 7.1 is correct as a conditional theorem.** I checked its proof: the tail bound via Prop. 5.2, Z_O(s) ≤ A/4πs + β + H(s), the Lipschitz perturbation, and the logic of the two criteria.
- **Tables 1–2 are correct** (one rounding).
- **Figures 1 and 3 are consistent with independent computation.**
- **What is not established is that the computed spectra satisfy the hypotheses of Theorem 7.1.**

## MAJOR issues

**M1. "Certify / certified / certificate" overstates what the computations establish (Abstract p. 1; p. 3; Section 7 pp. 14–15; Table 3; Fig. 2 p. 16).**

Theorem 7.1 needs three things:
- (a) Index-wise two-sided bounds |λ̃_j − λ_j(O)| ≤ ε_j for j ≤ N.
- (b) Completeness and correct indexing of the list up to λ̃_N. This enters the tail through λ_N ≥ λ̃_N − ε_N, which is a guaranteed lower bound on the N-th true eigenvalue.
- (c) A lower bound on the systole and an upper bound on the diameter.

What the paper does instead:
- On (a), p. 15 says the spectra "were computed with high-order finite elements and error estimates", while Theorem 1.2 (p. 3) speaks of "error bounds". An a-posteriori estimator (residual, hierarchical, or two-level difference) is not an enclosure. Its reliability constant is unknown or asymptotic, and it is unreliable in the pre-asymptotic regime λh² ≳ 1, which is exactly where the eigenvalues of index ~700 near λ ≈ 2500 used for O_ϑ lie.
- On (b), "complete below 1.6 × 10^4" and "complete up to λ ≈ 2440–2560" are asserted with no method. The counts agree with Weyl's law (Aλ/4π ≈ λ/8 gives about 2000; λ/3 gives about 815–856), but that is not a proof.

Item 10 above shows why (b) matters: a single missing or spurious eigenvalue produces a confident, unique, wrong "certified" signature. The test has no internal way to detect this.

As written, Theorem 7.1 is a theorem. Its application yields "the test passes on numerically computed data whose error estimates are believed to be bounds". That is a numerical observation, not a certificate.

Place-by-place assessment of the certificate vocabulary:

| # | Place | Wording | Status |
|---|---|---|---|
| 1 | Abstract, p. 1 | "an a-posteriori version certifies the signature of a computed spectrum from 21 to 750 eigenvalues in our examples" | **Overstatement.** The hypotheses are unverified, and one of the ten examples fails (p. 15). |
| 2 | Abstract, p. 1 | "ours can be computed and checked" | Justified: it refers to N and δ, which are computable. |
| 3 | p. 3, before Thm 1.2 | "gives a certificate that a computed spectrum can actually pass" | Conditional statement worded as unconditional. Acceptable only if "certificate" is defined as a conditional test. |
| 4 | Thm 1.2 (title and statement), p. 3 | "A-posteriori certificate", "with error bounds ε_j" | **Theorem** (conditional). Justified; but "of area A" for S is missing (see m2). |
| 5 | p. 3 | "the certificate succeeds with 21 to 750 eigenvalues" (for O(2,8,8), O(3,3,12) and eight (0;3,3,3,3) orbifolds) | **Overstatement**, twice: the inputs are estimates, and the systole-0.694 member fails. |
| 6 | p. 4, Organisation | "Section 7 the certificate" | Neutral. |
| 7 | Section 7 title; Thm 7.1 title, pp. 14–15 | "An a-posteriori certificate" | **Theorem** (conditional). Justified. |
| 8 | p. 15 | "We applied the certificate to the computed spectra …" | Conditional application with unverified hypotheses (a)–(c). Should read "applied the criterion of Theorem 7.1, with the estimated errors in place of ε_j". |
| 9 | p. 15 | N_apr "the least N for which the certificate succeeds" | Numerical experiment. Acceptable once the criterion and inputs are stated (m3, M3). |
| 10 | p. 15 | "the margin the certificate needs" | Neutral. |
| 11 | p. 15 | "the certificate would need t ≤ 0.003 … a limit of the data, not of the method" | Unsupported claim (m6). |
| 12 | p. 15 | "The certificate needs between 10^2 and 10^11 times fewer eigenvalues than the a-priori count" | Compares a conditional test on estimated data with a theorem. Acceptable as an observation if relabelled. |
| 13 | Fig. 2 caption, p. 16 | "observed and certified" | **Overstatement.** Nothing in Fig. 2 is certified. |
| 14 | Fig. 2 caption, p. 16 | "The certificate needs 10^2 to 10^11 times fewer eigenvalues" | As item 12. |

**M2. The systole input is not shown to be a lower bound (Section 7, p. 15; Table 2 "ε = 1.8626, 2.634, 0.694"; Fig. 1 "with the true systole").**
- Theorem 7.1 needs ℓ ≤ ℓ(O), and H is decreasing in ℓ, so an overestimate is unsafe.
- The paper never says how the systoles 1.8626, 2.634, …, 0.694 were obtained. If, as I did, they come from enumerating group elements or words up to some length, the minimum found is an upper bound for the systole, not a lower bound.
- My enumeration reproduces 1.86260 for O(3,3,12), which suggests this is what was done.
- For O(2,3,m) the paper does prove a lower bound (Prop. 8.2, via Jørgensen). It needs the same rigour for the orbifolds of Section 7.
- The family O_ϑ is never defined: ϑ ∈ [0, 2.8] is not explained anywhere (p. 15). Its systoles, diameters ("at most 7.8", Table 1 caption) and spectra therefore cannot be checked.

**M3. The numerical method is not documented, so Section 7 and Table 3 cannot be reproduced from the paper (pp. 15, 18, 20).**

The only information is "high-order finite elements and error estimates", NGSolve and ARPACK. A journal paper must state:
- Which model of H² was used, and how the geodesic sides were represented. This is exact in the Klein model, curved in the disc model, and affects whether FE values are upper bounds.
- The polynomial degree, the meshes (grading near small-angle vertices, essential for O(3,3,12), O(2,3,m) and pinched O_ϑ), the quadrature for the variable coefficients, and the solver tolerances.
- Which estimator was used and the resulting ε_j. At minimum, a table of λ̃_j and ε_j for j ≤ 40 for the two triangle orbifolds.
- How completeness and multiplicities were checked. ARPACK can miss members of clusters or multiple eigenvalues; the ϑ = 0 member with extra symmetry is a candidate.
- The inputs ℓ, Δ, the t-grid and the s-minimisation used in E_N.
- Which of the two criteria of Theorem 7.1 defines N_apr (see m3).

With my independent spectra:
- O(2,8,8): N_apr = 17–21 depending on the criterion and Δ, consistent with 21.
- O(3,3,12): N_apr = 25–35, never 39.

I cannot tell whether the difference comes from inputs, criterion, or the authors' eigenvalue list. Table 3 should be reproducible from the paper plus a short data table, not only from the repository.

## MINOR issues

**m1. Table 2, row 2 (p. 13).** t_1 = 6.849 × 10^-9 rounds to 6.8 × 10^-9, not 6.9 × 10^-9. All other entries of Tables 1 and 2 reproduce.

**m2. Theorem 1.2 (p. 3) vs Theorem 7.1 (p. 14).**
- Theorem 7.1 assumes S consists of signatures of area A; Theorem 1.2 omits "of area A".
- Both theorems presuppose exact knowledge of the area and an order bound M. So the test discriminates only among signatures of a known area. In all the examples the signature is known by construction, so they are demonstrations. Say so.

**m3. Definition of N_apr (p. 15).** "The least N for which the certificate succeeds" does not say which criterion is used. On my data:
- The first criterion of Theorem 7.1 (exactly one σ passes) gives 17–18 for O(2,8,8).
- The second criterion (E_N < half the nearest gap) gives 20–21, and the paper's 21 and the shaded window of Fig. 1 match it.

State which one is used. The first is the actual theorem and gives smaller N.

**m4. Definition of N_obs (p. 15).** "Up to the end of the complete range, the data lie within half the nearest gap" does not specify the t at which this is judged, nor whether Hyp(t) is subtracted.
- On my reading (some t in the grid), N_obs = 1 for both triangle orbifolds, not 3 and 4.
- N_obs uses knowledge of the true σ and ignores the unknown geodesic term, so it is not a decision rule.

Define it precisely, or drop it.

**m5. The failed example (Abstract p. 1; p. 3; p. 15).** The systole-0.694 member fails. The abstract and p. 3 should say "in nine of ten examples".

**m6. "Limit of the data, not of the method" (p. 15).** Support it with an estimate. For example, at t ≈ 0.003 the tail requires λ̃_N t ≳ 15–20, so by Weyl's law N of order 1500–2000, i.e. about twice the computed range. Better still, run it.

**m7. Problem 1 paragraph (p. 20).** "N of Theorem 6.2 grows like ε^-3 log(1/ε)" is stated there as a fact. On p. 14 it is correctly labelled an observation on the formulas. Make the two consistent. My check: the ratio per halving is 8.7–9.0.

**m8. Fig. 3 numerics (p. 18).** Agreement of two mesh levels "to at least 2.3 × 10^-10 relative" is not an error bound.
- What holds rigorously is that conforming FE with exact geometry and quadrature gives upper bounds. That suffices for "every eigenvalue lies below its bound", but not for "decreases in m".
- Say which model and mesh grading were used for m up to 4096. The order-m vertex has angle π/4096 and the triangle has length h_m ≈ 7.17.
- My values λ_1(7) = 44.88835 and λ_1(4096) = 0.47275 agree with the paper.

**m9. Evaluation of G_σ and E_N.** State how the integrals in G_σ(t) were evaluated and to what accuracy. My trapezoid evaluation agrees with mpmath to 10^-15, and the decision margins are about 10^-3, so this is harmless. But a certificate should either use interval arithmetic or state the bound.

**m10. Diameter (p. 15).** "Twice the longest side bounds the diameter" deserves its one-line proof: any point of either copy is within the longest side of a common vertex. Give the computation behind "at most 7.8" for O_ϑ.

**m11. Multiplicities (p. 15).** Theorem 7.1 counts with multiplicity. Say whether any O_ϑ has multiple eigenvalues (for example from extra symmetry at ϑ = 0), and how the solver was prevented from missing a copy.

## Presentation (figures and captions included)

**Fig. 1 (p. 14).**
- There is no legend. The five grey curves are not identified except "the darkest".
- The criterion is "half the nearest gap exceeds both errors", but full gaps are plotted. Plot half-gaps, or 2× the errors, so the shaded window can be read off.
- The shaded window agrees with my computation (t ∈ [0.048, 0.057] for N = 21).

**Fig. 2 (p. 16).**
- There is no legend. The marker shapes (circle/diamond/square) and fill (M = 3 open, M = 12 filled) are explained only in the text.
- The two coloured markers are not identified in the caption. From my systole computation, orange (1.86) is O(3,3,12) and teal (2.26) is O(2,8,8).
- The caption's "certified" should go (M1).
- The squares for the triangle orbifolds are the a-priori N for ε = 1.8626, the smaller systole, plotted at each orbifold's own systole. This is harmless because t_1 binds for M = 12, but say so.

**Fig. 3 (p. 19).**
- The "line 1/4" mentioned on p. 18 coincides with the lower frame of panel (a) and is effectively invisible.
- The dashed bounds are not matched to j. The order is clear, but say so in the caption.
- Panel (b) is clear and agrees with my values.

**Tables.**
- Table 3 would benefit from columns for ℓ, Δ, the t at success and max ε_j.
- Table 2 is fine.

**Text.**
- Section 7 should include a short "Numerical methods" subsection (M3).
- ϑ must be defined (M2).

## Recommendation

**Major revision.** Confidence: high on the numerical points (I recomputed or independently computed every number I comment on); moderate on the paper overall, as Sections 3–4 and 8.1 were outside my charge and I checked them only where they feed the numerics.

The mathematics I checked is correct and carefully done. Tables 1–2 reproduce, and my own spectra and the trace formula agree. The conditional Theorem 7.1 is a correct and useful result. The blocking issue is that the numerical part claims certification that the computations do not provide, together with insufficient documentation to reproduce Table 3.

## What resolves each issue

**M1.** Either of the following:
- (a) **Make the certificate real.**
  - Lower bounds: compute guaranteed index-wise lower bounds, either by Liu–Oishi / Carstensen–Gedicke nonconforming (Crouzeix–Raviart) bounds λ_j ≥ λ_j^CR/(1 + C_h²λ_j^CR), adapted to the variable-coefficient Klein-model form (Liu's 2015 framework covers this), or by Lehmann–Goerisch / Behnke–Goerisch with a CR lower bound for λ_{N+1} as the a-priori shift.
  - Upper bounds: take them from the conforming high-order computation with exact geometry, and verify the discrete counts by Sylvester inertia (LDLᵀ of K − σM).
  - Arithmetic: use interval arithmetic or explicitly bounded rounding.
  - The required accuracy is modest (relative 10^-4 suffices for the triangle orbifolds, item 10), so this is feasible at least for O(2,8,8) and O(3,3,12).
- (b) **Recast the claims.** Keep Theorem 7.1 as the theorem. Rename the numerical outcome (e.g. "a-posteriori criterion" / "the criterion is met with the estimated errors"). Rewrite items 1, 3, 5, 8, 12, 13 and 14 of the table in M1 conditionally. Remove "certified" from Fig. 2. State explicitly that the error bars are estimates, and that a missing or spurious eigenvalue can make the test pass for a wrong signature.

**M2.**
- Give rigorous systole lower bounds. For example: by the argument of Lemma 2.2, every class of length ≤ L has a representative moving a base point at most L + 2Δ. Enumerating all orbit points or tiles in that ball, with interval arithmetic, gives a certified length spectrum below L.
- Or prove lower bounds as in Prop. 8.2.
- Define O_ϑ and ϑ, and give its diameter bound.

**M3.**
- Add a numerical-methods subsection with the information listed in M3.
- Add a table of λ̃_j and ε_j (j ≤ 40) for the two triangle orbifolds, and the inputs ℓ, Δ, the t-grid and the criterion.
- Reconcile N_apr = 39 for O(3,3,12) with an independent computation (mine gives 25–35).

**m1.** Correct 6.9 → 6.8 × 10^-9, or explain the rounding.

**m2.** Add "of area A" to Theorem 1.2, and say that the examples are demonstrations with a known signature.

**m3.** State which criterion of Theorem 7.1 defines N_apr; preferably report both.

**m4.** Define N_obs precisely (which t, whether Hyp is subtracted), or remove it.

**m5.** "Nine of ten examples" in the abstract and on p. 3.

**m6.** Add the Weyl-law estimate, or compute the missing range.

**m7.** Label the ε^-3 log(1/ε) growth on p. 20 as an observation.

**m8.** State the method for Fig. 3; replace "agree to 2.3 × 10^-10" with what it is (a convergence indicator); keep "decreases in m" as an observation.

**m9.** State the quadrature accuracy for G_σ and E_N, or use validated quadrature.

**m10.** Add the one-line diameter argument and the O_ϑ computation.

**m11.** State how multiplicities were handled.

**Presentation.** Add legends to Figs. 1–2. Plot half-gaps in Fig. 1. Identify the colours and markers in the Fig. 2 caption. Make the 1/4 line in Fig. 3(a) visible.
