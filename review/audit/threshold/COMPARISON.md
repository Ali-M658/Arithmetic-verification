# Phase 2: blind review compared with the existing proofs

Read (read-only): `theory/threshold/proof.md`, `STATUS.md`, `attack-log.md`; `paper/main.tex`
sections sec:core, sec:threshold, sec:geometry and sec:density, and table tab:enum.
New script: `check_compare.py`, with output in `check_compare.txt`. It exits nonzero on failure, and every check passes.

The grades in REVIEW.md are unchanged. Two sentences of my blind report were inaccurate. Neither affects a grade. They are recorded in the errata at the end.

## Specific checks requested

**1. Odd-parity monotonicity (proof.md, Theorem 1(b)).** The claim is that "the odd-parity gap is strictly decreasing for S ≥ x*". **It is true.**
- φ_p′ has numerator −(S−3p−4)(3S−5p−4), confirmed. So φ_p is strictly decreasing for S > 3p+4.
- The correction 4/(D(D²−1)) has derivative −4(3D²−1)/(D²(D²−1)²) < 0.
- The real-variable odd gap φ_p − τ_p + 4/(D(D²−1)) is a sum of two strictly decreasing functions there, so it is strictly decreasing for S > 3p+4. Since x* = 3p+6+6/(p−1) > 3p+5, this covers S ≥ x*.
- An exact sweep over consecutive odd-D sums S ≥ 3p+4, for 2 ≤ p < 400, confirms it.

My blind report said "the odd gap is not monotone as a function". That is correct only at the very bottom of the range, and does not contradict the existing claim. The exact identity is

  gap_p(3p+3) = gap_p(3p+5) for every p.

Both equal 1/p + 1/(p+2) − 2/(p+1), checked symbolically and for p < 2000; for example gap_2(9) = gap_2(11) = 1/12. So strict monotonicity fails on S ≥ 3p+3, but it holds from 3p+5 on, and in particular on S ≥ x*. The existing proof states the restriction S ≥ x* explicitly, so it is correct.

**2. tab:enum against `tab_enum_reference.txt`.** The table matches entry by entry.
- 83 rows against my 83 triads.
- Same triads in the same order, and every R agrees exactly.
- The status column marks "collision" exactly for (2,8,8) and (3,3,12).
- R is distinct within each sum for S ≤ 17.
- There are no discrepancies. Fourteen R values repeat across different sums, which is not a collision; the table correctly does not mark them.

**3. The S = 3p+2 qualifier (Prop 3(1)).**
- At S = 3p+2 the formal gap is 0 for every p. There the "spread triad of stratum p+1", (p+1,p+1,p), is literally the balanced triad (p,p+1,p+1) of stratum p, and stratum p+1 is empty. Confirmed for p < 2000.
- The existing proof excludes this root in Theorem 1(a) ("for S ≥ 3p+3 every factor except S−x* is positive"), and Proposition 3(1) relies on (a). The *statement* of Proposition 3(1) does not carry the restriction.
- My MINOR grade on TH.6 stands. Fix: "for S ≥ 3p+3 (both strata nonempty)".

**4. The three per-p comparisons in the proof of thm:separation.** All are correct as written.
- p=2: τ₂ = 1/6. φ₂ peaks at 3p+4 = 10 and decreases on 11..18. φ₂(17) = 29/165 > 1/6, and φ₂(18) = 1/6.
- p=3: τ₃ = 1/6. φ₃ is unimodal with peak at 13. The endpoints give φ₃(12) = 7/36 and φ₃(17) = 11/63, both > 1/6.
- p=4: τ₄ = 3/20. φ₄(15) = 9/55 is the minimum of φ₄(15), φ₄(16) = 1/6 and φ₄(17) = 15/91, and 9/55 > 3/20.
- The stated ranges in which both strata are nonempty (11–18, 12–17, 15–17) are correct.
- The reduction to consecutive strata, via R⁺ non-increasing in p and within-stratum injectivity, is sound. The pair (4,5) is the last one needed for S ≤ 17, because stratum 6 first appears at S=18.
- The four comparisons at S=18 are reproduced: 3/4 = 3/4, 101/168 > 3/5, 15/28 > 21/40, 107/210 > 1/2.
- For p=2 the theorem's interval [R⁻_{S,2}, R⁺_{S,2}] is a formal interval: R⁺_{S,2} = 1 + 1/(S−4) is not attained. Disjointness still holds, since every other stratum lies below R⁻_{S,2}. This is the PC.11/PC.12 MINOR point; it is unchanged.

## Item by item: route and discrepancies

| item | route of the existing proof vs mine | discrepancies |
|---|---|---|
| PC.0 | statement only | none |
| PC.1 | thmA/thmB proofs go through thm:separation (case list); corD proof reads the coefficients off eq:a0conv and eq:a2red. Same logic as mine | none beyond the MINOR wording ("once the sum reaches 18") |
| PC.2 | paper quotes DGGW (5.7). I also re-derived it independently from the spectrum of S²/G | none |
| PC.3 | the same misattribution appears again in Scope (ii), line 160 ("constant-curvature orbifold cone has no curvature blow-up") | apply the PC.3 fix in both places |
| PC.4 | paper: Vieta on (z+1)^m − (z−1)^m, roots −i cot(jπ/m). Mine: Vieta on Im(x+i)^m, roots cot(jπ/m). Same route | none; the coefficients 2m, 0, 2C(m,3) are correct |
| PC.5, PC.6 | identical | none |
| PC.7 | identical | none (remark still recommended for deletion) |
| PC.8 | paper quotes eq:b1 and does not derive it. I verified it against Uçar, DGGW and Schueth, and independently at K=+1 | none |
| PC.9, PC.9b | identical (Newton's identity, eq:e3) | none |
| PC.10 | paper asserts it; I checked symbolically | none |
| PC.11, PC.12 | identical calculus | the p=2 caveat and the "fill" wording are still present |
| PC.13 | paper: Schur-convexity via convexity of 1/x. Mine: integer majorisation | "at fixed sum its extrema occur at the majorization-extreme configurations" is fine for the minimum, which is all that is used |
| PC.14 | identical | none |
| PC.15 | identical (φ/τ and unimodality) | none, see check 4 |
| PC.16 | identical | none |
| PC.17 | the localisation sentence is still in sec:density | SERIOUS stands |
| PC.18 | statement only | none |
| PC.19 | enumeration claimed "via interval-localization"; the conjecture stays as stated. Scope (iv), line 160, also says the quadratic growth "is supported by exact-arithmetic enumeration through sum 600" | SERIOUS stands; Scope (iv) also needs revision |
| PC.20 | remark only | SERIOUS stands |
| PC.21 | tab:enum | identical to my listing (check 2) |
| TH.0 | identical facts | none |
| TH.1 | different route for p=2 | proof.md first gets S ≥ 18 from the gap sign, then uses (2,5,S−7) with R > 7/10 against R⁻_{S,3} ≤ 1/3 + 60/224. I used (2,3,S−5) for S ≥ 12 plus a check at S=11. Both are valid; the bound and its monotonicity are verified |
| TH.2 | identical chain | none |
| TH.3 | even parity: same (proof.md factors φ−τ in S with roots 3p+2 and x*; I factored in D; equivalent). Odd parity: different route. proof.md uses monotonicity of φ plus the correction (check 1). I used the cubic g(D) and its sign pattern, so no monotonicity was needed. The 3p+7 branch is the same quantity: proof.md's −2(p²−5p−30)/(p(p+1)(p+3)(p+4)(p+5)) is my g(2p+7) after dividing out the positive factor. p ≤ 8: proof.md uses the seven gap(S*+1) fractions and monotonicity; I located the cubic's root | none. All seven fractions (−7/936, −1/72, −19/3960, −1/180, −76/15015, −1/231, −17/4680) and the odd gaps 1/840, 1/2310, 1/10296 are reproduced |
| TH.4 | proof.md: x*(p) − 18 = 3(p−2)(p−3)/(p−1) ≥ 0 (verified), uniform in p. Mine: S*(p) ≥ 18 via the S* table. Same logic; theirs is cleaner | none |
| TH.5 | both use enumeration | none; every row agrees. proof.md's extra §5 counts (first non-adjacent collision at 35, between strata 5 and 7) agree with my data |
| TH.6 | (1) even D: identical integrality and parity argument. (1) odd D: proof.md uses monotonicity (valid by check 1); I used the cubic root interval (2p+6, 2p+7). (2): identical window inequalities | the S ≥ 3p+3 qualifier is missing from the statement (check 3) |

## Addendum: grade changes

None. Every grade in REVIEW.md stands. No new FATAL or SERIOUS items. One related observation: the PC.3 and PC.19 problems also appear in the Scope paragraph (paper line 160, items (ii) and (iv)), and the fixes should be applied there too.

### Errata to my blind REVIEW.md (text only, grades unaffected)

1. Under "Independent proof of Theorem 1", the sentence "The odd gap is not monotone as a function" is imprecise. Corrected statement: the odd-parity gap is strictly decreasing for S ≥ 3p+5, hence for S ≥ x*. Its only non-strict step is gap(3p+3) = gap(3p+5). The existing monotonicity argument is correct.
2. Under PC.17, the sentence "The first such pair is the paper's own S = 36 example" is wrong. The first collision between non-adjacent strata is at S = 35: (5,15,15) and (7,7,21), with least orders 5 and 7 and R = 1/3. The S = 36 pair is a non-adjacent example from the paper itself, but it is not the first. The SERIOUS grade rests on the counts (2793 of 3067 pairs with S ≤ 600 are non-adjacent), which are unaffected.
