# G5 referee report — group AUDIBILITY (AU.0–AU.4, DF.6, DF.7)

Basis: the statements in `review/audit/statements/audibility.md` and the fetched source texts only.
No proofs, scripts or data of the project were consulted. All checks are exact (integers, `Fraction`,
sympy rationals / Gaussian rationals); the single mpmath block in `check_theoremC.py` is labelled as a
non-proof sanity check. Every script runs from the repository root and exits nonzero on a failed `assert`.

## Summary

| id | grade | one-line reason |
|---|---|---|
| AU.0 heat input | MINOR | Correct for every l (proved below from Uçar (4.25)+(4.33)+Thm 4.20); the Holtz–Tyaglov source is cited under a wrong arXiv number (1005.2843 is a hep-ph paper); Thm 4.20(ii) and (4.35) should be cited explicitly. |
| AU.1 Thm A | NONE | Independent proof via f(z)f'(−z) − f(−z)f'(z) = c z^{2n−1}, c = 0 by R; coprimality of f(z), f(−z). Exhaustive / adversarial searches agree. (Optional: say "K_mult(·;Pill_n) ≤ n".) |
| AU.1 Thm B | MINOR | True. The constant is c_n = (−1)^{n(n+1)/2} = (−1)^{n+⌊n/2⌋} for **every** n ≥ 2 (proved below); statement only lists n = 3..8 from a script. Upgrade to the closed form. |
| AU.1 Thm C(1) | NONE | Proved; κ = (P_{2n−3}(m') − P_{2n−3}(m))/(2n−3). |
| AU.1 Thm C(2) | NONE | Proved by the implicit function theorem (Jacobian minor is a Vandermonde in m_i²); exact Sturm certificates n = 2..6. Distinctness hypothesis is needed (e.g. {3,3,3} is locally isolated). |
| AU.1 Thm C(3) | NONE | Scaling argument correct; witnesses verified; n = 5 exhaustive search reproduced for orders ≤ 60 and ≤ 120 (0 collisions; counts match). |
| AU.2 Lemma 1 | NONE | Proved via f(z)/f(−z) = exp(2∑_{odd} s_k z^k/k); explicit certificates N ≤ 5, j ≤ 7. "s_j" in the converse should say "for odd j" (cosmetic). |
| AU.3 Remark 2 | MINOR | Jacobian formula true for every n (one-line Vandermonde proof; "checked n ≤ 7" can be replaced by the proof). Symbol c_n clashes with Theorem B's c_n (different constants). |
| AU.3 Remark 3 | MINOR | Correct; "every genus-0 orbifold" must read "every hyperbolic genus-0 orbifold" (the heat input uses K = −1). 3-vs-4 search reproduced. |
| AU.4 table | MINOR | Every number reproduced exactly (R, S_1, P_3, P_5, Φ = 500z³ and 1544400z³, counts 7,028,847 and 216,071,394). Only issue: S_1 vs P_1 notation. |
| DF.6 thm:Crestated | NONE | Follows from Thm A (n = 3) + rigidity; exact K_mult distribution over all pillows with orders ≤ 60 computed (values 1, 2, 3 all occur). |
| DF.7 rem:nconerestated | MINOR | Mathematically correct but stale: (a) says injectivity "is not proved here" for n ≥ 4 and (b),(c) keep it as a condition, while Theorem A proves it for all n. Numbers in (c) verified. |

No FATAL or SERIOUS findings.

Scripts and outputs (all in this folder):
`check_heat_input.py/.txt`, `check_theoremA.py/.txt`, `check_theoremB.py/.txt`, `check_theoremC.py/.txt`,
`check_lemma1.py/.txt`, `check_AU4_definitions.py/.txt`, `check_n5_search.py/.txt` (+ `n5_search.c`),
`fetches.md`, `ht_0912.4703.pdf/.txt` (correct Holtz–Tyaglov text).

Notation used below: f(z) = ∏(1+m_i z) = ∑ e_k z^k, E/O its even/odd parts, p(z) = ∏(z+m_i),
P_k = ∑ m_i^k, R = ∑ 1/m_i = e_{n−1}/e_n.

---

## AU.0 — heat input

**Claim.** Cone point of order m contributes b_l(m) = K^l (1/m) p_l(m) at t^l, p_l even, deg 2l+2,
p_l(1) = 0, leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)); smooth terms are multiples of the area.

**Inputs (verified in the fetched text; printed page / PDF page of arXiv:1711.03405v1):**
- Thm 4.20 (p.137): heat trace ~ (4πt)^{-1} ∑ a_ν t^ν + ∑_N I_N/|Iso N| (form taken from DGGW Thm 4.8).
- Thm 4.20(i), (4.35) (p.137): a_ν(O) = vol(O)/(ν!4^ν) ∑_ℓ C(ν,ℓ)(−4)^ℓ B_{2ℓ}(1/2) κ^ν — a fixed
  multiple of the area. (a_0..a_5 per unit area: 1, 1/3, 1/15, 4/315, 1/315, 4/3465 times κ^ν.)
- Thm 4.20(ii) (p.138, PDF p.143): a cone point of order k contributes exactly C.
- (4.33) (p.137, PDF p.142): C = ∑_ν ∑_{ℓ=0}^{ν} 2/(4^ℓ ℓ!) c^S_{ν−ℓ}(π/k) κ^ν t^ν.
- (4.25) (p.134, PDF p.139): c^S_r(π/k) = (1/4k)·(−1)^r/(r+1)!·1/(2r+1)·∑_{j=0}^{r+1} C(2r+2,2j)(k^{2j}−1) B_{2j} B_{2r+2−2j}(1/2).
  (Layout confirmed from the rendered PDF page: the text extraction garbles it.)
- Donnelly enters only inside Uçar's proof of Thm 4.20 (standing gap, accepted).

**Proof for all l.** Put q_r(k) := k·c^S_r(π/k) = (1/4)(−1)^r/((r+1)!(2r+1)) ∑_{j=0}^{r+1} C(2r+2,2j)(k^{2j}−1)B_{2j}B_{2r+2−2j}(1/2).
Then b_l(k) = κ^l (1/k) p_l(k) with p_l(k) = ∑_{ℓ=0}^{l} 2/(4^ℓ ℓ!) q_{l−ℓ}(k).
(i) Each q_r is a polynomial in k² (only k^{2j} occurs), so p_l is even.
(ii) Each summand of q_r carries the factor k^{2j}−1, so q_r(1) = 0 and p_l(1) = 0.
(iii) deg q_r ≤ 2r+2, so only the ℓ = 0 term of p_l can reach degree 2l+2; its k^{2l+2} coefficient is the
j = l+1 term: 2·(1/4)(−1)^l B_{2l+2} B_0(1/2)/((l+1)!(2l+1)) = (−1)^l B_{2l+2}/(2(l+1)!(2l+1)), using
B_0(x) = 1. Since B_{2n} ≠ 0 with sign (−1)^{n+1} (classical; checked exactly for n ≤ 80 in the script), this is
|B_{2l+2}|/(2(l+1)!(2l+1)) ≠ 0. So deg p_l = 2l+2 exactly.
(iv) (1/m)p_l(m) is a Q-combination of m^{−1}, m, m³, …, m^{2l+1}, so ∑_i b_l(m_i) is a combination of
R, P_1, …, P_{2l+1} with coefficient κ^l·lead ≠ 0 on P_{2l+1}. Together with c_1 = Area/4π = (n−2−R)/2 and
smooth terms ∝ Area, the map (c_1,…,c_n) ↦ (R, P_1, …, P_{2n−3}) is triangular with nonzero diagonal for fixed n.

**Exact checks (`check_heat_input.txt`).** l = 0..12 from the formula: even, degree 2l+2, p_l(1) = 0, leading
coefficient equals the claimed value (e.g. 1/12, 1/360, 1/2520, 1/10080, …, 657931/143700480000).
p_0 = (k²−1)/12, p_1 = k⁴/360 + k²/36 − 11/360, p_2 = k⁶/2520 + k⁴/720 + k²/180 − 37/5040,
p_3 = k⁸/10080 + k⁶/3780 + k⁴/2160 + k²/945 − 19/10080. Cross-checks: l = 0 equals DGGW Prop 5.5
((m²−1)/12 divided by |Iso| = m); l = 2 equals Schueth Thm 4.1 (p.14) with ΔK = 0.

**Grade: MINOR.** Fixes: (1) the source table cites Holtz–Tyaglov as arXiv:1005.2843; that number is M. Rauch,
"Extended Scalar Sector and Fat Jets" (hep-ph). The correct reference is arXiv:0912.4703, SIAM Rev. 54 (2012)
421–509 (DOI 10.1137/090781127); (1.37) and Theorem 1.17 (Orlando, (1.41)) are on p.13 there and agree
with the use made of them (verified, see Thm B). Correct the citation wherever it appears. (2) Cite
Thm 4.20(ii) (cone point contributes C) and (4.35) (smooth terms) next to (4.25)+(4.33), since those are the
statements that make (4.33) the per-cone-point term of an orbifold's heat trace.

---

## AU.1 — Theorem A

**Independent proof.** Let m satisfy the hypothesis and m' (n nonzero complex numbers) have I_n(m') = I_n(m).
Write f, f' for the two polynomials. Since log f(z) = ∑_k (−1)^{k+1} P_k z^k/k,
f(z)/f(−z) = exp(2∑_{k odd} P_k z^k/k). Equality of P_1,…,P_{2n−3} gives f(z)/f(−z) ≡ f'(z)/f'(−z) mod z^{2n−1},
hence (f(−z) and f'(−z) are units in C[[z]]) Ψ(z) := f(z)f'(−z) − f(−z)f'(z) ≡ 0 mod z^{2n−1}.
Ψ is odd of degree ≤ 2n, so Ψ = c z^{2n−1}. Its z^{2n−1} coefficient is
∑_{a+b=2n−1} e_a e'_b((−1)^b − (−1)^a) = 2(−1)^n(e_{n−1}e'_n − e_n e'_{n−1}) = 2(−1)^n e_n e'_n (R − R') = 0.
So f(z)f'(−z) = f(−z)f'(z) identically. The roots of f are −1/m_i, those of f(−z) are 1/m_i; a common root
means m_i + m_j = 0 for some i, j (i = j excluded by m_i ≠ 0). Under the hypothesis gcd(f(z), f(−z)) = 1, so
f | f'. Both have degree n (m'_j ≠ 0) and constant term 1, so f' = f, i.e. m' = m. ∎
Hypotheses used: m_i ≠ 0 (degree, R), m_i + m_j ≠ 0 (coprimality), m'_j ≠ 0 (R' defined, deg f' = n).
Nothing about m' beyond that. n = 1 (I_1 = (R)) and n = 2 are covered by the same argument.
"Equivalently e_nΔ_{n−1} ≠ 0": Holtz–Tyaglov Thm 1.17 with zeros z_i = −m_i and a_0 = 1 gives
Δ_{n−1}(p) = (−1)^{n(n−1)/2}∏(−m_i−m_j) = ∏_{i<j}(m_i+m_j) (also verified symbolically n ≤ 5, exactly at
points n ≤ 10). The heat-invariant corollary uses AU.0's triangularity, valid for a fixed n.

**Counterexample search (`check_theoremA.txt`).** No two distinct multisets share I_n among positive integers
1..300 (n = 1, 2), 1..90 (n = 3), 1..40 (n = 4) — orders 1 included, i.e. padded and repeated cases. Signed
nonzero integers ([−25,25], [−12,12], [−7,7] for n = 2, 3, 4): 1, 24, 99 collision classes, and every member of
every class violates the hypothesis (e.g. {−12,−12,12} vs {−12,−11,11}) — so the hypothesis is necessary and the
theorem's dichotomy is sharp. Gaussian integers (|Re|,|Im| ≤ 3, n = 2; ≤ 2, n = 3): same outcome. Constructive
recovery (solve Thm B's system from I_n, factor) returns m exactly for 105 multisets, n = 1..7, incl. repeated
orders and padding.

**Grade: NONE.** Optional wording: write K_mult(O; Pill_n) ≤ n to make explicit that n is known (comparison with
other n is Remark 3).

## AU.1 — Theorem B

**Independent proof, with the constant.** For X(z) = ∑_{k=1}^n x_k z^k let X_o, X_e be its odd/even parts.
The system says: odd coefficients z^1..z^{2n−3} of X_o − T X_e vanish (with x_0 := 1 moved to b), and
x_{n−1} − R x_n = 0. As T = O/E (true m; tanh(∑ P_k z^k/k) = (f(z)−f(−z))/(f(z)+f(−z))), the true e solves it.
For det M only the homogeneous part matters. (a) X_o − T X_e = E^{−1}(X_o E − X_e O) and E^{−1} has only even
powers with constant term 1, so the odd-coefficient vector of the left side through z^{2n−3} is a lower
unitriangular matrix times that of N_X := X_oE − X_eO. (b) The odd coefficient of z^{2j+1} in N_X is
∑_k (−1)^{k+1} e_{2j+1−k} x_k. For j = n−1 it equals (−1)^n(e_n x_{n−1} − e_{n−1} x_n) = (−1)^n e_n(x_{n−1} − R x_n).
Hence M = diag(L, (−1)^n/e_n)·N with N_{j,k} = (−1)^{k+1} e_{2j+1−k} (j = 0..n−1, k = 1..n), and
det M = (−1)^n e_n^{−1} (−1)^{⌊n/2⌋} det[e_{2j+1−k}]. Row j = 0 is (1,0,…,0); deleting it and column 1 leaves
[e_{2j−k'}]_{j,k'=1..n−1}, the transpose of the Hurwitz matrix (1.37) of p with a_k = e_k. So
  det M = (−1)^{n+⌊n/2⌋} Δ_{n−1}(p)/e_n = (−1)^{n(n+1)/2} ∏_{i<j}(m_i+m_j)/∏m_i,
since n + ⌊n/2⌋ ≡ n(n+1)/2 (mod 2) (check n mod 4). Kernel view (consistency): a kernel vector X satisfies
X(z)f(−z) = X(−z)f(z), forcing X = 0 when gcd(f(z), f(−z)) = 1, and X = z²g(z) is a kernel vector when
f = (1 − a²z²)g.

**Checks (`check_theoremB.txt`).** Symbolic identity in e_1..e_n for n = 2..6: det M · e_n/Δ_{n−1} = (−1)^{n(n+1)/2}.
Exact rational points with T computed from tanh of the odd power sums (heat data only), n = 2..10, 12 points each
(random, signed/rational, repeated, padded): c_n = −1, +1, +1, −1, −1, +1, +1, −1, −1 for n = 2..10, equal to
(−1)^{n(n+1)/2} in every case; claimed c_3..c_8 = +1,+1,−1,−1,+1,+1 confirmed. Gaussian-rational points n = 2..5.
Singular points {a, −a, …}: det M = 0 and z²g(z) is an explicit kernel vector. n = 1 (outside the claim) gives
M = [−R], consistent with c_1 = −1.
The other project claim c_n = (−1)^{n(n+1)/2} for every n is **correct** (and is proved above).

**Grade: MINOR.** Fix: replace "c_n ∈ Q^× … for n = 3..8 (linear_system.py)" by "c_n = (−1)^{n(n+1)/2}" with the
factorisation proof above; keep the computation as a check.

## AU.1 — Theorem C

**(1) Proof.** Let w = 1/z and F(w) = ∏(1−m_i w)∏(1+m'_j w), so Q(z) = z^{2n}F(w) and
F(w)/F(−w) = exp(−2∑_{k odd}(P_k − P'_k) w^k/k). If P_k = P'_k for odd k ≤ 2n−5, then F(w) − F(−w) = O(w^{2n−3}),
so Q(z) − Q(−z) (odd, degree ≤ 2n−1) has only z³ and z¹ terms; [z¹]Q = (−1)^{n−1}(e_{n−1}e'_n − e_n e'_{n−1}) vanishes
iff R = R'. Conversely if Q(z) − Q(−z) = 2κz³ then F(w)/F(−w) = 1 + O(w^{2n−3}), so the odd P_k agree for
k ≤ 2n−5, and [z¹]Q = 0 gives R = R'. Comparing the w^{2n−3} term: κ = (P_{2n−3}(m') − P_{2n−3}(m))/(2n−3).
κ = 0 ⇔ Q(z) = Q(−z) ⇔ A(z)A'(−z) = A(−z)A'(z) for A = ∏(z−m_i), A' = ∏(z−m'_j); under the hypothesis
gcd(A(z), A(−z)) = 1, so A | A', A' = A. (n = 2: I_1 = (R); n = 1: the condition reads m = m', consistent.)
**Checks.** All pairs sharing I_{n−1} among orders 1..30/40/30 (n = 2, 3, 4; 39, 37, 1 pairs) have Q(z)−Q(−z) = 2κz³,
κ ≠ 0; 1800 random signed pairs n = 1..6 satisfy the "iff"; {1,−1,5} vs {2,−2,5} shows κ = 0 with m ≠ m' without
the hypothesis; complex example {1+i, 1−i} vs {2,2}. **Grade: NONE.**

**(2) Proof.** The Jacobian of I_{n−1} = (R, P_1, …, P_{2n−5}) at m is the (n−1)×n matrix with rows −m_i^{−2},
(2s+1)m_i^{2s} (s = 0..n−3). Deleting column j, the minor is ±∏(2s+1)·∏_{i≠j} m_i^{−2}·V((m_i²)_{i≠j}) ≠ 0 when the
m_i are distinct and positive. Rank n−1, so by the implicit function theorem the level set through m is locally a
real-analytic curve, which stays in the open positive orthant and, near m, meets no permutation of m other than m
itself; so it gives a one-parameter family of distinct positive multisets with the same I_{n−1}.
Equivalently (Thm B's first n−2 rows plus the R row) the fibre in e-space is an affine line, and real-rootedness
with positive simple roots is open on it.
**Checks.** For 3 random distinct-integer multisets each n = 2..6, exact Sturm counts on the fibre line at
e_n = t_0(1 ± 10^{−k}) (k = 3 or 5) give n distinct positive real roots, same I_{n−1}, different P_{2n−3}.
Distinctness is needed: {3,3,3} and {4,4,4,4} lose real roots on both sides; {2,5,5} only on one side.
Sanity (mpmath, non-proof): the real arc through (2,3,5,7) is short (complex roots at e_4 = 200 and 230).
**Grade: NONE.**

**(3)** I_{n−1} is homogeneous (R of degree −1, P_k of degree k), so a positive rational pair scales to an integer
pair; scaling further makes all orders ≥ 2 and the orbifolds hyperbolic. Witnesses: {1,4,4}/{3/2,3/2,6} scales to
{2,8,8}/{3,3,12}; the n = 4 witness is the only hyperbolic class with orders ≤ 40. n = 5: reproduced by an
independent integer-only C enumeration bucketed by P_1 (validated against a pure-Python brute force at N = 22):
N = 60: 7,028,847 multisets, 134 classes share I_3 (control: the search is sensitive), none share I_4;
N = 120: 216,071,394 multisets, 2309 classes share I_3, none share I_4. **Grade: NONE.**

## AU.2 — Lemma 1

**Proof.** In Q[x][[z]], f(z)/f(−z) = exp G, G = 2∑_{k odd} s_k z^k/k. For odd j and b ≤ j, [z^b](exp G − 1) is a
polynomial in s_1, s_3, …, s_b without constant term, hence in I = (s_1, s_3, …, s_j). From f(z) − f(−z) =
f(−z)(exp G − 1): 2e_j = ∑_{b=1}^{j}(−1)^{j−b}e_{j−b}[z^b](exp G − 1) ∈ I. Conversely, f(z)/f(−z) − 1 = 2O/(E − O)
has all coefficients through z^j in J = (e_1, e_3, …, e_j) (E − O has constant term 1), so
log(f(z)/f(−z)) = log(1 + u) has its z^j coefficient 2s_j/j in J. Division by j and k needs Q. ∎
**Checks.** Explicit certificates verified identically for N = 1..5, odd j ≤ 7 (incl. N < j). **Grade: NONE**
(cosmetic: "Conversely, for odd j, s_j lies in …").

## AU.3 — Remark 2 (Jacobian) and Remark 3 (padding)

**Remark 2, proof for every n.** Rows of the Jacobian: −m_i^{−2}, then (2s+1)m_i^{2s}, s = 0..n−2. Pull out
∏_{s}(2s+1) = ∏_{r=1}^{n−1}(2r−1), the sign −1 of the first row and m_i^{−2} from column i: what remains is the
Vandermonde in m_i² with rows 1, m², …, m^{2n−2}, i.e. ∏_{i<j}(m_j²−m_i²) = V(m)∏_{i<j}(m_i+m_j). So
J = −∏_{r=1}^{n−1}(2r−1)·V(m)∏(m_i+m_j)/∏m_i² for all n. Checked symbolically n = 1..6 and at exact points
n = 8..10. Injectivity on the diagonals follows from Thm A; at m_i + m_j = 0, injectivity does fail (explicit
classes above), so the "Orlando factor is the obstruction" sentence is right.
**Remark 3, proof.** b_l(1) = 0 for all l (AU.0 (ii)), and (n, R) ↦ (n+1, R+1) leaves n−2−R fixed, so the actual
heat coefficients of an n'-cone orbifold coincide with those computed (with n fixed) from the padded n-multiset;
inverting the triangular map gives I_n(padded m') = I_n(m); Thm A (m positive, padded m' nonzero) gives padded
m' = m; m has no entry 1, so n' = n. Search (actual c_1, c_2, c_3 from (4.33)/(4.35), K = −1): no 3-cone vs 4-cone
pair with orders ≤ 60 shares c_1, c_2, c_3 (control: 9 four-cone multisets share c_1, c_2 with a three-cone one).
**Grade: MINOR.** Fixes: rename Remark 2's constant (e.g. j_n) to avoid the clash with Theorem B's c_n, write
∏_{r=1}^{n−1}, replace "(checked n ≤ 7)" by the Vandermonde proof; in Remark 3 write "every hyperbolic genus-0
orbifold with at most n cone points".

## AU.4 — integer witness table

All entries recomputed exactly (`check_AU4_definitions.txt`): n = 3: R = 3/4, S_1 = 18, P_3 = 1032 vs 1782,
Φ = 500z³; n = 4: R = 8/15, S_1 = 58, P_3 = 31402, P_5 = 25159618 vs 21298618, Φ = 1544400z³. All four multisets
hyperbolic. Φ = (−1)^{n+1}(Q(z) − Q(−z)) proved (Q(z) = (−1)^n p(−z)p'(z)) and checked symbolically n = 1..6; with
κ = (P_{2n−3}(m') − P_{2n−3}(m))/(2n−3): κ = 250 (n = 3), −772200 (n = 4), consistent with Φ. n = 5 counts are
C(63,5) and C(123,5) and the search result is reproduced (see Thm C(3)).
**Grade: MINOR** (S_1 is used for P_1; define it or write P_1).

## DF.6 — thm:Crestated

**Proof.** Within Pill_3 the count n = 3 is fixed, so H_k ↔ (R, P_1, P_3) triangularly for k ≤ 3 (AU.0). Thm A
(n = 3) gives: H_3 determines the signature, so K_mult ≤ 3; rigidity (DF.3: a genus-0 orbifold with three cone
points is determined up to isometry by its orders) gives K_iso = K_mult. K_mult ≥ 3 ⇔ H_2 fails to determine the
signature ⇔ some O' with different signature has the same (R, P_1). Hence "= 3 exactly when …".
**Check.** For every hyperbolic pillow with orders ≤ 60, competitors enumerated exactly with no bound on their
orders (for fixed R < 1 the solutions of 1/p+1/q+1/r = R are finite): no (R, P_1, P_3) collision; K_mult takes
the values 1, 2 and 3 on 6137, 29573 and 215 pillows respectively (e.g. K_mult(O(2,3,7)) = 1,
K_mult(O(2,3,12)) = 2, K_mult(O(2,8,8)) = 3); (2,8,8) and (3,3,12) are the only pillows with
R = 3/4, P_1 = 18. **Grade: NONE.**

## DF.7 — rem:nconerestated

(a) True as a conditional, but its final sentence ("for n ≥ 4 injectivity is not proved here") contradicts
Theorem A, which proves injectivity on n-element multisets of positive reals for every n. (b) The Kiso part is
correct given Prop Kinf (itself conditional on thm:locality) and dim M = 2n−6 > 0; the clause "(conditionally on
injectivity)" is stale. (c) Numbers verified; with Thm A, K_mult = 4 holds unconditionally for these two signatures
in Pill_4. Also "pillows" is used for n = 4 although DF.1 reserves the word for n = 3, and "c_1..c_n are the n
functions R, S_1, …" should say "determine and are determined by (triangularly)".
**Grade: MINOR.** Fix: in (a) replace the last sentence by "this holds for every n by Theorem A, so
K_mult(O; Pill_n) ≤ n"; drop "conditionally on injectivity" in (b); in (c) state K_mult = 4.

## Context items (DF.1–DF.5)

Checked only where they feed the above: DF.1's c_1 = Area/4π = −χ/2 = (1−R)/2 for pillows agrees with (4.35) and
Gauss–Bonnet (K·Area = 2πχ, Uçar (4.38)); DF.2's upward-closedness and K_mult ≤ K_iso are immediate. Not graded.
