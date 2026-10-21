import mpmath as mp
from fractions import Fraction
import sys
sys.path.insert(0,'/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/fixcheck-A/code')
mp.mp.dps=60
from sympy import bernoulli, factorial, Rational, symbols, series, sin
u=symbols('u'); NN=14
s=series(u/sin(u),u,0,2*NN+6).removeO()
sigma=[Rational(s.coeff(u,2*i)) for i in range(NN+4)]
def mphi(k,m): return Rational(1,4)*sum(sigma[k+1-n]*4**n*abs(bernoulli(2*n))/factorial(2*n)*(m**(2*n)-1) for n in range(1,k+2))
def p(l,m): return Rational(1,4**l)*sum(factorial(2*k)/(factorial(k)*factorial(l-k))*mphi(k,m) for k in range(l+1))
def b(l,m): return (-1)**l*p(l,m)/m
def alpha(k):
    return (-1)**k/(factorial(k)*4**k)*sum(Rational(factorial(k),factorial(l)*factorial(k-l))*(-4)**l*bernoulli(2*l,Rational(1,2)) for l in range(k+1))
print([alpha(k) for k in range(5)])
n=3; mu0=12; A0=mp.pi/2; D=mp.mpf('4.897')
def B0(t,l0):
    l0=mp.mpf(l0)
    if t> l0**2/(2*(1+l0)): return mp.inf
    return mp.pi*mp.e**(3*D)*l0*mp.e**(l0/2)/(A0*(1-mp.e**(-l0)))*(1+2*t/(l0-t))*mp.e**(-l0**2/(4*t))/mp.sqrt(4*mp.pi*t)
def delta(tau,N,eta,l0,rows=True):
    ts=[mp.mpf(tau)/2**k for k in range(N)]
    QN=max(mp.mpf(Rational(n-2,2)*abs(alpha(N))), n*mp.mpf(abs(b(N-1,mu0))))
    V=mp.matrix([[t**j for j in range(N)] for t in ts])
    Vi=V**-1
    err=[t*(eta+B0(t,l0)+QN*t**(N-1)) for t in ts]
    rb=max(sum(abs(Vi[j,k])*err[k] for k in range(N)) for j in range(3))
    ub=max(sum(abs(Vi[j,k]) for k in range(N)) for j in range(N))*max(err)
    return rb,ub
dthm=mp.mpf('3.80e-7'); dcert=mp.mpf('2.341e-3')
for l0 in ['1.8626','2.2567','1.1','0.01']:
    r,u_=delta(mp.mpf('1e-6'),3,0,l0); print('N=3 l0',l0,'row/tau',r/1e-6,'unif/tau',u_/1e-6)
def maxtau(N,target,l0,rows=True):
    lo,hi=mp.mpf('1e-14'),mp.mpf('0.2')
    for _ in range(200):
        mid=mp.sqrt(lo*hi)
        r,u_=delta(mid,N,0,l0)
        v=r if rows else u_
        if v<=target: lo=mid
        else: hi=mid
    return lo
def maxeta(tau,N,target,l0,rows=True):
    lo,hi=mp.mpf(0),mp.mpf(1)
    for _ in range(200):
        mid=(lo+hi)/2
        r,u_=delta(tau,N,mid,l0); v=r if rows else u_
        if v<=target: lo=mid
        else: hi=mid
    return lo
for l0 in ['1.8626','1.1','2.2567']:
    print('l0',l0)
    print(' N3 unif tau', mp.nstr(maxtau(3,dthm,l0,False),4),' eta@1e-11', mp.nstr(maxeta(mp.mpf('1e-11'),3,dthm,l0,False),4))
    print(' N3 rows tau', mp.nstr(maxtau(3,dthm,l0,True),4),' eta@1e-11', mp.nstr(maxeta(mp.mpf('1e-11'),3,dthm,l0,True),4))
    t1=maxtau(8,dthm,l0); t2=maxtau(8,dcert,l0)
    print(' N8 thm tau',mp.nstr(t1,4),' eta@tau/2',mp.nstr(maxeta(t1/2,8,dthm,l0),4))
    print(' N8 cert tau',mp.nstr(t2,4),' eta@tau/2',mp.nstr(maxeta(t2/2,8,dcert,l0),4),' smallest',mp.nstr(t2/128,3), mp.nstr(t2/256,3))
