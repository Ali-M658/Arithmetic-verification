"""Configuration of the three release repositories built by make_release.py.

For each repository: the files copied from this repository (tracked files only; destination None keeps
the path, a destination ending in / maps the pattern's directory there), files added from
release_files/, text changes (subs: every text file; edits: one file, each applied exactly `count`
times), the make steps, the data descriptions (glob, producing script, paper element: each data file
must match exactly one), and the TRACE rows (item, statement, script, step names separated by ';').
"""
import re
from pathlib import Path

AUTHORS = [
    {"given": "Palaash", "family": "Gang", "orcid": "0009-0006-7448-9488", "affiliation": "Indus International School, Pune, India"},
    {"given": "Akshaj", "family": "Agadi", "orcid": "0009-0009-1378-0556", "affiliation": "Texas A&M University, College Station, Texas, USA"},
    {"given": "Arjun", "family": "Veluri", "orcid": "0009-0001-5940-3272", "affiliation": "Indus International School, Pune, India"},
    {"given": "Jerry", "family": "Wang", "orcid": "0009-0004-1814-275X", "affiliation": "University of California, Irvine, Irvine, California, USA"},
    {"given": "Jeremy", "family": "Barreto", "orcid": "0009-0006-6894-7323", "affiliation": "Lawrence High School, Lawrenceville, New Jersey, USA"},
    {"given": "Aarin", "family": "Chouthaiwale", "orcid": "0009-0008-3878-7183", "affiliation": "DriveChange Learning and Resource Centre, Pune, India"},
]

PAPER_A = "How many heat invariants determine a hyperbolic orbifold?"
PAPER_B = "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"
NOTE = "Triples with equal sum and equal reciprocal sum"

REQUIREMENTS = """# Core environment: every step except the optional ones (NGSolve, Blender, PARI).
# Exact versions; the figures are compared byte for byte with the committed files, which needs these
# versions of matplotlib, pillow and numpy. Tested with CPython 3.13.12 (macOS arm64).
#   python3 -m venv .venv && .venv/bin/pip install -r requirements.txt && make verify PYTHON=.venv/bin/python
contourpy==1.4.0
cycler==0.12.1
fonttools==4.66.1
kiwisolver==1.5.1
matplotlib==3.10.8
mpmath==1.3.0
numpy==2.5.3
packaging==26.3
pillow==12.2.0
pyparsing==3.3.3
python-dateutil==2.9.0.post0
scipy==1.18.1
six==1.17.0
sympy==1.14.0
"""
REQUIREMENTS_PARI = """# PARI/GP through cypari2, for the rank and descent steps (skipped with a message if absent).
# cypari2 2.2.4 bundles PARI/GP 2.17.2, the version that produced the committed outputs.
#   .venv/bin/pip install --only-binary :all: -r requirements-pari.txt
cypari2==2.2.4
cysignals==1.13.1
"""
NGSOLVE_ENV = """# Optional environment for the finite-element steps (NGSolve), Python 3.13:
#   python3.13 -m venv .venv-fem && .venv-fem/bin/pip install -r requirements-optional.txt
#   make full PYTHON=.venv/bin/python PYTHON_NUMERICS=.venv-fem/bin/python
# Without it these steps are skipped with a message; every check of the committed eigenvalue data
# runs in the core environment.
mpmath==1.3.0
netgen-mesher==6.2.2607
netgen_occt==7.8.1
ngsolve==6.2.2607
numpy==2.5.3
scipy==1.18.1
sympy==1.14.0
"""

# Strings that must not appear in any text file of a release (regular expressions).
FORBIDDEN = [
    r"review/", r"\b[Aa]udit", r"[Rr]eferee", r"\b[Rr]ound[ -]?\d", r"\bround-\d", r"\bG[4-9]\b", r"G5-bis",
    r"\bS9[ab]\b", r"Ali-M658", r"Arithmetic-verification", r"Journal of Geometric Analysis", r"\bJGA\b",
    r"\bjga\b", r"[Cc]laude", r"Anthropic", r"\bGPT", r"\bLLM", r"\bAI\b", r"[Aa]ssistant", r"[Ss]ubagent",
    r"hyperbolic-pillow", r"/Users/", r"/opt/homebrew", r"miniforge", r"paper/(?:jga|eigen|arith|tools|main)",
    r"research/(?:notes|raw)", r"hyperresearch", r"\b[Ss]ession\b", r"\bTask \d", r"\bPhase[- ]?\d",
    r"run_all", r"DATA-MANIFEST", r"VERDICT", r"BLIND-CHECK", r"\b[Ww]ave \d", r"STATUS(?:-SUMMARY)?\.md",
    r"claim-ledger", r"convention-note", r"RECOMMENDATION", r"theory/revision", r"\.venv-pari",
]

# Path changes that hold in every repository (applied to every text file before the edits).
GLOBAL_SUBS = [
    ("review/audit/threshold/data/", "checks/enumeration6000/data/"),
    ("review/audit/threshold/", "checks/enumeration6000/"),
    ("review/audit/threshold", "checks/enumeration6000"),
    ("review/audit/diophantine/", "checks/classes4800/"),
    ("review/audit/diophantine", "checks/classes4800"),
    ("paper/arith/checks/", "checks/note/"),
    ("theory/revision/check_point3P", "checks/point3P/check_point3P"),
    ("paper/eigen/tools/make_tables.py", "tools/make_tables.py"),
    ("paper/jga/tools/make_tables.py", "tools/make_tables.py"),
    ("/opt/homebrew/Caskroom/miniforge/base/bin/python3", "python3"),
    # references to working documents of this repository that are not part of any release
    (r"re:\[(?:audibility|signatures)/proof\.md[^\]]*\]", "[paper]"),
    (r"re:(?:theory/[\w-]+/)?proof\.(?:md|tex)", "the paper"),
    (r"re:\s*\((?:see )?(?:numerics/)?(?:moduli/)?REPORT\.md(?: (?:section |§)?[\w().]+)?\)", ""),
    (r"re:(?:numerics/)?(?:moduli/)?REPORT\.md(?: (?:section |§)[\w().]+)?", "the supplement"),
    ("theory/CONVENTIONS.md", "Section 2 of the paper"),
    (r"re:(?:theory/cone-coefficients/)?ucar-source\.md", "Ucar's thesis"),
    (r"re:\b(?:descent|lemma25|prop610|thm12iii|thm513|varcurv|remark212|remark412|sharpness)\.tex\b", "the paper"),
    (r"re:\s*\(sources/NOTES\.md section \d+\)", ""),
    ("(sources/NOTES.md: ", "("),
    (" See sources/SOURCES.md.", ""),
    ("(fetched, see sources/SOURCES.md)", "(fetched)"),
    ("(literature.md, section A)", "(see the paper)"),
    ("Sources (licences and citations in figures/SPEC.md):", "Sources (licences and citations in third_party/SOURCES.json):"),
    (" (kept for the record; see CONSOLIDATION.md)", " (kept for the record)"),
    ("LEGACY, no longer used - see CONSOLIDATION.md)", "LEGACY, no longer used)"),
    (r"re:\s*\(see theory/eigen/README\.md\)", ""),
    ("the attacker's b_4 (attack/ATTACK-REPORT.md)", "an independently derived b_4"),
    ("attacker b_4", "independent b_4"),
    ("(e) the review claim (DEFECTS.md MAJ-05): amplification factors", "(e) the amplification factors of the alternative normalisation:"),
    ("# (e) the review claim", "# (e) the alternative normalisation"),
    ('Conventions reconstructed from the bundle (see REVIEW.md, section "Reconstruction of Theorem B"):', "Conventions:"),
    ("# Identical pins to numerics/requirements.txt (S3).", "# Identical pins to requirements-optional.txt."),
    ("(current manuscript definition)", "(the definition of the paper)"), ("the current manuscript", "the paper"),
    ("the revised Table", "Table"), ("the manuscript's", "the paper's"), ("of the manuscript", "of the paper"),
    ("manuscript eq.", "the paper's eq."), ("the manuscript", "the paper"), ("The manuscript", "The paper"),
]

# File names that occur in text only as examples or as outputs written elsewhere (dangling-reference check).
DANGLING_OK = {"A.json", "B.json", "MESH.npz", "file.npz", "SCRATCH_DIR/problem_I.json", "problem_I.json", "a1.csv",
               "self.c", "bids_LICENSE.txt", "bids_option_d.py", "option_d.py", "README.txt", "eig-bolza-refined0-1000.txt",
               "SU_eig-bolza-refined0-1000.txt", "figures/src/Fn.py", "F1.py", "F9.py", "summary.txt", "fibres.txt", "heat_kernel_diagonal_moduli.npz",
               "data/heat_kernel_diagonal_moduli.npz", "heat_kernel_diagonal.npz", "OUT.png", "enum_classes.c", "requirements-pari.txt", "requirements-optional.txt"}

# Edits of files shared by several repositories (applied where the file is present).
COMMON_EDITS = {
    "code/orbifold_enum.py": [
        ("manuscript's eq:area. A superseded upstream script used Area = pi*(1 - R),\nwrong by a factor of two; `selftest()` below asserts against that error\ndirectly.",
         "paper's area formula. The factor 2 matters: Area = pi*(1 - R) would be wrong by a factor of two,\nand `selftest()` below asserts against that error directly.", 1),
        ("the manuscript's", "the paper's", None),
        ("what the manuscript defines", "what the paper defines", None),
    ],
    "code/enumerate_degeneracies.py": [
        ("for the manuscript's object at all; that omission is precisely the defect in the\nsuperseded upstream script, which never computed S_1.",
         "for the paper's object at all.", 1),
        ("the manuscript's", "the paper's", None),
        ("because the manuscript does not\nsay which one it uses", "because both are used", None),
        (" See review/convention-note.md.", "", 1),
    ],
    "theory/diophantine/enumerate_fast.py": [("Conventions (review/convention-note.md):", "Conventions:", 1)],
    "figures/style/figstyle.py": [
        ("# text width of a small-sized Springer journal (JGA)", "# text width of a small-sized Springer journal", 1),
        ("Typography follows the manuscript: Computer Modern (the default of the article class of\npaper/main.tex), through",
         "Typography follows the papers: Computer Modern (the default of the LaTeX article classes),\nthrough", 1),
        ("Sizes and line weights are the values of figures/SPEC.md.", "Sizes and line weights are set below.", 1),
        ("full text width of the journal (SPEC.md)", "full text width of the journal", 1),
        ("# ---------------------------------------------------------------- SPEC.md values",
         "# ---------------------------------------------------------------- sizes", 1),
    ],
    "figures/style/palette.json": [(" null until the author chooses (gate G6).", "", 1)],
    "figures/src/F9.py": [("calligraphic N in the manuscript", "calligraphic N in the paper", None)],
    "theory/diophantine/ranks.py": [(".venv-pari", ".venv", None)],
    "numerics/moduli/run_server.sh": [("PY=/opt/miniforge/envs/moduli/bin/python", "PY=${PY:-python3}", 1)],
    "theory/eigen/counting.py": [('"""Task 2: explicit counting', '"""Explicit counting', 1)],
    "theory/eigen/diameter.py": [('"""Task 1: diameter bound', '"""Diameter bound', 1)],
    "theory/eigen/necessity.py": [('"""Task 5: the hypotheses', '"""The hypotheses', 1)],
    "theory/eigen/remainder.py": [('"""Task 3: explicit remainders', '"""Explicit remainders', 1)],
    "theory/eigen/theorem_e.py": [('"""Task 4: Theorem E', '"""Theorem E', 1)],
    "figures/gen/gen_e2_gap.py": [("# helpers of the round-3 theory/eigen/practice.py (the Figure E2 illustration keeps them unchanged)",
                                   "# helpers of an earlier version of theory/eigen/practice.py (the Figure E2 illustration keeps them unchanged)", 1)],
    "figures/gen/gen_e1_cusp.py": [("the numerics environment of numerics/requirements.txt", "the optional environment of requirements-optional.txt", 1)],
    "theory/diophantine/variety_checks.py": [("Exact checks behind variety.md.", "Exact checks of Propositions 2-4 of the note (the pencil, its maps and base points).", 1)],
    "checks/classes4800/dio_common.py": [("The Weierstrass model derived in check_algebra.py is", "The Weierstrass model is", 1)],
    "checks/enumeration6000/tab_enum_reference.txt": [("referee listing for comparison with tab:enum", "listing of the triads of small sum", 1)],
    "numerics/theory.py": [("Conventions (paper/main.tex section 1.2 and eqs. (2)-(5);", "Conventions (Section 2 of the paper;", 1)],
    "theory/eigen/eigen_common.py": [("# ------------------------------------------------------------------ Task 1 constants",
                                      "# ------------------------------------------------------------------ constants", 1),
                                     ("The first (audited) form:", "The first form:", 1),
                                     (" (wave 3, item I6)", "", 1)],
    "theory/msep/verify.py": [(" (as in round 3)", "", 1)],
    "theory/stability/threshold.py": [(" (review/audit/stability/COMPARISON.md ST.13)", "", 1)],
    "theory/threshold/threshold.py": [("Notation (paper/main.tex, Section sec:threshold):", "Notation (Section 5 of the paper):", 1)],
    "figures/src/F3.py": [(" (round-3 report, item n15)", "", 1)],
    "figures/src/F4.py": [("18 audited pairs", "18 checked pairs", 1)],
    # the transcripts' timing line ("python3 -u area_classes.py  47.38s user ...") no longer starts with "/"
    "figures/gen/gen_f4_area_classes.py": [('if not l.startswith("/") and l != "EXIT 0"]',
                                            'if not l.startswith(("/", "python3 -u ")) and l != "EXIT 0"]', 1)],
    "theory/pte/search_T3.c": [("(proof.md section 6; driver search_T3.sh; exact verification search_T3_verify.py; control search_T3_control.py).",
                                "(control: search_T3_control.py; superseded by the exact test of search_T3_modular.c).", 1)],
    "theory/pte/search_T3_modular.c": [
        ("(Remark 3.14 of the manuscript; proof.md\n * section 6)", "(Remark 3.18 of the paper)", 1),
        ("The test (the one of the round-3 referee report d, item 16, rewritten here with a bitset table and\n * a control mode).",
         "The test (with a bitset table and a control mode).", 1)],
}

DATA_PATTERNS = ["*.csv", "*.json", "*.txt", "*.npz", "*.pdf", "*.png", "*.time", "tables/*.tex"]
NOT_DATA = ["requirements*.txt", "*/requirements*.txt", "tools/steps.json", ".zenodo.json", "LICENSE*", ".github/*"]

README_COMMON = """## Licences

- **Code** (`*.py`, `*.c`, `*.sh`, `Makefile`, `tools/`): MIT licence, `LICENSE`.
- **Data, figures and text** (every file listed in `DATA.md`, and the documentation): Creative Commons
  Attribution 4.0 International, `LICENSE-DATA`.

Copyright (c) 2026 the authors: {authors}.

## How to cite

Cite the paper and the archived version of this repository:

- {authors}, *{paper}*, preprint, [PLACEHOLDER: preprint identifier].
- {authors}, *Code and data for: {paper}*, Zenodo, [PLACEHOLDER: Zenodo DOI].

`CITATION.cff` and `.zenodo.json` hold the same metadata, with the authors' ORCID iDs and affiliations.
The repository is https://github.com/pa1aash/{name}.
"""

INSTALL = """## Install and run

Requirements: Python 3.13 (3.9 or newer works for the checks; the byte-identical figure rebuilds need the
pinned versions), `make`{extra}.

```
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt{pari_install}
make verify PYTHON=.venv/bin/python      # fast exact checks
make all PYTHON=.venv/bin/python         # everything
```

| target | what it runs | time |
|---|---|---|
| `make verify` | the fast exact checks | {t_verify} |
| `make full` | the long computations | {t_full} |
| `make figures` | rebuild every figure from its data and compare with the committed file | {t_figures} |
| `make tables` | regenerate every table and compare with the committed file | {t_tables} |
| `make data-check` | compare every data file with `SHA256SUMS` | seconds |
| `make all` | all of the above | {t_all} |
| `make clean` | remove caches and compiled helpers | |

Each target prints PASS, FAIL or SKIP for every step and exits nonzero if any step fails. A step also
fails if it changes a committed data file: regenerating committed data is a reproduction test. Times were
measured on an Apple M-series laptop with 8 GB of memory. `python3 tools/steps.py --list` lists every step;
`TRACE.md` maps every checkable item of the paper to its script and target; `DATA.md` lists every data
file with its size, checksum, producing script and paper element.
"""


def extract(src, start, end):
    t = Path(src).read_text(encoding="utf-8")
    i = t.index(start)
    j = t.index(end, i) + len(end)
    return t[i:j]


# ============================================================================================ the note
def note_post(dest, root):
    note = (root / "paper/arith/integers/note.tex").read_text(encoding="utf-8")
    envs = re.findall(r"\\begin\{table\}.*?\\end\{table\}", note, re.S)
    tabs = [re.search(r"\\begin\{tabular\}.*?\\end\{tabular\}\n", e, re.S).group(0) for e in envs]
    assert len(tabs) == 2 and "tab:fibres" in envs[0] and "tab:density" in envs[1], len(tabs)
    (dest / "tables").mkdir(exist_ok=True)
    (dest / "tables" / "fibres.tex").write_text(tabs[0], encoding="utf-8")
    (dest / "tables" / "density.tex").write_text(tabs[1], encoding="utf-8")
    # the generator must reproduce the tables printed in the paper
    import subprocess, sys
    r = subprocess.run([sys.executable, "tools/make_tables.py", "--check"], cwd=dest, capture_output=True, text=True)
    assert r.returncode == 0, "tools/make_tables.py does not reproduce the note's tables: " + r.stdout + r.stderr


NOTE_README = """# Triples with equal sum and equal reciprocal sum: code and data

This repository reproduces every computation stated in the paper

> {authors}, *{paper}*.

The paper studies unordered triples of positive integers with $1/a+1/b+1/c<1$ that share both their sum
and their reciprocal sum with another such triple, through the cubic pencil
$(x+y+z)(xy+yz+zx)=\\Lambda xyz$. The repository contains:

- `theory/diophantine/`: the exact enumeration of all such classes with sum at most 4800
  (`enumerate_fast.py` with the C kernel `enumerate_core.c`), its data (`data/groups.csv`,
  `data/per_S.csv`), the checks of the curves (`variety_checks.py`), the families and dual pairs
  (`families.py`), the growth fits (`growth_fits.py`, `exponent_fits.py`) and the Mordell–Weil ranks
  (`ranks.py`, PARI/GP);
- `checks/classes4800/`: a second, independent enumeration to $S=4800$ (`enum_classes.c`) with the checks
  that rest on it (`check_enum.py`), the group-law checks (`check_groups.py`), the 2-isogeny descents
  (`check_descent.py`), the isosceles family (`check_isosceles.py`) and the conic-bundle family
  (`check_theorem5_family.py`);
- `checks/enumeration6000/`: a third enumeration, to $S=6000$ (`enum.c`, `check_enum.py`);
- `checks/note/`: the remaining checks of the paper (`check_note.py`, with the enumeration of
  $4801\\le S\\le6000$), and `count_sums.py`;
- `checks/point3P/`: the point $3P$ on $C_{{155/12}}$;
- `code/`: the reference enumerator for $S\\le600$ that `enumerate_fast.py` is checked against;
- `figures/`: Figure 1 (`figures/src/F9.py`) with its style files;
- `tools/make_tables.py`: Tables 1 and 2 (`tables/`).

{ndata} data files, {total} in all (`DATA.md`).

"""

NOTE = dict(
    name="equal-sum-reciprocal-triples",
    short="the paper",
    paper=NOTE,
    keywords=["equal sums of reciprocals", "Egyptian fractions", "elliptic curves", "rational points",
              "cubic pencil", "Diophantine enumeration", "heat invariants", "hyperbolic orbifolds"],
    zenodo_description=("<p>Code and data for the paper <em>Triples with equal sum and equal reciprocal sum</em>: "
                        "the exact enumerations of all classes of triples of positive integers with equal sum and equal "
                        "reciprocal sum up to sum 4800 (two independent programs) and 6000, the checks of the cubic pencil, "
                        "the dual family, the growth fits, the Mordell-Weil ranks (PARI/GP) and 2-isogeny descents, the "
                        "figure and the tables. <code>make verify</code> reruns the fast checks and <code>make all</code> "
                        "everything; DATA.md lists every data file with its checksum, producing script and paper element, "
                        "and TRACE.md maps every checkable item of the paper to its script.</p>"),
    pari=True,
    copy=[
        ("theory/diophantine/enumerate_fast.py", None), ("theory/diophantine/enumerate_core.c", None),
        ("theory/diophantine/cubic_group.py", None), ("theory/diophantine/check_committed.py", None),
        ("theory/diophantine/variety_checks.py", None), ("theory/diophantine/growth_fits.py", None),
        ("theory/diophantine/exponent_fits.py", None), ("theory/diophantine/families.py", None),
        ("theory/diophantine/ranks.py", None),
        ("theory/diophantine/data/groups.csv", None), ("theory/diophantine/data/per_S.csv", None),
        ("theory/diophantine/data/ranks.txt", None), ("theory/diophantine/data/families.txt", None),
        ("theory/diophantine/data/line_families.csv", None), ("theory/diophantine/data/exponent_fits.txt", None),
        ("theory/diophantine/data/growth_fits.txt", None), ("theory/diophantine/data/birthday.csv", None),
        ("theory/diophantine/data/variety_checks.txt", None),
        ("review/audit/threshold/check_enum.py", "checks/enumeration6000/check_enum.py"),
        ("review/audit/threshold/check_enum.txt", "checks/enumeration6000/check_enum.txt"),
        ("review/audit/threshold/enum.c", "checks/enumeration6000/enum.c"),
        ("review/audit/threshold/tab_enum_reference.txt", "checks/enumeration6000/tab_enum_reference.txt"),
        ("review/audit/threshold/data/*", "checks/enumeration6000/data/"),
        ("review/audit/diophantine/dio_common.py", "checks/classes4800/dio_common.py"),
        ("review/audit/diophantine/check_enum.py", "checks/classes4800/check_enum.py"),
        ("review/audit/diophantine/check_enum.txt", "checks/classes4800/check_enum.txt"),
        ("review/audit/diophantine/enum_classes.c", "checks/classes4800/enum_classes.c"),
        ("review/audit/diophantine/enum_4800.txt", "checks/classes4800/enum_4800.txt"),
        ("review/audit/diophantine/check_groups.py", "checks/classes4800/check_groups.py"),
        ("review/audit/diophantine/check_groups.txt", "checks/classes4800/check_groups.txt"),
        ("review/audit/diophantine/check_descent.py", "checks/classes4800/check_descent.py"),
        ("review/audit/diophantine/check_descent.txt", "checks/classes4800/check_descent.txt"),
        ("review/audit/diophantine/check_isosceles.py", "checks/classes4800/check_isosceles.py"),
        ("review/audit/diophantine/check_isosceles.txt", "checks/classes4800/check_isosceles.txt"),
        ("review/audit/diophantine/check_theorem5_family.py", "checks/classes4800/check_theorem5_family.py"),
        ("review/audit/diophantine/check_theorem5_family.txt", "checks/classes4800/check_theorem5_family.txt"),
        ("theory/revision/check_point3P.py", "checks/point3P/check_point3P.py"),
        ("theory/revision/check_point3P.txt", "checks/point3P/check_point3P.txt"),
        ("paper/arith/checks/check_note.py", "checks/note/check_note.py"),
        ("paper/arith/checks/check_note.txt", "checks/note/check_note.txt"),
        ("paper/arith/checks/enum_classes.c", "checks/note/enum_classes.c"),
        ("code/enumerate_degeneracies.py", None), ("code/orbifold_enum.py", None),
        ("data/degeneracies.csv", None), ("data/degeneracy-groups.csv", None),
        ("figures/src/F9.py", None), ("figures/src/figlib.py", None), ("figures/src/common_import.py", None),
        ("figures/style/figstyle.py", None), ("figures/style/colourtools.py", None),
        ("figures/style/palette.json", None), ("figures/style/third_party/*", None),
        ("figures/style/fetch_third_party.py", None), ("figures/out/F9.pdf", None), ("figures/out/F9.png", None),
    ],
    extra={"tools/make_tables.py": "note_make_tables.py", "checks/note/count_sums.py": "note_count_sums.py"},
    post=[note_post],
    edits={
        "checks/note/check_note.py": [
            ("ROOT = Path(__file__).resolve().parents[3]", "ROOT = Path(__file__).resolve().parents[2]", 1),
            ('"""Exact checks of the statements that are new in the arithmetic note (paper/arith/note.tex).\n\n'
             'Everything else in the note is traced to theory/diophantine/ or review/audit/ (paper/arith/TRACE.md).\n'
             'This script checks, in exact arithmetic, what those directories do not already contain:',
             '"""Exact checks of statements of the note that the other scripts do not cover (TRACE.md):', 1),
            ("by the audit enumerator\n     (copied to checks/enum_classes.c)", "by the second enumerator\n     (enum_classes.c, as in checks/classes4800/)", 1),
            ("agree with the G5 enumeration", "agree with the third enumeration", 1),
        ],
        "checks/note/check_note.txt": [("agree with the G5 enumeration", "agree with the third enumeration", 2)],
        "checks/classes4800/check_descent.py": [("review/audit/.venv-pari/bin/python", "python3", 1)],
        "checks/classes4800/check_theorem5_family.py": [('"""Phase-2 check of Theorem 5 (DI.10) against the family now visible in the proof.',
                                                       '"""Check of Lemma 3 and Theorem 4 (the conic bundle of dual pairs) against the family of the proof.', 1)],
        "checks/classes4800/dio_common.py": [("helpers for the diophantine audit.\n\nEverything here is independent of the manuscript code.",
                                             "helpers for the checks in this folder.\n\nEverything here is independent of theory/diophantine/.", 1)],
        "checks/classes4800/check_enum.py": [
            ('"""Counterexample search over all degeneracy classes (DI.3, DI.9, DI.11 and the PC.19 table).',
             '"""Checks over all degeneracy classes to S = 4800: Sections 3 and 6.1 of the note.', 1),
            ("# ---- 2. PC.17/PC.18/PC.19 sanity", "# ---- 2. small sums", 1),
            ("the two classes of PC.18", "the two classes", 1),
            ("PC.19 table of N(S) reproduced exactly", "table of N(S) reproduced exactly", 1),
            ("# ---- 3. DI.11 first fibres of each size", "# ---- 3. first fibres of each size", 1),
            ("# ---- 4. DI.3 statistics: primitive pairs", "# ---- 4. statistics: primitive pairs", 1),
            ("DI.3 counts 1753 = 423 + 1330 reproduced", "counts 1753 = 423 + 1330 reproduced", 1),
            ("# ---- 5. DI.9 isosceles family", "# ---- 5. isosceles family", 1),
        ],
        "checks/classes4800/check_enum.txt": [("the two classes of PC.18", "the two classes", 1),
                                             ("PC.19 table of N(S) reproduced exactly", "table of N(S) reproduced exactly", 1),
                                             ("DI.3 counts 1753 = 423 + 1330 reproduced", "counts 1753 = 423 + 1330 reproduced", 1)],
        "checks/classes4800/check_isosceles.py": [('"""Numerical checks of Theorem 4 (DI.9) and the lower-bound bookkeeping (DI.8).',
                                                 '"""Numerical checks of Theorem 3 (the isosceles family) and of the count of its copies.', 1)],
        "checks/classes4800/check_groups.py": [
            ("DI.2 (orders of the six base points), DI.3 (P + T2 = iota(P), the 12-point orbit),\nDI.5 (P = (4,9,18)",
             "Orders of the six base points; P + T2 = iota(P) and the 12-point orbit;\nP = (4,9,18)", 1),
            ("odd multiples positive),\nDI.7 (the 12 rational", "odd multiples positive);\nthe 12 rational", 1),
            ("# ---------------- DI.2: base points", "# ---------------- base points", 1),
            ("# ---------------- DI.3: reciprocation and orbit", "# ---------------- reciprocation and orbit", 1),
            ("# ---------------- DI.5: large fibres", "# ---------------- large fibres", 1),
            ("# ---------------- DI.7: C_{27/2} torsion", "# ---------------- C_{27/2} torsion", 1),
        ],
        "checks/enumeration6000/check_enum.py": [
            ('"""Referee enumeration of two-coefficient collisions (PC.1, PC.17-PC.19, PC.21, TH.4, TH.5,\nTH.6(2)).  Exits nonzero on failure.',
             '"""Third enumeration of two-coefficient collisions, to S = 6000.  Exits nonzero on failure.', 1),
            ("conj:density growth to SMAX_C; TH.5 table; Prop 3(2).", "growth to SMAX_C; first collisions.", 1),
            ("referee listing for comparison with tab:enum", "listing of the triads of small sum", 1),
            ("(TH.5 text)", "", 1),
            ("# ---------------------------------------------------------------- TH.5 and Prop 3(2)", "# ---------------------------------------------------------------- first collisions", 1),
            ('print("== TH.5 first adjacent collision table and Prop 3(2)")', 'print("== first adjacent collision table")', 1),
            ('"TH.5: every row reproduced', '"every row reproduced', 1),
        ],
        "checks/enumeration6000/check_enum.txt": [("(TH.5 text)", "", 1),
                                                 ("== TH.5 first adjacent collision table and Prop 3(2)", "== first adjacent collision table", 1),
                                                 ("PASS TH.5: every row reproduced", "PASS every row reproduced", 1)],
        "checks/point3P/check_point3P.py": [
            ('"""Task 6 (G7-15): the coordinates of 3P', '"""The coordinates of 3P', 1),
            ("(c) the point printed in the manuscript, (162833463 : 287876366 : 723926268), lies on C_L but is a",
             "(c) the point (162833463 : 287876366 : 723926268), with Y and Z exchanged, lies on C_L but is a", 1),
        ],
        "theory/diophantine/growth_fits.py": [("re:([Bb]irthday heuristic|birthday|empirical) audit", r"\1 check", None)],
        "theory/diophantine/data/growth_fits.txt": [("birthday heuristic audit", "birthday heuristic check", 1)],
    },
    clean=["checks/classes4800/enum_classes", "checks/enumeration6000/data/enum"],
    steps=[
        dict(name="committed data consistent", targets=["verify"], dir="theory/diophantine", cmd="$PYTHON check_committed.py", minutes=0.2),
        dict(name="curves of the pencil", targets=["verify"], dir="theory/diophantine", cmd="$PYTHON variety_checks.py", minutes=0.1),
        dict(name="families and dual pairs", targets=["verify"], dir="theory/diophantine", cmd="$PYTHON families.py 4800 7", minutes=4),
        dict(name="growth fits", targets=["verify"], dir="theory/diophantine", cmd="$PYTHON growth_fits.py", minutes=0.7, needs="cc"),
        dict(name="exponent fits", targets=["verify"], dir="theory/diophantine", cmd="$PYTHON exponent_fits.py", minutes=2),
        dict(name="ranks (PARI ellrank)", targets=["verify"], dir="theory/diophantine", cmd="$PYTHON_PARI ranks.py", minutes=0.1, needs="pari"),
        dict(name="note checks, with the enumeration 4801..6000", targets=["verify"], dir=".", cmd="$PYTHON checks/note/check_note.py --enum", minutes=1.5, needs="cc"),
        dict(name="sums with a primitive class", targets=["verify"], dir=".", cmd="$PYTHON checks/note/count_sums.py", minutes=0.1),
        dict(name="the point 3P", targets=["verify"], dir=".", cmd="$PYTHON checks/point3P/check_point3P.py", minutes=0.1),
        dict(name="classes to 4800, second program", targets=["verify"], dir="checks/classes4800", cmd="$PYTHON check_enum.py", minutes=2, needs="cc"),
        dict(name="group law on the curves", targets=["verify"], dir="checks/classes4800", cmd="$PYTHON check_groups.py", minutes=0.5),
        dict(name="2-isogeny descents (PARI points)", targets=["verify"], dir="checks/classes4800", cmd="$PYTHON_PARI check_descent.py", minutes=0.5, needs="pari"),
        dict(name="isosceles family", targets=["verify"], dir="checks/classes4800", cmd="$PYTHON check_isosceles.py", minutes=2),
        dict(name="conic-bundle family", targets=["verify"], dir="checks/classes4800", cmd="$PYTHON check_theorem5_family.py", minutes=1),
        dict(name="enumeration to 6000, third program", targets=["verify"], dir="checks/enumeration6000", cmd="$PYTHON check_enum.py",
             transcript="checks/enumeration6000/check_enum.txt", minutes=2),
        dict(name="tables 1 and 2", targets=["tables"], dir=".", cmd="$PYTHON tools/make_tables.py --check", minutes=0.1),
        dict(name="figure 1 (F9)", targets=["figures"], dir=".", cmd="$PYTHON figures/src/F9.py", minutes=0.3),
        dict(name="enumeration to 4800 from scratch (enumerate_fast)", targets=["full"], dir="theory/diophantine",
             cmd="$PYTHON enumerate_fast.py 4800", minutes=30, needs="cc"),
        dict(name="second program from scratch to 4800", targets=["full"], dir="checks/classes4800",
             cmd='cc -O2 -o "$LOGDIR/enum_classes" enum_classes.c && "$LOGDIR/enum_classes" 10 4800 4800 > "$LOGDIR/enum_4800.txt" && cmp "$LOGDIR/enum_4800.txt" enum_4800.txt',
             minutes=10, needs="cc"),
        dict(name="third program from scratch to 6000", targets=["full"], dir="checks/enumeration6000",
             cmd='mkdir -p "$LOGDIR/e6000" && cp check_enum.py enum.c "$LOGDIR/e6000/" && (cd "$LOGDIR/e6000" && $PYTHON check_enum.py > out.txt) && '
                 'cmp "$LOGDIR/e6000/data/summary_10_6000.txt" data/summary_10_6000.txt && cmp "$LOGDIR/e6000/data/fibres_10_2000.txt" data/fibres_10_2000.txt',
             minutes=20, needs="cc"),
    ],
    data=[
        ("theory/diophantine/data/groups.csv", "`theory/diophantine/enumerate_fast.py`", "every class with $S\\le4800$: Table 1, Theorem 4, Section 6, Figure 1"),
        ("theory/diophantine/data/per_S.csv", "`theory/diophantine/enumerate_fast.py`", "counts per sum: Table 2, Sections 3 and 6, Figure 1"),
        ("theory/diophantine/data/ranks.txt", "`theory/diophantine/ranks.py` (PARI)", "ranks and torsion of Table 1 and Section 5"),
        ("theory/diophantine/data/families.txt", "`theory/diophantine/families.py`", "dual pairs (Section 3, 6.1), isosceles count (Theorem 2), lines (Section 6.4), Figure 1"),
        ("theory/diophantine/data/line_families.csv", "`theory/diophantine/families.py`", "the 189 lines of Section 6.4"),
        ("theory/diophantine/data/exponent_fits.txt", "`theory/diophantine/exponent_fits.py`", "the fits of Section 6.3, Figure 1(b)"),
        ("theory/diophantine/data/growth_fits.txt", "`theory/diophantine/growth_fits.py`", "the model comparison of Section 6.3"),
        ("theory/diophantine/data/birthday.csv", "`theory/diophantine/growth_fits.py`", "input of the model comparison of Section 6.3"),
        ("theory/diophantine/data/variety_checks.txt", "`theory/diophantine/variety_checks.py`", "Propositions 1-3 (pencil, maps, base points, reciprocation)"),
        ("checks/enumeration6000/check_enum.txt", "`checks/enumeration6000/check_enum.py` (standard output)", "Table 2 (counts and local exponents to $S=6000$), Section 6.3"),
        ("checks/enumeration6000/tab_enum_reference.txt", "`checks/enumeration6000/check_enum.py`", "listing of the classes of small sum (by-product)"),
        ("checks/enumeration6000/data/summary_10_6000.txt", "`checks/enumeration6000/enum.c` (via `check_enum.py`)", "Table 2, Section 6.3"),
        ("checks/enumeration6000/data/fibres_10_2000.txt", "`checks/enumeration6000/enum.c` (via `check_enum.py`)", "class listing to $S=2000$, compared with the pure-Python enumeration"),
        ("checks/classes4800/check_enum.txt", "`checks/classes4800/check_enum.py`", "Section 3 (orders of $P'\\pm P$), Section 6.1 (histogram, admissible triples)"),
        ("checks/classes4800/enum_4800.txt", "`checks/classes4800/enum_classes.c` (`enum_classes 10 4800 4800`)", "the second enumeration of Section 6.1"),
        ("checks/classes4800/check_groups.txt", "`checks/classes4800/check_groups.py`", "Theorem 4 ($nP\\ne O$), Lemma 2, Theorem 1, Proposition 2"),
        ("checks/classes4800/check_descent.txt", "`checks/classes4800/check_descent.py`", "the 2-isogeny descents of Section 5"),
        ("checks/classes4800/check_isosceles.txt", "`checks/classes4800/check_isosceles.py`", "Theorem 2 (the copies with $k\\ge4$, a subset of those counted in Section 4)"),
        ("checks/classes4800/check_theorem5_family.txt", "`checks/classes4800/check_theorem5_family.py`", "Lemma 4 and Theorem 3"),
        ("checks/point3P/check_point3P.txt", "`checks/point3P/check_point3P.py`", "the point $3P$ of Section 5"),
        ("checks/note/check_note.txt", "`checks/note/check_note.py --enum`", "Lemmas 1 and 3, Proposition 2, Theorems 1 and 2, Proposition 4, Table 1, Table 2 (row 6000)"),
        ("data/degeneracies.csv", "`code/enumerate_degeneracies.py`", "reference counts for $S\\le600$, read by `check_committed.py`"),
        ("data/degeneracy-groups.csv", "`code/enumerate_degeneracies.py`", "reference classes for $S\\le600$, checked by `enumerate_fast.py`"),
        ("figures/out/F9.pdf", "`figures/src/F9.py`", "Figure 1"),
        ("figures/out/F9.png", "`figures/src/F9.py`", "Figure 1 (preview)"),
        ("figures/style/palette.json", "fixed input (colour palette)", "Figure 1 (style)"),
        ("figures/style/third_party/*", "fetched colour tables (`SOURCES.json` gives their sources and licences)", "Figure 1 (colour maps)"),
        ("tables/*.tex", "`tools/make_tables.py`", "Tables 1 and 2"),
    ],
    trace=[
        ("Abstract, Section 1", "smallest coincidence $\\{(2,8,8),(3,3,12)\\}$, $S=18$, $R=3/4$", "`checks/note/check_note.py`, `theory/diophantine/check_committed.py`", "note checks, with the enumeration 4801..6000; committed data consistent"),
        ("Abstract, Section 6.1", "$3.07\\times10^9$ admissible triples with $S\\le4800$", "`checks/classes4800/check_enum.py`", "classes to 4800, second program"),
        ("Abstract, Sections 1.3, 6.3", "local growth exponent from $2.0$ at $500$ to $1.58$ at $6000$", "`checks/enumeration6000/check_enum.py`", "enumeration to 6000, third program"),
        ("Lemma 1", "every coincidence is admissible", "`checks/note/check_note.py`", "note checks, with the enumeration 4801..6000"),
        ("Proposition 1", "classes are points on a cubic; $\\Lambda=SR$", "`theory/diophantine/variety_checks.py`", "curves of the pencil"),
        ("Proposition 2", "pencil identity, fibre types, maps to $E_\\Lambda$, discriminant, base points of orders 2, 3, 6", "`theory/diophantine/variety_checks.py`", "curves of the pencil"),
        ("Proposition 2", "orders of the base points from five lines through the flex $O$", "`checks/note/check_note.py`", "note checks, with the enumeration 4801..6000"),
        ("Proposition 2", "$(1:4:4)\\mapsto(-6,45)$ at $\\Lambda=27/2$", "`checks/note/check_note.py`", "note checks, with the enumeration 4801..6000"),
        ("Lemma 2", "odd multiples of a positive point are positive", "`checks/classes4800/check_groups.py`", "group law on the curves"),
        ("Theorem 1", "$(\\Lambda^2-6\\Lambda-3)^2-64\\Lambda=(\\Lambda-1)^3(\\Lambda-9)$; isosceles criterion", "`checks/note/check_note.py`", "note checks, with the enumeration 4801..6000"),
        ("Theorem 1", "geometric progressions of order 12 (order 4 when the middle term is last); isosceles orientations of orders 6, 6, 2; positive torsion points with $S\\le60$", "`checks/note/check_note.py`", "note checks, with the enumeration 4801..6000"),
        ("Theorem 1", "torsion $\\mathbb Z/2\\times\\mathbb Z/6$ at $\\Lambda=27/2$", "`theory/diophantine/ranks.py`", "ranks (PARI ellrank)"),
        ("Proposition 3, Corollary 1", "reciprocation is translation by $T_2$; the dual family", "`theory/diophantine/variety_checks.py`, `theory/diophantine/families.py`", "curves of the pencil; families and dual pairs"),
        ("Section 3", "1753 primitive pairs with $S\\le600$, 423 dual", "`theory/diophantine/families.py`", "families and dual pairs"),
        ("Section 3", "for the other 1330, neither $P'-P$ nor $P'+P$ has order at most 12", "`checks/classes4800/check_enum.py`", "classes to 4800, second program"),
        ("Lemma 3", "$\\mathcal N(X)=\\sum_D\\lfloor X/S_D\\rfloor$ over the primitive pairs, for every $X\\le4800$", "`checks/note/check_note.py`", "note checks, with the enumeration 4801..6000"),
        ("Theorem 2", "the isosceles family; 506 primitive isosceles pairs with $S\\le4800$", "`checks/note/check_note.py`, `theory/diophantine/families.py`", "note checks, with the enumeration 4801..6000; families and dual pairs"),
        ("Theorem 2", "copies $kD_{u,v}$, $k\\ge1$: $0.608X$ at $X=4800$ and $c_{\\rm iso}X\\log X-0.286X$; threshold $\\log X>437.8$ for Theorem 3", "`checks/note/check_note.py`", "note checks, with the enumeration 4801..6000"),
        ("Lemma 4, Theorem 3", "conic bundle of dual pairs; the three geometric-progression ratios; multiplicity; constants $3/(32\\pi^4)$, $3/(128\\pi^4)$", "`checks/classes4800/check_theorem5_family.py`, `theory/diophantine/families.py`", "conic-bundle family; families and dual pairs"),
        ("Theorem 4", "$P=(4:9:18)$ on $C_{155/12}$ has $nP\\ne O$ for $n\\le12$", "`checks/classes4800/check_groups.py`", "group law on the curves"),
        ("Section 5", "rank 0 of $C_{27/2}$ and its twelve rational points", "`theory/diophantine/ranks.py`", "ranks (PARI ellrank)"),
        ("Section 5", "rank of $C_{155/12}$ is 2 (`ellrank`, $r_1=r_2$)", "`theory/diophantine/ranks.py`", "ranks (PARI ellrank)"),
        ("Section 5", "independent 2-isogeny descents give the same ranks", "`checks/classes4800/check_descent.py`", "2-isogeny descents (PARI points)"),
        ("Section 5", "$3P=(162833463:723926268:287876366)$", "`checks/point3P/check_point3P.py`", "the point 3P"),
        ("Section 5", "first classes of sizes 3-6 at $S=136,408,1849,4600$; no class of size 7 to 6000", "`checks/note/check_note.py`, `checks/classes4800/check_enum.py`", "note checks, with the enumeration 4801..6000; classes to 4800, second program"),
        ("Table 1", "first class of each size, $\\Lambda$, ranks, torsion groups", "`tools/make_tables.py` (from `groups.csv`, `ranks.txt`)", "tables 1 and 2"),
        ("Table 2", "cumulative counts and local exponents", "`tools/make_tables.py` (from `check_enum.txt`, `per_S.csv`, `check_note.txt`)", "tables 1 and 2"),
        ("Section 6.1", "two independent enumerations agree to $S=4800$; class by class against exact fractions for $S\\le300$", "`theory/diophantine/enumerate_fast.py`, `checks/classes4800/check_enum.py`", "classes to 4800, second program; enumeration to 4800 from scratch (enumerate_fast)"),
        ("Section 6.1", "a third enumeration to $S=6000$", "`checks/enumeration6000/check_enum.py`", "enumeration to 6000, third program; third program from scratch to 6000"),
        ("Section 6.1", "the second program on $4801\\le S\\le6000$: counts at 5400 and 6000, 62401 primitive classes", "`checks/note/check_note.py --enum`", "note checks, with the enumeration 4801..6000"),
        ("Section 6.1", "582 sums $19\\le S\\le600$, 507 with a primitive class", "`checks/note/count_sums.py`", "sums with a primitive class"),
        ("Section 6.1", "class-size histogram to 4800", "`checks/classes4800/check_enum.py`", "classes to 4800, second program"),
        ("Section 6.1", "dual pairs: 32.9% to 200, 16.5% of 46 254 to 4800; 669 non-dual pairs to 400", "`theory/diophantine/families.py`", "families and dual pairs"),
        ("Section 1.4", "$R/r=(\\Lambda-1)/4$ under the Ravi substitution", "`checks/note/check_note.py`", "note checks, with the enumeration 4801..6000"),
        ("Proposition 4", "factorisation identity; recount of $n(S)$ for $S\\le160$", "`checks/note/check_note.py`", "note checks, with the enumeration 4801..6000"),
        ("Section 6.3", "fits of the exponent $q$ and their errors", "`theory/diophantine/exponent_fits.py`", "exponent fits"),
        ("Section 6.3", "a quadratic law is not supported", "`theory/diophantine/growth_fits.py`", "growth fits"),
        ("Section 6.3", "$\\mathcal N(S)/S^2$ from $0.0094$ to $0.0040$", "`checks/enumeration6000/check_enum.py`", "enumeration to 6000, third program"),
        ("Section 6.4", "189 lines; 84% of primitive pairs to 4800 are not dual", "`theory/diophantine/families.py`", "families and dual pairs"),
        ("Section 6.4", "pairs of points and the fibre square", "`theory/diophantine/variety_checks.py`", "curves of the pencil"),
        ("Figure 1", "the curve $C_{27/2}$ and the growth of the counts", "`figures/src/F9.py`", "figure 1 (F9)"),
    ],
)
NOTE["readme"] = NOTE_README + INSTALL.format(extra=", a C compiler (`cc`) and, for the PARI steps, `cypari2`",
                                             pari_install="\n.venv/bin/pip install --only-binary :all: -r requirements-pari.txt",
                                             t_verify="{t_verify}", t_full="{t_full}", t_figures="{t_figures}",
                                             t_tables="{t_tables}", t_all="{t_all}") + """
## Optional components

- **PARI/GP** (`requirements-pari.txt`, cypari2 2.2.4 with PARI/GP 2.17.2): the ranks and the descents.
  Without it those two steps are skipped with a message. Set `PYTHON_PARI` to use another interpreter.
- **C compiler**: the enumerations. Without `cc` (or `CC`) those steps are skipped with a message.
- `make full` reruns the three enumerations from scratch and compares their output with the committed
  files; they use all cores and about 400 MB of memory.

"""

REPOS = {"equal-sum-reciprocal-triples": NOTE}


# ============================================================================================== Paper A
def a_post(dest, root):
    supp = (root / "paper/jga/supplement.tex").read_text(encoding="utf-8")
    blocks = re.findall(r"% BEGIN GENERATED TABLE (\S+)\n.*?% END GENERATED TABLE \1\n?", supp, re.S)
    assert sorted(blocks) == ["enum", "overlap", "pairs", "thresholds_full"], blocks
    body = "".join(m.group(0) for m in re.finditer(r"% BEGIN GENERATED TABLE (\S+)\n.*?% END GENERATED TABLE \1\n?", supp, re.S))
    (dest / "tables").mkdir(exist_ok=True)
    (dest / "tables" / "supplement_tables.tex").write_text(
        "% The generated tables of the supplement (S1 pairs, S2 overlap, S3 enum, S4 thresholds_full), each between\n"
        "% its markers, as printed. tools/make_tables.py and checks/pairs/d2_explicit_pairs.py regenerate them.\n\n"
        + body, encoding="utf-8")
    st = (root / "review/audit-2/statements/pte-witnesses.md").read_text(encoding="utf-8")
    blk = st.split("### PW.5")[1].split("```")[1]
    (dest / "checks" / "witnesses4" / "pencil_configurations.md").write_text(
        "# The 61 pencil configurations of degree 4 (entries at most 220)\n\n"
        "The configurations of `theory/pte/data/pencil_m4_N220.json`, one per line, read by `check_direct4.py`.\n\n"
        "### PW.5\n```" + blk + "```\n", encoding="utf-8")
    import subprocess, sys
    r = subprocess.run([sys.executable, "tools/make_tables.py", "--check"], cwd=dest, capture_output=True, text=True)
    assert r.returncode == 0, "tools/make_tables.py does not reproduce the paper's tables: " + r.stdout + r.stderr


A_TABLE_EDITS = [
    ("ROOT = Path(__file__).resolve().parents[3]", "ROOT = Path(__file__).resolve().parents[1]", 1),
    ('FILES = {TEX.parent / "supplement.tex": ["overlap", "enum", "thresholds_full"]}',
     'FILES = {ROOT / "tables" / "supplement_tables.tex": ["overlap", "enum", "thresholds_full"]}', 1),
    ("re:^# -+ fibres\n.*?(?=^# -+ enum)", "", None),
    ("re:^def table_fibres\\(\\):.*?(?=^def table_enum)", "", None),
    ('"""Regenerate the tables of paper/jga/manuscript.tex and supplement.tex from committed data.',
     '"""Regenerate the generated tables of the supplement (tables/supplement_tables.tex) from committed data.', 1),
    ("in manuscript.tex, so that the manuscript stays a single file as the journal template asks.", "in tables/supplement_tables.tex.", 1),
    (" (in the supplement; the paper's four-column table was removed in referee round 2)", " (Table S4)", 1),
    ('TEX = ROOT / "paper" / "jga" / "manuscript.tex"\n', "", 1),
    (" (review/audit-2 F8)", "", 1),
    ("re:^# The 30-35 page revision keeps.*?(?=^TABLES = )", "", 1),
    ('          "fibres": table_fibres,\n          "density": table_density, "enum": table_enum}', '          "enum": table_enum}', 1),
    ("# Referee round 2 (R4): the threshold table left the paper; only the full table is written.\n", "", 1),
    ("re:^  fibres .*?\n(?=  enum )", "", 1),
]

FIG_A = ["F2", "F3", "F4", "F5", "F7", "F8"]
BLENDER_RENDER = ('rm -rf "$LOGDIR/render-{f}" && mkdir -p "$LOGDIR/render-{f}" && cp -R figures numerics theory "$LOGDIR/render-{f}/" && '
                  'cd "$LOGDIR/render-{f}" && $PYTHON figures/src/{f}.py && test -s figures/out/{f}.pdf')

PAPER_A_STEPS = [
    dict(name="Orlando's formula", targets=["verify"], dir="theory/audibility", cmd="$PYTHON orlando_check.py", minutes=0.1),
    dict(name="Theorem B: the linear system", targets=["verify"], dir="theory/audibility", cmd="$PYTHON linear_system.py", minutes=0.3),
    dict(name="Theorem A and Lemma 3.1: elimination", targets=["verify"], dir="theory/audibility", cmd="$PYTHON verify_elimination.py", minutes=2),
    dict(name="Theorem C and Remark 3.2: sharpness search N=60", targets=["verify"], dir="theory/audibility",
         cmd='rm -rf "$LOGDIR/sharp60" && cp -R . "$LOGDIR/sharp60" && (cd "$LOGDIR/sharp60" && $PYTHON sharpness_search.py 60 > /dev/null) && '
             '$PYTHON ../../tools/json_equal.py "$LOGDIR/sharp60/sharpness_n5_N60.json" sharpness_n5_N60.json --ignore wall_seconds', minutes=0.4),
    dict(name="cone coefficients p_l", targets=["verify"], dir="theory/cone-coefficients", cmd="$PYTHON verify_cone_coefficients.py", minutes=0.1),
    dict(name="heat structure of a signature", targets=["verify"], dir="theory/signatures", cmd="$PYTHON heat_structure.py", minutes=0.1),
    dict(name="cone count", targets=["verify"], dir="theory/signatures", cmd="$PYTHON cone_count.py", minutes=0.5),
    dict(name="complete area classes", targets=["verify"], dir="theory/signatures", cmd="$PYTHON area_classes.py", minutes=0.7),
    dict(name="genus separation", targets=["verify"], dir="theory/signatures", cmd="$PYTHON genus.py", minutes=2.5),
    dict(name="trace formula terms (locality)", targets=["verify"], dir="theory/locality", cmd="$PYTHON check_locality.py", minutes=0.3),
    dict(name="stability: front end", targets=["verify"], dir="theory/stability", cmd="$PYTHON front_end.py", minutes=0.1),
    dict(name="stability: Lipschitz constants", targets=["verify"], dir="theory/stability", cmd="$PYTHON lipschitz_e.py", minutes=0.1),
    dict(name="stability: Hoelder exponents of roots", targets=["verify"], dir="theory/stability", cmd="$PYTHON roots_holder.py", minutes=0.1),
    dict(name="blind recovery from the computed spectra", targets=["verify"], dir="theory/stability/blind", cmd="$PYTHON blind_pipeline.py", minutes=0.1),
    dict(name="stability constants zeta_n and sech^2 coefficients", targets=["verify"], dir="checks/stability-constants",
         cmd="$PYTHON check_setup.py", transcript="checks/stability-constants/check_setup.txt", minutes=1.5),
    dict(name="first overlap and first collision (Section 5)", targets=["verify"], dir="theory/threshold", cmd="$PYTHON threshold.py", minutes=0.4),
    dict(name="flat and spherical cases", targets=["verify"], dir="theory/curvature", cmd="$PYTHON curvature_checks.py", minutes=0.1),
    dict(name="rank of C_{27/2} (PARI ellrank)", targets=["verify"], dir="theory/diophantine", cmd="$PYTHON_PARI ranks.py", minutes=0.1, needs="pari"),
    dict(name="computed spectra: committed data", targets=["verify"], dir="numerics", cmd="$PYTHON validate_committed.py --quick", minutes=0.2),
    dict(name="moduli family: committed data", targets=["verify"], dir="numerics/moduli", cmd="$PYTHON validate_committed.py --quick", minutes=0.1),
    dict(name="locality bound: overestimation ratios", targets=["verify"], dir="numerics/moduli", cmd="$PYTHON locality_ratio.py", minutes=0.1),
    dict(name="double-window recomputation: record", targets=["verify"], dir="numerics", cmd="$PYTHON rerun_double_window.py --verify-record", minutes=0.1),
] + [
    dict(name=f"proof check {s}", targets=["verify"], dir=".", cmd=f"$PYTHON checks/proofs/{s}.py", minutes=m)
    for s, m in [("check_lemma25", 0.4), ("check_remark412", 0.1), ("check_thm12iii", 0.1), ("check_descent", 0.1),
                 ("check_thm513", 0.2), ("check_remark212", 0.1), ("check_prop610", 0.2), ("check_sharpness", 0.1)]
] + [
    dict(name=f"PTE {s}", targets=["verify"], dir="theory/pte", cmd=f"$PYTHON {s}.py", transcript=f"theory/pte/output/{s}.txt", minutes=m,
         **({"needs": "cc"} if s == "search_T3_control" else {}))
    for s, m in [("structure", 0.2), ("growth", 0.1), ("witnesses", 0.2), ("real_shapes", 2), ("search_T3_control", 7.5), ("pencil_search", 4)]
] + [
    dict(name="PTE T3 modular record", targets=["verify"], dir="theory/pte", cmd="$PYTHON search_T3_modular.py --check", minutes=0.1),
    dict(name="PTE T3 modular search to 220", targets=["verify"], dir="theory/pte", cmd="$PYTHON search_T3_modular.py 220 4 > /dev/null", minutes=3, needs="cc"),
    dict(name="bounded cone orders (Theorem 3.8)", targets=["verify"], dir="theory/msep", cmd="$PYTHON verify.py", minutes=3.5),
] + [
    dict(name=f"variable curvature {s}", targets=["verify"], dir="theory/varcurv", cmd=f"$PYTHON {s}.py", transcript=f"theory/varcurv/{s}_output.txt", minutes=m)
    for s, m in [("quadratic_form", 0.1), ("top_coefficient", 0.7), ("linear_part", 0.7), ("obstruction_check", 0.1), ("twisted_mp", 2.5)]
] + [
    dict(name="K_mult on the complete area classes", targets=["verify"], dir="checks/pairs", cmd="$PYTHON a1_fig2_kmult.py",
         transcript="checks/pairs/output/a1_fig2_kmult.txt", minutes=0.3),
    dict(name="pencil witness counts", targets=["verify"], dir="checks/pairs", cmd="$PYTHON d1_pencil_counts.py",
         transcript="checks/pairs/output/d1_pencil_counts.txt", minutes=0.1),
    dict(name="explicit pairs (Table S1)", targets=["verify"], dir="checks/pairs", cmd="$PYTHON d2_explicit_pairs.py",
         transcript="checks/pairs/output/d2_explicit_pairs.txt", minutes=1.5),
    dict(name="degree-4 witnesses to 440: analysis", targets=["verify"], dir="checks/witnesses4", cmd="$PYTHON check_direct4.py",
         transcript="checks/witnesses4/check_direct4.txt", minutes=0.2),
    dict(name="supplement tables S2-S4", targets=["tables"], dir=".", cmd="$PYTHON tools/make_tables.py --check", minutes=0.1),
    dict(name="supplement table S1 (pairs)", targets=["tables"], dir="checks/pairs", cmd="$PYTHON d2_explicit_pairs.py --check > /dev/null", minutes=1.5),
    dict(name="figure data F4 F7 F8", targets=["figures"], dir=".",
         cmd="$PYTHON figures/gen/gen_f4_area_classes.py && $PYTHON figures/gen/gen_f7_strata.py && $PYTHON figures/gen/gen_f8_recovery.py", minutes=1.2),
] + [dict(name=f"figure {f}", targets=["figures"], dir=".", cmd=f"$PYTHON figures/src/{f}.py", minutes=0.1) for f in FIG_A] + [
    dict(name="figures F1 F6: data assertions", targets=["figures"], dir=".", cmd="$PYTHON figures/src/F1.py --check && $PYTHON figures/src/F6.py --check", minutes=0.2),
    dict(name="figure F1: Blender render (scratch copy)", targets=["figures"], dir=".", cmd=BLENDER_RENDER.format(f="F1"), minutes=15, needs="blender"),
    dict(name="figure F6: Blender render (scratch copy)", targets=["figures"], dir=".", cmd=BLENDER_RENDER.format(f="F6"), minutes=15, needs="blender"),
    dict(name="Remark 3.2: no witness for n=5 with orders <= 120", targets=["full"], dir="theory/audibility",
         cmd='rm -rf "$LOGDIR/sharp120" && cp -R . "$LOGDIR/sharp120" && (cd "$LOGDIR/sharp120" && $PYTHON sharpness_search.py 120 > /dev/null) && '
             '$PYTHON ../../tools/json_equal.py "$LOGDIR/sharp120/sharpness_n5_N120.json" sharpness_n5_N120.json --ignore wall_seconds', minutes=7),
    dict(name="stability thresholds and certificates", targets=["full"], dir="theory/stability", cmd="$PYTHON threshold.py", minutes=7),
    dict(name="divergence of the heat coefficients", targets=["full"], dir="theory/divergence", cmd="$PYTHON divergence.py", minutes=6.5),
    dict(name="computed spectra: full validation", targets=["full"], dir="numerics", cmd="$PYTHON validate_committed.py", minutes=0.3),
    dict(name="moduli family: full validation", targets=["full"], dir="numerics/moduli", cmd="$PYTHON validate_committed.py", minutes=0.6),
    dict(name="degree-4 witnesses to 440: search from scratch", targets=["full"], dir="checks/witnesses4",
         cmd='cc -O2 -o "$LOGDIR/direct4" check_direct4.c && "$LOGDIR/direct4" 440 > "$LOGDIR/direct4_N440.txt" && cmp "$LOGDIR/direct4_N440.txt" direct4_N440.txt',
         minutes=12, needs="cc"),
    dict(name="computed spectra: double-window re-solve (NGSolve)", targets=["full"], dir="numerics",
         cmd='$PYTHON_NUMERICS rerun_double_window.py --no-record "$LOGDIR/rerun"', minutes=60, needs="ngsolve"),
]

PAPER_A_README = """# How many heat invariants determine a hyperbolic orbifold? Code and data

This repository reproduces every computation stated in the paper

> {authors}, *{paper}*,

and in its electronic supplement. The paper asks how many heat invariants determine the genus and the cone
orders of a closed hyperbolic 2-orbifold. The repository contains:

- `theory/audibility/`: Theorems A, B and C, Orlando's formula, the searches of Remark 3.2;
- `theory/cone-coefficients/`, `theory/signatures/`, `theory/locality/`, `theory/curvature/`,
  `theory/divergence/`: the cone polynomials, signature data, complete area classes, the terms of the trace
  formula and the asymptotics of the heat coefficients;
- `theory/msep/verify.py`: the bounded-order theorem (Theorem 3.8), with `theory/eigen/eigen_common.py`;
- `theory/pte/`: the Prouhet–Tarry–Escott constructions, the growth bounds, the pencil search and the
  modular search of Remark 3.18 (C programs `search_T3.c`, `search_T3_modular.c`);
- `theory/threshold/`, `theory/stability/`: triangle orbifolds (Section 5) and stability (Section 6), with
  the blind recovery of the supplement (`theory/stability/blind/`, protocol in `PROTOCOL.md`);
- `theory/varcurv/`: the exact computer algebra of variable curvature (Section 2.4);
- `theory/diophantine/ranks.py`: the rank of $C_{{27/2}}$ (PARI/GP);
- `checks/proofs/`: exact checks of individual proofs (Lemmas 2.5-2.8, the descent of $C_{{27/2}}$,
  Proposition S2.1, Proposition S3.5 and others), each writing its transcript;
- `checks/pairs/`: the explicit pairs of Table S1 (`d2_explicit_pairs.py`), the pencil counts
  (`d1_pencil_counts.py`) and $K_{{\\rm mult}}$ on the area classes (`a1_fig2_kmult.py`);
- `checks/witnesses4/`: the exhaustive degree-4 search of Remark 3.2 (`check_direct4.c`) and its analysis;
- `checks/stability-constants/`: the constants $\\zeta_n$ and the $\\operatorname{{sech}}^2$ coefficients of
  Section S3;
- `numerics/`: the finite-element eigenvalues of $\\mathcal O(2,8,8)$ and $\\mathcal O(3,3,12)$ (`solve.py`,
  NGSolve), their validation (`validate.py`, `validate_committed.py`), heat traces and the double-window
  recomputation (`rerun_double_window.py`); `numerics/moduli/`: the moduli family of Section 4;
- `figures/`: Figures 1-8 (`figures/src/F*.py`, data generators in `figures/gen/`);
- `tools/make_tables.py`: Tables S2-S4 (`tables/supplement_tables.tex`).

{ndata} data files, {total} in all (`DATA.md`).

"""
PAPER_A = dict(
    name="heat-invariants-orbifolds",
    short="the paper",
    paper=PAPER_A,
    supplement=True,
    keywords=["heat invariants", "hyperbolic orbifolds", "inverse spectral problems", "cone singularities",
              "power sums", "Prouhet-Tarry-Escott problem", "Laplace eigenvalues", "Selberg trace formula"],
    zenodo_description=("<p>Code and data for the paper <em>How many heat invariants determine a hyperbolic orbifold?</em> and its "
                        "supplement: the exact-arithmetic checks of the theorems on heat invariants of closed hyperbolic "
                        "2-orbifolds, the Prouhet-Tarry-Escott constructions and searches, the stability constants and "
                        "certificates, the computer algebra of variable curvature, the finite-element eigenvalues of the "
                        "minimal triangle pair and of a moduli family with their validation, the figures and the generated "
                        "tables. <code>make verify</code> reruns the fast checks and <code>make all</code> everything; DATA.md "
                        "lists every data file with its checksum, producing script and paper element, and TRACE.md maps "
                        "every checkable item of the paper to its script.</p>"),
    pari=True,
    optional_env=NGSOLVE_ENV + """# Blender (figures F1 and F6; tested with Blender 5.2.2): install it from blender.org and put
# `blender` on PATH, or set BLENDER. Without it the two render steps are skipped with a message;
# the data assertions of F1 and F6 run in the core environment.
""",
    copy=[(p, None) for p in [
        "theory/audibility/audibility_common.py", "theory/audibility/orlando_check.py", "theory/audibility/linear_system.py",
        "theory/audibility/verify_elimination.py", "theory/audibility/sharpness_search.py",
        "theory/audibility/sharpness_n5_N60.json", "theory/audibility/sharpness_n5_N120.json", "theory/audibility/output/*",
        "theory/cone-coefficients/verify_cone_coefficients.py", "theory/cone-coefficients/verify_output.txt",
        "theory/signatures/sig_common.py", "theory/signatures/heat_structure.py", "theory/signatures/cone_count.py",
        "theory/signatures/area_classes.py", "theory/signatures/genus.py", "theory/signatures/output/*",
        "theory/locality/check_locality.py", "theory/locality/output/check_locality.txt",
        "theory/curvature/curvature_checks.py", "theory/curvature/curvature_output.txt",
        "theory/divergence/divergence.py", "theory/divergence/divergence_output.txt",
        "theory/threshold/threshold.py", "theory/threshold/first_overlap_vs_collision.csv", "theory/threshold/threshold_output.txt",
        "theory/stability/stab_common.py", "theory/stability/front_end.py", "theory/stability/lipschitz_e.py",
        "theory/stability/roots_holder.py", "theory/stability/threshold.py", "theory/stability/front_end_output.md",
        "theory/stability/lipschitz_e_output.md", "theory/stability/roots_holder_output.md", "theory/stability/threshold_output.md",
        "theory/stability/threshold_results.json", "theory/stability/blind/blind_pipeline.py", "theory/stability/blind/PROTOCOL.md",
        "theory/stability/blind/RESULT.md", "theory/stability/blind/result.json",
        "theory/pte/pte_common.py", "theory/pte/witnesses.py", "theory/pte/structure.py", "theory/pte/growth.py",
        "theory/pte/real_shapes.py", "theory/pte/search_T3_control.py", "theory/pte/search_T3.c", "theory/pte/search_T3_modular.py",
        "theory/pte/search_T3_modular.c", "theory/pte/pencil_search.py", "theory/pte/data/witnesses.json",
        "theory/pte/data/orbifold_pairs.md", "theory/pte/data/T3_modular.json", "theory/pte/data/pencil_N130_200.json",
        "theory/pte/data/pencil_m4_N220.json", "theory/pte/data/pencil_log.txt", "theory/pte/output/growth.txt",
        "theory/pte/output/pencil_search.txt", "theory/pte/output/real_shapes.txt", "theory/pte/output/search_T3_control.txt",
        "theory/pte/output/search_T3_modular.txt", "theory/pte/output/structure.txt", "theory/pte/output/witnesses.txt",
        "theory/msep/verify.py", "theory/eigen/eigen_common.py",
        "theory/varcurv/quadratic_form.py", "theory/varcurv/top_coefficient.py", "theory/varcurv/linear_part.py",
        "theory/varcurv/obstruction_check.py", "theory/varcurv/twisted_mp.py", "theory/varcurv/*_output.txt",
        "theory/diophantine/ranks.py", "theory/diophantine/cubic_group.py", "theory/diophantine/data/ranks.txt",
        "theory/diophantine/data/groups.csv",
        "numerics/geometry.py", "numerics/theory.py", "numerics/eigdata.py", "numerics/solve.py", "numerics/validate.py",
        "numerics/validate_committed.py", "numerics/heat_trace.py", "numerics/rerun_double_window.py", "numerics/fetch_refs.sh",
        "numerics/legacy/s3_repro.py", "numerics/legacy/single_window.py",
        "numerics/data/eigenvalues_*.csv", "numerics/data/convergence.csv", "numerics/data/bolza_benchmark.csv",
        "numerics/data/weyl.csv", "numerics/data/heat_trace_checks.csv", "numerics/data/heat_trace_difference.csv",
        "numerics/data/fits.csv", "numerics/data/headline.json", "numerics/data/heat_kernel_diagonal.npz",
        "numerics/data/rerun_double_window_comparison.json", "numerics/data/double_window/*",
        "numerics/moduli/quad.py", "numerics/moduli/geodesics.py", "numerics/moduli/trace_formula.py",
        "numerics/moduli/solve_moduli.py", "numerics/moduli/analysis.py", "numerics/moduli/validate_committed.py",
        "numerics/moduli/locality_ratio.py", "numerics/moduli/check_geodesics_s3.py", "numerics/moduli/kernel.py",
        "numerics/moduli/run_server.sh", "numerics/moduli/env/requirements.txt", "numerics/moduli/env/environment.yml",
        "numerics/moduli/data/convergence.csv", "numerics/moduli/data/eigenvalue_flow_orbifold.csv",
        "numerics/moduli/data/eigenvalue_flow_sectors.csv", "numerics/moduli/data/geometries.json",
        "numerics/moduli/data/heat_traces.csv", "numerics/moduli/data/length_spectra.csv",
        "numerics/moduli/data/s3_geodesic_check.csv", "numerics/moduli/data/s3_repro.json", "numerics/moduli/data/summary.json",
        "numerics/moduli/data/trace_differences.csv", "numerics/moduli/data/weyl.csv",
        "figures/gen/common.py", "figures/gen/gen_f4_area_classes.py", "figures/gen/gen_f7_strata.py", "figures/gen/gen_f8_recovery.py",
        "figures/src/figlib.py", "figures/src/common_import.py", "figures/src/F[1-8].py", "figures/src/pillow_mesh.py",
        "figures/src/quad_mesh.py", "figures/src/render_pillow.py", "figures/src/blender_jobs.py",
        "figures/style/figstyle.py", "figures/style/colourtools.py", "figures/style/blender_palette.py",
        "figures/style/fetch_third_party.py", "figures/style/palette.json", "figures/style/third_party/*",
        "figures/data/f4_*.csv", "figures/data/f7_*.csv", "figures/data/f8_*.csv",
        "figures/out/F[1-8].pdf", "figures/out/F[1-8].png",
    ]] + [
        ("theory/revision/check_lemma25.*", "checks/proofs/"), ("theory/revision/check_remark412.*", "checks/proofs/"),
        ("theory/revision/check_thm12iii.*", "checks/proofs/"), ("theory/revision/check_descent.*", "checks/proofs/"),
        ("theory/revision/check_thm513.*", "checks/proofs/"), ("theory/revision/check_remark212.*", "checks/proofs/"),
        ("theory/revision/check_prop610.*", "checks/proofs/"), ("theory/revision/check_sharpness.*", "checks/proofs/"),
        ("theory/revision/collision_witnesses.csv", "checks/proofs/collision_witnesses.csv"),
        ("review/audit/diophantine/enum_4800.txt", "checks/classes4800/enum_4800.txt"),
        ("review/audit/threshold/tab_enum_reference.txt", "checks/enumeration6000/tab_enum_reference.txt"),
        ("review/round1-fixes/a1_fig2_kmult.py", "checks/pairs/a1_fig2_kmult.py"),
        ("review/round1-fixes/d1_pencil_counts.py", "checks/pairs/d1_pencil_counts.py"),
        ("review/round1-fixes/d2_explicit_pairs.py", "checks/pairs/d2_explicit_pairs.py"),
        ("review/round1-fixes/output/*", "checks/pairs/output/"),
        ("review/audit-2/pte-witnesses/check_direct4.c", "checks/witnesses4/check_direct4.c"),
        ("review/audit-2/pte-witnesses/check_direct4.py", "checks/witnesses4/check_direct4.py"),
        ("review/audit-2/pte-witnesses/check_direct4.txt", "checks/witnesses4/check_direct4.txt"),
        ("review/audit-2/pte-witnesses/heatlib.py", "checks/witnesses4/heatlib.py"),
        ("review/audit-2/pte-witnesses/direct4_N440.txt", "checks/witnesses4/direct4_N440.txt"),
        ("review/audit-2/pte-witnesses/direct4_N440.time", "checks/witnesses4/direct4_N440.time"),
        ("review/audit-2/stability/check_setup.py", "checks/stability-constants/check_setup.py"),
        ("review/audit-2/stability/check_setup.txt", "checks/stability-constants/check_setup.txt"),
        ("review/audit-2/stability/stab610.py", "checks/stability-constants/stab610.py"),
        ("paper/jga/tools/make_tables.py", "tools/make_tables.py"),
        ("code/json_equal.py", "tools/json_equal.py"),
    ],
    post=[a_post],
    subs=[("theory/revision/", "checks/proofs/"), ("review/round1-fixes/", "checks/pairs/"),
          ("table written to supplement.tex", "table written to supplement_tables.tex"),
          ("markers for table pairs not found in supplement.tex", "markers for table pairs not found in supplement_tables.tex"),
          ("Q-birationally (variety_checks.py, check 3c, asserts the map and its inverse)", "Q-birationally"),
          ("review/audit-2/pte-witnesses/", "checks/witnesses4/"), ("review/audit-2/stability/", "checks/stability-constants/")],
    edits={
        "tools/make_tables.py": A_TABLE_EDITS,
        "checks/proofs/check_thm513.py": [('os.path.join(ROOT, "review", "audit", "diophantine", "enum_4800.txt")',
                                          'os.path.join(ROOT, "checks", "classes4800", "enum_4800.txt")', 1)],
        "checks/pairs/d2_explicit_pairs.py": [('SUPP = ROOT / "paper" / "jga" / "supplement.tex"', 'SUPP = ROOT / "tables" / "supplement_tables.tex"', 1)],
        "checks/witnesses4/check_direct4.py": [("HERE + '/../statements/pte-witnesses.md'", "HERE + '/pencil_configurations.md'", 1)],
        "checks/pairs/a1_fig2_kmult.py": [('"""A1 (referee round 1, reviewer d m1): recompute every dot of Fig. 2 (F4) from scratch.',
                                          '"""Recompute every dot of Figure 3 (F4) from scratch.', 1)],
        "checks/pairs/d1_pencil_counts.py": [('"""D1 (referee round 1, reviewers b m9, c m6, d m6a): recount the pencil witnesses of Remark 3.2.',
                                             '"""Recount the pencil witnesses of Remark 3.2.', 1)],
        "checks/pairs/d2_explicit_pairs.py": [
            ('SUPP = ROOT / "paper" / "jga" / "supplement.tex"', 'SUPP = ROOT / "tables" / "supplement_tables.tex"', 1),
            ('"""D2 (referee round 1, reviewer d m6b, c P6): the explicit pairs behind Example 3.12 and Fig. 2.',
             '"""The explicit pairs behind Example 3.17 and Figure 3 (Table S1).', 1),
            ("paper/jga/supplement.tex (squares", "tables/supplement_tables.tex (squares", 1),
            (" (round 4, n28: rows L <= 5)", " (rows L <= 5)", 1)],
        "checks/proofs/check_descent.py": [('"""Task 5(a) (G7-4a): rank 0', '"""Theorem 5.8 and Section S7: rank 0', 1),
                                          ("Checks every step of descent.tex in exact arithmetic.", "Checks every step of the descent in exact arithmetic.", 1)],
        "checks/proofs/check_lemma25.py": [('"""Task 1 (G7-3): Lemma 2.5 for every order, from the elliptic term of the trace formula.',
                                           '"""Lemmas 2.6-2.10 and Remark 2.9 for every order, from the elliptic term of the trace formula.', 1),
                                          ("Checks every computational claim of theory/revision/lemma25.tex.", "Checks every computational claim of these statements.", 1)],
        "checks/proofs/check_prop610.py": [('"""Task 5(d) (G7-4d): explicit r_rem and |dM| bounds of Proposition 6.10, checkable from the paper.',
                                           '"""Explicit r_rem and |dM| bounds of Proposition S3.5, checkable from the paper.', 1),
                                          ("Re-implements Proposition 6.10 from the formulas printed in prop610.tex ONLY",
                                           "Re-implements Proposition S3.5 from the formulas printed in the paper ONLY", 1)],
        "checks/proofs/check_remark212.py": [('"""Task 5(c) (G7-4c): Remark 2.12 (divergence of the heat series).  Checks remark212.tex.',
                                             '"""The divergence of the heat series (Section 4).', 1),
                                            ("re:\\s*\\(the manuscript's claim; theory/divergence/STATUS\\.md says l <= 5\\)", "", 1)],
        "checks/proofs/check_remark412.py": [('"""Task 2: the corrected Remark 4.12.  Checks the computational content of remark412.tex.',
                                             '"""The moments alpha_k and the remainders (Propositions 2.7 and B.2).', 1)],
        "checks/proofs/check_sharpness.py": [('"""Task 7 (G7-7): the corrected sharpness statement.  Checks sharpness.tex.',
                                             '"""The sharpness statements (Propositions 6.3 and 6.4).', 1)],
        "checks/proofs/check_thm12iii.py": [('"""Task 4 (G7-8): the explicit constant of Theorem 1.2(iii).  Checks thm12iii.tex.',
                                            '"""The explicit constant C_hyp of Lemma 2.5.', 1)],
        "checks/proofs/check_thm513.py": [('"""Task 5(b) (G7-4b): the collision-free sums of Theorem 5.13, as a checkable certificate.',
                                          '"""The collision-free sums of Proposition S2.1, as a checkable certificate.', 1),
                                         ('os.path.join(ROOT, "review", "audit", "diophantine", "enum_4800.txt")',
                                          'os.path.join(ROOT, "checks", "classes4800", "enum_4800.txt")', 1)],
        "checks/stability-constants/stab610.py": [("Written from the statements in review/audit-2/statements/stability.md only (G5-bis, blind).",
                                                  "Written from the statements of the paper only, independently of theory/stability/.", 1)],
        "numerics/moduli/locality_ratio.py": [
            ('"""Two numbers quoted in round 4 (paper/jga, Section 4 and supplement S4, S6), from committed data only.',
             '"""Two numbers quoted in the paper (Section 4 and supplement S4, S6), from committed data only.', 1),
            ("lem:hypbound of paper/jga (lem:hyp of paper/eigen)", "Lemma 2.5 of the paper", 1)],
        "tools/json_equal.py": [("Used by run_all.sh for", "Used by the make steps for", 1)],
    },
    clean=["theory/pte/search_T3_modular", "theory/pte/search_T3"],
    steps=PAPER_A_STEPS,
    data=[],     # filled below
    trace=[],    # filled below
)
PAPER_A["readme"] = PAPER_A_README + INSTALL.format(
    extra=", a C compiler (`cc` and `clang`) and, for the PARI step, `cypari2`",
    pari_install="\n.venv/bin/pip install --only-binary :all: -r requirements-pari.txt",
    t_verify="{t_verify}", t_full="{t_full}", t_figures="{t_figures}", t_tables="{t_tables}", t_all="{t_all}") + """
## Optional components

- **NGSolve** (`requirements-optional.txt`, Python 3.13): the finite-element re-solve of the eigenvalue
  problems (`numerics/rerun_double_window.py`, about an hour). Set `PYTHON_NUMERICS` to its interpreter.
  Every check of the committed eigenvalue data runs without it. The original solves (`numerics/solve.py`,
  `numerics/moduli/solve_moduli.py` with `run_server.sh`) are included as the programs that produced the data.
- **Blender** (tested with 5.2.2): the renders of Figures 1 and 4 (`figures/src/F1.py`, `F6.py`), run in a
  scratch copy so that the committed PDFs are not replaced (a raster render is not byte-reproducible across
  machines). Their data assertions run without Blender.
- **PARI/GP** (`requirements-pari.txt`): the rank of $C_{{27/2}}$.
- Without any of these, the corresponding steps are skipped with a message.
- `numerics/validate.py` rebuilds the committed eigenvalue tables from the solver's raw output, which is not
  included (several GB); `numerics/fetch_refs.sh` fetches the published Bolza eigenvalues it compares with.

"""
REPOS["heat-invariants-orbifolds"] = PAPER_A

PAPER_A["data"] = [
    ("theory/audibility/sharpness_n5_N60.json", "`theory/audibility/sharpness_search.py 60`", "Theorem C, Remark 3.2"),
    ("theory/audibility/sharpness_n5_N120.json", "`theory/audibility/sharpness_search.py 120`", "Remark 3.2 ($n=5$, orders at most 120)"),
    ("theory/audibility/output/*", "the script of the same name in `theory/audibility/` (transcript)", "Theorems A-C, Lemma 3.1, Orlando's formula"),
    ("theory/cone-coefficients/verify_output.txt", "`theory/cone-coefficients/verify_cone_coefficients.py`", "Lemma 2.8"),
    ("theory/signatures/output/*", "the script of the same name in `theory/signatures/` (transcript)", "Lemmas 2.8, 2.10, 3.3, Theorem 3.4, Corollary 3.5, Theorem 3.13, Figure 3"),
    ("theory/locality/output/check_locality.txt", "`theory/locality/check_locality.py`", "Theorem 2.3, Lemma 2.4, Corollary 4.1"),
    ("theory/curvature/curvature_output.txt", "`theory/curvature/curvature_checks.py`", "Section 2.3 (curvature 0 and +1)"),
    ("theory/divergence/divergence_output.txt", "`theory/divergence/divergence.py`", "Section 4 (growth of the heat coefficients)"),
    ("theory/threshold/first_overlap_vs_collision.csv", "`theory/threshold/threshold.py`", "Theorems 5.4-5.7, Table S2, Figure 7"),
    ("theory/threshold/threshold_output.txt", "`theory/threshold/threshold.py` (transcript)", "Section 5, Proposition S2.2"),
    ("theory/stability/threshold_results.json", "`theory/stability/threshold.py`", "Section 6, Table S4, Figure 8"),
    ("theory/stability/blind/result.json", "`theory/stability/blind/blind_pipeline.py`", "Table S6 (blind recovery)"),
    ("theory/pte/data/witnesses.json", "`theory/pte/witnesses.py`", "Example 3.17, the bounds on $T(L)$, Figure 3, Table S1"),
    ("theory/pte/data/T3_modular.json", "`theory/pte/search_T3_modular.py 220 4`", "Remark 3.18"),
    ("theory/pte/data/pencil_N130_200.json", "`theory/pte/pencil_search.py`", "Lemma 3.16 and the text after it"),
    ("theory/pte/data/pencil_m4_N220.json", "`theory/pte/pencil_search.py` (degree-4 pencil to 220)", "Remark 3.2 (pencil witnesses)"),
    ("theory/pte/data/pencil_log.txt", "`theory/pte/pencil_search.py` (log)", "Lemma 3.16"),
    ("theory/pte/output/*", "the script of the same name in `theory/pte/` (transcript)", "Section 3.3, Theorem 3.14, Remark 3.18"),
    ("theory/varcurv/*_output.txt", "the script of the same name in `theory/varcurv/` (transcript)", "Propositions 2.11 and 2.13, Remark 2.12"),
    ("theory/diophantine/data/ranks.txt", "`theory/diophantine/ranks.py` (PARI)", "Theorem 5.8 (rank and torsion of $C_{27/2}$)"),
    ("checks/proofs/*.txt", "the script of the same name in `checks/proofs/` (transcript)", "Lemmas 2.5-2.10, Remark 2.9, Theorem 5.8, Proposition S2.1, Proposition S3.5, Proposition 6.3"),
    ("checks/proofs/collision_witnesses.csv", "`checks/proofs/check_thm513.py`", "Proposition S2.1 (the collision witnesses)"),
    ("checks/classes4800/enum_4800.txt", "the second enumeration of the companion note (`enum_classes 10 4800 4800`)", "input of Proposition S2.1"),
    ("checks/enumeration6000/tab_enum_reference.txt", "listing of the triads with $10\\le S\\le18$", "Table S3 (reference listing)"),
    ("checks/pairs/output/a1_*", "`checks/pairs/a1_fig2_kmult.py`", "Figure 3 ($K_{\\rm mult}$ on the complete area classes)"),
    ("checks/pairs/output/d1_*", "`checks/pairs/d1_pencil_counts.py`", "Remark 3.2 and Section S1 (pencil counts)"),
    ("checks/pairs/output/d2_*", "`checks/pairs/d2_explicit_pairs.py`", "Table S1 and the cone lists of Section S1"),
    ("checks/witnesses4/direct4_N440.txt", "`checks/witnesses4/check_direct4.c` (`direct4 440`)", "Remark 3.2 ($n=4$, orders at most 440)"),
    ("checks/witnesses4/direct4_N440.time", "timing record of the search above", "Remark 3.2"),
    ("checks/witnesses4/check_direct4.txt", "`checks/witnesses4/check_direct4.py`", "Remark 3.2 (193 witnesses, 107 primitive)"),
    ("checks/stability-constants/check_setup.txt", "`checks/stability-constants/check_setup.py`", "Section S3 ($\\zeta_n$, $\\operatorname{sech}^2U$)"),
    ("numerics/data/eigenvalues_*.csv", "`numerics/solve.py` (NGSolve) and `numerics/validate.py`", "Section 4, Section S4, Table S6"),
    ("numerics/data/double_window/eigenvalues_*.csv", "`numerics/rerun_double_window.py` (NGSolve)", "Section S4 (double-window recomputation)"),
    ("numerics/data/double_window/problem_*.json", "`numerics/rerun_double_window.py` (NGSolve)", "Section S4 (provenance of the recomputation)"),
    ("numerics/data/rerun_double_window_comparison.json", "`numerics/rerun_double_window.py`", "Section S4 (agreement to $1.4\\times10^{-14}$)"),
    ("numerics/data/convergence.csv", "`numerics/validate.py`", "Table S5, Section S4"),
    ("numerics/data/bolza_benchmark.csv", "`numerics/validate.py`", "Section S4 (Bolza benchmark)"),
    ("numerics/data/weyl.csv", "`numerics/validate.py`", "Section S4 (Weyl check)"),
    ("numerics/data/heat_trace_checks.csv", "`numerics/heat_trace.py`", "Section S4 (heat traces)"),
    ("numerics/data/heat_trace_difference.csv", "`numerics/heat_trace.py`", "Section 4, Figures 1 and 5"),
    ("numerics/data/fits.csv", "`numerics/heat_trace.py`", "Section 4 (fitted coefficients)"),
    ("numerics/data/headline.json", "`numerics/heat_trace.py`", "Section 4 and S4 (quoted values)"),
    ("numerics/data/heat_kernel_diagonal.npz", "`numerics/heat_trace.py kernel` (NGSolve)", "Figure 1"),
    ("numerics/moduli/data/*", "`numerics/moduli/solve_moduli.py` (NGSolve) and `numerics/moduli/analysis.py`", "Section 4, Theorem 4.2, Section S6, Figures 4 and 5"),
    ("figures/data/f4_*.csv", "`figures/gen/gen_f4_area_classes.py`", "Figure 3"),
    ("figures/data/f7_*.csv", "`figures/gen/gen_f7_strata.py`", "Figure 7"),
    ("figures/data/f8_*.csv", "`figures/gen/gen_f8_recovery.py`", "Figure 8"),
    ("figures/out/F1.*", "`figures/src/F1.py` (Blender)", "Figure 1"),
    ("figures/out/F3.*", "`figures/src/F3.py`", "Figure 2"),
    ("figures/out/F4.*", "`figures/src/F4.py`", "Figure 3"),
    ("figures/out/F6.*", "`figures/src/F6.py` (Blender)", "Figure 4"),
    ("figures/out/F5.*", "`figures/src/F5.py`", "Figure 5"),
    ("figures/out/F2.*", "`figures/src/F2.py`", "Figure 6"),
    ("figures/out/F7.*", "`figures/src/F7.py`", "Figure 7"),
    ("figures/out/F8.*", "`figures/src/F8.py`", "Figure 8"),
    ("figures/style/palette.json", "fixed input (colour palette)", "every figure (style)"),
    ("figures/style/third_party/*", "fetched colour tables (`figures/style/fetch_third_party.py`; `SOURCES.json` gives sources and licences)", "every figure (colour maps)"),
    ("tables/*.tex", "`tools/make_tables.py` (S2-S4) and `checks/pairs/d2_explicit_pairs.py` (S1)", "Tables S1-S4"),
    ("theory/diophantine/data/groups.csv", "the S <= 4800 enumeration of the companion note", "Section 5 (cross-check of the collision fibres for $S\\le600$)"),
]


# ============================================================================================== Paper B
def b_post(dest, root):
    tex = (root / "paper/eigen/manuscript.tex").read_text(encoding="utf-8")
    blocks = list(re.finditer(r"% BEGIN GENERATED TABLE (\S+)\n.*?% END GENERATED TABLE \1\n?", tex, re.S))
    assert sorted(m.group(1) for m in blocks) == ["inputs", "practice", "spectra"], [m.group(1) for m in blocks]
    (dest / "tables").mkdir(exist_ok=True)
    (dest / "tables" / "paper_tables.tex").write_text(
        "% The generated tables of the paper (Table 4 inputs, Table 5 spectra, Table 6 practice), each between its\n"
        "% markers, as printed. tools/make_tables.py regenerates them.\n\n" + "".join(m.group(0) for m in blocks),
        encoding="utf-8")
    import subprocess, sys
    r = subprocess.run([sys.executable, "tools/make_tables.py", "--check"], cwd=dest, capture_output=True, text=True)
    assert r.returncode == 0, "tools/make_tables.py does not reproduce the paper's tables: " + r.stdout + r.stderr


PAPER_B_STEPS = [
    dict(name=f"{s}", targets=["verify"], dir="theory/eigen", cmd=f"$PYTHON {s}.py", minutes=m) for s, m in [
        ("counting", 2.5), ("remainder", 2), ("theorem_e", 1.2), ("necessity", 0.1), ("diameter", 3.5), ("systole_233", 0.6),
        ("instances", 1.6), ("practice", 1.5), ("practice_double_window", 0.2)]
] + [
    dict(name="bounded cone orders (Theorem 3.2, from the companion paper)", targets=["verify"], dir="theory/msep", cmd="$PYTHON verify.py", minutes=3.5),
    dict(name="computed spectra: committed data", targets=["verify"], dir="numerics", cmd="$PYTHON validate_committed.py --quick", minutes=0.2),
    dict(name="moduli family: committed data", targets=["verify"], dir="numerics/moduli", cmd="$PYTHON validate_committed.py --quick", minutes=0.1),
    dict(name="double-window recomputation: record", targets=["verify"], dir="numerics", cmd="$PYTHON rerun_double_window.py --verify-record", minutes=0.1),
    dict(name="tables 4-6", targets=["tables"], dir=".", cmd="$PYTHON tools/make_tables.py --check", minutes=0.1),
    dict(name="figure data E2 E3", targets=["figures"], dir=".", cmd="$PYTHON figures/gen/gen_e2_gap.py && $PYTHON figures/gen/gen_e3_practice.py", minutes=1.6),
] + [dict(name=f"figure {f}", targets=["figures"], dir=".", cmd=f"$PYTHON figures/src/{f}.py", minutes=0.1) for f in ("E1", "E2", "E3")] + [
    dict(name="figure data E1: eigenvalues of O(2,3,m) (NGSolve)", targets=["figures"], dir=".",
         cmd="$PYTHON_NUMERICS figures/gen/gen_e1_cusp.py", minutes=3, needs="ngsolve"),
    dict(name="computed spectra: full validation", targets=["full"], dir="numerics", cmd="$PYTHON validate_committed.py", minutes=0.3),
    dict(name="moduli family: full validation", targets=["full"], dir="numerics/moduli", cmd="$PYTHON validate_committed.py", minutes=0.6),
    dict(name="computed spectra: double-window re-solve (NGSolve)", targets=["full"], dir="numerics",
         cmd='$PYTHON_NUMERICS rerun_double_window.py --no-record "$LOGDIR/rerun"', minutes=60, needs="ngsolve"),
]

PAPER_B_README = """# Finitely many eigenvalues determine the signature of a hyperbolic orbifold: code and data

This repository reproduces every computation stated in the paper

> {authors}, *{paper}*.

The paper proves that finitely many Laplace eigenvalues determine the signature of a closed hyperbolic
2-orbifold with bounded cone orders, with explicit constants, and applies an a-posteriori test to computed
spectra. The repository contains:

- `theory/eigen/`: the checks of the counting and remainder bounds (`counting.py`, `remainder.py`), the
  diameter bound and Table 2 (`diameter.py`), Theorem E and Table 3 (`theorem_e.py`), the necessity of the
  hypotheses (`necessity.py`), the systoles of $\\mathcal O(2,3,m)$ (`systole_233.py`), the inputs of the test
  (`instances.py`), the test itself (`practice.py`) and its rerun on the double-window spectra with one
  eigenvalue missing or duplicated (`practice_double_window.py`); `theory/eigen/METHODS.md` documents the
  numerical methods;
- `theory/msep/verify.py`: the bounded-order theorem used from the companion paper;
- `numerics/`: the finite-element eigenvalues of the triangle orbifolds $\\mathcal O(2,8,8)$ and
  $\\mathcal O(3,3,12)$ (`solve.py`, NGSolve), their validation, and the double-window recomputation
  (`rerun_double_window.py`); `numerics/moduli/`: the spectra of the family $(0;3,3,3,3)$ (`solve_moduli.py`);
- `figures/`: Figures 1-3 (`figures/src/E*.py`, data generators in `figures/gen/`);
- `tools/make_tables.py`: Tables 4-6 (`tables/paper_tables.tex`).

{ndata} data files, {total} in all (`DATA.md`).

"""
PAPER_B = dict(
    name="eigenvalues-orbifold-signature",
    short="the paper",
    paper=PAPER_B,
    keywords=["Laplace eigenvalues", "hyperbolic orbifolds", "inverse spectral problems", "Selberg trace formula",
              "a-posteriori test", "finite element method", "cone singularities"],
    zenodo_description=("<p>Code and data for the paper <em>Finitely many eigenvalues determine the signature of a hyperbolic "
                        "orbifold</em>: the checks of the counting, remainder and diameter bounds and of the constants of "
                        "Theorem E (at 40 digits), the a-posteriori test on computed spectra, the finite-element eigenvalues of "
                        "the triangle orbifolds O(2,8,8) and O(3,3,12) with their double-window recomputation, the spectra of a "
                        "moduli family, the figures and the tables. <code>make verify</code> reruns the fast checks and "
                        "<code>make all</code> everything; DATA.md lists every data file with its checksum, producing script "
                        "and paper element, and TRACE.md maps every checkable item of the paper to its script.</p>"),
    optional_env=NGSOLVE_ENV,
    copy=[(p, None) for p in [
        "theory/eigen/eigen_common.py", "theory/eigen/diameter.py", "theory/eigen/counting.py", "theory/eigen/remainder.py",
        "theory/eigen/theorem_e.py", "theory/eigen/necessity.py", "theory/eigen/instances.py", "theory/eigen/practice.py",
        "theory/eigen/practice_double_window.py", "theory/eigen/systole_233.py",
        "theory/eigen/data/*", "theory/msep/verify.py",
        "numerics/solve.py", "numerics/geometry.py", "numerics/eigdata.py", "numerics/theory.py", "numerics/heat_trace.py",
        "numerics/validate_committed.py", "numerics/rerun_double_window.py", "numerics/validate.py", "numerics/fetch_refs.sh",
        "numerics/legacy/single_window.py",
        "numerics/data/eigenvalues_*.csv", "numerics/data/double_window/*", "numerics/data/rerun_double_window_comparison.json",
        "numerics/data/convergence.csv", "numerics/data/bolza_benchmark.csv", "numerics/data/weyl.csv",
        "numerics/data/heat_trace_checks.csv", "numerics/data/heat_trace_difference.csv", "numerics/data/fits.csv",
        "numerics/data/headline.json",
        "numerics/moduli/solve_moduli.py", "numerics/moduli/quad.py", "numerics/moduli/analysis.py", "numerics/moduli/geodesics.py",
        "numerics/moduli/trace_formula.py", "numerics/moduli/validate_committed.py", "numerics/moduli/run_server.sh",
        "numerics/moduli/env/requirements.txt", "numerics/moduli/env/environment.yml",
        "numerics/moduli/data/convergence.csv", "numerics/moduli/data/eigenvalue_flow_sectors.csv",
        "numerics/moduli/data/eigenvalue_flow_orbifold.csv", "numerics/moduli/data/geometries.json",
        "numerics/moduli/data/summary.json", "numerics/moduli/data/length_spectra.csv", "numerics/moduli/data/weyl.csv",
        "numerics/moduli/data/heat_traces.csv", "numerics/moduli/data/trace_differences.csv",
        "numerics/moduli/data/s3_geodesic_check.csv", "numerics/moduli/data/s3_repro.json",
        "figures/gen/common.py", "figures/gen/gen_e1_cusp.py", "figures/gen/gen_e2_gap.py", "figures/gen/gen_e3_practice.py",
        "figures/src/figlib.py", "figures/src/common_import.py", "figures/src/E[1-3].py",
        "figures/style/figstyle.py", "figures/style/colourtools.py", "figures/style/palette.json", "figures/style/third_party/*",
        "figures/style/fetch_third_party.py",
        "figures/data/e1_*.csv", "figures/data/e2_gap.csv", "figures/data/e3_practice.csv",
        "figures/out/E[1-3].pdf", "figures/out/E[1-3].png",
        "numerics/moduli/kernel.py", "numerics/moduli/check_geodesics_s3.py",
    ]] + [("paper/eigen/tools/make_tables.py", "tools/make_tables.py")],
    extra={"theory/eigen/METHODS.md": "eigen_METHODS.md"},
    post=[b_post],
    edits={
        "tools/make_tables.py": [
            ("ROOT = Path(__file__).resolve().parents[3]", "ROOT = Path(__file__).resolve().parents[1]", 1),
            ('TEX = ROOT / "paper" / "eigen" / "manuscript.tex"', 'TEX = ROOT / "tables" / "paper_tables.tex"', 1),
            ('"""Regenerate the data tables of paper/eigen/manuscript.tex from committed data.',
             '"""Regenerate the data tables of the paper (tables/paper_tables.tex) from committed data.', 1),
            ("    python3 paper/eigen/tools/make_tables.py ", "    python3 tools/make_tables.py ", 2),
            ("# round 4 close-out: printed also when est <= N_c", "# printed also when est <= N_c", 1),
        ],
    },
    steps=PAPER_B_STEPS,
)
PAPER_B["readme"] = PAPER_B_README + INSTALL.format(
    extra="", pari_install="", t_verify="{t_verify}", t_full="{t_full}", t_figures="{t_figures}",
    t_tables="{t_tables}", t_all="{t_all}") + """
## Optional components

- **NGSolve** (`requirements-optional.txt`, Python 3.13): the finite-element re-solve of the triangle
  spectra (`numerics/rerun_double_window.py`, about an hour) and the eigenvalues of $\\mathcal O(2,3,m)$ for
  Figure 3 (`figures/gen/gen_e1_cusp.py`, which watches memory with macOS's `memory_pressure`). Set
  `PYTHON_NUMERICS` to its interpreter. Without it these steps are skipped with a message; every check of the
  committed eigenvalue data runs in the core environment. The original solves (`numerics/solve.py` and
  `numerics/moduli/solve_moduli.py` with `run_server.sh`) are included as the programs that produced the data;
  `numerics/validate.py` rebuilds the eigenvalue tables from the solver's raw output, which is not included.

"""
REPOS["eigenvalues-orbifold-signature"] = PAPER_B
PAPER_B["data"] = [
    ("theory/eigen/data/instances.csv", "`theory/eigen/instances.py`", "Table 4 (systoles, diameters, the bound D)"),
    ("theory/eigen/data/practice.csv", "`theory/eigen/practice.py`", "Table 6, Figure 2"),
    ("theory/eigen/data/practice_inputs.csv", "`theory/eigen/practice.py`", "Table 4"),
    ("theory/eigen/data/practice_t.csv", "`theory/eigen/practice.py`", "Section 7 (the test at every grid time)"),
    ("theory/eigen/data/triangle_spectra_first41.csv", "`theory/eigen/practice.py`", "Table 5"),
    ("theory/eigen/data/table2.csv", "`theory/eigen/practice.py`", "Table 3 (constants of Theorem E)"),
    ("theory/eigen/data/practice_double_window.csv", "`theory/eigen/practice_double_window.py`", "Section 7.1 (the test on the double-window spectra)"),
    ("theory/eigen/data/practice_missing.csv", "`theory/eigen/practice_double_window.py`", "Section 7.1 (one eigenvalue missing or duplicated)"),
    ("numerics/data/eigenvalues_*.csv", "`numerics/solve.py` (NGSolve) and `numerics/validate.py`", "Tables 4-6, Section 7.1, Lemma 2.2 checks"),
    ("numerics/data/double_window/eigenvalues_*.csv", "`numerics/rerun_double_window.py` (NGSolve)", "Section 7.1 (double-window recomputation)"),
    ("numerics/data/double_window/problem_*.json", "`numerics/rerun_double_window.py` (NGSolve)", "Section 7.1 (provenance of the recomputation)"),
    ("numerics/data/rerun_double_window_comparison.json", "`numerics/rerun_double_window.py`", "Section 7.1 (agreement of the two computations)"),
    ("numerics/data/convergence.csv", "`numerics/validate.py`", "Section 7.1 (error estimates)"),
    ("numerics/data/bolza_benchmark.csv", "`numerics/validate.py`", "Section 7.1 (benchmark)"),
    ("numerics/data/weyl.csv", "`numerics/validate.py`", "Section 7.1 (completeness, Weyl check)"),
    ("numerics/data/heat_trace_checks.csv", "`numerics/heat_trace.py`", "Section 7.1 (heat-trace check of completeness)"),
    ("numerics/data/heat_trace_difference.csv", "`numerics/heat_trace.py`", "input of the full validation"),
    ("numerics/data/fits.csv", "`numerics/heat_trace.py`", "input of the full validation"),
    ("numerics/data/headline.json", "`numerics/heat_trace.py`", "input of the full validation"),
    ("numerics/moduli/data/*", "`numerics/moduli/solve_moduli.py` (NGSolve) and `numerics/moduli/analysis.py`", "Tables 4 and 6, Figure 2 (the family)"),
    ("figures/data/e1_*.csv", "`figures/gen/gen_e1_cusp.py` (NGSolve)", "Figure 3"),
    ("figures/data/e2_gap.csv", "`figures/gen/gen_e2_gap.py`", "Figure 1"),
    ("figures/data/e3_practice.csv", "`figures/gen/gen_e3_practice.py`", "Figure 2"),
    ("figures/out/E2.*", "`figures/src/E2.py`", "Figure 1"),
    ("figures/out/E3.*", "`figures/src/E3.py`", "Figure 2"),
    ("figures/out/E1.*", "`figures/src/E1.py`", "Figure 3"),
    ("figures/style/palette.json", "fixed input (colour palette)", "every figure (style)"),
    ("figures/style/third_party/*", "fetched colour tables (`figures/style/fetch_third_party.py`; `SOURCES.json` gives sources and licences)", "every figure (colour maps)"),
    ("tables/*.tex", "`tools/make_tables.py`", "Tables 4-6"),
]
PAPER_B["trace"] = [
    ("Lemma 2.2", "counting bound for closed geodesics; the hyperbolic term", "`theory/eigen/counting.py`", "counting"),
    ("Proposition 2.3", "enveloping remainders", "`theory/eigen/remainder.py`", "remainder"),
    ("Theorem 3.2", "separation with bounded cone orders (from the companion paper)", "`theory/msep/verify.py`", "bounded cone orders (Theorem 3.2, from the companion paper)"),
    ("Lemma 3.3", "integrality at the first difference", "`theory/eigen/theorem_e.py`", "theorem_e"),
    ("Lemmas 4.1-4.3", "hyperbolic trigonometry, separation of cone points, area of balls", "`theory/eigen/diameter.py`", "diameter"),
    ("Theorem 4.4, Table 2", "the diameter bound $D(A,\\varepsilon,M)$ and its values (40 digits)", "`theory/eigen/diameter.py`", "diameter"),
    ("Lemma 5.1, Proposition 5.2", "elementary bounds; counting and tails", "`theory/eigen/counting.py`", "counting"),
    ("Lemma 6.1", "the gap", "`theory/eigen/theorem_e.py`", "theorem_e"),
    ("Theorem 6.2, Table 3", "Theorem E and its constants (40 digits)", "`theory/eigen/theorem_e.py`", "theorem_e"),
    ("Figure 1", "the separation mechanism on $\\mathcal O(2,8,8)$", "`figures/gen/gen_e2_gap.py`, `figures/src/E2.py`", "figure data E2 E3; figure E2"),
    ("Theorem 7.1, Table 4", "the inputs of the test: systoles, diameters, $D$", "`theory/eigen/instances.py`, `tools/make_tables.py`", "instances; tables 4-6"),
    ("Table 5", "the first 40 eigenvalues of the triangle orbifolds", "`theory/eigen/practice.py`, `tools/make_tables.py`", "practice; tables 4-6"),
    ("Table 6", "results of the test", "`theory/eigen/practice.py`, `tools/make_tables.py`", "practice; tables 4-6"),
    ("Section 7.1", "the computed spectra: error estimates, completeness, benchmark", "`numerics/validate_committed.py`", "computed spectra: committed data; computed spectra: full validation"),
    ("Section 7.1", "the family $(0;3,3,3,3)$: spectra and their checks", "`numerics/moduli/validate_committed.py`", "moduli family: committed data; moduli family: full validation"),
    ("Section 7.1", "double-window recomputation of the triangle spectra; agreement", "`numerics/rerun_double_window.py`", "double-window recomputation: record; computed spectra: double-window re-solve (NGSolve)"),
    ("Section 7.1", "the test on the recomputed spectra; one eigenvalue missing or duplicated", "`theory/eigen/practice_double_window.py`", "practice_double_window"),
    ("Figure 2", "eigenvalue counts against the systole", "`figures/gen/gen_e3_practice.py`, `figures/src/E3.py`", "figure data E2 E3; figure E3"),
    ("Lemma 8.1", "Jørgensen's inequality (commutator trace, 40 digits)", "`theory/eigen/diameter.py`", "diameter"),
    ("Proposition 8.2", "the family $\\mathcal O(2,3,m)$: area, systoles", "`theory/eigen/diameter.py`, `theory/eigen/systole_233.py`", "diameter; systole_233"),
    ("Equation (3), Propositions 8.3 and 8.5, Remark 8.4", "Rayleigh identities; unbounded orders; pinching", "`theory/eigen/necessity.py`", "necessity"),
    ("Figure 3", "eigenvalues of $\\mathcal O(2,3,m)$", "`figures/gen/gen_e1_cusp.py` (NGSolve), `figures/src/E1.py`", "figure E1; figure data E1: eigenvalues of O(2,3,m) (NGSolve)"),
]
GLOBAL_SUBS.append(("the revised paper", "the paper"))

PAPER_A["trace"] = [
    ("Figure 1", "heat-kernel diagonal of $\\mathcal O(2,8,8)$ and $\\mathcal O(3,3,12)$", "`figures/src/F1.py` (Blender)", "figures F1 F6: data assertions; figure F1: Blender render (scratch copy)"),
    ("Theorem 1.2(ii), Theorem 3.8, Corollary 3.9", "bounded cone orders: $M+1$ invariants suffice and are attained; sharp pairs; minimal areas $12\\pi$, $36\\pi$", "`theory/msep/verify.py`", "bounded cone orders (Theorem 3.8)"),
    ("Theorem 2.3, Lemma 2.4", "terms of the trace formula; counting bound", "`theory/locality/check_locality.py`", "trace formula terms (locality)"),
    ("Lemma 2.5", "the constant $C_{\\rm hyp}$", "`checks/proofs/check_thm12iii.py`", "proof check check_thm12iii"),
    ("Lemmas 2.6, 2.8, 2.10, Proposition 2.7, Remark 2.9", "$\\Phi_m$, cone polynomials $p_l$, moments $\\alpha_k$, agreement with Uçar for $l\\le40$", "`checks/proofs/check_lemma25.py`, `checks/proofs/check_remark412.py`, `theory/cone-coefficients/verify_cone_coefficients.py`, `theory/signatures/heat_structure.py`", "proof check check_lemma25; proof check check_remark412; cone coefficients p_l; heat structure of a signature"),
    ("Section 2.3", "curvature $0$ and $+1$", "`theory/curvature/curvature_checks.py`", "flat and spherical cases"),
    ("Proposition 2.11, Remark 2.12", "variable curvature: $\\beta_{l,l+1}$ for $l\\le7$, the $t^3$ coefficient, the linear part (833 cases)", "`theory/varcurv/top_coefficient.py`, `theory/varcurv/twisted_mp.py`, `theory/varcurv/linear_part.py`", "variable curvature top_coefficient; variable curvature twisted_mp; variable curvature linear_part"),
    ("Proposition 2.13", "second variation $\\omega_n$; flat-cone examples", "`theory/varcurv/quadratic_form.py`, `theory/varcurv/obstruction_check.py`", "variable curvature quadratic_form; variable curvature obstruction_check"),
    ("Lemma 3.1, Theorem A", "parity; $n$ invariants determine $n$ orders", "`theory/audibility/verify_elimination.py`", "Theorem A and Lemma 3.1: elimination"),
    ("Equation (orlando)", "Orlando's formula, $n\\le7$", "`theory/audibility/orlando_check.py`", "Orlando's formula"),
    ("Theorem B", "the linear system and its determinant, $n\\le8$", "`theory/audibility/linear_system.py`, `theory/stability/lipschitz_e.py`", "Theorem B: the linear system; stability: Lipschitz constants"),
    ("Theorem C", "$\\{2,8,8\\},\\{3,3,12\\}$ and $\\{3,10,15,30\\},\\{4,5,21,28\\}$", "`theory/audibility/sharpness_search.py`", "Theorem C and Remark 3.2: sharpness search N=60"),
    ("Remark 3.2", "$n=4$, orders at most 440: 193 witnesses, 107 primitive; six not from a pencil", "`checks/witnesses4/check_direct4.c`, `checks/witnesses4/check_direct4.py`", "degree-4 witnesses to 440: analysis; degree-4 witnesses to 440: search from scratch"),
    ("Remark 3.2", "pencil witnesses: 17 (14 primitive) to 130, 49 (30) to 220", "`checks/pairs/d1_pencil_counts.py`", "pencil witness counts"),
    ("Remark 3.2", "$n=5$: no witness with orders at most 120", "`theory/audibility/sharpness_search.py`", "Remark 3.2: no witness for n=5 with orders <= 120"),
    ("Lemma 3.3", "padding and genus reduction", "`theory/signatures/heat_structure.py`", "heat structure of a signature"),
    ("Theorem 3.4, Figure 2", "separation of signatures", "`theory/signatures/genus.py`, `figures/src/F3.py`", "genus separation; figure F3"),
    ("Corollary 3.5, Theorem 3.13", "cone count $n\\le{\\rm Area}/\\pi+4$; constructions", "`theory/signatures/cone_count.py`", "cone count"),
    ("Example 3.6", "$(1;15)$ and $(0;3,3,5,5)$ share exactly two invariants", "`theory/pte/witnesses.py`", "PTE witnesses"),
    ("Theorem 3.11", "the Descartes bound", "`theory/pte/structure.py`", "PTE structure"),
    ("Proposition 3.12, Proposition A.2", "doubling and shift identities", "`theory/pte/structure.py`", "PTE structure"),
    ("Theorem 3.14, Proposition 3.15, Lemma A.1", "growth bounds; constructions for $L\\le7$", "`theory/pte/growth.py`", "PTE growth"),
    ("Lemma 3.16", "no 4-configuration of size 10 of the stated form with entries at most 200", "`theory/pte/pencil_search.py`", "PTE pencil_search"),
    ("Example 3.17, bounds on $T(L)$", "explicit pairs sharing exactly $L$ invariants", "`theory/pte/witnesses.py`, `checks/pairs/d2_explicit_pairs.py`", "PTE witnesses; explicit pairs (Table S1)"),
    ("Figure 3", "the 525 complete area classes and $K_{\\rm mult}$", "`theory/signatures/area_classes.py`, `figures/gen/gen_f4_area_classes.py`, `figures/src/F4.py`, `checks/pairs/a1_fig2_kmult.py`", "complete area classes; figure data F4 F7 F8; figure F4; K_mult on the complete area classes"),
    ("Remark 3.18", "no genus pair of size 8 with five-element side at most 220; real partners", "`theory/pte/search_T3_modular.py`, `theory/pte/search_T3_control.py`, `theory/pte/real_shapes.py`", "PTE T3 modular record; PTE T3 modular search to 220; PTE search_T3_control; PTE real_shapes"),
    ("Corollary 4.1", "dimension of the zero set", "`theory/locality/check_locality.py`", "trace formula terms (locality)"),
    ("Figure 4, Section 4", "the moduli family: 8 members, systoles, $\\lambda_1$", "`numerics/moduli/validate_committed.py`, `figures/src/F6.py` (Blender)", "moduli family: committed data; moduli family: full validation; figures F1 F6: data assertions; figure F6: Blender render (scratch copy)"),
    ("Theorem 4.2", "the locality bound overestimates by $4.4\\times10^6$ to $1.0\\times10^{10}$", "`numerics/moduli/locality_ratio.py`", "locality bound: overestimation ratios"),
    ("Section 4, Figure 5", "computed spectra and heat traces; the first two coefficients of the difference of traces recovered", "`numerics/validate_committed.py`, `figures/src/F5.py`", "computed spectra: committed data; computed spectra: full validation; figure F5"),
    ("Section 4", "growth of the heat coefficients", "`checks/proofs/check_remark212.py`, `theory/divergence/divergence.py`", "proof check check_remark212; divergence of the heat coefficients"),
    ("Figure 6", "tilings of the triangle orbifolds", "`figures/src/F2.py`", "figure F2"),
    ("Lemmas 5.2-5.3, Theorems 5.4-5.7", "chambers, first overlaps, thresholds", "`theory/threshold/threshold.py`", "first overlap and first collision (Section 5)"),
    ("Figure 7", "strata of the first two invariants", "`figures/gen/gen_f7_strata.py`, `figures/src/F7.py`", "figure data F4 F7 F8; figure F7"),
    ("Theorem 5.8", "the isolation of $\\{(2,8,8),(3,3,12)\\}$: descent, torsion, points", "`checks/proofs/check_descent.py`", "proof check check_descent"),
    ("Theorem 5.8", "rank 0 of $C_{27/2}$ (PARI `ellrank`)", "`theory/diophantine/ranks.py`", "rank of C_{27/2} (PARI ellrank)"),
    ("Proposition 6.1", "the front end; amplification factors", "`theory/stability/front_end.py`", "stability: front end"),
    ("Theorem 6.2, Propositions 6.3-6.4", "stability exponents; sharpness", "`theory/stability/roots_holder.py`, `checks/proofs/check_sharpness.py`", "stability: Hoelder exponents of roots; proof check check_sharpness"),
    ("Figure 8, Section 6", "thresholds and recovery sweeps", "`theory/stability/threshold.py`, `figures/gen/gen_f8_recovery.py`, `figures/src/F8.py`", "stability thresholds and certificates; figure data F4 F7 F8; figure F8"),
    ("Proposition B.2", "enveloping remainders", "`checks/proofs/check_lemma25.py`, `checks/proofs/check_remark412.py`", "proof check check_lemma25; proof check check_remark412"),
    ("Table S1", "the explicit pairs", "`checks/pairs/d2_explicit_pairs.py`", "explicit pairs (Table S1); supplement table S1 (pairs)"),
    ("Section S1", "the complete area classes: 33 946 signatures", "`theory/signatures/area_classes.py`, `figures/gen/gen_f4_area_classes.py`", "complete area classes; figure data F4 F7 F8"),
    ("Proposition S2.1", "38 collision-free sums with $18\\le S\\le4800$; the collision witnesses", "`checks/proofs/check_thm513.py`", "proof check check_thm513"),
    ("Proposition S2.2", "tangency gaps", "`theory/threshold/threshold.py`", "first overlap and first collision (Section 5)"),
    ("Table S2", "first overlap against first collision", "`tools/make_tables.py`", "supplement tables S2-S4"),
    ("Table S3", "the 83 triads with $10\\le S\\le18$", "`tools/make_tables.py`", "supplement tables S2-S4"),
    ("Section S3", "Lemma S3.1 and Theorems S3.2-S3.4: conditioning and constants", "`theory/stability/lipschitz_e.py`, `theory/stability/roots_holder.py`", "stability: Lipschitz constants; stability: Hoelder exponents of roots"),
    ("Section S3", "$\\zeta_3,\\zeta_4,\\zeta_5=1,79/3,14048/15$; ${\\rm sech}^2U$ for $(2,2,2,2,3)$", "`checks/stability-constants/check_setup.py`", "stability constants zeta_n and sech^2 coefficients"),
    ("Proposition S3.5", "the certificate", "`theory/stability/threshold.py`, `checks/proofs/check_prop610.py`", "stability thresholds and certificates; proof check check_prop610"),
    ("Table S4", "thresholds, certificates, ratios", "`tools/make_tables.py` (from `threshold_results.json`)", "supplement tables S2-S4; stability thresholds and certificates"),
    ("Section S4, Table S5", "method, levels, error estimates, validation, the fitted coefficients", "`numerics/validate_committed.py` (data from `numerics/solve.py`, `numerics/validate.py`)", "computed spectra: committed data; computed spectra: full validation"),
    ("Section S4", "double-window recomputation agrees to $1.4\\times10^{-14}$", "`numerics/rerun_double_window.py`", "double-window recomputation: record; computed spectra: double-window re-solve (NGSolve)"),
    ("Section S5, Table S6", "blind recovery from the computed spectra", "`theory/stability/blind/blind_pipeline.py`", "blind recovery from the computed spectra"),
    ("Section S6", "the moduli family: errors, traces, length spectra", "`numerics/moduli/validate_committed.py`, `numerics/moduli/locality_ratio.py`", "moduli family: committed data; moduli family: full validation; locality bound: overestimation ratios"),
    ("Section S7", "the 2-isogeny descent of $C_{27/2}$ by hand", "`checks/proofs/check_descent.py`", "proof check check_descent"),
]

# Data files changed on purpose by the text edits above (label or comment wording only; the build
# asserts that line endings are unchanged and that no other data file differs from its source).
_PALETTE = "comment field: a note on an internal decision gate removed"
NOTE["edited_data"] = {
    "checks/classes4800/check_enum.txt": "check labels: internal register tags removed",
    "checks/enumeration6000/check_enum.txt": "check labels: internal register tags removed",
    "checks/enumeration6000/tab_enum_reference.txt": "header comment reworded",
    "checks/note/check_note.txt": "check label: 'the G5 enumeration' -> 'the third enumeration'",
    "figures/style/palette.json": _PALETTE,
    "theory/diophantine/data/growth_fits.txt": "section header: 'audit' -> 'check'",
}
NOTE["generated_data"] = ["tables/*.tex"]
PAPER_B["edited_data"] = {"figures/style/palette.json": _PALETTE}
PAPER_B["generated_data"] = ["tables/*.tex"]
PAPER_A["edited_data"] = {
    "checks/enumeration6000/tab_enum_reference.txt": "header comment reworded",
    "checks/pairs/output/d2_explicit_pairs.txt": "output file name: supplement.tex -> supplement_tables.tex",
    "checks/pairs/output/d2_pairs.csv": "recipe column: reference to an internal proof note -> [paper]",
    "checks/proofs/check_descent.txt": "check labels: reference to an internal draft -> the paper",
    "checks/proofs/check_lemma25.txt": "check labels: references to internal notes -> the paper, Ucar's thesis",
    "checks/proofs/check_prop610.txt": "check label: reference to an internal note -> Section 2 of the paper",
    "figures/style/palette.json": _PALETTE,
    "theory/pte/data/pencil_log.txt": "header: reference to an internal proof note -> the paper",
    "theory/pte/data/witnesses.json": "recipe strings: references to internal proof notes -> [paper]",
    "theory/pte/output/witnesses.txt": "recipe strings: references to internal proof notes -> [paper]",
    "theory/signatures/output/area_classes.txt": "timing line: absolute interpreter path -> python3",
    "theory/signatures/output/cone_count.txt": "timing line: absolute interpreter path -> python3",
    "theory/signatures/output/genus.txt": "timing line: absolute interpreter path -> python3",
    "theory/signatures/output/heat_structure.txt": "timing line: absolute interpreter path -> python3",
    "theory/varcurv/linear_part_output.txt": "label: 'attacker b_4' -> 'independent b_4'",
}
PAPER_A["generated_data"] = ["tables/*.tex"]

# Measured step times (minutes) from the fresh-copy tests of 2026-10-11 (TEST-REPORT.md, the longer of
# the verify and all runs); make help and the READMEs state these. Steps not timed keep their estimate.
MEASURED = {'equal-sum-reciprocal-triples': {'committed data consistent': 0.05, 'curves of the pencil': 0.02, 'families and dual pairs': 2.35, 'growth fits': 0.55, 'exponent fits': 1.25, 'ranks (PARI ellrank)': 0, 'note checks, with the enumeration 4801..6000': 0.95, 'sums with a primitive class': 0, 'the point 3P': 0, 'classes to 4800, second program': 0.22, 'group law on the curves': 1.37, '2-isogeny descents (PARI points)': 0, 'isosceles family': 0.15, 'conic-bundle family': 0.02, 'enumeration to 6000, third program': 0.08, 'enumeration to 4800 from scratch (enumerate_fast)': 1.2, 'second program from scratch to 4800': 0.65, 'third program from scratch to 6000': 2.45, 'figure 1 (F9)': 0.12, 'tables 1 and 2': 0}, 'eigenvalues-orbifold-signature': {'counting': 1.7, 'remainder': 1.17, 'theorem_e': 0.68, 'necessity': 0.03, 'diameter': 2.15, 'systole_233': 0.45, 'instances': 1.32, 'practice': 0.87, 'practice_double_window': 0.08, 'bounded cone orders (Theorem 3.2, from the companion paper)': 1.95, 'computed spectra: committed data': 0.08, 'moduli family: committed data': 0.02, 'double-window recomputation: record': 0, 'computed spectra: full validation': 0.18, 'moduli family: full validation': 0.3, 'figure data E2 E3': 0.75, 'figure E1': 0.1, 'figure E2': 0.02, 'figure E3': 0.02, 'tables 4-6': 0}, 'heat-invariants-orbifolds': {"Orlando's formula": 0.05, 'Theorem B: the linear system': 0.12, 'Theorem A and Lemma 3.1: elimination': 1.03, 'Theorem C and Remark 3.2: sharpness search N=60': 0.17, 'cone coefficients p_l': 0.02, 'heat structure of a signature': 0.02, 'cone count': 0.23, 'complete area classes': 0.4, 'genus separation': 1.37, 'trace formula terms (locality)': 0.12, 'stability: front end': 0, 'stability: Lipschitz constants': 0, 'stability: Hoelder exponents of roots': 0.03, 'blind recovery from the computed spectra': 0.22, 'stability constants zeta_n and sech^2 coefficients': 0.3, 'first overlap and first collision (Section 5)': 0.28, 'flat and spherical cases': 0.03, 'rank of C_{27/2} (PARI ellrank)': 0, 'computed spectra: committed data': 0.08, 'moduli family: committed data': 0.02, 'locality bound: overestimation ratios': 0, 'double-window recomputation: record': 0, 'proof check check_lemma25': 0.15, 'proof check check_remark412': 0.02, 'proof check check_thm12iii': 0.02, 'proof check check_descent': 0, 'proof check check_thm513': 0.02, 'proof check check_remark212': 0.03, 'proof check check_prop610': 0.02, 'proof check check_sharpness': 0.02, 'PTE structure': 0.05, 'PTE growth': 0, 'PTE witnesses': 0.08, 'PTE real_shapes': 1.08, 'PTE search_T3_control': 4.6, 'PTE pencil_search': 2.43, 'PTE T3 modular record': 0, 'PTE T3 modular search to 220': 1.52, 'bounded cone orders (Theorem 3.8)': 1.92, 'variable curvature quadratic_form': 0.03, 'variable curvature top_coefficient': 0.38, 'variable curvature linear_part': 0.4, 'variable curvature obstruction_check': 0.02, 'variable curvature twisted_mp': 1.5, 'K_mult on the complete area classes': 0.23, 'pencil witness counts': 0.03, 'explicit pairs (Table S1)': 0.63, 'degree-4 witnesses to 440: analysis': 0, 'Remark 3.2: no witness for n=5 with orders <= 120': 3.57, 'stability thresholds and certificates': 4.05, 'divergence of the heat coefficients': 3.85, 'computed spectra: full validation': 0.17, 'moduli family: full validation': 0.27, 'degree-4 witnesses to 440: search from scratch': 4.18, 'figure data F4 F7 F8': 0.63, 'figure F2': 0.08, 'figure F3': 0.02, 'figure F4': 0.02, 'figure F5': 0.02, 'figure F7': 0.02, 'figure F8': 0.02, 'figures F1 F6: data assertions': 0.02, 'figure F1: Blender render (scratch copy)': 0.2, 'figure F6: Blender render (scratch copy)': 0.38, 'supplement tables S2-S4': 0, 'supplement table S1 (pairs)': 0.58}}
