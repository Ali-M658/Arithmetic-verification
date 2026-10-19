"""Two checks of the a-posteriori test on the computed spectra of O(2,8,8) and O(3,3,12) (eigen paper, Section 7).

    python3 theory/eigen/practice_checks.py          (a few minutes; writes data/practice_checks.csv)

1. Robustness to the eigenvalue errors.  The least N for which criterion (C1) of Theorem 7.1 holds, with the
   instance inputs (Delta = 2 diam P), is recomputed with every error eps_j replaced by max(eps_j, r lambda~_j)
   for r = 1e-6, ..., 1e-2.  Asserted: the counts are those of the committed run for r <= 1e-3 (round 7: with the
   sharp perturbation term of Theorem 7.1).
2. Completeness against every signature.  At t = 0.0015 the trace of the whole computed list (Neumann and
   Dirichlet, about 2850 eigenvalues) is compared with G_sigma(t) for every sigma of area pi/2 with orders at
   most 12.  Asserted: it agrees with the true signature within the error budget 1.5e-11 of Section 7.1
   (eigenvalue errors with the factor e^{-(lambda-eps) t}, plus a Weyl-law estimate of the tail), and differs
   from every other signature by more than 10^6 times that budget.
"""
import csv
import math
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import practice as P  # noqa: E402
from eigen_common import check, area_over_2pi, mpq, signatures  # noqa: E402
import mpmath as mp  # noqa: E402

BUDGET = 1.5e-11
T_COMPLETE = 0.0015


def main():
    G = P.Gfun()
    inst = {r["orbifold"]: r for r in csv.DictReader(open(os.path.join(P.DATA, "instances.csv")))}
    committed = {(r["orbifold"], r["M"], r["diameter_input"], r["eps_j"], r["data"]): r
                 for r in csv.DictReader(open(os.path.join(P.DATA, "practice.csv")))}
    rows = []
    for name, pqr in (("O(2,8,8)", (2, 8, 8)), ("O(3,3,12)", (3, 3, 12))):
        sig = (0, pqr)
        spec = P.triangle_spectrum(pqr)
        I = inst[name]
        ell = float(I["systole_lower_bound"])
        Delta = float(I["diam_upper_B1_2diamP"])
        base = int(committed[(name, "12", "B1", "eps", "full")]["N_C1"])
        for r in (1e-6, 1e-5, 1e-4, 1e-3, 1e-2):
            sp = dict(spec)
            sp["eps"] = np.maximum(spec["eps"], r * spec["lam"])
            c = P.Case(name, sig, None, ell, 12, sp, Delta, "B1", "full", "eps", do_obs=False)
            o = c.run(G)
            n = o["C1"]["N"] if o["C1"] is not None else None
            rows.append([name, f"{r:g}", n if n is not None else f">{c.Nc - 1}", base])
            print(name, r, n, "committed", base, flush=True)
            if r <= 1e-3:
                check(n == base, f"{name}: count changes at relative error {r}")
        # completeness against every signature
        s = area_over_2pi(*sig)
        S = [x for x in signatures(2 * s, 12) if area_over_2pi(*x) == s]
        lam_all = np.array([x[0] for x in spec["rows"]])
        Z = float(np.sum(np.exp(-lam_all * T_COMPLETE)))
        Aq = float(mpq(s)) / 2
        G.prepare([T_COMPLETE])
        dev = {x: abs(Z - G.G(x, Aq, T_COMPLETE)) for x in S}
        true_dev = dev[sig]
        other = min(v for k, v in dev.items() if k != sig)
        print(name, "true", true_dev, "nearest other", other, flush=True)
        check(true_dev <= BUDGET, f"{name}: true signature outside the budget")
        check(other > 1e6 * BUDGET, f"{name}: another signature within 10^6 budgets")
        rows.append([name, "completeness", f"{true_dev:.2e}", f"{other:.2e}"])
    # how crude the closed-geodesic bound is (Section 7.2): for O(2,8,8) at t = 0.0562 the bound of Lemma 2.2(ii) with
    # the instance's diameter bound 2 diam P, against the hyperbolic term of the two classes at the systole
    # 2 arccosh(1 + cos(pi/4)) (the next length, 2.8816, adds less than 1e-14 there)
    from eigen_common import hyp_bound_small
    with mp.workdps(30):
        t = mp.mpf("0.0562")
        H = hyp_bound_small(t, mp.mpf("2.256767"), mp.mpf("4.897"), mp.pi / 2)
        L0 = 2 * mp.acosh(1 + mp.cos(mp.pi / 4))
        term = 2 * L0 / (2 * mp.sinh(L0 / 2)) * mp.e ** (-t / 4) * mp.e ** (-L0 ** 2 / (4 * t)) / mp.sqrt(4 * mp.pi * t)
        check(mp.mpf("6.7e-3") < H < mp.mpf("6.9e-3") and mp.mpf("2.7e-10") < term < mp.mpf("2.9e-10"), "bound vs term")
        check(mp.mpf("2e7") < H / term < mp.mpf("3e7"), "ratio of the closed-geodesic bound to the term")
        print(f"O(2,8,8), t = 0.0562: closed-geodesic bound {mp.nstr(H, 3)}, systole term {mp.nstr(term, 3)}, ratio {mp.nstr(H / term, 3)}")
    with open(os.path.join(P.DATA, "practice_checks.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["orbifold", "relative_error_or_check", "N_C1_or_true_deviation", "committed_N_or_nearest_other"])
        w.writerows(rows)
    print("wrote data/practice_checks.csv")


if __name__ == "__main__":
    main()
