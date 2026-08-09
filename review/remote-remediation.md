# Remote remediation plan

**This is a plan document. Nothing in it has been executed.** No remote is configured on this
repository, nothing has been pushed, and no upstream file has been altered. Collaborator access to
`Ali-M658/Arithmetic-verification` is pending; this is the sequence to run once it arrives.

Upstream HEAD at the time of writing: **`bb3a18a`**.

---

## 1. Why this is needed

Four claims in the manuscript — `DE-13`, `AP-13`, `AP-18`, `AP-19` — assert that verification code
is *available in the public repository*. A referee following the URL today finds four scripts that
verify none of the paper. See [reproducibility-report.md](reproducibility-report.md) §3.

The remediation is not "write code" — that is done, in `code/`. It is "publish it, and remove what
actively misleads".

---

## 2. Files to DELETE from upstream

Each is named individually with the reason it fails. None is salvageable by patching; each is
superseded by a file in `code/`.

### 2.1 `enumerate_degeneracies.py` — delete

Two independent, disqualifying defects.

1. **It computes the wrong invariant.** It keys collisions on `(1 − R, Σ mᵢ⁻², (pqr)⁻²)`. The
   manuscript's two-coefficient signature is `σ = (S₁, R)` with `S₁ = p + q + r`. **The script never
   computes `S₁` anywhere.** A degeneracy in the manuscript's sense is therefore outside what this
   code can find.
2. **It emits fabricated data.** When its search returns nothing — which it does at the default
   bound — it falls through to a hardcoded `sample_rows` block and prints two rows as though
   computed. Neither is a degeneracy under any definition: `(2,3,7)` and `(2,4,5)` have `1 − R` of
   `1/42` and `1/20`; `(3,3,4)` and `(2,5,5)` have `1/12` and `1/10`. The printed "Area/π" column
   shows only the first triple's value, concealing the mismatch. The output is labelled
   `\label{tab:enum}`.

*Superseded by:* `code/enumerate_degeneracies.py` (correct signature, no fallback path, asserts on
six independently computed checkpoints).

### 2.2 `advanced_pillow_verification.py` — delete

1. **It cannot fail.** It prints `all checks passed` unconditionally. There are **zero `assert`
   statements** in the entire upstream repository at HEAD.
2. **It contradicts eq. (1).** `verify_higher_invariants` returns `area = π(1 − R)`. Gauss–Bonnet
   gives `Area = 2π(1 − R)` — wrong by a factor of two.
3. **Its checks are not the paper's.** `verify_diophantine_bounds` bounds by *denominator*, not
   cone-order *sum*, and only prints a count. `vieta_reconstruction` runs on `[1/2, 1/3, 1/4]` —
   rationals unrelated to any cone-order triple — and so is not the recovery of eq. (6). It also
   returns `(a²+b²+c²)/(abc)²`, a quantity appearing nowhere in the manuscript.

*Superseded by:* `code/verify_identities.py` (27 assert-based check groups, claim-ID tagged) and
`code/orbifold_enum.py` (whose self-test asserts the correct area convention *and* asserts against
the `π(1−R)` form specifically, so this regression cannot return silently).

### 2.3 `generate_latex_supplementary_table.py` — delete

Emits area, `Σ mᵢ⁻²`, `(pqr)⁻²` and a quadratic characteristic polynomial for six hand-picked
triples, under `\label{tab:density}`. The manuscript's Table 1 is a cumulative degeneracy count at
seven checkpoints to `S = 600`. The two share no column, no row and no value. Its "Area/π" column
carries the same factor-of-two error as §2.2.

*Superseded by:* `code/make_table.py`.

### 2.4 `run_all.py` — delete

Fails at import with `ModuleNotFoundError: No module named 'sympy'`. Even with sympy present it
would orchestrate only the three scripts above, none of which asserts anything, so a green run would
mean nothing.

*Superseded by:* `code/run_all.sh`, which pre-flights the interpreter version and both packages and
exits with an install instruction rather than a traceback.

### 2.5 `README.md` — replace, do not delete

Its content is wrong in three ways: it attributes Table 1 and Table 2 to scripts that produce
neither, its install fence is unterminated, and it describes a suite that verifies nothing.

*Replaced by:* `code/README.md`.

---

## 3. Files to RESTORE to upstream

These are the co-author's own prior work, deleted on 2026-08-08 and preserved byte-identical in
`code/legacy/`. They are correct within their scope and should return, under `legacy/`, as the
third leg of the cross-check.

| File | Recover from | Why restore |
|---|---|---|
| `arithmetic verification.py` | `4d872ef~1` | Groups triads by the correct `(S₁, R)`; independently confirms Theorem A, Theorem B and the `P₃` separation |
| `table_data.py` | `bb3a18a~1` | Generates the exact content of the manuscript's Table 2 (`tab:enum`) |
| `output of verification.txt` | `860472d~1` | Captured output of the above |
| `table_output.txt` | `8e4d513~1` | Captured output of the above |

Restore them **unmodified**, with `legacy/PROVENANCE.md`, which records the SHAs, the deletion
timestamps, and their known limitations (no asserts; bounded to `S₁ ≤ 18`; stale theorem numbering).

Do **not** present them as the current suite — `code/cross_check.py` consumes them as an independent
check, which is their value.

---

## 4. Files to ADD to upstream

The contents of `code/`:

| File | Role |
|---|---|
| `orbifold_enum.py` | General *n*-cone enumerator, stdlib-only, reusable at `n = 4, 5` |
| `enumerate_degeneracies.py` | `σ = (S₁, R)` sweep to `S = 600`, both counting conventions, primitivity flags |
| `make_table.py` | Regenerates both LaTeX tables; collisions detected, never hardcoded |
| `verify_identities.py` | 27 claim-ID-tagged check groups |
| `cross_check.py` | Three-way agreement: harness vs. oracle vs. legacy |
| `coverage_report.py` | Claim-ID integrity across the ledger |
| `run_all.sh` | Single-command runner with pre-flight and PASS/FAIL summary |
| `requirements.txt` | Pinned `sympy==1.14.0`, `mpmath==1.3.0`; minimum Python 3.9 |
| `README.md` | Accurate contents, per-table and per-claim reproduction instructions |
| `legacy/` | §3 above |

Also add the generated artefacts, so a reader need not run a seven-minute sweep to see the numbers:
`data/degeneracies.csv`, `data/degeneracy-groups.csv`, `paper/tables/table1.tex`,
`paper/tables/table2.tex`, `paper/tables/table1-both-conventions.tex`.

`review/audit-independent.py` should also go up. It is the independent oracle `cross_check.py`
runs, and its value depends on staying unrefactored.

---

## 5. Commit sequence

Nine commits, ordered so the repository is never in a state where broken code and correct code both
claim to verify the paper. Plain imperative messages, no trailers.

| # | Commit | Contents |
|---:|---|---|
| 1 | `Restore verification scripts deleted in August` | `legacy/` + `PROVENANCE.md`. **First**, so nothing correct is ever absent from the tree. |
| 2 | `Add exact-arithmetic n-cone orbifold enumerator` | `orbifold_enum.py` |
| 3 | `Add degeneracy enumeration keyed on the two-coefficient signature` | `enumerate_degeneracies.py` |
| 4 | `Add identity verification for the displayed rational claims` | `verify_identities.py` |
| 5 | `Add LaTeX table generation` | `make_table.py`, `paper/tables/*` |
| 6 | `Add cross-validation and claim coverage reporting` | `cross_check.py`, `coverage_report.py`, `audit-independent.py` |
| 7 | `Add single-command runner and pin dependencies` | `run_all.sh`, `requirements.txt` |
| 8 | `Replace README with accurate suite documentation` | `README.md` |
| 9 | `Remove superseded verification scripts` | Deletes §2.1–§2.4. **Last**, so the replacements are already in place. |

Ordering rationale: additions before deletions. If the sequence is interrupted, the repository still
contains working verification. The reverse order would leave a window with nothing at all.

### Before pushing

1. Run `./run_all.sh` on a clean clone and confirm exit `0`, six stages PASS.
2. Confirm `git log` shows only `Palaash Gang <palaashgang@gmail.com>` and the co-author for the
   restored commits, with no trailers.
3. Confirm every commit message is a plain imperative description of its change, with no
   attribution trailers of any kind.

---

## 6. Manuscript edits that must accompany the push

Publishing the code closes `DE-13`, `AP-18` and `AP-19` as-is. Three text changes are still needed;
none is executed here, and `paper/main.tex` has not been modified.

| Location | Change | Why |
|---|---|---|
| Appendix A, `\texttt{run\_all}` | → `\texttt{run\_all.sh}` | Closes `AP-13`. The file has an extension. |
| Appendix A, script attribution | The manuscript credits `make_table.py` with Table 2 (`tab:enum`) and `enumerate_degeneracies.py` with Table 1 (`tab:density`). In the new suite **`make_table.py` generates both tables**; `enumerate_degeneracies.py` produces the counts Table 1 draws on. | Otherwise the attribution is still wrong after the push |
| Section 5, definition of `N(S)` | Add the pairs-vs-classes clause | See [convention-note.md](convention-note.md) |

Optionally, once the repository is public and stable, add an archival DOI (Zenodo) to the Code
availability statement. `source-hygiene.md` notes that **28 of 28** bibliography entries lack DOIs;
a software DOI would at least give the artefact a persistent identifier.

---

## 7. What is explicitly NOT in scope here

- No remote is added, and nothing is pushed.
- `paper/main.tex` is untouched.
- `code/legacy/` is not modified — those files are evidence.
- `review/audit-independent.py` is not refactored; its independence is the point.
