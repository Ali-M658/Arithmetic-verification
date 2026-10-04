# Comparison of the blind review with the existing proofs

Read only: `theory/curvature/{proof,STATUS,attack-log}.md` and `theory/divergence/{proof,STATUS,attack-log}.md`. The grades in REVIEW.md are unchanged; any changes are recorded below as addenda.

Exact support is in `check_comparison.py` / `check_comparison.txt` (run from the repo root; it exits nonzero on failure).

## Result in brief

- I found no new FATAL or SERIOUS item.
- No grade changes.
- One erratum in my own REVIEW.md (DV.1(c), pole list), with no effect on any conclusion.
- Two of my MINOR points (genus-10⁴ threshold, CU.1 wording) are confirmed as defects in the existing text.
- One additional MINOR gap: s_k > 0 is used but never proved. I supply the proof below.

---

## CU.0 Conventions

**(a) Route.** Identical text; nothing to prove.

**(b) Discrepancies.** None.

**(c) Grade.** NONE, unchanged.

## CU.1 Flat-cone input

**(a) Route.** Same inputs: Kokotov Prop 1 and Thm 1, then an orbifold = Friedrichs identification.
- My identification goes through Kokotov's description of the extension spaces (the orbifold domain contains the cutoff χ, which forces N = span{χ}), or equivalently through zero capacity of points.
- Theirs is the one-sentence justification added after their attack log F14.

**(b) Discrepancies.** Both defects I flagged are present in the proof text (proof.md §2, l. 65–70) exactly as in the statement:
- "only the bounded mode enters his deficiency space" is inaccurate: M = span{χ, χ log r}.
- DGGW Thm 4.8 is cited for the vanishing, but it gives neither the curvature-polynomial structure (that is Donnelly, reached via Uçar Thm 4.20) nor the O(e^{−ε/t}) remainder.

Their F3 check is a bookkeeping check of the K^l factor, as they say. The independent support for vanishing at K = 0 is Kokotov (F) itself.

**(c) Grade.** MINOR, unchanged.

## CU.2 Lemma 2

**(a) Route.** Same: character average, pole pairs, orbit counting. Their S1 check uses generated matrix groups (l ≤ 61). Mine uses Molien with exact class angles (l ≤ 40).

**(b) Discrepancies.** None in the mathematics.

Their "independent derivation of the spherical expansion" (S2: l ≤ 12, m ≤ 30) matches my Hurwitz computation (l ≤ 24, m ≤ 13), including m = 2. Both use Hurwitz zeta at negative integers, so the derivation is the same route.

Their §4 claim of novelty ("What is added here: an independent derivation…") is the point I flagged. The lemma is classical (Frobenius/Molien), and its role is as a cross-check.

**(c) Grade.** MINOR, unchanged.

## CU.3 Proposition

### Part 1

**(a) Route.** Same classification argument (n ≤ 4; 1/a + 1/b + 1/c = 1 with a ≤ 3) and the same constants.

**(b) Discrepancies.** None.

**(c) Grade.** MINOR, unchanged (the issue is prior art, not correctness).

### Part 2

**(a) Route.** Different, both correct.
- Theirs uses a fractional-part comparison of 12a_0 = 2n + 2/n, 3 + n + 1/n, 4, 7 1/6, 8 1/12, 9 1/30. I reproduced the table exactly.
- Mine uses divisibility (p | n and n | 2p) followed by a finite check.

**(b) Discrepancies.**
- Their argument treats the value 4 (S²) against S²(2,2,n) only implicitly. That case is immediate, since 1/n is never 0.
- The same "for every n" wording (n = 1 gives the same orbifold) is present.

**(c) Grade.** MINOR, unchanged.

### Part 3

**(a) Route.** Same: a black-box citation plus the witnesses. The values a_0(2,8,8) = 67/48, a_1(2,8,8) = −1601/480 and a_1(3,3,12) = −867/160 quoted in the divergence proof are reproduced exactly.

**(b) Discrepancies.** None.

The section 5 claim "non-decreasing in n (pad a witness with common cones)" lies outside my statement set. It is correct: adding a common cone to both members preserves agreement of the first k coefficients (the coefficients are additive over cones) and keeps χ < 0.

**(c) Grade.** NONE, unchanged.

### Part 4

**(a) Route.** Essentially the same. Their level-set argument uses AM–HM plus Lagrange (the centre is the only critical point), where I used strict convexity. Their "299 interior sample points" agrees with my interval α_1 ∈ [1/5, 1/2], which has 299 interior points k/1000 (exact).

**(b) Discrepancies.**
- The proof says "Scaled to equal area", so it is correct, while the statement says "have the same area". That is a wording mismatch between the statement and the proof.
- Neither the statement nor the proof names the Friedrichs extension for the non-orbifold cones.

**(c) Grade.** MINOR, unchanged.

### Strength paragraph

It agrees with my assessment. Their attack log F12 already narrowed it.

---

## DV.0 Notation

Identical. No discrepancies.

## DV.1 Lemma 1

**(a) Route.** Same: Bernoulli generating functions for (a), the substitution t = iy with positive series for (b), and the nearest poles for (c).

**(b) Discrepancies.**
- **Erratum in my REVIEW.md, DV.1(c).** I listed the points x = 2πn as poles of H, coming from 1/sin(x/2). They are not.
  - At x = 2πn the bracket (x/2)cot(x/2) − (kx/2)cot(kx/2) has cancelling residues, and it also vanishes there. So H is regular.
  - This is checked exactly for k = 2..5 and n = 1, 2.
  - The existing proof states this correctly ("the bracket vanishes").
  - My rates are unaffected: the nearest poles after ±2π/k are ±4π/k for k ≥ 3, and ±3π for k = 2, as both of us conclude.
- Their (c) proof gives O((2ρ)^{−N}) through Cauchy's estimate on |t| < 4π/k. That is correct for every k ≥ 2: for k = 2, G_2 is in fact analytic out to 3π > 2π.

**(c) Grade.** NONE, unchanged.

## DV.2 Theorem 2

**(a) Route.** Same as mine: c_n = ½A_n(1 + ε_n), a weighted sum, then tail bounds.

Their alternative derivation from the Dryden–Strohmaier weight is a genuinely different route. Their transcription of DS eq. (1) agrees with sources/ds_math0504571.txt l. 117–127. I did not reproduce their D4 numerics.

One technical point to note: DS state (1) for h entire of uniform exponential type, which the Gaussian h(r) = e^{−t(1/4 + r²)} is not. The use is standard, by approximation, but it deserves one sentence if the second derivation is printed. This is MINOR and outside the statement.

**(b) Discrepancies.** None. The l² limit π⁴/(32m⁴) agrees with mine (0.1903 for m = 2).

The "Equivalently" and "asymptotically" wording points stand.

**(c) Grade.** MINOR, unchanged.

## DV.3 Theorem 3

**(a) Route.** Same decomposition.
- Their bound on s_{l+1} uses an explicit ι_i formula. I verified exactly that it equals Uçar (4.35) for k < 60.
- Their bound |B_{2n}| ≤ 4(2n)!/(2π)^{2n} gives the stated O(l (2l)!/l! (2π)^{−2l}).

**(b) Discrepancies.**
- **Genus 10⁴ + {2}.** The proof and its attack log (F11) both say the smooth part dominates "for l ≤ 5". The exact value is l ≤ 8; it was computed twice, once via the independent closed form for β_l(2). The sign of a_l/K^l is also negative through l = 8. So no reading of "dominates" makes 5 the threshold. The figure was taken over from the attack log without recomputation.
- **n = 0 rate.** Their proof gives no argument for n = 0; it only states the n = 0 rate. Mine supplies one: (e_1 − 1)·l → 1, so the first limit converges at rate O(1/l), while the second converges at O(1/l) in all cases. Their D6 (1.0041 at l = 120 for genus 2) agrees with my values.
- **Ratio corrections.** "The (1 + c/l + ⋯) corrections … cancel to O(l^{−2})" holds for n ≥ 1, where the other error terms are exponentially small. This agrees with my measured l²(e_1 − M²) ≈ −2.5 for {3,3,12}.

**(c) Grade.** MINOR, unchanged.

## DV.4 Corollary 4

**(a) Route.** Same peeling procedure. My termination test is "first limit equals 1 if and only if n = 0", and theirs is the same ("the n = 0 case of Theorem 3 identifies this stage").

**(b) Discrepancies.**
- **New MINOR: s_k > 0 is assumed, never proved.** The statement lists s_k > 0 as an input, and the proof uses it in step 3, but nothing in either theory folder proves it, and Uçar does not state it.

  *Proof.* (Σ(2l+1)e^{−l(l+1)t}) = e^{t/4}·(1/t − Σ_k B_{2k}(1/2)(−t)^{k−1}/k!). Since sgn B_{2k}(1/2) = (−1)^k, the second factor has all coefficients positive, and so does e^{t/4}. Their product, which is Σ s_ν t^{ν−1}, is therefore positive. This is verified exactly for ν < 150 in check_lemma1.py.

  **Fix:** add this one line.
- **K is recoverable.** Their proof needs K. As noted in REVIEW.md, K is recoverable from the tail, so the hypothesis is removable. Neither the proof nor STATUS mentions this.
- **Uçar comparison.** Their literature note and attack log F16 agree with my reading of Uçar Thm 3.40: it is a large-order limit at the same rate, on W_{ν,1} extracted by induction from ν = 0 after subtracting the area term. So "tail-only" is the honest residual novelty, as both of us say.

  The curvature proof §5 (l. 289–291) says Uçar's proof "uses only heat invariants". That is consistent with this; it does not contradict the "starts at ν = 0" remark in DV.4.

**(c) Grade.** MINOR, unchanged. The s_k > 0 gap is MINOR because it has a one-line fix.

## DV.5 Borel reading

**(a) Route.** Same: Pringsheim in Kζ after a polynomial is removed.

**(b) Discrepancies.**
- The text again omits the hypothesis "n ≥ 1". For n = 0 with K = −1 every a_l/K^l is negative, and the radius is π².
- Citations: their Dunne check (attack log F15) agrees with my reading of Dunne eqs. (21)–(25). Li–Li–Tang is not discussed in their logs. I checked it (Example 2.30: Sing = {k²π²} for S²).

**(c) Grade.** MINOR, unchanged.

---

## Recommendations carried over

These are consistent with the existing STATUS files and my REVIEW.md.

- Keep the divergence material as a remark, which is also the authors' own recommendation.
- Present CU.3 Parts 1–2 as citations of DGGW and Uçar.
- Demote Lemma 2 to a cross-check.
- Fix the genus-10⁴ threshold (l ≤ 8).
- Add the s_k > 0 line and "n ≥ 1" in DV.5.
- Correct the deficiency-space sentence in CU.1.
