# numerics/legacy: retired code, kept for the record

Nothing under `numerics/` imports or runs anything in this directory except `s3_repro.py` itself.

| File | What it is | Why it is retired |
|---|---|---|
| `single_window.py` | the S3 eigenvalue routine `eigenvalues` (renamed `eigenvalues_single_window`), verbatim, and `run_single_window`, the old `solve.run` | Each shift-invert Lanczos slice certifies its window `(sigma - rho, sigma + rho)` from the `k` values ARPACK returns, so an eigenvalue ARPACK drops inside a window is lost without a warning (found in the moduli experiment, `moduli/REPORT.md` section 4a). Replaced by `solve.eigenvalues_robust`, in which every eigenvalue lies in two independent windows and the misses are counted and repaired. |
| `s3_repro.py` | the cross-machine rerun of the `(3,3,12)` Neumann problem with the old routine, run on the server | It documents that the old routine reproduced the committed eigenvalues on another machine; its record is `moduli/data/s3_repro.json` (committed data, never overwritten). The path to the old solver is the only change made to it in the consolidation (`legacy/` and `moduli/data/` paths fixed). |

The committed `numerics/data/eigenvalues_*.csv` were produced with the old routine. The four production
problems were rerun with the new one at the committed production settings; the comparison is
`numerics/data/rerun_double_window_comparison.json`, written by `numerics/rerun_double_window.py`, and is
discussed in `CONSOLIDATION.md`.
