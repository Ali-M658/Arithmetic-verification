# The geometry of the degeneracy equation

Every claim below is either proved in the text or checked exactly by
[variety_checks.py](variety_checks.py) (output: [data/variety_checks.txt](data/variety_checks.txt)).
Sources quoted were fetched and read. Guy's §D16 could not be retrieved; see
`review/outstanding-fetches.md`.

## 1. The scale-invariant reformulation

Write $e_1,e_2,e_3$ for the elementary symmetric functions of a triple
$t=(p,q,r)$. The sum is $S=e_1$, the reciprocal sum is $R=e_2/e_3$, and the
quantity

$$\lambda(t)=\frac{e_1e_2}{e_3}=S\cdot R$$

is invariant under scaling $t\mapsto kt$.

**Proposition 1.** Two triples with the same sum $S$ have the same $R$ if and
only if they have the same $\lambda$. Conversely, let $t_1,\dots,t_k$ be
pairwise non-proportional positive integer triples with a common
$\lambda$, primitive sums $s_i$, and $L=\operatorname{lcm}(s_i)$. Then the
rescaled triples $(L/s_i)\,t_i$ form a degeneracy class at sum $L$, and it is
primitive. Its multiples $mL$ are its scaled copies. It is hyperbolic as soon
as $mL>\lambda$, since $R=\lambda/(mL)$, and all entries are $\ge2$.

So a degeneracy class is a finite set of positive rational points on one
plane cubic

$$C_\lambda:\ (x+y+z)(xy+yz+zx)=\lambda\,xyz ,$$

and the counting problem is how often a cubic in this pencil carries two or
more positive rational points of small height.

## 2. Structure: an elliptic pencil (Beauville's Γ₁(6) family)

* **The pencil.** We have $(x+y)(y+z)(z+x)=e_1e_2-e_3$. So $C_\lambda$ is the
  member $t=1-\lambda$ of the pencil $(X+Y)(Y+Z)(Z+X)+tXYZ=0$. Beauville's
  classification (C. R. Acad. Sci. Paris 294 (1982) 657–660) lists this pencil
  as the semistable family for $\Gamma_1(6)$, with singular-fibre components
  6, 3, 2, 1.
* **Weierstrass model.** Derived here and checked by sympy:
  $$y^2=x^3+(\lambda-3)^2x^2+8(\lambda-3)(\lambda-1)x+16(\lambda-1)^2,\qquad
  \Delta=2^{12}\lambda^2(\lambda-9)(\lambda-1)^3 .$$
  Its $j$-invariant agrees with the model of Bremner–Guy–Nowakowski
  (Math. Comp. 61 (1993) 117–130, DOI 10.1090/s0025-5718-1993-1189516-5):
  $\tau^2=\sigma(\sigma^2+(n^2-6n-3)\sigma+16n)$. Their paper studies exactly
  this curve, for integer $n$, as "Knight's problem"
  $n=(x+y+z)(1/x+1/y+1/z)$.
* **Fibre types.** $I_6$ at $\lambda=\infty$, $I_3$ at $1$, $I_2$ at $0$, $I_1$
  at $9$. The Euler numbers sum to 12, so the pencil, blown up at its 9 base
  points, is a rational elliptic surface $\mathcal E\to\mathbf P^1_\lambda$.
  For every $\lambda\notin\{0,1,9,\infty\}$, $C_\lambda$ is a smooth genus-one
  curve. The positive values relevant here satisfy $\lambda>9$ by AM–HM; at
  $\lambda=9$ only the point $(1:1:1)$ is positive.
* **Mordell–Weil over $\overline{\mathbf Q}(\lambda)$.** By Shioda–Tate the
  rank is $8-\sum_v(m_v-1)=8-(5+2+1)=0$. The six base points
  $(1{:}0{:}0),(0{:}1{:}0),(0{:}0{:}1),(1{:}{-1}{:}0),(0{:}1{:}{-1}),(1{:}0{:}{-1})$
  are sections of orders $1,2,3,3,6,6$ (base point $O=(1{:}{-1}{:}0)$). So the
  generic Mordell–Weil group is $\mathbf Z/6$, matching BGN's statement that
  the torsion is $\mathbf Z/6$ except at $n=10$. **No section of infinite
  order exists.** Every infinite family of degeneracies is therefore either
  torsion-driven or comes from a base change (a rational curve in the
  $\lambda$-line's covers), never from a "constant" point.
* **Real picture.** The positive points of $C_\lambda$ form a whole
  connected component, the oval (BGN's "egg"). The base points lie on the
  coordinate lines, which positive points never approach, since $\lambda\to\infty$
  there. So the egg is the non-identity component, and BGN state that "if $P$
  is on the egg, then just the odd multiples of $P$ give positive solutions".

## 3. Reciprocation is a torsion translation

The Vieta move $(p,q,r)\mapsto(qr/p,q,r)$ preserves $\lambda$. Up to
permutation it is reciprocation $t\mapsto(1/p,1/q,1/r)$, and it equals
translation by the 2-torsion section $T_2=(0{:}0{:}1)$, again up to
permutation. This is checked on 300 random points, and BGN's table records
the same fact. Two consequences follow.

* **Every triple has a degeneracy partner.** For $t=(a,b,c)$,
  $$\{\,e_2(t)\,(a,b,c),\ e_1(t)\,(bc,ca,ab)\,\}\quad\text{has}\quad S=e_1e_2,\ R=1/e_3 ,$$
  divided by the gcd of its six entries. This is the **dual family**. It
  fails only for geometric progressions, which are self-dual. The base pair
  is $t=(1,4,4)$.
* **The trivial symmetries are exhausted.** Up to permutation, the orbit of a
  point under $S_3$, reciprocation and the torsion translations is
  $\{\pm P+T\}$: 12 points, i.e. $t$ and its dual. Any other pair on the same
  curve differs by a point of infinite order. Among the 1,753 primitive pairs
  with $S\le600$, 423 are dual pairs and the other 1,330 differ by points of
  infinite order. None of those 1,330 differs by torsion.

## 4. The degeneracy threefold

Pairs $(t,t')$ with $e_1=e_1'$ and $e_2e_3'=e_2'e_3$ form a cone over a
threefold $Y\subset\mathbf P^5$: a quintic hypersurface in the hyperplane
$e_1=e_1'$. Projection to $t$ fibres $Y$ over $\mathbf P^2$, with fibre
$C_{\lambda(t)}$. So $Y$ is birational to the fibre square
$\mathcal E\times_{\mathbf P^1}\mathcal E$.

Schoen (Math. Z. 197 (1988) 177–199, DOI 10.1007/bf01215188, Prop. 7.1 and
Table 1) shows that the self-fibre product of a Beauville surface, here the
$\Gamma_1(6)$ one with fibres 6,3,2,1, is a **rigid Calabi–Yau threefold**.
Livné–Yui (arXiv math/0304497, Table 1) attribute its $L$-series to
Saito–Yui and to Verrill in Yui's 2001 survey. It is the $L$-series of the
weight-4 cusp form $\eta(q)^2\eta(q^2)^2\eta(q^3)^2\eta(q^6)^2$. That this
form has level 6 is our inference; the source does not state it, and
Verrill's JNT paper could not be retrieved.

**Consequence for counting.** On a Calabi–Yau threefold, Manin-type heuristics
predict few points of bounded height off special subvarieties. The
degeneracies we see must therefore accumulate on rational surfaces inside
$Y$. One is identified exactly:

**The dual surface is an anticanonical quartic del Pezzo.** The map
$t\mapsto(e_2t,\ e_1(yz,zx,xy))$ is given by six cubics. Their only linear
relation is the equality of sums, so they span the full 5-dimensional space
of cubics through their base locus. That locus is five reduced points: the
three coordinate points and the conjugate pair $e_1=e_2=0$, i.e.
$(1{:}\omega{:}\omega^2)$ and $(1{:}\omega^2{:}\omega)$, with no three
collinear. The image is therefore $\mathrm{Bl}_5\mathbf P^2\subset\mathbf P^4$,
anticanonically embedded, a quartic del Pezzo surface $\Sigma$, with
$\operatorname{rk}\operatorname{Pic}(\Sigma_{\mathbf Q})=1+3+1=5$. The sum $S$
of a pair is comparable to the anticanonical height. Its 16 lines are the
exceptional curves, the lines joining two base points, and the conic
$e_2=0$, and all of them lie outside the positive region. Manin's conjecture
for $\Sigma$ therefore predicts

$$\#\{\text{primitive dual pairs with }S\le X\}\sim c_\Sigma\,X(\log X)^{4},$$

and summing over scalings gives $X(\log X)^5$. We use this only as a
heuristic and do not claim that Manin's conjecture is known for $\Sigma$.

## 5. No linear families

**Proposition 2.** Let $(t(u,v),t'(u,v))$ be a two-parameter family in which
every entry is a linear form, the triples are positive on an open cone, and
$S$ and $R$ agree identically. Then $t'$ is a permutation of $t$. A family
affine in one parameter (a line not through the origin) is likewise trivial.
In particular every non-scaling polynomial family has degree $\ge2$ in its
parameter.

*Proof.* Equal $R$ means $\sum_i 1/L_i=\sum_i 1/L'_i$ as rational functions on
$\mathbf P^1$, where $L_i,L'_i$ are the linear forms. Group the forms by
their zero $x\in\mathbf P^1$. If $L_i=c_iL_x$, the polar part at $x$ is
$(\sum 1/c_i)/L_x$. On an open cone where all forms are positive, the $c_i$
grouped at one $x$ share a sign, so every pole carries non-zero charge.
Uniqueness of partial fractions forces the same poles with the same charges
on both sides, and equal $S$ forces equal sums of the $c_i$ at each pole.

Run through the partitions of three forms by pole, $\{1,1,1\},\{2,1\},\{3\}$.
Distinct poles force equal forms. A pole of multiplicity two matched
against $\{2,1\}$ with the other pole doubled needs $\alpha+\beta=1/(1/\alpha+1/\beta)$
with $\alpha,\beta$ of one sign, which AM–HM forbids. The same pairing with
the same pole doubled forces equal $\{\alpha,\beta\}$. The case $\{3\}$ is a
single ray. An affine line not through 0 spans, with the origin, a plane in
the cone, so it reduces to the planar case. ∎

So the scaling law is the only linear phenomenon, and anything new is at
least quadratic.

**Degree-2 families, searched.** A family that is linear in the parameter
before the sums are equalised is a pair of lines $(G_1,G_2)$ in
$\mathbf P^2$ with a Möbius $\varphi$ satisfying
$\lambda\circ G_1=\lambda\circ G_2\circ\varphi$. `families.py` §5 searches
all 189 lines (up to permutation) with coefficients of absolute value
$\le7$ that meet the positive triangle, and tests every candidate exactly.

It finds exactly the 18 conics of the dual conic bundle: lines
$qy=rz$ through a vertex, paired with themselves by the Vieta involution.
The 189 lines have 189 pairwise distinct branch-value discriminants.
Since equivalent maps share their branch values, no two different lines
pair up. The only non-trivial self-equivalences are the Vieta involutions
on the 18 lines through a vertex. Separately, none of the 669 non-dual primitive
pairs with $S\le400$ is related by $Q=\pm mP+T$ or $P=\pm mQ+T$ with
$m\in\{2,3\}$ and $T$ torsion (`families.py` §6), so the non-dual pairs
are not low-degree multiplication images either.

## 6. Does Schinzel's method adapt? **Yes, verbatim, and further.**

Schinzel (Serdica Math. J. 22 (1996) 587–588, fetched) solves Guy D16
(equal sum and equal product) as follows. He takes $f(x)=x^3-9x+9=y^2$ and
the point $(7,17)$, which fails Nagell's condition $y^2\mid\Delta$ and so
has infinite order. By Poincaré–Hurwitz density there are infinitely many
rational points in a region that maps to positive solutions of
$x_1+x_2+x_3=x_1x_2x_3=6$. He then clears denominators of $k$ of them. No
group-law bookkeeping is needed beyond density.

The $(e_1,e_2/e_3)$ problem has exactly the same shape. The
scale-invariant curve $C_\lambda$ replaces his fixed-sum, fixed-product
curve, and "clear denominators" becomes "rescale to the lcm of the sums"
(Proposition 1).

**Theorem 3 (arbitrarily large fibres).** For every $k$ there are
infinitely many primitive degeneracy classes of size at least $k$, i.e. $k$
pairwise distinct hyperbolic triples with a common $S$ and a common $R$.

*Proof.* On $C_{155/12}$ the positive point $P=(4,9,18)$ has infinite order:
$nP\ne O$ for $n\le12$, which suffices by Mazur. PARI's 2-descent gives
rank exactly 2. By BGN, or by density of $\langle2P\rangle$ in the identity
component, the odd multiples $(2n+1)P$ are positive. They are pairwise
distinct, and each multiset accounts for at most six points. Any $k$ of them,
rescaled to the lcm of their sums and multiplied by any $m$, give classes of
size $\ge k$. Distinct choices give distinct classes. ∎

$3P=(162833463,287876366,723926268)$ is already large. Fibres from a single
generator are astronomically far out, and the enumeration finds far smaller
ones: the first sizes 3, 4, 5, 6 occur at $S=136,408,1849,4600$. The curves
carrying them have ranks 2, 2, 3, 3 (torsion $\mathbf Z/6$). Every primitive
size-5 class up to 4800 sits on a curve of rank 3 or 4.

**What does *not* adapt: the base pair is isolated.** $C_{27/2}$ has rank 0
by 2-descent, and torsion $\mathbf Z/2\times\mathbf Z/6$. Its only positive
points are the permutations of $(1,4,4)$ and $(1,1,4)$. Hence, for every
$k$, the class of $\{(2k,8k,8k),(3k,3k,12k)\}$ has exactly two members: no
third pillow ever joins the minimal degeneracy. Isosceles triples are
2-division points of torsion sections, hence torsion. So the whole isosceles
family, including the base pair, is a torsion phenomenon, and the unbounded
fibres come only from curves of positive rank.

**Difference from D16.** In D16 a degeneracy needs two independent points on
one curve. Here the 2-torsion translation hands every triple a partner for
free (§3), so degeneracies are much more plentiful. That is why the
counting function is nearly linear with many logarithms, rather than sparse.

## 7. Lower bounds from the families

Notation: $\mathcal N(X)$ is the cumulative count of degenerate **pairs**
with $S\le X$, the paper's convention. $\mathcal N_{\rm cl}(X)$ is the count
of classes. For a primitive pair $D$ with sum $S_D$, its copies $kD$ are
hyperbolic for all $k\ge4$. Indeed, if $D$ is the reduced dual pair of a
primitive $t$, then $R_D=G/e_3(t)\le e_2(t)/e_3(t)\le3$, because the gcd $G$
divides $e_2(t)$. So $R_{kD}\le 3/k<1$, and every entry of $kD$ is
$\ge k\ge2$. Distinct $(k,D)$ give distinct pairs, so

$$\mathcal N(X)\ \ge\ \sum_{D}\#\{k\ge4:\ kS_D\le X\}.\tag{$*$}$$

**Theorem 4 (isosceles family; explicit constant).** For coprime $1\le u<v$,
$$D_{u,v}=\{(2u+v)(u,v,v),\ (u+2v)(v,u,u)\}/g,\qquad g=\gcd(2u+v,u+2v)\in\{1,3\},$$
is a primitive degeneracy with $S=(2u+v)(u+2v)/g$ and $R=g/(uv)$; the base
pair is $D_{1,4}$. The number of these with $S\le y$ is
$c_{\rm iso}\,y+O(\sqrt y\log y)$, where $c_{\rm iso}=\dfrac{3\log2}{2\pi^2}=0.10535\ldots$.
Hence
$$\mathcal N(X)\ \ge\ \mathcal N_{\rm cl}(X)\ \ge\ \big(c_{\rm iso}+o(1)\big)\,X\log X .$$

*Proof.* The identity is checked symbolically in `families.py`. With
$a=2u+v$ and $b=u+2v$, the region $\{u,v>0,\ ab\le Y\}$ has area
$Y\log 2/3$. Coprime pairs have density $6/\pi^2$, and among them
$u\equiv v\pmod 3$, the case $g=3$, has relative density $1/4$. Ordered pairs
with $S\le y$ therefore number $\tfrac6{\pi^2}\tfrac{\log2}{3}\big(\tfrac34y+\tfrac14\cdot3y\big)
+O(\sqrt y\log y)$, and halving for $u<v$ gives $c_{\rm iso}y$. The
error term is the standard boundary estimate for primitive lattice points
in a region bounded by a hyperbola arc and two rays. Partial summation in
$(*)$ gives $c_{\rm iso}X\log X+O(X)$.

For classes: a class contains at most two triples with a repeated entry,
since $a+2b=S$ and $1/a+2/b=R$ is a quadratic in $b$. So each class contains
at most one isosceles pair, and the bound holds for $\mathcal N_{\rm cl}$ too.

*Check:* there are 506 such primitive pairs with $S\le4800$, against
$c_{\rm iso}\cdot4800=505.7$. All 2,917 hyperbolic isosceles pairs with
$S\le4800$ occur in the enumeration. ∎

This already beats $\lfloor S/18\rfloor$ by a growing factor of
$18c_{\rm iso}\log S\approx1.9\log S$.

**Theorem 5 (the conic bundle; one more logarithm).**
$$\mathcal N(X)\ \ge\ \Big(\frac{3}{128\pi^4}+o(1)\Big)\,X(\log X)^2 .$$

*Proof.* For coprime $q\le r$ and coprime $u,v\ge1$, put $t=(u,vq,vr)$. This
is primitive, and it lies on the line through $(1{:}0{:}0)$ of slope $q:r$.
Its dual pair, divided by $v$, is
$$\{(\alpha u+\beta v)(u,vq,vr),\ (u+\alpha v)(\beta v,ur,uq)\},\qquad \alpha=q+r,\ \beta=qr,$$
with common sum $Q(u,v)=(\alpha u+\beta v)(u+\alpha v)$, checked
symbolically. So the reduced pair $D(t)$ has $S_{D}\le Q(u,v)$. A pair $D$
arises from at most 6 tuples $(q,r,u,v)$: choose the member, then the entry
playing $u$. It is a genuine pair unless $t$ is a geometric progression,
which happens for at most 3 ratios $u:v$ per $(q,r)$.

Take $V=\sqrt{y/(4\alpha\beta)}$ and $U=\beta V/\alpha$. Since
$\beta/\alpha\le\alpha$, every $(u,v)\in[1,U]\times[1,V]$ has
$Q\le 4\alpha\beta V^2=y$. That box contains
$\tfrac6{\pi^2}UV+O((U+V)\log y)=\tfrac{3}{2\pi^2}\,y/\alpha^2+O(M\sqrt y\log y)$
coprime pairs.

Sum over coprime $q\le r\le M=y^{1/8}$, using
$\sum_{n\le M}\varphi(n)/(2n^2)\sim\tfrac3{\pi^2}\log M$. The error totals
$O(M^3\sqrt y\log y)=o(y)$, so
$$A(y):=\#\{D:\ S_D\le y\}\ \ge\ \tfrac16\cdot\tfrac{9}{2\pi^4}\,y\log M\,(1+o(1))=\tfrac{3}{32\pi^4}\,y\log y\,(1+o(1)).$$

In $(*)$, restrict to $S_D\le X/8$, where $\#\{k\ge4\}\ge X/(2S_D)$. Partial
summation with $\sum_{S_D\le Y}1/S_D\ge\int^Y A(y)y^{-2}\,dy\ge\tfrac{c_A}{2}(\log Y)^2$
finishes the proof. ∎

The constant is poor; the order of growth is the point. Neither theorem
gives a power $S^a$ with $a>1$. By Proposition 2 no family can be linear,
and every family found is a rational surface whose points have
anticanonical height comparable to $S$, so its count is
$X(\log X)^{O(1)}$. **A lower bound $S^{a}$ with $a>1$ is not available
from parametric families, and the data (§growth) give no reason to expect
one.**
