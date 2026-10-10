<!-- Saved verbatim by the main session from the final message of reviewer B-b: the harness refused the reviewer's own write. Text from the report's first heading on; the reviewer's preceding cover note was dropped. -->
# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (submitted to Annals of Global Analysis and Geometry)

I could not write `REPORT.md`: the harness refused the write. The complete report follows. Scripts and renders are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-5/B-b-hyperbolic-geometer/scratch/`: `consts.py`, `quad.py`, `systole.py`, `fem.py` and `renders/`.

Referee B-b: hyperbolic geometry (Fuchsian groups, orbifold Teichmüller theory, collars, systoles). My remit is Sections 4 and 8 and every geometric input the rest of the paper takes from them: Lemma 2.2 (via the diameter), the uses of D, ε and Area ≥ π/21 in Theorem 6.2 and Table 3, and the systole and diameter inputs of Section 7 (Table 4). I read the rendered pages (110 dpi renders of all pages, 200 dpi of pp. 13 and 22) as well as the extracted text.

## Summary

The paper proves an effective statement. In the class C(A, ε, M) (area ≤ A, systole ≥ ε, cone orders ≤ M), the first N eigenvalues, each known to within δ, determine the signature, and N and δ are given by explicit formulas. The method compares the heat trace with the signature term G_σ of the Selberg trace formula at a small time t*.

Section 4 supplies the geometry:
- three facts of plane hyperbolic geometry (Lemma 4.1);
- a lower bound d0 for the separation of elliptic fixed points (Lemma 4.2);
- a lower bound v0 for the area of balls (Lemma 4.3);
- the resulting packing bound D(A, ε, M) for the diameter (Theorem 4.4). Through Lemma 2.2, D controls the closed-geodesic term.

Section 8 discusses the hypotheses:
- The triangle orbifolds O(2,3,m) have area < π/3 and systole ≥ σ* ≈ 0.562 (proved by a self-contained proof of the hyperbolic case of Jørgensen's inequality). A cone-of-radius-h_m argument then gives λ_j ≤ 1/4 + π²(j+1)²/h_m². A pigeonhole argument shows that no N, δ depending only on (A, ε) can work (Prop. 8.2, 8.3, Remark 8.4).
- A pinching family O_{k,b} of spheres with four cone points of order k ∈ {3,4} has λ_1 → 0 and limsup λ_j ≤ 1/4 (Prop. 8.5). Problem 1, whether a systole bound is needed, is left open.

## Significance

Within my remit, the geometric content is elementary but careful, self-contained and correct. The O(2,3,m) counterexample is a clean, explicit way to show that the bound on the orders cannot be dropped. Elliptic degeneration itself is classical (Selberg, Hejhal, Garbin–Jorgenson), and the authors say so; their contribution is the explicit, quantitative form of Proposition 8.3. The diameter bound is honest, but it is far from the true order: linear in 1/ε and cubic in M, against the expected logarithmic behaviour. It is also the dominant source of the astronomically large constants (Section 7 and Table 6 show that "most of that difference is the instance's diameter bound"). The geometry is therefore where the effective theorem is weakest. The paper is upfront about this. Within Sections 4 and 8 I found no mathematical error.

## Correctness and what was recomputed

All computations were done in `scratch/` with mpmath (40 digits), numpy and scikit-fem, independently of the authors' code, which I did not consult.

1. **Lemma 4.1 (H1)–(H3), checked by hand.** Rotation displacement sinh(d/2) = sinh r |sin(φ/2)|; hyperbolic displacement sinh(d/2) = sinh(ℓ/2) cosh r; the angle/ultraparallel criterion X = sin α sin β cosh d − cos α cos β. I also checked the hyperboloid normals n1, n3, the identity ⟨n1, n3⟩ = −X, and the side argument for where the lines meet. Correct. (See m1 for one imprecision in (H2).)

2. **Lemma 4.2, checked by hand.**
   - The identity cosh d − 1 = (cos θ + cos(α+β))/(sin α sin β) holds.
   - The integer-numerator defect bound π/(abc) holds.
   - cos((θ−α−β)/2) ≥ sin(π/2M) ≥ 1/M holds, because |θ−α−β| ≤ π − π/M.
   - Together these give cosh d − 1 ≥ 2/(π²M²). In the hyperbolic case, X ≤ cosh d gives ε ≤ 2d.
   - The rendered statement (p. 9) is d0 = min{ε/2, arccosh(1 + 2/(π²M²))}, consistent with the proof.
   - **Numerical check:** arccosh(1+x) ≥ √(2x/(1+x)) ≥ 0.6/M for x = 2/(π²M²), all 2 ≤ M ≤ 1999.

3. **Lemma 4.3 and Theorem 4.4, checked by hand.** Both the injectivity-radius argument and the packing argument are correct. I also checked the closed form: v0 ≥ πr0²/max(M, M²/4), using cosh ρ1 − 1 ≥ (cosh r0 − 1) sin²(π/M) and sin(π/M) ≥ 2/M. This gives D ≤ (A/π) max(4M, M²) max(4/ε, 10M/3).

4. **Table 2, all twelve entries recomputed from D = 4r0A/v0.** All agree: 56.60, 1125.4, 6.368e5; 150.94, 3001.2, 1.698e6; 639.97, 3184.1, 1.698e6; 1132.0, 22509, 1.274e7. The asymptotic D ≈ 4AM³/π² (large M) also matches.

5. **Lemma 2.2, checked by hand (the geometric input from the companion paper).**
   - **Count.** Translates of a Dirichlet domain lie in B(x0, x + 3 diam), which gives n_O(x) ≤ π e^{x+3diam}/Area.
   - **First bound B.** I checked it by Stieltjes integration, using ∫_ℓ^∞ x e^{x/2 − x²/4t} dx ≤ 2tℓ e^{φ(ℓ)}/(ℓ − t). This produces exactly the factor ℓ e^{ℓ/2}(1 + 2t/(ℓ−t)).
   - **Monotonicity.** B decreases in ℓ for t ≤ ℓ²/(2+ℓ), which contains the stated range.
   - **"For every t" bound.** Correct, including the maxima at x = 2√t and x = 6t and the constant 2√π e^{17t/4 − 1/2 − ℓ}.

6. **Theorem 6.2, geometric part, checked by hand.** The constant 63 = 21 · 3 is correct. The reduction of B*(t) ≤ Γ(t)/8 to e^{−y} y^p ≤ (γ*/16ϖe^{3D})(ε²/4)^p, with p = k* − 3/2, is correct, and so is the sufficient condition y ≥ y0 obtained via max e^{−y/2} y^p = (2p/e)^p. The rendered y0 (p. 11) has p log(4/ε²), as it should.

7. **Table 3, all eight rows recomputed in full from the stated formulas.** I computed α_k from Bernoulli polynomials, φ_k(m) by Taylor expansion of Φ_m, b_K(M), a_l, t1, t2, t3, Γ*, Λ, N and δ. Every printed value is reproduced to the printed precision. Examples:
   - row 2: D = 1125, t1 = 6.85e−9, t3 = 1.28e−4, Γ* = 4.23e−22, N = 6.82e9, δ = 4.17e−25;
   - row 8: Γ* = 1.77e−272, N = 3.75e30, δ = 8.65e−278.

   The binding constraints are as stated, and t2 ≥ 0.00455 never binds.

8. **Prop. 8.2.**
   - **σ\*.** σ* = 2 arsinh((2√(1 + ¾cosh²(2s∞)))⁻¹) = 0.562066871…, matching "0.56206…" and the "0.5620" of Theorem 1.3.
   - **Triangle lengths.** I checked cosh d(v2,v3) = 2cos(π/m)/√3 and cosh d(v2,v_m) = 1/(2 sin(π/m)) against the second cosine rule.
   - **Trace identity.** For β = hkh⁻¹ the off-diagonal entries are ±sin(φ/2) cosh r. I verified this symbolically.
   - **Lemma 8.1.** I checked the recursion x_{n+1} = −x_n(1+x_n)(u−u⁻¹)², the zero-avoidance argument and the conjugation C_n → A. Correct.
   - **Systole argument.** The covering argument for the axis, the convexity bound d(x, v3) ≤ 2s_m and the conclusion L ≥ σ* are correct.
   - **Cone ball.** The cone-ball argument (the star-shaped P built from 2m tiles) is correct.

9. **Prop. 8.3 and (3), checked by hand.**
   - For f = w^{−1/2}u, f'²w = u'² + qu² + (d/dρ)(−w'u²/2w), with q = 1/2 − w'²/4w². This gives q = 1/4 − 1/(4 sinh²ρ) and q = 1/4 + 1/(4 cosh²ρ). Correct.
   - The Rayleigh bounds and the pigeonhole count K = (⌊Λ_N/δ⌋ + 1)^{N−1} are correct. So is Remark 8.4, including the finiteness argument for A < π/3.

10. **Prop. 8.5.**
    - The Lambert relation sinh a sinh b = cos(π/k) and the collar inclusion are correct.
    - **Collar integral.** ∫_{−a}^{a} ρ² cosh ρ dρ = 2((a²+2) sinh a − 2a cosh a), checked numerically. This gives the stated λ_1 bound.
    - **λ_j bound.** The bound 1/4 + 1/(4cosh²(a/2)) + 4π²(j+1)²/a² is correct.

11. **Systoles, independent enumeration.** I enumerated reflection-group tiles in the hyperboloid model, keeping orientation-preserving elements with d(x0, γx0) ≤ L + 2r and BFS radius L + 3r, with L = 3. Results:
    - O(2,8,8): 2.2567679 (next 2.8816);
    - O(3,3,12): 1.8626041 (next 2.9807);
    - O_ϑ, ϑ = 0, 0.4, …, 2.8: 2.6339158, 2.2026953, 1.8313027, 1.5157379, 1.2504285, 1.0291288, 0.8455936, 0.6939946, equal to 4b in every case;
    - O(2,3,7): 0.98398656, which equals 2 arccosh((1 + 2cos(2π/7))/2);
    - O(2,3,100): 1.9213132.

    All agree with Table 4 and p. 20. The rounding-down margins are ≥ 5.5 × 10⁻⁸, as claimed. All are ≥ σ*.

12. **Diameters.** I recomputed the vertex diameters of the eight quadrilaterals (all angles exactly 60°). 2 diam P = 4.5849, 4.6712, 4.9216, 5.3140, 5.8202, 6.4129, 7.0688, 7.7697, all as in Table 4. For the triangles, diam = arccosh(cot²(π/8)) = 2.448 and 2.158, as in Table 4. The bound diam O ≤ 2 diam P is correct.

13. **Eigenvalue spot check (not proof, about 4 digits).** I used P2 finite elements on the hyperbolic triangles in the disc, with the curved side mapped radially, at three refinements. Results:
    - λ_1(O(2,3,7)) → 44.888, matching "44.89" (p. 21).
    - O(2,8,8): Neumann 3.8382, 8.2479, 18.655; Dirichlet 40.115, 73.662, 97.875.
    - O(3,3,12): Neumann 3.4969 (converging slowly upward), 11.558, 14.938; Dirichlet 37.821, 72.361, 97.994.

    All are consistent with Table 5.

14. **Fig. 1 claim.** d_3 = 25/12 for (0;2,8,8) against (0;3,3,12): equal R = 3/4, equal P_1 = 18, and a_1(P_3 difference) = (1/360) × 750. Correct, and it agrees with the plotted starting value 2.1 × 10⁻³ at t = 10⁻³.

## MAJOR issues

Neither major issue is a mathematical error. Both concern how complete and how well positioned the geometric part is.

**M1 (Section 8.2, pp. 22–23, Problem 1 and the paragraph after it): the "missing input" is largely available in the literature, and the paper does not engage with it.**
- The authors say a negative answer to (b) would follow from a lower bound λ_j ≥ 1/4 − o(1), 2 ≤ j < N, along the two pinching families. They say this "might come from finite manifold covers … together with the spectral theory of degenerating hyperbolic surfaces; we have not carried this out."
- For surfaces, convergence of the spectrum below 1/4 under pinching, including the counting functions, is a theorem: Ji [10], Wolpert [11, 12], Hejhal [9], and Huntley–Jorgenson–Lundelius (arXiv:math/9412221) for weighted counting functions at every T < 1/4. Garbin–Jorgenson [6] prove the analogue under elliptic degeneration.
- There is also a second, possibly shorter, route. Otal–Rosas (Duke 2009) and Ballmann–Matthiesen–Mondal (arXiv:1506.06541) bound the number of eigenvalues ≤ 1/4 by −χ. If that nodal-domain argument extends to cone metrics with angles 2π/k on the four-punctured sphere (−χ = 2), it would give λ_2(O_{k,b}) > 1/4 for all b. Together with the authors' own limsup λ_j ≤ 1/4, both families would then have first-N spectra tending to (0, 0, 1/4, …, 1/4). That would settle (b) negatively for A = 2π, M = 4. I have not verified that the extension goes through, and I make no claim that it does. But the paper should discuss this route.
- The authors should either:
  - (i) settle (b), via an equivariant version of Ji / Huntley–Jorgenson–Lundelius on a fixed torsion-free normal cover (for example the kernel of (0;k,k,k,k) → Z/k with x1, x2 ↦ 1, x3, x4 ↦ −1), plus a statement about the spectrum below 1/4 of the cusped limits (0;k,k,∞); or
  - (ii) state precisely which ingredient is not available for orbifolds, and cite the surface results. At present the reader is left with the impression that the analytic input is unknown, which I believe overstates the case.
- As written, Problem 1(b) is presented as open without adequate literature context. This is a gap in exposition and scholarship, not an error.

**M2 (Section 4, p. 10, paragraph after Theorem 4.4): the diameter bound is the bottleneck, and the stated heuristic for the true order is imprecise.**
- Theorem 4.4 is correct, but D grows like A/ε and like AM³. Table 6 shows this is what makes Theorem 6.2's N astronomically large. A thick–thin argument with the orbifold collar lemma (Dryden–Parlier, *Collars and partitions of hyperbolic cone-surfaces*, Geom. Dedicata 127 (2007); Buser [15, Ch. 4]) is standard and would give a much better bound. Neither paper is cited.
- The heuristic "a diameter bound of order A + n log(1/ε) + log M" is not right as stated:
  - The ε-term comes from the collars of the short geodesics. There are at most 3g − 3 + n of them, not n, and n log(1/ε) gives no ε-dependence for surfaces (n = 0). Since n + 4g ≤ A/π + 4, the natural form is C·A·(1 + log(1/ε)) + O(log M).
  - The log M term comes from the cusp-like ends of depth ≈ h_M around high-order cone points (Prop. 8.2 shows that this is sharp).
- Please correct the heuristic and cite the orbifold collar lemma. Ideally, carry out at least the ε-part, which is routine and would replace the 1/ε rate by log(1/ε) in t3.
- The same applies to the remark that a Buser-type count [15, Lemma 6.6.4] "might remove the diameter". For orbifolds, passing to a torsion-free cover multiplies the genus by an index that depends on the orders. The authors should say that this is why the count does not transfer directly.
- This is a request concerning the strength of the effective result, not an error. If the authors decline, the corrected heuristic and the citations suffice.

## MINOR issues

- **m1 (p. 8, Lemma 4.1 (H2); used on p. 9, Lemma 4.2).** For asymptotic lines, (H2) says only that the product "has no fixed point in H²". Lemma 4.2 needs it to be parabolic, to conclude X ≠ 1 from "Γ has no parabolic element". An element without fixed points could a priori be hyperbolic. Fix: state that the product is parabolic. In the upper half-plane with the common ideal point at ∞, the reflections are x ↦ 2c_i − x̄ and the product is a translation. This is a gap in exposition, not an error.
- **m2 (p. 9, Lemma 4.2).** The M-dependence of d0 (≈ 0.6/M) is an artefact of the bound sin α sin β ≤ π²/(ab). I expect the separation of distinct elliptic fixed points in a Fuchsian group to be bounded below independently of the orders. The extremal case should be the order-2 and order-3 points of (2,3,7), at distance arccosh(2cos(π/7)/√3) ≈ 0.2831 (I computed this value; I have not proved that it is the minimum). This would follow from Knapp's classification of discrete groups generated by two elliptics, or from the elliptic-element estimates in Beardon [24, Ch. 11]. If the authors can use such a bound, it removes one factor of M from D. If not, a remark that d0's M-dependence is not intrinsic would help.
- **m3 (p. 10, after Theorem 4.4).** "The bound grows like A/ε" holds only in the regime ε/2 < arccosh(1 + 2/(π²M²)) ≈ 0.45/M, where the ε-term of d0 binds. For M = 12 and all the examples, D does not depend on ε at all (Table 4: 1125.4 and 3001.2 for every ℓ). State the regime.
- **m4 (p. 20, after Prop. 8.2).** The phrase "a search over all words of length at most 24 … finds no closed geodesic shorter than 0.98399" is weaker than what is true. With the distance criterion of Section 7.1, the enumeration is complete, and the systole of O(2,3,7) is exactly 2 arccosh((1+2cos(2π/7))/2) = 0.983986…, which I confirmed. Give the closed form. Also say whether the m = 100 value 1.92131 is the systole: it is, by my complete enumeration.
- **m5 (p. 20).** The script path `theory/eigen/systole_233.py` appears in the body of a mathematical argument. Repository paths belong in the Data and code availability statement only.
- **m6 (pp. 4, 21; Garbin–Jorgenson).** The text says the number of eigenvalues below a fixed level above 1/4 "grows like the logarithm of the orders [6, Cor. 5.5, Thm 5.3], [7, Thm 6.5]". I could confirm the convergence of counting functions below 1/4 from the abstract of [6]. I could not confirm the log-growth statement at the cited numbers. Please quote it. If it is exact, note that Prop. 8.3's count (j ≲ h_m√c/π ~ (√c/π) log m) is consistent with it.
- **m7 (p. 21, Section 8.2).** Two points about the pinching family:
  - The family O_ϑ of Section 7 (quadrilaterals with angles π/3 and sinh a sinh b = 1/2) is exactly O_{3,b} of Section 8.2, with ϑ = log(sinh a / sinh b). The paper never says so. The cross-reference matters: Table 6 and Fig. 2 then show the test along the very pinching family that Problem 1 is about.
  - The restriction k ∈ {3,4} is unnecessary: any k ≥ 3 gives a hyperbolic (0;k,k,k,k).
- **m8 (p. 2, Section 1, compactness argument).** "Nearby orbifolds are related by quasi-isometries with constants near 1" needs those maps to be orbifold maps, sending cone points to cone points of the same order, for the min–max comparison to apply to orbifold eigenfunctions. Add one sentence. The same applies to the continuity claim on p. 22.
- **m9 (p. 21, Prop. 8.5).** The λ_1 bound discards the region outside the collar in ∫f². That is legitimate, but say so, since the bound is otherwise puzzling at first reading. Also, "the other two sides are at distance at least a from β" is in fact "exactly a". The inclusion of the collar needs only that the sides are not crossed by ρ-lines of length < a, so say that.
- **m10 (p. 10, Lemma 5.1(i), second statement).** The case analysis is unnecessary. s = 2g − 2 + Σ(1 − 1/m_i) ≥ 2g − 2 + n/2 gives n + 4g ≤ Area/π + 4 at once. This is cosmetic.

## Presentation

- **P1 (notation overload, throughout Sections 4–8).**
  - Γ denotes the Fuchsian group and also the gap function Γ(t) and Γ*; γ denotes group elements and also γ*.
  - λ denotes a line in (H3) and Lemma 4.2, and also the eigenvalues.
  - β denotes an angle (Lemma 4.2), a rotation (Prop. 8.2), a line (Section 8.2) and the constant max Σ b0 (Theorem 7.1).
  - a, b denote cone orders (Lemma 4.2), distances (Sections 7.1, 8.2) and matrix entries (Lemma 8.1).
  - ℓ denotes the systole and also the interval length in the proof of Prop. 8.3.
  - A denotes the area and also a matrix in Lemma 8.1.
  - K denotes the truncation order and also the pigeonhole count in Prop. 8.3.
  - σ* (systole constant) sits next to σ (signature).

  In Sections 4 and 8 a reader must reparse symbols constantly. Please rename the gap function (for example 𝒢(t)), the lines (for example L_0), and the Lemma 8.1 matrices.
- **P2 (Fig. 3, p. 22).** The six grey shades in both panels are hard to tell apart, and there is no key for j. Label the curves with j = 1, …, 6 at the right margin. In panel (a), say in the caption which dashed curve bounds which j. The rendered figure is otherwise clean, with no sign or label errors.
- **P3 (p. 9, proof of Lemma 4.2).** The phrase "(both senses do)" is cryptic. Say "the rotations by ±2π/a both lie in Γ_p̃".
- **P4 (pp. 19–20, proof of Prop. 8.2).** The proof is dense, packing three arguments into one paragraph. Separate them with labelled steps (area/diameter, cone ball, systole), as the italics partly do. Say explicitly that the folding f is the quotient map to T = H²/Γ*.
- **P5 (pp. 8–9).** A small figure for (H3) and Lemma 4.2 would help: the segment [p, q], the lines L1, L3, and the vertex w or the common perpendicular.
- Fig. 1 (p. 13) and Fig. 2 (p. 19) render correctly. I found no typographical or sign errors in Sections 4 and 8 on the rendered pages.

## Recommendation

**Minor revision** (from the standpoint of Sections 4 and 8 and the geometric inputs).

The geometry is correct. I recomputed every constant in Tables 2 and 3 and every systole and diameter in Table 4 independently, and found no discrepancy. The arguments of Sections 4 and 8 check line by line. The required changes are:
- the literature context for Problem 1 (M1);
- correcting the diameter heuristic and citing the orbifold collar lemma (M2);
- small precision fixes (m1–m10);
- the notation cleanup (P1).

If the authors choose to strengthen the diameter bound or to settle Problem 1(b), the paper would be markedly stronger, but I do not make that a condition.

Confidence: high for Sections 4 and 8 and the geometric inputs to Section 6 and Table 4; I have not assessed the heat-invariant algebra of Sections 2–3 beyond what Table 3 and Fig. 1 exercise.

## What resolves each issue

- **M1:** Add a paragraph citing Ji, Wolpert, Hejhal, Huntley–Jorgenson–Lundelius, Garbin–Jorgenson, Otal–Rosas and Ballmann–Matthiesen–Mondal. Then either prove (b) negatively, via an equivariant degeneration result on a fixed torsion-free cover or an orbifold Otal–Rosas bound λ_2(O_{k,b}) > 1/4, or state exactly which orbifold/equivariant ingredient is missing.
- **M2:** Replace "A + n log(1/ε) + log M" by a correct heuristic, for example C·A·(1 + log(1/ε)) + O(log M), justified by the at most 3g − 3 + n collars. Cite Dryden–Parlier and Buser. Optionally carry out the thick–thin bound. Explain why Buser's count does not transfer directly to orbifolds.
- **m1:** State "parabolic" in (H2), with the one-line half-plane proof.
- **m2:** Use a uniform separation bound for elliptic points (Knapp / Beardon Ch. 11), or remark that d0's M-dependence is an artefact.
- **m3:** State the regime in which D ∝ 1/ε.
- **m4:** Give the closed-form systole of O(2,3,7) and say that the enumeration is complete (distance criterion).
- **m5:** Move the script path to the Data and code availability statement.
- **m6:** Quote the Garbin–Jorgenson log-growth statement precisely.
- **m7:** Identify O_ϑ with O_{3,b}, and drop or justify k ∈ {3,4}.
- **m8:** Specify orbifold (cone-point-preserving) bi-Lipschitz maps.
- **m9:** Note the discarded term and "exactly a".
- **m10:** Optionally give the one-line proof.
- **P1–P5:** Rename the overloaded symbols, add a key to Fig. 3, add a sketch for (H3), and split the proof of Prop. 8.2 into labelled steps.

Literature consulted:
- [Huntley–Jorgenson–Lundelius, arXiv:math/9412221](https://arxiv.org/abs/math/9412221)
- [Garbin–Jorgenson, arXiv:1603.01494](https://arxiv.org/abs/1603.01494)
- [Ballmann–Matthiesen–Mondal, arXiv:1506.06541](https://arxiv.org/pdf/1506.06541)
- [Otal–Rosas, arXiv:0905.0506](https://ar5iv.arxiv.org/html/0905.0506)
- [Ji, JDG 38 (1993), bibliographic record only](https://projecteuclid.org/journals/journal-of-differential-geometry/volume-38/issue-2/Spectral-degeneration-of-hyperbolic-Riemann-surfaces/10.4310/jdg/1214454296.full)
