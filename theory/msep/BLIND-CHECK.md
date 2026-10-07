# Blind check of Theorem msep (statement only)

A subagent was given only the statement of Theorem msep (parts (i), (ii), the M = 3 and M = 4
examples and the corollary) with the definitions of the heat invariants c_j (Proposition 2.7 of the
manuscript: alpha_k, b_l, p_l, phi_k); it was told not to open this directory and did not see
`proof.tex` or `verify.py`. It wrote its own implementation of the coefficients and its own scripts
(kept in the session scratch directory, not committed). Date: 2026-10-07.

## Verdict: TRUE

No mathematical error and no counterexample. Its own proofs:

- **Reduction.** Equal c_1 is equal area; then c_j (j >= 2) agree iff the cone sums agree; since
  p_l(m) = (m^2 - 1) q_l(m^2) with deg q_l = l and positive leading coefficient, the change of basis
  is triangular, so H_L agree iff sum_a d(a) (a^2 - 1)/a * a^{2j} = 0 for j = 0..L-2, with
  g' - g = (1/2) sum_a d(a)(1 - 1/a).
- **(i).** For L = M this is a Vandermonde system in the distinct a^2 (after removing the nonzero
  column factors), so d = 0 and g = g'; M = 2 and surfaces are covered.
- **(ii).** The Lagrange identity at the nodes 1^2, ..., M^2 gives the vanishing for j <= M - 3 and
  Delta c_M = (-1)^M C lead(p_{M-2}) != 0; "least C" is well defined; g' >= 0 and hyperbolicity of
  both sides follow from the choice of g and equal areas; every w_a != 0, so the signatures differ.
- **Corollary.** Immediate from (i) with M = L.

## Its computations (exact)

| check | result |
|---|---|
| implementation | alpha_0..alpha_4 and p_0, p_1, p_2 as stated; p_l even, degree 2l+2, p_l(1) = 0 for l <= 7 |
| pairs of (ii), M = 2..20, least admissible g | all hyperbolic, orders in [2, M], signatures different, c_1..c_{M-1} equal, c_M different; e.g. M = 3: C = 120, area 12 pi, Delta c_3 = -1/3; M = 4: C = 2520, area 36 pi, Delta c_4 = 1 |
| brute force, M = 2 (area <= 60 pi), 3 (<= 32 pi), 4 (<= 40 pi) | no collision of H_M; least area sharing H_{M-1}: pi for M = 2, 12 pi for M = 3, 36 pi for M = 4 |
| examples | confirmed, including minimality for M = 3, 4 |

## Notes it raised, and what was done

1. For M = 2 the least choice of (ii) is (1; 2^4) against (2;), area 4 pi, while (0; 2^5) against
   (1; 2), area pi, also shares c_1: a common cone point added to a non-hyperbolic pair. The theorem
   claims minimality only for M = 3, 4. **Done:** proof.tex says that the least choice need not
   have least area, and that common cone points can be added to both sides.
2. Hyperbolicity of the second side follows from equal areas. **Done:** said explicitly.
3. Delta c_M can be given as a formula. **Done:** Delta c_M = (-1)^M C a_{M-2} is now in (ii), and
   verify.py asserts it.
4. Empirically C = (2M - 1)! or (2M - 1)!/2 for small M. Not used; not added.

# Blind check of part (iii) (arbitrary competitors) and the corollary

A second subagent was given only the statement of part (iii) and of corollary (b), with the same
definitions and, as known facts, Lemma lem:sigdata and part (i); it did not see `proof.tex`.

## Verdict: TRUE

- **Order bound.** Its proof: with j = 2L - 3, m'^j <= P_j(V) = P_j(U) <= |U| M^j; edge cases
  (O' a surface, O a surface, either sign of d, M = 2) checked.
- **K_mult bound.** Its proof of M + 2 + floor(log N), N = 2 floor(A/pi) + 8, by bounding
  M N^(1/(2L-3)) - M.
- **Improvement it found.** The same method gives K_mult <= M + ceil((log N)/2): with
  L = M + k, k = ceil((log N)/2) >= 2, the bound log(1 + x) > 2x/(2 + x) at x = (k + 1)/M reduces
  the needed inequality to 2M + (k - 3)(k + 1) > 0. It confirmed this by an exact integer test for
  M < 400 and N up to 10^29.
- **Its computation.** Complete equal-area classes (orders unbounded) for every s = k/12 <= 2,
  for s = 25/12 .. 11/4 and s = 3: no failure of the order bound on 267,898 pairs sharing at least
  two invariants, and no failure of the K_mult bound. The largest K_mult observed was M + 1
  (for example (0; 2^10) against (1; 4,4,4,4) at s = 3, M = 2), so the logarithmic term was never
  needed in its data.

## What was done

The improvement was adopted, after checking the argument independently: part (iii) now reads
K_mult(O; Sig) <= M + ceil((1/2) log(2 floor(A/pi) + 8)), with the proof in `proof.tex`
(the inequality (2L-3) log((L+1)/M) > 2k >= lambda); corollary (b) and (c) and the manuscript
(Theorem 1.1(iii), Theorem thm:bounded(iii), Corollary cor:bounded, the remark after
Theorem thm:growth) were changed accordingly. `verify.py` checks the new bound on the complete
classes (section 7) and the integer inequality (L+1)^(2L-3) > N M^(2L-3) (section 8).
