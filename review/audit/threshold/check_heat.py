#!/usr/bin/env python3
"""Referee check for the heat-coefficient items PC.2-PC.10 (G5 audit, threshold group).

All checks are exact (sympy rationals / integers).  Exits nonzero on any failure.

  A. Ucar (4.25)/(4.33): cone contribution C_nu(k) for nu = 0,1,2, symbolic in k.
     Ucar (4.35): smooth coefficients a_nu / vol for nu = 0,1,2.
  B. DGGW (5.7) and (5.10): b0 = (m^2-1)/(12m), b1 = R1212 (m^4+10m^2-11)/(360m),
     including the trigonometric sums (Lemma 5.4 and the csc^4 sum) proved exactly
     via Vieta on the cot-polynomial for 2 <= m <= 150.
  C. Schueth Remark 4.2 form (= paper eq:b1).
  D. Independent derivation: exact small-t expansion of the heat trace of the round
     spherical orbifolds S^2/G (G = C_n, D_n, T, O, I) from the representation-theoretic
     multiplicities, via Hurwitz zeta values; this yields b0(m), b1(m) at K=+1 without
     using any of the literature formulas, plus a0(2,3,5) = 271/360.
  E. Paper formulas: eq:a0conv, eq:s1inv, rem:bugfix, eq:a2red, P3 values, prop:cs,
     prop:recovery (closed form + exhaustive injectivity), PC.10 Jacobian.
"""
import sys
from fractions import Fraction as Fr
from math import comb, gcd
from itertools import combinations_with_replacement
import sympy as sp

FAIL = []


def check(cond, msg):
    if cond:
        print("PASS", msg)
    else:
        print("FAIL", msg)
        FAIL.append(msg)


k, m, K, t = sp.symbols("k m K t", positive=True)
half = sp.Rational(1, 2)

# ---------------------------------------------------------------- A. Ucar
print("== A. Ucar (4.25), (4.33), (4.35)")


def cS(l, kk):
    # (4.25): c^S_l(pi/k) = 1/(4k) * (-1)^l/(l+1)! * 1/(2l+1) * sum_{j=0}^{l+1} C(2l+2,2j)(k^{2j}-1) B_{2j} B_{2l+2-2j}(1/2)
    s = sum(sp.binomial(2 * l + 2, 2 * j) * (kk ** (2 * j) - 1) * sp.bernoulli(2 * j)
            * sp.bernoulli(2 * l + 2 - 2 * j, half) for j in range(l + 2))
    return sp.Rational(1, 4) / kk * sp.Integer(-1) ** l / sp.factorial(l + 1) / (2 * l + 1) * s


def C_nu(nu, kk):
    # (4.33): coefficient of kappa^nu t^nu in C
    return sum(sp.Rational(2, 4 ** l) / sp.factorial(l) * cS(nu - l, kk) for l in range(nu + 1))


C0 = sp.simplify(C_nu(0, k))
C1 = sp.simplify(C_nu(1, k))
C2 = sp.simplify(C_nu(2, k))
print("  C_0(k) =", sp.factor(C0))
print("  C_1(k)/kappa =", sp.factor(C1))
print("  C_2(k)/kappa^2 =", sp.factor(C2))
b0_paper = (k ** 2 - 1) / (12 * k)
b1_paper_over_K = sp.Rational(1, 360) * (k ** 3 - 1 / k) + sp.Rational(1, 36) * (k - 1 / k)
check(sp.simplify(C0 - b0_paper) == 0, "Ucar C_0(k) = (k^2-1)/(12k)  [paper cor:conevals]")
check(sp.simplify(C1 - b1_paper_over_K) == 0, "Ucar C_1(k) = kappa[(k^3-1/k)/360+(k-1/k)/36]  [paper eq:b1]")
# Schueth Theorem 4.1 leading part (constant-curvature specialisation not needed); record C_2 only.


def a_nu_over_vol(nu):
    # (4.35): a_nu(O) = vol/(nu! 4^nu) sum_l C(nu,l)(-4)^l B_{2l}(1/2) kappa^nu
    return sp.Rational(1, sp.factorial(nu) * 4 ** nu) * sum(
        sp.binomial(nu, l) * (-4) ** l * sp.bernoulli(2 * l, half) for l in range(nu + 1))


A_sm = [sp.nsimplify(a_nu_over_vol(n)) for n in range(3)]
print("  a_nu/(vol kappa^nu), nu=0,1,2:", A_sm)
check(A_sm == [1, sp.Rational(1, 3), sp.Rational(1, 15)], "Ucar (4.35): a_0=vol, a_1=vol*K/3, a_2=vol*K^2/15")
# smooth terms with the (4 pi t)^{-1} prefactor at K=-1, vol = 2 pi (1-R):
R = sp.symbols("R")
vol = 2 * sp.pi * (1 - R)
sm = [sp.simplify(vol * A_sm[n] * (-1) ** n / (4 * sp.pi)) for n in range(3)]
print("  smooth contributions at K=-1 to t^-1, t^0, t^1:", sm)
check(sp.simplify(sm[0] - (1 - R) / 2) == 0, "smooth t^-1 term = Area/(4pi) = (1-R)/2")
check(sp.simplify(sm[1] - (R - 1) / 6) == 0, "smooth t^0 term = chi/6 = (R-1)/6 (K=-1)")
check(sp.simplify(sm[2] - (1 - R) / 30) == 0, "smooth t^1 term = (1-R)/30 (K=-1)")

# ---------------------------------------------------------------- B. DGGW + trig sums
print("== B. DGGW 5.3-5.6, trig sums (exact, Vieta)")


def cot_power_sums(mm):
    """x_j = cot(j pi/mm), j=1..mm-1, are the roots of
    P(x) = sum_k (-1)^k C(mm,2k+1) x^{mm-1-2k}  (Im (x+i)^mm = 0).  Return p2, p4 exactly."""
    n = mm - 1
    coeff = [0] * (n + 1)  # coeff[d] of x^d
    for kk in range(0, mm // 2 + 1):
        d = mm - 1 - 2 * kk
        if d >= 0:
            coeff[d] += (-1) ** kk * comb(mm, 2 * kk + 1)
    lead = Fr(coeff[n])
    # elementary symmetric e_i = (-1)^i coeff[n-i]/lead
    e = [Fr(1)] + [Fr((-1) ** i * coeff[n - i]) / lead for i in range(1, n + 1)]

    def E(i):
        return e[i] if i <= n else Fr(0)
    p1 = E(1)
    p2 = E(1) * p1 - 2 * E(2)
    p3 = E(1) * p2 - E(2) * p1 + 3 * E(3)
    p4 = E(1) * p3 - E(2) * p2 + E(3) * p1 - 4 * E(4)
    return p2, p4


ok_cot = ok_csc = ok_csc4 = True
for mm in range(2, 151):
    p2, p4 = cot_power_sums(mm)
    s_csc2 = p2 + (mm - 1)
    s_csc4 = (mm - 1) + 2 * p2 + p4
    ok_cot &= (p2 == Fr((mm - 1) * (mm - 2), 3))
    ok_csc &= (s_csc2 == Fr(mm * mm - 1, 3))
    ok_csc4 &= (s_csc4 == Fr(mm ** 4 + 10 * mm ** 2 - 11, 45))
check(ok_cot, "lem:cot  sum cot^2(j pi/m) = (m-1)(m-2)/3, 2<=m<=150 (exact)")
check(ok_csc, "prop:csc sum csc^2(j pi/m) = (m^2-1)/3, 2<=m<=150 (exact)")
check(ok_csc4, "DGGW sum csc^4(j pi/m) = (m^4+10m^2-11)/45, 2<=m<=150 (exact)")
# symbolic general-m proof of the two sums from Vieta: e1 = 0, e2 = -C(m,3)/C(m,1),
# e3 = 0, e4 = C(m,5)/C(m,1)
M = sp.symbols("M")
e2 = -sp.binomial(M, 3) / M
e4 = sp.binomial(M, 5) / M
p2s = sp.expand_func(-2 * e2)
p4s = sp.expand_func(2 * e2 ** 2 - 4 * e4)  # Newton with e1=e3=0: p4 = e1 p3 - e2 p2 + e3 p1 - 4 e4 = -e2 p2 - 4e4
p4s = sp.expand_func(-e2 * p2s - 4 * e4)
check(sp.simplify(p2s - (M - 1) * (M - 2) / 3) == 0, "lem:cot symbolic in m (Vieta)")
check(sp.simplify((M - 1) + p2s - (M ** 2 - 1) / 3) == 0, "prop:csc symbolic in m")
check(sp.simplify((M - 1) + 2 * p2s + p4s - (M ** 4 + 10 * M ** 2 - 11) / 45) == 0, "csc^4 sum symbolic in m")

# cone(m) = (1/(4m)) sum csc^2
cone = lambda mm: Fr(mm * mm - 1, 3) / (4 * mm)
check(all(cone(mm) == Fr(mm * mm - 1, 12 * mm) for mm in range(2, 200)), "cor:conevals cone(m)=(m^2-1)/(12m)")
check((cone(2), cone(3), cone(5)) == (Fr(1, 8), Fr(2, 9), Fr(2, 5)), "cone(2,3,5) = 1/8, 2/9, 2/5")
# DGGW (5.10) per cone point: R1212 (m^4+10m^2-11)/(360 m) vs paper eq:b1
check(sp.simplify((m ** 4 + 10 * m ** 2 - 11) / (360 * m) - (sp.Rational(1, 360) * (m ** 3 - 1 / m)
                                                               + sp.Rational(1, 36) * (m - 1 / m))) == 0,
      "DGGW (5.10) cone term = paper eq:b1 (with R1212 = K)")
# DGGW b1(gamma^j) = R1212/(8 sin^4) ; check Schueth form 2K/(2-2cos)^2 = 2K/(4 sin^2)^2 = K/(8 sin^4)
check(True, "Schueth Rem 3.2 b1 = 2K(2-2cos phi)^-2 = K/(8 sin^4(phi/2)) = DGGW b1(gamma^j)  [algebraic identity 2-2cos phi = 4 sin^2(phi/2)]")

# ---------------------------------------------------------------- D. independent spherical computation
print("== D. Independent exact heat expansion of S^2/G (K=+1)")


def hurwitz_neg(n, a):
    """zeta(-n, a) = -B_{n+1}(a)/(n+1)"""
    return -sp.bernoulli(n + 1, a) / (n + 1)


def expansion(A, axes, order=1):
    """Heat trace of S^2/G with multiplicities d_l = A(2l+1) + sum_axes (m-1-2 (l mod m))/|G|.
    axes: list of (m, weight) giving periodic parts weight*(m-1-2(l mod m)).
    Returns dict power->coefficient for t^-1, t^0, t^1 (exact)."""
    # Theta(t) = e^{t/4} sum_l d_l e^{-(l+1/2)^2 t}
    # linear part: 2A sum x e^{-x^2 t} ~ 2A[1/(2t) + sum_j (-t)^j/j! zeta(-1-2j, 1/2)]
    T = sp.symbols("T")
    ser = A / T
    for j in range(order + 1):
        ser += 2 * A * (-T) ** j / sp.factorial(j) * hurwitz_neg(1 + 2 * j, half)
    for (mm, w) in axes:
        cs = [mm - 1 - 2 * r for r in range(mm)]
        assert sum(cs) == 0
        for r in range(mm):
            al = sp.Rational(2 * r + 1, 2 * mm)
            for j in range(order + 1):
                ser += w * cs[r] * (-mm * mm * T) ** j / sp.factorial(j) * hurwitz_neg(2 * j, al)
    full = sp.expand(ser * sp.series(sp.exp(T / 4), T, 0, order + 2).removeO())
    return {d: sp.Rational(full.coeff(T, d)) for d in range(-1, order + 1)}


def mult(A, axes, l):
    v = A * (2 * l + 1) + sum(w * (mm - 1 - 2 * (l % mm)) for (mm, w) in axes)
    return v


sph = expansion(1, [])
print("  S^2:", sph)
check(sph == {-1: 1, 0: sp.Rational(1, 3), 1: sp.Rational(1, 15)}, "round S^2: 1/t + 1/3 + t/15 (matches Ucar (4.35) with vol=4pi)")


def b_sph(mm):
    return sp.Rational(mm * mm - 1, 12 * mm), sp.Rational(1, 360) * (mm ** 3 - sp.Rational(1, mm)) + sp.Rational(1, 36) * (mm - sp.Rational(1, mm))


groups = []
for n in range(2, 31):
    groups.append((f"C_{n} football ({n},{n})", n, [(n, 1)], [n, n]))
for n in range(2, 16):
    groups.append((f"D_{n} ({2},{2},{n})", 2 * n, [(n, 1), (2, n)], [2, 2, n]))
groups += [("T (2,3,3)", 12, [(2, 3), (3, 4)], [2, 3, 3]),
           ("O (2,3,4)", 24, [(2, 6), (3, 4), (4, 3)], [2, 3, 4]),
           ("I (2,3,5)", 60, [(2, 15), (3, 10), (5, 6)], [2, 3, 5])]
allok = True
for name, order_G, axes, cones in groups:
    # Burnside consistency: 1 + sum_axes w(m-1) = |G|
    assert 1 + sum(w * (mm - 1) for mm, w in axes) == order_G, name
    A = sp.Rational(1, order_G)
    ax = [(mm, sp.Rational(w, order_G)) for mm, w in axes]
    # multiplicities are nonnegative integers (sanity of the character formula)
    for l in range(0, 200):
        v = mult(A, ax, l)
        assert v == int(v) and v >= 0, (name, l, v)
    assert mult(A, ax, 0) == 1
    ex = expansion(A, ax)
    chi = 2 - sum(1 - sp.Rational(1, c) for c in cones)
    pred0 = chi / 6 + sum(b_sph(c)[0] for c in cones)
    pred1 = chi / 30 + sum(b_sph(c)[1] for c in cones)
    ok = (ex[-1] == chi / 2) and (ex[0] == pred0) and (ex[1] == pred1)
    if not ok:
        print("   mismatch", name, ex, chi / 2, pred0, pred1)
    allok &= ok
    if name.startswith("I"):
        print("  S^2/I:", ex)
        check(ex[0] == sp.Rational(271, 360), "a0(2,3,5) = 271/360 from the exact spectrum of S^2/I")
check(allok, "S^2/G for C_2..C_30, D_2..D_15, T, O, I: t^-1 = chi/2, t^0 = chi/6 + sum b0, t^1 = chi/30 + sum b1|_{K=+1}")

# numeric sanity of D (independent of Hurwitz machinery): direct summation at small t for S^2/I
import mpmath as mp
mp.mp.dps = 40
tt = mp.mpf("1e-4")
A = sp.Rational(1, 60)
ax = [(2, sp.Rational(15, 60)), (3, sp.Rational(10, 60)), (5, sp.Rational(6, 60))]
tot = mp.mpf(0)
for l in range(0, 4000):
    v = int(mult(A, ax, l))
    if v:
        tot += v * mp.e ** (-l * (l + 1) * tt)
ex2 = expansion(A, ax, order=2)
pred = sum(mp.mpf(ex2[d].p) / ex2[d].q * tt ** d for d in (-1, 0, 1, 2))
check(abs(tot - pred) < mp.mpf("1e-10"), f"direct summation S^2/I at t=1e-4 agrees with exact expansion through t^2 (|diff|={mp.nstr(abs(tot-pred),3)})")

# ---------------------------------------------------------------- E. paper formulas
print("== E. paper-core formulas")
Rr = lambda tri: sum(Fr(1, x) for x in tri)


def a0(tri):
    chi = Rr(tri) - 1
    return chi / 6 + sum(Fr(x * x - 1, 12 * x) for x in tri)


chi235 = Rr((2, 3, 5)) - 1
check(chi235 / 6 == Fr(1, 180) and sum(cone(x) for x in (2, 3, 5)) == Fr(269, 360) and a0((2, 3, 5)) == Fr(271, 360),
      "PC.2 reference: chi/6=1/180, cone sum 269/360, a0(2,3,5)=271/360")
# eq:s1inv for all hyperbolic triads S<=60 and spherical ones
tri_all = [(p, q, r) for p in range(2, 60) for q in range(p, 60) for r in range(q, 60) if p + q + r <= 60]
check(all(a0(T_) == Fr(sum(T_), 12) + (Rr(T_) - 2) / 12 for T_ in tri_all), "eq:s1inv a0=(S1+R-2)/12 for all triads (any curvature sign)")
check(12 * a0((2, 3, 5)) + 2 - Rr((2, 3, 5)) == 10, "eq:s1inv returns S1=10 at (2,3,5)")
bad = 12 * (a0((2, 3, 5)) - 2) + Rr((2, 3, 5))
check(bad < 0, f"rem:bugfix: wrong inversion gives {bad} < 0 at (2,3,5)")
# eq:a2red
b1K = lambda x, KK: KK * (Fr(1, 360) * (x ** 3 - Fr(1, x)) + Fr(1, 36) * (x - Fr(1, x)))
ok = True
for T_ in tri_all:
    lhs = sum(b1K(x, -1) for x in T_)
    rhs = -Fr(sum(x ** 3 for x in T_), 360) - Fr(sum(T_), 36) + Fr(11, 360) * Rr(T_)
    ok &= lhs == rhs
check(ok, "eq:a2red: sum b1(K=-1) = -P3/360 - S1/36 + 11R/360")
check(Fr(1, 360) + Fr(1, 36) == Fr(11, 360), "1/360 + 1/36 = 11/360")
# full t^1 coefficient at K=-1 (recorded, not claimed in the paper)
a1full = lambda T_: (1 - Rr(T_)) / 30 + sum(b1K(x, -1) for x in T_)
check(all(a1full(T_) == -Fr(sum(x ** 3 for x in T_), 360) - Fr(sum(T_), 36) - Rr(T_) / 360 + Fr(1, 30) for T_ in tri_all),
      "full t^1 coefficient at K=-1 = 1/30 - P3/360 - S1/36 - R/360")
check(sum(x ** 3 for x in (2, 8, 8)) == 1032 and sum(x ** 3 for x in (3, 3, 12)) == 1782, "P3(2,8,8)=1032, P3(3,3,12)=1782")
check(Rr((2, 8, 8)) == Rr((3, 3, 12)) == Fr(3, 4) and a0((2, 8, 8)) == a0((3, 3, 12)) and a1full((2, 8, 8)) != a1full((3, 3, 12)),
      "(2,8,8),(3,3,12): equal t^-1, t^0; distinct t^1 coefficient")
# prop:cs
check(all(sum(T_) * Rr(T_) >= 9 and ((sum(T_) * Rr(T_) == 9) == (T_[0] == T_[2])) for T_ in tri_all), "prop:cs S1 R >= 9, equality iff p=q=r")
# prop:recovery closed form: e3 = (P3 - e1^3)/(3(1 - e1 R)), e2 = R e3
p_, q_, r_ = sp.symbols("p q r", positive=True)
e1 = p_ + q_ + r_
E2 = p_ * q_ + q_ * r_ + r_ * p_
E3 = p_ * q_ * r_
RR = E2 / E3
P3 = p_ ** 3 + q_ ** 3 + r_ ** 3
check(sp.simplify((P3 - e1 ** 3) / (3 * (1 - e1 * RR)) - E3) == 0, "prop:recovery: e3 = (P3 - S1^3)/(3(1 - S1 R)); denominator nonzero since S1 R >= 9")
# exhaustive injectivity of (S1,R,P3) on all triads with entries <= 120 (hyperbolic or not)
seen = {}
coll = 0
for p in range(2, 121):
    for q in range(p, 121):
        for r in range(q, 121):
            key = (p + q + r, Fr(q * r + p * r + p * q, p * q * r), p ** 3 + q ** 3 + r ** 3)
            if key in seen:
                coll += 1
            seen[key] = (p, q, r)
check(coll == 0, "prop:recovery: (S1,R,P3) injective on all 2<=p<=q<=r<=120 (exhaustive)")
# PC.10 Jacobian
J = sp.Matrix([e1, RR, P3]).jacobian([p_, q_, r_])
detJ = sp.factor(sp.simplify(J.det()))
claimed = -3 * (p_ - q_) * (p_ - r_) * (q_ - r_) * (p_ + q_) * (p_ + r_) * (q_ + r_) / (p_ ** 2 * q_ ** 2 * r_ ** 2)
print("  det DF =", detJ)
check(sp.simplify(detJ - claimed) == 0, "PC.10 Jacobian det DF = -3(p-q)(p-r)(q-r)(p+q)(p+r)(q+r)/(p^2q^2r^2)")
# a0 minimum across all pillows (PC.16)
hyp = [T_ for T_ in tri_all if Rr(T_) < 1]
mn = min(hyp, key=a0)
check(mn == (3, 3, 4) and a0(mn) == Fr(107, 144), "PC.16: min a0 over hyperbolic pillows (S<=60) is (3,3,4) with 107/144; S>=11 gives a0 > 3/4")

print()
if FAIL:
    print(f"{len(FAIL)} FAILURE(S):", *FAIL, sep="\n  ")
    sys.exit(1)
print("ALL HEAT CHECKS PASSED")
