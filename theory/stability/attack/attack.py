"""Adversarial search for rounding failures inside |dH_nu|<=delta_cert."""
import numpy as np, itertools, sys
from scipy.optimize import differential_evolution, minimize
from fast import Fast
TABLE = {(2,8,8): (2.342e-03, 2.485e-03), (3,3,12): (4.040e-03, 4.588e-03),
         (3,10,15,30): (3.660e-03, 7.487e-03), (4,5,21,28): (1.462e-03, 2.018e-03)}
rng = np.random.default_rng(0)
def maxF(fs, delta, seeds=3):
    n = fs.n; best = (0, None)
    for v in itertools.product([-1, 1], repeat=n):
        v = np.array(v, float); f = fs.F(delta*v)
        if f > best[0]: best = (f, delta*v)
    for _ in range(4000):
        v = rng.uniform(-1, 1, n); f = fs.F(delta*v)
        if f > best[0]: best = (f, delta*v)
    for s in range(seeds):
        res = differential_evolution(lambda v: -fs.F(delta*v), [(-1, 1)]*n, seed=s, maxiter=200, popsize=30, tol=1e-12, polish=True)
        if -res.fun > best[0]: best = (-res.fun, delta*res.x)
    return best
for m, (dc, du) in TABLE.items():
    fs = Fast(m)
    print('m=', m, 'H=', fs.H, 'rel dc/|H|=', np.round(dc/np.abs(fs.H), 9))
    f, x = maxF(fs, dc)
    print('  at delta_cert: max deviation of sorted real parts = %.6f (fail iff >=0.5); argmax dH/delta=%s; roots=%s' % (f, np.round(x/dc, 4), fs.roots(x)))
    # bisection for empirical threshold
    lo, hi = dc*0.5, du*1.5
    if maxF(fs, hi, seeds=1)[0] < 0.5: hi = du*4
    for it in range(22):
        mid = (lo+hi)/2
        if maxF(fs, mid, seeds=1)[0] >= 0.5: hi = mid
        else: lo = mid
    f, x = maxF(fs, hi, seeds=1)
    print('  empirical threshold in [%.6e, %.6e]; delta_cert=%.4e delta_up=%.4e; failing dH/delta=%s roots=%s' % (lo, hi, dc, du, np.round(x/hi, 4), fs.roots(x)), flush=True)
