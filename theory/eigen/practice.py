"""The a-posteriori test of Theorem 7.1 (eigen paper, Section 7) on the committed spectra.

    .venv/bin/python theory/eigen/practice.py          (about 3 min; reads data/instances.csv)

Theorem 7.1.  O of area A, systole >= ell, diameter <= Delta, signature in a finite set S of
signatures of area A; beta = max_{sigma in S} sum_i b_0(m_i); computed lambda~_0 <= ... <= lambda~_N
with |lambda~_j - lambda_j| <= eps_j (j <= N), the lambda_j the first N+1 eigenvalues with
multiplicity.  With
    E_N(t) = H(t) + inf_{0<s<=t} e^{-(lambda~_N - eps_N)(t-s)} (A/(4 pi s) + beta + H(s)) + t sum_{j<N} eps_j,
H the bound of Lemma 2.3 (the first bound B(ell, Delta, s) for s <= ell^2/(2(1+ell)), the all-t bound
otherwise), and Z~_N(t) = sum_{j<N} e^{-lambda~_j t}:
    (C1) exactly one sigma in S has |Z~_N(t) - G_sigma(t)| <= E_N(t)                  => sigma(O) = sigma;
    (C2) sigma has it and E_N(t) < min_{sigma' != sigma} |G_sigma(t) - G_sigma'(t)|/2   => sigma(O) = sigma.
N_test(C) = the least N for which (C) holds at some t; we report the least over t and the t-window.

Method.
  G_sigma(t) = I(t) + sum_i E_{m_i}(t): composite Gauss-Legendre (16 nodes per panel of width 1/2) in
    float64, the identity term in the split form A/(4 pi) [e^{-t/4}/t - 4 int_0^inf r h_t(r)/(e^{2 pi r}+1) dr],
    E_m on [-220, 300]; asserted against 30-digit mpmath quadrature (eigen_common) to 1e-12.
  inf over s: s = t u on 240 log-spaced u in [1e-8, 1]; for every N at once the minimum over the grid
    of mu (s - t) + log(A/(4 pi s) + beta + H(s)), mu = lambda~_N - eps_N, is found exactly as a query on
    the lower convex hull of the points (s, log(...)).  Any s gives an upper bound for the infimum, so
    the grid value is a valid (conservative) E_N.  At each reported count N* the criterion is re-checked
    for N*-1, N*-2, ... with the infimum computed by bounded Brent minimisation in log s (scipy), over the
    refined t-window; the count is lowered while that succeeds.
  t: 400 log-spaced t in [0.002, 1] and 300 in [1e-5, 0.002) (relative steps 1.6% and 1.8%); then 61
    log-spaced points in the bracket of every grid point attaining the minimum.
  Everything is in logarithms where H carries e^{3 Delta}.
Inputs (data/instances.csv, written by instances.py): ell = the systole lower bound (complete
  enumeration, rounded down at 6 decimals); Delta = B1 = 2 diam P (rigorous), B2 (rigorous, sharper),
  the computed true diameter (numerical), or D(A, ell, M) of Theorem 4.4 (class level).
Spectra (complete ranges as stated in METHODS.md):
  triangles: union of numerics/data/eigenvalues_<pqr>_{N,D}.csv, eps_j = err_estimate, complete for
    lambda <= 16000 (a missing eigenvalue below ~1.66e4 would violate the trace test at t = 0.0015);
  family "full": numerics/moduli/data/convergence.csv (all ~5800 computed per member), complete below
    0.8 x the least sector maximum (cross-level counts agree exactly there, double-window solver);
  family "120": numerics/moduli/data/eigenvalue_flow_sectors.csv (first 120 per sector, the spectra of
    the current manuscript), complete below the least sector maximum.
When no N <= N_complete - 1 works, a Weyl estimate is given: lambda~_N replaced by 4 pi N/A, eps_j = 0
  beyond the computed range (the computed eps summed in full), and Z~_N(t) replaced by G_sigma_0(t), so
  that (C2) reads E_N < gap/2 and (C1) reads E_N < gap (gap = distance from G_sigma_0 to the nearest
  other G); minimised over t in [1e-9, 1].
N_obs(t) (current manuscript definition): the least N such that |Z~_N'(t) - G_sigma_0(t)| < gap(t)/2
  for every N' from N to the end of the complete range; N_rule(t): the least N such that the
  nearest-signature rule argmin_sigma |Z~_N'(t) - G_sigma(t)| returns sigma_0 for every such N'.
  Both use the true signature and the data, so neither is a decision rule.  Reported: least over the
  same t-grid, with t.
Theorem 6.2's N for Cl(A, ell, M): eigen_common.theorem_E_constants.

Writes data/practice.csv (counts per example, M, variant, data set), data/practice_t.csv (N(t) per t
for the instance inputs), data/practice_inputs.csv, data/triangle_spectra_first41.csv,
data/table2.csv.  Raises on a failed check, including: a criterion concluding a signature other than
the true one, G against mpmath, the family merge against the committed orbifold lists.
"""
import csv
import math
import os
import sys
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
from scipy.optimize import minimize_scalar

from eigen_common import (check, signatures, area_over_2pi, b_cone, mpq, theorem_E_constants,
                          elliptic_term, diam_bound)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..", "..")
DATA = os.path.join(HERE, "data")
TGRID = np.unique(np.concatenate([np.geomspace(1e-5, 0.002, 300, endpoint=False), np.geomspace(0.002, 1.0, 400)]))
UGRID = np.geomspace(1e-8, 1.0, 240)
LAM_COMPLETE_TRIANGLE = 16000.0
TAUS = ("0.0", "0.4", "0.8", "1.2", "1.6", "2.0", "2.4", "2.8")


# ------------------------------------------------------------------ G_sigma in float64
def gl_nodes(a, b, width, k=16):
    x, w = np.polynomial.legendre.leggauss(k)
    edges = np.arange(a, b + width / 2, width)
    R, W = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        R.append((hi - lo) / 2 * x + (hi + lo) / 2)
        W.append((hi - lo) / 2 * w)
    return np.concatenate(R), np.concatenate(W)


class Gfun:
    """I(t) per unit A/(4 pi) and E_m(t), vectorised over t, cached per t value."""

    def __init__(self, Mmax=12):
        self.r, self.w = gl_nodes(-220.0, 300.0, 0.5)
        self.ri, self.wi = gl_nodes(0.0, 14.0, 0.25)
        thetas = sorted({Fr(j, m) for m in range(2, Mmax + 1) for j in range(1, m)})
        self.thetas = thetas
        self.tpos = {th: i for i, th in enumerate(thetas)}
        r = self.r
        # log of 1/(1 + e^{-2 pi r}), stable for both signs
        lsig = np.where(r > 0, -np.log1p(np.exp(-2 * np.pi * np.abs(r))), 2 * np.pi * r - np.log1p(np.exp(-2 * np.pi * np.abs(r))))
        self.K = np.array([np.exp(-2 * np.pi * float(th) * r + lsig) * self.w for th in thetas])   # (Theta, R)
        self.Ki = 4 * self.ri / (np.exp(2 * np.pi * self.ri) + 1) * self.wi
        self.cache = {}

    def _compute(self, T):
        T = np.asarray(T, float)
        out = {}
        for i0 in range(0, len(T), 64):
            tt = T[i0:i0 + 64]
            gauss = np.exp(-np.outer(tt, 0.25 + self.r ** 2))
            ints = gauss @ self.K.T                                  # (t, Theta)
            gi = np.exp(-np.outer(tt, 0.25 + self.ri ** 2)) @ self.Ki
            unitI = np.exp(-tt / 4) / tt - gi
            for k, t in enumerate(tt):
                E = {}
                for m in range(2, 13):
                    E[m] = sum(ints[k, self.tpos[Fr(j, m)]] / (2 * m * math.sin(math.pi * j / m)) for j in range(1, m))
                out[float(t)] = (unitI[k], E)
        return out

    def prepare(self, T):
        need = [float(t) for t in T if float(t) not in self.cache]
        if need:
            self.cache.update(self._compute(need))

    def G(self, sig, A_over_4pi, t):
        unitI, E = self.cache[float(t)]
        return A_over_4pi * unitI + sum(E[m] for m in sig[1])

    def validate(self):
        T = [1e-5, 1e-3, 0.03, 0.4, 1.0]
        self.prepare(T)
        worst = 0.0
        for t in T:
            with mp.workdps(30):
                tt = mp.mpf(t)
                f = lambda r: r * mp.exp(-tt * (mp.mpf(1) / 4 + r * r)) / (mp.exp(2 * mp.pi * r) + 1)
                Iu = mp.exp(-tt / 4) / tt - 4 * mp.quad(f, [0, 1, 4, 12, mp.inf])
            unitI, E = self.cache[float(t)]
            worst = max(worst, abs(float(Iu) - unitI) / max(1.0, abs(float(Iu))))
            check(abs(float(Iu) - unitI) <= 1e-12 * max(1.0, abs(float(Iu))), f"identity term at t={t}")
            for m in (2, 3, 8, 12):
                Em = float(elliptic_term(m, t))
                worst = max(worst, abs(Em - E[m]))
                check(abs(Em - E[m]) <= 1e-12, f"E_{m}({t}): {Em} vs {E[m]}")
        return worst


# ------------------------------------------------------------------ the bound H of Lemma 2.3 (logs)
def logH(ell, Delta, A, t):
    t = np.asarray(t, float)
    first = (math.log(math.pi * ell * math.exp(ell / 2) / (A * (1 - math.exp(-ell)))) + 3 * Delta
             + np.log1p(2 * t / np.where(ell - t > 0, ell - t, 1.0)) - ell ** 2 / (4 * t) - 0.5 * np.log(4 * math.pi * t))
    allt = math.log(2 * math.sqrt(math.pi) / (A * (1 - math.exp(-ell)))) + 3 * Delta + 17 * t / 4 - 0.5 - ell
    return np.where(t <= ell ** 2 / (2 * (1 + ell)), first, allt)


def lower_hull(x, y):
    """Indices of the lower convex hull of points sorted by x (monotone chain)."""
    x, y = x.tolist(), y.tolist()
    h = []
    for i in range(len(x)):
        while len(h) >= 2:
            a, b = h[-2], h[-1]
            if (y[b] - y[a]) * (x[i] - x[a]) >= (y[i] - y[a]) * (x[b] - x[a]):
                h.pop()
            else:
                break
        h.append(i)
    return np.array(h)


class TailBound:
    """min over the s-grid of mu (s - t) + b(s), b(s) = log(A/(4 pi s) + beta + H(s)), for many mu."""

    def __init__(self, ell, Delta, A, beta, t):
        s = t * UGRID
        lh = logH(ell, Delta, A, s)
        b = np.logaddexp(np.log(A / (4 * math.pi * s) + beta), lh)
        h = lower_hull(s, b)
        self.s, self.b, self.t = s[h], b[h], t
        self.slopes = np.diff(self.b) / np.diff(self.s)
        self.args = (ell, Delta, A, beta)

    def log_tail(self, mu):
        k = np.searchsorted(self.slopes, -np.asarray(mu), side="left")
        return mu * (self.s[k] - self.t) + self.b[k]

    def log_tail_exact(self, mu):
        """inf over 0 < s <= t by bounded Brent in log s, started from the grid optimum."""
        ell, Delta, A, beta = self.args
        t = self.t

        def f(x):
            s = math.exp(x)
            return mu * (s - t) + float(np.logaddexp(math.log(A / (4 * math.pi * s) + beta), logH(ell, Delta, A, s)))
        k = int(np.searchsorted(self.slopes, -mu, side="left"))
        x0 = math.log(self.s[k])
        lo = math.log(self.s[max(k - 1, 0)] if k > 0 else t * 1e-9)
        hi = math.log(self.s[min(k + 1, len(self.s) - 1)])
        if hi <= lo:
            return f(x0)
        res = minimize_scalar(f, bounds=(lo, hi), method="bounded", options=dict(xatol=1e-12))
        return min(res.fun, f(x0))


# ------------------------------------------------------------------ spectra
def triangle_spectrum(pqr):
    name = "-".join(map(str, pqr))
    rows = []
    for bc in ("N", "D"):
        rel = f"numerics/data/eigenvalues_{name}_{bc}.csv"
        for r in csv.DictReader(open(os.path.join(ROOT, rel))):
            rows.append((float(r["lambda"]), float(r["err_estimate"]), float(r["err_conservative"]), bc, int(r["index"]), rel))
    rows.sort(key=lambda x: (x[0], x[3]))
    lam = np.array([x[0] for x in rows])
    check(np.all(np.diff(lam) >= 0), "sorted")
    keep = lam <= LAM_COMPLETE_TRIANGLE
    return dict(lam=lam[keep], eps=np.array([x[1] for x in rows])[keep], epsc=np.array([x[2] for x in rows])[keep],
                lam_complete=LAM_COMPLETE_TRIANGLE, rows=rows, n_total=len(rows), lam_top=float(lam[-1]),
                basis="trace test at t = 0.0015 (budget 1.5e-11) detects a missing eigenvalue below 1.66e4")


def family_spectra():
    conv = {}
    for r in csv.DictReader(open(os.path.join(ROOT, "numerics/moduli/data/convergence.csv"))):
        conv.setdefault(r["tau"], {}).setdefault(r["sector"], []).append(
            (int(r["index"]), float(r["lambda_prod_h0.05_p10"]), float(r["err_estimate"]), float(r["err_conservative"])))
    sec120 = {}
    for r in csv.DictReader(open(os.path.join(ROOT, "numerics/moduli/data/eigenvalue_flow_sectors.csv"))):
        sec120.setdefault(r["tau"], {}).setdefault(r["sector"], []).append(
            (float(r["lambda"]), float(r["err_estimate"]), float(r["err_conservative"])))
    orb = {}
    for r in csv.DictReader(open(os.path.join(ROOT, "numerics/moduli/data/eigenvalue_flow_orbifold.csv"))):
        orb.setdefault(r["tau"], []).append(float(r["lambda"]))
    out = {}
    for tau in TAUS:
        full = conv[tau]
        for sec, v in full.items():
            v.sort()
            check([x[0] for x in v] == list(range(len(v))), "consecutive indices per sector")
            check(all(abs(a[1] - b[0]) <= 1e-9 * max(1, b[0]) for a, b in zip(v, sec120[tau][sec])),
                  "first 120 per sector = eigenvalue_flow_sectors.csv")
        top = min(v[-1][1] for v in full.values())
        allv = sorted((x[1], x[2], x[3]) for v in full.values() for x in v)
        lam = np.array([x[0] for x in allv])
        ref = sorted(orb[tau])
        check(len(ref) == 400 and np.all(np.abs(lam[:400] - ref) <= 1e-9 * np.maximum(1, ref)),
              "merged sectors = committed orbifold list (first 400)")
        cut = 0.8 * top
        keep = lam <= cut
        fulld = dict(lam=lam[keep], eps=np.array([x[1] for x in allv])[keep], epsc=np.array([x[2] for x in allv])[keep],
                     lam_complete=cut, n_total=len(allv), lam_top=top,
                     basis="double-window slicing; exact count agreement of three mesh levels below 0.8 x least sector maximum; "
                           "trace test (t >= 0.0025, budget 2.2e-11) detects a missing eigenvalue below 9.8e3")
        v120 = sec120[tau]
        top120 = min(max(x[0] for x in v) for v in v120.values())
        a120 = sorted(x for v in v120.values() for x in v)
        lam120 = np.array([x[0] for x in a120])
        keep = lam120 <= top120
        d120 = dict(lam=lam120[keep], eps=np.array([x[1] for x in a120])[keep], epsc=np.array([x[2] for x in a120])[keep],
                    lam_complete=top120, n_total=len(a120), lam_top=top120,
                    basis="first 120 per sector, complete below the least sector maximum")
        out[tau] = dict(full=fulld, s120=d120)
    return out


# ------------------------------------------------------------------ the scan
class Case:
    def __init__(self, name, sig0, A_over_pi, ell, M, spec, Delta, variant, data, epskey="eps", do_obs=True):
        self.do_obs = do_obs
        self.name, self.sig0, self.M = name, sig0, M
        s = area_over_2pi(*sig0)
        self.A = float(2 * mp.pi * mpq(s))
        self.Aq = float(mpq(s)) / 2                               # A/(4 pi)
        self.S = [x for x in signatures(2 * s, M) if area_over_2pi(*x) == s]
        check(sig0 in self.S, "true signature in S")
        self.beta = max(float(sum(mpq(b_cone(0, m)) for m in o)) for _, o in self.S)
        self.ell, self.Delta, self.variant, self.data, self.epskey = ell, Delta, variant, data, epskey
        self.lam = spec["lam"]
        self.eps = spec[epskey]
        self.Nc = len(self.lam)
        self.cumeps = np.concatenate([[0.0], np.cumsum(self.eps)])  # cumeps[N] = sum_{j<N} eps_j
        self.i0 = self.S.index(sig0)
        self.memo = {}

    def Gs(self, G, t):
        return np.array([G.G(sig, self.Aq, t) for sig in self.S])

    def evaluate(self, G, t, exact_N=None):
        """At time t: (N_C1, sigma_C1, N_C2, sigma_C2, N_obs, N_rule, gap0, H) with N the least count, or
        None.  If exact_N is given, return (C1, C2) truth values at that N with the exact infimum over s."""
        if exact_N is None and float(t) in self.memo:
            return self.memo[float(t)]
        Gv = self.Gs(G, t)
        diffs = np.abs(Gv[:, None] - Gv[None, :]) + np.diag(np.full(len(Gv), np.inf))
        gaps = diffs.min(axis=1)
        lh = float(logH(self.ell, self.Delta, self.A, t))
        Ht = math.exp(min(lh, 700.0))
        part = np.cumsum(np.exp(-self.lam * t))                   # part[N-1] = Z~_N
        if exact_N is None and Ht > 10 * (self.Nc + float(np.max(np.abs(Gv)))):
            # E_N >= H(t) exceeds every |Z~_N - G_sigma| (Z~_N <= N): all of S passes, so neither criterion
            # can hold at this t, and N_obs, N_rule do not depend on H
            res = self._obs(part, Gv, gaps) if self.do_obs else {}
            res.update(gap0=float(gaps[self.i0]), H=lh, nearest=self._nearest(Gv))
            self.memo[float(t)] = res
            return res
        tb = TailBound(self.ell, self.Delta, self.A, self.beta, t)
        if exact_N is not None:
            N = exact_N
            mu = self.lam[N] - self.eps[N]
            E = Ht + math.exp(min(tb.log_tail_exact(mu), 700.0)) + t * self.cumeps[N]
            dev = np.abs(part[N - 1] - Gv)
            ps = dev <= E
            c1 = ps.sum() == 1 and bool(ps[self.i0])
            c2 = bool(ps[self.i0]) and E < gaps[self.i0] / 2
            check(not (ps.sum() == 1 and not ps[self.i0]), f"{self.name}: (C1) concludes a wrong signature")
            return c1, c2
        Ns = np.arange(1, self.Nc)                                # N with lambda~_N available
        mu = self.lam[Ns] - self.eps[Ns]
        E = Ht + np.exp(np.minimum(tb.log_tail(mu), 700.0)) + t * self.cumeps[Ns]
        Z = part[Ns - 1]
        dev = np.abs(Z[:, None] - Gv[None, :])                    # (N, sigma)
        ps = dev <= E[:, None]
        npass = ps.sum(axis=1)
        c1 = npass == 1
        c2 = ps & (E[:, None] < gaps[None, :] / 2)
        res = {}
        if c1.any():
            k = int(np.argmax(c1))
            who = int(np.argmax(ps[k]))
            check(who == self.i0, f"{self.name} M={self.M} {self.variant}: (C1) concludes {self.S[who]} at N={Ns[k]}, t={t}")
            res["C1"] = int(Ns[k])
        if c2.any(axis=1).any():
            k = int(np.argmax(c2.any(axis=1)))
            who = int(np.argmax(c2[k]))
            check(who == self.i0, f"{self.name} M={self.M} {self.variant}: (C2) concludes {self.S[who]} at N={Ns[k]}, t={t}")
            res["C2"] = int(Ns[k])
        if self.do_obs:
            res.update(self._obs(part, Gv, gaps))
        res["gap0"] = float(gaps[self.i0])
        res["H"] = lh
        res["nearest"] = self._nearest(Gv)
        self.memo[float(t)] = res
        return res

    def _nearest(self, Gv):
        return self.S[int(np.argmin(np.where(np.arange(len(Gv)) == self.i0, np.inf, np.abs(Gv - Gv[self.i0]))))]

    def _obs(self, part, Gv, gaps):
        """N_obs and N_rule (all N up to N_c, the full computed partial sum included)."""
        res = {}
        dev0 = np.abs(part - Gv[self.i0])
        ok = dev0 < gaps[self.i0] / 2
        bad = np.nonzero(~ok)[0]
        res["obs"] = int(bad[-1] + 2) if len(bad) else 1
        if res["obs"] > self.Nc:
            del res["obs"]
        nearest = np.argmin(np.abs(part[:, None] - Gv[None, :]), axis=1)
        bad = np.nonzero(nearest != self.i0)[0]
        res["rule"] = int(bad[-1] + 2) if len(bad) else 1
        if res["rule"] > self.Nc:
            del res["rule"]
        return res

    def weyl_estimate(self, G, crit):
        """Least N over t of the Weyl model (see the module docstring); (N, t) or (None, None).
        600 log-spaced t in [1e-9, 1], then 61 points in the bracket of the best."""
        pert_all = self.cumeps[-1]

        def at(t):
            Gv = self.Gs(G, t)
            gap = float(np.min(np.abs(np.delete(Gv, self.i0) - Gv[self.i0])))
            target = gap / 2 if crit == "C2" else gap
            Ht = math.exp(min(float(logH(self.ell, self.Delta, self.A, t)), 700.0))
            room = target - Ht - t * pert_all
            if room <= 0:
                return None
            tb = TailBound(self.ell, self.Delta, self.A, self.beta, t)
            sel = tb.s < t
            mu = float(np.min((tb.b[sel] - math.log(room)) / (t - tb.s[sel])))
            return max(1, math.ceil(mu * self.A / (4 * math.pi)))

        T = np.geomspace(1e-9, 1.0, 600)
        G.prepare(T)
        vals = [(at(float(t)), i) for i, t in enumerate(T)]
        vals = [(n, i) for n, i in vals if n is not None]
        if not vals:
            return (None, None)
        n0, i0 = min(vals)
        Tr = np.geomspace(T[max(i0 - 1, 0)], T[min(i0 + 1, len(T) - 1)], 61)
        G.prepare(Tr)
        ref = [(at(float(t)), float(t)) for t in Tr]
        return min((n, t) for n, t in ref if n is not None)

    def run(self, G, keep_t=False):
        G.prepare(TGRID)
        perT = []
        for t in TGRID:
            perT.append(self.evaluate(G, t))
        out = dict(per_t=perT if keep_t else None)
        for key in ("C1", "C2", "obs", "rule"):
            if key in ("obs", "rule") and not self.do_obs:
                out[key] = None
                continue
            vals = [(r[key], i) for i, r in enumerate(perT) if key in r]
            if not vals:
                out[key] = None
                continue
            nmin = min(v for v, _ in vals)
            idx = [i for v, i in vals if v == nmin]
            # refinement in the bracket of every grid point attaining the minimum
            Tref = sorted({float(x) for i in idx for x in np.geomspace(TGRID[max(i - 1, 0)], TGRID[min(i + 1, len(TGRID) - 1)], 61)})
            G.prepare(Tref)
            ref = [(self.evaluate(G, t).get(key), t) for t in Tref]
            ref = [(v, t) for v, t in ref if v is not None]
            nmin = min(v for v, _ in ref)
            tw = [t for v, t in ref if v == nmin]
            if key in ("C1", "C2"):
                # exact infimum over s: lower the count while it still succeeds somewhere in the window
                while nmin > 1:
                    hit = [t for t in Tref if self.evaluate(G, t, exact_N=nmin - 1)[0 if key == "C1" else 1]]
                    if not hit:
                        break
                    nmin, tw = nmin - 1, hit
                # and the reported count is confirmed with the exact infimum
                check(any(self.evaluate(G, t, exact_N=nmin)[0 if key == "C1" else 1] for t in tw),
                      f"{self.name}: count {nmin} confirmed with the exact infimum over s")
            tbest = tw[len(tw) // 2]
            r = self.evaluate(G, tbest)
            out[key] = dict(N=nmin, t=tbest, tlo=min(tw), thi=max(tw), lamN=float(self.lam[nmin]) if nmin < self.Nc else None,
                            gap0=r["gap0"], nearest=r["nearest"])
        if out["C1"] is None:
            out["C1w"] = self.weyl_estimate(G, "C1")
        if out["C2"] is None:
            out["C2w"] = self.weyl_estimate(G, "C2")
        return out


# ------------------------------------------------------------------ main
def main():
    G = Gfun()
    worst = G.validate()
    print(f"G_sigma (float64 Gauss-Legendre) against 30-digit mpmath: worst difference {worst:.1e} (relative for I, absolute for E_m)")
    inst = {r["orbifold"]: r for r in csv.DictReader(open(os.path.join(DATA, "instances.csv")))}
    tri = {"O(2,8,8)": triangle_spectrum((2, 8, 8)), "O(3,3,12)": triangle_spectrum((3, 3, 12))}
    fam = family_spectra()
    cases = []
    for name, sig in (("O(2,8,8)", (0, (2, 8, 8))), ("O(3,3,12)", (0, (3, 3, 12)))):
        cases.append((name, sig, (12,), {"full": tri[name]}))
    for tau in TAUS:
        cases.append((f"O_tau={tau}", (0, (3, 3, 3, 3)), (3, 12), fam[tau]))
    rows, trow, irows = [], [], []
    for name, sig, Ms, specs in cases:
        I = inst[name]
        ell = float(I["systole_lower_bound"])
        check(ell < float(I["systole_computed"]), "lower bound below the systole")
        deltas = {"B1": float(I["diam_upper_B1_2diamP"]), "B2": float(I["diam_upper_B2"]),
                  "true": float(I["diam_true_numerical"])}
        for M in Ms:
            Dcls = float(I[f"D_M{M}"])
            th = theorem_E_constants(2 * mp.pi * mpq(area_over_2pi(*sig)), mp.mpf(I["systole_lower_bound"]), M)
            plan = [("B1", "eps", "full"), ("B2", "eps", "full"), ("true", "eps", "full"), ("D", "eps", "full")]
            if name.startswith("O("):
                plan.append(("B1", "epsc", "full"))
            if "s120" in specs:
                plan.append(("B1", "eps", "s120"))
            for dv, ek, dk in plan:
                spec = specs[dk]
                Delta = Dcls if dv == "D" else deltas[dv]
                c = Case(name, sig, None, ell, M, spec, Delta, dv, dk, ek, do_obs=(dv == "B1" and ek == "eps"))
                keep = dv == "B1" and ek == "eps" and dk == "full"
                o = c.run(G, keep_t=keep)
                if keep:
                    for t, r in zip(TGRID, o["per_t"]):
                        trow.append([name, M, f"{t:.6e}", f"{r['gap0']:.6e}", str(r["nearest"]), f"{r['H'] / math.log(10):.3f}",
                                     r.get("C1", ""), r.get("C2", ""), r.get("obs", ""), r.get("rule", "")])
                    irows.append([name, str(sig), I["area_over_pi"] + "*pi", I["systole_lower_bound"], I["diam_upper_B1_2diamP"],
                                  I["diam_upper_B2"], I["diam_true_numerical"], f"{Dcls:.6g}", M, len(c.S), f"{c.beta:.6f}",
                                  f"{spec['lam_complete']:.1f}", c.Nc, spec["n_total"], dk, spec["basis"]])
                row = [name, M, len(c.S), dv, f"{Delta:.6g}", ek, dk, c.Nc, f"{spec['lam_complete']:.1f}"]
                for key in ("C1", "C2"):
                    r = o[key]
                    if r is not None:
                        row += [r["N"], f"{r['t']:.5g}", f"{r['tlo']:.5g}", f"{r['thi']:.5g}", f"{r['lamN']:.6g}", ""]
                    else:
                        w = o[key + "w"]
                        row += [f">{c.Nc - 1}", "", "", "", "", f"{w[0]} (t={w[1]:.3g})" if w[0] else "none"]
                for key in ("obs", "rule"):
                    r = o[key]
                    row += [r["N"], f"{r['t']:.4g}"] if r is not None else ["", ""]
                row += [str(o["C1"]["nearest"]) if o["C1"] else "", th["N"], mp.nstr(th["tstar"], 4)]
                rows.append(row)
                print(" | ".join(str(x) for x in row), flush=True)
    hdr = ["orbifold", "M", "S_size", "diameter_input", "Delta", "eps_j", "data", "N_complete", "lambda_complete",
           "N_C1", "t_C1", "tlo_C1", "thi_C1", "lambdaN_C1", "weyl_C1",
           "N_C2", "t_C2", "tlo_C2", "thi_C2", "lambdaN_C2", "weyl_C2",
           "N_obs", "t_obs", "N_rule", "t_rule", "nearest", "N_thm62", "tstar_thm62"]
    write(os.path.join(DATA, "practice.csv"), hdr, rows)
    write(os.path.join(DATA, "practice_t.csv"), ["orbifold", "M", "t", "gap", "nearest", "log10_H_bound", "N_C1", "N_C2",
                                                  "N_obs", "N_rule"], trow)
    write(os.path.join(DATA, "practice_inputs.csv"),
          ["orbifold", "signature", "area", "systole_lower_bound", "diam_B1_2diamP", "diam_B2", "diam_true_numerical",
           "D_A_eps_M", "M", "S_size", "beta", "lambda_complete", "N_complete", "n_computed", "data", "completeness_basis"], irows)
    # lambda~_j and eps_j, j <= 40, for the triangle orbifolds
    rows41 = []
    for name, sp in tri.items():
        for j, (l, e, ec, bc, idx, rel) in enumerate(sp["rows"][:41]):
            rows41.append([name, j, f"{l:.13g}", f"{e:.3e}", f"{ec:.3e}", bc, idx, rel])
    write(os.path.join(DATA, "triangle_spectra_first41.csv"),
          ["orbifold", "j", "lambda", "eps_j_err_estimate", "err_conservative", "boundary_condition", "index_in_file", "file"], rows41)
    # Table 2 of the manuscript with systole lower bounds
    t2 = []
    for A, Atxt, eps, M in ((mp.pi / 2, "pi/2", "1.8626", 8), (mp.pi / 2, "pi/2", "1.8626", 12),
                            (4 * mp.pi / 3, "4pi/3", "2.633915", 3), (4 * mp.pi / 3, "4pi/3", "0.693994", 3),
                            (4 * mp.pi / 3, "4pi/3", "0.693994", 12), (2 * mp.pi, "2pi", "0.1", 3),
                            (10 * mp.pi, "10pi", "1", 3), (10 * mp.pi, "10pi", "1", 12)):
        c = theorem_E_constants(A, mp.mpf(eps), M)
        bind = min((("t_1", c["t1"]), ("t_2", c["t2"]), ("t_3", c["t3"])), key=lambda x: x[1])[0]
        t2.append([Atxt, eps, M, c["kstar"], mp.nstr(c["D"], 5), mp.nstr(c["t1"], 5), mp.nstr(c["t2"], 4), mp.nstr(c["t3"], 4),
                   mp.nstr(c["tstar"], 5), mp.nstr(c["Gamma"], 4), mp.nstr(c["Lambda"], 4), c["N"], mp.nstr(c["delta"], 4), bind])
    write(os.path.join(DATA, "table2.csv"), ["A", "eps", "M", "kstar", "D", "t1", "t2", "t3", "tstar", "Gamma_star", "Lambda",
                                             "N", "delta", "binds"], t2)
    t1row2 = theorem_E_constants(mp.pi / 2, mp.mpf("1.8626"), 12)["t1"]
    check(abs(t1row2 - mp.mpf("6.8486487e-9")) < mp.mpf("1e-15"), "Table 2 row 2: t_1 = 6.8486e-9")
    print("wrote data/practice.csv, practice_t.csv, practice_inputs.csv, triangle_spectra_first41.csv, table2.csv")
    return 0


def write(path, hdr, rows):
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh, lineterminator="\n")
        w.writerow(hdr)
        w.writerows(rows)


if __name__ == "__main__":
    sys.exit(main())
