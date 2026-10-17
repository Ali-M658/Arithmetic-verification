<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Handling editor's report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (Annals of Global Analysis and Geometry)

## Summary

The submission considers closed orientable hyperbolic 2-orbifolds with cone points, in the class C(A, ε, M): area at most A, systole at least ε, cone orders at most M. Its main result, Theorem 1.1 / Theorem 6.2 (p. 2, p. 12), says that the first N eigenvalues, each known to within δ, determine the signature (g; m_1, ..., m_n). N and δ are given by explicit formulas. The signature is the unique σ in Sig(A, M) that minimises |Σ_{j<N} e^{-λ̃_j t*} - G_σ(t*)|, where G_σ is the identity-plus-elliptic part of the Selberg trace formula for the heat function.

The proof has four steps:
1. The first heat invariant at which two signatures differ is an integer multiple of an explicit rational number (Lemma 3.3).
2. Enveloping remainders for the cone and area expansions (Proposition 2.3, from the companion paper) turn this into a gap Γ(t) at a small time t1 (Lemma 6.1).
3. The closed-geodesic term is controlled by a diameter bound D(A, ε, M) (Theorem 4.4, Section 4).
4. The spectral tail is controlled by a heat-trace counting bound (Section 5).

The other results are:
- **Theorem 7.1.** An a-posteriori version of the test, run on finite-element spectra of O(2,8,8), O(3,3,12) and eight orbifolds of signature (0; 3,3,3,3) (Tables 4–6).
- **Theorem 1.3 / Propositions 8.2–8.3.** The family O(2,3,m) has area below π/3, systole at least 0.56206 (proved via Jørgensen's inequality), and λ_j ≤ 1/4 + π²(j+1)²/h_m². So no N and δ that depend only on (A, ε) can work, and the order bound cannot be dropped.
- **Proposition 8.5 and Problem 1.** A pinching family, and an open question on whether the systole bound is needed.

The paper says plainly that the constants are astronomically large (Table 3: N up to 3.8 × 10^30, δ down to 8.7 × 10^-278). It also says that the eigenvalue errors and the completeness of the lists are estimates, not enclosures. The analytic core is taken without proof from a companion manuscript submitted at the same time (Table 1, p. 5).

## Significance

What is good:
- The question is natural, and the paper fits AGAG well. It continues the orbifold inverse-spectral line this journal has published (Stanhope 2005; Rossetti–Schueth–Weilandt 2008, both cited).
- The statements are correct as far as I checked; see below. All the tables I recomputed are reproduced to the displayed precision.
- The paper is unusually honest about what its numerics prove.
- The O(2,3,m) counterexample is clean and fits the physics: an elliptic point of growing order becomes cusp-like, and eigenvalues pile up just above 1/4.

The significance is nonetheless limited, and as editor I must say so plainly:

1. **The qualitative statement follows from compactness.** The authors give that argument themselves (pp. 2–3, Mumford–Bers compactness plus Dryden–Strohmaier / Doyle–Rossetti). What remains is effectivity. But the effective constants are so large that the explicit N and δ carry no information beyond "finite and positive": δ/Λ is a relative accuracy of about 10^-30 in the best row and about 10^-307 in the worst. The authors themselves say the constants' rates "are properties of our formulas, not of the problem" (pp. 11, 14, 25).
2. **Little new mathematics.** The ingredients that carry the weight are in the companion manuscript. These are the enveloping remainders (Prop. 2.3), the separation results (Thm 3.2) and the trace formula with geodesic counting (Thm 2.1, Lemma 2.2). What is new here is Lemma 3.3 (a few lines), an elementary packing bound for the diameter (Section 4), a two-line counting lemma (Section 5), and the assembly in Section 6.
3. **Theorem 1.3 is largely known in substance.** Garbin–Jorgenson [14, Thm 5.3] already show that the number of eigenvalues below a fixed level above 1/4 grows like log m along elliptic degeneration. Theorem 1.3 adds a pigeonhole argument, an explicit min–max bound, and a uniform systole bound. The systole bound is the one genuinely new geometric input of that section.
4. **The size of the constants comes from the chosen test function, not the problem.** From my own field, the dominant costs of Theorem 6.2 and of the class-level test are e^{3D} through the diameter bound, and the divergence of the cone expansion through t1. Both come from using the heat function. A test function whose Fourier transform is compactly supported below the systole avoids both (M1). If that is right, the quantitative message of Sections 4, 6 and 7 ("most of the gap ... is knowledge of the geometry, through e^{3∆}", p. 19) is a statement about the heat kernel, not about the inverse problem.

## Correctness and what was recomputed

I spot-checked the main statements, partly by hand and partly with my own code. The code is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/B-a-editor-quantum-chaos/scratch/code/`: heat.py, thm62.py, test71.py, perturb.py, compact.py. It uses mpmath at 30–40 digits and scipy, and is independent of the authors' deposit.

**Heat coefficients (p. 7):**
- α_0, ..., α_4 = 1, -1/3, 1/15, -4/315, 1/315, computed from the stated Bernoulli formula.
- b_0(m) = (m² - 1)/(12m).
- The leading coefficients a_0 = 1/12, a_1 = 1/360, a_2 = 1/2520 match the stated formula.
- b_l(m) for m = 2, 3, 5, 8 and l ≤ 3, computed from the definition via the Taylor coefficients φ_k of Φ_m.

**Proposition 2.3(a).** Checked numerically against direct quadrature of E_m(t) for m = 3, 8, 12, t in {0.01, 0.1, 0.5} and K = 0, ..., 4. In all 45 cases the remainder has sign (-1)^K and modulus at most |b_K(m)| t^K.

**Lemma 3.3.**
- (0;4,4,4) against (0;3,4,6): d_2 = (1/12)(12 - 13) = -1/12, as stated (p. 8).
- (0;2,8,8) against (0;3,3,12): d_3 = -a_1(P_3(U) - P_3(V)) = -(1/360)(1032 - 1782) = 25/12, as stated (p. 14). The sign conventions are consistent.
- The proof of (ii) is correct given Lemma 3.1. Padding by 1 is harmless because ψ_k(1) = p_l(1) = 0.

**Lemma 2.2, last bound (p. 6).** Rederived. The maxima at x = 2√t and x = 6t give the factor 2√t e^{-1/2} e^{9t/2}, and integration by parts against n_O gives 2πe^{3 diam - ℓ}/Area. Correct.

**Lemmas 4.1–4.3, Theorem 4.4.**
- Lemma 4.2 checked line by line: the defect bound ≥ π/(abc), cos((θ-α-β)/2) ≥ 1/M, and cosh d - 1 ≥ 2/(π²M²).
- Lemma 4.3: injectivity radii.
- Theorem 4.4: the closed form holds, since arccosh(1 + 2/(π²M²)) ≥ 0.621/M ≥ 0.6/M for M ≥ 2.

**Lemma 5.1.** Case analysis checked: minimal areas 1/42, 1/20, 1/12, 1/10, 1/6, 1/2 (in units of 2π) and n + 4g ≤ Area/π + 4.

**Lemma 6.1 and Theorem 6.2.** The chain checks out:
- B ≤ B* with the factor 63 = 21 · 3.
- The reduction to e^{-y} y^p ≤ γ*(ε²/4)^p / (16ϖe^{3D}), with max y^p e^{-y/2} = (2p/e)^p.
- Λt* ≥ 1, the tail equals exactly Γ*/8, and the perturbation is Γ*/(8e).
- The total is < 3Γ*/8 against > 5Γ*/8 for the competitors.

**Table 2.** All twelve entries reproduced: 56.6, 1125, 6.37e5; 150.9, 3001, 1.70e6; 640, 3184; 1132, 2.25e4, 1.27e7.

**Table 3.** All eight rows reproduced to the displayed precision: k*, D, t1, t3, Γ*, Λ, N, δ and the binding constraint. For example, row 8 gives t1 = 2.5e-27, Γ* = 1.77e-272, N = 3.75e30 and δ = 8.65e-278. The claim on p. 14 that dropping k* ≤ M at A = 10π, M = 3 raises N to "about 4 × 10^18" is also reproduced: 4.19e18.

**Proposition 8.2.**
- σ* = 2 arsinh((1/2)(1 + (3/4)cosh²(2s_∞))^{-1/2}) = 0.56205, with cosh(2s_∞) = 5/3.
- The trace identity tr[γ,β] - 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r was checked numerically with explicit matrices.
- The convexity step d(x, v_3) ≤ 2s_m was checked.

**Identity (3) and Propositions 8.3 and 8.5.**
- Identity (3) rederived: q = 1/2 - w'²/(4w²).
- Proposition 8.5: the λ_1 bound follows from ∫ρ² cosh ρ dρ = (ρ² + 2) sinh ρ - 2ρ cosh ρ.
- Proposition 8.3: the pigeonhole count K = (⌊Λ_N/δ⌋ + 1)^{N-1} is correct.

**Table 4 geometry.**
- diam P for O(2,8,8): arccosh(cot²(π/8)) = 2.448.
- diam P for O(3,3,12): 2.158.
- diam P for O_ϑ at ϑ = 0: 2.292 (corner at x_0 = √3).
- Systoles 4b at ϑ = 0 and ϑ = 2.8: 2.6339 and 0.6940.

**Table 5 against the trace formula.** I summed e^{-λ̃_j t} over λ̃_0 = 0 and the 40 listed eigenvalues at t = 0.0596.
- O(2,8,8): Z - G_{(0;2,8,8)} = -9.0e-9, which is the size of the truncated tail.
- O(3,3,12): Z - G_{(0;3,3,12)} = +9.2e-7, which is the size of the closed-geodesic term for systole 1.86.
- Every competitor is off by at least 4.1e-2.

So the bottom of both lists is consistent with the stated signatures, and only with them.

**Theorem 7.1 counts (Table 6, rows 1–2).** I used Table 5's eigenvalues and errors and Table 4's ℓ and ∆ = 2 diam P. Over the six signatures of area π/2 with orders ≤ 12, the least N for (C1) is 18 for O(2,8,8) and 25 for O(3,3,12). For (C2) it is 20 and 29. All four agree exactly with Table 6.

**Fragility claim (p. 15, item (iv)).** Deleting or duplicating one of λ̃_1, λ̃_2, λ̃_3, λ̃_5, λ̃_8, λ̃_12 makes (C1) single out a wrong signature in **19 of 24** cases. This is exactly the authors' count, and the wrong answers come at N = 9–26.

**Not checked:**
- The companion's results used without proof: Theorem 2.1 admissibility, the first bound of Lemma 2.2, the proof of Proposition 2.3, Lemma 3.1, Theorem 3.2.
- The finite-element computations beyond Table 5.
- The family's class-level counts.
- The proof of Lemma 8.1 beyond a read-through. It follows Jørgensen's argument, and I found no gap.

## FATAL

None. I found no error in any main statement, no inconsistency between the text and the tables, and no misstated numerical claim. The issues below concern significance, method, dependence and framing, not validity.

## MAJOR

**M1. The two dominant costs come from the heat function. The paper neither avoids them nor justifies keeping them.** (pp. 3, 10–11, 13–14, 19; Theorems 4.4, 6.2, 7.1; Section 7.2.)

- In Theorem 6.2, t* is set by t1 (divergence of the cone expansion, |b_K(M)| ~ K!(M/π)^{2K}) or by t3 ≈ ε²/(24D) (the closed geodesics through e^{3D}). Table 3 shows these two alone drive N from about 10^4 to 10^30.
- In the test, p. 19 attributes "most of the gap" to e^{3∆}.

Both costs disappear if the heat function is replaced, in the same trace formula (Theorem 2.1), by h = ĝ with g = φ * φ, φ even, smooth and supported in [-τ/2, τ/2]:

- **(a)** For τ < ε the hyperbolic term vanishes identically. Lemma 2.2, Section 4 (the whole diameter bound) and t3 then become unnecessary. The test needs only a systole bound.
- **(b)** The elliptic term is ∫ g(u) K_θ(u) du with a kernel analytic in |u| < 2θ. For τ < 2π/M its expansion in the moments of g converges geometrically. It is no longer merely enveloping, and the t1 bottleneck disappears.
- **(c)** h = |φ̂|² ≥ 0, so the spectral tail is positive and can be bounded by an explicit local Weyl bound that uses no geodesics.

This is the standard route in rigorous automorphic computation (Booker–Strömbergsson–Venkatesh [22], cited). The authors use it themselves in the companion: [28, proof of Lemma B.1] takes ψ ∈ C_c^∞ with support below the systole "so the hyperbolic side vanishes for it". The companion also notes that its e^{3 diam} constant overestimates by factors up to 10^10 [28, Section 4].

**Illustration (not rigorous; the tail is a Weyl-law estimate).** I took φ to be the standard bump on [-1.1, 1.1], so g is supported in [-2.2, 2.2], inside (-ℓ, ℓ) with ℓ = 2.2568. For O(2,8,8) I used only Table 5's 41 eigenvalues and **no diameter information**:

| Signature | G_σ[h] - Σ h(r_j) |
|---|---|
| (0;2,8,8) | +9.8e-5 (Weyl tail estimate 9.6e-5) |
| (0;2,2,2,4) | -0.12 |
| (0;2,6,12) | +1.6e-2 |
| (0;3,3,12) | -1.2e-2 |
| (0;3,4,6) | -6.1e-2 |
| (0;4,4,4) | -7.4e-2 |

For O(3,3,12) with support [-1.8, 1.8], the true residual is 2.3e-4 (estimate 2.2e-4), against at least 8.4e-3 for every competitor. By contrast, the paper's class-level heat test fails within about 2000 eigenvalues for both orbifolds (estimates 5611 and 8619, Table 6). The a-priori theorem would change in the same way: the gap between signatures becomes O(1) at the scale of the systole, instead of γ* t^{k*-2} at t ~ 10^-7.

The authors must either recast Theorems 6.2 and 7.1 with such test functions, or explain clearly why the heat function is needed. For example, they might argue that the integrality of Lemma 3.3 needs the t-expansion. I do not see why it should: the moment expansion in (b) has the same triangular structure in the ψ_k. As written, Section 4, the t3 constraint, and the paper's headline conclusions about where the cost lies are artefacts of the method.

**M2. The significance beyond compactness is not established.** (pp. 1–4, 13–14.)

The paper's justification is effectivity ("Effectivity is the point", p. 4). But Table 3's values fall far outside anything computable or measurable. Row 1 needs relative accuracy δ/Λ ≈ 3 × 10^-30 on 3.4 × 10^8 eigenvalues; row 8 needs δ = 8.7 × 10^-278. And the authors concede that the rates in ε and M are artefacts. An effective theorem whose constants are known to be artefacts, and are astronomically far from the truth, needs some other selling point: a structural insight, a sharp rate, or a usable algorithm. The paper should either supply one (M1 may supply it) or state its contribution more modestly.

The same applies to Theorem 1.3. With [14, Thm 5.3] (logarithmic growth of the eigenvalue count below any level above 1/4) and a pigeonhole argument, the non-existence of (A, ε)-only constants is essentially immediate. The explicit bound of Proposition 8.3 is a one-line min–max. What is new is the uniform systole bound σ* of Proposition 8.2. The introduction (p. 4, "Our contribution there is the explicit estimate of Proposition 8.3") should say exactly this.

**M3. The correctness of Theorem 1.1 rests on an unrefereed companion submitted at the same time.** (Table 1, p. 5; Sections 2–3; p. 17.)

Theorem 2.1 (including the admissibility of the heat function), Lemma 2.2, Proposition 2.3, Lemma 3.1 and Theorem 3.2 are "stated here without proof". Proposition 2.3 (the enveloping remainders) and Theorem 3.2 (separation under bounded orders) are the analytic and combinatorial cores of Lemma 6.1. The numerical claims also rest on the companion's supplement: "the convergence in h and p is tabulated in the supplement of [28]" (p. 17). The companion's supplement is headed "Electronic supplementary material ... Annals of Global Analysis and Geometry", so it appears to be under consideration at this journal too.

Editorially, this paper cannot be accepted before [28], and the two must be refereed together, with at least one common referee. Alternatively, the authors should include in an appendix the proofs of Proposition 2.3(a)–(b) and of Theorem 3.2(ii), the only parts of Theorem 3.2 that Theorem 6.2 uses, together with the numerical convergence evidence they rely on.

**M4. The accuracy hypothesis is uniform in j. This is wasteful, and physically it is the wrong notion.** (Theorem 1.1, p. 2; Theorem 6.2, pp. 12–13; Theorem 7.1, p. 15.)

The perturbation step uses |e^{-at} - e^{-bt}| ≤ t|a - b| and discards the factor e^{-t min(a,b)}. Keeping it, the hypothesis |λ̃_j - λ_j| ≤ δ e^{λ_j t*}, or the equivalent relative form, gives the same conclusion. Near the top of the range this relaxes the required accuracy by up to e^{Λt*} = (8Z♯(t*/2)/Γ*)². For row 3 of Table 3 that factor is about 2 × 10^19. The same applies to the term t Σ ϵ_j in E_N(t), which should be t Σ ϵ_j e^{-(λ̃_j - ϵ_j)t}.

The physical framing in the abstract and p. 2, "a measurement or a computation yields ... eigenvalues, each to some accuracy", is about relative accuracy at high energy. The theorem should be stated in that form, and Table 3 should report the relaxed accuracy requirement.

**M5. As executed, the a-posteriori test is a consistency check, not a decision. The abstract and introduction still say "decides".** (Abstract; pp. 3, 15–19; Tables 4 and 6.)

The test takes as inputs:
- the exact area and the order bound, which reduce S to 3, 6 or 10 candidates. With M = 3 the candidates already differ at c_2, the constant term of the heat trace.
- an uncertified systole.
- estimated, not enclosed, eigenvalue errors.
- completeness, which is supported only by a trace comparison against the **true** signature.

I confirmed (19 of 24) that a single missing or duplicated eigenvalue produces a confident wrong answer at a smaller N than the true count. Without a completeness certificate that does not depend on the signature, a user who increases N until (C1) holds will stop at a wrong signature in most of these cases. The authors say all this (pp. 15–17, 19), which I commend. But the abstract's "decides four of ten ... decides all ten" does not match it.

Two remedies, either of which is acceptable:
- **(a)** Make at least one example fully rigorous. The triangle orbifolds are the natural choice. This needs: a systole certified in interval arithmetic (cheap; the enumeration already exists); eigenvalue enclosures for the first 20–30 eigenvalues (for example by guaranteed lower-bound FEM, or the Liu–Oishi or Plum–Behnke–Goerisch methods); a validated quadrature for G_σ; and a completeness argument that does not use the signature, run against every σ in S. With M1 the geodesic term is identically zero, which makes this considerably easier.
- **(b)** Rewrite the abstract and introduction to say "the criterion of Theorem 7.1 holds with estimated errors for lists assumed complete". Also run the test over Sig(A, M) with only an area bound. The paper says this "would suffice" (p. 15) but has not been done, and it is a short computation.

## MINOR

- **m1 (p. 4).** "Theorem 1.3 shows that no finite part of the spectrum bounds the orders" overstates it. Theorem 1.3 shows that no N and δ depending only on A and ε separate signatures. Equivalently, no locally bounded function of (λ_1, ..., λ_{N-1}) bounds the orders. It does not exclude that the exact first N eigenvalues determine m: the computed λ_j are strictly monotone in m (p. 23). Please state it precisely.
- **m2 (p. 23).** "The computed values suggest λ_j → 1/4, which Proposition 8.3 does not prove." The eigenvalues below 1/4 converge to those of the cusped limit [14, Cor. 5.5], and the limit PSL(2,Z)\H has no eigenvalue in (0, 1/4): its first cusp form has λ ≈ 91.1. If [14] covers the degeneration O(2,3,m) → O(2,3,∞), then λ_j → 1/4 for each fixed j follows from Proposition 8.3. Please check this and say so.
- **m3 (p. 25, Problem 1).** Calling Problem 1(a) "the signature-level analogue of the conjecture of Buser and Courtois" needs a qualification. The signature is determined by the heat invariants, that is, by the smooth (Weyl-type) part of the spectrum. Buser–Courtois concerns full isospectrality, which is carried by the oscillatory part (length spectrum and moduli). The companion itself stresses this distinction [28, Section 4]. The analogy is loose and should be presented as such.
- **m4 (p. 15).** "Criterion (C2) is the margin used in Theorem 6.2; (C1) is weaker and is the theorem's own conclusion." This is ambiguous: Theorem 6.2's conclusion is the unique minimiser, not (C1). Say "Theorem 7.1's own conclusion".
- **m5 (pp. 2, 12, 14, 18–19).** The counting convention changes:
  - Theorem 1.1 / 6.2: N counts λ_0, ..., λ_{N-1}.
  - Table 6 and the abstract: "N eigenvalues" means λ̃_0, ..., λ̃_N, that is, N nonzero values plus λ̃_0.
  - Fig. 1 (p. 14): "21 eigenvalues ... (N = 20)".

  The comparisons are unaffected, but please use one convention throughout.
- **m6 (abstract; p. 19).** "Decides four of ten ... with 855 to 2900" holds only for M = 3. With M = 12 the class-level test decides none. Say so in the abstract.
- **m7 (p. 13).** The decision rule needs G_σ(t*) to within Γ*/16, which can be as small as 10^-273. "Computable to any prescribed accuracy" is true but should be accompanied by an honest statement of the cost.
- **m8 (pp. 3–5, references).** Two works on effective spectral and length-spectral rigidity are missing and should be cited and compared:
  - Linowitz, McReynolds, Pollack, Thompson, "Counting and effective rigidity in algebra and geometry", Invent. Math. (2018), doi:10.1007/s00222-018-0796-y.
  - Friedman, Jorgenson, Kramer, "An effective bound for the Huber constant for cofinite Fuchsian groups", Math. Comp. 80 (2011) 1163–1196, doi:10.1090/S0025-5718-2010-02430-5.

  The paragraph "A rigorous decision would need guaranteed upper and lower eigenvalue bounds ..." (p. 16) should also cite the available verified-eigenvalue methods.
- **m9 (p. 2).** The fact that the full spectrum determines the signature is cited to [1] and to [5], and [5] is an arXiv preprint (2011/2014) that appears unpublished. [1] suffices. Mark [5] as independent or alternative.
- **m10 (pp. 10–11).** The diameter bound of order A(1 + log 1/ε) + log M that a thick–thin argument "should give" is conjectural. If M1 is adopted, Section 4 and this discussion can be removed. If it is not, label the claim as a conjecture.
- **m11 (p. 17).** The systole is "rounded down at the sixth decimal" from 40/50-digit floating point. Interval arithmetic (mpmath.iv, Arb) would certify it at negligible cost, so please do it.

## Presentation

- **P1 (notation clashes, all seen in the rendered pages).**
  - Γ: the Fuchsian group (p. 6), the gap Γ(t) and Γ* = Γ(t*) (p. 12), and the reflection group Γ* (p. 21).
  - The systole bound ε against the eigenvalue errors ϵ_j (p. 15): two epsilons in the same formulas.
  - ℓ: the systole, and the interval length in the proof of Proposition 8.3 (p. 22).
  - Q(K) (p. 12) against the quadrilateral Q_{k,b} (p. 23).
  - The point O = (1,0,0) against the orbifold 𝒪 (p. 23).
  - p: the exponent k* - 3/2 (p. 12), the polynomials p_l, and the cone point p̃.
  - a: a radius (p. 22), a distance (p. 23), and the coefficients a_l.

  Please rename.
- **P2 (abstract).** The abstract carries six numerical ranges and two caveats but does not state the theorem's hypotheses cleanly. State Theorem 1.1, the necessity of the order bound, and one sentence on the numerics.
- **P3 (pp. 2–3).** Theorem 1.2 forward-references E_N and (C2) without definitions. Either give the formula or present Theorem 1.2 informally.
- **P4 (Fig. 1, p. 14).** Six grey levels and two dotted styles with no legend are hard to read. Label the curves directly.
- **P5 (Fig. 2, p. 20).** Markers are drawn "slightly to the left/right of their systole", which displaces data along a quantitative axis. Use two panels (M = 3 and M = 12) instead.
- **P6 (throughout).** The caveats ("observations on our formulas, not proved asymptotics, and not properties of the problem", "an observation and not a result") are repeated many times. Collect them in one paragraph. The individual sentences are long and heavily parenthetical; a copy-edit for readability would help AGAG's readership.

## Overlap with the related manuscripts

**Companion "How much of a hyperbolic orbifold does heat hear?" [28] and its supplement.**
- **Disclosed reuse.** Sections 2–3 restate seven results of [28] without proof, listed transparently in Table 1. I verified the correspondences: [28] Thm 2.3/Lemma B.1, Lemmas 2.4–2.6, 2.8, 2.10, 3.3, Prop. B.2, Cor. 3.5, Thm 3.8(i). Lemma 3.3 here is new but is a few-line consequence of [28, Lemmas 2.10, 3.3].
- **Shared data.** The computed spectra (O(2,8,8), O(3,3,12) and the (0;3,3,3,3) family) are the same computations. [28, Section 4, Fig. 5] and its supplement (Sections S4–S6) already compare those heat traces with the trace formula. They show that the computed difference for the triangle pair follows the elliptic terms to 4 × 10^-13, and that the family differences equal the hyperbolic terms. The present Section 7 is a new use of these data, a decision criterion, but the numerical substance overlaps substantially. The present paper also leans on [28]'s supplement for its convergence evidence (p. 17).
- **Not duplicated.** The diameter bound, eigenvalue counting, Theorems 6.2 and 7.1, and Section 8 (O(2,3,m), Jørgensen, pinching) do not appear in [28]. [28] confirms this division (p. 5 there).
- **Dependence.** It runs one way and is substantial (M3). The division into two papers is coherent in theme: local heat invariants versus global finite spectral data. But it leaves this paper with thin independent content (M2). If the authors adopt M1, the method itself separates the two papers more clearly, which would strengthen the case for two papers.

**"Triples with equal sum and equal reciprocal sum" [29].** No overlap beyond the shared motivating pair O(2,8,8), O(3,3,12). There is no dependence in either direction, and the note says so explicitly.

There is no evidence of duplicate publication. The handling of the two AGAG submissions must be coordinated (M3).

## Editorial decision and recommendation

**Decision: SEND TO REVIEW.**

Reasons:
- The paper is within scope for AGAG.
- Its main statements are correct as far as I could check. Every table I recomputed agrees, including the a-posteriori counts and the fragility claim.
- It is carefully and honestly written about what its numerics prove.

It is not acceptable in its present form. The decisive questions for the referees are M1 and M2: whether the effective content survives once the heat-kernel artefacts are removed, and whether what remains is significant enough for AGAG.

Conditions for review:
- At least one referee in common with the companion [28].
- Referees with expertise in (i) trace-formula and effective spectral methods and (ii) validated numerics for eigenvalue problems.
- Referees should be asked explicitly to assess M1–M5.

**Recommendation (provisional, pending referees): MAJOR REVISION.**

Confidence:
- High (about 85%) that there is no fatal mathematical error in the main statements.
- Moderate (about 60%) that the paper can reach the bar after revision.
- About 30% that the referees will judge the significance insufficient even after revision, and recommend rejection.

## What resolves each issue

- **M1.** Reformulate Theorems 6.2 and 7.1 with a test function g = φ * φ supported in (-min(ε, 2π/M), min(ε, 2π/M)) and h = |φ̂|². This removes Section 4 and t3, and replaces the enveloping remainders by convergent moment expansions. Then redo Tables 3 and 6. Or give a convincing mathematical reason why the heat function is necessary, and remove the claim that the cost is "knowledge of the geometry".
- **M2.** State a contribution beyond compactness: rates in A, ε, M that are not artefacts, a usable algorithm (which M1 may supply), or a structural statement. Credit [14, Thm 5.3] precisely for the content of Theorem 1.3, and identify the systole bound of Proposition 8.2 as the new input.
- **M3.** Coordinate the review with [28]. Accept this paper only after [28], or include proofs of Proposition 2.3 and Theorem 3.2(ii) and the convergence data in this paper or its supplement.
- **M4.** Replace the uniform δ by a weighted or relative accuracy hypothesis (δ_j ≤ δ e^{λ_j t*}). Do the same for the term t Σ ϵ_j in E_N. Report the relaxed requirements in Table 3, and frame them in relative terms.
- **M5.** Either certify one example end to end (interval systole, eigenvalue enclosures, validated G_σ, completeness independent of the signature), or replace "decides" by "is consistent with" in the abstract and introduction. In either case, run the test over Sig(A, M) with an area bound only.
- **m1–m3.** Restate precisely: the meaning of "bounds the orders"; λ_j → 1/4 via [14]; the qualified Buser–Courtois analogy.
- **m4–m7.** Fix the wording; use one counting convention; qualify the abstract for M = 3; state the cost of evaluating G_σ.
- **m8–m9.** Add the missing references; mark [5] as an unpublished preprint.
- **m10–m11.** Mark or remove the conjectural diameter rate; certify the systole in interval arithmetic.
- **P1–P6.** Rename the clashing symbols, rewrite the abstract, define E_N or present Theorem 1.2 informally, add legends to Fig. 1, split Fig. 2 into panels, consolidate the caveats, and copy-edit.

---
The write to `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/B-a-editor-quantum-chaos/REPORT.md` was refused, so `REPORT.md` was not created and the complete report is the text above.
