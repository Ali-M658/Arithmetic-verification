---
title: '[1103.4372] Laplace-isospectral hyperbolic 2-orbifolds are representation-equivalent'
id: 11034372-doyle-rossetti-fulltext
tags:
- hyperbolic-pillow-heat-novelty-813161
- cone-orbifold
- orbifold-determinacy
- competing-priority-claim
- finite-spectral-data
- full-text-verified
created: '2026-08-09T08:45:09.630660Z'
updated: '2026-08-09T09:36:32.301624Z'
source: https://ar5iv.labs.arxiv.org/html/1103.4372
source_domain: ar5iv.labs.arxiv.org
fetched_at: '2026-08-09T08:45:09.630285Z'
fetch_provider: builtin
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Full text (ar5iv HTML) of Doyle & Rossetti, arXiv:1103.4372v2 (2014 streamlined
  version), never published in a journal (arXiv-only DataCite DOI 10.48550/arXiv.1103.4372).
  THEOREM 1 (verbatim, load-bearing): ''Let M be a compact hyperbolic 2-orbifold (not
  necessarily connected). The Laplace spectrum of M determines, and is determined
  by, the following data: 1. the volume; 2. the total length of the mirror boundary;
  3. the number of conepoints of each order, counting a mirror corner as half a conepoint
  of the corresponding order; 4. the number of closed geodesics of each length and
  orientability class [...].'' Proof uses the Selberg trace formula applied to the
  FULL Laplace spectrum (not a finite set of heat-trace coefficients) to recover the
  character of a linear representation of Isom(H^2) on the frame bundle; this is a
  full-spectrum, not finite-coefficient, determinacy result. Section 1 explicitly
  contrasts this with heat-trace approaches: citing Dryden-Gordon-Greenwald-Webb (arXiv:0805.3148),
  the authors state that DGGW''s short-time heat-trace asymptotics for general (variable-curvature,
  any-dimension) orbifolds, RESTRICTED to hyperbolic 2-orbifolds, ''don''t yield complete
  information about the singular set,'' though ''presumably it could be extracted
  using their approach, by looking at higher and higher terms in the asymptotic expansion''
  -- i.e., as of 2011/2014 Doyle-Rossetti flag full cone-order recovery from finitely
  many heat coefficients as an OPEN, unproven, and possibly infinite-coefficient-requiring
  question for hyperbolic 2-orbifolds. They also cite Dryden-Strohmaier (arXiv:math/0504571)
  as proving Theorem 1 for ORIENTABLE hyperbolic 2-orbifolds via wave-trace methods,
  and their own earlier arXiv:math/0605765 for orientable hyperbolic surfaces. Bibliography
  confirms DGGW citation as arXiv:0805.3148v1 [math.DG].'
---

*Suggested by [[11034372-laplace-isospectral-hyperbolic-2-orbifolds-are-representation-equivalen]] — full text needed for exact theorem statement*

[1103.4372] Laplace-isospectral hyperbolic 2-orbifolds are representation-equivalent
Laplace-isospectral hyperbolic 2-orbifolds are representation-equivalent
Peter G. Doyle
Dartmouth College.
Juan Pablo Rossetti
FaMAF-CIEM, Univ. Nac. Córdoba.
(Version 2.0 dated 9 April 2014
No Copyright
†
†
thanks:
The authors hereby waive all copyright
and related or neighboring rights to this work,
and dedicate it to the public domain.
This applies worldwide.
)
Abstract
Let
M
𝑀
M
be a compact hyperbolic
2
2
2
-orbifold
(not necessarily connected).
We show that
the spectrum of the Laplacian on functions on
M
𝑀
M
determines the following:
the volume;
the total length of the mirror boundary;
the number (properly counted) of conepoints of each order;
and the number (properly counted) of primitive closed geodesics
of each length and orientability class.
This means that Laplace-isospectral hyperbolic 2-orbifolds are
representation-equivalent, and hence strongly isospectral.
1
Statement
Let
M
𝑀
M
be a compact hyperbolic 2-orbifold (not necessarily connected).
Denote the eigenvalues of the Laplacian acting on functions on
M
𝑀
M
by
0
=
λ
0
≤
λ
1
≤
…
.
0
subscript
𝜆
0
subscript
𝜆
1
…
0=\lambda_{0}\leq\lambda_{1}\leq\ldots.
(Note that we don’t necessarily have
0
<
λ
1
0
subscript
𝜆
1
0<\lambda_{1}
because we aren’t assuming that
M
𝑀
M
is connected.)
We call the sequence
(
λ
0
,
λ
1
,
…
)
subscript
𝜆
0
subscript
𝜆
1
…
(\lambda_{0},\lambda_{1},\ldots)
the
Laplace spectrum
of
M
𝑀
M
.
If two spaces have the same Laplace spectrum we call them
Laplace-isospectral
.
(Note that we don’t simply call them ‘isospectral’,
because this term is used in different ways by different authors.)
Our goal here will be to prove:
Theorem 1
.
Let
M
𝑀
M
be a compact hyperbolic
2
2
2
-orbifold (not necessarily connected).
The Laplace spectrum of
M
𝑀
M
determines, and is determined by,
the following data:
1.
the volume;
2.
the total length of the mirror boundary;
3.
the number of conepoints of each order, counting a mirror corner
as half a conepoint of the corresponding order;
4.
the number of closed geodesics of each length and orientability class,
counting a geodesic running along the boundary as half
orientation-preserving and half orientation-reversing,
and counting the
k
𝑘
k
-fold iterate of a primitive geodesic
as worth
1
k
1
𝑘
\frac{1}{k}
of a primitive geodesic of the same length
and orientability.
Of course the
Laplace spectrum determines other data as well, for example the number
of connected components.
The data we list here determine those other data, since they
determine the spectrum.
Theorem
1
can be recast less picturesquely
as follows.
Associated to a 2-orbifold
M
𝑀
M
is a linear representation
ρ
M
¯
subscript
𝜌
¯
𝑀
\rho_{\bar{M}}
of
Isom
​
(
H
2
)
Isom
superscript
𝐻
2
\mathrm{Isom}(H^{2})
on functions on the frame bundle
M
¯
¯
𝑀
{\bar{M}}
of
M
𝑀
M
.
Associated to this representation is its character
χ
M
¯
subscript
𝜒
¯
𝑀
\chi_{\bar{M}}
,
a function on the set of conjugacy classes of
Isom
​
(
H
2
)
Isom
superscript
𝐻
2
\mathrm{Isom}(H^{2})
.
The geometrical data listed in Theorem
1
are just
a way of describing geometrically the information conveyed
by the character
χ
M
¯
subscript
𝜒
¯
𝑀
\chi_{\bar{M}}
.
The character determines
the Laplace spectrum of
M
𝑀
M
, and indeed, the spectrum of any other
natural operator.
Theorem
1
tells us
that for hyperbolic
2
2
2
-orbifolds,
we can go back the other way, and recover the character from the
Laplace spectrum.
From the character,
we get by general principles the linear equivalence class
of the representation
ρ
M
¯
subscript
𝜌
¯
𝑀
\rho_{\bar{M}}
,
and the spectrum of any natural operator on any natural bundle over
M
𝑀
M
.
Thus Laplace-isospectral hyperbolic
2
2
2
-orbifolds are
representation-equivalent and strongly isospectral.
We will discuss these matters further in section
7
below;
for now we concentrate on Theorem
1
.
2
Examples
In this section, we give examples of
the trade-offs between boundary and interior features that
are allowed for in the statement of Theorem
1
.
Boundary corners on one orbifold may appear as conepoints on the other,
while boundary geodesics may migrate to the interior.
These examples should clarify just what it is we will be trying to prove,
and why we can’t expect to prove something stronger.
The examples here will be obtained by glueing bunches of congruent
hyperbolic triangles.
The glueing patterns arise from transplantable pairs,
as described by
Buser et al.
[
2
]
.
Examples of trading boundary and interior geodesics are very common.
(Indeed, practically any pair of isospectral hyperbolic 2-orbifolds
with relecting boundary exhibit this phenomenon.)
A variation on the famous example
of Gordon, Webb, and Wolpert
[
9
]
yields a pair of planar hyperbolic 2-orbifolds
of types
∗
224236
absent
224236
*224236
and
∗
224623
absent
224623
*224623
,
shown in Figure
1
.
This is likely the simplest pair of isospectral hyperbolic polygons,
both in having the smallest number of vertices and having the smallest area.
Each member of the pair is glued together from
7
7
7
copies of
a prototype tile,
according to the glueing pattern labelled
7
3
subscript
7
3
7_{3}
in
[
2
]
.
The prototype tile is
a so-called
346
346
346
triangle
,
meaning a hyperbolic triangle with angles
π
/
3
𝜋
3
\pi/3
,
π
/
4
𝜋
4
\pi/4
,
π
/
6
𝜋
6
\pi/6
.
Figure 1:
The pair
∗
224236
absent
224236
*224236
,
∗
224623
absent
224623
*224623
.
There is no issue here with
geodesics passing through the interior of any of the triangles that
make up these two orbifolds:
These can be matched so as to preserve
length, orientability, and index of imprimitivity.
But when it comes to geodesics that run along the edges of the triangles,
whether along the mirror boundary or in the interior of the orbifold,
it is necessary to balance boundary geodesics on one orbifold against
interior geodesics on the other, as provided for in Theorem
1
.
To see this,
look at Figure
1
,
and count geodesics on the two sides.
Beware that boundary geodesics turn back at corners of even
order,
but continue along around the boundary at corners of odd order.
Beware also of the way interior geodesics bounce when they hit the
boundary.
The resulting counts are indicated in Table
1
.
The names ‘recto’ and ‘verso’ are short for ‘orientation-preserving’
and ‘orientation-reversing’,
in analogy with the names for the front and back of a printed page.
The table only shows lengths for which there is at least one imprimitive
geodesic.
Trade-offs between boundary and interior geodesics continue at multiples
of these lengths.
Geodesics for
∗
224236
absent
224236
*224236
:
boundary
interior
total
length
recto
verso
recto
verso
recto
verso
2
​
c
3
2
3
2
3
2
3
2
2
​
a
+
2
​
b
1
2
1
2
1
1
3
2
3
2
4
​
c
3
2
⋅
1
2
3
2
⋅
1
2
1
7
4
3
4
4
​
a
+
4
​
b
1
2
+
1
2
⋅
1
2
1
2
+
1
2
⋅
1
2
2
⋅
1
2
7
4
3
4
missing-subexpression
boundary
interior
total
length
recto
verso
recto
verso
recto
verso
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
2
𝑐
3
2
3
2
missing-subexpression
missing-subexpression
3
2
3
2
2
𝑎
2
𝑏
1
2
1
2
1
1
3
2
3
2
4
𝑐
⋅
3
2
1
2
⋅
3
2
1
2
1
missing-subexpression
7
4
3
4
4
𝑎
4
𝑏
1
2
⋅
1
2
1
2
1
2
⋅
1
2
1
2
⋅
2
1
2
missing-subexpression
7
4
3
4
\begin{array}[]{c||cc|cc|cc}\lx@intercol\hfil\hfil\lx@intercol&\lx@intercol\hfil\mbox{boundary}\hfil\lx@intercol&\lx@intercol\hfil\mbox{interior}\hfil\lx@intercol&\lx@intercol\hfil\mbox{total}\hfil\lx@intercol\\[5.69046pt]
\mbox{length}&\mbox{recto}&\mbox{verso}&\mbox{recto}&\mbox{verso}&\mbox{recto}&\mbox{verso}\\[5.69046pt]
\hline\cr 2c&\frac{3}{2}&\frac{3}{2}&&&\frac{3}{2}&\frac{3}{2}\\[5.69046pt]
2a+2b&\frac{1}{2}&\frac{1}{2}&1&1&\frac{3}{2}&\frac{3}{2}\\[5.69046pt]
4c&\frac{3}{2}\cdot\frac{1}{2}&\frac{3}{2}\cdot\frac{1}{2}&1&&\frac{7}{4}&\frac{3}{4}\\[5.69046pt]
4a+4b&\frac{1}{2}+\frac{1}{2}\cdot\frac{1}{2}&\frac{1}{2}+\frac{1}{2}\cdot\frac{1}{2}&2\cdot\frac{1}{2}&&\frac{7}{4}&\frac{3}{4}\\[5.69046pt]
\end{array}
Geodesics for
∗
224623
absent
224623
*224623
:
boundary
interior
total
length
recto
verso
recto
verso
recto
verso
2
​
c
1
2
1
2
1
1
3
2
3
2
2
​
a
+
2
​
b
3
2
3
2
3
2
3
2
4
​
c
1
2
+
1
2
⋅
1
2
1
2
+
1
2
⋅
1
2
2
⋅
1
2
7
4
3
4
4
​
a
+
4
​
b
3
2
⋅
1
2
3
2
⋅
1
2
1
7
4
3
4
missing-subexpression
boundary
interior
total
length
recto
verso
recto
verso
recto
verso
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
2
𝑐
1
2
1
2
1
1
3
2
3
2
2
𝑎
2
𝑏
3
2
3
2
missing-subexpression
missing-subexpression
3
2
3
2
4
𝑐
1
2
⋅
1
2
1
2
1
2
⋅
1
2
1
2
⋅
2
1
2
missing-subexpression
7
4
3
4
4
𝑎
4
𝑏
⋅
3
2
1
2
⋅
3
2
1
2
1
missing-subexpression
7
4
3
4
\begin{array}[]{c||cc|cc|cc}\lx@intercol\hfil\hfil\lx@intercol&\lx@intercol\hfil\mbox{boundary}\hfil\lx@intercol&\lx@intercol\hfil\mbox{interior}\hfil\lx@intercol&\lx@intercol\hfil\mbox{total}\hfil\lx@intercol\\[5.69046pt]
\mbox{length}&\mbox{recto}&\mbox{verso}&\mbox{recto}&\mbox{verso}&\mbox{recto}&\mbox{verso}\\[5.69046pt]
\hline\cr 2c&\frac{1}{2}&\frac{1}{2}&1&1&\frac{3}{2}&\frac{3}{2}\\[5.69046pt]
2a+2b&\frac{3}{2}&\frac{3}{2}&&&\frac{3}{2}&\frac{3}{2}\\[5.69046pt]
4c&\frac{1}{2}+\frac{1}{2}\cdot\frac{1}{2}&\frac{1}{2}+\frac{1}{2}\cdot\frac{1}{2}&2\cdot\frac{1}{2}&&\frac{7}{4}&\frac{3}{4}\\[5.69046pt]
4a+4b&\frac{3}{2}\cdot\frac{1}{2}&\frac{3}{2}\cdot\frac{1}{2}&1&&\frac{7}{4}&\frac{3}{4}\\[5.69046pt]
\end{array}
Table 1:
Counting geodesics.
Examples of trading corners for conepoints are not as common
as examples of trading boundary and interior geodesics,
but there are still plenty.
Figures
2
and
3
show how to construct a pair
6
∗
2232233
6
2232233
6*2232233
,
23
∗
22366
23
22366
23*22366
.
The transplantable pair used here is one of many found by John Conway
using the theory of quilts.
These will be described elsewhere, but there is no problem in verifying
transplantability here using the methods of
[
2
]
.
Note how the order-6 conepoint moves to the boundary going one way, while the
order-2 and order-3 conepoints move to the boundary going the other way.
Figure 2:
A transplantable pair of size 11.
Figure 3:
Replace the prototype equilateral triangle in Figure
2
by
a
366
366
366
triangle
so that six 3-vertices come together in the left-hand diagram.
This yields a Laplace-isospectral pair of hyperbolic 2-orbifolds
of types
6
∗
2232233
6
2232233
6*2232233
and
23
∗
22366
23
22366
23*22366
.
Note.
The groups associated to the prototype triangles in these two examples
(
346
346
346
and
366
366
366
) both belong to the
finite list of
arithmetic triangle groups
.
(Cf. Maclachlan and Reid
[
13
]
.)
The finite-index subgroup of a triangle group that belongs to an
orbifold obtained when the prototype triangle is arithmetic is
also arithmetic.
So our examples here are arithmetic.
3
Background
Huber
[
10
]
proved the result of Theorem
1
in the case of orientable hyperbolic 2-manifolds.
Huber used what would nowadays be seen as a version of the Selberg trace
formula,
which allows us to read off the lengths of geodesics from the spectrum
in a straight-forward way.
Doyle and Rossetti
[
5
]
extended the result to non-orientable hyperbolic 2-manifolds.
In the non-orientable case
we can’t simply read off the data about geodesics using the trace formula,
because of interference
between the spectral contributions of orientation-preserving
and orientation-reversing geodesics of the same length.
However, it turns out that
any possible scenario for matching spectral contributions would
require too many geodesics.
What we will show here is that,
as we indicated in
[
5
]
,
it is a short step from non-orientable surfaces to general
orbifolds.
The reason is that the Selberg formula permits us to read off the data about
orbifold features, just as Huber read off the data about geodesics in
the case of orientable manifolds.
Then we have only to check that there is still no scenario
for matching the spectral contributions of the geodesics.
There are other ways to approach showing that the Laplace spectrum determines
the data about orbifold features.
By looking at the wave trace,
Dryden and Strohmaier
[
8
]
proved the result of Theorem
1
for orientable hyperbolic 2-orbifolds.
While they did not consider non-orientable surfaces or orbifolds,
it seems likely that wave techniques could be used to
show that the Laplace spectrum determines all the orbifold data.
The argument would be essentially equivalent to the argument we give here,
only more complicated.
Another possible approach is via the heat equation.
By looking at short-time asymptotics of
the heat trace,
Dryden-Gordon-Greenwald-Webb
[
7
]
got information about the singular set of
general orbifolds
(for example, the volume of the reflecting boundary).
Their results
yield information about orbifolds of variable curvature,
and in any dimension.
Restricted to hyperbolic
2
2
2
-orbifolds,
the results they state
don’t yield complete information about the singular set.
All this information is there in the short-time asymptotics of the
heat trace, however,
and presumably it could be extracted using their approach,
by looking at higher and higher terms in the asymptotic expansion.
The beauty of the wave and heat approaches is that they can work in great
generality.
The Selberg method depends on having
spaces whose underlying geometry is homogeneous,
such as manifolds and orbifolds of constant curvature.
For studying such spaces,
it is a good bet that the Selberg method will
beat the wave and heat approaches.
Of course, the Selberg method can be used to treat the heat and wave
kernels;
the bet is that you will do better to consider a simpler kernel,
like the counting kernel that we use here.
Finally, just as it is true that hyperbolic manifolds whose geodesics match for
a sufficiently large number of lengths and twists
(in particular, all but a finite number)
must necessarily match for all lengths and twists
(cf. Kelmer
[
11
]
),
it is likely true on general principles that orbifolds with
matching geodesics must necessarily have matching orbifold features.
That would make Theorem
1
follow almost immediately from the methods
used to prove the corresponding result
[
5
]
about
2
2
2
-manifolds, without explicitly computing the contributions
of orbifold features to the spectrum, as we do here.
4
What we need from Selberg
Here we assemble what we will need from Selberg for the proof
of Theorem
1
.
All the ideas come from
Selberg
[
14
]
.
Let
G
=
Isom
​
(
H
2
)
𝐺
Isom
superscript
𝐻
2
G=\mathrm{Isom}(H^{2})
be
the group of isometries
of
H
2
superscript
𝐻
2
H^{2}
.
Note that
G
𝐺
G
has two components,
corresponding to orientation-preserving and orientation-reversing isometries.
A hyperbolic
2
2
2
-orbifold
can be written as a union of quotients of
H
2
superscript
𝐻
2
H^{2}
by discrete cocompact
subgroups
Γ
j
⊂
G
subscript
Γ
𝑗
𝐺
\Gamma_{j}\subset G
,
one for each connected component of
M
𝑀
M
:
M
=
∪
j
Γ
j
\
H
2
.
𝑀
subscript
𝑗
\
subscript
Γ
𝑗
superscript
𝐻
2
M=\cup_{j}\,\Gamma_{j}\backslash H^{2}.
We’ll denote by
F
​
(
Γ
j
)
𝐹
subscript
Γ
𝑗
F(\Gamma_{j})
a fundamental domain for
Γ
j
subscript
Γ
𝑗
\Gamma_{j}
.
In what follows, we could assume that
M
𝑀
M
is connected, and write
M
=
Γ
\
H
2
,
𝑀
\
Γ
superscript
𝐻
2
M=\Gamma\backslash H^{2},
because the extension to the disconnected case presents no difficulties.
We prefer not to do this, in part to combat the common prejudice against
disconnected spaces.
Define the
counting kernel
on
H
2
superscript
𝐻
2
H^{2}
by
c
​
(
x
,
y
;
s
)
=
{
1
,
d
​
(
x
,
y
)
≤
s
0
,
d
​
(
x
,
y
)
>
s
.
𝑐
𝑥
𝑦
𝑠
cases
1
𝑑
𝑥
𝑦
𝑠
0
𝑑
𝑥
𝑦
𝑠
c(x,y;s)=\left\{\begin{array}[]{ll}1,&d(x,y)\leq s\\
0,&d(x,y)>s\end{array}\right..
It tells when the hyperbolic distance
d
​
(
x
,
y
)
𝑑
𝑥
𝑦
d(x,y)
is at most
s
𝑠
s
.
Define the
counting trace
C
​
(
s
)
𝐶
𝑠
\displaystyle C(s)
=
\displaystyle=
∑
j
∫
F
​
(
Γ
j
)
∑
γ
∈
Γ
j
c
​
(
x
,
γ
​
x
;
t
)
​
d
​
x
subscript
𝑗
subscript
𝐹
subscript
Γ
𝑗
subscript
𝛾
subscript
Γ
𝑗
𝑐
𝑥
𝛾
𝑥
𝑡
𝑑
𝑥
\displaystyle\sum_{j}\int\limits_{F(\Gamma_{j})}\sum_{\gamma\in\Gamma_{j}}c(x,\gamma x;t)\,dx
=
\displaystyle=
∑
j
∫
F
​
(
Γ
j
)
#
​
{
γ
∈
Γ
j
:
d
​
(
x
,
γ
​
x
)
≤
s
}
​
𝑑
x
.
subscript
𝑗
subscript
𝐹
subscript
Γ
𝑗
#
conditional-set
𝛾
subscript
Γ
𝑗
𝑑
𝑥
𝛾
𝑥
𝑠
differential-d
𝑥
\displaystyle\sum_{j}\int\limits_{F(\Gamma_{j})}\#\{\gamma\in\Gamma_{j}:d(x,\gamma x)\leq s\}\,dx.
The counting trace
tells (after dividing by the volume of
M
𝑀
M
)
the average number of broken geodesic loops on
M
𝑀
M
of length at most
s
𝑠
s
,
The reason for the name ‘counting trace’ is that formally,
C
​
(
s
)
𝐶
𝑠
C(s)
is the trace of the linear operator
L
s
subscript
𝐿
𝑠
L_{s}
whose kernel is the counting kernel
c
​
(
x
,
y
;
s
)
𝑐
𝑥
𝑦
𝑠
c(x,y;s)
pushed down to
M
𝑀
M
.
L
s
subscript
𝐿
𝑠
L_{s}
associates to a function
f
:
M
→
R
:
𝑓
→
𝑀
𝑅
f:M\to R
the function whose value at
x
∈
M
𝑥
𝑀
x\in M
is the integral over a ball of radius
s
𝑠
s
of the lift of
f
𝑓
f
to the universal cover
H
2
superscript
𝐻
2
H^{2}
.
L
s
subscript
𝐿
𝑠
L_{s}
is not a actually trace class operator, because of the discontinuity of
the counting kernel,
but our expression for
C
​
(
s
)
𝐶
𝑠
C(s)
is still well-defined.
We will need the following two propositions,
which correspond to the two sides of the Selberg trace formula.
Proposition 1
.
The Laplace spectrum determines the counting trace.
∎
absent
\quad\qed
Let
Cl
​
(
γ
,
Γ
)
Cl
𝛾
Γ
\mathrm{Cl}(\gamma,\Gamma)
denote the conjugacy class
of
γ
𝛾
\gamma
in
Γ
Γ
\Gamma
,
and let
Z
​
(
γ
,
Γ
)
Z
𝛾
Γ
\mathrm{Z}(\gamma,\Gamma)
denote the centralizer.
We have the usual one-to-one correspondence between
the set of cosets
Z
​
(
γ
,
Γ
)
\
Γ
\
Z
𝛾
Γ
Γ
\mathrm{Z}(\gamma,\Gamma)\backslash\Gamma
and the conjugacy class
Cl
​
(
γ
,
Γ
)
Cl
𝛾
Γ
\mathrm{Cl}(\gamma,\Gamma)
,
where to the coset
Z
​
(
γ
,
Γ
)
​
δ
Z
𝛾
Γ
𝛿
\mathrm{Z}(\gamma,\Gamma)\delta
we associate
the conjugate
δ
−
1
​
γ
​
δ
superscript
𝛿
1
𝛾
𝛿
\delta^{-1}\gamma\delta
.
Proposition 2
.
The counting trace can be expressed as a sum of contributions from
conjugacy classes of
Γ
Γ
\Gamma
:
C
​
(
s
)
=
∑
j
∑
Cl
​
(
γ
,
Γ
j
)
Vol
​
(
{
x
∈
F
​
(
Z
​
(
γ
,
Γ
j
)
)
:
d
​
(
x
,
γ
​
x
)
≤
s
}
)
.
∎
𝐶
𝑠
subscript
𝑗
subscript
Cl
𝛾
subscript
Γ
𝑗
Vol
conditional-set
𝑥
𝐹
Z
𝛾
subscript
Γ
𝑗
𝑑
𝑥
𝛾
𝑥
𝑠
C(s)=\sum_{j}\sum_{\mathrm{Cl}(\gamma,\Gamma_{j})}\mathrm{Vol}(\{x\in F(\mathrm{Z}(\gamma,\Gamma_{j})):d(x,\gamma x)\leq s\}).\quad\qed
The virtue of this proposition is that we can evaluate the summands
using simple hyperbolic trigonometry.
5
Outline
The counting trace
C
​
(
s
)
𝐶
𝑠
C(s)
is built up of contributions from the conjugacy classes
of
Isom
​
(
H
2
)
Isom
superscript
𝐻
2
\mathrm{Isom}(H^{2})
.
The contribution from the identity is independent of
s
𝑠
s
,
and equal to the volume of
M
𝑀
M
.
The remaining conjugacy classes are of four kinds:
reflections, rotations, translations, and glide reflections.
Their contributions all vanish for
s
=
0
𝑠
0
s=0
, which means that
C
​
(
0
)
𝐶
0
C(0)
is the
volume of
M
𝑀
M
.
Translations and glide reflections make no contribution for
s
𝑠
s
smaller
than the length of the shortest closed geodesic,
so for small
s
𝑠
s
the only contributions are from the identity,
reflections, and rotations.
Begin by reading off the volume
C
​
(
0
)
𝐶
0
C(0)
,
and subtracting this constant from
C
​
(
s
)
𝐶
𝑠
C(s)
.
In what is left,
reflections make a contribution of first order in
s
𝑠
s
, proportional
to the total length of the mirror boundary.
Rotations contribute only to second order,
so we can read off the length of the mirror boundary, subtract out
its contribution,
and what is left is (for small
s
𝑠
s
)
entirely the result of rotations.
A simple computation now
shows that the contributions of
rotations through different angles are linearly independent.
This allows us to read off the orders of the conepoints,
and subtract out their contributions.
Once we’ve zapped the contributions of the identity,
reflections, and rotations,
what is left of the counting trace vanishes identically for small
s
𝑠
s
,
and overall is entirely the result of
translations and glide reflections,
corresponding in the quotient to closed geodesics.
Here we run into the
main
difficulty in the proof,
which is that the contributions of orientation-preserving
and orientation-reversing geodesics of a given length
are not linearly independent.
Indeed, they are proportional, with a constant of proportionality
depending on the length of the geodesic.
So we can’t simply read off these lengths.
Fortunately, we have already established that the spectrum determines
the lengths and twists of geodesics
for hyperbolic 2-manifolds,
(See Doyle and Rossetti
[
5
]
.)
and the argument carries over directly to the orbifold case,
providing we take care to count geodesics along the boundary as
half orientation-preserving and half orientation-reversing.
6
Details
Denote by
R
𝑅
R
the combined length of all reflecting boundaries.
Lemma 1
.
The combined contribution of the reflecting boundaries to the
counting trace
C
​
(
s
)
𝐶
𝑠
C(s)
is
R
​
sinh
⁡
s
2
.
𝑅
𝑠
2
R\sinh\frac{s}{2}.
Proof.
Let
ρ
∈
Γ
j
𝜌
subscript
Γ
𝑗
\rho\in\Gamma_{j}
be a reflection.
There are two possibilities for
Z
​
(
ρ
,
Γ
j
)
\
H
2
\
Z
𝜌
subscript
Γ
𝑗
superscript
𝐻
2
\mathrm{Z}(\rho,\Gamma_{j})\backslash H^{2}
:
a funnel or a planar domain.
(See Figure
4
.)
Figure 4:
Possible quotients for the centralizer of a reflection.
The left shows a funnel, the right shows a planar domain.
In either case, the contribution to
C
​
(
s
)
𝐶
𝑠
C(s)
is
R
ρ
​
sinh
⁡
s
2
subscript
𝑅
𝜌
𝑠
2
R_{\rho}\sinh\frac{s}{2}
,
where
R
ρ
subscript
𝑅
𝜌
R_{\rho}
is the portion of
R
𝑅
R
attributable to
Cl
​
(
ρ
,
Γ
j
)
Cl
𝜌
subscript
Γ
𝑗
\mathrm{Cl}(\rho,\Gamma_{j})
,
because this measures points in the quotient that are within
s
2
𝑠
2
\frac{s}{2}
of the axis of
ρ
𝜌
\rho
, and hence within
s
𝑠
s
of their images under the
reflection
ρ
𝜌
\rho
.
(See Figure
5
.)
Figure 5:
The contribution of a reflection to the counting trace.
Summing over the conjugacy classes of reflections in
all the groups
Γ
j
subscript
Γ
𝑗
\Gamma_{j}
gives
R
​
sinh
⁡
s
2
𝑅
𝑠
2
R\sinh\frac{s}{2}
.
∎
absent
\quad\qed
Now we turn to conjugacy classes of rotations.
Each such is associated to a unique conepoint or boundary corner.
From a conepoint of order
n
𝑛
n
we get
n
−
1
𝑛
1
n-1
rotations
through angles
2
​
π
​
k
n
2
𝜋
𝑘
𝑛
\frac{2\pi k}{n}
,
k
=
1
,
…
,
n
−
1
𝑘
1
…
𝑛
1
k=1,\ldots,n-1
.
For each such rotation
γ
𝛾
\gamma
the centralizer
Z
​
(
γ
,
Γ
j
)
Z
𝛾
subscript
Γ
𝑗
\mathrm{Z}(\gamma,\Gamma_{j})
is cyclic of order
n
𝑛
n
,
consisting of just these
n
−
1
𝑛
1
n-1
rotations, together with the identity.
The quotient
Z
​
(
γ
,
Γ
j
)
\
H
2
\
Z
𝛾
subscript
Γ
𝑗
superscript
𝐻
2
\mathrm{Z}(\gamma,\Gamma_{j})\backslash H^{2}
is
an infinite cone of cone angle
2
​
π
n
2
𝜋
𝑛
\frac{2\pi}{n}
.
For a boundary corner of angle
π
n
𝜋
𝑛
\frac{\pi}{n}
the centralizer is a dihedral group of order
2
​
n
2
𝑛
2n
,
and the quotient is an infinite sector of angle
π
n
𝜋
𝑛
\frac{\pi}{n}
.
This quotient is half of a cone of angle
π
n
𝜋
𝑛
\frac{\pi}{n}
,
and it should be clear that the contribution to
C
​
(
s
)
𝐶
𝑠
C(s)
of
rotations associated to a boundary corner is just half what it is for
a conepoint—which is why a boundary corner counts as half a cone-point.
So we can forget about boundary corners, and consider just conepoints.
Denote by
g
n
​
(
s
)
subscript
𝑔
𝑛
𝑠
g_{n}(s)
the total contribution to the
counting trace of a conepoint of order
n
𝑛
n
.
This contribution is the sum of the contributions of
the
n
−
1
𝑛
1
n-1
non-trivial conjugacy classes of rotations
associated to the conepoint.
Denote the contribution of the conjugacy class of the rotation through
angle
2
​
π
​
k
n
2
𝜋
𝑘
𝑛
\frac{2\pi k}{n}
by
g
k
,
n
​
(
s
)
subscript
𝑔
𝑘
𝑛
𝑠
g_{k,n}(s)
.
Lemma 2
.
The total contribution of a conepoint of order
n
𝑛
n
to the counting trace
is
g
n
​
(
s
)
=
∑
k
=
1
n
g
k
,
n
​
(
s
)
subscript
𝑔
𝑛
𝑠
superscript
subscript
𝑘
1
𝑛
subscript
𝑔
𝑘
𝑛
𝑠
g_{n}(s)=\sum_{k=1}^{n}g_{k,n}(s)
,
where
g
k
,
n
​
(
s
)
=
1
n
​
f
2
​
π
​
k
n
​
(
s
)
,
subscript
𝑔
𝑘
𝑛
𝑠
1
𝑛
subscript
𝑓
2
𝜋
𝑘
𝑛
𝑠
g_{k,n}(s)=\frac{1}{n}f_{\frac{2\pi k}{n}}(s),
where
f
θ
​
(
s
)
=
2
​
π
​
(
1
+
sinh
2
⁡
s
2
sin
2
⁡
θ
2
−
1
)
.
subscript
𝑓
𝜃
𝑠
2
𝜋
1
superscript
2
𝑠
2
superscript
2
𝜃
2
1
f_{\theta}(s)=2\pi\left(\sqrt{1+\frac{\sinh^{2}\frac{s}{2}}{\sin^{2}\frac{\theta}{2}}}-1\right).
Proof.
It should be clear that
g
k
,
n
​
(
s
)
=
1
n
​
f
2
​
π
​
k
n
​
(
s
)
,
subscript
𝑔
𝑘
𝑛
𝑠
1
𝑛
subscript
𝑓
2
𝜋
𝑘
𝑛
𝑠
g_{k,n}(s)=\frac{1}{n}f_{\frac{2\pi k}{n}}(s),
where
f
θ
​
(
s
)
subscript
𝑓
𝜃
𝑠
f_{\theta}(s)
is the area
2
​
π
​
(
cosh
⁡
r
−
1
)
2
𝜋
𝑟
1
2\pi(\cosh r-1)
of a hyperbolic disk of such a radius
r
𝑟
r
that
a chord of length
s
𝑠
s
subtends angle
θ
𝜃
\theta
.
(A fundamental domain for the cone hits a fraction
1
n
1
𝑛
\frac{1}{n}
of
any disk about the center of rotation.)
We just have to make sure that we have the correct formula for
f
θ
subscript
𝑓
𝜃
f_{\theta}
.
The quantities
r
,
θ
,
s
𝑟
𝜃
𝑠
r,\theta,s
satisfy
sinh
⁡
r
=
sinh
⁡
s
2
sin
⁡
θ
2
.
𝑟
𝑠
2
𝜃
2
\sinh r=\frac{\sinh\frac{s}{2}}{\sin\frac{\theta}{2}}.
(See Figure
6
.)
Figure 6:
The circle whose chord of length
s
𝑠
s
subtends angle
θ
𝜃
\theta
Thus
f
θ
​
(
s
)
subscript
𝑓
𝜃
𝑠
\displaystyle f_{\theta}(s)
=
\displaystyle=
2
​
π
​
(
cosh
⁡
r
−
1
)
2
𝜋
𝑟
1
\displaystyle 2\pi(\cosh r-1)
=
\displaystyle=
2
​
π
​
(
1
+
sinh
2
⁡
r
−
1
)
2
𝜋
1
superscript
2
𝑟
1
\displaystyle 2\pi\left(\sqrt{1+\sinh^{2}r}-1\right)
=
\displaystyle=
2
​
π
​
(
1
+
sinh
2
⁡
s
2
sin
2
⁡
θ
2
−
1
)
.
∎
2
𝜋
1
superscript
2
𝑠
2
superscript
2
𝜃
2
1
\displaystyle 2\pi\left(\sqrt{1+\frac{\sinh^{2}\frac{s}{2}}{\sin^{2}\frac{\theta}{2}}}-1\right).\quad\qed
Hopefully it will seem absolutely incredible that there might
be any non-trivial linear relation between these functions
f
θ
subscript
𝑓
𝜃
f_{\theta}
.
There isn’t:
Lemma 3
.
The functions
f
θ
,
0
<
θ
≤
π
subscript
𝑓
𝜃
0
𝜃
𝜋
f_{\theta},0<\theta\leq\pi
are linearly independent:
No non-trivial linear combination of any finite subset
of these functions vanishes identically on any interval
0
<
s
<
S
0
𝑠
𝑆
0<s<S
.
Proof.
It suffices to show linear independence of the family of functions
1
+
a
​
u
−
1
1
𝑎
𝑢
1
\sqrt{1+au}-1
,
1
<
a
<
∞
1
𝑎
1<a<\infty
, on all intervals
0
<
u
<
U
0
𝑢
𝑈
0<u<U
.
(Set
u
=
sinh
2
⁡
t
2
𝑢
superscript
2
𝑡
2
u=\sinh^{2}\frac{t}{2}
and
a
=
1
sin
2
⁡
θ
2
𝑎
1
superscript
2
𝜃
2
a=\frac{1}{\sin^{2}\frac{\theta}{2}}
.)
Actually, functions of this form remain independent when
a
𝑎
a
is allowed
to range throughout the punctured complex plane
𝐂
−
{
0
}
𝐂
0
\mathbf{C}-\{0\}
,
and not just over the specified
real interval.
A quick way to see this is to write in Taylor series
g
​
(
u
)
𝑔
𝑢
\displaystyle g(u)
=
\displaystyle=
1
+
u
−
1
1
𝑢
1
\displaystyle\sqrt{1+u}-1
=
\displaystyle=
1
1
!
​
(
1
2
)
​
u
+
1
2
!
​
(
1
2
)
​
(
−
1
2
)
​
u
2
+
1
3
!
​
(
1
2
)
​
(
−
1
2
)
​
(
−
3
2
)
​
u
3
+
…
1
1
1
2
𝑢
1
2
1
2
1
2
superscript
𝑢
2
1
3
1
2
1
2
3
2
superscript
𝑢
3
…
\displaystyle\frac{1}{1!}\left(\frac{1}{2}\right)u+\frac{1}{2!}\left(\frac{1}{2}\right)\left(\frac{-1}{2}\right)u^{2}+\frac{1}{3!}\left(\frac{1}{2}\right)\left(\frac{-1}{2}\right)\left(\frac{-3}{2}\right)u^{3}+\ldots
=
\displaystyle=
b
1
​
u
+
b
2
2
​
u
2
+
b
3
6
​
u
3
+
…
,
subscript
𝑏
1
𝑢
subscript
𝑏
2
2
superscript
𝑢
2
subscript
𝑏
3
6
superscript
𝑢
3
…
\displaystyle b_{1}u+\frac{b_{2}}{2}u^{2}+\frac{b_{3}}{6}u^{3}+\ldots,
where all we will need is that
b
1
,
b
2
,
…
≠
0
.
subscript
𝑏
1
subscript
𝑏
2
…
0
b_{1},b_{2},\ldots\neq 0.
If a linear combination
∑
i
=
1
n
c
i
​
g
​
(
a
i
​
u
)
superscript
subscript
𝑖
1
𝑛
subscript
𝑐
𝑖
𝑔
subscript
𝑎
𝑖
𝑢
\sum_{i=1}^{n}c_{i}g(a_{i}u)
is to vanish on
0
<
u
<
U
0
𝑢
𝑈
0<u<U
, then all its derivatives
must vanish at
u
=
0
𝑢
0
u=0
:
∑
i
=
1
n
c
i
​
a
i
k
​
b
k
=
0
,
k
=
1
,
2
,
…
.
formulae-sequence
superscript
subscript
𝑖
1
𝑛
subscript
𝑐
𝑖
superscript
subscript
𝑎
𝑖
𝑘
subscript
𝑏
𝑘
0
𝑘
1
2
…
\sum_{i=1}^{n}c_{i}a_{i}^{k}b_{k}=0,\quad k=1,2,\ldots.
(We ignore the constant term because all the functions involved here
vanish at
u
=
0
𝑢
0
u=0
.)
Dividing by
b
k
subscript
𝑏
𝑘
b_{k}
gives
∑
i
=
1
n
c
i
​
a
i
k
=
0
,
k
=
1
,
2
,
…
.
formulae-sequence
superscript
subscript
𝑖
1
𝑛
subscript
𝑐
𝑖
superscript
subscript
𝑎
𝑖
𝑘
0
𝑘
1
2
…
\sum_{i=1}^{n}c_{i}a_{i}^{k}=0,\quad k=1,2,\ldots.
Could this system of equations for
c
1
,
…
,
c
n
subscript
𝑐
1
…
subscript
𝑐
𝑛
c_{1},\ldots,c_{n}
have a non-trivial solution?
If so, then the subsystem consisting of only the first
n
𝑛
n
of these equations would have a non-trivial solution:
∑
i
=
1
n
c
i
​
a
i
k
=
0
,
k
=
1
,
…
,
n
.
formulae-sequence
superscript
subscript
𝑖
1
𝑛
subscript
𝑐
𝑖
superscript
subscript
𝑎
𝑖
𝑘
0
𝑘
1
…
𝑛
\sum_{i=1}^{n}c_{i}a_{i}^{k}=0,\quad k=1,\ldots,n.
Let
d
i
=
c
i
​
a
i
subscript
𝑑
𝑖
subscript
𝑐
𝑖
subscript
𝑎
𝑖
d_{i}=c_{i}a_{i}
, so that
∑
i
=
1
n
d
i
​
a
i
k
−
1
=
0
,
k
=
1
,
…
,
n
.
formulae-sequence
superscript
subscript
𝑖
1
𝑛
subscript
𝑑
𝑖
superscript
subscript
𝑎
𝑖
𝑘
1
0
𝑘
1
…
𝑛
\sum_{i=1}^{n}d_{i}a_{i}^{k-1}=0,\quad k=1,\ldots,n.
The
n
𝑛
n
-by-
n
𝑛
n
matrix
(
a
i
k
−
1
)
1
≤
i
,
j
≤
n
subscript
superscript
subscript
𝑎
𝑖
𝑘
1
formulae-sequence
1
𝑖
𝑗
𝑛
(a_{i}^{k-1})_{1\leq i,j\leq n}
of this system of linear equations is a
Vandermonde matrix, with determinant
∏
i
<
j
(
a
i
−
a
j
)
subscript
product
𝑖
𝑗
subscript
𝑎
𝑖
subscript
𝑎
𝑗
\prod_{i<j}(a_{i}-a_{j})
,
so as long as the
a
i
subscript
𝑎
𝑖
a_{i}
are distinct the system has no non-trivial
solution.
∎
absent
\quad\qed
Note.
In appealing to the fact
that none of the derivatives of
1
+
u
1
𝑢
\sqrt{1+u}
happen to vanish
at
u
=
0
𝑢
0
u=0
,
we are seizing upon an accidental feature of the problem.
A more robust proof can be based on the following lemma.
Lemma 4
.
Let
f
​
(
z
)
=
c
k
​
x
k
𝑓
𝑧
subscript
𝑐
𝑘
superscript
𝑥
𝑘
f(z)=c_{k}x^{k}
be analytic at
0
0
.
Suppose
g
​
(
z
)
=
∑
i
=
1
n
a
i
​
f
​
(
α
i
​
z
)
𝑔
𝑧
superscript
subscript
𝑖
1
𝑛
subscript
𝑎
𝑖
𝑓
subscript
𝛼
𝑖
𝑧
g(z)=\sum_{i=1}^{n}a_{i}f(\alpha_{i}z)
with all
|
α
i
|
<
1
subscript
𝛼
𝑖
1
|\alpha_{i}|<1
.
If the Taylor series for
f
𝑓
f
and
g
𝑔
g
agree then
f
𝑓
f
is a polynomial.
Proof.
We must have
∑
i
=
1
n
a
i
​
α
i
k
=
1
superscript
subscript
𝑖
1
𝑛
subscript
𝑎
𝑖
superscript
subscript
𝛼
𝑖
𝑘
1
\sum_{i=1}^{n}a_{i}\alpha_{i}^{k}=1
for any
k
𝑘
k
for which
c
k
≠
0
subscript
𝑐
𝑘
0
c_{k}\neq 0
.
If
f
𝑓
f
is not a polynomial,
we can choose
k
𝑘
k
big enough so that the left side is small,
and arrive at a contradiction.
∎
absent
\quad\qed
Note.
It would be interesting to know the extent to which
this result still holds without the requirement that
a
i
<
1
subscript
𝑎
𝑖
1
a_{i}<1
.
It will suffice to understand the case where all
|
α
i
|
=
1
subscript
𝛼
𝑖
1
|\alpha_{i}|=1
.
As an example, if we take
f
​
(
z
)
=
z
+
z
2
1
−
z
3
=
z
+
z
2
+
z
4
+
z
5
+
z
7
+
z
8
+
…
𝑓
𝑧
𝑧
superscript
𝑧
2
1
superscript
𝑧
3
𝑧
superscript
𝑧
2
superscript
𝑧
4
superscript
𝑧
5
superscript
𝑧
7
superscript
𝑧
8
…
f(z)=\frac{z+z^{2}}{1-z^{3}}=z+z^{2}+z^{4}+z^{5}+z^{7}+z^{8}+\ldots
we can write
f
​
(
z
)
=
−
f
​
(
ω
​
z
)
−
f
​
(
ω
2
​
z
)
𝑓
𝑧
𝑓
𝜔
𝑧
𝑓
superscript
𝜔
2
𝑧
f(z)=-f(\omega z)-f(\omega^{2}z)
where
ω
=
e
2
​
π
​
i
/
3
𝜔
superscript
𝑒
2
𝜋
𝑖
3
\omega=e^{2\pi i/3}
is a cube root of unity.
Are there examples where the
α
i
subscript
𝛼
𝑖
\alpha_{i}
are not roots of unity?
Completion of the proof of Theorem
1
.
Subtract from
C
​
(
s
)
𝐶
𝑠
C(s)
from the counting trace the volume
C
​
(
0
)
𝐶
0
C(0)
and the contributions of the reflectors.
Because of the linear independence of the functions
f
θ
subscript
𝑓
𝜃
f_{\theta}
,
we can identify the number of conepoints of highest order.
(It should go without saying that this includes the half-conepoints
at boundary corners.)
Subtract out their combined contribution from
C
​
(
s
)
𝐶
𝑠
C(s)
.
Now we can identify the number of conepoints of the next highest order,
and subtract out their contribution.
Proceed until all conepoint contributions
have been removed.
What remains arises from the closed geodesics.
In
[
5
]
,
we showed that if
M
𝑀
M
is a manifold,
the characteristics of the closed geodesics are determined
by the counting trace,
and hence by the spectrum.
The reason is that
any possible scenario for a counterexample requires
the participation of too many geodesics.
Roughly speaking, any balance between primitive orientation-reversing and
orientation-preserving geodesics
gets destroyed when you look at imprimitive iterates of the geodesics,
so you have to keep adding new geodesics to compensate.
The proof
in
[
5
]
carries over here essentially without change.
∎
absent
\quad\qed
7
Implications
Let
G
=
Isom
​
(
H
2
)
≃
P
​
G
​
L
​
(
2
,
𝐑
)
𝐺
Isom
superscript
𝐻
2
similar-to-or-equals
𝑃
𝐺
𝐿
2
𝐑
G=\mathrm{Isom}(H^{2})\simeq PGL(2,\mathbf{R})
denote the group of isometries of
H
2
superscript
𝐻
2
H^{2}
.
Note that
G
𝐺
G
has two connected components,
corresponding to orientation-preserving and orientation-reversing isometries.
A hyperbolic
2
2
2
-orbifold
M
𝑀
M
can be written as a union of quotients of
H
2
superscript
𝐻
2
H^{2}
by discrete cocompact
subgroups
Γ
j
⊂
G
subscript
Γ
𝑗
𝐺
\Gamma_{j}\subset G
,
one for each connected component of
M
𝑀
M
:
M
=
∪
j
Γ
j
\
H
2
.
𝑀
subscript
𝑗
\
subscript
Γ
𝑗
superscript
𝐻
2
M=\cup_{j}\,\Gamma_{j}\backslash H^{2}.
M
𝑀
M
is naturally covered by
M
¯
=
∪
j
Γ
j
\
G
.
¯
𝑀
subscript
𝑗
\
subscript
Γ
𝑗
𝐺
{\bar{M}}=\cup_{j}\,\Gamma_{j}\backslash G.
M
¯
¯
𝑀
{\bar{M}}
is the bundle of all orthonormal frames of
M
𝑀
M
, not just
those that have a particular orientation;
every point
x
𝑥
x
of
M
𝑀
M
is covered by two disjoint circles in
M
¯
¯
𝑀
{\bar{M}}
,
corresponding to the two orientation classes of frames of the tangent
space
T
x
​
M
subscript
𝑇
𝑥
𝑀
T_{x}M
.
Note that there will be two connected components of
M
¯
¯
𝑀
{\bar{M}}
for each orientable component of
M
𝑀
M
, and one for each non-orientable
component,
because dragging a frame around an orientation-reversing loop
(e.g. one that simply bumps off a mirror boundary) will take you from
one orientation class of frames to the other.
G
𝐺
G
acts naturally on the right on
M
¯
¯
𝑀
{\bar{M}}
,
and hence on
L
2
​
(
M
¯
)
superscript
𝐿
2
¯
𝑀
L^{2}({\bar{M}})
.
This linear representation of
G
𝐺
G
is analogous to the matrix representation
of a finite permutation group.
A finite permutation representation
ρ
𝜌
\rho
is determined up to
linear equivalence by its character
χ
𝜒
\chi
,
with
χ
​
(
g
)
=
tr
​
ρ
​
(
g
)
𝜒
𝑔
tr
𝜌
𝑔
\chi(g)=\mathrm{tr}\rho(g)
counting the fixed points of
g
𝑔
g
.
The situation here should be exactly analogous,
the only question being exactly how to define the character.
The answer comes from the Selberg trace formula.
For now let’s extend the discussion to an arbitrary unimodular Lie group
G
𝐺
G
, possibly disconnected.
Let
Γ
<
G
Γ
𝐺
\Gamma<G
be a discrete subgroup with compact quotient
M
¯
=
Γ
\
G
¯
𝑀
\
Γ
𝐺
{\bar{M}}=\Gamma\backslash G
.
(Notice that we make no mention here of
M
𝑀
M
, though in the intended
application
M
¯
¯
𝑀
{\bar{M}}
will arise from a homogeneous quotient
M
=
Γ
\
G
/
K
𝑀
\
Γ
𝐺
𝐾
M=\Gamma\backslash G/K
.)
Denote by
Cl
​
(
g
,
G
)
Cl
𝑔
𝐺
\mathrm{Cl}(g,G)
the conjugacy class of
g
𝑔
g
in
G
𝐺
G
,
and by
Z
​
(
g
,
G
)
Z
𝑔
𝐺
\mathrm{Z}(g,G)
the centralizer of
g
𝑔
g
in
G
𝐺
G
.
Introduce Haar measure
ρ
g
superscript
𝜌
𝑔
\rho^{g}
on
Z
G
​
(
g
)
subscript
𝑍
𝐺
𝑔
Z_{G}(g)
,
normalized in a consistent (i.e.,
G
𝐺
G
-equivariant) way.
Attribute to
Cl
​
(
γ
,
Γ
)
Cl
𝛾
Γ
\mathrm{Cl}(\gamma,\Gamma)
the
weight
ρ
γ
​
(
Z
​
(
γ
,
Γ
)
\
Z
​
(
γ
,
G
)
)
superscript
𝜌
𝛾
\
Z
𝛾
Γ
Z
𝛾
𝐺
\rho^{\gamma}(\mathrm{Z}(\gamma,\Gamma)\backslash\mathrm{Z}(\gamma,G))
,
and define the
character
χ
M
¯
subscript
𝜒
¯
𝑀
\chi_{\bar{M}}
to be the function associating
to
g
∈
G
𝑔
𝐺
g\in G
the total weight of all conjugacy classes
Cl
​
(
γ
,
Γ
)
Cl
𝛾
Γ
\mathrm{Cl}(\gamma,\Gamma)
for which
Cl
​
(
γ
,
G
)
=
Cl
​
(
g
,
G
)
Cl
𝛾
𝐺
Cl
𝑔
𝐺
\mathrm{Cl}(\gamma,G)=\mathrm{Cl}(g,G)
.
Extend the definition of
χ
M
¯
subscript
𝜒
¯
𝑀
\chi_{\bar{M}}
to
M
¯
=
∪
j
Γ
j
\
G
¯
𝑀
subscript
𝑗
\
subscript
Γ
𝑗
𝐺
{\bar{M}}=\cup_{j}\,\Gamma_{j}\backslash G
by linearity.
As in the finite case, the character is a
central function
,
which means that
χ
M
¯
​
(
g
​
h
)
=
χ
M
¯
​
(
h
​
g
)
subscript
𝜒
¯
𝑀
𝑔
ℎ
subscript
𝜒
¯
𝑀
ℎ
𝑔
\chi_{\bar{M}}(gh)=\chi_{\bar{M}}(hg)
for all
g
,
h
∈
G
𝑔
ℎ
𝐺
g,h\in G
,
or what is the same,
χ
M
¯
​
(
g
)
subscript
𝜒
¯
𝑀
𝑔
\chi_{\bar{M}}(g)
depends only on the conjugacy class
Cl
​
(
g
,
G
)
Cl
𝑔
𝐺
\mathrm{Cl}(g,G)
.
In analogy to the finite case,
we can think of
χ
M
¯
​
(
g
)
subscript
𝜒
¯
𝑀
𝑔
\chi_{\bar{M}}(g)
as measuring (in appropriate units) the size of the
fixed point set
{
x
∈
M
¯
:
x
​
g
=
x
}
conditional-set
𝑥
¯
𝑀
𝑥
𝑔
𝑥
\{x\in{\bar{M}}:xg=x\}
.
Proposition 3
(Berard
[
1
]
)
.
The character
χ
M
¯
subscript
𝜒
¯
𝑀
\chi_{\bar{M}}
determines the representation
L
2
​
(
M
¯
)
superscript
𝐿
2
¯
𝑀
L^{2}({\bar{M}})
up to linear equivalence.
Proof.
Using a version of Selberg’s trace formula
we can write the trace of the integral operator associated to any
smooth function of compact support on
G
𝐺
G
in terms of the values of
the character
χ
M
¯
subscript
𝜒
¯
𝑀
\chi_{\bar{M}}
.
(Cf. Wallach
[
16
, Theorem 2.1]
,
Selberg
[
14
, (2.10) on p. 66]
.)
By standard representation theory,
these traces determine the representation.
For details, see Bérard
[
1
]
.
∎
absent
\quad\qed
Proposition 4
(DeTurck-Gordon
[
4
]
)
.
The character
χ
M
¯
subscript
𝜒
¯
𝑀
\chi_{\bar{M}}
determines the trace of any natural
operator on any natural vector bundle over
M
𝑀
M
.
Proof.
Selberg again.
∎
absent
\quad\qed
With this preparation, we have the following corollaries of
Theorem
1
.
Corollary 1
(Character is determined)
.
The Laplace spectrum of a hyperbolic 2-orbifold
M
𝑀
M
(not necessarily connected)
determines
the character
χ
M
¯
subscript
𝜒
¯
𝑀
\chi_{\bar{M}}
.
∎
absent
\quad\qed
Corollary 2
(Representation-equivalence)
.
Laplace-isospectral hyperbolic
2
2
2
-orbifolds
(not necessarily connected)
determine
equivalent representations of
Isom
​
(
H
2
)
Isom
superscript
𝐻
2
\mathrm{Isom}(H^{2})
.
∎
absent
\quad\qed
Corollary 3
(Strong isospectrality)
.
If two compact hyperbolic 2-orbifolds
(not necessarily connected)
are Laplace-isospectral
then they have the same spectrum for any natural operator acting on
sections of any natural bundle.
∎
absent
\quad\qed
8
Counterexamples
The analog of Theorem
1
fails for flat 2-orbifolds.
In the connected case it does go through more or less by accident,
just because there aren’t many connected flat 2-orbifolds.
But there are counterexamples among disconnected flat 2-orbifolds.
We described such examples briefly in
[
5
]
.
Here’s our premier example, which we call
the
1
2
+
1
6
=
2
3
1
2
1
6
2
3
\frac{1}{2}+\frac{1}{6}=\frac{2}{3}
example
.
Let
H
1
subscript
𝐻
1
H_{1}
denote the standard hexagonal flat torus
⟨
(
1
,
0
)
,
(
−
1
2
,
3
2
)
⟩
\
𝐑
2
\
1
0
1
2
3
2
superscript
𝐑
2
\langle(1,0),(-\frac{1}{2},\frac{\sqrt{3}}{2})\rangle\backslash\mathbf{R}^{2}
.
H
1
subscript
𝐻
1
H_{1}
has as 2-, 3-, and 6-fold quotients
a
2222
2222
2222
orbifold
H
2
subscript
𝐻
2
H_{2}
(this is a regular tetrahedron); a
333
333
333
orbifold
H
3
subscript
𝐻
3
H_{3}
; and a
236
236
236
orbifold
H
6
subscript
𝐻
6
H_{6}
.
(See Figures
7
and
8
.)
Figure 7:
The universal covers of the standard hexagonal
torus
H
1
subscript
𝐻
1
H_{1}
and its quotient orbifolds
H
2
subscript
𝐻
2
H_{2}
,
H
3
subscript
𝐻
3
H_{3}
, and
H
6
subscript
𝐻
6
H_{6}
.
Figure 8:
The orbifolds
H
1
=
○
subscript
𝐻
1
○
H_{1}=\bigcirc
,
H
2
=
2222
subscript
𝐻
2
2222
H_{2}=2222
,
H
3
=
333
subscript
𝐻
3
333
H_{3}=333
, and
H
6
=
236
subscript
𝐻
6
236
H_{6}=236
.
Spectrally,
H
2
+
H
6
≡
2
​
H
3
,
subscript
𝐻
2
subscript
𝐻
6
2
subscript
𝐻
3
H_{2}+H_{6}\equiv 2H_{3},
(1)
meaning that these spaces have the same Laplace spectrum.
(In fact, as we’ll discuss below, they are isospectral
for the Laplacian on
k
𝑘
k
-forms for
k
=
0
,
1
,
2
𝑘
0
1
2
k=0,1,2
.)
Of course these two spaces match as to volume
(
1
2
+
1
6
=
2
3
1
2
1
6
2
3
\frac{1}{2}+\frac{1}{6}=\frac{2}{3}
)
and number of components
(
1
+
1
=
2
1
1
2
1+1=2
).
But conepoints do not match.
On the left we have a
2222
2222
2222
and a
236
236
236
, so
five conepoints of order
2
2
2
;
one of order
3
3
3
;
one of order
6
6
6
.
On the right we have two
333
333
333
s, so nine conepoints of order
3
3
3
.
The reason this example is possible is that in the flat case,
the contributions of rotations to the counting kernel differ
only by a multiplicative constant.
Lumping together the contribution of all the rotations associated with a
conepoint of order
n
𝑛
n
, we get something proportional to
n
2
−
1
n
superscript
𝑛
2
1
𝑛
\frac{n^{2}-1}{n}
.
(This nice simple formula was discovered by Dryden-Gordon-Greenwald
[
7
]
.)
For a general 2-orbifold with variable curvature, it measures
the contribution of conepoints to the short-time asymptotics of the heat trace.
In the flat case, the short-time asymptotics determine the
entire contribution, because the contributions
of all rotations are exactly proportional.
Combining contributions of all conepoints,
we get the following totals:
orbifold
contribution
examples
2222
:
4
⋅
3
2
=
6
H
2
,
T
2
333
:
3
⋅
8
3
=
8
H
3
244
:
3
2
+
2
⋅
15
4
=
9
T
4
236
:
3
2
+
8
3
+
35
6
=
10
H
6
orbifold
contribution
examples
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
:
2222
absent
⋅
4
3
2
6
subscript
𝐻
2
subscript
𝑇
2
:
333
absent
⋅
3
8
3
8
subscript
𝐻
3
:
244
absent
3
2
⋅
2
15
4
9
subscript
𝑇
4
:
236
absent
3
2
8
3
35
6
10
subscript
𝐻
6
\begin{array}[]{rcl}\mbox{orbifold}&\mbox{contribution}&\mbox{examples}\\
\hline\cr\\
2222:&4\cdot\frac{3}{2}=6&H_{2},T_{2}\\
333:&3\cdot\frac{8}{3}=8&H_{3}\\
244:&\frac{3}{2}+2\cdot\frac{15}{4}=9&T_{4}\\
236:&\frac{3}{2}+\frac{8}{3}+\frac{35}{6}=10&H_{6}\end{array}
The isospectrality
H
2
+
H
6
≡
2
​
H
3
subscript
𝐻
2
subscript
𝐻
6
2
subscript
𝐻
3
H_{2}+H_{6}\equiv 2H_{3}
arises because
6
+
10
=
2
⋅
8
6
10
⋅
2
8
6+10=2\cdot 8
makes conepoint
contributions match; we’ve already observed that the volumes match; and geodesic contributions match because on both sides the covering manifolds are
2
​
H
1
2
subscript
𝐻
1
2H_{1}
.
We get a second isospectrality
H
1
+
H
3
+
H
6
≡
3
​
H
2
subscript
𝐻
1
subscript
𝐻
3
subscript
𝐻
6
3
subscript
𝐻
2
H_{1}+H_{3}+H_{6}\equiv 3H_{2}
because
8
+
10
=
3
⋅
6
8
10
⋅
3
6
8+10=3\cdot 6
,
1
+
1
3
+
1
6
=
3
⋅
1
2
1
1
3
1
6
⋅
3
1
2
1+\frac{1}{3}+\frac{1}{6}=3\cdot\frac{1}{2}
,
and on both sides the covering manifolds are
3
​
H
1
3
subscript
𝐻
1
3H_{1}
.
Combining these two relations yields other Laplace-isospectral pairs, e.g.:
H
1
+
3
​
H
3
≡
4
​
H
2
;
subscript
𝐻
1
3
subscript
𝐻
3
4
subscript
𝐻
2
H_{1}+3H_{3}\equiv 4H_{2};
H
1
+
4
​
H
6
≡
5
​
H
3
;
subscript
𝐻
1
4
subscript
𝐻
6
5
subscript
𝐻
3
H_{1}+4H_{6}\equiv 5H_{3};
2
​
H
1
+
3
​
H
6
≡
5
​
H
2
.
2
subscript
𝐻
1
3
subscript
𝐻
6
5
subscript
𝐻
2
2H_{1}+3H_{6}\equiv 5H_{2}.
By linearity, all these relations satisfy the condition of
having equal volume, number
of components, and contributions from conepoints.
But look here:
We’re talking, in effect, about formal combinations of
H
1
,
H
2
,
H
3
,
H
6
subscript
𝐻
1
subscript
𝐻
2
subscript
𝐻
3
subscript
𝐻
6
H_{1},H_{2},H_{3},H_{6}
, so we’re in a space of dimension
4
4
4
.
We have three linear conditions, but to our surprise,
the subspace they determine has dimension
2
2
2
.
Our three linear conditions are not independent.
If we match volume and number of components,
agreement of conepoint contributions follows for free.
But why? We don’t know.
A similar coincidence happens for square tori.
Let
T
1
subscript
𝑇
1
T_{1}
denote the standard square torus
𝐙
2
\
𝐑
2
\
superscript
𝐙
2
superscript
𝐑
2
\mathbf{Z}^{2}\backslash\mathbf{R}^{2}
.
T
1
subscript
𝑇
1
T_{1}
has as 2-, and 4-fold quotients
a
2222
2222
2222
orbifold
T
2
subscript
𝑇
2
T_{2}
and a
244
244
244
orbifold
T
4
subscript
𝑇
4
T_{4}
.
We’re in a 3-dimensional space,
so we expect to be out of luck when we impose 3 constraints,
but in fact we have the relation
T
1
+
2
​
T
4
≡
3
​
T
2
.
subscript
𝑇
1
2
subscript
𝑇
4
3
subscript
𝑇
2
T_{1}+2T_{4}\equiv 3T_{2}.
We check equality of volume
1
+
2
4
=
3
2
1
2
4
3
2
1+\frac{2}{4}=\frac{3}{2}
and number of components
1
+
2
=
3
1
2
3
1+2=3
, and then we find that equality of conepoint
contributions follows for free:
2
⋅
9
=
3
⋅
6
⋅
2
9
⋅
3
6
2\cdot 9=3\cdot 6
.
Again, why?
These relations apply only to the spectrum of the Laplacian on functions,
not
1
1
1
-forms.
When we apply the Selberg formula to
1
1
1
-forms,
there is still interference between spectral contributions of conepoints,
which allows our
1
2
+
1
6
=
2
3
1
2
1
6
2
3
\frac{1}{2}+\frac{1}{6}=\frac{2}{3}
example to continue to slip through:
It is isospectral for
1
1
1
-forms as well as for functions.
But we get additional constraints, which taken with those coming from
the
0
0
-spectrum force there to be the same number of torus components
on each side,
and this wipes out the other examples.
The reason we have to have the same number of torus components is that this
is just half the dimension of the space of ‘constant’ or ‘harmonic’
1
1
1
-forms, meaning those belonging to the
0
0
-eigenspace of the Laplacian.
And since we are expecting just one more linear constraint, this must
be it.
So, no additional mystery here,
though when you do the computation it still seems a little surprising.
The isospectrality of the
1
2
+
1
6
=
2
3
1
2
1
6
2
3
\frac{1}{2}+\frac{1}{6}=\frac{2}{3}
example
does not hold for all natural operators.
because the left side admits harmonic differentials
that the right side does not.
Specifically,
look at the real part of a (non-holomorphic) quadratic differential,
i.e. an expression which in any conformally
correct chart with coordinate
z
𝑧
z
takes the form
ℜ
⁡
f
​
(
z
)
​
d
​
z
2
𝑓
𝑧
𝑑
superscript
𝑧
2
\Re f(z)dz^{2}
,
where
f
𝑓
f
is an arbitrary (not necessarily holomorphic) complex-valued
function.
We can rewrite this as
g
​
(
x
,
y
)
​
(
d
​
x
2
−
d
​
y
2
)
+
h
​
(
x
,
y
)
​
(
2
​
d
​
x
​
d
​
y
)
𝑔
𝑥
𝑦
𝑑
superscript
𝑥
2
𝑑
superscript
𝑦
2
ℎ
𝑥
𝑦
2
𝑑
𝑥
𝑑
𝑦
g(x,y)(dx^{2}-dy^{2})+h(x,y)(2dxdy)
where
g
𝑔
g
and
h
ℎ
h
are real.
Such quadratic differentials are sections of a natural flat bundle,
and in a flat coordinate system the Laplacian passes through to act on
g
𝑔
g
and
h
ℎ
h
.
Wherever the section doesn’t vanish we can set
R
​
e
​
f
​
(
z
)
​
d
​
z
2
=
0
𝑅
𝑒
𝑓
𝑧
𝑑
superscript
𝑧
2
0
Ref(z)dz^{2}=0
and solve for
d
​
z
𝑑
𝑧
dz
to get an unoriented line element.
A harmonic section (i.e. an eigensection belonging to eigenvalue 0)
will have
g
𝑔
g
and
h
ℎ
h
constant in any flat coordinate system,
and the line elements will be parallel.
In the
1
2
+
1
6
=
2
3
1
2
1
6
2
3
\frac{1}{2}+\frac{1}{6}=\frac{2}{3}
example only
the orbifold
H
2
subscript
𝐻
2
H_{2}
admits a globally parallel line
element like this, so the spectra for the Laplacian on these sections
are different.
9
Higher dimensions
Version 1 of this paper
[
6
]
contains, among many other things omitted here, the following conjecture:
‘It seems likely that in any dimension, if two hyperbolic
(or spherical) orbifolds are isospectral on
k
𝑘
k
-forms for all
k
𝑘
k
,
then they are representation-equivalent.’
Lauret, Miatello, and Rossetti
[
12
]
have shown that this is false in the spherical case.
They give many examples of lens spaces that are all-forms-isospectral
but not representation-equivalent, beginning in dimension 5.
(For a simpler approach to these examples, see DeFord and Doyle
[
3
]
.)
In the hyperbolic case, the question remains open.
As for the flat case,
we saw in Section
8
an example of disconnected
2
2
2
-orbifolds
that are all-forms-isospectral but not representation-equivalent.
We have been hoping to
find higher-dimensional examples that are connected, and perhaps even
manifolds and not just orbifolds,
but so far we’ve had no success with this.
References
[1]
Pierre Bérard.
Transplantation et isospectralité. II.
J. London Math. Soc. (2)
, 48(3):565–576, 1993.
[2]
Peter Buser, John Conway, Peter Doyle, and Klaus-Dieter Semmler.
Some planar isospectral domains.
Internat. Math. Res. Notices
, 9, 1994, arXiv:1005.1839v1
[math.DG].
http://arxiv.org/abs/1005.1839v1
.
[3]
Daryl R. DeFord and Peter G. Doyle.
Cyclic groups with the same hodge series, 2014, arXiv:1404.2574v1
[math.RA].
http://arxiv.org/abs/1404.2574v1
.
[4]
Dennis M. DeTurck and Carolyn S. Gordon.
Isospectral deformations. II. Trace formulas, metrics, and
potentials.
Comm. Pure Appl. Math.
, 42(8):1067–1095, 1989.
With an appendix by Kyung Bai Lee.
[5]
Peter G. Doyle and Juan Pablo Rossetti.
Isospectral hyperbolic surfaces have matching geodesics, 2008,
arXiv:math/0605765v2 [math.DG].
http://arxiv.org/abs/math/0605765v2.
[6]
Peter G. Doyle and Juan Pablo Rossetti.
Laplace-isospectral hyperbolic 2-orbifolds are
representation-equivalent (Version 1), 2011, arXiv:1103.4372v1 [math.DG].
http://arxiv.org/abs/1103.4372v1
.
[7]
Emily B. Dryden, Carolyn S. Gordon, Sarah J. Greenwald, and David L. Webb.
Asymptotic expansion of the heat kernel for orbifolds, 2008,
arXiv:0805.3148v1 [math.DG].
http://arxiv.org/abs/0805.3148v1
.
[8]
Emily B. Dryden and Alexander Strohmaier.
Huber’s theorem for hyperbolic orbisurfaces, 2005,
arXiv:math.SP/0504571.
http://arxiv.org/abs/math/0504571
.
[9]
C. Gordon, D. Webb, and S. Wolpert.
One cannot hear the shape of a drum.
Bull. Amer. Math. Soc.
, 27:134–138, 1992.
[10]
Heinz Huber.
Zur analytischen Theorie hyperbolischen Raumformen und
Bewegungsgruppen.
Math. Ann.
, 138:1–26, 1959.
[11]
Dubi Kelmer.
A refinement of strong multiplicity one for spectra of hyperbolic
manifolds, 2011, arXiv:1108.2977v2 [math.SP].
http://arxiv.org/abs/1108.2977v2
.
[12]
Emilio A. Lauret, Roberto J. Miatello, and Juan Pablo Rossetti.
Lens spaces isospectral on
p
𝑝
p
-forms for every
p
𝑝
p
, 2013,
arXiv:1311.7167v2 [math.DG].
http://arxiv.org/abs/1311.7167v2
.
[13]
Colin Maclachlan and Alan W. Reid.
The arithmetic of hyperbolic 3-manifolds
, volume 219 of
Graduate Texts in Mathematics
.
Springer-Verlag, New York, 2003.
[14]
Atle Selberg.
Harmonic analysis and discontinuous groups in weakly symmetric
Riemannian spaces with applications to Dirichlet series.
J. Indian Math. Soc. B
, 20:47–87, 1956.
Reprinted in
[
15
]
.
[15]
Atle Selberg.
Harmonic analysis and discontinuous groups in weakly symmetric
Riemannian spaces with applications to Dirichlet series.
In
Collected Papers, vol. 1
, pages 423–463. Springer, 1989.
[16]
Nolan R. Wallach.
On the Selberg trace formula in the case of compact quotient.
Bull. Amer. Math. Soc.
, 82(2):171–195, 1976.
◄
Feeling
lucky?
Conversion
report
Report
an issue
View original
on arXiv
►