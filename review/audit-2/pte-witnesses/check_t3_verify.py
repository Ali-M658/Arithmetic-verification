"""Exact verification of the T_3 search (check_t3.c) and of its planted positive control.

For a run directory, tag, N, nproc, delta:
  - coverage: every y1 in 1..N appears exactly once in the checkpoints, and the per-y1 counts
    equal the exact number of multisets y1 <= y2 <= ... <= y5 <= N, summing to C(N+4,5);
  - every survivor Y is re-examined in exact rational arithmetic: e1 = p1,
    e3 = (p3 + delta - p1^3)/(3(1 - p1 r)), e2 = r e3, and the cubic x^3 - e1 x^2 + e2 x - e3 is
    factored over Q (sympy); a SOLUTION is a Y for which it has three rational roots (then
    positive), giving Z = X + (-Y) with s1 = s3 (+delta) = s_{-1} = 0; X and Y must be disjoint.
Usage: check_t3_verify.py DIR TAG N NPROC DELTA [Y0 X0]   (e.g. 2,2,8,8,8 1,3,24)
Prints a report; exits nonzero if coverage fails, or (delta = 0) if a solution exists,
or (Y0 X0 given) if the planted pair is not among the verified solutions.
"""
import sys, glob
from fractions import Fraction as F
from math import comb
import sympy

D, TAG, N, NPROC, DELTA = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
EXPECT = len(sys.argv) > 7
if EXPECT:
    Y0 = tuple(map(int, sys.argv[6].split(','))); X0 = list(map(int, sys.argv[7].split(',')))

def count_y1(y1, N):
    # multisets of size 4 from {y1..N}
    m = N - y1 + 1
    return comb(m + 3, 4)

done = {}
for k in range(NPROC):
    for line in open(f"{D}/{TAG}_ckpt_{k}.txt"):
        _, a, c = line.split()
        a, c = int(a), int(c)
        assert a not in done, f"y1={a} done twice"
        done[a] = c
missing = [y for y in range(1, N + 1) if y not in done]
bad = [y for y, c in done.items() if c != count_y1(y, N)]
total = sum(done.values())
print(f"[{TAG}] N={N}: y1 done {len(done)}/{N}, missing {missing[:10]}, count mismatches {bad[:10]}")
print(f"[{TAG}] multisets examined: {total}; C(N+4,5) = {comb(N + 4, 5)}")
cov_ok = not missing and not bad and total == comb(N + 4, 5)

surv = []
for k in range(NPROC):
    for line in open(f"{D}/{TAG}_surv_{k}.txt"):
        surv.append(tuple(map(int, line.split())))
print(f"[{TAG}] survivors of the {16}-prime certified filter: {len(surv)}")
x = sympy.Symbol('x')
sols = []
for Y in surv:
    p1 = sum(Y); p3 = sum(y ** 3 for y in Y) + DELTA; r = sum(F(1, y) for y in Y)
    e1 = F(p1); e3 = F(p3 - p1 ** 3) / (3 * (1 - p1 * r)); e2 = r * e3
    poly = sympy.Poly(x ** 3 - sympy.Rational(e1.numerator, e1.denominator) * x ** 2
                      + sympy.Rational(e2.numerator, e2.denominator) * x
                      - sympy.Rational(e3.numerator, e3.denominator), x)
    _, facs = sympy.factor_list(poly.as_expr())
    lin = sum(m for f_, m in facs if sympy.degree(f_, x) == 1)
    if lin == 3:
        roots = []
        for f_, m in facs:
            c = sympy.Poly(f_, x).all_coeffs()
            roots += [F(int(sympy.fraction(-c[1] / c[0])[0]), int(sympy.fraction(-c[1] / c[0])[1]))] * m
        X = sorted(roots)
        if not all(t > 0 for t in X):
            assert DELTA != 0  # for the real problem e1,e2,e3 > 0 forces positive roots
            print(f"   survivor Y={Y}: three rational roots {[str(t) for t in X]}, not all positive -> not of the shape")
            continue
        assert sum(X) == p1 and sum(t ** 3 for t in X) == p3 and sum(1 / t for t in X) == r
        disjoint = not (set(X) & set(F(y) for y in Y))
        sols.append((Y, X, disjoint))
        print(f"   SOLUTION Y={Y} X={[str(t) for t in X]} disjoint={disjoint}")
    else:
        print(f"   survivor Y={Y}: cubic has {lin} rational root(s) (counted with multiplicity) -> not a solution")
print(f"[{TAG}] exact solutions: {len(sols)}")
ok = cov_ok
if DELTA == 0:
    ok = ok and not sols
    print(f"[{TAG}] RESULT: {'NO size-8 (3,5) configuration with five-element side <= %d' % N if not sols else 'SOLUTIONS FOUND'}"
          f"; coverage {'complete' if cov_ok else 'INCOMPLETE'}")
if EXPECT:
    hit = any(Y == Y0 and X == [F(t) for t in X0] for Y, X, _ in sols)
    print(f"[{TAG}] planted Y0={Y0}, X0={X0} (delta={DELTA}) recovered: {hit}")
    ok = ok and hit
sys.exit(0 if ok else 1)
