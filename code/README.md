# Verification harness

Exact-arithmetic verification for *How Few Heat Invariants Determine a Hyperbolic Triangular
Pillow*. Every numerical, arithmetic and computational assertion in `paper/main.tex` that can be
checked by machine is checked here, and every check is an assertion that can fail.

## Requirements

- **Python 3.9 or newer.** Tested on CPython 3.14.2, macOS 15 arm64.
- `sympy` and `mpmath`, pinned in `requirements.txt`.

Only `verify_identities.py` needs those two packages. `orbifold_enum.py`,
`enumerate_degeneracies.py` and `make_table.py` are stdlib-only, so the arithmetic the manuscript's
claims rest on carries no third-party dependency.

```bash
python3 -m pip install -r requirements.txt
```

## Running everything

```bash
./run_all.sh
```

One command, five stages, in order. It checks for Python 3.9+ and for both packages **before**
running anything and exits with an install instruction rather than a traceback if either is
missing. It exits `0` only if every stage passes and nonzero otherwise, so it is safe to use as a
gate in CI or a pre-submission check.

Expect roughly **six to seven minutes** end to end on a current laptop; stage 2 and stage 5 dominate.
Set `PYTHON=/path/to/python` to choose an interpreter.

## Contents

| File | Depends on | What it does |
|---|---|---|
| `orbifold_enum.py` | stdlib | General *n*-cone orbifold enumerator. Exact invariants `R`, `S₁`, `P_k`, `χ_orb`, `Area/π`. Built for reuse at *n* = 4 and *n* = 5; no triple is hardcoded. Run it directly for its self-test. |
| `enumerate_degeneracies.py` | stdlib | Sweeps `10 ≤ S ≤ 600` for two-coefficient degeneracies keyed on the true signature `σ = (S₁, R)`. Emits both counting conventions, primitivity flags, and CSVs. |
| `make_table.py` | stdlib | Writes the manuscript's two tables to `paper/tables/` as self-contained LaTeX fragments. |
| `verify_identities.py` | sympy, mpmath | 19 checks over the displayed identities, each tagged with its claim ID from `review/claim-ledger.md`. |
| `cross_check.py` | stdlib | Three-way cross-validation: this harness against `review/audit-independent.py` and against `legacy/`. Reports disagreements; never silently prefers a source. |
| `run_all.sh` | — | Runs all of the above with a PASS/FAIL summary. |
| `legacy/` | — | Recovered prior work. See below and `legacy/PROVENANCE.md`. |

Outputs land in `data/` (CSV) and `paper/tables/` (LaTeX). Neither directory is an input to
anything; both are regenerated from scratch on every run.

## Reproducing each table

Both tables are written by `make_table.py`, which enumerates from scratch and never reads a stored
result:

```bash
python3 make_table.py
```

| Manuscript table | Generated file | Content |
|---|---|---|
| Table 1, `\label{tab:density}` | `paper/tables/table1.tex` | Cumulative degeneracy count `𝒩(S)` at `S` = 18, 100, …, 600 |
| Table 2, `\label{tab:enum}` | `paper/tables/table2.tex` | All 83 hyperbolic triads with `10 ≤ S₁ ≤ 18` and their exact `R` |
| — | `paper/tables/table1-both-conventions.tex` | Supplementary: both counting conventions side by side |

`table2.tex` reproduces the manuscript's printed Table 2 row for row, in the same order, with the
same `unique`/`collision` status column. **The collision rows are detected, never hardcoded**: a
triad is flagged exactly when its signature group at that sum has more than one member. If no
collision were detected at `S₁ = 18`, `make_table.py` raises rather than emit a table.

`main.tex` is not modified by any script here. Wiring the generated fragments in with
`\input{tables/table2}` is a separate editing step.

### A note on Table 1

The manuscript does not state whether `N(S)` counts colliding **pairs** or signature **classes**.
Its printed values follow the pairs convention. The two agree through `S = 100` and diverge from
`S = 200` on. `table1.tex` therefore uses pairs, matching the manuscript; the supplementary
fragment shows both. See `review/convention-note.md`.

## Reproducing each claim

```bash
python3 verify_identities.py
```

Each line of output is tagged with the claim IDs it discharges, so a result here maps directly onto
a row of `review/claim-ledger.md`.

| Claim IDs | What is verified | Range |
|---|---|---|
| `HC-02, HC-04, HC-05` | Vieta chain for `(z+1)^m − (z−1)^m`, exact integer coefficients | `2 ≤ m ≤ 200` |
| `HC-01, HC-03` | Lemma 2.1, cotangent sum, and the root identification `z_j = −i·cot(jπ/m)` | `2 ≤ m ≤ 200` |
| `HC-06, HC-07` | Proposition 2.2, cosecant sum | `2 ≤ m ≤ 200` |
| `HC-10` – `HC-13` | `cone(m) = (m²−1)/(12m)`; `cone(2)`, `cone(3)`, `cone(5)` | `2 ≤ m ≤ 200` |
| `CV-02` – `CV-05`, `AP-03` | The normalization `a₀(2,3,5) = 271/360 = 269/360 + 1/180` | — |
| `HC-16` – `HC-18` | `Σ cone(mᵢ) = (S₁−R)/12`, and the inversion `S₁ = 12a₀ + 2 − R` | all triads `S₁ ≤ 200` |
| `HC-19` | Remark 2.5: the mis-normalized inversion really is negative at `(2,3,5)` | — |
| `HC-22` – `HC-25` | eq. (5), the third-coefficient reduction, derived symbolically from eq. (4) | symbolic |
| `HC-26, HC-27` | `S₁R ≥ 9`, equality iff `p = q = r` | all triads `S₁ ≤ 200` |
| `HC-28` – `HC-32` | eq. (6), the full round trip `(p,q,r) → (R,S₁,P₃) → (p,q,r)`, denominator nonvanishing | all triads `S₁ ≤ 200` |
| `HC-33, HC-34` | The Jacobian determinant of Section 2.3, symbolically | symbolic |
| `TH-23` – `TH-25` | `φ_p`, `τ_p`, and unimodality with peak at `S = 3p+4` | symbolic + `2 ≤ p ≤ 11` |
| `TH-26` – `TH-34` | The three adjacent-pair comparisons for `S ≤ 17` | — |
| `TH-29, TH-35, TH-39` – `TH-41` | The four endpoint comparisons at `S = 18` | — |
| `TH-45` – `TH-47` | `P₃ = 1032 ≠ 1782` separates the collision pair | — |
| `DE-03` – `DE-05` | Proposition 5.1, the scaling law | 10 primitive bases, `k ≤ 20` |

The degeneracy counts and the growth exponent come from the separate sweep:

```bash
python3 enumerate_degeneracies.py          # full sweep to S = 600
python3 enumerate_degeneracies.py 120      # shorter sweep while iterating
```

It asserts the base case at `S = 18`, the primitive and scaled pairs at `S = 36`, the lower bound
`𝒩(S) ≥ ⌊S/18⌋`, and all six cumulative checkpoints, and exits nonzero on any mismatch.

## Design rules

These are enforced, not aspirational.

1. **No hardcoded fallback data.** If a search that must succeed returns nothing, the code raises.
   Nothing canned is ever printed as though it had been computed.
2. **No unconditional success messages.** Every claim is an `assert`. A script that cannot fail
   verifies nothing.
3. **Exact arithmetic throughout.** Integers and `fractions.Fraction`. Floating point appears in
   exactly one function, `power_law_exponent`, which is an empirical fit reported as evidence for a
   conjecture and is marked as such in a banner comment. The decimal columns in the LaTeX tables are
   rendered from exact `Fraction` values by integer arithmetic.
4. **Failure propagates.** A broken assertion fails its module, which fails `run_all.sh`, which
   exits nonzero.
5. **Disagreement is reported, not resolved.** `cross_check.py` compares three independent
   implementations and fails loudly if they differ, rather than picking one.

## The area convention

Gauss–Bonnet gives `Area = −2π·χ_orb`, which at *n* = 3 is `Area = 2π(1 − R)` — the manuscript's
eq. (1). A superseded upstream script used `Area = π(1 − R)`, wrong by a factor of two.
`orbifold_enum.selftest()` asserts the correct value *and* separately asserts that the incorrect
form is not being reproduced, so that regression cannot return silently.

## Prior work

`legacy/` contains four files recovered unmodified from the history of the upstream verification
repository, `https://github.com/Ali-M658/Arithmetic-verification`. **They are prior work by the
co-author**, who wrote every commit in that repository. `arithmetic verification.py` and
`table_data.py` group triads by the correct signature `(S₁, R)` and independently confirm
Theorem A, Theorem B and the `P₃` separation; `table_data.py` produced the content of the
manuscript's Table 2.

Those four files were deleted upstream on 2026-08-08 and replaced by scripts that verify none of
the manuscript's claims. They are preserved here as a third independent cross-check on the *n* = 3
results and are exercised on every run by `cross_check.py`. Full commit SHAs, timestamps and
recovery details are in `legacy/PROVENANCE.md`. **Do not modify them.**

## Independent oracle

`review/audit-independent.py` is a separate exact-rational re-derivation written during the
manuscript audit, before this harness existed. It is treated as read-only: `cross_check.py` runs it
as a subprocess and compares results. It is deliberately not imported and not refactored, so that
it stays genuinely independent of the code it checks.
