<!-- Saved verbatim by the main session from the reviewer's returned text: the harness refused the reviewer's own write. Scripts (check_geom.py, sep_scaling.py, tables.py, tables_nok.py, systole.py) and outputs are in its git-ignored scratch/. -->

# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Submitted to Annals of Global Analysis and Geometry. Referee B-b (hyperbolic geometry: thick–thin, discreteness, Jørgensen, degenerations).

## Summary

The manuscript proves an effective version of the Dryden–Strohmaier theorem that the Laplace spectrum of a closed hyperbolic 2-orbifold determines its signature. Fix an area bound A, a systole bound ε and a cone-order bound M. The first N eigenvalues, each known to within δ, then determine the signature, and N and δ are given by formulas (Theorems 1.1 and 6.2). The proof takes the first heat invariant at which two signatures differ (Section 3), turns it into a quantitative gap between the signature parts G_σ(t) of the heat trace (Lemma 6.1), and controls three things at an explicit small time: the closed-geodesic term, through a diameter bound (Theorem 4.4, via Lemma 2.2 and Lemma 2.3); the eigenvalue tail (Proposition 5.2); and the perturbation. There is also an a-posteriori certificate (Theorem 7.1), applied to computed spectra (Table 3).

The paper also shows that the order bound cannot be dropped (Theorem 1.3, Propositions 8.2–8.3, Remark 8.4). The orbifolds O(2,3,m) have uniformly bounded area and systole, yet carry arbitrarily many eigenvalues below 1/4 + η. The systole bound in O(2,3,m) comes from a self-contained proof of the hyperbolic case of Jørgensen's inequality (Lemma 8.1). Section 8.2 discusses pinching and leaves the need for the systole bound open (Problem 1).

My charge was the geometric part:
- Section 4 (Lemmas 4.1–4.3, Theorem 4.4, Table 1);
- the geometric inputs to Section 6 (Lemmas 2.2 and 2.3, and the constants built from D in Theorem 6.2);
- Lemma 8.1;
- the O(2,3,m) argument (Propositions 8.2, 8.3 and Remark 8.4);
- Proposition 8.5.

## Significance

Effective inverse spectral results for orbifolds are rare, so a formula for N and δ is a genuine if modest addition to Dryden–Strohmaier [1]. The numbers themselves are astronomically large (Table 2: N up to 3.8 × 10^30). The authors say this openly and offer the a-posteriori certificate as the practically useful form, which I find honest and sensible.

The most interesting geometric content is Section 8.1: a clean, elementary demonstration that, without an order bound, area and systole do not suffice. This is a degeneration through elliptic elements, a cone point turning into a cusp. The geometry is elementary throughout. The paper does not use the Margulis lemma, the collar lemma or any thick–thin decomposition, and that choice costs a good deal in the constants (M1).

The paper is suitable for AGAG in scope. It is a careful paper whose novelty lies in effectivity rather than new phenomena.

## Correctness and what was recomputed

**Overall verdict.** Every geometric statement in my charge is correct as stated. I found no mathematical error in Section 4, in Lemmas 2.2–2.3, in Lemma 8.1 or in Propositions 8.2, 8.3 and 8.5. Every constant I recomputed agrees with the paper. The details follow; the scripts and their outputs are in my scratch folder (`check_geom.py`, `sep_scaling.py`, `tables.py`, `tables_nok.py`, `systole.py`).

1. **Lemma 4.1 (H1), p. 9.**
   - Checked the proof algebra symbolically.
   - Checked the rotation formula sinh(d/2) = sinh r |sin(φ/2)| (disc model) and the translation formula sinh(d/2) = sinh(ℓ/2) cosh r (half-plane) numerically: 200 random configurations each, 40-digit mpmath, maximum error below 10^-38.
   - Checked the auxiliary fact |z|/Im z = cosh(dist to iR+).
2. **Lemma 4.1 (H3), pp. 9–10.**
   - Built the configuration in the hyperboloid exactly as in the proof, with p = (1,0,0), q = (cosh d, sinh d, 0) and the given n1, n3.
   - Checked that n1 and n3 are unit, tangent at p and q respectively, and orthogonal to the stated tangent directions of L1 and L3.
   - Checked that ⟨n1, n3⟩ = −X.
   - For X < 1, solved numerically for the intersection w and measured the angle at w: cos θ = X to 10^-38.
   - For X > 1, checked |⟨n1, n3⟩| = X.
   - The sign argument excluding the side x2 < 0 is right.
3. **Lemma 4.2, p. 10.**
   - Verified the identity cosh d − 1 = (cos θ + cos(α+β))/(sin α sin β) = 2 cos((θ+α+β)/2) cos((θ−α−β)/2)/(sin α sin β) symbolically. The difference simplifies to 0.
   - Checked each estimate: defect ≥ π/(abc); cos((θ+α+β)/2) ≥ 1/(abc); |θ−α−β| ≤ π − π/M, so cos((θ−α−β)/2) ≥ 1/M; sin α sin β ≤ π²/(ab). Together these give cosh d − 1 ≥ 2/(π² c M) ≥ 2/(π² M²).
   - The rendered page (p. 10) confirms the constant is arccosh(1 + 2/(π²M²)); the extracted text is ambiguous.
   - Brute force over every configuration the proof admits (orders a, b, c ≤ M ≤ 24, θ = πk/c, positive defect) found no violation.
   - In the ultraparallel case, cosh h = X ≤ cosh d is immediate.
   - The use of (H2) is correct: s1 s_λ and s_λ s3 are rotations by 2π/a and 2π/b, γ = s1 s3 ∈ Γ, X ≠ 1 because there are no parabolics, and the rotation by 2θ forces θ ∈ (π/c)Z.
4. **Lemma 4.3 and Theorem 4.4, p. 11.**
   - Checked both cases of Lemma 4.3. Case 1: a ball about a cone point within r0. Case 2: Γ_x̃ = 1; hyperbolic elements move x̃ by at least ε ≥ 4 r0 ≥ 2ρ1, and elliptic elements by at least 2ρ1 via (H1) and |sin(πj/k)| ≥ sin(π/M).
   - Checked the packing argument and the closed form:
     - (cosh ρ1 − 1) ≥ (cosh r0 − 1) sin²(π/M), using ρ1 ≤ r0;
     - v0 ≥ π r0²/max(M, M²/4);
     - 8 max(M, M²/4) = 2 max(4M, M²);
     - arccosh(1+x) ≥ √(2x/(1+x)), checked numerically on 10^-15 ≤ x ≤ 1;
     - M · arccosh(1 + 2/(π²M²)) ≥ 0.6339 for all M ≥ 2, so d0 ≥ min(ε/2, 0.6/M).
   - Recomputed Table 1 from the exact formula 4 r0 A/v0. All twelve entries agree: 56.6, 1125, 6.368e5; 150.9, 3001, 1.698e6; 640.0, 3184, 1.698e6; 1132, 2.251e4, 1.274e7.
   - The diameter claims in the Table 1 caption hold:
     - O(2,8,8): twice its longest side is 2 × 2.44845 = 4.897 < 4.9;
     - O(3,3,12): 2 × 2.15817 = 4.316 < 4.4.
5. **Lemma 2.2 and Lemma 2.3, pp. 4–5.**
   - Checked by hand: the Dirichlet-domain count; both integrations by parts; the bound ∫_ℓ^∞ x e^{x/2−x²/4t} dx ≤ (2tℓ/(ℓ−t)) e^{ℓ/2−ℓ²/4t} (via x/(x−t) decreasing); and the logarithmic derivative of B in ℓ, with the bracket ≥ 0 exactly when t ≤ ℓ²/(2(1+ℓ)).
   - Checked the second bound: the maxima are at x = 2√t and x = 6t, and 9t/2 − t/4 = 17t/4.
   - In Theorem 6.2, checked:
     - ϖ = 63 ε e^{ε/2}/((1−e^{−ε})√(4π)), using Area ≥ π/21 and 1 + 2t/(ε−t) ≤ 3 on t ≤ t2;
     - that B* increases on (0, t2];
     - the derivation of y0 (including the term p log(4/ε²), confirmed on the rendered p. 12);
     - Λ t* ≥ 1, the tail estimate, and the 3/8 bookkeeping.
6. **Table 2, p. 13.**
   - Reimplemented all of Theorem 6.2 at 60 digits: α_k from μ_j = 4(2j+1)! η(2j+2)/(2π)^{2j+2}; b_l(m), g_k and ϕ_k from (2); a_l; the least common multiple L_M; then t1, t2, t3, t*, Γ*, Λ, N and δ.
   - Sanity checks:
     - α0, …, α3 = 1, −1/3, 1/15, −4/315;
     - b0(m) = (m²−1)/(12m);
     - d2 = −1/12 for (0;4,4,4) against (0;3,4,6);
     - d2 = 0 and d3 = 25/12 for (0;2,8,8) against (0;3,3,12).
   - Every entry of all eight rows agrees, including the binding constraint. Example: row 1 gives D = 402.2, t1 = 1.14e−7, t3 = 3.54e−4, N = 3.4e8, δ = 3.07e−21, binding t1.
   - The claim on p. 13 that N would be about 4 × 10^18 at A = 10π, M = 3 without the reduction k* ≤ M also checks out: 4.19 × 10^18.
7. **Lemma 8.1 (Jørgensen, hyperbolic case), pp. 16–17.**
   - Checked symbolically: tr[A,B] − 2 = −bc(u − u^{−1})², the matrix B_{n+1}, and the recursion x_{n+1} = −x_n(1+x_n)(u−u^{−1})².
   - The case analysis is correct:
     - x_n never vanishes;
     - if exactly one of a_{n−1}, d_{n−1} vanishes, B_n and A share exactly one fixed point, giving a nontrivial unipotent commutator;
     - the repelling and attracting fixed points p_n, q_n behave as claimed.
   - The renormalisation C_n = A^{−k_n} B_n A^{k_n} is right: the fixed-point moduli are ≤ u²|p_n/q_n|^{1/2} and ≥ |q_n/p_n|^{1/2}, attracting and repelling ends match those of A, and C_n ≠ A. So C_n → A, contradicting discreteness. The proof is correct.
8. **Trace identity, p. 17.**
   - Checked symbolically, with β = h k h^{−1}: bc = −sin²(φ/2) cosh² r, and tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r.
   - Checked numerically that h moves i along the unit circle by exactly r, and that h(i) is at distance r from the axis.
9. **Proposition 8.2, p. 17.**
   - Recomputed the sides of T(π/2, π/3, π/m) for m = 7, 8, 12, 100, 4096: s_m = d(v2,v3) < s∞ = 0.549306; h_m = d(v2,vm) ≥ log(m/2π); h_m + s_m − d(vm,v3) > 0.
   - cosh(2s∞) = 5/3, and σ* = 0.5620668711…, which matches the stated 0.56206….
   - The cone-ball argument is correct: P is the regular m-gon about v_m with inradius h_m, and the tiles about distinct m-vertices are distinct. So is the systole argument: some point of the axis lies outside all cone balls, hence within 2s_m of an order-3 point; Lemma 8.1 then applies with sin²(π/3) = 3/4.
   - As an independent check, I computed systoles by enumerating reflection words up to length 16:
     - O(2,3,7): 0.98399;
     - O(2,3,8): 1.266;
     - O(2,3,12): 1.663;
     - O(2,3,50): 1.911.
   - All exceed σ*. The bound is valid but loose by a factor of about 1.75.
10. **Formula (5) and Proposition 8.3, p. 18.**
    - Checked (5) symbolically for w = sinh ρ and w = cosh ρ. The difference is 0, and q is as stated.
    - Checked the Rayleigh quotient bound, the min–max step and the pigeonhole count K = (⌊Λ_N/δ⌋+1)^{N−1}.
11. **Proposition 8.5 and the construction of Q_{k,b}, pp. 18–20.**
    - ⟨n1, n2⟩ = −sinh a sinh b = −cos(π/k), checked numerically for k = 3, 4.
    - ∫_{−a}^{a} ρ² cosh ρ dρ = 2[(a²+2) sinh a − 2a cosh a], checked symbolically, so the λ1 bound is right.
    - The regular member (a = b) has 4a = 4 arsinh(1/√2) = 2.6339, which matches the systole 2.634 quoted for ϑ = 0 on p. 15.
12. **Triangle-orbifold systoles, Fig. 2 and Table 2.**
    - Computed systoles: ℓ(O(3,3,12)) = 1.86260 and ℓ(O(2,8,8)) = 2.25677.
    - These identify ε = 1.8626 in Table 2 as the systole of O(3,3,12).
    - They also identify the two coloured markers in Fig. 2: orange at 1.86 is O(3,3,12), whose diamond near 39 matches N_apr = 39; teal at 2.26 is O(2,8,8), whose diamond near 21 matches N_apr = 21. This is consistent with Table 3.

**Not checked by me.** Sections 2.2 and 3 and Appendix A belong to other referees' charges. I spot-checked only the coefficients listed above. I did not check the eigenvalue computations themselves.

## MAJOR issues

**M1. The geometric control is far cruder than standard thick–thin tools allow, and the paper presents the resulting growth rates as if they meant something.** (Lemma 2.2 p. 4; Theorem 4.4 p. 11; the text after Table 1 on p. 11; pp. 13–14; the last paragraph of Section 8.2 on p. 20.)

- The diameter enters only through Lemma 2.2, as e^{3D}. Theorem 4.4 gives D ≍ A/ε + A M³ (Table 1: D = 6.4 × 10^5 at A = π/2, M = 100). With the Margulis lemma and collar and cone neighbourhoods, the diameter of an orbifold in C(A, ε, M) is O(A + n log(1/ε) + log M). The thick part has injectivity radius bounded below by a universal constant, not by ε. Collars of geodesics shorter than ε have length about 2 log(1/ε), and cone neighbourhoods of order-m points have radius about log m. Proposition 8.2 shows the log M is necessary.
- The M³ comes from two sources:
  - d0 ~ 1/M (Lemma 4.2). Once discreteness is used fully, Lemma 4.2 can be made uniform: by Knapp's classification of discrete groups generated by two elliptics (A. W. Knapp, *Doubly generated Fuchsian groups*, Michigan Math. J. 15 (1968) 289–304), the minimal distance should be of order d(v2, v3) in (2,3,7), which is 0.283. My `sep_scaling.py` shows that among genuine triangle-group configurations (k = 1) the minimum of cosh d − 1 is 0.0403, attained at (2,3,7) for every M ≤ 48. The cases k > 1 that make the paper's bound decay are the ones Knapp's list restricts.
  - The fixed-radius packing in Lemma 4.3.
- More fundamentally, the diameter can be avoided altogether. Counting closed geodesics through a thick–thin decomposition, as in Buser's book (*Geometry and Spectra of Compact Riemann Surfaces*, Lemma 6.6.4, for closed surfaces), gives n(x) ≤ C(A) e^x plus a term of order (number of short geodesics) × x/ε for iterates of short geodesics, with C(A) depending only on the area.
- Consequences in the paper:
  - The claim that N grows "roughly like ε^{−3} log(1/ε)" (p. 14, stated as an observation) is restated as fact on p. 20 ("The N of Theorem 6.2 grows like ε^{−3} log 1/ε as ε → 0 once t3 binds"). This rate is an artefact of D ≍ 1/ε. With D = O(log(1/ε)) one gets N ≲ ε^{−2} polylog(1/ε).
  - The sentence "by Proposition 8.2 below some growth in M is necessary" (p. 11) hides a gap of M³ against log M.
- This is not an error. But for a paper whose contribution is effectivity, the geometric constants should be reasonable, or the authors should say plainly that they are not and why.

**M2. The certified examples rely on systole and diameter bounds whose rigour the manuscript does not establish.** (Section 7, pp. 14–15; Theorem 1.2; Table 3; Fig. 2; the abstract's "certifies the signature".)

- Theorem 7.1 is correct as a conditional statement. Its application needs a proven lower bound ℓ for the systole and a proven upper bound Δ for the diameter.
- For the triangle orbifolds, the diameter bound is justified on p. 15 (twice the longest side). For O_ϑ the bound "at most 7.8" (Table 1 caption) is unexplained.
- No systole values or bounds are justified at all:
  - the values quoted for O(2,8,8) and O(3,3,12) (my computation: 2.2568 and 1.8626);
  - the values 2.634 down to 0.694 for O_ϑ.
- A systole found by enumerating words up to some length is an upper bound, not a lower bound, unless a word-length cutoff argument is supplied. The parameter ϑ of the family O_ϑ is never defined (p. 15: "doubles of quadrilaterals with all angles π/3 and two mirror symmetries"). The family is presumably a reparametrisation of the Q_{3,b} of Section 8.2, since 4 arsinh(1/√2) = 2.634.
- The certified claims therefore stand or fall with inputs that a reader cannot verify. The same concern applies, outside my charge, to the eigenvalue enclosures ε_j and the completeness of the computed lists. The text says "high-order finite elements and error estimates", which does not by itself give guaranteed enclosures. I flag this for the numerical referee.

**M3. The cusp claims in the abstract, the introduction and the caption of Fig. 3 overstate what is proved.** (Abstract, p. 2; p. 3 below Theorem 1.3; Section 8.1 heading; caption of Fig. 3, p. 19.)

- Proposition 8.3 proves only upper bounds: λ_j ≤ 1/4 + π²(j+1)²/h_m².
- The abstract says the orbifolds "acquire arbitrarily many eigenvalues near 1/4". "Near" requires a lower bound λ_j ≥ 1/4 − o(1), which is not proved. Nothing in the paper excludes eigenvalues well below 1/4.
- The text on p. 3 says "the spectrum below any fixed level crowds towards 1/4", and the caption of Fig. 3 says "the low spectrum crowds towards 1/4". Both are stated as facts. As a description they are also inaccurate: in the picture the paper itself proposes (an interval of length h_m), for fixed Λ > 1/4 the eigenvalues in [1/4, Λ] become dense, with count about (h_m/π)√(Λ − 1/4). What tends to 1/4 is each fixed λ_j.
- The page-18 paragraph is careful ("an observation and not a result"). The abstract, the introduction and the caption should be equally careful.
- The non-uniformity in Remark 8.4 uses only the uniform upper bounds plus pigeonhole. It does not need the cusp picture, and the paper should say so.
- Relevant literature that is not cited:
  - C. Judge, *On the existence of Maass cusp forms on hyperbolic surfaces with cone points*, J. Amer. Math. Soc. 8 (1995) 715–759, which proves monotone dependence of eigenvalues on cone angles. This may prove the observed "decreases in m" on p. 18, since a sphere with three cone points has a rigid conformal structure.
  - C. Judge, *Conformally converting cusps to cones*, Conform. Geom. Dyn. 2 (1998).
  - The authors already cite Garbin–Jorgenson [13], who study precisely elliptic degeneration. Its spectral consequences should be discussed.

## MINOR issues

- **m1 (p. 16, Section 8.1, first paragraph).** The sentence "we could not obtain the text of [16]" is inappropriate in a journal article. Jørgensen's inequality, with proof, is Theorem 5.4.1 of Beardon [15], which the paper already cites. Cite it there; the self-contained proof of Lemma 8.1 can stay as a convenience. Note also that the hypothesis "no parabolic elements" is stronger than needed: given discreteness, the hypotheses on B are equivalent to ⟨A,B⟩ being non-elementary.
- **m2 (p. 11, after Theorem 4.4).** "In no row of Table 2 is it the binding constraint through t1" is vacuous, because D does not enter t1. Rephrase as "D enters only t3, which binds in rows 4, 6 and 7".
- **m3 (p. 10, proof of Lemma 4.2).** The parenthesis "(both senses do)" is cryptic. Say that s1 s_λ is the rotation by ±2π/a, and that both lie in Γ_p̃.
- **m4 (p. 17, proof of Proposition 8.2).** Supply a reference or a one-line proof for two facts:
  - the folding f: H² → T is 1-Lipschitz, and d(z, Γ*v) = d(f(z), v);
  - each tile has exactly one vertex of type m (true because m ≥ 7 differs from 2 and 3), which is what makes γP and P have disjoint interiors.
  Also say explicitly that P is the regular m-gon with vertices at the images of v3 and inradius h_m.
- **m5 (p. 17, Proposition 8.2; Theorem 1.3).** σ* = 0.5620 is valid but weak: the true systoles of O(2,3,m), m ≥ 7, appear to be at least 0.984, attained at m = 7. A remark would let the reader see that the threshold ε ≤ 0.5620 in Theorem 1.3 and Remark 8.4 is an artefact of the method.
- **m6 (p. 18, after Remark 8.4).** "Every eigenvalue … decreases in m" is an empirical observation. Say so, or prove it via Judge's monotonicity (see M3).
- **m7 (p. 20, after Proposition 8.5).** "Already at a fixed systole" is inaccurate: b and b′ differ, so the systoles 4b and 4b′ differ. Say "at systoles bounded below".
- **m8 (p. 20, end of Section 8.2).** The ε^{−3} log rate is stated as fact here and as an unproved observation on p. 14. Make the two consistent (see M1).
- **m9 (p. 15, Section 7).**
  - Define ϑ.
  - State the systole of each member, and how it was bounded below (M2).
  - State the true systoles of O(2,8,8) and O(3,3,12), and explain why ε = 1.8626 was used for the class in Tables 2 and 3. It is the smaller of the two.
- **m10 (p. 9, proof of (H3)).** "With equality only if α = β = π/2 and d = 0" can simply read "with strict inequality since d > 0".
- **m11 (p. 1, Theorem 1.3 statement).** h_m ≥ log(m/2π) is used only to show h_m → ∞. Fine, but the statement could give h_m = arccosh(1/(2 sin(π/m))) alone.
- **m12 (p. 4, Lemma 2.2).** It counts oriented closed geodesics, that is, hyperbolic conjugacy classes, including non-primitive ones. Say so, since "closed geodesic" is ambiguous on orbifolds.

## Presentation (figures and captions included)

The writing is compressed but precise. Proofs are terse to the point of being hard to follow in places, notably the proof of (H3) and the proof of Proposition 8.2, although every step I expanded was correct.

I checked the following against the rendered pages:

- **Fig. 1 (p. 14).** It matches its description: five grey gap curves, the darkest growing like (25/12)t, the dashed geodesic bound, two dotted truncation errors and a narrow shaded window near t ≈ 0.05. There is no legend identifying the four lighter competitors; label them or list them in the caption. The shaded window is barely visible at print size.
- **Fig. 2 (p. 16).** The open diamonds (N_apr for M = 3, range 33–694 in Table 3) are completely hidden under the filled diamonds (M = 12, range 38–750). I verified this at 250 dpi: only filled diamonds are visible. Offset or restyle them. The caption should name the colours: orange is O(3,3,12) and teal is O(2,8,8), as identified from their systoles. The caption's "10^2 to 10^11 times fewer" is consistent with Table 3: the ratios run from about 5 × 10^2 to about 2 × 10^11.
- **Fig. 3 (p. 19).** Both panels are consistent with Proposition 8.3. Every plotted λ_j lies below its dotted bound, and panel (b) has values below (j+1)². The caption's last sentence is an unproved claim (M3).
- **Tables 1–3.** Tables 1 and 2 are fully reproduced (see Correctness, items 4 and 6).

The marked placeholders (author contributions, AI-use statement, Zenodo DOI) are treated as known, as instructed.

## Recommendation

**Minor revision**, conditional on M2.

Within my charge the mathematics is correct. I verified every hyperbolic-trigonometric identity, every geometric lemma and every constant of Tables 1 and 2 independently. The Jørgensen argument and the O(2,3,m) cusp argument are sound.

M1 is a request to modernise crude but valid estimates, or at least to describe them honestly. M3 is a matter of wording plus missing references.

M2 decides the recommendation. If the systole (and O_ϑ diameter) inputs to the certificate are rigorously justified in the revision, minor revision suffices. If they are only numerical, the certification claims in the abstract, Theorem 1.2's discussion and Table 3 must be downgraded to "consistent with" rather than "certified", and I would then regard that as a major revision.

Confidence: high (4/5) on the correctness of the geometric parts; moderate on the overall assessment, since Sections 2.2, 3 and the numerics were outside my charge.

## What resolves each issue

- **M1.** Do one of the following:
  - replace Lemma 2.2 and Section 4 by a thick–thin count of closed geodesics (Buser-type, extended to cone points), removing D;
  - improve Theorem 4.4 to D = O(A + log(1/ε) + log M) via collars and cone neighbourhoods, and make Lemma 4.2 uniform using Knapp's classification;
  - at minimum, add a paragraph stating that the A/ε and AM³ growth of D, and hence the ε^{−3} log rate of N, are artefacts of the method. Name the expected orders and delete the unhedged rate claim on p. 20.
- **M2.**
  - State and prove (or cite) lower bounds for the systoles of O(2,8,8), O(3,3,12) and every O_ϑ used in Table 3, for example by a word-length cutoff argument or by a Jørgensen/collar argument as in Proposition 8.2.
  - Prove the O_ϑ diameter bound of 7.8.
  - Define ϑ.
  - State what guarantees the eigenvalue enclosures and the completeness of the computed lists.
  - Otherwise, downgrade "certifies" accordingly.
- **M3.**
  - Change the abstract to "arbitrarily many eigenvalues below 1/4 + η for any η > 0", or prove λ_j ≥ 1/4 − o(1).
  - Change the sentence on p. 3 and the caption of Fig. 3 to the proved statement, with the crowding marked as numerical.
  - Note that Remark 8.4 needs only the upper bounds.
  - Cite Judge (1995, 1998) and discuss Garbin–Jorgenson [13].
- **m1.** Cite Beardon Theorem 5.4.1; delete the sentence about [16].
- **m2.** Rephrase as suggested.
- **m3.** Expand the parenthesis.
- **m4.** Add the folding reference or proof, the unique-m-vertex remark and the regular-m-gon description.
- **m5.** Add a one-line remark on the true systoles.
- **m6.** Label the claim as an observation, or prove it via Judge.
- **m7.** Reword.
- **m8.** Make the two statements consistent.
- **m9.** Define ϑ and add the systole data and the justification for ε = 1.8626.
- **m10.** Simplify the sentence.
- **m11.** Optional.
- **m12.** Add "oriented, not necessarily primitive".
- **Figures.**
  - Fig. 1: add a legend or caption list of competitors.
  - Fig. 2: make the open diamonds visible and name the colours.
  - Fig. 3: correct the caption.
