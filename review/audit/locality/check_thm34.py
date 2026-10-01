#!/usr/bin/env python3
"""LO.8 (Lemma 3.3), LO.9 (Theorem 3.4 (b),(c)), LO.10, LO.11 (Theorem 3.5): exact checks.

Run from the repository root:  python3 review/audit/locality/check_thm34.py
Exits nonzero on any failed assertion.  mpmath appears only in labelled sanity lines.
"""
import sys
import sympy as sp
import mpmath as mp

L, t, t1, l, A, delta, x = sp.symbols('L t t1 ell A delta x', positive=True)
out = []


def lemma33():
    # 2 pi (cosh x - 1) <= pi e^x   <=>   e^x/2 - cosh x + 1 = 1 - e^{-x}/2 > 0
    diff = sp.simplify((sp.exp(x) / 2 - sp.cosh(x) + 1).rewrite(sp.exp) - (1 - sp.exp(-x) / 2))
    assert diff == 0
    out.append("[exact] Lemma 3.3, second inequality: pi e^x - 2pi(cosh x - 1) = 2pi(1 - e^{-x}/2) > 0")
    # area of a hyperbolic disc of radius R: 2 pi (cosh R - 1)
    rho, R = sp.symbols('rho R', positive=True)
    assert sp.simplify(sp.integrate(2 * sp.pi * sp.sinh(rho), (rho, 0, R)) - 2 * sp.pi * (sp.cosh(R) - 1)) == 0
    out.append("[exact] Area B(R) = int_0^R 2 pi sinh(rho) d rho = 2 pi (cosh R - 1)")


def thm34b():
    phi = L / 2 - L ** 2 / (4 * t)
    f = L * sp.exp(-L / 2) * sp.exp(-L ** 2 / (4 * t))
    # (i) logarithmic derivative
    assert sp.simplify(-sp.diff(f, L) / f - (L / (2 * t) + sp.Rational(1, 2) - 1 / L)) == 0
    # (ii) positivity of -f' on [ell, oo) for t <= ell^2/(2(1+ell)):
    #      L/(2t) + 1/2 - 1/L is increasing in L; at L=ell, with t = ell^2/(2(1+ell)) * s, 0<s<=1,
    s = sp.Symbol('s', positive=True)
    at_ell = (l / (2 * t) + sp.Rational(1, 2) - 1 / l).subs(t, l ** 2 / (2 * (1 + l)) * s)
    # = (1+ell)/(ell s) + 1/2 - 1/ell >= (1+ell)/ell + 1/2 - 1/ell = 3/2 for s <= 1
    assert sp.simplify(at_ell.subs(s, 1) - sp.Rational(3, 2)) == 0
    assert sp.simplify(sp.diff(at_ell, s) + (1 + l) / (l * s ** 2)) == 0  # decreasing in s: smaller t is better
    assert sp.simplify(sp.diff(L / (2 * t) + sp.Rational(1, 2) - 1 / L, L) - (1 / (2 * t) + 1 / L ** 2)) == 0
    out.append("[exact] -f'/f = L/2t + 1/2 - 1/L, increasing in L, equal to 3/2 at L=ell on the boundary t = ell^2/(2(1+ell)) (larger for smaller t)")
    # the monotonicity alone only needs t <= ell^2/(2-ell) (ell<2); the stated range is inside it:
    assert sp.simplify(l ** 2 / (2 - l) - l ** 2 / (2 * (1 + l)) - 3 * l ** 3 / (2 * (2 - l) * (1 + l))) == 0
    out.append("[exact] ell^2/(2-ell) - ell^2/(2(1+ell)) = 3 ell^3/(2(2-ell)(1+ell)) > 0: stated range is sufficient, not sharp")
    # t < ell on the range (needed for ell - t > 0)
    assert sp.simplify(l - l ** 2 / (2 * (1 + l)) - l * (2 + l) / (2 * (1 + l))) == 0
    out.append("[exact] ell - ell^2/(2(1+ell)) = ell(2+ell)/(2(1+ell)) > 0, so ell - t > 0 on the range")
    # (iii) -f' e^L = -(L e^phi)' + L e^phi
    lhs = -sp.diff(f, L) * sp.exp(L)
    rhs = -sp.diff(L * sp.exp(phi), L) + L * sp.exp(phi)
    assert sp.simplify(lhs - rhs) == 0
    out.append("[exact] -f'(L) e^L = -(L e^phi)' + L e^phi, phi = L/2 - L^2/4t")
    # (iv) D(L) = 2tL/(L-t) e^phi satisfies -D' - L e^phi = 2t^2 e^phi/(L-t)^2 >= 0, D(oo)=0
    D = 2 * t * L / (L - t) * sp.exp(phi)
    assert sp.simplify(-sp.diff(D, L) - L * sp.exp(phi) - 2 * t ** 2 * sp.exp(phi) / (L - t) ** 2) == 0
    assert sp.limit(D.subs(t, sp.Rational(1, 3)), L, sp.oo) == 0
    out.append("[exact] D = 2tL e^phi/(L-t): -D' = L e^phi + 2t^2 e^phi/(L-t)^2, so int_ell^oo L e^phi <= D(ell) for ell > t")
    # (v)+(vi) assemble: C [ell e^{phi(ell)} + D(ell)] / ((1-e^{-ell}) sqrt(4 pi t)), C = pi e^{3 delta}/A
    Cc = sp.pi * sp.exp(3 * delta) / A
    assembled = Cc * (l * sp.exp(phi.subs(L, l)) + D.subs(L, l)) / ((1 - sp.exp(-l)) * sp.sqrt(4 * sp.pi * t))
    stated = sp.pi * sp.exp(3 * delta) / (A * (1 - sp.exp(-l))) * l * sp.exp(l / 2) * (1 + 2 * t / (l - t)) \
        * sp.exp(-l ** 2 / (4 * t)) / sp.sqrt(4 * sp.pi * t)
    assert sp.simplify(assembled - stated) == 0
    out.append("[exact] assembled bound == the right-hand side of Theorem 3.4(b), identically")
    # weight bound 1/(2 sinh(L/2)) = e^{-L/2}/(1-e^{-L}) <= e^{-L/2}/(1-e^{-ell}) for L >= ell
    assert sp.simplify((1 / (2 * sp.sinh(L / 2))).rewrite(sp.exp) - sp.exp(-L / 2) / (1 - sp.exp(-L))) == 0
    out.append("[exact] 1/(2 sinh(L/2)) = e^{-L/2}/(1-e^{-L})")

    # (vii) extremal counting function N(L) = C e^L on [ell, oo): exact value of sum f dN vs the bound,
    # at rational sample points including the boundary t = ell^2/(2(1+ell)) and small systoles.
    I_closed = sp.integrate(L * sp.exp(phi), (L, l, sp.oo))
    mp.mp.dps = 40
    rows = []
    for lv in [sp.Rational(1, 100), sp.Rational(1, 10), sp.Rational(1, 2), 1, 2, 5]:
        lv = sp.Rational(lv)
        tb = lv ** 2 / (2 * (1 + lv))
        for tv in [tb, tb / 2, tb / 10]:
            Iv = I_closed.subs({l: lv, t: tv})
            # exact inequality: I(ell) <= D(ell), certified by (iv); evaluate the ratio for the record
            ratio_extremal = (lv + sp.exp(-phi.subs({L: lv, t: tv})) * Iv) / (lv + 2 * tv * lv / (lv - tv))
            rv = mp.mpf(sp.N(ratio_extremal, 40))
            assert rv <= 1, (lv, tv, rv)
            rows.append("        ell=%-5s t=%-14s extremal/bound = %s" % (lv, tv, mp.nstr(rv, 12)))
    out.append("[exact identity + sanity value] extremal counting measure N=Ce^L: (sum f dN)/(bound) <= 1 at:")
    out.extend(rows)


def thm34c():
    a = sp.Symbol('a', positive=True)  # a = L^2 - ell^2 >= 0
    term = lambda tt, LL: sp.exp(-tt / 4) * sp.exp(-LL ** 2 / (4 * tt)) / sp.sqrt(4 * sp.pi * tt)
    ratio = term(t, L) / term(t1, L)
    pref = sp.sqrt(t1 / t) * sp.exp((t1 - t) / 4) * sp.exp(l ** 2 / (4 * t1)) * sp.exp(-l ** 2 / (4 * t))
    q = sp.simplify(sp.powsimp(ratio / pref, force=True))
    expected = sp.exp(-(L ** 2 - l ** 2) * (1 / (4 * t) - 1 / (4 * t1)))
    assert sp.simplify(sp.powsimp(q / expected, force=True)) == 1
    out.append("[exact] Thm 3.4(c): term(t)/term(t1) = sqrt(t1/t) e^{(t1-t)/4} e^{ell^2/4t1} e^{-ell^2/4t} * e^{-(L^2-ell^2)(1/4t-1/4t1)}, last factor <= 1 for L>=ell, t<=t1")


def lo10_thm35():
    w = sp.Symbol('w', positive=True)
    main = w / (2 * sp.sinh(l / 2)) * sp.exp(-t / 4) * sp.exp(-l ** 2 / (4 * t)) / sp.sqrt(4 * sp.pi * t)
    lim = sp.limit(sp.sqrt(t) * sp.exp(l ** 2 / (4 * t)) * main, t, 0, '+')
    assert sp.simplify(lim - w / (2 * sp.sinh(l / 2) * sp.sqrt(4 * sp.pi))) == 0
    assert sp.limit(sp.exp(l ** 2 / (4 * t)) * main, t, 0, '+') == sp.oo
    out.append("[exact] LO.10: sqrt(t) e^{ell^2/4t} (main term) -> w/(2 sinh(ell/2) sqrt(4pi)); without sqrt(t) it -> oo, so no constant C works when L* = ell")
    # if L* > ell: t^{-1/2} e^{-(L*^2-ell^2)/4t} is bounded on (0,oo): max at t = (L*^2-ell^2)/2
    a = sp.Symbol('a', positive=True)
    g = t ** sp.Rational(-1, 2) * sp.exp(-a / (4 * t))
    crit = sp.solve(sp.diff(g, t), t)
    assert crit == [a / 2]
    out.append("[exact] if L* > ell: sup_t t^{-1/2} e^{-a/4t} = (a/2)^{-1/2} e^{-1/2}, a = L*^2-ell^2, finite -> constant-C bound holds")
    # Theorem 3.5 toy model (exact): two weight functions agreeing below L*, ell1 = ell2 or not
    for (w1, w2, Lstar) in [({1: 3, 2: 5}, {1: 3, 2: 4}, 2),      # same systole, differ at L=2
                            ({1: 2, 3: 1}, {sp.Rational(3, 2): 7}, 1),  # ell1 != ell2
                            ({1: 2}, {1: 1, sp.Rational(11, 10): 50}, 1)]:  # ell1 = ell2, multiplicities differ
        keys = sorted(set(w1) | set(w2), key=lambda v: sp.Rational(v))
        cL = {Lv: w1.get(Lv, 0) - w2.get(Lv, 0) for Lv in keys}
        assert min(Lv for Lv in keys if cL[Lv] != 0) == Lstar
        # (Z1-Z2)/leading = sum_L (c_L/c_{L*}) (sinh(L*/2)/sinh(L/2)) e^{-(L^2-L*^2)/4t}  (e^{-t/4}/sqrt(4 pi t) cancels)
        ratio_terms = [sp.Rational(cL[Lv], cL[Lstar]) * sp.sinh(sp.Rational(Lstar) / 2) / sp.sinh(sp.Rational(Lv) / 2)
                       * sp.exp(-(sp.Rational(Lv) ** 2 - sp.Rational(Lstar) ** 2) / (4 * t)) for Lv in keys if cL[Lv] != 0]
        lim = sum(sp.limit(term, t, 0, '+') for term in ratio_terms)
        assert lim == 1, lim
    out.append("[exact] Thm 3.5 toy models (incl. ell1=ell2 with different multiplicity, and a large later weight 50 at L=11/10): (Z1-Z2)/leading -> 1")


def main():
    lemma33()
    thm34b()
    thm34c()
    lo10_thm35()
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
