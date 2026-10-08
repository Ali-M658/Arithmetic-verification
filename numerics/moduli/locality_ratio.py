"""Two numbers quoted in round 4 (paper/jga, Section 4 and supplement S4, S6), from committed data only.

(1) How loose the explicit bound of thm:quantlocality(a) (the bound B(l, diam, t) of lem:hypbound) with the diameter bound
    2 diam Q) is on the (0;3,3,3,3) family: for every pair of the 28, at the first time at which the
    difference of the computed traces is 10^3 times its error budget (summary.json, first_strong_t),
    the ratio B / |Z_i - Z_j| (data/trace_differences.csv). Pairs whose time lies beyond the window
    t <= l^2/(2(1+l)) of the bound are skipped (none is).
(2) The contribution of the shortest closed geodesics to the heat traces of O(2,8,8) and O(3,3,12) at
    t = 0.025 and 0.03, with weight w = 2 l (one geodesic, two orientations; supplement S4) for each of
    the three shortest lengths listed there, so that the window 0.0015 <= t <= 0.025 of Section 4 is
    one on which the geodesic term is negligible against the stated agreements (7e-13, 4e-13).

    python3 numerics/moduli/locality_ratio.py        (a second; reads data/, writes nothing)
Asserted: (1) every ratio lies in [4e6, 1.1e10] and the extremes are those quoted (4.4e6, 1.0e10);
(2) at t = 0.025 both contributions are below 3e-15, and at t = 0.03 that of O(3,3,12) is 7.5e-13 to
8e-13.
"""
import csv
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
AREA = 4 * math.pi / 3


def B(ell, diam, A, t):
    """lem:hypbound of paper/jga (lem:hyp of paper/eigen): the bound on the hyperbolic term for t <= l^2/(2(1+l))."""
    return (math.pi * math.exp(3 * diam) * ell * math.exp(ell / 2) / (A * (1 - math.exp(-ell)))
            * (1 + 2 * t / (ell - t)) * math.exp(-ell ** 2 / (4 * t)) / math.sqrt(4 * math.pi * t))


summary = json.load(open(os.path.join(DATA, "summary.json")))
geo = json.load(open(os.path.join(DATA, "geometries.json")))["members"]
rows = list(csv.DictReader(open(os.path.join(DATA, "trace_differences.csv"))))
ratios = {}
for key, pair in summary["pairs"].items():
    ta, tb = key.split("-")
    ell = min(pair["systoles"])
    diam = max(geo[ta]["diam_O_upper_bound"], geo[tb]["diam_O_upper_bound"])
    r = [x for x in rows if x["tau_i"] == ta and x["tau_j"] == tb]
    x = min(r, key=lambda x: abs(float(x["t"]) - pair["first_strong_t"]))
    t = float(x["t"])
    assert t <= ell ** 2 / (2 * (1 + ell)), key
    ratios[key] = B(ell, diam, AREA, t) / abs(float(x["D_measured"]))
lo, hi = min(ratios, key=ratios.get), max(ratios, key=ratios.get)
print(f"(1) B / |Z_i - Z_j| at the first strong time, 28 pairs: from {ratios[lo]:.2e} ({lo}) to {ratios[hi]:.2e} ({hi})")
assert len(ratios) == 28
assert all(4e6 <= v <= 1.1e10 for v in ratios.values())
assert f"{ratios[lo]:.1e}" == "4.4e+06" and f"{ratios[hi]:.1e}" == "1.0e+10"


def hyp(lengths, t):
    """Sum over the listed primitive lengths of w g_t(l) / (2 sinh(l/2)), w = 2 l (two orientations)."""
    return sum(2 * ell * math.exp(-t / 4) * math.exp(-ell ** 2 / (4 * t)) / math.sqrt(4 * math.pi * t)
               / (2 * math.sinh(ell / 2)) for ell in lengths)


SHORTEST = {"O(2,8,8)": (2.256768, 2.8816, 3.0571), "O(3,3,12)": (1.862604, 2.9807, 3.4027)}
for t in (0.025, 0.03):
    vals = {k: hyp(v, t) for k, v in SHORTEST.items()}
    print(f"(2) t = {t}: geodesic term " + ", ".join(f"{k} {v:.2e}" for k, v in vals.items()))
    if t == 0.025:
        assert all(v < 3e-15 for v in vals.values())
    else:
        assert 7.5e-13 <= vals["O(3,3,12)"] <= 8e-13
print("all checks passed")
