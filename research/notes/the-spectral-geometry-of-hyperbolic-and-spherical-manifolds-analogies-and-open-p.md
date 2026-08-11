---
title: 'The spectral geometry of hyperbolic and spherical manifolds: analogies and
  open problems'
id: the-spectral-geometry-of-hyperbolic-and-spherical-manifolds-analogies-and-open-p
tags:
- hyperbolic-pillow-heat-novelty-813161
created: '2026-08-09T08:49:23.728422Z'
updated: '2026-08-09T09:36:32.487849Z'
source: https://arxiv.org/html/2305.10950
source_domain: arxiv.org
fetched_at: '2026-08-09T08:49:23.727354Z'
fetch_provider: builtin
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'The spectral geometry of hyperbolic and spherical manifolds: analogies and
  open problems'
---

The spectral geometry of hyperbolic and spherical manifolds: analogies and open problems
The spectral geometry of hyperbolic and spherical manifolds: analogies and open problems
Emilio A. Lauret
Instituto de Matemática (INMABB), Departamento de Matemática, Universidad Nacional del Sur (UNS)-CONICET, Bahía Blanca, Argentina.
emilio.lauret@uns.edu.ar
and
Benjamin Linowitz
Department of Mathematics
10 North Professor Street
Oberlin, OH 44074.
benjamin.linowitz@oberlin.edu
(Date: May 12, 2024)
Abstract.
The spectral geometry of negatively curved manifolds has received more attention than its positive curvature counterpart. In this paper we will survey a variety of spectral geometry results that are known to hold in the context of hyperbolic manifolds and discuss the extent to which analogous results hold in the setting of spherical manifolds. We conclude with a number of open problems.
Key words and phrases:
isospectral, spectrum, spherical space form, lens space
2020 Mathematics Subject Classification:
Primary 58J53. Secondary 22C05, 58J50.
This research was supported by grants from FONCyT (BID-PICT-2018-02073 and BID-PICT-2019-2019-01054) and SGCYT–UNS. The second author is partially supported by NSF Grant Number DMS-1905437.
1.
Introduction
Let
(
M
,
g
)
𝑀
𝑔
(M,g)
( italic_M , italic_g )
be a compact Riemannian manifold. The eigenvalues of the Laplace-Beltrami operator acting on the space
L
2
⁢
(
M
,
g
)
superscript
𝐿
2
𝑀
𝑔
L^{2}(M,g)
italic_L start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( italic_M , italic_g )
form a discrete subset of the non-negative real numbers in which every value occurs with a finite multiplicity. This collection of eigenvalues is called the spectrum of
(
M
,
g
)
𝑀
𝑔
(M,g)
( italic_M , italic_g )
and is denoted by
Spec
⁡
(
M
,
g
)
Spec
𝑀
𝑔
\operatorname{Spec}(M,g)
roman_Spec ( italic_M , italic_g )
. Two Riemannian manifolds are said to be isospectral if their spectra coincide.
Inverse Spectral Geometry studies to what extent the geometry and topology of
(
M
,
g
)
𝑀
𝑔
(M,g)
( italic_M , italic_g )
are determined by
Spec
⁡
(
M
,
g
)
Spec
𝑀
𝑔
\operatorname{Spec}(M,g)
roman_Spec ( italic_M , italic_g )
. It is well known, for example, that
dim
M
dimension
𝑀
\dim M
roman_dim italic_M
and
vol
⁡
(
M
,
g
)
vol
𝑀
𝑔
\operatorname{vol}(M,g)
roman_vol ( italic_M , italic_g )
are both spectral invariants; that is, their values are both determined by
Spec
⁡
(
M
,
g
)
Spec
𝑀
𝑔
\operatorname{Spec}(M,g)
roman_Spec ( italic_M , italic_g )
. Isometry class is not a spectral invariant, however. Indeed, the literature is full of interesting examples of Riemannian manifolds that are isospectral but not isometric. Alluding to Kac’s famous “Can one hear the shape of a drum” article
[
Ka66
]
, spectral invariants are called audible. Part of the importance of examples of isospectral Riemannian manifolds is their ability to show that certain properties are inaudible. For a more detailed discussion we refer the reader to the survey
[
Go00
]
by Gordon.
Locally symmetric spaces arise frequently in the construction of isospectral manifolds. In fact, the first three classes of examples of isospectral manifolds were all locally symmetric spaces: flat tori by Milnor
[
Mi64
]
, Riemann surfaces by Vignéras
[
Vi80
]
, and lens spaces by Ikeda
[
Ik80
]
.
Subsequently, compact locally symmetric spaces of non-compact type (that is, compact manifolds covered by non-compact symmetric spaces; e.g. compact hyperbolic manifolds) have attracted more attention than locally symmetric spaces of compact type (e.g. spherical space forms).
The main goal of this article is to discuss possible extensions to the compact type setting of several results in inverse spectral geometry of locally symmetric spaces of non-compact type. We introduce each of these results individually in Subsections
1.2
–
1.5
and address them in Sections
4
–
7
, respectively.
The article ends in Section
8
with further open questions and problems.
Before discussing this paper’s results, we introduce the main actors. A spherical space form is a Riemannian manifold of the form
S
d
/
Γ
superscript
𝑆
𝑑
Γ
S^{d}/\Gamma
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ
where
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
denotes the
d
𝑑
d
italic_d
-dimensional sphere endowed with its constant sectional curvature one Riemannian metric and where
Γ
Γ
\Gamma
roman_Γ
is a discrete (hence finite) subgroup of
Iso
⁡
(
S
d
)
Iso
superscript
𝑆
𝑑
\operatorname{Iso}(S^{d})
roman_Iso ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT )
acting freely on
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
.
An important subclass of spherical space forms are those of odd dimension with
Γ
Γ
\Gamma
roman_Γ
cyclic. These spaces are called lens spaces.
Lens spaces have long played an important role in inverse spectral geometry, beginning with Ikeda’s aforementioned examples
[
Ik80
]
of isospectral lens spaces. For more recent work on the spectral geometry of lens spaces, see e.g.
[
LMR21
]
and the references therein. Rather than working with manifolds, we will often consider instead (good) orbifolds.
These spaces, when defined as above, though with the free-action condition omitted, will be called
spherical orbifolds
and
lens orbifolds
respectively.
See §
2
for more details.
1.1.
Eigenvalue equivalence
In 1911 Weyl derived an asymptotic expression for the sequence of Laplace eigenvalues of a compact Riemannian manifold
(
M
,
g
)
𝑀
𝑔
(M,g)
( italic_M , italic_g )
which implied that
vol
⁡
(
M
,
g
)
vol
𝑀
𝑔
\operatorname{vol}(M,g)
roman_vol ( italic_M , italic_g )
is a spectral invariant. In particular, isospectral manifolds necessarily have the same volume. Recall, however, that the spectrum of
(
M
,
g
)
𝑀
𝑔
(M,g)
( italic_M , italic_g )
is the set of eigenvalues of the Laplace-Beltrami operator acting on
L
2
⁢
(
M
,
g
)
superscript
𝐿
2
𝑀
𝑔
L^{2}(M,g)
italic_L start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( italic_M , italic_g )
, counted with multiplicity. It is therefore natural to ask whether Riemannian manifolds which have the same set of Laplace-Beltrami eigenvalues (disregarding multiplicities) necessarily have the same volume. Call two Riemannian manifolds eigenvalue equivalent if they have the same set of Laplace-Beltrami eigenvalues. The question is therefore whether eigenvalue equivalent manifolds must have the same volume.
In 2007, Leininger, McReynolds, Neumann and Reid
[
LMNR07
]
proved that this is false by constructing examples of hyperbolic
n
𝑛
n
italic_n
-manifolds (for any dimension
n
≥
2
𝑛
2
n\geq 2
italic_n ≥ 2
) which are eigenvalue equivalent and whose volumes differ.
Question 1.1
.
Do there exist examples of eigenvalue equivalent spherical orbifolds whose volumes differ?
In Section
3
we will answer this question in the affirmative in every dimension
n
≥
9
𝑛
9
n\geq 9
italic_n ≥ 9
by proving the following theorem.
Theorem 1.2
.
Let
n
≥
9
𝑛
9
n\geq 9
italic_n ≥ 9
. There exist
n
𝑛
n
italic_n
-dimensional spherical orbifolds
M
1
subscript
𝑀
1
M_{1}
italic_M start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
M
2
subscript
𝑀
2
M_{2}
italic_M start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
which are eigenvalue equivalent yet whose volumes satisfy
vol
⁢
(
M
2
)
=
3
⋅
vol
⁢
(
M
1
)
vol
subscript
𝑀
2
⋅
3
vol
subscript
𝑀
1
\mathrm{vol}(M_{2})=3\cdot\mathrm{vol}(M_{1})
roman_vol ( italic_M start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ) = 3 ⋅ roman_vol ( italic_M start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT )
.
We also give a second construction of eigenvalue equivalent spherical orbifolds (lens spaces) whose volumes differ. This construction does not rely on the work of Leininger, McReynolds, Neumann and Reid
[
LMNR07
]
but rather makes use of an explicit formula for the Laplace eigenvalues of an arbitrary lens space.
Theorem 1.3
.
For every odd integer
d
≥
3
𝑑
3
d\geq 3
italic_d ≥ 3
, there exists an infinite family
𝔏
𝔏
\mathfrak{L}
fraktur_L
of
d
𝑑
d
italic_d
-dimensional lens spaces that are mutually eigenvalue equivalent and such that
(1.1)
sup
L
1
,
L
2
∈
𝔏
vol
⁡
(
L
1
)
vol
⁡
(
L
2
)
=
∞
.
subscript
supremum
subscript
𝐿
1
subscript
𝐿
2
𝔏
vol
subscript
𝐿
1
vol
subscript
𝐿
2
\sup_{L_{1},L_{2}\in\mathfrak{L}}\frac{\operatorname{vol}(L_{1})}{%
\operatorname{vol}(L_{2})}=\infty.
roman_sup start_POSTSUBSCRIPT italic_L start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_L start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ∈ fraktur_L end_POSTSUBSCRIPT divide start_ARG roman_vol ( italic_L start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ) end_ARG start_ARG roman_vol ( italic_L start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ) end_ARG = ∞ .
We conclude Section
3
by showing that the eigenvalue spectrum (with multiplicities disregarded) cannot detect singularities in lens orbifolds (Example
3.5
) and that it does not determine the dimension (Theorem
3.6
) of homogeneous Riemannian manifolds of compact type.
1.2.
Isospectral pairs of largest volume
The first pairs of isospectral hyperbolic surfaces were constructed by Vignéras
[
Vi80
]
and had enormous area. A decade later Buser
[
Bu
]
used Sunada’s method
[
Su85
]
, a powerful method that can be used to construct isospectral Riemannian manifolds in many different contexts, in order to construct isospectral hyperbolic surfaces of genus
5
5
5
5
and of genus
g
𝑔
g
italic_g
for all
g
≥
7
𝑔
7
g\geq 7
italic_g ≥ 7
. Examples with genus
4
4
4
4
and
6
6
6
6
were later constructed by Brooks and Tse
[
BT87
]
. There are no known examples of non-isometric isospectral hyperbolic surfaces with genus
2
2
2
2
or
3
3
3
3
, and it is suspected that in genus
2
2
2
2
such surfaces cannot exist.
In the arithmetic realm, John Voight and the second author constructed pairs of non-isometric (strongly) isospectral 2-dimensional and 3-dimensional arithmetic hyperbolic orbifolds and manifolds of minimal volume among certain nice classes of arithmetic orbifolds (see
[
LV15
]
). It is not known what the smallest area of a pair of arithmetic hyperbolic
2
2
2
2
-orbifolds is, but one may suspect that it is the area of a particularly simple pair of isospectral hyperbolic polygons found by Doyle and Rossetti
[
DR
, Section 2]
.
In this paper we will discuss spherical analogs of the above results.
The volume of a spherical orbifold
S
d
/
Γ
superscript
𝑆
𝑑
Γ
S^{d}/\Gamma
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ
is given by
(1.2)
vol
⁡
(
S
d
/
Γ
)
=
vol
⁡
(
S
d
)
|
Γ
|
.
vol
superscript
𝑆
𝑑
Γ
vol
superscript
𝑆
𝑑
Γ
\operatorname{vol}(S^{d}/\Gamma)=\frac{\operatorname{vol}(S^{d})}{|\Gamma|}.
roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ ) = divide start_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ) end_ARG start_ARG | roman_Γ | end_ARG .
In particular, the volume of any
d
𝑑
d
italic_d
-dimensional spherical orbifold is bounded by above by
vol
⁡
(
S
d
)
vol
superscript
𝑆
𝑑
\operatorname{vol}(S^{d})
roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT )
. This makes it clear that the spherical analog of the problem of finding the isospectral hyperbolic manifolds of smallest volume is to find the isospectral spherical manifolds of largest volume.
Question 1.4
.
What is the largest volume of an isospectral pair of
d
𝑑
d
italic_d
-dimensional non-isometric spherical orbifolds?
A pair of almost conjugate (and non-conjugate) subgroups in
SO
⁡
(
6
)
SO
6
\operatorname{SO}(6)
roman_SO ( 6 )
constructed by Rossetti, Schueth and Weilandt
[
RSW08
]
immediately provides the following quite good lower bound.
Theorem 1.5
.
The largest volume of an isospectral and non-isometric pair of spherical orbifolds of dimension
d
≥
5
𝑑
5
d\geq 5
italic_d ≥ 5
is at most
1
8
⁢
vol
⁡
(
S
d
)
1
8
vol
superscript
𝑆
𝑑
\frac{1}{8}\operatorname{vol}(S^{d})
divide start_ARG 1 end_ARG start_ARG 8 end_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT )
.
As in the hyperbolic setting, the difficulty increases when we consider manifolds instead of orbifolds.
In the spherical context, this situation is explained because the condition of acting freely on
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
is a great obstruction for a finite subgroup of
SO
⁡
(
d
+
1
)
SO
𝑑
1
\operatorname{SO}(d+1)
roman_SO ( italic_d + 1 )
.
Indeed, although every finite group can be embedded into an special orthogonal group, the classification of spherical space forms done by Wolf
[
Wo
]
shows that the groups acting freely on spheres are very particular.
Question 1.6
.
What is the largest volume of an isospectral and non-isometric pair of
d
𝑑
d
italic_d
-dimensional spherical space forms?
It is well known that there do not exist isospectral pairs of spherical space forms when
d
𝑑
d
italic_d
is even or when
d
=
3
𝑑
3
d=3
italic_d = 3
.
For all other values of
d
𝑑
d
italic_d
we have the following statement.
Theorem 1.7
.
If
n
≥
3
𝑛
3
n\geq 3
italic_n ≥ 3
, then any pair of isospectral and non-isometric
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional spherical space forms of largest volume are lens spaces provided that
(1.3)
{
n
≡
1
(
mod
4
)
,
or
n
≡
1
,
2
,
3
(
mod
5
)
,
or
n
≡
1
,
2
,
3
,
4
(
mod
6
)
,
or
n
≡
2
,
3
,
4
,
5
,
6
(
mod
8
)
,
or
n
≡
2
,
3
,
4
,
5
,
6
,
7
(
mod
9
)
,
or
n
≡
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
(
mod
11
)
.
\begin{cases}n\equiv 1&\pmod{4},\text{ or}\\
n\equiv 1,2,3&\pmod{5},\text{ or}\\
n\equiv 1,2,3,4&\pmod{6},\text{ or}\\
n\equiv 2,3,4,5,6&\pmod{8},\text{ or}\\
n\equiv 2,3,4,5,6,7&\pmod{9},\text{ or}\\
n\equiv 2,3,4,5,6,7,8,9&\pmod{11}.\end{cases}
{ start_ROW start_CELL italic_n ≡ 1 end_CELL start_CELL start_MODIFIER ( roman_mod start_ARG 4 end_ARG ) end_MODIFIER , or end_CELL end_ROW start_ROW start_CELL italic_n ≡ 1 , 2 , 3 end_CELL start_CELL start_MODIFIER ( roman_mod start_ARG 5 end_ARG ) end_MODIFIER , or end_CELL end_ROW start_ROW start_CELL italic_n ≡ 1 , 2 , 3 , 4 end_CELL start_CELL start_MODIFIER ( roman_mod start_ARG 6 end_ARG ) end_MODIFIER , or end_CELL end_ROW start_ROW start_CELL italic_n ≡ 2 , 3 , 4 , 5 , 6 end_CELL start_CELL start_MODIFIER ( roman_mod start_ARG 8 end_ARG ) end_MODIFIER , or end_CELL end_ROW start_ROW start_CELL italic_n ≡ 2 , 3 , 4 , 5 , 6 , 7 end_CELL start_CELL start_MODIFIER ( roman_mod start_ARG 9 end_ARG ) end_MODIFIER , or end_CELL end_ROW start_ROW start_CELL italic_n ≡ 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 end_CELL start_CELL start_MODIFIER ( roman_mod start_ARG 11 end_ARG ) end_MODIFIER . end_CELL end_ROW
In particular, this holds for all
3
≤
n
≤
1000
3
𝑛
1000
3\leq n\leq 1000
3 ≤ italic_n ≤ 1000
with the sole exceptions of
n
=
144
𝑛
144
n=144
italic_n = 144
and
n
=
935
𝑛
935
n=935
italic_n = 935
.
The authors conjecture that the above statement in fact holds for all
n
≥
3
𝑛
3
n\geq 3
italic_n ≥ 3
.
See Tables
1
and
2
for an explicit upper bound for the volume of a pair of
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional isospectral and non-isometric lens spaces, for each
n
𝑛
n
italic_n
satisfying (
1.3
).
1.3.
Finite part spectrum
In some situations, only a finite part of the spectrum is necessary to determine isospectrality.
This is the case for Riemann surfaces under some geometric obstructions.
Theorem 1.8
(Buser, Courtois
[
BC90
]
)
.
Given an integer
g
≥
2
𝑔
2
g\geq 2
italic_g ≥ 2
and
ε
>
0
𝜀
0
\varepsilon>0
italic_ε > 0
, there is
N
=
N
⁢
(
g
,
ε
)
𝑁
𝑁
𝑔
𝜀
N=N(g,\varepsilon)
italic_N = italic_N ( italic_g , italic_ε )
such that two compact Riemann surfaces of genus
g
𝑔
g
italic_g
and injectivity radius
≥
ε
absent
𝜀
\geq\varepsilon
≥ italic_ε
are isospectral if and only if they have the same first
N
𝑁
N
italic_N
eigenvalues (counted with multiplicities).
Dai and Wei
[
DW94
]
obtained a nice extension valid for the moduli space of Einstein metrics under some geometric conditions.
We discuss in Section
5
some extensions of Theorem
1.8
among quotients of compact symmetric spaces.
Indeed, we will observe that a CROSS (Compact Rank One Symmetric Space) is a very adequate choice for this sort of question.
The proofs will follow (more or less immediately) from Lie theoretical results in
[
LM20
]
by Miatello and the first named author; in fact,
[
LM21
, Rem. 3.8]
predicted such a situation though without providing details.
We realize simply connected CROSSes as quotients of compact Lie groups as follows:
(1.4)
S
n
superscript
𝑆
𝑛
\displaystyle S^{n}
italic_S start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
=
SO
⁡
(
n
+
1
)
SO
⁡
(
n
)
,
absent
SO
𝑛
1
SO
𝑛
\displaystyle=\tfrac{\operatorname{SO}(n+1)}{\operatorname{SO}(n)},
= divide start_ARG roman_SO ( italic_n + 1 ) end_ARG start_ARG roman_SO ( italic_n ) end_ARG ,
P
n
⁢
(
ℂ
)
superscript
𝑃
𝑛
ℂ
\displaystyle P^{n}(\mathbb{C})
italic_P start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( blackboard_C )
=
SU
⁡
(
n
+
1
)
S
⁡
(
U
⁡
(
n
)
×
U
⁡
(
1
)
)
,
absent
SU
𝑛
1
S
U
𝑛
U
1
\displaystyle=\tfrac{\operatorname{SU}(n+1)}{\operatorname{S}(\operatorname{U}%
(n)\times\operatorname{U}(1))},
= divide start_ARG roman_SU ( italic_n + 1 ) end_ARG start_ARG roman_S ( roman_U ( italic_n ) × roman_U ( 1 ) ) end_ARG ,
P
n
⁢
(
ℍ
)
superscript
𝑃
𝑛
ℍ
\displaystyle P^{n}(\mathbb{H})
italic_P start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( blackboard_H )
=
Sp
⁡
(
n
+
1
)
Sp
⁡
(
n
)
×
Sp
⁡
(
1
)
,
absent
Sp
𝑛
1
Sp
𝑛
Sp
1
\displaystyle=\tfrac{\operatorname{Sp}(n+1)}{\operatorname{Sp}(n)\times%
\operatorname{Sp}(1)},
= divide start_ARG roman_Sp ( italic_n + 1 ) end_ARG start_ARG roman_Sp ( italic_n ) × roman_Sp ( 1 ) end_ARG ,
P
2
⁢
(
𝕆
)
superscript
𝑃
2
𝕆
\displaystyle P^{2}(\mathbb{O})
italic_P start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( blackboard_O )
=
F
4
Spin
⁡
(
9
)
.
absent
subscript
F
4
Spin
9
\displaystyle=\tfrac{\operatorname{F}_{4}}{\operatorname{Spin}(9)}.
= divide start_ARG roman_F start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT end_ARG start_ARG roman_Spin ( 9 ) end_ARG .
The only non-simply connected CROSSes are real projective spaces that we write
P
n
⁢
(
ℝ
)
=
SO
⁡
(
n
+
1
)
/
O
⁡
(
n
)
superscript
𝑃
𝑛
ℝ
SO
𝑛
1
O
𝑛
P^{n}(\mathbb{R})=\operatorname{SO}(n+1)/\operatorname{O}(n)
italic_P start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( blackboard_R ) = roman_SO ( italic_n + 1 ) / roman_O ( italic_n )
.
Note that
G
𝐺
G
italic_G
acts almost effectively and by isometries on
X
=
G
/
K
𝑋
𝐺
𝐾
X=G/K
italic_X = italic_G / italic_K
in every case.
Theorem 1.9
.
Let
X
𝑋
X
italic_X
be a compact rank one symmetric space realized as
G
/
K
𝐺
𝐾
G/K
italic_G / italic_K
as in (
1.4
).
Given
ε
>
0
𝜀
0
\varepsilon>0
italic_ε > 0
, there is
N
=
N
⁢
(
X
,
ε
)
𝑁
𝑁
𝑋
𝜀
N=N(X,\varepsilon)
italic_N = italic_N ( italic_X , italic_ε )
such that, for
Γ
1
,
Γ
2
subscript
Γ
1
subscript
Γ
2
\Gamma_{1},\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
finite subgroups of
G
𝐺
G
italic_G
with
|
Γ
i
|
−
1
=
vol
⁡
(
Γ
i
\
X
)
vol
⁡
(
X
)
>
ε
superscript
subscript
Γ
𝑖
1
vol
\
subscript
Γ
𝑖
𝑋
vol
𝑋
𝜀
|\Gamma_{i}|^{-1}=\frac{\operatorname{vol}(\Gamma_{i}\backslash X)}{%
\operatorname{vol}(X)}>\varepsilon
| roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT | start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT = divide start_ARG roman_vol ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X ) end_ARG start_ARG roman_vol ( italic_X ) end_ARG > italic_ε
, the orbifolds
Γ
1
\
X
\
subscript
Γ
1
𝑋
\Gamma_{1}\backslash X
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT \ italic_X
and
Γ
2
\
X
\
subscript
Γ
2
𝑋
\Gamma_{2}\backslash X
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT \ italic_X
are isospectral if and only if they have the same first
N
𝑁
N
italic_N
eigenvalues (counted with multiplicities).
We note that the condition
|
Γ
i
|
−
1
>
ε
superscript
subscript
Γ
𝑖
1
𝜀
|\Gamma_{i}|^{-1}>\varepsilon
| roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT | start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT > italic_ε
cannot be omitted from Theorem
1.9
, as Example
5.3
shows.
1.4.
Isospectral towers of lens spaces
In order to state our results on isospectral towers we will need the following definitions.
Definition 1.10
.
A descending (respectively, ascending) tower of covers is a set of Riemannian manifolds
{
M
I
}
subscript
𝑀
𝐼
\{M_{I}\}
{ italic_M start_POSTSUBSCRIPT italic_I end_POSTSUBSCRIPT }
indexed by a poset
𝒮
𝒮
\mathcal{S}
caligraphic_S
such that if
I
<
J
𝐼
𝐽
I<J
italic_I < italic_J
, then there is a finite degree Riemannian covering
M
I
⟶
M
J
⟶
subscript
𝑀
𝐼
subscript
𝑀
𝐽
M_{I}\longrightarrow M_{J}
italic_M start_POSTSUBSCRIPT italic_I end_POSTSUBSCRIPT ⟶ italic_M start_POSTSUBSCRIPT italic_J end_POSTSUBSCRIPT
(respectively,
M
J
⟶
M
I
⟶
subscript
𝑀
𝐽
subscript
𝑀
𝐼
M_{J}\longrightarrow M_{I}
italic_M start_POSTSUBSCRIPT italic_J end_POSTSUBSCRIPT ⟶ italic_M start_POSTSUBSCRIPT italic_I end_POSTSUBSCRIPT
).
Towers of Riemannian manifolds appear frequently in the literature. As an example, seminal work of Buser and Sarnak
[
BS94
]
studied the growth of the systole along towers of arithmetic hyperbolic surfaces. This work was generalized to towers of arithmetic hyperbolic
3
3
3
3
-manifolds by Katz, Schaps and Vishne
[
KSV07
]
, and to arbitrary arithmetic locally symmetric spaces by Lapan, Linowitz, and Meyer
[
LLM23
]
.
Definition 1.11
.
If
{
M
I
}
subscript
𝑀
𝐼
\{M_{I}\}
{ italic_M start_POSTSUBSCRIPT italic_I end_POSTSUBSCRIPT }
and
{
N
I
}
subscript
𝑁
𝐼
\{N_{I}\}
{ italic_N start_POSTSUBSCRIPT italic_I end_POSTSUBSCRIPT }
are two towers of Riemannian manifolds indexed by a poset
𝒮
𝒮
\mathcal{S}
caligraphic_S
, then we say that
{
M
I
}
subscript
𝑀
𝐼
\{M_{I}\}
{ italic_M start_POSTSUBSCRIPT italic_I end_POSTSUBSCRIPT }
and
{
N
I
}
subscript
𝑁
𝐼
\{N_{I}\}
{ italic_N start_POSTSUBSCRIPT italic_I end_POSTSUBSCRIPT }
are a pair of isospectral towers if, for all
I
𝐼
I
italic_I
, the manifolds
M
I
subscript
𝑀
𝐼
M_{I}
italic_M start_POSTSUBSCRIPT italic_I end_POSTSUBSCRIPT
and
N
I
subscript
𝑁
𝐼
N_{I}
italic_N start_POSTSUBSCRIPT italic_I end_POSTSUBSCRIPT
are isospectral and not isometric.
In
[
Mc14
]
, McReynolds used a variant of Sunada’s method in order to construct pairs of isospectral (ascending) towers of Riemannian manifolds comprised of manifold quotients of symmetric spaces associated to non-compact Lie groups. Additional examples, which are not derivable from Sunada’s method, were obtained by Linowitz in
[
Li12
]
, in the context of quotients of products
𝐇
2
a
⁢
𝐇
3
b
superscript
subscript
𝐇
2
𝑎
superscript
subscript
𝐇
3
𝑏
\mathbf{H}_{2}^{a}\mathbf{H}_{3}^{b}
bold_H start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_a end_POSTSUPERSCRIPT bold_H start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_b end_POSTSUPERSCRIPT
of hyperbolic upper-half planes and upper-half spaces by discrete groups of isometries obtained via orders in quaternion algebras.
The following is the natural spherical analog of the aforementioned results.
Question 1.12
.
Do there exist isospectral towers of spherical manifolds?
In Section
6
we will completely answer this question by constructing isospectral towers of lens spaces.
Theorem 1.13
.
There exist infinitely many pairs of descending isospectral towers of lens spaces in every odd dimension
n
≥
5
𝑛
5
n\geq 5
italic_n ≥ 5
.
1.5.
Isospectrality between quotients of symmetric spaces
In
[
BGG98
]
, Brooks, Gornet, and Gustafson used Sunada’s method in order to construct arbitrarily large families of pairwise isospectral, non-isometric Riemann surfaces. More generally, Spatzier
[
Sp89
]
proved that every compact irreducible locally symmetric space admits a pair of isospectral finite covers provided its universal cover
X
=
G
/
K
𝑋
𝐺
𝐾
X=G/K
italic_X = italic_G / italic_K
satisfies that
G
𝐺
G
italic_G
is of type
A
n
subscript
A
𝑛
\textup{A}_{n}
A start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT
for
n
≥
26
𝑛
26
n\geq 26
italic_n ≥ 26
,
B
n
subscript
B
𝑛
\textup{B}_{n}
B start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT
or
D
n
subscript
D
𝑛
\textup{D}_{n}
D start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT
for
n
≥
13
𝑛
13
n\geq 13
italic_n ≥ 13
, or
C
n
subscript
C
𝑛
\textup{C}_{n}
C start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT
for
n
≥
27
𝑛
27
n\geq 27
italic_n ≥ 27
. After several more examples appeared, McReynolds
[
Mc14
, Cor. 1.2]
established the following result.
Theorem 1.14
(McReynolds)
.
Every non-compact irreducible simply connected symmetric space
X
𝑋
X
italic_X
admits isospectral and non-isometric locally symmetric spaces covered by
X
𝑋
X
italic_X
.
Actually, McReynolds proved that for any
n
𝑛
n
italic_n
there exist
n
𝑛
n
italic_n
closed isospectral non-isometric manifolds with universal cover
X
𝑋
X
italic_X
.
The aim of Section
7
is to discuss the analogous situation for locally symmetric spaces of compact type, which turns out to be very different from the non-compact type setting described above. For instance, there are many compact irreducible symmetric spaces that do not cover any manifold at all.
Therefore, a natural question is the following.
Question 1.15
.
Which compact simply connected irreducible symmetric spaces cover isospectral and non-isometric manifolds?
One of our results is the following.
Theorem 1.16
.
Let
G
𝐺
G
italic_G
be a compact connected simple Lie group of dimension at least
4
4
4
4
and let
g
0
subscript
𝑔
0
g_{0}
italic_g start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
be a bi-invariant metric on
G
𝐺
G
italic_G
(thus
(
G
,
g
0
)
𝐺
subscript
𝑔
0
(G,g_{0})
( italic_G , italic_g start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT )
is isometric to an irreducible symmetric space of group type).
Then
(
G
,
g
0
)
𝐺
subscript
𝑔
0
(G,g_{0})
( italic_G , italic_g start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT )
covers
isospectral and non-isometric manifolds, with the possible exception of
G
=
SU
⁡
(
3
)
𝐺
SU
3
G=\operatorname{SU}(3)
italic_G = roman_SU ( 3 )
,
Sp
⁡
(
2
)
Sp
2
\operatorname{Sp}(2)
roman_Sp ( 2 )
, and
G
2
subscript
G
2
\operatorname{G}_{2}
roman_G start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
.
The situation for compact irreducible symmetric spaces of non-group type is less unified, so a detailed description in this case is postponed to Section
7
.
Acknowledgments
The authors wishes to express their thanks to the referee for several helpful comments.
Furthermore, they are indebted to Loren Spice by a very useful answer in Mathoverflow to a question made by the first named author.
2.
Preliminaries
In this section we introduce fundamental tools that will be used throughout this article.
2.1.
Spherical space forms
We consider the
d
𝑑
d
italic_d
-dimensional sphere
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
with its Riemannian metric of constant sectional curvature one.
Its isometry group
Iso
⁡
(
S
d
)
Iso
superscript
𝑆
𝑑
\operatorname{Iso}(S^{d})
roman_Iso ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT )
is given by
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
via multiplication at the left, where the elements in
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
are considered as vertical vectors with
d
+
1
𝑑
1
d+1
italic_d + 1
entries and Euclidean norm one.
Similarly, the subgroup of preserving-orientation isometries satisfies
Iso
0
⁡
(
S
d
)
=
SO
⁡
(
d
+
1
)
superscript
Iso
0
superscript
𝑆
𝑑
SO
𝑑
1
\operatorname{Iso}^{0}(S^{d})=\operatorname{SO}(d+1)
roman_Iso start_POSTSUPERSCRIPT 0 end_POSTSUPERSCRIPT ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ) = roman_SO ( italic_d + 1 )
.
A
spherical space form
is a compact Riemannian manifold with constant sectional curvature.
Throughout this paper we will assume that the sectional curvature is one, unless explicitly stated otherwise, so that any
d
𝑑
d
italic_d
-dimensional spherical space form is covered by
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
.
More precisely, a spherical space form is isometric to
S
d
/
Γ
superscript
𝑆
𝑑
Γ
S^{d}/\Gamma
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ
, where
Γ
Γ
\Gamma
roman_Γ
is a discrete (hence finite) subgroup of
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
acting freely on
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
. The manifold
S
d
/
Γ
superscript
𝑆
𝑑
Γ
S^{d}/\Gamma
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ
is orientable if and only if
Γ
⊂
SO
⁡
(
d
+
1
)
Γ
SO
𝑑
1
\Gamma\subset\operatorname{SO}(d+1)
roman_Γ ⊂ roman_SO ( italic_d + 1 )
.
A non-trivial element
γ
𝛾
\gamma
italic_γ
in
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
acts freely on
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
(i.e. if
γ
⋅
x
=
x
⋅
𝛾
𝑥
𝑥
\gamma\cdot x=x
italic_γ ⋅ italic_x = italic_x
for some
x
∈
S
d
𝑥
superscript
𝑆
𝑑
x\in S^{d}
italic_x ∈ italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
, then
γ
=
I
d
+
1
𝛾
subscript
I
𝑑
1
\gamma=\operatorname{I}_{d+1}
italic_γ = roman_I start_POSTSUBSCRIPT italic_d + 1 end_POSTSUBSCRIPT
) if
+
1
1
+1
+ 1
is not an eigenvalue of
γ
𝛾
\gamma
italic_γ
.
One can see that the only even-dimensional spherical space forms are spheres
S
2
⁢
n
superscript
𝑆
2
𝑛
S^{2n}
italic_S start_POSTSUPERSCRIPT 2 italic_n end_POSTSUPERSCRIPT
and real projective spaces
P
2
⁢
n
⁢
(
ℝ
)
superscript
𝑃
2
𝑛
ℝ
P^{2n}(\mathbb{R})
italic_P start_POSTSUPERSCRIPT 2 italic_n end_POSTSUPERSCRIPT ( blackboard_R )
.
The latter is not orientable since it is the quotient by
{
±
I
2
⁢
n
+
1
}
plus-or-minus
subscript
I
2
𝑛
1
\{\pm\operatorname{I}_{2n+1}\}
{ ± roman_I start_POSTSUBSCRIPT 2 italic_n + 1 end_POSTSUBSCRIPT }
, which is not contained in
SO
⁡
(
2
⁢
n
+
1
)
SO
2
𝑛
1
\operatorname{SO}(2n+1)
roman_SO ( 2 italic_n + 1 )
.
Every odd-dimensional spherical space form is orientable.
The classification of spherical space forms was obtained by Wolf
[
Wo
]
following techniques due to Vincent (see
[
Wo
, §5.1]
for a clear explanation).
Although we will use it several times along this article, we omit the statement because it is quite technical and long, though any reference will be to a precise place in
[
Wo
]
(or
[
Wo01
, §3–5]
).
Now, let
Γ
Γ
\Gamma
roman_Γ
be an arbitrary finite subgroup of
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
.
The quotient
S
d
/
Γ
superscript
𝑆
𝑑
Γ
S^{d}/\Gamma
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ
has a structure of a (Riemannian) good orbifold and is called a
spherical orbifold
.
Two spherical orbifolds
S
d
/
Γ
1
superscript
𝑆
𝑑
subscript
Γ
1
S^{d}/\Gamma_{1}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
S
d
/
Γ
2
superscript
𝑆
𝑑
subscript
Γ
2
S^{d}/\Gamma_{2}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are isometric if and only if
Γ
1
subscript
Γ
1
\Gamma_{1}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
Γ
2
subscript
Γ
2
\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are conjugate in
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
.
2.2.
Spectral generating functions
As usual, the
spectrum
of a (compact) Riemannian manifold
M
𝑀
M
italic_M
is the spectrum of its associated Laplace-Beltrami operator; that is, the the spectrum of
M
𝑀
M
italic_M
is the collection of Laplace-Beltrami eigenvalues counted with multiplicity. We denote this spectrum by
Spec
⁡
(
M
,
g
)
Spec
𝑀
𝑔
\operatorname{Spec}(M,g)
roman_Spec ( italic_M , italic_g )
.
The spectra of spheres have been known for a long time.
The eigenfunctions are precisely the spherical harmonics restricted to the corresponding sphere.
More precisely, by denoting by
ℋ
k
subscript
ℋ
𝑘
\mathcal{H}_{k}
caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
the space of harmonic (w.r.t. the euclidean Laplacian on
ℝ
d
+
1
superscript
ℝ
𝑑
1
\mathbb{R}^{d+1}
blackboard_R start_POSTSUPERSCRIPT italic_d + 1 end_POSTSUPERSCRIPT
) homogeneous complex polynomials of degree
k
𝑘
k
italic_k
in
d
+
1
𝑑
1
d+1
italic_d + 1
variables, the restriction of
f
∈
ℋ
k
𝑓
subscript
ℋ
𝑘
f\in\mathcal{H}_{k}
italic_f ∈ caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
to
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
is an eigenfunction of the Laplacian
Δ
Δ
\Delta
roman_Δ
of
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
with eigenvalue
λ
k
:=
k
⁢
(
k
+
d
−
1
)
assign
subscript
𝜆
𝑘
𝑘
𝑘
𝑑
1
\lambda_{k}:=k(k+d-1)
italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT := italic_k ( italic_k + italic_d - 1 )
.
Moreover, since
L
2
⁢
(
S
d
)
≃
⨁
k
≥
0
ℋ
k
similar-to-or-equals
superscript
𝐿
2
superscript
𝑆
𝑑
subscript
direct-sum
𝑘
0
subscript
ℋ
𝑘
L^{2}(S^{d})\simeq\bigoplus_{k\geq 0}\mathcal{H}_{k}
italic_L start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ) ≃ ⨁ start_POSTSUBSCRIPT italic_k ≥ 0 end_POSTSUBSCRIPT caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
because polynomials are dense in the space of continuous functions,
Spec
⁡
(
S
d
)
Spec
superscript
𝑆
𝑑
\operatorname{Spec}(S^{d})
roman_Spec ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT )
is given by the multiset
(2.1)
Spec
⁡
(
S
d
)
=
{
{
λ
k
,
…
,
λ
k
⏟
dim
ℋ
k
∣
k
≥
0
}
}
.
Spec
superscript
𝑆
𝑑
conditional-set
subscript
⏟
subscript
𝜆
𝑘
…
subscript
𝜆
𝑘
dimension
subscript
ℋ
𝑘
𝑘
0
\operatorname{Spec}(S^{d})=\Big{\{}\!\!\Big{\{}\underbrace{\lambda_{k},\dots,%
\lambda_{k}}_{\dim\mathcal{H}_{k}}\mid k\geq 0\Big{\}}\!\!\Big{\}}.
roman_Spec ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ) = { { under⏟ start_ARG italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT , … , italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT end_ARG start_POSTSUBSCRIPT roman_dim caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT end_POSTSUBSCRIPT ∣ italic_k ≥ 0 } } .
There is a well defined Laplacian on every good orbifold (see e.g.
[
Go12
]
).
In this article, we will assume for simplicity that the good orbifold is of the form
M
/
Γ
𝑀
Γ
M/\Gamma
italic_M / roman_Γ
with
M
𝑀
M
italic_M
a compact Riemannian manifold and
Γ
Γ
\Gamma
roman_Γ
is a group acting effectively and by isometries on
M
𝑀
M
italic_M
.
Thus, every
Γ
Γ
\Gamma
roman_Γ
-invariant eigenfunction on
M
𝑀
M
italic_M
descends to an eigenfunction on
M
/
Γ
𝑀
Γ
M/\Gamma
italic_M / roman_Γ
with the same eigenvalue, and moreover, every eigenfunction on
M
𝑀
M
italic_M
is of this form.
We now apply the above paragraph to our case of interest.
Let
Γ
Γ
\Gamma
roman_Γ
be a finite subgroup of
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
.
Then
Γ
Γ
\Gamma
roman_Γ
acts on
ℋ
k
subscript
ℋ
𝑘
\mathcal{H}_{k}
caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
by
(
γ
⋅
f
)
⁢
(
x
)
=
f
⁢
(
γ
−
1
⁢
x
)
⋅
𝛾
𝑓
𝑥
𝑓
superscript
𝛾
1
𝑥
(\gamma\cdot f)(x)=f(\gamma^{-1}x)
( italic_γ ⋅ italic_f ) ( italic_x ) = italic_f ( italic_γ start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT italic_x )
; we denote by
ℋ
k
Γ
superscript
subscript
ℋ
𝑘
Γ
\mathcal{H}_{k}^{\Gamma}
caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT
the subspace of
Γ
Γ
\Gamma
roman_Γ
-invariant elements of
ℋ
k
subscript
ℋ
𝑘
\mathcal{H}_{k}
caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
.
Note that
f
∈
ℋ
k
𝑓
subscript
ℋ
𝑘
f\in\mathcal{H}_{k}
italic_f ∈ caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
is
Γ
Γ
\Gamma
roman_Γ
-invariant considered as a function on
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
if and only if
f
∈
ℋ
k
Γ
𝑓
superscript
subscript
ℋ
𝑘
Γ
f\in\mathcal{H}_{k}^{\Gamma}
italic_f ∈ caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT
.
We obtain that
(2.2)
Spec
⁡
(
S
d
/
Γ
)
=
{
{
λ
k
,
…
,
λ
k
⏟
dim
ℋ
k
Γ
∣
k
≥
0
}
}
.
Spec
superscript
𝑆
𝑑
Γ
conditional-set
subscript
⏟
subscript
𝜆
𝑘
…
subscript
𝜆
𝑘
dimension
superscript
subscript
ℋ
𝑘
Γ
𝑘
0
\operatorname{Spec}(S^{d}/\Gamma)=\Big{\{}\!\!\Big{\{}\underbrace{\lambda_{k},%
\dots,\lambda_{k}}_{\dim\mathcal{H}_{k}^{\Gamma}}\mid k\geq 0\Big{\}}\!\!\Big{%
\}}.
roman_Spec ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ ) = { { under⏟ start_ARG italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT , … , italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT end_ARG start_POSTSUBSCRIPT roman_dim caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT end_POSTSUBSCRIPT ∣ italic_k ≥ 0 } } .
Ikeda was the first to consider inverse spectral problems for spherical space forms.
His main tool was the generating function associated to a spherical orbifold
S
d
/
Γ
superscript
𝑆
𝑑
Γ
S^{d}/\Gamma
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ
given by
(2.3)
F
Γ
⁢
(
z
)
:=
∑
k
≥
0
dim
ℋ
k
Γ
⁢
z
k
.
assign
subscript
𝐹
Γ
𝑧
subscript
𝑘
0
dimension
superscript
subscript
ℋ
𝑘
Γ
superscript
𝑧
𝑘
F_{\Gamma}(z):=\sum_{k\geq 0}\dim\mathcal{H}_{k}^{\Gamma}\,z^{k}.
italic_F start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_z ) := ∑ start_POSTSUBSCRIPT italic_k ≥ 0 end_POSTSUBSCRIPT roman_dim caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT italic_z start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT .
Clearly, two spherical orbifolds
S
d
/
Γ
1
,
S
d
/
Γ
2
superscript
𝑆
𝑑
subscript
Γ
1
superscript
𝑆
𝑑
subscript
Γ
2
S^{d}/\Gamma_{1},S^{d}/\Gamma_{2}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are isospectral (i.e.
Spec
⁡
(
S
d
/
Γ
1
)
=
Spec
⁡
(
S
d
/
Γ
2
)
Spec
superscript
𝑆
𝑑
subscript
Γ
1
Spec
superscript
𝑆
𝑑
subscript
Γ
2
\operatorname{Spec}(S^{d}/\Gamma_{1})=\operatorname{Spec}(S^{d}/\Gamma_{2})
roman_Spec ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ) = roman_Spec ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT )
) if and only if
F
Γ
1
⁢
(
z
)
=
F
Γ
2
⁢
(
z
)
subscript
𝐹
subscript
Γ
1
𝑧
subscript
𝐹
subscript
Γ
2
𝑧
F_{\Gamma_{1}}(z)=F_{\Gamma_{2}}(z)
italic_F start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_z ) = italic_F start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_z )
.
Ikeda
[
Ik80
, Thm. 2.2]
proved that
(2.4)
F
Γ
⁢
(
z
)
=
1
−
z
2
|
Γ
|
⁢
∑
γ
∈
Γ
1
det
(
I
d
−
γ
⁢
z
)
,
subscript
𝐹
Γ
𝑧
1
superscript
𝑧
2
Γ
subscript
𝛾
Γ
1
subscript
I
𝑑
𝛾
𝑧
F_{\Gamma}(z)=\frac{1-z^{2}}{|\Gamma|}\sum_{\gamma\in\Gamma}\frac{1}{\det(%
\operatorname{I}_{d}-\gamma z)},
italic_F start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_z ) = divide start_ARG 1 - italic_z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG | roman_Γ | end_ARG ∑ start_POSTSUBSCRIPT italic_γ ∈ roman_Γ end_POSTSUBSCRIPT divide start_ARG 1 end_ARG start_ARG roman_det ( roman_I start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT - italic_γ italic_z ) end_ARG ,
where
det
(
I
d
−
γ
⁢
z
)
=
∏
λ
∈
Spec
⁡
(
γ
)
(
1
−
λ
⁢
z
)
subscript
I
𝑑
𝛾
𝑧
subscript
product
𝜆
Spec
𝛾
1
𝜆
𝑧
\det(\operatorname{I}_{d}-\gamma z)=\prod_{\lambda\in\operatorname{Spec}(%
\gamma)}(1-\lambda z)
roman_det ( roman_I start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT - italic_γ italic_z ) = ∏ start_POSTSUBSCRIPT italic_λ ∈ roman_Spec ( italic_γ ) end_POSTSUBSCRIPT ( 1 - italic_λ italic_z )
. We note that here,
Spec
⁡
(
γ
)
Spec
𝛾
\operatorname{Spec}(\gamma)
roman_Spec ( italic_γ )
denotes the set of eigenvalues of
γ
𝛾
\gamma
italic_γ
, counted with multiplicities. As an immediate consequence, he obtain the following result that can be considered as a precursor of Sunada’s method (
[
Ik80
, Cor. 2.3]
):
Let
Γ
1
subscript
Γ
1
\Gamma_{1}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
Γ
2
subscript
Γ
2
\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
be finite subgroups of
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
.
If there is a bijection
ϕ
:
Γ
1
→
Γ
2
:
italic-ϕ
→
subscript
Γ
1
subscript
Γ
2
\phi:\Gamma_{1}\to\Gamma_{2}
italic_ϕ : roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT → roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
satisfying that
Spec
⁡
(
γ
)
=
Spec
⁡
(
ϕ
⁢
(
γ
)
)
Spec
𝛾
Spec
italic-ϕ
𝛾
\operatorname{Spec}(\gamma)=\operatorname{Spec}(\phi(\gamma))
roman_Spec ( italic_γ ) = roman_Spec ( italic_ϕ ( italic_γ ) )
for all
γ
∈
Γ
1
𝛾
subscript
Γ
1
\gamma\in\Gamma_{1}
italic_γ ∈ roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
, then the spherical orbifolds
S
d
/
Γ
1
superscript
𝑆
𝑑
subscript
Γ
1
S^{d}/\Gamma_{1}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
S
d
/
Γ
2
superscript
𝑆
𝑑
subscript
Γ
2
S^{d}/\Gamma_{2}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are isospectral.
Ikeda constructed examples of isospectral spherical space forms via this result in
[
Ik83
]
.
We next show a more general version obtained by Wolf
[
Wo01
, Cor. 2.13]
, which replaces the condition involving the spectra of the matrices by the following well-known notion.
Definition 2.1
.
Two subgroups
Γ
1
,
Γ
2
subscript
Γ
1
subscript
Γ
2
\Gamma_{1},\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
of
G
𝐺
G
italic_G
are called
almost conjugate
if there is a bijection
ϕ
:
Γ
1
→
Γ
2
:
italic-ϕ
→
subscript
Γ
1
subscript
Γ
2
\phi:\Gamma_{1}\to\Gamma_{2}
italic_ϕ : roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT → roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
such that
h
ℎ
h
italic_h
and
ϕ
⁢
(
h
)
italic-ϕ
ℎ
\phi(h)
italic_ϕ ( italic_h )
are conjugate in
G
𝐺
G
italic_G
for all
h
∈
Γ
1
ℎ
subscript
Γ
1
h\in\Gamma_{1}
italic_h ∈ roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
.
Theorem 2.2
.
Let
M
𝑀
M
italic_M
be a compact Riemannian manifold.
If
Γ
1
subscript
Γ
1
\Gamma_{1}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
Γ
2
subscript
Γ
2
\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are almost conjugate finite subgroups of
Iso
⁡
(
M
)
Iso
𝑀
\operatorname{Iso}(M)
roman_Iso ( italic_M )
, then the Riemannian good orbifolds
M
/
Γ
1
𝑀
subscript
Γ
1
M/\Gamma_{1}
italic_M / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
M
/
Γ
2
𝑀
subscript
Γ
2
M/\Gamma_{2}
italic_M / roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are strongly isospectral.
Strongly isospectral manifolds satisfy the condition that, for any natural vector bundle, the natural strongly elliptic differential operators acting on square integrable sections of the corresponding vector bundles are isospectral, that is, they have the same spectra.
Instances of these natural differential operators are the Laplace-Beltrami operator, the Hodge-Laplace operator acting on
p
𝑝
p
italic_p
-forms, the Lichnerowicz Laplacian acting on (symmetric)
k
𝑘
k
italic_k
-tensors, etc.
For any of these operators, its spectrum on a good orbifold
M
/
Γ
𝑀
Γ
M/\Gamma
italic_M / roman_Γ
is obtained in a similar way as it was done for the Laplace-Beltrami operator above, namely, the eigensections on
M
/
Γ
𝑀
Γ
M/\Gamma
italic_M / roman_Γ
come from
Γ
Γ
\Gamma
roman_Γ
-eigensections on
M
𝑀
M
italic_M
.
2.3.
Lens spaces
We now focus on lens spaces, which are quotients of odd-dimensional spheres by cyclic groups under free actions.
Although lens spaces are topological spaces, we endow them with the constant sectional curvature one Riemannian metric so that they are spherical space forms.
In fact, lens spaces are the odd-dimensional spherical space forms with cyclic fundamental group.
Any of them is isometric to one of the following:
for
q
∈
ℕ
𝑞
ℕ
q\in\mathbb{N}
italic_q ∈ blackboard_N
and
s
=
(
s
1
,
…
,
s
n
)
∈
ℤ
n
𝑠
subscript
𝑠
1
…
subscript
𝑠
𝑛
superscript
ℤ
𝑛
s=(s_{1},\dots,s_{n})\in\mathbb{Z}^{n}
italic_s = ( italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ) ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
with
gcd
⁡
(
q
,
s
i
)
=
1
𝑞
subscript
𝑠
𝑖
1
\gcd(q,s_{i})=1
roman_gcd ( italic_q , italic_s start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) = 1
for all
i
𝑖
i
italic_i
, we set
L
⁢
(
q
;
s
)
=
S
2
⁢
n
−
1
/
Γ
q
;
s
𝐿
𝑞
𝑠
superscript
𝑆
2
𝑛
1
subscript
Γ
𝑞
𝑠
L(q;s)=S^{2n-1}/\Gamma_{q;s}
italic_L ( italic_q ; italic_s ) = italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT italic_q ; italic_s end_POSTSUBSCRIPT
, where
Γ
q
;
s
subscript
Γ
𝑞
𝑠
\Gamma_{q;s}
roman_Γ start_POSTSUBSCRIPT italic_q ; italic_s end_POSTSUBSCRIPT
is the group generated by
(2.5)
γ
q
;
s
:=
(
R
⁢
(
2
⁢
π
⁢
s
1
q
)
⋱
R
⁢
(
2
⁢
π
⁢
s
n
q
)
)
,
where
⁢
R
⁢
(
θ
)
=
(
cos
⁡
θ
sin
⁡
θ
−
sin
⁡
θ
cos
⁡
θ
)
.
formulae-sequence
assign
subscript
𝛾
𝑞
𝑠
matrix
𝑅
2
𝜋
subscript
𝑠
1
𝑞
missing-subexpression
⋱
missing-subexpression
missing-subexpression
𝑅
2
𝜋
subscript
𝑠
𝑛
𝑞
where
𝑅
𝜃
matrix
𝜃
𝜃
𝜃
𝜃
\gamma_{q;s}:=\begin{pmatrix}R(\tfrac{2\pi s_{1}}{q})\\
&\ddots\\
&&R(\tfrac{2\pi s_{n}}{q})\end{pmatrix},\qquad\text{where}\ R(\theta)=\begin{%
pmatrix}\cos\theta&\sin\theta\\
-\sin\theta&\cos\theta\end{pmatrix}.
italic_γ start_POSTSUBSCRIPT italic_q ; italic_s end_POSTSUBSCRIPT := ( start_ARG start_ROW start_CELL italic_R ( divide start_ARG 2 italic_π italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_ARG start_ARG italic_q end_ARG ) end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL ⋱ end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL italic_R ( divide start_ARG 2 italic_π italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT end_ARG start_ARG italic_q end_ARG ) end_CELL end_ROW end_ARG ) , where italic_R ( italic_θ ) = ( start_ARG start_ROW start_CELL roman_cos italic_θ end_CELL start_CELL roman_sin italic_θ end_CELL end_ROW start_ROW start_CELL - roman_sin italic_θ end_CELL start_CELL roman_cos italic_θ end_CELL end_ROW end_ARG ) .
Sometimes we will write
L
⁢
(
q
;
s
1
,
…
,
s
n
)
=
L
⁢
(
q
;
s
)
𝐿
𝑞
subscript
𝑠
1
…
subscript
𝑠
𝑛
𝐿
𝑞
𝑠
L(q;s_{1},\dots,s_{n})=L(q;s)
italic_L ( italic_q ; italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ) = italic_L ( italic_q ; italic_s )
.
The condition
gcd
⁡
(
q
,
s
i
)
=
1
𝑞
subscript
𝑠
𝑖
1
\gcd(q,s_{i})=1
roman_gcd ( italic_q , italic_s start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) = 1
for all
i
𝑖
i
italic_i
ensures that
Γ
q
;
s
subscript
Γ
𝑞
𝑠
\Gamma_{q;s}
roman_Γ start_POSTSUBSCRIPT italic_q ; italic_s end_POSTSUBSCRIPT
acts freely on
S
2
⁢
n
−
1
superscript
𝑆
2
𝑛
1
S^{2n-1}
italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT
.
The quotient
L
⁢
(
q
;
s
)
=
S
2
⁢
n
−
1
/
Γ
q
;
s
𝐿
𝑞
𝑠
superscript
𝑆
2
𝑛
1
subscript
Γ
𝑞
𝑠
L(q;s)=S^{2n-1}/\Gamma_{q;s}
italic_L ( italic_q ; italic_s ) = italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT italic_q ; italic_s end_POSTSUBSCRIPT
with
s
∈
ℤ
n
𝑠
superscript
ℤ
𝑛
s\in\mathbb{Z}^{n}
italic_s ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
satisfying the weaker condition
gcd
⁡
(
q
,
s
1
,
…
,
s
n
)
=
1
𝑞
subscript
𝑠
1
…
subscript
𝑠
𝑛
1
\gcd(q,s_{1},\dots,s_{n})=1
roman_gcd ( italic_q , italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ) = 1
is called a
lens orbifold
.
Proposition 2.3
.
Let
L
=
L
⁢
(
q
;
s
)
𝐿
𝐿
𝑞
𝑠
L=L(q;s)
italic_L = italic_L ( italic_q ; italic_s )
and
L
′
=
L
⁢
(
q
;
s
′
)
superscript
𝐿
′
𝐿
𝑞
superscript
𝑠
′
L^{\prime}=L(q;s^{\prime})
italic_L start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT = italic_L ( italic_q ; italic_s start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT )
be two lens orbifolds of dimension
2
⁢
n
−
1
2
𝑛
1
2n-1
2 italic_n - 1
.
The following assertions are equivalent:
(1)
L
⁢
(
q
;
s
)
𝐿
𝑞
𝑠
L(q;s)
italic_L ( italic_q ; italic_s )
and
L
⁢
(
q
;
s
′
)
𝐿
𝑞
superscript
𝑠
′
L(q;s^{\prime})
italic_L ( italic_q ; italic_s start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT )
are homeomorphic.
(2)
L
⁢
(
q
;
s
)
𝐿
𝑞
𝑠
L(q;s)
italic_L ( italic_q ; italic_s )
and
L
⁢
(
q
;
s
′
)
𝐿
𝑞
superscript
𝑠
′
L(q;s^{\prime})
italic_L ( italic_q ; italic_s start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT )
are diffeomorphic.
(3)
L
⁢
(
q
;
s
)
𝐿
𝑞
𝑠
L(q;s)
italic_L ( italic_q ; italic_s )
and
L
⁢
(
q
;
s
′
)
𝐿
𝑞
superscript
𝑠
′
L(q;s^{\prime})
italic_L ( italic_q ; italic_s start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT )
are isometric.
(4)
There are
σ
𝜎
\sigma
italic_σ
a permutation of
{
1
,
…
,
n
}
1
…
𝑛
\{1,\dots,n\}
{ 1 , … , italic_n }
,
ϵ
i
∈
{
±
1
}
subscript
italic-ϵ
𝑖
plus-or-minus
1
\epsilon_{i}\in\{\pm 1\}
italic_ϵ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ∈ { ± 1 }
for each
i
=
1
,
…
,
n
𝑖
1
…
𝑛
i=1,\dots,n
italic_i = 1 , … , italic_n
, and
t
∈
ℤ
𝑡
ℤ
t\in\mathbb{Z}
italic_t ∈ blackboard_Z
prime to
k
𝑘
k
italic_k
such that
(2.6)
s
σ
⁢
(
i
)
≡
ϵ
i
⁢
t
⁢
s
i
(
mod
q
)
for all
⁢
i
=
1
,
…
,
n
.
formulae-sequence
subscript
𝑠
𝜎
𝑖
annotated
subscript
italic-ϵ
𝑖
𝑡
subscript
𝑠
𝑖
pmod
𝑞
for all
𝑖
1
…
𝑛
s_{\sigma(i)}\equiv\epsilon_{i}ts_{i}\pmod{q}\qquad\text{for all }i=1,\dots,n.
italic_s start_POSTSUBSCRIPT italic_σ ( italic_i ) end_POSTSUBSCRIPT ≡ italic_ϵ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT italic_t italic_s start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_MODIFIER ( roman_mod start_ARG italic_q end_ARG ) end_MODIFIER for all italic_i = 1 , … , italic_n .
Concerning the spectrum of a lens orbifold
L
:=
L
⁢
(
q
;
s
)
assign
𝐿
𝐿
𝑞
𝑠
L:=L(q;s)
italic_L := italic_L ( italic_q ; italic_s )
, it follows form (
2.4
) that
(2.7)
F
L
⁢
(
z
)
:=
F
Γ
q
,
s
⁢
(
z
)
=
1
−
z
2
q
⁢
∑
h
=
0
q
−
1
1
(
z
−
ξ
q
h
⁢
s
1
)
⁢
(
z
−
ξ
q
−
h
⁢
s
1
)
⁢
…
⁢
(
z
−
ξ
q
h
⁢
s
n
)
⁢
(
z
−
ξ
q
−
h
⁢
s
n
)
,
assign
subscript
𝐹
𝐿
𝑧
subscript
𝐹
subscript
Γ
𝑞
𝑠
𝑧
1
superscript
𝑧
2
𝑞
superscript
subscript
ℎ
0
𝑞
1
1
𝑧
superscript
subscript
𝜉
𝑞
ℎ
subscript
𝑠
1
𝑧
superscript
subscript
𝜉
𝑞
ℎ
subscript
𝑠
1
…
𝑧
superscript
subscript
𝜉
𝑞
ℎ
subscript
𝑠
𝑛
𝑧
superscript
subscript
𝜉
𝑞
ℎ
subscript
𝑠
𝑛
F_{L}(z):=F_{\Gamma_{q,s}}(z)=\frac{1-z^{2}}{q}\sum_{h=0}^{q-1}\frac{1}{(z-\xi%
_{q}^{hs_{1}})(z-\xi_{q}^{-hs_{1}})\dots(z-\xi_{q}^{hs_{n}})(z-\xi_{q}^{-hs_{n%
}})},
italic_F start_POSTSUBSCRIPT italic_L end_POSTSUBSCRIPT ( italic_z ) := italic_F start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT italic_q , italic_s end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_z ) = divide start_ARG 1 - italic_z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG italic_q end_ARG ∑ start_POSTSUBSCRIPT italic_h = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_q - 1 end_POSTSUPERSCRIPT divide start_ARG 1 end_ARG start_ARG ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_h italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT - italic_h italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) … ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_h italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT - italic_h italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) end_ARG ,
where
ξ
q
=
e
2
⁢
π
⁢
i
/
q
subscript
𝜉
𝑞
superscript
𝑒
2
𝜋
i
𝑞
\xi_{q}=e^{2\pi\mathrm{i}/q}
italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT = italic_e start_POSTSUPERSCRIPT 2 italic_π roman_i / italic_q end_POSTSUPERSCRIPT
.
This expression first appeared in
[
IY79
, Thm. 3.2]
.
An alternative expression (see
[
LMR21
, Thm. 3.1]
) is given by
(2.8)
F
L
⁢
(
z
)
=
1
(
1
−
z
2
)
n
−
1
⁢
∑
k
≥
0
N
ℒ
⁢
(
k
)
⁢
z
k
,
subscript
𝐹
𝐿
𝑧
1
superscript
1
superscript
𝑧
2
𝑛
1
subscript
𝑘
0
subscript
𝑁
ℒ
𝑘
superscript
𝑧
𝑘
F_{L}(z)=\frac{1}{(1-z^{2})^{n-1}}\sum_{k\geq 0}N_{\mathcal{L}}(k)z^{k},
italic_F start_POSTSUBSCRIPT italic_L end_POSTSUBSCRIPT ( italic_z ) = divide start_ARG 1 end_ARG start_ARG ( 1 - italic_z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ) start_POSTSUPERSCRIPT italic_n - 1 end_POSTSUPERSCRIPT end_ARG ∑ start_POSTSUBSCRIPT italic_k ≥ 0 end_POSTSUBSCRIPT italic_N start_POSTSUBSCRIPT caligraphic_L end_POSTSUBSCRIPT ( italic_k ) italic_z start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT ,
where
ℒ
ℒ
\mathcal{L}
caligraphic_L
is the associated
congruence lattice
of
L
⁢
(
q
;
s
)
𝐿
𝑞
𝑠
L(q;s)
italic_L ( italic_q ; italic_s )
given by
(2.9)
ℒ
⁢
(
q
;
s
)
:=
{
(
a
1
,
…
,
a
n
)
∈
ℤ
n
:
a
1
⁢
s
1
+
⋯
+
a
n
⁢
s
n
≡
0
(
mod
q
)
}
assign
ℒ
𝑞
𝑠
conditional-set
subscript
𝑎
1
…
subscript
𝑎
𝑛
superscript
ℤ
𝑛
subscript
𝑎
1
subscript
𝑠
1
⋯
subscript
𝑎
𝑛
subscript
𝑠
𝑛
annotated
0
pmod
𝑞
\mathcal{L}(q;s):=\{(a_{1},\dots,a_{n})\in\mathbb{Z}^{n}:a_{1}s_{1}+\dots+a_{n%
}s_{n}\equiv 0\pmod{q}\}
caligraphic_L ( italic_q ; italic_s ) := { ( italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ) ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT : italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT + ⋯ + italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ≡ 0 start_MODIFIER ( roman_mod start_ARG italic_q end_ARG ) end_MODIFIER }
and
(2.10)
N
ℒ
⁢
(
k
)
=
#
⁢
{
(
a
1
,
…
,
a
n
)
∈
ℤ
n
:
|
a
1
|
+
⋯
+
|
a
n
|
=
k
}
.
subscript
𝑁
ℒ
𝑘
#
conditional-set
subscript
𝑎
1
…
subscript
𝑎
𝑛
superscript
ℤ
𝑛
subscript
𝑎
1
⋯
subscript
𝑎
𝑛
𝑘
N_{\mathcal{L}}(k)=\#\{(a_{1},\dots,a_{n})\in\mathbb{Z}^{n}:|a_{1}|+\dots+|a_{%
n}|=k\}.
italic_N start_POSTSUBSCRIPT caligraphic_L end_POSTSUBSCRIPT ( italic_k ) = # { ( italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ) ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT : | italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT | + ⋯ + | italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT | = italic_k } .
By expanding the right hand side of (
2.8
), one obtains
(2.11)
dim
ℋ
k
Γ
=
∑
r
=
0
⌊
k
/
2
⌋
(
r
+
n
−
2
n
−
2
)
⁢
N
ℒ
⁢
(
k
−
2
⁢
r
)
,
dimension
superscript
subscript
ℋ
𝑘
Γ
superscript
subscript
𝑟
0
𝑘
2
binomial
𝑟
𝑛
2
𝑛
2
subscript
𝑁
ℒ
𝑘
2
𝑟
\dim\mathcal{H}_{k}^{\Gamma}=\sum_{r=0}^{\lfloor k/2\rfloor}\binom{r+n-2}{n-2}%
N_{\mathcal{L}}(k-2r),
roman_dim caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT = ∑ start_POSTSUBSCRIPT italic_r = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⌊ italic_k / 2 ⌋ end_POSTSUPERSCRIPT ( FRACOP start_ARG italic_r + italic_n - 2 end_ARG start_ARG italic_n - 2 end_ARG ) italic_N start_POSTSUBSCRIPT caligraphic_L end_POSTSUBSCRIPT ( italic_k - 2 italic_r ) ,
which was established in
[
LMR16
, Thm. 3.5]
.
3.
Eigenvalue equivalence
The
eigenvalue spectrum
of a closed Riemannian orbifold is its set of eigenvalues for the Laplace-Beltrami operator, ignoring multiplicities. Two orbifolds are said to be
eigenvalue equivalent
if their eigenvalue spectra coincide.
We will exhibit two different constructions of eigenvalue equivalent spherical orbifolds with different volume.
The first one will closely follow the work of Leininger, McReynolds, Neumann, and Reid
[
LMNR07
]
, who considered the analogous problem for hyperbolic
n
𝑛
n
italic_n
-manifolds.
The second one describes the eigenvalue spectrum of an arbitrary lens space making use of the approach in
[
LMR16
]
, which is summarized in
[
LMR21
, §2–4]
.
We conclude this section with examples of eigenvalue equivalent Riemannian manifolds of different dimensions.
3.1.
Eigenvalue equivalent spherical orbifolds
Definition 3.1
.
Let
G
𝐺
G
italic_G
be a finite group. Two subgroups
H
𝐻
H
italic_H
and
K
𝐾
K
italic_K
of
G
𝐺
G
italic_G
are fixed point equivalent if, for any finite dimensional complex representation
ρ
𝜌
\rho
italic_ρ
of
G
𝐺
G
italic_G
, the restriction
ρ
|
H
evaluated-at
𝜌
𝐻
\rho|_{H}
italic_ρ | start_POSTSUBSCRIPT italic_H end_POSTSUBSCRIPT
has a nontrivial fixed vector if and only if
ρ
|
K
evaluated-at
𝜌
𝐾
\rho|_{K}
italic_ρ | start_POSTSUBSCRIPT italic_K end_POSTSUBSCRIPT
does.
Our interest in fixed point equivalent subgroups of finite groups is the following refinement of Sunada’s method
[
LMNR07
, Theorem 2.6]
(note that almost conjugate subgroups as in Definition
2.1
are always fixed point equivalent
[
LMNR07
, Proposition 2.4]
).
Theorem 3.2
.
Let
H
𝐻
H
italic_H
and
K
𝐾
K
italic_K
be fixed point equivalent subgroups of a finite group
G
𝐺
G
italic_G
. If
M
𝑀
M
italic_M
is a compact Riemannian manifold and
π
1
⁢
(
M
)
subscript
𝜋
1
𝑀
\pi_{1}(M)
italic_π start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( italic_M )
admits a surjective homomorphism onto
G
𝐺
G
italic_G
, then the covers
M
H
subscript
𝑀
𝐻
M_{H}
italic_M start_POSTSUBSCRIPT italic_H end_POSTSUBSCRIPT
and
M
K
subscript
𝑀
𝐾
M_{K}
italic_M start_POSTSUBSCRIPT italic_K end_POSTSUBSCRIPT
associated to the pullbacks in
π
1
⁢
(
M
)
subscript
𝜋
1
𝑀
\pi_{1}(M)
italic_π start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( italic_M )
of
H
𝐻
H
italic_H
and
K
𝐾
K
italic_K
have the same sets of eigenvalues of the Laplace-Beltrami operator.
We now prove the existence of spherical orbifolds whose sets of eigenvalues of the Laplace-Beltrami operator coincide yet whose volumes are different.
Theorem 3.3
.
Let
n
≥
9
𝑛
9
n\geq 9
italic_n ≥ 9
. There exist
n
𝑛
n
italic_n
-dimensional spherical orbifolds
M
1
subscript
𝑀
1
M_{1}
italic_M start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
M
2
subscript
𝑀
2
M_{2}
italic_M start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
which are eigenvalue equivalent yet whose volumes satisfy
vol
⁢
(
M
2
)
=
3
⋅
vol
⁢
(
M
1
)
vol
subscript
𝑀
2
⋅
3
vol
subscript
𝑀
1
\mathrm{vol}(M_{2})=3\cdot\mathrm{vol}(M_{1})
roman_vol ( italic_M start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ) = 3 ⋅ roman_vol ( italic_M start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT )
.
Proof.
Theorem 3.2 of
[
LMNR07
]
shows that there exist subgroups
K
<
H
𝐾
𝐻
K<H
italic_K < italic_H
of
PSL
2
⁢
(
ℤ
/
9
⁢
ℤ
)
subscript
PSL
2
ℤ
9
ℤ
\mathrm{PSL}_{2}(\mathbb{Z}/9\mathbb{Z})
roman_PSL start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ( blackboard_Z / 9 blackboard_Z )
with
[
H
:
K
]
=
3
[H:K]=3
[ italic_H : italic_K ] = 3
and which are fixed point equivalent. An easy computation is SAGE shows that
PSL
2
⁢
(
ℤ
/
9
⁢
ℤ
)
subscript
PSL
2
ℤ
9
ℤ
\mathrm{PSL}_{2}(\mathbb{Z}/9\mathbb{Z})
roman_PSL start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ( blackboard_Z / 9 blackboard_Z )
is isomorphic to the subgroup
G
=
⟨
(
3
,
9
,
4
,
6
)
⁢
(
5
,
10
,
8
,
7
)
,
(
1
,
2
,
4
)
⁢
(
5
,
6
,
8
)
⁢
(
7
,
9
,
10
)
⟩
𝐺
3
9
4
6
5
10
8
7
1
2
4
5
6
8
7
9
10
G=\langle(3,9,4,6)(5,10,8,7),(1,2,4)(5,6,8)(7,9,10)\rangle
italic_G = ⟨ ( 3 , 9 , 4 , 6 ) ( 5 , 10 , 8 , 7 ) , ( 1 , 2 , 4 ) ( 5 , 6 , 8 ) ( 7 , 9 , 10 ) ⟩
of the permutation group
S
10
subscript
𝑆
10
S_{10}
italic_S start_POSTSUBSCRIPT 10 end_POSTSUBSCRIPT
. Identifying
S
10
subscript
𝑆
10
S_{10}
italic_S start_POSTSUBSCRIPT 10 end_POSTSUBSCRIPT
with the set of
10
×
10
10
10
10\times 10
10 × 10
permutation matrices in
O
⁡
(
10
)
O
10
\operatorname{O}(10)
roman_O ( 10 )
allows us to identify
G
𝐺
G
italic_G
with a subgroup of
O
⁡
(
10
)
<
O
⁡
(
n
+
1
)
O
10
O
𝑛
1
\operatorname{O}(10)<\operatorname{O}(n+1)
roman_O ( 10 ) < roman_O ( italic_n + 1 )
. We may therefore assume that
G
<
O
⁡
(
n
+
1
)
𝐺
O
𝑛
1
G<\operatorname{O}(n+1)
italic_G < roman_O ( italic_n + 1 )
. Let
M
=
S
n
/
G
𝑀
superscript
𝑆
𝑛
𝐺
M=S^{n}/G
italic_M = italic_S start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT / italic_G
and
M
1
,
M
2
subscript
𝑀
1
subscript
𝑀
2
M_{1},M_{2}
italic_M start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_M start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
be the covers of
M
𝑀
M
italic_M
associated to the pullbacks in
G
𝐺
G
italic_G
of
H
𝐻
H
italic_H
and
K
𝐾
K
italic_K
along the isomorphism
G
→
PSL
2
⁢
(
ℤ
/
9
⁢
ℤ
)
→
𝐺
subscript
PSL
2
ℤ
9
ℤ
G\to\mathrm{PSL}_{2}(\mathbb{Z}/9\mathbb{Z})
italic_G → roman_PSL start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ( blackboard_Z / 9 blackboard_Z )
. That
M
1
subscript
𝑀
1
M_{1}
italic_M start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
M
2
subscript
𝑀
2
M_{2}
italic_M start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
have the desired properties now follows from Theorem
3.2
.
∎
3.2.
Eigenvalue equivalent lens spaces
From the description (
2.2
) of the spectrum of the Laplace-Beltrami operator of a spherical orbifold
S
2
⁢
n
−
1
/
Γ
superscript
𝑆
2
𝑛
1
Γ
S^{2n-1}/\Gamma
italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / roman_Γ
, it follows immediately that the eigenvalue spectrum of
S
2
⁢
n
−
1
/
Γ
superscript
𝑆
2
𝑛
1
Γ
S^{2n-1}/\Gamma
italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / roman_Γ
is given by
(3.1)
ℰ
⁢
(
S
2
⁢
n
−
1
/
Γ
)
:=
{
λ
k
=
k
⁢
(
k
+
2
⁢
n
−
2
)
:
k
∈
ℕ
⁢
and
⁢
dim
ℋ
k
Γ
>
0
}
,
assign
ℰ
superscript
𝑆
2
𝑛
1
Γ
conditional-set
subscript
𝜆
𝑘
𝑘
𝑘
2
𝑛
2
𝑘
ℕ
and
dimension
superscript
subscript
ℋ
𝑘
Γ
0
\mathcal{E}(S^{2n-1}/\Gamma):=\{\lambda_{k}=k(k+2n-2):k\in\mathbb{N}\text{ and%
 }\dim\mathcal{H}_{k}^{\Gamma}>0\},
caligraphic_E ( italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / roman_Γ ) := { italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT = italic_k ( italic_k + 2 italic_n - 2 ) : italic_k ∈ blackboard_N and roman_dim caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT > 0 } ,
where
ℋ
k
subscript
ℋ
𝑘
\mathcal{H}_{k}
caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
denotes the space of harmonic homogeneous complex polynomials of degree
k
𝑘
k
italic_k
in
2
⁢
n
2
𝑛
2n
2 italic_n
variables.
We next focus in the particular case of lens spaces introduced in §
2.3
.
Theorem 3.4
.
The eigenvalue spectrum of a lens space
L
=
L
⁢
(
q
;
s
1
,
…
,
s
n
)
𝐿
𝐿
𝑞
subscript
𝑠
1
…
subscript
𝑠
𝑛
L=L(q;s_{1},\dots,s_{n})
italic_L = italic_L ( italic_q ; italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT )
is given by
(3.2)
ℰ
⁢
(
L
)
=
{
λ
2
⁢
k
:
k
∈
ℕ
0
}
∪
{
λ
k
0
⁢
(
L
)
+
2
⁢
k
:
k
∈
ℕ
0
}
,
ℰ
𝐿
conditional-set
subscript
𝜆
2
𝑘
𝑘
subscript
ℕ
0
conditional-set
subscript
𝜆
subscript
𝑘
0
𝐿
2
𝑘
𝑘
subscript
ℕ
0
\mathcal{E}(L)=\{\lambda_{2k}:k\in\mathbb{N}_{0}\}\cup\{\lambda_{k_{0}(L)+2k}:%
k\in\mathbb{N}_{0}\},
caligraphic_E ( italic_L ) = { italic_λ start_POSTSUBSCRIPT 2 italic_k end_POSTSUBSCRIPT : italic_k ∈ blackboard_N start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT } ∪ { italic_λ start_POSTSUBSCRIPT italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ( italic_L ) + 2 italic_k end_POSTSUBSCRIPT : italic_k ∈ blackboard_N start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT } ,
where
λ
k
=
k
⁢
(
k
+
2
⁢
n
−
2
)
subscript
𝜆
𝑘
𝑘
𝑘
2
𝑛
2
\lambda_{k}=k(k+2n-2)
italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT = italic_k ( italic_k + 2 italic_n - 2 )
and
(3.3)
k
0
(
L
)
=
min
{
k
∈
ℕ
:
k
is odd and there is
⁢
(
a
1
,
…
,
a
n
)
∈
ℤ
n
⁢
such that
|
a
1
|
+
⋯
+
|
a
n
|
=
k
⁢
and
⁢
a
1
⁢
s
1
+
⋯
+
a
n
⁢
s
n
≡
0
(
mod
q
)
}
.
k_{0}(L)=\min\left\{k\in\mathbb{N}:\begin{array}[]{l}\text{$k$ is odd and %
there is }(a_{1},\dots,a_{n})\in\mathbb{Z}^{n}\text{ such that}\\
|a_{1}|+\dots+|a_{n}|=k\text{ and }a_{1}s_{1}+\dots+a_{n}s_{n}\equiv 0\pmod{q}%
\end{array}\right\}.
italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ( italic_L ) = roman_min { italic_k ∈ blackboard_N : start_ARRAY start_ROW start_CELL italic_k is odd and there is ( italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ) ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT such that end_CELL end_ROW start_ROW start_CELL | italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT | + ⋯ + | italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT | = italic_k and italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT + ⋯ + italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ≡ 0 start_MODIFIER ( roman_mod start_ARG italic_q end_ARG ) end_MODIFIER end_CELL end_ROW end_ARRAY } .
Proof.
Write
L
=
L
⁢
(
q
;
s
1
,
…
,
s
n
)
=
S
2
⁢
n
−
1
/
Γ
𝐿
𝐿
𝑞
subscript
𝑠
1
…
subscript
𝑠
𝑛
superscript
𝑆
2
𝑛
1
Γ
L=L(q;s_{1},\dots,s_{n})=S^{2n-1}/\Gamma
italic_L = italic_L ( italic_q ; italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ) = italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / roman_Γ
, with
s
=
(
s
1
,
…
,
s
n
)
𝑠
subscript
𝑠
1
…
subscript
𝑠
𝑛
s=(s_{1},\dots,s_{n})
italic_s = ( italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT )
and
Γ
=
Γ
q
,
s
Γ
subscript
Γ
𝑞
𝑠
\Gamma=\Gamma_{q,s}
roman_Γ = roman_Γ start_POSTSUBSCRIPT italic_q , italic_s end_POSTSUBSCRIPT
.
Recall from (
2.9
) that its associated congruence lattice is given by
(3.4)
ℒ
:=
ℒ
⁢
(
q
;
s
)
:=
{
(
a
1
,
…
,
a
n
)
∈
ℤ
n
:
a
1
⁢
s
1
+
⋯
+
a
n
⁢
s
n
≡
0
(
mod
q
)
}
.
assign
ℒ
ℒ
𝑞
𝑠
assign
conditional-set
subscript
𝑎
1
…
subscript
𝑎
𝑛
superscript
ℤ
𝑛
subscript
𝑎
1
subscript
𝑠
1
⋯
subscript
𝑎
𝑛
subscript
𝑠
𝑛
annotated
0
pmod
𝑞
\mathcal{L}:=\mathcal{L}(q;s):=\{(a_{1},\dots,a_{n})\in\mathbb{Z}^{n}:a_{1}s_{%
1}+\dots+a_{n}s_{n}\equiv 0\pmod{q}\}.
caligraphic_L := caligraphic_L ( italic_q ; italic_s ) := { ( italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ) ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT : italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT + ⋯ + italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ≡ 0 start_MODIFIER ( roman_mod start_ARG italic_q end_ARG ) end_MODIFIER } .
Besides (
3.1
), the main tool in the proof will be the formula for
dim
ℋ
k
Γ
dimension
superscript
subscript
ℋ
𝑘
Γ
\dim\mathcal{H}_{k}^{\Gamma}
roman_dim caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT
given in (
2.11
):
(3.5)
dim
ℋ
k
Γ
=
∑
r
=
0
⌊
k
/
2
⌋
(
r
+
n
−
2
n
−
2
)
⁢
N
ℒ
⁢
(
k
−
2
⁢
r
)
,
dimension
superscript
subscript
ℋ
𝑘
Γ
superscript
subscript
𝑟
0
𝑘
2
binomial
𝑟
𝑛
2
𝑛
2
subscript
𝑁
ℒ
𝑘
2
𝑟
\dim\mathcal{H}_{k}^{\Gamma}=\sum_{r=0}^{\lfloor k/2\rfloor}\binom{r+n-2}{n-2}%
N_{\mathcal{L}}(k-2r),
roman_dim caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT = ∑ start_POSTSUBSCRIPT italic_r = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ⌊ italic_k / 2 ⌋ end_POSTSUPERSCRIPT ( FRACOP start_ARG italic_r + italic_n - 2 end_ARG start_ARG italic_n - 2 end_ARG ) italic_N start_POSTSUBSCRIPT caligraphic_L end_POSTSUBSCRIPT ( italic_k - 2 italic_r ) ,
where
N
ℒ
⁢
(
k
)
=
#
⁢
{
μ
∈
ℒ
:
‖
μ
‖
1
=
k
}
subscript
𝑁
ℒ
𝑘
#
conditional-set
𝜇
ℒ
subscript
norm
𝜇
1
𝑘
N_{\mathcal{L}}(k)=\#\{\mu\in\mathcal{L}:\|{\mu}\|_{1}=k\}
italic_N start_POSTSUBSCRIPT caligraphic_L end_POSTSUBSCRIPT ( italic_k ) = # { italic_μ ∈ caligraphic_L : ∥ italic_μ ∥ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT = italic_k }
.
Notice
dim
ℋ
k
Γ
>
0
dimension
superscript
subscript
ℋ
𝑘
Γ
0
\dim\mathcal{H}_{k}^{\Gamma}>0
roman_dim caligraphic_H start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT > 0
if and only if
N
ℒ
⁢
(
k
−
2
⁢
r
)
>
0
subscript
𝑁
ℒ
𝑘
2
𝑟
0
N_{\mathcal{L}}(k-2r)>0
italic_N start_POSTSUBSCRIPT caligraphic_L end_POSTSUBSCRIPT ( italic_k - 2 italic_r ) > 0
for some
r
∈
{
0
,
1
,
…
,
⌊
k
/
2
⌋
}
𝑟
0
1
…
𝑘
2
r\in\{0,1,\dots,\lfloor k/2\rfloor\}
italic_r ∈ { 0 , 1 , … , ⌊ italic_k / 2 ⌋ }
.
Suppose
k
∈
ℕ
0
𝑘
subscript
ℕ
0
k\in\mathbb{N}_{0}
italic_k ∈ blackboard_N start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
is even.
By setting
r
=
k
/
2
𝑟
𝑘
2
r=k/2
italic_r = italic_k / 2
, we obtain that
N
ℒ
⁢
(
k
−
2
⁢
r
)
=
N
ℒ
⁢
(
0
)
=
1
subscript
𝑁
ℒ
𝑘
2
𝑟
subscript
𝑁
ℒ
0
1
N_{\mathcal{L}}(k-2r)=N_{\mathcal{L}}(0)=1
italic_N start_POSTSUBSCRIPT caligraphic_L end_POSTSUBSCRIPT ( italic_k - 2 italic_r ) = italic_N start_POSTSUBSCRIPT caligraphic_L end_POSTSUBSCRIPT ( 0 ) = 1
since
(
0
,
…
,
0
)
0
…
0
(0,\dots,0)
( 0 , … , 0 )
is clearly the only element in
ℒ
ℒ
\mathcal{L}
caligraphic_L
with one-norm equal to
0
0
.
We conclude that
λ
k
∈
ℰ
⁢
(
L
)
subscript
𝜆
𝑘
ℰ
𝐿
\lambda_{k}\in\mathcal{E}(L)
italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ∈ caligraphic_E ( italic_L )
for all
k
𝑘
k
italic_k
even.
We now assume that
k
∈
ℕ
𝑘
ℕ
k\in\mathbb{N}
italic_k ∈ blackboard_N
is odd.
The odd positive integer
k
0
:=
k
0
⁢
(
L
)
assign
subscript
𝑘
0
subscript
𝑘
0
𝐿
k_{0}:=k_{0}(L)
italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT := italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ( italic_L )
given in (
3.3
) satisfies
N
ℒ
⁢
(
k
0
)
>
0
subscript
𝑁
ℒ
subscript
𝑘
0
0
N_{\mathcal{L}}(k_{0})>0
italic_N start_POSTSUBSCRIPT caligraphic_L end_POSTSUBSCRIPT ( italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ) > 0
.
Hence
λ
k
∈
ℰ
⁢
(
L
)
subscript
𝜆
𝑘
ℰ
𝐿
\lambda_{k}\in\mathcal{E}(L)
italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ∈ caligraphic_E ( italic_L )
for every odd integer
k
≥
k
0
𝑘
subscript
𝑘
0
k\geq k_{0}
italic_k ≥ italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
by setting
r
=
k
−
k
0
2
𝑟
𝑘
subscript
𝑘
0
2
r=\frac{k-k_{0}}{2}
italic_r = divide start_ARG italic_k - italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_ARG start_ARG 2 end_ARG
in (
3.5
).
If
λ
k
∈
ℰ
⁢
(
L
)
subscript
𝜆
𝑘
ℰ
𝐿
\lambda_{k}\in\mathcal{E}(L)
italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ∈ caligraphic_E ( italic_L )
for some odd integer
k
<
k
0
𝑘
subscript
𝑘
0
k<k_{0}
italic_k < italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
, then
N
ℒ
⁢
(
k
1
)
>
0
subscript
𝑁
ℒ
subscript
𝑘
1
0
N_{\mathcal{L}}(k_{1})>0
italic_N start_POSTSUBSCRIPT caligraphic_L end_POSTSUBSCRIPT ( italic_k start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ) > 0
for some odd integer
k
1
≤
k
subscript
𝑘
1
𝑘
k_{1}\leq k
italic_k start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ≤ italic_k
by (
3.5
), which implies the contradiction
k
1
≥
k
0
subscript
𝑘
1
subscript
𝑘
0
k_{1}\geq k_{0}
italic_k start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ≥ italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
.
This concludes the proof.
∎
Theorem
3.4
ensures that the eigenvalue spectrum of a lens space
L
𝐿
L
italic_L
depends only on
k
0
⁢
(
L
)
subscript
𝑘
0
𝐿
k_{0}(L)
italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ( italic_L )
.
This allows us to give curious examples of eigenvalue equivalent lens spaces.
Proof of Theorem
1.3
.
Write
d
=
2
⁢
n
−
1
𝑑
2
𝑛
1
d=2n-1
italic_d = 2 italic_n - 1
for some
n
∈
ℕ
𝑛
ℕ
n\in\mathbb{N}
italic_n ∈ blackboard_N
with
n
≥
2
𝑛
2
n\geq 2
italic_n ≥ 2
.
Let
𝔏
⁢
(
n
,
q
)
𝔏
𝑛
𝑞
\mathfrak{L}(n,q)
fraktur_L ( italic_n , italic_q )
denote the isometry classes of
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional lens spaces with fundamental group of order
q
𝑞
q
italic_q
.
For a positive odd integer
k
𝑘
k
italic_k
, we set
(3.6)
𝔏
⁢
(
n
,
q
)
k
=
{
L
∈
𝔏
⁢
(
n
,
q
)
:
k
0
⁢
(
L
)
=
k
}
.
𝔏
subscript
𝑛
𝑞
𝑘
conditional-set
𝐿
𝔏
𝑛
𝑞
subscript
𝑘
0
𝐿
𝑘
\mathfrak{L}(n,q)_{k}=\{L\in\mathfrak{L}(n,q):k_{0}(L)=k\}.
fraktur_L ( italic_n , italic_q ) start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT = { italic_L ∈ fraktur_L ( italic_n , italic_q ) : italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ( italic_L ) = italic_k } .
It follows immediately from Theorem
3.4
that the elements in
𝔏
∗
⁢
(
n
)
k
:=
⋃
q
≥
3
𝔏
⁢
(
n
,
q
)
k
assign
superscript
𝔏
subscript
𝑛
𝑘
subscript
𝑞
3
𝔏
subscript
𝑛
𝑞
𝑘
\mathfrak{L}^{*}(n)_{k}:=\bigcup_{q\geq 3}\mathfrak{L}(n,q)_{k}
fraktur_L start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT ( italic_n ) start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT := ⋃ start_POSTSUBSCRIPT italic_q ≥ 3 end_POSTSUBSCRIPT fraktur_L ( italic_n , italic_q ) start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
are pairwise non-isometric and mutually eigenvalue equivalent.
It remains to show that
𝔏
∗
⁢
(
n
)
k
superscript
𝔏
subscript
𝑛
𝑘
\mathfrak{L}^{*}(n)_{k}
fraktur_L start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT ( italic_n ) start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
is infinite for some
k
𝑘
k
italic_k
.
We pick
k
=
3
𝑘
3
k=3
italic_k = 3
.
One has that
L
q
:=
L
⁢
(
q
;
1
,
…
,
1
,
2
)
∈
𝔏
⁢
(
n
,
q
)
3
assign
subscript
𝐿
𝑞
𝐿
𝑞
1
…
1
2
𝔏
subscript
𝑛
𝑞
3
L_{q}:=L(q;1,\dots,1,2)\in\mathfrak{L}(n,q)_{3}
italic_L start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT := italic_L ( italic_q ; 1 , … , 1 , 2 ) ∈ fraktur_L ( italic_n , italic_q ) start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT
for any positive integer
q
≥
3
𝑞
3
q\geq 3
italic_q ≥ 3
.
In fact,
μ
:=
(
2
,
0
,
…
,
0
,
−
1
)
∈
ℒ
⁢
(
q
;
1
,
…
,
1
,
2
)
assign
𝜇
2
0
…
0
1
ℒ
𝑞
1
…
1
2
\mu:=(2,0,\dots,0,-1)\in\mathcal{L}(q;1,\dots,1,2)
italic_μ := ( 2 , 0 , … , 0 , - 1 ) ∈ caligraphic_L ( italic_q ; 1 , … , 1 , 2 )
satisfies
‖
μ
‖
1
=
3
subscript
norm
𝜇
1
3
\|{\mu}\|_{1}=3
∥ italic_μ ∥ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT = 3
, and it is evident that no element of one-norm
1
1
1
1
is contained in
ℒ
⁢
(
q
;
1
,
…
,
1
,
2
)
ℒ
𝑞
1
…
1
2
\mathcal{L}(q;1,\dots,1,2)
caligraphic_L ( italic_q ; 1 , … , 1 , 2 )
.
The assertion about the volume follows immediately from
(3.7)
vol
⁡
(
L
q
′
)
vol
⁡
(
L
q
)
=
vol
⁡
(
S
2
⁢
n
−
1
)
q
⁢
q
′
vol
⁡
(
S
2
⁢
n
−
1
)
=
q
′
q
vol
subscript
𝐿
superscript
𝑞
′
vol
subscript
𝐿
𝑞
vol
superscript
𝑆
2
𝑛
1
𝑞
superscript
𝑞
′
vol
superscript
𝑆
2
𝑛
1
superscript
𝑞
′
𝑞
\frac{\operatorname{vol}(L_{q^{\prime}})}{\operatorname{vol}(L_{q})}=\frac{%
\operatorname{vol}(S^{2n-1})}{q}\frac{q^{\prime}}{\operatorname{vol}(S^{2n-1})%
}=\frac{q^{\prime}}{q}
divide start_ARG roman_vol ( italic_L start_POSTSUBSCRIPT italic_q start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_POSTSUBSCRIPT ) end_ARG start_ARG roman_vol ( italic_L start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT ) end_ARG = divide start_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT ) end_ARG start_ARG italic_q end_ARG divide start_ARG italic_q start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_ARG start_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT ) end_ARG = divide start_ARG italic_q start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_ARG start_ARG italic_q end_ARG
by taking
q
=
3
𝑞
3
q=3
italic_q = 3
and
q
′
superscript
𝑞
′
q^{\prime}
italic_q start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
arbitrarily large.
∎
Theorem
3.4
also allows us to show that the eigenvalue spectrum does not detect singularities.
Example 3.5
.
For positive integers
q
,
q
′
≥
3
𝑞
superscript
𝑞
′
3
q,q^{\prime}\geq 3
italic_q , italic_q start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ≥ 3
, the lens orbifold
L
⁢
(
2
⁢
q
;
1
,
2
,
q
)
𝐿
2
𝑞
1
2
𝑞
L(2q;1,2,q)
italic_L ( 2 italic_q ; 1 , 2 , italic_q )
, which has non-trivial singularities, is eigenvalue equivalent to the lens space
L
⁢
(
q
′
;
1
,
1
,
2
)
𝐿
superscript
𝑞
′
1
1
2
L(q^{\prime};1,1,2)
italic_L ( italic_q start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ; 1 , 1 , 2 )
since
k
0
⁢
(
L
⁢
(
2
⁢
q
;
1
,
2
,
q
)
)
=
k
0
⁢
(
L
⁢
(
q
′
;
1
,
1
,
2
)
)
=
3
.
subscript
𝑘
0
𝐿
2
𝑞
1
2
𝑞
subscript
𝑘
0
𝐿
superscript
𝑞
′
1
1
2
3
k_{0}\big{(}L(2q;1,2,q)\big{)}=k_{0}\big{(}L(q^{\prime};1,1,2)\big{)}=3.
italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ( italic_L ( 2 italic_q ; 1 , 2 , italic_q ) ) = italic_k start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ( italic_L ( italic_q start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ; 1 , 1 , 2 ) ) = 3 .
3.3.
Eigenvalue equivalent manifolds with different dimensions
It is known that in general, dimension is not determined by the eigenvalue spectrum.
For instance, Miatello and Rossetti
[
MR03
, Ex. 3.8]
have observed that the eigenvalue spectrum of the square torus
ℝ
n
/
ℤ
n
superscript
ℝ
𝑛
superscript
ℤ
𝑛
\mathbb{R}^{n}/\mathbb{Z}^{n}
blackboard_R start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT / blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
is
ℤ
≥
0
subscript
ℤ
absent
0
\mathbb{Z}_{\geq 0}
blackboard_Z start_POSTSUBSCRIPT ≥ 0 end_POSTSUBSCRIPT
for all
n
≥
4
𝑛
4
n\geq 4
italic_n ≥ 4
.
We now give examples of normal homogeneous Riemannian manifolds having the same eigenvalue spectrum but distinct dimensions.
A particularly simple example is
(
S
2
,
1
4
⁢
g
round
)
superscript
𝑆
2
1
4
subscript
𝑔
round
\big{(}S^{2},\tfrac{1}{4}\,g_{\text{round}}\big{)}
( italic_S start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT , divide start_ARG 1 end_ARG start_ARG 4 end_ARG italic_g start_POSTSUBSCRIPT round end_POSTSUBSCRIPT )
and
(
P
3
⁢
(
ℝ
)
,
g
round
)
superscript
𝑃
3
ℝ
subscript
𝑔
round
\big{(}P^{3}(\mathbb{R}),g_{\text{round}}\big{)}
( italic_P start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT ( blackboard_R ) , italic_g start_POSTSUBSCRIPT round end_POSTSUBSCRIPT )
, where
g
round
subscript
𝑔
round
g_{\text{round}}
italic_g start_POSTSUBSCRIPT round end_POSTSUBSCRIPT
denotes in both cases the round metric with constant sectional curvature one.
Indeed, on the one hand, the eigenvalues of
(
S
2
,
1
4
⁢
g
round
)
superscript
𝑆
2
1
4
subscript
𝑔
round
\big{(}S^{2},\tfrac{1}{4}\,g_{\text{round}}\big{)}
( italic_S start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT , divide start_ARG 1 end_ARG start_ARG 4 end_ARG italic_g start_POSTSUBSCRIPT round end_POSTSUBSCRIPT )
, which is isometric to the sphere in
ℝ
3
superscript
ℝ
3
\mathbb{R}^{3}
blackboard_R start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT
of radius
1
2
1
2
\frac{1}{2}
divide start_ARG 1 end_ARG start_ARG 2 end_ARG
endowed with the Riemannian metric induced by the canonical Euclidean metric in
ℝ
3
superscript
ℝ
3
\mathbb{R}^{3}
blackboard_R start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT
, are given by
4
4
4
4
-times the eigenvalues of
(
S
2
,
g
round
)
superscript
𝑆
2
subscript
𝑔
round
\big{(}S^{2},g_{\text{round}}\big{)}
( italic_S start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT , italic_g start_POSTSUBSCRIPT round end_POSTSUBSCRIPT )
, that is,
(3.8)
{
4
⁢
k
⁢
(
k
+
1
)
:
k
∈
ℕ
0
}
.
conditional-set
4
𝑘
𝑘
1
𝑘
subscript
ℕ
0
\left\{4k(k+1):k\in\mathbb{N}_{0}\right\}.
{ 4 italic_k ( italic_k + 1 ) : italic_k ∈ blackboard_N start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT } .
On the other hand, the eigenvalues of the
3
3
3
3
-dimensional real projective space
(
P
3
⁢
(
ℝ
)
,
g
round
)
superscript
𝑃
3
ℝ
subscript
𝑔
round
\big{(}P^{3}(\mathbb{R}),g_{\text{round}}\big{)}
( italic_P start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT ( blackboard_R ) , italic_g start_POSTSUBSCRIPT round end_POSTSUBSCRIPT )
with constant sectional curvature one are the same as those of its
2
2
2
2
-cover
(
S
3
,
g
round
)
superscript
𝑆
3
subscript
𝑔
round
\big{(}S^{3},g_{\text{round}}\big{)}
( italic_S start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT , italic_g start_POSTSUBSCRIPT round end_POSTSUBSCRIPT )
associated to odd-dimensional representations, that is,
(3.9)
{
k
⁢
(
k
+
2
)
:
k
∈
2
⁢
ℕ
0
}
.
conditional-set
𝑘
𝑘
2
𝑘
2
subscript
ℕ
0
\left\{k(k+2):k\in 2\mathbb{N}_{0}\right\}.
{ italic_k ( italic_k + 2 ) : italic_k ∈ 2 blackboard_N start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT } .
Of course, the multiplicities do not match since
4
⁢
k
⁢
(
k
+
1
)
4
𝑘
𝑘
1
4k(k+1)
4 italic_k ( italic_k + 1 )
has multiplicity
k
+
1
𝑘
1
k+1
italic_k + 1
in
(
S
2
,
g
round
)
superscript
𝑆
2
subscript
𝑔
round
\big{(}S^{2},g_{\text{round}}\big{)}
( italic_S start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT , italic_g start_POSTSUBSCRIPT round end_POSTSUBSCRIPT )
for any
k
∈
ℕ
𝑘
ℕ
k\in\mathbb{N}
italic_k ∈ blackboard_N
,
while
k
⁢
(
k
+
2
)
𝑘
𝑘
2
k(k+2)
italic_k ( italic_k + 2 )
has multiplicity
k
2
superscript
𝑘
2
k^{2}
italic_k start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT
for any
k
∈
2
⁢
ℕ
0
𝑘
2
subscript
ℕ
0
k\in 2\mathbb{N}_{0}
italic_k ∈ 2 blackboard_N start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
.
Both of the above manifolds are symmetric spaces.
Our next result generalizes them and provides infinitely many examples of eigenvalue equivalent normal homogeneous Riemannian manifolds with different dimensions.
Theorem 3.6
.
Let
G
𝐺
G
italic_G
be a compact, connected, simply connected, and semisimple Lie group.
The centerless Lie group
G
/
Z
⁢
(
G
)
𝐺
𝑍
𝐺
G/Z(G)
italic_G / italic_Z ( italic_G )
endowed with the standard bi-invariant metric (
Z
⁢
(
G
)
𝑍
𝐺
Z(G)
italic_Z ( italic_G )
is the center of
G
𝐺
G
italic_G
and the metric is induced by the Killing form of
𝔤
𝔤
\mathfrak{g}
fraktur_g
)
has the same eigenvalue spectrum as
the standard metric on the full flag manifold
G
/
T
𝐺
𝑇
G/T
italic_G / italic_T
(
T
𝑇
T
italic_T
is a maximal torus in
G
𝐺
G
italic_G
and the metric is induced by the Killing form of the Lie algebra
𝔤
𝔤
\mathfrak{g}
fraktur_g
of
G
𝐺
G
italic_G
).
Moreover,
dim
G
/
Z
⁢
(
G
)
>
dim
G
/
T
dimension
𝐺
𝑍
𝐺
dimension
𝐺
𝑇
\dim G/Z(G)>\dim G/T
roman_dim italic_G / italic_Z ( italic_G ) > roman_dim italic_G / italic_T
.
Proof.
The proof of this result makes use of objects from representation theory of compact Lie groups that have not appeared in the rest of the article.
For conciseness, we will give the arguments without introducing several objects (e.g. weight lattice) and will instead refer the interested reader to other references.
For an arbitrary compact connected Lie group
K
𝐾
K
italic_K
, the spectrum of the standard bi-invariant metric is given by
(3.10)
{
{
Cas
⁡
(
π
)
,
…
,
Cas
⁡
(
π
)
⏟
(
dim
V
π
)
2
:
π
∈
K
^
}
}
.
conditional-set
subscript
⏟
Cas
𝜋
…
Cas
𝜋
superscript
dimension
subscript
𝑉
𝜋
2
𝜋
^
𝐾
\Big{\{}\!\!\Big{\{}\underbrace{\operatorname{Cas}(\pi),\dots,\operatorname{%
Cas}(\pi)}_{(\dim V_{\pi})^{2}}:\pi\in\widehat{K}\Big{\}}\!\!\Big{\}}.
{ { under⏟ start_ARG roman_Cas ( italic_π ) , … , roman_Cas ( italic_π ) end_ARG start_POSTSUBSCRIPT ( roman_dim italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT ) start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_POSTSUBSCRIPT : italic_π ∈ over^ start_ARG italic_K end_ARG } } .
Here,
K
^
^
𝐾
\widehat{K}
over^ start_ARG italic_K end_ARG
stands for the unitary dual of
K
𝐾
K
italic_K
(the equivalent classes of irreducible representations of
K
𝐾
K
italic_K
), and
Cas
⁡
(
π
)
Cas
𝜋
\operatorname{Cas}(\pi)
roman_Cas ( italic_π )
denotes the scalar for which the Casimir element of
𝔤
ℂ
subscript
𝔤
ℂ
\mathfrak{g}_{\mathbb{C}}
fraktur_g start_POSTSUBSCRIPT blackboard_C end_POSTSUBSCRIPT
acts on
V
π
subscript
𝑉
𝜋
V_{\pi}
italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT
.
By the Highest Weight Theorem (see e.g.
[
Se
, Thm. 7.34]
),
K
^
^
𝐾
\widehat{K}
over^ start_ARG italic_K end_ARG
is in correspondence with dominant analytically integral weights.
In our case
K
=
G
/
Z
⁢
(
G
)
𝐾
𝐺
𝑍
𝐺
K=G/Z(G)
italic_K = italic_G / italic_Z ( italic_G )
, and since
K
𝐾
K
italic_K
is centerless,
[
Se
, Thm. 6.30(a)]
tells us that the lattice of analytically integral weights coincides with the root lattice
ℛ
:=
⨁
α
∈
Φ
⁢
(
𝔤
ℂ
,
𝔱
ℂ
)
ℤ
⁢
α
assign
ℛ
subscript
direct-sum
𝛼
Φ
subscript
𝔤
ℂ
subscript
𝔱
ℂ
ℤ
𝛼
\mathcal{R}:=\bigoplus_{\alpha\in\Phi(\mathfrak{g}_{\mathbb{C}},\mathfrak{t}_{%
\mathbb{C}})}\mathbb{Z}\alpha
caligraphic_R := ⨁ start_POSTSUBSCRIPT italic_α ∈ roman_Φ ( fraktur_g start_POSTSUBSCRIPT blackboard_C end_POSTSUBSCRIPT , fraktur_t start_POSTSUBSCRIPT blackboard_C end_POSTSUBSCRIPT ) end_POSTSUBSCRIPT blackboard_Z italic_α
, where
Φ
⁢
(
𝔤
ℂ
,
𝔱
ℂ
)
Φ
subscript
𝔤
ℂ
subscript
𝔱
ℂ
\Phi(\mathfrak{g}_{\mathbb{C}},\mathfrak{t}_{\mathbb{C}})
roman_Φ ( fraktur_g start_POSTSUBSCRIPT blackboard_C end_POSTSUBSCRIPT , fraktur_t start_POSTSUBSCRIPT blackboard_C end_POSTSUBSCRIPT )
denotes the root system associated to the Cartan subalgebra
𝔱
ℂ
subscript
𝔱
ℂ
\mathfrak{t}_{\mathbb{C}}
fraktur_t start_POSTSUBSCRIPT blackboard_C end_POSTSUBSCRIPT
of
𝔤
ℂ
subscript
𝔤
ℂ
\mathfrak{g}_{\mathbb{C}}
fraktur_g start_POSTSUBSCRIPT blackboard_C end_POSTSUBSCRIPT
.
Therefore, the eigenvalue spectrum of the standard bi-invariant metric on
G
/
Z
⁢
(
G
)
𝐺
𝑍
𝐺
G/Z(G)
italic_G / italic_Z ( italic_G )
is given by
(3.11)
{
Cas
⁡
(
π
Λ
)
:
Λ
∈
ℛ
⁢
is dominant
}
,
conditional-set
Cas
subscript
𝜋
Λ
Λ
ℛ
is dominant
\big{\{}\operatorname{Cas}(\pi_{\Lambda}):\Lambda\in\mathcal{R}\text{ is %
dominant}\big{\}},
{ roman_Cas ( italic_π start_POSTSUBSCRIPT roman_Λ end_POSTSUBSCRIPT ) : roman_Λ ∈ caligraphic_R is dominant } ,
where
π
Λ
subscript
𝜋
Λ
\pi_{\Lambda}
italic_π start_POSTSUBSCRIPT roman_Λ end_POSTSUBSCRIPT
denotes the corresponding irreducible representation with highest weight
Λ
Λ
\Lambda
roman_Λ
.
Yamaguchi
[
Ya79
, Thm. 6]
proved that the spectrum of the full flag manifold
G
/
T
𝐺
𝑇
G/T
italic_G / italic_T
endowed with standard (or Killing metric) is given by
(3.12)
{
{
Cas
⁡
(
π
)
,
…
,
Cas
⁡
(
π
)
⏟
dim
V
π
⁢
dim
V
π
⁢
(
0
)
:
π
∈
G
^
}
}
,
conditional-set
subscript
⏟
Cas
𝜋
…
Cas
𝜋
dimension
subscript
𝑉
𝜋
dimension
subscript
𝑉
𝜋
0
𝜋
^
𝐺
\Big{\{}\!\!\Big{\{}\underbrace{\operatorname{Cas}(\pi),\dots,\operatorname{%
Cas}(\pi)}_{\dim V_{\pi}\dim V_{\pi}(0)}:\pi\in\widehat{G}\Big{\}}\!\!\Big{\}},
{ { under⏟ start_ARG roman_Cas ( italic_π ) , … , roman_Cas ( italic_π ) end_ARG start_POSTSUBSCRIPT roman_dim italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT roman_dim italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT ( 0 ) end_POSTSUBSCRIPT : italic_π ∈ over^ start_ARG italic_G end_ARG } } ,
where
V
π
⁢
(
0
)
subscript
𝑉
𝜋
0
V_{\pi}(0)
italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT ( 0 )
is the weight space associated to the weight zero.
It is important to note that
π
∈
G
^
𝜋
^
𝐺
\pi\in\widehat{G}
italic_π ∈ over^ start_ARG italic_G end_ARG
contributes
Cas
⁡
(
π
)
Cas
𝜋
\operatorname{Cas}(\pi)
roman_Cas ( italic_π )
as an eigenvalue of the Laplacian if and only if
dim
V
π
⁢
(
0
)
>
0
dimension
subscript
𝑉
𝜋
0
0
\dim V_{\pi}(0)>0
roman_dim italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT ( 0 ) > 0
.
By a result of Freudenthal (see
[
Ya79
, Thm. 4]
),
dim
V
π
⁢
(
0
)
>
0
dimension
subscript
𝑉
𝜋
0
0
\dim V_{\pi}(0)>0
roman_dim italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT ( 0 ) > 0
if and only if the highest weight of
π
𝜋
\pi
italic_π
lives in the root lattice
ℛ
ℛ
\mathcal{R}
caligraphic_R
.
Therefore, the eigenvalue spectrum of
G
/
T
𝐺
𝑇
G/T
italic_G / italic_T
is precisely (
3.11
).
The last assertion follows easily from
dim
G
/
Z
⁢
(
G
)
=
dim
G
dimension
𝐺
𝑍
𝐺
dimension
𝐺
\dim G/Z(G)=\dim G
roman_dim italic_G / italic_Z ( italic_G ) = roman_dim italic_G
since
Z
⁢
(
G
)
𝑍
𝐺
Z(G)
italic_Z ( italic_G )
is discrete in
G
𝐺
G
italic_G
and
dim
G
/
T
=
dim
G
−
dim
T
dimension
𝐺
𝑇
dimension
𝐺
dimension
𝑇
\dim G/T=\dim G-\dim T
roman_dim italic_G / italic_T = roman_dim italic_G - roman_dim italic_T
with
dim
T
=
rank
⁡
G
>
0
dimension
𝑇
rank
𝐺
0
\dim T=\operatorname{rank}G>0
roman_dim italic_T = roman_rank italic_G > 0
.
∎
Remark 3.7
.
The choice
G
=
SU
⁡
(
2
)
𝐺
SU
2
G=\operatorname{SU}(2)
italic_G = roman_SU ( 2 )
in Theorem
3.6
provides the eigenvalue equivalent pair
(
P
3
⁢
(
ℝ
)
,
g
round
)
superscript
𝑃
3
ℝ
subscript
𝑔
round
(P^{3}(\mathbb{R}),g_{\text{round}})
( italic_P start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT ( blackboard_R ) , italic_g start_POSTSUBSCRIPT round end_POSTSUBSCRIPT )
and
(
S
2
,
1
4
⁢
g
round
)
superscript
𝑆
2
1
4
subscript
𝑔
round
(S^{2},\tfrac{1}{4}g_{\text{round}})
( italic_S start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT , divide start_ARG 1 end_ARG start_ARG 4 end_ARG italic_g start_POSTSUBSCRIPT round end_POSTSUBSCRIPT )
shown at the beginning of this subsection.
Remark 3.8
.
For any finite subgroup
Γ
Γ
\Gamma
roman_Γ
of the group
G
𝐺
G
italic_G
as in Theorem
3.6
, one can see that
(3.13)
Spec
⁡
(
Γ
\
G
/
Z
⁢
(
G
)
)
Spec
\
Γ
𝐺
𝑍
𝐺
\displaystyle\operatorname{Spec}(\Gamma\backslash G/Z(G))
roman_Spec ( roman_Γ \ italic_G / italic_Z ( italic_G ) )
=
{
{
Cas
⁡
(
π
)
,
…
,
Cas
⁡
(
π
)
⏟
dim
V
π
Γ
⁢
dim
V
π
:
π
∈
K
^
}
}
,
absent
conditional-set
subscript
⏟
Cas
𝜋
…
Cas
𝜋
dimension
superscript
subscript
𝑉
𝜋
Γ
dimension
subscript
𝑉
𝜋
𝜋
^
𝐾
\displaystyle=\Big{\{}\!\!\Big{\{}\underbrace{\operatorname{Cas}(\pi),\dots,%
\operatorname{Cas}(\pi)}_{\dim V_{\pi}^{\Gamma}\dim V_{\pi}}:\pi\in\widehat{K}%
\Big{\}}\!\!\Big{\}},
= { { under⏟ start_ARG roman_Cas ( italic_π ) , … , roman_Cas ( italic_π ) end_ARG start_POSTSUBSCRIPT roman_dim italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT roman_dim italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT end_POSTSUBSCRIPT : italic_π ∈ over^ start_ARG italic_K end_ARG } } ,
Spec
⁡
(
Γ
\
G
/
T
)
Spec
\
Γ
𝐺
𝑇
\displaystyle\operatorname{Spec}(\Gamma\backslash G/T)
roman_Spec ( roman_Γ \ italic_G / italic_T )
=
{
{
Cas
⁡
(
π
)
,
…
,
Cas
⁡
(
π
)
⏟
dim
V
π
Γ
⁢
dim
V
π
⁢
(
0
)
:
π
∈
G
^
}
}
,
absent
conditional-set
subscript
⏟
Cas
𝜋
…
Cas
𝜋
dimension
superscript
subscript
𝑉
𝜋
Γ
dimension
subscript
𝑉
𝜋
0
𝜋
^
𝐺
\displaystyle=\Big{\{}\!\!\Big{\{}\underbrace{\operatorname{Cas}(\pi),\dots,%
\operatorname{Cas}(\pi)}_{\dim V_{\pi}^{\Gamma}\dim V_{\pi}(0)}:\pi\in\widehat%
{G}\Big{\}}\!\!\Big{\}},
= { { under⏟ start_ARG roman_Cas ( italic_π ) , … , roman_Cas ( italic_π ) end_ARG start_POSTSUBSCRIPT roman_dim italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT roman_dim italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT ( 0 ) end_POSTSUBSCRIPT : italic_π ∈ over^ start_ARG italic_G end_ARG } } ,
so that in particular, they are eigenvalue equivalent.
For
G
𝐺
G
italic_G
simple of type
E
8
subscript
E
8
\textup{E}_{8}
E start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT
,
F
4
subscript
F
4
\textup{F}_{4}
F start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT
and
G
2
subscript
G
2
\textup{G}_{2}
G start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
, one has that
Z
⁢
(
G
)
𝑍
𝐺
Z(G)
italic_Z ( italic_G )
is trivial, thus any finite subgroup
Γ
Γ
\Gamma
roman_Γ
whose action on
G
/
T
𝐺
𝑇
G/T
italic_G / italic_T
is not free provides new examples of a manifold
Γ
\
G
\
Γ
𝐺
\Gamma\backslash G
roman_Γ \ italic_G
eigenvalue equivalent to an orbifold
Γ
\
G
/
T
\
Γ
𝐺
𝑇
\Gamma\backslash G/T
roman_Γ \ italic_G / italic_T
with non-trivial singularities.
4.
Isospectral pairs of largest volume
In this section we discuss the problem introduced in Subsection
1.2
: determining the isospectral pair of spherical orbifolds/space forms of largest volume.
Recall our assumption that every spherical orbifold is endowed with the Riemannian metric with constant sectional curvature one, and that there is an equality
(4.1)
vol
⁡
(
S
d
/
Γ
)
=
vol
⁡
(
S
d
)
|
Γ
|
vol
superscript
𝑆
𝑑
Γ
vol
superscript
𝑆
𝑑
Γ
\operatorname{vol}(S^{d}/\Gamma)=\frac{\operatorname{vol}(S^{d})}{|\Gamma|}
roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ ) = divide start_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ) end_ARG start_ARG | roman_Γ | end_ARG
for any finite subgroup
Γ
Γ
\Gamma
roman_Γ
of
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
.
4.1.
Isospectral spherical orbifold of largest volume
The orbifold setting is simpler than that of spherical space forms.
Proof of Theorem
1.5
.
Let
Γ
1
subscript
Γ
1
\Gamma_{1}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
Γ
2
subscript
Γ
2
\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
be the finite subgroups of
SO
⁡
(
6
)
SO
6
\operatorname{SO}(6)
roman_SO ( 6 )
with diagonal matrices whose entries are
(4.2)
Γ
1
:
{
(
1
,
1
,
1
,
1
,
1
,
1
)
,
(
−
1
,
−
1
,
−
1
,
−
1
,
−
1
,
−
1
)
,
(
−
1
,
−
1
,
1
,
1
,
1
,
1
)
,
(
−
1
,
1
,
−
1
,
1
,
1
,
1
)
,
(
1
,
−
1
,
−
1
,
1
,
1
,
1
)
,
(
−
1
,
1
,
1
,
−
1
,
−
1
,
−
1
)
,
(
1
,
−
1
,
1
,
−
1
,
−
1
,
−
1
)
,
(
1
,
1
,
−
1
,
−
1
,
−
1
,
−
1
)
,
Γ
2
:
{
(
1
,
1
,
1
,
1
,
1
,
1
)
,
(
−
1
,
−
1
,
−
1
,
−
1
,
−
1
,
−
1
)
,
(
−
1
,
−
1
,
1
,
1
,
1
,
1
)
,
(
1
,
1
,
−
1
,
−
1
,
1
,
1
)
,
(
1
,
1
,
1
,
1
,
−
1
,
−
1
)
,
(
−
1
,
−
1
,
−
1
,
−
1
,
1
,
1
)
,
(
−
1
,
−
1
,
1
,
1
,
−
1
,
−
1
)
,
(
1
,
1
,
−
1
,
−
1
,
−
1
,
−
1
)
.
:
subscript
Γ
1
cases
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
subscript
Γ
2
:
cases
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
1
1
1
1
1
1
otherwise
\Gamma_{1}:\begin{cases}(1,1,1,1,1,1),\\
(-1,-1,-1,-1,-1,-1),\\
(-1,-1,1,1,1,1),\\
(-1,1,-1,1,1,1),\\
(1,-1,-1,1,1,1),\\
(-1,1,1,-1,-1,-1),\\
(1,-1,1,-1,-1,-1),\\
(1,1,-1,-1,-1,-1),\end{cases}\qquad\Gamma_{2}:\begin{cases}(1,1,1,1,1,1),\\
(-1,-1,-1,-1,-1,-1),\\
(-1,-1,1,1,1,1),\\
(1,1,-1,-1,1,1),\\
(1,1,1,1,-1,-1),\\
(-1,-1,-1,-1,1,1),\\
(-1,-1,1,1,-1,-1),\\
(1,1,-1,-1,-1,-1).\end{cases}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT : { start_ROW start_CELL ( 1 , 1 , 1 , 1 , 1 , 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( - 1 , - 1 , - 1 , - 1 , - 1 , - 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( - 1 , - 1 , 1 , 1 , 1 , 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( - 1 , 1 , - 1 , 1 , 1 , 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( 1 , - 1 , - 1 , 1 , 1 , 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( - 1 , 1 , 1 , - 1 , - 1 , - 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( 1 , - 1 , 1 , - 1 , - 1 , - 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( 1 , 1 , - 1 , - 1 , - 1 , - 1 ) , end_CELL start_CELL end_CELL end_ROW roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT : { start_ROW start_CELL ( 1 , 1 , 1 , 1 , 1 , 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( - 1 , - 1 , - 1 , - 1 , - 1 , - 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( - 1 , - 1 , 1 , 1 , 1 , 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( 1 , 1 , - 1 , - 1 , 1 , 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( 1 , 1 , 1 , 1 , - 1 , - 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( - 1 , - 1 , - 1 , - 1 , 1 , 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( - 1 , - 1 , 1 , 1 , - 1 , - 1 ) , end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL ( 1 , 1 , - 1 , - 1 , - 1 , - 1 ) . end_CELL start_CELL end_CELL end_ROW
[
RSW08
, Ex. 2.4]
shows that
Γ
1
subscript
Γ
1
\Gamma_{1}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
Γ
2
subscript
Γ
2
\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are almost conjugate (but not conjugate) in
SO
⁡
(
6
)
SO
6
\operatorname{SO}(6)
roman_SO ( 6 )
.
Consequently,
S
5
/
Γ
1
superscript
𝑆
5
subscript
Γ
1
S^{5}/\Gamma_{1}
italic_S start_POSTSUPERSCRIPT 5 end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
S
5
/
Γ
2
superscript
𝑆
5
subscript
Γ
2
S^{5}/\Gamma_{2}
italic_S start_POSTSUPERSCRIPT 5 end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are (strongly) isospectral by Theorem
2.2
.
That
S
5
/
Γ
1
superscript
𝑆
5
subscript
Γ
1
S^{5}/\Gamma_{1}
italic_S start_POSTSUPERSCRIPT 5 end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
S
5
/
Γ
2
superscript
𝑆
5
subscript
Γ
2
S^{5}/\Gamma_{2}
italic_S start_POSTSUPERSCRIPT 5 end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are not isometric is proven in
[
RSW08
, Ex. 2.9]
.
For any
d
≥
5
𝑑
5
d\geq 5
italic_d ≥ 5
, let us denote by
Γ
~
i
subscript
~
Γ
𝑖
\widetilde{\Gamma}_{i}
over~ start_ARG roman_Γ end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
the subgroup of
SO
⁡
(
d
+
1
)
SO
𝑑
1
\operatorname{SO}(d+1)
roman_SO ( italic_d + 1 )
given by adding
d
−
5
𝑑
5
d-5
italic_d - 5
entries equal to
1
1
1
1
to each element in
Γ
i
subscript
Γ
𝑖
\Gamma_{i}
roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
.
It is not difficult to see that
S
d
/
Γ
~
1
superscript
𝑆
𝑑
subscript
~
Γ
1
S^{d}/\widetilde{\Gamma}_{1}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / over~ start_ARG roman_Γ end_ARG start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
S
d
/
Γ
~
2
superscript
𝑆
𝑑
subscript
~
Γ
2
S^{d}/\widetilde{\Gamma}_{2}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / over~ start_ARG roman_Γ end_ARG start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are again isospectral and non-isometric because
Γ
~
1
subscript
~
Γ
1
\widetilde{\Gamma}_{1}
over~ start_ARG roman_Γ end_ARG start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
Γ
~
2
subscript
~
Γ
2
\widetilde{\Gamma}_{2}
over~ start_ARG roman_Γ end_ARG start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are almost conjugate in
SO
⁡
(
d
+
1
)
SO
𝑑
1
\operatorname{SO}(d+1)
roman_SO ( italic_d + 1 )
.
Since
Γ
~
1
subscript
~
Γ
1
\widetilde{\Gamma}_{1}
over~ start_ARG roman_Γ end_ARG start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
Γ
~
2
subscript
~
Γ
2
\widetilde{\Gamma}_{2}
over~ start_ARG roman_Γ end_ARG start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
each have
8
8
8
8
elements, we have that
vol
⁡
(
S
d
+
1
/
Γ
~
i
)
=
vol
⁡
(
S
d
+
1
)
8
vol
superscript
𝑆
𝑑
1
subscript
~
Γ
𝑖
vol
superscript
𝑆
𝑑
1
8
\operatorname{vol}(S^{d+1}/\widetilde{\Gamma}_{i})=\frac{\operatorname{vol}(S^%
{d+1})}{8}
roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d + 1 end_POSTSUPERSCRIPT / over~ start_ARG roman_Γ end_ARG start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) = divide start_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d + 1 end_POSTSUPERSCRIPT ) end_ARG start_ARG 8 end_ARG
for
i
=
1
,
2
𝑖
1
2
i=1,2
italic_i = 1 , 2
, and the assertion follows.
∎
It is not known whether the above example attains the largest volume asked in Question
1.4
.
The following result provides a lower bound for the mentioned highest volume.
Proposition 4.1
.
There are no pairs of
d
𝑑
d
italic_d
-dimensional isospectral and non-isometric spherical orbifolds with volume greater than or equal to
vol
⁡
(
S
d
)
3
vol
superscript
𝑆
𝑑
3
\frac{\operatorname{vol}(S^{d})}{3}
divide start_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ) end_ARG start_ARG 3 end_ARG
.
Proof.
We have to prove that two isospectral spherical orbifolds of volume
1
q
⁢
vol
⁡
(
S
d
)
1
𝑞
vol
superscript
𝑆
𝑑
\frac{1}{q}\operatorname{vol}(S^{d})
divide start_ARG 1 end_ARG start_ARG italic_q end_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT )
are isometric for
q
=
1
,
2
,
3
𝑞
1
2
3
q=1,2,3
italic_q = 1 , 2 , 3
.
The case
q
=
1
𝑞
1
q=1
italic_q = 1
is trivial.
Let
Γ
Γ
\Gamma
roman_Γ
be a subgroup of
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
of order
2
2
2
2
and let
γ
𝛾
\gamma
italic_γ
denote the non-trivial element in
Γ
Γ
\Gamma
roman_Γ
.
Since
γ
2
=
I
d
+
1
superscript
𝛾
2
subscript
I
𝑑
1
\gamma^{2}=\operatorname{I}_{d+1}
italic_γ start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT = roman_I start_POSTSUBSCRIPT italic_d + 1 end_POSTSUBSCRIPT
, the eigenvalues of
γ
𝛾
\gamma
italic_γ
are
±
1
plus-or-minus
1
\pm 1
± 1
, say
−
1
1
-1
- 1
with multiplicity
m
𝑚
m
italic_m
and
+
1
1
+1
+ 1
with multiplicity
(
d
+
1
−
m
)
𝑑
1
𝑚
(d+1-m)
( italic_d + 1 - italic_m )
.
By (
2.4
) the corresponding spectral generating function is given by
F
Γ
⁢
(
z
)
subscript
𝐹
Γ
𝑧
\displaystyle F_{\Gamma}(z)
italic_F start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_z )
=
1
−
z
2
2
⁢
(
1
(
z
−
1
)
d
+
1
+
1
(
z
−
1
)
d
+
1
−
m
⁢
(
z
+
1
)
m
)
absent
1
superscript
𝑧
2
2
1
superscript
𝑧
1
𝑑
1
1
superscript
𝑧
1
𝑑
1
𝑚
superscript
𝑧
1
𝑚
\displaystyle=\frac{1-z^{2}}{2}\left(\frac{1}{(z-1)^{d+1}}+\frac{1}{(z-1)^{d+1%
-m}(z+1)^{m}}\right)
= divide start_ARG 1 - italic_z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG 2 end_ARG ( divide start_ARG 1 end_ARG start_ARG ( italic_z - 1 ) start_POSTSUPERSCRIPT italic_d + 1 end_POSTSUPERSCRIPT end_ARG + divide start_ARG 1 end_ARG start_ARG ( italic_z - 1 ) start_POSTSUPERSCRIPT italic_d + 1 - italic_m end_POSTSUPERSCRIPT ( italic_z + 1 ) start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT end_ARG )
=
−
z
+
1
2
⁢
(
z
−
1
)
d
−
1
2
⁢
(
z
−
1
)
d
−
m
⁢
(
z
+
1
)
m
−
1
.
absent
𝑧
1
2
superscript
𝑧
1
𝑑
1
2
superscript
𝑧
1
𝑑
𝑚
superscript
𝑧
1
𝑚
1
\displaystyle=-\frac{z+1}{2(z-1)^{d}}-\frac{1}{2(z-1)^{d-m}(z+1)^{m-1}}.
= - divide start_ARG italic_z + 1 end_ARG start_ARG 2 ( italic_z - 1 ) start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT end_ARG - divide start_ARG 1 end_ARG start_ARG 2 ( italic_z - 1 ) start_POSTSUPERSCRIPT italic_d - italic_m end_POSTSUPERSCRIPT ( italic_z + 1 ) start_POSTSUPERSCRIPT italic_m - 1 end_POSTSUPERSCRIPT end_ARG .
It follows immediately that
m
−
1
𝑚
1
m-1
italic_m - 1
is the order of the pole of
F
Γ
⁢
(
z
)
subscript
𝐹
Γ
𝑧
F_{\Gamma}(z)
italic_F start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_z )
at
z
=
−
1
𝑧
1
z=-1
italic_z = - 1
, and consequently
m
𝑚
m
italic_m
is determined by
Spec
⁡
(
S
d
+
1
/
Γ
)
Spec
superscript
𝑆
𝑑
1
Γ
\operatorname{Spec}(S^{d+1}/\Gamma)
roman_Spec ( italic_S start_POSTSUPERSCRIPT italic_d + 1 end_POSTSUPERSCRIPT / roman_Γ )
.
Since the number of times that the eigenvalue
−
1
1
-1
- 1
is in the spectrum of
γ
𝛾
\gamma
italic_γ
determines the conjugacy class of
Γ
Γ
\Gamma
roman_Γ
in
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
, we conclude that any two isospectral spherical orbifolds of volume
1
2
⁢
vol
⁡
(
S
d
)
1
2
vol
superscript
𝑆
𝑑
\frac{1}{2}\operatorname{vol}(S^{d})
divide start_ARG 1 end_ARG start_ARG 2 end_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT )
are necessarily isometric.
Let
Γ
Γ
\Gamma
roman_Γ
be a subgroup of
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
of order
3
3
3
3
.
Let
γ
𝛾
\gamma
italic_γ
denote any non-trivial element of
Γ
Γ
\Gamma
roman_Γ
so that
Γ
=
{
I
d
+
1
,
γ
,
γ
2
}
Γ
subscript
I
𝑑
1
𝛾
superscript
𝛾
2
\Gamma=\{\operatorname{I}_{d+1},\gamma,\gamma^{2}\}
roman_Γ = { roman_I start_POSTSUBSCRIPT italic_d + 1 end_POSTSUBSCRIPT , italic_γ , italic_γ start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT }
.
Since
γ
𝛾
\gamma
italic_γ
and
γ
2
superscript
𝛾
2
\gamma^{2}
italic_γ start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT
have order
3
3
3
3
, their eigenvalues are as follows:
m
𝑚
m
italic_m
-times
ξ
3
=
e
2
⁢
π
⁢
i
3
subscript
𝜉
3
superscript
𝑒
2
𝜋
i
3
\xi_{3}=e^{\frac{2\pi\mathrm{i}}{3}}
italic_ξ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT = italic_e start_POSTSUPERSCRIPT divide start_ARG 2 italic_π roman_i end_ARG start_ARG 3 end_ARG end_POSTSUPERSCRIPT
,
m
𝑚
m
italic_m
-times
ξ
3
2
superscript
subscript
𝜉
3
2
\xi_{3}^{2}
italic_ξ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT
, and
(
d
+
1
−
2
⁢
m
)
𝑑
1
2
𝑚
(d+1-2m)
( italic_d + 1 - 2 italic_m )
-times
1
1
1
1
, for some integer
m
𝑚
m
italic_m
satisfying
1
≤
m
≤
d
+
1
2
1
𝑚
𝑑
1
2
1\leq m\leq\frac{d+1}{2}
1 ≤ italic_m ≤ divide start_ARG italic_d + 1 end_ARG start_ARG 2 end_ARG
.
Hence,
F
Γ
⁢
(
z
)
subscript
𝐹
Γ
𝑧
\displaystyle F_{\Gamma}(z)
italic_F start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_z )
=
1
−
z
2
3
⁢
(
1
(
z
−
1
)
d
+
1
+
2
(
z
−
1
)
d
+
1
−
2
⁢
m
⁢
(
z
−
ξ
3
)
m
⁢
(
z
−
ξ
3
2
)
m
)
absent
1
superscript
𝑧
2
3
1
superscript
𝑧
1
𝑑
1
2
superscript
𝑧
1
𝑑
1
2
𝑚
superscript
𝑧
subscript
𝜉
3
𝑚
superscript
𝑧
superscript
subscript
𝜉
3
2
𝑚
\displaystyle=\frac{1-z^{2}}{3}\left(\frac{1}{(z-1)^{d+1}}+\frac{2}{(z-1)^{d+1%
-2m}(z-\xi_{3})^{m}(z-\xi_{3}^{2})^{m}}\right)
= divide start_ARG 1 - italic_z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG 3 end_ARG ( divide start_ARG 1 end_ARG start_ARG ( italic_z - 1 ) start_POSTSUPERSCRIPT italic_d + 1 end_POSTSUPERSCRIPT end_ARG + divide start_ARG 2 end_ARG start_ARG ( italic_z - 1 ) start_POSTSUPERSCRIPT italic_d + 1 - 2 italic_m end_POSTSUPERSCRIPT ( italic_z - italic_ξ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT ) start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT ( italic_z - italic_ξ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ) start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT end_ARG )
=
−
z
+
1
3
⁢
(
z
−
1
)
d
−
1
−
z
2
3
⁢
(
z
−
1
)
d
+
1
−
m
⁢
(
z
−
ξ
3
)
m
⁢
(
z
−
ξ
3
2
)
m
.
absent
𝑧
1
3
superscript
𝑧
1
𝑑
1
superscript
𝑧
2
3
superscript
𝑧
1
𝑑
1
𝑚
superscript
𝑧
subscript
𝜉
3
𝑚
superscript
𝑧
superscript
subscript
𝜉
3
2
𝑚
\displaystyle=-\frac{z+1}{3(z-1)^{d}}-\frac{1-z^{2}}{3(z-1)^{d+1-m}(z-\xi_{3})%
^{m}(z-\xi_{3}^{2})^{m}}.
= - divide start_ARG italic_z + 1 end_ARG start_ARG 3 ( italic_z - 1 ) start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT end_ARG - divide start_ARG 1 - italic_z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG 3 ( italic_z - 1 ) start_POSTSUPERSCRIPT italic_d + 1 - italic_m end_POSTSUPERSCRIPT ( italic_z - italic_ξ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT ) start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT ( italic_z - italic_ξ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ) start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT end_ARG .
As above,
m
𝑚
m
italic_m
is an spectral invariant because is the order of the pole of
F
Γ
⁢
(
z
)
subscript
𝐹
Γ
𝑧
F_{\Gamma}(z)
italic_F start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_z )
at
z
=
ξ
3
𝑧
subscript
𝜉
3
z=\xi_{3}
italic_z = italic_ξ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT
.
Furthermore, since
m
𝑚
m
italic_m
determines the conjugacy class of
Γ
Γ
\Gamma
roman_Γ
in
O
⁡
(
d
+
1
)
O
𝑑
1
\operatorname{O}(d+1)
roman_O ( italic_d + 1 )
, we conclude that any two isospectral spherical orbifolds of volume
1
3
⁢
vol
⁡
(
S
d
+
1
)
1
3
vol
superscript
𝑆
𝑑
1
\frac{1}{3}\operatorname{vol}(S^{d+1})
divide start_ARG 1 end_ARG start_ARG 3 end_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT italic_d + 1 end_POSTSUPERSCRIPT )
are necessarily isometric.
∎
Remark 4.2
.
It is not known whether there exist isospectral and non-isometric spherical orbifolds of dimension
≤
4
absent
4
\leq 4
≤ 4
.
There are two good reasons to believe that no such orbifolds exist.
On the one hand, Bari and Hunsicker
[
BH19
]
proved that there are no isospectral and non-isometric lens orbifolds of dimension
≤
4
absent
4
\leq 4
≤ 4
.
On the other hand, Vásquez
[
Vá18
, Prop. 2.4]
proved that there are no almost conjugate, non-conjugate subgroups of the double cover
Spin
⁡
(
4
)
≃
SU
⁡
(
2
)
×
SU
⁡
(
2
)
similar-to-or-equals
Spin
4
SU
2
SU
2
\operatorname{Spin}(4)\simeq\operatorname{SU}(2)\times\operatorname{SU}(2)
roman_Spin ( 4 ) ≃ roman_SU ( 2 ) × roman_SU ( 2 )
of
SO
⁡
(
4
)
SO
4
\operatorname{SO}(4)
roman_SO ( 4 )
.
4.2.
Isospectral spherical space forms of largest volume
We now restrict our attention to manifolds covered by round spheres.
This case is much more complicated than the previous one.
In particular, we need several preliminaries.
Question
1.6
is not applicable in even dimensions because in these dimensions it is known that no examples of isospectral, non-isometric spherical space forms exist.
In fact, the only spherical space forms of dimension
2
⁢
n
2
𝑛
2n
2 italic_n
are
S
2
⁢
n
superscript
𝑆
2
𝑛
S^{2n}
italic_S start_POSTSUPERSCRIPT 2 italic_n end_POSTSUPERSCRIPT
and
P
2
⁢
n
⁢
(
ℝ
)
superscript
𝑃
2
𝑛
ℝ
P^{2n}(\mathbb{R})
italic_P start_POSTSUPERSCRIPT 2 italic_n end_POSTSUPERSCRIPT ( blackboard_R )
, and they are not isospectral because there are no round metrics on them with the same volume and total scalar curvature.
Furthermore, Ikeda
[
Ik80
]
proved that any two isospectral
3
3
3
3
-dimensional spherical space forms are necessarily isometric. We will therefore restrict our attention on spherical space forms of odd dimension
≥
5
absent
5
\geq 5
≥ 5
.
The following spectral invariants, proven by Ikeda
[
Ik80
, Cor. 2.4, 2.8]
, will be very useful.
Proposition 4.3
(Ikeda)
.
Let
S
2
⁢
n
−
1
/
Γ
1
superscript
𝑆
2
𝑛
1
subscript
Γ
1
S^{2n-1}/\Gamma_{1}
italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
S
2
⁢
n
−
1
/
Γ
2
superscript
𝑆
2
𝑛
1
subscript
Γ
2
S^{2n-1}/\Gamma_{2}
italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
be isospectral spherical space forms.
Then,
|
Γ
1
|
=
|
Γ
2
|
subscript
Γ
1
subscript
Γ
2
|\Gamma_{1}|=|\Gamma_{2}|
| roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT | = | roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT |
and
Γ
1
,
Γ
2
subscript
Γ
1
subscript
Γ
2
\Gamma_{1},\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
have the same set of orders of their elements.
In particular,
Γ
1
subscript
Γ
1
\Gamma_{1}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
is cyclic if and only if
Γ
2
subscript
Γ
2
\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
is cyclic.
The first goal is to classify non-cyclic finite subgroups of low order acting freely on an odd-dimensional sphere.
This will allow us to show that the isospectral pairs of spherical space forms of largest volume are realized by lens spaces, at least in low dimensions.
Lemma 4.4
.
If the fundamental group
Γ
Γ
\Gamma
roman_Γ
of a spherical space form
S
2
⁢
n
−
1
/
Γ
superscript
𝑆
2
𝑛
1
Γ
S^{2n-1}/\Gamma
italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / roman_Γ
is non-cyclic and has order strictly less than
24
24
24
24
, then
Γ
Γ
\Gamma
roman_Γ
is isomorphic to one of the following groups:
•
the quaternion group
Q
8
:=
⟨
B
,
R
∣
B
4
=
e
,
R
2
=
B
2
,
R
⁢
B
⁢
R
−
1
=
B
3
⟩
assign
subscript
𝑄
8
inner-product
𝐵
𝑅
formulae-sequence
superscript
𝐵
4
𝑒
formulae-sequence
superscript
𝑅
2
superscript
𝐵
2
𝑅
𝐵
superscript
𝑅
1
superscript
𝐵
3
Q_{8}:=\langle B,R\mid B^{4}=e,\,R^{2}=B^{2},\,RBR^{-1}=B^{3}\rangle
italic_Q start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT := ⟨ italic_B , italic_R ∣ italic_B start_POSTSUPERSCRIPT 4 end_POSTSUPERSCRIPT = italic_e , italic_R start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT , italic_R italic_B italic_R start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT ⟩
of order
8
8
8
8
,
•
the group
P
12
:=
⟨
A
,
B
∣
A
3
=
B
4
=
e
,
B
⁢
A
⁢
B
−
1
=
A
2
⟩
assign
subscript
𝑃
12
inner-product
𝐴
𝐵
formulae-sequence
superscript
𝐴
3
superscript
𝐵
4
𝑒
𝐵
𝐴
superscript
𝐵
1
superscript
𝐴
2
P_{12}:=\langle A,B\mid A^{3}=B^{4}=e,\,BAB^{-1}=A^{2}\rangle
italic_P start_POSTSUBSCRIPT 12 end_POSTSUBSCRIPT := ⟨ italic_A , italic_B ∣ italic_A start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT 4 end_POSTSUPERSCRIPT = italic_e , italic_B italic_A italic_B start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT = italic_A start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ⟩
of order
12
12
12
12
,
•
the generalized quaternion group
Q
16
:=
⟨
B
,
R
∣
B
8
=
e
,
R
2
=
B
4
,
R
⁢
B
⁢
R
−
1
=
B
7
⟩
assign
subscript
𝑄
16
inner-product
𝐵
𝑅
formulae-sequence
superscript
𝐵
8
𝑒
formulae-sequence
superscript
𝑅
2
superscript
𝐵
4
𝑅
𝐵
superscript
𝑅
1
superscript
𝐵
7
Q_{16}:=\langle B,R\mid B^{8}=e,\,R^{2}=B^{4},\,RBR^{-1}=B^{7}\rangle
italic_Q start_POSTSUBSCRIPT 16 end_POSTSUBSCRIPT := ⟨ italic_B , italic_R ∣ italic_B start_POSTSUPERSCRIPT 8 end_POSTSUPERSCRIPT = italic_e , italic_R start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT 4 end_POSTSUPERSCRIPT , italic_R italic_B italic_R start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT 7 end_POSTSUPERSCRIPT ⟩
of order
16
16
16
16
,
•
the group
P
20
:=
⟨
A
,
B
∣
A
5
=
B
4
=
e
,
B
⁢
A
⁢
B
−
1
=
A
4
⟩
assign
subscript
𝑃
20
inner-product
𝐴
𝐵
formulae-sequence
superscript
𝐴
5
superscript
𝐵
4
𝑒
𝐵
𝐴
superscript
𝐵
1
superscript
𝐴
4
P_{20}:=\langle A,B\mid A^{5}=B^{4}=e,\,BAB^{-1}=A^{4}\rangle
italic_P start_POSTSUBSCRIPT 20 end_POSTSUBSCRIPT := ⟨ italic_A , italic_B ∣ italic_A start_POSTSUPERSCRIPT 5 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT 4 end_POSTSUPERSCRIPT = italic_e , italic_B italic_A italic_B start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT = italic_A start_POSTSUPERSCRIPT 4 end_POSTSUPERSCRIPT ⟩
of order
20
20
20
20
.
Moreover, for each group
H
𝐻
H
italic_H
in the above list and
m
∈
ℕ
𝑚
ℕ
m\in\mathbb{N}
italic_m ∈ blackboard_N
, there is up to isometry exactly one spherical space form with fundamental group isomorphic to
H
𝐻
H
italic_H
and dimension
4
⁢
m
+
3
4
𝑚
3
4m+3
4 italic_m + 3
.
Proof.
The proof is deeply based on the classification of spherical space forms obtained by Wolf in
[
Wo
]
.
We will use Wolf’s notation to facilitate the reading and refer to the article
[
Wo01
]
which has a summary of it.
The strategy of the classification of spherical space forms is to classify abstract finite groups
H
𝐻
H
italic_H
admitting fixed point free real representations (i.e.
ρ
:
H
→
SO
⁡
(
d
)
:
𝜌
→
𝐻
SO
𝑑
\rho:H\to\operatorname{SO}(d)
italic_ρ : italic_H → roman_SO ( italic_d )
such that
S
d
−
1
/
ρ
⁢
(
H
)
superscript
𝑆
𝑑
1
𝜌
𝐻
S^{d-1}/\rho(H)
italic_S start_POSTSUPERSCRIPT italic_d - 1 end_POSTSUPERSCRIPT / italic_ρ ( italic_H )
is a spherical space form), called
fixed point free groups
, and then to classify, for each fixed point free group
H
𝐻
H
italic_H
, all of its fixed point free real representations.
We first show that all non-cyclic fixed point free groups of order less than
24
24
24
24
are those listed in the statement.
Fixed point free groups divide into six types: Type I,II,…, VI (see
[
Wo01
, §3]
).
We will show that the number of non-cyclic fixed point free groups with at most
23
23
23
23
elements is
2
2
2
2
for Types I and II, and
0
0
for the rest of types.
The fixed point free groups of Type I are of the form (see
[
Wo01
, Prop. 3.1]
)
(4.3)
H
d
⁢
(
m
,
n
,
r
)
:=
⟨
A
,
B
∣
A
m
=
B
n
=
e
,
B
⁢
A
⁢
B
−
1
=
A
r
⟩
assign
subscript
𝐻
𝑑
𝑚
𝑛
𝑟
inner-product
𝐴
𝐵
formulae-sequence
superscript
𝐴
𝑚
superscript
𝐵
𝑛
𝑒
𝐵
𝐴
superscript
𝐵
1
superscript
𝐴
𝑟
H_{d}(m,n,r):=\langle A,B\mid A^{m}=B^{n}=e,\;BAB^{-1}=A^{r}\rangle
italic_H start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ( italic_m , italic_n , italic_r ) := ⟨ italic_A , italic_B ∣ italic_A start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT = italic_e , italic_B italic_A italic_B start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT = italic_A start_POSTSUPERSCRIPT italic_r end_POSTSUPERSCRIPT ⟩
for some
m
,
n
,
r
,
d
∈
ℕ
𝑚
𝑛
𝑟
𝑑
ℕ
m,n,r,d\in\mathbb{N}
italic_m , italic_n , italic_r , italic_d ∈ blackboard_N
satisfying that
{
(I.1)
gcd
⁡
(
n
⁢
(
r
−
1
)
,
m
)
=
1
,
(I.2)
r
n
≡
1
(
mod
m
)
,
1
≤
r
≤
m
,
(I.3)
d
is the order of
r
in
ℤ
m
×
,
(I.4)
n
/
d
is divisible by every prime divisor of
d
.
cases
(I.1)
𝑛
𝑟
1
𝑚
1
(I.2)
formulae-sequence
superscript
𝑟
𝑛
annotated
1
pmod
𝑚
1
𝑟
𝑚
(I.3)
d
is the order of
r
in
ℤ
m
×
(I.4)
n
/
d
is divisible by every prime divisor of
d
.
\begin{cases}\textup{(I.1)}&\gcd(n(r-1),m)=1,\\
\textup{(I.2)}&r^{n}\equiv 1\pmod{m},\;1\leq r\leq m,\\
\textup{(I.3)}&\text{$d$ is the order of $r$ in $\mathbb{Z}_{m}^{\times}$},\\
\textup{(I.4)}&\text{$n/d$ is divisible by every prime divisor of $d$.}\end{cases}
{ start_ROW start_CELL (I.1) end_CELL start_CELL roman_gcd ( italic_n ( italic_r - 1 ) , italic_m ) = 1 , end_CELL end_ROW start_ROW start_CELL (I.2) end_CELL start_CELL italic_r start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ≡ 1 start_MODIFIER ( roman_mod start_ARG italic_m end_ARG ) end_MODIFIER , 1 ≤ italic_r ≤ italic_m , end_CELL end_ROW start_ROW start_CELL (I.3) end_CELL start_CELL italic_d is the order of italic_r in blackboard_Z start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT start_POSTSUPERSCRIPT × end_POSTSUPERSCRIPT , end_CELL end_ROW start_ROW start_CELL (I.4) end_CELL start_CELL italic_n / italic_d is divisible by every prime divisor of italic_d . end_CELL end_ROW
Note
|
H
d
⁢
(
m
,
n
,
r
)
|
=
m
⁢
n
subscript
𝐻
𝑑
𝑚
𝑛
𝑟
𝑚
𝑛
|H_{d}(m,n,r)|=mn
| italic_H start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ( italic_m , italic_n , italic_r ) | = italic_m italic_n
.
One can easily see that
(4.4)
H
d
⁢
(
m
,
n
,
r
)
⁢
is cyclic
⇔
m
=
1
⇔
d
=
1
⇔
r
=
1
.
iff
subscript
𝐻
𝑑
𝑚
𝑛
𝑟
is cyclic
𝑚
1
iff
𝑑
1
iff
𝑟
1
H_{d}(m,n,r)\text{ is cyclic}\iff m=1\iff d=1\iff r=1.
italic_H start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ( italic_m , italic_n , italic_r ) is cyclic ⇔ italic_m = 1 ⇔ italic_d = 1 ⇔ italic_r = 1 .
Furthermore,
m
≠
2
𝑚
2
m\neq 2
italic_m ≠ 2
since otherwise
r
=
1
𝑟
1
r=1
italic_r = 1
by (I.2) and (
4.4
) gives a contradiction.
Also,
n
=
1
𝑛
1
n=1
italic_n = 1
gives
d
=
1
𝑑
1
d=1
italic_d = 1
by (I.4), so the group is trivial.
Claim 1
.
The only non-cyclic fixed point free groups of Type I of order
<
24
absent
24
<24
< 24
are
H
2
⁢
(
3
,
4
,
2
)
≃
P
12
similar-to-or-equals
subscript
𝐻
2
3
4
2
subscript
𝑃
12
H_{2}(3,4,2)\simeq P_{12}
italic_H start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ( 3 , 4 , 2 ) ≃ italic_P start_POSTSUBSCRIPT 12 end_POSTSUBSCRIPT
and
H
2
⁢
(
5
,
4
,
4
)
≃
P
20
similar-to-or-equals
subscript
𝐻
2
5
4
4
subscript
𝑃
20
H_{2}(5,4,4)\simeq P_{20}
italic_H start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ( 5 , 4 , 4 ) ≃ italic_P start_POSTSUBSCRIPT 20 end_POSTSUBSCRIPT
.
Proof.
Suppose
H
d
⁢
(
m
,
n
,
r
)
subscript
𝐻
𝑑
𝑚
𝑛
𝑟
H_{d}(m,n,r)
italic_H start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ( italic_m , italic_n , italic_r )
is non-cyclic and
m
⁢
n
<
24
𝑚
𝑛
24
mn<24
italic_m italic_n < 24
.
We have
d
≥
2
𝑑
2
d\geq 2
italic_d ≥ 2
,
m
≥
3
𝑚
3
m\geq 3
italic_m ≥ 3
and,
n
≥
4
𝑛
4
n\geq 4
italic_n ≥ 4
by (
4.4
).
It follows from (I.4) that
d
=
2
𝑑
2
d=2
italic_d = 2
and
n
=
4
𝑛
4
n=4
italic_n = 4
.
In fact,
d
≥
4
𝑑
4
d\geq 4
italic_d ≥ 4
implies
n
≥
2
⁢
d
=
8
𝑛
2
𝑑
8
n\geq 2d=8
italic_n ≥ 2 italic_d = 8
, thus
m
⁢
n
≥
24
𝑚
𝑛
24
mn\geq 24
italic_m italic_n ≥ 24
;
d
=
3
𝑑
3
d=3
italic_d = 3
leads to
n
=
9
𝑛
9
n=9
italic_n = 9
thus
m
⁢
n
≥
27
𝑚
𝑛
27
mn\geq 27
italic_m italic_n ≥ 27
;
d
=
2
𝑑
2
d=2
italic_d = 2
forces
n
=
2
⁢
n
′
𝑛
2
superscript
𝑛
′
n=2n^{\prime}
italic_n = 2 italic_n start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
with
n
′
superscript
𝑛
′
n^{\prime}
italic_n start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
divisible by
2
2
2
2
, thus
24
>
m
⁢
n
≥
6
⁢
n
′
24
𝑚
𝑛
6
superscript
𝑛
′
24>mn\geq 6n^{\prime}
24 > italic_m italic_n ≥ 6 italic_n start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
, so
n
′
=
2
superscript
𝑛
′
2
n^{\prime}=2
italic_n start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT = 2
.
Now, (I.1) implies
m
𝑚
m
italic_m
is odd, thus
m
=
3
𝑚
3
m=3
italic_m = 3
or
m
=
5
𝑚
5
m=5
italic_m = 5
.
If
m
=
3
𝑚
3
m=3
italic_m = 3
(resp.
m
=
5
𝑚
5
m=5
italic_m = 5
), then
r
=
2
𝑟
2
r=2
italic_r = 2
(resp.
r
=
4
𝑟
4
r=4
italic_r = 4
) by (I.3), and the proof is complete since (I.1) and (I.2) hold.
∎
A group of Type II is of the form (see
[
Wo01
, Prop. 3.1]
)
(4.5)
H
d
⁢
(
m
,
n
,
r
,
s
,
t
)
:=
⟨
A
,
B
,
R
∣
A
m
=
B
n
=
e
,
B
⁢
A
⁢
B
−
1
=
A
r
,
R
2
=
B
n
/
2
,
R
⁢
A
⁢
R
−
1
=
A
s
,
R
⁢
B
⁢
R
−
1
=
B
t
⟩
assign
subscript
𝐻
𝑑
𝑚
𝑛
𝑟
𝑠
𝑡
inner-product
𝐴
𝐵
𝑅
formulae-sequence
superscript
𝐴
𝑚
superscript
𝐵
𝑛
𝑒
𝐵
𝐴
superscript
𝐵
1
superscript
𝐴
𝑟
formulae-sequence
superscript
𝑅
2
superscript
𝐵
𝑛
2
formulae-sequence
𝑅
𝐴
superscript
𝑅
1
superscript
𝐴
𝑠
𝑅
𝐵
superscript
𝑅
1
superscript
𝐵
𝑡
H_{d}(m,n,r,s,t):=\left\langle A,B,R\mid\begin{array}[]{l}A^{m}=B^{n}=e,\;BAB^%
{-1}=A^{r},\\
R^{2}=B^{n/2},\;RAR^{-1}=A^{s},\;RBR^{-1}=B^{t}\end{array}\right\rangle
italic_H start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ( italic_m , italic_n , italic_r , italic_s , italic_t ) := ⟨ italic_A , italic_B , italic_R ∣ start_ARRAY start_ROW start_CELL italic_A start_POSTSUPERSCRIPT italic_m end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT = italic_e , italic_B italic_A italic_B start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT = italic_A start_POSTSUPERSCRIPT italic_r end_POSTSUPERSCRIPT , end_CELL end_ROW start_ROW start_CELL italic_R start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT italic_n / 2 end_POSTSUPERSCRIPT , italic_R italic_A italic_R start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT = italic_A start_POSTSUPERSCRIPT italic_s end_POSTSUPERSCRIPT , italic_R italic_B italic_R start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT italic_t end_POSTSUPERSCRIPT end_CELL end_ROW end_ARRAY ⟩
for some
m
,
n
,
r
,
d
,
s
,
t
∈
ℕ
𝑚
𝑛
𝑟
𝑑
𝑠
𝑡
ℕ
m,n,r,d,s,t\in\mathbb{N}
italic_m , italic_n , italic_r , italic_d , italic_s , italic_t ∈ blackboard_N
satisfying (I.1)–(I.4) and also
(4.6)
{
(II.1)
s
2
≡
1
(
mod
m
)
,
1
≤
s
≤
m
(II.2)
r
t
−
1
≡
1
(
mod
m
)
,
(II.3)
n
=
2
u
⁢
n
′′
with
u
≥
2
and
gcd
⁡
(
n
′′
,
2
)
=
1
,
(II.4)
t
≡
−
1
(
mod
2
u
)
,
t
2
≡
1
(
mod
n
)
,
1
≤
t
≤
n
cases
(II.1)
formulae-sequence
superscript
𝑠
2
annotated
1
pmod
𝑚
1
𝑠
𝑚
(II.2)
superscript
𝑟
𝑡
1
annotated
1
pmod
𝑚
(II.3)
n
=
2
u
⁢
n
′′
with
u
≥
2
and
gcd
⁡
(
n
′′
,
2
)
=
1
(II.4)
formulae-sequence
𝑡
annotated
1
pmod
superscript
2
𝑢
formulae-sequence
superscript
𝑡
2
annotated
1
pmod
𝑛
1
𝑡
𝑛
\begin{cases}\textup{(II.1)}&s^{2}\equiv 1\pmod{m},\;1\leq s\leq m\\
\textup{(II.2)}&r^{t-1}\equiv 1\pmod{m},\\
\textup{(II.3)}&\textup{$n=2^{u}n^{\prime\prime}$ with $u\geq 2$ and $\gcd(n^{%
\prime\prime},2)=1$},\\
\textup{(II.4)}&t\equiv-1\pmod{2^{u}},\;t^{2}\equiv 1\pmod{n},\;1\leq t\leq n%
\end{cases}
{ start_ROW start_CELL (II.1) end_CELL start_CELL italic_s start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ≡ 1 start_MODIFIER ( roman_mod start_ARG italic_m end_ARG ) end_MODIFIER , 1 ≤ italic_s ≤ italic_m end_CELL end_ROW start_ROW start_CELL (II.2) end_CELL start_CELL italic_r start_POSTSUPERSCRIPT italic_t - 1 end_POSTSUPERSCRIPT ≡ 1 start_MODIFIER ( roman_mod start_ARG italic_m end_ARG ) end_MODIFIER , end_CELL end_ROW start_ROW start_CELL (II.3) end_CELL start_CELL italic_n = 2 start_POSTSUPERSCRIPT italic_u end_POSTSUPERSCRIPT italic_n start_POSTSUPERSCRIPT ′ ′ end_POSTSUPERSCRIPT with italic_u ≥ 2 and roman_gcd ( italic_n start_POSTSUPERSCRIPT ′ ′ end_POSTSUPERSCRIPT , 2 ) = 1 , end_CELL end_ROW start_ROW start_CELL (II.4) end_CELL start_CELL italic_t ≡ - 1 start_MODIFIER ( roman_mod start_ARG 2 start_POSTSUPERSCRIPT italic_u end_POSTSUPERSCRIPT end_ARG ) end_MODIFIER , italic_t start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ≡ 1 start_MODIFIER ( roman_mod start_ARG italic_n end_ARG ) end_MODIFIER , 1 ≤ italic_t ≤ italic_n end_CELL end_ROW
Note that
⟨
A
,
B
⟩
≃
H
d
⁢
(
m
,
n
,
r
)
similar-to-or-equals
𝐴
𝐵
subscript
𝐻
𝑑
𝑚
𝑛
𝑟
\langle A,B\rangle\simeq H_{d}(m,n,r)
⟨ italic_A , italic_B ⟩ ≃ italic_H start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ( italic_m , italic_n , italic_r )
is a proper subgroup of
H
d
⁢
(
m
,
n
,
r
,
s
,
t
)
subscript
𝐻
𝑑
𝑚
𝑛
𝑟
𝑠
𝑡
H_{d}(m,n,r,s,t)
italic_H start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ( italic_m , italic_n , italic_r , italic_s , italic_t )
and
|
H
d
⁢
(
m
,
n
,
r
,
s
,
t
)
|
=
2
⁢
m
⁢
n
subscript
𝐻
𝑑
𝑚
𝑛
𝑟
𝑠
𝑡
2
𝑚
𝑛
|H_{d}(m,n,r,s,t)|=2mn
| italic_H start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ( italic_m , italic_n , italic_r , italic_s , italic_t ) | = 2 italic_m italic_n
.
Claim 2
.
The only non-cyclic fixed point free groups of Type II of order less than
24
24
24
24
are
H
1
⁢
(
1
,
4
,
1
,
1
,
3
)
≃
Q
8
similar-to-or-equals
subscript
𝐻
1
1
4
1
1
3
subscript
𝑄
8
H_{1}(1,4,1,1,3)\simeq Q_{8}
italic_H start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( 1 , 4 , 1 , 1 , 3 ) ≃ italic_Q start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT
and
H
1
⁢
(
1
,
8
,
1
,
1
,
7
)
≃
Q
16
similar-to-or-equals
subscript
𝐻
1
1
8
1
1
7
subscript
𝑄
16
H_{1}(1,8,1,1,7)\simeq Q_{16}
italic_H start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( 1 , 8 , 1 , 1 , 7 ) ≃ italic_Q start_POSTSUBSCRIPT 16 end_POSTSUBSCRIPT
.
Proof.
It is clear that the subgroup
⟨
A
,
B
⟩
𝐴
𝐵
\langle A,B\rangle
⟨ italic_A , italic_B ⟩
must be cyclic since otherwise
m
⁢
n
≥
12
𝑚
𝑛
12
mn\geq 12
italic_m italic_n ≥ 12
by Claim
1
.
Hence,
d
=
m
=
r
=
1
𝑑
𝑚
𝑟
1
d=m=r=1
italic_d = italic_m = italic_r = 1
by (
4.4
),
s
=
1
𝑠
1
s=1
italic_s = 1
by (II.1).
Note (II.2) hold trivially.
Since
|
H
d
⁢
(
m
,
n
,
r
,
s
,
t
)
|
=
2
⁢
n
<
24
subscript
𝐻
𝑑
𝑚
𝑛
𝑟
𝑠
𝑡
2
𝑛
24
|H_{d}(m,n,r,s,t)|=2n<24
| italic_H start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ( italic_m , italic_n , italic_r , italic_s , italic_t ) | = 2 italic_n < 24
, (II.3) forces
n
=
4
𝑛
4
n=4
italic_n = 4
or
n
=
8
𝑛
8
n=8
italic_n = 8
, which give
t
=
3
𝑡
3
t=3
italic_t = 3
and
t
=
7
𝑡
7
t=7
italic_t = 7
respectively, by (II.4).
The first case give
H
1
⁢
(
1
,
4
,
1
,
1
,
3
)
=
⟨
B
,
R
∣
B
4
=
e
,
R
2
=
B
2
,
R
⁢
B
⁢
R
−
1
=
B
3
⟩
subscript
𝐻
1
1
4
1
1
3
inner-product
𝐵
𝑅
formulae-sequence
superscript
𝐵
4
𝑒
formulae-sequence
superscript
𝑅
2
superscript
𝐵
2
𝑅
𝐵
superscript
𝑅
1
superscript
𝐵
3
H_{1}(1,4,1,1,3)=\langle B,R\mid B^{4}=e,\;R^{2}=B^{2},\;RBR^{-1}=B^{3}\rangle
italic_H start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( 1 , 4 , 1 , 1 , 3 ) = ⟨ italic_B , italic_R ∣ italic_B start_POSTSUPERSCRIPT 4 end_POSTSUPERSCRIPT = italic_e , italic_R start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT , italic_R italic_B italic_R start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT ⟩
, which is isomorphic to the quaternion group
Q
8
=
{
±
1
,
±
i
,
±
j
,
±
k
}
subscript
𝑄
8
plus-or-minus
1
plus-or-minus
i
plus-or-minus
j
plus-or-minus
k
Q_{8}=\{\pm 1,\pm\mathrm{i},\pm\mathrm{j},\pm\mathrm{k}\}
italic_Q start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT = { ± 1 , ± roman_i , ± roman_j , ± roman_k }
via
B
↦
i
maps-to
𝐵
i
B\mapsto\mathrm{i}
italic_B ↦ roman_i
and
R
↦
j
maps-to
𝑅
j
R\mapsto\mathrm{j}
italic_R ↦ roman_j
.
The second case gives
H
1
⁢
(
1
,
8
,
1
,
1
,
7
)
=
⟨
B
,
R
∣
B
8
=
e
,
R
2
=
B
4
,
R
⁢
B
⁢
R
−
1
=
B
7
⟩
subscript
𝐻
1
1
8
1
1
7
inner-product
𝐵
𝑅
formulae-sequence
superscript
𝐵
8
𝑒
formulae-sequence
superscript
𝑅
2
superscript
𝐵
4
𝑅
𝐵
superscript
𝑅
1
superscript
𝐵
7
H_{1}(1,8,1,1,7)=\langle B,R\mid B^{8}=e,\;R^{2}=B^{4},\;RBR^{-1}=B^{7}\rangle
italic_H start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( 1 , 8 , 1 , 1 , 7 ) = ⟨ italic_B , italic_R ∣ italic_B start_POSTSUPERSCRIPT 8 end_POSTSUPERSCRIPT = italic_e , italic_R start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT 4 end_POSTSUPERSCRIPT , italic_R italic_B italic_R start_POSTSUPERSCRIPT - 1 end_POSTSUPERSCRIPT = italic_B start_POSTSUPERSCRIPT 7 end_POSTSUPERSCRIPT ⟩
, which is precisely the usual presentation of the quaternion group
Q
16
subscript
𝑄
16
Q_{16}
italic_Q start_POSTSUBSCRIPT 16 end_POSTSUBSCRIPT
.
∎
Any group of Type III (resp. Type IV) has a proper subgroup isomorphic to
H
d
⁢
(
m
,
n
,
r
)
subscript
𝐻
𝑑
𝑚
𝑛
𝑟
H_{d}(m,n,r)
italic_H start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ( italic_m , italic_n , italic_r )
of coindex
8
8
8
8
(resp.
16
16
16
16
) with
n
𝑛
n
italic_n
odd and divisible by
3
3
3
3
(see
[
Wo01
, Prop. 3.1]
).
Thus, it has
8
⁢
m
⁢
n
≥
24
8
𝑚
𝑛
24
8mn\geq 24
8 italic_m italic_n ≥ 24
(resp.
16
⁢
m
⁢
n
≥
48
16
𝑚
𝑛
48
16mn\geq 48
16 italic_m italic_n ≥ 48
) elements.
Furthermore, the groups of Type V and VI have at least 120 elements since
SL
2
⁡
(
𝔽
5
)
subscript
SL
2
subscript
𝔽
5
\operatorname{SL}_{2}(\mathbb{F}_{5})
roman_SL start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ( blackboard_F start_POSTSUBSCRIPT 5 end_POSTSUBSCRIPT )
is a subgroup of them (
[
Wo01
, Top of page 327]
).
This concludes the first part of the proof.
The ways that a fixed point free group
H
𝐻
H
italic_H
embeds into
SO
⁡
(
2
⁢
n
)
SO
2
𝑛
\operatorname{SO}(2n)
roman_SO ( 2 italic_n )
via a fixed point free real representation
ρ
𝜌
\rho
italic_ρ
to give all the isometry classes of
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional spherical space forms of the form
S
2
⁢
n
−
1
/
ρ
⁢
(
H
)
superscript
𝑆
2
𝑛
1
𝜌
𝐻
S^{2n-1}/\rho(H)
italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / italic_ρ ( italic_H )
is quite complicated to be explained.
See
[
Wo01
, §4–5]
for a nice summary, or
[
Wo
, §7.2–3]
for their classifications.
However, our claim follows immediately from
[
Wo01
, Prop. 5.3]
.
More precisely, for any of our four choices of
H
𝐻
H
italic_H
, any two irreducible complex fixed point free representations of
H
𝐻
H
italic_H
are related by a composition with an automorphism of
H
𝐻
H
italic_H
(i.e.
π
k
,
l
≅
π
1
,
1
∘
𝙰
subscript
𝜋
𝑘
𝑙
subscript
𝜋
1
1
𝙰
\pi_{k,l}\cong\pi_{1,1}\circ\mathtt{A}
italic_π start_POSTSUBSCRIPT italic_k , italic_l end_POSTSUBSCRIPT ≅ italic_π start_POSTSUBSCRIPT 1 , 1 end_POSTSUBSCRIPT ∘ typewriter_A
or
α
k
,
l
≅
α
1
,
1
∘
𝙰
subscript
𝛼
𝑘
𝑙
subscript
𝛼
1
1
𝙰
\alpha_{k,l}\cong\alpha_{1,1}\circ\mathtt{A}
italic_α start_POSTSUBSCRIPT italic_k , italic_l end_POSTSUBSCRIPT ≅ italic_α start_POSTSUBSCRIPT 1 , 1 end_POSTSUBSCRIPT ∘ typewriter_A
for some
𝙰
∈
Aut
⁡
(
H
)
𝙰
Aut
𝐻
\mathtt{A}\in\operatorname{Aut}(H)
typewriter_A ∈ roman_Aut ( italic_H )
for all
k
,
l
𝑘
𝑙
k,l
italic_k , italic_l
admitted, when
H
𝐻
H
italic_H
is of Type I or II respectively), and have degree
δ
⁢
(
H
)
=
2
𝛿
𝐻
2
\delta(H)=2
italic_δ ( italic_H ) = 2
.
Hence, any spherical space form with fundamental group isomorphic to
H
𝐻
H
italic_H
is isometric to
(4.7)
S
4
⁢
m
−
1
/
(
(
π
⊕
π
¯
)
⊕
⋯
⊕
(
π
⊕
π
¯
)
⏟
m
⁢
-times
)
⁢
(
H
)
superscript
𝑆
4
𝑚
1
subscript
⏟
direct-sum
direct-sum
𝜋
¯
𝜋
⋯
direct-sum
𝜋
¯
𝜋
𝑚
-times
𝐻
S^{4m-1}/\big{(}\underbrace{(\pi\oplus\bar{\pi})\oplus\dots\oplus(\pi\oplus%
\bar{\pi})}_{m\text{-times}}\big{)}(H)
italic_S start_POSTSUPERSCRIPT 4 italic_m - 1 end_POSTSUPERSCRIPT / ( under⏟ start_ARG ( italic_π ⊕ over¯ start_ARG italic_π end_ARG ) ⊕ ⋯ ⊕ ( italic_π ⊕ over¯ start_ARG italic_π end_ARG ) end_ARG start_POSTSUBSCRIPT italic_m -times end_POSTSUBSCRIPT ) ( italic_H )
for some
m
∈
ℕ
𝑚
ℕ
m\in\mathbb{N}
italic_m ∈ blackboard_N
, where
π
𝜋
\pi
italic_π
denotes any irreducible complex fixed point free representations of
H
𝐻
H
italic_H
.
∎
Lemma
4.4
and Proposition
4.3
imply that any pair of odd-dimensional isospectral and non-isometric spherical space forms
S
2
⁢
n
−
1
/
Γ
1
,
S
2
⁢
n
−
1
/
Γ
2
superscript
𝑆
2
𝑛
1
subscript
Γ
1
superscript
𝑆
2
𝑛
1
subscript
Γ
2
S^{2n-1}/\Gamma_{1},S^{2n-1}/\Gamma_{2}
italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
with
|
Γ
i
|
<
24
subscript
Γ
𝑖
24
|\Gamma_{i}|<24
| roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT | < 24
are necessarily lens spaces. Consequently,
Γ
1
subscript
Γ
1
\Gamma_{1}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
Γ
2
subscript
Γ
2
\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are cyclic.
Therefore, if in a fixed odd dimension
2
⁢
n
−
1
2
𝑛
1
2n-1
2 italic_n - 1
there are isospectral lens spaces with fundamental groups of order strictly less than
24
24
24
24
, then the isospectral pairs of
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional spherical space forms with largest volume will be lens spaces.
For instance, this is the case for the isospectral pair
(4.8)
{
L
⁢
(
11
;
1
,
2
,
3
)
,
L
⁢
(
11
;
1
,
2
,
4
)
}
𝐿
11
1
2
3
𝐿
11
1
2
4
\{L(11;1,2,3),\,L(11;1,2,4)\}
{ italic_L ( 11 ; 1 , 2 , 3 ) , italic_L ( 11 ; 1 , 2 , 4 ) }
of
5
5
5
5
-dimensional lens spaces found by Ikeda
[
Ik80
]
.
See Table
1
for many more examples found with the computer (see e.g.
[
La21
]
).
The next goal is to construct higher dimensional isospectral pairs of lens spaces from such pairs in low dimension.
To facilitate the next statement, we introduce some notation.
Notation 4.5
.
We think of the parameters
s
=
(
s
1
,
…
,
s
n
)
𝑠
subscript
𝑠
1
…
subscript
𝑠
𝑛
s=(s_{1},\dots,s_{n})
italic_s = ( italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT )
of a
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional lens space
L
⁢
(
q
;
s
)
𝐿
𝑞
𝑠
L(q;s)
italic_L ( italic_q ; italic_s )
with fundamental group of order
q
𝑞
q
italic_q
as a list
[
s
1
,
…
,
s
n
]
subscript
𝑠
1
…
subscript
𝑠
𝑛
[s_{1},\dots,s_{n}]
[ italic_s start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_s start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ]
.
As usual, the concatenation of lists is given by
[
a
1
,
…
,
a
m
]
+
[
b
1
,
…
,
b
n
]
=
[
a
1
,
…
,
a
m
,
b
1
,
…
,
b
n
]
subscript
𝑎
1
…
subscript
𝑎
𝑚
subscript
𝑏
1
…
subscript
𝑏
𝑛
subscript
𝑎
1
…
subscript
𝑎
𝑚
subscript
𝑏
1
…
subscript
𝑏
𝑛
[a_{1},\dots,a_{m}]+[b_{1},\dots,b_{n}]=[a_{1},\dots,a_{m},b_{1},\dots,b_{n}]
[ italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT ] + [ italic_b start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_b start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ] = [ italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT , italic_b start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_b start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ]
and
r
⋅
[
a
1
,
…
,
a
n
]
=
[
a
1
,
…
,
a
n
]
+
⋯
+
[
a
1
,
…
,
a
n
]
⋅
𝑟
subscript
𝑎
1
…
subscript
𝑎
𝑛
subscript
𝑎
1
…
subscript
𝑎
𝑛
⋯
subscript
𝑎
1
…
subscript
𝑎
𝑛
r\cdot[a_{1},\dots,a_{n}]=[a_{1},\dots,a_{n}]+\dots+[a_{1},\dots,a_{n}]
italic_r ⋅ [ italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ] = [ italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ] + ⋯ + [ italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ]
for
r
∈
ℕ
𝑟
ℕ
r\in\mathbb{N}
italic_r ∈ blackboard_N
.
For
q
∈
ℕ
𝑞
ℕ
q\in\mathbb{N}
italic_q ∈ blackboard_N
, we set
q
0
=
φ
⁢
(
q
)
/
2
subscript
𝑞
0
𝜑
𝑞
2
q_{0}=\varphi(q)/2
italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = italic_φ ( italic_q ) / 2
, where
φ
⁢
(
q
)
=
|
ℤ
q
×
|
𝜑
𝑞
superscript
subscript
ℤ
𝑞
\varphi(q)=|\mathbb{Z}_{q}^{\times}|
italic_φ ( italic_q ) = | blackboard_Z start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT × end_POSTSUPERSCRIPT |
is Euler’s totient function, defined to be the number of units in
ℤ
q
=
ℤ
/
q
⁢
ℤ
subscript
ℤ
𝑞
ℤ
𝑞
ℤ
\mathbb{Z}_{q}=\mathbb{Z}/q\mathbb{Z}
blackboard_Z start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT = blackboard_Z / italic_q blackboard_Z
.
Let
t
⁢
(
q
)
=
[
t
1
,
…
,
t
q
0
]
𝑡
𝑞
subscript
𝑡
1
…
subscript
𝑡
subscript
𝑞
0
t(q)=[t_{1},\dots,t_{q_{0}}]
italic_t ( italic_q ) = [ italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_t start_POSTSUBSCRIPT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ]
, where
{
±
t
1
,
…
,
±
t
q
0
}
plus-or-minus
subscript
𝑡
1
…
plus-or-minus
subscript
𝑡
subscript
𝑞
0
\{\pm t_{1},\dots,\pm t_{q_{0}}\}
{ ± italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , ± italic_t start_POSTSUBSCRIPT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_POSTSUBSCRIPT }
is a representative set of
ℤ
q
×
superscript
subscript
ℤ
𝑞
\mathbb{Z}_{q}^{\times}
blackboard_Z start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT × end_POSTSUPERSCRIPT
, i.e. for any
m
∈
ℤ
𝑚
ℤ
m\in\mathbb{Z}
italic_m ∈ blackboard_Z
prime to
q
𝑞
q
italic_q
one has
m
≡
t
i
(
mod
q
)
𝑚
annotated
subscript
𝑡
𝑖
pmod
𝑞
m\equiv t_{i}\pmod{q}
italic_m ≡ italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_MODIFIER ( roman_mod start_ARG italic_q end_ARG ) end_MODIFIER
or
m
≡
−
t
i
(
mod
q
)
𝑚
annotated
subscript
𝑡
𝑖
pmod
𝑞
m\equiv-t_{i}\pmod{q}
italic_m ≡ - italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_MODIFIER ( roman_mod start_ARG italic_q end_ARG ) end_MODIFIER
for some (unique)
i
𝑖
i
italic_i
.
For instance,
t
⁢
(
7
)
=
[
1
,
2
,
3
]
𝑡
7
1
2
3
t(7)=[1,2,3]
italic_t ( 7 ) = [ 1 , 2 , 3 ]
and
t
⁢
(
12
)
=
[
1
,
5
]
𝑡
12
1
5
t(12)=[1,5]
italic_t ( 12 ) = [ 1 , 5 ]
.
Theorem 4.6
.
If the
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional lens spaces
L
⁢
(
q
;
s
)
𝐿
𝑞
𝑠
L(q;s)
italic_L ( italic_q ; italic_s )
and
L
⁢
(
q
;
s
′
)
𝐿
𝑞
superscript
𝑠
′
L(q;s^{\prime})
italic_L ( italic_q ; italic_s start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT )
are isospectral and non-isometric, then the
(
2
⁢
n
−
1
+
r
⁢
φ
⁢
(
q
)
)
2
𝑛
1
𝑟
𝜑
𝑞
(2n-1+r\varphi(q))
( 2 italic_n - 1 + italic_r italic_φ ( italic_q ) )
-dimensional lens spaces
(4.9)
L
⁢
(
q
;
s
+
r
⋅
t
⁢
(
q
)
)
and
L
⁢
(
q
;
s
′
+
r
⋅
t
⁢
(
q
)
)
𝐿
𝑞
𝑠
⋅
𝑟
𝑡
𝑞
and
𝐿
𝑞
superscript
𝑠
′
⋅
𝑟
𝑡
𝑞
L(q;s+r\cdot t(q))\quad\text{ and }\quad L(q;s^{\prime}+r\cdot t(q))
italic_L ( italic_q ; italic_s + italic_r ⋅ italic_t ( italic_q ) ) and italic_L ( italic_q ; italic_s start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT + italic_r ⋅ italic_t ( italic_q ) )
are isospectral and non-isometric for every
r
∈
ℕ
𝑟
ℕ
r\in\mathbb{N}
italic_r ∈ blackboard_N
.
Proof.
We fix
r
∈
ℕ
𝑟
ℕ
r\in\mathbb{N}
italic_r ∈ blackboard_N
and write
L
=
L
⁢
(
q
;
s
+
r
⋅
t
⁢
(
q
)
)
𝐿
𝐿
𝑞
𝑠
⋅
𝑟
𝑡
𝑞
L=L(q;s+r\cdot t(q))
italic_L = italic_L ( italic_q ; italic_s + italic_r ⋅ italic_t ( italic_q ) )
and
L
′
=
L
⁢
(
q
;
s
′
+
r
⋅
t
⁢
(
q
)
)
superscript
𝐿
′
𝐿
𝑞
superscript
𝑠
′
⋅
𝑟
𝑡
𝑞
L^{\prime}=L(q;s^{\prime}+r\cdot t(q))
italic_L start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT = italic_L ( italic_q ; italic_s start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT + italic_r ⋅ italic_t ( italic_q ) )
.
It is a simple matter to check that
L
𝐿
L
italic_L
and
L
′
superscript
𝐿
′
L^{\prime}
italic_L start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
are non-isometric using Proposition
2.3
.
We have to show that
F
L
⁢
(
z
)
=
F
L
′
⁢
(
z
)
subscript
𝐹
𝐿
𝑧
subscript
𝐹
superscript
𝐿
′
𝑧
F_{L}(z)=F_{L^{\prime}}(z)
italic_F start_POSTSUBSCRIPT italic_L end_POSTSUBSCRIPT ( italic_z ) = italic_F start_POSTSUBSCRIPT italic_L start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_POSTSUBSCRIPT ( italic_z )
.
Let us denote by
Φ
q
⁢
(
z
)
subscript
Φ
𝑞
𝑧
\Phi_{q}(z)
roman_Φ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT ( italic_z )
the
q
𝑞
q
italic_q
th cyclotomic polynomial;
notice
Φ
q
⁢
(
z
)
=
∏
j
=
1
q
0
(
z
−
ξ
q
t
i
)
⁢
(
z
−
ξ
q
−
t
i
)
subscript
Φ
𝑞
𝑧
superscript
subscript
product
𝑗
1
subscript
𝑞
0
𝑧
superscript
subscript
𝜉
𝑞
subscript
𝑡
𝑖
𝑧
superscript
subscript
𝜉
𝑞
subscript
𝑡
𝑖
\Phi_{q}(z)=\prod_{j=1}^{q_{0}}(z-\xi_{q}^{t_{i}})(z-\xi_{q}^{-t_{i}})
roman_Φ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT ( italic_z ) = ∏ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT - italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT )
.
From
2.7
, it follows that
(4.10)
F
L
⁢
(
z
)
subscript
𝐹
𝐿
𝑧
\displaystyle F_{L}(z)
italic_F start_POSTSUBSCRIPT italic_L end_POSTSUBSCRIPT ( italic_z )
=
1
−
z
2
q
⁢
∑
h
=
0
q
−
1
1
∏
i
=
1
n
(
z
−
ξ
q
h
⁢
s
i
)
⁢
(
z
−
ξ
q
−
h
⁢
s
i
)
⁢
(
1
∏
j
=
1
q
0
(
z
−
ξ
q
h
⁢
t
j
)
⁢
(
z
−
ξ
q
−
h
⁢
t
j
)
)
r
absent
1
superscript
𝑧
2
𝑞
superscript
subscript
ℎ
0
𝑞
1
1
superscript
subscript
product
𝑖
1
𝑛
𝑧
superscript
subscript
𝜉
𝑞
ℎ
subscript
𝑠
𝑖
𝑧
superscript
subscript
𝜉
𝑞
ℎ
subscript
𝑠
𝑖
superscript
1
superscript
subscript
product
𝑗
1
subscript
𝑞
0
𝑧
superscript
subscript
𝜉
𝑞
ℎ
subscript
𝑡
𝑗
𝑧
superscript
subscript
𝜉
𝑞
ℎ
subscript
𝑡
𝑗
𝑟
\displaystyle=\frac{1-z^{2}}{q}\sum_{h=0}^{q-1}\frac{1}{\prod_{i=1}^{n}(z-\xi_%
{q}^{hs_{i}})(z-\xi_{q}^{-hs_{i}})}\left(\frac{1}{\prod_{j=1}^{q_{0}}(z-\xi_{q%
}^{ht_{j}})(z-\xi_{q}^{-ht_{j}})}\right)^{r}
= divide start_ARG 1 - italic_z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG italic_q end_ARG ∑ start_POSTSUBSCRIPT italic_h = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_q - 1 end_POSTSUPERSCRIPT divide start_ARG 1 end_ARG start_ARG ∏ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_h italic_s start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT - italic_h italic_s start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) end_ARG ( divide start_ARG 1 end_ARG start_ARG ∏ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_h italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT - italic_h italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) end_ARG ) start_POSTSUPERSCRIPT italic_r end_POSTSUPERSCRIPT
=
1
−
z
2
q
⁢
1
(
z
−
1
)
2
⁢
n
+
2
⁢
r
⁢
q
0
+
1
Φ
q
⁢
(
z
)
r
⁢
1
−
z
2
q
⁢
∑
h
=
1
q
−
1
1
∏
i
=
1
n
(
z
−
ξ
q
h
⁢
s
i
)
⁢
(
z
−
ξ
q
−
h
⁢
s
i
)
absent
1
superscript
𝑧
2
𝑞
1
superscript
𝑧
1
2
𝑛
2
𝑟
subscript
𝑞
0
1
subscript
Φ
𝑞
superscript
𝑧
𝑟
1
superscript
𝑧
2
𝑞
superscript
subscript
ℎ
1
𝑞
1
1
superscript
subscript
product
𝑖
1
𝑛
𝑧
superscript
subscript
𝜉
𝑞
ℎ
subscript
𝑠
𝑖
𝑧
superscript
subscript
𝜉
𝑞
ℎ
subscript
𝑠
𝑖
\displaystyle=\frac{1-z^{2}}{q}\frac{1}{(z-1)^{2n+2rq_{0}}}+\frac{1}{\Phi_{q}(%
z)^{r}}\frac{1-z^{2}}{q}\sum_{h=1}^{q-1}\frac{1}{\prod_{i=1}^{n}(z-\xi_{q}^{hs%
_{i}})(z-\xi_{q}^{-hs_{i}})}
= divide start_ARG 1 - italic_z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG italic_q end_ARG divide start_ARG 1 end_ARG start_ARG ( italic_z - 1 ) start_POSTSUPERSCRIPT 2 italic_n + 2 italic_r italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT end_ARG + divide start_ARG 1 end_ARG start_ARG roman_Φ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT ( italic_z ) start_POSTSUPERSCRIPT italic_r end_POSTSUPERSCRIPT end_ARG divide start_ARG 1 - italic_z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG italic_q end_ARG ∑ start_POSTSUBSCRIPT italic_h = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_q - 1 end_POSTSUPERSCRIPT divide start_ARG 1 end_ARG start_ARG ∏ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_h italic_s start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) ( italic_z - italic_ξ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT start_POSTSUPERSCRIPT - italic_h italic_s start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT ) end_ARG
=
1
−
z
2
q
⁢
1
(
z
−
1
)
2
⁢
n
+
2
⁢
r
⁢
q
0
+
1
Φ
q
⁢
(
z
)
r
⁢
(
F
L
⁢
(
q
;
s
)
⁢
(
z
)
−
1
−
z
2
q
⁢
1
(
z
−
1
)
2
⁢
n
)
.
absent
1
superscript
𝑧
2
𝑞
1
superscript
𝑧
1
2
𝑛
2
𝑟
subscript
𝑞
0
1
subscript
Φ
𝑞
superscript
𝑧
𝑟
subscript
𝐹
𝐿
𝑞
𝑠
𝑧
1
superscript
𝑧
2
𝑞
1
superscript
𝑧
1
2
𝑛
\displaystyle=\frac{1-z^{2}}{q}\frac{1}{(z-1)^{2n+2rq_{0}}}+\frac{1}{\Phi_{q}(%
z)^{r}}\left(F_{L(q;s)}(z)-\frac{1-z^{2}}{q}\frac{1}{(z-1)^{2n}}\right).
= divide start_ARG 1 - italic_z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG italic_q end_ARG divide start_ARG 1 end_ARG start_ARG ( italic_z - 1 ) start_POSTSUPERSCRIPT 2 italic_n + 2 italic_r italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_POSTSUPERSCRIPT end_ARG + divide start_ARG 1 end_ARG start_ARG roman_Φ start_POSTSUBSCRIPT italic_q end_POSTSUBSCRIPT ( italic_z ) start_POSTSUPERSCRIPT italic_r end_POSTSUPERSCRIPT end_ARG ( italic_F start_POSTSUBSCRIPT italic_L ( italic_q ; italic_s ) end_POSTSUBSCRIPT ( italic_z ) - divide start_ARG 1 - italic_z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG italic_q end_ARG divide start_ARG 1 end_ARG start_ARG ( italic_z - 1 ) start_POSTSUPERSCRIPT 2 italic_n end_POSTSUPERSCRIPT end_ARG ) .
Now, using that
F
L
⁢
(
q
;
s
)
⁢
(
z
)
=
F
L
⁢
(
q
;
s
′
)
⁢
(
z
)
subscript
𝐹
𝐿
𝑞
𝑠
𝑧
subscript
𝐹
𝐿
𝑞
superscript
𝑠
′
𝑧
F_{L(q;s)}(z)=F_{L(q;s^{\prime})}(z)
italic_F start_POSTSUBSCRIPT italic_L ( italic_q ; italic_s ) end_POSTSUBSCRIPT ( italic_z ) = italic_F start_POSTSUBSCRIPT italic_L ( italic_q ; italic_s start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ) end_POSTSUBSCRIPT ( italic_z )
because
L
⁢
(
q
;
s
)
𝐿
𝑞
𝑠
L(q;s)
italic_L ( italic_q ; italic_s )
and
L
⁢
(
q
;
s
′
)
𝐿
𝑞
superscript
𝑠
′
L(q;s^{\prime})
italic_L ( italic_q ; italic_s start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT )
are isospectral by hypothesis, and returning over the steps in (
4.10
) for
s
′
superscript
𝑠
′
s^{\prime}
italic_s start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
, we obtain
F
L
⁢
(
z
)
=
F
L
′
⁢
(
z
)
subscript
𝐹
𝐿
𝑧
subscript
𝐹
superscript
𝐿
′
𝑧
F_{L}(z)=F_{L^{\prime}}(z)
italic_F start_POSTSUBSCRIPT italic_L end_POSTSUBSCRIPT ( italic_z ) = italic_F start_POSTSUBSCRIPT italic_L start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_POSTSUBSCRIPT ( italic_z )
as required.
∎
Table 1.
Isospectral lens spaces for low values of
q
𝑞
q
italic_q
and
n
𝑛
n
italic_n
.
q
q
0
n
Parameters
s
of isospectral lens spaces
11
5
3
[
1
,
2
,
3
]
,
[
1
,
2
,
4
]
7
[
1
,
1
,
2
,
2
,
3
,
3
,
4
]
,
[
1
,
1
,
2
,
2
,
3
,
3
,
5
]
11
[
1
,
1
,
1
,
2
,
2
,
2
,
3
,
3
,
3
,
5
,
5
]
,
[
1
,
1
,
1
,
2
,
2
,
2
,
3
,
3
,
4
,
4
,
4
]
13
6
3
[
1
,
2
,
3
]
,
[
1
,
2
,
4
]
4
[
1
,
2
,
3
,
4
]
,
[
1
,
2
,
3
,
5
]
7
[
1
,
1
,
2
,
2
,
3
,
3
,
5
]
,
[
1
,
1
,
2
,
2
,
3
,
4
,
4
]
8
[
1
,
1
,
2
,
2
,
3
,
3
,
4
,
4
]
,
[
1
,
1
,
2
,
2
,
3
,
3
,
5
,
5
]
16
4
5
[
1
,
1
,
3
,
3
,
5
]
,
[
1
,
1
,
3
,
3
,
7
]
17
8
3
[
1
,
2
,
5
]
,
[
1
,
2
,
6
]
]
4
[
1
,
2
,
3
,
5
]
,
[
1
,
2
,
3
,
6
]
5
[
1
,
2
,
3
,
4
,
5
]
,
[
1
,
2
,
3
,
4
,
6
]
6
[
1
,
2
,
3
,
4
,
5
,
6
]
,
[
1
,
2
,
3
,
4
,
5
,
7
]
10
[
1
,
1
,
2
,
2
,
3
,
4
,
5
,
7
,
7
,
8
]
,
[
1
,
1
,
2
,
2
,
3
,
4
,
6
,
7
,
7
,
8
]
19
9
3
[
1
,
2
,
7
]
,
[
1
,
3
,
4
]
4
[
1
,
2
,
6
,
8
]
,
[
1
,
3
,
4
,
5
]
5
[
1
,
2
,
3
,
4
,
5
]
,
[
1
,
2
,
3
,
4
,
6
]
6
[
1
,
2
,
3
,
4
,
5
,
6
]
,
[
1
,
2
,
3
,
4
,
5
,
7
]
7
[
1
,
2
,
3
,
4
,
5
,
6
,
7
]
,
[
1
,
2
,
3
,
4
,
5
,
6
,
8
]
11
[
1
,
1
,
2
,
2
,
3
,
3
,
4
,
6
,
6
,
7
,
7
]
,
[
1
,
1
,
2
,
2
,
3
,
3
,
4
,
6
,
6
,
9
,
9
]
20
4
5
[
1
,
1
,
3
,
3
,
7
]
,
[
1
,
1
,
3
,
3
,
9
]
21
6
4
[
1
,
2
,
4
,
5
]
,
[
1
,
2
,
4
,
8
]
9
[
1
,
1
,
2
,
2
,
4
,
4
,
5
,
5
,
10
]
,
[
1
,
1
,
2
,
2
,
4
,
4
,
5
,
8
,
8
]
14
[
1
,
1
,
1
,
2
,
2
,
2
,
4
,
4
,
4
,
5
,
5
,
5
,
10
,
10
]
,
[
1
,
1
,
1
,
2
,
2
,
2
,
4
,
4
,
4
,
5
,
5
,
8
,
8
,
8
]
22
5
3
[
1
,
3
,
5
]
,
[
1
,
3
,
7
]
7
[
1
,
1
,
3
,
3
,
5
,
5
,
9
]
,
[
1
,
1
,
3
,
3
,
5
,
7
,
7
]
11
[
1
,
1
,
1
,
3
,
3
,
3
,
5
,
5
,
5
,
9
,
9
]
,
[
1
,
1
,
1
,
3
,
3
,
3
,
5
,
5
,
9
,
9
,
9
]
23
11
4
[
1
,
2
,
4
,
5
]
,
[
1
,
2
,
4
,
8
]
5
[
1
,
2
,
3
,
4
,
11
]
,
[
1
,
2
,
3
,
5
,
6
]
6
[
1
,
2
,
3
,
4
,
5
,
10
]
,
[
1
,
2
,
3
,
4
,
6
,
7
]
7
[
1
,
2
,
3
,
4
,
5
,
6
,
7
]
,
[
1
,
2
,
3
,
4
,
5
,
6
,
8
]
8
[
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
]
,
[
1
,
2
,
3
,
4
,
5
,
6
,
7
,
9
]
9
[
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
9
]
,
[
1
,
2
,
3
,
4
,
5
,
6
,
7
,
8
,
10
]
13
[
1
,
1
,
2
,
3
,
3
,
4
,
4
,
5
,
6
,
7
,
8
,
9
,
10
]
,
[
1
,
1
,
2
,
3
,
3
,
4
,
4
,
5
,
6
,
7
,
8
,
10
,
11
]
14
[
1
,
1
,
2
,
2
,
3
,
5
,
6
,
7
,
8
,
8
,
9
,
9
,
10
,
11
]
⁢
[
1
,
1
,
2
,
2
,
4
,
5
,
6
,
7
,
8
,
8
,
9
,
9
,
10
,
11
]
\begin{array}[]{cccl}q&q_{0}&n&\text{Parameters $s$ of isospectral lens spaces%
}\\
\hline\cr\hline\cr 11&5&3&[1,2,3],[1,2,4]\\
&&7&[1,1,2,2,3,3,4],[1,1,2,2,3,3,5]\\
&&11&[1,1,1,2,2,2,3,3,3,5,5],[1,1,1,2,2,2,3,3,4,4,4]\\
\hline\cr 13&6&3&[1,2,3],[1,2,4]\\
&&4&[1,2,3,4],[1,2,3,5]\\
&&7&[1,1,2,2,3,3,5],[1,1,2,2,3,4,4]\\
&&8&[1,1,2,2,3,3,4,4],[1,1,2,2,3,3,5,5]\\
\hline\cr 16&4&5&[1,1,3,3,5],[1,1,3,3,7]\\
\hline\cr 17&8&3&[1,2,5],[1,2,6]]\\
&&4&[1,2,3,5],[1,2,3,6]\\
&&5&[1,2,3,4,5],[1,2,3,4,6]\\
&&6&[1,2,3,4,5,6],[1,2,3,4,5,7]\\
&&10&[1,1,2,2,3,4,5,7,7,8],[1,1,2,2,3,4,6,7,7,8]\\
\hline\cr 19&9&3&[1,2,7],[1,3,4]\\
&&4&[1,2,6,8],[1,3,4,5]\\
&&5&[1,2,3,4,5],[1,2,3,4,6]\\
&&6&[1,2,3,4,5,6],[1,2,3,4,5,7]\\
&&7&[1,2,3,4,5,6,7],[1,2,3,4,5,6,8]\\
&&11&[1,1,2,2,3,3,4,6,6,7,7],[1,1,2,2,3,3,4,6,6,9,9]\\
\hline\cr 20&4&5&[1,1,3,3,7],[1,1,3,3,9]\\
\hline\cr 21&6&4&[1,2,4,5],[1,2,4,8]\\
&&9&[1,1,2,2,4,4,5,5,10],[1,1,2,2,4,4,5,8,8]\\
&&14&[1,1,1,2,2,2,4,4,4,5,5,5,10,10],[1,1,1,2,2,2,4,4,4,5,5,8,8,8]\\
\hline\cr 22&5&3&[1,3,5],[1,3,7]\\
&&7&[1,1,3,3,5,5,9],[1,1,3,3,5,7,7]\\
&&11&[1,1,1,3,3,3,5,5,5,9,9],[1,1,1,3,3,3,5,5,9,9,9]\\
\hline\cr 23&11&4&[1,2,4,5],[1,2,4,8]\\
&&5&[1,2,3,4,11],[1,2,3,5,6]\\
&&6&[1,2,3,4,5,10],[1,2,3,4,6,7]\\
&&7&[1,2,3,4,5,6,7],[1,2,3,4,5,6,8]\\
&&8&[1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,9]\\
&&9&[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,10]\\
&&13&[1,1,2,3,3,4,4,5,6,7,8,9,10],[1,1,2,3,3,4,4,5,6,7,8,10,11]\\
&&14&[1,1,2,2,3,5,6,7,8,8,9,9,10,11][1,1,2,2,4,5,6,7,8,8,9,9,10,11]\end{array}
start_ARRAY start_ROW start_CELL italic_q end_CELL start_CELL italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_CELL start_CELL italic_n end_CELL start_CELL Parameters italic_s of isospectral lens spaces end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 11 end_CELL start_CELL 5 end_CELL start_CELL 3 end_CELL start_CELL [ 1 , 2 , 3 ] , [ 1 , 2 , 4 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 7 end_CELL start_CELL [ 1 , 1 , 2 , 2 , 3 , 3 , 4 ] , [ 1 , 1 , 2 , 2 , 3 , 3 , 5 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 11 end_CELL start_CELL [ 1 , 1 , 1 , 2 , 2 , 2 , 3 , 3 , 3 , 5 , 5 ] , [ 1 , 1 , 1 , 2 , 2 , 2 , 3 , 3 , 4 , 4 , 4 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 13 end_CELL start_CELL 6 end_CELL start_CELL 3 end_CELL start_CELL [ 1 , 2 , 3 ] , [ 1 , 2 , 4 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 4 end_CELL start_CELL [ 1 , 2 , 3 , 4 ] , [ 1 , 2 , 3 , 5 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 7 end_CELL start_CELL [ 1 , 1 , 2 , 2 , 3 , 3 , 5 ] , [ 1 , 1 , 2 , 2 , 3 , 4 , 4 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 8 end_CELL start_CELL [ 1 , 1 , 2 , 2 , 3 , 3 , 4 , 4 ] , [ 1 , 1 , 2 , 2 , 3 , 3 , 5 , 5 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 16 end_CELL start_CELL 4 end_CELL start_CELL 5 end_CELL start_CELL [ 1 , 1 , 3 , 3 , 5 ] , [ 1 , 1 , 3 , 3 , 7 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 17 end_CELL start_CELL 8 end_CELL start_CELL 3 end_CELL start_CELL [ 1 , 2 , 5 ] , [ 1 , 2 , 6 ] ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 4 end_CELL start_CELL [ 1 , 2 , 3 , 5 ] , [ 1 , 2 , 3 , 6 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 5 end_CELL start_CELL [ 1 , 2 , 3 , 4 , 5 ] , [ 1 , 2 , 3 , 4 , 6 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 6 end_CELL start_CELL [ 1 , 2 , 3 , 4 , 5 , 6 ] , [ 1 , 2 , 3 , 4 , 5 , 7 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 10 end_CELL start_CELL [ 1 , 1 , 2 , 2 , 3 , 4 , 5 , 7 , 7 , 8 ] , [ 1 , 1 , 2 , 2 , 3 , 4 , 6 , 7 , 7 , 8 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 19 end_CELL start_CELL 9 end_CELL start_CELL 3 end_CELL start_CELL [ 1 , 2 , 7 ] , [ 1 , 3 , 4 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 4 end_CELL start_CELL [ 1 , 2 , 6 , 8 ] , [ 1 , 3 , 4 , 5 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 5 end_CELL start_CELL [ 1 , 2 , 3 , 4 , 5 ] , [ 1 , 2 , 3 , 4 , 6 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 6 end_CELL start_CELL [ 1 , 2 , 3 , 4 , 5 , 6 ] , [ 1 , 2 , 3 , 4 , 5 , 7 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 7 end_CELL start_CELL [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ] , [ 1 , 2 , 3 , 4 , 5 , 6 , 8 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 11 end_CELL start_CELL [ 1 , 1 , 2 , 2 , 3 , 3 , 4 , 6 , 6 , 7 , 7 ] , [ 1 , 1 , 2 , 2 , 3 , 3 , 4 , 6 , 6 , 9 , 9 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 20 end_CELL start_CELL 4 end_CELL start_CELL 5 end_CELL start_CELL [ 1 , 1 , 3 , 3 , 7 ] , [ 1 , 1 , 3 , 3 , 9 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 21 end_CELL start_CELL 6 end_CELL start_CELL 4 end_CELL start_CELL [ 1 , 2 , 4 , 5 ] , [ 1 , 2 , 4 , 8 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 9 end_CELL start_CELL [ 1 , 1 , 2 , 2 , 4 , 4 , 5 , 5 , 10 ] , [ 1 , 1 , 2 , 2 , 4 , 4 , 5 , 8 , 8 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 14 end_CELL start_CELL [ 1 , 1 , 1 , 2 , 2 , 2 , 4 , 4 , 4 , 5 , 5 , 5 , 10 , 10 ] , [ 1 , 1 , 1 , 2 , 2 , 2 , 4 , 4 , 4 , 5 , 5 , 8 , 8 , 8 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 22 end_CELL start_CELL 5 end_CELL start_CELL 3 end_CELL start_CELL [ 1 , 3 , 5 ] , [ 1 , 3 , 7 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 7 end_CELL start_CELL [ 1 , 1 , 3 , 3 , 5 , 5 , 9 ] , [ 1 , 1 , 3 , 3 , 5 , 7 , 7 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 11 end_CELL start_CELL [ 1 , 1 , 1 , 3 , 3 , 3 , 5 , 5 , 5 , 9 , 9 ] , [ 1 , 1 , 1 , 3 , 3 , 3 , 5 , 5 , 9 , 9 , 9 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 23 end_CELL start_CELL 11 end_CELL start_CELL 4 end_CELL start_CELL [ 1 , 2 , 4 , 5 ] , [ 1 , 2 , 4 , 8 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 5 end_CELL start_CELL [ 1 , 2 , 3 , 4 , 11 ] , [ 1 , 2 , 3 , 5 , 6 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 6 end_CELL start_CELL [ 1 , 2 , 3 , 4 , 5 , 10 ] , [ 1 , 2 , 3 , 4 , 6 , 7 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 7 end_CELL start_CELL [ 1 , 2 , 3 , 4 , 5 , 6 , 7 ] , [ 1 , 2 , 3 , 4 , 5 , 6 , 8 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 8 end_CELL start_CELL [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ] , [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 9 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 9 end_CELL start_CELL [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 ] , [ 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 10 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 13 end_CELL start_CELL [ 1 , 1 , 2 , 3 , 3 , 4 , 4 , 5 , 6 , 7 , 8 , 9 , 10 ] , [ 1 , 1 , 2 , 3 , 3 , 4 , 4 , 5 , 6 , 7 , 8 , 10 , 11 ] end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL 14 end_CELL start_CELL [ 1 , 1 , 2 , 2 , 3 , 5 , 6 , 7 , 8 , 8 , 9 , 9 , 10 , 11 ] [ 1 , 1 , 2 , 2 , 4 , 5 , 6 , 7 , 8 , 8 , 9 , 9 , 10 , 11 ] end_CELL end_ROW end_ARRAY
Table 2.
Existence of isospectral pairs of lens spaces for low values of
q
𝑞
q
italic_q
and
n
𝑛
n
italic_n
.
n
\
q
11
q
0
=
5
13
q
0
=
6
16
q
0
=
4
17
q
0
=
8
19
q
0
=
9
20
q
0
=
4
21
q
0
=
6
22
q
0
=
5
23
q
0
=
11
⁢
3
⊗
×
−
×
×
−
−
×
−
4
−
⊗
−
×
×
−
×
−
×
5
−
−
⊗
×
×
×
−
−
×
6
−
−
−
⊗
×
−
−
−
×
7
⊗
×
−
−
×
−
−
×
×
8
⊗
×
−
−
−
−
−
×
×
9
−
⊗
×
−
−
×
×
−
×
10
−
⊗
−
×
−
−
×
−
−
11
⊗
−
−
×
×
−
−
×
−
12
⊗
−
−
×
×
−
−
×
−
13
⊗
×
×
×
×
×
−
×
×
14
−
⊗
−
×
×
−
×
−
×
\
𝑛
𝑞
subscript
𝑞
0
5
11
subscript
𝑞
0
6
13
subscript
𝑞
0
4
16
subscript
𝑞
0
8
17
subscript
𝑞
0
9
19
subscript
𝑞
0
4
20
subscript
𝑞
0
6
21
subscript
𝑞
0
5
22
subscript
𝑞
0
11
23
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
3
tensor-product
4
tensor-product
5
tensor-product
6
tensor-product
7
tensor-product
8
tensor-product
9
tensor-product
10
tensor-product
11
tensor-product
12
tensor-product
13
tensor-product
14
tensor-product
\begin{array}[]{cccccccccc}n\backslash q&\underset{q_{0}=5}{11}&\underset{q_{0%
}=6}{13}&\underset{q_{0}=4}{16}&\underset{q_{0}=8}{17}&\underset{q_{0}=9}{19}&%
\underset{q_{0}=4}{20}&\underset{q_{0}=6}{21}&\underset{q_{0}=5}{22}&\underset%
{q_{0}=11}{23}\\[5.69054pt]
\hline\cr\rule{0.0pt}{14.0pt}3&\otimes&\times&-&\times&\times&-&-&\times&-\\
4&-&\otimes&-&\times&\times&-&\times&-&\times\\
5&-&-&\otimes&\times&\times&\times&-&-&\times\\
6&-&-&-&\otimes&\times&-&-&-&\times\\
7&\otimes&\times&-&-&\times&-&-&\times&\times\\
8&\otimes&\times&-&-&-&-&-&\times&\times\\
9&-&\otimes&\times&-&-&\times&\times&-&\times\\
10&-&\otimes&-&\times&-&-&\times&-&-\\
11&\otimes&-&-&\times&\times&-&-&\times&-\\
12&\otimes&-&-&\times&\times&-&-&\times&-\\
13&\otimes&\times&\times&\times&\times&\times&-&\times&\times\\
14&-&\otimes&-&\times&\times&-&\times&-&\times\\
\end{array}
start_ARRAY start_ROW start_CELL italic_n \ italic_q end_CELL start_CELL start_UNDERACCENT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = 5 end_UNDERACCENT start_ARG 11 end_ARG end_CELL start_CELL start_UNDERACCENT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = 6 end_UNDERACCENT start_ARG 13 end_ARG end_CELL start_CELL start_UNDERACCENT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = 4 end_UNDERACCENT start_ARG 16 end_ARG end_CELL start_CELL start_UNDERACCENT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = 8 end_UNDERACCENT start_ARG 17 end_ARG end_CELL start_CELL start_UNDERACCENT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = 9 end_UNDERACCENT start_ARG 19 end_ARG end_CELL start_CELL start_UNDERACCENT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = 4 end_UNDERACCENT start_ARG 20 end_ARG end_CELL start_CELL start_UNDERACCENT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = 6 end_UNDERACCENT start_ARG 21 end_ARG end_CELL start_CELL start_UNDERACCENT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = 5 end_UNDERACCENT start_ARG 22 end_ARG end_CELL start_CELL start_UNDERACCENT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = 11 end_UNDERACCENT start_ARG 23 end_ARG end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 3 end_CELL start_CELL ⊗ end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL - end_CELL end_ROW start_ROW start_CELL 4 end_CELL start_CELL - end_CELL start_CELL ⊗ end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL × end_CELL end_ROW start_ROW start_CELL 5 end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL ⊗ end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL end_ROW start_ROW start_CELL 6 end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL ⊗ end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL end_ROW start_ROW start_CELL 7 end_CELL start_CELL ⊗ end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL × end_CELL end_ROW start_ROW start_CELL 8 end_CELL start_CELL ⊗ end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL × end_CELL end_ROW start_ROW start_CELL 9 end_CELL start_CELL - end_CELL start_CELL ⊗ end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL × end_CELL end_ROW start_ROW start_CELL 10 end_CELL start_CELL - end_CELL start_CELL ⊗ end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL - end_CELL end_ROW start_ROW start_CELL 11 end_CELL start_CELL ⊗ end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL - end_CELL end_ROW start_ROW start_CELL 12 end_CELL start_CELL ⊗ end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL - end_CELL end_ROW start_ROW start_CELL 13 end_CELL start_CELL ⊗ end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL × end_CELL end_ROW start_ROW start_CELL 14 end_CELL start_CELL - end_CELL start_CELL ⊗ end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL × end_CELL start_CELL - end_CELL start_CELL × end_CELL end_ROW end_ARRAY
References:
q
0
=
φ
⁢
(
q
)
2
subscript
𝑞
0
𝜑
𝑞
2
q_{0}=\frac{\varphi(q)}{2}
italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = divide start_ARG italic_φ ( italic_q ) end_ARG start_ARG 2 end_ARG
,
×
\times
×
means that there is an isospectral pair,
⊗
tensor-product
\otimes
⊗
means that there is an isospectral pair which is known to be of largest volume,
−
-
-
means there are no isospectral pairs.
There are no isospectral pairs for
n
≤
14
𝑛
14
n\leq 14
italic_n ≤ 14
and
q
≤
10
𝑞
10
q\leq 10
italic_q ≤ 10
or
q
=
12
,
14
,
15
,
18
𝑞
12
14
15
18
q=12,14,15,18
italic_q = 12 , 14 , 15 , 18
.
This result is very useful in constructing isospectral and non-isometric pairs of lens spaces in arbitrary large dimension and with fundamental group of a fixed size.
For instance, the pair in (
4.8
) implies the existence of
(
2
⁢
n
+
3
)
2
𝑛
3
(2n+3)
( 2 italic_n + 3 )
-dimensional isospectral and non-isometric lens spaces of volume
vol
⁡
(
S
2
⁢
n
+
3
)
/
11
vol
superscript
𝑆
2
𝑛
3
11
\operatorname{vol}(S^{2n+3})/11
roman_vol ( italic_S start_POSTSUPERSCRIPT 2 italic_n + 3 end_POSTSUPERSCRIPT ) / 11
for every
n
∈
ℕ
𝑛
ℕ
n\in\mathbb{N}
italic_n ∈ blackboard_N
.
We call a lens space
irreducible
if it cannot be constructed from a lower dimensional lens space by adding the coefficients
t
⁢
(
q
)
=
[
t
1
,
…
,
t
q
0
]
𝑡
𝑞
subscript
𝑡
1
…
subscript
𝑡
subscript
𝑞
0
t(q)=[t_{1},\dots,t_{q_{0}}]
italic_t ( italic_q ) = [ italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_t start_POSTSUBSCRIPT italic_q start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ]
.
In other words,
L
⁢
(
q
;
s
)
𝐿
𝑞
𝑠
L(q;s)
italic_L ( italic_q ; italic_s )
is irreducible if it is not isometric to
L
⁢
(
q
;
s
0
+
t
⁢
(
q
)
)
𝐿
𝑞
subscript
𝑠
0
𝑡
𝑞
L(q;s_{0}+t(q))
italic_L ( italic_q ; italic_s start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT + italic_t ( italic_q ) )
for any
s
0
subscript
𝑠
0
s_{0}
italic_s start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
, or equivalent, there is
m
∈
ℤ
×
𝑚
superscript
ℤ
m\in\mathbb{Z}^{\times}
italic_m ∈ blackboard_Z start_POSTSUPERSCRIPT × end_POSTSUPERSCRIPT
such that
m
≢
±
s
i
(
mod
q
)
not-equivalent-to
𝑚
annotated
plus-or-minus
subscript
𝑠
𝑖
pmod
𝑞
m\not\equiv\pm s_{i}\pmod{q}
italic_m ≢ ± italic_s start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_MODIFIER ( roman_mod start_ARG italic_q end_ARG ) end_MODIFIER
for all
i
𝑖
i
italic_i
.
After a computational search, Table
1
shows, for each
3
≤
n
≤
14
3
𝑛
14
3\leq n\leq 14
3 ≤ italic_n ≤ 14
and
3
≤
q
≤
23
3
𝑞
23
3\leq q\leq 23
3 ≤ italic_q ≤ 23
, a pair of
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional isospectral and non-isometric irreducible lens spaces with fundamental group of order
q
𝑞
q
italic_q
, in case it exists.
It is worth mentioning that, for each choice of
n
,
q
𝑛
𝑞
n,q
italic_n , italic_q
in the table, there exist more isospectral pairs than those appearing there, and the pair may belong to a larger isospectral family.
The convention is to show the minimal lens space with respect to the lexicographic order that is isospectral to some other non-isometric lens space.
Combining Theorem
4.6
and Table
1
, we obtain that there are pairs of
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional isospectral and non-isometric lens spaces with volume strictly greater than
vol
⁡
(
S
2
⁢
n
−
1
)
/
24
vol
superscript
𝑆
2
𝑛
1
24
\operatorname{vol}(S^{2n-1})/24
roman_vol ( italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT ) / 24
, for many choices of
n
𝑛
n
italic_n
.
Such choices are precisely encoded by condition (
1.3
) of Theorem
1.7
, whose proof follows.
Table
2
summarizes the existence problem of a pair of
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional isospectral and non-isometric lens spaces with fundamental group of order
q
𝑞
q
italic_q
, for the same values of
n
𝑛
n
italic_n
and
q
𝑞
q
italic_q
considered in Table
1
.
In particular, it gives the largest volume of an isospectral pair of spherical space forms for every odd dimension
5
≤
2
⁢
n
−
1
≤
27
5
2
𝑛
1
27
5\leq 2n-1\leq 27
5 ≤ 2 italic_n - 1 ≤ 27
, namely,
vol
⁡
(
S
2
⁢
n
−
1
)
q
vol
superscript
𝑆
2
𝑛
1
𝑞
\frac{\operatorname{vol}(S^{2n-1})}{q}
divide start_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT ) end_ARG start_ARG italic_q end_ARG
with
q
=
11
,
13
,
16
,
17
,
11
,
11
,
13
,
13
,
11
,
11
,
11
,
13
𝑞
11
13
16
17
11
11
13
13
11
11
11
13
q=11,13,16,17,11,11,13,13,11,11,11,13
italic_q = 11 , 13 , 16 , 17 , 11 , 11 , 13 , 13 , 11 , 11 , 11 , 13
for
n
=
3
,
…
,
14
𝑛
3
…
14
n=3,\dots,14
italic_n = 3 , … , 14
respectively.
We conclude the section with some open questions and remarks.
Question 4.7
.
Are isospectral and non-isometric spherical space forms of largest volume always lens spaces?
Remark 4.8
.
To the best of the authors’ knowledge, the smallest size of the fundamental groups of a pair of isospectral spherical space forms with non-cyclic fundamental group known so far is
275
275
275
275
(see
[
Ik97
, §5]
).
In the notation of the proof of Lemma
4.4
, this pair is realized by two irreducible fixed point free representations of the Type I group
H
5
⁢
(
11
,
25
,
3
)
subscript
𝐻
5
11
25
3
H_{5}(11,25,3)
italic_H start_POSTSUBSCRIPT 5 end_POSTSUBSCRIPT ( 11 , 25 , 3 )
that are non-equivalent by automorphisms of
H
5
⁢
(
11
,
25
,
3
)
subscript
𝐻
5
11
25
3
H_{5}(11,25,3)
italic_H start_POSTSUBSCRIPT 5 end_POSTSUBSCRIPT ( 11 , 25 , 3 )
.
The corresponding spherical space forms have dimension
9
9
9
9
.
Remark 4.9
.
In line with the previous remark, it is very feasible to improve Lemma
4.4
by increasing the order to a number greater than
24
24
24
24
.
However, this is not the main obstruction to prove a statement valid for all
n
≥
3
𝑛
3
n\geq 3
italic_n ≥ 3
.
Indeed, the computational results in the search of isospectral lens spaces for
q
≤
64
𝑞
64
q\leq 64
italic_q ≤ 64
provided a much larger set of conditions to (
1.3
) in such a way the only values omitted for
n
≤
30000
𝑛
30000
n\leq 30000
italic_n ≤ 30000
are
5039
,
6479
,
22319
,
23759
,
28799
5039
6479
22319
23759
28799
5039,6479,22319,23759,28799
5039 , 6479 , 22319 , 23759 , 28799
.
A very curious fact in the computational results evidences a negative answer for the question below.
Question 4.10
.
Are there isospectral and non-isometric
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional lens spaces with fundamental group of order
q
𝑞
q
italic_q
satisfying
n
≡
−
1
(
mod
φ
⁢
(
q
)
2
)
𝑛
annotated
1
pmod
𝜑
𝑞
2
n\equiv-1\pmod{\frac{\varphi(q)}{2}}
italic_n ≡ - 1 start_MODIFIER ( roman_mod start_ARG divide start_ARG italic_φ ( italic_q ) end_ARG start_ARG 2 end_ARG end_ARG ) end_MODIFIER
?
Remark 4.11
.
Because of a computational search, we know the largest volume of an
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional pair of isospectral and non-isometric spherical space forms for every
n
≤
14
𝑛
14
n\leq 14
italic_n ≤ 14
. The results of our computation are recorded in Table
2
.
Table
2
implies the existence of an
(
21
+
5
⁢
r
)
21
5
𝑟
(21+5r)
( 21 + 5 italic_r )
-dimensional isospectral pair with volume
vol
⁡
(
S
2
⁢
(
11
+
5
⁢
r
)
−
1
)
11
vol
superscript
𝑆
2
11
5
𝑟
1
11
\frac{\operatorname{vol}(S^{2(11+5r)-1})}{11}
divide start_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT 2 ( 11 + 5 italic_r ) - 1 end_POSTSUPERSCRIPT ) end_ARG start_ARG 11 end_ARG
for every
r
∈
ℕ
𝑟
ℕ
r\in\mathbb{N}
italic_r ∈ blackboard_N
(i.e.
n
=
11
+
5
⁢
r
𝑛
11
5
𝑟
n=11+5r
italic_n = 11 + 5 italic_r
and
q
=
11
𝑞
11
q=11
italic_q = 11
), but it is not clear whether these examples have the largest volumes possible in their dimensions because our computational search was done only for
n
≤
14
𝑛
14
n\leq 14
italic_n ≤ 14
.
It might be possible to prove the non-existence of isospectral lens spaces with fundamental group of order
q
≤
10
𝑞
10
q\leq 10
italic_q ≤ 10
in an arbitrary odd dimension.
In this case, we obtain the largest volume in infinitely many dimensions.
More precisely, the largest volume of an
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional pair of isospectral and non-isometric spherical space forms would be
vol
⁡
(
S
2
⁢
n
−
1
)
11
vol
superscript
𝑆
2
𝑛
1
11
\frac{\operatorname{vol}(S^{2n-1})}{11}
divide start_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT ) end_ARG start_ARG 11 end_ARG
for all
n
𝑛
n
italic_n
congruent to
1
1
1
1
,
2
2
2
2
or
3
3
3
3
modulo
5
5
5
5
and
n
≥
11
𝑛
11
n\geq 11
italic_n ≥ 11
.
5.
Finite part spectrum
The goal of this section is to obtain several statements ensuring that, for a quotient of a CROSS (Compact Rank One Symmetric Space), a convenient finite part of the spectrum (not necessarily the first eigenvalues) is sufficient to obtain the full spectrum under some geometric conditions.
Let
G
𝐺
G
italic_G
be a compact Lie group and
K
𝐾
K
italic_K
a closed subgroup of it.
We endow the homogeneous space
X
:=
G
/
K
assign
𝑋
𝐺
𝐾
X:=G/K
italic_X := italic_G / italic_K
with a normal metric, that is, a Riemannian metric induced by an
Ad
⁡
(
G
)
Ad
𝐺
\operatorname{Ad}(G)
roman_Ad ( italic_G )
-invariant inner product
⟨
⋅
,
⋅
⟩
⋅
⋅
\langle{\cdot},{\cdot}\rangle
⟨ ⋅ , ⋅ ⟩
on the Lie algebra
𝔤
𝔤
\mathfrak{g}
fraktur_g
of
G
𝐺
G
italic_G
(e.g. minus Killing form of
𝔤
𝔤
\mathfrak{g}
fraktur_g
provided
G
𝐺
G
italic_G
is semisimple).
For
Γ
Γ
\Gamma
roman_Γ
a discrete (hence finite) subgroup of
G
𝐺
G
italic_G
, the right regular representation of
G
𝐺
G
italic_G
on
L
2
⁢
(
Γ
\
G
)
superscript
𝐿
2
\
Γ
𝐺
L^{2}(\Gamma\backslash G)
italic_L start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( roman_Γ \ italic_G )
decomposes as
(5.1)
L
2
⁢
(
Γ
\
G
)
≃
⨁
(
π
,
V
π
)
∈
G
^
n
Γ
⁢
(
π
)
⁢
V
π
.
similar-to-or-equals
superscript
𝐿
2
\
Γ
𝐺
subscript
direct-sum
𝜋
subscript
𝑉
𝜋
^
𝐺
subscript
𝑛
Γ
𝜋
subscript
𝑉
𝜋
L^{2}(\Gamma\backslash G)\simeq\bigoplus_{(\pi,V_{\pi})\in\widehat{G}}n_{%
\Gamma}(\pi)\,V_{\pi}.
italic_L start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( roman_Γ \ italic_G ) ≃ ⨁ start_POSTSUBSCRIPT ( italic_π , italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT ) ∈ over^ start_ARG italic_G end_ARG end_POSTSUBSCRIPT italic_n start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_π ) italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT .
Unlike the case of non-compact semisimple Lie groups, the multiplicity
n
Γ
⁢
(
π
)
subscript
𝑛
Γ
𝜋
n_{\Gamma}(\pi)
italic_n start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_π )
of
π
𝜋
\pi
italic_π
in
L
2
⁢
(
Γ
\
G
)
superscript
𝐿
2
\
Γ
𝐺
L^{2}(\Gamma\backslash G)
italic_L start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( roman_Γ \ italic_G )
can be easily determined by
n
Γ
⁢
(
π
)
=
dim
V
π
Γ
subscript
𝑛
Γ
𝜋
dimension
superscript
subscript
𝑉
𝜋
Γ
n_{\Gamma}(\pi)=\dim V_{\pi}^{\Gamma}
italic_n start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_π ) = roman_dim italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ end_POSTSUPERSCRIPT
.
The spectrum
Spec
⁡
(
Γ
\
X
)
Spec
\
Γ
𝑋
\operatorname{Spec}(\Gamma\backslash X)
roman_Spec ( roman_Γ \ italic_X )
of the Laplace-Beltrami operator
Δ
Δ
\Delta
roman_Δ
on
Γ
\
X
\
Γ
𝑋
\Gamma\backslash X
roman_Γ \ italic_X
is determined by these coefficients since the multiplicity of a non-negative real number
λ
𝜆
\lambda
italic_λ
in
Spec
⁡
(
Γ
\
X
)
Spec
\
Γ
𝑋
\operatorname{Spec}(\Gamma\backslash X)
roman_Spec ( roman_Γ \ italic_X )
is given by
(5.2)
mult
Γ
⁡
(
λ
)
:=
∑
(
π
,
V
π
)
∈
G
^
∣
λ
⁢
(
C
,
π
)
=
λ
n
Γ
⁢
(
π
)
⁢
dim
V
π
K
,
assign
subscript
mult
Γ
𝜆
subscript
𝜋
subscript
𝑉
𝜋
conditional
^
𝐺
𝜆
𝐶
𝜋
𝜆
subscript
𝑛
Γ
𝜋
dimension
superscript
subscript
𝑉
𝜋
𝐾
\operatorname{mult}_{\Gamma}(\lambda):=\sum_{(\pi,V_{\pi})\in\widehat{G}\,\mid%
\,\lambda(C,\pi)=\lambda}n_{\Gamma}(\pi)\,\dim V_{\pi}^{K},
roman_mult start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_λ ) := ∑ start_POSTSUBSCRIPT ( italic_π , italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT ) ∈ over^ start_ARG italic_G end_ARG ∣ italic_λ ( italic_C , italic_π ) = italic_λ end_POSTSUBSCRIPT italic_n start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_π ) roman_dim italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_K end_POSTSUPERSCRIPT ,
where
λ
⁢
(
C
,
π
)
𝜆
𝐶
𝜋
\lambda(C,\pi)
italic_λ ( italic_C , italic_π )
is the scalar for which the Casimir operator
C
𝐶
C
italic_C
associated to
(
𝔤
,
⟨
⋅
,
⋅
⟩
)
𝔤
⋅
⋅
(\mathfrak{g},\langle{\cdot},{\cdot}\rangle)
( fraktur_g , ⟨ ⋅ , ⋅ ⟩ )
acts on
V
π
subscript
𝑉
𝜋
V_{\pi}
italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT
.
The value of
λ
⁢
(
C
,
π
)
𝜆
𝐶
𝜋
\lambda(C,\pi)
italic_λ ( italic_C , italic_π )
can be computed in terms of the highest weight of
π
𝜋
\pi
italic_π
via Freudenthal’s formula.
Note that the sum in (
5.2
) is restricted to
G
^
K
:=
{
π
∈
G
^
:
V
π
K
≠
0
}
assign
subscript
^
𝐺
𝐾
conditional-set
𝜋
^
𝐺
superscript
subscript
𝑉
𝜋
𝐾
0
\widehat{G}_{K}:=\{\pi\in\widehat{G}:V_{\pi}^{K}\neq 0\}
over^ start_ARG italic_G end_ARG start_POSTSUBSCRIPT italic_K end_POSTSUBSCRIPT := { italic_π ∈ over^ start_ARG italic_G end_ARG : italic_V start_POSTSUBSCRIPT italic_π end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_K end_POSTSUPERSCRIPT ≠ 0 }
, the
spherical representations
of the pair
(
G
,
K
)
𝐺
𝐾
(G,K)
( italic_G , italic_K )
.
It follows from (
5.2
) that
Spec
⁡
(
Γ
\
X
)
Spec
\
Γ
𝑋
\operatorname{Spec}(\Gamma\backslash X)
roman_Spec ( roman_Γ \ italic_X )
is included in
Spec
⁡
(
X
)
Spec
𝑋
\operatorname{Spec}(X)
roman_Spec ( italic_X )
in the sense that every eigenvalue
λ
𝜆
\lambda
italic_λ
in
Spec
⁡
(
Γ
\
X
)
Spec
\
Γ
𝑋
\operatorname{Spec}(\Gamma\backslash X)
roman_Spec ( roman_Γ \ italic_X )
is necessarily in
Spec
⁡
(
X
)
Spec
𝑋
\operatorname{Spec}(X)
roman_Spec ( italic_X )
and
mult
Γ
⁡
(
λ
)
≤
mult
⁡
(
λ
)
subscript
mult
Γ
𝜆
mult
𝜆
\operatorname{mult}_{\Gamma}(\lambda)\leq\operatorname{mult}(\lambda)
roman_mult start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_λ ) ≤ roman_mult ( italic_λ )
, where
mult
⁡
(
λ
)
mult
𝜆
\operatorname{mult}(\lambda)
roman_mult ( italic_λ )
stands for the multiplicity of
λ
𝜆
\lambda
italic_λ
in
Spec
⁡
(
X
)
Spec
𝑋
\operatorname{Spec}(X)
roman_Spec ( italic_X )
.
From now on we assume that
X
𝑋
X
italic_X
is a simply connected CROSS realized as in (
1.4
), that is,
S
n
=
SO
⁡
(
n
+
1
)
/
SO
⁡
(
n
)
superscript
𝑆
𝑛
SO
𝑛
1
SO
𝑛
S^{n}=\operatorname{SO}(n+1)/\operatorname{SO}(n)
italic_S start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT = roman_SO ( italic_n + 1 ) / roman_SO ( italic_n )
,
P
n
⁢
(
ℂ
)
=
SU
⁡
(
n
+
1
)
/
S
⁡
(
U
⁡
(
n
)
×
U
⁡
(
1
)
)
superscript
𝑃
𝑛
ℂ
SU
𝑛
1
S
U
𝑛
U
1
P^{n}(\mathbb{C})=\operatorname{SU}(n+1)/\operatorname{S}(\operatorname{U}(n)%
\times\operatorname{U}(1))
italic_P start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( blackboard_C ) = roman_SU ( italic_n + 1 ) / roman_S ( roman_U ( italic_n ) × roman_U ( 1 ) )
,
P
n
⁢
(
ℍ
)
=
Sp
⁡
(
n
+
1
)
/
Sp
⁡
(
n
)
×
Sp
⁡
(
1
)
superscript
𝑃
𝑛
ℍ
Sp
𝑛
1
Sp
𝑛
Sp
1
P^{n}(\mathbb{H})=\operatorname{Sp}(n+1)/\operatorname{Sp}(n)\times%
\operatorname{Sp}(1)
italic_P start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( blackboard_H ) = roman_Sp ( italic_n + 1 ) / roman_Sp ( italic_n ) × roman_Sp ( 1 )
,
P
2
⁢
(
𝕆
)
=
F
4
/
Spin
⁡
(
9
)
superscript
𝑃
2
𝕆
subscript
F
4
Spin
9
P^{2}(\mathbb{O})=\operatorname{F}_{4}/\operatorname{Spin}(9)
italic_P start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( blackboard_O ) = roman_F start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT / roman_Spin ( 9 )
.
We endow
X
𝑋
X
italic_X
with the symmetric metric such that the sectional curvature is constantly one for spheres and satisfies
1
≤
sec
≤
4
1
sec
4
1\leq\operatorname{sec}\leq 4
1 ≤ roman_sec ≤ 4
for the rest of the cases.
It turns out that the spherical representations of
(
G
,
K
)
𝐺
𝐾
(G,K)
( italic_G , italic_K )
are given by a single string of representations
(5.3)
G
^
K
=
{
(
π
k
,
V
k
)
:
k
≥
0
}
subscript
^
𝐺
𝐾
conditional-set
subscript
𝜋
𝑘
subscript
𝑉
𝑘
𝑘
0
\widehat{G}_{K}=\{(\pi_{k},V_{k}):k\geq 0\}
over^ start_ARG italic_G end_ARG start_POSTSUBSCRIPT italic_K end_POSTSUBSCRIPT = { ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT , italic_V start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) : italic_k ≥ 0 }
with
dim
V
k
K
=
1
dimension
superscript
subscript
𝑉
𝑘
𝐾
1
\dim V_{k}^{K}=1
roman_dim italic_V start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_K end_POSTSUPERSCRIPT = 1
and that
(5.4)
λ
k
:=
λ
⁢
(
C
,
π
k
)
=
{
k
⁢
(
k
+
n
−
1
)
if
⁢
X
=
S
n
,
k
⁢
(
k
+
n
)
if
⁢
X
=
P
n
⁢
(
ℂ
)
,
k
⁢
(
k
+
2
⁢
n
+
1
)
if
⁢
X
=
P
n
⁢
(
ℍ
)
,
k
⁢
(
k
+
11
)
if
⁢
X
=
P
2
⁢
(
𝕆
)
,
assign
subscript
𝜆
𝑘
𝜆
𝐶
subscript
𝜋
𝑘
cases
𝑘
𝑘
𝑛
1
if
𝑋
superscript
𝑆
𝑛
𝑘
𝑘
𝑛
if
𝑋
superscript
𝑃
𝑛
ℂ
𝑘
𝑘
2
𝑛
1
if
𝑋
superscript
𝑃
𝑛
ℍ
𝑘
𝑘
11
if
𝑋
superscript
𝑃
2
𝕆
\lambda_{k}:=\lambda(C,\pi_{k})=\begin{cases}k(k+n-1)&\quad\text{if }X=S^{n},%
\\
k(k+n)&\quad\text{if }X=P^{n}(\mathbb{C}),\\
k(k+2n+1)&\quad\text{if }X=P^{n}(\mathbb{H}),\\
k(k+11)&\quad\text{if }X=P^{2}(\mathbb{O}),\\
\end{cases}
italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT := italic_λ ( italic_C , italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) = { start_ROW start_CELL italic_k ( italic_k + italic_n - 1 ) end_CELL start_CELL if italic_X = italic_S start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT , end_CELL end_ROW start_ROW start_CELL italic_k ( italic_k + italic_n ) end_CELL start_CELL if italic_X = italic_P start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( blackboard_C ) , end_CELL end_ROW start_ROW start_CELL italic_k ( italic_k + 2 italic_n + 1 ) end_CELL start_CELL if italic_X = italic_P start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( blackboard_H ) , end_CELL end_ROW start_ROW start_CELL italic_k ( italic_k + 11 ) end_CELL start_CELL if italic_X = italic_P start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( blackboard_O ) , end_CELL end_ROW
for every
k
≥
0
𝑘
0
k\geq 0
italic_k ≥ 0
.
For a proof, see for instance Lemmas 4.1, 5.1, 6.2, 7.2, and 8.1 in
[
LM21
]
, where
τ
𝜏
\tau
italic_τ
is always the trivial representation of
K
𝐾
K
italic_K
, so its highest weight is
0
0
(see also
[
La16
]
).
It follows that the spectrum of
Γ
\
X
\
Γ
𝑋
\Gamma\backslash X
roman_Γ \ italic_X
is given by the eigenvalues
λ
k
subscript
𝜆
𝑘
\lambda_{k}
italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
having multiplicity
n
Γ
⁢
(
π
k
)
subscript
𝑛
Γ
subscript
𝜋
𝑘
n_{\Gamma}(\pi_{k})
italic_n start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT )
, that is,
(5.5)
Spec
⁡
(
Γ
\
X
)
=
{
{
λ
k
,
…
,
λ
k
⏟
n
Γ
⁢
(
π
k
)
:
k
≥
0
}
}
.
Spec
\
Γ
𝑋
conditional-set
subscript
⏟
subscript
𝜆
𝑘
…
subscript
𝜆
𝑘
subscript
𝑛
Γ
subscript
𝜋
𝑘
𝑘
0
\operatorname{Spec}(\Gamma\backslash X)=\Big{\{}\!\!\Big{\{}\underbrace{%
\lambda_{k},\dots,\lambda_{k}}_{n_{\Gamma}(\pi_{k})}:k\geq 0\Big{\}}\!\!\Big{%
\}}.
roman_Spec ( roman_Γ \ italic_X ) = { { under⏟ start_ARG italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT , … , italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT end_ARG start_POSTSUBSCRIPT italic_n start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) end_POSTSUBSCRIPT : italic_k ≥ 0 } } .
Let
|
Φ
+
|
superscript
Φ
|\Phi^{+}|
| roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT |
denote the number of positive root associated to the complexified Lie algebra
𝔤
ℂ
subscript
𝔤
ℂ
\mathfrak{g}_{\mathbb{C}}
fraktur_g start_POSTSUBSCRIPT blackboard_C end_POSTSUBSCRIPT
.
One has
|
Φ
+
|
=
n
2
,
n
⁢
(
n
−
1
)
,
n
⁢
(
n
+
1
)
2
,
(
n
+
1
)
2
,
24
superscript
Φ
superscript
𝑛
2
𝑛
𝑛
1
𝑛
𝑛
1
2
superscript
𝑛
1
2
24
|\Phi^{+}|=n^{2},n(n-1),\frac{n(n+1)}{2},(n+1)^{2},24
| roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT | = italic_n start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT , italic_n ( italic_n - 1 ) , divide start_ARG italic_n ( italic_n + 1 ) end_ARG start_ARG 2 end_ARG , ( italic_n + 1 ) start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT , 24
for
X
=
S
2
⁢
n
,
S
2
⁢
n
−
1
,
P
n
⁢
(
ℂ
)
,
P
n
⁢
(
ℍ
)
,
P
2
⁢
(
𝕆
)
𝑋
superscript
𝑆
2
𝑛
superscript
𝑆
2
𝑛
1
superscript
𝑃
𝑛
ℂ
superscript
𝑃
𝑛
ℍ
superscript
𝑃
2
𝕆
X=S^{2n},S^{2n-1},P^{n}(\mathbb{C}),P^{n}(\mathbb{H}),P^{2}(\mathbb{O})
italic_X = italic_S start_POSTSUPERSCRIPT 2 italic_n end_POSTSUPERSCRIPT , italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT , italic_P start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( blackboard_C ) , italic_P start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT ( blackboard_H ) , italic_P start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( blackboard_O )
respectively.
The next statement is
[
LM20
, Thm. 1.2]
applied to our case of interest.
Proposition 5.1
.
Let
G
𝐺
G
italic_G
be a classical compact Lie group or the compact simple Lie group
F
4
subscript
F
4
\operatorname{F}_{4}
roman_F start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT
,
and let
{
π
k
:
k
≥
0
}
conditional-set
subscript
𝜋
𝑘
𝑘
0
\{\pi_{k}:k\geq 0\}
{ italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT : italic_k ≥ 0 }
denote the irreducible representations of
G
𝐺
G
italic_G
as in (
5.3
).
Given a positive integer
q
𝑞
q
italic_q
, let
𝒜
𝒜
\mathcal{A}
caligraphic_A
be any finite subset of
ℕ
0
subscript
ℕ
0
\mathbb{N}_{0}
blackboard_N start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
satisfying that
(5.6)
|
𝒜
∩
(
j
+
q
⁢
ℤ
)
|
≥
|
Φ
+
|
+
1
for all
⁢
0
≤
j
≤
q
−
1
.
formulae-sequence
𝒜
𝑗
𝑞
ℤ
superscript
Φ
1
for all
0
𝑗
𝑞
1
|\mathcal{A}\cap(j+q\mathbb{Z})|\geq|\Phi^{+}|+1\quad\text{ for all }0\leq j%
\leq q-1.
| caligraphic_A ∩ ( italic_j + italic_q blackboard_Z ) | ≥ | roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT | + 1 for all 0 ≤ italic_j ≤ italic_q - 1 .
Then, for any finite subgroup
Γ
Γ
\Gamma
roman_Γ
of
G
𝐺
G
italic_G
with
q
𝑞
q
italic_q
divisible by
|
Γ
|
Γ
|\Gamma|
| roman_Γ |
, the finite set of multiplicities
n
Γ
⁢
(
π
k
)
subscript
𝑛
Γ
subscript
𝜋
𝑘
n_{\Gamma}(\pi_{k})
italic_n start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT )
for
k
∈
𝒜
𝑘
𝒜
k\in\mathcal{A}
italic_k ∈ caligraphic_A
determine
n
Γ
⁢
(
π
k
)
subscript
𝑛
Γ
subscript
𝜋
𝑘
n_{\Gamma}(\pi_{k})
italic_n start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT )
for all
k
≥
0
𝑘
0
k\geq 0
italic_k ≥ 0
.
In particular, if
Γ
1
,
Γ
2
subscript
Γ
1
subscript
Γ
2
\Gamma_{1},\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are finite subgroups of
G
𝐺
G
italic_G
with
q
𝑞
q
italic_q
divisible by
|
Γ
i
|
subscript
Γ
𝑖
|\Gamma_{i}|
| roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT |
for
i
=
1
,
2
𝑖
1
2
i=1,2
italic_i = 1 , 2
such that
n
Γ
1
⁢
(
π
k
)
=
n
Γ
2
⁢
(
π
k
)
subscript
𝑛
subscript
Γ
1
subscript
𝜋
𝑘
subscript
𝑛
subscript
Γ
2
subscript
𝜋
𝑘
n_{\Gamma_{1}}(\pi_{k})=n_{\Gamma_{2}}(\pi_{k})
italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) = italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT )
for all
k
∈
𝒜
𝑘
𝒜
k\in\mathcal{A}
italic_k ∈ caligraphic_A
, then
n
Γ
1
⁢
(
π
k
)
=
n
Γ
2
⁢
(
π
k
)
subscript
𝑛
subscript
Γ
1
subscript
𝜋
𝑘
subscript
𝑛
subscript
Γ
2
subscript
𝜋
𝑘
n_{\Gamma_{1}}(\pi_{k})=n_{\Gamma_{2}}(\pi_{k})
italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) = italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT )
for all
k
≥
0
𝑘
0
k\geq 0
italic_k ≥ 0
.
The first step in the proof (see
[
LM20
, Prop. 2.2]
) is to show that there is a polynomial
p
Γ
⁢
(
z
)
subscript
𝑝
Γ
𝑧
p_{\Gamma}(z)
italic_p start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_z )
of degree less than
q
⁢
(
|
Φ
+
|
+
1
)
𝑞
superscript
Φ
1
q(|\Phi^{+}|+1)
italic_q ( | roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT | + 1 )
such that
(5.7)
F
Γ
⁢
(
z
)
:=
∑
k
≥
0
n
Γ
⁢
(
π
k
)
⁢
z
k
=
p
Γ
⁢
(
z
)
(
1
−
z
q
)
|
Φ
+
|
+
1
.
assign
subscript
𝐹
Γ
𝑧
subscript
𝑘
0
subscript
𝑛
Γ
subscript
𝜋
𝑘
superscript
𝑧
𝑘
subscript
𝑝
Γ
𝑧
superscript
1
superscript
𝑧
𝑞
superscript
Φ
1
F_{\Gamma}(z):=\sum_{k\geq 0}n_{\Gamma}(\pi_{k})\,z^{k}=\frac{p_{\Gamma}(z)}{(%
1-z^{q})^{|\Phi^{+}|+1}}.
italic_F start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_z ) := ∑ start_POSTSUBSCRIPT italic_k ≥ 0 end_POSTSUBSCRIPT italic_n start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) italic_z start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT = divide start_ARG italic_p start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_z ) end_ARG start_ARG ( 1 - italic_z start_POSTSUPERSCRIPT italic_q end_POSTSUPERSCRIPT ) start_POSTSUPERSCRIPT | roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT | + 1 end_POSTSUPERSCRIPT end_ARG .
The second one (see
[
LM20
, Prop. 3.1]
) is to expand the right hand side of the above identity and, from the identities corresponding to the
k
𝑘
k
italic_k
-th term for
k
∈
𝒜
𝑘
𝒜
k\in\mathcal{A}
italic_k ∈ caligraphic_A
, obtain the values of all coefficients of
p
Γ
⁢
(
z
)
subscript
𝑝
Γ
𝑧
p_{\Gamma}(z)
italic_p start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_z )
in terms of
n
Γ
⁢
(
π
k
)
subscript
𝑛
Γ
subscript
𝜋
𝑘
n_{\Gamma}(\pi_{k})
italic_n start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT )
for
k
∈
𝒜
𝑘
𝒜
k\in\mathcal{A}
italic_k ∈ caligraphic_A
.
Here is an immediate consequence.
Corollary 5.2
.
Let
X
𝑋
X
italic_X
be a simply connected compact rank one symmetric space realized as in (
1.4
)
Given a positive integer
q
𝑞
q
italic_q
, let
𝒜
𝒜
\mathcal{A}
caligraphic_A
be as in Proposition
5.1
.
Then, for any finite subgroup
Γ
Γ
\Gamma
roman_Γ
of
G
𝐺
G
italic_G
with
q
𝑞
q
italic_q
divisible by
|
Γ
|
Γ
|\Gamma|
| roman_Γ |
, the finite set of multiplicities
mult
Γ
⁡
(
π
k
)
subscript
mult
Γ
subscript
𝜋
𝑘
\operatorname{mult}_{\Gamma}(\pi_{k})
roman_mult start_POSTSUBSCRIPT roman_Γ end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT )
of
λ
k
subscript
𝜆
𝑘
\lambda_{k}
italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
in
Spec
⁡
(
Γ
\
X
)
Spec
\
Γ
𝑋
\operatorname{Spec}(\Gamma\backslash X)
roman_Spec ( roman_Γ \ italic_X )
for each
k
∈
𝒜
𝑘
𝒜
k\in\mathcal{A}
italic_k ∈ caligraphic_A
determine the spectrum
Spec
⁡
(
Γ
\
X
)
Spec
\
Γ
𝑋
\operatorname{Spec}(\Gamma\backslash X)
roman_Spec ( roman_Γ \ italic_X )
of the orbifold
Γ
\
X
\
Γ
𝑋
\Gamma\backslash X
roman_Γ \ italic_X
.
In particular, if
Γ
1
,
Γ
2
subscript
Γ
1
subscript
Γ
2
\Gamma_{1},\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are finite subgroups of
G
𝐺
G
italic_G
with
q
𝑞
q
italic_q
divisible by
|
Γ
i
|
subscript
Γ
𝑖
|\Gamma_{i}|
| roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT |
for
i
=
1
,
2
𝑖
1
2
i=1,2
italic_i = 1 , 2
such that
mult
Γ
1
⁡
(
π
k
)
=
mult
Γ
2
⁡
(
π
k
)
subscript
mult
subscript
Γ
1
subscript
𝜋
𝑘
subscript
mult
subscript
Γ
2
subscript
𝜋
𝑘
\operatorname{mult}_{\Gamma_{1}}(\pi_{k})=\operatorname{mult}_{\Gamma_{2}}(\pi%
_{k})
roman_mult start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) = roman_mult start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT )
for all
k
∈
𝒜
𝑘
𝒜
k\in\mathcal{A}
italic_k ∈ caligraphic_A
, then the orbifolds
Γ
1
\
X
\
subscript
Γ
1
𝑋
\Gamma_{1}\backslash X
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT \ italic_X
and
Γ
2
\
X
\
subscript
Γ
2
𝑋
\Gamma_{2}\backslash X
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT \ italic_X
are isospectral.
We are now in position to prove the main theorem of this section.
Proof of Theorem
1.9
.
We set
q
=
⌊
1
ε
⌋
!
𝑞
1
𝜀
q=\lfloor\frac{1}{\varepsilon}\rfloor!
italic_q = ⌊ divide start_ARG 1 end_ARG start_ARG italic_ε end_ARG ⌋ !
and
(5.8)
N
𝑁
\displaystyle N
italic_N
=
1
+
∑
k
=
0
q
⁢
(
|
Φ
+
|
+
1
)
dim
V
k
.
absent
1
superscript
subscript
𝑘
0
𝑞
superscript
Φ
1
dimension
subscript
𝑉
𝑘
\displaystyle=1+\sum_{k=0}^{q(|\Phi^{+}|+1)}\dim V_{k}.
= 1 + ∑ start_POSTSUBSCRIPT italic_k = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_q ( | roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT | + 1 ) end_POSTSUPERSCRIPT roman_dim italic_V start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT .
Let
Γ
1
,
Γ
2
subscript
Γ
1
subscript
Γ
2
\Gamma_{1},\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
be finite subgroups of
G
𝐺
G
italic_G
such that
q
i
:=
|
Γ
i
|
≤
1
ε
assign
subscript
𝑞
𝑖
subscript
Γ
𝑖
1
𝜀
q_{i}:=|\Gamma_{i}|\leq\frac{1}{\varepsilon}
italic_q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT := | roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT | ≤ divide start_ARG 1 end_ARG start_ARG italic_ε end_ARG
for
i
=
1
,
2
𝑖
1
2
i=1,2
italic_i = 1 , 2
, thus
q
i
subscript
𝑞
𝑖
q_{i}
italic_q start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
divides
q
𝑞
q
italic_q
and
vol
⁡
(
Γ
i
\
X
)
vol
⁡
(
X
)
>
ε
vol
\
subscript
Γ
𝑖
𝑋
vol
𝑋
𝜀
\frac{\operatorname{vol}(\Gamma_{i}\backslash X)}{\operatorname{vol}(X)}>\varepsilon
divide start_ARG roman_vol ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X ) end_ARG start_ARG roman_vol ( italic_X ) end_ARG > italic_ε
.
The converse is obvious, so we assume that the first
N
𝑁
N
italic_N
eigenvalues of
Γ
1
\
X
\
subscript
Γ
1
𝑋
\Gamma_{1}\backslash X
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT \ italic_X
and
Γ
2
\
X
\
subscript
Γ
2
𝑋
\Gamma_{2}\backslash X
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT \ italic_X
coincide.
We write
Spec
⁡
(
Γ
i
\
X
)
Spec
\
subscript
Γ
𝑖
𝑋
\operatorname{Spec}(\Gamma_{i}\backslash X)
roman_Spec ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X )
as
0
=
λ
0
⁢
(
Γ
i
\
X
)
<
λ
1
⁢
(
Γ
i
\
X
)
≤
λ
2
⁢
(
Γ
i
\
X
)
≤
⋯
≤
λ
j
⁢
(
Γ
i
\
X
)
≤
…
0
subscript
𝜆
0
\
subscript
Γ
𝑖
𝑋
subscript
𝜆
1
\
subscript
Γ
𝑖
𝑋
subscript
𝜆
2
\
subscript
Γ
𝑖
𝑋
⋯
subscript
𝜆
𝑗
\
subscript
Γ
𝑖
𝑋
…
0=\lambda_{0}(\Gamma_{i}\backslash X)<\lambda_{1}(\Gamma_{i}\backslash X)\leq%
\lambda_{2}(\Gamma_{i}\backslash X)\leq\dots\leq\lambda_{j}(\Gamma_{i}%
\backslash X)\leq\dots
0 = italic_λ start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X ) < italic_λ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X ) ≤ italic_λ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X ) ≤ ⋯ ≤ italic_λ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X ) ≤ …
counted with multiplicities.
By (
5.5
), it follows that
(5.9)
λ
0
subscript
𝜆
0
\displaystyle\lambda_{0}
italic_λ start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
=
λ
0
⁢
(
Γ
i
\
X
)
,
absent
subscript
𝜆
0
\
subscript
Γ
𝑖
𝑋
\displaystyle=\lambda_{0}(\Gamma_{i}\backslash X),
= italic_λ start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X ) ,
λ
1
subscript
𝜆
1
\displaystyle\lambda_{1}
italic_λ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
=
λ
j
⁢
(
Γ
i
\
X
)
for
⁢
1
≤
j
≤
n
Γ
i
⁢
(
π
1
)
,
formulae-sequence
absent
subscript
𝜆
𝑗
\
subscript
Γ
𝑖
𝑋
for
1
𝑗
subscript
𝑛
subscript
Γ
𝑖
subscript
𝜋
1
\displaystyle=\lambda_{j}(\Gamma_{i}\backslash X)\quad\text{ for }1\leq j\leq n%
_{\Gamma_{i}}(\pi_{1}),
= italic_λ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X ) for 1 ≤ italic_j ≤ italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ) ,
λ
2
subscript
𝜆
2
\displaystyle\lambda_{2}
italic_λ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
=
λ
j
⁢
(
Γ
i
\
X
)
for
⁢
1
≤
j
−
n
Γ
i
⁢
(
π
1
)
≤
n
Γ
i
⁢
(
π
2
)
,
formulae-sequence
absent
subscript
𝜆
𝑗
\
subscript
Γ
𝑖
𝑋
for
1
𝑗
subscript
𝑛
subscript
Γ
𝑖
subscript
𝜋
1
subscript
𝑛
subscript
Γ
𝑖
subscript
𝜋
2
\displaystyle=\lambda_{j}(\Gamma_{i}\backslash X)\quad\text{ for }1\leq j-n_{%
\Gamma_{i}}(\pi_{1})\leq n_{\Gamma_{i}}(\pi_{2}),
= italic_λ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X ) for 1 ≤ italic_j - italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ) ≤ italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ) ,
⋮
⋮
\displaystyle\;\;\vdots
⋮
λ
k
subscript
𝜆
𝑘
\displaystyle\lambda_{k}
italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
=
λ
j
⁢
(
Γ
i
\
X
)
for
⁢
1
≤
j
−
∑
l
=
1
k
−
1
n
Γ
i
⁢
(
π
l
)
≤
n
Γ
i
⁢
(
π
k
)
.
formulae-sequence
absent
subscript
𝜆
𝑗
\
subscript
Γ
𝑖
𝑋
for
1
𝑗
superscript
subscript
𝑙
1
𝑘
1
subscript
𝑛
subscript
Γ
𝑖
subscript
𝜋
𝑙
subscript
𝑛
subscript
Γ
𝑖
subscript
𝜋
𝑘
\displaystyle=\lambda_{j}(\Gamma_{i}\backslash X)\quad\text{ for }1\leq j-{%
\textstyle\sum\limits_{l=1}^{k-1}}n_{\Gamma_{i}}(\pi_{l})\leq n_{\Gamma_{i}}(%
\pi_{k}).
= italic_λ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X ) for 1 ≤ italic_j - ∑ start_POSTSUBSCRIPT italic_l = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_k - 1 end_POSTSUPERSCRIPT italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_l end_POSTSUBSCRIPT ) ≤ italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) .
Recall that
λ
k
subscript
𝜆
𝑘
\lambda_{k}
italic_λ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
is explicitly given in (
5.4
) for any
k
≥
0
𝑘
0
k\geq 0
italic_k ≥ 0
.
Now, since
(5.10)
λ
j
⁢
(
Γ
1
\
X
)
=
λ
j
⁢
(
Γ
2
\
X
)
∀
j
=
0
,
…
,
N
−
1
=
∑
k
=
0
q
⁢
(
|
Φ
+
|
+
1
)
n
Γ
i
⁢
(
π
k
)
,
formulae-sequence
subscript
𝜆
𝑗
\
subscript
Γ
1
𝑋
subscript
𝜆
𝑗
\
subscript
Γ
2
𝑋
formulae-sequence
for-all
𝑗
0
…
𝑁
1
superscript
subscript
𝑘
0
𝑞
superscript
Φ
1
subscript
𝑛
subscript
Γ
𝑖
subscript
𝜋
𝑘
\lambda_{j}(\Gamma_{1}\backslash X)=\lambda_{j}(\Gamma_{2}\backslash X)\quad%
\forall\,j=0,\dots,N-1=\sum\limits_{k=0}^{q(|\Phi^{+}|+1)}n_{\Gamma_{i}}(\pi_{%
k}),
italic_λ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT \ italic_X ) = italic_λ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT \ italic_X ) ∀ italic_j = 0 , … , italic_N - 1 = ∑ start_POSTSUBSCRIPT italic_k = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_q ( | roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT | + 1 ) end_POSTSUPERSCRIPT italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) ,
we obtain that
n
Γ
1
⁢
(
π
k
)
=
n
Γ
2
⁢
(
π
k
)
subscript
𝑛
subscript
Γ
1
subscript
𝜋
𝑘
subscript
𝑛
subscript
Γ
2
subscript
𝜋
𝑘
n_{\Gamma_{1}}(\pi_{k})=n_{\Gamma_{2}}(\pi_{k})
italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) = italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT )
for all
k
=
0
,
…
,
q
⁢
(
|
Φ
+
|
+
1
)
𝑘
0
…
𝑞
superscript
Φ
1
k=0,\dots,q(|\Phi^{+}|+1)
italic_k = 0 , … , italic_q ( | roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT | + 1 )
.
Clearly,
𝒜
:=
{
k
∈
ℕ
0
:
k
≤
q
⁢
(
|
Φ
+
|
+
1
)
}
assign
𝒜
conditional-set
𝑘
subscript
ℕ
0
𝑘
𝑞
superscript
Φ
1
\mathcal{A}:=\{k\in\mathbb{N}_{0}:k\leq q(|\Phi^{+}|+1)\}
caligraphic_A := { italic_k ∈ blackboard_N start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT : italic_k ≤ italic_q ( | roman_Φ start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT | + 1 ) }
satisfies (
5.6
).
Since
q
1
subscript
𝑞
1
q_{1}
italic_q start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
q
2
subscript
𝑞
2
q_{2}
italic_q start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
divide
q
𝑞
q
italic_q
, Proposition
5.1
implies that
n
Γ
1
⁢
(
π
k
)
=
n
Γ
2
⁢
(
π
k
)
subscript
𝑛
subscript
Γ
1
subscript
𝜋
𝑘
subscript
𝑛
subscript
Γ
2
subscript
𝜋
𝑘
n_{\Gamma_{1}}(\pi_{k})=n_{\Gamma_{2}}(\pi_{k})
italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) = italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT )
for all
k
≥
0
𝑘
0
k\geq 0
italic_k ≥ 0
, therefore
Spec
⁡
(
Γ
1
\
X
)
=
Spec
⁡
(
Γ
2
\
X
)
Spec
\
subscript
Γ
1
𝑋
Spec
\
subscript
Γ
2
𝑋
\operatorname{Spec}(\Gamma_{1}\backslash X)=\operatorname{Spec}(\Gamma_{2}%
\backslash X)
roman_Spec ( roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT \ italic_X ) = roman_Spec ( roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT \ italic_X )
.
∎
The next example shows that the condition
vol
⁡
(
Γ
i
\
X
)
vol
⁡
(
X
)
>
ε
vol
\
subscript
Γ
𝑖
𝑋
vol
𝑋
𝜀
\frac{\operatorname{vol}(\Gamma_{i}\backslash X)}{\operatorname{vol}(X)}>\varepsilon
divide start_ARG roman_vol ( roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT \ italic_X ) end_ARG start_ARG roman_vol ( italic_X ) end_ARG > italic_ε
cannot be omitted in Theorem
1.9
.
Example 5.3
.
Let
N
𝑁
N
italic_N
be an arbitrary positive integer.
We will show that there are
3
3
3
3
-dimensional lens orbifolds whose first
N
𝑁
N
italic_N
eigenvalues coincide but which are not isospectral.
We set
X
=
S
3
𝑋
superscript
𝑆
3
X=S^{3}
italic_X = italic_S start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT
, thus
G
=
SO
⁡
(
4
)
𝐺
SO
4
G=\operatorname{SO}(4)
italic_G = roman_SO ( 4 )
,
n
=
2
𝑛
2
n=2
italic_n = 2
.
Let
q
𝑞
q
italic_q
be the smallest integer divisible by
4
4
4
4
such that
(5.11)
N
≤
q
⁢
(
q
+
4
)
16
=
∑
k
=
0
q
2
−
1
(
⌊
k
2
⌋
+
1
)
.
𝑁
𝑞
𝑞
4
16
superscript
subscript
𝑘
0
𝑞
2
1
𝑘
2
1
N\leq\frac{q(q+4)}{16}=\sum_{k=0}^{\frac{q}{2}-1}\big{(}\lfloor\tfrac{k}{2}%
\rfloor+1\big{)}.
italic_N ≤ divide start_ARG italic_q ( italic_q + 4 ) end_ARG start_ARG 16 end_ARG = ∑ start_POSTSUBSCRIPT italic_k = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT divide start_ARG italic_q end_ARG start_ARG 2 end_ARG - 1 end_POSTSUPERSCRIPT ( ⌊ divide start_ARG italic_k end_ARG start_ARG 2 end_ARG ⌋ + 1 ) .
For any divisor
d
𝑑
d
italic_d
of
q
𝑞
q
italic_q
, let
L
d
=
L
⁢
(
q
;
0
,
d
)
subscript
𝐿
𝑑
𝐿
𝑞
0
𝑑
L_{d}=L(q;0,d)
italic_L start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT = italic_L ( italic_q ; 0 , italic_d )
and
Γ
d
=
Γ
q
;
(
0
,
d
)
subscript
Γ
𝑑
subscript
Γ
𝑞
0
𝑑
\Gamma_{d}=\Gamma_{q;(0,d)}
roman_Γ start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT = roman_Γ start_POSTSUBSCRIPT italic_q ; ( 0 , italic_d ) end_POSTSUBSCRIPT
, so
L
d
=
S
3
/
Γ
d
subscript
𝐿
𝑑
superscript
𝑆
3
subscript
Γ
𝑑
L_{d}=S^{3}/\Gamma_{d}
italic_L start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT = italic_S start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT
.
It is evident from Proposition
2.3
that these lens orbifolds are pairwise non-isometric.
One can easily check that the associated congruence lattice
ℒ
d
subscript
ℒ
𝑑
\mathcal{L}_{d}
caligraphic_L start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT
of
L
d
subscript
𝐿
𝑑
L_{d}
italic_L start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT
(see (
2.9
)) is given by
(5.12)
ℒ
d
=
{
(
a
,
b
)
∈
ℤ
2
:
q
d
∣
b
}
=
ℤ
×
q
d
⁢
ℤ
.
subscript
ℒ
𝑑
conditional-set
𝑎
𝑏
superscript
ℤ
2
conditional
𝑞
𝑑
𝑏
ℤ
𝑞
𝑑
ℤ
\mathcal{L}_{d}=\{(a,b)\in\mathbb{Z}^{2}:\tfrac{q}{d}\mid b\}=\mathbb{Z}\times%
\tfrac{q}{d}\mathbb{Z}.
caligraphic_L start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT = { ( italic_a , italic_b ) ∈ blackboard_Z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT : divide start_ARG italic_q end_ARG start_ARG italic_d end_ARG ∣ italic_b } = blackboard_Z × divide start_ARG italic_q end_ARG start_ARG italic_d end_ARG blackboard_Z .
This implies that they are mutually non-isospectral by (
2.8
).
We claim that the first
N
𝑁
N
italic_N
eigenvalues of the Laplacians on
L
1
subscript
𝐿
1
L_{1}
italic_L start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
L
2
subscript
𝐿
2
L_{2}
italic_L start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
coincide.
Since
ℒ
1
=
ℤ
×
q
⁢
ℤ
subscript
ℒ
1
ℤ
𝑞
ℤ
\mathcal{L}_{1}=\mathbb{Z}\times q\mathbb{Z}
caligraphic_L start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT = blackboard_Z × italic_q blackboard_Z
and
ℒ
2
=
ℤ
×
q
2
⁢
ℤ
subscript
ℒ
2
ℤ
𝑞
2
ℤ
\mathcal{L}_{2}=\mathbb{Z}\times\tfrac{q}{2}\mathbb{Z}
caligraphic_L start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT = blackboard_Z × divide start_ARG italic_q end_ARG start_ARG 2 end_ARG blackboard_Z
, it is clear that
N
ℒ
1
⁢
(
k
)
=
N
ℒ
2
⁢
(
k
)
=
1
subscript
𝑁
subscript
ℒ
1
𝑘
subscript
𝑁
subscript
ℒ
2
𝑘
1
N_{\mathcal{L}_{1}}(k)=N_{\mathcal{L}_{2}}(k)=1
italic_N start_POSTSUBSCRIPT caligraphic_L start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_k ) = italic_N start_POSTSUBSCRIPT caligraphic_L start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_k ) = 1
for all
k
<
q
2
𝑘
𝑞
2
k<\tfrac{q}{2}
italic_k < divide start_ARG italic_q end_ARG start_ARG 2 end_ARG
.
Now, (
2.11
) immediately implies that
(5.13)
n
Γ
i
⁢
(
π
k
)
=
dim
V
π
k
Γ
i
=
⌊
k
2
⌋
+
1
∀
k
<
q
2
,
for
i
=
1
,
2
.
formulae-sequence
subscript
𝑛
subscript
Γ
𝑖
subscript
𝜋
𝑘
dimension
superscript
subscript
𝑉
subscript
𝜋
𝑘
subscript
Γ
𝑖
𝑘
2
1
for-all
𝑘
𝑞
2
for
i
=
1
,
2
.
n_{\Gamma_{i}}(\pi_{k})=\dim V_{\pi_{k}}^{\Gamma_{i}}=\lfloor\tfrac{k}{2}%
\rfloor+1\qquad\forall\,k<\tfrac{q}{2},\text{ for $i=1,2$.}
italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) = roman_dim italic_V start_POSTSUBSCRIPT italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT end_POSTSUBSCRIPT start_POSTSUPERSCRIPT roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUPERSCRIPT = ⌊ divide start_ARG italic_k end_ARG start_ARG 2 end_ARG ⌋ + 1 ∀ italic_k < divide start_ARG italic_q end_ARG start_ARG 2 end_ARG , for italic_i = 1 , 2 .
The same reasoning in (
5.9
) tells us that
λ
j
⁢
(
L
1
)
=
λ
j
⁢
(
L
2
)
subscript
𝜆
𝑗
subscript
𝐿
1
subscript
𝜆
𝑗
subscript
𝐿
2
\lambda_{j}(L_{1})=\lambda_{j}(L_{2})
italic_λ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_L start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ) = italic_λ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( italic_L start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT )
for all
j
𝑗
j
italic_j
satisfying
(5.14)
0
≤
j
≤
∑
k
=
0
q
2
−
1
n
Γ
i
⁢
(
π
k
)
=
∑
k
=
0
q
2
−
1
(
⌊
k
2
⌋
+
1
)
0
𝑗
superscript
subscript
𝑘
0
𝑞
2
1
subscript
𝑛
subscript
Γ
𝑖
subscript
𝜋
𝑘
superscript
subscript
𝑘
0
𝑞
2
1
𝑘
2
1
0\leq j\leq\sum_{k=0}^{\frac{q}{2}-1}n_{\Gamma_{i}}(\pi_{k})=\sum_{k=0}^{\frac%
{q}{2}-1}\big{(}\lfloor\tfrac{k}{2}\rfloor+1\big{)}
0 ≤ italic_j ≤ ∑ start_POSTSUBSCRIPT italic_k = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT divide start_ARG italic_q end_ARG start_ARG 2 end_ARG - 1 end_POSTSUPERSCRIPT italic_n start_POSTSUBSCRIPT roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( italic_π start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) = ∑ start_POSTSUBSCRIPT italic_k = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT divide start_ARG italic_q end_ARG start_ARG 2 end_ARG - 1 end_POSTSUPERSCRIPT ( ⌊ divide start_ARG italic_k end_ARG start_ARG 2 end_ARG ⌋ + 1 )
and the assertion follows.
Remark 5.4
.
Although we have considered only the Laplace-Beltrami operator acting on functions on
Γ
\
X
\
Γ
𝑋
\Gamma\backslash X
roman_Γ \ italic_X
, the discussion can be extended to the standard Laplacian acting on smooth sections of homogeneous vector bundles of CROSSes.
Among them, we have the Hodge-Laplace operator acting on smooth
p
𝑝
p
italic_p
-forms, and the Lichnerowicz Laplacian acting on (symmetric)
k
𝑘
k
italic_k
-tensors.
Remark 5.5
.
Can Theorem
1.9
be extended to some (or all) compact symmetric spaces of rank at least two?
The main difficulty for such a symmetric space
G
/
K
𝐺
𝐾
G/K
italic_G / italic_K
is that
G
^
K
subscript
^
𝐺
𝐾
\widehat{G}_{K}
over^ start_ARG italic_G end_ARG start_POSTSUBSCRIPT italic_K end_POSTSUBSCRIPT
cannot be written as a finite union of strings, in the sense of
[
LM20
, Def. 2.1]
(see also
[
LM20
, Rmks. 5.3 and 5.4]
).
6.
Isospectral towers of lens spaces
In this section we will construct isospectral towers of lens spaces in every odd dimension
≥
5
absent
5
\geq 5
≥ 5
. Our construction will make extensive use of some terminology defined by Doyle and DeFord
[
DD18
]
.
Let
r
>
2
,
t
≥
1
formulae-sequence
𝑟
2
𝑡
1
r>2,t\geq 1
italic_r > 2 , italic_t ≥ 1
be positive integers.
Definition 6.1
.
We say that
a
∈
ℤ
n
𝑎
superscript
ℤ
𝑛
a\in\mathbb{Z}^{n}
italic_a ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
is
•
univalent mod
r
𝑟
r
italic_r
if its entries are distinct mod
r
𝑟
r
italic_r
,
•
reversible mod
r
𝑟
r
italic_r
if there exists
c
∈
ℤ
r
𝑐
subscript
ℤ
𝑟
c\in\mathbb{Z}_{r}
italic_c ∈ blackboard_Z start_POSTSUBSCRIPT italic_r end_POSTSUBSCRIPT
such that
a
+
c
𝑎
𝑐
a+c
italic_a + italic_c
and
−
a
𝑎
-a
- italic_a
are equal as multisets mod
r
𝑟
r
italic_r
,
•
good mod
r
𝑟
r
italic_r
if it is univalent or reversible mod
r
𝑟
r
italic_r
,
•
hereditarily good mod
r
𝑟
r
italic_r
if it is good mod
d
𝑑
d
italic_d
for all divisors
d
𝑑
d
italic_d
of
r
𝑟
r
italic_r
, and
•
useful mod
r
𝑟
r
italic_r
if it is hereditarily good and irreversible mod
r
𝑟
r
italic_r
.
Remark 6.2
.
Every
a
∈
ℤ
n
𝑎
superscript
ℤ
𝑛
a\in\mathbb{Z}^{n}
italic_a ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
is reversible (and hence good) mod
1
,
2
1
2
1,2
1 , 2
. So to check whether or not
a
𝑎
a
italic_a
is hereditarily good we need only consider divisors
d
𝑑
d
italic_d
of
r
𝑟
r
italic_r
for which
d
>
2
𝑑
2
d>2
italic_d > 2
. In particular, when
r
𝑟
r
italic_r
is prime
a
∈
ℤ
n
𝑎
superscript
ℤ
𝑛
a\in\mathbb{Z}^{n}
italic_a ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
is hereditarily good mod
r
𝑟
r
italic_r
if and only if it is good mod
r
𝑟
r
italic_r
.
Example 6.3
.
Let
a
=
(
1
,
3
,
6
)
𝑎
1
3
6
a=(1,3,6)
italic_a = ( 1 , 3 , 6 )
. Then
a
𝑎
a
italic_a
is
•
univalent mod
r
𝑟
r
italic_r
when
r
∉
{
1
,
2
,
3
,
5
}
𝑟
1
2
3
5
r\not\in\{1,2,3,5\}
italic_r ∉ { 1 , 2 , 3 , 5 }
,
•
reversible mod
r
𝑟
r
italic_r
when
r
∈
{
1
,
2
,
4
,
7
,
8
}
𝑟
1
2
4
7
8
r\in\{1,2,4,7,8\}
italic_r ∈ { 1 , 2 , 4 , 7 , 8 }
,
•
good mod
r
𝑟
r
italic_r
when
r
≠
3
,
5
𝑟
3
5
r\neq 3,5
italic_r ≠ 3 , 5
,
•
hereditarily good mod
r
𝑟
r
italic_r
when
r
𝑟
r
italic_r
is not divisible by
3
3
3
3
or
5
5
5
5
, and
•
useful mod
r
𝑟
r
italic_r
for any
r
≥
11
𝑟
11
r\geq 11
italic_r ≥ 11
not divisible by
3
3
3
3
or
5
5
5
5
.
Given
r
,
t
,
a
𝑟
𝑡
𝑎
r,t,a
italic_r , italic_t , italic_a
as above, we define the lens space
L
⁢
(
r
,
t
,
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,a)
italic_L ( italic_r , italic_t , italic_a )
by
L
⁢
(
r
,
t
,
a
)
=
L
⁢
(
r
2
⁢
t
;
r
⁢
t
⁢
a
1
+
1
,
…
,
r
⁢
t
⁢
a
n
+
1
)
.
𝐿
𝑟
𝑡
𝑎
𝐿
superscript
𝑟
2
𝑡
𝑟
𝑡
subscript
𝑎
1
1
…
𝑟
𝑡
subscript
𝑎
𝑛
1
L(r,t,a)=L(r^{2}t;rta_{1}+1,\dots,rta_{n}+1).
italic_L ( italic_r , italic_t , italic_a ) = italic_L ( italic_r start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT italic_t ; italic_r italic_t italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT + 1 , … , italic_r italic_t italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT + 1 ) .
The main theorem of
[
DD18
]
is:
Theorem 6.4
.
If
a
∈
ℤ
n
𝑎
superscript
ℤ
𝑛
a\in\mathbb{Z}^{n}
italic_a ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
is hereditarily good mod
r
𝑟
r
italic_r
, then for any
t
𝑡
t
italic_t
the lens spaces
L
⁢
(
r
,
t
,
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,a)
italic_L ( italic_r , italic_t , italic_a )
and
L
⁢
(
r
,
t
,
−
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,-a)
italic_L ( italic_r , italic_t , - italic_a )
are isospectral.
Remark 6.5
.
The lens spaces
L
⁢
(
r
,
t
,
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,a)
italic_L ( italic_r , italic_t , italic_a )
and
L
⁢
(
r
,
t
,
−
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,-a)
italic_L ( italic_r , italic_t , - italic_a )
in Theorem
6.4
are actually
p
𝑝
p
italic_p
-isospectral for all
p
𝑝
p
italic_p
.
This means that the Hodge-Laplace operator acting on
p
𝑝
p
italic_p
-forms on each of them has the same spectrum for all
p
=
0
,
…
,
2
⁢
n
−
1
𝑝
0
…
2
𝑛
1
p=0,\dots,2n-1
italic_p = 0 , … , 2 italic_n - 1
.
Proposition
2.3
tells us that
a
𝑎
a
italic_a
is reversible mod
r
𝑟
r
italic_r
precisely when the lens spaces
L
⁢
(
r
,
t
,
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,a)
italic_L ( italic_r , italic_t , italic_a )
and
L
⁢
(
r
,
t
,
−
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,-a)
italic_L ( italic_r , italic_t , - italic_a )
are isometric and hence trivially isospectral. The theorem is thus only interesting in the case that
a
𝑎
a
italic_a
is hereditarily good and irreversible mod
r
𝑟
r
italic_r
. This is what prompted DeFord and Doyle to call such
a
𝑎
a
italic_a
useful
: when
a
𝑎
a
italic_a
is useful mod
r
𝑟
r
italic_r
the lens spaces
L
⁢
(
r
,
t
,
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,a)
italic_L ( italic_r , italic_t , italic_a )
and
L
⁢
(
r
,
t
,
−
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,-a)
italic_L ( italic_r , italic_t , - italic_a )
will be isospectral but not isometric.
Definition 6.6
.
We say that
a
∈
ℤ
n
𝑎
superscript
ℤ
𝑛
a\in\mathbb{Z}^{n}
italic_a ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
is self-reversing mod
r
𝑟
r
italic_r
if
a
𝑎
a
italic_a
and
−
a
𝑎
-a
- italic_a
are equal as multisets mod
r
𝑟
r
italic_r
.
Lemma 6.7
.
Let
n
≥
3
𝑛
3
n\geq 3
italic_n ≥ 3
and
r
>
2
𝑟
2
r>2
italic_r > 2
be coprime positive integers and
a
∈
ℤ
n
𝑎
superscript
ℤ
𝑛
a\in\mathbb{Z}^{n}
italic_a ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
. If
a
𝑎
a
italic_a
is not self-reversing mod
r
𝑟
r
italic_r
and the sum of its entries is divisible by
r
𝑟
r
italic_r
, then
a
𝑎
a
italic_a
is irreversible mod
r
𝑟
r
italic_r
.
Proof.
If
a
𝑎
a
italic_a
is reversible then there exists
c
∈
ℤ
r
𝑐
subscript
ℤ
𝑟
c\in\mathbb{Z}_{r}
italic_c ∈ blackboard_Z start_POSTSUBSCRIPT italic_r end_POSTSUBSCRIPT
such that
a
+
c
𝑎
𝑐
a+c
italic_a + italic_c
and
−
a
𝑎
-a
- italic_a
are equal as multisets mod
r
𝑟
r
italic_r
. In this case for every
i
∈
{
1
,
…
,
m
}
𝑖
1
…
𝑚
i\in\{1,\dots,m\}
italic_i ∈ { 1 , … , italic_m }
there exists
j
∈
{
1
,
…
,
m
}
𝑗
1
…
𝑚
j\in\{1,\dots,m\}
italic_j ∈ { 1 , … , italic_m }
such that
a
i
+
c
≡
−
a
j
(
mod
r
)
.
subscript
𝑎
𝑖
𝑐
annotated
subscript
𝑎
𝑗
pmod
𝑟
a_{i}+c\equiv-a_{j}\pmod{r}.
italic_a start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT + italic_c ≡ - italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_MODIFIER ( roman_mod start_ARG italic_r end_ARG ) end_MODIFIER .
If we sum over all
i
𝑖
i
italic_i
then we get
2
⁢
S
+
n
⁢
c
≡
0
(
mod
r
)
,
2
𝑆
𝑛
𝑐
annotated
0
pmod
𝑟
2S+nc\equiv 0\pmod{r},
2 italic_S + italic_n italic_c ≡ 0 start_MODIFIER ( roman_mod start_ARG italic_r end_ARG ) end_MODIFIER ,
where
S
=
∑
i
=
1
n
a
i
𝑆
superscript
subscript
𝑖
1
𝑛
subscript
𝑎
𝑖
S=\sum_{i=1}^{n}a_{i}
italic_S = ∑ start_POSTSUBSCRIPT italic_i = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT italic_a start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
. By hypothesis
S
≡
0
(
mod
r
)
𝑆
annotated
0
pmod
𝑟
S\equiv 0\pmod{r}
italic_S ≡ 0 start_MODIFIER ( roman_mod start_ARG italic_r end_ARG ) end_MODIFIER
, hence
n
⁢
c
≡
0
(
mod
r
)
𝑛
𝑐
annotated
0
pmod
𝑟
nc\equiv 0\pmod{r}
italic_n italic_c ≡ 0 start_MODIFIER ( roman_mod start_ARG italic_r end_ARG ) end_MODIFIER
. Since
n
𝑛
n
italic_n
is coprime to
r
𝑟
r
italic_r
, it is invertible modulo
r
𝑟
r
italic_r
and consequently we find that
c
≡
0
(
mod
r
)
𝑐
annotated
0
pmod
𝑟
c\equiv 0\pmod{r}
italic_c ≡ 0 start_MODIFIER ( roman_mod start_ARG italic_r end_ARG ) end_MODIFIER
. But this means that
a
𝑎
a
italic_a
is self-reversing mod
r
𝑟
r
italic_r
, a contradiction.
∎
Ikeda’s families of isospectral lens spaces show that there are isospectral lens spaces of arbitrarily high dimension. Although it is well known to experts that there are in fact isospectral lens spaces in every odd dimension at least
5
5
5
5
, this result has not, to our knowledge, ever appeared in the literature. Below we provide a proof.
Proposition 6.8
.
In every odd dimension at least
5
5
5
5
, there are pairs of non-isometric lens spaces that are isospectral (and
p
𝑝
p
italic_p
-isospectral for all
p
𝑝
p
italic_p
).
Proof.
We fix
n
≥
3
𝑛
3
n\geq 3
italic_n ≥ 3
.
Let
r
>
n
2
𝑟
superscript
𝑛
2
r>n^{2}
italic_r > italic_n start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT
be a prime number and observe that
a
=
(
1
,
2
,
…
,
n
−
1
,
r
−
n
⁢
(
n
−
1
)
2
)
𝑎
1
2
…
𝑛
1
𝑟
𝑛
𝑛
1
2
a=\left(1,2,\dots,n-1,r-\frac{n(n-1)}{2}\right)
italic_a = ( 1 , 2 , … , italic_n - 1 , italic_r - divide start_ARG italic_n ( italic_n - 1 ) end_ARG start_ARG 2 end_ARG )
is not self-reversing mod
r
𝑟
r
italic_r
(since
a
1
=
1
subscript
𝑎
1
1
a_{1}=1
italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT = 1
and no entry of
a
𝑎
a
italic_a
is equal to
r
−
1
𝑟
1
r-1
italic_r - 1
) and satisfies that the sum of its entries is
0
0
mod
r
𝑟
r
italic_r
since this sum will in fact be equal to
r
𝑟
r
italic_r
. It follows from Theorem
6.4
that the lens spaces
L
⁢
(
r
,
t
,
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,a)
italic_L ( italic_r , italic_t , italic_a )
and
L
⁢
(
r
,
t
,
−
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,-a)
italic_L ( italic_r , italic_t , - italic_a )
will be isospectral but not isometric for all
t
𝑡
t
italic_t
.
∎
It is interesting to note that when
gcd
⁡
(
n
,
r
)
=
1
𝑛
𝑟
1
\gcd(n,r)=1
roman_gcd ( italic_n , italic_r ) = 1
, all tuples
a
∈
ℤ
n
𝑎
superscript
ℤ
𝑛
a\in\mathbb{Z}^{n}
italic_a ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
which are useful mod
r
𝑟
r
italic_r
yield lens spaces isometric to those produced by tuples whose sum of entries is congruent to
0
0
mod
r
𝑟
r
italic_r
.
Lemma 6.9
.
Let
n
≥
3
𝑛
3
n\geq 3
italic_n ≥ 3
and
r
>
2
𝑟
2
r>2
italic_r > 2
be coprime positive integers and
t
>
1
𝑡
1
t>1
italic_t > 1
be any positive integer. If
a
∈
ℤ
n
𝑎
superscript
ℤ
𝑛
a\in\mathbb{Z}^{n}
italic_a ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
is useful mod
r
𝑟
r
italic_r
then there exists
b
∈
ℤ
n
𝑏
superscript
ℤ
𝑛
b\in\mathbb{Z}^{n}
italic_b ∈ blackboard_Z start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
such that:
(1)
b
𝑏
b
italic_b
is useful mod
r
𝑟
r
italic_r
,
(2)
the sum of the entries of
b
𝑏
b
italic_b
is
0
0
mod
r
𝑟
r
italic_r
, and
(3)
the lens spaces
L
⁢
(
r
,
t
,
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,a)
italic_L ( italic_r , italic_t , italic_a )
and
L
⁢
(
r
,
t
,
b
)
𝐿
𝑟
𝑡
𝑏
L(r,t,b)
italic_L ( italic_r , italic_t , italic_b )
are isometric.
Proof.
Let
c
∈
ℤ
r
𝑐
subscript
ℤ
𝑟
c\in\mathbb{Z}_{r}
italic_c ∈ blackboard_Z start_POSTSUBSCRIPT italic_r end_POSTSUBSCRIPT
. The sum of the entries of
a
+
c
=
(
a
1
+
c
,
…
,
a
n
+
c
)
𝑎
𝑐
subscript
𝑎
1
𝑐
…
subscript
𝑎
𝑛
𝑐
a+c=(a_{1}+c,\dots,a_{n}+c)
italic_a + italic_c = ( italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT + italic_c , … , italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT + italic_c )
is
S
+
n
⁢
c
𝑆
𝑛
𝑐
S+nc
italic_S + italic_n italic_c
where
S
𝑆
S
italic_S
is the sum of the entries of
a
𝑎
a
italic_a
. Because
n
𝑛
n
italic_n
is coprime to
r
𝑟
r
italic_r
, it is invertible modulo
r
𝑟
r
italic_r
. Let
m
∈
ℤ
𝑚
ℤ
m\in\mathbb{Z}
italic_m ∈ blackboard_Z
be such that
m
⁢
n
≡
0
(
mod
r
)
𝑚
𝑛
annotated
0
pmod
𝑟
mn\equiv 0\pmod{r}
italic_m italic_n ≡ 0 start_MODIFIER ( roman_mod start_ARG italic_r end_ARG ) end_MODIFIER
. A straightforward argument now shows that if
c
≡
−
m
⁢
S
(
mod
r
)
𝑐
annotated
𝑚
𝑆
pmod
𝑟
c\equiv-mS\pmod{r}
italic_c ≡ - italic_m italic_S start_MODIFIER ( roman_mod start_ARG italic_r end_ARG ) end_MODIFIER
then the sum of the entries of
a
+
c
𝑎
𝑐
a+c
italic_a + italic_c
will be
0
0
mod
r
𝑟
r
italic_r
. Defining
b
=
a
+
c
𝑏
𝑎
𝑐
b=a+c
italic_b = italic_a + italic_c
we see that (2) and (3) are trivially satisfied. To prove (1), note that Lemma
6.7
shows that
b
𝑏
b
italic_b
is irreversible, while
b
𝑏
b
italic_b
is hereditarily good mod
r
𝑟
r
italic_r
since
a
𝑎
a
italic_a
is hereditarily good mod
r
𝑟
r
italic_r
and
b
=
a
+
c
𝑏
𝑎
𝑐
b=a+c
italic_b = italic_a + italic_c
.
∎
Theorem 6.10
.
Let
n
≥
3
𝑛
3
n\geq 3
italic_n ≥ 3
. There exist infinitely many pairs of descending isospectral towers of lens spaces in dimension
2
⁢
n
−
1
2
𝑛
1
2n-1
2 italic_n - 1
.
Proof.
We begin with the example from the proof of Proposition
6.8
:
a
=
(
1
,
2
,
…
,
n
−
1
,
r
−
n
⁢
(
n
−
1
)
2
)
,
𝑎
1
2
…
𝑛
1
𝑟
𝑛
𝑛
1
2
a=\left(1,2,\dots,n-1,r-\frac{n(n-1)}{2}\right),
italic_a = ( 1 , 2 , … , italic_n - 1 , italic_r - divide start_ARG italic_n ( italic_n - 1 ) end_ARG start_ARG 2 end_ARG ) ,
where
r
𝑟
r
italic_r
is a fixed prime greater than
n
2
superscript
𝑛
2
n^{2}
italic_n start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT
. As was mentioned earlier, for any
t
𝑡
t
italic_t
the lens spaces
L
⁢
(
r
,
t
,
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,a)
italic_L ( italic_r , italic_t , italic_a )
and
L
⁢
(
r
,
t
,
−
a
)
𝐿
𝑟
𝑡
𝑎
L(r,t,-a)
italic_L ( italic_r , italic_t , - italic_a )
are isospectral but not isometric. Let
k
𝑘
k
italic_k
be any positive integer greater than
1
1
1
1
satisfying
k
≡
1
(
mod
r
)
𝑘
annotated
1
pmod
𝑟
k\equiv 1\pmod{r}
italic_k ≡ 1 start_MODIFIER ( roman_mod start_ARG italic_r end_ARG ) end_MODIFIER
and define
t
j
=
t
⁢
k
j
subscript
𝑡
𝑗
𝑡
superscript
𝑘
𝑗
t_{j}=tk^{j}
italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT = italic_t italic_k start_POSTSUPERSCRIPT italic_j end_POSTSUPERSCRIPT
. Thus
L
⁢
(
r
,
t
j
,
a
)
𝐿
𝑟
subscript
𝑡
𝑗
𝑎
L(r,t_{j},a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT , italic_a )
and
L
⁢
(
r
,
t
j
,
−
a
)
𝐿
𝑟
subscript
𝑡
𝑗
𝑎
L(r,t_{j},-a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT , - italic_a )
are isospectral and not isometric for all
j
≥
0
𝑗
0
j\geq 0
italic_j ≥ 0
.
Claim
.
For any
i
>
j
≥
0
𝑖
𝑗
0
i>j\geq 0
italic_i > italic_j ≥ 0
the lens spaces
L
⁢
(
r
2
⁢
t
j
;
r
⁢
t
i
⁢
a
1
+
1
,
…
,
r
⁢
t
i
⁢
a
n
+
1
)
𝐿
superscript
𝑟
2
subscript
𝑡
𝑗
𝑟
subscript
𝑡
𝑖
subscript
𝑎
1
1
…
𝑟
subscript
𝑡
𝑖
subscript
𝑎
𝑛
1
L(r^{2}t_{j};rt_{i}a_{1}+1,\dots,rt_{i}a_{n}+1)
italic_L ( italic_r start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ; italic_r italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT + 1 , … , italic_r italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT + 1 )
and
L
⁢
(
r
,
t
j
,
a
)
𝐿
𝑟
subscript
𝑡
𝑗
𝑎
L(r,t_{j},a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT , italic_a )
are isometric.
Proof.
This follows from Proposition
2.3
since
r
⁢
t
i
⁢
a
s
+
1
≡
r
⁢
t
j
⁢
a
s
+
1
(
mod
r
2
⁢
t
j
)
𝑟
subscript
𝑡
𝑖
subscript
𝑎
𝑠
1
annotated
𝑟
subscript
𝑡
𝑗
subscript
𝑎
𝑠
1
pmod
superscript
𝑟
2
subscript
𝑡
𝑗
rt_{i}a_{s}+1\equiv rt_{j}a_{s}+1\pmod{r^{2}t_{j}}
italic_r italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT + 1 ≡ italic_r italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT + 1 start_MODIFIER ( roman_mod start_ARG italic_r start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT end_ARG ) end_MODIFIER
for
s
=
1
,
…
,
n
𝑠
1
…
𝑛
s=1,\dots,n
italic_s = 1 , … , italic_n
, which in turn follows from the fact that
k
≡
1
(
mod
r
)
𝑘
annotated
1
pmod
𝑟
k\equiv 1\pmod{r}
italic_k ≡ 1 start_MODIFIER ( roman_mod start_ARG italic_r end_ARG ) end_MODIFIER
, as we now show. That
k
≡
1
(
mod
r
)
𝑘
annotated
1
pmod
𝑟
k\equiv 1\pmod{r}
italic_k ≡ 1 start_MODIFIER ( roman_mod start_ARG italic_r end_ARG ) end_MODIFIER
and
i
>
j
𝑖
𝑗
i>j
italic_i > italic_j
implies
k
i
−
j
−
1
superscript
𝑘
𝑖
𝑗
1
k^{i-j}-1
italic_k start_POSTSUPERSCRIPT italic_i - italic_j end_POSTSUPERSCRIPT - 1
is divisible by
r
𝑟
r
italic_r
. Thus there is an integer
m
𝑚
m
italic_m
such that
k
i
−
j
−
1
=
r
⁢
m
superscript
𝑘
𝑖
𝑗
1
𝑟
𝑚
k^{i-j}-1=rm
italic_k start_POSTSUPERSCRIPT italic_i - italic_j end_POSTSUPERSCRIPT - 1 = italic_r italic_m
. Then
(
r
⁢
t
i
⁢
a
s
+
1
)
−
(
r
⁢
t
j
⁢
a
s
+
1
)
𝑟
subscript
𝑡
𝑖
subscript
𝑎
𝑠
1
𝑟
subscript
𝑡
𝑗
subscript
𝑎
𝑠
1
\displaystyle(rt_{i}a_{s}+1)-(rt_{j}a_{s}+1)
( italic_r italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT + 1 ) - ( italic_r italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT + 1 )
=
r
⁢
t
⁢
k
j
⁢
a
s
⁢
(
k
i
−
j
−
1
)
=
r
2
⁢
t
j
⁢
a
s
⁢
m
.
absent
𝑟
𝑡
superscript
𝑘
𝑗
subscript
𝑎
𝑠
superscript
𝑘
𝑖
𝑗
1
superscript
𝑟
2
subscript
𝑡
𝑗
subscript
𝑎
𝑠
𝑚
\displaystyle=rtk^{j}a_{s}(k^{i-j}-1)=r^{2}t_{j}a_{s}m.
= italic_r italic_t italic_k start_POSTSUPERSCRIPT italic_j end_POSTSUPERSCRIPT italic_a start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT ( italic_k start_POSTSUPERSCRIPT italic_i - italic_j end_POSTSUPERSCRIPT - 1 ) = italic_r start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT italic_m .
In particular
r
2
⁢
t
j
superscript
𝑟
2
subscript
𝑡
𝑗
r^{2}t_{j}
italic_r start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT
divides
(
r
⁢
t
i
⁢
a
s
+
1
)
−
(
r
⁢
t
j
⁢
a
s
+
1
)
𝑟
subscript
𝑡
𝑖
subscript
𝑎
𝑠
1
𝑟
subscript
𝑡
𝑗
subscript
𝑎
𝑠
1
(rt_{i}a_{s}+1)-(rt_{j}a_{s}+1)
( italic_r italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT + 1 ) - ( italic_r italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT + 1 )
and
r
⁢
t
i
⁢
a
s
+
1
≡
r
⁢
t
j
⁢
a
s
+
1
(
mod
r
2
⁢
t
j
)
𝑟
subscript
𝑡
𝑖
subscript
𝑎
𝑠
1
annotated
𝑟
subscript
𝑡
𝑗
subscript
𝑎
𝑠
1
pmod
superscript
𝑟
2
subscript
𝑡
𝑗
rt_{i}a_{s}+1\equiv rt_{j}a_{s}+1\pmod{r^{2}t_{j}}
italic_r italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT + 1 ≡ italic_r italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT + 1 start_MODIFIER ( roman_mod start_ARG italic_r start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT italic_t start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT end_ARG ) end_MODIFIER
as claimed.
∎
We now define our towers inductively. Let
M
0
=
L
⁢
(
r
,
t
0
,
a
)
subscript
𝑀
0
𝐿
𝑟
subscript
𝑡
0
𝑎
M_{0}=L(r,t_{0},a)
italic_M start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = italic_L ( italic_r , italic_t start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT , italic_a )
and
N
0
=
L
⁢
(
r
,
t
0
,
−
a
)
subscript
𝑁
0
𝐿
𝑟
subscript
𝑡
0
𝑎
N_{0}=L(r,t_{0},-a)
italic_N start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT = italic_L ( italic_r , italic_t start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT , - italic_a )
. We have already seen that
M
0
subscript
𝑀
0
M_{0}
italic_M start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
and
N
0
subscript
𝑁
0
N_{0}
italic_N start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
are isospectral and not isometric. To construct
M
1
subscript
𝑀
1
M_{1}
italic_M start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
N
1
subscript
𝑁
1
N_{1}
italic_N start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
, we note that the claim shows that
L
⁢
(
r
2
⁢
t
0
;
r
⁢
t
1
⁢
a
1
+
1
,
…
,
r
⁢
t
1
⁢
a
n
+
1
)
𝐿
superscript
𝑟
2
subscript
𝑡
0
𝑟
subscript
𝑡
1
subscript
𝑎
1
1
…
𝑟
subscript
𝑡
1
subscript
𝑎
𝑛
1
L(r^{2}t_{0};rt_{1}a_{1}+1,\dots,rt_{1}a_{n}+1)
italic_L ( italic_r start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT italic_t start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ; italic_r italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT + 1 , … , italic_r italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT + 1 )
and
L
⁢
(
r
,
t
0
,
a
)
𝐿
𝑟
subscript
𝑡
0
𝑎
L(r,t_{0},a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT , italic_a )
are isometric. Since the former is a finite degree cover of
L
⁢
(
r
,
t
1
,
a
)
𝐿
𝑟
subscript
𝑡
1
𝑎
L(r,t_{1},a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_a )
, there is some lens space
M
1
subscript
𝑀
1
M_{1}
italic_M start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
isometric to
L
⁢
(
r
,
t
1
,
a
)
𝐿
𝑟
subscript
𝑡
1
𝑎
L(r,t_{1},a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_a )
having
L
⁢
(
r
,
t
0
,
a
)
𝐿
𝑟
subscript
𝑡
0
𝑎
L(r,t_{0},a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT , italic_a )
as a finite degree cover. Similarly, we obtain a lens space
N
1
subscript
𝑁
1
N_{1}
italic_N start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
isometric to
L
⁢
(
r
,
t
1
,
−
a
)
𝐿
𝑟
subscript
𝑡
1
𝑎
L(r,t_{1},-a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , - italic_a )
having
L
⁢
(
r
,
t
1
,
−
a
)
𝐿
𝑟
subscript
𝑡
1
𝑎
L(r,t_{1},-a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , - italic_a )
as a finite degree cover. Since isometric manifolds are trivially isospectral, the isospectrality of
M
1
subscript
𝑀
1
M_{1}
italic_M start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
N
1
subscript
𝑁
1
N_{1}
italic_N start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
follows from the isospectrality of
L
⁢
(
r
,
t
1
,
a
)
𝐿
𝑟
subscript
𝑡
1
𝑎
L(r,t_{1},a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_a )
and
L
⁢
(
r
,
t
1
,
−
a
)
𝐿
𝑟
subscript
𝑡
1
𝑎
L(r,t_{1},-a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , - italic_a )
.
Suppose now that we have constructed
M
i
−
1
subscript
𝑀
𝑖
1
M_{i-1}
italic_M start_POSTSUBSCRIPT italic_i - 1 end_POSTSUBSCRIPT
and
N
i
−
1
subscript
𝑁
𝑖
1
N_{i-1}
italic_N start_POSTSUBSCRIPT italic_i - 1 end_POSTSUBSCRIPT
, and note that by construction these lens spaces will be isometric to
L
⁢
(
r
,
t
i
−
1
,
a
)
𝐿
𝑟
subscript
𝑡
𝑖
1
𝑎
L(r,t_{i-1},a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT italic_i - 1 end_POSTSUBSCRIPT , italic_a )
and
L
⁢
(
r
,
t
i
−
1
,
−
a
)
𝐿
𝑟
subscript
𝑡
𝑖
1
𝑎
L(r,t_{i-1},-a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT italic_i - 1 end_POSTSUBSCRIPT , - italic_a )
. By the claim, the lens space
L
⁢
(
r
2
⁢
t
i
−
1
;
r
⁢
t
i
⁢
a
1
+
1
,
…
,
r
⁢
t
i
⁢
a
n
+
1
)
𝐿
superscript
𝑟
2
subscript
𝑡
𝑖
1
𝑟
subscript
𝑡
𝑖
subscript
𝑎
1
1
…
𝑟
subscript
𝑡
𝑖
subscript
𝑎
𝑛
1
L(r^{2}t_{i-1};rt_{i}a_{1}+1,\dots,rt_{i}a_{n}+1)
italic_L ( italic_r start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT italic_t start_POSTSUBSCRIPT italic_i - 1 end_POSTSUBSCRIPT ; italic_r italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT + 1 , … , italic_r italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT italic_a start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT + 1 )
is isometric to
L
⁢
(
r
,
t
i
,
a
)
𝐿
𝑟
subscript
𝑡
𝑖
𝑎
L(r,t_{i},a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT , italic_a )
and hence to
M
i
−
1
subscript
𝑀
𝑖
1
M_{i-1}
italic_M start_POSTSUBSCRIPT italic_i - 1 end_POSTSUBSCRIPT
as well. Therefore there is a lens space
M
i
subscript
𝑀
𝑖
M_{i}
italic_M start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
isometric to
L
⁢
(
r
,
t
i
,
a
)
𝐿
𝑟
subscript
𝑡
𝑖
𝑎
L(r,t_{i},a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT , italic_a )
having
M
i
−
1
subscript
𝑀
𝑖
1
M_{i-1}
italic_M start_POSTSUBSCRIPT italic_i - 1 end_POSTSUBSCRIPT
as a finite degree cover. We similarly obtain a lens space
N
i
subscript
𝑁
𝑖
N_{i}
italic_N start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
isometric to
L
⁢
(
r
,
t
i
,
−
a
)
𝐿
𝑟
subscript
𝑡
𝑖
𝑎
L(r,t_{i},-a)
italic_L ( italic_r , italic_t start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT , - italic_a )
having
N
i
−
1
subscript
𝑁
𝑖
1
N_{i-1}
italic_N start_POSTSUBSCRIPT italic_i - 1 end_POSTSUBSCRIPT
as a finite degree cover. As above,
M
i
subscript
𝑀
𝑖
M_{i}
italic_M start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
and
N
i
subscript
𝑁
𝑖
N_{i}
italic_N start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
are isospectral but not isometric. Continuing in this manner yields the desired pair of descending isospectral towers
{
M
i
}
subscript
𝑀
𝑖
\{M_{i}\}
{ italic_M start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT }
and
{
N
i
}
subscript
𝑁
𝑖
\{N_{i}\}
{ italic_N start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT }
.
It remains only to show that there are infinitely many such pairs of descending towers. This follows immediately from the fact that the above construction holds for any positive integer
t
𝑡
t
italic_t
. We can therefore obtain infinitely many towers by allowing
t
𝑡
t
italic_t
to range over the set of prime numbers not equal to
r
𝑟
r
italic_r
and not dividing
k
𝑘
k
italic_k
.
∎
7.
Isospectrality between quotients of symmetric spaces
In this section we discuss Question
1.15
, which asks for the determination of the compact simply connected irreducible symmetric spaces that cover isospectral and non-isometric manifolds.
Henceforth we will omit the fact that the isospectral covered manifolds are non-isometric, for the sake of conciseness.
Unlike the non-compact type setting, the structure of locally symmetric spaces of compact type is quite rigid.
In particular, the classification of manifolds covered by spheres, the so called spherical space forms, was a long process finished by Wolf in
[
Wo
]
.
Wolf also classified in
[
Wo
, Ch. 9]
the manifolds covered by compact symmetric spaces
G
/
K
𝐺
𝐾
G/K
italic_G / italic_K
satisfying
rank
⁡
(
G
)
−
rank
⁡
(
K
)
≤
1
rank
𝐺
rank
𝐾
1
\operatorname{rank}(G)-\operatorname{rank}(K)\leq 1
roman_rank ( italic_G ) - roman_rank ( italic_K ) ≤ 1
.
We will use his results throughout the section.
We now start discussing partial answers of Question
1.15
, starting from the simplest case.
There are many compact irreducible symmetric spaces that cannot cover isospectral pairs because they do not cover any manifold at all.
For instance, this is the case for
even dimensional real projective spaces
P
2
⁢
n
⁢
(
ℝ
)
=
SO
⁡
(
2
⁢
n
+
1
)
O
⁡
(
2
⁢
n
)
superscript
𝑃
2
𝑛
ℝ
SO
2
𝑛
1
O
2
𝑛
P^{2n}(\mathbb{R})=\frac{\operatorname{SO}(2n+1)}{\operatorname{O}(2n)}
italic_P start_POSTSUPERSCRIPT 2 italic_n end_POSTSUPERSCRIPT ( blackboard_R ) = divide start_ARG roman_SO ( 2 italic_n + 1 ) end_ARG start_ARG roman_O ( 2 italic_n ) end_ARG
,
quaternionic Grassmannian spaces
Sp
⁡
(
m
+
n
)
Sp
⁡
(
m
)
×
Sp
⁡
(
n
)
Sp
𝑚
𝑛
Sp
𝑚
Sp
𝑛
\frac{\operatorname{Sp}(m+n)}{\operatorname{Sp}(m)\times\operatorname{Sp}(n)}
divide start_ARG roman_Sp ( italic_m + italic_n ) end_ARG start_ARG roman_Sp ( italic_m ) × roman_Sp ( italic_n ) end_ARG
for
m
>
n
≥
1
𝑚
𝑛
1
m>n\geq 1
italic_m > italic_n ≥ 1
,
complex Grassmannian spaces
SU
⁡
(
m
+
n
)
S
⁡
(
U
⁡
(
m
)
×
U
⁡
(
n
)
)
SU
𝑚
𝑛
S
U
𝑚
U
𝑛
\frac{\operatorname{SU}(m+n)}{\operatorname{S}(\operatorname{U}(m)\times%
\operatorname{U}(n))}
divide start_ARG roman_SU ( italic_m + italic_n ) end_ARG start_ARG roman_S ( roman_U ( italic_m ) × roman_U ( italic_n ) ) end_ARG
for
m
>
n
≥
1
𝑚
𝑛
1
m>n\geq 1
italic_m > italic_n ≥ 1
with
m
⁢
n
𝑚
𝑛
mn
italic_m italic_n
even,
E
6
SU
⁡
(
6
)
⋅
SU
⁡
(
2
)
subscript
E
6
⋅
SU
6
SU
2
\frac{\textup{E}_{6}}{\operatorname{SU}(6)\cdot\operatorname{SU}(2)}
divide start_ARG E start_POSTSUBSCRIPT 6 end_POSTSUBSCRIPT end_ARG start_ARG roman_SU ( 6 ) ⋅ roman_SU ( 2 ) end_ARG
,
and
E
6
SO
⁡
(
10
)
⋅
SO
⁡
(
2
)
subscript
E
6
⋅
SO
10
SO
2
\frac{\textup{E}_{6}}{\operatorname{SO}(10)\cdot\operatorname{SO}(2)}
divide start_ARG E start_POSTSUBSCRIPT 6 end_POSTSUBSCRIPT end_ARG start_ARG roman_SO ( 10 ) ⋅ roman_SO ( 2 ) end_ARG
Similarly, the real Grassmannian spaces
SO
⁡
(
m
+
n
)
SO
⁡
(
m
)
×
SO
⁡
(
n
)
SO
𝑚
𝑛
SO
𝑚
SO
𝑛
\frac{\operatorname{SO}(m+n)}{\operatorname{SO}(m)\times\operatorname{SO}(n)}
divide start_ARG roman_SO ( italic_m + italic_n ) end_ARG start_ARG roman_SO ( italic_m ) × roman_SO ( italic_n ) end_ARG
with
m
+
n
𝑚
𝑛
m+n
italic_m + italic_n
odd, cover properly exactly one manifold with fundamental group of order
2
2
2
2
, hence these spaces do not cover isospectral manifolds.
The best known instance are the even dimensional spheres
S
2
⁢
n
=
SO
⁡
(
2
⁢
n
+
1
)
SO
⁡
(
2
⁢
n
)
superscript
𝑆
2
𝑛
SO
2
𝑛
1
SO
2
𝑛
S^{2n}=\frac{\operatorname{SO}(2n+1)}{\operatorname{SO}(2n)}
italic_S start_POSTSUPERSCRIPT 2 italic_n end_POSTSUPERSCRIPT = divide start_ARG roman_SO ( 2 italic_n + 1 ) end_ARG start_ARG roman_SO ( 2 italic_n ) end_ARG
which only cover properly
P
2
⁢
n
⁢
(
ℝ
)
superscript
𝑃
2
𝑛
ℝ
P^{2n}(\mathbb{R})
italic_P start_POSTSUPERSCRIPT 2 italic_n end_POSTSUPERSCRIPT ( blackboard_R )
.
Even dimensional Grassmannian spaces cover only finitely many manifolds.
On the opposite side, odd dimensional Grassmannian spaces (i.e.
SO
⁡
(
m
+
n
)
SO
⁡
(
m
)
×
SO
⁡
(
n
)
SO
𝑚
𝑛
SO
𝑚
SO
𝑛
\frac{\operatorname{SO}(m+n)}{\operatorname{SO}(m)\times\operatorname{SO}(n)}
divide start_ARG roman_SO ( italic_m + italic_n ) end_ARG start_ARG roman_SO ( italic_m ) × roman_SO ( italic_n ) end_ARG
with
m
⁢
n
𝑚
𝑛
mn
italic_m italic_n
odd) cover infinitely many manifolds.
Ikeda is the main contributor to Question
1.15
for these spaces.
We summarize his results
[
Ik80
, Thm. II]
,
[
Ik83
, Thm. 4]
, and
[
Ik97
, Thm. 7]
, in the following statement.
Theorem 7.1
(Ikeda)
.
Odd-dimensional spheres of dimension
≥
5
absent
5
\geq 5
≥ 5
and real Grassmannian spaces
SO
⁡
(
m
+
n
)
SO
⁡
(
m
)
×
SO
⁡
(
n
)
SO
𝑚
𝑛
SO
𝑚
SO
𝑛
\frac{\operatorname{SO}(m+n)}{\operatorname{SO}(m)\times\operatorname{SO}(n)}
divide start_ARG roman_SO ( italic_m + italic_n ) end_ARG start_ARG roman_SO ( italic_m ) × roman_SO ( italic_n ) end_ARG
with
n
≥
m
>
1
𝑛
𝑚
1
n\geq m>1
italic_n ≥ italic_m > 1
satisfying
m
⁢
n
≡
1
(
mod
2
)
𝑚
𝑛
annotated
1
𝑝𝑚𝑜𝑑
2
mn\equiv 1\pmod{2}
italic_m italic_n ≡ 1 start_MODIFIER ( roman_mod start_ARG 2 end_ARG ) end_MODIFIER
and
m
+
n
∈
{
2
⁢
k
:
k
=
5
⁢
or
⁢
k
≥
7
}
𝑚
𝑛
conditional-set
2
𝑘
𝑘
5
or
𝑘
7
m+n\in\{2k:k=5\text{ or }k\geq 7\}
italic_m + italic_n ∈ { 2 italic_k : italic_k = 5 or italic_k ≥ 7 }
, cover infinitely many isospectral and non-isometric pairs of manifolds.
Furthermore, the
3
3
3
3
-dimensional sphere does not cover any pair of isospectral and non-isometric manifolds.
Wolf
[
Wo01
]
extended Ikeda’s isospectral constructions by adopting a much more general perspective.
Remark 7.2
.
Ikeda proved the existence of infinitely many pairs of (non-cyclic) almost conjugate but not conjugate subgroups of
SO
⁡
(
2
⁢
d
)
SO
2
𝑑
\operatorname{SO}(2d)
roman_SO ( 2 italic_d )
for
d
=
5
𝑑
5
d=5
italic_d = 5
or
d
≥
7
𝑑
7
d\geq 7
italic_d ≥ 7
acting freely on
S
2
⁢
d
−
1
=
SO
⁡
(
2
⁢
d
)
SO
⁡
(
2
⁢
d
−
1
)
superscript
𝑆
2
𝑑
1
SO
2
𝑑
SO
2
𝑑
1
S^{2d-1}=\frac{\operatorname{SO}(2d)}{\operatorname{SO}(2d-1)}
italic_S start_POSTSUPERSCRIPT 2 italic_d - 1 end_POSTSUPERSCRIPT = divide start_ARG roman_SO ( 2 italic_d ) end_ARG start_ARG roman_SO ( 2 italic_d - 1 ) end_ARG
and
SO
⁡
(
2
⁢
d
)
SO
⁡
(
m
)
×
SO
⁡
(
2
⁢
d
−
m
)
SO
2
𝑑
SO
𝑚
SO
2
𝑑
𝑚
\frac{\operatorname{SO}(2d)}{\operatorname{SO}(m)\times\operatorname{SO}(2d-m)}
divide start_ARG roman_SO ( 2 italic_d ) end_ARG start_ARG roman_SO ( italic_m ) × roman_SO ( 2 italic_d - italic_m ) end_ARG
for any
m
𝑚
m
italic_m
odd.
This proves Theorem
7.1
for all cases excepting
S
5
superscript
𝑆
5
S^{5}
italic_S start_POSTSUPERSCRIPT 5 end_POSTSUPERSCRIPT
,
S
7
superscript
𝑆
7
S^{7}
italic_S start_POSTSUPERSCRIPT 7 end_POSTSUPERSCRIPT
, and
S
11
superscript
𝑆
11
S^{11}
italic_S start_POSTSUPERSCRIPT 11 end_POSTSUPERSCRIPT
, where he proved the existence of
finitely many
isospectral lens spaces covered by each of them.
The existence of infinitely many pairs of isospectral lens spaces of dimension
5
5
5
5
,
7
7
7
7
, and
11
11
11
11
follows from
[
DD18
]
(see also Section
6
).
Remark 7.3
.
Even dimensional Grassmannian spaces (i.e.
SO
⁡
(
m
+
n
)
SO
⁡
(
m
)
×
SO
⁡
(
n
)
SO
𝑚
𝑛
SO
𝑚
SO
𝑛
\frac{\operatorname{SO}(m+n)}{\operatorname{SO}(m)\times\operatorname{SO}(n)}
divide start_ARG roman_SO ( italic_m + italic_n ) end_ARG start_ARG roman_SO ( italic_m ) × roman_SO ( italic_n ) end_ARG
with
m
⁢
n
𝑚
𝑛
mn
italic_m italic_n
even and all complex and quaternionic Grassmannian spaces) cover finitely many manifolds; see
[
Wo
, §9.3]
for the classification.
Spectrally distinguishing them may a feasible but tedious achievement.
A similar situation should occur with
SO
⁡
(
2
⁢
n
)
U
⁡
(
n
)
SO
2
𝑛
U
𝑛
\frac{\operatorname{SO}(2n)}{\operatorname{U}(n)}
divide start_ARG roman_SO ( 2 italic_n ) end_ARG start_ARG roman_U ( italic_n ) end_ARG
,
Sp
⁡
(
n
)
U
⁡
(
n
)
Sp
𝑛
U
𝑛
\frac{\operatorname{Sp}(n)}{\operatorname{U}(n)}
divide start_ARG roman_Sp ( italic_n ) end_ARG start_ARG roman_U ( italic_n ) end_ARG
,
E
7
(
SU
⁡
(
8
)
/
{
±
I
}
)
subscript
E
7
SU
8
plus-or-minus
𝐼
\frac{\operatorname{E}_{7}}{(\operatorname{SU}(8)/\{\pm I\})}
divide start_ARG roman_E start_POSTSUBSCRIPT 7 end_POSTSUBSCRIPT end_ARG start_ARG ( roman_SU ( 8 ) / { ± italic_I } ) end_ARG
,
E
7
E
6
⋅
T
1
subscript
E
7
⋅
subscript
E
6
superscript
T
1
\frac{\operatorname{E}_{7}}{\operatorname{E}_{6}\cdot\operatorname{T}^{1}}
divide start_ARG roman_E start_POSTSUBSCRIPT 7 end_POSTSUBSCRIPT end_ARG start_ARG roman_E start_POSTSUBSCRIPT 6 end_POSTSUBSCRIPT ⋅ roman_T start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT end_ARG
(see
[
Wo
, §9.4]
).
A more challenging problem is to decide whether the symmetric space
SU
⁡
(
3
)
/
SO
⁡
(
3
)
SU
3
SO
3
\operatorname{SU}(3)/\operatorname{SO}(3)
roman_SU ( 3 ) / roman_SO ( 3 )
covers isospectral manifolds.
Its corresponding locally symmetric spaces were classified by Wolf
[
Wo
, Lem. 9.6.3]
and turn out to be infinitely many manifolds with cyclic fundamental groups.
The existence of isospectral covered manifolds is more feasible for compact irreducible symmetric spaces of
group type
.
These are of the form
K
×
K
diag
⁡
(
K
)
𝐾
𝐾
diag
𝐾
\frac{K\times K}{\operatorname{diag}(K)}
divide start_ARG italic_K × italic_K end_ARG start_ARG roman_diag ( italic_K ) end_ARG
, where
K
𝐾
K
italic_K
is a compact simple Lie group and
diag
⁡
(
K
)
=
{
(
k
,
k
)
∈
K
×
K
:
k
∈
K
}
diag
𝐾
conditional-set
𝑘
𝑘
𝐾
𝐾
𝑘
𝐾
\operatorname{diag}(K)=\{(k,k)\in K\times K:k\in K\}
roman_diag ( italic_K ) = { ( italic_k , italic_k ) ∈ italic_K × italic_K : italic_k ∈ italic_K }
.
We will abbreviate
K
×
K
K
=
K
×
K
diag
⁡
(
K
)
𝐾
𝐾
𝐾
𝐾
𝐾
diag
𝐾
\frac{K\times K}{K}=\frac{K\times K}{\operatorname{diag}(K)}
divide start_ARG italic_K × italic_K end_ARG start_ARG italic_K end_ARG = divide start_ARG italic_K × italic_K end_ARG start_ARG roman_diag ( italic_K ) end_ARG
.
Alternatively,
K
×
K
K
𝐾
𝐾
𝐾
\frac{K\times K}{K}
divide start_ARG italic_K × italic_K end_ARG start_ARG italic_K end_ARG
is isometric to
K
𝐾
K
italic_K
endowed with a bi-invariant metric.
The following consequence of Sunada’s method provides many examples.
Proposition 7.4
.
Let
K
𝐾
K
italic_K
be a compact connected simple Lie group and let
g
0
subscript
𝑔
0
g_{0}
italic_g start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
denote any bi-invariant metric on
K
𝐾
K
italic_K
(which is unique up to a positive multiple).
If
Γ
1
subscript
Γ
1
\Gamma_{1}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
Γ
2
subscript
Γ
2
\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are almost conjugate but non-conjugate finite subgroups of
K
𝐾
K
italic_K
, then
(
K
/
Γ
1
,
g
1
)
𝐾
subscript
Γ
1
subscript
𝑔
1
(K/\Gamma_{1},g_{1})
( italic_K / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_g start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT )
and
(
K
/
Γ
,
g
2
)
𝐾
Γ
subscript
𝑔
2
(K/\Gamma,g_{2})
( italic_K / roman_Γ , italic_g start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT )
are isospectral and non-isometric, where
g
i
subscript
𝑔
𝑖
g_{i}
italic_g start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
denotes the Riemannian metric on
K
/
Γ
1
𝐾
subscript
Γ
1
K/\Gamma_{1}
italic_K / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
induced by
g
0
subscript
𝑔
0
g_{0}
italic_g start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT
(i.e.
(
K
,
g
0
)
→
(
K
/
Γ
i
,
g
i
)
→
𝐾
subscript
𝑔
0
𝐾
subscript
Γ
𝑖
subscript
𝑔
𝑖
(K,g_{0})\to(K/\Gamma_{i},g_{i})
( italic_K , italic_g start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ) → ( italic_K / roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT , italic_g start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT )
is a Riemannian cover).
For a proof, see
[
Wo01
, Prop. 2.10]
and take into account that
Γ
i
subscript
Γ
𝑖
\Gamma_{i}
roman_Γ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
acts freely on
K
𝐾
K
italic_K
.
Proof of Theorem
1.16
.
By Proposition
7.4
, it is sufficient to show the existence of almost conjugate and non-conjugate subgroups in any simply connected compact simple Lie group
K
𝐾
K
italic_K
non-isomorphic to
SU
⁡
(
2
)
SU
2
\operatorname{SU}(2)
roman_SU ( 2 )
,
SU
⁡
(
3
)
SU
3
\operatorname{SU}(3)
roman_SU ( 3 )
,
Sp
⁡
(
2
)
Sp
2
\operatorname{Sp}(2)
roman_Sp ( 2 )
or
G
2
subscript
G
2
\textrm{G}_{2}
G start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
.
The pair
Γ
1
,
Γ
2
⊂
SO
⁡
(
6
)
subscript
Γ
1
subscript
Γ
2
SO
6
\Gamma_{1},\Gamma_{2}\subset\operatorname{SO}(6)
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ⊂ roman_SO ( 6 )
from (
LABEL:eq:almostconjugate-in-SO(6)
) gives almost conjugate and non-conjugate subgroups of the universal cover
Spin
⁡
(
6
)
≃
SU
⁡
(
4
)
similar-to-or-equals
Spin
6
SU
4
\operatorname{Spin}(6)\simeq\operatorname{SU}(4)
roman_Spin ( 6 ) ≃ roman_SU ( 4 )
of
SO
⁡
(
6
)
SO
6
\operatorname{SO}(6)
roman_SO ( 6 )
.
For any
n
≥
7
𝑛
7
n\geq 7
italic_n ≥ 7
, the image of
Γ
1
,
Γ
2
subscript
Γ
1
subscript
Γ
2
\Gamma_{1},\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
under the canonical embedding
Spin
⁡
(
6
)
↪
Spin
⁡
(
n
)
↪
Spin
6
Spin
𝑛
\operatorname{Spin}(6)\hookrightarrow\operatorname{Spin}(n)
roman_Spin ( 6 ) ↪ roman_Spin ( italic_n )
are still almost conjugate and non-conjugate in
Spin
⁡
(
n
)
Spin
𝑛
\operatorname{Spin}(n)
roman_Spin ( italic_n )
.
The same occurs for the well-known embeddings
(7.1)
SU
⁡
(
4
)
SU
4
\displaystyle\operatorname{SU}(4)
roman_SU ( 4 )
↪
SU
⁡
(
n
)
for all
⁢
n
≥
5
,
formulae-sequence
↪
absent
SU
𝑛
for all
𝑛
5
\displaystyle\hookrightarrow\operatorname{SU}(n)\quad\text{for all }n\geq 5,
↪ roman_SU ( italic_n ) for all italic_n ≥ 5 ,
SU
⁡
(
4
)
SU
4
\displaystyle\operatorname{SU}(4)
roman_SU ( 4 )
↪
U
⁡
(
4
)
↪
Sp
⁡
(
n
)
for all
⁢
n
≥
4
,
formulae-sequence
↪
absent
U
4
↪
Sp
𝑛
for all
𝑛
4
\displaystyle\hookrightarrow\operatorname{U}(4)\hookrightarrow\operatorname{Sp%
}(n)\quad\text{for all }n\geq 4,
↪ roman_U ( 4 ) ↪ roman_Sp ( italic_n ) for all italic_n ≥ 4 ,
SO
⁡
(
6
)
SO
6
\displaystyle\operatorname{SO}(6)
roman_SO ( 6 )
↪
SO
⁡
(
10
)
↪
E
6
↪
E
7
↪
E
8
,
↪
absent
SO
10
↪
subscript
E
6
↪
subscript
E
7
↪
subscript
E
8
\displaystyle\hookrightarrow\operatorname{SO}(10)\hookrightarrow\operatorname{%
E}_{6}\hookrightarrow\operatorname{E}_{7}\hookrightarrow\operatorname{E}_{8},
↪ roman_SO ( 10 ) ↪ roman_E start_POSTSUBSCRIPT 6 end_POSTSUBSCRIPT ↪ roman_E start_POSTSUBSCRIPT 7 end_POSTSUBSCRIPT ↪ roman_E start_POSTSUBSCRIPT 8 end_POSTSUBSCRIPT ,
Spin
⁡
(
6
)
Spin
6
\displaystyle\operatorname{Spin}(6)
roman_Spin ( 6 )
↪
Spin
⁡
(
9
)
↪
F
4
,
↪
absent
Spin
9
↪
subscript
F
4
\displaystyle\hookrightarrow\operatorname{Spin}(9)\hookrightarrow\operatorname%
{F}_{4},
↪ roman_Spin ( 9 ) ↪ roman_F start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT ,
and the proof is complete.
∎
The symmetric space associated to
SU
⁡
(
2
)
≃
Spin
⁡
(
3
)
≃
Sp
⁡
(
1
)
similar-to-or-equals
SU
2
Spin
3
similar-to-or-equals
Sp
1
\operatorname{SU}(2)\simeq\operatorname{Spin}(3)\simeq\operatorname{Sp}(1)
roman_SU ( 2 ) ≃ roman_Spin ( 3 ) ≃ roman_Sp ( 1 )
is isometric to
S
3
superscript
𝑆
3
S^{3}
italic_S start_POSTSUPERSCRIPT 3 end_POSTSUPERSCRIPT
, hence it does not cover isospectral manifolds by Theorem
7.1
.
It is worth to mention as a similar result that Vásquez
[
Vá18
]
proved that two almost conjugate subgroups in
Spin
⁡
(
4
)
≃
SU
⁡
(
2
)
×
SU
⁡
(
2
)
similar-to-or-equals
Spin
4
SU
2
SU
2
\operatorname{Spin}(4)\simeq\operatorname{SU}(2)\times\operatorname{SU}(2)
roman_Spin ( 4 ) ≃ roman_SU ( 2 ) × roman_SU ( 2 )
are necessarily conjugate.
Question 7.5
.
Are there almost conjugate and non-conjugate subgroups in
SU
⁡
(
3
)
SU
3
\operatorname{SU}(3)
roman_SU ( 3 )
(resp.
Sp
⁡
(
2
)
≃
Spin
⁡
(
5
)
similar-to-or-equals
Sp
2
Spin
5
\operatorname{Sp}(2)\simeq\operatorname{Spin}(5)
roman_Sp ( 2 ) ≃ roman_Spin ( 5 )
,
Sp
⁡
(
3
)
Sp
3
\operatorname{Sp}(3)
roman_Sp ( 3 )
and
G
2
subscript
G
2
\operatorname{G}_{2}
roman_G start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
)?
Question 7.6
.
Which compact symmetric spaces of group type (not necessarily simply connected) cover isospectral manifolds.
Problem 7.7
.
Study Question
1.15
in the context of orbifolds covered by compact symmetric spaces.
8.
Open problems and questions
In this section we discuss further problems and questions, in addition to those included in the previous sections.
8.1.
Constructing large families of spherical space forms
Call a set of Riemannian manifolds an
isospectral set
if the manifolds in the set are pairwise isospectral and non-isometric. In
[
BGG98
]
Brooks, Gornet, and Gustafson used Sunada’s method in order to construct isospectral sets of hyperbolic surfaces of arbitrarily large cardinality. In particular, they constructed an infinite sequence of natural numbers
g
i
subscript
𝑔
𝑖
g_{i}
italic_g start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
such that for each
i
𝑖
i
italic_i
there is an isospectral set of genus
g
i
subscript
𝑔
𝑖
g_{i}
italic_g start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
hyperbolic surfaces of cardinality at least
g
i
c
⁢
log
⁡
(
g
i
)
superscript
subscript
𝑔
𝑖
𝑐
subscript
𝑔
𝑖
g_{i}^{c\log(g_{i})}
italic_g start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_c roman_log ( italic_g start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) end_POSTSUPERSCRIPT
, for some constant
c
𝑐
c
italic_c
which does not depend on
i
𝑖
i
italic_i
. We note that these isospectral sets are the largest known for hyperbolic surfaces.
The Brooks-Gornet-Gustafson construction was subsequently generalized by McReynolds
[
Mc14
]
to higher dimensional real hyperbolic spaces, to the complex hyperbolic
2
2
2
2
-space, and to the symmetric spaces of arbitrary non-compact simple Lie groups. Later work of Belolipetsky and the second author
[
BL17
]
extended the Brooks-Gornet-Gustafson construction to simple Lie groups of real rank at least
2
2
2
2
.
In light of the aforementioned work it is natural to ask for the maximal size of an isospectral set of spherical manifolds or orbifolds. Every finite group admits an orthogonal representation, hence the results mentioned above (which all employ Sunada’s method) can be modified so as to produce isospectral sets of spherical orbifolds with arbitrarily large cardinalities. It should be noted however, that the dimension of the manifolds in these isospectral sets will go to infinity as the cardinality does.
Problem 8.1
.
Fix a dimension
d
𝑑
d
italic_d
. What is the maximal cardinality of an isospectral set of spherical space forms of volume
x
𝑥
x
italic_x
and dimension
d
𝑑
d
italic_d
?
This problem seems particularly tractable in the setting of lens spaces. It seems reasonable, for example, to expect that one could modify Ikeda’s proof
[
Ik80
]
of the existence of pairs of isospectral non-isometric lens spaces in order to obtain isospectral sets of larger cardinality.
8.2.
Upper bounds on the cardinality of an isospectral set
In this section we discuss a problem which serves as a natural complement to Problem
8.1
. Given a hyperbolic surface
S
𝑆
S
italic_S
, how many hyperbolic surfaces are there that are isospectral to
S
𝑆
S
italic_S
but not isometric to it? In other words, what is the maximal cardinality of an isospectral set containing
S
𝑆
S
italic_S
? The Brooks-Gornet-Gustafson construction shows that in general, if
S
𝑆
S
italic_S
has genus
g
𝑔
g
italic_g
, then there may be as many as
g
c
⁢
log
⁡
(
g
)
superscript
𝑔
𝑐
𝑔
g^{c\log(g)}
italic_g start_POSTSUPERSCRIPT italic_c roman_log ( italic_g ) end_POSTSUPERSCRIPT
other hyperbolic surfaces isospectral to
S
𝑆
S
italic_S
but not isometric to it. The first upper bound for this quantity is due to Buser
[
Bu
]
, who showed that if
g
𝑔
g
italic_g
denotes the genus of
S
𝑆
S
italic_S
, then there are at most
e
720
⁢
g
2
superscript
𝑒
720
superscript
𝑔
2
e^{720g^{2}}
italic_e start_POSTSUPERSCRIPT 720 italic_g start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_POSTSUPERSCRIPT
hyperbolic surfaces that are isospectral to
S
𝑆
S
italic_S
but not isometric to it. This result was later improved to
e
c
⁢
g
⁢
log
⁡
(
g
)
superscript
𝑒
𝑐
𝑔
𝑔
e^{cg\log(g)}
italic_e start_POSTSUPERSCRIPT italic_c italic_g roman_log ( italic_g ) end_POSTSUPERSCRIPT
(for some universal constant
c
𝑐
c
italic_c
) by Parlier
[
Pa18
]
.
Problem 8.2
.
Let
M
𝑀
M
italic_M
be a spherical orbifold of volume
V
𝑉
V
italic_V
. What is an upper bound for the cardinality of an isospectral set of spherical orbifolds which contains
M
𝑀
M
italic_M
?
8.3.
Wolpert’s genericity results
Before Vignéras
[
Vi80
]
constructed the first examples of isospectral Riemann surfaces, Wolpert
[
Wo77
,
Wo79
]
proved that a generic Riemann surface of genus
g
≥
2
𝑔
2
g\geq 2
italic_g ≥ 2
is spectrally unique within the moduli space
ℳ
g
subscript
ℳ
𝑔
\mathcal{M}_{g}
caligraphic_M start_POSTSUBSCRIPT italic_g end_POSTSUBSCRIPT
of isometry classes of Riemann surfaces of genus
g
𝑔
g
italic_g
; that is, a generic Riemann surface is not isospectral to any non-isometric Riemann surface of the same genus.
Theorem 8.3
(Wolpert
[
Wo79
]
)
.
For each
g
∈
ℕ
𝑔
ℕ
g\in\mathbb{N}
italic_g ∈ blackboard_N
, there is a dense subset
ℳ
g
∙
superscript
subscript
ℳ
𝑔
∙
\mathcal{M}_{g}^{\bullet}
caligraphic_M start_POSTSUBSCRIPT italic_g end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∙ end_POSTSUPERSCRIPT
of
ℳ
g
subscript
ℳ
𝑔
\mathcal{M}_{g}
caligraphic_M start_POSTSUBSCRIPT italic_g end_POSTSUBSCRIPT
satisfying that for any
S
∈
ℳ
g
∙
𝑆
superscript
subscript
ℳ
𝑔
∙
S\in\mathcal{M}_{g}^{\bullet}
italic_S ∈ caligraphic_M start_POSTSUBSCRIPT italic_g end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∙ end_POSTSUPERSCRIPT
one has that
Spec
⁡
(
S
′
)
≠
Spec
⁡
(
S
)
Spec
superscript
𝑆
′
Spec
𝑆
\operatorname{Spec}(S^{\prime})\neq\operatorname{Spec}(S)
roman_Spec ( italic_S start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ) ≠ roman_Spec ( italic_S )
for all
S
′
≠
S
superscript
𝑆
′
𝑆
S^{\prime}\neq S
italic_S start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ≠ italic_S
in
ℳ
g
subscript
ℳ
𝑔
\mathcal{M}_{g}
caligraphic_M start_POSTSUBSCRIPT italic_g end_POSTSUBSCRIPT
.
In the moduli space
𝒯
n
subscript
𝒯
𝑛
\mathcal{T}_{n}
caligraphic_T start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT
of
n
𝑛
n
italic_n
-dimensional flat tori, he proved the analogous result.
Theorem 8.4
(Wolpert
[
Wo78
]
)
.
For each
n
∈
ℕ
𝑛
ℕ
n\in\mathbb{N}
italic_n ∈ blackboard_N
, there is a dense subset
𝒯
n
∙
superscript
subscript
𝒯
𝑛
∙
\mathcal{T}_{n}^{\bullet}
caligraphic_T start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∙ end_POSTSUPERSCRIPT
of
𝒯
n
subscript
𝒯
𝑛
\mathcal{T}_{n}
caligraphic_T start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT
satisfying that for any
T
∈
𝒯
n
∙
𝑇
superscript
subscript
𝒯
𝑛
∙
T\in\mathcal{T}_{n}^{\bullet}
italic_T ∈ caligraphic_T start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∙ end_POSTSUPERSCRIPT
one has that
Spec
⁡
(
T
′
)
≠
Spec
⁡
(
T
)
Spec
superscript
𝑇
′
Spec
𝑇
\operatorname{Spec}(T^{\prime})\neq\operatorname{Spec}(T)
roman_Spec ( italic_T start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ) ≠ roman_Spec ( italic_T )
for all
T
′
≠
T
superscript
𝑇
′
𝑇
T^{\prime}\neq T
italic_T start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ≠ italic_T
in
𝒯
n
subscript
𝒯
𝑛
\mathcal{T}_{n}
caligraphic_T start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT
.
It is natural to ask if a similar situation occurs for lens spaces.
Problem 8.5
.
Is a “generic” lens space spectrally unique?
Note that there is not a direct analogy to the case of Riemann surfaces and flat tori due to the absence of a natural topology on the space of lens spaces. In what follows we formulate a possible extension of Wolpert’s results and provide numerical evidence for its validity.
For positive integers
n
,
q
𝑛
𝑞
n,q
italic_n , italic_q
, let us denote by
𝔏
⁢
(
n
,
q
)
𝔏
𝑛
𝑞
\mathfrak{L}(n,q)
fraktur_L ( italic_n , italic_q )
the isometry classes of
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional lens spaces with fundamental group of order
q
𝑞
q
italic_q
.
We set
(8.1)
𝔏
∙
⁢
(
n
,
q
)
=
{
L
∈
𝔏
⁢
(
n
,
q
)
:
Spec
⁡
(
L
)
≠
Spec
⁡
(
L
′
)
∀
L
′
≠
L
⁢
in
⁢
𝔏
⁢
(
n
,
q
)
}
.
superscript
𝔏
∙
𝑛
𝑞
conditional-set
𝐿
𝔏
𝑛
𝑞
formulae-sequence
Spec
𝐿
Spec
superscript
𝐿
′
for-all
superscript
𝐿
′
𝐿
in
𝔏
𝑛
𝑞
\mathfrak{L}^{\bullet}(n,q)=\{L\in\mathfrak{L}(n,q):\operatorname{Spec}(L)\neq%
\operatorname{Spec}(L^{\prime})\quad\forall\,L^{\prime}\neq L\text{ in }%
\mathfrak{L}(n,q)\}.
fraktur_L start_POSTSUPERSCRIPT ∙ end_POSTSUPERSCRIPT ( italic_n , italic_q ) = { italic_L ∈ fraktur_L ( italic_n , italic_q ) : roman_Spec ( italic_L ) ≠ roman_Spec ( italic_L start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ) ∀ italic_L start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ≠ italic_L in fraktur_L ( italic_n , italic_q ) } .
In words,
𝔏
∙
⁢
(
n
,
q
)
superscript
𝔏
∙
𝑛
𝑞
\mathfrak{L}^{\bullet}(n,q)
fraktur_L start_POSTSUPERSCRIPT ∙ end_POSTSUPERSCRIPT ( italic_n , italic_q )
is the subset of
𝔏
⁢
(
n
,
q
)
𝔏
𝑛
𝑞
\mathfrak{L}(n,q)
fraktur_L ( italic_n , italic_q )
given by lens spaces that are spectrally unique within
𝔏
⁢
(
n
,
q
)
𝔏
𝑛
𝑞
\mathfrak{L}(n,q)
fraktur_L ( italic_n , italic_q )
.
The space of all (isometry classes) of
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional lens spaces is
⋃
q
≥
1
𝔏
⁢
(
n
,
q
)
subscript
𝑞
1
𝔏
𝑛
𝑞
\bigcup_{q\geq 1}\mathfrak{L}(n,q)
⋃ start_POSTSUBSCRIPT italic_q ≥ 1 end_POSTSUBSCRIPT fraktur_L ( italic_n , italic_q )
.
Now, for a positive number
x
𝑥
x
italic_x
, it is natural to ask whether the density
(8.2)
𝒰
n
⁢
(
x
)
:=
∑
q
≤
x
#
⁢
𝔏
∙
⁢
(
n
,
q
)
∑
q
≤
x
#
⁢
𝔏
⁢
(
n
,
q
)
assign
subscript
𝒰
𝑛
𝑥
subscript
𝑞
𝑥
#
superscript
𝔏
∙
𝑛
𝑞
subscript
𝑞
𝑥
#
𝔏
𝑛
𝑞
\mathcal{U}_{n}(x):=\frac{\sum\limits_{q\leq x}\#\mathfrak{L}^{\bullet}(n,q)}{%
\sum\limits_{q\leq x}\#\mathfrak{L}(n,q)}
caligraphic_U start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ( italic_x ) := divide start_ARG ∑ start_POSTSUBSCRIPT italic_q ≤ italic_x end_POSTSUBSCRIPT # fraktur_L start_POSTSUPERSCRIPT ∙ end_POSTSUPERSCRIPT ( italic_n , italic_q ) end_ARG start_ARG ∑ start_POSTSUBSCRIPT italic_q ≤ italic_x end_POSTSUBSCRIPT # fraktur_L ( italic_n , italic_q ) end_ARG
of the set of spectrally unique lens spaces with fundamental groups of order
≤
x
absent
𝑥
\leq x
≤ italic_x
into the set of lens spaces with fundamental groups of order
≤
x
absent
𝑥
\leq x
≤ italic_x
is close to
1
1
1
1
.
Conjecture 8.6
.
One has
lim
x
→
∞
𝒰
n
⁢
(
x
)
=
1
subscript
→
𝑥
subscript
𝒰
𝑛
𝑥
1
\displaystyle\lim_{x\to\infty}\mathcal{U}_{n}(x)=1
roman_lim start_POSTSUBSCRIPT italic_x → ∞ end_POSTSUBSCRIPT caligraphic_U start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ( italic_x ) = 1
for all
n
∈
ℕ
𝑛
ℕ
n\in\mathbb{N}
italic_n ∈ blackboard_N
.
Table 3.
Density of spectrally unique
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional lens spaces for
n
=
3
𝑛
3
n=3
italic_n = 3
,
4
4
4
4
,
5
5
5
5
,
6
6
6
6
,
7
7
7
7
.
n
x
∑
q
≤
x
#
⁢
𝔏
∙
⁢
(
n
,
q
)
∑
q
≤
x
#
⁢
𝔏
⁢
(
n
,
q
)
𝒰
n
⁢
(
x
)
⁢
3
50
40
990
0.95960
100
64
6680
0.99042
150
83
21881
0.99621
200
119
51580
0.99769
250
131
97546
0.99866
300
183
167856
0.99891
⁢
4
30
47
693
0.93218
60
138
7966
0.98268
90
202
36699
0.99450
120
228
107094
0.99787
150
268
253189
0.99894
⁢
5
10
0
28
1.0000
20
23
397
0.94207
30
74
1806
0.95903
40
127
5456
0.97672
50
197
17332
0.98863
60
255
37137
0.99313
70
345
71449
0.99517
⁢
6
10
0
37
1.0000
20
14
801
0.98252
30
118
4640
0.97457
40
199
16497
0.98794
50
297
66751
0.99555
60
432
163935
0.99736
⁢
7
10
0
41
1.0000
20
9
1501
0.99400
30
174
11188
0.98445
40
358
46750
0.99234
50
466
239345
0.99805
𝑛
𝑥
subscript
𝑞
𝑥
#
superscript
𝔏
∙
𝑛
𝑞
subscript
𝑞
𝑥
#
𝔏
𝑛
𝑞
subscript
𝒰
𝑛
𝑥
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
3
50
40
990
0.95960
missing-subexpression
missing-subexpression
missing-subexpression
100
64
6680
0.99042
missing-subexpression
missing-subexpression
missing-subexpression
150
83
21881
0.99621
missing-subexpression
missing-subexpression
missing-subexpression
200
119
51580
0.99769
missing-subexpression
missing-subexpression
missing-subexpression
250
131
97546
0.99866
missing-subexpression
missing-subexpression
missing-subexpression
300
183
167856
0.99891
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
4
30
47
693
0.93218
missing-subexpression
missing-subexpression
missing-subexpression
60
138
7966
0.98268
missing-subexpression
missing-subexpression
missing-subexpression
90
202
36699
0.99450
missing-subexpression
missing-subexpression
missing-subexpression
120
228
107094
0.99787
missing-subexpression
missing-subexpression
missing-subexpression
150
268
253189
0.99894
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
5
10
0
28
1.0000
missing-subexpression
missing-subexpression
missing-subexpression
20
23
397
0.94207
missing-subexpression
missing-subexpression
missing-subexpression
30
74
1806
0.95903
missing-subexpression
missing-subexpression
missing-subexpression
40
127
5456
0.97672
missing-subexpression
missing-subexpression
missing-subexpression
50
197
17332
0.98863
missing-subexpression
missing-subexpression
missing-subexpression
60
255
37137
0.99313
missing-subexpression
missing-subexpression
missing-subexpression
70
345
71449
0.99517
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
6
10
0
37
1.0000
missing-subexpression
missing-subexpression
missing-subexpression
20
14
801
0.98252
missing-subexpression
missing-subexpression
missing-subexpression
30
118
4640
0.97457
missing-subexpression
missing-subexpression
missing-subexpression
40
199
16497
0.98794
missing-subexpression
missing-subexpression
missing-subexpression
50
297
66751
0.99555
missing-subexpression
missing-subexpression
missing-subexpression
60
432
163935
0.99736
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
missing-subexpression
7
10
0
41
1.0000
missing-subexpression
missing-subexpression
missing-subexpression
20
9
1501
0.99400
missing-subexpression
missing-subexpression
missing-subexpression
30
174
11188
0.98445
missing-subexpression
missing-subexpression
missing-subexpression
40
358
46750
0.99234
missing-subexpression
missing-subexpression
missing-subexpression
50
466
239345
0.99805
missing-subexpression
missing-subexpression
\begin{array}[]{ccccccc}n&x&\sum\limits_{q\leq x}\#\mathfrak{L}^{\bullet}(n,q)%
&\sum\limits_{q\leq x}\#\mathfrak{L}(n,q)&\mathcal{U}_{n}(x)\\
\hline\cr\hline\cr\rule{0.0pt}{14.0pt}3&50&40&990&0.95960\\
&100&64&6680&0.99042\\
&150&83&21881&0.99621\\
&200&119&51580&0.99769\\
&250&131&97546&0.99866\\
&300&183&167856&0.99891\\
\hline\cr\rule{0.0pt}{14.0pt}4&30&47&693&0.93218\\
&60&138&7966&0.98268\\
&90&202&36699&0.99450\\
&120&228&107094&0.99787\\
&150&268&253189&0.99894\\
\hline\cr\rule{0.0pt}{14.0pt}5&10&0&28&1.0000\\
&20&23&397&0.94207\\
&30&74&1806&0.95903\\
&40&127&5456&0.97672\\
&50&197&17332&0.98863\\
&60&255&37137&0.99313\\
&70&345&71449&0.99517\\
\hline\cr\rule{0.0pt}{14.0pt}6&10&0&37&1.0000\\
&20&14&801&0.98252\\
&30&118&4640&0.97457\\
&40&199&16497&0.98794\\
&50&297&66751&0.99555\\
&60&432&163935&0.99736\\
\hline\cr\rule{0.0pt}{14.0pt}7&10&0&41&1.0000\\
&20&9&1501&0.99400\\
&30&174&11188&0.98445\\
&40&358&46750&0.99234\\
&50&466&239345&0.99805\\
\end{array}
start_ARRAY start_ROW start_CELL italic_n end_CELL start_CELL italic_x end_CELL start_CELL ∑ start_POSTSUBSCRIPT italic_q ≤ italic_x end_POSTSUBSCRIPT # fraktur_L start_POSTSUPERSCRIPT ∙ end_POSTSUPERSCRIPT ( italic_n , italic_q ) end_CELL start_CELL ∑ start_POSTSUBSCRIPT italic_q ≤ italic_x end_POSTSUBSCRIPT # fraktur_L ( italic_n , italic_q ) end_CELL start_CELL caligraphic_U start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ( italic_x ) end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 3 end_CELL start_CELL 50 end_CELL start_CELL 40 end_CELL start_CELL 990 end_CELL start_CELL 0.95960 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 100 end_CELL start_CELL 64 end_CELL start_CELL 6680 end_CELL start_CELL 0.99042 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 150 end_CELL start_CELL 83 end_CELL start_CELL 21881 end_CELL start_CELL 0.99621 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 200 end_CELL start_CELL 119 end_CELL start_CELL 51580 end_CELL start_CELL 0.99769 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 250 end_CELL start_CELL 131 end_CELL start_CELL 97546 end_CELL start_CELL 0.99866 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 300 end_CELL start_CELL 183 end_CELL start_CELL 167856 end_CELL start_CELL 0.99891 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 4 end_CELL start_CELL 30 end_CELL start_CELL 47 end_CELL start_CELL 693 end_CELL start_CELL 0.93218 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 60 end_CELL start_CELL 138 end_CELL start_CELL 7966 end_CELL start_CELL 0.98268 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 90 end_CELL start_CELL 202 end_CELL start_CELL 36699 end_CELL start_CELL 0.99450 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 120 end_CELL start_CELL 228 end_CELL start_CELL 107094 end_CELL start_CELL 0.99787 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 150 end_CELL start_CELL 268 end_CELL start_CELL 253189 end_CELL start_CELL 0.99894 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 5 end_CELL start_CELL 10 end_CELL start_CELL 0 end_CELL start_CELL 28 end_CELL start_CELL 1.0000 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 20 end_CELL start_CELL 23 end_CELL start_CELL 397 end_CELL start_CELL 0.94207 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 30 end_CELL start_CELL 74 end_CELL start_CELL 1806 end_CELL start_CELL 0.95903 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 40 end_CELL start_CELL 127 end_CELL start_CELL 5456 end_CELL start_CELL 0.97672 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 50 end_CELL start_CELL 197 end_CELL start_CELL 17332 end_CELL start_CELL 0.98863 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 60 end_CELL start_CELL 255 end_CELL start_CELL 37137 end_CELL start_CELL 0.99313 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 70 end_CELL start_CELL 345 end_CELL start_CELL 71449 end_CELL start_CELL 0.99517 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 6 end_CELL start_CELL 10 end_CELL start_CELL 0 end_CELL start_CELL 37 end_CELL start_CELL 1.0000 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 20 end_CELL start_CELL 14 end_CELL start_CELL 801 end_CELL start_CELL 0.98252 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 30 end_CELL start_CELL 118 end_CELL start_CELL 4640 end_CELL start_CELL 0.97457 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 40 end_CELL start_CELL 199 end_CELL start_CELL 16497 end_CELL start_CELL 0.98794 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 50 end_CELL start_CELL 297 end_CELL start_CELL 66751 end_CELL start_CELL 0.99555 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 60 end_CELL start_CELL 432 end_CELL start_CELL 163935 end_CELL start_CELL 0.99736 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL 7 end_CELL start_CELL 10 end_CELL start_CELL 0 end_CELL start_CELL 41 end_CELL start_CELL 1.0000 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 20 end_CELL start_CELL 9 end_CELL start_CELL 1501 end_CELL start_CELL 0.99400 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 30 end_CELL start_CELL 174 end_CELL start_CELL 11188 end_CELL start_CELL 0.98445 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 40 end_CELL start_CELL 358 end_CELL start_CELL 46750 end_CELL start_CELL 0.99234 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW start_ROW start_CELL end_CELL start_CELL 50 end_CELL start_CELL 466 end_CELL start_CELL 239345 end_CELL start_CELL 0.99805 end_CELL start_CELL end_CELL start_CELL end_CELL end_ROW end_ARRAY
Table
3
provides, for small values of
x
𝑥
x
italic_x
, numerical calculations of
𝒰
n
⁢
(
x
)
subscript
𝒰
𝑛
𝑥
\mathcal{U}_{n}(x)
caligraphic_U start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT ( italic_x )
for
3
≤
n
≤
7
3
𝑛
7
3\leq n\leq 7
3 ≤ italic_n ≤ 7
.
A first step towards proving the above conjecture could be to show, for a fixed dimension
2
⁢
n
−
1
2
𝑛
1
2n-1
2 italic_n - 1
, infinitely many values of
q
∈
ℕ
𝑞
ℕ
q\in\mathbb{N}
italic_q ∈ blackboard_N
such that no isospectrality can occur within
𝔏
⁢
(
n
,
q
)
𝔏
𝑛
𝑞
\mathfrak{L}(n,q)
fraktur_L ( italic_n , italic_q )
, that is,
𝔏
∙
⁢
(
n
,
q
)
=
𝔏
⁢
(
n
,
q
)
superscript
𝔏
∙
𝑛
𝑞
𝔏
𝑛
𝑞
\mathfrak{L}^{\bullet}(n,q)=\mathfrak{L}(n,q)
fraktur_L start_POSTSUPERSCRIPT ∙ end_POSTSUPERSCRIPT ( italic_n , italic_q ) = fraktur_L ( italic_n , italic_q )
.
Problem 8.7
.
Provide conditions on
n
𝑛
n
italic_n
and
q
𝑞
q
italic_q
such that
𝔏
∙
⁢
(
n
,
q
)
=
𝔏
⁢
(
n
,
q
)
superscript
𝔏
∙
𝑛
𝑞
𝔏
𝑛
𝑞
\mathfrak{L}^{\bullet}(n,q)=\mathfrak{L}(n,q)
fraktur_L start_POSTSUPERSCRIPT ∙ end_POSTSUPERSCRIPT ( italic_n , italic_q ) = fraktur_L ( italic_n , italic_q )
; that is, for which no (non-trivial) isospectrality is possible among
(
2
⁢
n
−
1
)
2
𝑛
1
(2n-1)
( 2 italic_n - 1 )
-dimensional lens spaces with volume
vol
⁡
(
S
2
⁢
n
−
1
)
q
vol
superscript
𝑆
2
𝑛
1
𝑞
\frac{\operatorname{vol}(S^{2n-1})}{q}
divide start_ARG roman_vol ( italic_S start_POSTSUPERSCRIPT 2 italic_n - 1 end_POSTSUPERSCRIPT ) end_ARG start_ARG italic_q end_ARG
.
8.4.
The length spectra of spherical space forms
The length spectrum of a hyperbolic manifold, or more generally of a closed Riemannian manifold, is the set of lengths of closed geodesics on the manifold. The length spectrum has been an extremely fruitful area of research and is closely related to the Laplace eigenvalue spectrum. For example, the Selberg Trace Formula implies that two hyperbolic surfaces are (Laplace) isospectral if and only if they have the same length spectrum (see e.g.
[
Bu
, Chapter 7]
). The work of Duistermaat and Guillemin and Duistermaat, Kolk, and Varadarajan shows that in the setting of compact locally symmetric manifolds of nonpositive curvature, the Laplace spectrum determines the length spectrum. (See also
[
PR09
, Theorem 10.1]
.)
Question 8.8
.
What is the relationship between the Laplace spectrum and the length spectrum of a spherical space form?
Some of the most interesting work concerning the length spectra of locally symmetric spaces of nonpositive curvature has been done in the arithmetic case and concerns the notion of
commensurability
. Recall that two Riemannian manifolds are said to be commensurable if they have a common finite degree covering space. It is a result of Reid
[
Re92
]
that arithmetic hyperbolic surfaces with the same length spectra are necessarily commensurable. This result was extended to arithmetic hyperbolic
3
3
3
3
-manifolds by Chinburg, Hamilton, Long, and Reid
[
CHLR08
]
, and to a very broad class of arithmetic locally symmetric spaces by Prasad and Rapinchuk
[
PR09
]
. More recently, the second author, together with McReynolds, Pollack and Thompson, has proven (see
[
LMPT18
]
) that two incommensurable arithmetic hyperbolic manifolds of dimension
2
2
2
2
or
3
3
3
3
must have length spectra that disagree for some geodesic length bounded by an explicit function of the manifolds’ volumes.
Although all spherical space forms are trivially commensurable (they are all covered with finite degree by the sphere
S
d
superscript
𝑆
𝑑
S^{d}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
), one might instead consider the notion of
quotient commensurable
manifolds. Two Riemannian manifolds are said to be quotient commensurable if they share a common, finite degree quotient manifold. If
S
d
/
Γ
1
superscript
𝑆
𝑑
subscript
Γ
1
S^{d}/\Gamma_{1}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
S
d
/
Γ
2
superscript
𝑆
𝑑
subscript
Γ
2
S^{d}/\Gamma_{2}
italic_S start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT / roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are spherical space forms, then they are quotient commensurable if and only if
Γ
1
subscript
Γ
1
\Gamma_{1}
roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
Γ
2
subscript
Γ
2
\Gamma_{2}
roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
both have finite index inside the group
G
=
⟨
Γ
1
,
Γ
2
⟩
𝐺
subscript
Γ
1
subscript
Γ
2
G=\langle\Gamma_{1},\Gamma_{2}\rangle
italic_G = ⟨ roman_Γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , roman_Γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ⟩
.
Question 8.9
.
If two spherical space forms have the same length spectrum, must they be quotient commensurable?
8.5.
Isospectral but not strongly isospectral hyperbolic manifolds
We end the article with a question that goes in the reverse direction in the sense that it concerns a result in the compact setting which is open in the non-compact one.
We mentioned after Theorem
2.2
that Sunada’s method always produces
strongly isospectral
manifolds.
In particular, in addition to the Laplace-Beltrami operator (acting on
0
0
-forms), the corresponding Hodge-Laplace operators acting on
p
𝑝
p
italic_p
-forms are isospectral, for each
p
𝑝
p
italic_p
.
It has been known for a while that Ikeda’s examples of lens spaces cannot be constructed via Sunada’s method (see
[
Ch92
]
).
Miatello, Rossetti and the first author proved that strongly isospectral lens spaces are necessarily isometric (see
[
LMR16
, Prop. 7.2]
), so isospectral and non-isometric lens spaces, including Ikeda’s examples, are not strongly isospectral.
Question 8.10
.
Are there isospectral hyperbolic manifolds that are not strongly isospectral?
Furthermore, there are lens spaces
p
𝑝
p
italic_p
-isospectral for all
p
𝑝
p
italic_p
, and not strongly isospectral (see
[
LMR16
]
and
[
DD18
]
).
Question 8.11
.
Are there hyperbolic manifolds
p
𝑝
p
italic_p
-isospectral for all
p
𝑝
p
italic_p
that are not strongly isospectral?
Doyle and Rossetti have conjectured that the answer is negative (see
[
DR
, §9]
).
References
[BH19]
N.S. Bari, E. Hunsicker
.
Isospectrality for orbifolds lens spaces.
Canad. J. Math.
72
:2 (2020), 281–325.
DOI:
10.4153/S0008414X19000178
.
[BL17]
M. Belolipetsky, B. Linowitz
.
Counting isospectral manifolds.
Adv. Math.
321
(2017), 69–79.
DOI:
10.1016/j.aim.2017.09.040
.
[BR11]
C. Bhagwat, C.S. Rajan
.
On a spectral analog of the strong multiplicity one theorem.
Int. Math. Res. Not. IMRN
2011
:18 (2011), 4059–4073.
DOI:
10.1093/imrn/rnq243
.
[BGG98]
R. Brooks, R. Gornet, W.H. Gustafson
.
Mutually isospectral Riemann surfaces.
Adv. Math.
138
:2 (1998), 306–322.
DOI:
10.1006/aima.1998.1750
.
[BT87]
R. Brooks, R. Tse
.
Isospectral surfaces of small genus.
Nagoya Math. J.
107
(1987), 13–24.
DOI:
10.1017/S0027763000002518
.
[Bu]
P. Buser
.
Geometry and spectra of compact Riemann surfaces.
Progr. Math.
106
.
Birkhäuser Boston, 1992.
[BS94]
P. Buser, P. Sarnak
.
On the period matrix of a Riemann surface of large genus
(with an appendix by J. H. Conway and N. J. A. Sloane).
Invent. Math.
117
:1 (1994), 27–56.
DOI:
10.1007/BF01232233
.
[BC90]
P. Buser, G. Courtois
.
Finite parts of the spectrum of a Riemann surface.
Math. Ann.
287
:3 (1990), 523–530.
DOI:
10.1007/BF01446910
.
[Ch92]
S. Chen
.
Constructing isospectral but nonisometric Riemannian manifolds
.
Canad. Math. Bull.
35
(1992), 303–310.
DOI:
10.4153/CMB-1992-042-1
.
[CHLR08]
T. Chinburg, E. Hamilton, D.D. Long, A.W. Reid
.
Geodesics and commensurability classes of arithmetic hyperbolic 3-manifolds
.
Duke Math. J.
145
:1 (2008), 25–44.
DOI:
10.1215/00127094-2008-045
.
[DW94]
X. Dai, G. Wei
.
Finite part of spectrum and isospectrality.
In
Geometry of the spectrum
, 99–107,
Contemp. Math.
173
, Amer. Math. Soc., Providence, RI, 1994.
DOI:
10.1090/conm/173/01818
.
[DD18]
D. DeFord, P. Doyle
.
Cyclic groups with the same Hodge series
.
Rev. Un. Mat. Argentina
59
:2 (2018), 241–254.
DOI:
10.33044/revuma.v59n2a02
.
[DR]
P. Doyle, J.P. Rossetti
.
Laplace-isospectral hyperbolic 2-orbifolds are representation-equivalent
.
10.48550/arXiv.1103.4372v2
(2014).
[DG75]
J.J. Duistermaat, V.W. Guillemin
.
The spectrum of positive elliptic operators and periodic bicharacteristics
.
Invent. Math.
29
:1 (1975), 39–79.
DOI:
10.1007/BF01405172
.
[DKV79]
J.J. Duistermaat, J.A.C. Kolk, V.S. Varadarajan
.
Spectra of compact locally symmetric manifolds of negative curvature
.
Invent. Math.
52
:1 (1979), 27–93.
DOI:
10.1007/BF01389856
.
[Go00]
C. Gordon
.
Survey of isospectral manifolds.
In
Handbook of differential geometry
, Vol. I, 747–778, North-Holland, Amsterdam, 2000.
[Go12]
C. Gordon
.
Orbifolds and their spectra
.
In
Spectral Geometry
, 49–71,
Proc. Sympos. Pure Math.
84
, Amer. Math. Soc., Providence, RI, 2012.
DOI:
10.1090/pspum/084
.
[Ik80]
A. Ikeda
.
On lens spaces which are isospectral but not isometric
.
Ann. Sci. École Norm. Sup. (4)
13
:3 (1980), 303–315.
[Ik80]
A. Ikeda
.
On the spectrum of a riemannian manifold of positive constant curvature.
Osaka J. Math.
17
(1980), 75–93.
DOI:
10.18910/5171
[Ik83]
A. Ikeda
.
On spherical space forms which are isospectral but not isometric
.
J. Math. Soc. Japan
35
:3 (1983), 437–444.
DOI:
10.2969/jmsj/03530437
.
[Ik97]
A. Ikeda
.
On space forms of real Grassmann manifolds which are isospectral but not isometric
.
Kodai Math. J.
20
:1 (1997), 1–7.
DOI:
10.2996/kmj/1138043715
.
[IY79]
A. Ikeda, Y. Yamamoto
.
On the spectra of 3-dimensional lens spaces
.
Osaka J. Math.
16
:2 (1979), 447–469.
DOI:
10.18910/4811
.
[Ka66]
M. Kac
.
Can one hear the shape of a drum?
Amer. Math. Monthly
73
(1966), 1–23.
[KSV07]
M. G. Katz, M. Schaps, U. Vishne
.
Logarithmic growth of systole of arithmetic Riemann surfaces along congruence subgroups.
J. Differential Geom.
76
:3 (2007), 399–422.
DOI:
10.4310/jdg/1180135693
.
[LLM23]
S. Lapan, B. Linowitz and J. Meyer
.
Systole inequalities for arithmetic locally symmetric spaces.
To appear in Comm. Anal. Geom.
DOI:
10.48550/arXiv.1710.00071
.
[La16]
E.A. Lauret
.
Spectra of orbifolds with cyclic fundamental groups
.
Ann. Global Anal. Geom.
50
:1 (2016), 1–28.
DOI:
10.1007/s10455-016-9498-0
.
[La21]
E.A. Lauret
.
A computational study on lens spaces isospectral on forms
.
Exp. Math.
30
:2 (2021), 268–282.
DOI:
10.1080/10586458.2018.1538908
.
[LM20]
E.A. Lauret, R.J. Miatello
.
Strong multiplicity one theorems for locally homogeneous spaces of compact type.
Proc. Amer. Math. Soc.
148
:7 (2020), 3163–3173.
DOI:
10.1090/proc/14980
.
[LM21]
E.A. Lauret, R.J. Miatello
.
Representation equivalence for compact symmetric spaces of real rank one.
Pacific J. Math.
314
:2 (2021), 333–373.
DOI:
10.2140/pjm.2021.314.333
.
[LMR16]
E.A. Lauret, R.J. Miatello, J.P. Rossetti
.
Spectra of lens spaces from 1-norm spectra of congruence lattices.
Int. Math. Res. Not. IMRN
2016
:4 (2016), 1054–1089.
DOI:
10.1093/imrn/rnv159
.
[LMR21]
E.A. Lauret, R.J. Miatello, J.P. Rossetti
.
Recent results on the spectra of lens spaces.
São Paulo J. Math. Sci.
15
:1 (2021), 240–267.
DOI:
10.1007/s40863-019-00154-3
.
[LMNR07]
C. J. Leininger, D. B. McReynolds, W. D. Neumann, A. W. Reid
.
Length and eigenvalue equivalence.
Int. Math. Res. Not. IMRN
2007
:24 (2007), rnm135.
DOI:
10.1093/imrn/rnm135
.
[Li12]
B. Linowitz
.
Isospectral towers of Riemannian manifolds.
New York J. Math.
18
(2012), 451–461.
[LMPT18]
B. Linowitz, D.B. McReynolds, P. Pollack, L. Thompson
.
Counting and effective rigidity in algebra and geometry
.
Invent. Math.
213
:2 (2018), 697–758.
DOI:
10.1007/s00222-018-0796-y
.
[LV15]
B. Linowitz, J. Voight
.
Small isospectral and nonisometric orbifolds of dimension 2 and 3.
Math. Z.
281
:1–2 (2015), 523–569.
DOI:
10.1007/s00209-015-1500-1
.
[Mc14]
D.B. Mc Reynolds
.
Isospectral locally symmetric manifolds.
Indiana Univ. Math. J.
63
:2 (2014), 533–549.
[MR03]
R.J. Miatello, J.P. Rossetti
.
Length spectra and
p
𝑝
p
italic_p
-spectra of compact flat manifolds
.
Jour. Geom. Analysis
13
:4 (2003), 631–657.
DOI:
10.1007/BF02921882
.
[Mi64]
J. Milnor
.
Eigenvalues of the Laplace operator on certain manifolds.
Proc. Natl. Acad. Sci. USA
51
:4 (1964), 542.
[Pa18]
H. Parlier
.
Interrogating surface length spectra and quantifying isospectrality
.
Math. Ann.
370
:3–4 (2018), 1759–1787.
DOI:
10.1007/s00208-017-1571-x
.
[PR09]
G. Prasad, A.S. Rapinchuk
.
Weakly commensurable arithmetic groups and isospectral locally symmetric spaces
.
Publ. Math. Inst. Hautes Études Sci.
109
(2009), 113–184.
DOI:
10.1007/s10240-009-0019-6
.
[Re92]
A.W. Reid
.
Isospectrality and commensurability of arithmetic hyperbolic
2
2
2
2
- and
3
3
3
3
-manifolds.
Duke Math. J.
65
:2 (1992), 215–228.
DOI:
10.1215/S0012-7094-92-06508-2
.
[RSW08]
J.P. Rossetti, D. Schueth, M. Weilandt
.
Isospectral orbifolds with different maximal isotropy orders
.
Ann. Global Anal. Geom.
34
:4 (2008), 351–366.
DOI:
10.1007/s10455-008-9110-3
.
[Se]
M.R. Sepanski
.
Compact Lie groups.
Grad. Texts in Math.
235
.
Springer-Verlag New York, 2007.
DOI:
10.1007/978-0-387-49158-5
.
[Sp89]
R.J. Spatzier
.
On isospectral locally symmetric spaces and a theorem of von Neumann.
Duke Math. J.
59
:1 (1989), 289–294.
DOI:
10.1215/S0012-7094-89-05910-3
.
[Su85]
T. Sunada
.
Riemannian coverings and isospectral manifolds.
Ann. of Math. (2)
121
:1 (1985), 169–186.
DOI:
10.2307/1971195
.
[Vá18]
J.J. Vásquez
.
Isospectral nearly Kähler manifolds.
Abh. Math. Semin. Univ. Hambg.
88
:1 (2018), 23–50.
DOI:
10.1007/s12188-017-0185-2
.
[Vi80]
M. Vignéras
.
Variétés riemanniennes isospectrales et non isométriques.
Ann. of Math. (2)
112
:1 (1980), 21–32.
DOI:
10.2307/1971319
.
[Wo]
J. Wolf
.
Spaces of constant curvature. 6th ed.
Providence, RI: AMS Chelsea Publishing, 2011.
[Wo01]
J. Wolf
.
Isospectrality for spherical space forms.
Result. Math.
40
(2001), 321–338.
DOI:
10.1007/BF03322715
.
[Wo77]
S. Wolpert
.
The eigenvalue spectrum as moduli for compact Riemann surfaces.
Bull. Amer. Math. Soc.
83
(1977), 1306–1308.
DOI:
10.1090/S0002-9904-1977-14425-X
.
[Wo78]
S. Wolpert
.
The eigenvalue spectrum as moduli for flat tori.
Trans. Amer. Math. Soc.
244
(1978), 313–321.
DOI:
10.2307/1997901
.
[Wo79]
S. Wolpert
.
The length spectra as moduli for compact Riemann surfaces.
Ann. of Math. (2)
109
(1979), 323–351.
DOI:
10.2307/1971114
.
[Ya79]
S. Yamaguchi
.
Spectra of flag manifolds.
Mem. Fac. Sci. Kyushu Univ. Ser. A
33
:1 (1979), 95–112.
DOI:
10.2206/kyushumfs.33.95
.