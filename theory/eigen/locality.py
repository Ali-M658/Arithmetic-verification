"""Task 6: Theorem 4.4 with the diameter replaced by D(A, eps, M) (Theorem L).

Checks (asserts; nonzero exit on failure):
 1. For the eight members of the (0;3,3,3,3) family (numerics/moduli/data/geometries.json), the
    committed upper bound for the diameter is <= D(4 pi/3, systole, 3).
 2. For every pair of members and every committed t in the admissible range
    t <= l^2/(2(1+l)) (l = shorter systole), the predicted trace difference
    H_i - H_j (trace_differences.csv; its agreement with the measured difference is checked in
    numerics/moduli) is <= B(l, D(A, l, M), t) <= C(A, l, D(A, l, M)) t^{-1/2} e^{-l^2/4t},
    and the old bound with the actual diameter is <= the new one (B increases with the diameter).
 3. The size of the constants, old and new.
"""
import csv
import json
import os
import sys

import mpmath as mp

from eigen_common import check, diam_bound

mp.mp.dps = 30
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")


def B(ell, diam, A, t):
    """Lemma 2.5: B(ell, diam, t) with Area = A."""
    return (mp.pi * mp.e ** (3 * diam) * ell * mp.e ** (ell / 2) / (A * (1 - mp.e ** (-ell)))
            * (1 + 2 * t / (ell - t)) * mp.e ** (-ell ** 2 / (4 * t)) / mp.sqrt(4 * mp.pi * t))


def C(A, ell, diam):
    """eq. (Cconst)."""
    return (mp.sqrt(mp.pi) * mp.e ** (3 * diam) * ell * mp.e ** (ell / 2) * (2 + 3 * ell)
            / (2 * A * (1 - mp.e ** (-ell)) * (2 + ell)))


def main():
    out = []
    geo = json.load(open(os.path.join(ROOT, "numerics", "moduli", "data", "geometries.json")))
    A = mp.mpf(geo["area_orbifold"])
    check(abs(A - 4 * mp.pi / 3) < 1e-12, "area 4 pi/3")
    M = 3
    mem = geo["members"]
    sysl = {k: mp.mpf(v["systole"]) for k, v in mem.items()}
    diam = {k: mp.mpf(v["diam_O_upper_bound"]) for k, v in mem.items()}
    out.append("member: systole, committed diam upper bound, D(4pi/3, systole, 3), C old, C new")
    for k in sorted(mem, key=float):
        D = diam_bound(A, sysl[k], M)
        check(diam[k] <= D, f"diam <= D for member {k}")
        out.append(f"  theta={k}: {mp.nstr(sysl[k], 5)}, {mp.nstr(diam[k], 5)}, {mp.nstr(D, 5)}, "
                   f"{mp.nstr(C(A, sysl[k], diam[k]), 4)}, {mp.nstr(C(A, sysl[k], D), 4)}")
    rows = list(csv.DictReader(open(os.path.join(ROOT, "numerics", "moduli", "data", "trace_differences.csv"))))
    n = 0
    worst = 0
    for r in rows:
        i, j = r["tau_i"], r["tau_j"]
        t = mp.mpf(r["t"])
        ell = min(sysl[i], sysl[j])
        if t > ell ** 2 / (2 * (1 + ell)):
            continue
        dpred = abs(mp.mpf(r["D_predicted_Hi_minus_Hj"]))
        dmax = max(diam[i], diam[j])
        D = diam_bound(A, ell, M)
        bnew = B(ell, D, A, t)
        bold = B(ell, dmax, A, t)
        check(bold <= bnew, "old bound <= new bound")
        check(dpred <= bold, "difference <= old bound")
        check(bnew <= C(A, ell, D) * t ** mp.mpf(-0.5) * mp.e ** (-ell ** 2 / (4 * t)) * (1 + mp.mpf(10) ** -20), "B <= C t^-1/2 e^-l^2/4t")
        n += 1
        if dpred > 0:
            worst = max(worst, mp.log10(bnew / dpred))
    out.append(f"{n} (pair, t) rows in the admissible range: |H_i - H_j| <= B(l, diam, t) <= B(l, D(A,l,M), t) <= C(A,l,D) t^(-1/2) e^(-l^2/4t);"
               f" the new bound exceeds the predicted difference by at most 10^{mp.nstr(worst, 4)}")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
