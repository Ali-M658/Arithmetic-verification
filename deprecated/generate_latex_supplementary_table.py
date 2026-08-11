#!/usr/bin/env python3
"""
Builds Table 2 (tab:density) - area, e1/e2 invariants and the quadratic
characteristic polynomial for a handful of sample pillow triples.
"""
from fractions import Fraction


def compute_pillow_data(triples):
    table_data = []
    for (a, b, c) in triples:
        area_frac = Fraction(1, 1) - (Fraction(1, a) + Fraction(1, b) + Fraction(1, c))

        # x^2 - e1*x + e2
        e1 = Fraction(1, a * a) + Fraction(1, b * b) + Fraction(1, c * c)
        e2 = Fraction(1, (a * b * c) ** 2)

        table_data.append({'triple': (a, b, c), 'area': area_frac, 'e1': e1, 'e2': e2})
    return table_data


def generate_table2_latex():
    sample_triples = [
        (2, 3, 7),
        (2, 3, 8),
        (2, 4, 5),
        (3, 3, 4),
        (3, 4, 4),
        (2, 5, 5),
    ]

    data = compute_pillow_data(sample_triples)

    print("% Table 2: spectral density (tab:density)")
    print("\\begin{table}[h!]")
    print("\\centering")
    print("\\begin{tabular}{ccccc}")
    print("\\toprule")
    print("Triple $(a, b, c)$ & Area $/ \\pi$ & Invariant $e_1$ & Invariant $e_2$ & Characteristic Poly $P(x)$ \\\\")
    print("\\midrule")

    for row in data:
        a, b, c = row['triple']
        ar, e1, e2 = row['area'], row['e1'], row['e2']
        poly_str = f"x^2 - \\frac{{{e1.numerator}}}{{{e1.denominator}}}x + \\frac{{{e2.numerator}}}{{{e2.denominator}}}"
        print(f"({a}, {b}, {c}) & $\\frac{{{ar.numerator}}}{{{ar.denominator}}}$ & $\\frac{{{e1.numerator}}}{{{e1.denominator}}}$ & $\\frac{{{e2.numerator}}}{{{e2.denominator}}}$ & ${poly_str}$ \\\\")

    print("\\bottomrule")
    print("\\end{tabular}")
    print("\\caption{Spectral invariants and exact Newton characteristic polynomials for selected hyperbolic triangular pillows.}")
    print("\\label{tab:density}")
    print("\\end{table}")


if __name__ == "__main__":
    generate_table2_latex()
