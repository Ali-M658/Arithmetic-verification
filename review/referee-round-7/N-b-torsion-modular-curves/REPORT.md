<!-- N-b referee (torsion and modular curves), round 7: returned text saved verbatim; the reviewer could not write files -->

# Referee report for *Integers*: "Triples with Equal Sum and Equal Reciprocal Sum"

I could not save this to `REPORT.md`: the write was refused because subagents must return findings as text. The full report follows.

**Assigned part:** Sections 2, 3 and 5 (pp. 5–14). These cover the curves C_Λ, the pencil and the Weierstrass model, the egg lemma, reciprocation as translation by a 2-torsion point, the action of S_3, the torsion theorem (Theorem 1 / Theorem A), classes of every size (Theorem 4 / Theorem C), and the ranks, root numbers and 2-isogeny descents with Table 1.

**Placeholders** (author contributions, AI-use statement, Zenodo DOI, preprint identifier) are treated as known.

---

## 1. Summary

The note shows that integer triples sharing a sum S and a reciprocal sum R are rescaled positive rational points on one fibre C_Λ : e1·e2 = Λ·e3 (Λ = SR) of Beauville's pencil with singular fibres I6, I3, I2, I1. In my part it proves the following:

- **Lemma 1.** Every coincidence is admissible (R < 1).
- **Proposition 1.** A class is a finite set of positive points on one C_Λ.
- **Proposition 2.** It lists the singular fibres and gives an explicit Q-birational map to E_Λ : η² = s(s² + (Λ²−6Λ−3)s + 16Λ). The base points form Z/6, with origin O = (1:−1:0).
- **Lemma 2 (the egg).** For Λ > 9, the positive locus is the non-identity real component.
- **Proposition 3.** Reciprocation ι is translation by T2 = (0:0:1).
- **Action of S_3.** Transpositions act as P ↦ π(O) − P, and 3-cycles act as translations by points of order 3.
- **Theorem 1.** The torsion subgroup is Z/6, Z/12 or Z/2×Z/6, with criteria for each. For Λ > 9, a positive point is torsion exactly when two entries are equal or the entries form a geometric progression. The orders are given explicitly.
- **Theorem 4.** For every k there are infinitely many primitive classes of size ≥ k, by Schinzel's method on C_{155/12}.
- **Section 5.** Ranks, root numbers and 2-isogeny Selmer groups for the Table 1 curves.

## 2. Significance

The arithmetic in my part is correct, clearly written and almost self-contained. To an arithmetic geometer it is also largely classical. C_Λ is the universal elliptic curve over X_1(6) (see M2). Given that, Theorem 1(i)–(iii) is the standard description of the rational points on the genus-0 covers X_1(12) → X_1(6) and X_1(2,6) → X_1(6), combined with Mazur's theorem.

What is new and useful:

- the translation into the language of triples: isosceles triples are points of order 2 or 6, and geometric progressions are points of order 4 or 12;
- the clean proof that ι is translation by T2;
- the use of these facts in the counting results.

Credit to Bremner–Guy–Nowakowski and to Beauville is given honestly. Credit to Kubert, and the modular interpretation, are missing. The note also misses one structural consequence of its own torsion theorem (M1).

## 3. Correctness, and what I recomputed

I used PARI/GP 2.17.2 (through cypari2) and independent Python code, all in exact arithmetic.

1. **Proposition 2 (p. 6).**
   - Both maps are verified symbolically. Each lands on the target curve, and both compositions are the identity modulo the defining equations.
   - The discriminant is 2^12 Λ²(Λ−1)³(Λ−9). The j-invariant is (Λ−3)³(Λ³−9Λ²+3Λ−3)³ / (Λ²(Λ−1)³(Λ−9)).
   - The fibre types are I2 at Λ = 0, I3 at Λ = 1, I1 at Λ = 9 and I6 at Λ = ∞.
   - At Λ = 27/2, the point (1:4:4) maps to (−6, 45), as printed.
2. **Base-point group (p. 6).** I re-derived:
   - all five line intersections;
   - that O is a flex, with tangent x + y = (Λ−1)z;
   - the multiplicity 2 at the three coordinate points;
   - the relations (0:1:0) = −A, (1:0:−1) = −Q, A = T2 + Q, 2A = −Q and 2T2 = O.

   All are correct.
3. **Lemma 1 (p. 5).** The case analysis is complete. Both discriminants are correct and negative. The rendered page correctly prints R = 6/5 and 13/12 (pdftotext garbles these).
4. **Lemma 2.** Correct.
5. **Proposition 3.** I verified:
   - the third intersection point R = (p0p2 : p1p2 : p0p1);
   - the identity F(ι(P)) = p0p1p2 · F(P);
   - that O, R and ι(P) are collinear;
   - that the excluded set p0p1p2(p0 − p1) ≠ 0 covers every degenerate case.

   Correct.
6. **Action of S_3 (p. 8).** The values π(O) for the three transpositions are as stated, and the 3-cycles have no fixed points on C_Λ. This is correct apart from one omitted step (m1).
7. **Theorem 1.** Each step of (ii)–(iv) checks out, including the bookkeeping of the multiples 3G, 4G, 5G, 6G, 7G, 8G and 9G.
   - In 300 random tests, `elltors` gives Z/2×Z/6 exactly when (Λ−1)(Λ−9) is a square.
   - In 300 random tests of Λ = (r+1+1/r)², `elltors` always gives Z/12.
   - On C_{27/2}, the points (1:4:4) and (4:1:4) have order 6 and (4:4:1) has order 2.
   - On C_{49/4}, the points (1:4:2) and (4:1:2) have order 4, and the other four orderings of (1, 2, 4) have order 12.
   - In Kubert's Tate normal form E(b, c) with b = c + c², j(C_Λ) equals j(E(b, c)) exactly when Λ = −1/c. I checked this as an identity of rational functions.
8. **Theorem 4.**
   - P = (4:9:18) lies on C_{155/12}.
   - 3P = (162833463 : 723926268 : 287876366), exactly as printed.
   - 2P = (−16352 : −288 : 365), which is not positive.
   - ι(P) = (9:4:2).
9. **Table 1.**
   - Every member has the stated sum S and the stated Λ, and every class is primitive.
   - `ellrank` gives [0,0], [2,2], [3,3] and [3,3], and C_{155/12} has rank 2.
   - The torsion subgroups are as stated.
   - The root numbers are +1 (27/2), +1 (68/5), −1 (1849/120), −1 (230/21) and +1 (155/12).
10. **2-isogeny descent.** I wrote my own local-solvability code for the quartics N² = dM⁴ + aM²e² + (b/d)e⁴, at ∞ and at all bad primes. It uses the integral model a = p² − 6pq − 3q², b = 16pq³ for Λ = p/q.
    - The Selmer orders are (4,1), (4,4), (8,4), (16,2) and (8,2), exactly as in the paper.
    - No local test was inconclusive.
11. **Enumeration up to S = 600 (independent code).**
    - The counts N, N_cl and primitive classes match Table 2 at X = 18, 100, 200, …, 600.
    - There are 1753 primitive pairs, of which 423 are dual and 1330 are not, as stated on p. 8.
    - The first classes of sizes 2, 3 and 4 occur at S = 18, 136 and 408, with exactly the Table 1 members.
12. **Mazur [12] (fetched from Numdam).** Page 156 is correct. The item cited, however, should be Theorem (5.1), not Corollary (5.2) (see m10).

I could not retrieve Bremner–Guy–Nowakowski [3]; the AMS server returned HTML. The verbatim quotations on pp. 6–8 are therefore unchecked by me. Their content is consistent with my computations: for integer Λ, the only Z/2×Z/6 case is Λ = 10, and Λ = (r+1+1/r)² is never an integer outside {1, 9}.

## 4. FATAL

None. Every proof that a main result of Sections 2, 3 and 5 depends on is correct, and every number I recomputed agrees.

## 5. MAJOR

**M1 (pp. 8, 14, 17–18). A missed source of coincidences: translation by torsion points of order 4 and 12.**

What the note says:
- p. 8: the orbit of P under permutations, ι and translation by the *base* points has twelve points, and two non-dual positive points of a class differ by a point outside the group of base points. This is checked only for S ≤ 600.
- p. 14: "for the other pairs we know no structure beyond the group law".
- pp. 17–18: only the twelve surfaces {(P, ±P + T)}, with T a base point, are singled out.

What is missed:
- By Lemma 2, translation by a torsion point T keeps positive points positive exactly when T lies on the identity component C_Λ(R)^0.
- In case (iii), G = (1:r:r²) lies on that component exactly when r < 0.
- Λ = (r+1+1/r)² exceeds 9 for r < −2 − √3 or −2 + √3 < r < 0.
- On such curves, if P is positive then so is P + G. So every positive point of infinite order gives a class of size ≥ 4: {x, x*, y, y*} with y = P + G. These are not dual pairs.

Verified example on C_{169/16} (r = −4; torsion Z/12, rank 1):
- The four triples (6,11,16), (33,48,88), (14,16,35) and (16,35,40) all have Λ = 169/16.
- The primitive non-dual pair {(165,240,440), (182,208,455)} has S = 845 and R = 1/80. Depending on the ordering, the two points differ by a torsion point of order 4 or 12; for example, Y + X has order 12.
- A second such pair occurs at S = 1183: {(208,455,520), (231,336,616)}.

My search covered every non-dual primitive pair with S ≤ 1300 on Z/12 curves. These two are the only pairs of torsion type. The other hits have r > 0 and pair a geometric progression with a point of infinite order. This explains why the S ≤ 600 check found nothing.

No theorem becomes false. But the structural picture in Sections 3 and 6.4 is incomplete, and the "16.5% dual" statistic needs a third category.

**Fix:**
- State that the torsion-explained partners of P are ±P + T with T ∈ C_Λ(Q)_tors ∩ C_Λ(R)^0. This is the base group, except on Z/12 curves with r < 0, where it is all of Z/12.
- Add the C_{169/16} example.
- Count such pairs up to 4800.
- Revise pp. 8, 14 and 17–18.

**M2 (pp. 3–9). Missing modular interpretation and attribution.**

- (C_Λ, A = (1:0:0)) is Kubert's universal curve over X_1(6), with Λ = −1/c in Tate normal form E(c + c², c); I verified this through the j-invariant.
- Beauville's I6 I3 I2 I1 surface is the elliptic modular surface for Γ_1(6), with Mordell–Weil group Z/6 (Oguiso–Shioda).
- Theorem 1(i)–(iii) is therefore the description of the rational points of X_1(12) → X_1(6) and X_1(2,6) → X_1(6) (Kubert 1976), combined with Mazur's theorem. The degrees match: 4 and 2.
- The note never mentions X_1(N), Kubert or Tate normal form, and attributes the geometry only to [3] and [1].

**Fix:**
- Add a remark giving Λ = −1/c and Kubert's parameters for Z/12 and Z/2×Z/6.
- Cite Kubert, and Oguiso–Shioda (or Shioda).
- Reword the novelty claim: what is new is the translation into triples and part (iv).
- Note that (ii) and (iii) are mutually exclusive, since Z/2×Z/12 does not occur over Q.

## 6. MINOR

- **m1 (p. 8).** The step "α = −1" only excludes α = 1. Add that π² = id forces α² = 1. This matters because j = 0 occurs at the rational value Λ = 3.
- **m2 (p. 8).** The proof of Theorem 1(iv) relies on the S_3 action, which sits in an unnumbered paragraph mixed with computational asides. Make it a numbered lemma.
- **m3 (p. 13).** Under the standard convention (Silverman, AEC X.4), the isogeny φ with kernel (0,0) has Sel^φ of order 1 and Sel^φ̂ of order 4 for C_{27/2}. The printed "4 and 1" is in the opposite order (the same reversal applies to 1849/120, 230/21 and 155/12). The ranks are unaffected. State the convention used.
- **m4 (p. 13).** Give all five root numbers; +1 for C_{27/2} is missing. Also give the conductors (90, 82110, 1715185290 and 41388270 for the Table 1 curves) so readers can check them against LMFDB.
- **m5 (p. 13).** The exact descent alone proves the ranks, so the floating-point caveat about the regulator is moot. Say so, and list the generators.
- **m6 (pp. 9–10).** Remark 1 is only a sketch. Matching partial fractions line by line does not give the per-line sum condition a + b = c. Either prove that step or weaken the claim; Section 6.4 relies on it.
- **m7 (p. 9).** The sets ±G + T and ±P0 + T have six points, not twelve: the dual of a geometric progression is one of its own orderings. Say so.
- **m8 (p. 6).** "c4 ≠ 0, so multiplicative" also needs ord Δ < 12, so that the model is minimal there.
- **m9 (p. 8).** Say "not torsion" rather than "order at most 12", and specify which orderings of the points were compared.
- **m10 (pp. 8, 9).** Mazur's Corollary (5.2) only bounds the order of a single rational point (m ≤ 10 or m = 12). It does not exclude Z/2×Z/12 or Z/3×Z/6. The list used in Theorem 1(i) is Theorem (5.1), on the same p. 156. Cite Theorem (5.1), or add the Weil-pairing argument against Z/3×Z/6.

## 7. Presentation

- **P1.** I found no typographical, sign or figure errors on the rendered pp. 5–9 and 13–14.
- **P2.** A table for Theorem 1(iv) would help, with columns for the ordering, the corresponding multiple of G or P0, and the order.
- **P3.** On p. 7, say which model's point (0,0) is meant in the BGN table, and identify it with T2.

## 8. Recommendation

**Major revision**, with high confidence for Sections 2, 3 and 5. The mathematics is correct and every number I recomputed agrees. The required changes are:

- the missed torsion-translation phenomenon (M1);
- the modular context and attribution (M2);
- the precise Mazur citation (m10).

All of these are readily fixable.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Classify the positivity-preserving torsion translations. Add the C_{169/16} pairs at S = 845 and 1183. Count such pairs up to 4800. Revise pp. 8, 14 and 17–18. |
| M2 | Add the Λ = −1/c remark and the X_1(12) and X_1(2,6) parameters. Cite Kubert and Oguiso–Shioda. Reword the novelty claim. Note that (ii) and (iii) are mutually exclusive. |
| m1 | Add: π² = id, so α² = 1. |
| m2 | Make the S_3 action a numbered lemma. |
| m3 | State the Selmer convention. |
| m4 | Give all five root numbers and the conductors. |
| m5 | Say the descent alone proves the ranks; list the generators. |
| m6 | Complete Remark 1 or weaken its conclusion. |
| m7 | Count the coset as six points. |
| m8 | Add the minimality clause. |
| m9 | Say "not torsion" and specify the orderings. |
| m10 | Cite Mazur, Theorem (5.1). |

Everything is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/N-b-torsion-modular-curves/scratch/`:
- `code/` holds the checks: `c1.gp`–`c5.gp`, the descent in `sel.py`, and the enumerations `enumc.py` and `enum2.py`.
- `pages/` holds the rendered page images.
- `lit/mazur.pdf` is the Mazur paper fetched from Numdam.
