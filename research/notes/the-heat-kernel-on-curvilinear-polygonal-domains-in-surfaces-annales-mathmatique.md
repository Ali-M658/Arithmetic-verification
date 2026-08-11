---
title: The heat kernel on curvilinear polygonal domains in surfaces | Annales mathématiques
  du Québec | Springer Nature Link
id: the-heat-kernel-on-curvilinear-polygonal-domains-in-surfaces-annales-mathmatique
tags:
- hyperbolic-pillow-heat-novelty-813161
- heat-trace-coefficients
- doi-record
- bibliography-correction
- cone-orbifold
created: '2026-08-09T08:48:20.244093Z'
updated: '2026-08-09T09:36:32.466278Z'
source: https://doi.org/10.1007/s40316-024-00237-4
source_domain: link.springer.com
fetched_at: '2026-08-09T08:48:20.238034Z'
fetch_provider: builtin
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'SpringerLink publisher record. FULL CITATION (BibTeX-usable, verbatim):
  Nursultanov, M., Rowlett, J. & Sher, D. ''The heat kernel on curvilinear polygonal
  domains in surfaces.'' Ann. Math. Quebec 49, 1-61 (2025). DOI: https://doi.org/10.1007/s40316-024-00237-4.
  Open access (CC-BY 4.0). Received: 02 March 2024; Accepted: 22 March 2024; Published
  (version of record): 27 December 2024; Issue date: April 2025. Journal name as printed:
  Annales mathematiques du Quebec, standard abbreviation ''Ann. Math. Quebec''. Confirms
  this is the correct published-version DOI matching the DOI already present in the
  arXiv:1905.00259 metadata (10.1007/s40316-024-00237-4).'
---

*Suggested by [[190500259-the-heat-kernel-on-curvilinear-polygonal-domains-in-surfaces]] — publisher confirmation of DOI and journal reference*

The heat kernel on curvilinear polygonal domains in surfaces | Annales mathématiques du Québec | Springer Nature Link
Skip to main content
The heat kernel on curvilinear polygonal domains in surfaces
Open access
Published:
27 December 2024
Volume 49
, pages 1–61 (
2025
)
Cite this article
You have full access to this
open access
article
Download PDF
Save article
View saved research
Annales mathématiques du Québec
Aims and scope
Submit manuscript
The heat kernel on curvilinear polygonal domains in surfaces
Download PDF
R\'esum\'e
We construct the heat kernel on curvilinear polygonal domains in arbitrary surfaces for Dirichlet, Neumann, and Robin boundary conditions as well as mixed problems, including those of Zaremba type. We compute the short time asymptotic expansion of the heat trace and apply this expansion to demonstrate a collection of results showing that corners are spectral invariants.
Résumé
Nous construisons le noyau de la chaleur pour des domaines polygonaux curvilignes dans des surfaces arbitraires avec des conditions aux bords de Dirichlet, Neumann et Robin ainsi que des conditions mixtes, y compris celles de type Zaremba. Nous calculons l’expansion asymptotique de la trace quand le temps approche zéro et nous utilisons cette expansion pour démontrer un ensemble de résultats montrant que les coins sont des invariants spectraux.
Similar content being viewed by others
Fast Polynomial Approximation to Heat Diffusion in Manifolds
Chapter
© 2019
Heat Kernel Estimates for Schrödinger Operators on Exterior Domains with Robin Boundary Conditions
Article
22 May 2017
How to Hear the Corners of a Drum
Chapter
© 2019
Explore related subjects
Discover the latest articles, books and news in related subjects, suggested using machine learning.
Abstract Harmonic Analysis
Global Analysis and Analysis on Manifolds
Hyperbolic Geometry
Partial Differential Equations
Diffusion  Processes and Stochastic Analysis on  Manifolds
Partial Differential Equations on Manifolds
Spectral Theory of Pseudodifferential Operators on Manifolds
1
Introduction
If two compact Riemannian manifolds (
M
,
g
) and
\((M', g')\)
are isospectral, meaning they have the same Laplace spectrum, then they need not be isometric. However, isospectrality does imply that
M
and
\(M'\)
both have the same dimension,
n
. Moreover, they also have the same
n
-dimensional volume. Thus, both dimension and volume are spectral invariants, in the sense that they are determined by the spectrum. This fact follows from Weyl’s law [
52
], proven over one hundred years ago. It is natural to ask: what other geometric features are spectral invariants?
The next geometric spectral invariant was discovered by Pleijel [
44
] some forty years after Weyl’s law. For an
n
-dimensional Riemannian manifold with smooth boundary, the
\(n-1\)
dimensional volume of the boundary is a spectral invariant. About ten years later, McKean and Singer [
37
] proved that certain curvature integrals are also spectral invariants. For smooth surfaces and smoothly bounded planar domains, McKean and Singer [
37
] and independently M. Kac [
22
] proved that the Euler characteristic is a spectral invariant. By the Gauss–Bonnet theorem, this shows that the number of holes in a planar domain is a geometric spectral invariant for a planar domain.
The tactic of both McKean and Singer and Kac was to use the existence of a short time asymptotic expansion for the heat trace, together with the calculation of the coefficients in this expansion. Recall that the
heat kernel
\(H^M (t,z,z')\)
on a Riemannian manifold (
M
,
g
) is the fundamental solution of the heat equation on
M
:
$$\begin{aligned} {\left\{ \begin{array}{ll} (\partial _t+\Delta _z)H^M(t,z,z')=0;\\ \lim _{t\rightarrow 0}H^M(t,z,z')=\delta _z(z').\end{array}\right. } \end{aligned}$$
(1.1)
As long as the eigenvalues are discrete and approach
\(\infty \)
sufficiently quickly, which is the case in all geometric settings considered here, the
heat trace
is the trace of this kernel, and satisfies
$$\begin{aligned} \operatorname {Tr}H^M(t)=\int _{M}H^M(t,z,z)\, dz=\sum _{j=1}^{\infty }e^{-\lambda _j t}. \end{aligned}$$
(1.2)
Above,
\(\lambda _j\)
are the eigenvalues of the Laplacian
\(\Delta \)
on
M
, arranged in increasing order. As a consequence, the heat trace is a spectral invariant. Therefore the coefficients in its asymptotic expansion as
\(t\rightarrow 0\)
are also spectral invariants. The existence and calculation of an asymptotic expansion for the heat trace is a powerful method for producing spectral invariants. This program has been carried out extensively both for smooth manifolds and for manifolds with boundary [
37
].
Here, we are interested in the heat kernel on curvilinear polygonal domains which are subsets of smooth surfaces. This includes curvilinear polygonal domains in the plane, as well as more exotic non-planar examples. We are interested in the heat kernel for such domains in part because it may allow us to determine new geometric spectral invariants. Indeed, we show in Sect.
6
that in general, the presence or lack of vertices is a spectral invariant for Dirichlet, Neumann, Robin, and mixed boundary conditions. Moreover, we shall see there that a jump in boundary condition is also a spectral invariant.
Let us now introduce our geometric setting.
Definition 1.1
We say that
\(\Omega \)
is a
curvilinear polygonal domain
if it is a compact subset of a smooth Riemannian surface (
M
,
g
) with piecewise smooth boundary and a vertex at each non-smooth point of
\(\partial \Omega \)
. A
vertex
is a point
p
on the boundary of
\(\Omega \)
at which the following are satisfied.
1.
The boundary in a neighborhood of
p
is defined by a continuous curve
\(\gamma (t): (-a, a) \rightarrow M\)
for
\(a > 0\)
with
\(\gamma (0) = p\)
. We require that
\(\gamma \)
is smooth on
\((-a,0]\)
and [0,
a
), with
\(||{\dot{\gamma }}(t)|| =1\)
for all
\(t \in (-a, a)\)
, and such that
$$\begin{aligned} \lim _{t \uparrow 0} {\dot{\gamma }} (t) = v_1, \quad \lim _{t \downarrow 0} {\dot{\gamma }} (t) = v_2, \end{aligned}$$
for some vectors
\(v_1,v_2\in T_{p}M\)
, with
\(- v_1 \ne v_2\)
.
2.
The
interior angle
at the point
p
is the
interior angle
at that corner, which is the angle between the vectors
\(-v_1\)
and
\(v_2\)
.
Note that requiring
\(-v_1\)
and
\(v_2\)
to be distinct means that the interior angle will be an element of
\((0,2\pi )\)
, which rules out inward and outward pointing cusps. An angle of
\(\pi \)
is allowed.
A vertex in a curvilinear polygonal domain is an example of a conical singularity where the link is a one-dimensional manifold with boundary. Moreover, it is a “non-exact” conical singularity in the sense that the curve
\(\gamma \)
defining the boundary near a vertex may have non-zero geodesic curvature on the entire interval
\((-a, a)\)
. For curvilinear domains in the plane, this means that there need not be a neighborhood of the vertex in which the edges are straight. This geometric setting is therefore not contained within the literature for either (1) conical singularities whose link is a compact manifold without boundary nor for (2) planar polygons for which the edges are straight near the vertices.
There is substantial work in the literature on heat trace expansions in the settings (1) and (2). For conical singularities with no boundary on the link, a non-exhaustive list of works concerning the heat kernel and its trace is: [
12
,
13
,
24
,
26
,
29
,
30
,
41
,
46
]. In the case (2) of vertices which locally have straight edges, a non-exhaustive list includes [
23
,
27
,
42
,
48
].
For polygonal domains in the plane with the Dirichlet boundary condition, Fedosov showed in the 1960s that the vertices produce an extra term in the short time asymptotic expansion of the heat trace [
9
,
10
]. This term appears in the coefficient of
\(t^0\)
. Its most simplified form and calculation can be found in a paper of van den Berg and Srisatkunarajah [
51
], although the expression there is originally due to unpublished work of Ray, and is mentioned in both [
22
] and [
37
].
Although it has been widely assumed that analogous results for the heat trace expansion hold for curvilinear polygons, a rigorous proof even in the planar Dirichlet case was not given until [
31
]. Similar results hold for Neumann boundary conditions, see [
34
]. Although Robin conditions have been studied on manifolds with boundary [
14
,
54
], to our knowledge there is no work in the literature about heat trace expansions with Robin conditions in the presence of corners of arbitrary angles, even in the plane. For certain corner angles, however, we refer to the physical approach of [
3
]. Outside the planar case, or even in the planar case with mixed boundary conditions, less is known. For the mixed boundary condition, also known as Zaremba boundary condition, references include [
4
,
21
,
28
,
47
].
Our geometric microlocal methods allow us to handle the general case of compact curvilinear polygonal domains in surfaces, with any combination of Dirichlet, Neumann, and/or Robin boundary conditions on the various smooth boundary components. The sign convention for our Laplacian, in local coordinates, with respect to the Riemannian metric,
g
, on a surface is
$$\begin{aligned} \Delta = - \frac{1}{\sqrt{\det (g)}} \sum _{i,j=1} ^2 \partial _i \sqrt{\det (g)} g^{ij} \partial _j. \end{aligned}$$
Our convention for the Robin boundary condition on any portion of the boundary is:
$$\begin{aligned} \left. \frac{\partial u}{\partial \nu } \right| _{\partial \Omega } = \left. \kappa u \right| _{\partial \Omega }. \end{aligned}$$
Here, the derivative on the left is the
inward
pointing normal derivative, and therefore, on the right,
\(\kappa \)
is a
non-negative
function. Under this condition the spectrum is non-negative. We assume throughout, for simplicity, that
\(\kappa \)
is smooth.
Our main result is:
Theorem 1.2
Let
\(\Omega \)
be a curvilinear polygonal domain in a smooth surface with finitely many vertices
\(V_1,\ldots , V_n\)
of angles
\(\alpha _1,\ldots ,\alpha _n\)
. Define its edges
\(E_1,\ldots ,E_n\)
by letting
\(E_j\)
be the segment of the boundary between
\(V_{j-1}\)
and
\(V_j\)
, with subscripts taken mod
n
. Let
\({\mathcal {E}}_D\)
,
\({\mathcal {E}}_N\)
, and
\({\mathcal {E}}_R\)
be three disjoint sets whose union is
\(\{1,\dots ,n\}\)
. For each
\(j\in {\mathcal {E}}_D\)
,
\({\mathcal {E}}_N\)
, and
\({\mathcal {E}}_R\)
, we impose Dirichlet, Neumann, and Robin conditions with parameter
\(\kappa _j(x)\)
, respectively, along
\(E_j\)
. Assume that all functions
\(\kappa _j(x)\)
are non-negative and smooth.
Let
\({\mathcal {V}}_{=}\)
be the set of
j
for which vertex
\(V_j\)
has either zero or two Dirichlet edges adjacent to it, i.e. either both
j
and
\(j+1\in {\mathcal {E}}_D\)
or neither are. Conversely, let
\({\mathcal {V}}_{\ne }\)
be the set of
j
for which
\(V_j\)
has exactly one adjacent Dirichlet edge. Also let
K
(
z
) and
\(k_g(x)\)
be the Gauss curvature and geodesic/mean curvature of
\(\Omega \)
and
\(\partial \Omega \)
respectively.
Then the heat trace
\(\operatorname {Tr}H^{\Omega }(t)\)
for the Laplacian with those boundary conditions, and with the Friedrichs extension at each vertex, has a complete polyhomogeneous conormal expansion in
t
as
\(t\rightarrow 0\)
. Moreover, the first few terms of this expansion have the form
$$\begin{aligned} \operatorname {Tr}H^{\Omega }(t)=a_{-1}t^{-1}+a_{-1/2}t^{-1/2}+a_0+O(t^{1/2}\log t), \end{aligned}$$
where:
$$\begin{aligned} a_{-1}= &   \frac{A(\Omega )}{4\pi };\end{aligned}$$
(1.3)
$$\begin{aligned} a_{-1/2}= &   \frac{1}{8\sqrt{\pi }}\left( \sum _{j\notin {\mathcal {E}}_D}\ell (E_j)-\sum _{j\in {\mathcal {E}}_D}\ell (E_j)\right) ; \end{aligned}$$
(1.4)
$$\begin{aligned} a_0= &   \frac{1}{12\pi }\int _{\Omega }K(z)\, dz+\frac{1}{12\pi }\int _{\partial \Omega }k_g(x)\, dx-\frac{1}{2\pi }\sum _{j\in {\mathcal {E}}_R}\int _{E_j}\kappa _j(x)\, dx \end{aligned}$$
(1.5)
$$\begin{aligned}  &   +\sum _{j\in V_{=}}\frac{\pi ^2-\alpha _j^2}{24\pi \alpha _j}+\sum _{j\in V_{\ne }}\frac{-\pi ^2-2\alpha _j^2}{48\pi \alpha _j}. \end{aligned}$$
(1.6)
Remark 1.3
It is well-known that if the boundary of
\(\Omega \)
is smooth then there are no logarithmic terms in the heat expansion. We do not characterize the nature of logarithmic terms in the expansion in our more general setting.
The proof of this result contains several ingredients which may be of independent interest. The main strategy is to use geometric microlocal analysis to construct the heat kernel on a heat space, denoted by
\(\Omega _h ^2\)
, which is created by blowing up
\(\Omega \times \Omega \times [0, 1)\)
along various p-submanifolds. On this heat space we show, in Theorem
5.8
, that the heat kernel has a polyhomogeneous conormal expansion at every boundary hypersurface. Indeed we construct the heat kernel by solving suitable model problems at the various boundary hypersurfaces. This gives a full description of the heat kernel on a curvilinear polygonal domain in a surface, in all asymptotic regimes. As such this construction is useful for any application in which fine structure information about the heat kernel near
\(t=0\)
is needed.
A major advantage of this method is that a complete asymptotic description of the heat
kernel
, rather than just its trace, is obtained. This allows precise asymptotic analysis for expressions such as the gradient of the heat kernel and is likely of interest for future work.
The paper is organized as follows. In Sect.
2
, we develop an integral representation of the heat kernel for infinite circular sectors with Dirichlet, Neumann, and mixed boundary conditions. We do this by first obtaining an integral representation of the Green’s function for the corresponding boundary condition. Using functional calculus, we prove that the heat kernel is obtained by taking the inverse Laplace transform of the Green’s function. By the uniqueness of the heat kernel, we thereby obtain the equivalence of this integral representation of the heat kernel and the more common series representation of the heat kernel [
6
]. In Sect.
3
, we construct the heat spaces and demonstrate the composition rule for operators with polyhomogeneous conormal Schwartz kernels. To construct the heat kernel, we proceed in Sect.
4
to solve the model problem for the smooth parts of the boundary for the Dirichlet, Neumann, and Robin boundary conditions. In Sect.
5
we solve the model problem for the vertices with the various boundary conditions and combinations thereof. In this way, we construct the heat kernel on a curvilinear polygonal domain in a surface. In Sect.
6
, we use this construction together with our integral representation of the heat kernels obtained in Sect.
2
to compute the heat trace and prove Theorem
1.2
. We conclude in Sect.
6
with applications of Theorem
1.2
showing contexts in which corners (vertices) are spectral invariants.
1.1
Notation
For the benefit of readers, we collect here all notations occurring in at least two non-consecutive pages.
Notation
Meaning
Sections
\(\mathbb {R}\)
,
\(\mathbb {C}\)
,
\(\mathbb {N}\)
Real, complex, and natural numbers
\(\Re \)
,
\(\Im \)
Real and imaginary parts
\(\mathbb {Z}\)
,
\(\mathbb {N}_0\)
Integers and non-negative integers
\(H^\Omega \)
,
\(\operatorname {Tr}H^{\Omega }\)
The Heat kernel and Heat trace on a curvilinear polygon
\(\Omega \)
1
\(E_j\)
,
\(V_j\)
Edges and vertices
1
K
,
\(k_g\)
The Gauss and geodesic curvature
1
G
,
\(G_D\)
,
\(G_N\)
,
\(G_{DN}\)
Green functions
2.1
\(K_\nu \)
,
\(I_\nu \)
The modified Bessel functions
2.1
\( \mathfrak {L}\)
,
\( \mathfrak {L}^{-1}\)
The Laplace transform and its inverse
2.2
F
,
\(\mathcal {F}\)
The index set and index family
3.1
pc
Polyhomogeneous conormal distributions
3.1
\(\beta \)
Blow-down map
3.1
E
,
V
The set of edges and vertices
3.2
tf
,
\(e_j\)
,
\(sv_j\)
,
\(pv_j\)
,
\(pe_j\)
Boundary hypersurfaces of single heat space
3.2
\(M_h^2\)
,
\(M_{rh}^2\)
,
\(M_{rh}^3\)
,
\(M_{rh,c}^3\)
Heat spaces
3.3
,
3.5
\(E_{j0}\)
,
\(E_{0j}\)
,
\(hvff_{jk}\)
,
\(hvrf_j\)
,
\(hvlf_j\)
Boundary hypersurfaces of double heat space and their components
3.3
ff
,
sf
,
\(ff_j\)
,
\(sf_j\)
\(\pi _C\)
,
\(\pi _L\)
,
\(\pi _R\)
Lifted projections from triple heat space to double heat space
3.4
\(\rho \)
,
\(\rho _X\)
Boundary defining functions
3.4
Notation
Meaning
Sections
\(e_f(\cdot , \cdot )\)
Boundary exponents
3.4
\(\Pi _C\)
,
\(\Pi _L\)
,
\(\Pi _R\)
b
-maps
3.5
\(F_A\)
,
\(F_{AB}\)
,
\(F_{ABC}\)
,
\(F_{ABCD}\)
Boundary hypersurfaces of triple heat space
3.5
\(\mathcal {A}_h^{\mathcal {F}}\)
Spaces of pc functions
3.8
,
4.2
\(\Psi _h^{\mathcal {F}}\)
,
\(\Psi ^{a,b,c,d}\)
Set of pseudodifferential operators
3.8
,
4.2
\(\mathcal {L}\)
Lifted heat operator
4.1.1
\(\chi \)
Euler characteristic
6.1.2
2
Analytic preliminaries
The Laplace operator on a curvilinear polygonal domain, even with specified boundary conditions on each side, is emphatically
not
guaranteed to be self-adjoint. The angles at the vertices as well as the possibility of different boundary conditions on either side of a vertex can give rise to interesting phenomena [
7
,
8
,
17
]. We shall consider a Friedrichs type extension of the Laplace operator here. The Laplacian is a priori a symmetric operator on smooth, compactly supported functions on our domain,
\(\Omega \)
.
Our sign convention for the Robin boundary condition is
$$\begin{aligned} \frac{\partial v}{\partial n} = \kappa v, \quad {\text { for the inward pointing normal derivative.}} \end{aligned}$$
The Robin parameter is smooth on each boundary component and is non-negative. We define the Laplace operator corresponding to the mixed boundary conditions in the following way, as in [
11
,
45
]. Consider the form
$$\begin{aligned} a(u,v)=\int _\Omega \nabla u(z) \overline{\nabla v(z)}dz+\int _{\partial \Omega _R} \kappa (z) u(z)\overline{v(z)}d\sigma (z) \end{aligned}$$
with domain
$$\begin{aligned} \textrm{D}(a)= \left\{ u \in H^1 (\Omega ): u|_{\partial \Omega _D} = 0\right\} . \end{aligned}$$
Above,
\(\partial \Omega _D\)
and
\(\partial \Omega _R\)
are the unions of the boundary components on which we impose the Dirichlet and Robin boundary conditions, respectively, and
\(\kappa (z)\)
is the Robin parameter. Then
a
is a closed, densely defined, symmetric form. Therefore, by [
25
, Theorem 2.23 Chap. 6], it generates a self-adjoint operator, which we call the Laplace operator corresponding to the boundary conditions we mentioned above.
2.1
Green’s functions
The general approach to study the heat kernel via the associated Green’s function and Kantorovich–Lebedev transform is well documented in the literature, dating at least back to Fedosov in the 1960s [
10
]. This approach has continued to produce interesting results in modern work as well; see for example the doctoral thesis of Uçar [
49
] who considers polygonal domains in hyperbolic surfaces. Although the general technique is well known, the details of the calculations are often omitted. To maintain the flow and focus of this work, we present here the results of our calculations, and for the sake of completeness include the details in Appendix
A
.
We obtain integral expressions for Green’s functions for the Laplacian on an infinite circular sector with Dirichlet, Neumann, and mixed boundary conditions. Let
\(\gamma \)
be the interior angle of the sector; we need only assume
\(\gamma \in (0, 2\pi )\)
. The Green’s function solves the following equation:
$$\begin{aligned} {\left\{ \begin{array}{ll} sG-\frac{\partial ^2 G}{\partial r^2}-\frac{1}{r}\frac{\partial G}{\partial r}-\frac{1}{r^2}\frac{\partial ^2 G}{\partial \phi ^2}=\frac{1}{r}\delta (r-r_0)\delta (\phi -\phi _0),\\ \left. \left( \alpha G+\beta \frac{\partial G}{\partial \phi }\right) \right| _{\phi =0,\gamma }=0, \end{array}\right. } \end{aligned}$$
(2.1)
with
\(\alpha = 1\)
and
\(\beta = 0\)
for the Dirichlet boundary condition or
\(\alpha = 0\)
and
\(\beta = 1\)
for the Neumann boundary condition, and in all cases with spectral parameter
\(s>0\)
.
For the Dirichlet boundary condition we compute in Appendix
A
that the Green’s function is
$$\begin{aligned} G_D(s,r,\phi ,r_0,\phi _0)= &   \frac{1}{\pi ^2}\int _{0}^{\infty }K_{i\mu }(r \sqrt{s})K_{i\mu }(r_0 \sqrt{s})\nonumber \\  &   \times \biggl \{ \cosh (\pi -|\phi _0-\phi |)\mu -\frac{\sinh \pi \mu }{\sinh \gamma \mu }\cosh (\phi +\phi _0-\gamma )\mu \nonumber \\  &   +\frac{\sinh (\pi -\gamma )\mu }{\sinh \gamma \mu }\cosh (\phi -\phi _0) \mu \biggl \}d\mu , \end{aligned}$$
(2.2)
where
\(K_\nu \)
is the modified Bessel function of second kind. For the Neumann boundary condition, we obtain
$$\begin{aligned} G_N(s,r,\phi ,r_0,\phi _0)= &   \frac{1}{\pi ^2}\int _{0}^{\infty }K_{i\mu }(r \sqrt{s})K_{i\mu }(r_0 \sqrt{s})\nonumber \\  &   \times \biggl \{ \cosh (\pi -|\phi _0-\phi |)\mu +\frac{\sinh \pi \mu }{\sinh \gamma \mu }\cosh (\phi +\phi _0-\gamma )\mu \nonumber \\  &   +\frac{\sinh (\pi -\gamma )\mu }{\sinh \gamma \mu }\cosh (\phi -\phi _0) \mu \biggl \}d\mu . \end{aligned}$$
(2.3)
For the mixed Dirichlet–Neumann boundary condition, taking the Dirichlet condition at
\(\phi =0\)
and the Neumann condition at
\(\phi =\gamma \)
we obtain the Green’s function
$$\begin{aligned} G_{DN} (s,r,\phi ,r_0,\phi _0)= &   \frac{1}{\pi ^2}\int _{0}^{\infty }K_{i\mu }(r\sqrt{s})K_{i\mu }(r_0\sqrt{s})\nonumber \\  &   \times \biggl \{ \cosh (\pi -|\phi _0-\phi |)\mu +\frac{\sinh (\pi \mu )}{\cosh \gamma \mu }\sinh ((\phi +\phi _0-\gamma )\mu )\nonumber \\  &   -\frac{\cosh (\pi -\gamma )\mu }{\cosh \gamma \mu }\cosh ((\phi -\phi _0)\mu \biggl \}d\mu . \end{aligned}$$
(2.4)
2.2
The Heat kernel and the Green’s function
Let
\(\Delta \)
be a self-adjoint, non-negative Laplace operator whose domain is contained in
\(\mathcal {L}^2(\Omega )\)
associated with certain boundary conditions
$$\begin{aligned} B(u)=0 \quad \text {on} \quad \partial \Omega , \end{aligned}$$
where
\(\Omega \)
is a domain with a piecewise smooth boundary
\(\partial \Omega \)
which is contained in a larger smooth ambient manifold. Assume that
G
(
x
,
y
,
s
) is the Green’s function of the operator
\(s+\Delta \)
, that is the solution of the system
$$\begin{aligned} {\left\{ \begin{array}{ll} (s+\Delta )G(x,y,s)=\delta (x-y),\\ B(G)=0. \end{array}\right. } \end{aligned}$$
(2.5)
Before stating the next result, we recall the definition of the Laplace transform and its inverse.
Definition 2.1
Let
f
be a continuous function such that there exists a constant
\(c>0\)
with
$$\begin{aligned} \int _0 ^\infty |f(t)| e^{-c |t|} dt < \infty . \end{aligned}$$
The Laplace transform of
f
is defined to be
$$\begin{aligned} g(s):=\mathfrak {L}(f(t))(s):=\int _0^\infty f(t)e^{-st} dt, \quad \Re (s) \ge c. \end{aligned}$$
The inverse Laplace transform is then
$$\begin{aligned} f(x):=\mathfrak {L}^{-1}(g(s))(t):=\frac{1}{2\pi i} \lim _{k\rightarrow \infty }\int _{a -ik}^{a +ik} g(s) e^{st} ds, \end{aligned}$$
for
\(t>0\)
and
\(a>c\)
.
Proposition 2.2
With the notations above, let
H
(
x
,
y
,
t
) be the heat kernel corresponding to
\(\Delta \)
. Then
$$\begin{aligned} \mathfrak {L}[H](x,y,s)=G(x,y,s), \end{aligned}$$
where
\(\mathfrak {L}\)
is the Laplace transform.
Proof
Let
\(\{e^{-t\Delta }\}_{t\ge 0}\)
be the semigroup generated by
\(-\Delta \)
. We note that
\(-\Delta \)
is a non-positive, self-adjoint operator, so that this semigroup is well defined on
\(\mathcal {L}^{2}(\Omega )\)
. Moreover, the self-adjointness gives
$$\begin{aligned} \left\| (\lambda + \Delta )^{-1}\right\| \le \frac{1}{\textrm{dist}(\lambda , \sigma (-\Delta ))} \qquad \lambda \in \rho (-\Delta ), \end{aligned}$$
(2.6)
where
\(\sigma (-\Delta )\)
and
\(\rho (-\Delta )\)
are, respectively, the spectrum and resolvent set of
\(-\Delta \)
. Therefore, by the Hille–Yosida theorem [
53
],
\(\{e^{-t\Delta }\}_{t\ge 0}\)
is a contracting semigroup. Hence, by Theorem 8.2.2 in [
53
], it follows
$$\begin{aligned} \mathfrak {L}\circ e^{-t\Delta }(s)=(s+\Delta )^{-1}, \qquad s>0, \end{aligned}$$
(2.7)
where
\(\mathfrak {L}\)
is the Laplace transform acting in
t
variable.
On the one hand, since the heat kernel
H
(
x
,
y
,
t
) is
\(\mathfrak {L}\)
transformable, we may express
$$\begin{aligned} \mathfrak {L}[e^{-t\Delta }\phi ]=\mathfrak {L}\int _{\Omega }H(t,x,y)\phi (y)dy=\int _{\Omega }\mathfrak {L}[H]\phi (y)dy \end{aligned}$$
for
t
,
\(s>0\)
and
$$\begin{aligned} (s+\Delta )^{-1}\phi =\int _{\Omega }G(x,y,s)\phi (s)dy. \end{aligned}$$
for
\(s>0\)
. Therefore, the uniqueness of Schwartz kernels and (
2.7
) imply the statement.
\(\square \)
Remark 2.3
Due to Proposition
2.2
, by applying the inverse Laplace transform to (
2.2
), (
2.3
), and (
2.4
), we obtain expressions for the heat kernels for the Laplacian on an infinite circular sector with Dirichlet, Neumann, and mixed boundary conditions, respectively. The heat kernels for an infinite circular sector were computed by Cheeger using separation of variables in polar coordinates [
6
, p. 592 (3.42)]. Cheeger’s formula simplifies in our setting to:
$$\begin{aligned} H(t,r,\theta ,r',\theta ')=\frac{1}{2t}\exp \left[ -\frac{r^2+(r')^2}{4t}\right] \sum _{j=1}^{\infty }I_{\mu _j}\left( \frac{rr'}{2t}\right) \phi _j(\theta )\phi _j(\theta '). \end{aligned}$$
(2.8)
Here
\(I_{\mu _j}\)
are the modified Bessel functions, and
\((\phi _j,\mu _j)\)
are the eigenfunctions, and corresponding eigenvalues, of the appropriate eigenvalue problem (D–D, N–N, or D–N) on the interval
\([0,\gamma ]\)
. By the uniqueness of the heat kernel we therefore obtain the equality of these expressions with the inverse Laplace transform of the expression for the Greens functions.
3
Heat spaces
We consider curvilinear polygonal domains as in Definition
1.1
; see examples illustrated in Fig.
1
.
Fig. 1
Full size image
Two examples of curvilinear polygonal domains, with edges and vertices
3.1
Manifolds with corners and polyhomogeneity
Near a vertex,
\(\Omega \)
has the differentiable structure of a manifold with corners after blowing up the vertex. Specifically, an open neighborhood of a vertex is diffeomorphic to a sector,
\((0, \varepsilon ] \times C\)
, where
C
is a circular arc. If we include the point
\(\{0\} \times C\)
, then we obtain a smooth manifold with corners. This is what is meant by “blowing up the vertex,” in the sense that we replace the vertex with a copy of the link of the sector, namely
C
. This process may be thought of as pretending that polar coordinates are actually valid down to the origin. Doing this construction at each vertex yields a smooth surface with corners which we call
\(\Omega _0\)
. In this way, we may identify the differentiable structure of all the surfaces we consider here as the differentiable structure of
manifolds with corners,
defined below. The definition is first due to Melrose [
39
], here we use the version which is introduced in [
38
].
In order to define a manifold with corners, we must first define t-manifolds.
Definition 3.1
[
38
, Definition 1.6.1] An
n
-dimensional t-manifold
X
is a paracompact Hausdorff space such that at each point
\(x \in X\)
there is a non-negative integer
k
such that a neighborhood of
x
is homeomorphic to a neighborhood of the origin in the product
\([0,\infty )^k \times \mathbb {R}^{n-k}\)
, with all transition maps being smooth with respect to the subspace topology on
\([0,\infty )^k\times \mathbb {R}^{n-k}\subseteq \mathbb {R}^n\)
.
Now we define a manifold with corners.
Definition 3.2
[
38
, Definition 1.8.5] A manifold with corners is a t-manifold such that each boundary hypersurface is embedded.
Since with this definition we may have
\(k=0\)
, we see that smooth manifolds without boundary also fit into the general class of “manifolds with corners.”
The purpose of the heat space construction is to create spaces on which the heat kernel and its trace are polyhomogeneous conormal distributions, abbreviated pc. This is a natural class of functions within which to study partial differential equations on manifolds with corners; see [
33
] and references therein. We briefly recap the definition here. To begin, we say that a subset
\(F\subseteq {\mathbb {C}}\times {\mathbb {N}}_0\)
is an
index set
if
F
is a discrete set satisfying the following properties:
For all
N
,
\(F\cap \{\Re (z)<N\}\)
is finite;
If
\((s,p)\in F\)
, then
\((s+1,p)\in F\)
;
If
\((s,p)\in F\)
and
\(p>0\)
, then
\((s,p-1)\in F\)
.
The latter two conditions are sometimes omitted from this definition, but they give pc functions nice invariance properties; see [
16
].
Let
X
be an
n
-dimensional manifold with corners, and let
\(\{M_i\}_{i=1}^J\)
be the set of its boundary hypersurfaces, that is, the set of all boundary faces of codimension one. We say that
\({\mathcal {F}}=(F_1,\ldots ,F_J)\)
is an
index family
for
X
if each
\(F_i=\{(s_{ij},p_{ij})_{j=1}^{\infty }\}\)
is an index set, ordered so that
\(s_{ij}\in {\mathbb {R}}\)
are non-decreasing and
\(p_{ij}\)
are non-increasing whenever
\(s_{ij}\)
is unchanged. For each
i
, let
\(x^i\)
be a
boundary defining function
for
\(M_i\)
; that is, a smooth, non-negative function
\(x^i: X \rightarrow \mathbb {R}\)
such that
\(x^i\)
vanishes precisely at
\(M_i\)
but the differential
\(dx^i\)
is non-zero on
\(M_i\)
. We may use boundary defining functions as coordinates on
X
. Finally, let
\(\mathcal {V}_b\)
denote the space of smooth vector fields on
X
which are tangent to all boundaries. With this terminology, we define
\({\mathcal {A}}^{{\mathcal {F}}}(X)\)
, the space of polyhomogeneous conormal, or pc functions, to be the space of functions
f
smooth on the interior of
X
which have:
generalized Taylor-like expansions at each boundary hypersurface
\(M_i\)
of the form
$$\begin{aligned} f\sim \sum _{j=1}^{\infty }(x^i)^{s_{ij}}(\log (x^i))^{p_{ij}}a_{ij}(x^1,\ldots ,x^{i-1},x^{i+1},\ldots ,x^n), \end{aligned}$$
where for each
i
, the set
\(\{(s_{ij},p_{ij})\}\)
is the index set
\(F_i\)
, enumerated so that
\(s_{ij}\)
is non-decreasing;
product type expansions of the same form at each corner (polyhomogeneous),
and for which
Vf
has expansions of the same type whenever
V
is a product of elements of
\(\mathcal {V}_b\)
(conormal).
The union of these spaces over all possible index sets is denoted
\({\mathcal {A}}^*(X)\)
. Note that by definition these spaces are invariant under
\(\mathcal {V}_b\)
, in the sense that for any
\(V\in \mathcal {V}_b\)
and any
\(u\in {\mathcal {A}}^{{\mathcal {F}}}(X)\)
,
\(Vu\in {\mathcal {A}}^{{\mathcal {F}}}(X)\)
as well. Observe also that smooth functions on
X
are pc with each index set consisting of
\({\mathbb {N}}_0\times \{0\}\)
.
3.1.1
Blowups
Consider the finite cone,
\((0,1]_r \times {\textbf{S}}^1_\theta \)
with the Riemannian metric,
\(dr^2 + r^2 d\theta ^2\)
, where
\(d\theta ^2\)
is the standard metric on
\({\textbf{S}}^1\)
, and the conical point is at
\(r=0\)
. The simplest example of blowing up is replacing the conical point at
\(r=0\)
with a copy of
\({\textbf{S}}^1\)
, so that the finite cone is now topologically identified with the cylinder
\([0,1] \times {\textbf{S}}^1\)
. In this example, the point at
\(r=0\)
is replaced with the set of all directions, that is all values of
\(\theta \)
, with which one can approach the point,
\(r=0\)
. This type of blowup is known as a
radial blowup
, or a
normal
blowup.
More generally, we shall consider blowups along
p
-
submanifolds.
An embedded submanifold
Y
contained in a manifold with corners,
X
, is a
p
-
submanifold
if near each point
\(q \in Y\)
, there exist local coordinates so that
Y
is defined by the vanishing of a subset of these local coordinates. For example, the boundary faces of
X
are
p
-submanifolds. The intersection of two or more boundary faces of
X
is also a
p
-submanifold. The normal blowup of
X
around
Y
is denoted by
$$\begin{aligned} {[}X; Y] = \text {ff}\sqcup (X {\setminus } Y). \end{aligned}$$
Above, ff is the inward pointing spherical normal bundle of
Y
which has replaced
Y
in [
X
;
Y
]. There is a unique minimal differentiable structure with respect to which [
X
;
Y
] is a manifold with corners such that the following two conditions hold.
1.
There is a smooth “blow-down” map
$$\begin{aligned} \beta : [X;Y] \rightarrow X \end{aligned}$$
which is the identity on
\((X{\setminus } Y)\)
.
2.
Cylindrical coordinates around
Y
are smooth coordinates on [
X
;
Y
].
In case we wish to blow up two or more
p
-submanifolds, we write
$$\begin{aligned} {[}X; Y_1; Y_2] \end{aligned}$$
to indicate that we first blow up
\(Y_1\)
and next blow up the lift of
\(Y_2\)
to
\([X;Y_1]\)
. This lift is the usual lift if
\(Y_2\subseteq Y_1\)
, and otherwise is the closure of
\(Y_2{\setminus } Y_1\)
in
\([X;Y_1]\)
.
3.2
The single heat space
The first of the heat spaces we construct is the single heat space. Let
\(\Omega \)
be a curvilinear polygonal domain. Let
E
be the set of edges of
\(\Omega \)
(maximal smooth boundary components) and
V
the set of vertices. Throughout, we let
\(\Omega _0\)
be
\(\Omega \)
with the vertices blown up, so that
\(\Omega _0\)
is a surface with corners. We also let
\({\tilde{V}}\)
be the lift of
V
to
\(\Omega _0\)
, that is, the union of the faces
\(\{r=0\}\)
at each vertex.
Throughout, we will use the time coordinate
\(T=\sqrt{t}\)
. This changes the smooth structure at
\(t=0\)
somewhat, but allows us to avoid the use of parabolic blow-ups.
The heat kernel restricted to the diagonal is defined on
\(\Omega \times [0, \infty )_T\)
and is dubbed
the diagonal heat kernel.
The single heat space is a natural habitat of the diagonal heat kernel in the sense that the diagonal heat kernel lifted to the single heat space is pc. Note that the single heat space is the same for all the possible boundary conditions we consider. To create the single heat space, we begin with the manifold with corners
\(\Omega _0\times [0,1)_T\)
. We denote its
\(T=0\)
boundary hypersurface
Footnote
1
by tf. The remainder of the boundary hypersurfaces correspond either to an edge or to a vertex (which has been blown up, so there is a boundary hypersurface for each vertex). Denote the edge/side faces for positive
T
by
\(\{e_j\}_{j=1}^{|E|}\)
, and the vertex faces
\({\tilde{V}}_j\times [0,1)_T\)
by
$$\begin{aligned} \{ s v_j\}_{j=1} ^{|V|}. \end{aligned}$$
(3.1)
Next we perform blow-ups, first of the vertices at
\(T=0\)
and then of the edges at
\(T=0\)
, to create the
single space
Footnote
2
$$\begin{aligned} M_h = [ \Omega _0 \times [0, 1)_T; \{s v_j\}_{j=1}^{|V|} \cap \{T=0\}; {E \times \{T=0\}}]. \end{aligned}$$
We call the new faces obtained
\(\{pv_j\}_{j=1}^{|V|}\)
and
\(\{pe_j\}_{j=1}^{|E|}\)
.
Fig. 2
Full size image
Single heat space
The sequence of blowups is therefore:
1.
the normal blowup about each vertex for all time (implicit in the starting point of
\(\Omega _0\times [0,1)_T\)
);
2.
the blowup of each vertex at
\(T=0\)
;
3.
the blowup of each edge at
\(T=0\)
.
The space
\(M_h\)
has
\(2|V|+2|E|+1\)
boundary hypersurfaces in total.
To motivate this construction, consider the diagonal heat kernel on an infinite sector, which from (
2.8
) is
$$\begin{aligned} H(t,r,\theta ,r,\theta )=\frac{1}{2T^2}\exp \left[ -\frac{r^2}{2T^2}\right] \sum _{j=1}^{\infty }I_{\nu _j}\left( \frac{r^2}{2T^2}\right) |\phi _j(\theta )|^2. \end{aligned}$$
The pre-factor is not a pc function of (
r
,
T
), but it is a pc function of (
r
,
T
/
r
). And indeed, after creating
\(\hbox {pv}_j\)
,
T
/
r
may be taken as a boundary defining function for tf near
\(\hbox {pv}_j\)
.
In relation to the literature, our heat space construction can be seen as a hybrid combining elements of Mooers’s heat space for manifolds with isolated conical singularities [
41
] and Mazzeo and Vertman’s heat space for manifolds with edges [
35
]. The first step in Mooers’s construction is to blow up the conical singularity by replacing the point with the cross-section (link) of the cone. Next she takes the product with time. It is completely equivalent to first take the product with time, and then perform a normal blowup of the cone point for all time. This is the procedure we follow at the vertices (and cone points). Next, we perform blowups at
\(T=0\)
of the edges (and smooth boundary), analogous to [
35
].
In fact our construction can be viewed as an iterated version of [
35
], where we perform each of their blow-ups at the vertices (of codimension 2) and then at the edges (of codimension 1). We expect that a similar construction, with additional iteration, could work for polyhedral domains in manifolds of arbitrary dimension.
3.3
The double heat space
The double heat space is a natural habitat of the heat kernel in the sense that the heat kernel, initially defined on
\(\Omega \times \Omega \times [0,\infty )\)
, lifts to be pc on it. As with the single space, our models guide the construction of the double heat space by indicating which p-submanifolds should be blown up to ensure that the heat kernel will be pc. The general philosophy is to mimic [
35
], performing each of their blow-ups first at the vertices and then at the edges.
Begin with
\(M^2:=\Omega _0\times \Omega _0\times [0,1)_T\)
. As we are using
\(\Omega _0\)
rather than
\(\Omega \)
, this is now a manifold with corners, the analogue of the space with which Mazzeo and Vertman begin [
35
, Sect. 3.1]. Denote its
\(T=0\)
boundary hypersurface by tf. All other boundary hypersurfaces are of one of the following forms:
\(E_j\times \Omega _0\times [0,1)\)
, which we call
\(E_{j0}\)
,
\(\Omega _0\times E_j\times [0,1)\)
, which we call
\(E_{0j}\)
,
\({\tilde{V}}_j\times \Omega _0\times [0,1)\)
, which is now a boundary hypersurface which we call
\(\hbox {hvrf}_j\)
;
\(\Omega _0\times {\tilde{V}}_j\times [0,1)\)
, which we call
\(\hbox {hvlf}_j\)
.
As a guide to the nomenclature here,“h” indicates “height” because these blowups persist for all time, and time is usually the vertical axis in figures of this type. As usual, “v” indicates vertices, and “ff”, “rf”, and “lf” indicate left, right, and front faces respectively.
Footnote
3
Now, for each
j
and
k
, blow up the intersection
\(\hbox {hvlf}_{j}\cap \hbox {hvrf}_k\)
to create a new boundary hypersurface
Footnote
4
\(\hbox {hvff}_{jk}\)
. At this point we call the new space
\(M_0^2\)
:
$$\begin{aligned} M_0^2=[\Omega _0\times \Omega _0\times [0,1);\ \cup _{j,k}\text {hvlf}_j\cap \text {hvrf}_k]. \end{aligned}$$
The next step is to blow up the union over all
j
of
\(\hbox {hvff}_{jj}\cap \{T=0\}\)
. This blowup creates
N
boundary faces, one at each vertex, denoted by
\(\hbox {ff}_j\)
. We shall collectively refer to these as ff for “front face(s).” The resulting space is
$$\begin{aligned} {[}M_0 ^2; \cup _j \text {hvff}_{jj} \cap \{ T=0\}]. \end{aligned}$$
This construction at the vertices needs to be imitated at the edges, so now lift the triple intersection of the diagonal, boundary, and
\(T=0\)
, namely
\(\{ (z, z', 0): z=z' \in E\}\)
, to
\([M_0 ^2; \text {hvff}_{jj} \cap \{T=0\}]\)
. As the lift of a p-submanifold is a p-submanifold, this lift is a boundary p-submanifold which meets ff. We blow it up, creating a new boundary hypersurface at each side face. We denote their union by sf, for “side face(s)”. When we need to distinguish components, we shall refer to the
\(j^{th}\)
component as
\(\hbox {sf}_{j}\)
. Observe that the side faces are pairwise disjoint, as their intersection in
\(\Omega _0\times \Omega _0\times [0,1)\)
has already been blown up to create ff. Let us call the space at this point the “reduced double heat space”
\(M_{rh}^2\)
. It is the analogue in our setting of the “intermediate heat space” in [
35
, Sect. 3.1]. Specifically, we have
$$\begin{aligned} M_{rh}^2=[M_0 ^2; \cup _j\text {hvff}_{jj} \cap \{ T=0\}; \{ (z, z', 0): z=z' \in E\}]. \end{aligned}$$
The final blowup is at the lift of the diagonal at
\(T=0\)
. This blowup produces the double heat space:
$$\begin{aligned} M_h^2=[M_{rh} ^2; \{ (z, z', 0): z=z' \in \Omega \}]. \end{aligned}$$
Call the new front face td, for “time diagonal.” It intersects both sf and ff, as well as tf, though no other boundary hypersurfaces (in particular none of the hvff, hvlf, or hvrf components, as the intersection of the diagonal with the boundary has already been blown up). The double heat space is depicted in Fig.
3
.
Fig. 3
Full size image
This is a schematic depiction of the double heat space
3.4
The triple heat space
The triple heat space, unlike the single and double heat spaces, is
not
a natural habitat. Instead, it is an artificial environment to which we shall lift the Schwartz kernels of operators from their natural habitats on the double space in order to compose them. With the correct construction of the triple space, the process of composition returns an element which is pc on the double space. Consequently, the construction of the triple space is guided by the desire to be able to lift and compose Schwartz kernels which live on the double heat space.
Our construction is based on that of Mazzeo and Vertman [
35
], and indeed is identical when
\(V=\emptyset \)
, that is when there are no vertices. Our guiding principle is that whenever Mazzeo and Vertman blow up a boundary, we first blow up
V
and then
E
. However, our setting is further complicated by the additional blow-ups at the vertices for positive time. To begin, we consider the original triple space, with the vertices blown up in each factor so that we have the structure of a manifold with corners:
$$\begin{aligned} M^3:=\Omega _0\times \Omega _0\times \Omega _0\times [0,1) \times [0,1) \end{aligned}$$
(3.2)
along with the three projections
\(\pi _C\)
,
\(\pi _L\)
, and
\(\pi _R\)
defined by
$$\begin{aligned}  &   \pi _C:M^3\rightarrow \Omega _0^2\times {\mathbb {R}}_{\sqrt{(T')^2+(T'')^2}}, (z,z',z'',T',T'')\rightarrow (z,z'',\sqrt{(T')^2+(T'')^2}); \end{aligned}$$
(3.3)
$$\begin{aligned}  &   \pi _L:M^3\rightarrow \Omega _0^2\times {\mathbb {R}}_{T'}, (z,z',z'',T',T'')\rightarrow (z,z',T'); \end{aligned}$$
(3.4)
$$\begin{aligned}  &   \pi _R:M^3 \rightarrow \Omega _0^2\times {\mathbb {R}}_{T''}, (z,z',z'',T',T'')\rightarrow (z',z'',T''). \end{aligned}$$
(3.5)
These projections will be used to re-interpret operator composition in terms of pullbacks and push-forwards. Modulo all the technical details, if we have two operators, one
A
with Schwartz kernel
\(K_A\)
and the other
B
with Schwartz kernel
\(K_B\)
, the Schwartz kernel
\(K_C\)
of the composition
\(C=A\circ B\)
is given by
$$\begin{aligned} K_C=(\pi _C)_*(\pi _L^*K_A\pi _R^*K_B). \end{aligned}$$
Fortunately, we do not need the full composition formula, just the version in which one of the operators vanishes to infinite order at td. This is because we use the composition formula to run a Neumann series argument to construct our heat kernel, and with a good enough initial parametrix for the heat kernel, the error will vanish to infinite order at td. For this reason, we will construct a reduced triple heat space
\(M^3_{rh}\)
in order to prove a special case of the composition formula, the case in which
\(K_B\)
has order
\(\infty \)
at the face td. In this case,
\(K_B\)
is pc on
\(M^2_{rh}\)
.
Footnote
5
The triple space construction is guided by the following conditions, which are necessary and sufficient to obtain the composition formula we require:
1.
we need the projection
\(\pi _C\)
to lift to a b-fibration
\(\Pi _C:M^3_{rh}\rightarrow M^2_{rh}\)
;
2.
we need the projection
\(\pi _L\)
to lift to a b-map
\(\Pi _L:M^3_{rh}\rightarrow M^2_h\)
;
3.
since
\(K_B\)
is pc on
\(M^2_{rh}\)
, we need only that the projection
\(\pi _R\)
lift to a b-map
\(\Pi _R:M^3_{rh}\rightarrow M^2_{rh}\)
.
We therefore recall the definitions of these important “b-notions.”
Definition 3.3
[
39
, p. 51] Let
\(f: X \rightarrow Y\)
be a smooth map between manifolds with corners,
X
with boundary hypersurfaces
\(M_1(X)\)
, and
Y
with boundary hypersurfaces
\(M_1(Y)\)
. Then
f
is a
b-map
if for each
\(H \in M_1(Y)\)
, and boundary defining function
\(\rho _H\)
$$\begin{aligned} f^*(\rho _H) = 0 \quad \text {or} \quad f^*(\rho _H) = a \cdot \prod _{G \in M_1 (X)} \rho _G ^{e_f (G, H)}, \quad 0< a \in \mathcal {C}^\infty (X). \end{aligned}$$
In the latter case, the numbers
\(e_f (G,H)\)
are called the boundary exponents of
f
. In this case, writing
\(M_1 (X) = \{ G_j\}_{j=1} ^n\)
and
\(M_1 (Y) = \{H_k \}_{k=1} ^m\)
, the
exponent matrix
is the matrix whose entries are
\(\{e_f (G_j, H_k)\}_{j,k=1} ^{n,m} \)
.
Definition 3.4
[
39
, p. 53] A b-map is a
b-submersion
if the b-differential is surjective for all
\(x \in X\)
. For the definition of the b-differential, we refer to [
39
, pp. 53–54].
Definition 3.5
[
39
, p. 53] A b-map is
b-normal
if
\(\, ^b f_*\)
, defined as in [
39
, (7), p. 53] is surjective.
Definition 3.6
[
19
, p. 124] A b-map is a
b-fibration
if
\(f_*\)
, acting on the b-tangent bundle, is surjective on each fibre, and the image of each boundary hypersurface in
X
is either
Y
or one boundary hypersurface
\(H \subset Y\)
. We note that this holds if and only if the b-map is both b-normal and a b-submersion [
39
, p. 53].
Definition 3.7
[
19
, p. 124] A total boundary defining function for
X
, which we denote
\(\rho _X\)
, is the product of boundary defining functions for all the boundary hypersurfaces. We say that a b-fibration is
simple
if
$$\begin{aligned} f^* \rho _Y = a \cdot \rho _X, \quad 0<a \in \mathcal {C}^\infty (X). \end{aligned}$$
In terms of the exponent matrix, this is equivalent to requiring that the elements are either 0 or 1, and moreover for each
\(G \in M_1 (X)\)
there exists precisely one
\(H \in M_1 (Y)\)
with
\(e_f (G,H) = 1\)
.
To start constructing
\(M^3_{rh}\)
, we begin with (
3.2
). This space has a number of boundary hypersurfaces: the
\(T''=0\)
face, which we denote
\(F_{TL}\)
, the
\(T'=0\)
face, which we denote
\(F_{TR}\)
, and a number of faces of the form
\(E_j\times \Omega _0 \times \Omega _0 \times [0,1)_{T''}\times [0,1)_{T'}\)
, which we call
\(F_{j00}\)
, with similar notation for products where
\(E_j\)
is in the second or third factor. We also have a number of faces of the form
\({\tilde{V}}_j\times \Omega _0 \times \Omega _0 \times [0,1)\times [0,1)\)
, which we call
\(F_{V_j00}\)
and collectively
\(F_{V00}\)
, et cetera. The notation used in the triple space is a bit different from the single and double spaces, in particular the use of capitals. This is in part to distinguish the triple space as an artefact to be used for the purpose of composition and in part to draw a parallel to related constructions in the literature [
1
,
50
] which use an analogous notation.
A few blow-up facts will be useful throughout.
Proposition 3.8
The following are true (each is well-known in the geometric microlocal literature):
1.
Blow-ups which are nested, disjoint, or transverse commute [
19
, Lemma 2.1].
2.
Blow-down maps are b-maps [
16
, Sect. 2.3.3], [
19
, Proof of Lemma 2.7]. Moreover, if
\(Y\subset X\)
is an intersection of boundary hypersurfaces of
X
, then the blow-down map from
\([X;Y]\rightarrow X\)
is a b-submersion. (This reduces to the case
\(X={\mathbb {R}}^n_+\)
,
\(Y=0\)
, and then follows from a computation in local coordinates).
3.
The composition of b-maps is a b-map [
16
, Sect. 2.3.3]. Further, it follows immediately from the definition that the composition of b-submersions is a b-submersion.
4.
Once a b-map is known to be a b-submersion, checking b-normality is a matter of ensuring, by checking the exponent matrix, that no boundary hypersurface is mapped into a face of codimension
\(>1\)
in the image [
16
, Definition 3.9], [
1
, Remark B.4].
We will also use the following.
Lemma 3.9
Suppose
A
,
B
,
C
, and
D
are p-submanifolds of a manifold with corners
X
, and suppose that
$$\begin{aligned} A\subseteq B\subseteq D,\ A\subseteq C\subseteq D, \text{ and } B\cap C\subseteq A. \end{aligned}$$
Then
$$\begin{aligned} {[}X;C;D;A;B]\cong [X;A;B;C;D]. \end{aligned}$$
Proof
Nested blow-ups commute, so we may do
A
before
C
and
D
and thus
$$\begin{aligned} {[}X;C;D;A;B]\cong [X;A;C;D;B]. \end{aligned}$$
Similarly, we may do
B
before
D
and thus
$$\begin{aligned} {[}X;C;D;A;B]\cong [X;A;C;B;D]. \end{aligned}$$
Now since
\(B\cap C\subseteq A\)
, the lifts of
B
and
C
are disjoint in the space [
X
;
A
], and since disjoint blow-ups commute they may be done in either order. This completes the proof.
\(\square \)
Our strategy will be to repeatedly take advantage of the following lemma of Hassell, Mazzeo, and Melrose [
19
]:
Lemma 3.10
[
19
, Lemma 2.5] Suppose
\(f:X\rightarrow Y\)
is a simple b-fibration of compact manifolds with corners. Suppose
\(U\subset Y\)
is a closed p-submanifold. Then, with
S
the minimal collection of p-submanifolds of
X
into which the lift of
U
under
f
decomposes,
f
extends from the complement of
\(f^{-1}(U)\)
to a b-fibration
\(f_U:[X,S]\rightarrow [Y,U]\)
, for any order of blow-up of the elements of
S
.
This lemma guides our construction of the triple space using the construction of the double space.
3.5
Lifting the projection maps
To construct the triple space from
\(M^3\)
we first blow up
\({\mathcal {O}}=\{T'=T''=0\}\)
. The spatial variables are unaffected by this blow-up and so the space
$$\begin{aligned} {[}M^3;{\mathcal {O}}]=\Omega _0^3\times [[0,1)\times [0,1);\{0,0\}]. \end{aligned}$$
(3.6)
Denote the new front face by
\(F_{{\mathcal {O}}}\)
, and as usual continue to denote the
\(T''=0\)
face by
\(F_{TL}\)
and the
\(T'=0\)
face by
\(F_{TR}\)
. We claim:
Lemma 3.11
The projections
\(\pi _C\)
,
\(\pi _L\)
, and
\(\pi _R\)
lift by continuity to projections
\(\Pi _C\)
,
\(\Pi _L\)
, and
\(\Pi _R\)
with domain
\([M^3;{\mathcal {O}}]\)
and ranges as in (
3.3
), (
3.4
), (
3.5
). Moreover,
\(\Pi _C\)
,
\(\Pi _L\)
, and
\(\Pi _R\)
are all b-fibrations. Under
\(\Pi _C\)
, the image of
\(F_{{\mathcal {O}}}\)
is the face
\(\{T=0\}\)
, and the faces at
\(T'=0\)
and
\(T''=0\)
are mapped into the interior.
Proof
This follows immediately from (
3.6
) and the corresponding statement considering only the time variables. Specifically, the map
$$\begin{aligned} \Pi :[[0,1)_{T'}\times [0,1)_{T''}; \{(0,0)\}]\rightarrow [0,1)_{T},\ T=\sqrt{(T')^2+(T'')^2} \end{aligned}$$
is a b-fibration, where the image of the front face is
\(\{T=0\}\)
, and the image of the other two faces is [0, 1). Now the lifted projection
\(\Pi _C\)
is simply
\(\Pi \)
in the time variables and the usual projection from
\(M^3\)
to
\(M^2\)
in the spatial variables, and thus is itself a b-fibration. Similar arguments take care of
\(\Pi _L\)
and
\(\Pi _R\)
, as left and right projection lift to b-fibrations from
\([{\mathbb {R}}_+^2; \{0\}]\)
to
\({\mathbb {R}}\)
.
\(\square \)
We will now make further blow-ups to
\([M^3;{\mathcal {O}}]\)
which allow all three of these maps to be b-fibrations onto
\(M_0^2\)
. In each we use
3.10
. Recalling (
3.6
), we define submanifolds
\({\mathcal {P}}_{VVV}\)
,
\({\mathcal {P}}_{VV0}\)
,
\({\mathcal {P}}_{V0V}\)
, et cetera of
\([M^3;{\mathcal {O}}]\)
by restricting to
\({\tilde{V}}\)
(the lift of
V
) each of the spatial variables which have index
V
rather than 0. For example,
$$\begin{aligned} {\mathcal {P}}_{V0V}={\tilde{V}}\times \Omega _0\times {\tilde{V}}\times [[0,1)\times [0,1);\{0,0\}]. \end{aligned}$$
Using this notation, the lift of hvff under
\(\Pi _C\)
is
\({\mathcal {P}}_{V0V}\)
, under
\(\Pi _L\)
is
\({\mathcal {P}}_{VV0}\)
, and under
\(\Pi _R\)
is
\({\mathcal {P}}_{0VV}\)
. Then the lifts of hvlf and hvrf may be computed under each map. Application of Lemma
3.10
shows that
$$\begin{aligned}  &   \Pi _C:[M^3;{\mathcal {O}};{\mathcal {P}}_{V0V}]\rightarrow M_0^2,\\  &   \Pi _L:[M^3;{\mathcal {O}};{\mathcal {P}}_{VV0}]\rightarrow M_0^2,\\  &   \Pi _R:[M^3;{\mathcal {O}};{\mathcal {P}}_{0VV}]\rightarrow M_0^2, \end{aligned}$$
are each b-fibrations. In fact we can define a common domain: let
$$\begin{aligned} M_0^3:=[M^3;{\mathcal {O}};{\mathcal {P}}_{VVV};{\mathcal {P}}_{V0V};{\mathcal {P}}_{0VV};{\mathcal {P}}_{VV0}]. \end{aligned}$$
Denote the new faces created by
\(F_{VVV}\)
,
\(F_{V0V}\)
, et cetera.
Proposition 3.12
\(\Pi _C\)
,
\(\Pi _L\)
, and
\(\Pi _R\)
all lift to b-fibrations from
\(M_0^3\)
to
\(M_0^2\)
.
Proof
First observe that
\(M_0^3\)
is a blow-up of each of the three domain spaces for
\(\Pi _C\)
,
\(\Pi _L\)
, and
\(\Pi _R\)
. Indeed, begin with the domain space for
\(\Pi _C\)
and blow up the lift of
\({\mathcal {P}}_{VVV}\)
. This blow-up is nested with the blow-up of
\({\mathcal {P}}_{V0V}\)
, so it may be done before that. So a blow-up of the domain space for
\(\Pi _C\)
is
$$\begin{aligned} {[}M^3;{\mathcal {O}};{\mathcal {P}}_{VVV};{\mathcal {P}}_{V0V}]. \end{aligned}$$
Now we can blow up the lifts of
\({\mathcal {P}}_{0VV}\)
and
\({\mathcal {P}}_{VV0}\)
, which are disjoint from the lift of
\({\mathcal {P}}_{V0V}\)
and thus can be done in any order. Analogous arguments show that
\(M_0^3\)
is a blow-up of each of the three domain spaces. Since all our p-submanifolds are intersections of boundary hypersurfaces, by Proposition
3.8
b),
\(\Pi _C\)
,
\(\Pi _R\)
, and
\(\Pi _L\)
are all b-submersions from
\(M_0^3\)
to
\(M_0^2\)
.
At this point, proving these maps are b-fibrations is simply a matter of checking their exponent matrices to make sure no boundary hypersurface is mapped into a corner. This calculation is combinatorial, very similar to the proof of Lemma 3.14 in [
33
], and as a result we omit it.
\(\square \)
Having proven that
\(\Pi _C\)
is a b-fibration from
\(M_0 ^3 \rightarrow M_0 ^2\)
, we shall now lift
\(\Pi _C\)
to be a b-fibration onto
\(M^2 _{rh}\)
. Let
\({\mathcal {O}}_{V0V}=F_{{\mathcal {O}}}\cap \{z=z''\in {\tilde{V}}\}\)
, with a similar definition for
\({\mathcal {O}}_{E0E}\)
,
\({\mathcal {O}}_{VVV}, {\mathcal {O}}_{EEE},\)
etc. Using Lemma
3.10
, we obtain that
\(\Pi _C\)
lifts to a b-fibration
$$\begin{aligned} \Pi _C:[M_0^3;{\mathcal {O}}_{V0V};{\mathcal {O}}_{E0E}]\rightarrow M^2_{rh}. \end{aligned}$$
Call the new faces
\(F_{\mathcal {O}V0V}\)
and
\(F_{\mathcal {O}E0E}\)
. We are now in good shape with
\(\Pi _C\)
but we need to do more work in order for
\(\Pi _L\)
and
\(\Pi _R\)
to be b-maps onto
\(M_h^2\)
and
\(M_{rh}^2\)
respectively.
To begin the extra work, we do some more blow-ups which preserve the b-fibration property of
\(\Pi _C\)
. Begin with
\({\mathcal {O}}_{VVV}\)
, which in
\(M_0^3\)
is
\(F_{{\mathcal {O}}}\cap \{z=z'=z''\in {\tilde{V}} \}\)
. Using notation as before, we claim that
$$\begin{aligned} \Pi _C:M^3_{cen}:=[M_0^3;{\mathcal {O}}_{V0V};{\mathcal {O}}_{E0E};{\mathcal {O}}_{VVV};{\mathcal {O}}_{EEE}]\rightarrow M^2_{rh} \end{aligned}$$
is a b-fibration. Indeed, this follows from two applications of [
19
, Lemma 2.7].
Footnote
6
Moreover, by an application of Lemma
3.9
, we have
$$\begin{aligned} M^3_{cen}=[M_0^3;{\mathcal {O}}_{VVV};{\mathcal {O}}_{EEE};{\mathcal {O}}_{V0V};{\mathcal {O}}_{E0E}]. \end{aligned}$$
Continuing in this vein, let
\(L_{0VV}=F_{TL}\cap \{z'=z''\in {\tilde{V}}\}\)
, with similar notations for
\(L_{0EE}\)
,
\(R_{VV0}\)
,
\(R_{EE0}\)
, and let
\(R_{diag}=F_{TL}\cap \{z=z'\}\)
. Let
$$\begin{aligned}M^3_{rh,c}:=[M^3_{cen};R_{VV0};R_{EE0};R_{diag};L_{0VV};L_{0EE}].\end{aligned}$$
Denote the five new boundary hypersurfaces by
\(F_{RVV0}\)
,
\(F_{REE0}\)
,
\(F_{TRD}\)
,
\(F_{L0VV}\)
, and
\(F_{L0EE}\)
. None of the five new boundary hypersurfaces are mapped into a corner by
\(\Pi _C\)
; their images are hvrf,
\(\cup _j E_{j0}\)
, the interior, hvlf, and
\(\cup _j E_{0j}\)
respectively. Thus by the same argument with [
19
, Lemma 2.17],
\(\Pi _C:M^3_{rh,c}\rightarrow M^2_{rh}\)
is a b-fibration.
Finally, using similar notation, we define p-submanifolds
\({\mathcal {O}}_{VV0}\)
,
\({\mathcal {O}}_{EE0}\)
,
\({\mathcal {O}}_{0VV}\)
,
\({\mathcal {O}}_{0EE}\)
, and
\({\mathcal {O}}_D\)
, which is the interior lift of
\(\{t'=t''=0,z=z'\}\)
in our new space. Define the
reduced triple heat space
$$\begin{aligned} M^3_{rh}:=[M^3_{rh,c};{\mathcal {O}}_{VV0};{\mathcal {O}}_{EE0};{\mathcal {O}}_{0VV};{\mathcal {O}}_{0EE};{\mathcal {O}}_{D}]. \end{aligned}$$
Call the new boundary hypersurfaces
\(F_{\mathcal {O}VV0}\)
,
\(F_{\mathcal {O}EE0}\)
,
\(F_{{\mathcal {O}}0VV}\)
,
\(F_{{\mathcal {O}}0EE}\)
, and
\(F_{\mathcal {O}D}\)
. It is no longer true that
\(\Pi _C\)
is a b-fibration from
\(M^3_{rh}\)
onto
\(M^2_{rh}\)
, but it is a b-map.
We must also know something about
\(\Pi _L\)
and
\(\Pi _R\)
:
Proposition 3.13
\(\Pi _L\)
and
\(\Pi _R\)
lift by continuity to well-defined b-maps from
\(M^3_{rh}\)
to
\(M^2_h\)
and
\(M^2_{rh}\)
respectively.
Proof
It is immediate by composing with the blow-down map that
\(\Pi _L\)
and
\(\Pi _R\)
lift to well-defined b-maps from
\(M^3_{rh}\)
to
\(M_0^2\)
. The question is whether they still lift to b-maps when
\(M_0^2\)
is blown up to create ff, then sf, then (for
\(\Pi _L\)
) td. But this may be checked directly: computing the pullbacks of the boundary defining functions for the boundary hypersurfaces of
\(M^2_{h}\)
and
\(M^2_{rh}\)
shows that each is a product of boundary defining functions on
\(M^3_{rh}\)
. The specific products are given below, in Lemma
3.14
(Fig.
4
).
\(\square \)
Fig. 4
Full size image
The schematic diagram for the construction of the reduced triple space as required here for our composition rule. The kernel
\(K_A\)
lifts from the double heat space,
\(M_h ^2\)
, to the triple heat space via pullback by the projection map
\(\Pi _L\)
. The kernel
\(K_B\)
vanishes to infinite order at td, so it is pc on the reduced double heat space. It lifts to the triple heat space via pullback by the projection map
\(\Pi _R\)
. On
\(M_{rh} ^3\)
the two kernels are composed, and the result is then pushed forward by the blow-down map to
\(M_{rh,c} ^3\)
, followed by the projection map
\(\Pi _C\)
to
\(M_{rh} ^2\)
3.6
Combinatorics of b-maps
Now we come to the key combinatorial lemma for composition. Recall that
\(\Pi _L:M^3_{rh}\rightarrow M^2_h\)
and
\(\Pi _R:M^3_{rh}\rightarrow M^2_{rh}\)
are b-maps and
\(\Pi _C:M^3_{rh,c}\rightarrow M^2_{rh}\)
is a b-fibration.
Lemma 3.14
The exponent matrix entries for the b-maps
\(\Pi _L:M^3_{rh}\rightarrow M^2_h\)
,
\(\Pi _R: M^3_{rh}\rightarrow M^2_{rh}\)
, and
\(\Pi _C:M^3_{rh,c}\rightarrow M^2_{rh}\)
are all zero, except for the following, which are 1:
$$\begin{aligned}  &   \text{ For } \Pi _L: (F_{TR},\text {tf}),(F_{\mathcal {O}},\text {tf}),(F_{\mathcal {O}V_j0V_j},\text {tf}), (F_{\mathcal {O}E_j0E_j},\text {tf}), (F_{\mathcal {O}0V_jV_j},\text {tf}),\nonumber \\  &   \quad (F_{\mathcal {O}0E_jE_j},\text {tf}), (F_{TRD},\text {td}),(F_{\mathcal {O}D},\text {td}), (F_{\mathcal {O}V_j V_j V_j},\text {ff}_j), (F_{R V_j V_j 0}, \text {ff}_j), (F_{\mathcal {O}V_j V_j 0},\text {ff}_j),\nonumber \\  &   \quad (F_{\mathcal {O}E_j E_j E_j},\text {sf}_j), (F_{R E_j E_j 0},\text {sf}_j), (F_{\mathcal {O}E_j E_j 0},\text {sf}_j),(F_{V_jV_kV_l},\text {hvff}_{jk}),(F_{V_jV_k0},\text {hvff}_{jk}),\nonumber \\  &   \quad (F_{V_j0V_l},\text {hvrf}_j),(F_{V_j00},\text {hvrf}_j),(F_{\mathcal {O}V_j0V_j},\text {hvrf}_j),\nonumber \\  &   \quad (F_{0V_kV_l},\text {hvlf}_k),(F_{0V_k0},\text {hvlf}_k), (F_{\mathcal {O}0V_jV_j},\text {hvlf}_j), (F_{L0V_jV_j},\text {hvlf}_j),\nonumber \\  &   \quad (F_{\mathcal {O}E_j0E_j},E_{j0}),(F_{j00},E_{j0}),(F_{\mathcal {O}0E_jE_j},E_{0j}),(F_{0j0},E_{0j}),(F_{L0E_jE_j},E_{0j}), \end{aligned}$$
(3.7)
with
\(F_{TL}\)
,
\(F_{00\,l}\)
, and
\(F_{00V_l}\)
mapping to the interior.
$$\begin{aligned}  &   \text{ For } \Pi _R: (F_{TL},\text {tf}), (F_{{\mathcal {O}}},\text {tf}), (F_{\mathcal {O}D},\text {tf}), (F_{\mathcal {O}V_j0V_j},\text {tf}), (F_{\mathcal {O}E_j0E_j},\text {tf}),\nonumber \\  &   \quad (F_{\mathcal {O}V_jV_j0},\text {tf}), (F_{\mathcal {O}E_jE_j0},\text {tf}), (F_{\mathcal {O}V_jV_jV_j},\text {ff}_j), (F_{L0V_jV_j}, \text {ff}_j), (F_{{\mathcal {O}}0V_jV_j},\text {ff}_j),\nonumber \\  &   \quad (F_{\mathcal {O}E_jE_jE_j},\text {sf}_j), (F_{L0E_jE_j},\text {sf}_j), (F_{{\mathcal {O}}0E_jE_j},\text {sf}_j),(F_{V_jV_kV_l},\text {hvff}_{kl}),(F_{0V_kV_l},\text {hvff}_{kl}),\nonumber \\  &   \quad (F_{V_j0V_l},\text {hvlf}_l),(F_{00V_l},\text {hvlf}_l),(F_{\mathcal {O}V_j0V_j},\text {hvlf}_j),\nonumber \\  &   \quad (F_{V_jV_k0},\text {hvrf}_k),(F_{0V_k0},\text {hvrf}_k), (F_{\mathcal {O}V_jV_j0},\text {hvrf}_j), (F_{RV_jV_j0},\text {hvrf}_j),\nonumber \\  &   \quad (F_{\mathcal {O}E_j0E_j},E_{0j}),(F_{00j},E_{0j}),(F_{\mathcal {O}E_jE_j0},E_{j0}),(F_{0j0},E_{j0}),(F_{RE_jE_j0},E_{j0}), \end{aligned}$$
(3.8)
with
\(F_{TR}\)
,
\(F_{j00}\)
,
\(F_{V_j00}\)
, and
\(F_{TRD}\)
mapping to the interior.
$$\begin{aligned}  &   \text{ For } \Pi _C: (F_{{\mathcal {O}}},\text {tf}), (F_{j00}, E_{j0}), (F_{RE_jE_j0},E_{j0}), (F_{00j}, E_{0j}),\nonumber \\  &   \quad (F_{L0E_jE_j},E_{0j}), (F_{\mathcal {O}V_jV_jV_j},\text {ff}_j),(F_{\mathcal {O}V_j0V_j},\text {ff}_j), (F_{\mathcal {O}E_jE_jE_j},\text {sf}_j), (F_{\mathcal {O}E_j0E_j},\text {sf}_j),\nonumber \\  &   \quad (F_{V_jV_kV_l}, \text {hvff}_{jl}), (F_{V_j0V_l}, \text {hvff}_{jl}), (F_{V_jV_k0},\text {hvrf}_j), (F_{V_j00},\text {hvrf}_j), (F_{RV_jV_j0}, \text {hvrf}_j),\nonumber \\  &   \quad (F_{0V_kV_l}, \text {hvlf}_l),(F_{00V_l},\text {hvlf}_l), (F_{L0V_lV_l},\text {hvlf}_l), \end{aligned}$$
(3.9)
with
\(F_{TR}\)
,
\(F_{TL}\)
,
\(F_{0j0}\)
,
\(F_{0V_j0}\)
, and
\(F_{TRD}\)
mapping to the interior.
Proof
All of the exponent matrices are computed the same way: by computing pullbacks of boundary defining functions. Consider, for example, the face
\(\text {ff}_j\)
of
\(M^2_{rh}\)
. The faces of
\(M_{rh,c} ^3\)
which are in the preimage of
\(\text {ff}_j\)
under
\(\Pi _C\)
are all of the faces where
\(z=z''=V_j\)
and
\(\sqrt{(T')^2+(T'')^2}=0\)
, that is
\(T'=T''=0\)
. These are precisely
\(F_{\mathcal {O}V_jV_jV_j}\)
and
\(F_{\mathcal {O}V_j0V_j}\)
, so those two faces map to
\(\text {ff}_j\)
, and the corresponding exponent matrix entries are 1. Computing these pullbacks for each boundary hypersurface of
\(M^2_{rh}\)
yields the desired exponent matrix for
\(\Pi _C\)
. By a similar process we obtain the exponent matrices for
\(\Pi _L\)
and
\(\Pi _R\)
.
Note also that the fact that
\(\Pi _C\)
is a b-fibration can be observed directly: for each boundary hypersurface
G
of
\(M^3_{rh,c}\)
there is at most one boundary hypersurface
H
of
\(M^2_{rh}\)
such that the (
G
,
H
) exponent matrix entry for
\(\Pi _C\)
equals 1.
\(\square \)
3.7
Densities
Our kernels on the double space are most naturally considered as “full right densities” with respect to the usual metric on
\(\Omega \)
. For example, the kernels of our operators
A
and
B
will be
$$\begin{aligned} K_A(t',z,z')\,dt'\, dz';\ K_B(t'',z',z'')\, dt''\, dz'', \quad \text { respectively.} \end{aligned}$$
Multiplying the two, then integrating over
\(t=t'+t''\)
and
\(z'\)
, yields
$$\begin{aligned} K_{A\circ B}(t,z.z')\,dt\, dz''. \end{aligned}$$
If we multiply everything in the expressions by
dz
, we have the full-density form we need for the pushforward theorem; see [
31
, Theorems 4 and 5] and [
19
, Theorem 2.3].
To apply the aforementioned pushforward theorem, we need to transform our natural metric densities into canonical full densities and b-densities on
\(M^3_{rh,c}\)
and
\(M^2_{rh}\)
. Here are the formulas for those transformations. Throughout, let
\(\nu (X)\)
and
\(\nu _b(X)\)
be canonical densities and b-densities on a manifold with corners
X
, and let
\(\rho _{tot}(X)\)
be a product of boundary defining functions for all boundary hypersurfaces of
X
. It is immediate that
\(\nu _b(X)=\rho _{tot}^{-1}(X)\nu (X)\)
.
Proposition 3.15
The density bundles transform under blow-ups as follows:
$$\begin{aligned}&\beta ^*(\nu (\Omega \times \Omega \times [0,1)))=\rho _{ff}^4\rho _{sf}^3\rho _{hvff}^3\rho _{hvlf}\rho _{hvrf}\nu (M^2_{rh}); \\&\beta ^*(\nu (\Omega \times \Omega \times \Omega \times [0,1)))=\rho _{{\mathcal {O}}}\rho _{\mathcal {O}VVV}^7\rho _{\mathcal {O}EEE}^6\rho _{\mathcal {O}V0V}^5\rho _{\mathcal {O}E0E}^4\rho _{VVV}^5\rho _{V0V}^3 \\&\cdot \rho _{0VV}^3\rho _{VV0}^3\rho _{V00}\rho _{0V0}\rho _{00V} \rho _{RVV0}^4\rho _{REE0}^3\rho _{L0VV}^4\rho _{L0EE}^3\rho _{TRD}^2\nu (M^3_{rh,c}). \end{aligned}$$
Proof
When blowing up a submanifold
F
of a manifold with corners
W
, blow-up introduces a factor of
\(\rho ^{\dim (W)-\dim (F)-1}\)
, equivalently
\(\rho ^{\tiny {\text{ codim }}(F)-1}\)
, with
\(\rho \)
the defining function for the new (blown-up) face (see Proposition C.5 of [
1
]). We repeatedly apply this.
Footnote
7
For
\(M^2_{rh}\)
,
\(\dim (W)=5\)
. The blow-up to produce ff blows up a finite collection of points, so the codimension is 5 and we acquire a
\(\rho _{\text {ff}}^4\)
. The blow-up to produce sf, on the other hand, requires
\(t'=0\)
,
\(z=z'\in E\)
, so the codimension is 4 and we acquire a
\(\rho ^3\)
. The blow-up to produce hvff has codimension 4, and the blow-ups to produce hvlf and hvrf have codimension 2. Putting this all together yields the result.
A similar analysis works for
\(M^3_{rh,c}\)
, being careful about repeated blow-ups. For example, blowing up
\({\mathcal {O}}\)
introduces a factor of
\(\rho _{{\mathcal {O}}}\)
at first. However, when blowing up a submanifold of
\({\mathcal {O}}\)
,
\(\rho _{{\mathcal {O}}}\)
itself continues to lift. For example, when creating
\(F_{\mathcal {O}VVV}\)
,
\(\rho _{{\mathcal {O}}}\)
lifts to
\(\rho _{{\mathcal {O}}}\rho _{\mathcal {O}VVV}\)
.
\(\square \)
Another important observation is that rather than
\(t'\)
and
\(t''\)
, we are treating their square roots as the boundary defining functions, so canonical densities have
\(dT'\)
and
\(dT'\)
. For example,
$$\begin{aligned} \nu (\Omega \times \Omega \times [0,1))=dT dz dz'', \end{aligned}$$
and recalling that
\(dt=2TdT\)
,
$$\begin{aligned} K_{A\circ B}dt dz dz''=2T K_{A\circ B}\nu (\Omega \times \Omega \times [0,1)). \end{aligned}$$
Similarly,
$$\begin{aligned}&K_A(t',z,z')K_B(t'',z',z'')dt' dt'' dz dz' dz'' \\  &\quad = 4T'T''K_A(t',z,z')K_B(t'',z',z'')\nu (\Omega \times \Omega \times \Omega \times [0,1)^2). \end{aligned}$$
3.8
Composition theorem
To define various classes of operator kernels we use notation which is similar but not identical to [
35
]. For an index family,
$$\begin{aligned} {\mathcal {F}}=(F_{\text {ff}_j}, F_{\text {sf}_j}, F_{\text {hvff}_{jk}}, F_{\text {hvrf}_j}, F_{\text {hvlf}_j}, F_{j0},F_{0j}, F_{\text {td}}), \end{aligned}$$
define
\({\mathcal {A}}^{{\mathcal {F}}}_{h}(M^2_h)\)
to be the space of functions on
\(M_h^2\)
which are pc with index sets given at the respective faces by
\({\mathcal {F}}\)
and which also vanish to infinite order at tf. We also define
\(\Psi _h ^{{\mathcal {F}}}\)
as the set of pseudodifferential operators whose Scheartz kernels, as functions on
\(M_h^2\)
, are elements of
\({\mathcal {A}}^{{\mathcal {F}}}_{h}(M^2_h)\)
.
We may also use the notation
$$\begin{aligned} {\mathcal {A}}^{\alpha _{\text {ff}_j}, \alpha _{\text {sf}_j}, \alpha _{\text {hvff}_{jk}}, \alpha _{\text {hvrf}_j}, \alpha _{\text {hvlf}_j}, \alpha _{j0}, \alpha _{0j}, \alpha _{\text {td}}} _{h} \end{aligned}$$
to indicate functions on
\(M_h^2\)
which are elements of
\({\mathcal {A}}_h^{{\mathcal {F}}}\)
for some index family
\({\mathcal {F}}\)
whose index set at each face is bounded below by the corresponding
\(\alpha \)
. In other words these are functions on
\(M_h^2\)
which are pc and which have leading order at each face no worse than the corresponding
\(\alpha \)
(and which furthermore do not have terms of the form
\(x^{\alpha }(\log x)^p\)
for
\(p\ge 1\)
). We also use
\(\Psi ^{\alpha _{\text {ff}_j}, \alpha _{\text {sf}_j}, \alpha _{\text {hvff}_{jk}}, \alpha _{\text {hvrf}_j}, \alpha _{\text {hvlf}_j}, \alpha _{j0}, \alpha _{0j}, \alpha _{\text {td}}}\)
in the analogous way.
Theorem 3.16
Suppose that
A
is an operator whose Schwartz kernel
\(K_A \in {\mathcal {A}}^{{\mathcal {F}}_A} _h\)
with index family
$$\begin{aligned} {\mathcal {F}}_A = (A_{\text {ff}_j}, A_{\text {sf}_j}, A_{\text {hvff}_{jk}}, A_{\text {hvrf}_j}, A_{\text {hvlf}_j}, A_{0j}, A_{j0}, A_{\text {td}}). \end{aligned}$$
Suppose that
B
is an operator whose Schwartz kernel
\(K_B \in {\mathcal {A}}^{{\mathcal {F}}_B} _h\)
with index family
$$\begin{aligned} {\mathcal {F}}_B = (B_{\text {ff}_j}, B_{\text {sf}_j}, B_{\text {hvff}_{jk}}, B_{\text {hvrf}_j}, B_{\text {hvlf}_j}, B_{0j}, B_{j0}, B_{\text {td}} = \infty ). \end{aligned}$$
Suppose, finally, that
$$\begin{aligned} A_{0j}+B_{j0}>-1,\ A_{\text {hvlf}_j}+B_{\text {hvrf}_j}>-2, \text{ and } A_{\text {td}}>-4. \end{aligned}$$
(3.10)
Then the Schwartz kernel of the composition
\(A \circ B\)
is an element of
\({\mathcal {A}}^{{\mathcal {F}}} _h\)
, where
\({\mathcal {F}}\)
has index sets
$$\begin{aligned} \begin{aligned}&A_{\text {ff}_j}+B_{\text {ff}_j}+4 \text { at } \text {ff}_j, \\&A_{\text {sf}_j}+B_{\text {sf}_j}+4 \text { at } \text {sf}_j, \\&({\overline{\cup }}_k(A_{\text {hvff}_{jk}}+B_{\text {hvff}_{kl}}+2)){\overline{\cup }}(A_{\text {hvrf}_j}+B_{\text {hvlf}_j}) \text { at } \text {hvff}_{jl}, \\&({\overline{\cup }}_k(A_{\text {hvff}_{jk}}+B_{\text {hvrf}_k}+2)){\overline{\cup }}(A_{\text {hvrf}_j}){\overline{\cup }}(A_{\text {ff}_j}+B_{\text {hvrf}_j}+4) \text { at } \text {hvrf}_j, \\&({\overline{\cup }}_k(A_{\text {hvlf}_k}+B_{\text {hvff}_{kl}}+2)){\overline{\cup }}(B_{\text {hvlf}_l}){\overline{\cup }}(A_{\text {hvlf}_l}+B_{\text {ff}_l}+4) \text { at } \text {hvlf}_l, \\&A_{j0}{\overline{\cup }}(A_{\textsf {j}}+B_{j0}+4) \text { at } E_{j0}, \\&B_{0j}{\overline{\cup }}(A_{0j}+B_{\textsf {j}}+4) \text { at } E_{0j}, \\&\infty \text { at } \text {td}. \end{aligned} \end{aligned}$$
Proof
By the pullback theorem (see [
39
, Theorem 3] or [
19
, Theorem 2.2]),
\(\Pi _L^*K_A\)
is polyhomogeneous on
\(M^3_{rh}\)
with index sets:
$$\begin{aligned} \begin{aligned}&A_{\text {td}} \text{ at } F_{TRD} \text{ and } F_{\mathcal {O}D};\ A_{\text {ff}_j} \text{ at } F_{{\mathcal {O}} V_jV_jV_j}, F_{RV_jV_j0}, \text{ and } F_{\mathcal {O}V_jV_j0};\\&A_{\text {sf}_j} \text{ at } F_{{\mathcal {O}} E_jE_jE_j},F_{RE_jE_j0}, \text{ and } F_{\mathcal {O}E_jE_j0};\ A_{\text {hvff}_{jk}} \text{ at } F_{V_jV_kV_l} \text{ and } F_{V_jV_k0};\\&A_{\text {hvrf}_j} \text{ at } F_{V_j0V_l} \text{ and } F_{V_j00}; A_{\text {hvlf}_k} \text{ at } F_{0V_kV_l}, F_{0V_k0}, \text{ and } F_{L0V_kV_k};\\&A_{j0} \text{ at } F_{j00}; A_{0j} \text{ at } F_{0j0} \text{ and } F_{L0E_jE_j};0 \text{ at } F_{TL}, F_{00l}, \text{ and } F_{00V_l}; \text{ and } \text{ finally }\\&\infty \text{ at } F_{TR}, F_{{\mathcal {O}}},F_{\mathcal {O}V_j0V_j}, F_{\mathcal {O}E_j0E_j}, F_{{\mathcal {O}}0V_jV_j}, F_{{\mathcal {O}}0E_jE_j}. \end{aligned} \end{aligned}$$
Note in particular that at the four hypersurfaces in the domain mapped to intersections of two hypersurfaces in the range, the pullback index set is the sum of the index sets at the two range hypersurfaces. At each of these the sum ends up being infinity. Similarly,
\(\Pi _R^*K_B\)
is polyhomogeneous on
\(M^3_{rh}\)
with index sets
$$\begin{aligned} \begin{aligned}&B_{\text {ff}_j} \text{ at } F_{\mathcal {O}V_jV_jV_j}, F_{L0V_jV_j}, \text{ and } F_{{\mathcal {O}}0V_jV_j}; \\&B_{\text {sf}_j} \text{ at } F_{\mathcal {O}E_jE_jE_j},F_{L0E_jE_j}, \text{ and } F_{{\mathcal {O}}0E_jE_j};\\&B_{\text {hvff}_{kl}} \text{ at } F_{V_jV_kV_l} \text{ and } F_{0V_kV_l}; \, B_{\text {hvlf}_l} \text{ at } F_{V_j0V_l} \text{ and } F_{00V_l}; \\&B_{\text {hvrf}_k} \text{ at } F_{V_jV_k0}, F_{0V_k0}, \text{ and } F_{RV_kV_k0}; \, B_{0j} \text{ at } F_{00j}; B_{j0} \text{ at } F_{0j0} \text{ and } F_{RE_jE_j0}; \\&0 \text{ at } F_{TR}, F_{j00}, F_{V_j00}, \text{ and } F_{TRD}; \text{ and } \text{ finally } \\&\infty \text{ at } F_{TL}, F_{{\mathcal {O}}}, F_{\mathcal {O}D}, F_{\mathcal {O}V_jV_j0}, F_{\mathcal {O}V_j0V_j}, F_{\mathcal {O}E_jE_j0} \text{ and } F_{\mathcal {O}E_j0E_j}. \end{aligned} \end{aligned}$$
It is also easy enough to compute the pullbacks of
\(T'\)
and
\(T''\)
; they each have order 1 at each face in the lift of
\(T'=0\)
and
\(T''=0\)
respectively. Therefore the product
\(4T'T''(\Pi _L^*K_A)(\Pi _R^*K_B)\)
is polyhomogeneous on
\(M^3_{rh}\)
with index sets
$$\begin{aligned} \begin{aligned}&A_{j0}\text { at }F_{j00}; A_{0j}+B_{j0}\text { at }F_{0j0}; B_{0j}\text { at }F_{00j}; \\&A_{\text {ff}_j}+B_{\text {ff}_j}+2 \text{ at } F_{\mathcal {O}V_jV_jV_j}; A_{\text {sf}_j}+B_{\text {sf}_j}+2 \text{ at } F_{\mathcal {O}E_jE_jE_j}; \\&A_{\text {hvff}_{jk}}+B_{\text {hvff}_{kl}} \text{ at } F_{V_jV_kV_l}; A_{\text {hvff}_{jk}}+B_{\text {hvrf}_k} \text{ at } F_{V_jV_k0}; \\&A_{\text {hvrf}_j}+B_{\text {hvlf}_l} \text{ at } F_{V_j0V_l}; A_{\text {hvlf}_k}+B_{\text {hvff}_{kl}} \text{ at } F_{0V_kV_l}; \\&A_{\text {hvrf}_j} \text{ at } F_{V_j00}; A_{\text {hvlf}_k}+B_{\text {hvrf}_k} \text{ at } F_{0V_k0}; B_{\text {hvlf}_l} \text{ at } F_{00V_l}; \\&A_{\text {ff}_j}+B_{\text {hvrf}_j}+1 \text{ at } F_{RV_jV_j0}; A_{\text {sf}_j}+B_{j0}+1 \text{ at } F_{RE_jE_j0}; \\&A_{\text {hvlf}_j}+B_{\text {ff}_j}+1 \text{ at } F_{L0V_jV_j}; A_{0j}+B_{\text {sf}_j}+1 \text{ at } F_{L0E_jE_j}; \\&A_{\text {td}}+1 \text{ at } F_{TRD}; \\&\infty \text{ at } F_{TL}, F_{TR}, F_{{\mathcal {O}}}, F_{{\mathcal {O}} D}, F_{\mathcal {O}V_jV_j0}, F_{\mathcal {O}E_jE_j0}, F_{\mathcal {O}V_j0V_j}, \\&F_{\mathcal {O}E_j0E_j}, F_{{\mathcal {O}}0V_jV_j}, \text{ and } F_{{\mathcal {O}}0E_jE_j}. \end{aligned} \end{aligned}$$
(3.11)
Now we make the observation that on the front faces of each of the five blow-ups needed to create
\(M^3_{rh}\)
from
\(M^3_{rh,c}\)
, the product
\((\Pi _L^*K_A)(\Pi _R^*K_B)\)
vanishes to infinite order. Applying Proposition
3.8
five times, we see that
\(4T'T''(\Pi _L^*K_A)(\Pi _R^*K_B)\)
is in fact polyhomogeneous conormal on
\(M^3_{rh,c}\)
with index sets the same as in (
3.11
), with the exception of deleting the five extra faces.
We would like to use the pushforward theorem, but first we must view
\(4T'T''(\Pi _L^*K_A) (\Pi _R^*K_B)\)
, currently a section of
\(\nu (\Omega \times \Omega \times \Omega \times [0,1)^2)\)
, as a section of
\(\nu (M^3_{rh,c})\)
. By Proposition
3.15
, as a section of
\(\nu (M^3_{rh,c})\)
, its orders are:
$$\begin{aligned} \begin{aligned}&A_{j0}\text { at }F_{j00}; A_{0j}+B_{j0}\text { at }F_{0j0}; B_{0j}\text { at }F_{00j};\\&A_{\text {ff}_j}+B_{\text {ff}_j}+9 \text{ at } F_{\mathcal {O}V_jV_jV_j}; A_{\text {sf}_j}+B_{\text {sf}_j}+8 \text{ at } F_{\mathcal {O}E_jE_jE_j}; \\&A_{\text {hvff}_{jk}}+B_{\text {hvff}_{kl}}+5 \text{ at } F_{V_jV_kV_l}; A_{\text {hvff}_{jk}}+B_{\text {hvrf}_k}+3 \text{ at } F_{V_jV_k0}; \\&A_{\text {hvrf}_j}+B_{\text {hvlf}_l}+3 \text{ at } F_{V_j0V_l}; A_{\text {hvlf}_k}+B_{\text {hvff}_{kl}}+3 \text{ at } F_{0V_kV_l}; \\&A_{\text {hvrf}_j}+1 \text{ at } F_{V_j00}; A_{\text {hvlf}_k}+B_{\text {hvrf}_k}+1 \text{ at } F_{0V_k0}; \\&B_{\text {hvlf}_l}+1 \text{ at } F_{00V_l}; A_{\text {ff}_j}+B_{\text {hvrf}_j}+5 \text{ at } F_{RV_jV_j0}; \\&A_{\text {sf}_j}+B_{j0}+4 \text{ at } F_{RE_jE_j0}; A_{\text {hvlf}_j}+B_{\text {ff}_j}+5 \text{ at } F_{L0V_jV_j}; \\&A_{0j}+B_{\text {sf}_j}+4 \text{ at } F_{L0E_jE_j}; A_{\text {td}}+3 \text{ at } F_{TRD}; \\&\text{ and } \infty \text{ at } F_{TL}, F_{TR}, F_{{\mathcal {O}}}, F_{\mathcal {O}V_j0V_j}, \text{ and } F_{{\mathcal {O}}0E_jE_j}. \end{aligned} \end{aligned}$$
(3.12)
Now we apply the pushforward theorem and push forward by
\(\Pi _C\)
. There is a condition in the pushforward theorem, see [
19
], Theorem 2.3] or [
33
]: any face which is mapped to the interior must have index set greater than
\(-\,1\)
(or, equivalently, 0 as a b-density). This, however, is guaranteed by (
3.10
). By the pushforward theorem,
\((\Pi _C)_*((\Pi _L^*K_A)(\Pi _R^*K_B))\)
is polyhomogeneous on
\(M^2_{rh}\)
with index sets given as a section of
\(\nu (M^2_{rh})\)
by
$$\begin{aligned} \begin{aligned}&A_{\text {ff}_j}+B_{\text {ff}_j}+9 \text{ at } \text {ff}_j; \ A_{\text {sf}_j}+B_{\text {sf}_j}+8 \text{ at } \text {sf}_j;\ \infty \text{ at } \text {tf}; \\&({\overline{\cup }}_k(A_{\text {hvff}_{jk}}+B_{\text {hvff}_{kl}}+5)){\overline{\cup }}(A_{\text {hvrf}_j}+B_{\text {hvlf}_j}+3) \text{ at } \text {hvff}_{jl};\\&({\overline{\cup }}_k(A_{\text {hvff}_{jk}}+B_{\text {hvrf}_k}+3)){\overline{\cup }}(A_{\text {hvrf}_j}+1){\overline{\cup }}(A_{\text {ff}_j}+B_{\text {hvrf}_j}+5) \text{ at } \text {hvrf}_j;\\&({\overline{\cup }}_k(A_{\text {hvlf}_k}+B_{\text {hvff}_{kl}}+3)){\overline{\cup }}(B_{\text {hvlf}_l}+1){\overline{\cup }}(A_{\text {hvlf}_l}+B_{\text {ff}_l}+5) \text{ at } \text {hvlf}_l;\\&A_{j0}{\overline{\cup }}(A_{\text {sf}_j}+B_{j0}+4) \text{ at } E_{j0};\ B_{0j}{\overline{\cup }}(A_{0j}+B_{\text {sf}_j}+4) \text{ at } E_{0j}. \end{aligned} \end{aligned}$$
Finally, we use Proposition
3.15
to go back from sections of
\(\nu (M^2_{rh})\)
to sections of
\(\nu (\Omega \times \Omega \times [0,1))\)
, then divide by 2
T
to go back to
\(dt dz dz''\)
. The index sets of the composition are thus
$$\begin{aligned} \begin{aligned}&\text{ A}_{\text {ff}_j}+B_{\text {ff}_j}+4 \text{ at } \text {ff}_j;\ A_{\text {sf}_j}+B_{\text {sf}_j}+4 \text{ at } \text {sf}_j; \ \infty \text{ at } \text {tf} \text{ and } \text {td};\\&({\overline{\cup }}_k(A_{\text {hvff}_{jk}}+B_{\text {hvff}_{kl}}+2)){\overline{\cup }}(A_{\text {hvrf}_j}+B_{\text {hvlf}_j}) \text{ at } \text {hvff}_{jl};\\&({\overline{\cup }}_k(A_{\text {hvff}_{jk}}+B_{\text {hvrf}_k}+2)){\overline{\cup }}(A_{\text {hvrf}_j}){\overline{\cup }}(A_{\text {ff}_j}+B_{\text {hvrf}_j}+4) \text{ at } \text {hvrf}_j;\\&({\overline{\cup }}_k(A_{\text {hvlf}_k}+B_{\text {hvff}_{kl}}+2)){\overline{\cup }}(B_{\text {hvlf}_l}){\overline{\cup }}(A_{\text {hvlf}_l}+B_{\text {ff}_l}+4) \text{ at } \text {hvlf}_l;\\&A_{j0}{\overline{\cup }}(A_{\text {sf}_j}+B_{j0}+4) \text{ at } E_{j0};\ B_{0j}{\overline{\cup }}(A_{0j}+B_{\text {sf}_j}+4) \text{ at } E_{0j}. \end{aligned} \end{aligned}$$
\(\square \)
Remark 3.17
It is instructive to compare our composition formula to that of Mazzeo–Vertman [
35
, Theorem 5.3]. Indeed, the two settings coincide in the special case of a surface with boundary and no vertices. Our faces ff, hvff, hvrf, and hvlf do not exist in that case. Moreover, in the notation of Mazzeo–Vertman,
\(\ell =A_{\text {sf}_j}+4\)
and
\(\ell '=B_{\text {sf}_j}+4\)
(see Definition 3.1, and note that the dimension of the base
\(b=1\)
), so our calculations are in agreement.
4
The heat kernel on a surface with boundary
In this section we will build the heat kernel for a surface with smooth boundary in the absence of conical singularities. This construction has been performed in the Neumann and Dirichlet settings by Grieser [
16
]; the Robin case we give here is new. The work we do here shall be used in the later construction of the heat kernel for a surface with corners. We follow the usual geometric microlocal strategy. Namely, we specify models at various boundary hypersurfaces to which
\(\{T=0\}\)
lifts in the heat space, then look for a pc function which has those models as its leading order behavior at each boundary hypersurface. In order for this method to work the models must be compatible with each other at the surfaces where they intersect, in the sense that their restrictions to the intersection must be identical, as otherwise no pc function with the specified leading order behavior can exist.
This setting is a special case of the setting of surfaces with corners, and as such the double heat space will be a special case of the space
\(M_h^2\)
constructed in the previous section. Many of the blow-ups are now trivial; in this setting, we need just two blowups, the first of which is
$$\begin{aligned} {[}\Omega \times \Omega \times [0, \infty ); \{ (z, z, 0): z \in \partial \Omega \}]. \end{aligned}$$
The new boundary face is sf, and in the absence of corners, the resulting space is the reduced heat space
\(M^2_{rh}\)
. To complete the construction, we perform one more blowup,
$$\begin{aligned}{[}M^2 _{rh}; \{ (z, z, 0): z \in \Omega \}] = M^2 _h. \end{aligned}$$
The resulting blown-up face is td. Thus, the heat space for a surface with smooth boundary has boundary faces sf, td, tf, as well as the two side faces
\(E_{10}\)
and
\(E_{01}\)
, which are the lifts of
\(\partial \Omega \times \Omega \times [0, \infty )\)
and
\(\Omega \times \partial \Omega \times [0, \infty )\)
, respectively. The boundary hypersurfaces which comprise the lift of
\(\{T=0\}\)
to
\(M^2 _h\)
are therefore sf, td, and tf (Fig.
5
).
Fig. 5
Full size image
The model heat kernels (abbreviated hk) and the boundary faces which intersect are given above. Note that the heat kernel for the half plane is taken with the corresponding boundary condition: Dirichlet, Neumann, or Robin
4.1
Heat kernels on the half-plane
Let (
x
,
y
) be the usual Cartesian coordinates on
\({\mathbb {R}}^2\)
, and consider the half-space
$$\begin{aligned} {\mathbb {R}}^2_{+}:=\{(x,y)\in {\mathbb {R}}^2:y\ge 0\}. \end{aligned}$$
(4.1)
The heat kernel on all of
\({\mathbb {R}}^2\)
is
$$\begin{aligned} H_{{\mathbb {R}}^2}(t,x,y,x',y'):=\frac{1}{4\pi t}\exp \left[ -\frac{(x-x')^2+(y-y')^2}{4t} \right] . \end{aligned}$$
(4.2)
4.1.1
The Neumann and Dirichlet heat kernels
By the method of images, the Neumann heat kernel on
\({\mathbb {R}}^2_+\)
is
$$\begin{aligned} \begin{aligned}&H_{{\mathbb {R}}^2}(t,x,y,x',y')+H_{{\mathbb {R}}^2}(t,x,y,x',-y') \\&\quad =\frac{1}{4\pi t}\exp \left[ -\frac{(x-x')^2}{4t}\right] \left( \exp \left[ -\frac{(y-y')^2}{4t}\right] +\exp \left[ \frac{-(y+y')^2}{4t}\right] \right) . \end{aligned} \end{aligned}$$
(4.3)
The first term above is known as the direct term, whereas the second term is known as the reflected term or image term. We examine the behavior of this Neumann heat kernel on the double heat space
\(M_h^2\)
, albeit in the simpler setting where there are no corners. Although we will not prove that this heat kernel is pc on the double space in this section (it is a consequence of later work), we will use our examination to determine the appropriate pc models in the next section.
To examine the model heat kernels for the half-space, let us examine the blow-ups in local coordinates. To get
\(M_h^2\)
, we first blow up
$$\begin{aligned}\{T=y=y'=0; x=x'\},\end{aligned}$$
then blow up the lift of the diagonal at
\(T=0\)
:
$$\begin{aligned}\{T=0; y=y'; x=x'\}.\end{aligned}$$
After the first blow-up, coordinates near the interior of the new face sf, away from the intersection with
\(\{T=0\}\)
(where the second blow-up takes place), are given by
$$\begin{aligned} X:=\frac{x-x'}{T};\ \xi :=\frac{y}{T};\ \xi '=\frac{y'}{T};\ x'; \text{ and } T. \end{aligned}$$
(4.4)
In these coordinates, the expression (
4.3
) becomes
$$\begin{aligned} T^{-2}\frac{1}{4\pi }\exp \left[ -\frac{1}{4}X^2 \right] \left( \exp \left[ -\frac{1}{4}(\xi -\xi ')^2\right] +\exp \left[ -\frac{1}{4}(\xi +\xi ')^2\right] \right) . \end{aligned}$$
(4.5)
To encode this, we write
$$\begin{aligned} {\mathcal {H}}_{-2,\text {sf},N} := \frac{1}{4\pi }\exp \left[ -\frac{1}{4}X^2\right] \left( \exp \left[ -\frac{1}{4}(\xi -\xi ')^2\right] +\exp \left[ -\frac{1}{4}(\xi +\xi ')^2\right] \right) \end{aligned}$$
(4.6)
and say that
\({\mathcal {H}}_{-2,\text {sf},N}\)
, which we view as a function on sf, is the leading order model of the Neumann heat kernel at the face sf, appearing at order
\(T^{-2}\)
. What this means is that the Neumann heat kernel, in a coordinate patch near the interior of sf, is given at least to leading order (in this case, exactly) by
$$\begin{aligned}T^{-2}{\mathcal {H}}_{-2,\text {sf},N}.\end{aligned}$$
After the second blow-up, coordinates near the interior of the new face td, away from
\(y=0\)
, are given by
$$\begin{aligned} X=\frac{x-x'}{T};\ Y:=\frac{y-y'}{T};\ x';\ y'; \text{ and } T. \end{aligned}$$
(4.7)
Consider (
4.3
) in these coordinates. Away from
\(y=0\)
the image term is
\(O(T^{\infty })\)
, and so (
4.3
) becomes
$$\begin{aligned} T^{-2}\frac{1}{4\pi }\exp \left[ -\frac{1}{4}X^2\right] \exp \left[ -\frac{1}{4}Y^2\right] + O(T^{\infty }). \end{aligned}$$
(4.8)
So we may similarly define
$$\begin{aligned} {\mathcal {H}}_{-2,\text {td}}:=\frac{1}{4\pi }\exp \left[ -\frac{1}{4}X^2\right] \exp \left[ -\frac{1}{4}Y^2\right] , \end{aligned}$$
(4.9)
where we have omitted the
N
since the model will be the same for all boundary conditions. The leading order of the Neumann heat kernel at td is given by
$$\begin{aligned} T^{-2}{\mathcal {H}}_{-2,\text {td}}. \end{aligned}$$
To check for compatibility, we show that our model for the Neumann heat kernel on
\({\mathbb {R}}^2_{+}\)
is compatible with the model we have defined at td. Specifically, we want
$$\begin{aligned} {\mathcal {H}}_{-2,\text {sf},N}|_{\text {sf}\cap \text {td}}={\mathcal {H}}_{-2,\text {td}}|_{\text {sf}\cap \text {td}}. \end{aligned}$$
The coordinate patches we have described to this point are not necessarily valid systems of coordinates near the intersection sf
\(\cap \)
td. However, it is easy enough to show that
$$\begin{aligned} \eta :=\frac{T}{y'}=\frac{1}{\xi '};\ X;\ Y;\ x';\ y' \end{aligned}$$
(4.10)
are valid coordinates in a neighborhood of this intersection, away from tf. In this new coordinate patch,
$$\begin{aligned} y=YT+y', \text{ so } \xi =Y+\frac{1}{\eta }, \text{ so } \xi +\xi '=Y+\frac{2}{\eta }, \end{aligned}$$
and we get
$$\begin{aligned} {\mathcal {H}}_{-2,\text {sf},N}= &   \frac{1}{4\pi }\exp \left[ -\frac{1}{4}X^2\right] \left( \exp \left[ -\frac{1}{4}Y^2\right] +\exp \left[ -\frac{1}{4}(Y+\frac{2}{\eta })^2\right] \right) ;\\ {\mathcal {H}}_{-2,\text {td}}= &   \frac{1}{4\pi }\exp \left[ -\frac{1}{4}X^2\right] \exp \left[ -\frac{1}{4}Y^2\right] . \end{aligned}$$
Restricting to sf
\(\cap \)
td means letting
\(\eta \rightarrow 0\)
in the first term, which corresponds to approaching sf
\(\cap \)
td from the interior of sf, and letting
\(y' \rightarrow 0\)
in the second term, which corresponds to approaching sf
\(\cap \)
td from the interior of td. We see immediately that the second exponential in
\({\mathcal {H}}_{-2,\text {sf},N}\)
tends to zero when
\(\eta \)
tends to zero, and
\(H_{-2,\text {td}}\)
is independent of
\(y'\)
, so the restrictions are well-defined and they match. This proves compatibility of
\({\mathcal {H}}_{-2,\text {sf},N}\)
and
\({\mathcal {H}}_{-2,\text {td}}\)
.
An identical analysis works for the Dirichlet heat kernel; the only difference is the sign of the image term. So we write
$$\begin{aligned}&{\mathcal {H}}_{-2,\text {sf},D} \nonumber \\&\quad :=\frac{1}{4\pi }\exp \left[ -\frac{1}{4}X^2\right] \left( \exp \left[ -\frac{1}{4}(\xi -\xi ')^2\right] -\exp \left[ -\frac{1}{4}(\xi +\xi ')^2\right] \right) , \end{aligned}$$
(4.11)
and just as before,
\({\mathcal {H}}_{-2,\text {sf},D}\)
is compatible with
\({\mathcal {H}}_{-2,\text {td}}\)
.
Note that the models
\({\mathcal {H}}_{-2,\text {sf},N}\)
and
\({\mathcal {H}}_{-2,\text {sf},D}\)
themselves satisfy Neumann or Dirichlet boundary conditions, respectively. In particular, looking at the expansion of
\({\mathcal {H}}_{-2,\text {sf},N}\)
in
\(\xi \)
at
\(\{\xi =0\}\)
(i.e.
\(y=0\)
), we observe that there is a complete Taylor expansion with no first-order term. If we take
\(\frac{\partial }{\partial \xi }{\mathcal {H}}_{-2,\text {sf},N}\)
and restrict to
\(\{\xi =0\}\)
, we get zero. Similarly,
\({\mathcal {H}}_{-2,\text {sf},D}\)
has a Taylor expansion with no zeroth-order term; that is, its restriction to
\(\{\xi =0\}\)
is zero.
It is also useful to consider the heat operator, lifted from the left (that is, acting in the unprimed coordinates):
$$\begin{aligned} {\mathcal {L}}:=\partial _t-\partial _{xx}-\partial _{yy}=\frac{1}{2T}\partial _T-\partial _{xx}-\partial _{yy}. \end{aligned}$$
This operator lifts under the blow-down maps to an operator on the double heat space, which we also call
\({\mathcal {L}}\)
, abusing notation. The lift of the operator
\(t{\mathcal {L}}=T^2{\mathcal {L}}\)
is more useful, because
\(T^2 \mathcal {L}\)
lifts to the double heat space to be a b-operator, except in a neighborhood of
\(E_{10}\)
, where it is merely smooth. In particular
\(\rho _{E_{10}}^2T^2\mathcal {L}\)
is a b-operator. Therefore
\(T^2\mathcal {L}\)
(1) preserves polyhomogeneity and (2) preserves infinite order vanishing at tf. These two facts shall be useful.
The operator
\(T^2\mathcal {L}\)
can be analyzed in the coordinate systems (
4.4
), (
4.7
), and (
4.10
). In the coordinates (
4.4
) we have by a chain rule calculation:
$$\begin{aligned} T^2{\mathcal {L}}=\frac{1}{2}T\partial _{T}-\partial _{XX}-\frac{1}{2}X\partial _X-\partial _{\xi \xi }-\frac{1}{2}\xi \partial _{\xi } - \frac{1}{2} \xi ' \partial _{\xi '}. \end{aligned}$$
(4.12)
In the coordinates (
4.7
), we have
$$\begin{aligned} T^2{\mathcal {L}}=\frac{1}{2}T\partial _{T}-\partial _{XX}-\frac{1}{2}X\partial _X-\partial _{YY}-\frac{1}{2}Y\partial _Y. \end{aligned}$$
(4.13)
Finally, in the coordinates (
4.10
), we get
$$\begin{aligned} T^2{\mathcal {L}}=\frac{1}{2}\eta \partial _{\eta }-\partial _{XX}-\frac{1}{2}X\partial _X-\partial _{YY}-\frac{1}{2}Y\partial _Y. \end{aligned}$$
(4.14)
The point of all of this is to show that our leading order models solve model problems at their designated boundary hypersurfaces. Specifically, since the heat kernel solves the heat equation, we must have
$$\begin{aligned} \left. \beta ^* (T^2 \mathcal {L}) \beta ^*(T^{-2} {\mathcal {H}}_{-2, \text {td}}) \right| _{\text {td}}= &   \left. \beta ^* (T^2 \mathcal {L}) \beta ^*(T^{-2} {\mathcal {H}}_{-2, \text {sf}, N}) \right| _{\text {sf}} \nonumber \\= &   \left. \beta ^* (T^2 \mathcal {L}) \beta ^*(T^{-2} {\mathcal {H}}_{-2, \text {sf}, D}) \right| _{\text {sf}} = 0. \end{aligned}$$
(4.15)
Observe additionally that when lifting to the double heat space, in the coordinate systems near these boundary faces, the three factors of
\({\mathcal {H}}\)
are independent of the
T
coordinate. Consequently,
$$\begin{aligned}\frac{1}{2} T \partial _T (T^{-2} {\mathcal {H}}) = - T^{-2} {\mathcal {H}},\end{aligned}$$
and so
$$\begin{aligned} (T^2{\mathcal {L}}-\operatorname {Id})|_{\text {sf}}{\mathcal {H}}_{-2,\text {sf},N}= &   (T^2{\mathcal {L}}-\operatorname {Id})|_{\text {sf}}{\mathcal {H}}_{-2,\text {sf},D} \nonumber \\= &   (T^2{\mathcal {L}}-\operatorname {Id})|_{\text {td}}{\mathcal {H}}_{-2,\text {td}}=0. \end{aligned}$$
(4.16)
Remark 4.1
The Neumann and Dirichlet heat kernels for a half-space are indeed pc on
\(M_h^2\)
. This can be seen directly in local coordinates, and alternately follows from a reflection argument similar to the proof of Lemma
5.1
.
4.1.2
The Robin heat kernel
Now we consider the heat kernel on
\({\mathbb {R}}^2_{+}\)
with a Robin boundary condition, namely
$$\begin{aligned} \left. \frac{\partial u(x,y)}{\partial y}\right| _{y=0}=\kappa u(x,0), \text{ for } \text{ some } \text{ constant } \kappa >0. \end{aligned}$$
(4.17)
We recall that this condition is for the
inward
pointing normal derivative. The explicit expression for this heat kernel is known [
5
]. It is
$$\begin{aligned}H_{{\mathbb {R}}_+^2,\text {Robin}}:=H_{{\mathbb {R}}_{+}^2,\text {Neumann}}+H_{corr},\end{aligned}$$
where
$$\begin{aligned}H_{corr}(t,x,y,x',y'):=-\frac{\kappa e^{\kappa (y+y')}e^{\kappa ^2 t}}{\sqrt{4\pi t}}\exp \left[ -\frac{1}{4t}(x-x')^2\right] \text{ erfc }\left( \frac{y+y'}{\sqrt{4t}}+\kappa \sqrt{t}\right) .\end{aligned}$$
Recall that the complementary error function is smooth in
z
, bounded by 1 for
\(z\ge 0\)
, and decaying to infinite order as
\(z\rightarrow \infty \)
:
$$\begin{aligned}\operatorname {erfc}(z) = 1 - \operatorname {erf}(z) = \frac{2}{\sqrt{\pi }} \int _z ^\infty e^{-s^2}ds.\end{aligned}$$
Let us examine the behavior of
\(H_{corr}\)
in the coordinate systems (
4.4
) and (
4.10
). In (
4.4
):
$$\begin{aligned}H_{corr}=-T^{-1}\frac{\kappa e^{\kappa T(\xi +\xi ')}e^{\kappa ^2 T^2}}{2\sqrt{\pi }}\exp \left[ -\frac{1}{4}X^2\right] \text{ erfc }\left( \frac{1}{2}(\xi +\xi ')+\kappa T\right) .\end{aligned}$$
The restriction of
\(TH_{corr}\)
to sf, that is to
\(T=0\)
, is well-defined. Based on our previous notation, we give it a name:
$$\begin{aligned} {\mathcal {H}}_{-1,\text {sf},R}:=-\frac{\kappa }{2\sqrt{\pi }}\exp \left[ -\frac{1}{4}X^2\right] \text{ erfc }\left( \frac{1}{2}(\xi +\xi ')\right) . \end{aligned}$$
(4.18)
On the other hand, in the coordinate system (
4.10
) that is valid near the intersection of sf and td, we have
$$\begin{aligned}H_{corr}=-T^{-1}\frac{\kappa e^{\kappa y'(\eta Y+2)}e^{\kappa ^2\eta ^2(y')^2}}{2\sqrt{\pi }}\exp \left[ -\frac{1}{4}X^2\right] \text{ erfc }\left( \frac{1}{2}Y+\frac{1}{\eta }+\kappa \eta y' \right) .\end{aligned}$$
We approach td
\(\cap \)
sf from the interior of sf by letting
\(\eta \rightarrow 0\)
. As this happens, the erfc function decays to infinite order due to the
\(1/\eta \)
term in its argument, and we see that
\(H_{corr}\)
vanishes to infinite order at td
\(\cap \)
sf. Thus
\({\mathcal {H}}_{-1,\text {sf},R}\)
vanishes to infinite order at td, and so adding
\(H_{corr}\)
to the Neumann heat kernel does not disrupt compatibility at td
\(\cap \)
sf.
The Robin correction term also solves a model problem at sf. The model problem in this case is slightly different, because
\({\mathcal {H}}\)
has a factor of
\(T^{-1}\)
rather than
\(T^{-2}\)
. Consequently,
$$\begin{aligned}\frac{1}{2} T \partial _T (T^{-1} {\mathcal {H}}) = - \frac{1}{2} T^{-1} {\mathcal {H}},\end{aligned}$$
so here our model problem is
$$\begin{aligned} \left. \left( t{\mathcal {L}}-\frac{1}{2}\operatorname {Id}\right) \right| _{\text {sf}}{\mathcal {H}}_{-1,\text {sf},R}=0. \end{aligned}$$
(4.19)
For the sake of completeness we include this calculation. First, we compute (dropping the subscripts for notational simplicity)
$$\begin{aligned}\partial _X {\mathcal {H}}= \frac{\kappa X}{4\sqrt{\pi }} e^{-X^2/4} \operatorname {erfc}\left( \frac{\xi + \xi '}{2} \right) \implies - \frac{X}{2} \partial _X {\mathcal {H}}= \frac{X^2}{4} {\mathcal {H}}.\end{aligned}$$
Similarly we compute
$$\begin{aligned}\partial _{XX} {\mathcal {H}}= \frac{\kappa }{4\sqrt{\pi }} e^{-X^2/4} \operatorname {erfc}\left( \frac{\xi + \xi '}{2} \right) - \frac{\kappa X^2}{8\sqrt{\pi }} e^{-X^2/4} \operatorname {erfc}\left( \frac{\xi + \xi '}{2} \right) ,\end{aligned}$$
thus
$$\begin{aligned}-\partial _{XX} {\mathcal {H}}= \frac{1}{2} {\mathcal {H}}- \frac{X^2}{4} {\mathcal {H}}, \quad - \frac{X}{2} \partial _X {\mathcal {H}}- \partial _{XX} {\mathcal {H}}= \frac{1}{2} {\mathcal {H}}.\end{aligned}$$
Noting that
\(\operatorname {erfc}'(z) = - e^{-z^2}\)
, we also compute
$$\begin{aligned}\partial _\xi {\mathcal {H}}= \frac{\kappa }{4 \sqrt{\pi }} e^{-X^2/4} e^{-(\xi +\xi ')^2/4}, \quad - \frac{\xi }{2} \partial _\xi {\mathcal {H}}= \frac{-\xi \kappa }{8\sqrt{\pi }} e^{-X^2/4} e^{-(\xi +\xi ')^2/4}.\end{aligned}$$
By the symmetry in
\(\xi \)
and
\(\xi '\)
, we also have
$$\begin{aligned}- \frac{\xi '}{2} \partial _{\xi '} {\mathcal {H}}= \frac{-\xi ' \kappa }{8\sqrt{\pi }} e^{-X^2/4} e^{-(\xi +\xi ')^2/4}.\end{aligned}$$
Finally, we compute
$$\begin{aligned}\partial _{\xi \xi } {\mathcal {H}}= - \frac{\kappa (\xi + \xi ')}{8 \sqrt{\pi }} e^{-X^2/4} e^{-(\xi +\xi ')^2/4}, \quad - \partial _{\xi \xi } {\mathcal {H}}= \frac{\kappa (\xi + \xi ')}{8 \sqrt{\pi }} e^{-X^2/4} e^{-(\xi +\xi ')^2/4}.\end{aligned}$$
In total, we therefore have
$$\begin{aligned} \begin{aligned} T^2\mathcal {L}{\mathcal {H}}&= \frac{1}{2} {\mathcal {H}}+ \frac{-\xi \kappa }{8\sqrt{\pi }} e^{-X^2/4} e^{-(\xi +\xi ')^2/4} + \frac{-\xi ' \kappa }{8\sqrt{\pi }} e^{-X^2/4} e^{-(\xi +\xi ')^2/4} \\&\quad + \frac{\kappa (\xi + \xi ')}{8 \sqrt{\pi }} e^{-X^2/4} e^{-(\xi +\xi ')^2/4}= \frac{1}{2} {\mathcal {H}}, \end{aligned} \end{aligned}$$
verifying (
4.19
).
The upshot of all of this is that the Robin heat kernel on a half-space may be seen as a correction of the Neumann heat kernel, where the correction is lower order in the sense that it appears in the asymptotic behavior half an order below the leading order in the asymptotic regime corresponding to sf, namely at
\(T^{-1}\)
rather than
\(T^{-2}\)
. The correction also vanishes to infinite order at the
\(T=0\)
diagonal in the interior, indicating that it has no effect on the interior heat asymptotics. So the Robin heat kernel on a half space has:
Leading order behavior at td of order
\(T^{-2}\)
given by
\({\mathcal {H}}_{-2,\text {td}}\)
, in particular the same as the Neumann and Dirichlet heat kernels;
Leading order behavior at sf of order
\(T^{-2}\)
given by
\({\mathcal {H}}_{-2,\text {sf},N}\)
, in particular the same as the Neumann heat kernel; and
Additional sub-leading order behavior at sf of order
\(T^{-1}\)
given by
\({\mathcal {H}}_{-1,\text {sf},R}\)
(and some subsequent terms at higher powers of
T
). However, there is no additional sub-leading order behavior at td.
4.2
Construction of the heat kernel on a surface with boundary
We are now poised to construct the Dirichlet, Neumann, and Robin heat kernels on a surface with boundary, prove they are pc on the double heat space, and identify their leading order terms in their pc expansion. Our construction is inspired by [
35
,
16
] and indeed has already been done in [
35
] for Dirichlet boundary conditions (which are the Friedrichs extension for a cone-edge structure with one-dimensional edge and zero-dimensional link). These references were both largely inspired and guided by [
40
].
We use the same double space
\(M_h^2\)
that we have been using, which in the boundary-only case for surfaces is the same as the double space of [
35
], with a one-dimensional edge and a zero-dimensional cone link. Note that the faces have the same names, with the exception of our
\(E_{10}\)
which corresponds to rf in [
35
] and our
\(E_{01}\)
which corresponds to lf. Our composition formula, Theorem
3.16
, agrees with that of [
35
] as well.
Throughout, we will use boundary normal coordinates (
x
,
y
) on our surface with boundary
\(\Omega \)
. In these coordinates, the boundary is defined by
\(y=0\)
. The Riemannian metric in these boundary normal coordinates near the boundary takes the form
$$\begin{aligned}g(x,y)dx^2+dy^2,\end{aligned}$$
with
\(g(0,y)=1\)
, and
g
(
x
,
y
) smooth in
x
and
y
. The Laplacian has the following expression:
$$\begin{aligned}\Delta :=-\partial _{xx}-\partial _{yy}+a_1(x,y)\partial _{xx}+a_2(x,y)\partial _x+a_3(x,y)\partial _y,\end{aligned}$$
where
\(a_1\)
,
\(a_2\)
, and
\(a_3\)
are smooth, with
\(a_1(x,0)=0\)
and
\(a_2(x,0)=0\)
. In the interior, we let
z
be a local coordinate patch on
M
; then let
\(Z=(z-z')/T\)
and use
\((T,Z,z')\)
near the interior of td.
4.2.1
The Dirichlet and Neumann heat kernels
Since the heat space here only has boundary faces td, sf, tf, and the side faces, for an index family
\({\mathcal {F}}=(F_{\text {td}},F_{\text {sf}},F_{E10},F_{E01})\)
, define
\({\mathcal {A}}^{{\mathcal {F}}}_{h}\)
to be the space of kernels in
\({\mathcal {A}}^{{\mathcal {F}}}_{h}(\Omega ^2_h)\)
, as functions of
\((T,z,z')\)
, which vanish to infinite order at tf. Similarly, we define
\(\Psi ^{a,b,c,d}\)
to be the set of operators whose kernels are in
\({\mathcal {A}} ^{{\mathcal {F}}} _h\)
for some index family
\({\mathcal {F}}\)
which has leading orders
a
,
b
,
c
,
d
, at the corresponding faces.
Let us begin with the Neumann heat kernel. We follow [
35
]. We construct first a parametrix:
Proposition 4.2
There exists an element of
\(\Psi ^{-2,-2,0,0}\)
whose Schwartz kernel
\(H^{(1)}\)
satisfies Neumann boundary conditions in the left (unprimed) variable, whose limit as
\(T \rightarrow 0\)
is
\(\delta (z-z')\)
, and with
$$\begin{aligned} T^2\mathcal {L}H^{(1)}\in {\mathcal {A}}_h^{\infty ,-1,0,0}. \end{aligned}$$
Proof
The idea is to solve our model problems to infinite order at td and first order at sf, and to do so in a way that satisfies Neumann boundary conditions.
In the interior of td, we use the ansatz
$$\begin{aligned} H^{(1)}(T,Z,z')\sim \sum _{j=0}^{\infty }T^{-2+j}{\mathcal {H}}_{-2+j,\text {td}}(Z,z'). \end{aligned}$$
(4.20)
As in [
35
], we formally apply
\(t{\mathcal {L}}\)
to this expansion and set the result equal to zero. We can solve, inductively, for each coefficient function
\({\mathcal {H}}_{-2+j,td}\)
. For example, the equation for
\(j=0\)
is
$$\begin{aligned}-T^{-2}{\mathcal {H}}_{-2,\text {td}}-T^{-2}\left( \partial _{ZZ}+\frac{1}{2}Z\partial _Z \right) {\mathcal {H}}_{-2,\text {td}}=0.\end{aligned}$$
By direct computation (
4.16
) letting
\({\mathcal {H}}_{-2,\text {td}}\)
be the expression (
4.9
), namely
$$\begin{aligned}{\mathcal {H}}_{-2,\text {td}}(Z,z')=\frac{1}{4\pi }e^{-\frac{1}{4}Z^2},\end{aligned}$$
it solves this equation for
\(j=0\)
. For the higher order terms, we have to expand
\(T^2{\mathcal {L}}\)
in a power series in
T
, and more terms than just its restriction to td will be involved. Nevertheless, one may show inductively that there exist terms
\({\mathcal {H}}_{-2+j,\text {td}}(Z,z')\)
for all
j
that satisfy the formal ansatz. These terms each decay rapidly in
Z
. Since
\(\Omega \)
is a subset of a smooth manifold
M
and this construction is uniform over the interior of
M
, all terms
\({\mathcal {H}}_{-2+j,\text {td}}\)
are smooth up to sf
\(\cap \)
td. The result also satisfies the delta function initial condition. We omit the details, as they may be found in [
35
,
40
], as well as other references.
We verified in Sect.
4.1.1
that
\({\mathcal {H}}_{-2,\text {sf},N}\)
, defined in (
4.6
), is compatible with
\({\mathcal {H}}_{-2,\text {td}}\)
, so it is possible to choose an element of
\(\Psi ^{-2,-2,0,0}\)
whose kernel
\(H^{(1)}\)
simultaneously has leading order
\(T^{-2}{\mathcal {H}}_{-2,\text {sf},N}\)
at sf and has full expansion (
4.20
) at td, which vanishes to infinite order at tf, and which is smooth down to
\(E_{10}\)
and
\(E_{01}\)
. In fact it is also possible to choose
\(H^{(1)}\)
to satisfy Neumann boundary conditions. To see this, examine the expansion of
\({\mathcal {H}}_{-2,\text {sf},N}\)
as we approach
\(E_{10}\)
and
\(E_{01}\)
. Boundary defining functions for those faces are
\(\xi \)
and
\(\xi '\)
respectively. Indeed, (
4.6
) is smooth in
\(\xi \)
and
\(\xi '\)
, and it has no order 1 term at
\(\xi =0\)
or
\(\xi '=0\)
. We may thus choose
\(H^{(1)}\)
so that there is no term of order 1 in its expansions at
\(E_{10}\)
and
\(E_{01}\)
. This
\(H^{(1)}\)
satisfies Neumann boundary conditions, as claimed.
It remains to show that
$$\begin{aligned}T^2\mathcal {L}H^{(1)}\in {\mathcal {A}}_h^{\infty ,-1,0,0}.\end{aligned}$$
First we have to show that
\(T^2\mathcal {L}H^{(1)}\)
is polyhomogeneous. However, the operator
\(T^2 \mathcal {L}\)
lifts to one which is tangent to all boundary hypersurfaces except for
\(E_{10}\)
, and at
\(E_{10}\)
it may be written as
\(\rho _{E_{10}}^{-2}\)
times such an operator. Since such operators preserve polyhomogeneity and also preserve the infinite order vanishing at tf, the polyhomogeneity follows.
Now we compute the leading orders. Since
\(H^{(1)}\)
has the full expansion (
4.20
), which is annihilated by
\(t{\mathcal {L}}\)
, we see that
\(T^2\mathcal {L}H^{(1)}\)
has order
\(\infty \)
at td.
At sf, we claim that the model problem is the same as for a half-space. We have solved the model problem for a half-space to first order, so we get an improvement of one order, from
\(-2\)
to
\(-\,1\)
. To see this, compute
\(t{\mathcal {L}}\)
in the coordinates (
4.4
). We get
$$\begin{aligned} T^2{\mathcal {L}}= &   \frac{1}{2}T\partial _{T}-\partial _{XX}-\frac{1}{2}X\partial _X-\partial _{\xi \xi }-\frac{1}{2}\xi \partial _{\xi } - \frac{1}{2} \xi ' \partial _{\xi '}\nonumber \\  &   +a_1(XT+x',\xi T)\partial _{XX}+Ta_2(XT+x',\xi T)\partial _X+Ta_3(XT+x',\xi T)\partial _{\xi }.\nonumber \\ \end{aligned}$$
(4.21)
We apply
\(T^2{\mathcal {L}}\)
to our pc expansion at sf, namely
$$\begin{aligned} T^{-2}{\mathcal {H}}_{-2,\text {sf},N}+T^{-1}{\mathcal {H}}_{-1,\text {sf},N}+\dots . \end{aligned}$$
Since
\(T^2{\mathcal {L}}\)
is tangent to sf, the leading order of the result will be at worst
\(-2\)
. We claim it is actually
\(-\,1\)
. Indeed, as with the half-space, the application of the first six terms in (
4.21
) to
\(T^{-2}{\mathcal {H}}_{-2,\text {sf},N}\)
yields zero by (
4.16
). Moreover, applying
\(T^2{\mathcal {L}}\)
to only the terms with order
\(T^{-1}\)
or higher yields something of order at most
\(-\,1\)
. So the only possible term of order
\(-2\)
in the expansion of
\(t{\mathcal {L}} H^{(1)}\)
at sf comes from
$$\begin{aligned}&T^{-2}(a_1(XT+x',\xi T)\partial _{XX}+Ta_2(XT+x',\xi T)\partial _X \\&\quad +Ta_3(XT+x',\xi T)\partial _{\xi }){\mathcal {H}}_{-2,\text {sf},N}. \end{aligned}$$
However, the coefficients of the last two terms vanish at sf to first order in
T
, and since
\(a_1(x',0)=0\)
identically, so does the coefficient of the first term. In other words, the Laplacian in boundary normal coordinates is the same as that for a half-space up to terms which are lower order at sf. Thus
\(t{\mathcal {L}} H^{(1)}\)
has order
\(-\,1\)
at sf, as desired.
At
\(E_{01}\)
,
\(T^2{\mathcal {L}}\)
is tangent to
\(E_{01}\)
, so the leading order remains unchanged at 0. Finally, at
\(E_{10}\)
, at any point in the interior of
\(E_{10}\)
, we can use the coordinates
\((T,x,y,x',y')\)
, in which
y
is the defining function for
\(E_{10}\)
. So
\(H^{(1)}\)
has a smooth expansion in
y
down to
\(y=0\)
, with smooth dependence on all other variables. Applying
\(T^2{\mathcal {L}}\)
would usually turn a term of order
\(y^{\gamma }\)
into a term of order
\(y^{\gamma -2}\)
, but since
\(H^{(1)}\)
has a smooth expansion, it stays smooth. So the leading order of
\(T^2\mathcal {L}H^{(1)}\)
at
\(E_{10}\)
is 0, completing the proof.
\(\square \)
As in [
35
], this can be improved at
\(E_{10}\)
, the analogue of rf:
Proposition 4.3
There exists an element
\(H^{(2)}\in {\mathcal {A}}_h^{-2,-2,0,0}\)
which satisfies Neumann boundary conditions in the left variable, with
$$\begin{aligned} \lim _{t\rightarrow 0}H^{(2)}=\delta (z-z') \quad \text {and} \quad T^2\mathcal {L}H^{(2)}\in {\mathcal {A}}_h^{\infty ,-1,\infty ,0}. \end{aligned}$$
Proof
This is a standard argument, as in [
33
, p. 32] and [
35
]. We use the fact that
\(T^2{\mathcal {L}}\)
is elliptic in the
y
-direction to iteratively solve away the Taylor expansion of
\(T^2\mathcal {L}H^{(1)}\)
at
\(E_{10}\)
. To be concrete, let
\(A_2\)
be a pc kernel on
\(\Omega ^2_h\)
, smooth at
\(E_{10}\)
, whose expansion in any coordinate neighborhood
\((t,x,y,x',y')\)
is
$$\begin{aligned} \frac{1}{2}y^2\left( \mathcal {L}H^{(1)}\right) (t,x,0,x',y')+ O(y^3). \end{aligned}$$
Then
\((T^2{\mathcal {L}})A_2\)
is pc as well, and its leading order term at
\(E_{10}\)
is
$$\begin{aligned} \left( T^2\mathcal {L}H^{(1)}\right) (t,x,0,x',y'). \end{aligned}$$
Furthermore, using the coordinates (
4.4
) it is straightforward to see that
\(A_2\)
may be chosen to be pc down to sf and have the same order as
\(y^2\mathcal {L}H^{(1)}\)
at sf, namely
\(2-2=0\)
. So if we consider
\(H^{(1)}-A_2\)
, then
\((T^2{\mathcal {L}})(H^{(1)}-A_2)\)
is pc and vanishes to first order, rather than zeroth order, at
\(E_{10}\)
. Moreover
\(H^{(1)}-A_2\)
still satisfies Neumann boundary conditions.
This construction may now be iterated to produce
\(A_3\)
,
\(A_4\)
, et cetera, so that
\(H^{(1)}-\sum _{j=2}^{k}A_j\)
vanishes to order
\(k-1\)
at
\(E_{10}\)
. The
\(A_j\)
may be summed, and then setting
$$\begin{aligned}H^{(2)}=H^{(1)}-\sum _{j=2}^{\infty }A_j\end{aligned}$$
gives us the result. Note that since each
\(A_j\)
has order
\(-\,1\)
or better at sf (
\(\mathcal {L}H^{(1)}\)
has order
\(-3\)
there, but
\(y^2\)
has order 2), the leading order term of
\(H^{(2)}\)
at sf is still
\({\mathcal {H}}_{-2,\text {sf},N}\)
.
\(\square \)
Now, as in [
35
], let
\(P^{(2)}=(t{\mathcal {L}})H^{(2)}\)
. Then, as a kernel,
$$\begin{aligned} \mathcal {L}H^{(2)}=\frac{1}{T^2}P^{(2)}\in {\mathcal {A}}_h^{\infty ,-3,\infty ,0}. \end{aligned}$$
Kernels on
\(\Omega _h^2\)
may be naturally identified as convolution operators on
\([0,\infty )\times \Omega \)
, acting in the usual way. In this sense, as in [
40
, (7.67)] we have
$$\begin{aligned} \mathcal {L}H^{(2)}=\operatorname {Id}-\left( -\frac{1}{T^2}P^{(2)}\right) . \end{aligned}$$
(4.22)
To see this for any
\(g\in C^{\infty }([0,\infty )\times \Omega )\)
, we have
$$\begin{aligned}\mathcal {L}H^{(2)}*g(t)=(\partial _t+\Delta )\int _0^t[H^{(2)}g](s)(t-s)\, ds.\end{aligned}$$
By the fundamental theorem of calculus and the definition of
\(P^{(2)}\)
, this becomes
$$\begin{aligned} [H^{(2)}g(t)](0)+\int _0^t \left[ \frac{1}{s}[P^{(2)}g](s)\right] (t-s)\, ds.\end{aligned}$$
Since
\([H^{(2)}g(t)](0)=g(0)\)
by the delta function initial condition, we have (
4.22
).
To invert the right-hand side of (
4.22
), we use the Neumann series
$$\begin{aligned}\left( \operatorname {Id}+\frac{1}{T^2}P^{(2)}\right) ^{-1}=\operatorname {Id}-\sum _{j=1}^{\infty }\left( -\frac{1}{T^2}P^{(2)}\right) ^{j}=:\operatorname {Id}+P^{(3)}.\end{aligned}$$
By our composition Theorem
3.16
, since
\(-T^{-2}P^{(2)}\in {\mathcal {A}}_h^{\infty ,-3,\infty ,0}\)
, we obtain that for each
j
,
$$\begin{aligned}\left( -\frac{1}{T^2}P^{(2)}\right) ^j\in {\mathcal {A}}_h^{\infty ,-4+j,\infty ,0}.\end{aligned}$$
This series may therefore be asymptotically summed, and we obtain that
\(P^{(3)}\in {\mathcal {A}}_h^{\infty ,-3,\infty ,0}\)
.
In fact this asymptotic sum is a legitimately convergent sum. This is asserted in [
35
] in the edge case and proven in [
40
, p. 270] for compact manifolds; the same applies here as well.
Finally, set
$$\begin{aligned}H^{(3)}=H^{(2)}\left( \operatorname {Id}+P^{(3)}\right) .\end{aligned}$$
By the definition of convolution, the Neumann boundary conditions, being satisfied by
\(H^{(2)}\)
, are also satisfied by
\(H^{(3)}\)
. Since
\(H^{(2)}\in {\mathcal {A}}_h^{-2,-2,0,0}\)
and
\(P^{(3)}\in {\mathcal {A}}_h^{\infty ,-3,\infty ,0}\)
, our composition Theorem
3.16
tells us that
$$\begin{aligned} H^{(3)}\in {\mathcal {A}}_h^{-2,-2,0,0}+{\mathcal {A}}_h^{\infty ,-1,0,0}. \end{aligned}$$
Since
\(\mathcal {L}H^{(3)}=\operatorname {Id}\)
,
\(H^{(3)}\)
satisfies the delta function initial condition. By uniqueness for the Neumann heat kernel on a manifold with boundary,
\(H^{(3)}\)
must therefore be the true heat kernel.
Theorem 4.4
The Neumann heat kernel on
\(\Omega \)
is pc on
\(\Omega ^2_h\)
, and is an element of
\({\mathcal {A}}_h^{-2,-2,0,0}\)
. Its expansion at td is given by (
4.20
), and its leading term at sf is given by
\({\mathcal {H}}_{-2,\text {sf},N}\)
. Moreover it is smooth down to both
\(E_{j0}\)
and
\(E_{0j}\)
, and its expansion at sf is
\(T^{-2}\)
times a smooth expansion.
Proof
The heat kernel is smooth down to
\(E_{j0}\)
because
\(H^{(2)}\)
is smooth by construction, and the composition theorem implies
\(H^{(3)}\)
is smooth. The required statement at sf follows from the same logic. Finally, it is smooth down to
\(E_{0j}\)
because it is symmetric. For the leading term statements, the leading terms of
\(H^{(2)}\)
have the claimed properties, and
\(H^{(2)}P^{(3)}\)
vanishes rapidly at td and is lower order than
\(H^{(2)}\)
at sf. This completes the proof.
\(\square \)
An analogous theorem, proved in an identical fashion, holds for the Dirichlet heat kernel. Since the Dirichlet boundary condition is the Friedrichs extension for a one-dimensional cone, this is in fact a special case of [
35
]. Note that the Dirichlet boundary condition implies that the heat kernel vanishes to first order at
\(E_{10}\)
and
\(E_{01}\)
:
Theorem 4.5
[
35
] The Dirichlet heat kernel on
\(\Omega \)
is pc on
\(\Omega ^2_h\)
, and is an element of
\({\mathcal {A}}_h^{-2,-2,1,1}\)
. Its expansion at td is given by (
4.20
), and its leading term at sf is given by
\({\mathcal {H}}_{-2,\text {sf},D}\)
. Moreover it is smooth down to both
\(E_{j0}\)
and
\(E_{0j}\)
, and is
\(T^{-2}\)
times a smooth expansion at sf.
4.2.2
The Robin heat kernel
We now construct the Robin heat kernel on
\(\Omega \)
as a correction, or perturbation, of the Neumann heat kernel on
\(\Omega \)
. To distinguish it, let
\(H_{Neumann}(t,z,z')\)
be the Neumann heat kernel, which is pc on
\(\Omega ^2_h\)
by the previous section. Our Robin boundary condition is
$$\begin{aligned} \left. \frac{\partial u(x,y)}{\partial y} \right| _{y=0}=\kappa (x)u(x,0). \end{aligned}$$
Our model will be the Robin heat kernel for a half-space with constant
\(\kappa \)
. With that in mind, define
$$\begin{aligned} H^{(0)}_{Robin}:=H_{Neumann}-\frac{\kappa (XT+x')}{2\sqrt{\pi } T}\exp \left[ -\frac{1}{4}X^2\right] \text{ erfc }\left( \frac{1}{2}(\xi +\xi ')\right) . \end{aligned}$$
The distinction here is that now
\(\kappa \)
depends on the variable
x
, which can be expressed in terms of the coordinates
X
,
T
, and
\(x'\)
as
\(x=XT+x'\)
.
Both terms are pc. The first term is an element of
\({\mathcal {A}}_h^{-2,-2,0,0}\)
and the second term is an element of
\({\mathcal {A}}_h^{\infty ,-1,0,0}\)
. Now we compute, using erfc
\('(s)=-2e^{-s^2}/\sqrt{\pi }\)
, that
$$\begin{aligned} \begin{aligned}&\left. \left( \frac{\partial }{\partial y}-\kappa \right) H^{(0)}_{Robin}\right| _{y=0} \\&\quad =\left. \frac{1}{T}\frac{\partial }{\partial \xi }\right| _{\xi =0}\left( -\frac{\kappa (XT+x')}{2\sqrt{\pi } T}\exp \left[ -\frac{1}{4}X^2\right] \operatorname {erfc}\left( \frac{1}{2}(\xi +\xi ')\right) \right) \\&\quad \quad \left. -\kappa H^{(0)}_{Robin}\right| _{y=0} \\&\quad =\frac{\kappa (XT+x')}{2\pi T^2}\exp \left[ -\frac{1}{4}X^2\right] \exp \left[ -\frac{1}{4}\xi '^2\right] \\&\quad \quad -\kappa (XT+x') \left. H_{Neumann}\right| _{y=0} \\&\quad \quad +\frac{(\kappa (XT+x'))^2}{2\sqrt{\pi } T}\exp \left[ -\frac{1}{4}X^2\right] \text{ erfc }\left( \frac{1}{2}\xi '\right) . \end{aligned} \end{aligned}$$
(4.23)
Let this right-hand side be
\(c(T,X,x',\xi ')\)
. To put it politely, this is not zero. We correct this defect by defining
$$\begin{aligned} H^{(1)}_{Robin}:=H^{(0)}_{Robin}-ye^{-(y/T)^2}c(T,X,x',\xi '). \end{aligned}$$
This fixes the Robin defect: the derivative in
y
at
\(y=0\)
of the second term above is precisely
\(-c(T,X,x',\xi ')\)
, and
\(\kappa \)
times this term is zero at
\(y=0\)
, so we have
$$\begin{aligned} \left. \left( \frac{\partial }{\partial y}-\kappa (x)\right) H^{(1)}_{Robin}\right| _{y=0}=0. \end{aligned}$$
Lemma 4.6
The function
\(H^{(1)}_{Robin}\)
is an element of
\({\mathcal {A}}^{-2,-2,0,0}_h\)
, satisfying Robin boundary conditions in the left variable. At td, it has the same expansion as
\(H_{Neumann}\)
. At sf, the first two terms of its asymptotic expansion are the first two terms for
\(H_{Neumann}\)
plus
\(T^{-1}{\mathcal {H}}_{-1,\text {sf},R}\)
, where
$$\begin{aligned} {\mathcal {H}}_{-1,\text {sf},R}:=-\frac{\kappa (x')}{2\sqrt{\pi }}\exp \left[ -\frac{1}{4}X^2\right] \operatorname {erfc}\left( \frac{1}{2}(\xi +\xi ')\right) . \end{aligned}$$
(Comparing to (
4.18
), the only change is that
\(\kappa \)
is now a function of
\(x'\)
rather than a constant.) Furthermore,
$$\begin{aligned}t{\mathcal {L}} H^{(1)}_{Robin}\in {\mathcal {A}}^{\infty ,0,0,0}_h.\end{aligned}$$
Remark 4.7
Note that
\(H^{(1)}_{Robin}\)
is a slightly better parametrix than
\(H^{(1)}\)
was for the Neumann and Dirichlet problems. This is because we have solved the model problem to two orders at sf, rather than just to first order. This is necessary because we want to identify the sub-leading term of the true Robin heat kernel at sf.
Proof
We just showed
\(H^{(1)}\)
does satisfy the Robin boundary condition. Now we claim it is pc. At first it appears there are problems with the second term at
\(y=T=0\)
away from the diagonal, and that we might need to blow up the intersection of
\(E_{10}\)
and tf. However, at this intersection,
\(c(T,X,x',\xi ')\)
decays rapidly, so in fact
\(H^{(1)}_{Robin}\)
is already pc. It decays to infinite order at tf because both terms in its definition do. We also have
$$\begin{aligned} H_{Robin}^{(1)}-H_{Neumann} =&-ye^{-(y/T)^2}c(T,X,x',\xi ') \\  &-\frac{\kappa (XT+x')}{2\sqrt{\pi } T} \exp \left[ -\frac{1}{4}X^2 \right] \operatorname {erfc}\left( \frac{1}{2}(\xi +\xi ')\right) . \end{aligned}$$
It is immediate that the leading order of the second term at sf is in fact
\(T^{-1}{\mathcal {H}}_{-1,\text {sf},R}\)
, and that the second term vanishes to infinite order at td and is smooth up to all other boundary hypersurfaces. We claim that
$$\begin{aligned} ye^{-(y/T)^2}c(T,X,x',\xi ')\in {\mathcal {A}}_h^{\infty ,0,0,0}, \end{aligned}$$
(4.24)
which immediately implies the statements concerning the asymptotic expansions of
\(H^{(1)}_{Robin}\)
at td and sf.
To prove (
4.24
), we need to check decay. The statements at
\(E_{10}\)
and
\(E_{01}\)
are obvious, and the presence of
\(ye^{-(y/T)^2}\)
implies the requisite infinite-order decay at td. The trickier face is sf. Since
y
decays to first order at sf, and
\(e^{-(y/T)^2}\)
is smooth, we need to examine
\(c(T,X,x',\xi ')\)
and show it has order at worst
\(-\,1\)
. The third term in (
4.23
) is already order − 1. However, the first and second terms have order
\(-2\)
, but we shall compute that their difference has order
\(-\,1\)
. As
\(T\rightarrow 0\)
, because
\(H_{Neumann}\)
is polyhomogeneous, its restriction to
\(y=0\)
has an expansion at sf, and the leading term is (
4.6
), so
$$\begin{aligned} \left. H_{Neumann}\right| _{y=0}&= \left. \frac{1}{T^2}{\mathcal {H}}_{-2,\text {sf},N}\right| _{\xi =0}+ O\left( \frac{1}{T}\right) \\&=\frac{1}{2\pi T^2}\exp \left[ -\frac{1}{4}X^2\right] \exp \left[ -\frac{1}{4}(\xi ')^2\right] + O\left( \frac{1}{T}\right) . \end{aligned}$$
Examining (
4.23
), this
\(T^{-2}\)
term here cancels the first
\(T^{-2}\)
term, and thus
\(c(T,X,x',\xi ')\)
is
\(O(\frac{1}{T})\)
at sf. Therefore the order of
\(ye^{-(y/T)^2}c(T,X,x',\xi ')\)
is at worst
\(1+(-1)=0\)
at sf, proving the claim (
4.24
).
Now consider
\((t{\mathcal {L}})H^{(1)}_{Robin}\)
. Since
\(\mathcal {L}H_{Neumann}=0\)
because it is the heat kernel, we have
$$\begin{aligned} (t{\mathcal {L}})H^{(1)}_{Robin}&=(t{\mathcal {L}})(H^{(1)}_{Robin}-H_{Neumann}) \nonumber \\&=(t{\mathcal {L}})(-ye^{(-y/T)^2}c(T,X,x',\xi ')) \nonumber \\&\quad -(t{\mathcal {L}})\left( \frac{\kappa (XT+x')}{2\sqrt{\pi } T}\exp \left[ -\frac{1}{4}X^2\right] \operatorname {erfc}\left( \frac{1}{2}(\xi +\xi ')\right) \right) . \end{aligned}$$
(4.25)
The first term is an element of
\({\mathcal {A}}^{\infty ,0,0,0}_h\)
before applying
\(t{\mathcal {L}}\)
. Since
\(t{\mathcal {L}}\)
is tangent to all boundary hypersurfaces except
\(E_{10}\)
, it preserves the orders, and at
\(E_{10}\)
,
\(t\mathcal {L}\)
takes a smooth expansion to a smooth expansion. The second term is an element of
\({\mathcal {A}}^{\infty ,-1,0,0}_h\)
, but we can write the Taylor expansion of
\(\kappa (XT+x')\)
in powers of
T
. The
\(T^0\)
term is just
\(\kappa (x')\)
, yielding
\({\mathcal {H}}_{-1,\text {sf},R}\)
, which
\(t{\mathcal {L}}\)
annihilates by (
4.19
). All terms except the
\(T^0\)
term are elements of
\({\mathcal {A}}^{\infty ,0,0,0}_h\)
, and thus remain so after the application of
\(t{\mathcal {L}}\)
. This completes the proof of Lemma
4.6
.
\(\square \)
From here the argument is very similar to the Neumann and Dirichlet arguments.
Proposition 4.8
There exists an element
\(H^{(2)}_{Robin}\in {\mathcal {A}}_h^{-2,-2,0,0}\)
which satisfies Robin boundary conditions in the left factor, with
\(\lim _{t\rightarrow 0}H^{(2)}=\delta (z-z')\)
, and with
$$\begin{aligned} t\mathcal {L}H^{(2)}\in {\mathcal {A}}_h^{\infty ,0,\infty ,0}. \end{aligned}$$
Moreover the expansions of
\(H^{(2)}_{Robin}\)
and
\(H^{(1)}_{Robin}\)
are identical for all terms at td and for the terms of order
\(-2\)
and
\(-\,1\)
at sf.
Proof
We add terms at order
\(y^2\)
and up at the face
\(E_{10}\)
, as in Proposition
4.3
. Note that each of these terms is
\(y^k\)
for
\(k\ge 2\)
times a term which has order
\(-2\)
at sf, and thus each of these terms has order greater than or equal to zero at sf, so there is no effect on the first two terms of the expansion there.
\(\square \)
Now we let
$$\begin{aligned}P^{(2)}_{Robin}:=t\mathcal {L}H^{(2)}_{Robin};\ P^{(3)}_{Robin}:=-\sum _{j=1}^{\infty }\left( -\frac{1}{T^2}P^{(2)}_{Robin}\right) ^j.\end{aligned}$$
We have
\(T^{-2}P^{(2)}_{Robin}\in {\mathcal {A}}_h^{\infty ,-2,\infty ,0}\)
, so its
j
th power is an element of
\(A_h^{\infty ,-4+2j,\infty ,0}\)
by the composition theorem, and thus
\(P^{(3)}_{Robin}\in {\mathcal {A}}_h^{\infty ,-2,\infty ,0}\)
. As before the sum is convergent, not just asymptotically convergent. Then set
$$\begin{aligned}H^{(3)}_{Robin}=H^{(2)}_{Robin}\left( \operatorname {Id}+P^{(3)}_{Robin}\right) .\end{aligned}$$
This satisfies the Robin boundary conditions and the initial condition, so by uniqueness it is the true Robin heat kernel. By composition,
\(H^{(2)}_{Robin}P^{(3)}_{Robin}\in {\mathcal {A}}_h ^{\infty ,0,0,0}\)
, so
\(H^{(3)}_{Robin}\)
has the same first two terms at sf and same full expansion at td as
\(H^{(2)}_{Robin}\)
. We have now proved:
Theorem 4.9
The Robin heat kernel on
\(\Omega \)
, with smooth non-negative Robin parameter
\(\kappa (x)\)
, is pc on
\(\Omega ^2_h\)
, and is an element of
\({\mathcal {A}}_h^{-2,-2,0,0}\)
, smooth down to both
\(E_{10}\)
and
\(E_{01}\)
and equal to
\(T^{-2}\)
times a smooth expansion at sf. It is equal to the Neumann heat kernel on
\(\Omega \)
plus a correction term which is an element of
\({\mathcal {A}}_h^{\infty ,-1,0,0}\)
and which has leading order
\({\mathcal {H}}_{-1,\text {sf},R}\)
at sf.
Indeed, the only part of this we have not addressed is the smoothness, and it follows as in the Neumann case.
5
The heat kernel on a curvilinear polygonal domain
Consider a two-dimensional sector
\(S_{\gamma }\)
with angle
\(\gamma \in (0,2\pi )\)
. We investigate heat kernels on
\(S_{\gamma }\)
to serve as models for our eventual construction of the heat kernel on curvilinear polygonal domains.
5.1
Properties of the heat kernel for an infinite sector
We will consider the D–D, N–N, and D–N heat kernels. Recall the expression from [
6
, p. 592 (3.42)], which in our setting is simply
$$\begin{aligned} H(t,r,\theta ,r',\theta ')=\frac{1}{2t}\exp \left[ -\frac{r^2+(r')^2}{4t}\right] \sum _{j=1}^{\infty }I_{\mu _j}\left( \frac{rr'}{2t}\right) \phi _j(\theta )\phi _j(\theta '). \end{aligned}$$
(5.1)
Here
\(I_{\mu _j}\)
are the modified Bessel functions, and
\((\phi _j,\mu _j)\)
are the eigenfunctions, and corresponding eigenvalues, of the appropriate eigenvalue problem (D–D, N–N, or D–N) on the interval
\([0,\gamma ]\)
.
The pc properties of (
5.1
) are not obvious from the expression alone. They are equally non-obvious from the equivalent expression given by the inverse Laplace transform of the Green’s function. However, we claim:
Lemma 5.1
In each of the three settings, D–D, N–N, and D–N, the heat kernel (
5.1
) is pc on our double space
\((S_{\gamma })_h^2\)
.
Proof
The proof is based on the reflection argument in [
2
, Sect. 3]. Consider the D–D case for the moment. The sector
\(S_{\gamma }\)
doubles to an infinite flat cone
\(C_{2\gamma }\)
, and if we let
L
cut this cone in half, then we claim that the D–D heat kernel on
\(S_{\gamma }\)
is
$$\begin{aligned} H_{S_{\gamma }}(t,r,\theta ,r',\theta ')=H_{C_{2\gamma }}(t,r,\theta ,r',\theta ')-H_{C_{2\gamma }}(t,r,\theta ,\text {ref}_L(r',\theta ')). \end{aligned}$$
(5.2)
Above
\(H_{C_{2\gamma }}\)
is the Friedrichs heat kernel on
\(C_{2\gamma }\)
, and
\(\text {ref}_L\)
is reflection across
L
. Indeed it is clear that the difference of heat kernels satisfies the heat equation and the initial condition on
\(S_{\gamma }\)
, as well as the Dirichlet boundary condition. By uniqueness of the heat kernel, we have (
5.2
).
The pc properties of
\(H_{S_{\gamma }}\)
may now be deduced from those of
\(H_{C_{2\gamma }}\)
, as in [
2
]. By [
41
,
35
],
\(H_{C_{2\gamma }}\)
is pc on a double heat space. In the notation of [
35
], the
x
-coordinate is
r
, there is no
y
-coordinate, and the
z
-coordinate is
\(\theta \)
. The Mazzeo–Vertman heat space is not exactly the same as our heat space
\((C_{2\gamma })_h^2\)
, as [
35
] do not create a face hvff, but nevertheless:
\(\square \)
Proposition 5.2
The Mazzeo–Vertman heat space is a blow-down of
\((C_{2\gamma })_h^2\)
, and therefore
\(H_{C_{2\gamma }}\)
is pc on
\((C_{2\gamma })_h^2\)
.
Proof
Begin with the manifold with corners
\([0,\infty )\times (C_{2\gamma })_0\times (C_{2\gamma })_0\)
. The Mazzeo–Vertman heat space is created by blowing up:
\(\{0\}\times {\tilde{V}}\times {\tilde{V}}\)
; and
the lift of the interior
\(T=0\)
diagonal.
From this space, we make a further blow-up at
\([0,\infty )\times {\tilde{V}}\times {\tilde{V}}\)
. We claim that the resulting space is
\((C_{2\gamma })^2_h\)
, which is all we need. Indeed, this further blow-up is disjoint from the lift of the interior
\(T=0\)
diagonal and thus may be done second instead of third, by Proposition
3.8
. It may then be done first instead of second, since nested blow-ups commute (again by Proposition
3.8
). Hence our heat space
\((C_{2\gamma })_h^2\)
is a blow-up (indeed, an overblown version) of the Mazzeo–Vertman heat space.
\(\square \)
This takes care of the direct term, which is the first term in the right side (
5.2
). The reflected term [the second term in the right side of (
5.2
)] is pc on a nearly identical space, the only difference being that we blow up the
\(T=0\)
anti-diagonal
\(\{T=0,r=r',\theta =\text {ref}_L(\theta ')\}\)
in the last step rather than the
\(t=0\)
diagonal. The lifts of the diagonal and anti-diagonal are not disjoint. They intersect at the lift of
\(\{T=0,r=r',\theta =\theta '\in L\}\)
. So in order to obtain a space on which both the direct and reflected terms are pc we blow up that lift before dealing with the diagonal and anti-diagonal. We do this: first blow up that lift, then blow up the diagonal and anti-diagonal, and we have obtained a space on which the direct and reflected terms are both pc.
When we restrict our spatial arguments to lie in
\(S_{\gamma }\)
, we claim that this space is the double heat space
\((S_{\gamma })^2_h\)
. Indeed, blowing up the lift of
\(\{T=0,r=r',\theta =\theta '\in L\}\)
is precisely what is needed to create the face sf. We are doing it after blowing up hvff, hvlf, and hvrf, rather than before, but these blow-ups are disjoint (since we have already created ff) and therefore commute. The anti-diagonal does not appear once we have restricted our arguments to lie in
\(S_{\gamma }\)
. Therefore
\(H_{S_{\gamma }}\)
is pc on
\((S_{\gamma })_h^2\)
, as desired.
The argument for the N–N heat kernel is identical; there is a plus sign instead of a minus sign in (
5.2
). For the D–N heat kernel, we double twice, to the cone
\(C_{4\gamma }\)
, and use the method of images with four terms rather than two. The details are very similar and we omit them here. This proves Lemma (
5.1
).
\(\square \)
Having proven that
\(H_{S_{\gamma }}\)
is pc on the double space, we may write down its leading order models at the various boundary hypersurfaces. We begin at ff. In the interior of ff, good coordinates are given by
$$\begin{aligned} T=\sqrt{t},\ R:=\frac{r}{T},\ R':=\frac{r'}{T},\ \theta ,\ \theta '. \end{aligned}$$
(5.3)
In fact these coordinates are good uniformly down to hvlf and hvrf in the Mazzeo–Vertman double space, but to create
\((S_{\gamma })_h^2\)
we have made an additional blowup at hvff, which in these coordinates is
\(\{R=R'=0\}\)
. Fortunately this is not important for our present concerns. Writing (
5.1
) in the coordinates (
5.3
) gives
$$\begin{aligned} H_{S_{\gamma }}=\frac{1}{2}T^{-2}\exp \left[ -\frac{1}{4}(R^2+(R')^2)\right] \sum _{j=1}^{\infty }I_{\mu _j}\left( \frac{1}{2}RR'\right) \phi _j(\theta )\phi _j(\theta '). \end{aligned}$$
(5.4)
This motivates the definition of the models
$$\begin{aligned}  &   {\mathcal {H}}_{-2,\text {ff},DD},\text { resp. } H_{-2,\text {ff},DN},\text { resp. } H_{-2,\text {ff},NN}\nonumber \\  &   \quad :=\frac{1}{2}\exp \left[ -\frac{1}{4}(R^2+(R')^2)\right] \sum _{j=1}^{\infty }I_{\mu _j}\left( \frac{1}{2}RR'\right) \phi _j(\theta )\phi _j(\theta '), \end{aligned}$$
(5.5)
where
\((\phi _j,\mu _j)\)
are the eigenfunctions and eigenvalues of the appropriate problems on
\([0,\gamma ]\)
. It is then true that the leading term of the expansion of
\(H_{S_{\gamma }}\)
at ff, with D–D, D–N, or N–N boundary conditions, is
\(T^{-2}{\mathcal {H}}_{-2,\text {ff},DD}\)
,
\(T^{-2}{\mathcal {H}}_{-2,\text {ff},DN}\)
, or
\(T^{-2}{\mathcal {H}}_{-2,\text {ff},NN}\)
, respectively.
As usual, the heat kernel is decaying to infinite order at tf. We claim that its models at sf and at td are familiar:
Proposition 5.3
The leading order models at sf and td of
\(H_{S_{\gamma }}\)
are the same as the models (
4.11
), (
4.6
), and (
4.9
) for a manifold with boundary, namely
\({\mathcal {H}}_{-2,\text {sf},D}\)
or
\({\mathcal {H}}_{-2,\text {sf},N}\)
at each of the two components of sf (depending on the boundary condition) and
\({\mathcal {H}}_{-2,\text {td}}\)
at td.
Proof
This is true because of locality; in fact, all the models are the same, not just the leading order. In any patch of sf away from ff, the spatial variables are near the boundary of
\(S_{\gamma }\)
but bounded away from the corner. Since we are looking at short-time asymptotics, Kac’s principle holds: the heat kernel can be approximated to infinite order in
T
by the heat kernel on a half-plane. To make this precise, we quote [
32
, Theorem 3]; see also [
43
]. Since this works on any patch of sf away from ff, and the models themselves are pc on sf, they must agree on all of sf, including down to ff.
\(\square \)
Since
\(H_{S_{\gamma }}\)
is pc on the double heat space, its leading order models must be compatible with each other at the intersections. We will use this in the construction of the heat kernel for curvilinear polygonal domains. In particular:
Corollary 5.4
We have the following compatibility conditions for the D–D heat kernel:
$$\begin{aligned}{\mathcal {H}}_{-2,\text {ff},DD}|_{\text {ff}\cap \text {sf}}={\mathcal {H}}_{-2,\text {sf},D}|_{\text {ff}\cap \text {sf}};\ {\mathcal {H}}_{-2,\text {ff},DD}|_{\text {ff}\cap \text {td}}={\mathcal {H}}_{-2,\text {td}}|_{\text {ff}\cap \text {td}}.\end{aligned}$$
An analogous result holds for the N–N heat kernel at both intersections, and for the D–N heat kernel at ff
\(\cap \)
td. Moreover, if
\(\hbox {sf}_{1}\)
is the Dirichlet component of sf and
\(\hbox {sf}_2\)
is the Neumann component of sf, we have the appropriate compatibility conditions for the D–N heat kernel at ff
\(\cap \)
sf:
$$\begin{aligned} {\mathcal {H}}_{-2,\text {ff},DN}|_{\text {ff}\cap \text {sf}_1}={\mathcal {H}}_{-2,\text {sf}_1,D}|_{\text {ff}\cap \text {sf}_1};\ {\mathcal {H}}_{-2,\text {ff},DN}|_{\text {ff}\cap \text {sf}_2}={\mathcal {H}}_{-2,\text {sf}_2,N}|_{\text {ff}\cap \text {sf}_2}.\end{aligned}$$
Remark 5.5
The preceding two results may be of independent interest, as it is not obvious from the explicit expressions of the leading order models that they satisfy these compatibility conditions.
5.2
Construction of the heat kernel
As before, let
\(\Omega \)
be a curvilinear polygonal domain, a subdomain of a larger surface
M
. Label its edges
\(E_j\)
and its vertices
\(V_j\)
, with
\(V_j\)
connecting
\(E_{j}\)
and
\(E_{j+1}\)
(with the appropriate generalization for multiple connected boundary components, which are allowed). For each
j
, let
\(\Omega _j\)
be a surface with smooth boundary, also a subdomain of
M
, such that
\(E_{j}\)
is a subset of the boundary of
\(\Omega _j\)
. Such a surface may always be created. In fact, using the tubular neighborhood theorem,
\(\Omega _j\)
may be chosen to be contained within a small neighborhood (in
M
) of
\(E_j\)
.
Fig. 6
Full size image
The lines between boundary faces of the double heat space indicate faces whose boundaries have non-empty intersection. The
\(E_{j0}\)
and
\(E_{0j}\)
faces are omitted for the sake of simplicity. We note that
\(E_{j0}\)
has non-empty intersection with hvrf, sf, and tf, whereas
\(E_{0j}\)
has non-empty intersection with hvlf, sf, and tf
5.3
Dirichlet and Neumann boundary conditions
We now construct the heat kernel in the setting where the boundary conditions on each side are either Dirichlet or Neumann, rather than Robin. Consider the heat space
\(\Omega _h^2\)
. We define a kernel
\(H^{(1)}\)
on this heat space by specifying its leading order behavior at various boundary hypersurfaces. In Fig.
6
, we show the faces of the double heat space whose boundaries have non-empty intersection, and in Fig.
7
, we zoom in on the double heat space near the intersection of
\(\overline{V}\)
and
E
. In fact, we will define
\(H^{(1)}\)
on a blown-down version of the heat space, without the faces
\(\hbox {hvff}_{jk}\)
. Call this space
\({\widetilde{\Omega }}_h^2\)
. By the proof of Proposition
5.2
, the hvff blowup may be done last, so
\({\widetilde{\Omega }}_h^2\)
is in fact a blow-down of
\(\Omega _h^2\)
. The reason is that the blowup at hvff is not necessary for the heat kernel for an exact cone, and is not done in Mazzeo–Vertman [
35
]. Here we only require this blowup to obtain the composition formula in Theorem
3.16
.
Fig. 7
Full size image
This is a schematic illustration of the intersection between the side and front faces
First, at td, we require
\(H^{(1)}\)
to have the usual local asymptotic expansion (
4.20
), namely
$$\begin{aligned} H^{(1)}\sim \sum _{j=0}^{\infty }T^{-2+j}{\mathcal {H}}_{-2+j,\text {td}}. \end{aligned}$$
(5.6)
Naturally we also ask that
\(H^{(1)}\)
decay to infinite order at tf.
Observe that since
\(\Omega \)
is a subdomain of a smooth manifold
M
, each model
\({\mathcal {H}}_{-2+j,\text {td}}\)
is smooth up to the boundary of
\(\Omega \)
, so in particular smooth up to each
\(\hbox {sf}_j\)
and each
\(\hbox {ff}_j\)
.
At each side face
\(\hbox {sf}_j\)
, we use the heat kernel on
\(\Omega _j\)
, in boundary normal coordinates, as a model, where
\(\Omega _j\)
is the surface with boundary defined above. By Theorems
4.4
and
4.5
, the heat kernel
\(H^{\Omega _j}\)
is pc on
\((\Omega _j)_h^2\)
, and its expansion at the face sf of
\((\Omega _j)_h^2\)
may be written
$$\begin{aligned}\sum _{k=0}^{\infty }T^{-2+k}{\mathcal {H}}^{\Omega _j}_{-2+k,\text {sf}}\end{aligned}$$
for models
\({\mathcal {H}}^{\Omega _j}_{-2+k,\text {sf}}\)
which are pc on sf. Note that the leading order
\({\mathcal {H}}^{\Omega _j}_{-2,\text {sf}}\)
is either
\({\mathcal {H}}_{-2,\text {sf},D}\)
or
\({\mathcal {H}}_{-2,\text {sf},N}\)
, defined in (
4.11
) and (
4.6
), as appropriate. Now our face
\(\hbox {sf}_j\)
is simply a subdomain of the face sf of
\((\Omega _j)_h^2\)
, namely the restriction of sf to the region where both spatial variables are elements of
\(E_j\subseteq \partial \Omega _j\)
. So we simply set
$$\begin{aligned} H^{(1)}\sim \sum _{k=0}^{\infty }T^{-2+k}{\mathcal {H}}^{\Omega _j}_{-2+k,\text {sf}}. \end{aligned}$$
(5.7)
The requirements (
5.7
) and (
5.6
) are compatible since the heat kernel
\(H^{\Omega _j}\)
is pc and has the same models. They are also both compatible with infinite-order decay at tf, and with the appropriate boundary conditions on
\(E_{j0}\)
, for the same reason.
Near each face
\(\hbox {ff}_j\)
it is necessary to pick local polar coordinates. Define
r
and
\(\theta \)
to be the polar-coordinate version of boundary normal coordinates along
\(E_j\)
, so that i.e.
\(x=r\cos \theta \)
and
\(y=r\sin \theta \)
. In these coordinates,
\(E_j\)
is given by
\(\theta =0\)
, and
\(E_{j+1}\)
is given by a curve with angle
\(\theta =\alpha _j\)
at the origin. Of course, we could also have chosen polar coordinates from the boundary normal coordinates along
\(E_{j+1}\)
, so that
\(E_{j+1}\)
is precisely
\(\theta =\alpha _j\)
and
\(E_j\)
is a curve with angle
\(\theta =0\)
at the origin. These two choices of polar coordinate systems agree to second order in a neighborhood of
\(r=0\)
. With this described, coordinates valid in the interior of ff are (
5.3
). Moreover, in these coordinates, we have
\(R=0\)
at
\(\hbox {hvlf}_j\)
,
\(R'=0\)
at
\(\hbox {hvrf}_j\)
,
\(\theta =0\)
at
\(E_{j0}\)
,
\(\theta =\alpha _j\)
at
\(E_{j+1,0}\cap ff_j\)
,
\(\theta '=0\)
at
\(E_{0j}\)
, and
\(\theta '=\alpha _j\)
at
\(E_{0,j+1}\cap ff_j\)
. The face
\(\hbox {hvff}_j\)
is an extra, overblown face at
\(R=R'=0\)
.
The point is that at
\(\hbox {ff}_j\)
, we can just use one of the models
\({\mathcal {H}}_{-2,\text {ff},DD}\)
,
\({\mathcal {H}}_{-2,\text {ff},DN}\)
(or its flipped variant
\({\mathcal {H}}_{-2,\text {ff},ND}\)
) or
\({\mathcal {H}}_{-2,\text {ff},NN}\)
, depending on which boundary conditions we are imposing on
\(E_j\)
and
\(E_{j+1}\)
. These models are defined in (
5.5
). So we require that at each
\(\hbox {ff}_j\)
,
$$\begin{aligned} H^{(1)}\sim T^{-2}{\mathcal {H}}_{-2,\text {ff},DD}(R,\theta ,R',\theta '), \end{aligned}$$
(5.8)
with DD replaced by DN, ND, or NN depending on the boundary conditions. Since the Laplacian is equal to the Laplacian for a straight sector to leading order at ff, these models solve the model problem at each
\(\hbox {ff}_j\)
.
By Corollary
5.4
, the requirement (
5.8
) is compatible with (
5.6
) and (
5.7
) at td and at
\(\hbox {sf}_j\)
. At
\(\hbox {sf}_{j+1}\)
, it also follows from Corollary
5.4
, because even though we no longer have an exact cone and thus the boundary normal coordinates for
\(E_{j+1}\)
do not agree with the polar coordinates
\((r,\theta )\)
everywhere, these two coordinate systems do agree to second order in
\(\rho _{ff_j}\)
. A similar argument, from the exact cone condition, shows that (
5.8
) is compatible with the appropriate boundary conditions at
\(E_{j0}\)
and
\(E_{j+1,0}\)
.
Since (
5.8
) is identical to the model for the exact sectorial heat kernel, this is also compatible with
\(H^{(1)}\)
being pc on
\({\widetilde{\Omega }}_h^2\)
rather than
\(\Omega _h^2\)
.
The point of checking compatibility is that as a result, we know that there exists a kernel
\(H^{(1)}\)
, pc on
\({\widetilde{\Omega }}_h^2\)
, with the expansions (
5.6
), (
5.7
), and (
5.8
) at the boundary hypersurfaces td,
\(\hbox {sf}_j\)
, and
\(\hbox {ff}_j\)
respectively, and which decays to infinite order at tf and satisfies the appropriate boundary conditions at each
\(E_{j0}\)
. If we let
\(\nu _{0,j}\)
be the smallest eigenvalue of the appropriate cross-sectional Laplacian in
\(\theta \)
at each component
\(\hbox {ff}_j\)
(note that in the Neumann–Neumann case we have
\(\nu _{0,j}=0\)
, and otherwise
\(\nu _{0,j}>0\)
), then the leading orders of
\(H^{(1)}\)
may be chosen as follows:
\(-2\)
at td,
\(\hbox {sf}_j\)
, and
\(\hbox {ff}_j\)
, with only integer powers in the expansion;
0 at
\(E_{j0}\)
and
\(E_{0j}\)
for each
j
, with only integer powers in the expansion; and
\(\nu _{0,j}\)
at
\(\hbox {hvlf}_j\)
and
\(\hbox {hvrf}_j\)
, with other fractional powers.
As in the case of manifolds with boundary, we consider
\(P^{(1)}:=t{\mathcal {L}} H^{(1)}\)
. It is pc on
\({\widetilde{\Omega }}_h^2\)
. Since both
\(\Delta H^{(1)}\)
and
\(\partial _t H^{(1)}\)
satisfy the boundary conditions (by the eigenfunction expansion, the Laplacian preserves the boundary conditions when it is applied), so does
\(P^{(1)}\)
. The leading orders of
\(P^{(1)}\)
are as follows:
\(\infty \)
at td and at each
\(\hbox {sf}_j\)
, since we have solved the model problem to all orders;
\(-\,1\)
at
\(\hbox {ff}_j\)
, since we have solved the model problem to one order;
0 at
\(E_{0j}\)
, and
\(\nu _{0,j}\)
at
\(\hbox {hvrf}_j\)
, since the lift of
\(t{\mathcal {L}}\)
is tangent to these hypersurfaces;
0 at
\(E_{j0}\)
, since
\(t{\mathcal {L}}\)
decreases the index set by 2, but not when applied to a
smooth
expansion; and
\(\nu _{0,j}-1\)
at
\(\hbox {hvlf}_j\)
, since
\(t{\mathcal {L}}\)
decreases the index set by 2 at this face but the leading term is killed, as in Mazzeo–Vertman [
35
]. The leading order term of the Laplacian is the same as for the flat Laplacian, and our model is the flat heat kernel there. Technically this requires us to choose
\(H^{(1)}\)
to be equal to (
5.8
) in a neighborhood of
\(\hbox {hvlf}_j\)
, which we can do. Note this is compatible with the boundary condition at
\(E_{j0}\)
as well.
We now construct an improved parametrix which has error decaying to infinite order at both hvlf and
\(E_{j0}\)
. We do this in two steps, first eliminating the error at hvlf. This proceeds exactly as in Mazzeo–Vertman [
35
], as hvlf is the analogue of their face rf. In the interior of hvlf,
r
is a boundary defining function for hvlf; the other variables are
\(\theta \in [0,\alpha _j]\)
,
T
, and
\(z'\in \Omega \)
. To remove a term
\(r^{\gamma }a(\theta ,t,z')\)
in the expansion of
\(P^{(1)}\)
at
\(\hbox {hvlf}_j\)
, we need to solve the indicial equation on the cone
\(C([0,\alpha _j])\)
in
\((r,\theta )\)
, with
t
and
\(z'\)
as parameters:
$$\begin{aligned}\left( -\partial _{rr}-\frac{1}{r^2}(\partial _{\theta \theta }+\frac{1}{4})\right) u(r,\theta ,T,z')=r^{\gamma }T^{-2}a(\theta ,T,z'),\end{aligned}$$
with the appropriate boundary conditions at
\(\theta =0\)
and
\(\theta =\alpha _j\)
. Since
a
is a term in the expansion of
\(P^{(1)}\)
, it, itself, satisfies those boundary conditions. Therefore, as in [
33
,
35
] a solution
u
exists with asymptotic behavior at
\(r=0\)
given by either
\(r^{\gamma +2}\)
or possibly
\(r^{\gamma +2}\log r\)
in case of an unlucky indicial root coincidence. The dependence in
t
and
\(z'\)
is purely parametric, so
\(u(r,\theta ,T,z')\)
is pc in a neighborhood of
\(\hbox {hvlf}_j\)
. We multiply
\(u(r,\theta ,T,z')\)
by a cutoff function equal to 1 on a neighborhood of
\(\hbox {hvlf}_j\)
, choosing the cutoff function so that its gradient is parallel to each edge
\(E_{j0}\)
and thus preserves the boundary conditions at
\(\theta =0\)
and
\(\theta =\alpha _j\)
. Then subtracting this product from
\(H^{(1)}\)
eliminates the term
\(r^{\gamma }a(\theta ,T,z')\)
in the expansion at hvlf and does not change the leading order of
\(H^{(1)}\)
at any other boundary hypersurface. In particular, since hvlf does not intersect td or sf, the expansion of
\(H^{(1)}\)
there is unchanged. Moreover,
r
vanishes at ff, so
u
actually decays to the same order as
a
at ff, and thus the leading order of the expansion of
\(H^{(1)}\)
at ff is unchanged.
Iterating this process produces a parametrix
\(H^{(2a)}\)
and an error
\(P^{(2a)}\)
with all the same properties as
\(H^{(1)}\)
and
\(P^{(1)}\)
, except for two differences. First, there may be logarithmic terms at
\(\hbox {ff}_j\)
(as well as at
\(\hbox {hvlf}_j\)
) once we go one order down in the expansion. Second,
\(P^{(2a)}\)
now vanishes to infinite order at
\(\hbox {hvlf}_j\)
for each
j
.
To remove the error at
\(E_{j0}\)
, we follow the same template as for manifolds with boundary, using boundary ellipticity. Namely, if
y
is the boundary normal coordinate for the side
\(\Omega _j\)
, add a kernel which is equal to
$$\begin{aligned}\frac{1}{2}y^2\left( \mathcal {L}H^{(2a)}\right) (T,x,0,x',y')+ O(y^3)\end{aligned}$$
and supported in a neighborhood of
\(E_{j0}\)
. This improves the order of the error at
\(E_{j0}\)
from 0 to 1. Note also that
\(\mathcal {L}H^{(2a)}\)
vanishes to infinite order at
\(\hbox {sf}_j\)
, so there is no effect on the expansion at
\(\hbox {sf}_j\)
. Iterating this process and taking an asymptotic sum, as for manifolds with boundary, we obtain the following.
Proposition 5.6
There exists a kernel
\(H^{(2)}\)
pc on
\({\widetilde{\Omega }}_h^2\)
, satisfying the appropriate combination of Dirichlet and Neumann boundary conditions, with
\(\lim _{t\rightarrow 0}H^{(2)}=\delta (z-z')\)
, where if we let
\(P^{(2)}=t\mathcal {L}H^{(2)}\)
,
\(H^{(2)}\)
vanishes to infinite order at tf and has the full expansions (
5.6
) and (
5.7
) at td and each
\(\hbox {sf}_j\)
respectively;
\(H^{(2)}\)
has leading term given by (
5.8
) at each
\(\hbox {ff}_j\)
, with the next term being one full order lower (possibly logarithmic);
\(P^{(2)}\)
vanishes to infinite order at tf, td, each
\(\hbox {sf}_j\)
, each
\(\hbox {hvlf}_j\)
, and each
\(E_{j0}\)
;
\(P^{(2)}\)
has leading order
\(-\,1\)
at each
\(\hbox {ff}_j\)
, 0 at each
\(E_{0j}\)
, and
\(\nu _{0,j}\)
at each
\(\hbox {hvrf}_j\)
.
We will need to compose, so we will blow up to pass to
\(\Omega _h^2\)
by creating
\(\hbox {hvff}_{jk}\)
.
Corollary 5.7
The kernels
\(H^{(2)}\)
and
\(P^{(2)}\)
also lift to be pc on
\(\Omega _h^2\)
, with leading orders
\(2\nu _{j,0}\)
and
\(\infty \)
respectively at
\(\hbox {hvff}_{jk}\)
.
Now we eliminate the last error by forming the formal Neumann series
$$\begin{aligned} \operatorname {Id}+P^{(3)}:=\operatorname {Id}-\sum _{k=1}^{\infty }\left( -\frac{1}{T^2}P^{(2)}\right) ^k. \end{aligned}$$
Note that
\(T^{-2}P^{(2)}\)
vanishes to infinite order at all faces except for
\(\hbox {ff}_j\)
,
\(E_{0j}\)
, and
\(\hbox {hvrf}_j\)
, where it has leading orders
\(-3\)
, 0, and
\(\nu _{0,j}\)
respectively. We use Theorem
3.16
to analyze the power
\((-T^{-2}P^{(2)})^{k}\)
. We see immediately that it also vanishes to infinite order at all other faces and has leading order
\(-4+k\)
at
\(\hbox {ff}_j\)
. At
\(\hbox {hvrf}_j\)
, the index sets have an inductive relationship: the index set for the
\(k^{th}\)
power is the extended union of the index set for the
\((k-1)^{st}\)
power with
k
plus the index set for the
\(0^{th}\)
power. The union of all of these is indeed a legitimate index set. In particular, there are only a finite number of extended unions involved at order less than
s
for each value of
s
. The leading order is
\(\nu _{0,j}\)
, and there is no logarithmic term at that leading order. At
\(E_{0j}\)
, the index set is the same as that for
\(P^{(2)}\)
, with leading order zero.
All of this allows us to asymptotically sum the Neumann series, and as before, the sum is convergent. The sum
\(P^{(3)}\)
has the same leading orders as
\(P^{(2)}\)
at each boundary hypersurface. As before, we let
$$\begin{aligned}H^{(3)}=H^{(2)}\left( \operatorname {Id}+P^{(3)}\right) ,\end{aligned}$$
and deduce that
\(H^{(3)}\)
is the true heat kernel.
By Theorem
3.16
, the term
\(H^{(2)}P^{(3)}\)
vanishes to infinite order at tf, td and sf, with leading order
\(-\,1\)
at
\(\hbox {ff}_j\)
, so it does not affect the expansion at td and sf and does not affect the first term at
\(\hbox {ff}_j\)
. It has leading order greater than or equal to zero everywhere else, with no logarithmic terms. This tells us the following:
Theorem 5.8
The heat kernel for
\(\Omega \)
, with Dirichlet or Neumann boundary conditions on each side
\(E_j\)
, is pc on
\(\Omega _h^2\)
, vanishing to infinite order at tf and continuous down to all boundary hypersurfaces except for td,
\(\hbox {sf}_j\)
, and
\(\hbox {ff}_j\)
.
Its full expansions at td and each
\(\hbox {sf}_j\)
are (
5.6
) and (
5.7
), which are the same as those for a closed manifold, and a manifold with boundary and the appropriate boundary condition, respectively.
Its expansion at
\(\hbox {ff}_j\)
has leading term (
5.8
) and no other terms within one order.
Remark 5.9
It is certainly possible to push through the composition formula and compute the index sets of the heat kernel for
\(\Omega \)
at other faces (hvff, hvrf, hvlf). However, we do not think that the results obtained in this fashion are optimal—there are quite a lot of log terms which may not actually exist—so we omit the statements. In fact, it is possible that the off-diagonal faces for positive time, namely
\(\hbox {hvff}_{jk}\)
for
\(j\ne k\)
, are not necessary at all, but our results are easier and likely quicker to prove this way.
The following corollary is a version of Kac’s principle of not feeling the boundary for the Dirichlet boundary condition [
22
]; see also [
43
] for the Neumann and Robin boundary conditions.
Corollary 5.10
The full expansions at td,
\(\hbox {sf}_j\)
, and
\(\hbox {ff}_j\)
are local, in the sense that if two domains with corners
\(\Omega \)
and
\(\Omega '\)
are isometric in a region
R
, then the expansions at the corresponding faces of the heat spaces
\(\Omega _h^2\)
and
\((\Omega ')_h^2\)
agree to all orders when the spatial variables are restricted to lie within the interior of
R
.
Note that these are all the faces in the lift of
\(\{t=0\}\)
where the heat kernel has nontrivial behavior, so the statement implies that any global contribution to the heat kernel at
\(t=0\)
is
\(O(t^{\infty })\)
.
Proof
The corollary follows immediately for td and
\(\hbox {sf}_j\)
from the construction, since the expansions there are the same as for
\(H^{(2)}\)
. For
\(\hbox {ff}_j\)
, it is also true: although the powers
\((T^{-2}P^{(2)})^j\)
are compositions and thus not local, by the composition theorem, their expansions at
\(\hbox {ff}_j\)
only depend on the expansion of
\(P^{(2)}\)
itself at
\(\hbox {ff}_j\)
, which
is
local. Thus the expansion of
\(P^{(3)}\)
at
\(\hbox {ff}_j\)
is local, and using the composition theorem again, so is the expansion of the true heat kernel.
\(\square \)
5.4
Robin boundary conditions
The construction of the Robin heat kernel proceeds very similarly to that of the Neumann heat kernel, though the boundary condition is somewhat more complicated. For each edge
\(E_j\)
, let
\(\kappa _j(x)\)
be a smooth function on
\(E_j\)
. The key lemma is as follows.
Lemma 5.11
There exists a kernel
\(H^{(1)}_{Robin}\)
, pc on
\({\widetilde{\Omega }}_h^2\)
and with
\(\lim _{t\rightarrow 0}H^{(2)}=\delta (z-z')\)
, such that, letting
\(P^{(1)}_{Robin}=H^{(1)}_{Robin}\)
,
\(H^{(1)}_{Robin}\)
satisfies Robin boundary conditions with parameter
\(\kappa _j(x)\)
on each edge
\(E_j\)
;
\(H^{(1)}_{Robin}\)
vanishes to infinite order at tf and has the full expansion (
5.6
) at td;
At each
\(\hbox {sf}_j\)
,
\(H^{(1)}_{Robin}\)
has the same full expansion as the Robin heat kernel on
\(\Omega _j\)
, with a parameter agreeing with
\(\kappa _j(x)\)
upon restriction to
\(E_j\)
;
At each
\(\hbox {ff}_j\)
,
\(H^{(1)}_{Robin}\)
has the same leading term (
5.8
) as in the Dirichlet, Neumann, or mixed cases, using the Neumann model at every Robin edge; and
\(P^{(1)}_{Robin}\)
has leading orders
\(\infty \)
at td and at
\(\hbox {sf}_j\)
,
\(-\,1\)
at
\(\hbox {ff}_j\)
, 0 at
\(E_{0j}\)
and
\(E_{j0}\)
,
\(\nu _{j,0}\)
at
\(\hbox {hvrf}_j\)
, and
\(\nu _{j,0}-1\)
at
\(\hbox {hvlf}_j\)
.
Proof
The issue is compatibility of all these requirements, noting that Robin boundary conditions are more complicated than Dirichlet or Neumann boundary conditions at the intersections of
\(E_{j0}\)
with
\(\hbox {sf}_j\)
and
\(\hbox {ff}_j\)
. However, it turns out that Robin boundary conditions only affect the
sub-leading
terms of the expansion of
\(H^{(1)}\)
at ff. This is why the Robin heat kernel may be viewed as a correction of the Neumann heat kernel.
We require the full expansion (
5.6
) at td, and observe that this is compatible with the expansion at
\(\hbox {sf}_j\)
, whose form is guaranteed by Theorem
4.9
, and the leading term (
5.8
) at
\(\hbox {ff}_j\)
. Indeed the compatibility betwen td and
\(\hbox {sf}_j\)
follows from the fact that the Robin heat kernel on
\(\Omega _j\)
is pc. The compatibility between td and
\(\hbox {ff}_j\)
follows from the fact that the Neumann heat kernel on
\(\Omega \)
is pc. The compatibility between
\(\hbox {sf}_j\)
and the leading term at
\(\hbox {ff}_j\)
follows from the fact that the leading term at
\(\hbox {sf}_j\)
is the same as for the Neumann problem on
\(\Omega \)
, so we can use Corollary
5.4
as in the previous section. It remains only to show that we can find such a kernel which also satisfies Robin boundary conditions.
To do this, note that Robin boundary conditions imply that if
u
is the leading order term (zeroth order) of the expansion of
\(H^{(1)}_{Robin}\)
at ff, then the next term must be
$$\begin{aligned}\kappa (x)y\cdot u.\end{aligned}$$
Since
y
vanishes at
\(\hbox {ff}_j\)
and
\(\hbox {sf}_j\)
as well as
\(E_{0j}\)
, this term vanishes to an order at
\(\hbox {ff}_j\)
and
\(\hbox {sf}_j\)
which is one higher than the order of
u
there. Hence any compatibility requirements only affect the lower order terms.
In order to dissect the compatibility requirements imposed by Robin boundary conditions, we zoom in near a triple intersection
\(E_{j0}\, \cap \, \text {sf}_j\, \cap \, \text {ff}_j\)
. Let boundary defining functions
\(\rho _E\)
,
\(\rho _{\text {sf}}\)
, and
\(\rho _{\text {ff}}\)
be chosen so that the product of all three is
y
; we use these three coordinates and suppress the (parametric) dependence in all other coordinates. We write out the (previously specified) expansion at sf
\(_j\)
as well as the (unknown save for the first term) expansion at ff
\(_j\)
, doing both for
\(tH^{(1)}\)
rather than
\(H^{(1)}\)
to keep notation simple:
$$\begin{aligned}&tH^{(1)}_{Robin}\cong \sum _{i=0}^{\infty }\rho _{\text {sf}}^i g_i(\rho _E,\rho _{\text {ff}})\text { at } \text {sf}_j; \nonumber \\&tH^{(1)}_{Robin}\cong \sum _{j=0}^{\infty }\rho _{\text {ff}}^j h_j(\rho _E,\rho _{\text {sf}})\text { at } \text {ff}_j. \end{aligned}$$
(5.9)
We also write the expansion of each
\(g_i\)
at
\(\rho _{\text {ff}}=0\)
:
$$\begin{aligned} g_i(\rho _E,\rho _{\text {ff}})\cong \sum _{k=0}^{\infty }\rho _{\text {ff}}^ka_{ik}(\rho _E)+O(\rho _{\text {ff}}^{\infty }). \end{aligned}$$
(5.10)
In order for the expansions (
5.9
) to be compatible with each other, for each
j
, we need
$$\begin{aligned} h_{j}(\rho _{E},\rho _{\text {sf}})\cong \sum _{i=0}^{\infty }\rho _{\text {sf}}^{i}a_{ij}(\rho _E) + O(\rho _{\text {sf}}^{\infty }). \end{aligned}$$
(5.11)
On the other hand, in these coordinates, our Robin boundary condition becomes
$$\begin{aligned} \left( \frac{1}{\rho _{\text {sf}}\rho _{\text {ff}}}\frac{\partial }{\partial \rho _E}-\kappa (\rho _{\text {sf}},\rho _{\text {ff}})\right) H^{(1)}_{Robin}=0, \\ \text{ i.e. } \left( \frac{\partial }{\partial \rho _E}-\rho _{\text {sf}}\rho _{\text {ff}}\kappa (\rho _{\text {sf}},\rho _{\text {ff}})\right) tH^{(1)}_{Robin}=0. \end{aligned}$$
Plugging in (
5.9
), organizing, and equating the coefficients of the
\(\rho _{\text {sf}}^i\)
terms tells us that the compatibility condition at sf
\(_j\cap E_{j0}\)
is, for each
\(i\ge 1\)
:
$$\begin{aligned} (g_i)_{\rho _E}(0,\rho _{\text {ff}})= \rho _{\text {ff}}\cdot \left( \text { the coefficient of }\rho _{\text {sf}}^{i}\text { in }\sum _{\ell =0}^i\kappa (\rho _{\text {sf}},\rho _{\text {ff}})g_{\ell -1}(0,\rho _{\text {ff}})\rho _{\text {sf}}^{\ell }\right) , \end{aligned}$$
(5.12)
and that this derivative is zero when
\(i=0\)
. Similarly, the compatibility condition at
\(\hbox {ff}_j\cap E_{j0}\)
is, for each
\(j\ge 1\)
,
$$\begin{aligned} (h_j)_{\rho _E}(0,\rho _{\text {sf}}) = \rho _{\text {sf}}\cdot \left( \text { the coefficient of }\rho _{\text {ff}}^{j}\text { in }\sum _{m=0}^j\kappa (\rho _{\text {sf}},\rho _{\text {ff}})h_{m-1}(0,\rho _{\text {sf}})\rho _{\text {ff}}^{m}\right) , \end{aligned}$$
(5.13)
and that the derivative is zero when
\(j=0\)
.
Recall that the full expansion of
\(H^{(1)}_{Robin}\)
is specified at
\(\hbox {sf}_j\)
; since that heat kernel satisfies Robin conditions, we assume the compatibility condition (
5.12
). We have also specified the first term
\(h_0(\rho _{E},\rho _{\text {sf}})\)
at
\(\hbox {ff}_j\)
. Since it satisfies a Neumann boundary condition, its
\(\rho _E\)
derivative at
\(E_{0j}\)
is indeed zero, as required. We need to show that lower-order terms
\(h_j\)
,
\(j\ge 1\)
, may be chosen to simultaneously guarantee (
5.11
) and (
5.13
). Working one
j
at a time, (
5.11
) prescribes the full expansion of
\(h_j(\rho _E,\rho _{\text {sf}})\)
at
\(\rho _{\text {sf}}=0\)
, and (
5.13
) prescribes the order 1 term of
\(h_j\)
at
\(\rho _E=0\)
in terms of the order-0 term of
\(h_{j-1}\)
. As long as these two requirements are consistent we are fine.
To check this, we just plug (
5.11
) into (
5.13
). After rearrangement and equating like terms, we see that we need for each
i
and
\(j>1\)
,
$$\begin{aligned} a_{ij}'(0) =\text { the coefficient of }\rho _{\text {sf}}^{i}\rho _{\text {ff}}^j\text { in }\sum _{\ell =0}^{i-1}\sum _{m=0}^{j-1}\kappa (\rho _{\text {sf}},\rho _{\text {ff}})a_{\ell ,m}(0)\rho _{\text {sf}}^{\ell +1}\rho _{\text {ff}}^{m+1}. \end{aligned}$$
(5.14)
This, in turn, is guaranteed by plugging (
5.10
) into (
5.12
), completing the proof of Lemma
5.11
.
\(\square \)
The construction of the Robin heat kernel is now analogous to the Dirichlet and Neumann cases. We solve away the error at
\(\hbox {hvlf}_j\)
and then at
\(E_{j0}\)
. When solving away the error at
\(\hbox {hvlf}_j\)
, we need to remove a term
\(r^{\gamma }a(\theta , t,z')\)
. Since
\(\partial _{\theta }=r\partial _y\)
, the coefficient
\(a(\theta ,t,z')\)
actually solves Neumann conditions, rather than Robin conditions, at
\(\theta =0\)
and
\(\theta =\alpha _j\)
. So as in the Neumann construction, the indicial equation may be solved and the solution, which has leading order
\(\gamma +2\)
at
\(\hbox {hvlf}_j\)
, may be added to our parametrix in a neighborhood of
\(\hbox {hvlf}_j\)
. Of course this does not preserve the Robin condition at
\(E_{j0}\)
. However, the error has leading order
\(\gamma +2\)
at
\(\hbox {hvlf}_j\)
, and
y
has order 1 there. If we just add back
\(\kappa y\)
times this Robin error in a neighborhood of
\(\hbox {hvlf}_j\)
, the result satisfies the Robin boundary condition. Moreover, after applying
\(t{\mathcal {L}}\)
, the result has error at worst
\((\gamma +2)+1-2=\gamma +1\)
there. So this construction may be iterated to remove the error at
\(\hbox {hvlf}_j\)
.
The error at
\(E_{j0}\)
may be eliminated in the same way as before, since adding terms at order 2 at
\(E_{j0}\)
does not affect the Robin boundary condition there. The construction of the formal Neumann series proceeds precisely as before, and yields:
Theorem 5.12
The heat kernel for
\(\Omega \)
, with Dirichlet, Neumann, or Robin boundary conditions on each side
\(E_j\)
, is pc on
\(\Omega _h^2\)
, vanishing to infinite order at tf and continuous down to all boundary hypersurfaces except for td,
\(\hbox {sf}_j\)
, and
\(\hbox {ff}_j\)
.
Its full expansion at td is (
5.6
), which is the same as that for a closed manifold.
Its full expansion at each
\(\hbox {sf}_j\)
is (
5.7
), which is identical to that for the manifold with boundary
\(\Omega _j\)
and the appropriate (Dirichlet/Neumann/Robin) boundary condition. Note that by Theorem
4.9
, at any Robin component of
\(\hbox {sf}_j\)
, the leading term is equal to the leading term for the heat kernel on
\(\Omega _j\)
with Neumann boundary conditions, the second term is
\({\mathcal {H}}_{-1,\text {sf},R}\)
, and all other terms are at order
\(T=t^{1/2}\)
.
Its expansion at each
\(\hbox {ff}_j\)
has leading term (
5.8
), with Neumann conditions at any Neumann OR Robin component, and Dirichlet conditions at any other Dirichlet component. There are no other terms within one order in
\(T=t^{1/2}\)
.
6
Heat trace on a curvilinear polygonal domain
Let
\(\Omega \)
be a curvilinear polygonal domain as defined previously, with a Dirichlet, Neumann, or Robin condition along each side. Assume any Robin parameters
\(\kappa (x)\)
are smooth along each side. In the previous section we have constructed the heat kernel for
\(\Omega \)
and shown that it is pc on
\(\Omega _h^2\)
. We now pass to the heat trace.
The first thing to do is to restrict to the diagonal. The lifted diagonal in
\(\Omega _h^2\)
is a p-submanifold and is diffeomorphic to
\(\Omega _h\)
via the lift of the map
\((t,z,z)\rightarrow (t,z)\)
. The identification of faces is hvff
\(\rightarrow \)
sv, ff
\(\rightarrow \)
pv, sf
\(\rightarrow \)
pe, td
\(\rightarrow \)
tf. Therefore, by restriction:
Proposition 6.1
The diagonal heat kernel
\(H_{\Omega }(t,z,z)\)
is pc on
\(\Omega _{h}\)
, with leading order
\(-2\)
at tf, each
\(pv_j\)
, and each
\(pe_j\)
, as well as non-negative leading orders at all other boundary hypersurfaces.
Remark 6.2
Naturally, all locality statements about the kernel still hold when it is restricted to the diagonal. For example, the expansion at tf is the same as that for a closed manifold. The expansion at
\(pe_j\)
is the same as that for a manifold with boundary. If there are any Robin edges, the expansion at the corresponding
\(pe_j\)
is the same as the Neumann expansion, plus the restriction to the diagonal of
\({\mathcal {H}}_{-1,\text {sf},R}\)
, plus terms of order zero.
Let
\(\pi _{1}\)
be the lift of the projection map from
\(\Omega _0\times [0,1)_T\)
to
\([0,1)_T\)
to a map from
\(\Omega _{h}\)
to
\([0,1)_T\)
. This map is the composition of a projection map and a blow-down map and therefore is a b-map which is a b-submersion. Since the image space has no corners it is automatically b-normal, and therefore
\(\pi _{1}\)
is a b-fibration. Thus, from the pushforward theorem:
Theorem 6.3
The heat trace
\(\operatorname {Tr}H_{\Omega }(t)\)
has a pc expansion in
\(T=t^{1/2}\)
.
We can say substantially more, and in fact can explicitly identify all terms in this expansion up to and including the
\(t^0\)
term, by carefully analyzing push-forward by this integration map. The integration is with respect to the usual measure
dz
on
\(\Omega \)
. Multiplying both sides by the canonical density
dT
, we get
$$\begin{aligned}\int _{\Omega }H_{\Omega }(T^2,z,z)\, dz\, dT=\operatorname {Tr}H_{\Omega }(T^2)\, dT.\end{aligned}$$
The density
\(dz\, dT\)
is
\(\nu (\Omega \times [0,1)_T)\)
, but it is not
\(\nu (\Omega _{h})\)
. Using an analogous process to the proof of Proposition
3.15
,
$$\begin{aligned}(\beta )^*(dz\, dT)=\rho _{\text {ff}}^2\rho _{\text {sf}}\nu (\Omega _{h}).\end{aligned}$$
So, writing integration as a push-forward by
\(\pi _{1}\)
, we obtain
$$\begin{aligned}(\pi _{1})_*(H^{\Omega }(T^2,z,z)\rho _{pv}^2\rho _{pe}\cdot \nu (\Omega _{h}))=\operatorname {Tr}H_{\Omega }(T^2)\cdot \nu ([0,1)_T).\end{aligned}$$
From this we see that we really need to understand
\(H^{\Omega }(T^2,z,z)\rho _{pv}^2\rho _{pe}\)
.
Remark 6.4
This transformation to canonical densities explains why the leading terms at
pe
and
pv
, though they both have order
\(-2\)
, only contribute at orders
\(-\,1\)
and 0 respectively to the heat trace.
Consider the function
\(H^{\Omega }(T^2,z,z)\rho _{pv}^2\rho _{pe}\)
. Its expansions are as follows:
At tf, there is an expansion in integer powers of
T
beginning with
\(T^{-2}\)
.
At
pe
, there is an expansion in integer powers of
T
beginning with
\(T^{-1}\)
.
At
pv
, there is an expansion with leading term at
\(T^0\)
which may have logarithmic terms beginning at
\(T\log T\)
.
We may say more about these expansions. Each of them is inherited from the expansion at the corresponding face in the double space. From that analysis, each term of the expansion of
\(H^{\Omega }(T^2,z,z)\)
at the face tf is
\(T^j\)
times a smooth function of
z
. Since
\(T=\rho _{\text {tf}}\rho _{pe}\rho _{pv}\)
for suitable boundary defining functions, the coefficient of the term of order
\(\rho _{\text {tf}}^j\)
at tf has leading order
j
at
pe
and at
pv
. When multiplying by
\(\rho _{pv}^2\rho _{pe}\)
, though, this coefficient has leading order
\(j+1\)
at
pe
and
\(j+2\)
at
pv
. Similarly, the order
\(\rho _{pe}^j\)
term at
pe
has leading order
\(j+1\)
at
pv
.
What this means is that no extended unions appear in the pushforward theorem. Recall that an extended union only occurs when the coefficient of a term of order
j
at one boundary hypersurface in the preimage of
\(\{t=0\}\)
itself has leading order at most
j
at an adjacent such boundary hypersurface, which may produce a term
\(t^j\log t\)
(or
\(t^j(\log t)^2\)
if all three boundary hypersurfaces are involved). The preceding discussion shows that this does not happen. So any logarithmic terms in the heat trace expansion must come from logarithmic terms at the face ff (i.e. pv), and thus arise at order
\(T^{1/2}\)
at the earliest. Therefore
$$\begin{aligned}\operatorname {Tr}H_{\Omega }(t)=a_{-1}t^{-1}+a_{-1/2}t^{-1/2}+a_0t^0+O(t^{1/2}\log t).\end{aligned}$$
Moreover, the coefficients
\(a_{-1}\)
,
\(a_{-1/2}\)
, and
\(a_0\)
are the sum of the contributions from each of the three faces tf,
pe
, and
pv
.
These contributions are easy to evaluate. At tf, the expansion is just the usual heat trace expansion from the interior of a manifold (as the coefficients are all the same), giving a contribution of
$$\begin{aligned}\frac{A(\Omega )}{4\pi t}+\frac{1}{12\pi }\int _{\Omega } K(z)\, dz+O(t).\end{aligned}$$
At
\(pe_j\)
, for the same reason, the expansion is the heat trace expansion for a manifold with boundary, giving a contribution for each edge
\(E_j\)
. The McKean–Singer asymptotics [
37
] tell us what this term must be in the Dirichlet and Neumann settings. In the Robin setting, there is an extra contribution at
\(t^0\)
coming from the integral of
\({\mathcal {H}}_{-1,\text {sf},Robin}\)
, and it is easy to see that it will be an integral of
\(\kappa (x)\)
over the boundary times a constant. From [
14
, Theorem 5.2], we know what the constant must be.
Footnote
8
All in all, the contribution from
\(pe_j\)
is, where
\(k_g(x)\)
is the geodesic curvature on the boundary,
$$\begin{aligned}  &   -\frac{\ell (E_j)}{8\sqrt{\pi }} t^{-1/2}+\frac{1}{12\pi }\int _{E_j}k_g(x)\, dx+O(t^{1/2})\text { in the Dirichlet setting;}\\  &   \quad \frac{\ell (E_j)}{8\sqrt{\pi }} t^{-1/2}+\frac{1}{12\pi }\int _{E_j}k_g(x)\, dx+O(t^{1/2})\text { in the Neumann setting;}\\  &   \quad \text { and } \frac{\ell (E_j)}{8\sqrt{\pi }} t^{-1/2}+\frac{1}{12\pi }\int _{E_j}k_g(x)\, dx-\frac{1}{2\pi }\int _{E_j}\kappa (x)\, dx+O(t^{1/2}) \end{aligned}$$
in the Robin setting. As discussed previously, at
pv
, the leading order contribution to the heat trace is at
\(T^0\)
. This reflects the fact that
rdr
lifts to
\(T^2 R dR\)
, thereby canceling the factor of
\(T^{-2}\)
. The leading order term in the expansion of the diagonal heat kernel at
pv
is the same as it is for the heat kernel on an exact sector of the same angle, and therefore may be calculated by studying the model heat kernel on that sector.
6.1
Vertex contributions
We recall our explicit calculations of the Green’s kernels for infinite circular sectors to compute the “vertex contribution” to the short time asymptotic expansion of the heat trace. For this purpose it is convenient to define:
$$\begin{aligned}  &   A:= \int _{0}^{\infty }K_{i\mu }(r \sqrt{s})K_{i\mu }(r_0 \sqrt{s}) \cosh (\pi -|\phi _0-\phi |)\mu d\mu ,\\  &   B:= \int _{0}^{\infty }K_{i\mu }(r \sqrt{s})K_{i\mu }(r_0 \sqrt{s}) \frac{\sinh \pi \mu }{\sinh \gamma \mu }\cosh (\phi +\phi _0-\gamma )\mu d\mu \\  &   C:= \int _{0}^{\infty }K_{i\mu }(r \sqrt{s})K_{i\mu }(r_0 \sqrt{s}) \frac{\sinh (\pi -\gamma )\mu }{\sinh \gamma \mu }\cosh (\phi -\phi _0)\mu d\mu ,\\  &   F:= \int _{0}^{\infty }K_{i\mu }(r \sqrt{s})K_{i\mu }(r_0 \sqrt{s})\frac{\sinh (\pi \mu )}{\cosh \gamma \mu }\sinh ((\phi +\phi _0-\gamma )\mu ) d\mu \end{aligned}$$
and
$$\begin{aligned} E:= - \int _{0}^{\infty }K_{i\mu }(r \sqrt{s})K_{i\mu }(r_0 \sqrt{s}) \frac{\cosh (\pi -\gamma )\mu }{\cosh \gamma \mu }\cosh ((\phi -\phi _0)\mu )d\mu .\end{aligned}$$
The Dirichlet and Neumann Green’s functions are, respectively,
$$\begin{aligned} G_D = \frac{1}{\pi ^2} \left( A - B + C \right) , \quad G_N = \frac{1}{\pi ^2} \left( A + B + C \right) .\end{aligned}$$
For the Dirichlet condition at
\(\phi =0\)
and Neumann condition at
\(\phi =\gamma \)
, the Green’s function is
$$\begin{aligned} \frac{1}{\pi ^2}(A+F+E). \end{aligned}$$
In [
43
, Sect. 3] we have computed the contributions of the terms
A
,
B
, and
C
to the heat trace; see also [
51
] for an earlier computation along similar lines. In particular, we computed the integral of each of these expressions, along the diagonal
\(r=r_0\)
and
\(\phi =\phi _0\)
over the region
\([0, R]_r \times [0, \gamma ]_\phi \)
with respect to polar coordinates
\((r, \phi )\)
. The vertex contribution comes solely from the
C
term in the D–D and N–N cases. There we see that the C term contributes to the heat trace [
43
, Sect. 3.1.3]
$$\begin{aligned} \frac{\pi ^2 - \gamma ^2}{24\pi \gamma }. \end{aligned}$$
(6.1)
In the D–N case, the vertex contribution arises from the terms F and E.
6.1.1
Contribution from the
F
term
Let us make some manipulations
$$\begin{aligned}  &   \frac{\sinh (\pi \mu )}{\cosh \gamma \mu }\sinh ((\phi +\phi _0-\gamma )\mu ) \\  &   \quad = \frac{\sinh (\pi \mu )}{\cosh \gamma \mu }\sinh ((\phi +\phi _0-\gamma )\mu ) -\frac{\sinh (\pi \mu )}{\sinh \gamma \mu }\cosh ((\phi +\phi _0-\gamma )\mu )\\  &   \qquad +\frac{\sinh (\pi \mu )}{\sinh \gamma \mu }\cosh ((\phi +\phi _0-\gamma )\mu )\\  &   \quad =\frac{\sinh ((\phi +\phi _0-\gamma )\mu )\sinh \gamma \mu -\cosh ((\phi +\phi _0-\gamma )\mu )\cosh \gamma \mu }{\sinh \gamma \mu \cosh \gamma \mu }\sinh (\pi \mu )\\  &   \qquad +\frac{\sinh (\pi \mu )}{\sinh \gamma \mu }\cosh ((\phi +\phi _0-\gamma )\mu ). \end{aligned}$$
This expression simplifies to:
$$\begin{aligned} \begin{aligned}&-\frac{2\sinh (\pi \mu )}{\sinh (2\gamma \mu )}\cosh ((\phi +\phi _0-2\gamma )\mu )+\frac{\sinh (\pi \mu )}{\sinh \gamma \mu }\cosh ((\phi +\phi _0-\gamma )\mu )=:-2B_1+B_2. \end{aligned} \end{aligned}$$
By the calculation of the trace of the
B
term in [
43
, Sect. 3], the contribution of
\(B_2\)
is
\(\frac{R}{4\sqrt{\pi t}}+O(\sqrt{t})\)
. Next we note that, for
\(\phi =\phi _0\)
,
$$\begin{aligned} \int _{0}^{\gamma }B_1d\phi =\frac{\sinh \pi \mu }{2\mu }=\int _{0}^{\gamma }B_2d\phi . \end{aligned}$$
Hence the contributions of
\(B_1\)
and
\(B_2\)
are the same, so that
F
contributes
$$\begin{aligned} -2\frac{R}{4\sqrt{\pi t}}+\frac{R}{4\sqrt{\pi t}}+O(\sqrt{t})=-\frac{R}{4\sqrt{\pi t}}+O(\sqrt{t}). \end{aligned}$$
(6.2)
Consequently, this gives no contribution because the coefficient of
\(t^0\)
vanishes.
6.1.2
Contribution from the
E
term
Finally, we study the term
E
. We need to compute
$$\begin{aligned} -\frac{1}{\pi ^2}\int _{0}^{\infty }K_{i\mu }(r\sqrt{s})K_{i\mu }(r_0\sqrt{s})\frac{\cosh (\pi -\gamma )\mu }{\cosh \gamma \mu }\cosh ((\phi -\phi _0)\mu ) d\mu \end{aligned}$$
This is similar to the computation of the
C
term, which we would like to recycle. Hence, we add and subtract:
$$\begin{aligned}  &   -\frac{\cosh (\pi -\gamma )\mu }{\cosh \gamma \mu }\cosh ((\phi -\phi _0)\mu ) +\frac{\sinh (\pi -\gamma )\mu }{\sinh \gamma \mu }\cosh ((\phi -\phi _0)\mu )\\  &   -\frac{\sinh (\pi -\gamma )\mu }{\sinh \gamma \mu }\cosh ((\phi -\phi _0)\mu )\\  &   \quad =\frac{-\cosh (\pi -\gamma )\mu \sinh \gamma \mu +\sinh (\pi -\gamma )\mu \cosh \gamma \mu }{\sinh \gamma \mu \cosh \gamma \mu }\cosh ((\phi -\phi _0)\mu )\\  &   \quad \quad -\frac{\sinh (\pi -\gamma )\mu }{\sinh \gamma \mu }\cosh ((\phi -\phi _0)\mu ). \end{aligned}$$
This reduces to:
$$\begin{aligned} \begin{aligned} \frac{2\sinh (\pi -2\gamma )\mu }{\sinh (2\gamma \mu )}\cosh ((\phi -\phi _0)\mu )- \frac{\sinh (\pi -\gamma )\mu }{\sinh \gamma \mu }\cosh ((\phi -\phi _0)\mu )=:2C_1-C_2. \end{aligned} \end{aligned}$$
We recognize the term
$$\begin{aligned} \int _0 ^\infty K_{i\mu }(r\sqrt{s})K_{i\mu }(r_0\sqrt{s}) C_2 d\mu = C. \end{aligned}$$
Consequently, we already know the contribution to the trace from
\(C_2\)
, because it is the same as that which we computed for
C
$$\begin{aligned} \frac{\gamma }{2\pi }\cdot \frac{\pi ^2-\gamma ^2}{12\gamma ^2} + O(t^\infty ), \quad t \downarrow 0. \end{aligned}$$
The reason we write it in this way is to recall the differences between the contributions of
\(C_1\)
and
\(C_2\)
. The factor of
\(\gamma \)
in
\(\frac{\gamma }{2\pi }\)
comes from the trace calculation in which we integrate the angular coordinate over
\((0,\gamma )\)
. This factor is therefore the same in
\(C_1\)
. Hence when we consider
\(C_1\)
, we just need to change
\(\gamma \)
to
\(2\gamma \)
in the second factor only. The contribution of
\(C_1\)
is
$$\begin{aligned} \frac{\gamma }{2\pi }\cdot \frac{\pi ^2-(2\gamma )^2}{12(2\gamma )^2}, \end{aligned}$$
and hence the trace contribution of
E
is
$$\begin{aligned} \frac{\pi ^2-4\gamma ^2}{48\pi \gamma }-\frac{\pi ^2-\gamma ^2}{24\pi \gamma }=-\frac{\pi ^2+2\gamma ^2}{48\pi \gamma } + O(t^\infty ). \end{aligned}$$
(6.3)
We have now computed the contribution of the vertex to the
\(t^0\)
term. Any Robin–Dirichlet, or Robin–Neumann, or Robin–Robin corner is treated as if the Robin conditions were Neumann conditions, as the corresponding models at
\(\hbox {ff}_{diag,j}\)
are the same.
The vertex contribution for an interior angle of
\(\gamma \)
is therefore:
$$\begin{aligned} \frac{\pi ^2 - \gamma ^2}{24 \pi \gamma } \text { for D}{-}\hbox {D}, \hbox {N}{-}\hbox {N}, \hbox {R}--\hbox {R}, \hbox {and N}{-}\hbox {R boundary conditions} \end{aligned}$$
(6.4)
or
$$\begin{aligned} -\frac{\pi ^2+2\gamma ^2}{48\pi \gamma } \text { for }\hbox {D}{-}\hbox {N and D}{-}\hbox {R mixed boundary conditions.} \end{aligned}$$
(6.5)
The vertex contribution (
6.5
) appears to be new and may be of independent interest. In §
B
we show how, given the D–D corner contribution, one may also use the more familiar series expression for the heat kernel as in [
6
] to compute the N–N and D–N corner contribution. The result is of course the same as we have computed here. In summary, we have Theorem
1.2
.
Remark 6.5
The Gauss–Bonnet theorem dictates that
$$\begin{aligned} 2\pi \chi (\Omega )=\int _{\Omega }K(z)\, dz+\int _{\partial \Omega }k_g(x)\, dx+\sum _{j=1}^n(\pi -\alpha _j), \end{aligned}$$
where
\(\chi (\Omega )\)
is the Euler characteristic of
\(\Omega \)
. This yields an alternate expression for
\(a_0\)
:
$$\begin{aligned} a_0&= \frac{1}{6}\chi (\Omega )-\frac{1}{12\pi }\sum _{j=1}^{n}(\pi -\alpha _j) - \frac{1}{2\pi }\sum _{j\in {\mathcal {E}}_R}\int _{E_j}\kappa _j(x)\, dx \\&\quad +\sum _{j\in V_{=}}\frac{\pi ^2-\alpha _j^2}{24\pi \alpha _j}+\sum _{j\in V_{\ne }}\frac{-\pi ^2-2\alpha _j^2}{48\pi \alpha _j}. \end{aligned}$$
Remark 6.6
It is straightforward to allow for surfaces which may also have isolated conical singularities. An isolated conical singularity with opening angle
\(2\alpha \)
will give contribute to the heat trace:
$$\begin{aligned} \frac{\pi ^2 - \alpha ^2}{12 \pi \alpha }. \end{aligned}$$
6.2
Vertices as spectral invariants
Here we apply our results, presenting several contexts in which the presence, or lack, of vertices is spectrally determined. We also show that a jump in boundary condition is spectrally determined.
Theorem 6.7
Let
\(\Sigma \)
be a surface with at least one vertex with interior angle not equal to
\(\pi \)
and either the Dirichlet boundary condition or the Neumann boundary condition. Let
\(\Omega \)
be a smoothly bounded surface with either the Dirichlet boundary condition or the Neumann boundary condition such that
\(\chi (\Omega ) \le \chi (\Sigma )\)
. Then
\(\Sigma \)
and
\(\Omega \)
are not isospectral.
Proof
It suffices to compare the short time asymptotic expansion of the heat traces and demonstrate that the coefficients cannot be the same for
\(\Sigma \)
and
\(\Omega \)
. The coefficient
\(a_0\)
for
\(\Sigma \)
is:
$$\begin{aligned} a_0 (\Sigma ) = \frac{\chi (\Sigma )}{6} - \frac{1}{12\pi } \sum _{j=1} ^n (\pi - \alpha _j) + \sum _{j=1} ^n \frac{\pi ^2 - \alpha _j^2}{24 \pi \alpha _j}, \end{aligned}$$
where
\(\Sigma \)
has
n
vertices with interior angles
\(\alpha _j\)
. This expression simplifies to:
$$\begin{aligned} a_0 (\Sigma ) = \frac{\chi (\Sigma )}{6} - \frac{n}{12} + \sum _{j=1} ^n \frac{\pi ^2 + \alpha _j ^2}{24 \pi \alpha _j}. \end{aligned}$$
On the other hand,
$$\begin{aligned} a_0 (\Omega ) = \frac{\chi (\Omega )}{6} \le \frac{\chi (\Sigma )}{6}. \end{aligned}$$
Since at least one
\(\alpha _j \ne \pi \)
, it is a straightforward exercise in multivariable analysis [
31
] to demonstrate the strict inequality
$$\begin{aligned} a_0 (\Sigma ) > \frac{\chi (\Sigma )}{6} \ge \frac{\chi (\Omega )}{6} = a_0(\Omega ). \end{aligned}$$
\(\square \)
We obtain a similar result for the Robin boundary condition. Recall the Robin boundary condition is,
$$\begin{aligned} u = \kappa \frac{\partial u}{\partial \nu }, \quad \text { on all smooth boundary components,} \quad \kappa \ge 0. \end{aligned}$$
Above,
\(\frac{\partial u}{\partial \nu }\)
is the
inward
pointing unit normal, as in (
4.17
).
Theorem 6.8
Let
\(\Sigma \)
be a surface with at least one vertex with interior angle not equal to
\(\pi \)
with the Robin boundary condition as above, with constant Robin parameter. Let
\(\Omega \)
be a smoothly bounded surface with
\(\chi (\Omega ) \le \chi (\Sigma )\)
. Assume the same Robin boundary condition on
\(\partial \Omega \)
. Then
\(\Sigma \)
and
\(\Omega \)
are not isospectral.
Proof
We argue by contradiction. Assume that
\(\Sigma \)
and
\(\Omega \)
are isospectral. Then, they must have the same heat trace coefficients. The terms
\(a_{-1/2}(\Sigma )\)
and
\(a_{-1/2} (\Omega )\)
show that the boundaries of
\(\Omega \)
and
\(\Sigma \)
have the same length. Hence, since at least one of the angles
\(\alpha _j\)
is not equal to
\(\pi \)
, we have
$$\begin{aligned} a_0 (\Sigma ) = \frac{\chi (\Sigma )}{6} - \frac{n}{12} + \sum _{j=1} ^n \frac{\pi ^2 + \alpha _j^2}{24 \pi \alpha _j}- \frac{\kappa |\partial \Sigma |}{2\pi } > \frac{\chi (\Sigma )}{6} - \frac{\kappa |\partial \Sigma |}{2\pi }.\end{aligned}$$
Above,
\(|\partial \Sigma |\)
is the length of the boundary of
\(\Sigma \)
,
n
is the number of vertices, and
\(\alpha _j\)
is the interior angle at the
\(j^{th}\)
vertex. On the other hand
$$\begin{aligned} a_0(\Omega ) = \frac{\chi (\Omega )}{6} - \frac{\kappa |\partial \Omega |}{2\pi } = \frac{\chi (\Omega )}{6} - \frac{\kappa |\partial \Sigma |}{2\pi } < a_0(\Sigma ).\end{aligned}$$
This is the desired contradiction.
\(\square \)
For the case of smoothly bounded surfaces, the spectrum also detects a jump in the boundary condition, even without vertices. This is depicted in Fig.
8
.
Fig. 8
Full size image
For a circular domain, impose the Dirichlet boundary on the red arc and the Neumann boundary on the black arc, taking the Friedrichs extension at the intervace. Such a domain is not isospectral to any simply connected smoothly bounded domain which has either the Dirichlet or Neumann condition (but not mixed). In fact, one may take the red and black pieces of the boundary to be of
any
proportions, not necessarily equal
Theorem 6.9
Let
\(\Sigma \)
be a smoothly bounded surface which has Dirichlet boundary condition and Neumann boundary condition on a single boundary component (that is, a nontrivial Zaremba boundary condition), with a Friedrichs extension at the interface. Let
\(\Omega \)
be a smoothly bounded surface which has either Neumann or Dirichlet boundary condition (not mixed). Assume that
$$\begin{aligned} \chi (\Omega ) \ge \chi (\Sigma ). \end{aligned}$$
Then
\(\Sigma \)
and
\(\Omega \)
are not isospectral.
Proof
For
\(\Sigma \)
, the heat trace coefficient
$$\begin{aligned} a_0 (\Sigma ) = \frac{\chi (\Sigma )}{6} - \frac{n}{16}, \end{aligned}$$
where
n
is the number of times the boundary condition jumps between Dirichlet and Neumann. We obtain this because the boundary is smooth, and hence the angle at the “vertex” where the boundary condition jumps is equal to
\(\pi \)
. On the other hand,
$$\begin{aligned} a_0 (\Omega ) \ge \frac{\chi (\Omega )}{6} \ge \frac{\chi (\Sigma )}{6} > a_0 (\Sigma ), \end{aligned}$$
since
\(n\ge 1\)
.
\(\square \)
In conclusion, we determine contexts in which entirely mixed Dirichlet–Neumann vertices are spectrally determined. In particular, this shows that we may distinguish between the presence of mixed-boundary condition vertices versus vertices with the same boundary condition on both sides; see Fig.
9
.
Theorem 6.10
Assume that
\(\Sigma \)
is a surface with vertices with mixed Dirichlet and Neumann boundary condition such that each vertex has Dirichlet on one side and Neumann on the other side. Moreover, assume that all interior angles are less than
\(\frac{\pi }{\sqrt{2}}\)
. Let
\(\Omega \)
be any surface which is either:
1.
smoothly bounded and with either the Dirichlet or Neumann, but not mixed, boundary condition;
2.
a surface with vertices with either the Dirichlet or Neumann, but not mixed, boundary condition.
Assume further that
\(\chi (\Sigma ) \le \chi (\Omega )\)
. Then
\(\Sigma \)
and
\(\Omega \)
are not isospectral.
Proof
We compute the heat trace coefficient for
\(\Sigma \)
,
$$\begin{aligned}a_0 (\Sigma ) = \frac{\chi (\Sigma )}{6} - \frac{n}{12} + \sum _{j=1} ^n \frac{-\pi ^2 + 2 \alpha _j^2}{48\pi \alpha _j}.\end{aligned}$$
Above,
n
is the number of vertices, and
\(\alpha _j\)
is the interior angle at the
\(j^{th}\)
vertex. By the assumption that
\(\alpha _j < \frac{\pi }{\sqrt{2}}\)
for all
j
we have
$$\begin{aligned}a_0 (\Sigma ) < \frac{\chi (\Sigma )}{6} - \frac{n}{12}.\end{aligned}$$
On the other hand, if
\(\Omega \)
has smooth boundary and Dirichlet or Neumann boundary condition (not mixed), we have
$$\begin{aligned}a_0 (\Omega ) \ge \frac{\chi (\Omega )}{6} \ge \frac{\chi (\Sigma )}{6} > a_0 (\Sigma ).\end{aligned}$$
This shows that
\(\Sigma \)
and
\(\Omega \)
are not isospectral.
In case
\(\Omega \)
has
m
vertices, and a single fixed boundary condition then
$$\begin{aligned}a_0 (\Omega ) \ge \frac{\chi (\Omega )}{6} - \frac{n}{12} + \sum _{j=1} ^m \frac{\pi ^2 + \beta _j^2}{24 \pi \beta _j}.\end{aligned}$$
Here the interior angle at the
\(j^{th}\)
vertex is
\(\beta _j\)
. By the assumption that
\(\Omega \)
has vertices, at least one
\(\beta _j \ne \pi \)
, and therefore
$$\begin{aligned}a_0 (\Omega ) > \frac{\chi (\Omega )}{6} \ge a_0 (\Sigma ).\end{aligned}$$
Consequently,
\(\Sigma \)
and
\(\Omega \)
are not isospectral.
\(\square \)
We conclude with a familiar example which satisfies the hypotheses of the preceding theorem. Let us consider domains in the plane which do not have holes. Let
\(\Sigma \)
be a rectangular domain with the Dirichlet boundary condition on two opposite sides, and Neumann boundary condition on the other two sides; see Fig.
9
. Then, the interior angles are all equal to
\(\frac{\pi }{2} < \frac{\pi }{\sqrt{2}}\)
. Consequently, the theorem shows that such a domain is not isospectral to
any
smoothly bounded domain with either Dirichlet or Neumann (but not mixed) boundary condition, nor is it isospectral to
any
domain with corners but which has a single fixed boundary condition, either Dirichlet or Neumann. An analogous result holds for any polygonal domain which has an even number of sides and alternating Dirichlet and Neumann boundary conditions, such that the interior angles do not exceed
\(\frac{\pi }{\sqrt{2}}\)
.
Fig. 9
Full size image
For a rectangular domain we impose the Dirichlet boundary condition on the red sides and Neumann boundary condition on the black sides
Data availability
There are no data sets or data for this article.
Notes
A boundary hypersurface will often be referred to as a boundary face or face. A “side face” is a boundary hypersurface arising from the boundary in
\(\Omega \)
. This is in contrast to the
tf
face as well as to the boundary hypersurfaces created by blowing up along
p
-submanifolds.
In the notation
\(M_h\)
for the single heat space,
M
acts as a place-holder for the various model geometries we shall use to construct the heat kernel on our surface
\(\Omega \)
(the analogous notation is used for the double and triple heat spaces) (Fig.
2
).
Some authors reverse the roles of “right” and “left” here—our terminology is chosen to match [
35
].
This is different from [
35
]. It may be that only the blow-ups with
\(j=k\)
are necessary, but doing all of them makes the proof of the composition theorem easier to read.
In general, the operator kernel would be pc on
\(M^2 _h\)
but not on
\(M^2 _{rh}\)
.
See in particular the comment after the proof in [
19
]; in this case
\(\Pi _C\)
restricts to a b-fibration from
\({\mathcal {O}}_{VVV}\)
onto ff and also from
\({\mathcal {O}}_{EEE}\)
onto sf, which is sufficient.
Note that even though
\(\Omega \)
with the usual metric is not technically a manifold with corners, the same analysis works to write
\(\nu (\Omega )\)
in terms of
\(\nu (\Omega _0)\)
.
An expression for this term also appears in [
54
]. However, it differs by an overall sign from the expression in [
14
]. A direct computation due to Félix Houde [
20
] indicates that the reference [
14
] has the correct sign.
References
Pierre Albin, Frédéric Rochon, and David Sher,
Analytic torsion and R-torsion of Witt representations on manifolds with cusps
, Duke Math. J.
167
(2018), no. 10, 1883–1950.
Article
MathSciNet
Google Scholar
Clara L. Aldana and Julie Rowlett,
A Polyakov formula for sectors
, J. Geom. Anal.
28
(2018), no. 2, 1773–1839.
Article
MathSciNet
Google Scholar
J. S. Apps and J. S. Dowker,
The
\(C_2\)
heat-kernel coefficient in the presence of boundary discontinuities
, Classical Quantum Gravity
15
(1998), no. 5, 1121–1139.
Ivan G. Avramidi,
Heat kernel asymptotics of Zaremba boundary value problem
, Math. Phys. Anal. Geom.
7
(2004), no. 1, 9–46.
Article
MathSciNet
Google Scholar
J. D. Bondurant and S. A. Fulling,
The Dirichlet-to-Robin transform
, J. Phys. A
38
(2005), no. 7, 1505–1532.
Article
MathSciNet
Google Scholar
Jeff Cheeger,
Spectral geometry of singular Riemannian spaces
, J. Differential Geom.
18
(1983), no. 4, 575–657 (1984).
Monique Dauge,
Neumann and mixed problems on curvilinear polyhedra
, Integral Equations Operator Theory
15
(1992), no. 2, 227–261.
Article
MathSciNet
Google Scholar
Monique Dauge,
Singularities of corner problems and problems of corner singularities
, Actes du 30ème Congrès d’Analyse Numérique: CANum ’98 (Arles, 1998), ESAIM Proc., vol. 6, Soc. Math. Appl. Indust., Paris, 1999, pp. 19–40.
B. V. Fedosov,
Asymptotic formulae for the eigenvalues of the Laplace operator in the case of a polygonal domain
, Dokl. Akad. Nauk SSSR
151
(1963), 786–789.
MathSciNet
Google Scholar
Boris Fedosov,
Asymptotic formulas for eigenvalues of the laplacian in a polyhedron
, Doklady Akad. Nauk SSSR
157
(1964), 536–538.
MathSciNet
Google Scholar
Rupert L. Frank and Leander Geisinger,
Semi-classical analysis of the Laplace operator with Robin boundary conditions
, Bull. Math. Sci.
2
(2012), no. 2, 281–319.
Article
MathSciNet
Google Scholar
Juan B. Gil,
Full asymptotic expansion of the heat trace for non-self-adjoint elliptic cone operators
, Math. Nachr.
250
(2003), 25–57.
Article
MathSciNet
Google Scholar
Juan B. Gil and Paul A. Loya,
Resolvents of cone pseudodifferential operators, asymptotic expansions and applications
, Math. Z.
259
(2008), no. 1, 65–95.
Article
MathSciNet
Google Scholar
Peter Gilkey,
The spectral geometry of operators of Dirac and Laplace type
, in Handbook of Global Analysis, Elsevier Sci. B. V. Amsterdam (2008), 289–326.
I. S. Gradshteyn and I. M. Ryzhik,
Table of integrals, series, and products
, eighth ed., Elsevier/Academic Press, Amsterdam, 2015, Translated from the Russian, Translation edited and with a preface by Daniel Zwillinger and Victor Moll, Revised from the seventh edition [MR2360010].
Daniel Grieser,
Basics of the
\(b\)
-
calculus
, Approaches to singular analysis (Berlin, 1999), Oper. Theory Adv. Appl., vol. 125, Birkhäuser, Basel, 2001, pp. 30–84.
Pierre Grisvard,
Elliptic problems in nonsmooth domains
, Classics in Applied Mathematics, vol. 69, Society for Industrial and Applied Mathematics (SIAM), Philadelphia, PA, 2011, Reprint of the 1985 original [ MR0775683], With a foreword by Susanne C. Brenner.
Andrew Hassell,
Analytic surgery and analytic torsion
, Comm. Anal. Geom.
6
(1998), no. 2, 255–289.
Article
MathSciNet
Google Scholar
Andrew Hassell, Rafe Mazzeo, and Richard B. Melrose,
Analytic surgery and the accumulation of eigenvalues
, Comm. Anal. Geom.
3
(1995), no. 1-2, 115–222.
Article
MathSciNet
Google Scholar
Félix Houde, private communication (2021).
Dmitry Jakobson, Michael Levitin, Nikolai Nadirashvili, and Iosif Polterovich,
Spectral problems with mixed Dirichlet–Neumann boundary conditions: isospectrality and beyond
, J. Comput. Appl. Math.
194
(2006), no. 1, 141–155.
Article
MathSciNet
Google Scholar
Mark Kac,
Can one hear the shape of a drum?
, Amer. Math. Monthly
73
(1966), no. 4, part II, 1–23.
D. Kapanadze and B.-W. Schulze,
Symbolic calculus for boundary value problems on manifolds with edges
, Integral Equations Operator Theory
45
(2003), no. 1, 64–104.
Article
MathSciNet
Google Scholar
A. I. Karol’,
Asymptotics of the parabolic Green function for an elliptic operator on a manifold with conical points
, Mat. Zametki
63
(1998), no. 1, 28–36.
MathSciNet
Google Scholar
Tosio Kato,
Perturbation theory for linear operators
, second ed., Springer-Verlag, Berlin, 1976, Grundlehren der Mathematischen Wissenschaften, Band 132.
A. Kokotov and D. Korotkin,
Tau-functions on spaces of Abelian differentials and higher genus generalization of Ray–Singer formula
, J. Diff. Geom.
82
(2009), 35–100.
MathSciNet
Google Scholar
V. A. Kozlov,
Asymptotic behavior as
\(t\rightarrow 0\)
of the solutions of the heat equation in a domain with a conic point
, Mat. Sb. (N.S.)
136(178)
(1988), no. 3, 384–395, 431.
Michael Levitin, Leonid Parnovski, and Iosif Polterovich,
Isospectral domains with mixed boundary conditions
, J. Phys. A
39
(2006), no. 9, 2073–2082.
Article
MathSciNet
Google Scholar
Paul Loya,
Asymptotic properties of the heat kernel on conic manifolds
, Israel J. Math.
136
(2003), 285–306.
Article
MathSciNet
Google Scholar
Paul Loya,
Complex powers of differential operators on manifolds with conical singularities
, J. Anal. Math.
89
(2003), 31–56.
Article
MathSciNet
Google Scholar
Zhiqin Lu and Julie M. Rowlett,
One can hear the corners of a drum
, Bull. Lond. Math. Soc.
48
(2016), no. 1, 85–93.
Article
MathSciNet
Google Scholar
W. Lück and T. Schick,
\(L^2\)
-
torsion of hyperbolic manifolds of finite volume
, Geom. Funct. Anal.
9
(1999), no. 3, 518–567.
Rafe Mazzeo,
Elliptic theory of differential edge operators. I
, Comm. Partial Differential Equations
16
(1991), no. 10, 1615–1664.
Article
MathSciNet
Google Scholar
Rafe Mazzeo and Julie Rowlett,
A heat trace anomaly on polygons
, Math. Proc. Cambridge Philos. Soc.
159
(2015), no. 2, 303–319.
Article
MathSciNet
Google Scholar
Rafe Mazzeo and Boris Vertman,
Analytic torsion on manifolds with edges
, Adv. Math.
231
(2012), no. 2, 1000–1040.
Article
MathSciNet
Google Scholar
A. McIntosh,
Operators which have an
\(h_{\infty }\)
functional calculus, miniconference on operator theory and partial differential equations
, Proc. Centre Math. Anal. Austral. Nat. Univ.
14
(1986), 210–231.
H. P. McKean, Jr. and I. M. Singer,
Curvature and the eigenvalues of the Laplacian
, J. Differential Geometry
1
(1967), no. 1, 43–69.
MathSciNet
Google Scholar
Richard B. Melrose,
Differential analysis on manifolds with corners
, Book in preparation.
Richard B. Melrose,
Calculus of conormal distributions on manifolds with corners
, Internat. Math. Res. Notices (1992), no. 3, 51–61.
Richard B. Melrose,
The Atiyah–Patodi–Singer index theorem
, Research Notes in Mathematics, vol. 4, A K Peters, Ltd., Wellesley, MA, 1993.
Google Scholar
Edith A. Mooers,
Heat kernel asymptotics on manifolds with conic singularities
, J. Anal. Math.
78
(1999), 1–36.
V. V. Nesterenko, I. G. Pirozhenko, and J. Dittrich,
Non-smoothness of the boundary and the relevant heat kernel coefficients
, Classical Quantum Gravity
20
(2003), no. 3, 431–455.
Article
MathSciNet
Google Scholar
M. Nursultanov, J. Rowlett & D. Sher
How to hear the corners of a drum
, Matrix Annals Book Series (2018).
Åke Pleijel,
A study of certain Green’s functions with applications in the theory of vibrating membranes
, Ark. Mat.
2
(1954), 553–569.
Article
MathSciNet
Google Scholar
Luca Raimondi,
Self-adjoint extensions for symmetric laplacians on polygons
, 2012, PhD Thesis, Universita degli studi dell’Insubria.
R. Seeley,
Heat kernel expansions in the case of conic singularities
, Proceedings of the Second International Winter School on Mathematical Methods in Physics (Londrina, 2002), vol. 18, 2003, pp. 2197–2203.
Robert Seeley,
Trace expansions for the Zaremba problem
, Comm. Partial Differential Equations
27
(2002), no. 11-12, 2403–2421.
Article
MathSciNet
Google Scholar
Mindaugas Skujus and Vytenis Šumskas,
Asymptotics of a solution to the time-periodic heat equation set in domains with corner points
, Lith. Math. J.
56
(2016), no. 4, 552–571.
Article
MathSciNet
Google Scholar
Eren Ucar,
Spectral invariants for polygons and orbisurfaces
, 2017, PhD Thesis, Humboldt Universität zu Berlin.
Boris Vaillant,
Index- and spectral theory for manifolds with generalized fibred cusps
, Bonner Mathematische Schriften [Bonn Mathematical Publications], vol. 344, Dissertation, Rheinische Friedrich-Wilhelms-Universität Bonn, Bonn, 2001.
M. van den Berg and S. Srisatkunarajah,
Heat equation for a region in
\({\bf R}^2\)
with a polygonal boundary
, J. London Math. Soc. (2)
37
(1988), no. 1, 119–127.
Hermann Weyl,
Das asymptotische Verteilungsgesetz der Eigenwerte linearer partieller Differentialgleichungen (mit einer Anwendung auf die Theorie der Hohlraumstrahlung)
, Math. Ann.
71
(1912), no. 4, 441–479.
Article
MathSciNet
Google Scholar
Jürgen Jost,
Partial Differential Equations
Third edition. Graduate Texts in Mathematics, 214. Springer, New York, 2013. xiv+410 pp. ISBN: 978-1-4614-4808-2; 978-1-4614-4809-9 35-01
E. M. E. Zayed,
Short-time asymptotics of the heat kernel of the Laplacian of a bounded domain with Robin boundary conditions
, Houston J. Math.
24
(1998), no. 2, 377–385.
MathSciNet
Google Scholar
Download references
Acknowledgements
The authors are deeply grateful to Daniel Grieser for his insightful comments on an early draft of this manuscript, and would also like to thank Félix Houde, Rafe Mazzeo, Richard Melrose, and Iosif Polterovich for helpful conversations. Thanks also to the anonymous referee for a careful reading of the paper, which led to significant improvements. We are grateful to Noémie Legout for suggestions to improve our French abstract. The first author was partially supported by the Ministry of Education and Science of the Republic of Kazakhstan under grant AP22683207. The first author was also supported by the Government of Kazakhstan and the World Bank under Grant APP-PHD-A-18/013P financed by the project “Fostering productive innovation”. The second author is supported by the Swedish Research Council Grant, 2018-03873 (GAAME). The third author was partially supported by a Grant from the College of Science and Health at DePaul University.
Funding
Open access funding provided by Chalmers University of Technology.
Author information
Authors and Affiliations
Department of Mathematics and Statistics, University of Helsinki, Helsinki, Finland
Medet Nursultanov
Institute of Mathematics and Mathematical Modeling, Almaty, Kazakhstan
Medet Nursultanov
Mathematical Sciences, Chalmers University and the University of Gothenburg, 412 96, Gothenburg, Sweden
Julie Rowlett
Department of Mathematical Sciences, DePaul University, 2320 N Kenmore Ave, Chicago, IL, 60614, USA
David Sher
Authors
Medet Nursultanov
View author publications
Search author on:
PubMed
Google Scholar
Julie Rowlett
View author publications
Search author on:
PubMed
Google Scholar
David Sher
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
Appendices
Calculation of the Green’s function for Dirichlet, Neumann, and mixed Dirichlet–Neumann boundary conditions
Here we will explain how to obtain the explicit expression for the Green’s functions introduced in Sect.
2.1
. Inspired by Fedosov [
10
], we consider the Kontorovich–Lebedev transform
$$\begin{aligned} F(x)=\int _{0}^{\infty }K_{ix}(z) f(z) \frac{dz}{z} \end{aligned}$$
and its inverse transform
$$\begin{aligned} f(y)=\frac{2}{\pi ^2}\int _{0}^{\infty }x\sinh (\pi x)K_{ix}(y)F(x)dx. \end{aligned}$$
Above,
\(K_\nu \)
is the modified Bessel function of second kind. At least formally
$$\begin{aligned} f(r_0 \sqrt{s} )=\int _{0}^{\infty }\frac{2}{\pi ^2r}\int _{0}^{\infty }x\sinh (\pi x)K_{ix}(r \sqrt{s})K_{ix}(r_0 \sqrt{s})dx\cdot f(r \sqrt{s})dr. \end{aligned}$$
Hence, in the distributional sense we obtain
$$\begin{aligned} \frac{2}{\pi ^2r}\int _{0}^{\infty }x\sinh (\pi x)K_{ix}(r\sqrt{s})K_{ix}(r_0\sqrt{s})dx=\delta (r-r_0). \end{aligned}$$
(A.1)
We will search for the Green’s function of the following form
\(G(s,r,\phi ,r_0,\phi _0)=\)
$$\begin{aligned} \frac{2}{\pi ^2}\int _{0}^{\infty }K_{i\mu }(r\sqrt{s})K_{i\mu }(r_0\sqrt{s})\mu \sinh (\pi \mu )\Phi (\mu ,\phi ,\phi _0)d\mu . \end{aligned}$$
(A.2)
Inserting (
A.2
) into (
2.1
) and using the definition of
\(K_\nu \)
, we want to solve:
$$\begin{aligned}  &   \frac{2}{\pi ^2}\int _{0}^{\infty }K_{i\mu }(r \sqrt{s})K_{i\mu }(r_0 \sqrt{s})\mu \sinh (\pi \mu )\frac{1}{r^2}\left[ -(i\mu )^2\Phi (\mu ,\phi ,\phi _0)-\Phi ''(\mu ,\phi ,\phi _0)\right] d\mu \\  &   \quad =\frac{1}{r}\delta (r-r_0)\delta (\phi -\phi _0). \end{aligned}$$
By (
A.1
), it will suffice to find
\(\Phi \)
such that
$$\begin{aligned}  &   -(i\mu )^2\Phi (\mu ,\phi ,\phi _0)-\Phi ''(\mu ,\phi ,\phi _0)=\delta (\phi -\phi _0), \nonumber \\  &   \quad \alpha \Phi (0)+\beta \Phi '(0)=0, \quad \alpha \Phi (\gamma )+\beta \Phi '(\gamma )=0, \end{aligned}$$
(A.3)
with either
\(\alpha =1\)
and
\(\beta = 0\)
or
\(\alpha = 0\)
and
\(\beta = 1\)
. Solving the first case will yield (
2.2
), and the second case will yield (
2.3
). For this purpose, we note that
$$\begin{aligned} \Phi _1(\phi ):=\alpha \sinh \phi \mu -\mu \beta \cosh \phi \mu , \quad \Phi _2(\phi ):=\alpha \sinh (\phi -\gamma )\mu -\mu \beta \cosh (\phi -\gamma )\mu \end{aligned}$$
are solutions of (
A.3
) and satisfy the first and second boundary conditions, respectively. Hence, the Green’s function is obtained by inserting
$$\begin{aligned} \Phi :=-\frac{\Phi _1(\phi )\Phi _2(\phi _0)}{W(\Phi _1,\Phi _2)}, \qquad \text {for }\phi <\phi _0, \end{aligned}$$
(A.4)
into (
A.2
) where above
\(W(\Phi _1,\Phi _2)\)
is the Wronskian of
\(\Phi _1\)
and
\(\Phi _2\)
.
Similarly, with the Dirichlet–Neumann mixed boundary condition, the Green’s function is of the form (
A.2
), but in this case
\(\Phi \)
solves
$$\begin{aligned} -\Phi ''+\mu ^2\Phi =0, \qquad \Phi (0)=0, \qquad \Phi '(\gamma )=0. \end{aligned}$$
Now defining
$$\begin{aligned} \Phi _1(\phi ):=\sinh (\phi \mu ), \qquad \Phi _2(\phi ):=\cosh ((\phi -\gamma )\mu ) \end{aligned}$$
the Green’s function is obtained from (
A.4
) inserted into (
A.2
).
The corner contribution using Cheeger’s series expression for the heat kernel on an infinite sector
Here we show how, given the contribution for a D–D corner, which has been computed in [
43
,
51
], we may use the series expression of the heat kernel from [
6
] to compute the contribution for both N–N and D–N corners. For a corner of angle
\(\alpha \)
, the corner contribution is obtained by computing the renormalized integral, (see also [
18
,
19
])
$$\begin{aligned}\text {f.p.}_{\epsilon =0}\int _{R=0} ^{1/\epsilon } \int _{0}^{\alpha }\frac{1}{2}R\exp \left[ -\frac{1}{2}R^2\right] \sum _{j=1}^{\infty }I_{\mu _j}\left( \frac{1}{2}R^2\right) |\phi _j(\theta )|^2\, d\theta \, dR.\end{aligned}$$
Since the cross-sectional eigenfunctions,
\(\phi _j\)
, have unit
\(\mathcal {L}^2\)
norm, this simplifies to
$$\begin{aligned} \text {f.p.}_{\epsilon =0}\int _{R=0} ^{1/\epsilon } \frac{1}{2}Re^{-\frac{1}{2}R^2}\sum _{j=1}^{\infty }I_{\mu _j}(\frac{1}{2}R^2)\, dR. \end{aligned}$$
(B.1)
In the Dirichlet–Dirichlet case,
\(\mu _j=j\pi /\alpha \)
and (
B.1
) becomes
$$\begin{aligned} \text {f.p.}_{\epsilon =0}\int _{R=0} ^{1/\epsilon }\frac{1}{2}Re^{-\frac{1}{2}R^2}\sum _{j=1}^{\infty }I_{j\pi /\alpha } \left( \frac{1}{2}R^2\right) \, dR. \end{aligned}$$
(B.2)
By [
43
,
51
], (
B.2
) is equal to
$$\begin{aligned} \frac{\pi ^2-\alpha ^2}{24\pi \alpha }. \end{aligned}$$
(B.3)
In the Neumann–Neumann case, the only difference is that there is a zero eigenvalue. So the difference of the corner contributions in the D–D and N–N cases is
$$\begin{aligned} \text {f.p.}_{\epsilon =0}\int _0^{1/\epsilon }\frac{1}{2}Re^{-\frac{1}{2}R^2}I_0 \left( \frac{1}{2}R^2\right) \, dR. \end{aligned}$$
(B.4)
This integral may be evaluated directly. First make a substitution in the integral setting
\(u=\frac{1}{2} R^2\)
, so that it becomes
$$\begin{aligned}\text {f.p.}_{\epsilon =0}\int _0^{\frac{1}{2\epsilon ^2}}\frac{1}{2} e^{-u} I_0(u)\, du.\end{aligned}$$
In [
2
, 5.5], a primitive for the integrand is obtained,
$$\begin{aligned}g(u):= e^{-u} u (I_0(u) + I_1 (u)) \implies g'(u) = e^{-u} I_0 (u).\end{aligned}$$
Since
\(I_0(0) = I_1(0) = 0\)
, the integral above is therefore
$$\begin{aligned} \text {f.p.}_{\epsilon =0} \frac{1}{2} \left[ \frac{1}{2\epsilon ^2} e^{-\frac{1}{2\epsilon ^2}} \left( I_0 \left( \frac{1}{2\epsilon ^2}\right) +I_1\left( \frac{1}{2\epsilon ^2}\right) \right) \right] . \end{aligned}$$
(B.5)
However, both
\(I_0(z)\)
and
\(I_1(z)\)
have expansions of the form
$$\begin{aligned}e^z z^{-1/2}(C_0+C_1z^{-1}+C_2z^{-2}+\dots )\end{aligned}$$
as
\(z\rightarrow \infty \)
. Substituting these expansions for the Bessel functions above, there are only odd powers of
\(\epsilon \)
in the expansion. Therefore the coefficient of the
\(\epsilon ^0\)
power is zero, and the finite part is zero. This shows that (
B.4
) equals zero and the Neumann–Neumann corner contribution is (
B.3
), the same as the Dirichlet–Dirichlet contribution.
In the Dirichlet–Neumann cases,
\(\mu _j=(j+1/2)\pi /\alpha \)
, starting at
\(j=0\)
, so we get
$$\begin{aligned} \text {f.p.}_{\epsilon =0}\int _0^{1/\epsilon }\frac{1}{2}Re^{-\frac{1}{2}R^2}\sum _{j=0}^{\infty }I_{(j+1/2)\pi /\alpha }\left( \frac{1}{2}R^2\right) \, dR. \end{aligned}$$
(B.6)
Observe that, since renormalized integrals are linear, this equals
$$\begin{aligned} \begin{aligned} \text {f.p.}_{\epsilon =0}\int _0^{1/\epsilon }\frac{1}{2}Re^{-\frac{1}{2}R^2}\sum _{j=1}^{\infty }I_{j\pi /(2\alpha )}\left( \frac{1}{2}R^2\right) \, dR \\ - \text {f.p.}_{\epsilon =0}\int _0^{1/\epsilon }\frac{1}{2}Re^{-\frac{1}{2}R^2}\sum _{j=1}^{\infty }I_{j\pi /\alpha }\left( \frac{1}{2}R^2\right) \, dR. \end{aligned} \end{aligned}$$
(B.7)
We recognize this to be (
B.2
) for angle
\(2\alpha \)
minus (
B.2
) for angle
\(\alpha \)
. We therefore obtain the Dirichlet–Neumann mixed corner contribution is
$$\begin{aligned} \frac{\pi ^2-(2\alpha )^2}{48\pi \alpha }-\frac{\pi ^2-\alpha ^2}{24\pi \alpha }=\frac{-\pi ^2-2\alpha ^2}{48\pi \alpha }. \end{aligned}$$
(B.8)
Rights and permissions
Open Access
This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit
http://creativecommons.org/licenses/by/4.0/
.
Reprints and permissions
About this article
Cite this article
Nursultanov, M., Rowlett, J. & Sher, D. The heat kernel on curvilinear polygonal domains in surfaces.
Ann. Math. Québec
49
, 1–61 (2025). https://doi.org/10.1007/s40316-024-00237-4
Download citation
Received
:
02 March 2024
Accepted
:
22 March 2024
Published
:
27 December 2024
Version of record
:
27 December 2024
Issue date
:
April 2025
DOI
:
https://doi.org/10.1007/s40316-024-00237-4
Share this article
Anyone you share the following link with will be able to read this content:
Get shareable link
Sorry, a shareable link is not currently available for this article.
Copy shareable link to clipboard
Provided by the Springer Nature SharedIt content-sharing initiative
Keywords
Curvilinear polygon
Surface with corners
Corner
Edge
Conic singularity
Heat kernel
Heat trace
Spectrum
Isospectral
Spectral invariant
Inverse spectral problem
Robin boundary condition
Vertex
Dirichlet boundary condition
Neumann boundary condition
Zaremba boundary condition
Mixed boundary conditions
Mathematics Subject Classification
Primary 58J35
35K08
58J53
58J50
Secondary 44A10
35A22
47A60
Profiles
Julie Rowlett
View author profile