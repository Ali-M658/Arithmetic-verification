#!/usr/bin/env python3
"""Regenerate the data tables of paper/eigen/manuscript.tex from committed data.

Each table is written between the markers
    % BEGIN GENERATED TABLE <name>
    % END GENERATED TABLE <name>

    python3 paper/eigen/tools/make_tables.py           # rewrite the tables in place
    python3 paper/eigen/tools/make_tables.py --check   # exit 1 if any table is out of date

Sources (all committed, written by theory/eigen/practice.py and theory/eigen/instances.py):
  practice   theory/eigen/data/practice.csv (diameter inputs B1 and D, estimated eps_j, full spectra)
  spectra    theory/eigen/data/triangle_spectra_first41.csv
"""
import csv
import math
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TEX = ROOT / "paper" / "eigen" / "manuscript.tex"
DATA = ROOT / "theory" / "eigen" / "data"


def sci(x, digits=2):
    """a x 10^b in LaTeX, `digits` significant digits."""
    if x == 0:
        return "0"
    e = int(math.floor(math.log10(abs(x))))
    m = x / 10 ** e
    m = float(f"{m:.{digits - 1}f}")
    if m >= 10:
        m, e = m / 10, e + 1
    return f"{m:.{digits - 1}f}\\times10^{{{e}}}"


def tex_name(orb):
    if orb.startswith("O_tau="):
        return f"$\\Orb_\\vartheta$, $\\vartheta={orb[6:]}$"
    return "$\\Orb" + orb[1:] + "$"


def count(n, t, weyl, ncomp):
    """A count with its time, or '>N_c; estimate' when the criterion fails in the complete range."""
    if n and not n.startswith(">"):
        return f"${n}$ (${float(t):.3g}$)" if t else f"${n}$"
    est = int(float(weyl.split()[0])) if weyl else None
    w = f"; ${est}$" if est else ""                  # round 4 close-out: printed also when est <= N_c
    return f"$>{ncomp}${w}"


def table_practice():
    rows = list(csv.DictReader(open(DATA / "practice.csv")))
    key = {}
    for r in rows:
        if r["eps_j"] == "eps" and r["data"] == "full":
            key[(r["orbifold"], r["M"], r["diameter_input"])] = r
    inp = {r["orbifold"]: r for r in csv.DictReader(open(DATA / "practice_inputs.csv")) if r["data"] == "full"}
    order = [k for k in dict.fromkeys((r["orbifold"], r["M"]) for r in rows if r["diameter_input"] == "B1"
                                      and r["data"] == "full" and r["eps_j"] == "eps")]
    out = ["\\begin{table}[t]", "\\centering\\footnotesize",
           "\\caption{The a-posteriori test on computed spectra, with the instance inputs of Table~\\ref{tab:inputs} "
           "(diameter bound $\\Delta=2\\diam P$) and with the class-level diameter bound $D(A,\\ell,M)$ of "
           "Theorem~\\ref{thm:diam}: the least $N$ for which criterion (C1) or (C2) of Theorem~\\ref{thm:post} holds, "
           "with the time $t$ at which it holds; $>N_c$ means that the criterion fails for every $N$ up to the "
           "$N_c$ eigenvalues of the complete range, followed by the estimate of Section~\\ref{sec:numerical}; and "
           "the $N$ of Theorem~\\ref{thm:E} for the class $\\Cl(A,\\ell,M)$.}\\label{tab:practice}",
           "\\setlength{\\tabcolsep}{3.5pt}\\begin{tabular}{@{}llllllll@{}}", "\\toprule",
           "orbifold & $\\ell$ & $M$ & $|\\mathcal S|$ & (C1), $\\Delta$ & (C2), $\\Delta$ & (C1), $D(A,\\ell,M)$ & $N$, Thm~\\ref{thm:E}\\\\",
           "\\midrule"]
    for orb, M in order:
        b = key[(orb, M, "B1")]
        d = key[(orb, M, "D")]
        name = tex_name(orb)
        ell = inp[orb]["systole_lower_bound"]
        out.append(f"{name} & ${ell}$ & ${M}$ & ${b['S_size']}$ & {count(b['N_C1'], b['t_C1'], b['weyl_C1'], b['N_complete'])} & "
                   f"{count(b['N_C2'], b['t_C2'], b['weyl_C2'], b['N_complete'])} & "
                   f"{count(d['N_C1'], d['t_C1'], d['weyl_C1'], d['N_complete'])} & ${sci(float(b['N_thm62']))}$\\\\")
    out += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    return "\n".join(out)


def table_inputs():
    rows = list({r["orbifold"]: r for r in reversed(list(csv.DictReader(open(DATA / "practice_inputs.csv"))))
                 if r["data"] == "full"}.values())[::-1]
    out = ["\\begin{table}[t]", "\\centering\\footnotesize",
           "\\caption{Inputs of the test for the ten examples: exact area, the lower bound $\\ell$ for the "
           "systole, the proved diameter bound $2\\diam P$ and the computed diameter, the class-level bound "
           "$D(A,\\ell,M)$ of Theorem~\\ref{thm:diam}, and the complete range: the eigenvalues $\\lambda\\le\\lambda_c$, "
           "$N_c$ of them, of the $n$ computed; for the family the trace test alone covers $\\lambda<9.8\\times10^3$, and the range above rests on the agreement of the eigenvalue counts of three discretisations.}\\label{tab:inputs}",
           "\\setlength{\\tabcolsep}{4pt}\\begin{tabular}{@{}lllllllll@{}}", "\\toprule",
           "orbifold & area & $\\ell$ & $2\\diam P$ & $\\diam$ & $D$, $M=3$ & $D$, $M=12$ & $\\lambda_c$ & $N_c$ of $n$\\\\",
           "\\midrule"]
    inst = {r["orbifold"]: r for r in csv.DictReader(open(DATA / "instances.csv"))}
    for r in rows:
        orb = r["orbifold"]
        name = tex_name(orb)
        area = "$\\pi/2$" if r["area"].startswith("0.5") else "$4\\pi/3$"
        i = inst[orb]
        d3 = f"${float(i['D_M3']):.1f}$" if "tau" in orb else "--"
        out.append(f"{name} & {area} & ${r['systole_lower_bound']}$ & ${float(r['diam_B1_2diamP']):.3f}$ & "
                   f"${float(r['diam_true_numerical']):.3f}$ & {d3} & ${float(i['D_M12']):.1f}$ & "
                   f"${float(r['lambda_complete']):.0f}$ & ${r['N_complete']}$ of ${r['n_computed']}$\\\\")
    out += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    return "\n".join(out)


def table_spectra():
    rows = list(csv.DictReader(open(DATA / "triangle_spectra_first41.csv")))
    a = [r for r in rows if r["orbifold"] == "O(2,8,8)"]
    b = [r for r in rows if r["orbifold"] == "O(3,3,12)"]
    assert len(a) == len(b) == 41
    out = ["\\begin{table}[t]", "\\centering\\scriptsize",
           "\\caption{The computed eigenvalues $\\tilde\\lambda_j$, $1\\le j\\le40$, of $\\Orb(2,8,8)$ and "
           "$\\Orb(3,3,12)$, with the a-posteriori error estimates $\\epsilon_j$ (Section~\\ref{sec:numerical}); "
           "N or D marks the boundary condition on the triangle. aeb means $a\\times10^b$.}\\label{tab:spectra}",
           "\\setlength{\\tabcolsep}{2pt}\\begin{tabular}{@{}rllllll|rllllll@{}}", "\\toprule",
           "$j$ & \\multicolumn{3}{l}{$\\Orb(2,8,8)$} & \\multicolumn{3}{l|}{$\\Orb(3,3,12)$} & "
           "$j$ & \\multicolumn{3}{l}{$\\Orb(2,8,8)$} & \\multicolumn{3}{l}{$\\Orb(3,3,12)$}\\\\", "\\midrule"]

    def cell(r):
        e = float(r["eps_j_err_estimate"])
        es = f"{e:.0e}".replace("e-0", "e-").replace("e+0", "e")
        return f"{float(r['lambda']):.6f} & {es} & {r['boundary_condition']}"
    for j in range(1, 21):
        out.append(f"{j} & {cell(a[j])} & {cell(b[j])} & {j + 20} & {cell(a[j + 20])} & {cell(b[j + 20])}\\\\")
    out += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    return "\n".join(out)


TABLES = {"inputs": table_inputs, "practice": table_practice, "spectra": table_spectra}


def main():
    check = "--check" in sys.argv
    tex = TEX.read_text()
    new = tex
    for name, fn in TABLES.items():
        pat = re.compile(rf"(% BEGIN GENERATED TABLE {name}\n)(.*?)(% END GENERATED TABLE {name})", re.S)
        if not pat.search(new):
            sys.exit(f"markers for table {name} not found")
        body = fn()
        new = pat.sub(lambda m: m.group(1) + body + "\n" + m.group(3), new)
    if check:
        if new != tex:
            print("tables out of date")
            return 1
        print("tables up to date")
        return 0
    TEX.write_text(new)
    print("tables written")
    return 0


if __name__ == "__main__":
    sys.exit(main())
