"""Checks for Lemma eig:elem, Propositions eig:counttail, eig:hypall, Theorem eig:count,
and the closed form of Theorem eig:diam.  Every check raises on failure."""
from fractions import Fraction
import itertools
import math
import random
import mpmath as mp
import sympy as sp

mp.mp.dps = 30
random.seed(7)


def check(c, msg):
    if not c:
        raise AssertionError(msg)


# ---------- eig:elem (i): Area >= pi/21 and n + 4g <= Area/pi + 4, exact over a large range
def negchi(g, ms):
    return 2 * g - 2 + sum(1 - Fraction(1, m) for m in ms)

best = None; nsig = 0
for g in range(0, 4):
    for n in range(0, 7 if g == 0 else 4):
        top = {3: 120, 4: 40, 5: 14, 6: 8}.get(n, 60)
        for ms in itertools.combinations_with_replacement(range(2, top + 1), n):
            x = negchi(g, ms)
            if x <= 0:
                continue
            nsig += 1
            # Area/pi = 2 x ; n + 4g <= 2x + 4
            check(n + 4 * g <= 2 * x + 4, "n+4g bound fails at %s" % ((g, ms),))
            if best is None or x < best[0]:
                best = (x, g, ms)
check(best[0] == Fraction(1, 42) and best[1:] == (0, (2, 3, 7)), "minimal -chi %s" % (best,))
# analytic completion: g>=2 -> -chi>=2; g=1,n>=1 -> >=1/2; g=0,n>=5 -> >=1/2; g=0,n=4 -> >=1/6
# (orders (2,2,2,3)); g=0,n=3: 1/42 at (2,3,7) is the classical minimum (checked up to 120 above,
# and beyond: if some order exceeds 120 then -chi = 1 - 1/p - 1/q - 1/r with p<=q<=r, r>120, and the
# remaining (p,q) != (2,2) give -chi >= 1/6 - 1/r > 1/42; (2,2,r) is not hyperbolic).
print("eig:elem(i) OK: %d hyperbolic signatures, min -chi = %s at %s, n+4g <= Area/pi+4"
      % (nsig, best[0], best[1:]))

# ---------- eig:elem (ii): sum csc^2 identity, E_m bounds, I bound
for m in range(2, 60):
    s = mp.fsum(1 / mp.sin(mp.pi * j / m) ** 2 for j in range(1, m))
    check(abs(s - mp.mpf(m * m - 1) / 3) < mp.mpf(10) ** -20, "csc^2 sum")
    # b_0 from the manuscript's eq:phik with k = 0: m phi_0 = (1/4) sigma_0 4|B_2|/2! (m^2-1)
    mphi0 = sp.Rational(1, 4) * 1 * 4 * abs(sp.bernoulli(2)) / sp.factorial(2) * (m * m - 1)
    check(sp.simplify(mphi0 / m - sp.Rational(m * m - 1, 12 * m)) == 0, "b_0(m)")
# beta-integral at s=0: int e^{-a r}/(1+e^{-2 pi r}) dr = 1/(2 sin(a/2))
for a in (0.3, 1.0, 2.5, 5.0, 6.0):
    v = mp.quad(lambda r: mp.e ** (-a * r) / (1 + mp.e ** (-2 * mp.pi * r)), [-mp.inf, 0, mp.inf])
    check(abs(v - 1 / (2 * mp.sin(a / 2))) < mp.mpf(10) ** -15, "beta integral")


def E_m(m, t):
    tot = 0
    for j in range(1, m):
        th = mp.pi * j / m
        f = lambda r: mp.e ** (-2 * th * r) * mp.e ** (-t * (mp.mpf(1) / 4 + r * r)) / (1 + mp.e ** (-2 * mp.pi * r))
        tot += mp.quad(f, [-mp.inf, 0, mp.inf]) / (2 * m * mp.sin(th))
    return tot


def I_over_area(t):
    f = lambda r: r * mp.tanh(mp.pi * r) * mp.e ** (-t * (mp.mpf(1) / 4 + r * r))
    return mp.quad(f, [-mp.inf, 0, mp.inf]) / (4 * mp.pi)


for m in (2, 3, 5, 7, 12):
    for t in (1e-3, 0.05, 0.5, 2.0, 10.0):
        e = E_m(m, t)
        check(0 < e <= mp.mpf(m * m - 1) / (12 * m), "E_m bound m=%d t=%g" % (m, t))
for t in (1e-3, 0.05, 0.5, 2.0, 10.0):
    i = I_over_area(t)
    check(0 < i <= mp.e ** (-t / 4) / (4 * mp.pi * t), "I bound t=%g" % t)
print("eig:elem(ii) OK (csc^2 identity m<60, b_0, beta integral, E_m and I by quadrature)")

# ---------- eig:counttail on synthetic spectra
for trial in range(300):
    lam = sorted([0.0] + [random.expovariate(0.3) for _ in range(random.randint(1, 300))])
    Z = lambda t: math.fsum(math.exp(-l * t) for l in lam)
    for x in (0.1, 1, 5, 20):
        check(sum(1 for l in lam if l <= x) <= math.e * Z(1 / x) + 1e-12, "counting")
    Lam = random.uniform(0.1, 20); t = random.uniform(0.01, 3); s = t * random.random()
    tail = math.fsum(math.exp(-l * t) for l in lam if l > Lam)
    check(tail <= math.exp(-Lam * (t - s)) * Z(s) + 1e-12, "tail")
    N = math.ceil(math.e * Z(1 / Lam))
    check(all(l > Lam for l in lam[N:]), "index statement")
print("eig:counttail OK on 300 synthetic spectra")

# ---------- eig:hypall: the two elementary steps
# (a) sup_x x e^{3x/2} g_t(x) <= e^{17t/4 - 1/2}/sqrt(pi), with g_t(x) = e^{-t/4} e^{-x^2/4t}/sqrt(4 pi t)
worst = 0
for t in [10 ** k for k in mp.linspace(-4, 1.5, 120)]:
    t = mp.mpf(t)
    def F(x):
        return x * mp.e ** (1.5 * x) * mp.e ** (-t / 4) * mp.e ** (-x * x / (4 * t)) / mp.sqrt(4 * mp.pi * t)
    # maximiser of x e^{3x/2 - x^2/4t}: x^2/(2t) - 3x/2 - 1 = 0
    xs = (mp.mpf(3) / 2 + mp.sqrt(mp.mpf(9) / 4 + 2 / t)) * t
    val = max(F(xs), F(xs * 0.999), F(xs * 1.001))
    bound = mp.e ** (17 * t / 4 - mp.mpf(1) / 2) / mp.sqrt(mp.pi)
    check(val <= bound * (1 + mp.mpf(10) ** -20), "hypall maximisation t=%s" % t)
    worst = max(worst, val / bound)
# (b) sum over classes of e^{-2 len} <= 2 K e^{-ell} for any counting function n <= K e^x, n=0 below ell
for trial in range(200):
    K = random.uniform(0.5, 50); ell = random.uniform(0.05, 3)
    # extremal step function n(x) = floor(K e^x) for x >= ell: jumps at log(j/K)
    j0 = math.floor(K * math.exp(ell))
    tot = j0 * math.exp(-2 * ell) + math.fsum(math.exp(-2 * math.log(j / K)) for j in range(j0 + 1, j0 + 200000))
    tot += K * K / (j0 + 200000)        # tail of sum_j (K/j)^2
    check(tot <= 2 * K * math.exp(-ell) * (1 + 1e-9), "Stieltjes step")
print("eig:hypall OK: max ratio sup/bound = %s (equality approached as t->0? no: <1)" % mp.nstr(worst, 6))

# ---------- lem:hypbound monotonicity in ell (Section A input, used in eig:count)
def logB(ell, t):
    return (mp.log(ell) + ell / 2 - mp.log(1 - mp.e ** (-ell)) + mp.log(1 + 2 * t / (ell - t))
            - ell ** 2 / (4 * t))
nmono = 0
for ell in mp.linspace(0.01, 8, 160):
    tmax = ell ** 2 / (2 * (1 + ell))
    for f in (0.01, 0.2, 0.5, 0.9, 1.0):
        t = tmax * f
        dl = mp.diff(lambda e: logB(e, t), ell)
        check(dl < 0, "B not decreasing in ell at ell=%s t=%s" % (ell, t))
        nmono += 1
# eps -> eps^2/(2(1+eps)) increasing
e = sp.symbols('e', positive=True)
check(sp.simplify(sp.diff(e ** 2 / (2 * (1 + e)), e) - e * (e + 2) / (2 * (1 + e) ** 2)) == 0, "deriv")
print("lem:hypbound monotonicity in ell OK on %d grid points" % nmono)

# ---------- eig:count constants (exact)
D, eps = sp.symbols('D epsilon', positive=True)
A21 = sp.pi / 21
case1 = sp.pi * sp.exp(3 * D) * eps * sp.exp(eps / 2) / (A21 * (1 - sp.exp(-eps)))
check(sp.simplify(case1 - 21 * sp.exp(3 * D) * eps * sp.exp(eps / 2) / (1 - sp.exp(-eps))) == 0, "21")
case2 = 2 * sp.sqrt(sp.pi) * sp.exp(3 * D) / (A21 * (1 - sp.exp(-eps)))
check(sp.simplify(case2 - 42 * sp.exp(3 * D) / (sp.sqrt(sp.pi) * (1 - sp.exp(-eps)))) == 0, "42")
# b_0 increasing in m and n <= floor(A/pi)+4
for m in range(2, 500):
    check(Fraction(m * m - 1, 12 * m) < Fraction((m + 1) ** 2 - 1, 12 * (m + 1)), "b0 increasing")
print("eig:count constants OK (21, 42/sqrt(pi), b_0 increasing)")

# ---------- eig:diam closed form: 4 r0 A / v0 <= (A/pi) max(4M,M^2) max(4/eps, 10M/3)
def ratio(epsv, M):
    x = mp.acosh(1 + 2 / (mp.pi ** 2 * M ** 2))
    d0 = min(epsv / 2, x); r0 = d0 / 2
    rho1 = mp.asinh(mp.sinh(r0) * mp.sin(mp.pi / M))
    v0 = 2 * mp.pi * min((mp.cosh(r0) - 1) / M, mp.cosh(rho1) - 1)
    lhs = 4 * r0 / v0
    rhs = max(4 * M, M * M) * max(4 / epsv, mp.mpf(10) * M / 3) / mp.pi
    return lhs / rhs
worst = 0; arg = None
for M in list(range(2, 60)) + [100, 1000, 10 ** 4, 10 ** 6]:
    for epsv in [mp.mpf(10) ** k for k in mp.linspace(-6, 2, 81)]:
        r = ratio(epsv, M)
        check(r <= 1, "closed form fails M=%d eps=%s ratio %s" % (M, epsv, r))
        if r > worst:
            worst, arg = r, (M, epsv)
print("eig:diam closed form OK; max ratio (exact D)/(closed form) = %s at M=%d eps=%s"
      % (mp.nstr(worst, 8), arg[0], mp.nstr(arg[1], 5)))
print("elem_count OK")
