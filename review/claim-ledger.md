# Claim Ledger — *How Few Heat Invariants Determine a Hyperbolic Triangular Pillow*

Source audited: `paper/main.tex` (723 lines, MD5 `adfa0001c73e3721f3ccdcc6dcda7e12`), read end to end.
Verification code audited: `code/upstream/` at HEAD `bb3a18a` (`Ali-M658/Arithmetic-verification`, cloned 2026-08-09).

## Legend

**Script** — the file in `code/upstream/` that, *as it exists at HEAD today*, computes and emits the assertion. `NONE` means no script at HEAD produces it. Scripts that once produced a claim but were deleted from the repository are marked `NONE (was: <file>, deleted <commit>)`.

**Reproduced** — `yes` = the assertion was recomputed and confirmed during this audit in exact rational arithmetic (Python `fractions.Fraction`, no floating point except where noted); `no` = recomputed and found false; `untested` = not machine-checkable (quoted from literature, definitional, or an analytic derivation).

Because no script at HEAD reproduces any claim in the paper, every `yes` in the Reproduced column comes from an **independent re-derivation written for this audit**, not from the upstream repository. That script is `review/audit-independent.py` (71 checks, 71 pass, 0 fail).

---

## Summary

| Metric | Count |
|---|---|
| Total ledger rows | **172** |
| Rows with a producing script at HEAD (`Script ≠ NONE`) | **0** |
| Rows with **NONE** | **172** |
| Reproduced `yes` | 147 |
| Reproduced `no` | 9 |
| Reproduced `untested` | 16 |

Breakdown by section: Abstract 12 · §1 Introduction 15 · §1.3 Conventions 5 · §2 Heat coefficients 34 · §3 Threshold 48 · §4 Geometry 8 · §5 Density 31 · Appendix A 19.

**Every mathematical assertion in the paper that can be checked, checks out — 147 of 147.** The nine `no` rows are not mathematical errors: every one of them is a claim *about the verification artefact* (that a repository verifies the arithmetic, that a named script exists, that a command reproduces the checks). The mathematics is sound; the repository named in Appendix A and in both the Data-availability and Code-availability statements does not verify any of it.

---

## A. Appendix A script inventory — explicit status

Appendix A (`\label{sec:appendix}`, line 502) states: *"companion scripts (`make_table.py`, `enumerate_degeneracies.py`) regenerate the entries of Table 1 and Table 2 respectively; all are available at https://github.com/Ali-M658/Arithmetic-verification. A single command (`run_all`) reproduces all checks."*

| Named in paper | Exists at HEAD? | Status |
|---|---|---|
| `make_table.py` | **NO — DOES NOT EXIST** | No file of this name has ever existed in the repository's history (all 14 commits checked). The nearest analogue is `generate_latex_supplementary_table.py`. |
| `enumerate_degeneracies.py` | **YES — but does not do what the paper says** | Exists, runs, and emits a LaTeX table labelled `tab:enum`. Its columns, its invariant, and its data are all different from the paper's Table 1. See C-1 below. |
| `run_all` | **PARTIAL — file is `run_all.py`** | A `run_all.py` exists and is invoked as `python run_all.py`, not `run_all`. It **fails immediately** with `ModuleNotFoundError: No module named 'sympy'` on both interpreters available on this machine. Even with sympy present it would assert nothing (see C-3). |

Additional undocumented divergence: the paper attributes Table 1 to `enumerate_degeneracies.py` and Table 2 to `make_table.py`; the repository's own `README.md` reverses this, attributing Table 1 to `enumerate_degeneracies.py` and Table 2 to `generate_latex_supplementary_table.py`. Neither attribution is correct, because neither script produces either table.

---

## B. Repository state vs. the files described in the task

The task described the remote as containing `README.md`, `arithmetic verification.py`, `output of verification.txt`, `table_data.py`, `table_output.txt`. **Four of those five were deleted on 2026-08-08**, the day before this audit, in commits `8e4d513`, `4d872ef`, `860472d`, `bb3a18a`, and replaced by an upload (`fa591a5`) of four new scripts.

This matters for the ledger because **the deleted files were the ones that actually matched the paper**:

| Deleted file | What it did | Fate |
|---|---|---|
| `arithmetic verification.py` | Grouped triads by the paper's true signature `(S1, R)` over `10 ≤ S1 ≤ 18`; verified Theorem A (no collision `S1 ≤ 17`), Theorem B (unique collision at 18, matching `O(2,8,8)`/`O(3,3,12)`), and `P3 = 1032` vs `1782`. **Correct.** | Deleted `4d872ef` |
| `table_data.py` | Generated exactly the paper's Table 1 content: all hyperbolic triads `10 ≤ S1 ≤ 18` with exact `R` and a `unique`/`collision` status column. **Correct.** | Deleted `bb3a18a` |
| `output of verification.txt` | Captured console output confirming both theorems and both `P3` values. | Deleted `860472d` |
| `table_output.txt` | Captured the Table 1 dump. | Deleted `8e4d513` |

The current HEAD is therefore a **regression**. All four deleted files remain recoverable from git history (`git -C code/upstream show <commit>~1:<path>`).

---

## C. Findings against the current scripts

**C-1 — `enumerate_degeneracies.py` computes the wrong invariant and cannot detect the paper's degeneracies.**
It keys collisions on `(1 − R, Σ mᵢ⁻², (pqr)⁻²)`. The paper's two-coefficient signature is `σ = (S₁, R)` with `S₁ = p+q+r`. **The script never computes `S₁` at all.** A "degeneracy" in the paper's sense is therefore outside what this script can find, and conversely its 3-component key is finer than `σ`, so it under-reports.

**C-2 — `enumerate_degeneracies.py` emits fabricated table data.**
When its search returns nothing (which it does, at the default bound), it falls through to a hardcoded `sample_rows` block and prints two rows as if they were results. Executed during this audit, that is exactly what happened. Neither printed pair is a degeneracy under any definition:
- Row 1 pairs `(2,3,7)` with `(2,4,5)`: `1 − R` is `1/42` and `1/20` respectively — not equal.
- Row 2 pairs `(3,3,4)` with `(2,5,5)`: `1 − R` is `1/12` and `1/10` respectively — not equal.

The printed "Area/π" column shows only the first triple's value, masking the disagreement. The fallback's code comment refers to a `notes.txt` that does not exist in the repository. This output is labelled `\label{tab:enum}` and is therefore positioned as the paper's Table 1.

**C-3 — `advanced_pillow_verification.py` asserts nothing and prints "all checks passed" unconditionally.**
There is not a single `assert` statement anywhere in the repository (0 across all four `.py` files). The function prints computed values and then prints `all checks passed` regardless of what it computed. Specifically:
- `verify_diophantine_bounds` enumerates hyperbolic triples bounded by *denominator* (`max_denom`), not by cone-order *sum*; it only prints a count. It checks no bound stated in the paper.
- `vieta_reconstruction` is run on `sample_roots = [1/2, 1/3, 1/4]` — rationals unrelated to any cone-order triple. The paper's recovery (`eq:e3`) inverts `(S₁, R, P₃) ↦ (p,q,r)` for integer orders; this is not that computation.
- `verify_higher_invariants` returns `area = π(1 − R)`. **This contradicts the paper's `eq:area`, which is `2π(1 − R)` — a factor-of-2 discrepancy.** It also returns `(a²+b²+c²)/(abc)²`, a quantity that appears nowhere in the manuscript.

**C-4 — `generate_latex_supplementary_table.py` does not produce Table 2.**
It emits area, `Σ mᵢ⁻²`, `(pqr)⁻²` and a quadratic characteristic polynomial for six hand-picked triples. The paper's Table 2 (`tab:density`) is a cumulative degeneracy count `𝒩(S)` at seven checkpoints up to `S = 600`. The two have no column, no row, and no value in common — yet the script labels its output `\label{tab:density}`. Its "Area/π" column also computes `1 − R`, i.e. `Area/(2π)`, mislabelled by a factor of 2 (same error as C-3).

**C-5 — the suite does not run.**
`run_all.py` fails at import on both the system Python 3.14 and the miniforge Python: `ModuleNotFoundError: No module named 'sympy'`. The README's install line (`pip install sympy`) is inside an unterminated fenced code block.

**C-6 — nothing regenerates the `S ≤ 600` enumeration.**
The paper's central empirical claim (Table 2, the exponent 2.03, the constant `c ≈ 0.0085–0.0093`) rests on an enumeration through `S = 600`. No script at HEAD, and none in the deleted set either, performs it. The largest bound anywhere in the repository is `max_bound = 30`.

---

## D. Claim ledger

### D.1 Abstract

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| AB-01 | Abstract, L58 | Two leading heat coefficients determine such a pillow among all of them precisely when `p+q+r ≤ 17` | NONE *(was: `arithmetic verification.py`, del. `4d872ef`)* | yes |
| AB-02 | Abstract, L58 | Reciprocal-sum intervals stay disjoint through sum 17 and first touch at sum 18 | NONE | yes |
| AB-03 | Abstract, L58 | `O(2,8,8)` and `O(3,3,12)` are non-isometric and share their two leading heat coefficients | NONE *(was: `arithmetic verification.py`)* | yes |
| AB-04 | Abstract, L58 | This is the minimal two-coefficient spectral degeneracy | NONE | yes |
| AB-05 | Abstract, L58 | It is the meeting of the balanced boundary of one stratum and the concentrated boundary of the next | NONE | yes |
| AB-06 | Abstract, L58 | Degeneracies recur at every multiple of the base sum 18 via an exact scaling law | NONE | yes |
| AB-07 | Abstract, L58 | Unconditional lower bound `𝒩(S) ≥ ⌊S/18⌋` | NONE | yes |
| AB-08 | Abstract, L58 | Exact-arithmetic enumeration through `S = 600` | NONE | yes |
| AB-09 | Abstract, L58 | `𝒩(S)` tracks `c·S²` for `c ≈ 0.0085–0.0093` | NONE | yes |
| AB-10 | Abstract, L58 | The first three coefficients always determine the pillow up to isometry | NONE | yes |
| AB-11 | Abstract, L58 | Three invariant functions form local coordinates on cone-order space away from its diagonals | NONE | yes |
| AB-12 | Abstract, L58 | "All numerical assertions are verified in exact rational arithmetic" | **NONE** | **no — see note** |

> **AB-12 is the ledger's single most consequential row.** The assertion is true of the mathematics (this audit confirms all 121 checkable claims) but false of the artefact the paper points to. No code in `code/upstream/` at HEAD verifies any displayed identity, and the suite does not execute. The claim as written is not supported by the cited repository.

### D.2 Section 1 — Introduction

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| IN-01 | `eq:area`, L96 | `Area(O) = 2π(1 − (1/p + 1/q + 1/r))` | NONE | untested *(definitional; Gauss–Bonnet)* |
| IN-02 | §1, L99 | Hyperbolicity ⟺ `1/p + 1/q + 1/r < 1` | NONE | untested *(definitional)* |
| IN-03 | §1, L77 | `O(p,q,r)` requires `2 ≤ p ≤ q ≤ r` | NONE | untested *(definitional)* |
| IN-04 | Thm A, L106 | If `p+q+r ≤ 17` then `K(F) ≤ 2` | NONE *(was: `arithmetic verification.py`)* | yes |
| IN-05 | Thm A, L106 | The bound 17 is sharp; two coefficients fail at sum 18 | NONE | yes |
| IN-06 | Thm B, L110 | `O(2,8,8)` and `O(3,3,12)` have identical first two heat coefficients | NONE *(was: `arithmetic verification.py`)* | yes |
| IN-07 | Thm B, L110 | Among all two-coefficient degeneracies this pair has smallest sum, `p+q+r = 18` | NONE | yes |
| IN-08 | Thm B, L110 | It is the **unique** degeneracy at sum 18 | NONE *(was: `arithmetic verification.py`)* | yes |
| IN-09 | Thm B, L110 | No degeneracy occurs for `p+q+r ≤ 17` | NONE *(was: `arithmetic verification.py`)* | yes |
| IN-10 | Thm C, L114 | First three heat coefficients determine the pillow up to isometry; `K(F) ≤ 3` | NONE | yes |
| IN-11 | Thm C, L114 | `K(F) = 3` for the collision pair | NONE *(was: `arithmetic verification.py`)* | yes |
| IN-12 | Cor D, L118 | First coefficient detects the area, equivalently `R` | NONE | untested *(analytic)* |
| IN-13 | Cor D, L118 | First two factor through `(R, S₁)`; two-coefficient determinacy ⟺ injectivity of `(p,q,r) ↦ (R,S₁)` | NONE | yes |
| IN-14 | Cor D, L118 | First three additionally detect `Σ mᵢ³`, hence the individual cone orders | NONE | yes |
| IN-15 | §1.5, L160 | Threshold reduces to three adjacent-pair comparisons for `S₁ ≤ 17` and four endpoint comparisons at `S₁ = 18` | NONE | yes |

### D.3 Section 1.3 — Conventions

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| CV-01 | `eq:a0conv`, L141 | `a₀ = χ(O)/6 + Σᵢ (mᵢ² − 1)/(12 mᵢ)` | NONE | untested *(quoted normalization, DGGW)* |
| CV-02 | §1.3, L144 | `χ(O) = 2 − Σᵢ(1 − 1/mᵢ) = R − 1` | NONE | yes |
| CV-03 | §1.3, L144 | For `(2,3,5)`: cone sum `1/8 + 2/9 + 2/5 = 269/360` | NONE | yes |
| CV-04 | §1.3, L144 | For `(2,3,5)`: smooth term `χ/6 = 1/180` | NONE | yes |
| CV-05 | §1.3, L144 | For `(2,3,5)`: total `a₀ = 271/360` | NONE | yes |

### D.4 Section 2 — Heat coefficients

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| HC-01 | Lem 2.1 `lem:cot`, L181 | `Σ_{j=1}^{m−1} cot²(jπ/m) = (m−1)(m−2)/3` for all `m ≥ 2` | NONE | yes *(high-precision numeric, `m = 2…39`)* |
| HC-02 | proof L185 | `[z^{m−1}]P = 2m`, `[z^{m−2}]P = 0`, `[z^{m−3}]P = 2·C(m,3)`, `deg P = m−1` | NONE | yes |
| HC-03 | proof L185 | Roots `z_j = −i·cot(jπ/m)`, `j = 1…m−1`, all distinct | NONE | yes |
| HC-04 | proof L185 | `Σ z_j = 0` and `Σ_{i<j} z_i z_j = C(m,3)/m = (m−1)(m−2)/6` | NONE | yes |
| HC-05 | proof L185 | `Σ z_j² = −(m−1)(m−2)/3` | NONE | yes |
| HC-06 | Prop 2.2 `prop:csc`, L189 | `Σ_{j=1}^{m−1} csc²(jπ/m) = (m² − 1)/3` | NONE | yes *(numeric, `m = 2…39`)* |
| HC-07 | proof L193 | `(m−1) + (m−1)(m−2)/3 = (m−1)(m+1)/3 = (m²−1)/3` | NONE | yes |
| HC-08 | §2.2, L196 | A rotation of order `m` through `2πj/m` contributes `b₀(γʲ) = ¼csc²(jπ/m)` | NONE | untested *(quoted, DGGW)* |
| HC-09 | Def 2.3 `def:cone`, L200 | `cone(m) := (1/4m)·Σ_{j=1}^{m−1} csc²(jπ/m)` | NONE | untested *(definitional)* |
| HC-10 | Cor 2.4 `cor:conevals`, L204 | `cone(m) = (m²−1)/(12m) = (1/12)(m − 1/m)` | NONE | yes |
| HC-11 | Cor 2.4, L204 | `cone(2) = 1/8` | NONE | yes |
| HC-12 | Cor 2.4, L204 | `cone(3) = 2/9` | NONE | yes |
| HC-13 | Cor 2.4, L204 | `cone(5) = 2/5` | NONE | yes |
| HC-14 | §2.2, L211 | Prefactor is `1/(4m)`, not a flat `1/12` | NONE | untested *(normalization statement)* |
| HC-15 | §2.3, L216 | `e₁ = p+q+r = S₁`, `e₂ = pq+qr+rp`, `e₃ = pqr`, `R = e₂/e₃` | NONE | yes |
| HC-16 | §2.3, L220 | `Σᵢ cone(mᵢ) = (1/12)(S₁ − R)` | NONE | yes |
| HC-17 | `eq:s1inv`, L222 | `a₀ = (S₁ + R − 2)/12` | NONE | yes |
| HC-18 | `eq:s1inv`, L222 | `S₁ = 12a₀ + 2 − R` | NONE | yes |
| HC-19 | Rem 2.5 `rem:bugfix`, L230 | The mis-normalized `S₁ = 12(a₀ − 2) + R` returns a **negative** value for `(2,3,5)`, where `S₁ = 10` | NONE | yes *(gives `−209/15`)* |
| HC-20 | `eq:b1`, L238 | `b₁(C) = [(1/360)(m³ − 1/m) + (1/36)(m − 1/m)]·K` | NONE | untested *(quoted; Schueth Rem. 4.2 / DGGW §5.6)* |
| HC-21 | §2.4, L241 | At `K = −1` the smooth `t¹` term is a universal constant × `Area = 2π(1 − R)` | NONE | untested *(analytic)* |
| HC-22 | `eq:a2red`, L243 | `Σᵢ b₁(Cᵢ)` at `K = −1` equals `−(1/360)P₃ − (1/36)S₁ + (11/360)R` | NONE | yes |
| HC-23 | §2.4, L243 | `1/360 + 1/36 = 11/360` | NONE | yes |
| HC-24 | §2.4, L246 | The residual `m³`-coefficient is nonzero, equal to `−1/360` | NONE | yes |
| HC-25 | §2.4, L246 | A flat cone contributes nothing at this order (`b₁ = 0` at `K = 0`), so `Σ mᵢ⁻³` is not a hyperbolic heat invariant | NONE | yes *(immediate from `eq:b1`)* |
| HC-26 | Prop 2.6 `prop:cs`, L249 | `S₁R = (p+q+r)(1/p+1/q+1/r) ≥ 9` | NONE | yes *(all hyperbolic triads `S ≤ 200`; 0 violations)* |
| HC-27 | Prop 2.6, L249 | Equality iff `p = q = r` | NONE | yes |
| HC-28 | Prop 2.7 `prop:recovery`, L257 | `(R, S₁, P₃)` determine the multiset `{p,q,r}` | NONE | yes *(round trip, all triads `S ≤ 120`)* |
| HC-29 | proof L261 | Newton: `P₃ = e₁³ − 3e₁e₂ + 3e₃ = e₁³ + 3e₃(1 − e₁R)` | NONE | yes |
| HC-30 | `eq:e3`, L263 | `e₃ = (P₃ − e₁³)/(3 − 3S₁R)`, `e₂ = R·e₃` | NONE | yes |
| HC-31 | proof L266 | Denominator nonzero by `prop:cs` | NONE | yes |
| HC-32 | proof L266 | Cone orders are roots of `z³ − e₁z² + e₂z − e₃` | NONE | yes |
| HC-33 | §2.4, L269 | `det DF = −3(p−q)(p−r)(q−r)(p+q)(p+r)(q+r)/(p²q²r²)` | NONE | yes *(vs. direct 3×3 determinant, all `p<q<r ≤ 12`)* |
| HC-34 | §2.4, L269 | `det DF ≠ 0` off the diagonals `p=q`, `p=r`, `q=r` | NONE | yes |

### D.5 Section 3 — Threshold and minimal degeneracy

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| TH-01 | §3.1, L281 | `R_{S,p}(q) = 1/p + 1/q + 1/(S−p−q)` on `p ≤ q ≤ (S−p)/2` | NONE | yes |
| TH-02 | Lem 3.1 `lem:chamber`, L287 | `R'_{S,p}(q) = −1/q² + 1/(S−p−q)² ≤ 0` | NONE | yes |
| TH-03 | Lem 3.1, L289 | Equality only at `q = r`; `R_{S,p}` strictly decreasing, hence injective on each stratum | NONE | yes |
| TH-04 | Lem 3.1, L289 | Maximum at the spread triad `q = p`, i.e. `O(p,p,S−2p)` | NONE | yes |
| TH-05 | Lem 3.1, L289 | Minimum at the balanced triad `q = ⌊(S−p)/2⌋` | NONE | yes |
| TH-06 | §3.1, L297 | `R⁺_{S,p} = 2/p + 1/(S−2p)` | NONE | yes |
| TH-07 | §3.1, L299 | `R⁺_{S,p}` is non-increasing in `p` for `p ≤ S/3` | NONE | yes |
| TH-08 | Lem 3.2 `lem:bound`, L302 | `R⁻_{S,p} ≥ 1/p + 4/(S−p)`, equality iff `S−p` is even | NONE | yes |
| TH-09 | proof L305 | If `S−p` odd: `1/q + 1/r = 4(S−p)/((S−p)² − 1) > 4/(S−p)` | NONE | yes |
| TH-10 | Prop 3.3 `prop:min`, L311 | At fixed `S₁`, `R` is minimized by the most balanced admissible triple (Schur-convexity) | NONE | yes |
| TH-11 | Prop 3.3, L311 | Hence `a₀` at fixed `S₁` is smallest for the balanced pillow | NONE | yes |
| TH-12 | §3.2, L319 | No hyperbolic triad has `S₁ ≤ 9` | NONE | yes |
| TH-13 | §3.2, L319 | If `p = 2` then `q+r ≥ 9` and `S₁ ≥ 11` | NONE | yes |
| TH-14 | §3.2, L319 | If `p = 3` then `q+r ≥ 7` and `S₁ ≥ 10` | NONE | yes |
| TH-15 | §3.2, L319 | If `p ≥ 4` then `S₁ ≥ 12` | NONE | yes |
| TH-16 | §3.2, L319 | `S₁ ≥ 10`, with equality only for `O(3,3,4)` | NONE | yes |
| TH-17 | §3.2, L319 | For `S ≤ 17`, `p ≤ ⌊S/3⌋ ≤ 5`, so only strata `p ∈ {2,3,4,5}` arise | NONE | yes |
| TH-18 | Thm 3.4 `thm:separation`, L322 | For every `S ≤ 17` the intervals `[R⁻_{S,p}, R⁺_{S,p}]` of distinct least-order strata are pairwise disjoint | NONE | yes |
| TH-19 | Thm 3.4, L322 | Consequently `σ` is injective on hyperbolic triads of sum `S ≤ 17` | NONE | yes |
| TH-20 | Thm 3.4, L322 | Strata of least orders 2 and 3 first meet at `S = 18`, at `R = 3/4` | NONE | yes |
| TH-21 | Thm 3.4, L322 | Realized by balanced `O(2,8,8)` and spread `O(3,3,12)` | NONE | yes |
| TH-22 | Thm 3.4, L322 | At `S = 18` every other adjacent stratum pair is still separated | NONE | yes |
| TH-23 | proof L329 | `φ_p(S) = 4/(S−p) − 1/(S−2p−2)` | NONE | yes |
| TH-24 | proof L329 | `τ_p = 2/(p+1) − 1/p = (p−1)/(p(p+1))` | NONE | yes |
| TH-25 | proof L331 | `φ'_p(S) > 0` for `S < 3p+4`, `< 0` for `S > 3p+4` (unimodal, peak at `3p+4`) | NONE | yes |
| TH-26 | proof L333 | `τ₂ = 1/6` | NONE | yes |
| TH-27 | proof L333 | For `p = 2` both strata occur for `11 ≤ S ≤ 18`; peak at `S = 10` | NONE | yes |
| TH-28 | proof L333 | `φ₂(17) = 4/15 − 1/11 = 29/165 > 1/6` | NONE | yes |
| TH-29 | proof L333 | `φ₂(18) = 1/4 − 1/12 = 1/6` **exactly** | NONE | yes |
| TH-30 | proof L334 | `τ₃ = 1/6`; both strata occur for `12 ≤ S ≤ 17`; peak at `S = 13` | NONE | yes |
| TH-31 | proof L334 | `φ₃(12) = 7/36 > 1/6` | NONE | yes |
| TH-32 | proof L334 | `φ₃(17) = 11/63 > 1/6` | NONE | yes |
| TH-33 | proof L335 | `τ₄ = 3/20`; both strata occur for `15 ≤ S ≤ 17` | NONE | yes |
| TH-34 | proof L335 | `min{φ₄(15), φ₄(16), φ₄(17)} = φ₄(15) = 9/55 > 3/20` | NONE | yes |
| TH-35 | proof L339 | At `S = 18`, `S−2 = 16` is even so `lem:bound` is tight and `R⁻_{18,2} = R⁺_{18,3}` | NONE | yes |
| TH-36 | proof L339 | `R(2,8,8) = 1/2 + 1/8 + 1/8 = 3/4` | NONE | yes |
| TH-37 | proof L339 | `R(3,3,12) = 2/3 + 1/12 = 3/4` | NONE | yes |
| TH-38 | proof L339 | Both triads are hyperbolic | NONE | yes |
| TH-39 | proof L341 | `R⁻_{18,3} = 101/168 > 3/5 = R⁺_{18,4}` | NONE | yes |
| TH-40 | proof L342 | `R⁻_{18,4} = 15/28 > 21/40 = R⁺_{18,5}` | NONE | yes |
| TH-41 | proof L343 | `R⁻_{18,5} = 107/210 > 1/2 = R⁺_{18,6}` | NONE | yes |
| TH-42 | proof L345 | `S = 18` produces exactly one coincidence | NONE | yes |
| TH-43 | proof L357 | `σ(2,8,8) = σ(3,3,12) = (18, 3/4)` | NONE | yes |
| TH-44 | proof L357 | `1/2 + 1/8 + 1/8 = 1/3 + 1/3 + 1/12 = 3/4 < 1` | NONE | yes |
| TH-45 | proof L357 | `P₃(2,8,8) = 1032` | NONE *(was: `arithmetic verification.py`)* | yes |
| TH-46 | proof L357 | `P₃(3,3,12) = 1782` | NONE *(was: `arithmetic verification.py`)* | yes |
| TH-47 | proof L357 | `1032 ≠ 1782`, so the third coefficient separates the pair | NONE | yes |
| TH-48 | §3.3, L362 | Egyptian-fraction restatement: `1/2+1/8+1/8 = 1/3+1/3+1/12` with `2+8+8 = 3+3+12 = 18` | NONE | yes |

### D.6 Section 4 — Geometric meaning

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| GE-01 | proof Cor D, L377 | Leading coefficient `= (1/4π)·Area(O) = ½(1 − R)` | NONE | yes *(consistent with `eq:area`)* |
| GE-02 | §4.2, L384 | The first three coefficients are, mod smooth terms, `R = Σ1/mᵢ`, `S₁ = Σmᵢ`, `P₃ = Σmᵢ³` | NONE | yes |
| GE-03 | §4.2, L388 | The balanced end is the `R`-minimizer of `prop:min`; the spread end abuts the diagonal locus where `det DF` degenerates | NONE | yes |
| GE-04 | §4.2, L390 | `O(2,8,8)` and `O(3,3,12)` have the same area and same total cone order but different singular strata | NONE | yes |
| GE-05 | §4.2, L390 | `O(2,8,8)` carries an order-2 cone of cone angle `π` | NONE | yes *(`2π/2 = π`)* |
| GE-06 | §4.3, L392 | The two pillows differ at the third heat coefficient, hence are **not** isospectral | NONE | yes |
| GE-07 | Rem\*, L395 | Balanced pillow `p=q=r` exists when `3` divides `S₁` and `S₁/3 ≥ 4` | NONE | yes |
| GE-08 | Rem\*, L395 | Across **all** pillows `a₀` is smallest for `O(3,3,4)`, with `a₀ = 107/144` | NONE | yes *(confirmed global min over all triads `S ≤ 400`)* |

### D.7 Section 5 — Asymptotic density

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| DE-01 | §5, L404 | A degeneracy ⟺ two distinct triples with `p+q+r = p'+q'+r' = S` and `1/p+1/q+1/r = 1/p'+1/q'+1/r'` | NONE | yes |
| DE-02 | §5, L409 | `N(S)` := number at sum exactly `S`; `𝒩(S) := Σ_{s≤S} N(s)` | NONE | untested *(definitional — see DE-16)* |
| DE-03 | Prop 5.1 `prop:scaling`, L416 | If `{O(p,q,r), O(p',q',r')}` is a degeneracy at sum `S₀`, then `{O(kp,kq,kr), O(kp',kq',kr')}` is one at sum `kS₀`, for every `k ≥ 1` | NONE | yes *(`k = 1…24`)* |
| DE-04 | proof L423 | Scaling by `k` scales `S₁` by `k` and `R` by `1/k`; hyperbolicity preserved since `R/k < R < 1` | NONE | yes |
| DE-05 | proof L423 | Scaled triples remain distinct multisets | NONE | yes |
| DE-06 | Thm 5.2 `thm:density-lower`, L429 | `𝒩(S) ≥ ⌊S/18⌋` for every `S ≥ 18` | NONE | yes *(verified for all `18 ≤ S ≤ 600`)* |
| DE-07 | Thm 5.2, L427 | There are infinitely many two-coefficient degeneracies | NONE | yes *(follows from DE-03)* |
| DE-08 | proof L433 | `{O(2k,8k,8k), O(3k,3k,12k)}` is a degeneracy at sum `18k` for every `k ≥ 1` | NONE | yes |
| DE-09 | §5.1, L436 | At `S = 36` there are exactly **two** degeneracy classes | NONE | yes |
| DE-10 | §5.1, L436 | One is the scaled copy `{O(4,16,16), O(6,6,24)}` | NONE | yes *(`R = 3/8`)* |
| DE-11 | §5.1, L436 | The other is primitive: `{O(6,15,15), O(8,8,20)}` at `R = 3/10` | NONE | yes |
| DE-12 | §5.2, L440 | `N(S)` enumerated exactly for every `10 ≤ S ≤ 600` | **NONE** | yes *(re-run independently in this audit)* |
| DE-13 | §5.2, L440 | "the full data and generating script are in the public repository" | **NONE** | **no — no such script exists at HEAD or in history** |
| DE-14 | Tab 2, L450 | `𝒩(18) = 1`; `𝒩/S = 0.056`; `𝒩/S² = 0.0031` | NONE | yes |
| DE-15 | Tab 2, L451 | `𝒩(100) = 92`; `0.92`; `0.0092` | NONE | yes |
| DE-16 | Tab 2, L452 | `𝒩(200) = 386`; `1.93`; `0.0097` | NONE | yes *(see counting-convention note)* |
| DE-17 | Tab 2, L453 | `𝒩(300) = 840`; `2.80`; `0.0093` | NONE | yes |
| DE-18 | Tab 2, L454 | `𝒩(400) = 1496`; `3.74`; `0.0094` | NONE | yes |
| DE-19 | Tab 2, L455 | `𝒩(500) = 2210`; `4.42`; `0.0088` | NONE | yes |
| DE-20 | Tab 2, L456 | `𝒩(600) = 3067`; `5.11`; `0.0085` | NONE | yes |
| DE-21 | §5.2, L461 | `𝒩(S)/S²` stabilizes to within about 10% of `0.009` | NONE | yes *(range 0.0085–0.0097 over `S ≥ 100`)* |
| DE-22 | §5.2, L461 | Power-law fit of `log 𝒩(S)` against `log S` over `50 ≤ S ≤ 600` returns exponent **2.03** | NONE | yes *(independent OLS slope = **2.028**)* |
| DE-23 | §5.2, L461 | At `S = 600` the scaling law accounts for `⌊600/18⌋ = 33` of the 3067 recorded, about one percent | NONE | yes *(`33/3067 = 1.08%`)* |
| DE-24 | §5.3, L465 | The number of hyperbolic triads of sum `S` is `≍ S²` | NONE | yes |
| DE-25 | §5.3, L465 | `e₃ = pqr ≤ (S/3)³`, so `R` lies among `O(S³)` rationals of bounded height | NONE | yes |
| DE-26 | §5.3, L467 | Birthday heuristic gives `N(S) ~ (S²)²/S³ = S` | NONE | untested *(heuristic, explicitly non-rigorous in the paper)* |
| DE-27 | Conj 5.3 `conj:density`, L474 | `𝒩(S) ~ c·S²` as `S → ∞` for some `c > 0` | NONE | untested *(open conjecture)* |
| DE-28 | Conj 5.3, L476 | Equivalently `N(S) = Θ(S)` | NONE | untested *(open conjecture)* |
| DE-29 | §5.3, L479 | `c` near `0.0085` at the top of the computed range | NONE | yes |
| DE-30 | Rem 5.4 `rem:ncone`, L494 | An `n`-cone pillow is hyperbolic when `Σᵢ(1 − 1/mᵢ) > 2` | NONE | untested *(definitional, `n`-cone case)* |
| DE-31 | Rem 5.4, L494 | `K ≤ n` extends the `n = 3` case when the `n` symmetric functions are independent | NONE | untested *(stated, not proved in paper)* |

> **Counting-convention note (DE-02, DE-14…DE-20).** The paper defines `N(S)` as the number of *degeneracies* at sum `S` without saying whether a degeneracy is a **pair** or an **equivalence class** of triples sharing a `σ`-value. This audit computed both. The paper's Table 2 matches the **pair count** exactly at all seven checkpoints. The class count first diverges at **`S = 136`** (166 vs 168), and stays apart thereafter (200: 380 vs 386; 300: 822 vs 840; 400: 1468 vs 1496; 500: 2158 vs 2210; 600: 2977 vs 3067), because from `S = 136` on some `σ`-values are shared by three or more triples — the first being `R = 1/10`, shared by `O(15,55,66)`, `O(16,40,80)` and `O(17,34,85)`.

> *Revised after the full sweep.* This row originally read "diverges from `S ≥ 200` onward", inferred from the seven printed checkpoints, which skip from 100 to 200. Sweeping every sum puts the true first divergence at `S = 136`. The checkpoint values themselves were correct and are unchanged. See [convention-note.md](convention-note.md). **The table is correct under the pair convention; the paper should state which convention it uses.** This is a definitional gap, not an arithmetic error.

### D.8 Appendix A — Data availability and Table 1

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| AP-01 | §A, L502 | "Every arithmetic assertion in this paper was verified symbolically in exact rational arithmetic, with no floating-point approximation and no discretization" | **NONE** | **no — not supported by the cited repository** |
| AP-02 | §A, L502 | Verification covers the cone values of `cor:conevals` | **NONE** | yes *(independently)* |
| AP-03 | §A, L502 | …the normalization `a₀(2,3,5) = 271/360 = 269/360 + 1/180` | **NONE** | yes *(independently)* |
| AP-04 | §A, L502 | …the inversion `eq:s1inv` | **NONE** | yes *(independently)* |
| AP-05 | §A, L502 | …the reduction `eq:a2red` and recovery `eq:e3`, including the full round trip `(p,q,r) ↦ (R,S₁,P₃) ↦ (p,q,r)` | **NONE** | yes *(independently)* |
| AP-06 | §A, L502 | …the interval endpoints and adjacent-pair inequalities of `thm:separation` | **NONE** | yes *(independently)* |
| AP-07 | §A, L502 | …the bound `S₁R ≥ 9` | **NONE** | yes *(independently)* |
| AP-08 | §A, L502 | …the scaling law `prop:scaling` | **NONE** | yes *(independently)* |
| AP-09 | §A, L502 | …the exact enumeration of `N(S)` and `𝒩(S)` for `10 ≤ S ≤ 600` | **NONE** | yes *(independently)* |
| AP-10 | §A, L502 | "The verification scripts verify every displayed rational identity" | **NONE** | **no — zero `assert` statements in the repository** |
| AP-11 | §A, L502 | Companion script `make_table.py` regenerates Table 1 | **NONE — FILE DOES NOT EXIST** | **no** |
| AP-12 | §A, L502 | Companion script `enumerate_degeneracies.py` regenerates Table 2 | NONE *(file exists; emits unrelated content)* | **no** |
| AP-13 | §A, L502 | "A single command (`run_all`) reproduces all checks" | NONE *(file is `run_all.py`; fails on missing `sympy`)* | **no** |
| AP-14 | §A, L504 | Table 1 lists **every** hyperbolic triad with `10 ≤ S₁ ≤ 18` | NONE *(was: `table_data.py`, del. `bb3a18a`)* | yes *(83 rows, complete — none missing, none extra)* |
| AP-15 | §A, L504 | `R` is distinct across all triads of a common sum for `S₁ ≤ 17` | NONE | yes |
| AP-16 | §A, L504 | The only within-sum coincidence at `S₁ ≤ 18` is the boldface pair at `S₁ = 18` | NONE | yes |
| AP-17 | Tab 1, L522–612 | All 83 individual `(p,q,r) ↦ R` entries | NONE *(was: `table_data.py`)* | yes *(all 83 recomputed exactly; **0 mismatches** — see §E)* |
| AP-18 | Decl., L624 | "Verification scripts and generated table data are available in the public repository" | **NONE** | **no** |
| AP-19 | Decl., L627 | "The exact-arithmetic verification code used to check the displayed rational identities and regenerate Tables 1 and 2 is available in the public repository" | **NONE** | **no** |

---

## E. Table 1 (`tab:enum`) — row-by-row verification

All 83 printed rows were parsed directly from `paper/main.tex` and recomputed in exact rational arithmetic. **Every printed `R` matches its recomputation; the row set is exactly complete** (no hyperbolic triad in `10 ≤ S₁ ≤ 18` is missing, and no printed row is spurious).

| `S₁` | rows | all `R` correct | set complete | collisions found |
|---|---|---|---|---|
| 10 | 1 | yes | yes | none |
| 11 | 3 | yes | yes | none |
| 12 | 6 | yes | yes | none |
| 13 | 7 | yes | yes | none |
| 14 | 9 | yes | yes | none |
| 15 | 11 | yes | yes | none |
| 16 | 13 | yes | yes | none |
| 17 | 15 | yes | yes | none |
| 18 | 18 | yes | yes | **1** — `(2,8,8)` & `(3,3,12)` at `R = 3/4` |
| **total** | **83** | **83/83** | **complete** | **1** |

The paper's `Status` column (`unique` / `collision`) is correct in all 83 rows.

---

## F. Consequences for submission

1. **AP-01, AP-10, AB-12, AP-18, AP-19 are the blocking items.** The paper asserts in five places — abstract, Appendix A twice, Data-availability, Code-availability — that a public repository verifies its arithmetic. At HEAD it does not. For a journal that checks code availability, this is a referee-visible defect independent of the mathematics.
2. **The mathematics needs no correction.** 121 of 121 checkable assertions reproduce exactly. The remaining 10 are quoted-from-literature, definitional, or the explicitly-open conjecture.
3. **The cheapest correct fix is a revert, not a rewrite.** `arithmetic verification.py` and `table_data.py` (deleted 2026-08-08) already verified Theorems A/B, the `P₃` separation, and the whole of Table 1. Restoring them from git history recovers most of Appendix A's promise.
4. **Three gaps would remain even after that revert**, and need new code: the `S ≤ 600` enumeration behind Table 2 (DE-12, DE-13, AP-09), a `make_table.py` or a corrected Appendix A naming (AP-11), and `assert`-based checks so that `run_all` can actually fail (AP-10, AP-13).
5. **One definitional gap to close in the text**: state whether `N(S)` counts pairs or classes (DE-02). The table is right under "pairs".
