"""check_probes: exact probes of the Prop. 6.10 bounds and of the recovery conclusion.

For each multiset and radius vector, every probe dH (exact rationals, |dH_nu| <= radius_nu) is pushed through the
exact recovery map and we assert, componentwise:
  |dI| <= Delta,  |dT| <= tau,  |dT - sech^2U * dU| <= tau_rem,  |r| <= rho,  |r_rem| <= rho_rem (r_rem = r + J dI),
  |dM| <= Delta_M,  |e~ - e| <= E,  |e~ - e - G dH| <= |M^-1| rho_rem + A E,
and (whenever the certificate passes at that radius) that rounding the real parts of the roots of q~ returns m,
decided exactly by Routh-Hurwitz strip counts on the shifted polynomial.
Probe families: all 2^n corners (+-delta), random interior points, random face points (some coordinates at
+-delta), gradient directions dH = +-delta * G_j / max|G_j| and +-delta * sign(G_j), linear root-push corners
dH_c = +-delta sign(p_c(a +- 1/2)).
Radii: absolute model at printed delta_cert and at printed delta_thm; uniform relative at printed eps_cert;
absolute at delta_cert*(1+1/1000) (bounds only, certificate fails there, recovery still checked and reported);
extra cluster multisets at their own 4-s.f. certified delta.
"""
import sys, random, itertools, time
from fractions import Fraction as Fr
from stab610 import *
from rows_table import TABLE, max_sig, passes

random.seed(20261006)
fails = 0
nprobe = 0


def check(cond, msg):
    global fails
    if not cond:
        fails += 1
        print("   FAIL:", msg)
    return cond


def le_vec(a, b):
    return all(abs(x) <= y for x, y in zip(a, b))


def probe(st, B, dH, want_recovery):
    global nprobe
    nprobe += 1
    n, N, S = st.n, st.N, st.S
    dI = mat_vec(st.Finv, dH)
    It = [x + y for x, y in zip(st.I, dI)]
    ok = le_vec(dI, B['Delta'])
    Tt = T_series(It)
    dT = [x - y for x, y in zip(Tt, st.T)]
    dU = [Fr(0)] * N
    for k in range(1, n):
        dU[2 * k - 1] = dI[k] / (2 * k - 1)
    lin = S.mul(st.s, dU)
    odd = [k for k in range(1, N, 2)]
    ok &= all(abs(dT[k]) <= B['tau'][k] for k in odd)
    ok &= all(abs(dT[k] - lin[k]) <= B['tau_rem'][k] for k in odd)
    Mt, bt = M_b(It, Tt)
    e = st.e
    r = [bt[j] - sum(Mt[j][c] * e[c + 1] for c in range(n)) for j in range(n)]
    ok &= le_vec(r, B['rho'])
    rlin = [-x for x in mat_vec(st.J, dI)]
    rrem = [x - y for x, y in zip(r, rlin)]
    ok &= le_vec(rrem, B['rho_rem'])
    ok &= all(abs(Mt[i][j] - st.M[i][j]) <= B['DM'][i][j] for i in range(n) for j in range(n))
    Mti = mat_inv(Mt)
    if Mti is None:
        check(False, f"M~ singular at {st.m} {dH}")
        return False, None
    et = [Fr(1)] + mat_vec(Mti, bt)
    d = [x - y for x, y in zip(et[1:], e[1:])]
    ok &= le_vec(d, B['E'])
    vr = [x - y for x, y in zip(d, mat_vec(st.G, dH))]
    ok &= le_vec(vr, B['varrho'])
    check(ok, f"a Prop. 6.10 bound is violated at m={st.m}, dH={[str(x) for x in dH]}")
    rec = recovers(et, st.m)
    if want_recovery:
        check(rec, f"recovery FAILS inside certified radius: m={st.m}, dH={[str(x) for x in dH]}")
    ratio = max((abs(x) / y for x, y in zip(d, B['E']) if y), default=Fr(0))
    return rec, ratio


def families(st, rad, nrand):
    n = st.n
    out = []
    for s in itertools.product((-1, 1), repeat=n):
        out.append([si * x for si, x in zip(s, rad)])
    for j in range(n):
        g = st.G[j]
        mx = max(abs(x) for x in g)
        for sg in (1, -1):
            out.append([sg * rad[c] * g[c] / mx for c in range(n)])
            out.append([sg * rad[c] * (1 if g[c] >= 0 else -1) for c in range(n)])
    for a in st.orders:
        for z0 in (Fr(a) - Fr(1, 2), Fr(a) + Fr(1, 2)):
            pc = [sum((-1) ** j * st.G[j - 1][c] * z0 ** (n - j) for j in range(1, n + 1)) for c in range(n)]
            for sg in (1, -1):
                out.append([sg * rad[c] * (1 if pc[c] >= 0 else -1) for c in range(n)])
    D = 997
    for _ in range(nrand):
        out.append([rad[c] * Fr(random.randint(-D, D), D) for c in range(n)])
    for _ in range(nrand // 2):
        v = [rad[c] * Fr(random.randint(-D, D), D) for c in range(n)]
        for c in random.sample(range(n), random.randint(1, n)):
            v[c] = random.choice((-1, 1)) * rad[c]
        out.append(v)
    return out


def run(st, rad, nrand, label, expect_cert=True):
    B = st.bounds(rad)
    cert = st.certify(rad)
    if expect_cert:
        check(cert['spec'] and cert['mixed'], f"{label}: certificate does not pass")
    if not B['ok_spec']:
        print(f"  {label}: rho(A)<1 not certified; skipped")
        return
    t = time.time()
    fam = families(st, rad, nrand)
    nrec = 0
    worst = Fr(0)
    for dH in fam:
        rec, ratio = probe(st, B, dH, want_recovery=cert['mixed'])
        nrec += rec
        worst = max(worst, ratio or 0)
    print(f"  {label}: {len(fam)} probes, certificate={cert['mixed']}, recovered {nrec}/{len(fam)},"
          f" all bounds held; max |e~-e|_j/E_j = {float(worst):.3f}  ({time.time() - t:.1f}s)")


print("Probes of the 11 printed rows")
for m, dthm_s, dcert_s, dup_s, ratio_s, built, rel_s, eps_s in TABLE:
    st = Setup(m)
    n = st.n
    print(f"=== {m}")
    dc = parse_sci(dcert_s)
    run(st, [dc] * n, 900, f"abs delta_cert={dcert_s}")
    run(st, [parse_sci(dthm_s)] * n, 60, f"abs delta_thm={dthm_s}")
    run(st, [parse_sci(eps_s) * abs(h) for h in st.H], 200, f"rel eps_cert={eps_s}")
    run(st, [dc * Fr(1001, 1000)] * n, 100, "abs delta_cert*(1+1e-3) [beyond certificate]", expect_cert=False)

print()
print("Extra adversarial multisets (clusters, n = 3, 4, 5) at their own 4-s.f. certified delta")
EXTRA = [(2, 2, 2, 2, 2), (3, 3, 3, 3), (2, 3, 3, 3, 3), (6, 6, 6, 6, 6), (2, 2, 3, 3, 3), (3, 3, 3), (2, 7, 7),
         (2, 2, 2, 2, 7), (5, 6, 7, 8, 9)]
for m in EXTRA:
    st = Setup(m)
    q, e = max_sig(st.certify_abs, 4, 'mixed')
    d = from_sig(q, e)
    r = st.certify_abs(d)
    w = 'ii' if r['ii'] else ('i' if r['i'] else 'mixed')
    print(f"=== {m}: certified delta (4 s.f.) = {fmt(q, e, 4)} by test {w}")
    run(st, [d] * st.n, 300, f"abs delta={fmt(q, e, 4)}")

print("TOTAL PROBES:", nprobe, " TOTAL FAILURES:", fails)
sys.exit(1 if fails else 0)
