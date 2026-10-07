"""E2 data (eigen paper, Section 6): the separation mechanism for O(2,8,8).

    python3 figures/gen/gen_e2_gap.py        (about a minute)

For the six signatures of area pi/2 with cone orders at most 12 (the competitor set S of the eigen
paper's Table tab:practice), G_sigma(t) = I(t) + sum_i E_{m_i}(t) at 30 digits
(theory/eigen/eigen_common.G-terms through practice.Gcache), and against sigma_0 = (0;2,8,8):
  gap_<sigma>(t) = |G_sigma0(t) - G_sigma(t)|                 (five curves)
  hyp(t)         = the bound of the eigen paper's Lemma lem:hyp with the true systole 2.256768 and
                   the diameter bound 2 x (longest side) (practice.hypB, practice.triangle_diam_upper)
  err_N(t)       = tail + perturbation terms of Theorem thm:post for N = 21 and N = 100, from the
                   committed spectrum of O(2,8,8) (eigen_common.load_triangle_spectrum), with
                   beta = max over S of sum b_0(m_i) and s minimised over s = t/20, 2t/20, ..., 19t/20.
Writes figures/data/e2_gap.csv. Asserted: the competitor set is the six signatures; at t = 0.001
the gap to (0;3,3,12) is within 0.5% of d_3 t + d_4 t^2 = (25/12) t - (1775/24) t^2, from the first
heat-invariant difference; the
certificate condition hyp + err_21 < (nearest gap)/2 holds at t = 0.05 (where practice.py finds
N_apr = 21) and fails at t = 0.001 and at t = 1, so the window is bounded on both sides.
"""
import math
from fractions import Fraction as Fr

import mpmath as mp

from common import import_from, write_csv

ec, _ = import_from("theory/eigen", "eigen_common")
pr, _ = import_from("theory/eigen", "practice")
mp.mp.dps = 30

SIG0 = (0, (2, 8, 8))
ELL = mp.mpf("2.256768")
TS = [10 ** (-3 + 3 * i / 60) for i in range(61)]
NS = (21, 100)


def main():
    comp = [x for x in ec.signatures(Fr(1, 2), 12) if ec.area_over_2pi(*x) == Fr(1, 4)]
    assert sorted(comp) == sorted([(0, (2, 8, 8)), (0, (3, 3, 12)), (0, (2, 6, 12)), (0, (3, 4, 6)),
                                   (0, (4, 4, 4)), (0, (2, 2, 2, 4))]), comp
    others = [c for c in comp if c != SIG0]
    A = mp.pi / 2
    diam = pr.triangle_diam_upper((2, 8, 8))
    spec, _ = ec.load_triangle_spectrum((2, 8, 8))
    lam = [x for x, _ in spec]
    err = [e for _, e in spec]
    beta = max(sum(ec.mpq(ec.b_cone(0, m)) for m in o) for _, o in comp)
    cache = pr.Gcache()
    rows, check = [], {}
    for t in TS:
        tt = mp.mpf(t)
        G0 = cache.G(SIG0[0], SIG0[1], tt)
        gaps = {o: abs(cache.G(g, o, tt) - G0) for g, o in others}
        hyp = pr.hypB(ELL, diam, A, tt)
        errs = {}
        for N in NS:
            lamN = mp.mpf(lam[N]) - err[N]
            tail = min(mp.e ** (-lamN * (tt - s)) * (A / (4 * mp.pi * s) + beta + pr.hypB(ELL, diam, A, s))
                       for s in (tt * k / 20 for k in range(1, 20)))
            errs[N] = tail + tt * mp.fsum(err[:N])
        nearest = min(gaps.values())
        rows.append([f"{t:.6g}"] + [mp.nstr(gaps[o], 8) for _, o in others] + [mp.nstr(hyp, 8)]
                    + [mp.nstr(errs[N], 8) for N in NS] + [mp.nstr(nearest, 8)])
        check[round(t, 6)] = (gaps, hyp, errs, nearest)
    g1 = check[0.001][0][(3, 3, 12)]
    t1 = mp.mpf("0.001")
    assert abs(g1 / (mp.mpf(25) / 12 * t1 - mp.mpf(1775) / 24 * t1 ** 2) - 1) < 0.005, g1
    t05 = min(check, key=lambda x: abs(x - 0.05))
    gaps, hyp, errs, nearest = check[t05]
    assert hyp + errs[21] < nearest / 2, ("certificate fails at t = 0.05", hyp, errs[21], nearest)
    for tb in (0.001, 1.0):
        gaps, hyp, errs, nearest = check[tb]
        assert hyp + errs[21] > nearest / 2, ("window not bounded", tb)
    header = ["t"] + ["gap_" + "-".join(map(str, o)) for _, o in others] + ["hyp_bound"] + \
             [f"err_N{N}" for N in NS] + ["nearest_gap"]
    write_csv("e2_gap.csv", header, rows)
    print(f"E2 data: {len(TS)} times, five competitors, assertions passed")


if __name__ == "__main__":
    main()
