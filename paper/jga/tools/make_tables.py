#!/usr/bin/env python3
"""Regenerate the tables of paper/jga/manuscript.tex from committed data.

Each table is written between the markers
    % BEGIN GENERATED TABLE <name>
    % END GENERATED TABLE <name>
in manuscript.tex, so that the manuscript stays a single file as the journal template asks.

    python3 paper/jga/tools/make_tables.py           # rewrite the tables in place
    python3 paper/jga/tools/make_tables.py --check   # exit 1 if any table is out of date

Sources (all committed):
  overlap     theory/threshold/first_overlap_vs_collision.csv
  thresholds  theory/stability/threshold_results.json
  fibres      theory/diophantine/data/groups.csv, theory/diophantine/data/ranks.txt
  density     review/audit/threshold/check_enum.txt (to S = 6000), cross-checked against
              theory/diophantine/data/per_S.csv (to S = 4800)
  enum        review/audit/threshold/tab_enum_reference.txt, re-derived here by enumeration
"""
import csv
import json
import math
import re
import sys
from decimal import ROUND_CEILING, ROUND_FLOOR, Decimal
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TEX = ROOT / "paper" / "jga" / "manuscript.tex"


def sig(x, digits, mode):
    """x rounded to `digits` significant figures, down or up, as a LaTeX a\\times10^{b}."""
    d = Decimal(repr(float(x))) if not isinstance(x, Fraction) else Decimal(x.numerator) / Decimal(x.denominator)
    e = d.adjusted()
    q = Decimal(1).scaleb(e - digits + 1)
    r = d.quantize(q, rounding=ROUND_FLOOR if mode == "down" else ROUND_CEILING)
    if r.adjusted() != e:  # rounding up crossed a power of ten
        e = r.adjusted()
    mant = r.scaleb(-e)
    mant = f"{mant:.{digits - 1}f}"
    return f"{mant}\\times10^{{{e}}}"


def tex_triple(t):
    return "(" + ",".join(str(x) for x in t) + ")"


# ---------------------------------------------------------------- overlap
def table_overlap():
    rows = list(csv.DictReader(open(ROOT / "theory/threshold/first_overlap_vs_collision.csv")))
    out = []
    for r in rows:
        p = int(r["p"])
        if p > 14:
            continue
        xs = Fraction(r["x_star"])
        xs_t = str(xs.numerator) if xs.denominator == 1 else f"{xs.numerator}/{xs.denominator}"
        pair = " and ".join("$" + tex_triple(eval(t)) + "$" for t in r["triads"].split(";"))
        out.append(f"{p} & ${xs_t}$ & {r['S_star']} & {r['first_collision_S']} & {r['gap']} & {pair} \\\\")
    assert [int(r["p"]) for r in rows if int(r["p"]) <= 14] == list(range(2, 15))
    body = "\n".join(out)
    return (
        "\\begin{table}[t]\n"
        "\\caption{First overlap and first collision of the adjacent strata $p$ and $p+1$, for $2\\le p\\le14$, "
        "from the exhaustive enumeration of all hyperbolic triads with $S\\le600$. The gap is the first collision sum "
        "minus $S^*(p)$; it vanishes only for $p=2$ and $p=4$ (Proposition~\\ref{prop:tangency}).}\\label{tab:overlap}\n"
        "\\centering\\small\n"
        "\\begin{tabular}{@{}rrrrrl@{}}\n\\toprule\n"
        "$p$ & $x^*(p)$ & $S^*(p)$ & first collision & gap & colliding pair\\\\\n\\midrule\n"
        f"{body}\n\\bottomrule\n\\end{{tabular}}\n\\end{{table}}"
    )


# ------------------------------------------------------------- thresholds
def table_thresholds():
    d = json.load(open(ROOT / "theory/stability/threshold_results.json"))
    out = []
    for key, v in d.items():
        m = eval(key)
        n = len(m)
        cert_exact = Fraction(v["delta_cert_exact"])
        up = v["delta_up"]
        thm_s = sig(v["delta_thm"], 3, "down")
        cert_s = sig(cert_exact, 4, "down")
        up_s = sig(up, 4, "up")
        ratio = float(Decimal(up_s.split("\\times")[0]).scaleb(int(up_s.split("{")[1].rstrip("}")))) / float(
            Decimal(cert_s.split("\\times")[0]).scaleb(int(cert_s.split("{")[1].rstrip("}"))))
        eps_s = sig(v["eps_cert"], 2, "down")
        out.append(f"${tex_triple(m)}$ & {n} & ${thm_s}$ & ${cert_s}$ & ${up_s}$ & {ratio:.2f} & ${eps_s}$ \\\\")
    body = "\n".join(out)
    return (
        "\\begin{table}[t]\n"
        "\\caption{Thresholds for exact recovery of integer orders under the uniform model $|\\delta c_j|\\le\\delta$: "
        "the closed form $\\delta_{\\rm thm}$ of Theorem~\\ref{thm:S4}, the certified $\\delta_{\\rm cert}$ of "
        "Proposition~\\ref{prop:S5}, a constructed failure $\\delta_{\\rm up}$, their ratio, and the largest certified "
        "uniform relative error $\\epsilon_{\\rm cert}$.}\\label{tab:thresholds}\n"
        "\\centering\\footnotesize\n"
        "\\begin{tabular}{@{}lrlllrl@{}}\n\\toprule\n"
        "$m$ & $n$ & $\\delta_{\\rm thm}$ & $\\delta_{\\rm cert}$ & $\\delta_{\\rm up}$ & ratio & $\\epsilon_{\\rm cert}$\\\\\n\\midrule\n"
        f"{body}\n\\bottomrule\n\\end{{tabular}}\n\\end{{table}}"
    )


# ----------------------------------------------------------------- fibres
def table_fibres():
    first = {}
    for r in csv.DictReader(open(ROOT / "theory/diophantine/data/groups.csv")):
        k = int(r["multiplicity"])
        if k not in first:
            first[k] = r
    ranks = {}
    txt = (ROOT / "theory/diophantine/data/ranks.txt").read_text()
    for blk in txt.split("\nlambda = ")[1:]:
        lam = blk.split()[0]
        rk = re.search(r"rank:\s+(\d+) <= rank <= (\d+)\s+-> PROVEN", blk)
        assert rk and rk.group(1) == rk.group(2)
        ranks[Fraction(lam)] = int(rk.group(1))
    out = []
    for k in sorted(first):
        r = first[k]
        S = int(r["S"])
        R = Fraction(int(r["R_num"]), int(r["R_den"]))
        lam = S * R
        lam_t = str(lam.numerator) if lam.denominator == 1 else f"{lam.numerator}/{lam.denominator}"
        mem = "; ".join("$" + tex_triple(eval(t)) + "$" for t in r["triples"].split(";"))
        out.append(f"{k} & {S} & ${lam_t}$ & {ranks[lam]} & {mem} \\\\")
    assert sorted(first) == [2, 3, 4, 5, 6]
    body = "\n".join(out)
    return (
        "\\begin{table}[t]\n"
        "\\caption{The first degeneracy class of each size $k$, from the enumeration of all hyperbolic triads with "
        "$S\\le4800$: its sum, $\\Lambda=S_1R$, the Mordell--Weil rank of $C_\\Lambda$ (proved by coinciding PARI "
        "bounds), and its members, which share $c_1$ and $c_2$. No class of size $7$ occurs up to "
        "$S=4800$.}\\label{tab:fibres}\n"
        "\\centering\\footnotesize\n"
        "\\begin{tabular}{@{}rrrrp{0.62\\textwidth}@{}}\n\\toprule\n"
        "$k$ & $S$ & $\\Lambda$ & rank & members\\\\\n\\midrule\n"
        f"{body}\n\\bottomrule\n\\end{{tabular}}\n\\end{{table}}"
    )


# ---------------------------------------------------------------- density
def table_density():
    per = {int(r["S"]): r for r in csv.DictReader(open(ROOT / "theory/diophantine/data/per_S.csv"))}
    txt = (ROOT / "review/audit/threshold/check_enum.txt").read_text()
    sec = txt.split("== conj:density test to S=6000", 1)[1]
    rows = []
    for line in sec.splitlines()[2:]:
        f = line.split()
        if len(f) != 7 or not f[0].isdigit():
            break
        rows.append((int(f[0]), int(f[1]), int(f[3]), f[5]))
    keep = [100, 200, 300, 400, 500, 600, 1000, 2000, 3000, 4000, 4800, 6000]
    rows = [r for r in rows if r[0] in keep]
    assert [r[0] for r in rows] == keep
    maxfib, cur = {}, 0
    for S in sorted(per):
        cur = max(cur, int(per[S]["max_fibre"]))
        maxfib[S] = cur
    out = []
    r18 = per[18]
    out.append(f"18 & {r18['cum_pairs']} & {r18['cum_classes']} & {r18['cum_prim_classes']} & {maxfib[18]} & -- \\\\")
    for S, pairs, classes, loc in rows:
        if S in per:
            assert int(per[S]["cum_pairs"]) == pairs and int(per[S]["cum_classes"]) == classes, S
            prim, mf = per[S]["cum_prim_classes"], str(maxfib[S])
        else:
            prim, mf = "--", "--"
        out.append(f"{S} & {pairs} & {classes} & {prim} & {mf} & {loc} \\\\")
    body = "\n".join(out)
    return (
        "\\begin{table}[t]\n"
        "\\caption{Cumulative counts of two-coefficient degeneracies with sum at most $S$, in both conventions: "
        "pairs $\\N(S)$ and classes $\\N_{\\rm cl}(S)$, with the primitive classes, the largest class size so far, and "
        "the local exponent of $\\N$ on $[S/2,S]$. Exhaustive enumeration; the primitive counts are recorded to "
        "$S=4800$.}\\label{tab:density}\n"
        "\\centering\\small\n"
        "\\begin{tabular}{@{}rrrrrr@{}}\n\\toprule\n"
        "$S$ & pairs $\\N(S)$ & classes $\\N_{\\rm cl}(S)$ & primitive classes & largest class & local exponent\\\\\n\\midrule\n"
        f"{body}\n\\bottomrule\n\\end{{tabular}}\n\\end{{table}}"
    )


# ------------------------------------------------------------------- enum
def table_enum():
    ref = {}
    for line in (ROOT / "review/audit/threshold/tab_enum_reference.txt").read_text().splitlines():
        m = re.match(r"S=(\d+) \(\d+ triads\): (.*)", line)
        if m:
            ref[int(m.group(1))] = [(eval(t.split()[0]), Fraction(t.split()[1])) for t in m.group(2).split("; ")]
    # re-derive by enumeration
    for S in range(10, 19):
        mine = []
        for p in range(2, S):
            for q in range(p, S):
                r = S - p - q
                if r < q:
                    continue
                R = Fraction(1, p) + Fraction(1, q) + Fraction(1, r)
                if R < 1:
                    mine.append(((p, q, r), R))
        assert mine == ref[S], S
    assert sum(len(v) for v in ref.values()) == 83
    out = []
    for S in range(10, 19):
        items = []
        Rs = [R for _, R in ref[S]]
        for t, R in ref[S]:
            s = f"{tex_triple(t)}\\,{R.numerator}/{R.denominator}"
            items.append(f"$\\mathbf{{{s}}}$" if Rs.count(R) > 1 else f"${s}$")
        joined = "; ".join(items)
        out.append(f"{S} & {joined} \\\\")
    body = "\n".join(out)
    return (
        "\\begin{table}[ht]\n"
        "\\caption{All $83$ hyperbolic triads $(p,q,r)$ with $10\\le S_1\\le18$, each followed by its reciprocal sum "
        "$R$. The only coincidence of $R$ within a sum is the pair in bold.}\\label{tab:enum}\n"
        "\\centering\\footnotesize\n"
        "\\begin{tabular}{@{}rp{0.9\\textwidth}@{}}\n\\toprule\n"
        "$S_1$ & triads and $R$\\\\\n\\midrule\n"
        f"{body}\n\\bottomrule\n\\end{{tabular}}\n\\end{{table}}"
    )


TABLES = {"overlap": table_overlap, "thresholds": table_thresholds, "fibres": table_fibres,
          "density": table_density, "enum": table_enum}


def main():
    src = TEX.read_text(encoding="utf-8")
    new = src
    for name, fn in TABLES.items():
        pat = re.compile(r"(% BEGIN GENERATED TABLE " + name + r"\n).*?(% END GENERATED TABLE " + name + r")", re.S)
        if not pat.search(new):
            raise SystemExit(f"markers for table {name} not found")
        new = pat.sub(lambda m: m.group(1) + fn() + "\n" + m.group(2), new)
    if "--check" in sys.argv:
        if new != src:
            print("tables are out of date; run make_tables.py")
            sys.exit(1)
        print("tables up to date")
        return
    TEX.write_text(new, encoding="utf-8")
    print("tables written")


if __name__ == "__main__":
    main()
