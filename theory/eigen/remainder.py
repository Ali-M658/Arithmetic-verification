"""Task 3: explicit remainders for the cone expansion and the area expansion.

Checks (asserts; nonzero exit on failure):
 1. phi_k(m) >= 0, increasing in m, and phi_k(m) <= Phi_m(rho) rho^{-2k} for rho in (0, pi/m)
    (Cauchy with positive coefficients); the closed form Phi_m(pi/(2m)) =
    cos(pi/2m)/(4 m sin^2(pi/2m)) and the corollary phi_k(m) <= (m/4)(2m/pi)^{2k}.
 2. The moment identity sum_j m_{2k}(2 theta_j)/(2 m sin theta_j) = (2k)!/4^k phi_k(m) by quadrature.
 3. Exact: the coefficients of e^{-t/4} sum_k (-1)^k |g_k| t^k are the b_l(m) of (eq:bl), and those of
    (e^{-t/4}/t)(1 - t J(t)) are the alpha_k.
 4. |E_m(t) - sum_{l<K} b_l(m) t^l| <= t^K Qcone(m, K, t0) and
    |I(t) - (A/4pi) sum_{k<=K} alpha_k t^{k-1}| <= (A/4pi) t^K Qarea(K, t0), on a grid of (m, K, t),
    against 40-digit quadrature.
"""
import sys
from fractions import Fraction as Fr
from math import factorial

import mpmath as mp

from eigen_common import (check, mpq, phi, b_cone, alpha, mu_moment, g_abs, Qcone, Qarea, Phi_closed,
                          elliptic_term, identity_term)

mp.mp.dps = 40


def main():
    out = []
    # 1. Cauchy bound and monotonicity
    for m in range(2, 31):
        for k in range(0, 41):
            v = phi(k, m)
            check(v >= 0, "phi_k >= 0")
            if m > 2:
                check(phi(k, m) > phi(k, m - 1), "phi_k increasing in m")
            for kappa in (Fr(1, 4), Fr(1, 2), Fr(3, 4), Fr(9, 10)):
                rho = mp.pi * mpq(kappa.numerator) / kappa.denominator / m
                if m == 1:
                    continue
                check(mpq(v) <= Phi_closed(m, rho) * rho ** (-2 * k) * (1 + mpq(10) ** -30),
                      f"Cauchy bound m={m} k={k}")
            corr = mpq(m) / 4 * (2 * mpq(m) / mp.pi) ** (2 * k)
            check(mpq(v) <= corr, "phi_k(m) <= (m/4)(2m/pi)^{2k}")
        rho = mp.pi / (2 * m)
        check(abs(Phi_closed(m, rho) - mp.cos(rho) / (4 * m * mp.sin(rho) ** 2)) < mpq(10) ** -30, "closed form at pi/2m")
        # Taylor series of the closed form vs phi_k (small u)
        u = mpq(1) / (10 * m)
        ser = sum(mpq(phi(k, m)) * u ** (2 * k) for k in range(60))
        check(abs(ser - Phi_closed(m, u)) < mpq(10) ** -30, "series of Phi_m")
    out.append("1. phi_k(m) >= 0, increasing in m, Cauchy bounds at rho = (1/4,1/2,3/4,9/10) pi/m: m <= 30, k <= 40")
    # growth of the ratio, for the record
    m = 12
    rat = [mpq(phi(k + 1, m)) / mpq(phi(k, m)) for k in (5, 10, 20, 40)]
    out.append(f"   phi_(k+1)/phi_k at m=12, k=5,10,20,40: {[mp.nstr(r, 6) for r in rat]}  (limit (m/pi)^2 = {mp.nstr((12 / mp.pi) ** 2, 6)})")

    # 2. moment identity by quadrature
    for m in (2, 3, 5, 8):
        for k in range(0, 5):
            tot = mpq(0)
            for j in range(1, m):
                th = mp.pi * j / m
                f = lambda r: r ** (2 * k) * mp.exp(-2 * th * r) / (1 + mp.exp(-2 * mp.pi * r))
                tot += mp.quad(f, [-mp.inf, -10, 0, 10, mp.inf]) / (2 * m * mp.sin(th))
            ref = mp.factorial(2 * k) / mpq(4) ** k * mpq(phi(k, m))
            check(abs(tot - ref) < mpq(10) ** -25 * (1 + ref), f"moment identity m={m} k={k}")
    out.append("2. moment identity checked by quadrature for m in {2,3,5,8}, k <= 4")

    # 3. exact coefficient identities
    for m in (2, 3, 4, 7, 12, 30):
        for l in range(0, 15):
            s = sum(Fr((-1) ** k) * g_abs(k, m) * Fr((-1) ** (l - k), 4 ** (l - k) * factorial(l - k)) for k in range(l + 1))
            check(s == b_cone(l, m), f"b_l from g_k, m={m} l={l}")
    for k in range(0, 20):
        # coefficient of t^{k-1} in e^{-t/4}/t - e^{-t/4} J(t), J = sum_j (-t)^j mu_j / j!
        s = Fr((-1) ** k, 4 ** k * factorial(k))
        for i in range(k):
            j = k - 1 - i
            s -= Fr((-1) ** i, 4 ** i * factorial(i)) * Fr((-1) ** j) * mu_moment(j) / factorial(j)
        check(s == alpha(k), f"alpha_{k} from mu")
    out.append("3. exact: b_l(m) = [t^l] e^{-t/4} sum (-1)^k |g_k(m)| t^k (m in {2,3,4,7,12,30}, l < 15); alpha_k from mu_k (k < 20)")

    # 4. remainders against quadrature
    worst = {}
    t0 = 1
    for m in (2, 3, 7, 8, 12):
        for t in ('0.001', '0.01', '0.05', '0.2', '1'):
            tt = mpq(t)
            E = elliptic_term(m, tt, dps=40)
            for K in range(0, 7):
                approx = sum(mpq(b_cone(l, m)) * tt ** l for l in range(K))
                err = abs(E - approx)
                bound = tt ** K * Qcone(m, K, t0)
                check(err <= bound, f"cone remainder m={m} t={t} K={K}: {err} > {bound}")
                worst[(m, K)] = max(worst.get((m, K), 0), err / bound)
    out.append("4a. cone remainder |E_m - sum_{l<K} b_l t^l| <= t^K Qcone(m,K,1): m in {2,3,7,8,12}, K <= 6, t in {1e-3,..,1}")
    out.append("    largest ratio error/bound per m: " + ", ".join(f"m={m}: {mp.nstr(max(v for (mm, K), v in worst.items() if mm == m), 3)}" for m in (2, 3, 7, 8, 12)))
    worstA = 0
    for t in ('0.001', '0.01', '0.05', '0.2', '1'):
        tt = mpq(t)
        area = 4 * mp.pi  # A/(4 pi) = 1
        I = identity_term(area, tt, dps=40)
        for K in range(0, 8):
            approx = sum(mpq(alpha(k)) * tt ** (k - 1) for k in range(K + 1))
            err = abs(I - approx)
            bound = tt ** K * Qarea(K, t0)
            check(err <= bound, f"area remainder t={t} K={K}")
            worstA = max(worstA, err / bound)
    out.append(f"4b. area remainder |I - (A/4pi) sum_(k<=K) alpha_k t^(k-1)| <= (A/4pi) t^K Qarea(K,1): K <= 7; largest ratio {mp.nstr(worstA, 3)}")
    # table of constants
    out.append("\nQcone(m, K, 1) and Qarea(K, 1):")
    for K in range(0, 7):
        out.append(f"  K={K}: Qarea={mp.nstr(Qarea(K, 1), 5)}  " + "  ".join(f"m={m}:{mp.nstr(Qcone(m, K, 1), 5)}" for m in (2, 3, 8, 12, 100)))
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
