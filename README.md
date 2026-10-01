# How much of a hyperbolic orbifold does heat hear?

Manuscript, proofs, exact-arithmetic verification and numerical data for the paper on how many
leading heat-trace coefficients of a closed hyperbolic 2-orbifold determine its cone orders (and,
at three cone points, the orbifold itself). Target journal: *The Journal of Geometric Analysis*.

## Reproduce everything with one command

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
PYTHON=.venv/bin/python code/run_all.sh --quick      # every stage under about ten minutes
PYTHON=.venv/bin/python code/run_all.sh --full       # every stage, including the long searches
```

`code/run_all.sh` runs every check in the repository from the committed data: the arithmetic harness
(`code/`), the theory checks (`theory/`), and the checks of the committed numerics (`numerics/`). It prints
PASS, FAIL or SKIP with a reason for each stage and its time, and exits nonzero if any stage fails. A stage
also fails if it changes a committed file: regenerating an output has to reproduce it byte for byte, and the
original is restored. Missing optional dependencies skip only the stages that need them, with an install
message (NGSolve for the re-solve, PARI for the rank certification); the checks of committed CSV data never
need NGSolve. The mode `--list` prints the stages, `--only REGEX` runs a subset.

Everything above needs only `requirements.txt` (sympy, mpmath, numpy, scipy, pinned). Re-solving the
eigenvalue problems needs `numerics/requirements.txt` (Python 3.13, NGSolve 6.2.2607); the rank
certification needs `theory/diophantine/requirements-pari.txt` (cypari2 2.2.4, PARI/GP 2.17.2).

## Layout

| Path | Contents |
|---|---|
| `paper/` | `main.tex` (the manuscript; not modified by the consolidation), `build/main.pdf`, `tables/` (generated LaTeX tables) |
| `code/` | the arithmetic verification harness and `run_all.sh`; `legacy/` holds the co-author's recovered original scripts (`legacy/PROVENANCE.md`) |
| `theory/` | one directory per theorem, each with proof, status, attack log, checking scripts and their outputs: `audibility/` (Theorem A: cone orders are audible), `cone-coefficients/`, `signatures/` (general signatures), `locality/` (heat invariants do not see moduli), `stability/` (recovery under errors, blind recovery), `threshold/` (closed-form first overlap), `curvature/` (flat and spherical comparison), `divergence/` (growth of the cone coefficients), `diophantine/` (the degeneracy variety and the growth of the count); `CONVENTIONS.md` is the one notation with a translation table from every file, checked by `conventions_check.py`; `definitions.tex` states the definitions |
| `numerics/` | the finite-element eigenvalue computation for the triangles `(2,8,8)` and `(3,3,12)` (Neumann and Dirichlet), the heat-trace comparison, validation (`validate_committed.py` runs from the committed data), and `moduli/`, the experiment on the moduli family `(0;3,3,3,3)`; `solve.py` is the one eigensolver (double-window slicing), `legacy/` the retired single-window routine, `rerun_double_window.py` the comparison of the two |
| `data/` | the enumeration of two-coefficient degeneracies for `S ≤ 600` (Table 1 and the density table) |
| `review/` | `DEFECTS.md` (the single ledger of defects, with owner and status), the literature notes (`literature/`, `hyperresearch/`), `outstanding-fetches.md` (sources not retrieved, with the accepted gaps), the claim ledger and the audit records |
| `research/`, `refs/` | the literature vault and the bibliography source |
| `admin/` | `build_data_manifest.py`, which writes `DATA-MANIFEST.md` |
| `figures/` | (empty until the figure session) |
| `DATA-MANIFEST.md` | every committed data file: size, SHA-256, generating script and command, and the paper element that uses it; figures F1 to F9 with the status of their data |
| `CONSOLIDATION.md` | what was moved, renamed or changed in the consolidation, and why |

## Current state

`review/DEFECTS.md` lists every open item with its owner. The theorems of `theory/` are proved and their
checks pass under `code/run_all.sh`; the manuscript text has not yet been brought into line with them
(that is the rewrite session), and the figures are not yet drawn (`DATA-MANIFEST.md` flags the figures
whose data is incomplete).

## Credits

The original verification scripts are the co-author's work, and are kept in this repository: the
repository-root scripts `advanced_pillow_verification.py`, `enumerate_degeneracies.py`,
`generate_latex_supplementary_table.py` and `run_all.py`, and the recovered earlier versions in
`code/legacy/` (`arithmetic verification.py`, `table_data.py` and their outputs). They come from
<https://github.com/Ali-M658/Arithmetic-verification> (author `Ali-M658`; see `code/legacy/PROVENANCE.md` for
the recovery record). The harness in `code/` re-implements and cross-checks them, and `code/cross_check.py` compares against
the recovered originals in `code/legacy/`.
