#!/usr/bin/env python3
"""LO.0, LO.2-LO.5, DF.3, DF.5: exact bookkeeping for hyperbolic signatures.

  * hyperbolic  <=>  chi < 0  (Thurston Thm 13.3.6);  Area = -2 pi chi (Thurston 13.3.5 + following sentence)
  * Thurston Cor 13.3.7 dimension -3 chi(X_O) + 2k + l with X_O closed orientable genus g, k = n, l = 0
    equals 6g - 6 + 2n;  it is 0 exactly for (g;n) = (0;3) among hyperbolic signatures, else even and >= 2.
  * boundary cases requested by the editor.

Run from the repository root:  python3 review/audit/locality/check_teich.py
"""
import sys
from itertools import combinations_with_replacement
from fractions import Fraction as Fr

out = []


def chi(g, ms):
    return 2 - 2 * g - sum(1 - Fr(1, m) for m in ms)


def dim_thurston(g, ms):
    chiX = 2 - 2 * g
    k, l = len(ms), 0
    return -3 * chiX + 2 * k + l


def main():
    count = 0
    min_area = None
    for g in range(0, 4):
        for n in range(0, 7):
            for ms in combinations_with_replacement(range(2, 13), n):
                c = chi(g, ms)
                if c >= 0:
                    continue  # not hyperbolic
                count += 1
                d = dim_thurston(g, ms)
                assert d == 6 * g - 6 + 2 * n
                assert d >= 0
                if d == 0:
                    assert (g, n) == (0, 3), (g, ms)
                else:
                    assert d >= 2 and d % 2 == 0
                if min_area is None or -c < min_area[0]:
                    min_area = (-c, g, ms)
    # every (0;3) hyperbolic signature has d = 0
    for ms in combinations_with_replacement(range(2, 40), 3):
        if chi(0, ms) < 0:
            assert dim_thurston(0, ms) == 0
    out.append("[exact] %d hyperbolic signatures (g<=3, n<=6, m<=12): Thurston dim = 6g-6+2n; 0 iff (0;3); otherwise even and >= 2" % count)
    out.append("[exact] smallest |chi| in the enumeration: %s at (%d;%s)  -> area 2pi|chi| = pi/21" % (min_area[0], min_area[1], ",".join(map(str, min_area[2]))))
    assert min_area[0] == Fr(1, 42)

    cases = [(0, (2, 2, 2, 3)), (0, (2, 2, 2, 2, 2)), (1, (2,)), (1, ()), (0, (2, 2, 2, 2)), (0, (2, 3, 7)),
             (0, (2, 3, 6)), (2, ()), (0, (3, 3, 4)), (0, (2, 2, 2, 2, 2, 2))]
    for g, ms in cases:
        c = chi(g, ms)
        hyp = c < 0
        d = dim_thurston(g, ms)
        out.append("        (%d;%s): chi = %s, hyperbolic = %s, area = %s, dim T = %s" % (
            g, ",".join(map(str, ms)), c, hyp, ("%s*pi" % (-2 * c)) if hyp else "-", d if hyp else "n/a (Cor 13.3.7 needs chi<0)"))
    assert chi(1, ()) == 0 and chi(0, (2, 2, 2, 2)) == 0 and chi(0, (2, 3, 6)) == 0
    out.append("[exact] (1;) and (0;2,2,2,2), (0;2,3,6) are Euclidean (chi=0): excluded from every statement, consistent with 'hyperbolic'")
    # c_1 = Area/4pi = -chi/2
    for g, ms in cases:
        c = chi(g, ms)
        if c < 0:
            area_over_pi = -2 * c
            assert area_over_pi / 4 == -c / 2
    out.append("[exact] c_1 = Area/4pi = -chi/2 on all listed hyperbolic cases")
    print("\n".join(out))
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        import traceback
        traceback.print_exc()
        print("ASSERTION FAILED:", e)
        sys.exit(1)
