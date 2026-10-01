# Comparison of the blind review with the existing proofs (group AUDIBILITY)

Read (read-only): `theory/audibility/proof.md`, `STATUS.md`, `attack-log.md`. The grades in `REVIEW.md` are
unchanged; changes are recorded only in the addendum (§C). New exact checks for this phase:
`check_phase2.py` → `check_phase2.txt` (exit 0), with helper `n5_pairs.c` (a copy of `n5_search.c` that also
counts pairs).

## A. Item by item

### AU.0 heat input
(a) The existing text does not re-derive the input. It imports it from an internal note plus Uçar
(4.25)+(4.33) and Schueth (STATUS: "not re-derived here"). My review derives it for all l from (4.25), (4.33),
Thm 4.20(i),(ii) and (4.35), and cross-checks against DGGW Prop 5.5 and Schueth Thm 4.1.
(b) No mathematical discrepancy: my p_0..p_3 are even and vanish at 1, as the text says. Two differences of
substance. (i) The proof's §6 lists the heat input as "depends on the cited heat input … not re-derived here";
the derivation in REVIEW.md §AU.0 can close that gap and should be adopted. (ii) The text cites (4.25)+(4.33)
but not Thm 4.20(ii) or (4.35), which are what make (4.33) the per-cone-point term and the smooth terms
multiples of the area.

### AU.1 Theorem A
(a) **Same core, different finish.** Both proofs reduce to "Q(z) = ∏_{x∈X}(z−x), X = m ⊎ (−m'), is even". The
existing proof gets there through Lemma 1 (odd power sums of X vanish ⇒ odd e_j(X) vanish) plus
e_{2n−1}(X) = e_{2n}(X)(R − R'). Mine works with the generating function f(z)f'(−z) − f(−z)f'(z) = c·z^{2n−1}, which is
the same statement in reciprocal variables. The finish differs: the existing proof uses multiplicities, mine
uses gcd(f(z), f(−z)) = 1 ⇒ f | f'.
(b) **Multiplicity argument: correct.** For x ∈ A = supp m, the hypothesis gives −x ∉ A, so μ_m(−x) = 0 and
μ_X(−x) = μ_{m'}(x). Evenness of Q gives μ_m(x) + μ_{m'}(−x) = μ_{m'}(x) ≥ μ_m(x). Summing over A,
n ≤ ∑_A μ_{m'} ≤ n, so μ_{m'} = μ_m on A and m' has no mass off A. Every step checks, including the case
i = j (excluded by m_i ≠ 0) and the repeated-order case. The use of Lemma 1 over Q[x_1..x_{2n}] and its
specialisation to complex values is legitimate. No discrepancy.

### AU.1 Theorem B
(a) **Different route.**
- Existing proof, Steps 1–2: a kernel argument (Step 1 is the same as my "kernel view", worked in w = z²)
  shows det M ≠ 0 off V(e_nΔ_{n−1}). A replacement argument (a, −a) → (b, −b) shows det M = 0 on it.
- Existing proof, Step 3: the Nullstellensatz, irreducibility and weights give det M = c·Δ_{n−1}/e_n with
  c ∈ Q^× unspecified.
- My route: an explicit factorisation M = diag(L, (−1)^n/e_n)·N, with L lower unitriangular and N a
  column-signed Hurwitz matrix. It gives c_n = (−1)^{n(n+1)/2} in closed form.

(b) Step 3 checked line by line:
- *Polynomiality:* T_k is a polynomial in the P's, hence in e, and R enters only the last row. So
  N(e) = e_n det M ∈ Q[e]. Correct.
- *Weights:* the entry in row j, column k has weight 2j+1−k. In the last row, the entry 1 at column n−1 has
  weight 0 and R at column n has weight −1. The determinant therefore has weight
  ∑_{j=0}^{n−2}(2j+1) + (n−1) − n(n+1)/2 = (n²−3n)/2, and N has weight (n²−3n)/2 + n = C(n,2) = deg Π(m_i+m_j).
  Correct.
- *Irreducibility of Δ_{n−1} in C[e] = C[m]^{S_n}:* the factors m_i+m_j are pairwise non-associate and
  Δ is squarefree. S_n acts transitively on the pairs {i,j}, so a symmetric divisor contains all of them or
  none. Correct; for n = 2, Δ_1 = e_1.
- *Nullstellensatz:* Step 1 holds for all complex e (every e is the coefficient vector of some p), so
  V(N) ⊆ V(Δe_n). Each irreducible factor π generates a prime ideal, hence π | Δe_n and
  N = cΔ^β e_n^ι. Step 2 gives β ≥ 1, and the weights give β = 1, ι = 0. Correct.
- *Step 2:* two distinct e-vectors solve the same system, so M is singular. Correct (b ∉ {0, ±a} makes the
  multiset change).

So Step 3 is a valid proof of the shape. It does not give the constant. The text then says "c_n = ±1 computed
only for n ≤ 8" (§6 and STATUS). My factorisation proves c_n = (−1)^{n(n+1)/2} for every n, so the other
project claim is right. It also proves §0's observation, "the leading minors of the system are, up to sign,
Hurwitz determinants (checked n ≤ 8)", for all n. Because L is lower unitriangular, the leading k×k minor of M
(k ≤ n−1) equals that of N, which is (−1)^{⌊k/2⌋}Δ_{k−1}(p). This was checked exactly at signed rational points
for n = 2..9 (`check_phase2.txt` (5)). There is no discrepancy in the values: the text's c_3..c_8 and the
attack log's c_2..c_6 = −1,+1,+1,−1,−1 agree with mine.

### AU.1 Theorem C
- **(1)** (a) The existing proof reads off Q(z) − Q(−z) = −2e_{2n−3}(X)z³ from the vanishing odd e_j(X), and gets the
  converse from Lemma 1's second half. Mine uses F(w) = w^{2n}Q(1/w) and logarithms. The routes are
  equivalent: κ = −e_{2n−3}(X) in theirs and κ = (P_{2n−3}(m') − P_{2n−3}(m))/(2n−3) in mine, consistent by
  Newton's identity once the lower odd power sums of X vanish. (b) No discrepancy.
- **(2)** (a) Same route (column scaling by m_i², Vandermonde in m_i², implicit function theorem, permutations are
  at least the minimum gap away). (b) None.
- **(3)** (a) Same scaling argument. The text adds the explicit criterion R/k < n−2 for hyperbolicity.
  (b) No discrepancy in the statement or the table. Two discrepancies concern the §4 commentary; both are
  listed under "pair variety" and "control counts" below.

### AU.2 Lemma 1
(a) **Different route.** Theirs is short: by Newton, e_j is a Q-combination of products s_{i_1}⋯s_{i_r} with
∑ i_t = j, and an odd total forces an odd index i_t ≤ j; the converse is symmetric. Mine uses
f(z)/f(−z) = exp(2∑_{odd} s_k z^k/k) and gives explicit certificates. (b) Both are correct; no discrepancy.
Theirs is the cleaner proof for the paper.

### AU.3 Remark 2 and Remark 3
- **Remark 2:** c_n = −∏_{r<n}(2r−1) **agrees** with my Jacobian, −∏_{r=1}^{n−1}(2r−1) = −1, −1, −3, −15, −105,
  −945 for n = 1..6 (symbolic) and at exact points for n = 8..10. It also agrees with their own C(2)
  computation (c_0 = −1, c_r = 2r−1). The only issues are the ones already graded: the implicit lower limit
  r ≥ 1, the clash with Theorem B's c_n, and "checked n ≤ 7" where a one-line proof exists (their own C(2)
  column scaling is that proof).
- **Remark 3:** same route as mine. Their reference to "part C" of the 3-vs-4 search matches mine (none
  with orders ≤ 60).

### AU.4 table
Every entry matches my recomputation. Witnesses with I_3 collisions for n = 5: my class count for orders ≤ 60
is 134, equal to theirs (see the control counts below for orders ≤ 120).

### DF.6, DF.7
Not proved in `proof.md`. My REVIEW grades stand. DF.7's stale "not proved here" is confirmed by STATUS
("PROVED FOR ALL n").

## B. Specific claims the coordinator asked about

1. **Theorem B Step 3 (Nullstellensatz / irreducibility / weights): valid** (details in §A). It proves only
   c_n ∈ Q^×. The closed form c_n = (−1)^{n(n+1)/2} for all n is supplied by my factorisation.
2. **Theorem A multiplicity argument: valid** (details in §A).
3. **Remark 2, c_n = −∏(2r−1): correct** for every n, with r running over 1..n−1.
4. **"Witnesses are necessarily disjoint": correct.** If m = {a} ⊎ u and m' = {a} ⊎ u' share
   (R, P_1, …, P_{2n−5}), then u and u' are (n−1)-multisets sharing their full I_{n−1}. Theorem A then gives u = u',
   hence m = m'. Exact check: all 86 hyperbolic n = 3 witness pairs with orders ≤ 60 and all 11 n = 4 pairs with
   orders ≤ 90 are disjoint. This does not contradict the n = 5 I_3-control collisions that share an entry,
   such as {2,4,5,21,28} / {2,3,10,15,30}: those share only n−2 invariants (they are the n = 4 witness padded
   by 2).
5. **Pair-variety degree sum n²−2n+3: correct.** The n−1 equations have degrees 1, 3, …, 2n−5 and 2n−1, so the sum is
   (n−2)² + 2n − 1 = n²−2n+3. It exceeds 2n = dim P^{2n−1} + 1 exactly when (n−1)(n−3) > 0, i.e. n ≥ 4 (checked
   n = 3..10). **But the accompanying sentence is wrong in one respect.** "It is neither smooth nor irreducible
   (it contains the n! diagonal components)" does not hold as stated:
   - Every irreducible component of a variety cut out by n−1 equations in P^{2n−1} has dimension ≥ n
     (Krull). The permutation loci {m' = σm} have dimension n−1, so they are **not components**.
   - By Theorem C(2) itself, every point (m, m) with m distinct is a limit of off-diagonal points (m, m'(t)) of
     the variety. Exact instance: m = (2,3,5), e_3 = 30(1 + 10^{−k}), k = 3..8.
   - The defining equations have Jacobian rank n−1 at such points, so the variety is **smooth** there.
     Non-smoothness does hold elsewhere, e.g. at (a,…,a; a,…,a), where the rank is 1. Irreducibility is
     neither proved nor disproved by anything in the text.

   Since the paragraph is explicitly a heuristic, this is MINOR. Fix: "it is singular (e.g. at
   (a,…,a; a,…,a)) and contains the n! permutation loci, which have positive codimension in it; the
   Bombieri–Lang heuristic therefore does not apply directly".

## C. Further discrepancies found in the comparison (all MINOR, none in the frozen statements)

- **n = 4 integer witnesses are not rare.** proof.md §4 says the heuristic is "consistent with one primitive witness
  for n=4 in the scanned range", and STATUS says witnesses "become rare or absent for n≥4". The attack log reports
  11 witnesses with orders ≤ 90 but the author did not confirm the count. I confirm it exactly:
  - 11 hyperbolic n = 4 classes with orders ≤ 90, all pairs, all disjoint;
  - 9 of them primitive (gcd 1), e.g. {7,15,50,75}/{9,10,56,72}, {11,37,44,88}/{16,16,74,74} (full list in
    `check_phase2.txt` (2,3));
  - the primitive count grows with the bound. For comparison, the n = 3 bound ≤ 60 gives 86 classes, 58 of
    them primitive.

  The general-type heuristic predicts non-density, not finiteness or rarity, so nothing is contradicted
  formally. Still, the "one primitive witness" and "rare or absent for n ≥ 4" wording should be revised to the
  verified counts.
- **Control counts for n = 5 (orders ≤ 120).** The text gives 2317 I_3 collisions. My exact counts are 2309 classes
  and 2325 pairs, with 8 classes of size 3. 2317 = 2309 + 8 = ∑(|class| − 1), so the numbers are consistent
  once the counting convention is defined. For orders ≤ 60 all three conventions give 134. Fix: define what is
  counted.
- **Stale "verified only" entries.** §6 and STATUS list "c_n = ±1 for n ≤ 8" and "Hurwitz-minor structure of the
  elimination for n ≤ 8" as checked only in range. Both are proved for all n by the factorisation in REVIEW.md
  §Thm B, so they can move to "proved".
- **Heat input listed as "not re-derived".** REVIEW.md §AU.0 re-derives it for all l from the fetched Uçar text.
  §6 can cite that derivation.

## Addendum: grade changes

**None.** All REVIEW.md grades stand: AU.0 MINOR, Thm A NONE, Thm B MINOR, C(1)–(3) NONE, Lemma 1 NONE,
Remarks 2/3 MINOR, AU.4 MINOR, DF.6 NONE, DF.7 MINOR. The comparison found no FATAL or SERIOUS issue. The new
items in §B.5 and §C are MINOR and concern commentary in proof.md §4–§6 and STATUS.md, not the frozen statements.
