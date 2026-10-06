"""search_dup_deep: deeper NUMERICAL search (not a certificate) for the (2,2,2,2,3) row (and any row given on the
command line). Starting points are random root configurations of g: the remaining orders perturbed into real
roots or complex-conjugate pairs at distance up to 0.7 (cluster splittings), with y random for the complex shape.
Writes dup_candidates_deep.json; check_dup.py verifies these candidates exactly too.
"""
import json, sys, time
import numpy as np
from search_dup import make_obj, optimise
from rows_table import TABLE

rng = np.random.default_rng(777)
OUT = 'dup_candidates_deep.json'
NSTART = int(sys.argv[1]) if len(sys.argv) > 1 else 150
targets = sys.argv[2:] or ['(2, 2, 2, 2, 3)']
try:
    res = json.load(open(OUT))
except Exception:
    res = {}


def random_roots(rest):
    rest = list(rest)
    out = []
    while rest:
        b = rest.pop()
        if rest and rng.random() < 0.5:
            b2 = rest.pop()
            mid = (b + b2) / 2 + rng.normal(0, 0.2)
            y = abs(rng.normal(0, 0.4))
            out += [complex(mid, y), complex(mid, -y)]
        else:
            out.append(b + rng.normal(0, 0.25))
    return out


for m, dthm_s, dcert_s, dup_s, *_ in [t for t in TABLE if str(t[0]) in targets]:
    n = len(m)
    mu = float(max(m))
    scale = float(dup_s.replace('e', 'E'))
    key = str(m)
    res.setdefault(key, {})
    t0 = time.time()
    for a in sorted(set(m)):
        for s in (1, -1):
            for shape in ('R', 'C'):
                dH, _ = make_obj(m, a + s / 2, shape)
                rest = list(m); rest.remove(a)
                if shape == 'C':
                    rest.remove(a if a in rest else min(rest, key=lambda b: abs(b - a)))
                best = (None, np.inf)
                for it in range(NSTART):
                    g = np.real(np.poly(random_roots(rest)))
                    p0 = g[1:] / mu ** np.arange(1, len(g))
                    if shape == 'C':
                        p0 = np.concatenate(([abs(rng.normal(0, 0.4))], p0))
                    try:
                        p, val = optimise(dH, p0, scale)
                    except Exception:
                        continue
                    if np.isfinite(val) and val < best[1]:
                        best = (p, val)
                kk = f"{a}|{s}|{shape}"
                res[key][kk] = dict(a=a, s=s, shape=shape, params=[float(x) for x in best[0]], value=float(best[1]))
                json.dump(res, open(OUT, 'w'), indent=1)
                print(f"{m} a={a} c={a + s / 2} {shape}: best float {best[1]:.6e}  ({time.time() - t0:.0f}s)", flush=True)
