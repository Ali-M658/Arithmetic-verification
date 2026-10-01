"""Symbolic checks for DI.1-DI.4, DI.8, DI.9 (algebraic parts).

Run from the repository root:
    /opt/homebrew/Caskroom/miniforge/base/bin/python3 review/audit/diophantine/check_algebra.py
Writes review/audit/diophantine/check_algebra.txt; exits nonzero on any failure.
"""
import os
import sys
from sympy import (symbols, expand, factor, Poly, rem, simplify, discriminant, Rational,
                   integrate, log as slog, oo, cancel, together, degree, gcd as sgcd, pi, N, sqrt, Symbol)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from dio_common import check, finish, Fail  # noqa: E402

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "check_algebra.txt")
log = []
lam, x, y, z, s, W, t, w = symbols("lambda x y z s W t w")
a, b, c = symbols("a b c", positive=True)

try:
    e1 = x + y + z
    e2 = x * y + y * z + z * x
    e3 = x * y * z
    Fc = e1 * e2 - lam * e3

    # ---- DI.2 pencil ------------------------------------------------------------
    check(expand((x + y) * (y + z) * (z + x) - (e1 * e2 - e3)) == 0,
          "pencil identity (x+y)(y+z)(z+x) = e1 e2 - e3", log)
    check(expand(((x + y) * (y + z) * (z + x) + (1 - lam) * e3) - Fc) == 0,
          "C_lambda is the member t = 1 - lambda of (X+Y)(Y+Z)(Z+X) + t XYZ = 0", log)

    # ---- DI.2 own Weierstrass model ----------------------------------------------
    # chart z = 1, quadratic in x: A x^2 + B x + C = 0
    A = y + 1
    B = y ** 2 + (3 - lam) * y + 1
    C = y * (y + 1)
    F1 = Fc.subs(z, 1)
    check(expand(F1 - (A * x ** 2 + B * x + C)) == 0, "chart z=1: F = (y+1)x^2 + (y^2+(3-lam)y+1)x + y(y+1)", log)
    Q = expand(B ** 2 - 4 * A * C)
    qa, qb, qc, qd = [Poly(Q, y).all_coeffs()[i] for i in (1, 2, 3, 4)]
    check(Poly(Q, y).all_coeffs()[0] == 1 and qd == 1, "discriminant quartic v^2=Q(y) is monic with Q(0)=1", log)
    log.append("     Q(y) = " + str(Poly(Q, y).as_expr()))
    # classical quartic -> cubic: v = y^2 + (qa/2) y + t, then disc in y is a cubic in t
    cub = expand(-8 * t ** 3 + 4 * qb * t ** 2 + (8 * qd - 2 * qa * qc) * t + qc ** 2 - 4 * (qb - qa ** 2 / 4) * qd)
    # X = -2t, then shift s = X + 2 (rational 2-torsion at X = -2)
    cubX = expand(cub.subs(t, -(s - 2) / 2))
    target = s * (s ** 2 + (lam ** 2 - 6 * lam - 3) * s + 16 * lam)
    check(expand(cubX - target) == 0, "own model E_lam: W^2 = s(s^2 + (lam^2-6lam-3)s + 16 lam)", log)

    # explicit forward map and check it lands on E_lam modulo the curve equation
    vv = 2 * A * x + B
    tt = vv - y ** 2 - (qa / 2) * y
    s_map = -2 * tt + 2
    W_map = 2 * ((qb - qa ** 2 / 4) - 2 * tt) * y + (qc - qa * tt)
    d1 = expand(W_map ** 2 - target.subs(s, s_map))
    check(rem(Poly(d1, x), Poly(F1, x)).as_expr() == 0 or simplify(rem(Poly(d1, x), Poly(F1, x)).as_expr()) == 0,
          "forward map (x:y:1) -> (s,W) lands on E_lam", log)
    check(expand(s_map + 4 * (x * y + x + y)) == 0, "forward map has s = -4 e2 / z^2 (z=1)", log)
    log.append("     W = " + str(factor(W_map)))

    # inverse map (s,W) -> (x:y:1)
    t_inv = (2 - s) / 2
    y_inv = (W - (qc - qa * t_inv)) / (2 * ((qb - qa ** 2 / 4) - 2 * t_inv))
    v_inv = y_inv ** 2 + (qa / 2) * y_inv + t_inv
    x_inv = (v_inv - B.subs(y, y_inv)) / (2 * A.subs(y, y_inv))
    # check: F(x_inv, y_inv, 1) vanishes on E_lam
    num = together(F1.subs({x: x_inv, y: y_inv})).as_numer_denom()[0]
    num = expand(num)
    Wsq = target
    r_ = rem(Poly(num, W), Poly(W ** 2 - Wsq, W)).as_expr()
    check(simplify(r_) == 0, "inverse map (s,W) -> (x:y:1) lands on C_lam", log)
    # composition forward(inverse) = identity on E_lam
    comp_s = cancel(s_map.subs({x: x_inv, y: y_inv}))
    nn = expand(together(comp_s - s).as_numer_denom()[0])
    check(simplify(rem(Poly(nn, W), Poly(W ** 2 - Wsq, W)).as_expr()) == 0, "s(forward(inverse(s,W))) = s", log)
    comp_W = cancel(W_map.subs({x: x_inv, y: y_inv}))
    nn = expand(together(comp_W - W).as_numer_denom()[0])
    check(simplify(rem(Poly(nn, W), Poly(W ** 2 - Wsq, W)).as_expr()) == 0, "W(forward(inverse(s,W))) = W", log)
    # base point: s = -4 e2/z^2 -> infinity only at z=0 points with e2 != 0; on z=0 the curve
    # meets (1:0:0),(0:1:0),(1:-1:0); e2 = xy there, nonzero only at (1:-1:0)
    zline = factor(Fc.subs(z, 0))
    check(zline == factor(x * y * (x + y)), "C meets z=0 in (1:0:0),(0:1:0),(1:-1:0)", log)
    log.append("     O_E (point at infinity) <-> (1:-1:0) since e2(1,-1,0) = -1 != 0 (the other two have e2=0)")

    # ---- discriminant, fibre types ----------------------------------------------
    A2 = lam ** 2 - 6 * lam - 3
    A4 = 16 * lam
    Delta = 16 * A4 ** 2 * (A2 ** 2 - 4 * A4)   # disc of x(x^2+A2 x+A4) is A4^2 (A2^2-4A4); Delta = 16*that
    check(factor(Delta - 2 ** 12 * lam ** 2 * (lam - 9) * (lam - 1) ** 3) == 0,
          "Delta(E_lam) = 2^12 lam^2 (lam-9)(lam-1)^3", log)
    c4 = 16 * (A2 ** 2 - 3 * A4)
    c6 = -32 * A2 * (2 * A2 ** 2 - 9 * A4)
    check(expand(c4 ** 3 - c6 ** 2 - 1728 * Delta) == 0, "c4^3 - c6^2 = 1728 Delta", log)
    for val, mult, name in [(0, 2, "I2"), (1, 3, "I3"), (9, 1, "I1")]:
        ordD = 0
        D_ = Poly(Delta, lam)
        while D_.eval(val) == 0:
            D_ = Poly(cancel(D_.as_expr() / (lam - val)), lam)
            ordD += 1
        check(ordD == mult and c4.subs(lam, val) != 0, f"fibre at lam={val}: ord Delta={ordD}, c4 != 0 -> {name}", log)
    dA2, dA4, dD, dc4 = (degree(A2, lam), degree(A4, lam), degree(Delta, lam), degree(c4, lam))
    check(dA2 <= 2 and dA4 <= 4 and dD == 6 and dc4 == 4,
          f"at lam=oo: deg a2={dA2}<=2, deg a4={dA4}<=4 (model regular at oo), ord_oo Delta = 12-{dD} = 6, ord_oo c4 = 4-{dc4} = 0 -> I6", log)
    check(2 + 3 + 1 + 6 == 12, "Euler numbers 2+3+1+6 = 12: rational elliptic surface", log)
    check(8 - ((2 - 1) + (3 - 1) + (1 - 1) + (6 - 1)) == 0, "Shioda-Tate: rank over Qbar(lam) = 8 - (1+2+0+5) = 0", log)

    # compare the manuscript's model y^2 = x^3+(l-3)^2 x^2 + 8(l-3)(l-1)x + 16(l-1)^2
    # use standard formulas with a1=a3=0: b2=4a2, b4=2a4, b6=4a6, b8=4a2a6 - a4^2
    a2m, a4m, a6m = (lam - 3) ** 2, 8 * (lam - 3) * (lam - 1), 16 * (lam - 1) ** 2
    b2m, b4m, b6m, b8m = 4 * a2m, 2 * a4m, 4 * a6m, 4 * a2m * a6m - a4m ** 2
    c4m = b2m ** 2 - 24 * b4m
    c6m = -b2m ** 3 + 36 * b2m * b4m - 216 * b6m
    Dm = -b2m ** 2 * b8m - 8 * b4m ** 3 - 27 * b6m ** 2 + 9 * b2m * b4m * b6m
    check(factor(Dm - Delta) == 0, "manuscript model has the same Delta = 2^12 lam^2 (lam-9)(lam-1)^3", log)
    check(expand(c4m - c4) == 0 and expand(c6m - c6) == 0,
          "manuscript model has identical (c4, c6): isomorphic to E_lam over Q(lam) (not a twist)", log)
    # its 2-torsion: x^3+(l-3)^2x^2+8(l-3)(l-1)x+16(l-1)^2 at x = -4 ?
    pm = x ** 3 + a2m * x ** 2 + a4m * x + a6m
    root = [r for r in [-4, -4 * (lam - 1), -(lam - 1) ** 2, -4 * lam, 4 - 4 * lam] if expand(pm.subs(x, r)) == 0]
    log.append(f"     manuscript model: rational 2-torsion abscissa {root}; it is E_lam translated by s = x + {root[0]*-1 if root else '?'}")

    # ---- DI.3 reciprocation -------------------------------------------------------
    P0, P1, P2 = symbols("p0 p1 p2")
    # line through P=(p0:p1:p2) and T2=(0:0:1): points (p0:p1:w)
    qline = expand(Fc.subs({x: P0, y: P1, z: w}))
    pq = Poly(qline, w)
    check(pq.degree() == 2, "line P T2 meets C in a quadratic in the z-coordinate (T2 at infinity)", log)
    co = pq.all_coeffs()
    check(simplify(co[2] / co[0] - P0 * P1) == 0, "product of the two roots = p0 p1, so third point is (p0:p1:p0p1/p2) = (p0p2:p1p2:p0p1)", log)
    Qp = (P0 * P2, P1 * P2, P0 * P1)
    Rp = (P1 * P2, P0 * P2, P0 * P1)
    # collinear O, Qp, Rp: det = 0
    from sympy import Matrix
    det = Matrix([[1, -1, 0], list(Qp), list(Rp)]).det()
    check(expand(det) == 0, "O=(1:-1:0), (p0p2:p1p2:p0p1), (p1p2:p0p2:p0p1) are collinear", log)
    check(expand(Fc.subs({x: Rp[0], y: Rp[1], z: Rp[2]}) - (P0 * P1 * P2) * Fc.subs({x: P0, y: P1, z: P2})) == 0,
          "F(p1p2,p0p2,p0p1) = p0p1p2 * F(p0,p1,p2): (p1p2:p0p2:p0p1) lies on C_lam whenever P does", log)
    log.append("     => P + T2 = O*(P*T2) = (1/p0 : 1/p1 : 1/p2) = iota(P); iota involution => 2 T2 = O")

    # ---- DI.3 dual family -----------------------------------------------------------
    E1, E2, E3 = a + b + c, a * b + b * c + c * a, a * b * c
    t1 = [E2 * a, E2 * b, E2 * c]
    t2 = [E1 * b * c, E1 * c * a, E1 * a * b]
    S1, S2 = sum(t1), sum(t2)
    R1 = sum(1 / q for q in t1)
    R2 = sum(1 / q for q in t2)
    check(expand(S1 - E1 * E2) == 0 and expand(S2 - E1 * E2) == 0, "dual family: both sums equal e1 e2", log)
    check(simplify(R1 - 1 / E3) == 0 and simplify(R2 - 1 / E3) == 0, "dual family: both reciprocal sums equal 1/e3", log)

    # ---- DI.9 isosceles D_{u,v} -----------------------------------------------------
    uu, vv_ = symbols("u v", positive=True)
    T1 = [(2 * uu + vv_) * uu, (2 * uu + vv_) * vv_, (2 * uu + vv_) * vv_]
    T2_ = [(uu + 2 * vv_) * vv_, (uu + 2 * vv_) * uu, (uu + 2 * vv_) * uu]
    check(expand(sum(T1) - (2 * uu + vv_) * (uu + 2 * vv_)) == 0 and expand(sum(T2_) - sum(T1)) == 0,
          "D_{u,v}: both sums = (2u+v)(u+2v)", log)
    check(simplify(sum(1 / q for q in T1) - 1 / (uu * vv_)) == 0 and simplify(sum(1 / q for q in T2_) - 1 / (uu * vv_)) == 0,
          "D_{u,v}: both reciprocal sums = 1/(uv) (before division by g)", log)
    check(expand(2 * (2 * uu + vv_) - (uu + 2 * vv_) - 3 * uu) == 0 and expand(2 * (uu + 2 * vv_) - (2 * uu + vv_) - 3 * vv_) == 0,
          "g | 2(2u+v)-(u+2v) = 3u and g | 3v, so g | 3 gcd(u,v) = 3", log)
    # isosceles points on C_lam: (r:1:1) with 2r^2 + (5-lam) r + 2 = 0 (roots r, 1/r)
    r = symbols("r")
    iso = factor(Fc.subs({x: r, y: 1, z: 1}))
    check(expand(iso - (2 * r ** 2 + (5 - lam) * r + 2)) == 0,
          "isosceles points (r:1:1) on C_lam: 2r^2+(5-lam)r+2 = 0, roots r and 1/r", log)
    log.append("     => each C_lam carries at most one isosceles pair {(u,v,v),(v,u,u)} up to permutation")

    # ---- DI.9 area ---------------------------------------------------------------------
    sv = symbols("sv", positive=True)
    area_half = integrate(Rational(1, 2) / ((2 + sv) * (1 + 2 * sv)), (sv, 1, oo))
    check(simplify(area_half - slog(2) / 6) == 0,
          "area{0<u<v, (2u+v)(u+2v) <= 1} = (1/2) int_1^oo ds/((2+s)(1+2s)) = log2/6 (whole quadrant: log2/3)", log)
    # density: coprime pairs 6/pi^2; g=3 on the classes u=v!=0 mod 3: 2 of the 8 admissible
    # residue pairs mod 3; region for g=3 is scaled by 3 in Y
    c_iso = Rational(6) / pi ** 2 * (slog(2) / 6) * (Rational(6, 8) * 1 + Rational(2, 8) * 3)
    check(simplify(c_iso - 3 * slog(2) / (2 * pi ** 2)) == 0, f"c_iso = (6/pi^2)(log2/6)(3/4 + 3/4) = 3 log2/(2 pi^2) = {N(c_iso, 8)}", log)

    # ---- DI.4 Prop 2: the (2 vs 1) case inside one proportionality class ---------------
    c1_, c2_ = symbols("c1 c2", positive=True)
    dd = c1_ + c2_
    check(factor(together(1 / c1_ + 1 / c2_ - 1 / dd)).as_numer_denom()[0] == factor(c1_ ** 2 + c1_ * c2_ + c2_ ** 2),
          "Prop 2: c1+c2=d and 1/c1+1/c2=1/d force c1^2+c1c2+c2^2 = 0, impossible for c_i > 0", log)

    # ---- DI.8 ---------------------------------------------------------------------------
    log.append("     DI.8: G = gcd(e2 a, e2 b, e2 c, e1 bc, e1 ca, e1 ab) divides e2*gcd(a,b,c) = e2 (t primitive); "
               "any positive integer triple has R <= 3 anyway")

    # ---- the manuscript's stated maps to BGN's model (statement DI.2) -----------------
    tau = 4 * lam * (lam - 1) * (x - y) / (x + y - (lam - 1))
    sig = -4 * (x * y + x + y)
    num = expand(together(tau ** 2 - target.subs(s, sig)).as_numer_denom()[0])
    check(simplify(rem(Poly(num, x), Poly(F1, x)).as_expr()) == 0,
          "stated forward map sigma=-4e2/z^2, tau=4l(l-1)(x-y)/(x+y-(l-1)z) lands on BGN (6)", log)
    S_ = s * (lam - 1) / (s - 4 * lam)
    D_ = W * (S_ - lam + 1) / (4 * lam * (lam - 1))
    num = expand(together(F1.subs({x: (S_ + D_) / 2, y: (S_ - D_) / 2}, simultaneous=True)).as_numer_denom()[0])
    check(simplify(rem(Poly(num, W), Poly(W ** 2 - target, W)).as_expr()) == 0,
          "stated inverse map (x+y)/z = s(l-1)/(s-4l), (x-y)/z = tau((x+y)/z-l+1)/(4l(l-1)) lands on C_lam", log)
    num = expand(together(W_map + tau).as_numer_denom()[0])
    check(simplify(rem(Poly(num, x), Poly(F1, x)).as_expr()) == 0,
          "own map and stated map agree up to the sign of the ordinate (W_own = -tau on C_lam)", log)
    log.append("ALL ALGEBRA CHECKS PASSED")
    finish(log, OUT)
except Fail as e:
    finish(log, OUT)
    sys.exit(1)
