"""Theorem 6.2 with a computed gap (eigen paper, Corollary after Theorem 6.2).

    python3 theory/eigen/computed_gap.py          (about a minute)

The proof of Theorem 6.2 uses Lemma 6.1 only to bound the gap Theta = min_{sigma != sigma'} |G_sigma(t) - G_sigma'(t)|
over the finite set Sig(A, M) at the time t_*.  Any time t <= t_2 and any lower bound Theta <= 8 for that gap with
B_*(t) <= Theta/8 and Lambda t >= 1 give the conclusion of the theorem with the same formulas for Lambda, N and
delta.  This script evaluates the gap directly (G_sigma by the Gauss-Legendre quadrature of practice.py, checked
against 30-digit mpmath there; floating point, not certified) on a grid of times, for the classes of Table 3 whose
Sig(A, M) is small enough to enumerate, and reports the least N with its time and delta.  These numbers are
computed, not proved: a proof would need certified lower bounds for the gaps (interval quadrature).

Writes data/computed_gap.csv.
"""
import csv
import math
import os

import mpmath as mp
import numpy as np

from eigen_common import area_over_2pi, check, count_constant, signatures, theorem_E_constants, mpq
from practice import Gfun

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
CLASSES = [("pi/2", 1, 2, "1.8626", 8), ("pi/2", 1, 2, "1.8626", 12), ("4pi/3", 4, 3, "2.633915", 3),
           ("4pi/3", 4, 3, "0.693994", 3), ("4pi/3", 4, 3, "0.693994", 12), ("2pi", 2, 1, "0.1", 3)]


def main():
    G = Gfun()
    rows = []
    for Atxt, num, den, eps_txt, M in CLASSES:
        A_over_pi = mp.mpf(num) / den
        A = float(mp.pi * A_over_pi)
        eps = float(eps_txt)
        from fractions import Fraction as Fr
        S = signatures(Fr(num, den), M)
        aq = np.array([float(mpq(area_over_2pi(*x))) / 2 for x in S])
        nstar = int(math.floor(float(A_over_pi))) + 4
        C = float(count_constant(mp.pi * A_over_pi, mp.mpf(eps_txt), M))
        varpi = 3 * C * eps * math.exp(eps / 2) / ((1 - math.exp(-eps)) * math.sqrt(4 * math.pi))
        t2 = eps ** 2 / (2 * (1 + eps))
        T = np.geomspace(1e-7, t2, 480)
        G.prepare(T)
        best = None
        for t in T:
            Gv = np.array([G.G(sig, a, t) for sig, a in zip(S, aq)])
            gv = np.sort(Gv)
            Theta = float(min(np.min(np.diff(gv)), 8.0))
            if Theta <= 0:
                continue
            Bstar = varpi * math.exp(-eps ** 2 / (4 * t)) / math.sqrt(t)
            if Bstar > Theta / 8:
                continue

            def Zs(s):
                return A / (4 * math.pi * s) + nstar * (M * M - 1) / (12 * M) + 1

            Lam = (2 / t) * math.log(8 * Zs(t / 2) / Theta)
            if Lam * t < 1:
                continue
            N = int(math.floor(math.e * Zs(1 / Lam))) + 1
            delta = Theta / (8 * math.e * N * t)
            if best is None or N < best[0]:
                best = (N, t, Theta, delta, Lam)
        check(best is not None, f"{Atxt}, {eps_txt}, {M}: some admissible time")
        th = theorem_E_constants(mp.pi * A_over_pi, mp.mpf(eps_txt), M)
        N, t, Theta, delta, Lam = best
        print(f"A={Atxt} eps={eps_txt} M={M}: |Sig| = {len(S)}; computed gap {Theta:.3g} at t = {t:.4g}: N = {N}, "
              f"delta = {delta:.3g}  (Theorem 6.2: N = {th['N']}, delta = {mp.nstr(th['delta'], 3)})", flush=True)
        rows.append([Atxt, eps_txt, M, len(S), f"{t:.5g}", f"{Theta:.4g}", N, f"{delta:.4g}", th["N"], mp.nstr(th["delta"], 4)])
    with open(os.path.join(DATA, "computed_gap.csv"), "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["A", "eps", "M", "Sig_size", "t", "computed_gap", "N", "delta", "N_thm62", "delta_thm62"])
        w.writerows(rows)
    print("wrote data/computed_gap.csv")


if __name__ == "__main__":
    main()
