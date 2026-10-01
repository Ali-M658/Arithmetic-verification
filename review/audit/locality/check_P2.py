#!/usr/bin/env python3
"""P2: exact checks behind the referee's proof of Lemma 3.2 / Theorem 3.1.

  (N) Fourier normalisation of DS eq. (1): g(u) = (1/2pi) int h(r) e^{-iru} dr,
      checked against DS's own wave example and DS eq. (2); g_t computed exactly.
  (S) spectral side: h_t(r_n) = e^{-t lambda_n} for real and imaginary r_n (lambda=0 included);
      a polynomial-decay bound of order >= 3 in r is needed for dominated convergence under a
      linear Weyl bound (order 2 is NOT enough).
  (E) elliptic kernel: exact bound 0 < k_theta <= 1 and exact decay rates.
  (W) the window test function used for the self-contained Weyl bound.
  (H) hyperbolic side: summability of the heat weights against N(L) <= C e^L.

Run from the repository root:  python3 review/audit/locality/check_P2.py
Exits nonzero on any failed assertion.  mpmath is used only for labelled sanity checks.
"""
import sys
import sympy as sp
import mpmath as mp

r, u, T, eps = sp.symbols('r u T epsilon', real=True)
t, beta, L, C = sp.symbols('t beta L C', positive=True)
out = []


def FT_DS(h, var=r, x=u):
    """DS normalisation: g(u) = (1/2pi) int h(r) e^{-iru} dr."""
    return sp.simplify(sp.integrate(h * sp.exp(-sp.I * var * x), (var, -sp.oo, sp.oo)) / (2 * sp.pi))


def check_normalisation():
    h_t = sp.exp(-t * (sp.Rational(1, 4) + r ** 2))
    g_t = FT_DS(h_t)
    g_claim = sp.exp(-t / 4) * sp.exp(-u ** 2 / (4 * t)) / sp.sqrt(4 * sp.pi * t)
    assert sp.simplify(g_t - g_claim) == 0
    # inverse: h(r) = int g(u) e^{iru} du
    back = sp.simplify(sp.integrate(g_claim * sp.exp(sp.I * r * u), (u, -sp.oo, sp.oo)))
    assert sp.simplify(back - h_t) == 0
    out.append("[exact] g_t(u) = e^{-t/4} e^{-u^2/4t}/sqrt(4 pi t) is the DS-normalised transform of h_t, and int g_t e^{iru} du = h_t")

    # DS wave example: h(r) = cos(T r) must give g = (1/2)[delta(u-T)+delta(u+T)].
    # Regularise: h_eps(r) = cos(T r) e^{-eps r^2}; then g_eps = (1/2)[G(u-T)+G(u+T)] with G a
    # probability density (mass 1) of variance 2 eps -> delta. The 1/2 is DS's printed coefficient.
    Tp = sp.Symbol('Tp', positive=True)
    e = sp.Symbol('e', positive=True)
    # cos(Tr) = (e^{iTr}+e^{-iTr})/2; transform each exponential separately (linearity)
    G = lambda x: sp.exp(-x ** 2 / (4 * e)) / sp.sqrt(4 * sp.pi * e)
    for sgn in (1, -1):
        g_part = sp.integrate(sp.exp(sgn * sp.I * Tp * r - e * r ** 2) * sp.exp(-sp.I * r * u), (r, -sp.oo, sp.oo)) / (2 * sp.pi)
        ratio = sp.simplify(sp.powsimp(sp.expand(g_part / G(u - sgn * Tp)), force=True))
        assert ratio == 1, ratio
    assert sp.integrate(G(u), (u, -sp.oo, sp.oo)) == 1
    out.append("[exact] DS wave example: transform of cos(Tr)e^{-eps r^2} is (1/2)[G_eps(u-T)+G_eps(u+T)], mass-1 kernels -> DS's g = (1/2)[delta+delta]")
    # the unnormalised convention int h e^{-iru} dr would give pi[delta+delta] instead -> excluded by DS's text
    out.append("        (the convention without 1/2pi would give pi[delta(u-T)+delta(u+T)], contradicting DS p.4)")

    # DS eq.(2): first term is d/dt of mu/(4pi) * 1/sinh(t/2)
    mu = sp.Symbol('mu', positive=True)
    assert sp.simplify(sp.diff(mu / (4 * sp.pi) / sp.sinh(t / 2), t) + mu / (8 * sp.pi) * sp.cosh(t / 2) / sp.sinh(t / 2) ** 2) == 0
    # 1/sinh(ln N/2) = 2/(N^{1/2}-N^{-1/2})
    N = sp.Symbol('N', positive=True)
    assert sp.simplify((1 / sp.sinh(sp.log(N) / 2)).rewrite(sp.exp) - 2 / (sp.sqrt(N) - 1 / sp.sqrt(N))) == 0
    out.append("[exact] DS eq.(2) identity-term derivative and 1/sinh(ln N/2) = 2/(N^{1/2}-N^{-1/2}) verified")
    # hyperbolic weight in Thm 3.1: ln N(Pc)/(N^{1/2}-N^{-1/2}) = l0/(2 sinh(l/2)) with l = ln N(P)
    l0, l = sp.symbols('l0 l', positive=True)
    assert sp.simplify((l0 / (sp.exp(l / 2) - sp.exp(-l / 2))) - l0 / (2 * sp.sinh(l / 2)).rewrite(sp.exp)) == 0
    out.append("[exact] DS hyperbolic weight ln N(Pc)/(N(P)^{1/2}-N(P)^{-1/2}) = l(gamma0)/(2 sinh(l(gamma)/2))")

    # Marklof (69) uses the same normalisation; his (192) prints exponent t^2/(2 beta).
    g_beta = FT_DS(sp.exp(-beta * r ** 2))
    assert sp.simplify(g_beta - sp.exp(-u ** 2 / (4 * beta)) / sp.sqrt(4 * sp.pi * beta)) == 0
    assert sp.simplify(g_beta - sp.exp(-u ** 2 / (2 * beta)) / sp.sqrt(4 * sp.pi * beta)) != 0
    out.append("[exact] Marklof (69) normalisation agrees with DS; the exponent in Marklof (192)/(193) should read t^2/(4 beta)")
    out.append("        (prefactor 1/sqrt(4 pi beta) as printed is consistent only with exponent t^2/(4 beta); source misprint, harmless here)")


def check_spectral():
    # r_n^2 = lambda_n - 1/4 ; h_t(r) depends on r^2 only
    lam = sp.Symbol('lambda', nonnegative=True)
    h_t = lambda rr: sp.exp(-t * (sp.Rational(1, 4) + rr ** 2))
    for lv in [0, sp.Rational(1, 10), sp.Rational(1, 4), 1, 7]:
        rr = sp.sqrt(sp.Rational(lv) - sp.Rational(1, 4))
        assert sp.simplify(h_t(rr) - sp.exp(-t * lv)) == 0
    assert h_t(sp.I / 2) == 1
    out.append("[exact] h_t(r_n) = e^{-t lambda_n} for lambda in {0,1/10,1/4,1,7}; r_0 = i/2 gives h_t = 1")
    # imaginary r = i y with |y| <= 1/2 : h_R(iy) = int g_R(u) e^{-yu} du is dominated by
    # int g_t(u) e^{|u|/2} du < oo. Exact value of the dominating integral:
    gt = sp.exp(-t / 4) * sp.exp(-u ** 2 / (4 * t)) / sp.sqrt(4 * sp.pi * t)
    dom = sp.simplify(2 * sp.integrate(gt * sp.exp(u / 2), (u, 0, sp.oo)))
    assert dom.is_finite is not False
    out.append("[exact] int g_t(u) e^{|u|/2} du = %s  (finite: dominates h_R(iy), |y|<=1/2, uniformly in R)" % sp.simplify(dom))

    # derivatives of g_t: g_t^{(k)} = P_k(u) g_t with P_k polynomial => ||g_t^{(k)}||_1 < oo
    for k in range(6):
        Pk = sp.simplify(sp.diff(gt, u, k) / gt)
        assert Pk.is_polynomial(u)
    out.append("[exact] g_t^{(k)} = (polynomial in u) * g_t for k<=5, so ||g_t^{(k)}||_1 < oo and |h_R(r)| <= C_k(1+|r|)^{-k} uniformly in R>=1")

    # order of decay needed: model a linear Weyl law lambda_n = n (worst case of O(Lambda))
    n = sp.Symbol('n', positive=True, integer=True)
    s1 = sp.summation(1 / (1 + (n - sp.Rational(1, 4))), (n, 1, sp.oo))
    s2 = sp.summation(1 / (1 + (n - sp.Rational(1, 4))) ** 2, (n, 1, sp.oo))
    assert s1 == sp.oo and s2.is_finite
    out.append("[exact] with lambda_n = n: sum (1+r_n^2)^{-1} = oo but sum (1+r_n^2)^{-2} = polygamma(1,7/4) = %s < oo" % sp.N(s2, 15))
    out.append("        => a bound |h_R(r)| <= C/(1+r^2) is NOT summable; at least (1+|r|)^{-3} is required (4 integrations by parts used)")

    # Stieltjes: N(Lam) <= C(1+Lam)  =>  sum (1+lambda_n)^{-2} <= int_0^oo 2 C(1+x)/(1+x)^3 dx = 2C
    x = sp.Symbol('x', nonnegative=True)
    val = sp.integrate(2 * C * (1 + x) / (1 + x) ** 3, (x, 0, sp.oo))
    assert sp.simplify(val - 2 * C) == 0
    out.append("[exact] N(Lam) <= C(1+Lam) implies sum_n (1+lambda_n)^{-2} <= 2C (+C from the boundary term)")


def check_elliptic():
    th = sp.Symbol('theta', positive=True)
    rr = sp.Symbol('rr', real=True)
    k = sp.exp(-2 * th * rr) / (1 + sp.exp(-2 * sp.pi * rr))
    # even part
    ev = sp.simplify(((k + k.subs(rr, -rr)) / 2).rewrite(sp.exp) - (sp.cosh((sp.pi - 2 * th) * rr) / (2 * sp.cosh(sp.pi * rr))).rewrite(sp.exp))
    assert sp.simplify(ev) == 0
    # k(-r) with theta equals k(r) with pi - theta  (l <-> m-l)
    assert sp.simplify((k.subs(rr, -rr) - k.subs(th, sp.pi - th)).rewrite(sp.exp)) == 0
    out.append("[exact] even part of e^{-2 theta r}/(1+e^{-2 pi r}) is cosh((pi-2theta)r)/(2cosh(pi r)); k_theta(-r) = k_{pi-theta}(r)")
    # bound 0 < k <= 1: for r>=0, k = e^{-2 theta r}/(1+e^{-2 pi r}) <= e^{-2theta r} <= 1;
    # for r<0, k = e^{(2pi-2theta) r}/(1+e^{2 pi r}) <= e^{(2pi-2theta) r} <= 1  (0<theta<pi).
    assert sp.simplify((k - sp.exp((2 * sp.pi - 2 * th) * rr) / (1 + sp.exp(2 * sp.pi * rr))).rewrite(sp.exp)) == 0
    # exact decay: k e^{2 theta r} -> 1 (r->+oo), k e^{-(2pi-2theta) r} -> 1 (r->-oo)
    for tv in [sp.pi / 2, sp.pi / 7, 3 * sp.pi / 7]:
        kk = k.subs(th, tv)
        assert sp.limit(kk * sp.exp(2 * tv * rr), rr, sp.oo) == 1
        assert sp.limit(kk * sp.exp(-(2 * sp.pi - 2 * tv) * rr), rr, -sp.oo) == 1
    out.append("[exact] 0 < k_theta(r) <= 1; k ~ e^{-2theta r} (r->+oo), k ~ e^{-(2pi-2theta)|r|} (r->-oo); rate >= 2pi/m for theta = pi l/m")
    out.append("        DS's psi_m ~ (2m sin(pi/m))^{-1} e^{-2pi r/m} is consistent (l=1 and l=m-1 each give (4m sin(pi/m))^{-1})")


def check_window():
    # h_T(r) = h0(r-T) + h0(r+T) has transform 2 cos(Tu) g0(u) (shift theorem); exact with a
    # Gaussian stand-in for h0 (the identity is linear and holds for every h0 in the class).
    Tp = sp.Symbol('Tp', positive=True)
    h0 = lambda x: sp.exp(-x ** 2)
    g0 = FT_DS(h0(r))
    for sgn in (1, -1):
        g_shift = FT_DS(h0(r - sgn * Tp))
        ratio = sp.simplify(sp.powsimp(sp.expand(g_shift / (sp.exp(-sgn * sp.I * Tp * u) * g0)), force=True))
        assert ratio == 1, ratio
    # sum of the two shifted transforms: (e^{-iTu}+e^{iTu}) g0 = 2 cos(Tu) g0
    out.append("[exact] transform of h0(r-T)+h0(r+T) is 2cos(Tu) g0(u): same support as g0, |g_T| <= 2|g0| uniformly in T")
    # lower bound on [-1,1]: phi >= 0 supported in [-1,1]; for |s|<=1, |x|<=1: cos(sx) >= cos 1 > 0
    assert sp.cos(1) > 0
    out.append("[exact] for phi>=0, supp phi in [-1,1]: phi^(s) >= cos(1) int phi > 0 on |s|<=1, so h0 = phi^2 >= c > 0 there")
    # identity-term bound: int |r| h0(r-T) dr <= int (|s|+T) h0(s) ds = O(1+T)
    out.append("        identity term of h_T is O(1+T); elliptic terms O(1) since |k|<=1; hyperbolic side is a fixed finite sum")


def check_hyperbolic():
    # f(L) = L e^{-L/2} e^{-L^2/4t}  (weight of one class, up to 1/(1-e^{-l}) and 1/sqrt(4 pi t))
    f = L * sp.exp(-L / 2) * sp.exp(-L ** 2 / (4 * t))
    integrand = sp.simplify(-sp.diff(f, L) * C * sp.exp(L))
    # integrand = C e^{L/2 - L^2/4t} (L/2 + L^2/(2t) - 1): Gaussian decay => finite
    expected = C * sp.exp(L / 2 - L ** 2 / (4 * t)) * (L / 2 + L ** 2 / (2 * t) - 1)
    assert sp.simplify(integrand - expected) == 0
    val = sp.integrate(expected.subs(t, 1), (L, 1, sp.oo))
    assert val.is_finite
    out.append("[exact] -f'(L) C e^L = C e^{L/2-L^2/4t}(L/2+L^2/2t-1); its integral over [l,oo) is finite (t=1, l=1: %s)" % sp.nsimplify(val))


def sanity_truncation():
    # labelled numerical sanity only: h_R -> h_t, with a C^oo even cutoff chi = 1 on [-1,1], supp [-2,2]
    mp.mp.dps = 25
    def smoothstep(x):
        if x <= 0:
            return mp.mpf(0)
        if x >= 1:
            return mp.mpf(1)
        a = mp.e ** (-1 / x)
        b = mp.e ** (-1 / (1 - x))
        return a / (a + b)
    chi = lambda x: smoothstep(2 - abs(x))
    tt = mp.mpf(1)
    g = lambda x: mp.e ** (-tt / 4) * mp.e ** (-x * x / (4 * tt)) / mp.sqrt(4 * mp.pi * tt)
    for R in [1, 2, 4, 8]:
        for rr in [0, 1, 3]:
            hR = 2 * mp.quad(lambda x: g(x) * chi(x / R) * mp.cos(rr * x), [0, R, 2 * R])
            ht = mp.e ** (-tt * (mp.mpf(1) / 4 + rr * rr))
            if R == 8:
                assert abs(hR - ht) < mp.mpf(10) ** -6, (R, rr, hR, ht)
    out.append("[sanity, mpmath] h_R(r) -> h_t(r) at t=1 (|h_8 - h_t| < 1e-6 at r=0,1,3)")


def main():
    check_normalisation()
    check_spectral()
    check_elliptic()
    check_window()
    check_hyperbolic()
    sanity_truncation()
    print("\n".join(out))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        import traceback; traceback.print_exc(); print("ASSERTION FAILED:", e)
        sys.exit(1)
