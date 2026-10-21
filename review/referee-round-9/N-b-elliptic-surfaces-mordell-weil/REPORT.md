<!-- Round 9 N-b referee report: returned text saved verbatim; the reviewer could not write files -->

I could not save the report to /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/N-b-elliptic-surfaces-mordell-weil/REPORT.md because the write was refused. The full report follows.

# Referee report: "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

**Referee N-b** (arithmetic geometry: elliptic surfaces, Mordell–Weil lattices, torsion in families).

**Assignment.** Sections 2, 3 and 5 (pp. 6–12 and 16–17): the curves C_Λ, their Weierstrass models, the elliptic surface, torsion, reciprocation, permutations and torsion translations, the rank and descent statements, and arbitrarily large classes. I also checked the statements in Sections 1.3–1.4 that summarise these sections: Theorem A, Theorem C, and the Tate normal form on p. 3.

**Conventions.** Placeholders (author contributions, AI-use statement, Zenodo DOI, preprint identifier) are treated as known. I read the rendered pages 3, 6–12 and 16–17 before making any presentation comment.

## Summary

**Section 2.** A class of coincidences (S, R) is identified with a finite set of positive rational points on the plane cubic C_Λ : e1·e2 = Λ·e3, where Λ = SR. The section then does the following.
- It identifies C_Λ as the member t = 1 − Λ of Beauville's pencil (X+Y)(Y+Z)(Z+X) + tXYZ = 0, which is the pencil for Γ0(6) = ±Γ1(6).
- It gives an explicit isomorphism over Q with E_Λ : η² = s(s² + (Λ² − 6Λ − 3)s + 16Λ).
- It gives a change of variables to Tate's normal form for a point of order 6, with c = −1/Λ.
- It locates the singular fibres: I6, I3, I2, I1 at Λ = ∞, 1, 0, 9.
- It shows that the six base points form a cyclic group of order 6.
- It proves that for Λ > 9 the positive locus is the non-identity real component ("the egg"). Consequently, odd multiples of a positive point are positive.

**Section 3.** This section proves the following.
- Reciprocation is translation by the 2-torsion point T2.
- A transposition acts as P ↦ π(O) − P. A cyclic permutation is translation by a point of order 3.
- Theorem 1:
  - the torsion is Z/6, Z/12 or Z/2×Z/6;
  - it is Z/2×Z/6 exactly when (Λ−1)(Λ−9) is a square;
  - it is Z/12 exactly when Λ = (r + 1 + 1/r)²;
  - for Λ > 9, the positive torsion points are the isosceles triples and the geometric progressions, with stated orders.
- Lemma 4 says which torsion translations preserve positivity.
- Remark 1 shows there are no linear families other than scaling.

**Section 5.** Theorem C (arbitrarily large primitive classes) is proved by Schinzel's argument, using the point (4 : 9 : 18) on C_{155/12}. The section also reports ranks, root numbers, conductors and a 2-isogeny descent (Table 1) for the curves that carry the first class of each size (Table 2).

## Significance

The mathematics in my sections is correct and clearly attributed. The authors say themselves that the geometry of Sections 2–3 "is largely in [3], [1] and [20]". What is new here:

- **Theorem 1(iv) and Lemma 4.** These are short, correct consequences of the egg lemma combined with Kubert's classification. They are useful for sorting the pairs in Section 6.1, but they are not deep.
- **The explicit dictionary.** It runs from the Bremner–Guy–Nowakowski (BGN) plane model to Beauville and Tate, and writes permutations and reciprocation as P ↦ ±P + T. It is tidy and checks out exactly.
- **Theorem C.** The authors concede that it is Schinzel's argument applied to a different cubic. It is close to immediate from what BGN already observed; see M1.

For my sections: correct, well referenced, and modest. On their own, Sections 2, 3 and 5 would not carry a paper. The verdict on the note as a whole rests on Sections 4 and 6.

## Correctness, and what I recomputed

Tools: sympy 1.14 and PARI/GP 2.17.2 (through cypari2) in a venv in scratch, plus my own code for local solubility and enumeration. The scripts are in scratch/code/.

### Section 2

- **Lemma 1 (p. 6).** Checked line by line.
  - Discriminant 3(c′+3)(1−c′): correct.
  - Discriminant (c′+4)(24 − 22c′ − c′²)/(6 − c′): correct, and negative for 3 ≤ c′ ≤ 5.
  - R = 6/5 and R = 13/12: correct.
- **Proposition 1.** Correct, including the primitivity argument and L | S.
- **Proposition 2 (p. 7).** All checked symbolically in sympy:
  - the identity (x+y)(y+z)(z+x) = e1e2 − e3;
  - the forward map lands on E_Λ, the inverse lands on C_Λ, and both compositions are the identity on C_Λ;
  - Δ = 2^12 Λ² (Λ−1)³ (Λ−9);
  - c4 = 16(Λ−3)(Λ³ − 9Λ² + 3Λ − 3), which equals 144, 256 and 2304 at Λ = 0, 1, 9. So those fibres are multiplicative, of types I2, I3, I1;
  - at Λ = ∞ the model is as stated, with ord Δ = 6, giving I6. Euler numbers 6 + 3 + 2 + 1 = 12, as they must be.
  - The fibre configuration agrees with Top–Yui [30] (I fetched arXiv:math/0307230): Example 1.2 and Table 2 give I6, I3, I2, I1 over t = ∞, 0, 1, −8, i.e. Λ = ∞, 1, 0, 9.
  - The point (1 : 4 : 4) on C_{27/2} maps to (−6, 45): correct.
- **Tate normal form (p. 3).** The map x = (c²/4)s + c, y = (c³/8)η + (c²(c−1)/8)s + c² with c = −1/Λ carries E_Λ onto y² + (1−c)xy − (c+c²)y = x³ − (c+c²)x². This holds identically. The point (0 : 1 : 0), where η = −4Λ(Λ−1), maps to (0, 0): correct.
- **Base points and group law (pp. 7–8).**
  - The tangent at O, the flex, the five line sections, and the relations (0:1:0) = −A, (1:0:−1) = −Q, A = T2 + Q, 2A = −Q, 2T2 = O are all correct.
  - PARI orders on C_{155/12}: 2, 3, 3, 6, 6.
  - Intersection multiplicities 2, 2, 2, 1, 1, 1 (nine in total): correct.
- **Lemma 2 (the egg).** Correct.

### Section 3

- **Proposition 3 and Lemma 3.** Proofs checked by hand. Numerically, I took about 150 random positive triples with distinct entries and worked on the corresponding curve each time. In every case:
  - ι(P) = P + T2;
  - each transposition acts as π(O) − P, with the stated π(O);
  - each cyclic permutation is translation by (0:1:−1) or by (1:0:−1).

  There were no failures.
- **Theorem 1(i).** Correct. I checked the Mazur citation in the Numdam PDF: Chapter III, §5, Theorem (5.1) is on p. 156, and the Kubert table is mentioned on that same page. Both citations are accurate.
- **Theorem 1(ii).** Kubert's Z/2×Z/6 parameter c = (10 − 2τ)/(τ² − 9) gives (Λ−1)(Λ−9) = (τ−9)²(τ−1)²/(4(τ−5)²), a square, as it should. PARI gives torsion [6, 2] for (3,5,5) at Λ = 143/15 and for (1,1,4) at Λ = 27/2.
- **Theorem 1(iii).** For r ∈ {2, 3, 2/3, −4, −5, −3/2}, PARI gives the orders 12, 4, 12, 12, 4, 12 for the six orderings of (1, r, r²). Order 4 occurs exactly when the middle term is last. 2G = (1 : 0 : 0) on C_{49/4}.
- **Theorem 1(iv), with the orders.** Verified.
- **Integer Λ > 9.** Only Λ = 10 has extra torsion: correct. For the 2-torsion case, t ∈ {±1, ±2, ±1/2}; for the order-12 case, r = ±1.
- **Lemma 4.** Correct.
- **C_{169/16}.**
  - PARI gives rank 1 (bounds [1, 1]), torsion Z/12 and conductor 6630.
  - The four pairs on p. 18 have equal sums and Λ = 169/16.
  - In each pair, exactly three orderings of the second triple differ from the first by a torsion point, of orders 4, 12 and 12.
- **Remark 1.** Correct.

### Section 5

- **Theorem 4.**
  - P = (4 : 9 : 18) on C_{155/12} has infinite order (canonical height 1.4534).
  - 3P = (162833463 : 723926268 : 287876366) and P + T2 = (9 : 4 : 2), exactly as printed.
  - The proof is correct.
- **Ranks, root numbers, conductors, torsion.** Computed on y² = x(x² + ax + b) with a = p² − 6pq − 3q², b = 16pq³.

  | Λ | conductor | root number | rank | torsion |
  |---|---|---|---|---|
  | 27/2 | 90 | +1 | 0 | Z/2×Z/6 |
  | 155/12 | 6250530 | +1 | 2 | Z/6 |
  | 68/5 | 82110 | +1 | 2 | Z/6 |
  | 1849/120 | 1715185290 | −1 | 3 | Z/6 |
  | 230/21 | 41388270 | −1 | 3 | Z/6 |

  - Every printed value agrees, and so do the a and b columns of Table 1.
  - C_{27/2} has reduction I6 at 2, I2* at 3 (additive) and I6 at 5. The other curves are semistable.
- **Table 1 (Selmer groups).** I recomputed both Selmer groups for all five curves independently. I wrote a p-adic local-solubility test for N² = dM⁴ + aM²e² + (b/d)e⁴, and for the isogenous curve (a′ = −2a, b′ = a² − 4b), at every p dividing 2b(a² − 4b) and at ∞.
  - Every entry of Table 1 is reproduced exactly. For example, Λ = 155/12 gives {1, 3, −10, −30, −62, 155, −186, 465} and {1, 6721}.
  - The images of torsion together with ellrank's points fill the Selmer groups. So Ш[φ] = Ш[φ̂] = 0 and the ranks are 0, 2, 2, 3, 3, as claimed.
  - a² − 4b = q⁸(Λ−1)³(Λ−9), consistent with 6721, 1449, 1329601 and 8569.
- **Table 2.** I enumerated all admissible triples at S = 18, 136, 408, 1849 and 4600. Each printed class is complete and is the largest class at its sum; the numbers of classes at these sums are 1, 5, 12, 8 and 57. The Λ values match. The class at S = 408 is 3 × (the class at 136) together with (65, 70, 273). I did not check the claim "first class of each size"; that needs the full enumeration in Section 6.
- **Not verified.** Bremner–Guy–Nowakowski [3] is behind an AMS bot wall, so the page-specific quotations and attributions from it are unchecked. I also could not see Beauville's table itself.

## FATAL

None. I found no mathematical error in Sections 2, 3 or 5. Every number I could recompute is correct.

## MAJOR

**M1 (pp. 3–4, 16; Theorem C / Theorem 4). Theorem C is presented as a headline result but is essentially a corollary of BGN plus Schinzel.**
- BGN [3, p. 119] already state that the odd multiples of a point on the egg are positive.
- Proposition 1 shows that any k positive primitive points on one C_Λ give a class after rescaling.
- So Theorem 4 follows at once for any C_n with n > 9 and positive rank, including integer n. The "new input" claimed on p. 16 is already in [3].

The authors should either:
- (a) demote it to a corollary or remark, and remove it from the abstract's list of results; or
- (b) give it content. Options:
  - a quantitative version: on a fixed curve of rank ρ the least sum of a class of size k grows like exp(c·k^{1+2/ρ}), since the sums of nP grow like exp(ĥ(P)n²); compare with Table 2;
  - classes with no dual or torsion relations among their members;
  - infinitely many Λ carrying classes of size ≥ k.

**M2 (pp. 7, 22). The elliptic-surface framing omits the key Mordell–Weil fact.**
- The surface is Beauville's semistable extremal surface. Shioda–Tate gives 10 = 2 + rank + (5 + 2 + 1 + 0), so MW(E/Q̄(Λ)) = Z/6, of rank 0, and the Mordell–Weil lattice is trivial.
- This explains why there is no family of non-torsion positive points over the Λ-line itself.
- The torsion families of Theorem 1(ii) and (iii) are the modular covers:
  - X1(2,6) → X1(6), of degree 2, given by Λ = 2t + 5 + 2/t (this matches Theorem 2's Λ = 5 + 2(u/v + v/u));
  - X1(12) → X1(6), of degree 4 in r, given by Λ = (r + 1 + 1/r)².
- Any further family must come from a base change Λ = f(t) with positive Mordell–Weil rank. Examples are the quadratic base changes to K3 surfaces in Top–Yui §2.3. This would turn the vague search in Section 6.4 into a concrete one.
- Theorem 1(ii) should also be stated in the parametrised form Λ = 2t + 5 + 2/t.
- This is not an error. But without this paragraph, the "elliptic surface" language in the abstract and in Sections 1.3 and 6.4 is decorative.

## MINOR

- **m1 (p. 17, Table 1).** The text asserts that "images of explicit rational points fill" the Selmer groups, but prints no points and no local obstructions.
  - Give witness points for each curve; for example, (−11904, 154752) and (−9720, 463320) on the Λ = 155/12 model, together with torsion, fill the images.
  - Name one obstructing place for each excluded class.
  - Change the caption from "Selmer groups containing the images" to "Selmer groups, which equal the images".
- **m2 (p. 7, Proposition 2).** The fibre types are computed on the Weierstrass model but are asserted for "the rational elliptic surface obtained by blowing up the base points".
  - Add that the blow-up, which needs infinitely near points at T2, (1:0:0) and (0:1:0) because all members share a tangent there, is relatively minimal, so it is the Kodaira–Néron model.
  - Add that the I6 fibre consists of the three lines of xyz = 0 plus three exceptional curves.
  - "ord_{µ=0} c4 = 0" should read "c4 does not vanish at µ = 0".
- **m3 (p. 7).** The irreducibility argument is compressed. It should say:
  - the rational map E_Λ ⇢ C_Λ is non-constant;
  - so it gives a component of genus 1;
  - so C_Λ is irreducible and smooth.

  Also state that the maps are defined only when Λ(Λ − 1) ≠ 0.
- **m4 (p. 10, Theorem 1(iii)).** "2G = (0:1:−1) + T2" is just 2G = (1 : 0 : 0) = A. Say so, in the statement and in the converse.
- **m5 (p. 11, Lemma 4).** "The base points, together with all twelve torsion points" is clumsy, since the twelve include the base points. Suggested wording: "If the torsion is Z/12 with r < 0, no torsion point is positive; otherwise exactly the base points are non-positive." Also note that the sign of r is well defined, since r ↔ 1/r and so on.
- **m6 (p. 3 and p. 9, Corollary 1).** "Not a geometric progression" should be "no ordering is a geometric progression", or "b² ≠ ac with a ≤ b ≤ c". As written, (1, 4, 2) qualifies.
- **m7 (p. 11, proof of (iv)).** "Among them its dual, an ordering of (r², r, 1)" is circular, because (r², r, 1) is itself an ordering of (1, r, r²). Say instead that the dual (r² : r : 1) is again an ordering.
- **m8 (p. 16).** "The next positive multiple is 3P": but −P = (9 : 4 : 18) is also a positive multiple. Say "nP with n > 1".
- **m9 (p. 17).** "No class of size 7 up to S = 6000" is an enumeration fact; move it to Section 6.
- **m10 (p. 3).** Top–Yui's Table 2 lists Γ0(6); the identity Γ0(6) = ±Γ1(6) (index φ(6)/2 = 1) is the authors'. Write it as "Γ0(6) = ±Γ1(6) [30, Table 2]".
- **m11 (pp. 8, 10).** Double-check the page-specific BGN quotations against the published paper, since I could not access it: p. 117 (reciprocal pairs), p. 118 (model (6), the egg), p. 119 (odd multiples), and §4, p. 120 (the torsion sentence and the table recording reciprocals as translates by (0, 0)).

## Presentation

- **P1 (p. 6).** In Proposition 1, "Conversely" introduces a statement that is not a converse; use "Moreover".
- **P2 (p. 7).** State once, in Section 2, that O = (1 : −1 : 0) is not positive, since every positivity argument relies on it.
- **P3 (p. 9).** In Lemma 3, "translation by the base points" includes reciprocation (translation by T2). Say so in one clause.
- **P4 (pp. 10–11).** Put the orders from (iv) in a small table:
  - (v:v:u): order 2;
  - (u:v:v) and (v:u:v): order 6;
  - (1:r²:r) and (r²:1:r): order 4;
  - the other four orderings: order 12.
- **P5 (p. 17).** Factor the conductors:
  - 90 = 2·3²·5;
  - 6250530 = 2·3·5·11·13·31·47;
  - 82110 = 2·3·5·7·17·23;
  - 1715185290 = 2·3·5·7·13·19·43·769;
  - 41388270 = 2·3·5·7·11·19·23·41.

  Also note that the reduction of C_{27/2} at 3 is additive (I2*).
- **P6 (pp. 11, 18).** The torsion-type pairs differ by a point of order 4 for one ordering and order 12 for two. Saying so would be more precise than "4 or 12".

## Recommendation

For Sections 2, 3 and 5: **minor revision**.
- Confidence that they are correct: high. Every proof was checked and every number recomputed.
- Confidence that they are adequate as a contribution: moderate.

M1 and M2 concern how the results are positioned, not whether they are correct, and each can be fixed with a paragraph. If the editor weighs headline novelty heavily, M1 alone would push these sections toward major revision. The overall verdict should rest on the referees of Sections 4 and 6.

## What resolves each issue

- **M1:** demote Theorem C, crediting [3, p. 119] and [27], and revise the abstract and §1.3. Or add a quantitative or structural strengthening.
- **M2:** add a paragraph on extremality (MW = Z/6), the modular covers X1(2,6) and X1(12) with their parametrisations, and positive-rank base changes; point to it from §6.4.
- **m1:** print the witness points and the obstructing places; fix the caption.
- **m2, m3:** add the sentences on relative minimality, the Kodaira–Néron model and the domain of the maps.
- **m4–m9:** the rewordings indicated above.
- **m10, m11:** fix or check the citations.
- **P1–P6:** cosmetic changes as indicated.

Recomputation scripts are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/N-b-elliptic-surfaces-mordell-weil/scratch/code/:
- c1.py: symbolic checks of Proposition 2 and the Tate normal form;
- c2.py and c3.py: group law, torsion, ranks, conductors;
- descent.py: independent Selmer groups;
- c4.py: Table 2 classes;
- c5.py: Selmer images.
