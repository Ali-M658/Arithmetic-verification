<!-- Verbatim final message of the independent reviewer subagent (its own write was refused by the harness); saved by the main session from the report's first heading on. -->
# Referee report: "Triples with equal sum and equal reciprocal sum" (submitted to Integers)

Writing REPORT.md was refused, so the complete report is given here.

Referee's coverage: Sections 2 and 3 in full, and every statement elsewhere about elliptic curves, rational points, ranks, torsion, isogenies and models (Sections 1.3–1.4, Section 4 where it uses Λ, Section 5, Table 1, the end of Section 6.1, Section 6.4). I did not referee the analytic counting in Theorems 3–4, Proposition 5, or the statistics of Section 6, except where they make claims about the curves.

## Summary

Two triples with the same sum have the same reciprocal sum exactly when they have the same Λ = e1e2/e3. So a coincidence class is a finite set of positive rational points on one member C_Λ : (x+y+z)(xy+yz+zx) = Λxyz of the Bremner–Guy–Nowakowski (BGN) pencil, taken over rational Λ rather than integer Λ. Section 2 sets out the following:
- the pencil and its identification with Beauville's semistable surface (fibres I6, I3, I2, I1);
- a birational map from C_Λ to the Weierstrass model E_Λ : η² = s(s² + (Λ²−6Λ−3)s + 16Λ);
- the cyclic group of order 6 formed by the base points;
- the "egg" lemma: positive points lie on the non-identity real component, so odd multiples of a positive point are positive.

Section 3 proves that reciprocation (x:y:z) ↦ (yz:xz:xy) is translation by the 2-torsion point T2 = (0:0:1). This gives the "dual family" of coincidences (Corollary 1). The section also shows that isosceles points are torsion, and reports a computation that non-dual pairs with S ≤ 600 differ by non-torsion points.

Section 5 uses Schinzel's argument on C_{155/12}, with P = (4:9:18) of infinite order, to get classes of every size. It states Mordell–Weil ranks for the curves that carry the first classes of sizes 3–6 (Table 1). These are said to be certified by PARI's `ellrank` and by a 2-isogeny descent that is not documented.

**Verdict on my part:** the elliptic-curve mathematics is essentially correct, and I could reproduce every number I tested. The problems are these:
- a false sentence in Remark 2;
- an incomplete torsion statement in Remark 1, which misses the Z/12 case that the paper's own data contains;
- the rank of the k = 2 curve is handed off to an unavailable companion paper, although it is a two-line fact;
- the claimed "independent 2-isogeny descents" are not documented;
- several small gaps in proofs.

The elliptic-curve content is also mostly known (BGN 1993; Beauville 1982; Nguyen Xuan Tho 2021). The authors say so honestly.

## Significance

The arithmetic-geometry input is classical. The pencil, the model E_n, the egg, the Z/6 torsion and the reciprocal-pairs phenomenon are all in BGN [3]. The semistable surface is in Beauville [1]. The move from integer to rational Λ changes nothing structurally, because every statement holds over Q(Λ). Proposition 4 recasts BGN's "reciprocal = translate by (0,0)" in the plane model; this is useful but not new. The paper's own contribution lies in the counting results (Theorems 1–4, Proposition 1) and the enumeration, which are outside my coverage.

From the elliptic-curve side, the main observation is something the paper says only implicitly. **Every proved lower bound (Theorems 3 and 4) comes from a single rational surface: the graph of translation by the torsion point T2 inside the fibre square of the rational elliptic surface.** Mordell–Weil rank plays no part in the counting; it enters only the qualitative Theorem 5. The paper is honest that its bounds and its conjecture are far apart. A Mordell–Weil-flavoured result would make the elliptic-curve sections pull their weight. Examples:
- How often coincidences lie on rank ≥ 2 fibres.
- Whether non-dual classes are explained by small linear relations in E_Λ(Q). The authors tested only m ∈ {2, 3}.
- The root-number distribution over the Λ that carry classes.

Without such a result, Sections 2–3 are a competent exposition. For an elementary journal such as Integers that may be acceptable, but it should be presented as exposition.

## Correctness and what was recomputed

All computations were done independently in a Python virtual environment with cypari2 (PARI/GP 2.17.2) and sympy. I also used my own exact-rational chord-and-tangent code on the plane cubic, and LMFDB API queries. Results:

1. **Proposition 3, model and maps.**
   - I checked symbolically that (Λ²−6Λ−3)² − 64Λ = (Λ−1)³(Λ−9), and that Δ(E_Λ) = 2¹² Λ² (Λ−1)³ (Λ−9).
   - I also checked c4 = 16(Λ−3)(Λ³−9Λ²+3Λ−3), with c4(0) = 144, c4(1) = 256 and c4(9) = 2304, all nonzero.
   - deg c4 = 4 and deg Δ = 6, so the fibre at ∞ is I6 and the configuration is I6, I3, I2, I1 with Euler number 12. **Agrees.**
   - The forward map C_Λ → E_Λ lands on E_Λ, checked as a remainder modulo the curve equation F. The inverse map lands on C_Λ, and both compositions are the identity modulo the curve equations. **Agrees.**
   - Example: at Λ = 27/2, (1:4:4) ↦ (−6, 45), which lies on E_{27/2}. **Agrees.**
   - Nguyen Xuan Tho [11], which I fetched, uses the identical model v² = u(u² + (n²−6n−3)u + 16n). This supports the attribution to BGN's model (6).
   - I could not download BGN itself (paywalled), so I have not checked the page numbers or the two quotations from [3].
2. **Base-point torsion.** With O = (1:−1:0), I computed exactly at Λ = 27/2, 155/12, 68/5, 7/3, −5/2 and 11.
   - The multiples of g = (1:0:0) are g, 2g = (1:0:−1), 3g = (0:0:1), 4g = (0:1:−1), 5g = (0:1:0) and 6g = O.
   - The stated orders 2, 3, 3, 6, 6 and the cyclic structure **agree**.
3. **Lemma 1 (egg).** The argument is correct. Numerically, for P = (4:9:18) on C_{155/12}, nP is positive exactly for odd n ≤ 7.
4. **Proposition 4.** P + T2 = ι(P) was checked on five points of C_{155/12}. The actions of the permutations were also checked, and **agree**:
   - swapping x and y gives −P;
   - swapping x and z gives (0:1:−1) − P;
   - swapping y and z gives (1:0:−1) − P;
   - cyclic shifts are translations by the points of order 3.
5. **Corollary 1.** The identities and the example {(2,8,8),(3,3,12)} **agree**.
6. **Remark 1.** The identity and the isosceles formulas Λ−1 = 2(u+v)²/(uv) and Λ−9 = 2(u−v)²/(uv) **agree**. The torsion statement is incomplete; see M1.
7. **Remark 2.** Recount: there are 40 305 primitive positive triples other than (1,1,1) with sum ≤ 120. **Agrees.**
   - Each was tested with `ellorder` on E_Λ. 2212 are torsion: 1460 of order 2, 731 of order 6 and 21 of order 12.
   - All of them are isosceles or geometric progressions. **Agrees.**
   - However, the order-2 points falsify a sentence of the remark (M2), and the order-12 points are exactly the geometric progressions (M1).
8. **Section 3, paragraph after Corollary 1.** I re-enumerated all admissible triples with S ≤ 600. Results, all of which **agree**:
   - N(600) = 3067, matching Table 2.
   - There are 1753 primitive pairs, of which 423 are dual pairs.
   - For each of the other 1330, both P′−P and P′+P have infinite order (`ellorder` = 0).
   - End of Section 6.1: of the 669 non-dual primitive pairs with S ≤ 400, none satisfies P′ = ±mP + T or P = ±mP′ + T with m ∈ {2, 3} and T torsion.
9. **Theorem 5.**
   - P = (4:9:18) lies on C_{155/12}.
   - nP ≠ O for n ≤ 12, so P has infinite order.
   - 3P = (162833463 : 723926268 : 287876366) exactly.
   - 2P = (16352 : 288 : −365) is not positive.
   - **Agrees.**
10. **Ranks, torsion and conductors (minimal models of E_Λ).**

| Λ | minimal model [a1,a2,a3,a4,a6] | conductor | torsion | root no. | `ellrank` [r1,r2] | analytic rank (numerical) | LMFDB |
|---|---|---|---|---|---|---|---|
| 27/2 | [1,−1,1,−3002,63929] | 90 = 2·3²·5 | Z/2×Z/6 | +1 | [0,0] | 0 | 90.c3, rank 0 |
| 155/12 | [1,0,0,−2952566,1946655396] | 6250530 = 2·3·5·11·13·31·47 | Z/6 | +1 | [2,2] | 2 | not in the database |
| 68/5 | [1,0,1,−122648,16493078] | 82110 = 2·3·5·7·17·23 | Z/6 | +1 | [2,2] | 2 | 82110.ba4, rank 2 |
| 1849/120 | [1,0,0,−83872601980,9344251075024400] | 1715185290 | Z/6 | −1 | [3,3] | 3 | not in the database |
| 230/21 | [1,0,1,−8507979,9343104706] | 41388270 | Z/6 | −1 | [3,3] | 3 | not in the database |

   - `ellrank` gives r1 = r2 on every curve in each isogeny class: four curves each for the rank-2 and rank-3 cases, and eight for Λ = 27/2. Each run is a separate 2-descent, which gives a partly independent check.
   - For C_{155/12}, generators on the minimal model, saturated at all primes ≤ 100, are (−1394, 58612) and (−1940, −18374), with regulator ≈ 2.3082.
   - Every member listed in Table 1 lies on its curve, with the stated S and Λ.
   - Re-enumeration to S ≤ 600 confirms that the first classes of sizes 2, 3 and 4 occur at S = 18, 136 and 408, with exactly the listed members.
   - **All rank and torsion entries agree.** The ranks are established by PARI's unconditional 2-Selmer upper bound together with explicit independent points. The paper states this honestly, and it is a proof modulo the correctness of the software.
   - The additional "independent 2-isogeny descent" is asserted but not documented (M4).
11. **Literature claims I could check.**
    - Nguyen Xuan Tho [11, Theorem 1.1] (no positive solutions when 4 | n; Hilbert-symbol method on E_n): **correct**.
    - Sadek–El-Sissi [13]: Proposition 2.5 (isosceles triples give points of order 6) is **correctly cited**.
    - Sadek–El-Sissi [13]: Theorem 2.8 (torsion Z/3, Z/6 or Z/2×Z/6 according to #S(M,N) = 0, 1, 2, under the hypotheses of Proposition 2.7) is **correctly cited**.
    - The "infinite order under a mild condition" statement, however, is [13, Proposition 2.7] (see m7).
    - I could not access Beauville [1], Schoen [15] or the exact numbering in Mazur [10].

No FATAL issue was found in my coverage.

## FATAL

None in my coverage. Proposition 2, Proposition 3, Lemma 1, Proposition 4, Corollary 1 and Theorem 5 are correct as mathematics, up to the minor gaps below.

## MAJOR

**M1 (p. 6, Remark 1; p. 7, Remark 2; p. 4, Section 1.4, "Remark 2 is the analogue here").** The torsion description is incomplete. The paper's own data contradicts the impression it gives.

- Remark 1 says only that "for rational Λ there is more", namely Z/2×Z/6. But the torsion subgroup of C_Λ(Q) can also be **Z/12**.
- This happens exactly for Λ = ((r²+r+1)/r)², that is, when C_Λ carries a geometric-progression point (1 : r : r²). I verified it with `elltors` for r = 2, 3, 3/2, 5/3, −2 and −1/3.
- Exact chord-and-tangent arithmetic shows that (1,2,4), (1,3,9), (4,6,9), (1,4,16) and (9,12,16) are points of **order 12**.
- A survey of the 447 smooth Λ = a/b with |a| ≤ 30 and b ≤ 12 found torsion Z/6 for 434 values, Z/2×Z/6 for 13, and Z/12 for one (Λ = 9/4, from r = −2).
- Remark 2's sentence "every one that is a torsion point of its curve is isosceles or a geometric progression" already points this way. But nowhere does the paper say that geometric progressions are torsion, or of which order.
- Remark 2's claim that "on the equal-sum, equal-product curves the same holds" is therefore misleading:
  - In that family the possible torsion groups are Z/3, Z/6 and Z/2×Z/6, and distinct-entry triples are non-torsion under Sadek–El-Sissi's condition.
  - Here, positive distinct-entry torsion points exist (geometric progressions, of order 12), and Z/12 occurs.

A complete statement with a short proof is available. It would turn the numerical check up to S ≤ 120 into a theorem:
- (a) Mazur's theorem and the Z/6 base group leave only Z/6, Z/12 or Z/2×Z/6.
- (b) The 2-torsion points other than T2 are the fixed points (1:1:t) of the swap of x and y, with 2t² + (5−Λ)t + 2 = 0. Its discriminant is (Λ−1)(Λ−9).
  - So full 2-torsion holds if and only if C_Λ has a rational isosceles point. This is an equivalence, not merely "contains".
  - For Λ ≥ 9 such a point is positive.
- (c) For a point Q, 2Q equals an order-6 base point if and only if the geometric-progression condition holds for Q or for −Q. That condition says ι(Q) is the image of Q under the swap of x and z. So Z/12 holds if and only if C_Λ has a rational geometric-progression point.
- (d) By Lemma 1, a positive torsion point has even order, so it lies outside the base group. The orbit description of Section 3 then shows it is a permutation or dual of an isosceles or geometric-progression triple.

Together these give two results:
- A positive point is torsion if and only if it is isosceles or a geometric progression.
- The torsion group is Z/6, Z/12 or Z/2×Z/6 according as C_Λ has no such point, a geometric-progression point, or an isosceles point.

This is the true analogue of Sadek–El-Sissi's Theorem 2.8.

**M2 (p. 7, Remark 2, third sentence).** "A positive isosceles point therefore has order 6" is **false**.
- The argument covers only the orientations (u:v:v) and (u:v:u).
- A point (v:v:u) is fixed by the swap of x and y, which acts as P ↦ −P, so it has **order 2**.
- Example: on C_{27/2}, (1:1:4) has order 2 while (1:4:4) has order 6. Figure 1(a) and the smallest pair itself contain this case, since (3,3,12) corresponds to (1:1:4).
- My recount up to S ≤ 120 found 1460 positive isosceles points of order 2.
- The conclusion that isosceles coincidences are a torsion phenomenon survives, but the sentence must be corrected. Each isosceles triple gives two orientations of order 6 and one of order 2.

**M3 (p. 11, Table 1 row k = 2; p. 2, Section 1.1).** The rank cell for C_{27/2} reads "[8]". The "isolation" of the smallest coincidence is also deferred to the companion manuscript [8, Theorem 5.8], which the reader cannot see. Both are immediate in this note's own framework:
- E_{27/2} is LMFDB 90.c3, with rank 0 and torsion Z/2×Z/6.
- The rank is provably 0. `ellrank` gives r2 = 0 unconditionally. The analytic rank is 0, which also proves it via Kolyvagin.
- Hence C_{27/2}(Q) has exactly 12 points: the six base points and the six orderings of (1,4,4) and (1,1,4).
- So no triple other than these has Λ = 27/2. The class {(2,8,8),(3,3,12)} and its scalings are the only coincidences on that curve.

A referee cannot accept a table entry, within the paper's declared subject, whose content is only a pointer to an unavailable preprint. State the rank as 0 with this one-paragraph proof. Cite [8] for the spectral consequences only.

**M4 (pp. 10–11, Section 5; Table 1 caption).** The paper makes two unsupported assertions: that "an independent 2-isogeny descent, whose Selmer groups are filled by the images of explicit points, gives the same rank", and that "the descents above confirm each rank independently of PARI". No data is given:
- no Selmer groups Sel^φ(E) and Sel^φ̂(E′), and no dimensions;
- no explicit points filling them;
- no Mordell–Weil generators.

As written, the claim cannot be checked from the paper. For each of the five curves, either give a compact table or delete the claim and rely on `ellrank`. Such a table would contain:
- the minimal model and conductor;
- the dimensions of the φ- and φ̂-Selmer groups and of the image of torsion;
- generators in plane coordinates, for example (4:9:18) and a second point on C_{155/12};
- the regulator.

The `ellrank` claim is honest and adequate; I reproduced it on every curve in each isogeny class. I recommend stating it explicitly: "the rank is r1 = r2 by PARI 2.17.2 `ellrank`, which computes the 2-Selmer rank and the 2-part of the Cassels pairing unconditionally and exhibits r1 independent points". Two further points should be added:
- The lower bound depends on the independence of the exhibited points. This is certified by a nonzero regulator, which PARI computes in floating point, so say so.
- The analytic ranks I computed (2, 2, 3, 3) agree with the root numbers (+1, +1, −1, −1). The paper never mentions this consistency check, and it costs one line.

## MINOR

- **m1 (p. 6, Proposition 4).** ι(x:y:z) = (yz:xz:xy) is undefined at the three coordinate vertices, which are base points on C_Λ.
  - "P + T2 = ι(P) for every point P" should read "ι extends to an automorphism of C_Λ, and it equals translation by T2". For example, the extension sends (1:0:0) to (0:1:−1).
  - The proof has a gap. It shows that ι(P) lies on C_Λ, but the conclusion requires O, R = (p0p2 : p1p2 : p0p1) and ι(P) to be collinear. They are, because R and ι(P) differ by swapping the first two coordinates, so R − ι(P) is proportional to (1, −1, 0). Add this sentence.
  - The proof also needs a word on the degenerate cases P = T2, and lines tangent at P or at R.
- **m2 (p. 5, Proposition 3).** "The six base points of the pencil are torsion points: ..." lists five points and then adds "together with O". O = (1:−1:0) is itself one of the six base points; rephrase.
  - On p. 14, "blowing up the nine base points" conflicts with "six base points" on p. 5.
  - There are six distinct base points. (1:0:0), (0:1:0) and (0:0:1) have intersection multiplicity 2, giving nine once infinitely near points are counted. Say so.
- **m3 (p. 5, Proposition 3 proof).** "The orders of the base points follow from the chord-and-tangent law, computed exactly" is an appeal to computation where a two-line geometric argument is available. The lines z = 0, x + y = 0 and so on each meet C_Λ only in base points, which gives the relations directly. Also give the tangent-line facts used.
- **m4 (p. 5, Lemma 1 proof).** The argument shows that the positive locus is a union of components not containing O. Hence it is either empty or the non-identity component.
  - The lemma asserts that it "form[s] one connected component", which needs nonemptiness for every Λ > 9. This is easy: (1:1:t) with 2t² + (5−Λ)t + 2 = 0 has two positive real roots when Λ > 9. Add the sentence.
  - The word "rational" in "Let Λ > 9 be rational" is irrelevant to the real-topology statement.
- **m5 (p. 4, Proposition 2).** "Then the triples (L/si)xi lie in one primitive class at sum L" is stated before admissibility. A class is defined only for admissible triples (p. 2), so the claim holds only when L > Λ. Move the admissibility clause, or say "in one primitive class once L > Λ".
- **m6 (p. 3 and p. 5, "row Γ_0^0(6) of Beauville's table").** The configuration I6, I3, I2, I1 is that of Γ1(6): cusp widths 6, 3, 2, 1 and index 12 in PSL2(Z).
  - Its image in PSL2(Z) is Γ0(6), and the generic Mordell–Weil torsion is Z/6.
  - In standard notation, Γ_0^0(6) = Γ0(6) ∩ Γ^0(6) is conjugate to Γ0(36), which has index 72 in PSL2(Z).
  - If this symbol is Beauville's own notation, say so; otherwise use Γ1(6). I could not access [1] to check.
- **m7 (pp. 3–4, Section 1.4).** "Triples with distinct entries give points of infinite order under a mild condition [13, Proposition 2.5 and Theorem 2.8]" mixes up the references. The infinite-order statement is [13, Proposition 2.7]; Proposition 2.5 is the isosceles order-6 statement. Make the references precise.
  - Also verify the locator "[10, Chapter III, Corollary (5.2), p. 156]" for Mazur's torsion theorem. It is usually cited as Theorem 8 of the introduction; I could not check the internal numbering.
- **m8 (p. 14, Section 6.4).** "Conjecture 1 is a statement about the positive rational points of bounded height on this threefold" needs sharpening.
  - No height is specified, and for a Calabi–Yau threefold there is no Manin-type prediction to compare with.
  - The text should note that the 12 "trivial" surfaces {(P, ±P + T)} are graphs of automorphisms.
  - Pairs that are permutations of one another are excluded, but the graph of translation by T2 (the dual family) is retained. That graph is therefore one of these accumulating surfaces, and all of Theorems 3–4 live on it.
  - The self-fibre product of a Beauville surface is, by Schoen's work, a rigid Calabi–Yau threefold after small resolution. I believe it is also known to be modular. This deserves a sentence, with a correct locator in [15].
- **m9 (p. 6, Remark 1).** "This happens on an infinite family that contains every curve through an isosceles point" understates the situation. By M1(b), the family is exactly the set of curves with a rational isosceles point (1:1:t), t ∈ Q*. For Λ ≥ 9 the point is positive. State the equivalence.
- **m10 (p. 7).** "For a point P of infinite order, the orbit ... is {±P + T}, twelve points: the triple x, its dual, and their permutations." Say "six orderings each of x and of its dual". As written it can be read as twelve unordered triples.
- **m11 (p. 10, Section 5).** "Classes generated by one point are far out: ... the next positive point is 3P". With rank 2, "next" is ambiguous, because other positive points P + Q′ + T exist. Say "the next positive multiple of P".

## Presentation

- **P1.** Section 3 should state the main structural fact once and prominently. A class is a finite set of positive points of C_Λ(Q), and the "trivial" coincidences (dual pairs) are exactly the pairs {P, ±P + T2 + T3} with T3 in the 3-torsion. The current text spreads this over Proposition 4, Corollary 1, an unnumbered paragraph and Remark 2.
- **P2.** Give, in Section 2, the explicit correspondence between the plane points and the Weierstrass points for the base points and T2, for example T2 ↦ (0,0). The dictionary is then checkable without software.
- **P3.** Table 1 needs three changes:
  - add the minimal model or an LMFDB label (90.c3 and 82110.ba4 exist), the conductor and the torsion for each Λ;
  - replace "[8]" with "0";
  - move the caption sentence "in every row with k ≥ 3 the bounds r1 = r2 of `ellrank` coincide" into the text.
- **P4.** "Rational Λ" is emphasised repeatedly (abstract, Section 1.3, before Lemma 1) as if it were a substantive extension of BGN. All the structure is over Q(Λ), so a single sentence suffices.
- **P5.** Typography: "withsum" in Section 1.2 on p. 2 is a missing space. I saw it in the extracted text, not on a rendered page, so check the source.

## Recommendation

**Major revision**, at least for the elliptic-curve parts. Confidence: high for the elliptic-curve parts I recomputed; moderate for the paper overall, since I did not referee the analytic counting.

The elliptic-curve mathematics is sound, and every number I recomputed agrees. That covers counts, torsion orders, points, ranks and the enumeration up to S = 600. The required changes are:
- one false statement (M2);
- an incomplete torsion classification, which is easily completed and would strengthen the paper (M1);
- a rank fact deferred to an unavailable companion paper (M3);
- an undocumented verification claim (M4).

Separately, the editor should know that the elliptic-curve sections are largely a re-presentation of BGN and Beauville. Any case for publication rests on the counting results, which other referees must assess.

## What resolves each issue

- **M1:** Replace Remark 1 with a theorem, proved by the four-step argument sketched in M1, and correct the comparison with [13]. The theorem should state:
  - The torsion group is Z/6, Z/12 or Z/2×Z/6.
  - It is Z/2×Z/6 if and only if there is a rational point (1:1:t), equivalently (Λ−1)(Λ−9) is a square.
  - It is Z/12 if and only if there is a geometric-progression point, equivalently Λ = ((r²+r+1)/r)².
  - A positive point is torsion if and only if it is isosceles (order 2 or 6) or a geometric progression (order 12).
- **M2:** Replace the sentence with "an isosceles triple gives points of order 6 in the orientations (u:v:v) and (v:u:v), and of order 2 in the orientation (v:v:u)". Add the one-line reason that the swap of x and y acts as P ↦ −P.
- **M3:** Put "0" in Table 1 and add the proof:
  - LMFDB 90.c3 and `ellrank` r2 = 0 give C_{27/2}(Q) ≅ Z/2×Z/6;
  - list its 12 points;
  - conclude, in this note, that no other triple has Λ = 27/2.
- **M4:** Add a table of Selmer dimensions and generators for the five curves, or delete the "independent 2-isogeny descent" claim. State precisely what `ellrank` proves. Optionally mention the root-number and analytic-rank consistency.
- **m1:** State the extension of ι to C_Λ, add the collinearity sentence, and handle the degenerate cases.
- **m2:** Count O among the six base points, and reconcile "six" with "nine" by mentioning multiplicity.
- **m3:** Give the geometric derivation of the base-point orders.
- **m4:** Add the nonemptiness sentence using the positive roots t, and drop "rational".
- **m5:** Move the admissibility condition L > Λ before the class claim in Proposition 2.
- **m6:** Use Γ1(6), or justify Γ_0^0(6) as Beauville's own notation.
- **m7:** Cite [13, Proposition 2.7] for infinite order and [13, Proposition 2.5] for order 6, and check the Mazur locator.
- **m8:** Specify the height, identify the accumulating graph surfaces, and mention rigidity with a correct locator in [15].
- **m9:** State the equivalence in Remark 1.
- **m10, m11:** Make the two wording fixes.
- **P1–P5:** Restructure Section 3 as described, add the dictionary and labels, and fix the typography.
