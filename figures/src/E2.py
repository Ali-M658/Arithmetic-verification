"""E2 (eigen paper, Section 6): the separation mechanism for O(2,8,8) among the six signatures of
area pi/2 with orders at most 12.

Curves from figures/data/e2_gap.csv (figures/gen/gen_e2_gap.py): the gaps |G_sigma0 - G_sigma| to the
five competitors (grey ramp, the nearest competitor (0;3,3,12) darkest and heavy), the bound on the
closed-geodesic term (ink, dashed), and the error of keeping N = 21 and N = 100 eigenvalues (ink and
mid grey, dotted); shaded: the times at which hyp + err_21 is below half the nearest gap.
Asserted: the shaded window is one interval inside (0.001, 1) containing a grid time within 1% of
t = 0.05, where theory/eigen/practice.py certifies with N = 21; the nearest
gap is the gap to (0;3,3,12) for t <= 0.3.
"""
import numpy as np

from figlib import check_only, finish, fs, grey_ramp, rows

COMP = ["2-6-12", "3-4-6", "4-4-4", "2-2-2-4", "3-3-12"]


def data():
    r = rows("figures/data/e2_gap.csv")
    t = np.array([float(x["t"]) for x in r])
    gaps = {c: np.array([float(x["gap_" + c]) for x in r]) for c in COMP}
    hyp = np.array([float(x["hyp_bound"]) for x in r])
    e21 = np.array([float(x["err_N21"]) for x in r])
    e100 = np.array([float(x["err_N100"]) for x in r])
    near = np.array([float(x["nearest_gap"]) for x in r])
    ok = hyp + e21 < near / 2
    idx = np.flatnonzero(ok)
    assert len(idx) and np.all(np.diff(idx) == 1), "window is one interval"
    assert t[idx[0]] > 0.001 and t[idx[-1]] < 1 and np.any(np.abs(t[idx] / 0.05 - 1) < 0.01)
    assert np.all(np.isclose(near[t <= 0.3], gaps["3-3-12"][t <= 0.3]))
    return t, gaps, hyp, e21, e100, ok


def draw(t, gaps, hyp, e21, e100, ok):
    fs.use()
    fig = fs.figure(72)
    ax = fig.add_axes([0.12, 0.16, 0.85, 0.80])
    lo, hi = 1e-6, 30
    ax.fill_between(t, lo, hi, where=ok, color=fs.GREY["faint"], lw=0, zorder=0)
    tones = grey_ramp(4, lo="light", hi="mid")
    for c, g in zip(COMP[:4], tones):
        ax.plot(t, gaps[c], color=g, lw=fs.LW["regular"])
    ax.plot(t, gaps["3-3-12"], color=fs.GREY["ink"], lw=fs.LW["heavy"])
    ax.plot(t, np.clip(hyp, lo / 10, None), color=fs.GREY["ink"], lw=fs.LW["thin"], ls=(0, (3, 2)))
    ax.plot(t, e21, color=fs.GREY["ink"], lw=fs.LW["thin"], ls=(0, (1, 1.5)))
    ax.plot(t, e100, color=fs.GREY["mid"], lw=fs.LW["thin"], ls=(0, (1, 1.5)))
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(1e-3, 1)
    ax.set_ylim(lo, hi)
    fs.decimal_log_ticks(ax.xaxis, [0.001, 0.01, 0.1, 1])
    ax.set_yticks([1e-6, 1e-4, 1e-2, 1])
    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"$|G_{\sigma_0}(t)-G_\sigma(t)|$")
    return fig


if __name__ == "__main__":
    d = data()
    if not check_only():
        finish(draw(*d), "E2")
    print("E2: assertions passed")
