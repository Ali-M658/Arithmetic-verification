"""
Independent derivation of the quadratic (lambda^2) part of the heat-trace coefficients of
g_lambda = e^{2 lambda psi}|dx|^2 on R^2, relative to flat space, via the second-order Duhamel
form factor in Fourier space.  Exact (sympy).

Convention here: P := -(d1^2 + d2^2) >= 0 (the positive flat Laplacian, = Delta_0 in the
convention Delta = -div grad).  Delta_g = e^{-2 sigma} P, sigma = lambda psi.
Write Delta_g = P + V, V = w P, w = e^{-2 sigma} - 1 = -2 sigma + 2 sigma^2 + O(sigma^3).
  Tr e^{-t(P+V)} - Tr e^{-tP} = -t Tr(V e^{-tP}) + (t^2/2) int_0^1 Tr(V e^{-stP} V e^{-(1-s)tP}) ds + O(V^3)
  -t Tr(V e^{-tP}) = -(1/(4 pi t)) int w      (only t^{-1})
  second order    = (t^2/2) int_0^1 ds int |w^(k)|^2 dk/(2pi)^2  I(t,s,k),
  I = int |eta|^2 |eta+k|^2 exp(-ts|eta|^2 - t(1-s)|eta+k|^2) d eta/(2 pi)^2.
Parseval: int |psi^(k)|^2 |k|^{2n} dk/(2pi)^2 = int psi P^n psi dx.
Result: coefficient G_n with  t^{n-1}-coefficient = lambda^2 G_n int psi P^n psi dx.
"""
import sympy as sp

t, s, kap = sp.symbols('t s kappa', positive=True)
x1, x2 = sp.symbols('xi1 xi2', real=True)

# shift eta = xi - (1-s)k, k = (kappa, 0): exponent = t|xi|^2 + t s(1-s) kappa^2
eta2 = (x1 - (1 - s) * kap)**2 + x2**2
etak2 = (x1 + s * kap)**2 + x2**2
poly = sp.Poly(sp.expand(eta2 * etak2), x1, x2)


def gmom(p, q):
    # int xi1^p xi2^q e^{-t|xi|^2} dxi / (2pi)^2
    if p % 2 or q % 2:
        return 0
    return sp.gamma(sp.Rational(p + 1, 2)) * sp.gamma(sp.Rational(q + 1, 2)) / t**sp.Rational(p + q + 2, 2) / (4 * sp.pi**2)


Ipre = sp.expand(sum(cf * gmom(p, q) for (p, q), cf in poly.terms()))
NMAX = 9
# expand exp(-t s(1-s) kappa^2) to order needed
expo = sum((-t * s * (1 - s) * kap**2)**j / sp.factorial(j) for j in range(NMAX + 2))
second = sp.expand(t**2 / 2 * Ipre * expo)
second = sp.integrate(second, (s, 0, 1))
second = sp.expand(4 * second)  # |w^|^2 = 4 lambda^2 |psi^|^2 at order lambda^2

G = {}
for l in range(-1, NMAX):
    coeff = sp.expand(second.coeff(t, l))
    # must be a single power kappa^{2(l+1)}
    P = sp.Poly(coeff, kap)
    G[l + 1] = P
print('t^{-1} part of the 2nd-order Duhamel term (coefficient of lambda^2 int psi^2):', G[0].as_expr())
# consistency check of the t^{-1} term: total lambda^2 part = second-order + first-order(-(1/4pi t) int 2 lambda^2 psi^2)
# = area term (1/4pi t) int (e^{2 sigma}-1) -> lambda^2: (1/4pi t) 2 int psi^2.
tot_m1 = G[0].as_expr() - 2 / (4 * sp.pi)   # first-order term contributes -(1/4pi)*int(2 psi^2)
assert sp.simplify(tot_m1 - 2 / (4 * sp.pi)) == 0
print('t^{-1}: lambda^2 coefficient = 2/(4pi) int psi^2 = area term: OK')
# t^0: must vanish (Gauss-Bonnet: int K dA topological)
assert G[1].as_expr() == 0 or sp.simplify(G[1].as_expr()) == 0
print('t^0: quadratic part 0 (Gauss-Bonnet): OK')

F = lambda n: sp.Integer(-1)**n * n * (n - 1) * sp.factorial(n) / sp.factorial(2 * n + 1)
out = []
for n in range(2, NMAX + 1):
    P = G[n]
    assert P.monoms() == [(2 * n,)], (n, P)
    Gn = sp.nsimplify(P.coeffs()[0])
    claim_if_minusDelta0_is_P = F(n) / (2 * sp.pi)                 # (-Delta_0)^n = P^n
    claim_if_minusDelta0_is_minusP = F(n) * (-1)**n / (2 * sp.pi)   # (-Delta_0)^n = (-P)^n
    out.append((n, Gn, Gn * 2 * sp.pi))
    print('n=%d: G_n = %s ;  2 pi G_n = %s ; F_n = %s ; matches F_n with (-Delta_0)=P(>=0): %s ; with (-Delta_0)=-P: %s'
          % (n, Gn, sp.simplify(Gn * 2 * sp.pi), F(n), sp.simplify(Gn - claim_if_minusDelta0_is_P) == 0,
             sp.simplify(Gn - claim_if_minusDelta0_is_minusP) == 0))
    assert sp.simplify(Gn - claim_if_minusDelta0_is_P) == 0

# Berger: (4pi)^{-1} int u_2 dA, u_2 = K^2/15 - Delta K/15, K = e^{-2 sigma} P sigma ~ lambda P psi:
# lambda^2 (1/(60 pi)) int psi P^2 psi
assert sp.simplify(G[2].coeffs()[0] - 1 / (60 * sp.pi)) == 0
print('n=2 agrees with Berger u_2 = K^2/15 - Delta K/15: OK')
# Gilkey a_6 via Vassilevich hep-th/0306138 (4.29) (fetched), restricted to n=2, quadratic terms, integrated:
# (1/7!)[17*4 - 2*2 - 4 + 9*4 - 28*4 + 8*2 - 24 - 12*4] int|grad K|^2 = -72/5040 = -1/70
q = sp.Rational(17 * 4 - 2 * 2 - 4 + 9 * 4 - 28 * 4 + 8 * 2 - 24 - 12 * 4, 5040)
assert q == sp.Rational(-1, 70)
# int |grad K|^2 ~ lambda^2 int psi P^3 psi ; (4pi)^{-1} * (-1/70)
assert sp.simplify(G[3].coeffs()[0] - q / (4 * sp.pi)) == 0
print('n=3 agrees with Gilkey a_6 (Vassilevich (4.29)): quadratic part of int u_3 dA = -(1/70) int |grad K|^2: OK')
print('CONCLUSION: Lemma VC5a holds iff (-Delta_0) denotes the NONNEGATIVE flat Laplacian -(d1^2+d2^2),')
print('i.e. iff Delta_0 = +(d1^2+d2^2) (analyst sign). With Delta_0 = -div grad (the file\'s convention for Delta_g)')
print('the sign is wrong for every odd n (even l): e.g. n=3 the true value is -1/(280 pi) int psi P^3 psi < 0.')
print('ALL ASSERTS PASSED')
