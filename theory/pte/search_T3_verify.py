"""Exact verification of search_T3.c candidates: rebuild the cubic for U from V exactly and factor it.
Prints EXACT lines for genuine size-8 genus collisions (none found) and a count."""
import sys, sympy as sp
from fractions import Fraction as F
t=sp.symbols('t')
n=0
for line in sys.stdin:
    if not line.startswith('V'): continue
    V=list(map(int,line.split()[1:6]))
    S=sum(V); C=sum(v**3 for v in V); R=sum(F(1,v) for v in V)
    e3=F(C-S**3)/(3*(1-S*R)); e2=R*e3
    P=sp.Poly(t**3-S*t**2+sp.Rational(e2.numerator,e2.denominator)*t-sp.Rational(e3.numerator,e3.denominator),t)
    lin=[f for f,_ in P.factor_list()[1] if f.degree()==1]
    if sum(_ for f,_ in P.factor_list()[1] if f.degree()==1)==3 or len(lin)==3:
        print("EXACT", V, P.factor_list()); n+=1
print("exact splits:",n)
