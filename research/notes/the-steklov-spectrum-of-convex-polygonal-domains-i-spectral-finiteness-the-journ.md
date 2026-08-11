---
title: 'The Steklov Spectrum of Convex Polygonal Domains I: Spectral Finiteness |
  The Journal of Geometric Analysis | Springer Nature Link'
id: the-steklov-spectrum-of-convex-polygonal-domains-i-spectral-finiteness-the-journ
tags:
- hyperbolic-pillow-heat-novelty-813161
created: '2026-08-09T08:48:53.989818Z'
updated: '2026-08-09T09:36:32.472587Z'
source: https://link.springer.com/article/10.1007/s12220-025-01922-8
source_domain: link.springer.com
fetched_at: '2026-08-09T08:48:53.989515Z'
fetch_provider: builtin
status: evergreen
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'The Steklov Spectrum of Convex Polygonal Domains I: Spectral Finiteness
  | The Journal of Geometric Analysis | Springe...'
---

The Steklov Spectrum of Convex Polygonal Domains I: Spectral Finiteness | The Journal of Geometric Analysis | Springer Nature Link
Skip to main content
The Steklov Spectrum of Convex Polygonal Domains I: Spectral Finiteness
Open access
Published:
06 February 2025
Volume 35
, article number
91
(
2025
)
Cite this article
You have full access to this
open access
article
Download PDF
Save article
View saved research
The Journal of Geometric Analysis
Aims and scope
Submit manuscript
The Steklov Spectrum of Convex Polygonal Domains I: Spectral Finiteness
Download PDF
Abstract
We explore the Steklov eigenvalue problem on convex polygons, focusing mainly on the inverse Steklov problem. Our primary finding reveals that, for almost all convex polygonal domains, there exist at most finitely many non-congruent domains with the same Steklov spectrum. Moreover, we obtain explicit upper bounds for the maximum number of mutually Steklov isospectral non-congruent polygonal domains. Along the way, we obtain isoperimetric bounds for the Steklov eigenvalues of a convex polygon in terms of the minimal interior angle of the polygon.
Similar content being viewed by others
Flexibility of Steklov eigenvalues via boundary homogenisation
Article
Open access
09 November 2022
Continuity of eigenvalues and shape optimisation for Laplace and Steklov problems
Article
Open access
01 June 2021
Computation of Eigenvalues for Nonlocal Models by Spectral Methods
Article
02 December 2021
Explore related subjects
Discover the latest articles, books and news in related subjects, suggested using machine learning.
Convex and Discrete Geometry
Geometry
Linear Algebra
Mathematics
Polytopes
Partial Differential Equations on Manifolds
Spectral Graph Theory and Its Applications
1
Introduction
The Steklov eigenvalue problem on a bounded planar domain
\(\Omega \)
with sufficiently regular boundary, first introduced by Vladimir Andreevich Steklov in 1895, consists of finding all
\(\sigma \in \mathbb {R}\)
for which there exists
\(0\ne u\in C^\infty (\Omega )\)
satisfying
$$\begin{aligned} \Delta u = 0 \text { in } \Omega , \quad \frac{\partial u}{\partial n} = \sigma u \, \, \text { on } \partial \Omega \end{aligned}$$
(1)
where
\(\Delta \)
is the Laplacian and
\(\frac{\partial }{\partial n}\)
is the outward-pointing normal derivative. The Steklov spectrum, i.e., the collection of all such
\(\sigma \)
repeated with multiplicity, is discrete and satisfies
$$\begin{aligned} 0 = \sigma _0(\Omega ) < \sigma _1 (\Omega ) \le \cdots \le \sigma _m (\Omega ) \le \cdots \nearrow + \infty . \end{aligned}$$
(2)
Equivalently, the Steklov eigenvalues are those of the Dirichlet-to-Neumann operator, which maps the Dirichlet boundary values of harmonic functions on
\(\Omega \)
to their Neumann boundary values.
For compact Riemmanian manifolds with smooth boundary, the Dirichlet-to-Neumann operator is an elliptic pseudodifferential operator and Hörmander’s theory yields Weyl asymptotics for the Steklov spectrum. However, for manifolds with only piecewise smooth or less regular boundary, the Dirichlet-to-Neumann operator fails to be pseudodifferential. Recently, Karpukhin et al. [
21
, Theorem 1.1], respectively Rozenblum [
32
, Theorem 1.2], proved that the asymptotics
$$\begin{aligned} \sigma _m = \frac{\pi m}{|\partial \Omega |} + o(m), \quad \text { as } m \rightarrow \infty . \end{aligned}$$
(3)
are valid for all compact Riemannian surfaces with Lipschitz boundary, respectively for bounded Euclidean domains of all dimensions with Lipschitz boundary. We refer to [
21
,
32
] for the history of these asymptotics under various regularity conditions on
\(\partial \Omega \)
. It follows from the asymptotics that the perimeter is a Steklov spectral invariant.
The Steklov eigenvalue problem lay mostly dormant for many years. A breakthrough came in 1954 when Weinstock [
34
] proved that the unit disk uniquely maximizes
\(\sigma _1(\Omega )\)
among all simply-connected planar domains of perimeter one. Recent decades have seen tremendous interest in the Steklov problem, not only for planar domains but for more general compact Riemannian manifolds with boundary. The very rich tapestry of results includes asymptotics, isoperimetric eigenvalue bounds, optimization of eigenvalues and a remarkable relationship to free boundary minimal surfaces in balls, inverse spectral results, numerical results, and much more. See the surveys [
8
] and [
3
] for exposition and many references in this very rapidly expanding area. For historical background and physical implications, we refer to Kuznetsov et. al [
24
].
The impetus for the current paper arose from the powerful results of Levitin et al. in [
25
] and in the subsequent article [
22
], joint also with Krymski. The focus of these papers is on simply-connected curvilinear
n
-gons
\(\Omega \)
with all interior angles lying in
\((0,\pi )\)
. They associate to each such
\(\Omega \)
a trigonometric polynomial
\(P_\Omega \)
, referred to as the
characteristic polynomial
of
\(\Omega \)
. The polynomial depends only on the edge lengths and angles of
\(\Omega \)
. In the former paper, they show that the roots of
\(P_\Omega \)
yield the Steklov spectral asymptotics of
\(\Omega \)
up to order
\(O(m^{-\epsilon })\)
for some
\(\epsilon >0\)
. In the latter, they show that the characteristic polynomial is a Steklov spectral invariant. By applying this invariant, they show for generic curvilinear
n
-gons with angles in
\((0,\pi )\)
that the Steklov spectrum determines the edge lengths, and it moreover determines the angles up to countably many explicit possibilities. The genericity conditions, referred to as
admissibility
, consist of an incommensurability condition on the edge lengths together with the exclusion of angles of the form
\(\frac{\pi }{2m+1}\)
with
\(m\in {\mathbb {Z}}^+\)
.
Motivated by their results, we address the question of finite Steklov spectral determination of convex polygons. First, however, we prove Steklov eigenvalue bounds for compact Riemannian surfaces with boundary and for triangles. Then we further develop our results to apply to non-convex polygonal domains. The eigenvalue bounds lead to an additional spectral invariant. To address eigenvalue bounds that are independent of scaling, we adopt the commonly used normalization by the perimeter of the boundary, i.e., we consider
\(\sigma _k(\Omega )L(\partial \Omega )\)
. We prove:
Result 1.1
[See Theorem
3.10
for a more precise statement.] For each
\(n=3, 4, \dots \)
, there exists a constant
\(C_n>0\)
depending only on
n
such that if
\(\Omega \)
is any convex
n
-gon with smallest angle
\(\alpha (\Omega )\)
, then the Steklov eigenvalues of
\(\Omega \)
satisfy
$$\begin{aligned} \sigma _k(\Omega ) L(\partial \Omega ) \le C_n k^2\alpha (\Omega ), \quad \text {for all } k \ge 0. \end{aligned}$$
For simply connected domains, and in particular for convex
n
-gons, Hersch et al. [
13
, p. 102] proved that
\(\sigma _k (\Omega ) L(\partial \Omega ) \le 2 \pi k\)
for every
k
, and Girouard and Polterovich [
7
, Theorem 1.3.1] later proved that the Hersch–Payne–Schiffer bounds are sharp. These bounds were originally shown for surfaces with smooth boundary. However, it was recently proven [
20
]—see also [
1
]—that all isoperimetric eigenvalue bounds that hold for domains with smooth boundary remain valid when the boundary is only Lipschitz. Although our bound is quadratic in
k
rather than linear in
k
, and the constant
\(C_n\)
is far from optimal even when
\(k=1\)
, the usefulness of the bound arises from the fact that it depends only on the smallest angle. For any sequence
\(\{\Omega _j\}\)
of convex polygonal domains of fixed perimeter that collapses to an interval, the eigenvalue bound implies that
\(\lim _{j\rightarrow \infty }\sigma _k(\Omega _j)= 0\)
for each
k
. In particular, the eigenvalue bounds yield the following inverse spectral result:
Corollary 1.2
A lower bound on the
k
th normalized eigenvalue yields a lower bound on all the interior angles of
\(\Omega \)
. In particular, there is a uniform lower bound on the angles of any collection of mutually Steklov isospectral convex
n
-gons.
In our next results we address spectral finiteness using the characteristic polynomial and in some cases also Corollary
1.2
:
Results 1.3
(a)
[See Sect.
4
] For every convex
n
-gon
\(\Omega \)
that satisfies the generic conditions of admissibility, we obtain an explicit finite upper bound on the number (up to congruence) of convex
n
-gons with the same Steklov spectrum as
\(\Omega \)
. If, moreover, all angles of the admissible convex
n
-gon
\(\Omega \)
are obtuse, then
\(\Omega \)
is uniquely determined by its Steklov spectrum among all convex
n
-gons.
(b)
[See Sect.
5
] For convex
n
-gons satisfying some genericity conditions that are weaker than admissibility, we obtain further Steklov finiteness results by applying Corollary
1.2
along with the characteristic polynomial.
We emphasize that additional tools need to be developed if one hopes to remove genericity assumptions completely. Indeed, as noted in [
22
], all parallelograms of fixed perimeter with angles
\(\frac{\pi }{5}, \frac{4\pi }{5}\)
(more generally,
\(\frac{\pi }{2\,m+1}, \frac{2\,m\pi }{2\,m+1}\)
for fixed
\(m\in {\mathbb {Z}}^+\)
) have the same characteristic polynomial. Corollary
1.2
is of no help in this case. In an upcoming paper, we will drop the genericity conditions and address questions of Steklov spectral determination within special classes of convex polygons including triangles, kites and regular polygons. In work in progress, we are also investigating the question of whether the characteristic polynomial distinguishes all convex
n
-gons from smoothly bounded simply-connected plane domains.
1.1
Organization of this Work
In Sect.
2
we review results of [
22
] and [
25
] and provide some simplifications in the context of convex polygons. We then address eigenvalue bounds in Sect.
3
, bounds on the sizes of Steklov isospectral sets of admissible convex
n
-gons in Sect.
4
, and inverse results under weaker genericity conditions in Sect.
5
. We end with a brief comparison between the Steklov and Laplace inverse spectral problems and look towards the future of this field in Sect.
6
.
2
Preliminaries
In this section we will recall some of the beautiful results of [
22
] providing Steklov spectral invariants for simply-connected curvilinear
n
-gons in
\(\mathbb {R}^2\)
. The edges of the curvilinear
n
-gons are assumed to be piecewise smooth and the angles at the
n
vertices are required to lie in the interval
\((0,\pi )\)
. In the special case in which the edges are geodesic, i.e., the case of convex
n
-gons, we will see that some of their results take on a simpler form. A polygon with edges that are line segments but that is not necessarily convex will be referred to simply as an
n
-gon.
2.1
Curvilinear
n
-Gons
We follow the same labeling convention for the edge lengths and interior angles at the vertices as [
22
].
Notational Conventions 2.1
We use
\(\ell _1,\dots , \ell _n\)
to denote edge lengths and
\(\alpha _1,\dots ,\alpha _n\)
to denote the interior angles at the vertices. We will usually abuse notation and use the same notation
\(\ell _j\)
, respectively
\(\alpha _j\)
, to denote the
j
th edge, respectively vertex. In settings where this can result in confusion, we will instead use
\(e_j\)
, respectively
\(v_j\)
, for the edges and vertices. We always number the edges and vertices cyclically with vertex
\(\alpha _j\)
occurring between edges
\(\ell _j\)
and
\(\ell _{j+1}\)
(see Fig.
1
);
\(\ell _{n+1}\)
is understood to be
\(\ell _1\)
. The data associated with a curvilinear
n
-gon
\(\Omega \)
consists of its vectors of edge lengths and angles
$$\begin{aligned} \pmb {\ell }=(\ell _1,\dots ,\ell _n)\,\,\,\text{ and }\,\,\,\pmb {\alpha }=(\alpha _1,\dots , \alpha _n). \end{aligned}$$
The cyclic labeling is unique only up to 2
n
possible permutations, corresponding to a choice of orientation of
\(\partial \Omega \)
and a choice of initial edge.
Fig. 1
Full size image
A triangle with angles and edges labeled as in [
22
]
The primary tool we will use to obtain inverse spectral results is the characteristic polynomial
\(P_\Omega \)
of a curvilinear
n
-gon first introduced in [
25
, Equation (2.20)]; see also [
22
].
Definition 2.2
The
characteristic polynomial
\(P_\Omega : \mathbb {R}\rightarrow \mathbb {R}\)
is a trigonometric polynomial given by:
$$\begin{aligned} P_{\Omega } (t):=\frac{1}{2} \sum _{\pmb {\xi }\in \{\pm 1\}^n}\, a_{\pmb {\xi }} \cos (|\pmb {\xi }\cdot \pmb {\ell }| t) - \prod _{j=1} ^n \sin \left( \frac{\pi ^2}{2 \alpha _j}\right) . \end{aligned}$$
(4)
Here
\(a_{\pmb {\xi }}\)
is defined for
\(\pmb {\xi }=(\xi _1,\dots , \xi _n)\in \{\pm 1\}^n\)
by
$$\begin{aligned} a_{\pmb {\xi }}=\prod _{\{j:\xi _j\ne \xi _{j+1}\}}\,c(\alpha _j), \end{aligned}$$
(5)
where
\(a_{\pmb {\xi }}\)
equals 1 if the product is over the empty set, and
$$\begin{aligned} c(\alpha _j)=\cos \left( \frac{\pi ^2}{2\alpha _j}\right) .\end{aligned}$$
(6)
The subscripts in
\(\pmb {\xi }\)
are cyclically ordered, so
\(\xi _{n+1}\)
is understood to be
\(\xi _1\)
. Thus in the definition of
\(a_{\pmb {\xi }}\)
, the product is either empty or contains an even number of factors, because there is always an even number of sign changes as one moves cyclically through the entries of
\(\pmb {\xi }\)
in order to return to the starting value.
Observe that the characteristic polynomial
\(P_\Omega \)
depends only on the data
\(\pmb {\alpha }(\Omega )\)
and
\(\pmb {\ell }(\Omega )\)
. Since
\(P_\Omega \)
is an even function, the roots occur in pairs
\(\pm \nu \)
. Let
$$\begin{aligned} 0\le \nu _0(P_\Omega )\le \nu _1(P_\Omega )\le \nu _2(P_\Omega )\le \dots \end{aligned}$$
(7)
be all the non-negative roots of
\(P_\Omega \)
where the positive roots are repeated according to their multiplicity and zero, if it occurs, is counted with half its multiplicity. The remarkable main result of [
25
] is that the roots of the characteristic polynomial determine the asymptotics of the Steklov eigenvalues:
Theorem 2.3
[
25
, Theorem 1.4 and Remark 4.21] Let
\(\Omega \)
be a curvilinear
n
-gon with angles
\(\alpha _1, \dots ,\alpha _n\in (0,\pi )\)
. Then the Steklov eigenvalues
\(\sigma _j(\Omega )\)
(see Eq. (
2
)) satisfy
$$\begin{aligned} \sigma _j(\Omega )-\nu _j(P_\Omega )=O(j^{-\epsilon })\,\,\text{ as }\,\,j\rightarrow \infty \end{aligned}$$
(8)
for every
\(\epsilon \)
satisfying
$$\begin{aligned} 0<\epsilon < \min \left( \left\{ \frac{\pi }{2\alpha _k}-\frac{1}{2}: k=1,\dots , n\right\} \cup \left\{ \frac{1}{4}\right\} \right) .\end{aligned}$$
In [
22
], the authors use the Hadamard-Weierstrass factorization theorem and a result of [
23
] on the zeros of periodic functions to show that
\(P_\Omega \)
is uniquely determined by the
o
(1)-asymptotics of its roots, thus yielding:
Theorem 2.4
[
22
, Theorem 1.13 and Remark 1.15] Let
\(\Omega \)
and
\(\Omega '\)
be curvilinear
n
-gons with all angles in
\((0,\pi )\)
. Then the following are equivalent:
(a)
\(\Omega \)
and
\(\Omega '\)
have the same characteristic polynomial;
(b)
\(\sigma _j(\Omega )-\sigma _j(\Omega ')= o(1)\,\,\text{ as }\,\,j\rightarrow \infty \)
;
(c)
For
\(\epsilon \)
as in Theorem
2.3
, we have
\(\sigma _j(\Omega )-\sigma _j(\Omega ')= O(j^{-\epsilon })\,\,\text{ as }\,\,j\rightarrow \infty \)
.
The equivalence of (a) and (b) is the content of [
22
, Theorem 1.13]. The implication (a)
\(\implies \)
(c) follows from Theorem
2.3
above, as noted in [
22
, Remark 1.15]. Finally, (c)
\(\implies \)
(b) is immediate.
Theorem 2.5
[
22
, Theorem 1.16] The characteristic polynomial
\(P_{\Omega }\)
of a curvilinear
n
-gon
\(\Omega \)
with all angles in
\((0,\pi )\)
can be constructed algorithmically from the Steklov spectrum of
\(\Omega \)
. In particular, the characteristic polynomial is a Steklov spectral invariant of
\(\Omega \)
.
Remark 2.6
Curvilinear polygons are simply-connected plane domains with piecewise smooth—but not smooth—boundary. In order to use Theorems
2.4
and
2.5
to compare the spectra of curvilinear
n
-gons to smooth domains, we can extend Definition
2.2
by defining the characteristic polynomial of a smooth plane domain
\(\Omega \)
of perimeter
\(\ell \)
to be
$$\begin{aligned} P_\Omega (t)=\cos (\ell t) -1. \end{aligned}$$
(9)
The sequence of non-negative roots
\(\nu _j(\Omega )\)
with multiplicities as in Eq. (
7
) is given in this case by
$$\begin{aligned} 0, \frac{2\pi }{\ell }, \frac{2\pi }{\ell }, \frac{4\pi }{\ell }, \frac{4\pi }{\ell }, \dots \end{aligned}$$
which is precisely the Steklov spectrum of a disk of circumference
\(\ell \)
. Moreover, by the well-known Steklov asymptotics for smooth simply-connected plane domains [
5
,
31
], one has
\(\sigma _j(\Omega )-\nu _j(\Omega ) = O(j^{-\infty })\)
as
\(j\rightarrow \infty \)
for every such domain. Thus Theorem
2.3
certainly holds. Theorem
2.4
also extends when one includes smooth domains along with curvilinear
n
-gons, since it is based on Theorem
2.3
together with a proof that the asymptotics of the non-negative roots determine a trigonometric polynomial uniquely. In particular, this theorem allows one to compare the asymptotics of a given curvilinear
n
-gon with the asymptotics of a smooth domain as in Example
2.7
below. The extension of the definition of the characteristic polynomial to smoothly bounded domains will also be convenient for us in Sect.
5
.
Example 2.7
Let
\(\Omega \)
be a curvilinear
n
-gon satisfying
$$\begin{aligned} \pmb {\alpha }(\Omega )=\left( \frac{\pi }{2m_1 +1}, \frac{\pi }{2m_2 +1},\dots , \frac{\pi }{2m_n +1}\right) .\end{aligned}$$
Then one easily computes that
$$\begin{aligned}P_\Omega (t)=\cos (\ell t) +(-1)^{m+1}\end{aligned}$$
where
\(\ell \)
is the perimeter of
\(\Omega \)
and
\(m:=m_1+\dots +m_n\)
. In particular, if
m
is even, then
\(P_\Omega \)
has the same characteristic polynomial as a disk and thus the same Steklov spectral asymptotics up to order
\(O(j^{-\epsilon })\)
for all
\(\epsilon <\frac{1}{4}\)
. (See Theorem
2.4
and Remark
2.6
.)
Observe that
\(\cos (\ell t)\)
necessarily occurs in
\(P_\Omega (t)\)
with coefficient one corresponding to
\(\pmb {\xi }=\pm (1,1,\dots , 1)\)
. This term reflects the well-known fact that the perimeter of a compact planar domain is a Steklov spectral invariant. Observe that at most
\(2^{n-1}\)
distinct cosine frequencies of the form
\(\pmb {\xi }\cdot \pmb {\ell }\)
occur in the characteristic polynomial. As in Example
2.7
above, if
\(c(\alpha _j)=0\)
, then some of the coefficients
\(a_{\pmb {\xi }}\)
will vanish. Information is also lost if
\(\pmb {\xi }\cdot \pmb {\ell }=0\)
for some
\(\pmb {\xi }\)
, in which case the corresponding cosine function will be absorbed into the constant term of the characteristic polynomial. If there are repetitions among the various
\(\pmb {\xi }\cdot \pmb {\ell }\)
, then one can have cancellations among their coefficients. The article [
22
] introduces genericity conditions on curvilinear
n
-gons, referred to as
admissibility conditions
, to guarantee that
\(2^{n-1}\)
distinct cosine frequencies appear in the characteristic polynomial with non-zero coefficients. In order to define their genericity conditions, we first introduce the intuitive language of rational, odd, and even angles.
Definition 2.8
We will say that an angle is
rational
if it is a rational multiple of
\(\pi \)
. Among the rational angles, those of the form
\(\frac{\pi }{k}\)
, where
\(k\in {\mathbb {Z}}\)
, will play an especially important role in what follows. Angles of this form will be called odd, respectively even, angles if
k
is an odd, respectively even, positive integer. (These angles are referred to as “special,” respectively “exceptional,” in [
22
].) Observe that an angle
\(\alpha \)
is odd if and only if
\(c(\alpha )=0\)
, while even angles
\(\alpha =\frac{\pi }{2m}\)
satisfy
\(c(\alpha )=(-1)^m\)
. Following [
22
], we will refer to
\((-1)^m\)
as the
parity
of the even angle
\(\frac{\pi }{2m}\)
. Similarly, we will refer to
\((-1)^j\)
as the parity of the odd angle
\(\frac{\pi }{2j+1}\)
.
Definition 2.9
[
22
, Definition 1.8] A curvilinear
n
-gon with all interior angles in
\((0,\pi )\)
is said to be admissible if the following two conditions hold: (1) the side lengths
\(\ell _1, \ldots , \ell _n\)
are incommensurable over
\(\{-1, 0, +1\}\)
(that is, no non-trivial linear combination of
\(\ell _1, \ldots , \ell _n\)
with coefficients taken from
\(\{-1, 0, 1\}\)
vanishes); and (2) none of the interior angles
\(\alpha _1, \ldots , \alpha _n\)
are odd (see Definition
2.8
).
Admissibility can also be viewed as a restriction on the form of the characteristic polynomial. A set of positive lengths
\(\ell _1,\dots , \ell _n\)
is incommensurable over
\(\{-1, 0, 1\}\)
if and only if all
\(\pmb {\xi }\cdot \pmb {\ell }\)
are distinct and non-zero, with
\(\pmb {\ell }\)
as in Notational Conventions
2.1
and
\(\pmb {\xi }\in \{-1,1\}^n\)
as in Definition
2.2
. In this case, the constant term in
\(P_\Omega \)
will be non-zero if and only if no interior angle of
\(\Omega \)
is even. More generally, we have the following relationships between admissibility and the characteristic polynomial.
Proposition 2.10
[
22
, p. 22] A curvilinear
n
-gon
\(\Omega \)
with all interior angles in
\((0, \pi )\)
is admissible if and only if its characteristic polynomial
\(P_\Omega \)
contains exactly
\(2^{n-1}\)
linearly independent terms of the form
\(a\cos (ct)\)
with
\(c\ne 0\)
. Moreover, within the class of all admissible curvilinear polygons, the characteristic polynomial determines the number of vertices.
A straightforward consequence of the above proposition is the following corollary.
Corollary 2.11
The characteristic polynomial distinguishes admissible curvilinear
n
-gons from all non-admissible curvilinear polygons that have at most
n
vertices and have all interior angles in
\((0,\pi )\)
.
We note, however, that an admissible curvilinear
n
-gon may have the same characteristic polynomial as a non-admissible curvilinear polygon with more than
n
vertices; see Lemma
5.3
. Before we proceed with stating further inverse spectral results for admissible curvilinear
n
-gons, we recall additional notation from [
22
].
Notation and Remarks 2.12
Let
\(\Omega \)
be a curvilinear
n
-gon with interior angles
\(\alpha _1,\dots , \alpha _n\)
. Write
$$\begin{aligned} \pmb {C}(\Omega )= (c(\alpha _1),\dots , c(\alpha _n)) \ \ \ \text {and}\ \ \ \pmb {C}_{\operatorname {ab}}(\Omega )=(|c(\alpha _1)|,\dots , |c(\alpha _n)|), \end{aligned}$$
(10)
where
\(c(\alpha _j)=\cos \left( \frac{\pi ^2}{2 \alpha _j} \right) \)
as in Definition
2.2
. Suppose that exactly
\(k\ge 1\)
of the interior angles of
\(\Omega \)
are even. The corresponding
k
vertices split the boundary
\(\partial \Omega \)
into
k
components
\({\mathcal {Y}}_1, \dots , {\mathcal {Y}}_k\)
consisting of the adjacent sides contained between the even angles. These are called the
exceptional components
in [
22
]. With a choice of orientation, each exceptional component is described by its vectors of ordered edge lengths and angles:
$$\begin{aligned} \pmb {\ell }({\mathcal {Y}}_j)=(\ell _1^j, \dots , \ell _{n_j}^j) \,\,\text{ and }\,\,\pmb {\alpha }({\mathcal {Y}}_j)=(\alpha _1^j,\dots \alpha _{n_j-1}^j). \end{aligned}$$
(11)
Write
$$\begin{aligned} \pmb {C}({\mathcal {Y}}_j)= \left( c(\alpha ^j_1),\dots , c(\alpha _{n_j-1}^j) \right) . \end{aligned}$$
(12)
We denote by
\(-{\mathcal {Y}}_j\)
the component
\({\mathcal {Y}}_j\)
with its orientation reversed. Following [
22
], we refer to
\(-{\mathcal {Y}}_j\)
as the
inverse
of
\({\mathcal {Y}}_j\)
.
We shall repeatedly make use of the following powerful result of [
22
].
Theorem 2.13
[
22
, Theorem 1.17] We use the notation of
2.1
,
2.9
, and
2.12
. Suppose that
\(\Omega \)
and
\(\Omega '\)
are admissible curvilinear
n
-gons that have the same characteristic polynomial. Then
(a)
\(\Omega \)
and
\(\Omega '\)
have the same number of even angles.
(b)
If they have no even angles, then the boundary orientations and cyclical labeling of the edges and vertices can be chosen so that
$$\begin{aligned} \pmb {\ell }(\Omega )=\pmb {\ell }(\Omega ') \,\,\text{ and }\,\, \pmb {C}(\Omega )=\pm \pmb {C}(\Omega ')\end{aligned}$$
for some choice of ±.
(c)
If there is at least one even angle, then there exists a one-to-one correspondence between the exceptional components of
\(\Omega \)
and
\(\Omega '\)
such that corresponding exceptional components
\({\mathcal {Y}}_j\)
and
\({\mathcal {Y}}'_j\)
satisfy either
$$\begin{aligned} \pmb {\ell }({\mathcal {Y}}_j)=\pmb {\ell }({\mathcal {Y}}'_j)\,\,\text{ and }\,\,\pmb {C}({\mathcal {Y}}_j)=\pm \pmb {C}({\mathcal {Y}}'_j)\end{aligned}$$
or else
$$\begin{aligned} \pmb {\ell }({\mathcal {Y}}_j)=\pmb {\ell }(-{\mathcal {Y}}'_j)\,\,\text{ and }\,\,\pmb {C}({\mathcal {Y}}_j)=\pm \pmb {C}(-{\mathcal {Y}}'_j)\end{aligned}$$
for some choice of ±.
Theorem 1.17 in [
22
] further asserts that for each exceptional component of an admissible curvilinear
n
-gon
\(\Omega \)
, the characteristic polynomial determines whether the even angles at its two ends have the same or the opposite parity in the sense of Definition
2.8
. In part (c) of Theorem
2.13
, we emphasize that the one-to-one correspondence does not necessarily respect the order in which the exceptional components appear. In particular, adjacent exceptional components in
\(\Omega \)
need not correspond to adjacent ones in
\(\Omega '\)
.
Remark 2.14
If
\(\Omega \)
has precisely one even angle, then there is only one exceptional component
\({\mathcal {Y}}\)
. Reorienting
\({\mathcal {Y}}\)
is equivalent to simply reorienting
\(\partial \Omega \)
and thus is a trivial change, i.e., it does not affect the isometry class. Part (c) of the theorem implies in this case that the boundary orientation of
\(\Omega '\)
can be chosen so that
\(\pmb {\ell }(\Omega )=\pmb {\ell }(\Omega ')\)
and
\(\pmb {C}({\mathcal {Y}})=\pm \pmb {C}({\mathcal {Y}}')\)
. Thus, up to the choice of boundary orientation and cyclic labeling, the characteristic polynomial determines
\(\pm \pmb {C}(\Omega )\)
up to the sign of the entry
\(\pm 1\)
(the entry corresponding to the even angle) and up to a global sign change of all the remaining entries. In particular, it determines
\(\pmb {C}_{\operatorname {ab}}(\Omega )\)
uniquely up to trivial changes.
Remark 2.15
Amir Vig raised the following question to us: Does the Steklov spectrum of an
n
-gon detect whether the angles are rational multiples of
\(\pi \)
? Theorem
2.13
yields a positive answer in the case of admissible curvilinear
n
-gons: if
\(\Omega \)
and
\(\Omega '\)
are Steklov isospectral admissible curvilinear
n
-gons and if all of the interior angles of
\(\Omega \)
are rational multiplies of
\(\pi \)
, then the same is true for all the angles of
\(\Omega '\)
. Indeed, Theorem
2.13
tells us that, up to reordering,
\(|c(\alpha _j)|=|c(\alpha '_j)|\)
for
\(j=1,\dots , n\)
. This implies that
\(\frac{\pi ^2}{2\alpha '_j}=k\pi \pm \frac{\pi ^2}{2\alpha _j} \)
for some
\(k\in {\mathbb {Z}}\)
. Writing
\(\alpha _j=q_j\pi \)
, we then have
\(\alpha '_j=\frac{q_j\pi }{2kq_j\pm 1}.\)
To conclude the background on curvilinear
n
-gons, we summarize the properties of
\(|c(\alpha )|\)
that will be used extensively.
Lemma 2.16
Define
\(|c|:(0,\pi )\rightarrow [0,1]\)
by
\(|c|(\alpha ):=|c(\alpha )|\)
where
\(c(\alpha )=\cos \left( \frac{\pi ^2}{2\alpha }\right) \)
as in Definition
2.2
. Then:
(a)
\(|c|^{-1}(\{0\})\)
consists of all odd angles
\(\frac{\pi }{2k+1}\)
,
\(k\in {\mathbb {Z}}^+\)
.
(b)
\(|c|^{-1}(\{1\})\)
consists of all even angles
\(\frac{\pi }{2k}\)
,
\(k\in {\mathbb {Z}}^+\)
.
(c)
|
c
| maps each interval
\((\frac{\pi }{m+1},\frac{\pi }{m})\)
,
\(m\in {\mathbb {Z}}^+\)
, bijectively onto (0, 1). In particular, the restriction of |
c
| to the set of all obtuse angles is injective.
(d)
For
\(s\in [0,1]\)
, the inverse image
\(|c|^{-1}(\{s\})\)
is discrete and accumulates only at 0.
2.2
Convex Polygons
We now specialize to the case of convex polygons
\(\Omega \)
; i.e., in addition to assuming that all angles lie in
\((0, \pi )\)
, we assume all edges of
\(\Omega \)
are straight line segments. The only convex
n
-gon that has three odd angles is the equilateral triangle; all others have at most two odd angles since the angles must sum to
\((n-2)\pi \)
. For the same reason, with the exception of rectangles, a convex
n
-gon can have at most three even angles. In particular, an admissible convex
n
-gon
\(\Omega \)
can have at most three exceptional components. Consequently, any two exceptional components are adjacent, so we can view any ordering
\({\mathcal {Y}}_1,\dots , {\mathcal {Y}}_k\)
of the exceptional components as a cyclic ordering.
Notational Conventions 2.17
A choice of orientation of
\(\partial \Omega \)
induces compatible orientations of each exceptional boundary component. Moreover, the orientation yields a cyclic ordering
\({\mathcal {Y}}_1,\dots ,{\mathcal {Y}}_k\)
of the boundary components, unique up to the choice
\({\mathcal {Y}}_1\)
. In what follows, we will always assume that orientations and cyclic ordering of the exceptional boundary components are simultaneously compatible with some orientation of
\(\partial \Omega \)
.
Thus part (c) of Theorem
2.13
takes on the following simpler form:
Corollary 2.18
Suppose that
\(\Omega \)
and
\(\Omega '\)
are admissible convex
n
-gons that have the same characteristic polynomial and that have
\(k>0\)
even angles. Then there exist orientations of
\(\partial \Omega \)
and
\(\partial \Omega '\)
and cyclic orderings
\({\mathcal {Y}}_1,\dots ,{\mathcal {Y}}_k\)
and
\({\mathcal {Y}}'_1,\dots {\mathcal {Y}}'_k\)
of the exceptional components compatible with the orientations of
\(\partial \Omega \)
and
\(\partial \Omega '\)
, respectively, so that for each
\(j\in \{1,\dots , k\}\)
, we have either
$$\begin{aligned} \pmb {\ell }({\mathcal {Y}}_j)=\pmb {\ell }({\mathcal {Y}}'_j)\,\,\text{ and }\,\,\pmb {C}({\mathcal {Y}}_j)=\pm \pmb {C}({\mathcal {Y}}'_j)\end{aligned}$$
or else
$$\begin{aligned} \pmb {\ell }({\mathcal {Y}}_j)=\pmb {\ell }(-{\mathcal {Y}}'_j)\,\,\text{ and }\,\,\pmb {C}({\mathcal {Y}}_j)=\pm \pmb {C}(-{\mathcal {Y}}'_j)\end{aligned}$$
for some choice of ±.
The corollary is immediate from Theorem
2.13
since every ordering of the exceptional components is cyclic and compatible with some orientation of the boundary.
3
Eigenvalue Bounds and Applications to Steklov Isospectrality
In this section, we demonstrate a collection of estimates for the Steklov eigenvalues. In Subsect.
3.1
, we develop the tools needed for the rest of the section. In particular, we extend work of Girouard and Polterovich [
7
] addressing Steklov eigenvalue bounds for Riemannian surfaces containing long thin passages. In Subsect.
3.2
, we obtain bounds for the perimeter-normalized Steklov eigenvalues of arbitrary triangles in terms of the smallest vertex angle. Turning to
n
-gons with
\(n\ge 4\)
in Subsect.
3.3
, we first obtain Steklov eigenvalue bounds for long, thin
n
-gons,
convex or not
. Then as a consequence, we obtain bounds for the perimeter-normalized Steklov eigenvalues of
convex
n
-gons
\(\Omega \)
in terms of the smallest vertex angle
\(\alpha (\Omega )\)
. These bounds are not sharp and are far from optimal as
k
tends to infinity. However, for the purpose of obtaining spectral finiteness for certain sets of polygons, we only need a relationship between a fixed portion of the spectrum and the geometry of the polygon; the bounds we find provide such a relationship (see Sect.
5
).
3.1
Riemannian Surfaces Containing Long Thin Passages
Steklov eigenvalues satisfy a certain variational principle, also known as a min-max principle, which allows one to obtain eigenvalue estimates by choosing specific trial functions. This variational principle can be shown in a very general context (see [
2
]), but the following formulation will suffice for our purposes.
Proposition 3.1
Let
\(\Omega \)
be a compact Riemannian manifold with boundary. For
\(u\in H^1(\Omega )\)
, the Rayleigh quotient for the Steklov problem is defined by
$$\begin{aligned} \mathcal {R}(u)=\frac{\int _\Omega \,|\nabla u|^2 dA}{\int _{\partial \Omega }\,u^2 ds}. \end{aligned}$$
Here,
dA
denotes the Riemannian volume form on
\(\Omega \)
, and
ds
the induced Riemannian measure on the boundary. Let
\({\mathcal {E}}_k(\Omega )\)
denote the set of all
k
-dimensional subspaces of
\(H^1(\Omega )\)
that consist of functions whose restrictions to
\(\partial \Omega \)
are orthogonal to constants relative to the
\(L^2(\partial \Omega )\)
inner product. Then, the Steklov eigenvalues satisfy
$$\begin{aligned} \sigma _k(\Omega )=\min _{E\in {\mathcal {E}}_k(\Omega )}\,\max _{0\ne u\in E}\, \mathcal {R}(u). \end{aligned}$$
(13)
In dimension two, the numerator of the Rayleigh quotient (the Dirichlet energy) is invariant under conformal change of metric. Consequently, the Steklov spectrum of a compact Riemannian surface
M
with boundary is invariant of conformal changes of metric provided that the conformal factor is identically one on
\(\partial M\)
.
Girouard and Polterovich [
7
, §2] gave Steklov eigenvalue bounds for compact Riemannian manifolds of arbitrary dimension that contain a long thin cylindrical passage. We state their result only in dimension two and then, still in the 2-dimensional case, we give two extensions, the first in Proposition
3.4
and the second in Proposition
3.5
.
Lemma 3.2
[
7
, §2] Let
\(\Omega \)
be a compact Riemannian surface with Lipschitz boundary that contains a Euclidean rectangle of length
\(\ell \)
and width
w
. Assume that the two sides of length
\(\ell \)
lie in
\(\partial \Omega \)
. Then the
\(k^{th}\)
Steklov eigenvalue of
\(\Omega \)
satisfies
$$\begin{aligned} \sigma _k(\Omega ) \le \frac{2\pi ^2 k^2 w}{\ell ^2}. \end{aligned}$$
(14)
We note that there is no additional hypothesis on the sides of length
w
; they may or may not lie in
\(\partial \Omega \)
.
Proof
One uses the variational characterization of eigenvalues in Proposition
3.1
. Without loss of generality, we may assume that the rectangle contained in
\(\Omega \)
is located at
\([0, \ell ] \times [0, w]\)
in the
xy
-plane. We define trial functions on the rectangle via
$$\begin{aligned} u_j(x,y) = \sin \left( \frac{2\pi j x}{\ell } \right) , \quad 0 \le x \le \ell , \quad 0 \le y \le w, \end{aligned}$$
(15)
and extend
\(u_j\equiv 0\)
outside the rectangle. Then
\(E_k:=\text {span}\{u_1,\dots , u_k\}\in \mathcal {E}_k(\Omega )\)
with
\(\mathcal {E}_k\)
as in Proposition
3.1
. We have
$$\begin{aligned} \int _\Omega |\nabla u_j|^2 dA= &   \frac{4\pi ^2 j^2}{\ell ^2} \frac{w \ell }{2}. \end{aligned}$$
Moreover,
\(\nabla u_j\)
is orthogonal to
\(\nabla u_m\)
in
\(L^2(\Omega )\)
for
\(j \ne m\)
. We compute
$$\begin{aligned} \int _{\partial \Omega } u_j \, u_m \, ds = {\left\{ \begin{array}{ll} 0, &  j \ne m, \\ \ell , &  j = m. \end{array}\right. } \end{aligned}$$
Therefore, for every real linear combination
\(u=a_1 u_1 + \ldots + a_k u_k \in E_k\)
, we have
$$\begin{aligned} \mathcal {R}(u) \le \frac{2\pi ^2 w}{\ell ^2} \frac{\sum _{j=1} ^k j^2 a_j^2}{\sum _{j=1} ^k a_j^2} \le \frac{2\pi ^2k^2 w}{\ell ^2}, \end{aligned}$$
which implies that
$$\begin{aligned} \sigma _k(\Omega ) \le \frac{2\pi ^2k^2 w}{\ell ^2}. \end{aligned}$$
\(\square \)
The actual eigenvalue bound in the lemma above is not explicitly stated in [
7
] but the trial functions are given there. The lemma does not require that
\(\ell \gg w\)
but the bounds are much stronger in that case.
Definition 3.3
Recall that a
polar rectangle
is a sector either of a Euclidean disk or of a Euclidean annulus. If
\(r_1\)
and
\(r_2\)
are the inner and outer radii (so
\(r_1=0\)
in the case of a disk sector), we will refer to
\(\rho :=r_2-r_1\)
as the
radial side length
.
In the next proposition, we show how to use these polar rectangles to obtain estimates in the spirit of Lemma
3.2
.
Proposition 3.4
Let
\(\Omega \)
be a compact Riemannian surface with Lipschitz boundary that contains a closed subdomain
S
isometric to a polar rectangle of radial side length
\(\rho \)
and opening angle
\(\alpha \)
. Let
\(0\le r_1 < r_2\)
be the inner and outer radii (thus
\(\rho =r_2-r_1\)
) and let
\(s_1\)
and
\(s_2\)
be the arclengths of the inner and outer circular boundary arcs. Suppose that the two radial boundary edges of
S
lie in
\( S\cap \partial \Omega \)
. (We make no assumption on whether the inner and outer circular edges lie in
\(\partial \Omega \)
.) Then for all
\(k=1,2,\dots \)
, the Steklov eigenvalues of
\(\Omega \)
satisfy
$$\begin{aligned} \sigma _k(\Omega ) \le \alpha \frac{k^2 \pi ^2}{\rho } \left[ 1 + \frac{2 r_1}{\rho }\right] =k^2\pi ^2\left( \frac{s_1+s_2}{\rho ^2}\right) .\end{aligned}$$
(16)
In particular, if
\(r_1=0\)
(i.e.,
S
is isometric to a sector of a disk), then
$$\begin{aligned} \sigma _k(\Omega )\le \pi ^2\frac{k^2\alpha }{\rho }.\end{aligned}$$
(17)
Proof
The second statement follows from the first since
\(s_1=0\)
and
\(s_2=\alpha \rho \)
when
\(r_1=0\)
. To prove the first, we again apply the variational principle (
13
). We assume without loss of generality that the polar rectangle is described by
\(r_1< r < r_2\)
and
\(0<\theta < \alpha \)
. Using these polar coordinates
\((r, \theta )\)
on
S
, define functions
\(u_j\)
on
S
by
$$\begin{aligned} u_j(r,\theta ) = \sin \left( \frac{2\pi j\, (r-r_1)}{\rho }\right) , \end{aligned}$$
(18)
and extend
\(u_j\)
to
\(\Omega \)
by setting
\(u_j\equiv 0\)
on
\(\Omega \setminus S\)
. We have
\(E_k=\text {span}\{u_1,\dots , u_k\}\)
\(\subset \mathcal {E}_k\)
with
\(\mathcal {E}_k\)
as in Proposition
3.1
; the functions
\(u_j\)
satisfy
$$\begin{aligned} \int _\Omega |\nabla u_j|^2 dA = \alpha \frac{4\pi ^2 j^2}{\rho ^2} \int _{r_1}^{r_2} |\cos (2\pi j (r-r_1)/\rho )|^2 r dr = \alpha \pi ^2 j^2 \left[ 1+ \frac{2r_1}{\rho } \right] . \end{aligned}$$
We compute that
\(\nabla u_j\)
is orthogonal to
\(\nabla u_m\)
in
\(L^2(\Omega )\)
for
\(j \ne m\)
and
$$\begin{aligned} \int _{\partial \Omega } u_j \, u_m \, ds = 2 \int _{r_1} ^{r_2} \sin (2\pi j (r-r_1)/\rho ) \sin (2 \pi m (r-r_1)/\rho ) dr = {\left\{ \begin{array}{ll} 0, &  j \ne m, \\ \rho , &  j = m. \end{array}\right. } \end{aligned}$$
Therefore, for every real linear combination
\(u=a_1 u_1 + \ldots + a_k u_k \in E_k\)
, we have
$$\begin{aligned} \mathcal {R}(u) \le \alpha \pi ^2 \left[ 1+ \frac{2r_1}{\rho } \right] \frac{\sum _{j=1} ^k j^2 a_j^2}{\rho \sum _{j=1} ^k a_j^2} \le \alpha \frac{k^2 \pi ^2}{\rho } \left[ 1 + \frac{2 r_1}{\rho } \right] , \end{aligned}$$
giving the desired upper bound.
The final equality follows from the facts that
\(\rho =r_2-r_1\)
and that
\(s_i=r_i\alpha \)
for
\(i=1,2\)
.
\(\square \)
We build upon Lemma
3.2
and Proposition
3.4
to obtain eigenvalue estimates for Riemannian surfaces that contain either a long and narrow quadrilateral or a long and narrow triangle.
Proposition 3.5
Let
\(\Omega \)
be a compact Riemannian surface with Lipschitz boundary.
(a)
Suppose that
\(\Omega \)
contains a long, thin Euclidean quadrilateral
Q
with vertices in cyclic order given by
\(p_1, q_1, q_2, p_2\)
. More precisely, writing
$$\begin{aligned} w:= \max \{|p_1p_2|, |q_1q_2|\} \end{aligned}$$
and
$$\begin{aligned} \ell := \min \{|p_1q_1|,|p_2q_2|\}, \end{aligned}$$
suppose that
$$\begin{aligned} \ell >3w \end{aligned}$$
as in Fig.
2
. Assume that the two long sides
\(p_1q_1\)
and
\(p_2q_2\)
lie in
\(\partial \Omega \)
. Then the
\(k^{th}\)
Steklov eigenvalue of
\(\Omega \)
satisfies
$$\begin{aligned} \sigma _k(\Omega )\le 2k^2 \pi ^3\frac{w}{(\ell -3w)^2}. \end{aligned}$$
(b)
Suppose that
\(\Omega \)
contains a Euclidean triangle
T
with vertices
\(p,q_1,q_2\)
, such that the sides
\(pq_1\)
and
\(pq_2\)
lie in
\(\partial \Omega \)
and that
$$\begin{aligned} w:=|q_1q_2|< \frac{\ell }{2}<\ell = \min \{|pq_1|,|pq_2|\}. \end{aligned}$$
Then the
\(k^{th}\)
Steklov eigenvalue of
\(\Omega \)
satisfies
$$\begin{aligned} \sigma _k(\Omega )\le k^2 \pi ^3\frac{w}{(\ell -2w)^2}. \end{aligned}$$
Fig. 2
Full size image
A long thin quadrilateral
Q
. The extensions of the two long sides of
Q
intersect at
v
Proof
(a) Assume first that the two long sides are parallel, that is
\(p_1 q_1\)
is parallel to
\(p_2 q_2\)
. Then the distance between these sides is bounded above by
w
. We slice off a small region of
Q
near each of the two short sides in order to obtain a rectangle of length at least
\(\ell -|p_1p_2|-|q_1q_2|\ge \ell -2w\)
and width
\(\le w\)
. We then apply Lemma
3.2
to complete the proof in this case.
Thus we assume that
\(p_1q_1\)
is not parallel to
\(p_2q_2\)
. We will construct a polar rectangle in
\(\Omega \)
satisfying the hypotheses of Proposition
3.4
. Take an isometric copy of
Q
in
\(\mathbb {R}^2\)
and let
v
be the point of intersection of the lines through
\(p_1q_1\)
and
\(p_2q_2\)
as in Fig.
2
. We may assume for convenience that
\(|p_1p_2| < |q_1q_2|\)
. Thus
\(p_i\)
is the closest point to
v
and
\(q_i\)
the furthest point from
v
on side
\(p_iq_i\)
for
\(i=1,2\)
. Let
$$\begin{aligned} r_1:= \max (|v p_1|, |v p_2|) \end{aligned}$$
and
$$\begin{aligned} r_2':= \min ( |v q_1|, |v q_2|).\end{aligned}$$
(We are using the notation
\(r_2'\)
here as we will shrink it below to obtain the outer radius
\(r_2\)
of the desired polar rectangle.) Let
\(S_v(t)\)
denote the circle with center
v
and radius
t
. Then
\(S_v(r_1)\)
, respectively
\(S_v(r_2')\)
, intersects side
\(p_iq_i\)
at a point
\(p_i'\)
within distance
\(|p_1p_2|\)
of
\(p_i\)
, respectively a point
\(q_i'\)
within distance
\(|q_1q_2|\)
of
\(q_i\)
, for
\(i=1,2\)
. (Note that
\(p_i'=p_i\)
and
\(q_j'=q_j\)
for at least one value of
i
and one value of
j
in
\(\{1,2\}.\)
) Thus
$$\begin{aligned} r_2'-r_1\ge \ell -|p_1p_2|-|q_1q_2|> \ell -2w.\end{aligned}$$
(19)
We next shrink
\(r_2'\)
since the polar rectangle centered at
v
with inner radius
\(r_1\)
and outer radius
\(r_2'\)
may extend a little outside of
Q
near edge
\(q_1q_2\)
. Denote by
\(r_2\)
the distance from
v
to
\(q_1'q_2'\)
. Then the polar rectangle
S
bounded by
\(S_v(r_1)\)
,
\(S_v(r_2)\)
,
\(p_1q_1\)
and
\(p_2q_2\)
lies entirely inside
Q
.
Observe that for any
\(t\in [r_1,r_2']\)
, the chord of the circle
\(S_v(t)\)
joining points on
\(p_1q_1\)
and
\(p_2q_2\)
has length at most 2
w
. In particular, the midpoint
\(q_m\)
of the chord
\(q_1'q_2'\)
satisfies
\(|q_1'q_m|\le w\)
. Thus
\(r_2 \ge r_2'-w\)
and by Inequality (
19
), we have
$$\begin{aligned} \rho :=r_2-r_1 > \ell -3w.\end{aligned}$$
(20)
Next, since the length
s
of the arc of a circle subtended by a chord of length
c
satisfies
\(s\le \frac{\pi }{2} c\)
, the inner and outer arclengths
\(s_1\)
and
\(s_2\)
of
S
satisfy
$$\begin{aligned} s_j\le \frac{\pi }{2} (2w) =\pi w\end{aligned}$$
(21)
for
\(i=1,2\)
. Applying Proposition
3.4
, we thus have
$$\begin{aligned} \sigma _k(\Omega )\le 2k^2 \pi ^3\frac{w}{(\ell -3w)^2}, \end{aligned}$$
completing the proof.
(b) The proof follows the same steps with some minor modifications. We now set
\(p_1=p_2=p\)
, so
\(v=p\)
, and
\(r_1=0\)
. Inequality (
19
) becomes
\(r_2'\ge \ell -|q_1q_2|= \ell -w\)
. Since
\(r_2\ge r_2'-w\)
as before, we have
\(\rho :=r_2\ge \ell -2w\)
. Finally
\(s_1=0\)
and, as before,
\(s_2\le \pi w\)
. We can now apply the bound in (
17
) in Proposition
3.4
to obtain the stated eigenvalue bounds.
\(\square \)
Remark 3.6
It suffices to assume that the passage
Q
, respectively
T
, is conformally equivalent to a quadrilateral, respectively triangle, satisfying the hypotheses of the proposition provided that the conformal factor is identically one on
\(Q\cap \partial \Omega \)
, respectively
\(T\cap \partial \Omega \)
. (Indeed the trial functions used in the proof are supported in the passage so such conformal changes do not affect the Rayleigh quotients.)
3.2
Steklov Eigenvalue Bounds for Triangles
We apply the results of the previous subsection to give bounds for the perimeter-normalized Steklov eigenvalues of triangles. The bounds depend only on the smallest angle of the triangle. Note the contrast with the second item in Proposition
3.5
, which does not require that the domain itself be a triangle but imposes assumptions on the lengths of the sides of the triangular subdomain. Although our bounds in this subsection and the next are only improvements on the Hersch–Payne–Schiffer bound of
\(2\pi k\)
on normalized eigenvalues [
13
, p. 102] for certain values of the smallest angle in the domain, our interest is in obtaining bounds that depend explicitly on the geometry of the domains. We will prove the eigenvalue bound for triangles by using Proposition
3.4
, independently of Proposition
3.5
.
Proposition 3.7
Let
T
be a triangle and denote by
\(\alpha (T)\)
its smallest interior angle. Then
$$\begin{aligned} \sigma _k(T)L(\partial T) < 4.02\pi ^2k^2\alpha (T) \end{aligned}$$
with
\(L(\partial T)\)
the perimeter of
T
. More precisely, let
T
be a triangle with angles
\(\alpha \le \beta \le \gamma \)
and corresponding opposite side lengths
A
,
B
and
C
.
If
\(\gamma \ge \frac{\pi }{2}\)
, then
$$\begin{aligned} \sigma _k(T)L(\partial T) \le \frac{\pi ^2}{B} k^2 \alpha <4\pi ^2 k^2 \alpha .\end{aligned}$$
If
\(\gamma <\frac{\pi }{2}\)
, then
$$\begin{aligned} \sigma _k(T)L(\partial T) \le \min \left\{ \frac{\pi ^2}{B\sin (\gamma )} k^2 \alpha , 2k\pi \right\} <4.02\pi ^2 k^2 \alpha .\end{aligned}$$
Proof of Proposition 3.7
We may assume that
\(L(\partial T)=1\)
since
\(\sigma _k(T)L(\partial T)\)
is invariant under rescaling.
We will find the maximal value
\(\rho \)
such that the intersection of
T
with a disk of radius
\(\rho \)
centered at the vertex
\(\alpha \)
is a sector of radius
\(\rho \)
(and necessarily of angle
\(\alpha \)
). We can then apply (
17
) of Proposition
3.4
to conclude that
$$\begin{aligned} \sigma _k(T)L(\partial T) \le \frac{\pi ^2}{\rho } k^2 \alpha . \end{aligned}$$
The two sides of
T
adjacent to
\(\alpha \)
have edge lengths
B
and
C
satisfying
\(B\le C\)
. Observe that
\(\rho \)
is precisely the distance from vertex
\(\alpha \)
to the opposite side of
T
. If the triangle is non-acute, then
\(\rho =B\)
. For acute triangles,
\(\rho \)
is the length of the altitude from vertex
\(\alpha \)
to the opposite side and thus
\(\rho =B\sin (\gamma )\)
.
Since the perimeter of
T
is one, the triangle inequality implies that
\(A+B> \frac{1}{2}\)
. Recalling that
\(A \le B\)
, we thus have
\(B> \frac{1}{4}\)
, and the proposition follows for non-acute triangles. For the acute case, we may assume that
\(\alpha <\frac{1}{2\pi }\)
, since otherwise
\(2k\pi < 4\pi ^2 k^2 \alpha \)
for all
k
. Observe that
\(\frac{\pi }{2}>\gamma \ge \frac{1}{2}(\pi -\alpha )= \frac{\pi }{2}-\frac{\alpha }{2}\)
, so
\(\sin (\gamma )\ge \cos \left( \frac{\alpha }{2}\right) > \cos \left( \frac{1}{4\pi }\right) \)
. Thus we have
$$\begin{aligned} \sigma _k(T)L(\partial T)< \frac{4}{\sin (\gamma )} \pi ^2 k^2 \alpha<\frac{4}{\cos \left( \frac{1}{4\pi }\right) } \pi ^2 k^2 \alpha < 4.02 \pi ^2k^2\alpha .\end{aligned}$$
\(\square \)
The usefulness of the proposition is not so much for the specific bounds on the eigenvalues but rather for the inverse spectral problem. The proposition shows that knowledge of any perimeter-normalized Steklov eigenvalue suffices to provide a lower bound on the angles of the triangle. The actual eigenvalue bounds in Proposition
3.7
are quite weak in general. For triangles with two sufficiently small angles, one can somewhat improve the eigenvalue bounds when
\(k>1\)
by considering sectors emanating from both of the corresponding vertices. We illustrate this with isosceles triangles.
Corollary 3.8
Let
T
be an isosceles triangle such that the two equal angles of measure
\(\alpha \)
are less than or equal to the remaining angle. Then the perimeter-normalized Steklov eigenvalues satisfy
$$\begin{aligned} \sigma _{2k-1}(T)L(\partial T) \le \sigma _{2k}(T)L(\partial T) \le \frac{\pi ^2 }{B\cos (\alpha )}k^2\alpha =\frac{2(1+\cos (\alpha ))}{\cos (\alpha )}\pi ^2 k^2\alpha \end{aligned}$$
where
\(B (=A)\)
is the length of the two equal sides.
Proof
We have
\(2B+2B\cos (\alpha )=\)
perimeter of
T
. Without loss of generality, we assume the perimeter of
T
equals 1. So
$$\begin{aligned} B=\frac{1}{2(1+\cos (\alpha ))}.\end{aligned}$$
The altitude through the remaining angle (the largest angle) bisects the base, with each half having length
$$\begin{aligned} \rho :=B\cos (\alpha )= \frac{\cos (\alpha )}{2(1+\cos (\alpha ))}.\end{aligned}$$
The 2 sectors of angle
\(\alpha \)
and length
\(\rho \)
emanating from the 2 vertices of angle
\(\alpha \)
intersect only at the midpoint of the longest side of the triangle as shown in Fig.
3
.
Fig. 3
Full size image
This isosceles triangle has two smaller equal angles of measure
\(\alpha \)
. The two circular sectors of radius
\(\rho \)
centered at the two vertices of angle
\(\alpha \)
intersect only at the midpoint of the side of length
\(2\rho \)
Thus to estimate
\(\sigma _{2k}\)
, we can use
\(E_{2k}=\{u_1,\dots , u_k,v_1,\dots , v_k\}\)
where the
\(u_j\)
’s, respectively
\(v_j\)
’s, are defined according to (
18
) with support on the first, respectively second, sector. Here we are setting
\(r_1=0\)
in (
18
). We then obtain
$$\begin{aligned} \sigma _{2k}(T)\le \frac{\pi ^2 k^2}{\rho }\alpha ={\pi ^2 k^2}\frac{2(1+\cos (\alpha ))}{\cos (\alpha )}\alpha . \end{aligned}$$
\(\square \)
We compare the bounds in Corollary
3.8
with those in Proposition
3.7
for isosceles triangles. First observe that for either bound to beat the Hersch–Payne–Schiffer bound for some
k
, the value of
\(\alpha \)
must be very small. In particular, the isosceles triangle must be obtuse. Proposition
3.7
thus yields
$$\begin{aligned} \sigma _{2k}(T)L(\partial T) \le \frac{\pi ^2 }{B}(2k)^2\alpha = \frac{4\pi ^2 }{B}k^2\alpha .\end{aligned}$$
Since
\(\alpha \)
is small,
\(\cos (\alpha )\)
is only slightly smaller than one, so the estimate in Corollary
3.8
for even eigenvalues is a little more than
\(\frac{1}{4}\)
that of the former estimate. For odd eigenvalues
\(\sigma _{2k-1}\)
with
\(k\ge 2\)
, we again get an improvement although not quite as substantial. For
\(\sigma _1\)
, the original estimate is slightly better.
In the case of a non-isosceles triangle
T
with two very small angles
\(\alpha < \beta \)
, we can construct sectors centered at
\(\alpha \)
and
\(\beta \)
. For each sector, the analogous argument to that in Corollary
3.8
yields a set of eigenvalue bounds corresponding to trial functions that are supported on that sector, with
\(\sigma _k(T)L(\partial T)\)
bounded above by the
k
th smallest element of the union of those two sets. The magnitude of the improvement in the bounds using two sectors rather than just one depends on the ratio
\(\frac{\beta }{\alpha }\)
.
3.3
Steklov Eigenvalue Bounds for
n
-Gons
We first give eigenvalue bounds for long thin
n
-gons that are
not
necessarily convex as shown in Fig.
4
.
Fig. 4
Full size image
The x-coordinates of this polygon are labelled from left to right. We create the dashed rectangle with vertices
\(x_3\)
and
\(x_4\)
. Then there are an even number of disjoint open segments in the boundary of the polygon whose closures have endpoints with
x
-coordinates equal to
\(x_3\)
and
\(x_4\)
, respectively. The topmost are denoted
\(S_1\)
and
\(S_2\)
Proposition 3.9
Let
\(\Omega \)
be an
n
-gon contained in a rectangle
\([0,\ell ^*]\times [-\frac{w^*}{2}, \frac{w^*}{2}]\)
with
\(w^* < \frac{\ell ^*}{3(n-1)}\)
. Assume that at least one vertex of
\(\Omega \)
lies on each of the sides
\(x=0\)
and
\(x=\ell ^*\)
. Then
$$\begin{aligned} \sigma _k(\Omega )\le \frac{2k^2(n-1)^2\pi ^3 w^*}{(\ell ^*-3(n-1)w^*)^2}. \end{aligned}$$
There are no assumptions on the perimeter of
\(\Omega \)
, although the hypotheses imply that
\(|\partial \Omega |>2\ell ^*\)
.
Proof
Let
\(\{x_1,\dots , x_m\}\)
be the set of all
x
-coordinates of vertices of
\(\Omega \)
, labelled so that
\(0=x_1<x_2\dots <x_m=\ell \)
. There may be more than one vertex with a given
x
-coordinate, so
m
can be less than
n
. We emphasize that the labelling of the
\(x_i\)
’s does not coincide with the usual cyclical labelling of vertices. Since
\(m\le n\)
, at least one index
\(i\in \{2,\dots , m\}\)
satisfies
\(x_i-x_{i-1}\ge \frac{\ell ^*}{n-1}\)
. Fix such an
i
.
The subrectangle
$$\begin{aligned} R_i:=(x_{i-1},x_i)\times \left( -\frac{w^*}{2},\frac{w^*}{2}\right) \end{aligned}$$
intersects
\(\partial \Omega \)
in an even number of disjoint open segments
\(S_j\)
, each of whose closures
\(\overline{S}_j\)
has endpoints on the two edges
\(\{x_{i-1}\}\times [-\frac{w^*}{2}, \frac{w^*}{2}]\)
and
\(\{x_{i}\}\times [-\frac{w^*}{2}, \frac{w^*}{2}]\)
. This is depicted in Fig.
4
. In general, the evenness follows from there being no vertices with
x
-coordinates contained in
\((x_{i-1}, x_i)\)
. Since the polygon is not collapsed, for each part of the boundary contained in this subrectangle there is an opposing segment, hence the segments come in pairs. Moving vertically down from the top of the subrectangle, one enters
\(\Omega \)
upon crossing the highest segment (call it
\(S_1)\)
, exits
\(\Omega \)
upon crossing the next one
\(S_2\)
, and so forth. If
\(\Omega \)
is convex, there are exactly two such segments; otherwise there can be more than two but we will focus just on the first two in what follows. The region
Q
in
\(R_i\)
between
\(S_1\)
and
\(S_2\)
is either a quadrilateral or a triangle. In either case, we can apply Proposition
3.5
with
\(\ell =\frac{\ell ^*}{n-1}\)
and
\(w=w^*\)
to obtain
$$\begin{aligned} \sigma _k(\Omega )\le \frac{2k^2\pi ^3w}{(\ell -3w)^2}=\frac{2k^2(n-1)^2\pi ^3 w^*}{(\ell ^*-3(n-1)w^*)^2}.\end{aligned}$$
\(\square \)
With the preceding result, we can partially generalize the eigenvalue bound for triangles to all convex polygons.
Theorem 3.10
For
\(n=3,4,5,\dots \)
there exists a constant
\(C_n>0\)
depending only on
n
such that if
\(\Omega \)
is any convex
n
-gon with smallest angle
\(\alpha (\Omega )\)
, then the Steklov eigenvalues of
\(\Omega \)
satisfy
$$\begin{aligned} \sigma _k(\Omega ) L(\partial \Omega ) \le C_n k^2\alpha (\Omega ), \quad \text {for all } k \ge 0. \end{aligned}$$
In particular, this holds with
$$\begin{aligned} C_n = \frac{800 \pi ^3 (n-1)^2}{49}. \end{aligned}$$
Proof
We place
\(\Omega \)
so that the vertex of its smallest interior angle, say of measure
\(\alpha \)
, is at the origin, and the horizontal axis (
x
-axis) bisects this angle. Let
\(\ell \)
be the maximum distance of the vertices of
\(\Omega \)
from the
y
-axis, and assume without loss of generality that the perimeter of
\(\Omega \)
is one. Then
\(\ell < \frac{1}{2}\)
. By convexity,
\(\Omega \)
is contained in the isosceles triangle with vertices (0, 0) and
\((\ell , \pm \ell \tan (\alpha /2))\)
as in Fig.
5
. Moreover, since
\(\ell <\frac{1}{2}\)
, the polygon
\(\Omega \)
lies in a rectangle
R
of length
\(\ell \)
and width
\(w:=\tan (\alpha /2)\)
as in Fig.
5
; the perimeter of
R
is greater than the perimeter of
\(\Omega \)
, i.e., greater than one. Thus
\(2\ell +2w>1\)
and
$$\begin{aligned} \ell >0.5 -w.\end{aligned}$$
(22)
To obtain an upper bound for
w
, assume that
\(\alpha <\frac{1}{7}\)
. The Maclaurin series for the cosine then implies that
\(\cos (\alpha /2)>\frac{97}{98}>0.98\)
. Thus
$$\begin{aligned} w=\tan (\alpha /2)<\frac{\sin (\alpha /2)}{0.98}<\frac{\alpha }{2(0.98)}.\end{aligned}$$
(23)
To apply Proposition
3.9
, we require that
\(\ell -3(n-1)w>0\)
. By Eq.
22
,
$$\begin{aligned} \ell -3(n-1)w> 0.5-w -3(n-1)w=0.5 -(3n-2)w,\end{aligned}$$
so we need that
$$\begin{aligned}w< \frac{1}{2(3n-2)}.\end{aligned}$$
By Eq.
23
, we therefore further assume that
$$\begin{aligned} \alpha<\frac{0.49}{3n-2} \implies w < \frac{1}{4(3n-2)}.\end{aligned}$$
Then Proposition
3.9
and (
23
) give the estimate
$$\begin{aligned} \sigma _k(\Omega )\le \frac{2k^2(n-1)^2\pi ^3 w}{(0.5-w-3(n-1)w)^2}< \frac{8 k^2 (n-1)^2 \pi ^3 \alpha }{0.49}.\end{aligned}$$
(24)
Here we used the calculation that
$$\begin{aligned} (0.5 - w - 3(n-1)w)^2 > \left( \frac{1}{2} - \frac{1}{4(3n-2)} - \frac{3(n-1)}{4(3n-2)} \right) ^2 = \frac{1}{16}.\end{aligned}$$
To obtain this estimate, we required that
\(\alpha < \frac{1}{7}\)
and
\(\alpha < \frac{0.49}{3n-2}\)
. Since
\(n \ge 3\)
, the latter of these two values is smaller. So, now, assume that
\(\alpha \ge \frac{0.49}{3n-2}\)
. In this case we have the Hersch–Payne–Schiffer bound that gives
\(\sigma _k (\Omega ) \le 2 \pi k\)
(see [
13
, p. 102]). Excluding the case
\(k=0\)
, we calculate that
$$\begin{aligned} 2 \pi k \le \frac{800 k^2 (n-1)^2 \pi ^3}{49} \alpha \iff \frac{49}{400 k (n-1)^2 \pi ^2} \le \alpha .\end{aligned}$$
Since we are assuming
\(\alpha \ge \frac{0.49}{3n-2}\)
and
\(k \ge 1\)
, it is enough to show that
$$\begin{aligned} \frac{49}{400(n-1)^2 \pi ^2} \le \frac{49}{100 (3n-2)} \iff \frac{3n-2}{4(n-1)^2 \pi ^2} \le 1.\end{aligned}$$
This is indeed true since
\(n \ge 3\)
. We therefore obtain the eigenvalue estimate for all values of the angle
\(\alpha \)
.
\(\square \)
Fig. 5
Full size image
The polygon
\(\Omega \)
(not shown) lies inside an isosceles triangle, which in turn lies inside a rectangle. One vertex of
\(\Omega \)
is at the origin and at least one vertex of
\(\Omega \)
lies on the righthand edge of the isosceles triangle and thus of the rectangle
Remark 3.11
Note that Theorem
3.10
improves, for the class of convex
n
-gons with
\(\alpha (\Omega )\le \frac{49}{400\pi ^2(n-1)^2k}\)
, the Hersch–Payne–Schiffer estimate
\(\sigma _{k}(\Omega )L(\partial \Omega )\le 2\pi k\)
.
The eigenvalue bounds in Theorem
3.10
can be reversed to yield an inverse spectral result:
Corollary 3.12
Given
n
, let
\(C_n\)
be as in Theorem
3.10
, and let
k
be any positive integer. Then for all convex
n
-gons
\(\Omega \)
, the interior angles
\(\alpha _1,\dots , \alpha _n\)
of
\(\Omega \)
satisfy
$$\begin{aligned} \alpha _j\ge \frac{\sigma _k(\Omega )L(\partial \Omega )}{C_n k^2},\,\,j=1,\dots , n. \end{aligned}$$
Thus a lower bound on the
k
th perimeter-normalized Steklov eigenvalue yields a lower bound on the angles of
\(\Omega \)
. In particular, there exists a uniform lower bound on the angles of any collection of mutually Steklov isospectral convex
n
-gons.
Theorem
2.13
, Lemma
2.16
, and Corollary
3.12
together imply that the characteristic polynomial of an admissible convex
n
-gon
\(\Omega \)
along with a lower bound on the
k
th Steklov eigenvalue for some
\(k\in {\mathbb {Z}}^+\)
suffice to determine
\(\Omega \)
up to finitely many possibilities among all convex
n
-gons. We will see in the next section that the characteristic polynomial alone suffices to obtain finiteness of Steklov isospectral admissible convex
n
-gons. However, Corollary
3.12
will play a role in extending the spectral finiteness results to a larger class of
n
-gons in Sect.
5
. Using Corollary
3.12
, it is possible to obtain finiteness of certain Steklov isospectral sets of convex polygons, but it is not clear if that result alone suffices to obtain an upper bound on the number of such mutually Steklov isospectral non-congruent polygons. For this reason, in the next section we will use a different approach to obtain explicit bounds on the size of such sets.
4
Bounds on the Sizes of Steklov Isospectral Sets of Admissible Convex Polygons
We will give upper bounds on the number of mutually non-congruent convex
n
-gons that can be Steklov isospectral to a given admissible convex
n
-gon. Although we expect the following result is contained in the literature, we include it with a short proof, since it is essential to our results.
Lemma 4.1
Let
\(\Omega \)
be a convex
n
-gon. Assume that we know the cyclically ordered side lengths
\(\pmb {\ell }=(\ell _1,\dots , \ell _n)\)
and the corresponding vector of interior angles
\(\pmb {\alpha }=(\alpha _1,\dots , \alpha _n)\)
but with three of the entries replaced by blank place holders. Then we can uniquely determine the three missing angles and therewith
\(\Omega \)
up to congruence.
Fig. 6
Full size image
A convex
n
-gon (in this case
\(n=5\)
) is shown here with
\(v_n\)
a vertex whose interior angle is known. We divide
\(\Omega \)
by drawing a line segment from
\(v_{n-1}\)
to
\(v_1\)
, splitting
\(\Omega \)
into a convex
\((n-1)-\)
gon
\(\Omega '\)
and a triangle
T
Proof
We prove the lemma by induction. The lemma holds when
\(n=3\)
since triangles that have all their side lengths in common are congruent. Now let
\(n>3\)
and assume the lemma holds for
\((n-1)\)
-gons. Let
\(\Omega \)
be an
n
-gon with the given data. Denote by
\(v_1,\dots , v_n\)
the vertices with the corresponding angles
\(\alpha _1,\dots , \alpha _n\)
. Let
$$\begin{aligned} \mathcal {K}=\{j\in \{1,\dots , n\}:\alpha _j\,\text{ is }\,\text{ known }\}. \end{aligned}$$
For notational convenience in what follows, we assume without loss of generality that
\(n\in \mathcal {K}\)
. (Otherwise, we may cyclically permute the entries of
\(\pmb {\ell }\)
and
\(\pmb {\alpha }\)
.) In particular, the edges
\(v_{n-1}v_n\)
and
\(v_nv_1\)
adjacent to
\(v_n\)
have lengths
\(\ell _n\)
and
\(\ell _1\)
respectively. The line segment
\(v_{n-1}v_1\)
divides
\(\Omega \)
into a triangle
T
with vertices
\(v_{n-1}, v_n, v_1\)
and a necessarily convex
\((n-1)\)
-gon
\(\Omega '\)
with vertices
\(v_1, \dots , v_{n-1}\)
as in Fig.
6
. Since we know the angle of
T
at vertex
\(v_n\)
and the lengths of the two adjacent sides, we can determine
T
. In particular, we can read off the length
\(\ell _1':=|v_{n-1}v_1|\)
. The remaining cyclically ordered side lengths of
\(\Omega '\)
are given by
\(\ell '_j=\ell _j\)
,
\(j=2,\dots , n-1\)
. The angle of
\(\Omega '\)
at vertex
\(v_1\)
is the difference between the angles of
\(\Omega \)
and
T
at that vertex and similarly for the angle at
\(v_{n-1}\)
. Define
\(\mathcal {K}'\)
analogously to
\(\mathcal {K}\)
. Since the interior angles of
T
are known, one easily sees that
$$\begin{aligned} \mathcal {K}'=\mathcal {K}\cap \{1,\dots , n-1\} \end{aligned}$$
and thus
\(\vert \mathcal {K}'\vert =(n-1)-3\)
; i.e., the only missing data for
\(\Omega '\)
consists of three angles. The induction hypothesis yields these three remaining angles of
\(\Omega '\)
, and we can determine the three missing angles of
\(\Omega \)
.
\(\square \)
Theorem 4.2
Let
\(\Omega \)
be a convex admissible
n
-gon and let
\(\operatorname {Iso}_{\operatorname {poly}}(\Omega )\)
be the set of all congruence classes of convex
n
-gons (necessarily admissible) that have the same characteristic polynomial as
\(\Omega \)
. Then the order
\( \vert \operatorname {Iso}_{\operatorname {poly}}(\Omega ) \vert \)
of
\(\operatorname {Iso}_{\operatorname {poly}}(\Omega )\)
satisfies the following:
(a)
If
\(\Omega \)
has no even angles, we have
\( \vert \operatorname {Iso}_{\operatorname {poly}}(\Omega )\vert \le \left( {\begin{array}{c}n\\ 3\end{array}}\right) .\)
(b)
If
\(\Omega \)
has exactly one even angle, then
\( \vert \operatorname {Iso}_{\operatorname {poly}}(\Omega ) \vert \le \left( {\begin{array}{c}n-1\\ n-3\end{array}}\right) =\left( {\begin{array}{c}n-1\\ 2\end{array}}\right) .\)
(c)
If
\(\Omega \)
has exactly two even angles, then
\( \vert \operatorname {Iso}_{\operatorname {poly}}(\Omega ) \vert \le 4(n-2).\)
This bound can be improved to
\(2(n-2)\)
if the even angles are adjacent.
(d)
If
\(\Omega \)
has three even angles, then
\( \vert \operatorname {Iso}_{\operatorname {poly}}\Omega )\vert \le 8\)
. This bound can be improved to 4 if two of the even angles are adjacent and to 2 if all three of the even angles are in consecutive order.
Proof
Recall that the characteristic polynomial determines the number of even angles (see Theorem
2.13
). (a) By Theorem
2.13
(b) and the fact that
\(\Omega \)
is admissible, the characteristic polynomial determines
\(\pmb {\ell }(\Omega )\)
and
\(\pmb {C}_{\operatorname {ab}}(\Omega )\)
modulo a choice of orientation and cyclic labelling. (See Notation and Remarks
2.12
for the definition of
\(\pmb {C}_{\operatorname {ab}}(\Omega )\)
.) For every convex
n
-gon
\(\Omega \)
, at least
\(n-3\)
of the interior angles are obtuse, and Lemma
2.16
tells us that |
c
| is injective on the set of all obtuse angles. Thus, by Lemma
4.1
,
\(\Omega \)
is uniquely determined up to congruence by
\(\pmb {\ell }(\Omega )\)
, the locations (i.e., the corresponding subscripts
j
) of
\(n-3\)
obtuse angles among the
\(\alpha _j\)
’s, and the corresponding values of
\(|c|(\alpha _j)\)
for these obtuse angles. There are
\(\left( {\begin{array}{c}n\\ n-3\end{array}}\right) =\left( {\begin{array}{c}n\\ 3\end{array}}\right) \)
possible ways that the obtuse angles may be distributed among
\(\alpha _1,\dots , \alpha _n\)
.
(b) We may choose the labeling so the unique even angle is
\(\alpha _n\)
. By Remark
2.14
, the characteristic polynomial again determines both
\(\pmb {\ell }(\Omega )\)
and
\(\pmb {C}_{\operatorname {ab}}(\Omega )\)
up to orientation and cyclic relabeling. There are
\(\left( {\begin{array}{c}n-1\\ n-3\end{array}}\right) =\left( {\begin{array}{c}n-1\\ 2\end{array}}\right) \)
possible ways that
\(n-3\)
obtuse angles may be distributed among
\(\alpha _1,\dots , \alpha _{n-1}\)
, and (b) follows.
(c) Let
\(\alpha _m\)
and
\(\alpha _n\)
be the two even angles; here
\(m\in \{1,\dots , n-1\}\)
. The exceptional components then satisfy
\(\pmb {\ell }({\mathcal {Y}}_1)=(\ell _1,\dots ,\ell _m)\)
,
\(\pmb {\ell }({\mathcal {Y}}_2)=(\ell _{m+1},\dots , \ell _n)\)
,
\(\pmb {C}_{\operatorname {ab}}({\mathcal {Y}}_1)=(|c|(\alpha _1),\dots , |c|(\alpha _{m-1}))\)
, and
\(\pmb {C}_{\operatorname {ab}}({\mathcal {Y}}_2)=(|c|(\alpha _{m+1}),\dots , |c|(\alpha _{n-1}))\)
. Corollary
2.18
tells us that this information is determined up to the four possible reorderings that arise from the choices of
\({\mathcal {Y}}_i\)
versus
\(-{\mathcal {Y}}_i\)
. Once the ordering is fixed, it remains to choose
\(n-3\)
obtuse angles among the
\(n-2\)
angles
\(\{ \alpha _1, \dots , \alpha _{n-1}\} {\setminus } \{\alpha _m\}\)
in order to determine
\(\Omega \)
. Thus
\(\Omega \)
is spectrally determined up to at most
\(4\left( {\begin{array}{c}n-2\\ n-3\end{array}}\right) =4(n-2)\)
possibilities. If the even angles are adjacent, then one of the exceptional components
\({\mathcal {Y}}_i\)
consists of a single edge and
\(\pmb {\ell }({\mathcal {Y}}_i)=\pmb {\ell }(-{\mathcal {Y}}_i)\)
. Thus we have only two rather than four possible reorderings, proving the final statement in part (c).
(d) The proof is similar to that of (c). We now have three exceptional components, each of which may undergo a change of orientation, so we have
\(2^3=8\)
possible reorderings. Since we have three even, thus non-obtuse, angles, all the remaining angles are obtuse so there are no further choices to be made. The characterisic polynomial thus determines
\(\Omega \)
up to 8 possibilities. If two of the even angles are adjacent, then the exceptional component between them consists of a single edge and thus
\(\pmb {\ell }({\mathcal {Y}}_i)=\pmb {\ell }(-{\mathcal {Y}}_i)\)
, so we are reduced to
\(2^2=4\)
possibilities. If all three even angles are in consecutive order, then two exceptional components are singleton edges and only the orientation of the remaining exceptional component remains to be determined, thus reducing the size of the isospectral set to at most 2.
\(\square \)
Since the characteristic polynomial is a Steklov spectral invariant, our theorem also quantifies the maximum number of congruence classes of convex admissible
n
-gons that have a common Steklov spectrum. Moreover, for certain convex admissible
n
-gons, that number is one:
Proposition 4.3
Let
\(\Omega \)
be a convex admissible
n
-gon all of whose angles are obtuse. Then
\(\Omega \)
is uniquely determined up to congruence by its Steklov spectrum within the set of all convex
n
-gons.
Proof
The assumption that all angles of
\(\Omega \)
are obtuse says, in particular, that there are no even angles. Thus the spectrum determines
\(\pmb {\ell }(\Omega )\)
and
\(\pmb {C}_{\operatorname {ab}}(\Omega )\)
modulo a choice of orientation and cyclic labelling. By Lemma
2.16
(c), the map
\(|c|: \left( \frac{\pi }{2}, \pi \right) \rightarrow (0,1)\)
is one-to-one on the set of obtuse angles. Consequently, if
\(\Omega '\)
is another convex
n
-gon with
\(\pmb {C}_{\operatorname {ab}}(\Omega ') =\pmb {C}_{\operatorname {ab}}(\Omega )\)
, then the sum of all the angles of
\(\Omega '\)
will be less than
\((n-2)\pi \)
unless
\(\pmb {\alpha }(\Omega ')=\pmb {\alpha }(\Omega )\)
. Thus
\(\Omega '\)
is congruent to
\(\Omega \)
.
\(\square \)
In the proofs of Theorem
4.2
and Proposition
4.3
, we did not use the full strength of the spectral invariant
\(\pm \pmb {C}(\Omega )\)
since we instead used
\(\pmb {C}_{\operatorname {ab}}(\Omega )\)
. We can sometimes improve the upper bound by using the stronger invariant, as we now demonstrate.
Proposition 4.4
Let
\(\Omega \)
be a convex admissible
n
-gon and let
\(\operatorname {Iso}_{\operatorname {Stek}}(\Omega )\)
be the maximal set of all congruence classes of convex
n
-gons that are Steklov isospectral to
\(\Omega \)
. Denote by
b
the number of interior angles of
\(\Omega \)
that lie in
$$\begin{aligned} B^+:=\{\alpha \in (0,\pi ): \,0<c(\alpha )<1\}=\bigcup _{m\in 4{\mathbb {Z}}^+}\, \left( \frac{\pi }{m+1}, \frac{\pi }{m}\right) \cup \left( \frac{\pi }{m}, \frac{\pi }{m-1}\right) . \end{aligned}$$
If
\(n\ge 5\)
, and if
\(\Omega \)
has no even angles, then
\(\vert \operatorname {Iso}_{\operatorname {Stek}}(\Omega )\vert \le \left( {\begin{array}{c}n-b\\ 3\end{array}}\right) \)
. If
\(n\ge 6\)
and if
\(\Omega \)
has one even angle, then
\(\vert \operatorname {Iso}_{\operatorname {Stek}}(\Omega ) \vert \le \left( {\begin{array}{c}n-1-b\\ 2-b\end{array}}\right) \)
. This result also holds when
\(n=5\)
provided that
\(b\le 1\)
.
Proof
We first make some general observations. The fact that all elements of
\(B^+\)
are less than
\(\frac{\pi }{3}\)
implies that
\(b \le 2\)
. Moreover, if
\(\Omega \)
has an even angle less than
\(\frac{\pi }{2}\)
, then
\(b \le 1\)
. If
\(\Omega \)
either has two even angles whose sum is less than
\(\frac{3\pi }{4}\)
, or if
\(\Omega \)
has three even angles, then
\(b=0\)
.
We now assume
\(n \ge 5\)
, and
\(\Omega \)
has no even angles. Since
\(\Omega \)
, being admissible, has no odd angles, and has no even angles, all the entries of
\(\pmb {C}(\Omega )\)
lie in
\((-1,0) \cup (0,1)\)
. Thus
b
is precisely the number of positive entries in
\(\pmb {C}(\Omega )\)
. Since
\(n\ge 5\)
, and
\(b\le 2\)
, the number of negative entries must exceed the number of positive entries and thus knowledge of
\(\pm \pmb {C}(\Omega )\)
uniquely determines
\(\pmb {C}(\Omega )\)
. For any obtuse angle
\(\alpha _j\)
, the corresponding entry
\(c(\alpha _j)\)
is negative. Thus in the proof of Theorem
4.2
(a), we may replace
\(\left( {\begin{array}{c}n\\ 3\end{array}}\right) \)
by
\(\left( {\begin{array}{c}n-b\\ 3\end{array}}\right) \)
.
Next we assume that
\(n \ge 6\)
, and
\(\Omega \)
has one even angle. Following the notation in the proof of Theorem
4.2
(b), we need to count the possible ways
\(n-3\)
obtuse angles may be distributed among
\(\alpha _1,\dots , \alpha _{n-1}\)
. Since
\(\Omega \)
has only one even angle, an argument analogous to the preceding case allows us to determine the sign of the spectral invariant
\(\pm \pmb {C}({\mathcal {Y}})\)
and then to narrow the candidates down to
\(n-1-b\)
, from which we must choose
\(n-3\)
. Thus
\(\vert \operatorname {Iso}_{\operatorname {Stek}}(\Omega )\vert \le \left( {\begin{array}{c}n-1-b\\ n-3\end{array}}\right) =\left( {\begin{array}{c}n-1-b\\ 2-b\end{array}}\right) \)
.
\(\square \)
5
Spectral Finiteness Results for Some Classes Of Weakly Admissible Polygons
Recall that admissibility of an
n
-gon
\(\Omega \)
with all interior angles in
\((0,\pi )\)
says both that the edge lengths are incommensurable over
\(\{-1,0,1\}\)
and that there are no odd angles. In this section we obtain spectral finiteness results for convex
n
-gons satisfying significantly weaker hypotheses.
Definition 5.1
Let
\(\Omega \)
be a convex
n
-gon.
(a)
Let
k
be the number of odd interior angles in
\(\Omega \)
. If
\(k=0\)
, set
\(\Omega ^{\operatorname {red}}:=\Omega \)
. If
\(k=1\)
or 2, let
\(\Omega ^{\operatorname {red}}\)
be a curvilinear
\((n-k)\)
-gon obtained by “removing” the vertices where the odd angles occur. More precisely, if
\(\alpha _j\)
is an odd angle and
\(\ell _j\)
and
\(\ell _{j+1}\)
are the lengths of the two edges that meet at the vertex with angle
\(\alpha _j\)
, then replace the two edges by a single smooth curve of length
\(\ell _j+\ell _{j+1}\)
, being careful not to affect the adjacent vertex angles
\(\alpha _{j-1}\)
and
\(\alpha _{j+1}\)
. If there are two odd angles, repeat the process. In particular, if odd angles
\(\alpha _{j-1}\)
and
\(\alpha _j\)
occur at adjacent vertices of
\(\Omega \)
, then the three edges incident to these two vertices are replaced by a single smooth curve of length
\(\ell _{j-1}+\ell _j+\ell _{j+1}\)
. The only convex polygons with more than two odd angles are equilateral triangles. In this case,
\(\Omega ^{\operatorname {red}}\)
is a smooth simply-connected domain, and the characteristic polynomial of
\(\Omega ^{\operatorname {red}}\)
is defined as in Remark
2.6
. We refer to
\(\Omega ^{\operatorname {red}}\)
as the reduced curvilinear
\((n-k)\)
-gon associated with
\(\Omega \)
.
(b)
We say that a convex
n
-gon is
weakly edge-admissible
if the edge lengths of
\(\Omega ^{\operatorname {red}}\)
are incommensurable over
\(\{-1,0,1\}\)
. Observe that incommensurability of the edge lengths of
\(\Omega \)
over
\(\{-1,0,1\}\)
implies that
\(\Omega \)
is weakly edge-admissible.
Remark 5.2
We note that
\(\Omega ^{\operatorname {red}}\)
is well-defined only up to the choice of the smooth curves replacing the pairs of edges that meet at an odd angle. In what follows, the choice of curves will not matter. What will be important are the lengths of these smooth curves and the fact that they are not straight line segments. The latter distinguishes them from the other edges of
\(\Omega ^{\operatorname {red}}\)
.
Fig. 7
Full size image
On the left, a
\(30^\circ \)
–
\(60^\circ \)
–
\(90^\circ \)
triangle, having one odd angle, is shown together with its associated reduced curvilinear 2-gon in blue. On the right, a triangle with two odd angles each measuring
\(\frac{\pi }{9}\)
is shown together with its associated reduced curvilinear 1-gon in blue(Color figure online)
Large classes of polygons are weakly edge-admissible. In particular, triangles with one odd angle are weakly edge-admissible by the triangle inequality. If a triangle has 2 or 3 odd angles, then the only edge length of
\(\Omega ^{\operatorname {red}}\)
is its perimeter; with 3 odd angles, its reduced curvilinear polygon is a smoothly bounded domain. Examples of triangles with one and two odd angles and their associated reduced curvilinear polygons are shown in Fig.
7
. In addition to triangles, every convex quadrilateral
\(\Omega \)
that has two adjacent odd interior angles is necessarily weakly edge-admissible. Indeed, suppose angles
\(\alpha _2\)
and
\(\alpha _3\)
are odd. Then
\(\Omega ^{\operatorname {red}}\)
has only two edges of lengths
\(\ell _1':=\ell _1\)
and
\(\ell _2':=\ell _2+\ell _3+\ell _4\)
, respectively, where the
\(\ell _j\)
’s are the edge lengths of
\(\Omega \)
. Since all edges have positive length and since we necessarily have
\(\ell _1<\ell _2+\ell _3+\ell _4\)
, the set
\(\{\ell _1',\ell _2'\}\)
is incommensurable over
\(\{-1,0,1\}\)
.
Lemma 5.3
We use the notation of Definition
5.1
. Let
\(\Omega \)
be a weakly edge-admissible convex
n
-gon. Let
k
be the number of odd interior angles in
\(\Omega \)
. Then:
(a)
\(\Omega ^{\operatorname {red}}\)
is either an admissible curvilinear
\((n-k)\)
-gon or a domain with smooth boundary if
\(n=k=3\)
;
(b)
The characteristic polynomials of
\(\Omega \)
and
\(\Omega ^{\operatorname {red}}\)
are identical except possibly for a change in the sign of the constant term. The sign will depend on the parity of the odd angles in the sense of Definition
2.9
.
(c)
If
\(\Omega \)
is not an equilateral triangle, the characteristic polynomial of
\(\Omega \)
determines
\(\pmb {C}_{\operatorname {ab}}(\Omega ^{\operatorname {red}})\)
and
\(\pmb {\ell }(\Omega ^{\operatorname {red}})\)
up to possible permutations of the entries. Moreover, unless
\(\Omega \)
has more than one even angle, the characteristic polynomial of
\(\Omega \)
determines
\(\pmb {C}_{\operatorname {ab}}(\Omega ^{\operatorname {red}})\)
and
\(\pmb {\ell }(\Omega ^{\operatorname {red}})\)
uniquely (modulo the choice of boundary orientation and cyclic labelling).
We have excluded equilateral triangles in part (c) only because we have not defined
\(\pmb {C}_{\operatorname {ab}}(\Omega ^{\operatorname {red}})\)
when
\(\Omega ^{\operatorname {red}}\)
has smooth boundary.
Proof
(a) is immediate from Definitions
2.9
and
5.1
.
(b) Under the hypothesis of weak edge-admissibility, it is straightforward to see from Definition
2.2
that the non-constant terms of the characteristic polynomials of
\(\Omega \)
and
\(\Omega ^{\operatorname {red}}\)
are identical, since
\(c(\alpha _j)=0\)
when
\(\alpha _j\)
is odd. Moreover weak edge-admissibility implies that the constant term in the characteristic polynomial of
\(\Omega \)
is given by
\(\prod _{j=1}^n\,\sin \left( \frac{\pi ^2}{2\alpha _j}\right) .\)
Any odd angles contribute a factor of
\(\pm 1\)
to this product, while the product of the remaining factors yields the constant term in the characteristic polynomial of
\(\Omega ^{\operatorname {red}}\)
.
(c) Observe that for any admissible curvilinear polygon
\(\Sigma \)
, the data
\(\pmb {C}(\Sigma )\)
and
\(\pmb {\ell }(\Sigma )\)
are independent of the sign of the constant term in the characteristic polynomial of
\(\Sigma \)
. We can now apply parts (a) and (b) along with Theorem
2.13
and Remark
2.14
to complete the proof.
\(\square \)
Before addressing spectral finiteness, we observe the following consequence of Lemma
5.3
:
Proposition 5.4
Let
\(\Omega _1\)
and
\(\Omega _2\)
be weakly edge-admissible convex
n
-gons that have the same characteristic polynomial. If all angles of
\(\Omega _1\)
are rational multiples of
\(\pi \)
, then the same is true for all angles of
\(\Omega _2\)
.
Proof
Applying Remark
2.15
along with Lemma
5.3
(c), we see that all angles of
\(\Omega ^{\operatorname {red}}_2\)
are rational multiples of
\(\pi \)
. The only remaining angles of
\(\Omega ^{\operatorname {red}}_2\)
are odd angles, which are necessarily rational multiples of
\(\pi \)
.
\(\square \)
Theorem 5.5
Let
\(\mathcal {P}^*\)
be the set of all weakly edge-admissible convex polygons; moreover, assume that if the polygon contains two odd angles, then they are adjacent. Let
S
be any subset of
\(\mathcal {P}^*\)
consisting of congruence classes of convex polygons that have the same characteristic polynomial and that share a common lower bound on their
k
th perimeter-normalized Steklov eigenvalue for some
\(k\in {\mathbb {Z}}^+\)
. Then
S
is finite. In particular, any set of mutually Steklov isospectral elements of
\(\mathcal {P}^*\)
is finite.
Fig. 8
Full size image
A convex quadrilateral is shown here with fixed interior angles. Connecting points on the rays
R
and
\(R'\)
by lines parallel to the side of the quadrilateral connecting the upper vertices generates a family of quadrilaterals with the same interior angles
To prove Theorem
5.5
we require the following geometric lemma.
Lemma 5.6
A convex quadrilateral is uniquely determined up to congruence by its four labeled angles, one labeled side length, and its perimeter.
Proof of Lemma 5.6
Let
Q
be a convex quadrilateral with the given data. Let
\(\ell \)
be the known side length. Situate
Q
in the plane so that the edge with the prescribed length is the interval
I
on the
x
-axis with endpoints (0, 0) and
\((\ell , 0)\)
and such that
Q
lies in the closed upper half plane. There are two edges adjacent to
I
on the rays
R
and
\(R'\)
emanating upwards from the endpoints of
I
at the prescribed angles; the fourth edge of
Q
, which is opposite
I
, must have endpoints on
R
and
\(R'\)
and make the prescribed angles with these rays. The assumption that there exists at least one quadrilateral with the given data guarantees the existence of at least one line segment joining
R
and
\(R'\)
at the prescribed angles. Then there exists a continuum of such segments, all mutually parallel as in Fig.
8
. Each gives rise to a convex quadrilateral with the prescribed angles and side length. However, the perimeters of these quadrilaterals strictly increase as the distance from the segment to the
x
-axis increases. Thus there can be only one such quadrilateral with the prescribed perimeter.
\(\square \)
Proof of Theorem 5.5
Write
$$\begin{aligned} \mathcal {P}^{*} =\bigcup _{n=3}^\infty \,\mathcal {P}^*(n), \end{aligned}$$
where
\(\mathcal {P}^*(n)\)
consists of all convex
n
-gons in
\(\mathcal {P}^*\)
. Equilateral triangles are distinguishable from other elements of
\(\mathcal {P}^{*}\)
by the number of cosine terms in their characteristic polynomials (see Lemma
5.3
, Remark
2.6
, and the observations immediately preceding Proposition
2.10
). Thus for notational simplicity, we will exclude equilateral triangles in the remainder of the proof. For
\(\Omega \in \mathcal {P}^*\)
, Lemma
5.3
implies that the characteristic polynomial of
\(\Omega \in \mathcal {P}^*\)
determines the number of vertices in
\(\Omega ^{\operatorname {red}}\)
. Since each
\(\Omega \in \mathcal {P}^*\)
has at most three more vertices than
\(\Omega ^{\operatorname {red}}\)
, any set
S
as above can intersect
\(\mathcal {P}^*(n)\)
for at most four values of
n
. To prove finiteness, it thus suffices to fix
n
and show that each
\(\Omega \in \mathcal {P}^*(n)\)
is determined up to finitely many possibilities in
\(\mathcal {P}^*(n)\)
by its characteristic polynomial and a Steklov eigenvalue bound as in the statement of the theorem.
If
\(\Omega \)
has no odd angles, then it is necessarily admissible and we may apply Theorem
4.2
to complete the proof. Thus we assume that
\(\Omega \)
has at least one odd angle. Each of the following are determined up to finitely many possibilities by the characteristic polynomial and the eigenvalue bound:
(i)
\(\pmb {C}_{\operatorname {ab}}(\Omega ^{\operatorname {red}})\)
and
\(\pmb {\ell }(\Omega ^{\operatorname {red}})\)
by Lemma
5.3
;
(ii)
the number of odd angles in
\(\Omega \)
, since
n
is fixed and we know the number of angles in
\(\Omega ^{\operatorname {red}}\)
;
(iii)
\(\pmb {\alpha }(\Omega ^{\operatorname {red}})\)
and also the values of the odd angles by (i), Corollary
3.12
and Lemma
2.16
;
(iv)
the location of the odd angles: indeed, all but one of the edges of
\(\Omega ^{\operatorname {red}}\)
is a straight line segment, since all odd angles of
\(\Omega \)
are assumed to be adjacent. There are only finitely many choices for this edge and thus for the odd angles.
To complete the proof of finiteness, it thus suffices to fix a choice of the data (i)–(iv) and show that there is at most one convex
n
-gon with the given data. The data gives us
all
the angles
\(\alpha _1,\dots ,\alpha _n\)
of
\(\Omega \)
, the lengths of all the edges that join the non-odd angles, and the sum of the lengths of those edges that are adjacent to odd angles (in particular, the perimeter of
\(\Omega \)
).
If
\(n=3\)
, the angles along with the perimeter determine
\(\Omega \)
. Thus we assume
\(n\ge 4\)
. Let
\(k\in \{1,2\}\)
be the number of odd angles of
\(\Omega \)
. For notational simplicity, we cyclically relabel the vertices of
\(\Omega \)
so that
\(\alpha _n\)
, and also
\(\alpha _{n-1}\)
if
\(k=2\)
, are the odd angles. In addition to knowing all the angles of
\(\Omega \)
, we know
\(\ell _2,\dots , \ell _{n-k}\)
and the perimeter. It remains to determine the remaining lengths.
If
\(n=4\)
, then we can apply Lemma
5.6
, with
\(\ell _2\)
playing the role of the known edge length, to complete the proof. Thus assume
\(n\ge 5\)
. For
\(j=1,\dots , n\)
, we denote by
\(v_j\)
the
j
th vertex of
\(\Omega \)
and by
\(e_j\)
the
j
th edge, so the angle at
\(v_j\)
is
\(\alpha _j\)
and the length of
\(e_j\)
is
\(\ell _j\)
. The line segment
\(v_{n-k}v_1\)
divides
\(\Omega \)
into a convex
\((n-k)\)
-gon
\(\Omega '\)
with vertices
\(v_1,\dots , v_{n-k}\)
and edges
\(e_2,\dots , e_{n-k}, v_{n-k}v_1\)
and a convex
\((k+2)\)
-gon
\(\Omega ''\)
(so a triangle or a quadrilateral) whose edge set consists of
\(v_{n-k}v_1\)
along with the edges of
\(\Omega \)
adjacent to the odd angle(s). This is shown in Fig.
9
. It’s easy to see that the known data
\(\ell _2,\dots , \ell _{n-k}, \alpha _2,\dots , \alpha _{n-k-1}\)
determines
\(\Omega '\)
. Consequently, we know the edge length
\(|v_{n-k}v_1|\)
and we know the angles of
\(\Omega '\)
at
\(v_{n-k}\)
and
\(v_1\)
. From these angles along with our knowledge of
\(\alpha _{n-k}\)
and
\(\alpha _1\)
from
\(\pmb {\alpha }(\Omega ^{\operatorname {red}})\)
, we also know the angles of
\(\Omega ''\)
at these two vertices. Thus we know the information angle-side-angle (ASA) for
\(\Omega ''\)
. If
\(k=1\)
so that
\(\Omega ''\)
is a triangle, this determines
\(\Omega ''\)
. If
\(k=2\)
, we use Lemma
5.6
and the fact that we also know the sum of the remaining edge lengths of
\(\Omega ''\)
(equivalently, we know the perimeter of
\(\Omega ''\)
) to recover
\(\Omega ''\)
. We have thus determined the remaining side lengths of
\(\Omega \)
, completing the proof.
\(\square \)
Fig. 9
Full size image
Two convex 5-gons are shown here, the left having one odd angle at vertex
\(v_5\)
while the right has two odd angles at vertices
\(v_4\)
and
\(v_5\)
. The 5-gons are split into
\(\Omega ''\)
and
\(\Omega '\)
by joining
\(v_1\)
to
\(v_4\)
or
\(v_3\)
, respectively
To complete our discussion of weakly edge-admissible convex polygons it remains to consider those with two non-adjacent odd angles. Note that any such polygon necessarily has at least four vertices. We will denote by
\(\mathcal {P}^{**}\)
the class of all such convex polygons and write
$$\begin{aligned} \mathcal {P}^{**}=\cup _{n=4}^\infty \, \mathcal {P}^{**}(n) \end{aligned}$$
where
\(\mathcal {P}^{**}(n)\)
consists of all
n
-gons in
\(\mathcal {P}^{**}\)
.
The known Steklov spectral invariants do not suffice to show in full generality that Steklov isospectral sets of such polygons are finite. Indeed, we will see below that some convex polygons in this class can be continuously deformed while keeping all angles fixed and keeping the characteristic polynomial fixed. However, we will also show that most convex polygons in this class are finitely determined within
\(\mathcal {P}^{**}\)
by their characteristic polynomials alone.
Proposition 5.7
For
\(\Omega \in \mathcal {P}^{**}\)
, the characteristic polynomial yields the following data:
(a)
the number
n
of vertices;
(b)
\(\pmb {C}(\Omega ^{\operatorname {red}})\)
and
\(\pmb {\ell }(\Omega ^{\operatorname {red}})\)
(both uniquely, modulo the choice of boundary orientation and cyclic labeling);
(c)
\(\pmb {\alpha }(\Omega ^{\operatorname {red}})\)
up to at most
\(n-1\)
explicit possibilities and typically uniquely (modulo the choice of boundary orientation and cyclic labeling);
(d)
the values of the two odd angles of
\(\Omega \)
up to finitely many explicit possibilities.
Consequently, the characteristic polynomial of
\(\Omega \)
determines
\(\pmb {\alpha }(\Omega )\)
up to finitely many explicit possibilities. For each such choice of
\(\pmb {\alpha }(\Omega )\)
, the characteristic polynomial uniquely determines all the edge lengths except for the pairs of edges incident on the odd angles. For the latter, the characteristic polynomial determines the sum of the lengths of the edges in each pair.
Proof
(a) follows from Lemma
5.3
since
\(\Omega \)
has exactly two more vertices than
\(\Omega ^{\operatorname {red}}\)
. Next consider (b). Since the sum of the two odd angles is at most
\(\frac{2\pi }{3}\)
, we have
$$\begin{aligned} \pmb {\alpha }(\Omega ^{\operatorname {red}})\in \left( \frac{\pi }{3}, \pi \right) ^{n-2}\end{aligned}$$
(25)
and at most one angle of
\(\Omega ^{\operatorname {red}}\)
is non-obtuse.
In particular,
\(\Omega ^{\operatorname {red}}\)
has at most one even angle, and then the even angle must be a right angle. (b) now follows from Lemma
5.3
(c) along with the fact that
\(c(\alpha )<0\)
for all
\(\alpha \in (\frac{\pi }{3},\pi )\)
.
We apply (b) and Lemma
2.16
to prove (c). If
\(\pmb {C}(\Omega ^{\operatorname {red}})\)
has an entry
\(-1\)
, necessarily corresponding to a right angle, then
\(\pmb {C}(\Omega ^{\operatorname {red}})\)
determines
\(\pmb {\alpha }(\Omega ^{\operatorname {red}})\)
uniquely since the remaining angles are obtuse. Otherwise, each of the
\(n-2\)
entries in
\(\pmb {C}(\Omega ^{\operatorname {red}})\)
corresponds to a possible location of one non-obtuse angle in
\((\frac{\pi }{3}, \frac{\pi }{2})\)
; for each entry, Lemma
2.16
(c) implies that we know the angle. It is also possible that all angles are obtuse, giving a total of
\(n-1\)
possibilities for
\(\pmb {\alpha }(\Omega ^{\operatorname {red}})\)
. To prove generic uniqueness, suppose that
\(\pmb {\gamma }:=(x_1\pi ,\dots , x_{n-2}\pi )\)
and
\(\pmb {\delta }:=(y_1\pi ,\dots , y_{n-2}\pi )\)
are two of the possible
\(n-1\)
candidates for
\(\pmb {\alpha }(\Omega ^{\operatorname {red}})\)
. If
\(x_j\ne y_j\)
, Eq. (
25
) and Lemma
2.16
imply that one of
\(x_j\pi ,y_j\pi \)
lies in
\((\frac{\pi }{3},\frac{\pi }{2})\)
and the other in
\((\frac{\pi }{2},\pi )\)
. Since (b) says that
\(c(x_j\pi )=c(y_j\pi )\)
, we then have
\(\frac{\pi ^2}{2 x_j\pi }=2\pi -\frac{\pi ^2}{2 y_j\pi }\)
. Thus
$$\begin{aligned} y_j=\frac{x_j}{4x_j-1} \,\,\text{ and }\,\,x_j=\frac{y_j}{4y_j-1}. \end{aligned}$$
Hence
$$\begin{aligned} y_j\pi -x_j\pi = \pi \frac{2x_j-4x_j^2}{4x_j-1}. \end{aligned}$$
(26)
Define
D
to be the discrete set given by
\(D=\{\frac{\pi }{2p+1}+\frac{\pi }{2q+1}:\,\,p,q\in {\mathbb {Z}}^+\}\)
. Let
\(s(\pmb {\gamma })=x_1\pi +\dots +x_{n-2}\pi \)
and
\(s(\pmb {\delta })=y_1\pi +\dots +y_{n-2}\pi \)
. Observe that both
\((n-2)\pi -s(\pmb {\gamma })\)
and
\((n-2)\pi -s(\pmb {\delta })\)
lie in
D
. Thus
$$\begin{aligned} s(\pmb {\gamma })-s(\pmb {\delta })\in D -D =\{a-b: \,a,b\in D\}.\end{aligned}$$
(27)
Equations (
26
) and (
27
) together imply the generic uniqueness of
\(\Omega ^{\operatorname {red}}\)
.
Next consider (d). Given any fixed choice of
\(\pmb {\alpha }(\Omega ^{\operatorname {red}})\)
in (c), let
\(\mu \)
be the sum of the entries. Then the sum of the two odd angles is
\((n-2)\pi -\mu \)
, so at least one of the odd angles is greater than or equal to
\(\frac{1}{2}[(n-2)\pi -\mu ]\)
. Hence there are only finitely many possible values for the odd angles, and they are explicitly computable.
For the final statement of the proposition, items (c) and (d) together yield
\(\pmb {\alpha }(\Omega )\)
up to finitely many possibilities. (Missing from (c) and (d) is the location of the two odd angles—equivalently the determination of which edges of
\(\Omega ^{\operatorname {red}}\)
have non-trivial curvature—but there are only finitely many possible locations.) For each of the finitely many choices of
\(\pmb {\alpha }(\Omega )\)
, the assertion concerning the edge lengths is equivalent to the knowledge of
\(\pmb {\ell }(\Omega ^{\operatorname {red}})\)
, guaranteed by (b).
\(\square \)
Given
\(\Omega \in \mathcal {P}^{**}\)
, consider the set of all convex polygons in
\(\mathcal {P}^{**}\)
that have the same characteristic polynomial as
\(\Omega \)
. To determine whether this set is finite, it remains only to determine for each of the finitely many choices of
\(\pmb {\alpha }(\Omega )\)
in Proposition
5.7
whether we can recover the lengths of the edges adjacent to the odd angles from our knowledge of
\(\pmb {\alpha }(\Omega )\)
and of the other edge lengths. The following purely geometric lemma tells us that generically these lengths are uniquely determined but that, when the genericity condition fails, the edge lengths can be continuously deformed without affecting the characteristic polynomial. For notational simplicity in the lemma, we cyclically relabel the vertices so that the odd angles are labeled
\(\alpha _1\)
and
\(\alpha _m\)
for some
m
. The restriction on
m
in the lemma is the condition that the two odd angles are not adjacent.
Lemma 5.8
Fix
m
with
\(3\le m\le n-1\)
. Suppose that the following data for a convex
n
-gon
\(\Omega \)
is known:
$$\begin{aligned} \alpha _1, \dots , \alpha _n\end{aligned}$$
(28)
and
$$\begin{aligned} \ell _1+\ell _2, \,\ell _3,\dots , \ell _{m-1}, \,\ell _m+\ell _{m+1},\,\ell _{m+2},\dots , \ell _{n}.\end{aligned}$$
(29)
Let
$$\begin{aligned} \Psi =\sum _{i=2}^{m-1}\,(\pi -\alpha _i)\,\,\text{ and }\,\,\Phi =\sum _{j=m+1}^{n}\,(\pi -\alpha _j). \end{aligned}$$
(a)
If
\(\Psi \ne \Phi \)
, then
\(\Omega \)
is uniquely determined up to congruence by this data.
(b)
If
\(\Psi =\Phi \)
, then one can continuously deform
\(\Omega \)
without changing the data above.
Proof
Denote the vertices of
\(\Omega \)
by
\(v_1,\dots , v_n\)
. We first claim that
\(\Psi =\Phi \)
if and only if the bisector
\(\mathcal {L}_m\)
of the angle
\(\alpha _m\)
at
\(v_m\)
is parallel to the bisector
\(\mathcal {L}_1\)
of
\(\alpha _1\)
at
\(v_1\)
.
Consider two polygonal paths between
\(v_1\)
and
\(v_m\)
given by
\(P: v_1,v_2,\dots , v_{m}\)
and
\(Q: v_1, v_n, \dots , v_{m+1}, v_m\)
. Since
\(\Omega \)
is convex, each of these paths has curvature of constant sign. Due to the opposite orientations, the curvatures of
P
and
Q
have opposite sign.
\(\Psi \)
and
\(\Phi \)
are precisely the absolute values of the total curvatures of
P
and
Q
, respectively, and measure the change in the direction of the tangents to the initial and final segments. The initial segments of the two paths make the same angle with
\(\mathcal {L}_1\)
, differing only by reflection across
\(\mathcal {L}_1\)
. Consequently, letting
\(\mathcal {L}\)
denote the line through
\(v_m\)
parallel to
\(\mathcal {L}_1\)
, we have
\(\Psi =\Phi \)
if and only if the final segments of
P
and
Q
make equal angles with
\(\mathcal {L}\)
, i.e., if and only if
\(\mathcal {L}_m=\mathcal {L}\)
.
We now prove statements (a) and (b). We may assume
\(\Omega \)
has perimeter one. Write
\(h=\ell _1+\ell _2\)
and
\(k=\ell _m+\ell _{m+1}.\)
Situate
\(\Omega \)
in the plane and let
\(\textbf{u}_1, \dots , \textbf{u}_n\)
be unit vectors parallel to the edges
\(e_1, \dots , e_n\)
, oriented so that
\(\textbf{u}_j\)
points in the direction from
\(v_{j-1}\)
to
\(v_j\)
. Observe that
\(\textbf{u}_2, \dots , \textbf{u}_n\)
are uniquely determined by
\(\textbf{u}_1\)
and the angles
\(\alpha _1,\dots , \alpha _n\)
. Using the fact that the boundary of
\(\Omega \)
is a closed polygonal path, we see that the edge lengths satisfy the following system of linear equations:
$$\begin{aligned} {\left\{ \begin{array}{ll}\ell _1\textbf{u}_1+ \ell _2\textbf{u}_2 +\ell _{m}\textbf{u}_m+\ell _{m+1}\textbf{u}_{m+1} = -\textbf{c}\\ \ell _1+\ell _2=h\\ \ell _m+\ell _{m+1}=k \end{array}\right. } \end{aligned}$$
(30)
where
\(\textbf{c}\)
is the constant vector
$$\begin{aligned} \textbf{c}=\sum _{j\ne 1, 2, m, m+1}\,\ell _j\textbf{u}_j. \end{aligned}$$
We know that this system has a solution with all the
\(\ell _j\)
strictly positive since we began with the data for a convex
n
-gon
\(\Omega \)
. In view of the last two equations, any other solution
\(\ell _1', \ell _2', \ell _m', \ell _{m+1}'\)
must satisfy
$$\begin{aligned} \ell _1'=\ell _1+x,\,\, \ell _2'=\ell _2-x,\,\, \ell _m'=\ell _m+y,\,\,\ell _{m+1}'=\ell _{m+1}-y \end{aligned}$$
for some
x
,
y
. The first equation then implies that
$$\begin{aligned} x(\textbf{u}_1-\textbf{u}_2) = y(\textbf{u}_{m+1}-\textbf{u}_m).\end{aligned}$$
(31)
Unless
\(\textbf{u}_2-\textbf{u}_1\)
is parallel to
\(\textbf{u}_{m+1}-\textbf{u}_m\)
, Eq.
31
implies that
\(x=y=0\)
, and thus the system given by (
30
) has a unique solution; equivalently,
\(\Omega \)
is uniquely determined up to congruence. Now observe that
\(\textbf{u}_2-\textbf{u}_1\)
, respectively
\(\textbf{u}_{m+1}-\textbf{u}_m\)
, is the bisector of angle
\(\alpha _1\)
, respectively
\(\alpha _m\)
, in
\(\Omega \)
. As noted above, the hypothesis of part (a) is precisely the condition that the two bisectors are not parallel. This proves (a).
On the other hand, if the bisectors are parallel, i.e., if the hypothesis of part (b) holds, then for any
x
and
y
sufficiently small, we get another solution
\(\ell _1', \ell _2', \ell _m', \ell _{m+1}'\)
with all entries positive. This yields a new closed polygonal path. By continuity, if
x
and
y
are sufficiently small, this path must also bound a convex
n
-gon. Part (b) now follows.
\(\square \)
In the case of quadrilaterals, we can say much more; the following lemma is independent of whether the odd angles are adjacent.
Lemma 5.9
Within the class of all weakly edge-admissible convex quadrilaterals with two odd angles, the characteristic polynomial determines whether the two non-odd angles are equal. Moreover, if they are equal, then the characteristic polynomial determines their value.
Proof
Let
\(\Omega \)
and
\(\Omega '\)
lie in this class of quadrilaterals; assume that they have the same characteristic polynomial. Denote by
\(\gamma \)
and
\(\delta \)
, respectively
\(\gamma '\)
and
\(\delta '\)
, the two angles of
\(\Omega \)
, respectively
\(\Omega '\)
, that are not odd. Suppose that one of
\(\Omega \)
and
\(\Omega '\)
, say
\(\Omega \)
, has two equal angles, i.e.,
\(\gamma =\delta \)
. We need to show that
\(\gamma '=\delta '=\gamma \)
. Since the sum of any two odd angles is at most
\(\frac{2\pi }{3}\)
, the two equal angles
\(\gamma \)
and
\(\delta \)
are obtuse. Moreover,
$$\begin{aligned} \gamma ',\,\delta '\in \left( \frac{\pi }{3}, \pi \right) ,\end{aligned}$$
(32)
and at least one of these angles, say
\(\gamma '\)
, is obtuse.
By Lemma
5.3
(c), we have
\(\{|c|(\gamma '), |c|(\delta ')\}= \{|c|(\gamma ), |c|(\delta )\}\)
. Since
\(\gamma \)
and
\(\gamma '\)
are both obtuse, we must then have
\(\gamma =\gamma '\)
by Lemma
2.16
(c). If
\(\delta '\)
is also obtuse, then
\(\delta '=\gamma =\gamma '\)
and we are done.
Suppose that
\(\delta '\)
is not obtuse. Then
\(\delta '\in \left( \frac{\pi }{3}, \frac{\pi }{2}\right) \)
by Eq.
32
. (We can’t have
\(\delta '=\frac{\pi }{2}\)
since
\(|c|(\delta ')=|c|(\delta ).\)
) Let
\(\pi x\)
be the sum of the two odd angles of
\(\Omega \)
, where
\(x \in (0, \frac{2}{3}]\)
. Then the sum of the odd angles of
\(\Omega '\)
is given by
$$\begin{aligned} S(x):=\pi x + \delta -\delta '.\end{aligned}$$
(33)
To get a contradiction, it suffices to show that
\(S(x)>\frac{2\pi }{3}\)
. We have
$$\begin{aligned} \delta =\gamma =\pi \frac{2-x}{2}\,\,\text{ so }\,\,\frac{\pi ^2}{2\delta }=\frac{\pi }{2-x}. \end{aligned}$$
Since
\(|c|(\delta )=|c|(\delta ')\)
and
\(\frac{\pi ^2}{2\delta }\in \left( \frac{\pi }{2},\pi \right) \)
while
\(\frac{\pi ^2}{2\delta '}\in \left( \pi ,\frac{3\pi }{2}\right) \)
, we have
$$\begin{aligned} \frac{\pi ^2}{2\delta '}=2\pi - \frac{\pi ^2}{2\delta }= \pi \frac{3-2x}{2-x} \,\,\text{ so }\,\, \delta '= \pi \frac{2-x}{6-4x}. \end{aligned}$$
Thus
$$\begin{aligned} S(x)=\pi \left[ \frac{2-x^2}{3-2x}\right] . \end{aligned}$$
One easily checks that
\(S(x)>\frac{2\pi }{3}\)
, and the lemma follows.
\(\square \)
Remark 5.10
If a weakly edge-admissible convex quadrilateral
\(\Omega \)
has two non-adjacent odd angles and two equal non-odd angles, then Lemma
5.8
shows that one can continuously deform the edge lengths without affecting either the characteristic polynomial or the angles.
Theorem 5.11
Let
\(\Omega \)
be any weakly edge-admissible convex quadrilateral other than those in Remark
5.10
. Then the characteristic polynomial of
\(\Omega \)
and a lower bound on the
k
th Steklov eigenvalue for some
\(k\in {\mathbb {Z}}^+\)
together determine
\(\Omega \)
up to finitely many possibilities within the class of all weakly edge-admissible convex quadrilaterals.
Proof
If
\(\Omega \)
has no odd angles, then it is admissible, and the proof is completed by Theorem
4.2
. If
\(\Omega \)
has one odd angle or has two adjacent odd angles, then the proof is completed by Theorem
5.5
. We are left with the case that
\(\Omega \)
has two non-adjacent odd angles and two unequal non-odd angles. Any other weakly edge-admissible quadrilateral with the same characteristic polynomial as
\(\Omega \)
must also have two odd angles, and Lemma
5.9
tells us that the non-odd angles are unequal. Choosing the cyclic ordering so that
\(\alpha _1\)
and
\(\alpha _3\)
are the odd angles, Proposition
5.7
yields
\(\pmb {\alpha }(\Omega )\)
up to finitely many possibilities. Lemma
5.3
also yields
\(\ell _1+\ell _2\)
and
\(\ell _3+\ell _4\)
. Thus all the hypotheses of Lemma
5.8
hold which, together with the fact that
\(\Phi \ne \Psi \)
, concludes our proof.
\(\square \)
6
Outlook
We obtained a collection of inverse spectral results for the Steklov eigenvalue problem on polygonal domains. It is natural to compare these results and, more generally, the results of [
22
] for simply connected curvilinear domains, with the analogous inverse results for the Laplace eigenvalue problem with Dirichlet or Neumann boundary conditions. The Laplace spectrum distinguishes simply-connected curvilinear polygons from all bounded plane domains, simply-connected or otherwise, with smooth boundary; see [
26
] (Dirichlet case) and [
28
] (Neumann and Dirichlet). The latter article also obtains similar results with Robin boundary conditions. The article [
29
] extends these results to more general surfaces with piecewise smooth boundary under an additional hypothesis on the Euler characteristic. However, it is not known whether the Laplace spectrum detects the number of vertices in a curvilinear domain. In contrast, while the question of whether the Steklov spectrum can always distinguish curvilinear polygons from smooth domains remains open, the results of [
22
] for the Steklov problem provide much greater information (e.g., number of vertices, edge lengths) for admissible—thus generic—curvilinear
n
-gons with all angles in
\((0,\pi )\)
.
To our knowledge, the question of generic finiteness of Dirichlet or Neumann isospectral sets of
n
-gons—convex or otherwise—remains open. This situation contrasts with the results of Sect.
4
for the Steklov eigenvalue problem. However, spectral uniqueness for the Laplace spectrum is known within certain classes of polygons; e.g., triangles are mutually distinguishable by their Laplace spectrum [
4
,
12
], with either Dirichlet or Neumann boundary condition. Non-obtuse trapezoids are mutually distinguishable by their Dirichlet spectrum [
17
] and also by their Neumann spectrum [
16
]. The currently known Steklov spectral invariants are not sufficient to mutually distinguish all triangles, although we will see in an upcoming paper that Steklov isospectral sets of triangles are always finite and generic triangles are uniquely determined by their Steklov spectra. We will also address additional classes of convex
n
-gons.
Instead of finiteness of isospectral sets, one may ask about compactness of such sets. Osgood et al. [
30
] proved that Dirichlet isospectral families of smooth simply connected planar domains are compact in an appropriate topology. A similar result for the Steklov problem was proven by Jollivet and Sharafutdinov [
18
] for smooth simply connected (possibly multisheet) planar domains, building on related work in the Steklov setting by Edward [
6
].
On the other hand, many examples exist, beginning with [
10
], of non-congruent polygonal domains that are isospectral for the Laplacian with both Dirichlet and Neumann boundary conditions. The maximal possible size of mutually Laplace isospectral sets of non-congruent polygonal domains in the plane is unknown. The question of existence of Steklov isospectral plane domains remains open in both the convex and the non-convex case. However, the known examples of Laplace isospectral plane domains are also isospectral for both a mixed Steklov–Neumann problem and a mixed Steklov–Dirichlet problem [
11
].
Although the polygonal examples of Dirichlet and Neumann isospectral plane domains provide a negative answer to Mark Kac’s question about hearing the shape of a drum [
19
], the question remains open for domains with smooth boundary and for convex domains. Watanabe [
33
] used heat trace methods to show that there exist oval-shaped domains that are uniquely determined by their Dirichlet (or Neumann) spectra among all bounded planar domains. Around the same time, Zelditch used wave trace methods to prove that domains with an analytic bi-axisymmetric boundary are uniquely determined by their Laplace spectra within this class of domains [
35
]. More recently, Hezari and Zelditch proved that within the class of ellipses with small eccentricity, each element is uniquely determined by its Dirichlet or Neumann Laplace spectrum [
14
]. They also proved a similar result for generic real analytic centrally symmetric plane domains [
15
]. We refer interested readers to the surveys [
3
,
8
,
27
] for further reading on the Laplace and Steklov inverse spectral problems.
Data Availability
There is no data for this manuscript.
References
Arias-Marco, T., Dryden, E.B., Gordon, C.S., Hassannezhad, A., Ray, A., Stanhope, E.: Applications of possibly hidden symmetry to Steklov and mixed Steklov problems on surfaces. J. Math. Anal. Appl.
534
(2), Paper No. 128088, 34 (2024).
https://doi.org/10.1016/j.jmaa.2024.128088
Article
MathSciNet
MATH
Google Scholar
Birman, M.Š, Solomjak, M.Z.: The principal term of the spectral asymptotics for “non-smooth’’ elliptic problems. Funkcional. Anal. i Priložen.
4
(4), 1–13 (1970). (
(Russian). English translation in Functional Analysis Appl. 4 (1970), 265-275 (1971)
)
MathSciNet
MATH
Google Scholar
Colbois, B., Girouard, A., Gordon, C., Sher, D.: Some recent developments on the Steklov eigenvalue problem. Rev. Mat. Complut.
37
(1), 1–161 (2024).
https://doi.org/10.1007/s13163-023-00480-3
Article
MathSciNet
MATH
Google Scholar
Durso, C.: On the Inverse Spectral Problem for Polygonal Domains. Massachusetts Institute of Technology, Cambridge (1988)
MATH
Google Scholar
Edward, J.: An inverse spectral result for the Neumann operator on planar domains. J. Funct. Anal.
111
(2), 312–322 (1993).
https://doi.org/10.1006/jfan.1993.1015
Article
MathSciNet
MATH
Google Scholar
Edward, J.: Pre-compactness of isospectral sets for the Neumann operator on planar domains. Commun. Partial Differ. Equ.
18
(7–8), 1249–1270 (1993).
https://doi.org/10.1080/03605309308820973
Article
MathSciNet
MATH
Google Scholar
Girouard, A., Polterovich, I.: On the Hersch-Payne-Schiffer estimates for the eigenvalues of the Steklov problem. Funktsional. Anal. i Prilozhen.
44
(2), 33–47 (2010).
https://doi.org/10.1007/s10688-010-0014-1
((Russian, with Russian summary); English transl., Funct. Anal. Appl. 44 (2010), no. 2, 106-117)
Girouard, A., Polterovich, I.: Spectral geometry of the Steklov problem (survey article). J. Spectr. Theory
7
(2), 321–359 (2017).
https://doi.org/10.4171/JST/164
Article
MathSciNet
MATH
Google Scholar
Girouard, A., Lagacé, L., Polterovich, I.: The Steklov spectrum of cuboids. Mathematika
65
(2), 272–310 (2019).
https://doi.org/10.1112/s0025579318000414
Article
MathSciNet
MATH
Google Scholar
Gordon, C., Webb, D., Wolpert, S.: Isospectral plane domains and surfaces via Riemannian orbifolds. Invent. Math.
110
(1), 1–22 (1992).
https://doi.org/10.1007/BF01231320
Article
MathSciNet
MATH
Google Scholar
Gordon, C., Herbrich, P., Webb, D.: Steklov and Robin isospectral manifolds. J. Spectr. Theory
11
(1), 39–61 (2021).
https://doi.org/10.4171/jst/335
Article
MathSciNet
MATH
Google Scholar
Grieser, D., Maronna, S.: Hearing the shape of a triangle. Not. AMS
60
(11), 1440–1447 (2013)
MathSciNet
MATH
Google Scholar
Hersch, J., Payne, L.E., Schiffer, M.M.: Some inequalities for Stekloff eigenvalues. Arch. Ration. Mech. Anal.
57
, 99–114 (1975).
https://doi.org/10.1007/BF00248412
Article
MathSciNet
MATH
Google Scholar
Hezari, H., Zelditch, S.: One can hear the shape of ellipses of small eccentricity. Ann. Math. (2)
196
(3), 1083–1134 (2022).
https://doi.org/10.4007/annals.2022.196.3.4
Article
MathSciNet
MATH
Google Scholar
Hezari, H., Zelditch, S.: Centrally symmetric analytic plane domains are spectrally determined in this class. Trans. Am. Math. Soc.
376
(11), 7521–7553 (2023).
https://doi.org/10.1090/tran/8889
Article
MathSciNet
MATH
Google Scholar
Hezari, H., Lu, Z., Rowlett, J.: The Neumann isospectral problem for trapezoids. Ann. Henri Poincaré
18
(12), 3759–3792 (2017).
https://doi.org/10.1007/s00023-017-0617-7
Article
MathSciNet
MATH
Google Scholar
Hezari, H., Lu, Z., Rowlett, J.: The Dirichlet isospectral problem for trapezoids. J. Math. Phys.
62
(5), Paper No. 051511, 13 (2021).
https://doi.org/10.1063/5.0036384
Article
MathSciNet
MATH
Google Scholar
Jollivet, A., Sharafutdinov, V.: Steklov zeta-invariants and a compactness theorem for isospectral families of planar domains. J. Funct. Anal.
275
(7), 1712–1755 (2018).
https://doi.org/10.1016/j.jfa.2018.06.019
Article
MathSciNet
MATH
Google Scholar
Kac, M.: Can one hear the shape of a drum? Amer. Math. Mon.
73
(4), 1–23 (1966).
https://doi.org/10.2307/2313748
Article
MathSciNet
MATH
Google Scholar
Karpukhin, M., Lagacé, J.: Flexibility of Steklov eigenvalues via boundary homogenisation. Ann. Math. Qué.
48
(1), 175–186 (2024).
https://doi.org/10.1007/s40316-022-00207-8
. (
(English, with English and French summaries)
)
Article
MathSciNet
MATH
Google Scholar
Karpukhin, M., Lagacé, J., Polterovich, I.: Weyl’s law for the Steklov problem on surfaces with rough boundary. Arch. Ration. Mech. Anal.
247
(5), 77, 20 (2023).
https://doi.org/10.1007/s00205-023-01912-6
Article
MathSciNet
MATH
Google Scholar
Krymski, S., Levitin, M., Parnovski, L., Polterovich, I., Sher, D.A.: Inverse Steklov spectral problem for curvilinear polygons. Int. Math. Res. Not.
1
, 1–37 (2021).
https://doi.org/10.1093/imrn/rnaa200
Article
MathSciNet
MATH
Google Scholar
Kurasov, P., Suhr, R.: Asymptotically isospectral quantum graphs and generalised trigonometric polynomials. J. Math. Anal. Appl.
488
(1), 124049,15 (2020).
https://doi.org/10.1016/j.jmaa.2020.124049
Article
MathSciNet
MATH
Google Scholar
Kuznetsov, N., Kulczycki, T., Kwaśnicki, M., Nazarov, A., Poborchi, S., Polterovich, I., Siudeja, B.: The legacy of Vladimir Andreevich Steklov. Not. Am. Math. Soc.
61
(1), 9–22 (2014).
https://doi.org/10.1090/noti1073
Article
MathSciNet
MATH
Google Scholar
Levitin, M., Parnovski, L., Polterovich, I., Sher, D.A.: Sloshing, Steklov and corners: asymptotics of Steklov eigenvalues for curvilinear polygons. Proc. Lond. Math. Soc. (3)
125
(3), 359–487 (2022).
https://doi.org/10.1112/plms.12461
Article
MathSciNet
MATH
Google Scholar
Lu, Z., Rowlett, J.: One can hear the corners of a drum. Bull. Lond. Math. Soc.
48
(1), 85–93 (2016)
Article
MathSciNet
MATH
Google Scholar
Mårdby, G., Rowlett, J.: 112 years of listening to Riemannian manifolds.
https://arxiv.org/pdf/2406.18369
(2024)
Nursultanov, M., Rowlett, J., Sher, D.: How to hear the corners of a drum. In: 2017 MATRIX Annals, pp. 243–278 (2019)
Nursultanov, M., Rowlett, J., Sher, D.: The heat kernel on curvilinear polygonal domains in surfaces.
arXiv:1905.00259
(2019)
Osgood, B., Phillips, R., Sarnak, P.: Compact isospectral sets of surfaces. J. Funct. Anal.
80
(1), 212–234 (1988).
https://doi.org/10.1016/0022-1236(88)90071-7
Article
MathSciNet
MATH
Google Scholar
Rozenbljum, G.V.: Asymptotic behavior of the eigenvalues for some two-dimensional spectral problems, boundary value problems. Spectral theory (Russian). In: Problems of Mathematical Physics, vol. 7, pp. 188–203, 245, Leningrad University, Leningrad (1979)
(Russian)
Rozenblum, G.V.: Weyl asymptotics for Poincaré-Steklov eigenvalues in a domain with Lipschitz boundary. J. Spectr. Theory
13
(3), 755–803 (2023).
https://doi.org/10.4171/jst/477
Article
MathSciNet
MATH
Google Scholar
Watanabe, K.: Plane domains which are spectrally determined. II. J. Inequal. Appl.
7
(1), 25–47 (2002).
https://doi.org/10.1155/S1025583402000036
Article
MathSciNet
MATH
Google Scholar
Weinstock, R.: Inequalities for a classical eigenvalue problem. J. Ration. Mech. Anal.
3
, 745–753 (1954).
https://doi.org/10.1512/iumj.1954.3.53036
Article
MathSciNet
MATH
Google Scholar
Zelditch, S.: Spectral determination of analytic bi-axisymmetric plane domains. Geom. Funct. Anal.
10
(3), 628–677 (2000).
https://doi.org/10.1007/PL00001633
Article
MathSciNet
MATH
Google Scholar
Download references
Acknowledgements
This work was initiated at the BIRS-CMO workshop 22w5149. We sincerely thank the organizers as well as all sponsors of the workshop. We thank David Sher, Alexandre Girouard and Iosif Polterovich for inspiring and insightful discussions and correspondence, and Amir Vig for posing the question concerning rational angles discussed in Remark
2.15
. C. Villegas-Blas was partially supported by projects CONACYT Ciencia Básica CB-2016-283531-F-0363 and UNAM-PAPIIT-IN 116323. We are grateful to the referee for their attention to detail and suggestions that led to improvements in some of our results.
Funding
Open access funding provided by Chalmers University of Technology.
Author information
Authors and Affiliations
Department of Mathematics, Bucknell University, Lewisburg, PA, 17837, USA
Emily B. Dryden
Department of Mathematics, Dartmouth College, Hanover, NH, 03755, USA
Carolyn Gordon
Department of Mathematics, Universidad de Los Andes, 111711, Bogotá, Colombia
Javier Moreno
Mathematical Sciences, Chalmers University, 412 96, Gothenburg, Sweden
Julie Rowlett
Instituto de Matemáticas, Unidad Cuernavaca, Universidad Nacional Autónoma de México, 62210, Cuernavaca, Morelos, Mexico
Carlos Villegas-Blas
Authors
Emily B. Dryden
View author publications
Search author on:
PubMed
Google Scholar
Carolyn Gordon
View author publications
Search author on:
PubMed
Google Scholar
Javier Moreno
View author publications
Search author on:
PubMed
Google Scholar
Julie Rowlett
View author publications
Search author on:
PubMed
Google Scholar
Carlos Villegas-Blas
View author publications
Search author on:
PubMed
Google Scholar
Corresponding author
Correspondence to
Julie Rowlett
.
Additional information
Publisher's Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
Rights and permissions
Open Access
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit
http://creativecommons.org/licenses/by/4.0/
.
Reprints and permissions
About this article
Cite this article
Dryden, E.B., Gordon, C., Moreno, J.
et al.
The Steklov Spectrum of Convex Polygonal Domains I: Spectral Finiteness.
J Geom Anal
35
, 91 (2025). https://doi.org/10.1007/s12220-025-01922-8
Download citation
Received
:
09 August 2024
Accepted
:
24 January 2025
Published
:
06 February 2025
Version of record
:
06 February 2025
DOI
:
https://doi.org/10.1007/s12220-025-01922-8
Share this article
Anyone you share the following link with will be able to read this content:
Get shareable link
Sorry, a shareable link is not currently available for this article.
Copy shareable link to clipboard
Provided by the Springer Nature SharedIt content-sharing initiative
Keywords
Steklov
Eigenvalues
Dirichlet-to-Neumann map
Inverse spectral problem
Polygon
Curvilinear polygon
Mathematics Subject Classification
58C40
47A75
35R30
58J50
Profiles
Julie Rowlett
View author profile