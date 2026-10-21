<!-- Round 10, B-d, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

Writing REPORT.md was refused, so here is the full report.

# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (AGAG)

**Remit of this report.** I was asked to referee the computer-assisted part of the paper: Corollary 6.4, the certification paragraph (p. 16), Proposition 6.5 with Tables 3 and 4 (p. 17), Section 7 (pp. 20–27, Tables 6–8, Figs. 1–2), and the numerical claims those parts rely on. I work on validated numerics (interval and ball arithmetic, validated quadrature, validated eigenvalue enclosures). I did not referee Sections 3–5 or 8 or the appendix, except where Proposition 6.5 depends on them. I treated the marked placeholders (author contributions, AI statement, Zenodo DOIs, preprint identifiers) as known. So I did not have the authors' deposit code. All of my recomputation below starts from the formulas printed in the manuscript.

## Summary

The paper shows that, within a class C(A, ε, M), finitely many approximate Laplace eigenvalues determine the signature of a closed hyperbolic 2-orbifold. It gives explicit N and δ (Theorem 6.2). Those constants are astronomically large, so the paper adds Corollary 6.4. This corollary turns a gap |G_σ(t) − G_σ'(t)| ≥ Θ, computed over the finite set Sig(A, M) at one moderate time t, into rigorous values of N and δ. It then certifies the gap in Arb ball arithmetic for six classes (Proposition 6.5, Tables 3–4), which gives N = 139 to 7416 for the classes that contain the computed examples, and 387 182 for one class with small systole. Section 7 runs an a-posteriori version of the test (Theorem 7.1) on ten FEM spectra. It labels the results as consistency checks, not proofs.

## Significance

The computer-assisted part is modest in scope but genuine. Corollary 6.4 is a clean observation: the proof of Theorem 6.2 uses Lemma 6.1 only to obtain the gap at one time, so a certified gap can replace it. With this observation the effective theorem moves from 10^8–10^30 eigenvalues to 10^2–10^4. The certified statement concerns six classes chosen to contain the authors' examples, so on its own it is a demonstration that the method can be made concrete, not a general result. That is appropriate for the role the paper gives it. The paper is careful not to oversell Section 7.

## Correctness and what I recomputed

I wrote an independent implementation in python-flint 0.9.0 (FLINT 3.6.0, `acb.integral`, 200 bits) and mpmath/scipy, in a private venv. It uses only the manuscript's formulas: Theorem 2.1, Lemma 4.5, Corollary 6.4, Theorem 6.2, Theorem 7.1. Results:

1. **Enumeration of Sig(A, M).** Recomputed in exact rational arithmetic, including genus ≥ 1. I get |Sig| = 27, 48, 8, 8, 281, 12, matching Table 3.
2. **Certified gaps (Table 4).** I enclosed I(t) and every E_m(t) by Arb integration on finite intervals, adding the printed tail bounds to the radius. The certified minimal gaps are 0.01588232199, 0.006527298332, 0.1520292966, 0.1655107998, 0.001373851304, 0.1666487023, with radii ≤ 5e-11. All agree with Table 4 to every printed digit.
   - The minimising pairs are the ones listed.
   - The tie statements on p. 16 are correct: two pairs in row 1, including (0;2,3,8)/(0;2,4,5); two pairs in rows 3–4; three pairs in row 6.
3. **The three inequalities of Corollary 6.4 (Table 4) and N, δ (Table 3).** I recomputed C*, B*(t), t2, Z♯, Λ, eZ♯(1/Λ), N and δ in ball arithmetic, using Θ as printed in Table 3. Every ball of eZ♯(1/Λ) lies strictly between two consecutive integers, at distances from 0.13 to 0.53 from the nearest integer. I get:
   - N = 244, 283, 139, 2605, 7416, 387182 and δ = 1.1671e-4, 4.2731e-5, 5.8993e-4, 4.8669e-4, 2.4878e-6, 2.1414e-4. These match Table 3 exactly; δ is correctly rounded down.
   - B*(t) = 7.976e-6, 7.104e-5, 0.017933, 0.016707, 1.406e-4, 0.013936, and Λt = 17.63, 19.64, 12.52, 17.21, 27.94, 26.32. These agree with Table 4.
   - t ≤ t2 holds with a wide margin in every row.
   - The tightest margin is row 3 (B*/(Θ/8) = 0.944), as stated.
4. **Theorem 6.2 constants (Table 5, last column of Table 3).** I computed b_K(M) from the Taylor coefficients of Φ_M (80 digits), α_K, a_k, C*, t1, t3, Θ*, Λ, N and δ for all eight rows. Every entry agrees with the stated rounding convention; for example N = 3.40e8, 6.82e9, 4.32e4, 7.44e12, 2.28e6, 1.08e6, 3.75e30. The peripheral claims on p. 18 also check:
   - N ≈ 4.2e18 without k* ≤ M at A = 10π.
   - t3 binds from ε = 0.44 down.
   - The per-halving factor of N falls from 5.24 to 4.67 after seven halvings.
5. **Table 6.**
   - Closed-form systoles: 2.2567679, 1.8626041, and 4b for the family (2.6339158 … 0.6939946). The printed ℓ are correct floors at the sixth decimal; the least margin is 5.5e-8, as stated.
   - 2 diam P is correct and correctly rounded up in all ten rows (4.897, 4.317, 4.585, …, 7.770).
   - C* is correct (3.545e9 → 3.6e9; 4.010e5 → 4.1e5; 9.454e9 → 9.5e9).
6. **Independent check of Theorem 2.1's normalisation and of Table 7.** With the 40 tabulated eigenvalues, Σ e^{-λ̃_j t} − G_σ(t) at t = 0.08–0.2 equals the contribution of the two systolic classes (γ and γ^{-1}) to 3–4 digits for both triangle orbifolds. For example, at t = 0.1 for O(2,8,8): 4.202e-6 against 4.192e-6. The FEM does not use the trace formula, so this independently confirms the elliptic and identity normalisation of G_σ, which the certificate rests on. It also confirms that Table 7 is consistent.
7. **Section 7 numbers.**
   - Nearest-competitor gap at t = 0.0015: 2.9686e-3 (claimed ≥ 2.96e-3).
   - The thresholds 1.563e4 and 1.576e4 are correct.
   - H(0.0562) = 6.77e-3 against a geodesic term of 2.77e-10, a ratio of 2.44e7 (as stated).
8. **Table 8, triangle rows, re-run from Table 7 alone.** I re-ran Theorem 7.1 using only the 40 eigenvalues of Table 7, with errors max(ε_j, 5e-7) to cover the six-decimal rounding.
   - I reproduce all eight triangle counts exactly: 18, 20, 24, 24 for O(2,8,8) and 25, 29, 36, 36 for O(3,3,12). My window midpoints agree to within grid resolution.
   - With r = 1e-2 I get 21 for O(2,8,8) (claimed 21). The claimed 43 for O(3,3,12) needs more than 40 eigenvalues, so I could not check it.
   - **The 24-corruption experiment (item (iv), p. 21) reproduces exactly**: 19 of 24 corrupted lists make (C1) single out a wrong signature, at N = 9–26, below the true counts.
9. **The analytic chain behind Corollary 6.4.** I checked the proofs of the following, as far as Proposition 6.5 uses them:
   - Lemma 2.2(ii): the integration by parts, the monotonicity range, and the factor 3 for t ≤ t2.
   - Lemmas 4.2, 4.3 and 4.5: the constant C*.
   - Lemma 5.1 (n ≤ ⌊A/π⌋+4, b0 increasing).
   - Proposition 5.2 and the proof of Theorem 6.2.

   I found no error. The error budget Θ/8 + Θ/8 + Θ/(8e) < 3Θ/8 < 5Θ/8 is correct.

**Verdict on the computer-assisted statement.** Proposition 6.5 is a proof in the accepted sense for computer-assisted mathematics:
- every quantity is enclosed in ball arithmetic;
- the quadrature tails are bounded analytically, and correctly (I checked both elliptic tail bounds and the identity tail bound);
- every decision is made on balls;
- N is taken only after the floor is decided;
- δ is rounded down.

I reproduced the whole certificate independently in under 30 seconds per class. Section 7 is honestly framed overall, with the exceptions listed under M2 and m2–m4.

## FATAL

None.

## MAJOR (required changes; none affects the correctness of any stated result)

**M1 (pp. 16–17). The certificate must be checkable from the paper, and the integration protocol must be stated completely.** The proof of Proposition 6.5 currently consists of a prose description plus "the program certified_gap.py … asserts each of them … This proves the following." A computer-assisted proof should let a reader check the certificate without rerunning adaptive integration. The data needed are tiny. For each row, J(t) = e^{-t/4}/t − ∫_0^∞ 4r e^{-t(1/4+r^2)}/(e^{2πr}+1) dr and E_m(t), 2 ≤ m ≤ M, determine every G_σ(t) by G_σ = (s(σ)/2)·J + Σ E_{m_i}. That is at most 12 enclosures per row, or at most 61 numbers in total. Please print them with their radii in an appendix table. With that table, the gap, the minimising pairs and the inequalities of Table 4 become checkable by hand or with any interval package. In the same paragraph, please also state:
- (a) how t enters the computation: as the exact decimal rational, enclosed as a ball;
- (b) the tolerances and evaluation limits passed to acb_calc_integrate;
- (c) that the integrands are compositions of exp, polynomials and division only, with no branch cuts. Arb's holomorphy requirement on complex balls is therefore met automatically, and ball evaluation detects the poles of 1/(1+e^{-2πr}) at r = ±i/2, …. Misuse of the `analytic` flag is the classic failure mode of Arb-based proofs, and the reader should not have to infer that it cannot occur here.

Resolution: add the enclosure table and the three sentences. My recomputation confirms all values, so this is a matter of verifiability, not of correctness.

**M2 (p. 22, "The accuracy needed is modest"). The paragraph misstates what a rigorous instance would require, in both directions.**
- (i) It quotes the uniform δ = 4.27e-5, "about 2e-8 relative at λ_282". Proposition 6.5 also allows the weighted hypothesis Σ_j |λ̃_j − λ_j| e^{-t min(λ̃_j, λ_j)} ≤ Nδ = 0.0121 (row 2). With a uniform relative error r and Weyl's law (λ_j ≈ 8j), the left side is about 8r Σ_j j e^{-0.199 j} ≈ 200r. So r ≈ 6e-5 relative already suffices. That is three orders of magnitude weaker than the figure quoted. Only the low part of the spectrum needs accuracy; the top only needs index information.
- (ii) Conversely, the route the paragraph proposes, Crouzeix–Raviart-type lower bounds [41, 42], converges only at O(h^2). Liu's bound λ ≥ λ_h/(1 + C_h^2 λ_h) with C_h ≈ 0.19h would need h ≈ 1e-5 to reach 2e-8 relative at λ ≈ 2250, that is, of order 1e9 elements. So the claim "accuracy is modest" is wrong for the method proposed, if one targets the uniform δ.

As written, a reader cannot tell whether a rigorous instance is near or far. My estimate suggests it is near, if one uses the weighted hypothesis (CR lower bounds with r ≈ 6e-5 at λ up to a few hundred need meshes of order 1e6). Completeness would then follow from index-wise enclosures. Alternatively, method-of-particular-solutions inclusion intervals, combined with the certified heat-trace comparison, rule out a missing eigenvalue once spurious ones are excluded by existence enclosures.

Resolution: rewrite the paragraph around the weighted requirement, with a short feasibility estimate. Ideally, carry out one rigorous instance (O(2,8,8) in the M = 8 class needs N = 244), which would make Proposition 6.5 an actual determination. If no instance is done, replace "certified instances of practical size" (p. 3) by a description that does not imply practice, for example "of moderate size".

## MINOR

- **m1 (p. 17, Table 4; p. 16).** Rows 1 and 3 of the Θ/8 column read 0.001984 and 0.01899. But Θ/8 is 0.001985 and 0.019000 exactly (Θ = 0.01588 and 0.1520 from Table 3; the certified gaps/8 are 0.0019853 and 0.0190037). The printed values are valid lower bounds, but they are not "rounded down" values as the caption says. The text on p. 16 repeats "Θ/8 ≥ 0.01899". Print 0.001985 and 0.01900, or say that one unit was subtracted.
- **m2 (p. 22).** "The counts of Table 8 survive errors of 1e-3 relative" is stronger than item (v) on p. 21, which claims this only for the (C1),Δ counts 18 and 25. On my 240-point grid in [0.01, 0.2], with ε_j = max(ε_j, 1e-3·λ̃_j):
  - (C1),Δ stays at 18 and 25;
  - but (C2),Δ for O(2,8,8) moves from 20 to 21;
  - and (C1),C* for O(3,3,12) moves from 36 to 37.

  This may depend on the grid. Please either verify the sentence on your grid or restrict it to what item (v) states.
- **m3 (p. 26, last paragraph; Fig. 2 caption).** The comparisons "the data account for a further factor of about 6 to 12" and "the test needs 56 to 2.7e11 times fewer eigenvalues" set a count from the test (uses N+1 eigenvalues, with estimated errors and assumed completeness) against rigorous counts (use N eigenvalues). The ratios are right: I get 5.7–11.8 and 56–2.7e11. But the caption advertises the comparison with Theorem 6.2, which the paper itself calls irrelevant in practice.
  - Add Proposition 6.5's N to Fig. 2 as its own marker at systoles 1.8626, 2.6339 and 0.6940.
  - Lead the caption with the comparison against Proposition 6.5.
  - Say once that a test count of N corresponds to N+1 eigenvalues.
- **m4 (p. 25, Table 7).** The column ε_j is titled "a-posteriori error estimates". But p. 24 says that for these 40 eigenvalues the ε_j "are at rounding level and say nothing about the discretisation error". The table should not label them error estimates. Either rename the column (for example "difference of two discretisations") or tabulate the more meaningful second estimate |λ_j(0.05,10) − λ_j(0.07,10)| alongside.
- **m5 (p. 17, Prop. 6.5).** "(or with omissions only as in Remark 6.3)": Remark 6.3 is stated with t*, Θ* and Λ_o = t*^{-1} log(8/Θ*). Say that t and Θ of Table 3 replace them, and consider adding Λ_o to Table 3, since it is what a user needs. For row 2, Λ_o ≈ 287, so omissions are tolerated only above roughly the 36th eigenvalue.
- **m6 (p. 17).** The decision rule requires G_σ(t). Say explicitly that the certified enclosures (radius < 1e-10) are far inside the slack Θ/8, so the rule as certified is computable from M1's table. The paper makes this remark for Theorem 6.2 (Θ*/16) but not for Proposition 6.5.
- **m7 (p. 17).** "N = 3.9 × 10^5 … where the closed geodesics bind": Corollary 6.4 has no t3, and in row 6 B*/(Θ/8) = 0.67, which is not the tightest row. Say what "bind" means here: the admissible t is forced down by the factor e^{-ε²/4t}.
- **m8 (Abstract, p. 1; p. 3).** "within about 6 × 10^-4 to 2 × 10^-6": the smallest δ is 2.48e-6. Write 2.5 × 10^-6.
- **m9 (p. 17, Table 3 caption).** Add "with none omitted" after "each known to within δ". The caption currently states the conclusion without the hypothesis that the paper elsewhere rightly stresses.
- **m10 (p. 23).** The completeness budget "at most 5.2e-11" and the agreement "4.7e-13" cannot be checked from the paper, because only 40 of about 2000 eigenvalues are printed. Since Section 7 is explicitly illustrative, a pointer to the exact data file is enough. Make sure the deposit contains the lists used for Table 8, not only the full computed lists.

## Presentation

- **P1 (p. 16).** The certification paragraph is one block of about 25 lines mixing enumeration, quadrature, tails, decisions and ties. Split it into numbered steps (enumerate; enclose J and E_m; decide the pairwise gaps; decide the three inequalities; decide ⌊eZ♯⌋; round δ down). Move the tie discussion into the Table 4 caption.
- **P2 (p. 16).** The parenthesis "(several pairs attain it … as G_σ is additive in the orders and pairs differing by {3,3,3} against {2,2,2,2} have the same gap)" runs two different explanations together. The first-row tie comes from the same additivity, with the common order 3 replaced by 2. Rewrite it as two sentences, and add that row 6 has three tied pairs.
- **P3 (p. 19, Fig. 1).** N = 21 is drawn while (C2) holds with N = 20. The reason is the coarser s-grid (k/20) in the figure, and it is explained, but readers will stumble. Either draw N = 20 with the paper's s-grid, or move the explanation into the caption.
- **P4 (p. 26).** Table 8 mixes the count conventions of Theorem 7.1 (N+1 eigenvalues) and Theorem 6.2 (N eigenvalues) in one row. The caption says so, but a separate final column for Proposition 6.5's N, in the Theorem 6.2 convention, would make the table self-explanatory (see m3).

## Recommendation

**For the parts in my remit: minor revision. Confidence: high.**

I independently reproduced every certified number of Proposition 6.5 (Tables 3 and 4) to all printed digits, all of Table 5, the inputs in Table 6, and the triangle rows of Table 8, including the corruption experiment. I found no error in the analytic chain the certificate relies on. Proposition 6.5 is a valid computer-assisted proof. Section 7 is honestly framed: the title, the abstract and the text all say these are consistency checks with estimated errors and assumed completeness. M1 and M2 are the only substantive requests. M1 asks that the certificate be printed so it is checkable from the paper. M2 asks for a correct account of how far a rigorous instance is. Neither changes a result.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Appendix table of the enclosures of J(t) and E_m(t), 2 ≤ m ≤ M, for the six times; state the exact-rational t, the integration tolerances, and why holomorphy on balls holds |
| M2 | Rewrite p. 22 around the weighted hypothesis, with a feasibility estimate (≈ 6e-5 relative, not 2e-8); preferably carry out one rigorous instance; otherwise soften "practical size" (p. 3) |
| m1 | Print 0.001985 and 0.01900 (or state the extra unit), also on p. 16 |
| m2 | Restrict the 1e-3 sentence to the (C1),Δ counts, or verify it on the full grid |
| m3 | Add Proposition 6.5 to Fig. 2 and lead the caption with that comparison; state the N/N+1 convention once |
| m4 | Rename the Table 7 error column, or add the second estimate |
| m5 | State the substitution in Remark 6.3; add Λ_o to Table 3 |
| m6 | One sentence on the tolerance of the decision rule to enclosure radii |
| m7 | Clarify "bind" for row 6 |
| m8 | 2.5 × 10^-6 |
| m9 | "with none omitted" in the Table 3 caption |
| m10 | Point to the exact data files used for Table 8 |
| P1–P4 | Restructure the certification paragraph; fix the tie parenthesis; align Fig. 1 with Table 8; add a Proposition 6.5 column to Table 8 |

Reproducibility of this report. My scripts are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/B-d-computer-assisted-proof-referee/scratch/:
- cert.py: Arb re-certification of Tables 3–4.
- thm62.py and thm62b.py: Table 5 and the claims on p. 18.
- sec7.py: heat-trace and normalisation checks, the t = 0.0015 gap, and H(0.0562).
- test71.py: Theorem 7.1 on Table 7.
- corrupt.py: the 24 corruptions.
