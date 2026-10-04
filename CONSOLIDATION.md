# CONSOLIDATION: what was moved, renamed or changed, and why

Branch `s9b-consolidate`. The consolidation brings the work of the theory, numerics and Diophantine
sessions under one convention, one verification command, one eigensolver and one data manifest, and cleans
the review files. `paper/main.tex` and the mathematical content of every proof under `theory/` are
untouched. Every change below is either a new file, a move with fixed paths, or an edit to
documentation or to a ledger.

## 1. Conventions (`theory/CONVENTIONS.md`, `theory/conventions_check.py`)

New. One notation for the paper (`c_j` is the coefficient of `t^{j-2}`, `c_1 = Area/4π`; `b_l(m) = K^l p_l(m)/m`;
`σ(O) = (g; m)`; `K_iso`, `K_mult` over a class `𝒫`), a translation table from every file, and a table of every
symbol collision found with the paper's choice. The nine collisions that matter most:

| collision | resolution |
|---|---|
| numerics `c1, c2, c3` (coefficients of `D(t)`) vs heat coefficients `c_j` | `D(t)` coefficients are `d_j`; numerics `c1, c2, c3 = d_3, d_4, d_5` (`25/12`, `−1775/24`, `153025/48`) |
| `K`: curvature, `K_iso`/`K_mult`, `K(F)`, `K_n`/`K_g`, heat kernel, log exponent, function field | `K` is curvature only; the others are subscripted or renamed (`𝔥_t`, `𝔮`, `𝕂`) |
| `Δ`: Laplacian, Hurwitz determinant, genus difference, discriminant, triangle group | `Δ` is the Laplacian; `𝔇_j`, `δg`, `Disc`, `Γ(p,q,r)` |
| `H_ν` (stability, `t^ν`) vs `H_k = (c_1,…,c_k)` (definitions) | `H_ν = c_{ν+2}`; `H_k` is the tuple |
| `β_k` signed (locality) vs `β_ℓ` unsigned (divergence) | `β_ℓ = b_ℓ/K^ℓ > 0`, `b_ℓ = (−1)^ℓ β_ℓ` at `K = −1` |
| `α_l` per `Area` (signatures) vs `α_j` per `Area/4π` (stability, locality, numerics) | `α_j` per `Area/4π`; `α_l^sig = α_{l+1}/(4π)` |
| `σ(O) = (g; m)` vs `σ(p,q,r) = (S_1, R)` (`main.tex:279`) | `σ(O)` is the signature; the pair is `key_2(p,q,r)` |
| `κ`: curvature, condition number, monomial coefficient, log exponent | none is curvature; `cond(M)`, `amp_r`, `ϰ`, `𝔮` |
| `T`, `t`, `τ`, `λ`, `S`, `P_j`, `R`, `e_k` | see the table of section 4 of `CONVENTIONS.md` |

`conventions_check.py` recomputes the first four coefficients of `(2,8,8)`, `(3,3,12)`, `(3,10,15,30)`,
`(1;15)` and `(0;3,3,5,5)` from a retyped reference and from ten of the repository's own coefficient functions
through the translation, and asserts agreement (45 comparisons pass, 5 skip because a function is genus-0 or
triples only; the skipped cells are covered through its building blocks). It also asserts that every
replacement symbol is unused elsewhere in the repository. Nothing was renamed in the code: committed data
headers (`c1`, `c2` in `numerics/data`) keep their names.

## 2. One verification suite (`code/run_all.sh`)

Extended from six stages to 42 stages (see `--list`), quick and full modes, per-stage PASS/FAIL/SKIP with
time and reason, exit nonzero on any FAIL. New files: `requirements.txt` (pinned: sympy 1.14.0, mpmath 1.3.0,
numpy 2.5.3, scipy 1.18.1; `code/requirements.txt` now includes it), `code/data_guard.py` (a stage that changes
a committed file fails and the file is restored), `code/json_equal.py` (timing-field-aware comparison for the
sharpness JSON). New checking scripts, all read-only on committed data:

| file | what it checks from committed data |
|---|---|
| `numerics/validate_committed.py` | the numerics validation (geometry, convergence, Bolza benchmark, Weyl law, heat traces against the trace formula, `D(t)`, fits, headline) recomputed from `numerics/data/*.csv`; `numerics/validate.py` needs the uncommitted raw runs and rewrites the CSVs, so it is not in the suite |
| `numerics/moduli/validate_committed.py` | the moduli analysis `(0)`, `(a)`, `(c)` to `(g)` recomputed from `moduli/data/convergence.csv` and `length_spectra.csv`; the direct full-quadrilateral runs are not committed, so the symmetry reduction is asserted from its record |
| `theory/diophantine/check_committed.py` | `groups.csv` row by row, `per_S.csv` against it and against `data/degeneracies.csv`, and an independent recount at 146 sums |
| `numerics/rerun_double_window.py --verify-record` | the committed double-window comparison record, and that the committed eigenvalue CSVs still have the recorded hashes |

`numerics/eigdata.py` falls back to the committed CSV when the raw runs are absent (`table_committed`), which is
what lets the existing heat-trace code run without a solver. PARI-dependent `ranks.py` is skipped with a message
when `cypari2` is missing; the NGSolve re-solve is skipped when NGSolve is missing. Dependencies are checked
before any stage runs, with install commands.

### Stage table of `run_all.sh --quick` (from a clean working tree; timings taken under load)

The 1-minute load average exceeded 8 during the run (peak 38), so the times are wall-clock under load, not idle-machine times. Result: 34 passed, 0 failed, 8 skipped, total 11:31, exit 0.

| status | time | stage | note |
|---|---|---|---|
| PASS | 0:01 | code 1 enumerator self-test |  |
| PASS | 1:09 | code 2 displayed identities |  |
| PASS | 0:09 | code 3 degeneracy enumeration |  |
| PASS | 0:09 | code 4 LaTeX table generation |  |
| PASS | 1:04 | code 5 three-way cross-check |  |
| PASS | 0:00 | code 6 claim-ledger coverage |  |
| PASS | 0:01 | review DEFECTS.md is current |  |
| PASS | 0:23 | review defects-check |  |
| PASS | 0:00 | theory definitions-check |  |
| PASS | 0:03 | theory conventions-check |  |
| PASS | 0:00 | admin DATA-MANIFEST is current |  |
| PASS | 0:03 | audibility orlando_check |  |
| PASS | 0:06 | audibility linear_system |  |
| PASS | 0:42 | audibility verify_elimination |  |
| PASS | 0:08 | audibility sharpness N=60 |  |
| SKIP |  | audibility sharpness N=120 | full mode only: about 22 min |
| PASS | 0:01 | cone-coefficients verify |  |
| PASS | 0:01 | signatures heat_structure |  |
| PASS | 0:10 | signatures cone_count |  |
| PASS | 0:18 | signatures area_classes |  |
| PASS | 1:05 | signatures genus |  |
| PASS | 0:06 | locality check_locality |  |
| PASS | 0:00 | stability front_end |  |
| PASS | 0:01 | stability lipschitz_e |  |
| PASS | 0:02 | stability roots_holder |  |
| PASS | 0:01 | stability blind pipeline |  |
| SKIP |  | stability threshold | full mode only: 30-60 min counterexample search |
| PASS | 0:12 | threshold first overlap |  |
| PASS | 0:02 | curvature curvature_checks |  |
| SKIP |  | divergence divergence | full mode only: about 10 min |
| PASS | 0:03 | diophantine committed-data check |  |
| PASS | 0:01 | diophantine variety_checks |  |
| PASS | 0:21 | diophantine growth_fits |  |
| PASS | 1:27 | diophantine exponent_fits |  |
| PASS | 3:30 | diophantine families |  |
| SKIP |  | diophantine ranks (PARI) | PARI (cypari2) not installed (see the pre-flight note) |
| PASS | 0:05 | numerics validate (committed) |  |
| PASS | 0:01 | numerics moduli validate |  |
| SKIP |  | numerics S3 rerun record | rerun comparison record deferred to the final submission check |
| SKIP |  | numerics validate (full) | full mode only: heat traces and fits, a few minutes |
| SKIP |  | numerics moduli validate (full) | full mode only: trace formula for 8 members, about 5 min |
| SKIP |  | numerics S3 re-solve (NGSolve) | full mode only: about an hour; needs NGSolve |

The skips: seven stages are full-mode only (the `N = 120` sharpness search, `stability threshold`, `divergence`, the full numerics and moduli validations, the NGSolve re-solve) and are deferred with `--full`; `ranks.py` is skipped because PARI/cypari2 is not installed on this machine (its install message is printed); the rerun comparison record is deferred (section 3). Failure test: with one assertion in `code/orbifold_enum.py` changed (`2 * (1 - R)` to `3 * (1 - R)`) the stage `code 1 enumerator self-test` failed and `run_all.sh` exited 1; after restoring the file its SHA-256 (`358ded8f9a367160e9fc404a0642c933769e82fe00ff750ed8d220c8db18122d`) was identical to the original and `git status` was clean.


## 3. One eigensolver (`numerics/solve.py`)

`eigenvalues_robust` (every eigenvalue in two independent shift-invert windows; ARPACK misses counted and
repaired) moved from `numerics/moduli/solve_moduli.py` into `numerics/solve.py`, verbatim apart from its docstring and
the import of `slice_eigs`, which is now local. `solve.eigenvalues` is a wrapper with the old signature, so
`heat_trace.kernel` and the suites are unchanged; `solve.run` and the CLI default to the production `k = 200`
(the old default `160` was only reached by one-off runs; the suite always used 200). `moduli/solve_moduli.py` imports
the routine from `solve`. The old routine is `numerics/legacy/single_window.py`, unused, with
`numerics/legacy/README.md`; `moduli/s3_repro.py`, which exercises the old routine, moved to `numerics/legacy/s3_repro.py`
(paths fixed; `moduli/data/s3_repro.json` is committed data and was not rewritten).

**T3 status: verified by existing checks; full rerun deferred to the final submission check.** The brief asked for the four S3
production problems to be rerun with the double-window solver and compared with `numerics/data/eigenvalues_*.csv`. That
rerun was prepared (`numerics/rerun_double_window.py`: one problem at a time to a scratch directory, never `data/`; counts must
match exactly and values within the published `err_conservative`, with the first 500 below 1e-8 relative; it writes
`numerics/data/rerun_double_window_comparison.json` and `--verify-record` asserts that record) but was not run: the machine was
swapping under unrelated load and then rebooted, and the decision was taken not to start any FEM solve now. No rerun result exists
and none is claimed. The question the rerun answers (did the single-window routine drop an eigenvalue of the committed S3 data?)
is already answered by two independent pieces of evidence in the repository:

1. `numerics/REPORT.md` section 4d: the committed S3 heat traces agree with the exact Selberg identity plus elliptic terms to
   7e-13 (and `numerics/moduli/data/s3_geodesic_check.csv` with the geodesic terms included); a missing eigenvalue below about 1e4
   would show at 1e-7 or more. `numerics/validate_committed.py` re-asserts this from the committed CSVs inside `run_all.sh`.
2. `numerics/moduli/REPORT.md` section 4a and `numerics/moduli/data/s3_repro.json`: a server rerun of the (3,3,12) Neumann
   problem at the production settings reproduced all 1434 committed eigenvalues (count equal, maximum relative difference 1.0e-12,
   0.15 of the error estimate). That rerun used the old routine, so it shows the committed data are complete, not that the new
   routine agrees; the new routine's own check is the full rerun, deferred.

The double-window solver is the only solver under `numerics/`. `DATA-MANIFEST.md` lists the comparison record as DEFERRED, and the
`run_all.sh` stage `numerics S3 rerun record` is a SKIP with that reason until the record exists; `--full` includes the NGSolve rerun
stage (`numerics S3 re-solve (NGSolve)`), which writes nothing under `data/`.

**`run_all.sh --full` was not run in this consolidation** (deferred to the final submission check). The full-only stages are the
`N = 120` sharpness search, `stability/threshold.py` (30 to 60 min), `divergence.py`, the full numerics validations and the NGSolve
re-solve. The `--quick` stages already reproduce their committed outputs at smaller scope.

## 4. Data manifest (`DATA-MANIFEST.md`, `admin/build_data_manifest.py`)

New. Every committed data file with size, SHA-256, generator and command, and paper element; figures F1 to F9 with
the status of their data; environment specifications. `run_all.sh` fails if it is out of date, so a data file
cannot be committed without being described. Figures whose data is missing or incomplete: F4 (a per-class table: only a text transcript exists), F7 (the stratum intervals are not stored; only `S*(p)`), F8 (the recovery-error sweep was never computed; only thresholds and two recovered specimens). All three are marked "to be generated in the figure stage"; F2 and F3 need no data file.

## 5. Housekeeping

* `review/outstanding-fetches.md`: the union merge had left two `1.9` sections and the Watson item twice. Items are
  now numbered `1.1` to `1.10`; the second Watson attempt is folded into `1.1`; four items that were retrieved after
  all moved to a "Retrieved after all" group (`R.1` to `R.4`); a new "Accepted gaps" table at the top lists the five
  items that will not be chased (Steinig 1971, Drury–Marshall 1987, Donnelly 1976, Watson 2005, Shioda for the
  Shioda–Tate rank source), each with the reason it is not load-bearing. No fact was deleted.
* `review/DEFECTS.md` (regenerated from `review/build_defects.py`, the single source): every row owned by S1 or S3 to
  S8 is now closed by merged work (MAJ-02 by the audibility theorem, MAJ-05 by the stability front end, MIN-06 by the
  `n = 5` search to order 120, MIN-11 by the literature sweep) or reassigned to S11 (rewrite) or S14 (submission),
  with the evidence added to its note; 12 rows closed, 48 open (S10: 1, S11: 20, S14: 27). FAT-02 now records that
  the growth conjecture itself is contradicted by the Diophantine data.
* `README.md`: current layout, the one command, credit for the original verification scripts to the co-author.
* `numerics/REPORT.md`: a note that the single-window routine it describes is superseded, and the new reproduce line. The FAT-02 note in `DEFECTS.md` cites the revised Diophantine growth statement (conjecture `N(S) = S^(1+o(1))`, empirical `kappa = 4.5 +/- 0.5`; `theory/diophantine/RECOMMENDATION.md`), superseding the earlier 5.3.

## 6. Observations not acted on

* `numerics/validate.py` still needs the raw solver runs and the Bolza reference list (`numerics/refs_cache/`, fetched
  from the network); it was left as the way to regenerate the tables, and is not part of the suite.
* `theory/stability/threshold.py` and `theory/threshold/threshold.py` share a file name (kept; cited with their directory).
* Several committed outputs are transcripts that include wall-clock times (`verify_elimination.txt` ends with `[496.8s]`);
  the suite compares reproduction by assertion, not by transcript.
* The paper's `rem:ncone`, definition of `K` and Theorem C still say what `DEFECTS.md` FAT-01 says they say; that is the
  rewrite session's work.

### Clean-clone check

A fresh clone of `origin/s9b-consolidate` at `5458773` (the commit before this record) was run with `code/run_all.sh --quick` (interpreter: the pinned-requirements venv; no NGSolve, no PARI). Exit code **0**: 34 passed, 0 failed, 8 skipped, total 11:58 (1-minute load average 9 to 12 at the end; earlier in the run higher, so times are under load). The stage table is identical in status to the table above; times: longest stages: 1:18 code 2 displayed identities; 1:15 code 5 three-way cross-check; 1:16 signatures genus; 1:23 diophantine exponent_fits; 2:52 diophantine families. The clone was deleted after the run.
