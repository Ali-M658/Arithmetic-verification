"""Example ex:siggenus (SG.13), Corollary N1 (SG.12) arithmetic, Cor S2 bound on examples.

* ex:siggenus: exact shared counts with the actual cone coefficients b_l (Ucar (4.33)).
* Cor N1: with A = q*pi (q rational), lower(A) = floor(log_4(q/2 + 1)) + 2 computed exactly
  (largest t with 4^t <= q/2+1), upper(A) = floor(q) + 4.  Checks, at and around every
  threshold q = 2(4^t - 1) (t = 1..12) and on a grid:
    - L := lower(A) - 1 >= 2  iff  A >= 6 pi;
    - 2 pi (4^{L-1} - 1) <= A, so the Theorem N(a) pair (area < that bound) has area <= A;
    - lower(A) <= upper(A).
"""
import os
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sigcommon import shared_count, s_of  # noqa: E402

F = Fraction

# ---- ex:siggenus -----------------------------------------------------------
pairs = [((1, (15,)), (0, (3, 3, 5, 5)), 2), ((1, (15, 15, 15)), (0, (3, 3, 5, 7, 7, 21)), 3)]
for (g1, m1), (g2, m2), claim in pairs:
    assert s_of(g1, m1) == s_of(g2, m2) > 0
    sc = shared_count(g1, m1, g2, m2, cap=10)
    assert sc >= claim
    print(f"ex:siggenus ({g1};{m1}) vs ({g2};{m2}): Area/2pi = {s_of(g1, m1)}, "
          f"share exactly {sc} coefficients (claim: first {claim})")
    assert sc == claim
    # Cor S2 consistency
    assert sc < int(2 * s_of(g1, m1)) + 4

# literal reading of "j odd, j <= 2L-3" would include j = -3: false already for the first pair
U, V = [15, 1], [3, 3, 5, 5]          # Lemma 4 paddings (d = R(m') - R(m) = 1)
assert sum(F(1, x) for x in U) == sum(F(1, x) for x in V) and sum(U) == sum(V)
assert sum(F(1, x ** 3) for x in U) != sum(F(1, x ** 3) for x in V)
print("wording: with U={15,1}, V={3,3,5,5}: R and P_1 agree but P_{-3} differs, so the range "
      "'j odd, j <= 2L-3' must be read as j in {-1} or 1 <= j <= 2L-3")


# ---- Cor N1 ----------------------------------------------------------------
def flog4(x):
    """floor(log_4 x) for rational x >= 1, exact."""
    assert x >= 1
    t = 0
    while 4 ** (t + 1) <= x:
        t += 1
    return t


def lower(q):
    return flog4(q / 2 + 1) + 2


def upper(q):
    return (q.numerator // q.denominator) + 4


qs = set()
for t in range(1, 13):
    thr = F(2 * (4 ** t - 1))
    for eps in [F(0), F(1, 10 ** 9), F(-1, 10 ** 9), F(1, 3), F(-1, 3)]:
        qs.add(thr + eps)
for num in range(6 * 7, 400 * 7):
    qs.add(F(num, 7))
for q in sorted(qs):
    if q < 6:
        assert flog4(q / 2 + 1) == 0   # below 6 pi the bound would need L = 1
        continue
    lo, up = lower(q), upper(q)
    L = lo - 1
    assert L >= 2
    assert 2 * (4 ** (L - 1) - 1) <= q            # pair area < 2pi(4^{L-1}-1) <= A
    assert 2 * (4 ** L - 1) > q                    # L is the largest admissible
    assert lo <= up
# boundary: just below 6 pi the formula would give L = 1
assert flog4(F(6 - F(1, 10 ** 9)) / 2 + 1) == 0 and flog4(F(6) / 2 + 1) == 1
print("Cor N1: exact floor/log arithmetic at all thresholds 2(4^t-1), t<=12 (+/- 1e-9, +/- 1/3), "
      "and on a grid q in [6,400): L>=2 iff A>=6pi, construction area fits, lower<=upper: OK")
print("  (A = 6pi: lower = 3, upper = 10;  A = 30pi: lower = 4, upper = 34)")
assert lower(F(6)) == 3 and upper(F(6)) == 10 and lower(F(30)) == 4 and upper(F(30)) == 34
print("ALL CHECKS PASSED")
