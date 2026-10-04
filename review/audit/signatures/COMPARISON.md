# Phase 2: comparison with the existing proofs (group SIGNATURES)

## Scope and method

**Read (read-only):** `theory/signatures/proof.md`, `attack-log.md` and `STATUS.md`.

**Ran:** `genus.py` and `cone_count.py`, together with their helper `sig_common.py`, from copies in `pinned/`.
- The SHA-256 hashes of the originals are in `pinned/SHA256SUMS`.
- The outputs are `pinned/genus.txt` and `pinned/cone_count.txt`. Both scripts exit 0.
- Nothing was written under `theory/`.

**Independent rebuild of the Theorem N constructions:** `check_their_constructions.py` (output in `.txt`).
- It is built from the text of proof.md §4 only, not from their code.
- It checks the result with this folder's own cone coefficients (`sigcommon.py`, derived from Uçar).

**Grades:** the REVIEW.md grades are unchanged. Addenda are in §(c).

## (a) Route and (b) discrepancies, item by item

| id | same route? | discrepancies |
|---|---|---|
| SG.0 | Same. | None. |
| SG.1 | Same: top term from i = 0, j = l+1; sign of B_{2l+2}. They check l ≤ 15, I check l ≤ 14 and also cross-check against Schueth. | None. |
| SG.2 | Same: p_l(1) = 0 converts the constant term into ψ-form. | Their proof writes p_l = Σ_{k=0}^{l+1} a_{l,k} x^{2k}, so a_{l,0} exists. The statement, which sums from k = 1, never shows a_{l,0}. See SG.4. |
| SG.3 | Same. | None. |
| SG.4 | Same bookkeeping; the converse goes through the area formula 2π(2g − 2 + \|U\| − R(U)). | Detailed below. |
| SG.5 | Same: odd e_j vanish (their Lemma 5, i.e. Newton parity), e_{T−1} = e_T · p_{−1}, even polynomial, then Z = −Z. | None. Their remark "positive real orders different from 1" is correct. The pinned run checks 97,920 pairs: no violation, 28,168 attain equality. |
| SG.6 | Same. | None. |
| SG.7 | Same, written as n + g − g' ≤ n + 4g ≤ A/π + 4. | None. |
| SG.8 | Different for part 2. They pad to N = ⌊A/π⌋ + 4 and invoke Theorem A. I use Cor S1 with g = g' = 0, which goes through Theorem S and does not need Theorem A. | None. Both routes are valid. Mine removes the dependence on Theorem A. |
| SG.9 | Same. Their integral ∫_0^1 y^{c/h−1} Π(1 − y^{2^r}) dy is mine after y = e^{−hs}. | None. |
| SG.10 N(a) | Same architecture, different blocks (detailed below). | No defect. |
| SG.10 N(b) | Different. They use an Egyptian fraction with distinct p_i ≥ 2. I use the doubling identity 1 = 1/2 + 1/2 (f′). | No defect. Mine is smaller and uniform (detailed below). |
| SG.11 | n/a | The stated numbers are confirmed: 1023 / 1025 for L = 6, 9 vs 10, 103 vs 104. "k ≥ 4 impractical" is specific to their route. |
| SG.12 | Same. | None. |
| SG.13 | n/a | ex:siggenus agrees: exactly 2 and exactly 3 shared, in my run and in theirs. The j-range wording defect stands. |

### SG.4 in detail

**The Σa_{l,k} = 0 sentence.** The defect I flagged is exactly this sentence, but it is a notation problem, not a false claim.
- In the proof of Lemma 2, a_{l,k} is defined for 0 ≤ k ≤ l+1 as the coefficients of p_l. Under that definition, Σ_k a_{l,k} = p_l(1) = 0 is correct, and it is the right reason.
- The statement of Lemma 2 shows only k ≥ 1. So a reader of the statement alone, as I was in the blind phase, reads Σ_{k=1}^{l+1} a_{l,k}, which equals −p_l(0) ≠ 0.
- Fix: write "Σ_{k=0}^{l+1} a_{l,k} = p_l(1) = 0", or introduce a_{l,0} in the statement of Lemma 2.

**The j-range.** "j odd, j ≤ 2L−3" is unchanged in proof.md and statements.tex, so this defect stands. Their Theorem S proof uses only positive odd j, so nothing downstream is affected.

**The converse.** It still lacks "(g;m) ∈ Sig". This is wording only.

### SG.10 N(a) in detail

Their blocks are 2i − 1 and 2i + 1 (h = 2). Mine are 3i − 1 and 3i + 2 (h = 3). The architecture is otherwise the same: one block with a single negative entry −1, one all-positive block, and a rational ratio of scalings. Point by point:

| question | their construction |
|---|---|
| Scaling-by-1 trap | Handled. The text says "doubling both if one of them is 1". In their construction it is also necessary, more so than in mine. V₀ contains the entry 1 twice: once from i = 1 ∈ T₁, since 2·1 − 1 = 1, and once from the added 1. A′ contains 1 from i = 0. So both scalings p and q must be ≥ 2, and the rule guarantees that. In the rebuilt construction min(p,q) = 1 never occurs for L ≤ 6. |
| Sign of r₀ | The text handles both signs, and also r₀ = 0, without proving which occurs. By my integral argument with h = 2, r₀ = Σ_{i≥1} ε_i/(2i−1) − 1 < 0 always. So the swap branch is always the one taken, and the r₀ = 0 branch is vacuous. The rebuild asserts r₀ < 0 for L ≤ 6. This is harmless. |
| Entries ≥ 2 | Holds; checked for L ≤ 6. |
| Cone counts | 2^D − 1 and 2^D + 1, checked for L ≤ 6; this gives 1023 / 1025 at L = 6. |
| Area bound | s(0;V) = −2 + \|V\| − R(V) < 2^D − 1 = 4^{L−1} − 1. Correct and strict. |
| Hyperbolicity | s ≥ −2 + \|V\|/2 > 0. Correct. |

"Exactly L shared" is claimed only computationally (L ≤ 6). My closed form for M_{D+1} proves it for every L. Theirs is not claimed for all L, so this is not a defect.

Rebuilt from the text, every L from 2 to 6 shares exactly L coefficients, for g' = 0 and 1. The L = 2 pair is (1;2,14,35) against (0;6,7,7,10,21), which matches their transcript.

### SG.10 N(b) in detail

| question | their construction |
|---|---|
| r₀/ρ ≥ 1 | Handled in the text by the harmonic start, and in the code by p = max(p, ⌈1/x⌉). I checked that this code is equivalent to the text. The branch is never exercised in the computed cases: r₀/ρ = 175/256 for k = 2, about 0.667 for k = 3 and about 0.667 for k = 4. |
| Distinct p_i | Imposed, but not needed. |
| Equal cardinality and exactly one 1 | Hold. The only 1 is the i = 0 entry of A. Every A′ entry is scaled by p_i ≥ 2, and every B′ entry by p_i ≥ 2 is ≥ 6. |
| Hyperbolicity | V ⊇ B ∋ 2, 3, plus at least two more entries ≥ 2. Correct. |

**9 vs 10 and 103 vs 104: verified.** My text-only rebuild with my own b_l gives 9 vs 10 sharing exactly 2, using 4 unit fractions (largest denominator 12 bits). It gives 103 vs 104 sharing exactly 3, using 12 unit fractions (largest denominator 7,471 bits). Their pinned run agrees, and its k = 2 pair is printed in `pinned/cone_count.txt`.

At k = 4 the ratio r₀/ρ has a 55-digit numerator, which confirms their impracticality remark for their route.

**My doubling construction (f′) gives smaller pairs.**

| k | their construction | doubling construction |
|---|---|---|
| 2 | 9 vs 10 | 5 vs 6 |
| 3 | 103 vs 104 | 23 vs 24 |
| 7 | not computed | 6143 vs 6144 |

All three doubling pairs are verified with the actual b_l and share exactly k. STATUS.md lists "the least cone count of a genus-0 pair with different cone counts sharing three coefficients" as open, citing 103 vs 104 as the only known example. **23 vs 24 is a new, smaller upper bound.**

### Searches

Their searches and mine cover different ranges and are consistent.
- My census found 6 pairs sharing 3 coefficients. All 6 have equal genus: the cone-order pairs {3,7,7,7,14} / {4,4,6,12,12} and {5,8,12,16,16} / {6,6,15,15,15}, each at g = 0, 1, 2.
- That agrees with their "no genus-changing pair shares three" (orders ≤ 16).
- The attack log reports that an earlier reviewer found the same sharpness example family at size 2L+2 that I found.

## (c) Grade addenda

The REVIEW.md grades are unchanged. Addenda:

1. **SG.4, finding 1.** Reclassified from "false justification" to "notation/cross-reference". The sentence is correct under the proof's definition of a_{l,k}, which includes k = 0, but it is unreadable from the statement. It stays MINOR. Fix: write Σ_{k=0}^{l+1}.
2. **SG.4 (finding 2, j-range) and finding 3 (converse hypothesis).** Confirmed present in the source. They stay MINOR.
3. **SG.11.** Confirmed route-specific: the k = 4 Egyptian ratio has a 55-digit numerator. It stays MINOR. In addition, the doubling construction improves the "open" upper bound for the least genus-0 pair with different cone counts sharing three coefficients, from 103 vs 104 to 23 vs 24. STATUS.md §"precise open question" and proof.md §7 item 2 should be updated.
4. **SG.10 (NONE).** Their construction handles every trap I listed: the scaling-by-1 guard, r₀/ρ ≥ 1, entries ≥ 2 and the area bound. There are no new findings.

There are no new SERIOUS or FATAL items.
