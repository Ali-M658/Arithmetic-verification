<!-- Round 8 N-b referee report: returned text saved verbatim; the reviewer could not write files -->

I couldn't save the report: writing `REPORT.md` was refused. So here it is in full. Sections 2, 3 and 5 are correct, and every number I could recompute matches. I recommend minor revision. There is one major issue: the abstract says "classes of every size", but the paper only proves classes of size at least k.

# Referee report: "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

**Scope of this report.** Sections 2, 3 and 5: the curves C_Λ, their Weierstrass models and torsion; reciprocation, permutations and torsion translations; ranks and descents; classes of every size. I also checked the parts of Section 1 that state or cite these results (the Tate normal form on p. 3, Theorems A and C, the MacLeod substitution on p. 5) and the members of Table 1 (p. 16). I did not referee Sections 4 and 6, apart from the Table 1 entries that Section 5 quotes. I rendered the PDF at 110 dpi and read pages 3 and 6–11 and 15–16 as images. Every sign and typographical remark below was checked against those images.

## 1. Summary

The note studies unordered triples of positive integers that share both the sum e1 and the reciprocal sum e2/e3 with another triple. Sections 2, 3 and 5 contain the arithmetic-geometric part:

- **Section 2.**
  - Lemma 1: a triple with R ≥ 1 never takes part in a coincidence.
  - Proposition 1: classes are sets of positive points on one fibre C_Λ : e1e2 = Λe3 of Beauville's I6 I3 I2 I1 pencil.
  - Proposition 2: an explicit Q-isomorphism C_Λ → E_Λ : η² = s(s² + (Λ²−6Λ−3)s + 16Λ), with the discriminant, the fibre types, and the base-point group Z/6.
  - Lemma 2: for Λ > 9 the positive locus is the non-identity real component (the "egg").
- **Section 3.**
  - Proposition 3: the Cremona involution ι is translation by T2.
  - Corollary 1: the dual family.
  - Lemma 3: transpositions act as P ↦ π(O) − P and 3-cycles as translations by 3-torsion.
  - Theorem 1: the torsion is Z/6, Z/12 or Z/2×Z/6, with explicit criteria, plus a description of the positive torsion points and their orders.
  - Lemma 4: which torsion translations preserve positivity.
  - Remark 1: no linear families.
- **Section 5.**
  - Theorem 4: for every k there are infinitely many primitive classes of size ≥ k. This is Schinzel's argument applied to C_{155/12}.
  - Ranks, conductors, root numbers and 2-isogeny descent data for the five curves in Table 1.

## 2. Significance

The geometry of Sections 2–3 is largely classical, and the authors say so: Bremner–Guy–Nowakowski for the model and the reciprocal pairs, Beauville for the pencil, Kubert and Mazur for torsion. The genuinely new items are modest:

- Theorem 1(iv): the positive torsion points are exactly the isosceles triples and the geometric progressions, with their orders.
- Lemma 4: positivity under torsion translation. This yields the useful three-way sorting of primitive pairs: dual, Z/12 torsion with r < 0, or infinite order.

Theorem 4 is Schinzel's method word for word, and the authors claim no novelty for it.

The value of these sections is that they are complete, correct, cleanly attributed and precisely matched to the counting problem. For a note in *Integers* that is enough. I would not call any of it a significant advance in the arithmetic of elliptic curves.

## 3. Correctness, and what I recomputed

I used my own code in a private venv: cypari2 (the PARI library), sympy, and an exact rational-arithmetic group law on E_Λ. Every arithmetic claim in Sections 2, 3 and 5 that I could test was **correct**.

**Proposition 2 (pp. 6–7)**
- Pencil identity: (x+y)(y+z)(z+x) = e1e2 − e3. Correct.
- The forward map lands on E_Λ (modulo the cubic). The inverse lands on C_Λ (modulo E_Λ). Both compositions are the identity (sympy). Correct.
- Δ = 2^12 Λ²(Λ−1)³(Λ−9). Correct.
- Plane-curve singularities occur only at Λ ∈ {0, 1, 9}: gradient system solved, with nothing on z = 0. Λ = ∞ is the triangle xyz = 0.
- Fibre types: ord Δ = 2, 3, 1 at Λ = 0, 1, 9, with c4 ≠ 0 there. At ∞, deg a2 = 2, deg a4 = 1 and deg Δ = 6, so ord∞ Δ = 6, ord∞ c4 = 0, giving I6. Total 6+3+2+1 = 12. Correct.
- Example on p. 6: (1:4:4) on C_{27/2} maps to (−6, 45). Correct.
- O ↦ ∞ and T2 ↦ (0,0). Correct.
- Tangent at O is x + y = (Λ−1)z, and the cubic restricts to Λ(Λ−1)z³. Correct.
- All five line-section identities. Correct.
- Base-point orders, computed by the group law on four curves: O 1, T2 2, (0:1:−1) and (1:0:−1) 3, (1:0:0) and (0:1:0) 6. Correct.

**Tate normal form (p. 3)**
- With c = −1/Λ, the stated substitution carries E_Λ to y² + (1−c)xy − (c+c²)y = x³ − (c+c²)x² identically (sympy).
- (0:1:0) goes to (0,0), on the branch η = −4Λ(Λ−1), s = 4Λ.
- The degenerate values c = 0, −1, −1/9, ∞ correspond to Λ = ∞, 1, 9, 0. Correct.

**Lemma 1 (pp. 5–6)**
- Both discriminants were rederived: 3(c′+3)(1−c′), and (c′+4)(24−22c′−c′²)/(6−c′).
- The case split (least entries {1,·} or {2,3}) is exhaustive. Correct.

**Proposition 1 and Lemma 2 (pp. 6–7)**
- Both proofs are correct: compactness plus openness gives a union of components; Δ > 0 gives two real components.
- Group-law check of Lemma 2 on C_{155/12}: nP is positive for n = 1, 3, 5, 7 and not positive for n = 2, 4, 6.

**Proposition 3 and Corollary 1 (p. 8)**
- Root product p0p1 on the line through T2. Correct.
- F(yz, xz, xy) = e3 · F(x, y, z). Correct.
- V − ι(P) = (p0−p1)p2(1, −1, 0). Correct.
- The dual pair of (1,4,4) is {(2,8,8), (12,3,3)}, after dividing by 12. Correct.

**Lemma 3 (pp. 8–9)**
- Correct; the involution and fixed-point arguments are sound.
- π(O) for the three transpositions was checked.

**Theorem 1 (pp. 9–10)** was checked by the group law:
- C_{27/2} (Z/2×Z/6, confirmed by elltors): (1:1:4) and (4:4:1) have order 2; (1:4:4), (4:1:4), (4:1:1) and (1:4:1) have order 6. This matches "(v:v:u) order 2; (u:v:v), (v:u:v) order 6".
- C_{49/4} (r = 2, torsion Z/12): (1:4:2) and (4:1:2) have order 4, and the other four orderings of (1,2,4) have order 12. The "middle term last ⇒ order 4" rule holds.
- C_{169/16} (r = −4): (16:1:−4) and (1:16:−4) have order 4, and the rest order 12.
- 2G = (0:1:−1) + T2 = (1:0:0), together with 4G, 6G, 8G and the identification of the six orderings as G, 11G, 7G, 3G, 9G, 5G: all correct.
- Λ(1:r:r²) = (r+1+1/r)². Correct.
- Over the integers, (n−1)(n−9) is a square only for n = 10 (apart from n = 0, 1, 9). Z/12 never occurs for integer n ∉ {1, 9}. This is consistent with the BGN quotation on p. 7.

**Lemma 4 and the paragraph after it (pp. 10–11)**
- C_{169/16} has rank 1 (ellrank [1, 1]), torsion Z/12 and conductor 6630.
- {(165,240,440), (182,208,455)}: both triples have sum 845, R = 1/80 and Λ = 169/16.
- The difference of the two points is torsion for exactly 3 of the 6 orderings of the second triple, against each fixed ordering of the first: once of order 4 and twice of order 12. Correct.

**Remark 1 (p. 11)**
- I completed the sketch for the homogeneous case. Poles force the same set of lines on both sides. With three lines the entries coincide. With two lines, matching the ℓ1-coefficients of S forces a + b = c against 1/a + 1/b = 1/c. The argument is sound.

**Section 5 (p. 15).** Ranks, torsion, root numbers and conductors from PARI (ellrank, elltors, ellrootno, ellglobalred). Λ = p/q is put on the integral model a = p² − 6pq − 3q², b = 16pq³.

| Λ | rank (ellrank) | torsion | root no. | conductor |
|---|---|---|---|---|
| 27/2 | 0 | Z/2×Z/6 | +1 | 90 = 2·3²·5 |
| 155/12 | 2 | Z/6 | +1 | 6250530 |
| 68/5 | 2 | Z/6 | +1 | 82110 |
| 1849/120 | 3 | Z/6 | −1 | 1715185290 |
| 230/21 | 3 | Z/6 | −1 | 41388270 |

All of these agree with the paper.

**Independent 2-isogeny descent.** I wrote my own local-solubility test: a p-adic ball recursion with exact integers, run at all primes dividing 2b(a²−4b) and at ∞. It gives the following φ-Selmer groups:

| Λ | Sel^φ | \|Sel^φ\| | Sel^φ̂ | \|Sel^φ̂\| | rank |
|---|---|---|---|---|---|
| 27/2 | {±1, ±6} | 4 | {1} | 1 | 0 |
| 68/5 | {1, −5, −17, 85} | 4 | {1, 21, 69, 161} | 4 | 2 |
| 1849/120 | {1, −3, −10, 30, 43, −129, −430, 1290} | 8 | {1, 769, 1729, 1329601} | 4 | 3 |
| 230/21 | (16 classes) | 16 | {1, 8569} | 2 | 3 |
| 155/12 | {1, 3, −10, −30, −62, 155, −186, 465} | 8 | {1, 6721} | 2 | 2 |

These are exactly the orders 4/1, 4/4, 8/4, 16/2 and 8/2 stated on p. 15. For C_{27/2}, the 2-torsion points x = 0, −9, −384 fill Sel^φ = {1, 6, −1, −6}. That proves rank 0 and justifies the claim that the pair at S = 18 and its multiples are the only coincidences with Λ = 27/2.

**Theorem 4 (p. 15)**
- P = (4:9:18) lies on C_{155/12}. Correct.
- 3P = (162833463 : 723926268 : 287876366) and P + T2 = (9:4:2). Both reproduced exactly.
- ĥ(P) = 1.4534 (PARI normalisation). P is part of the ellrank basis, whose regulator is 2.3082.

**Table 1 (p. 16)**
- A brute-force enumeration from scratch for all S ≤ 408 confirms that the first classes of sizes 2, 3 and 4 are at S = 18, 136 and 408, with exactly the members listed.
- At S = 1849 and S = 4600 the largest classes have sizes 5 and 6, again with exactly the listed members.
- Every member has the stated Λ.
- The example at S = 36 (p. 16) was checked.

**Not verified:**
- The verbatim quotations from [3] (pp. 117–120); the AMS site refused headless access.
- That E_Λ is "model (6) of [3, p. 118]".
- The page and table references to [1], [18] and [26].

The editor or authors should confirm these against the originals.

## 4. FATAL

None. I found no error in any proof or arithmetic claim in Sections 2, 3 or 5.

## 5. MAJOR

**M1 (pp. 1, 14, 15; abstract, Section 5 title, Theorem C). The headline overstates the result.**
- The abstract says "classes of every size exist", and Section 5 is titled "Classes of Every Size".
- Theorem C and Theorem 4 prove only that there are infinitely many primitive classes of size **at least** k.
- Proposition 1 itself warns that the class at L "may contain further triples", and nothing in the proof controls them. A class of size exactly k for every k is not proved. Exact size is not obvious either: the extra members are the other positive points of C_{155/12} whose primitive sum divides L.

*Resolution:* say "arbitrarily large classes" (or "classes of size at least k for every k") in the abstract, the Section 5 title and the theorem name. Alternatively, prove the exact-size statement.

## 6. MINOR

**m1 (p. 15). The rank proofs cannot be checked from the paper.**
- The paper says the images of explicit rational points fill the local sets, but it prints neither the points nor the sets.
- The rank-0 claim for C_{27/2} carries a stated result: the only coincidences with Λ = 27/2 are the scaled smallest pair. So the paper should state the data used.

*Resolution:*
- Give the integral model explicitly (a = p² − 6pq − 3q², b = 16pq³ for Λ = p/q).
- Add a short table of Sel^φ and Sel^φ̂ (as in §3 above), with points realising each class.
- For C_{27/2} one line suffices: the 2-torsion x-coordinates 0, −9, −384 give {1, 6, −1, −6}, and Sel^φ̂ = {1}.

**m2 (p. 15). Use the standard terminology.** "Sets, cut out by local conditions" are the Selmer groups Sel^{(φ)}(E/Q) and Sel^{(φ̂)}(E′/Q).
- Say so, and note the consequence that Ш(E/Q)[φ] = Ш(E′/Q)[φ̂] = 0 for these five curves.
- "An independent 2-isogeny descent … proves them without it": "it" is ambiguous (ellrank? the 2-Selmer group?).

**m3 (p. 10, Theorem 1(iv) proof). Distinctness is not stated for the P0 coset.**
- The proof says the six points of P0 + Z/6 are the three orderings of (1,1,t) and the three of (t,t,1). That requires the six to be distinct, which the proof does not say.
- It holds because t ≠ ±1: t = 1 forces Λ = 9 and t = −1 forces Λ = 1.
- Likewise, the six orderings of (1, r, r²) are distinct because r ≠ ±1. (For G the proof does exhibit them as the six odd multiples, so only P0 needs the sentence.)
- Lemma 3 is stated for P of infinite order, but here it is applied to torsion points. Only its action formulas are needed, not the distinctness. Say so.

*Resolution:* add one sentence on each point.

**m4 (p. 7, Proposition 2 proof).**
- "Verified symbolically" is not a proof a reader can follow. At minimum state the identity: η² − s(s² + …) equals an explicit multiple of e1e2 − Λe3 under the substitution, and give the two compositions.
- "At Λ = ∞ the model is regular" is unclear. Say what is meant: in the parameter μ = 1/Λ, with s = s′/μ², the model is integral and minimal at μ = 0, and ord Δ = 12 − deg Δ = 6, ord c4 = 4 − deg c4 = 0.

**m5 (p. 6).** "Its singular members are at Λ = ∞, 1, 0, 9, with fibres of these types." At Λ = ∞ the plane member xyz = 0 has three components. The I6 fibre appears only on the surface obtained by blowing up the nine base points, where the three doubled base points supply the extra components. State that the fibre types refer to that rational elliptic surface.

**m6 (pp. 9–10, Theorem 1(iv)).** The rule "order 4 if the middle term is its last coordinate" depends on the choice of origin O = (1:−1:0) and of T2 = (0:0:1), which single out z. Add a sentence: the order-4 points P satisfy 2P = T2, and z is distinguished by O and T2.

**m7 (p. 11).** "Differ, for suitable orderings, by a torsion point of order 4 or 12" can be made exact. For each ordering of one triple, exactly three orderings of the other differ from it by torsion: one of order 4 and two of order 12.

**m8 (p. 16, Table 1).** The torsion column is attributed to elltors, but it follows from Theorem 1:
- Z/12 is excluded because Λ is not a rational square.
- Z/2×Z/6 is excluded because (Λ−1)(Λ−9) times the square of the denominator is 1449, 1329601, 8569 and 6721 respectively, and none is a square.

Say so. The text then supports itself and the theorem is put to use.

**m9 (p. 6, Proposition 1).** "No one of them proportional to a permutation of another" is, for primitive positive triples, just "pairwise distinct as unordered triples". Also, "a class is a finite set of positive rational points on C_Λ" should say "up to the action of S3", since one triple gives six points.

## 7. Presentation

**P1 (pp. 6–7).** Proposition 2 carries too much. It contains the pencil identification, the fibre types, the birational maps, the discriminant, the identification with BGN's model, a worked example, the base points and the group structure. Split it into a proposition (model and fibres) and a lemma (base points and group law).

**P2 (p. 11).** Remark 1 is a heuristic about families and belongs in §6.4, which uses it. If it stays in Section 3, give the full argument (about six lines; see §3 above) rather than "a sketch".

**P3 (p. 9).** Theorem 1(i): "Z/6, the group of base points, or Z/12, or Z/2×Z/6" reads as a list of four items. Write "Z/6 (the group of base points), Z/12, or Z/2×Z/6".

**P4 (p. 6).** "The first sends O to the point at infinity": say "the map C_Λ → E_Λ".

**P5 (p. 15, suggestion).** "Classes generated by one point are far out" could be quantified with canonical heights: ĥ(P) ≈ 1.453 and ĥ(3P) = 9ĥ(P).

I also expressed the Table 1 members in the ellrank Mordell–Weil bases. Up to torsion and sign, every class consists of the lattice points of smallest canonical height. For example, on C_{68/5}:
- (16,40,80) and (17,34,85) are ±P1, the dual pair;
- (15,55,66) and (65,70,273) are P2 ∓ P1.

The same pattern of a dual pair ±Q together with R ± Q appears in the classes of sizes 5 and 6. So the non-dual members differ by twice another class member, a relation the authors' test (P′ = ±mP + T, m ∈ {2, 3}) does not look for.

A short paragraph giving the members of each Table 1 class in terms of a Mordell–Weil basis, with their heights, would:
- answer "we know no structure beyond the group law" with at least this description;
- explain why small classes need curves of rank 2–3.

This is optional but would strengthen Section 5.

**P6 (p. 15).** The choice of C_{155/12} for Theorem 4 is unexplained. C_{68/5}, with the positive non-torsion point (2:5:10), is the curve of the first class of size 3, and using it would tie Theorem 4 to Table 1. Either way, say why.

## 8. Recommendation

For Sections 2, 3 and 5: **minor revision**. The confidence is high for the mathematics: every proof was checked line by line and every number was recomputed independently. The confidence is moderate for the bibliographic page references, which I could not access.

The mathematics is correct and honestly attributed. The new content is modest. M1 is a real overclaim in the abstract and the section title, but it is fixed by rewording.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Replace "classes of every size" with "arbitrarily large classes" in the abstract (p. 1), the Section 5 title (p. 14) and the Theorem C/4 names (pp. 3, 15), or prove the exact-size statement. |
| m1 | State the integral model; print Sel^φ and Sel^φ̂ with realising points for the five curves. |
| m2 | Use Selmer-group terminology; note Ш[φ] = Ш[φ̂] = 0; remove the ambiguous "it". |
| m3 | Add a distinctness sentence (t ≠ ±1, r ≠ ±1) and note that only Lemma 3's action formulas are used for torsion P. |
| m4 | State the verifying identities; define "regular at ∞" via μ = 1/Λ. |
| m5 | Say the fibre types are those of the blown-up rational elliptic surface. |
| m6 | Explain the z-asymmetry of the orders through O and T2. |
| m7 | State the exact count: one ordering at order 4, two at order 12. |
| m8 | Derive the torsion column of Table 1 from Theorem 1. |
| m9 | Simplify the hypothesis of Proposition 1; say "up to S3". |
| P1–P6 | As described in §7. |

---

My scripts and the rendered pages are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/N-b-descent-heights/scratch/` (`code/selmer.py`, `code/grp.py`, `code/sym.py`, `code/enum.py`, `code/c1.gp`, `code/h2.gp`).
