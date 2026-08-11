---
title: Do the Hodge spectra distinguish orbifolds from manifolds? Part 2
id: do-the-hodge-spectra-distinguish-orbifolds-from-manifolds-part-2
tags:
- hyperbolic-pillow-heat-novelty-813161
- doi-record
created: '2026-08-09T08:43:02.170344Z'
updated: '2026-08-09T09:36:32.184960Z'
source: https://arxiv.org/html/2311.00337
source_domain: arxiv.org
fetched_at: '2026-08-09T08:43:02.169253Z'
fetch_provider: builtin
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: Full arXiv HTML rendering of Gittins et al., 'Do the Hodge Spectra Distinguish
  Orbifolds from Manifolds? Part 2' (arXiv:2311.00337v2). Confirms full author list
  (Katie Gittins, Carolyn Gordon, Ingrid Membrillo Solis, Juan Pablo Rossetti, Mary
  Sandoval, Elizabeth Stanhope) and affiliations. See [[231100337-do-the-hodge-spectra-distinguish-orbifolds-from-manifolds-part-2]]
  and [[20236493]] for the published-DOI resolution (Michigan Math. J., advance publication,
  DOI 10.1307/mmj/20236493 -- manuscript's 'preprint, arXiv:2311.00337 (2023)' citation
  is STALE).
---

Do the Hodge spectra distinguish orbifolds from manifolds? Part 2
License: arXiv.org perpetual non-exclusive license
arXiv:2311.00337v2 [math.DG] 04 Jan 2024
\setenumerate
label=0.,ref=0
Do the Hodge spectra distinguish orbifolds from manifolds?
Part 2
Katie Gittins
Department of Mathematical Sciences, Durham University,
Mathematical Sciences & Computer Science Building,
Upper Mountjoy Campus, Stockton Road,
Durham DH1 3LE,
United Kingdom.
katie.gittins@durham.ac.uk
,
Carolyn Gordon
Department of Mathematics, Dartmouth College, Hanover, NH, 03755, USA.
csgordon@dartmouth.edu
,
Ingrid Membrillo Solis
Mathematical Sciences, University of Southampton, Southampton SO17 1BJ, United Kingdom
i.membrillo-solis@soton.ac.uk
,
Juan Pablo Rossetti
Universidad Nacional de Cordoba, Medina Allende s/n, Ciudad Universitaria, 5000 Cordoba, Argentina.
jprossetti@unc.edu.ar
,
Mary Sandoval
Department of Mathematics, Trinity College, 300 Summit Street, Hartford, CT, 06106, USA.
mary.sandoval@trincoll.edu
and
Elizabeth Stanhope
Department of Mathematical Sciences, Lewis & Clark College, Portland, OR, 97219, USA.
stanhope@lclark.edu
Abstract.
In
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
we examined the relationship between the singular set of a compact Riemannian orbifold and the spectrum of the Hodge Laplacian on
p
𝑝
p
italic_p
-forms by computing the heat invariants associated to the
p
𝑝
p
italic_p
-spectrum. We showed that the heat invariants of the
0
0
-spectrum together with those of the
1
1
1
1
-spectrum for the corresponding Hodge Laplacians are sufficient to distinguish orbifolds from manifolds as long as the singular sets have codimension
≤
3
.
absent
3
\leq 3.
≤ 3 .
This is enough to distinguish orbifolds from manifolds for dimension
≤
3
.
absent
3
\leq 3.
≤ 3 .
Here we give both positive and negative inverse spectral results for the individual
p
𝑝
p
italic_p
-spectra considered separately. For example, we give conditions on the codimension of the singular set which guarantee that the volume of the singular set is determined, and in many cases we show by providing counterexamples that the conditions are sharp.
Key words and phrases:
Hodge Laplacian, orbifolds, isospectrality
2020 Mathematics Subject Classification:
Primary: 58J53; Secondary: 53C20 58J50 58J37
1.
Introduction
A (Riemannian) orbifold is a generalization of a (Riemannian) manifold that permits the presence of mild singularities, in the following sense: orbifolds of dimension
d
𝑑
d
italic_d
are locally modeled by the orbit spaces of finite effective group actions on
ℝ
d
superscript
ℝ
𝑑
\mathbb{R}^{d}
blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
. Orbifold singularities correspond to orbits with non-trivial isotropy and thus each singularity has an associated “isotropy type.” Orbifolds appear in a variety of mathematical areas and have applications in physics, in particular to string theory. In this paper, we will always assume all orbifolds under consideration are connected and compact without boundary.
The notions of the Laplace-Beltrami operator and the Hodge Laplacian extend to Riemannian orbifolds so it is natural to extend many questions from the spectral theory of manifolds to orbifolds. This paper will be concerned with inverse spectral problems for the spectrum of the Hodge Laplacian on
p
𝑝
p
italic_p
-forms, which we refer to as the
p
𝑝
p
italic_p
-spectrum. We will say that two closed Riemannian orbifolds are
p
𝑝
p
italic_p
-
isospectral
if their Hodge Laplacians acting on
p
𝑝
p
italic_p
-forms are isospectral. In particular,
0
0
-isospectrality means that the Laplace-Beltrami operators are isospectral.
We will focus on both negative results–what properties of orbifolds cannot be detected by the
p
𝑝
p
italic_p
-spectra, and positive results–what properties of orbifolds or manifolds can be heard by the
p
𝑝
p
italic_p
-spectra for various
p
𝑝
p
italic_p
. Because the possible presence of singular points is a defining characteristic of the class of orbifolds, we will be particularly interested in the question “Can one hear the singularities of an orbifold in the
p
𝑝
p
italic_p
-spectrum?” More precisely, one asks for various values of
p
𝑝
p
italic_p
:
(1)
Does the
p
𝑝
p
italic_p
-spectrum distinguish orbifolds with singularities from manifolds? If so, does the
p
𝑝
p
italic_p
-spectrum detect the topology and geometry of the set of singular points, including the isotropy types of singularities?
(2)
What other geometric or topological properties does the
p
𝑝
p
italic_p
-spectrum detect or fail to detect for orbifolds?
Many authors have addressed these questions for the spectrum of the Laplace-Beltrami operator (see, for example, the literature review in
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
and corresponding references). However, the question of whether the
0
0
-spectrum
always
distinguishes Riemannian orbifolds with singularities from Riemannian manifolds remains open. In the first part of this project,
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
, we showed that the heat invariants for the
0
0
-spectrum and the
1
1
1
1
-spectrum together can distinguish orbifolds from manifolds when the codimension of the singular set is less than or equal to three. In this paper, we will consider the inverse spectral problem for individual
p
𝑝
p
italic_p
-spectra, obtaining both positive and negative results.
1.1.
Main Results
We summarize our main results below.
As stating the results in full detail requires us to introduce various definitions and notation, we give an overview here and refer to the complete statements of the results (via citations in parentheses) that appear later in the paper.
First recall that orbifolds admit a natural stratification. In a connected orbifold, the collection of regular points forms a single stratum of full dimension, while the singular set is a union of lower-dimensional strata. By the
dimension
m
𝑚
m
italic_m
of the singular set, we mean the maximum dimension of the singular strata. The volume of the singular set is then understood to be its
m
𝑚
m
italic_m
-dimensional Hausdorff measure.
1.1.1.
Results for arbitrary
p
𝑝
p
italic_p
-spectra.
Our results refer to the combinatorial Krawtchouk polynomials
K
p
d
subscript
superscript
𝐾
𝑑
𝑝
K^{d}_{p}
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT
; see subsection
2.3
for the definition. These polynomials depend on a positive integer parameter
d
𝑑
d
italic_d
and a parameter
p
𝑝
p
italic_p
lying in
{
0
,
…
,
d
}
0
…
𝑑
\{0,\dots,d\}
{ 0 , … , italic_d }
. There is a large literature on the zeros of these polynomials (e.g., see
[
CS90
,
KL96
]
).
The first item in Result
1.1
below is motivated by and applies the work of Roberto Miatello and Juan Pablo Rossetti
[
MR01
]
, where the Krawtchouk polynomials were used to construct
p
𝑝
p
italic_p
-isospectral Bieberbach manifolds.
Result 1.1
.
Let
𝒪
⁢
r
⁢
b
k
d
𝒪
𝑟
subscript
superscript
𝑏
𝑑
𝑘
{\mathcal{O}rb}^{d}_{k}
caligraphic_O italic_r italic_b start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
denote the class of all closed
d
𝑑
d
italic_d
-dimensional Riemannian orbifolds with singular set of codimension
k
𝑘
k
italic_k
.
(1)
If
k
∈
{
1
,
…
,
d
−
1
}
𝑘
1
…
𝑑
1
k\in\{1,\dots,d-1\}
italic_k ∈ { 1 , … , italic_d - 1 }
is a zero of the Krawtchouk polynomial
K
p
d
subscript
superscript
𝐾
𝑑
𝑝
K^{d}_{p}
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT
, then there exists a
d
𝑑
d
italic_d
-dimensional flat orbifold
𝒪
∈
𝒪
⁢
r
⁢
b
k
d
𝒪
𝒪
𝑟
subscript
superscript
𝑏
𝑑
𝑘
{\mathcal{O}}\in{\mathcal{O}rb}^{d}_{k}
caligraphic_O ∈ caligraphic_O italic_r italic_b start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
and a Bieberbach manifold
M
𝑀
M
italic_M
such that
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is
p
𝑝
p
italic_p
-isospectral to
M
𝑀
M
italic_M
. Moreover there exist families of mutually isospectral flat orbifolds and manifolds some of which are orientable and others not. (See Proposition
3.5
.)
(2)
In contrast, if
k
𝑘
k
italic_k
is odd and
K
p
d
⁢
(
k
)
≠
0
subscript
superscript
𝐾
𝑑
𝑝
𝑘
0
K^{d}_{p}(k)\neq 0
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_k ) ≠ 0
, then the
p
𝑝
p
italic_p
-spectrum determines the volume of the singular set of each orbifold in
𝒪
⁢
r
⁢
b
k
d
𝒪
𝑟
subscript
superscript
𝑏
𝑑
𝑘
{\mathcal{O}rb}^{d}_{k}
caligraphic_O italic_r italic_b start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
. In particular, the
p
𝑝
p
italic_p
-spectrum distinguishes orbifolds in
𝒪
⁢
r
⁢
b
k
d
𝒪
𝑟
subscript
superscript
𝑏
𝑑
𝑘
{\mathcal{O}rb}^{d}_{k}
caligraphic_O italic_r italic_b start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
from closed Riemannian manifolds. (See Theorem
4.4
.)
The first item in Result
1.1
yields many examples of Riemannian orbifolds that are
p
𝑝
p
italic_p
-isospectral to manifolds for various
p
≠
0
𝑝
0
p\neq 0
italic_p ≠ 0
, including examples that are simultaneously
p
𝑝
p
italic_p
-isospectral for all odd values of
p
𝑝
p
italic_p
. Moreover, the codimension of the singular sets in the various examples can have either even or odd parity. To our knowledge, the only previously known examples
[
GR03
]
of isospectralities between orbifolds with singularities and manifolds were in the special case that
d
𝑑
d
italic_d
is even and
p
=
d
2
𝑝
𝑑
2
p=\frac{d}{2}
italic_p = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
. See the discussion
1.1.3
below concerning isospectrality in the middle degree.
Consider the case of orbifolds
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
with singular set of codimension one. Result
1.1
, together with an examination of the zeros of the Krawtchouk polynomials, says in this case that the
p
𝑝
p
italic_p
-spectrum determines the volume of the singular set unless the dimension
d
𝑑
d
italic_d
of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is even and
p
=
d
2
𝑝
𝑑
2
p=\frac{d}{2}
italic_p = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
. Specializing a little further, suppose that
all
the singular strata have codimension one. The underlying space of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is then a Riemannian manifold
M
𝑀
M
italic_M
with boundary; the singular set of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
(which consists of what are called “reflector edges”) corresponds to the manifold boundary. Moreover, the
p
𝑝
p
italic_p
-spectrum of the orbifold coincides with the
p
𝑝
p
italic_p
-spectrum of
M
𝑀
M
italic_M
with absolute boundary conditions (Neumann boundary conditions if
p
=
0
𝑝
0
p=0
italic_p = 0
.) (See, e.g., Remark 3.16 of
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
.) Result
1.1
coincides in this special case with the well-known consequence of the heat invariants stating that, except when the dimension
d
𝑑
d
italic_d
is even and
p
=
d
2
𝑝
𝑑
2
p=\frac{d}{2}
italic_p = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
, the
p
𝑝
p
italic_p
-spectrum of a compact Riemannian manifold determines the volume of the boundary.
For
p
=
0
𝑝
0
p=0
italic_p = 0
, the Krawtchouk polynomial has no zeros, so Result
1.1
says that if the singular set has odd codimension, its volume is determined by the
0
0
-spectrum, i.e., by the spectrum of the Laplacian on functions. This fact can also be seen as an immediate consequence of the heat invariants for the 0-spectrum of orbifolds given in
[
DGGW08
]
. Moreover,
[
DGGW08
, Theorem 5.1]
says that an orbifold that contains at least one singular stratum of odd codimension cannot be 0-isospectral to a manifold, even if the full singular set has even codimension.
Our proof of the second item in Result
1.1
uses a new spectral invariant for the
p
𝑝
p
italic_p
-spectrum of orbifolds that we introduce in Notation
4.1
and Proposition
4.3
. A necessary (but not sufficient) condition for an orbifold to be
p
𝑝
p
italic_p
-isospsectral to a manifold is that this invariant vanishes. The expression for the invariant is somewhat simpler to work with when
p
=
1
𝑝
1
p=1
italic_p = 1
than for higher
p
𝑝
p
italic_p
and enables us to obtain weak – but in some cases sharp – analogues for 1-forms of the result
[
DGGW08
, Theorem 5.1]
described in the previous paragraph. We discuss these and other results for the 1-spectrum next.
1.1.2.
Results for the
1
1
1
1
-spectrum.
We obtain the following positive results for the
1
1
1
1
-spectrum for orbifolds of arbitrary dimension
d
𝑑
d
italic_d
(see Theorem
4.7
.) We also show that some of the results below are sharp.
Result 1.2
.
Let
𝒪
𝒪
\mathcal{O}
caligraphic_O
be a closed Riemannian orbifold of dimension
d
𝑑
d
italic_d
.
(1)
If
𝒪
𝒪
\mathcal{O}
caligraphic_O
contains at least one primary singular stratum of odd codimension
k
<
d
2
𝑘
𝑑
2
k<\frac{d}{2}
italic_k < divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
, then
𝒪
𝒪
\mathcal{O}
caligraphic_O
cannot be 1-isospectral to any closed Riemannian manifold.
(2)
If
𝒪
𝒪
\mathcal{O}
caligraphic_O
contains at least one singular stratum of codimension
k
<
d
2
𝑘
𝑑
2
k<\frac{d}{2}
italic_k < divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
, then
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
cannot be
1
1
1
1
-isospectral to any closed Riemannian manifold
M
𝑀
M
italic_M
such that
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
have isometric infinite homogeneous Riemannian covers. If in addition
𝒪
𝒪
\mathcal{O}
caligraphic_O
is good, then
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
cannot be
1
1
1
1
-isospectral to any closed Riemannian manifold
M
𝑀
M
italic_M
such that
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
have finite
1
1
1
1
-isospectral Riemannian covers.
(3)
For
d
𝑑
d
italic_d
even, both statements remain true when
k
=
d
2
𝑘
𝑑
2
k=\frac{d}{2}
italic_k = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
provided at least one stratum of codimension
k
𝑘
k
italic_k
has isotropy group of order at least three.
(4)
An element of
𝒪
⁢
r
⁢
b
k
d
𝒪
𝑟
subscript
superscript
𝑏
𝑑
𝑘
{\mathcal{O}rb}^{d}_{k}
caligraphic_O italic_r italic_b start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
with
k
𝑘
k
italic_k
odd can be 1-isospectral to a Riemannian manifold only if
d
𝑑
d
italic_d
is even and
k
=
d
2
𝑘
𝑑
2
k=\frac{d}{2}
italic_k = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
.
The conditions imposed on the codimension in the first two items of Result
1.2
are sharp at least for all even-dimensional orbifolds, and the assumption on the isotropy order in the third item cannot be removed. Indeed, when
d
𝑑
d
italic_d
is even, the first item in Result
1.1
allows one to construct a
d
𝑑
d
italic_d
-dimensional orbifold
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
with singular set of codimension
d
2
𝑑
2
\frac{d}{2}
divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
and a manifold
M
𝑀
M
italic_M
such that
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
and
M
𝑀
M
italic_M
are
p
𝑝
p
italic_p
-isospectral for all odd
p
𝑝
p
italic_p
, in particular for
p
=
1
𝑝
1
p=1
italic_p = 1
. (See Example
3.6
and Remark
2.10
, part 5.)
Item
1
of Result
1.2
is the weak analogue for the
1
1
1
1
-spectrum of
[
DGGW08
, Theorem 5.1]
, and
Item
2
of Result
1.2
gives weak analogues for
1
1
1
1
-forms of results for functions from
[
GR03
]
and its errata
[
GR21
]
and
[
Sut10
, Theorem 1.2]
.
1.1.3.
Results for the middle-degree spectrum
As discussed in
[
GR03
]
and its errata
[
GR21
]
, the middle degree
p
=
d
2
𝑝
𝑑
2
p=\frac{d}{2}
italic_p = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
Hodge spectrum of even-dimensional Riemannian manifolds, or more generally orbifolds, contains less information than the other spectra due to Hodge duality. This weakness of the middle-degree spectrum is also apparent in Result
1.1
: when
p
=
d
2
𝑝
𝑑
2
p=\frac{d}{2}
italic_p = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
, the Krawtchouk polynomial
K
p
d
⁢
(
k
)
=
0
superscript
subscript
𝐾
𝑝
𝑑
𝑘
0
K_{p}^{d}(k)=0
italic_K start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ( italic_k ) = 0
for every odd integer
k
𝑘
k
italic_k
in the interval
[
1
,
d
−
1
]
1
𝑑
1
[1,d-1]
[ 1 , italic_d - 1 ]
; Krawtchouk polynomials for other values of
p
𝑝
p
italic_p
have far fewer integer zeros.
Result 1.3
.
We exhibit a family of five
1
1
1
1
-isospectral flat 2-orbifolds (none of which are
0
0
-isospectral) that have different types of singularities. (See Example
3.9
.)
(1)
One can be viewed as a Euclidean square with absolute boundary conditions.
(2)
The underlying spaces of the various orbifolds include a sphere, a projective plane, and disks.
(3)
Some have reflector edges of various lengths while another has only cone points. Thus this family contains locally orientable and non-locally orientable orbifolds, in contrast to a result from
[
RS20
]
showing that this cannot happen with
0
0
-isospectral orbifolds. (See Remark
2.2
for the notion of local orientability of orbifolds.)
Note that a pair of 1-isospectral 2-orbifolds, one locally orientable and one not, were already constructed in
[
GR03
]
. See Example
3.8
for details. Also, in contrast to these five 1-isospectral 2-orbifolds which are not 0-isospectral, in
[
RSW08
]
the authors give examples of
3
3
3
3
-orbifolds that are
0
0
-isospectral and are not
1
1
1
1
-isospectral (see Remark
4.5
).
1.2.
Plan of the paper.
This paper is organized as follows: Section 2 recalls the relevant definitions, notation, and results from
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
, and the Krawtchouk polynomials that will be used throughout. Section 3 contains proofs of all the negative inverse spectral results; Section 4 contains proofs of all the positive inverse spectral results.
2.
Preliminaries
We begin this section by recalling the definition and some basic properties of orbifolds. See
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
or the references therein for more detail. We will then review results from
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
addressing heat asymptotics for the Hodge Laplacian on
p
𝑝
p
italic_p
-forms for orbifolds. In the final subsection, we will recall the definition and some properties of Krawtchouk polynomials and explore their link to the heat invariants.
2.1.
Notation
Here, we define the notation needed for this paper from
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
.
Definition 2.1
.
For a connected open subset
U
⊆
X
𝑈
𝑋
U\subseteq X
italic_U ⊆ italic_X
, an
orbifold chart
(of dimension
d
𝑑
d
italic_d
) over
U
𝑈
U
italic_U
is a triple
(
U
~
,
G
U
,
π
U
)
normal-~
𝑈
subscript
𝐺
𝑈
subscript
𝜋
𝑈
(\widetilde{U},G_{U},\pi_{U})
( over~ start_ARG italic_U end_ARG , italic_G start_POSTSUBSCRIPT italic_U end_POSTSUBSCRIPT , italic_π start_POSTSUBSCRIPT italic_U end_POSTSUBSCRIPT )
where
U
~
⊆
ℝ
d
normal-~
𝑈
superscript
ℝ
𝑑
\widetilde{U}\subseteq\mathbb{R}^{d}
over~ start_ARG italic_U end_ARG ⊆ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
is a connected open subset,
G
U
subscript
𝐺
𝑈
G_{U}
italic_G start_POSTSUBSCRIPT italic_U end_POSTSUBSCRIPT
is a finite group acting on
U
~
normal-~
𝑈
\widetilde{U}
over~ start_ARG italic_U end_ARG
effectively and by diffeomorphisms, and
π
U
:
U
~
→
X
normal-:
subscript
𝜋
𝑈
normal-→
normal-~
𝑈
𝑋
\pi_{U}\colon\widetilde{U}\to X
italic_π start_POSTSUBSCRIPT italic_U end_POSTSUBSCRIPT : over~ start_ARG italic_U end_ARG → italic_X
is a map inducing a homeomorphism
U
~
/
G
→
≅
U
normal-→
normal-~
𝑈
𝐺
𝑈
\widetilde{U}/G\xrightarrow{\cong}U
over~ start_ARG italic_U end_ARG / italic_G start_ARROW over≅ → end_ARROW italic_U
.
An
orbifold
of dimension
d
𝑑
d
italic_d
is a second countable Hausdorff topological space together with a maximal atlas of
d
𝑑
d
italic_d
-dimensional orbifold coordinate charts. See, for example, Definition 2.1 of
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
for the notion of compatibility of orbifold charts.
Remark 2.2
.
While manifolds are always locally orientable, an orbifold is locally orientable if and only if the isotropy group at every point consists of orientation-preserving transformations, i.e., it is a subgroup of
S
⁢
O
⁢
(
d
)
𝑆
𝑂
𝑑
SO(d)
italic_S italic_O ( italic_d )
. Global orientability of an orbifold further requires that the local charts can be compatibly oriented. As in the manifold case, global orientability is equivalent to the existence of a nowhere vanishing continuous
d
𝑑
d
italic_d
-form.
Definition 2.3
.
We define the isotropy type of
x
𝑥
x
italic_x
as follows: A chart
(
U
~
,
G
U
,
π
U
)
normal-~
𝑈
subscript
𝐺
𝑈
subscript
𝜋
𝑈
(\widetilde{U},G_{U},\pi_{U})
( over~ start_ARG italic_U end_ARG , italic_G start_POSTSUBSCRIPT italic_U end_POSTSUBSCRIPT , italic_π start_POSTSUBSCRIPT italic_U end_POSTSUBSCRIPT )
about
x
𝑥
x
italic_x
defines a smooth action of
G
U
subscript
𝐺
𝑈
G_{U}
italic_G start_POSTSUBSCRIPT italic_U end_POSTSUBSCRIPT
on
U
~
⊂
ℝ
d
normal-~
𝑈
superscript
ℝ
𝑑
\widetilde{U}\subset\mathbb{R}^{d}
over~ start_ARG italic_U end_ARG ⊂ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
. Fix a lift
x
~
∈
U
~
normal-~
𝑥
normal-~
𝑈
\widetilde{x}\in\widetilde{U}
over~ start_ARG italic_x end_ARG ∈ over~ start_ARG italic_U end_ARG
of
x
𝑥
x
italic_x
and let
Iso
⁡
(
x
~
)
normal-Iso
normal-~
𝑥
{\operatorname{{Iso}}}(\widetilde{x})
roman_Iso ( over~ start_ARG italic_x end_ARG )
be the isotropy subgroup of
G
U
subscript
𝐺
𝑈
G_{U}
italic_G start_POSTSUBSCRIPT italic_U end_POSTSUBSCRIPT
at
x
~
normal-~
𝑥
\widetilde{x}
over~ start_ARG italic_x end_ARG
. The map
γ
↦
d
⁢
γ
x
~
∈
End
⁡
(
T
x
~
⁢
U
~
)
maps-to
𝛾
𝑑
subscript
𝛾
normal-~
𝑥
normal-End
subscript
𝑇
normal-~
𝑥
normal-~
𝑈
\gamma\mapsto d\gamma_{\widetilde{x}}\in\operatorname{End}(T_{\widetilde{x}}%
\widetilde{U})
italic_γ ↦ italic_d italic_γ start_POSTSUBSCRIPT over~ start_ARG italic_x end_ARG end_POSTSUBSCRIPT ∈ roman_End ( italic_T start_POSTSUBSCRIPT over~ start_ARG italic_x end_ARG end_POSTSUBSCRIPT over~ start_ARG italic_U end_ARG )
, defines an injective linear representation of
Iso
⁡
(
x
~
)
normal-Iso
normal-~
𝑥
{\operatorname{{Iso}}}(\widetilde{x})
roman_Iso ( over~ start_ARG italic_x end_ARG )
. Every finite-dimensional linear representation of a compact Lie group is equivalent to an orthogonal representation, unique up to orthogonal equivalence. Thus
Iso
⁡
(
x
~
)
normal-Iso
normal-~
𝑥
{\operatorname{{Iso}}}(\widetilde{x})
roman_Iso ( over~ start_ARG italic_x end_ARG )
can be viewed as a subgroup of the orthogonal group
O
⁢
(
d
)
𝑂
𝑑
O(d)
italic_O ( italic_d )
, unique up to conjugacy. The conjugacy class of
Iso
⁡
(
x
~
)
normal-Iso
normal-~
𝑥
{\operatorname{{Iso}}}(\widetilde{x})
roman_Iso ( over~ start_ARG italic_x end_ARG )
in
O
⁢
(
d
)
𝑂
𝑑
O(d)
italic_O ( italic_d )
is independent both of the choice of the lift
x
~
normal-~
𝑥
\widetilde{x}
over~ start_ARG italic_x end_ARG
of
x
𝑥
x
italic_x
in
U
~
normal-~
𝑈
\widetilde{U}
over~ start_ARG italic_U end_ARG
and of the choice of chart
(
U
~
,
G
U
,
π
U
)
normal-~
𝑈
subscript
𝐺
𝑈
subscript
𝜋
𝑈
(\widetilde{U},G_{U},\pi_{U})
( over~ start_ARG italic_U end_ARG , italic_G start_POSTSUBSCRIPT italic_U end_POSTSUBSCRIPT , italic_π start_POSTSUBSCRIPT italic_U end_POSTSUBSCRIPT )
and is called the
isotropy type
of
x
𝑥
x
italic_x
.
Next we recall the definition of the singular stratification. See, for example, Section 2.1 of
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
for more detail.
Definition 2.4
.
Let
𝒪
𝒪
\mathcal{O}
caligraphic_O
be an orbifold of dimension
d
𝑑
d
italic_d
.
(1)
Every orbifold admits a stratification, as follows. We define an equivalence relation on
𝒪
𝒪
\mathcal{O}
caligraphic_O
by saying that two points in
𝒪
𝒪
\mathcal{O}
caligraphic_O
are
isotropy equivalent
if they have the same isotropy type. The connected components of the isotropy equivalence classes of
𝒪
𝒪
\mathcal{O}
caligraphic_O
form a smooth stratification of
𝒪
𝒪
\mathcal{O}
caligraphic_O
. When the corresponding isotropy type is non-trivial these strata are called
singular strata
. Note that in the literature, the requirement that a singular stratum be connected is sometimes dropped.
(2)
Let
N
𝑁
N
italic_N
be a singular stratum in
𝒪
𝒪
\mathcal{O}
caligraphic_O
and let
Iso
⁡
(
N
)
<
O
⁢
(
d
)
Iso
𝑁
𝑂
𝑑
\operatorname{Iso}(N)<O(d)
roman_Iso ( italic_N ) < italic_O ( italic_d )
denote a representative of its isotropy type. We will refer to
Iso
⁡
(
N
)
Iso
𝑁
\operatorname{Iso}(N)
roman_Iso ( italic_N )
as the
isotropy group
of the stratum.
(3)
We denote by
Iso
max
⁡
(
N
)
superscript
Iso
max
𝑁
\operatorname{Iso}^{\rm max}(N)
roman_Iso start_POSTSUPERSCRIPT roman_max end_POSTSUPERSCRIPT ( italic_N )
the set of all elements
γ
∈
Iso
⁡
(
N
)
𝛾
Iso
𝑁
\gamma\in\operatorname{Iso}(N)
italic_γ ∈ roman_Iso ( italic_N )
such that the dimension of the
1
1
1
1
-eigenspace of
γ
𝛾
\gamma
italic_γ
is equal to the dimension of
N
𝑁
N
italic_N
. We say that a stratum
N
𝑁
N
italic_N
is
primary
if
Iso
max
⁡
(
N
)
superscript
Iso
max
𝑁
\operatorname{Iso}^{\rm max}(N)
roman_Iso start_POSTSUPERSCRIPT roman_max end_POSTSUPERSCRIPT ( italic_N )
is non-empty.
2.2.
Differential forms, the Hodge Laplacian, and the Heat asymptotics for differential
p
𝑝
p
italic_p
-forms on orbifolds.
Differential forms on orbifolds and the corresponding Hodge Laplacian on
p
𝑝
p
italic_p
-forms can be defined as in Section 2.2 of
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
. The Hodge Laplacian can be defined on the space of differential
p
𝑝
p
italic_p
-forms whose components are square-integrable, denoted by
L
p
2
⁢
(
𝒪
)
,
subscript
superscript
𝐿
2
𝑝
𝒪
L^{2}_{p}({\mathcal{O}}),
italic_L start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( caligraphic_O ) ,
where it is essentially self-adjoint and has a discrete spectrum. We denote the closure of this operator by
Δ
p
.
superscript
Δ
𝑝
\Delta^{p}.
roman_Δ start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT .
We apply the spectral theorem to this operator and denote its eigenvalues by
0
≤
λ
1
(
p
)
≤
λ
2
(
p
)
≤
…
→
+
∞
0
subscript
superscript
𝜆
𝑝
1
subscript
superscript
𝜆
𝑝
2
…
→
0\leq\lambda^{(p)}_{1}\leq\lambda^{(p)}_{2}\leq\dots\to+\infty
0 ≤ italic_λ start_POSTSUPERSCRIPT ( italic_p ) end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ≤ italic_λ start_POSTSUPERSCRIPT ( italic_p ) end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ≤ … → + ∞
, with associated smooth eigenforms, denoted by
(
φ
i
)
i
subscript
subscript
𝜑
𝑖
𝑖
(\varphi_{i})_{i}
( italic_φ start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ) start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT
, which form an orthonormal basis of
L
p
2
⁢
(
𝒪
)
superscript
subscript
𝐿
𝑝
2
𝒪
L_{p}^{2}({\mathcal{O}})
italic_L start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( caligraphic_O )
.
Recall if
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
has empty singular set then
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is a closed Riemannian manifold,
M
𝑀
M
italic_M
, and the heat trace has a small-time asymptotic expansion
(1)
∑
j
=
0
∞
e
−
λ
j
(
p
)
⁢
t
∼
t
→
0
+
(
4
⁢
π
⁢
t
)
−
d
/
2
⁢
∑
i
=
0
∞
a
i
p
⁢
(
M
)
⁢
t
i
,
subscript
similar-to
→
𝑡
superscript
0
superscript
subscript
𝑗
0
superscript
𝑒
superscript
subscript
𝜆
𝑗
𝑝
𝑡
superscript
4
𝜋
𝑡
𝑑
2
superscript
subscript
𝑖
0
subscript
superscript
𝑎
𝑝
𝑖
𝑀
superscript
𝑡
𝑖
\sum_{j=0}^{\infty}\,e^{-\lambda_{j}^{(p)}t}\sim_{t\to 0^{+}}(4\pi t)^{-d/2}%
\sum_{i=0}^{\infty}a^{p}_{i}(M)t^{i},
∑ start_POSTSUBSCRIPT italic_j = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∞ end_POSTSUPERSCRIPT italic_e start_POSTSUPERSCRIPT - italic_λ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ( italic_p ) end_POSTSUPERSCRIPT italic_t end_POSTSUPERSCRIPT ∼ start_POSTSUBSCRIPT italic_t → 0 start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT end_POSTSUBSCRIPT ( 4 italic_π italic_t ) start_POSTSUPERSCRIPT - italic_d / 2 end_POSTSUPERSCRIPT ∑ start_POSTSUBSCRIPT italic_i = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∞ end_POSTSUPERSCRIPT italic_a start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT ( italic_M ) italic_t start_POSTSUPERSCRIPT italic_i end_POSTSUPERSCRIPT ,
where the
a
j
p
subscript
superscript
𝑎
𝑝
𝑗
a^{p}_{j}
italic_a start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT
, the so-called heat invariants, are integrals over
M
𝑀
M
italic_M
of universal polynomials in the curvature and its covariant derivatives.
(See, for example,
[
Pat70
]
and references therein.)
In Section 3 of
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
, the authors constructed the heat kernel and the heat trace for the orbifold case. The universal expressions defining the
a
j
p
superscript
subscript
𝑎
𝑗
𝑝
a_{j}^{p}
italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT
make sense on Riemannian orbifolds as well as on manifolds. We will use the same notation
a
j
p
superscript
subscript
𝑎
𝑗
𝑝
a_{j}^{p}
italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT
for the extension of the function
a
j
p
superscript
subscript
𝑎
𝑗
𝑝
a_{j}^{p}
italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT
to the class of all closed Riemannian orbifolds.
Notation and Remarks 2.5
.
Let
γ
∈
O
⁢
(
d
)
𝛾
𝑂
𝑑
\gamma\in O(d)
italic_γ ∈ italic_O ( italic_d )
.
(1)
We denote by
tr
p
⁡
(
γ
)
subscript
tr
𝑝
𝛾
\operatorname{tr}_{p}(\gamma)
roman_tr start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_γ )
the trace of the natural action of
γ
𝛾
\gamma
italic_γ
on the space
∧
p
(
ℝ
d
)
superscript
𝑝
superscript
ℝ
𝑑
\wedge^{p}(\mathbb{R}^{d})
∧ start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT )
of alternating
p
𝑝
p
italic_p
-tensors.
(2)
Let
A
γ
=
γ
|
E
1
(
γ
)
⟂
A_{\gamma}=\gamma_{|E_{1}(\gamma)^{\perp}}
italic_A start_POSTSUBSCRIPT italic_γ end_POSTSUBSCRIPT = italic_γ start_POSTSUBSCRIPT | italic_E start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( italic_γ ) start_POSTSUPERSCRIPT ⟂ end_POSTSUPERSCRIPT end_POSTSUBSCRIPT
, where
E
1
⁢
(
γ
)
<
O
⁢
(
d
)
subscript
𝐸
1
𝛾
𝑂
𝑑
E_{1}(\gamma)<O(d)
italic_E start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( italic_γ ) < italic_O ( italic_d )
is the 1-eigenspace of
γ
𝛾
\gamma
italic_γ
.
Note that if
N
𝑁
N
italic_N
is a singular stratum of an orbifold
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
and
γ
∈
Iso
max
⁡
(
N
)
𝛾
superscript
Iso
max
𝑁
\gamma\in\operatorname{Iso}^{\rm max}(N)
italic_γ ∈ roman_Iso start_POSTSUPERSCRIPT roman_max end_POSTSUPERSCRIPT ( italic_N )
, then
dim
(
E
1
⁢
(
γ
)
)
=
dim
(
N
)
dimension
subscript
𝐸
1
𝛾
dimension
𝑁
\dim(E_{1}(\gamma))=\dim(N)
roman_dim ( italic_E start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( italic_γ ) ) = roman_dim ( italic_N )
where
dim
(
N
)
dimension
𝑁
\dim(N)
roman_dim ( italic_N )
is the dimension of
N
𝑁
N
italic_N
in
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
.
We recall the heat trace asymptotics and an explicit formula for some of the heat invariants using the previous notation.
Theorem 2.6
.
[Theorem 3.15,
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
] Let
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
be a closed
d
𝑑
d
italic_d
-dimensional Riemannian orbifold, let
p
∈
{
1
,
…
,
d
}
𝑝
1
normal-…
𝑑
p\in\{1,\dots,d\}
italic_p ∈ { 1 , … , italic_d }
and let
0
≤
λ
1
(
p
)
≤
λ
2
(
p
)
≤
…
→
+
∞
0
superscript
subscript
𝜆
1
𝑝
superscript
subscript
𝜆
2
𝑝
normal-…
normal-→
0\leq\lambda_{1}^{(p)}\leq\lambda_{2}^{(p)}\leq\dots\to+\infty
0 ≤ italic_λ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ( italic_p ) end_POSTSUPERSCRIPT ≤ italic_λ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ( italic_p ) end_POSTSUPERSCRIPT ≤ … → + ∞
be the spectrum of the Hodge Laplacian acting on smooth
p
𝑝
p
italic_p
-forms on
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
. The heat trace yields an asymptotic expansion as
t
→
0
+
normal-→
𝑡
superscript
0
t\to 0^{+}
italic_t → 0 start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT
given by
(2)
∑
j
=
1
∞
e
−
λ
j
(
p
)
⁢
t
∼
t
→
0
+
I
0
p
⁢
(
t
)
+
∑
N
∈
P
⁢
S
⁢
(
𝒪
)
I
N
p
⁢
(
t
)
|
Iso
⁡
(
N
)
|
,
subscript
similar-to
→
𝑡
superscript
0
superscript
subscript
𝑗
1
superscript
𝑒
superscript
subscript
𝜆
𝑗
𝑝
𝑡
superscript
subscript
𝐼
0
𝑝
𝑡
subscript
𝑁
𝑃
𝑆
𝒪
superscript
subscript
𝐼
𝑁
𝑝
𝑡
Iso
𝑁
\sum_{j=1}^{\infty}\,e^{-\lambda_{j}^{(p)}t}\,\sim_{t\to 0^{+}}\,I_{0}^{p}(t)+%
\sum_{N\in PS({\mathcal{O}})}\,\frac{I_{N}^{p}(t)}{|\operatorname{Iso}(N)|},
∑ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∞ end_POSTSUPERSCRIPT italic_e start_POSTSUPERSCRIPT - italic_λ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ( italic_p ) end_POSTSUPERSCRIPT italic_t end_POSTSUPERSCRIPT ∼ start_POSTSUBSCRIPT italic_t → 0 start_POSTSUPERSCRIPT + end_POSTSUPERSCRIPT end_POSTSUBSCRIPT italic_I start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_t ) + ∑ start_POSTSUBSCRIPT italic_N ∈ italic_P italic_S ( caligraphic_O ) end_POSTSUBSCRIPT divide start_ARG italic_I start_POSTSUBSCRIPT italic_N end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_t ) end_ARG start_ARG | roman_Iso ( italic_N ) | end_ARG ,
where
P
⁢
S
⁢
(
𝒪
)
𝑃
𝑆
𝒪
PS({\mathcal{O}})
italic_P italic_S ( caligraphic_O )
is the set of all primary singular
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
-strata,
|
Iso
⁡
(
N
)
|
normal-Iso
𝑁
|\operatorname{Iso}(N)|
| roman_Iso ( italic_N ) |
is the order of the isotropy group of
N
𝑁
N
italic_N
. Here
(3)
I
0
p
⁢
(
t
)
:=
(
4
⁢
π
⁢
t
)
−
d
/
2
⁢
∑
k
=
0
∞
a
k
p
⁢
(
𝒪
)
⁢
t
k
assign
superscript
subscript
𝐼
0
𝑝
𝑡
superscript
4
𝜋
𝑡
𝑑
2
superscript
subscript
𝑘
0
superscript
subscript
𝑎
𝑘
𝑝
𝒪
superscript
𝑡
𝑘
I_{0}^{p}(t):=(4\pi t)^{-d/2}\sum_{k=0}^{\infty}\,a_{k}^{p}({\mathcal{O}})t^{k}
italic_I start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_t ) := ( 4 italic_π italic_t ) start_POSTSUPERSCRIPT - italic_d / 2 end_POSTSUPERSCRIPT ∑ start_POSTSUBSCRIPT italic_k = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∞ end_POSTSUPERSCRIPT italic_a start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O ) italic_t start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT
with
a
k
p
⁢
(
𝒪
)
superscript
subscript
𝑎
𝑘
𝑝
𝒪
a_{k}^{p}({\mathcal{O}})
italic_a start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O )
given as above, and for
N
∈
P
⁢
S
⁢
(
𝒪
)
𝑁
𝑃
𝑆
𝒪
N\in PS({\mathcal{O}})
italic_N ∈ italic_P italic_S ( caligraphic_O )
,
(4)
I
N
p
⁢
(
t
)
:=
(
4
⁢
π
⁢
t
)
−
dim
(
N
)
/
2
⁢
∑
k
=
0
∞
b
k
p
⁢
(
N
)
⁢
t
k
.
assign
superscript
subscript
𝐼
𝑁
𝑝
𝑡
superscript
4
𝜋
𝑡
dimension
𝑁
2
superscript
subscript
𝑘
0
superscript
subscript
𝑏
𝑘
𝑝
𝑁
superscript
𝑡
𝑘
I_{N}^{p}(t):=(4\pi t)^{-\dim(N)/2}\sum_{k=0}^{\infty}\,b_{k}^{p}(N)t^{k}.
italic_I start_POSTSUBSCRIPT italic_N end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_t ) := ( 4 italic_π italic_t ) start_POSTSUPERSCRIPT - roman_dim ( italic_N ) / 2 end_POSTSUPERSCRIPT ∑ start_POSTSUBSCRIPT italic_k = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∞ end_POSTSUPERSCRIPT italic_b start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_N ) italic_t start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT .
The coefficients
b
k
p
⁢
(
N
)
superscript
subscript
𝑏
𝑘
𝑝
𝑁
b_{k}^{p}(N)
italic_b start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_N )
are of the form
b
k
p
⁢
(
N
)
=
∑
γ
∈
Iso
max
⁡
(
N
)
∫
N
b
k
p
⁢
(
γ
,
x
)
⁢
𝑑
V
⁢
(
x
)
superscript
subscript
𝑏
𝑘
𝑝
𝑁
subscript
𝛾
superscript
Iso
max
𝑁
subscript
𝑁
superscript
subscript
𝑏
𝑘
𝑝
𝛾
𝑥
differential-d
𝑉
𝑥
b_{k}^{p}(N)=\sum_{\gamma\in\operatorname{Iso}^{\rm max}(N)}\,\int_{N}\,b_{k}^%
{p}(\gamma,x)\,dV(x)
italic_b start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_N ) = ∑ start_POSTSUBSCRIPT italic_γ ∈ roman_Iso start_POSTSUPERSCRIPT roman_max end_POSTSUPERSCRIPT ( italic_N ) end_POSTSUBSCRIPT ∫ start_POSTSUBSCRIPT italic_N end_POSTSUBSCRIPT italic_b start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_γ , italic_x ) italic_d italic_V ( italic_x )
where the
b
k
p
superscript
subscript
𝑏
𝑘
𝑝
b_{k}^{p}
italic_b start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT
are universal orthogonally invariant expressions in the germs of the Riemannian metric of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
at
x
𝑥
x
italic_x
and the action of
γ
𝛾
\gamma
italic_γ
.
In the notation of
2.5
, we have
(5)
b
0
p
⁢
(
N
)
=
∑
γ
∈
Iso
max
⁡
(
N
)
tr
p
⁡
(
γ
)
|
det
(
Id
codim
⁡
(
N
)
−
A
γ
)
|
.
superscript
subscript
𝑏
0
𝑝
𝑁
subscript
𝛾
superscript
Iso
max
𝑁
subscript
tr
𝑝
𝛾
subscript
Id
codim
𝑁
subscript
𝐴
𝛾
b_{0}^{p}(N)=\sum_{\gamma\in\operatorname{Iso}^{\rm max}(N)}\,\frac{%
\operatorname{tr}_{p}(\gamma)}{\lvert\det({\operatorname{{Id}}}_{\operatorname%
{codim}(N)}-A_{\gamma})\rvert}.
italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_N ) = ∑ start_POSTSUBSCRIPT italic_γ ∈ roman_Iso start_POSTSUPERSCRIPT roman_max end_POSTSUPERSCRIPT ( italic_N ) end_POSTSUBSCRIPT divide start_ARG roman_tr start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_γ ) end_ARG start_ARG | roman_det ( roman_Id start_POSTSUBSCRIPT roman_codim ( italic_N ) end_POSTSUBSCRIPT - italic_A start_POSTSUBSCRIPT italic_γ end_POSTSUBSCRIPT ) | end_ARG .
The asymptotic expansion (
2
) is of the form
(6)
(
4
⁢
π
⁢
t
)
−
d
/
2
⁢
∑
j
=
0
∞
c
j
p
⁢
(
𝒪
)
⁢
t
j
2
superscript
4
𝜋
𝑡
𝑑
2
superscript
subscript
𝑗
0
subscript
superscript
𝑐
𝑝
𝑗
𝒪
superscript
𝑡
𝑗
2
\displaystyle(4\pi t)^{-d/2}\sum_{j=0}^{\infty}\,c^{p}_{j}(\mathcal{O})\,t^{%
\frac{j}{2}}
( 4 italic_π italic_t ) start_POSTSUPERSCRIPT - italic_d / 2 end_POSTSUPERSCRIPT ∑ start_POSTSUBSCRIPT italic_j = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT ∞ end_POSTSUPERSCRIPT italic_c start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( caligraphic_O ) italic_t start_POSTSUPERSCRIPT divide start_ARG italic_j end_ARG start_ARG 2 end_ARG end_POSTSUPERSCRIPT
with
c
j
p
⁢
(
𝒪
)
∈
ℝ
subscript
superscript
𝑐
𝑝
𝑗
𝒪
ℝ
c^{p}_{j}(\mathcal{O})\in\mathbb{R}
italic_c start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( caligraphic_O ) ∈ blackboard_R
.
To analyze the contributions from the
b
k
p
⁢
(
N
)
superscript
subscript
𝑏
𝑘
𝑝
𝑁
b_{k}^{p}(N)
italic_b start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_N )
to the
c
j
p
⁢
(
𝒪
)
subscript
superscript
𝑐
𝑝
𝑗
𝒪
c^{p}_{j}(\mathcal{O})
italic_c start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ( caligraphic_O )
coefficients, we recall the following notation from Section 2 of
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
.
Notation and Remarks 2.7
.
For
γ
∈
O
⁢
(
d
)
𝛾
𝑂
𝑑
\gamma\in O(d)
italic_γ ∈ italic_O ( italic_d )
, we define the
eigenvalue type
of
γ
𝛾
\gamma
italic_γ
as follows: Let
r
𝑟
r
italic_r
be the dimension of the
(
−
1
)
1
(-1)
( - 1 )
-eigenspace of
γ
𝛾
\gamma
italic_γ
; in particular,
r
=
0
𝑟
0
r=0
italic_r = 0
if
−
1
1
-1
- 1
is not an eigenvalue. Let
e
±
i
⁢
θ
j
superscript
𝑒
plus-or-minus
𝑖
subscript
𝜃
𝑗
e^{\pm i\theta_{j}}
italic_e start_POSTSUPERSCRIPT ± italic_i italic_θ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT end_POSTSUPERSCRIPT
,
j
=
1
,
…
,
s
𝑗
1
normal-…
𝑠
j=1,\dots,s
italic_j = 1 , … , italic_s
be all the eigenvalues with non-trivial imaginary part, repeated according to multiplicity. Observe that the dimension of the
(
+
1
)
1
(+1)
( + 1 )
-eigenspace is then
d
−
2
⁢
s
−
r
𝑑
2
𝑠
𝑟
d-2s-r
italic_d - 2 italic_s - italic_r
. The expression
E
⁢
(
θ
1
,
θ
2
,
…
,
θ
s
;
r
)
𝐸
subscript
𝜃
1
subscript
𝜃
2
normal-…
subscript
𝜃
𝑠
𝑟
E(\theta_{1},\theta_{2},\dots,\theta_{s};r)
italic_E ( italic_θ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_θ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , italic_θ start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT ; italic_r )
will be called the eigenvalue type of
γ
𝛾
\gamma
italic_γ
. When
r
=
0
𝑟
0
r=0
italic_r = 0
, respectively
s
=
0
𝑠
0
s=0
italic_s = 0
, we instead write
E
(
θ
1
,
θ
2
,
…
,
θ
s
;
)
E(\theta_{1},\theta_{2},\dots,\theta_{s};)
italic_E ( italic_θ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_θ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , italic_θ start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT ; )
, respectively
E
(
;
r
)
E(;r)
italic_E ( ; italic_r )
.
With this notation, we recall the following result, Proposition 4.3 of
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
, which will be needed in the subsequent sections for results involving the
1
1
1
1
-spectrum.
The result follows as the
1
1
1
1
-trace is the trace of the matrix representation of
γ
𝛾
\gamma
italic_γ
in
O
⁢
(
d
)
𝑂
𝑑
O(d)
italic_O ( italic_d )
(as in Definition
2.3
).
Proposition 2.8
.
[Proposition 4.3,
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
] Let
N
𝑁
N
italic_N
be a singular stratum of codimension
k
𝑘
k
italic_k
in the
d
𝑑
d
italic_d
-dimensional closed orbifold
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
. Suppose
γ
∈
Iso
max
⁡
(
N
)
𝛾
superscript
normal-Iso
normal-max
𝑁
\gamma\in\operatorname{Iso}^{\rm max}(N)
italic_γ ∈ roman_Iso start_POSTSUPERSCRIPT roman_max end_POSTSUPERSCRIPT ( italic_N )
has eigenvalue type
E
⁢
(
θ
1
,
θ
2
,
…
,
θ
s
;
r
)
𝐸
subscript
𝜃
1
subscript
𝜃
2
normal-…
subscript
𝜃
𝑠
𝑟
E(\theta_{1},\theta_{2},\dots,\theta_{s};r)
italic_E ( italic_θ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_θ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , italic_θ start_POSTSUBSCRIPT italic_s end_POSTSUBSCRIPT ; italic_r )
, using Notation
2.7
.
Then
(7)
b
0
1
⁢
(
γ
)
=
(
d
−
k
−
r
+
∑
j
=
1
s
2
⁢
cos
⁡
(
θ
j
)
)
⁢
(
2
−
k
⁢
∏
j
=
1
s
csc
2
⁡
(
θ
j
/
2
)
)
.
superscript
subscript
𝑏
0
1
𝛾
𝑑
𝑘
𝑟
superscript
subscript
𝑗
1
𝑠
2
subscript
𝜃
𝑗
superscript
2
𝑘
superscript
subscript
product
𝑗
1
𝑠
superscript
2
subscript
𝜃
𝑗
2
b_{0}^{1}(\gamma)=\left(d-k-r+\sum_{j=1}^{s}\,2\cos(\theta_{j})\right)\left(2^%
{-k}\prod_{j=1}^{s}\,\csc^{2}(\theta_{j}/2)\right).
italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT ( italic_γ ) = ( italic_d - italic_k - italic_r + ∑ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_s end_POSTSUPERSCRIPT 2 roman_cos ( italic_θ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT ) ) ( 2 start_POSTSUPERSCRIPT - italic_k end_POSTSUPERSCRIPT ∏ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_s end_POSTSUPERSCRIPT roman_csc start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( italic_θ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT / 2 ) ) .
Here we use the convention that when
s
=
0
𝑠
0
s=0
italic_s = 0
, we have
∏
j
=
1
s
csc
2
⁡
(
θ
j
/
2
)
=
1
superscript
subscript
product
𝑗
1
𝑠
superscript
2
subscript
𝜃
𝑗
2
1
\prod_{j=1}^{s}\,\csc^{2}(\theta_{j}/2)=1
∏ start_POSTSUBSCRIPT italic_j = 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_s end_POSTSUPERSCRIPT roman_csc start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ( italic_θ start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT / 2 ) = 1
.
2.3.
Krawtchouk polynomials and their role in heat invariants
The (binary) Krawtchouk polynomial of degree
p
𝑝
p
italic_p
is defined as
(8)
K
p
d
⁢
(
x
)
=
∑
j
=
0
p
(
−
1
)
j
⁢
(
x
j
)
⁢
(
d
−
x
p
−
j
)
.
subscript
superscript
𝐾
𝑑
𝑝
𝑥
superscript
subscript
𝑗
0
𝑝
superscript
1
𝑗
binomial
𝑥
𝑗
binomial
𝑑
𝑥
𝑝
𝑗
K^{d}_{p}(x)=\sum_{j=0}^{p}\,(-1)^{j}\,\binom{x}{j}\binom{d-x}{p-j}.
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_x ) = ∑ start_POSTSUBSCRIPT italic_j = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( - 1 ) start_POSTSUPERSCRIPT italic_j end_POSTSUPERSCRIPT ( FRACOP start_ARG italic_x end_ARG start_ARG italic_j end_ARG ) ( FRACOP start_ARG italic_d - italic_x end_ARG start_ARG italic_p - italic_j end_ARG ) .
In some settings, the Krawtchouk polynomials are related to the heat invariants. We give the following example that will be used later to prove Theorem
4.4
.
Example 2.9
.
Suppose
N
𝑁
N
italic_N
is a singular stratum of codimension
k
𝑘
k
italic_k
with isotropy group of order
2
2
2
2
. The generator
γ
𝛾
\gamma
italic_γ
of
Iso
⁡
(
N
)
normal-Iso
𝑁
{\operatorname{{Iso}}}(N)
roman_Iso ( italic_N )
must have eigenvalue type
E
(
;
k
)
E(;k)
italic_E ( ; italic_k )
, and thus
(9)
tr
p
⁡
(
γ
)
=
∑
j
=
0
p
(
−
1
)
j
⁢
(
k
j
)
⁢
(
d
−
k
p
−
j
)
subscript
tr
𝑝
𝛾
superscript
subscript
𝑗
0
𝑝
superscript
1
𝑗
binomial
𝑘
𝑗
binomial
𝑑
𝑘
𝑝
𝑗
\operatorname{tr}_{p}(\gamma)=\sum_{j=0}^{p}\,(-1)^{j}\,\binom{k}{j}\binom{d-k%
}{p-j}
roman_tr start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_γ ) = ∑ start_POSTSUBSCRIPT italic_j = 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( - 1 ) start_POSTSUPERSCRIPT italic_j end_POSTSUPERSCRIPT ( FRACOP start_ARG italic_k end_ARG start_ARG italic_j end_ARG ) ( FRACOP start_ARG italic_d - italic_k end_ARG start_ARG italic_p - italic_j end_ARG )
with the understanding that
(
m
n
)
=
0
binomial
𝑚
𝑛
0
\binom{m}{n}=0
( FRACOP start_ARG italic_m end_ARG start_ARG italic_n end_ARG ) = 0
when
n
>
m
𝑛
𝑚
n>m
italic_n > italic_m
.
By Theorem
2.6
equation (
5
) and equation (
9
), we have
(10)
b
0
p
⁢
(
N
)
=
vol
⁢
(
N
)
2
k
⁢
K
p
d
⁢
(
k
)
.
superscript
subscript
𝑏
0
𝑝
𝑁
vol
𝑁
superscript
2
𝑘
superscript
subscript
𝐾
𝑝
𝑑
𝑘
b_{0}^{p}(N)=\frac{{\rm vol}(N)}{2^{k}}K_{p}^{d}(k).
italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_N ) = divide start_ARG roman_vol ( italic_N ) end_ARG start_ARG 2 start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT end_ARG italic_K start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ( italic_k ) .
In particular, in the previous example,
b
0
p
⁢
(
N
)
superscript
subscript
𝑏
0
𝑝
𝑁
b_{0}^{p}(N)
italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_N )
vanishes if and only if the codimension
k
𝑘
k
italic_k
of
N
𝑁
N
italic_N
is a zero of the Krawtchouk polynomial
K
p
d
superscript
subscript
𝐾
𝑝
𝑑
K_{p}^{d}
italic_K start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
.
Remark 2.10
.
There is a large literature on the zeros of Krawtchouk polynomials (see, for example,
[
CS90
,
KL96
]
). We include a few elementary observations here:
(1)
K
0
d
⁢
(
k
)
=
1
subscript
superscript
𝐾
𝑑
0
𝑘
1
K^{d}_{0}(k)=1
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT ( italic_k ) = 1
and
K
d
d
⁢
(
k
)
=
(
−
1
)
k
subscript
superscript
𝐾
𝑑
𝑑
𝑘
superscript
1
𝑘
K^{d}_{d}(k)=(-1)^{k}
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ( italic_k ) = ( - 1 ) start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT
.
(2)
K
1
d
⁢
(
k
)
=
0
subscript
superscript
𝐾
𝑑
1
𝑘
0
K^{d}_{1}(k)=0
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ( italic_k ) = 0
if and only if
k
=
d
2
𝑘
𝑑
2
k=\frac{d}{2}
italic_k = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
.
(3)
K
2
d
⁢
(
k
)
=
0
subscript
superscript
𝐾
𝑑
2
𝑘
0
K^{d}_{2}(k)=0
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ( italic_k ) = 0
if and only if the dimension
d
=
n
2
𝑑
superscript
𝑛
2
d=n^{2}
italic_d = italic_n start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT
is a perfect square and
k
=
n
⁢
(
n
±
1
)
2
𝑘
𝑛
plus-or-minus
𝑛
1
2
k=\frac{n(n\pm 1)}{2}
italic_k = divide start_ARG italic_n ( italic_n ± 1 ) end_ARG start_ARG 2 end_ARG
. (For later use, we observe that if
4
|
n
conditional
4
𝑛
4|n
4 | italic_n
, then both zeros
n
⁢
(
n
±
1
)
2
𝑛
plus-or-minus
𝑛
1
2
\frac{n(n\pm 1)}{2}
divide start_ARG italic_n ( italic_n ± 1 ) end_ARG start_ARG 2 end_ARG
are even.)
(4)
When
d
𝑑
d
italic_d
is even and
p
=
d
2
𝑝
𝑑
2
p=\frac{d}{2}
italic_p = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
, we have
K
p
d
⁢
(
k
)
=
0
subscript
superscript
𝐾
𝑑
𝑝
𝑘
0
K^{d}_{p}(k)=0
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_k ) = 0
for all odd
k
𝑘
k
italic_k
, see
[
MR02
, Remark 3.14]
.
(5)
When
d
𝑑
d
italic_d
is even and
p
𝑝
p
italic_p
is odd, we have
K
p
d
⁢
(
d
2
)
=
0
subscript
superscript
𝐾
𝑑
𝑝
𝑑
2
0
K^{d}_{p}(\frac{d}{2})=0
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( divide start_ARG italic_d end_ARG start_ARG 2 end_ARG ) = 0
, see
[
MR02
, Remark 3.14]
.
(6)
It is remarked in
[
MR02
, Remark 3.14]
that
d
=
9
𝑑
9
d=9
italic_d = 9
is the lowest odd dimension for which some of the Krawtchouk polynomials
K
p
d
⁢
(
k
)
superscript
subscript
𝐾
𝑝
𝑑
𝑘
K_{p}^{d}(k)
italic_K start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ( italic_k )
have an integral zero and that the next odd dimension with an integral zero is
d
=
17
𝑑
17
d=17
italic_d = 17
.
3.
Negative Results
We construct examples of orbifolds that are
p
𝑝
p
italic_p
-isospectral to manifolds (for various
p
≥
1
𝑝
1
p\geq 1
italic_p ≥ 1
) and obtain some inverse spectral results for the
p
𝑝
p
italic_p
-spectrum alone. We also construct a family of mutually 1-isospectral 2-orbifolds with different geometric and topological properties.
3.1.
Isospectrality of manifolds and orbifolds for various
p
𝑝
p
italic_p
-spectra
The article
[
GR03
]
contains examples of orbifolds of even dimension
d
=
2
⁢
m
𝑑
2
𝑚
d=2m
italic_d = 2 italic_m
that are
m
𝑚
m
italic_m
-isospectral to manifolds. Here, we will construct examples of flat orbifolds that are
p
𝑝
p
italic_p
-isospectral to manifolds for various values of
p
𝑝
p
italic_p
.
Notation 3.1
.
Every closed flat orbifold or manifold is of the form
𝒪
=
Σ
\
ℝ
d
𝒪
normal-\
normal-Σ
superscript
ℝ
𝑑
{\mathcal{O}}=\Sigma{\backslash}\mathbb{R}^{d}
caligraphic_O = roman_Σ \ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
where
Σ
normal-Σ
\Sigma
roman_Σ
is a discrete subgroup of the Euclidean motion group
ℝ
d
⋊
O
⁢
(
d
)
right-normal-factor-semidirect-product
superscript
ℝ
𝑑
𝑂
𝑑
\mathbb{R}^{d}\rtimes O(d)
blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ⋊ italic_O ( italic_d )
. (Note that
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is a manifold, i.e.,
Σ
normal-Σ
\Sigma
roman_Σ
acts freely on
ℝ
d
superscript
ℝ
𝑑
\mathbb{R}^{d}
blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
, if and only if
Σ
normal-Σ
\Sigma
roman_Σ
is a Bieberbach group). The restriction of the projection
ℝ
d
⋊
O
⁢
(
d
)
→
O
⁢
(
d
)
normal-→
right-normal-factor-semidirect-product
superscript
ℝ
𝑑
𝑂
𝑑
𝑂
𝑑
\mathbb{R}^{d}\rtimes O(d)\to O(d)
blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ⋊ italic_O ( italic_d ) → italic_O ( italic_d )
to
Σ
normal-Σ
\Sigma
roman_Σ
has finite image
F
𝐹
F
italic_F
and kernel a lattice
Λ
normal-Λ
\Lambda
roman_Λ
of rank
d
𝑑
d
italic_d
. We will refer to
Λ
normal-Λ
\Lambda
roman_Λ
as the translation lattice of
Σ
normal-Σ
\Sigma
roman_Σ
. The group
F
𝐹
F
italic_F
is the holonomy group of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
. For each
γ
∈
F
𝛾
𝐹
\gamma\in F
italic_γ ∈ italic_F
, there exists
a
=
a
⁢
(
γ
)
∈
ℝ
d
𝑎
𝑎
𝛾
superscript
ℝ
𝑑
a=a(\gamma)\in\mathbb{R}^{d}
italic_a = italic_a ( italic_γ ) ∈ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
, unique modulo
Λ
normal-Λ
\Lambda
roman_Λ
, such that
γ
∘
L
a
∈
Σ
𝛾
subscript
𝐿
𝑎
normal-Σ
\gamma\circ L_{a}\in\Sigma
italic_γ ∘ italic_L start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT ∈ roman_Σ
, where
L
a
subscript
𝐿
𝑎
L_{a}
italic_L start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT
denotes translation by
a
𝑎
a
italic_a
. Let
Λ
*
superscript
normal-Λ
\Lambda^{*}
roman_Λ start_POSTSUPERSCRIPT * end_POSTSUPERSCRIPT
denote the lattice dual to
Λ
normal-Λ
\Lambda
roman_Λ
. For
μ
≥
0
𝜇
0
\mu\geq 0
italic_μ ≥ 0
and
γ
∈
F
𝛾
𝐹
\gamma\in F
italic_γ ∈ italic_F
, set
e
μ
,
Σ
⁢
(
γ
)
=
∑
v
∈
Λ
*
,
‖
v
‖
=
μ
,
γ
⁢
(
v
)
=
v
e
2
⁢
π
⁢
i
⁢
v
⋅
a
.
subscript
𝑒
𝜇
Σ
𝛾
subscript
formulae-sequence
𝑣
superscript
Λ
formulae-sequence
norm
𝑣
𝜇
𝛾
𝑣
𝑣
superscript
𝑒
⋅
2
𝜋
𝑖
𝑣
𝑎
e_{\mu,\Sigma}(\gamma)=\sum_{v\in\Lambda^{*},\|v\|=\mu,\gamma(v)=v}e^{2\pi iv%
\cdot a}.
italic_e start_POSTSUBSCRIPT italic_μ , roman_Σ end_POSTSUBSCRIPT ( italic_γ ) = ∑ start_POSTSUBSCRIPT italic_v ∈ roman_Λ start_POSTSUPERSCRIPT * end_POSTSUPERSCRIPT , ∥ italic_v ∥ = italic_μ , italic_γ ( italic_v ) = italic_v end_POSTSUBSCRIPT italic_e start_POSTSUPERSCRIPT 2 italic_π italic_i italic_v ⋅ italic_a end_POSTSUPERSCRIPT .
In the notation of Notation
3.1
, let
T
𝑇
T
italic_T
be the torus
Λ
\
ℝ
d
\
Λ
superscript
ℝ
𝑑
\Lambda{\backslash}\mathbb{R}^{d}
roman_Λ \ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
. Let
η
=
∑
J
f
J
⁢
d
⁢
x
J
𝜂
subscript
𝐽
subscript
𝑓
𝐽
𝑑
superscript
𝑥
𝐽
\eta=\sum_{J}\,f_{J}\,dx^{J}
italic_η = ∑ start_POSTSUBSCRIPT italic_J end_POSTSUBSCRIPT italic_f start_POSTSUBSCRIPT italic_J end_POSTSUBSCRIPT italic_d italic_x start_POSTSUPERSCRIPT italic_J end_POSTSUPERSCRIPT
be the pullback to
ℝ
n
superscript
ℝ
𝑛
\mathbb{R}^{n}
blackboard_R start_POSTSUPERSCRIPT italic_n end_POSTSUPERSCRIPT
of a
p
𝑝
p
italic_p
-form on
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
. (Here
J
𝐽
J
italic_J
varies over all multi-indices
1
≤
j
1
<
⋯
<
j
p
≤
d
1
subscript
𝑗
1
⋯
subscript
𝑗
𝑝
𝑑
1\leq j_{1}<\dots<j_{p}\leq d
1 ≤ italic_j start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT < ⋯ < italic_j start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ≤ italic_d
, and the functions
f
J
subscript
𝑓
𝐽
f_{J}
italic_f start_POSTSUBSCRIPT italic_J end_POSTSUBSCRIPT
are
Σ
Σ
\Sigma
roman_Σ
-invariant.) We have
Δ
p
⁢
(
η
)
=
∑
J
Δ
0
⁢
(
f
J
)
⁢
d
⁢
x
J
.
superscript
Δ
𝑝
𝜂
subscript
𝐽
superscript
Δ
0
subscript
𝑓
𝐽
𝑑
superscript
𝑥
𝐽
\Delta^{p}(\eta)=\sum_{J}\,\Delta^{0}(f_{J})\,dx^{J}.
roman_Δ start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_η ) = ∑ start_POSTSUBSCRIPT italic_J end_POSTSUBSCRIPT roman_Δ start_POSTSUPERSCRIPT 0 end_POSTSUPERSCRIPT ( italic_f start_POSTSUBSCRIPT italic_J end_POSTSUBSCRIPT ) italic_d italic_x start_POSTSUPERSCRIPT italic_J end_POSTSUPERSCRIPT .
Thus every element of the
p
𝑝
p
italic_p
-spectrum of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
occurs as an eigenvalue in the 0-spectrum of the torus
T
𝑇
T
italic_T
; i.e., it is of the form
4
⁢
π
2
⁢
‖
μ
‖
2
4
superscript
𝜋
2
superscript
norm
𝜇
2
4\pi^{2}\|\mu\|^{2}
4 italic_π start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ∥ italic_μ ∥ start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT
for some
μ
𝜇
\mu
italic_μ
in the dual lattice
Λ
*
superscript
Λ
\Lambda^{*}
roman_Λ start_POSTSUPERSCRIPT * end_POSTSUPERSCRIPT
of
Λ
Λ
\Lambda
roman_Λ
. The following result of Miatello and Rossetti, while originally stated in the context of flat manifolds, is also valid for orbifolds.
Proposition 3.2
(
[
MR01
, Theorem 3.1]
)
.
We use the notation of Notation
3.1
.
(1)
For
μ
≥
0
𝜇
0
\mu\geq 0
italic_μ ≥ 0
, the multiplicity
m
p
,
μ
⁢
(
Σ
)
subscript
𝑚
𝑝
𝜇
Σ
m_{p,\mu}(\Sigma)
italic_m start_POSTSUBSCRIPT italic_p , italic_μ end_POSTSUBSCRIPT ( roman_Σ )
of
μ
𝜇
\mu
italic_μ
in the
p
𝑝
p
italic_p
-spectrum of
𝒪
=
Σ
\
ℝ
d
𝒪
\
Σ
superscript
ℝ
𝑑
{\mathcal{O}}=\Sigma{\backslash}\mathbb{R}^{d}
caligraphic_O = roman_Σ \ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
is given by
m
p
,
μ
⁢
(
Σ
)
=
1
|
F
|
⁢
∑
γ
∈
F
tr
p
⁡
(
γ
)
⁢
e
μ
,
Σ
⁢
(
γ
)
=
1
|
F
|
⁢
(
d
p
)
+
1
|
F
|
⁢
∑
1
≠
γ
∈
F
tr
p
⁡
(
γ
)
⁢
e
μ
,
Σ
⁢
(
γ
)
.
subscript
𝑚
𝑝
𝜇
Σ
1
𝐹
subscript
𝛾
𝐹
subscript
tr
𝑝
𝛾
subscript
𝑒
𝜇
Σ
𝛾
1
𝐹
binomial
𝑑
𝑝
1
𝐹
subscript
1
𝛾
𝐹
subscript
tr
𝑝
𝛾
subscript
𝑒
𝜇
Σ
𝛾
m_{p,\mu}(\Sigma)=\frac{1}{|F|}\sum_{\gamma\in F}\,\operatorname{tr}_{p}(%
\gamma)e_{\mu,\Sigma}(\gamma)=\frac{1}{|F|}\binom{d}{p}+\frac{1}{|F|}\sum_{1%
\neq\gamma\in F}\,\operatorname{tr}_{p}(\gamma)e_{\mu,\Sigma}(\gamma).
italic_m start_POSTSUBSCRIPT italic_p , italic_μ end_POSTSUBSCRIPT ( roman_Σ ) = divide start_ARG 1 end_ARG start_ARG | italic_F | end_ARG ∑ start_POSTSUBSCRIPT italic_γ ∈ italic_F end_POSTSUBSCRIPT roman_tr start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_γ ) italic_e start_POSTSUBSCRIPT italic_μ , roman_Σ end_POSTSUBSCRIPT ( italic_γ ) = divide start_ARG 1 end_ARG start_ARG | italic_F | end_ARG ( FRACOP start_ARG italic_d end_ARG start_ARG italic_p end_ARG ) + divide start_ARG 1 end_ARG start_ARG | italic_F | end_ARG ∑ start_POSTSUBSCRIPT 1 ≠ italic_γ ∈ italic_F end_POSTSUBSCRIPT roman_tr start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_γ ) italic_e start_POSTSUBSCRIPT italic_μ , roman_Σ end_POSTSUBSCRIPT ( italic_γ ) .
(2)
Thus if
𝒪
′
=
Σ
′
\
ℝ
d
superscript
𝒪
′
\
superscript
Σ
′
superscript
ℝ
𝑑
{\mathcal{O}}^{\prime}=\Sigma^{\prime}{\backslash}\mathbb{R}^{d}
caligraphic_O start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT = roman_Σ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT \ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
, where
Σ
′
superscript
Σ
′
\Sigma^{\prime}
roman_Σ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
has the same translation lattice
Λ
′
=
Λ
superscript
Λ
′
Λ
\Lambda^{\prime}=\Lambda
roman_Λ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT = roman_Λ
, and if there is a bijection
γ
↦
γ
′
maps-to
𝛾
superscript
𝛾
′
\gamma\mapsto\gamma^{\prime}
italic_γ ↦ italic_γ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
between the holonomy groups of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
and
𝒪
′
superscript
𝒪
′
{\mathcal{O}}^{\prime}
caligraphic_O start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
such that
tr
p
⁡
(
γ
)
⁢
e
μ
,
Σ
⁢
(
γ
)
=
tr
p
⁡
(
γ
′
)
⁢
e
μ
,
Σ
′
⁢
(
γ
′
)
subscript
tr
𝑝
𝛾
subscript
𝑒
𝜇
Σ
𝛾
subscript
tr
𝑝
superscript
𝛾
′
subscript
𝑒
𝜇
superscript
Σ
′
superscript
𝛾
′
\operatorname{tr}_{p}(\gamma)e_{\mu,\Sigma}(\gamma)=\operatorname{tr}_{p}(%
\gamma^{\prime})e_{\mu,\Sigma^{\prime}}(\gamma^{\prime})
roman_tr start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_γ ) italic_e start_POSTSUBSCRIPT italic_μ , roman_Σ end_POSTSUBSCRIPT ( italic_γ ) = roman_tr start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_γ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ) italic_e start_POSTSUBSCRIPT italic_μ , roman_Σ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_POSTSUBSCRIPT ( italic_γ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT )
for all
γ
∈
F
𝛾
𝐹
\gamma\in F
italic_γ ∈ italic_F
, then
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
and
𝒪
′
superscript
𝒪
′
{\mathcal{O}}^{\prime}
caligraphic_O start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
are
p
𝑝
p
italic_p
-isospectral.
Corollary 3.3
.
Suppose
𝒪
=
Σ
\
ℝ
d
𝒪
normal-\
normal-Σ
superscript
ℝ
𝑑
{\mathcal{O}}=\Sigma{\backslash}\mathbb{R}^{d}
caligraphic_O = roman_Σ \ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
and
𝒪
′
=
Σ
′
\
ℝ
d
superscript
𝒪
normal-′
normal-\
superscript
normal-Σ
normal-′
superscript
ℝ
𝑑
{\mathcal{O}}^{\prime}=\Sigma^{\prime}{\backslash}\mathbb{R}^{d}
caligraphic_O start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT = roman_Σ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT \ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
where
Σ
normal-Σ
\Sigma
roman_Σ
and
Σ
′
superscript
normal-Σ
normal-′
\Sigma^{\prime}
roman_Σ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
have the same translation lattice. If
|
F
|
=
|
F
′
|
𝐹
superscript
𝐹
normal-′
|F|=|F^{\prime}|
| italic_F | = | italic_F start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT |
and if
tr
p
⁡
(
γ
)
=
0
=
tr
p
⁡
(
γ
′
)
subscript
normal-tr
𝑝
𝛾
0
subscript
normal-tr
𝑝
superscript
𝛾
normal-′
\operatorname{tr}_{p}(\gamma)=0=\operatorname{tr}_{p}(\gamma^{\prime})
roman_tr start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_γ ) = 0 = roman_tr start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_γ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT )
for all
1
≠
γ
∈
F
1
𝛾
𝐹
1\neq\gamma\in F
1 ≠ italic_γ ∈ italic_F
and
1
≠
γ
′
∈
F
′
1
superscript
𝛾
normal-′
superscript
𝐹
normal-′
1\neq\gamma^{\prime}\in F^{\prime}
1 ≠ italic_γ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ∈ italic_F start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
, then
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
and
𝒪
′
superscript
𝒪
normal-′
{\mathcal{O}}^{\prime}
caligraphic_O start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT
are
p
𝑝
p
italic_p
-isospectral.
Notation 3.4
.
Given
d
≥
2
𝑑
2
d\geq 2
italic_d ≥ 2
and
k
∈
{
1
,
…
,
d
−
1
}
𝑘
1
normal-…
𝑑
1
k\in\{1,\dots,d-1\}
italic_k ∈ { 1 , … , italic_d - 1 }
, let
γ
k
:
ℝ
d
→
ℝ
d
normal-:
subscript
𝛾
𝑘
normal-→
superscript
ℝ
𝑑
superscript
ℝ
𝑑
\gamma_{k}:\mathbb{R}^{d}\to\mathbb{R}^{d}
italic_γ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT : blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT → blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
be given by
γ
k
⁢
(
x
1
,
…
,
x
d
)
=
(
−
x
1
,
…
,
−
x
k
,
x
k
+
1
,
…
,
x
d
)
,
subscript
𝛾
𝑘
subscript
𝑥
1
…
subscript
𝑥
𝑑
subscript
𝑥
1
…
subscript
𝑥
𝑘
subscript
𝑥
𝑘
1
…
subscript
𝑥
𝑑
\gamma_{k}(x_{1},\dots,x_{d})=(-x_{1},\dots,-x_{k},x_{k+1},\dots,x_{d}),
italic_γ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ( italic_x start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , italic_x start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ) = ( - italic_x start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , … , - italic_x start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT , italic_x start_POSTSUBSCRIPT italic_k + 1 end_POSTSUBSCRIPT , … , italic_x start_POSTSUBSCRIPT italic_d end_POSTSUBSCRIPT ) ,
let
a
∈
(
1
2
⁢
ℤ
)
d
𝑎
superscript
1
2
ℤ
𝑑
a\in(\frac{1}{2}\mathbb{Z})^{d}
italic_a ∈ ( divide start_ARG 1 end_ARG start_ARG 2 end_ARG blackboard_Z ) start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
with at least one of the last
d
−
k
𝑑
𝑘
d-k
italic_d - italic_k
entries of
a
𝑎
a
italic_a
equal to
1
2
1
2
\frac{1}{2}
divide start_ARG 1 end_ARG start_ARG 2 end_ARG
, and let
ρ
k
=
γ
k
∘
L
a
subscript
𝜌
𝑘
subscript
𝛾
𝑘
subscript
𝐿
𝑎
\rho_{k}=\gamma_{k}\circ L_{a}
italic_ρ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT = italic_γ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ∘ italic_L start_POSTSUBSCRIPT italic_a end_POSTSUBSCRIPT
. Let
Σ
k
subscript
normal-Σ
𝑘
\Sigma_{k}
roman_Σ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
, respectively
Σ
k
′
subscript
superscript
normal-Σ
normal-′
𝑘
\Sigma^{\prime}_{k}
roman_Σ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
be the discrete subgroup of the Euclidean motion group
ℝ
d
⋊
O
⁢
(
d
)
right-normal-factor-semidirect-product
superscript
ℝ
𝑑
𝑂
𝑑
\mathbb{R}^{d}\rtimes O(d)
blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ⋊ italic_O ( italic_d )
generated by
ℤ
d
superscript
ℤ
𝑑
\mathbb{Z}^{d}
blackboard_Z start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
together with
γ
k
subscript
𝛾
𝑘
\gamma_{k}
italic_γ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
, respectively
ρ
k
subscript
𝜌
𝑘
\rho_{k}
italic_ρ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
. Set
𝒪
k
:=
Σ
\
ℝ
d
assign
subscript
𝒪
𝑘
normal-\
normal-Σ
superscript
ℝ
𝑑
{\mathcal{O}}_{k}:=\Sigma{\backslash}\mathbb{R}^{d}
caligraphic_O start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT := roman_Σ \ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
and
M
k
:=
Σ
′
\
ℝ
d
assign
subscript
𝑀
𝑘
normal-\
superscript
normal-Σ
normal-′
superscript
ℝ
𝑑
M_{k}:=\Sigma^{\prime}{\backslash}\mathbb{R}^{d}
italic_M start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT := roman_Σ start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT \ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
.
Proposition 3.5
.
We use Notation
3.4
.
(1)
Suppose that
K
p
d
⁢
(
k
)
=
0
superscript
subscript
𝐾
𝑝
𝑑
𝑘
0
K_{p}^{d}(k)=0
italic_K start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ( italic_k ) = 0
, where
K
p
d
superscript
subscript
𝐾
𝑝
𝑑
K_{p}^{d}
italic_K start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
is the Krawtchouk polynomial given by Equation (
8
). Then
𝒪
k
subscript
𝒪
𝑘
{\mathcal{O}}_{k}
caligraphic_O start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
and
M
k
subscript
𝑀
𝑘
M_{k}
italic_M start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
are
p
𝑝
p
italic_p
-isospectral.
(2)
Moreover, if
k
′
∈
{
1
,
…
,
d
−
1
}
superscript
𝑘
′
1
…
𝑑
1
k^{\prime}\in\{1,\dots,d-1\}
italic_k start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT ∈ { 1 , … , italic_d - 1 }
is another zero of
K
p
d
superscript
subscript
𝐾
𝑝
𝑑
K_{p}^{d}
italic_K start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
, then the collection
{
M
k
,
M
k
′
,
𝒪
k
,
𝒪
k
′
}
subscript
𝑀
𝑘
subscript
𝑀
superscript
𝑘
′
subscript
𝒪
𝑘
subscript
𝒪
superscript
𝑘
′
\{M_{k},M_{k^{\prime}},{\mathcal{O}}_{k},{\mathcal{O}}_{k^{\prime}}\}
{ italic_M start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT , italic_M start_POSTSUBSCRIPT italic_k start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_POSTSUBSCRIPT , caligraphic_O start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT , caligraphic_O start_POSTSUBSCRIPT italic_k start_POSTSUPERSCRIPT ′ end_POSTSUPERSCRIPT end_POSTSUBSCRIPT }
are all mutually
p
𝑝
p
italic_p
-isospectral.
(3)
M
k
subscript
𝑀
𝑘
M_{k}
italic_M start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
is a manifold for all
k
𝑘
k
italic_k
, whereas the singular set of
𝒪
k
subscript
𝒪
𝑘
{\mathcal{O}}_{k}
caligraphic_O start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
consists precisely of
2
k
superscript
2
𝑘
2^{k}
2 start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT
singular strata each of which has codimension
k
𝑘
k
italic_k
.
(4)
𝒪
k
subscript
𝒪
𝑘
{\mathcal{O}}_{k}
caligraphic_O start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
and
M
k
subscript
𝑀
𝑘
M_{k}
italic_M start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
are orientable if and only if
k
𝑘
k
italic_k
is even.
Proof.
(1 and 2) In the notation of Notation
3.1
, the holonomy groups of both
𝒪
k
subscript
𝒪
𝑘
{\mathcal{O}}_{k}
caligraphic_O start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
and
M
k
subscript
𝑀
𝑘
M_{k}
italic_M start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
have order 2 with generator
γ
k
subscript
𝛾
𝑘
\gamma_{k}
italic_γ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
. Since
tr
p
⁡
(
γ
k
)
=
K
p
d
⁢
(
k
)
=
0
subscript
tr
𝑝
subscript
𝛾
𝑘
subscript
superscript
𝐾
𝑑
𝑝
𝑘
0
\operatorname{tr}_{p}(\gamma_{k})=K^{d}_{p}(k)=0
roman_tr start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_γ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT ) = italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT ( italic_k ) = 0
(as seen in Example
2.9
), Corollary
3.3
implies that
𝒪
k
subscript
𝒪
𝑘
{\mathcal{O}}_{k}
caligraphic_O start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
and
M
k
subscript
𝑀
𝑘
M_{k}
italic_M start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
are
p
𝑝
p
italic_p
-isospectral . Moreover, the corollary also implies that their
p
𝑝
p
italic_p
-spectra are independent of the choice of the zero
k
𝑘
k
italic_k
of
K
p
d
subscript
superscript
𝐾
𝑑
𝑝
K^{d}_{p}
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT
.
(3) The torus
T
=
ℤ
d
\
ℝ
d
𝑇
\
superscript
ℤ
𝑑
superscript
ℝ
𝑑
T=\mathbb{Z}^{d}{\backslash}\mathbb{R}^{d}
italic_T = blackboard_Z start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT \ blackboard_R start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
is a two-fold cover of each of
𝒪
k
subscript
𝒪
𝑘
{\mathcal{O}}_{k}
caligraphic_O start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
and
M
k
subscript
𝑀
𝑘
M_{k}
italic_M start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
. The map
ρ
k
subscript
𝜌
𝑘
\rho_{k}
italic_ρ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
induces a fixed-point free involution of
T
𝑇
T
italic_T
, so
M
k
subscript
𝑀
𝑘
M_{k}
italic_M start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
is a manifold. In contrast, the involution of
T
𝑇
T
italic_T
induced by
γ
k
subscript
𝛾
𝑘
\gamma_{k}
italic_γ start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
fixes all points each of whose first
k
𝑘
k
italic_k
coordinates lie in
{
0
,
1
2
}
0
1
2
\{0,\frac{1}{2}\}
{ 0 , divide start_ARG 1 end_ARG start_ARG 2 end_ARG }
. Thus
𝒪
k
subscript
𝒪
𝑘
{\mathcal{O}}_{k}
caligraphic_O start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
contains
2
k
superscript
2
𝑘
2^{k}
2 start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT
singular strata each of codimension
k
𝑘
k
italic_k
.
(4) is immediate.
∎
The examples below follow from Proposition
3.5
.
Example 3.6
.
In the notation of Notation
3.1
,
in every even dimension
d
𝑑
d
italic_d
, there exists a Bieberbach manifold
M
𝑀
M
italic_M
and a flat
d
𝑑
d
italic_d
-dimensional orbifold with singular set of codimension
d
2
𝑑
2
\frac{d}{2}
divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
such that
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
are
p
𝑝
p
italic_p
-isospectral for
all odd
p
𝑝
p
italic_p
. (See Remark
2.10
part 5.)
Example 3.7
.
By Equation (
8
), one easily sees that if
k
𝑘
k
italic_k
is a zero of
K
p
d
subscript
superscript
𝐾
𝑑
𝑝
K^{d}_{p}
italic_K start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT
, then so is
d
−
k
𝑑
𝑘
d-k
italic_d - italic_k
. Moreover, observe that
𝒪
k
subscript
𝒪
𝑘
{\mathcal{O}}_{k}
caligraphic_O start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
and
M
k
subscript
𝑀
𝑘
M_{k}
italic_M start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
are orientable if and only if
k
𝑘
k
italic_k
is even. In particular, if
d
𝑑
d
italic_d
is odd and
K
p
d
⁢
(
k
)
=
0
superscript
subscript
𝐾
𝑝
𝑑
𝑘
0
K_{p}^{d}(k)=0
italic_K start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ( italic_k ) = 0
, then the collection of
p
𝑝
p
italic_p
-isospectral orbifolds and manifolds
{
M
k
,
𝒪
k
,
M
d
−
k
,
𝒪
d
−
k
}
subscript
𝑀
𝑘
subscript
𝒪
𝑘
subscript
𝑀
𝑑
𝑘
subscript
𝒪
𝑑
𝑘
\{M_{k},{\mathcal{O}}_{k},M_{d-k},{\mathcal{O}}_{d-k}\}
{ italic_M start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT , caligraphic_O start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT , italic_M start_POSTSUBSCRIPT italic_d - italic_k end_POSTSUBSCRIPT , caligraphic_O start_POSTSUBSCRIPT italic_d - italic_k end_POSTSUBSCRIPT }
contains an orientable and a non-orientable manifold and an orientable and a non-orientable orbifold. Moreover, the codimensions of the singular sets of the two orbifolds have different parity.
For a specific example, we can take
d
=
n
2
𝑑
superscript
𝑛
2
d=n^{2}
italic_d = italic_n start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT
with
n
≥
3
𝑛
3
n\geq 3
italic_n ≥ 3
,
p
=
2
𝑝
2
p=2
italic_p = 2
and
k
=
n
⁢
(
n
+
1
)
2
𝑘
𝑛
𝑛
1
2
k=\frac{n(n+1)}{2}
italic_k = divide start_ARG italic_n ( italic_n + 1 ) end_ARG start_ARG 2 end_ARG
as in Remark
2.10
, part 3.
This example
was motivated by Example 4.3 in Miatello-Rossetti
[
MR01
]
, where the case
n
=
3
𝑛
3
n=3
italic_n = 3
was considered in the manifold case. We will use this example to prove sharpness in a result in the next section.
3.2.
Negative inverse spectral results for the middle degree
For manifolds and orbifolds of even dimension
d
𝑑
d
italic_d
, the
d
2
𝑑
2
\frac{d}{2}
divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
-spectrum contains less information than the other Hodge spectra due to Hodge duality: in any degree
p
𝑝
p
italic_p
, the Hodge Laplacian leaves invariant the subspace of exact forms and the subspace of co-exact forms. In the middle degree
p
=
d
2
𝑝
𝑑
2
p=\frac{d}{2}
italic_p = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
, the spectra on these two subspaces are identical. See
[
GR03
]
for many examples illustrating the weakness of the middle degree spectrum.
Example 3.8
.
Proposition
3.5
together with Remark
2.10
part 4 yield
d
2
𝑑
2
\frac{d}{2}
divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
-isospectral flat manifolds and orbifolds that are
p
𝑝
p
italic_p
-isospectral for all odd
p
𝑝
p
italic_p
.
[
GR03
, Theorem 3.2]
proves the isospectrality of these manifolds and orbifolds by different methods. In the special case that
d
=
2
𝑑
2
d=2
italic_d = 2
, the resulting manifold is a Klein bottle, while the orbifold is a cylinder, and these were also shown to be 1-isospectral to a Möbius strip. In
[
GR03
]
, it was also asserted that these surfaces are
1
1
1
1
-isospectral to a flat
3
3
3
3
-pillow (i.e., a flat Riemannian orbifold whose underlying space is a sphere with three cone points); however as shown in the subsequent errata
[
GR21
]
, that assertion was incorrect.
The example below describes a similar family of mutually
1
1
1
1
-isospectral
2
2
2
2
-dimensional orbifolds, demonstrating further the weakness of the middle-degree spectrum as a topological invariant. The
1
1
1
1
-isospectrality of the first and the fifth orbifolds is particularly striking as the first can be viewed as a square with absolute boundary conditions, while the second is topologically a sphere with three cone points. We also see that the
1
1
1
1
-spectrum does not detect the maximum order of isotropy present in an orbifold: the second and third orbifolds have maximum isotropy of order two in contrast to maximum order four in the other three.
Example 3.9
.
We construct a family of five mutually 1-isospectral 2-dimensional flat orbifolds. We use Notation
3.1
. All the orbifolds will have the same translation lattice
Λ
=
ℤ
2
normal-Λ
superscript
ℤ
2
\Lambda=\mathbb{Z}^{2}
roman_Λ = blackboard_Z start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT
, and their holonomy groups will have order four. To define each orbifold, we will specify both its holonomy group
F
<
O
⁢
(
2
)
𝐹
𝑂
2
F<O(2)
italic_F < italic_O ( 2 )
and a choice of
a
⁢
(
γ
)
𝑎
𝛾
a(\gamma)
italic_a ( italic_γ )
for each
γ
∈
F
𝛾
𝐹
\gamma\in F
italic_γ ∈ italic_F
. The orbifold is then given by
𝒪
:=
Σ
\
ℝ
2
assign
𝒪
normal-\
normal-Σ
superscript
ℝ
2
{\mathcal{O}}:=\Sigma{\backslash}\mathbb{R}^{2}
caligraphic_O := roman_Σ \ blackboard_R start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT
where
Σ
<
ℝ
2
⋊
O
⁢
(
2
)
normal-Σ
right-normal-factor-semidirect-product
superscript
ℝ
2
𝑂
2
\Sigma<\mathbb{R}^{2}\rtimes O(2)
roman_Σ < blackboard_R start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT ⋊ italic_O ( 2 )
is generated by
Λ
∪
{
γ
∘
L
a
⁢
(
γ
)
:
γ
∈
F
}
normal-Λ
conditional-set
𝛾
subscript
𝐿
𝑎
𝛾
𝛾
𝐹
\Lambda\cup\{\gamma\circ L_{a(\gamma)}:\gamma\in F\}
roman_Λ ∪ { italic_γ ∘ italic_L start_POSTSUBSCRIPT italic_a ( italic_γ ) end_POSTSUBSCRIPT : italic_γ ∈ italic_F }
. In each example,
F
𝐹
F
italic_F
contains
Id
normal-Id
{\operatorname{{Id}}}
roman_Id
,
−
Id
normal-Id
-{\operatorname{{Id}}}
- roman_Id
, and two elements with 1-trace zero. One can easily verify the mutual isospectrality of the five orbifolds using Proposition
3.2
, part
2
. The symbolic expression at the end of each example gives the Conway notation for the orbifold diffeomorphism class to which
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
belongs.
(1)
Let
F
<
O
⁢
(
2
)
𝐹
𝑂
2
F<O(2)
italic_F < italic_O ( 2 )
be the Klein 4-group generated by the reflections
γ
1
subscript
𝛾
1
\gamma_{1}
italic_γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
γ
2
subscript
𝛾
2
\gamma_{2}
italic_γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
across the
x
𝑥
x
italic_x
and
y
𝑦
y
italic_y
-axes, respectively. Take
a
⁢
(
γ
1
)
𝑎
subscript
𝛾
1
a(\gamma_{1})
italic_a ( italic_γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT )
and
a
⁢
(
γ
2
)
𝑎
subscript
𝛾
2
a(\gamma_{2})
italic_a ( italic_γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT )
both trivial. The underlying space of the corresponding orbifold
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is a square, and the
1
1
1
1
-spectrum of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
as an orbifold coincides with the
1
1
1
1
-spectrum of the square with absolute boundary conditions. As an orbifold, the four edges are reflectors and the four corners are order
2
2
2
2
dihedral points. Thus
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is of class
*
2222
absent
2222
*2222
* 2222
.
(2)
Let
F
<
O
⁢
(
2
)
𝐹
𝑂
2
F<O(2)
italic_F < italic_O ( 2 )
be as in item
1
now with
a
⁢
(
γ
1
)
=
(
1
2
,
0
)
𝑎
subscript
𝛾
1
1
2
0
a(\gamma_{1})=(\tfrac{1}{2},0)
italic_a ( italic_γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ) = ( divide start_ARG 1 end_ARG start_ARG 2 end_ARG , 0 )
and
a
⁢
(
γ
2
)
𝑎
subscript
𝛾
2
a(\gamma_{2})
italic_a ( italic_γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT )
trivial. The underlying space of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is a disk, and the singular set consists of two cone points of order
2
2
2
2
and a mirror edge along the boundary of the disk. Thus
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is of class
22
*
22*
22 *
.
(3)
Let
F
<
O
⁢
(
2
)
𝐹
𝑂
2
F<O(2)
italic_F < italic_O ( 2 )
be as in item
1
now with
a
⁢
(
γ
1
)
=
(
1
2
,
0
)
𝑎
subscript
𝛾
1
1
2
0
a(\gamma_{1})=(\tfrac{1}{2},0)
italic_a ( italic_γ start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT ) = ( divide start_ARG 1 end_ARG start_ARG 2 end_ARG , 0 )
and
a
⁢
(
γ
2
)
=
(
0
,
1
2
)
𝑎
subscript
𝛾
2
0
1
2
a(\gamma_{2})=(0,\tfrac{1}{2})
italic_a ( italic_γ start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ) = ( 0 , divide start_ARG 1 end_ARG start_ARG 2 end_ARG )
. The underlying space of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is a projective plane, and the singular set consists of two cone points of order
2
2
2
2
. Thus
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is of class
22
×
22\times
22 ×
.
(4)
Let
F
<
O
⁢
(
2
)
𝐹
𝑂
2
F<O(2)
italic_F < italic_O ( 2 )
be the Klein 4-group generated by the reflections
γ
3
subscript
𝛾
3
\gamma_{3}
italic_γ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT
and
γ
4
subscript
𝛾
4
\gamma_{4}
italic_γ start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT
across the lines
y
=
x
𝑦
𝑥
y=x
italic_y = italic_x
and
y
=
−
x
𝑦
𝑥
y=-x
italic_y = - italic_x
, respectively. Take
a
⁢
(
γ
3
)
𝑎
subscript
𝛾
3
a(\gamma_{3})
italic_a ( italic_γ start_POSTSUBSCRIPT 3 end_POSTSUBSCRIPT )
and
a
⁢
(
γ
4
)
𝑎
subscript
𝛾
4
a(\gamma_{4})
italic_a ( italic_γ start_POSTSUBSCRIPT 4 end_POSTSUBSCRIPT )
both trivial. The underlying space of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is a disk, and the singular set consists of two order
2
2
2
2
dihedral points on the boundary of the disk connected by two reflector edges, along with an interior order
2
2
2
2
cone point. Thus
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is of class
2
*
22
2
22
2*22
2 * 22
.
(5)
Let
F
<
O
⁢
(
2
)
𝐹
𝑂
2
F<O(2)
italic_F < italic_O ( 2 )
be the cyclic group of order
4
4
4
4
generated by rotation
γ
𝛾
\gamma
italic_γ
through angle
π
2
𝜋
2
\frac{\pi}{2}
divide start_ARG italic_π end_ARG start_ARG 2 end_ARG
about the origin, each element acting without precomposition by a translation. The underlying space of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is a sphere, and the singular set consists of two cone points of order
4
4
4
4
and one cone point of order
2
2
2
2
. Thus
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is of class
244
244
244
244
.
Remark 3.10
.
The five orbifolds in Example
3.9
are all mutually distinguishable by their 0-spectra. This follows, for example, by comparing the heat invariants for these orbifolds using
[
DGGW08
, Table 1]
and the fact that the lengths of the mirror loci in the first, second and fourth orbifolds are mutually distinct.
4.
Positive Results
In this section we obtain positive results regarding our central question of isospectrality between Riemannian manifolds and orbifolds. We first consider the
p
𝑝
p
italic_p
-spectrum for
p
≥
0
𝑝
0
p\geq 0
italic_p ≥ 0
and then focus our attention on the case where
p
=
1
𝑝
1
p=1
italic_p = 1
.
4.1.
Positive inverse spectral results for the
p
𝑝
p
italic_p
-spectra
We continue to assume that
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is a
d
𝑑
d
italic_d
-dimensional closed Riemannian orbifold.
Notation 4.1
.
We will say that a singular stratum of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
has
positive, respectively negative, parity
if its codimension in
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is even, respectively odd. For
ϵ
∈
{
±
}
italic-ϵ
plus-or-minus
\epsilon\in\{\pm\}
italic_ϵ ∈ { ± }
, let
k
ϵ
subscript
𝑘
italic-ϵ
k_{\epsilon}
italic_k start_POSTSUBSCRIPT italic_ϵ end_POSTSUBSCRIPT
be the minimum codimension of the primary singular strata (if any) of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
of parity
ϵ
italic-ϵ
\epsilon
italic_ϵ
, and let
S
ϵ
⁢
(
𝒪
)
subscript
𝑆
italic-ϵ
𝒪
S_{\epsilon}({\mathcal{O}})
italic_S start_POSTSUBSCRIPT italic_ϵ end_POSTSUBSCRIPT ( caligraphic_O )
be the collection of all primary strata of codimension
k
ϵ
subscript
𝑘
italic-ϵ
k_{\epsilon}
italic_k start_POSTSUBSCRIPT italic_ϵ end_POSTSUBSCRIPT
. Set
B
ϵ
p
⁢
(
𝒪
)
=
∑
N
∈
S
ϵ
⁢
(
𝒪
)
1
|
Iso
⁡
(
N
)
|
⁢
b
0
p
⁢
(
N
)
.
superscript
subscript
𝐵
italic-ϵ
𝑝
𝒪
subscript
𝑁
subscript
𝑆
italic-ϵ
𝒪
1
Iso
𝑁
superscript
subscript
𝑏
0
𝑝
𝑁
B_{\epsilon}^{p}({\mathcal{O}})=\sum_{N\in S_{\epsilon}({\mathcal{O}})}\,\frac%
{1}{|{\operatorname{{Iso}}}(N)|}\,b_{0}^{p}(N).
italic_B start_POSTSUBSCRIPT italic_ϵ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O ) = ∑ start_POSTSUBSCRIPT italic_N ∈ italic_S start_POSTSUBSCRIPT italic_ϵ end_POSTSUBSCRIPT ( caligraphic_O ) end_POSTSUBSCRIPT divide start_ARG 1 end_ARG start_ARG | roman_Iso ( italic_N ) | end_ARG italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_N ) .
If there are no singular strata of parity
ϵ
italic-ϵ
\epsilon
italic_ϵ
, then we set
B
ϵ
p
⁢
(
𝒪
)
=
0
.
superscript
subscript
𝐵
italic-ϵ
𝑝
𝒪
0
B_{\epsilon}^{p}({\mathcal{O}})=0.
italic_B start_POSTSUBSCRIPT italic_ϵ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O ) = 0 .
Remark 4.2
.
In case
p
=
0
𝑝
0
p=0
italic_p = 0
, one has
b
0
0
⁢
(
N
)
>
0
superscript
subscript
𝑏
0
0
𝑁
0
b_{0}^{0}(N)>0
italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 0 end_POSTSUPERSCRIPT ( italic_N ) > 0
for every primary singular stratum. Thus the condition
B
−
0
⁢
(
𝒪
)
≠
0
superscript
subscript
𝐵
0
𝒪
0
B_{-}^{0}({\mathcal{O}})\neq 0
italic_B start_POSTSUBSCRIPT - end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 0 end_POSTSUPERSCRIPT ( caligraphic_O ) ≠ 0
, respectively
B
+
0
⁢
(
𝒪
)
≠
0
superscript
subscript
𝐵
0
𝒪
0
B_{+}^{0}({\mathcal{O}})\neq 0
italic_B start_POSTSUBSCRIPT + end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 0 end_POSTSUPERSCRIPT ( caligraphic_O ) ≠ 0
, is equivalent to the condition that
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
contains at least one primary singular stratum of odd, respectively even, codimension. In the following proposition we obtain weak analogues of results for functions from
[
GR03
]
and its errata
[
GR21
]
and
[
Sut10
, Theorem 1.2]
.
Proposition 4.3
.
(1)
B
−
p
⁢
(
𝒪
)
superscript
subscript
𝐵
𝑝
𝒪
B_{-}^{p}({\mathcal{O}})
italic_B start_POSTSUBSCRIPT - end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O )
is an invariant of the
p
𝑝
p
italic_p
-spectrum. In particular, if
B
−
p
⁢
(
𝒪
)
≠
0
superscript
subscript
𝐵
𝑝
𝒪
0
B_{-}^{p}({\mathcal{O}})\neq 0
italic_B start_POSTSUBSCRIPT - end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O ) ≠ 0
, then
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
cannot be
p
𝑝
p
italic_p
-isospectral to a Riemannian manifold.
(2)
If
B
+
p
⁢
(
𝒪
)
≠
0
superscript
subscript
𝐵
𝑝
𝒪
0
B_{+}^{p}({\mathcal{O}})\neq 0
italic_B start_POSTSUBSCRIPT + end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O ) ≠ 0
, then
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
cannot be
p
𝑝
p
italic_p
-isospectral to any closed Riemannian manifold
M
𝑀
M
italic_M
such that
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
have isometric (possibly infinite) homogeneous Riemannian covers. If
B
+
p
⁢
(
𝒪
)
≠
0
superscript
subscript
𝐵
𝑝
𝒪
0
B_{+}^{p}({\mathcal{O}})\neq 0
italic_B start_POSTSUBSCRIPT + end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O ) ≠ 0
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
is good, then
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
cannot be
p
𝑝
p
italic_p
-isospectral to any closed Riemannian manifold
M
𝑀
M
italic_M
such that
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
have finite
p
𝑝
p
italic_p
-isospectral Riemannian covers.
Proof.
To prove part
1
observe that because
k
−
subscript
𝑘
k_{-}
italic_k start_POSTSUBSCRIPT - end_POSTSUBSCRIPT
is the minimal codimension of the odd primary singular strata, we have that
c
k
−
p
⁢
(
𝒪
)
=
(
4
⁢
π
)
k
−
/
2
⁢
B
−
p
⁢
(
𝒪
)
superscript
subscript
𝑐
subscript
𝑘
𝑝
𝒪
superscript
4
𝜋
subscript
𝑘
2
superscript
subscript
𝐵
𝑝
𝒪
c_{k_{-}}^{p}({\mathcal{O}})=(4\pi)^{k_{-}/2}B_{-}^{p}({\mathcal{O}})
italic_c start_POSTSUBSCRIPT italic_k start_POSTSUBSCRIPT - end_POSTSUBSCRIPT end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O ) = ( 4 italic_π ) start_POSTSUPERSCRIPT italic_k start_POSTSUBSCRIPT - end_POSTSUBSCRIPT / 2 end_POSTSUPERSCRIPT italic_B start_POSTSUBSCRIPT - end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O )
in the notation of Equation (
6
), and thus
B
−
p
⁢
(
𝒪
)
superscript
subscript
𝐵
𝑝
𝒪
B_{-}^{p}({\mathcal{O}})
italic_B start_POSTSUBSCRIPT - end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O )
is a spectral invariant. The second statement of part
1
is immediate.
The proof of part
2
is similar to the proofs of the analogous statements for the 0-spectrum cited in the introduction and above. We give a summary. It suffices to show that if
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
are isospectral, then each of the two conditions on
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
implies that
a
j
p
⁢
(
𝒪
)
=
a
j
p
⁢
(
M
)
superscript
subscript
𝑎
𝑗
𝑝
𝒪
superscript
subscript
𝑎
𝑗
𝑝
𝑀
a_{j}^{p}({\mathcal{O}})=a_{j}^{p}(M)
italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O ) = italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_M )
for all
j
𝑗
j
italic_j
. (See equation (
3
).) Writing
k
+
=
2
⁢
ℓ
subscript
𝑘
2
ℓ
k_{+}=2\ell
italic_k start_POSTSUBSCRIPT + end_POSTSUBSCRIPT = 2 roman_ℓ
, one then notes that
c
k
+
p
⁢
(
𝒪
)
=
a
ℓ
p
⁢
(
𝒪
)
+
(
4
⁢
π
)
ℓ
⁢
B
+
p
⁢
(
𝒪
)
subscript
superscript
𝑐
𝑝
subscript
𝑘
𝒪
superscript
subscript
𝑎
ℓ
𝑝
𝒪
superscript
4
𝜋
ℓ
superscript
subscript
𝐵
𝑝
𝒪
c^{p}_{k_{+}}({\mathcal{O}})=a_{\ell}^{p}({\mathcal{O}})+(4\pi)^{\ell}B_{+}^{p%
}({\mathcal{O}})
italic_c start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k start_POSTSUBSCRIPT + end_POSTSUBSCRIPT end_POSTSUBSCRIPT ( caligraphic_O ) = italic_a start_POSTSUBSCRIPT roman_ℓ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O ) + ( 4 italic_π ) start_POSTSUPERSCRIPT roman_ℓ end_POSTSUPERSCRIPT italic_B start_POSTSUBSCRIPT + end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O )
whereas the corresponding coefficient for
M
𝑀
M
italic_M
is
a
ℓ
p
⁢
(
M
)
superscript
subscript
𝑎
ℓ
𝑝
𝑀
a_{\ell}^{p}(M)
italic_a start_POSTSUBSCRIPT roman_ℓ end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_M )
, contradicting the
p
𝑝
p
italic_p
-isospectrality of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
and
M
𝑀
M
italic_M
.
First consider the case that there exist finite Riemannian covers
M
*
superscript
𝑀
M^{*}
italic_M start_POSTSUPERSCRIPT * end_POSTSUPERSCRIPT
of
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
and
M
*
*
superscript
𝑀
absent
M^{**}
italic_M start_POSTSUPERSCRIPT * * end_POSTSUPERSCRIPT
of
M
𝑀
M
italic_M
that are
p
𝑝
p
italic_p
-isospectral. Suppose that
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
are
p
𝑝
p
italic_p
-isospectral. Since the
p
𝑝
p
italic_p
-spectrum determines the volume, we have
vol
⁢
(
M
)
=
vol
⁢
(
𝒪
)
vol
𝑀
vol
𝒪
{\rm vol}(M)={\rm vol}({\mathcal{O}})
roman_vol ( italic_M ) = roman_vol ( caligraphic_O )
and also
vol
⁢
(
M
*
*
)
=
vol
⁢
(
M
*
)
vol
superscript
𝑀
absent
vol
superscript
𝑀
{\rm vol}(M^{**})={\rm vol}(M^{*})
roman_vol ( italic_M start_POSTSUPERSCRIPT * * end_POSTSUPERSCRIPT ) = roman_vol ( italic_M start_POSTSUPERSCRIPT * end_POSTSUPERSCRIPT )
. Thus the two coverings are of the same order
r
𝑟
r
italic_r
. Using equation (
3
), we then have
a
j
p
⁢
(
𝒪
)
=
1
r
⁢
a
j
p
⁢
(
M
*
)
=
1
r
⁢
a
j
p
⁢
(
M
*
*
)
=
a
j
p
⁢
(
M
)
superscript
subscript
𝑎
𝑗
𝑝
𝒪
1
𝑟
superscript
subscript
𝑎
𝑗
𝑝
superscript
𝑀
1
𝑟
superscript
subscript
𝑎
𝑗
𝑝
superscript
𝑀
absent
superscript
subscript
𝑎
𝑗
𝑝
𝑀
a_{j}^{p}({\mathcal{O}})=\frac{1}{r}a_{j}^{p}(M^{*})=\frac{1}{r}a_{j}^{p}(M^{*%
*})=a_{j}^{p}(M)
italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O ) = divide start_ARG 1 end_ARG start_ARG italic_r end_ARG italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_M start_POSTSUPERSCRIPT * end_POSTSUPERSCRIPT ) = divide start_ARG 1 end_ARG start_ARG italic_r end_ARG italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_M start_POSTSUPERSCRIPT * * end_POSTSUPERSCRIPT ) = italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_M )
for all
j
𝑗
j
italic_j
.
Next suppose that
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
and
M
𝑀
M
italic_M
have a common homogeneous Riemannian cover
M
~
~
𝑀
\tilde{M}
over~ start_ARG italic_M end_ARG
. We use the fact that the invariants
a
j
p
⁢
(
M
)
superscript
subscript
𝑎
𝑗
𝑝
𝑀
a_{j}^{p}(M)
italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_M )
and
a
j
p
⁢
(
𝒪
)
superscript
subscript
𝑎
𝑗
𝑝
𝒪
a_{j}^{p}({\mathcal{O}})
italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O )
are integrals over
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
, respectively, of functions
U
j
p
⁢
(
M
;
⋅
)
superscript
subscript
𝑈
𝑗
𝑝
𝑀
⋅
U_{j}^{p}(M;\cdot)
italic_U start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_M ; ⋅ )
and
U
j
p
⁢
(
𝒪
,
⋅
)
superscript
subscript
𝑈
𝑗
𝑝
𝒪
⋅
U_{j}^{p}({\mathcal{O}},\cdot)
italic_U start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O , ⋅ )
that satisfy locality and universality. (See
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
, Notation 3.13]
.) Homogeneity of the cover, along with the locality and universality properties, implies that
U
j
p
⁢
(
M
;
⋅
)
superscript
subscript
𝑈
𝑗
𝑝
𝑀
⋅
U_{j}^{p}(M;\cdot)
italic_U start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_M ; ⋅ )
and
U
j
p
⁢
(
𝒪
,
⋅
)
superscript
subscript
𝑈
𝑗
𝑝
𝒪
⋅
U_{j}^{p}({\mathcal{O}},\cdot)
italic_U start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O , ⋅ )
are constant functions with the same constant value
U
j
subscript
𝑈
𝑗
U_{j}
italic_U start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT
. If
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
are isospectral, then again they have the same volume
V
𝑉
V
italic_V
, so
a
j
p
⁢
(
M
)
=
U
j
⁢
V
=
a
j
p
⁢
(
𝒪
)
superscript
subscript
𝑎
𝑗
𝑝
𝑀
subscript
𝑈
𝑗
𝑉
superscript
subscript
𝑎
𝑗
𝑝
𝒪
a_{j}^{p}(M)=U_{j}V=a_{j}^{p}({\mathcal{O}})
italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( italic_M ) = italic_U start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT italic_V = italic_a start_POSTSUBSCRIPT italic_j end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O )
.
∎
Theorem 4.4
.
Denote by
𝒪
⁢
r
⁢
b
k
d
𝒪
𝑟
subscript
superscript
𝑏
𝑑
𝑘
{\mathcal{O}rb}^{d}_{k}
caligraphic_O italic_r italic_b start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
the class of all closed
d
𝑑
d
italic_d
-dimensional Riemannian orbifolds with singular set of codimension
k
𝑘
k
italic_k
. Assume that
k
𝑘
k
italic_k
is odd. Let
p
∈
{
0
,
1
,
2
,
…
,
d
}
𝑝
0
1
2
normal-…
𝑑
p\in\{0,1,2,\dots,d\}
italic_p ∈ { 0 , 1 , 2 , … , italic_d }
and let
K
p
d
superscript
subscript
𝐾
𝑝
𝑑
K_{p}^{d}
italic_K start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT
be the Krawtchouk polynomial given by Equation (
8
). If
K
p
d
⁢
(
k
)
≠
0
superscript
subscript
𝐾
𝑝
𝑑
𝑘
0
K_{p}^{d}(k)\neq 0
italic_K start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ( italic_k ) ≠ 0
, then the
p
𝑝
p
italic_p
-spectrum determines the
(
d
−
k
)
𝑑
𝑘
(d-k)
( italic_d - italic_k )
-dimensional volume of the singular set of elements of
𝒪
⁢
r
⁢
b
k
d
𝒪
𝑟
subscript
superscript
𝑏
𝑑
𝑘
{\mathcal{O}rb}^{d}_{k}
caligraphic_O italic_r italic_b start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
. In particular, the
p
𝑝
p
italic_p
-spectrum distinguishes elements of orbifolds in
𝒪
⁢
r
⁢
b
k
d
𝒪
𝑟
subscript
superscript
𝑏
𝑑
𝑘
{\mathcal{O}rb}^{d}_{k}
caligraphic_O italic_r italic_b start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
from Riemannian manifolds.
Remark 4.5
.
The condition requiring that the parity of the codimension of the singular set is odd in Theorem
4.4
cannot be removed. In
[
RSW08
]
, Example 3.3, a pair of flat three-dimensional orbifolds were described,
𝒪
1
subscript
𝒪
1
{\mathcal{O}}_{1}
caligraphic_O start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
𝒪
2
subscript
𝒪
2
{\mathcal{O}}_{2}
caligraphic_O start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
, which are
0
0
-isospectral but not
1
1
1
1
-isospectral. In this example, the singular sets of both
𝒪
1
subscript
𝒪
1
{\mathcal{O}}_{1}
caligraphic_O start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
and
𝒪
2
subscript
𝒪
2
{\mathcal{O}}_{2}
caligraphic_O start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
are of codimension 2. Further, as noted in the above paper, the singular set of
𝒪
2
subscript
𝒪
2
{\mathcal{O}}_{2}
caligraphic_O start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT
has volume equal to 12. On the other hand, one can check that the volume of the singular set of
𝒪
1
subscript
𝒪
1
{\mathcal{O}}_{1}
caligraphic_O start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT
is 6.
Proof of Theorem
4.4
.
Let
N
⊂
𝒪
∈
𝒪
⁢
r
⁢
b
k
d
𝑁
𝒪
𝒪
𝑟
subscript
superscript
𝑏
𝑑
𝑘
N\subset\mathcal{O}\in{\mathcal{O}rb}^{d}_{k}
italic_N ⊂ caligraphic_O ∈ caligraphic_O italic_r italic_b start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
be a singular stratum of codimension
k
𝑘
k
italic_k
. View
Iso
⁡
(
N
)
Iso
𝑁
{\operatorname{{Iso}}}(N)
roman_Iso ( italic_N )
as a subgroup of the orthogonal group
O
⁢
(
d
)
𝑂
𝑑
O(d)
italic_O ( italic_d )
. All non-trivial elements of
Iso
⁡
(
N
)
Iso
𝑁
{\operatorname{{Iso}}}(N)
roman_Iso ( italic_N )
must lie in
Iso
max
⁡
(
N
)
superscript
Iso
max
𝑁
\operatorname{Iso}^{\rm max}(N)
roman_Iso start_POSTSUPERSCRIPT roman_max end_POSTSUPERSCRIPT ( italic_N )
and must have the same 1-eigenspace; otherwise there would exist a stratum of smaller codimension. Thus
Iso
⁡
(
N
)
Iso
𝑁
{\operatorname{{Iso}}}(N)
roman_Iso ( italic_N )
must be of the form
Iso
⁡
(
N
)
=
Γ
×
{
Id
d
−
k
}
Iso
𝑁
Γ
subscript
Id
𝑑
𝑘
{\operatorname{{Iso}}}(N)=\Gamma\times\{{\operatorname{{Id}}}_{d-k}\}
roman_Iso ( italic_N ) = roman_Γ × { roman_Id start_POSTSUBSCRIPT italic_d - italic_k end_POSTSUBSCRIPT }
where
Γ
Γ
\Gamma
roman_Γ
is a subgroup of the orthogonal group
O
⁢
(
k
)
𝑂
𝑘
O(k)
italic_O ( italic_k )
that acts freely on the sphere
S
k
−
1
superscript
𝑆
𝑘
1
S^{k-1}
italic_S start_POSTSUPERSCRIPT italic_k - 1 end_POSTSUPERSCRIPT
. Since
k
𝑘
k
italic_k
is odd and the only finite group acting freely on even-dimensional spheres has order 2,
Γ
Γ
\Gamma
roman_Γ
and thus also
Iso
⁡
(
N
)
Iso
𝑁
{\operatorname{{Iso}}}(N)
roman_Iso ( italic_N )
must have order 2.
Using Equation (
10
) and Notation
4.1
we have,
B
−
p
⁢
(
𝒪
)
=
K
p
d
⁢
(
k
)
2
k
+
1
⁢
∑
N
∈
S
−
⁢
(
𝒪
)
vol
⁢
(
N
)
.
superscript
subscript
𝐵
𝑝
𝒪
superscript
subscript
𝐾
𝑝
𝑑
𝑘
superscript
2
𝑘
1
subscript
𝑁
subscript
𝑆
𝒪
vol
𝑁
B_{-}^{p}(\mathcal{O})=\frac{K_{p}^{d}(k)}{2^{k+1}}\sum_{N\in S_{-}(\mathcal{O%
})}\,{\rm vol}(N).
italic_B start_POSTSUBSCRIPT - end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O ) = divide start_ARG italic_K start_POSTSUBSCRIPT italic_p end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT ( italic_k ) end_ARG start_ARG 2 start_POSTSUPERSCRIPT italic_k + 1 end_POSTSUPERSCRIPT end_ARG ∑ start_POSTSUBSCRIPT italic_N ∈ italic_S start_POSTSUBSCRIPT - end_POSTSUBSCRIPT ( caligraphic_O ) end_POSTSUBSCRIPT roman_vol ( italic_N ) .
As shown in Proposition
4.3
part
1
,
B
−
p
⁢
(
𝒪
)
superscript
subscript
𝐵
𝑝
𝒪
B_{-}^{p}({\mathcal{O}})
italic_B start_POSTSUBSCRIPT - end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_p end_POSTSUPERSCRIPT ( caligraphic_O )
is a spectral invariant, thus the proof is complete.
∎
Thus for example, Theorem
4.4
along with Remark
2.10
imply the following.
Corollary 4.6
.
(1)
Assume
d
𝑑
d
italic_d
is not a perfect square. Then no closed Riemannian
d
𝑑
d
italic_d
-orbifold with singular set of odd codimension can be 2-isospectral to a Riemannian manifold (see Remark
2.10
, part 3). The same statement holds if
d
𝑑
d
italic_d
is of the form
d
=
4
⁢
m
2
𝑑
4
superscript
𝑚
2
d=4m^{2}
italic_d = 4 italic_m start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT
for some integer
m
𝑚
m
italic_m
.
(2)
Assume that
d
<
9
𝑑
9
d<9
italic_d < 9
is odd. Then no closed Riemannian
d
𝑑
d
italic_d
-orbifold with singular set of odd codimension can be
p
𝑝
p
italic_p
-isospectral to a Riemannian manifold for
p
∈
{
0
,
1
,
2
,
…
,
d
−
1
}
𝑝
0
1
2
…
𝑑
1
p\in\{0,1,2,\dots,d-1\}
italic_p ∈ { 0 , 1 , 2 , … , italic_d - 1 }
(see Remark
2.10
, part 6).
4.2.
Positive inverse spectral results for the
1
1
1
1
-spectrum
We next focus on the
1
1
1
1
-spectrum.
We treat this case in more depth as the
1
1
1
1
-trace is the trace of the matrix representation of the isometries in
O
⁢
(
d
)
𝑂
𝑑
O(d)
italic_O ( italic_d )
and this makes the corresponding calculations more tractable.
We begin with a theorem about what the
1
1
1
1
-spectrum reveals about orbifolds with a relatively large dimensional singular set.
Theorem 4.7
.
Let
𝒪
𝒪
\mathcal{O}
caligraphic_O
be a closed Riemannian orbifold of dimension
d
𝑑
d
italic_d
.
(1)
If
𝒪
𝒪
\mathcal{O}
caligraphic_O
contains at least one primary singular stratum of odd codimension
k
<
d
2
𝑘
𝑑
2
k<\frac{d}{2}
italic_k < divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
, then
𝒪
𝒪
\mathcal{O}
caligraphic_O
cannot be 1-isospectral to any closed Riemannian manifold.
(2)
If
𝒪
𝒪
\mathcal{O}
caligraphic_O
contains at least one singular stratum of codimension
k
<
d
2
𝑘
𝑑
2
k<\frac{d}{2}
italic_k < divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
, then
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
cannot be
1
1
1
1
-isospectral to any closed Riemannian manifold
M
𝑀
M
italic_M
such that
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
have isometric infinite homogeneous Riemannian covers. If in addition
𝒪
𝒪
\mathcal{O}
caligraphic_O
is good, then
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
cannot be
1
1
1
1
-isospectral to any closed Riemannian manifold
M
𝑀
M
italic_M
such that
M
𝑀
M
italic_M
and
𝒪
𝒪
{\mathcal{O}}
caligraphic_O
have finite
1
1
1
1
-isospectral Riemannian covers.
(3)
For
d
𝑑
d
italic_d
even, both statements remain true when
k
=
d
2
𝑘
𝑑
2
k=\frac{d}{2}
italic_k = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
provided at least one stratum of codimension
k
𝑘
k
italic_k
has isotropy group of order at least three.
(4)
An element of
𝒪
⁢
r
⁢
b
k
d
𝒪
𝑟
subscript
superscript
𝑏
𝑑
𝑘
{\mathcal{O}rb}^{d}_{k}
caligraphic_O italic_r italic_b start_POSTSUPERSCRIPT italic_d end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_k end_POSTSUBSCRIPT
with
k
𝑘
k
italic_k
odd can be 1-isospectral to a Riemannian manifold only if
d
𝑑
d
italic_d
is even and
k
=
d
2
𝑘
𝑑
2
k=\frac{d}{2}
italic_k = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
.
Remark 4.8
.
The proof of Proposition
3.5
shows that the hypothesis on isotropy order in Theorem
4.7
part
3
cannot be removed.
In Theorem
4.7
, part
1
and the first part of part
2
, the condition
k
=
d
2
𝑘
𝑑
2
k=\frac{d}{2}
italic_k = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
is sharp: Example
3.6
shows that the conclusion fails when
k
=
d
2
𝑘
𝑑
2
k=\frac{d}{2}
italic_k = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
with
d
𝑑
d
italic_d
even (see Remark
2.10
, part 5).
Proof of Theorem
4.7
.
Parts
1
and
2
follow from Proposition
4.3
along with the following two observations:
(1)
Since any singular stratum of minimum codimension is necessarily primary, the hypothesis of part
2
implies that
k
ϵ
<
d
2
subscript
𝑘
italic-ϵ
𝑑
2
k_{\epsilon}<\frac{d}{2}
italic_k start_POSTSUBSCRIPT italic_ϵ end_POSTSUBSCRIPT < divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
for at least one
ϵ
∈
{
±
}
italic-ϵ
plus-or-minus
\epsilon\in\{\pm\}
italic_ϵ ∈ { ± }
, while the hypothesis of part
1
says that
k
−
<
d
2
subscript
𝑘
𝑑
2
k_{-}<\frac{d}{2}
italic_k start_POSTSUBSCRIPT - end_POSTSUBSCRIPT < divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
.
(2)
If
N
𝑁
N
italic_N
is any primary singular stratum of codimension
k
𝑘
k
italic_k
and if
γ
∈
Iso
max
⁡
(
N
)
𝛾
superscript
Iso
max
𝑁
\gamma\in\operatorname{Iso}^{\rm max}(N)
italic_γ ∈ roman_Iso start_POSTSUPERSCRIPT roman_max end_POSTSUPERSCRIPT ( italic_N )
, then 1 is an eigenvalue of
γ
𝛾
\gamma
italic_γ
with multiplicity
d
−
k
𝑑
𝑘
d-k
italic_d - italic_k
while all other eigenvalues lie in
[
−
1
,
1
)
1
1
[-1,1)
[ - 1 , 1 )
. Thus if
k
<
d
2
𝑘
𝑑
2
k<\frac{d}{2}
italic_k < divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
, then
tr
⁡
(
γ
)
>
0
tr
𝛾
0
\operatorname{tr}(\gamma)>0
roman_tr ( italic_γ ) > 0
for all
γ
∈
Iso
max
⁡
(
N
)
𝛾
superscript
Iso
max
𝑁
\gamma\in\operatorname{Iso}^{\rm max}(N)
italic_γ ∈ roman_Iso start_POSTSUPERSCRIPT roman_max end_POSTSUPERSCRIPT ( italic_N )
, so
b
0
1
⁢
(
N
)
>
0
superscript
subscript
𝑏
0
1
𝑁
0
b_{0}^{1}(N)>0
italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT ( italic_N ) > 0
. In particular, if
k
ϵ
⁢
(
𝒪
)
<
d
2
subscript
𝑘
italic-ϵ
𝒪
𝑑
2
k_{\epsilon}(\mathcal{O})<\frac{d}{2}
italic_k start_POSTSUBSCRIPT italic_ϵ end_POSTSUBSCRIPT ( caligraphic_O ) < divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
, then
B
ϵ
⁢
(
𝒪
)
>
0
subscript
𝐵
italic-ϵ
𝒪
0
B_{\epsilon}(\mathcal{O})>0
italic_B start_POSTSUBSCRIPT italic_ϵ end_POSTSUBSCRIPT ( caligraphic_O ) > 0
.
To prove part
3
,
suppose that
k
ϵ
=
d
2
subscript
𝑘
italic-ϵ
𝑑
2
k_{\epsilon}=\frac{d}{2}
italic_k start_POSTSUBSCRIPT italic_ϵ end_POSTSUBSCRIPT = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
and let
N
𝑁
N
italic_N
be a primary stratum of codimension
k
=
d
2
𝑘
𝑑
2
k=\frac{d}{2}
italic_k = divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
. Every
γ
∈
Iso
max
⁡
(
N
)
𝛾
superscript
Iso
max
𝑁
\gamma\in\operatorname{Iso}^{\rm max}(N)
italic_γ ∈ roman_Iso start_POSTSUPERSCRIPT roman_max end_POSTSUPERSCRIPT ( italic_N )
has eigenvalues
1
1
1
1
with multiplicity
d
2
𝑑
2
\frac{d}{2}
divide start_ARG italic_d end_ARG start_ARG 2 end_ARG
while all other eigenvalues are either -1, or occur in conjugate pairs with real parts less than 1, so
tr
⁡
(
γ
)
≥
0
tr
𝛾
0
\operatorname{tr}(\gamma)\geq 0
roman_tr ( italic_γ ) ≥ 0
with equality if and only if
γ
2
=
Id
superscript
𝛾
2
Id
\gamma^{2}={\operatorname{{Id}}}
italic_γ start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT = roman_Id
. If
N
𝑁
N
italic_N
has higher order isotropy, then some
γ
∈
Iso
max
⁡
(
N
)
𝛾
superscript
Iso
max
𝑁
\gamma\in\operatorname{Iso}^{\rm max}(N)
italic_γ ∈ roman_Iso start_POSTSUPERSCRIPT roman_max end_POSTSUPERSCRIPT ( italic_N )
has at least two eigenvalues with real part strictly less than one, and thus
b
0
1
⁢
(
N
)
>
0
superscript
subscript
𝑏
0
1
𝑁
0
b_{0}^{1}(N)>0
italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT ( italic_N ) > 0
. Hence the presence of any primary strata with isotropy order greater than 2 implies that
B
ϵ
⁢
(
𝒪
)
>
0
subscript
𝐵
italic-ϵ
𝒪
0
B_{\epsilon}(\mathcal{O})>0
italic_B start_POSTSUBSCRIPT italic_ϵ end_POSTSUBSCRIPT ( caligraphic_O ) > 0
, so we can again apply Proposition
4.3
.
Part
4
follows from Theorem
4.4
along with Remark
2.10
, part 2.
∎
In
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
, we prove that the combination of the 0-spectrum and the 1-spectrum can distinguish closed orbifolds with singular sets of codimension at most 3 from smooth, closed Riemannian manifolds. As mentioned in the introduction, a natural question is whether the
1
1
1
1
-spectrum alone can distinguish orbifolds from manifolds? In the special case where
d
=
6
𝑑
6
d=6
italic_d = 6
, we have that the heat invariant
a
1
1
⁢
(
∗
)
=
(
d
−
6
)
⁢
a
1
0
⁢
(
∗
)
=
0
superscript
subscript
𝑎
1
1
∗
𝑑
6
superscript
subscript
𝑎
1
0
∗
0
a_{1}^{1}(\ast)=(d-6)a_{1}^{0}(\ast)=0
italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT ( ∗ ) = ( italic_d - 6 ) italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 0 end_POSTSUPERSCRIPT ( ∗ ) = 0
where
∗
∗
\ast
∗
is
M
𝑀
M
italic_M
or
𝒪
𝒪
\mathcal{O}
caligraphic_O
(see, for example,
[
Pat70
]
).
This observation motivates the investigation of whether, in dimension 6, it is possible for the 1-spectrum to distinguish orbifolds with singular sets of codimension 2 from Riemannian manifolds. With this in mind, we obtain the following result as an application of Theorem
4.7
and part of the strategy of the proof of Theorem 1.1 in
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
.
Theorem 4.9
.
Let
𝒪
𝒪
\mathcal{O}
caligraphic_O
be a
6
6
6
6
-dimensional, closed orbifold.
(1)
If
𝒪
𝒪
\mathcal{O}
caligraphic_O
has singular sets of codimension
≤
2
absent
2
\leq 2
≤ 2
, then the 1-spectrum distinguishes
𝒪
𝒪
\mathcal{O}
caligraphic_O
from smooth, closed,
6
6
6
6
-dimensional Riemannian manifolds.
(2)
If
𝒪
𝒪
\mathcal{O}
caligraphic_O
contains at least one stratum of codimension 3 with isotropy group of order at least 3, then
𝒪
𝒪
\mathcal{O}
caligraphic_O
cannot be 1-isospectral to any smooth, closed,
6
6
6
6
-dimensional Riemannian manifold.
Proof.
The second statement follows immediately from Theorem
4.7
part
3
.
To prove the first statement, we have from Theorem
4.7
part
1
that if
𝒪
𝒪
\mathcal{O}
caligraphic_O
contains at least one primary singular stratum of codimension 1, then
𝒪
𝒪
\mathcal{O}
caligraphic_O
cannot be 1-isospectral to any closed Riemannian manifold.
It remains to treat the case where
𝒪
𝒪
\mathcal{O}
caligraphic_O
has strata of codimension 2. Let
𝒮
2
⁢
(
𝒪
)
subscript
𝒮
2
𝒪
\mathcal{S}_{2}(\mathcal{O})
caligraphic_S start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ( caligraphic_O )
denote the collection of strata of codimension 2.
Following the proof of Theorem 1.1 of
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
, if
N
𝑁
N
italic_N
is a stratum of
𝒪
𝒪
\mathcal{O}
caligraphic_O
of codimension 2 then, as codimension 1 strata have already been considered above,
N
𝑁
N
italic_N
must have cyclic isotropy group of order
m
𝑚
m
italic_m
. For
d
=
6
𝑑
6
d=6
italic_d = 6
, the formula for
b
0
1
⁢
(
N
)
superscript
subscript
𝑏
0
1
𝑁
b_{0}^{1}(N)
italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT ( italic_N )
computed in
[
GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23
]
reads
b
0
1
⁢
(
N
)
=
(
m
2
−
1
3
+
m
2
−
6
⁢
m
+
5
6
)
⁢
vol
⁢
(
N
)
=
(
m
−
1
)
2
2
⁢
vol
⁢
(
N
)
.
superscript
subscript
𝑏
0
1
𝑁
superscript
𝑚
2
1
3
superscript
𝑚
2
6
𝑚
5
6
vol
𝑁
superscript
𝑚
1
2
2
vol
𝑁
b_{0}^{1}(N)=\left(\frac{m^{2}-1}{3}+\frac{m^{2}-6m+5}{6}\right){\rm vol}(N)=%
\frac{(m-1)^{2}}{2}{\rm vol}(N).
italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT ( italic_N ) = ( divide start_ARG italic_m start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT - 1 end_ARG start_ARG 3 end_ARG + divide start_ARG italic_m start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT - 6 italic_m + 5 end_ARG start_ARG 6 end_ARG ) roman_vol ( italic_N ) = divide start_ARG ( italic_m - 1 ) start_POSTSUPERSCRIPT 2 end_POSTSUPERSCRIPT end_ARG start_ARG 2 end_ARG roman_vol ( italic_N ) .
Hence
b
0
1
⁢
(
N
)
>
0
superscript
subscript
𝑏
0
1
𝑁
0
b_{0}^{1}(N)>0
italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT ( italic_N ) > 0
.
Now, since
a
1
1
⁢
(
∗
)
=
(
d
−
6
)
⁢
a
1
0
⁢
(
∗
)
=
0
superscript
subscript
𝑎
1
1
∗
𝑑
6
superscript
subscript
𝑎
1
0
∗
0
a_{1}^{1}(\ast)=(d-6)a_{1}^{0}(\ast)=0
italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT ( ∗ ) = ( italic_d - 6 ) italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 0 end_POSTSUPERSCRIPT ( ∗ ) = 0
, where
∗
∗
\ast
∗
is
M
𝑀
M
italic_M
or
𝒪
𝒪
\mathcal{O}
caligraphic_O
, the term of order
t
−
2
superscript
𝑡
2
t^{-2}
italic_t start_POSTSUPERSCRIPT - 2 end_POSTSUPERSCRIPT
in the small-time asymptotic expansion for the heat trace for 1-forms on
𝒪
𝒪
\mathcal{O}
caligraphic_O
has coefficient
∑
N
∈
𝒮
2
⁢
(
𝒪
)
b
0
1
⁢
(
N
)
>
0
,
subscript
𝑁
subscript
𝒮
2
𝒪
superscript
subscript
𝑏
0
1
𝑁
0
\sum_{N\in\mathcal{S}_{2}(\mathcal{O})}b_{0}^{1}(N)>0,
∑ start_POSTSUBSCRIPT italic_N ∈ caligraphic_S start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT ( caligraphic_O ) end_POSTSUBSCRIPT italic_b start_POSTSUBSCRIPT 0 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT ( italic_N ) > 0 ,
but there is no such term in the small-time asymptotic expansion for the heat trace for 1-forms on
M
𝑀
M
italic_M
as
a
1
1
⁢
(
M
)
=
0
superscript
subscript
𝑎
1
1
𝑀
0
a_{1}^{1}(M)=0
italic_a start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT start_POSTSUPERSCRIPT 1 end_POSTSUPERSCRIPT ( italic_M ) = 0
.
∎
References
[CS90]
Laura Chihara and Dennis Stanton.
Zeros of generalized Krawtchouk polynomials.
J. Approx. Theory
, 60(1):43–57, 1990.
[DGGW08]
Emily B. Dryden, Carolyn S. Gordon, Sarah J. Greenwald, and David L. Webb.
Asymptotic expansion of the heat kernel for orbifolds.
Michigan Math. J.
, 56(1):205–238, 2008.
[GGK
+
{}^{+}
start_FLOATSUPERSCRIPT + end_FLOATSUPERSCRIPT
23]
Katie Gittins, Carolyn Gordon, Magda Khalile, Ingrid Membrillo Solis, Mary
Sandoval, and Elizabeth Stanhope.
Do the Hodge Spectra Distinguish Orbifolds from Manifolds? Part 1.
Michigan Mathematical Journal
, pages 1 – 28, 2023.
[GR03]
Carolyn S. Gordon and Juan Pablo Rossetti.
Boundary volume and length spectra of Riemannian manifolds: what
the middle degree Hodge spectrum doesn’t reveal.
Ann. Inst. Fourier (Grenoble)
, 53(7):2297–2314, 2003.
[GR21]
Carolyn S. Gordon and Juan Pablo Rossetti.
Correction to “Boundary volume and length spectra of Riemannian
manifolds: what the middle degree Hodge spectrum doesn’t reveal”.
Annales de l’Institut Fourier
, 71(6):2647–2648, 2021.
[KL96]
Ilia Krasikov and Simon Litsyn.
On integral zeros of Krawtchouk polynomials.
J. Combin. Theory Ser. A
, 74(1):71–99, 1996.
[MR01]
R. J. Miatello and J. P. Rossetti.
Flat manifolds isospectral on
p
𝑝
p
italic_p
-forms.
J. Geom. Anal.
, 11(4):649–667, 2001.
[MR02]
R. J. Miatello and J. P. Rossetti.
Comparison of twisted
p
𝑝
p
italic_p
-form spectra for flat manifolds with
diagonal holonomy.
Ann. Global Anal. Geom.
, 21(4):341–376, 2002.
[Pat70]
V. K. Patodi.
Curvature and the fundamental solution of the heat operator.
J. Indian Math. Soc.
, 34(3-4):269–285 (1971), 1970.
[RS20]
Sean Richardson and Elizabeth Stanhope.
You can hear the local orientability of an orbifold.
Differential Geom. Appl.
, 68:101577, 7, 2020.
[RSW08]
Juan Pablo Rossetti, Dorothee Schueth, and Martin Weilandt.
Isospectral orbifolds with different maximal isotropy orders.
Ann. Global Anal. Geom.
, 34(4):351–366, 2008.
[Sut10]
Craig J. Sutton.
Equivariant isospectrality and Sunada’s method.
Arch. Math. (Basel)
, 95(1):75–85, 2010.