"""Systoles of the triangle orbifolds O(2,3,m) found by a word search (eigen paper, after Proposition 8.2).

    .venv/bin/python theory/eigen/systole_233.py          (about 1 min)

Proposition 8.2 proves systole >= sigma_* = 0.56206... for every m >= 7. This script shows how far that
bound is from the truth: in Gamma_m = <a, b | a^2 = b^3 = (ab)^m = 1>, represented in SL(2,R) with
tr a = 0, tr b = 1, tr ab = -2 cos(pi/m), it lists every word (a b^{+-1})^L, L <= 12 (word length <= 24),
and takes the least translation length 2 arccosh(|tr|/2) of a hyperbolic one. Every element of Gamma_m is
conjugate to such a word or to an elliptic one, so this is the length of the shortest closed geodesic
among the words searched: an upper bound for the systole, equal to it once the search is long enough.
Asserted: the value for m = 7 is 0.98398..., the known systole of O(2,3,7); the values increase with m;
all lie below 2 arccosh(3/2) = 1.9248..., the systole of the modular orbifold O(2,3,infinity), and above
sigma_*. 40-digit floating point (mpmath), not interval arithmetic.
"""
import itertools

import mpmath as mp

mp.mp.dps = 40
ORDERS = (7, 8, 9, 10, 12, 15, 20, 30, 50, 100)
DEPTH = 12


def generators(m):
    """a of order 2 (trace 0), b of order 3 (trace 1), tr(ab) = -2 cos(pi/m)."""
    A = mp.matrix([[0, 1], [-1, 0]])
    tb, tab = mp.mpf(1), -2 * mp.cos(mp.pi / m)
    # B = [[l, u], [v, tb - l]] with l = tb/2; tr(AB) = v - u, det B = 1
    l = tb / 2
    d = tab
    k = l * (tb - l) - 1
    u = (-d + mp.sqrt(d * d + 4 * k)) / 2
    v = u + d
    B = mp.matrix([[l, u], [v, tb - l]])
    assert abs(mp.det(B) - 1) < mp.mpf(10) ** -35 and abs((A * B)[0, 0] + (A * B)[1, 1] - tab) < mp.mpf(10) ** -35
    assert mp.norm(A * A + mp.eye(2)) < mp.mpf(10) ** -35          # a^2 = -1 in SL(2,R)
    assert mp.norm(B * B * B + mp.eye(2)) < mp.mpf(10) ** -30      # b^3 = -1
    return A, B


def shortest(m, depth=DEPTH):
    A, B = generators(m)
    Bi = B ** -1
    best = mp.inf
    for L in range(1, depth + 1):
        for signs in itertools.product((1, -1), repeat=L):
            M = mp.eye(2)
            for e in signs:
                M = M * A * (B if e == 1 else Bi)
            t = abs(M[0, 0] + M[1, 1])
            if t > 2 + mp.mpf(10) ** -20:
                best = min(best, 2 * mp.acosh(t / 2))
    return best


def main():
    s_inf = mp.acosh(2 / mp.sqrt(3))
    sigma_star = 2 * mp.asinh(1 / (2 * mp.sqrt(1 + mp.mpf(3) / 4 * mp.cosh(2 * s_inf) ** 2)))
    modular = 2 * mp.acosh(mp.mpf(3) / 2)
    vals = [(m, shortest(m)) for m in ORDERS]
    assert abs(vals[0][1] - mp.mpf("0.983986")) < mp.mpf("1e-6"), vals[0]
    assert all(a[1] < b[1] for a, b in zip(vals, vals[1:])), "not increasing in m"
    assert all(sigma_star < v < modular for _, v in vals)
    print(f"sigma_* = {mp.nstr(sigma_star, 8)}; modular systole 2 arccosh(3/2) = {mp.nstr(modular, 8)}")
    for m, v in vals:
        print(f"m = {m:3d}: shortest closed geodesic among words of length <= {2 * DEPTH}: {mp.nstr(v, 8)}")
    print("systole_233: assertions passed")


if __name__ == "__main__":
    main()
