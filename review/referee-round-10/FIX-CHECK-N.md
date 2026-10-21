# FIX-CHECK-N (round 10): "Triples with Equal Sum and Equal Reciprocal Sum" (Integers PDF, 29 pp.)

Inputs: `paper/arith/integers/note.pdf` and `VERDICT-N.md` only. The scripts are in `review/referee-round-10/fixcheckN/scratch/`: `selmer.py`, `pari_check.py`, `checks.py`, `branch.py`, `enum.py`, `enum2.py`. Fetched literature is in `scratch/dl/`: Bremner–Macleod 2014 [4], its 2025 corrigendum [5], and Nguyen Xuan Tho 2021 [24]. Project Euclid blocked the download of Choudhry 2011 [11], so I could not check citations to [11] against the source.

## Task 1: fix check

| id | status | where | remaining fix |
|---|---|---|---|
| N1 Choudhry comparison | RESOLVED | p. 3 (l. 127–129); p. 4 (Thm C paragraph: [11, §5.1, (52)–(55)] chains on Λ = 0, mixed signs, and [11, §2]; novelty is positivity); p. 6 (the false clause is gone; [11, (3), p. 738] is the 2011 printing of the S = 26 and 34 pairs; Chen's "smallest" and "first known chains" are corrected to S = 18 and to a size-3 class at S = 136; the first solution is credited as the dual family and as the isosceles family at x = (u,v,v); (34)/(35) are described as the line through x and its cyclic shift; −(2P+τ) is never positive); p. 7 (novelty paragraph); p. 11 (Cor. 1 header); p. 15 (Thm 2); p. 16 (dual family "not new") | None. I could not check the page and equation numbers of [11] against the source. Everything I could recompute is correct: (4,10,12) is dual to (5,6,15); the pairs with S ≤ 34 are at S = 18, 20, 26, 31, 32, 34; the first size-3 class is at S = 136; (51,102,255) completes the S = 408 chain; the S = 573 chain is a whole class. |
| N2 Bremner–Macleod priority | RESOLVED | p. 7 | None. I checked the text against the fetched [4] (Task 2c). Optional: at Λ = 8 (M = 2), Δ < 0, so "its bounded real component" does not exist. The conclusion still holds because Λ < 9. "4M ≥ 12" or a short parenthesis would fix it. |
| N3 Theorem 3 demoted | RESOLVED | Abstract (dual-family bound removed; only the O(X(log X)^5) upper bound remains); p. 4 (Thm B is isosceles only; Prop. 4 is stated with its constant; X(log X)^5 is named as expected; the open point is whether the Frei–Loughran–Sofos lower bound holds on positive points); p. 18 (the same, stated precisely, "we do not claim it") | None |
| N4 Holdouts and precision | RESOLVED | Abstract, p. 5 and p. 25 are consistent ("data cannot locate it"; laws with exponent 1–1.3 fit almost equally well); no "evidence" wording is left anywhere; p. 23–24: overdispersion 6.3, cumulative fit "not an independent estimate", q to one decimal, sliding windows for q and β, b₀ ∈ {0.1, 0.2, 0.3} with deviance and both holdouts, the free 3-parameter fit | None. Optional wording on p. 24: "The excess grows steadily with b₀, and nothing singles out b₀ = 0" reads as self-contradictory, because steady growth does single out b₀ = 0 as best. Suggest: "the fit worsens only gradually with b₀, with no threshold at which a larger b₀ is rejected." |
| N5 §6.4 heuristic and line search | RESOLVED | p. 25–27: adjunction gives ω ≅ O; the a-invariant reading (planes a = 3, del Pezzo a = 1, quadratic surface a = 3/2); the dichotomy for third-kind pairs (83.5%); 53 of 189 lines through a base point, 136 informative | None. Optional: the "forced in advance" argument as written only covers a line compared with itself, through its Vieta involution. I checked (`branch.py`) that the 53 line classes have pairwise distinct branch-value sets, so cross-pairs reduce to permuted copies and the claim holds. One sentence saying so would close the gap. |
| N6 Descent checkable | RESOLVED | p. 19–20, Table 1 and text: Selmer groups, the generating points, the places tested (∞ and p \| 2b(a²−4b)); "the ranks are illustrative", since Thm 3 needs only Thm 1(iv) | None. Fully reproduced (Task 2b). |
| Minor items | RESOLVED (in spirit) | §1.4 is now split into topical paragraphs (p. 5–7); no regressions found in the pages read | I did not check the minor items one by one, because the reviewers' reports were outside the inputs. |

## Task 2: blind mathematical check

**(a) Choudhry (35) = −(2P+τ) is never positive. Correct.**
- Lemma 3 holds: the cyclic shift (x,y,z) → (y,z,x) sends O = (1:−1:0) to (1:0:−1) = τ, and τ has order 3.
- O is a flex, and the line through P and P+τ meets the cubic again in −(2P+τ).
- Any positive point has Λ ≥ 9. For real x with Λ(x) < 9, the curve C_Λ has no positive point at all.
- For Λ > 9:
  - The component group of C_Λ(ℝ) is ℤ/2, so 2P lies on the identity component.
  - τ has odd order, so it lies there too, and so does −(2P+τ).
  - The identity component has no positive point (Lemma 2).
- For Λ = 9:
  - The only positive real point is the node (1:1:1), by AM–HM.
  - A line through the node meets C₉ there with multiplicity ≥ 2, so it cannot also contain two further distinct points x ≠ σx.
  - The parenthetical "whose entries are distinct" is true for real points of C₉ other than the node and the base points: on C₉, x = y forces t = 1. The proof does not need it.
- Exact rational test (`checks.py`): 193 747 integer x with |xᵢ| ≤ 60 and all signs, 48 755 of them positive. The third intersection was never positive.

**(b) Table 1 descent. Fully confirmed.** `selmer.py` does its own local-solubility test: a Hensel-type recursion over ℤ_p for both affine charts, plus the real condition. It runs at ∞ and at every p | 2b(a²−4b).
- For all five Λ:
  - The values of a and b match the table.
  - Both computed Selmer groups match Table 1 element by element.
  - Every listed x gives x(x²+ax+b), or x(x²−2ax+a²−4b) on the isogenous curve, a rational square. Note that x = −9 at Λ = 27/2 is the 2-torsion point (y = 0).
  - Their square-free images, together with the images of (0,0), generate the Selmer groups.
- Ranks from 2^r = |S|·|S̄|/4 are 0, 2, 2, 3, 3. PARI `ellrank` (via cypari2) gives matching lower and upper bounds.
- PARI also confirms:
  - conductors 90, 6250530, 82110, 1715185290 and 41388270;
  - root numbers +, +, +, −, −;
  - torsion [6,2], [6], [6], [6], [6];
  - for C_{169/16}: rank 1, torsion ℤ/12.
- The values 6721, 1449, 1329601 and 8569 of (Λ−1)(Λ−9)·q² are correct, and none is a square.

**(c) Bremner–Macleod [4] Thm 5.1 for Λ = 4M ≥ 8. Verified against the fetched paper.**
- [4] Lemma 2.1 is the torsion statement.
- §4 (Thm 4.1) shows that positive solutions lie in a subregion of the egg.
- Thm 5.1 reads: "Suppose N ≡ 1 mod 2. Then (x,y) ∈ E_N(ℚ) implies x ≥ 0." Corollary 5.2 follows it.
- Their E_N is y² = x³ + (4N²+12N−3)x² + 32(N+3)x. This is the note's E_{2N+6}: Λ² − 6Λ − 3 and 16Λ match.
- In their proof (N+3 = 2M, M ≥ 2) the curve becomes y² = x(x² + (16M²−24M−3)x + 64M), which is exactly E_{4M}.
- For Λ > 9 both nonzero roots are negative (A, B > 0 and Δ > 0), so the egg lies in x < 0. The egg is the non-identity component, which carries the positive points by Lemma 2.
- So [4] gives "no positive rational point on C_{4M}", as the note says.
- [24] Thm 1.1 states "no positive integer solutions if 4 | n" and does not cite [4]. Both statements in the note are correct.
- The corrigendum [5] corrects Table 2 of [4], as the note says.

**(d) Numerical statements in §6.3–6.4 (and nearby). All reproduced.**
- **Lines** (`checks.py`): primitive (a,b,c) with |·| ≤ 7 whose line meets the open positive triangle, taken up to permutation and sign, give exactly 189 classes. Of these, 53 pass through one of the six base points. On all 53, Λ has degree 2.
- **Exactness bounds:**
  - e₂ ≤ S²/3 holds because e₁² − 3e₂ = ½Σ(xᵢ−xⱼ)² ≥ 0; brute-force check for S < 200.
  - e₃ ≤ (S/3)³ = 8·10⁹ < 2⁵³.
- **Brute-force enumeration to S = 600** (`enum.py`, `enum2.py`):
  - Table 3 rows 18 through 600 match: N, N_cl, primitive classes and largest class size.
  - A(500) = 1328.
  - 507 of the 582 sums carry a primitive class.
  - There are 1330 non-dual primitive pairs with S ≤ 600 and 669 with S ≤ 400.
  - The dual share for S ≤ 200 is 32.9%.
- **Derived numbers:**
  - Local exponents in Table 3: 2.069, 1.954, 1.868, 1.790, 1.713, 1.624, 1.585.
  - Local exponents of A: 1.64, 1.60, 1.51, 1.46.
  - N/X² = 0.0094 and 0.0040.
  - Deviance/degrees of freedom = 26479/4199 = 6.31.
  - 38624/46254 = 83.5% and 7626/46254 = 16.5%.
  - q/log s = β at s ≈ 2100.
  - N(6000) − N(4800) = 42 960.
- **§4 checks:**
  - There are 506 pairs D_{u,v} with S ≤ 4800, against c_iso·4800 = 505.66.
  - The copies number 0.6077X at X = 4800.
  - At X = 10⁶ the copies number c_iso X log X − 0.2863X.
  - 3/(128π⁴) = 2.41·10⁻⁴, and the crossover is at log X = 437.8.

I could not recompute the following cheaply: the 46 254 classification above S = 600, the deviance and holdout values, and the window fits.

## REQUIRED FIXES

None.

Optional:
1. p. 24: reword "nothing singles out b₀ = 0".
2. p. 26: add one sentence that the 53 base-point lines have pairwise distinct branch values, so the forcing argument covers every comparison made.
3. p. 7: "Λ = 4M ≥ 8" says "its bounded real component", but at Λ = 8 there is none; say ≥ 12 or add a parenthesis.

## Follow-up (applied after this check)

The three optional wording items were applied in `paper/arith/note.tex` and propagated to the Integers version: p. 24 now reads "the fit worsens only gradually with b₀, with no threshold at which a larger b₀ is rejected"; p. 26 states that the 53 base-point lines have pairwise distinct branch values (verified by this check's script); p. 7 says the bounded real component is present when M ≥ 3. Both builds are clean (23 and 29 pages).
