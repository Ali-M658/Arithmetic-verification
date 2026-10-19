<!-- Round 8 blind check N: returned text saved verbatim; the reviewer could not write files -->

# Blind check N: "Triples with Equal Sum and Equal Reciprocal Sum"

Writing `REPORT.md` was refused, so the full report follows.

Six of the seven items check out completely: items 1, 2, 3, 4, 6 and 7 are VERIFIED. Item 5 has one error: a single sentence on p. 3 about Λ = 10 leaves out half the torsion points. There is also one small wording mismatch in Section 5.

My scripts and data are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-8/blind-check-N/scratch/`:
- `sym.py`: sympy checks for items 1, 3, 4 and 5.
- `descent.py`: my own 2-isogeny descent with a p-adic local-solubility test, plus PARI through cypari2.
- `enum.c` and its output `per_s.txt`: the exhaustive enumeration in C.
- `fits.py`: the item 7 fits.
- `dl_bs/`: the Browning–Sofos paper, arXiv:1609.09057, fetched with curl.

For the items checked, the wording in `note-amsart.pdf` is the same as in `note.pdf`.

## 1. Proposition 4: VERIFIED

**Linear independence.** The six cubic forms are e2·a, e2·b, e2·c, e1·bc, e1·ca and e1·ab.
- Their coefficient matrix over the ten cubic monomials has rank 5, and the first five forms already have rank 5.
- I redid the paper's argument by hand and it is right: a²b, ab², b²c, bc² and a²c give λ1 = λ2 = μ1 = λ3 = μ2 = 0.

**The anticanonical model.**
- All forms vanish at the five points (1:0:0), (0:1:0), (0:0:1), (1:ω:ω²) and (1:ω²:ω).
- No three of the points are collinear. The line through the two non-real points is a+b+c = 0, which misses the coordinate points.
- The five points impose five independent conditions on cubics (rank 5), so the five forms span the cubics through them.
- So Y is the anticanonical image of the blow-up, a quartic del Pezzo surface in P⁴.

**Picard rank 5 over Q.**
- Galois only swaps E4 and E5, so the invariant part of Pic has rank 5. Y has rational points, for example D(1,4,4).
- This agrees with Browning–Sofos's formula ρ = 2 + δ0. The conic bundle |H − E1| degenerates over three closed points, all split: two rational ones and one of degree 2. So δ0 = 3.
- H − E1 has anticanonical degree 2, so it gives conics over Q, as claimed.

**The sixteen lines.**
- They are E1, …, E5, the ten lines through pairs of points, and one conic, which I confirmed is e2 = 0.
- Each of the six non-real lines has exactly one real point. For example, c = ωb meets the real plane only at (1:0:0).
- A positive triple has abc ≠ 0, e1 > 0 and e2 > 0, so it avoids all sixteen.

**Height comparison.**
- y6 = y1 + y2 + y3 − y4 − y5, so the gcd of five coordinates equals the gcd of six.
- After division the vector is the reduced pair, and every entry is at most S_D.
- Example: D(1,4,4) = (24, 96, 96, 144, 36, 36). Dividing by 12 gives height 12 ≤ 18.

**Browning–Sofos Theorem 1.1, checked against arXiv:1609.09057.**
- Its hypotheses: a quartic del Pezzo surface X over Q, X(Q) ≠ ∅, and a conic defined over Q.
- Its count: points of X minus the 16 lines, with the standard height on P⁴. The bound is of order B(log B)^(ρ−1) from above and below.
- The note's phrase "a rational point and a conic bundle" is equivalent here, and the height used is the right one. The application is correct, with ρ − 1 = 4.

**At most twelve points.** The count is correct, but the upper bound does not need it. Only "each pair has at least one point" and "a point determines the pair" are used. It is harmless.

**The O(X(log X)⁵) conclusion.** Partial summation is correct: A(y) = O(y(log y)⁴) gives Σ 1/S_D = O((log X)⁵).

## 2. Remark 1: VERIFIED

The proof is complete for homogeneous linear forms in (u,v).
- Positivity on the cone means the coefficients on any one line share a sign, so every charge is nonzero, for both x and x′.
- Linear independence of the functions 1/ℓ then gives the same lines with the same charges.
- Three lines: the entries match one by one.
- Two lines: comparing line by line gives {a′, b′} = {a, b}, or else (a+b)² = ab. That is impossible, because (a+b)² ≥ 4ab > ab when a and b have the same sign.
- The counterexample ℓ·(2,8,8), ℓ·(3,3,12) is correct.

## 3. Proposition 2: VERIFIED

**Symbolic checks, for general Λ.**
- Both maps land on the target curves, and both compositions are the identity modulo the curve equations.
- Δ = 2¹²·Λ²·(Λ−1)³·(Λ−9), as stated.
- c4 takes the values 144, 256 and 2304 at Λ = 0, 1, 9, all nonzero. So the fibres there are I2, I3 and I1.
- The example (1:4:4) at Λ = 27/2 does map to (−6, 45).

**The genus-one argument is sound.**
- For Λ ∉ {0, 1}, (x+y)/z is a Möbius function of s with determinant −4Λ(Λ−1) ≠ 0, and η is then recovered linearly. So the map E_Λ → C_Λ is birational onto its image.
- Lines and conics have genus zero, so the genus-one component must be the whole cubic, which is then smooth.

**The model at Λ = ∞.**
- The substitution μ = 1/Λ, s = s′/μ², η = η′/μ³ gives exactly η′² = s′³ + (1 − 6μ − 3μ²)s′² + 16μ³s′.
- Its discriminant is 2¹²·μ⁶·(μ−1)³·(9μ−1), so ord Δ = 6 at μ = 0.
- c4′ = 16 at μ = 0, so the fibre is I6. The orders 6 + 3 + 2 + 1 add up to 12, as they should.

## 4. Theorem 1(iv): VERIFIED

- The coset consists of the cyclic permutations of (1:1:t) and of ι(1:1:t) = (t:t:1).
- ι is defined at (1:1:t) because t ≠ 0. The two roots multiply to 1, so (t:t:1) = (1:1:1/t).
- Two of the six points coincide only if t = 1 or t² = 1. Those correspond to Λ = 9 and Λ = 1, which are excluded.
- Distinctness is automatic in any case: a coset of a group of order 6 has six elements.

## 5. Introduction facts: one error; the rest VERIFIED

**Error, p. 3 (amsart, line 99).** The sentence "For integer Λ > 9 the only positive torsion points are the orderings of (1:1:2), at Λ = 10" is incomplete.
- At Λ = 10 the roots are t = 2 and t = 1/2, so the positive torsion points are the orderings of (1:1:2) **and** of its dual (1:2:2).
- Direct check: for (1,2,2), e1·e2/e3 = 5·8/4 = 10.
- Theorem 1(iv)'s own proof lists both orderings, so this is a slip in the introduction only.
- **Suggested fix:** "the orderings of (1:1:2) and (1:2:2), at Λ = 10."

**"Only at Λ = 10" is correct.**
- Isosceles case: t = p/q with p, q dividing 2, so Λ is 9 or 10.
- Geometric progressions: r = ±1, so Λ is 9 or 1.
- A search over all p, q < 200 agrees.

**Bremner–MacLeod: VERIFIED.**
- Under (x,y,z) = (b+c, c+a, a+b), Λ = 2N + 6, so the problem lives on C_{2N+6}.
- At that Λ, Λ² − 6Λ − 3 = 4N² + 12N − 3 and 16Λ = 32(N+3). So their curve is exactly E_{2N+6}.
- I did not fetch their paper to compare against their printed equation.

**The classical identity: VERIFIED.** It is immediate in general; I also checked it symbolically for n = 3, 4 and 5.

## 6. Table 1 and the torsion of Table 2: VERIFIED

**Selmer groups.** My own local-solubility descent reproduces every entry of Table 1:

| Λ | Sel(α) | Sel(ᾱ) | rank |
|---|---|---|---|
| 27/2 | {±1, ±6} | {1} | 0 |
| 155/12 | 8 classes, as in Table 1 | {1, 6721} | 2 |
| 68/5 | {1, −5, −17, 85} | {1, 21, 69, 161} | 2 |
| 1849/120 | 8 classes, as in Table 1 | {1, 769, 1729, 1329601} | 3 |
| 230/21 | 16 classes, as in Table 1 | {1, 8569} | 3 |

- For every Selmer class I found an explicit rational point, so each Selmer group equals the image.
- PARI's `ellrank` gives the same ranks, with matching lower and upper bounds.
- Root numbers are +1, +1, +1, −1, −1, matching the rank parities.
- The conductors are 90, 6250530, 82110, 1715185290 and 41388270, as stated.
- PARI's `elltors` gives Z/2×Z/6 for 27/2 and Z/6 for the others.
- The integral model with a = p² − 6pq − 3q² and b = 16pq³ is correct.

**Torsion for Table 2.** 6721, 1449, 1329601 and 8569 are not squares, and none of the four Λ is a rational square. So the torsion is Z/6, by Theorem 1. For 27/2 the product is 225 = 15², giving Z/2×Z/6.

**Wording mismatch.** The text says the descent "gives the ranks 0, 2, 3, 3, and 2", but in Table 1's row order the ranks are 0, 2, 2, 3, 3. Stating them in table order, or naming the curves, would fix it.

## 7. Section 6.3: VERIFIED, every number reproduced

**Enumeration.** For each S ≤ 6000, my C program enumerated all triples with 1 ≤ a ≤ b ≤ c. It grouped them by e2/e3, sorting on the double value and confirming every match by exact 128-bit cross-multiplication.
- No coincidence involves a non-admissible triple, which confirms Lemma 1 numerically.
- The triple counts are 3,067,197,199 up to 4800 and 5,992,496,499 up to 6000, as stated.
- All 13 rows of Table 3 match for both pairs and classes, from 1/1 at X = 18 to 102719/98742 at 4800 and 145679/140005 at 6000.
- Up to 4800 there are 96981, 1627, 122, 11 and 1 classes of sizes 2 to 6. The first classes of sizes 3–6 are at S = 136, 408, 1849 and 4600, and no class of size 7 or more appears up to 6000.
- N(6000) − N(4800) = 42,960.

**Fits.** Poisson maximum likelihood on 600 ≤ s ≤ 4800:

| Quantity | Recomputed | Stated |
|---|---|---|
| q, all sums | 4.4887 | 4.49 |
| q, gcd(s,6) = 1 | 4.0608 | 4.06 |
| q, s odd | 4.2893 | 4.29 |
| q, s even | 4.6086 | 4.61 |
| q, 6 divides s | 4.9664 | 4.97 |
| β (power law) | 0.5868 | 0.587 |
| Tangency point | about 2098 | about 2100 |

The other numbers in the section also match:
- **Window fits:** [1200, 4800] gives 4.437, [600, 2400] gives 4.642 and [2400, 4800] gives 4.390 (stated 4.44, 4.64 and 4.39).
- **Primitive pairs:** 3.532 per sum (stated 3.53).
- **Cumulative fits:** 4.557 for all pairs and 3.625 for primitive pairs (stated 4.56 and 3.63).
- **Out of sample, sums 4801–6000:** the log-power law over-predicts by 0.25% and the power law by 2.33%, as stated.

I did not check the dual / non-dual breakdown of the fits (2.56, 3.33, 3.73 and 4.80); it was not in the list.
