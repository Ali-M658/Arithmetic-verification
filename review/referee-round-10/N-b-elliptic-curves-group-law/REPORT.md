<!-- Round 10, N-b, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

I couldn't save the report to `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/N-b-elliptic-curves-group-law/REPORT.md`: the write was refused (subagents may not write report files). The full report follows. My recomputation scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/N-b-elliptic-curves-group-law/scratch/code/`.

# Referee report for *Integers*: "Triples with Equal Sum and Equal Reciprocal Sum"

**Referee N-b: rational points and group laws on plane cubics.** My assignment was Sections 2, 3 and 5, plus the new comparison with Choudhry's three-parameter solution in the introduction (p. 5). I read the rendered pages (pdftoppm) for every passage cited below. I treated the placeholders (author contributions, AI-use statement, Zenodo DOIs, preprint identifiers) as known.

## Summary

The note studies unordered triples of positive integers that share their sum S and their reciprocal sum R with another triple. Sections 2, 3 and 5 contain the geometry:

- **Section 2.** A class of such triples is a finite set of positive rational points on one member of the pencil C_Λ : e1e2 = Λe3 (Λ = SR). This is the Bremner–Guy–Nowakowski curve, and it is identified with the Γ1(6) (Beauville / Top–Yui) pencil. Section 2 gives an explicit Weierstrass model E_Λ and the six base points with their group structure. Lemma 2 shows that the positive real locus is the non-identity real component.
- **Section 3.** Reciprocation is translation by the 2-torsion point T2 = (0:0:1) (Prop. 3). Coordinate permutations act as P ↦ ±P + (3-torsion) (Lemma 3). Theorem 1 gives the torsion (Z/6, Z/12, Z/2×Z/6, with explicit criteria) and identifies the positive torsion points as the isosceles triples and the geometric progressions, with their exact orders. Lemma 4 says which torsion translations preserve positivity, and Remark 1 excludes non-trivial families of pairs by linear forms.
- **Section 5.** Schinzel's argument, applied to the positive point (4:9:18) of infinite order on C_{155/12}, gives infinitely many primitive classes of every size (Theorem 4). Ranks of five curves are proved by a 2-isogeny descent (Table 1). Table 2 lists the first class of each size.
- **Choudhry comparison (p. 5).** Choudhry's second solution for exponents −1, 1 [11, (35)] is identified with P ↦ −(2P + τ), which is never positive.

Within my sections I found **no mathematical error**. Every statement I could test symbolically or numerically is correct, and the descent in Table 1 agrees exactly with an independent local-solubility computation of mine. I found **one factual misstatement in the new Choudhry comparison** (M1). It concerns attribution, so it matters, and it contradicts the paper's own Theorem 2. The remaining points are small gaps and presentation.

## Significance (for the parts I reviewed)

Most of Sections 2, 3 and 5 is classical, and the authors say so honestly:

- The pencil, its fibre types and the order-6 structure come from Beauville, Kubert and Top–Yui.
- Reciprocation as a 2-torsion translation and the "egg" are in Bremner–Guy–Nowakowski [3].
- Theorem 1(i)–(iii) is Kubert's description of the curves with a point of order 6, combined with Mazur.
- Section 5 is Schinzel's argument with a different curve, and the authors claim no novelty for it.

What is new here is:

- the clean, elementary, plane-model treatment;
- the classification of the *positive* torsion points for rational Λ (Theorem 1(iv));
- Lemma 4;
- Remark 1;
- the identification of Choudhry's family in the group law.

All of these are short consequences of Lemma 2 and the explicit group law. They are useful and correct, but modest. Taken alone they would not justify a paper. They serve as the geometric foundation for Sections 4 and 6, which are outside my remit. For *Integers*, foundational exposition of this kind is acceptable if it is accurately attributed. That is why M1 matters.

## Correctness, and what I recomputed

All computations were done in a private venv (sympy, cypari2 with PARI/GP 2.17.2), using code I wrote myself. The scripts are in `scratch/code/` (`glaw.py`, `t1.py`–`t7.py`, `descent.py`).

1. **Tate normal form (p. 3).** With c = −1/Λ, the substitution x = c²s/4 + c, y = c³η/8 + c²(c−1)s/8 + c² carries E_Λ to y² + (1−c)xy − (c+c²)y = x³ − (c+c²)x² exactly; the remainder modulo E_Λ is 0. The Tate point (0,0) corresponds to (s,η) = (4Λ, 4Λ(1−Λ)). This is the image of (0:1:0) under the map of Prop. 2, which agrees with "(0:1:0) = −(1:0:0)". Confirmed.
2. **Prop. 2 (pp. 7–8).**
   - Δ(E_Λ) = 2¹²Λ²(Λ−1)³(Λ−9) and c4 = 16(Λ−3)(Λ³−9Λ²+3Λ−3), with c4(0), c4(1), c4(9) = 144, 256, 2304, all nonzero. So the fibres are I2, I3, I1 at Λ = 0, 1, 9. At ∞ the order of Δ is 6 and c4 ≠ 0, giving I6.
   - The map C_Λ → E_Λ and its stated inverse both land on the target modulo the source equation. The composite recovers (x+y)/z, so the maps are mutually inverse.
   - (1:4:4) on C_{27/2} maps to (−6, 45). O maps to ∞ and T2 to (0,0).
   - The tangent at O restricts the cubic to Λ(Λ−1)z³, so O is a flex.
   - The Shioda–Tate count 10 = 2 + 0 + 8 and the identity |MW|² = 6·3·2·1 = 36 are correct.
   - My fibre-type assignment agrees with Top–Yui [30], whose Table 2 lists Γ0(6) with exactly the equation (x+y)(y+z)(z+x) + t·xyz = 0.
3. **Base-point group (p. 8).** I wrote an exact chord-and-tangent group law on the plane cubic with origin O = (1:−1:0). On Λ = 27/2, 49/4, 169/16, 155/12 and 10 it confirms the following: T2 has order 2; (0:1:−1) and (1:0:−1) have order 3; (1:0:0) and (0:1:0) have order 6; and the relations −A = (0:1:0), A = T2 + Q, 2A = −Q all hold.
4. **Lemma 2 (pp. 8–9).** The argument is sound. The positive locus is compact and open, hence a union of components. It is nonempty and misses O, and C_Λ(R) ≅ S¹ × Z/2 because Δ > 0. Therefore it is exactly the non-identity component.
5. **Prop. 3 (p. 9).** I checked the line-through-T2 computation (root product p0p1, third point V = (p0p2 : p1p2 : p0p1)) by hand. The difference vector (p0−p1)p2(1,−1,0) is correct. Numerically, ι(P) = P + T2 for P = (4:9:18).
6. **Corollary 1 (pp. 9–10).** Correct. For (1,4,4) the pair 24(1,4,4), 9(16,4,4) divided by 12 gives {(2,8,8),(12,3,3)}.
7. **Lemma 3 (p. 10).** Confirmed by the group law:
   - swapping x and y gives −P;
   - swapping y and z gives (1:0:−1) − P;
   - swapping x and z gives (0:1:−1) − P;
   - the cyclic shift (x2,x3,x1) is P + (1:0:−1), and (x3,x1,x2) is P + (0:1:−1).

   The proof is correct: it uses the automorphism group of an elliptic curve and the fixed-point argument at (1:1:1), (1:ω:ω²) and (1:ω²:ω).
8. **Theorem 1 (pp. 10–11).** Each step of (i)–(iv) checks. Mazur's theorem is indeed Chapter III, Theorem (5.1), p. 156 of [22]; I checked the Numdam scan. On G = (1:2:4) (Λ = 49/4) and G = (1:−4:16) (Λ = 169/16) I find:
   - G has order 12 and 2G = (0:1:−1) + T2;
   - the six orderings are G, 3G, 5G, 7G, 9G, 11G exactly as stated;
   - (1:r²:r) and (r²:1:r) have order 4, and the rest have order 12.

   On C_{27/2}, the points (1:4:4) and (4:1:4) have order 6 and (4:4:1) has order 2. PARI's `elltors` gives Z/12 for Λ = 49/4 and 169/16, and Z/2×Z/6 for Λ = 27/2 and 10. The remark "for integer Λ > 9 the only positive torsion points are at Λ = 10" is correct. (Λ−1)(Λ−9) is a square only for Λ = 10, and (r+1+1/r)² is an integer only for r = ±1.
9. **Lemma 4 and the C_{169/16} examples (p. 12; also p. 20).** PARI gives rank 1 for C_{169/16}. All four listed pairs, starting with {(165,240,440),(182,208,455)}, differ for suitable orderings by torsion points of orders 4 and 12 (multiples ±G, ±5G, ±3G or 9G).
10. **Remark 1 (pp. 12–13).** I checked the proof line by line. It is correct, including the impossible case (a+b)² = ab.
11. **Lemma 1 and Prop. 1 (pp. 6–7).** I checked both line by line, including the two discriminants 3(c′+3)(1−c′) and (c′+4)(24−22c′−c′²)/(6−c′). Both are correct.
12. **Choudhry comparison (p. 5).** I fetched [11] (Rocky Mountain J. Math. 41 (2011), 737–763, via the Wayback Machine; p. 748, (34)–(35)).
    - Symbolically, Choudhry's y in (35) has the same sum and reciprocal sum as x, and it is collinear with x and (x2,x3,x1). So it is the third intersection, exactly as the authors say. It is in fact Choudhry's own construction (34).
    - For 300 random triples x, the group law gives y = −(2P + τ) with τ = (1:0:−1), and y was never positive.
    - Chen's survey [10, A.5.1] lists "Ajai Choudhry gave a three-parameter solution" and the triples quoted.
    - The class at S = 408 does contain (51,102,255).
    - The pairs at S = 18, 20, 26, 31, 32, 34 are the only ones with S ≤ 34, as the text implies.
13. **Theorem 4 and Section 5 (pp. 17–18).**
    - P = (4:9:18) lies on C_{155/12}. 3P = (162833463 : 723926268 : 287876366) and P + T2 = (9:4:2), both as stated, and 2P = (16352 : 288 : −365) is not positive, consistent with Lemma 2.
    - Table 1's a and b are correct for all five Λ.
    - PARI's `ellrank` gives r1 = r2 = 0, 2, 2, 3, 3 and `elltors` gives Z/2×Z/6, Z/6, Z/6, Z/6, Z/6. Conductors are 90, 6250530, 82110, 1715185290, 41388270, and root numbers are +, +, +, −, −. All as stated.
    - **Independent descent.** I wrote my own recursive Q_p-solubility test for N² = d M⁴ + a M²e² + (b/d)e⁴, run at every p | 2b(a²−4b) and at ∞, for both isogenous curves. The φ- and φ̂-Selmer groups it returns coincide *exactly* with the sets in Table 1, for all five curves. Those sets are also generated by the images of the torsion points and of PARI's generators. So Table 1 and the claim Ш[φ] = Ш[φ̂] = 0 are correct.
    - All members of Table 2 have the stated S and Λ.
    - A direct enumeration for S ≤ 420 confirms that the first classes of sizes 2, 3, 4 are at S = 18, 136, 408 with the listed members, and that N(100), N(200), N(300), N(400) = 92, 386, 840, 1496, matching Table 3.
    - (Λ−1)(Λ−9)·q² = 6721, 1449, 1329601, 8569 are non-squares.

**Not verified:** the page-level quotations from Bremner–Guy–Nowakowski [3, pp. 117–120] (the AMS PDF was not retrievable headlessly), and Beauville's table [1].

## FATAL

None.

## MAJOR

**M1 (p. 5, Choudhry comparison). The claim that "the isosceles family below does not appear in that section" is false, and it contradicts the paper's own Theorem 2.**

- The same paragraph identifies Choudhry's first solution y_i = m/x_i (with m = Σx_i / Σx_i⁻¹) with the dual family of Corollary 1.
- Theorem 2 (p. 13) describes D_{u,v} as "the dual pair of (u, v, v)".
- Concretely, Choudhry's first solution at x = (u, v, v) is y = m·(1/u, 1/v, 1/v), which is proportional to (v, u, u). This is D_{u,v}.

So the isosceles family is exactly the specialisation x = (u, v, v) of a solution printed in [11, §4.1]. Choudhry gives that solution for arbitrary positive x_i, so it includes x = (u, v, v), although he does not single out the isosceles case. The paper also says on p. 6 that "a parametric family [is] in [11]". Telling the reader that the isosceles family is absent from Choudhry misattributes the source of the family whose count is Theorem 2.

This is a priority statement in the comparison newly added in this revision. Fixing it does not affect any theorem, but as written it is inaccurate.

*Resolution:* Replace the clause with something like: "the isosceles family of Theorem 2 is the specialisation x = (u, v, v) of his first solution, though he does not single it out". Check the novelty sentence on p. 6 for consistency with this.

## MINOR

- **m1 (p. 5).** The argument "by Lemma 2 it is never positive when x is" is correct but weaker than the truth, and it leaves the reader to handle Λ ≤ 9 and non-positive x. Since C_Λ(R)/C_Λ(R)⁰ ≅ Z/2, the point 2P lies on the identity component for *every* real P. The point τ, of order 3, lies there too. So −(2P+τ) is never positive, for any x. If the second member were positive, Λ would be at least 9, and Λ = 9 forces x = (1,1,1), where (35) is undefined. Stating it this way is shorter and gives the stronger conclusion: no member y of Choudhry's second family is ever a positive triple.
- **m2 (p. 5).** Choudhry's derivation *is* the line through x and its cyclic shift; see [11, (34)], y_i = (x_{i+1} − x_i)t + x_i. Saying "by construction [11, (34)]" would make the identification self-evidently faithful to the source.
- **m3 (p. 5).** "Three-parameter" is Chen's and Choudhry's wording. The solution is homogeneous of degree 1 in (x1, x2, x3), so projectively it is a two-parameter family: the rational surface {(P, −2P−τ)} in the variety of pairs. Saying this would connect it with the heuristic of §6.4. It is an explicit rational surface of pairs whose positive locus is empty, which illustrates why the authors' condition in §6.4 concerns positive real points.
- **m4 (p. 11, Theorem 1(iv)).** The proof concludes that the six points of G + Z/6 *are* the six orderings of (1, r, r²). This needs the orderings to be six distinct projective points. That holds because r ∈ Q, r ≠ 0, ±1, but the proof should say so in one line. The analogous fact for (1,1,t) is stated, as t ≠ ±1.
- **m5 (p. 8, proof of Prop. 2).** The proof that the maps are mutually inverse and that Δ is as stated is delegated to `check_note.py`. These are short identities. State them, for example: substituting the inverse into F_Λ gives a multiple of the E_Λ equation, and the composite C_Λ → E_Λ → C_Λ returns (x+y)/z modulo F_Λ. Then the printed proof is self-contained.
- **m6 (pp. 17–18, Table 1).** The text says the Selmer groups are "cut out by the local conditions" and that "the images of explicit rational points fill them". However, neither the points nor the method of the local computation appears in the paper. Please list, for each curve, rational points whose α- or ᾱ-images generate the listed groups. For example, PARI's generators on y² = x(x²+ax+b) are:
  - Λ = 155/12: (−11904, 154752), (−9720, 463320);
  - Λ = 68/5: (−2000, 42000), (8500, 892500);
  - Λ = 1849/120: (−132096, 163138560), (1100800/9, 5309158400/27), (154800/49, 4626507600/343);
  - Λ = 230/21: (−20580, 391020), (−17388, 991116), (10143, 1927170).

  Add the needed points on the isogenous curve, and one sentence on which primes were checked (p | 2b(a²−4b) and ∞). As it stands the reader must redo the descent to check the table. I did, and it is correct.
- **m7 (p. 18).** "So C_{27/2} has rank 0" follows the sentence on root numbers and conductors, which gives only the parity. The rank 0 comes from Table 1. Reorder the sentences or change "So" to "By Table 1".
- **m8 (p. 3).** "the elliptic modular surface of Γ0(6) [30, Table 2], which is ±Γ1(6)". This matches [30], but elliptic modular surfaces are normally attached to groups without −I. Saying "the elliptic modular surface of Γ1(6), whose image in PSL2(Z) equals that of Γ0(6), as in [30, Table 2]" would be more precise.

## Presentation

- **P1 (throughout, first used p. 1).** "Positive point" of P²(Q) is never defined. Please define it once in §1.2 or at the start of §2: a point with a representative whose coordinates are all positive (equivalently, all of one sign).
- **P2 (p. 11).** The parenthesis "(of Lemma 3 only its formulas for the action are used)" is awkward. Better: "(we use only the formulas of Lemma 3 for the action, not its statement about orbits, which assumes infinite order)".
- **P3 (p. 18).** "No class of size 7" appears both in the caption of Table 2 and at the end of the following paragraph. Keep one.
- **P4 (p. 10, after Lemma 3).** "Which of these differences are torsion is decided by positivity" anticipates Lemma 4 but reads as a non sequitur before Theorem 1. A forward reference to Lemma 4 would help.

## Recommendation

**Minor revision** for Sections 2, 3 and 5 and the Choudhry comparison. My confidence is high for correctness, since nearly every claim was recomputed, and moderate for the significance judgment.

There are no fatal or proof-level errors in my sections. Every statement I tested is correct, including the full 2-isogeny descent. The one substantive defect is M1: an inaccurate attribution in the newly added Choudhry comparison, which contradicts the paper's own description of the isosceles family. It must be fixed before acceptance, but it is a one-sentence correction. The geometry in these sections is mostly classical, as the authors acknowledge. Its value lies in serving the counting results of Sections 4 and 6, which other referees assess.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | State that the isosceles family is Choudhry's first solution at x = (u,v,v), not absent from §4.1 of [11]; align the p. 6 novelty sentence. |
| m1 | Replace "by Lemma 2 it is never positive when x is" by the component argument: 2P and τ lie on the identity component, so −(2P+τ) is never positive. |
| m2 | Cite [11, (34)] as the construction of the line. |
| m3 | Optional: one sentence identifying Choudhry's family with the surface {(P, −2P−τ)}, linked to §6.4. |
| m4 | One line: the six orderings of (1,r,r²) are distinct for r ∈ Q, r ≠ 0, ±1. |
| m5 | State the two identities that prove Prop. 2 in the text. |
| m6 | List the rational points generating the α and ᾱ images, and the primes at which local solubility was tested. |
| m7 | Attribute the rank 0 of C_{27/2} to Table 1, not to the root number. |
| m8 | Rephrase the Γ0(6)/Γ1(6) sentence. |
| P1–P4 | Wording changes as indicated. |
