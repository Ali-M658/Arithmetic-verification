"""E3 data (eigen paper, Section 7): eigenvalues needed by the a-posteriori test against the a-priori count.

    python3 figures/gen/gen_e3_practice.py        (a second)

From theory/eigen/data/practice.csv (written by theory/eigen/practice.py) and
theory/eigen/data/instances.csv (theory/eigen/instances.py): for each computed orbifold and M (the two
triangle orbifolds at M = 12, the eight members of the family (0;3,3,3,3) at M = 3 and 12), with the
instance inputs (systole lower bound from the complete enumeration, diameter bound 2 diam P) and the
full committed spectra:
  N_obs     the least N over the t-grid from which on the data lie within half the nearest gap of
            G_sigma_0 (the manuscript's N_obs, on the fine grid);
  N_apr     the test's count N_test for criterion (C1) of Theorem 7.1 (column kept under its old name,
            which figures/src/E3.py reads); N_test_C2 for criterion (C2) alongside;
  N_theory  N of Theorem 6.2 for Cl(Area, systole lower bound, M).
The x-coordinate is the systole (computed value).  Writes figures/data/e3_practice.csv.
Asserted: the values of the revised Table 3 (O(2,8,8): N_obs 3, N_test 18 (C1), 20 (C2); O(3,3,12): 3,
25, 29; family M = 3: N_obs 3-43, N_test(C1) 24-767; M = 12: 4-63, 28-847; all ten succeed);
N_obs <= N_test(C1) <= N_test(C2) and 100 N_test(C2) < N_theory everywhere.
"""
from common import read_csv, write_csv

NAMES = {"O(2,8,8)": "O(2, 8, 8)", "O(3,3,12)": "O(3, 3, 12)"}   # the labels figures/src/E3.py expects


def main():
    rows = read_csv("theory/eigen/data/practice.csv")
    inst = {r["orbifold"]: r for r in read_csv("theory/eigen/data/instances.csv")}
    out = []
    for r in rows:
        if (r["diameter_input"], r["eps_j"], r["data"]) != ("B1", "eps", "full"):
            continue
        name = r["orbifold"]
        label = NAMES.get(name, "(0;3,3,3,3) theta=" + name.split("=")[1] if name.startswith("O_tau") else name)
        n1, n2, nobs, nth = int(r["N_C1"]), int(r["N_C2"]), int(r["N_obs"]), int(r["N_thm62"])
        assert nobs <= n1 <= n2 and 100 * n2 < nth, (name, r["M"], nobs, n1, n2, nth)
        out.append([label, int(r["M"]), inst[name]["systole_computed"], nobs, n1, nth, n2,
                    inst[name]["systole_lower_bound"]])
    out.sort(key=lambda x: (x[0], x[1]))
    d = {(o[0], o[1]): o for o in out}
    assert [d[("O(2, 8, 8)", 12)][i] for i in (3, 4, 6)] == [3, 18, 20]
    assert [d[("O(3, 3, 12)", 12)][i] for i in (3, 4, 6)] == [3, 25, 29]
    for M, nobs, n1 in ((3, (3, 43), (24, 767)), (12, (4, 63), (28, 847))):
        fam = [o for o in out if o[0].startswith("(0;3") and o[1] == M]
        assert len(fam) == 8
        assert (min(o[3] for o in fam), max(o[3] for o in fam)) == nobs, (M, [o[3] for o in fam])
        assert (min(o[4] for o in fam), max(o[4] for o in fam)) == n1, (M, [o[4] for o in fam])
    write_csv("e3_practice.csv", ["orbifold", "M", "systole", "N_obs", "N_apr", "N_theory", "N_test_C2",
                                  "systole_lower_bound"], out)
    print(f"E3 data: {len(out)} rows, assertions passed")


if __name__ == "__main__":
    main()
