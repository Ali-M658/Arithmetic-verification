"""Load eigenvalue runs and attach per-eigenvalue error estimates.

Production level = last entry of solve.LEVELS.  The error estimate of each
production eigenvalue is the difference to the level before it (a pure
p-refinement, same mesh), floored at 1e-14 * lambda for round-off.  Because the
convergence is exponential in p, this difference over-estimates the error of
the finer level; it is used as a conservative bound throughout.
"""

import os

import numpy as np

from solve import LEVELS, run_path


def load_level(pqr, bc, h, order):
    d = np.load(run_path(pqr, bc, h, order), allow_pickle=True)
    return d["lam"], d


def table(pqr, bc, levels=LEVELS, nmax=None):
    lams = []
    for h, order in levels:
        lam, _ = load_level(pqr, bc, h, order)
        lams.append(lam)
    n = min(len(l) for l in lams)
    if nmax is not None:
        n = min(n, nmax)
    lams = [l[:n] for l in lams]
    prod, prev = lams[-1], lams[-2]
    err = np.maximum(np.abs(prod - prev), 1e-14 * np.maximum(np.abs(prod), 1.0))
    if bc == "N":
        # the constant eigenfunction: lambda_0 = 0 exactly
        assert abs(prod[0]) < 1e-8, prod[0]
        prod = prod.copy()
        prod[0] = 0.0
        err[0] = 0.0
    return dict(lam=prod, err=err, levels=list(levels), all=lams)


def available(pqr, bc, levels=LEVELS):
    return all(os.path.exists(run_path(pqr, bc, h, o)) for h, o in levels)
