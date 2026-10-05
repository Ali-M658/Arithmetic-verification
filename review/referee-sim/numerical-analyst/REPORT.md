# Referee report: "How much of a hyperbolic orbifold does heat hear?"

**Journal:** The Journal of Geometric Analysis
**Referee role:** numerical analyst. I read the whole paper but concentrated on Sections 6.4–6.5, 7, Tables 2–3, Figures 4, 5 and 9, and Appendix C.
**Basis:** the 56-page PDF and nothing else. I did not consult the repository or the Zenodo archive. The only literature I fetched was Strohmaier–Uski (arXiv:1110.2150v4), including its ancillary eigenvalue file for the Bolza surface. Every recomputation below was done with my own scripts: exact rational arithmetic in sympy, mpmath, and a small independent P2 finite-element solver in the Klein model.

---

## 1. Summary of the paper

The paper asks how many short-time heat-trace coefficients c_1, c_2, … of a closed orientable hyperbolic 2-orbifold are needed to determine its signature (the genus and the multiset of cone orders), and what the coefficients cannot determine. It uses Uçar's closed form for the constant-curvature cone contributions (Prop. 2.4, Lemma 2.5). From this it shows that the j-th coefficient adds exactly one new odd power sum P_{2j−3} of the cone orders (Lemma 2.10). Comparing two orbifolds therefore becomes a moment problem for a signed multiset. The main results are:

- **Signature.** The first ⌊Area/π⌋+4 coefficients determine the signature (Cor. 3.7). No fixed number works for all areas (Thm 3.10, via Prouhet–Thue–Morse). For spheres with n cone points, n coefficients suffice (Thm A). The paper also gives a linear system with a closed-form determinant (Thm B) and sharpness statements (Thm C).
- **Shape.** Every coefficient depends only on the signature (Thm 4.1). The moduli enter the heat trace only at the size t^{−1/2}e^{−ℓ²/4t}, and this rate is attained (Thms 4.9, 4.10).
- **Triangle orbifolds.** Two coefficients determine O(p,q,r) whenever p+q+r ≤ 17. The first failure is the pair O(2,8,8), O(3,3,12) (Thms 5.12–5.14), which is isolated through a rank-0 elliptic curve (Thm 5.16). Section 8 counts the later two-coefficient degeneracies.
- **Stability.** Recovering the orders from noisy coefficients is Lipschitz at simple orders and Hölder-1/k at k-fold orders, with explicit constants (Thms 6.4, 6.6, 6.9). Rigorous rational-arithmetic certificates give thresholds for exact recovery of integer orders (Prop. 6.10, Table 2).
- **Numerics.** Section 7 computes about 2850 eigenvalues of each of O(2,8,8) and O(3,3,12) with p = 10 finite elements in the Poincaré disc, and about 5450 eigenvalues of each of eight members of a one-parameter family of signature (0;3,3,3,3). The paper uses these spectra to:
  - "listen" to the minimal pair, by fitting d_3 and d_4 of D(t) = Z_{(2,8,8)} − Z_{(3,3,12)};
  - show that the heat trace agrees with I + E across the moduli family while the spectra move;
  - test the geodesic-sum prediction of Theorem 4.10;
  - run a "blind" recovery of both triples from estimated c_1, c_2, c_3 (Section 6.5, Table 3).

  The paper states that none of the computations is used in a proof.

## 2. Significance and novelty

The mathematical core is a clean and, as far as I can judge, new quantitative answer to a question that earlier work left qualitative:

- **Prior results do not count coefficients.** Dryden–Strohmaier [6, Thm 1.1] and Doyle–Rossetti [7] obtain the cone orders from the full spectrum. Uçar [8] obtains them from the entire coefficient sequence through a large-order limit. Dryden–Gordon–Greenwald–Webb [3, Rem. 5.16] explicitly leave open whether c separates the triangular pillows.
- **The threshold is new.** Theorem 1.3 answers [3, Rem. 5.16] with an exact threshold of 17 and an isolated minimal pair, which I find attractive. The ⌊Area/π⌋+4 bound and the Prouhet construction are also new as far as I know.
- **The stability analysis is unusual for this area.** Section 6 has explicit constants, sharp exponents and certificates done in rational arithmetic, and it is the part of the paper closest to numerical analysis.

The numerical sections are confirmations, not evidence for theorems. Nothing in Sections 2–6 or 8 depends on them, so none of my major issues affects the validity of a theorem. They do affect:

- the abstract sentence "Computed spectra confirm the predictions within their error budgets";
- the claims of a "certified" blind recovery;
- the reproducibility statement.

**Comparison with the numerical literature.**

- **Strohmaier–Uski [34].** This is the standard reference for high-accuracy eigenvalues of compact hyperbolic surfaces. I confirmed from arXiv:1110.2150v4 that:
  - they give λ_1(Bolza) = 3.83888725884219951858… (multiplicity 3);
  - the ancillary file `eig-bolza-refined0-1000.txt` lists about 1000 eigenvalues with multiplicity, up to 998.0509;
  - they state about 12-digit accuracy for the first 500 eigenvalues and checked completeness through the Selberg trace formula.

  Only λ_1 carries a rigorous error bound, of 10^{−6}. The other values are high-accuracy but heuristic.
- **Aurich–Steiner.** They computed the Bolza spectrum by finite elements (cited in [34]).
- **Hejhal's method.** Hejhal's method for cofinite Fuchsian groups is the obvious independent technique for triangle groups. The paper does not use or cite it, and it would be a natural cross-check.

The paper's numerical method (high-order H¹ finite elements on a geodesic triangle, with Neumann ∪ Dirichlet giving the orbifold) is sensible and standard. Its use of the exact I + E of the trace formula as an a-posteriori completeness and accuracy check is good practice, and it is the same idea Strohmaier–Uski use.

## 3. Correctness: claim by claim (numerical content)

Key to status labels:

- **V:** verified by my own recomputation.
- **E:** error found.
- **G:** gap (the claim may be true, but the paper does not give enough to check it).
- **NC:** could not check.

### Heat-coefficient formulas (Sections 2, 6.1)

| Location | Claim | What I did | Status |
|---|---|---|---|
| p. 8, line after (6) | α_0..α_4 = 1, −1/3, 1/15, −4/315, 1/315 | Implemented (5) exactly; also got α_5 = −4/3465 | V |
| (7), p. 8 | p_0, p_1, p_2 | Implemented (4)–(5) exactly; all three match | V |
| Cor. 2.9, p. 9 | cone(2), cone(3), cone(5) = 1/8, 2/9, 2/5; (2,3,5) gives 269/360 and 271/360 | Exact arithmetic | V |
| (10)–(11), p. 9 | b_1 and Σ b_1 | Matches the p_1 above | V |
| p. 43 | c_2 = 67/48; d_3 = 25/12; d_4 = −1775/24; d_5 = 153025/48 | Exact c_j for both orbifolds: c_3 = −1601/480 and −867/160; c_4 = 555313/20160 and 2046313/20160; c_5 differences as stated | V |
| p. 44 | at t = 0.02, d_3t, d_4t², d_5t³ = 0.042, −0.030, 0.026 | 0.0417, −0.0296, 0.0255 | V |
| p. 36 | F^{−1} rows; amp_0..amp_4 = 2, 14, 498, 4062, 56230/3; diagonal 2, 12, 360, 2520, 10080 | Built F from Prop. 6.2 and inverted exactly | V |
| Thm C(3), p. 14 | R, P_1, P_3, P_5 of the four multisets | Exact | V |
| Rem. 3.11, Ex. 3.13 | (0;4,4,4,6,6) ~ (0;2,2,2,3,8,8) share exactly c_1, c_2; (1;15) ~ (0;3,3,5,5) exactly two; (1;15,15,15) ~ (0;3,3,5,7,7,21) exactly three | Exact c_1..c_4 | V |

### Stability (Section 6)

| Location | Claim | What I did | Status |
|---|---|---|---|
| p. 37 | ζ_3 = 1, ζ_4 = 79/3, ζ_5 = 14048/15 | Taylor coefficients of artanh·sec² | V |
| p. 37 | "exact cond is between 1 and 3.5 on every test multiset" | cond = 1.0 for all n = 3 cases; 1.82–2.34 for n = 4; **3.5109** for (2,2,2,2,3) | E (trivial, m2) |
| Prop. 6.7, p. 39 | ratios 2.7385, 4.4630, 2.0446 | Series of c(m(s)) to O(s²): 2.73850, 4.46296, 2.04460 | V |
| Table 2, δ_thm column | all 11 values | Implemented Thm 6.9 from scratch (cond, r_n, Ξ_µ, Π̂_a, ζ_n). Got 3.803e−7, 1.189e−7, 4.021e−11, 3.147e−11, 4.492e−7, 9.354e−7, 9.973e−8, 1.487e−9, 4.744e−10, 2.031e−9, 2.7298e−12. All agree with the table after rounding down. | V |
| Table 2, δ_up column (n = 3 rows) | 2.485e−3, 4.589e−3, 6.587e−3, 5.036e−4, 8.273e−5 | Global minimisation (differential evolution) of ‖c(q̃)−c(m)‖_∞ over real monic cubics with a root, or a complex pair, of real part a ± ½. Got 2.4849e−3, 4.5883e−3, 6.5869e−3, 5.0358e−4, 8.2721e−5. These agree after rounding up, so the constructed failures are reproducible. | V |
| Table 2, δ_cert | the certified values | Did not reimplement Prop. 6.10. The ratio column is consistent with δ_up/δ_cert to 3 s.f. in all 11 rows. | NC (ratios V) |
| Table 2, ε_cert; p. 41 | "binding coefficient is c_3 … relative precision about 7×10^{−4}; c_1 and c_2 need only percent-level and 10^{−3}-level" | 7×10^{−4} = δ_cert/\|c_3\| is arithmetically right. But the interpretation is wrong: see m1. Under the relative model, the minimal failure for (2,8,8) is ε_up = 2.09×10^{−3}, with all three coefficients saturated. Perturbing c_3 alone needs 0.93% relative error, and c_2 alone fails first, at 0.28%. | E (m1) |

### Blind recovery (Section 6.5, Table 3)

| Location | Claim | What I did | Status |
|---|---|---|---|
| Table 3 | estimates and error bars | Compared with exact values: c_2(A) −3.0e−9 (0.13 bar), c_3(A) +3.17e−6 (0.15 bar), c_2(B) −4.18e−8 (0.32 bar), c_3(B) +5.47e−5 (0.39 bar) | V (but see m4) |
| Table 3 "roots" | A: 2, 8 ± 0.0050i; B: 2.9915, 3.0085, 11.99995 | Reran the whole recovery map (F^{−1}, then the Theorem B system with tanh series, then roots) from the printed estimates. A: 1.9999996, 8.0000002 ± 0.0050176i. B: 2.991538, 3.008513, 11.999948. | V |
| p. 42 | margin to δ_cert "about 100 for A and 20 for B" | (\|est−exact\| + bar) for c_3: 2.42e−5 and 1.95e−4, giving ratios 97 and 20.7 | V |
| p. 42 | c_1, c_2 of A and B "differ by 0.21 and 0.26 standard errors" | c_2: 3.88e−8, which is 0.29 in quadrature or 0.25 with linear addition. c_1: unverifiable from the printed digits. | G (m3) |
| p. 42 | c_3 differ by 2.0833 ± 1.6×10^{−4} | 2.0832818 vs exact 25/12 (−0.36 combined bar); 1.6e−4 is the quadrature sum | V |
| p. 42 | exhaustive triad enumeration returns {(2,8,8),(3,3,12)} | Follows from Table B1 (I recounted 83 triads with 10 ≤ S ≤ 18) | V |

### Listening experiment (Section 7.1)

| Location | Claim | What I did | Status |
|---|---|---|---|
| p. 43 | about 1420–1440 eigenvalues per triangle and BC up to λ ≈ 21,700 (N) and 23,800 (D) | Computed triangle perimeters: 5.5056 for (2,8,8) and 5.3801 for (3,3,12). Three-term Weyl law: N_N(21700) = 1421.5 / 1420.0; N_D(23800) = 1420.6 / 1422.1 | V |
| p. 43 | fitted d_3 = 2.0833320 ± 3.1e−6 (−0.4σ), d_4 = −73.9551 ± 0.0062 (+0.5σ) | Deviations from exact: −1.33e−6 (−0.43) and +3.23e−3 (+0.52) | V (arithmetic) |
| p. 43 | eigenvalue errors ≤ 2.9e−11 relative (first 500), conservative ≤ 1.2e−8; error budget 3×10^{−11} | See M1: the budget cannot follow from these per-eigenvalue bounds by worst-case propagation | G (M1) |
| p. 43 | "a missing eigenvalue below about 10^4 would show at the level 10^{−7}" | e^{−10^4·0.0015} = 3e−7. The trace test actually detects (at 10× the 7e−13 agreement) a missing eigenvalue up to λ ≈ 1.7×10^4, but not in 1.7×10^4–2.4×10^4 | V, with qualification (m7) |
| p. 43 | trace agrees with I + E "to 7×10^{−13} for t ≤ 0.03" | No lower limit is given. My Weyl estimate of the truncation tail: 3.2e−13 at t = 0.0015 and 2.6e−8 at t = 0.001, so the statement is only meaningful for t ≳ 0.0015 | G (m5) |
| p. 44 | systoles 2.2568 for (2,8,8) and 1.8626 for (3,3,12) | Computed from the products of the two highest-order rotations: cosh(ℓ/2) = cos²(π/8)+sin²(π/8)·cosh d with cosh d = 5.8284, giving ℓ = 2.2568; and (1+3·1.62124)/4, giving ℓ = 1.8626 | V |
| Fig. 5(a), p. 26 | D changes sign near t = 0.34 | Needs the spectra or a long geodesic enumeration | NC |

### Bolza benchmark (p. 43)

| Location | Claim | What I did | Status |
|---|---|---|---|
| p. 43 | "reproduces all 42 multiplicity-one eigenvalues below 998 of the Bolza surface listed by [34], which covers the (2,3,8) triangle orbifold, to 5.7×10^{−11}" | Built a P2 FEM in the Klein model for the (π/8, π/2, π/3) triangle with the four admissible 1-D characters of the extended triangle group (NNN, DDD, and the two mixed classes, where the edges at the π/3 corner must agree). Counts below 998: **15 (NNN, excl. 0) + 6 (DDD) + 11 + 10 (mixed) = 42**. My values reproduce [34]'s 23.0786 (NNN) and 32.6737 (mixed). So the "42" is right, but only 21 of the 42 are eigenvalues of O(2,3,8); the other 21 need mixed boundary conditions. | E (description), see M4 |

### Moduli experiment (Section 7.2, Fig. 4)

| Location | Claim | What I did | Status |
|---|---|---|---|
| p. 44 | sinh a sinh b = cos(π/3); ϑ = log(sinh a/sinh b); systole 4b(ϑ) = 2.634, 1.831, 1.250, 0.694 at ϑ = 0, 0.8, 1.6, 2.8 | 2.6339, 1.8313, 1.2504, 0.6940 | V |
| p. 44 | about 5450 eigenvalues up to λ ≈ 1.6×10^4 | Weyl: λ/3 + 7/9 = 5450 at λ ≈ 16,350 | V |
| p. 44, Fig. 4 | λ_1 = 4.1224 at ϑ = 0 and 0.4348 at ϑ = 2.8 | Independent P2 FEM in the Klein model (where the Lambert quadrilateral is a Euclidean rectangle [0, tanh a]×[0, tanh b]), with all 8 symmetry sectors. ϑ = 0: λ_1 = 4.122413 (double, sectors N·ND and N·DN). ϑ = 2.8: 0.434834 (40×40 P2). Also λ_1(0.8) = 2.14295 and λ_1(1.6) = 1.10702. | V |
| p. 44 | "first 200 eigenvalues move by up to 89%" | λ_1 alone moves 89.45% | consistent |
| p. 44 | Z_i − Z_j = Hyp_i − Hyp_j to 1.1e−13 for t ≤ 0.33, with geodesics enumerated to length 6.5 | Order-of-magnitude estimate of the omitted geodesic tail at t = 0.33: about 10^{−14} | consistent, NC exactly |
| p. 44 | ℓ²/4t* ≈ 24.5 in every case | Leading term at ℓ²/4t = 24.5 is 4e−11 to 2e−10, the size of the shaded budget in Fig. 5(b) | consistent |

### Section 5 and 8 enumerations (not my focus; cheap to check)

| Location | Claim | What I did | Status |
|---|---|---|---|
| Thm 5.13 | exactly 38 collision-free sums 18 ≤ S ≤ 4800, the largest 557 | Exhaustive enumeration to S = 600 finds exactly 38, listed as 19, 21–25, 27–30, 33, 41, 44, 46–51, 59, 65, 67, 81, 99, 115, 119, 123, 125, 173, 199, 203, 223, 235, 243, 251, 307, 329, 557 | V (to 600) |
| p. 33 | 3067 collision pairs with S ≤ 600, 2793 joining strata whose least orders differ by ≥ 2 | 3067, 2793 | V |
| Table 1 | all 13 rows of first collisions | Identical | V |
| p. 46 | 1753 primitive pairs with S ≤ 600 | 1753 | V |
| Table 4 | rows k = 3, 4, 5 share S, R, Λ = 68/5, 68/5, 1849/120 | Exact | V |
| Table B1 | 83 triads | 83 | V |

**Overall.** Every number I could recompute from the printed data is correct, with two exceptions: the cond bound of 3.5 (cosmetic) and the interpretation of the "binding coefficient" (m1). The arithmetic and the Section 6 constants are well done. The problems are in how the eigenvalue computations are documented, how their error budgets are justified, how the benchmark is described, and how strong the blind test is.

---

## 4. MAJOR issues

### M1. The error budgets are not derived, and they do not follow from the stated eigenvalue errors (§7.1 p. 43; §7.2 p. 44; Fig. 5(b); Table 3; Remark 6.1)

The paper states:

- "for the first 500 eigenvalues it is at most 2.9×10^{−11} relative, and the coarser, conservative estimate at most 1.2×10^{−8}";
- an "error budget of 3×10^{−11}" for D(t) when t ≤ 0.03;
- an "error budget of 2.2×10^{−11}" in §7.2.

The paper never gives the formula that turns per-eigenvalue errors into a heat-trace budget. A worst-case propagation gives:

- δZ(t) ≤ Σ_j t λ_j ε_j e^{−λ_j t} ≈ ε·c_1/t (Weyl density 1/8);
- with ε = 2.9×10^{−11}: 2.4×10^{−9} at t = 0.0015 and 1.2×10^{−10} at t = 0.03;
- with the conservative ε = 1.2×10^{−8}: 10^{−6} and 4×10^{−8}.

These exceed the stated budget by factors of 4 to 3×10^4. Cancellation cannot be invoked:

- conforming Galerkin eigenvalues are upper bounds, so the discretisation errors share a sign;
- D(t) is a difference of two independently discretised spectra, so their errors need not cancel either.

The observed agreements (4×10^{−13}, 7×10^{−13}) show that the true errors are far below the stated bounds. In that case the stated bounds are not the quantities the budget is built from, and the paper must say what is. In addition:

- **Errors above index 500 are not reported.** The fine error estimate covers only "the first 500 eigenvalues". Nothing is said about eigenvalues 500–1440 of each triangle and BC, which carry about 2% of the weight of Σ λt e^{−λt} at t = 0.0015.
- **The error bars in Table 3 and on d_3, d_4 are undefined.** They are fit statistics plus a model-selection rule. The truncation error of a divergent asymptotic series is not bounded, and the paper does not say that these are not rigorous intervals.
- **"Certified" depends on these bars.** Table 3's "certified" and the abstract's "within their error budgets" both rest on them.

**To resolve:**

- give the budget formula explicitly, including how the per-eigenvalue estimates, the truncation tail and floating-point summation enter;
- tabulate the per-eigenvalue error estimate over the whole computed range (for example by index blocks), not just the first 500;
- define the error bars (1σ, 2σ, or worst case) and how they are computed;
- say plainly, in the abstract, §6.5 and the Table 3 caption, that the end-to-end recovery is certified conditional on non-rigorous error bars.

Alternatively, make the eigenvalue errors rigorous: Kato–Temple or Lehmann–Goerisch bounds, or residual-based enclosures in the manner of Strohmaier–Uski, are feasible at this scale.

### M2. The discretisation and convergence evidence are insufficient to reproduce or assess the spectra (§7.1 "Method" and "Validation", §7.2, Appendix C)

The whole method is one paragraph: "H¹ finite elements of order 10 on meshes of uniform hyperbolic size 0.05 … the geodesic side represented exactly … shift-invert Lanczos … overlapping spectral windows." Missing items:

- **Second discretisation.** The error estimate is "the difference between two independent discretizations", but the second one (h, p, mesh) is not specified.
- **Convergence evidence.** No table under h- or p-refinement is given for any eigenvalue, so the reader cannot see whether the difference estimate is asymptotically reliable. The relevant regime is λ ~ 2×10^4, which is about 8–9 nodes per wavelength at p = 10, h = 0.05.
- **Geometry.** In the Poincaré disc the geodesic side is a circular arc. "Represented exactly" needs explaining: is it exact blending, or order-10 isoparametric curving? (In the Klein model all sides are straight, at the cost of a non-conformal metric.)
- **Quadrature.** The quadrature order for the non-polynomial weight w = 4/(1−|z|²)² is not given, and quadrature error is a classical source of eigenvalue error at p = 10.
- **Corner regularity.** The treatment of the cone points is never discussed. Here it is benign: at a corner of angle π/m with pure N or pure D conditions, the eigenfunctions extend by reflection to smooth functions, so there are no singular functions and p-FEM should converge exponentially without grading. The paper should say this, because it is the reason p = 10 on a uniform mesh is appropriate.
- **Moduli family.** The Lambert-quadrilateral sectors include mixed corners; their regularity, and the discretisation used for that family, are not stated.
- **Eigensolver settings.** Shift-invert parameters (window placement, overlap, number of eigenpairs per window, tolerances), library versions, and the DOF count are not given.

**To resolve:** add a table (or appendix) of discretisation parameters for the minimal-pair spectra, the moduli family and the Bolza benchmark. Add a convergence table for a few representative eigenvalues (for example λ_1, λ_500, λ_1400 in each class) under p = 8, 9, 10, 11 or under h-refinement. Add a short paragraph on corner regularity.

### M3. A known eigensolver defect affects the main experiment, and the fix "has not yet been run" (§7.1 "Limitations", p. 44; Appendix C, p. 53)

The paper says the single-window slicing used for the minimal-pair spectra "can miss an eigenvalue at a window boundary", that only one of the four spectra was recomputed on a second machine, and that "A recomputation of all four spectra with the double-window solver … has not yet been run". The a-posteriori exclusion argument is weaker than stated:

- **The trace test has a blind band.** It detects a missing eigenvalue λ* only while e^{−λ* t_min} exceeds the noise. With t_min ≈ 0.0015 and an agreement of 7×10^{−13}, that means λ* ≲ 1.7×10^4, so missing eigenvalues in 1.7×10^4–2.4×10^4 are not excluded. (Such misses would also be harmless for the heat-trace conclusions, which should be said.)
- **The Weyl check is weak.** "The counting functions follow the two-term Weyl law … with residuals centred on zero, so no eigenvalue is missing or duplicated." A unit offset in N(λ) against fluctuations of size O(√λ) is not reliably detectable.

**To resolve:** run the double-window recomputation of all four spectra before publication, report the agreement, and either drop the "no eigenvalue is missing" claim or restrict it to the range the trace test actually covers.

### M4. The Bolza benchmark is misdescribed and too narrow (§7.1, p. 43)

The paper states: "The same code reproduces all 42 multiplicity-one eigenvalues below 998 of the Bolza surface listed by Strohmaier and Uski [34], which covers the (2,3,8) triangle orbifold, to 5.7×10^{−11} relative."

My independent FEM count on the (2,3,8) triangle gives 15 (Neumann, nonzero) + 6 (Dirichlet) + 11 + 10 (the two mixed classes) = 42. The figure 42 is therefore right, but:

- **Only half the list belongs to the orbifold.** The multiplicity-one Bolza eigenvalues are the four one-dimensional characters of the extended group. Only 21 of the 42 are eigenvalues of O(2,3,8) = N ∪ D. The other 21 require mixed boundary conditions that the paper's method (N ∪ D) never uses. The paper should say which boundary-condition classes were computed and how the 42 were matched.
- **The benchmark covers only the low end.** It reaches λ < 998, about 4% of the range used in the experiments (λ up to 23,800), where errors are largest. It is also a different triangle, with a different mesh and order that are not reported.
- **The reference is itself heuristic.** [34] rigorously bounds only λ_1, to 10^{−6}. Its other values have about 12 digits for the first 500, so "5.7×10^{−11}" is agreement close to the reference's own precision, not validation against a certified reference.

**To resolve:**

- correct the description (for example, "the 21 multiplicity-one eigenvalues below 998 that belong to O(2,3,8), and the 21 in the mixed classes");
- report the discretisation used;
- add a high-λ benchmark, such as the full Strohmaier–Uski list (about 1000 eigenvalues with multiplicities), or the Selberg/I+E trace test of the Bolza spectrum at small t with a geodesic sum, which [34] used for completeness;
- consider an independent method for at least a few eigenvalues of O(2,8,8) or O(3,3,12) (for example Hejhal's algorithm, or the method of [34] on the triangle-group quotient).

### M5. The blind-recovery experiment is weak by design, is not blind to the signature type, and its protocol cannot be assessed from the paper (§6.5 p. 41–42; Table 3; Appendix C)

- **The signature type was assumed.** Section 6 assumes "a hyperbolic sphere with a known number n of cone points", and the confirmation step enumerates "hyperbolic integer triads". So genus 0 and n = 3 were given to the pipeline. Only the labels A and B were blinded.
- **The discrimination is easy.** With c_1 and c_2 at the reported precision, R = 3/4 and S_1 = 18 are fixed, so the candidates are exactly the two triples whose c_3 differ by 25/12. The specimens' c_3 errors are 2×10^{−5} and 1.4×10^{−4}, about 10^4 below the separation. The test therefore exercises the arithmetic of the pipeline, not a hard inference.
- **The protocol is not documented.** "A protocol was committed before the pipeline code and before the result." The paper gives no commit identifier or timestamp, does not say who ran the pipeline or what they knew (the paper's subject is this very pair), and does not say what counted as failure in advance.
- **The certificate is conditional.** "Both recoveries pass the certificate of Proposition 6.10" is conditional on the heuristic error bars (M1).

**To resolve:**

- state precisely what was blinded and what was assumed (n = 3, g = 0, integrality);
- quote the protocol (or a hash and date) in the paper or the supplement;
- make the test signature-blind. This is cheap here. The estimated area π/2 admits only finitely many signatures in Sig: genus 0 with n = 3 (R = 3/4), or n = 4 (for example (0;2,2,2,4), whose c_2 = 31/48 is far from 67/48). Enumerating them, as Corollary 3.7/Theorem 3.8 permit with up to ⌊A/π⌋+4 = 4 coefficients, would turn the test into a genuine instance of Theorem 1.1;
- preferably add decoy specimens: other triangle orbifolds, a triple order such as (4,4,4) to exercise the Hölder-1/3 regime, and an n = 4 sphere;
- relabel Table 3's "certified" as "certified, conditional on the stated error bars".

## 5. MINOR issues

**m1 (p. 41, lines on Table 2).** The text says "the binding coefficient is c_3 … its required relative precision is about 7×10^{−4}. The coefficients c_1 and c_2 need only percent-level and 10^{−3}-level relative accuracy." Under the uniform model the extremal failure moves all three coefficients by the same δ, so 7×10^{−4} = δ_cert/|c_3| is a ratio, not a requirement on c_3. My computations for (2,8,8):

| Perturbation | Coefficient | First failure (relative) |
|---|---|---|
| Single coefficient | c_1 | 6.8% |
| Single coefficient | c_2 | **0.28%** |
| Single coefficient | c_3 | 0.93% |
| Relative model, joint | all three saturated | ε_up = 2.09×10^{−3} |

For (3,3,12) the joint relative failure is ε_up = 4.80×10^{−3}. So c_2, not c_3, is the most sensitive single coefficient, and c_3 alone tolerates about 1% relative error. **Fix:** rephrase, or give single-coefficient tolerances.

**m2 (p. 37).** "The exact cond is between 1 and 3.5 on every test multiset." For (2,2,2,2,3) I get cond = 3.5109. **Fix:** write "about 3.5" or "at most 3.52".

**m3 (p. 42).** "Differ by 0.21 and 0.26 standard errors." For c_2 I get 0.29 (quadrature) or 0.25 (linear), and c_1 cannot be checked from the printed digits. **Fix:** state the combination rule and print enough digits.

**m4 (Table 3; p. 43).** All six deviations from the exact values lie within 0.13–0.52 of the quoted bars (c_2, c_3 of A and B; d_3, d_4). If the bars were 1σ, the probability that the four Table 3 entries all fall within 0.4σ is about 1%. The bars are evidently conservative or not Gaussian. **Fix:** say what they are, and avoid "σ" language if they are not standard errors.

**m5 (p. 43).** "Agree … to 7×10^{−13} for t ≤ 0.03" needs a lower limit on t. The Weyl tail beyond the computed range is about 3×10^{−13} at t = 0.0015 and about 3×10^{−8} at t = 0.001. **Fix:** state the t-range and the size of the tail correction applied.

**m6 (p. 43).** "The counting functions follow the two-term Weyl law with constant c_2/2". For each triangle and boundary condition the law has three terms: area, ±perimeter and the constant c_2/2. My three-term estimates reproduce the counts (1421/1421 and 1420/1422). **Fix:** state the law used and the size of the residuals.

**m7 (p. 43).** "A missing eigenvalue below about 10^4 would show there at the level 10^{−7}". **Fix:** give the actual detectable range (about 1.7×10^4 at t_min = 0.0015) and its relation to the computed λ_max.

**m8 (p. 42).** "An error of order 10^{−4} in c_3 splits the double order 3". The c_3 error of specimen B is 5.5×10^{−5}. **Fix:** say "about 5×10^{−5}".

**m9 (§7.2).** Enumerating geodesics "in floating point up to length 6.5" is fine, but give the truncation estimate. Mine is about 10^{−14} at t = 0.33, which supports the 1.1×10^{−13} claim. Also say how the systole-minimising class is certified (4b(ϑ) is the shortest, not merely a short, geodesic).

**m10 (§7.1, "fit … with window and degree chosen to minimize …").** The paper does not give the selected degree, the weights, or whether the fit was in absolute or relative residuals. **Fix:** state them.

**m11 (§7.1).** "One of the four spectra was recomputed on a second machine and all 1434 eigenvalues agreed." **Fix:** say to what tolerance.

**m12 (Fig. 4(b)).** "Joined within each of the eight symmetry sectors" uses only eight ϑ values, so any crossings or avoided crossings drawn between the dots are interpolation artefacts. **Fix:** say so, or give a numeric table of λ_1..λ_5 per ϑ, which would also help reproducibility. My values for λ_1 at ϑ = 0, 0.8, 1.6, 2.8 are 4.12241, 2.14295, 1.10702, 0.43483.

**m13 (Remark 6.1 vs abstract).** The abstract's "Computed spectra confirm the predictions within their error budgets" should carry the qualifier in Remark 6.1 ("a-posteriori agreements, not enclosures").

## 6. Presentation issues

**p1 (§6.5 before §7).** The blind recovery uses spectra that are only described later. **Fix:** move §6.5 after §7.1, or forward-reference the method explicitly.

**p2 (Fig. 5(a)).** The panel has no t tick labels, so the reader cannot read off "≈ 0.1" or "0.34". **Fix:** share or label the axis.

**p3 (Table 3).** The "roots" row mixes formats ("8 ± 0.0050i" next to "11.99995"). **Fix:** use consistent digits, and give the error bars' meaning in the caption.

**p4 (§7.1).** Undefined terms: "conservative estimate", "coarser", "error budget" and "noise". **Fix:** define each once.

**p5 (Appendix C).** The software versions for NGSolve, NETGEN and ARPACK are only "in the repository". **Fix:** list them in the paper, since a reader cannot otherwise reproduce the computation as written.

**p6 (§7.1).** "H¹ finite elements of order 10" does not say what kind of basis is used. **Fix:** specify, for example hierarchical H¹ of polynomial degree 10.

**p7 (Fig. 9).** Diamonds for different curves overlap near δ ≈ 10^{−3}. **Fix:** offset them or enlarge the inset.

## 7. Recommendation

**Major revision.** Confidence: **medium-high** for the numerical aspects; I defer to the other referees on Sections 3–5 and 8, beyond the enumerations I re-ran.

The mathematical content is substantial and well checked. Every formula, constant and threshold I could recompute is correct, including:

- all δ_thm values;
- the constructed failures δ_up for the triangle cases;
- the blind-recovery roots;
- the Section 5 and 8 counts up to S = 600;
- the moduli-family systoles and λ_1.

The numerical experiments are plausible, and my independent computations agree with every value I could test. They are not, however, documented well enough for a reader to reproduce them from the paper. In particular:

- the error budgets are asserted rather than derived, and are inconsistent with a worst-case use of the stated per-eigenvalue errors (M1);
- the convergence evidence and discretisation details are missing (M2);
- an acknowledged solver defect is left unremedied (M3);
- the Bolza benchmark is misdescribed (M4);
- the blind test is easy and only partially blind (M5).

None of these threatens a theorem, because the computations are not used in proofs. All of them are fixable without new mathematics.

---

*Saved by the coordinating session: this subagent could not write files, so the report came back as text and was saved verbatim. The coordinator removed only the hand-back note addressed to itself.*
