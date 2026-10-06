"""TF.3 (hyperbolic-term bound) and TF.8 (Theorem 1.2(iii)).

Certificates:
 1. (sympy, exact symbolic) C(A,l,D) = pi/sqrt(4 pi) * e^{3D} l e^{l/2}/(A(1-e^{-l})) * max_{0<t<=T}(1+2t/(l-t)),
    T = l^2/(2(1+l)): the factor is increasing in t (derivative 2l/(l-t)^2>0), T<l, and its value
    at T is (2+3l)/(2+l); the product equals the printed C.
 2. (sympy, exact symbolic) d/dl log B(l,D,t) = -1/2 - [l/(2t) - (1+l)/l] - e^{-l}/(1-e^{-l})
    - 2t/(l^2-t^2), where B is the right side of TF.3; each bracket is >= 0 when t <= T(l).
    Hence B is strictly decreasing in l on {l : T(l) >= t}; T is increasing; B is increasing in D.
    So the bound for the orbifold with systole l_i >= l and diameter D_i <= D is <= B(l, D, t).
 3. (mpmath interval arithmetic, rigorous at grid points) B(l2,D,t) < B(l1,D,t) for l1<l2 on a grid,
    t = theta*T(l1), theta in (0,1].
 4. (exact, integers) weighted / all-classes / primitive length counts first differ at the same
    length: random primitive-count data, w(L) = sum_k (L/k) n_prim(L/k), n_all(L) = sum_k n_prim(L/k).
Sanity (mpmath, not a certificate): a synthetic length spectrum that saturates the counting bound
N(L) <= (pi/A) e^{L+3D} satisfies the TF.3 inequality, for small and large systoles at t = T.
"""
import sys
import random
import sympy as sp
import mpmath as mp
from mpmath import iv

l, t, A, D = sp.symbols('ell t A D', positive=True)
T = l ** 2 / (2 * (1 + l))

# ---- 1
fac = 1 + 2 * t / (l - t)
assert sp.simplify(sp.diff(fac, t) - 2 * l / (l - t) ** 2) == 0
assert sp.simplify(l - T - l * (2 + l) / (2 * (1 + l))) == 0          # l - T > 0
facT = sp.simplify(fac.subs(t, T))
assert sp.simplify(facT - (2 + 3 * l) / (2 + l)) == 0
pref = sp.pi * sp.exp(3 * D) / (A * (1 - sp.exp(-l))) * l * sp.exp(l / 2) / sp.sqrt(4 * sp.pi)
C_derived = pref * facT
C_printed = sp.sqrt(sp.pi) * sp.exp(3 * D) * l * sp.exp(l / 2) * (2 + 3 * l) / (2 * A * (1 - sp.exp(-l)) * (2 + l))
assert sp.simplify(C_derived - C_printed) == 0
print("1. C(A,l,D) re-derived: max of 1+2t/(l-t) at t=T is (2+3l)/(2+l); pi/sqrt(4pi)=sqrt(pi)/2; equals printed C")

# ---- 2
logB = sp.log(sp.pi) + 3 * D - sp.log(A) - sp.log(1 - sp.exp(-l)) + sp.log(l) + l / 2 \
    + sp.log(fac) - l ** 2 / (4 * t) - sp.log(4 * sp.pi * t) / 2
dB = sp.diff(logB, l)
claimed = -sp.Rational(1, 2) - (l / (2 * t) - (1 + l) / l) - sp.exp(-l) / (1 - sp.exp(-l)) - 2 * t / (l ** 2 - t ** 2)
assert sp.simplify(dB - claimed) == 0
# bracket >= 0  <=>  t <= l^2/(2(1+l)) = T
assert sp.simplify(sp.solve(sp.Eq(l / (2 * t), (1 + l) / l), t)[0] - T) == 0
assert sp.simplify(sp.diff(T, l) - (l ** 2 + 2 * l) / (2 * (1 + l) ** 2)) == 0      # T increasing
assert sp.simplify(sp.diff(logB, D) - 3) == 0
print("2. d/dl log B = -1/2 - [l/2t-(1+l)/l] - e^-l/(1-e^-l) - 2t/(l^2-t^2) < -1/2 on t<=T(l); T increasing; B increasing in D")

# ---- 3
def B_iv(lv, Dv, tv, Av=iv.mpf(1)):
    return iv.pi * iv.exp(3 * Dv) / (Av * (1 - iv.exp(-lv))) * lv * iv.exp(lv / 2) \
        * (1 + 2 * tv / (lv - tv)) * iv.exp(-lv ** 2 / (4 * tv)) / iv.sqrt(4 * iv.pi * tv)


iv.dps = 30
grid = [iv.mpf(x) for x in ['0.01', '0.05', '0.1', '0.3', '0.7', '1', '1.5', '2', '3', '5', '8', '12', '20']]
cnt = 0
for i, l1 in enumerate(grid):
    T1 = l1 ** 2 / (2 * (1 + l1))
    for th in ['0.001', '0.1', '0.5', '0.9', '1']:
        tv = T1 * iv.mpf(th)
        for l2 in grid[i + 1:]:
            b1, b2 = B_iv(l1, iv.mpf(1), tv), B_iv(l2, iv.mpf(1), tv)
            assert b2.b < b1.a, (l1, l2, th)
            cnt += 1
print(f"3. interval check: B(l2,D,t) < B(l1,D,t) for l1<l2, t=theta T(l1): {cnt} cases OK")

# ---- 4
random.seed(20261006)
LMAX = 60
for trial in range(4000):
    n1 = [0] + [random.choice([0, 0, 0, 1, 2]) for _ in range(LMAX)]
    n2 = list(n1)
    # perturb at a random position, adversarially sometimes compensating at a multiple
    p = random.randint(1, LMAX)
    n2[p] += random.choice([-1, 1]) if n2[p] > 0 else 1
    if random.random() < 0.5 and 2 * p <= LMAX:
        n2[2 * p] = max(0, n2[2 * p] + random.choice([-2, -1, 1, 2]))

    def w(n, L):
        return sum(sp.Rational(L, k) * n[L // k] for k in range(1, L + 1) if L % k == 0)

    def nall(n, L):
        return sum(n[L // k] for k in range(1, L + 1) if L % k == 0)

    def first(f):
        for L in range(1, LMAX + 1):
            if f(n1, L) != f(n2, L):
                return L
        return None
    fp = first(lambda n, L: n[L])
    assert fp == first(w) == first(nall), trial
print("4. weighted, all-class and primitive length counts first differ at the same length (4000 random pairs): OK")

# ---- sanity: saturating synthetic spectrum
mp.mp.dps = 40
for (ell, Dv, Av) in [(mp.mpf('0.05'), mp.mpf('0.5'), mp.mpf('3')), (mp.mpf('0.5'), mp.mpf(2), mp.mpf(1)),
                      (mp.mpf(2), mp.mpf(1), mp.mpf('0.5')), (mp.mpf(6), mp.mpf(4), mp.mpf(10))]:
    c = mp.pi * mp.exp(3 * Dv) / Av
    for th in [mp.mpf('0.2'), mp.mpf(1)]:
        tt = th * ell ** 2 / (2 * (1 + ell))
        # lengths: jumps of floor(c e^x) on [ell, oo), with N(ell) = floor(c e^ell) classes at ell
        S = mp.mpf(0)
        n0 = int(mp.floor(c * mp.exp(ell)))
        def term(x):
            return x / (2 * mp.sinh(x / 2)) * mp.exp(-x * x / (4 * tt)) / mp.sqrt(4 * mp.pi * tt)
        S += n0 * term(ell)
        k = n0 + 1
        while True:
            x = mp.log(k / c)
            tm = term(x)
            S += tm
            if tm < mp.mpf(10) ** -60 * S and x > 4 * ell + 10:
                break
            k += 1
            if k > n0 + 200000:
                break
        bound = c / (1 - mp.exp(-ell)) * ell * mp.exp(ell / 2) * (1 + 2 * tt / (ell - tt)) \
            * mp.exp(-ell ** 2 / (4 * tt)) / mp.sqrt(4 * mp.pi * tt)
        assert S <= bound, (ell, th, S, bound)
print("sanity: saturating synthetic spectra satisfy the TF.3 inequality (not a certificate)")
print("ALL CHECKS PASSED")
sys.exit(0)
