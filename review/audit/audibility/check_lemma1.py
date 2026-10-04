"""Lemma 1 (parity), with explicit ideal-membership certificates.

For odd j, with f(z) = prod(1 + x_i z), G(z) = 2 sum_{k odd} s_k z^k / k:
  f(z) - f(-z) = f(-z) (exp G - 1), so
  2 e_j = sum_{b=1}^{j} [z^{j-b}] f(-z) * [z^b](exp G - 1),
and every [z^b](exp G - 1), b <= j, is a polynomial in s_1, s_3, ..., s_b without constant term.
Conversely log(f(z)/f(-z)) = G, and f(z)/f(-z) - 1 = 2 O(z)/(E(z) - O(z)) has all coefficients up to
z^j in the ideal (e_1, e_3, ..., e_j); log(1+u) = u - u^2/2 + ... then gives 2 s_j / j in that ideal.
The script builds these certificates as explicit polynomials in formal symbols S_k (resp. Ek), checks
that each coefficient multiplying the generators is a polynomial, and that substituting the true
power sums (resp. elementary symmetric functions) reproduces e_j (resp. s_j) identically.
"""
from sympy import symbols, expand, Rational, S
from itertools import combinations


def ser_exp(g, M):
    """exp of a power series g (list, g[0]=0), truncated to degree < M; via e' = g' e."""
    e = [S(0)] * M
    e[0] = S(1)
    for n in range(1, M):
        e[n] = expand(sum(k * g[k] * e[n - k] for k in range(1, n + 1) if k < len(g)) / n)
    return e


def ser_mul(a, b, M):
    return [expand(sum(a[i] * b[n - i] for i in range(n + 1) if i < len(a) and n - i < len(b))) for n in range(M)]


def ser_inv(a, M):
    r = [S(0)] * M
    r[0] = 1 / a[0]
    for n in range(1, M):
        r[n] = expand(-sum(a[i] * r[n - i] for i in range(1, n + 1) if i < len(a)) * r[0])
    return r


def ser_log1(u, M):
    """log(1+u) for u[0]=0, truncated; via (log)' = u'/(1+u)."""
    one_u = [S(1)] + list(u[1:M])
    d = [(k + 1) * u[k + 1] if k + 1 < len(u) else S(0) for k in range(M)]
    q = ser_mul(d, ser_inv(one_u, M), M)
    return [S(0)] + [expand(q[k - 1] / k) for k in range(1, M)]

out = []


def esym(xs, k):
    if k == 0:
        return S(1)
    if k > len(xs):
        return S(0)
    return sum(_prod(c) for c in combinations(xs, k))


def _prod(c):
    r = S(1)
    for t in c:
        r *= t
    return r


z = symbols("z")
for N in range(1, 6):
    xs = symbols(f"x1:{N+1}")
    for j in range(1, 8, 2):
        Ssym = {k: symbols(f"S{k}") for k in range(1, j + 1, 2)}
        G = [S(0)] * (j + 1)
        for k in Ssym:
            G[k] = 2 * Ssym[k] / k
        expG = ser_exp(G, j + 1)
        # coefficient of z^b of expG - 1 is in the ideal (S_1,...,S_b): no constant term in S
        cert = S(0)
        for b in range(1, j + 1):
            cb = expG[b]
            assert cb.subs({v: 0 for v in Ssym.values()}) == 0
            cert += (-1) ** (j - b) * esym(xs, j - b) * cb      # [z^{j-b}] f(-z) = (-1)^{j-b} e_{j-b}
        sub = {Ssym[k]: sum(x ** k for x in xs) for k in Ssym}
        assert expand(cert.subs(sub) - 2 * esym(xs, j)) == 0, (N, j)
        # converse
        Esym = {k: symbols(f"E{k}") for k in range(1, j + 1, 2)}
        Ev = [esym(xs, k) if k % 2 == 0 else S(0) for k in range(j + 1)]   # even part, true values
        Od = [Esym[k] if k in Esym else S(0) for k in range(j + 1)]        # odd part, formal generators
        num = [a + b for a, b in zip(Ev, Od)]
        den = [a - b for a, b in zip(Ev, Od)]
        ratio = ser_mul(num, ser_inv(den, j + 1), j + 1)
        Lg = ser_log1([S(0)] + ratio[1:], j + 1)
        cj = Lg[j]
        assert expand(cj.subs({v: 0 for v in Esym.values()})) == 0
        sub2 = {Esym[k]: esym(xs, k) for k in Esym}
        assert expand(cj.subs(sub2) - Rational(2, j) * sum(x ** j for x in xs)) == 0, (N, j)
    out.append(f"N={N}: e_j in (s_1,...,s_j) and s_j in (e_1,...,e_j) certified for odd j<=7")
for l in out:
    print(l)
print("ALL CHECKS PASSED")
