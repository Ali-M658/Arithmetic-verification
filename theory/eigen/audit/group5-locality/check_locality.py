"""Independent checks for Theorem eig:loc (Group 5), written from STATEMENTS.md only.

Implements D(A,eps,M) (eig:diam), B and C (lem:hypbound, eq. Cconst) and checks:
  1. B(l,D,t) <= C(A,l,D) t^{-1/2} e^{-l^2/4t} on 0<t<=l^2/(2(1+l)), with equality at the endpoint;
     the ratio is exactly (l+t)/(l-t) * (2+l)/(2+3l) (symbolic).
  2. B increasing in diam (trivial) and decreasing in l' for l' >= l at fixed t in the l-range
     (symbolic bound on d log B / d l' plus numerical grid).
  3. t-range for the smaller systole is contained in the range of the larger one.
  4. D(A,eps,M) <= the stated crude bound; D >= the trivial lower bound arccosh(1+A/2pi) for diam;
     D(pi/3, sigma0, m) >= log(m/2pi) (Proposition eig:233 consistency).
  5. Degenerate inputs: no cone points (M=2), tiny / large l, t at the endpoint.
Every check raises on failure.
"""
import mpmath as mp
import sympy as sp

mp.mp.dps = 50


def d0(eps, M):
    return mp.mpf(min(mp.mpf(eps) / 2, mp.acosh(1 + 2 / (mp.pi**2 * M**2))))


def D(A, eps, M):
    r0 = d0(eps, M) / 2
    rho1 = mp.asinh(mp.sinh(r0) * mp.sin(mp.pi / M))
    v0 = 2 * mp.pi * min((mp.cosh(r0) - 1) / M, mp.cosh(rho1) - 1)
    return 4 * r0 * A / v0


def Dcrude(A, eps, M):
    return A / mp.pi * max(4 * M, M**2) * max(4 / mp.mpf(eps), mp.mpf(10) * M / 3)


def B(A, l, diam, t):
    l, t = mp.mpf(l), mp.mpf(t)
    return (mp.pi * mp.e**(3 * diam) * l * mp.e**(l / 2) / (A * (1 - mp.e**(-l)))
            * (1 + 2 * t / (l - t)) * mp.e**(-l**2 / (4 * t)) / mp.sqrt(4 * mp.pi * t))


def C(A, l, diam):
    l = mp.mpf(l)
    return (mp.sqrt(mp.pi) * mp.e**(3 * diam) * l * mp.e**(l / 2) * (2 + 3 * l)
            / (2 * A * (1 - mp.e**(-l)) * (2 + l)))


def tmax(l):
    l = mp.mpf(l)
    return l**2 / (2 * (1 + l))


def area(g, ms):
    return 2 * mp.pi * (2 * g - 2 + sum(1 - mp.mpf(1) / m for m in ms))


fails = []


def check(cond, msg):
    if not cond:
        fails.append(msg)
        raise AssertionError(msg)


# ---- 1. symbolic ratio B / (C t^-1/2 e^{-l^2/4t}) ----
l_, t_, A_, Dm = sp.symbols('ell t A Dm', positive=True)
Bs = (sp.pi * sp.exp(3 * Dm) * l_ * sp.exp(l_ / 2) / (A_ * (1 - sp.exp(-l_)))
      * (1 + 2 * t_ / (l_ - t_)) * sp.exp(-l_**2 / (4 * t_)) / sp.sqrt(4 * sp.pi * t_))
Cs = (sp.sqrt(sp.pi) * sp.exp(3 * Dm) * l_ * sp.exp(l_ / 2) * (2 + 3 * l_)
      / (2 * A_ * (1 - sp.exp(-l_)) * (2 + l_)))
ratio = sp.simplify(Bs / (Cs * t_**sp.Rational(-1, 2) * sp.exp(-l_**2 / (4 * t_))))
target = (l_ + t_) / (l_ - t_) * (2 + l_) / (2 + 3 * l_)
check(sp.simplify(ratio - target) == 0, "ratio formula")
tm = l_**2 / (2 * (1 + l_))
check(sp.simplify(target.subs(t_, tm) - 1) == 0, "ratio = 1 at endpoint")
check(sp.simplify(tm - l_ + l_ * (2 + l_) / (2 * (1 + l_))) == 0, "l - tmax = l(2+l)/(2(1+l)) > 0")
print("1. symbolic: B/(C t^-1/2 e^-l^2/4t) = (l+t)/(l-t)*(2+l)/(2+3l), increasing in t, =1 at tmax")

# ---- 2. monotonicity in l' at fixed t (symbolic upper bound for d/dl' log B) ----
lp = sp.symbols('lp', positive=True)
logB = (sp.log(lp) + lp / 2 - sp.log(1 - sp.exp(-lp)) + sp.log(lp + t_) - sp.log(lp - t_)
        - lp**2 / (4 * t_))
dlog = sp.diff(logB, lp)
# with lp/(2t) >= 1/lp + 1 (i.e. t <= lp^2/(2(1+lp))) the derivative is
# <= -1/2 - 1/(e^lp - 1) - 2t/(lp^2 - t^2) < 0
num_checked = 0
for l in [mp.mpf(x) for x in ['1e-3', '0.01', '0.1', '0.3', '0.5617', '1', '2', '3.0571', '5', '10', '30']]:
    T = tmax(l)
    for frac in [mp.mpf('1e-6'), mp.mpf('0.01'), mp.mpf('0.3'), mp.mpf('0.9'), mp.mpf(1)]:
        t = T * frac
        prev = None
        for k in range(0, 60):
            lpv = l * (1 + mp.mpf(k) / 10)
            check(t <= tmax(lpv) * (1 + mp.mpf('1e-40')), "range nesting")
            d = dlog.subs({lp: sp.Float(str(lpv), 40), t_: sp.Float(str(t), 40)})
            check(float(d) < 0, f"dlogB/dl >= 0 at l={l}, lp={lpv}, t={t}")
            b = B(1, lpv, 0, t)
            if prev is not None:
                check(b < prev, f"B not decreasing at l={l} lp={lpv} t={t}")
            prev = b
            num_checked += 1
print(f"2. B decreasing in l' >= l at fixed t in the l-range: {num_checked} points OK")

# ---- 3. inequality chain on grid, including D and degenerate cases ----
sigma0 = 2 * mp.asinh(1 / (2 * mp.sqrt(1 + mp.mpf(3) / 4 * mp.cosh(2 * mp.acosh(2 / mp.sqrt(3)))**2)))
sigs = [(2, []), (3, []), (0, [2, 3, 7]), (0, [2, 3, 1000]), (0, [2, 2, 2, 3]), (1, [2]),
        (0, [2, 2, 2, 2, 2]), (0, [7, 7, 7]), (5, [2, 50])]
for g, ms in sigs:
    A = area(g, ms)
    check(A > 0, "hyperbolic")
    M = max(ms) if ms else 2
    for l in [mp.mpf(x) for x in ['1e-4', '0.05', '0.3', str(sigma0), '1', '3.0571', '8']]:
        Dv = D(A, l, M)
        check(Dv <= Dcrude(A, l, M) * (1 + mp.mpf('1e-30')), f"D > crude bound {g},{ms},{l}")
        check(Dv >= mp.acosh(1 + A / (2 * mp.pi)), f"D below trivial diameter lower bound {g},{ms},{l}")
        for frac in [mp.mpf('1e-8'), mp.mpf('0.01'), mp.mpf('0.5'), mp.mpf(1)]:
            t = tmax(l) * frac
            lhs = B(A, l, Dv, t)
            rhs = C(A, l, Dv) * t**mp.mpf(-0.5) * mp.e**(-l**2 / (4 * t))
            check(lhs <= rhs * (1 + mp.mpf('1e-40')), f"B>C bound {g},{ms},{l},{frac}")
            if frac == 1:
                check(abs(lhs / rhs - 1) < mp.mpf('1e-40'), "equality at endpoint")
            # monotone in diam
            check(B(A, l, Dv * mp.mpf('0.9'), t) < lhs, "B increasing in diam")
print("3. chain B(l,D,t) <= C t^-1/2 e^-l^2/4t verified on signature x systole x t grid")

# ---- 4. eig:233 consistency and numbers ----
for m in [7, 8, 20, 100, 10**4]:
    Dv = D(mp.pi / 3, sigma0, m)
    check(Dv >= mp.log(m / (2 * mp.pi)), "D below 233 lower bound")
Ds = {}
for (g, ms, l) in [(2, [], mp.mpf('3.0571')), (0, [2, 3, 7], sigma0), (0, [2, 3, 7], mp.mpf('0.98')),
                   (2, [], mp.mpf('0.1'))]:
    A = area(g, ms)
    M = max(ms) if ms else 2
    Dv = D(A, l, M)
    Ds[(g, tuple(ms), float(l))] = (float(A), M, float(Dv), mp.nstr(C(A, l, Dv), 6))
for k, v in Ds.items():
    print("   sig/l", k, "-> A, M, D, C =", v)

# ---- 5. no cone points: M=2 vs uncapped surface radius ----
cap2 = mp.acosh(1 + 2 / (4 * mp.pi**2))
print("5. M=2 cap on d0 for surfaces: arccosh(1+1/(2pi^2)) =", mp.nstr(cap2, 8),
      "(so d0 <= this even when l/2 is larger)")
# D(A,eps,2) is non-increasing in eps
prev = None
for k in range(1, 200):
    e = mp.mpf(k) / 20
    v = D(4 * mp.pi, e, 2)
    if prev is not None:
        check(v <= prev * (1 + mp.mpf('1e-40')), "D not non-increasing in eps")
    prev = v
print("   D(4pi, eps, 2) non-increasing in eps on (0,10]; saturates at", mp.nstr(prev, 8))

print("ALL CHECKS PASSED" if not fails else fails)
