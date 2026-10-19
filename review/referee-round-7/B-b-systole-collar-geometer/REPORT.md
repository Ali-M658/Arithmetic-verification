<!-- Referee B-b: returned text saved verbatim; the reviewer could not write files -->

I could not save the report to REPORT.md: the Write call was refused (subagents must return findings as text). The full report is below.

# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Submitted to the Annals of Global Analysis and Geometry.

**Scope of this report.** I was asked to referee Sections 4 and 8 and every proof those results depend on. That covers:
- Lemmas 4.1–4.5 and Theorem 4.4 (the diameter bound and the counts of closed geodesics);
- Lemma 2.2 (counting with the diameter; the bound on the hyperbolic term), which Section 4 feeds;
- Lemma 8.1, Propositions 8.2, 8.3 and 8.5, Remark 8.4 and Problem 1;
- the systole and diameter inputs of Section 7.1 and Table 4, which come from the same geometry.

I treat Sections 2–3 (heat invariants), 5–6 (except where they use C\*) and the spectral numerics of Section 7 as belonging to the other referees. I read the rendered page images of pp. 7, 9–12 and 22–26 as well as the extracted text. Page numbers below are those printed on the pages.

## 1. Summary

Section 4 makes the class C(A, ε, M) geometrically effective, in four steps:
1. **Lemma 4.2.** Two distinct elliptic points are at distance at least d0 = min{ε/2, arccosh(1 + 2/(π²M²))}. The proof is a reflection-triangle argument: the product of two rotations is either hyperbolic, which brings in the systole, or a rotation about a third cone point, which brings in an integer angle defect.
2. **Lemma 4.3.** Every ball of radius 2r0 has area at least v0.
3. **Theorem 4.4.** A packing argument gives a diameter bound D ~ A·M³·max(1/ε, M).
4. **Lemma 4.5.** A second packing argument, based at cone points or at points with trivial stabiliser, gives n_O(x) ≤ C\*·eˣ in terms of A, ε and M alone. This count is the one Theorem 6.2 uses.

Section 8 contains two pieces.
- **§8.1.** The triangle orbifolds O(2,3,m) have:
  - area below π/3;
  - an embedded cone ball of radius h_m ≥ log(m/2π) (Proposition 8.2);
  - a systole bounded below uniformly in m, by ℓ₂,₃ = 0.56207. The proof is a self-contained hyperbolic-case Jørgensen inequality (Lemma 8.1) applied to the axis and a nearby order-3 point.

  Test functions on the cone ball give λⱼ ≤ 1/4 + π²(j+1)²/h_m² (Proposition 8.3). Pigeonhole then shows that the order bound M cannot be dropped (Theorem 1.3, Remark 8.4).
- **§8.2.** A pinching family O_{k,b} (doubles of quadrilaterals with angles π/k) gets a collar test-function bound (Proposition 8.5). Whether the systole bound is needed is left open (Problem 1).

## 2. Significance

**What is good.** Everything in my part is correct, and every proof is short and complete.
- Lemma 4.2 is a clean, explicit separation result for cone points under a systole bound.
- Lemma 4.5 removes the e^{3D} factor that a diameter-based count carries. This matters: with D from Table 2, πe^{3D}/A is between about 10^196 (A = 4π/3, M = 3) and 10^29326 (A = 10π, M = 12), against C\* ≤ 7 × 10^10.
- The uniform systole bound for O(2,3,m) keeps the counterexample family inside one class C(π/3, ε, ·). That is what turns the known elliptic-degeneration results (Garbin–Jorgenson) into a statement about the hypotheses of an effective theorem.

**Reservations.**
- The geometry is elementary and the constants are crude: the 1/M factors in d0 and v0 make D grow like M³. Nothing in Section 4 would stand as a paper on its own; its value is as the input to Theorem 6.2. That is legitimate for AGAG, but the Introduction should not present Theorem 4.4 as more than it is. Theorem 6.2 does not use it, and the e^{3D} count it gives is astronomically worse than Lemma 4.5 (see m6).
- Theorem 1.3 is a soft consequence (pigeonhole) of an upper bound plus the uniform systole bound. Its interest lies in the uniformity, which the authors say clearly.
- §8.2 contains no new result. Proposition 8.5 is the classical collar test-function argument, and the closing intermediate-value remark says nothing (see M2).

## 3. Correctness, and what I recomputed

I checked every proof in my scope line by line. Where it helped, I recomputed with my own code in `scratch/code/`.

**Lemma 4.1.**
- (H1): both displacement formulas check out, in the disc and half-plane models.
- (H2): the classification of products of reflections is right, including the asymptotic case and the fixed-point argument.
- (H3): the hyperboloid normal computation, cos θ = X, cosh h = X and the side argument are right. X ≥ −cos(α+β) rules out X ≤ −1 because d > 0.

**Lemma 4.2.** Correct.
- In the hyperbolic case, ε ≤ 2h ≤ 2d because X ≤ cosh d when α, β ≤ π/2.
- In the elliptic case the factorisation of cosh d − 1 is right.
- The defect π(abc − bc − ac − kab)/(abc) has a positive integer numerator, so cos((θ+α+β)/2) ≥ 1/(abc).
- |θ − α − β| ≤ π − π/M holds because α + β ≤ π − θ.
- With sin α sin β ≤ π²/(ab), these give cosh d − 1 ≥ 2/(π²cM).

**Lemma 4.3.** Correct.
- Γ_ỹ\B(ỹ, r) maps injectively when every γ ∉ Γ_ỹ moves ỹ by at least 2r.
- The elliptic displacement step uses sin(πj/k) ≥ sin(π/M) for 1 ≤ j < k ≤ M. This is implicit in the text (P3).
- ε ≥ 2ρ₁ holds because ρ₁ ≤ r0 = d0/2 ≤ ε/4.

**Theorem 4.4.** Correct, including the strict inequality.
- The closed-form chain checks out: cosh ρ₁ − 1 ≥ (cosh r0 − 1)sin²(π/M), v0 ≥ πr0²/max(M, M²/4), and arccosh(1+x) ≥ √(2x/(1+x)). The last is tight only as x → 0; numerically the margin stays nonnegative.
- 2/√(π²M² + 2) ≥ 0.6/M holds for M ≥ 2.
- **Table 2 recomputed exactly:** 56.6, 1125, 6.37 × 10⁵ / 150.9, 3001, 1.70 × 10⁶ / 640, 3184, 1.70 × 10⁶ / 1132, 2.25 × 10⁴, 1.27 × 10⁷. All entries agree. The closed form is 1.0–2.6 times larger.

**Lemma 4.5.** Correct.
- The 5r0 covering, the coset packing count M(cosh(R+ρ₁) − 1)/(cosh ρ₁ − 1), and d(b̃, γb̃) ≤ x + 10r0 are all right.
- Distinct classes give distinct γ, and cosh y − 1 ≤ eʸ/2.
- **C\* recomputed for every row of Table 3 and both columns of Table 4:** 1.32e8, 3.55e9, 4.01e5, 4.01e5, 9.45e9, 8.06e7, 3.01e6, 7.09e10, and 3.55e9 for the triangle orbifolds at M = 12. All agree.
- For these parameters d0 is fixed by M, not by ε. That is why the C\* columns of Table 4 are constant.

**Lemma 2.2.**
- (i): the Dirichlet-domain packing is correct.
- (ii): I redid three computations, all correct:
  - the integration by parts and the identity x e^{x/2−x²/4t} = −(2tx/(x−t)) d/dx e^{x/2−x²/4t};
  - the logarithmic derivative of B_C in ℓ (the bracket is ≥ 0 exactly when t ≤ ℓ²/(2(1+ℓ)));
  - the global bound, with its maxima at x = 2√t and x = 6t.
- The factor 1 + 2t/(ε−t) ≤ 3 used in Theorem 6.2 is valid on (0, t2].

**Lemma 8.1.** Correct. I checked:
- tr[A,B] − 2 = −bc(u − u⁻¹)²;
- the recursion for B_{n+1}, and x_{n+1} = −xₙ(1+xₙ)(u − u⁻¹)²;
- why xₙ = 0 cannot occur: when exactly one fixed point is shared, the commutator is parabolic;
- the fixed points pₙ, qₙ;
- the conjugated sequence Cₙ = A^{−kₙ}BₙA^{kₙ} → A with Cₙ ≠ A.

I also checked numerically:
- the commutator trace identity tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r;
- bc = −sin²(φ/2)cosh² r;
- that h moves i by r.

**Proposition 8.2.** Correct.
- The area formula, and h_m ≥ log(1/(2 sin(π/m))) ≥ log(m/2π).
- The folding identity d(z, Wv) = d(f(z), v).
- The cone ball: P is star-shaped, and its boundary sides are at distance h_m because the angle at v2 is right.
- The convexity step d(x, v3) ≤ 2s_m.
- β cannot swap the ends of the axis.
- **ℓ₂,₃ = 2 arsinh((2√(1 + (3/4)·(25/9)))⁻¹) = 0.5620669**, as stated.
- The quoted (2,3,7) value 2 arccosh((1 + 2cos(2π/7))/2) = 0.9839866 is the Klein-quartic systole divided by 4. The modular value 2 arccosh(3/2) = 1.9248473 is also right.

**Proposition 8.3 and identity (3).**
- I rederived q = 1/2 − w′²/(4w²) from w″ = w, and both special cases.
- Each sine arch has Rayleigh quotient at most 1/4 + π²/ℓ², and disjoint supports give the min–max bound for λⱼ.
- J = (⌊Λ_N/δ⌋ + 1)^{N−1} is right, since λ₀ = 0 leaves N − 1 coordinates. M in Remark 8.4 is right.
- I recomputed h_m and the λ₁ bound: 133.0 at m = 7 against the computed 44.89, and 1.017 at m = 4096 against 0.473.
- Fig. 3(b) is consistent with "6% to 16% above j²": for j = 1 at m = 4096, h²(λ₁ − 1/4)/π² ≈ 1.16.
- Remark 8.4 (A < π/3): the case analysis is correct.

**§8.2 and Proposition 8.5.** Correct.
- The normals (sinh b, cosh b, 0) and (sinh a, 0, cosh a), and the Lambert relation sinh a sinh b = cos(π/k).
- The Fermi rectangle {|ρ| < a, |s| ≤ b} ⊂ Q_{k,b}, the doubled collar and the separating core of length 4b.
- The λ₁ Rayleigh quotient: ∫ρ² cosh ρ = (a²+2) sinh a − 2a cosh a, so the bound is ~ 1/a² → 0.
- The λⱼ bound, with q ≤ 1/4 + 1/(4cosh²(a/2)) on [a/2, a).

**Section 7.1 geometric inputs.**
- **Triangle orbifolds:** I recomputed diam P = 2.448452 and 2.158170 from the second law of cosines, and the closed-form systoles 2.25676793 and 1.86260406. Rounded down, these give Table 4's 2.256767 and 1.862604; the second margin is 5.5 × 10⁻⁸, as claimed.
- **The family:** I built Q for ϑ = 0, 0.4, …, 2.8 on the hyperboloid. All eight values of diam P (2.2924, …, 3.8849) agree with Table 4.
- **Family systoles:** I enumerated all words of length at most 7 in the four order-3 rotations, in double precision. The shortest translation lengths were 2.633916 (ϑ = 0), 1.831303 (ϑ = 0.8) and 0.693993 (ϑ = 2.8), equal to 4b to the precision used. This agrees with Table 4, but it is again a computation, not a proof (M1).

**I found no error in the mathematics of Sections 4 and 8.**

## FATAL

None.

## MAJOR

**M1. The systole lower bounds that feed the test are not proved, although proving them is easy (pp. 18–20, Table 4; p. 25).**

Theorem 7.1 needs a lower bound ℓ ≤ systole, and C\*(A, ℓ, M) depends on it through d0. Every ℓ in Table 4 comes from a floating-point enumeration "not interval arithmetic". For the family, the paper itself says that Proposition 8.5 "proves only that the systole is at most 4b" (p. 19), which is the wrong direction.

The authors disclose this and present Section 7 as consistency checks. Still, a geometer will see this as the cheapest gap in the paper to close:
- **(a) Triangle orbifolds.** For O(2,8,8) and O(3,3,12), the systoles are explicit products of two elliptic generators. To prove nothing is shorter, run the paper's own enumeration-radius argument in interval arithmetic. That argument says every class of length ≤ L has a representative moving x0 by at most L + 2r, so only finitely many 2×2 matrix products need checking.
- **(b) The family O_ϑ.** The same interval enumeration works. Alternatively, the argument of Proposition 8.2 adapts: a geodesic shorter than 4b must avoid the collar or cross it, and a Jørgensen or collar estimate against the nearest order-3 point gives a rigorous lower bound. That bound may be weaker than 4b.
- **Little would change.** Even a weaker certified ℓ would make the inputs column of Table 4 a theorem. The counts in Table 6 depend on ℓ only through e^{−ℓ²/4t} and C\*, and C\* does not depend on ℓ in any row.

As written, the abstract's phrase "a systole bound computed in high-precision floating point" is accurate. The fix is cheap and would remove one of the five caveats listed in Section 7.

*To resolve:* certify ℓ for all ten examples, by interval arithmetic or by proof, and state it as a lemma. Otherwise, explain why this cannot be done.

**M2. §8.2 proves nothing new, lacks attribution, and its one remark says nothing (pp. 25–27).**

- **(i) Attribution.** Proposition 8.5 is the classical collar test-function bound for small eigenvalues near a short separating geodesic: Schoen–Wolpert–Yau (1980), Buser's book (Ch. 8), Dodziuk–Randol and others. The bound lim sup λⱼ ≤ 1/4 is also standard, as the authors' own citations [18]–[20] show. Cite these, and say plainly that Proposition 8.5 is included for its explicit constants.
- **(ii) The intermediate-value remark is empty** (p. 26: "two orbifolds of different signatures … share λ₁, which only says that N = 2 is too small"). Since λ₀ = 0 always, it only says that λ₁ alone does not determine the signature, which is obvious. Moreover O_{3,b} and O_{4,b′} have different areas (4π/3 and 2π). Problem 1 fixes A and M, so the interesting case is same-area signatures; Theorem 6.2 already separates different areas at the first heat invariant.
- **(iii) The discussion of Problem 1 should use same-area pairs.** Examples:
  - (0;3,3,3,3), (1;3) and (0;2,2,6,6), all of area 4π/3;
  - (0;2,8,8) and (0;3,3,12), both of area π/2.

  It should also say which degenerations each signature admits:
  - (1;3) has no separating essential curve whose complement is hyperbolic, because a disc with one cone point cannot have geodesic boundary. Its pinchings are therefore non-separating, with limit (0;3,∞,∞), and λ₁ does not tend to 0.
  - (0;3,3,3,3) pinched along a separating curve has λ₁ → 0.

  This bears directly on Problem 1(b). A negative answer needs two same-area degenerations with the same number of eigenvalues tending to 0 and the same limit spectrum below 1/4. The current discussion hides this.

*To resolve:*
- cite the classical collar bounds;
- delete the intermediate-value remark, or replace it with a same-area statement;
- rewrite the paragraph after Problem 1 around same-area degenerations.

## MINOR

**m1. ℓ₂,₃ can be improved to log 2 with the paper's own argument (p. 24).** The bound d(x, v3) ≤ 2s_m is wasteful. In T minus B(v_m, h_m), the boundary has three pieces:
- the segment [v2, v3], where the distance to v3 is at most s_m;
- the part of [v_m, v3] outside the ball, where it is at most d(v_m, v3) − h_m ≤ s_m;
- the arc of radius h_m about v_m, where by the law of cosines the distance to v3 is largest at the end v2, equal to s_m.

So r ≤ s_m < s_∞. Then 4 sinh²(L/2)(1 + (3/4)cosh² s_∞) = 8 sinh²(L/2) ≥ 1, which gives L ≥ 2 arsinh(1/(2√2)) = log 2 = 0.6931 exactly; I checked this numerically. Theorem 1.3 would then read "systole at least log 2". This is optional but cleaner. The authors already acknowledge (p. 24) that the 2s_m step is where the bound loses.

**m2. "The factors 1/M in d0 and v0 are not intrinsic" (p. 11) is asserted without proof.** Prove it, cite it, or soften it to an expectation. Two points matter:
- Without a systole bound, two order-2 points can be arbitrarily close, because their product is a translation by twice their distance. So the systole term is necessary.
- For orders at least 3, collar and cone-neighbourhood theorems for hyperbolic cone-surfaces with angles at most π (e.g. Dryden–Parlier, *Collars and partitions of hyperbolic cone-surfaces*, Geom. Dedicata 127 (2007) 139–149) should give separations independent of M. That would improve D from M³ growth. Please check and cite.

**m3. Lemma 4.5 compared with Buser's count (p. 4 and p. 11).** The Introduction contrasts Lemma 4.5 with Buser's (g−1)e^{L+6} count. Buser's count needs no systole bound because it excludes iterates of short geodesics. Add a sentence on why that route is not taken here: the heat-kernel bound needs all classes, iterates included, and the systole enters through e^{−ℓ²/4t} anyway. The point is that the ε-dependence of C\* is not the bottleneck; t3 is.

**m4. Proposition 8.5 states only ℓ ≤ 4b; it should give both bounds (p. 25).** The construction is symmetric in a and b, so ℓ(O_{k,b}) ≤ 4 min(a, b), and Section 7 uses ϑ ≥ 0, that is, b ≤ a. Say so, since Table 4 identifies the systole with 4b.

**m5. "Every computed eigenvalue … decreases in m" (p. 25).** This is labelled an observation, which is fine. But Fig. 3(b) shows h_m²(λⱼ − 1/4)/π² increasing in m for j ≥ 2 at small m. That fits decreasing λⱼ only because h_m increases. One sentence would prevent misreading.

**m6. The comparison with the diameter-based count is not stated (p. 12).** "C\* lies between 4 × 10⁵ and 7 × 10¹⁰, against πe^{3D}/A with D of Table 2" leaves the reader to work out the other side. Give it: by my computation, πe^{3D}/A ranges from about 10^196 to 10^29326 on these classes. This also makes clear that Theorem 4.4 has no bearing on the size of the constants in Theorem 6.2.

**m7. Self-contained proof of Jørgensen's inequality (p. 22).** Here ⟨γ, β⟩ is non-elementary: β fixes no boundary point and does not preserve the axis. So the classical Jørgensen inequality ([41]; [35, Thm 5.4.1]) applies directly. The self-contained proof is correct and may stay, but say in one line that it is the standard inequality applied to a non-elementary pair.

**m8. Wording of the enumeration-radius argument (p. 19).** The text says "move a point of the axis into P by the reflection group, in which Γ is normal". The element obtained is W-conjugate to γ, not necessarily Γ-conjugate; it may be the mirror class. This is harmless for lengths but should be said. Also explain why tiles out to L + 3r, rather than L + 2r, are enumerated.

## PRESENTATION

- **P1** (p. 12, end of the proof of Lemma 4.5): "≤ Keˣ" uses an undefined K. It should be C\*eˣ.
- **P2** Several symbols are reused for different things:
  - λ is a line in (H3) and the proof of Lemma 4.2, and an eigenvalue elsewhere;
  - α, β are angles in §4, β is a rotation in Proposition 8.2, and β, β′ are lines in §8.2;
  - A is the area bound and also a matrix in Lemma 8.1;
  - ρ₁ (Lemma 4.3) sits next to the Fermi coordinate ρ (§8).

  Rename the matrices (e.g. g, h) and the lines.
- **P3** (p. 11, Lemma 4.3): state sin(πj/k) ≥ sin(π/M) explicitly.
- **P4** (p. 23): "ℓ₂,₃ = 0.56206…" is accurate (0.5620669), and "0.5620" in Theorem 1.3 is a valid rounded-down value. Keep the two consistent with m1 if it is adopted.
- **P5** (Fig. 3, p. 26): the dashed bound for λⱼ runs next to λ_{j+1}, as the text concedes, which makes panel (a) hard to read. Label each dashed curve, or plot the bound with numerator j² labelled as a heuristic.
- **P6** (p. 4): "Theorem 4.4 supplies such a diameter bound" for Proctor–Stanhope. Add that in an isospectral family the systole and the orders are fixed by the spectrum (Huber's theorem for orbifolds [1]), so the hypotheses of Theorem 4.4 are indeed spectral.
- **P7** (Table 2 caption): the diameters "from 2.29 to 3.88" for the eight orbifolds of signature (0;3,3,3,3) are computed values. Say "computed", to match Table 4.

## Recommendation

**Minor revision, as far as Sections 4 and 8 and their dependencies are concerned. Confidence: high.**

The mathematics in my scope is correct. I found no error in any proof, and every number I recomputed agrees: Table 2, the C\* values of Tables 3–4, ℓ₂,₃, the (2,3,7) and modular systoles, and the diameters and systoles of Table 4.

The two MAJOR points are not errors:
- M1 is an input that is not yet certified and is easy to certify.
- M2 concerns attribution and how much §8.2 actually contributes.

For the overall verdict, I defer to the referees of Sections 2–3 and 5–7 on the heat-invariant and numerical parts.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Certified systole lower bounds for the ten examples, by interval enumeration or proof, stated as a lemma. |
| M2 | Cite the classical collar eigenvalue bounds; remove or replace the intermediate-value remark; rewrite the Problem 1 discussion around same-area degenerations. |
| m1 | Replace 2s_m by s_m, so ℓ₂,₃ becomes log 2 (optional). |
| m2 | Prove, cite (Dryden–Parlier or similar), or soften "not intrinsic". |
| m3 | One sentence on why a Buser-type count does not help here. |
| m4 | State ℓ ≤ 4 min(a, b) and the convention b ≤ a. |
| m5 | One clarifying sentence. |
| m6 | Give the magnitude of πe^{3D}/A. |
| m7 | One sentence noting that the pair is non-elementary. |
| m8 | Clarify W- versus Γ-conjugacy and the L + 3r radius. |
| P1–P7 | Editorial. |

---

The checking scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/B-b-systole-collar-geometer/scratch/code/`:
- `consts.py`: Table 2, C\*, ℓ₂,₃ and the bounds;
- `fam.py`: the family's quadrilaterals, diameters and systole enumeration.

The page renders are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/B-b-systole-collar-geometer/scratch/pages/`.
