"""TF.6 (Agreement with Ucar), exact.

Ucar arXiv:1711.03405, as fetched (sources/ucar_1711.03405.txt, printed p. 134, eq. (4.25)):
  c^S_l(pi/k) = 1/(4k) * (-1)^l/(l+1)! * 1/(2l+1) * sum_{j=0}^{l+1} C(2l+2,2j)(k^{2j}-1) B_{2j} B_{2l+2-2j}(1/2)
printed p. 137, (4.33): C = sum_nu sum_{l<=nu} 2/(4^l l!) c^S_{nu-l}(pi/k) kappa^nu t^nu
printed p. 137, (4.35): a_nu(O) = vol(O)/(nu! 4^nu) sum_l C(nu,l)(-4)^l B_{2l}(1/2) kappa^nu,
  with Z ~ (1/4 pi t) sum a_nu t^nu.
Checks, all exact, as POLYNOMIAL identities in M = m^2 (hence for every m):
 (a) 2 c^S_k(pi/m) = (2k)!/(k! 4^k) phi_k(m)                         k <= 40
 (b) p_l(m)/m = sum_{i<=l} 2 (4^i i!)^{-1} c^S_{l-i}(pi/m)             l <= 40
 (c) Ucar's t^l cone coefficient at kappa=-1 equals b_l(m) = (-1)^l p_l(m)/m, l <= 40
     (so p_l/m is (-1)^l times Ucar's coefficient, as the remark says)
 (d) Ucar (4.35)/(4 pi) at kappa = -1 equals alpha_nu * Area/(4 pi),     nu <= 40
 (e) m t^2 Phi_m(i t/2) = t^2/(4 sinh(t/2)) * (m coth(m t/2) - coth(t/2)) as power series
     in t through t^82, m = 1..12 (exact series arithmetic, no Bernoulli numbers).
"""
import sys
from fractions import Fraction as Fr
from math import factorial, comb
from tf_lib import (sigmas, mphi_poly, p_poly, ucar_mcS_poly, alpha_printed, bern_half,
                    phi_direct, ser_mul, ser_inv, ser_shift)

L = 40
sig = sigmas(L + 3)


def padd(a, b):
    n = max(len(a), len(b))
    a = a + [Fr(0)] * (n - len(a))
    b = b + [Fr(0)] * (n - len(b))
    return [x + y for x, y in zip(a, b)]


def pscale(a, c):
    return [c * x for x in a]


def ptrim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


# (a)
for k in range(L + 1):
    lhs = pscale(ucar_mcS_poly(k), Fr(2))
    rhs = pscale(mphi_poly(k, sig), Fr(factorial(2 * k), factorial(k) * 4 ** k))
    assert ptrim(lhs) == ptrim(rhs), k
print(f"(a) 2 c^S_k(pi/m) = (2k)!/(k!4^k) phi_k(m) as polynomials, k<={L}: OK")

# (b), (c)
for l in range(L + 1):
    acc = []
    for i in range(l + 1):
        acc = padd(acc, pscale(ucar_mcS_poly(l - i), Fr(2, 4 ** i * factorial(i))))
    assert ptrim(acc) == ptrim(p_poly(l, sig)), l
    # Ucar's coefficient of t^l at kappa=-1 is (-1)^l * acc/m ; b_l = (-1)^l p_l/m
    ucar_coef_times_m = pscale(acc, Fr((-1) ** l))
    b_l_times_m = pscale(p_poly(l, sig), Fr((-1) ** l))
    assert ptrim(ucar_coef_times_m) == ptrim(b_l_times_m)
print(f"(b) p_l/m = sum_i 2(4^i i!)^-1 c^S_(l-i)(pi/m), l<={L}: OK")
print(f"(c) Ucar (4.33) at kappa=-1 = b_l(m) = (-1)^l p_l(m)/m, l<={L}: OK")

# (d)
for nu in range(L + 1):
    ucar = Fr(1, factorial(nu) * 4 ** nu) * sum((comb(nu, l) * Fr(-4) ** l * bern_half(2 * l)
                                                 for l in range(nu + 1)), Fr(0)) * Fr(-1) ** nu
    assert ucar == alpha_printed(nu), nu
print(f"(d) Ucar (4.35) at kappa=-1 equals alpha_nu, nu<={L}: OK")

# (e) series in t, exact
N = 2 * L + 6


def sinh_s(a):
    a = Fr(a)
    return [a ** n / factorial(n) if n % 2 == 1 else Fr(0) for n in range(N + 4)]


def cosh_s(a):
    a = Fr(a)
    return [a ** n / factorial(n) if n % 2 == 0 else Fr(0) for n in range(N + 4)]


for m in range(1, 13):
    # F(t) = t^2/(4 sinh(t/2)) * (m coth(mt/2) - coth(t/2))
    #      = t^2 [m cosh(mt/2) sinh(t/2) - cosh(t/2) sinh(mt/2)] / (4 sinh(t/2)^2 sinh(mt/2))
    M = N + 4
    num = [m * x - y for x, y in zip(ser_mul(cosh_s(Fr(m, 2)), sinh_s(Fr(1, 2)), M),
                                     ser_mul(cosh_s(Fr(1, 2)), sinh_s(Fr(m, 2)), M))]
    den = [4 * x for x in ser_mul(ser_mul(sinh_s(Fr(1, 2)), sinh_s(Fr(1, 2)), M), sinh_s(Fr(m, 2)), M)]
    if m == 1:
        assert all(x == 0 for x in num)
        F = [Fr(0)] * N
    else:
        num, den = ser_shift(num, 3), ser_shift(den, 3)
        K = min(len(num), len(den))
        F = [Fr(0), Fr(0)] + ser_mul(num, ser_inv(den[:K], K), K)   # times t^2
    ph = phi_direct(m, L)
    G = [Fr(0)] * N
    for k in range(L + 1):
        if 2 * k + 2 < N:
            G[2 * k + 2] = m * ph[k] * Fr(-1) ** k / 4 ** k
    assert F[:2 * L + 3] == G[:2 * L + 3], m
print("(e) m t^2 Phi_m(it/2) = t^2/(4 sinh(t/2)) (m coth(mt/2) - coth(t/2)) through t^82, m<=12: OK")
print("ALL CHECKS PASSED")
sys.exit(0)
