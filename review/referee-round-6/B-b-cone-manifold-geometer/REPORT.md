<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (Annals of Global Analysis and Geometry)

Writing REPORT.md was refused, so the complete report is below. Referee B-b: geometry of hyperbolic cone-manifolds. My assigned coverage is Section 4, Section 8, and every geometric input used in Sections 5–6. I read the rest of the paper closely enough to judge how these parts are used.

## Summary

The paper takes a closed orientable hyperbolic 2-orbifold O with area at most A, systole at least ε and cone orders at most M. It proves that the first N eigenvalues, each known to within δ, determine the signature of O, with N and δ given by explicit formulas (Theorem 1.1 / Theorem 6.2). The mechanism runs through the heat trace. The signature term G_σ(t) is separated from its competitors at a small time t, using an integrality statement for the first differing heat invariant (Lemma 3.3). The closed-geodesic term is controlled through a count of closed geodesics in terms of the diameter (Lemma 2.2). That count needs a diameter bound depending only on A, ε and M (Theorem 4.4, Section 4).

The paper also does the following:

- It gives an a-posteriori test (Theorem 7.1) and runs it on computed spectra.
- It shows that the order bound cannot be dropped (Theorem 1.3, Section 8.1). The triangle orbifolds O(2,3,m) have systole at least σ* = 0.56206, proved with a Jørgensen-inequality argument, and they carry many eigenvalues below any level above 1/4, by test functions placed in the embedded cone of radius h_m around the order-m point. A pigeonhole argument then gives the counterexample.
- It discusses whether the systole bound is needed (Section 8.2, Problem 1).

Within my coverage the mathematics is correct. I checked every proof line by line, and every constant I recomputed agreed with the paper. My main objection is structural and concerns the geometric input. The diameter, and with it all of Section 4, is not needed. The factor e^{3·diam} that the diameter brings into the closed-geodesic count is avoidable with the paper's own Lemmas 4.2–4.3. That factor, not the spectral side, drives the poor class-level results that the abstract reports.

## Significance

**What is good:**

- The effective statement is clean. The proofs in Section 4 and Section 8 are short and self-contained, and they are correct.
- The authors are scrupulously honest about what is proved and what is only observed: floating-point systoles, eigenvalue errors that are estimates rather than enclosures, and completeness that is supported but not proved.
- The counterexample O(2,3,m) is a nice explicit use of elliptic degeneration. The Jørgensen-type systole bound uniform in m is elegant.
- Proposition 8.5 makes the pinching discussion precise.

**On the geometric side the novelty is modest:**

- Lemma 4.2 (separation of elliptic points via the triangle pqw), Lemma 4.3 (ball areas) and Theorem 4.4 (a packing bound on the diameter) are standard arguments.
- Lemma 8.1 is Jørgensen's inequality, re-proved.
- Proposition 8.3 is a standard test-function bound in a cone.
- The qualitative phenomenon behind Theorem 1.3 is in Garbin–Jorgenson [14,15], as the authors acknowledge.

The paper's contribution is the effective packaging. Its value depends on how good the effective constants are. Here the geometric input is the weakest link: D(A,ε,M) grows like A·M³ and like A/ε, it enters through e^{3D}, and D is in fact unnecessary (M1). Whether AGAG wants this paper depends largely on whether that is repaired.

## Correctness and what was recomputed

All scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/B-b-cone-manifold-geometer/scratch/`: `consts.py`, `check2.py`, `systole.py`, `sys233.py` and `diam.py`. I used mpmath at 80 digits for the constants and float64 for the tile enumeration.

**Proofs checked line by line (all correct):**

- **Lemma 2.2 (p. 6).** I re-derived independently all three statements, including the two the paper imports from [28]:
  - **The count n_O(x) ≤ π e^{x+3 diam}/Area.** Take a Dirichlet domain at a point with trivial stabiliser. Each conjugacy class has a representative with d(x0,γx0) ≤ x + 2 diam, and the translates are disjoint inside B(x0, x + 3 diam).
  - **The bound B(ℓ, diam, t).** For t ≤ ℓ²/(2(1+ℓ)) the function x e^{-x/2-x²/4t} is decreasing on [ℓ,∞), and integration by parts gives exactly the factor (1 + 2t/(ℓ−t)). I also checked the monotonicity of B in ℓ.
  - **The all-t bound.** The two maxima at x = 2√t and x = 6t are correct, and so is the Stieltjes integration.
- **Lemma 4.1 (H1)–(H3) (pp. 8–9).** I checked the disc computation, the half-plane computation and the hyperboloid normals (−e2, n1, n3). The identities ⟨n1,n3⟩ = −X and X > −1 for d > 0 are correct.
- **Lemma 4.2 (p. 10).** Correct:
  - γ = s1 s3 lies in Γ.
  - In the case X > 1, ε ≤ 2h ≤ 2d.
  - In the case X < 1, θ = πk/c, the defect is ≥ π/(abc), cos((θ+α+β)/2) ≥ 1/(abc) and cos((θ−α−β)/2) ≥ 1/M. These give cosh d − 1 ≥ 2/(π²cM) ≥ 2/(π²M²).
- **Lemma 4.3 and Theorem 4.4 (p. 10).** Both cases of the ball-area argument are correct, including the bounds ρ1 ≤ r0 and 2ρ1 ≤ ε. The chain cosh ρ1 − 1 ≥ (cosh r0 − 1)·sin²(π/M) holds. I checked numerically that arccosh(1+x) ≥ √(2x/(1+x)) for x ∈ [10⁻⁸, 10³]. The step d0 ≥ 0.6/M holds for M ≥ 2. The closed form max(4M, M²)·max(4/ε, 10M/3) is a valid upper bound; it exceeds the exact value 4r0A/v0 by up to a factor 2.6.
- **Lemma 5.1, Proposition 5.2, Lemma 6.1 and Theorem 6.2 (pp. 11–13).** The geometric inputs are correct: Area ≥ π/21, n + 4g ≤ A/π + 4, b0(m) = (m²−1)/(12m), and the replacement of B by B* using Area ≥ π/21 and 1 + 2t/(ε−t) ≤ 3 on (0, t2]. B* is monotone on (0, t2], and the derivation of y0 and t3 is correct (I re-derived y0 = 2(3D + log(16ϖ/γ*) + p log(4/ε²) + p log(2p/e)). I also checked that Λt* ≥ 1 and the 3/8 margin. These checks are conditional on the companion-paper results listed in Table 1, which are outside my remit.
- **Theorem 7.1 (p. 15).** The tail, perturbation and hyperbolic terms are correct, and (C2) implies (C1).
- **Lemma 8.1 (pp. 20–21).** I checked the recursion for B_{n+1} and x_{n+1} by hand. The exclusion of x_n = 0, the conjugation C_n = A^{−k_n} B_n A^{k_n} and the convergence C_n → A are correct.
- **Trace identities (p. 21).** I verified tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r numerically. I also verified that h moves i by distance r perpendicular to the axis.
- **Proposition 8.2 (pp. 21–22):**
  - The area formula, cosh d(v2,v3) = 2cos(π/m)/√3 and cosh d(v2,vm) = 1/(2 sin(π/m)) are correct.
  - The embedded cone ball B(vm, h_m) is correct; P is a union of 2m tiles and is a fundamental domain for Stab(vm).
  - The bound d(x, v3) ≤ 2s_m (convexity on [v2,v3]) and the application of Lemma 8.1 are correct.
- **Identity (3) and Proposition 8.3 (p. 22).** I checked q = 1/2 − w'²/(4w²) for w = sinh and w = cosh. Including the boundary term, the Rayleigh quotient is ≤ 1/4 + π²/ℓ². The pigeonhole count K = (⌊Λ_N/δ⌋+1)^{N−1} is correct.
- **Remark 8.4 (pp. 22–23).** The orders 7..M give K+1 orbifolds. The case analysis for A < π/3 is correct.
- **Proposition 8.5 (p. 23).** The Fermi-coordinate collar is correct, with the common perpendicular of β and the a-side having length a. I recomputed ∫_{−a}^{a} ρ² cosh ρ dρ = 2((a²+2) sinh a − 2a cosh a), which gives exactly the stated λ1 bound. The λ_j bound with q ≤ 1/4 + 1/(4cosh²(a/2)) is correct.

**Constants recomputed (all agree with the paper):**

- **Table 2 (p. 11), all 12 entries.** 56.602 / 1125.4 / 6.3683e5; 150.94 / 3001.2 / 1.6982e6; 639.97 / 3184.1 / 1.6982e6; 1132.0 / 22509 / 1.2737e7. The growth claims "AM³", "A/ε" and "ε < 0.42 for A = 4π/3, M = 3" also agree.
- **Table 3 (p. 13), all 8 rows and every column.** I recomputed k*, D, t1, t3, Γ*, Λ, N, δ and the binding constraint. t2 = 0.00455 is its smallest value. t3 binds in rows 4, 6 and 7, as the paper says on p. 10.
- **Statements on pp. 13–14.** With k* = n* instead of min(n*, M), I get N = 4.19 × 10¹⁸ at A = 10π, M = 3, against 1.1 × 10⁷ with the minimum. The growth factor of N per halving of ε (A = 4π/3, M = 3) is 9.03, 8.94, 8.86, 8.79, 8.73, 8.67, as stated.
- **Table 6, last column (p. 19).** 4.3e4, 4.3e4, 4.5e4, 6.8e4, 1.0e5, 1.6e5, 2.4e5, 3.7e5 at M = 3; 7.4e12 at M = 12; 6.8e9 for both triangle orbifolds.
- **Table 4 (p. 16), class-level D.** 1125.44, 150.937 and 3001.18 agree.
- **Systoles of all ten examples.** I computed these by my own complete tile enumeration (tiles within distance L + r_v of a vertex):
  - O(2,8,8): 2.2567679, which equals 2 arccosh(1 + cos(π/4)).
  - O(3,3,12): 1.8626041, which equals 2 arccosh(1/2 + cos(π/12)).
  - All eight O_ϑ: exactly 4b, with sinh b = e^{−ϑ/2}/√2.
  - All agree with Table 4 after rounding down.
- **Diameters.** diam P agrees with Table 4 for all ten examples (2.448, 2.158, 2.292, …, 3.885). By sampling I found that diam O = diam P for O(2,8,8), O(3,3,12) and ϑ = 0, 1.6, 2.8.
- **Constants of Section 8:**
  - σ* = 0.5620669 agrees.
  - Systole of O(2,3,7) = 0.9839866 = 2 arccosh((1+2cos(2π/7))/2) agrees.
  - Systoles of O(2,3,m) for m = 8, 9, 12, 20, 50, 100: 1.26595, 1.42834, 1.66289, 1.83459, 1.91067, 1.92131. They increase in m and stay below 2 arccosh(3/2) = 1.92485, as stated on p. 22.
  - h_m and log(m/2π) agree. The plotted λ1 values (44.89 at m = 7, 0.473 at m = 4096) lie below the Proposition 8.3 bounds (133 and 1.017).
- **Heat-invariant spot checks.** α0..α3, a0 = 1/12, a1 = 1/360, d2 = −1/12 for (0;4,4,4) against (0;3,4,6), and d3 = 25/12 for (0;2,8,8) against (0;3,3,12) all agree.

## FATAL

None in my coverage. Theorem 1.1 / 6.2 (conditional on the companion-paper inputs in Table 1), Theorem 1.2 / 7.1 as a conditional statement, and Theorem 1.3 / Propositions 8.2–8.3 are correct.

## MAJOR

**M1 (Lemma 2.2 p. 6; Section 4 pp. 8–11; Theorem 6.2 pp. 12–13; Table 6 and Section 7.2 pp. 18–19; abstract; p. 5). The diameter is unnecessary, and the e^{3·diam} count it feeds is the dominant artefact in the paper's effective results.**

The diameter enters only through n_O(x) ≤ π e^{x+3 diam}/Area (p. 10, lines after Theorem 4.4). The paper says (p. 5, p. 11) that a Buser-type count "does not transfer directly" to orbifolds because a torsion-free cover multiplies the genus. No cover is needed. The paper's own Lemmas 4.2–4.3 give a count of the form C(A,ε,M)·e^x with C polynomial in A, M and 1/ε:

1. Let Y be a maximal 4r0-separated set in O. The balls B(y, 2r0) are disjoint, so by Lemma 4.3 |Y| ≤ A/v0.
2. Replace each y that lies within r0 of a cone point by that cone point. Every point of O is then within 5r0 of some base point b.
3. Each closed geodesic of length ≤ x has a conjugate with d(b̃, γb̃) ≤ x + 10r0 for some base point b.
4. Orbit points of distinct cosets of Γ_b̃ are at least 2r0 apart if b is a cone point (Lemma 4.2), and at least 2ρ1 apart otherwise (proof of Lemma 4.3). Also |Γ_b̃| ≤ M.
5. Hence n_O(x) ≤ (A/v0) · M e^{x+11r0} / (2(cosh ρ1 − 1)). This involves no diameter.

**Consequences:**

- In Theorem 6.2 the term 6D in y0, which comes from 3D, becomes 2 log C. So t3 changes from about ε²/(24D) to about ε²/(4(log C + log(1/Γ*) + …)). In rows 4, 6 and 7 of Table 3 (where t3 binds, D = 151–1132), t3 and hence N improve by roughly one to two orders of magnitude.
- For the class-level column of Table 6, the factor e^{3D} with D = 1125 (e^{3376}) is replaced by a constant of order 10⁸ (my rough evaluation for the triangle class, A = π/2, M = 12). The instance-level factor is e^{3Δ} ≈ 2.4 × 10⁶. Because H enters the test through e^{−ℓ²/4t}, the usable time shrinks only logarithmically. The class-level test would then very likely succeed on all ten examples, with counts comparable to the instance-level ones.
- The following then rest on an avoidable artefact of Lemma 2.2, not on "knowledge of the geometry" (p. 19): the headline statement in the abstract ("decides four of ten … estimated to need 4.4 × 10³ to 4.1 × 10⁵ for the others"), the interpretation on p. 19 ("most of the gap … is knowledge of the geometry, through e^{3Δ}"), and the sentence "An orbifold whose diameter is known is in practice one whose geometry is known".

This is not an error in a proof. It is a substantive weakness in the only geometric input of the main theorem, in a paper whose stated point is effectivity ("Effectivity is the point", p. 4). It also makes the M³ and 1/ε rates discussed on pp. 10–11 and 14 moot.

## MINOR

**m1 (Lemma 4.2, p. 10).** The order-dependence d0 ~ 0.6/M is an artefact of allowing an arbitrary third vertex order c ≤ M. Jørgensen's inequality applied to two elliptic elements already gives an order-independent bound whenever one order a ≥ 7. I verified numerically that tr[A,B] − 2 = 4 sin²(π/a) sin²(π/b) sinh² d. This gives sinh² d ≥ (1 − 4 sin²(π/a)) / (4 sin²(π/a) sin²(π/b)), hence d ≥ 0.5453. That value is sharp: it is h_7, the distance between the order-2 and order-7 points of O(2,3,7). I expect the remaining cases (both orders ≤ 6) to follow by applying the same bound at the third vertex w of the triangle pqw when c ≥ 7. Even if M1 is not taken up, the authors should either sharpen the lemma or say explicitly that the 1/M is not intrinsic. The same applies to the factor 1/M in v0 (Lemma 4.3): a cone point of order m sits in an embedded cone of radius about log m, whose area is bounded below independently of m.

**m2 (p. 11, the paragraph after Theorem 4.4).** The thick–thin sketch ("should give a diameter bound of order A(1 + log 1/ε) + log M") is unproved. It also relies on Dryden–Parlier [34], which excludes cone angle π (order 2), while the classes C(A,ε,M) contain order-2 points. Either give a proof or label it plainly as an expectation. M1 makes it unnecessary.

**m3 (Section 7.1 p. 17; Table 4 p. 16; abstract).** The systoles are stated to be "computed in floating point, not certified", and this is listed among the caveats in the abstract. Certification is easy here. The systoles have closed forms:
- ℓ(O(2,8,8)) = 2 arccosh(1 + cos(π/4));
- ℓ(O(3,3,12)) = 2 arccosh(1/2 + cos(π/12));
- ℓ(O_ϑ) = 4b (I confirmed all ten values by an independent enumeration).

The enumeration involves only a few hundred to about 1350 tiles, so interval arithmetic, or exact traces, settles it. For O_ϑ, Proposition 8.5 already gives ℓ ≤ 4b, and only the reverse inequality needs a short argument. This would remove one caveat from Theorem 1.2's demonstration.

**m4 (Section 7.1 p. 17, (iii) p. 15).** The proved diameter bound 2 diam P is a factor 2 above the computed diameter, which equals diam P in all cases I sampled. Since the instance-level test carries e^{3Δ}, a proof that diam O = diam P for these doubles would cut that factor by e^{3 diam P} ≈ 10³. This does not arise if M1 is adopted.

**m5 (p. 4 and p. 21).** The phrase "their diameters growing like log m" is stated as fact. Only the lower bound diam ≥ h_m ≥ log(m/2π) is proved. Say "at least logarithmically".

**m6 (p. 24).** "Related by quasi-isometries with constants near 1": quasi-isometries with additive constants do not control eigenvalues. What is needed, and what Section 1 says, is bi-Lipschitz maps with constants near 1, sending cone points to cone points of the same order. Fix the wording.

**m7 (Proposition 8.2, pp. 21–22; Theorem 1.3).** σ* = 0.562 is far below the numerically observed infimum, ℓ(O(2,3,7)) = 0.98399, with ℓ increasing in m. The theorem is true as stated. But the remark on p. 22 could note that the Jørgensen argument loses mainly through the crude bound r ≤ 2s_∞ on the distance from the axis to an order-3 point.

**m8 (Proposition 8.5, p. 23).** The λ_j bound uses arches only in [a/2, a). Using both halves of the collar, which is symmetric under ρ ↦ −ρ, halves (j+1) in the bound at no cost.

**m9 (Lemma 2.2 p. 6; Theorem 7.1 p. 15).** The first bound is the one the theorem uses when s ≤ ℓ²/(2(1+ℓ)). State in the lemma that the systole entering it may be replaced by any lower bound ℓ. B is decreasing in ℓ only on the range t ≤ ℓ²/(2(1+ℓ)), and that range itself depends on ℓ. Theorem 6.2's proof handles this correctly; the statement of Theorem 7.1 should say it too.

## Presentation

**P1 (Lemma 4.1 (H2), proof, p. 9).** The asymptotic case is justified obscurely ("it is the centre of a rotation that is a product of reflections in lines through it"). The clean argument: if s2s1 z = z, then s1 z = s2 z; if this point were not z, both lines would be the perpendicular bisector of the segment from z to it. So z lies on both lines, which is impossible for asymptotic lines.

**P2 (notation overload).**
- σ* (a length, p. 21) clashes with σ (signatures).
- Γ denotes the group, the function Γ(t), the constant Γ* and the reflection group Γ* (p. 21).
- γ* (p. 12) is a constant.
- The diameter bound is called D in Section 6 and Δ in Theorems 1.2 and 7.1.

Rename these, for example ℓ_{2,3} for the length, W for the reflection group, and g(t) for the gap.

**P3 (Table 2 caption, p. 11).** "True diameters" should read "computed diameters", since diam O = diam P is not proved (see m4).

**P4 (Figure 3(a), p. 24).** The dashed bound for λ_j has numerator (j+1)², so it lies close to the curve of λ_{j+1}. Readers will pair each bound with the wrong eigenvalue. Use matching grey levels, or label the bounds.

**P5 (p. 10).** "The diameter enters only through Lemma 2.2": state this already at the start of Section 4, with a forward pointer to Lemma 2.2. Section 4 is otherwise unmotivated.

## Recommendation

**Major revision.** Confidence: high on correctness within my coverage; medium-high on the assessment of M1.

Everything I could check in Sections 4 and 8 and in the geometric inputs of Sections 5–6 is correct, and every number I recomputed agrees. I am not recommending acceptance because the paper's effective content, which it presents as its point, rests on a geometric input (Lemma 2.2 with Theorem 4.4) that is unnecessarily weak. The paper's own lemmas already contain the fix. The class-level conclusions in the abstract and in Section 7.2 are artefacts of that weakness.

## What resolves each issue

- **M1:** Replace the diameter-based count in Lemma 2.2 with the packing count sketched above, n_O(x) ≤ (A/v0) · M e^{x+11r0} / (2(cosh ρ1 − 1)), or any count polynomial in A, M and 1/ε. Then:
  - remove D from Theorem 6.2 and recompute Table 3;
  - rerun the class-level column of Table 6 with the new count;
  - revise the abstract, p. 5, pp. 10–11 and p. 19 accordingly.

  Alternatively, if the authors keep the diameter, they must show why the direct count fails for orbifolds and withdraw the interpretation "most of the gap is knowledge of the geometry".
- **m1:** Sharpen Lemma 4.2 (Jørgensen for elliptic pairs, plus the third-vertex argument), or add a sentence saying the 1/M is not intrinsic. Do the same for the 1/M in v0.
- **m2:** Prove the thick–thin diameter bound, including order-2 points, or label it as an expectation. M1 makes it unnecessary.
- **m3:** Certify the systoles with interval or exact arithmetic using the closed forms above, and remove the corresponding caveat from the abstract and from Table 4.
- **m4:** Prove diam O = diam P for these doubles, or keep 2 diam P and say it is a factor-2 bound.
- **m5, m6:** Change the wording as indicated.
- **m7:** Add a sentence on where σ* loses.
- **m8:** Use both halves of the collar.
- **m9:** Add the clarifying sentence to Lemma 2.2 and Theorem 7.1.
- **P1–P5:** Editorial changes as described.
