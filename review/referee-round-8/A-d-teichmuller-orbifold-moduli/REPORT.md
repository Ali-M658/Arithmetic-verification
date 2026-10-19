<!-- Round 8 A-d referee report: returned text saved verbatim; the reviewer could not write files -->

I couldn't write `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/A-d-teichmuller-orbifold-moduli/REPORT.md`: the write was refused because subagents must return reports as text. As instructed, the full report follows. It recommends minor revision; I found nothing fatal and no mathematical error in my part.

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

**Referee's area:** Teichmüller and moduli spaces of hyperbolic orbifolds; arithmetic triangle groups and their length spectra.

**What I was asked to review:** Section 5 (triangle orbifolds), Appendix D (which Section 5 uses), Appendix E (the rank of C_{27/2}), supplement Sections S2, S4, S5, S6 and S7, and the hyperbolic-geometry input to Sections 3 and 6. That input is the trace formula, the geodesic count (Lemma 2.4), the hyperbolic remainder (Lemma 2.5), Corollary 4.1, Lemma B.3 and Remark B.4, and the existence and area facts for signatures.

**Placeholders:** I treated the marked placeholders as known (author contributions, AI-use statement, Zenodo DOIs, preprint identifiers).

**Rendered pages checked:** manuscript pp. 36–42 and 50–53; supplement pp. 7–14.

---

## 1. Summary

Section 5 studies which heat invariants determine a hyperbolic triangle orbifold O(p,q,r) among triangle orbifolds.

- **Three invariants suffice.** By (10), c1, c2, c3 are equivalent to (R, S1, P3). These give e1, e2, e3 through e3 = (P3 − e1³)/(3 − 3 S1 R) (Corollary 5.1).
- **Two invariants suffice up to cone-order sum 17.** The triads of a fixed sum S are split into strata by their least order p. The reciprocal sum R is monotone on each stratum (Lemma 5.2). An exact computation of the "gap" between adjacent strata (Lemma 5.3, Theorem 5.4, eq. (15)) shows that no two triads of sum at most 17 share (S1, R) (Theorems 5.5 and 5.6).
- **The first failure.** O(2,8,8) and O(3,3,12) form the only collision at sum 18. They are also the collision of least area (Theorem 5.7).
- **Isolation.** Collisions correspond to rational points on the cubic C_Λ: (X+Y+Z)(XY+YZ+ZX) = Λ·XYZ. For the minimal pair, Λ = 27/2. Theorem 5.8 shows that C_{27/2} is isomorphic to E: y² = x(x+9)(x+384), an elliptic curve with E(Q) ≅ Z/2 × Z/6. Appendix E proves the rank is 0 by a hand 2-isogeny descent. So every scaling O(2k,8k,8k), O(3k,3k,12k) is a collision of exactly two orbifolds.
- **Numerical illustration.** The supplement computes about 2850 eigenvalues of each orbifold of the minimal pair by hp finite elements. It recovers d3 and d4 from the computed traces, runs a pre-registered blind recovery of the cone orders, and computes a one-parameter family in the Teichmüller space of (0;3,3,3,3) in which the heat expansion is fixed and the spectrum moves.

## 2. Significance

Within my remit the results are correct, complete and clearly separated from what is only computed.

- **What is new.** The sharp threshold 17/18 for two invariants and the arithmetic isolation statement are new. They make precise the remark of Dryden–Gordon–Greenwald–Webb (Rem. 5.16) that c2 "does not seem sufficiently strong" for triangular pillows. The link to the cubics of Bremner–Guy–Nowakowski, at a non-integral Λ they do not treat, is a pleasant one.
- **What is not deep.** "Three invariants suffice" is the case n = 3 of Newton's identities, as the authors say. The strata analysis is elementary.
- **Fit for the journal.** The section is a solid, honest contribution and suits AGAG, as part of a longer paper.

**The main weakness is scope.** The paper's own question is "against all of Sig". For triangle orbifolds it stops at "we do not know" whether three invariants suffice there (p. 37). I show below (M1) that this question reduces, by a few lines of elementary case analysis, to one Diophantine problem. That problem is very likely within the authors' reach, and they should address it.

## 3. Correctness, and what I recomputed

I recomputed everything below independently: exact rational arithmetic in Python/SymPy, floating-point PSL(2,R) matrices for the geodesics, and an LMFDB lookup. **Every number matched.**

### Section 5 and Appendix D

- **Table S3 (83 triads).** There are exactly 83 hyperbolic triads with 10 ≤ S1 ≤ 18. The only coincidence of R within a sum is (2,8,8) and (3,3,12), with R = 3/4.
- **Theorem 5.4, checked by brute force.** For every p from 2 to 59 and every S in [3p+3, 3p+119], I enumerated both strata and compared their convex hulls with the claimed S*(p). There was no mismatch.
- **Gap values.** I confirmed:
  - gap_3(18) = 1/840, gap_7(28) = 1/2310, gap_8(31) = 1/10296;
  - gap_2(9) = gap_2(10) = 1/12;
  - the seven values gap_p(S*(p)+1) for p = 2,…,8: −7/936, −1/72, −19/3960, −1/180, −76/15015, −1/231, −17/4680.
- **Closed form at 3p+7.** SymPy gives gap_p(3p+7) = −2(p²−5p−30)/(p(p+1)(p+3)(p+4)(p+5)).
- **Other identities.** I checked the factorisation of φ_p − τ_p, the formula for φ′_p, x*(p) − 18 = 3(p−2)(p−3)/(p−1), and identity (15).
- **Appendix D.** The divisibility argument (p−1) | 6 and the parity check are correct.
- **Table S2.** Enumerating all triads up to S = 600, I reproduced every first collision for p = 2,…,14.
- **Other collision facts.** The first non-adjacent collision is (5,15,15) and (7,7,21) at S = 35. Among collisions with S < 200, the one with largest R (least area) is the minimal pair.
- **Computation S2.1.** Recomputed independently for 18 ≤ S ≤ 600: I get exactly the 38 listed collision-free sums, the last being 557. This range covers every listed sum; I did not go up to 4800.
- **Proof of Theorem 5.7.** The majorisation argument is correct.
- **Corollary 5.1.** The formula for e3 and the AM–HM bound S1·R ≥ 9 are correct.
- **Example O(5,5,5) against (0;2,2,2,10).** The areas are equal (4π/5) and Σ(m − 1/m) = 14.4 on both sides, so they share c1 and c2.

### Theorem 5.8 and Appendix E

- **The map ψ.** Substituting ψ into the cubic gives C_{27/2}∘ψ = −10800·(y² − x³ − 393x² − 3456x), identically.
- **The inverse φ.** φ∘ψ is the identity modulo the equation of E, and φ(1:4:4) = (−24, 360).
- **The twelve points.** All twelve listed points lie on C_{27/2}.
- **Invariants of E.** Δ = 2^18·3^8·5^6, and j = 4102915888729/9000000.
- **LMFDB match.** LMFDB 90.c3 has a-invariants [1,−1,1,−3002,63929], c4 = 144081 and c6 = −54586521. These equal c4(E)/2⁴ and c6(E)/2⁶, so E ≅ 90.c3 over Q. LMFDB lists rank 0, torsion [2,6], analytic rank 0 and Sha = 1.
- **Torsion.** #E(F_7) = #E(F_11) = 12, and all eleven affine points lie on E. The tangent line at (16, 400) cuts E in (x−16)³, so (16, 400) is a flex.
- **Appendix E descent.** I checked every congruence by hand:
  - On E, the classes ±2 and ±3 fail 5-adically. The right-hand side is ≡ d1, d1⁻¹ or ±3 mod 5, a non-residue in each case.
  - On E′, the classes 3, 5 and 15 fail 3-adically. I checked the brackets mod 3 and mod 9: 5w² − w + 2 ≡ 6 for w ∈ {1,4,7}.
  - The negative classes fail over R.
  - The images of the 2-torsion points are {1, 6, −1, −6} and {1}.
  - Hence rank = 2 + 0 − 2 = 0, with Sha[φ] trivial.

  **The descent is correct and complete.**

### Hyperbolic input

- **Lemma 2.4.** The Dirichlet-domain packing argument is correct.
- **Lemma 2.5.** I checked:
  - the integration by parts and the sign of (log ϕ)′ on the stated range;
  - the bound x/(x−t) ≤ ℓ/(ℓ−t);
  - the identity (ℓ+t)/(ℓ−t) = (2+3ℓ)/(2+ℓ) at the endpoint t = ℓ²/(2(1+ℓ));
  - the constant √π/2.

  All are correct.
- **Centraliser weights in the trace formula.** These are correct in the presence of torsion: centralisers of hyperbolic elements are infinite cyclic.
- **Systoles of the minimal pair.** I built both triangle groups as matrices and enumerated reduced words up to length 9. This gives 2.256768, 2.881637, 3.057142 for O(2,8,8) and 1.862604, 2.980681, 3.402746 for O(3,3,12). These match S4 and are consistent with ℓ0 = 2.2567.
- **Diameter bound.** The longest side of the (2,8,8) triangle is arccosh(cot²(π/8)) = 2.448452. The argument that D = 2 × (longest side) is a diameter bound is correct.
- **Size of the closed-geodesic term of O(3,3,12).** From ℓ = 1.8626 with two orientations, I get about 4.0×10⁻¹³ at t = 0.0293, 7.8×10⁻¹³ at t = 0.03, and 2.7×10⁻¹⁵ at t = 0.025. These match S4. Also (π/12)² ≈ 0.069 and ℓ²/4 ≈ 0.867.
- **Remark B.4.** For the times (t3/4, t3/2, t3), the third row sum of the scaled inverse Vandermonde matrix is 16, and Q3 = 3·b2(12) = 303.63. Hence δ1 ≈ 4858·t3, the threshold t3 ≤ 7.8×10⁻¹¹, and η ≤ 2.07×10⁻¹⁹ at t3 = 10⁻¹¹. All as stated.
- **Coefficients for the minimal pair.** p0, p1, p2 agree with (8), and α0,…,α4 agree with the text. The differences are d3 = 25/12, d4 = −1775/24 and d5 = 153025/48. The values c1 = 1/8 and c2 = 67/48 for both, and c3 = −3.335417 and −5.418750, are consistent with Table S6 within its error bars.
- **Front-end amplification (Section 6).** amp0,…,amp4 = 2, 14, 498, 4062, 56230/3. P3 = −18c̃1 − 120c̃2 − 360c̃3. The diagonal of F is as stated.
- **Proposition 6.3(i) and Proposition 6.4.** δR = s²/(4(64−s²)) and δP3 = 48s² for (2,8,8); the constant is 498 + 42a². Correct.
- **Corollary 4.1.** The dimension 6g − 6 + 2n is correct. The countable-fibre argument through Out(Γ) is correct.
- **The (0;3,3,3,3) family.** The Lambert relation sinh a · sinh b = cos(π/3) holds. The endpoint systoles are 4b = 2.6339 at ϑ = 0 and 0.6940 at ϑ = 2.8. The simple geodesic around two adjacent cone points satisfies cosh(ℓ/2) = (3/4)·cosh s − 1/4, where s is the side; this reproduces cosh(2a) exactly. So the systole formula is consistent with the trace identities.
- **Witness counts (Remark 3.5).** Recomputed up to orders 100: there are 12 primitive n = 4 witnesses, and exactly the eight of Chen (A.685)–(A.692) have all orders at most 84. This confirms the claim within that range.

**I found no mathematical error in the part assigned to me.**

## 4. FATAL issues

None.

## 5. MAJOR issues

**M1 (p. 37, after Corollary 5.1; also Theorem 1.4 and the abstract). The open question "is K_mult(O(p,q,r); Sig) ≤ 3?" reduces to one finite-type problem, and the paper should do that reduction.**

The reduction:

- A rival O′ must have the same area 2π(1 − R) < 2π. By (2), the only possible signatures are (0;3 points), (0;4 points), (0;5 points) and (1;m).
- **(1;m) is impossible.** Lemma 3.6 forces m = p+q+r and m³ = p³+q³+r³.
- **Five cone points are impossible.** They need R(V) = R + 2 > 2. That forces V = {2,2,2,2,m} or V = {2,2,2,3,m′} with 3 ≤ m′ ≤ 5. The first gives R_triad = 1/m < 9/(m+6) ≤ R_triad, a contradiction. The other three are finitely many cases, each failing directly.
- **Four cone points remain.** Equal heat data mean the 4-multisets {1,p,q,r} and {a,b,c,d} have equal (R, P1, P3), with a ≤ 4 because R(V) > 1. This is an ideal balanced 3-configuration of size 8 containing the entry 1 — the n = 4 witness problem of Remark 3.5 with one order equal to 1. The search in Remark 3.5 excluded orders equal to 1 by design.

I ran this search (one side {1,p,q,r} with p,q,r ≤ 300 hyperbolic; other side a ∈ {2,3,4}, b,c,d ≤ 300). **It found no solution.** A full 4-multiset search with entries ≤ 100, including 1, found no pair in which exactly one side contains 1.

This strongly suggests that K_mult(O(p,q,r); Sig) = K_mult(O(p,q,r); Sig_{0,3}) ≤ 3. The pair criterion (Theorem 3.4(1)) turns the remaining case into rational points on explicit curves, one for each a ∈ {2,3,4}, which may well be provable.

**Requested:** state the reduction; extend the existing search to include an order 1; and either prove the statement or record it as the precise open problem. As written, the headline "three invariants always suffice" in the abstract reads as a statement against all orbifolds, but it is proved only within triangle orbifolds. The abstract and Theorem 1.4 must say "among triangle orbifolds" at that point. Theorem 1.4 already does; the abstract sentence "Among triangle orbifolds three invariants always suffice" is ambiguous about the comparison class.

## 6. MINOR issues

**m1 (p. 42, Theorem 5.8, "The model").** The argument through the closure of ψ(E), geometric genus, "not a line, a conic or a singular cubic", and then a birational morphism is correct but roundabout. ψ is the restriction of a projective linear map of P², with matrix ((25,1,0),(25,−1,0),(4,0,−864)) and determinant 43200 ≠ 0. A direct check gives C_{27/2}(ψ) = −10800·(equation of E). So ψ is a projective change of coordinates carrying E onto C_{27/2}. Nonsingularity and the isomorphism follow at once. Replace the paragraph.

**m2 (p. 39, proof of Lemma 5.3(ii)).** The case p = 2 cites "(a), (b) below", i.e. the proof of Theorem 5.4, which in turn uses Lemma 5.3(ii). There is no circularity, since (a) and (b) are direct sign computations, but the order of the argument should be made explicit. Simpler: state the needed fact "gap_2(S) ≤ 0 implies S ≥ 18" as a separate line, checked from the closed form of φ_2 − τ_2.

**m3 (p. 38, Lemma 5.2).** "Maximum at the spread triad q = p (attained unless p = 2 …)". For p = 2 the maximum of the stratum is attained at (2,3,S−5), and R⁺_{S,2} = 1 + 1/(S−4) is only an upper bound. Say so, because Lemma 5.3(i) uses R⁺_{S,p″} as an upper bound and Lemma 5.3(ii) uses R⁺_{S,p+1} as an attained maximum only for p+1 ≥ 3.

**m4 (p. 42, Theorem 5.8, "Torsion").** Cremona §3.3 should be cited with the exact hypothesis: good reduction at an odd prime p, where the absolute ramification index 1 is less than p − 1. Note also that the orders of the six points of order 6 follow from the group structure rather than from separate checks. A sentence saying this would help.

**m5 (p. 41).** The minimal pair is a "reciprocal pair": C_Λ is invariant under the Cremona involution (X:Y:Z) ↦ (YZ:ZX:XY), which exchanges (1:4:4) and (4:1:1). Saying this explicitly is more informative than the pointer to BGN's remark. It also shows that the collision class is a single orbit of S3 × ⟨involution⟩ on E(Q), which may interest readers.

**m6 (supplement p. 13, S6).** "Pairwise non-isometric" rests on floating-point systoles 4b(ϑ). This can be made exact cheaply. The closed geodesics of lengths 4a and 4b exist exactly (via the Lambert relations), and the moduli of the quadrilateral determine the point of Teich(0;3,3,3,3) up to the action of the mapping class group. Alternatively, keep "numerical" and say so in Section 4 as well; at present the main text states it (p. 33) with a parenthetical qualifier.

**m7 (supplement p. 10, Table S5).** The first Neumann eigenvalue of the (2,8,8) triangle, 3.838887, equals the first eigenvalue of the Bolza surface (3.8388872588…, Strohmaier–Uski). This is to be expected: Δ(2,8,8) ⊂ Δ(2,4,8) ⊂ Δ(2,3,8), and the coincidence shows that Bolza covers O(2,8,8). It gives a direct, independent benchmark for O(2,8,8) itself, stronger than the (2,3,8) benchmark of S4(iii). The authors should state the covering relation (with a reference or a short proof) and use it.

**m8 (p. 37).** "Against orbifolds that are not triangle orbifolds two invariants fail earlier." Give the comparison precisely: cone-order sums 15 against 16 and area 4π/5, both below the minimal pair's 18. As it stands, "earlier" is ambiguous between area and sum.

**m9 (supplement p. 8, Table S2).** The column "gap" (first collision minus S*) clashes with the function gap_p(S) of Section 5. Rename it, for example to "delay".

## 7. Presentation

**P1.** Fig. 6 is called "exact tilings of the hyperboloid", but the reader sees a disc-like ellipse. One sentence on the projection already appears in the text (p. 36) and should be repeated in the caption.

**P2.** In Lemma B.3 the times are indexed t1 < … < tn, while Remark B.4 writes them as t3/4, t3/2, t3. State explicitly that n = 3 and t_n = t3 there.

**P3.** In Appendix E, the sentence "then v is odd or f0 ≡ 2 (mod 3)" should end with "so f is not a square in Q3", to close each case explicitly.

**P4.** Section 5 relies throughout on the convention p ≤ q ≤ r together with "least order p". The (S,p)-stratum is defined once, with the bound q ≤ (S−p)/2, but Lemma 5.3 also uses strata at sums where they are empty (S = 9, 10). A sentence on the convention for empty strata would help.

**What is good.** The writing of Section 5 is clear. The separation of proved from computed statements, in S7 and in the "validated, not proved" language of S4–S5, is exemplary. The pre-registered blind recovery is a model of honest numerical illustration.

## 8. Recommendation

**Minor revision**, for the parts I reviewed.

**Confidence:** high for Section 5, Appendices D and E, and the hyperbolic input, all of which I recomputed. Medium for the finite-element numerics, which I could check only for internal consistency and against exact trace-formula quantities.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Add the area case analysis reducing K_mult(O(p,q,r); Sig) ≤ 3 to {1,p,q,r} ~ {a,b,c,d} with a ≤ 4. Extend the search of Remark 3.5 to allow the order 1, then prove the statement or state it as a precise open problem. Make the abstract's comparison class explicit. |
| m1 | Replace the birational argument with the projective-linear observation (determinant 43200; C∘ψ = −10800·E). |
| m2 | Isolate the fact "gap_2(S) ≤ 0 implies S ≥ 18" before Lemma 5.3, or reorder. |
| m3 | Correct the wording on the maximum of stratum 2. |
| m4 | State the precise hypothesis of the injectivity of torsion reduction; note that the orders follow from the group structure. |
| m5 | Describe the Cremona involution on C_Λ. |
| m6 | Prove the non-isometry of the family members, or label it numerical in Section 4. |
| m7 | State that the Bolza surface covers O(2,8,8) and use it as a benchmark. |
| m8 | Make "earlier" precise (sum and area). |
| m9 | Rename the column of Table S2. |
| P1–P4 | Editorial changes as described. |

---

My verification scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/A-d-teichmuller-orbifold-moduli/scratch/code/`:
- `strata.py` checks Section 5, Tables S2 and S3, and the gap values.
- `ec.py` checks the elliptic curve maps and torsion.
- `geo.py` computes the triangle-group geodesic lengths.
- `heat.py` checks the coefficients and the amplification constants.
- `cfree.py` checks the collision-free sums up to 600.
- `search4.py` and `search_tri.py` are the searches behind M1.
