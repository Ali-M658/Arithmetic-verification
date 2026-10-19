"""Corollary 6.3 with a certified gap (eigen paper, Corollary 6.3 and the proposition after it).

    python3 theory/eigen/certified_gap.py          (about a minute; needs python-flint)

computed_gap.py evaluates the gap Theta = min_{sigma != sigma'} |G_sigma(t) - G_sigma'(t)| over Sig(A, M) in
floating point on a grid of times.  Here, at one rational time t per class (the time of computed_gap.csv, rounded to
the digits printed there), every quantity in the hypotheses of Corollary 6.3 is enclosed in ball arithmetic (Arb,
through python-flint):

  * G_sigma(t) = (Area/4 pi) I_1(t) + sum_i E_{m_i}(t), with
        I_1(t)  = e^{-t/4}/t - int_0^oo 4 r e^{-t(1/4 + r^2)} / (e^{2 pi r} + 1) dr,
        E_m(t)  = sum_{j=1}^{m-1} (2 m sin(pi j/m))^{-1} int_R e^{-2 theta_j r - t(1/4 + r^2)} / (1 + e^{-2 pi r}) dr,
    theta_j = pi j/m: each integral by Arb's certified integration over a finite interval, whose integrand is
    meromorphic (Arb returns a non-finite value on any ball that meets a pole, as its integration routine
    requires), plus an explicit bound for the two tails, added to the radius;
  * the least pairwise distance of the enclosures of G_sigma(t), sigma in Sig(A, M) (enumerated exactly), as a
    lower bound Theta for the gap, rounded down to a decimal Theta';
  * B_*(t) = 3 C_* eps e^{eps/2} e^{-eps^2/4t} / ((1 - e^{-eps}) sqrt(4 pi t)) with the count constant C_* of Lemma 4.5,
    checked to be at most Theta'/8, and t <= t_2 = eps^2/(2(1 + eps));
  * Lambda = (2/t) log(8 Z^#(t/2)/Theta'), Z^#(s) = A/(4 pi s) + n_*(M^2 - 1)/(12 M) + 1, checked Lambda t >= 1;
    N = 1 + floor(upper bound of e Z^#(1/Lambda)), and delta = a decimal below Theta'/(8 e N t).
Every comparison is decided by the balls (an undecided comparison is a failure).  The script asserts that each
class passes and writes data/certified_gap.csv.
"""
import csv
import os
from fractions import Fraction as Fr

from flint import arb, acb, ctx

from eigen_common import area_over_2pi, signatures

ctx.prec = 200
HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data")
PI = arb.pi()


def A_(x):
    return arb(str(x)) if isinstance(x, str) else arb(x.numerator) / x.denominator if isinstance(x, Fr) else arb(x)


def upper(x):
    return x.mid() + x.rad()


def lower(x):
    return x.mid() - x.rad()


def unit_identity(t):
    """I_1(t) = e^{-t/4}/t - int_0^oo 4 r e^{-t(1/4+r^2)}/(e^{2 pi r}+1) dr, enclosed."""
    R = 40
    f = lambda z, analytic: 4 * z * (-t * (acb(1) / 4 + z * z)).exp() / ((2 * PI * z).exp() + 1)
    core = acb.integral(f, 0, R).real
    # tail: 4 r e^{-t/4 - t r^2}/(e^{2 pi r}+1) <= 4 r e^{-2 pi r}; int_R^oo 4 r e^{-2 pi r} = (4/2pi)(R + 1/2pi) e^{-2 pi R}
    tail = 4 / (2 * PI) * (R + 1 / (2 * PI)) * (-2 * PI * R).exp()
    return (-t / 4).exp() / t - core + arb(0, upper(tail))


def elliptic(m, t):
    """E_m(t), enclosed."""
    tot = arb(0)
    for j in range(1, m):
        th = PI * j / m
        # tails: r >= R2: e^{-2 th r}; r <= -R1: e^{-(2 pi - 2 th) s} (s = -r); both times e^{-t/4} <= 1
        a_pos, a_neg = 2 * th, 2 * PI - 2 * th
        R2 = int(float(upper(80 / a_pos))) + 1
        R1 = int(float(upper(80 / a_neg))) + 1
        f = lambda z, analytic: (-2 * th * z - t * (acb(1) / 4 + z * z)).exp() / (1 + (-2 * PI * z).exp())
        core = acb.integral(f, -R1, R2).real
        tail = (-a_pos * R2).exp() / a_pos + (-a_neg * R1).exp() / a_neg
        tot += (core + arb(0, upper(tail))) / (2 * m * (PI * j / m).sin())
    return tot


def count_constant(A, eps, M):
    """C_* of Lemma 4.5 (eigen_common.count_constant), in ball arithmetic; returns an upper bound."""
    a1, a2 = eps / 2, (1 + 2 / (PI ** 2 * M * M)).acosh()
    assert a1 < a2 or a2 < a1
    d0 = a1 if a1 < a2 else a2
    r0 = d0 / 2
    rho1 = (r0.sinh() * (PI / M).sin()).asinh()
    b1, b2 = (r0.cosh() - 1) / M, rho1.cosh() - 1
    assert b1 < b2 or b2 < b1
    v0 = 2 * PI * (b1 if b1 < b2 else b2)
    return A * M * (10 * r0 + rho1).exp() / (2 * v0 * (rho1.cosh() - 1))


CLASSES = [("pi/2", Fr(1, 2), "1.8626", 8, "0.025643"), ("pi/2", Fr(1, 2), "1.8626", 12, "0.02482"),
           ("4pi/3", Fr(4, 3), "2.633915", 3, "0.08524"), ("4pi/3", Fr(4, 3), "0.693994", 3, "0.0060028"),
           ("4pi/3", Fr(4, 3), "0.693994", 12, "0.0034221"), ("2pi", Fr(2), "0.1", 3, "0.000092402")]


def dec_below(x, digits=3):
    """a decimal string with `digits` significant digits strictly below the lower end of the ball x > 0"""
    lo = float(lower(x))
    from decimal import Decimal, ROUND_FLOOR
    d = Decimal(repr(lo * (1 - 1e-12)))
    q = Decimal(1).scaleb(d.adjusted() - digits + 1)
    v = d.quantize(q, rounding=ROUND_FLOOR)
    assert arb(str(v)) < x
    return str(v)


def main():
    rows = []
    for Atxt, A_over_pi, eps_txt, M, t_txt in CLASSES:
        A = PI * A_(A_over_pi)
        eps, t = arb(eps_txt), arb(t_txt)
        S = signatures(A_over_pi, M)
        I1 = unit_identity(t)
        E = {m: elliptic(m, t) for m in range(2, M + 1)}
        G = [A_(area_over_2pi(*s)) / 2 * I1 + sum((E[m] for m in s[1]), arb(0)) for s in S]
        # least pairwise distance: every difference is decided by the balls, and each |difference| is bounded below
        # by a decimal; Theta' is the least of these decimals
        from decimal import Decimal
        lows = []
        for i in range(len(G)):
            for k in range(i + 1, len(G)):
                d = G[i] - G[k]
                assert d > 0 or d < 0, (Atxt, M, S[i], S[k])
                lows.append(Decimal(dec_below(abs(d), 4)))
        Th = str(min(lows))
        Thp = arb(Th)
        assert Thp <= 8
        t2 = eps ** 2 / (2 * (1 + eps))
        assert t < t2
        C = count_constant(A, eps, M)
        Bstar = 3 * C * eps * (eps / 2).exp() * (-eps ** 2 / (4 * t)).exp() / ((1 - (-eps).exp()) * (4 * PI * t).sqrt())
        assert Bstar < Thp / 8, (Atxt, eps_txt, M)
        nstar = int(A_over_pi) + 4
        Zs = lambda s: A / (4 * PI * s) + arb(nstar * (M * M - 1)) / (12 * M) + 1
        Lam = (2 / t) * (8 * Zs(t / 2) / Thp).log()
        assert Lam * t >= 1
        bound = arb(1).exp() * Zs(1 / Lam)
        N = int(bound.mid().floor().unique_fmpz()) + 1          # N = floor(e Z#(1/Lambda)) + 1, as in Theorem 6.2
        assert arb(N - 1) <= bound and arb(N) > bound, "the floor is decided by the ball"
        delta = Thp / (8 * arb(1).exp() * N * t)
        dl = dec_below(delta)
        print(f"A={Atxt} eps={eps_txt} M={M} t={t_txt}: |Sig| = {len(S)}; certified gap >= {Th}; "
              f"B_* <= {float(upper(Bstar)):.2e}; N = {N}, delta = {dl}", flush=True)
        rows.append([Atxt, eps_txt, M, len(S), t_txt, Th, N, dl])
    with open(os.path.join(DATA, "certified_gap.csv"), "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["A", "eps", "M", "Sig_size", "t", "certified_gap_lower", "N", "delta"])
        w.writerows(rows)
    print("wrote data/certified_gap.csv")


if __name__ == "__main__":
    main()
