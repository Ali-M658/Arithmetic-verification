"""Task 4: Theorem E (finitely many approximate eigenvalues determine the signature).

Checks (asserts; nonzero exit on failure):
 1. Lemma E1 (integrality of the first difference), exhaustively and exactly: for every pair of
    distinct signatures of equal area in S(A, M) for (A/pi, M) in {(4, 10), (2, 30), (6, 6)}, the
    first differing heat invariant has index k <= min(floor(Area/pi) + 4, M) (the second bound is part
    (i) of the theorem on bounded cone orders, theory/msep/proof.tex), and d_k / a_{k-2,k-1} is a
    nonzero integer, divisible by prod_{p prime, (p-1) | 2(k-2)} p when k >= 3 (a divisibility the
    eigen paper does not use).
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
        kbound = min(floor(area_over_pi) + 4, M)
        for i in range(len(members)):
            for j in range(i):
                a, b = data[members[i]], data[members[j]]
                k = next((k for k in range(1, kmax + 1) if a[k - 1] != b[k - 1]), None)
                check(k is not None and k <= kbound, f"first difference beyond min(floor(Area/pi)+4, M): {members[i]} {members[j]}")
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
        # Remark 6.3(a) (round 7): in these classes no two signatures first differ beyond k = 3 (different areas
        # differ at k = 1)
        check(max(kdist) <= 3, f"A/pi<={A_over_pi}, M={M}: a first difference beyond k = 3")
        out.append(f"E1: A/pi<={A_over_pi}, M={M}: {n} signatures, {npairs} equal-area pairs; first differing index k: {kdist};"
                   f" least |d_k|/a_(k-2) = {minratio}")
    for A_over_pi, M in ((Fr(1, 2), 12), (Fr(4, 3), 6), (2, 5)):
        n, res = lemma_E2(A_over_pi, M)
        for t, mg, Gam in res:
            out.append(f"E2: A/pi<={A_over_pi}, M={M}: {n} signatures; t={mp.nstr(t, 4)}: least gap {mp.nstr(mg, 4)} >= Gamma {mp.nstr(Gam, 4)} (ratio {mp.nstr(mg / Gam, 4)})")
    out.append("\nTheorem E constants (eps = lower bound on the systole):")
    out.append("  A, eps, M | k_*, gamma_*, t_1, t_2, t_3, D | t*, Gamma, Lambda | N, delta")
    for A, eps, M in ((mp.pi / 2, mp.mpf('1.8626'), 12), (mp.pi / 2, mp.mpf('1.8626'), 8),
                      (4 * mp.pi / 3, mp.mpf('0.693994'), 3), (4 * mp.pi / 3, mp.mpf('2.633915'), 3),
                      (4 * mp.pi / 3, mp.mpf('0.693994'), 12), (2 * mp.pi, 1, 3), (2 * mp.pi, mp.mpf('0.1'), 3),
                      (10 * mp.pi, 1, 3), (10 * mp.pi, 1, 12)):
        c = theorem_E_constants(A, eps, M)
        # Remark 6.3(a) (round 7): the minimum defining t_1 is attained at k = k_*
        dm = {1: Fr(1, 2 * c["LM"])}
        dm.update({k: lead_coef(k - 2) for k in range(2, c["kstar"] + 1)})
        terms = {k: mpq(dm[k]) / (4 * c["Q"][k - 1]) for k in dm}
        check(min(terms, key=lambda k: terms[k]) == c["kstar"] and terms[c["kstar"]] < 1, "t_1 attained at k = k_*")
        # the chain: B_*(t*) <= Gamma/8 is asserted inside; tail: e^{-Lam t*/2} Zb(t*/2) = Gamma/8
        tail = mp.e ** (-c["Lambda"] * c["tstar"] / 2) * c["Zb_half"]
        check(tail <= c["Gamma"] / 8 * (1 + mp.mpf(10) ** -20), "tail <= Gamma/8")
        pert = c["N"] * c["tstar"] * c["delta"] * mp.e ** (c["tstar"] * c["delta"])
        check(pert <= c["Gamma"] / 8, "perturbation <= Gamma/8")
        check(c["Bstar_tstar"] + tail + pert < c["Gamma"] / 2, "total error < Gamma/2")
        out.append(f"  {mp.nstr(A, 5)}, {mp.nstr(eps, 4)}, {M} | {c['kstar']}, {c['gamma']}, {mp.nstr(c['t1'], 3)}, {mp.nstr(c['t2'], 3)},"
                   f" {mp.nstr(c['t3'], 3)}, {mp.nstr(c['D'], 4)} | {mp.nstr(c['tstar'], 3)}, {mp.nstr(c['Gamma'], 3)},"
                   f" {mp.nstr(c['Lambda'], 3)} | {mp.nstr(mp.mpf(c['N']), 4)}, {mp.nstr(c['delta'], 3)}")
    # growth of N as eps -> 0 (A, M fixed): roughly eps^-2 log(1/eps)^2 once t_3 < t_1 (count constant K ~ eps^-4)
    out.append("\nGrowth in eps (A = pi/2, M = 7): eps, binding constraint, N, N(eps)/N(2 eps)")
    prev, prev_bind = None, None
    for eps in (mp.mpf('0.04'), mp.mpf('0.02'), mp.mpf('0.01'), mp.mpf('0.005'), mp.mpf('0.0025')):
        c = theorem_E_constants(mp.pi / 2, eps, 7)
        bind = "t_3" if c["t3"] < c["t1"] else "t_1"
        ratio = "" if prev is None else mp.nstr(mp.mpf(c["N"]) / prev, 4)
        if prev is not None and bind == "t_3" and prev_bind == "t_3":
            check(4 < mp.mpf(c["N"]) / prev < 6, "N grows roughly like eps^-2 log(1/eps)^2 (ratio about 5 per halving, towards 4)")
        out.append(f"  {mp.nstr(eps, 3)}, {bind}, {mp.nstr(mp.mpf(c['N']), 4)}, {ratio}")
        prev, prev_bind = mp.mpf(c["N"]), bind
    # round 8: the class of the text (A = 4 pi/3, M = 3): t_3 binds from eps = 0.44 down (not at 0.45), and from
    # eps = 0.42 the factor per halving of eps falls from 5.24 to below 4.7; and pi e^{3D}/A over the rows of Table 3
    from eigen_common import diam_bound
    c45 = theorem_E_constants(4 * mp.pi / 3, mp.mpf('0.45'), 3)
    c44 = theorem_E_constants(4 * mp.pi / 3, mp.mpf('0.44'), 3)
    check(c45["t3"] >= c45["t1"] and c44["t3"] < c44["t1"], "t_3 binds from eps = 0.44")
    prev, ratios = None, []
    for k in range(8):
        c = theorem_E_constants(4 * mp.pi / 3, mp.mpf('0.42') / 2 ** k, 3)
        check(c["t3"] < c["t1"], "t_3 binds")
        if prev is not None:
            ratios.append(mp.mpf(c["N"]) / prev)
        prev = mp.mpf(c["N"])
    check(all(a > b for a, b in zip(ratios, ratios[1:])) and 5.2 < ratios[0] < 5.3 and 4.6 < ratios[-1] < 4.7,
          "factor per halving decreasing from 5.24")
    out.append("\nA = 4pi/3, M = 3: t_3 binds from eps = 0.44; factors per halving from 0.42: "
               + ", ".join(mp.nstr(r, 3) for r in ratios))
    exps = []
    for (A, eps, M) in ((mp.pi / 2, '1.8626', 8), (mp.pi / 2, '1.8626', 12), (4 * mp.pi / 3, '2.633915', 3),
                        (4 * mp.pi / 3, '0.693994', 3), (4 * mp.pi / 3, '0.693994', 12), (2 * mp.pi, '0.1', 3),
                        (10 * mp.pi, '1', 3), (10 * mp.pi, '1', 12)):
        D = diam_bound(A, mp.mpf(eps), M)
        exps.append(mp.log10(mp.pi) + 3 * D * mp.log10(mp.e) - mp.log10(A))
    check(196.5 < min(exps) < 196.6 and 29325.3 < max(exps) < 29325.4, "pi e^{3D}/A between 3e196 and 2e29325")
    out.append(f"pi e^(3D)/A between 10^{mp.nstr(min(exps), 6)} and 10^{mp.nstr(max(exps), 8)}")
    # Remark 6.5(a): first differences beyond k = 3 at area 12 pi, (0;2^4,7^7) and (0;4^6,8^4) share c_1, c_2, c_3
    from eigen_common import heat_coeffs, area_over_2pi
    sa, sb = (0, (2,) * 4 + (7,) * 7), (0, (4,) * 6 + (8,) * 4)
    ca, cb = heat_coeffs(*sa, 4), heat_coeffs(*sb, 4)
    check(area_over_2pi(*sa) == area_over_2pi(*sb) == 6 and ca[:3] == cb[:3] and ca[3] != cb[3],
          "(0;2^4,7^7) and (0;4^6,8^4): area 12 pi, share c_1..c_3, differ at c_4")
    out.append("(0;2^4,7^7), (0;4^6,8^4): area 12 pi, first difference at c_4")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
