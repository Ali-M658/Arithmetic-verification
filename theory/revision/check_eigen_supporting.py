"""Checks for supporting statements of the eigenvalue paper (paper/eigen/manuscript.tex): the count of closed
geodesics without the diameter (Lemma 4.5) and its use in Theorem 6.2, and two steps of Appendix A.

Run from the repository root:
    python3 theory/revision/check_eigen_supporting.py
Writes theory/revision/check_eigen_supporting.txt.  Exits nonzero on any failed assertion.

1. Lemma 4.5: K(A, eps, M) = A M e^{10 r_0 + rho_1} / (2 v_0 (cosh rho_1 - 1)), with r_0, rho_1, v_0 of
   Lemma 4.3; the values in theory/eigen/data/table2.csv are those of the formula, and the committed length
   spectra of the family (0;3,3,3,3) (numerics/moduli/data/length_spectra.csv) satisfy n(x) <= K e^x for
   every listed length, with K for the class C(4 pi/3, systole, 3) and the count of classes bounded above
   by w(x)/systole (each class of length x has primitive length at least the systole).
2. The intermediate inequality of the proof: (A/v_0) M (cosh(x + 10 r_0 + rho_1) - 1)/(cosh rho_1 - 1) <= K e^x.
3. Theorem 3.2(ii): det(y_a^k - 1), 1 <= k <= M-1, 2 <= a <= M, y_a = a^2, equals prod_{a<b}(y_b - y_a)
   (Vandermonde with the column a = 1 subtracted), for M <= 12.
4. Appendix A, Proposition 2.3(b): mu_k = 4 int_0^inf r^{2k+1}/(e^{2 pi r}+1) dr = (1 - 2^{-2k-1})(-1)^k
   B_{2k+2}/(k+1), and alpha_k from the mu_k equals the Bernoulli-polynomial formula, k <= 8.
"""
import csv
import os
import sys
from fractions import Fraction as Fr
from math import comb, factorial

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "theory", "eigen"))
from eigen_common import count_constant, ball_constants, alpha, bernoulli  # noqa: E402

mp.mp.dps = 40
out = []


def say(s):
    print(s)
    out.append(s)


# 1. table2 values and the family length spectra
for r in csv.DictReader(open(os.path.join(ROOT, "theory/eigen/data/table2.csv"))):
    A = {"pi/2": mp.pi / 2, "4pi/3": 4 * mp.pi / 3, "2pi": 2 * mp.pi, "10pi": 10 * mp.pi}[r["A"]]
    K = count_constant(A, mp.mpf(r["eps"]), int(r["M"]))
    assert abs(K / mp.mpf(r["K"]) - 1) < mp.mpf("1e-4"), (r, K)
say("1. table2.csv: K equals the formula of Lemma 4.5 in all rows")
fam = {}
for r in csv.DictReader(open(os.path.join(ROOT, "numerics/moduli/data/length_spectra.csv"))):
    fam.setdefault(r["tau"], []).append((float(r["length"]), float(r["weight_w"])))
inst = {r["orbifold"]: r for r in csv.DictReader(open(os.path.join(ROOT, "theory/eigen/data/instances.csv")))}
worst = 0.0
for tau, rows in fam.items():
    sysl = mp.mpf(inst[f"O_tau={tau}"]["systole_lower_bound"])
    K = count_constant(4 * mp.pi / 3, sysl, 3)
    rows.sort()
    n = mp.mpf(0)
    for x, w in rows:
        n += mp.mpf(w) / sysl
        worst = max(worst, float(n / (K * mp.e ** x)))
        assert n <= K * mp.e ** mp.mpf(x)
say(f"1. family length spectra: n(x) <= K e^x at every listed length (largest ratio {worst:.2e})")

# 2. the intermediate inequality
for A, eps, M in ((mp.pi / 2, mp.mpf("1.8626"), 12), (4 * mp.pi / 3, mp.mpf("0.6939"), 3), (10 * mp.pi, mp.mpf(1), 12)):
    r0, rho1, v0 = ball_constants(eps, M)
    K = count_constant(A, eps, M)
    for x in (0.1, 1, 5, 20, 80):
        lhs = A / v0 * M * (mp.cosh(x + 10 * r0 + rho1) - 1) / (mp.cosh(rho1) - 1)
        assert lhs <= K * mp.e ** x
    assert 2 * r0 >= 2 * rho1 and eps >= 4 * r0 - mp.mpf(10) ** -30      # d_0 = 2 r_0 <= eps/2, rho_1 <= r_0
say("2. Lemma 4.5: the counting bound is at most K e^x; d_0 = 2 r_0 <= eps/2 and rho_1 <= r_0")

# 3. Vandermonde step of Theorem 3.2(ii)
for M in range(2, 13):
    y = [sp.Integer(a * a) for a in range(1, M + 1)]
    mat = sp.Matrix(M - 1, M - 1, lambda k, j: y[j + 1] ** (k + 1) - 1)
    rhs = sp.prod([y[b] - y[a] for a in range(M) for b in range(a + 1, M)])
    assert mat.det() == rhs, M
say("3. Theorem 3.2(ii): det(y_a^k - 1) = prod (y_b - y_a), M <= 12")

# 4. Appendix A, moments of the area term
for k in range(0, 9):
    mu = 4 * mp.quad(lambda r: r ** (2 * k + 1) / (mp.e ** (2 * mp.pi * r) + 1), [0, 1, 5, mp.inf])
    exact = Fr(1) - Fr(1, 2 ** (2 * k + 1))
    exact = exact * (-1) ** k * bernoulli(2 * k + 2) / (k + 1)
    assert abs(mu - mp.mpf(exact.numerator) / exact.denominator) < mp.mpf(10) ** -30, k
mus = [(Fr(1) - Fr(1, 2 ** (2 * j + 1))) * (-1) ** j * bernoulli(2 * j + 2) / (j + 1) for j in range(9)]
for k in range(0, 9):
    ak = Fr(-1, 4) ** k / factorial(k) - sum((-1) ** j * mus[j] / factorial(j) * Fr(-1, 4) ** (k - 1 - j) / factorial(k - 1 - j)
                                             for j in range(k))
    assert ak == alpha(k), (k, ak, alpha(k))
say("4. Appendix A: mu_k in closed form, and alpha_k from the moments equals the Bernoulli formula, k <= 8")

# 5. (round 8, the remark after Theorem 4.4) Jorgensen's inequality for two elliptic elements: rotations f, g by
#    2 pi/p and 2 pi/q about points at distance d have tr[f,g] - 2 = 4 sin^2(pi/p) sin^2(pi/q) sinh^2 d, so
#    |tr^2 f - 4| + |tr[f,g] - 2| >= 1 reads 4 sin^2(pi/p) (1 + sin^2(pi/q) sinh^2 d) >= 1; in the (2,3,7) triangle group
#    the bound is attained by the cone points of orders 7 and 2 and of orders 7 and 3.
def rot(theta, d):
    """rotation by 2 theta about the point e^d i of the upper half-plane"""
    R = mp.matrix([[mp.cos(theta), mp.sin(theta)], [-mp.sin(theta), mp.cos(theta)]])
    S = mp.matrix([[mp.e ** (d / 2), 0], [0, mp.e ** (-d / 2)]])
    return S * R * S ** -1


def comm_trace(p, q, d):
    f, g = rot(mp.pi / p, 0), rot(mp.pi / q, d)
    C = f * g * f ** -1 * g ** -1
    return C[0, 0] + C[1, 1]


for p, q, d in ((7, 2, mp.mpf("0.3")), (5, 3, mp.mpf("1.1")), (12, 8, mp.mpf("0.05")), (3, 3, mp.mpf("2.0"))):
    lhs = comm_trace(p, q, d) - 2
    rhs = 4 * mp.sin(mp.pi / p) ** 2 * mp.sin(mp.pi / q) ** 2 * mp.sinh(d) ** 2
    assert abs(lhs - rhs) < mp.mpf(10) ** -25, (p, q, lhs, rhs)


def jorgensen_d(p, q):
    s = 1 - 4 * mp.sin(mp.pi / p) ** 2
    return mp.asinh(mp.sqrt(s / (4 * mp.sin(mp.pi / p) ** 2 * mp.sin(mp.pi / q) ** 2)))


# (2,3,7): cosh of the side opposite the angle pi/r is (cos(pi/p)cos(pi/q) + cos(pi/r))/(sin(pi/p) sin(pi/q))
side = lambda a, b, c: mp.acosh((mp.cos(mp.pi / a) * mp.cos(mp.pi / b) + mp.cos(mp.pi / c)) / (mp.sin(mp.pi / a) * mp.sin(mp.pi / b)))
assert abs(jorgensen_d(7, 2) - side(7, 2, 3)) < mp.mpf(10) ** -25
assert abs(jorgensen_d(7, 3) - side(7, 3, 2)) < mp.mpf(10) ** -25
assert abs(jorgensen_d(7, 2) - mp.acosh(1 / (2 * mp.sin(mp.pi / 7)))) < mp.mpf(10) ** -25
say(f"5. Jorgensen for elliptic pairs: tr[f,g]-2 = 4 sin^2(pi/p) sin^2(pi/q) sinh^2 d; bound attained in (2,3,7): "
    f"d(7,2) = {mp.nstr(jorgensen_d(7, 2), 7)}, d(7,3) = {mp.nstr(jorgensen_d(7, 3), 7)}")

open(os.path.join(HERE, "check_eigen_supporting.txt"), "w").write("\n".join(out) + "\n")
print("ALL CHECKS PASSED")
