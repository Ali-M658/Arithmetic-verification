"""E1 (eigen paper, Section 8): the low spectrum of O(2,3,m) as the cone point of order m becomes cusp-like.

(a) lambda_1, ..., lambda_6 of O(2,3,m) against m (log-log), from figures/data/e1_cusp_spectrum.csv
    (computed by figures/gen/gen_e1_cusp.py with the repository's finite-element solver, two mesh
    levels), lambda_1 heavy ink and lambda_2..lambda_6 a grey ramp, each with its upper bound
    1/4 + pi^2 (j+1)^2 / h_m^2 of the eigen paper's Proposition prop:N1 (thin dashed, same tone), and
    the line 1/4 (thin, light).
(b) h_m^2 (lambda_j - 1/4) / pi^2 against m, with thin dotted lines at j^2.
Asserted: the CSV has 21 orders 7..4096 and j = 1..6; h_m and the bound are recomputed and equal the
CSV columns; the two mesh levels agree to 1e-6 relative; every lambda_j exceeds 1/4, lies below its
bound and decreases in m; lambda_1(7) = 44.8883536 (to 7 digits).
"""
import math

import numpy as np

from figlib import check_only, finish, fs, grey_ramp, rows


def data():
    r = rows("figures/data/e1_cusp_spectrum.csv")
    ms = sorted({int(x["m"]) for x in r})
    assert len(ms) == 21 and ms[0] == 7 and ms[-1] == 4096
    lam = np.zeros((len(ms), 6))
    hm = np.zeros(len(ms))
    for x in r:
        i, j = ms.index(int(x["m"])), int(x["j"])
        m = int(x["m"])
        h = math.acosh(1 / (2 * math.sin(math.pi / m)))
        assert abs(h - float(x["h_m"])) < 1e-9 and abs(0.25 + math.pi ** 2 * (j + 1) ** 2 / h ** 2 - float(x["rayleigh_bound"])) < 1e-6
        assert float(x["rel_diff"]) < 1e-6
        lam[i, j - 1] = float(x["lambda"])
        hm[i] = h
    bound = 0.25 + math.pi ** 2 * (np.arange(1, 7)[None, :] + 1) ** 2 / hm[:, None] ** 2
    assert np.all(lam > 0.25) and np.all(lam <= bound) and np.all(np.diff(lam, axis=0) < 0)
    assert abs(lam[0, 0] - 44.8883536) < 1e-6
    return np.array(ms, float), hm, lam, bound


def draw(ms, hm, lam, bound):
    fs.use()
    fig = fs.figure(118)
    tones = [fs.GREY["ink"]] + grey_ramp(5, lo="dark", hi="light")
    ax = fig.add_axes([0.12, 0.57, 0.85, 0.40])
    ax.axhline(0.25, color=fs.GREY["light"], lw=fs.LW["thin"], zorder=0)
    for j in range(6):
        ax.plot(ms, bound[:, j], color=tones[j], lw=fs.LW["hair"], ls=(0, (3, 2)))
        ax.plot(ms, lam[:, j], color=tones[j], lw=fs.LW["heavy"] if j == 0 else fs.LW["regular"],
                marker="o", ms=fs.MARKER_PT["small"] * 0.8, mfc=tones[j], mec="none")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(6, 5000)
    ax.set_ylim(0.2, 3000)
    fs.decimal_log_ticks(ax.xaxis, [10, 100, 1000])
    fs.decimal_log_ticks(ax.yaxis, [0.25, 1, 10, 100, 1000])
    ax.set_ylabel(r"$\lambda_j$")
    bx = fig.add_axes([0.12, 0.09, 0.85, 0.36])
    y = hm[:, None] ** 2 * (lam - 0.25) / math.pi ** 2
    for j in range(6):
        bx.axhline((j + 1) ** 2, color=tones[j], lw=fs.LW["hair"], ls=(0, (1, 2)), zorder=0)
        bx.plot(ms, y[:, j], color=tones[j], lw=fs.LW["heavy"] if j == 0 else fs.LW["regular"],
                marker="o", ms=fs.MARKER_PT["small"] * 0.8, mfc=tones[j], mec="none")
    bx.set_xscale("log")
    bx.set_yscale("log")
    bx.set_xlim(6, 5000)
    bx.set_ylim(0.5, 60)
    fs.decimal_log_ticks(bx.xaxis, [10, 100, 1000])
    fs.decimal_log_ticks(bx.yaxis, [1, 4, 9, 16, 25, 36])
    bx.set_xlabel(r"$m$")
    bx.set_ylabel(r"$h_m^2(\lambda_j-1/4)/\pi^2$")
    fs.letter_at(fig, 0.005, 0.995, "a")
    fs.letter_at(fig, 0.005, 0.475, "b")
    return fig


if __name__ == "__main__":
    d = data()
    if not check_only():
        finish(draw(*d), "E1")
    print("E1: assertions passed")
