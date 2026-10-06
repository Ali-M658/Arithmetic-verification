# G5-bis comparison: group `pte-growth`

Written after the blind `REVIEW.md` was committed and frozen. In this phase I read `theory/pte/proof.md`
§§0, 1, 3, 4, `theory/pte/statements.tex`, `theory/pte/growth.py`, `theory/pte/witnesses.py` (ODDEQ,
`shift_piece`, `doubling`, `scale_combine`), `theory/pte/pte_common.py` (`realise`), and
`theory/pte/attack/a06_*.txt` and `a07_growth.{py,txt}`. I ran `growth.py` (with `python3 -B`, so nothing was
written; `git status` shows no change under `theory/pte`). Its output matches the producer's: "ALL CHECKS PASSED".

**No blind grade changes.** One blind sub-point is resolved (the Lemma 1.5(3) citation, PG.0). Three
discrepancies are new; each is MINOR and sits in a proof, a sketch or a script, not in a statement.

## Summary

| id | existing proof vs my derivation | grade (blind → now) |
|---|---|---|
| PG.0 | agrees; the Chen survey citation is now confirmed | MINOR → MINOR (T^cone wording, B–I gap) |
| PG.1 | agrees, except the area citation; does **not** treat 1 ∈ X∩Y or the multiplicities | MINOR → MINOR |
| PG.2 | agrees; does **not** justify hyperbolicity of the cancelled realisation for T^cone (the script checks only instances) | MINOR → MINOR |
| PG.3 | agrees | NONE → NONE |
| PG.4 | agrees; evenness is hidden in "the proof of S2"; (b) takes a different but valid route | MINOR → MINOR |
| PG.5 | agrees; no explicit c in the proof | MINOR → MINOR |
| PG.6 | statement agrees; the sketch of (c) omits the second shift piece | MINOR → MINOR (one item added) |

## PG.0. Definitions 1.3, 1.4, Lemma 1.5

- **(1)** Agrees: translation preserves =_k.
- **(2)** The proof (proof.md l. 129–131) has the same count, M^n/n! against n^{L−1}M^{(L−1)²}, with
  "M > n!n^{L−1}". It agrees. The attack script `a06` checks the exact inequality for L = 2..7 with M = n!n^{L−1}+1.
  My script does it for L = 2..9 with M = n!n^{L−1}.
- **(3)** Agrees, with one difference in route. The proof applies [Sig] Lemma 5 to X ⊎ (−Y) without cancelling
  common elements first. That is still valid: X ⊎ (−Y) = −(X ⊎ (−Y)) gives X = Y on comparing positive parts. I
  cancelled first.
- **Upper-bound witnesses.** `witnesses.py` ODDEQ is identical to mine for L = 3, 5, 6, and contains mine for L = 4,
  plus extra pairs. The proof cites Chen's survey A.1.6, A.1.17, A.1.26, A.1.33. **I have now confirmed these in the
  fetched `sources/chen_survey_2506.11429.txt`.** My blind grep missed them because the file is detected as binary
  and I grepped without `-a`; that was my instrument error, not a missing source. The entries:
  - A.1.6: "Smallest solution, by computer search: [1, 5, 5]k = [2, 3, 6]k (A.48)". This agrees with my own exhaustive
    search.
  - A.1.17: (A.178) [1,13,17,23] = [3,9,21,21].
  - A.1.26: (A.266) [3,19,37,51,53] = [9,11,43,45,55].
  - A.1.33: (A.313) [7,91,173,269,289,323] = [29,59,193,247,311,313]; "Only the above four ideal non-negative
    solutions are known so far."

  So blind PG.0 wording item 3 shrinks to the Borwein–Ingalls numbering only. That is still an instrument gap.
- **L = 7.** Neither the proof nor statements.tex claims it. `a06` notes N_odd(7) ≤ N(11) = 12, which agrees with my
  "7 ≤ N_odd(7) ≤ 12". The Chen survey gives no (k = 1,3,…,11) solution with 7 terms; its (k = 1,…,11) text at
  pdf p. ≈248 is an identity, not a solution.
- Blind items 1 (T^cone wording) and 2 (state L = 2 as well) stand. Grade unchanged: **MINOR**.

## PG.1. Proposition 3.3

**Questions asked by the lead:**

- *Does the proof treat 1 ∈ X ∩ Y?* No. Proof.md l. 301–304 proves hyperbolicity of (0;V) by a bound that holds in
  every case. For n = 2, "Y contains at most one 1"; for n ≥ 3, the 2n entries of 2X ⊎ 2X give s ≥ n − 2. Then the
  proof says "If 1 ∈ Y∖X, exchange the roles of X and Y … The 1s are padding."
  - When 1 ∈ X ∩ Y, it never discusses the cone counts.
  - It never discusses the multiset reading of "1 ∈ X∖Y". My counterexample X = {1,1,5}, Y = {1,3,3} (V contains
    1, and the cone counts differ by 1, not 2) is not addressed.

  Note that for n ≥ 3 the proof's bound is computed on V *including* its 1s (they contribute 0), so the
  hyperbolicity part does survive the multiset reading. Only the cone-count sentence and the "(0;V)" notation fail.
- *Multiplicities.* Only "the multiplicity of 1 in X" appears. μ_Y is never used.

**Steps that differ from mine:**

- *Nonemptiness.* The proof uses x* = max supp(1_X − 1_Y): the multiplicity of 2x* in U − V is −2μ(x*) ≠ 0. This is
  equivalent to my top-exponent argument. It agrees.
- *Area.* The proof says "The area bound is Lemma 1.2(5)". Lemma 1.2(5) concerns the realisation of the
  **cancelled, primitive** Z (Area/2π < T/2 − 2). The pair of Prop. 3.3 is the **uncancelled** (0;U∖{1}),
  (0;V∖{1}), which can be different orbifolds. Its bound comes from the same one-line argument applied to V
  directly: |V| = 3n and every term is < 1. This is a mis-targeted citation, not a gap. New, **MINOR**.
  Fix: "The area is 2π(−2 + Σ_{v∈V}(1−1/v)) < 2π(3n−2), since |V| = 3n."
- *Sharing L coefficients.* The proof's only words for this are "The 1s are padding" ([Sig] Lemma 4 converse). The
  statement still does not say it.

Grade unchanged: **MINOR**. My blind replacement text (stated with μ_X and μ_Y) covers every point above.

## PG.2. Theorem 3.4

- **τ_L.** Agrees.
- **T_L.** Agrees with my construction: c with ι ≠ 0 and ρ(c) ≠ 0, c' large, λ = −ρ(c')/ρ(c).
  - The script `scale_combine` scales the *balanced* piece by t = −r_B/r_P. That is the same as scaling Z(c') by λ.
  - The proof's "ι = ι(Z(c))" leaves out the term sgn(λ)·ι(Z(c')) = 0. That is harmless.
  - The proof does not mention pairs {z,−z} inside Z(c), or even size. Both are covered by "after cancellation" and
    by ι being even. This is implicit, not a gap.
- **T^cone_L.** The lead asked: *does the proof justify hyperbolicity of the cancelled genus-0 realisation?*
  **No.** Proof.md l. 324–325 is all of it: "translate a solution of size N(2L−3) so that its least element is 1,
  and call the side containing 1 X. Then apply Proposition 3.3." The proof leaves three things unsaid:
  1. **Hyperbolicity of the cancelled realisation.** Def. 1.3 requires the genus-0 realisation of the cancelled,
     primitive Z to be hyperbolic, and Prop. 3.3 proves hyperbolicity only for the uncancelled pair.
  2. **That 1 survives cancellation**, so that Z is primitive and contains ±1.
  3. **That X ∩ Y = ∅.** This follows because a solution of the least size N(2L−3) cannot share an element
     (cancelling it would give a smaller solution). Without it, "the side containing 1" is ambiguous.

  `growth.py` (2) does test item 1, but only on instances: `realise(Zcn, genus0_only=True)` returns None when the
  pair is not hyperbolic, and the unpacking `ca, cb = …` would then raise, giving a nonzero exit. This happens for
  L = 2..7 with fixed ideal solutions. The general argument is in my blind REVIEW.md: |V*| ≥ L+1 entries ≥ 2;
  L ≥ 4 is immediate; L = 3 by excluding V* = {2,2,2,2}; L = 2 by example. The proof should include it.
  Blind finding confirmed; grade unchanged: **MINOR**.
- **Printed numbers.** The sizes differ from mine because different PTE solutions were used. Both sets respect the
  bounds:

  | L | growth.py: genus / balanced / cone | mine: T / τ / T^cone |
  |---|---|---|
  | 2 | 8 / 12 / 12 | 8 / 12 / 12 |
  | 3 | 16 / 16 / 24 | 16 / 16 / 22 |
  | 4 | 24 / 24 / 32 | 24 / 24 / 34 |

  This is not a discrepancy.
- **Script overclaim.** The `growth.py` docstring says "Every object is checked exactly and its pair is checked with
  the actual cone coefficients." For the balanced (τ_L) object, (2) only asserts `is_config`, ι = 0 and the size; it
  never realises or checks a pair. New, **MINOR**. Fix: change the docstring, or add the pair check for Zb.
- The "previous bound T_L ≤ 2^{2L−1} ([Sig] N(a))" citation is unchanged in the proof. Blind item 1 stands.

## PG.3. Theorem 4.1

The proof (l. 334–335) is three sentences and agrees with mine.

The lead asked: *does growth.py's floor check match mine?* **No, it tests something else.**

- `growth.py` (1) compares the Thm 4.1 bound with the [Sig] N1 bound, interval by interval on [4, 10^6]. It
  asserts new ≥ old, and new > old exactly on [13,15) ∪ [28, 10^6). I re-derived those intervals by hand and they
  are right.
- It does **not** test the identity "largest L with 3(L−1)²+1 ≤ A/2π, plus 1, equals ⌊√((A/2π−1)/3)⌋+2".
- That identity is checked in `attack/a07_growth.py` l. 70–73, at integer x ∈ [4, 5000). Since every breakpoint
  3m²+1 is an integer and both sides are constant on [k, k+1), integer points suffice for that range. My check
  (7493 exact points: breakpoints up to m < 1500 and ±10^{−9}, ±10^{−30} around them, plus A = 8π) reaches further
  and agrees.
- Both use the same exact floor-sqrt on Fractions.

`a07` also caught an earlier false parenthetical, "(the two agree on [4,28))". The current proof.md l. 337–339 has
the corrected text ("strictly larger exactly on [13,15) and on [28,10^6]"), which matches `growth.py`'s assert and
my re-derivation.

Grade: **NONE** (unchanged).

## PG.4. Theorem 4.2

- **(a)** The proof (l. 355–358) bounds |U|+|V| ≤ 2⌊A/π⌋+8 "by [Sig] (4.3) and the proof of S2". I could not check
  this from the statements alone (the S2 proof is not in my bundle). I re-derived it independently, and the
  derivation needs the evenness of |U|+|V|; the proof does not mention it. It is presumably inside the proof of S2.
  Proposition 2.2 is then used; I re-proved that inline. Agrees.
- **(b)** Different route. The proof uses (2L−3)^β ≤ (2L)^β and L = ⌊x/2⌋ with x = (A/6πC)^{1/β}. The "otherwise"
  case is "½x < 2 < 3 ≤ f(A)". Valid (it needs β > 0, again implicit), and it gives the same printed constant. Mine
  uses L = ⌊(x+3)/2⌋. `a07` checks claimed ≤ delivered for four (C, β) pairs on x ∈ [4, 3004]. Agrees.
- **(c)** Same as mine, including A = ((L+1)/c)^{1/α}, absorbing small k, and the closing remark on α ≤ 1. Agrees.
- **Truncation.** proof.md l. 350–351 reads "…iff $N(k)=O(k)$." So the statement in the source is complete, and the
  truncation is only in the extraction range (342–350 should be 342–351). Blind finding 1 confirmed as a
  bundle-builder defect.
- Blind items 2 (L ≥ 2) and 3 (β > 0) stand. Grade unchanged: **MINOR**.

## PG.5. Theorem 4.3

- The proof (l. 392–393) agrees: T_L ≤ 4N with Lemma 1.2(5) for f_g, and the Prop. 3.3 pair for f_n.
- For f_n it relies on the T^cone-style translated pair being covered by Prop. 3.3's first bullet. That holds,
  because a minimal PTE solution is disjoint (see PG.2 item 3).
- No definition of f_g, f_n beyond the loose sentence, and no explicit c. `a07` checks the thresholds only for
  L = 2..7 against the witness tables.
- Blind wording stands. Grade unchanged: **MINOR**.

## PG.6. statements.tex Theorem (Growth), and the commentary sentence

**Where the "any exponent above ½" commentary appears.** There are three places:

1. **proof.md §0 item 2 (l. 21–24):** "Any exponent above ½ would answer the open problem N(k)=o(k²) of
   Borwein–Ingalls (1994, §6, Q3) in a strong form."
2. **proof.md §4 "Consequence for the paper" (l. 374–376):** "An exponent >½ would prove N(k)=O(k^{2−ε}), which is
   stronger than the open problem 'N(k)=o(k²)'".
3. **statements.tex `rem:pteexponent`:** "Any exponent α>½ would give N(k)=O(k^{1/α}), which would settle in a strong
   form the open problem N(k)=o(k²) [§6, Q3]."

The algebra is correct in all three. α > ½ gives 1/α = 2 − ε with ε > 0, and O(k^{2−ε}) ⊂ o(k²). "Any quadratic
bound gives the exponent ½" is right too: (c) with 1/α = 2. "Linear growth of f is equivalent to N(k)=O(k), which is
implied by the conjecture N(k)=k+1" is right. The statement that ideal solutions are known only for k ≤ 9 and k = 11
matches CMSV p. 2. The Wright–Melzak values ½(k²−3) and ½(k²−4), and "B–I §6, Q3, 'No progress … for many years'",
are not checkable by me (instrument gap: Borwein–Ingalls and Melzak were not fetched).

**The sketch in statements.tex.**

- *(a)* Agrees, and is in fact better worded than Prop. 3.3. "(0;U) and (0;V), with any 1s removed" covers
  1 ∈ X∩Y. That is the form my blind wording proposes for Prop. 3.3.
- *(c), genus.* "shift a PTE solution X,Y of degree 2L−3 into (X+c) ⊎ (−(Y+c))". A single shift has
  s_{−1} = ρ(c), which is in general ≠ 0. The second, scaled, balanced piece λZ(c'), which proof.md and growth.py
  both use, is missing. New, **MINOR** (sketch only). Replace with: "For the genus, combine a shift
  $(X+c)\uplus(-(Y+c))$ with $\iota\ne0$ and a scaled balanced shift $\lambda\bigl((X+c')\uplus(-(Y+c'))\bigr)$
  chosen so that $\sum z^{-1}=0$."
- *(c), cone count.* "translate it so that it contains 1 and apply the doubling" is the same as proof.md, with the
  same unstated hyperbolicity of the cancelled realisation (PG.2).

Grade unchanged: **MINOR**. Blind items 1–4 stand, and the sketch item is added.

## Correction to my own blind files

`fetches.md` said Chen's survey had "no searchable 'Appendix A.1' heading". That was wrong: the extracted text is
detected as binary, and `grep -a` finds A.1.6, A.1.17, A.1.26 and A.1.33 at lines 19703–20946. This is recorded here
rather than edited into the frozen files. It does not change any grade, since the eslpower witnesses and my own
searches gave the same pairs.
