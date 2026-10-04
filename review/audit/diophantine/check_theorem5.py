"""Numerical context for Theorem 5 (DI.10) and the bound (*) of DI.8.

The statement file does not define the conic-bundle family, so the constant 3/(128 pi^4)
cannot be recomputed from it.  What is checked here, from the exact enumeration S <= 4800:
  * N(X) >= the right-hand side of (*) summed over ALL primitive pairs D (consistency of (*));
  * growth of the number A_dual(y) of primitive DUAL pairs with S <= y, against y log y
    (the order of magnitude needed for X (log X)^2 after partial summation);
  * the size of 3/(128 pi^4) X (log X)^2 relative to N(X).

Run from the repository root:
    /opt/homebrew/Caskroom/miniforge/base/bin/python3 review/audit/diophantine/check_theorem5.py
"""
import os
import sys
from math import gcd, log, pi

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from dio_common import check, finish, Fail  # noqa: E402
from check_enum import parse, gcd_all, is_dual, ENUM  # noqa: E402

OUT = os.path.join(HERE, "check_theorem5.txt")
log_ = []
c5 = 3 / (128 * pi ** 4)
try:
    with open(ENUM) as fh:
        stats, classes = parse(fh.read())
    prim, dual = [], []
    for c in classes:
        m = c["mem"]
        for i in range(len(m)):
            for j in range(i + 1, len(m)):
                if gcd_all([m[i], m[j]]) == 1:
                    prim.append(c["S"])
                    if is_dual(m[i], m[j]):
                        dual.append(c["S"])
    prim.sort()
    dual.sort()
    cum, run = {}, 0
    for S in range(10, 4801):
        run += stats[S]["pairs"]
        cum[S] = run
    log_.append(f"     c5 = 3/(128 pi^4) = {c5:.3e}")
    log_.append("     X      N(X)     sum_D#{k>=4}   c5 X log^2 X   A_prim(X)  A_dual(X)  A_dual/(X log X)")
    ok = True
    for X in [600, 1200, 2400, 3600, 4800]:
        rhs = sum(X // s - 3 for s in prim if 4 * s <= X)
        Ad = sum(1 for s in dual if s <= X)
        Ap = sum(1 for s in prim if s <= X)
        log_.append(f"     {X:<6d} {cum[X]:<8d} {rhs:<14d} {c5*X*log(X)**2:<14.1f} {Ap:<10d} {Ad:<10d} {Ad/(X*log(X)):.4f}")
        ok &= cum[X] >= rhs >= c5 * X * log(X) ** 2
    check(ok, "N(X) >= RHS of (*) (all primitive pairs) >= 3/(128pi^4) X log^2 X on the computed range", log_)
    log_.append("     note: A_dual counts only hyperbolic primitive dual pairs (non-hyperbolic primitive D are absent "
                "from the enumeration); the ratio A_dual/(X log X) is the quantity that must stay bounded below.")
    log_.append("ALL THEOREM-5 CONTEXT CHECKS PASSED")
    finish(log_, OUT)
except Fail:
    finish(log_, OUT)
    sys.exit(1)
