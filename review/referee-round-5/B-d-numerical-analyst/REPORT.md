<!-- Saved verbatim by the main session from the final message of reviewer B-d: the harness refused the reviewer's own write. Text from the report's first heading on; the reviewer's preceding cover note was dropped. -->
# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (Annals of Global Analysis and Geometry)

Referee profile: validated numerics (interval arithmetic, guaranteed eigenvalue bounds for elliptic operators, reproducibility of computer-assisted claims). My remit is Section 7 (the a-posteriori test, its numerical methods, Tables 4 to 6, Figures 1 and 2) and every other place where the paper relies on computed numbers (Tables 2 and 3, Section 6, Section 8.1 and Figure 3). I read the rendered pages, not only the extracted text. The only material I used was the PDF. All my computations are independent re-implementations from the formulas printed in the paper. I did not see the authors' code.

## Summary

The paper proves that, among closed orientable hyperbolic 2-orbifolds of area at most A, systole at least ε and cone orders at most M, the first N eigenvalues, each known to within δ, determine the signature. N and δ are explicit (Theorem 6.2). The proof runs through the Selberg trace formula for the heat kernel. The signature part G_σ(t) is separated from its competitors at a small time using an integrality lemma for the first differing heat invariant (Lemma 3.3) and enveloping remainders. The geodesic part is controlled by a diameter bound (Theorem 4.4), and the eigenvalues beyond the N-th by a counting bound (Proposition 5.2).

The same mechanism, run on data at one time, gives an a-posteriori test (Theorem 7.1). The test is applied to computed spectra of O(2,8,8), O(3,3,12) and eight orbifolds of signature (0;3,3,3,3). The criterion holds with 18 to 847 eigenvalues, against 4×10^4 to 7×10^12 from Theorem 6.2. The paper says plainly that the eigenvalue errors and completeness are estimated and not proved, and that the systole is computed in floating point. Section 8 shows that the order bound cannot be dropped (O(2,3,m)) and leaves open whether the systole bound can be (Problem 1).

## Significance

From the validated-numerics side, the useful contribution is Theorem 7.1. It is a short, correct and checkable test that turns a finite, approximately known spectrum into a decision among finitely many signatures, with every input named. Its structure suits computer-assisted proof well.
- The bound |Σ_{j<N} e^{-λ̃_j t} − G_{σ(O)}(t)| ≤ E_N(t) holds for every t at once. So choosing the time after seeing the data is legitimate; there is no hidden multiple-testing problem.
- As I show below, it is very forgiving of eigenvalue error. The load-bearing inputs are completeness and a lower bound for λ_N, which are exactly what modern guaranteed-bound methods supply.

Theorem 6.2 is valuable as an existence statement with explicit, if huge, constants. Its numbers (Table 3) reproduce exactly.

What is good, plainly:
- The paper is unusually honest about the status of its numerics: abstract, p. 4, items (i)–(v) on p. 14, and the sentence "what the computations below establish is that the criterion ... holds with the estimated errors".
- Every printed constant I could recompute is correct.
- The test itself is correctly derived from the cited bounds.

## Correctness and what was recomputed

All of this was done in a Python virtual environment (mpmath at 60 digits for the constants; SciPy adaptive quadrature in double precision for G_σ, cross-checked against mpmath at 30 digits). Scripts are in my scratch folder.

1. **Signature term G_σ(t) (Thm 2.1).** I implemented I(t) and E_m(t) independently.
   - Agreement with 30-digit mpmath: about 1e-16 at t = 0.0565.
   - E_m(0+) = b_0(m) = (m²−1)/(12m) for m = 2, 3, 8, 12.
   - The small-t limit of (G_{(0;2,8,8)} − G_{(0;3,3,12)})/t tends to 25/12 (2.0760 at t = 1e-4). This confirms d_3 = 25/12 (p. 13) and, through Lemma 3.3, a_1 = 1/360 and P_3 = 1032 versus 1782.
   - d_2 = −1/12 for (0;4,4,4) against (0;3,4,6) (p. 8) also checks.

2. **Heat invariants and enveloping remainders (Sec. 2.2, Prop. 2.3).**
   - I computed φ_k(m) by power-series inversion, then p_l, b_l, α_k and a_l. α_0..α_4 = 1, −1/3, 1/15, −4/315, 1/315; a_0, a_1, a_2 = 1/12, 1/360, 1/2520.
   - Spot check of Prop. 2.3: for m ∈ {3, 8, 12}, t ∈ {1e-3, 1e-2, 0.05} and K = 0..3, the remainder of E_m has sign (−1)^K and modulus at most |b_K(m)| t^K. The same holds for the area term (I up to double-precision roundoff at t = 1e-3, K = 3).

3. **Signature sets S.**
   - Area π/2, orders ≤ 12: (0;2,2,2,4), (0;2,6,12), (0;2,8,8), (0;3,3,12), (0;3,4,6), (0;4,4,4), so |S| = 6.
   - Area 4π/3: |S| = 3 for M = 3 and |S| = 10 for M = 12.
   - These agree with Table 6. For the family every competitor differs from (0;3,3,3,3) already at c_2, so no precision problem arises at small t.

4. **Table 2 (D(A,ε,M), Thm 4.4).** All twelve entries reproduce (56.6, 1125, 6.37e5; 150.9, 3001, 1.70e6; 640, 3184, 1.70e6; 1132, 2.25e4, 1.27e7). The closed-form upper bound in Thm 4.4 dominates in every case.

5. **Table 3 (Thm 6.2).** All eight rows reproduce to the printed digits: k_*, D, t_1, t_3, Γ_*, Λ, N, δ and the binding constraint. In every row Λt_* ≥ 1, as the proof requires. I also checked the derivation of y_0, t_3, the 3/8 margin and the tail and perturbation bookkeeping in the proof of Thm 6.2; I find them correct.

6. **Table 6, last column (N of Thm 6.2 for the ten examples).** All values reproduce: 6.82e9 (both triangles), and for the family 4.32e4, 4.32e4, 4.49e4, 6.79e4, 1.03e5, 1.57e5, 2.41e5, 3.69e5 (M = 3) and 7.44e12 (M = 12).

7. **Table 4 inputs.**
   - Systoles: my own word enumeration in the triangle groups gives ℓ(O(2,8,8)) = 2.2567679, ℓ(O(3,3,12)) = 1.8626041 and ℓ(O(2,3,7)) = 0.98399 (the last also matches p. 20). The family closed form 4b = 4 arsinh(√(e^{−ϑ}/2)) gives 2.6339158, 2.2026953, 1.8313027, 1.5157379, 1.2504285, 1.0291288, 0.8455936, 0.6939946. Every tabulated ℓ is these values rounded down, with margin ≥ 5e-8.
   - 2 diam P: closed-form vertex distances give 4.897, 4.316, 4.585, 4.671, 4.922, 5.314, 5.820, 6.413, 7.069, 7.770. All agree.
   - I checked that the quadrilaterals have angles π/3.

8. **Table 6, rows O(2,8,8) and O(3,3,12): the actual test, from the Table 5 data.** Using λ̃_j and ϵ_j as printed, with β = 77/48 and H from Lemma 2.2 (ℓ and Δ from Table 4), I recompute exactly the least N:
   - O(2,8,8): (C1) at N = 18, holding for t ∈ [0.0536, 0.0597]; (C2) at N = 20, t ∈ [0.0547, 0.0563].
   - O(3,3,12): (C1) at N = 25, t ∈ [0.0377, 0.0449]; (C2) at N = 29.
   - The reported times 0.0565, 0.0556, 0.0412 and 0.0402 lie in these windows. The criteria fail for all smaller N.

9. **Error budget at the reported points.** For O(2,8,8), N = 18, t = 0.0565: H(t) = 7.6e-3, tail = 2.3e-2, perturbation tΣϵ_j = 1.0e-11, E_N = 3.09e-2. The data residuals relative to E_N are 0.04 (true signature), 1.28 (nearest competitor (0;3,3,12)), and 3.4 to 20.6 for the others. O(3,3,12) is similar (nearest ratio 1.68). The perturbation term is nine orders of magnitude below E_N.

10. **Table 6, "estimate" entries (Weyl replacement, Sec. 7.1).** I recomputed the procedure as described (data replaced by G_{σ(O)}, λ̃_N by 4πN/A) on a 700-point t-grid. I get:
    - Triangles, class-level D: 5614 and 8669 (paper 5611 and 8619).
    - Family, M = 12, class-level D: 23488, 35060, 51427, 77923, 117968, 178451, 269741, 414214 (paper 23498 ... 409805).
    - Family, M = 3, class-level D: 850, 1265, 1904, 2914 (actual counts 855, 1269, 1911, 2900); 4431, 6816, 10406, 16121 (paper estimates 4412, 6761, 10384, 15967).
    - Instance Δ: 17, 23, 24/29, 36/43, 57/66, 93/107, 156/177, 264/298, 449/502, 764/848 (paper counts 18, 25, 24/28, 36/43, 58/67, 94/106, 156/177, 265/295, 451/499, 767/847).

    Agreement is within about 2%, which my coarser t-grid accounts for. Section 7.2's derived ratios also hold: "20–50 at M = 3", "10^6" and "10^7–3×10^8"; and Figure 2's "5×10^2 to 3×10^11" (actual range 4.8e2 to 2.6e11).

11. **Section 8 numbers.** σ_* = 0.562064; h_m and the Prop. 8.3 bound at m = 7 (132.7 > 44.89) and m = 4096 (1.017 > 0.473). The rescaled λ_1 at m = 4096 is 16% above 1, consistent with the 6–16% statement on p. 22 and with Figure 3(b).

12. **Sensitivity experiments (new, not in the paper; used in M1–M4).**
    - **Uniform relative eigenvalue errors.** The O(2,8,8) and O(3,3,12) results are unchanged for errors up to 1e-4. At 3e-4 the count for O(2,8,8) rises to 21 and O(3,3,12) fails. At 1e-3 both fail.
    - **One eigenvalue deleted or duplicated (j ∈ {1,2,3,5,8,12}).** In 22 of 24 cases (C1) certifies a wrong signature, usually at a smaller N than the correct count. Examples: O(2,8,8) with λ_1 deleted passes for (0;2,2,2,4) at N = 9; O(3,3,12) with λ_5 deleted passes for (0;3,4,6) at N = 16.
    - **Consistency diagnostic.** With the correct data the true signature satisfies |Σ e^{-λ̃_j t} − G_σ0(t)| ≤ E_N(t) for every N < 40 and every t ∈ [0.01, 0.2] (maximum ratio 0.91). After deleting λ_1 (or λ_5) the ratio rises to 3995 (884) for O(2,8,8) and 349 (95) for O(3,3,12).

**Bottom line on correctness.** Within my remit I found no mathematical error in Theorem 7.1, Theorem 6.2 or the tables. The problems are in what the numerical inputs are said to establish and how; see below.

## MAJOR issues

**M1. The completeness argument is not a bound, and is weaker than stated (p. 15, Sec. 7.1 "Completeness"; Table 4 caption; item (iv) p. 14).**
The text says the computed heat trace "agrees with I + E to 4.7×10^-13 at t = 0.0015, within the error budget of 1.5×10^-11 formed by the ϵ_j and a tail bound from Weyl's law", and concludes "given the budget, no eigenvalue below 1.6×10^4 is missing or spurious". Four problems:

- (a) **Weyl's law is an asymptotic statement, not a tail bound.** The Weyl-type tail (A/4π)e^{-Λt}/t beyond Λ = 2.2×10^4 at t = 0.0015 is 3.9×10^-13. The paper's own rigorous tail (Prop. 5.2 with s = t/2) is 1.1×10^-5, six orders of magnitude above the budget. So the deduction rests on an unproved asymptotic, not only on the error estimates. Item (iv) says the argument is "conditional on the error estimates", but it is also conditional on a heuristic tail.
- (b) **Missing error sources.** The budget omits floating-point summation error and the quadrature error of I + E. The trace is about 83 at t = 0.0015. A worst-case bound for naive summation of about 2850 terms is n·u·Σ|x| ≈ 2.6×10^-11, which exceeds the budget; a typical error is about 1e-13. Compensated or interval summation, or at least an explicit rounding term, is needed.
- (c) **The check only sees net changes.** A single-time scalar check detects only the e^{-λt}-weighted net change in the count. A missing eigenvalue paired with a spurious one nearby is invisible. Overlapping windows with de-duplication at relative 1e-9 (p. 15) are a classic source of exactly such pairs.
- (d) **The family above 9.8×10^3 rests on count agreement.** Agreement of eigenvalue counts across three discretisations that share the same windowed shift-invert pipeline protects against discretisation artefacts, not against solver misses.

This matters because, as my item 12 shows, completeness is by far the most dangerous input: one missing or duplicated eigenvalue makes (C1) certify a wrong signature, typically at a smaller N than the true one. A user who increases N until (C1) first holds would then stop at the wrong answer.

**M2. The test lacks a stated internal consistency check, though a free and strong one exists (Thm 7.1, pp. 13–14; Sec. 7.1 "The test"; Table 6).**
If the inputs are valid, the true signature satisfies the inequality of Theorem 7.1 for every N and every t. Hence:
- (C1) can never hold for two different signatures at two different (N,t);
- the true σ must never fail at any (N,t).

The paper reports only the least N at which (C1)/(C2) holds. It does not say whether the claimed σ satisfies the inequality on the whole (N,t) grid, or whether any other σ ever passes. On the Table 5 data this diagnostic is clean: maximum ratio 0.91, and no other signature ever passes. With one eigenvalue removed it is violated by factors of 10^2 to 4×10^3 (item 12). So it is a cheap and effective falsification test of the completeness and error inputs. It should be part of the stated procedure, and its outcome should be reported for all ten examples over the complete range.

The maximum ratio of 0.91 also shows that E_N is nearly attained somewhere on the grid. The paper should say where (which N, t) so the reader can judge how tight the budget is.

**M3. Statements about the eigenvalue errors are partly incorrect and insufficiently documented (p. 15, "Discretisation and solver", "Error estimates").**
- (a) **"Conforming elements give upper bounds for the λ_j" is not true for the computation described.** The Rayleigh–Ritz upper bound requires the discrete space to be a subspace of H^1 on the exact domain, with exactly evaluated forms. Here:
  - the elements are "curved to order p", so the meshed domain is a polynomial approximation of the circular-arc boundary, not P itself;
  - the weight w = 4/(1−|z|²)² is integrated by quadrature, not exactly;
  - everything is in floating point.

  These are variational crimes, and none of the computed values is a guaranteed upper bound. The sentence should be corrected; it is also the only place the paper suggests that half of an enclosure is already available.
- (b) **The error estimate is not justified as an estimate for the reported values.** ϵ_j = |λ_j(0.05,10) − λ_j(0.07,12)| compares a finer-h/lower-p level with a coarser-h/higher-p level. Which is the more accurate one is not stated. The difference is used as the error of the (0.05,10) value without argument.
- (c) **The Table 5 estimates sit at solver/round-off level.** Values of about 1.6×10^-13·λ_j are at the level of the eigensolver tolerance and floating-point round-off for p = 10–12 bases, not at discretisation level. A difference that small says little about the discretisation error.
- (d) **No evidence is shown for the convergence claim.** The claimed "observed convergence h^13 to h^19 at p = 10 and geometric in p" has no supporting data (no table, no rates, no ARPACK tolerance, no residual norms).

**M4. Feasibility of a validated result is understated, and the counterfactual on p. 14 is incomplete.**
The paper says "with guaranteed eigenvalue enclosures and a proved completeness, the same computation would decide the signature rigorously". That is not quite enough. A validated version also needs:
- an enclosure of G_σ(t). Theorem 7.1 uses exact G_σ, but the computation uses Gauss–Legendre quadrature with a floating-point check (see m3);
- a certified systole lower bound (currently 40/50-digit floating point);
- outward rounding in E_N.

My sensitivity results (item 12) show the remaining gap to a computer-assisted proof is small for the two triangle orbifolds. For N ≤ 29 one needs:
- enclosures of λ_1..λ_29 of relative width about 1e-4 (the crude perturbation term tΣϵ_j is what limits this; see m4);
- an index-certified lower bound for λ_N good to a few percent;
- Sylvester-inertia completeness;
- a validated G_σ at one t.

All of these are standard:
- **Lower bounds:** guaranteed lower bounds via the Crouzeix–Raviart/Liu–Oishi framework (Liu & Oishi, SIAM J. Numer. Anal. 2013; Liu, Appl. Math. Comput. 2015; Carstensen & Gedicke, Math. Comp. 2014), or Lehmann–Goerisch with Plum's homotopy (Nakao, Plum & Watanabe, *Numerical Verification Methods and Computer-Assisted Proofs for PDEs*, Springer 2019). In the Beltrami–Klein model the hyperbolic triangles and quadrilaterals are exact Euclidean polygons, with a smooth, uniformly elliptic variable-coefficient operator, so polygonal-domain lower-bound methods apply without geometric variational crimes.
- **Completeness:** the shift-invert factorisations already computed per window give, through Sylvester's law of inertia, the exact count of discrete eigenvalues below each shift. Combined with guaranteed lower bounds this certifies completeness by index.
- **G_σ(t):** it is a sum of integrals of explicit analytic functions and can be enclosed by validated quadrature (for example Arb's integration) at one t.
- **Systole:** the enumeration is a finite computation that can be redone in interval arithmetic at negligible cost.

I do not require the certification for acceptance, because the paper is honest that it has not been done. But either:
- (i) certify at least the two triangle cases (the computation is small), or
- (ii) replace the p. 14 sentence by a complete and accurate list of what a validated version needs, with the quantitative tolerances above, so that "the same computation would decide the signature rigorously" is correct as written.

## MINOR issues

- **m1 (Table 6, p. 18, caption).** "> N_c means that the criterion fails for every N up to the N_c eigenvalues". The test at N needs λ̃_N, so with N_c eigenvalues λ_0..λ_{N_c−1} the largest testable N is N_c − 1, as p. 16 itself says ("still fails at N = 4423" with N_c = 4424). The entries should read "≥ N_c" (or "> N_c − 1").
- **m2 (Table 3, p. 12, row 1, and text p. 12).** Row 1 has M = 8 with ε = 1.8626, "that of O(3,3,12) ... so that the class contains both". But C(π/2, 1.8626, 8) does not contain O(3,3,12), which has order 12. Explain the purpose of the M = 8 row or change it.
- **m3 (p. 16, "The test").** "Checked against 30-digit quadrature (worst difference 2.1×10^-15)". Say whether this is absolute or relative, and over which t. G_σ(10^-5) ≈ 1.25×10^4, so an absolute 2.1×10^-15 is below double-precision resolution there. Theorem 7.1 is stated for exact G_σ, so the evaluation error should appear in the inequality, even if it is negligible against the margin (about 8.7×10^-3 absolute for O(2,8,8)).
- **m4 (Thm 7.1, p. 14; proof of Thm 6.2, p. 12).** The perturbation bound |e^{-at} − e^{-bt}| ≤ t|a−b| discards a factor e^{-t·min(a,b)}. Using |e^{-at} − e^{-bt}| ≤ t·e^{-t·min(a,b)}·|a−b|, each term contributes at most t·e^{-t(λ̃_j−ϵ_j)}·ϵ_j. That improves the test's tolerance to eigenvalue errors by roughly e^{λt} for the upper eigenvalues (about e^7 at the reported points). This matters for any validated version (M4), where enclosures are wider than the present estimates. Similarly, the tail could use Z_O(s) − Σ_{j<N} e^{-λ_j s} instead of Z_O(s).
- **m5 (Table 4 caption and item (ii), pp. 14–15).** "the lower bound ℓ for the systole" should be qualified in the caption as computed in floating point (not certified), as the text does. My double-precision enumeration reproduces all ten values, so I have no doubt about them, but the caption should not call them bounds without qualification.
- **m6 (Sec. 7.1, "Systoles and diameters", p. 16).** The computed diameter equals diam P in all ten cases, while the test uses 2 diam P, and H depends on Δ through e^{3Δ}. With Δ = diam P instead of 2 diam P, H(0.0565) for O(2,8,8) drops from 7.6×10^-3 to 4.9×10^-6. If diam O = diam P can be proved for doubles of these polygons, or any sharper proved bound found, the counts would drop and the comparison in Section 7.2 ("most of the gap ... is knowledge of the geometry") would sharpen. At minimum, state that the factor 2 is not believed sharp.
- **m7 (Sec. 7.1, last paragraph, p. 16).** "Every reported count is confirmed with the infimum computed by Brent's method." Brent finds a local minimiser. Validity comes from the fact that any s gives an upper bound, so the grid value is already valid. Say that the reported counts use the valid upper bound and that Brent only confirms that the count does not change.
- **m8 (Sec. 7.1, p. 16, ϑ = 1.6, M = 3).** The Weyl-replacement estimate is sensitive to the t-grid at the 1% level. My 700-point grid gives 4431, outside the complete range, against the paper's 4412. The statement "the estimate is low by at least 0.3%" therefore depends on the grid. State the grid used for the estimates and treat them as having about 1% resolution.
- **m9 (Sec. 7.1, "Completeness" for the family, pp. 15–16).** "We use those below 0.8 times the least sector maximum" is a heuristic cut-off. State what it guards against (loss of accuracy at the top of each sector's computed range), and report Sylvester-inertia counts at the cut-offs if available (see M1, M4).
- **m10 (Sec. 8.1, p. 22, Figure 3).** For λ_1..λ_6 of O(2,3,m) up to m = 4096, nothing is said about completeness: a missing low eigenvalue would relabel the curves. Nor is anything said about how a triangle with angle π/4096 is meshed ("uniform hyperbolic size h" near a vertex of angle 7.7×10^-4 implies extreme element aspect ratios unless graded). Since Figure 3 is illustrative and the paper says "an observation, not proved here", one sentence on each point suffices.
- **m11 (p. 20).** A repository script path ("theory/eigen/systole 233.py") appears in the mathematical text. Cite the archived deposit (Data availability) instead of a development path in the body.
- **m12 (p. 15, "Error estimates").** ϵ_j has the floor 10^-14·max(λ_j, 1). State how ARPACK convergence was set and verified (tolerance, residual norms ‖Ku − λMu‖ relative to ‖M‖), since at the 1e-13 level the solver, not the discretisation, sets the difference.

## Presentation (figures, captions, notation, exposition)

- **Figure 1 (p. 13).**
  - There is no legend. The two dotted curves are not identified as N = 21 and N = 100 in the figure, only through the order of words in the text. The dashed curve's diameter bound is not stated ("a diameter bound": which one?).
  - The y-axis label is |G_σ0(t) − G_σ(t)|, but the error curves are plotted on the same axis.
  - I measured the shaded N = 21 window on a 400-dpi render as t ∈ [0.050, 0.056]. My recomputation with the stated criterion (half the nearest gap exceeds H + tail + perturbation, ℓ = 2.256767, Δ = 4.897, Table 5 data) gives [0.048, 0.059]. For N = 20 it gives [0.0547, 0.0563]. The drawn window lies between the two, so state the indexing convention behind "N = 21" (eigenvalues λ_0..λ_20 with tail from λ̃_21, or otherwise) and check the shading.
- **Figure 2 (p. 19).**
  - There is no legend in the figure. The marker code (open/filled = M = 3/12; diamonds/squares/circles; colours for the triangles; horizontal offsets) is given only in the text on p. 17, not in the caption. Put it in the caption or a legend.
  - The class-level-diameter counts of Table 6 (fourth numeric column), which the text uses to separate the two effects, are not plotted.
- **Table 6 (p. 18).**
  - The column header "(C1), D(A,ℓ,M)" mixes actual counts (M = 3 rows) with "> N_c; estimate" entries. Typographically distinguishing estimates (for example italics) would prevent misreading them as counts.
  - In the triangle rows, state that the class-level D is for M = 12 (1125.4).
- **Table 4 (p. 15).** λ_c for the triangles is 16000, while the text derives completeness below 1.66×10^4 and then uses 1.6×10^4. This is consistent, but say once which number is the cut-off.
- **Theorem 1.2 (p. 3) versus Theorem 7.1.** Theorem 1.2 states only (C1). Since the test also reports (C2) and Table 6 lists both, mention (C2) in Theorem 1.2 or point to it.
- **Notation.** ϵ_j (eigenvalue errors) and ε (systole bound) are visually close in the rendered PDF, and both appear in Section 7. Consider δ_j or e_j for the eigenvalue errors. "N" is also used for Neumann in Table 5; harmless, but "Neu"/"Dir" would be clearer.
- **Exposition of what is certified.** The honesty is commendable. I suggest a short table near the start of Section 7 listing, for each of the five inputs and for G_σ and E_N, its status in this paper: exact / proved / floating point at k digits / estimated / heuristic (Weyl tail). Readers in validated numerics will look for exactly this.

## Recommendation

**Major revision** (within my remit). Confidence: high on the recomputed items (all tables in and feeding Section 7 reproduce), and medium-high overall for the numerical part.

The theorems I checked are correct, and the numbers reproduce. The reasons for "major" are:
- (M1) the completeness argument presented as a deduction uses a heuristic Weyl tail and omits rounding;
- (M2) the absence of the free consistency check that would guard against the most dangerous failure mode;
- (M3) an incorrect statement that the FEM values are upper bounds, plus an undocumented error estimate;
- (M4) the claim of what a rigorous version requires is incomplete.

None of these affects Theorems 1.1, 1.3 or 6.2. M2 and most of M1/M3 are fixable with modest work. Certifying the two triangle cases would turn Section 7 into a genuine computer-assisted result at small cost, and I encourage it.

## What resolves each issue

- **M1:**
  - Replace the Weyl tail by a proved bound (Prop. 5.2 at a smaller t, or a larger computed range), or label it explicitly as heuristic in Sec. 7.1, item (iv) and the Table 4 caption.
  - Add floating-point summation and quadrature error terms to the budget, or use compensated or interval summation.
  - Add Sylvester-inertia counts at window endpoints (available from the existing factorisations) as the primary completeness evidence, with the trace check as a secondary check.
  - Reword "no eigenvalue below 1.6×10^4 is missing or spurious" to state exactly what is assumed.
- **M2:**
  - State the consistency check as part of the procedure: the claimed σ satisfies the inequality of Thm 7.1 for every N and t on the grid within the complete range, and no other σ ever passes (C1).
  - Report the maximal ratio |Σ e^{-λ̃_j t} − G_σ0(t)|/E_N(t) and where it is attained, for all ten examples.
- **M3:**
  - Correct the "upper bounds" sentence (variational crimes: curved elements, quadrature of w, floating point).
  - State which discretisation is the reference and why the difference estimates the error of λ_j(0.05,10).
  - Give a short convergence table (h and p sequences, observed rates) and the eigensolver tolerance and residuals.
- **M4:** Either certify the two triangle orbifolds, or replace the p. 14 counterfactual by the complete list of required ingredients with the tolerances quantified in item 12. Certification means guaranteed lower bounds with index (Liu-type or Lehmann–Goerisch), Rayleigh–Ritz upper bounds with outward rounding, inertia counts, a validated G_σ at one t, and an interval systole.
- **m1:** Change "> N_c" to "≥ N_c" (or "> N_c − 1").
- **m2:** Justify or change the M = 8 row of Table 3.
- **m3:** State whether the 2.1e-15 is absolute or relative, and add the G_σ evaluation error to E_N.
- **m4:** Optionally adopt the sharper perturbation and tail bounds; this becomes necessary if a validated version is attempted.
- **m5:** Qualify "lower bound" in the Table 4 caption.
- **m6:** Comment on, or prove, a sharper instance diameter bound.
- **m7:** Clarify the role of Brent's method.
- **m8:** State the t-grid used for the estimates and their resolution.
- **m9:** Justify the 0.8 cut-off, or replace it by inertia counts.
- **m10:** Add one sentence each on completeness and meshing for Figure 3.
- **m11:** Replace the script path in the body by a reference to the deposit.
- **m12:** Report the eigensolver tolerance and residuals.
- **Presentation:** Add legends to Figures 1 and 2 and fix or explain the Figure 1 shading; mark estimates in Table 6; mention (C2) in Theorem 1.2; consider renaming ϵ_j; add the input-status table.

---

The scripts behind these recomputations (heat.py, consts.py, table3.py, test71.py, sens2.py, sens3.py, consist.py, weyl.py, systole.py) and the page renders are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-5/B-d-numerical-analyst/scratch/.
