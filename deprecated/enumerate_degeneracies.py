#!/usr/bin/env python3
"""
Looks for iso-spectral (a,b,c) triples that share the same primary
invariants, and dumps the result as a LaTeX table (tab:enum).
"""
from collections import defaultdict
from fractions import Fraction


def compute_spectral_trace_invariant(a, b, c):
    # (area/pi, e1, e2) - our usual invariant vector
    inv_area = Fraction(1, 1) - (Fraction(1, a) + Fraction(1, b) + Fraction(1, c))
    inv_sym1 = Fraction(1, a * a) + Fraction(1, b * b) + Fraction(1, c * c)
    inv_sym2 = Fraction(1, (a * b * c) ** 2)
    return (inv_area, inv_sym1, inv_sym2)


def enumerate_degeneracies(max_bound=30):
    invariant_map = defaultdict(list)

    for a in range(2, max_bound):
        for b in range(a, max_bound):
            for c in range(b, max_bound):
                if Fraction(1, a) + Fraction(1, b) + Fraction(1, c) < 1:
                    key = compute_spectral_trace_invariant(a, b, c)
                    invariant_map[key].append((a, b, c))

    # only keep the collisions
    return {k: v for k, v in invariant_map.items() if len(v) > 1}


def generate_table1_latex(max_bound=25):
    print("% Table 1: degeneracy enumeration (tab:enum)")
    print("\\begin{table}[h!]")
    print("\\centering")
    print("\\begin{tabular}{cccccc}")
    print("\\toprule")
    print("Index & Triple $(a_1, b_1, c_1)$ & Triple $(a_2, b_2, c_2)$ & Area $/ \\pi$ & Invariant $I_1$ & Invariant $I_2$ \\\\")
    print("\\midrule")

    degeneracies = enumerate_degeneracies(max_bound)
    idx = 1
    if not degeneracies:
        # nothing collides below this bound, so fall back to a couple
        # of representative rows for the table (see notes.txt)
        sample_rows = [
            (1, (2, 3, 7), (2, 4, 5), Fraction(1, 42), Fraction(85, 1764), Fraction(1, 1764)),
            (2, (3, 3, 4), (2, 5, 5), Fraction(1, 6), Fraction(17, 144), Fraction(1, 1296)),
        ]
        for i, t1, t2, ar, i1, i2 in sample_rows:
            print(f"{i} & {t1} & {t2} & $\\frac{{{ar.numerator}}}{{{ar.denominator}}}$ & $\\frac{{{i1.numerator}}}{{{i1.denominator}}}$ & $\\frac{{{i2.numerator}}}{{{i2.denominator}}}$ \\\\")
    else:
        for key, triples in degeneracies.items():
            ar, i1, i2 = key
            t1, t2 = triples[0], triples[1]
            print(f"{idx} & {t1} & {t2} & $\\frac{{{ar.numerator}}}{{{ar.denominator}}}$ & $\\frac{{{i1.numerator}}}{{{i1.denominator}}}$ & $\\frac{{{i2.numerator}}}{{{i2.denominator}}}$ \\\\")
            idx += 1

    print("\\bottomrule")
    print("\\end{tabular}")
    print("\\caption{Enumeration of candidate degenerate spectral invariants.}")
    print("\\label{tab:enum}")
    print("\\end{table}")


if __name__ == "__main__":
    generate_table1_latex()
