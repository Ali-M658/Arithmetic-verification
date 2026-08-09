# Provenance — recovered upstream verification scripts

The four files in this directory are **prior work by the co-author**, recovered unmodified from the
git history of the upstream verification repository:

    https://github.com/Ali-M658/Arithmetic-verification

All 14 commits in that repository are authored by `Ali-M658 <Fastninja277@gmail.com>`. These files
are reproduced here verbatim, byte-for-byte, as a preserved third cross-check for the `n = 3`
results. **Do not modify them.** They are evidence, not maintained code.

## What happened upstream

On **2026-08-08**, between 17:10:06 and 17:10:48 (−05:00), all four files were deleted in four
consecutive commits and replaced by an upload of four new scripts (`fa591a5`). The replacements do
not compute the paper's signature `σ = (S₁, R)` and verify none of its claims. The deletion was
therefore a regression: **the files recovered here are the ones that actually matched the
manuscript.**

## Recovery record

Each file was extracted with `git show <deletion-commit>~1:<path>` and verified byte-identical to
the upstream blob by SHA-256.

| File | Last modified upstream | Deleted upstream | Recovered from | SHA-256 (verified) |
|---|---|---|---|---|
| `arithmetic verification.py` | `9326872` — 2026-07-05T14:45:01−05:00 — *Refactor arithmetic verification script structure* | `4d872ef` — 2026-08-08T17:10:23−05:00 — *Delete arithmetic verification.py* | `4d872ef~1` | `5055d5c4…0abe6820` |
| `table_data.py` | `e355fec` — 2026-07-05T16:53:22−05:00 — *Refactor table generation to mathematical context* | `bb3a18a` — 2026-08-08T17:10:48−05:00 — *Delete table_data.py* | `bb3a18a~1` | `fde714dc…ab635e49` |
| `output of verification.txt` | `e70fc02` — 2026-07-05T14:45:19−05:00 — *Update verification output with detailed results* | `860472d` — 2026-08-08T17:10:38−05:00 — *Delete output of verification.txt* | `860472d~1` | `aade2c41…0b3353de` |
| `table_output.txt` | `94e00a9` — 2026-07-05T16:53:05−05:00 — *Update table_output.txt with new output format* | `8e4d513` — 2026-08-08T17:10:06−05:00 — *Delete table_output.txt* | `8e4d513~1` | `29d78e1e…073a4609` |

Upstream HEAD at the time of recovery: `bb3a18a`.

## What each file does

**`arithmetic verification.py`** — groups hyperbolic triads by the paper's true two-coefficient
signature `(S₁, R)` over `10 ≤ S₁ ≤ 18` using `sympy.Rational`, then checks Theorem A (no collision
for `S₁ ≤ 17`), Theorem B (exactly one collision at `S₁ = 18`, matching `O(2,8,8)` / `O(3,3,12)`),
and the `P₃` separation (`1032 ≠ 1782`). This is the correct signature and the correct result.

**`table_data.py`** — enumerates every hyperbolic triad with `10 ≤ S₁ ≤ 18`, computes exact `R` with
`fractions.Fraction`, groups by `(S₁, R)` to mark each row `unique` or `collision`, and prints the
table. This is the content of the manuscript's Table 2 (`\label{tab:enum}`).

**`output of verification.txt`**, **`table_output.txt`** — captured console output of the two
scripts above. `table_output.txt` contains ANSI colour escapes around the collision rows.

## Known limitations of the recovered scripts

Recorded so that later cross-checks are not surprised by them. None of these are corrected here.

1. **No `assert` statements.** Both scripts report by printing. They cannot fail a build. Every
   conclusion is guarded by an `if`, and a false condition simply prints nothing.
2. **Bounded to `S₁ ≤ 18`.** Neither performs the `S ≤ 600` enumeration behind the manuscript's
   Table 1 (`\label{tab:density}`).
3. **Stale theorem numbering.** `arithmetic verification.py` refers to "Lemma 3.1" for the
   conditions `p < p′`, `p′ < 3p`, `S ≥ 3p′`, which appear nowhere in the current `paper/main.tex`,
   and to "Proposition 2.5" for the `P₃` recovery, which is Proposition 2.7 (`prop:recovery`) in the
   current manuscript. The scripts predate the present draft.
4. **`arithmetic verification.py` requires sympy**; `table_data.py` is stdlib-only.
5. `output of verification.txt` embeds an absolute Windows interpreter path from the machine that
   produced it.

## Relationship to the current harness

The scripts in `code/` supersede these for day-to-day verification: they are assert-based, cover
`n ≥ 3`, and reach `S = 600`. These legacy files are retained as an **independent third check** on
`n = 3` alongside `review/audit-independent.py`. `code/cross_check.py` runs all three and reports
any disagreement rather than preferring one.
