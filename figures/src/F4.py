"""F4 (Section 3): how many heat coefficients are needed, against the area.

Points: for each of the 525 complete area classes Sig(s), s = Area/2pi <= 7/5, the largest
K_mult(O; Sig) in the class (figures/data/f4_area_classes.csv). Step curves: the proven upper
bound floor(2s) + 4 (Theorem S, Corollary S2) and, from s = 3 (A >= 6 pi, the hypothesis of
Corollary N1), the lower bound floor(log_4(s+1)) + 2 of f(A) = max_{Area <= A} K_mult. Split disc: the class s = 1/4 of (2,8,8) and (3,3,12).
Open squares: the Theorem N(a) pairs for
L = 2..6, which share L coefficients, so K_mult >= L + 1 there (figures/data/f4_construction.csv).

Asserted: every class value lies strictly below the upper bound; the class data lie below
s = 3, outside the range of Corollary N1; the construction points sit
above the lower bound at their own s and below the upper bound; the step functions are
recomputed exactly (Fraction) and equal the CSV columns.
"""
from fractions import Fraction

import numpy as np

from figlib import check_only, finish, fs, rows


def upper(s):
    return int(2 * s) + 4


def lower(s):
    j = 0
    while 4 ** (j + 1) <= s + 1:
        j += 1
    return j + 2


S_LOWER = 3                                         # Corollary N1 holds for A >= 6 pi, i.e. s >= 3


def data():
    cls = rows("figures/data/f4_area_classes.csv")
    con = rows("figures/data/f4_construction.csv")
    assert len(cls) == 525
    s = [Fraction(r["s"]) for r in cls]
    k = [int(r["max_K_mult"]) for r in cls]
    for si, ki, r in zip(s, k, cls):
        assert upper(si) == int(r["upper_bound_floor_2s_plus_4"]) and lower(si) == int(r["lower_bound_floor_log4_s_plus_1_plus_2"])
        assert 1 <= ki < upper(si)
    pil = next(r for r in cls if r["s"] == "1/4")    # the pillow class: (2,8,8) ~ (3,3,12) share c_1, c_2
    assert (pil["extremal_signature"], pil["partner_sharing_K_mult_minus_1"], pil["max_K_mult"]) == ("(0;2,8,8)", "(0;3,3,12)", "3")
    assert max(s) < S_LOWER                         # the class data lie below the range of Corollary N1
    cs = [float(r["s_float"]) for r in con]
    ck = [int(r["K_mult_at_least"]) for r in con]
    for r, c, kk in zip(con, cs, ck):
        L = int(r["L"])
        assert kk == L + 1 and int(r["shared_coefficients"]) == L
        assert c < 4 ** (L - 1) - 1 + 1e-9 and lower(Fraction(c).limit_denominator(10 ** 6)) <= kk < upper(c)
    return np.array([float(x) for x in s]), np.array(k), np.array(cs), np.array(ck)


def draw(s, k, cs, ck):
    fs.use()
    fig = fs.figure(68)
    ax = fig.add_axes([0.10, 0.15, 0.86, 0.80])
    x = np.logspace(np.log10(0.02), np.log10(2000), 4000)
    ax.step(x, [upper(v) for v in x], where="post", color=fs.GREY["ink"], lw=fs.LW["regular"])
    xl = x[x >= S_LOWER]
    ax.step(xl, [lower(v) for v in xl], where="post", color=fs.GREY["ink"], lw=fs.LW["regular"], ls=(0, (4, 2)))
    ax.plot(s, k, ls="none", marker="o", ms=fs.MARKER_PT["small"], mfc=fs.GREY["dark"], mec="none")
    ax.plot([0.25], [3], ls="none", marker="o", ms=fs.MARKER_PT["large"], fillstyle="left", mfc=fs.PILLOW["2,8,8"],
            mfcalt=fs.PILLOW["3,3,12"], mec=fs.GREY["ink"], mew=fs.LW["hair"], zorder=5)
    ax.plot(cs, ck, ls="none", marker="s", ms=fs.MARKER_PT["regular"], mfc="white", mec=fs.GREY["ink"], mew=fs.LW["regular"])
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(0.02, 2000)
    ax.set_ylim(0.8, 3000)
    ax.set_xlabel(r"$\mathrm{Area}/2\pi$")
    ax.set_ylabel(r"$K_{\mathrm{mult}}$")
    return fig


if __name__ == "__main__":
    d = data()
    if not check_only():
        finish(draw(*d), "F4")
    print("F4: assertions passed")
