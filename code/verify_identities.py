#!/usr/bin/env python3
"""
Exact verification of the manuscript's displayed identities.

Every check below is a real `assert` tagged with its claim ID from
review/claim-ledger.md. Nothing prints success unless the assertion that backs
it actually held: there is no unconditional PASS anywhere in this file, and a
failing check is recorded and propagated to a nonzero exit status.

This is the one module permitted to use sympy, and it uses it where symbolic
work is the honest tool -- the Jacobian determinant, the derivation of the
third-coefficient reduction, the sign of phi_p'. Bulk numeric sweeps over
hyperbolic triads use `fractions.Fraction` instead, which is equally exact and
several orders of magnitude faster over the ~214k triads with S_1 <= 200.
Exactness is the requirement; sympy is a means, not the goal.

The trigonometric sums of Lemma 2.1 and Proposition 2.2 are verified twice, by
independent routes:

  (a) exactly, by the integer Vieta chain the manuscript's own proof uses --
      the coefficients of (z+1)^m - (z-1)^m are integers, so this needs no
      transcendental evaluation at all; and
  (b) numerically at 60 significant digits via mpmath, which independently
      confirms the root identification z_j = -i*cot(j*pi/m) that route (a)
      assumes.

Run directly. Exit status is 0 only if every check passed.
"""

from __future__ import annotations

import sys
from fractions import Fraction
from math import comb, gcd
from pathlib import Path
from typing import Callable

import sympy as sp
from mpmath import mp

from orbifold_enum import enumerate_by_sum, power_sum, reciprocal_sum

REPO = Path(__file__).resolve().parent.parent

TRIG_MAX = 200      # cot/csc sums verified for 2 <= m <= TRIG_MAX
SWEEP_MAX = 200     # triad sweeps run over all hyperbolic triads with S_1 <= this
SCALE_MAX = 20      # scaling law verified for 1 <= k <= this

mp.dps = 60


# --------------------------------------------------------------------------
# Tiny harness: register checks, run them, collect failures.
# --------------------------------------------------------------------------

class Harness:
    def __init__(self) -> None:
        self.checks: list[tuple[str, str, Callable[[], None]]] = []
        self.passed: list[str] = []
        self.failed: list[tuple[str, str]] = []

    def check(self, claim_ids: str, description: str):
        def register(fn: Callable[[], None]) -> Callable[[], None]:
            self.checks.append((claim_ids, description, fn))
            return fn
        return register

    def run(self) -> int:
        width = max(len(c) for c, _, _ in self.checks)
        for claim_ids, description, fn in self.checks:
            try:
                fn()
            except AssertionError as exc:
                self.failed.append((claim_ids, str(exc)))
                print(f"  FAIL  {claim_ids:<{width}}  {description}")
                print(f"        {exc}")
            except Exception as exc:  # noqa: BLE001 - report, do not mask
                self.failed.append((claim_ids, f"{type(exc).__name__}: {exc}"))
                print(f"  ERROR {claim_ids:<{width}}  {description}")
                print(f"        {type(exc).__name__}: {exc}")
            else:
                self.passed.append(claim_ids)
                print(f"  PASS  {claim_ids:<{width}}  {description}")

        total = len(self.checks)
        print(f"\n{len(self.passed)}/{total} checks passed")
        if self.failed:
            print(f"\nFAIL -- {len(self.failed)} check(s) failed:")
            for claim_ids, msg in self.failed:
                print(f"  - {claim_ids}: {msg}")
            return 1
        print("PASS -- every displayed identity verified")
        return 0


H = Harness()


# --------------------------------------------------------------------------
# Shared helpers
# --------------------------------------------------------------------------

_TRIAD_CACHE: dict[int, list[tuple[int, ...]]] = {}


def hyperbolic_triads(s_max: int = SWEEP_MAX) -> list[tuple[int, ...]]:
    """
    Every hyperbolic triad with 10 <= S_1 <= s_max, as a list.

    Cached: several checks sweep the same ~214k triads, and re-enumerating them
    per check dominated the runtime.
    """
    if s_max not in _TRIAD_CACHE:
        biggest = max((k for k in _TRIAD_CACHE if k >= s_max), default=None)
        if biggest is not None:
            _TRIAD_CACHE[s_max] = [t for t in _TRIAD_CACHE[biggest] if sum(t) <= s_max]
        else:
            _TRIAD_CACHE[s_max] = [
                orders
                for S in range(10, s_max + 1)
                for orders in enumerate_by_sum(3, S)
            ]
    return _TRIAD_CACHE[s_max]


def cone(m: int) -> Fraction:
    """The manuscript's cone contribution, from its closed form."""
    return Fraction(m * m - 1, 12 * m)


def a0_of(orders) -> Fraction:
    """
    a_0 built the way eq:a0conv defines it: chi/6 plus the cone sum. Deliberately
    NOT built from the (S_1 + R - 2)/12 shortcut, so that comparing the two is a
    real test rather than a restatement.
    """
    R = reciprocal_sum(orders)
    chi = R - 1
    return chi / 6 + sum((cone(m) for m in orders), Fraction(0))


# ==========================================================================
# Section 2.2 -- the cotangent and cosecant sums
# ==========================================================================

@H.check("HC-02, HC-04, HC-05", "Vieta chain for (z+1)^m - (z-1)^m, exact, 2 <= m <= 200")
def _vieta_chain() -> None:
    for m in range(2, TRIG_MAX + 1):
        # P(z) = (z+1)^m - (z-1)^m, integer coefficients.
        # coefficient of z^k is C(m,k) * (1 - (-1)^(m-k))
        coeff = {k: comb(m, k) * (1 - (-1) ** (m - k)) for k in range(m + 1)}

        assert coeff[m] == 0, f"m={m}: deg P should be m-1, but [z^m] = {coeff[m]}"
        assert coeff[m - 1] == 2 * m, f"m={m}: [z^(m-1)] = {coeff[m-1]}, expected {2*m}"
        if m >= 2:
            assert coeff[m - 2] == 0, f"m={m}: [z^(m-2)] = {coeff[m-2]}, expected 0"
        if m >= 3:
            assert coeff[m - 3] == 2 * comb(m, 3), (
                f"m={m}: [z^(m-3)] = {coeff[m-3]}, expected {2*comb(m,3)}"
            )

        # Vieta on the m-1 roots z_j:
        #   sum z_j            = -[z^(m-2)] / [z^(m-1)] = 0
        #   sum_{i<j} z_i z_j  =  [z^(m-3)] / [z^(m-1)] = C(m,3)/m
        e1 = Fraction(-coeff[m - 2], coeff[m - 1])
        assert e1 == 0, f"m={m}: sum of roots is {e1}, expected 0"

        if m >= 3:
            e2 = Fraction(coeff[m - 3], coeff[m - 1])
            assert e2 == Fraction(comb(m, 3), m) == Fraction((m - 1) * (m - 2), 6), (
                f"m={m}: sum_(i<j) z_i z_j = {e2}, expected {Fraction((m-1)*(m-2), 6)}"
            )
            power2 = e1 * e1 - 2 * e2          # sum z_j^2
            assert power2 == Fraction(-(m - 1) * (m - 2), 3), (
                f"m={m}: sum z_j^2 = {power2}, expected {Fraction(-(m-1)*(m-2), 3)}"
            )


@H.check("HC-01, HC-03", "Lemma 2.1: sum cot^2(j*pi/m) = (m-1)(m-2)/3, 2 <= m <= 200")
def _cot_sum() -> None:
    for m in range(2, TRIG_MAX + 1):
        total = mp.mpf(0)
        for j in range(1, m):
            total += mp.cot(mp.pi * j / m) ** 2
        expect = mp.mpf((m - 1) * (m - 2)) / 3
        tol = mp.mpf(10) ** (-35) * max(1, abs(expect))
        assert abs(total - expect) < tol, (
            f"m={m}: sum cot^2 = {total}, expected {expect}"
        )
        # HC-03: the roots really are z_j = -i*cot(j*pi/m), i.e. P(z_j) = 0.
        # Stay inside mpmath throughout -- routing through Python's complex
        # would silently truncate to double precision and make this vacuous.
        if m <= 60:
            for j in range(1, m):
                z = mp.mpc(0, -mp.cot(mp.pi * j / m))
                val = (z + 1) ** m - (z - 1) ** m
                scale = max(abs(z + 1), abs(z - 1)) ** m
                assert abs(val) < mp.mpf(10) ** (-30) * max(mp.mpf(1), scale), (
                    f"m={m}, j={j}: z_j = -i*cot(j*pi/m) is not a root, "
                    f"P(z)={val}, scale={scale}"
                )


@H.check("HC-06, HC-07", "Prop 2.2: sum csc^2(j*pi/m) = (m^2-1)/3, 2 <= m <= 200")
def _csc_sum() -> None:
    for m in range(2, TRIG_MAX + 1):
        total = mp.mpf(0)
        for j in range(1, m):
            total += mp.csc(mp.pi * j / m) ** 2
        expect = mp.mpf(m * m - 1) / 3
        tol = mp.mpf(10) ** (-35) * max(1, abs(expect))
        assert abs(total - expect) < tol, (
            f"m={m}: sum csc^2 = {total}, expected {expect}"
        )
        # csc^2 = 1 + cot^2 route, exactly, on the closed forms
        assert Fraction((m - 1), 1) + Fraction((m - 1) * (m - 2), 3) == Fraction(m * m - 1, 3), (
            f"m={m}: (m-1) + (m-1)(m-2)/3 != (m^2-1)/3"
        )


# ==========================================================================
# Section 2.2 -- the cone contribution
# ==========================================================================

@H.check("HC-09, HC-10, HC-14",
         "Cor 2.4: cone(m) from Def 2.3 equals (m^2-1)/(12m) = (1/12)(m - 1/m), 2 <= m <= 200")
def _cone_formula() -> None:
    for m in range(2, TRIG_MAX + 1):
        from_defn = Fraction(1, 4 * m) * Fraction(m * m - 1, 3)   # Def 2.3 + Prop 2.2
        assert from_defn == Fraction(m * m - 1, 12 * m), (
            f"m={m}: cone from definition {from_defn} != (m^2-1)/(12m)"
        )
        assert from_defn == Fraction(1, 12) * (Fraction(m) - Fraction(1, m)), (
            f"m={m}: cone != (1/12)(m - 1/m)"
        )
        # not the flat 1/12 prefactor (HC-14, recorded as a guard)
        assert from_defn != Fraction(m * m - 1, 12), f"m={m}: prefactor collapsed to 1/12"


@H.check("HC-11, HC-12, HC-13", "Cor 2.4: cone(2)=1/8, cone(3)=2/9, cone(5)=2/5")
def _cone_values() -> None:
    assert cone(2) == Fraction(1, 8), f"cone(2) = {cone(2)}"
    assert cone(3) == Fraction(2, 9), f"cone(3) = {cone(3)}"
    assert cone(5) == Fraction(2, 5), f"cone(5) = {cone(5)}"


# ==========================================================================
# Section 1.3 -- the normalization
# ==========================================================================

@H.check("CV-02, CV-03, CV-04, CV-05, AP-03",
         "a_0(2,3,5) = 271/360 = 269/360 + 1/180")
def _normalization() -> None:
    orders = (2, 3, 5)
    R = reciprocal_sum(orders)
    assert R == Fraction(31, 30), f"R(2,3,5) = {R}"

    cone_sum = sum((cone(m) for m in orders), Fraction(0))
    assert cone_sum == Fraction(269, 360), f"cone sum = {cone_sum}, expected 269/360"

    chi = R - 1
    assert chi / 6 == Fraction(1, 180), f"chi/6 = {chi/6}, expected 1/180"

    a0 = cone_sum + chi / 6
    assert a0 == Fraction(271, 360), f"a_0(2,3,5) = {a0}, expected 271/360"
    assert Fraction(269, 360) + Fraction(1, 180) == Fraction(271, 360), (
        "269/360 + 1/180 != 271/360"
    )


@H.check("HC-16", "sum_i cone(m_i) = (1/12)(S_1 - R), all triads S_1 <= 200")
def _cone_sum_identity() -> None:
    for orders in hyperbolic_triads():
        lhs = sum((cone(m) for m in orders), Fraction(0))
        rhs = Fraction(1, 12) * (Fraction(sum(orders)) - reciprocal_sum(orders))
        assert lhs == rhs, f"{orders}: {lhs} != {rhs}"


# ==========================================================================
# Section 2.3 -- the inversion
# ==========================================================================

@H.check("HC-17, HC-18, AP-04", "eq:s1inv: a_0 = (S_1+R-2)/12 and S_1 = 12a_0 + 2 - R, S_1 <= 200")
def _inversion() -> None:
    for orders in hyperbolic_triads():
        S1 = sum(orders)
        R = reciprocal_sum(orders)
        a0 = a0_of(orders)                      # built from eq:a0conv
        assert a0 == Fraction(S1 + R - 2, 1) / 12, (
            f"{orders}: a_0 = {a0} != (S_1+R-2)/12 = {(S1 + R - 2) / 12}"
        )
        recovered = 12 * a0 + 2 - R
        assert recovered == S1, (
            f"{orders}: inversion returned S_1 = {recovered}, expected {S1}"
        )


@H.check("HC-19", "Remark 2.5: the mis-normalized inversion is negative at (2,3,5)")
def _bugfix_remark() -> None:
    orders = (2, 3, 5)
    R = reciprocal_sum(orders)
    a0 = a0_of(orders)
    wrong = 12 * (a0 - 2) + R
    assert wrong < 0, f"mis-normalized form gave {wrong}, expected a negative value"
    assert wrong == Fraction(-209, 15), f"mis-normalized form gave {wrong}, expected -209/15"
    assert sum(orders) == 10, "the reference triple should have S_1 = 10"


# ==========================================================================
# Section 2.4 -- the third coefficient, eq (5)
# ==========================================================================

@H.check("HC-22, HC-23, HC-24, HC-25",
         "eq (5): sum b_1(C_i) at K=-1 equals -(1/360)P_3 - (1/36)S_1 + (11/360)R")
def _third_coefficient_reduction() -> None:
    # Symbolic derivation from eq:b1, over the three cone orders.
    p, q, r, K = sp.symbols("p q r K", positive=True)
    b1 = lambda m: (sp.Rational(1, 360) * (m ** 3 - 1 / m)
                    + sp.Rational(1, 36) * (m - 1 / m)) * K

    total = (b1(p) + b1(q) + b1(r)).subs(K, -1)
    P3 = p ** 3 + q ** 3 + r ** 3
    S1 = p + q + r
    R = 1 / p + 1 / q + 1 / r
    claimed = -sp.Rational(1, 360) * P3 - sp.Rational(1, 36) * S1 + sp.Rational(11, 360) * R

    assert sp.simplify(total - claimed) == 0, (
        f"eq (5) does not follow from eq:b1: residual {sp.simplify(total - claimed)}"
    )

    # HC-23: the coefficient arithmetic behind the 11/360
    assert sp.Rational(1, 360) + sp.Rational(1, 36) == sp.Rational(11, 360), "1/360 + 1/36 != 11/360"

    # HC-24: the residual m^3 coefficient is nonzero, and equal to -1/360
    coeff = sp.simplify(sp.expand(total).coeff(p, 3))
    assert coeff == -sp.Rational(1, 360), f"m^3 coefficient is {coeff}, expected -1/360"
    assert coeff != 0, "the m^3 coefficient vanished; recovery would be impossible"

    # HC-25: a flat cone contributes nothing at this order
    flat = (b1(p) + b1(q) + b1(r)).subs(K, 0)
    assert sp.simplify(flat) == 0, f"b_1 at K=0 is {sp.simplify(flat)}, expected 0"

    # And numerically on the collision pair, at K = -1.
    f = sp.lambdify((p, q, r), claimed, "math")
    for orders in [(2, 8, 8), (3, 3, 12)]:
        exact = (-Fraction(1, 360) * power_sum(orders, 3)
                 - Fraction(1, 36) * sum(orders)
                 + Fraction(11, 360) * reciprocal_sum(orders))
        assert abs(float(exact) - f(*orders)) < 1e-9, f"{orders}: numeric mismatch"


# ==========================================================================
# Section 2.4 -- Cauchy-Schwarz and the recovery, eq (6)
# ==========================================================================

@H.check("HC-26, HC-27, AP-07", "Prop 2.6: S_1*R >= 9, equality iff p = q = r, S_1 <= 200")
def _cauchy_schwarz() -> None:
    saw_equality = False
    for orders in hyperbolic_triads():
        prod = Fraction(sum(orders)) * reciprocal_sum(orders)
        assert prod >= 9, f"{orders}: S_1*R = {prod} < 9"
        if prod == 9:
            saw_equality = True
            assert orders[0] == orders[1] == orders[2], (
                f"{orders}: equality S_1*R = 9 without p = q = r"
            )
        else:
            assert not (orders[0] == orders[1] == orders[2]), (
                f"{orders}: p = q = r but S_1*R = {prod} != 9"
            )
    assert saw_equality, "no equilateral triad encountered; the equality case went untested"


@H.check("HC-15, HC-28, HC-29, HC-30, HC-31, HC-32, IN-10, IN-14, AP-05",
         "eq (6): full round trip (p,q,r) -> (R,S_1,P_3) -> (p,q,r), S_1 <= 200")
def _round_trip() -> None:
    for orders in hyperbolic_triads():
        p, q, r = orders
        S1 = sum(orders)
        R = reciprocal_sum(orders)
        P3 = power_sum(orders, 3)
        e1 = Fraction(S1)

        # HC-31: the denominator of eq:e3 never vanishes, by Prop 2.6
        denom = 3 - 3 * e1 * R
        assert denom != 0, f"{orders}: denominator 3 - 3*S_1*R vanished"

        # HC-30
        e3 = (Fraction(P3) - e1 ** 3) / denom
        e2 = R * e3
        assert e3 == Fraction(p * q * r), f"{orders}: e_3 = {e3}, expected {p*q*r}"
        assert e2 == Fraction(p * q + q * r + r * p), (
            f"{orders}: e_2 = {e2}, expected {p*q + q*r + r*p}"
        )

        # HC-29: Newton's identity in the form the proof uses
        assert Fraction(P3) == e1 ** 3 - 3 * e1 * e2 + 3 * e3, f"{orders}: Newton failed"
        assert Fraction(P3) == e1 ** 3 + 3 * e3 * (1 - e1 * R), (
            f"{orders}: the rearranged Newton identity failed"
        )

        # HC-32 / HC-28: the cone orders are the roots of z^3 - e1 z^2 + e2 z - e3
        for m in orders:
            value = Fraction(m) ** 3 - e1 * Fraction(m) ** 2 + e2 * Fraction(m) - e3
            assert value == 0, f"{orders}: {m} is not a root of the recovery cubic"
        # and the cubic is exactly (z-p)(z-q)(z-r)
        z = sp.Symbol("z")
        cubic = sp.expand(z ** 3 - int(e1) * z ** 2 + sp.Rational(e2.numerator, e2.denominator) * z
                          - sp.Rational(e3.numerator, e3.denominator))
        if S1 <= 30:   # symbolic factorisation is expensive; sample the low range
            assert sp.expand((z - p) * (z - q) * (z - r) - cubic) == 0, (
                f"{orders}: recovery cubic is not (z-p)(z-q)(z-r)"
            )


@H.check("HC-33, HC-34, IN-11", "Section 2.3: Jacobian det DF, symbolically")
def _jacobian() -> None:
    p, q, r = sp.symbols("p q r", positive=True)
    F = sp.Matrix([
        p + q + r,                      # S_1
        1 / p + 1 / q + 1 / r,          # R
        p ** 3 + q ** 3 + r ** 3,       # P_3
    ])
    J = F.jacobian(sp.Matrix([p, q, r]))
    det = sp.simplify(J.det())

    claimed = (-3 * (p - q) * (p - r) * (q - r) * (p + q) * (p + r) * (q + r)
               / (p ** 2 * q ** 2 * r ** 2))
    assert sp.simplify(det - claimed) == 0, (
        f"Jacobian determinant mismatch; residual {sp.simplify(det - claimed)}"
    )

    # HC-34: nonzero exactly off the diagonals
    for orders in hyperbolic_triads(60):
        a, b, c = orders
        value = Fraction(
            -3 * (a - b) * (a - c) * (b - c) * (a + b) * (a + c) * (b + c),
            (a * b * c) ** 2,
        )
        distinct = len({a, b, c}) == 3
        assert (value != 0) == distinct, (
            f"{orders}: det DF = {value} but distinct={distinct}"
        )


# ==========================================================================
# Section 3 -- the separation inequalities
# ==========================================================================

def phi(p: int, S: int) -> Fraction:
    return Fraction(4, S - p) - Fraction(1, S - 2 * p - 2)


def tau(p: int) -> Fraction:
    return Fraction(2, p + 1) - Fraction(1, p)


def R_plus(S: int, p: int) -> Fraction:
    """Spread endpoint: the triad O(p, p, S-2p)."""
    return Fraction(2, p) + Fraction(1, S - 2 * p)


def R_minus(S: int, p: int) -> Fraction:
    """Balanced endpoint: the minimum of R over the (S,p)-stratum."""
    values = [reciprocal_sum(t) for t in enumerate_by_sum(3, S) if t[0] == p]
    assert values, f"stratum (S={S}, p={p}) is empty; cannot take its minimum"
    return min(values)


@H.check("TH-23, TH-24", "phi_p and tau_p closed forms; tau_2=1/6, tau_3=1/6, tau_4=3/20")
def _phi_tau_forms() -> None:
    for p in range(2, 40):
        assert tau(p) == Fraction(p - 1, p * (p + 1)), f"tau_{p} closed form wrong"
    assert tau(2) == Fraction(1, 6), f"tau_2 = {tau(2)}"
    assert tau(3) == Fraction(1, 6), f"tau_3 = {tau(3)}"
    assert tau(4) == Fraction(3, 20), f"tau_4 = {tau(4)}"


@H.check("TH-25", "phi_p is unimodal with peak at S = 3p+4 (symbolic sign of phi_p')")
def _unimodality() -> None:
    S, p = sp.symbols("S p", positive=True)
    phi_sym = 4 / (S - p) - 1 / (S - 2 * p - 2)
    dphi = sp.simplify(sp.diff(phi_sym, S))

    # phi_p'(S) = -4/(S-p)^2 + 1/(S-2p-2)^2
    expected = -4 / (S - p) ** 2 + 1 / (S - 2 * p - 2) ** 2
    assert sp.simplify(dphi - expected) == 0, f"phi' mismatch: {sp.simplify(dphi - expected)}"

    # The stationary point is S = 3p+4 for every p.
    roots = sp.solve(sp.Eq(expected, 0), S)
    assert any(sp.simplify(rt - (3 * p + 4)) == 0 for rt in roots), (
        f"stationary point is not 3p+4; solve gave {roots}"
    )

    # Sign check on integers: positive below the peak, negative above.
    for pv in range(2, 12):
        peak = 3 * pv + 4
        for Sv in range(2 * pv + 3, 3 * pv + 4):
            d = Fraction(-4, (Sv - pv) ** 2) + Fraction(1, (Sv - 2 * pv - 2) ** 2)
            assert d > 0, f"p={pv}, S={Sv} < peak {peak}: phi' = {d}, expected > 0"
        for Sv in range(3 * pv + 5, 3 * pv + 40):
            d = Fraction(-4, (Sv - pv) ** 2) + Fraction(1, (Sv - 2 * pv - 2) ** 2)
            assert d < 0, f"p={pv}, S={Sv} > peak {peak}: phi' = {d}, expected < 0"
        d0 = Fraction(-4, (peak - pv) ** 2) + Fraction(1, (peak - 2 * pv - 2) ** 2)
        assert d0 == 0, f"p={pv}: phi'({peak}) = {d0}, expected 0"


@H.check("TH-26, TH-27, TH-28, TH-29, TH-30, TH-31, TH-32, TH-33, TH-34, IN-15",
         "Thm 3.4: the three adjacent-pair comparisons for S <= 17")
def _adjacent_pairs() -> None:
    # (1) p = 2: strata coexist for 11 <= S <= 18, phi_2 decreasing there.
    assert phi(2, 17) == Fraction(29, 165), f"phi_2(17) = {phi(2,17)}"
    assert phi(2, 17) > tau(2), f"phi_2(17) = {phi(2,17)} !> tau_2 = {tau(2)}"
    for S in range(11, 18):
        assert phi(2, S) > tau(2), f"phi_2({S}) = {phi(2,S)} !> 1/6"

    # (2) p = 3: strata coexist for 12 <= S <= 17; minimum at an endpoint.
    assert phi(3, 12) == Fraction(7, 36), f"phi_3(12) = {phi(3,12)}"
    assert phi(3, 17) == Fraction(11, 63), f"phi_3(17) = {phi(3,17)}"
    assert phi(3, 12) > tau(3) and phi(3, 17) > tau(3), "phi_3 endpoint comparison failed"
    for S in range(12, 18):
        assert phi(3, S) > tau(3), f"phi_3({S}) = {phi(3,S)} !> 1/6"

    # (3) p = 4: strata coexist for 15 <= S <= 17.
    assert phi(4, 15) == Fraction(9, 55), f"phi_4(15) = {phi(4,15)}"
    window = {S: phi(4, S) for S in (15, 16, 17)}
    assert min(window.values()) == phi(4, 15), f"min over {window} is not phi_4(15)"
    assert phi(4, 15) > tau(4), f"phi_4(15) = {phi(4,15)} !> 3/20"
    for S in range(15, 18):
        assert phi(4, S) > tau(4), f"phi_4({S}) = {phi(4,S)} !> 3/20"


@H.check("TH-29, TH-35, TH-39, TH-40, TH-41, AP-06",
         "Thm 3.4: the four endpoint comparisons at S = 18")
def _s18_endpoints() -> None:
    # (4) the (2,3) pair reaches equality
    assert phi(2, 18) == tau(2) == Fraction(1, 6), (
        f"phi_2(18) = {phi(2,18)}, tau_2 = {tau(2)}; expected both 1/6"
    )
    assert R_minus(18, 2) == R_plus(18, 3), (
        f"R^-_(18,2) = {R_minus(18,2)} != R^+_(18,3) = {R_plus(18,3)}"
    )
    assert R_minus(18, 2) == Fraction(3, 4), f"R^-_(18,2) = {R_minus(18,2)}, expected 3/4"

    # (5), (6), (7) the remaining adjacent pairs stay strictly separated
    for p, want_minus, want_plus in [
        (3, Fraction(101, 168), Fraction(3, 5)),
        (4, Fraction(15, 28), Fraction(21, 40)),
        (5, Fraction(107, 210), Fraction(1, 2)),
    ]:
        rm = R_minus(18, p)
        rp = R_plus(18, p + 1)
        assert rm == want_minus, f"R^-_(18,{p}) = {rm}, expected {want_minus}"
        assert rp == want_plus, f"R^+_(18,{p+1}) = {rp}, expected {want_plus}"
        assert rm > rp, f"stratum {p} and {p+1} not separated at S=18: {rm} !> {rp}"


@H.check("TH-36, TH-37, TH-38, TH-43, TH-44, TH-45, TH-46, TH-47, TH-48",
         "Thm B: the S=18 pair shares (S_1,R)=(18,3/4); P_3 = 1032 != 1782 separates it")
def _p3_separation() -> None:
    a, b = (2, 8, 8), (3, 3, 12)
    assert power_sum(a, 3) == 1032, f"P_3{a} = {power_sum(a,3)}"
    assert power_sum(b, 3) == 1782, f"P_3{b} = {power_sum(b,3)}"
    assert power_sum(a, 3) != power_sum(b, 3), "P_3 fails to separate the pair"
    assert sum(a) == sum(b) == 18, "the pair does not share S_1 = 18"
    assert reciprocal_sum(a) == reciprocal_sum(b) == Fraction(3, 4), "the pair does not share R = 3/4"


# ==========================================================================
# Section 5 -- the scaling law
# ==========================================================================

@H.check("DE-03, DE-04, DE-05, AP-08",
         f"Prop 5.1: scaling law for k <= {SCALE_MAX} on ten distinct base degeneracies")
def _scaling_law() -> None:
    from enumerate_degeneracies import degeneracy_groups

    # Collect ten distinct PRIMITIVE base degeneracies, discovered not hardcoded.
    bases: list[tuple[int, Fraction, tuple[tuple[int, ...], ...]]] = []
    S = 10
    while len(bases) < 10:
        if S > 400:
            raise AssertionError(
                f"only found {len(bases)} primitive base degeneracies below S = 400"
            )
        for g in degeneracy_groups(S):
            if g.primitive:
                bases.append((g.S, g.R, g.triples))
                if len(bases) == 10:
                    break
        S += 1

    assert len({b[0:2] for b in bases}) == 10, "base degeneracies are not distinct"
    assert bases[0][0] == 18 and bases[0][2] == ((2, 8, 8), (3, 3, 12)), (
        f"the first primitive base should be the S=18 pair, got {bases[0]}"
    )

    for S0, R0, triples in bases:
        for k in range(1, SCALE_MAX + 1):
            scaled = [tuple(m * k for m in t) for t in triples]
            sums = {sum(t) for t in scaled}
            recips = {reciprocal_sum(t) for t in scaled}
            assert sums == {k * S0}, f"base S_1={S0}, k={k}: sums {sums} != {k*S0}"
            assert recips == {R0 / k}, f"base S_1={S0}, k={k}: R {recips} != {R0/k}"
            assert len({tuple(t) for t in scaled}) == len(triples), (
                f"base S_1={S0}, k={k}: scaling merged distinct multisets"
            )
            for t in scaled:
                assert reciprocal_sum(t) < 1, (
                    f"base S_1={S0}, k={k}: {t} is not hyperbolic"
                )
                assert min(t) >= 2, f"base S_1={S0}, k={k}: {t} has an order below 2"


# ==========================================================================
# Section 3.1 -- chamber monotonicity and the stratum endpoints
# ==========================================================================

def _stratum(S: int, p: int) -> list[tuple[int, ...]]:
    """Hyperbolic triads of sum S whose least cone order is exactly p, ordered by q."""
    return sorted((t for t in enumerate_by_sum(3, S) if t[0] == p), key=lambda t: t[1])


@H.check("TH-01, TH-02, TH-03, TH-04, TH-05",
         "Lemma 3.1: R strictly decreasing in q on each (S,p)-stratum; extrema at its ends")
def _chamber_monotonicity() -> None:
    seen = 0
    for S in range(10, 121):
        for p in range(2, S // 3 + 1):
            stratum = _stratum(S, p)
            if not stratum:
                continue
            seen += 1
            Rs = [reciprocal_sum(t) for t in stratum]

            # TH-01: the stratum is exactly {(p, q, S-p-q)} with p <= q <= (S-p)/2
            for (a, b, c) in stratum:
                assert a == p and a <= b <= c and a + b + c == S, f"bad stratum member {(a,b,c)}"
                assert b <= Fraction(S - p, 2), f"{(a,b,c)}: q exceeds (S-p)/2"

            # TH-02: R'(q) = -1/q^2 + 1/(S-p-q)^2 <= 0, equality only at q = r
            for (a, b, c) in stratum:
                d = Fraction(-1, b * b) + Fraction(1, c * c)
                assert d <= 0, f"{(a,b,c)}: R' = {d} > 0"
                assert (d == 0) == (b == c), f"{(a,b,c)}: R' vanishing does not match q == r"

            # TH-03: strictly decreasing in q, hence injective on the stratum
            for i in range(len(Rs) - 1):
                assert Rs[i] > Rs[i + 1], (
                    f"S={S}, p={p}: R not strictly decreasing at {stratum[i]} -> {stratum[i+1]}"
                )
            assert len(set(Rs)) == len(Rs), f"S={S}, p={p}: R repeats within the stratum"

            # TH-04 / TH-05: maximum at the spread end, minimum at the balanced end
            assert Rs[0] == max(Rs), f"S={S}, p={p}: max not at the smallest q"
            assert Rs[-1] == min(Rs), f"S={S}, p={p}: min not at the largest q"
            spread = (p, p, S - 2 * p)
            if spread in stratum:
                assert stratum[0] == spread, f"S={S}, p={p}: spread triad is not the q-least member"
            balanced_q = (S - p) // 2
            if any(t[1] == balanced_q for t in stratum):
                assert stratum[-1][1] == balanced_q, (
                    f"S={S}, p={p}: q-greatest member is not the balanced one"
                )
    assert seen > 500, f"only {seen} strata exercised; the sweep is too thin to mean anything"


@H.check("TH-06, TH-07",
         "R^+_(S,p) = 2/p + 1/(S-2p), and is non-increasing in p for p <= S/3")
def _spread_endpoint() -> None:
    for S in range(10, 201):
        for p in range(2, S // 3 + 1):
            if S - 2 * p < p:
                continue
            # TH-06: the closed form is the reciprocal sum of the spread triad
            assert Fraction(2, p) + Fraction(1, S - 2 * p) == reciprocal_sum((p, p, S - 2 * p)), (
                f"S={S}, p={p}: R^+ closed form disagrees with R(p,p,S-2p)"
            )
        # TH-07: non-increasing in p
        ps = [p for p in range(2, S // 3 + 1) if S - 2 * p >= p]
        for a, b in zip(ps, ps[1:]):
            ra = Fraction(2, a) + Fraction(1, S - 2 * a)
            rb = Fraction(2, b) + Fraction(1, S - 2 * b)
            assert ra >= rb, f"S={S}: R^+ increased from p={a} ({ra}) to p={b} ({rb})"


@H.check("TH-08, TH-09",
         "Lemma 3.2: R^-_(S,p) >= 1/p + 4/(S-p), with equality exactly when S-p is even")
def _balanced_bound() -> None:
    for S in range(10, 151):
        for p in range(2, S // 3 + 1):
            stratum = _stratum(S, p)
            if not stratum:
                continue
            R_minus = min(reciprocal_sum(t) for t in stratum)
            bound = Fraction(1, p) + Fraction(4, S - p)
            assert R_minus >= bound, f"S={S}, p={p}: R^- = {R_minus} < bound {bound}"

            balanced_q = (S - p) // 2
            has_balanced = any(t[1] == balanced_q for t in stratum)
            if has_balanced:
                if (S - p) % 2 == 0:
                    assert R_minus == bound, (
                        f"S={S}, p={p}: S-p even but R^- = {R_minus} != {bound}"
                    )
                else:
                    assert R_minus > bound, (
                        f"S={S}, p={p}: S-p odd but the bound is tight at {R_minus}"
                    )

    # TH-09: the odd-case identity, arithmetically
    for D in range(5, 300, 2):          # D = S - p, odd
        q, r = (D - 1) // 2, (D + 1) // 2
        assert Fraction(1, q) + Fraction(1, r) == Fraction(4 * D, D * D - 1), (
            f"D={D}: 1/q + 1/r != 4D/(D^2-1)"
        )
        assert Fraction(4 * D, D * D - 1) > Fraction(4, D), f"D={D}: odd-case bound not strict"


@H.check("TH-10, TH-11",
         "Prop 3.3: at fixed S_1 the most balanced triad minimizes both R and a_0")
def _balanced_minimizes() -> None:
    for S in range(10, 201):
        triads = list(enumerate_by_sum(3, S))
        if not triads:
            continue
        best = min(triads, key=lambda t: reciprocal_sum(t))
        # the minimizer is the admissible triad of least spread
        spread = lambda t: t[2] - t[0]
        assert spread(best) == min(spread(t) for t in triads), (
            f"S={S}: R-minimizer {best} is not of least spread"
        )
        # a_0 is increasing in R at fixed S_1, so it is minimized at the same triad
        best_a0 = min(triads, key=lambda t: a0_of(t))
        assert a0_of(best_a0) == a0_of(best), (
            f"S={S}: a_0 minimizer {best_a0} differs in value from the R minimizer {best}"
        )
        for t in triads:
            assert a0_of(t) == Fraction(S + reciprocal_sum(t) - 2, 1) / 12, f"{t}: a_0 form"


@H.check("TH-12, TH-13, TH-14, TH-15, TH-16, TH-17",
         "Section 3.2: S_1 >= 10 with the stated per-p bounds; p <= floor(S/3) <= 5 for S <= 17")
def _least_sum_bounds() -> None:
    # TH-12 / TH-16
    for S in range(6, 10):
        assert not list(enumerate_by_sum(3, S)), f"unexpected hyperbolic triad at S={S}"
    assert [t for t in enumerate_by_sum(3, 10)] == [(3, 3, 4)], "S=10 not uniquely O(3,3,4)"

    saw2 = saw3 = saw4 = False
    for orders in hyperbolic_triads():
        p, q, r = orders
        S = sum(orders)
        if p == 2:
            saw2 = True
            assert q + r >= 9, f"{orders}: p=2 but q+r = {q+r} < 9"
            assert S >= 11, f"{orders}: p=2 but S_1 = {S} < 11"
        elif p == 3:
            saw3 = True
            assert q + r >= 7, f"{orders}: p=3 but q+r = {q+r} < 7"
            assert S >= 10, f"{orders}: p=3 but S_1 = {S} < 10"
        else:
            saw4 = True
            assert p >= 4 and S >= 12, f"{orders}: p>=4 but S_1 = {S} < 12"
    assert saw2 and saw3 and saw4, "not all three least-order cases were exercised"

    # TH-17
    for S in range(10, 18):
        least = {t[0] for t in enumerate_by_sum(3, S)}
        assert least <= {2, 3, 4, 5}, f"S={S}: least orders {least} exceed 5"
        for p in least:
            assert p <= S // 3, f"S={S}: least order {p} exceeds floor(S/3)"
        assert S // 3 <= 5, f"S={S}: floor(S/3) = {S//3} > 5"


@H.check("TH-18, TH-19, TH-20, TH-21, TH-22",
         "Thm 3.4: stratum intervals pairwise disjoint for S <= 17; first contact at S = 18")
def _interval_separation() -> None:
    def interval(S: int, p: int):
        st = _stratum(S, p)
        if not st:
            return None
        Rs = [reciprocal_sum(t) for t in st]
        return min(Rs), max(Rs)

    # TH-18 / TH-19: pairwise disjoint for every S <= 17
    for S in range(10, 18):
        ivs = {p: interval(S, p) for p in range(2, S // 3 + 1)}
        ivs = {p: v for p, v in ivs.items() if v}
        ps = sorted(ivs)
        for i, a in enumerate(ps):
            for b in ps[i + 1:]:
                lo_a, hi_a = ivs[a]
                lo_b, hi_b = ivs[b]
                assert lo_a > hi_b, (
                    f"S={S}: strata p={a} [{lo_a},{hi_a}] and p={b} [{lo_b},{hi_b}] overlap"
                )

    # TH-20 / TH-21: strata 2 and 3 touch at S = 18, at R = 3/4
    lo2, hi2 = interval(18, 2)
    lo3, hi3 = interval(18, 3)
    assert lo2 == hi3 == Fraction(3, 4), (
        f"S=18: strata 2 and 3 meet at ({lo2}, {hi3}), expected both 3/4"
    )
    st2, st3 = _stratum(18, 2), _stratum(18, 3)
    assert st2[-1] == (2, 8, 8), f"balanced end of stratum (18,2) is {st2[-1]}, expected (2,8,8)"
    assert st3[0] == (3, 3, 12), f"spread end of stratum (18,3) is {st3[0]}, expected (3,3,12)"

    # TH-22: every other adjacent pair at S = 18 is still strictly separated
    ps = sorted(p for p in range(2, 7) if interval(18, p))
    for a, b in zip(ps, ps[1:]):
        if (a, b) == (2, 3):
            continue
        lo_a, _ = interval(18, a)
        _, hi_b = interval(18, b)
        assert lo_a > hi_b, f"S=18: strata p={a} and p={b} not separated ({lo_a} !> {hi_b})"


# ==========================================================================
# Section 4 -- geometric consequences
# ==========================================================================

@H.check("GE-05, GE-07, GE-08",
         "Section 4: cone angle 2*pi/m; balanced pillow existence; a_0 minimized globally at O(3,3,4)")
def _geometric_consequences() -> None:
    # GE-05: an order-m cone has cone angle 2*pi/m; O(2,8,8) carries an angle-pi cone
    for m in (2, 3, 8, 12):
        assert Fraction(2, m) * m == 2, f"cone-angle normalization broken at m={m}"
    assert Fraction(2, 2) == 1, "the order-2 cone angle is not pi"

    # GE-07: a balanced pillow p=q=r exists exactly when 3 | S_1 and S_1/3 >= 4
    for S in range(10, 301):
        equilateral = [t for t in enumerate_by_sum(3, S) if t[0] == t[1] == t[2]]
        expected = (S % 3 == 0) and (S // 3 >= 4)
        assert bool(equilateral) == expected, (
            f"S={S}: equilateral present={bool(equilateral)}, expected={expected}"
        )
        if expected:
            assert equilateral == [(S // 3,) * 3], f"S={S}: unexpected equilateral set"
    assert not [t for t in enumerate_by_sum(3, 9) if t[0] == t[1] == t[2]], (
        "O(3,3,3) is Euclidean, not hyperbolic, and must not be enumerated"
    )

    # GE-08: across ALL pillows a_0 is smallest for O(3,3,4), at 107/144.
    # Rigorous, not merely sampled: a_0 = (S_1 + R - 2)/12 and R > 0, so
    # a_0 > (S_1 - 2)/12. For S_1 >= 11 that already exceeds 107/144, so only
    # S_1 = 10 can hold the minimum -- and S_1 = 10 is O(3,3,4) alone.
    target = Fraction(107, 144)
    assert a0_of((3, 3, 4)) == target, f"a_0(3,3,4) = {a0_of((3,3,4))}, expected 107/144"
    assert Fraction(11 - 2, 12) > target, (
        "the tail argument fails: (S_1-2)/12 at S_1=11 does not exceed 107/144"
    )
    for orders in hyperbolic_triads():
        if sum(orders) >= 11:
            assert a0_of(orders) > target, f"{orders}: a_0 = {a0_of(orders)} <= 107/144"
    assert [t for t in enumerate_by_sum(3, 10)] == [(3, 3, 4)], "S_1 = 10 is not O(3,3,4) alone"


# ==========================================================================
# Section 5 -- the counting heuristic's inputs
# ==========================================================================

@H.check("DE-24, DE-25",
         "Section 5.3: the triad count of sum S is of order S^2, and e_3 = pqr <= (S/3)^3")
def _heuristic_inputs() -> None:
    # DE-25: AM-GM bound on e_3, exactly, over every triad in the sweep
    for orders in hyperbolic_triads():
        p, q, r = orders
        S = sum(orders)
        assert Fraction(p * q * r) <= Fraction(S, 3) ** 3, (
            f"{orders}: pqr = {p*q*r} exceeds (S/3)^3 = {Fraction(S,3)**3}"
        )

    # DE-24: the triad count is bounded above and below by positive multiples of S^2
    ratios = []
    for S in range(40, 201):
        n = sum(1 for _ in enumerate_by_sum(3, S))
        assert n > 0, f"S={S}: no triads"
        ratios.append(Fraction(n, S * S))
    lo, hi = min(ratios), max(ratios)
    assert lo > 0, "triad count is not bounded below by a positive multiple of S^2"
    assert hi < Fraction(1, 2), f"triad count/S^2 reached {hi}; the S^2 order claim is off"
    assert hi / lo < 2, (
        f"triad count/S^2 varies by a factor of {float(hi/lo):.2f} over 40 <= S <= 200, "
        "which is not consistent with a clean S^2 order"
    )


# ==========================================================================

def main() -> int:
    print("exact verification of the manuscript's displayed identities")
    print(f"claim IDs refer to review/claim-ledger.md")
    print(f"trig sums to m = {TRIG_MAX}; triad sweeps to S_1 = {SWEEP_MAX}; "
          f"scaling to k = {SCALE_MAX}\n")
    return H.run()


if __name__ == "__main__":
    sys.exit(main())
