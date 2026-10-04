#!/usr/bin/env python3
"""LO.1 / LO.6: small-t expansion of the identity and elliptic terms of the
Dryden-Strohmaier trace formula (DS eq. (1)) applied to h_t(r)=exp(-t(1/4+r^2)),
compared, in exact rational arithmetic, with
  * LO.1's alpha_k and Ucar (4.35) at kappa=-1,
  * Ucar (4.33)/(4.25) (the cone series C) at kappa=-1,
  * DGGW (5.7) (degree-zero term) and (5.9)/(5.10) (degree-one cone term).

Run from the repository root:
  python3 review/audit/locality/check_expansion.py
Exits nonzero on any failed assertion.
"""
import sys
import sympy as sp
import mpmath as mp

K_MAX = 7          # orders t^k checked
M_RANGE = range(2, 14)

t = sp.Symbol('t')
B = sp.bernoulli


def Bhalf(n):
    # B_n(1/2), exact
    return sp.bernoulli(n, sp.Rational(1, 2))


# ---------------------------------------------------------------- identity term
# I(t)*4pi/A = int_R r tanh(pi r) e^{-t(1/4+r^2)} dr
#            = e^{-t/4} [ 1/t - 4 int_0^oo r e^{-t r^2}/(1+e^{2 pi r}) dr ]
# using tanh(pi r) = 1 - 2/(1+e^{2 pi r}) for r>0 and evenness of r tanh(pi r).
# Expanding e^{-t r^2} termwise (legitimate as an asymptotic expansion because
# r^{2j+1}/(1+e^{2 pi r}) is integrable for every j):
#   mu_j = int_0^oo r^{2j+1}/(1+e^{2 pi r}) dr = (1-2^{-2j-1}) (2j+1)! zeta(2j+2)/(2pi)^{2j+2}
# from int_0^oo x^{s-1}/(e^x+1) dx = (1-2^{1-s}) Gamma(s) zeta(s)  (expand 1/(e^x+1)
# = sum_{n>=1} (-1)^{n-1} e^{-nx}).

def mu(j):
    s = 2 * j + 2
    val = (1 - sp.Rational(1, 2) ** (s - 1)) * sp.factorial(s - 1) * sp.zeta(s) / (2 * sp.pi) ** s
    val = sp.nsimplify(sp.simplify(val))
    assert val.is_rational, (j, val)
    return sp.Rational(val)


def alpha_from_trace(kmax):
    ser = 1 - 4 * sum((-1) ** j * t ** (j + 1) * mu(j) / sp.factorial(j) for j in range(kmax + 1))
    ser = sp.expand(sp.series(sp.exp(-t / 4), t, 0, kmax + 2).removeO() * ser)
    return [sp.Rational(ser.coeff(t, k)) for k in range(kmax + 1)]


def alpha_LO1(k):
    # LO.1: alpha_k = (-1)^k/(k! 4^k) sum_l C(k,l) (-4)^l B_{2l}(1/2)
    return sp.Rational((-1) ** k, sp.factorial(k) * 4 ** k) * sum(
        sp.binomial(k, l) * (-4) ** l * Bhalf(2 * l) for l in range(k + 1))


def alpha_ucar(k, kappa=-1):
    # Ucar (4.35): a_nu(O)/vol(O) = 1/(nu! 4^nu) sum_l C(nu,l)(-4)^l B_{2l}(1/2) kappa^nu
    return sp.Rational(1, sp.factorial(k) * 4 ** k) * sum(
        sp.binomial(k, l) * (-4) ** l * Bhalf(2 * l) for l in range(k + 1)) * kappa ** k


# ---------------------------------------------------------------- elliptic term
# E_m(t) = sum_{l=1}^{m-1} 1/(2m sin(pi l/m)) int_R e^{-2pi l r/m}/(1+e^{-2pi r}) e^{-t(1/4+r^2)} dr.
# F(a) := int_R e^{-a r}/(1+e^{-2 pi r}) dr = 1/(2 sin(a/2)),  0<a<2pi,
# so int_R r^{2j} e^{-a r}/(1+e^{-2pi r}) dr = F^{(2j)}(a) = 2^{-2j-1} csc^{(2j)}(a/2).
# Even derivatives of csc are polynomials in (csc, cot) with even cot-degree;
# with cot^2 = csc^2 - 1 they become polynomials in csc. Hence
#   (1/(2m)) csc(x) F^{(2j)}(2x) is a polynomial in csc^2(x), x = pi l/m,
# and sum_l csc^{2k}(pi l/m) = sum over roots y of U_{m-1} of (1-y^2)^{-k}, exact (RootSum).

s_, c_ = sp.symbols('s c')  # s = csc x, c = cot x ; ds/dx = -s c, dc/dx = -s^2


def csc_deriv_poly(n):
    Q = s_
    for _ in range(n):
        Q = sp.expand(sp.diff(Q, s_) * (-s_ * c_) + sp.diff(Q, c_) * (-s_ ** 2))
    return Q


def csc_power_sum(m, k, _cache={}):
    """sum_{l=1}^{m-1} csc^{2k}(pi l/m), exact.

    The numbers u_l = 1/sin^2(pi l/m) = 1/(1-y_l^2), y_l = cos(pi l/m) the roots of the
    Chebyshev polynomial U_{m-1}, are the roots of R(u) = Res_y(U_{m-1}(y), u(1-y^2)-1).
    Power sums of the roots follow from Newton's identities (exact rationals)."""
    if m not in _cache:
        y, u = sp.symbols('y u')
        U = sp.Poly(sp.chebyshevu(m - 1, y), y)
        R = sp.Poly(sp.resultant(U.as_expr(), u * (1 - y ** 2) - 1, y), u)
        assert R.degree() == m - 1
        a = [sp.Rational(c) for c in R.all_coeffs()]  # a[0] u^n + a[1] u^{n-1} + ...
        n = len(a) - 1
        e = [sp.Rational((-1) ** i) * a[i] / a[0] for i in range(n + 1)]  # elementary symmetric
        p = [sp.Rational(n)]
        for kk in range(1, 40):
            val = sum((-1) ** (i - 1) * e[i] * p[kk - i] for i in range(1, min(kk, n + 1)))
            if kk <= n:
                val += (-1) ** (kk - 1) * kk * e[kk]
            p.append(sp.Rational(val))
        _cache[m] = p
    return _cache[m][k]


def moment_sum(m, j):
    """M_{2j}(m) = sum_l 1/(2m sin x_l) * F^{(2j)}(2 x_l), x_l = pi l/m, exact rational."""
    Q = csc_deriv_poly(2 * j)
    Q = sp.expand(Q.subs(c_ ** 2, s_ ** 2 - 1))  # only even powers of c occur
    # make sure no odd powers of c survive
    Q = sp.expand(sp.Poly(Q, c_).as_expr())
    Qp = sp.Poly(Q, c_)
    total = 0
    for (deg,), coeff in Qp.terms():
        assert deg % 2 == 0
        total += sp.expand(coeff * (s_ ** 2 - 1) ** (deg // 2))
    summand = sp.expand(sp.Rational(1, 2 * m) * s_ * total * sp.Rational(1, 2 ** (2 * j + 1)))
    P = sp.Poly(summand, s_)
    out = 0
    for (deg,), coeff in P.terms():
        assert deg % 2 == 0, deg
        out += coeff * csc_power_sum(m, deg // 2)
    return sp.Rational(out)


def beta_from_trace(m, kmax):
    ser = sum((-t) ** j / sp.factorial(j) * moment_sum(m, j) for j in range(kmax + 1))
    ser = sp.expand(sp.series(sp.exp(-t / 4), t, 0, kmax + 1).removeO() * ser)
    return [sp.Rational(ser.coeff(t, k)) for k in range(kmax + 1)]


def cS_ucar(l, k):
    # Ucar (4.25)
    return sp.Rational(1, 4 * k) * sp.Rational((-1) ** l, sp.factorial(l + 1)) * sp.Rational(1, 2 * l + 1) * sum(
        sp.binomial(2 * l + 2, 2 * j) * (k ** (2 * j) - 1) * B(2 * j) * Bhalf(2 * l + 2 - 2 * j)
        for j in range(l + 2))


def beta_ucar(m, nu, kappa=-1):
    # Ucar (4.33): coefficient of t^nu in C
    return sum(sp.Rational(2, 4 ** l * sp.factorial(l)) * cS_ucar(nu - l, m) for l in range(nu + 1)) * kappa ** nu


def main():
    out = []
    # --- closed-form sanity checks (mpmath, labelled as such) -----------------
    mp.mp.dps = 30
    for j in range(4):
        num = mp.quad(lambda r: r ** (2 * j + 1) / (1 + mp.e ** (2 * mp.pi * r)), [0, mp.inf])
        assert abs(num - mp.mpf(sp.Rational(mu(j)).p) / sp.Rational(mu(j)).q) < mp.mpf(10) ** -30
    out.append("[sanity, mpmath] mu_j closed form agrees with quadrature for j<=3")
    for (l, m) in [(1, 2), (1, 3), (2, 5), (3, 7), (1, 11)]:
        a = 2 * mp.pi * l / m
        for j in range(3):
            num = mp.quad(lambda r: r ** (2 * j) * mp.e ** (-a * r) / (1 + mp.e ** (-2 * mp.pi * r)), [-mp.inf, 0, mp.inf])
            ref = mp.diff(lambda aa: 1 / (2 * mp.sin(aa / 2)), a, 2 * j)
            assert abs(num - ref) < mp.mpf(10) ** -20, (l, m, j, num, ref)
    out.append("[sanity, mpmath] F^{(2j)}(a) = int r^{2j} e^{-ar}/(1+e^{-2pi r}) dr for sample (l,m), j<=2")

    # --- exact trig sums against DGGW Lemma 5.4 and the sum quoted after (5.9)
    for m in M_RANGE:
        assert csc_power_sum(m, 1) == sp.Rational(m * m - 1, 3)
        assert csc_power_sum(m, 2) == sp.Rational(m ** 4 + 10 * m ** 2 - 11, 45)
    out.append("[exact] sum csc^2 = (m^2-1)/3 and sum csc^4 = (m^4+10m^2-11)/45 for m=2..13")

    # --- alpha_k
    al = alpha_from_trace(K_MAX)
    for k in range(K_MAX + 1):
        assert al[k] == alpha_LO1(k) == alpha_ucar(k), (k, al[k], alpha_LO1(k), alpha_ucar(k))
    out.append("[exact] alpha_k (trace formula identity term) == LO.1 formula == Ucar (4.35)/vol at kappa=-1, k=0..%d" % K_MAX)
    out.append("        alpha = " + ", ".join(str(a) for a in al))
    assert al[0] == 1 and al[1] == sp.Rational(-1, 3)

    # --- beta_k(m)
    for m in M_RANGE:
        bt = beta_from_trace(m, K_MAX)
        for k in range(K_MAX + 1):
            bu = beta_ucar(m, k)
            assert bt[k] == bu, (m, k, bt[k], bu)
        # DGGW (5.7): degree-zero cone term (m^2-1)/(12 m)
        assert bt[0] == sp.Rational(m * m - 1, 12 * m)
        # DGGW (5.9)/(5.10): cone term of degree one = R1212 (m^4+10m^2-11)/(360 m); with R1212=K=-1:
        assert bt[1] == -sp.Rational(m ** 4 + 10 * m ** 2 - 11, 360 * m), (m, bt[1])
        # Schueth Thm 4.1 (arXiv:1812.06119, p.14): a_2({p}) with K = -1 constant (Delta K = 0)
        k_ = sp.Rational(m)
        schueth = (k_ ** 5 - 1 / k_) / 2520 + (k_ ** 3 - 1 / k_) / 720 + (k_ - 1 / k_) / 180
        assert bt[2] == schueth, (m, bt[2], schueth)
        if m <= 4:
            out.append("        beta_k(%d) = %s" % (m, ", ".join(str(b) for b in bt)))
    out.append("[exact] beta_k(m) (trace formula elliptic term) == Ucar (4.33) at kappa=-1, m=2..13, k=0..%d" % K_MAX)
    out.append("[exact] beta_2(m) == Schueth Thm 4.1 at K=-1, Delta K=0, m=2..13")
    out.append("[exact] beta_0(m) == (m^2-1)/(12m)  [DGGW (5.7)];  beta_1(m) == -(m^4+10m^2-11)/(360m)  [DGGW (5.10), R1212=-1]")

    # --- degree-zero total = chi/6 + sum (m^2-1)/(12m)   [DGGW (5.7)]
    # A/(4 pi) * alpha_1 = -chi/2 * (-1/3) = chi/6
    out.append("[exact] (A/4pi)*alpha_1 = (-chi/2)(-1/3) = chi/6, matching DGGW (5.7)")

    # --- the DS elliptic normalisation is the one that reproduces DGGW: doubling it would not
    for m in M_RANGE:
        assert 2 * beta_from_trace(m, 0)[0] != sp.Rational(m * m - 1, 12 * m)
    out.append("[exact] a factor-2 change in the DS elliptic weight 1/(2 m sin theta) would contradict DGGW (5.7)")

    text = "\n".join(out)
    print(text)
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        import traceback; traceback.print_exc(); print("ASSERTION FAILED:", e)
        sys.exit(1)
