<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (Annals of Global Analysis and Geometry)

Writing REPORT.md was refused, so this message is the full report. My scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/B-c-prime-geodesic-analyst/scratch/code/`.

Referee coverage: Sections 2, 3, 5 and 6 (the heat trace and its expansion, the heat invariants of a signature, counting eigenvalues, and Theorem 6.2 with Lemma 6.1 and Table 3), together with every lemma they use. Sections 4, 7 and 8 come in only where Section 6 depends on them (the diameter bound D of Theorem 4.4 enters t₃).

## Summary

The paper considers closed orientable hyperbolic 2-orbifolds with area at most A, systole at least ε and cone orders at most M. It proves (Theorem 6.2, announced as Theorem 1.1) that the first N eigenvalues, each known to within δ, determine the signature. N and δ are given in closed form. The decision rule picks the σ in Sig(A,M) that minimises |Σ_{j<N} e^{−λ̃_j t*} − G_σ(t*)|, where G_σ is the identity-plus-elliptic part of the Selberg trace formula for the heat kernel.

The proof has four steps:
1. **Gap at the first differing invariant.** At the first heat invariant where two signatures differ, the difference is bounded below by an explicit lattice constant (Lemma 3.3): 1/(2·lcm(1..M)) when the areas differ, and a_{k−2} = |B_{2k−2}|/(2(k−1)!(2k−3)) when they are equal. The index of that invariant is at most k* = min(⌊A/π⌋+4, M) (Theorem 3.2, imported).
2. **Lower bound for |G_σ − G_σ′|.** Enveloping remainders (Proposition 2.3, imported) turn this gap into |G_σ(t) − G_σ′(t)| ≥ Γ(t) for t ≤ t₁ (Lemma 6.1).
3. **Hyperbolic term.** Hyp(t) is bounded through a closed-geodesic count with factor e^{3·diam} (Lemma 2.2, imported in part). Together with the diameter bound D(A,ε,M) this keeps Hyp below Γ/8 for t ≤ t₃.
4. **Tail.** A Chernoff-type count, #{λ ≤ x} ≤ e·Z(1/x) (Proposition 5.2), controls the eigenvalues beyond the N-th.

Section 7 gives an a-posteriori test and Section 8 shows that the bound on the orders cannot be dropped. Both are outside my coverage except where noted.

## Significance

**What is good:**
- Within my sections the paper is careful and honest. Every constant is explicit.
- Table 1 is a clear ledger of what is imported from the companion.
- The proofs that are actually given (Lemma 2.2, third bound; Lemma 3.3; Lemma 5.1; Proposition 5.2; Lemma 6.1; Theorem 6.2) are correct. I checked each line.
- The numerical tables agree with the formulas to the printed precision (see below).
- The authors say plainly that the rates in ε and M are artefacts of the method and not properties of the problem.

**The mathematical content of Sections 2–6 is modest.** Without constants the statement is a compactness triviality, as the authors themselves note on p. 2–3. With constants it is a careful assembly of standard pieces:
- an explicit asymptotic expansion that envelopes the truth,
- an integrality gap,
- a crude geodesic count,
- a Chernoff tail bound.

The real input, that finitely many heat invariants (at most k*) separate signatures, is Theorem 3.2. It is imported without proof from an unrefereed companion submitted at the same time.

**The effective constants have no practical value.** N runs from 4.3×10⁴ to 3.8×10³⁰ and δ from 1.5×10⁻⁹ to 8.7×10⁻²⁷⁸ (Table 3). Part of this size comes from a factor e^{3D} that the method does not need (M2).

For AGAG the paper is publishable only if the dependence on the companion is resolved, and in my view only if the hyperbolic-term bound is brought to the standard that an "effective" paper should meet. As a whole, the paper's interest rests more on Theorem 1.3 / Section 8 and on the test of Section 7 than on Theorem 6.2.

## Correctness and what was recomputed

All computations used mpmath at 30–160 digits, and exact rationals where possible.

**1. Trace formula normalisation (Theorem 2.1).**
- I checked that ĝ_t is the Fourier transform of g_t.
- I checked that E_m(t) → (m²−1)/(12m) = b₀(m) as t ↓ 0. This is the known cone-point invariant (1/12)(m − 1/m).
- I checked that I(t)·4π/Area ~ t⁻¹(1 − t/3 + t²/15 − 4t³/315 + …), as in McKean.

The normalisation of the elliptic term is therefore the one under which each of the m−1 nontrivial rotations about a cone point is counted once. **Agreed.**

**2. Heat coefficients b_l(m).**
- I computed b_l(m) two ways: from the paper's formula through the Taylor coefficients φ_k of Φ_m, and as moments b_l = ((−1)^l/l!)∫(r²+1/4)^l w_m(r) dr of the elliptic weight w_m. The two agree to 15+ digits for m = 2, 3, 7, 12 and l ≤ 5.
- α₀, …, α₅ = 1, −1/3, 1/15, −4/315, 1/315, −1/866.25. These agree with the paper's α₀, …, α₃.
- a₀, …, a₄ = 1/12, 1/360, 1/2520, 1/10080, 3.507×10⁻⁵. **Agreed.**

**3. Enveloping remainders (Proposition 2.3, imported).**
- Cone part: tested for m ∈ {2, 3, 8, 12, 14}, K ≤ 12 and t ∈ [10⁻⁵, 3]. The sign (−1)^K and the bound |b_K| t^K held in every case.
- Area part: tested for K ≤ 14 and t ∈ [10⁻⁶, 5]. It held in every case. Apparent failures at t = 10⁻⁶ at 30 and 80 digits were cancellation artefacts and disappeared at 160 digits.
- Strict monotonicity of |b_K(m)| in m: checked for K ≤ 13 and 2 ≤ m ≤ 16.

Part (a) in fact has a two-line proof, given under m3. **Agreed (numerically).**

**4. Lemma 2.2, hyperbolic-term bound.**
- From the counting bound n_O(x) ≤ πe^{x+3 diam}/Area, I re-derived B(ℓ, diam, t) by Stieltjes integration. With f(x) = x e^{−x/2−x²/4t}, the condition t ≤ ℓ²/(2(1+ℓ)) is exactly what makes f′ < 0 on [ℓ, ∞).
- Then ∫(−f′)e^x = ℓe^{ℓ/2−ℓ²/4t} + ∫_ℓ^∞ x e^{x/2−x²/4t} dx ≤ ℓe^{ℓ/2−ℓ²/4t}(1 + 2t/(ℓ−t)), which is the stated B. I confirmed this numerically for three (ℓ, t) pairs; the closed form exceeds the integral, as it should.
- The monotonicity of B in ℓ on the range follows from ℓ/2t ≥ 1 + 1/ℓ.
- The third (all-t) bound is correct as written: the maxima at x = 2√t and x = 6t are right, and the factor 2√π e^{3 diam}/(Area(1−e^{−ℓ})) follows.
- I also reconstructed the imported counting bound: take a Dirichlet domain centred at a non-elliptic base point; it lies inside the ball of radius diam; every class has a representative moving the base point by at most x + 2 diam. This gives n_O(x) ≤ 2π(cosh(x+3 diam) − 1)/Area. **Agreed.**

**5. Lemma 3.3 and Theorem 3.2.**
- d₂((0;4,4,4), (0;3,4,6)) = −1/12 exactly.
- d₃((0;2,8,8), (0;3,3,12)) = 25/12 = a₁·750 exactly, matching Fig. 1.
- The proof of Lemma 3.3 is correct given Lemma 3.1 and the triangular expansion.
- Theorem 3.2 (imported): I brute-forced all 654,505 hyperbolic signatures with s ≤ 2 (area ≤ 4π) and orders ≤ 60, using the exact-rational criterion of Lemma 3.1. There were no violations of (i) or (ii). The largest first-difference index found was 4, against the bound ⌊A/π⌋+4 ≤ 8.
- Part (ii) has a self-contained proof (see m4). **Agreed.**

**6. Lemma 5.1 and Proposition 5.2.**
- The case analysis for Area ≥ π/21 is correct; the minimisers are (2,3,7), (2,4,5), (3,3,4), (2,2,2,3), (2,5,5), …
- n + 4g ≤ Area/π + 4 holds.
- **Counting estimate.** For O(2,8,8), with the 41 eigenvalues of Table 5 and G_σ (a lower bound for Z_O) evaluated by quadrature, #{λ ≤ x} against e·G_σ(1/x) gives 8 vs 20.6 (x = 50), 14 vs 37.7 (x = 100), 26 vs 71.7 (x = 200) and 39 vs 105.7 (x = 300). The Weyl values are 6.25, 12.5, 25 and 37.5. The bound holds and loses about the factor e, as expected. **Agreed.**

**7. Lemma 6.1 and Theorem 6.2.**
- I checked every inequality. In particular:
  - 1 + 2t/(ε−t) ≤ 3 on t ≤ t₂;
  - the factor 63 = 21·3;
  - B* increases on (0, t₂] because t₂ ≤ ε²/2;
  - y₀ follows from e^{−y/2}y^p ≤ (2p/e)^p;
  - Λt* ≥ 1;
  - the tail estimate e^{−Λt*/2}Z♯(t*/2) = Γ*/8;
  - the perturbation term Nt*δ = Γ*/(8e);
  - the final margins: below 3Γ*/8 for σ₀ and above 5Γ*/8 for every other σ.
- **The proof is correct.**

**8. Table 3: all eight rows recomputed from the printed formulas.**
- I computed D (Theorem 4.4), t₁, t₂, t₃, Γ*, Λ, N and δ for every row.
- Example, row 1: D = 402.0, t₁ = 1.14e−7, t₃ = 3.54e−4, Γ* = 2.59e−18, Λ = 1.0e9, N = 3.40e8, δ = 3.07e−21.
- Example, row 8: t₁ = 2.5e−27, t₃ = 1.85e−6, Γ* = 1.77e−272, Λ = 5.52e29, N = 3.75e30, δ = 8.65e−278.
- The binding constraints are t₁, t₁, t₁, t₃, t₁, t₃, t₃, t₁, as printed.
- **All entries agree to the printed rounding.**

**9. Other numerical claims in Section 6.**
- "N from about 4×10¹⁸ to 1.1×10⁷" (A = 10π, M = 3, k* forced to 14): I get 4.19×10¹⁸. **Agreed.**
- The Theorem 6.2 column of Table 6: I get 4.49e4, 6.79e4, 1.03e5, 1.57e5 and 2.41e5 for ϑ = 0.8, …, 2.4 at M = 3; 7.4e12 for the family at M = 12; and 6.8e9 for the triangle orbifolds. **Agreed.**
- "Factor of about 9 per halving of ε, decreasing towards 8": the successive ratios are 9.03, 8.94, 8.86 and 8.79. **Agreed.**
- ε < 0.42: arccosh(1 + 2/(9π²)) = 0.2119, so the threshold is ε < 0.4238. **Agreed.**

**10. Figure 1.**
- I recomputed |G_{(0;2,8,8)} − G_σ| for the five competitors (the area-π/2 signatures with orders ≤ 12 are (2,6,12), (3,3,12), (3,4,6), (4,4,4) and (2,2,2,4); |S| = 6 is correct).
- At t = 10⁻³: 0.164, 0.0020, 0.415, 0.498, 0.747. At t = 1: 0.025, 0.029, 0.113, 0.137, 0.248.
- These match the rendered curves (p. 14), including the black (3,3,12) curve crossing above the lightest grey one near t = 1.
- The Lemma 2.2 dashed curve is about 9×10⁻⁴ at t = 0.05 and about 10² at t = 0.1, consistent with the plot.

**Taken from the companion without proof** (Table 1, p. 5):
- Theorem 2.1;
- Lemma 2.2, first two statements;
- positivity and monotonicity of φ_k (Lemma 2.6 there);
- Proposition 2.3;
- the structure of p_l, including the triangular expansion with a_{l,l+1} = a_l;
- Lemma 3.1;
- Theorem 3.2.

The marking is clear and accurate: Table 1, the sentence on p. 6, and citations inside each statement. Whether the dependence is acceptable is discussed in M1.

## FATAL

None. I found no false statement and no unsupported step in Sections 2, 3, 5 and 6, assuming the imported results. The imported results that I could test held in every test.

## MAJOR

**M1 (pp. 5–8; Table 1, Theorem 2.1, Lemma 2.2, Proposition 2.3, Lemma 3.1, Theorem 3.2): the main theorem rests on unrefereed results imported without proof.**
- Theorem 6.2 cannot even be stated without Theorem 3.2: k* defines t₁, Γ and p.
- Lemma 6.1 needs Proposition 2.3 for every t ≤ t₁, and the monotonicity of |b_K(m)| in m.
- t₃ needs the counting bound of Lemma 2.2.

None of these is proved here, and the companion [28] is a preprint submitted at the same time. Clear marking is necessary but not sufficient: as it stands a reader of this journal cannot verify the main theorem from refereed material. Most of the imported statements have short proofs (m2–m4), and the authors should include them. Only Theorem 3.2(i) and Proposition 2.3(b) need any real space. Theorem 6.2 remains true with k* = M if only Theorem 3.2(ii) is used, so the dependence on part (i) could be confined to a remark on improved constants.

**M2 (p. 6 Lemma 2.2; p. 10–11 discussion; p. 12 Theorem 6.2, definition of y₀ and t₃): the factor e^{3D} in the hyperbolic-term bound is not needed, and the paper's claim that removing it "does not transfer directly" to orbifolds is unfounded.**

Lemma 2.2 counts classes from a single base point, which costs e^{3 diam}. With D = 151 to 2.25×10⁴, that factor alone (e^{453} up to e^{6.75×10⁴}) makes t₃ ≈ ε²/(24D) where it binds (rows 4, 6, 7). Through e^{3D} with the class-level D, it is also why the class-level test of Section 7 fails within the computed range for most of the examples.

A standard net argument gives n_O(x) ≤ C(A,ε,M)·e^x with C polynomial in A, M and 1/v₀, with no diameter at all. The argument uses only Lemmas 4.2–4.3, which the paper already has:
- Take as a net all cone points (at most n* of them), together with a maximal 2r₀-separated set among the points at distance ≥ r₀ from the cone points (at most A/v₀ points).
- By the proof of Lemma 4.3, every net point q̃ is displaced by at least 2ρ₁ by every element outside its stabiliser (order ≤ M).
- So #{γ : d(q̃, γq̃) ≤ R} ≤ M(cosh(R+ρ₁) − 1)/(cosh ρ₁ − 1).
- Every closed geodesic passes within 2r₀ of a net point, so its class has a representative with R ≤ x + 4r₀.

My rough estimate for row 7 (10π, 1, 3) is that this moves t₃ from 3.7×10⁻⁵ to about 5×10⁻³. Then t₁ binds, and N falls from 1.1×10⁷ to below 10⁶. Row 6 gains similarly. These are my estimates, not the paper's. This is not an error, but the effective constants are the paper's entire contribution over compactness. The authors should either adopt this count, which makes Theorem 4.4 unnecessary for Theorem 6.2, or withdraw the statement on p. 11 and explain why they keep e^{3D}.

## MINOR

**m1 (p. 6, after Theorem 2.1).** The text says the trace formula is extended "by a standard approximation argument" and then that ĝ_t is "admissible for the trace formula as stated". These contradict each other. The Gaussian satisfies the usual admissibility conditions directly (even, holomorphic in |Im r| ≤ 1/2 + η, decaying faster than (1+|r|)^{−2−η}), so no approximation is needed. Normalisations of the elliptic term differ across [31, 32]: some sum over primitive classes and powers, some symmetrise to cosh((π−2θ)r)/cosh(πr). Please state explicitly that the j-sum counts each nontrivial element of the stabiliser once, and give the check E_m(0⁺) = (m²−1)/(12m).

**m2 (p. 6, Lemma 2.2).** Include the three-line proof of the counting bound sketched in item 4 above: a Dirichlet domain at a non-elliptic base point, contained in the ball of radius diam. Please also state that the bound counts oriented classes, as Hyp does.

**m3 (p. 7, Proposition 2.3(a)).** Prove it here. Since w_m(r) > 0, E_m(t) = ∫_{[1/4,∞)} e^{−ts} dν_m(s) with ν_m ≥ 0 the image of w_m(r) dr under s = r² + 1/4. The Taylor remainder of e^{−ts} is then enveloping, and b_l = ((−1)^l/l!)∫s^l dν_m; I checked this identity numerically. Monotonicity of |b_K| in m is immediate from p_K, because |b_K(m)| = 4^{−K}Σ_k (2k)!/(k!(K−k)!) φ_k(m) is a positive combination of the φ_k. For (b), note that 4π I/Area = ∫_{1/4}^∞ e^{−ts} tanh(π√(s−1/4)) ds has infinite mass, so the enveloping is not automatic. Give the proof or a precise pointer.

**m4 (p. 8, Theorem 3.2(ii)).** Here is a self-contained proof. By Lemma 3.1 with L = M, the vector x_m (m = 2..M) of differences in multiplicities satisfies Σ_m x_m ψ_k(m) = 0 for k = 1..M−1. The matrix ((m^{2k}−1)/m) is nonsingular: up to the column factors 1/m, its determinant is the Vandermonde determinant of the nodes 1, 2², …, M². So x = 0, and then c₁ fixes g. Include it.

**m5 (p. 8, Lemma 3.3(ii) and p. 12, Lemma 6.1).** A is used both for the class bound and for the common area. In Lemma 6.1 the bound actually used is k ≤ ⌊Area(σ)/π⌋ + 4 ≤ n*; say so.

**m6 (p. 12, δ₁ = 1/(2·lcm(1..M))).** For M = 12 this is 1.8×10⁻⁵, and it is γ*, so it fixes Γ*. The least nonzero |d₁| over the finite set Sig(A,M) can be computed exactly and is much larger: the true gaps are of order 1/(M(M−1)), e.g. (2,3,11) against (2,3,12) gives 1/264. Similarly, Γ(t) = ½γ* t^{k*−2} could keep the individual δ_k t^{k−2}. These change only logarithms in N, but the paper advertises explicit constants.

**m7 (p. 12, proof of Theorem 6.2).** Hyp ≥ 0 and the tail enters with a minus sign, so |Z̃ − G_{σ₀}| ≤ max(Hyp, tail) + perturbation. This gains a factor of about 2 in the margin at no cost. In ϖ, Area ≥ π/21 can be replaced by min Area over Sig(A,M), which is π/3 for M ≤ 6, for example.

**m8 (p. 13, paragraph after the proof).**
- "Any rational t ≤ t* may replace it" is true only if Γ*, Λ, N and δ are recomputed from t. With the stated Λ and N, the tail bound at a smaller time t gives e^{−Λt/2}Z♯(t/2), which is not ≤ Γ(t)/8. Say this explicitly.
- The truncated-expansion remark ("We do not prove that such a K exists") adds nothing to the theorem. Either prove the claim or remove it.
- If the rule is to be called computable, cite or give a rigorous quadrature error bound for the E_m integrals.

**m9 (indexing).** Theorem 6.2 uses λ̃₀, …, λ̃_{N−1}; Theorems 1.2 and 7.1 use λ̃₀, …, λ̃_N. Table 6 nevertheless compares the two N's in adjacent columns. Use one convention throughout.

**m10 (p. 8, after Lemma 3.3).** "The bound |d_k| ≥ a_{k−2} is attained": the example only shows k = 2. Say "for k = 2", or give an example for k = 3 if one exists.

## Presentation

**P1 (notation collisions).**
- Γ is used for the Fuchsian group, Γ_x̃ for a stabiliser, and Γ(t), Γ* for the gap. Rename the gap.
- ℓ is used for the systole, for translation lengths, and for the systole bound in Theorem 7.1.
- δ and δ_k mean different things.
- p means the exponent in Theorem 6.2, points p̃ in Section 4, and the polynomials p_l.
- A means both the class bound and an actual area.

**P2 (p. 12, Theorem 6.2).** The block of definitions is very dense. Set them out as a numbered list saying what each quantity controls: the gap (t₁, Γ), the geodesics (t₂, t₃), the tail (Λ, N) and the perturbation (δ). Also state in the theorem that Area ≥ π/21 has been used in ϖ.

**P3 (p. 7, proof of Lemma 2.2).** The proof of the third bound is a run-on chain of inline inequalities. Display it.

**P4 (p. 7).** Give the meaning of α_k, the Taylor coefficients of the McKean expansion, next to the Bernoulli formula, so that readers can check α₀, …, α₃ at a glance.

**P5 (p. 13, Table 3).** The ε values are explained only in the following paragraph, by forward reference to Section 7. Put the provenance in the caption.

**P6 (Figure 1).** The rendered figure agrees with my recomputation. Labelling the five grey curves directly, rather than "darkest", would help.

## Recommendation

**Major revision.**

Confidence in the correctness of Sections 2, 3, 5 and 6, given the imported results: high. Every proof given was checked, every Table 3 row was reproduced, and the imported statements were tested numerically and by brute force. Confidence in the significance assessment: medium.

I would not accept while M1 is open. Under the journal's standards, the main theorem must be verifiable from refereed material or from this manuscript. M2 does not affect correctness, but in a paper whose contribution is effectivity it should be addressed.

## What resolves each issue

- **M1:** Include the short proofs (m2–m4, the counting bound and Proposition 2.3(a)). Either prove Proposition 2.3(b) and Theorem 3.2(i) here, or make this paper's acceptance explicitly conditional on [28]. Alternatively, state Theorem 6.2 with k* = M so that only the self-contained part (ii) is used, and mention (i) as an improvement.
- **M2:** Replace the single-base-point count by the net count n_O(x) ≤ C(A,ε,M)e^x, with C polynomial, built from Lemmas 4.2–4.3. Redo y₀, t₃, Table 3 and the class-level column of Table 6. Alternatively, remove the claim on p. 11 that the improvement does not transfer to orbifolds, and justify keeping e^{3D}.
- **m1:** Rewrite the admissibility sentence; state the elliptic convention and the check E_m(0⁺) = b₀(m).
- **m2:** Add the Dirichlet-domain proof.
- **m3:** Add the Laplace-transform proof of (a) and the one-line monotonicity argument; prove (b) or cite it precisely.
- **m4:** Add the Vandermonde proof.
- **m5:** Distinguish the class bound from the actual area.
- **m6:** Use the exact minimal area gap and the individual δ_k, or remark that they would improve the constants.
- **m7:** Use the max in place of the sum; use the minimal area in Sig(A,M).
- **m8:** Say that N, δ, Λ and Γ* must be recomputed at the replacement time; remove or prove the remark about K; support the computability claim.
- **m9:** Harmonise the indexing of N.
- **m10:** Qualify "attained".
- **P1–P6:** Editorial changes as described.
