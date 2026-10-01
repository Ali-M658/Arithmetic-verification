"""Independent derivation of the cone polynomials p_nu and smooth alpha_j
from the Selberg trace formula (elliptic and identity terms), heat kernel
h(r)=exp(-t(r^2+1/4)).  Elliptic term for order m:
  sum_k 1/(2 m sin th_k) int h(r) e^{-2 th_k r}/(1+e^{-2 pi r}) dr ,  th_k = pi k/m.
Moments: int r^{2j} e^{(pi-2th)r}/(2cosh pi r) dr = (1/2)(2j)! [x^{2j}] csc(th - x/2).
"""
import mpmath as mp
from fractions import Fraction
import sympy as sp
mp.mp.dps = 60
NU_MAX = 9

def cone_b(m, numax=NU_MAX):
    # coefficients of t^nu, nu=0..numax
    J = numax
    mom = [mp.mpf(0)]*(J+1)  # sum_k 1/(2 m s_k) * M_{2j}
    for k in range(1, m):
        th = mp.pi*k/m
        tay = mp.taylor(lambda x: 1/mp.sin(th - x/2), 0, 2*J)
        for j in range(J+1):
            mom[j] += 1/(2*m*mp.sin(th)) * mp.mpf(0.5)*mp.factorial(2*j)*tay[2*j]
    # series: e^{-t/4} * sum_j (-t)^j/j! mom_j
    s = [mom[j]*(-1)**j/mp.factorial(j) for j in range(J+1)]
    e = [(-mp.mpf(1)/4)**i/mp.factorial(i) for i in range(J+1)]
    return [sum(e[i]*s[nu-i] for i in range(nu+1)) for nu in range(J+1)]

def rat(x, maxden=10**15):
    f = Fraction(str(mp.nstr(x, 50))).limit_denominator(maxden)
    assert abs(mp.mpf(f.numerator)/f.denominator - x) < mp.mpf(10)**-35, (x, f)
    return f

def cone_polys(numax=NU_MAX):
    npts = numax + 4
    data = {m: cone_b(m, numax) for m in range(1, npts+2)}
    polys = []
    for nu in range(numax+1):
        K = nu+2
        ms = list(range(1, K+1))
        A = mp.matrix([[mp.mpf(m)**(2*k) for k in range(K)] for m in ms])
        y = mp.matrix([(-1)**nu*m*data[m][nu] for m in ms])
        c = mp.lu_solve(A, y)
        coeffs = [rat(c[k]) for k in range(K)]
        # verify at extra points
        for m in range(K+1, npts+2):
            val = sum(mp.mpf(cf.numerator)/cf.denominator*mp.mpf(m)**(2*k) for k, cf in enumerate(coeffs))
            assert abs(val - (-1)**nu*m*data[m][nu]) < mp.mpf(10)**-30, (nu, m)
        polys.append(coeffs)
    return polys

def alphas(jmax=NU_MAX+1):
    # int e^{-t(r^2+1/4)} r tanh(pi r) dr = (1/t) sum alpha_j t^j
    t = sp.symbols('t')
    ser = 1/t
    for j in range(jmax+1):
        s = 2*j+2
        mom = (1-sp.Integer(2)**(1-s))*sp.factorial(s-1)*sp.zeta(s)/(2*sp.pi)**s
        ser += -4*(-t)**j/sp.factorial(j)*sp.nsimplify(sp.simplify(mom))
    ser = sp.series(sp.exp(-t/4)*ser*t, t, 0, jmax+1).removeO()
    return [sp.Rational(ser.coeff(t, j)) for j in range(jmax+1)]

if __name__ == '__main__':
    al = alphas()
    print('alpha', al)
    P = cone_polys()
    for nu, c in enumerate(P):
        print(nu, c, 'p(1)=', sum(c))
    import pickle
    pickle.dump({'alpha': [Fraction(int(a.p), int(a.q)) for a in al], 'p': P}, open('cone.pkl', 'wb'))
