"""Exact checks of Theorem B system, Lemma S2.1 (det M), Lemma S2.2 (B = S M, det B), det N, D_I e."""
from common import *
from fractions import Fraction as F
import random, itertools
random.seed(1)
def prod(it):
    p = F(1)
    for x in it: p *= x
    return p
for n in range(2, 11):
    for trial in range(3):
        m = [F(random.randint(1, 60), random.randint(1, 7)) for _ in range(n)]
        if trial == 2 and n >= 3: m[1] = m[0]  # coincident orders
        e = e_of_m(m)
        I = I_of_m(m)
        assert I == I_of_e(e)
        M, b = Mb(I, n)
        Ms = sp.Matrix(M)
        assert Ms*sp.Matrix(e[1:]) == sp.Matrix(b), 'Theorem B fails'
        orl = prod(m[i]+m[j] for i in range(n) for j in range(i+1, n))
        detM = Ms.det()
        cn = detM*e[n]/orl
        assert cn == (-1)**(n*(n+1)//2), (n, cn)
        # Lemma S2.2
        E = lambda i: e[i] if 0 <= i <= n else 0
        B = sp.Matrix(n, n, lambda k, j: (-1)**(j+2)*E(2*k+1-(j+1)))
        S = sp.zeros(n, n)
        for k in range(n-1):
            for i in range(k+1):
                S[k, i] = E(2*(k-i))
        S[n-1, n-1] = (-1)**n*e[n]
        assert B == S*Ms, ('B != S M', n)
        assert B.det() == (-1)**(n*(n-1)//2)*orl
        # B as the map d -> W_D: check with a random D
        d = [F(random.randint(-9, 9)) for _ in range(n)]
        z, w = sp.symbols('z w')
        f = sp.expand(sp.prod([1+sp.Rational(x.numerator, x.denominator)*z for x in m]))
        Dp = sum(sp.Rational(d[k])*z**(k+1) for k in range(n))
        def EO(p):
            p = sp.Poly(p, z); cs = p.all_coeffs()[::-1]
            Ev = sum(c*w**(i//2) for i, c in enumerate(cs) if i % 2 == 0)
            Ov = sum(c*w**(i//2) for i, c in enumerate(cs) if i % 2 == 1)
            return Ev, Ov
        Ef, Of = EO(f); ED, OD = EO(Dp)
        W = sp.Poly(sp.expand(Ef*OD - ED*Of), w)
        Wc = [W.coeff_monomial(w**k) for k in range(n)]
        assert sp.Matrix(Wc) == B*sp.Matrix([sp.Rational(x) for x in d]), 'B is not d->W_D'
    print('n=%d: Thm B exact, det M = (-1)^{n(n+1)/2} Orl/e_n, B=SM, det B, W_D map: OK' % n)

# det N and D_I e = -M^{-1} N via symbolic differentiation for n=2..6
for n in range(2, 7):
    m = [F(random.randint(2, 30), random.randint(1, 3)) for _ in range(n)]
    e = e_of_m(m); I = I_of_m(m)
    syms = sp.symbols('x0:%d' % n)
    Ms, bs = Mb(list(syms), n)
    Fv = sp.Matrix(Ms)*sp.Matrix(e[1:]) - sp.Matrix(bs)
    Nm = Fv.jacobian(syms).subs(dict(zip(syms, I)))
    detN = Nm.det()
    assert detN == -e[n]/prod(F(2*j+1) for j in range(n-1)), n
    # D_I e via finite differences of the e<-I map (exact: D_eG inverse)
    es = sp.symbols('y1:%d' % (n+1))
    G = sp.Matrix(I_of_e([1]+list(es)))
    DG = G.jacobian(es).subs(dict(zip(es, e[1:])))
    M0 = sp.Matrix(Mb(I, n)[0])
    assert sp.simplify(DG.inv() + M0.inv()*Nm) == sp.zeros(n, n)
    print('n=%d: det N and D_I e = -M^{-1}N exact OK' % n)
