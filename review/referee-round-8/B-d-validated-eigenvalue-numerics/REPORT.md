<!-- Round 8 B-d referee report: returned text saved verbatim; the reviewer could not write files -->

Writing `REPORT.md` was refused, so the full report is below. I recommend **major revision**, with high confidence for my part of the paper. I found no fatal issue: every number I recomputed agrees with the manuscript. The major points are about what is left uncertified and how it is framed, not about errors.

# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (AGAG)

**Remit:** Section 7 (the a-posteriori test), and every numerical claim, table and figure in the paper: what is certified, what is only estimated, and whether the numerical claims are stated honestly. The marked placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifiers) are treated as known.

## 1. Summary

The paper's main result is Theorem 6.2 (stated as Theorem 1.1). Fix an area bound A, a systole bound ε and an order bound M. Then the first N eigenvalues, each known to within δ, determine the signature, with N and δ given by explicit formulas. These numbers are huge (Table 3).

The tool is the heat trace written through the Selberg trace formula. It splits into a signature term G_σ, a positive closed-geodesic term, and an eigenvalue tail.

Two further results follow:
- **Corollary 6.3** evaluates the gap between signature terms numerically.
- **Theorem 7.1** (= Theorem 1.2) is an a-posteriori test on finite lists of eigenvalues.

The test is run on ten computed spectra: O(2,8,8), O(3,3,12) and eight members of the (0;3,3,3,3) family. For these:
- eigenvalues come from high-order FEM, with error *estimates* only;
- systole lower bounds are *certified* in interval arithmetic;
- diameter bounds are proved;
- completeness of the lists is supported by evidence, not proved.

Section 8 gives the O(2,3,m) counterexample and Fig. 3.

## 2. Significance

Theorem 6.2 is a reasonable effectivisation of a compactness argument, at the level of the signature.

Theorem 7.1 is short and natural from a numerics viewpoint. It is the Strohmaier–Uski trace-formula completeness check, inverted to discriminate between signatures.

The ten examples are illustrations only. The signatures are known by construction, the errors are estimated, and completeness is assumed; the paper says all of this (abstract, p. 3, p. 18 items (i)–(v), p. 22).

The most informative number is N_obs = 3 for both triangles (p. 22). The rigorous-style counts in Table 6 (18 to 847) mostly measure how crude the closed-geodesic bound is (see M4). So Theorem 1.2 is promoted to a headline theorem, yet its application determines nothing rigorously.

## 3. Correctness, and what I recomputed

All recomputation used the manuscript only, with Python, mpmath, SciPy and scikit-fem.

### 3.1 Proofs checked line by line

- **Lemma 2.2.** Both parts re-derived and correct: the integration by parts, the range t ≤ ℓ²/(2(1+ℓ)), and the all-t bound (maxima at 2√t and 6t).
- **Proposition 2.3.** Verified against 30-digit quadrature at (m,t) = (8, .05), (12, .0412), (3, .002), (12, 1), with K = 0..5. The remainder always has sign (−1)^K and modulus at most |b_K(m)| t^K.
- **Coefficients.** α₀..α₄ = 1, −1/3, 1/15, −4/315, 1/315. a₀..a₃ = 1/12, 1/360, 1/2520, 1/10080. d₃ = 25/12 and d₂ = −1/12. All correct.
- **Lemmas 4.2, 4.3, 4.5, Theorem 4.4, Lemma 5.1, Proposition 5.2.** Checked and correct.
- **Lemma 6.1 and Theorem 6.2.** All inequalities hold, including the y₀ formula, Θ* ≤ 1/8 ⇒ Λt* ≥ 2 log 64, and the 3/8 versus 5/8 margin.
- **"Θ ≤ 8" in Corollary 6.3.** It is intentional and sufficient; it is not a typo.
- **Theorem 7.1.** The proof is correct, and (C2) ⇒ (C1) holds.

### 3.2 Recomputed numbers

**Table 2.** All 12 entries reproduce.

**Table 3.** All 8 rows × 11 columns reproduce, including the binding constraint (N = 3.4e8, 6.82e9, 43188, 43188, 7.44e12, 2.28e6, 1.08e6, 3.75e30). The side claims also reproduce:
- C* ∈ [4.0e5, 7.1e10];
- N = 4.19e18 if k* = 14 at A = 10π;
- growth factors per halving of ε of 5.24 → 4.81.

**Table 4.** Systole closed forms, 4b for the family, diam P (2.44845 … 3.88487), the rounding of 2 diam P, and C* (3.55e9, 4.01e5, 9.45e9) all check. |S| = 6, 3, 10 and |Sig(π/2, 12)| = 48.

**Table 5, independent FEM check.** I used P3 elements on an isoparametric quadratic mesh in the disc model.
- O(3,3,12): my first 14 eigenvalues agree to all printed digits.
- O(2,8,8): agreement to 2–5e−7 relative, limited by my mesh.

**Trace check at moderate t.** At t = 0.08–0.15 the tail beyond λ̃₄₀ is negligible (under 2e−11). There, Σ_{j≤40} e^{−λ̃_j t} − G_σ(t) equals the contribution of 2.00 systole-length classes, to 3–4 digits. This independently confirms three things: the trace-formula normalisation, the systoles, and low-end completeness.

**Table 6, triangle rows.** Re-run from the Table 5 data alone, with the grids of p. 21. Every count reproduces:

| | (C1),Δ | (C2),Δ | (C1),C* | (C1),Sig(A,M) |
|---|---|---|---|---|
| O(2,8,8) | 18 (0.0565) | 20 (0.0556) | 24 (0.0433) | 24 |
| O(3,3,12) | 25 (0.0414) | 29 (0.0401) | 36 (0.0294) | 36 |

No wrong signature is ever singled out for N ≤ 39.

**Robustness claim (v).** r = 1e−3 leaves the counts unchanged. r = 1e−2 gives 21 for O(2,8,8); for O(3,3,12) nothing passes up to N = 39, which is consistent with the stated 43.

**Corruption experiment (iv).** Reproduced exactly: **19 of 24** corruptions give a wrong first answer. All 24 corrupted lists reach an (N, t) where no signature passes, by N ≤ 30. One case is notable: O(3,3,12) with λ̃₁₂ duplicated is first accepted as its heat-invariant twin O(2,8,8).

**Other Section 7 checks.**
- N_obs = 3 for both triangles.
- The gap "at least 2.96e−3" on p. 20 is 2.9686e−3.
- The cut-offs 1.66e4 and 9.8e3 follow from the stated budgets.

**Corollary 6.3.** These N are "the best time of a grid", so they depend on the grid; the differences are within about 2%:

| Class | Paper | Mine |
|---|---|---|
| π/2, M = 8 | 244 | 244 |
| π/2, M = 12 | 283 | 282 |
| 4π/3, M = 3, ε = 2.63 | 139 | 139 |
| 4π/3, M = 3, ε = 0.69 | 2605 | 2578 |
| 4π/3, M = 12 | 7415 | 7445 |
| 2π, M = 3, ε = 0.1 | 3.9e5 | 3.82e5 |

**Section 7.2 and the Fig. 2 caption.** Every ratio quoted there checks.

**Section 8.**
- ℓ₂,₃ = 0.5620668…, 0.983986 and 1.92484 check.
- Garbin–Jorgenson condition (a) holds exactly from m ≥ 13.
- Fig. 3(b): λ₁ rescales to 1.345 at m = 7 and 1.163 at m = 4096, consistent with the "6–16%" statement.

## 4. FATAL

None.

## 5. MAJOR

**M1. Section 7 certifies nothing, although for the triangle orbifolds a rigorous version is cheap (pp. 17–22).**

By experiment (v), the counts survive relative errors of 1e−3. The test needs only λ̃₀..λ̃₃₆ (eigenvalues below about 290). A rigorous version could go as follows:
- In the Klein model the geodesic triangle is an exact polygon. Conforming FEM with interval assembly then gives rigorous upper bounds, with no geometric error.
- Index-wise lower bounds come from Liu's framework for self-adjoint operators (2015, extending [37]), Carstensen–Gedicke [38], or Lehmann–Goerisch.
- Index-wise lower bounds also give completeness up to index N. That removes the hypothesis that produced 19 wrong answers in 24.
- G_σ is a one-dimensional integral, so validated quadrature is trivial.

*Resolution:* either do this for O(2,8,8) and O(3,3,12), which yields two proved determinations, or demote Theorem 1.2 to a remark and say in the abstract that no determination in the paper is proved.

**M2. Corollary 6.3, the only practically sized N, is uncertified and its δ is never reported (pp. 2, 14, 22).**

An interval enclosure of the minimal gap over the 48 signatures of Sig(π/2, 12), at one rational t, is easier than the systole certification already done. With it, "283 eigenvalues to accuracy δ suffice for C(π/2, 1.8626, 12)" becomes a practical theorem.

From my recomputation, δ is about:

| Class | δ |
|---|---|
| π/2, M = 12 | 4.8e−5 (Θ = 7.3e−3, t = 0.0247) |
| π/2, M = 8 | 1.2e−4 |
| 4π/3, M = 3, ε = 2.63 | 5.9e−4 |
| 4π/3, M = 3, ε = 0.69 | 4.9e−4 |

*Resolution:* certify the gap, report δ beside every N, and state the time grid.

**M3. "A finite procedure that decides" (pp. 4, 15) is effective only in principle.**

Table 3, row 2 requires 6.8e9 eigenvalues, each to absolute accuracy 4.2e−25, and G_σ(t*) with about 31 significant digits. The 10π, M = 12 row requires 3.8e30 eigenvalues to accuracy 1e−278. On p. 15, "cost grows with log(1/Θ*)" is misleading: the dominant costs are N and δ.

*Resolution:* reword, add one sentence saying these inputs are far beyond any eigenvalue solver, and point to a certified Corollary 6.3 as the practical version.

**M4. A closed-geodesic bound about 10⁷ times too large drives the counts and their interpretation (pp. 21–22, Remark 6.4(c)).**

For O(2,8,8) at t = 0.0562:
- the bound H is 6.9e−3, the largest term of E_N;
- the true hyperbolic term is about 3e−10 (two systole classes).

The authors already have a certified enumeration of every geodesic of length ≤ 4 but don't use it. Two claims in Section 7.2 therefore reflect the crude H, not the spectra:
- "knowing the geometry changes counts little";
- "data account for a factor 6–12".

*Resolution:* use the exact enclosed sum up to L = 4 plus the count bound above it, and report the new counts. Otherwise, qualify those claims and state the size of the overestimate.

**M5. The completeness evidence is heuristic, and the paper's own experiment shows that completeness decides the outcome (pp. 18, 20).**

The evidence is one trace check at t = 0.0015 (with a Weyl-law tail *estimate*), agreement between window runs, and agreement of eigenvalue counts between discretisations. None of these detects a missing eigenvalue paired with a nearby spurious one.

The stop-when-inconsistent protocol is validated only on 24 synthetic corruptions. The Sylvester inertia counts are mentioned but not reported.

*Resolution:* report the inertia counts, label the protocol heuristic, or do M1.

## 6. MINOR

- **m1 (p. 16, Fig. 1).** The text implies N = 21 is needed on the figure's grid. On that grid, with s = kt/20, I find N = 20 already passes at t = 0.0562: E₂₀ = 0.01988 against a half-gap of 0.02035, a 2% margin. Reconcile, or state the exact s-grid and H used.
- **m2 (p. 17).** The diameter count C = πe^{3Δ}/Area(O) needs Area(O) or a lower bound for it. When only A is known, name the lower bound used (π/21, or the minimum over S).
- **m3 (pp. 18, 21).** E_N omits the floating-point error in Σ e^{−λ̃t} and the quadrature error of G_σ. Include them or say they are omitted.
- **m4 (p. 20).** ϵ_j is the difference between two comparable discretisations, not an asymptotic error estimate. Reword or justify. My independent check supports about 1e−7 accuracy.
- **m5 (p. 20).** Add one sentence on why the pruned breadth-first search reaches every tile meeting the ball (the tiles meeting a convex ball are edge-connected). Add one on classifying hyperbolic versus elliptic elements by trace intervals bounded away from ±2.
- **m6 (p. 12).** The values are 3.4e196 and 2.4e29325, but the text says "10¹⁹⁶ to 10²⁹³²⁶": the exponents are rounded in opposite directions.
- **m7.** "Geometric middle" in the Table 6 caption versus "middle" on p. 21: unify.
- **m8 (p. 22).** The definition of N_obs should say that a single t serves every N′ ≥ N.
- **m9.** The abstract and pp. 3–4 say "the same theorem gives 10²–10⁴". Those numbers come from Corollary 6.3 with a computed gap, not from Theorem 6.2.
- **m10.** Corollary 6.3 should be compared only with the Sig(A,M) column of Table 6. The "factor 6–12" claim mixes columns.
- **m11.** Suggestion: add the moderate-t trace check of §3.2 (two systole classes reproduced to 4 digits). It checks low-end completeness and does not depend on any tail estimate.
- **m12 (p. 26, Fig. 3).** Give the discretisation parameters for m up to 4096. The thin cone region needs anisotropic meshes.

## 7. Presentation

- **P1.** Figs 1 and 2 have no legend; the coding is explained only on pp. 16 and 22.
- **P2.** N means two different things (the number of eigenvalues used, versus the tail index with N+1 used). The paper flags this three times. Use one convention.
- **P3.** Symbols are overloaded: ε / ϵ_j / ϵ, δ / δ_k / δ, and Θ / θ.
- **P4.** Theorem 1.2 restates Theorem 7.1 almost verbatim.
- **P5.** Add a λ̃_N column to Table 6.

## 8. Recommendation

**Major revision**, high confidence for my part. The mathematics I checked is correct, every recomputed number agrees, and the honesty of the numerical claims is exemplary; items (i)–(v) on p. 18 are a model of how to state computed evidence.

What holds the paper back:
- The only practically sized results are left uncertified, although certifying them is cheap (M1, M2).
- The effectivity wording overstates what can be executed (M3).
- The interpretation of the counts reflects a crude bound (M4).
- Completeness, which the paper's own experiment shows is decisive, rests on heuristics (M5).

I would accept the paper after text changes on M3 and M4 plus the demotion of Theorem 1.2. Certifying Corollary 6.3 and the triangle test would make it clearly stronger.

## 9. What resolves each issue

| Issue | What resolves it |
|---|---|
| M1 | Certified enclosures with index-wise lower bounds for the two triangles, or demote Theorem 1.2 and change the abstract |
| M2 | Interval-certified gap; δ reported beside every N; time grid stated |
| M3 | Reword, add the infeasibility sentence, fix the cost remark on p. 15 |
| M4 | Use the enumerated geodesics up to L = 4, or qualify the Section 7.2 claims |
| M5 | Inertia counts reported; protocol labelled heuristic; or M1 |
| m1–m12, P1–P5 | As stated in each item |

---

My scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/B-d-validated-eigenvalue-numerics/scratch/code/`:
- `consts.py`: Tables 2–3
- `gsig.py`: G_σ and the signature sets
- `test71.py`: Table 6 and the robustness claim
- `corrupt.py`: experiment (iv)
- `cor63.py`: Corollary 6.3
- `fem.py`: independent eigenvalues
