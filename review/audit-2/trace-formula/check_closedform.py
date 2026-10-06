"""TF.2 (Closed form), exact.

For m = 1..MMAX and k = 0..KMAX, three independent computations of phi_k(m):
  (A) the DEFINING SUM  sum_j 1/(4m sin th_j sin(th_j - u)), via
      1/(sin th sin(th-u)) = (1+cot^2 th)/(cos u - cot th sin u) and the exact
      power sums of the roots cot(pi j/m) of ((X+i)^m-(X-i)^m)/(2i)  (Newton);
  (B) the CLOSED FORM (cot u - m cot mu)/(4 m sin u), by exact power series;
  (C) the BERNOULLI expression (phik) with sigma_i from the series of u/sin u.
Also: sigma_i in Q, sigma_0 = 1, sigma_i > 0, and sigma_i = (4^i-2)|B_2i|/(2i)!.
Exit status nonzero on any failure.
"""
import sys
from fractions import Fraction as Fr
from math import factorial
from tf_lib import (phi_direct, phi_closed, sigmas, mphi_poly, poly_eval,
                    bern_even)

MMAX, KMAX = 12, 40
MMAX_DIRECT_ONLY = 30   # (A) vs (C) also for 13..30

sig = sigmas(KMAX + 2)
assert sig[0] == 1
for i, s in enumerate(sig):
    assert isinstance(s, Fr)
    assert s > 0, (i, s)
    if i >= 1:
        assert s == (Fr(4) ** i - 2) * abs(bern_even(2 * i)) / factorial(2 * i), i
print(f"sigma_i: rational, sigma_0=1, sigma_i>0 and = (4^i-2)|B_2i|/(2i)! for i<={KMAX+2}")
print("  sigma_1..sigma_4 =", [str(s) for s in sig[1:5]])

# Phi_1 = 0
assert all(x == 0 for x in phi_direct(1, KMAX))

nchk = 0
for m in range(1, MMAX_DIRECT_ONLY + 1):
    A = phi_direct(m, KMAX)
    C = [poly_eval(mphi_poly(k, sig), m) / m for k in range(KMAX + 1)]
    assert A == C, ("defining sum vs (phik)", m, next(k for k in range(KMAX + 1) if A[k] != C[k]))
    if m <= MMAX:
        B = phi_closed(m, KMAX)
        assert A == B, ("defining sum vs closed form", m)
    nchk += 1
print(f"(A)=(C) for m=1..{MMAX_DIRECT_ONLY}, (A)=(B) for m=1..{MMAX}, all k<={KMAX}: OK")
print("  phi_0..phi_3 at m=2:", [str(x) for x in phi_direct(2, 3)])
print("  phi_0..phi_3 at m=7:", [str(x) for x in phi_direct(7, 3)])
print("ALL CHECKS PASSED")
sys.exit(0)
