<!-- Saved verbatim by the main session from the final message of reviewer A-b: the harness refused the reviewer's own write. Text from the report's first heading on; the reviewer's preceding cover note was dropped. -->
# Referee report: "How much of a hyperbolic orbifold does heat hear?" (Annals of Global Analysis and Geometry)

Referee remit: Section 2 in full (Sections 2.1 to 2.4), Appendix B (the proof of Proposition 2.7), and what later sections take from Section 2. My background is in heat invariants of singular spaces: cones, corners, and orbifold heat expansions. I read the rendered pages 2 and 6 to 14 of the manuscript as well as the extracted text. For literature I fetched Schueth, *On the corner contributions...* (arXiv:1812.06119, ref. [20]), Schueth, *Heat coefficients of surfaces with curved conical singularities* (arXiv:2511.22255, ref. [21]), and Uçar's thesis (ref. [13], pp. 134–143). All scripts are in `scratch/`: `constcurv.py`, `hinv.py`, `ucar_check.py`, `f61.py`, `fixedpoint.py`, `fixedpoint_fast2.py`, `analyse.py` and `an4.py`.

## Summary

Section 2 sets up the heat trace of a closed hyperbolic 2-orbifold with cone points from the Selberg trace formula (Theorem 2.3). It bounds the hyperbolic term explicitly (Lemmas 2.4–2.5). It then derives the full small-t expansion in closed form (Lemma 2.6, Proposition 2.7, Lemma 2.8, proved in Appendix B), with *enveloping* remainders (Proposition B.2, inequality (6)). From this it extracts the triangular "one new odd power sum per coefficient" structure (Lemma 2.10), which drives the rest of the paper.

Section 2.4 goes beyond constant curvature in two ways:
- **Proposition 2.11** gives the structure of the cone terms in variable curvature. Part (iv) is a new explicit t³ cone coefficient b₃.
- **Proposition 2.12** shows three things:
  - The constant-curvature counting transfers when the curvature is constant and flat to high order at the cone points, and the smooth parts agree.
  - For each L, the first L heat invariants of variable-curvature metrics hear only c₂.
  - Pairs with equal Σ(1−1/mᵢ) and Σ(mᵢ−1/mᵢ), including O(2,8,8) and O(3,3,12), carry metrics that are flat near their cone points and whose heat invariants agree to all orders.

## Significance

Sections 2.1–2.3 are mostly a careful re-derivation of known material: Donnelly; Dryden–Gordon–Greenwald–Webb; and Uçar, who computed every constant-curvature cone coefficient. The re-derivation comes directly from the trace formula, and two of its features are new and useful:
- the closed form (4)–(5) via Φ_m(u) = (cot u − m cot mu)/(4m sin u);
- the enveloping remainder bound (6) with explicit constants. This is what makes the stability and companion-paper results quantitative.

The paper says plainly that the coefficients are Uçar's and treats the agreement only as a check (Remark 2.9), which is the right attitude.

Section 2.4 contains genuinely new statements:
- the variable-curvature b₃;
- the all-order structure of Proposition 2.11;
- the Jacobi-field formula for the top coefficient β_{l,l+1};
- the clean construction of Proposition 2.12(iii).

They place the paper's constant-curvature counting in context. The main theorems of the paper do not depend on Section 2.4.

## Correctness and what was recomputed

Everything I recomputed agrees with the manuscript. I found no mathematical error in Section 2, Appendix B, or the places where later sections use Section 2. Specifically:

1. **Lemma 2.6 (p. 9).**
   - I checked numerically that the closed form of Φ_m equals the defining sum, for m = 2, 3, 5, 7 (30 digits).
   - I checked that the Taylor coefficients of the closed form equal formula (4) exactly, for k < 8 and the same m.

2. **Proposition 2.7 and (8) (pp. 9–10).** From (4)–(5) I recomputed:
   - p₀ = (m²−1)/12, p₁ = m⁴/360 + m²/36 − 11/360, p₂ = m⁶/2520 + m⁴/720 + m²/180 − 37/5040, all as printed;
   - p₃ = (m²−1)(m²+3)(3m⁴+2m²+19)/30240.

   The α_k formula gives α₀,…,α₅ = 1, −1/3, 1/15, −4/315, 1/315, −4/3465, matching the printed values and McKean's.

3. **Lemma 2.8.** For l < 8, p_l is even, has degree 2l+2, satisfies p_l(1) = 0, and has leading coefficient exactly |B_{2l+2}|/(2(l+1)!(2l+1)).

4. **Agreement with Uçar (Remark 2.9).** I read Uçar's (4.25), (4.33) and (4.34) from the rendered thesis pages. Both of the following hold exactly:
   - Uçar's cone contribution at κ = 1 equals p_ν(m)/m for ν < 12 and m ∈ {2, 3, 5, 8};
   - the identity m Φ_m^{(2k)}(0) = 2·4^k k! m c_k^S(π/m) holds for k < 6.

5. **Agreement with Schueth.** p₂ agrees with Schueth's Thm 4.1 (arXiv:1812.06119). Her b₂(Φ) = (12/C⁶ − 2/C⁴)K² − (2/C⁶)ΔK, Thm 3.7, uses the same sign convention Δ = −div grad.

6. **Trace formula to expansion (Appendix B, Proposition B.2, inequality (6)).**
   - I computed E_m(t) by direct quadrature of the elliptic integrals of Theorem 2.3 for m = 2, 3, 7 and t = 0.05, 0.2. For K = 0,…,5 the remainder E_m − Σ_{l<K} b_l t^l has the sign (−1)^K and modulus at most |b_K| t^K, as claimed.
   - I did the same for the identity term, t = 0.05, 0.3: (4π/Area)I − Σ_{k≤K} α_k t^{k−1} has the sign (−1)^{K+1} and modulus at most |α_{K+1}| t^K. All cases hold.
   - I also checked by hand:
     - the Euler-beta moment identity;
     - the integration-by-parts and monotonicity arguments of Lemma 2.5, including the inequality 1 + 2t/(ℓ−t) ≤ (2+3ℓ)/(2+ℓ), which is equivalent to the range t ≤ ℓ²/(2(1+ℓ));
     - the counting of Lemma 2.4;
     - the eigenvalue count and the dominated convergence in Lemma B.1.

7. **Section 2.3 and later uses.**
   - (10) for triangles holds symbolically.
   - The heat-invariant differences of the paper's pairs (computed from (7)) are:
     - (0;2¹⁰) vs (1;4⁴): (0, 0, 1/2, −7/4, 179/24);
     - O(2,8,8) vs O(3,3,12): (0, 0, 25/12, −1775/24, 153025/48);
     - (0;5,5,5) vs (0;2,2,2,10): (0, 0, 9/5, −369/10, 19863/20).

     These confirm Theorem 1.2(ii), Theorem 1.4(ii) and the values d₃, d₄, d₅ quoted in Section 4.
   - Proposition 6.1 is correct: the absolute row sums of F⁻¹ are 2, 14, 498, 4062, 56230/3, and row 2 is (−18, −120, −360), as printed.

8. **Proposition 2.11, independent computation.** I wrote my own code, using a method different from both of those mentioned in the Sketch.
   - **Setup:** a rotationally symmetric germ with K(r) = K₀ + K₂r² + K₄r⁴ + K₆r⁶ in normal coordinates. I solved Synge's world function from the Hamilton–Jacobi equation and the Minakshisundaram–Pleijel transport equations as exact power series in (x, y). I evaluated the fixed-point integral ∫H(t, x, R_ϑx) dA by Laplace's method. The results are exact rationals, as polynomials in 1/C² with C = 2 sin(ϑ/2).
   - **Validation:** the code reproduces Donnelly's B₀ and B₁ and Schueth's B₂ exactly, including the ΔK term.
   - **Results:**
     - **(iv) is correct exactly.** After the m-sum, I obtain b₃ = (m²−1)(m²+3)(3m⁴+2m²+19)/(30240m)·K³ − (m²−1)(7m⁶+47m⁴+173m²+733)/(201600m)·KΔK + (m²−1)(m²+11)(3m⁴+10m²+227)/(3628800m)·Δ²K. Here Δ²K is computed with the true Δ_g, which gives Δ²K(p) = 64K₄ − (8/3)K₀K₂ for this germ. The difference from (iv) is identically zero. At l = 3 no non-radial term can enter for m ≥ 2, so for orbifold cone points this is a complete check.
     - **(i): the Π-structure holds** with β_{l,1} = 0 for l = 1,…,4. Explicitly, β_{2,2} = −2K², β_{3,2} = 4K³/3 and β_{3,3} = 8KΔK − 32K³.
     - **(ii): the Jacobi-field formula** β_{l,l+1} = 4^l l! [v^{2l}](J⁻¹)′(v) holds exactly for l = 1, 2, 3, 4. Examples: β_{2,3} = 12K² − 2ΔK and β_{3,4} = 120K³ − 42KΔK + Δ²K, both as printed. For l = 4, β_{4,5} = 1680K⁴ − 904K²ΔK + (124/3)(ΔK)² + (98/3)KΔ²K − (1/3)Δ³K, consistent with (2l)!/l!·K^l + … + 2/(l−1)!·(−Δ)^{l−1}K.
     - **(iii): the linear part** is exactly (2/(l−1)!)(−Δ)^{l−1}K·(2 sin ϑ/2)^{−2l−2}, top pole only. I checked this for l ≤ 5; at l = 5 I get B₅ ⊃ 12288·K₈/C¹², as predicted.
     - **Constant curvature:** b₄ reduces to K⁴p₄(m)/m.
   - **Π polynomials:** m Π_i(m) is even, vanishes at m = 1 and has leading coefficient |B_{2i}|/(2i)! for i ≤ 5. In particular m Π₄ = (m²−1)(m²+11)(3m⁴+10m²+227)/3628800, so the Δ²K coefficient in (iv) is exactly Π₄, as (iii) predicts.

9. **Proposition 2.12.**
   - The second-order constant ω_n = (−1)^n n(n−1) n!/(2n+1)! agrees exactly with the second-order (curvature-squared) heat-trace form factors of Barvinsky–Vilkovisky, reduced to a conformally flat metric in dimension 2. I checked l = 1,…,7; at l = 1 it reproduces the classical a₂ = (1/4π)(1/15)∫K².
   - The flat metric in (iii) is correct. Checks: the cone angle at ∞ is 2π exactly when α₀ = Σ(1−1/mᵢ) − 1, and the defects sum to 4π. For O(2,8,8) and O(3,3,12), Σ(1−1/m) = 9/4 and Σ(m−1/m) = 69/4 for both.
   - The c₂ identity χ/6 + Σ(m²−1)/(12m) = (2−2g)/6 + Σ(m−1)²/(12m), and the example (0;2⁸) vs (0;3,3,3) (both give 2/3), are correct.
   - The weight and Jacobian arguments in the Sketch of (i) and (ii) are sound as far as they go (but see M1).

In short, every explicit formula of Section 2 that I could test is correct. What remains is about how Section 2.4 is proved and documented.

## MAJOR issues

**M1 (gap in proof, not an error). Section 2.4, Propositions 2.11 and 2.12 (pp. 12–13): stated as propositions, but proved only by "Sketch".** These are new results; nothing in the literature I know covers them beyond l = 2. The load-bearing steps are asserted, not shown. In Proposition 2.11:
- **(i):** the claim that (2 sin ϑ/2)^{2l+2}·B_l is bounded for every l, said to follow by "following the substitution of Schueth's proof to all orders". This is the whole pole-order statement, and it needs an argument. One route: a Laplace-method count of r-powers against t-powers, with every coefficient polynomial in cos ϑ, sin ϑ. Another: Donnelly's degree bound on the polynomial in the entries of (I−A)⁻¹.
- **(ii):** the claim that "only the leading Gaussian and the area element reach the pole". The formula is right; I verified it for l ≤ 4. But it needs a proof that the u_k with k ≥ 1, and the corrections of σ(x,Rx) beyond the Jacobi-field term, contribute only to lower poles.
- **(iii):** a "first-order Duhamel expansion" whose result is stated without computation.
- **(iv):** "an exact computation" that is not shown.

In Proposition 2.12:
- **(ii)** is a three-paragraph sketch of a gluing and implicit-function argument (bumps, scales, a ball about w₀, a flat cylinder).

The Introduction (p. 3) and the closing paragraph of Section 2.4 (pp. 13–14) present these as results of the paper. By AGAG standards a statement labelled "Proposition" needs a proof. I have confirmed by an independent method that the explicit claims are correct (item 8 above), so this is a matter of rigour, not truth.

**M2 (reproducibility). The computations behind Proposition 2.11 are not documented.** The Sketch ends by citing "an exact computation" for (iv) and "an independent computation by a different method (a Duhamel expansion about the flat rotation with exact Gaussian traces)" that "confirms (i) and (ii) for l ≤ 5, (iii) for every l, and (iv) exactly". Section S8 of the supplement describes every other computation in the paper but says nothing about these: no method, truncation orders, normalisations or program. In addition, "confirms (iii) for every l" cannot be the output of a computation. Either (iii) is proved for all l, in which case the proof should be given, or it was checked up to some l, which should be stated.

## MINOR issues

**m1 (p. 12, Sketch of 2.11(i); a gap, harmless for the conclusion).** The sketch says "B_l is even in ϑ (a reflection conjugates R to R⁻¹)". A reflection is an isometry only of a reflection-symmetric germ. For a general germ, naturality gives only B_l(ϑ; jet) = B_l(−ϑ; σ*jet). An individual B_l(R) can therefore contain odd powers of cot(ϑ/2), multiplied by pseudoscalar invariants of the jet. The conclusion for b_l is still correct for two reasons:
- R^{m−j} = R^{−j}, so the average over j pairs ϑ with −ϑ and cancels odd terms;
- for m ≥ l−1 pseudoscalars cannot occur anyway, by the same Fourier-mode count as for the non-radial terms.

Please argue this way, or state the polynomial structure only for the average.

**m2 (p. 12, Proposition 2.11(ii)).**
- The coefficient-extraction notation [v^{2l}] is not defined.
- "J(r) being the length of the distance circle of radius r about p divided by 2π" should say "in an orbifold chart": on the orbifold the circle has length 2πJ(r)/m.
- "In general the corresponding average over directions" is undefined. Please define J̄(r) = (1/2π)∫J(r,θ)dθ in the chart. Then either prove that the formula holds with J̄ when m ≥ l−1, which I believe follows from the non-radial count, or restrict (ii) to rotationally symmetric germs.

**m3 (p. 11, end of Section 2.3).** "At constant curvature K the expansion holds with K^l in place of (−1)^l". This should also say that the smooth coefficients become α_k(−K)^k. As written, a reader may apply the replacement to the cone terms only.

**m4 (p. 11, opening of Section 2.4).** Ω_l = (1/4π)∫u_{l+1} dA uses local coefficients u_k whose normalisation is never fixed (u₀ = 1, u₁ = K/3, with the convention Δ = −div grad). Ω₀ = χ/6 depends on it. Please state it.

**m5 (p. 13, Proposition 2.12(i)).** Two statements need narrowing:
- "Lemma 3.3 holds verbatim in this class" is not literally true. In this class equal c₁ no longer means equal χ: the first condition of (13) comes from the hypothesis Ω₀(O) = Ω₀(O′), not from c₁. Likewise, the converse clause of Lemma 3.3 ("equal area") must become "equal Ω₋₁ and Ω₀".
- "So does everything deduced from it" is too vague. Please list which results transfer (presumably Theorems A, 3.4, 3.8 and 3.11, Corollary 3.5 with χ in place of the area) and note that the transferred statements are conditional on equality of the Ω_l, which are not heat invariants.

**m6 (p. 13, Sketch of 2.12(ii)).** The area is fixed with "a flat cylinder of adjustable length", but the metrics constructed earlier only have "two flat discs". A cylinder cannot be lengthened inside a flat disc. Build a flat cylinder into the construction from the start. Also say that it is the orbifold with smaller area whose cylinder is lengthened.

**m7 (p. 14, lines 2–4).** "Short of knowing those, heat invariants of any finite order hear only c₂" overstates 2.12(ii), whose metrics depend on L. Suggested wording: "for every L there are metrics … with the same first L heat invariants whenever c₂ agrees". Only for pairs as in 2.12(iii) does one get agreement at all orders.

**m8 (p. 12, Sketch, last sentence; and Problem 5(a), p. 36).**
- Since (iv) determines β_{3,2} = 4K³/3 and β_{3,3} = 8KΔK − 32K³, please print them; the paper prints only β_{3,4}.
- Problem 5(a) asks for β_{l,i}, i ≤ l, for l ≥ 4. For m ≥ l−1 this is a finite, routine computation of the kind in item 8. For m ≥ 3 my computation gives:
  - β_{4,1} = 0;
  - β_{4,2} = −(2/3)K⁴;
  - β_{4,3} = 52K⁴ − (52/3)K²ΔK + (1/3)(ΔK)²;
  - β_{4,4} = −600K⁴ + 280K²ΔK − 10(ΔK)² − (20/3)KΔ²K;
  - β_{4,5} as in item 8.

  At weight 8 with m ≥ 3, the five monomials K⁴, K²ΔK, (ΔK)², KΔ²K and Δ³K are the only invariants, and a radial germ separates them. The authors may wish to check these values against their own code. Either way, Problem 5(a) should be reformulated as asking for a closed form in l, or for the case m ≤ l−2, rather than for individual l. Separately, β_{l,1} = 0 for all l ≥ 1 is suggested by l ≤ 4 and may be worth stating, or asking about.

**m9 (p. 8, proof of Theorem 2.3).** The heat function ĝ_t is already admissible for the standard Selberg trace formula: it is entire, and in the strip |Im r| ≤ 1/2 + ε it decays like a Gaussian. Hejhal [37] and Iwaniec [38, Thm 10.2] state the formula for such h. Lemma B.1 is correct, so this is not an error. But a one-line remark that a standard admissible class covers the heat function would make clear that Appendix B is a convenience, not a necessity.

**m10 (p. 9, Proposition 2.7).** "Through the polynomial p_l, b_l extends to every real m > 0" should say that the extension is purely algebraic. For a non-integral cone angle with nonzero curvature, the actual cone coefficient is a different object: Schueth [21] shows that half-integer powers and logarithmic terms can occur for general curved cones. Section 6 already says that real orders give heat invariants of an orbifold only when they are integers; a matching sentence here would prevent misreading.

## Presentation (figures, captions, notation, exposition)

- **Figure 1 (p. 2).** The colour bar runs to 12, but the darkest rendered pixels (the order-8 tips in (a), the order-12 tip in (b)) are about 4–6 on the scale. The value 4πt·h_t(p,p) ≈ m(1 − t/3) is reached only at the vertex itself, which the rendering cannot resolve at the tip of a π/12 angle. Please say so in the caption, or mark the vertex value, so that readers do not take the figure to show cone values near m.
- **Sketch proofs (pp. 12–13).** See M1. If the authors keep some statements without full proof, use "Remark" or "Claim", and keep "Proposition" for proved statements. The paper is otherwise careful about what is proved and what is computed (Section S8, Remark 2.9), and Section 2.4 should meet the same standard.
- **Table 1** helpfully lists Ω_l, Π_i and β_{l,i}. It would also help to add u_k (see m4) and C = 2 sin(ϑ/2), which Section 2.4 uses implicitly through (2 sin ϑ/2)^{−2}.
- **Prop. 2.11(iii) and the paragraph after it (pp. 12–13).** The paragraph says the linear parts form "a power sum with an independent weight at each cone point, which no longer defines a Prouhet–Tarry–Escott condition". This is a heuristic remark and should be phrased as one.
- **Notation.** The heading of Proposition 2.11 says "orbisurface" while the rest of the paper says "orbifold"; use one term. In Proposition 2.11(i) the hypothesis "m ≥ max(2, l−1)" would read better as "m ≥ l−1 (and m ≥ 2)", with a pointer to Problem 5(b) for the excluded case.
- I found no sign or typographical errors in the rendered formulas of pages 6–14. In particular, Lemma 2.5, (3), (4), (5), (6), (8), (10) and Proposition 2.11(iv) are correctly typeset.

## Recommendation

**Minor revision** as far as Section 2 is concerned.

- **Confidence: high** for Sections 2.1–2.3, Appendix B and their later uses. All formulas were recomputed independently and agree with Uçar, Schueth and direct numerical quadrature of the trace formula.
- **Confidence: moderate-to-high** for Section 2.4. Every explicit claim I could test is correct, by a method independent of the authors', but the general-l statements rest on sketches.

If the authors choose to write full proofs for Propositions 2.11 and 2.12, the revision becomes more substantial, though I expect no mathematical change.

## What resolves each issue

- **M1:** Either give complete proofs of Propositions 2.11(i)–(iv) and 2.12(ii), in an appendix if preferred, or relabel the parts that remain unproved as remarks or claims, stating exactly what is proved and what is computed. The minimum full proof would cover three points:
  - the pole-order bound for all l, by a Laplace-method count or Donnelly's degree bound;
  - the reduction of the top pole to the Jacobi-field integral;
  - the linear-response computation for (iii).

  For (iv), an exact computer-algebra derivation documented in the supplement is acceptable.
- **M2:** Add a subsection to S8 describing the variable-curvature computations: method, truncation orders, normalisations, the range of l checked for each claim, and the program in the deposit. Replace "(iii) for every l" with either a proof or the range actually checked.
- **m1:** Replace the reflection argument with the j ↔ m−j pairing, or restrict the structure statement to the average b_l.
- **m2:** Define [v^{2l}], say "in an orbifold chart", and define J̄ or restrict (ii) to radial germs.
- **m3:** Add "and α_k by α_k(−K)^k".
- **m4:** State the normalisation of u_k.
- **m5:** Reword "verbatim" and list the results that transfer, with the Ω-hypotheses explicit.
- **m6:** Put a flat cylinder into the construction from the outset.
- **m7:** Reword as suggested.
- **m8:** Print β_{3,2} and β_{3,3}, and reformulate Problem 5(a). Optionally include the l = 4 values after checking them.
- **m9:** One sentence noting that the heat function is admissible in the standard trace formula.
- **m10:** One sentence saying that the real-m extension is algebraic only.
- **Presentation:** Revise the Figure 1 caption, the labelling of sketched statements, and the Table 1 additions as above.
