"""Task 4: Theorem E (finitely many approximate eigenvalues determine the signature).

Checks (asserts; nonzero exit on failure):
 1. Lemma E1 (integrality of the first difference), exhaustively and exactly: for every pair of
    distinct signatures of equal area in S(A, M) for (A/pi, M) in {(4, 10), (2, 30), (6, 6)}, the
    first differing heat invariant has index k <= floor(Area/pi) + 4, and
    d_k / a_{k-2,k-1} is a nonzero integer, divisible by prod_{p prime, (p-1) | 2(k-2)} p when k >= 3.
 2. Lemma E2 (the gap), numerically at 60 digits on whole classes: for (A/pi, M) in
    {(1/2, 12), (4/3, 6), (2, 5)}, every pair sigma != sigma' in S(A, M) has
    |G_sigma(t) - G_sigma'(t)| >= Gamma(t) = gamma_* t^{k_*-2}/2 at t = t_1 and at t = t_1/10.
 3. The chain of inequalities behind N and delta (B_*(t*) <= Gamma/8, tail, perturbation) for a
    table of classes, and the sizes of N and delta.
"""
import sys
from collections import defaultdict
from fractions import Fraction as Fr
from math import floor

import mpmath as mp

from eigen_common import (check, mpq, heat_coeffs, signatures, area_over_2pi, lead_coef, lcm_upto,
                          theorem_E_constants, elliptic_term, identity_term, Qcone, Qarea)


mp.mp.dps = 40


def primes_upto(n):
    return [p for p in range(2, n + 1) if all(p % q for q in range(2, int(p ** 0.5) + 1))]


def fermat_factor(l):
    """prod of primes p with (p-1) | 2l (the denominator of B_{2l}, von Staudt-Clausen)."""
    f = 1
    for p in primes_upto(2 * l + 1):
        if (2 * l) % (p - 1) == 0:
            f *= p
    return f


def lemma_E1(A_over_pi, M):
    sigs = signatures(Fr(A_over_pi), M)
    kmax = floor(Fr(A_over_pi)) + 4
    groups = defaultdict(list)
    data = {}
    for g, orders in sigs:
        c = heat_coeffs(g, orders, kmax)
        data[(g, orders)] = c
        groups[c[0]].append((g, orders))
    npairs = 0
    kdist = defaultdict(int)
    minratio = None
    for c1, members in groups.items():
        area_over_pi = 4 * c1  # Area/pi = 4 c_1
        kbound = floor(area_over_pi) + 4
        for i in range(len(members)):
            for j in range(i):
                a, b = data[members[i]], data[members[j]]
                k = next((k for k in range(1, kmax + 1) if a[k - 1] != b[k - 1]), None)
                check(k is not None and k <= kbound, f"first difference beyond floor(Area/pi)+4: {members[i]} {members[j]}")
                d = a[k - 1] - b[k - 1]
                l = k - 2
                q = d / lead_coef(l)
                check(q.denominator == 1 and q != 0, f"d_k / a_l not a nonzero integer: {members[i]} {members[j]}")
                if l >= 1:
                    check(q.numerator % fermat_factor(l) == 0, "Fermat divisibility")
                npairs += 1
                kdist[k] += 1
                r = abs(q)
                minratio = r if minratio is None or r < minratio else minratio
    return len(sigs), npairs, dict(sorted(kdist.items())), minratio


def lemma_E2(A_over_pi, M):
    """Numerical check of |G_sigma - G_sigma'| >= Gamma(t) at t = t_1, t_1/10 over a whole class."""
    A = mp.pi * mpq(Fr(A_over_pi))
    c = theorem_E_constants(A, 1, M)  # eps does not enter t_1, gamma, Gamma(t)
    sigs = signatures(Fr(A_over_pi), M)
    res = []
    for t in (c["t1"], c["t1"] / 10):
        with mp.workdps(60):
            Em = {m: elliptic_term(m, t, dps=60) for m in range(2, M + 1)}
            Iunit = identity_term(4 * mp.pi, t, dps=60)  # A/(4 pi) = 1
            G = {}
            for g, orders in sigs:
                s = area_over_2pi(g, orders)
                G[(g, orders)] = mpq(s) / 2 * Iunit + mp.fsum(Em[m] for m in orders)
            vals = sorted(G.values())
            gaps = [vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
            mingap = min(gaps) if gaps else mp.inf
            Gam = mpq(c["gamma"]) * t ** (c["kstar"] - 2) / 2
            check(mingap >= Gam, f"gap lemma fails for A/pi={A_over_pi}, M={M}, t={t}")
            res.append((t, mingap, Gam))
    return len(sigs), res


def main():
    out = []
    for A_over_pi, M in ((4, 10), (2, 30), (6, 6)):
        n, npairs, kdist, minratio = lemma_E1(A_over_pi, M)
        out.append(f"E1: A/pi<={A_over_pi}, M={M}: {n} signatures, {npairs} equal-area pairs; first differing index k: {kdist};"
                   f" least |d_k|/a_(k-2) = {minratio}")
    for A_over_pi, M in ((Fr(1, 2), 12), (Fr(4, 3), 6), (2, 5)):
        n, res = lemma_E2(A_over_pi, M)
        for t, mg, Gam in res:
            out.append(f"E2: A/pi<={A_over_pi}, M={M}: {n} signatures; t={mp.nstr(t, 4)}: least gap {mp.nstr(mg, 4)} >= Gamma {mp.nstr(Gam, 4)} (ratio {mp.nstr(mg / Gam, 4)})")
    out.append("\nTheorem E constants (eps = lower bound on the systole):")
    out.append("  A, eps, M | k_*, gamma_*, t_1, t_2, t_3, D | t*, Gamma, Lambda | N, delta")
    for A, eps, M in ((mp.pi / 2, mp.mpf('1.8626'), 12), (mp.pi / 2, mp.mpf('1.8626'), 8),
                      (4 * mp.pi / 3, mp.mpf('0.694'), 3), (4 * mp.pi / 3, mp.mpf('2.634'), 3),
                      (4 * mp.pi / 3, mp.mpf('0.694'), 12), (2 * mp.pi, 1, 3), (2 * mp.pi, mp.mpf('0.1'), 3),
                      (10 * mp.pi, 1, 3), (10 * mp.pi, 1, 12)):
        c = theorem_E_constants(A, eps, M)
        # the chain: B_*(t*) <= Gamma/8 is asserted inside; tail: e^{-Lam t*/2} Zb(t*/2) = Gamma/8
        tail = mp.e ** (-c["Lambda"] * c["tstar"] / 2) * c["Zb_half"]
        check(tail <= c["Gamma"] / 8 * (1 + mp.mpf(10) ** -20), "tail <= Gamma/8")
        pert = c["N"] * c["tstar"] * c["delta"] * mp.e ** (c["tstar"] * c["delta"])
        check(pert <= c["Gamma"] / 8, "perturbation <= Gamma/8")
        check(c["Bstar_tstar"] + tail + pert < c["Gamma"] / 2, "total error < Gamma/2")
        out.append(f"  {mp.nstr(A, 5)}, {mp.nstr(eps, 4)}, {M} | {c['kstar']}, {c['gamma']}, {mp.nstr(c['t1'], 3)}, {mp.nstr(c['t2'], 3)},"
                   f" {mp.nstr(c['t3'], 3)}, {mp.nstr(c['D'], 4)} | {mp.nstr(c['tstar'], 3)}, {mp.nstr(c['Gamma'], 3)},"
                   f" {mp.nstr(c['Lambda'], 3)} | {mp.nstr(mp.mpf(c['N']), 4)}, {mp.nstr(c['delta'], 3)}")
    # growth of N as eps -> 0 (A, M fixed): roughly eps^-3 log(1/eps) once t_3 < t_1
    out.append("\nGrowth in eps (A = pi/2, M = 7): eps, binding constraint, N, N(eps)/N(2 eps)")
    prev = None
    for eps in (mp.mpf('0.04'), mp.mpf('0.02'), mp.mpf('0.01'), mp.mpf('0.005'), mp.mpf('0.0025')):
        c = theorem_E_constants(mp.pi / 2, eps, 7)
        bind = "t_3" if c["t3"] < c["t1"] else "t_1"
        ratio = "" if prev is None else mp.nstr(mp.mpf(c["N"]) / prev, 4)
        if prev is not None and bind == "t_3":
            check(6 < mp.mpf(c["N"]) / prev < 12, "N grows roughly like eps^-3 (ratio about 8 per halving)")
        out.append(f"  {mp.nstr(eps, 3)}, {bind}, {mp.nstr(mp.mpf(c['N']), 4)}, {ratio}")
        prev = mp.mpf(c["N"])
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
