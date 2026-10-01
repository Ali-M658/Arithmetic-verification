#!/usr/bin/env python3
"""
The log-power kappa, fitted the same way on the per-S and the cumulative series.

Model. n(s) = c (log s)^k for the number of degenerate pairs at sum s.
  * per-S:      Poisson maximum likelihood for n(s), s in a window [a, b];
  * cumulative: least squares on log of N(S) - N(a-1) against the exact sum
                sum_{s=a}^{S} c (log s)^k, S in [a, b].
Both fit the same two parameters on the same window, so the two estimates of
k are comparable. Uncertainties: block bootstrap (blocks of 50 consecutive
sums, 400 resamples) applied identically to both.

For contrast it also refits the earlier closed form N(S) = c S (log S)^K from
S = 100, and shows that K exceeds k by the secondary term of
sum_{s<=S} (log s)^k = S (log S)^k (1 - k/log S + ...).

Series fitted: all pairs; primitive pairs; dual (reciprocal) pairs with
scalings; primitive dual pairs; non-dual pairs. Manin's conjecture on the
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
    n = {k: np.zeros(S_MAX + 1) for k in ("all", "primitive", "dual", "primitive dual", "non-dual")}
    for S, _, _, _, _, T in load_groups():
        for t1, t2 in combinations(T, 2):
            prim = gcd(gcd(*t1), gcd(*t2)) == 1
            d = dual(t1) == tuple(sorted(normalize(t2)))
            n["all"][S] += 1
            n["primitive"][S] += prim
            n["dual"][S] += d
            n["primitive dual"][S] += prim and d
            n["non-dual"][S] += not d
    check = np.array([r["pairs"] for r in load_per_s()])
    assert np.array_equal(n["all"][10:], check), "group file and per-S file disagree"
    return n


def fit_per_s(s, y):
    ls = np.log(np.log(s))

    def nll(th):
        mu = np.exp(th[0] + th[1] * ls)
        return np.sum(mu - y * np.log(mu))
    return minimize(nll, [0.0, 4.0], method="Nelder-Mead",
                    options=dict(xatol=1e-9, fatol=1e-9, maxiter=20000)).x[1]


def fit_cumulative(s, y):
    cum = np.cumsum(y)
    ok = cum > 0
    ll = np.log(np.log(s))

    def resid(th):
        model = np.cumsum(np.exp(th[0] + th[1] * ll))
        return np.log(model[ok]) - np.log(cum[ok])
    return least_squares(resid, [0.0, 4.0]).x[1]


def bootstrap(fn, s, y, rng):
    nb = len(s) // BLOCK
    est = []
    for _ in range(NBOOT):
        idx = rng.integers(0, nb, nb)
        # resample blocks of counts, keep the abscissae fixed so the sum structure is preserved
        yb = np.concatenate([y[i * BLOCK:(i + 1) * BLOCK] for i in idx])
        sb = s[: len(yb)]
        est.append(fn(sb, yb))
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
            # trim to a whole number of blocks so resamples have equal length
            m = (len(s) // BLOCK) * BLOCK
            s, y = s[:m], y[:m]
            kp = fit_per_s(s, y)
            kc = fit_cumulative(s, y)
            sp = bootstrap(fit_per_s, s, y, rng)
            sc = bootstrap(fit_cumulative, s, y, rng)
            table[(name, a, b)] = (kp, sp, kc, sc)
            say(f"{name:16s} {a:5d}-{b:<5d} {kp:7.2f} +- {sp:4.2f} {kc:7.2f} +- {sc:4.2f}")
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
