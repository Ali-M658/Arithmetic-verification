"""E3 (eigen paper, Section 7): eigenvalues needed in practice against the a-priori count.

From figures/data/e3_practice.csv (figures/gen/gen_e3_practice.py), against the systole: for the
eight members of the family (0;3,3,3,3), N_obs (circles), N_apr (diamonds) and N of Theorem thm:E
(squares), open for M = 3 and filled for M = 12, members joined by thin lines; for O(2,8,8) and
O(3,3,12) (M = 12) the same markers in their pillow hues (dark, light).
Asserted: N_obs <= N_apr < N wherever N_apr exists; within the family at fixed M, N_apr decreases
as the systole grows.
"""
import numpy as np

from figlib import check_only, finish, fs, rows


def data():
    r = rows("figures/data/e3_practice.csv")
    out = []
    for x in r:
        napr = int(x["N_apr"]) if x["N_apr"] else None
        rec = (x["orbifold"], int(x["M"]), float(x["systole"]), int(x["N_obs"]), napr, float(x["N_theory"]))
        if napr is not None:
            assert rec[3] <= napr < rec[5]
        out.append(rec)
    for M in (3, 12):
        fam = sorted([o for o in out if o[0].startswith("(0;") and o[1] == M and o[4] is not None], key=lambda o: o[2])
        assert all(a[4] > b[4] for a, b in zip(fam, fam[1:]))
    return out


def draw(recs):
    fs.use()
    fig = fs.figure(78)
    ax = fig.add_axes([0.12, 0.15, 0.85, 0.81])
    marks = {3: "o", 4: "D", 5: "s"}           # column index -> marker
    for M, filled in ((3, False), (12, True)):
        fam = sorted([o for o in recs if o[0].startswith("(0;") and o[1] == M], key=lambda o: o[2])
        x = np.array([o[2] for o in fam])
        for col, mk in marks.items():
            y = np.array([np.nan if o[col] is None else o[col] for o in fam], float)
            ax.plot(x, y, color=fs.GREY["mid"], lw=fs.LW["hair"], zorder=1)
            ax.plot(x, y, ls="none", marker=mk, ms=fs.MARKER_PT["small"],
                    mfc=fs.GREY["ink"] if filled else "white", mec=fs.GREY["ink"], mew=fs.LW["thin"], zorder=3)
    for name, hue in (("O(2, 8, 8)", fs.PILLOW["2,8,8"]), ("O(3, 3, 12)", fs.PILLOW["3,3,12"])):
        o = next(o for o in recs if o[0] == name and o[1] == 12)
        for col, mk in marks.items():
            ax.plot([o[2]], [o[col]], ls="none", marker=mk, ms=fs.MARKER_PT["regular"], mfc=hue,
                    mec=fs.GREY["ink"], mew=fs.LW["hair"], zorder=4)
    ax.set_yscale("log")
    ax.set_xlim(0.6, 2.75)
    ax.set_ylim(1, 1e14)
    ax.set_yticks([1, 1e2, 1e4, 1e6, 1e8, 1e10, 1e12, 1e14])
    ax.set_xlabel(r"systole")
    ax.set_ylabel(r"number of eigenvalues")
    return fig


if __name__ == "__main__":
    d = data()
    if not check_only():
        finish(draw(d), "E3")
    print("E3: assertions passed")
