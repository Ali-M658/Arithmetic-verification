"""Theorem N(a) (SG.10 / thm:signonuniform (a)): referee's own construction, built and checked.

Construction (D = 2L-2, eps_i = (-1)^{t(i)}, i < 2^D):
  block 1: x_i = 3i - 1  (only i = 0 is negative, value -1),  r1 = sum eps_i/x_i < 0
  block 2: y_i = 3i + 2  (all >= 2),                          r2 = sum eps_i/y_i > 0
  r2/(-r1) = a/b in lowest terms; lam1 = 2b, lam2 = 2a  (factor 2 keeps every entry >= 2)
  X = {lam1 eps_i x_i} + {lam2 eps_i y_i};  U = positive part of X,  V = -(negative part).
  O  = (g'+1; U),  O' = (g'; V).
Claims verified:
  |U| = 2^D - 1, |V| = 2^D + 1, all entries >= 2, both hyperbolic,
  H_L(O) = H_L(O') and H_{L+1}(O) != H_{L+1}(O')  (actual cone coefficients b_l, Ucar (4.33)),
  for g' = 0: Area(O) < 2 pi (4^{L-1} - 1).
Full element-wise check with b_l for L = 2..6; for L = 7..9 the same identities are checked
through the block moments (exact, using b_l = (-1)^l p_l(x)/x with p_l from Ucar).
"""
import os
import sys
import time
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sigcommon import thue_morse, fsum_recip, shared_count, s_of, p_poly  # noqa: E402

F = Fraction


def build(L):
    D = 2 * L - 2
    eps = [(-1 if thue_morse(i) else 1) for i in range(2 ** D)]
    xs = [3 * i - 1 for i in range(2 ** D)]
    ys = [3 * i + 2 for i in range(2 ** D)]
    r1 = F(-1) + fsum_recip([xs[i] for i in range(1, 2 ** D) if eps[i] > 0]) \
        - fsum_recip([xs[i] for i in range(1, 2 ** D) if eps[i] < 0])
    r2 = fsum_recip([ys[i] for i in range(2 ** D) if eps[i] > 0]) \
        - fsum_recip([ys[i] for i in range(2 ** D) if eps[i] < 0])
    assert r1 < 0 < r2
    q = r2 / (-r1)
    lam1, lam2 = 2 * q.denominator, 2 * q.numerator
    X1 = [eps[i] * xs[i] for i in range(2 ** D)]
    X2 = [eps[i] * ys[i] for i in range(2 ** D)]
    return D, eps, lam1, lam2, X1, X2, r1, r2


def split(lam1, lam2, X1, X2):
    U = [lam1 * v for v in X1 if v > 0] + [lam2 * v for v in X2 if v > 0]
    V = [-lam1 * v for v in X1 if v < 0] + [-lam2 * v for v in X2 if v < 0]
    return U, V


def moment(X, j):
    if j == -1:
        return fsum_recip([v for v in X if v > 0]) - fsum_recip([-v for v in X if v < 0])
    return sum(v ** j for v in X)


report = []
for L in range(2, 10):
    t0 = time.time()
    D, eps, lam1, lam2, X1, X2, r1, r2 = build(L)
    # reciprocal balance
    assert r1 / lam1 + r2 / lam2 == 0
    # sizes and entries, from the sign pattern (no need to form U, V)
    nU = sum(1 for v in X1 if v > 0) + sum(1 for v in X2 if v > 0)
    nV = sum(1 for v in X1 if v < 0) + sum(1 for v in X2 if v < 0)
    assert nU == 2 ** D - 1 and nV == 2 ** D + 1
    assert min(abs(v) for v in X1) == 1 and min(abs(v) for v in X2) == 2
    assert lam1 >= 2 and lam2 >= 2  # so every entry of U, V is >= 2
    # reduced identities via moments: s_j(X) = lam1^j M_j(X1) + lam2^j M_j(X2)
    mom = {}
    for j in [-1] + list(range(1, 2 * L, 2)):
        mom[j] = F(lam1) ** j * moment(X1, j) + F(lam2) ** j * moment(X2, j)
    for j in [-1] + list(range(1, 2 * L - 2, 2)):
        assert mom[j] == 0, (L, j)
    assert mom[2 * L - 1] != 0
    # cone-sum differences via p_l coefficients: Delta C_l = (-1)^l sum_i [x^{2i}]p_l * s_{2i-1}(X)
    for l in range(0, L):
        P = p_poly(l)
        dC = sum(P[2 * i] * mom[2 * i - 1] for i in range(l + 2))
        if l <= L - 2:
            assert dC == 0
        else:
            assert dC != 0
    # area: s(O) for g' = 0 is |U| - R(U) with R(U) > 0
    RU = F(1, lam1) * fsum_recip([v for v in X1 if v > 0]) + F(1, lam2) * fsum_recip([v for v in X2 if v > 0])
    sO = nU - RU
    assert 0 < sO < 4 ** (L - 1) - 1  # Area/2pi < 4^{L-1}-1, strictly
    full = "moments"
    if L <= 6:
        U, V = split(lam1, lam2, X1, X2)
        assert len(U) == nU and len(V) == nV and min(U + V) >= 2
        for gp in (0, 1, 2):
            sU, sV = s_of(gp + 1, U), s_of(gp, V)
            assert sU == sV and sU > 0
            sc = shared_count(gp + 1, U, gp, V, cap=L + 1)
            assert sc == L, (L, gp, sc)
        assert s_of(1, U) == sO
        full = "full b_l, g'=0,1,2"
    digs = int(max(lam1, lam2).bit_length() * 0.30103) + 1
    line = (f"L={L} D={D} |U|={nU} |V|={nV} lam digits={digs} "
            f"Area/2pi(g'=0)={float(sO):.3f} < 4^(L-1)-1={4 ** (L - 1) - 1}  "
            f"shared exactly L [{full}]  ({time.time() - t0:.1f}s)")
    print(line, flush=True)
print("ALL CHECKS PASSED")
