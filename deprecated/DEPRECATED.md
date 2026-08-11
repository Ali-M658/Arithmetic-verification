# Deprecated verification scripts

**Nothing here has been deleted.** The four files in this directory were moved, unmodified, from
the repository root. Their content is byte-identical to what stood at commit `bb3a18a`; `git log
--follow deprecated/<file>` recovers their full history.

They are here because each of them, as written, reports success without verifying anything the
manuscript claims — and three of them emit output labelled as a manuscript table. A reader who
runs them concludes the paper is verified. It is not verified by them.

Replacements live in `code/`. Each entry below names the file that supersedes it.

**This branch is for review, not for merging.** It exists so the changes to these files can be
looked at before anything happens to them on `main`.

---

## Why each file is here

Every claim below was checked against the file itself, at the line cited.

### `advanced_pillow_verification.py`

1. **Unconditional pass message.** Line 65 is `print("all checks passed")`, reached on every
   execution regardless of what was computed. Nothing upstream of it can prevent it.
2. **Zero assertions.** `grep -c '^\s*assert\b'` returns **0**. It returns 0 for all four files in
   this directory — there is not one `assert` statement anywhere in the upstream suite, so no
   computation in it can fail.
3. **Wrong area convention.** Line 40 is
   `area = sp.pi * (1 - (1/a + 1/b + 1/c))`, i.e. $\pi(1-R)$. Gauss–Bonnet gives
   $\mathrm{Area} = 2\pi(1-R)$, which is equation (1) of the manuscript. **Wrong by a factor of
   two.**
4. **The checks are not the paper's checks.** `verify_diophantine_bounds` bounds the search by
   *denominator*, not by cone-order *sum*, and only prints a count — it tests no bound stated in
   the paper. `vieta_reconstruction` runs on `[1/2, 1/3, 1/4]`, rationals unrelated to any
   cone-order triple, so it is not the recovery of equation (6). `verify_higher_invariants` also
   returns $(a^2+b^2+c^2)/(abc)^2$, a quantity that appears nowhere in the manuscript.

*Superseded by:* `code/verify_identities.py` (27 assert-based check groups, each tagged with the
claim ID it discharges) and `code/orbifold_enum.py`, whose self-test asserts the correct
$2\pi(1-R)$ convention **and** asserts against the $\pi(1-R)$ form specifically, so this
particular regression cannot come back silently.

### `enumerate_degeneracies.py`

1. **Hardcoded fallback rows printed as computed results.** Lines 42–52: when the search returns
   nothing — which it does at the default bound — control falls into a `sample_rows` literal and
   prints two rows as though they had been computed. The code comment points at a `notes.txt`
   that does not exist in the repository.

   Neither printed row is a degeneracy under any definition, and the printed numbers do not even
   match the triples they are attached to:

   | Row | Triples printed | Printed "Area $/\pi$" | Actual $1-R$ |
   |---|---|---|---|
   | 1 | $(2,3,7)$ and $(2,4,5)$ | $1/42$ | $1/42$ and $1/20$ — unequal, so not a collision; the column shows only the first |
   | 2 | $(3,3,4)$ and $(2,5,5)$ | $1/6$ | $1/12$ and $1/10$ — unequal, **and $1/6$ is neither of them** |

   This output is labelled `\label{tab:enum}` and is therefore positioned as a manuscript table.

2. **Wrong invariant.** Line 12 keys collisions on $(1-R,\ \sum m_i^{-2},\ (pqr)^{-2})$. The
   manuscript's two-coefficient signature is $\sigma = (S_1, R)$ with $S_1 = p+q+r$. **The script
   never computes $S_1$ anywhere** — the cone-order sum does not appear in the file. A degeneracy
   in the manuscript's sense is outside what this code can find; and its three-component key is
   finer than $\sigma$, so it also under-reports.

3. **Zero assertions.**

*Superseded by:* `code/enumerate_degeneracies.py` — keys on the correct $\sigma = (S_1,R)$,
sweeps to $S = 600$, carries both counting conventions, has no fallback path at all (it raises
rather than printing canned data), and asserts against six independently computed checkpoints.

### `generate_latex_supplementary_table.py`

1. **Does not produce the table it is labelled with.** It emits area, $\sum m_i^{-2}$,
   $(pqr)^{-2}$ and a quadratic characteristic polynomial for six hand-picked triples, under
   `\label{tab:density}`. The manuscript's density table is a cumulative degeneracy count
   $\mathcal N(S)$ at seven checkpoints up to $S = 600$. The two share no column, no row and no
   value.
2. **Same factor-of-two area error.** Line 12 computes `area_frac` as $1-R$ and line 39 prints
   that column as `Area $/ \pi$`. It is $\mathrm{Area}/(2\pi)$.
3. **Zero assertions.**

*Superseded by:* `code/make_table.py`, which regenerates both manuscript tables with collisions
detected rather than hardcoded.

### `run_all.py`

1. **Import failure — the suite does not run.** Line 6 imports
   `advanced_pillow_verification`, which imports `sympy` at its line 10. On a machine without
   sympy the whole suite dies before executing anything:

   ```
   Traceback (most recent call last):
     File "run_all.py", line 6, in <module>
       import advanced_pillow_verification
     File "advanced_pillow_verification.py", line 10, in <module>
       import sympy as sp
   ModuleNotFoundError: No module named 'sympy'
   ```

   The repository's own README gives the install line inside an unterminated fenced code block.
2. **A green run would mean nothing.** Even with sympy present, it orchestrates only the three
   scripts above, none of which asserts anything. Success is not evidence.
3. **Zero assertions.**

*Superseded by:* `code/run_all.sh`, which pre-flights the interpreter version and both required
packages and exits with an install instruction rather than a traceback, runs all six stages even
after one fails so a single run reports every problem, and returns a nonzero exit code if any
stage fails. That last property was verified by deliberately falsifying an assertion and
confirming the suite exits `1`.

---

## Not moved

`README.md` is left in place. It is inaccurate in three ways — it attributes Table 1 and Table 2
to scripts that produce neither, its install fence is unterminated, and it describes a suite that
verifies nothing — but it is documentation rather than a verification script, and replacing prose
is a different decision from retiring code. `code/README.md` is the accurate version. Whether to
replace the root README is left to the co-author.

## Summary

| File | Asserts | Unconditional pass | Fabricated output | Wrong area convention | Runs at all |
|---|---:|---|---|---|---|
| `advanced_pillow_verification.py` | 0 | yes | — | yes, $\pi(1-R)$ | needs sympy |
| `enumerate_degeneracies.py` | 0 | — | yes, `sample_rows` | — | yes |
| `generate_latex_supplementary_table.py` | 0 | — | — | yes, mislabelled column | yes |
| `run_all.py` | 0 | inherits | inherits | inherits | **no** |
