# G5-bis comparison phase: group `stability`

Written after the blind REVIEW.md was frozen. Files read in this phase:
- `theory/revision/prop610.tex` (all of it);
- `theory/revision/check_prop610.py` and `.txt`;
- `theory/stability/threshold.py`, `threshold_output.md`, `threshold_results.json`, `stab_common.py`
  (`theorem_B_system`), `lipschitz_e.py` (`N_matrix`);
- `proof.md` lines 18–40 and its ST.14 table, and `STATUS.md` (grep);
- `review/audit/stability/COMPARISON.md` (grep for the δ_up item).

`paper/**` was not released, so the manuscript's own Theorem B and Table 4 were not seen.

The new script `check_compare.py` (output `check_compare.txt`, exit 0) imports `threshold.py` read-only. It
executes `check_prop610.py` only up to its "(a)" block, so nothing under `theory/` is written; `git status`
shows `theory/` clean. It then compares everything exactly with my `stab610.py`.

**No blind grade changes.** Every blind finding is confirmed by the producer's own code or data, with one
added discrepancy (D4).

## Per-result agreement (exact, all 11 rows)

| quantity | producer source | agreement with my implementation |
|---|---|---|
| Theorem B M(I), b(I) | `stab_common.theorem_B_system`; `check_prop610.system`; prop610.tex proof, Step 3 | **identical**: rows e_{2j+1} − Σ_{i≤j} T_{2i+1}e_{2j−2i} = 0 with e₀ moved to b, and last row e_{n−1} − Re_n = 0. This is exactly my reconstruction (REVIEW §0) |
| E, A = \|M⁻¹\|Δ_M, r_rem bound at the printed δ_cert | `threshold._common`; `check_prop610.bounds` | **identical** (Fraction equality); ϱ bound also identical to check_prop610's `vrho` |
| G | threshold: −M⁻¹·`N_matrix`·L⁻¹; check_prop610: printed J | **identical**. `lipschitz_e.N_matrix` == printed J == my J |
| δ_thm | `threshold.delta_thm` | **identical exact rationals** |
| δ_cert | `threshold_results.json` `delta_cert_exact` (bisection sup) | lies inside my 6-s.f. bracket in all rows and certifies under my code; the printed 4-s.f. values are equal |
| ε_cert | `threshold_results.json` | floats agree with my 4-s.f. maxima; see D4 |
| δ_up | `threshold_results.json` | **identical to 8 digits in all 11 rows** (e.g. (2,2,2,2,3): 5.3113199e−05) |
| ladder | `threshold.RADII`, `check_prop610.RADII` | **identical** to my reading {k/40 : k = 20..1} ∪ {1/100, 1/1000} (threshold writes it as [1/2] + [j/40, j = 19..1] + …) |

## Discrepancies

**D1. The (2,2,2,2,3) δ_up: the printed 5.743e−05 / 7.26 is stale.** (Confirms blind R10; grade unchanged,
MINOR.)
- `threshold_output.md` and `threshold_results.json` already give **5.312e−05** (5.3113199e−05), "3−1/2
  (real)". This is the same point 5/2 as my "2+1/2", and the same value as mine to 8 digits.
- `theory/stability/proof.md` line 446 (the source of ST.14/SB.4) and `STATUS.md` line 53 still print
  5.743e−05 and 7.26 with "2+1/2".
- The G5 COMPARISON (review/audit/stability/COMPARISON.md, l. 211) had already asked for "reprint δ_up =
  5.312e−05 and the ratio 6.72". The output was regenerated, but the prose table was never updated.
- The paper is presumably stale too; I could not check, because paper/** was not released.
- The same staleness gives (3,10,15,30) δ_up = 7.488e−03 in proof.md versus **7.487e−03** in
  threshold_output.md (= mine).
- Required change as in REVIEW R10: 5.312e−05, ratio 6.72; also 7.487e−03 for (3,10,15,30).

**D2. The (2,3,7) relative-precision entry: blind diagnosis confirmed** (R9, MINOR, unchanged).
- threshold.py computes `rel = float(dcert/|H|)` with `dcert` the **unrounded** bisection sup
  (3.65881e−03), not the printed 3.658e−03.
- It formats with `:.2e`, which is round-to-nearest at 3 s.f.: 4.0001e−03 → "4.00e−03".
- The 2-s.f. table then truncates "4.00e−03" to 4.0e−03. With the printed δ_cert the value is 3.9992e−03,
  which rounds down to 3.9e−03.
- So the column is "sup/|H_ν|" with double rounding (nearest at 3 s.f., then truncation), not
  "δ_cert/|H_ν| rounded down". It is still a certified precision.
- Fix as in R9: print 3.9e−03, or re-caption the column.

**D3. Code paths differ from the printed text in three places; none changes a number.**
1. *Test combination.*
   - threshold.py: `certify = certify_coherent or certify_abs`, i.e. test (ii) for all orders, or test (i) for
     all orders.
   - check_prop610: accepts an order when `low > min(t1, t2)` at some radius, i.e. per-order and per-radius
     mixing of (i) and (ii).
   - Both are valid (REVIEW R4). Since every row certifies by test (ii) at every order, the results coincide.
     The printed "either test succeeds" matches threshold.py.
2. *G.* threshold.py uses `lipschitz_e.N_matrix`, not the printed J. They are equal entrywise (check_compare),
   so threshold.py does not itself test the printed J formula. check_prop610 does test it, but against
   threshold's E, A, r_rem, never against an independent J.
3. *δ_up search shapes.* ST.13 says both shapes are searched for each order. `threshold.counterexample` tries
   the complex-pair shape only when `m.count(a) ≥ 2`, and uses only the natural start plus one 1e−3 rescale.
   My search covered both shapes for every order, with 11–35 starts per case and 60 more for (2,2,2,2,3).
   (Correction to REVIEW R10, which says "13–31 starts": rows (2,8,8) and (3,3,12) used 31 (real shape) or 35
   (pair shape). The other nine rows were re-run with 11 (real) or 15 (pair) starts, to fit the time budget.
   No value changes.) No minimiser is a complex pair, so the
   numbers agree, but ST.13 overstates the search. Suggested wording: "with a complex pair (for repeated
   orders)".

**D4 (new; producer artifact only, not the printed table). `threshold_output.md` prints ε_cert at 4 s.f.
rounded to nearest, against the round-down convention of ST.13.** The code is
`f"{float(rlo):.3e}"`, while δ_cert and δ_thm use `fmt_down`. In 5 rows the printed 4-s.f. ε_cert **does not
certify**, under my certificate and under `threshold.certify` itself:

| m | sup (float) | printed | certifies? |
|---|---|---|---|
| (3,3,12) | 4.49158774e−03 | 4.492e−03 | no |
| (3,10,15,30) | 8.70775496e−04 | 8.708e−04 | no |
| (2,3,7) | 5.01361323e−03 | 5.014e−03 | no |
| (3,3,4,4) | 1.18572580e−04 | 1.186e−04 | no |
| (2,2,2,3) | 4.39879305e−04 | 4.399e−04 | no |

- The 2-s.f. values printed in ST.14 (4.4e−03, 8.7e−04, 5.0e−03, 1.1e−04, 4.3e−04) are round-downs and do
  certify (blind R8 stands, NONE).
- Severity MINOR, internal artifact. Fix: format ε_cert with `fmt_down` in threshold.py and regenerate. If any
  4-s.f. ε is quoted anywhere, use 4.491e−03, 8.707e−04, 5.013e−03, 1.185e−04, 4.398e−04.

**D5. check_prop610.py: what it does and does not check.**
- Its computation is independent of threshold.py: its own Bernoulli numbers, tanh/tan series, front end from
  the trace-formula p_l, Theorem B and bounds. It imports threshold.py only for the comparison in (b), and in
  (c), where its PASS line is the conjunction `ok and TH.certify(...)`. So it is a genuine second
  implementation of the printed formulas, and the prop610.tex header claim ("reproduces r_rem, A and E of
  threshold.py EXACTLY … certifies every printed δ_cert and δ_thm") is **true**; I reproduce it independently.
- It shares the *conventions* with threshold.py (the same reading of Theorem B), so it does not independently
  check that reconstruction. My checks against Lemma S2.2/S2.1 (REVIEW §0) do.
- It does **not** check:
  - that each printed δ_cert is the 4-s.f. maximum;
  - that the printed δ_thm equals the Theorem S4 value;
  - ε_cert, δ_up, or the relative-precision column;
  - the SB.3 claim.

  All of these are covered only by this review (check_cert, check_dup).
- Its test (c) uses the per-radius min(t1, t2), which is not literally the printed "either test" (D3.1).

**D6. The SB.3 sentence (R5) is unchanged in prop610.tex l. 63–65.** The odd/even issue stands. In the
producer's own code (`sech2`, `sec2` in `bounds`/`_common`) these are even series with constant term 1. R5
stays MINOR.

## Items checked with no discrepancy

- **Ladder reading:** the same in both producer scripts and mine.
- **J formula:** prop610.tex l. 45 equals check_prop610 equals `N_matrix` equals sympy (REVIEW R2).
- **Notation (R3):** prop610.tex also writes F for the front end and δ for the radii, while threshold.py calls
  them L and dH. The ρ overloading (R3) is present in the proposition text; the code avoids it by using
  `dH`. R3 stays MINOR.

## Grade changes

None. R1–R11 stand as blind-graded. D4 is a new MINOR finding on the producer artifact
`threshold_output.md` (not on the printed table). It needs the one-line `fmt_down` fix above.
