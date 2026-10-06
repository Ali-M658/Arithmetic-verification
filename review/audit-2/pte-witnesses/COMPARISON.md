# G5-bis comparison phase: group `pte-witnesses`

This file compares my blind `REVIEW.md` (frozen, unchanged) with the producer's code and data.

**Files read:**
- in `theory/pte/`: `witnesses.py`, `pte_common.py`, `pencil_search.py`, `search_T3.c`, `search_T3.sh`,
  `search_T3_verify.py`, `search_T3_control.py`, `real_shapes.py`;
- `data/witnesses.json`, `data/pencil_log.txt`, `data/pencil_*.json`, `data/T3_search_log.txt`;
- `output/*`, `attack/a01`, `attack/a04`, `attack/a09` outputs, `attack-log.md`, `STATUS.md` (grep);
- `proof.md` §5–7.

**Not opened:** `theory/signatures/sig_common.py`, which is not in the release list (see PW.4).

**New script:** `check_cmp_t3filter.py` with output `check_cmp_t3filter.txt`.

**Grade changes: none.** Every blind grade stands. The comparison adds one stronger fact under
PW.3b and confirms the T_3 result by a second, independent route.

## PW.4: the 18 pairs. Blind grade NONE, unchanged

- **Data agreement.** `data/witnesses.json` matches the bundle and my computation for all 18 entries:
  kind, L, both signatures (as multisets), exact Area/2π, T, ι and the number of shared coefficients
  (checked programmatically). The producer's `output/witnesses.txt` and `attack/a01_witnesses.txt`
  agree as well.
- **Shared count from coefficients or from the criterion?** From both, and they must agree.
  - `witnesses.py::record` calls `shared_exact(a, b, Lmax+2)`, which is `sig_common.shared`.
    Its docstring says this uses the actual cone coefficients b_l of Uçar.
  - It then asserts `sc == Lmax`, where `Lmax = level(Zi)` is the power-sum criterion (the first
    nonzero odd s_j).
  - So the coefficient count is computed and cross-checked against the criterion. I did not open
    `sig_common.py` (it is not in the release list), so the claim "actual b_l" rests on that
    docstring.
  - My blind check computed the c_j directly from first principles (and against Uçar), so the
    point is independently covered. The adversarial `a01` also used its own b_l.
- **Discrepancies:** none.

## PW.0 / PW.1 / PW.2: blind grades MINOR / SERIOUS / MINOR, unchanged

- **Numbers.** Every number in the proof.md §5 tables agrees with mine. The cone-count column is
  printed as "n vs n'" in increasing order, while the pairs are listed (larger, smaller). This is
  cosmetic.
- **PW.1 "previously 2π·14/5".** proof.md §5 itself labels the 22/15 pair "a pencil point", and
  `witnesses.py` records its recipe as "also audibility Thm C, Chen A.685". The producer knew the pair
  was the Theorem C(3) witness, so the "previously" sentence in `statements.tex` is a wording error,
  not a missing citation. The SERIOUS grade stands, because the sentence as printed contradicts
  Theorem C(3). The fix is the one given in REVIEW.md.
- **PW.2.** The linear-growth paragraph is identical in proof.md §5. No supporting script derives
  "≈ T/2−2" or "grows at least linearly". `a07_growth` concerns Theorem 4.1, not this paragraph. The
  MINOR grade and its fix stand.
- **"Abundance of real solutions" (PW.0 item 6).**
  - Supporting script: `real_shapes.py`, floating point and explicitly labelled as such.
  - It finds 35.3% of log-normally sampled real V giving three positive real roots.
  - proof.md §6 item 3 adds that for integral V ≤ 220 the proportion is about 0.7%, from the
    counters in the T_3 log (29,494,902 / 4,325,115,770 = 0.68%).
  - This agrees with my exact 0.65% for Y ≤ 24.
  - **Discrepancy:** the bundle's PW.0 item 6 drops this qualification. proof.md §6 states it
    correctly. My MINOR wording change stands: say "exist (an open set)", or keep the §6 sentence
    with both numbers.

## PW.3a / PW.5: the 25 and 61 counts. Blind grade MINOR, unchanged

`pencil_search.py::sets_m4(N)` loops `a, b, c` over [−N, N] and sets `d = −(a+b+c)` with **no bound
on d**. Its docstring and printout ("|entries| <= N") are therefore wrong. The family actually
searched is exactly my "mode 1" reading: {a,b,c,−(a+b+c)} with |a|,|b|,|c| ≤ N.

| quantity | producer | mine (mode 1) |
|---|---|---|
| sets at N = 130 (A and −A both kept) | 1,229,952 | 2 × 614,976 = 1,229,952 |
| configurations at N = 130 | 25 | 25 |
| configurations at N = 220 | 61 | 61 |
| pencil pairs at N = 220 (logged) | 352 | 88 classes × 4 non-trivial ordered-by-sign pairs = 352 |

The configuration sets are identical. As worded ("all entries ≤ N"), the counts would be 15 and 35.

**Discrepancy, a new detail:** the N = 220 run is not reproducible from the script defaults. It was
"run once in a scratch copy" (`pencil_log.txt`), and its result is imported from
`data/pencil_m4_N220.json`. My enumeration reproduces it exactly, so the content is right.

## PW.3c: the 1,592 count. Blind grade MINOR, unchanged

`pencil_search.py::sets_m5(N)` loops three entries a ≤ b ≤ c in [−N, N]. It solves the remaining
two from s1 = s3 = 0 with no bound, divides by the gcd and keeps A and −A separately. This is exactly
my "at least three entries in [−200,200]" family, and it gives 1,592 in both computations. The
printout "|entries|<=200" is wrong in the same way as at m = 4. With all entries ≤ 200 the count is
602. "No pencil pair" agrees (0 in both).

## PW.3b: "pencil phenomenon". Blind grade SERIOUS, unchanged, with a stronger reason

proof.md §7 states the converse honestly: "every balanced size-8 configuration is a pencil point"
is not proved, only observed for entries ≤ 80 (`attack/a04`: 7 configurations, all pencil).

- My direct search reproduces exactly **7** primitive witnesses with entries ≤ 80.
- At max entry 88 it finds (0;16,16,74,74) ~ (0;11,37,44,88), which has **no** pencil splitting.
- Five more non-pencil witnesses follow up to 440, including (0;77,88,182,208) ~ (0;68,112,154,221),
  which has distinct entries.

So the open converse of §7 is **false**. The a04 range (≤ 80) stopped just short of the first
counterexample.

**Required additional change** (proof.md §7, second bullet). Replace "its converse ... is **not**
proved. It is only observed: all 7 balanced size-8 3-configurations with entries $\le80$ are pencil
points" with:

> "its converse is false: all 7 balanced size-8 3-configurations with entries $\le80$ are pencil points, but $\{16,16,74,74\}\sim\{11,37,44,88\}$ is not; with entries $\le440$ there are 107 primitive balanced size-8 configurations, 6 of them not pencil points (review/audit-2/pte-witnesses/check_direct4.txt)."

The PW.3 sentence fix in REVIEW.md stands.

On the §7 question T^cone_3 = 8 (a balanced size-8 configuration containing ±1): my direct search
allows the entry 1, and none of its 193 collisions (orders ≤ 440) contains a 1. So there is no
3-vs-4-cone genus-0 pair sharing three coefficients with orders ≤ 440. This extends the "≤ 80" of
[Sig] §5 and of §7. It is a by-product of `direct4_N440.txt`; the count of order-1 entries was taken
with a one-line awk over that file and is not in a check script.

## PW.3d: smallest witness. NONE, unchanged

The producer gives the same smallest configuration (−28,−21,−5,−4,3,10,15,30).

## T_3: blind grade NONE, unchanged

| item | producer (`search_T3.c`) | mine (`check_t3.c`) |
|---|---|---|
| range | primitive V, v5 ≤ 220 | all Y (primitive or not), y5 ≤ 220 |
| V counted | 4,325,115,770 | 4,493,032,544 |
| coverage check | v5 blocks 1–5 … 216–220, 44 blocks, all present in the log; total line present | per-y1 counts checked against C(224−y1,4), total C(224,5) |
| cubic | K t³ − K S t² + M R_n t − M R_d | same cubic, monic form (e3 = (p3−p1³)/(3(1−p1 r)), e2 = r e3) |
| rejection rule | floating point (arm64: long double = IEEE double) with a stated error model: disc > 4·(error bound) ⇒ one real root; Smith inclusion disks (doubled, errors ≤ 64 ε) pairwise disjoint; root excluded if \|K′r − nearest int\| > K′·radius (only when K′·radius < 0.2); otherwise routed to sympy | algebraic: f mod p does not split for one of 16 primes > 220 (with 1 − p1 r a p-unit) ⇒ no rational X; no floating point |
| candidates verified exactly | 220,428 (220,352 undecided), 0 splits | 0 survivors |
| result | no collision | no collision |

I verified the producer's primitive count independently by Möbius inversion:
Σ_d μ(d)·C(⌊220/d⌋+4, 5) = 4,325,115,770 exactly.

**Is the producer's filter certified?**
- It is certified only up to its floating-point error model. The bounds (64·LDBL_EPSILON relative
  coefficient error, factor-4 and factor-2 safety margins, the 1e-9 absolute slack) are reasoned,
  not interval arithmetic, so it is not a proof-grade certificate.
- The history matters. `attack/a09` showed that the first version rejected 34 of 27,900 planted
  genuine rational U, with clustered roots and K′ > 1. The code was rewritten, and the full search
  was rerun with the current `decide()` (attack-log item 9, proof.md §6 "History").
- **My test of the current `decide()`** (`check_cmp_t3filter.py`): 536,277 planted genuine rational U
  with S ≤ 1100, false negatives 0. The families are:
  - all p/q with q = 2..33 (K′ > 1);
  - near-double clusters;
  - random denominators 2..12;
  - integer near-triple clusters {a,a+1,a+2}, {a,a,a+1}, {a,a+1,a+1}.

  Clustered roots go to the exact check (code 2) or are accepted.
- **Coverage gap check:** none. Clustered and repeated roots are routed (code 2) and never rejected.
  The guards K = 0 and M = 0 are impossible here, since S·R ≥ 25.
- My search is algebraically certified and independent of floating point. So the claim no longer
  depends on the producer's error model.

**Does the control really plant a positive?**
- It plants genuine positive rational triples U (families A–E, 53,324 cases, including K′ > 1 and
  near-double ones). It feeds their exact (S, C, R_n, R_d) to the same `decide()` the search uses,
  in `test` mode. These are real positives for the decision rule.
- It does **not** plant through the enumeration loop: no V is planted, and the gcd filter and the
  i128 sums are not exercised on a positive.
- It also covers a much smaller K′ regime than the search: R_d of five integers ≤ 220 can reach
  about 10^11, and K′ about 10^15. For K′ that large, `decide()` returns "undecided" (tol ≥ 0.2)
  and everything goes to the exact check (220,352 such cases).
- The loop itself is validated negatively, by exact agreement of the V-set and real-root counters
  with a sympy enumeration for v5 ≤ 30 (and a09 for v5 ≤ 45).
- My controls plant **through the full search loop** (a shifted target with a planted Y at y5 = 8
  and at y5 = 220).

**Discrepancy:** `search_T3.c`'s header and STATUS.md call the filter "certified"; it is certified
only relative to a floating-point error model. Suggested wording for proof.md §6: "rejects only when
certain under an explicit floating-point error model". The conclusion is now also established by
the exact modular search in this folder, which can be cited instead.

## Summary of discrepancies

1. `pencil_search.py`: the docstring and printout say "|entries| ≤ N" for m = 4 and m = 5, but the
   code bounds only three entries (m = 4: a, b, c; m = 5: a, b, c). Counts 25 / 61 / 1,592 are
   correct for the code's family. The N = 220 run comes from a scratch copy, not the script defaults.
2. proof.md §7's open converse ("every balanced size-8 configuration is a pencil point") is
   **false**. The first counterexample, {16,16,74,74} ~ {11,37,44,88}, lies just above the a04
   range (≤ 80).
3. T_3: the producer's filter is error-model-certified, not exact. The current version has 0 false
   negatives in my 536k planted cases. Its control does not plant through the search loop. My exact
   modular search independently confirms the result on a superset.
4. "Abundance": proof.md §6 qualifies it correctly (35% of log-normal real V, 0.7% of integral V);
   the bundle's PW.0 item 6 does not.
5. `witnesses.py` cross-checks the coefficient count against the criterion (assert). It relies on
   `sig_common.shared`, which I did not open.

Blind grades are unchanged: PW.4 NONE; PW.0 MINOR; PW.1 SERIOUS; PW.2 MINOR; PW.3a MINOR;
PW.3b SERIOUS; PW.3c MINOR; PW.3d NONE; PW.5 MINOR; T_3 NONE.
