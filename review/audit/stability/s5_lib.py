"""Independent implementation of the Proposition S5 certificate (tests (i) and (ii)), Theorem S4's
delta_thm, and helpers.  Exact rational arithmetic throughout."""
from stab_lib import *

R_LIST = [F(k, 40) for k in range(20, 0, -1)] + [F(1, 100), F(1, 1000)]


def ps_add(a, b):
    return [x + y for x, y in zip(a, b)]


def lhs_q(m, a, r):
    """r^{k_a} prod_{b != a} (|a-b| - r)^{k_b}  (a lower bound for |q| on |z-a| = r when r < gaps)."""
    v = F(1)
    for b, kb in multiset(m):
        if b == a:
            v *= r ** kb
        else:
            v *= (abs(F(a) - b) - r) ** kb
    return v


class Cert:
    def __init__(self, m):
        self.m = list(m)
        n = self.n = len(m)
        self.I = invariants(m)
        self.e = esym(m)
        self.L = L_matrix(n)
        self.Linv = inv(self.L)
        self.absLinv = absM(self.Linv)
        self.H = heat_direct(m)
        N = self.N = max(2 * n - 3, 1)
        self.U = U_series(self.I, n, N)
        assert all(x >= 0 for x in self.U)  # 'valid because U >= 0'
        th = ps_compose(tanh_coeffs(N), self.U, N)
        self.sech2 = [F(int(k == 0)) - x for k, x in enumerate(ps_mul(th, th, N))]
        self.tanU = ps_compose(tan_coeffs(N), self.U, N)
        self.sec2U = [F(int(k == 0)) + x for k, x in enumerate(ps_mul(self.tanU, self.tanU, N))]
        self.M, self.b = M_b(self.I, n)
        self.Minv = inv(self.M)
        self.absMinv = absM(self.Minv)
        assert matvec(self.M, self.e[1:]) == self.b
        # exact Jacobian of (b - M e) with respect to I (e held fixed), and G = M^{-1} J L^{-1}
        J = [[F(0)] * n for _ in range(n)]
        J[n - 1][0] = self.e[n]
        for j in range(n - 1):
            for l in range(1, n):
                k = 2 * l - 1
                s = F(0)
                for i in range(j + 1):
                    if 2 * i + 1 - k >= 0 and 2 * j - 2 * i <= n:
                        s += self.sech2[2 * i + 1 - k] * self.e[2 * j - 2 * i]
                J[j][l] = s / k
        self.J = J
        self.DIe = matmul(self.Minv, J)
        self.G = matmul(self.DIe, self.Linv)
        # Taylor coefficients at each distinct order of p_c(z) = sum_j (-1)^j G_{jc} z^{n-j}
        self.taylor = {}
        for a, k in multiset(m):
            rows = []
            for c in range(n):
                coef = [F(0)] + [(-1) ** j * self.G[j - 1][c] for j in range(1, n + 1)]
                rows.append([abs(x) for x in reversed(poly_shift(coef, F(a)))])  # low->high in w
            self.taylor[a] = rows

    def bounds(self, rho):
        n, N, e = self.n, self.N, self.e
        dI = matvec(self.absLinv, rho)
        dR = dI[0]
        dU = [F(0)] * (N + 1)
        for l in range(1, n):
            dU[2 * l - 1] = dI[l] / (2 * l - 1)
        lin = [sum(abs(self.sech2[k - j]) * dU[j] for j in range(k + 1)) for k in range(N + 1)]
        tUV = ps_compose(tan_coeffs(N), ps_add(self.U, dU), N)
        rem = [a - b - c for a, b, c in zip(tUV, self.tanU, ps_mul(self.sec2U, dU, N))]
        assert all(x >= 0 for x in rem)
        dT = [x + y for x, y in zip(lin, rem)]
        g = lambda i: e[i] if 0 <= i <= n else F(0)
        r_abs = [sum(dT[2 * i + 1] * g(2 * j - 2 * i) for i in range(j + 1)) for j in range(n - 1)] + [dR * e[n]]
        r_rem = [sum(rem[2 * i + 1] * g(2 * j - 2 * i) for i in range(j + 1)) for j in range(n - 1)] + [F(0)]
        dM = [[F(0)] * n for _ in range(n)]
        for j in range(n - 1):
            for i in range(j):
                k = 2 * j - 2 * i
                if k <= n:
                    dM[j][k - 1] = dT[2 * i + 1]
        dM[n - 1][n - 1] = dR
        A = matmul(self.absMinv, dM)
        IA = [[F(int(i == j)) - A[i][j] for j in range(n)] for i in range(n)]
        if det(IA) == 0:
            return None
        IAinv = inv(IA)
        v = matvec(IAinv, [F(1)] * n)
        if not all(x > 0 for x in v):
            return None  # rho(A) < 1 not certified
        E = matvec(IAinv, matvec(self.absMinv, r_abs))
        varrho = [x + y for x, y in zip(matvec(self.absMinv, r_rem), matvec(A, E))]
        return dict(E=E, varrho=varrho, A=A, v=v, dT=dT, dI=dI)

    def test(self, rho, radii=R_LIST):
        """returns (ok_i, ok_ii, per-order detail)."""
        bd = self.bounds(rho)
        if bd is None:
            return False, False, 'rho(A)<1 not certified'
        n = self.n
        E, vr = bd['E'], bd['varrho']
        ok_i = ok_ii = True
        det_ = {}
        for a, k in multiset(self.m):
            ri = rii = None
            for r in radii:
                L = lhs_q(self.m, a, r)
                if ri is None:
                    rhs = sum(E[j - 1] * (a + r) ** (n - j) for j in range(1, n + 1))
                    if L > rhs:
                        ri = r
                if rii is None:
                    lin = sum(rho[c] * sum(t * r ** l for l, t in enumerate(self.taylor[a][c])) for c in range(n))
                    rhs2 = lin + sum(vr[j - 1] * (a + r) ** (n - j) for j in range(1, n + 1))
                    if L > rhs2:
                        rii = r
                if ri is not None and rii is not None:
                    break
            det_[a] = (ri, rii)
            ok_i &= ri is not None
            ok_ii &= rii is not None
        return ok_i, ok_ii, det_

    def certified(self, delta):
        oi, oii, _ = self.test([F(delta)] * self.n)
        return oi or oii


def theorem_s4(m):
    """delta_thm(m) and its ingredients, exactly (Theorem S4 / S2 / S3 constants)."""
    n = len(m)
    mu = F(max(m))
    mh = [F(x) / mu for x in m]
    eh = esym(mh)
    Ih = invariants(mh)
    M, _ = M_b(Ih, n)
    kappa = max(sum(abs(x) for x in row) for row in inv(M))
    sig = sigma_series(n, 2 * n)
    zeta = F(1)
    for j in range(n - 1):
        s = sum(sig[2 * i + 1] for i in range(j) if 2 <= 2 * j - 2 * i <= n)
        zeta = max(zeta, s)
    g = lambda i: eh[i] if 0 <= i <= n else F(0)
    rho = max([eh[n]] + [sum(sig[2 * i + 1] * g(2 * j - 2 * i) for i in range(j + 1)) for j in range(n - 1)])
    ell = [sum(abs(x) for x in row) for row in inv(L_matrix(n))]
    lam = max([mu * ell[0]] + [ell[r] * mu ** (1 - 2 * r) for r in range(1, n)])
    terms = [1 / lam, 1 / (2 * kappa * zeta * lam)]
    for a, k in multiset(m):
        Q = F(1)
        for b, kb in multiset(m):
            if b != a:
                Q *= abs(F(a) / mu - F(b) / mu) ** kb
        terms.append(Q * 2 ** (k - 1) / (3 ** n * (2 * mu) ** k * 2 * kappa * rho * lam))
    return min(terms), dict(kappa=kappa, zeta=zeta, rho=rho, lam=lam, terms=terms)


@lru_cache(None)
def sigma_series(n, Nmax):
    """sigma_k(n) = [w^k] artanh(w) sec^2((n+1) artanh w), k <= Nmax."""
    N = Nmax
    at = [F(0)] * (N + 1)
    for k in range(1, N + 1, 2):
        at[k] = F(1, k)
    arg = [F(n + 1) * x for x in at]
    t = ps_compose(tan_coeffs(N), arg, N)
    sec2 = [F(int(k == 0)) + x for k, x in enumerate(ps_mul(t, t, N))]
    return tuple(ps_mul(at, sec2, N))


def round_down_sig(x, s):
    """largest number with s significant digits that is <= x (exact, x > 0); returns Fraction."""
    x = F(x)
    e = 0
    while F(10) ** e > x:
        e -= 1
    while F(10) ** (e + 1) <= x:
        e += 1
    unit = F(10) ** (e - s + 1)
    return (x // unit) * unit


def round_up_sig(x, s):
    x = F(x)
    d = round_down_sig(x, s)
    if d == x:
        return d
    e = 0
    while F(10) ** e > d:
        e -= 1
    while F(10) ** (e + 1) <= d:
        e += 1
    return d + F(10) ** (e - s + 1)
