"""Prop S3.2 (sharpness) and Remark S3.3."""
from common import *
from fractions import Fraction as F
import random
mp.mp.dps = 60
def Hvec(e, n):
    I = I_of_e(e)
    return Lmat(n)*sp.Matrix(I) + h0(n)
def ratio_double(m, a, ss):
    n = len(m); base = Hvec(e_of_m([F(x) for x in m]), n)
    out = []
    for s in ss:
        mm = list(m); i = mm.index(a); j = mm.index(a, i+1)
        mm[i] = F(a) + s; mm[j] = F(a) - s
        d = Hvec(e_of_m(mm), n) - base
        out.append(float(s)/float(max(abs(x) for x in d))**0.5)
    return out
print('(i) double order: s/||dH||^{1/2}')
for m, a in [((2,8,8), 8), ((3,3,12), 3), ((3,3,4,4), 3), ((3,3,4,4), 4)]:
    print('  ', m, 'split', a, ['%.5f' % x for x in ratio_double(m, a, [F(1, 10**k) for k in (2, 4, 6)])])
# exact Delta for (2,8,8)
s = sp.symbols('s')
mm = [8+s, 8-s, 2]
R = sum(1/x for x in mm); P3 = sum(x**3 for x in mm); P1 = sum(mm)
print('  (2,8,8): dR=', sp.simplify(R - sp.Rational(3, 4)), ' dP1=', sp.simplify(P1-18), ' dP3=', sp.expand(P3 - 1032))
print('  claimed dR = 2s^2/(8(64-s^2)) equal?', sp.simplify(R - sp.Rational(3, 4) - 2*s**2/(8*(64-s**2))) == 0)
print('(ii) k-fold: q_s=((z-a)^k - s^k) g ; ratio s/||dH||^{1/k}, and recovered roots distance')
def poly_e(roots_poly):
    # roots_poly: sympy poly in z, monic; return e list with q = sum (-1)^j e_j z^{n-j}
    z = sp.symbols('z'); c = sp.Poly(roots_poly, z).all_coeffs()
    return [F(str((-1)**j*c[j])) for j in range(len(c))]
z = sp.symbols('z')
for m, a, k in [((4,4,4), 4, 3), ((7,7,7), 7, 3), ((2,2,2,3), 2, 3), ((5,5,5,5), 5, 4)]:
    n = len(m); g = sp.prod([z-x for x in m if x != a])
    base = Hvec(e_of_m([F(x) for x in m]), n)
    rs = []
    for sv in [sp.Rational(1, 10**2), sp.Rational(1, 10**3), sp.Rational(1, 10**4)]:
        q = sp.expand(((z-a)**k - sv**k)*g)
        e = poly_e(q)
        d = Hvec(e, n) - base
        rs.append(float(sv)/float(max(abs(x) for x in d))**(1/k))
        # recovery from exact data
        I = I_of_e(e); er = recover_e(I, n, exact=True)
        assert [F(str(x)) for x in er[1:]] == e[1:]
    print('  ', m, 'k=%d' % k, ['%.5f' % x for x in rs], 'recovery returns q_s exactly: yes')
print('Remark S3.3: random + adversarial real perturbations near (a,a,a)')
worst = 0
random.seed(2)
for trial in range(20000):
    a = random.choice([2, 3, 5, 10, 50])
    sc = 10**random.uniform(-6, 0)
    d = [random.uniform(-1, 1)*a*sc for _ in range(3)]
    if trial % 3 == 0: d = [-a*0.999*sc, a*sc*random.uniform(-1,1), -a*0.999]  # push to d=-a edge
    mmv = [a+x for x in d]
    lhs = sum(x**3 for x in mmv) - 3*a*a*sum(mmv) - (3*a**3 - 9*a**3)
    bound = (abs(lhs)/(2*a))**0.5
    worst = max(worst, max(abs(x) for x in d)/bound)
print('  max over trials of max|d_i| / sqrt(|dP3-3a^2 dP1|/(2a)) =', worst, '(must be <=1)')
