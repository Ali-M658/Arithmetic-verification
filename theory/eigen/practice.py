"""Task 7: Theorem E in practice, on the committed spectra (read-only use of numerics/).

For a true orbifold O of signature sigma_0 and a competitor set S = {signatures of the same area,
orders <= M}, and a time t:
  gap(t)   = min_{sigma != sigma_0} |G_sigma(t) - G_sigma_0(t)|           (quadrature, 30 digits)
  Zt_N(t)  = sum_{j<N} e^{-lambda_j t}                                    (committed eigenvalues)
  N_obs(t) = least N such that |Zt_N'(t) - G_sigma_0(t)| < gap(t)/2 for every N' >= N up to the
             end of the complete range: the nearest-signature rule of Theorem E then returns sigma_0
             with the margin the theorem requires, judged against the data;
  N_apr(t) = least N with  HypB(t) + TailB(N, t) + PertB(N, t) < gap(t)/2, where
             HypB  = Lemma 2.5 with the systole and a committed upper bound for the diameter,
             TailB = min_s e^{-lambda_N (t-s)} (A/(4 pi s) + sum b_0 + HypB(s))   (Theorem C),
             PertB = sum_{j<N} t * err_j  (committed a-posteriori eigenvalue error estimates);
             this is the a-priori rule of Theorem E with the actual constants, valid modulo the
             a-posteriori error bars and the completeness of the computed spectrum below lambda_N.
The theoretical N of Theorem E for C(A, systole, M) is printed alongside.

Writes theory/eigen/data/practice.csv.  Asserts: the data load and are sorted; the merged sector
spectra of the (0;3,3,3,3) family agree with the committed first-400 orbifold lists; the rule
returns the true signature at the reported (t, N); every reported count lies inside the complete
range.
"""
import csv
import json
import math
import os
import sys
from fractions import Fraction as Fr

import mpmath as mp

from eigen_common import (check, mpq, signatures, area_over_2pi, elliptic_term, identity_term, b_cone,
                          load_triangle_spectrum, theorem_E_constants, hyp_bound_all)

mp.mp.dps = 30
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
TGRID = ['0.002', '0.003', '0.005', '0.0075', '0.01', '0.015', '0.02', '0.03', '0.05', '0.075',
         '0.1', '0.15', '0.2', '0.3', '0.5', '0.75', '1.0']


def B_lemma25(ell, diam, A, t):
    return (mp.pi * mp.e ** (3 * diam) * ell * mp.e ** (ell / 2) / (A * (1 - mp.e ** (-ell)))
            * (1 + 2 * t / (ell - t)) * mp.e ** (-ell ** 2 / (4 * t)) / mp.sqrt(4 * mp.pi * t))


def hypB(ell, diam, A, t):
    if t <= ell ** 2 / (2 * (1 + ell)):
        return B_lemma25(ell, diam, A, t)
    return hyp_bound_all(t, ell, diam, area_lb=A)


class Gcache:
    def __init__(self):
        self.E = {}
        self.I = {}

    def G(self, g, orders, t):
        key = t
        if key not in self.I:
            self.I[key] = identity_term(4 * mp.pi, mp.mpf(t))  # per unit Area/(4 pi)
        s = area_over_2pi(g, orders)
        tot = mpq(s) / 2 * self.I[key]
        for m in orders:
            if (m, t) not in self.E:
                self.E[(m, t)] = elliptic_term(m, mp.mpf(t))
            tot += self.E[(m, t)]
        return tot


def analyse(name, sig0, lam, err, lam_complete, ell, diam, M, cache, rows, out):
    g0, ord0 = sig0
    s = area_over_2pi(g0, ord0)
    A = 2 * mp.pi * mpq(s)
    comp = [x for x in signatures(2 * s, M) if area_over_2pi(*x) == s]
    check(sig0 in comp, "true signature in the competitor set")
    ncomp = len(comp)
    check(all(lam[i] <= lam[i + 1] for i in range(len(lam) - 1)), "sorted")
    Ncomplete = sum(1 for x in lam if x <= lam_complete)
    # the tail bound may not use the (unknown) true signature: bound E by b_0 summed over the cone
    # points, maximised over the competitor set (eigen paper, Corollary cert:post)
    cone0 = max(sum(mpq(b_cone(0, m)) for m in o) for (_, o) in comp)
    best_obs, best_apr = None, None
    for t in TGRID:
        tt = mp.mpf(t)
        G0 = cache.G(g0, ord0, t)
        others = [(abs(cache.G(g, o, t) - G0), (g, o)) for (g, o) in comp if (g, o) != sig0]
        gap, nearest = min(others)
        # observed
        terms = [math.exp(-x * float(tt)) for x in lam[:Ncomplete]]
        partial = []
        acc = 0.0
        comp_sum = 0.0  # Kahan
        for v in terms:
            y = v - comp_sum
            tmp = acc + y
            comp_sum = (tmp - acc) - y
            acc = tmp
            partial.append(acc)
        dev = [abs(mp.mpf(p) - G0) for p in partial]  # dev[N-1] for Zt_N
        Nobs = None
        ok_from = None
        for N in range(Ncomplete, 0, -1):
            if dev[N - 1] < gap / 2:
                ok_from = N
            else:
                break
        Nobs = ok_from
        # a priori
        hb = hypB(ell, diam, A, tt)
        Napr = None
        if hb < gap / 2:
            pert = mp.mpf(0)
            zb = [(tt * mp.mpf(k), A / (4 * mp.pi * tt * mp.mpf(k)) + cone0 + hypB(ell, diam, A, tt * mp.mpf(k)))
                  for k in ('0.2', '0.35', '0.5', '0.65', '0.8')]
            for N in range(1, Ncomplete):
                pert += tt * err[N - 1]
                lamN = mp.mpf(lam[N]) - err[N]
                best_tail = min(mp.e ** (-lamN * (tt - ss)) * z for ss, z in zb)
                if hb + best_tail + pert < gap / 2:
                    Napr = N
                    break
        if Nobs is not None:
            # the rule really returns sigma_0 at N_obs
            Zt = mp.mpf(partial[Nobs - 1])
            pick = min(comp, key=lambda x: abs(Zt - cache.G(x[0], x[1], t)))
            check(pick == sig0, "nearest-signature rule returns the truth at N_obs")
            check(Nobs <= Ncomplete, "inside the complete range")
        rows.append(dict(orbifold=name, M=M, competitors=ncomp, t=t, gap=mp.nstr(gap, 6), nearest=str(nearest),
                         hyp_bound=mp.nstr(hb, 4), N_obs=Nobs if Nobs is not None else "",
                         lambda_N_obs=f"{lam[Nobs - 1]:.4f}" if Nobs else "", N_apr=Napr if Napr is not None else "",
                         lambda_N_apr=f"{lam[Napr - 1]:.4f}" if Napr else ""))
        if Nobs is not None and (best_obs is None or Nobs < best_obs[0]):
            best_obs = (Nobs, t, nearest, gap)
        if Napr is not None and (best_apr is None or Napr < best_apr[0]):
            best_apr = (Napr, t, nearest, gap)
    th = theorem_E_constants(A, ell, M)
    out.append(dict(orbifold=name, M=M, competitors=ncomp, Ncomplete=Ncomplete, lam_complete=lam_complete,
                    best_obs=best_obs, best_apr=best_apr, N_theory=th["N"], delta_theory=th["delta"],
                    tstar=th["tstar"], ell=ell))


def triangle_diam_upper(pqr):
    A, B, C = (mp.pi / x for x in pqr)
    sides = [mp.acosh((mp.cos(C) + mp.cos(A) * mp.cos(B)) / (mp.sin(A) * mp.sin(B))),
             mp.acosh((mp.cos(B) + mp.cos(A) * mp.cos(C)) / (mp.sin(A) * mp.sin(C))),
             mp.acosh((mp.cos(A) + mp.cos(B) * mp.cos(C)) / (mp.sin(B) * mp.sin(C)))]
    return 2 * max(sides)


def moduli_spectra():
    rows = list(csv.DictReader(open(os.path.join(ROOT, "numerics", "moduli", "data", "eigenvalue_flow_sectors.csv"))))
    orb = list(csv.DictReader(open(os.path.join(ROOT, "numerics", "moduli", "data", "eigenvalue_flow_orbifold.csv"))))
    taus = sorted(set(r["tau"] for r in rows), key=float)
    res = {}
    for tau in taus:
        sec = {}
        for r in rows:
            if r["tau"] == tau:
                sec.setdefault(r["sector"], []).append((float(r["lambda"]), float(r["err_estimate"])))
        complete = min(max(x for x, _ in v) for v in sec.values())
        merged = sorted(x for v in sec.values() for x in v)
        ref = sorted(float(r["lambda"]) for r in orb if r["tau"] == tau)
        check(len(ref) == 400, "400 committed orbifold eigenvalues")
        for a, b in zip([x for x, _ in merged][:400], ref):
            check(abs(a - b) <= 1e-9 * max(1, b), "merged sectors = committed orbifold list")
        res[tau] = (merged, complete)
    return res


def main():
    out = []
    rows = []
    cache = Gcache()
    for pqr, ell in (((2, 8, 8), mp.mpf('2.256768')), ((3, 3, 12), mp.mpf('1.862604'))):
        spec, top = load_triangle_spectrum(pqr)
        lam = [x for x, _ in spec]
        err = [mp.mpf(e) for _, e in spec]
        lam_complete = 16000.0  # Section 7: no eigenvalue below about 1.6e4 is missing
        for M in (12, 30):
            analyse(f"O{pqr}", (0, pqr), lam, err, lam_complete, ell, triangle_diam_upper(pqr), M, cache, rows, out)
    geo = json.load(open(os.path.join(ROOT, "numerics", "moduli", "data", "geometries.json")))
    spec = moduli_spectra()
    for tau, (merged, complete) in spec.items():
        mem = geo["members"][tau]
        ell = mp.mpf(mem["systole"])
        diam = mp.mpf(mem["diam_O_upper_bound"])
        lam = [x for x, _ in merged]
        err = [mp.mpf(e) for _, e in merged]
        for M in (3, 12):
            analyse(f"(0;3,3,3,3) theta={tau}", (0, (3, 3, 3, 3)), lam, err, complete, ell, diam, M, cache, rows, out)
    os.makedirs(os.path.join(HERE, "data"), exist_ok=True)
    with open(os.path.join(HERE, "data", "practice.csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("orbifold | M | #competitors | complete range (N, lambda) | best N_obs (t, nearest) | best N_apr (t) | N_theory, delta_theory")
    for o in out:
        bo = o["best_obs"]
        ba = o["best_apr"]
        print(f"{o['orbifold']} | {o['M']} | {o['competitors']} | {o['Ncomplete']}, {o['lam_complete']:.0f} | "
              f"{bo[0] if bo else '-'} (t={bo[1] if bo else '-'}, vs {bo[2] if bo else '-'}) | "
              f"{ba[0] if ba else '-'} (t={ba[1] if ba else '-'}) | {mp.nstr(mp.mpf(o['N_theory']), 3)}, {mp.nstr(o['delta_theory'], 3)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
