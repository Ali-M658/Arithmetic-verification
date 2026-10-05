# How much of a hyperbolic orbifold does heat hear? The Prouhet–Tarry–Escott side of the signature problem

This file continues `theory/signatures/proof.md`, cited below as **[Sig]**. It answers the
question left open in [Sig] §7: how fast does

$$f(A)=\max\{K_{\rm mult}(\mathcal O;\mathrm{Sig}):\operatorname{Area}(\mathcal O)\le A\}$$

grow? [Sig] proved $\lfloor\log_4(A/2\pi+1)\rfloor+2\le f(A)\le\lfloor A/\pi\rfloor+4$.

## 0. Results in one place

1. **Polynomial lower bound (Theorem 4.1).** For $A\ge8\pi$,
   $$f(A)\ \ge\ \Bigl\lfloor\sqrt{\tfrac13\bigl(\tfrac{A}{2\pi}-1\bigr)}\Bigr\rfloor+2 .$$
   This replaces the logarithm of [Sig] Cor. N1 by a square root. The same order holds for the
   genus alone and for the cone count alone in genus 0 (Theorem 4.3).
2. **The exponent is a Prouhet–Tarry–Escott exponent (Theorem 4.2).** Let $N(k)$ be the least
   size of a nontrivial PTE solution of degree $k$ (Borwein–Ingalls). For $0<\alpha\le1$,
   $$f(A)\ge cA^{\alpha}\ \text{for all large }A\iff N(k)\le Ck^{1/\alpha}\ \text{for all }k .$$
   In particular **$f(A)=\Theta(A)$ if and only if $N(k)=O(k)$**. The best known bounds on
   $N(k)$ are quadratic: $\frac12k(k+1)+1$ by pigeonhole, and the slightly smaller
   $\frac12(k^2-3)$, $\frac12(k^2-4)$ of Wright and Melzak. Any quadratic bound gives the
   exponent $\frac12$ above. Any exponent above
   $\frac12$ would answer the open problem $N(k)=o(k^2)$ of Borwein–Ingalls (1994, §6, Q3) in a
   strong form.
3. **Sharper shape bound (Theorem 2.1).** If orbifolds of genera $g\ne g'$ share $L$ heat
   coefficients, then $|U^*|+|V^*|\ge2L+2|g-g'|$. A genus collision of the least possible size
   $2L+2$ has shape $\{|U^*|,|V^*|\}=\{L,L+2\}$.
4. **Why the classical symmetric solutions never change the genus (Proposition 2.3).** Pairs
   of odd ideal symmetric PTE solutions, and the "pencil" solutions of Theorem 3.1, always give
   *balanced* configurations: equal genus. Genus collisions need asymmetric (shifted)
   solutions.
5. **Explicit witnesses (§5).** Pairs sharing exactly $L$ coefficients, verified with the actual
   cone coefficients:

   | $L$ | least area found, any pair: Area$/2\pi$ | genus pair: $\lvert U^*\rvert+\lvert V^*\rvert$ | genus 0, cone counts $n$ vs $n'$ | Thue–Morse bound on Area$/2\pi$ |
   |---|---|---|---|---|
   | 2 | $1/4$ | 6 | 3 vs 4 | 3 |
   | 3 | $22/15$ | 10 | 7 vs 8 | 15 |
   | 4 | $\approx5.000$ | 16 | 11 vs 12 | 63 |
   | 5 | $\approx7.000$ | 20 | 22 vs 23 | 255 |
   | 6 | $\approx10.000$ | 26 | 29 vs 30 | 1023 |
   | 7 | $\approx18.000$ | 40 | 35 vs 36 | 4095 |

6. **$T_3$ (§6).** $T_3\in\{8,10\}$ is not decided. An exhaustive exact search excludes every
   size-8 genus collision whose 5-element side, made primitive, has entries $\le220$. The
   collision must have shape $(3,5)$ (Theorem 2.1). Real solutions of that shape exist in
   abundance, so the obstruction, if there is one, is arithmetic.

## 1. Setting

Throughout, (H1)–(H3) of [Sig] §1 are assumed, as there. Two closed orientable hyperbolic
2-orbifolds with signatures $\sigma=(g;m)\ne\sigma'=(g';m')$ share their first $L$ heat
coefficients if and only if the following holds ([Sig] Lemma 4, Theorem S). Pad $m$ and $m'$
by 1s to $U$ and $V$ with $R(U)=R(V)$, and cancel common elements to get $U^*,V^*$. Then the
multiset $Z=U^*\uplus(-V^*)$ satisfies the definition below, and $|V^*|-|U^*|=2(g-g')$.

**Definition 1.1.** An *$L$-configuration* is a nonempty finite multiset $Z$ of nonzero
rationals such that:

- $s_j(Z):=\sum_{z\in Z}z^j=0$ for odd $1\le j\le2L-3$;
- $s_{-1}(Z)=0$;
- $Z$ contains no pair $\{z,-z\}$;
- $|Z|$ is even (equivalently, $\iota(Z)$ below is even).

The last condition is automatic for configurations coming from orbifold pairs, since
$|U^*|+|V^*|\equiv|V^*|-|U^*|=2(g-g')$. Without it there are odd examples, e.g.
$\{-24,-18,-8,5,45\}$ has $s_1=s_{-1}=0$; they correspond to no orbifold pair.

Write $T=|Z|$ for its *size* and $\iota(Z)=\#\{z>0\}-\#\{z<0\}$ for its *imbalance*.

**Lemma 1.2 (dictionary).**

1. Configurations are invariant under $Z\mapsto\lambda Z$ for $\lambda\in\mathbb Q^\times$. This
   preserves $T$, and multiplies $\iota$ by $\operatorname{sgn}\lambda$.
2. Let $Z$ be an $L$-configuration scaled to primitive integers. Put $U=Z_{>0}$ and
   $V=-Z_{<0}$, and let $g-g'=-\iota/2$ with the smaller genus chosen least such that both are
   hyperbolic. Then $(g;U\setminus\{1\})$ and $(g';V\setminus\{1\})$ have equal area and
   distinct signatures, and they share at least $L$ heat coefficients. They share exactly $L$
   iff $s_{2L-1}(Z)\ne0$.
3. The pair is genus-changing iff $\iota\ne0$. If $\iota=0$, the pair has equal genus, and the
   cone counts differ iff $\pm1\in Z$ (a padding point).
4. $T$ is even and $T\ge2L+2$.
5. Area. If $\iota\ne0$, then $\operatorname{Area}<2\pi T$. If $\iota=0$ and the genus-0
   realisation is hyperbolic, then $\operatorname{Area}/2\pi=-2+\sum_{v\in V}(1-1/v)<T/2-2$.

*Proof.*

1. Every defining equation is homogeneous.
2. This is the converse half of [Sig] Lemma 4. The signatures differ because $U\neq V$ (they
   are disjoint and not both empty) and a 1 is only padding. Exactness: by [Sig] Lemma 2 the
   $(L+1)$-st coefficient agrees iff $P_{2L-1}(U)=P_{2L-1}(V)$, i.e. iff $s_{2L-1}(Z)=0$.
3. Follows from $|V|-|U|=-\iota$.
4. This is [Sig] Theorem S.
5. Let $W\in\{U,V\}$ be the side with the smaller genus $g_0$ (the side with more elements; either
   side if $\iota=0$). The area is $2\pi(2g_0-2+\sum_{w\in W}(1-1/w))$. If $g_0=0$ is hyperbolic,
   this is $<2\pi(|W|-2)$. Otherwise $g_0=1$, and the area is at most $4\pi$. In both cases
   $|W|\le T$, and $|W|=T/2$ when $\iota=0$. $\square$

**Definition 1.3.** For $L\ge2$:

- $\tau_L$ is the least size of an $L$-configuration;
- $T_L$ is the least size with $\iota\ne0$ (the $T_L$ of [Sig] §7);
- $T^{\rm cone}_L$ is the least size of an $L$-configuration with $\iota=0$ whose primitive
  integral form contains $\pm1$ and whose genus-0 realisation is hyperbolic.

Then $2L+2\le\tau_L\le T_L$ and $\tau_L\le T^{\rm cone}_L$.

**PTE notation** (Borwein–Ingalls 1994, `sources/NOTES.md` §1).

- $[A]=_k[B]$ means equal power sums $P_j$ for $1\le j\le k$, for distinct multisets $A,B$ of
  integers of a common size $n$.
- $N(k)$ is the least such $n$.
- $N(k)\ge k+1$ (their Prop. 2), and $N(k)\le\frac12k(k+1)+1$ (their Prop. 3, by pigeonhole).
- $N$ is nondecreasing, because a solution of degree $k+1$ is one of degree $k$.

**Definition 1.4.** $N_{\rm odd}(L)$ is the least $n$ such that two distinct $n$-multisets of
*positive* integers have equal $P_j$ for every odd $j\le2L-3$.

**Lemma 1.5.**

1. $N_{\rm odd}(L)\le N(2L-3)$.
2. $N_{\rm odd}(L)\le(L-1)^2+1$.
3. $N_{\rm odd}(L)=L$ for $3\le L\le6$.

*Proof.*

1. Translate a PTE solution of degree $2L-3$ into the positive integers. Translation preserves
   $=_k$.
2. There are at least $M^n/n!$ multisets of size $n$ from $\{1,\dots,M\}$. Their odd power-sum
   vectors $(P_1,P_3,\dots,P_{2L-3})$ take at most $\prod_{j}nM^j=n^{L-1}M^{(L-1)^2}$ values.
   With $n=(L-1)^2+1$ and $M>n!\,n^{L-1}$, two of them collide.
3. The lower bound: for $L\ge2$, $N_{\rm odd}(L)\ge L$. Equal $P_j$ for odd $j\le2L-3$
   between multisets $X\ne Y$ of size $n\le L-1$ would make $X\uplus(-Y)$ a multiset of size
   $\le2L-2$ with vanishing odd power sums up to $2L-3$. Its odd elementary symmetric
   functions then vanish ([Sig] Lemma 5), so it is symmetric, and $X=Y$. The upper bound:
   size-$L$ examples for $L=3,4,5,6$ are in Chen's survey (`sources/NOTES.md` §7: A.1.6,
   A.1.17, A.1.26, A.1.33), re-verified exactly in `witnesses.py`. $\square$

## 2. Lower bounds and structure

**Theorem 2.1 (Descartes bound).** Every $L$-configuration satisfies $|\iota(Z)|\le T-2L$. In
particular:

1. Two orbifolds of genera $g\ne g'$ sharing $L$ heat coefficients have
   $|U^*|+|V^*|\ge2L+2|g-g'|$.
2. A genus-changing configuration of size $2L+2$ has $\iota=\pm2$, i.e. shape
   $\{|U^*|,|V^*|\}=\{L,L+2\}$. An $L$-configuration of size $2L+2$ has $\iota\in\{0,\pm2\}$.

*Proof.* Let $Q(x)=\prod_{z\in Z}(x-z)=\sum_k(-1)^ke_kx^{T-k}$, a real polynomial of even
degree $T$ with all roots real and nonzero.

- By [Sig] Lemma 5, $e_k=0$ for odd $k\le2L-3$. Also $e_{T-1}=e_T\,s_{-1}(Z)=0$.
- Since $T$ is even, the coefficient of $x^{T-k}$ has odd degree iff $k$ is odd. So at most
  the $(T-2L)/2$ coefficients with odd $k\in[2L-1,T-3]$ of odd degree are nonzero.

Let $V^\pm$ count the sign changes in the coefficient sequences of $Q(x)$ and $Q(-x)$. Take two
consecutive nonzero coefficients, of degrees $d>d'$:

- if $d-d'$ is even, they produce a change in both sequences or in neither (contributing 0 or
  $2\le d-d'$ to $V^++V^-$, and 0 to $V^+-V^-$);
- if $d-d'$ is odd, they produce a change in exactly one sequence (contributing $1\le d-d'$ to
  $V^++V^-$, and $\pm1$ to $V^+-V^-$).

Hence $V^++V^-\le T$, since the constant term $e_T\neq0$. By Descartes' rule,
$\#\{z>0\}\le V^+$ and $\#\{z<0\}\le V^-$. The two counts add up to $T\ge V^++V^-$, so both
are equalities, and $\iota=V^+-V^-$.

An odd gap joins a coefficient of odd degree to one of even degree. Each nonzero odd-degree
coefficient ends at most two consecutive pairs. Therefore
$|\iota|\le2\cdot\frac{T-2L}2=T-2L$.

For (1): $\iota=2(g'-g)$ by Lemma 1.2. For (2): $|\iota|\le2$, and $\iota$ is even. $\square$

**Proposition 2.2 (PTE lower bound).** An $L$-configuration of size $T$ gives the PTE solution
$[Z]=_{2L-2}[-Z]$ of size $T$. Hence $\tau_L\ge N(2L-2)$.

*Proof.* Scale $Z$ to integers. $Z\ne-Z$ because $Z$ has no pair $\{z,-z\}$ and is nonempty.
For odd $j\le2L-3$, $P_j(Z)-P_j(-Z)=2s_j(Z)=0$. For even $j$ the two sums are equal anyway.
$\square$

This is Chen Shuwen's lifting of equal odd power sums to a PTE solution (`sources/NOTES.md`
§8, Theorem 3), applied to $Z$.

**Proposition 2.3 (symmetric constructions are balanced).**

(a) Let $A$ be an *odd ideal symmetric* PTE solution in the sense of Borwein–Ingalls (p. 8):
$|A|=2L-1$, $s_j(A)=0$ for odd $j\le2L-3$, $0\notin A$, and no pair $\{a,-a\}$. Then
$s_{-1}(A)\ne0$ and $\iota(A)=\operatorname{sgn}s_{-1}(A)$.

(b) For two such sets $A,B$, let $\lambda=-s_{-1}(B)/s_{-1}(A)$, so that
$s_{-1}(A\uplus\lambda B)=s_{-1}(A)+s_{-1}(B)/\lambda=0$. Then $Z=A\uplus\lambda B$ is, after
cancellation, either empty or an $L$-configuration with $\iota(Z)=0$.

(c) The pencil configurations of Theorem 3.1 have $\iota=0$.

*Proof.* (a) Put $n=2L-1$ and $Q_A(x)=\prod_{a\in A}(x-a)$. Its odd-index $e_k$ vanish for
$k\le n-2$ ([Sig] Lemma 5). Hence
$$Q_A(x)=\Bigl(\sum_{i=0}^{L-1}e_{2i}x^{n-2i}\Bigr)-e_n,$$
an odd polynomial minus a constant, with $e_n=\prod a\ne0$. All $n$ roots are real and nonzero,
so the proof of Theorem 2.1 applies: the gap sum $V^++V^-$ equals $n$. That forces:

- every gap to be $\le2$, so every $e_{2i}\ne0$, $0\le2i\le n-1$;
- every gap of 2 to carry a sign change in both sequences.

So $V^+=(L-1)+\delta$, where $\delta=1$ iff the last two coefficients, $e_{n-1}$ (at $x^1$) and
$-e_n$ (at $x^0$), have opposite signs, i.e. iff $s_{-1}(A)=e_{n-1}/e_n>0$. Since $e_{n-1}\ne0$,
$s_{-1}(A)\ne0$, and $\iota(A)=2V^+-n=2\delta-1=\operatorname{sgn}s_{-1}(A)$.

(b) $\lambda$ is fixed by $s_{-1}(A)+s_{-1}(B)/\lambda=0$, so
$\operatorname{sgn}\lambda=-\operatorname{sgn}s_{-1}(A)\operatorname{sgn}s_{-1}(B)$. By (a),
$$\iota(\lambda B)=\operatorname{sgn}\lambda\cdot\operatorname{sgn}s_{-1}(B)=-\operatorname{sgn}s_{-1}(A)=-\iota(A).$$
Cancellation preserves $\iota$.

(c) See the end of the proof of Theorem 3.1. $\square$

So the odd ideal symmetric solutions (sizes 3, 5, 7, 9 are known) produce same-genus pairs
only. Two size-$(2L-1)$ sets give balanced configurations of size $4L-2$: genus-0 pairs with
$2L-1$ cone points each sharing $L$ coefficients. For genus collisions one needs the
asymmetric constructions of §3.

## 3. Constructions

**Theorem 3.1 (pencil: ideal balanced configurations).** Let $m\ge4$, put $r=m-1$ and $k_0=m-2$
if $m$ is even, and $r=m$ and $k_0=m-3$ if $m$ is odd. Let $A\ne B$ be $m$-multisets of nonzero
rationals such that:

- $e_k(A)=e_k(B)=0$ for every odd $k<r$;
- $e_k(A)=e_k(B)$ for every $k\ne k_0$.

Equivalently, $\prod_A(x-a)-\prod_B(x-b)=\kappa\,x^{m-k_0}$, and $A,B$ are two full fibres of
the rational function $x\mapsto\prod_A(x-a)/x^{m-k_0}$. Then, if nonempty after cancellation,
$Z=A\uplus(-B)$ is an $(m-1)$-configuration of size $2m=2(m-1)+2$, the least possible, with
$\iota(Z)=0$.

*Proof.* For odd $j$, $s_j$ is an isobaric polynomial of weight $j$ in the $e_k$ (Newton). Each
monomial contains an odd number of odd-index factors. The only odd-index $e_k$ that can be
nonzero is $e_r$. So every monomial involving $e_{k_0}$ has weight $\ge r+k_0=2m-3$, and
$s_j(A)=s_j(B)$ for odd $j\le2m-5=2(m-1)-3$. Also $s_{-1}=e_{m-1}/e_m$ agrees, because
$k_0\notin\{m-1,m\}$. So $Z$ satisfies the moment conditions, and $A\cap B=\emptyset$, since a
common root $x$ would give $\kappa x^{m-k_0}=0$.

After cancelling pairs, the size is either 0 or at least $2(m-1)+2=2m$ by Theorem S, so it is
$2m$ (or $Z$ is empty). Balance:

- $\#A_{>0}$ equals the number of sign changes $V(\prod_A)$, by the equality case in the proof
  of Theorem 2.1.
- $\prod_A$ and $\prod_B$ differ in a single interior coefficient. Changing one coefficient
  alters the number of sign changes by an even amount, since only its two neighbours matter.
- So $\#A_{>0}\equiv\#B_{>0}\pmod2$, and
  $\iota(Z)=\iota(A)-\iota(B)=2(\#A_{>0}-\#B_{>0})\equiv0\pmod4$.
- Theorem 2.1(2) gives $|\iota|\le2$, so $\iota=0$. $\square$

*Instances.* For $m=4$ the hypothesis says that $A,B$ have $e_1=0$ and equal $e_3,e_4$.
`pencil_search.py` finds 25 distinct configurations from 4-sets with entries $\le130$, and 61
with entries $\le220$ (`data/pencil_log.txt`). These include 60 integer sharpness witnesses
for Theorem A at $n=4$ beyond the one recorded in `theory/audibility`. The smallest is
$A=\{-30,-3,5,28\}$, $B=\{-21,-4,10,15\}$, which gives
$\{3,10,15,30\}\sim\{4,5,21,28\}$. That is the $n=4$ witness of `theory/audibility/proof.md`
Theorem C(3) and Chen's type $(-1,1,3)$ entry A.685. So Theorem C(3) at $n=4$ is a pencil
phenomenon.

For $m=5$ the hypothesis asks for two odd symmetric 5-sets with equal $e_4,e_5$. Such a pair
would give a balanced 4-configuration of size 10, i.e. the integer sharpness of Theorem A at
$n=5$, which is open in `theory/audibility`. Among all 1,592 primitive 5-sets with entries
$\le200$, no such pair exists.

**Proposition 3.2 (shift).** Let $[X]=_k[Y]$ with $k\ge2L-3$, $|X|=|Y|=n$, and $X\cap Y=\emptyset$.
For $c\in\mathbb Q\setminus(-X\cup-Y)$ put $Z(c)=(X+c)\uplus(-(Y+c))$.

1. $s_j(Z(c))=0$ for odd $j\le2L-3$.
2. $\iota(Z(c))=2(\#\{x>-c\}-\#\{y>-c\})$. It is $0$ for $c>-\min(X\cup Y)$, and nonzero on
   some open interval of $c$.
3. $\rho(c):=s_{-1}(Z(c))=\sum_x\frac1{x+c}-\sum_y\frac1{y+c}$ is a nonzero rational function of
   $c$.

*Proof.*

1. $P_j(X+c)-P_j(Y+c)$ is a combination of the differences $P_i(X)-P_i(Y)$, $i\le j$.
2. The first formula counts signs. Since $X\ne Y$, their counting functions differ at some
   real $t$, and the difference is constant on an interval around $t$.
3. The poles $-x$ and $-y$ are distinct, since $X\cap Y=\emptyset$. $\square$

**Proposition 3.3 (doubling).** Let $X\ne Y$ be $n$-multisets of positive integers with equal
$P_j$ for odd $j\le2L-3$. Put
$$U=X\uplus2Y\uplus2Y,\qquad V=Y\uplus2X\uplus2X .$$
Then $Z=U\uplus(-V)$, after cancellation, is a balanced $L$-configuration of size $\le6n$.

- If $1\in X\setminus Y$, the pair $(0;U\setminus\{1\})$, $(0;V)$ consists of hyperbolic genus-0
  orbifolds whose cone counts differ by the multiplicity of $1$ in $X$. If $1\in Y\setminus X$,
  exchange the roles of $X$ and $Y$.
- If $1\notin X\cup Y$, the cone counts are equal.

In every case the area is $<2\pi(3n-2)$.

*Proof.* For every $j$, including $j=-1$,
$$s_j(Z)=(1-2^{j+1})\bigl(P_j(X)-P_j(Y)\bigr),$$
which is $0$ for odd $j\le2L-3$ and for $j=-1$. Let $\mu$ be the signed counting measure
$1_X-1_Y\ne0$ and $x^*=\max\operatorname{supp}\mu$. The multiplicity of $2x^*$ in $U-V$ is
$-2\mu(x^*)\ne0$, so $Z\ne\emptyset$ after cancellation.

$V$ contains the $2n$ entries of $2X\uplus2X$, all $\ge2$, so $s(0;V)\ge-2+n>0$ for $n\ge3$.
For $n=2$, $Y$ contains at most one 1: two 1s would force $X=Y$ from $P_1(X)=P_1(Y)=2$. So $V$
has at least 5 entries $\ge2$, and $s(0;V)\ge\frac12$. If $1\in Y\setminus X$, exchange the roles
of $X$ and $Y$. The area bound is Lemma 1.2(5). The 1s are padding. $\square$

The doubling is the identity $1=\frac12+\frac12$, as in the audit's construction for
[Sig] N(b) (`review/audit/signatures/REVIEW.md` P1(f′)). There it was applied to Thue–Morse
blocks. Here it is applied to any equal-odd-power-sum pair, which is what makes the size
polynomial.

**Theorem 3.4 (upper bounds).** For every $L\ge2$:
$$\tau_L\le6N_{\rm odd}(L)\le6(L-1)^2+6,\qquad T_L\le4N(2L-3),\qquad T^{\rm cone}_L\le6N(2L-3).$$
With $N(2L-3)\le\frac12(2L-3)(2L-2)+1=2L^2-5L+4$, all three are $O(L^2)$. The previous bound
was $T_L\le2^{2L-1}$ ([Sig] N(a)).

*Proof.*

- $\tau_L$: Proposition 3.3 with $n=N_{\rm odd}(L)$, then Lemma 1.5.
- $T_L$: take $[X]=_{2L-3}[Y]$ of size $n=N(2L-3)$, with common elements cancelled. By
  Proposition 3.2, choose $c$ with $\iota(Z(c))\ne0$ and $\rho(c)\ne0$, and $c'$ large with
  $\iota(Z(c'))=0$ and $\rho(c')\ne0$. Both are possible because $\rho$ has finitely many zeros.
  Then $Z=Z(c)\uplus\lambda Z(c')$ with $\lambda=-\rho(c')/\rho(c)$ has $s_{-1}=0$ and
  $\iota=\iota(Z(c))\neq0$. So it is nonempty after cancellation, and $T\le4n$.
- $T^{\rm cone}_L$: translate a solution of size $N(2L-3)$ so that its least element is 1, and
  call the side containing 1 $X$. Then apply Proposition 3.3. $\square$

## 4. Growth of $f$

**Theorem 4.1 (square-root lower bound).** For every $L\ge2$ there are two genus-0 hyperbolic
orbifolds with different signatures and area $<2\pi(3N_{\rm odd}(L)-2)\le2\pi(3(L-1)^2+1)$ that
share at least $L$ heat coefficients. Consequently, for $A\ge8\pi$,
$$f(A)\ \ge\ \Bigl\lfloor\sqrt{\tfrac13\bigl(\tfrac{A}{2\pi}-1\bigr)}\Bigr\rfloor+2 .$$

*Proof.* Proposition 3.3 with $n=N_{\rm odd}(L)$ gives the pair. Both members have
$K_{\rm mult}\ge L+1$. Take the largest $L$ with $3(L-1)^2+1\le A/2\pi$. $\square$

`growth.py` checks exactly that this bound is $\ge$ the bound of [Sig] Cor. N1 for every
$A/2\pi\in[4,10^6]$, interval by interval between the breakpoints of both sides. It is
strictly larger exactly on $[13,15)$ and on $[28,10^6]$; the two agree on $[4,13)$ and $[15,28)$. Asymptotically the old bound is $\sim\log_4A$ and the new one is
$\sim\sqrt{A/6\pi}$.

**Theorem 4.2 (the exponent of $f$ is a PTE exponent).**

(a) If $f(A)\ge L+1$, then $N(2L-2)\le2\lfloor A/\pi\rfloor+8$.

(b) If $N(k)\le Ck^\beta$ for all $k\ge1$, then $f(A)\ge\frac12(A/6\pi C)^{1/\beta}$ for all
$A\ge8\pi$.

(c) For $0<\alpha\le1$: $f(A)\ge cA^\alpha$ for all large $A$ (some $c>0$) if and only if
$N(k)\le Ck^{1/\alpha}$ for all $k$ (some $C$). In particular $f(A)=\Theta(A)$ iff
$N(k)=O(k)$.

*Proof.*

(a) $f(A)\ge L+1$ means some $\mathcal O$ of area $\le A$ has a partner $\mathcal O'$ with a
different signature sharing $L$ coefficients. Its configuration has size
$T\le|U|+|V|=2\max(n+g-g',n'+g'-g)\le2\lfloor A/\pi\rfloor+8$, by [Sig] (4.3) and the proof of
S2. Proposition 2.2 then gives $N(2L-2)\le T$.

(b) $N_{\rm odd}(L)\le N(2L-3)\le C(2L)^\beta$ (Lemma 1.5). By Theorem 4.1, $f(A)\ge L+1$ as
soon as $6\pi C(2L)^\beta\le A$, i.e. for $L=\lfloor\frac12(A/6\pi C)^{1/\beta}\rfloor$ when this is
$\ge2$. Otherwise $\frac12(A/6\pi C)^{1/\beta}<2<3\le f(A)$ for $A\ge8\pi$.

(c) "⇐" is (b). "⇒": given $k$, let $L=\lceil k/2\rceil+1$, so that $2L-2\ge k$. Take
$A=((L+1)/c)^{1/\alpha}$, which is in the range of the hypothesis once $k$ is large; small $k$
are absorbed into $C$. Then (a) and monotonicity give
$N(k)\le N(2L-2)\le2A/\pi+8=O(L^{1/\alpha})=O(k^{1/\alpha})$.

Since $f(A)\le\lfloor A/\pi\rfloor+4$, $\alpha\le1$ is the only meaningful range. $\square$

*Consequence for the paper.* All known bounds on $N(k)$ are quadratic: Borwein–Ingalls
Prop. 3 gives $\frac12k(k+1)+1$, and the "slightly stronger" bounds of Wright and Melzak quoted
there give $\frac12(k^2-3)$, $\frac12(k^2-4)$. So the exponent $\frac12$ in Theorem 4.1 is the
best that (c) can give from current knowledge. An exponent $>\frac12$
would prove $N(k)=O(k^{2-\varepsilon})$, which is stronger than the open problem
"$N(k)=o(k^2)$" (Borwein–Ingalls §6, Q3, "No progress … for many years"). Linear growth of $f$
is equivalent to $N(k)=O(k)$. That is weaker than the ideal-solution conjecture
$N(k)=k+1$, which is open (sizes $\le10$ and $12$ are known, 11 is open).

**Theorem 4.3 (genus alone, cone count alone).**

- Let $f_g(A)$ be the largest number of coefficients needed to determine the *genus* of an
  orbifold of area $\le A$, and $f_n(A)$ the analogous number for the *cone count* among
  genus-0 orbifolds.
- Then $f_g(A)\ge L+1$ whenever $A\ge8\pi N(2L-3)$, and $f_n(A)\ge L+1$ whenever
  $A\ge2\pi(3N(2L-3)-2)$. Both are therefore $\ge c\sqrt A$. Both are
  $\le\lfloor A/\pi\rfloor+4$ ([Sig] S2, T1).
- Theorem 4.2(c) holds verbatim for $f_g$ and for $f_n$. "⇐": by the two thresholds just
  stated. "⇒": a genus or cone-count collision is in particular a collision of signatures, so
  $f_g\le f$ and $f_n\le f$, and Theorem 4.2(a) applies.

*Proof.* Theorem 3.4 and Lemma 1.2(5). For $f_g$, $T\le4N(2L-3)$ gives area $<2\pi T$. For
$f_n$, Proposition 3.3 gives area $<2\pi(3N-2)$. $\square$

## 5. Explicit witnesses

`witnesses.py` rebuilds every pair from a recipe, checks it exactly as an $L$-configuration,
realises it (Lemma 1.2), and recomputes the number of shared heat coefficients from the actual
cone coefficients $b_l$ of Uçar (via `theory/signatures/sig_common.shared`). Every pair below
shares **exactly** $L$. The data are in `data/witnesses.json` and the transcript is
`output/witnesses.txt`. All PTE inputs are the fetched solutions listed in `LITERATURE.md`:

- Borwein–Ingalls p. 9;
- BLP 2003 p. 2069;
- CMSV 2023 (5);
- Chen's odd-power equalities.

**Genus collisions** ($\iota=2$; genus 1 versus genus 0):

| $L$ | $T$ | cone points (genus 0 / genus 1) | Area$/2\pi$ | recipe |
|---|---|---|---|---|
| 2 | 6 | 4 / 1 | $14/15$ | $(1;15)\sim(0;3,3,5,5)$ [Sig] |
| 3 | 10 | 6 / 3 | $14/5$ | $(1;15,15,15)\sim(0;3,3,5,7,7,21)$ [Sig] |
| 4 | 16 | 9 / 7 | $6.9999$ | size-6 solution $\{\pm7,\pm11,\pm18\}$, $\{\pm3,\pm14,\pm17\}$ (own enumeration) shifted by $c=-11/2$, plus scaled $[1,13,17,23]=[3,9,21,21]$ |
| 5 | 20 | 11 / 9 | $9.0000$ | size-8 solution shifted by $-9/2$, plus scaled $[3,19,37,51,53]=[9,11,43,45,55]$ |
| 6 | 26 | 14 / 12 | $12.000$ | size-10 BLP solution shifted, plus scaled $(1,3,\dots,9)$ equality of Chen (2000) |
| 7 | 40 | 21 / 19 | $19.000$ | size-12 solution shifted by $-27$, plus its balanced shift by $-27/2$ |

The shifts are half-sums $-(a+b)/2$ of two elements of one side of a symmetric solution. They
cancel the pair $a+c$, $b+c=-(a+c)$, so $T$ is smaller than $4n$. For example, at $L=5$ three
pairs cancel and $26\to20$. At $L=4$ two pairs cancel inside the shifted piece, leaving an
imbalanced 8-element set of shape $(3,5)$ with $s_1=s_3=s_5=0$ (but $s_{-1}\ne0$); one scaled
balanced piece of size 8 then gives $16$. The fetched size-6 solution gives only $18$; the
smaller one comes from a search over all 19,450 symmetric size-6 solutions with entries
$\le400$ against all 25 odd-power equalities $(1,3,5)$ with entries $\le60$, in which $16$ was
the minimum.

**Balanced, equal cone counts** ($\iota=0$, genus 0 on both sides):

| $L$ | $T$ | $n$ | Area$/2\pi$ | recipe |
|---|---|---|---|---|
| 2 | 6 | 3 | $1/4$ | $(0;2,8,8)\sim(0;3,3,12)$ |
| 3 | 8 | 4 | $22/15$ | $(0;3,10,15,30)\sim(0;4,5,21,28)$, a pencil point |
| 4 | 14 | 7 | $\approx5.000$ | two odd ideal symmetric 7-sets (Prop. 2.3(b)) |
| 5 | 18 | 9 | $\approx7.000$ | Letac's two 9-sets (1942; CMSV p. 2, B–I p. 9) |
| 6 | 24 | 12 | $\approx10.000$ | two $(1,3,\dots,9)$ equalities of Wróblewski (2009), from Chen's survey A.1.33 |
| 7 | 40 | 20 | $\approx18.000$ | two balanced shifts of the size-12 solution |

**Genus 0, different cone counts:**

| $L$ | $T$ | $n$ vs $n'$ | Area$/2\pi$ | recipe |
|---|---|---|---|---|
| 2 | 8 | 3 vs 4 | $2/5$ | $(0;5,5,5)\sim(0;2,2,2,10)$ [Sig] |
| 3 | 16 | 7 vs 8 | $113/30$ | doubling of $[1,5,5]=[2,3,6]$: $(0;4,4,5,5,6,12,12)\sim(0;2,2,2,3,10,10,10,10)$ |
| 4 | 24 | 11 vs 12 | $2651846/320229$ | doubling of $[1,13,17,23]=[3,9,21,21]$ |
| 5 | 46 | 22 vs 23 | $\approx18.60$ | size-8 solution translated to start at 1, doubled |
| 6 | 60 | 29 vs 30 | $\approx26.56$ | size-10 BLP solution translated, doubled |
| 7 | 72 | 35 vs 36 | $\approx32.31$ | size-12 solution translated, doubled |

These replace:

- for the genus, the Thue–Morse pairs with $4^{L-1}\mp1$ cone points ([Sig] N(a): 63/65,
  255/257, 1023/1025, …);
- for the cone count, the pairs 103 vs 104 ([Sig] N(b), $L=3$) and $3\cdot2^{2L-3}-1$ vs
  $3\cdot2^{2L-3}$ (audit: 23 vs 24 at $L=3$, 95 vs 96 at $L=4$, …).

**Improved lower bounds on $f$ in the covered range.** Let $A_L$ be the least area in the
tables above among pairs sharing $L$ coefficients. Then $f(A)\ge L+1$ for $A\ge A_L$:

| $f(A)\ge$ | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| for $A/2\pi\ge$ (new) | $1/4$ | $22/15$ | $5.000$ | $7.000$ | $10.000$ | $18.000$ |
| for $A/2\pi\ge$ ([Sig] N1) | 3 | 15 | 63 | 255 | 1023 | 4095 |

The exact values of $A_L$ are in `data/witnesses.json`. The $\approx$ values lie just below
the integers shown, e.g. $A_4/2\pi=4.99999\ldots$, so "$\ge5.000$" is a safe rounding up.

Over this range the best pairs have Area$/2\pi\approx T/2-2$ with $T\le4L-2$ for $L\le5$. So
for $A/2\pi\le18$, $f$ grows at least linearly: $f(A)\ge L+1$ at
$A/2\pi\approx2L-3$ for $L\le5$.

## 6. $T_3$

**Status: $T_3\in\{8,10\}$, undecided.** What is proved and what was searched:

1. *Shape.* A size-8 genus collision sharing 3 coefficients has shape $(|U^*|,|V^*|)=(3,5)$ up
   to swapping (Theorem 2.1).
2. *The search* (`search_T3.c`, driver `search_T3.sh`, exact verifier `search_T3_verify.py`,
   control `search_T3_control.py`, log `data/T3_search_log.txt`). Write the 5-element side
   $V=\{v_1\le\dots\le v_5\}$ as positive integers with $\gcd=1$. Given $V$, the three
   elements of $U$ are the roots of
   $$Kt^3-KSt^2+M R_n t-M R_d,\qquad K=3(R_d-SR_n),\ M=C-S^3,$$
   where $S=\sum v$, $C=\sum v^3$ and $R_n/R_d=\sum1/v$ (eliminate $e_2=Re_3$ and $e_3$ from the
   three conditions). A rational root $p/q$ has $q\mid K'$, the leading coefficient after
   removing the content, so $K'r$ must be an integer.
   - *Decision rule.* Floating point only rejects what it can reject with certainty:
     - "one real root" requires the discriminant to exceed four times its error bound;
     - otherwise the roots are enclosed in Smith's inclusion disks (radius
       $3|f(r_i)|/\prod_{j\ne i}|r_i-r_j|$, doubled, with evaluation and coefficient errors
       bounded by $64\varepsilon_{\rm mach}$), which must be pairwise disjoint;
     - a root is excluded only if $K'r_i$ is farther from every integer than $K'$ times the
       radius.
     Near-zero discriminants (possible repeated roots, which split over $\mathbb Q$
     automatically), overlapping disks and too-large radii are routed to the exact check.
   - *Exact check.* Every routed or surviving $V$ is verified exactly (sympy factorisation of the
     integer cubic).
   - *Control.* 53,324 planted genuine rational $U$ (integral, non-integral with $K'>1$,
     near-double, exactly repeated; `output/search_T3_control.txt`): **no false negative**.
     The counters agree exactly with an independent sympy enumeration for $v_5\le30$, and with
     the adversarial referee's own exact search for $v_5\le45$ (`attack/a09_T3.txt`).
   - *History.* The first version of the filter assumed 80-bit `long double`. On this machine
     (arm64) `long double` is IEEE double, and the referee showed that this filter rejected 34 of
     27,900 planted genuine rational $U$ with clustered roots (`attack-log.md`, item 9). The
     search was therefore rerun from scratch with the certified rule above; only the rerun is
     relied on.
   - *Result:* every $V$ with $v_5\le220$ tested: 4,325,115,770 primitive 5-sides; 29,494,902
     cubics with three positive real roots; 220,428 candidates (220,352 undecided by the certified
     rule), all verified exactly. **No size-8 genus collision** (`data/T3_search_log.txt`). A collision of shape $(3,5)$ is excluded whenever its 5-element
     side, scaled to primitive integers, has entries $\le220$. Its 3-element side is
     unrestricted (any rationals).
3. *Real solutions of shape $(3,5)$ exist in abundance* (`real_shapes.py`). About 35% of
   log-normally sampled real $V$ give three positive real roots. For integral $V$ with
   $v_5\le220$ the proportion is about 0.7% (counters in `data/T3_search_log.txt`). So no sign or real obstruction rules out
   $T_3=8$. In contrast, shapes $(2,6)$ and $(1,7)$ have no real solutions, as Theorem 2.1
   predicts.
4. *Every structured family tried yields only balanced size-8 objects:*
   - pencils (Theorem 3.1, Prop. 2.3(c));
   - pairs of odd symmetric sets (size 10, Prop. 2.3(b));
   - shifts of size-4 ideal solutions. These are all symmetric. A short calculation shows the
     only shift with $\rho(c)=0$ is $c^2=(a^2+b^2)/2$, which lies in a balanced window.

   So a genus collision of size 8 would have to come from outside all of these.

*Heuristic.* The size-8 configurations form a 4-dimensional variety in $\mathbb P^7$, cut out by
equations of degrees $1,3,7$. The degree sum $11>8$ puts it in "general type" territory (the
same heuristic as `theory/audibility/proof.md` §4, with the same caveat that the variety is
neither smooth nor irreducible). This predicts that rational points lie on special
subvarieties, such as the pencil locus, which is balanced by Prop. 2.3(c). That is consistent
with finding none. **No claim is made.**

## 7. The cone-count version

- The least cone counts of genus-0 pairs sharing $L$ coefficients are those in the third table
  of §5.
- In general, Theorem 3.4 gives $T^{\rm cone}_L\le6N(2L-3)=O(L^2)$, replacing the $3\cdot2^{2L-2}$
  of the doubling construction on Thue–Morse blocks.
- The ideal value $T^{\rm cone}_3=8$ (3 vs 4 cone points) would be a balanced size-8
  3-configuration containing $\pm1$. Theorem 3.1 produces such configurations, but its converse
  (every balanced size-8 configuration is a pencil point) is **not** proved. It is only observed:
  all 7 balanced size-8 3-configurations with entries $\le80$ are pencil points
  (`attack/a04_pencil_converse.py`).
  - None of the 61 pencil configurations from 4-sets with entries $\le220$ contains $\pm1$
    (`data/pencil_log.txt`).
  - The search of [Sig] §5 found no 3-vs-4 pair with orders $\le80$.

## 8. Exact extent

**Proved for every $L$, given (H1)–(H3) of [Sig]:**

- Lemma 1.2, Lemma 1.5(1)–(2);
- Theorem 2.1, Proposition 2.2, Proposition 2.3;
- Theorem 3.1, Propositions 3.2–3.3, Theorem 3.4;
- Theorems 4.1–4.3.

**Cited:**

- $N(k)\le\frac12k(k+1)+1$ (Borwein–Ingalls Prop. 3; our Lemma 1.5(2) is the same pigeonhole);
- the PTE solutions and odd-power equalities used as inputs (`LITERATURE.md`). Each is
  re-verified exactly before use.

**Verified by exact computation:**

- every pair of §5;
- the searches of §§3, 6, 7, in the stated ranges.

**Open:**

- $T_3\in\{8,10\}$;
- whether $T_L$, $\tau_L$ or $T^{\rm cone}_L$ is $O(L)$. By Theorem 4.2 this is equivalent to
  $N(k)=O(k)$ for $\tau_L$, and implied by it for the others;
- the integer sharpness of Theorem A at $n=5$ (a pencil point with $m=5$ would settle it).
