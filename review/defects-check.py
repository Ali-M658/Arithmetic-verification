#!/usr/bin/env python3
"""Machine checks for the facts and line numbers cited in review/DEFECTS.md.

Everything here is recomputed from paper/main.tex, the vault note and the
enumerator below; nothing is read from the earlier review files except the
Takeuchi class table, which is checked against the vault note as a set.
The enumerator is written from scratch (no import from code/) so that it
shares no logic with the harness in code/.

Run from the repository root:  python3 review/defects-check.py
Exit status is nonzero if any assertion fails.
"""
import hashlib
import re
from collections import defaultdict
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEX = (ROOT / "paper" / "main.tex").read_text()
LINES = TEX.split("\n")


def line(n):
    return LINES[n - 1]


# ---------------------------------------------------------------- manuscript
assert hashlib.md5(TEX.encode()).hexdigest() == "adfa0001c73e3721f3ccdcc6dcda7e12", \
    "paper/main.tex changed: every line number in DEFECTS.md must be re-derived"
assert len(LINES) == 723 or len(LINES) == 724  # trailing newline tolerance

# Location anchors used in DEFECTS.md: (line, required substring)
ANCHORS = [
    (1, r"\documentclass[12pt, letterpaper]{article}"),
    (17, r"\hyphenpenalty=10000"),
    (48, r"\vspace{-2cm}"),
    (58, "0.0085$--$0.0093$"),
    (58, "All numerical assertions are verified in exact rational arithmetic"),
    (103, "denotes the least number of leading heat coefficients"),
    (114, "up to isometry"),
    (134, "Dryden--Strohmaier"),
    (146, r"\subsection{Locating the novelty}"),
    (151, r"(a) Prior art"),
    (153, "To our knowledge this is the first exact finite-coefficient"),
    (229, r"\begin{remark}\label{rem:bugfix}"),
    (236, r"p_\ell(m)"),
    (404, ""),  # start of the N(S) definition region (text checked below)
    (440, "the full data and generating script are in the public repository"),
    (445, r"\label{tab:density}"),
    (461, "stabilizes to within about"),
    (465, "standard in analogous Diophantine settings"),
    (487, r"\emph{Stability of the recovery.}"),
    (493, r"\begin{remark}[Larger cone counts]\label{rem:ncone}"),
    (494, r"the upper bound $K\le n$ extends the $n=3$ case of Theorem"),
    (502, r"A single command (\texttt{run\_all}) reproduces all checks."),
    (507, r"\begin{longtable}"),
    (618, "The author declares no competing interests"),
    (624, "Verification scripts and generated table data are available"),
    (627, "regenerate Tables"),
]
for n, sub in ANCHORS:
    assert sub in line(n), f"main.tex:{n} no longer contains {sub!r}"

# bibitem line numbers
BIB = {
    "kac1966": 633, "mckeansinger1967": 636, "datchevhezari2013": 639,
    "griesermaronna2013": 642, "lurowlett2015": 645, "gomezserrano2020": 648,
    "hezarizelditch2022": 651, "sunada1985": 655, "gww1992": 658,
    "donnelly1976": 662, "dggw2008": 665, "ssw2006": 668, "rsw2008": 671,
    "proctorstanhope2009": 674, "barihunsicker2017": 677,
    "richardsonstanhope2019": 680, "gittinsetal2024": 683, "schueth2019": 687,
    "schueth2025": 690, "suleymanova2017": 693, "nrs2024": 696,
    "looisher2025": 699, "doylerossetti2008": 703, "drydenstrohmaier2009": 706,
    "harmer2008": 709, "ucar2017": 712, "scott1983": 715, "buser1992": 718,
}
for key, n in BIB.items():
    assert line(n).strip() == "\\bibitem{%s}" % key, (key, n, line(n))
assert len(re.findall(r"\\bibitem\{", TEX)) == len(BIB) == 28

# em-dash corruption: ' ,  ' inline plus trailing ' , ' in bibliography comments
inline = [i + 1 for i, l in enumerate(LINES) if " ,  " in l and not l.rstrip().endswith(" ,")]
trailing = [i + 1 for i, l in enumerate(LINES) if l.rstrip().endswith(" , ") or l.endswith(" , ")]
n_inline = sum(l.count(" ,  ") for l in LINES)
all_lines = [i + 1 for i, l in enumerate(LINES) if " ,  " in l or l.endswith(" , ")]
print(f"em-dash artefacts: {n_inline} ' ,  ' occurrences + {len(trailing)} trailing ' , '; "
      f"{len(all_lines)} distinct lines")
assert n_inline == 48 and len(trailing) == 5 and len(all_lines) == 25
assert "—" not in TEX, "a real em-dash exists; hygiene report claims none"
assert line(58).count(" ,  ") == 5

# the n-cone remark and the two tables compile as Remark 5.1 / Table 1 / Table 2
# (checked from paper-compile aux by hand: rem:ncone = 5.1, tab:density = 1,
# tab:enum = 2); here we only assert the source order that forces it.
assert TEX.index(r"\label{tab:density}") < TEX.index(r"\label{tab:enum}")
assert TEX.index("{definition}{Definition}[section]") < TEX.index(r"\label{rem:ncone}")
sec5 = TEX[TEX.index(r"\section{Asymptotic Density"):TEX.index(r"\section{Data availability")]
assert r"\begin{definition}" not in sec5 and sec5.count(r"\begin{remark}") == 1

# ------------------------------------------------------------ the enumeration
# Fresh enumerator: hyperbolic triads p<=q<=r, p>=2, 1/p+1/q+1/r<1 (manuscript l.99).
cum_pairs = cum_classes = 0
first_triple_class = None
checkpoint = {}
for S in range(10, 601):
    groups = defaultdict(list)
    for p in range(2, S // 3 + 1):
        for q in range(p, (S - p) // 2 + 1):
            r = S - p - q
            if r < q:
                continue
            R = F(1, p) + F(1, q) + F(1, r)
            if R < 1:
                groups[R].append((p, q, r))
    cum_pairs += sum(len(v) * (len(v) - 1) // 2 for v in groups.values())
    cum_classes += sum(1 for v in groups.values() if len(v) > 1)
    if first_triple_class is None:
        for R, v in groups.items():
            if len(v) >= 3:
                first_triple_class = (S, R, v)
                break
    checkpoint[S] = (cum_pairs, cum_classes)
    if S == 18:
        assert groups[F(3, 4)] == [(2, 8, 8), (3, 3, 12)] or \
            sorted(groups[F(3, 4)]) == [(2, 8, 8), (3, 3, 12)]

# Table printed at main.tex:449-456 (compiled as Table 1)
PRINTED = {18: (1, 0.0031), 100: (92, 0.0092), 200: (386, 0.0097),
           300: (840, 0.0093), 400: (1496, 0.0094), 500: (2210, 0.0088),
           600: (3067, 0.0085)}
for S, (N, ratio) in PRINTED.items():
    assert checkpoint[S][0] == N, (S, checkpoint[S])
    assert round(N / S**2, 4) == ratio, (S, N / S**2)
    assert f"{N}" in TEX and f"{ratio:.4f}" in TEX

# first fibre of size 3 is at S = 136, R = 1/10
assert first_triple_class[0] == 136 and first_triple_class[1] == F(1, 10)
assert first_triple_class[2] == [(15, 55, 66), (16, 40, 80), (17, 34, 85)]
# pair and class counts first differ at S = 136
first_div = min(S for S in checkpoint if checkpoint[S][0] != checkpoint[S][1])
assert first_div == 136 and checkpoint[135][0] == checkpoint[135][1] == 161
assert checkpoint[136] == (168, 166)
assert checkpoint[600] == (3067, 2977)

# abstract range (0.0085-0.0093) vs the printed table and the full sweep
ratios = {S: checkpoint[S][0] / S**2 for S in range(100, 601)}
tab = [PRINTED[S][1] for S in (100, 200, 300, 400, 500, 600)]
assert min(tab) == 0.0085 and max(tab) == 0.0097
assert max(tab) > 0.0093, "abstract band 0.0085-0.0093 excludes printed values"
assert [PRINTED[S][1] for S in (200, 400)] == [0.0097, 0.0094]  # outside the band
assert round(max(ratios.values()), 5) == 0.00979 and max(ratios, key=ratios.get) == 196
assert round(min(ratios.values()), 5) == 0.00851 and min(ratios, key=ratios.get) == 599
# The ratio is NOT monotone at the printed checkpoints (0.0093 at 300, 0.0094 at 400),
# so 'decreasing' is only a statement about the trend: peak 0.00979 at S=196, a
# negative least-squares slope on 200<=S<=600, and a last 100-block mean below
# each of the four earlier blocks.
assert PRINTED[400][1] > PRINTED[300][1] and PRINTED[200][1] > PRINTED[100][1]
xs = list(range(200, 601))
mx = sum(xs) / len(xs)
my = sum(ratios[s] for s in xs) / len(xs)
slope = sum((s - mx) * (ratios[s] - my) for s in xs) / sum((s - mx) ** 2 for s in xs)
assert slope < 0 and abs(slope + 1.75e-6) < 5e-8, slope
blocks = [sum(ratios[s] for s in range(a, a + 101)) / 101 for a in (100, 200, 300, 400, 500)]
assert blocks[4] == min(blocks) and blocks[4] < 0.0087 < min(blocks[:4])
print("N(S)/S^2: range over 100<=S<=600 = [%.5f, %.5f]; printed checkpoints %s"
      % (min(ratios.values()), max(ratios.values()), tab))

# ----------------------------------------------------- Takeuchi: both arithmetic
note = (ROOT / "research" / "notes" /
        "takeuchi-1977-arithmetic-triangle-groups-theorem-3-full-list-verbatim-85-triples.md").read_text()
sect = note[note.index("(i) Compact types"):note.index("(ii)", note.index("(i) Compact types"))]
compact = {tuple(map(int, m)) for m in re.findall(r"\((\d+),\s*(\d+),\s*(\d+)\)", sect)}
assert len(compact) == 76 and (2, 8, 8) in compact and (3, 3, 12) in compact
assert (2, 3, 16) in compact
verdict = (ROOT / "review" / "takeuchi-verdict.md").read_text()
cls = {}
for roman, body in re.findall(
        r"^\| (?:\*\*)?(II|III|IV|V|VI|VII|VIII|IX|X|XI|XII|XIII|XIV|XV|XVI|XVII|XVIII|XIX)(?:\*\*)? \| (.*?) \| \d+ \|$",
        verdict, re.M):
    for m in re.findall(r"\((\d+),\s*(\d+),\s*(\d+)\)", body):
        cls[tuple(map(int, m))] = roman
assert set(cls) == compact, "class table and vault note disagree"
assert cls[(2, 8, 8)] == "III" and cls[(3, 3, 12)] == "XV"

print("defects-check: all assertions passed")
