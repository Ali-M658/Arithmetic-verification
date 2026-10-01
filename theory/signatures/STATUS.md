# STATUS: the signature (cone count and genus) from heat coefficients

## Verdicts

| task | verdict | statement |
|---|---|---|
| T1 cone count, genus 0 | **PROVED** | the first $\lfloor A/\pi\rfloor+4$ coefficients determine the cone-order multiset, hence $n$, among all hyperbolic genus-0 orbifolds (Theorem T1) |
| T1 "least number that determines $n$" | **PROVED: no uniform number** | for every $k$ there are genus-0 pairs with $n$ and $n+1$ cone points sharing $k$ coefficients (Theorem N(b)) |
| T2 genus / full signature | **PROVED** | the first $\lfloor A/\pi\rfloor+4$ coefficients determine genus and cone orders among all closed orientable hyperbolic 2-orbifolds (Corollary S2); sharp pairwise threshold (Theorem S) |
| T2 "least uniform $L$" | **PROVED: none exists** | for every $L$ there are orbifolds of genus $g'+1$ and $g'$ sharing $L$ coefficients (Theorem N(a)) |
| growth of $f(A)=\max_{\mathrm{Area}\le A}K_{\rm mult}$ | **OPEN** | $\lfloor\log_4(A/2\pi+1)\rfloor+2\le f(A)\le\lfloor A/\pi\rfloor+4$ (Corollary N1) |

All verdicts are given the cited heat input (H1)–(H3) of `proof.md` §1, fetched in `literature.md`.

## T1

**Theorem T1.** Let $\mathcal O$ be hyperbolic of genus 0, with $n$ cone points and area $A$.

- $n\le A/\pi+4$, with equality iff every order is 2.
- The first $\lfloor A/\pi\rfloor+4$ heat coefficients determine the cone-order multiset among
  all hyperbolic genus-0 orbifolds.
- More sharply, $\max(n,n')$ coefficients separate it from any genus-0 orbifold with $n'$ cone
  points.

Every step is verified:

- Padding by order-1 points preserves the area and every coefficient (Lemma 3; exact for
  $l\le15$, and for all $l$ by Lemma 1).
- The padded data equal $\mathcal I_N$, and Theorem A applies.
- Brute force on 27,007 signatures (70,579 equal-area pairs) found no violation.

**Is the bound wasteful?** As a uniform statement in the area, yes and no:

- It cannot be replaced by a constant. Theorem N(b) gives pairs with different cone counts that
  agree to any order, and Corollary N1 shows that the needed number grows at least like
  $\log_4A$.
- On every complete area class computed exactly, the true value is below the bound. On all 525
  classes with $s=-\chi\le\tfrac75$ (33,946 signatures, all genera), the largest $K_{\rm mult}$ in a class is
  at most 3. The bound $\lfloor A/\pi\rfloor+4$ exceeds it by 1 in 4 classes, by 2–4 in 520,
  and by 5 in 1.

**Least number determining $n$.** There is no uniform number.

- Two coefficients do not suffice even among small orbifolds: $(0;5,5,5)$ and $(0;2,2,2,10)$
  share $c_1,c_2$.
- No pair with different cone counts sharing **three** coefficients exists with padded length
  $\le6$ in the ranges searched (orders $\le80$, $40$, $20$ for lengths 4, 5, 6).
- The construction of Theorem N(b) produces one, with 103 vs 104 cone points.

## T2

- **(a) Fetched** (`literature.md` §A). Uçar Thm 4.20(i), eq. (4.35): every smooth-stratum
  coefficient at constant curvature is $\mathrm{vol}(\mathcal O)$ times a constant, for every
  $\nu$. DGGW Thm 4.8 and Def. 4.7 give the stratum structure. That genus enters *only* through
  the area is an inference via Gauss–Bonnet, recorded as such.
- **(b) Reduction.** Pad to a common length and put $X=m\uplus(-m')$. Equal area is
  $\sum_X x^{-1}=2(g-g')$. Equal $C_0,\dots,C_{L-2}$ is then equivalent to
  $\sum_X x^{j}=2(g-g')$ for every odd $j\le2L-3$: the same multiple for every $j$. This is the
  unique solution of the cone-sum system (exact, $L\le16$; all $L$ by Lemma 2).
- **(c) Decision.**
  - Different genera can share any number of coefficients, over the positive reals, over the
    integers $\ge2$, and with hyperbolicity (Theorem N(a), integer and hyperbolic). So no uniform
    $L$ exists.
  - For a given area, $\lfloor A/\pi\rfloor+4$ coefficients determine the full signature
    (Corollary S2).
  - The sharp pairwise form is Theorem S: a collision sharing $L$ needs
    $|U^*|+|V^*|\ge2L+2$. Equality occurs in 28,168 of 97,920 tested pairs.
  - The smallest genus-changing collisions found: $(1;15)\sim(0;3,3,5,5)$ sharing 2, and
    $(1;15,15,15)\sim(0;3,3,5,7,7,21)$ sharing 3.
- **(d) Literature** (`literature.md` §B).
  - Uçar Cor. 4.21(iv) and 4.23: the *full* sequence of heat invariants (with $\kappa$)
    determines the cone orders and $\chi(X_{\mathcal O})$, hence the genus. The cone orders come
    from limits $\nu\to\infty$.
  - Dryden–Strohmaier Thm 1.1 and Prop. 3.3: the full Laplace spectrum determines the cone
    orders "and thus the genus", via the Selberg trace formula.
  - arXiv:2311.00337 (Gittins et al.) says nothing about the genus.
  - No fetched source gives a finite number of heat invariants.

## The precise open question

Determine the growth of $f(A)=\max\{K_{\rm mult}(\mathcal O;\mathrm{Sig}):\mathrm{Area}(\mathcal O)\le A\}$.
Equivalently, for the genus, determine
$$T_L=\min\bigl(|U|+|V|\bigr)$$
over disjoint multisets $U,V$ of positive integers with $|V|-|U|$ nonzero and even, $R(U)=R(V)$,
and $P_j(U)=P_j(V)$ for odd $j\le2L-3$.

- Known: $2L+2\le T_L\le2^{2L-1}$, $T_2=6$, $T_3\in\{8,10\}$.
- Is $T_L=O(L)$? An odd-power Prouhet–Tarry–Escott problem with a reciprocal condition.

Also open: the least cone count of a genus-0 pair with different cone counts sharing three
coefficients, and whether the real threshold $|U^*|+|V^*|=2L+2$ is attained for every $L$.

## Reproduction

All scripts are exact (Fraction and integer keys; sympy for symbolic checks), use real asserts,
and exit nonzero on failure. Run them from this directory with
`/opt/homebrew/Caskroom/miniforge/base/bin/python3` (sympy 1.14). Transcripts are in `output/`.

| script | covers | time |
|---|---|---|
| `heat_structure.py` | Lemmas 1–3 ($l\le15$), T2(b) reduction ($L\le16$), key equivalence | ~4 s |
| `genus.py` | Theorem N(a) for $L\le6$, collision searches, Theorem S on 97,920 pairs | ~3.5 min |
| `cone_count.py` | T1 by brute force, different-$n$ searches, Theorem N(b) for $k\le3$ | ~35 s |
| `area_classes.py` | exact $K_{\rm mult}$, $K_n$, $K_g$ on complete area classes, $s\le7/5$ | ~50 s |

Adversarial review: `attack-log.md`.
