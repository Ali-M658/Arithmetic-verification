# G5-bis comparison phase: group `descent`

Written after the blind REVIEW.md was frozen. Files read in this phase:
- `theory/revision/descent.tex` (in full), `point3P.tex`;
- `check_descent.py` / `.txt`, `check_point3P.py` / `.txt`;
- `attack-log.md` (the F1 row and the descent rows of "what the reviewer tried to break");
- `review/audit/diophantine/check_groups.py` (DI.5 / DI.7 part);
- `theory/diophantine/novelty.md` §3, `RECOMMENDATION.md` §5.2, and `variety.md` (grep for isolation and torsion).

New exact checks for this phase are in `check_g_comparison.py` / `.txt` (15 asserts, exit 0).

## Grade changes

| id | blind | after comparison | reason |
|---|---|---|---|
| DE.0 | MINOR | MINOR (unchanged) | The proof does not define φ at Z = 0 either. It also asserts without proof that C_{27/2} is nonsingular |
| DE.1 | NONE | NONE | The proof agrees with my derivation, including the obstruction at p = 5 |
| DE.2 | NONE | **MINOR (raised)** | The proof contains a false sentence: the tangent at (16,400) meets E again at (16,400) itself, not at (16,-400). The conclusion, order 3, is right |
| DE.3 | NONE | NONE | |
| DE.4 | MINOR | MINOR | Neither the proof nor the diophantine notes ever restrict k to integers |
| DE.5 | MINOR | MINOR | |
| DE.6 | NONE | NONE | Identical to my result. One gap in a script, noted below |

No FATAL or SERIOUS discrepancy.

## DE.0: the model

**Agreement.** The proof shows three things by substitution: φ(C) ⊂ E, ψ(E) ⊂ C, and φ∘ψ = id_E. This is the
same as my check_a.

**Does the image argument hold? Yes.** The proof says the closure of ψ(E) is an irreducible curve in the cubic,
of geometric genus 1, so "not a line, a conic or a singular cubic, hence it is all of C_{27/2}, which is a
nonsingular cubic." The argument is sound. A nonsingular plane cubic is irreducible, so any curve contained in it
is the whole curve; the genus remark is not even needed. Then:
- φ∘ψ = id gives a birational inverse pair between two smooth projective curves, so both maps are isomorphisms;
- ψ∘φ = id holds on a dense open set, hence everywhere.

I checked ψ∘φ = id directly, and the two routes agree.

**Discrepancy 1 (minor, already in my blind DE.0 finding).** Nonsingularity of C_{27/2} is asserted in the proof
("which is a nonsingular cubic") without a reason. It is checked in `check_descent.py` (e) with `sp.solve` on
three charts. My check_a confirms it with a Groebner basis.

Suggested insertion: *"(C_{27/2} is nonsingular: Λ ∉ {0, 1, 9}, or directly, the partial derivatives have no
common zero)"*.

**Discrepancy 2 (my blind DE.0 MINOR, confirmed).** The proof never says how φ is defined at the three points
with Z = 0. Its only statement there is ψ(origin) = O, by the limit, which is correct. "Mutually inverse
isomorphisms" is true for the extended φ. My blind replacement text stands.

**Example.** φ(1:4:4) = (-24, 360) agrees with mine.

## DE.1: the descent

**Primes checked.** The question was whether the proof makes its local checks at all primes dividing 2dd'.
The proof does not compute Selmer groups prime by prime. It excludes each non-image class with **one** explicit
local obstruction, and that is sufficient:
- **E, d1 = ±2, ±3:** the proof works mod 5 (descent.tex (i)). This is exactly the prime I found to be the only
  obstructing one. The congruence argument is correct: the right side mod 5 takes only the values {2, 3}
  (check_g §3).
- **E', d1 < 0:** the real place, with the same negative-definite argument as mine.
- **E', d1 = 3, 5, 15:** the prime 3, with the mod-9 values 6, 6, 6 for d1 = 15 (check_g §3). My hand proof for
  d1 = 3 is the same as the proof's. I did not hand-prove d1 = 5 or 15; the proof's arguments for them check
  out. My code also found obstructions at 2 for these classes, which the proof does not need.

The parenthesis "every class is decided by a local condition, so no Tate–Shafarevich ambiguity arises" is
correct, because each obstruction is local.

**`check_descent.py` (c).** The script tests p in {2, 3, 5}, which is all p | 2dd', together with R. It finds an
obstruction for every class outside the image by exhaustive search mod p^k. That test is independent of the
printed congruences, which the script then also re-evaluates one by one. This agrees with my finding.

One caveat on the script: for classes inside the image, "no obstruction up to KMAX" is not a proof of local
solubility. That does not matter, because those classes are attained by torsion points, which the script checks.

**Result.** n1 = 4, n1' = 1, rank = 2 + 0 - 2 = 0. The proof matches mine.

## DE.2: torsion

**Agreement.** The proof uses the injectivity statement of Cremona p. 70 and #E(F_7) = #E(F_11) = 12. The point
orders are as listed, and since F1 the script asserts each point's order individually. All agree with check_c.

**Discrepancy 3 (new, MINOR).** descent.tex l. 81-82 says: "(for instance the tangent at (16,400) has slope 21
and meets E again at (16,−400))". The slope 21 is right. But the third intersection x is
m² - 393 - 32 = 16, and the tangent line has y = 400 there. E restricted to the line is (x-16)³ (check_g §1).
So **(16,400) is a flex**: the tangent meets E only at (16,400), with multiplicity 3. The point (16,-400) is not
on the line. The conclusion is still right: 2(16,400) = -(16,400) = (16,-400), so the order is 3. Neither
`check_descent.py` nor the attack log (F1 fix) checks this sentence.

Replacement text: *"(for instance the tangent at (16,400) has slope 21 and meets E only at (16,400), with
multiplicity 3, so (16,400) is a flex and 2(16,400) = (16,−400) = −(16,400))"*.

## DE.3 / DE.4 / DE.5: points, triads, isolation

**DE.3.** The proof's argument (12 points on C, distinct, hence all) agrees with mine.

**Scope of the script for the triads.** `check_descent.py` (e) checks the triads only at k = 1:
(2,8,8) and (3,3,12). The general k follows logically, and I enumerated every triple for k <= 60.

**"For every k".** The proof (l. 89-91), `variety.md` l. 239-252, `novelty.md` §3 and `RECOMMENDATION.md` §5.2
all say "for every k", and none of them states that k is an integer. If k is allowed to be a half-integer, the
claim fails: k = 3/2 gives the class {(3,12,12)}, with one member. My blind MINOR wording, "every integer
k ≥ 1", stands. The hyperbolicity line should also say that the entries are ≥ 2k ≥ 2.

**Isosceles census.** `review/audit/diophantine/check_groups.py` checks only the primitive (u,v,v) with
u, v ≤ 24, while `variety.md` claims all 1,482 triples with u ≠ v ≤ 39. My check_e confirms the full claim
of 1,482, all of order 6. So the printed claim is true; it just is not established by that particular script.

My blind recommendation stands: the general argument σ(Q) = -Q + (1:0:-1) proves every isosceles point has
order 6 and removes the hedge. Neither the theory nor the scripts contain that argument.

**PARI.** `novelty.md` and `RECOMMENDATION.md` still describe the PARI rank-0 certificate as the new content.
descent.tex replaces it with the descent, as the blind review recommended. Those notes should be updated to
cite the descent.

## DE.6: 3P

**Agreement.** `point3P.tex`, `check_point3P.py` and `check_groups.py` all give
3P = (162833463 : 723926268 : 287876366), and all say that the old print equals (1:0:-1) - 3P, the image of 3P
under Y ↔ Z. This is identical to my check_f. The old audit bug is gone: it compared the coordinates as a set,
and the comparison is now done on ordered, normalised points.

**Discrepancy 4 (script only, NOTE).** `check_point3P.py` does not assert the printed value
2P = (16352 : 288 : -365). It only puts the computed value in a PASS message about lying on the curve. My
check_f asserts it, and it is correct. Suggested fix: add `check(P2 == (16352, 288, -365), ...)`.

**Base point.** The script hard-codes O = (1:-1:0) and does not use that O is a flex. Its negation through O*O
is correct in general. Not a defect.

## Summary of discrepancies

| # | where | severity | text |
|---|---|---|---|
| 1 | descent.tex l. 34 | MINOR | nonsingularity of C_{27/2} asserted without a reason (it is true) |
| 2 | descent.tex l. 21-37 | MINOR (= blind DE.0) | φ undefined at Z = 0 points; the extension is not stated |
| 3 | descent.tex l. 81-82 | MINOR (new; DE.2 raised NONE → MINOR) | "meets E again at (16,−400)" is false: (16,400) is a flex |
| 4 | descent.tex l. 89-91 and the notes | MINOR (= blind DE.4/DE.5) | "for every k" needs "integer k ≥ 1" |
| 5 | check_descent.py (b) | NOTE | the printed ψ is never evaluated symbolically; the script tests an algebraically equal form (equality proved in check_g §2) plus the limit at the origin; ψ∘φ = id is not checked (the proof does not need it) |
| 6 | check_descent.py (e) | NOTE | triads checked only at k = 1 |
| 7 | check_point3P.py | NOTE | the printed 2P is not asserted |
| 8 | check_groups.py vs variety.md | NOTE | the isosceles census in the script covers u, v ≤ 24 primitive, not the claimed 1,482 with ≤ 39 (true by my check_e) |
| 9 | novelty.md, RECOMMENDATION.md | NOTE | still present the PARI certificate as the rank-0 proof |

Contamination: none beyond the files released for this phase.
