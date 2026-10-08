# theory/msep: bounded cone orders (referee round 3, item I6)

| file | content |
|---|---|
| `proof.tex` | Theorem msep (Theorem 3.7 of `paper/jga/manuscript.tex`, Theorem 3.4 of `paper/eigen/manuscript.tex` for part (i)): (i) the first M heat invariants determine the signature among orbifolds with cone orders <= M; (ii) M is optimal, with explicit pairs; (iii) against all orbifolds, M + 1 suffice, uniformly in the area, and 2 d_O + 2 with d_O distinct orders (round 4, sign-change argument); (iv) M + 1 is attained, for every integer X > M (Lagrange weights on 1^2..M^2, X^2; M = 2, X = 4 is (0;2^10), (1;4^4), area 6 pi); and the corollary that the growth of the count needs large orders. A fragment in the manuscript's macros. |
| `verify.py` | exact checks: ranks for 2 <= M <= 24 (two formulations, sympy cross-check), the determinant identity, the Lagrange kernel, the sharp pairs with Delta c_M = (-1)^M C a_{M-2}, brute force for M <= 4, parts (iii)-(iv) on complete area classes with unbounded orders (sign changes checked pair by pair) and the attaining pairs. About 3 minutes; stage "msep bounded cone orders" of `code/run_all.sh`. |
| `BLIND-CHECK.md` | two statement-only checks by subagents, with their verdicts and what was changed. |

Run: `python3 verify.py` (Python with sympy and mpmath; uses `theory/eigen/eigen_common.py`).
