from fractions import Fraction as F
from sympy import bernoulli, factorial, Rational, symbols, series, sin, cot, simplify
import math
# phi_k(m) via (4): m phi_k = 1/4 sum_{n=1}^{k+1} sigma_{k+1-n} 4^n|B2n|/(2n)! (m^{2n}-1)
u=symbols('u')
N=12
s=series(u/sin(u),u,0,2*N+4).removeO()
sigma=[Rational(s.coeff(u,2*i)) for i in range(N+3)]
def mphi(k,m):
    return Rational(1,4)*sum(sigma[k+1-n]*4**n*abs(bernoulli(2*n))/factorial(2*n)*(m**(2*n)-1) for n in range(1,k+2))
def p(l,m):
    return Rational(1,4**l)*sum(factorial(2*k)/(factorial(k)*factorial(l-k))*mphi(k,m) for k in range(l+1))
def b(l,m): return (-1)**l*p(l,m)/m
print([float(abs(b(l,12))) for l in range(7)])
# triangle c2 checks
print('p0..',[p(l,symbols('m')).expand() for l in range(3)])
