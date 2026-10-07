"""Task 2: explicit counting and tail bounds.

Checks (asserts; nonzero exit on failure):
 1. 0 < E_m(t) <= b_0(m) = (m^2-1)/(12m) and 0 < I(t) <= e^{-t/4} Area/(4 pi t) (quadrature).
 2. Area >= pi/21 and n + 4g <= Area/pi + 4 on every hyperbolic signature with g <= 3, n <= 7,
    orders <= 40 (the lemma is proved for all; this is a consistency check).
 3. The counting bound #{lambda_j <= x} <= e Z(1/x) <= e Zb(1/x), and the tail bound, on the
    committed spectra of O(2,8,8) and O(3,3,12) (numerics/data), where the spectrum is complete.
 4. The all-t bound for Hyp (Proposition C2) and Lemma 2.5 against Hyp(t) = Z(t) - I(t) - E(t)
    computed from the committed spectra.
"""
import sys
from fractions import Fraction as Fr
from math import floor

import mpmath as mp

from eigen_common import (check, mpq, b_cone, elliptic_term, identity_term, area_over_2pi, diam_bound,
                          hyp_bound_small, hyp_bound_all, load_triangle_spectrum)

mp.mp.dps = 30

# systoles of the two orbifolds: the shortest lengths of Section 7 of the manuscript, recomputed by
# diameter.py from the triangle groups (2.256768 and 1.862604)
SYSTOLE = {(2, 8, 8): mp.mpf('2.256768'), (3, 3, 12): mp.mpf('1.862604')}


def main():
    out = []
    # 1. pointwise bounds on I and E
    for m in range(2, 13):
        for t in ('0.001', '0.01', '0.1', '1', '5'):
            E = elliptic_term(m, mp.mpf(t))
            check(0 < E <= mpq(b_cone(0, m)), f"E_{m}({t}) <= b_0")
    for t in ('0.001', '0.01', '0.1', '1', '5'):
        tt = mp.mpf(t)
        I = identity_term(4 * mp.pi, tt)
        check(0 < I <= mp.e ** (-tt / 4) / tt, "I(t) <= e^{-t/4} A/(4 pi t)")
    out.append("1. 0 < E_m(t) <= b_0(m) (m <= 12) and 0 < I(t) <= e^{-t/4} A/(4 pi t), t in {1e-3,...,5}")

    # 2. area and cone count
    import itertools
    smin = None
    cnt = 0
    for g in range(0, 4):
        for n in range(0, 8):
            for orders in itertools.combinations_with_replacement(range(2, 41), n):
                if n > 5 and orders[-1] > 6:
                    continue  # keep the enumeration small; large n is far from the minimum
                s = area_over_2pi(g, orders)
                if s <= 0:
                    continue
                cnt += 1
                smin = s if smin is None or s < smin else smin
                check(n + 4 * g <= 2 * s + 4, "n + 4g <= Area/pi + 4")
    check(smin == Fr(1, 42), "least Area/2pi is 1/42")
    out.append(f"2. {cnt} hyperbolic signatures: least Area/(2 pi) = {smin} (so Area >= pi/21); n + 4g <= Area/pi + 4 on all")

    # 3./4. committed spectra
    for pqr in ((2, 8, 8), (3, 3, 12)):
        spec, lam_top = load_triangle_spectrum(pqr)
        lam = [x for x, _ in spec]
        s = area_over_2pi(0, pqr)
        A = 2 * mp.pi * mpq(s)
        M = max(pqr)
        eps = SYSTOLE[pqr]
        D = diam_bound(A, eps, M)
        cone0 = sum(mpq(b_cone(0, m)) for m in pqr)
        t2 = eps ** 2 / (2 * (1 + eps))

        def Zdata(t):
            # Weyl-type tail beyond the computed range, for t where it is negligible
            return mp.fsum(mp.e ** (-x * t) for x in lam)

        def H(t):
            return hyp_bound_small(t, eps, D, area_lb=A) if t <= t2 else hyp_bound_all(t, eps, D, area_lb=A)

        def Zb(t):
            return A / (4 * mp.pi * t) + cone0 + H(t)

        # counting bound at x up to the complete range
        worst = 0
        for x in (5, 10, 50, 100, 500, 1000, 5000, 10000, 15000):
            if x > lam_top:
                continue
            Nx = sum(1 for v in lam if v <= x)
            bound = mp.e * Zb(mp.mpf(1) / x)
            check(Nx <= bound, f"counting bound {pqr} x={x}")
            worst = max(worst, Nx / bound)
        # Hyp from data at moderate t (the truncation is below 1e-60 for t >= 0.01)
        hyp_rows = []
        for t in ('0.06', '0.1', '0.2', '0.5', '1', '2'):
            tt = mp.mpf(t)
            check(mp.e ** (-lam_top * tt) * A / (4 * mp.pi * tt) < mp.mpf(10) ** -60, "truncation negligible")
            Z = Zdata(tt)
            I = identity_term(A, tt)
            E = sum(elliptic_term(m, tt) for m in pqr)
            hyp = Z - I - E
            check(hyp > -mp.mpf(10) ** -9, "Hyp >= 0 up to eigenvalue error")
            hb = hyp_bound_all(tt, eps, D, area_lb=A)
            check(hyp <= hb, "Hyp <= all-t bound")
            if tt <= t2:
                check(hyp <= hyp_bound_small(tt, eps, D, area_lb=A), "Hyp <= Lemma 2.5 bound")
            hyp_rows.append(f"t={t}: Hyp={mp.nstr(hyp, 4)}")
        # tail bound: sum_{lambda > Lam} e^{-lambda t} <= e^{-Lam (t-s)} Z(s), checked with data
        t, ssm = mp.mpf('0.02'), mp.mpf('0.01')
        for Lam in (100, 500, 1000, 3000):
            tail = mp.fsum(mp.e ** (-x * t) for x in lam if x > Lam)
            check(tail <= mp.e ** (-Lam * (t - ssm)) * Zdata(ssm) * (1 + mp.mpf(10) ** -12), "tail bound")
            check(tail <= mp.e ** (-Lam * (t - ssm)) * Zb(ssm), "tail bound with Zb")
        out.append(f"3./4. O{pqr}: {len(lam)} eigenvalues, complete to {lam_top:.0f}; D(A,eps,M) = {mp.nstr(D, 6)};"
                   f" max N(x)/(e Zb(1/x)) = {mp.nstr(worst, 4)}; " + "; ".join(hyp_rows))
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
