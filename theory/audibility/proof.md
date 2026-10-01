# How much of a hyperbolic orbifold does heat hear? Audibility of the cone orders

## 0. Interpretation, kept apart from the mathematics

Read the cone orders $m_1,\dots,m_n$ as the decay rates of a stable linear system
$\dot x=-\operatorname{diag}(m_1,\dots,m_n)\,x$. Its characteristic polynomial is
$p(z)=\prod_i(z+m_i)$. In this reading the leading heat coefficients report the system's total
relaxation time $R=\sum_i 1/m_i$ and its odd spectral moments $\sum_i m_i^{2l+1}$, one per
coefficient.

The question is whether these numbers fix the decay spectrum. Recovery can fail in only one way:
a pair of rates that cancel, $m_i+m_j=0$, which is one mode decaying exactly as fast as another
grows. By Orlando's formula the product of all such pair sums is the Hurwitz determinant
$\Delta_{n-1}$ of $p$. The Routh–Hurwitz criterion makes every Hurwitz determinant of a stable
system positive. So audibility follows from stability: a stable system cannot be the time
reversal of part of itself, and that is the step on which the proof below turns.

The same structure appears computationally. Solving for the system from its heat data is a linear
problem, and its Gaussian elimination runs through Hurwitz determinants: the leading minors of the
system are, up to sign, Hurwitz determinants of $p$ (checked for $n\le8$).

This section is interpretation only. Nothing below depends on it.

## 1. Setting and statements

**Input from the heat expansion (not re-derived here).** On a closed hyperbolic orbifold of
genus 0 with cone points of orders $m_1,\dots,m_n\ge2$, the heat coefficient of $t^{-1}$ is a
fixed multiple of the area $2\pi(n-2-R)$. Every smooth-stratum term is a fixed multiple of the
area. A cone point of order $m$ contributes $b_l(m)=K^l\,\tfrac1m\,p_l(m)$ at order $t^l$ (Gauss curvature $K=-1$),
where $p_l$ is an *even* polynomial of degree $2l+2$ with
$p_l(1)=0$ and leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$. Sources:
`review/hyperresearch/Q2-cone-coefficients.md`, Uçar (4.25)+(4.33), and Schueth Thm 4.1 for
$l\le2$. The explicit $p_0,\dots,p_3$ listed there are even with root $m=1$.

Hence $\sum_i b_l(m_i)$ is a rational combination of $R,P_1,P_3,\dots,P_{2l+1}$ (write
$P_k=\sum_i m_i^k$) with a nonzero coefficient on $P_{2l+1}$. The map from the first $n$ heat
coefficients to

$$\mathcal I_n(m)=(R,\;P_1,\;P_3,\;\dots,\;P_{2n-3})$$

is therefore triangular and invertible, for a fixed number $n$ of cone points. Throughout,
$e_k$ denotes the elementary symmetric functions of the $m_i$, $e_0=1$, and $R=e_{n-1}/e_n$. Two
polynomials are attached to $m$:

- $f(z)=\prod_i(1+m_iz)=\sum_k e_kz^k$;
- $p(z)=\prod_i(z+m_i)=\sum_k e_kz^{n-k}$.

$\Delta_k$ is the $k$-th Hurwitz determinant of $p$, following Holtz–Tyaglov (1.37); see
`sources/SOURCES.md`.

> **Theorem A (audibility of the cone orders; all $n\ge1$).** Let $m$ be a multiset of $n$
> nonzero complex numbers with $m_i+m_j\neq0$ for all $i<j$. Equivalently, by Orlando,
> $e_n\Delta_{n-1}\neq0$. Let $m'$ be any multiset of $n$ nonzero complex numbers with
> $\mathcal I_n(m')=\mathcal I_n(m)$. Then $m'=m$.
>
> In particular $\mathcal I_n$ is injective on multisets of positive reals, repeated orders
> allowed. So the first $n$ heat coefficients determine the cone-order multiset of an $n$-cone
> hyperbolic orbifold of genus 0: $K_{\rm mult}\le n$.

> **Theorem B (the linear system and its determinant).** Let $T(z)=\tanh\bigl(\sum_{k\ {\rm odd}}
> P_kz^k/k\bigr)$. The $n-1$ equations
> $$e_{2j+1}-\sum_{i=0}^{j}T_{2i+1}\,e_{2j-2i}=0\qquad (j=0,\dots,n-2),$$
> together with $e_{n-1}-Re_n=0$, form a square linear system $M\,e=b$ in $e_1,\dots,e_n$.
> Its coefficients are polynomials in the heat invariants $\mathcal I_n$ alone, and the true
> $e$ solves it. For every $n\ge2$,
> $$\det M=c_n\,\frac{\Delta_{n-1}(p)}{e_n}=c_n\,\frac{\prod_{i<j}(m_i+m_j)}{\prod_i m_i},
> \qquad c_n\in\mathbb Q^\times .$$
> For $n=3,\dots,8$, $c_n=+1,+1,-1,-1,+1,+1$ (`linear_system.py`).

> **Theorem C (the fibres of $n-1$ invariants; sharpness).**
>
> 1. *Pair criterion.* Let $m,m'$ be multisets of $n$ nonzero complex numbers, and let
>    $Q(z)=\prod_i(z-m_i)\prod_j(z+m'_j)$. Then $\mathcal I_{n-1}$ agree, meaning $R$ and
>    $P_1,\dots,P_{2n-5}$, if and only if $Q(z)-Q(-z)=2\kappa z^3$ for some $\kappa$. If
>    $m_i+m_j\neq0$ for $i<j$, then $\kappa=0$ exactly when $m'=m$.
> 2. *Real sharpness, every $n\ge2$.* Every multiset of $n$ pairwise distinct positive reals lies
>    on a real curve of positive-real multisets sharing $\mathcal I_{n-1}$. Over the positive
>    reals, $n-1$ invariants never suffice.
> 3. *Integer sharpness ($n\ge3$, the range where hyperbolic genus-0 orbifolds exist).* It is
>    equivalent to finding a positive rational pair $m\neq m'$ (as multisets), i.e. a point off
>    all permutation components
>    on the pair variety, by scaling. It holds for $n=3$ and $n=4$ with explicit witnesses. For
>    $n=5$ no witness exists with all orders $\le120$ (216,071,394 multisets, exhaustive). For
>    $n\ge5$ it is open.

## 2. Proof of Theorem A

**Lemma 1 (parity).** In $\mathbb Q[x_1,\dots,x_N]$ let $s_j=\sum x_i^j$ and let $e_j$ be the
elementary symmetric functions. For odd $j$, $e_j$ lies in the ideal generated by
$s_1,s_3,\dots,s_j$. Conversely, $s_j$ lies in the ideal generated by $e_1,e_3,\dots,e_j$.

*Proof.* Newton's identity $je_j=\sum_{i=1}^{j}(-1)^{i-1}e_{j-i}s_i$ and induction on $j$ show
that $e_j$ is a $\mathbb Q$-linear combination of products $s_{i_1}\cdots s_{i_r}$ with
$i_1+\dots+i_r=j$. If $j$ is odd, some $i_t$ is odd. The converse is symmetric, writing $s_j$ in
the $e_i$ by the same identity. (Checked for odd $j\le11$, `verify_elimination.py`.) $\square$

*Proof of Theorem A.* Let $X=m\uplus(-m')$, a multiset of $2n$ nonzero numbers. Its power sums
are $s_j(X)=P_j(m)+(-1)^jP_j(m')$, so $s_j(X)=0$ for odd $j\le2n-3$. By Lemma 1,
$e_j(X)=0$ for odd $j\le 2n-3$.

Next, $e_{2n}(X)=\pm e_n(m)e_n(m')\neq0$, and
$$e_{2n-1}(X)=e_{2n}(X)\sum_{x\in X}\frac1x=e_{2n}(X)\bigl(R(m)-R(m')\bigr)=0.$$
So every odd-index elementary symmetric function of $X$ vanishes, and
$Q(z)=\prod_{x\in X}(z-x)=\sum_j(-1)^je_j(X)z^{2n-j}$ is an even polynomial. Hence the
multiplicity function satisfies $\mu_X(x)=\mu_X(-x)$ for all $x$, where
$\mu_X(x)=\mu_m(x)+\mu_{m'}(-x)$.

Let $A=\operatorname{supp}m$. If $x\in A$ then $-x\notin A$: otherwise $x=m_i$ and $-x=m_j$, so
either $i\ne j$ and $m_i+m_j=0$, or $i=j$ and $m_i=0$. For $x\in A$ this gives
$$\mu_m(x)+\mu_{m'}(-x)=\mu_X(x)=\mu_X(-x)=\mu_{m'}(x),$$
so $\mu_{m'}(x)\ge\mu_m(x)$. Summing over $A$,
$$n=\sum_{x\in A}\mu_m(x)\le\sum_{x\in A}\mu_{m'}(x)\le n .$$
All inequalities are equalities, so $m'=m$.

The equivalence of the hypothesis with $e_n\Delta_{n-1}\ne0$ is Orlando's formula
$\Delta_{n-1}(p)=\prod_{i<j}(m_i+m_j)$ for $p=\prod(z+m_i)$. That is [HT, Thm 1.17], verified
for $n\le8$ in `orlando_check.py` and `verify_elimination.py`. $\square$

*Remarks.*

1. The hypothesis is sharp over $\mathbb C$. If $m$ contains a pair $a,-a$, replacing it by
   $b,-b$ changes $m$ but not $\mathcal I_n$.
2. Repeated orders are allowed. The Jacobian of $\mathcal I_n$ is
   $c_n\,V(m)\prod_{i<j}(m_i+m_j)/\prod m_i^2$ with $V(m)=\prod_{i<j}(m_j-m_i)$ and
   $c_n=-\prod_{r<n}(2r-1)$ (checked $n\le7$).
   It vanishes on the diagonals $m_i=m_j$, so the map is not an immersion there, yet it is
   injective. The obstruction to injectivity is the Orlando factor $\prod(m_i+m_j)$, not the
   Vandermonde $V(m)$.
3. Different numbers of cone points. An order-1 "cone" is invisible to every heat coefficient
   ($b_l(1)=0$, and the area $2\pi(n-2-R)$ is unchanged by adding $m=1$). An orbifold with
   $n'\le n$ cone points padded by ones is therefore an $n$-multiset of positive reals. By
   Theorem A, the first $n$ coefficients distinguish an $n$-cone orbifold from every genus-0
   orbifold with at most $n$ cone points.
   - The comparison with orbifolds having *more* cone points is not covered by Theorem A.
   - A search of 3-cone against 4-cone orbifolds with orders $\le60$ found no pair sharing three
     coefficients (`sharpness_search.py`, part C).

## 3. Proof of Theorem B (the linearity behind every elimination step)

*Why the system is linear and the true $e$ solves it.* Write $f=E(z^2)+zO(z^2)$, split into even
and odd parts. From $\log f(z)=\sum_k(-1)^{k+1}P_kz^k/k$,
$$\tanh\Bigl(\tfrac12\log\tfrac{f(z)}{f(-z)}\Bigr)=\tfrac{f(z)-f(-z)}{f(z)+f(-z)}=\frac{zO}{E},
\qquad \tfrac12\log\tfrac{f(z)}{f(-z)}=\sum_{k\ \rm odd}\frac{P_kz^k}{k}.$$
So $zO=T\,E$ as power series. Modulo $z^{2n-1}$ only $P_1,\dots,P_{2n-3}$ enter, and the odd
coefficients $z^1,\dots,z^{2n-3}$ of $zO-TE$ give the $n-1$ rows. They are linear in $e$
because $T$ depends only on the data.

The converse also holds. If the $P_k$ are replaced by their Newton expressions in free
variables $e$, the same series identity shows the Newton system ($P_k(e)=P_k$ for odd
$k\le2n-3$) and the linear rows generate the same ideal. Hence the polynomial system has no
solutions beyond those of the linear system. This is why each elimination step in H2 and H3
was linear or reducible to a linear one. (Checked: `linear_system.py` (a) and (d).)

*Step 1: $\det M\ne0$ when $e_n\Delta_{n-1}\ne0$.* Let $Md=0$ and
$D(z)=\sum_{k=1}^nd_kz^k$, so $D(0)=0$. Then $zO_D\equiv TE_D$ and $zO_f\equiv TE_f$ modulo
$z^{2n-1}$. Hence
$$W:=E_fO_D-E_DO_f\equiv0\pmod{w^{n-1}},\qquad w=z^2.$$
Also $\deg_wW\le\lfloor n/2\rfloor+\lfloor(n-1)/2\rfloor=n-1$, so $W=c\,w^{n-1}$. Reading off
top coefficients (top of $E_f$, $O_f$ is $e_n$, $e_{n-1}$ for $n$ even, and $e_{n-1}$, $e_n$
for $n$ odd) gives
$$c=\pm\bigl(e_nd_{n-1}-e_{n-1}d_n\bigr)=\pm e_n\bigl(d_{n-1}-Rd_n\bigr)=0$$
by the last row. So $E_fO_D=E_DO_f$.

$E_f$ and $O_f$ are coprime. A common root $w_0$ gives $f(z_0)=f(-z_0)=0$ with $z_0^2=w_0$, and
$z_0\ne0$ since $f(0)=1$. Then $-1/m_i=z_0$ and $-1/m_j=-z_0$ for some $i\ne j$, so
$m_i+m_j=0$. Whichever of $E_f,O_f$ carries the leading coefficient $e_n\ne0$ has the maximal
possible degree, so it divides the corresponding part of $D$ with quotient a constant
$\lambda$. Then $D=\lambda f$, and $D(0)=0\ne\lambda$ forces $D=0$.

*Step 2: $\det M=0$ when $e_n\ne0$ and $\Delta_{n-1}=0$ ($n\ge2$).* Here the complex
multiset $m$ (the roots of $p$, all nonzero) contains a pair $a,-a$ at distinct positions.
Replacing it by $b,-b$ with $b\notin\{0,\pm a\}$ changes the multiset, hence $e$, but not $R$
or any odd $P_k$. Both $e$-vectors solve the same system $Me=b$, so $M$ is singular.

*Step 3: the exact form.* $\det M$ is a polynomial in the $P_k$ and is affine in $R$, which
occurs only in the last row. So $N(e):=e_n\det M$ is a polynomial in $e$. Assign weight $k$ to
$e_k$, $P_k$ and $T_k$, and weight $-1$ to $R$. Then row $j$ has weight $2j+1$, the last row
has weight $n-1$, and column $k$ has weight $k$. So $N$ is weighted-homogeneous of weight
$$\textstyle\sum_{j=0}^{n-2}(2j+1)+(n-1)-\binom{n+1}2+n=\binom n2,$$
which is also the weight of $\Delta_{n-1}$.

$\Delta_{n-1}=\prod_{i<j}(m_i+m_j)$ is irreducible in $\mathbb C[e]$. Its linear factors in
$\mathbb C[m]$ are pairwise non-associate and permuted transitively by $S_n$, so a symmetric
factor uses all or none of them. $e_n$ is a variable, hence irreducible.

By Step 1, valid for complex $e$, $V(N)\subseteq V(\Delta_{n-1}e_n)$. Each irreducible factor
$\pi$ of $N$ then satisfies $V(\pi)\subseteq V(\Delta_{n-1}e_n)$, so by the Nullstellensatz
$\pi\mid\Delta_{n-1}e_n$. Hence $N=c\,\Delta_{n-1}^\beta e_n^\iota$. By Step 2, $\beta\ge1$. Comparing weights,
$\beta\binom n2+\iota n=\binom n2$, so $\beta=1$ and $\iota=0$. $c\ne0$ by Step 1. $\square$

Step 1 alone gives a second, independent proof of Theorem A. The linear system depends only on
$\mathcal I_n$, and it has a unique solution.

## 4. Proof of Theorem C and the sharpness record

(1) This is the proof of Theorem A with one invariant fewer. Agreement of
$R,P_1,\dots,P_{2n-5}$ kills $e_j(X)$ for odd $j\le2n-5$ and for $j=2n-1$. That leaves
$Q(z)-Q(-z)=-2e_{2n-3}(X)z^3$. The converse uses the second half of Lemma 1. If $\kappa=0$ then
$Q$ is even, and the multiplicity argument gives $m'=m$.

(2) Multiply column $i$ of the $(n-1)\times n$ Jacobian of $\mathcal I_{n-1}$ by $m_i^2$.
Row $r$ becomes $c_r x_i^r$, with $x_i=m_i^2$, $r=0,\dots,n-2$, $c_0=-1$ and $c_r=2r-1$. Any
$n-1$ columns form a scaled Vandermonde in distinct $x_i$, so the rank is $n-1$ when the
positive $m_i$ are distinct. By the implicit function theorem the fibre through $m$ is a smooth
curve. Nearby points on it are ordered tuples close to $m$, and their entries remain distinct
and in the same order. A permutation of $m$ is at least the minimum gap away, so these nearby
points are positive-real multisets $m'\neq m$ with $\mathcal I_{n-1}(m')=\mathcal I_{n-1}(m)$.

(3) Rational and integer witnesses are equivalent. If positive rationals $m\ne m'$ share
$\mathcal I_{n-1}$, then so do $km,km'$ for any $k>0$, since $R\mapsto R/k$ and
$P_j\mapsto k^jP_j$. Choosing $k\in\mathbb Z$ large clears denominators, makes all orders
$\ge2$, and gives $R/k<n-2$, i.e. hyperbolicity.

Integer record (exact, `sharpness_search.py`, data in `sharpness_n5_N60.json` and
`sharpness_n5_N120.json`):

In the table, $\Phi(z):=p(z)p'(-z)-p'(z)p(-z)$ with $p=\prod(z+m_i)$ and $p'=\prod(z+m'_j)$.
It satisfies $\Phi=(-1)^{n+1}\bigl(Q(z)-Q(-z)\bigr)$.

| $n$ | witness sharing $\mathcal I_{n-1}$ | separated by | $\Phi(z)$ |
|---|---|---|---|
| 3 | $\{2,8,8\}$, $\{3,3,12\}$ ($R=3/4$, $S_1=18$) | $P_3$: 1032 vs 1782 | $500\,z^3$ |
| 4 | $\{3,10,15,30\}$, $\{4,5,21,28\}$ ($R=8/15$, $S_1=58$, $P_3=31402$) | $P_5$: 25159618 vs 21298618 | $1544400\,z^3$ |
| 5 | none with orders $\le60$ (7,028,847 multisets) or $\le120$ (216,071,394) | | |

The $n=5$ scan also records $(R,S_1,P_3)$ collisions as a control. There are 134 with orders
$\le60$, of which 11 are primitive and disjoint; to order 120 there are 2317, of which 42 are
primitive and disjoint. The smallest is $\{3,7,7,7,14\}$, $\{4,4,6,12,12\}$, matching the
review appendix. Collisions that are only scalings or paddings of smaller ones are excluded from
the primitive-disjoint count. So three invariants fail often for $n=5$, while four never failed
in range.

**Why integer sharpness for all $n$ is not proved here.** By (1), a witness is a multiset $X$
of $2n$ nonzero integers, $n$ positive and $n$ negative, with
$$\sum_{x\in X}x^j=0\ (j=1,3,\dots,2n-5),\qquad \sum_{x\in X}1/x=0,\qquad X\neq-X.$$
This is a Prouhet–Tarry–Escott-type system in odd powers with an extra reciprocal condition.
Equivalently, it asks for a monic $Q\in\mathbb Z[z]$ that splits into such linear factors and
whose odd part is a single monomial $\kappa z^3$.

Two features of this system are known:

- Witnesses are necessarily disjoint. A shared order can be cancelled, leaving two
  $(n-1)$-multisets that share all $n-1$ of their invariants, which contradicts Theorem A.
- Witnesses are rigid under the usual PTE moves. Translation destroys both the odd-power
  structure and the reciprocal condition.

The pair variety (with scaling removed) is cut out in $\mathbb P^{2n-1}$ by equations of degrees
$1,3,\dots,2n-5$ and $2n-1$ (the reciprocal condition after clearing denominators). The degree
sum $n^2-2n+3$ exceeds $2n$ for $n\ge4$. If this variety were a smooth complete intersection, it
would be of general type, and the Bombieri–Lang heuristic would predict non-dense rational
points. It is neither smooth nor irreducible (it contains the $n!$ diagonal components), so this
is only a heuristic. It is consistent with one primitive witness for $n=4$ in the scanned range
and none for $n=5$. **No sharpness theorem over the integers for $n\ge5$ is claimed.**

## 5. The planning hypotheses, tested independently

| | claim | verdict | exact form found |
|---|---|---|---|
| H1 | $3-3S_1R=-3\Delta_2/e_3$, $\Delta_2=(p+q)(q+r)(r+p)$ | **confirmed** | as stated |
| H2 | P5 equation linear in $e_4$, coefficient $\propto\Delta_3$, 38 positive terms | **confirmed** | coefficient $=5\Delta_3/(e_4S_1)$, i.e. $-15(P_3R-RS_1^3+3S_1^2)/(9S_1)$; the factor is $45/e_4$ over $9S_1$, not a constant |
| H3 | resultant linear in $e_3$ with lead $\propto\Delta_4/e_5$; $e_5$-step coefficient $-5(RS_1-1)$ | **confirmed** | $\operatorname{Res}_{e_5}=-9S_1^2\,L(e_3)$, lead$(L)=-945\,\Delta_4/e_5$ |
| H4 | $\Delta_{n-1}=\pm\prod(m_i+m_j)$ | **confirmed**, sign $+$ | Orlando [HT Thm 1.17]; checked $n\le8$ |
| H5 | linear at every step, obstruction a nonzero multiple of $\Delta_{n-1}$ | **proved for all $n$** | Theorem B; $\det M=c_n\Delta_{n-1}/e_n$ |

H3 has no spurious solutions. $F_5$ has degree 1 in $e_5$ with leading coefficient
$-45S_1(RS_1-1)$, which is nonzero since $RS_1-n^2=\sum_{i<j}(m_i-m_j)^2/(m_im_j)\ge0$. The
resultant therefore vanishes exactly at the $e_3$ of common solutions. Its only extra factor,
$S_1^2$, is nonzero. The remaining factor is linear with leading coefficient $-945\Delta_4/e_5$,
which is nonzero. The unique solution was checked to be the true $(e_2,\dots,e_5)$.

The only divisions are by $3S_1$ (the $e_2$-step), by powers of $S_1$ (clearing the
substituted $P_5,P_7$), by $-45S_1(RS_1-1)$, and by the lead of $L$.

The naive Newton route is not linear for larger $n$. After $e_1=S_1$, $e_{n-1}=Re_n$ and $e_2$
from $P_3$, the $P_{2k+1}$ equation has total degree $k-1$ in the remaining unknowns
($n=6,7,8$, `verify_elimination.py`). Linearity appears only after recombining through
$\tanh$, i.e. through the identity $zO=TE$. That is the explanation H5 asked for.

## 6. Exact extent of what is proved

**Proved for all $n$:**

- Theorem A (injectivity, hence $K_{\rm mult}\le n$ given the heat input of §1).
- Theorem B (linear system, $\det M=c_n\Delta_{n-1}/e_n$).
- Theorem C(1)–(2).

**Verified only for the stated ranges:**

- $c_n=\pm1$ for $n\le8$.
- The Hurwitz-minor structure of the elimination for $n\le8$.
- Orlando in full generality for $n\le7$, and for $p=\prod(z+m_i)$ for $n\le8$.

**Open:** integer sharpness $K_{\rm mult}\ge n$ for $n\ge5$.

**Depends on the cited heat input:** evenness of $p_l$, $p_l(1)=0$, and the nonzero leading
coefficient for every $l$. This is the only analytic input, and it is taken from the review's
reading of Uçar and Schueth, not re-derived here.

A correction to the review is needed. `VERDICT.md` §3 and `Q2-cone-coefficients.md` propose
reading the problem as "an $n$-node Prony system with $n$ moments", with non-degeneracy given by
the Vandermonde in $m_i^2$. As stated that is not a classical theorem: Prony recovery of $n$ free
nodes and $n$ free weights needs $2n$ moments. Its non-degeneracy condition is also the wrong
one. Injectivity holds on the diagonals, and the true obstruction is $\prod(m_i+m_j)$ (Remark 2).
