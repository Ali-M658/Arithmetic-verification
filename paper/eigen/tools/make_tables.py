#!/usr/bin/env python3
"""Regenerate the data tables of paper/eigen/manuscript.tex from committed data.

Each table is written between the markers
    % BEGIN GENERATED TABLE <name>
    % END GENERATED TABLE <name>

    python3 paper/eigen/tools/make_tables.py           # rewrite the tables in place
    python3 paper/eigen/tools/make_tables.py --check   # exit 1 if any table is out of date

Sources (all committed, written by theory/eigen/practice.py and theory/eigen/instances.py):
  E          theory/eigen/data/table2.csv (the constants of Theorem 6.2)
  practice   theory/eigen/data/practice.csv (diameter inputs B1 and D, estimated eps_j, full spectra)
  spectra    theory/eigen/data/triangle_spectra_first41.csv
  certgap    theory/eigen/data/certified_gap.csv (theory/eigen/certified_gap.py) with computed_gap.csv
  certdetail theory/eigen/data/certified_gap_detail.csv (theory/eigen/certified_gap.py)
  certencl   theory/eigen/data/certified_gap_enclosures.csv (theory/eigen/certified_gap.py; round 10)
  (the certgap table also reads theory/eigen/data/certified_gap_omissions.csv for Lambda_o; round 10)
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
    m = math.ceil(m * 10 ** (digits - 1) - 1e-9) / 10 ** (digits - 1)   # rounded up: N and the count constants are upper bounds
    if m >= 10:
        m, e = m / 10, e + 1
    return f"{m:.{digits - 1}f}\\times10^{{{e}}}"


def tex_name(orb):
    if orb.startswith("O_tau="):
        return f"$\\Orb_\\vartheta$, $\\vartheta={orb[6:]}$"
    return "$\\Orb" + orb[1:] + "$"


def count(n, t, weyl, ncomp):
    """A count with its time, or '>=N_c; est. estimate' when the criterion fails in the complete range."""
    if n and not n.startswith(">"):
        return f"${n}$ (${float(t):#.3g}$)" if t else f"${n}$"
    est = int(float(weyl.split()[0])) if weyl else None
    w = f"; est.~${est}$" if est else ""             # round 4 close-out: printed also when est <= N_c
    return f"$\\ge{ncomp}${w}"


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
           "\\caption{The criterion of Theorem~\\ref{thm:post} on the computed spectra, with estimated errors and lists assumed complete: "
           "the least $N$ for which (C1) or (C2) holds with the instance's diameter bound $\\Delta=2\\diam P$, and for which (C1) holds with "
           "the class-level count of Lemma~\\ref{lem:countK}, with the geometric middle of the window of times at which that $N$ holds; "
           "the least $N$ for which (C1) holds against all of $\\Sig(A,M)$, with the area bound $A$ and $C_*(A,\\ell,M)$ only; "
           "and the $N$ of Theorem~\\ref{thm:E} for the class $\\Cl(A,\\ell,M)$. Here, as in Theorem~\\ref{thm:post}, the test with $N$ uses "
           "$\\tilde\\lambda_0,\\dots,\\tilde\\lambda_N$; Theorem~\\ref{thm:E} uses $N$ eigenvalues.}\\label{tab:practice}",
           "\\setlength{\\tabcolsep}{2.4pt}\\begin{tabular}{@{}lllllllll@{}}", "\\toprule",
           "orbifold & $\\ell$ & $M$ & $|\\mathcal S|$ & (C1), $\\Delta$ & (C2), $\\Delta$ & (C1), $C_*$ & (C1), $\\Sig(A,M)$ & $N$, Thm~\\ref{thm:E}\\\\",
           "\\midrule"]
    for orb, M in order:
        b = key[(orb, M, "B1")]
        d = key[(orb, M, "K")]
        e = key[(orb, M, "Kall")]
        name = tex_name(orb)
        ell = inp[orb]["systole_lower_bound"]
        out.append(f"{name} & ${ell}$ & ${M}$ & ${b['S_size']}$ & {count(b['N_C1'], b['t_C1'], b['weyl_C1'], b['N_complete'])} & "
                   f"{count(b['N_C2'], b['t_C2'], b['weyl_C2'], b['N_complete'])} & "
                   f"{count(d['N_C1'], d['t_C1'], d['weyl_C1'], d['N_complete'])} & "
                   f"{count(e['N_C1'], None, e['weyl_C1'], e['N_complete'])} & ${sci(float(b['N_thm62']), 3)}$\\\\")
    out += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    return "\n".join(out)


def table_inputs():
    rows = list({r["orbifold"]: r for r in reversed(list(csv.DictReader(open(DATA / "practice_inputs.csv"))))
                 if r["data"] == "full"}.values())[::-1]
    out = ["\\begin{table}[t]", "\\centering\\footnotesize",
           "\\caption{Inputs of the test for the ten examples: exact area, the lower bound $\\ell$ for the "
           "systole (certified in interval arithmetic), the proved diameter bound $2\\diam P$ (rounded up) and the computed diameter, the class-level count constant "
           "$C_*(A,\\ell,M)$ of Lemma~\\ref{lem:countK}, rounded up (-- where an order exceeds $M$), and the complete range: the eigenvalues $\\lambda\\le\\lambda_c$, "
           "$N_c$ of them, of the $n$ computed; for the family the trace test alone covers $\\lambda<9.8\\times10^3$, and the range above rests on the agreement of the eigenvalue counts of three discretisations.}\\label{tab:inputs}",
           "\\setlength{\\tabcolsep}{4pt}\\begin{tabular}{@{}lllllllll@{}}", "\\toprule",
           "orbifold & area & $\\ell$ & $2\\diam P$ & $\\diam$ & $C_*$, $M=3$ & $C_*$, $M=12$ & $\\lambda_c$ & $N_c$ of $n$\\\\",
           "\\midrule"]
    Kv = {(r["orbifold"], r["M"]): r["K_A_eps_M"] for r in csv.DictReader(open(DATA / "practice_inputs.csv")) if r["data"] == "full"}
    for r in rows:
        orb = r["orbifold"]
        name = tex_name(orb)
        area = "$\\pi/2$" if r["area"].startswith("0.5") else "$4\\pi/3$"
        k3 = f"${sci(float(Kv[(orb, '3')]))}$" if (orb, "3") in Kv else "--"
        k12 = f"${sci(float(Kv[(orb, '12')]))}$"
        out.append(f"{name} & {area} & ${r['systole_lower_bound']}$ & ${math.ceil(float(r['diam_B1_2diamP']) * 1000) / 1000:.3f}$ & "
                   f"${float(r['diam_true_numerical']):.3f}$ & {k3} & {k12} & "
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
           "$\\Orb(3,3,12)$, with $\\epsilon_j$, the difference between two discretisations (Section~\\ref{sec:numerical}), "
           "which for these eigenvalues is at rounding level and is not an estimate of the discretisation error; "
           "N or D marks the boundary condition on the triangle. aeb means $a\\times10^b$. These are the spectra of the companion paper, whose supplement "
           "gives their convergence data \\cite{companionA}.}\\label{tab:spectra}",
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


def table_E():
    rows = list(csv.DictReader(open(DATA / "table2.csv")))
    out = ["\\begin{table}[t]", "\\centering\\footnotesize",
           "\\caption{The constants of Theorem~\\ref{thm:E}, with $t_*=\\min(t_1,t_2,t_3)$; the last column names the binding "
           "constraint. aeb means $a\\times10^b$; $N$ is rounded up, to three significant digits, and $\\Theta_*$ and $\\delta$ down, and $C_*$, $t_1$, $t_3$ and $\\Lambda$ are rounded to the nearest unit of the last digit (Table~\\ref{tab:inputs} rounds $C_*$ up).}\\label{tab:E}",
           "\\setlength{\\tabcolsep}{3pt}\\begin{tabular}{@{}llllllllllll@{}}", "\\toprule",
           "$A$ & $\\varepsilon$ & $M$ & $k_*$ & $C_*$ & $t_1$ & $t_3$ & $\\Theta_*$ & $\\Lambda$ & $N$ & $\\delta$ & binds\\\\",
           "\\midrule"]
    area = {"pi/2": "$\\pi/2$", "4pi/3": "$4\\pi/3$", "2pi": "$2\\pi$", "10pi": "$10\\pi$"}

    def e(x, mode="near", digits=2):
        """`digits` significant digits; mode "up" for N and "down" for delta, so that the printed values remain valid"""
        x = float(x)
        ex = math.floor(math.log10(x))
        m = x / 10 ** ex
        f = 10 ** (digits - 1)
        m = math.ceil(m * f - 1e-9) / f if mode == "up" else math.floor(m * f + 1e-9) / f if mode == "down" else round(m, digits - 1)
        if m >= 10:
            m, ex = m / 10, ex + 1
        return f"${m:.{digits - 1}f}$e${ex}$"
    for r in rows:
        whole, _, frac = r["eps"].partition(".")
        eps = (whole + "." + frac[:4]).rstrip("0").rstrip(".") if frac else whole   # truncated: a lower bound
        out.append(f"{area[r['A']]} & ${eps}$ & ${r['M']}$ & ${r['kstar']}$ & {e(r['K'])} & {e(r['t1'])} & {e(r['t3'])} & "
                   f"{e(r['Gamma_star'], "down")} & {e(r['Lambda'])} & {e(r['N'], "up", 3)} & {e(r['delta'], "down")} & ${r['binds']}$\\\\")
    out += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    return "\n".join(out)


def table_certgap():
    rows = list(csv.DictReader(open(DATA / "certified_gap.csv")))
    thm = {(r["A"], r["eps"], r["M"]): r for r in csv.DictReader(open(DATA / "computed_gap.csv"))}
    omis = {(r["A"], r["eps"], r["M"]): r for r in csv.DictReader(open(DATA / "certified_gap_omissions.csv"))}
    out = ["\\begin{table}[t]", "\\centering\\footnotesize",
           "\\caption{Proposition~\\ref{prop:certgap}: at the time $t$, every gap $|G_\\sigma(t)-G_{\\sigma'}(t)|$ over "
           "$\\Sig(A,M)$ is at least $\\Theta$, certified in ball arithmetic, and the first $N$ eigenvalues, each known to "
           "within $\\delta$, with none omitted, determine the signature in $\\Cl(A,\\varepsilon,M)$; one wrong entry is "
           "tolerated above $\\Lambda_o=t^{-1}\\log(8/\\Theta)$ (Remark~\\ref{rem:omissions}; rounded up), and the last column is the $N$ of "
           "Theorem~\\ref{thm:E} for the same class, rounded up. aeb means $a\\times10^b$.}\\label{tab:certgap}",
           "\\setlength{\\tabcolsep}{3.5pt}\\begin{tabular}{@{}llllllllll@{}}", "\\toprule",
           "$A$ & $\\varepsilon$ & $M$ & $|\\Sig(A,M)|$ & $t$ & $\\Theta$ & $N$ & $\\delta$ & $\\Lambda_o$ & $N$, Thm~\\ref{thm:E}\\\\",
           "\\midrule"]
    area = {"pi/2": "$\\pi/2$", "4pi/3": "$4\\pi/3$", "2pi": "$2\\pi$", "10pi": "$10\\pi$"}

    def e(x):
        m, ex = f"{float(x):.2e}".split("e")
        return f"${m}$e${int(ex)}$"
    for r in rows:
        n62 = thm[(r["A"], r["eps"], r["M"])]["N_thm62"]
        o = omis[(r["A"], r["eps"], r["M"])]
        assert o["t"] == r["t"] and o["certified_gap_lower"] == r["certified_gap_lower"]
        lo = float(o["Lambda_o_upper"])
        lo_txt = f"${lo:.0f}$" if lo >= 100 else f"${o['Lambda_o_upper']}$"
        assert float(lo_txt.strip("$")) >= lo                       # printed value is still an upper bound
        out.append(f"{area[r['A']]} & ${r['eps']}$ & ${r['M']}$ & ${r['Sig_size']}$ & ${r['t']}$ & ${r['certified_gap_lower']}$ & "
                   f"${r['N']}$ & {e(r['delta'])} & {lo_txt} & ${sci(float(n62), 3)}$\\\\")
    out += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    return "\n".join(out)


def table_certdetail():
    rows = list(csv.DictReader(open(DATA / "certified_gap_detail.csv")))
    out = ["\\begin{table}[t]", "\\centering\\footnotesize",
           "\\caption{The certificate of Proposition~\\ref{prop:certgap}, one row per class of Table~\\ref{tab:certgap}: "
           "the pair $\\sigma,\\sigma'$ of signatures with the least certified gap at the time $t$ of that table, a lower "
           "bound for that gap, and the bounds, decided in ball arithmetic, for the three inequalities of "
           "Corollary~\\ref{cor:computedgap}. Lower bounds are decimals strictly below the certified values and upper bounds "
           "strictly above them, so that in the first and third rows, where $\\Theta/8$ is exactly $0.001985$ and $0.019$, "
           "the column $\\Theta/8$ shows $0.001984$ and $0.01899$. Appendix~\\ref{app:certificate} lists the enclosures "
           "from which every gap can be checked by hand.}\\label{tab:certdetail}",
           "\\setlength{\\tabcolsep}{4pt}\\begin{tabular}{@{}lllllllll@{}}", "\\toprule",
           "$A$ & $\\varepsilon$ & $M$ & $\\sigma$ & $\\sigma'$ & gap $\\ge$ & $B_*(t)\\le$ & $\\Theta/8\\ge$ & $\\Lambda t\\ge$\\\\",
           "\\midrule"]
    area = {"pi/2": "$\\pi/2$", "4pi/3": "$4\\pi/3$", "2pi": "$2\\pi$", "10pi": "$10\\pi$"}

    def sig(s):
        g, rest = s.strip("()").split(";")
        orders = rest.split(",")
        parts, i = [], 0
        while i < len(orders):
            j = i
            while j < len(orders) and orders[j] == orders[i]:
                j += 1
            parts.append(orders[i] if j - i == 1 else f"{orders[i]}^{j - i}")
            i = j
        return f"$({g};{','.join(parts)})$"
    for r in rows:
        out.append(f"{area[r['A']]} & ${r['eps']}$ & ${r['M']}$ & {sig(r['sigma'])} & {sig(r['sigma_prime'])} & "
                   f"${r['least_gap_lower']}$ & ${r['Bstar_upper']}$ & ${r['Theta_over_8_lower']}$ & ${r['Lambda_t_lower']}$\\\\")
    out += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    return "\n".join(out)


def table_certencl():
    """Round 10 (B5): the enclosures of I_1(t) and E_m(t) behind Proposition 6.6, one column per class."""
    rows = list(csv.DictReader(open(DATA / "certified_gap_enclosures.csv")))
    classes = list(dict.fromkeys((r["A"], r["eps"], r["M"], r["t"]) for r in rows))
    val = {(r["A"], r["eps"], r["M"], r["t"], r["quantity"], r["m"]): r for r in rows}
    area = {"pi/2": "$\\pi/2$", "4pi/3": "$4\\pi/3$", "2pi": "$2\\pi$"}
    for r in rows:   # every printed decimal is within one unit of its last digit of the exact value (asserted upstream)
        d = r["printed"].lstrip("-").replace(".", "").lstrip("0")
        assert len(d) <= 10 and float(r["error_less_than"]) <= 10 ** (math.floor(math.log10(abs(float(r["printed"])))) - 9) * 1.000001
    Mmax = max(int(c[2]) for c in classes)
    ncol = len(classes)
    out = ["\\begin{table}[h]", "\\centering\\scriptsize",
           "\\caption{The enclosures behind Proposition~\\ref{prop:certgap}, one column per class of Table~\\ref{tab:certgap}: "
           "$\\mathrm I_1(t)=\\frac{4\\pi}{\\Area}\\mathrm I(t)$ and $\\mathrm E_m(t)$, $2\\le m\\le M$, at the time $t$ of that table. "
           "Each entry differs from the exact value by less than one unit of its last digit (the balls computed have radii below "
           "$10^{-34}$), and $G_\\sigma(t)=\\frac{s(\\sigma)}2\\mathrm I_1(t)+\\sum_i\\mathrm E_{m_i}(t)$, $s(\\sigma)=\\Area/2\\pi$; "
           "\\texttt{certified\\_gap.py} asserts that these decimals alone give every pairwise gap at least $\\Theta$.}\\label{tab:certencl}",
           f"\\setlength{{\\tabcolsep}}{{2pt}}\\begin{{tabular}}{{@{{}}l{'r' * ncol}@{{}}}}", "\\toprule",
           "$A$ & " + " & ".join(area[c[0]] for c in classes) + "\\\\",
           "$\\varepsilon$ & " + " & ".join(f"${c[1]}$" for c in classes) + "\\\\",
           "$M$ & " + " & ".join(f"${c[2]}$" for c in classes) + "\\\\",
           "$t$ & " + " & ".join(f"${c[3]}$" for c in classes) + "\\\\", "\\midrule"]
    out.append("$\\mathrm I_1(t)$ & " + " & ".join(f"${val[c + ('I1', '')]['printed']}$" for c in classes) + "\\\\")
    for m in range(2, Mmax + 1):
        cells = [f"${val[c + ('E', str(m))]['printed']}$" if c + ("E", str(m)) in val else "" for c in classes]
        out.append(f"$\\mathrm E_{{{m}}}(t)$ & " + " & ".join(cells) + "\\\\")
    assert max(float(r["radius_upper"]) for r in rows) < 1e-34
    out += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    return "\n".join(out)


TABLES = {"inputs": table_inputs, "practice": table_practice, "spectra": table_spectra, "E": table_E, "certgap": table_certgap,
          "certdetail": table_certdetail, "certencl": table_certencl}


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
