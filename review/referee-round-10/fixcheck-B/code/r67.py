import sympy as sp, mpmath as mp, itertools, sys
sys.path.insert(0,'.')
from consts import b_l, alpha, a_l
from gaps import sig
mp.mp.dps=40
S=sig(sp.Rational(1,4),12)
from fractions import Fraction as F
def c(j,g,ms,s):
    s=sp.Rational(s.numerator,s.denominator)
    if j==1: return s/2
    return alpha(j-1)*s/2+sum(b_l(j-2,m) for m in ms)
cache={}
best={};maxk=0
for (g1,m1,s1),(g2,m2,s2) in itertools.combinations(S,2):
    for j in range(1,6):
        d=c(j,g1,m1,s1)-c(j,g2,m2,s2)
        if d!=0: break
    maxk=max(maxk,j)
    if j not in best or abs(d)<best[j][0]: best[j]=(abs(d),(m1,m2))
print('max first-diff index',maxk); print(best)
# t1 with exact data
A=mp.pi/2; ns=4; M=12
Q=lambda K: A/(4*mp.pi)*abs(mp.mpf(sp.N(alpha(K+1),50)))+ns*abs(mp.mpf(sp.N(b_l(K,M),50)))
t1=min(mp.mpf(1),min(mp.mpf(sp.N(best[k][0],50))/(4*Q(k-1)) for k in best))
print('t1 exact data',t1)
# alpha moment form vs closed form k<=10
def mu(k): return (1-sp.Rational(1,2**(2*k+1)))*(-1)**k*sp.bernoulli(2*k+2)/(k+1)
def alpha_mom(k): return sp.Rational(-1,4)**k/sp.factorial(k)-sum((-1)**j*mu(j)/sp.factorial(j)*sp.Rational(-1,4)**(k-1-j)/sp.factorial(k-1-j) for j in range(k))
print('alpha agree k<=10:',all(sp.simplify(alpha_mom(k)-alpha(k))==0 for k in range(0,11)), [alpha(k) for k in range(5)])
# numeric check of mu
print(mp.nstr(4*mp.quad(lambda r:r**3/(mp.e**(2*mp.pi*r)+1),[0,mp.inf]),15), sp.N(mu(1),15))
h7=mp.acosh(1/(2*mp.sin(mp.pi/7))); print('c1',0.25+mp.pi**2/h7**2,'Lam2',0.25+4*mp.pi**2/h7**2,'h7',h7)
print('l23',2*mp.asinh(mp.sqrt(1/(4*(1+mp.mpf(3)/4*mp.cosh(2*mp.acosh(2/mp.sqrt(3)))**2)))))
