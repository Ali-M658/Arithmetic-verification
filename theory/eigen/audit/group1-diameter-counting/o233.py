"""Checks of Proposition eig:233 (the family O(2,3,m)).

1. sigma_0: closed-form value (mpmath, 30 digits), and exact simplification cosh(2 s_inf) = 5/3.
2. Area, s_m increasing to s_inf, h_m >= log(m/(2 pi)), for m = 7..10^5 (sampled) exactly/mpmath.
3. Systole hunt: in SL(2,R), x = rotation by 2pi/m about P_m, a = half-turn about P_2 (so
   b = a x has order 3).  Traces of all cyclic words a x^k1 ... a x^kj, j <= 3 (j <= 4 for m <= 24),
   for m = 7..150, plus BFS over the reflection group for m <= 20.  Every hyperbolic length found
   must be >= sigma_0; we record the minimum per m.
4. Geometry used in the Jorgensen argument: for m = 7..20 and every enumerated hyperbolic element
   whose axis passes within distance 1 of P_2, the axis passes within s_m (hence within 2 s_m) of
   an enumerated order-3 point; and Jorgensen's quantity with the order-3 rotation is >= 1.
5. The ball of radius h_m about P_m: no other elliptic point of the enumeration is closer to P_m
   than h_m (order-2 points at exactly h_m), consistent with the embedded cone claim.
"""
import math
import numpy as np
import mpmath as mp
from group_enum import triangle, enumerate_group, mink

mp.mp.dps = 30


def check(c, msg):
    if not c:
        raise AssertionError(msg)


# 1. sigma_0
s_inf = mp.acosh(2 / mp.sqrt(3))
check(abs(mp.cosh(2 * s_inf) - mp.mpf(5) / 3) < mp.mpf(10) ** -25, "cosh 2 s_inf = 5/3")
sigma0 = 2 * mp.asinh(1 / (2 * mp.sqrt(1 + mp.mpf(3) / 4 * mp.cosh(2 * s_inf) ** 2)))
check(abs(sigma0 - 2 * mp.asinh(1 / (2 * mp.sqrt(mp.mpf(37) / 12)))) < mp.mpf(10) ** -25, "37/12")
check(str(sigma0).startswith("0.56206"), "sigma0 value %s" % sigma0)
# the bound obtained with r <= s_inf instead of 2 s_inf (the polygon argument gives r <= s_m)
sigma_better = 2 * mp.asinh(1 / (2 * mp.sqrt(1 + mp.mpf(3) / 4 * mp.cosh(s_inf) ** 2)))
print("sigma_0 = %s ; with r <= s_inf one gets %s" % (mp.nstr(sigma0, 12), mp.nstr(sigma_better, 12)))

# 2. elementary facts
prev = mp.mpf(0)
for m in list(range(7, 2000)) + [10 ** 4, 10 ** 5]:
    s_m = mp.acosh(2 * mp.cos(mp.pi / m) / mp.sqrt(3))
    h_m = mp.acosh(1 / (2 * mp.sin(mp.pi / m)))
    check(s_m > prev and s_m < s_inf, "s_m increasing below s_inf")
    prev = s_m
    check(h_m >= mp.log(m / (2 * mp.pi)), "h_m >= log(m/2pi)")
    # law of cosines in the (pi/2, pi/3, pi/m) triangle
    c23 = mp.cos(mp.pi / m) / mp.sin(mp.pi / 3)
    c2m = (mp.cos(mp.pi / 3)) / (mp.sin(mp.pi / m))
    c3m = (mp.cos(mp.pi / 2) + mp.cos(mp.pi / 3) * mp.cos(mp.pi / m)) / (mp.sin(mp.pi / 3) * mp.sin(mp.pi / m))
    check(abs(c23 - mp.cosh(s_m)) < mp.mpf(10) ** -20, "d(P2,P3) = s_m")
    check(abs(c2m - mp.cosh(h_m)) < mp.mpf(10) ** -20, "d(P2,Pm) = h_m")
    check(c3m > c2m, "P3 farther from Pm than P2")
print("elementary facts OK for m = 7..1999, 1e4, 1e5")


# 3. systole hunt
def rot(z, phi):
    x, y = z.real, z.imag
    s = math.sqrt(y)
    T = np.array([[s, x / s], [0, 1 / s]])
    c, sn = math.cos(phi / 2), math.sin(phi / 2)
    R = np.array([[c, sn], [-sn, c]])
    return T @ R @ np.linalg.inv(T)


def geometry(m):
    # P2 = i, P_m = i e^{h_m} on the imaginary axis (distance h_m)
    h = math.acosh(1 / (2 * math.sin(math.pi / m)))
    P2 = 1j; Pm = 1j * math.exp(h)
    a = rot(P2, math.pi)
    for sgn in (1, -1):
        x = rot(Pm, sgn * 2 * math.pi / m)
        b = a @ x
        if abs(abs(np.trace(b)) - 1.0) < 1e-9:     # order 3: |tr| = 2 cos(pi/3)
            return a, x
    raise AssertionError("no consistent orientation")


min_len = {}
s0 = float(sigma0)
for m in range(7, 151):
    a, x = geometry(m)
    Y = [a @ np.linalg.matrix_power(x, k) for k in range(1, m)]
    Y = np.array(Y)
    best = math.inf

    def upd(tr):
        global best
        t = np.abs(tr)
        t = t[t > 2 + 1e-9]
        if t.size:
            best = min(best, float(2 * np.arccosh(t.min() / 2)))
    upd(np.einsum('kaa->k', Y))
    YY = np.einsum('iab,jbc->ijac', Y, Y)
    upd(np.einsum('ijaa->ij', YY).ravel())
    upd(np.einsum('ijab,kba->ijk', YY, Y).ravel())
    if m <= 24:
        upd(np.einsum('ijab,klba->ijkl', YY, YY).ravel())
    check(best >= s0, "systole below sigma_0 at m=%d: %s" % (m, best))
    min_len[m] = best
print("systole hunt OK (m=7..150): min found length per m >= sigma_0; smallest = %.6f at m=%d"
      % (min(min_len.values()), min(min_len, key=min_len.get)))
print("  sample:", {m: round(min_len[m], 4) for m in (7, 8, 9, 10, 12, 20, 50, 100, 150)})

# BFS cross-check, axis-tree claim, Jorgensen, cone ball
for m in range(7, 21):
    normals, verts = triangle(2, 3, m)
    G = enumerate_group(normals, 30000, 80.0)
    (P2, _), (P3, _), (Pm, _) = verts
    s_m = math.acosh(2 * math.cos(math.pi / m) / math.sqrt(3))
    h_m = math.acosh(1 / (2 * math.sin(math.pi / m)))
    P3s = np.array([g @ P3 for g in G])
    P2s = np.array([g @ P2 for g in G])
    Pms = np.array([g @ Pm for g in G])
    bfs_min = math.inf; nax = 0
    for g in G:
        t = np.trace(g)
        if t <= 3 + 1e-9:
            continue
        L = math.acosh((t - 1) / 2)
        bfs_min = min(bfs_min, L)
        w, V = np.linalg.eig(g)
        i = int(np.argmin(np.abs(w - 1)))
        n = np.real(V[:, i]); n = n / math.sqrt(mink(n, n))
        if abs(mink(P2, n)) > math.sinh(1.0):
            continue
        sh = np.abs(P3s[:, 0] * n[0] + P3s[:, 1] * n[1] - P3s[:, 2] * n[2])
        r = math.asinh(sh.min())
        check(r <= s_m + 1e-9, "axis farther than s_m from order-3 points (m=%d, r=%f)" % (m, r))
        # Jorgensen with A = gamma, B = order-3 rotation at distance r from the axis
        jq = 4 * math.sinh(L / 2) ** 2 * (1 + 0.75 * math.cosh(r) ** 2)
        check(jq >= 1 - 1e-9, "Jorgensen quantity < 1")
        nax += 1
    check(bfs_min >= s0, "BFS systole below sigma_0 at m=%d" % m)
    check(abs(bfs_min - min_len[m]) < 1e-6, "BFS and word systoles differ at m=%d (%f vs %f)"
          % (m, bfs_min, min_len[m]))
    # cone ball: elliptic points other than Pm itself are at distance >= h_m from Pm
    allpts = np.vstack([P2s, P3s, Pms])
    c = -(allpts[:, 0] * Pm[0] + allpts[:, 1] * Pm[1] - allpts[:, 2] * Pm[2])
    c = c[c > 1 + 1e-9]
    check(math.acosh(c.min()) >= h_m - 1e-9, "elliptic point inside the cone ball, m=%d" % m)
    print("m=%2d: BFS |G|=%5d, BFS systole %.5f (words: %.5f), axes checked %d, nearest elliptic to"
          " P_m at %.5f = h_m %.5f" % (m, len(G), bfs_min, min_len[m], nax, math.acosh(c.min()), h_m))
print("o233 OK")
