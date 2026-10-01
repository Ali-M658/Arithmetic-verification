from common import *
from fractions import Fraction as F
import random
N = 8
L = Lmat(N); Li = L.inv()
print('L^{-1} first 5 rows:')
for r in range(5): print([str(Li[r,c]) for c in range(r+1)])
print('diag 1/|L_rr|:', [str(abs(1/L[r,r])) for r in range(N)])
print('ell_r:', [str(sum(abs(Li[r,c]) for c in range(N))) for r in range(N)])
# check L I + h0 equals cone evaluation
for trial in range(20):
    n = random.randint(3, 8)
    m = [F(random.randint(2, 40)) if random.random()<.5 else F(random.randint(5,90), random.randint(1,4)) for _ in range(n)]
    I = [sum(1/x for x in m)] + [sum(x**(2*l-1) for x in m) for l in range(1, n)]
    H = Lmat(n)*sp.Matrix(I) + h0(n)
    assert list(H) == H_cone(m), m
print('L I + h0 == cone sum OK')
