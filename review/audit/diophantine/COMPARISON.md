# Phase 2: comparison of the blind review with the existing proofs

Read (read-only): `theory/diophantine/variety.md`, `RECOMMENDATION.md`, `families.py`,
`ranks.py`, `cubic_group.py`. The grades in REVIEW.md are unchanged. Changes are recorded as
addenda in Section (c). One new script was added: `check_theorem5_family.py` (output in
`check_theorem5_family.txt`).

## Summary of addenda

| item | blind grade | addendum | reason |
|---|---|---|---|
| DI.5 | NONE | **MINOR** | The proof text says "Distinct choices give distinct classes" and "multiplied by any m give classes". Both are literally false, though the conclusion stands (see DI.5). |
| DI.10 | MINOR (provisional) | **NONE** | The family is now visible. Multiplicity 6, the 1/8, the densities, uniformity and the constant 3/(128π⁴) are all verified exactly. |
| all others | unchanged | none | |

No SERIOUS or FATAL item. The existing proofs contain no mathematical error that affects any statement.

---

## DI.1 Proposition 1

(a) variety.md states Proposition 1 with no written proof. My lcm/gcd argument fills that gap. (b) The
two wording issues confirmed in REVIEW.md stand. "Primitive sums s_i" leaves primitivity of t_i
implicit. "Form a degeneracy class" should be "lie in". RECOMMENDATION.md's own table shows the issue: at S=408 the class is
the rescaled S=136 triples plus (65,70,273). (c) No change (MINOR).

## DI.2 Pencil, model, fibres, torsion

(a) Same route in substance. Their maps to BGN are the ones I verified, and their model
y² = x³+(λ−3)²x²+… is mine translated by s = x+4 (identical c₄, c₆). The fibre types are computed in a
script I did not read; my derivation agrees.
(b) **Base-point orders, checked against the text.** variety.md §2 reads "The six base points
(1:0:0),(0:1:0),(0:0:1),(1:−1:0),(0:1:−1),(1:0:−1) are sections of orders 1,2,3,3,6,6 (base point
O=(1:−1:0))". Read in order this is wrong: the correct orders are 6, 6, 2, 1, 3, 3. `cubic_group.py`
lists `TRIVIAL` in the same order but never asserts orders. `ranks.py` asserts only that (1,4,4) has order 6. So the
error lives in the prose alone, and nothing computed depends on it. The multiset {1,2,3,3,6,6} and the
conclusion "generic Mordell–Weil group Z/6" are correct. (c) No change (MINOR).

## DI.3 Reciprocation, dual family

(a) Identical route: the line through T₂, then the line through O. The counts 1753/423/1330 are reproduced
exactly by my independent enumeration. (b) The text gives no proof that "any other pair on the same curve
differs by a point of infinite order". It rests on the data ("none of those 1,330 differs by torsion").
My lemma supplies the proof: positive torsion points are isosceles or geometric progressions, and
in both cases the coset consists of permutations of t and its dual. The "12 points" claim again
holds only for non-torsion P. (c) No change (MINOR).

## DI.4 Proposition 2

(a) Same route: partial fractions by pole, partitions {1,1,1}, {2,1}, {3}, and AM–HM for the
mismatched {2,1} case. (b) **Scaling-family defect, checked against the text.** The proof disposes of the case {3}
with "The case {3} is a single ray." The authors therefore know the all-proportional
family is degenerate. The statement still does not exclude it, so ℓ(u,v)(2,8,8), ℓ(u,v)(3,3,12) satisfies it
literally. A second, harmless imprecision: "equal S forces equal sums of the c_i at each pole"
holds only when the poles' linear forms are independent, i.e. at most two poles. With three poles the three forms
satisfy a linear relation. The {1,1,1} case does not need it, because matching charges 1/c = 1/d already give
c = d. (c) No change (MINOR). Fix as in REVIEW.md: add "entries of t not all proportional".

## DI.5 Theorem 3

(a) Same route: (4,9,18) on C_{155/12}, nP ≠ O for n ≤ 12 plus Mazur, odd multiples on the egg, lcm
rescaling. (b) **Discrepancy.** The proof ends "Any k of them, rescaled to the lcm of their sums and
multiplied by any m, give classes of size ≥ k. Distinct choices give distinct classes."
- Two different k-subsets with the same lcm L give the *same* class: the class at sum L contains every point
  whose primitive sum divides L.
- Multiplying by m gives scaled copies, which are not primitive classes.

The conclusion still holds. Only finitely many triples have primitive sum below any bound,
so the lcm values L are unbounded. Each L gives a primitive class, by the gcd argument of
Proposition 1, of size ≥ k. (c) **Addendum: NONE → MINOR.** Fix: replace the last sentence
with "since only finitely many of the points have primitive sum ≤ B, the lcm L is unbounded over the
choices, giving infinitely many distinct primitive classes".

## DI.6 / DI.11 Ranks and first fibres

(a) Their route is PARI `ellrank` with r1 = r2 (pinned script, reproduced exactly). Mine adds an independent 2-isogeny descent
proving every rank unconditionally. (b) No discrepancy. The RECOMMENDATION.md enumeration table agrees with my
independent C enumeration in every entry I can compute:

| S | pairs | classes | primitive classes | largest fibre |
|---:|---:|---:|---:|---:|
| 100 | 92 | 92 | 69 | 2 |
| 200 | 386 | 380 | 243 | 3 |
| 600 | 3067 | 2977 | 1714 | 4 |
| 1000 | 7641 | 7386 | 4040 | 4 |
| 2000 | 25042 | 24127 | 12210 | 5 |
| 3000 | 48574 | 46755 | 22657 | 5 |
| 4000 | 77203 | 74234 | 34721 | 5 |
| 4800 | 102719 | 98742 | 45167 | 6 |

The first-fibre table and "no size 7 ≤ 4800" also agree. (c) No change.

## DI.7 Isolation

(a) Their route uses `ellrank` r2 = 0, citing the manual's "unconditionally", together with an explicit 12-point list from
`cubic_group.py` (base points plus translates by (1,4,4)). It is the same as mine. Mine adds:
- the 2-isogeny descent, Sel^φ = {±1, ±6} and Sel^φ′ = {1}, which proves the rank independently of PARI;
- a check of `ellrank.c`: no GRH path is used for curves with a rational 2-torsion point;
- an explicit bijection of the 12 plane points with PARI's torsion points.

Their 12-point list is the six base points and their translates by (1,4,4); mine is generated by closure. The two lists are identical.
(b) The isosceles torsion claim is "(as far as tested)" in their text. It is provable in two
lines (2P = (1:0:−1), which has order 3). (c) No change (NONE, with the optional upgrade).

## DI.8 Copies kD hyperbolic

(a) The text, variety.md §7, is the statement itself: "Indeed, if D is the reduced dual pair of a primitive t,
then R_D = G/e₃ ≤ e₂/e₃ ≤ 3". (b) **Checked against the text.** The argument covers only dual pairs, while the
sentence claims every primitive pair. Every D actually fed into (*) in Theorems 4 and 5 *is* a reduced dual pair:
D_{u,v} is the dual pair of (u,v,v), and the bundle pairs are dual pairs of (u,vq,vr). So the
argument is sufficient for every use. Only the general wording overreaches, and R ≤ 3 holds trivially for any
positive triple. (c) No change (MINOR, wording).

## DI.9 Theorem 4

(a) Same route. Their area "Y log2/3" is for the full quadrant {u,v>0}, and they then halve for u<v. This
agrees with my log2/6 for u<v, so the possible factor-2 slip I raised blind does not occur.
Their class argument (a+2b=S, 1/a+2/b=R quadratic in b) is equivalent to my 2r²+(5−λ)r+2=0.
(b) No discrepancy. Their "partial summation gives c_iso X log X + O(X)" matches my numerics
(secondary term ≈ −0.479 X). (c) No change.

## DI.10 Theorem 5: resolved

**The family** (variety.md §7). Take coprime q ≤ r ≤ M = y^{1/8}, coprime u,v ≥ 1 and t = (u, vq, vr), with α = q+r and β = qr.
The dual pair of t divided by v is
{(αu+βv)(u,vq,vr), (u+αv)(βv,ur,uq)}, with common sum Q = (αu+βv)(u+αv) ≥ S_D. Verified
symbolically: e₂(t) = v(αu+βv) and e₁(t) = u+αv. The fibres are the lines through (1:0:0) of slope q:r,
which the dual map sends to conics. This is the "conic bundle". Only the dual family is used. My blind guess that it was the pencil e₂/e₁² = const
was wrong, but immaterial.

1. **Multiplicity: 6 is correct.** Given a reduced pair D, a tuple (q,r,u,v) is determined once one
   chooses which member is proportional to (u,vq,vr) (2 ways) and which entry plays u (3 ways). The
   order q ≤ r removes the remaining transposition, so there are at most 6 tuples. My blind worry about 12 came from
   counting S₃-orderings, which this parametrization already quotients. **Exhaustive check** for Q ≤ 60000
   (46,067 non-GP tuples, 24,353 distinct D): tuples per D are distributed as {1: 12180, 2: 5961, 3: 4115, 4: 1260, 5: 442,
   6: 395}. The maximum is 6 and it is attained. 6,925 pairs D are reached from two different slopes, i.e. the second member is again a
   bundle point. Dividing by 6 is therefore exactly right for a lower bound.
2. **Where the 1/8 comes from, and uniformity.** For each (q,r) the box [1,U]×[1,V], with V = √(y/(4αβ)) and U = βV/α,
   satisfies Q ≤ 4αβV² = y, using β/α ≤ α. It contains (6/π²)UV + O((U+V) log y) = (3/(2π²)) y/α² + O(M√y log y)
   coprime pairs. The error is uniform in (q,r), since U+V ≤ (α+1)V ≤ (2M+1)√y. Summed over the ≤ M² slopes the total error is
   O(M³√y log y). This is o(y) iff M = y^θ with θ < 1/6, and θ = 1/8 is a valid choice. So the 1/8 is a
   uniformity cutoff that turns Σ 1/α² ~ (3/π²) log M into (3/(8π²)) log y. The count is uniform.
3. **Coprimality densities: correct.**
   - 6/π² applies to (u,v), coprime with no congruence condition.
   - For (q,r), Σ over coprime q ≤ r ≤ M of 1/(q+r)² is at least Σ_{n≤M} φ(n)/(2n²) ~ (3/π²) log M. Here n = q+r, there are φ(n)/2 pairs per n ≥ 3, and n=2 contributes the single pair (1,1). Checked numerically: at M = 1000 the left side is 2.1668, the φ-sum is 2.0735, and (3/π²) log M = 2.0997.
   - No local correction at 2 or 3 is needed, because only the upper bound S_D ≤ Q is used. Reduction by the gcd only helps.
   - Imprecision in their text: "Sum over coprime q ≤ r ≤ M, using Σ_{n≤M}" is used as a lower bound. It is a valid lower bound, though the text reads it as an asymptotic for the full sum.
4. **The constant, recomputed exactly** (sympy, `check_theorem5_family.py`):
   c_A = (3/(2π²)) · (3/π²) · (1/6) · (1/8) = **3/(32π⁴)**, for A(y) ≥ c_A y log y (1+o(1)). Then (*) is restricted
   to S_D ≤ X/8, where #{k ≥ 4} ≥ X/(2S_D), and partial summation gives Σ 1/S_D ≥ (c_A/2) log²X. Hence
   N(X) ≥ (1/2)(1/2) c_A X log²X = **3/(128π⁴) X (log X)²**. **The stated constant is correct.** It is
   not optimal for the method: θ ↑ 1/6 and #{k ≥ 4} ~ X/S_D on S_D ≤ X/log X give 1/(16π⁴). That is a remark, not an error.
   On the computed range the family alone gives 24,353 pairs with S_D ≤ 60000, against c_A y log y = 635.
5. **Final grade addendum: DI.10 MINOR (provisional) → NONE.** The proof is complete and correct. Optional
   remarks:
   - say "≥" for the φ-sum step;
   - note that θ = 1/8 is any admissible θ < 1/6;
   - note that Theorem 5 is stated for pairs only (RECOMMENDATION.md §3 already says so).

## Other observations from the read files (no grade impact)

- `ranks.py`'s docstring cites the manual's "computed unconditionally". As established in the P5 verdict, this is correct
  for the five curves (each has a rational 2-torsion point, so no `Buchall`). It would be worth one sentence in the
  paper's appendix.
- RECOMMENDATION.md §4 lists Beauville and Schoen as fetched. I did not fetch them, and no graded item depends on them.
- Their Theorem 3 cites "density of ⟨2P⟩ in the identity component" as an alternative to BGN for odd multiples
  being positive. That is valid: the real component group is Z/2 and P lies on the egg.
