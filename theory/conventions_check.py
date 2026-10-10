#!/usr/bin/env python3
"""Checks that the translations in theory/CONVENTIONS.md are right.

For each of the signatures  (2,8,8), (3,3,12), (3,10,15,30), (1;15), (0;3,3,5,5)  this
script recomputes the first four heat coefficients c_1, c_2, c_3, c_4 (the coefficients of
t^-1, t^0, t^1, t^2; paper convention, K = -1) from

  * the reference formulas of CONVENTIONS.md, retyped here from the Selberg identity
    term and Ucar (4.25)/(4.33) with nothing imported;
  * each repository file's own formulas, called through the translation that
    CONVENTIONS.md gives for that file's indexing and normalisation, and asserts that
    every file reproduces the reference.

A file whose own functions cannot take the signature (genus-0 only, triples only) is
reported as SKIP for that signature, never silently passed; its building blocks are
tested instead where the table says "blocks".

Run from anywhere:  python3 theory/conventions_check.py
Needs: sympy, mpmath (requirements.txt).  Exits nonzero on any failed assert.
"""

import ast
import importlib.util
import os
import sys
from fractions import Fraction as Fr
from math import comb, factorial

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

SIGNATURES = [
    ("(2,8,8)", 0, (2, 8, 8)),
    ("(3,3,12)", 0, (3, 3, 12)),
    ("(3,10,15,30)", 0, (3, 10, 15, 30)),
    ("(1;15)", 1, (15,)),
    ("(0;3,3,5,5)", 0, (3, 3, 5, 5)),
]
NCOEF = 4


# --------------------------------------------------------------------------- reference
def _bern(n, _c={0: Fr(1)}):
    if n not in _c:
        _c[n] = -sum(comb(n + 1, j) * _bern(j) for j in range(n)) / (n + 1)
    return _c[n]


def _bern_half(n):
    return Fr(1) if n == 0 else (Fr(1, 2 ** (n - 1)) - 1) * _bern(n)


def ref_alpha(j):
    """alpha_j = (t^(j-1) coefficient of the Selberg identity term) / (Area/4pi), K = -1:
    e^{-t/4} [1/t - 4 sum_k (-t)^k/k! J_k],  J_k = (1 - 2^{-2k-1}) (-1)^k B_{2k+2} / (4(k+1))."""
    N = j + 2
    J = [(1 - Fr(1, 2 ** (2 * k + 1))) * (-1) ** k * _bern(2 * k + 2) / (4 * (k + 1)) for k in range(N)]
    inner = {-1: Fr(1)}
    for k in range(N):
        inner[k] = inner.get(k, 0) - 4 * Fr((-1) ** k, factorial(k)) * J[k]
    out = Fr(0)
    for k, v in inner.items():                   # times e^{-t/4} = sum_i (-1/4)^i t^i / i!
        i = (j - 1) - k
        if i >= 0:
            out += v * Fr((-1) ** i, 4 ** i * factorial(i))
    return out


def ref_b(l, m):
    """b_l(m) at K = -1 (Ucar (4.25), (4.33)): (-1)^l sum_i 2/(4^i i!) c_{l-i}(pi/m)."""
    def c(L):
        s = sum(comb(2 * L + 2, 2 * j) * (Fr(m) ** (2 * j) - 1) * _bern(2 * j) * _bern_half(2 * L + 2 - 2 * j)
                for j in range(L + 2))
        return Fr((-1) ** L, 4 * m * factorial(L + 1) * (2 * L + 1)) * s
    return (-1) ** l * sum(Fr(2, 4 ** i * factorial(i)) * c(l - i) for i in range(l + 1))


def area_over_4pi(g, m):
    """c_1 = Area/(4 pi) = (2g - 2 + sum(1 - 1/m_i)) / 2."""
    return (2 * g - 2 + sum(1 - Fr(1, x) for x in m)) / 2


def ref_c(g, m, n=NCOEF):
    """[c_1, ..., c_n]:  c_1 = Area/4pi,  c_j = (Area/4pi) alpha_{j-1} + sum_i b_{j-2}(m_i)."""
    a = area_over_4pi(g, m)
    return [a] + [a * ref_alpha(j - 1) + sum(ref_b(j - 2, x) for x in m) for j in range(2, n + 1)]


# --------------------------------------------------------------------------- loaders
def load(path, name, extra_paths=()):
    for p in extra_paths:
        if p not in sys.path:
            sys.path.insert(0, p)
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, path))
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def load_defs_only(path, wanted):
    """Execute only the imports and the named function definitions of a script that also
    runs its checks at import time, so that the script's own formulas can be called (plus its
    two module-level assignments, the Bernoulli cache _B and the symbol m)."""
    src = open(os.path.join(ROOT, path)).read()
    tree = ast.parse(src)
    keep = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))
            or (isinstance(n, ast.FunctionDef) and n.name in wanted)
            or (isinstance(n, ast.Assign) and any(getattr(t, "id", "") in ("_B", "m") for t in n.targets))]
    ns = {}
    exec(compile(ast.Module(body=keep, type_ignores=[]), path, "exec"), ns)
    missing = [w for w in wanted if w not in ns]
    assert not missing, (path, missing)
    return ns


class Skip(Exception):
    pass


# --------------------------------------------------------------------------- adapters
# Each adapter returns [c_1, ..., c_4] in the paper convention, or raises Skip(reason).
# The comment on each states the translation (CONVENTIONS.md section 3).

def make_adapters():
    A = {}

    stab = load("theory/stability/stab_common.py", "stab_common", [os.path.join(ROOT, "theory/stability")])
    sig = load("theory/signatures/sig_common.py", "sig_common", [os.path.join(ROOT, "theory/signatures")])
    aud = load("theory/audibility/audibility_common.py", "audibility_common",
               [os.path.join(ROOT, "theory/audibility")])
    div = load("theory/divergence/divergence.py", "divergence", [os.path.join(ROOT, "theory/divergence")])
    cur = load("theory/curvature/curvature_checks.py", "curvature_checks", [os.path.join(ROOT, "theory/curvature")])
    num = load("numerics/theory.py", "numerics_theory", [os.path.join(ROOT, "numerics")])
    enum = load("code/orbifold_enum.py", "orbifold_enum", [os.path.join(ROOT, "code")])
    vid = load("code/verify_identities.py", "verify_identities", [os.path.join(ROOT, "code")])
    cone = load_defs_only("theory/cone-coefficients/verify_cone_coefficients.py",
                          ["bern", "bern_half", "R", "c_ucar", "b_ratio"])

    # theory/stability: H_nu, nu = -1, 0, 1, 2  ->  c_{nu+2}.  heat_direct(m, N) returns
    # [H_{-1}, ..., H_{N-2}] = [c_1, ..., c_N]; genus 0 only.
    def stability(g, m):
        if g != 0:
            raise Skip("heat_direct is genus 0 only")
        return list(stab.heat_direct(list(m), NCOEF))
    A["theory/stability  heat_direct  (H_nu = c_{nu+2})"] = stability

    # same file, building blocks b_cone, alpha_smooth: area is supplied for any genus.
    def stability_blocks(g, m):
        a = area_over_4pi(g, m)
        return [a] + [a * stab.alpha_smooth(nu + 1) + sum(stab.b_cone(nu, x) for x in m)
                      for nu in range(NCOEF - 1)]
    A["theory/stability  blocks   (alpha_j, b_nu)"] = stability_blocks

    # theory/signatures: heat_key(g, m, k) = (s, C_0, ..., C_{k-2}), s = Area/2pi = 2 c_1,
    # C_l = sum_i b_l(m_i);  c_{l+2} = (Area/4pi) alpha_{l+1} + C_l with alpha from the
    # reference (signatures never needs the smooth constants, only that they are
    # proportional to the area).
    def signatures(g, m):
        key = sig.heat_key(g, tuple(m), NCOEF)
        s, C = key[0], key[1:]
        a = s / 2
        return [a] + [a * ref_alpha(l + 1) + C[l] for l in range(NCOEF - 1)]
    A["theory/signatures heat_key   (s = 2 c_1, C_l)"] = signatures

    # theory/divergence: coeff_hyperbolic(l, cones, genus) = t^l total (a_l) = c_{l+2};
    # c_1 = |chi|/2.
    def divergence(g, m):
        chi = Fr(2 - 2 * g) - sum(1 - Fr(1, x) for x in m)
        return [-chi / 2] + [div.coeff_hyperbolic(l, tuple(m), genus=g) for l in range(NCOEF - 1)]
    A["theory/divergence coeff_hyperbolic (a_l = c_{l+2})"] = divergence

    # theory/curvature: b_ucar(l, m) = b_l(m)/K^l, so b_l = (-1)^l b_ucar at K = -1.
    def curvature(g, m):
        a = area_over_4pi(g, m)
        return [a] + [a * ref_alpha(l + 1) + (-1) ** l * sum(cur.b_ucar(l, x) for x in m)
                      for l in range(NCOEF - 1)]
    A["theory/curvature  b_ucar    (b_l/K^l)"] = curvature

    # theory/cone-coefficients: b_ratio(l, k) = b_l/kappa^l (sympy), kappa = K.
    def cone_coeffs(g, m):
        a = area_over_4pi(g, m)
        return [a] + [a * ref_alpha(l + 1)
                      + (-1) ** l * sum(Fr(int(cone["b_ratio"](l, x).p), int(cone["b_ratio"](l, x).q)) for x in m)
                      for l in range(NCOEF - 1)]
    A["theory/cone-coefficients b_ratio (b_l/kappa^l)"] = cone_coeffs

    # numerics/theory.py: pillow_coeffs(pqr)['coef'][nu] is keyed by the t-power nu = -1, 0, 1, 2
    # (c_{nu+2}); triples only.  a_smooth_over_vol(j) = alpha_j, b_cone(nu, k) = b_nu.
    def numerics(g, m):
        if g != 0 or len(m) != 3:
            raise Skip("pillow_coeffs is for triangular pillows only")
        co = num.pillow_coeffs(tuple(m), NCOEF)["coef"]
        return [co[nu] for nu in range(-1, NCOEF - 1)]
    A["numerics/theory   pillow_coeffs (coef[nu], nu = t-power)"] = numerics

    def numerics_blocks(g, m):
        a = area_over_4pi(g, m)
        return [a] + [a * num.a_smooth_over_vol(nu + 1) + sum(num.b_cone(nu, x) for x in m)
                      for nu in range(NCOEF - 1)]
    A["numerics/theory   blocks   (a_smooth_over_vol, b_cone)"] = numerics_blocks

    # theory/audibility: I_n(m) = (R, P_1, P_3, ..., P_{2n-3}); the j-th coefficient c_j is the first
    # to involve P_{2j-3}.  Power sums come from audibility_common's Newton identities.  The affine
    # map c = L I + h0 is stability.front_end (L independent of the signature, h0 = ((2g-2+n)/2)(alpha_0..)).
    def audibility(g, m):
        n = len(m)
        e = aud.elementary([sp.Integer(x) for x in m])
        P = aud.power_sums_from_e(e, 2 * NCOEF - 3)
        R = sp.Rational(e[n - 1]) / sp.Rational(e[n])
        I = [Fr(int(R.p), int(R.q))] + [Fr(int(P[2 * k - 1])) for k in range(1, NCOEF)]
        L, _ = stab.front_end(NCOEF)
        h0 = [Fr(2 * g - 2 + n, 2) * (1 if j == 0 else stab.alpha_smooth(j)) for j in range(NCOEF)]
        return [sum(L[j][k] * I[k] for k in range(NCOEF)) + h0[j] for j in range(NCOEF)]
    A["theory/audibility I_n -> stability.front_end (c = L I_4 + h0)"] = audibility

    # code/orbifold_enum.py: area_over_pi(orders) = Area/pi (genus 0), so c_1 = area_over_pi/4;
    # code/verify_identities.py: a0_of(orders) = chi/6 + sum cone(m) = c_2 (triples).
    def code_files(g, m):
        if g != 0:
            raise Skip("orbifold_enum is genus 0 only")
        c1 = enum.area_over_pi(list(m)) / 4
        if len(m) == 3:
            return [c1, vid.a0_of(tuple(m)), None, None]
        return [c1, None, None, None]
    A["code/             orbifold_enum.area_over_pi/4, verify_identities.a0_of"] = code_files

    return A


import sympy as sp  # noqa: E402  (used by the audibility adapter)


FREE_SYMBOLS = {
    "d_j": r"\bd_\{?[0-9j]", "varsigma": r"ς|\\varsigma", "varpi": r"ϖ|\\varpi", "varkappa": r"ϰ|\\varkappa",
    "mathfrak q": r"𝔮|\\mathfrak\{q\}", "vartheta": r"ϑ|\\vartheta", "mathbb K": r"𝕂|\\mathbb\{K\}",
    "mathfrak h_t": r"𝔥_t|\\mathfrak\{h\}_t", "mathfrak D": r"𝔇|\\mathfrak\{D\}", "delta g": r"δg|\\delta g",
    "N^*": r"N\^\*|N\^\{\*\}", "key_2": r"key_2|key_\{2\}", "Hyp": r"\bHyp\b", "cond(M)": r"\bcond\(M",
}


def check_free_symbols():
    """Each symbol CONVENTIONS.md introduces occurs nowhere else in the repository's text files."""
    import re
    skip_dirs = {".git", ".venv", "research", "refs", "__pycache__", "runs", "refs_cache", "sources_cache", "env", "jga",
                 "revision", "audit-2", "literature-pass", "referee-sim",
                 "eigen", "varcurv", "arxiv"}   # varcurv/: variable-curvature work of its own session, with its own notation (d_j); session work areas: reports, fetched papers, check transcripts; eigen/ holds the fragments of manuscript Section 4, which use the manuscript's notation (d_k, varpi)
    skip_files = {"CONVENTIONS.md", "conventions_check.py"}
    texts = {}
    # review/ is not walked: review rounds, audits and literature notes are prose or fetched text, not paper notation
    for top in ("theory", "numerics", "code", "paper", "."):
        for dp, dn, fn in os.walk(os.path.join(ROOT, top)):
            dn[:] = [d for d in dn if d not in skip_dirs and not d.startswith(".")]
            if top == "." and dp != ROOT:
                continue
            for f in fn:
                if f in skip_files or not f.endswith((".md", ".tex", ".py", ".sh", ".txt", ".csv")):
                    continue
                path = os.path.join(dp, f)
                if path not in texts:
                    texts[path] = open(path, errors="ignore").read()
    assert len(texts) > 100, len(texts)
    for name, pat in FREE_SYMBOLS.items():
        hits = [os.path.relpath(p, ROOT) for p, t in texts.items() if re.search(pat, t)]
        assert not hits, f"replacement symbol {name!r} is already used in {hits[:3]}"
    print(f"{len(FREE_SYMBOLS)} replacement symbols are free across {len(texts)} text files")


def main():
    adapters = make_adapters()
    refs = {name: ref_c(g, m) for name, g, m in SIGNATURES}
    # the reference itself against independently known values
    assert refs["(2,8,8)"] == [Fr(1, 8), Fr(67, 48), Fr(-1601, 480), Fr(555313, 20160)], refs["(2,8,8)"]
    assert refs["(3,3,12)"][2] == Fr(-867, 160)                       # numerics/REPORT.md 4(d)
    for name, g, m in SIGNATURES:                                    # c_2 = chi/6 + sum (m^2 - 1)/(12 m)
        chi = 2 - 2 * g - sum(1 - Fr(1, x) for x in m)
        assert refs[name][1] == chi / 6 + sum(Fr(x * x - 1, 12 * x) for x in m), name
    # alpha_j of the Selberg identity term equals Ucar (4.35) (numerics/theory.py)
    num = sys.modules["numerics_theory"]
    for j in range(0, 8):
        assert ref_alpha(j) == num.a_smooth_over_vol(j), j
    for j in range(0, 6):
        assert ref_alpha(j) == sys.modules["stab_common"].alpha_smooth(j), j

    header = f"{'file / function (translation)':<66}" + "".join(f"{n:>14}" for n, _, _ in SIGNATURES)
    print(header)
    print("-" * len(header))
    ok = skip = 0
    for label, fn in adapters.items():
        cells = []
        for name, g, m in SIGNATURES:
            try:
                got = fn(g, m)
            except Skip:
                cells.append("skip")
                skip += 1
                continue
            for j, (x, y) in enumerate(zip(got, refs[name]), start=1):
                if x is None:
                    continue
                assert Fr(x) == y, f"{label}  {name}  c_{j}: got {x}, reference {y}"
            cells.append("ok")
            ok += 1
        print(f"{label:<66}" + "".join(f"{c:>14}" for c in cells))
    # locality: its cyclotomic-field evaluation of the elliptic Taylor coefficients is asserted equal
    # to numerics/theory.b_cone, which the rows above tie to the reference.
    loc = load("theory/locality/check_locality.py", "check_locality", [os.path.join(ROOT, "theory/locality")])
    all_orders = sorted({x for _, _, m in SIGNATURES for x in m if x <= 15})
    loc.check_elliptic_term(numax=3, orders=tuple(x for x in all_orders if x in (3, 5, 15) or x < 6))
    for name, g, m in SIGNATURES:
        for l in range(NCOEF - 1):
            for x in set(m):
                assert ref_b(l, x) == num.b_cone(l, x)
    print("theory/locality     elliptic Taylor coefficients (beta_nu = b_nu)       asserted equal to numerics b_cone")
    # numerics: Delta c_3, Delta c_4 (its c1, c2) of the pair (2,8,8) - (3,3,12)
    d = [x - y for x, y in zip(refs["(2,8,8)"], refs["(3,3,12)"])]
    pd = num.predicted_difference(3)
    assert d[0] == 0 and d[1] == 0
    assert d[2] == pd[1] == Fr(25, 12) and d[3] == pd[2] == Fr(-1775, 24)
    print("numerics            c1, c2 of D(t) = Z_(2,8,8) - Z_(3,3,12)  =  d_3, d_4 = 25/12, -1775/24")
    # beta (divergence, unsigned) vs beta (locality, signed): b_l = (-1)^l beta_l
    div = sys.modules["divergence"]
    for l in range(NCOEF + 2):
        for x in (2, 3, 8, 15):
            assert num.b_cone(l, x) == (-1) ** l * div.b_ucar(l, x) and div.b_ucar(l, x) > 0
    # d_j: the D(t) coefficients are the coefficient differences, indexed by the t-power in the files
    check_free_symbols()
    assert ok >= 5 * 5, ok            # no adapter silently vanished
    print(f"\n{ok} checks passed, {skip} skipped (a file's own function does not cover that signature)")
    print("CONVENTIONS CHECK PASSED")


if __name__ == "__main__":
    main()
