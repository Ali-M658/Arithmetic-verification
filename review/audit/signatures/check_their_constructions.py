"""Phase 2: rebuild the Theorem N constructions exactly as written in proof.md section 4
(text only, not their code), and check them with this folder's own cone coefficients.

N(a): D = 2L-2, U0 = {2i-1 : i in T0, i >= 1}, V0 = {2i-1 : i in T1} + {1},
      A' = {2i+1 : T0}, B' = {2i+1 : T1}, r0 = R(U0)-R(V0), rho = R(A')-R(B') > 0;
      swap A', B' if needed so rho/r0 > 0; rho/r0 = p/q, doubled if min(p,q) = 1;
      U = qU0 + pB', V = qV0 + pA';  O = (g'+1; U), O' = (g'; V).
N(b): D = 2k-2, A = {i+1 : T0}, B = {i+1 : T1}, r0 = R(A)-R(B) > 0, rho as above,
      r0/rho = sum 1/p_i (distinct p_i >= 2: harmonic start, then greedy),
      U = A + sum p_i B', V = B + sum p_i A';  O = (0; U minus 1), O' = (0; V).
"""
import os
import sys
import time
from fractions import Fraction
from math import ceil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sigcommon import thue_morse, fsum_recip, shared_count, s_of  # noqa: E402

F = Fraction


def split(D):
    T0 = [i for i in range(2 ** D) if not thue_morse(i)]
    T1 = [i for i in range(2 ** D) if thue_morse(i)]
    return T0, T1


def odd_moments_equal(U, V, upto):
    return all(sum(x ** j for x in U) == sum(x ** j for x in V) for j in range(1, upto + 1, 2))


print("N(a), as written:")
for L in range(2, 7):
    t0 = time.time()
    D = 2 * L - 2
    T0, T1 = split(D)
    U0 = [2 * i - 1 for i in T0 if i >= 1]
    V0 = [2 * i - 1 for i in T1] + [1]
    Ap = [2 * i + 1 for i in T0]
    Bp = [2 * i + 1 for i in T1]
    assert V0.count(1) == 2          # i = 1 lies in T1 and gives 2*1-1 = 1, plus the added 1
    r0 = fsum_recip(U0) - fsum_recip(V0)
    rho = fsum_recip(Ap) - fsum_recip(Bp)
    assert rho > 0 and r0 < 0        # r0 < 0 always: the swap branch is the one used
    Ap, Bp, rho = Bp, Ap, -rho
    ratio = rho / r0
    p, q = ratio.numerator, ratio.denominator
    doubled = min(p, q) == 1
    if doubled:
        p, q = 2 * p, 2 * q
    U = [q * u for u in U0] + [p * b for b in Bp]
    V = [q * v for v in V0] + [p * a for a in Ap]
    assert min(U + V) >= 2
    assert len(U) == 2 ** D - 1 and len(V) == 2 ** D + 1
    assert fsum_recip(U) == fsum_recip(V) and odd_moments_equal(U, V, 2 * L - 3)
    for gp in (0, 1):
        assert s_of(gp + 1, U) == s_of(gp, V) > 0
        assert shared_count(gp + 1, U, gp, V, cap=L + 1) == L
    sV = s_of(0, V)
    assert sV < 4 ** (L - 1) - 1 and sV < -2 + len(V)
    print(f"  L={L}: q={q if q < 10**6 else '~10^%d' % (len(str(q)) - 1)}, "
          f"min(p,q)=1 occurred: {doubled}; |U|={len(U)}, |V|={len(V)}, entries >= 2, "
          f"Area/2pi < 4^(L-1)-1, shares exactly {L} (g'=0,1)  ({time.time() - t0:.1f}s)", flush=True)


def egypt_text(x):
    """Harmonic start 1/2 + 1/3 + ... while <= x, then Fibonacci-Sylvester greedy."""
    out, p = [], 2
    while F(1, p) <= x:
        x -= F(1, p)
        out.append(p)
        p += 1
    while x > 0:
        d = ceil(1 / x)
        out.append(d)
        x -= F(1, d)
    return out


print("N(b), as written:")
for k in (2, 3, 4):
    D = 2 * k - 2
    T0, T1 = split(D)
    A = [i + 1 for i in T0]
    B = [i + 1 for i in T1]
    Ap = [2 * i + 1 for i in T0]
    Bp = [2 * i + 1 for i in T1]
    r0 = fsum_recip(A) - fsum_recip(B)
    rho = fsum_recip(Ap) - fsum_recip(Bp)
    assert r0 > 0 and rho > 0
    q = r0 / rho
    if k == 4:
        # do not run the greedy to completion: report the size of the problem
        print(f"  k=4: r0/rho = {float(q):.6f} (>= 1: {q >= 1}), numerator has {len(str(q.numerator))} digits; "
              f"greedy not run (doubly exponential denominators)")
        continue
    ps = egypt_text(q)
    assert sum(F(1, x) for x in ps) == q and len(set(ps)) == len(ps) and min(ps) >= 2
    U = A + [x * y for x in ps for y in Bp]
    V = B + [x * y for x in ps for y in Ap]
    assert len(U) == len(V) and U.count(1) == 1 and V.count(1) == 0
    m = [x for x in U if x != 1]
    assert min(m) >= 2
    assert s_of(0, m) == s_of(0, V) > 0
    sc = shared_count(0, m, 0, V, cap=k + 1)
    assert sc == k
    print(f"  k={k}: r0/rho = {q} (>= 1: {q >= 1}); {len(ps)} unit fractions, largest denominator "
          f"{max(ps).bit_length()} bits; n = {len(m)} vs n+1 = {len(V)}; shares exactly {sc}")
    if k == 2:
        assert (len(m), len(V)) == (9, 10)
    if k == 3:
        assert (len(m), len(V)) == (103, 104)
print("ALL CHECKS PASSED")
