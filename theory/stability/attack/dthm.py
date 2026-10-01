"""Recompute delta_thm of Theorem S4 from the stated formula."""
from s2const import *
from fractions import Fraction as F
ELL = [F(2), F(14), F(498), F(4062), F(56230, 3), F(303654, 5)]
def lam(mu, n):
    return max([mu*ELL[0]] + [ELL[r]*F(mu)**(1-2*r) for r in range(1, n)])
def dthm(m, verbose=True):
    n = len(m); mu = max(m); k, _ = kappa(m); z = zeta(n); r = rho(m); L = lam(F(mu), n)
    vals = sorted(set(m)); terms = []
    for a in vals:
        ka = m.count(a)
        Q = 1
        for b in vals:
            if b != a: Q *= (abs(F(a-b))/mu)**m.count(b)
        terms.append(Q*2**(ka-1)/(3**n*(2*mu)**ka*2*k*r*L))
    t = [1/L, 1/(2*k*z*L), min(terms)]
    if verbose: print(m, 'lambda=%s kappa=%.5g zeta=%s rho=%.5g' % (L, float(k), z, float(r)), ' terms=', ['%.4g' % float(x) for x in t], ' delta_thm=%.4g' % float(min(t)))
    return min(t)
for m in [(2,8,8), (3,3,12), (3,10,15,30), (4,5,21,28)]:
    dthm(list(m))
