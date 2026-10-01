# G5 referee report: diophantine group (DI.1 to DI.11)

Scope: statements DI.1–DI.11 in `review/audit/statements/diophantine.md` (and PC.* for context),
re-derived from the statements alone. Sources read: BGN (Math. Comp. 61, 1993), Schinzel
(Serdica 22, 1996), the PARI/GP manual (elliptic curves; general number fields), and the
PARI 2.17.2 source file `ellrank.c` (see `fetches.md`). No manuscript proof, code or data
was opened before Sections 1–3 below were written.

Every check is exact (integers, `Fraction`, sympy) and exits nonzero on failure. Run from the repository root:

| script | interpreter | output |
|---|---|---|
| `check_algebra.py` | `/opt/homebrew/Caskroom/miniforge/base/bin/python3` | `check_algebra.txt` |
| `check_groups.py` | same | `check_groups.txt` |
| `check_enum.py` (needs `enum_classes.c`; it compiles the program and runs it itself if `enum_4800.txt` is missing, which takes about 10 min) | same | `check_enum.txt`, `enum_4800.txt` |
| `check_isosceles.py` | same | `check_isosceles.txt` |
| `check_theorem5.py` | same | `check_theorem5.txt` |
| `check_descent.py` | `review/audit/.venv-pari/bin/python` | `check_descent.txt` |
| `check_ranks.py` | `review/audit/.venv-pari/bin/python` (PARI 2.17.2, version asserted) | `check_ranks.txt` |

## Summary table

| item | content | grade | one-line reason |
|---|---|---|---|
| DI.1 | Proposition 1 | MINOR | True. Two wording issues: "primitive sums" should say "primitive triples t_i with sums s_i", and the rescaled t_i *lie in* a class that may contain other points of C_λ. "Entries ≥ 2" follows from R < 1. |
| DI.2 | pencil, Weierstrass model, fibres, generic MW | MINOR | Everything re-derived and correct, including the stated maps to BGN's model. The list "(1:0:0),…,(1:0:−1) are of orders 1,2,3,3,6,6" is wrong if read in order; the true orders are 6,6,2,1,3,3. |
| DI.3 | reciprocation = +T₂; dual family | MINOR | The identities are proved, and 1753/423/1330 is reproduced. "12-point orbit" holds only for non-torsion P. "Any other pair differs by a point of infinite order" is true but given no proof; a short proof exists (see below). |
| DI.4 | Proposition 2 | MINOR | The literal statement is false for rank-1 (scaling) families, e.g. t = ℓ(u,v)(2,8,8), t′ = ℓ(u,v)(3,3,12). It is true once the entries of t are not all proportional. The affine case is fully correct. |
| DI.5 | Theorem 3 (large fibres) | NONE | Proved. P=(4,9,18) on C_{155/12} has nP ≠ O for n ≤ 12, so by Mazur it has infinite order. 3P is as stated. Odd multiples are positive and even ones are not (checked up to 9P). |
| DI.6 | ranks 2,2,3,3 of fibre curves | NONE | PARI gives r1 = r2. My own 2-isogeny descent proves the same ranks unconditionally. Torsion Z/6. |
| DI.7 | isolation of the base pair (P5) | NONE (one MINOR remark) | rank C_{27/2} = 0 unconditionally (three independent ways), torsion Z/2×Z/6, 12 points as stated. The remark: "isosceles points are torsion (as far as tested)" can be upgraded to a theorem. |
| DI.8 | copies kD hyperbolic for k ≥ 4 | MINOR | True. The given justification covers only dual pairs, but R ≤ 3 holds for every positive triple, so the claim holds for every primitive D. |
| DI.9 | Theorem 4, S log S | NONE (MINOR presentation) | The identity, primitivity, g∈{1,3}, area log2/6 (u<v), c_iso, the error term, partial summation in both conventions and at most one isosceles pair per class are all verified. The o(1) converges slowly: the secondary term is about −0.48 X. |
| DI.10 | Theorem 5, S (log S)² | MINOR (provisional; constant NOT re-derived) | The statement does not define the conic-bundle family, so 3/(128π⁴) cannot be recomputed from it. The order X log²X is plausible and consistent with the data. Specific items are listed for phase 2. |
| DI.11 | first fibres; ranks proven | NONE | First sizes 3,4,5,6 occur at S = 136, 408, 1849, 4600 with exactly the listed members. No size 7 up to 4800. All five ranks are proven (PARI r1=r2, and unconditionally by my 2-isogeny descent). |

No FATAL or SERIOUS findings.

---

## DI.1 Proposition 1

**Independent proof.** Write λ(t) = e₁e₂/e₃ = S·R. For a common S, R = R′ ⇔ λ = λ′. Take
pairwise non-proportional primitive triples t_i with sums s_i and common λ, and let L = lcm s_i. The triples (L/s_i)t_i
have sum L and R = λ/L. They are distinct because they are non-proportional. gcd of all entries =
gcd_i (L/s_i)·gcd(t_i) = gcd_i(L/s_i) = 1, because for each prime p some s_i attains v_p(L). Any
integer triple proportional to t_i is c·t_i with c ∈ Z, since t_i is primitive. So a common sum S forces
s_i | S for all i, hence L | S. With S = mL the triples are m(L/s_i)t_i, the scaled copies.
R = λ/(mL) < 1 ⇔ mL > λ. If R < 1 then every entry is > 1, because 1/p ≤ R. So "entries ≥ 2"
is automatic.

**Counterexample search.** This is implicit in the enumeration (check_enum): every class found up to S=4800 is consistent.

**Grade: MINOR.** **Fix:** (i) say "primitive triples t_i with sums s_i". (ii) Replace "form a
degeneracy class" with "lie in one degeneracy class (which contains, in addition, every other
positive point of C_λ whose primitive sum divides L)". The S=408 class is an example: it is 3×(S=136 class) plus (65,70,273).
(iii) Note that entries ≥ 2 follows from R < 1.

## DI.2 Pencil, Weierstrass model, fibres, torsion

**Independent derivation (check_algebra.py).**
- (x+y)(y+z)(z+x) = e₁e₂ − e₃, so C_λ is the member t = 1−λ.
- *Own model.* In the chart z=1 the curve is quadratic in x: (y+1)x² + (y²+(3−λ)y+1)x + y(y+1) = 0.
  The discriminant gives v² = Q(y) = y⁴ + (2−2λ)y³ + (λ²−6λ+3)y² + (2−2λ)y + 1, which is monic, so the
  classical quartic→cubic reduction applies (v = y² + (a/2)y + t). Shifting the rational 2-torsion abscissa to 0 gives
  **E_λ : W² = s(s² + (λ²−6λ−3)s + 16λ)**, with forward map s = −4e₂/z² and
  W = −4(2xy² + 2y²z + 3xyz − λxyz + xz² − λxz² + yz² + λyz²)/z³. The base point is
  **O = (1:−1:0) ↦ ∞**: on z=0 the curve meets (1:0:0), (0:1:0), (1:−1:0), and e₂ ≠ 0 only at the last.
  The forward and inverse maps, and both compositions, are verified symbolically. This turns out to be BGN's
  (6) with n = λ. The manuscript's own model x³+(λ−3)²x²+… has the same (c₄,c₆), so it is E_λ
  translated by s = x+4. The manuscript's stated forward and inverse maps to BGN are also verified; they differ
  from mine by the sign of the ordinate.
- Δ = 2¹²λ²(λ−9)(λ−1)³. c₄ ≠ 0 at λ = 0, 1, 9, so the fibres there are I₂, I₃, I₁. At ∞: deg a₂ = 2, deg a₄ = 1,
  so the model is regular at ∞, ord_∞Δ = 12−6 = 6 and ord_∞c₄ = 0, giving **I₆**. The Euler numbers sum to 12, and
  Shioda–Tate gives rank 8 − (1+2+0+5) = 0 over Q̄(λ). λ ≥ 9 holds for positive points (AM–HM).
- *Torsion sections* (check_groups.py, exact chord–tangent law on the plane cubic, base O, at six
  values of λ): orders are **(1:0:0):6, (0:1:0):6, (0:0:1):2, (1:−1:0):1, (0:1:−1):3, (1:0:−1):3**.
  These six points form a cyclic group of order 6.
- *Egg.* On x=0 the curve meets only (0:1:0), (0:0:1), (0:1:−1), and λ → ∞ at the vertices of
  the positive triangle. So the positive real points form a closed component disjoint from the coordinate lines. It is
  not the component of O. BGN p. 119 states, verbatim, "If P is on the egg, then just the odd multiples of
  P give positive solutions"; this is reproduced in check_groups for P = (4,9,18) up to 9P.

**Grade: MINOR.** **Fix:** write the orders as a correspondence: "(1:−1:0)=O, (0:0:1) of order 2,
(0:1:−1),(1:0:−1) of order 3, (1:0:0),(0:1:0) of order 6". Optionally note that the own model is BGN's (6) translated.
Beauville and Shioda were not fetched (fetches.md), but nothing graded depends on them.

## DI.3 Reciprocation and the dual family

**Independent proof.** The line through P = (p₀:p₁:p₂) and T₂ = (0:0:1) consists of the points (p₀:p₁:w). F is
quadratic in w with root product p₀p₁, so the third point is (p₀p₂:p₁p₂:p₀p₁). Next, O, that point and
(p₁p₂:p₀p₂:p₀p₁) are collinear, and F(p₁p₂,p₀p₂,p₀p₁) = p₀p₁p₂·F(p). Hence P+T₂ = O∗(P∗T₂) = ι(P)
for every P. Because ι is an involution, 2T₂ = O. This is checked symbolically and on points of C_{155/12}.
Dual family: sums e₁e₂, reciprocal sums 1/e₃ (symbolic). Self-duality happens only for geometric progressions: for sorted a ≤ b ≤ c,
(ab, ac, bc) ∝ (a, b, c) ⇔ b² = ac.

Orbit: transposition y↔z acts as P ↦ (1:0:−1) − P, and cyclic permutations act as translations by the order-3 sections. So
the S₃ × ⟨ι⟩ orbit is {±P + T : T ∈ Z/6}, verified to have 12 elements for non-torsion P.

**Counterexample search.** check_enum: primitive pairs with S ≤ 600: **1753, of which 423 are dual and 1330 are not**,
exactly as claimed. None of the 1330 has P′−P or P′+P of order ≤ 12. check_groups: among the 40,305
primitive positive triples with sum ≤ 120, every torsion point is **isosceles (order 2 or 6
depending on ordering) or a geometric progression (order 12)**.

**Grade: MINOR.** "Any other pair on the same curve differs by a point of infinite order" is true, but the
argument needs extra torsion to be excluded. Curves with an isosceles point have torsion Z/2×Z/6, and
GP curves have Z/12. **Fix:** add the following lemma. A positive torsion point is fixed by a
transposition, so it is isosceles (2P ∈ ⟨T₃⟩), or it is self-dual up to permutation, i.e. a GP. In both cases its full
torsion coset consists of permutations of itself and its dual. Also restrict "12 points" to non-torsion P.

## DI.4 Proposition 2

**Independent proof.** Write t = (c₁ℓ₁, …), t′ = (d₁ℓ′₁, …) with every entry positive on the cone.
Group the entries into proportionality classes [ℓ]. The functions 1/ℓ for distinct classes have distinct poles, so ΣR equal
gives Σ_{class} 1/c = Σ_{class} 1/d for each class. Positivity then forces every class to occur in both triples.
(a) Three classes: one entry each, so c = d, a permutation. (b) Two classes: the forms are linearly independent, so the sum identity holds
classwise. A (2,2) split forces equal multisets. A (2,1) split forces c₁+c₂ = d and 1/c₁+1/c₂ = 1/d, i.e.
c₁²+c₁c₂+c₂² = 0, which is impossible (check_algebra). (c) **One class: t = ℓ·(c₁,c₂,c₃), t′ = ℓ·(d₁,d₂,d₃)
with (c),(d) any degeneracy, e.g. ℓ(u,v)·(2,8,8) and ℓ(u,v)·(3,3,12). This satisfies every
hypothesis as written and t′ is not a permutation of t.** For an affine family on a line not through the
origin, case (c) cannot occur, so that half is correct. So is "non-scaling polynomial families have degree ≥ 2".

**Grade: MINOR** (the counterexample is just a scaling family; the intended statement is clear). **Fix:** add "and the
entries of t are not all proportional (equivalently (u,v) ↦ t has rank 2)".

## DI.5 Theorem 3

**Independent proof.** λ(4,9,18) = 31·270/648 = 155/12. Exact chord–tangent arithmetic gives
nP ≠ O for 1 ≤ n ≤ 12. Mazur's list allows only orders 1–10 and 12 for rational torsion, so P has infinite order. (PARI
independently gives rank 2 and torsion Z/6.) 3P = (162833463, 723926268, 287876366) as a set matches the claim.
P is positive, so it lies on the egg, and the odd multiples (2j+1)P are pairwise distinct positive points. Each
unordered triple accounts for at most 6 points, so there are infinitely many distinct triples. Take any k of them. Proposition 1 puts
them in one primitive class at L = lcm of their primitive sums, and that class is hyperbolic once L > 155/12. Because only finitely many
triples have primitive sum ≤ B, the values of L are unbounded, which gives infinitely many distinct primitive classes of size ≥ k.

**Grade: NONE.**

## DI.6 / DI.11 Ranks and first fibres

**Counterexample search (check_enum.py, C enumerator `enum_classes.c`).** All 3,067,197,199 hyperbolic
triples with 10 ≤ S ≤ 4800 were enumerated and grouped by exact R. Grouping uses the correctly rounded double
plus 128-bit cross-multiplication. The enumerator agrees class by class with an independent pure-Python
Fraction enumeration for S ≤ 300. Results:
- the first class of size 3 occurs at S=136 (λ=68/5), size 4 at **S=408**, size 5 at S=1849 and size 6 at S=4600. Members are exactly as listed.
  The S=408 class lies on λ = 68/5 and equals 3×(S=136 class) ∪ {(65,70,273)}.
- **no class of size ≥ 7 up to 4800.** Size histogram: {2: 96981, 3: 1627, 4: 122, 5: 11, 6: 1}.
- PC.19 table N(S) at 18…600 = 1, 92, 386, 840, 1496, 2210, 3067: **reproduced exactly**. The PC.18 classes at S=36 are confirmed.

**Ranks (check_ranks.py and check_descent.py).** Each curve uses the integral own model [0, p²−6pq−3q², 0, 16pq³, 0], λ = p/q:

| curve | PARI `ellrank` | torsion | own 2-isogeny descent |Sel^φ|, |Sel^φ′| | images of found points | rank |
|---|---|---|---|---|---|
| C_{68/5} (S=136, 408) | [2,2,0] | Z/6 | 4, 4 | fill both | **2 proven** |
| C_{1849/120} (S=1849) | [3,3,0] | Z/6 | 8, 4 | fill both | **3 proven** |
| C_{230/21} (S=4600) | [3,3,0] | Z/6 | 16, 2 | fill both | **3 proven** |
| C_{155/12} (Thm 3) | [2,2,0] | Z/6 | 8, 2 | fill both | **2 proven** |

The listed fibre points have height-matrix rank 2, 3, 3 (numerically: eigenvalues ≥ 0.98 versus ≤ 10⁻¹⁸).

**Grade: NONE** for both DI.6 and DI.11.

## DI.7 Isolation: see the "P5 verdict" section below.

The proof that rank 0 plus the torsion list implies "exactly two members for every k":
any member of the class at (S, R) = (18k, 3/(4k)) has λ = SR = 27/2, so it is a positive rational point of
C_{27/2}. C_{27/2} is a smooth genus-1 curve with the rational point O, hence isomorphic to E_{27/2} by the
verified birational map, so C_{27/2}(Q) is the 12-element torsion group. Exactly 6 of those points are positive: the
permutations of (1,4,4) and (1,1,4). Up to order these are two projective points. Each has exactly one
integer representative with sum 18k: 2k(1,4,4) and 3k(1,1,4). R = 3/(4k) < 1, so both are hyperbolic. ∎

The secondary claim "every isosceles triple tested is torsion" can be upgraded to a theorem: (u:v:v) is a fixed point of y↔z, i.e.
of P ↦ (1:0:−1) − P, so 2P = (1:0:−1), which has order 3. Hence P has order 6 (verified for 358 coprime pairs u,v ≤ 24).
Every isosceles curve therefore has torsion exactly Z/2×Z/6. The count "1,482" = 39·38 is consistent.

**Grade: NONE.** **Optional fix:** replace "(as far as tested)" with the two-line proof.

## DI.8 Copies kD hyperbolic for k ≥ 4

**Independent proof.** Every positive integer triple has R ≤ 3, so R_{kD} ≤ 3/k < 1 for k ≥ 4, and the entries are ≥ k ≥ 2.
For the dual pair, G | e₂·gcd(a,b,c) = e₂ as stated. (k,D) ↦ kD is injective because gcd(kD) = k.
So (*) holds. It is checked numerically against N(X) in check_theorem5: N(4800) = 102719 ≥ 31177 = RHS over
all primitive pairs.

**Grade: MINOR** (the argument is narrower than the claim). **Fix:** "for any primitive pair D, R_D ≤ 3 since entries ≥ 1".

## DI.9 Theorem 4

**Independent proof.**
- D_{u,v} is the dual pair of t = (u,v,v). Both triples have sum (2u+v)(u+2v) and R = 1/(uv), and λ = (2u+v)(u+2v)/(uv) (symbolic).
- g | 3u and g | 3v, so g | 3. Also g = 3 ⇔ u ≡ v ≢ 0 (mod 3).
- Primitivity: gcd = gcd((2u+v)/g, (u+2v)/g)·gcd(u,v) = 1.
- The two triples are distinct for u ≠ v. D_{1,4} = {(2,8,8),(3,3,12)}.
- *Count.* The region {0<u<v, (2u+v)(u+2v) ≤ Y} has area **Y·log2/6**. The full quadrant has area Y·log2/3, so if the
  proof's "Y log2/3" refers to u<v it is off by a factor 2, but the stated constant is right. Coprime density is
  6/π². Among coprime pairs, g = 3 on 2 of the 8 admissible residue pairs mod 3, with threshold 3y. So
  A(y) = (6/π²)(log2/6)(3/4 + (1/4)·3) y = **(3 log2/(2π²)) y** = 0.105346 y.
- The region is bounded: v ≤ √(3y/2). Möbius inversion with the boundary error O(√y/d) per d ≤ √y gives O(√y log y).
- *Partial summation.* Σ_{S_D ≤ X/4}(⌊X/S_D⌋ − 3) = X∫dA(y)/y + O(X) = c_iso X log X + O(X).
- *Classes versus pairs.* The isosceles points on C_λ are the roots r, 1/r of 2r²+(5−λ)r+2 = 0, so a curve, and therefore a
  class, carries at most one isosceles pair. Distinct D_{u,v} have distinct λ, and distinct k give distinct S. So the kD_{u,v}
  (k ≥ 4) lie in pairwise distinct classes, and N ≥ N_cl ≥ (c_iso+o(1)) X log X.

**Numerics (check_isosceles.py, check_enum.py).** A(4800) = **506** as claimed (c_iso·4800 = 505.66). All
2917 hyperbolic copies kD_{u,v} with kS ≤ 4800 are found by the enumeration. No class contains two
isosceles pairs. |A(y) − c_iso y|/(√y log y) ≤ 0.002 for y up to 4·10⁷. However, L(X)/(X log X) = 0.053, 0.064,
0.071, 0.076, 0.078 for X = 10⁴…4·10⁷: the secondary term is about −0.479 X, constant over that range.

**Grade: NONE.** **Optional presentation fix:** state L(X) = c_iso X log X + O(X) explicitly. With the constant
c′ ≈ −0.48, any numerical comparison at feasible X shows only about 70% of the leading term.

## DI.10 Theorem 5

The statement gives only N(X) ≥ (3/(128π⁴)+o(1)) X(log X)². The conic-bundle family, the
"multiplicity 6", U, V and M = y^{1/8} are proof-internal and absent from the statement file. Under the
rules of this audit **the constant could not be recomputed**. What I can say independently:
- The order X(log X)² is natural. The dual family is parametrised by t ∈ P², with pair height
  S = e₁e₂/G, where G ⊇ gcd(e₁,e₂). The pencil ⟨e₁², e₂⟩ consists of the conics n·e₂ = m·e₁² (fibres
  {e₂/e₁² = const}), which is a conic bundle over P¹. Its base points (e₁ = e₂ = 0, i.e. a²+ab+b² = 0) are a
  conjugate pair, so the Picard rank of the relevant model is 2. Counting with Manin-type heuristics, or by summing the lattice counts
  y·Σ_δ ρ(δ)/δ over δ = gcd(e₁,e₂), gives A_dual(y) ≍ y log y, and partial summation then gives ≍ X log²X with half the
  constant. If the manuscript truncates δ (or a fibre parameter) at M = y^{1/8}, a factor 1/8 enters naturally.
  3/(128π⁴) = (1/2)·(1/8)·(1/6)·(36/π⁴)·(1/16) has the shape "partial summation × truncation ×
  multiplicity × two coprimality densities × area", which is consistent with this reading.
- Data (check_theorem5.py): the hyperbolic primitive dual pairs number 7626 at S ≤ 4800, and
  A_dual/(X log X) rises from 0.110 to 0.187 over 600…4800, so it is not decaying. N(X) exceeds the claimed bound by a
  factor of more than 1000 throughout. No counterexample is possible at this scale, and none was expected.
- **Items for phase 2:** (1) the multiplicity. An ordered t and its 5 permutations give the same D, but so do
  the 6 permutations of the dual t*. If t and t* lie in the counted region (on different conics e₂/e₁² = κ and
  e₁e₃/e₂² = κ′), the multiplicity is 12, not 6, unless the region excludes one of them. (2) The area constant
  and the 1/8 from M = y^{1/8}, given that the δ-sum must be uniform in the cusp of {e₁e₂ ≤ T} near the axes. (3) The
  coprimality densities: whether both pairs (u,v) and (U,V) are independently coprime with density 6/π² each, or
  whether there are local corrections at 2 and 3 (g ∈ {1,3} appeared in Theorem 4).

**Grade: MINOR (provisional).** No defect found, but the constant is unverified. **Fix:** make the
statement self-contained by defining the family in a lemma, so that a reader can check the count without the proof.

---

## P5 verdict (DI.7: isolation of the base pair)

1. **Model.** My own model is E_{27/2}: W² = s(s² + (393/4)s + 216). Scaling s = X/4, W = Y/8 gives **[0,393,0,3456,0]**,
   identical to the manuscript's integral model. Y² = X(X+9)(X+384), so there is full rational 2-torsion. The conductor is 90.
2. **Rank 0, proven three independent ways:**
   - *PARI 2.17.2* (version asserted [2,17,2]): `ellrank` = [0,0,0,[]].
   - *Own 2-isogeny descent* (check_descent.py, exact). E′ = [0,−786,0,140625,0]. Sel^φ(E) = {±1, ±6},
     which is exactly the image of the 2-torsion ((0,0)↦6, (−9,0)↦−1, (−384,0)↦−6). Sel^φ′(E′) = {1}: every
     other d ∈ {−1, ±3, ±5, ±15} is locally insoluble. So 2^r = 4·1/4 and **r = 0, unconditionally**. This uses only
     integer arithmetic and a Hensel-type p-adic solubility test. The same routine reproduces textbook
     y² = x³−x, and its Selmer sets are closed under multiplication for all five curves.
   - *Analytic*: `ellanalyticrank` = [0, 1.3376]. With modularity and Kolyvagin this independently gives rank 0,
     modulo the reliability of the numerical L-value.
3. **What ellrank's bounds guarantee.** The manual: the output [r1,r2,s,L] satisfies r1 ≤ rank ≤ r2.
   r1 is the rank of the points found. r2 = C − T − s, where C is the 2-Selmer rank, T the rank of E(Q)[2], and s the rank of
   Ш[2]/2Ш[4] detected by the Cassels pairing. The manual says these "are computed unconditionally". r1 = r2 proves the rank.
   r1 < r2 always happens when Ш has 4-torsion. **GRH:** the manual's `bnfinit` entry states that bnf data are
   GRH-conditional unless certified. In `ellrank.c` (2.17.2, `makevbnf`, line 1348), however, `Buchall` (the
   GRH-conditional class-group routine) is called only for irreducible factors of degree ≥ 3 of the 2-division
   polynomial. Rational factors go through `bnfselmerQ`, and quadratic factors go through `nf2selmer_quad`, which is built from
   Hilbert symbols (`hilbertii`). **For all five curves here the 2-division cubic has a rational root, so PARI's
   r2 involves no GRH and no other unproved hypothesis.** For C_{27/2} the cubic splits completely. The manuscript's word
   "unconditionally" is correct for these curves. It would not automatically be correct for a curve with no rational 2-torsion,
   but no such curve occurs here.
4. **Torsion.** `elltors` = [12, [6,2], [[−24,360],[0,0]]], i.e. Z/2×Z/6. Independently, the exact plane-cubic group law closes the six base points and
   (1:4:4) into a group of 12 points with order histogram {1:1, 2:3, 3:2, 6:6}. (1:4:4) has order 6.
5. **The 12 points** of C_{27/2}(Q): (1:−1:0)=O, (0:0:1), (0:1:−1), (1:0:−1), (1:0:0), (0:1:0) and
   the six permutations of (1,4,4) and (1,1,4). They map bijectively onto PARI's 12 torsion points of [0,393,0,3456,0]
   (the z=0 points are handled through the group law), and the two group laws agree on test sums. **The positive ones are exactly the
   permutations of (1,4,4) and (1,1,4).** This set is also the six base points together with their translates by (1:4:4), as claimed.
6. **Consequence.** For every k the class of {(2k,8k,8k),(3k,3k,12k)} has exactly two members (proof in DI.7 above).
7. **Pinned-script reproduction:** see the next section.

**P5: CONFIRMED. rank C_{27/2} = 0 unconditionally; torsion Z/2×Z/6; 12 points as stated; isolation holds for every k.**

## Pinned-script reproduction (step 4)

This section was written after Sections 1–3 were complete. `theory/diophantine/ranks.py` (sha256 4e08fdb1…2b50a) was
copied to `pinned/ranks.py` and run as `review/audit/.venv-pari/bin/python -B review/audit/diophantine/pinned/ranks.py`.
**One change was made to the copy:** it imports a helper `cubic_group.py` from its own directory. That helper was not copied
or read. Instead the copy appends `theory/diophantine/` to `sys.path` (marked "AUDIT CHANGE" in the file; `diff` shows
3 added lines). Output paths are unchanged relative to the script, so its output is `pinned/data/ranks.txt` and its
stdout is `pinned/run_stdout.txt`. A first run without `-B` left a `__pycache__` under `theory/diophantine/`; I deleted it
and reran with `-B`. Nothing under `theory/` is modified (`git status --ignored theory/` is clean).

Result (exit 0, cypari2 2.2.4 / PARI 2.17.2):
- C_{27/2}: model [0,393,0,3456,0], `ellrank` = [0,0,0,[]], `elltors` = [12,[6,2],[[−24,360],[0,0]]]. **This agrees
  exactly with my own run.**
- The script asserts that the 12 points are the six base points plus their translates by (1,4,4), and that the positive ones are, up to order,
  (1,1,4) and (1,4,4). **This agrees with my independent list** (check_groups.txt, check_ranks.txt).
- C_{155/12}, C_{68/5}, C_{1849/120}, C_{230/21}: [2,2,0], [2,2,0], [3,3,0], [3,3,0], torsion Z/6, root numbers
  +1, +1, −1, −1. **This agrees with check_ranks.txt and with my 2-isogeny descent.**
- Minor remark on the pinned script: it certifies "PROVEN" from r1 = r2 alone. Its docstring cites the manual's
  "unconditionally". As shown in the P5 verdict, that is correct here because every curve has a rational 2-torsion point
  (no `Buchall`/GRH path in `ellrank.c`). The docstring could say so, since the same script on a curve without rational 2-torsion
  would rely on GRH through `bnfinit`.
