from common import *
from fractions import Fraction as F
import numpy as np, itertools
from fast import Fast
# kappa_r for (2,8,8)
m = [F(2), F(8), F(8)]; n = 3
fr = Front(n); H = H_cone(m); I = I_of_m(m)
for r in range(n):
    print('kappa_r', r, float(sum(abs(fr.Linv[r, c])*abs(H[c]) for c in range(n))/abs(I[r])))
# zeta_n with rows j<=n-2 only vs j<=n-1
from s2const import sigma
for nn in range(3, 7):
    s = sigma(nn, 2*nn)
    def z(jmax):
        return max([F(1)] + [sum(F(str(s[2*i+1])) for i in range(j) if 2 <= 2*j-2*i <= nn) for j in range(jmax+1)])
    print('n=%d zeta (rows j<=n-2, the rows of M) = %s ; zeta (j<=n-1, as used in delta_thm) = %s' % (nn, z(nn-2), z(nn-1)))
# dense grid on the delta_cert box (n=3) and full mp check of the best point
TABLE = {(2,8,8): 2.342e-03, (3,3,12): 4.040e-03, (3,10,15,30): 3.660e-03, (4,5,21,28): 1.462e-03}
for mm, dc in TABLE.items():
    fs = Fast(mm); nn = len(mm)
    g = np.linspace(-1, 1, 41 if nn == 3 else 17)
    best = (0, None)
    for v in itertools.product(g, repeat=nn):
        f = fs.F(dc*np.array(v))
        if f > best[0]: best = (f, v)
    H0 = H_cone([F(x) for x in mm])
    Hm = [mp.mpf(H0[i].numerator)/H0[i].denominator + mp.mpf(dc)*best[1][i] for i in range(nn)]
    roots = recover(Hm, nn, Front(nn), dps=60)
    ok, dev = rounds_ok(roots, mm)
    print(mm, 'grid max deviation %.6f at %s; mp recheck: rounding ok=%s dev=%.6f' % (best[0], np.round(best[1], 3), ok, dev))
