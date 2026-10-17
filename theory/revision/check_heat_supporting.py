"""Checks for supporting statements of the heat-invariant paper (paper/jga/manuscript.tex): the bound (6) and
its failure to bracket, Lemma B.3 and Remark B.4, the least area of the minimal pair (Theorem 5.7), the
wave-trace kernel (Remark 4.3), the flat-cone image sums of the Introduction, U\u00e7ar's normalisation
(Remark 2.9) and the signs in Theorem B.

Run from the repository root:
    python3 theory/revision/check_heat_supporting.py
Writes theory/revision/check_heat_supporting.txt.  Exits nonzero on any failed assertion.

1. (A1) Consecutive truncations do not bracket G = I + E in general (three counterexamples), while the
   sharper form of (6), |remainder| <= max(area bound, cone bound), holds on a scan of signatures: the
   area and cone remainders of Proposition B.2 have opposite signs.
2. (A7) Lemma B.3: with exact values of G at n times, the Vandermonde reconstruction of c_1..c_n is
   within ||V^{-1}||_inf max_k t_k * Q_n t_k^{n-1}; and the bound printed in the remark for O(2,8,8).
3. (a33) Among collisions of (c_1, c_2) between hyperbolic triangle orbifolds, the reciprocal sum R is
   at most 3/4, with equality only for {(2,8,8), (3,3,12)}: so the minimal pair is the unique collision
   of least area.  Proof step checked: max R over triads with least order >= 3 and sum S is
   2/3 + 1/(S-6) (majorisation), and R is injective on the triads (2, q, S-2-q).
4. (A5) Wave-trace kernel: int e^{iru} cosh(ar)/cosh(pi r) dr = 2 cos(a/2) cosh(u/2)/(cos a + cosh u)
   for |a| < pi; with a = pi - 2 theta_j its singularities nearest the real axis are at u = +-2 i theta_j,
   so a cone point of order m gives a kernel analytic in |Im u| < 2 pi/m with poles at +-2 pi i/m.
5. (A5) Flat-cone image sum 4 pi t h_t(x,x) = sum_j exp(-(2 r sin(pi j/m))^2/4t) at m = 12, t = 0.02:
   about 1.8 at r = sqrt(t)/sin(pi/m), above 1.03 at twice that, within 1% of 1 from three times that on.
"""
import itertools
import os
import sys
from fractions import Fraction as Fr

import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "eigen"))
from eigen_common import alpha, b_cone, heat_coeffs, elliptic_term, identity_term, area_over_2pi  # noqa: E402

out = []


def say(*a):
    s = " ".join(str(x) for x in a)
    print(s)
    out.append(s)


def F(x):
    return mp.mpf(x.numerator) / x.denominator


# ---------------------------------------------------------------- 1. bracketing and the sharper (6)
_cache = {}


def E_c(m, t):
    if ("E", m, t) not in _cache:
        _cache[("E", m, t)] = elliptic_term(m, t, 40)
    return _cache[("E", m, t)]


def I_c(t):
    """I(t) for area 4 pi (I is linear in the area)."""
    if ("I", t) not in _cache:
        _cache[("I", t)] = identity_term(4 * mp.pi, t, 40)
    return _cache[("I", t)]


def pieces(g, orders, t, K):
    """Area remainder, cone remainder and the bounds of Proposition B.2 for G - sum_{j<=K+1} c_j t^{j-2}."""
    s = area_over_2pi(g, orders)
    area = 2 * mp.pi * F(s)
    I = I_c(t) * area / (4 * mp.pi)
    RI = I - area / (4 * mp.pi) * sum(F(alpha(k)) * mp.mpf(t) ** (k - 1) for k in range(K + 1))
    RE = sum(E_c(m, t) - sum(F(b_cone(l, m)) * mp.mpf(t) ** l for l in range(K)) for m in orders)
    bI = F(s) / 2 * abs(F(alpha(K + 1))) * mp.mpf(t) ** K
    bE = sum(abs(F(b_cone(K, m))) for m in orders) * mp.mpf(t) ** K
    return RI, RE, bI, bE


mp.mp.dps = 40
for (g, orders, t, K) in [(2, (2,), 0.05, 1), (4, (2,), 0.05, 2), (3, (2,), 0.2, 2)]:
    RI, RE, bI, bE = pieces(g, orders, t, K)
    R = RI + RE
    c = heat_coeffs(g, orders, K + 2)
    nxt = F(c[K + 1]) * mp.mpf(t) ** K
    brackets = (R * nxt >= 0) and abs(R) <= abs(nxt)
    assert not brackets, (g, orders, t, K)
    say(f"1. no bracketing: ({g};{orders}) t={t} K={K}: R={mp.nstr(R, 6)}, next term {mp.nstr(nxt, 6)}")

checked = 0
for g in range(0, 4):
    for n in range(0, 6):
        for orders in itertools.combinations_with_replacement([2, 3, 4, 8, 12], n):
            if area_over_2pi(g, orders) <= 0 or (g == 0 and n < 3):
                continue
            for t in (0.01, 0.05, 0.2):
                for K in range(0, 4):
                    RI, RE, bI, bE = pieces(g, orders, t, K)
                    tol = mp.mpf(10) ** -30
                    assert RI * (-1) ** (K + 1) >= -tol and abs(RI) <= bI + tol, ("B.2(b)", g, orders, t, K)
                    assert RE * (-1) ** K >= -tol and abs(RE) <= bE + tol, ("B.2(a)", g, orders, t, K)
                    assert abs(RI + RE) <= max(bI, bE) + tol, ("max bound", g, orders, t, K)
                    checked += 1
    if g == 1:
        break      # genus 0 and 1 suffice for the scan; higher genus only scales the area term
say(f"1. sharper (6): |R| <= max(area bound, cone bound) and the signs of Proposition B.2 hold in {checked} cases")

# ---------------------------------------------------------------- 2. Lemma B.3
def vinv_norm(ts):
    V = mp.matrix([[mp.mpf(tk) ** j for j in range(len(ts))] for tk in ts])
    W = V ** -1
    return W, max(sum(abs(W[i, j]) for j in range(len(ts))) for i in range(len(ts)))


def Qn(n, mu0):
    """max((n-2)|alpha_n|/2, n |b_{n-1}(mu0)|): bound of the remainder coefficient for genus 0, n cone points
    (Lemma B.3; the area and cone remainders have opposite signs, so the larger bound suffices)."""
    return max(Fr(n - 2, 2) * abs(alpha(n)), n * abs(b_cone(n - 1, mu0)))


for orders in [(2, 8, 8), (3, 3, 12), (2, 3, 7), (3, 3, 3, 3)]:
    n = len(orders)
    c = heat_coeffs(0, orders, n)
    mu0 = max(orders)
    for tn in (0.002, 0.01):
        ts = [tn * mp.mpf(0.5) ** (n - 1 - k) for k in range(n)]
        W, nv = vinv_norm(ts)
        z = [mp.mpf(tk) * (identity_term(2 * mp.pi * F(area_over_2pi(0, orders)), tk, 40)
                           + sum(elliptic_term(m, tk, 40) for m in orders)) for tk in ts]
        ct = W * mp.matrix(z)
        err = max(abs(ct[j] - F(c[j])) for j in range(n))
        bound = nv * max(mp.mpf(tk) * F(Qn(n, mu0)) * mp.mpf(tk) ** (n - 1) for tk in ts)
        assert err <= bound, (orders, tn, err, bound)
        say(f"2. Lemma B.3 {orders} t_n={tn}: max |c~ - c| = {mp.nstr(err, 4)} <= {mp.nstr(bound, 4)}")

# Remark: O(2,8,8) and O(3,3,12) with a-priori mu0 = 12, systole >= 1.8626, diam <= 2.448, area >= pi/2,
# exact trace values (eta = 0): best delta_1 over geometric time grids, against delta_thm(2,8,8) = 3.80e-7.
l0, D, A0 = mp.mpf("1.8626"), mp.mpf("2.448"), mp.pi / 2


def Bhyp(t):
    t = mp.mpf(t)
    return (mp.pi * mp.e ** (3 * D) * l0 * mp.e ** (l0 / 2) / (A0 * (1 - mp.e ** -l0))
            * (1 + 2 * t / (l0 - t)) * mp.e ** (-l0 ** 2 / (4 * t)) / mp.sqrt(4 * mp.pi * t))


tmax = l0 ** 2 / (2 * (1 + l0))


def delta1(t3, q, eta=0):
    ts = [mp.mpf(t3) * mp.mpf(q) ** (2 - k) for k in range(3)]
    assert max(ts) <= tmax
    W, nv = vinv_norm(ts)
    return nv * max(tk * (eta + Bhyp(tk) + F(Qn(3, 12)) * tk ** 2) for tk in ts), nv * max(ts)


d_a, amp_a = delta1(mp.mpf("1e-11"), 0.5)
d_b, _ = delta1(mp.mpf("1e-10"), 0.5)
dthm = mp.mpf("3.80e-7")
assert d_a < dthm < d_b
assert delta1(mp.mpf("7.8e-11"), 0.5)[0] < dthm < delta1(mp.mpf("7.9e-11"), 0.5)[0]   # threshold t_3 = 7.8e-11
eta_max = (dthm - d_a) / amp_a
assert mp.mpf("1e-19") < eta_max < mp.mpf("3e-19")
for e in (-13, -12, -11, -10, -6, -3):
    d, _ = delta1(mp.mpf(10) ** e, 0.5)
    assert abs(d / mp.mpf(10) ** e / 4860 - 1) < 0.01      # delta_1 = 4.86e3 t_3 for eta = 0
say(f"2. remark: times t_3, t_3/2, t_3/4: delta_1 = {mp.nstr(d_a / mp.mpf('1e-11'), 4)} t_3 + {mp.nstr(amp_a * mp.mpf('1e-22'), 3)}*1e22 eta at t_3 = 1e-11;")
say(f"   delta_1 <= delta_thm(2,8,8) = 3.80e-7 needs t_3 <= 7.8e-11, and at t_3 = 1e-11 eta <= {mp.nstr(eta_max, 3)}")

# ---------------------------------------------------------------- 3. least area among collisions
SMAX = 600
coll_R = []
for S in range(9, SMAX + 1):
    byR = {}
    for p in range(2, S // 3 + 1):
        for q_ in range(p, (S - p) // 2 + 1):
            r = S - p - q_
            R = Fr(1, p) + Fr(1, q_) + Fr(1, r)
            if R < 1:
                byR.setdefault(R, []).append((p, q_, r))
    for R, trs in byR.items():
        if len(trs) > 1:
            coll_R.append((R, S, tuple(trs)))
    if S >= 9:
        st3 = [Fr(1, p) + Fr(1, q_) + Fr(1, S - p - q_) for p in range(3, S // 3 + 1) for q_ in range(p, (S - p) // 2 + 1)]
        if S >= 9 and st3:
            assert max(st3) == Fr(2, 3) + Fr(1, S - 6), S
        st2 = [Fr(1, 2) + Fr(1, q_) + Fr(1, S - 2 - q_) for q_ in range(2, (S - 2) // 2 + 1)]
        assert len(set(st2)) == len(st2), S
coll_R.sort(reverse=True)
assert coll_R[0][0] == Fr(3, 4) and coll_R[0][2] == ((2, 8, 8), (3, 3, 12)), coll_R[0]
assert coll_R[1][0] < Fr(3, 4)
say(f"3. collisions with S <= {SMAX}: largest R = {coll_R[0][0]} only at {coll_R[0][2]}; next {coll_R[1][0]} at {coll_R[1][2]}")
assert all(Fr(2, 3) + Fr(1, S - 6) <= Fr(3, 4) for S in range(18, 10 ** 4)) and Fr(2, 3) + Fr(1, 12) == Fr(3, 4)

# ---------------------------------------------------------------- 4. wave-trace kernel
mp.mp.dps = 30
for a in (mp.mpf("0.3"), mp.pi - 2 * mp.pi / 8, mp.pi - 2 * mp.pi / 3):
    for u in (mp.mpf(0), mp.mpf("0.7"), mp.mpf("2.5")):
        lhs = mp.quad(lambda r: mp.cos(r * u) * mp.cosh(a * r) / mp.cosh(mp.pi * r), [-mp.inf, 0, mp.inf])
        rhs = 2 * mp.cos(a / 2) * mp.cosh(u / 2) / (mp.cos(a) + mp.cosh(u))
        assert abs(lhs - rhs) < mp.mpf(10) ** -15, (a, u, lhs, rhs)
for m in (3, 8, 12):
    th = mp.pi / m
    a = mp.pi - 2 * th
    # denominator cos a + cosh u vanishes at u = 2 i th, numerator 2 cos(a/2) cosh(th i) = 2 sin(th) cos(th) != 0
    assert abs(mp.cos(a) + mp.cosh(2j * th)) < mp.mpf(10) ** -25
    assert abs(2 * mp.cos(a / 2) * mp.cosh(1j * th)) > mp.mpf("0.1")
    # no zero of the denominator with |Im u| < 2 th: cosh(iy) = cos y > -cos a = cos(2 th) for |y| < 2 th
    for y in [2 * th * k / 50 for k in range(50)]:
        assert mp.cos(y) + mp.cos(a) > 0
say("4. wave-trace kernel: Fourier formula verified; nearest singularities at u = +-2 pi i/m (m = 3, 8, 12)")
# E_m(t) = int g_t(u) k_m(u) du with k_m(u) = (1/2m) sum_j cosh(u/2)/(cosh u - cos(2 pi j/m)),
# g_t(u) = e^{-t/4} e^{-u^2/4t}/sqrt(4 pi t) (the normalisation of Theorem 2.3)
for m in (3, 8, 12):
    for tt in (mp.mpf("0.01"), mp.mpf("0.05"), mp.mpf("0.3")):
        km = lambda u: sum(mp.cosh(u / 2) / (mp.cosh(u) - mp.cos(2 * mp.pi * j / m)) for j in range(1, m)) / (2 * m)
        gt = lambda u: mp.e ** (-tt / 4) * mp.e ** (-u ** 2 / (4 * tt)) / mp.sqrt(4 * mp.pi * tt)
        lhs = mp.quad(lambda u: gt(u) * km(u), [-mp.inf, 0, mp.inf])
        rhs = elliptic_term(m, tt, 30)
        assert abs(lhs - rhs) < mp.mpf(10) ** -18 * max(1, abs(rhs)), (m, tt, lhs, rhs)
say("4. E_m(t) = int g_t(u) k_m(u) du verified for m = 3, 8, 12 and t = 0.01, 0.05, 0.3")

# ---------------------------------------------------------------- 5. flat-cone image sums
m, t = 12, mp.mpf("0.02")
rho = mp.sqrt(t) / mp.sin(mp.pi / m)
vals = {}
for r in (mp.mpf("0.14"), rho, 2 * rho, 3 * rho, 4 * rho):
    vals[float(r)] = sum(mp.e ** (-(2 * r * mp.sin(mp.pi * j / m)) ** 2 / (4 * t)) for j in range(m))
    say(f"5. m=12, t=0.02, r={mp.nstr(r, 3)} (= {mp.nstr(r / rho, 3)} sqrt(t)/sin(pi/m)): 4 pi t h = {mp.nstr(vals[float(r)], 4)}")
assert vals[float(rho)] > 1.5 and vals[float(3 * rho)] < 1.01 and vals[float(2 * rho)] > 1.01

# ---------------------------------------------------------------- 6. Uçar's normalisation (Remark 2.9)
from math import comb, factorial  # noqa: E402
from eigen_common import phi, bernoulli  # noqa: E402


def c_lune(l, k):
    """U\u00e7ar's c^S_l(pi/k), [13, (4.25)]."""
    bh = lambda n: (Fr(2) ** (1 - n) - 1) * bernoulli(n)
    s = sum(comb(2 * l + 2, 2 * j) * (k ** (2 * j) - 1) * bernoulli(2 * j) * bh(2 * l + 2 - 2 * j) for j in range(l + 2))
    return Fr((-1) ** l, 4 * k * factorial(l + 1) * (2 * l + 1)) * s


for m in (2, 3, 5, 7, 12):
    for k in range(0, 8):
        assert m * factorial(2 * k) * phi(k, m) == 2 * 4 ** k * factorial(k) * m * c_lune(k, m), (m, k)
say("6. m Phi_m^(2k)(0) = 2 4^k k! m c^S_k(pi/m) exactly, m in {2,3,5,7,12}, k <= 7")

# ---------------------------------------------------------------- 7. Theorem B with its signs
import random  # noqa: E402
import sympy as sp  # noqa: E402

random.seed(6)
z = sp.symbols("z")
for n in range(2, 6):
    for trial in range(3):
        m = [sp.Rational(random.randint(1, 40), random.randint(1, 6)) for _ in range(n)]
        e = [sp.Integer(1)] + [sum(sp.prod(c) for c in itertools.combinations(m, k)) for k in range(1, n + 1)]
        # Hurwitz matrix (a_{2j-i}) of chi_m(z) = prod (z + m_i), a_0 = 1
        a = lambda k: e[k] if 0 <= k <= n else 0
        H = sp.Matrix(n, n, lambda i, j: a(2 * (j + 1) - (i + 1)))
        prod_plus = sp.prod([m[i] + m[j] for i in range(n) for j in range(i + 1, n)])
        assert H[:n - 1, :n - 1].det() == prod_plus
        # the system (12): e_{2j+1} - sum_i T_{2i+1} e_{2j-2i} = 0 (j <= n-2), e_{n-1} - R e_n = 0, unknowns e_1..e_n
        P = {k: sum(x ** k for x in m) for k in range(1, 2 * n)}
        U = sum(P[k] * z ** k / k for k in range(1, 2 * n, 2))
        T = sp.series(sp.tanh(U), z, 0, 2 * n).removeO()
        Tc = [T.coeff(z, k) for k in range(2 * n)]
        R = sum(1 / x for x in m)
        M = sp.zeros(n, n)
        for j in range(n - 1):
            if 2 * j + 1 <= n:
                M[j, 2 * j] = 1                              # coefficient of e_{2j+1} (column index 2j)
            for i in range(j + 1):
                k = 2 * j - 2 * i
                if 1 <= k <= n:
                    M[j, k - 1] -= Tc[2 * i + 1]
        M[n - 1, n - 2] += 1
        M[n - 1, n - 1] -= R
        sign = (-1) ** (n * (n + 1) // 2)
        assert sp.simplify(M.det() - sign * prod_plus / e[n]) == 0, (n, m)
say("7. Theorem B: Hur_{n-1}(chi_m) = prod(m_i+m_j) for the Hurwitz matrix (a_{2j-i}), and det M = (-1)^{n(n+1)/2} prod(m_i+m_j)/e_n, n = 2..5")

open(os.path.join(HERE, "check_heat_supporting.txt"), "w").write("\n".join(out) + "\n")
print("ALL CHECKS PASSED")
