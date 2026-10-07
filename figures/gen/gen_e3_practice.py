"""E3 data (eigen paper, Section 7): eigenvalues needed in practice against the a-priori count.

    python3 figures/gen/gen_e3_practice.py        (a few seconds)

From theory/eigen/data/practice.csv (written by theory/eigen/practice.py): for each computed
orbifold and M, the least N_obs and the least N_apr over the time grid; and N of Theorem thm:E for
the class (Area, systole, M), recomputed by eigen_common.theorem_E_constants. Systoles: the
triangle orbifolds as in practice.py, the family members from numerics/moduli/data/geometries.json.
Writes figures/data/e3_practice.csv. Asserted: the minima reproduce Table tab:practice of the eigen
paper (O(2,8,8): 3, 21; O(3,3,12): 4, 39; family M = 3: 3-50 and 33-694; M = 12: 5-98 and 38-750,
the member of systole 0.694 having no N_apr); N_apr < N everywhere, by a factor of at least 100.
"""
import json
from collections import defaultdict

import mpmath as mp

from common import ROOT, import_from, read_csv, write_csv

ec, _ = import_from("theory/eigen", "eigen_common")
mp.mp.dps = 30


def main():
    rows = read_csv("theory/eigen/data/practice.csv")
    best = defaultdict(lambda: [None, None])
    for r in rows:
        key = (r["orbifold"], int(r["M"]))
        for i, col in enumerate(("N_obs", "N_apr")):
            if r[col]:
                v = int(r[col])
                best[key][i] = v if best[key][i] is None else min(best[key][i], v)
    geo = json.loads((ROOT / "numerics/moduli/data/geometries.json").read_text())["members"]
    sysl = {"O(2, 8, 8)": ("2.256768", "1/4"), "O(3, 3, 12)": ("1.862604", "1/4")}
    for tau, mem in geo.items():
        sysl[f"(0;3,3,3,3) theta={tau}"] = (str(mem["systole"]), "2/3")
    out = []
    for (name, M), (nobs, napr) in sorted(best.items()):
        ell, s = sysl[name]
        num, den = (int(x) for x in s.split("/"))
        A = 2 * mp.pi * num / den
        N = ec.theorem_E_constants(A, mp.mpf(ell), M)["N"]
        if napr is not None:
            assert napr * 100 < N, (name, M, napr, N)
        out.append([name, M, ell, nobs, napr if napr is not None else "", N])
    d = {(r[0], r[1]): r for r in out}
    assert d[("O(2, 8, 8)", 12)][3:5] == [3, 21] and d[("O(3, 3, 12)", 12)][3:5] == [4, 39]
    for M, lo, hi in ((3, (3, 33), (50, 694)), (12, (5, 38), (98, 750))):
        fam = [r for r in out if r[0].startswith("(0;3") and r[1] == M]
        assert min(r[3] for r in fam) == lo[0] and max(r[3] for r in fam) == hi[0]
        apr = [r[4] for r in fam if r[4] != ""]
        assert len(apr) == 7 and min(apr) == lo[1] and max(apr) == hi[1]
    write_csv("e3_practice.csv", ["orbifold", "M", "systole", "N_obs", "N_apr", "N_theory"], out)
    print(f"E3 data: {len(out)} rows, assertions passed")


if __name__ == "__main__":
    main()
