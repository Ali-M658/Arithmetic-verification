"""Exhaustive check of the configuration analysis behind Lemma eig:sep.

Independent proof (see REPORT.md): let p != q be elliptic points of orders m_p, m_q <= M at distance d,
alpha = pi/m_p, beta = pi/m_q, and a, b the generators (signs chosen so that the lines of (H3) are on
the same side).  X = sin(alpha) sin(beta) cosh d - cos(alpha) cos(beta).
  * X >= 1: X = 1 is parabolic (excluded, cocompact); X > 1 gives ab hyperbolic of length 2h,
    cosh h = X <= cosh d, so d >= h >= eps/2.
  * X < 1: ab is a rotation by 2 theta, cos theta = X, theta < theta0 = pi - alpha - beta, and
    theta = pi k / m_r for an elliptic point of order m_r <= M.  So d is at least the d solving
    cos(theta_max) = X(d), theta_max the largest pi k/m_r < theta0 with m_r <= M.
This script computes, for every M <= MMAX and every 2 <= m_p <= m_q <= M, that worst d exactly
(Fractions for theta/pi, mpmath for d) and checks cosh d - 1 >= 2/(pi^2 M^2), i.e.
d >= arccosh(1 + 2/(pi^2 M^2)).  It records the smallest ratio (cosh d - 1)/(2/(pi^2 M^2)).
It also checks the analytic bound cosh d - 1 >= 2/(pi M^2) obtained in the report (a factor pi better).
"""
from fractions import Fraction
from math import floor
import mpmath as mp

mp.mp.dps = 30
MMAX = 70

worst = (mp.inf, None)
worst_analytic = (mp.inf, None)
count = 0
for M in range(2, MMAX + 1):
    target = 2 / (mp.pi ** 2 * M ** 2)
    for mp_ in range(2, M + 1):
        for mq in range(mp_, M + 1):
            t0 = 1 - Fraction(1, mp_) - Fraction(1, mq)   # theta0/pi
            if t0 <= 0:
                continue                                    # only (2,2): X>1 always (d>0)
            best = Fraction(0)
            for mr in range(2, M + 1):
                k = -(-t0.numerator * mr // t0.denominator) - 1   # ceil(t0*mr)-1
                if k >= 1:
                    f = Fraction(k, mr)
                    assert f < t0
                    if f > best:
                        best = f
            if best == 0:
                continue                                    # no elliptic product possible
            al, be = mp.pi / mp_, mp.pi / mq
            th = mp.pi * best.numerator / best.denominator
            coshd = (mp.cos(th) + mp.cos(al) * mp.cos(be)) / (mp.sin(al) * mp.sin(be))
            if coshd <= 1:
                raise AssertionError("degenerate configuration %s" % ((M, mp_, mq),))
            ratio = (coshd - 1) / target
            count += 1
            if ratio < 1:
                raise AssertionError("eig:sep constant fails at M=%d orders %d,%d: ratio %s"
                                     % (M, mp_, mq, ratio))
            if ratio < worst[0]:
                worst = (ratio, (M, mp_, mq, best))
            r2 = (coshd - 1) / (2 / (mp.pi * M ** 2))
            if r2 < 1:
                raise AssertionError("analytic bound 2/(pi M^2) fails at %s" % ((M, mp_, mq),))
            if r2 < worst_analytic[0]:
                worst_analytic = (r2, (M, mp_, mq, best))

print("sep_exhaustive OK: %d (M, m_p, m_q) configurations with an elliptic product, M <= %d"
      % (count, MMAX))
print("  min (cosh d - 1)/(2/(pi^2 M^2)) = %s at (M, m_p, m_q, theta/pi) = %s"
      % (mp.nstr(worst[0], 8), worst[1]))
print("  min (cosh d - 1)/(2/(pi M^2))   = %s at %s" % (mp.nstr(worst_analytic[0], 8),
                                                         worst_analytic[1]))
