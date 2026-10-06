# G5-bis comparison, group `threshold-sharpness`

**What I read**, after the comparison phase was released and REVIEW.md was frozen:

- `theory/revision/thm513.tex`, `sharpness.tex`, `check_thm513.py` and `.txt`, `check_sharpness.py` and `.txt`,
  `collision_witnesses.csv`;
- `theory/stability/proof.md`, §4 (Prop. S3.2, Remark S3.3) and the "Not claimed" list;
- `theory/stability/attack-log.md`.

The directory listing of `theory/threshold/` and `review/audit/threshold/` was used for orientation only.

**New script:** `check_comparison.py`, output in `check_comparison.txt`. It is exact, asserts on failure, and ends
with ALL CHECKS PASSED.

## Grade changes

**None.** The blind grades stand: TH.1a NONE, TH.1b NONE, TH.1b-M NONE, TH.2 MINOR, TH.3 NONE.

One blind suggestion is withdrawn. Under TH.1b-M I proposed clarifying "783 remaining". In `thm513.tex`
the sentence reads "For each of the other 4745 sums … this covers 3962 sums, and the remaining 783 have explicit
pairs". So "remaining" means 4745 − 3962, which is exactly my reading, and the text is unambiguous. No wording
change is needed. The grade was NONE and stays NONE.

## TH.1a. Theorem 5.13

The existing proof, in `thm513.tex`, reads: "A collision has equal sums and equal R, and by
Theorem `thm:separation` none has sum at most 17; a triad of sum at most 17 cannot share `\keytwo` with one of a
different sum."

- **Agreement:** yes, it is the same argument as mine.
- **Discrepancy (presentation only):** the proof does not say *why* a triad cannot share the two invariants
  with a triad of a different sum. The reason is that S₁ = 12H₀ + 2 − R is a function of the first two
  invariants (eq:s1inv).
  - This is the only point that handles competitors of larger sum.
  - My blind optional suggestion stands: add ", since the first two invariants determine S₁ by (eq:s1inv)".
  - This is not graded.

## TH.1b. Collision-free sums, and the Method

**Exhaustive part (a) of `check_thm513.py`.**

- It enumerates *every* hyperbolic triad and compares the reciprocal sums as exact `Fraction`s:
  - at each of the 38 listed sums (the list is asserted to have 38 distinct entries, the largest 557);
  - at every S from 3 to 17.
- It covers all 38 sums. Its triad counts agree with mine at every one of the 38 sums, including 25,575 at 557.
- Agreement is complete.

**Part (b) of `check_thm513.py`, the 4745 collision sums.**

- The witnesses are read from `review/audit/diophantine/enum_4800.txt`, taking the first class listed at each S.
- Each witness is re-verified from scratch: distinct, sorted, same sum, hyperbolic, equal R.
- So the certificate does not trust the file. My C search produces its own witness at every one of these sums,
  and every one was re-verified with `Fraction`. The two are independent and agree.

**Part (c) of `check_thm513.py`, the scaling argument.**

- It scales a witness at d (18 ≤ d ≤ S/2, d | S) by S/d and re-verifies the result.
- "Covered" means some proper divisor d ≥ 18 carries a collision. That is the definition I used blind, and the
  counts agree: 3962 covered, 783 primitive.
- The scaling lemma itself is not proved in the script. It is used constructively, and each scaled witness is
  re-verified, which suffices for a computational certificate. The Method states the lemma correctly; my blind
  derivation shows that no hypothesis is missing.
- **Minor discrepancy (docstring only).** The docstring says the scaled witnesses are "produced independently
  of that file". In fact they are scalings of primitive witnesses that come from that file. This is
  harmless, because everything is re-verified, but the docstring overstates the independence.

**`collision_witnesses.csv` against my 783 sums.**

- 783 rows, all re-verified exactly.
- The set of S values is **identical** to my blind set of 783 primitive collision sums.
- In 781 rows the pair is the same as the first pair my C search found. The other 2 rows are different, equally
  valid pairs at sums with more than one collision fibre.

## TH.2 and TH.3. Sharpness

**Agreement.**

- `sharpness.tex` asserts exactly what I derived blind:
  - 1/k is sharp for arbitrary data;
  - for real orders the exponent is 1/2 and sharp at a double order (any n);
  - for real orders the exponent is 1/2 and sharp when n = k ≥ 3;
  - 1/k is not attained for k ≥ 3 with real data;
  - the witnesses for k ≥ 3 are non-real.
- Item (5) of `sharpness.tex` proves non-realisability by the same argument I used blind: the system of
  Theorem B is invertible at these data, so a real m′ would satisfy e(m′) = e(q_s).

**Discrepancies.**

1. **The hypothesis of the Remark 6.8 inequality.**
   - `theory/stability/proof.md` l. 351 (Remark S3.3) states it "for real d with |dᵢ| ≤ a".
   - The header comment of `sharpness.tex` says "(for dᵢ ≥ −a)".
   - `check_sharpness.py` (c) tests only |dᵢ| ≤ a, on a grid.
   - `attack-log.md` already notes that "|dᵢ| ≤ a is redundant for positive orders".

   Both hypotheses are correct: dᵢ ≥ −a is the exact condition (my blind identity
   Σ(3a dᵢ² + dᵢ³) − 2aΣdᵢ² = Σdᵢ²(a + dᵢ)), and |dᵢ| ≤ a implies it. So this is an internal inconsistency
   of wording, not an error. My blind MINOR wording ("real dᵢ ≥ −a (in particular |dᵢ| ≤ a)") makes the remark,
   the comment and the script agree.

2. **The bound in terms of δ.**
   - Remark S3.3 ends at "max|dᵢ| ≤ (|ΔP₃ − 3a²ΔP₁|/(2a))^{1/2}".
   - It never converts this into a bound in the heat-coefficient error δ, although the claimed exponent concerns
     δ.
   - The missing line: by the front-end rows (ST.2), |ΔP₃ − 3a²ΔP₁| ≤ (498 + 42a²)δ, so
     max|dᵢ| ≤ ((498 + 42a²)δ/(2a))^{1/2}.

   This was derived and checked exactly in my blind `check_sharpness.py`. It is a MINOR gap in the write-up and
   is folded into my existing TH.2 MINOR. It does not change the grade.

3. **Coverage of the checks.** `check_sharpness.py` checks the claims only at sample sizes:
   - n = k = 3 and a = 8 for the witness;
   - n = 3 and n = 4 for the family;
   - |d| ≤ a on a grid.

   Two claims are not tested by any script:
   - item (5), that the witnesses for k ≥ 3 are non-real and not realisable;
   - "all other data changes O(s²)" for general n.

   The "any n" and "any k" claims rest on the written argument. My blind script covers the family for
   n = 2..7, the witness for k = 2..6 and non-realisability for n = k = 3. The claims are true, but the script
   tests less than the text asserts.

4. **Are the 3 ≤ k < n cases settled anywhere?** No.
   - `proof.md` Remark S3.3: "No general statement for realisable data at mixed clusters is claimed".
   - `proof.md`, "Not claimed": "a general realisable-data exponent at mixed clusters".
   - `sharpness.tex`: "not settled".

   Nothing in the read files contradicts my blind sketch (confluent-Jacobian argument, exponent 1/2 at every
   multiple order for positive real data). The authors' "not settled" is accurate for the record. My
   strengthening stays an optional suggestion, not a grade.

5. **The abstract sentence.** `sharpness.tex` item (1) reads "for the coefficients of real orders it is 1/2 when
   all the orders are equal". The blind MINOR stands unchanged:
   - add n ≥ 2, or else it is literally false for n = 1;
   - say "positive real" orders;
   - optionally mention the double order and "sharp".

   Theorem 1.4, item (2), already covers the double order.

## Summary of discrepancies

| # | item | nature | effect on grade |
|---|---|---|---|
| 1 | Thm 5.13 proof does not say S₁ is determined by the two invariants | presentation | none (optional clause) |
| 2 | `check_thm513.py` docstring: scaled witnesses called "independent of that file" | docstring overstatement | none |
| 3 | 2 of 783 witness pairs differ from mine (other valid fibres) | none: both valid | none |
| 4 | Remark S3.3 "\|dᵢ\| ≤ a" vs `sharpness.tex` "dᵢ ≥ −a" vs script tests \|d\| ≤ a | wording inconsistency, both correct | inside the TH.2 MINOR |
| 5 | Remark S3.3 bound not converted to δ: (498 + 42a²) factor missing | write-up gap | inside the TH.2 MINOR |
| 6 | `check_sharpness.py` does not test item (5), non-realisability, or general n | script tests less than text | none (claims re-proved blind) |
| 7 | 3 ≤ k < n with real data: settled nowhere; blind sketch suggests 1/2 | open as recorded | none |
| 8 | "783 remaining" | blind suggestion withdrawn: the text is unambiguous | none |
