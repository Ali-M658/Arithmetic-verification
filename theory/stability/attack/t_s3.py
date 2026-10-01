"""Adversarial tests of Lemma S3 (e-space) and Theorem S3 (data space) at the edge of their hypotheses."""
import numpy as np, itertools, math
from scipy.optimize import differential_evolution
from fractions import Fraction as F
from dthm import *
rng = np.random.default_rng(3)
def clusters(mh):
    vals = sorted(set(mh)); out = []
    for a in vals:
        k = mh.count(a); others = [b for b in vals if b != a]
        g = min([abs(a-b) for b in others], default=math.inf)
        Q = np.prod([abs(a-b)**mh.count(b) for b in others]) if others else 1.0
        out.append((a, k, g, Q))
    return out
def kth_dist(roots, a, k):
    d = np.sort(np.abs(roots - a)); return d[k-1], (d[k] if k < len(d) else 1e6)
# ---------- Lemma S3 in e-space ----------
print('Lemma S3, adversarial e-perturbations: worst (k-th nearest root distance)/r_a  [must be <1]  and (k+1)-th/r_a [must be >=1]')
for m in [(2,8,8), (3,3,12), (2,2,2), (1,1,100), (2,2,50,50), (5,5,5,5), (1,2,2,2,3), (3,3,3,9,9,10), (1,1,1,1,1,1)]:
    n = len(m); mu = max(m); mh = [x/mu for x in m]
    e = np.array([float(x) for x in e_of_m([F(x, mu) for x in m])])
    worst = 0; worst2 = np.inf
    for (a, k, g, Q) in clusters(mh):
        # largest eps allowed: r_a(eps) <= min(g,1)/2
        rmax = min(g, 1)/2
        epsmax = rmax**k*Q/(2**(1-k)*3**n)
        for eps in [epsmax, epsmax*1e-3]:
            ra = (2**(1-k)*3**n*eps/Q)**(1/k)
            def obj(v):
                v = np.clip(np.nan_to_num(np.asarray(v, float)), -1, 1); ee = e.copy(); ee[1:] += eps*v
                r = np.roots([(-1)**j*ee[j] for j in range(n+1)])
                d1, d2 = kth_dist(r, a, k); return d1/ra, d2/ra
            cands = list(itertools.product([-1, 1], repeat=n)) + list(rng.uniform(-1, 1, (3000, n)))
            vals = [obj(v) for v in cands]
            res = differential_evolution(lambda v: -obj(v)[0], [(-1, 1)]*n, seed=0, maxiter=150, popsize=25, tol=1e-12)
            res2 = differential_evolution(lambda v: obj(v)[1], [(-1, 1)]*n, seed=0, maxiter=150, popsize=25, tol=1e-12)
            w1 = max(max(v[0] for v in vals), -res.fun); w2 = min(min(v[1] for v in vals), res2.fun)
            worst = max(worst, w1); worst2 = min(worst2, w2)
            print('  m=%s a=%.4g k=%d eps=%.3g: max kth/r_a=%.4f  min (k+1)th/r_a=%.4f' % (m, a, k, eps, w1, w2))
print('overall worst', worst, worst2)
