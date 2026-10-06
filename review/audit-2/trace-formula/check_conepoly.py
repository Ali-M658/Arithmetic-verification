"""TF.4 (heat expansion constants) and TF.5 (Lemma 2.5 + printed values), exact.

Certificates (exact, Fraction / sympy Rational):
 1. p_l from (bl) with phi_k from the DEFINING SUM (Newton power sums), m = 1..30,
    equals the polynomial built from (phik); l <= 40.
 2. Lemma 2.5 for l <= 40: even polynomial (built in M=m^2), rational coefficients,
    degree exactly 2l+2, p_l(1) = 0, leading coefficient |B_{2l+2}|/(2 (l+1)! (2l+1)),
    p_l = sum_n w_n (m^{2n}-1) with every w_n > 0 (computed from the double sum, not
    from the monomials), and p_l(1+x) has all coefficients > 0 except the zero constant
    (so p_l > 0 on (1, oo), in particular on (1,2)).
 3. alpha_k: (alphak) equals the coefficients obtained from the identity term,
    e^{-t/4}(1 - 4t sum_k (-t)^k M_k / k!), with the Fermi moments
    M_k = int_0^oo r^{2k+1}/(e^{2 pi r}+1) dr computed as (1-2^{-2k-1}) (2k+1)! zeta(2k+2)/(2pi)^{2k+2}
    by sympy (exact zeta at even integers); also equal to the printed moment formula
    (1-2^{-2k-1})(-1)^k B_{2k+2}/(4(k+1)); k <= 40.
 4. printed values alpha_0..alpha_4 and p_0, p_1, p_2.
 5. c_j indexing: c_2 and c_3 reproduce DGGW (5.7) and (5.10) with R1212 = K = -1;
    b_0, b_1, b_2 reproduce Schueth Rem. 4.2 and Thm 4.1 at K = -1;
    Sum 1/sin^2 and Sum 1/sin^4 identities quoted by DGGW checked exactly for m <= 30.
Sanity only (mpmath, 40 digits, NOT a certificate): Lemma (i) integral; identity term and
elliptic term E_m(t) vs the truncated expansion at small t.
"""
import sys
from fractions import Fraction as Fr
from math import factorial
import sympy
import mpmath as mp
from tf_lib import (phi_direct, sigmas, p_poly, p_basis_weights, poly_eval,
                    bern_even, alpha_printed, cot_power_sums)

L = 40
sig = sigmas(L + 3)

# ---- 1 & 2: Lemma 2.5
x = sympy.Symbol('x')
for l in range(L + 1):
    P = p_poly(l, sig)                       # in M = m^2  -> even in m automatically
    assert all(isinstance(c, Fr) for c in P)
    assert len(P) == l + 2 and P[-1] != 0    # degree l+1 in M = degree 2l+2 in m
    lead = abs(bern_even(2 * l + 2)) / (2 * factorial(l + 1) * (2 * l + 1))
    assert P[-1] == lead, l
    assert sum(P) == 0                       # p_l(1) = 0
    W = p_basis_weights(l, sig)
    assert W[0] == 0 and all(w > 0 for w in W[1:]), (l, W)
    # W reproduces P
    Q = [Fr(0)] * (l + 2)
    for n in range(1, l + 2):
        Q[n] += W[n]
        Q[0] -= W[n]
    assert Q == P, l
    # p_l(1+x): all coefficients of x^1..x^{2l+2} positive
    poly_m = sum(sympy.Rational(c.numerator, c.denominator) * (1 + x) ** (2 * e)
                 for e, c in enumerate(P))
    co = sympy.Poly(sympy.expand(poly_m), x).all_coeffs()[::-1]
    assert co[0] == 0 and all(c > 0 for c in co[1:]), l
    # against the defining sum, m = 1..30
for m in range(1, 31):
    ph = phi_direct(m, L)
    for l in range(L + 1):
        direct = Fr(1, 4 ** l) * sum((Fr(factorial(2 * k), factorial(k) * factorial(l - k)) * m * ph[k]
                                      for k in range(l + 1)), Fr(0))
        assert direct == poly_eval(p_poly(l, sig), m), (m, l)
print(f"Lemma 2.5 holds for every l<={L}: even, rational, deg 2l+2, p(1)=0, leading coeff,")
print(f"  positive weights on (m^2n-1), p_l(1+x) has positive coefficients; (bl) from the")
print(f"  defining sum equals the polynomial for m=1..30, l<={L}.")

# ---- 3: alpha_k
pi = sympy.pi
Mk = []
for k in range(L + 1):
    zeta_form = (1 - sympy.Rational(1, 2 ** (2 * k + 1))) * sympy.factorial(2 * k + 1) \
        * sympy.zeta(2 * k + 2) / (2 * pi) ** (2 * k + 2)
    zeta_form = sympy.nsimplify(sympy.simplify(zeta_form))
    assert zeta_form.is_Rational, k
    printed = (1 - Fr(1, 2 ** (2 * k + 1))) * (-1) ** k * bern_even(2 * k + 2) / (4 * (k + 1))
    assert Fr(str(zeta_form)) == printed, k
    Mk.append(printed)
# S(t) = 1 - 4 t sum_k (-t)^k M_k/k!  ; alpha = coefficients of e^{-t/4} S(t)
S = [Fr(1)] + [Fr(-4) * Fr(-1) ** k * Mk[k] / factorial(k) for k in range(L)]
E = [Fr(-1, 4) ** j / factorial(j) for j in range(L + 1)]
alpha_id = [sum((S[i] * E[k - i] for i in range(k + 1)), Fr(0)) for k in range(L + 1)]
for k in range(L + 1):
    assert alpha_id[k] == alpha_printed(k), k
print(f"(alphak) = identity-term coefficients for k<={L}; moment formula = zeta form for k<={L}")

# ---- 4: printed values
assert [alpha_printed(k) for k in range(5)] == [1, Fr(-1, 3), Fr(1, 15), Fr(-4, 315), Fr(1, 315)]
p0 = [Fr(-1, 12), Fr(1, 12)]
p1 = [Fr(-11, 360), Fr(1, 36), Fr(1, 360)]
p2 = [Fr(-37, 5040), Fr(1, 180), Fr(1, 720), Fr(1, 2520)]
assert p_poly(0, sig) == p0 and p_poly(1, sig) == p1 and p_poly(2, sig) == p2
print("printed alpha_0..alpha_4 and p_0, p_1, p_2: OK")
print("  alpha_5..alpha_7 =", [str(alpha_printed(k)) for k in range(5, 8)])
print("  p_3 =", [str(c) for c in p_poly(3, sig)], "(coefficients of m^0, m^2, ...)")

# ---- 5: c_j indexing and literature values (K = -1)
for m in range(2, 31):
    P = cot_power_sums(m, 4)
    s2 = P[0] + P[2]                       # sum csc^2 = sum (1+cot^2)
    s4 = P[0] + 2 * P[2] + P[4]            # sum csc^4
    assert s2 == Fr(m * m - 1, 3) and s4 == Fr(m ** 4 + 10 * m * m - 11, 45), m
    b0 = poly_eval(p_poly(0, sig), m) / m
    b1 = -poly_eval(p_poly(1, sig), m) / m
    b2 = poly_eval(p_poly(2, sig), m) / m
    # DGGW Prop 5.5 / (5.7): (1/m)(m^2-1)/12 ;  (5.10): R1212 (m^4+10m^2-11)/(360 m), R1212=K=-1
    assert b0 == Fr(m * m - 1, 12 * m)
    assert b1 == Fr(-1) * Fr(m ** 4 + 10 * m * m - 11, 360 * m)
    assert b1 == Fr(1, m) * Fr(-1, 8) * s4      # (1/m) sum R1212/(8 sin^4)
    # Schueth Rem 4.2 (a_0, a_1 with K=-1), Thm 4.1 (a_2 with K^2 = 1, Delta K = 0)
    k = Fr(m)
    assert b0 == Fr(1, 12) * (k - 1 / k)
    assert b1 == (Fr(1, 360) * (k ** 3 - 1 / k) + Fr(1, 36) * (k - 1 / k)) * (-1)
    assert b2 == Fr(1, 2520) * (k ** 5 - 1 / k) + Fr(1, 720) * (k ** 3 - 1 / k) + Fr(1, 180) * (k - 1 / k)
# smooth part: c_2 = alpha_1 A/4pi = chi/6 (DGGW (5.7)), c_3 = a_2/4pi with a_2 = (1/360)(2|R|^2-2|rho|^2+5 tau^2) A
K = -1
a2_over_A = Fr(1, 360) * (2 * 4 * K * K - 2 * 2 * K * K + 5 * (2 * K) ** 2)
assert a2_over_A == alpha_printed(2)
# alpha_1 * A/4pi = chi/6 with A = -2 pi chi  <=>  alpha_1 * (-chi/2) = chi/6
assert alpha_printed(1) * Fr(-1, 2) == Fr(1, 6)
print("c_j indexing: DGGW (5.7),(5.10) [R1212=K=-1] and Schueth Rem 4.2/Thm 4.1 [K=-1]")
print("  reproduced for m=2..30; trig sums of DGGW checked exactly.")

# ---- sanity (floating, NOT a certificate)
mp.mp.dps = 40
for a in [mp.mpf('0.7'), mp.mpf(2), mp.mpf(5)]:
    for s in [mp.mpf(0), mp.mpf('0.3'), a - mp.mpf('0.1')]:
        val = mp.quad(lambda r: mp.exp(-a * r + s * r) / (1 + mp.exp(-2 * mp.pi * r)), [-mp.inf, 0, mp.inf])
        assert abs(val - 1 / (2 * mp.sin((a - s) / 2))) < mp.mpf(10) ** -25
t = mp.mpf('0.02')
idt = mp.quad(lambda r: r * mp.tanh(mp.pi * r) * mp.exp(-t * (mp.mpf(1) / 4 + r * r)), [-mp.inf, 0, mp.inf])
ser = sum(mp.mpf(alpha_printed(k).numerator) / alpha_printed(k).denominator * t ** (k - 1) for k in range(12))
assert abs(idt - ser) < mp.mpf(10) ** -15, (idt, ser)
for m in range(2, 8):
    Em = mp.mpf(0)
    for j in range(1, m):
        a = 2 * mp.pi * j / m
        Em += 1 / (2 * m * mp.sin(mp.pi * j / m)) * mp.quad(
            lambda r: mp.exp(-a * r) / (1 + mp.exp(-2 * mp.pi * r)) * mp.exp(-t * (mp.mpf(1) / 4 + r * r)),
            [-mp.inf, 0, mp.inf])
    serE = mp.mpf(0)
    NT = 10
    for l in range(NT):
        pl = poly_eval(p_poly(l, sig), m)
        serE += (-1) ** l * mp.mpf(pl.numerator) / pl.denominator / m * t ** l
    pn = poly_eval(p_poly(NT, sig), m)
    nxt = abs(mp.mpf(pn.numerator) / pn.denominator / m * t ** NT)
    # alternating-type asymptotic series: error should be of the size of the first omitted term
    assert abs(Em - serE) < 2 * nxt, (m, Em, serE, nxt)
print("sanity (mpmath, not a certificate): Lemma (i) integral; I(t), E_m(t) at t=0.02 match the series")
print("ALL CHECKS PASSED")
sys.exit(0)
