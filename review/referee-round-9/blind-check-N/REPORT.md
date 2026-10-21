<!-- Round 9 blind check N: returned text saved verbatim; the reviewer could not write files -->

I could not write `REPORT.md` (the write was refused), so the full report is below. Of the nine items, seven are correct as written, item 8 is half correct and half imprecise, and item 7 reproduces exactly as far as I could compute it (up to S = 1000).

All scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/blind-check-N/scratch/` and run in the virtual environment there (sympy, cypari2/PARI, scipy, plus one C program, `enum.c`). The only literature I fetched was the two arXiv versions of 1303.6705, by curl.

| Item | Verdict |
|---|---|
| 1. Proposition 2: extremal surface, Shioda–Tate, base changes | CORRECT (one standard step left implicit) |
| 2. Theorem 2: (2u+v)/g and (u+2v)/g coprime | CORRECT |
| 3. Proposition 4(i): Y(Q) nonempty via D(1,1,2) | CORRECT |
| 4. Smallest coincidences vs Chen Shuwen's | CORRECT |
| 5. Sadek–El-Sissi numbering | CORRECT for arXiv; published version not accessible |
| 6. Five planes carry about S² points | CORRECT ("components" is the wrong word) |
| 7. Holdouts, A(X), local exponents, wording | Exact match up to S = 1000; larger values not reproduced (cap); wording accurate |
| 8. One curve gives at most X^{1+o(1)}; bidegree (3,3) | First claim CORRECT; bidegree claim INCOMPLETE |
| 9. Odd multiples positive; Theorem 4 from any positive point of infinite order | CORRECT |

---

## Item 1: Proposition 2 (pencil, extremal surface, base changes)

**CORRECT, with one step left implicit.** Checked in `item1.py`:
- **Pencil identity:** (x+y)(y+z)(z+x) + (1−Λ)xyz = (x+y+z)(xy+yz+zx) − Λxyz holds.
- **Discriminant:** Δ = 2^12 Λ²(Λ−1)³(Λ−9).
- **c4:** c4 = 16(Λ−3)(Λ³−9Λ²+3Λ−3). It equals 144, 256 and 2304 at Λ = 0, 1, 9, so those fibres are I2, I3, I1.
- **Fibre at infinity:** in μ = 1/Λ the model is η'² = s'³ + (1−6μ−3μ²)s'² + 16μ³s', with Δ = 4096μ⁶(μ−1)³(9μ−1) and c4(0) = 16. That gives I6.
- **Euler numbers:** they sum to 12, as they must for a rational elliptic surface.
- **Maps:** the forward and inverse maps are verified symbolically. At Λ = 27/2, (1:4:4) maps to (−6, 45).
- **Base points:** there are six. The local intersection multiplicity is 2 at each coordinate point and 1 at the others, so 9 in all.
- **Shioda–Tate:** the rendered page reads "over Q̄(Λ)". Then 10 = 2 + r + 8 gives r = 0.
- **Base changes:** Λ(1:1:t) = 2t+5+2/t and Λ(1:r:r²) = (r+1+1/r)², both identically. These match Theorem 1(ii) and (iii).

**Gap (minor):** "rank 0, so its sections are the six base points" needs the Mordell–Weil group to have order exactly 6. The missing step is |MW|² = ∏m_v / |disc NS| = 6·3·2·1 = 36. Alternatively, cite the Oguiso–Shioda table, which gives Z/6 for I6 I3 I2 I1.

## Item 2: Theorem 2, coprimality

**CORRECT.**
- A common prime p of the two quotients divides 3u and 3v, so p = 3.
- Then 3 divides g, so g = 3, and 9 divides the sum 3(u+v). Hence u + v ≡ 0 (mod 3).
- g = 3 also means u ≡ v (mod 3). Together these give 3 | u, which contradicts u ≢ 0 (mod 3).
- The gcd of each member's entries really is (2u+v)/g, respectively (u+2v)/g.

An exhaustive check over all coprime 1 ≤ u < v < 400 found:
- g is always 1 or 3, and g = 3 exactly when u ≡ v ≢ 0 (mod 3).
- No case where the quotients share a factor.
- Every pair is primitive, with equal sums and R = g/(uv).

Also confirmed: A_iso(4800) = 506, against c_iso · 4800 = 505.66.

## Item 3: Proposition 4(i)

**CORRECT.**
- D(1,1,2) = (5,5,10,8,8,4): both halves sum to 20 and the gcd is 1. It is the dual pair {(5,5,10), (8,8,4)}.
- The five cubics have rank 5 and vanish at the five points. The sixth coordinate is y1+y2+y3−y4−y5.
- The quadrics through the image span a 2-dimensional space: y2y5 − y1y4 and −y1y3 + y1y4 − y2y3 − y3² + y3y4 + y3y5. That is the expected complete intersection of two quadrics in P⁴.
- Both quadrics vanish at (5:5:10:8:8).

## Item 4: Smallest coincidences

**CORRECT.** Exact enumeration for S ≤ 40 gives:

| S | R | Pair |
|---|---|---|
| 18 | 3/4 | (2,8,8), (3,3,12) |
| 20 | 1/2 | (4,8,8), (5,5,10) |
| 26 | 13/30 | (4,10,12), (5,6,15) (Chen Shuwen) |
| 31 | 5/12 | (4,9,18), (5,6,20) |
| 32 | 11/28 | (4,14,14), (5,7,20) |
| 34 | 13/42 | (6,14,14), (7,9,18) (Chen Shuwen) |

So the pairs at 18 and 20 are smaller than both of Chen's pairs. The pairs at 31 and 32 are the only ones strictly between 26 and 34, so they are smaller than the second.

## Item 5: Sadek–El-Sissi numbering

**CORRECT for the arXiv versions.**
- **Numbering:** in both v1 (26 Mar 2013) and v2 (6 Apr 2013), Proposition 2.5 is the order-6 statement, Proposition 2.6 the positive-rank statement and Theorem 2.7 the torsion statement.
- **"Stated for integers":** v1 states the results for nonzero integers and v2 for integers M, N with positive integers d1 > d2 > d3. The description is fair.
- **Extra hypothesis:** the condition d1(d2−d3)³ ≠ d3(d1−d2)³ is in v2 and absent from v1, as the note says.
- **Counterexample (3,10,24):** 24·7³ = 3·14³ = 8232, so the hypothesis fails. PARI on y² − 37xy − 720y = x³ gives rank [0,0] and torsion of order 12, so v1's Proposition 2.6 is false there.

The published Osaka J. Math. numbering (Prop. 2.7, Thm. 2.8) is unverified: Project Euclid returned a bot wall to curl, and the Osaka repository search needs JavaScript.

## Item 6: The five planes

**CORRECT, but one word is wrong.** For fixed S the pairs form a hypersurface in (a, b, a', b')-space, which is a threefold. Each plane x' = σ(x) lies on it. I counted the integer points on each of the five planes with max|coordinate| ≤ S, for S = 50, 100, 200 and 400:
- all integer points: about 2.01·S² on four planes and 4.01·S² on one;
- positive points: about 0.50·S².

So each plane does carry about S² points, and the argument stands. But the note calls the planes "its trivial components". They are surfaces inside a 3-dimensional hypersurface, not components of it; "trivial subvarieties" would be accurate.

## Item 7: Enumeration, holdouts, A(X), local exponents

**Everything I could compute matches exactly.** My own C enumeration covers every triple, including those with a = 1, for S ≤ 1000, grouping by the exact reduced fraction (7 s).
- **Lemma 1, empirically:** no coincidence involves a triple with R ≥ 1.
- **Table 3 up to 1000:** every row matches, including N(1000) = 7641, Ncl(1000) = 7386, 4040 primitive classes, and local exponent 1.790.
- **A(1000) = 4141 and A(500) = 1328.** The local exponent is log2(4141/1328) = 1.641, as stated.
- **Stated values above 1000:** log2(12512/4141) = 1.595 and log2(35567/12512) = 1.507 agree with the stated 1.60 and 1.51. The exponent 1.48 at 4800 needs A(2400), which I could not compute under the cap.
- **Other counts:** 32.9% of primitive pairs with S ≤ 200 are dual; there are 1330 non-dual primitive pairs with S ≤ 600; 507 of the 582 sums 19 ≤ S ≤ 600 carry a primitive class. All as stated.
- **Not reproduced because of the cap:** q = 4.49, β = 0.587, both holdout figures, and 42960 (which does equal 145679 − 102719).

**Scaled-down fits.** With per-sum Poisson fits:
- On [600,1000], q = 4.18, β = 0.625, and q = 3.52 for primitive pairs (the paper's primitive value on its window is 3.53).
- q moves a lot with the window: 4.63 on [300,1000] and 5.73 on [400,800].
- A three-parameter fit s^β(log s)^q cannot pin the parameters down; on [600,1000] it gives (β, q) = (−15.5, 107.7).

Small holdouts (prediction minus exact):

| Fit window | Holdout | Log-power law | Power law |
|---|---|---|---|
| [300,800] | 801–1000 | +5.10% | +6.67% |
| [300,700] | 701–1000 | −4.68% | −3.27% |
| [200,600] | 601–800 | −2.74% | −0.96% |

At this scale the two laws trade places depending on the window.

**Judgement on the wording:** "weak, non-asymptotic evidence", together with the caveat that a finite range bounds the exponent from neither side, is accurate, if anything generous. The paper's two holdouts overlap in their training data and compare only two particular two-parameter laws. Saying so explicitly would make the sentence more precise.

## Item 8: One curve, and the bidegree

**"A single curve contributes at most X^{1+o(1)}": CORRECT.**
- A rational curve given by degree-d forms with no common factor has ≪ y^{2/d} primitive points with S ≤ y. The gcd of the values divides the resultant, so it is bounded.
- Counting copies with Lemma 5 gives ≪ X log X for d = 2 and ≪ X for d ≥ 3.
- Curves of genus at least 1 have X^{o(1)} primitive points.
- d = 1 is excluded by Remark 1. If one triple has all entries proportional, Remark 1 applied to the other forces it to be proportional too, and the "curve" is then a single scaled pair.
- The "about X^{2/d}" in the parenthetical counts primitive pairs; with copies it becomes X log X, still within X^{1+o(1)}.

**"The correspondence {Λ(p) = Λ(p')} on two lines has bidegree (3,3)": INCOMPLETE.** It holds only for lines that avoid all six base points. On a line through a base point, Λ restricted to the line has degree 2 and the correspondence has bidegree (2,2). Lines through a base point can meet the positive triangle, for example:
- 2x + 3y = 7z (no base point): degree 3, bidegree (3,3) = diagonal (1,1) + residual (2,2).
- y = 2z (through the vertex (1:0:0)): factors t = t' and tt' = 2, the Vieta involution of the dual family.
- x + y = 3z (through (1:−1:0)): factor t + t' = 3, the swap of x and y.
- y + z = 4x (through (0:1:−1)): factor t + t' = 4, the swap of y and z.

The extra (1,1) components on lines through (1:−1:0), (0:1:−1) and (1:0:−1) are just coordinate swaps, so the paper's conclusion stands as long as the search treats permutations and the diagonal as trivial. The sentence should be qualified ("for lines avoiding the base points; lower otherwise"), and the exclusion of trivial components should be stated.

## Item 9: Theorem 4 discussion

**CORRECT.**
- **Lemma 2 proof:** the positive locus is open in C_Λ(R), compact because Λ → ∞ at the boundary of the triangle, and nonempty. Δ > 0 gives two real components, and O is not positive. So the positive points are exactly the non-identity component, and nP is positive exactly when n is odd.
- **Λ > 9 is automatic:** a positive point forces Λ ≥ 9, with equality only at (1:1:1), which I checked is a singular point of C_9.
- **The deduction:** odd multiples of a positive point of infinite order are infinitely many distinct positive points, at most six per unordered triple. Proposition 1 puts any k of them, from distinct permutation orbits, into one primitive class at L = lcm of their sums. L is unbounded, so there are infinitely many such classes.

Explicit checks with PARI, via the verified isomorphism to E_Λ:
- Λ(4,9,18) = 155/12, and the point has infinite order: rank [2,2], torsion Z/6.
- nP is positive for n = 1, 3, 5, 7 and not positive for n = 2, 4, 6.
- 3P = (162833463 : 723926268 : 287876366), exactly as printed.
- ι(P) = (9:4:2).
- (165,240,440) on C_169/16 has infinite order: rank 1, torsion of order 12.
