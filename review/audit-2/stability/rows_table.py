"""Printed ST.14/SB.4 table (verbatim values) and grid-search helpers shared by the check scripts."""
from fractions import Fraction as Fr

TABLE = [  # m, dthm, dcert, dup, ratio, built, relprec, eps
    ((2, 8, 8), '3.80e-07', '2.341e-03', '2.485e-03', '1.06', '8-1/2', ['1.8e-02', '1.6e-03', '7.0e-04'], '1.9e-03'),
    ((3, 3, 12), '1.18e-07', '4.040e-03', '4.589e-03', '1.14', '3+1/2', ['3.2e-02', '2.8e-03', '7.4e-04'], '4.4e-03'),
    ((3, 10, 15, 30), '4.02e-11', '3.660e-03', '7.488e-03', '2.05', '10+1/2',
     ['4.9e-03', '8.0e-04', '4.1e-05', '3.6e-07'], '8.7e-04'),
    ((4, 5, 21, 28), '3.14e-11', '1.461e-03', '2.018e-03', '1.38', '5-1/2',
     ['1.9e-03', '3.2e-04', '1.6e-05', '1.7e-07'], '4.6e-04'),
    ((2, 3, 7), '4.49e-07', '3.658e-03', '6.587e-03', '1.80', '3-1/2', ['3.0e-01', '4.0e-03', '2.7e-03'], '5.0e-03'),
    ((4, 4, 4), '9.35e-07', '4.539e-04', '5.036e-04', '1.11', '4+1/2', ['3.6e-03', '5.0e-04', '5.4e-04'], '8.2e-04'),
    ((7, 7, 7), '9.97e-08', '8.068e-05', '8.273e-05', '1.03', '7-1/2', ['2.8e-04', '4.9e-05', '2.3e-05'], '1.2e-04'),
    ((3, 3, 4, 4), '1.48e-09', '9.597e-05', '1.195e-04', '1.24', '4-1/2',
     ['2.3e-04', '1.0e-04', '1.1e-04', '7.2e-05'], '1.1e-04'),
    ((5, 5, 5, 5), '4.74e-10', '3.617e-05', '3.826e-05', '1.06', '5-1/2',
     ['6.0e-05', '2.5e-05', '1.9e-05', '6.2e-06'], '3.1e-05'),
    ((2, 2, 2, 3), '2.03e-09', '1.858e-04', '2.520e-04', '1.36', '3-1/2',
     ['2.2e-03', '3.2e-04', '5.6e-04', '7.7e-04'], '4.3e-04'),
    ((2, 2, 2, 2, 3), '2.72e-12', '7.908e-06', '5.743e-05', '7.26', '2+1/2',
     ['2.3e-05', '1.2e-05', '2.1e-05', '2.9e-05', '1.9e-05'], '1.4e-05'),
]

def passes(res, mode):
    return res['spec'] and res[mode]


def max_sig(fun, digits, mode):
    """Largest value x on the `digits`-s.f. grid with fun(x) passing (monotone). Returns (q, exp)."""
    # exponent: find decade
    e = 0
    while passes(fun(Fr(10) ** e), mode):
        e += 1
    while not passes(fun(Fr(10) ** e), mode):
        e -= 1
        if e < -40:
            return None
    # now 10^e passes, 10^(e+1) fails; bisect mantissa in [10^(d-1), 10^d)
    lo, hi = 10 ** (digits - 1), 10 ** digits  # lo passes, hi fails
    sc = e - (digits - 1)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if passes(fun(Fr(mid) * Fr(10) ** sc), mode):
            lo = mid
        else:
            hi = mid
    return lo, sc


