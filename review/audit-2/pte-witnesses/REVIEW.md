# G5-bis blind review: group `pte-witnesses`

This review re-derives the results from the statements in `review/audit-2/statements/pte-witnesses.md`
and the context files that bundle names. I did not open any proof, script or data of the producing
sessions. Every number below comes from my own exact code in this folder. All `check_*.py` exit
nonzero on failure. Each `.txt` was produced by running its script. Interpreter:
`/opt/homebrew/Caskroom/miniforge/base/bin/python3` (sympy 1.14).

## Summary table

| id | statement | grade | one line |
|---|---|---|---|
| PW.4 | the 18 claimed pairs | **NONE** | All 18 verified. Both sides hyperbolic. Areas exact and equal to the printed values. Signatures and cone multisets distinct. c_1..c_L equal and c_{L+1} different, computed directly from the heat coefficients; the P_j criterion agrees. T, ι and cone counts as claimed. |
| PW.0 | headline table + item 6 (T_3) | **MINOR** | Every number in the table is reproduced. The T_3 search claim is confirmed by my own complete search (N = 220). "Real solutions exist in abundance" is vague: they exist (an open set), but only 635 of the 98,280 integer Y ≤ 24 give one. |
| PW.1 | Example (Small pairs), Remark (first open case) | **SERIOUS** | "Previously the smallest area known to share three coefficients was 2π·14/5" is contradicted by the paper's own Theorem C(3). Its n = 4 witness is this very pair, (0;3,10,15,30) ~ (0;4,5,21,28), of area 2π·22/15. Every other number is verified, and the remark is confirmed. |
| PW.2 | improved lower bounds on f | **MINOR** | The logic f(A) ≥ L+1 for A ≥ A_L is correct (both orbifolds are in Sig, and K_mult counts genus). The table and the rounding are safe; exact margins are below. "Area/2π ≈ T/2−2" fails for L = 2, 3. "f grows at least linearly for A/2π ≤ 18" has no content on a bounded range and fails at slope 2 for L = 6, 7. |
| PW.3a | counts "25 ... entries ≤ 130, 61 ... entries ≤ 220" | **MINOR** | As worded (all four entries ≤ N), the counts are **15** and **35**. The numbers 25 and 61 are reproduced exactly for the family {a,b,c,−(a+b+c)} with \|a\|,\|b\|,\|c\| ≤ N, where the fourth entry is unrestricted. |
| PW.3b | "So Theorem C(3) at n = 4 is a pencil phenomenon" | **SERIOUS** | False as a characterisation. My exhaustive direct search (orders ≤ 440) finds 107 primitive n = 4 witnesses, 6 of them **not** pencil configurations. The smallest is (0;16,16,74,74) ~ (0;11,37,44,88), with orders ≤ 88. |
| PW.3c | n = 5: "1,592 primitive 5-sets with entries ≤ 200, no pair" | **MINOR** | With all entries ≤ 200 there are **602** sets (301 up to sign). 1,592 is the family with at least three entries in [−200,200], counting A and −A separately. The substantive claim (no pencil pair) is TRUE in all three readings. |
| PW.3d | smallest witness {3,10,15,30} ~ {4,5,21,28} from A, B | **NONE** | Verified. Chen's "A.685" could not be located in the fetched text extraction (logged as an instrument gap for the literature group). |
| PW.5 | the 61 listed configurations | **MINOR** | All 61 verified: primitive, no {z,−z}, s1 = s3 = s_{−1} = 0, 4+4, entries ≥ 2, pairwise inequivalent. Each shares **exactly** 3 coefficients and is a pencil. "ALL" holds for the corrected description (one entry unrestricted) and fails for the printed one ("all entries of absolute value ≤ 220": 35 configurations). |
| T_3 (PW.0 item 6, rem:ptet3) | no size-8 genus collision with five-element side ≤ 220 | **NONE** | Re-derived the shape (3,5). Ran my own exhaustive search over all 4,493,032,544 multisets Y ≤ 220, with a certified 16-prime filter. 0 survivors, coverage proved complete. Planted controls were recovered at y5 = 8 and at y5 = 220. |

## Contamination

None. I read only `review/audit-2/REVIEWER-BRIEF.md`, `review/audit/G5-VERDICT.md`, my bundle,
`review/audit/statements/{signatures,audibility}.md`, `review/audit-2/statements/pte-structure.md`
(PS.0–PS.5, as the brief instructs), the `prop:heatinput` block of
`review/audit-2/statements/trace-formula.md` (named by my bundle), a `grep` of `review/audit-2/STATEMENTS.md`
for line anchors, and `review/audit-2/sources/`. G5-VERDICT item 3 mentions the pair
{3,10,15,30}/{4,5,21,28}; that file is allowed reading.

## Instrument gaps

- Chen, arXiv:2506.11429: the entry "A.685, type (−1,1,3)" and the identity [1,5,5]=[2,3,6]
  could not be found in `sources/chen_survey_2506.11429.txt` by grep (see `fetches.md`). The numbers
  themselves were re-verified exactly. Their provenance is for the literature group.
- The recipes of W02–W17 (BI/BLP/Chen/CMSV origin, "the doubling above") are withheld from this bundle,
  so their provenance was not checked. The pairs were verified directly from the printed orders.
- `data/witnesses.json` and `data/pencil_log.txt` are cited by the statements. They are forbidden
  reading and were not opened.

---

## 0. The heat-coefficient convention used throughout (`heatlib.py`, `check_heat.py`)

DF.1 and `prop:heatinput` give
tr e^{−tΔ} ~ Σ_{j≥1} c_j t^{j−2}, with c_1 = Area/4π and
c_j = α_{j−1}·Area/4π + Σ_i b_{j−2}(m_i). Here

- b_l(m) = (−1)^l p_l(m)/m;
- p_l(m) = 4^{−l} Σ_k (2k)!/(k!(l−k)!) m φ_k(m);
- Φ_m(u) = (cot u − m cot mu)/(4m sin u) = Σ φ_k(m) u^{2k}.

**Derivation of φ_k as a polynomial.** From the Laurent series cot u = Σ_{n≥0} c_n u^{2n−1}, with
c_n = (−1)^n 2^{2n} B_{2n}/(2n)!, we get cot u − m cot mu = Σ_{n≥1} c_n(1−m^{2n}) u^{2n−1}. The n = 0 terms
1/u − m/(mu) cancel. Also 1/sin u = Σ d_n u^{2n−1}, with d_n = (−1)^{n+1}2(2^{2n−1}−1)B_{2n}/(2n)!. Hence

m φ_k(m) = ¼ Σ_{n=1}^{k+1} c_n d_{k+1−n}(1−m^{2n}).

This is an even polynomial vanishing at m = 1.

**Checks (exact).**
- p_l is even, of degree 2l+2, with p_l(1) = 0 and leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)) (l ≤ 12).
- b_0(m) = (m²−1)/(12m).
- b_l(m) agrees **exactly** with Uçar (4.25)+(4.33) at κ = −1 for l ≤ 12, m ≤ 40. I re-implemented his formulas
  from the fetched text: c^S_ℓ(π/k) = (1/4k)·((−1)^ℓ/(ℓ+1)!)·(1/(2ℓ+1))·Σ_j C(2ℓ+2,2j)(k^{2j}−1)B_{2j}B_{2ℓ+2−2j}(½), and
  b_ν = Σ_ℓ 2/(4^ℓ ℓ!) c^S_{ν−ℓ} κ^ν.
- α_k agrees exactly with Uçar (4.35) for k ≤ 13.
- First values: p_1 = (m⁴+10m²−11)/360 and α = 1, −1/3, 1/15, −4/315, 1/315.
- As a non-certificate (mpmath, 50 digits), the closed form of Φ_m agrees with the trigonometric sum and with the series for m ≤ 8.

Output: `check_heat.txt` (ALL OK).

---

## PW.4: the 18 pairs. Grade **NONE**

**Method (`check_pairs.py`, which parses the bundle verbatim).** For each pair:

1. **Hyperbolicity.** g ≥ 0, every order is an integer ≥ 2, and Area/2π = 2g−2+Σ(1−1/m_i) > 0 (χ < 0). Every closed
   orientable 2-orbifold with χ < 0 is good and hyperbolic (DF.1: "carries a hyperbolic metric exactly when χ < 0").
2. **Equal area**, equal to the printed rational, computed exactly.
3. **Distinct signatures**, and in fact distinct cone multisets.
4. **Exactly L shared coefficients.** I computed c_1,…,c_{L+2} from §0 and counted the leading agreements.
   The result is L for all 18 pairs: c_{L+1} differs, with numerators of up to 558 digits.
5. **The criterion** (equal area and Ψ_k = P_{2k−1}−R equal for k < L) gives the same L.
6. **[Sig] Lemma 4 padding.** d = R(m')−R(m) is an integer. Pad with 1s, cancel common elements to get U*, V*,
   and check s_{−1} = s_1 = … = s_{2L−3} = 0 ≠ s_{2L−1} on Z = U* ⊎ (−V*). Then T = |U*|+|V*|,
   ι = |U*|−|V*| = 2(g'−g), and the cone counts.

**Result.** All 18 pass every check.

| W | L | T | ι | cones | Area/2π |
|---|---|---|---|---|---|
| 00 | 2 | 6 | 2 | 4 vs 1 | 14/15 |
| 01 | 3 | 10 | 2 | 6 vs 3 | 14/5 |
| 02–05 | 4–7 | 16, 20, 26, 40 | 2 | as printed | ≈ 6.99990, 8.999998, 12−, 19− |
| 06–11 | 2–7 | 6, 8, 14, 18, 24, 40 | 0 | equal | 1/4, 22/15, 5−3.27e−11, 7−3.4e−16, 10−4.3e−20, 18−5.7e−42 |
| 12–17 | 2–7 | 8, 16, 24, 46, 60, 72 | 0 | as printed | 2/5, 113/30, 8.281, 18.596, 26.559, 32.309 |

In the cone pairs exactly one padding 1 occurs, which is what produces the different cone count
(PS.0 Lemma 1.2(3)). Output: `check_pairs.txt`.

**Adversarial notes.**
- L = 2 is the smallest L tested. The order-15 single cone of W00 is the n = 1 edge case; it is hyperbolic since g = 1.
- No pair has equal cone multisets, so all 18 also witness K_mult in the sense of DF.2.
- The balanced pairs satisfy Lemma 1.2(5): Area/2π < T/2−2.

---

## PW.0: headline table and item 6. Grade **MINOR**

**Table.** Reproduced from the 18 pairs (`check_pairs.txt`, "Derived numbers"):
- least area among the listed pairs: 1/4, 22/15, then 4.99999999997, 7−3.4e−16, 10−4.3e−20, 18−5.7e−42;
- genus-pair T: 6, 10, 16, 20, 26, 40;
- genus-0 cone counts: 3/4, 7/8, 11/12, 22/23, 29/30, 35/36;
- Thue–Morse bound 4^{L−1}−1: 3, 15, 63, 255, 1023, 4095.

All are correct.

**Item 6.** "T_3 ∈ {8,10}" is correct:
- T ≥ 2L+2 = 8 and T is even (Theorem S, Lemma 1.2(4));
- W01 is a genus collision of size 10 sharing exactly 3 coefficients.

The search claim is confirmed (section T_3 below).

"Real solutions of that shape exist in abundance" (check_t3_real.py):
- real (3,5) solutions **exist**, e.g. Y = {1,1,1,1,7}, X ≈ {0.2664, 4.2830, 6.4506};
- the condition disc > 0 is open, so they form an open set;
- for integer Y with entries ≤ 24 (exact discriminant), only 635 of 98,280 multisets (0.65%) admit a real X.

"Abundance" is unquantified, and the evidence shows that real solutions are rare among small integer Y.

**Required wording** (proof.md §0 item 6). Replace "Real solutions of that shape exist in abundance, so
the obstruction, if there is one, is arithmetic." with:

> "Real solutions of that shape exist: they form a nonempty open set (for example $Y=\{1,1,1,1,7\}$ admits three positive real $x$). So the obstruction, if there is one, is arithmetic."

Also replace "whose 5-element side, made primitive, has entries $\le220$" with:

> "whose 5-element side, scaled to coprime integers, has entries $\le220$"

The search covers that set, and more (section T_3).

---

## PW.1: Example (Small pairs) and Remark (first open case). Grade **SERIOUS**

Verified numbers (`check_pairs.txt`):
- (0;3,10,15,30) ~ (0;4,5,21,28) has area 2π·22/15 and shares exactly 3 coefficients;
- (1;15,15,15) ~ (0;3,3,5,7,7,21) has area 2π·14/5 and shares exactly 3;
- (0;4,4,5,5,6,12,12) ~ (0;2,2,2,3,10,10,10,10) shares exactly 3, with 7 vs 8 cones;
- [1,5,5] and [2,3,6] have equal s_1 = 11 and s_3 = 251 (s_2 = 51 ≠ 49), i.e. equal sums of odd powers;
- the L = 4..7 equal-count genus-0 pairs have area strictly below 2π·5, 7, 10, 18;
- the genus 1/0 sizes are 16, 20, 26, 40, against 2^{2L−1} = 128, 512, 2048, 8192.

**Finding (SERIOUS).** "Previously the smallest area known to share three coefficients was
2π·14/5" is false within the paper itself. (0;3,10,15,30) ~ (0;4,5,21,28) is the n = 4 witness of
Theorem C(3) (audibility.md AU.4: {3,10,15,30}, {4,5,21,28}, R = 8/15, S_1 = 58, P_3 = 31402). Sharing
I_3 = (R, P_1, P_3) at equal cone count means sharing the first three heat coefficients (AU.0; [Sig]
Lemma 4 with d = 0). The pair of area 2π·22/15 was therefore already in the paper, and PW.3 itself
says so. The sentence would present a result of the same paper as an improvement on 14/5. This
belongs to the class of G5 SERIOUS item 3 (a remark contradicting Theorem C).

**Required wording** (statements.tex `ex:ptepairs`, first item). Replace "Previously the smallest area
known to share three coefficients was $2\pi\cdot\frac{14}5$, for $(1;15,15,15)$ and $(0;3,3,5,7,7,21)$."
with:

> "This is the $n=4$ witness of Theorem~C(3). Its area is less than that of the smallest genus-changing pair sharing three coefficients found here, $(1;15,15,15)$ and $(0;3,3,5,7,7,21)$, of area $2\pi\cdot\frac{14}5$."

The same applies to any "previously 2π·14/5" in proof.md or in the headline.

**Remark rem:ptet3.** Confirmed: the shape and the search (section T_3). Make the wording change
"made primitive" → "scaled to coprime integers" as in PW.0. "Real solutions of this shape exist" is
correct as printed here.

---

## PW.2: improved lower bounds on f. Grade **MINOR**

**Logic.** f(A) = max{K_mult(O;Sig) : Area(O) ≤ A}. Suppose O, O' ∈ Sig have σ(O) ≠ σ(O'), equal area A_L
and H_L(O) = H_L(O'). Then k = L fails the defining condition of K_mult(O;Sig) (DF.2), and the condition
is upward closed, so K_mult(O;Sig) ≥ L+1. Since Area(O) = A_L ≤ A, f(A) ≥ L+1.

This needs O' ∈ Sig, i.e. hyperbolic: checked for all 18. It does not need σ to differ in the cone
multiset, since K_mult determines the signature. The proof uses the pair sharing **at least** L
coefficients, so pairs sharing more are allowed.

**Table.** The thresholds are 1/4, 22/15, 5, 7, 10, 18. The [Sig] N1 row 3, 15, 63, 255, 1023, 4095
is correct: ⌊log_4(s+1)⌋+2 ≥ L+1 ⟺ s ≥ 4^{L−1}−1, valid for A ≥ 6π (s ≥ 3). Rounding up to the integer
is safe, because A_L/2π lies strictly below it. The exact margins are 3.27·10⁻¹¹, 3.4·10⁻¹⁶,
4.3·10⁻²⁰ and 5.7·10⁻⁴² (fractions in `check_pairs.txt`). "A_4/2π = 4.99999…" is correct
(4.999999999967).

**"Area/2π ≈ T/2−2 with T ≤ 4L−2 for L ≤ 5."**
- T ≤ 4L−2 holds: T = 6, 8, 14, 18 against 6, 10, 14, 18.
- "≈" is false for L = 2 (1/4 vs 1) and L = 3 (22/15 vs 2). It holds for L = 4..7.
- What is true for every balanced pair is the strict inequality Area/2π < T/2−2 (Lemma 1.2(5), checked).
- Together with T ≤ 4L−2 this gives the clean statement **A_L/2π < 2L−3 for 2 ≤ L ≤ 5**, hence
  f(A) ≥ L+1 for A/2π ≥ 2L−3 (L ≤ 5). This part is justified.
- For L = 6, 7 the thresholds are 10 and 18, not 2L−3 = 9 and 11 (T = 24, 40 > 4L−2).

**"So for A/2π ≤ 18, f grows at least linearly."** This has no content: any nondecreasing function is
bounded below by some linear function on a bounded interval. Read as slope 2, it fails beyond L = 5.

**Required wording** (proof.md lines 468–470). Replace the last paragraph with:

> "For the balanced pairs, Area$/2\pi<T/2-2$ (Lemma 1.2(5)), and $T\le4L-2$ for $L\le5$. Hence $A_L/2\pi<2L-3$ and $f(A)\ge L+1$ for $A/2\pi\ge2L-3$, $2\le L\le5$. For $L=6,7$ the thresholds are $A/2\pi\ge10$ and $18$."

---

## PW.3 / PW.5: pencil witnesses at n = 4 and the n = 5 claim

**Derivation (pencil, m = 4).** Let A, B be 4-multisets of nonzero rationals with e_1 = 0 and equal
e_3, e_4. Then:
- s_1(A) = s_1(B) = 0;
- s_3 = e_1³ − 3e_1e_2 + 3e_3 = 3e_3 for both;
- s_{−1} = e_3/e_4 for both.

So Z = A ⊎ (−B), after cancelling ±pairs, has s_1 = s_3 = s_{−1} = 0: a 3-configuration of size ≤ 8.
If it has four positive and four negative entries, U = Z_{>0} and V = −Z_{<0} are positive 4-multisets
with equal R, P_1 and P_3. These are equal area and equal Ψ_1, Ψ_2, so the two genus-0 4-cone
orbifolds share their first three coefficients ([Sig] Lemma 4 with d = 0). This is exactly
integer sharpness of Theorem A at n = 4 (AU.1). They share exactly three, because P_5 differs; by
Theorem A, four would force U = V.

For primitive integer A and B, a rational λ with e_3(λB) = e_3(A) and e_4(λB) = e_4(A) exists iff
e_3(A)⁴/e_4(A)³ = e_3(B)⁴/e_4(B)³. It is then λ = e_4(A)e_3(B)/(e_3(A)e_4(B)). Two edge cases:
- A and −A always share the invariant, but λ = −1 makes λ(−A) = A, so this trivial pair is excluded;
- e_3 = 0 forces A = {u,−u,v,−v}, which cancels completely.

**Part 1: the 61 listed configurations (`check_pencil61.py`, Part 1).** Each listed Z:
- is primitive, has no {z,−z} pair, has s_1 = s_3 = s_{−1} = 0, and has exactly 4 positive and 4 negative entries, all |z| ≥ 2;
- gives hyperbolic orbifolds of equal area that share **exactly 3** coefficients (direct c_j, and the criterion);
- is pencil-decomposable;
- is distinct from the other 60 modulo scaling and negation.

All 61 pass.

**Part 2: own enumeration (`check_pencil4.c`, exact int64 and __int128; `check_pencil61.py`, Part 2).**
I enumerated every primitive 4-multiset with e_1 = 0 and nonzero entries, identifying A with −A, and
grouped them by J = e_3⁴/e_4³ as a reduced __int128 fraction. For every pair in a class I formed Z and
canonicalised it. An independent pure-Python enumeration reproduces the N = 130 result exactly.

| reading | N = 130 | N = 220 |
|---|---|---|
| as worded: all four entries in [−N, N] | **15** | **35** |
| {a,b,c,−(a+b+c)}, \|a\|,\|b\|,\|c\| ≤ N, fourth entry unrestricted | **25** | **61** = exactly the listed set |

Every configuration generated in either reading is in the list. Every listed Z has a pencil split
with at least one primitive side ≤ 220, and 35 of them have a split with both sides ≤ 220.

### PW.3a / PW.5: grade **MINOR**

The counts are right for a family other than the one stated. Required wording, in PW.3 (proof.md
253–255) and the PW.5 generator description:

> "finds 25 distinct configurations from 4-sets $\{a,b,c,-(a+b+c)\}$ with $|a|,|b|,|c|\le130$ (the fourth entry unrestricted), and 61 with $|a|,|b|,|c|\le220$ (with all four entries $\le130$, resp. $\le220$, there are 15, resp. 35)."

### PW.3d: smallest witness. Grade **NONE**

- A = {−30,−3,5,28} and B = {−21,−4,10,15} have e_1 = 0, e_3 and e_4 equal with λ = 1, and e_2 = −859 ≠ −391.
- A ⊎ (−B) gives {4,5,21,28} and {3,10,15,30}.
- This is the smallest listed configuration by maximal entry, and the AU.4 witness.

### PW.3b: "So Theorem C(3) at n = 4 is a pencil phenomenon". Grade **SERIOUS**

**Direct search for n = 4 witnesses, independent of the pencil** (`check_direct4.c`, `check_direct4.py`):
- all pairs m ≠ m' of 4-multisets of positive integers ≤ 440 with equal R, P_1, P_3, exhaustive
  (1,583,091,510 multisets, per-sum checkpoints, every sum 4..1760 marked done);
- 193 collisions, i.e. **107** primitive configurations, each re-verified to share exactly 3 coefficients;
- all 61 listed configurations are among them (the list's maximum entry is 440);
- for each Z, all 35 splittings into 4+4 were tested for the pencil condition. **6 are not pencil configurations:**

```
(0;16,16,74,74)          ~ (0;11,37,44,88)          R=45/296, P1=180, P3=818640
(0;11,21,99,99)          ~ (0;9,51,51,119)
(0;17,17,88,136)         ~ (0;11,52,52,143)
(0;77,88,182,208)        ~ (0;68,112,154,221)
(0;154,175,308,350)      ~ (0;143,200,280,364)
(0;22,50,209,418)        ~ (0;19,85,170,425)
```

Counts by bound:

| max entry ≤ | witnesses | not pencil |
|---|---|---|
| 88 | 9 | 1 |
| 130 | 16 | 2 |
| 220 | 33 | 3 |
| 440 | 107 | 6 |

The first non-pencil witness has orders ≤ 88, inside the range of the claimed search. The recorded
witness is a pencil, but n = 4 integer sharpness as a phenomenon is not only a pencil phenomenon.

The pencil list is also far from all witnesses: 46 primitive witnesses with orders ≤ 440 are not in
it. That is not claimed, but it should not be implied.

**Required wording** (proof.md line 260). Replace "So Theorem C(3) at $n=4$ is a pencil phenomenon."
with:

> "So the recorded witness of Theorem C(3) at $n=4$ is a pencil configuration. Not every witness is: $(0;16,16,74,74)$ and $(0;11,37,44,88)$ share $R=45/296$, $P_1=180$, $P_3=818640$, and their configuration admits no pencil splitting."

### PW.3c: the n = 5 claim. Grade **MINOR**

Enumeration (`check_n5.c` exhaustive in C; `check_n5.py` independent in Python): primitive 5-multisets
of nonzero integers with s_1 = s_3 = 0.

| reading | count, A and −A separate | up to sign |
|---|---|---|
| all \|x\| ≤ 200 | **602** | 301 |
| at most one \|x\| > 200 | 674 | 337 |
| at least three entries in [−200, 200] | **1,592** | 796 |

**Pencil at m = 5** (r = 5, k_0 = 2). The invariant is J = e_4⁵/e_5⁴. A and −A always share it, with
λ = −1. In the largest family every J-class has exactly 2 members, {A, −A}, and no set has e_4 = 0. So
there is **no non-trivial pencil pair** in any of the three families. The claim holds; only the count
is misdescribed.

The step "such a pair would give integer sharpness at n = 5" is correct: the size is 10 = 2·4+2 by
Theorem S, ι = 0, and the two sides are positive 5-multisets sharing I_4.

**Required wording** (proof.md line 265). Replace "Among all 1,592 primitive 5-sets with entries
$\le200$" with:

> "Among all 1,592 primitive odd symmetric 5-sets with at least three entries in $[-200,200]$ ($A$ and $-A$ counted separately; 602 have all entries in $[-200,200]$)"

---

## T_3 (PW.0 item 6, rem:ptet3): the size-8 search. Grade **NONE**

### Shape (3,5): re-derivation of the Descartes bound |ι| ≤ T − 2L

Let Z be an L-configuration of size T, and Q(z) = ∏_{ζ∈Z}(z−ζ) = Σ(−1)^k e_k z^{T−k}.
- By the parity lemma (AU.2), s_j = 0 for odd j ≤ 2L−3 gives e_k = 0 for odd k ≤ 2L−3.
- s_{−1} = e_{T−1}/e_T = 0 gives e_{T−1} = 0.
- So the odd part Q_o(z) = (Q(z)−Q(−z))/2 contains only e_k with k odd and 2L−1 ≤ k ≤ T−3:
  at most M = (T−2L)/2 monomials. It also has a zero of order ≥ 3 at 0.

On the imaginary axis put W(it) = Q(it)/Q(−it). Each factor has modulus 1, and
W(it) = exp(iθ(t)) with θ(t) = −2Σ_{x∈Z>0} arctan(t/x) + 2Σ_{y∈−Z<0} arctan(t/y).
- θ(0) = 0 and θ(∞) = −πι.
- Q is real, so Q(−it) is the conjugate of Q(it). Hence W(it) = 1 iff Q(it) is real iff Q_o(it) = 0.
- Q_o(it) = (it)^a S(−t²), where S has ≤ M terms. By Descartes it has ≤ M−1 roots t > 0.
- θ is continuous and must pass every multiple of 2π strictly between 0 and −πι: there are |ι|/2 − 1 of them.

Hence |ι|/2 − 1 ≤ M − 1, i.e. |ι| ≤ T − 2L.

For L = 3, T = 8 this gives |ι| ≤ 2. A genus collision has ι = 2(g'−g) ≠ 0, so ι = ±2: shape (3,5).
This agrees with PS.1.

### Search formulation

Write Z = X ⊎ (−Y) with |X| = 3, |Y| = 5, scaled so that Y is integral. Up to Z ↦ −Z this covers both
orientations. The conditions are Σx = Σy = p_1, Σx³ = Σy³ = p_3 and Σ1/x = Σ1/y = r. With e_k = e_k(X):

- e_1 = p_1;
- p_3 = e_1³ − 3e_1e_2 + 3e_3;
- r = e_2/e_3.

Since p_1 r ≥ 25 > 1 (Cauchy–Schwarz on five positive numbers), this solves uniquely as

e_3 = (p_3 − p_1³)/(3(1 − p_1 r)) > 0 (as p_3 < p_1³), and e_2 = r e_3 > 0.

So a configuration exists iff f(x) = x³ − e_1x² + e_2x − e_3 has three rational roots. They are then
automatically positive.

### Certified filter (`check_t3.c`)

Take a prime p > 220, p ≠ 3. Every y ≤ 220 is a p-unit, so r is p-integral. If 1 − p_1 r ≢ 0 (mod p),
then e_1, e_2, e_3 are p-integral. A monic polynomial with p-integral coefficients has only p-integral
rational roots. So if f splits over Q, then f mod p is a product of three linear factors.

"f mod p does not split" therefore **proves** that Y has no X. A prime with 1 − p_1 r ≡ 0 is
inconclusive and does not reject. Splitting is a table lookup: all (a,b,c) ∈ F_p³ arising as
∏(x−r_i). The table is self-tested against brute-force root counting on 20,000 random cubics per prime.
Sixteen primes (223 … 307) are used, and every survivor is re-examined exactly with sympy
(`check_t3_verify.py`).

The loop covers **every** multiset 1 ≤ y_1 ≤ … ≤ y_5 ≤ 220, primitive or not. This is a superset of
"five-element side made primitive ≤ 220". The verifier checks coverage per y_1 against C(224−y_1, 4),
and the total against C(224, 5).

### Runs

Two processes, `nice -n 10`, memory checked before starting (30–37% free), checkpoint per y_1.

- **Main, N = 220:** 4,493,032,544 multisets examined, equal to C(224,5). All 220 values of y_1 are
  done, with exact per-y_1 counts. **0 survivors, 0 solutions.**
  - Rejections by successive primes: 3.58e9, 7.30e8, … The pass rate per prime is ≈ 1/6, as expected
    for generic S_3 cubics. The last rejection happened at the 16th prime, once.
  - Output: `check_t3_verify_main.txt`, `t3run/cube220_*`.
- **Planted control 1** (same code, modified target Σx³ = Σy³ + 12300, N = 60): it recovers the planted
  Y_0 = {2,2,8,8,8}, X_0 = {1,3,24}. The other 3 survivors are degenerate (roots 0,0,·). Output: `check_t3_verify_plant1.txt`.
- **Planted control 2** (Σx³ = Σy³ + 18099612, full N = 220): it recovers Y_0 = {2,2,28,77,220},
  X_0 = {1,20,308} at the top of the range, y_5 = 220. The other 121 survivors are degenerate. Output: `check_t3_verify_plant2.txt`.
- The binary of the main run was compared with a fresh build of the final source: the machine code
  (`otool -tv`) is identical. The later source edits were comments and the `DELTA` default 0.
- CPU: about 13 CPU-minutes for all T_3 runs, within the 100-minute cap. The direct n = 4 search took
  8.2 CPU-minutes (`direct4_N440.time`).

**Conclusion.** The claim is confirmed exactly as stated, and on a larger set (all Y ≤ 220, not only
the primitive ones). Nothing is extrapolated beyond 220. Whether T_3 = 8 remains open, as the
statements say.

**Real solutions** (`check_t3_real.py`): see PW.0. They exist and form an open set, but are rare
among small integer Y. No disc = 0 case occurs for Y ≤ 24.

---

## Files

- `heatlib.py`: exact heat coefficients (paper's convention) and the Uçar cross-check.
- `check_heat.py/.txt`: the convention against Uçar (4.25), (4.33), (4.35).
- `check_pairs.py/.txt`: PW.4, and the PW.0/PW.1/PW.2 numbers.
- `check_pencil4.c` → `pencil4_N{130,220}_mode{0,1}.txt`; `check_pencil61.py/.txt`: PW.3/PW.5 (n = 4).
- `check_direct4.c` → `direct4_N440.txt` (and `.time`); `check_direct4.py/.txt`: non-pencil witnesses.
- `check_n5.c` → `n5_N200_mode{0,1}.txt`; `check_n5.py/.txt`: the n = 5 claim.
- `check_t3.c`, `t3run/` (checkpoints, logs, survivors); `check_t3_verify.py` with `check_t3_verify_{main,plant1,plant2}.txt`.
- `check_t3_real.py/.txt`: real (3,5) solutions.
- `fetches.md`.
