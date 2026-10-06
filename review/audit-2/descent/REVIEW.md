# G5-bis blind review: group `descent`

Reviewer inputs: `review/audit-2/REVIEWER-BRIEF.md`, `review/audit/G5-VERDICT.md`,
`review/audit-2/statements/descent.md`, the DI.* items of `review/audit/statements/diophantine.md`
(DI.1 to DI.11, for the definitions of C_lambda, S, R, classes and hyperbolicity), and
`review/audit-2/sources/cremona_ch3.txt` (Cremona, *Algorithms for Modular Elliptic Curves*, 2nd ed., ch. III).
All code is in this folder. Each `check_*.py` uses exact integers, `Fraction` and sympy 1.14, asserts every
claim and exits nonzero on failure. Each `check_*.txt` was produced with
`/opt/homebrew/Caskroom/miniforge/base/bin/python3 check_x.py > check_x.txt`. All six exit 0.
The shared helper `descent_lib.py` holds the group laws, written from scratch.

## Summary table

| id | statement | grade | one line |
|---|---|---|---|
| DE.0 | phi, psi mutually inverse Q-isomorphisms C_{27/2} <-> E, psi(origin) = O | **MINOR** | True, and it is not a twist. The printed phi is undefined at the three rational points with Z = 0, including O. "phi(O) = origin" holds only for the extended morphism |
| DE.1 | 2-isogeny groups {+-1,+-6} for E, {1} for E'; rank 0; no Sha ambiguity | **NONE** | Re-derived: n1 = n2 = 4 and n1' = n2' = 1, so rank = 2 + 0 - 2 = 0. Independently, full 2-Selmer has order 4 |
| DE.2 | E(Q) = Z/2 x Z/6, the twelve points, orders, #E(F_7) = #E(F_11) = 12 | **NONE** | All orders and counts confirmed. Lutz-Nagell gives the same twelve points |
| DE.3 | the twelve points of C_{27/2}; the positive ones | **NONE** | Confirmed, and also by a brute-force search with \|coords\| <= 80 that does not use the descent |
| DE.4 | triads with S_1 = 18k, R = 3/(4k) | **MINOR** | True for positive integers k. False if k is only assumed to make 18k an integer (k = 3/2 gives one member). Add "k a positive integer" |
| DE.5 | Theorem 5.16 (isolation) as printed | **MINOR** | Mathematically true for every positive integer k. Wording fixes: "every k" should say positive integer k. Rest the proof on the descent rather than on PARI. The "(as far as tested)" hedge on isosceles torsion can be replaced by a two-line theorem: every isosceles point has order 6 |
| DE.6 | 3P = (162833463 : 723926268 : 287876366) on C_{155/12}, base O = (1:-1:0) | **NONE** | The corrected claim is right. The old printing is sigma(3P) = -3P + (1:0:-1): the same unordered triad, but a different point |

No FATAL or SERIOUS finding. The G5 P5 verdict ("CONFIRMED, UNCONDITIONAL") is reproduced without PARI,
by my own 2-isogeny descent (Cremona (3.6.2)) and by an independent full 2-Selmer computation.

## Contamination

None. I opened only the files listed above. I did not open `theory/**`, `paper/**`, `review/referee-sim/**`,
any other file of `review/audit/` beyond `G5-VERDICT.md` and `statements/diophantine.md`, or any other
group's scripts or outputs. Within `statements/diophantine.md` I read lines 1-256, which are the header and DI.1
to DI.11. That range includes the context items DI.6, DI.7 and DI.11 that my bundle names. I did not read the
PC.* items.

## Instrument gaps

- PARI/GP and Sage are not installed on this machine (`which gp sage` is empty, and `cypari2` is absent), so
  there is no PARI cross-check. None is needed: every claim is certified by exact code of my own.
- I did not consult the PARI/GP manual statement quoted in DE.5 ("the upper bound r_2 = C - T - s is computed
  unconditionally"). It is not among my sources. I neither confirm nor refute it, and my recommendation
  below makes it unnecessary.
- The independent full 2-Selmer route (check_b, second half) uses one standard input that is **not** in the
  fetched Cremona chapter: |E(Q_p)/2E(Q_p)| = |E(Q_p)[2]| * |2|_p^{-1}, and |E(R)/2E(R)| = 2 when Delta > 0.
  It is used only as an upper bound for the local images, which the code then fills with explicit points.
  The main route, (3.6.2), does not use it.
- The group-law facts used in (a) and (f) are not in the fetched text either: on a smooth plane cubic with a
  rational point O, P + Q = O*(P*Q) defines the group, and an isomorphism of curves that maps base point to
  base point is a group isomorphism. They are checked numerically instead: associativity on 343 triples;
  psi(P+Q) = psi(P) + psi(Q) on 36 pairs; and the same 2P and 3P through the BGN Weierstrass model.

---

## DE.0: the isomorphism (grade MINOR)

**Equation.** By DI.1, C_lambda is (X+Y+Z)(XY+YZ+ZX) = lambda XYZ. For lambda = 27/2 the integral form is
F = 2 e1 e2 - 27 e3.

**Nonsingularity.** The Groebner basis of (F_X, F_Y, F_Z) contains X^6, Y^6 and Z^6, so the partials have no
common zero in P^2(Qbar). E: y^2 = x^3 + 393x^2 + 3456x = x(x+9)(x+384) has the cubic discriminant
d^2(c^2 - 4d) = 3456^2 * 140625 != 0. The b-invariant formula of Cremona section 3.1 gives
Delta = 26873856000000 = 2^18 3^8 5^6 (check_a).

**phi maps C into E.** The numerator of y^2 - x(x+9)(x+384) at (x, y) = phi(X:Y:Z) lies in the ideal (F) of
Q[X,Y,Z]. **psi maps E into C**: identically F(psi(x,y)) = -21600 (y^2 - x(x+9)(x+384)).

**Mutual inverses.** phi(psi(x,y)) = (x, y) modulo the equation of E. psi(phi(P)) x P has all three
2 x 2 minors in (F), so psi(phi(P)) = P projectively on C. The point psi(x,y) is never the zero vector:
25x + y = 25x - y = 0 forces x = 0, and then 4(x - 216) != 0. So psi is a morphism on the affine part of E.
In weighted coordinates x = u/w^2, y = v/w^3 it sends the origin (w = 0) to (1:-1:0) = O. Both curves are
smooth and projective, psi is a morphism, and it has a rational inverse. Hence psi is an isomorphism, and it is
defined over Q, because both maps have rational coefficients.

**Not a twist.** No twist can arise, because the inverse maps are Q-rational. As a check, #C(F_p) = #E(F_p) for
all p in {7, ..., 43}, with a_p = -4, 0, 2, -6, -4, 0, 6, 8, 2, 6, -4. A nontrivial quadratic twist would change
a_p to -a_p at the inert primes, and a_p != 0 at p = 7, 13, 17, ...

**Group law.** psi(P+Q) = psi(P) + psi(Q) on all 36 pairs from a generating set of torsion (check_a). Here the
right side is the chord-tangent law on C with base O.

**Every printed point.** The images under psi are:

| point of E | psi(point) |
|---|---|
| O | (1:-1:0) |
| (0,0) | (0:0:1) |
| (-9,0) | (1:1:4) |
| (-384,0) | (4:4:1) |
| (-24, ±360) | (1:4:4), (4:1:4) |
| (-144, ±2160) | (1:4:1), (4:1:1) |
| (16, ±400) | (1:0:-1), (0:1:-1) |
| (216, ±5400) | (1:0:0), (0:1:0) |

phi maps each image back, wherever Z != 0.

**Defect (MINOR).** The printed phi has Z in its denominators. It is undefined at the three rational points of C
with Z = 0, namely O = (1:-1:0), (1:0:0) and (0:1:0). So "phi sends O to the origin" is true only for the
extension of phi to the smooth projective curve; the extension maps (1:0:0) to (216, 5400) and (0:1:0) to
(216, -5400). The statement says "psi(origin) = O", which is literally true, so this is wording only.

Replacement text: *"... the maps below are mutually inverse isomorphisms over Q between C_{27/2} and the
elliptic curve E. ψ is a morphism everywhere and sends the origin of E to O = (1:-1:0). φ is given by the
formula where Z ≠ 0 and extends to the three points with Z = 0 by φ(O) = origin, φ(1:0:0) = (216,5400),
φ(0:1:0) = (216,-5400)."*

## DE.1: rank 0 by 2-isogeny descent (grade NONE)

**Input (Cremona ch. III, section 3.6, "Method 1: descent using 2-isogeny", p. 84).** For E: y^2 = x(x^2 + cx + d)
with c, d in Z, the text gives "E′ : y2 = x(x2 + c′x + d′) where c′ = −2c and d′ = c2 −4d. The nonsingularity
condition on E is equivalent to dd′ ̸= 0." For each factorization d = d1 d2 with d1 squarefree, it considers
H(d1, c, d2): v^2 = d1 u^4 + c u^2 + d2. It defines n1 as "the number of factorizations of d for which the quartic
H(d1, c, d2) has a rational point" and n2 as the number "for which the quartic has a point everywhere locally".
Then E(Q)/φ′(E′(Q)) "is isomorphic to the subgroup of Q∗/(Q∗)2 generated by the factors d1 for which
H(d1, c, d2) has a rational point", with |E(Q)/φ′(E′(Q))| = n1 = 2^{e1} and similarly n1' = 2^{e1'}, and

> (3.6.2) rank(E(Q)) = rank(E′(Q)) = e1 + e′1 −2.

**Hypotheses.** There is a rational 2-torsion point at (0,0), the coefficients are integral, and d d' != 0. All
hold here: c = 393, d = 3456, c' = -786, d' = 140625 = 375^2.

**Proof of (3.6.2), as given on p. 86.** The n1 n1' points obtained cover E(Q)/2E(Q) "either once each, when
|E(Q)[2]| = 4, which is when d′ is a square, or twice ... hence 2r = n1n′1/4 in both cases". I re-derived this:
here d' is a square, |E(Q)[2]| = 4 and |E(Q)/2E(Q)| = 2^{r+2} = n1 n1'.

**Selmer side (p. 85).** There are exact sequences 0 → E(Q)/φ′(E′(Q)) → S(φ′)(E′/Q) → X(E′/Q)[φ′] → 0 and the
analogue for φ. The text gives "|X(E′/Q)[φ′]| = n2/n1" and "|X(E/Q)[φ]| = n′2/n′1". Local solubility "is
automatic for all primes p which do not divide 2dd′" (p. 85).

**Real place (p. 86).** "if d′ < 0 then we require d1 > 0, while if d′ > 0 then either d1 > 0 or c + √d′ > 0 is
necessary."

**Note for the brief.** The relevant primes are p | 2dd', not only p | 2dd1. For E, the four classes ±2, ±3 are
soluble at 2, at 3 and over R. Their **only** obstruction is at p = 5, which divides d' = c^2 - 4d but not 2d.
A check restricted to p | 2dd1 would therefore wrongly put them in the Selmer group, giving n2 = 8 and a rank
bound of 1.

**My computation (check_b).** For each squarefree d1, I decide local solubility at 2, 3, 5 and R and search for
global points. A local "yes" means a primitive (M, e) in Z^2 with g(M, e) a nonzero p-adic square. A local "no"
means no primitive (M, e) mod p^k with g a square mod p^k. That is a valid certificate, because every Q_p point
rescales to a primitive Z_p point.

E (c = 393, d = 3456 = 2^7 3^3; d1 in {±1, ±2, ±3, ±6}):

| d1 | 2 | 3 | 5 | R | global point (N, M, e) | point on E |
|---|---|---|---|---|---|---|
| 1 | yes | yes | yes | yes | (1, 1, 0), at infinity | O |
| -1 | yes | yes | yes | yes | (0, 3, 1) | (-9, 0) |
| 6 | yes | yes | yes | yes | (24, 0, 1) | (0, 0) |
| -6 | yes | yes | yes | yes | (30, 2, 1) | (-24, -360) |
| 2, -2, 3, -3 | yes | yes | **no** (mod 5) | yes | none | |

Hand proof of the mod-5 obstruction. Since 5^6 | c^2 - 4d,
d1 g ≡ (d1 M^2 + (c/2) e^2)^2 (mod 5).
- If 5 ∤ N, then d1 is a square mod 5. But ±2 and ±3 are non-residues.
- If 5 | N, then M^2 ≡ -(c/(2 d1)) e^2 ≡ d1^{-1} e^2 (mod 5), which is a non-residue times e^2. This forces
  M ≡ e ≡ 0, contradicting primitivity.

So n1 = n2 = 4 and the group is {±1, ±6}. It is the image of the torsion: x mod squares, with (0,0) ↦ d ≡ 6.

E' (c' = -786, d' = 140625 = 3^2 5^6; d1 in {±1, ±3, ±5, ±15}):

| d1 | obstruction |
|---|---|
| 1 | global point (375, 0, 1) = (0,0) of E' |
| -1, -3, -5, -15 | R: d1 < 0, c' < 0, d2 < 0, so the right side is negative definite. This matches Cremona's criterion, since c' + √(c'^2 - 4d') = -786 + √55296 < 0 |
| 3 | 2 (mod 2^4) and 3 (mod 3^2) |
| 5 | 2 (mod 2^7) and 3 (mod 3^3) |
| 15 | 2 (mod 2^4) and 3 (mod 3^3) |

Hand proof for d1 = 3:
- N^2 = 3M^4 - 786 M^2 e^2 + 46875 e^4 ≡ 0 (mod 3), so 3 | N.
- Dividing by 3 gives 3 N1^2 = M^4 - 262 M^2 e^2 + 15625 e^4 ≡ M^4 - M^2 e^2 + e^4 (mod 3).
- The right side is 1 (mod 3) for every primitive (M, e). Contradiction.

So n1' = n2' = 1 and the group is {1}.

**Result.** rank = e1 + e1' - 2 = 2 + 0 - 2 = 0. Because n1 = n2 and n1' = n2', X(E)[φ] = X(E')[φ'] = 0: there is
no ambiguity, and the bound is unconditional.

**Independent route (check_b, second half): full 2-descent.** The Kummer map is
κ(P) = (x - 0, x + 9) mod squares, with the usual values at the 2-torsion points. For p in {2, 3, 5, R}, explicit
points fill local images of the full sizes 8, 4, 4 and 2. The 2-Selmer group in ⟨-1, 2, 3, 5⟩^2 is
{(1,1), (6,1), (-1,-15), (-6,-15)}. This has order 4 and equals κ(E(Q)[2]), so 2^{r+2} <= 4, r = 0 and
X(E)[2] = 0. An analytic-rank computation was not done; it would not be a certificate in floating point anyway.

**On the wording "Selmer-type groups".** The groups {±1, ±6} and {1} are, in Cremona's notation, the images
E(Q)/φ′(E′(Q)) and E′(Q)/φ(E(Q)) in Q*/Q*^2. They equal the Selmer groups S^(φ′)(E′/Q) and S^(φ)(E/Q). The
statement is correct. If the paper prints it, I suggest: *"the images of E(Q) and E′(Q) in Q*/Q*², which equal
the Selmer groups S^{(φ′)}(E′/Q) and S^{(φ)}(E/Q) of Cremona §3.6, are {±1, ±6} and {1}"*.

## DE.2: torsion (grade NONE)

**Points and orders (check_c).** All eleven affine points lie on E. Their orders, computed by my own group law
(Cremona 3.1 conventions, a1 = a3 = 0), are:

| points | order |
|---|---|
| (0,0), (-9,0), (-384,0) | 2 |
| (16, ±400) | 3 |
| (-24, ±360), (-144, ±2160), (216, ±5400) | 6 |

**Group structure.** The twelve points are closed under addition (all 144 sums checked). Exactly three
elements have order 2, so the group is Z/2 x Z/6 and not Z/12. Explicitly it is ⟨(216, 5400)⟩ x ⟨(-9, 0)⟩.

**No further torsion.** The model has Delta = 2^18 3^8 5^6, so its bad primes are exactly 2, 3 and 5:
- at 5, v5(c4) = 0, so the reduction is multiplicative;
- at 3, v3(c4) = 2 < 4, so the model is minimal and the reduction additive;
- at 2, any minimal model still has v2(Delta) >= 6.

The input is Cremona section 3.3, p. 70: "for an odd prime p of good reduction (that is, p ∤ 2∆), the reduction
map from E(Q)tors to E(Z/pZ) is injective". It cites [58, VIII.7] and [28, V.1]. Counting gives
#E(F_7) = #E(F_11) = #E(F_13) = 12 and #E(F_17) = #E(F_19) = #E(F_23) = 24. So |E(Q)_tors| divides 12, and
the 12 listed points are all of it. The twelve points also stay distinct mod 7 and mod 11. The prime 7 alone
already suffices.

**Second proof.** Cremona's Prop. 3.3.1 and 3.3.2 (Lutz-Nagell) say torsion points are integral, with y = 0 or
y^2 | Delta0, and the text checks Delta = -16 Delta0 (p. 70). Enumerating every y with y^2 | Delta0 and solving
for integer x gives exactly the eleven listed affine points. All of them have finite order.

## DE.3: the twelve points of C_{27/2} (grade NONE)

All twelve points lie on F = 0 and are pairwise distinct. They coincide with psi(E(Q)) (see DE.0), so they are
all of C_{27/2}(Q).

**Points with a zero coordinate.** The line Z = 0 meets C where (X+Y)XY = 0, giving (1:0:0), (0:1:0) and
(1:-1:0), and similarly for X = 0 and Y = 0. So the points with a zero coordinate are exactly the six base
points, for every lambda.

**Positive points.** They are exactly the six permutations of (1:4:4) and (1:1:4).

**Independent check.** A search over all primitive integer points with |coords| <= 80 solves the quadratic in Z
exactly and finds exactly these twelve.

**Orders with base point O.** The base points have orders 6, 6, 2, 1, 3, 3 in the listed order, matching the
G5 correction. (1:4:4) has order 6 and (1:1:4) has order 2. The twelve points are the six base points together
with their translates by (1:4:4), as DE.5 says.

## DE.4: triads (grade MINOR)

**Definitions (DI.1, DI.5).** A triad (a, b, c) has S = a+b+c and R = 1/a + 1/b + 1/c, so lambda = S R. It is
hyperbolic when R < 1 and all entries are >= 2. A class is the set of (unordered) triples with a common S and a
common R.

**Derivation.** If S = 18k and R = 3/(4k), then lambda = 27/2. The triple is a positive rational point of
C_{27/2}, hence by DE.3 a positive multiple m of a permutation of (1,4,4) or of (1,1,4). The sum fixes the
multiple: 9m = 18k, or 6m = 18k. So the representatives are (2k, 8k, 8k) and (3k, 3k, 12k), and each is
unique. Both are hyperbolic for k >= 1: R = 3/(4k) < 1 and the smallest entry is 2k >= 2.

**Exact check (check_d).** For k = 1..30, 36, 42, 49 and 60, I enumerated **every** positive integer triple
with S = 18k. The ones with R = 3/(4k) are exactly these two, and the uniqueness of the representative is
asserted for k <= 49.

**Defect.** The statement needs k to be a positive integer. It is not enough that 18k is an integer:

| k | S | members |
|---|---|---|
| 3/2 | 27 | (3, 12, 12) only |
| 5/2 | 45 | (5, 20, 20) only |
| 2/3 | 12 | (2, 2, 8) only |
| 1/6, 7/6 | | none |

Relatedly, every pillow (j, 4j, 4j) with j odd is alone in its class; this is checked for j < 40.

Replacement text: *"Let k ≥ 1 be an integer. A triad with S₁ = 18k and R = 3/(4k) has Λ = 27/2 ... namely
(2k,8k,8k) and (3k,3k,12k), and both are hyperbolic since R = 3/(4k) < 1 and all entries are ≥ 2k ≥ 2."*

## DE.5: Theorem 5.16, isolation (grade MINOR)

**Is it supported by (a)-(d)?** Yes. The chain DE.0 (Q-isomorphism, with O ↦ origin) → DE.1 (rank 0) → DE.2
(torsion of order 12) → DE.3 (the twelve points) → DE.4 proves that, for every **positive integer** k, the class
with S = 18k and R = 3/(4k) is exactly {(2k,8k,8k), (3k,3k,12k)}.

**The meaning of "class".** It agrees with the definition used here: common S and R, unordered triples, as in
DI.1 and DI.5. Hyperbolicity is automatic for both members, so the claim holds whether or not the class is
restricted to hyperbolic triples.

**Defects, all wording:**

1. **"for every k" → "for every integer k ≥ 1".** For half-integers k the "class" (3k, 12k, 12k) has one member
   (DE.4).
2. **The certificate.** The text rests "rank 0 unconditionally" on PARI `ellrank` and on a quoted manual
   sentence I could not check (instrument gap). The 2-isogeny descent above is short, exact and citable
   (Cremona (3.6.2), with n1 = n2 = 4 and n1' = n2' = 1). I recommend making it the proof and demoting PARI to a
   cross-check. Torsion likewise: reduction mod 7, using Cremona p. 70.
3. **"(as far as tested) a torsion phenomenon".** This is provable. O, (0:1:-1) and (1:0:-1) are flexes of every
   smooth C_λ: the tangent at each meets C with multiplicity 3, checked symbolically in λ (check_e). They lie on
   the line X+Y+Z = 0. Hence T = (1:0:-1) has order 3.

   The transposition σ: Y ↔ Z is an involutive automorphism of C_λ. Write it as σ(Q) = αQ + σ(O). It has fixed
   points such as (0:1:-1). A translation by σ(O) = T ≠ O has none, so α ≠ 1. Since σ² = 1, α² = 1, so α = -1
   and σ(Q) = -Q + T. This is checked exactly on 28 points of 7 curves.

   An isosceles point (u:v:v) is fixed by σ, so 2Q = T and Q has order 3 or 6. A positive point has order
   exactly 6, since order 3 would give Q = -T = (0:1:-1). All 1,482 triples (u, v, v) with u ≠ v ≤ 39 have
   order 6 and satisfy 2Q = (1:0:-1) (check_e, exact). So the census claim is correct, and the hedge can go.

Replacement text for the theorem:
*"C_{27/2} is isomorphic over Q to E: y² = x(x+9)(x+384), which has rank 0 (2-isogeny descent: the images of
E(Q) and E′(Q) in Q*/Q*² are {±1, ±6} and {1}, so rank = 2+0−2 = 0 by Cremona (3.6.2); the Selmer groups
equal the images, so the result is unconditional) and torsion Z/2 × Z/6 (reduction mod 7). Hence
C_{27/2}(Q) consists of the six base points and their translates by the order-6 point (1:4:4), and its positive
points are the permutations of (1:4:4) and (1:1:4). Hence, for every integer k ≥ 1, the class of
{(2k,8k,8k),(3k,3k,12k)} has exactly two members ... Every isosceles point (u:v:v) of every C_λ satisfies
2(u:v:v) = (1:0:−1), so it has order 6: the isosceles family, including the base pair, is a torsion
phenomenon, and the unbounded fibres come only from curves of positive rank."*

PARI `ellrank`/`elltors` can be kept as a cross-check sentence. The last clause, "unbounded fibres come only
from curves of positive rank", is a formal consequence: a rank-0 curve has finitely many points.

## DE.6: 3P on C_{155/12} (grade NONE)

**Setup.** The curve is 12(X+Y+Z)(XY+YZ+ZX) = 155XYZ. It is nonsingular: Groebner basis of the partials, as in
(a). P = (4:9:18) lies on it: S = 31, e2 = 270, e3 = 648, and 31·270 = 8370 = (155/12)·648.

**Law used (descent_lib).** Let A*B be the third intersection of line AB with C (the tangent line if A = B),
computed exactly by restricting F to the line and dividing out the known roots. Then A + B = O*(A*B) and
-A = A*(O*O).

**O is a flex, contrary to the caution in the brief.** The tangent at O is -X - Y + (λ-1)Z = 0, and F restricted
to it is λ s³/(λ-1)², with s = X+Y. So O*O = O and -A = A*O. The same holds for (0:1:-1) and (1:0:-1). The other
three base points are not flexes.

**Checks.**
- Associativity holds on all 343 triples drawn from 7 rational points, and A + (-A) = O on the sample.
- 2P = (16352 : 288 : -365), as printed.
- 3P = P + 2P = 2P + P = **(162833463 : 723926268 : 287876366)**, the corrected claim. The old printing
  (162833463 : 287876366 : 723926268) is not 3P.
- Independent check: transported to the BGN Weierstrass model of DI.2,
  τ² = s(s² + (12433/144)s + 620/3), P maps to (-10/3, 275/18). A separate Weierstrass group law gives 2P and 3P,
  which map back to the same points.
- gcd(162833463, 723926268, 287876366) = 1, so the representative is the unique primitive integer one, up to
  sign.

**Relation between the two printings.** 3P + (old) = (1:0:-1), so old = -3P + (1:0:-1) = σ(3P). Both have the
same unordered triad {162833463, 287876366, 723926268}, with S = 1174636097 and S·R = 155/12. So DI.6's
unordered statement "3P = (162833463, 287876366, 723926268)" is correct as a **triad**, but wrong as a point of
C with base O. The correction is right.

**Role of the base point.** With base (0:0:1), which has order 2, [3]P is the same point, since
[3]_{O''}P = 3P - 2O''. With the other four base points one obtains cyclic rotations of the corrected
coordinates. No base point produces the old printing, so the old printing is a transposition slip, not a
base-point convention.

Optional wording: *"3P = (162833463 : 723926268 : 287876366); as an unordered triad,
{162833463, 287876366, 723926268}."*

## Files

- `descent_lib.py`: the Weierstrass group law, #E(F_p), and the plane-cubic chord-tangent law with an
  arbitrary base point.
- `check_a_isomorphism.py` / `.txt`: DE.0 (97 asserts).
- `check_b_descent.py` / `.txt`: DE.1, the 2-isogeny descent on E and E', and the full 2-Selmer group
  (31 asserts).
- `check_c_torsion.py` / `.txt`: DE.2 (35 asserts).
- `check_d_points_triads.py` / `.txt`: DE.3 and DE.4 (191 asserts).
- `check_e_isolation.py` / `.txt`: the DE.5 side claims (flexes, σ relation, isosceles census; 17 asserts).
- `check_f_3P.py` / `.txt`: DE.6 (30 asserts).
- `fetches.md`.
