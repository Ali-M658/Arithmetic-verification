# G5-bis blind review — group `pte-structure`

## Summary of grades

| id | statement | grade |
|---|---|---|
| PS.0a | Setting + Definition 1.1 (incl. odd example {−24,−18,−8,5,45}) | NONE |
| PS.0b | Lemma 1.2 (dictionary), items 1–5 | MINOR |
| PS.1 | Theorem 2.1 (Descartes bound), items 1–2 | NONE |
| PS.2 | Proposition 2.2 (PTE lower bound) | NONE (τ_L is not defined in the bundle; see below) |
| PS.3 | Proposition 2.3 (a)(b)(c) | NONE (the "no pair" hypothesis in (a) is redundant) |
| PS.4 | Theorem 3.1 (pencil) | MINOR ("Equivalently" clause) |
| PS.5 | Proposition 3.2 (shift) | MINOR (n ≥ 1 is implicit) |
| PS.6 | statements.tex versions | **SERIOUS** (one sentence false as printed) + MINOR ×3 |

No result is false. The single SERIOUS finding is a manuscript-facing "exactly when" sentence that leaves out the genus condition. The proof.md Setting states that condition correctly.

## Contamination

None. I did not open `theory/pte/**`, `theory/revision/**`, `paper/**`, `review/referee-sim/**` or any other session's scripts or outputs. For transparency:
- I read the head of `review/audit-2/STATEMENTS.md`, which repeats my own bundle.
- A `grep` for "Borwein" in that file showed five one-line statement excerpts from other groups' bundles (lines 177–179, 192, 222, 248, 388, 439, 1531). These are statements, not proofs, and they told me nothing about any proof in my bundle.

## Instrument gaps

- **Borwein–Ingalls 1994** (Enseign. Math. 40): e-periodica serves a CAPTCHA (see `fetches.md`). Not verified:
  - "p. 8" (odd ideal symmetric);
  - "Props. 2, 3";
  - "§1";
  - "§6".

  Both bounds k+1 ≤ N(k) ≤ k(k+1)/2+1 were re-proved here. Croot–Mao–Yip, arXiv:2609.05061, p. 1 (fetched) states the same bounds and the same open status. That is a secondary source only.

## Scripts (all exact, assert-style, exit nonzero on failure; all exited 0)

Run with `/opt/homebrew/Caskroom/miniforge/base/bin/python3 check_x.py > check_x.txt`.

| script | content |
|---|---|
| `confenum.py` | Shared module: exhaustive enumeration of integer L-configurations, Z = U ⊎ (−V), entries ≤ H, size ≤ Tmax |
| `check_descartes.py` | Theorem 2.1 and Lemma 1.2(4): exhaustive boxes; a Descartes certificate on every configuration; targeted search for violators with N ≤ L−1, no bound on \|U\| |
| `check_attain.py` | Meet-in-the-middle search of the shapes (\|U\|,\|V\|) for L = 2, 3, 4 |
| `check_dictionary.py` | Definition 1.1 example; Lemma 1.2 items 1–5 on every primitive configuration found; L = 1 |
| `check_balanced.py` | Proposition 2.3 (a)(b) on the reviewer's own odd symmetric sets for L = 2, 3, 4; Proposition 2.2; N(k) ≥ k+1 spot check |
| `check_pencil.py` | Theorem 3.1: sympy identity for m = 4..10; box searches m = 4..8; "Equivalently" counterexample; degenerate cases |
| `check_pencil_fibre.py` | Supplementary fibre search, m = 5 |
| `check_shift.py` | Proposition 3.2 on the reviewer's own PTE solutions |
| `check_ps6.py` | Witnesses for the PS.6 wording findings |

## Notation and two tools used throughout

For a multiset Z of nonzero rationals of size T:
- p_Z(x) = ∏(x−z) = Σ_k (−1)^k e_k x^{T−k};
- s_j = Σ z^j;
- P = #{z>0}, N = #{z<0}, ι = P − N.

**Fact A (parity of Newton).** Let K be odd. Then e_k = 0 for all odd k < K if and only if s_j = 0 for all odd j < K.

*Proof.* Write ∏(1−zt) = E(t) + O(t), with E even and O odd. Then
- the odd part of log∏(1−zt) = −Σ s_j t^j/j is artanh(O/E);
- O = O(t^K) if and only if artanh(O/E) = O(t^K).

Also s_{−1} = e_{T−1}/e_T, and e_T ≠ 0.

**Fact B (Lemma 5 re-proved).** If T ≤ 2L−2 and s_j = 0 for odd j ≤ 2L−3, then every odd e_k with k ≤ T vanishes.
- T even: p_Z is even, so Z = −Z.
- T odd: e_T = 0, so 0 ∈ Z.

So a nonempty pair-free multiset of nonzero numbers with these vanishing sums has T ≥ 2L−1.

**Descartes.** P is at most the number of sign changes V(p_Z). N is at most V(p_Z(−x)). Zero coefficients are skipped and roots are counted with multiplicity.

---

## PS.0a Setting and Definition 1.1 — NONE

**Derivation of the Setting.** By [Sig] Lemma 4 (4.2), padding with R(U) = R(V) gives P_j(U) = P_j(V) for odd j ≤ 2L−3 and |V|−|U| = 2(g−g'). Cancelling common elements removes the same number of elements from U and V. It changes no power-sum difference. So Z = U*⊎(−V*) satisfies:
- s_j(Z) = P_j(U*) − P_j(V*) = 0;
- s_{−1}(Z) = R(U*) − R(V*) = 0.

Z has no pair {z,−z}, because U* ∩ V* = ∅. Z is nonempty: U = V would force m = m' (all m_i ≥ 2) and g = g', contradicting σ ≠ σ'. Finally, |U*|+|V*| ≡ |V*|−|U*| = 2(g−g') mod 2, and |V*|−|U*| = 2(g−g').

**Odd example.** {−24,−18,−8,5,45} has s₁ = 0 and s₋₁ = 0 exactly (`check_dictionary.txt`).

## PS.0b Lemma 1.2 — MINOR

**Item 1.** s_j(λZ) = λ^j s_j(Z). The vanishing conditions, the pair-freeness and T are therefore preserved. For λ < 0 the signs swap, so ι ↦ sgn(λ)ι. Checked with λ ∈ {−3, 1/2, −2/7} on 364 primitive configurations.

**Item 2.** For a genus h and a multiset W of positive integers, Area/2π of (h; W without its 1s) is 2h − 2 + |W| − R(W), because 1s contribute 0. So

Area(U-side)/2π − Area(V-side)/2π = 2(g−g') + ι − s₋₁(Z) = 0  when g − g' = −ι/2.

Equal area means hyperbolicity holds on both sides or on neither. Raising both genera by 1 adds 4π to the area. So "least smaller genus with both hyperbolic" exists and is well defined.

The signatures are distinct:
- if ι ≠ 0, the genera differ;
- if ι = 0, the order multisets are disjoint (no pair), and they cannot both be empty, because that would force Z to be empty.

[Sig] Lemma 4 (converse), applied to the paddings U = Z_{>0} and V = −Z_{<0}, gives "share at least L". By [Sig] Lemma 4 at L+1, together with ψ_k(1) = 0 (so padding does not change Ψ_k) and R(U) = R(V), the two sides share L+1 coefficients if and only if P_{2L−1}(U) = P_{2L−1}(V), that is, s_{2L−1}(Z) = 0. Hence "exactly L iff s_{2L−1}(Z) ≠ 0".

**Attack: does the genus choice always exist, and what if genus 0 fails?** For every L ≥ 2 the smaller genus is always 0. Proof: let W be the side with more elements (either side if ι = 0). This is the smaller-genus side. Genus 0 is hyperbolic if and only if R(W) < |W| − 2.
- At most one side contains 1. In both cases R(W) ≤ |W|/2:
  - if 1 ∉ W, then directly;
  - if 1 ∈ W, then R(W) = R(W') ≤ |W'|/2 ≤ |W|/2.
- So genus 0 works whenever |W| ≥ 5.
- Since |W| ≥ T/2 ≥ L+1 ≥ 3, only |W| ∈ {3, 4} remains.
- **|W| = 3** (T = 6, ι = 0). The pair-free side X without 1 would need R(X) ≥ 1. Then X ∈ {(2,2,n), (2,3,3..6), (2,4,4), (3,3,3)}. Matching sums and reciprocal sums against a disjoint partner (with or without 1) leads every time to a quadratic with negative discriminant or to unequal sums.
- **|W| = 4.** This forces W or its partner to be (2,2,2,2) against {1,3,3,3} or {1,1}. The sums are unequal.

For L = 1 genus 1 does occur. Examples (`check_dictionary.txt`):
- Z = (−6,−3,−2,1) gives (2;∅) ~ (1;2,3,6);
- Z = (−8,−8,−1,2,2,4) gives (1;2,2,4) ~ (1;8,8).

Every one of the 364 primitive configurations with L ≥ 2 has smaller genus 0.

**Attack: "U∖{1}" with 1 of multiplicity ≥ 2.** Z = (−15,−5,−1,−1,2,2,2,3,3,10) is a 2-configuration with 1 ∈ V twice. Removing a single 1 would leave an order-1 point. The intended meaning, "remove all 1s", gives (0;2,2,2,3,3,10) ~ (1;5,15), which share exactly 2 coefficients. This is a wording finding.

**Item 3.** ι ≠ 0 if and only if g ≠ g'. If ι = 0, then |U| = |V|, and the cone counts differ by the number of 1s. Only one side can contain 1s. So the counts differ if and only if ±1 ∈ Z, and the difference equals the multiplicity of ±1. Checked on all configurations. Here "Z" is the primitive scaling of item 2.

**Item 4.** T is even by definition. T ≥ 2L+2 is re-proved below (PS.1) for every L-configuration, not only for those coming from orbifolds.

**Item 5.**
- **ι ≠ 0, genus 0:** Area/2π = |W| − R(W) − 2 < (T+|ι|)/2 − 2 ≤ T − L − 2 < T.
- **ι ≠ 0, genus 1 (only possible for L = 1):** Area/2π = |W| − R(W) < |W| ≤ T − 1.
- **ι = 0:** Area/2π = −2 + Σ_V(1 − 1/v) < |V| − 2 = T/2 − 2. Each term is < 1.

So Area < 2πT is true but loose. The largest ratio observed was Area/(2πT) = 53/176. For L ≥ 2 the hypothesis "the genus-0 realisation is hyperbolic" is automatic.

**L = 1.** The definition is meaningful: the only condition is s₋₁ = 0, and T ≥ 4. Size T = 2 would need 1/a + 1/b = 0, so b = −a. 74 configurations with entries ≤ 8 and T ≤ 6 were tested.

**Wording change.** In item 2, replace "$(g;U\setminus\{1\})$ and $(g';V\setminus\{1\})$" by "$(g;U^{\ne1})$ and $(g';V^{\ne1})$, where $W^{\ne1}$ is $W$ with every entry $1$ removed". After "both are hyperbolic", add: "(both sides have equal area, so this is one condition; for $L\ge2$ the smaller genus is always $0$)". In item 5 (optional, sharper), use "If $\iota\ne0$ and $L\ge2$, then $\operatorname{Area}/2\pi<T-L-2$; in all cases $\operatorname{Area}<2\pi T$." Delete "and the genus-0 realisation is hyperbolic", or keep it with "(automatic for $L\ge2$)".

---

## PS.1 Theorem 2.1 — NONE

**Proof.**
1. By Fact B, T ≥ 2L−1.
2. By Fact A, e_k(Z) = 0 for the L−1 odd indices k ≤ 2L−3.
3. Since s₋₁ = e_{T−1}/e_T = 0, also e_{T−1} = 0. Here T−1 > 2L−3.
4. So p_Z has at most T+1−L nonzero coefficients.
5. By Descartes, P ≤ T−L and N ≤ T−L. Hence min(P,N) ≥ L and |ι| = T − 2min(P,N) ≤ T − 2L.

**T ≥ 2L+2 (Lemma 1.2(4), re-proved without [Sig]).** If T = 2L, then every odd e_k with k ≤ T−1 vanishes. So Z = −Z and Z contains a pair. Hence T ≥ 2L+1, and since T is even, T ≥ 2L+2.

**Items 1 and 2.**
- Item 1: ι = |U*| − |V*| = 2(g'−g).
- Item 2: at T = 2L+2, |ι| ≤ 2 and ι is even, so ι ∈ {0, ±2}. If ι = ±2, then {|U*|,|V*|} = {L, L+2}.

**Hunt.**
- Exhaustive boxes (H, Tmax) = (30,6), (22,8), (15,10), (10,12). For every L ≤ maxL(Z), each configuration was checked against the bound, the size claim, the T = 2L+2 claim, and the Descartes certificate: zero e_k as predicted, at most T−L+1 nonzero coefficients, and P ≤ V(p) ≤ T−L. Zero coefficients and multiplicities were included. No failure.
- Targeted violator search: all V with |V| ≤ L−1 against every U, with no bound on |U| or its entries (pruned DFS over partitions, cross-checked against brute force).

  | L | entries of V |
  |---|---|
  | 2 | ≤ 400 |
  | 3 | ≤ 60 |
  | 4 | ≤ 18 |

  0 violators.
- **Attainment.** For L = 2 the bound is attained at T = 6 (e.g. (−30,−2,5,9,9,9)) and at T = 8 with |ι| = 4: (−10,−10,−8,−5,−4,−4,1,40) and two others, all with entries ≤ 40. For L = 3:

  | T | shape | entries | configurations found |
  |---|---|---|---|
  | 8 | (4,4) | ≤ 60 | 1 up to scaling: (−28,−21,−5,−4,3,10,15,30) |
  | 8 | (3,5) genus-changing | ≤ 60 | 0 |
  | 10 | (4,6) | ≤ 26 | (−21,−7,−7,−5,−3,−3,1,15,15,15), which is [Sig]'s (1;15,15,15) ~ (0;3,3,5,7,7,21) |
  | 10 | (3,7) | ≤ 24 | 0 |

  For L = 4, T = 10: none with entries ≤ 30. So item 2's genus-changing case is not exhibited for L ≥ 3 in these boxes. The theorem does not claim it.

## PS.2 Proposition 2.2 — NONE

s_j(−Z) = (−1)^j s_j(Z). For even j the two sums agree trivially. For odd j ≤ 2L−3 both vanish. So [Z] =_{2L−2} [−Z]. Since Z is pair-free and nonempty, Z ≠ −Z. Scaling to integers preserves the equalities. So this is a non-trivial integer PTE solution of size T, and τ_L ≥ N(2L−2), provided τ_L is the least size of an L-configuration. s₋₁ is not used.

Checks: 352 enumerated configurations; N(k) ≥ k+1 checked for n ≤ 3.

Remarks:
- **τ_L is not defined in the bundle.** I could not check its definition.
- The bound is weaker than T ≥ 2L+2 wherever N(2L−2) = 2L−1. Croot–Mao–Yip p. 1 says P(k,2) = k+1 is known for 2 ≤ k ≤ 9 and k = 11. The text should not suggest the bound is informative there.

Both N(k) bounds re-proved:
- **Lower:** if n ≤ k, Newton's identities force the two multisets to be equal.
- **Upper:** pigeonhole. There are C(M,n) subsets of [1,M], and at most n^k M^{k(k+1)/2} power-sum vectors. These are exceeded for n = k(k+1)/2 + 1 and large M. Cancel common elements afterwards.

## PS.3 Proposition 2.3 — NONE

**(a).** |A| = 2L−1 and e_k = 0 for odd k ≤ 2L−3 (Fact A). So p_A(x) = x·q(x²) − E, with E = e_{2L−1} ≠ 0. Compare V(p_A) with V(p_A(−x)):
- The odd-degree coefficients (1, e₂, e₄, …, e_{2L−2}) are the same in both. Each has w ≤ L−1 sign changes.
- The last step, to −E, changes sign in exactly one of the two.

So 2L−1 = P + N ≤ 2w + 1. This forces w = L−1: e₂, …, e_{2L−2} are all nonzero and alternate. In particular s₋₁(A) = e_{2L−2}/e_{2L−1} ≠ 0. Also P = V(p_A) and N = V(p_A(−x)), so ι(A) = sgn(e_{2L−2}·E) = sgn s₋₁(A).

The "no pair" hypothesis is implied. If {a,−a} ⊂ A, the remaining 2L−3 elements have vanishing odd sums up to 2L−3. By Fact B, this forces 0 ∈ A.

**(b).** s_{−1}(A ⊎ λB) = s₋₁(A) + s₋₁(B)/λ = 0. The odd sums vanish. The size 4L−2 is even.

ι(λB) = sgn(λ)·ι(B), and sgn λ = −sgn s₋₁(A)·sgn s₋₁(B). Using (a):

ι(A) + ι(λB) = sgn s₋₁(A) − sgn s₋₁(A) = 0.

Cancelling a ± pair removes one positive and one negative element. It also preserves the odd sums, s₋₁ and the parity. So the result is empty or an L-configuration with ι = 0. It is empty exactly when λB = −A.

**(c).** Follows from Theorem 3.1 (below).

**Hunt.** My own exhaustive searches: A = X ⊎ −Y, every split (|X|,|Y|).

| L | \|A\| | entries | sets found (both signs) |
|---|---|---|---|
| 2 | 3 | ≤ 60 | 1800 |
| 3 | 5 | ≤ 40 | 58 |
| 4 | 7 | ≤ 60 | 4, i.e. two sets up to sign: (−55,−40,−30,6,19,49,51) and the centred Escott set |

Across all three searches:
- 0 sets with an internal pair;
- ι = ±1 always, equal to sgn s₋₁;
- e_{2L−2} ≠ 0 with alternation, every time.

The fetched Escott solution (Chen survey p. 12), centred, was re-verified.

(b) was run on 4040, 3404 and 24 pairs for L = 2, 3, 4. Self-pairs and pairs with B = −3A gave empty results, as predicted. 0 partial cancellations. For L = 2 a partial cancellation is impossible, since 4L−2−2 < 2L+2. The sign of λ was checked on every pair. Every nonempty result is an L-configuration with ι = 0 and size ≥ 2L+2.

## PS.4 Theorem 3.1 — MINOR

**Proof.** k0 is even in both parities. So bullet 1 for A, together with bullet 2, gives bullet 1 for B. The only differing coefficient is that of x^{m−k0}, so p_A − p_B = κx^{m−k0} with κ = e_{k0}(A) − e_{k0}(B). κ ≠ 0 because A ≠ B. A and B are the fibres of p_A/x^{m−k0} over 0 and κ.

Let c be the single free odd coefficient: c = e_{m−1} for m even, c = e_m for m odd. Write p_A = G + (κ/2)x^{m−k0} ∓ c·x^{ε}. Then p_Z(x) = p_A(x)·(−1)^m p_B(−x) is a difference of squares. Its odd part is exactly ±cκx³ (sympy, generic coefficients, m = 4..10). Hence:
- e_k(Z) = 0 for every odd k ≠ 2m−3;
- by Fact A, s_j(Z) = 0 for odd j ≤ 2m−5 = 2(m−1)−3;
- s₋₁(Z) = 0;
- s_{2m−3}(Z) = ±(2m−3)cκ.

**Cancellation.**
- A ∩ B = ∅: a common root forces κx^{m−k0} = 0.
- An internal pair {z,−z} ⊂ A: for m even, p_A(z) − p_A(−z) = −2cz, so this forces c = 0; for m odd, p_A(z) + p_A(−z) = −2e_m ≠ 0, so it is impossible.
- Hence: for m odd, Z never cancels. For m even, Z cancels only when c = 0. Then A and B are symmetric and Z cancels completely, e.g. A = {±1,±2}, B = {±½,±4}.
- So a nonempty Z has size 2m and shares exactly m−1 coefficients.

**ι = 0.**
- **m odd:** this is Proposition 2.3(b) with λ = −1, since s₋₁(A) = s₋₁(B).
- **m even:** Descartes on p_A = E(x²) − cx, as in (a), forces e₂, …, e_{m−2} to be nonzero and alternating. ι(A) is then determined by sgn e_{m−2}, sgn c and sgn e_m. All three are equal for B, because sgn e_{m−2}(B) is forced to the same value (−1)^{m/2−1}. So ι(A) = ι(B), and ι(A) = ±2 does occur (see the hunt).

**Hunt.** Exhaustive boxes:

| m | entries | nonempty pairs | empty (symmetric) pairs | other pairs |
|---|---|---|---|---|
| 4 | ≤ 40 | 4 | 457 | — |
| 5 | ≤ 150 | — | — | 0 |
| 6 | ≤ 45 | 0 | 22 | — |
| 7 | ≤ 60 | — | — | 0 |
| 8 | ≤ 30 | 0 | 1 | — |

- m = 4 example: A = (−30,−3,5,28), B = (−21,−4,10,15), κ = −468. All four nonempty pairs satisfy every conclusion, including two pairs with ι(A) = ι(B) = ±2.
- A supplementary m = 5 fibre search over integers in [−4000, 4000] found 0 hits. So nonempty examples exist in these boxes only for m = 4. The theorem is conditional, so this is not a defect.
- κ = 0 is excluded by A ≠ B.
- A and B with entries of both signs occur in the m = 4 examples.

**Finding (MINOR).** "Equivalently, ∏_A(x−a) − ∏_B(x−b) = κx^{m−k0}" is equivalent to the second bullet only. With bullet 1 dropped, the conclusion fails.

Counterexample, m = 4: A = (−24,−15,−8,−5), B = (−20,−20,−6,−6). Then p_A − p_B = −9x², but e₁(A) = −52. Z = A ⊎ −B has s₁ = 0 and s₋₁ = 0 but s₃ = −1404, so Z is not a 3-configuration (`check_pencil.txt`, Part 3).

**Wording change.** Replace "Equivalently, $\prod_A(x-a)-\prod_B(x-b)=\kappa\,x^{m-k_0}$, and $A,B$ are two full fibres…" with "Equivalently, $e_k(A)=0$ for every odd $k<r$ and $\prod_A(x-a)-\prod_B(x-b)=\kappa\,x^{m-k_0}$ with $\kappa\ne0$; that is, $A,B$ are two full fibres…".

Optional addition: "For $m$ odd no cancellation occurs. For $m$ even, $Z$ is empty iff $e_{m-1}(A)=0$, and otherwise no cancellation occurs. A nonempty $Z$ shares exactly $m-1$ coefficients, since $s_{2m-3}(Z)=\pm(2m-3)\,e_{r}(A)\,\kappa\neq0$."

## PS.5 Proposition 3.2 — MINOR

**Item 1.** For odd j:

s_j(Z(c)) = Σ_x (x+c)^j − Σ_y (y+c)^j = Σ_{i≤j} C(j,i) c^{j−i} (s_i(X) − s_i(Y)) = 0  for j ≤ k.

The i = 0 term vanishes because |X| = |Y|.

**Item 2.** Positives are {x > −c} ∪ {y < −c}. Negatives are the rest. No element is 0, by the choice of c. Substituting #{x < −c} = n − #{x > −c} gives the formula. For c > −min, every shifted element is positive, so ι = 0. The same holds for c < −max.

f(t) = #{x>t} − #{y>t} is constant between consecutive points of X ∪ Y. If f vanished on every such interval, the two counting functions would agree and X = Y, which is impossible for disjoint nonempty X and Y. So ι ≠ 0 on a whole open c-interval, and that interval contains rationals.

**Item 3.** At c = −x₀ (x₀ ∈ X), ρ has a pole with residue mult(x₀) ≠ 0. The Y-terms do not cancel it, because X ∩ Y = ∅. So ρ ≢ 0.

**Edge cases.**
- n = 1 is impossible for k ≥ 1.
- n = 2, k = 1: 161 solutions.
- Also tested: n = 3, k = 1, 2; n = 4, k = 3 (Prouhet-type).
- Every claim held on all sampled c, including the endpoints of the excluded set.
- ρ can have no zero at all, e.g. X = (0,2), Y = (1,1), where the numerator is the constant 2.
- Zeros of ρ can produce pairs (c = −3/2 for X = (0,3), Y = (1,2)).
- 8 rational zeros, for n = 3, k = 1, gave pair-free 2-configurations with ι ≠ 0.

If n = 0 is allowed, then X = Y = ∅, ρ ≡ 0, and item 2 fails.

**Wording change.** Add "$n\ge1$" (equivalently "$X\ne Y$") to the hypotheses.

## PS.6 statements.tex versus proof.md

**(i) SERIOUS: false as printed.** "two orbifolds in Sig with different signatures share their first L heat coefficients exactly when the cancelled mirror multiset Z=U*⊎(−V*) is an L-configuration".

Counterexample: (2;15) and (0;3,3,5,5). Their mirror multiset Z = (−5,−5,−3,−3,1,15) is a 2-configuration, but the areas are 44/15·2π and 14/15·2π, so not even c₁ agrees. The missing condition is ι(Z) = 2(g'−g). Without it, equal area fails. The proof.md Setting includes this condition ("and |V*|−|U*| = 2(g−g')"). With genus 1 instead of 2, (1;15) ~ (0;3,3,5,5) share 2 coefficients (`check_ps6.txt`).

Replacement: "…share their first $L$ heat coefficients exactly when the cancelled mirror multiset $Z=U^*\uplus(-V^*)$ (paddings with $R(U)=R(V)$) is an \emph{$L$-configuration} and $\iota(Z)=2(g'-g)$." Then change the later sentence to: "Its size is $|Z|=|U^*|+|V^*|$ and its imbalance is $\iota(Z)=\#\{z>0\}-\#\{z<0\}$."

**(ii) MINOR.** In thm:ptedescartes, "equality $|U^*|+|V^*|=2L+2$ forces $\{|U^*|,|V^*|\}=\{L,L+2\}$". "Equality" in the displayed inequality means |U*|+|V*| = 2L+2|g−g'|, and that does not force {L, L+2}. Example: (2;40) and (0;4,4,5,8,10,10) share exactly 2 coefficients, with |U*|+|V*| = 8 = 2L+2|g−g'| and shape {2,6}.

Replacement: "In particular, if $|U^*|+|V^*|=2L+2$ (the least size allowed by Theorem~\ref{thm:sigsep}), then $|g-g'|=1$ and $\{|U^*|,|V^*|\}=\{L,L+2\}$; more generally, equality $|U^*|+|V^*|=2L+2|g-g'|$ holds iff $\min(|U^*|,|V^*|)=L$."

**(iii) MINOR.** In prop:ptebalanced, the "i.e." clause drops 0 ∉ A. A = {−1,0,1} satisfies the printed hypothesis, and Σ a^{−1} is undefined. "every L-configuration A ⊎ λB" ignores cancellation: such an A ⊎ λB may contain pairs.

Replacement: "Let $A$ be an odd ideal symmetric solution of size $2L-1$, i.e.\ $0\notin A$ and $\sum_{a\in A}a^j=0$ for odd $j\le2L-3$ (then $A$ contains no pair $\{a,-a\}$). Then $\sum_{a\in A}a^{-1}\ne0$ and $\#\{a>0\}-\#\{a<0\}=\operatorname{sgn}\sum_{a\in A}a^{-1}$. Consequently, for two such sets $A,B$ and $\lambda=-\sum_B b^{-1}/\sum_A a^{-1}$, the multiset $A\uplus\lambda B$ with all pairs $\{z,-z\}$ removed is empty or an $L$-configuration with $\iota=0$."

**(iv) MINOR / instrument gap.** The citations [BI §1, Props. 2, 3, §6, p. 8] are not verified (CAPTCHA). The mathematics was re-proved. Croot–Mao–Yip (Sept 2026), p. 1, supports the status "no o(k²) bound known". In its terminology P(k,2) = N(k), and the best-known W-bound is k(k+1)/2+1.

Everything else in PS.6 matches the proof.md versions:
- the definition;
- ι = 2(g'−g);
- the Descartes inequality;
- the orbifold inequality.
