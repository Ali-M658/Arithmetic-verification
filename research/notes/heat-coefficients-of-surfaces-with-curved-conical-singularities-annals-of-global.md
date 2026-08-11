---
title: Heat coefficients of surfaces with curved conical singularities | Annals of
  Global Analysis and Geometry | Springer Nature Link
id: heat-coefficients-of-surfaces-with-curved-conical-singularities-annals-of-global
tags:
- hyperbolic-pillow-heat-novelty-813161
- heat-trace-coefficients
- doi-record
- bibliography-correction
- cone-orbifold
created: '2026-08-09T08:44:00.829226Z'
updated: '2026-08-09T09:36:32.233182Z'
source: https://link.springer.com/article/10.1007/s10455-025-10024-1
source_domain: link.springer.com
fetched_at: '2026-08-09T08:44:00.828861Z'
fetch_provider: builtin
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'SpringerLink publisher record confirming the published version of Schueth''s
  paper. FULL CITATION (BibTeX-usable, verbatim from the publisher page): Schueth,
  D. ''Heat coefficients of surfaces with curved conical singularities.'' Ann. Glob.
  Anal. Geom. 69, 2 (2026). DOI: https://doi.org/10.1007/s10455-025-10024-1. Open
  access (CC-BY 4.0). Received: 30 September 2025; Accepted: 27 November 2025; Published
  (version of record): 08 December 2025. Article number 2, Volume 69, Issue 1 (2026).
  Note the published title uses ''conical'' (not arXiv''s abstract-metadata ''conic'').
  Body text of the article (abstract + full introduction through the b_1/b_2 literature
  survey) is reproduced identically to the arXiv HTML version; see [[heat-coefficients-of-surfaces-with-curved-conical-singularities]]
  for the full content summary.'
---

*Suggested by [[251122255-heat-coefficients-of-surfaces-with-curved-conic-singularities]] — published version DOI confirmation for bibliography correction*

Heat coefficients of surfaces with curved conical singularities | Annals of Global Analysis and Geometry | Springer Nature Link
Skip to main content
Heat coefficients of surfaces with curved conical singularities
Open access
Published:
08 December 2025
Volume 69
, article number
2
(
2026
)
Cite this article
You have full access to this
open access
article
Download PDF
Save article
View saved research
Annals of Global Analysis and Geometry
Aims and scope
Submit manuscript
Heat coefficients of surfaces with curved conical singularities
Download PDF
Abstract
Let (
M
,
g
) be a two-dimensional Riemannian manifold of finite diameter with a conical singularity. Under the assumption that the metric near the cone point
C
is rotationally invariant, but not necessarily flat, we give an explicit formula for the coefficient
\(b_{1/2}(C)\)
in the heat trace expansion
\(\operatorname {tr}(\operatorname {exp}(-t\Delta _g))\sim _{t\searrow 0} (4\pi t)^{-1}\sum _{j=0}^\infty a_j(M) t^j+\sum _{j=0}^\infty b_{j/2}(C)t^{j/2}+\sum _{j=0}^\infty c_{j/2}(C) t^{j/2} \log t\)
. In the case that the Gaussian curvature
K
of (
M
,
g
) satisfies
\(|K(p)|\rightarrow \infty \)
as
\(p\rightarrow C\)
, we show that
\(b_{1/2}(C)\)
varies irrationally under constant rescalings of the distance circles near the cone point. This is a sharp contrast to the behavior of
\(b_0(C)\)
and of those coefficients
\(b_j(C)\)
which appear in certain known formulas in the case of orbifold cone points or corners of geodesic polygons.
Similar content being viewed by others
Sharp estimates for convolution operators associated to hypersurfaces in
\({\mathbb {R}}^3\)
with height
\(h\le 2\)
Article
21 June 2025
Torsion points of small order on cyclic covers of
\({\mathbb {P}}^1\)
Article
24 May 2025
Neumann Cut-Offs and Essential Self-adjointness on Complete Riemannian Manifolds with Boundary
Article
Open access
24 March 2025
Explore related subjects
Discover the latest articles, books and news in related subjects, suggested using machine learning.
Differential Geometry
Geodesy
Hyperbolic Geometry
Membrane curvature
Diffusion  Processes and Stochastic Analysis on  Manifolds
Partial Differential Equations on Manifolds
Stochastic Dynamics of Random Polynomials on Complex Manifolds
1
Introduction
After the seminal work of Cheeger [
4
] on extending the theory of the Laplace operator to Riemannian spaces with singularities, the asymptotic behaviour of the resolvent trace and the heat trace on manifolds with conical singularities (or, more generally, stratified spaces with a stratum of conical type) was studied, among others, by Brüning and Seeley [
2
,
3
] who considered certain associated one parameter families of operators using a functional analytic approach. Their theory was extended to stratified spaces with iterated cone-edge metrics by Hartmann, Lesch, and Vertman [
7
,
8
]. In the case of two-dimensional Riemannian manifolds with isolated conical singularities, the metric near such a singularity
C
has the form
$$\begin{aligned} g=dr^2+f(r)^2 d\theta ^2, \end{aligned}$$
(1)
where
\(d\theta ^2\)
is the standard metric on the circle
\(S^1\)
of length
\(2\pi \)
, and where
f
is a smooth function on some
\([0,\varepsilon )\)
with
\(f(0)=0\)
and
\(f'(0)>0\)
. The special case
\(f(r)=\text {const}\cdot r\)
corresponds to a cone point in the classical sense, where the metric near the singularity is flat.
Assume that the conical singularity
C
is the only singularity of the surface
M
and that the closure
\(\overline{M}=M\cup \{C\}\)
of
M
with respect to the Riemannian distance is compact. We denote by
\(\Delta \)
the Friedrichs extension of the Laplace operator on functions on
M
. General results from [
2
] imply that in this setting, the associated heat trace has an asymptotic expansion
$$\begin{aligned} \operatorname {tr}(\exp (-t\Delta ))\sim {\textstyle {\frac{1}{4\pi t}}}\sum _{j=0}^\infty a_j(M) t^j+\sum _{j=0}^\infty b_{j/2}(C) t^{j/2}+\sum _{j=0}^\infty c_{j/2}(C) t^{j/2}\log t \end{aligned}$$
(2)
for
\(t\searrow 0\)
, where the coefficients in the first sum are (possibly regularized) integrals over certain curvature invariants on
M
, while the second and third sums depend only on the germ of
f
at
\(r=0\)
and correspond to the contribution of the cone point
C
; see Section
2
for more details. It is well-known that
\(a_0(M)=\operatorname {vol}(M)\)
. Moreover,
\(b_0(C) = \frac{1}{12}(\frac{1}{f'(0)}-f'(0))\)
(see [
2
], p. 424), and, in our situation,
\(c_0(C) =0\)
(see [
2
], p. 423/424) and
\(c_{j/2}(C)=0\)
for all odd
j
(see, e.g., Remark
2.8
below).
In her dissertation [
11
], Suleymanova computed
\(b_0(C)\)
and
\(c_0(C)\)
for cone points
C
of higher dimensional manifolds under the assumption that the metric near the cone point is of the special form
\(g=dr^2+r^2 g_N\)
on a punctured neighborhood
\(U\approx (0,\varepsilon )\times N\)
of
C
, where
\(g_N\)
is a Riemannian metric on the cross section
N
.
Note that cone points of orbisurfaces constitute a special case of conical singularities – at least if one assumes full rotational symmetry of a punctured neighborhood of the cone point, such that it fits into the above setting. Dryden et al. [
5
] applied general results by Donnelly to derive a qualitative description of the heat trace expansion for compact orbifolds. No logarithmic terms occur in that case. For cone points
C
of order
n
in two-dimensional Riemannian orbifolds, it was shown in [
5
] that
\(b_1(C)=\big (\frac{1}{360}(n^3-\frac{1}{n})+\frac{1}{36}(n-\frac{1}{n})\big )K(p)\)
, where
K
is the Gauss curvature and
p
the point corresponding to
C
in an orbifold chart. In [
10
], the author obtained a similar formula for
\(b_2(C)\)
in the same context;
\(b_2(C)\)
turns out to be a linear combination of
\(K(p)^2\)
and
\((\Delta K)(p)\)
, where the coefficients are, again, rational functions of the order of the cone point.
The cited results for
\(b_1(C)\)
and
\(b_2(C)\)
in the orbifold case do not assume full rotational symmetry of a punctured neighborhood of
C
.
Uçar [
13
] obtained explicit formulas for
all
\(b_\ell (C)\)
for cone points
C
of two-dimensional orbifolds under the special assumption that the orbifold has constant curvature
\(\kappa \in \mathbb {R}\)
. In our notation, this corresponds to the case
\(f(r)=\frac{1}{n} s_\kappa (r)\)
in (
1
), where
n
is the order of the cone point and
\(s_\kappa \)
is the modified sine function determined by
\(s_\kappa ''=-\kappa s_\kappa \)
,
\(s_\kappa (0)=0\)
, and
\(s_\kappa '(0)=1\)
. More specifically,
\(b_\ell (C)\)
can then be written as
\(\kappa ^\ell \)
times
\(\frac{1}{n} p_\ell (n)\)
, where
n
is the order of the cone point and
\(p_\ell \)
is a certain polynomial of order
\(2\ell +2\)
. Uçar [
13
] also proved formulas of the same type for the contributions of corners of geodesic polygons in surfaces of constant curvature to the Dirichlet heat trace expansion, regardless of whether the angle at the corner is of the form
\(\pi /n\)
or not.
We note here, without proving it in this paper, that in the case of full rotational symmetry around
C
, it would be possible to reprove the formulas for
\(b_1(C)\)
from [
5
] and for
\(b_2(C)\)
from [
10
] (or, for the constant curvature case, from [
13
]) using similar methods as in the current paper, i.e. relying on the approach of [
2
]. For this, it plays no role at all whether
\(n=1/f'(0)>0\)
is a natural number or not. Therefore, replacing
n
by
\(1/f'(0)\)
, we can note that these
\(b_\ell (C)\)
depend rationally on
\(f'(0)\)
. Equivalently, under rescalings of
f
by a constant
\(\lambda >0\)
, these coefficients depend rationally on
\(\lambda \)
. (Note that the Gaussian curvature
\(K=-f''/f\)
and its derivatives, which also appear in the
\(b_\ell (C)\)
above, are invariant under constant rescalings of
f
.)
If
p
is a point in a
smooth
two-dimensional Riemannian manifold
M
and the metric on a neighborhood of
p
has full rotational symmetry around
p
, then the metric near
p
can be written in the form (
1
), where
\(r=d(p,\,.\,)\)
and
f
(
r
) is the distortion of the length of the distance circle under the geodesic exponential map
\(\exp _p\)
. In that case, it is well-known that
\(f(r) = r -\frac{1}{6} K(p)r^3 + O(r^4)\)
; in particular,
\(f''(0)=0\)
. Passing to an orbifold cone point of order
n
just corresponds to passing from
f
to
f
/
n
, so
\(f''(0)=0\)
still holds for cone points in orbisurfaces. The same, of course, holds for arbitrary constant rescalings of
f
.
In (
1
), however, we allow more general functions
f
, as long as they are smooth on
\([0,\varepsilon )\)
for some
\(\varepsilon >0\)
and satisfy
\(f(0)=0\)
and
\(f'(0)>0\)
. In particular, we allow
\(f''(0)\ne 0\)
. Since
\(K=-f''/f\)
in the coordinates from (
1
), the inequality
\(f''(0)\ne 0\)
is equivalent to
\(|K(p)|\rightarrow \infty \)
for
\(p\rightarrow C\)
. On the other hand, if a punctured neighborhood of the singularity happens to be isometric to a rotational surface embedded in
\(\mathbb {R}^3\)
then
\(f'(0)=\sin \varphi \)
, where
\(\varphi \)
is the sine of the angle between the axis and the initial direction of the profile curve; if
\(\varphi <\pi /2\)
then the inequality
\(f''(0)\ne 0\)
is equivalent to nonzero curvature of the profile curve at its initial point (see Remark
2.3
).
If
\(f''(0)\ne 0\)
in (
1
), then, unlike in the orbifold case, half powers of
t
can occur in the middle sum of (
2
), and logarithmic terms can occur, too. For example, it turns out that
\(c_1(C)=-\frac{1}{60} f''(0)^2/f'(0)\)
(see Remark
2.8
). The main goal of this paper is to prove the following explicit formula for
\(b_{1/2}(C)\)
:
$$\begin{aligned} b_{1/2}(C) =\frac{2 f''(0)}{\sqrt{\pi }f'(0)}\int _0^1\left( \hat{h}_{2,\alpha }(1-u^2)-\frac{1}{4}\hat{h}_{0,\alpha }(1-u^2)\right) \,du, \end{aligned}$$
(3)
where
\(\alpha :=1/f'(0)\)
and
\(\hat{h}_{k,\alpha }\)
is defined as follows for all
\(k\in \mathbb {N}_0\)
and
\(\alpha >0\)
: For
\(z\in \mathbb {C}\)
with
\(|z|<1\)
and
\(|1-z|<1\)
, first let
$$h_{k,\alpha }(z):=\sum _{n=0}^\infty \alpha ^k n^k(1-z)^{n\alpha }=\left( -(1-z)\frac{d}{dz}\right) ^k\frac{1}{1-(1-z)^\alpha }\,. $$
This turns out to define a meromorphic function in a neighborhood of the origin, with a pole in
\(z=0\)
. Denote its regular part (obtained by subtracting the principal part of the Laurent series) by
\(h^{\text {reg}}_{k,\alpha }(z)\)
and let
$$\hat{h}_{k,\alpha }(z):=\frac{1}{z}(h^{\text {reg}}_{k,\alpha }(z)-h^{\text {reg}}_{k,\alpha }(0)); $$
see Section
3
for a detailed discussion of these functions.
Our formula for
\(b_{1/2}(C)\)
differs fundamentally from the one which is stated in [
12
] and claims this coefficient to be equal to
\(\frac{f''(0)}{f'(0)}\cdot \frac{5}{96\sqrt{\pi }}\)
. (More precisely,
\(1/f'(0)\)
is written on p. 10 of that paper as
\(\cot \varphi \)
instead of
\(1/\sin \varphi \)
, where
\(\varphi \)
is the opening angle in the case of embedded rotational surfaces as above; however, this small mistake is not the main reason for the difference between the formula from [
12
] and our result.) See Remark
3.3
for more details concerning this discrepancy.
Moreover, in contrast to the situation for the
\(b_\ell (C)\)
as described above, it turns out that if
\(f''(0)\ne 0\)
then
\(b_{1/2}(C)\)
does
not
depend rationally on the scaling factor
\(\lambda \)
when one replaces
f
by
\(\lambda f\)
– or equivalently, when one rescales small distance circles around
C
by
\(\lambda \)
. In fact, the integral in (
3
) turns out to be a non-rational function of
\(\alpha =1/f'(0)\)
. To the author’s knowledge, this is the first instance where such an irrational behaviour of a coefficient in the heat expansion of conical singularities is detected.
This paper is organized as follows: In Section
2
we recall, adapted to our special setting, the necessary background from [
2
] concerning the description of
\(\Delta \)
near the singularity in terms of a certain one parameter family of operators
A
(
r
), the associated scaled boundary operators and the expansion of the trace of their resolvents, thereby arriving at a first description of the contributions of the singularity to the coefficients of the asymptotic expansion of the resolvent trace. We also recall the relations between these and the corresponding coefficients of the heat trace expansion. In Section
3
we derive our explicit formula for
\(b_{1/2}(C)\)
(Corollary
3.15
), and in Section
4
we prove that if
\(f''(0)\ne 0\)
then
\(b_{1/2}(C)\)
is
\(f''(0)/f'(0)\)
times an irrational function of
\(f'(0)\)
(Theorem
4.1
).
2
Preliminaries
NotationandRemarks 2.1
(i)
In this paper, (
M
,
g
) will always denote a two-dimensional Riemannian manifold of finite diameter with one conical singularity
C
. We assume that the closure of
M
with respect to the Riemannian distance is compact and equals
\(\overline{M}=M\cup \{C\}\)
.
(ii)
By definition of the notion of conical singularity, there exists
\(\varepsilon >0\)
such that the punctured
\(\varepsilon \)
-neighborhood
\(U_\varepsilon \)
of
C
is isometric to
\(]0,\varepsilon [\times S^1\)
equipped with the metric
$$dr^2+f(r)^2 d\theta ^2 $$
for some
\(f\in C^\infty ([0,\varepsilon [,\mathbb R_{\ge 0})\)
with
\(f(0)=0\)
and
\(f'(0)>0\)
. Here,
\(d\theta ^2\)
denotes the standard metric on
\(S^1\)
with length
\(2\pi \)
.
Remark 2.2
In the above coordinates, the Gaussian curvature
K
is given by
$$K=-f''/f. $$
Therefore, for
\(p\rightarrow C\)
we have
$$\begin{aligned} K(p)\rightarrow {\left\{ \begin{array}{ll}-f'''(0)/f'(0),& f''(0)=0,\\ \infty ,& f''(0)<0,\\ -\infty ,& f''(0)>0.\end{array}\right. } \end{aligned}$$
In particular,
\(f''(0)\ne 0\)
is equivalent to
\(|K(p)|\rightarrow \infty \)
for
\(p\rightarrow C\)
.
Remark 2.3
(i)
In the special case that
\(U_\varepsilon \)
can be embedded isometrically as a surface of revolution around the
x
-axis in
\(\mathbb {R}^3\)
with profile curve
\(]0,\varepsilon [\ni r\mapsto (x(r),0,z(r))\in \mathbb {R}^3\)
of unit speed with
\(x(r)\ge 0\)
and
\(z(r)\ge 0\)
for all
r
, one has
\(f(r)=z(r)\)
,
\({x'}^2+{f'}^2=1\)
, and
\(x'x''+f'f''=0\)
. In particular,
\(f'(0)\le 1\)
.
(ii)
If
\(f'(0)<1\)
in the situation of (i), then
\(x'(0)>0\)
, and the curvature
\(\kappa (0)\)
of the profile curve in the (
x
,
z
)-plane in its initial point is given by
$$\kappa (0)=(x'f''-f'x'')(0)=\frac{({x'}^2f''+(f')^2f'')(0)}{x'(0)}=\frac{f''(0)}{x'(0)}=\frac{f''(0)}{f'(0)}\cdot \tan \varphi , $$
where
\(\varphi =\arctan (f'(0)/x'(0))=\arcsin (f'(0))\in ]0,\frac{\pi }{2}[\)
is the angle between the
x
-axis and the initial direction of the profile curve. In particular,
\(f''(0)\ne 0\)
is equivalent to
\(\kappa (0)\ne 0\)
in this situation.
Remark 2.4
(i) Following [
2
], p. 423, we note that in the setting of
2.1
(ii) the associated Laplacian
$$\Delta =-f^{-1}(\partial _r f\partial _r)-f^{-2}\partial _\theta ^2 $$
on
\(U_\varepsilon \)
is conjugate, via the map
\(u\mapsto f^{1/2} u\)
, to the operator
$$\begin{aligned} \begin{aligned} L:=&{}-\partial _r^2+f^{-2}\left( -\partial _\theta ^2-\frac{1}{4}(f')^2+\frac{1}{2} ff''\right) \\ =&{}-\partial _r^2+r^{-2}A(r) \end{aligned} \end{aligned}$$
on
\(]0,\varepsilon [\,\times S^1\)
, where each
$$\begin{aligned} A(r):=-\frac{r^2}{f(r)^2}\partial _\theta ^2-\frac{1}{4}\frac{r^2f'(r)^2}{f(r)^2}+\frac{1}{2}\frac{r^2 f''(r)}{f(r)} \end{aligned}$$
acts on
\(C^\infty (S^1)\)
. Note that
A
smoothly extends to
\(r=0\)
.
(ii) We have
$$r^2/f(r)^2=(f'(0)+\frac{r}{2} f''(0)+O(r^2))^{-2}=f'(0)^{-2}(1-rf''(0)/f'(0)+O(r^2)) $$
and, thus,
$$r^2f'(r)^2/f(r)^2=(1-rf''(0)/f'(0))(1+rf''(0)/f'(0))^2+O(r^2)=1+rf''(0)/f'(0)+O(r^2). $$
Moreover,
$$r^2f''(r)/f(r)=rf''(0)/f'(0)+O(r^2). $$
Hence,
$$\begin{aligned} \begin{aligned} A(r)=&{}-\frac{1}{f'(0)^2}\left( 1-r\frac{f''(0)}{f'(0)}+O(r^2)\right) \partial _\theta ^2 -\frac{1}{4}\left( 1+r\frac{f''(0)}{f'(0)}\right) +\frac{1}{2} r\frac{f''(0)}{f'(0)}+O(r^2)\\ =&{}-\frac{1}{f'(0)^2}\left( 1-r\frac{f''(0)}{f'(0)}+O(r^2)\right) \partial _\theta ^2 -\frac{1}{4}\left( 1-r\frac{f''(0)}{f'(0)}+O(r^2)\right) . \end{aligned} \end{aligned}$$
In particular,
$$\begin{aligned} A(0)=-\frac{1}{f'(0)^2}\partial _\theta ^2-\frac{1}{4}\ge -\frac{1}{4} \end{aligned}$$
(4)
and
$$\begin{aligned} A'(0)=k_f A(0) \text{ with } k_f:=-\frac{f''(0)}{f'(0)}\,. \end{aligned}$$
(5)
Remark 2.5
We denote by
\(\Delta \)
the Friedrichs extension of the Laplacian on the singular surface
M
. For
\(m>\dim (M)/2=1\)
, the resolvent
\((\Delta +z^2)^{-m}\)
is of trace class; see, e.g. [
3
], p. 275. Moreover, there is an asymptotic expansion as
\(z\rightarrow \infty \)
:
$$\begin{aligned} \operatorname {tr}(\Delta +z^2)^{-m}\sim \sum _{j=0}^\infty a_{j,m}(M) z^{-2m+2-2j}+\sum _{j=0}^\infty b_{j,m}(C) z^{-2m-j}+\sum _{j=0}^\infty c_{j,m}(C)z^{-2m-j}\log z, \end{aligned}$$
(6)
where the coefficients in the first sum are (possibly regularized) integrals over certain curvature invariants on
M
, while the second and third sums depend only on the germ of
f
at
\(r=0\)
and consist of contributions of the cone point
C
. This follows (using
\(\operatorname {dim}(M) = 2\)
and
\(\operatorname {dim}(C) = 0\)
) as a special case of either [
3
], Theorem 5.2, or [
8
], Theorem 1.1, each with slightly different notation.
Corollary 2.6
The heat trace associated with
\(\Delta \)
has the asymptotic expansion
$$\begin{aligned} \operatorname {tr}(\exp (-t\Delta ))\sim {\textstyle {\frac{1}{4\pi t}}}\sum _{j=0}^\infty a_j(M) t^j+\sum _{j=0}^\infty b_{j/2}(C) t^{j/2}+\sum _{j=0}^\infty c_{j/2}(C) t^{j/2}\log t, \end{aligned}$$
(7)
for
\(t\searrow 0\)
, where the relation to the coefficients of (
6
) is as follows:
$$\begin{aligned} \begin{aligned} a_j(M)&=\frac{4\pi (m-1)!}{\Gamma (m-1+j)}a_{j,m}(M)\\ b_{j/2}(C)&=\frac{(m-1)!}{\Gamma (m+\frac{j}{2})}b_{j,m}(C) + \frac{(m-1)!\,\Gamma '(m+\frac{j}{2})}{2\Gamma (m+\frac{j}{2})^2}c_{j,m}(C)\\ c_{j/2}(C)&= - \frac{(m-1)!}{2\Gamma (m+\frac{j}{2})}c_{j,m}(C) \end{aligned} \end{aligned}$$
(8)
for each
\(j\in \mathbb {N}_0\)
.
Proof
The existence, in itself, of the asymptotic expansion (
7
) is well-known; e.g., it is a special case of [
2
], Theorem 7.1. The explicit relations (
8
) to the coefficients in the resolvent expansion are a bit hidden in the formulas on p. 416 of that (more general) paper. The argument is as follows: Let
\(\gamma \subset \mathbb {C}\)
denote the contour
\(\{\lambda :\operatorname {arg}(\lambda +1)=\pm \pi /4\}\)
, traversed upward. Then
$$\begin{aligned} \operatorname {tr}e^{-t\Delta }=t^{1-m}\frac{(m-1)!}{2\pi i}\int _\gamma e^{-t\lambda }\operatorname {tr}(\Delta -\lambda )^{-m}\,d\lambda . \end{aligned}$$
We insert (
6
) with
\(z=\sqrt{-\lambda }\)
and use the equations
$$\begin{aligned} \begin{aligned} \int _\gamma e^{-t\lambda }(-\lambda )^{-n/2}d\lambda&=\frac{2\pi i}{\Gamma (n/2)}t^{-1+n/2}\\ \int _\gamma e^{-t\lambda }(-\lambda )^{-n/2}\log \sqrt{-\lambda }\,d\lambda&= - \frac{\pi i}{\Gamma (n/2)}t^{-1+n/2}\log t + \frac{\pi i\,\Gamma '(n/2)}{\Gamma (n/2)^2}t^{-1+n/2} \end{aligned} \end{aligned}$$
(9)
for all
\(t>0\)
and
\(n\in \mathbb {N}\)
. Comparing coefficients then yields (
8
).
\(\square \)
Remark 2.7
We will now summarize some facts, mainly from [
2
], in order to establish formulas for the resolvent expansion coefficients
\(b_{j,m}(C)\)
and
\(c_{j,m}(C)\)
in our specific situation.
(i) Recall from Remark
2.4
that
\(\Delta \)
on
$$U_\varepsilon \simeq (0,\varepsilon )\times S^1 $$
is conjugate to
$$ L=-\partial _r^2+r^{-2}A(r). $$
We choose a modification
\(\tilde{A}\)
of
A
as in [
2
], p. 396; in particular,
\(\tilde{A}\)
is defined on all of
\([0,\infty )\)
, coincides with
A
in some neighborhood of
\(r=0\)
, and
\(\tilde{A}(r)\)
is an elliptic operator on
\(C^\infty (S^1)\)
for each
r
. The corresponding modification of
L
is the “boundary operator”
$$L_b:=-\partial _r^2+r^{-2}\tilde{A}(r). $$
For any
\(t\ge 0\)
, let
$$\tilde{A}_t(r):=\tilde{A}(tr) $$
and consider the “scaled boundary operator”
$$L_{b,t}:=-\partial _r^2+r^{-2}\tilde{A}_t(r). $$
Writing
$$G^m_{b,t}(z):=(L_{b,t}+z^2)^{-m}, $$
we recall from [
2
], Lemma 4.9, that for each
\(m>\operatorname {dim}(M)/2=1\)
, the operators
\(G^m_{b,t}(z)\)
have kernels
\(G^m_{b,t}(r,s;z)\)
such that each
\(G^m_{b,t}(\,.\,,\,.\,;z)\)
is a continuous map from
\((0,\infty )\times (0,\infty )\)
into the space of trace class operators on
$$H:=L^2(S^1,d\theta ^2), $$
and then
\(G_{b,t}^m\)
satisfies
$$\begin{aligned} G_b^m(tr,ts;z/t)=t^{2m-1}G_{b,t}^m(r,s;z), \end{aligned}$$
(10)
where
$$G_b:=G_{b,1}. $$
Moreover, by [
2
], Theorem 4.2,
\(\varphi G^m_{b,t}(z)\)
is of trace class for each
\(\varphi \in C^\infty ([0,\infty ),\mathbb {R})\)
with compact support, and
$$\begin{aligned} \operatorname {tr}(\varphi G^m_{b,t}(z))=\int _0^\infty \varphi (r)\operatorname {tr}_H G^m_{b,t}(r,r;z)\,dr. \end{aligned}$$
In particular,
$$\operatorname {tr}(\varphi G^m_b(z))=\int _0^\infty \sigma (r,rz)\,dr $$
with
$$\begin{aligned} \sigma (r,\zeta ):=\varphi (r)\operatorname {tr}_H G^m_b(r,r;\zeta /r). \end{aligned}$$
By formula (4.18) in [
2
],
$$\begin{aligned} \sigma (r,\zeta )=\varphi (r)\cdot r^{2m-1}\operatorname {tr}_H G^m_{b,r}(1,1;\zeta ), \end{aligned}$$
(11)
which is a consequence of (
10
). Since the operators
\(L_{b,r}\)
are elliptic with resolvents
\(G_{b,r}\)
, it follows that there is an asymptotic expansion of the form
$$\begin{aligned} \sigma (r,\zeta )\sim \sum _{j=0}^\infty \varphi (r)\sigma _j(r)\zeta ^{-2m+\operatorname {dim}(M)-2j}=\sum _{j=0}^\infty \varphi (r)\sigma _j(r)\zeta ^{-2m+2-2j} \end{aligned}$$
(12)
for
\(\zeta \rightarrow \infty \)
(see, e.g., [
2
], p. 421, or [
3
], p. 286).
(ii) From now on, we let
\(\varphi \)
be a smooth cut-off function on
\([0,\infty )\)
with compact support and
$$\varphi (r)\equiv 1 \text{ near } r=0; $$
in particular, all derivatives of
\(\varphi \)
in
\(r=0\)
vanish. We also denote by
\(\varphi \)
the corresponding function on
\(U_\varepsilon \)
and its extension to
M
by zero outside
\(U_\varepsilon \)
. The asymptotic expansion (
12
) and the Singular Asymptotics Lemma (see [
2
], p. 372) now imply
(13)
for
\(z\rightarrow \infty \)
. Here,
denotes the regularized integral:
where
\(\mathcal {M}\mu :s\mapsto \int _0^\infty r^{s-1} \mu (r)\,dr\)
is the Mellin transform of
\(\mu \)
, and
\({\operatorname {Res}_0}_{|s=1}\,\mathcal {M}\mu \)
is the coefficient at
\((s-1)^0\)
(i.e., the constant term) in the Laurent expansion around
\(s=1\)
of a meromorphic continuation of
\(\mathcal {M}\mu \)
; see [
9
], Section 2.1 for a thorough introduction to these concepts. Note that, equivalently,
(14)
(iii) The coefficients
\(b_{j,m}(C)\)
and
\(c_{j,m}(C)\)
in the asymptotic expansion (
6
) of
\(\operatorname {tr}(\Delta +z^2)^{-m}\)
for
\(z\rightarrow \infty \)
are the same as in the asymptotic expansion of
\(\operatorname {tr}(\varphi (\Delta +z^2)^{-m})\)
which, in turn, are the same as in the asymptotic expansion of
\(\operatorname {tr}(\varphi G_b^m(z))=\int _0^\infty \sigma (r,rz)\,dr\)
(see, e.g., [
3
], p. 284). From (
13
) it follows that
(15)
where for the second equation one uses (
11
) and
\(\varphi (r)\equiv 1\)
near
\(r=0\)
, and
$$\begin{aligned} c_{j,m}(C)={\left\{ \begin{array}{ll} 0,& j \text{ odd },\\ \frac{1}{(2m-1+j)!}\cdot \sigma _{1+\frac{j}{2}}^{(2m-1+j)}(0),& j \text{ even }.\end{array}\right. } \end{aligned}$$
(16)
(iv) Note that for
r
sufficiently close to 0, the asymptotic expansion of
\(\sigma (r,\zeta )\)
for
\(\zeta \rightarrow \infty \)
is the same as that of the integral over
\((S^1,\operatorname {dvol}_{f^2d\theta ^2})\)
of the value of the operator kernel of
\((\Delta +\zeta ^2/r^2)^{-m}\)
in (
p
,
p
), where
\(p=(r,\theta )\)
. Consider the well-known the asymptotic expansion
$$H(t,p,p)\sim \frac{1}{4\pi t}\sum _{\ell =0}^\infty u_\ell (p)t^\ell $$
for
\(t\rightarrow 0\)
of the heat kernel
H
of
\(\Delta \)
, that is, the (interior) operator kernel associated with
\(e^{-t\Delta }\)
. Using the first formula of (
9
) and the above, one obtains, for all sufficiently small
\(r>0\)
:
$$ \sigma (r,\zeta )\sim \sum _{j=0}^\infty \frac{1}{4\pi }(\zeta /r)^{-2m+2-2j}\int _{S^1}u_j(r,\theta )f(r)d\theta \cdot \frac{\Gamma (m-1+j)}{(m-1)!} $$
for
\(\zeta \rightarrow \infty \)
. Since
g
on
\(U_\varepsilon \)
is rotationally invariant, we can write
\(u_j(r):=u_j(r,\theta )\)
and get
$$ \sigma (r,\zeta )\sim \sum _{j=0}^\infty \zeta ^{-2m+2-2j}\cdot \frac{1}{2} r^{2m-2+2j} u_j(r)f(r)\cdot \frac{(m-2+j)!}{(m-1)!} $$
for
\(\zeta \rightarrow \infty \)
; thus,
$$\begin{aligned} \sigma _j(r)=\frac{1}{2} r^{2m-2+2j} f(r)u_j(r)\cdot \frac{(m-2+j)!}{(m-1)!} \end{aligned}$$
for all
\(j\in \mathbb {N}_0\)
and all sufficiently small
\(r>0\)
(see also formula (3.19) of [
11
] which concerned the special case
\(f(r)=r\)
with general dimension of
M
). In particular, (
16
) now implies:
$$\begin{aligned} c_{j,m}(C){\left\{ \begin{array}{ll} 0,& j \text{ odd },\\ \frac{1}{(2m-1+j)!}\cdot \frac{1}{2}\cdot {\partial _r^{2m-1+j}}_{|r=0}\,( r^{2m+j} f(r) u_{1+\frac{j}{2}}(r))\cdot \frac{(m-1+\frac{j}{2})!}{(m-1)!},& j \text{ even }. \end{array}\right. } \end{aligned}$$
(17)
Remark 2.8
(i) Recall that
$$\begin{aligned} u_0(r)=1 \text{ and } u_1(r)=\frac{1}{6}\operatorname {scal}(r)=\frac{1}{3} K(r)=-\frac{1}{3} f''(r)/f(r). \end{aligned}$$
In particular, both
\(fu_0\)
and
\(fu_1\)
are smooth in
\(r=0\)
. By (
17
), this implies
$$c_{0,m}(C)=0 $$
(as well as
\(c_{-2,m}(C)=0\)
for the hypothetical coefficient
\(c_{-2,m}(C)\)
). This is well-known; see, e.g., [
2
], p. 423/424. Since
\(c_{j,m}(C)=0\)
for all odd
j
by (
16
), one concludes using (
8
):
\(c_0(C)=0\)
,
\(c_{1/2}(C)=0\)
,
\(b_0(C)=b_{0,m}(C)\)
, and
$$\begin{aligned} b_{1/2}(C)= \frac{(m-1)!}{\Gamma (m+\frac{1}{2})}b_{1,m}(C). \end{aligned}$$
(18)
Moreover,
\(u_2(r) = \frac{1}{15}K(r)^2=\frac{1}{15}f''(r)^2/f(r)^2\)
. One easily derives using (
17
):
$$\begin{aligned} c_{2,m}(C)=\frac{m}{30} f''(0)^2/f'(0) \end{aligned}$$
and, consequently,
\(c_1(C)=-\frac{1}{60} f''(0)^2/f'(0)\)
. Note that the above statements about
\(c_{0,m}(C)\)
and
\(c_{2,m}(C)\)
do agree with those given in Proposition 3.3 of [
12
], while our explicit formula for
\(b_{1,m}(C)\)
in Corollary
3.15
will differ fundamentally from the one given in Proposition 3.5 of [
12
]; see also Remark
3.3
(i) below.
(ii) Just for a moment, let us consider the special case that a punctured neighborhood of
C
in
\(\overline{M}=M\cup \{C\}\)
, after removing one radial geodesic, is isometric to the interior of a compact subset of a smooth surface. In that case, the Gaussian curvature and, therefore, each of the functions
\(u_j\)
smoothly extends to
\(r=0\)
. By (
17
) this implies that all
\(c_{j,m}(C)\)
vanish, and so do the
\(c_{j/2}(C)\)
. So, in that setting, no logarithmic terms occur in the asymptotic expansions (
6
) and (
7
). For cone points in orbisurfaces this is, of course, well-known (even without the assumption of full rotational invariance of the metric); see, e.g., [
5
].
3
An explicit formula for
\(b_{1/2}(C)\)
The explicit value of
\(b_0(C)=b_{0,m}(C)\)
is well-known: By [
2
], p. 424, interpreted in our notation (see also [
11
], Lemma 4.1), one has:
$$b_0(C)=\frac{1}{12}\left( \frac{1}{f'(0)}-f'(0)\right) $$
In this section, we will compute
\(b_{1/2}(C)\)
. Note that this is also the purpose of Proposition 3.5 in [
12
], which does, however, not agree with the results that we obtain in Corollary
3.15
and Theorem
4.1
below. This will be in part, but not only, be a consequence of the difference between (
5
) and formula (3.1) of [
12
].
Remark 3.1
Let
$$L_0:=L_{b,0}=-\partial _r^2+r^{-2}A(0), $$
the so-called “frozen” operator. Its resolvent is
$$G_0:=G_{b,0} $$
and can be written as
$$G_0(\zeta )=\bigoplus _{a\in \operatorname {spec}(A(0))}(-\partial _r^2 +r^{-2}a+\zeta ^2)^{-1}\otimes \pi _a\,, $$
where the sum is over all eigenvalues of
A
(0), and the endomorphism
\(\pi _a\)
of
\(L^2((0,\varepsilon )\times S^1)\)
denotes fiberwise projection onto the eigenspace
\(E_a\)
of the eigenvalue
a
of
A
(0); that is,
$$(\pi _a \phi )(r,\theta )=(\operatorname {proj}_{E_a}(\phi (r,\,.\,)))(\theta ). $$
From Lemma 4.3 of [
2
] it follows that
$${\partial _r}_{|r=0} G_{b,r}=-G_0 X^{-1/2} A'(0) X^{-1/2}G_0\,, $$
where
X
is the operator acting on functions on
\((0,\varepsilon )\times S^1\)
as multiplication by the first coordinate. Since
\(A'(0)\)
commutes with
\(L_0\)
and, thus, with
\(G_0\)
, it follows that
$$\begin{aligned} {\partial _r}_{|r=0}\operatorname {tr}_H G^m_{b,r}(1,1;\zeta )=-m\operatorname {tr}_H (G_0^{m+1}A'(0))(1,1;\zeta ). \end{aligned}$$
(19)
Recall from (
4
) that
\(A(0)\ge -\frac{1}{4}\)
. For each eigenvalue
a
of
A
(0) write
$$\nu (a):=\sqrt{a+\frac{1}{4}}. $$
By formula (7.9) of [
2
], the operator
\((-\partial _r^2+r^{-2}a+\zeta ^2)^{-m}\)
has a kernel
\(k^m_{\nu (a)}\)
which is given on the diagonal by
$$k_{\nu (a)}^m(r,r;\zeta )=\frac{1}{(m-1)!}\left( -\frac{1}{2\zeta }\frac{\partial }{\partial \zeta }\right) ^{m-1}r I_{\nu (a)}(r\zeta ) K_{\nu (a)}(r\zeta ), $$
where
\(I_\nu \)
and
\(K_\nu \)
are the Bessel functions of the first and second kind, respectively. In particular,
$$k_{\nu (a)}^m(1,1;\zeta )=\frac{1}{(m-1)!}\left( -\frac{1}{2\zeta }\frac{\partial }{\partial \zeta }\right) ^{m-1}I_{\nu (a)}(\zeta ) K_{\nu (a)}(\zeta ) $$
and, by formula (7.10) of [
2
],
$$\operatorname {tr}_H G_0^m(1,1;\zeta )=\sum _{a\in \operatorname {spec}(A(0))} \frac{1}{(m-1)!}\left( -\frac{1}{2\zeta }\frac{\partial }{\partial \zeta }\right) ^{m-1}I_{\nu (a)}(\zeta ) K_{\nu (a)}(\zeta ), $$
where the eigenvalues of
A
(0) are repeated according to their multiplicity
\(\operatorname {dim}(E_a)\)
from now on. Note that on the image of
\(\pi _a\)
, the operator
\(A'(0)=k_f A(0)\)
acts as multiplication by the number
\(k_f a\)
, where
\(k_f=-f''(0)/f'(0)\)
as in (
5
). Thus,
$$\operatorname {tr}_H (G_0^{m+1}A'(0))(1,1;\zeta )=\sum _{a\in \operatorname {spec}(A(0))} \frac{1}{m!}\left( -\frac{1}{2\zeta }\frac{\partial }{\partial \zeta }\right) ^{m}I_{\nu (a)}(\zeta ) K_{\nu (a)}(\zeta ) k_f a\,d\zeta . $$
By (
15
) and (
19
), this implies:
(20)
Lemma 3.2
$$\begin{aligned} b_{1,m}(C)  &   =-\frac{k_f}{(m-1)!}{\operatorname {Res}_0}_{|s=0}\\    &   \quad \left[ \frac{1}{4\sqrt{\pi }}\Gamma \left( m+\frac{1}{2}+\frac{s}{2}\right) \Gamma \left( -\frac{s}{2}\right) \sum _{a\in \operatorname {spec}(A(0))} a\,\frac{\Gamma \left( \nu (a)+\frac{1}{2}+\frac{s}{2}\right) }{\Gamma \left( \nu (a)+\frac{1}{2}-\frac{s}{2}\right) }\right] , \end{aligned}$$
where the elements
\(a\in \operatorname {spec}(A(0))\)
are counted with multiplicity.
Proof
By formula (7.11) of [
2
] (substituting
\(m+1\)
for
m
in that formula), we have
$$\begin{aligned} \int _0^\infty \zeta ^w\left( -\frac{1}{2\zeta }\frac{\partial }{\partial \zeta }\right) ^m I_\nu (\zeta )K_\nu (\zeta )\,d\zeta = \frac{1}{4\sqrt{\pi }}\,\Gamma \left( \frac{w+1}{2}\right) \Gamma \left( m-\frac{w}{2}\right) \frac{\Gamma (\nu +\frac{1}{2}+\frac{w}{2} -m)}{\Gamma (\nu +\frac{1}{2} -\frac{w}{2}+m)} \end{aligned}$$
For
\(w=2m+s\)
, this gives:
$$\int _0^\infty \zeta ^{2m+s}\left( -\frac{1}{2\zeta }\frac{\partial }{\partial \zeta }\right) ^m I_\nu (\zeta )K_\nu (\zeta )\,d\zeta = \frac{1}{4\sqrt{\pi }}\,\Gamma \left( m+\frac{1}{2}+\frac{s}{2}\right) \Gamma \left( -\frac{s}{2}\right) \frac{\Gamma (\nu +\frac{1}{2}+\frac{s}{2})}{\Gamma (\nu +\frac{1}{2} -\frac{s}{2})} $$
Together with (
20
) and (
14
), this implies the statement.
\(\square \)
Remark 3.3
(i) In view of the factor
\(\Gamma (-\frac{s}{2})\)
in the formula from Lemma
3.2
, the fact that
\(\Gamma \)
has a pole at
\(s=0\)
plays an important role for the subsequent computation of
\(b_{1,m}(C)\)
. Note that this is a very different situation compared to formula (7.12) of [
2
], which gives a similar expression concerning (in our notation)
\(b_{0,m}(C)\)
. As it is, the pole of
\(\Gamma \)
at
\(s=0\)
seems to have been ignored in the computation starting in the lower part of p. 9 in [
12
]. In that paper,
\(b_{1,m}(C)\)
is claimed to be equal to
\(\frac{f''(0)}{f'(0)}\cdot \frac{5\Gamma (m+\frac{1}{2})}{96\sqrt{\pi }(m-1)!}\)
(see p. 9 of [
12
]), that is,
\(-k_f\cdot \frac{5\Gamma (m+\frac{1}{2})}{96\sqrt{\pi }(m-1)!}\)
(in our notation). This would mean that
\(b_{1/2}(C)\)
were equal to
\(\frac{f''(0)}{f'(0)}\cdot \frac{5}{96\sqrt{\pi }}\)
. Note that this expression is constant under constant rescalings of
f
and contradicts our formula for
\(b_{1,m}(C)\)
in Corollary
3.15
below, as well as its irrational dependence on
\(f'(0)\)
described in Section
4
.
(ii) The numbers
\(\nu (a)=\sqrt{a+\frac{1}{4}}\)
, when
a
runs through
\(\operatorname {spec}(A(0))\)
(with multiplicities) constitute the series
$$0, \alpha , \alpha , 2\alpha , 2\alpha , 3\alpha , 3\alpha , 4\alpha , 4\alpha , \dots $$
This follows immediately from (
4
), recalling that
\(\alpha =\frac{1}{f'(0)}\)
.
(iii) In the following we will use the Beta function
$$B(z,w)=\frac{\Gamma (z)\Gamma (w)}{\Gamma (z+w)}=\int _0^1 (1-t)^{z-1} t^{w-1}\,dt, $$
considered as a meromorphic function in
\(z\in \mathbb {C}\)
for each fixed
\(w\in \mathbb {C}\setminus \{0,-1,-2,\dots \}\)
, and vice versa. The integral on the right side converges only for
\(\operatorname {Re}(z)>0\)
and
\(\operatorname {Re}(w)>0\)
, but can, in other cases, be interpreted using the above formula.
(iv) The functional equation
\(\Gamma (z+1)=z\Gamma (z)\)
implies functional equations for the Beta function, for example:
$$B(z,w)=\frac{z+w}{w} B(z,w+1) \text{ and } B(z+1,w-1)=\frac{z}{w-1}B(z,w) $$
Corollary 3.4
Using
\(a=\nu (a)^2-\frac{1}{4}\)
, we conclude from Lemma
3.2
and Remark
3.3
(ii):
$$\begin{aligned} b_{1,m}(C)=-\frac{k_f}{4\sqrt{\pi }(m-1)!}{\operatorname {Res}_0}_{|s=0}\left[ \psi _m(s)\cdot h_\alpha (s)\right] , \end{aligned}$$
where
\(\psi _m\)
is the meromorphic function given by
$$\psi _m(s):=\frac{\Gamma (m+\frac{1}{2}+\tfrac{s}{2})\Gamma (-\frac{s}{2})}{\Gamma (-s)}, $$
and
$$\begin{aligned} \begin{aligned} h_\alpha (s):=&{}-\frac{1}{4}\cdot \frac{\Gamma (\frac{1}{2}+\frac{s}{2})\Gamma (-s)}{\Gamma (\frac{1}{2} - \frac{s}{2})} +2\sum _{n=1}^\infty \left( \alpha ^2 n^2-\frac{1}{4}\right) \frac{\Gamma (n\alpha +\frac{1}{2}+\frac{s}{2})\Gamma (-s)}{\Gamma (n\alpha +\frac{1}{2}-\frac{s}{2})}\\ \end{aligned} \end{aligned}$$
Remark 3.5
Note that
\(\psi _m\)
has no pole at
\(s=0\)
. Thus, it is holomorphic in some open neighborhood of
\(s=0\)
. Its value at
\(s=0\)
is
$$\psi _m(0)=2\,\Gamma (m+\tfrac{1}{2}) $$
The function
\(h_\alpha \)
is meromorphic in some neighborhood of
\(s=0\)
. We are going to show that
\(h_\alpha \)
does actually not have a pole in
\(s=0\)
, either; see Corollary
3.15
.
Definition 3.6
For each
\(\alpha >0\)
,
\(k\in \mathbb {N}_0\)
, and
z
in
$$\begin{aligned} W:=\{z\in \mathbb {C}: |z|<1 \text{ and } |1-z|<1\} \end{aligned}$$
(21)
we write
$$\begin{aligned} h_{k,\alpha }(z):=\sum _{n=0}^\infty \alpha ^k n^k (1-z)^{n\alpha }, \end{aligned}$$
where
\((1-z)^{n\alpha }:=\exp (n\alpha \log (1-z))\)
; here,
\(\log \)
denotes the main branch of the complex logarithm.
Note that for
\(n=0\)
, the summand
\(\alpha ^k n^k (1-z)^{n\alpha }\)
of
\(h_{k,\alpha }(z)\)
equals 1 for
\(k=0\)
(and 0 for
\(k>0\)
). Taking this into account, we obtain (noting that the term
\(+\frac{1}{4}\)
in the bracket of the following equation serves for achieving the correct coefficient
\(-\frac{1}{4}\)
in the first term of
\(h_\alpha (s)\)
from Corollary
3.4
):
Corollary 3.7
For the function
\(h_\alpha \)
from Corollary
3.4
we get, using the monotone convergence theorem for the integral over ]0, 1[,
$$\begin{aligned} h_\alpha (s)= \int _0^1\left( 2h_{2,\alpha }(t)-\frac{1}{2} h_{0,\alpha }(t)+\frac{1}{4}\right) (1-t)^{\frac{s}{2}-\frac{1}{2}} t^{-s-1}\,dt. \end{aligned}$$
NotationandRemarks 3.8
Let
\(\alpha >0\)
.
(i) For each
\(z\in W\)
(which was defined in (
21
)) we have
$$\begin{aligned} \begin{aligned} h_{0,\alpha }(z)&=\sum _{n=0}^\infty ((1-z)^\alpha )^n=\frac{1}{1-(1-z)^\alpha }= \frac{1}{\alpha z-\left( {\begin{array}{c}\alpha \\ 2\end{array}}\right) z^2+\left( {\begin{array}{c}\alpha \\ 3\end{array}}\right) z^3-\ldots }\\&=\frac{1}{\alpha z}\cdot \frac{1}{1-Q_\alpha (z)}=\frac{1}{\alpha z}+\frac{1}{2}\left( 1-\frac{1}{\alpha }\right) +O(z), \end{aligned} \end{aligned}$$
where
$$Q_\alpha (z)=\frac{1}{2}(\alpha -1)z-\frac{1}{6}(\alpha -1)(\alpha -2)z^2+\ldots $$
is a power series vanishing in
\(z=0\)
and converging for each
\(|z|<1\)
. Thus,
\(h_{0,\alpha }\)
has a meromorphic extension, denoted
\(h_{0,\alpha }\)
again, to the open unit disc and has a simple pole at
\(z=0\)
with residue
\(\frac{1}{\alpha }\)
. In particular, the function
$$ z\mapsto h_{0,\alpha }(z)-\frac{1}{\alpha z}=h_{0,\alpha }(z)-\frac{1}{\alpha }h_{0,1}(z) $$
is holomorphic in some open neighborhood of
\(z=0\)
.
(ii) More precisely, the meromorphic function
\(h_{0,\alpha }\)
on the open unit disc has a pole in
z
if and only if
\(|1-z|=1\)
and
$$\log (1-z)\in i\cdot \left( \tfrac{2\pi }{\alpha }\mathbb {Z}\,\cap \,]-\tfrac{\pi }{3},\tfrac{\pi }{3}[\,\right) $$
(in fact, if
\(|1-z|=1\)
then the condition
\(|z|<1\)
is equivalent to
\(\log (1-z)\in i\,]-\frac{\pi }{3},\frac{\pi }{3}[\)
). For
\(\alpha \le 6\)
, this is satsfied only for
\(z=0\)
. For
\(\alpha >6\)
, there are additional poles in the open unit disc. Among these, the ones with the smallest nonzero distance to
\(z=0\)
are the points
\(1-\exp (\pm \frac{2\pi i}{\alpha })\)
with norm
\(2\left| \sin (\frac{\pi }{\alpha })\right| \)
. Thus, the function
\(z\mapsto h_{0,\alpha }(z) - \frac{1}{\alpha z}\)
is holomorphic on the open disc
$$\begin{aligned} V_\alpha :=\{z\in \mathbb {C}:|z|<r_\alpha \},\text { where }r_\alpha :={\left\{ \begin{array}{ll}1 &  \text { if }0<\alpha <6,\\ 2\left| \sin \tfrac{\pi }{\alpha }\right| &  \text { if }\alpha \ge 6, \end{array}\right. } \end{aligned}$$
(22)
and the above function is still holomorphic on
$$\begin{aligned} W_\alpha :=W\cup V_\alpha . \end{aligned}$$
(23)
(iii) For each
\(k\in \mathbb {N}_0\)
and
\(z\in W\)
, we have
$$\frac{d}{dz} h_{k,\alpha }(z)=\sum _{n=1}^\infty \alpha ^k n^k\cdot n\alpha (1-z)^{n\alpha -1}\cdot (-1) = -\frac{1}{1-z} h_{k+1,\alpha }(z). $$
Hence,
$$\begin{aligned} h_{k,\alpha }(z)=\left( -(1-z)\frac{d}{dz}\right) ^k h_{0,\alpha }(z). \end{aligned}$$
(24)
Consequently, (i) implies that for
each
\(k\in \mathbb {N}_0\)
, the function
\(h_{k,\alpha }\)
has a meromorphic extension to the open unit disc, with the same set of poles as
\(h_{0,\alpha }\)
. Moreover, since
\(h_{0,\alpha }(z)-\frac{1}{\alpha z}\)
is holomorphic near
\(z=0\)
, it follows that for each
\(k\in \mathbb {N}_0\)
, the singular part
\(h_{k,\alpha }^{\text {sing}}(z)\)
of the Laurent series of
\(h_{k,\alpha }(z)\)
at
\(z=0\)
is given by
$$\begin{aligned} \begin{aligned} h_{k,\alpha }^{\text {sing}}(z)=\frac{1}{\alpha }\left( -(1-z)\frac{d}{dz}\right) ^k\left( \frac{1}{z}\right) =\frac{1}{\alpha }h_{k,1}(z)=\frac{1}{\alpha }h_{k,1}^{\text {sing}}(z) \end{aligned} \end{aligned}$$
(25)
(iv) We denote the regular part of
\(h_{k,\alpha }(z)\)
with respect to the pole at
\(z=0\)
by
$$h_{k,\alpha }^{\text {reg}}(z):=h_{k,\alpha }(z)-h_{k,\alpha }^{\text {sing}}(z)=h_{k,\alpha }(z)-\frac{1}{\alpha }h_{k,1}(z). $$
This is again a holomorphic function on the open set
\(W_\alpha \)
from (
23
). Equation (
24
) implies that
\(h_{k,\alpha }^{\text {reg}}\)
satisfies the analogous equation
$$\begin{aligned} h_{k,\alpha }^{\text {reg}}(z)=\left( -(1-z)\frac{d}{dz}\right) ^k h_{0,\alpha }^{\text {reg}}(z). \end{aligned}$$
(26)
(v) For future use, we also introduce the following functions:
$$h_{k,\alpha }^{\text {pos}}(z):=h_{k,\alpha }^{\text {reg}}(z)-h_{k,\alpha }^{\text {reg}}(0) $$
and
$$\hat{h}_{k,\alpha }(z):=\frac{h_{k,\alpha }^{\text {pos}}(z)}{z} $$
These are again holomorphic on the open set
\(W_\alpha \)
from (
23
).
(vi) Note that
\(h_{0,\alpha }(z)\)
for general
\(\alpha >0\)
is not defined on any open neighborhood of
\(z=1\)
. However, it extends continuously (with value
\(h_{0,\alpha }(1)=1\)
) to the limit point
\(z=1\)
of the open set
\(W\subset W_\alpha \)
. Using equation (
24
), one easily sees that
each
of the functions
\(h_{k,\alpha }\)
extends continuously to
\(z=1\)
(with value
\(h_{k,\alpha }(1)=0\)
for
\(k>0\)
). Obviously, continuous extendability in
\(z=1\)
now follows for each of the functions
\(h_{k,\alpha }^{\text {reg}}\)
and
\(\hat{h}_{k,\alpha }\)
, too. In particular, for each
\(k\in \mathbb {N}_0\)
and
\(\alpha >0\)
, we obtain a continuous function
$$\hat{h}_{k,\alpha }:[0,1]\rightarrow \mathbb {R} $$
on the closed unit interval (which coincides with the restriction of the holomorhpic function
\(\hat{h}_{k,\alpha }:W_\alpha \rightarrow \mathbb {C}\)
on the half-open interval [0, 1[ ).
Lemma 3.9
For each
\(\alpha >0\)
we have:
(i)
$$\int _0^1 h_{0,\alpha }^{\text {sing}}(t)(1-t)^{\frac{s}{2}-\frac{1}{2}}t^{-s-1}\,dt =\frac{1}{2\alpha }\int _0^1 (1-t)^{\frac{s}{2} - \frac{1}{2}}t^{-s-1}\,dt. $$
(ii)
The function
$$s\mapsto \int _0^1 h_{2,\alpha }^{\text {sing}}(t)(1-t)^{\frac{s}{2}-\frac{1}{2}}t^{-s-1}\,dt $$
vanishes identically in
\(s\in \mathbb {C}\)
.
Proof
(i) By Remark
3.8
(i),
$$\begin{aligned} h_{0,\alpha }^{\text {sing}}(z)=\frac{1}{\alpha z}. \end{aligned}$$
(27)
Thus, the left hand side of the statement equals
$$\alpha ^{-1}B\left( \frac{s}{2}+\frac{1}{2},-s-1\right) =\alpha ^{-1}\cdot \frac{\frac{s}{2}+\frac{1}{2}-s-1}{-s-1}B\left( \frac{s}{2}+\frac{1}{2},-s\right) =\frac{1}{2\alpha }B\left( \frac{s}{2}+\frac{1}{2},-s\right) , $$
where we have used Remark
3.3
(iv) in the first equation.
(ii) By equation (
25
),
$$\begin{aligned} \alpha h_{2,\alpha }^{\text {sing}}(z)=\left( -(1-z)\frac{d}{dz}\right) \left( (1-z)\frac{1}{z^2}\right) =(1-z)^2\frac{2}{z^3}+(1-z)\frac{1}{z^2} \end{aligned}$$
Thus,
$$\begin{aligned} \begin{aligned} \int _0^1 \alpha h_{2,\alpha }^{\text {sing}}(t)(1-t)^{\frac{s}{2}-\frac{1}{2}}t^{-s-1}\,dt&=2B\left( \frac{s}{2}+\frac{5}{2}, -s-3\right) +B\left( \frac{s}{2}+\frac{3}{2},-s-2\right) \\  &=\left[ 2\frac{\frac{s}{2}+\frac{3}{2}}{-s-3}+1\right] B\left( \frac{s}{2}+\frac{3}{2},-s-2\right) =0, \end{aligned} \end{aligned}$$
where Remark
3.3
(iv) is used in the last equation.
\(\square \)
Definition 3.10
(i) For each
\(\alpha >0\)
we define a complex power series
\(P_\alpha (w)\)
by
$$P_\alpha (w):=\sum _{j=0}^\infty \frac{1}{(j+1)!}B_{j+1}\alpha ^{j+1} w^j, $$
where the
\(B_j\)
denote the Bernoulli numbers. The radius of convergence of
\(P_\alpha \)
is
$$R_\alpha :=\frac{2\pi }{\alpha }\,. $$
We write
$$U_\alpha :=\{z\in \mathbb {C}: |z|<1 \text { and } |\log (1-z)|<R_\alpha \}. $$
(ii) We define a families of holomorphic functions
\(\Phi _k\)
and
\(\hat{\Phi }_k\)
(
\(k\in \mathbb {N}_0\)
) on the open unit disc
\(\{z\in \mathbb {C}:|z|<1\}\)
by
$$\begin{aligned} \begin{aligned} \Phi _k(z)&:=\left( -(1-z)\frac{d}{dz}\right) ^k\left( \frac{1}{z}+\frac{1}{\log (1-z)}\right) ,\\ \hat{\Phi }_k(z)&:=\frac{\Phi _k(z)-\Phi _k(0)}{z}\,. \end{aligned} \end{aligned}$$
Remark 3.11
(i) The
k
th derivative
\(P^{(k)}\)
of
\(P_\alpha \)
satisfies
$$\begin{aligned} P^{(k)}_\alpha (w)=\sum _{j=0}^\infty \frac{1}{j!\cdot (j+k+1)}B_{j+k+1}\alpha ^{j+k+1}w^j \end{aligned}$$
(28)
for all
\(w\in \mathbb {C}\)
with
\(|w|<R_\alpha \)
.
(ii) The functions
\(\Phi _k\)
are indeed holomorphic on the open unit disc because the singularity of
\(\Phi _0\)
at
\(z=0\)
is removable (with value
\(\Phi _0(0)=\frac{1}{2}\)
). Consequently, the functions
\(\hat{\Phi }_k\)
, too, are holomorphic on the open unit disc. Moreover, we note that the functions
\(\Phi _k\)
continuously extend to the limit point
\(z=1\)
(with value 1 for
\(k=0\)
and value 0 for
\(k>0\)
). Consequently, the functions
\(\hat{\Phi }_k\)
, too, continuously extend to the point
\(z=1\)
. In particular,
\(\Phi _k\)
and
\(\hat{\Phi }_k\)
induce continuous functions
\(\Phi _k:[0,1]\rightarrow \mathbb {R}\)
and
\(\hat{\Phi }_k:[0,1]\rightarrow \mathbb {R}\)
, respectively.
Lemma 3.12
Using the notation of
3.8
, we have the following for each
\(\alpha >0\)
:
(i)
For all
\(z\in U_\alpha \)
,
$$\begin{aligned} \begin{aligned} h_{0,\alpha }(z)&=-\frac{1}{\alpha \log (1-z)}-\frac{1}{\alpha }P_\alpha (\log (1-z))\text { and }\\ h_{0,\alpha }^{\text {reg}}(z)&=-\frac{1}{\alpha }\Phi _0(z)-\frac{1}{\alpha }P_\alpha (\log (1-z)). \end{aligned} \end{aligned}$$
Moreover, for all
\(z\in U_\alpha \cap U_1\)
,
$$h_{0,\alpha }^{\text {reg}}(z)=\frac{1}{\alpha }(P_1-P_\alpha )(\log (1-z)). $$
(ii)
For each
\(k\in \mathbb {N}_0\)
and all
\(z\in U_\alpha \)
,
$$\begin{aligned} h_{k,\alpha }^{\text {reg}}(z)=-\frac{1}{\alpha }\Phi _k(z)-\frac{1}{\alpha }P_\alpha ^{(k)}(\log (1-z)). \end{aligned}$$
(29)
Moreover, for all
\(z\in U_\alpha \cap U_1\)
,
$$\begin{aligned} \begin{aligned} h_{k,\alpha }^{\text {reg}}(z)&=\frac{1}{\alpha }(P^{(k)}_1-P^{(k)}_\alpha )(\log (1-z))\\&=\frac{1}{\alpha }\sum _{j=0}^\infty \frac{1}{j!\cdot (j+k+1)}B_{j+k+1}(1-\alpha ^{j+k+1})(\log (1-z))^j. \end{aligned} \end{aligned}$$
In particular,
$$\begin{aligned} h_{k,\alpha }^{\text {reg}}(0)=\frac{1}{\alpha }\cdot \frac{1}{k+1}B_{k+1}(1-\alpha ^{k+1}). \end{aligned}$$
(30)
(iii)
For each
\(k\in \mathbb {N}_0\)
and all
\(z\in U_\alpha \)
,
$$\begin{aligned} \begin{aligned} \hat{h}_{k,\alpha }(z)&=-\frac{1}{\alpha }\hat{\Phi }_k(z)-\frac{1}{\alpha z} (P_\alpha ^{(k)}(\log (1-z))-P_\alpha ^{(k)}(0))\\&=-\frac{1}{\alpha }\hat{\Phi }_k(z)-\frac{1}{\alpha z}\sum _{j=1}^\infty \frac{1}{j!\cdot (j+k+1)}B_{j+k+1}\alpha ^{j+k+1}(\log (1-z)^j). \end{aligned} \end{aligned}$$
(31)
Proof
(i) For all
\(z\in U_\alpha \)
we have
$$\begin{aligned} \begin{aligned} h_{0,\alpha }(z)&=\frac{1}{1-(1-z)^\alpha }=\frac{1}{1-\exp (\alpha \log (1-z))}\\  &=-\frac{\alpha \log (1-z)}{\exp (\alpha \log (1-z))-1}\cdot \frac{1}{\alpha \log (1-z)}\\&=-\sum _{\ell =0}^\infty \frac{1}{\ell !}B_\ell (\alpha \log (1-z))^{\ell }\cdot \frac{1}{\alpha \log (1-z)}=-\frac{1}{\alpha \log (1-z)}-\frac{1}{\alpha }P_\alpha (\log (1-z)). \end{aligned} \end{aligned}$$
This shows the first statement. The second statement follows by (
27
). In order to conclude the third statement, we let
\(\alpha =1\)
in the first statement, which gives
$$P_1(\log (1-z))=-h_{0,1}(z)-\frac{1}{\log (1-z)}=-\frac{1}{z}-\frac{1}{\log (1-z)}=-\Phi _0(z) $$
for all
\(z\in U_1\)
.
(ii) This follows from (i) using (
26
), (
28
), and
$$\left( -(1-z)\frac{d}{dz}\right) (\log (1-z)^j)=j(\log (1-z))^{j-1} $$
for all
\(j\in \mathbb {Z}\)
.
(iii) This is an immediate consequence of (
29
), (
28
), and
\(\log (1)=0\)
.
\(\square \)
Remark 3.13
Note that the open set
\(U_\alpha \)
on which
\(P_\alpha (\log (1-z))\)
converges does, in general, not contain the entire open disc
\(V_\alpha \)
from (
22
) on which the functions
\(h_{k,\alpha }^{\text {reg}}\)
are holomorphic. The reason is that the formulas from Lemma
3.12
do not directly express
\(h_{k,\alpha }^{\text {reg}}(z)\)
as a power series in
z
. Doing this would rearrange the summation and make the resulting power series converge on
\(V_\alpha \)
.
Proposition 3.14
The function
\(h_\alpha \)
from Corollary
3.4
satisfies
$$\begin{aligned} \begin{aligned} h_\alpha (s)&=\int _0^1\left( 2h_{2,\alpha }^{\text {pos}}(t)-\frac{1}{2} h_{0,\alpha }^{\text {pos}}(t)\right) (1-t)^{\frac{s}{2}-\frac{1}{2}} t^{-s-1}\,dt\\&=\int _0^1\left( 2\hat{h}_{2,\alpha }(t)-\frac{1}{2} \hat{h}_{0,\alpha }(t)\right) (1-t)^{\frac{s}{2}-\frac{1}{2}} t^{-s}\,dt, \end{aligned} \end{aligned}$$
where
\(h_{k,\alpha }^{\text {pos}}\)
and
\(\hat{h}_{k,\alpha }\)
are defined as in
3.8
(v).
Proof
Note that the second equation is immediate, so it remains to show the first equation. Recall from Corollary
3.7
that
$$h_\alpha (s)= \int _0^1\left( 2h_{2,\alpha }(t)-\frac{1}{2} h_{0,\alpha }(t)+\frac{1}{4}\right) (1-t)^{\frac{s}{2}-\frac{1}{2}} t^{-s-1}\,dt. $$
We already know from Lemma
3.9
(ii) that we can replace
\(h_{2,\alpha }\)
by
\(h_{2,\alpha }^{\text {sing}}\)
in this formula. Moreover, by (
30
) and
\(B_{0+2+1}=B_3=0\)
,
$$\begin{aligned} h_{2,\alpha }^{\text {reg}}(0)=0, \end{aligned}$$
so we can actually replace
\(h_{2,\alpha }\)
by
\(h_{2,\alpha }^{\text {pos}}\)
in the above formula. It remains to show that
$$\begin{aligned} \int _0^1\left( -\frac{1}{2} h_{0,\alpha }^{\text {sing}}(t)-\frac{1}{2} h_{0,\alpha }^{\text {reg}}(0)+\frac{1}{4}\right) (1-t)^{\frac{s}{2}-\frac{1}{2}} t^{-s-1}\,dt=0. \end{aligned}$$
(32)
By Remark
3.8
(i) (or (
30
) and
\(B_1=-\frac{1}{2}\)
) we have
$$\begin{aligned} h_{0,\alpha }^{\text {reg}}(0)=-\frac{1}{2}\left( \frac{1}{\alpha }-1\right) , \end{aligned}$$
giving
\(-\frac{1}{2} h_{0,\alpha }^{\text {reg}}(0)+\frac{1}{4}=\frac{1}{4\alpha }\)
. Now (
32
) follows from Lemma
3.9
(i).
\(\square \)
Using continuity of the functions
\(\hat{h}_{k,\alpha }\)
on the closed interval [0, 1] (recall
3.8
(vi)), we now obtain:
Corollary 3.15
The function
\(h_\alpha \)
from Corollary
3.4
has a finite value at
\(s=0\)
. In particular, that Corollary together with Remark
3.5
and Proposition
3.14
implies
$$\begin{aligned} \begin{aligned} b_{1,m}(C)&=-\frac{k_f}{4\sqrt{\pi }(m-1)!}\psi _m(0)h_\alpha (0)\\&=-\frac{k_f \cdot \Gamma (m+\frac{1}{2})}{\sqrt{\pi }(m-1)!}\int _0^1 \left( \hat{h}_{2,\alpha }(t)-\frac{1}{4}\hat{h}_{0,\alpha }(t)\right) (1-t)^{-\frac{1}{2}}\,dt\\&=-\frac{2 k_f \cdot \Gamma (m+\frac{1}{2})}{\sqrt{\pi }(m-1)!}\int _0^1 \left( \hat{h}_{2,\alpha }(1-u^2)-\frac{1}{4}\hat{h}_{0,\alpha }(1-u^2)\right) \,du, \end{aligned} \end{aligned}$$
where, as introduced before,
\(k_f=-f''(0)/f'(0)\)
,
\(\alpha =1/f'(0)\)
, and the functions
\(\hat{h}_{k,\alpha }\)
are defined as in
3.8
(v). Using (
18
), we finally conclude
$$\begin{aligned} b_{1/2}(C) =-\frac{2 k_f}{\sqrt{\pi }}\int _0^1\left( \hat{h}_{2,\alpha }(1-u^2)-\frac{1}{4}\hat{h}_{0,\alpha }(1-u^2)\right) \,du \end{aligned}$$
(33)
4
Irrational dependence of
\(b_{1/2}(C)\)
on constant rescalings of the distance circles
In this section, we will show that if
\(f''(0)\ne 0\)
then, under rescalings
\(\lambda f\)
of
f
by a constant
\(\lambda >0\)
, the coefficient
\(b_{1/2}(C)\)
is
not
a rational function of
\(\lambda \)
. Since, by
2.1
, the length of the distance circles is
\(2\pi f(r)\)
for small
\(r>0\)
, this means that
\(b_{1/2}(C)\)
does not depend rationally on the scaling factor for constant rescalings of small distance circles aronnd
C
if
\(f''(0)\ne 0\)
. Note that the factor
\(k_f=-f''(0)/f'(0)\)
in (
33
) is invariant under such rescalings, while
\(f'(0)\)
changes linearly. Recall that
\(\alpha \)
is just the inverse of
\(f'(0)\)
. So, what we intend to show is that the integral in (
33
) – or, equivalently,
\(\alpha \)
times that integral – is not a rational function of the parameter
\(\alpha \)
. The aim of this section is, thus, to prove the following theorem:
Theorem 4.1
$$\begin{aligned} F:]0,\infty [\ni \alpha \mapsto \int _0^1\left( \alpha \hat{h}_{2,\alpha }(1-u^2)-\frac{1}{4}\alpha \hat{h}_{0,\alpha }(1-u^2)\right) \,du\in \mathbb {R} \end{aligned}$$
(34)
is not a rational function of
\(\alpha \)
. In particular, if
\(f''(0)\ne 0\)
then
\(b_{1/2}(C)\)
does not change rationally under constant rescalings of the distance circles near the singularity
C
.
We first give several preparations for the proof.
Definition 4.2
For each
\(\alpha >0\)
let
$$\begin{aligned} c_\alpha :=e^{-\frac{\pi }{2\alpha }}. \end{aligned}$$
Lemma 4.3
For each
\(k\in \mathbb {N}_0\)
there exists a constant
\(\Lambda _k>0\)
, independent of
\(\alpha \)
, such that for each
\(0<\alpha \le 1\)
,
$$\max \left\{ |\alpha \hat{h}_{k,\alpha }(1-u^2)|:u\in [0,c_\alpha ]\right\} \le \Lambda _k\,. $$
Proof
The definitions and formulas of
3.8
together with (
30
) imply that
$$\begin{aligned} \begin{aligned} \alpha \hat{h}_{k,\alpha }(z)&=\frac{1}{z}\left( \alpha \left( -(1-z)\frac{d}{dz}\right) ^k h_{0,\alpha }^{\text {reg}}(z)-\alpha h_{k,\alpha }^{\text {reg}}(0)\right) \\&=\frac{1}{z}\left( \left( -(1-z)\frac{d}{dz}\right) ^k \left( \frac{\alpha }{1-(1-z)^\alpha }-\frac{1}{z}\right) -\frac{1}{k+1}B_{k+1}(1-\alpha ^{k+1})\right) \end{aligned} \end{aligned}$$
This implies that for each fixed
\(k\in \mathbb {N}_0\)
,
\(\alpha \hat{h}_{k,\alpha }(z)\)
is a linear combination of finite products of the terms
$$\alpha , \ \frac{1}{z}, \ 1-z, \ \frac{1}{1-(1-z)^\alpha }, \ (1-z)^\alpha . $$
Consequently,
\(\alpha \hat{h}_{k,\alpha }(1-u^2)\)
is a linear combination of finite products of the terms
$$\alpha , \ \frac{1}{1-u^2}, \ u^2, \ \frac{1}{1-u^{2\alpha }}, \ u^{2\alpha }. $$
For each
\(0<\alpha \le 1\)
one has
\(c_\alpha \le e^{-\frac{\pi }{2}}<\frac{1}{2}\)
and, for every
\(u\in [0,c_\alpha ]\)
,
$$0\le u^2\le u^{2\alpha }\le e^{-\pi }<\frac{1}{2}\text { \ and \ }0<\frac{1}{1-u^2}\le \frac{1}{1-u^{2\alpha }}\le \frac{1}{1-e^{-\pi }}<2. $$
In view of the structure of
\(\alpha \hat{h}_{k,\alpha }(1-u^2)\)
described above, these estimates obviously imply the statement.
\(\square \)
Proposition 4.4
For each
\(j\in \mathbb {N}\)
write
$$\tau _j:]0,1[\ni u\mapsto \frac{(\log (u^2))^j}{1-u^2}\in \mathbb {R}\text {\ \ and\ \ }I_j:=\int _0^1\tau _j(u)\,du\in \mathbb {R}. $$
Then, for all
\(k\in \mathbb {N}_0\)
and
\(r\in \mathbb {N}\)
we have
$$\begin{aligned} \int _0^1\alpha \hat{h}_{k,\alpha }(1-u^2)\,du =-\int _0^1\hat{\Phi }_k(1-u^2)\,du -\sum _{j=1}^r\frac{I_j}{j!\cdot (j+k+1)}B_{j+k+1}\alpha ^{j+k+1} +o(\alpha ^{r+k+1}) \end{aligned}$$
(35)
as
\(\alpha \searrow 0\)
, where
\(\Phi _k\)
is as in Definition
3.10
(ii). In particular, for each
\(r\in \mathbb {N}\)
, the function
F
from (
34
) satisfies
$$\begin{aligned} \begin{aligned} F(\alpha ) ={}&-\int _0^1\left( \hat{\Phi }_2(1-u^2)-\frac{1}{4}\hat{\Phi }_0(1-u^2)\right) \,du\\&{}+\frac{I_1}{48}\alpha ^2 -\sum _{j=1}^r \left( \frac{I_j}{j!\cdot (j+3)}-\frac{1}{4}\cdot \frac{I_{j+2}}{(j+3)!}\right) B_{j+3}\alpha ^{j+3}+o(\alpha ^{r+3}) \end{aligned} \end{aligned}$$
as
\(\alpha \rightarrow 0\)
.
Proof
First of all, note that the numbers
\(I_j\)
are indeed finite: The integrand
\(\tau _j\)
of
\(I_j\)
extends continuously to
\(u=1\)
(with value
\(-\log '(1)=-1\)
for
\(j=1\)
and value 0 for
\(j>1\)
); moreover, powers of
\(\log \)
are integrable over the unit interval.
By
\(B_2=\frac{1}{6}\)
and the definition of
F
, the first statement of the lemma immediately implies the second. It remains to prove the first statement. Fix
\(k\in \mathbb {N}_0\)
. For any
\(\alpha >0\)
and
\(r\in \mathbb {N}\)
let
$$\begin{aligned} \begin{aligned} D_*(\alpha ,r)&:=\int _0^{c_\alpha } (\alpha \hat{h}_{k,\alpha }(1-u^2)+\hat{\Phi }_k(1-u^2))\,du+\sum _{j=1}^r\frac{\int _0^{c_\alpha }\tau _j(u)\,du}{j!\cdot (j+k+1)}B_{j+k+1}\alpha ^{j+k+1},\\ D^*(\alpha ,r)&:=\int _{c_\alpha }^1 (\alpha \hat{h}_{k,\alpha }(1-u^2)+\hat{\Phi }_k(1-u^2))\,du+\sum _{j=1}^r\frac{\int _{c_\alpha }^1\tau _j(u)\,du}{j!\cdot (j+k+1)}B_{j+k+1}\alpha ^{j+k+1}, \end{aligned} \end{aligned}$$
where
\(c_\alpha =e^{-\frac{\pi }{2\alpha }}\)
as in Definition
4.2
. For the rest of this proof, we may assume that
\(\alpha <1\)
; in particular,
\(c_\alpha <\frac{1}{2}\)
. Our aim is to show that
\(D_*(\alpha ,r)+D^*(\alpha ,r)\in o(\alpha ^{r+k+1})\)
as
\(\alpha \searrow 0\)
.
We will first show that
\(D_*(\alpha ,r)\in o(\alpha ^\infty )\)
, meaning that it is in
\(o(\alpha ^n)\)
for each
\(n\in \mathbb {N}\)
, as
\(\alpha \searrow 0\)
. From Lemma
4.3
and Remark
3.11
(ii) we easily conclude that the first integral in
\(D_*(\alpha ,r)\)
is indeed in
\(o(\alpha ^\infty )\)
. Moreover, for each
\(j\in \mathbb {N}\)
one has
\(\int \log ^j(v)\,dv=(-1)^j j!\cdot v\sum _{s=0}^j\frac{1}{s!}(-\log (v))^s\)
. Hence, recalling that
\(\log (c_\alpha )=-\frac{\pi }{2\alpha }\)
and
\(c_\alpha \in o(\alpha ^\infty )\)
, we have:
$$\left| \int _0^{c_\alpha }\tau _j(u)\,du\right| \le \frac{1}{1-c_\alpha ^2}\cdot \left| \int _0^{c_\alpha }\log ^j(u^2)\,du\right| <\frac{4}{3}\cdot 2^j j!\cdot c_\alpha \sum _{s=0}^j\frac{1}{s!}(\tfrac{\pi }{2})^s\alpha ^{-s}\in o(\alpha ^\infty ) $$
for each
\(j\in \mathbb {N}\)
. This implies
\(D_*(\alpha ,r)\in o(\alpha ^\infty )\)
.
In order to prove (
35
), it remains to show that
\(D^*(\alpha ,r)\in o(\alpha ^{r+k+1})\)
. Note that for
\(u\in [c_\alpha \,,1]\)
we have
\(|\log (u^2)|\le \frac{\pi }{\alpha }\)
. This implies that the compact set
\(\{1-u^2: u\in [c_\alpha \,,1]\}\)
is contained in
\(U_\alpha \)
; recall Definition
3.10
. In particular, the power series
\(P_\alpha ^{(k)}(w)\)
converges uniformly on the compact set
\(\{\log (u^2):u\in [c_\alpha \,,1]\}\)
. Using (
28
) and the fact that the function
\(u\mapsto \frac{\log (u^2)}{1-u^2}\)
is bounded on
\([c_\alpha \,,1]\)
, it follows that the series
$$\frac{1}{1-u^2}\sum _{j=1}^\infty \frac{(\log (u^2))^j}{j!\cdot (j+k+1)}B_{j+k+1}\alpha ^{j+k+1} $$
converges uniformly in
\(u\in [c_\alpha \,,1]\)
. By (
31
), the corresponding limit function is
$$u\mapsto -\alpha \hat{h}_{k,\alpha }(1-u^2)-\hat{\Phi }_k(1-u^2) $$
with
\(\hat{\Phi }_k\)
from Definition
3.10
(ii). In particular,
$$\sum _{j=1}^\infty \frac{\int _{c_\alpha }^1\tau _j(u)\,du}{j!\cdot (j+k+1)}B_{j+k+1}\alpha ^{j+k+1}=-\int _{c_\alpha }^1(\alpha \hat{h}_{k,\alpha }(1-u^2)+\hat{\Phi }_k(1-u^2))\,du. $$
Hence,
$$\begin{aligned} \begin{aligned} D^*(r,\alpha )&=-\sum _{j=r+1}^\infty \frac{\int _{c_\alpha }^1\tau _j(u)\,du}{j!\cdot (j+k+1)}B_{j+k+1}\alpha ^{j+k+1}\\&=-\alpha ^{r+k+2}\sum _{j=r+1}^\infty \frac{\int _{c_\alpha }^1\tau _j(u)\,du}{j!\cdot (j+k+1)}B_{j+k+1}\alpha ^{j-r-1}. \end{aligned} \end{aligned}$$
This is in
\(o(\alpha ^{r+k+1})\)
, as claimed.
\(\square \)
Corollary 4.5
The function
F
from (
34
) continuously extends to a function
\(F:[0,\infty [\,\rightarrow \mathbb {R}\)
. This function is infinitely differentiable at
\(\alpha =0\)
, and the corresponding Taylor series
\(T_{0}F\)
of
F
around 0 is given by
$$\begin{aligned} \begin{aligned} T_{0}F(\alpha ) ={}&-\int _0^1\left( \hat{\Phi }_2(1-u^2)-\frac{1}{4}\hat{\Phi }_0(1-u^2)\right) \,du\\&{}+\frac{I_1}{48}\alpha ^2 -\sum _{j=1}^\infty \left( \frac{I_j}{j!\cdot (j+3)}-\frac{1}{4}\cdot \frac{I_{j+2}}{(j+3)!}\right) B_{j+3}\alpha ^{j+3}, \end{aligned} \end{aligned}$$
where
\(I_j\)
is as in Proposition
4.4
.
Theorem 4.6
The Taylor series
\(T_0F\)
of
F
around 0 has convergence radius 0.
Proof
Since
\(B_{j+3}=0\)
if
\(j\in \mathbb {N}\)
is even, only the summands with
j
odd actually occur in
\(T_0F\)
. For each
\(n\in \mathbb {N}\)
one has (noting that
\(\log (u^2)=2\log (u)\)
)
$$I_{2n-1}=2^{2n-1}\frac{1-2^{2n}}{4n}\pi ^{2n}|B_{2n}|; $$
see, e.g., [
6
], p. 550. In particular, for each odd
\(j\in \mathbb {N}\)
,
$$I_j=2^j\cdot \frac{1-2^{j+1}}{2(j+1)}\pi ^{j+1}|B_{j+1}| \text { \ and \ }I_{j+2}=2^{j+2}\cdot \frac{1-2^{j+3}}{2(j+3)}\pi ^{j+3}|B_{j+3}|. $$
Let
$$V_j:=-\left( \frac{I_j}{j!\cdot (j+3)}-\frac{1}{4}\cdot \frac{I_{j+2}}{(j+3)!}\right) $$
for all
\(j\in \mathbb {N}\)
. Then for all odd
\(j\in \mathbb {N}\)
we obtain:
$$\begin{aligned} \begin{aligned} V_j&=2^j\left( \frac{2^{j+1}-1}{2(j+1)!\cdot (j+3)}{\pi ^{j+1}}|B_{j+1}|-\frac{2^{j+3}-1}{2(j+3)!\cdot (j+3)}\pi ^{j+3}|B_{j+3}|\right) \\&=\frac{2^{j-1}\pi ^{j+3}}{(j+3)!\cdot (j+3)}\left( (2^{j+1}-1)\frac{(j+2)(j+3)}{\pi ^2}|B_{j+1}|-(4\cdot 2^{j+1}-1)|B_{j+3}|\right) \\&=\frac{2^{j-1}\pi ^{j+3}|B_{j+3}|}{(j+3)!\cdot (j+3)}\left( (2^{j+1}-1)\frac{(j+2)(j+3)}{\pi ^2}\cdot \frac{|B_{j+1}|}{|B_{j+3}|}-(2^{j+3}-1)\right) \\&=\frac{2^{j-1}\pi ^{j+3}|B_{j+3}|}{(j+3)!\cdot (j+3)}\left( (2^{j+1}-1)D_j-(2^{j+3}-1)\right) , \end{aligned} \end{aligned}$$
where
$$D_j:=\frac{(j+2)(j+3)}{\pi ^2}\cdot \frac{|B_{j+1}|}{|B_{j+3}|}\,. $$
Bagul [
1
] recently proved that
$$\frac{2(2n)!}{\pi ^{2n}(2^{2n}-1)}\cdot \frac{3^{2n}}{3^{2n}-\alpha }<|B_{2n}|<\frac{2(2n)!}{\pi ^{2n}(2^{2n}-1)}\cdot \frac{3^{2n}}{3^{2n}-\beta } $$
for all
\(n\in \mathbb {N}\)
, all
\(\alpha \le 1\)
and all
\(\beta \ge 9(1-\frac{8}{\pi ^2})\approx 1.704875\)
. We use
\(\alpha :=1\)
,
\(\beta :=2\)
in this formula and conclude, for each odd
\(j\in \mathbb {N}\)
:
$$\begin{aligned} D_j>\frac{1}{9}\cdot \frac{(2^{j+3}-1)(3^{j+3}-2)}{(2^{j+1}-1)(3^{j+1}-1)}=\frac{(2^{j+3}-1)(3^{j+1}-\frac{2}{9})}{(2^{j+1}-1)(3^{j+1}-1)} \end{aligned}$$
and
$$\begin{aligned} \begin{aligned} (2^{j+1}-1)D_j-(2^{j+3}-1)&>\frac{(2^{j+3}-1)(3^{j+1}-\frac{2}{9})-(2^{j+3}-1)(3^{j+1}-1)}{3^{j+1}-1}\\&=\frac{7}{9}\cdot \frac{2^{j+3}-1}{3^{j+1}-1} \end{aligned} \end{aligned}$$
Consequently,
$$V_j>\frac{2^{j-1}\pi ^{j+3}|B_{j+3}|}{(j+3)!\cdot (j+3)}\cdot \frac{7}{9}\cdot \frac{2^{j+3}-1}{3^{j+1}-1}>0 $$
for each odd
\(j\in \mathbb {N}\)
. Using
\(\limsup _{j\rightarrow \infty }\root j+3 \of {|B_{j+3}|/(j+3)!}=\frac{1}{2\pi }\)
, we conclude
$$\begin{aligned} \limsup _{j\rightarrow \infty }\root j+3 \of {|V_j|}\ge \frac{2}{3}>0. \end{aligned}$$
(36)
Recall from Corollary
4.5
that the coefficient of
\(\alpha ^{j+3}\)
in
\(T_0F(\alpha )\)
is
\(V_j\cdot B_{j+3}\)
for each odd
\(j\in \mathbb {N}\)
. Now (
36
) implies that
$$\limsup _{j\rightarrow \infty }\root j+3 \of {|V_j|\cdot |B_{j+3}|}=\infty . $$
Thus, the radius of convergence of
\(T_0F\)
is indeed zero.
\(\square \)
Proof of Theorem 4.1
By Theorem
4.6
, the continuous extension
\(F:[0,\infty [ \rightarrow \mathbb {R}\)
from Corollary
4.5
of our original
\(F:]0,\infty [ \rightarrow \mathbb {R}\)
cannot coincide with the restriction of any analytic function. Since rational functions are analytic,
F
cannot be rational. Theorem
4.1
now follows.
\(\square \)
Data Availability
No datasets were generated or analysed during the current study.
References
Bagul, Y.J.: Stringent bounds for the non-zero Bernoulli numbers, preprint, (2023),
https://arxiv.org/abs/2303.14532
Brüning, J., Seeley, R.: The resolvent expansion for second order regular singular operators. J. Funct. Anal.
73
(2), 369–429 (1987)
Article
MathSciNet
Google Scholar
Brüning, J., Seeley, R.: The Expansion of the Resolvent near a Singular Stratum of Conical Type. J. Funct. Anal.
95
(2), 255–290 (1991)
Article
MathSciNet
Google Scholar
Cheeger, J.: Spectral geometry of singular Riemannian spaces. J. Differential Geom.
18
(4), 575–657 (1983)
Article
MathSciNet
Google Scholar
Dryden, E.B., Gordon, C.S., Greenwald, S.J., Webb, D.L.: Asymptotic expansion of the heat kernel for orbifolds. Michigan J. Math.
56
(1), 205–238 (2008)
Article
MathSciNet
Google Scholar
Gradshteyn, I.S., Ryzhik, I.M.: Table of integrals, series and products, 7th edn. Elsevier/Academic Press Inc., Amsterdam (2007)
Google Scholar
Hartmann, L., Lesch, M., Vertman, B.: On the domain of Dirac and Laplace type operators on stratified spaces. J. Spectr. Theory
8
(4), 1295–1348 (2018)
Article
MathSciNet
Google Scholar
Hartmann, L., Lesch, M., Vertman, B.: Resolvent trace asymptotics on stratified spaces. Pure Appl. Anal.
3
(1), 75–108 (2021)
Article
MathSciNet
Google Scholar
Lesch, M.: Operators of Fuchs type, conical singularitieres, and asymptotic methods, Teubner Texte zur Mathematik, vol. 136. Teubner-Verlag, Leipzig (1997)
Google Scholar
Schueth, D.: On the corner contributions to the heat coefficients of geodesic polygons. Ann. Inst. Fourier
69
(7), 2827–2855 (2019)
Article
MathSciNet
Google Scholar
Suleymanova, A.: On the spectral geometry of manifolds with conical singularities, PhD thesis (2017), Humboldt-Universität zu Berlin, edoc-Server,
https://doi.org/10.18452/18420
Suleymnova, A.: Spectral geometry of surfaces with curved conic singularities, preprint, (2017),
https://arxiv.org/abs/1711.00577
Uçar, E.: Spectral invariants for polygons and orbisurfaces, PhD thesis (2017), Humboldt-Universität zu Berlin, edoc-Server,
https://doi.org/10.18452/18463
(also:
https://arxiv.org/abs/1711.03405
)
Download references
Author information
Authors and Affiliations
Institut für Mathematik, Humboldt-Universität zu Berlin, 10099, Berlin, Germany
Dorothee Schueth
Authors
Dorothee Schueth
View author publications
Search author on:
PubMed
Google Scholar
Contributions
Dorothee Schueth is the only author of this manuscript.
Corresponding author
Correspondence to
Dorothee Schueth
.
Ethics declarations
Competing interests
The authors declare no competing interests.
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
Schueth, D. Heat coefficients of surfaces with curved conical singularities.
Ann Glob Anal Geom
69
, 2 (2026). https://doi.org/10.1007/s10455-025-10024-1
Download citation
Received
:
30 September 2025
Accepted
:
27 November 2025
Published
:
08 December 2025
Version of record
:
08 December 2025
DOI
:
https://doi.org/10.1007/s10455-025-10024-1
Share this article
Anyone you share the following link with will be able to read this content:
Get shareable link
Sorry, a shareable link is not currently available for this article.
Copy shareable link to clipboard
Provided by the Springer Nature SharedIt content-sharing initiative
Keywords
Laplace operator
Heat kernel
Heat coefficients
Surfaces
Conic singularities
Mathematics Subject Classification
58J50