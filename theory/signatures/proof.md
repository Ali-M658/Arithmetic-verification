# How much of a hyperbolic orbifold does heat hear? The signature: cone count and genus

## 0. Interpretation, kept apart from the mathematics

Short-time heat diffusion is local. In time $t$ heat explores a neighbourhood of radius about
$\sqrt t$, so each heat coefficient is a sum of local contributions. On a closed hyperbolic
2-orbifold only two kinds of place are distinguishable at short range. Smooth points all look
alike at curvature $-1$, and they contribute a fixed multiple of the area. A cone point
contributes a fixed function of its order.

A handle has no local signature. Heat can hear the genus only through the area it uses up, via
Gauss–Bonnet. The question is therefore one of bookkeeping. An area $A$ can be spent on handles
($4\pi$ each) or on cone points (between $\pi$ and $2\pi$ each), and the question is whether
finitely many coefficients reveal how it was spent.

The mechanism found below fits the mirror picture of the genus-0 work
(`theory/audibility/proof.md`).

- Two orbifolds are compared through a single multiset $Z=U\uplus(-V)$. Here $U$ and $V$ are
  their cone orders, padded with invisible order-1 points.
- Agreement of the first $L$ coefficients says that $Z$ has vanishing reciprocal sum and
  vanishing odd moments up to order $2L-3$.
- Equal genera make $Z$ *balanced*: as many positive as negative entries. A genus difference
  $g-g'$ unbalances it by exactly $2(g-g')$.
- If $Z$ is small compared with $L$, the moment conditions force $Z$ to be symmetric, $Z=-Z$,
  and a symmetric multiset is balanced.

So a handle is heard as a *parity defect* of the mirror multiset, and it costs no more
coefficients than a cone point does.

There are two consequences.

- Once the area is known, $\lfloor A/\pi\rfloor+4$ coefficients determine the genus and every
  cone order.
- No fixed number of coefficients works for all areas. Prouhet's Thue–Morse partition produces
  large orbifolds of different genus, or with different numbers of cone points, whose heat
  coefficients agree to any prescribed order.

This section is interpretation only. Nothing below depends on it.

## 1. Setting, heat input and notation

$\mathrm{Sig}$ denotes the set of signatures $\sigma=(g;m_1,\dots,m_n)$ of closed orientable
hyperbolic 2-orbifolds (`definitions.tex`, `def:signature`). Here $g\ge0$, each $m_i\ge2$, and
$m=\{m_i\}$ is a multiset. Write
$$n=|m|,\qquad R(m)=\sum_i\frac1{m_i},\qquad P_j(m)=\sum_im_i^j,\qquad
s(\sigma)=2g-2+\sum_i\Bigl(1-\frac1{m_i}\Bigr)=-\chi=\frac{\mathrm{Area}}{2\pi}>0 .$$
$H_k(\mathcal O)=(c_1,\dots,c_k)$ are the first $k$ heat coefficients (`def:heatcoef`), and
$K_{\rm mult}(\mathcal O;\mathcal P)$ is as in `def:K`.

**Heat input (H).** This is the only analytic input. Every quoted statement was fetched and is
recorded in `literature.md` and `../cone-coefficients/ucar-source.md`.

- (H1) *Smooth part.* At constant curvature $\kappa$ the smooth-stratum coefficient $a_\nu$ is
  $\mathrm{vol}(\mathcal O)$ times a constant depending only on $\nu$ and $\kappa$. This is
  Uçar, Thm 4.20(i), eq. (4.35), for every $\nu$. The structure (smooth part plus one term per
  singular stratum) is DGGW, Thm 4.8 and Def. 4.7.
- (H2) *Cone part.* A cone point of order $k$ contributes $b_l(k)$ at order $t^l$, with
  $b_l(k)=K^l\sum_{i=0}^{l}\frac{2}{4^ii!}c^{\mathbb S}_{l-i}(\pi/k)$ and $c^{\mathbb S}$ given
  by (4.25). This is Uçar, Thm 4.20(ii), eqs. (4.33)–(4.34).
- (H3) The expansion runs in the powers $t^{-1},t^0,t^1,\dots$ (`def:heatcoef`). Hence, at
  $K=-1$,
  $$c_1=\frac{\mathrm{Area}}{4\pi}=\frac s2,\qquad c_{l+2}=\alpha_l\,\mathrm{Area}+C_l(m),\qquad
  C_l(m):=\sum_ib_l(m_i)\quad(l\ge0),$$
  with universal constants $\alpha_l$.

Two consequences follow. Genus enters the heat data only through the area. And two orbifolds of
equal area have equal $c_{l+2}$ exactly when they have equal $C_l$.

The first consequence is an inference, not a fetched sentence: by Gauss–Bonnet the area is
$2\pi s$, and $g$ appears nowhere else. `literature.md` ("What is fetched vs. what is inferred")
records this.

Put $\psi_k(x)=x^{2k-1}-x^{-1}$ for $k\ge1$, and $\Psi_k(m)=\sum_i\psi_k(m_i)=P_{2k-1}(m)-R(m)$.

## 2. Lemmas on the heat data

**Lemma 1 (cone polynomials, every $l$).** $p_l(k):=k\,b_l(k)/K^l$ is an even polynomial of
degree $2l+2$ with $p_l(1)=0$. Its leading coefficient is
$|B_{2l+2}|/(2(l+1)!(2l+1))\neq0$.

*Proof.* In (4.25), $k\,c^{\mathbb S}_l(\pi/k)$ is a rational combination of the polynomials
$k^{2j}-1$, $0\le j\le l+1$. Each of these is even and vanishes at $k=1$. So the same holds for
$p_l$, a combination of the $k\,c^{\mathbb S}_{l-i}$, which have degree $2(l-i)+2$.

The top degree $2l+2$ comes only from $i=0$, $j=l+1$. Its coefficient is
$$2\cdot\tfrac14\cdot\frac{(-1)^l}{(l+1)!(2l+1)}\,B_{2l+2}B_0(\tfrac12)
=\frac{(-1)^lB_{2l+2}}{2(l+1)!(2l+1)},$$
since $B_0(\tfrac12)=1$. Now $B_{2l+2}=(-1)^{l}\,2(2l+2)!\,\zeta(2l+2)/(2\pi)^{2l+2}$ is nonzero
with sign $(-1)^l$. Checked exactly for $l\le15$ (`heat_structure.py`). $\square$

(This closes, for all $l$, the nonvanishing that `definitions.tex` records as verified only for
$l\le6$.)

**Lemma 2 (triangular basis).** $\phi_l(x):=p_l(x)/x=\sum_{k=1}^{l+1}a_{l,k}\,\psi_k(x)$ with
$a_{l,l+1}\ne0$. Hence, for multisets $m,m'$ and $L\ge1$:
$$C_l(m)=C_l(m')\ (0\le l\le L-2)\iff\Psi_k(m)=\Psi_k(m')\ (1\le k\le L-1).$$
The direction "$\Leftarrow$" does not use $a_{l,l+1}\neq0$.

*Proof.* Write $p_l(x)=\sum_{k=0}^{l+1}a_{l,k}x^{2k}$. Then $\sum_ka_{l,k}=p_l(1)=0$, so
$p_l(x)/x=\sum_{k\ge1}a_{l,k}x^{2k-1}+a_{l,0}x^{-1}=\sum_{k\ge1}a_{l,k}\psi_k(x)$. The system is
triangular with diagonal $a_{l,l+1}\neq0$ (Lemma 1). Every $a_{l,k}$ for $l\le15$ is computed in
`heat_structure.py`; e.g. $\phi_1=\tfrac1{36}\psi_1+\tfrac1{360}\psi_2$. $\square$

**Lemma 3 (padding).** Adjoining points of order 1 changes neither the area nor any $C_l$.

*Proof.* $1-\tfrac11=0$, and $b_l(1)=K^lp_l(1)=0$ by Lemma 1. Checked directly on 300 random
signatures for $l\le15$. $\square$

**Lemma 4 (reduction).** Let $\sigma=(g;m)$ and $\sigma'=(g';m')$ have $n$ and $n'$ cone
points, and let $L\ge1$. Then $H_L(\mathcal O)=H_L(\mathcal O')$ if and only if
$$2g+n-R(m)=2g'+n'-R(m')\quad\text{and}\quad\Psi_k(m)=\Psi_k(m')\ (1\le k\le L-1).\tag{4.1}$$
Assume (4.1). Then $d:=R(m')-R(m)=2(g'-g)+n'-n$ is an integer. Put
$$U=m\uplus\{1\}^{\max(d,0)},\qquad V=m'\uplus\{1\}^{\max(-d,0)} .$$
Then
$$R(U)=R(V),\qquad P_j(U)=P_j(V)\ \ (j\text{ odd},\ j\le2L-3),\qquad |V|-|U|=2(g-g'),\tag{4.2}$$
and
$$|U|+|V|=2\max\bigl(n+g-g',\;n'+g'-g\bigr).\tag{4.3}$$

Conversely, let $U=m\uplus\{1\}^a$ and $V=m'\uplus\{1\}^b$ be any paddings, and let $g,g'\ge0$.
If (4.2) holds, then $(g;m)$ and $(g';m')$ have equal area and equal first $L$ heat
coefficients.

*In terms of the mirror multiset.* Pad both multisets to a common length $N$, write $R_N$, $P_{j,N}$
for the padded sums, and put $X=m_N\uplus(-m'_N)$. Equal area is
$$s_{-1}(X)=R_N-R'_N=2(g-g').$$
Equal $C_0,\dots,C_{L-2}$ is then equivalent to
$$s_j(X)=P_{j,N}-P'_{j,N}=2(g-g')\qquad (j\text{ odd},\ j\le2L-3),$$
the *same* multiple $2(g-g')$ for every odd $j$ and for $j=-1$. This is the unique solution of
the linear system formed by the cone-sum differences, computed in `heat_structure.py` (4) for
$L\le16$. It follows for all $L$ from Lemma 2, because $\sum_ka_{l,k}=0$.

*Proof.* By (H3), $c_1$ agrees iff the areas agree, i.e. iff $s(\sigma)=s(\sigma')$, i.e. iff the
first equation of (4.1) holds. Given equal area, $c_2,\dots,c_L$ agree iff $C_0,\dots,C_{L-2}$
agree. By Lemma 2 that is the second part of (4.1).

From (4.1), $d$ is an integer. With $U$ and $V$ as defined, $R(U)=R(m)+\max(d,0)$ and
$R(V)=R(m')+\max(-d,0)$, and these are equal. Since $\psi_k(1)=0$, $\Psi_k(U)=\Psi_k(m)$, so
$P_{2k-1}(U)=\Psi_k(U)+R(U)=P_{2k-1}(V)$. Next,
$|U|-|V|=n-n'+d=2(g'-g)$. For (4.3): $|U|+|V|=n+n'+|d|$, and $|d|$ is the larger of $\pm d$.

For the converse, the area of $(g;m)$ is $2\pi(2g-2+|U|-R(U))$, because each padding 1 adds
$1$ to $|U|$ and $1$ to $R(U)$. The same holds for $V$, so (4.2) gives equal area. The equalities
$\Psi_k(m)=\Psi_k(U)=P_{2k-1}(U)-R(U)$ and Lemma 2 ("$\Leftarrow$") give equal
$C_0,\dots,C_{L-2}$. $\square$

**Lemma 5 (parity; `theory/audibility/proof.md`, Lemma 1).** For odd $j$, $e_j$ lies in the
ideal generated by the power sums $s_1,s_3,\dots,s_j$.

## 3. The separation theorem

**Theorem S.** Let $\mathcal O,\mathcal O'$ be closed orientable hyperbolic 2-orbifolds with
$\sigma(\mathcal O)\neq\sigma(\mathcal O')$ and $H_L(\mathcal O)=H_L(\mathcal O')$. Let $U,V$ be
as in Lemma 4, and let $U^*,V^*$ be obtained by cancelling the elements they have in common.
Then
$$|U^*|+|V^*|\ \ge\ 2L+2 .$$

*Proof.* Cancelling a common element removes it from both sides of every identity in (4.2) and
leaves $|V|-|U|$ unchanged. So $U^*,V^*$ are disjoint and satisfy (4.2). Put $T=|U^*|+|V^*|$.
Then $T\equiv|V^*|-|U^*|=2(g-g')\pmod 2$, so $T$ is even. Suppose $T\le2L$.

Let $Z=U^*\uplus(-V^*)$, a multiset of $T$ nonzero reals. Its power sums are
$s_j(Z)=P_j(U^*)-P_j(V^*)=0$ for odd $j\le2L-3$, so $e_j(Z)=0$ for those $j$ (Lemma 5). If
$T>0$, then
$$e_{T-1}(Z)=e_T(Z)\sum_{z\in Z}\frac1z=e_T(Z)\bigl(R(U^*)-R(V^*)\bigr)=0 .$$
Every odd $j\in[1,T-1]$ is either $\le T-3\le2L-3$ or equal to $T-1$. So all odd-index
elementary symmetric functions of $Z$ vanish, and since $T$ is even,
$$Q(z)=\prod_{x\in Z}(z-x)=\sum_{j\ \rm even}(-1)^je_j(Z)\,z^{T-j}$$
is an even polynomial. Hence $\mu_Z(x)=\mu_Z(-x)$ for every $x$. For $x>0$ this reads
$\mu_{U^*}(x)=\mu_{V^*}(x)$, so $U^*=V^*$; being disjoint, both are empty. (If $T=0$ this holds
trivially.)

So $U=V$. Then $|U|=|V|$ gives $g=g'$, and deleting the 1s gives $m=m'$. This contradicts
$\sigma\neq\sigma'$. Hence $T\ge2L+1$, and since $T$ is even, $T\ge2L+2$. $\square$

The proof uses only that the orders are positive reals and the genera are integers, so Theorem S
holds verbatim for positive real "orders" different from 1. (An order equal to 1 is invisible: $(0;1,2,3,7)$ and $(0;2,3,7)$ have identical heat data.)

**Corollary S1 (pairwise form).** If $H_L(\mathcal O)=H_L(\mathcal O')$ with
$$L\ \ge\ \max\bigl(n+g-g',\ n'+g'-g\bigr),$$
then $\sigma(\mathcal O)=\sigma(\mathcal O')$.

*Proof.* $|U^*|+|V^*|\le|U|+|V|$, and the latter equals $2\max(\cdot)$ by (4.3). $\square$

**Corollary S2 (area form: genus and cone orders from finitely many coefficients).** Let
$\mathcal O$ have area $A$. Any closed orientable hyperbolic 2-orbifold $\mathcal O'$ with
$H_{\lfloor A/\pi\rfloor+4}(\mathcal O')=H_{\lfloor A/\pi\rfloor+4}(\mathcal O)$ has the same
genus and the same cone-order multiset. In the notation of `def:K`, with
$\mathrm{Sig}$ the class of all closed orientable hyperbolic 2-orbifolds,
$$K_{\rm mult}(\mathcal O;\mathrm{Sig})\ \le\ \Bigl\lfloor\frac{\mathrm{Area}(\mathcal O)}{\pi}\Bigr\rfloor+4 .$$

*Proof.* Each cone point adds at least $\tfrac12$ to $\sum(1-1/m_i)$. So
$A/2\pi\ge2g-2+n/2$, i.e.
$$n+4g\le A/\pi+4 .$$
The same holds for $\mathcal O'$, which has the same area because $c_1$ agrees. Hence
$n+g-g'\le n+4g\le A/\pi+4$, and likewise $n'+g'-g\le A/\pi+4$. Both are integers, so both are
$\le\lfloor A/\pi\rfloor+4$. Apply S1. $\square$

The number of coefficients needed is itself heard: $c_1$ gives $A$, and $A$ says how many more
coefficients to take.

**Theorem T1 (cone count and cone orders, genus 0).** Let $\mathcal O$ be a hyperbolic
genus-0 orbifold of area $A$ with $n$ cone points.

1. $n\le A/\pi+4$, with equality iff every order is 2.
2. The first $\lfloor A/\pi\rfloor+4$ heat coefficients determine the cone-order multiset, and
   in particular $n$, among *all* hyperbolic genus-0 orbifolds. The number $n$ need not be known
   in advance.
3. More sharply, the first $\max(n,n')$ coefficients separate it from every genus-0 orbifold
   with $n'$ cone points and a different multiset.

*Proof via Theorem A, every step.*

(1) $A/2\pi=\sum(1-1/m_i)-2\ge n/2-2$, with equality iff every $1-1/m_i=\tfrac12$.

(2) Let $\mathcal O'$ be genus-0 and hyperbolic with $H_N(\mathcal O')=H_N(\mathcal O)$, where
$N=\lfloor A/\pi\rfloor+4$. Then $c_1$ agrees, so $\mathcal O'$ also has area $A$, and $n'\le N$
by (1). Pad $m$ and $m'$ with 1s to length $N$. By Lemma 3 this changes neither the area nor any
$C_l$. The padded multisets $m_N,m'_N$ are $N$-multisets of positive reals.

- From $s=N-2-R(m_N)$ (padding preserves $s$), $R(m_N)=N-2-s$ is the same for both.
- By Lemma 2, $\Psi_k(m_N)=\Psi_k(m'_N)$ for $k\le N-1$, so
  $P_{2k-1}(m_N)=\Psi_k+R(m_N)$ agree.

Thus $\mathcal I_N(m_N)=(R,P_1,P_3,\dots,P_{2N-3})$ agree. By Theorem A
(`theory/audibility/proof.md`), $m_N=m'_N$. Deleting the 1s gives $m=m'$.

(3) This is S1 with $g=g'=0$. $\square$

`cone_count.py` (a)–(b) checks (1) and (2) by brute force on 27,007 genus-0 signatures
($n\le6$, orders $\le14$; 70,579 equal-area pairs).

## 4. No fixed number of coefficients suffices

**Proposition P (Prouhet; Thue–Morse).** Let $t(i)$ be the parity of the binary digit sum of
$i$. Let $D\ge1$, and let $T_0,T_1$ split $\{0,\dots,2^D-1\}$ according to $t(i)$. Then:

1. $\sum_{T_0}f=\sum_{T_1}f$ for every polynomial $f$ of degree $<D$.
2. For every $c>0$ and $h>0$,
   $$\sum_{i<2^D}\frac{(-1)^{t(i)}}{hi+c}>0 .$$

*Proof.* $\sum_{i<2^D}(-1)^{t(i)}x^i=\prod_{r<D}(1-x^{2^r})$ by binary expansion. This vanishes
to order $D$ at $x=1$, and applying $(x\,d/dx)^j$ for $j<D$ gives (1). For (2), the sum equals
$$\frac1h\int_0^1y^{c/h-1}\prod_{r<D}\bigl(1-y^{2^r}\bigr)\,dy,$$
whose integrand is positive on $(0,1)$. $\square$

**Theorem N (non-uniformity).**

(a) *Genus.* For every $L\ge2$ and every $g'\ge0$ there are closed orientable hyperbolic
2-orbifolds of genus $g'+1$ and $g'$ with equal first $L$ heat coefficients. For $g'=0$ they can
be chosen with area $<2\pi(4^{L-1}-1)$.

(b) *Cone count.* For every $k\ge2$ there are hyperbolic genus-0 orbifolds with $n$ and $n+1$
cone points, for some $n$, with equal first $k$ heat coefficients.

(c) Consequently:

- no fixed number of heat coefficients determines the genus among closed orientable hyperbolic
  2-orbifolds;
- no fixed number determines the cone count among genus-0 ones;
- $\sup_{\mathcal O}K_{\rm mult}(\mathcal O;\mathcal P)=\infty$, both for $\mathcal P=\mathrm{Sig}$
  and for $\mathcal P$ the genus-0 class.

*Proof of (a).* Put $D=2L-2\ge2$ and use the points $2i-1$, $i<2^D$. Prouhet (1), applied to
$f(i)=(2i-1)^j$ for odd $j\le D-1$, separates the $i=0$ term $(-1)^j=-1$ and gives
$P_j(U_0)=P_j(V_0)$ for
$$U_0=\{2i-1:i\in T_0,\ i\ge1\},\qquad V_0=\{2i-1:i\in T_1\}\uplus\{1\},$$
with $|U_0|=2^{D-1}-1$ and $|V_0|=2^{D-1}+1$. Let
$$A'=\{2i+1:i\in T_0\},\qquad B'=\{2i+1:i\in T_1\}.$$
These have equal $P_j$ for all $j<D$, and $\rho:=R(A')-R(B')>0$ by Prouhet (2). Put
$r_0=R(U_0)-R(V_0)$.

- If $r_0=0$, let $U=2U_0$ and $V=2V_0$.
- Otherwise swap $A',B'$ if necessary so that $\rho/r_0>0$. Write $\rho/r_0=p/q$, doubling both
  if one of them is 1. Let $U=qU_0\uplus pB'$ and $V=qV_0\uplus pA'$. Then
  $$R(U)-R(V)=\frac{r_0}{q}-\frac{\rho}{p}=0,$$
  every odd $P_j$ with $j\le D-1=2L-3$ agrees, all entries are $\ge2$, and $|V|-|U|=2$.

By the converse in Lemma 4 (with $a=b=0$), $(g'+1;U)$ and $(g';V)$ share their first $L$
coefficients.

Hyperbolicity: $s(g';V)\ge-2+|V|/2=-2+(2^D+1)/2>0$. Area:
$s<-2+|V|=2^D-1=4^{L-1}-1$ when $g'=0$.

*Proof of (b).* Put $D=2k-2$ and let
$$A=\{i+1:i\in T_0\}\ni1,\qquad B=\{i+1:i\in T_1\}\not\ni1 .$$
Then $P_j(A)=P_j(B)$ for $j<D$, and $r_0=R(A)-R(B)>0$. With $A',B',\rho$ as in (a), write
$r_0/\rho=\sum_{i=1}^{t}1/p_i$ with distinct integers $p_i\ge2$. This is possible for every
positive rational: take $1/2+1/3+\dots$ while the partial sum stays $\le r_0/\rho$, then finish
with the Fibonacci–Sylvester greedy algorithm, whose denominators keep increasing.

Let $U=A\uplus\biguplus_ip_iB'$ and $V=B\uplus\biguplus_ip_iA'$. Then
$$R(U)-R(V)=r_0-\rho\sum_i\frac1{p_i}=0,$$
the odd $P_j$ agree for $j\le2k-3$, $|U|=|V|$, $U$ contains exactly one 1, and $V$ contains
none.

By Lemma 4 (with $g=g'=0$), $(0;U\setminus\{1\})$ and $(0;V)$ share their first $k$
coefficients. They have $|U|-1$ and $|U|$ cone points. Hyperbolicity:
$s(0;V)\ge-2+(1-\tfrac12)+(1-\tfrac13)+2\cdot\tfrac12>0$, since $V\supseteq B\ni2,3$ and $V$ has
at least two further entries $\ge2$.

*Proof of (c).* Each pair in (a) or (b) consists of distinct signatures, so
$K_{\rm mult}\ge L+1$ (respectively $k+1$) for its members. $\square$

The constructions are built and checked with the actual cone coefficients $b_l$:

- (a) for $L=2,\dots,6$ (`genus.py` (A)). Each pair shares *exactly* $L$ coefficients; the
  $L=6$ pair has 1023 and 1025 cone points.
- (b) for $k=2,3$ (`cone_count.py` (d)): 9 vs 10 and 103 vs 104 cone points, sharing exactly
  2 and 3 coefficients.

For $k\ge4$ the greedy denominators grow doubly exponentially, which makes exact verification
impractical. The proof above covers every $k$.

**Corollary N1 (growth).** Let $f(A)=\max\{K_{\rm mult}(\mathcal O;\mathrm{Sig}):
\mathrm{Area}(\mathcal O)\le A\}$. For $A\ge6\pi$,
$$\Bigl\lfloor\log_4\Bigl(\frac{A}{2\pi}+1\Bigr)\Bigr\rfloor+2\ \le\ f(A)\ \le\
\Bigl\lfloor\frac A\pi\Bigr\rfloor+4 .$$

*Proof.* The upper bound is S2, since $\lfloor\cdot\rfloor$ is monotone. For the lower bound,
take $L=\lfloor\log_4(A/2\pi+1)\rfloor+1\ge2$. Then $2\pi(4^{L-1}-1)\le A$, and N(a) gives an
orbifold of smaller area with $K_{\rm mult}\ge L+1$. $\square$

## 5. Exact searches

All searches use exact integer or rational keys. Every pair reported is re-verified with the
actual cone coefficients $b_l$ from (H2), not only through Lemma 2.

**Genus-changing collisions** (`genus.py`, transcript `output/genus.txt`).

| shared $L$ | smallest found | $\lvert U^*\rvert+\lvert V^*\rvert$ | area$/2\pi$ |
|---|---|---|---|
| 1 | $(g+1;\,)$ vs $(g;2,3,6)$, $g\ge1$: area alone | 4 | $2g$ |
| 2 | $(1;15)$ vs $(0;3,3,5,5)$ | 6 = $2L+2$ (least possible) | $14/15$ |
| 2 | $(1;10,10)$ vs $(0;4,4,4,4,5)$ | 8 | $9/5$ |
| 3 | $(1;15,15,15)$ vs $(0;3,3,5,7,7,21)$ | 10 | $14/5$ |
| 3 | $(1;14,22,22)$ vs $(0;2,4,7,7,11,28)$ | 10 | $437/154$ |
| 3 | Thue–Morse, 15 vs 17 cone points | — | $<15$ |
| 4, 5, 6 | Thue–Morse, $4^{L-1}\mp1$ cone points | — | $<4^{L-1}-1$ |

Least-size searches ($\lvert U^*\rvert+\lvert V^*\rvert=2L+2$):

- $L=2$: 9 pairs with entries $\le40$, shapes $(\lvert U\rvert,\lvert V\rvert)=(2,4)$ and
  $(1,5)$.
- $L=3$: none with entries $\le30$, shapes $(3,5),(2,6),(1,7)$.
- $L=4$: none with entries $\le22$, shapes $(4,6),(3,7),(2,8)$.

At size $2L+4$:

- $L=3$: 2 pairs with entries $\le30$, shape $(4,6)$; none with entries $\le24$, shape $(3,7)$.
- $L=4$: none with entries $\le16$, shape $(5,7)$.

Direct search of signature space: all hyperbolic $(g;m)$ with $g\le2$, $n\le5$ and orders
$\le16$, 46,353 signatures. Among genus-changing equal-area pairs, 11,048 share exactly one
coefficient, 46 share exactly two, and none shares three.

**Theorem S, brute force.** All 97,920 equal-area pairs of that pool satisfy
$\text{shared}\le\tfrac12(\lvert U^*\rvert+\lvert V^*\rvert)-1$. Equality holds in 28,168 pairs.
So the inequality of Theorem S is attained, and cannot be improved as a pairwise statement.

**Genus 0, different cone counts** (`cone_count.py`, transcript `output/cone_count.txt`).

| shared $k$ | example or search | result |
|---|---|---|
| 1 | $(0;4,4,6)$ vs $(0;2,2,3,3)$ | area only |
| 2 | $(0;5,5,5)$ vs $(0;2,2,2,10)$; $(0;6,9,9)$ vs $(0;2,2,3,18)$ | 3 vs 4 cone points |
| 2 | $(0;4,5,8,8)$ vs $(0;2,2,2,10,10)$ | 4 vs 5 |
| 3 | padded length $N=4$ (3 vs 4), orders $\le80$ | **none** |
| 3 | $N=5$ (3 or 4 vs 5), orders $\le40$; $N=6$, orders $\le20$ | **none** |
| 3 | construction N(b) | 103 vs 104 cone points |
| 4 | $N=5$, orders $\le40$; $N=6$, orders $\le22$ | **none** |

Theorem A forces $N\ge k+1$ in any such pair. So "3 vs 4 sharing 3" is the least-size case.
Equivalently, a 3-vs-4 pair sharing three coefficients is an integer witness of Theorem C(3)
(`theory/audibility/proof.md`) at $n=4$ in which one side contains the gcd of all eight orders.
Dividing by that gcd turns the entry into a padding 1.

AREA_CLASSES_PLACEHOLDER

## 6. Relation to $K_{\rm mult}$ (`def:K`)

- *All genera.* $K_{\rm mult}(\mathcal O;\mathrm{Sig})\le\lfloor\mathrm{Area}(\mathcal O)/\pi\rfloor+4$
  (S2). The sharper bound is the maximum over the finitely many signatures $\sigma'$ of the same
  area of $\max(n+g-g',\,n'+g'-g)$ (S1). The supremum over $\mathcal O$ is infinite (N), and it
  grows at least like $\log_4\mathrm{Area}$ (N1).
- *Fixed $n$, genus 0.* Theorem A gives $K_{\rm mult}(\mathcal O;\mathcal P_n)\le n$. That is S1
  with $g=g'=0$ and $n=n'$.
- *$K_{\rm iso}$* is unaffected. By `eq:Kcompare`, $K_{\rm mult}\le K_{\rm iso}$, and `prop:Kinf`
  (conditional on `thm:locality`) still makes $K_{\rm iso}=\infty$ wherever two non-isometric
  orbifolds share a signature. The results here concern $K_{\rm mult}$ only. No moduli count for
  $g\ge1$ is used or claimed; `definitions.tex` notes that one would need its own source.

## 7. Exact extent of what is proved

**Proved, every $L$, given (H):**

- Lemmas 1–4. Lemma 1 includes the nonvanishing leading coefficient for every $l$.
- Theorem S, Corollaries S1 and S2.
- Theorem T1.
- Theorem N (a)–(c) and Corollary N1.

**Verified only in the stated ranges:**

- The constructions are built explicitly for $L\le6$ in (a) and $k\le3$ in (b).
- The searches of §5.
- The per-area values of §5.

**Open.**

1. *The growth of $f(A)$.* It is at least logarithmic and at most linear (N1). Is it linear?

   The Diophantine core is as follows, for the genus. Let $T_L$ be the least $|U|+|V|$ over
   disjoint multisets $U,V$ of positive integers with $|V|-|U|$ even and nonzero, $R(U)=R(V)$,
   and $P_j(U)=P_j(V)$ for odd $j\le2L-3$. By Lemma 4 these are exactly the genus-changing
   collisions sharing $L$ coefficients.

   - Theorem S gives $T_L\ge2L+2$, and N(a) gives $T_L\le2^{2L-1}$.
   - $T_2=6$, attained by $(1;15)$ vs $(0;3,3,5,5)$.
   - $T_3\in\{8,10\}$: size 10 is attained, and no size-8 pair has entries $\le30$.
   - Linear growth of $f$ would need $T_L=O(L)$ along a sequence.

   This is an odd-power Prouhet–Tarry–Escott problem with a reciprocal condition, and
   $T_L=2L+2$ is its analogue of an "ideal" solution. For the classical PTE problem, existence
   of ideal solutions in every degree is a long-standing open problem. That analogy is heuristic
   only.
2. *The least number of coefficients determining the cone count in genus 0.* It is not uniform
   (N(b)). No pair with different cone counts sharing three coefficients was found with padded
   length $\le6$, while N(b) produces one at 103 vs 104 cone points. The least cone count of
   such a pair is unknown.
3. *Real versus integer thresholds.* Over positive reals, whether $\lvert U^*\rvert+\lvert V^*\rvert=2L+2$
   is attained for every $L$ is not established here.

**Depends on the cited heat input:** (H1)–(H3), as fetched in `literature.md`. Lemma 1 derives the
needed properties of the cone polynomials from Uçar (4.25)+(4.33) for every $l$.

## 8. Literature: what is known about heat invariants and the genus

Quoted in full in `literature.md`.

- **Uçar** (arXiv:1711.03405), Cor. 4.21(iv) and Cor. 4.23. For closed orientable orbisurfaces
  of constant curvature $\kappa\neq0$, "$\kappa$ together with the spectrum of $\mathcal O$
  determines the Euler characteristic of $\mathcal O$ as well as the Euler characteristic of the
  underlying space $X_{\mathcal O}$". The proof uses only heat invariants, but all of them: the
  cone orders are recovered through limits $\nu\to\infty$ (proof of Thm 3.40). The word "genus"
  does not occur in the thesis.
- **Dryden–Strohmaier** (arXiv:math/0504571; Canad. Math. Bull. 52 (2009) 66–71), Thm 1.1 and
  Prop. 3.3. For compact orientable hyperbolic orbisurfaces the Laplace spectrum determines the
  number of cone points of each order, "and thus the genus". This is proved with the Selberg
  trace formula, i.e. from the full spectrum, not from heat invariants.
- **Gittins–Gordon–Membrillo Solis–Rossetti–Sandoval–Stanhope** (arXiv:2311.00337). This paper
  makes no statement about the genus; the full-text search found no occurrence. It states that
  heat invariants are integrals of universal curvature polynomials, and it gives 1-form-isospectral
  flat 2-orbifolds with different underlying spaces.
- **Full-text arXiv search** (first result pages of nine queries). No paper found states that
  *finitely many* heat invariants determine the genus or the signature of an orbisurface. Only
  first pages were inspected, so this is not a proof of absence.

Relative to this record, the new statements are:

- the finite and explicit count $\lfloor A/\pi\rfloor+4$ (S2);
- the sharp pairwise threshold (S, S1);
- the proof that no count independent of the area exists (N).
