<!-- Round 9 A-d referee report: returned text saved verbatim; the reviewer could not write files -->

Writing to REPORT.md was refused (the harness does not let subagents write report files), so the full report is below.

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

**Referee A-d:** hyperbolic polygons and triangle groups.

**Scope of this report:**
- Section 5 (pp. 37–44), including Proposition 5.2 and Problem 5 (p. 47).
- Appendix D and Appendix E (pp. 55–56).
- Supplement S4–S7 (pp. 10–16).
- The hyperbolic-geometry input of Sections 3 and 6. For this I read Definition 2.1 and (2), Theorem 2.3, Lemmas 2.4–2.5, Corollaries 3.8 and 4.1, Lemma 3.6, the area examples of Section 3.3, Proposition 4.2 and Remark 4.3, Figures 4–5, and Propositions 6.1, 6.3 and 6.4.

I treated the marked placeholders as known. I rendered the relevant pages (pp. 35, 37–44, 47, 54–55) and checked every typographical and figure point below against the rendered images.

## Summary

Section 5 studies how many heat invariants determine a hyperbolic triangle orbifold O(p,q,r).

- **Corollary 5.1.** By (10), c1, c2, c3 are equivalent to (R, S1, P3), so three invariants determine a triangle orbifold among triangle orbifolds.
- **Proposition 5.2.** Against all of Sig, any rival sharing c1, c2, c3 must be a sphere with four cone points (a,b,c,d), a ∈ {2,3}, such that {1,p,q,r} and {a,b,c,d} have the same R, P1 and P3. Whether such a rival exists is Problem 5.
- **Section 5.1.** The triads of sum S are cut into strata by their least order p. Lemmas 5.3–5.4, Theorem 5.5 and Proposition D.1 locate the first sum at which adjacent strata overlap. Theorems 5.6–5.8 deduce three things: two invariants suffice for p+q+r ≤ 17; the pair O(2,8,8), O(3,3,12) is the only collision at sum 18; and this pair has the least area among all pairs in Sig sharing c1, c2.
- **Section 5.2.** Collisions are rational points on the cubics C_Λ. For Λ = 27/2 the curve is identified with y² = x(x+9)(x+384) (LMFDB 90.c3). Its rank is computed by hand by 2-isogeny descent (Appendix E) and its torsion is Z/2 × Z/6, so the minimal pair and its scalings form an isolated pair (Theorem 5.9).
- **Supplement.** S4–S6 give finite-element spectra of the minimal pair and of a one-parameter family of signature (0;3,3,3,3), a "blind" recovery of the cone orders, and checks of the trace formula against the computed traces.

## Significance

The part I refereed is correct, clean and fully elementary. I have no doubt about any proof in it. Its weight is modest, and I want to state this plainly.

- **Theorem 1.4(i)–(ii) is essentially a finite check.** Corollary 5.1 is Newton's identities for three numbers. Theorems 5.6–5.8 can be checked by hand on the 83 triads of Table S3. The general theory of strata (Theorem 5.5 for every p, Proposition D.1, Table S2, Figure 7) is correct, but no main result uses it beyond p ≤ 5, S ≤ 18 (see M3).
- **Theorem 5.9 is a computation on a single elliptic curve.** It is done correctly and, commendably, by hand.
- **The comparison of triangle orbifolds against all of Sig is the one geometrically interesting question in Section 5.** The paper leaves it open as Problem 5. It also states a weaker unconditional bound than its own tools give (M1).

What is good:
- The reduction in Proposition 5.2 is sharp and its proof is complete.
- The proof that the minimal pair has the least area against the whole class Sig (last part of Theorem 5.8) is a genuine statement about all hyperbolic 2-orbifolds, and it is proved, not searched.
- Appendix E is a model of a hand descent: every Selmer class is killed by an explicit local argument.
- The numerical sections are honest about what is validated and what is proved. Every numerical claim I could test independently came out right (below).

## Correctness, and what I recomputed

I checked every proof in my scope line by line. Using my own code (exact rational arithmetic with sympy, and floating point for the geodesics and the trace formula), I recomputed the following.

**Heat coefficients and (10).**
- p0, p1, p2 from (4)–(5) agree with (8).
- α0, …, α4 = 1, −1/3, 1/15, −4/315, 1/315.
- The closed form of Lemma 2.7 agrees with the Taylor coefficient of Φ_m (m = 7, k = 2).
- c1, c2, c3 for triangle orbifolds agree with (10).
- c2 = 67/48 for the minimal pair.
- d3, d4, d5 = 25/12, −1775/24, 153025/48 (Section 4 and Section S4) are exact.
- Table S6: c3(2,8,8) = −3.3354167 and c3(3,3,12) = −5.41875, consistent with the estimates and their error bars.

**Corollary 5.1.** The formula e3 = (P3 − e1³)/(3 − 3 S1 R) is correct, and the denominator is nonzero because S1 R ≥ 9.

**Proposition 5.2: every case checked.**
- Area < 2π forces g = 0 with n′ ≤ 5, or (g;n′) = (1;1).
- The (1;m) case gives the contradiction m³ = p³ + q³ + r³ < (p+q+r)³.
- In the five-order case the paddings (d = 2) give the values (p+q+r)R = 1 + 6/x (for {2,2,2,2,x}, any x ≥ 2) and 10/6, 11/12, 12/30 (for {2,2,2,3,x}, x = 3, 4, 5). All are below 9.
- In the four-order case, R(m′) = 1 + R > 1 forces a ∈ {2,3}.
- The converse direction, used in Problem 5, holds by the converse of Lemma 3.6. When p, q, r ≥ 2 the triad is automatically hyperbolic: R = 1 would force {a,b,c,d} = {2,2,2,2} and p+q+r = 7, and no Euclidean triad has sum 7.

**The Problem 5 search (Section S7).** I re-ran it independently:
- all {2,2,c,d} with d ≤ 1000;
- all {a,b,c,d} with a ∈ {2,3}, b ≥ 3, R(m′) > 1 and d ≤ 20000.

For each candidate I solved for e1, e2, e3 of {p,q,r} exactly and tested for complete integer splitting, allowing roots equal to 1. There are no solutions, which confirms the stated search.

**Section 5.1: brute force over all hyperbolic triads with S ≤ 700, in exact arithmetic.**
- There are 83 triads with 10 ≤ S ≤ 18. Every R value of Table S3 is correct.
- The first overlap of strata p, p+1 equals S\*(p) of Theorem 5.5 for every 2 ≤ p ≤ 15, and the overlap persists for the next 60 sums.
- The first adjacent collisions for p = 2, …, 11 agree with Table S2.
- The tangencies R⁻_{S,p} = R⁺_{S,p+1} occur only at (p,S) = (2,18) and (4,20) (p < 30, S < 400), as in Proposition D.1.
- The gap values are 1/840, 1/2310, 1/10296 and −7/936, −1/72, −19/3960, −1/180, −76/15015, −1/231, −17/4680, all as stated.
- I recomputed symbolically the closed form gap_p(3p+7) = −2(p²−5p−30)/(p(p+1)(p+3)(p+4)(p+5)) and the factorisation in (a). The identity x\*(p) − 18 = 3(p−2)(p−3)/(p−1) is correct.
- The first non-adjacent collision is (5,15,15), (7,7,21) at S = 35.
- The collision-free sums in [18, 700] are exactly the 38 listed in Computation S2.1, the last being 557. I did not go to 4800.

**Theorem 5.9.**
- ψ maps E into C_{27/2}, and φ∘ψ = id on E. I checked both by exact reduction modulo the equation of E.
- Δ = 2¹⁸3⁸5⁶.
- All twelve listed points lie on E, and their images under ψ are the twelve listed points of C_{27/2}.
- #E(F₇) = #E(F₁₁) = 12.
- The tangent at (16,400) is y = 21x + 64, with x³ + 393x² + 3456x − (21x+64)² = (x−16)³.
- (c4, c6) = (2305296, −3493537344), and (c4/2⁴, c6/2⁶) = (144081, −54586521). This is exactly (c4, c6) of the LMFDB curve 90.c3 = [1,−1,1,−3002,63929], which I fetched from the LMFDB API: rank 0, torsion [2,6], j = 4102915888729/9000000.

**Appendix E.** I checked every congruence by hand.
- On E: d ≡ 1 and c ≡ 3 (mod 5), d1 + d1⁻¹ ≡ 0, and in the three cases the right side is a non-residue. The torsion images are ±1, ±6.
- On E′: c′ = −786 and d′ = 3²5⁶.
  - d1 = 3: the bracket M⁴ − 262M²e² + 15625e⁴ is ≡ 1 (mod 3).
  - d1 = 5: f ≡ 2M⁴, and after M = 3M1 the bracket is ≡ 2 (mod 3).
  - d1 = 15: 5w² − w + 2 ≡ 6 (mod 9) for w ∈ {1,4,7}, so g ≡ 6e⁴ ≡ 6 (mod 9).
- Hence e1 = 2, e1′ = 0 and the rank is 0. The descent is complete and correct.

**Hyperbolic input.**
- Lemma 2.4: the counting argument, area 2π(cosh ρ − 1) of a disc, and the orbit argument through the Dirichlet domain are all correct.
- Lemma 2.5: I redid the integration by parts, the monotonicity of φ on the stated range, the bound on the Gaussian tail, the inequality 1 + 2t/(ℓ−t) ≤ (2+3ℓ)/(2+ℓ), and the logarithmic derivative in ℓ. All are correct.
- Remark 4.3: the Fourier identity, the kernel k_m and its poles at ±2πi/m are correct. From the residues I re-derived the asymptotics of Lemma B.3 used in Section 4, |b_l(m)| ~ (2π sin(π/m))⁻¹(πl)^{−1/2} l!(m/π)^{2l}.
- Section 1: sinh(d/2) = sinh r sin(πj/m) is correct, and so are the flat-cone values 0.55 and about 1.8.
- The Lambert-quadrilateral relation sinh a sinh b = cos(π/3) = 1/2 is correct. The systoles 4b(ϑ) at ϑ = 0 and 2.8 come out as 2.634 and 0.694.
- Corollary 3.8 and the area examples are correct: (1;3⁹)/(0;2¹⁶) at 12π, (0;2²⁸,4⁸)/(1;3²⁷) at 36π, (0;2¹⁰)/(1;4⁴) at 6π, (1;15)/(0;3,3,5,5), and (5,5,5)/(0;2,2,2,10).
- In Section 6 the hyperbolic input is only the area formula and n ≥ 3. amp1 = 14, amp2 = 498, the identity P3 = −18c̃1 − 120c̃2 − 360c̃3, and the bounds of Propositions 6.3(i) and 6.4 are correct.

**Supplement numerics that I could test independently.**
- Closed geodesics: from SL(2,R) words in the triangle groups, the three shortest lengths are 2.2568, 2.8816, 3.0571 for O(2,8,8) and 1.8626, 2.9807, 3.4027 for O(3,3,12), exactly as in S4.
- For O(3,3,12) the systole is the class of ab⁻¹, with cosh(ℓ/2) = 1/4 + (3/4)cosh c. That is consistent with "one geodesic, two orientations".
- I evaluated the elliptic terms of Theorem 2.3 through k_m by quadrature, plus the hyperbolic terms from these lengths (multiplicity 2). D(t) peaks at about 0.047 near t ≈ 0.1–0.2 and changes sign between t = 0.34 and 0.36, as stated in Section 4, Figure 5(a) and S4.
- The Bolza count of characters (four characters, of which Neumann and Dirichlet belong to O(2,3,8)) is correct.

I found no mathematical error in the proofs within my scope.

## FATAL

None.

## MAJOR

**M1. The unconditional bound for triangle orbifolds against Sig is stated too weakly (p. 38–39, Theorem 1.4, abstract).**

The paper says that Corollary 3.8 gives K_mult(O(p,q,r); Sig) ≤ 5, and ≤ 4 when R > 1/2. The paper's own tools give **≤ 4 for every triangle orbifold, unconditionally**:
- The proof of Proposition 5.2 excludes rivals of genus 1 or with five cone points using only the equalities of R, P1 and P3. These still hold when c1, …, c4 agree.
- For the remaining rivals, spheres with four cone points, Theorem 3.7 applies with max(n + g − g′, n′ + g′ − g) = max(3, 4) = 4. So equal H4 forces equal signatures. Equivalently, |U\*| + |V\*| ≤ 8 < 2·4 + 2.

So K_mult(O(p,q,r); Sig) ≤ 4 always, and = 3 for every O(p,q,r) exactly when Problem 5 has no solution. This belongs in Theorem 1.4 and in the abstract ("three suffice among triangle orbifolds, four against all orbifolds"). It replaces the current "≤ 5, ≤ 4 when R > 1/2", which a reader will take as the best the paper knows.

**M2. Problem 5 is misstated, and its structure is not exploited (p. 39, p. 47; Section S7).**

(a) As written, "positive integers p, q, r" is not equivalent to the claim that a negative answer is equivalent to K_mult ≤ 3. A solution with min(p,q,r) = 1 would answer the problem positively without giving a rival. It must read p, q, r ≥ 2. Add the remark that hyperbolicity of (p,q,r) is then automatic (argument in "Correctness" above).

(b) The system of Proposition 5.2 is exactly an n = 4 witness in the sense of Remark 3.5 and Theorem 3.4(1), with one entry equal to 1. The 8-element signed set {1,p,q,r,−a,−b,−c,−d} has s1 = s3 = 0 and vanishing reciprocal sum, so Q(z) − Q(−z) = 2κz³. Because (R, P1, P3)-equality is invariant under scaling, a solution of Problem 5 is the same as a rational n = 4 witness in which one side contains the greatest common divisor of all eight entries. The paper does not say this. It should:
- state the equivalence;
- report whether any of the 193 witnesses of Remark 3.5 (orders ≤ 440, which include the scalings by k ≥ 2 of all Problem-5 solutions with entries ≤ 220) has this form;
- say whether the pencil-splitting family of Section S1, which covers all but six of the 107 primitive witnesses, can contain such a member.

This would turn a bare search into a statement tied to the paper's own structure, and might settle Problem 5 for that family.

(c) Disjointness is not recorded. By Theorem 3.2 with n = 3, {a,b,c,d} ∩ {p,q,r} = ∅, and the 1 is not cancelled. Proposition 5.2 should say so, since it constrains any further search.

**M3. The general theory of strata is not used by any main result, and its role should be made explicit (pp. 39–42, Appendix D, Table S2, Figure 7).**

Theorem 1.4(i)–(ii) and Theorems 5.6–5.8 need only the strata with S ≤ 18, so p ≤ 5. Theorem 5.5 for all p, Proposition D.1, Table S2 and Figure 7 are correct, but they prove statements (first overlaps for every p, tangency only at p = 2, 4) that feed nothing. A referee for AGAG must ask what geometric or spectral content they carry. I do not ask for removal. I ask that the paper either:
- state a consequence that needs the general-p result (for instance a uniform statement about where collisions can first occur within each stratum pair, used later); or
- label Theorem 5.5 and Proposition D.1 explicitly as structural results that the main theorems do not depend on, and say in Section 1 that Theorem 1.4(i)–(ii) is a finite verification on 83 triads, made conceptual by the strata.

At present the introduction (p. 6, "for triangle orbifolds, Theorem 1.4 with its arithmetic part (iii)") presents this part as new results of weight, and the reader should be told precisely what is new: the least-area statement against all of Sig, and the isolation.

## MINOR

**m1 (p. 39, proof of Proposition 5.2).** "which leaves {2,2,2,2,x} and {2,2,2,3,x} with 3 ≤ x ≤ 5" reads as if the range applies to both families. For {2,2,2,2,x} every x ≥ 2 is allowed; that is why the value 1 + 6/x appears. Write "{2,2,2,2,x} (x ≥ 2) and {2,2,2,3,x} (3 ≤ x ≤ 5)".

**m2 (p. 39, Lemma 5.3 and the definition of R⁺_{S,p}).** For p = 2 the "spread triad" (2,2,S−4) is not hyperbolic, so R⁺_{S,2} is not a value of the stratum. Its true maximum is at q = 3, or q = 4 when S = 11. The text says "attained unless p = 2" but then defines R⁺_{S,p} = 2/p + 1/(S−2p) as "these extreme values" for every p. State explicitly that R⁺_{S,2} is only an upper bound. The proof of Lemma 5.4(ii) handles p = 2 correctly through (2,5,S−7), but the definition as written is false for p = 2.

**m3 (p. 41, Theorem 5.8).** The proof shows more than is stated: the minimal pair is the *unique* pair of least area in Sig sharing c1 and c2. The only other orbifold of area ≤ π/2 with four cone points is (0;2,2,2,4), which does not share c2. Say "the unique pair".

**m4 (p. 43, Theorem 5.9).** Notation clashes:
- O denotes both the base point (1:−1:0) and an orbifold.
- E denotes both the elliptic curve and the elliptic term E(t) of Theorem 2.3.
- In Appendix E, c and d are the coefficients 393 and 3456, while in Proposition 5.2 they are cone orders.
- S is the sum in Section 5 and the number of sign changes in Lemma 3.10.

Rename locally.

**m5 (p. 43, torsion step).** Cite the hypothesis of the reduction theorem precisely: p odd and p ∤ Δ, where Δ is the discriminant of the cubic. Note that 7 and 11 do not divide 2·3·5. Also give the edition of [63] for "§3.3, p. 70".

**m6 (p. 55, Appendix E).** Add one sentence on E′:
- α′(0,0) = d′ is a square, so torsion contributes only the class 1;
- the d1 < 0 classes are excluded by the real place;
- the normalisation gcd(M, e) = 1 is the one of [63, (3.6.2)].

The argument is complete, but the reader has to reconstruct these three points.

**m7 (p. 42, Figure 7).** The dots for p = 2 and p = 4 are hidden under the circles, because first overlap and first collision coincide there. Say so in the caption. Otherwise the reader looks for dots that are not visible.

**m8 (p. 38, Figure 6).** State which vertex the cap of radius 2.4 is centred at (an order-8 vertex in (a), the order-12 vertex in (b)?). The phrase "2m triangles of the tiling meet at a vertex of order m" would be easier to verify with the cone orders marked at the three vertices of the coloured triangle.

**m9 (p. 35, Figure 4(a)).** At ϑ = 0 the systole is attained by two geodesics (text, p. 34), but only one is drawn. Draw both, or say that one is drawn.

**m10 (Supplement p. 10, S4 "Convergence").** "At a corner of angle π/k the eigenfunctions extend to smooth Z_k-symmetric functions." Neumann and Dirichlet eigenfunctions extend by reflection to functions that are invariant (Neumann) or sign-twisted (Dirichlet) under the dihedral group of order 2k, the local group of the corner reflector, and are smooth there. "Z_k-symmetric" is the wrong group.

**m11 (Supplement p. 14, S6).** "The family is a real one-parameter slice, the orbifolds with an orientation-reversing isometry fixing the four cone points." This needs an argument, which is short and should be given:
- Such an involution fixes a single circle through the four cone points; two circles would make the quotient an annulus, whose double is a torus.
- So the orbifold is the double of a quadrilateral with all angles π/3.
- Every such quadrilateral has the two mirror symmetries, because a cyclically ordered 4-point configuration on a circle is Möbius-equivalent to a symmetric one with the same cross-ratio.

**m12 (Supplement p. 10, S4).** p is used both for the polynomial order of the finite elements and for a cone order. Rename one of them.

**m13 (Supplement pp. 10–12, S4 "Validation").** O(2,8,8) itself is covered by the Bolza surface, with index 8. The regular π/4-octagon is tiled by 16 copies of the (2,8,8) triangle, and the side pairings preserve the tiling. So the Neumann spectrum of the (2,8,8) triangle is contained in Bolza's spectrum. Indeed, the first Neumann value in Table S5, 3.838887, is Bolza's λ1 = 3.8388872588… of Strohmaier–Uski to the printed digits. The paper benchmarks only (2,3,8), which is not one of its orbifolds. A direct benchmark of one member of the minimal pair is available at no cost and should be used. The multiplicities follow from the character table of the automorphism group of order 96.

**m14 (Supplement pp. 12–13, S5).** The "blind recovery" separates two candidates whose c3 differ by about 1.5 × 10⁴ error bars, and the paper itself calls it easy by design. It shows that the pipeline works, but as evidence for anything it adds nothing to the exact statements. The text in Section 6 (p. 47) should not suggest more.

**m15 (p. 33, Corollary 4.1(a)).** "Any two hyperbolic structures of signature (0;p,q,r) are isotopic, hence isometric." The simpler and standard reason is that a hyperbolic triangle is determined up to isometry by its angles, so the triangle group is unique up to conjugacy. Use that.

## Presentation

**P1 (p. 38).** "All that the first two heat invariants record" (area and order sum) is a good sentence. Put the observation that c2 alone gives key2 on triangle orbifolds (12c2 + 2 = S1 + R with 0 < R < 1) into Corollary 5.1 or Theorem 5.7 as a stated fact: Theorem 5.7 then holds with c2 alone. In the language of prefixes this is the statement that K_iso ≤ 2 is already achieved by a single invariant, which deserves to be said.

**P2 (p. 43).** Theorem 5.9 says "isomorphic to Z/2 × Z/6" for the group of rational points of C_{27/2}. Make clear that the group law is the one transported by ψ, with base point (1:−1:0), and not the chord–tangent law with an arbitrary base point. They agree here, but the reader should not have to check.

**P3 (pp. 39–41).** Theorem 5.5 is easier to read if case (a) is stated as the formula of the gap for even S − p, followed by the sign table; the identity φ_p(S) − τ_p = … is the heart of the section.

**P4 (pp. 40–41).** Several fractions in the gap lists are typeset small and run together in the rendered PDF: 1/840, 1/2310, 1/10296 on p. 41 line 1, and in Appendix D. They are correct, but hard to read; use display or a table.

## Recommendation

**Minor revision** for the parts I refereed. My confidence is high that the mathematics in my scope is correct: I verified every proof and recomputed every number listed above independently.

The revision must:
- state the unconditional bound K_mult(O(p,q,r); Sig) ≤ 4 (M1);
- correct Problem 5 and relate it to the n = 4 witnesses (M2);
- make honest the role of the general strata theory (M3).

None of these needs new mathematics beyond what is in the paper. The numerical supplement is careful and correctly labelled as validated, not certified. One cost-free independent benchmark is missing (m13).

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Add the corollary "K_mult(O(p,q,r); Sig) ≤ 4 for every hyperbolic triangle orbifold" (proof: Proposition 5.2's exclusions plus Theorem 3.7 with L = 4). Update Theorem 1.4, the abstract, and the sentence on pp. 38–39. |
| M2 | Write p, q, r ≥ 2 in Problem 5 and note that hyperbolicity is automatic. State that a solution is an n = 4 witness with an entry equal to the gcd. Report the check against the 193 witnesses with orders ≤ 440 and against the pencil-splitting family. Add disjointness from Theorem 3.2 to Proposition 5.2. |
| M3 | Either give a use of Theorem 5.5 and Proposition D.1 for general p, or label them as independent structural results. Say in Section 1 exactly which statements of Theorem 1.4 are a finite check and which (least area in Sig, isolation) are not. |
| m1–m3 | Textual corrections as indicated; "unique" in Theorem 5.8. |
| m4–m6 | Rename the clashing symbols. Give the precise hypothesis and edition for [63]. Add the three sentences on E′. |
| m7–m9 | Captions and figures as indicated. |
| m10–m12 | Dihedral group in S4. The short argument for the real slice in S6. Rename the finite-element order. |
| m13 | Add the Bolza benchmark for the Neumann (and, via the characters, Dirichlet) spectrum of the (2,8,8) triangle. |
| m14–m15 | Temper the wording on the blind recovery. Use triangle rigidity in Corollary 4.1(a). |
| P1–P4 | As described. |

---
Scratch files are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/A-d-hyperbolic-polygon-geometer/scratch/:
- code/ec.py: the elliptic-curve checks.
- code/strata.py: the strata and collision checks.
- code/prob5b.py: the Problem 5 search.
- code/heat.py: the heat coefficients and d3–d5.
- code/geod.py: the closed geodesics.
- code/dsign.py: the sign change of D(t).
- dl/lmfdb.json: the LMFDB record for 90.c3.
- img/: the rendered pages.
