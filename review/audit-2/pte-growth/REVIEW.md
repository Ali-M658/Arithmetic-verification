# G5-bis blind review: group `pte-growth`

Reviewer input: `review/audit-2/REVIEWER-BRIEF.md`, `review/audit/G5-VERDICT.md`,
`review/audit-2/statements/pte-growth.md`, the context files it names
(`review/audit/statements/signatures.md`; `review/audit-2/statements/pte-structure.md` for PS.0 and PS.5),
and `review/audit-2/sources/`. Scripts: `check_lemma15.py`, `check_doubling.py`, `check_upper.py`,
`check_growth.py`, each with its `.txt` output (all exit 0, all assert-based, exact arithmetic).

## Summary table

| id | result | grade |
|---|---|---|
| PG.0 | Definitions 1.3, 1.4, PTE notation, Lemma 1.5 (1)(2)(3) | **MINOR** (wording of T^cone; witnesses and citation; L = 2 also holds) |
| PG.1 | Proposition 3.3 (doubling) | **MINOR** ("1 ∈ X∖Y" false under the multiset reading; case 1 ∈ X∩Y missing; the shared-coefficient conclusion is not stated) |
| PG.2 | Theorem 3.4 (upper bounds) | **MINOR** (true; the "[Sig] N(a)" citation for T_L ≤ 2^{2L−1} is not a statement of [Sig]; one proof obligation for T^cone) |
| PG.3 | Theorem 4.1 (square-root lower bound) | **NONE** |
| PG.4 | Theorem 4.2 (a)(b)(c) | **MINOR** (true; "L ≥ 2" and "β > 0" implicit; extracted statement truncated after "iff") |
| PG.5 | Theorem 4.3 (f_g, f_n) | **MINOR** (true; f_g, f_n need exact definitions; "≥ c√A" needs a range of A; explicit c given below) |
| PG.6 | statements.tex Theorem (Growth) | **MINOR** (true; final sentence names undefined quantities; (b) needs L ≥ 2) |

No FATAL and no SERIOUS finding. Every inequality was re-derived; no counterexample was found.

## Contamination

None. I opened only the files listed above. I did not open `theory/**`, `paper/**`, `review/referee-sim/**`,
any other session's scripts or outputs, or any `review/audit/**/REVIEW.md`. I opened
`review/audit-2/build_statements.py` only to grep the line range of PG.4 (lines 90–96: range tuples and anchors,
no proof text) after noticing the truncation.

## Instrument gaps

- Borwein–Ingalls 1994 (Enseign. Math. 40): e-periodica returns a captcha page; CECM 403 (see `fetches.md`).
  The citations "Prop. 2", "Prop. 3", "§6", "p. 8" are therefore unconfirmed. Both inequalities
  N(k) ≥ k+1 and N(k) ≤ ½k(k+1)+1 are re-proved below, so no result depends on the gap.
- Nothing else needed was unreachable.

## Inputs assumed (as instructed) and where my derivations use them

- [Sig] Lemma 4 (SG.4), both directions, including the converse "any paddings U = m⊎{1}^a, V = m'⊎{1}^b".
  Used by: Prop. 3.3, Thm 4.1, Thm 4.2(a), Thm 4.3. I use it in the form: if (g;m), (g';m') are hyperbolic
  signatures and some paddings satisfy (4.2), they have equal area and equal H_L. (Lemma 4 says "equal first L
  heat coefficients" and does not repeat that the signatures must be hyperbolic; that is implicit in "closed
  orientable hyperbolic 2-orbifolds" of its setting, and I always check hyperbolicity separately.)
- [Sig] Corollary S2 and Theorem T1(2): upper bounds for f, f_g, f_n.
- Lemma 1.2 (PS.0), **assumed as stated**: items (2) (realisation of a configuration), (4) (T ≥ 2L+2) and
  (5) (Area < 2πT when ι ≠ 0). Used by Def. 1.3's "2L+2 ≤ τ_L", by the meaning of "genus-0 realisation" in
  T^cone, and by the f_g threshold of Thm 4.3 (Area < 2π T_L). My derivation needs nothing beyond what (2), (4), (5)
  state. For L = 2, 3, 4 I also checked the realised genus-changing pairs directly (Lemma-4 conditions, genera,
  hyperbolicity, area) without using (5): `check_upper.txt`.
- Proposition 3.2 (PS.5), **assumed as stated**: items (1)–(3). Used by T_L ≤ 4N(2L−3). Needed in addition, and
  proved here: cancellation of pairs {z,−z} preserves every odd s_j, s_{−1} and ι (each pair contributes
  z^j + (−z)^j = 0 for odd j, 1/z − 1/z = 0, and +1 − 1 to ι). PS.5 says nothing about pairs {z,−z} *inside* Z(c)
  (they occur when x + x' = −2c or y + y' = −2c); the construction must cancel them. That is a proof step, not a
  defect of PS.5.
- [Sig] Lemma 5 (symmetric multisets) is quoted in the pte-structure bundle; I re-prove it (below) because Lemma
  1.5(3)'s lower bound needs it.

---

## PG.0. Definitions 1.3, 1.4, PTE notation, Lemma 1.5 — MINOR

### Derivation

**Def. 1.3 inequalities.** τ_L ≤ T_L and τ_L ≤ T^cone_L hold because T_L and T^cone_L are minima over
subsets of the L-configurations. τ_L ≥ 2L+2 is Lemma 1.2(4) (assumed).

**PTE facts.** N(k) ≥ k+1: if [A]=_k[B] with |A| = |B| = n ≤ k, the power sums p_1..p_n agree, so by
Newton's identities e_1..e_n agree, so ∏(x−a) = ∏(x−b) and A = B. N(k) ≤ ½k(k+1)+1: the pigeonhole argument
below with all exponents 1..k (sum k(k+1)/2) instead of the odd ones. N nondecreasing: a degree-(k+1) solution is a
degree-k solution. N(1) = 2 ({0,3},{1,2}).

**Lemma 1.5(1).** Take [A]=_{2L−3}[B] of size n = N(2L−3) and shift both by c = 1 − min(A∪B). Since
|A| = |B|, Σ(a+c)^j = Σ_i C(j,i)c^{j−i}P_i(A) and likewise for B, so all P_j, j ≤ 2L−3, stay equal; the sets stay
distinct; all entries are ≥ 1. Hence N_odd(L) ≤ N(2L−3).

**Lemma 1.5(2).** Let n = (L−1)²+1 and M ≥ 2. The n-multisets from {1..M} number
C(M+n−1, n) = M(M+1)…(M+n−1)/n! ≥ M^n/n!. For each odd j ≤ 2L−3, P_j takes integer values in [n, nM^j],
at most n(M^j−1)+1 < nM^j of them. There are L−1 odd exponents and Σ_{j odd ≤ 2L−3} j = (L−1)², so the vector
(P_1, P_3, …, P_{2L−3}) takes fewer than n^{L−1}M^{(L−1)²} values. If M^n/n! ≥ n^{L−1}M^{(L−1)²}, i.e.
M ≥ n!·n^{L−1} (since n − (L−1)² = 1), two distinct multisets share the vector. So "M > n!n^{L−1}" suffices
(and "≥" already does, because the value count is strict). Checked as exact integer inequalities for L = 2..9.

**Lemma 1.5(3), lower bound N_odd(L) ≥ L, for every L ≥ 2.** *Symmetric lemma:* a multiset Z of nonzero reals
with |Z| = m ≤ 2L−2 and p_j(Z) = 0 for odd j ≤ 2L−3 satisfies Z = −Z. Proof: Newton's identities give
e_k(Z) from p_1..p_k; for k ≤ 2L−3 the power sums of Z and −Z agree (even j trivially, odd j both 0), so
e_k(−Z) = e_k(Z) for k ≤ min(m, 2L−3). If m ≤ 2L−3 this is all k ≤ m. If m = 2L−2 the remaining one is
e_m(−Z) = (−1)^m e_m(Z) = e_m(Z) since m is even. So ∏(x−z) = ∏(x+z), Z = −Z.
Now let X ≠ Y be n-multisets of positive integers with equal odd P_j, j ≤ 2L−3, and n ≤ L−1. Cancel common
elements to X*, Y* (disjoint, equal size ≤ n, still equal odd sums, nonempty since X ≠ Y). Then
Z = X* ⊎ (−Y*) has size ≤ 2L−2 and vanishing odd sums, so Z = −Z, i.e. X* = Y*, contradicting disjointness and
nonemptiness. Hence N_odd(L) ≥ L.

**Upper bound N_odd(L) ≤ L for L = 3..6**: explicit witnesses, re-verified exactly (`check_lemma15.txt`):

| L | exponents | witness | origin |
|---|---|---|---|
| 2 | 1 | [1,4] = [2,3] | own |
| 3 | 1,3 | [1,5,5] = [2,3,6]; also [2,10,12] = [3,8,13] | own exhaustive search (smallest max entry, box ≤ 20); eslpower |
| 4 | 1,3,5 | [1,13,17,23] = [3,9,21,21] | own exhaustive search (box ≤ 30) and eslpower ("Smallest solution") |
| 5 | 1,3,5,7 | [3,19,37,51,53] = [9,11,43,45,55] | own search (streamed by P_1, first hit at P_1 = 163) and eslpower (Golden) |
| 6 | 1,3,5,7,9 | [7,91,173,269,289,323] = [29,59,193,247,311,313] | eslpower (Chen Shuwen 2000), re-verified; no own search |

So N_odd(L) = L for 2 ≤ L ≤ 6 (the statement says 3 ≤ L ≤ 6; L = 2 holds as well).

**L = 7 is not claimed, and it is unknown from the sources.** What is known: 7 ≤ N_odd(7) ≤ N(11) = 12
(ideal solutions exist for n = 12, CMSV p. 2). eslpower lists no (k = 1,3,…,11) solution of size 7.
For L ≥ 7 the statement correctly claims only the bounds (1), (2).

### Counterexample hunt

- Symmetric lemma exhaustive in boxes (L = 2: [−12,12]; L = 3: [−7,7]; L = 4: [−4,4]): every qualifying
  multiset is symmetric.
- No two distinct (L−1)-multisets with equal odd sums for L = 2 (box 60), 3 (box 40), 4 (box 25).
- Pigeonhole inequality exact for L = 2..9; collisions of size (L−1)²+1 exist for L = 2, 3 (trivially, since
  N_odd(L) = L ≤ (L−1)²+1).
- Side remark: eslpower calls [0,7,8] = [1,5,9] the "smallest solution" for (k = 1,3); my search finds
  [1,5,5] = [2,3,6] with a repeated entry, so eslpower's "smallest" is among distinct entries. Not relevant to
  the lemma.

### Findings and wording

1. *T^cone in Def. 1.3* says "whose genus-0 realisation is hyperbolic" without saying which realisation. The
   uncancelled pair of Prop. 3.3 and the cancelled primitive pair of Lemma 1.2(2) are different orbifolds.
   Replace with: "…with ι = 0 whose primitive integral form contains ±1 and for which the genus-0 pair
   $(0;U\setminus\{1\}),(0;V\setminus\{1\})$ of Lemma 1.2(2) ($U=Z_{>0}$, $V=-Z_{<0}$, $Z$ primitive) is hyperbolic."
2. *Lemma 1.5(3)*: replace "$N_{\rm odd}(L)=L$ for $3\le L\le6$" with
   "$N_{\rm odd}(L)\ge L$ for every $L\ge2$, with equality for $2\le L\le6$; for instance
   $[1,5,5]=[2,3,6]$, $[1,13,17,23]=[3,9,21,21]$, $[3,19,37,51,53]=[9,11,43,45,55]$ and
   $[7,91,173,269,289,323]=[29,59,193,247,311,313]$ (the last two from Golden and Chen, as tabulated at eslpower.org).
   For $L=7$ only $7\le N_{\rm odd}(7)\le N(11)=12$ is known to us."
3. *Citation*: the Borwein–Ingalls proposition numbers could not be checked (instrument gap). Keep them only if
   verified against the paper.

---

## PG.1. Proposition 3.3 (doubling) — MINOR

### Derivation

Let U = X ⊎ 2Y ⊎ 2Y, V = Y ⊎ 2X ⊎ 2X. For any j (including j = −1),
s_j(U) − s_j(V) = s_j(X) + 2·2^j s_j(Y) − s_j(Y) − 2·2^j s_j(X) = (1 − 2^{j+1})(s_j(X) − s_j(Y)).
For odd j ≤ 2L−3 the bracket vanishes; for j = −1 the factor 1 − 2^0 vanishes, whatever X and Y are.
Let U*, V* be U, V with common elements removed and Z = U* ⊎ (−V*). Removing common elements does not change
the differences s_j(U) − s_j(V) = s_j(Z), so s_j(Z) = 0 for odd j ≤ 2L−3 and s_{−1}(Z) = 0. Since |U| = |V| = 3n,
|U*| = |V*|, so ι(Z) = 0 and |Z| is even and ≤ 6n. U*, V* are disjoint sets of positive integers, so Z has no
pair {z,−z} and no 0.

*Nonempty.* If U = V, the generating polynomials x(t) = Σ_{x∈X} t^x, y(t) satisfy x(t) + 2y(t²) = y(t) + 2x(t²),
so d = x − y ≠ 0 satisfies d(t) = 2d(t²). The top exponent a ≥ 1 of d would equal 2a, impossible.

*Orbifolds.* 1 can lie in U only via X (2Y ≥ 2) and in V only via Y. Let μ_X, μ_Y be the multiplicities of 1.
U = (U∖{1}) ⊎ {1}^{μ_X} and V = (V∖{1}) ⊎ {1}^{μ_Y} are paddings with R(U) = R(V), P_j(U) = P_j(V) (odd j ≤ 2L−3),
|U| = |V|; by [Sig] Lemma 4 (converse, g = g' = 0) the genus-0 orbifolds (0;U∖{1}) and (0;V∖{1}) have equal
area and equal H_L, provided they are hyperbolic. Their signatures differ: if U∖{1} = V∖{1}, then |U| = |V| forces
μ_X = μ_Y and U = V. Cone counts: 3n − μ_X and 3n − μ_Y.

*Hyperbolicity.* n ≥ 2 (distinct 1-multisets cannot have equal P_1). Area/2π = −2 + Σ_{v∈V}(1−1/v).
If μ_Y = 0, every element of V is ≥ 2, so the sum is ≥ 3n/2 ≥ 3 > 2. If μ_Y > 0, the 2n elements of 2X ⊎ 2X are
≥ 2, so the sum is ≥ n; and μ_X, μ_Y > 0 forces n ≥ 3 (for n = 2, X = {1,a}, Y = {1,b} with equal P_1 gives X = Y),
so the sum is ≥ 3 > 2. Hyperbolic in every case.

*Area.* Each term 1 − 1/v < 1 and |V| = 3n, so Area/2π < 3n − 2, strictly, in every case.

So the statement holds when "1 ∈ X∖Y" is read as "1 ∈ X and 1 ∉ Y": then μ_Y = 0, (0;V) is a genuine signature,
and the cone counts differ by μ_X.

### Counterexample hunt (`check_doubling.txt`)

All unordered pairs X ≠ Y with equal odd sums: n = 2, L = 2 (entries ≤ 40, 5130 pairs); n = 3, L = 2 (≤ 14,
5514); n = 4, L = 2 (≤ 8, 2672); n = 3, L = 3 (≤ 40, 231); n = 4, L = 3 (≤ 16, 324); n = 4, L = 4 (≤ 30, 2). Each run
in both orders, non-disjoint pairs included. Checked: the identity for j = −1, 1, 3, …, 11 (also on 15,625 pairs
*without* equal sums), Z nonempty, Def. 1.1, ι = 0, |Z| ≤ 6n, both orbifolds hyperbolic, distinct signatures,
cone-count difference μ_X − μ_Y, area < 2π(3n−2), Lemma-4 conditions; U ≠ V for all X ≠ Y with n ≤ 3, entries ≤ 8.
0 failures. The cancelled realisation (0;U*∖{1}), (0;V*∖{1}) was hyperbolic in every case as well (not claimed by
Prop. 3.3; relevant to T^cone, see PG.2).

**Wording defect (found).** Under the multiset reading of X∖Y, the second sentence is false:
X = {1,1,5}, Y = {1,3,3} (equal P_1 = 7, L = 2) has 1 ∈ X∖Y (multiset), but
V = {1,2,2,2,2,3,3,10,10} contains 1, so "(0;V)" is not a signature, and the cone counts of
(0;U∖{1}) and (0;V∖{1}) differ by 1, not by the multiplicity 2 of 1 in X (`check_upper.txt`, last block).
Under the set reading, the case 1 ∈ X ∩ Y is not covered by the three bullets. The downstream uses (Thm 3.4,
4.1, 4.3) only need disjoint X, Y, so nothing downstream breaks. Also, the proposition never states that the
two orbifolds share their first L heat coefficients, which is what Theorems 4.1 and 4.3 use.

### Wording change

Replace the two bullets and the last line by:

> Let $\mu_X,\mu_Y$ be the multiplicities of $1$ in $X,Y$. Then $(0;U\setminus\{1\})$ and $(0;V\setminus\{1\})$ are
> hyperbolic genus-0 orbifolds with distinct signatures, equal area $<2\pi(3n-2)$ and equal first $L$ heat
> coefficients; their cone counts are $3n-\mu_X$ and $3n-\mu_Y$. In particular, if $X\cap Y=\emptyset$ (which can
> always be arranged by cancelling common elements) and $1\in X$, then $V$ contains no $1$ and the cone counts of
> $(0;U\setminus\{1\})$ and $(0;V)$ differ by $\mu_X$; if $1\notin X\cup Y$ they are equal.

---

## PG.2. Theorem 3.4 (upper bounds) — MINOR

### Derivation

**τ_L ≤ 6N_odd(L) ≤ 6(L−1)²+6.** Apply Prop. 3.3 to a pair of size N_odd(L): an L-configuration of size
≤ 6N_odd(L). Then Lemma 1.5(2).

**T^cone_L ≤ 6N(2L−3).** Take [A]=_{2L−3}[B] of size N = N(2L−3). Cancel common elements: A', B' disjoint,
size n ≤ N, distinct, still equal P_1..P_{2L−3} (equal sizes). Shift by c = 1 − min(A'∪B'): still equal
P_1..P_{2L−3} (binomial expansion, equal sizes), entries ≥ 1, and 1 lies in exactly one of them, say X (swap
otherwise). In particular the odd sums agree, so Prop. 3.3 applies with X ∩ Y = ∅, 1 ∈ X, 1 ∉ Y. Z = U* ⊎ (−V*)
has ι = 0, size ≤ 6n ≤ 6N, and 1 ∈ Z (1 ∈ U, 1 ∉ V, so it survives cancellation); hence Z is already primitive and
contains 1.
*Proof obligation not covered by Prop. 3.3:* T^cone requires the genus-0 realisation of the **cancelled** Z to be
hyperbolic; Prop. 3.3 proves it for the uncancelled pair only. It holds: V* ⊂ V has no 1s, so all its elements are
≥ 2, and |V*| = |Z|/2 ≥ L+1 by Lemma 1.2(4). For L ≥ 4, Σ_{V*}(1−1/v) ≥ 5/2 > 2. For L = 3, the sum is ≥ 2 with
equality only for V* = {2,2,2,2}; then U* would be 4 positive integers ≠ 2 with R = 2 and P_1 = 8, which is impossible
(at most one 1 can occur, and {1,a,b,c} with 1/a+1/b+1/c = 1, a,b,c ≥ 3 forces {3,3,3}, sum 10). For L = 2 the bound is
a single number; the explicit example below (Area/2π = 5/3) suffices.

**T_L ≤ 4N(2L−3).** With X = A', Y = B' disjoint (Prop. 3.2 requires X ∩ Y = ∅, hence the cancellation),
|X| = |Y| = n ≤ N. By Prop. 3.2(2) choose rational c ∉ −X ∪ −Y in an open interval with ι(Z(c)) ≠ 0, and by
Prop. 3.2(3) (ρ a nonzero rational function, so finitely many zeros) with ρ(c) ≠ 0. Choose rational
c' > −min(X ∪ Y) with ρ(c') ≠ 0; then ι(Z(c')) = 0. Put λ = −ρ(c')/ρ(c) ∈ ℚ^×. Then
s_{−1}(Z(c) ⊎ λZ(c')) = ρ(c) + ρ(c')/λ = 0, every odd s_j vanishes (s_j(λW) = λ^j s_j(W)), and
ι = ι(Z(c)) + sgn(λ)·0 ≠ 0. Cancel pairs {z,−z} (this preserves all of these and ι; see "Inputs"). The result is
nonempty (ι ≠ 0), has even size (ι is even by Prop. 3.2(2), and |Z| ≡ ι mod 2), no 0, no pair: an L-configuration
with ι ≠ 0 and size ≤ 2n + 2n ≤ 4N. (Minimality of the PTE solution is not needed, only cancellation.)

**Arithmetic.** ½(2L−3)(2L−2)+1 = (2L−3)(L−1)+1 = 2L²−5L+4. Checked for 2 ≤ L < 10^4.

### Tests on explicit data (`check_upper.txt`)

Own PTE solutions: degree 1 [0,2]=[1,1]; degree 3 [0,3,4,7]=[1,1,6,6] (own exhaustive search); degree 5
[±7,±7,0,0]=[±3,±5,±8] (own, from Σx² = 2Q, Σx⁴ = 2Q² on {a,b,a+b}, Q = a²+ab+b² = 49); eslpower's
[0,5,6,16,17,22]=[1,2,10,12,20,21] re-verified. For L = 2, 3, 4 (N = 2, 4, 6):

| L | τ (doubling of N_odd witness) | T^cone (shift + doubling) | T (shift construction) |
|---|---|---|---|
| 2 | 12 ≤ 12 | 12 ≤ 12; contains 1; cancelled Area/2π = 5/3 | 8 ≤ 8, ι = −2, genera 1, 0, Area/2π = 13/8 |
| 3 | 16 ≤ 18 | 22 ≤ 24; cancelled Area/2π = 877/140 | 16 ≤ 16, ι = −2, genera 1, 0 |
| 4 | 24 ≤ 24 | 34 ≤ 36; cancelled Area/2π = 103723/8568 | 24 ≤ 24, ι = 2, genera 0, 1 |

Every Def. 1.1 condition, ι, primitivity, the Lemma-4 conditions of the realisation, hyperbolicity, and the area
bounds were checked exactly. The L = 2 T-configuration is the primitive Z = {1,3,24,−2,−2,−8,−8,−8}.

### Findings and wording

1. "The previous bound was $T_L\le2^{2L-1}$ ([Sig] N(a))": the audited statement of [Sig] Theorem N(a) gives
   an area bound $2\pi(4^{L-1}-1)$, not a size bound; the size is only visible in the proof/construction (SG.11 is
   consistent: $1023+1025=2^{11}$ at $L=6$). Replace by: "The Prouhet construction in the proof of [Sig] Theorem N(a)
   gave $T_L\le2^{2L-1}$."
2. Add to the proof (not the statement): the cancelled genus-0 realisation in the T^cone bound is hyperbolic
   (argument above). No change to the statement.

---

## PG.3. Theorem 4.1 (square-root lower bound) — NONE

### Derivation

Let n = N_odd(L) and X ≠ Y attain it. By minimality X ∩ Y = ∅ (cancelling a common element gives a smaller
distinct pair). Since X ∩ Y = ∅, one of the three bullets of Prop. 3.3 applies (and the extended version above covers every case anyway): (0;U∖{1}), (0;V∖{1}) are hyperbolic, genus 0, distinct signatures, equal H_L, area
< 2π(3n−2) ≤ 2π(3((L−1)²+1)−2) = 2π(3(L−1)²+1).

If O, O' have distinct signatures and H_L(O) = H_L(O'), then for each k ≤ L the condition in DF.2's definition of
K_mult(O; Sig) fails at k (H_k(O') = H_k(O), σ(O') ≠ σ(O)), so K_mult(O; Sig) ≥ L+1, and likewise for O'. Thus
both members have K_mult ≥ L+1, and f(A) ≥ L+1 whenever A ≥ 2π(3(L−1)²+1) (the area is strictly smaller, so
non-strict suffices).

For A ≥ 8π let x = A/2π ≥ 4 and L the largest integer ≥ 2 with 3(L−1)²+1 ≤ x, i.e. (L−1)² ≤ (x−1)/3. For
y ≥ 0 the largest integer k ≥ 0 with k² ≤ y is ⌊√y⌋, so L−1 = ⌊√((x−1)/3)⌋ and f(A) ≥ L+1 =
⌊√((A/2π−1)/3)⌋ + 2. A ≥ 8π is exactly what makes L ≥ 2 available (x = 4 gives L = 2, bound 3).

### Counterexample hunt (`check_growth.txt`)

Exact rationals at every breakpoint x = 3m²+1 (m < 1500), and at x ± 10^{−9}, x ± 10^{−30}: 7493 points, the
"largest L" equals the formula each time. A = 8π exactly gives 3; just below 8π no L ≥ 2 qualifies. The bound
dominates [Sig] Corollary N1 at every integer A/2π in [4, 5000).

No change required.

---

## PG.4. Theorem 4.2 — MINOR

### (a) Derivation

f(A) ≥ L+1 gives O with Area(O) = A_0 ≤ A and K_mult(O) ≥ L+1, so k = L fails: there is O' with σ' ≠ σ and
H_L(O') = H_L(O). [Sig] Lemma 4 gives paddings U, V with (4.2) and |U|+|V| = 2max(n+g−g', n'+g'−g).
Cancel common elements: Z = U* ⊎ (−V*) is nonempty (U = V would force g = g' and m = m'), has s_j(Z) = 0 for odd
j ≤ 2L−3, and no pair {z,−z}. Then Z and −Z are distinct (Z ≠ −Z, as Z has no pair and is nonempty) and have equal
power sums for j = 1..2L−2 (even j trivially, odd j both 0): a PTE solution of degree 2L−2 and size |Z|. So
N(2L−2) ≤ |Z| ≤ |U|+|V|.
Bound: with s = A_0/2π = 2g−2+n−R(m) and R(m) ≤ n/2, n ≤ 2s+4−4g, so n+g−g' ≤ 2s+4−3g−g' ≤ 2s+4; same for the
primed side (equal area). So |U|+|V| ≤ 4s+8 = 2A_0/π+8, hence ≤ ⌊2A_0/π⌋+8. **Evenness is needed:** |U|+|V|
is even, and the largest even integer ≤ ⌊2t⌋+8 is 2⌊t⌋+8. So |U|+|V| ≤ 2⌊A_0/π⌋+8 ≤ 2⌊A/π⌋+8. Without the
evenness step one only gets ⌊2A/π⌋+8, which exceeds the printed constant by 1 for t = A/π with frac(t) ≥ ½
(t = 3/2 in the script). The printed constant is right.

### (b) Derivation

By the argument of Thm 4.1, f(A) ≥ L+1 whenever 2π(3N_odd(L)−2) ≤ A; and N_odd(L) ≤ N(2L−3) ≤ C(2L−3)^β, so
6πC(2L−3)^β ≤ A suffices. Put x = (A/6πC)^{1/β}. If x ≥ 1, L = ⌊(x+3)/2⌋ ≥ 2 has 2L−3 ≤ x, so
f(A) ≥ L+1 ≥ (x+2)/2+1 > x/2. If x < 1 ("otherwise"), x/2 < ½ < 3 ≤ f(A) (Thm 4.1, A ≥ 8π), or simply f ≥ 1.
The hypothesis forces β ≥ 1 (N(k) ≥ k+1), so 1/β is meaningful; the statement should say β > 0.

### (c) Derivation

"⇐": (b) with β = 1/α ≥ 1 gives f(A) ≥ ½(6πC)^{−α}A^α for all A ≥ 8π.
"⇒": suppose f(A) ≥ cA^α for A ≥ A_0. Given k ≥ 1, put L = ⌈k/2⌉+1 ≥ 2, so 2L−2 ≥ k and L+1 ≤ 3k. Let
A = max(A_0, ((L+1)/c)^{1/α}); then f(A) ≥ cA^α ≥ L+1, so by (a) and monotonicity of N,
N(k) ≤ N(2L−2) ≤ 2A/π+8 ≤ 2A_0/π + (2/π)(3k/c)^{1/α} + 8 ≤ C k^{1/α} for a suitable C (k ≥ 1). Small k are
absorbed by taking A ≥ A_0. Integer-valuedness and monotonicity of f are not used (A is chosen explicitly; f is
integer-valued and nondecreasing anyway).
α ∈ (0,1]: for α > 1 both sides are false (f ≤ A/π+4, N(k) ≥ k+1), so the restriction is harmless.
α = 1: f ≥ cA for large A iff N(k) = O(k); with f(A) ≤ ⌊A/π⌋+4 = O(A) (S2), f = Θ(A) iff N(k) = O(k).

Commentary "any exponent above ½ would give N(k) = O(k^{2−ε})": not in my bundle; the algebra is right
(α > ½ gives 1/α = 2 − ε with ε = 2 − 1/α > 0).

### Counterexample hunt (`check_growth.txt`)

n+g−g' ≤ 2s+4 on 54,708 (signature, g') cases; equality at (0;2,2,2,2,2); the evenness identity on 4000
rational t; worked instance (1;15) ~ (0;3,3,5,5) (Lemma-4 conditions, |U|+|V| = 6 ≤ 10, the size-6 PTE
solution of degree 2); the (b) step on 19,999 rational x; (c) index inequalities for k < 10^5; C = 2, β = 2
admissible and (b) then never exceeds Thm 4.1.

### Findings and wording

1. **Extraction defect**: PG.4 as extracted (proof.md lines 342–350) ends "In particular $f(A)=\Theta(A)$ iff"
   with no conclusion; the range should end one line later. Reviewers saw a truncated statement. (PG.6 has the
   full sentence.) Fix the range in `build_statements.py`, and check the source sentence is complete.
2. (a): "If $L\ge2$ and $f(A)\ge L+1$, then …" ($N(0)$ is not defined by the PTE notation).
3. (b): "If $\beta>0$ and $N(k)\le Ck^\beta$ for all $k\ge1$ …" (or note that the hypothesis forces $\beta\ge1$).

---

## PG.5. Theorem 4.3 — MINOR

### What f_g, f_n must mean

$K_g(\mathcal O)=\min\{k\ge1:\ \forall\mathcal O'\in\mathrm{Sig},\ H_k(\mathcal O')=H_k(\mathcal O)\Rightarrow g(\mathcal O')=g(\mathcal O)\}$,
$f_g(A)=\max\{K_g(\mathcal O):\mathcal O\in\mathrm{Sig},\ \mathrm{Area}(\mathcal O)\le A\}$;
$K_n(\mathcal O)=\min\{k\ge1:\ \forall\mathcal O'\in\mathcal P_0,\ H_k(\mathcal O')=H_k(\mathcal O)\Rightarrow n(\mathcal O')=n(\mathcal O)\}$,
$f_n(A)=\max\{K_n(\mathcal O):\mathcal O\in\mathcal P_0,\ \mathrm{Area}(\mathcal O)\le A\}$, n = number of cone points.
("The largest number of coefficients needed" is this; both are finite by S2/T1.)

### Derivation

*f_g.* T_L ≤ 4N(2L−3) (PG.2) gives an L-configuration with ι ≠ 0 of size T ≤ 4N(2L−3); Lemma 1.2(2),(5)
(assumed) realise it by two orbifolds of genera differing by |ι|/2 ≠ 0, equal H_L, Area < 2πT ≤ 8πN(2L−3). If
A ≥ 8πN(2L−3), both have area ≤ A and K_g ≥ L+1, so f_g(A) ≥ L+1. Strictness: the area is strictly below the threshold, so the non-strict "A ≥ 8πN(2L−3)" is right.
*f_n.* The shifted-PTE doubling of PG.2 gives X ∩ Y = ∅, 1 ∈ X, and (0;U∖{1}), (0;V): genus 0, hyperbolic,
equal H_L, cone counts differing by μ_X ≥ 1, area < 2π(3n−2) ≤ 2π(3N(2L−3)−2). So A ≥ 2π(3N(2L−3)−2) gives
f_n(A) ≥ L+1. (Uses the uncancelled pair, which Prop. 3.3 covers.)
*Explicit c.* With N(2L−3) ≤ 2L²−5L+4 ≤ 2L²: f_g(A) ≥ L+1 for L = ⌊√(A/16π)⌋ ≥ 2, so
**f_g(A) ≥ √(A/16π) for A ≥ 16π**. With 3(2L²−5L+4)−2 = 6L²−15L+10 ≤ 6L² (L ≥ 1): **f_n(A) ≥ √(A/12π) for
A ≥ 8π**. (At L = 2, N(1) = 2: f_g ≥ 3 from A ≥ 16π, f_n ≥ 3 from A ≥ 8π.) Since K_g, K_n ≥ 1, these bounds
in fact hold for every A for which the max is over a nonempty set.
*Upper bounds.* K_g(O) ≤ K_mult(O; Sig) pointwise, so f_g ≤ f ≤ ⌊A/π⌋+4 (S2). K_n(O) ≤ K_mult(O; P_0) ≤ ⌊A/π⌋+4
(T1(2)), and K_mult(O;P_0) ≤ K_mult(O;Sig), so f_n ≤ f.
*4.2(c) for f_g, f_n.* "⇐": the two thresholds with N(2L−3) ≤ C(2L−3)^{1/α}, exactly as in 4.2(b) (constants
8πC resp. 6πC). "⇒": f_g ≤ f and f_n ≤ f, then 4.2(c) for f.

### Counterexample hunt

Exact grid of A/π up to 10^4 for both explicit-c claims; the realised pairs for L = 2, 3, 4 meet both thresholds
(`check_upper.txt`: f_g Area/2π = 13/8 < 8 at L = 2, etc.).

### Wording change

Replace the first bullet and "Both are therefore $\ge c\sqrt A$" by:

> Let $K_g(\mathcal O)$ (resp. $K_n(\mathcal O)$) be the least $k$ such that every $\mathcal O'\in\mathrm{Sig}$
> (resp. every genus-0 $\mathcal O'$) with $H_k(\mathcal O')=H_k(\mathcal O)$ has the same genus (resp. the same
> number of cone points) as $\mathcal O$, and let $f_g(A)$, $f_n(A)$ be the maxima of $K_g$ over $\mathrm{Sig}$ and
> of $K_n$ over genus-0 orbifolds of area $\le A$. … Consequently $f_g(A)\ge\sqrt{A/16\pi}$ for $A\ge16\pi$ and
> $f_n(A)\ge\sqrt{A/12\pi}$ for $A\ge8\pi$.

---

## PG.6. statements.tex Theorem (Growth) — MINOR

Compared with PG.3–PG.5: (a) is Thm 4.1 plus S2 (both re-derived, true for A ≥ 8π); (b) is 4.2(a); (c) is 4.2(c)
with the complete "f = Θ(A) iff N(k) = O(k)" sentence (true). Differences:

1. (b) lacks "$L\ge2$". Replace "If $f(A)\ge L+1$" by "If $L\ge2$ and $f(A)\ge L+1$".
2. The last sentence uses two quantities never defined in the manuscript version and "up to the constant" with no
   range. Replace by: "The lower bound in (a) also holds, with $\sqrt{A/16\pi}$ for $A\ge16\pi$, for the least number
   of coefficients that determine the genus, and, with $\sqrt{A/12\pi}$ for $A\ge8\pi$, for the least number that
   determine the number of cone points among genus-0 orbifolds (both maximised over area $\le A$)."
3. The manuscript version should not use N without recalling it (it is defined in `subsec:pte`, PS.6; fine if the
   theorem stays in that subsection).
4. Bundle note: PG.6's title mentions "Theorem (Descartes)", which is not in the PG.6 excerpt (it is in PS.6).
