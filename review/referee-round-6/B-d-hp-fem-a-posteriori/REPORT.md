<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (Annals of Global Analysis and Geometry)

(Writing REPORT.md was refused, so this message is the complete report. My scripts are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/B-d-hp-fem-a-posteriori/scratch/.)

Referee profile: numerical analysis of a-posteriori error estimation for eigenvalue problems (residual estimators, Kato–Temple and Lehmann bounds, hp-FEM). I cover Section 7 in full (Theorem 7.1, Section 7.1 on numerical methods, Section 7.2 on results, Tables 4–6, Figures 1–2), and the parts of Sections 1 and 6 that describe it (the abstract, Theorem 1.2 and the paragraph after it, Table 3, and the discussion of Figure 1 on p. 14). Page numbers refer to the 29-page PDF. I read the rendered pages for everything I report about figures and tables (pp. 2, 3, 6, 12–20).

## Summary

Section 7 turns the mechanism of Theorem 6.2 into a test on given data, Theorem 7.1. The inputs are approximate eigenvalues λ̃_0..λ̃_N with errors ϵ_j, the exact area, a lower bound for the systole, an upper bound Δ for the diameter, and a finite candidate set S of signatures. The test computes an error budget E_N(t). It is made of three bounds:
- the hyperbolic-term bound H(t) of Lemma 2.2;
- a tail bound e^{-(λ̃_N-ϵ_N)(t-s)} Z(s);
- a perturbation term t Σ ϵ_j.

It then asks whether exactly one σ ∈ S satisfies |Σ_{j<N} e^{-λ̃_j t} − G_σ(t)| ≤ E_N(t) (criterion C1), or the stronger margin criterion C2.

The test is run on ten computed spectra: O(2,8,8), O(3,3,12) and eight members O_ϑ of signature (0;3,3,3,3). The spectra come from H¹-conforming curved hp-FEM (p = 10) in the Poincaré disc, sector by sector, with shift-invert Lanczos in spectral windows. The errors ϵ_j are differences between two discretisations. Completeness is supported by one heat-trace comparison against the true signature, and for the family above λ ≈ 9.8×10³ by agreement of eigenvalue counts.
- **Instance-level diameter bound (2 diam P):** C1 holds with 18 to 847 eigenvalues.
- **Class-level bound D(A,ℓ,M):** C1 holds for four family members at M = 3 (855 to 2900 eigenvalues) and is estimated to need 4.4×10³ to 4.1×10⁵ elsewhere.
- **Theorem 6.2, for comparison:** asks for 4×10⁴ to 7×10¹².

The section is unusually candid. Inputs (i)–(v) on p. 15 state that:
- the errors ϵ_j are estimates, not enclosures;
- completeness is supported but not proved;
- the systole is computed in floating point;
- the examples are demonstrations, not determinations.

The deletion/duplication experiment in (iv) is the most useful single sentence in the section. My objections concern three things:
- a few places where the wording claims more than this candour allows;
- one conclusion in Section 7.2 that the paper's own Table 6 contradicts;
- one figure that does not match its description.

I also argue that completeness, the one input the conclusions actually depend on, gets the weakest support, although stronger and cheap evidence is available inside the authors' own solver.

## Significance

Within the paper, Section 7 plays a supporting role. Theorem 7.1 is a direct a-posteriori version of the proof of Theorem 6.2, built from bounds already in the paper; mathematically it is a corollary. Its value is showing that:
- the a-priori constants of Theorem 6.2 are pessimistic by factors of 5×10² to 3×10¹¹;
- with the instance's geometry, a few dozen to a few hundred eigenvalues suffice.

From a numerical-analysis standpoint the section has no new method:
- the eigenvalue solver and the two-discretisation error estimate are standard;
- the completeness check is that of Strohmaier–Uski, as the authors say.

The section never actually applies Theorem 7.1 as a theorem, because none of its hypotheses about the eigenvalues is verified. What it shows is that the computed spectra are consistent with the trace formula for the stated signature and for no other; the authors say this on p. 19. That is worth showing, but it is a consistency check on known orbifolds. Its significance for an inverse-spectral reader is limited unless at least one instance is made rigorous.

My computations below show that one rigorous instance is within reach.

**Good points:**
- Honest statement of the inputs.
- Full reproducibility: everything I could recompute from the printed data agreed.
- A correct and clean Theorem 7.1.
- Tables 3–6 are internally consistent.

## Correctness and what was recomputed

I worked only from the PDF. I wrote my own code with mpmath and scipy: the heat-kernel trace formula integrals I(t) and E_m(t) of Theorem 2.1, the bounds of Lemma 2.2, and E_N(t) of Theorem 7.1. I used no code or data from the authors.

**1. Proof of Theorem 7.1 (p. 15): correct.**
- I checked each step:
  - the hyperbolic term is at most H(t);
  - the tail bound Σ_{j≥N} e^{-λ_j t} ≤ e^{-λ_N(t-s)} Z_O(s), with λ_N ≥ λ̃_N − ϵ_N;
  - Z_O(s) ≤ A/(4πs) + β + H(s), using I(s) ≤ e^{-s/4}A/(4πs), E_m ≤ b_0(m), and σ(O) ∈ S;
  - the perturbation bound |e^{-at} − e^{-bt}| ≤ t|a−b|;
  - C2 implies C1.
- I also re-derived both bounds of Lemma 2.2 (p. 6), which Theorem 7.1 uses, from the stated count n_O(x) ≤ π e^{x+3 diam}/Area:
  - The first bound needs f(x) = x e^{-x/2-x²/4t} to be decreasing on [ℓ, ∞). This holds for t ≤ ℓ²/(2(1+ℓ)): the logarithmic derivative is at most −3/2 there.
  - x/φ′(x) is decreasing, which gives the factor (1 + 2t/(ℓ−t)).
  - The global bound follows from the two maximisations stated, at x = 2√t and x = 6t.
- Using a lower bound ℓ for the systole in place of the systole is legitimate. On s ≤ ℓ²/(2(1+ℓ)) the bound is decreasing in ℓ (the logarithmic derivative is at most −1/2), and the integration by parts from ℓ instead of the true systole remains valid.

**2. Trace comparison from the printed eigenvalues (Table 5).**
I formed Σ_{j≤40} e^{-λ̃_j t} (with λ̃_0 = 0) and subtracted G_σ(t) for the true signature. Where the truncation tail is negligible (t ≥ 0.08), the difference should equal Hyp(t), which is dominated by the systole classes. I divided it by one primitive-class term ℓ e^{-t/4} e^{-ℓ²/4t} / (√(4πt)·2 sinh(ℓ/2)), using ℓ from Table 4.

| t | O(2,8,8) ratio | O(3,3,12) ratio |
|---|---|---|
| 0.08 | 2.062 | 1.9993 |
| 0.10 | 2.005 | 1.9999 |
| 0.12 | 2.005 | 2.00001 |
| 0.15 | 2.019 | 2.0004 |

The ratio is 2, which corresponds to one geodesic counted in both orientations. This holds to about 10⁻⁵ for O(3,3,12), which pins down its systole value to about 10⁻⁶. The printed eigenvalues, signature and systole are mutually consistent.

At t = 0.1 the true-signature residual is 4×10⁻⁶. The nearest competitor, (0;3,3,12) against (0;2,8,8), is 0.047 away. I also checked c_2 and d_3 = 25/12 against the curves of Fig. 1.

**3. The test itself on the triangle orbifolds (Table 6, rows 1–2).**
I used S = the six signatures of area π/2 with orders ≤ 12, which I enumerated: |S| = 6 and β = 1.6042. I used ℓ and Δ = 2 diam P from Table 4, the ϵ_j from Table 5, 240 log-spaced values of s/t, and 400 times in [0.01, 0.2].

| Orbifold | Criterion | Least N, mine | Window of times, mine | Table 6 |
|---|---|---|---|---|
| O(2,8,8) | C1 | 18 | [0.0534, 0.0597], geometric middle 0.0564 | 18 (0.0565) |
| O(2,8,8) | C2 | 20 | [0.0546, 0.0567] | 20 (0.0556) |
| O(3,3,12) | C1 | 25 | [0.0375, 0.0449] | 25 (0.0412) |
| O(3,3,12) | C2 | 29 | [0.0375, 0.0432] | 29 (0.0402) |

All four entries agree. Adding the print rounding (5×10⁻⁷) to every ϵ_j changes nothing. For every N ≤ 39 and every time on my grid, the true signature satisfies the inequality of Theorem 7.1, and C1 never singles out a wrong signature.

**4. The deletion/duplication claim (p. 15, (iv)).**
I deleted or duplicated each of λ̃_1, λ̃_2, λ̃_3, λ̃_5, λ̃_8, λ̃_12 for both triangle orbifolds and ran the test. C1 concludes a wrong signature in 19 of 24 cases. This is exactly the paper's count, mostly at N = 9–26, below the true counts 18 and 25.

**5. Weyl-law count estimates (p. 18; Table 6, column "est.").** I replaced λ̃_N by 4πN/A and the data by G_σ(O).
- Class-level, triangles: 5603 and 8624 against the printed 5611 and 8619.
- Instance-level, triangles: 17 and 23 against the actual 18 and 25. This is consistent with the claimed accuracy of "within 8% for N < 100".
- Family, with my own S = {(0;3,3,3,3), (0;2,2,2,2,3), (1;3)}, |S| = 3, M = 3:

| Member | Instance-level estimate, mine | Table C1 | Class-level estimate, mine | Table |
|---|---|---|---|---|
| ϑ = 0 | 24 | 24 | 858 | 855 |
| ϑ = 1.2 | 93 | 94 | 2917 | 2900 |
| ϑ = 1.6 | 156 | 156 | 4438 | 4412 |
| ϑ = 2.8 | 764 | 767 | 16249 | 15967 |

  All agree within 2%. My grid has 150 times; a coarser grid can only raise the estimate.

**6. Inputs (Table 4).**
- I recomputed the family systoles as 4b with sinh a sinh b = 1/2 and ϑ = log(sinh a/sinh b). The printed values are correctly rounded down; the margins are at least 2.9×10⁻⁷.
- I recomputed diam P for all ten polygons: the longest side of each triangle, and the vertex diameter of each quadrilateral. Every printed 2 diam P is rounded up, as it should be for an upper bound. Every "diam" agrees.
- I recomputed D(A,ℓ,M) for both M = 3 and M = 12 (150.9, 3001.2, 1125.4); they agree, as does all of Table 2.

**7. Table 3 and the last column of Table 6 (Section 6).**
I recomputed every constant of Theorem 6.2, including φ_k, b_K(M) and α_K. I confirmed the k!-convention in p_l against the numerical expansion of E_3(t). All eight rows of Table 3 agree to the printed digits: D, t_1, t_3, Γ_*, Λ, N, δ, and the binding constraint. All entries of the last column of Table 6 agree, including the M = 3 family values 4.3e4, 4.3e4, 4.5e4, 6.8e4, 1.0e5, 1.6e5, 2.4e5, 3.7e5.

**8. Quoted comparisons.**
- These agree with Table 6:
  - "18 to 847";
  - "855 to 2900";
  - "4.4×10³ to 4.1×10⁵";
  - "4×10⁴ to 7×10¹²";
  - the factors "20–50 at M = 3", "10⁶" and "10⁷–3×10⁸";
  - the Fig. 2 caption "5×10² to 3×10¹¹".
- The completeness threshold "λ < 1.66×10⁴" agrees: e^{-λt} > 1.5×10⁻¹¹ at t = 0.0015 gives λ < 16,613.
- The Weyl tail beyond λ ≈ 2.2×10⁴ at t = 0.0015 is (A/4πt)e^{-Λt} ≈ 3.9×10⁻¹³. This is consistent with the reported agreement of 4.7×10⁻¹³.

**9. Disagreements:** Fig. 1 (m1) and the interpretive sentence in Section 7.2 (M2).

## FATAL

None. Within my coverage, Theorem 7.1 is correct, and every number I could recompute agrees. The paper does not claim that the tests are rigorous determinations.

## MAJOR

**M1. "Decides" overstates what Section 7 establishes (abstract, pp. 1–2; Section 1, p. 3; Section 7.2, p. 18 "the test succeeds"; Fig. 2 caption, p. 20).**
- The abstract says the test "decides four of ten computed spectra" and "decides all ten with 18 to 847".
- Section 7 itself (p. 16) says that what the computations establish is "that the criterion of Theorem 7.1 holds with the estimated errors, for lists assumed complete". Section 1 (p. 3) says these are "demonstrations … not determinations".

Theorem 7.1 decides only when its hypotheses hold: the errors ϵ_j are bounds, and the list is complete. Neither is verified here. Item 4 of the previous section shows that a single missing eigenvalue makes C1 return a wrong signature without any warning. So "decides" is not available.

In addition, "four of ten" refers only to the M = 3 runs. With M = 12, those same four members are not decided at the class level (estimates 2.3×10⁴ to 7.7×10⁴). The abstract does not say this.

**M2. The conclusion "most of the gap … is knowledge of the geometry" (p. 19) is contradicted by Table 6.**
The gap between Theorem 6.2 and the instance-level test has two factors:
- geometry = (class-level count)/(instance-level count);
- data = (Theorem 6.2 count)/(class-level count).

From Table 6:

| Case | Geometry factor | Data factor |
|---|---|---|
| Triangles | 5611/18 ≈ 3×10² and 8619/25 ≈ 3×10² | ≈ 10⁶ |
| Family, M = 12 | ≈ 5×10² to 8×10² | 10⁷ to 3×10⁸ |
| Family, M = 3 | 855/24 ≈ 36 up to 15967/767 ≈ 21 | 23 to 50 |

So, in log terms, the data factor dominates for the triangles and for the family at M = 12, and the two factors are comparable at M = 3. The sentence that follows ("the use of the data saves a further factor of … 10⁶ … 10⁷–3×10⁸") contradicts the one before it.

This matters because it is the paper's interpretation of its own experiment, and it underlies the remark that "an orbifold whose diameter is known is in practice one whose geometry is known."

**M3. Completeness, the input the conclusions depend on, has the weakest support, although stronger evidence is cheap (p. 15 (iv); p. 17 "Completeness"; Table 4).**
I quantified how sensitive the conclusions are to each input (item 4 above and M4(c)):
- the counts are insensitive to the eigenvalue errors by four orders of magnitude (M4);
- they are destroyed by one missing or duplicated eigenvalue.

The deletion experiment shows more than the paper says:
- In the low-index cases (deleting or duplicating λ̃_1 or λ̃_2), the wrong conclusion persists for every N up to 39, at all times. Nothing internal to the test flags it.
- In some higher-index cases, C1 later singles out different signatures at different times. That inconsistency is detectable, and the paper could use it as a diagnostic.

The completeness evidence offered has these weaknesses:
- **(a) It is circular for a determination.** It compares the computed trace only with G for the true signature.
- **(b) It uses one time.** At t = 0.0015 the check is blind to a missing eigenvalue paired with a spurious one nearby, as the paper says.
- **(c) Its tail term is only a Weyl estimate.** It is not a bound.
- **(d) Its budget is not the error term of Theorem 7.1** (see m3).
- **(e) The family evidence is weaker.** For λ > 9.8×10³ it is only that three discretisations give equal counts. For the family the trace test's time and budget are not even stated.
- **(f) The two-window recomputation is a check of the eigensolver only.** It checks the eigensolver against itself.

The remedy is within the authors' existing pipeline. They already compute one sparse factorisation of K − σM per window. An LDLᵀ factorisation gives the inertia, so by Sylvester's law of inertia it gives the exact number of discrete eigenvalues below σ, without extra cost. For a conforming Galerkin discretisation this changes the logical structure of (iv) and (v):
- **Discrete completeness is certified.** The inertia counts at the window boundaries settle it, in floating point, and that error can be controlled.
- **Index matching then holds.** For each index j, the discrete eigenvalue λ_{j,h} is an upper bound for λ_j by the min–max principle, given exact geometry and integration; see M4. A guaranteed lower bound with the same index then gives an enclosure, matched by index, of the continuous j-th eigenvalue.
- **(iv) and (v) merge into one requirement.** Completeness of the continuous list is then not a separate unprovable input: it is implied by index-wise enclosures.
- **Merging sectors is safe.** Merging the Neumann/Dirichlet or four-sector lists preserves index-wise enclosures, since the k-th order statistic is monotone.

This should at least be stated. The inertia counts should be reported.

**M4. The error model is misdescribed, and its role is not quantified (p. 17, "Error estimates"; p. 15 (v); p. 16, "Discretisation and solver").**
- **(a) The upper-bound statement is incomplete.** The paper says that "conforming elements would bound the eigenvalues from above in exact arithmetic with exact integration".
  - That also requires the exact domain.
  - Section 7.1 says the sides are "represented exactly as rational quadratic splines and the elements curved to order p". In standard isoparametric practice, curving elements to order p replaces the exact boundary by a polynomial one.
  - In that case the discrete domain is not P, and the Rayleigh–Ritz upper bound is lost even in exact arithmetic. For the Neumann problem, domain perturbation is not even monotone.
  - The authors must say which it is.
  - Note also that in the Beltrami–Klein model geodesic sides are straight. The polygon is then exactly polygonal, and the operator has smooth matrix coefficients. This removes the geometric variational crime altogether.
- **(b) The printed ϵ_j measure rounding, not discretisation error.** They are about 1.3–1.6×10⁻¹³ relative (Table 5), which is the 10⁻¹⁴·λ floor times about 10. The text admits this ("near 10⁻¹⁴λ_j the difference reflects the solver and rounding"). Calling them "the difference between two independent discretisations" therefore overstates what they show at the low end.
- **(c) The counts are robust to the eigenvalue errors, and the paper should say so.** The quantitative point is in the authors' favour. I replaced ϵ_j by a uniform relative error rλ_j:
  - the triangle counts (18 and 25) are unchanged for r ≤ 10⁻⁴;
  - C1 fails for all N ≤ 39 at r = 10⁻³.

  So the conclusions hold under errors four orders of magnitude larger than the a-posteriori estimates.

  Enclosures at relative accuracy 10⁻⁴ of the first 20–40 eigenvalues of a triangle are routine with verified methods:
  - Liu–Oishi (SIAM J. Numer. Anal. 51, 2013) or Liu (Appl. Math. Comput. 267, 2015) Crouzeix–Raviart lower bounds, or Carstensen–Gedicke (Math. Comp. 83, 2014);
  - with the conforming upper bounds;
  - or Lehmann–Goerisch / Kato–Temple, with the required lower bound ρ for λ_{N+1} taken from such a bound.

  Combined with interval enumeration of the systole and validated quadrature of G_σ (the margins are 10⁻²), this would make the two triangle instances fully rigorous applications of Theorem 7.1.

  Either do this, or state the robustness margin explicitly and reword per M1.

## MINOR

**m1. Figure 1 does not match its description (p. 14).**
- The text says that the dark dotted curve is the tail-plus-perturbation term with "21 eigenvalues λ̃_0..λ̃_20 … (N = 20 …)". It also says the C2-type condition holds "at the grid times 0.050 and 0.056 (shaded)".
- The shaded band I measured on the rendered page spans t ≈ 0.050–0.056.
- With N = 20 (tail from λ̃_20 = 148.44) and s = kt/20, the condition "half the nearest gap exceeds the sum of the errors" holds only on [0.0550, 0.0567]. At t = 0.050 the error term is 0.034 against a half-gap of 0.0195.
- The plotted dark dotted curve reaches 10⁻⁶ at t ≈ 0.105. That matches a tail starting at λ̃_21 (1.3×10⁻⁶ at t = 0.105), not at λ̃_20 (9.4×10⁻⁶).
- The figure therefore appears to use N = 21, or the full gap instead of the half-gap: the window for "E < gap" is [0.049, 0.061]. Either way it does not match the text, which also says C2 "holds there with N = 20 (Table 6)".
- Fix the off-by-one, or the criterion, and the stated grid times.

**m2. E_N is needlessly two-sided and crude (Theorem 7.1, p. 15).**
Z̃ − G_σ(O) = Hyp − tail + perturbation, and Hyp and the tail are both positive. So the rigorous acceptance region for each σ is the interval [−(T+P), H+P], not ±(H+T+P), where T and P are the tail and perturbation bounds. With this one-sided test the triangle counts drop from 18 to 13 and from 25 to 19 (my computation, same grids). This is optional, but it is free.

**m3. The completeness budget (p. 17) cannot be built from Theorem 7.1's perturbation term.**
With about 2000 eigenvalues and ϵ_j ≥ 10⁻¹³ λ_j, the term t Σ ϵ_j at t = 0.0015 is at least about 3×10⁻⁹. That is far above the stated budget of 1.5×10⁻¹¹. The budget must use the sharper Σ t ϵ_j e^{-(λ̃_j−ϵ_j)t}. State the formula used. Better, put the sharper term into Theorem 7.1 itself: it is equally rigorous.

**m4. "(λ̃_N − ϵ_N)t of about 11" (p. 19).**
For the triangle instances this product is 135.94 × 0.0565 ≈ 7.7 and 202.56 × 0.0412 ≈ 8.3. The value about 11 applies only to the large-N family runs. Qualify it.

**m5. The hyperbolic bound wastes the authors' own enumeration (p. 17, "Systoles and diameters").**
- The enumeration up to L = 4 already lists every closed geodesic of length ≤ 4.
- Summing those classes explicitly, and using the counting bound of Lemma 2.2 only for lengths > L, replaces e^{3Δ}e^{-ℓ²/4t} by e^{3Δ}e^{-L²/4t}.
- In an illustrative computation, with three systole-class terms standing in for the enumerated short classes, both triangle counts fall to about 5.
- This also bears on M2: the instance-level gain comes from geometric information that could be exploited much further.

**m6. Consistency check limited to the least N (p. 18).**
"The program also checks … at the least N for which it holds." Extend this to all N in the complete range and report it. I find no wrong C1 for the triangles for N ≤ 39.

**m7. Missing details of the family completeness test (p. 17).**
- Give the time and budget of the family trace test that "covers λ < 9.8×10³".
- Name the three discretisations whose counts agree.
- Say whether they share the window strategy, which affects whether their agreement is independent evidence.

**m8. Regularity claim (p. 16, "No grading is used").**
The reflection argument covers corners of angle π/k with the same boundary condition on both sides. For the four-sector splitting of O_ϑ there are corners with mixed Dirichlet–Neumann conditions where a symmetry line meets a side at a right angle. The singular exponents there are (2j+1)π/(2ω) = 2j+1, which are integers, so the claim survives, but it should be stated.

**m9. Completeness hypothesis not explicit in the theorem statements (Theorem 7.1, p. 15; Theorem 1.2, p. 3).**
- The ordering hypothesis λ̃_0 ≤ … ≤ λ̃_N is not used in the proof.
- The hypothesis that carries completeness is the index-matched |λ̃_j − λ_j(O)| ≤ ϵ_j. Say so in the statement, as Theorem 1.1 does ("so that none of the first N is omitted").
- Theorem 1.2 leaves completeness implicit in "its first N+1 eigenvalues".

**m10. Systole margin (p. 17).**
The claimed "margin of at least 5×10⁻⁸" is consistent with my recomputed family values, whose actual margins are at least 2.9×10⁻⁷. For the family, the identification "systole = 4b" is numerical: Proposition 8.5 proves only ℓ ≤ 4b. Since Theorem 7.1 needs a lower bound, this is exactly the input that interval arithmetic should certify. It is cheap at the depth L = 4.

## Presentation

**P1.** N_obs is plotted in Fig. 2 (p. 20) but tabulated nowhere. Add it as a column of Table 6.

**P2.** Table 6 (p. 19) prints times with inconsistent precision: "0.084", "0.026", "0.017", "0.011" next to "0.0858" and "0.0107". Also state that "middle of the window" means the geometric middle; that is what reproduces the printed values.

**P3.** The abstract should say that the four decided cases are the M = 3 runs (see M1).

**P4.** Fig. 1 (p. 14) has six line styles and no legend. Label the competitor curves directly.

**P5.** Section 7.2 (p. 19): "the last two columns separate them". The separation comes from columns "(C1), Δ" against "(C1), D(A,ℓ,M)" and "N, Thm 6.2", that is, three columns. Rephrase.

## Recommendation

**Major revision** for the part I reviewed.

- Theorem 7.1 is correct.
- The tables are internally consistent and reproducible: I reproduced Table 3 and the triangle rows of Table 6 exactly, and the Table 6 estimates to within 2%.
- The section is commendably frank about its limitations.

However:
- the abstract and Section 7.2 still use "decides" and "succeeds" (M1);
- the main interpretive conclusion of Section 7.2 is contradicted by Table 6 (M2);
- Figure 1 does not match its text (m1);
- the treatment of completeness and eigenvalue errors omits the structural fact that would turn the demonstrations into rigorous decisions at modest cost (M3, M4).

Confidence: high on the recomputations and on M2 and m1; medium-high on the overall recommendation.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Replace "decides" and "succeeds" by "the criterion of Theorem 7.1 holds (with estimated errors, for lists assumed complete)" in the abstract, Section 1, Section 7.2 and the Fig. 2 caption, and say that "four of ten" means M = 3. Alternatively, keep "decides" for any instance made rigorous under M4(c). |
| M2 | Delete or invert the sentence "most of the gap … is knowledge of the geometry". Report both factors per row (geometry about 20 to 840; data about 20 to 3×10⁸) and state that the data dominate except at M = 3. |
| M3 | Report Sylvester inertia counts at every window boundary for all problems. State that for a conforming discretisation with index-wise enclosures, completeness follows and (iv) and (v) merge. Run the completeness trace check against every σ ∈ S and at several times. Give t and the budget for the family. Add the persistence diagnostic, with the observation that the low-index failures are not flagged by it. |
| M4 | Say whether the computational domain is exact or polynomially approximated; if the latter, correct the upper-bound sentence; consider the Klein model. Describe the ϵ_j honestly as near rounding level. Report the robustness margin: counts unchanged for relative errors up to 10⁻⁴. Preferably certify the two triangle instances: guaranteed lower bounds of Liu–Oishi or Carstensen–Gedicke type plus conforming upper bounds, an interval systole, and validated G_σ. |
| m1 | Correct N (20 or 21), the criterion (half-gap or gap) and the shaded grid times in Fig. 1 so that they agree. |
| m2 | Optionally adopt the one-sided acceptance interval. |
| m3 | State the completeness-budget formula, and put the sharper perturbation term into Theorem 7.1. |
| m4 | Qualify "about 11". |
| m5 | Optionally use the enumerated short geodesics in H; at least mention it. |
| m6 | Extend the wrong-signature check to all N and report it. |
| m7 | Add the missing family completeness details. |
| m8 | Add one sentence on the mixed-boundary-condition corners. |
| m9 | Make the completeness hypothesis explicit in Theorems 7.1 and 1.2, and drop the unused ordering hypothesis. |
| m10 | Certify the systole lower bounds with interval arithmetic, or flag the family identification "systole = 4b" as numerical. |
| P1–P5 | Editorial fixes as listed. |
