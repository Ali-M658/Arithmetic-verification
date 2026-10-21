# Recompute Tables 4 (N, delta, Lambda_o, B*, Lambda t, Weyl ratio) and 6 (Thm 6.2 constants)
import mpmath as mp, sympy as sp
from math import gcd
from functools import reduce
mp.mp.dps=60
u=sp.symbols('u')
SIG=sp.series(u/sp.sin(u),u,0,60).removeO()
def sigma(i): return SIG.coeff(u,2*i)
def mphi(k,m):  # m*phi_k(m)
    return sp.Rational(1,4)*sum(sigma(k+1-n)*4**n*abs(sp.bernoulli(2*n))/sp.factorial(2*n)*(m**(2*n)-1) for n in range(1,k+2))
def p_l(l,m): return sum(sp.factorial(2*k)/(sp.factorial(k)*sp.factorial(l-k))*mphi(k,m) for k in range(l+1))/4**l
def b_l(l,m): return (-1)**l*p_l(l,m)/m
def alpha(k):
    return (-1)**k/(sp.factorial(k)*4**k)*sum(sp.binomial(k,l)*(-4)**l*sp.bernoulli(2*l,sp.Rational(1,2)) for l in range(k+1))
def a_l(l): return abs(sp.bernoulli(2*l+2))/(2*sp.factorial(l+1)*(2*l+1))
def Cstar(A,eps,M):
    A=mp.mpf(A);eps=mp.mpf(eps)
    d0=min(eps/2, mp.acosh(1+2/(mp.pi**2*M**2)))
    r0=d0/2; rho1=mp.asinh(mp.sinh(r0)*mp.sin(mp.pi/M))
    v0=2*mp.pi*min((mp.cosh(r0)-1)/M, mp.cosh(rho1)-1)
    return A*M*mp.e**(10*r0+rho1)/(2*v0*(mp.cosh(rho1)-1))
def nstar(A): return int(mp.floor(A/mp.pi))+4
def Zs(A,M,s): ns=nstar(A); return mp.mpf(A)/(4*mp.pi*s)+ns*mp.mpf(M**2-1)/(12*M)+1
def varpi(A,eps,M):
    eps=mp.mpf(eps); return 3*Cstar(A,eps,M)*eps*mp.e**(eps/2)/((1-mp.e**(-eps))*mp.sqrt(4*mp.pi))
def Bstar(A,eps,M,t): eps=mp.mpf(eps); return varpi(A,eps,M)*t**-0.5*mp.e**(-eps**2/(4*t))
def NLd(A,M,t,Th):
    t=mp.mpf(t);Th=mp.mpf(Th)
    Lam=2/t*mp.log(8*Zs(A,M,t/2)/Th)
    x=mp.e*Zs(A,M,1/Lam); N=int(mp.floor(x))+1
    return Lam,N,Th/(8*mp.e*N*t),x
def thm62(A,eps,M):
    A=mp.mpf(A);eps=mp.mpf(eps)
    ns=nstar(A);ks=min(ns,M)
    LM=reduce(lambda x,y:x*y//gcd(x,y),range(1,M+1))
    d={1:sp.Rational(1,2*min(LM,M**(2*ns)))}
    for k in range(2,ks+1): d[k]=a_l(k-2)
    gam=min(d.values())
    Q=lambda K: A/(4*mp.pi)*abs(mp.mpf(sp.N(alpha(K+1),70)))+ns*abs(mp.mpf(sp.N(b_l(K,M),70)))
    vals={k:mp.mpf(sp.N(d[k],70))/(4*Q(k-1)) for k in range(1,ks+1)}
    t1=min(mp.mpf(1),min(vals.values())); kmin=min(vals,key=vals.get)
    t2=eps**2/(2*(1+eps)); p=ks-mp.mpf(3)/2; w=varpi(A,eps,M); g=mp.mpf(sp.N(gam,70))
    y0=2*(mp.log(16*w/g)+p*mp.log(4/eps**2)+p*mp.log(2*p/mp.e))
    t3=eps**2/(4*max(y0,1)); ts=min(t1,t2,t3)
    binds='t1' if ts==t1 else ('t2' if ts==t2 else 't3')
    Th=g/2*ts**(ks-2)
    Lam,N,dl,x=NLd(A,M,ts,Th)
    return dict(ks=ks,C=Cstar(A,eps,M),t1=t1,t3=t3,Th=Th,Lam=Lam,N=N,d=dl,binds=binds,kmin=kmin,x=x)
pi=mp.pi
if __name__=='__main__':
    print("Table 4/5 rows")
    rows=[(pi/2,'1.8626',8,'0.025643','0.01588'),(pi/2,'1.8626',12,'0.02482','0.006527'),
          (4*pi/3,'2.633915',3,'0.08524','0.1520'),(4*pi/3,'0.693994',3,'0.0060028','0.1655'),
          (4*pi/3,'0.693994',12,'0.0034221','0.001373'),(2*pi,'0.1',3,'0.000092402','0.1666')]
    for A,e,M,t,Th in rows:
        Lam,N,dl,x=NLd(A,M,t,Th); t_=mp.mpf(t)
        B=Bstar(A,e,M,t_); t2=mp.mpf(e)**2/(2*(1+mp.mpf(e)))
        Lo=mp.log(8/mp.mpf(Th))/t_
        print(M,e,'N',N,'frac',mp.nstr(x-mp.floor(x),3),'delta',mp.nstr(dl,6),'Lo',mp.nstr(Lo,6),'B*',mp.nstr(B,6),'Th/8',mp.mpf(Th)/8,'Lt',mp.nstr(Lam*t_,5),'t<=t2',t_<=t2,'Weyl ratio',mp.nstr(N/(A*Lam/(4*pi)),4),'Nd',mp.nstr(N*dl,4))
    print("Table 6")
    for A,e,M in [(pi/2,'1.8626',8),(pi/2,'1.8626',12),(4*pi/3,'2.6339',3),(4*pi/3,'0.6939',3),(4*pi/3,'0.6939',12),(2*pi,'0.1',3),(10*pi,'1',3),(10*pi,'1',12)]:
        r=thm62(A,e,M)
        print(M,e,{k:(mp.nstr(v,6) if isinstance(v,mp.mpf) else v) for k,v in r.items()})
