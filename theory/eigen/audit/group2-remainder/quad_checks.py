"""High-precision quadrature checks of eig:remcone, eig:remarea, eig:Grem from the integrals of thm:IEH.

E_m(t) and I(t) are computed directly by mpmath quadrature (no use of the expansions); the
coefficients b_l, alpha_k, g_k, mu_k come from exact_checks.py (manuscript formulas eq:phik, eq:bl,
alpha_k of prop:heatinput). Checks raise on failure.
Also tests the strengthened bounds found in the audit:
  |E_m - sum_{l<K} b_l t^l| <= |b_K| t^K,  sign (-1)^K;   |I/(A/4pi) - sum_{k<=K} alpha_k t^{k-1}| <= |alpha_{K+1}| t^K, sign (-1)^{K+1}.
"""
import sys, time
import mpmath as mp
from fractions import Fraction as Fr
import importlib.util

spec = importlib.util.spec_from_file_location("ex", __file__.replace("quad_checks.py", "exact_checks.py"))
ex = importlib.util.module_from_spec(spec); spec.loader.exec_module(ex)

mp.mp.dps = 50
KMAX = 8
MS = list(range(2, 21))
TS_ALL = ['1e-4', '1e-3', '1e-2', '0.05', '0.1', '0.3', '0.5', '1', '2', '3']
TS = sys.argv[1].split(',') if len(sys.argv) > 1 else TS_ALL


def f2m(x):
    return mp.mpf(x.numerator) / x.denominator


def Fint(a, t):
    """int_R e^{-a r} e^{-t r^2}/(1+e^{-2 pi r}) dr, 0<a<2pi; returns (value, error estimate)."""
    pos = lambda r: mp.exp(-a * r - t * r * r) / (1 + mp.exp(-2 * mp.pi * r))
    neg = lambda r: mp.exp((2 * mp.pi - a) * r - t * r * r) / (1 + mp.exp(2 * mp.pi * r))
    v1, e1 = mp.quad(pos, [0, 1, 10, mp.inf], error=True)
    v2, e2 = mp.quad(neg, [-mp.inf, -10, -1, 0], error=True)
    return v1 + v2, e1 + e2


def E(m, t):
    s = mp.mpf(0); err = mp.mpf(0)
    for j in range(1, m):
        th = mp.pi * j / m
        v, e = Fint(2 * th, t)
        c = 1 / (2 * m * mp.sin(th))
        s += c * v; err += c * e
    return mp.exp(-t / 4) * s, err


def Ihat(t):
    """I(t)/(Area/4pi) = e^{-t/4} int_R r tanh(pi r) e^{-t r^2} dr, computed directly."""
    f = lambda r: 2 * r * mp.tanh(mp.pi * r) * mp.exp(-t * r * r)
    v, e = mp.quad(f, [0, 1, 10, 100, mp.inf], error=True)
    return mp.exp(-t / 4) * v, e


# sanity: t=0 limit is Euler's beta integral 1/(2 sin(a/2)); and direct I vs 1/t - 4 int r/(e^{2pi r}+1) e^{-tr^2}
for a in (mp.pi / 10, 1, 3, 2 * mp.pi - mp.mpf(1) / 3):
    v, e = Fint(a, mp.mpf(0))
    assert abs(v - 1 / (2 * mp.sin(a / 2))) < mp.mpf(10)**-40, a
for tt in ('1e-3', '1'):
    tt = mp.mpf(tt)
    alt = 1 / tt - 4 * mp.quad(lambda r: r * mp.exp(-tt * r * r) / (mp.exp(2 * mp.pi * r) + 1), [0, 1, 10, mp.inf])
    assert abs(Ihat(tt)[0] - mp.exp(-tt / 4) * alt) < mp.mpf(10)**-38, tt

g = {(k, m): f2m(ex.g(k, m)) for m in MS for k in range(KMAX + 1)}
b = {(l, m): f2m(ex.b_manuscript(l, m)) for m in MS for l in range(KMAX + 1)}
al = [f2m(ex.alpha_manuscript(k)) for k in range(KMAX + 2)]
mu = [f2m(ex.mu(k)) for k in range(KMAX + 1)]


def Qcone(m, K, t):
    return abs(g[(K, m)]) + mp.exp(t / 4) * sum(abs(g[(k, m)]) * mp.mpf(4)**(k - K) / mp.factorial(K - k) for k in range(K))


def Qarea(K, t):
    return 1 / (mp.mpf(4)**(K + 1) * mp.factorial(K + 1)) + mu[K] / mp.factorial(K) + \
        mp.exp(t / 4) * sum(mu[k] * mp.mpf(4)**(k - K) / (mp.factorial(k) * mp.factorial(K - k)) for k in range(K))


t0 = time.time()
stats = dict(cone=0, area=0, grem=0)
worst_cone = mp.mpf(0); worst_cone_strong = mp.mpf(0); worst_area = mp.mpf(0); worst_area_strong = mp.mpf(0)
Ecache = {}
Icache = {}
for ts in TS:
    t = mp.mpf(ts)
    # area
    Iv, Ie = Ihat(t)
    Icache[ts] = (Iv, Ie)
    for K in range(KMAX + 1):
        rem = Iv - sum(al[k] * t**(k - 1) for k in range(K + 1))
        bound = t**K * Qarea(K, t)
        strong = t**K * abs(al[K + 1])
        tol = 10 * Ie + mp.mpf(10)**-40 / t
        if not abs(rem) <= bound + tol:
            raise AssertionError(("area", ts, K, rem, bound))
        if not abs(rem) <= strong + tol:
            raise AssertionError(("area strong", ts, K, rem, strong))
        if abs(rem) > 1000 * tol and not (rem > 0) == (K % 2 == 1):  # sign of alpha_{K+1}
            raise AssertionError(("area sign", ts, K, rem))
        worst_area = max(worst_area, abs(rem) / bound)
        worst_area_strong = max(worst_area_strong, abs(rem) / strong)
        stats['area'] += 1
    # cone
    for m in MS:
        Ev, Ee = E(m, t)
        Ecache[(m, ts)] = (Ev, Ee)
        for K in range(KMAX + 1):
            rem = Ev - sum(b[(l, m)] * t**l for l in range(K))
            bound = t**K * Qcone(m, K, t)
            strong = t**K * abs(b[(K, m)])
            tol = 10 * Ee + mp.mpf(10)**-40
            if not abs(rem) <= bound + tol:
                raise AssertionError(("cone", m, ts, K, rem, bound))
            if not abs(rem) <= strong + tol:
                raise AssertionError(("cone strong", m, ts, K, rem, strong))
            if abs(rem) > 1000 * tol and not (rem > 0) == (K % 2 == 0):
                raise AssertionError(("cone sign", m, ts, K, rem))
            worst_cone = max(worst_cone, abs(rem) / bound)
            worst_cone_strong = max(worst_cone_strong, abs(rem) / strong)
            stats['cone'] += 1
    print("t=%s done (%.0fs)" % (ts, time.time() - t0)); sys.stdout.flush()

# Grem: signatures with 0..4 cone points from MS, area A computed from (g; m) ; t <= t0 with t0 in TS
import itertools
sigs = [(0, (2, 3, 7)), (0, (2, 2, 2, 3)), (2, ()), (1, (2,)), (2, (5, 5)), (0, (20, 20, 20)), (0, (2, 3, 20)), (3, (2, 2, 2, 2))]
for gg, ms in sigs:
    A = 2 * mp.pi * (2 * gg - 2 + sum(1 - mp.mpf(1) / m for m in ms))
    assert A > 0
    for ts0 in TS_ALL:
        tt0 = mp.mpf(ts0)
        for ts in [x for x in TS if mp.mpf(x) <= tt0]:
            t = mp.mpf(ts)
            Iv, Ie = Icache[ts]
            G = A / (4 * mp.pi) * Iv + sum(Ecache[(m, ts)][0] for m in ms)
            Gerr = A / (4 * mp.pi) * Ie + sum(Ecache[(m, ts)][1] for m in ms)
            for K in range(KMAX + 1):
                c = [None, A / (4 * mp.pi)] + [al[j - 1] * A / (4 * mp.pi) + sum(b[(j - 2, m)] for m in ms) for j in range(2, K + 2)]
                P = sum(c[j] * t**(j - 2) for j in range(1, K + 2))
                bound = t**K * (A / (4 * mp.pi) * Qarea(K, tt0) + sum(Qcone(m, K, tt0) for m in ms))
                if not abs(G - P) <= bound + 10 * Gerr + mp.mpf(10)**-38 / t:
                    raise AssertionError(("Grem", gg, ms, ts0, ts, K))
                stats['grem'] += 1
print("counts:", stats)
print("max |rem|/(t^K Q_cone)      = %s" % mp.nstr(worst_cone, 10))
print("max |rem|/(|b_K| t^K)       = %s" % mp.nstr(worst_cone_strong, 10))
print("max |rem|/(t^K Q_area)      = %s" % mp.nstr(worst_area, 10))
print("max |rem|/(|alpha_{K+1}|t^K) = %s" % mp.nstr(worst_area_strong, 10))
print("ALL QUADRATURE CHECKS PASSED (%.0fs)" % (time.time() - t0))
