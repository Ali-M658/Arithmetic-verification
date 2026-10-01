"""Theorem S3 / S4 in data space at the largest delta allowed by the hypotheses (vertices + random, mpmath)."""
import itertools, random, math
from dthm import *
mp.mp.dps = 80
random.seed(5)
def S3_test(m, nrand=150):
    m = list(m); n = len(m); mu = max(m)
    k, _ = kappa(m); z = zeta(n); r = rho(m); L = lam(F(mu), n)
    vals = sorted(set(m))
    info = []
    for a in vals:
        ka = m.count(a); others = [b for b in vals if b != a]
        g = min([F(abs(a-b), mu) for b in others], default=F(10**9))
        Q = 1
        for b in others: Q *= (F(abs(a-b), mu))**m.count(b)
        info.append((a, ka, g, Q))
    # largest delta satisfying all hypotheses
    cands = [1/L, 1/(2*k*z*L)]
    for (a, ka, g, Q) in info:
        cands.append((min(g, 1)/2)**ka*Q/(2**(2-ka)*3**n*k*r*L))
    dmax = float(min(cands))
    fr = Front(n); H0 = H_cone([F(x) for x in m])
    worst = 0
    for delta in [dmax, dmax*1e-4]:
        dirs = list(itertools.product([-1, 1], repeat=n)) + [[random.uniform(-1, 1) for _ in range(n)] for _ in range(nrand)]
        for v in dirs:
            H = [mp.mpf(H0[i].numerator)/H0[i].denominator + mp.mpf(delta)*v[i] for i in range(n)]
            roots = recover(H, n, fr, dps=80)
            for (a, ka, g, Q) in info:
                ra = mu*(2**(2-ka)*3**n*float(k)*float(r)*float(L)*delta/float(Q))**(1/ka)
                d = sorted(float(abs(x - a)) for x in roots)
                cnt = sum(1 for x in d if x < ra)
                assert cnt == ka, ('S3 VIOLATED', m, a, delta, v, roots)
                worst = max(worst, d[ka-1]/ra)
    print(m, 'delta_max(S3 hyp)=%.3e  worst kth-root-distance/r_a = %.4f  (count always = k_a)' % (dmax, worst), flush=True)
for m in [(2,8,8), (3,3,12), (2,2,2), (3,10,15,30), (4,5,21,28), (2,2,50,50), (3,3,3,9,9,10), (2,3,1000), (5,5,5,5)]:
    S3_test(m)
