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
class passes and writes data/certified_gap.csv, and data/certified_gap_detail.csv with, per class, the pair of
signatures with the least certified gap, a lower bound for that gap, and decimal bounds for B_*(t), Theta'/8 and Lambda t.

Round 10 (referee B-d M1, B5 of the verdict): the certificate is also written in a form that can be checked by hand.
data/certified_gap_enclosures.csv lists, per class, the enclosures of I_1(t) and of E_m(t), 2 <= m <= M (at most twelve
balls per class), with their midpoints, radii, a decimal with ten significant digits and an upper bound for the
distance from that decimal to the exact value (at most one unit of its last digit, asserted).  Since
G_sigma(t) = (s(sigma)/2) I_1(t) + sum_i E_{m_i}(t), s(sigma) = Area/2 pi, these numbers determine every G_sigma(t); the
script asserts that the gap bound Theta' follows from the printed decimals and their error bounds alone, in exact
rational arithmetic.  data/certified_gap_omissions.csv gives, per class, an upper bound for
Lambda_o = t^{-1} log(8/Theta') of the remark on omissions (one wrong entry above Lambda_o is tolerated).
The integrations use acb.integral with its default tolerances (relative and absolute 2^-200 at 200 bits) and default
work limits; the limits only abort a computation, and every returned ball is an enclosure.  t enters as the ball
arb(t_txt) of the exact decimal rational t_txt.
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


def dec_up(x, digits=3):
    """a decimal string with `digits` significant digits strictly above the upper end of the ball x > 0"""
    from decimal import Decimal, ROUND_CEILING
    hi = float(upper(x))
    d = Decimal(repr(hi * (1 + 1e-12)))
    q = Decimal(1).scaleb(d.adjusted() - digits + 1)
    v = d.quantize(q, rounding=ROUND_CEILING)
    assert arb(str(v)) > x
    return str(v)


def dec_sig(x, digits=10):
    """(decimal string with `digits` significant digits nearest the midpoint of the ball x, an upper bound for its
    distance to every point of x); asserts that this distance is at most one unit of the last printed digit"""
    from decimal import Decimal, ROUND_HALF_EVEN
    d = Decimal(x.mid().str(40, radius=False))
    q = Decimal(1).scaleb(d.adjusted() - digits + 1)
    v = d.quantize(q, rounding=ROUND_HALF_EVEN)
    err = abs(arb(str(v)) - x)
    ulp = arb(str(q))
    assert upper(err) < ulp, (str(v), x)
    return str(v), str(q)


def main():
    rows, detail, encl, omis = [], [], [], []
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
                lows.append((Decimal(dec_below(abs(d), 4)), i, k, abs(d)))
        Th = str(min(x[0] for x in lows))
        _, i0, k0, d0 = min(lows, key=lambda x: lower(x[3]))     # the pair with the least certified lower end
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
        sig = lambda s: "(%d;%s)" % (s[0], ",".join(map(str, s[1])))
        detail.append([Atxt, eps_txt, M, sig(S[i0]), sig(S[k0]), dec_below(d0, 7), dec_up(Bstar), dec_below(Thp / 8, 4),
                       dec_below(Lam * t, 3)])
        # round 10: the enclosures of I_1(t), E_m(t) as printed decimals with error bounds, and a check, in exact
        # rational arithmetic, that the printed decimals alone give every pairwise gap >= Theta'
        pr = {}
        for name, m, x in [("I1", "", I1)] + [("E", m, E[m]) for m in range(2, M + 1)]:
            v, ulp = dec_sig(x)
            pr[(name, m)] = (Fr(v), Fr(ulp))
            encl.append([Atxt, eps_txt, M, t_txt, name, m, x.mid().str(25, radius=False), dec_up(x.rad(), 2), v, ulp])
        Gp = []
        for s in S:
            half = area_over_2pi(*s) / 2
            val = half * pr[("I1", "")][0] + sum((pr[("E", m)][0] for m in s[1]), Fr(0))
            err = half * pr[("I1", "")][1] + sum((pr[("E", m)][1] for m in s[1]), Fr(0))
            Gp.append((val, err))
        Thf = Fr(Th)
        for i in range(len(Gp)):
            for k in range(i + 1, len(Gp)):
                assert abs(Gp[i][0] - Gp[k][0]) - Gp[i][1] - Gp[k][1] >= Thf, ("printed enclosures", Atxt, M, S[i], S[k])
        # Lambda_o = t^{-1} log(8/Theta') (remark on omissions, with t and Theta' in place of t_*, Theta_*)
        omis.append([Atxt, eps_txt, M, t_txt, Th, dec_up((8 / Thp).log() / t, 3)])
    with open(os.path.join(DATA, "certified_gap.csv"), "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["A", "eps", "M", "Sig_size", "t", "certified_gap_lower", "N", "delta"])
        w.writerows(rows)
    with open(os.path.join(DATA, "certified_gap_detail.csv"), "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["A", "eps", "M", "sigma", "sigma_prime", "least_gap_lower", "Bstar_upper", "Theta_over_8_lower",
                    "Lambda_t_lower"])
        w.writerows(detail)
    with open(os.path.join(DATA, "certified_gap_enclosures.csv"), "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["A", "eps", "M", "t", "quantity", "m", "midpoint", "radius_upper", "printed", "error_less_than"])
        w.writerows(encl)
    with open(os.path.join(DATA, "certified_gap_omissions.csv"), "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(["A", "eps", "M", "t", "certified_gap_lower", "Lambda_o_upper"])
        w.writerows(omis)
    print("wrote data/certified_gap.csv, data/certified_gap_detail.csv, data/certified_gap_enclosures.csv and "
          "data/certified_gap_omissions.csv")


if __name__ == "__main__":
    main()
