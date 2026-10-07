"""Exact (Fraction / sympy) checks for Group 2 (eig:remcone, eig:remarea, eig:Grem).

Independent re-derivation; inputs are only the verbatim statements of STATEMENTS.md, Sections A-B.
Every check raises on failure.
"""
from fractions import Fraction as Fr
from math import factorial, comb
import sympy as sp

KMAX = 14


def B(n):
    return Fr(sp.Rational(sp.bernoulli(n)).p, sp.Rational(sp.bernoulli(n)).q)


def B2l_half(l):  # Bernoulli polynomial B_{2l}(1/2)
    v = sp.bernoulli(2 * l, sp.Rational(1, 2))
    v = sp.Rational(v)
    return Fr(v.p, v.q)


# sigma_i: u/sin u = sum sigma_i u^{2i}
u = sp.symbols('u')
ser = sp.series(u / sp.sin(u), u, 0, 2 * KMAX + 6).removeO()
sigma = [Fr(sp.Rational(ser.coeff(u, 2 * i)).p, sp.Rational(ser.coeff(u, 2 * i)).q) for i in range(KMAX + 3)]
assert sigma[0] == 1 and all(s > 0 for s in sigma)
# extend with the closed form x/sin x = sum (-1)^{n+1}(2^{2n}-2)B_{2n}x^{2n}/(2n)!, checked against the series
def _sig(n):
    return (-1)**(n + 1) * (2**(2 * n) - 2) * B(2 * n) / factorial(2 * n)
assert all(_sig(i) == sigma[i] for i in range(len(sigma)))
sigma = [_sig(i) for i in range(60)]
assert all(s > 0 for s in sigma)


def mphi(k, m):  # m*phi_k(m), Lemma lem:Phi (eq:phik)
    m = Fr(m)
    return Fr(1, 4) * sum(sigma[k + 1 - n] * 4**n * abs(B(2 * n)) / factorial(2 * n) * (m**(2 * n) - 1)
                          for n in range(1, k + 2))


def phi(k, m):
    return mphi(k, m) / Fr(m)


def g(k, m):
    return (-1)**k * Fr(factorial(2 * k), factorial(k) * 4**k) * phi(k, m)


def b_manuscript(l, m):  # eq:bl
    p = Fr(1, 4**l) * sum(Fr(factorial(2 * k), factorial(k) * factorial(l - k)) * mphi(k, m) for k in range(l + 1))
    return (-1)**l * p / Fr(m)


def b_identity(l, m):
    return sum(g(k, m) * Fr(-1, 4)**(l - k) / factorial(l - k) for k in range(l + 1))


# 1. identity b_l = sum g_k (-1/4)^{l-k}/(l-k)!, exact, m = 1..25 (and rational m), l <= KMAX
for m in list(range(1, 26)) + [Fr(3, 2), Fr(7, 3)]:
    for l in range(KMAX + 1):
        assert b_manuscript(l, m) == b_identity(l, m), (l, m)
print("1. b_l identity: OK (l<=%d, m=1..25, 3/2, 7/3)" % KMAX)

# 1b. Phi_m Taylor coefficients from the closed form agree with eq:phik (sympy series), m=2..8
for m in range(2, 9):
    cf = (sp.cot(u) - m * sp.cot(m * u)) / (4 * m * sp.sin(u))
    s = sp.series(cf, u, 0, 2 * 8 + 2).removeO()
    for k in range(8):
        c = sp.nsimplify(sp.expand(s.coeff(u, 2 * k)), rational=True)
        c = sp.simplify(c)
        assert c.is_Rational, (m, k, c)
        assert Fr(int(c.p), int(c.q)) == phi(k, m), (m, k)
print("1b. closed form Taylor coeffs == eq:phik: OK (m=2..8, k<8)")

# 2. positivity and strict monotonicity of phi_k in m
for k in range(KMAX + 1):
    prev = Fr(0)
    for m in range(2, 61):
        v = phi(k, m)
        assert v > 0 and v > prev, (k, m)
        prev = v
    assert phi(k, 1) == 0
print("2. phi_k(m) > 0 and strictly increasing in m=2..60, phi_k(1)=0: OK")

# 3. sign structure g_k: sign (-1)^k  ->  all terms of b_K have sign (-1)^K, so
#    Q_cone(m,K,0) := |g_K| + sum_{k<K}|g_k|4^{k-K}/(K-k)! = |b_K| ... wait: b_K includes k=K term g_K.
for m in range(2, 21):
    for K in range(KMAX):
        Q0 = abs(g(K, m)) + sum(abs(g(k, m)) * Fr(4)**(k - K) / factorial(K - k) for k in range(K))
        assert Q0 == abs(b_identity(K, m)), (m, K)
        assert b_identity(K, m) != 0 and (b_identity(K, m) > 0) == (K % 2 == 0)
print("3. Q_cone(m,K,t->0) == |b_K(m)| exactly and sgn b_K = (-1)^K: OK (m=2..20, K<%d)" % KMAX)


# 4. mu_k and alpha_k consistency
def mu(k):
    return (1 - Fr(1, 2**(2 * k + 1))) * abs(B(2 * k + 2)) / (k + 1)


def alpha_manuscript(k):
    return Fr((-1)**k, factorial(k) * 4**k) * sum(comb(k, l) * Fr(-4)**l * B2l_half(l) for l in range(k + 1))


def beta(k):  # coefficient of t^k in int r tanh(pi r) e^{-t r^2} dr - 1/t
    return -Fr((-1)**k, factorial(k)) * mu(k)


def alpha_derived(k):
    s = Fr(-1, 4)**k / factorial(k)
    s += sum(beta(j) * Fr(-1, 4)**(k - 1 - j) / factorial(k - 1 - j) for j in range(k))
    return s


for k in range(KMAX + 2):
    assert alpha_manuscript(k) == alpha_derived(k), (k, alpha_manuscript(k), alpha_derived(k))
assert alpha_manuscript(0) == 1
print("4. alpha_k from mu_k (Taylor of tanh = 1 - 2/(e^{2pi r}+1)) == manuscript alpha_k: OK (k<=%d)" % (KMAX + 1))

# mu_k via the Dirichlet eta integral: int_0^inf x^{s-1}/(e^x+1) = (1-2^{1-s}) Gamma(s) zeta(s), s=2k+2
for k in range(KMAX):
    s = 2 * k + 2
    val = 4 * (1 - sp.Rational(1, 2**(s - 1))) * sp.factorial(s - 1) * sp.zeta(s) / (2 * sp.pi)**s
    val = sp.simplify(val)
    assert val.is_Rational, (k, val)
    assert val == sp.Rational(mu(k).numerator, mu(k).denominator), k
print("4b. mu_k closed form == 4 (1-2^{-2k-1}) (2k+1)! zeta(2k+2)/(2pi)^{2k+2}: OK")


# 5. Q_area(K, t->0) == |alpha_{K+1}| and sgn alpha_k = (-1)^k
def Qarea0(K):
    return Fr(1, 4**(K + 1) * factorial(K + 1)) + mu(K) / factorial(K) + \
        sum(mu(k) * Fr(4)**(k - K) / (factorial(k) * factorial(K - k)) for k in range(K))


for K in range(KMAX):
    assert Qarea0(K) == abs(alpha_manuscript(K + 1)), K
    assert (alpha_manuscript(K) > 0) == (K % 2 == 0)
print("5. Q_area(K,t->0) == |alpha_{K+1}| exactly, sgn alpha_k = (-1)^k: OK")

# 6. Grem indexing: sum_{j=1}^{K+1} c_j t^{j-2} == (A/4pi) sum_{k=0}^K alpha_k t^{k-1} + sum_i sum_{l<K} b_l t^l
t, A = sp.symbols('t A', positive=True)
for K in range(0, 7):
    for ms in [(2,), (2, 3, 7), (5, 5), ()]:
        c = [None, A / (4 * sp.pi)]
        for j in range(2, K + 2):
            a = alpha_manuscript(j - 1)
            c.append(sp.Rational(a.numerator, a.denominator) * A / (4 * sp.pi) +
                     sum(sp.Rational(b_manuscript(j - 2, m).numerator, b_manuscript(j - 2, m).denominator) for m in ms))
        lhs = sum(c[j] * t**(j - 2) for j in range(1, K + 2))
        rhs = A / (4 * sp.pi) * sum(sp.Rational(alpha_manuscript(k).numerator, alpha_manuscript(k).denominator) * t**(k - 1)
                                    for k in range(K + 1))
        rhs += sum(sp.Rational(b_manuscript(l, m).numerator, b_manuscript(l, m).denominator) * t**l
                   for m in ms for l in range(K))
        assert sp.simplify(lhs - rhs) == 0, (K, ms)
print("6. (eig:Grem) polynomial == area part (k<=K) + cone parts (l<K): OK (K=0..6)")

# 7. the bound phi_k <= cos(pi/2m)/(4m sin^2(pi/2m)) (2m/pi)^{2k} <= m/4 (2m/pi)^{2k}; |g_k| bound
import mpmath as mp
mp.mp.dps = 40
worst = 0
for m in range(2, 41):
    x = mp.pi / (2 * m)
    c0 = mp.cos(x) / (4 * m * mp.sin(x)**2)
    assert c0 <= mp.mpf(m) / 4
    # direct closed form at rho=pi/2m
    rho = x
    clo = (mp.cot(rho) - m * mp.cot(m * rho)) / (4 * m * mp.sin(rho))
    direct = sum(1 / (4 * m * mp.sin(mp.pi * j / m) * mp.sin(mp.pi * j / m - rho)) for j in range(1, m))
    assert abs(clo - c0) < mp.mpf(10)**-30 and abs(direct - c0) < mp.mpf(10)**-30
    for k in range(0, 41):
        ph = phi(k, m)
        bnd = c0 * (2 * m / mp.pi)**(2 * k)
        assert mp.mpf(ph.numerator) / ph.denominator <= bnd * (1 + mp.mpf(10)**-30), (m, k)
        gb = mp.mpf(m) / 4 * mp.factorial(2 * k) / mp.factorial(k) * (m / mp.pi)**(2 * k)
        gk = g(k, m)
        assert abs(mp.mpf(gk.numerator) / gk.denominator) <= gb, (m, k)
        worst = max(worst, (mp.mpf(ph.numerator) / ph.denominator) / bnd)
    # sum phi_k rho^{2k} converges to Phi_m(rho) (nonnegative series): partial sums below
    ps = sum(mp.mpf(phi(k, m).numerator) / phi(k, m).denominator * rho**(2 * k) for k in range(41))
    assert ps <= c0 * (1 + mp.mpf(10)**-30)
print("7. Cauchy bound, value at rho=pi/2m, <= m/4, and |g_k| bound: OK (m=2..40, k=0..40); "
      "max ratio phi_k/bound = %s" % mp.nstr(worst, 8))

# 7b. how loose: phi_k (pi/m)^{2k} -> const (bound loses 4^k)
for m in (2, 5, 20):
    r = [float(phi(k, m) * 1) * float((mp.pi / m)**(2 * k)) for k in (10, 20, 30)]
    print("   m=%d  phi_k (pi/m)^{2k}, k=10,20,30:" % m, ["%.6g" % v for v in r])
print("ALL EXACT CHECKS PASSED")
