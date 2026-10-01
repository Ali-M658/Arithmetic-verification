# The first overlap of adjacent least-order strata, for every p

## 0. Physical reading

Fix the total cone order $S$ of a hyperbolic triangular pillow and its least cone order $p$.
The pillows of this stratum form a one-parameter family. They slide from the balanced pillow,
with the two remaining orders equal, to the spread pillow, with the two smallest orders equal.
Along the slide the reciprocal sum $R$ moves monotonically across an interval
(Lemma `lem:chamber`). $R$ is the area deficit, $\operatorname{Area}=2\pi(1-R)$.

As $S$ grows, the interval of stratum $p$ drifts down towards that of stratum $p+1$. The first
sum at which the two intervals touch is where the balanced end of one stratum first reaches the
spread end of the next. This is a statement about two real curves in the $(S,R)$-plane, and
their crossing point $x^*(p)=3p(p+1)/(p-1)$ is the root of a quadratic.

A two-coefficient collision asks for more: two pillows with exactly the same $R$. Overlap of
the intervals is only the real-variable shadow of this arithmetic condition. Two coincidences
make the first overlap and the first collision agree, and they happen only for $p=2$ and $p=4$.

## 1. Notation (from `paper/main.tex`, Section `sec:threshold`)

A hyperbolic triad is $2\le p\le q\le r$ with $R=\frac1p+\frac1q+\frac1r<1$. The
$(S,p)$-stratum is the set of hyperbolic triads with $p+q+r=S$ and least order $p$.

- For $p\ge3$ it is nonempty for $S\ge3p$ except $(S,p)=(9,3)$, and it contains both its
  balanced and its spread triad. $(p,p,S-2p)$ is hyperbolic unless it is $(3,3,3)$.
- For $p=2$ it is nonempty iff $S\ge11$, and it never contains its spread triad.

By Lemma `lem:chamber` and Lemma `lem:bound`,
$$R^+_{S,p}=\frac2p+\frac1{S-2p},\qquad
R^-_{S,p}=\frac1p+\frac1{\lfloor D/2\rfloor}+\frac1{\lceil D/2\rceil},\quad D=S-p,$$
and
$$\varphi_p(S)=\frac4{S-p}-\frac1{S-2p-2},\qquad \tau_p=\frac{p-1}{p(p+1)}$$
as in the proof of Theorem `thm:separation`. Write $\operatorname{gap}_p(S)=R^-_{S,p}-R^+_{S,p+1}$.

**Definition.** The strata $p$ and $p+1$ *overlap at $S$* if their sets of reciprocal sums
have intersecting convex hulls.

Stratum $p=2$ is truncated by $R<1$. Its spread triad $(2,2,S-4)$ is not hyperbolic, so its
upper endpoint is the largest hyperbolic value, not $R^+_{S,2}$. Its lower endpoint
$R^-_{S,2}$ is attained iff $S\ge11$. For the two formal cases $(p,S)=(2,9),(2,10)$ covered by
"$S\ge3p+3$" below, stratum 2 is empty and $\operatorname{gap}_2(S)>0$, so all statements hold
trivially. Every other endpoint is attained. Brute-force agreement for $S\le600$ is in
`threshold.py` C5.

## 2. Two reductions

**Lemma 1 (one inequality).** For $S\ge3p+3$, the strata $p,p+1$ overlap at $S$ iff
$\operatorname{gap}_p(S)\le0$.

*Proof.* Overlap means $R^-_{S,p}\le\max(\text{stratum }p{+}1)=R^+_{S,p+1}$ together with
$R^-_{S,p+1}\le\max(\text{stratum }p)$.

- For $p\ge3$ the second inequality is automatic. $R^-_{S,p+1}\le R^+_{S,p+1}\le R^+_{S,p}$,
  because $R^+_{S,p}$ is non-increasing in $p$ for $p\le S/3$.
- For $p=2$, if $\operatorname{gap}_2(S)\le0$ then $S\ge18$. This follows from the sign of
  the gap alone, Theorem 1(a),(b) below, which do not use Lemma 1. Then $(2,5,S-7)$ is hyperbolic with $R>7/10$, while
  $R^-_{S,3}\le\frac13+\frac{4(S-3)}{(S-3)^2-1}\le\frac13+\frac{60}{224}<\frac7{10}$
  (decreasing in $S$, value at $S=18$).

$\square$

**Lemma 2 (adjacent separation suffices; the chain in the proof of `thm:separation`).** If
$\operatorname{gap}_p(S)>0$ for every $p$ with both strata $p,p+1$ nonempty at $S$, then all
strata of sum $S$ have pairwise disjoint reciprocal-sum sets, and $\sigma$ is injective on
triads of sum $S$.

*Proof.* For $p<p''$, every value of stratum $p''$ is at most
$R^+_{S,p''}\le R^+_{S,p+1}<R^-_{S,p}$, and $R^-_{S,p}$ is at most every value of stratum $p$.
Injectivity within a stratum is Lemma `lem:chamber`. $\square$

## 3. The closed form

**Theorem 1.** For every $p\ge2$ let
$$S^*(p)=\begin{cases}18,&p=2,\\ 19,&p=3,\\ 3p+8,&4\le p\le8,\\ 3p+7,&p\ge9.\end{cases}$$
For $S\ge3p+3$, the strata $p$ and $p+1$ overlap at $S$ iff $S\ge S^*(p)$. Equivalently,
$S^*(p)$ is the least $S\ge x^*(p)=\dfrac{3p(p+1)}{p-1}=3p+6+\dfrac6{p-1}$ with $S\equiv p$
(mod 2), except for $p\ge9$, where the odd-parity sum $3p+7$ comes first.

*Proof.*

*(a) Even parity ($D=S-p$ even).* Lemma `lem:bound` is an equality, and
$\operatorname{gap}_p(S)=\varphi_p(S)-\tau_p$. Clearing denominators gives the quadratic
$(p-1)S^2-(6p^2+2p-2)S+3p(p+1)(3p+2)$. Its discriminant is $4(2p+1)^2$, so its roots are
rational, $3p+2$ and $x^*(p)$, and
$$\varphi_p(S)-\tau_p=-\frac{(p-1)(S-3p-2)(S-x^*(p))}{p(p+1)(S-p)(S-2p-2)}.$$
For $S\ge3p+3$ every factor except $S-x^*$ is positive. So for even $D$,
$\operatorname{gap}_p(S)\le0$ iff $S\ge x^*(p)$, and by Lemma 1 this is the overlap
condition.

*(b) Odd parity.* With $q=(D-1)/2$ and $r=(D+1)/2$,
$\frac1q+\frac1r=\frac4D+\frac4{D(D^2-1)}$. Hence
$$\operatorname{gap}_p(S)=\varphi_p(S)-\tau_p+\frac4{D(D^2-1)}>\varphi_p(S)-\tau_p .$$
So there is no overlap of either parity for $S<x^*(p)$.

For $S>3p+4$, $\varphi_p$ is strictly decreasing. The numerator of $\varphi_p'$ is
$-(S-3p-4)(3S-5p-4)$. The correction $4/(D(D^2-1))$ also decreases, so the odd-parity gap is
strictly decreasing for $S\ge x^*>3p+4$. Once an odd sum overlaps, every larger odd sum
overlaps.

*(c) The sum $3p+7$.* Here $D=2p+7$ is odd and $S-2p-2=p+5$. The gap is
$$\operatorname{gap}_p(3p+7)=\frac1p+\frac1{p+3}+\frac1{p+4}-\frac2{p+1}-\frac1{p+5}
=-\frac{2\,(p^2-5p-30)}{p(p+1)(p+3)(p+4)(p+5)} .$$
$p^2-5p-30$ has roots $(5\pm\sqrt{145})/2$, the larger about 8.52, so it is negative for
$2\le p\le8$. At $p=9+u$ it equals
$u^2+13u+6$, with positive coefficients. Hence the strata overlap at $3p+7$ iff $p\ge9$.

*(d) Assembly.*

- **$p\ge9$.** $x^*<3p+7$, so every $S\le3p+6$ lies below $x^*$ and does not overlap. $S=3p+7$
  overlaps by (c). Every larger sum overlaps: even sums are $\ge x^*$, and odd sums by
  monotonicity (b).
- **$p\le8$.** $x^*(p)=18,18,20,\tfrac{45}2,\tfrac{126}5,28,\tfrac{216}7$ for $p=2,\dots,8$.
  The least $S\ge x^*$ with $D$ even is $18,19,20,23,26,29,32$.

  The only odd-parity sums in $[x^*,\text{that value})$ are:

  | $p$ | odd sum | $\operatorname{gap}_p$ |
  |---|---|---|
  | 3 | $S=18$ | $\tfrac{101}{168}-\tfrac35=\tfrac1{840}>0$ |
  | 7 | $S=28$ | $\tfrac{257}{770}-\tfrac13=\tfrac1{2310}>0$ |
  | 8 | $S=31$ | $\tfrac1{10296}>0$, by (c) |

  None of them overlaps. The odd sum $S^*(p)+1$ overlaps in each case, with
  $\operatorname{gap}_p(S^*+1)=-\frac7{936},-\frac1{72},-\frac{19}{3960},-\frac1{180},
  -\frac{76}{15015},-\frac1{231},-\frac{17}{4680}$ for $p=2,\dots,8$. So by (b) all larger odd
  sums overlap too.

$\square$

The reduction to Lemma 1 and the endpoint formulas were checked against a brute-force
computation of all stratum endpoints from the hyperbolic triads themselves, for every
adjacent pair with $S\le600$ (58,705 pairs, `threshold.py` C5). The closed form was checked
against the case analysis for $2\le p<5000$ (C3).

## 4. No collision below 18, for all p

**Corollary 2.** For every $S\le17$, the map $\sigma=(S_1,R)$ is injective on hyperbolic
triads of sum $S$. At $S=18$ there is exactly one collision,
$\{\mathcal O(2,8,8),\mathcal O(3,3,12)\}$.

*Proof.* A collision at sum $S$ joins two different strata (Lemma `lem:chamber`). By Lemma 2,
some adjacent pair $p,p+1$ must then overlap at $S$, so $S\ge S^*(p)\ge x^*(p)$. Now
$$x^*(p)-18=\frac{3(p-2)(p-3)}{p-1}\ge0,$$
with equality only at $p=2,3$. So $S\ge18$.

At $S=18$:

- $S^*(p)\le18$ only for $p=2$. Every other adjacent pair is strictly separated, and Lemma 2
  applies to strata $3,4,\dots$.
- For $p=2$, $S=x^*(2)$ with $D=16$ even, so by (a) $\operatorname{gap}_2(18)=0$. The two
  intervals share exactly the point $R=\tfrac34$, attained by the balanced triad $(2,8,8)$ and
  the spread triad $(3,3,12)$.
- Strata $\ge4$ lie below $R^+_{18,4}=\tfrac35<\tfrac34$, so they meet neither.

$\square$

For $S\le17$ this replaces the three per-$p$ comparisons in the proof of Theorem
`thm:separation` by one inequality, $x^*(p)\ge18$, valid for every $p$, with no case list. The
statement at $S=18$ still uses one exact comparison: $\operatorname{gap}_3(18)=\frac1{840}>0$,
needed because $18=x^*(3)$, together with the $p=2$ tangency.

## 5. First overlap versus first collision

Overlap is necessary for a collision, not sufficient. The table compares $S^*(p)$ with the
first sum at which a triad of least order $p$ and one of least order $p+1$ share $R$. It comes
from exact enumeration of every hyperbolic triad with $S\le600$ (`threshold.py`, full table in
`first_overlap_vs_collision.csv`). The enumeration reproduces all 2,977 collision fibres of
`theory/diophantine/data/groups.csv` for $S\le600$. "Window" counts the triads of each stratum
lying in $[R^-_{S,p},R^+_{S,p+1}]$, the only candidates for an adjacent collision.

| $p$ | $x^*(p)$ | $S^*(p)$ | first collision | gap | window at $S^*$ / at collision | colliding pair |
|---|---|---|---|---|---|---|
| 2 | 18 | 18 | 18 | 0 | 1+1 / 1+1 | (2,8,8), (3,3,12) |
| 3 | 18 | 19 | 38 | 19 | 2+1 / 11+3 | (3,14,21), (4,6,28) |
| 4 | 20 | 20 | 20 | 0 | 1+1 / 1+1 | (4,8,8), (5,5,10) |
| 5 | 45/2 | 23 | 117 | 94 | 1+1 / 49+12 | (5,32,80), (6,15,96) |
| 6 | 126/5 | 26 | 34 | 8 | 2+1 / 6+3 | (6,14,14), (7,9,18) |
| 7 | 28 | 29 | 62 | 33 | 2+1 / 18+8 | (7,20,35), (8,14,40) |
| 8 | 216/7 | 32 | 64 | 32 | 2+1 / 18+8 | (8,20,36), (9,15,40) |
| 9 | 135/4 | 34 | 42 | 8 | 1+1 / 5+3 | (9,15,18), (10,12,20) |
| 10 | 110/3 | 37 | 109 | 72 | 1+1 / 37+18 | (10,44,55), (11,28,70) |
| 11 | 198/5 | 40 | 66 | 26 | 1+1 / 14+8 | (11,22,33), (12,18,36) |
| 12 | 468/11 | 43 | 188 | 145 | 1+1 / 74+34 | (12,72,104), (13,45,130) |
| 13 | 91/2 | 46 | 94 | 48 | 1+1 / 25+15 | (13,39,42), (14,28,52) |
| 14 | 630/13 | 49 | 69 | 20 | 1+1 / 11+7 | (14,20,35), (15,18,36) |
| 22 | 506/7 | 73 | 422 | 349 | 1+1 / 176+96 | (22,92,308), (23,77,322) |

Of the 198 adjacent pairs whose strata coexist below 600, only 50 collide by $S=600$, the
largest such $p$ being 143. The first collision between any two strata is at 18. The first
between non-adjacent strata is at 35, between strata 5 and 7.

**Proposition 3 (why the gap is positive except at $p=2,4$).**

1. The balanced triad of stratum $p$ and the spread triad of stratum $p+1$ have equal $R$
   (a tangency) iff $p\in\{2,4\}$, at $S=x^*(p)$.
2. For every $p\notin\{2,4\}$ the first adjacent collision occurs strictly after $S^*(p)$.

*Proof.*

(1) *Even $D$.* By (a), equality forces $S=x^*(p)\in\mathbb Z$ with $S\equiv p$ (mod 2). Since
$\gcd(p-1,p)=1$ and $\gcd(p-1,p+1)\mid2$, $x^*\in\mathbb Z$ iff $(p-1)\mid6$, i.e.
$p\in\{2,3,4,7\}$. Here $x^*-p=2p(p+2)/(p-1)$ equals $16,15,16,21$, so only $p=2,4$ have the
right parity.

*Odd $D$.* An endpoint equality is a zero of the strictly decreasing odd-parity gap.

- For $p\ge9$ the gap is positive below $x^*>3p+6$ and negative at $3p+7$ by (c), so its zero
  lies strictly inside $(3p+6,3p+7)$ and is not an integer.
- For $p\le8$, the odd-parity gap is strictly decreasing. It is positive at the odd sums
  below $S^*(p)$ listed in Theorem 1(d), or there are none in $[x^*,S^*)$. It is negative at
  $S^*(p)+1$, the fractions above. Hence it has no zero at an odd integer.

(2) For $p\ge9$, at $S^*=3p+7$ the window holds exactly one triad of each stratum:

- In stratum $p$ the balanced triad is $(p,p+3,p+4)$. The next one, $(p,p+2,p+5)$, lies above
  $R^+_{S,p+1}=\frac2{p+1}+\frac1{p+5}$ because $\frac1p+\frac1{p+2}>\frac2{p+1}$ by
  convexity.
- In stratum $p+1$ the spread triad is $(p+1,p+1,p+5)$. The next one, $(p+1,p+2,p+4)$, lies
  below $R^-_{S,p}=\frac1p+\frac1{p+3}+\frac1{p+4}$ because
  $\frac1{p+1}+\frac1{p+2}<\frac1p+\frac1{p+3}$. The two pairs have equal sums, and the spread
  pair has the larger reciprocal sum.

So a collision at $S^*$ would be an endpoint equality, excluded by (1). For $p\in\{3,5,6,7,8\}$
there is no collision at $S^*(p)$ by direct check. $\square$

**The gap, physically.** At the first overlap, the two intervals overlap only in a sliver. The
sliver holds just the two extreme pillows, plus one more for $p\in\{3,6,7,8\}$.

- For $p\notin\{3,6,7,8\}$, a collision there would need a tangency, and that is an
  integrality accident in $x^*(p)$.
- For $p\in\{3,6,7,8\}$, the third pillow is excluded by direct check.

Beyond $S^*$ the sliver widens. The overlap depth is $-\operatorname{gap}_p(S)$, which by (a)
grows linearly in $S-x^*$ at first. The window fills with pillows from both ends:

- At the balanced end of stratum $p$ the values of $R$ are packed quadratically, because $R$ is
  stationary at $q=r$.
- At the spread end of stratum $p+1$ they are spaced about $1/p^2$ apart, so the $p$-side
  window fills fastest. This matches the window counts in the table.

A collision then needs two reciprocal sums from different strata to coincide exactly. When
that first happens is an arithmetic event, not a geometric one.

- In practice coincidences occur through shared small denominators. At the first collisions the
  denominator of $R$ is tiny compared with $pqr$: 42 at $S=38$, 30 at $S=42$, 3542 at $S=422$.
- The data show no geometric regularity. Among the 50 adjacent pairs that collide by $S=600$,
  the gaps other than the two tangencies range from 8 to 455, the maximum at $p=33$ ($S^*=106$, first collision 561). There is
  no monotone pattern in $p$, and the windows hold tens of pillows on each side at the first
  collision.
- The other 148 coexisting pairs have no collision by 600. Their gaps are censored by the
  search limit. Small gaps come from rationally parametrised coincidences such as
$(9,15,18)=3(3,5,6)$ against $(10,12,20)=2(5,6,10)$, with
$\tfrac13R(3,5,6)=\tfrac12R(5,6,10)=\tfrac7{30}$.

## 6. What is proved, and what is only computed

- Proved for all $p\ge2$: Theorem 1 (closed form, both parities, overlap iff $S\ge S^*$),
  Corollary 2 (no collision below 18, exactly one at 18), and Proposition 3(1) together with
  3(2) for $p\ge9$.
- Exact finite checks: the cases $p\le8$ in Theorem 1(d) and Proposition 3, the agreement with
  brute-force endpoints for $S\le600$, and the first-collision table for $S\le600$.
- Not claimed: any formula for the first collision sum. The data give no reason to expect a
  closed form.
