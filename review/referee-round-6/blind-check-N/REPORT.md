# Blind check of the round-6 changes to the note (returned text, saved verbatim; the checker could not write files)

I couldn't save the report to `REPORT.md` because the write was refused, so the full report is below. I found **no mathematical errors or gaps in any of the 15 items**. The only point is a wording slip in Proposition 2.

# Blind check N: "Triples with Equal Sum and Equal Reciprocal Sum" (Integers format, 19 pp.)

I used only `scratch/input/note-integers.pdf`. I rendered every page with `pdftoppm` (110 dpi, and 220 dpi for pp. 6 and 9) and read the formulas from the images. All scripts and outputs are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-6/blind-check-N/scratch/`:

| Item(s) | Script | Output |
|---|---|---|
| 1 | `c1_brute.py` | `c1_out.txt` |
| 3, 4 | `c3_group.py` (sympy and exact group law) | `c3_out.txt` |
| 5, 6, 7, 12 | `c5_perm_tors.py` | `c5_out.txt` |
| 7, 13 | `c7_pari.py` (cypari2 in the venv) | `c7_out.txt` |
| 9, 10 | `c9_iso.py` | `c9_out.txt` |
| 11, 14, 15, Table 1 | `c11_misc.py` | `c11_out.txt` |

`cubgrp.py` holds the exact chord-and-tangent arithmetic on C_Λ, with origin O = (1:−1:0).

## 1. Lemma 1 (Coincidences are admissible): VERIFIED

**List of triples with R ≥ 1.**
- If a ≥ 4, then R ≤ 3/4.
- If a = 3, then R ≥ 1 forces b = c = 3.
- If a = 2, we need 1/b + 1/c ≥ 1/2. That gives b = 2 (any c), or b = 3 with c ≤ 6, or b = c = 4. If b ≥ 5 the sum is at most 2/5.
- R = 1 exactly for (2,3,6), (2,4,4) and (3,3,3).
- A brute-force search with a ≥ 2 and c < 60 returns exactly (2,2,c), (2,3,3..6), (2,4,4) and (3,3,3).

**Same least entry.** The other two entries then share their sum and their reciprocal sum, hence their product, so x' = x.

**Different least entries.** If neither least entry is 1, the triples are (3,3,3) and a triple with least entry 2 and sum 9. That is (2,2,5) with R = 6/5 or (2,3,4) with R = 13/12, neither equal to 1. Correct.

**First discriminant, x' = (2,2,c').** sympy gives −3(c'−1)(c'+3) = 3(c'+3)(1−c'), which is negative for c' ≥ 2.

**Second discriminant, x' = (2,3,c').** Here bc = 6c'(c'+4)/(6−c'). The discriminant is (c'+4)(24 − 22c' − c'^2)/(6−c'), identical to the paper's expression. Its values at c' = 3, 4, 5 are −119, −320 and −999.

**Brute force, sums ≤ 200.** There are 380 groups of at least two triples with the same (S, R), giving 386 pairs. **None has R ≥ 1.** These counts also match the X = 200 row of Table 2.

## 2. Proposition 1 (Classes are points on a cubic): VERIFIED

- The rescaled triples (L/s_i)x_i are distinct because the x_i are pairwise non-proportional. With k ≥ 2 they are admissible by Lemma 1.
- **Primitivity:** if d divides every entry, then d | L/s_i for every i. So s_i | L/d for every i, hence L | L/d and d = 1.
- Any further members of the class cannot spoil primitivity.
- The claim that every common sum is a multiple of L is correct.

## 3. Proposition 2 (The pencil): VERIFIED

**Pencil and base points (sympy).**
- (x+y)(y+z)(z+x) = e1·e2 − e3, so C_Λ is the member t = 1 − Λ.
- All six base points lie on every C_Λ.
- T2, (1:0:0) and (0:1:0) have multiplicity 2. O, (0:1:−1) and (1:0:−1) have multiplicity 1. **Total 9.**

**Tangent at O.** The gradient at O is (−1, −1, Λ−1), so the tangent is x + y = (Λ−1)z. On it, F reduces to Λ(Λ−1)z^3, so O is a flex.

**The five lines.** Restricted to the lines, F becomes xy(x+y), Λxy(x+y), xz(x+z), (Λ−1)xy^2 and (Λ−1)x^2z. These give exactly the stated intersection sets, including the double point (1:0:0) on y + z = 0 and the double point T2 on x + y = 0. All the derived relations follow.

**Weierstrass model.**
- The maps C_Λ ↔ E_Λ send each curve onto the other, and both compositions are the identity on the curves.
- (1:4:4) at Λ = 27/2 maps to (−6, 45), as stated.
- Δ = 2^12 Λ^2 (Λ−1)^3 (Λ−9).
- c4 = 16(Λ−3)(Λ^3 − 9Λ^2 + 3Λ − 3) is 144, 256 and 2304 at Λ = 0, 1, 9, so it is nonzero there. Its degree is 4, so it does not vanish at ∞ either.
- So the order of Δ is 2, 3, 1 at Λ = 0, 1, 9 and 6 at ∞.

**Exact group law** on Λ = 27/2, 155/12, 49/4, 68/5, 7/3, −5/2 and 100/7:
- T2 has order 2; (0:1:−1) and (1:0:−1) have order 3; (1:0:0) and (0:1:0) have order 6.
- −A = (0:1:0), −Q = (1:0:−1), A = T2 + Q and 2A = 2Q = −Q all hold.

**Wording point (not a mathematical error).** The statement says "the first three coordinate points have intersection multiplicity 2". The list begins with O, which has multiplicity 1, so "the first three" reads wrongly. Suggested text: "the three coordinate points T2, (1:0:0), (0:1:0) have intersection multiplicity 2".

## 4. Lemma 2 (The egg), nonemptiness sentence: VERIFIED

- The point (1:1:t) lies on C_Λ exactly when 2t^2 + (5−Λ)t + 2 = 0.
- The discriminant is (Λ−1)(Λ−9), which is positive for Λ > 9.
- The roots have product 1 and sum (Λ−5)/2, both positive, so both roots are positive.
- The rest of the argument holds: the positive locus is compact and open, there are two real components, and O is not positive.

## 5. Proposition 3 (Reciprocation is a 2-torsion translation): VERIFIED

- The leading coefficient is p0 + p1. It is nonzero because the line x + y = 0 meets C_Λ only at T2 and O.
- The root product is p0p1, so the third intersection is R = (p0p2 : p1p2 : p0p1).
- F(ι(P)) = p0p1p2 · F(P).
- ι(P) − R = −(p0 − p1)p2 (1, −1, 0); the paper writes R − ι(P) = (p0 − p1)p2 (1, −1, 0). Either way O lies on the line through R and ι(P).
- O, R and ι(P) are distinct because p2(p0 − p1) ≠ 0 and p0p1 ≠ 0.
- Since O is a flex, ι(P) = −R = P + T2.
- Exact check on 175 random rational points: 0 failures.

## 6. Permutations paragraph: VERIFIED

- π(O) is O for x↔y, (1:0:−1) for y↔z, and (0:1:−1) for x↔z, as stated.
- The fixed points are as stated: (1:1:1) gives F = 9 − Λ, and (1:ω:ω^2) gives F = −Λ.
- α = −1 is justified, since −1 is the only automorphism of order 2, even for j = 0 or 1728.
- On the 175 random points, σ(P) = σ(O) − P for each transposition and π(P) = P + π(O) for each cyclic permutation, with π(O) of order 3: 0 failures.
- On C_{155/12}, the set {±P + T} has 12 elements. It equals the six orderings of (4,9,18) together with the six orderings of its dual (9,4,2).

## 7. Theorem 1 (Torsion): VERIFIED

**(i)** Correct application of Mazur's theorem.

**(ii)** The 2-torsion description is correct, and the discriminant is (Λ−1)(Λ−9).

**(iii)** The equivalence is correct.
- G = (1:r:r^2) gives 2G = (0:1:−1) + T2.
- The converse gives g1^2 = g0g2.
- Λ = (r + 1 + 1/r)^2.

**(iv)** The parity and coset argument is correct. Exact orders:
- For (u,v) ∈ {(1,4), (2,3), (5,2), (7,3), (1,2)}: (u:v:v) and (v:u:v) have order 6, and (v:v:u) has order 2.
- For r ∈ {2, 3, 3/2, 5/2, 1/4, −2, 7/3}:
  - G has order 12, 4G = (1:0:−1), 6G = T2 and 8G = Q.
  - The orderings are −G = (r:1:r^2), 7G = (r^2:r:1), 3G = (1:r^2:r), 9G = (r^2:1:r) and 5G = (r:r^2:1).
  - Order 4 occurs exactly for (1:r^2:r) and (r^2:1:r), the two orderings whose middle term is the last coordinate. The other four have order 12.

**PARI elltors** on the paper's model [0, Λ^2−6Λ−3, 0, 16Λ, 0] (PARI's discriminant matches Δ):

| Λ | elltors |
|---|---|
| 27/2, 10, 28/3, 35/3, 54/5, −18/7 | Z/2 × Z/6 |
| 49/4, 169/9, 9/4, 2401/225, 169/144, 4489/196 | Z/12 |
| 155/12, 68/5, 1849/120, 230/21, plus 30 random rationals | Z/6 |

46 curves in all, with 0 mismatches against the theorem's prediction.

## 8. Lemma 3 (Scaled copies) and N(X) = Σ ⌊X/S_D⌋: VERIFIED

The scaling k is the gcd of the six entries and is unique, and kD is again a pair. Hence N(X) = Σ_D ⌊X/S_D⌋.

## 9. Theorem 2 (The isosceles family): VERIFIED

**Algebra.**
- The common sum, the reciprocal sum g/(uv), g ∈ {1, 3} with g = 3 exactly when u ≡ v ≢ 0 (mod 3), and primitivity all hold.
- D_{1,4} = {(2,8,8), (12,3,3)} is the smallest pair.
- Checked exactly for every coprime pair with v < 200.

**Counting.**
- |Ω| = (1/6) log 2.
- In the Möbius step, Σ over d not divisible by 3 of μ(d)/d^2 = (6/π^2)(9/8).
- #U1 = 6 with t^2 = y, and #U3 = 2 with t^2 = 3y.
- Together: (6/π^2)|Ω|·(3/2)y, so c_iso = 3 log 2/(2π^2) = 0.1053457…
- The partial summation and the distinct-Λ argument (Λ = 5 + 2(u/v + v/u)) are correct.

**Numerics.**
- There are **506** pairs D_{u,v} with S ≤ 4800; c_iso · 4800 = 505.66.
- A_iso(y)/y = 0.10530, 0.10535, 0.10533, 0.10534, 0.10535 at y = 10^4, 10^5, 10^6, 10^7, 4·10^7.
- The number of copies k·D_{u,v} with sum ≤ 4800 is 2917 = **0.6077 X**.
- (copies − c_iso X log X)/X is −0.28597 at 10^4, −0.28621 at 10^5, −0.28628 at 10^6, −0.28628 at 10^7 and −0.28628 at 4·10^7. Every value on [10^4, 4·10^7] rounds to **−0.286**.

## 10. Threshold log X > 128π^4 c_iso/3 ≈ 438: VERIFIED

128π^4 c_iso/3 = 437.83.

## 11. Lemma 4 and Theorem 3 (One more logarithm): VERIFIED

**Lemma 4.**
- The displayed pair, the common sum W = (αu+βv)(u+αv), and the ratios √(qr), q^2/r, r^2/q all check out symbolically.
- In a brute-force search, multiplicity 6 is attained and never exceeded.
- Every primitive triple with entries ≤ 14 has the form (u, vq, vr).

**Theorem 3.**
- β/α ≥ 1/2, so U ≥ V/2. Also V^2 ≥ y^{5/8}/8, so V/2 ≥ 1 for large y.
- β/α ≤ α gives W ≤ y. Numerically, max W(U,V)/y = 0.625 at y = 10^8.
- UV = y/(4α^2), so each box contains (3/(2π^2))·y/α^2 coprime pairs.
- Σ φ(n)/(2n^2) ~ (3/π^2) log M.
- The total error O(M^3 √y log y) is o(y).
- c_A = 3/(32π^4).
- ⌊X/S_D⌋ ≥ X/(2S_D) when S_D ≤ X, and partial summation then gives the constant 3/(128π^4).

## 12. Theorem 4 (Classes of every size): VERIFIED

- Λ(4,9,18) = 155/12 > 9, and (4,9,18) is not a geometric progression in any order, so P has infinite order by Theorem 1(iv).
- P + T2 = (9:4:2) = ι(P).
- 3P = (162833463 : 723926268 : 287876366), exactly as stated.
- P, 3P, 5P and 7P are positive; 2P, 4P and 6P are not.

## 13. Section 5: C_{27/2}, ranks and root numbers: VERIFIED

| Curve | ellrank (r1, r2) | Root number |
|---|---|---|
| C_{27/2} | (0, 0) | +1 |
| C_{68/5} | (2, 2) | +1 |
| C_{1849/120} | (3, 3) | −1 |
| C_{230/21} | (3, 3) | −1 |
| C_{155/12} | (2, 2) | +1 |

C_{27/2} has torsion Z/2 × Z/6 and rank 0, so it has 12 rational points: the 6 base points plus the 3 orderings of each of (1,4,4) and (1,1,4), which are dual to each other. Table 1's rows are also consistent: common sums, common R, gcd 1, and the stated Λ values.

## 14. Ravi substitution: VERIFIED

sympy confirms R/r = 2abc/((a+b−c)(b+c−a)(c+a−b)) = abc/(4xyz) = (Λ − 1)/4.

## 15. Section 6.4: VERIFIED

- The defining equation has total degree 5. Where e1·e3 ≠ 0 it is equivalent to Λ(x) = Λ(x').
- The map (P, P') ↦ (e1(P')P, e1(P)P') is well defined projectively.
- Of the twelve surfaces, P + {O, ±Q} and −P + {O, ±Q} are the orderings of P, including the diagonal. Adding T2 gives the six dual-family surfaces. This was confirmed exactly on C_{155/12}.
- I did not check the Schoen citation [18, Prop. 7.1].

## Summary

| # | Item | Verdict | Notes |
|---|---|---|---|
| 1 | Lemma 1 and brute force to S ≤ 200 | VERIFIED | Discriminants exact. No R ≥ 1 coincidence; 386 pairs and 380 classes, matching Table 2. |
| 2 | Proposition 1 | VERIFIED | |
| 3 | Proposition 2 | VERIFIED | Wording: "the first three coordinate points" should read "the three coordinate points T2, (1:0:0), (0:1:0)". |
| 4 | Lemma 2, nonemptiness | VERIFIED | |
| 5 | Proposition 3 | VERIFIED | 175 random points, 0 failures |
| 6 | Permutations | VERIFIED | |
| 7 | Theorem 1 (i)–(iv) | VERIFIED | elltors matches on 46 curves; all orders confirmed |
| 8 | Lemma 3 and identity (2) | VERIFIED | |
| 9 | Theorem 2 and numerics | VERIFIED | 506 pairs; 0.6077X; −0.286X on [10^4, 4·10^7] |
| 10 | Threshold | VERIFIED | 437.83 |
| 11 | Lemma 4 and Theorem 3 | VERIFIED | |
| 12 | Theorem 4 | VERIFIED | 3P exact |
| 13 | C_{27/2}, ranks, root numbers | VERIFIED | |
| 14 | Ravi identity | VERIFIED | |
| 15 | Section 6.4 | VERIFIED | Schoen citation not checked |
