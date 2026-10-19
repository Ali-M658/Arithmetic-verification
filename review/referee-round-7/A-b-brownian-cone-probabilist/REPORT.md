<!-- Referee A-b: returned text saved verbatim; the reviewer could not write files -->

I couldn't save the report: writing `REPORT.md` was refused, so the full report is below instead. My recommendation for Section 2, the variable-curvature propositions and the appendices they rest on is **major revision**, at medium confidence (about 0.65). Neither major issue touches the main theorems, and with both fixed my recommendation would drop to minor revision.

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

**Referee B (probability: heat kernels and Brownian motion on cones and orbifolds).**

**Scope.** I was asked to review Section 2 (the trace formula, the hyperbolic-term bound, the closed-form expansion, the triangular structure, and variable curvature: Propositions 2.11 and 2.13 and Remark 2.12). I also reviewed everything those results depend on:

- Appendix B (Lemma B.1, the proof of Proposition 2.7, Proposition B.2, Lemma B.3, Remark B.4);
- Lemma 3.3, as far as Proposition 2.13 uses it;
- the parts of Section 4 that use Lemma 2.5 (Proposition 4.2, Remark 4.3);
- supplement Section S7 (computations behind Remark 2.9, Remark 2.12, the bound (6) and Remark B.4).

I did not referee Sections 3, 5 or 6, or Appendices A, C, D and E, except where Section 2 points to them. As instructed, the placeholders (author contributions, AI-use statement, Zenodo DOIs, preprint identifiers) are taken as known.

Page numbers refer to the manuscript PDF; "S" refers to the supplement. I read the rendered pages 2, 9–18 and 44–47 before reporting any typographical or sign issue.

---

## 1. Summary of the part under review

Section 2 gives the constant-curvature heat trace of a closed hyperbolic 2-orbifold in a closed form valid at every order. It starts from the Selberg trace formula (Theorem 2.3, made admissible for the heat function by Lemma B.1). The elliptic terms are rewritten through the function Φ_m(u) = (cot u − m cot mu)/(4m sin u) (Lemma 2.6). This gives cone coefficients b_l(m) = (−1)^l p_l(m)/m with explicit even polynomials p_l of degree 2l+2 (Proposition 2.7, Lemma 2.8).

The truncations of the area series and of the cone series are shown to be **enveloping**, with remainders of opposite signs. This gives the explicit bound (6). The closed geodesics are bounded explicitly through the systole and the diameter (Lemmas 2.4 and 2.5).

Lemma 2.10 restates Uçar's triangular structure: each order in t adds one new odd power sum of the cone orders, which is what drives the counting in Section 3.

Section 2.4 treats variable curvature:

- **Proposition 2.11** shows that, for m ≥ l−1, the cone term has the form Σ_{i ≤ l+1} β_{l,i} Π_i(m), where the β_{l,i} depend on the radial part of the curvature jet. It identifies the top coefficient as β_{l,l+1} = 4^l l! [v^{2l}](f^{−1})′, and the part linear in the curvature as (2/(l−1)!) Π_{l+1}(m) (−Δ)^{l−1} K(p).
- **Proposition 2.13** shows that once the curvature varies, the counts of the paper lose their meaning. Signatures with equal c₂ carry metrics that share any prescribed finite number of invariants. The minimal pair O(2,8,8), O(3,3,12) carries metrics, flat near the cone points, that share every invariant.

## 2. Significance (of this part)

The constant-curvature expansion is **not new in substance**. All coefficients are Uçar's (thesis, Thm 4.20), and the triangular mechanism is Uçar's induction; the authors say so honestly (pp. 6, 12). Two things are new and useful:

- the closed form through Φ_m, which makes the coefficients easy to compute and to bound;
- above all, the enveloping property with its fully explicit remainder (6) and the explicit closed-geodesic bound.

These are what the rest of the paper needs for anything quantitative, and they are proved cleanly.

Section 2.4 is partly new. The formula for β_{l,l+1} in terms of the inverse of the radial Jacobi field f, the linear-part formula valid for every m, and the constructions of Proposition 2.13 are, to my knowledge, not in the literature. Schueth (AIF 2019, Thm 3.7/4.1) has l ≤ 2; her 2026 paper (AGAG) treats rotationally symmetric curved cones only at order t^{1/2}.

The main theorems of the paper do not depend on Section 2.4. That section is a negative result plus a structural one. Its interest is in showing that the constant-curvature counting is genuinely tied to constant curvature.

From the point of view of short-time diffusion, the picture is correct and well explained:

- the cone point of order m acts through its rotations at distance 2r sin(πj/m);
- the cone series diverges, with scale (π/m)²;
- closed geodesics enter only at order exp(−ℓ²/4t).

## 3. Correctness, and what I recomputed

I found **no mathematical error that affects any statement used in the main theorems**. Everything that the main results take from Section 2 and Appendix B is correct, and I checked it independently:

- Theorem 2.3;
- Lemmas 2.4, 2.5, 2.6, 2.8 and 2.10;
- Proposition 2.7 with the bound (6);
- Proposition B.2 and Lemma B.3.

My issues are about:

- the completeness of the proof of Proposition 2.11 (M1);
- the gap between what Lemma B.3 proves and what is claimed for O(2,8,8) (M2, including a rounding error in the diameter in Remark B.4);
- a number of smaller points.

All scripts are in `scratch/code/` (Python with sympy/mpmath in a local venv).

**Recomputed and confirmed:**

1. **Lemma 2.6.**
   - Checked the closed form numerically (m = 7, at u = 0.1, to 120 digits).
   - The Taylor coefficients of the closed form agree exactly with (4) for k ≤ 4.
   - Checked the Bernoulli/cotangent step, including the sign sgn B_{2n} = (−1)^{n+1}, by hand.
2. **Proposition 2.7 / Lemma 2.8.**
   - p_l from (4)–(5) for l ≤ 6. All are even, with p_l(1) = 0, degree 2l+2, and leading coefficient exactly |B_{2l+2}|/(2(l+1)!(2l+1)) for every l ≤ 6.
   - p₀, p₁, p₂ agree with (8).
   - p₃ = (m²−1)(m²+3)(3m⁴+2m²+19)/30240, which is the K³ coefficient of Remark 2.12(b).
   - α₀, …, α₅ = 1, −1/3, 1/15, −4/315, 1/315, −4/3465 by both the Bernoulli-polynomial formula and the μ_k formula of Appendix B. The μ_k were checked by quadrature.
   - b₀ = (m²−1)/(12m), and b₁, b₂ at K = −1, agree with DGGW/Schueth. I checked the latter against Schueth, AIF 2019, Rem. 4.2 and Thm 4.1, which I fetched from arXiv:1812.06119.
3. **Equation (10), and d₃, d₄ (p. 32).** d₃ = 25/12 and d₄ = −1775/24 are exact.
4. **Proposition B.2 (enveloping), numerically at 60 digits.**
   - E_m: m ∈ {2, 3, 7, 12}, t ∈ {10⁻³, 10⁻², 0.05, 0.2, 1}, K ≤ 5.
   - (4π/Area)·I: t ≤ 3, K ≤ 5.
   - In every case the remainder has the stated sign and is at most the first omitted term.
   - The proof's bookkeeping of the three remainders in part (b) is exactly the decomposition of α_{K+1} into same-sign terms. I checked this by hand.
5. **The (2;2) claim on p. 11.** At t = 0.05 the remainder after c₁, c₂ is 1.0775×10⁻³, which exceeds c₃t = 1.0417×10⁻³. Confirmed.
6. **Lemmas 2.4 and 2.5.**
   - I re-derived the integration by parts, the bound x/(x−t) ≤ ℓ/(ℓ−t), and the identity 1 + 2t/(ℓ−t) = (2+3ℓ)/(2+ℓ) at the end of the range.
   - I re-derived the logarithmic derivative in ℓ, which equals 1/ℓ + 1/2 − ℓ/2t − e^{−ℓ}/(1−e^{−ℓ}) − 2t/(ℓ²−t²), as printed.
   - All correct.
7. **Lemma B.1.** Checked line by line: the η_T counting with the evenness of ψ̂, and the dominated convergence. Correct (but see m3).
8. **Remark 4.3.**
   - The Fourier identity, checked numerically.
   - E_m(t) = ∫ g_t k_m, checked numerically (m = 5, t = 0.3). Both agree to 15 digits.
9. **Proposition 2.11.**
   - mΠ_i in closed form for i ≤ 5, with leading coefficient |B_{2i}|/(2i)!.
   - 2Π₂ = p₁/m.
   - 12Π₃ − 2Π₂ = p₂/m, which is Schueth's Thm 3.7 averaged at K = −1.
   - The Δ²K coefficient of Remark 2.12(b) equals Π₄(m), as part (iii) predicts.
   - **β_{l,l+1} from 4^l l! [v^{2l}](f^{−1})′ for l ≤ 3, on the radial metric with K̄ = k₀ + k₁r² + k₂r⁴:**
     - β_{1,2} = 2k₀;
     - β_{2,3} = 12k₀² + 8k₁ = 12K² − 2ΔK;
     - β_{3,4} = 120k₀³ + (496/3)k₀k₁ + 64k₂. This equals 120K³ − 42KΔK + Δ²K exactly once ΔK = −4k₁ and Δ²K = 64k₂ − (8/3)k₀k₁, both computed on the curved radial metric.
     - So Remark 2.12(a) is confirmed, including its non-linear part.
   - At constant curvature the top coefficient is (2l)!/l!·K^l, and the linear part is as stated.
   - I also verified the Duhamel integral for λ_l by hand: −2l·l!·4^l t^l C^{−2l−2}, giving λ_l = 2C^{−2l−2}/(l−1)!.
10. **Proposition 2.13(ii).**
    - I recomputed the second-variation constants by an independent Fourier/Gaussian computation of the second-order Duhamel term. This gives ω_n = 1/30, −1/140, 1/1260, −1/16632 for n = 2, …, 5, exactly the stated (−1)^n n(n−1) n!/(2n+1)!.
    - The example (0; 2⁸), (0; 3, 3, 3) and the condition of (iii) for O(2,8,8), O(3,3,12) hold: Σ(1−1/m) = 9/4 and Σ(m−1/m) = 69/4 on both sides.
11. **Remark B.4.**
    - Q₃ = 303.63 and δ₁ = 4858·t₃.
    - t₃ ≤ 7.8×10⁻¹¹, and η ≤ 2.07×10⁻¹⁹ at t₃ = 10⁻¹¹.
    - All as stated, apart from the diameter issue in M2.
12. **Figure 1 and the Introduction.**
    - √0.02/sin(π/12) = 0.546.
    - On the flat cone of order 12, 4πt·h_t = 1.785 at that distance, and within 3×10⁻⁴ of 1 at three times it.
    - Confirmed.

**Not independently checked:**

- the coefficients of KΔK in Remark 2.12(b) below the top one (the authors say these rest on a single computation);
- the Uçar comparison of Remark 2.9 (this needs his normalisation, which I did not obtain).

Neither is used in a proof.

---

## FATAL

None in the part under review.

## MAJOR

**M1. Proposition 2.11 (pp. 13–15): the proof is not complete as written.**

The statements are, I believe, correct: I checked every closed-form instance up to l = 3, see item 9 above. But four steps are asserted rather than proved, and the proposition is offered as a theorem.

**(a) The form B_l(Φ) = C^{−2} P(cot(ϑ/2)) with P a polynomial ("Donnelly's form … [2, 4.2]", p. 14) is the crux, and it is not justified.**

Donnelly's coefficients are universal expressions in the jet and in A = dΦ_p. If entries of A appeared, as cos ϑ = 1 − C²/2 or sin ϑ = (C²/2)·cot(ϑ/2), then B_l would be a Laurent polynomial in C² with possibly **positive** powers. Then:

- b_l(p) would acquire terms β₀(1 − 1/m) and constants;
- the representation Σ_{i ≥ 1} β_{l,i} Π_i(m) would fail;
- the pole-order argument would not exclude these terms.

The fact that rescues it is that only (I−A)^{−1} enters. After the substitution w = (I−A)v one has Av = ((I−A)^{−1} − I)w, so every polynomial in v and Av is a polynomial in (I−A)^{−1}w. Moreover (I−R_ϑ)^{−1} = ½I + ½cot(ϑ/2)J. This must be stated and proved, or cited with a precise theorem number and the exact form of the statement.

**(b) The "radial reduction" (p. 15) is a sketch.**

- The phrase "radial part of the jet" is never defined as a set of coordinates. The natural choice is the Taylor coefficients k_j of K̄ in r², and β_{l,i} should be stated as polynomials in (k₀, …, k_{l−1}).
- The claim that the SO(2)-invariant part of the jet of covariant derivatives equals the jet of dr² + f²dθ² "up to terms at least quadratic in the non-radial modes (from the passage between covariant derivatives and Taylor coefficients)" needs an actual argument. One must show that the correction terms are at least quadratic in non-radial modes, or of nonzero frequency.

**(c) The expansion in powers of s/C (p. 14) is not justified uniformly.**

The step inverts s = C·r·W_u(r)^{1/2} and integrates term by term, with coefficients "bounded uniformly" in ϑ. This needs a short lemma that the inversion and the Laplace expansion are uniform in (u, ϑ). Otherwise "O(C^{−2l})" is not justified as ϑ → 0.

**(d) Part (ii) is ill-posed as stated.**

"The coefficient of the new power m^{2l+1} in b_l(p)" has no meaning for a fixed cone point, whose order m is fixed. What is meant is the universal identity b_l = Σ_i β_{l,i}(radial jet)·Π_i(m), with β independent of m, read as a polynomial in m for a fixed radial jet. Please state it that way.

**Resolution.**

- Give a complete proof, with (a) made explicit and (b), (c) as lemmas.
- Alternatively, downgrade the statement to a proposition "with proof sketched", noting that the main results do not use it.

I also note two simplifications that may help the authors, and they may strengthen (i):

- **Evenness holds for every germ.** B_l(Φ) = B_l(Φ^{−1}) for every germ, because the heat kernel is symmetric: substitute x = Φ^{−1}y in ∫χ(x)h_t(x, Φx). No reflection symmetry is needed. Note, though, that this does not by itself make P an even polynomial for a germ with only Z_m symmetry, since ϑ takes only finitely many values.
- **The form of (i) holds for every m.** In the average over j, the terms j and m−j have the same C and opposite cot(πj/m). So the odd part of P cancels **for every m ≥ 2**. Hence b_l(p) = Σ_{i=1}^{l+1} β_{l,i}·Π_i(m) holds for every m, with β_{l,i} SO(2)-invariant polynomials in the full jet. The hypothesis m ≥ l−1 is needed only to evaluate them on the radial part. This narrows Problem 5.

**M2. Lemma B.3 and Remark B.4 (p. 47): the "proved" error is not proved for the example given; a-priori data are needed and one input is wrong.**

Lemma B.3 is correct as stated. It assumes:

- a lower bound ℓ₀ for the systole;
- an upper bound D for the diameter.

Neither is a spectral invariant. This should be said plainly wherever the paper advertises "a proved but large error" (p. 5, Section 6). The heat-trace-to-invariants step is proved only relative to geometric a-priori bounds.

In Remark B.4 the a-priori data for O(2,8,8) are described as "the smaller systole of the minimal pair" and "its computed diameter". Neither is proved there, and **D = 2.448 is not an upper bound for the diameter**:

- The two cone points of order 8 are the endpoints of the triangle side opposite the right angle. Its length is arccosh(cot²(π/8)) = arccosh((1+√2)²) = 2.448452…
- That side is a minimising geodesic in the double, because every path between the two points folds into the triangle without getting longer.
- So diam O(2,8,8) ≥ 2.44845 > 2.448, and the hypothesis "diameter at most D" of Lemma B.3 fails.

The numerical effect is nil: e^{3·0.00045} ≈ 1.0014, and the B₀ term is in any case negligible at t₃ ~ 10⁻¹¹. But as written the example does not satisfy the lemma it illustrates.

**Resolution.**

- **Diameter.** The double of a geodesic triangle has diameter at most the triangle's diameter, which is its longest side. That is computable in closed form, so use D = arccosh(cot²(π/8)), rounded *up*.
- **Systole.** Give the systoles in closed form:
  - ℓ(O(3,3,12)) = 2·arccosh((1 + 2cos(π/12))/2) = 1.862604…, so ℓ₀ = 1.8626 is a valid lower bound;
  - ℓ(O(2,8,8)) = 2·arccosh(1 + √2/2) = 2.256768…, which I found by a word search in the triangle group; a proof that this is the minimum is needed.
- Then δ₁ is genuinely proved for this example. State explicitly in Lemma B.3, and in Section 6 where it is used, that ℓ₀ and D are geometric inputs.

## MINOR

**m1. Abstract (p. 1) and the first paragraph of the Introduction (p. 2): locality is misstated.**

"The heat kernel on the diagonal depends, up to an error smaller than every power of t, only on the geometry within a distance of order √t." This conflates two different facts:

- The O(t^∞) locality (Kac's principle) holds for every *fixed* neighbourhood, with error O(e^{−ε²/Ct}).
- Within a ball of radius c√t the heat kernel is determined only up to an error of relative size about e^{−c²/C}, a constant and not a power of t.

The heuristic "felt within about √t/sin(π/m)" is fine as a heuristic. The "smaller than every power" clause should be attached to a fixed radius.

**m2. Theorem 2.3 and Lemma B.1 (pp. 8–9, 45).**

- The appeal to "the class [5] intend" is not a citation.
- The heat function ĝ_t(r) = e^{−t(1/4+r²)} is entire, and decays like a Gaussian in every horizontal strip. So it satisfies the standard admissibility hypotheses of Hejhal (vol. I) and Iwaniec (Thm 10.2) directly: h even, holomorphic in |Im r| ≤ 1/2 + δ, h(r) = O((1+|r|)^{−2−δ}).
- Lemma B.1 is correct, but it is a detour. I suggest citing the admissible-class theorem with its exact number and keeping Lemma B.1 only as a remark.

**m3. Lemma B.1, proof (p. 45).**

- State that ψ̂ is real and even, so that η_T ≥ 0 on the real axis. This is used but not said.
- The condition 2ε < ℓ (ℓ the systole) introduces a geometric quantity into a counting argument that does not need it. Any support of g in (−ℓ, ℓ) works, and ℓ > 0 is all that is used.

**m4. Proposition 2.7 and Section 4 (pp. 11, 32–33): the growth of the cone series is left heuristic, though it is easy to prove.**

Φ_m is analytic in |u| < π/m. So Cauchy's estimate on a circle of radius ρ < π/m gives φ_k(m) ≤ M_ρ·ρ^{−2k}. With (5) and (6), this gives a rigorous Gevrey bound |b_l(m)| ≤ C_ρ·l!·(4ρ²)^{−l}·(…), and an error bound for optimal truncation of the form exp(−c/(μ²t)). Section 4 currently states this only "heuristically, and without use in any proof". A proved version would make the second timescale (π/μ)² a theorem rather than an observation. This is a suggestion, not a defect.

**m5. Proposition 2.13 (pp. 16–17).**

- **(ii)**: say "for each L there are metrics (depending on L)". The Introduction (p. 6) and p. 18 say "for every L", which reads as "one pair of metrics for all L". That is false in general, and (iii) is the all-orders statement.
- **(ii), proof**:
  - say explicitly that G_l is computed on ℝ² and transfers because u_{l+1} is local and vanishes where the metric is flat;
  - say that the bumps are chosen with disjoint supports inside D₁ after shrinking.
- **(iii), proof**: say why the neighbourhood of z₀ is an *exact* flat cone. Near z₀ the metric is |(z−z₀)^{α₀−1}h(z)dz| with h holomorphic and non-vanishing, so w = ∫ (z−z₀)^{α₀−1}h dz is a cone coordinate. Also say that the same radius can be chosen on both sides.

**m6. Section 2.3, p. 13, "(it also follows from Proposition 2.7 by the weight argument …)".**

Scaling the K = −1 metric gives only K < 0. Extending to K > 0 uses the polynomial dependence of b_l and α_k on the jet (Donnelly). Say so in one clause.

**m7. Proposition 2.11(i): the hypothesis m ≥ max(2, l−1) and "For m ≤ l−2 nothing is claimed".**

See M1: the form Σ β_{l,i} Π_i(m) holds for all m ≥ 2. Only the evaluation on the radial part needs m ≥ l−1.

**m8. Remark 2.12 (p. 16).**

Its content rests entirely on code in the deposit (named by file in S7). I have no objection, since it is "used nowhere else". But I suggest an independent cross-check of the KΔK coefficients below the top one against the physics literature on curved cones that the authors cite ([13, (3.26)–(3.28)], [14]), if those cover t³. Otherwise, label the formula as computational in the statement itself.

**m9. Lemma B.3 (p. 47).**

The lemma uses the monotonicity of |b_{n−1}| in the *integer* order (Proposition B.2(a)). Say "integer cone orders at most μ₀". This is implicit, but Sections 3 and 6 also use b_l at real m.

**m10. Proposition 4.2(a) and Lemma 2.4 (pp. 9, 31).**

The factor e^{3·diam} makes the constant useless in practice: the supplement (S6) reports overestimates by factors of 4×10⁶ to 10¹⁰. A counting bound through the injectivity radius away from the cone points, or through the systole alone (Buser-type), would remove the diameter. If the authors keep the present bound, state in Proposition 4.2 that the constant depends on a non-spectral quantity. This is a suggestion, not a defect.

## PRESENTATION

**P1. Notational collisions in Section 2.** Each of the following symbols has two or more meanings:

| Symbol | Meanings |
|---|---|
| χ | Euler characteristic (p. 8); cut-off function (p. 14); polynomial χ_m (p. 18) |
| Φ | Φ_m (Lemma 2.6); a local isometry (Proposition 2.11) |
| ψ | ψ_k (Section 2.3); bump functions (Propositions 2.11, 2.13) |
| B | B (Lemma 2.5); Bernoulli numbers B_{2n}; the calligraphic fixed-point coefficients; B and Y (Lemma C.1) |
| C | 2 sin(ϑ/2); constants C; classes C (Definition 2.2) |
| a | a_l, the leading coefficient in Table 1; a_{l,k}, the coefficients of p_l (Lemma 2.10) |

This makes Section 2.4 hard to read. Please rename at least χ (cut-off), Φ (isometry) and the bump ψ.

**P2. p. 10, Lemma 2.5 proof.** In "…the bracket being nonnegative exactly on the range, which grows with ℓ", it is unclear what "which" refers to. Write "and the range grows with ℓ".

**P3. p. 14.** "B_l(Φ) = C^{−2l−2}(X_l + O(ϑ))" is announced, and then "B_l(Φ) = C^{−2l−2}T(ϑ) + O(C^{−2l})" is proved. State once that T(0) = X_l and that the coefficient of C^{−2l−2} in the even expansion is T(0).

**P4. p. 13.** "Section 3 is used only in Proposition 2.13, through Lemma 3.3" is a forward dependence. It is harmless, since Lemma 3.3 uses only Lemma 2.10, but say so to reassure the reader that there is no circularity.

**P5. Placement of Remarks 2.9 and 2.12.** Both are computational cross-checks "used nowhere else". They interrupt the logical line of Section 2 and would read better as remarks at the end of the section or in the supplement. This is a placement issue only.

**P6. p. 11, "envelop E_m and I".** Define "enveloping" once: the remainder has the sign of the first omitted term and modulus at most that term. Proposition B.2 proves exactly this, and readers outside asymptotics may otherwise read it loosely.

---

## Recommendation (for the part under review)

**Major revision.** Confidence: medium (about 0.65).

The constant-curvature core is correct, carefully proved and fully explicit. I would accept it as it stands, and I verified every closed-form formula and the enveloping inequalities independently. This core comprises Theorem 2.3, Lemmas 2.4–2.6, 2.8 and 2.10, Proposition 2.7 with (6), and Appendix B through Proposition B.2.

I recommend major rather than minor revision for one reason. Proposition 2.11 is stated as a theorem, but its proof has an unjustified structural step (M1a) and two sketched steps (M1b, c). In addition, the worked example of Lemma B.3 does not satisfy the lemma's hypotheses (M2).

Neither issue touches the main theorems. If the authors complete or explicitly downgrade the proof of Proposition 2.11 and repair Remark B.4, my recommendation for this part becomes **minor revision**.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1(a) | Prove that Donnelly's coefficient depends on A only through (I−A)^{−1} (w = (I−A)v, A(I−A)^{−1} = (I−A)^{−1} − I), hence B_l = C^{−2}P(cot(ϑ/2)); or cite the exact statement. |
| M1(b) | Define the radial jet as (k₀, k₁, …); prove the identification with the jet of dr² + f²dθ² modulo terms quadratic in non-radial modes. |
| M1(c) | A lemma on the uniformity in (u, ϑ) of the inversion s ↦ r and of the Laplace expansion. |
| M1(d) | Restate (ii) as a statement about the universal identity b_l = Σ_i β_{l,i}(radial jet) Π_i(m). |
| M2 | Use D = arccosh(cot²(π/8)) rounded up (or any proved upper bound) and the closed-form systoles; state that ℓ₀ and D are non-spectral inputs wherever a "proved error" is claimed. |
| m1 | Attach "smaller than every power of t" to a fixed neighbourhood; keep √t/sin(π/m) as a heuristic. |
| m2, m3 | Cite the admissible-class trace formula precisely; note that ψ̂ is real and even; drop 2ε < ℓ from the counting. |
| m4 | (Optional) prove the Gevrey bound on b_l by Cauchy estimates for Φ_m. |
| m5 | "For each L" wording; the locality and disjointness remarks in (ii); the exact-cone remark in (iii). |
| m6 | One clause on polynomial extension in K. |
| m7 | Weaken the hypothesis in (i), or explain why it is kept. |
| m8 | Cross-check against [13, 14], or label the formula as computational. |
| m9 | "Integer cone orders at most μ₀". |
| m10 | (Optional) a counting bound without the diameter, or an explicit note. |
| P1–P6 | Renaming and wording as indicated. |

---

The verification scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/A-b-brownian-cone-probabilist/scratch/code/` (`check1.py`, `check2.py`, `beta.py`, `omega.py`, `envelope.py`, `env2.py`, `remB4.py`, `systole.py`). The two Schueth papers I fetched are in `scratch/lit/`.
