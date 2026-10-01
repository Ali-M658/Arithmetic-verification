"""Adversarial test of Theorem S2(b) and of the majorant |dT_k|<=eta sigma_k(n)."""
from s2const import *
import itertools, random
from scipy.optimize import differential_evolution
mp.mp.dps = 40
random.seed(0)
def worst(m, eta, tries=0):
    n = len(m); mu, mh = scaled(m)
    I0 = [mp.mpf(x.numerator)/x.denominator for x in I_of_m(mh)]
    e0 = [mp.mpf(x.numerator)/x.denominator for x in e_of_m(mh)]
    T0 = T_of_I(I0, n)
    s = [float(x) for x in sigma(n, 2*n)]
    def ratio(dv):
        I = [I0[i] + eta*dv[i] for i in range(n)]
        try:
            e = recover_e(I, n)
        except ZeroDivisionError:
            return 1e9, 0
        err = max(abs(e[k]-e0[k]) for k in range(1, n+1))
        T = T_of_I(I, n)
        maj = max(abs(T[k]-T0[k])/(eta*s[k]) for k in range(1, 2*n-2, 2))
        return float(err), float(maj)
    k, _ = kappa(m); r = rho(m); bound = 2*float(k)*float(r)*eta
    best = (0, None); bestmaj = 0
    cands = list(itertools.product([-1, 1], repeat=n)) + [[random.uniform(-1, 1) for _ in range(n)] for _ in range(tries)]
    for v in cands:
        err, maj = ratio(v)
        if err/bound > best[0]: best = (err/bound, v)
        bestmaj = max(bestmaj, maj)
    res = differential_evolution(lambda v: -ratio(v)[0]/bound, [(-1, 1)]*n, maxiter=40, popsize=15, seed=1, tol=1e-10, polish=True)
    return best[0], -res.fun, bestmaj
for m in [(2,8,8), (3,3,12), (2,2,2), (1,1,100), (2,3,1000), (3,10,15,30), (4,5,21,28), (2,2,50,50), (1,1,1,1,1), (2,3,3,7,9), (1,1,30,31,40), (2,2,2,2,2,2), (2,2,9,9,30,31), (1,2,100,100,100,100)]:
    n = len(m); k, _ = kappa(m); z = zeta(n)
    etamax = min(1.0, 0.5/(float(k)*float(z)))
    out = []
    for eta in [etamax, etamax*1e-2, etamax*1e-5]:
        v, de, maj = worst(m, eta, tries=200)
        out.append('eta=%.2e: vert/rand %.3g, DE %.3g, maj %.3g' % (eta, v, de, maj))
    print(m, ' | '.join(out), flush=True)
