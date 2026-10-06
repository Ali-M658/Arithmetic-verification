"""search_dup: NUMERICAL search (floating point, not a certificate) for failure points of the ST.13 construction.

For each row m, each distinct order a, each sign s = +-1 (c = a + s/2) and each shape
   (R) q~ = (z - c) g(z),            g real monic of degree n-1, parameters = coefficients of g
   (C) q~ = ((z - c)^2 + y^2) g(z),  g real monic of degree n-2, parameters = (y, coefficients of g)
minimise max_nu |H_nu(q~) - H_nu(m)| = max |F (I(q~) - I(m))| by multistart Nelder-Mead + SLSQP (epigraph form).
Writes dup_candidates.json (float parameters of the best point per (a, s, shape)); check_dup.py rebuilds
each one exactly in rationals and verifies it. Time cap per row; checkpoint after every row.
"""
import json, sys, time
import numpy as np
from scipy.optimize import minimize
from fractions import Fraction as Fr
from stab610 import Setup, F as Fexact, invariants
from rows_table import TABLE

rng = np.random.default_rng(12345)
OUT = 'dup_candidates.json'
import os
TIME_CAP = int(os.environ.get('DUP_CAP', 900))  # seconds per row
NPER = int(os.environ.get('DUP_NPER', 6))


def make_obj(m, c, shape):
    n = len(m)
    Fm = np.array([[float(x) for x in row] for row in Fexact(n)])
    Im = np.array([float(x) for x in invariants(m)])
    mu = float(max(m))
    nb = 2 * n - 3

    def coeffs(p):
        if shape == 'R':
            g = np.concatenate(([1.0], p * mu ** np.arange(1, n)))
            return np.polymul([1.0, -c], g)
        y = p[0]
        g = np.concatenate(([1.0], p[1:] * mu ** np.arange(1, n - 1)))
        return np.polymul([1.0, -2 * c, c * c + y * y], g)

    def dH(p):
        q = coeffs(p)
        e = np.array([(-1) ** j * q[j] for j in range(n + 1)])
        pk = np.zeros(nb + 1)
        E = lambda j: e[j] if j <= n else 0.0
        for k in range(1, nb + 1):
            s = (-1) ** (k - 1) * k * E(k)
            for i in range(1, k):
                s += (-1) ** (i - 1) * E(i) * pk[k - i]
            pk[k] = s
        I = np.array([e[n - 1] / e[n]] + [pk[2 * k - 1] for k in range(1, n)])
        return Fm @ (I - Im)

    return dH, coeffs


def natural_start(m, a, shape):
    rest = list(m)
    rest.remove(a)
    if shape == 'C':
        # remove a second root: another copy of a if present, else the nearest order
        if a in rest:
            rest.remove(a)
        else:
            rest.remove(min(rest, key=lambda b: abs(b - a)))
    mu = float(max(m))
    g = np.poly(np.array(rest, dtype=float))
    p = g[1:] / mu ** np.arange(1, len(g))
    return p


def optimise(dH, p0, scale):
    f = lambda p: np.max(np.abs(dH(p))) / scale
    r = minimize(f, p0, method='Nelder-Mead', options=dict(xatol=1e-13, fatol=1e-14, maxiter=6000, maxfev=12000))
    p = r.x
    t0 = f(p)
    cons = [{'type': 'ineq', 'fun': (lambda v, i=i, s=s: v[-1] - s * dH(v[:-1])[i] / scale)}
            for i in range(len(dH(p))) for s in (1, -1)]
    r2 = minimize(lambda v: v[-1], np.concatenate((p, [t0])), method='SLSQP', constraints=cons,
                  options=dict(ftol=1e-15, maxiter=500))
    if r2.success or True:
        p2 = r2.x[:-1]
        if f(p2) < f(p):
            p = p2
    return p, f(p) * scale


def main():
    results = {}
    try:
        results = json.load(open(OUT))
    except Exception:
        pass

    rows = TABLE if len(sys.argv) < 2 else [t for t in TABLE if str(t[0]) in sys.argv[1:]]
    for m, dthm_s, dcert_s, dup_s, *_ in rows:
        key = str(m)
        t_row = time.time()
        n = len(m)
        scale = float(dup_s.replace('e', 'E'))
        best_row = {}
        for a in sorted(set(m)):
            for s in (1, -1):
                c = a + s / 2
                for shape in (('R', 'C') if n >= 3 else ('R',)):
                    dH, coeffs = make_obj(m, c, shape)
                    base = natural_start(m, a, shape)
                    if shape == 'C':
                        base = np.concatenate(([0.05], base))
                    best = (None, np.inf)
                    starts = [base] + [base + rng.normal(0, sig, size=base.shape) * (1 + np.abs(base))
                                       for sig in (1e-3, 3e-3, 1e-2, 3e-2, 0.1) for _ in range(NPER)]
                    if shape == 'C':
                        starts += [np.concatenate(([yy], base[1:])) for yy in (0.0, 0.2, 0.5, 1.0)]
                    for p0 in starts:
                        if time.time() - t_row > TIME_CAP:
                            break
                        try:
                            p, val = optimise(dH, p0, scale)
                        except Exception:
                            continue
                        if np.isfinite(val) and val < best[1]:
                            best = (p, val)
                    if best[0] is not None:
                        best_row[f"{a}|{s}|{shape}"] = dict(a=a, s=s, shape=shape, params=[float(x) for x in best[0]],
                                                           value=float(best[1]))
                        print(f"{m} a={a} c={c} {shape}: best float max|dH| = {best[1]:.6e}", flush=True)
        results[key] = best_row
        json.dump(results, open(OUT, 'w'), indent=1)
        bk = min(best_row.values(), key=lambda d: d['value'])
        print(f"== {m}: best {bk['value']:.6e} at a={bk['a']} s={bk['s']} shape={bk['shape']} (printed {dup_s});"
              f" {time.time() - t_row:.0f}s", flush=True)


if __name__ == '__main__':
    main()
