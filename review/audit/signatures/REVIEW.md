# Referee report, gate G5: group SIGNATURES

I worked from the statements in `review/audit/statements/signatures.md` and the fetched source texts. I did not consult the existing proofs, scripts or data. Every proof below is my own. Every check uses exact arithmetic (integers, `fractions.Fraction`, sympy Bernoulli numbers), uses real `assert`s and exits nonzero on failure.

Scripts are run from the repo root with `/opt/homebrew/Caskroom/miniforge/base/bin/python3 review/audit/signatures/<script>`. The outputs sit next to them as `*.txt`.

| script | covers | runtime |
|---|---|---|
| `sigcommon.py` | b_l(k) from Uçar (4.25)+(4.33); exact heat-coefficient comparison | (module) |
| `check_cone_coefficients.py` | SG.1, SG.2, SG.3, the remark in SG.4; Schueth cross-check | 1 s |
| `check_prouhet.py` | SG.9 and the block lemmas used for Theorem N | 3 s |
| `check_theorem_S.py` | SG.4, SG.5, SG.6, SG.7, SG.8, lem:sigdata (brute force) | ~4 min |
| `check_thmN_a.py` | Theorem N(a): full b_l check for L = 2..6 (g' = 0, 1, 2); moment check for L = 7, 8, 9 | ~15 min |
| `check_thmN_b.py` | Theorem N(b) for k = 2..7 with full b_l; the Egyptian-fraction lemma | 10 s |
| `check_corollaries.py` | ex:siggenus, Cor N1 floor/log arithmetic, the j-range wording | 1 s |

## Summary

| id | grade | one-line reason |
|---|---|---|
| SG.0 (setting, H) | NONE | Consistent with Uçar Thm 4.20 / (4.33). c_1 = Area/4π = s/2. |
| SG.1 Lemma 1 | NONE | Proved for all l from (4.25)/(4.33). Checked for l ≤ 14. p_0, p_1, p_2 agree with Schueth. |
| SG.2 Lemma 2 | NONE | φ_l = Σ_{k≥1} [x^{2k}]p_l · ψ_k, triangular, with a nonzero diagonal. |
| SG.3 Lemma 3 | NONE | ψ_k(1) = 0, b_l(1) = p_l(1) = 0, and 1 − 1/1 = 0. |
| SG.4 Lemma 4 | MINOR | The statement is true for all L. Three defects: the justification "because Σ_k a_{l,k} = 0" is false (Σ_k a_{l,k} = −p_l(0) ≠ 0); "j odd, j ≤ 2L−3" literally includes j ≤ −3; the converse should require (g;m) ∈ Sig. |
| SG.5 Theorem S | NONE | Short proof via odd elementary symmetric functions. Brute force finds nothing; the bound is sharp at L = 1, 2. |
| SG.6 Cor S1 | NONE | Follows from (4.3) and Theorem S. |
| SG.7 Cor S2 | NONE | n + g − g' ≤ A/π + 4 − 3g − g'. |
| SG.8 Theorem T1 | NONE | Gauss–Bonnet plus Cor S1 with g = g' = 0. Brute force agrees. |
| SG.9 Prop P | NONE | Generating-product / Laplace-integral proof. |
| SG.10 Theorem N | NONE | True for every L and k. An independent explicit construction is proved in general and built exactly (see P1). |
| SG.11 computed ranges | MINOR | "k ≥ 4 impractical" is an artefact of the Egyptian/greedy route. A uniform construction with 3·2^{2k−3} points per side is verified here for k ≤ 7. |
| SG.12 Cor N1 | NONE | Both bounds hold. Exact floor/log arithmetic checked at every threshold 2π(4^t − 1). |
| SG.13 LaTeX versions | MINOR | lem:sigdata repeats the "odd j ≤ 2L−3" range defect. Everything else matches SG.4–SG.12. ex:siggenus is exact. |
| DF.1–DF.7 | NONE (context) | Used only as definitions. c_1 = −χ/2 is consistent. |

There are no FATAL or SERIOUS findings.

---

## Heat input and cone polynomials (SG.0–SG.3)

**Cone coefficients.** From Uçar (4.25):

c^S_l(π/k) = (1/4k) · (−1)^l / ((l+1)!(2l+1)) · Σ_{j=0}^{l+1} C(2l+2, 2j)(k^{2j} − 1) B_{2j} B_{2l+2−2j}(1/2)

From (4.33), with κ = K:

b_ν(k) = K^ν Σ_{i=0}^{ν} 2/(4^i i!) · c^S_{ν−i}(π/k)

**Lemma 1, proof.** Put p_ν = k·b_ν/K^ν = Σ_i 2/(4^i i!) · (k c^S_{ν−i}).
- Each k c^S_l is a polynomial in k² of degree l+1. Every term carries a factor (k^{2j} − 1). Hence p_ν is even, has degree at most 2ν+2, and satisfies p_ν(1) = 0.
- The power k^{2ν+2} occurs only for i = 0 and j = ν+1. Its coefficient is (1/2)(−1)^ν B_{2ν+2} B_0(1/2) / ((ν+1)!(2ν+1)).
- Since sign B_{2ν+2} = (−1)^ν, this equals |B_{2ν+2}| / (2(ν+1)!(2ν+1)) ≠ 0.

Check: l ≤ 14 in `check_cone_coefficients.py`. The values p_0 = (k²−1)/12, p_1 = (k⁴−1)/360 + (k²−1)/36 and p_2 = (k⁶−1)/2520 + (k⁴−1)/720 + (k²−1)/180 agree with Schueth, Remark 4.2 and Theorem 4.1. That is an independent source.

**Lemma 2, proof.** Write p_l = Σ_{i=0}^{l+1} e_i x^{2i}. Since p_l(1) = 0, e_0 = −Σ_{i≥1} e_i. So

φ_l = p_l/x = e_0 x^{−1} + Σ_{i≥1} e_i x^{2i−1} = Σ_{i≥1} e_i ψ_i.

Hence a_{l,k} = e_k, and a_{l,l+1} is the leading coefficient, which is nonzero.

At K = −1, C_l(m) = (−1)^l Σ_k a_{l,k} Ψ_k(m). The system is triangular with nonzero diagonal, so (C_l equal for l ≤ L−2) ⇔ (Ψ_k equal for k ≤ L−1). The direction "⇐" is plain linearity.

**Lemma 3.** b_l(1) = p_l(1)/1 = 0, and an order-1 point adds 1 − 1/1 = 0 to s.

**H3.** Z ~ (4πt)^{−1} Σ a_ν t^ν + Σ_cones C gives c_1 = a_0/4π = Area/4π and c_{l+2} = a_{l+1}/4π + C_l. By (4.35), a_{l+1} is proportional to the area.

Grades: SG.0–SG.3 NONE.

## SG.4 Lemma 4 (reduction)

**Proof.**
- c_1 equal ⇔ s equal ⇔ 2g + n − R = 2g' + n' − R'.
- Given equal area, c_{l+2} equal ⇔ C_l equal, and Lemma 2 turns this into Ψ_k equal for k ≤ L−1. This gives (4.1).
- Then d = R' − R = 2(g' − g) + n' − n is an integer. With U and V as defined:
  - R(U) − R(V) = −d + max(d,0) − max(−d,0) = 0.
  - Ψ_k equal gives P_{2k−1}(m) − P_{2k−1}(m') = R − R' = −d, so the padded power sums agree.
  - |V| − |U| = n' − n − d = 2(g − g').
  - |U| + |V| = n + n' + |d|. Also 2max(a,b) = a + b + |a − b| with a − b = −d, which gives (4.3).
- Converse: from (4.2), R' − R = a − b = P_j(m) − P_j(m'), so the Ψ_k agree. From 2(g − g') = n' + b − n − a, the areas agree.
- Mirror form: pad both to length N. Then N − R_N = n − R. Equal area ⇔ R_N − R'_N = 2(g − g'). Equal Ψ_k ⇔ P_{j,N} − P'_{j,N} = R_N − R'_N.

**Defects.**
1. The sentence "It follows for all L from Lemma 2, because Σ_k a_{l,k} = 0" is false with Lemma 2's indexing. Σ_{k=1}^{l+1} a_{l,k} = −p_l(0) ≠ 0. For example, l = 0 gives 1/12, and l = 1 gives 11/360. Every l ≤ 14 was checked.
   - The correct reason is p_l(1) = Σ_{k=0}^{l+1} [x^{2k}]p_l = 0. Note that k starts at 0.
   - With that reason, the constant vector s_{−1} = s_1 = … = s_{2L−3} solves the cone-difference system Σ_{i=0}^{l+1} e_i s_{2i−1} = 0. The system is triangular in s_{2l+1} with a nonzero diagonal, so its solution space is one-dimensional.
   - The claim itself is right. I proved it directly above.
2. "(j odd, j ≤ 2L−3)" literally includes j = −3, −5, …. On that reading the forward direction is false. For (1;15) against (0;3,3,5,5) with Lemma 4's paddings U = {15,1} and V = {3,3,5,5}, P_{−3} differs (`check_corollaries.py`). The range should be 1 ≤ j ≤ 2L−3. R is already listed separately.
3. In the converse, "let g, g' ≥ 0" should add "with (g;m) ∈ Sig". Equal area then makes (g';m') hyperbolic too.

Brute force: `check_theorem_S.py` covers all 78,806 hyperbolic signatures with g ≤ 2, n ≤ 5 and orders ≤ 18. That gives 173,354 equal-area pairs. Every pair satisfies (4.2), (4.3) and the mirror form. The shared counts L ≥ 2 were recomputed with the actual b_l and agree.

**Grade: MINOR.** Fix: replace the justification with "because p_l(1) = 0", write "1 ≤ j ≤ 2L−3", and add the hypothesis in the converse.

## SG.5 Theorem S

**Proof.**
1. Parity and non-emptiness:
   - Cancelling common elements preserves (4.2).
   - |U*| + |V*| ≡ |U| + |V| ≡ |V| − |U| = 2(g − g') ≡ 0 (mod 2).
   - If U* = V* = ∅ then U = V. Hence g = g'. Since m and m' contain no 1s, m = m'. That contradicts σ ≠ σ'.
2. Put X = U* ⊎ (−V*), with N = |X| even and nonzero. X contains no pair {x, −x}, because U* and V* are disjoint and positive. Also p_j(X) = 0 for j = −1, 1, 3, …, 2L−3.
3. Let f(t) = Π(1 + x t). Then log f(t) − log f(−t) = 2 Σ_{j odd} p_j t^j / j = O(t^{2L−1}). So f(t) − f(−t) = O(t^{2L−1}), which means e_1 = e_3 = … = e_{2L−3} = 0.
4. Also e_{N−1} = e_N · p_{−1} = 0.
5. Suppose N ≤ 2L. Every odd index ≤ N − 1 is then either ≤ 2L−3 or equal to N − 1. So all odd e_k vanish and f is even. Hence X = −X, a contradiction. Therefore N ≥ 2L+2.

The proof does not need Theorem A. Its equal-size case is Theorem A.

The LaTeX version adds that U* and V* do not depend on the paddings. That is true: R(U) = R(V) forces a − b = d, so after cancellation exactly |d| ones remain, all on one side.

**Search** (`check_theorem_S.py`). Exhaustive over disjoint multisets with entries ≤ M (1 allowed) and |U*| + |V*| ≤ 2L, using (L, M) = (1, 60), (2, 40), (3, 16), (4, 9): no example exists.
- The bound is sharp. L = 1: {1} against {2,3,6}, realised by (2;∅) against (1;2,3,6). L = 2: {2,8,8} against {3,3,12}.
- In the signature census, 2,088 pairs with L ≥ 2 attain 2L+2.
- Every census pair satisfies the bound.

**Grade: NONE.**

## SG.6 Corollary S1, SG.7 Corollary S2, SG.8 Theorem T1

**S1.** By (4.3), |U*| + |V*| ≤ |U| + |V| = 2max(…) ≤ 2L < 2L+2. Theorem S then forces σ = σ'.

**S2.**
- c_1 equal forces equal area.
- From s ≥ 2g − 2 + n/2 we get n ≤ A/π − 4g + 4. Hence n + g − g' ≤ A/π + 4 − 3g − g' ≤ A/π + 4.
- The other term is symmetric, since the areas are equal. It is an integer, so it is ≤ ⌊A/π⌋ + 4.
- Apply S1.
- K_mult ≤ ⌊A/π⌋ + 4, and the number is read off from c_1.

**T1.**
1. With g = 0: s = −2 + Σ(1 − 1/m_i) ≥ −2 + n/2, with equality iff every m_i = 2. So n ≤ 2s + 4 = A/π + 4.
2. Both n and n' are ≤ A/π + 4. Apply S1 with g = g' = 0.
3. Apply S1 directly.

**Brute force.** In the census:
- T1(1), including the equality case, holds for every genus-0 signature.
- Every equal-area pair sharing L coefficients satisfies L < max(n + g − g', n' + g' − g), L < ⌊A/π⌋ + 4, and, in genus 0, L < max(n, n').
- Shared-count histogram: L = 1: 169,809 pairs; L = 2: 3,539; L = 3: 6.

**Grades: NONE.**

## SG.9 Proposition P

**Proof.**
1. Σ_i (−1)^{t(i)} z^i = Π_{d<D}(1 − z^{2^d}), which is divisible by (1 − z)^D. Applying (z d/dz)^r at z = 1 gives zero for r < D.
2. 1/(hi + c) = ∫_0^∞ e^{−(hi+c)s} ds. Therefore Σ (−1)^{t(i)}/(hi + c) = ∫_0^∞ e^{−cs} Π_d(1 − e^{−h 2^d s}) ds > 0.

Checks: part 1 exactly for D ≤ 12, including failure at degree D (so the range is sharp); part 2 on 288 rational samples.

**Grade: NONE.**

## SG.10 / SG.13 thm:signonuniform: Theorem N

The statement is true for every L ≥ 2, every g' ≥ 0 and every k ≥ 2. The full verdict is in the P1 section below.

Part (c) follows at once:
- (a) gives two different signatures sharing L coefficients for every L. So K_mult = L+1 is attained, the supremum over Sig is ∞, and genus is not determined.
- (b) does the same inside genus 0, for the cone count.

**Grade: NONE.**

## SG.11 Computed ranges

I cannot check the specific pairs claimed (9 vs 10, 103 vs 104, and the L ≤ 6 pairs) without the authors' objects, which I was not allowed to see. That comparison belongs to phase two.

Consistency: my own (a) construction, built independently, also gives 1023 and 1025 cone points at L = 6 and shares exactly L coefficients for L ≤ 9.

The sentence "For k ≥ 4 the greedy denominators grow doubly exponentially, which makes exact verification impractical" describes one proof route, not the problem. The construction in P1(f′) below has 3·2^{2k−3} − 1 against 3·2^{2k−3} cone points. It was verified with the full b_l for k ≤ 7 (6,143 against 6,144 points) in seconds.

**Grade: MINOR.** Fix: either adopt the doubling construction, which makes the proof explicit and verifiable for every k, or rephrase the sentence as a statement about the particular construction.

## SG.12 Corollary N1

**Upper bound.** By S2, K_mult(O) ≤ ⌊Area/π⌋ + 4 ≤ ⌊A/π⌋ + 4. The values are bounded, so the maximum exists.

**Lower bound.**
- Let L = ⌊log_4(A/2π + 1)⌋ + 1. Then 4^{L−1} ≤ A/2π + 1, so the N(a) pair with g' = 0 has area < 2π(4^{L−1} − 1) ≤ A.
- Both members have K_mult ≥ L+1 = ⌊log_4(A/2π + 1)⌋ + 2.
- L ≥ 2 ⇔ A/2π + 1 ≥ 4 ⇔ A ≥ 6π. So the hypothesis is exactly what is needed.
- At A = 2π(4^t − 1) the logarithm is an exact integer. Strictness is not needed there, because "area < bound ≤ A" holds anyway.

`check_corollaries.py` evaluates the floor-log exactly (largest t with 4^t ≤ A/2π + 1):
- at every threshold t ≤ 12, at ±10⁻⁹ and ±1/3 around it, and on a grid of 2,758 values;
- assertions: L ≥ 2 iff A ≥ 6π; 2(4^{L−1} − 1) ≤ A/π; L is maximal; lower ≤ upper.

**Grade: NONE.**

## SG.13 Manuscript versions

- **lem:sigdata.** Equivalent to Lemma 4 and correct, apart from the range "odd j ≤ 2L−3", which must read 1 ≤ j ≤ 2L−3. The parenthetical heat-input sentence is correct: the contribution is (−1)^l k^{−1} p_l(k) at t^l when K = −1.
- **thm:sigsep, cor:sigarea, thm:sigcount, thm:signonuniform, cor:siggrowth.** As above.
- **ex:siggenus.** Exact, with the actual b_l:
  - (1;15) against (0;3,3,5,5): Area/2π = 14/15, and they share exactly 2 coefficients.
  - (1;15,15,15) against (0;3,3,5,7,7,21): Area/2π = 14/5, and they share exactly 3.
- **rem:sigK, rem:sigphysics.** Consistent. The phrase "a handle costs no more than a cone point" matches the max(n + g − g', …) term in (4.3).
- The "Exact extent" comment should be updated if the doubling construction is adopted.

**Grade: MINOR** (the range only).

---

## P1 verdict: Theorem N

**Verdict: Theorem N is TRUE for all L ≥ 2, all g' ≥ 0 and all k ≥ 2, including the area bound.**

The theorem statement does not specify its construction. Below I construct objects that satisfy it and prove (a)–(g) for them in general. At each point I mark the pitfalls the prompt lists and whether they can bite.

Notation: D = 2L − 2 (or D = 2k − 2), ε_i = (−1)^{t(i)} for i < 2^D, and M_j(h,c) = Σ_i ε_i (hi + c)^j.

**Construction for (a).** All blocks are signed multisets. For odd j a term ε·x contributes (εx)^j, so a negative entry moves to the other side.
- Block 1: x_i = 3i − 1. Only i = 0 is negative (value −1, with ε_0 = +1).
- Block 2: y_i = 3i + 2, which is ≥ 2.
- Let r_1 = M_{−1}(3, −1) and r_2 = M_{−1}(3, 2). Write r_2/(−r_1) = a/b in lowest terms, and set λ_1 = 2b, λ_2 = 2a.
- Let X = λ_1{ε_i x_i} ⊎ λ_2{ε_i y_i}. U is the positive part of X and V is the negated negative part.
- O = (g'+1; U) and O' = (g'; V).

### (a) Prouhet step

**Degree range.** For a polynomial f with deg f < D, f(h·+c) has the same degree, so M_j(h,c) = 0 for 0 ≤ j < D by P(1). The needed j are 1, 3, …, 2L−3 < D = 2L−2. So D = 2L−2 is the least admissible value, and 2^D = 4^{L−1}.

**Signs of the reciprocal sums.**
- r_2 > 0 by P(2), since c = 2 > 0.
- r_1 < 0. The i = 0 term is −1. The tail is Σ_{i≥1} ε_i/(3i − 1) = ∫_0^∞ e^{s}(Π_d(1 − e^{−3·2^d s}) − 1) ds. The integrand is negative, and it is O(e^{−2s}) at infinity.
- Checked exactly for D ≤ 14.

**Exactness.**
- M_{D+1}(h,c) = (−1)^D 2^{D(D−1)/2} (D+1)! h^D (c + h(2^D − 1)/2). This closed form was checked for D ≤ 10.
- It is nonzero, with the same sign, for c = −1 and for c = 2.
- Hence s_{2L−1}(X) = λ_1^{2L−1} M_{D+1}(3,−1) + λ_2^{2L−1} M_{D+1}(3,2) ≠ 0.

### (b) Scaling

r_1/λ_1 + r_2/λ_2 = 0 ⇔ λ_2/λ_1 = r_2/(−r_1) ∈ ℚ_{>0}. A positive rational ratio always has an integer solution.

Odd moments of each block vanish individually and scale by λ^j, so scaling cannot break them. One scaling per block suffices. The opposite signs of r_1 and r_2 are exactly what makes the scaling possible.

### (c) Entries ≥ 2

- Block 2 entries are ≥ 2·2.
- Block 1 entries are λ_1(3i − 1) ≥ 2 for i ≥ 1.
- The i = 0 term gives the entry λ_1 in V.

Pitfall: with the minimal scalings (b, a), λ_1 = 1 is possible in principle. Then V would contain a 1. That 1 is harmless as padding, but V would have 2^D rather than 2^D + 1 cone points. The factor 2 removes the case. With the factor, λ ranges up to about 64,000 digits for L ≤ 9.

For (b) the element 1 is wanted. See (f).

### (d) Hyperbolicity

The genus-(g'+1) side has 2^D − 1 ≥ 3 points of order ≥ 2, so s ≥ 2g' + 3/2 > 0. The other side has equal area by the converse of Lemma 4, so it is hyperbolic as well.

### (e) Area bound for g' = 0

- Cone counts: |U| − |V| = Σ_i sign(ε_i x_i) summed over both blocks. Block 2 contributes Σ ε_i = 0. Block 1 contributes Σ ε_i − 2Σ_{x_i<0} ε_i = 0 − 2ε_0 = −2. Counted directly: |U| = 2^D − 1 and |V| = 2^D + 1, with no 1s.
- |V| − |U| = 2 = 2(g − g'). So U is the genus-1 side, which agrees with the assignment.
- Area/2π = |U| − R(U) < 2^D − 1 = 4^{L−1} − 1, strictly, because R(U) > 0.
- The bound is essentially tight for this construction. The deficit is R(U), which is tiny: the printed values are 15.000, 63.000, …. Any off-by-one in the count on the genus-1 side (for example 2^D points) would break the bound. That is why the count matters.

### (f) Part (b) and the Egyptian-fraction step

**Existence (general).** Every positive rational q is a finite sum of distinct unit fractions with denominators ≥ 2:
1. Take 1/2 + 1/3 + … + 1/N greedily while the partial sum stays ≤ q. This is possible because the harmonic series diverges.
2. The remainder is < 1/(N+1). Expand it by Fibonacci–Sylvester greedy. The denominators are strictly increasing and > N, and the process terminates because the numerators strictly decrease.

Pitfalls:
- The plain greedy algorithm returns 1/1 whenever q ≥ 1, which is forbidden.
- Denominators explode doubly-exponentially. At q = 4 there are 98 terms, and the largest denominator has about 473,000 bits.

**Distinctness is not needed.** Scaled Prouhet blocks may be repeated, because the multiset union adds the moments.

**Construction (f′).** Use the doubling identity 1 = 1/2 + 1/2:
- Base block x_i = i + 1.
- U = {x_i : ε_i = +1} ⊎ 2 × {2x_i : ε_i = −1}.
- V = {x_i : ε_i = −1} ⊎ 2 × {2x_i : ε_i = +1}.

Then P_j(U) − P_j(V) = (1 − 2^{j+1}) M_j(1,1). This vanishes for j < D by Prouhet and for j = −1 because 1 − 2⁰ = 0. No Egyptian step and no rational coincidence are needed. Any list of unit fractions summing to 1 with p_i ≥ 2 works the same way; (2,3,6) was also checked.

**Properties.**
- Equal cardinality: each block contributes 2^{D−1} entries to each side.
- Exactly one 1: it is x_0 = 1, in U. All other entries are ≥ 2.
- The pitfall: if p_i = 1 were allowed, a 1 would appear in V and cancel the lone 1, destroying the n vs n+1 property.
- Result: O = (0; U∖{1}) with n = 3·2^{D−1} − 1 ≥ 5 points of order ≥ 2, not all equal to 2, so s > 0. O' = (0; V) with n + 1 points.
- Smallest instance, k = 2: (0;4,4,4,6,6) against (0;2,2,2,3,8,8).

### (g) Shared coefficients through the reduction lemma

The reduction lemma is proved for all L above.

**Exactly L (or k).** By Lemma 2 with a_{l,l+1} ≠ 0, H_{L+1} agrees iff in addition P_{2L−1}(U) = P_{2L−1}(V).
- For (a) this fails by the exactness computation in (a).
- For (b), (1 − Σ_i p_i^{D+1}) M_{D+1}(1,1) ≠ 0.

So the (a) pair shares exactly L coefficients and the (b) pair exactly k.

### Computation

All counts below use the actual b_l from Uçar (4.33).

**(a), full element-wise check** (`check_thmN_a.py`), L = 2..6 and g' = 0, 1, 2:

| L | cone points (genus g'+1 / genus g') | shared coefficients |
|---|---|---|
| 2 | 3 / 5 | exactly 2 |
| 3 | 15 / 17 | exactly 3 |
| 4 | 63 / 65 | exactly 4 |
| 5 | 255 / 257 | exactly 5 |
| 6 | 1023 / 1025 | exactly 6 |

The area is < 2π(4^{L−1} − 1) in every case.

**(a), L = 7, 8, 9.** The same identities hold exactly through the block moments: R, P_1, …, P_{2L−3} agree and P_{2L−1} differs. The cone differences are ΔC_l = (−1)^l Σ_i [x^{2i}]p_l · s_{2i−1}(X), equal to 0 for l ≤ L−2 and nonzero for l = L−1. The cone counts are 4095/4097, 16383/16385 and 65535/65537, and the area bound holds.

**(b), full check** (`check_thmN_b.py`), k = 2..7 with p = (2,2) and with p = (2,3,6). Shared exactly k in every case. With p = (2,2) the cone counts are:

| k | genus 0, n | genus 0, n + 1 |
|---|---|---|
| 2 | 5 | 6 |
| 3 | 23 | 24 |
| 4 | 95 | 96 |
| 5 | 383 | 384 |
| 6 | 1535 | 1536 |
| 7 | 6143 | 6144 |

**Theorem S consistency.** |U*| + |V*| ≥ 2L+2 holds throughout.

## Findings above NONE (all MINOR)

1. **SG.4 remark.** "because Σ_k a_{l,k} = 0" is false: the sum is −p_l(0), which is 1/12 for l = 0 and 11/360 for l = 1. Replace it with "because p_l(1) = 0, i.e. the coefficients of p_l, including the constant term, sum to 0".
2. **SG.4 (4.2) and lem:sigdata.** "j odd, j ≤ 2L−3" includes j ≤ −3, and the literal forward direction is then false (P_{−3} counterexample above). Write 1 ≤ j ≤ 2L−3.
3. **SG.4 converse.** Add "(g;m) ∈ Sig". This is wording only.
4. **SG.11.** The "k ≥ 4 impractical" remark is route-dependent. The doubling construction (f′) gives an explicit, exactly verifiable pair for every k and removes the Egyptian-fraction lemma and its pitfalls (q ≥ 1, p_i = 1, distinctness).
