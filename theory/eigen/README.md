# theory/eigen: from finitely many eigenvalues to the signature

The analytic theorem answering the referees' question: why count heat invariants, when no heat
invariant is computable from finitely many eigenvalues?

Start with `STATUS.md`. `STATEMENTS.md` has every new result without proofs, and `AUDIT.md` has the
blind audit.

| file | content |
|---|---|
| `diameter.tex` | Task 1. Cone separation (Lemma eig:sep), balls (eig:balls), diameter bound (Theorem eig:diam), the O(2,3,m) obstruction (Proposition eig:233) |
| `counting.tex` | Task 2. Elementary bounds, counting and tails, Hyp at all times, Theorem eig:count |
| `remainder.tex` | Task 3. Explicit remainders of the cone and area expansions |
| `theorem_e.tex` | Task 4. Integrality at the first difference, the gap, Theorem E, sizes |
| `necessity.tex` | Task 5. Unbounded orders (proved); small systole (partial; what is not proved) |
| `locality.tex` | Task 6. Theorem 4.4 with D(A, ε, M) in place of the diameter |
| `practice.md`, `data/practice*.csv`, `data/instances.csv`, `data/table2.csv`, `data/triangle_spectra_first41.csv` | Task 7. The a-posteriori test of Theorem 7.1 on the committed spectra: systole lower bounds by complete enumeration and diameter bounds (`instances.py`), criteria (C1) and (C2) on a fine time grid (`practice.py`) |
| `METHODS.md` | the numerical methods behind the committed spectra, with file:line references (for the paper's numerical-methods subsection) |
| `eigen_common.py` | shared exact (Fraction) and 30–80 digit (mpmath) routines |
| `diameter.py`, `counting.py`, `remainder.py`, `theorem_e.py`, `necessity.py`, `locality.py`, `instances.py`, `practice.py` | verification, one per task; every check is an `assert`-equivalent that raises, so a failure exits nonzero |
| `run.sh` | runs all eight scripts |
| `sources/` | fetched external sources, and the instrument gap |
| `audit/` | the blind reviewers' reports and code |

The fragments use the macros and labels of `paper/jga/manuscript.tex`. Their own labels start with
`eig:`.

Requirements: Python 3 with mpmath ≥ 1.3, sympy ≥ 1.12, numpy and scipy (instances.py, practice.py), in a virtual environment:

    python3 -m venv /path/to/venv && /path/to/venv/bin/pip install mpmath sympy numpy scipy
    PY=/path/to/venv/bin/python bash theory/eigen/run.sh

Run times on the development machine: diameter 110 s, counting 80 s, remainder 9 s, theorem_e
35 s, necessity 3 s, locality 2 s, instances 90 s, practice 170 s (practice needs scipy).
