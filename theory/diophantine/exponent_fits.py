#!/usr/bin/env python3
"""
The log-power kappa, fitted the same way on the per-S and the cumulative series.

Model. n(s) = c (log s)^k for the number of degenerate pairs at sum s.
  * per-S:      Poisson maximum likelihood for n(s), s in a window [a, b];
  * cumulative: least squares on log of N(S) - N(a-1) against the exact sum
                sum_{s=a}^{S} c (log s)^k, S in [a, b].
Both fit the same two parameters on the same window, so the two estimates of
k are comparable. The per-S fit is the exact Poisson maximum-likelihood estimate
(Newton's method on the log-linear model). Uncertainties: residual block
bootstrap, applied identically to both fits: the per-S model is fitted, the
multiplicative residuals y/mu are resampled in blocks of 50 consecutive sums and
multiplied back onto the fitted trend, and both fits are repeated (400
resamples). (Resampling blocks of the counts themselves onto fixed abscissae
would destroy the trend and measure the spread of a trend-free null instead.)
For comparison the pure power law n(s) = c s^beta is fitted by Poisson maximum
likelihood on the same window, with the log-likelihood difference and the
Pearson dispersion of the log-power fit.

For contrast it also refits the earlier closed form N(S) = c S (log S)^K from
S = 100, and shows that K exceeds k by the secondary term of
sum_{s<=S} (log s)^k = S (log S)^k (1 - k/log S + ...).

Series fitted: all pairs; primitive pairs; dual (reciprocal) pairs with
scalings; primitive dual pairs; non-dual pairs (all, with scalings); primitive
non-dual pairs. Point estimates use the whole window; the bootstrap uses the
largest whole number of blocks in it. Manin's conjecture on the
dual quartic del Pezzo predicts k = 4 for primitive dual pairs and k = 5 for
dual pairs with scalings (per-S densities of the cumulative X (log X)^4 and
X (log X)^5).

Writes data/exponent_fits.txt.
"""

from __future__ import annotations

import sys
from itertools import combinations
from math import gcd
from pathlib import Path

import numpy as np
from scipy.optimize import least_squares, minimize

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cubic_group import dual, normalize  # noqa: E402
from enumerate_fast import load_groups, load_per_s  # noqa: E402

S_MAX = 4800
BLOCK, NBOOT = 50, 400
OUT: list[str] = []


def say(s=""):
    print(s, flush=True)
    OUT.append(s)


def series() -> dict[str, np.ndarray]:
    n = {k: np.zeros(S_MAX + 1) for k in ("all", "primitive", "dual", "primitive dual", "non-dual",
                                          "primitive non-dual")}
    for S, _, _, _, _, T in load_groups():
        for t1, t2 in combinations(T, 2):
            prim = gcd(gcd(*t1), gcd(*t2)) == 1
            d = dual(t1) == tuple(sorted(normalize(t2)))
            n["all"][S] += 1
            n["primitive"][S] += prim
            n["dual"][S] += d
            n["primitive dual"][S] += prim and d
            n["non-dual"][S] += not d
            n["primitive non-dual"][S] += prim and not d
    check = np.array([r["pairs"] for r in load_per_s()])
    assert np.array_equal(n["all"][10:], check), "group file and per-S file disagree"
    return n


def poisson_fit(x, y):
    """Exact Poisson MLE of log mu = a + b x by Newton's method; returns (a, b, mu)."""
    X = np.column_stack([np.ones_like(x), x])
    th = np.array([np.log(max(y.mean(), 1e-9)) - 4.0 * x.mean(), 4.0])
    for _ in range(100):
        mu = np.exp(X @ th)
        g = X.T @ (y - mu)
        H = X.T @ (X * mu[:, None])
        step = np.linalg.solve(H, g)
        th = th + step
        if np.max(np.abs(step)) < 1e-13:
            break
    mu = np.exp(X @ th)
    return th[0], th[1], mu


def fit_per_s(s, y):
    return poisson_fit(np.log(np.log(s)), y)[1]


def nll(y, mu):
    return float(np.sum(mu - y * np.log(mu)))


def fit_cumulative(s, y):
    cum = np.cumsum(y)
    ok = cum > 0
    ll = np.log(np.log(s))

    def resid(th):
        model = np.cumsum(np.exp(th[0] + th[1] * ll))
        return np.log(model[ok]) - np.log(cum[ok])
    return least_squares(resid, [0.0, 4.0]).x[1]


def bootstrap(fn, s, y, rng):
    """Residual block bootstrap around the fitted per-S trend (the trend is kept)."""
    nb = len(s) // BLOCK
    mu = poisson_fit(np.log(np.log(s)), y)[2]
    r = y / mu
    est = []
    for _ in range(NBOOT):
        idx = rng.integers(0, nb, nb)
        rb = np.concatenate([r[i * BLOCK:(i + 1) * BLOCK] for i in idx])
        est.append(fn(s, mu * rb))
    return np.std(est)


def closed_form_K(S_all, N_all, lo=100):
    m = S_all >= lo
    S, N = S_all[m], N_all[m]
    r = least_squares(lambda th: th[0] + np.log(S) + th[1] * np.log(np.log(S)) - np.log(N), [-8, 5])
    return r.x[1]


def main() -> int:
    rng = np.random.default_rng(20261001)
    n = series()
    s_all = np.arange(S_MAX + 1, dtype=float)
    windows = [(600, 4800), (1200, 4800), (600, 2400), (2400, 4800)]
    say("k in n(s) = c (log s)^k; same model, same window, both series; +- block-bootstrap sd")
    say(f"{'series':16s} {'window':>11s} {'per-S k':>14s} {'cumulative k':>14s}")
    table = {}
    for name in n:
        for a, b in windows:
            s = s_all[a:b + 1]
            y = n[name][a:b + 1]
            kp = fit_per_s(s, y)          # point estimates on the whole window [a, b]
            kc = fit_cumulative(s, y)
            # the bootstrap uses a whole number of blocks, so that resamples have equal length
            m = (len(s) // BLOCK) * BLOCK
            sp = bootstrap(fit_per_s, s[:m], y[:m], rng)
            sc = bootstrap(fit_cumulative, s[:m], y[:m], rng)
            table[(name, a, b)] = (kp, sp, kc, sc)
            say(f"{name:16s} {a:5d}-{b:<5d} {kp:7.2f} +- {sp:4.2f} {kc:7.2f} +- {sc:4.2f}")
        say()

    say("pure power law n(s) = c s^beta, Poisson MLE, window 600-4800 (for comparison with the log-power model)")
    for name in ("all", "primitive"):
        s = s_all[600:4801]
        y = n[name][600:4801]
        _, beta, mu_p = poisson_fit(np.log(s), y)
        _, k, mu_l = poisson_fit(np.log(np.log(s)), y)
        disp = float(np.sum((y - mu_l) ** 2 / mu_l) / (len(y) - 2))
        d = nll(y, mu_p) - nll(y, mu_l)
        say(f"{name:16s} beta = {beta:.3f} (cumulative exponent about {1 + beta:.2f}); log-power k = {k:.3f}; "
            f"NLL(power) - NLL(log-power) = {d:.2f}; Pearson dispersion {disp:.2f}; scaled difference {d / disp:.2f}")
    say()

    # round 7: the sums 4801..6000 as a holdout. Both laws are fitted per sum on 600..4800 (above); their
    # predictions of N(6000) - N(4800) are compared with the exact count, 145679 - 102719 (Table 2 of the note;
    # N(6000) from the third enumeration, N(4800) from per_S.csv).
    N6000, N4800 = 145679, int(np.cumsum(n["all"])[4800])
    assert N4800 == 102719, N4800
    s = s_all[600:4801]
    y = n["all"][600:4801]
    a_p, beta, mu_p = poisson_fit(np.log(s), y)
    a_l, k, mu_l = poisson_fit(np.log(np.log(s)), y)
    disp = float(np.sum((y - mu_l) ** 2 / mu_l) / (len(y) - 2))
    sh = np.arange(4801, 6001, dtype=float)
    pred_l = float(np.sum(np.exp(a_l + k * np.log(np.log(sh)))))
    pred_p = float(np.sum(np.exp(a_p + beta * np.log(sh))))
    act = N6000 - N4800
    say(f"holdout 4801-6000 (all pairs): exact N(6000) - N(4800) = {act}; log-power law predicts {pred_l:.0f} "
        f"({100 * (pred_l / act - 1):+.1f}%), power law {pred_p:.0f} ({100 * (pred_p / act - 1):+.1f}%); "
        f"misses in dispersion-scaled Poisson sd: {abs(pred_l - act) / np.sqrt(disp * act):.1f} and "
        f"{abs(pred_p - act) / np.sqrt(disp * act):.1f}")
    say()

    # round 8: how much the per-sum exponent depends on the arithmetic of s (Lemma 5: n(s) is a divisor sum), and
    # where the two laws are tangent: the log-slope k/log s of c (log s)^k equals beta at s = exp(k/beta).
    s = s_all[600:4801]
    y = n["all"][600:4801]
    si = s.astype(int)
    classes = {"gcd(s,6)=1": np.gcd(si, 6) == 1, "s odd": si % 2 == 1, "s even": si % 2 == 0, "6 | s": si % 6 == 0}
    kres = {}
    for lab, mask in classes.items():
        kres[lab] = fit_per_s(s[mask], y[mask])
    say("per-sum k for all pairs on 600-4800, by residue class of s: "
        + "; ".join(f"{lab}: {v:.2f}" for lab, v in kres.items()))
    assert 4.0 < kres["gcd(s,6)=1"] < 4.1 and 4.25 < kres["s odd"] < 4.35 and 4.55 < kres["s even"] < 4.65 \
        and 4.9 < kres["6 | s"] < 5.0, kres
    s_tan = float(np.exp(k / beta))
    say(f"tangency of the two fitted laws: k/log s = beta at s = {s_tan:.0f}")
    assert 2000 < s_tan < 2200, s_tan
    assert abs(100 * (pred_l / act - 1) - 0.25) < 0.01 and abs(100 * (pred_p / act - 1) - 2.33) < 0.01
    say()

    N_all = np.cumsum(n["all"])
    K = closed_form_K(s_all[10:], N_all[10:])
    kp = table[("all", 600, 4800)][0]
    L = np.log(3000)
    say(f"closed form c S (log S)^K fitted on 100..4800 (the earlier cumulative fit): K = {K:.2f}")
    say(f"secondary-term prediction from per-S k = {kp:.2f}: K ~ k (1 + 1/log S) = "
        f"{kp * (1 + 1 / L):.2f} at S ~ 3000")
    (HERE / "data" / "exponent_fits.txt").write_text("\n".join(OUT) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
