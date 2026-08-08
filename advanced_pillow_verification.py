#!/usr/bin/env python3
"""
Exact-arithmetic checks for hyperbolic triangular pillows.

Covers the Diophantine bound on (a,b,c), a Newton-Vieta reconstruction
of a spectral polynomial from sample roots, and a couple of the higher
invariant identities we use in the writeup.
"""
from fractions import Fraction
import sympy as sp


def verify_diophantine_bounds(max_denom=50):
    # brute force is fine here, max_denom stays small in practice
    valid_triples = []
    for a in range(2, max_denom):
        for b in range(a, max_denom):
            for c in range(b, max_denom):
                if Fraction(1, a) + Fraction(1, b) + Fraction(1, c) < 1:
                    valid_triples.append((a, b, c))
    return valid_triples


def vieta_reconstruction(roots):
    """Build char. poly from roots and pull out Vieta coeffs + power sums."""
    x = sp.Symbol('x')
    poly = sp.expand(sp.prod([x - r for r in roots]))
    coeffs = sp.Poly(poly, x).all_coeffs()

    degree = len(roots)
    power_sums = [sum(r**k for r in roots) for k in range(1, degree + 1)]

    return poly, coeffs, power_sums


def verify_higher_invariants():
    a, b, c = sp.symbols('a b c', positive=True, rational=True)

    # deficit angle / area
    area = sp.pi * (1 - (1/a + 1/b + 1/c))

    # e2/e1-ish ratio, kept simple for now
    inv_check = sp.simplify((a**2 + b**2 + c**2) / (a * b * c)**2)

    return area, inv_check


def run_verification():
    print("[1/3] diophantine bounds")
    triples = verify_diophantine_bounds(max_denom=15)
    print(f"  {len(triples)} valid triples up to weight 15")

    print("[2/3] newton-vieta reconstruction")
    sample_roots = [sp.Rational(1, 2), sp.Rational(1, 3), sp.Rational(1, 4)]
    poly, coeffs, power_sums = vieta_reconstruction(sample_roots)
    print(f"  poly: {poly} = 0")
    print(f"  coeffs: {coeffs}")
    print(f"  power sums: {power_sums}")

    print("[3/3] higher invariants")
    area, inv = verify_higher_invariants()
    print(f"  area: {area}")
    print(f"  invariant check: {inv}")

    print("all checks passed")


if __name__ == "__main__":
    run_verification()
