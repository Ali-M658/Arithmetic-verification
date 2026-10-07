"""Recompute the explicit constants of Lemma eig:gap and Theorem eig:E for a class (A, eps, M),
check every inequality of the proof chain (re-derived independently, see REPORT.md), and test the
gap lemma by quadrature of the trace-formula integrals of thm:IEH at t_1 and t_*.
Usage: python theorem_e.py A_over_pi eps M [quad]"""
import sys, itertools
from fractions import Fraction as F
from math import lcm, factorial
import mpmath as mp
from heat import *

import os
mp.mp.dps = int(os.environ.get("DPS", "60"))


def mf(x):
    if isinstance(x, F):
        return mp.mpf(x.numerator) / x.denominator
    return mp.mpf(x)
A_pi = F(sys.argv[1]) if len(sys.argv) > 1 else F(1, 2)
eps = mf(sys.argv[2]) if len(sys.argv) > 2 else mf('1.86')
M = int(sys.argv[3]) if len(sys.argv) > 3 else 12
QUAD = len(sys.argv) > 4 and sys.argv[4] == 'quad'
A = mp.pi * mf(A_pi.numerator) / A_pi.denominator
pi = mp.pi


def check(cond, msg):
    if not cond:
        raise SystemExit("FAIL: " + msg)


# ---------- Theorem eig:diam
d0 = min(eps / 2, mp.acosh(1 + 2 / (pi ** 2 * M ** 2)))
r0 = d0 / 2
rho1 = mp.asinh(mp.sinh(r0) * mp.sin(pi / M))
v0 = 2 * pi * min((mp.cosh(r0) - 1) / M, mp.cosh(rho1) - 1)
D = 4 * r0 * A / v0
Dsimple = A / pi * max(4 * M, M ** 2) * max(4 / eps, mf(10) * M / 3)
check(D <= Dsimple, "D <= simple bound")

# ---------- constants of Section C Group 3
nstar = int(mp.floor(A / pi)) + 4
kstar = nstar
LM = lcm(*range(1, M + 1))
delta_k = {1: F(1, 2 * LM)}
for k in range(2, kstar + 1):
    delta_k[k] = a_lead(k - 2)
gamma_star = min(delta_k.values())


def phi(k, m):
    return m_phi(k, m) / m


def gk(k, m):
    return (-1) ** k * F(factorial(2 * k), factorial(k) * 4 ** k) * phi(k, m)


def mu(k):
    return (1 - F(1, 2 ** (2 * k + 1))) * abs(bern(2 * k + 2)) / (k + 1)


def Qcone(m, K, t):
    t = mf(t)
    s = mf(abs(gk(K, m)))
    s += mp.e ** (t / 4) * sum(mf(abs(gk(k, m)) * F(4) ** (k - K) / factorial(K - k)) for k in range(K))
    return s


def Qarea(K, t):
    t = mf(t)
    s = mf(F(1, 4 ** (K + 1) * factorial(K + 1)) + mu(K) / factorial(K))
    s += mp.e ** (t / 4) * sum(mf(mu(k) * F(4) ** (k - K) / (factorial(k) * factorial(K - k))) for k in range(K))
    return s


# check mu_k against its integral definition, and phi_k monotone in m, for a few k
for k in range(4):
    I = 4 * mp.quad(lambda r: r ** (2 * k + 1) / (mp.e ** (2 * pi * r) + 1), [0, mp.inf])
    check(abs(I - mf(mu(k))) < mf(10) ** -40, "mu_k")
    for m in range(2, M):
        check(phi(k, m) <= phi(k, m + 1), "phi monotone")


def Q(K):
    return A / (4 * pi) * Qarea(K, 1) + nstar * Qcone(M, K, 1)


t1 = min([mf(1)] + [mf(delta_k[k]) / (4 * Q(k - 1)) for k in range(1, kstar + 1)])
argt1 = min(range(1, kstar + 1), key=lambda k: mf(delta_k[k]) / (4 * Q(k - 1)))


def Gamma(t):
    return mf(gamma_star) / 2 * t ** (kstar - 2)


t2 = eps ** 2 / (2 * (1 + eps))
p = kstar - mf(3) / 2
varpi = 63 * eps * mp.e ** (eps / 2) / ((1 - mp.e ** (-eps)) * mp.sqrt(4 * pi))
y0 = 2 * (3 * D + mp.log(16 * varpi / mf(gamma_star)) + p * mp.log(4 / eps ** 2) + p * mp.log(2 * p / mp.e))
t3 = eps ** 2 / (4 * max(y0, 1))
tstar = min(t1, t2, t3)
Gs = Gamma(tstar)


def Zb(s):
    return A / (4 * pi * s) + nstar * mf(M * M - 1) / (12 * M) + 1


Lam = 2 / tstar * mp.log(8 * Zb(tstar / 2) / Gs)
N = int(mp.floor(mp.e * Zb(1 / Lam))) + 1
delta = min(1 / tstar, Gs / (8 * mp.e * N * tstar))


def logBstar(t):  # log of varpi e^{3D} t^{-1/2} e^{-eps^2/4t}
    return mp.log(varpi) + 3 * D - mp.log(t) / 2 - eps ** 2 / (4 * t)


def logBexact(t, ell, diam, area):  # lem:hypbound B(ell,diam,t), log
    return (mp.log(pi) + 3 * diam + mp.log(ell) + ell / 2 - mp.log(area) - mp.log(1 - mp.e ** (-ell))
            + mp.log(1 + 2 * t / (ell - t)) - ell ** 2 / (4 * t) - mp.log(mp.sqrt(4 * pi * t)))


print(f"class: A = {A_pi}*pi, eps = {mp.nstr(eps, 6)}, M = {M}")
print(f"  d0={mp.nstr(d0, 8)} r0={mp.nstr(r0, 8)} v0={mp.nstr(v0, 8)} D={mp.nstr(D, 10)} (simple bound {mp.nstr(Dsimple, 6)})")
print(f"  n*=k*={kstar}, L_M={LM}, delta_k={ {k: str(v) for k, v in delta_k.items()} }, gamma*={gamma_star}")
print(f"  Q(K), K=0..{kstar-1}: {[mp.nstr(Q(K), 8) for K in range(kstar)]}")
print(f"  t1={mp.nstr(t1, 10)} (attained at k={argt1})  t2={mp.nstr(t2, 10)}  t3={mp.nstr(t3, 10)}  y0={mp.nstr(y0, 10)}")
print(f"  t*={mp.nstr(tstar, 10)}  Gamma*={mp.nstr(Gs, 10)}  p={p}  varpi={mp.nstr(varpi, 10)}")
print(f"  Lambda={mp.nstr(Lam, 10)}  N={N}  delta={mp.nstr(delta, 10)}")

# ---------- the chain
check(t1 <= 1 and tstar <= t1 and tstar <= t2 and tstar <= t3, "t ordering")
check(t2 < eps / 2, "t2 < eps/2 so 1+2t/(eps-t) <= 3")
check(3 * 21 == 63, "")
# B(ell,diam,t) <= B_*(t) for ell>=eps, diam<D, Area>=pi/21, t<=t2 (sampled, ell up to 3 eps)
for ell in [eps, eps * 1.1, eps * 2, eps * 3]:
    for t in [tstar, tstar / 2, t2, t2 / 3]:
        check(logBexact(t, ell, D, pi / 21) <= logBstar(t) + mf(10) ** -30, "B <= B_*")
# B_*(t*) <= Gamma*/8
lhs, rhs = logBstar(tstar), mp.log(Gs / 8)
print(f"  log B*(t*) = {mp.nstr(lhs, 12)}  log(Gamma*/8) = {mp.nstr(rhs, 12)}  slack = {mp.nstr(rhs - lhs, 6)}")
check(lhs <= rhs, "B*(t*) <= Gamma*/8")
# the elementary inequality p log y <= y/2 + p log(2p/e) at y = eps^2/(4 t*)
y = eps ** 2 / (4 * tstar)
check(p * mp.log(y) <= y / 2 + p * mp.log(2 * p / mp.e), "p log y <= y/2 + p log(2p/e)")
# monotonicity of B_* on (0, t2]: derivative sign of -log t/2 - eps^2/4t is + iff t < eps^2/2
check(t2 < eps ** 2 / 2, "B_* increasing on (0,t2]")
check(1 / Lam < tstar, "1/Lambda < t*")
check(Gs / 8 <= 1, "Gamma*/8 <= 1 so Hyp <= 1 at s <= t*")
for s in [tstar / 2, 1 / Lam]:
    check(logBstar(s) <= logBstar(tstar), "B_* monotone")
# tail
tail = mp.e ** (-Lam * (tstar - tstar / 2)) * Zb(tstar / 2)
check(abs(tail - Gs / 8) <= Gs * mf(10) ** -30, "tail = Gamma*/8")
check(N > mp.e * Zb(1 / Lam), "N > e Zb(1/Lambda)")
pert = mp.e ** (delta * tstar) * N * tstar * delta
check(delta * tstar <= 1 and pert <= Gs / 8 * (1 + mf(10) ** -40), "perturbation <= Gamma*/8")
check(3 * Gs / 8 < Gs - 3 * Gs / 8, "3/8 < 5/8")
print("  chain of Theorem E verified")

# ---------- enumerate Sig(A, M)
sigs = []
for g in range(0, nstar):
    for n in range(0, nstar + 1):
        for ms in itertools.combinations_with_replacement(range(2, M + 1), n):
            x = -chi(g, ms)
            if 0 < x and 2 * x <= A_pi:
                sigs.append((g, ms))
print(f"  |Sig(A,M)| = {len(sigs)}")
check(all(len(ms) + 4 * g <= A_pi + 4 for g, ms in sigs), "n+4g <= A/pi+4")

if QUAD and len(sigs) >= 2:
    def Iint(t, area):  # (Area/4pi) int r tanh(pi r) h_t = (Area/4pi) e^{-t/4} (1/t - 4 int_0^inf r e^{-tr^2}/(e^{2pi r}+1))
        J = mp.quad(lambda r: r * mp.e ** (-t * r * r) / (mp.e ** (2 * pi * r) + 1), [0, 1, 4, 12, mp.inf])
        return area / (4 * pi) * mp.e ** (-t / 4) * (1 / t - 4 * J)

    def Em(t, m):
        tot = 0
        for j in range(1, m):
            th = pi * j / m
            f = lambda r: mp.e ** (-2 * th * r) * mp.e ** (-t * (mf(1) / 4 + r * r)) / (1 + mp.e ** (-2 * pi * r))
            tot += mp.quad(f, [-mp.inf, -12, -4, -1, 0, 1, 4, 12, mp.inf]) / (2 * m * mp.sin(th))
        return tot

    for t in sorted(set([tstar, t1, t1 / 10, min(1, 10 * t1)])):
        Ecache = {m: Em(t, m) for m in range(2, M + 1)}
        G = {s: Iint(t, -2 * pi * mf(chi(*s).numerator) / chi(*s).denominator) + sum(Ecache[m] for m in s[1]) for s in sigs}
        # remainder sanity (Group 2 input, eig:Grem) at K = 0..kstar-1 if t<=1
        worst_rem = mp.inf
        for s in sigs:
            c = c_vec(*s, kstar + 1)
            area = -2 * pi * mf(chi(*s).numerator) / chi(*s).denominator
            for K in range(kstar):
                approx = sum(mf(c[j - 1]) * t ** (j - 2) for j in range(1, K + 2))
                bnd = t ** K * (area / (4 * pi) * Qarea(K, 1) + sum(Qcone(m, K, 1) for m in s[1]))
                if t <= 1:
                    check(abs(G[s] - approx) <= bnd, f"Grem at t={t} K={K} {s}")
                    worst_rem = min(worst_rem, bnd / max(abs(G[s] - approx), mf(10) ** -55))
        ming, arg = mp.inf, None
        for s1, s2 in itertools.combinations(sigs, 2):
            gap = abs(G[s1] - G[s2])
            if gap < ming:
                ming, arg = gap, (s1, s2)
        ratio = ming / Gamma(t)
        print(f"  t={mp.nstr(t, 8)}: min pairwise |G-G'| = {mp.nstr(ming, 8)} at {arg}; Gamma(t)={mp.nstr(Gamma(t), 8)}; ratio={mp.nstr(ratio, 8)}; Grem slack factor >= {mp.nstr(worst_rem, 4)}")
        if t <= t1:
            check(ming >= Gamma(t), "gap lemma")
        # decision rule with worst-case adversarial error |e| = 3Gamma*/8 (only meaningful at t = t*)
        if t == tstar:
            for s in sigs:
                for sgn in (+1, -1):
                    S = G[s] + sgn * mf(3) / 8 * Gs
                    best = min(sigs, key=lambda u: abs(S - G[u]))
                    check(best == s, f"decision rule {s}")
            print("  decision rule recovers every sigma in Sig(A,M) under adversarial error 3Gamma*/8")
print("theorem_e OK")
