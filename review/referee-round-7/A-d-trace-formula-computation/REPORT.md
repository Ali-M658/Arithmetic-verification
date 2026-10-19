<!-- Referee A-d: returned text saved verbatim; the reviewer could not write files -->

The REPORT.md write was refused (subagents may not write report files), so the full report follows.

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

**Remit.** I reviewed:
- Sections 4 and 5.
- Lemmas 2.4–2.5 (Proposition 4.2 depends on them).
- Appendix B, including Lemma B.3 and Remark B.4.
- Appendices D and E.
- Supplement sections S2 and S4–S6, plus S7 where it describes these computations.

I treat the marked placeholders as known. Page numbers are manuscript pages, or "S p." for the supplement. I read the rendered page images before reporting any figure or typesetting point.

---

## 1. Summary

**Section 4** makes three points:
- Heat invariants depend only on the signature (Corollary 4.1, via the dimension of Teichmüller space).
- Proposition 4.2 bounds the difference of the heat traces of two orbifolds with the same signature: |Z₁ − Z₂| ≤ B(ℓ, diam, t) ≤ C_hyp t^{−1/2} e^{−ℓ²/4t}. When the weighted length spectra differ, the exponent and the power of t are attained.
- Computed spectra illustrate two timescales:
  - the cone timescale (π/μ)², for the minimal pair O(2,8,8), O(3,3,12);
  - the geodesic timescale, for a one-parameter family of (0;3,3,3,3) pillows.

  Remark 4.3 explains the cone timescale through the wave-trace kernel k_m.

**Section 5** proves:
- Three heat invariants determine a hyperbolic triangle orbifold (Corollary 5.1).
- The reciprocal-sum strata are separated for sums up to 17, and adjacent strata first overlap at S*(p) (Theorems 5.4–5.6).
- O(2,8,8), O(3,3,12) is the unique collision of least sum (18), and also of least area (Theorem 5.7).
- The pair is isolated: collisions in its class are the rational points of C_{27/2}. This cubic is isomorphic to E: y² = x(x+9)(x+384), which has rank 0 and E(Q) ≅ Z/2 × Z/6 (Theorem 5.8; hand descent in Appendix E).

## 2. Significance

**Strengths.**
- Section 5 is clean, complete and correct.
- The stratum analysis (Lemmas 5.2–5.3, Theorem 5.4) is an exact and elegant explanation of the threshold 17.
- Reducing isolation to a single elliptic curve, with a 2-descent a reader can check by hand, is attractive.
- Remark 4.3 is illuminating: the radius 2π/m of the Taylor series of k_m is the source of the l!(m/π)^{2l} growth.
- The numerics in S4–S6 are careful and honestly labelled: the paper says they are not enclosures and that no proof uses them.

**Weaknesses (detailed in M1 and M2).**
- Most of Section 4 is classical in substance, as the authors say themselves.
- The explicit constant of Proposition 4.2 grows like e^{3·diam}, and the signature does not control the diameter. So the constant says little.
- The computations illustrate facts that are already proved.
- The triangle results are elementary once Theorem A is available; Corollary 5.1 is the n = 3 case.

The genuinely new content in my part is the strata theorem, the identification of the minimal pair, and the isolation theorem. All three are correct and nice, but modest in depth for AGAG on their own.

## 3. Correctness, and what I recomputed

I found no mathematical error in Sections 4–5, Appendix B, Appendices D–E or Lemmas 2.4–2.5. One numerical claim disagrees with my computation (m1).

### Proofs checked line by line

**Lemmas 2.4 and 2.5.**
- The counting argument via a Dirichlet domain is correct.
- Integration by parts needs −φ′ ≥ 0 on [ℓ, ∞). On the stated range this holds; at x = ℓ it reduces to t(2 − ℓ) < ℓ².
- The tail bound 2tℓ/(ℓ − t) · e^{ℓ/2 − ℓ²/4t} is correct.
- The constant C_hyp and the factor (2 + 3ℓ)/(2 + ℓ) are correct.
- The sign of the logarithmic derivative of B in ℓ is correct.

**Proposition 4.2.**
- (a) is correct.
- (b) is correct; dropping the boundary term −φ(L′)·n(L′−) ≤ 0 is legitimate.

**Corollary 4.1.** The dimension count and the countability argument via Out(Γ) are correct.

**Remark 4.3.**
- I verified the Fourier identity analytically, by averaging sech((u ± ia)/2).
- I evaluated E_m(t) two ways, from the r-integral of Theorem 2.3 and as ∫ g_t k_m, for m = 2, 3, 8, 12 at t = 0.0015 and 0.34. The values agree to 15 digits.
- The poles at ±2πi/m are simple for every m ≥ 2, including m = 2, where k₂ = 1/(8 cosh(u/2)).

**Appendix B.**
- Lemma B.1, the proof of Proposition 2.7, the sign and modulus bookkeeping of Proposition B.2, inequality (6), and Lemma B.3 are all correct.
- Remark B.4: I recomputed Q₃ = 303.63 and ‖V⁻¹‖_∞ = 16/t₃².
- This gives δ₁ = 4858·t₃, the threshold t₃ ≤ 7.8×10⁻¹¹, and η ≤ 2.07×10⁻¹⁹. All match the paper.

**Section 5, in exact arithmetic.**
- The factorisation of φ_p − τ_p and the formula for φ_p′ are correct.
- gap_p(3p+7) = −2(p² − 5p − 30)/(p(p+1)(p+3)(p+4)(p+5)) holds for every p ≤ 60.
- Every listed gap value is correct: 1/840, 1/2310, 1/10296, the seven values at S*(p)+1, the two 1/12's, and gap₂(18) = 0.
- R⁻_{18,3} = 101/168, attained at (3,7,8).

**Theorem 5.4 by brute force.** For every 2 ≤ p < 40 I computed the first overlap from the actual triads, checked it persists through S ≤ 3p + 80, and it equals S*(p) in every case.

**Theorems 5.5 and 5.7.** There are 83 hyperbolic triads with 10 ≤ S ≤ 18, with exactly one coincidence. The majorisation and least-area arguments are correct.

**Proposition D.1.** Brute force over p < 200 and S ≤ 3p + 400 finds exactly the tangencies (2,18) and (4,20).

**Theorem 5.8.**
- Symbolically, ψ(E) ⊂ C_{27/2} and φ∘ψ = id modulo the equation of E.
- Δ = 2¹⁸·3⁸·5⁶ and j = 4102915888729/9000000.
- c₄/2⁴ equals c₄ of LMFDB 90.c3 = [1,−1,1,−3002,63929]. The LMFDB API record agrees: same j, rank 0, torsion [2,6].
- All 11 affine points lie on E, and #E(F₇) = #E(F₁₁) = 12.
- The tangent line at (16,400) gives (x − 16)³, so (16,400) is a flex.
- The 12 listed points lie on C_{27/2}, and ∇C = 0 only at the origin.

**Appendix E (descent).** I redid it by hand and it is correct:
- The classes ±2, ±3 are excluded mod 5.
- The image of the descent map is {1, 6, −1, −6}.
- On E′: the bracket for class 3 is ≡ 1 (mod 3); class 5 reduces to f ≡ 2M⁴, or a bracket ≡ 2 when 3 | M; class 15 needs a mod-9 step, where 5w² − w + 2 ≡ 6.
- So the rank is 0.

### Numerical claims recomputed

**Heat invariants of the pair.**
- p₀, p₁, p₂ and α₀, …, α₄ agree with the paper.
- c₁ = 1/8 and c₂ = 67/48 for both orbifolds; P₃ = 1032 and 1782.
- d₃ = 25/12, d₄ = −1775/24, d₅ = 153025/48 exactly.

**Growth heuristic (p. 33).** The quantity |b_l|·√l / (l!·(m/π)^{2l}) stabilises at about 0.092, 0.234 and 0.345 for m = 2, 8, 12 (checked to l = 18).

**Closed geodesics (S4).**
- My enumeration is complete. It uses the displacement bound d(x₀, γx₀) ≤ ℓ + 2·rad(F) from the proof of Lemma 2.4, with weights w(x) = Σ length(axis ∩ F).
- O(2,8,8): lengths 2.25677, 2.88164, 3.05714, with w/ℓ = 2, 4, 3.
- O(3,3,12): lengths 1.86260, 2.98068, 3.40275, with w/ℓ = 2, 4, 2.
- These confirm the stated lengths and the fitted leading multiplicity 2.

**Hyperbolic term of O(3,3,12).** 2.64×10⁻¹⁵ at t = 0.025, 3.96×10⁻¹³ at t = 0.0293, and 7.81×10⁻¹³ at t = 0.03, all as claimed.

**D(t) from the trace formula.**
- At t = 0.0015 the elliptic part is 2.96855×10⁻³, against 2.96935×10⁻³ from the three-term expansion.
- The maximum is 0.0469 at t ≈ 0.116.
- The geodesic share of D is 0.5% at t = 0.10 and 2% at t = 0.12.
- **The sign change is at t ≈ 0.359, not 0.34** (m1).

**Family (0;3,3,3,3).**
- The systole is 4b(ϑ), from 2.6339 down to 0.6940. Its multiplicity is 2 for ϑ > 0, and 4 at ϑ = 0, where 4a = 4b.
- At t = 0.33, geodesics of length between 6.5 and 7.5 contribute at most 1.6×10⁻¹⁴. This supports the claimed agreement to 1.1×10⁻¹³ with a length cutoff of 6.5.
- The leading terms at the emergence condition ℓ²/4t* = 24.5 are 5×10⁻¹¹ to 1.8×10⁻¹⁰, consistent with the circles in Fig. 5(b).
- With diam = 2·diam(Q) I reproduce the overestimate factors 4.4×10⁶ and 1.0×10¹⁰ (see M2).

**Computation S2.1 and Table S2.**
- My exact enumeration up to S = 1200 finds exactly the 38 listed collision-free sums.
- S = 557 has 25,575 triads.
- All rows of Table S2 for p = 2 to 14 are reproduced.
- The first non-adjacent collision is (5,15,15), (7,7,21) at S = 35.
- I did not extend the enumeration to S = 4800.

**Table S6.** The recovered roots are reproduced: 8 ± 0.0050i and 2; 11.99995, 3.0085 and 2.9915. The margins of about 100 and 20 are also reproduced.

**Not recomputed:** the finite-element eigenvalues, λ₁ of the family, the Bolza benchmark, and the error budgets.

## 4. FATAL

None.

## 5. MAJOR

**M1. What Section 4 adds (pp. 29–33; p. 5).**
- Corollary 4.1 is standard, and Proposition 4.2(b) is classical by the authors' own account (pp. 30, 32).
- The numerics illustrate proved facts but are worded as if they were evidence:
  - p. 30: "shows on computed spectra that the expansions … first differ at the third order". This is just d₃ = 25/12 ≠ 0.
  - p. 33: "the coefficients d₃, d₄ are tested by the fit". The computed D already matches the exact elliptic difference to 4×10⁻¹⁴, so the fit tests the finite-element computation, not d₃ and d₄.
- As written, the section reads as validating a finite-element code against the trace formula.

*Resolution:*
- State what is new: the explicit constant in Proposition 4.2(a), and Remark 4.3.
- Reword the two places so the numerics illustrate proved identities.
- Move Remark 4.3 forward.

**M2. The explicit constant of Proposition 4.2(a) carries little quantitative information, and its looseness is misattributed (pp. 31–32; S p. 14).**
- C_hyp contains e^{3·diam} through Lemma 2.4. The diameter is unbounded on each moduli space, so "a constant controlled by the diameter" (p. 5) gives no bound uniform in the moduli for a fixed signature and systole.
- Page 32 attributes "factors up to 10¹⁰" to the e^{3·diam} of Lemma 2.4. The supplement shows that diam was replaced by 2·diam(Q).
- With the true diam(Q) I get about 4.0×10³ (for ϑ = 0.4) and 8.8×10⁴ (for ϑ = 2.8). So three to five orders of magnitude come from the authors' choice of diameter bound, not from the lemma.

*Resolution, either of:*
- Prove a diameter-free count n_O(x) ≤ C(Area, signature)·eˣ, for example by a Buser-type thick–thin argument (Buser, Lemma 6.6.4) adapted to cone points.
- At minimum: give the true or proved diameter, state on p. 32 that the 10¹⁰ factor used 2·diam(Q), and stop presenting the "explicit constant" as a contribution.

## 6. MINOR

**m1 (p. 33; S pp. 11, 12): "sign change near t ≈ 0.34".**
- Theorem 2.3, with the elliptic terms (checked two ways) and the complete length spectra up to 6.5, puts the sign change at t = 0.359. Cutting the spectrum at 5.5 changes it only in the fourth digit.
- At t = 0.34, D = +0.0035: elliptic part 0.0448, geodesic part −0.0413.
- Measured on a 300-dpi render, Fig. 5(a) crosses zero at about 0.35 ± 0.01.

Correct the number or explain it.

**m2 (p. 30; S p. 12; S p. 14): completeness of the geodesic enumeration.**
- "Words of length at most 10" is not a completeness criterion for a length bound.
- Integrality of w/ℓ cannot detect a missing conjugacy class.
- Use the displacement bound from the proof of Lemma 2.4. With it, the non-isometry of the eight members becomes provable (distinct systoles, certifiable with interval arithmetic).
- My enumeration with this criterion confirms all the stated values.

**m3 (p. 37; Table S2 caption, S p. 8): touching versus overlapping.**
- "Touch without overlapping" contradicts the definition on p. 35 and Lemma 5.3(ii): gap = 0 counts as overlap.
- The caption's claim "vanishes only for p = 2, 4 (Proposition D.1)" is a non sequitur. Proposition D.1 is about equality of the extreme values only; a collision among interior values at the first-overlap sum is not excluded. The table supports the claim only for p ≤ 14.

**m4 (p. 33).**
- "Truncating (6) at its smallest term": (6) is an inequality; you mean the cone series.
- The asymptotic |b_l(m)| ~ C_m l^{−1/2} l! (m/π)^{2l} is a routine Darboux argument, given simple poles at ±π/m and the next singularity at 2π/m. Prove it in a few lines or keep it labelled a heuristic. My numerics agree with it up to l = 18.

**m5 (Fig. 4, pp. 30–31).** At ϑ = 0 the systole is attained by two geodesics (w/ℓ = 4), and λ₁ looks double: two curves leave 4.12 in panel (b). Say so.

**m6 (Remark B.4, p. 47).**
- "D = 2.448 (its computed diameter)": "its" is ambiguous.
- Lemma B.3 needs a proved diameter bound if δ₁ is to be "proved". The numerical effect is nil, since B₀ is about e^{−10¹⁰} at these t. Either supply a proved bound or note that any D works here.

**m7 (p. 33).** "Against orbifolds outside the triangle family … (0;5,5,5) and (0;2,2,2,10)": O(5,5,5) is itself a triangle orbifold. Rephrase. I checked that both have area 4π/5 and c₂ = 17/15.

**m8 (S p. 14).** "Traces differ by up to 0.79": I get |Z₀ − Z_{2.8}| = 0.782 at t = 0.33, so write 0.78.

**m9 (p. 39).** Nonsingularity of C_{27/2} also follows from a one-line check that ∇C = 0 only at the origin. Optional.

## 7. Presentation

- **P1 (p. 30):** "records … records" is repeated.
- **P2 (p. 33):** two consecutive parentheticals; merge them or move one to the caption.
- **P3 (pp. 35–39), notation clashes:**
  - φ_p(S), the map φ of Theorem 5.8, and ϕ_k(m).
  - The base point O and the orbifold 𝒪.
  - gap_p(S) and the "gap" column of Table S2.
- **P4 (Fig. 5):** the caption should say both panels use a logarithmic t-axis.
- **P5 (p. 32):** "tested by the fit"; see M1.
- **P6:** Figs. 4–7 render correctly. The axes match the text (square-root scale in Fig. 4(b), log axes in Fig. 7), and the circles in Fig. 7 match Table S2. I found no sign or typesetting errors in the displayed formulas of Sections 4–5 or Appendices B, D, E.

## 8. Recommendation

**Minor revision** for the part under my review.
- **Correctness:** high confidence. Every proof was checked and every number I could recompute was recomputed; only m1 disagrees.
- **Significance:** moderate confidence that this material is of AGAG level on its own. M1 is for the editor's overall weighting together with the reports on Sections 2, 3 and 6.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | State what is new in Section 4; reword "shows on computed spectra" (p. 30) and "tested by the fit" (p. 33); move Remark 4.3 forward. |
| M2 | Prove a diameter-free geodesic count; or disclose the 2·diam(Q) choice, give the true-diameter factors (about 4×10³ to 9×10⁴), and drop the "explicit constant" claim on p. 5. |
| m1 | Correct the sign-change time to about 0.36, or explain 0.34. |
| m2 | State a provable completeness criterion for the geodesic enumerations. |
| m3 | Fix "touch without overlapping"; restrict or prove the Table S2 caption claim. |
| m4 | Fix the wording; prove the growth asymptotic or keep it a heuristic. |
| m5 | Note the multiplicities at ϑ = 0. |
| m6 | Use a proved diameter bound, or note that it is irrelevant here. |
| m7 | Rephrase the (0;5,5,5) sentence. |
| m8 | Write 0.78. |
| m9 | Optional direct nonsingularity check. |
| P1–P5 | Editorial. |

My verification scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/A-d-trace-formula-computation/scratch/code/`:
- `exact_checks.py`
- `collisions.py`
- `curve.py`
- `remB4.py`
- `geod.py`
- `run_tri.py`
- `run_quad.py`
- `quad_tail.py`
- `Dt.py`
- `Echeck.py`
- `growth.py`

The page renders are in `.../scratch/img/`.
