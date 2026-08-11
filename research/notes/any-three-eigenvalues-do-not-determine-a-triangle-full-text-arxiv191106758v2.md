---
title: Any three eigenvalues do not determine a triangle (full text, arXiv:1911.06758v2)
id: any-three-eigenvalues-do-not-determine-a-triangle-full-text-arxiv191106758v2
tags:
- hyperbolic-pillow-heat-novelty-813161
- rigorous-numerics
- triangle-eigenvalues
- finite-spectral-data
created: '2026-08-09T08:51:01.526360Z'
updated: '2026-08-09T09:36:32.533090Z'
source: https://arxiv.org/pdf/1911.06758
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Gomez-Serrano & Orriols (arXiv:1911.06758v2; published J. Differential Equations,
  DOI 10.1016/j.jde.2020.11.002). Theorem 1.1: there exist two non-isometric triangles
  T_A, T_B with matching Dirichlet eigenvalues lambda_i(T_A)=lambda_i(T_B) for i=1,2,4,
  refuting Antunes-Freitas''s numerical conjecture that the first three eigenvalues
  determine a triangle, and answering Open Problem 1 of Grieser-Maronna (Notices AMS
  60(11):1440-1447) and Conjecture 3 of Lu-Rowlett (Amer. Math. Monthly 122(9):815-835).
  METHOD (this is the technique the query asked to record): NOT a stability/perturbation
  estimate -- an EXISTENCE proof via rigorous computer-assisted verification. Two
  passes: (1) verified finite-element eigenvalue enclosures using Crouzeix-Raviart
  a priori error bounds (Theorem 2.1: lambda_h,k/(1+C_h^2 lambda_h,k) <= lambda_k
  with explicit constant C_h <= 0.1893h) to bracket eigenvalue ratios xi_21=lambda2/lambda1
  and xi_41=lambda4/lambda1 to high precision; (2) interval arithmetic propagates
  these bounds to two small parallelogram regions in the space of third-vertex coordinates,
  centered near A=(0.63500,0.27500) and B=(0.84906,0.31995) with side vectors of magnitude
  ~0.001-0.007 (e.g. v21,A=(0.004610608896618232,0.0012403688839389946)). The Poincare-Miranda
  theorem (a topological generalization of the intermediate value theorem / Brouwer,
  cited as C. Miranda 1940) is applied to the validated sign pattern on the parallelogram
  boundary to PROVE, rigorously and non-approximately, that an exact coincidence point
  exists inside each box -- i.e. closeness is quantified as a certified-small enclosure
  box (~10^-3 in vertex-coordinate space) within which an EXACT (not merely near)
  eigenvalue coincidence is guaranteed to exist. This is qualitatively different from
  a stability/conditioning theorem: it proves existence of an exact degeneracy near
  a numerically observed one, not a bound relating perturbation size in eigenvalues
  to perturbation size in triangle parameters.'
---

arXiv:1911.06758v2  [math.AP]

arXiv:1911.06758v2  [math.AP]  21 Jan 2020
ANY THREE EIGENVALUES DO NOT DETERMINE A TRIANGLE
JAVIER G´OMEZ-SERRANO∗AND GERARD ORRIOLS
Abstract. Despite the moduli space of triangles being three dimensional, we prove the existence
of two triangles which are not isometric to each other for which the ﬁrst, second and fourth Dirichlet
eigenvalues coincide, establishing a numerical observation from Antunes–Freitas [1]. The two tri-
angles are far from any known, explicit cases. To do so, we develop new tools to rigorously enclose
eigenvalues to a very high precision, as well as their position in the spectrum. This result is also
mentioned as (the negative) part of [35, Conjecture 6.46], [23, Open Problem 1] and [39, Conjecture
3].
1. Introduction
Mark Kac coined the term “hearing the shape of a drum” [32] in 1965 for the problem of
the determination of a domain D given the spectrum of the Laplacian. Since then, the spectral
determination of (mostly planar) domains has become a fundamental question in geometric analysis.
Throughout this paper we will work with Dirichlet boundary conditions, that is, we will consider
the set of real numbers 0 < λ1 < λ2 ≤λ3 ≤. . . that solve
−∆uk = λkuk in D
uk = 0 on ∂D.
(1)
Most of the results in the literature are negative. In particular, for euclidean polygons, the ﬁrst
example of a pair of non-isometric polygons with the same spectrum is due to Gordon, Webb and
Wolpert [22]. In the case of Riemannian manifolds, even the local geometry of isospectral manifolds
can be diﬀerent [53].
We now mention some of the very few positive results for the inverse spectral problem. For
negatively curved manifolds, there are spectral rigidity [11, 24] and compactness results [44], some
of which have been recently extended to Anosov surfaces [48].
See also [43, 45] for a proof of
these compactness results in the case of planar domains. Zelditch [57] showed, by computing wave
invariants, that any analytic bounded planar domain that has an even symmetry with respect to
a line is spectrally determined. This was later generalized to higher dimensional domains [27].
Without any symmetry and analyticity assumptions, only few results exist on the plane: a family
of perturbed disks [55], semi-regular polygons in the class of convex piecewise smooth domains
[13] and very recently, Hezari and Zelditch [28] have shown that ellipses of small eccentricity are
spectrally determined in the class of smooth domains, even without assumptions on convexity or
closeness to the ellipse.
Instead of focusing on a wide class of domains, one could try to solve the inverse spectral problem
in a smaller class. Simple, positive examples include the regular n-gon in the class of n-gons (due
to the isoperimetric inequality) or rectangles in the class of rectangles (since the eigenvalues are
explicit). A nontrivial result is to show that triangles are determined in the class of triangles (see [12]
for a proof using the wave trace and a simpler one [23] that only uses the heat kernel and elementary
calculations). Recently, trapezoids have been shown to be determined in the class of trapezoids
(under Neumann boundary conditions) [26], as well as parallelograms and acute trapezoids [39] in
their respective classes.
1


However, most known results use the full spectrum (i.e. an inﬁnite amount of quantities); the
only non-explicit results using only ﬁnitely many eigenvalues rely on isoperimetric inequalities, most
remarkably the Payne–P´olya–Weinberger conjecture proved by Ashbaugh and Benguria [3], which
implies that the ﬁrst two eigenvalues determine the disk among all domains of Rn. See [25] for a
discussion on extremizers of functions of eigenvalues. Being in a ﬁnite dimensional ambient space
(such as the space of n-gons for a ﬁxed n) it is expected that a ﬁnite amount of eigenvalues should
suﬃce to characterize an n-gon. Chang and DeTurck [10] showed that given a triangle T, there is
a ﬁnite number N(T) such that the ﬁrst N(T) eigenvalues distinguish T from any other triangle.
However, N(T) is not known to be uniformly bounded. Since the moduli space of triangles is 3
dimensional, it is conceivable (see [34]) that 3 eigenvalues could characterize every triangle. Our
paper is a ﬁrst step in this direction by showing (on the negative) that if that is the case, not any
3 eigenvalues suﬃce. Speciﬁcally we prove the following theorem:
Theorem 1.1. There exist two triangles TA and TB, not isometric to each other, such that λi(TA) =
λi(TB), for i = 1, 2, 4.
Antunes and Freitas [1] had observed numerically the presence of a saddle point for λ4/λ1 around
which λ2/λ1 is regular, which would imply the existence of such two triangles (see Figure 1).
Moreover they conjectured that the three ﬁrst eigenvalues λ1, λ2 and λ3 do determine the shape of
a triangle. This question has recently attracted a lot of attention. Laugesen and Siudeja mention
both (positive and negative) directions in [35, Conjecture 6.46], as well as Grieser and Maronna
[23, Open Problem 1] and Lu and Rowlett [39, Conjecture 3]. Despite being the simplest polygonal
class, the spectral theory of triangles is far from well understood and many advances have been
made recently, for example [31], [29] and [46].
Remark 1.2. With no extra eﬀort, we also show that there exists an open set in the moduli space
of triangles such that for every triangle from this set there is another one with the same eigenvalues
λi, i = 1, 2, 4.
We do not know how to show the existence of a saddle point for the quotient of two eigenvalues
in a region far away from the explicit triangles; that would require controlling up to two derivatives
of the eigenvalues, which have very diﬃcult expressions. Instead, we use a topological argument
relying only on “C0 computations” and using very tight, rigorous enclosures of eigenvalues, as
well as a control of their position in the spectrum. While upper bounds are easy to obtain using
Rayleigh–Ritz quotients over suitable test functions, guaranteed lower bounds (and indices) are
much more diﬃcult.
There are many classical results in the literature [33, 36, 6, 15, 41, 52] showing the existence
of an eigenvalue close to an approximate one. The main philosophy is that if (λapp, uapp) is an
eigenpair that satisﬁes the equation up to an error bounded by δ, then there is a true eigenpair
(λ, u) at a distance Cδk. Recently, Barnett and Hassell [4] improved on the classical estimates by
a factor of O(
√
λ) using quasi-orthogonality arguments. Unfortunately, none of these results can
assert the position in the spectrum of the eigenvalue without knowing any a priori bounds.
In order to circumvent this issue and obtain the position, Plum [49] proposed a homotopy method
linking the eigenvalues of the domain of the problem with another, known domain (the base prob-
lem). See also the intermediate method [56, 17, 5] for another example of connecting the problem
to a known domain. The diﬃculty in our case is that we have to solve many eigenvalue prob-
lems and all of them are far from any known domain, yielding impractical times at the precision
needed. In [38] and [37], Liu and Oishi found rigorous lower bounds in terms of the solutions of a
ﬁnite dimensional problem given by a Finite Element Method discretization (see also [9] for similar
bounds). Again, at the level of the required precision for Theorem 1.1 the number of elements that
we need in the mesh is too high.
2


In this paper we propose a combination of the two families of methods in two passes. In a ﬁrst
pass, we separate the ﬁrst 4 eigenvalues from the rest of the spectrum (using the method of [37]).
At that point the enclosures that we ﬁnd are big and not admissible. In a second pass we ﬁnd
a very good approximation of 4 eigenvalues and eigenvectors below the threshold (which have to
be necessarily close to λ1, λ2, λ3, λ4). Combining now the stability methods from Barnett–Hassell
[4] with the a priori knowledge of the lower bound of λ5 this yields very small enclosures of the
ﬁrst 4 eigenvalues and their respective positions in the spectrum. This new method combines the
diﬀerent strengths of the two families and their characters: the global problem (ﬁnding the order)
versus the local problem (the reﬁnement of its value).
In order to ﬁnd a very accurate representation of the eigenvalue and eigenvector we will use the
Method of Particular Solutions (MPS). This method was introduced by Fox, Henrici and Moler [15]
and has been later adapted by many authors (see [2, 50, 18, 14, 7] as a sample, and the thorough
review [8]).
The main idea is to consider a set of functions that solve the eigenvalue problem
without boundary conditions as a basis, and writing the solution of the problem with boundary
conditions as a linear combination of them, solving for the coeﬃcients that minimize the error on
the boundary. Typically, the choices have been products of Bessel functions and trigonometric
polynomials centered at certain points. The diﬀerent choices for these points have a big impact
in the performance of the method. Very recently, Gopal and Trefethen [20, 21] have developed
a new way of selecting the base functions in such a way to yield root exponential convergence
(the lightning Laplace solver). We use their algorithm (though our own implementation in C++)
to obtain accurate, fast approximations of the eigenpairs. We stress that these methods produce
accurate approximations but there is no explicit control of the error with respect to the true solution.
In order to overcome this issue and make all the bounds (such as the defect) rigorous we will use
interval arithmetics to bound errors whenever needed.
By working this way, the method outlined above produces a rigorous enclosure of the eigenvalues
corresponding to a particular triangle, but using only this information it is impossible to show that
two given triangles share the same eigenvalues since we only obtain (narrow) bounds and we are
looking at a closed condition. Instead, due to the stability of the problem, we can transform the
closed condition into an open condition using a topological argument and check it by computing
multiple bounds along the sides of a parallelogram in the moduli space of triangles, at the price
of an increased computational cost. To mitigate this cost, we reduce the amount of points to be
computed using stability estimates (with explicit constants) for the eigenvalues of a small open ball
of triangles around a given one. We remark that perturbation methods will not work directly since
the two triangles TA and TB are far from the triangles for which the spectrum is explicitly known.
In the recent years, the application of calculations done by computers to mathematical proofs
has become more popular due to the increment of computational resources, but in order to make
sure that their results are rigorous, we need to control the errors that ﬂoating point arithmetic
can accumulate. This is usually done by means of interval arithmetic, in which the data that a
computer stores for a real number is an interval (two endpoints, or a midpoint and a radius) of real
numbers, stored by two high-precision ﬂoating point numbers, instead of just one.
Operations between intervals are implemented to return intervals which are guaranteed to contain
every possible result when the operands belong to the input intervals. For example, if [x] = [x, x]
and [y] = [y, y] are two intervals, their sum will can be given by the interval [x]+[y] = [x+y, x+y]
and their product by [x] · [y] = [min{xy, xy, xy, xy}, max{xy, xy, xy, xy}]. The same rule applies to
function implementations: a function f evaluated on [x] should return an interval containing every
f(x) for x ∈[x]. We refer to the book [54] for an introduction to validated numerics, in which most
of the techniques used here are explained, and to the survey [19] and the recent book [42] for a
more speciﬁc treatment of computer-assisted proofs in PDE.
3


The paper is organized as follows. In Section 2 we explain how to get tight, rigorous enclosures
of the eigenvalues corresponding to a single triangle. Section 3 is devoted to the extension of the
previous method to a continuous set of triangles, and to the proof of Theorem 1.1. Finally, in
Section 4 we give some implementation details.
2. Enclosing the spectrum of one triangle
In this section we explain how we obtain rigorous bounds for the eigenvalue quotients ξ21 =
λ2
λ1 , ξ41 = λ4
λ1 for a particular triangle, using the two passes explained above. This will be the main
ingredient for the next section, in which we will explain how these bounds can be propagated to a
segment in the moduli space of triangles.
2.1. First pass: separating the ﬁrst 4 eigenvalues. We will focus on the lower bound of λ5
needed to validate ξ41, as the discussion for ξ21 is analogous. In order to ﬁnd a rigorous lower bound
for the ﬁfth eigenvalue of a triangle we will use a recent result found by Liu [37], which is similar
to the one presented in [9] but simpliﬁes the hypotheses and improves the constant involved. Both
use the non-conforming Finite Element Method of Crouzeix–Raviart, which has the advantage over
other conforming ﬁnite elements (such as [38]) that the mass matrix is diagonal.
The Crouzeix–Raviart ﬁnite-element method uses a triangulation of the domain Ω, which in our
case we will take to be the trivial triangulation given by N 2 triangles with sides equal to 1/N of
the original one. The basis functions are indexed by interior edges of the triangulation: if E is a
common edge of triangles τ, τ ′, the basis function ψE is the unique function supported on τ ∪τ ′
such that restricted to each triangle is aﬃne, takes the value 1 in the midpoint of E and the value
0 in the midpoints of the other edges of τ and τ ′.
The weak formulation of the problem (1) reads:
Z
Ω
∇u · ∇ψ = λ
Z
Ω
uψ.
Deﬁning the coeﬃcients of the stiﬀness and mass matrices A = (aEF ), B = (bEF ) by the bilinear
forms
aEF =
Z
Ω
∇ψE · ∇ψF
bEF =
Z
Ω
ψEψF
we are left to solve the discrete system
Ax = λBx,
(2)
where the vector x = (xi) corresponds to the discrete solution ud = P xiψi. For our choice of
triangulation, B is simply a multiple of the identity 2|Ω|I/
 3N 2
(see [9, Remark 3.9]), whereas
A is a sparse matrix whose entries involve in a straightforward way the geometry of the triangle.
This allows us to invert B in the system (2), so we have to solve the following matrix eigenvalue
problem
Mx = λx,
M = 3N 2A/(2|Ω|),
(3)
instead of the previous generalized one. The main result that we will use is the following [37,
Theorem 2.1 and Remark 2.2] linking solutions of the ﬁnite element problem (3) with solutions of
the continuous one (1):
Theorem 2.1. Consider a polygonal domain Ωwith a triangulation so that each triangle has
diameter at most h. Let λk be the k-th solution of the eigenvalue problem (1) in Ωand λk,h the
k-th eigenvalue of the Crouzeix–Raviart discretized problem (3) in Ω. Then
λh,k
1 + C2
hλh,k
≤λk,
(4)
4


where Ch ≤0.1893h is a constant.
In order to be able to deal with approximate eigenvalues we will need in addition the following a
posteriori bound found in a lemma from [47, Theorem 15.9.1], which given an approximate solution
quantiﬁes an upper bound on how far there has to be a true solution nearby.
Lemma 2.2. Let (˜λh, ˜uh) be an approximate eigenpair solving (3) approximately such that ˜λh is
closer to some λh (which solves exactly (3)) than to any other solution of (3). Suppose that the
coeﬃcient vector ˜uh is normalised, ∥˜uh∥= 1. Then the (algebraic) residual r := M ˜uh −˜λh˜uh
satisﬁes
|λh −˜λh| ≤∥r∥.
Remark 2.3. We can combine Theorem 2.1 with Lemma 2.2 thanks to the monotonicity of (4),
using λh,k −∥r∥as a lower bound of λh,k instead.
It is easy to obtain estimations ˜λh with a very small residual using standard eigenvalue routines.
The hardest part here before applying the theorem is to check that they have indeed the correct
index, i.e., that they are closer to the appropriate λh than to any other discrete eigenvalue. This is
why we need to control the whole spectrum of the discrete problem. We will do that by ﬁnding an
approximately orthonormal basis which approximately diagonalizes the matrix, and proving that
there is an exactly orthonormal basis nearby (with explicit bounds) of actual eigenvectors. This
will give us useful bounds after application of Gershgorin disks theorem [16]. More precisely we
will use the following:
Lemma 2.4. Let v1, . . . , vm be vectors in Rm and s > 0 such that |⟨vi, vj⟩−δij| ≤s, and suppose that
8ms < 1. Then there exists an orthonormal set of vectors w1, . . . , wm ∈Rm such that ∥vi −wi∥≤
√
3s1.
Proof. Consider the Gram–Schmidt method applied to the vectors v1, . . . , vm: we deﬁne recursively
uk := vk −
k−1
X
i=1
ui
⟨ui, vk⟩
∥ui∥2
and the normalized vectors wk := uk/∥uk∥. Let β = s + 2ms2. We will prove by induction that
∥uk∥2 ≥1 −β and that |⟨vk, uj⟩| ≤β for all j < k. Indeed, for the ﬁrst inequality,
∥uk∥2 = ⟨vk, vk⟩−
k−1
X
i=1
⟨vk, ui⟩2
∥ui∥2
≥1 −s −m β2
1 −β
(5)
and for the second inequality,
|⟨vk, uj⟩| ≤|⟨vk, vj⟩| +
j−1
X
i=1
|⟨vk, ui⟩⟨vj, ui⟩|
∥ui∥2
≤s + m β2
1 −β .
(6)
We will be able to close the iteration as long as
s + mβ2
1 −β ≤β
(note that both (5) and (6) give place to the same condition). Using the deﬁnition of β this reduces
to checking that s(4m + 4m2s + 2 + 4ms) ≤1, which holds true by virtue of the condition on s.
1The constants in this lemma can be optimized, but for the sake of simplicity of the implementation, and since
the errors in this part are very small, we have preferred to use simpler bounds.
5


Then we can bound the diﬀerence
∥vi −wi∥2 = ∥vi∥2 + ∥wi∥2 −2⟨vi, wi⟩= ∥vi∥2 + 1−2⟨vi, ui⟩
∥ui∥
= ∥vi∥2 + 1−2∥ui∥≤2+ s −2
p
1 −β
which is bounded by 3s.
□
We will use Lemma 2.4 in our proof in the following way: we will ﬁrst ﬁnd an approximate
orthonormal basis of eigenvectors {vi}, let ˜Q be the matrix that has them as columns, and compute
an enclosure for the almost-diagonal matrix ˜D = ˜QT M ˜Q. Let Q be the matrix whose column
vectors are given by the lemma, and construct D = QT MQ, which now has the same eigenvalues
as M due to the orthogonality of Q. We can obtain rigorous enclosures of the entries of D using ˜D
in this way:
|Dij −˜Dij| = |⟨wi, Mwj⟩−⟨vi, Mvj⟩|
≤|⟨wj −vj, Mvi⟩+ ⟨wj −vj, M(wi −vi)⟩+ ⟨wi −vi, Mvj⟩|
≤
√
3s (∥Mvi∥+ ∥Mvj∥) + 4s∥M∥2,
where s is as in the lemma and we have used the symmetry of M. Observe that the bounds for
∥Mvi∥can be computed explicitly, and that the upper bound ∥M∥2 ≤∥M∥Frob is easily computed.
Finally, applying Gershgorin’s generalized disks theorem to the matrix D, of which we have sharp
bounds, we can separate the spectrum of M in at least two components, one of which will contain
the ﬁrst 5 eigenvalues, and the other of which will contain the rest. This will allow us to rigorously
identify the index of the λh,5, for which Lemma 2.2 provides a very sharp bound, by identifying
5 disjoint enclosures of eigenvalues in the ﬁrst component.
Once we have this, application of
Theorem 2.1 and of Remark 2.3 will provide a lower bound for λ5.
2.2. Second pass:
getting narrow enclosures. Our approach to ﬁnd tight bounds for the
eigenvalues of triangles uses the Method of Particular Solutions (MPS), introduced by Fox, Henrici
and Moler in [15] and more recently revived by Betcke and Trefethen [8].
In this method, a
function u is written as a linear combination of functions φi (1 ≤i ≤N) that satisfy the equation
(∆+ λ)φi = 0 on the full plane for a ﬁxed λ. It is very important to remark that there are no
boundary conditions on φi and the linear combination u is chosen in such a way to ensure the
boundary conditions of (1). In other words, the coeﬃcients are chosen to optimize the proximity
of the function to the eigenspace of the actual eigenvalue λj. In order to achieve this, one tries to
ﬁnd a λ and a non-zero function for which the boundary conditions are close to zero. This amounts
to ﬁnd a nontrivial solution (c, λ) of
A(λ)c = 0,
with ci being the coeﬃcient vector such that u(x) = PN
i=1 ciφi(x) and A a rectangular matrix
encoding the boundary conditions evaluated at certain points of the boundary ∂Ω.
Thus, the
eigenvalues λ will be the values for which the smallest singular value of A is zero. In practice, λ are
found by using a golden ratio search on the smallest singular value of A. This provides a candidate
λ ∈R and coeﬃcients ci for which u can be computed with arbitrary precision.
The basis of functions φi that we will use was introduced very recently by Gopal and Tre-
fethen [20, 21] and oﬀers root-exponential convergence. These functions are of two classes: the
ﬁrst are centered around points (that we will call charges) that accumulate exponentially near the
vertices of the triangle along the outside of the angle bisector. More precisely, the j-th of them is lo-
cated at a distance ℓe−σj/√nc of the vertex, where the parameters we have used are ℓ= 1.0, σ = 2.5.
Here nc is the number of charges and 0 ≤j < nc; we have used nc = 7. Using polar coordinates
around the charges, the three functions centered around every charge take the form
φext(r, θ) = Y0

r
√
λ

,
φc
ext(r, θ) = Y1

r
√
λ

cos θ,
φs
ext(r, θ) = Y1

r
√
λ

sin θ.
6


The functions of the second class are all centered around the same point, which we have chosen
to be the centroid of the triangle. Using polar coordinates around it, they take the form
φ0(r, θ) = J0

r
√
λ

,
φc
j(r, θ) = Jj

r
√
λ

cos jθ,
φs
j(r, θ) = Jj

r
√
λ

sin jθ.
for 1 ≤j ≤d; we have used d = 10. Here Jj and Yj are the Bessel functions of the ﬁrst and second
kind, respectively. Note that the ﬁrst class of functions are singular at the charge point, which
allows us to develop the correct behavior at the vertex of the triangle, where the eigenfunction is
singular. The second class of functions allows us to ﬁt the boundary values near the vertices.
This method produces very accurate eigenvalues and eigenfunctions but with no guaranteed
bounds.
In order to obtain these, we will make use of the method developed by Barnett and
Hassell [4], that bounds the error if we can control the L2 norm of the candidate eigenfunction
on the border. In addition to an improvement in the constant by a factor of
√
λ, which makes
it optimal in the high eigenvalue limit, the L2 control is a lot more eﬃcient in practice than the
L∞bounds originally developed in [15, 41], because the approximate eigenfunctions generated with
typical MPS bases tend to be very irregular around the vertices but regular and small in most of
the boundary. Their method is however optimized for high-index eigenvalues, so we adapt some of
the steps to our case of small eigenvalues, simplifying the bookkeeping of the explicit constants.
We summarize the main results that we will use. Let Ωbe a triangle and u a nonzero smooth
function on Ωsuch that (∆+ λ)u = 0. We will measure how good u is as an approximation to an
eigenfunction using the tension
t[u] := ∥u∥L2(∂Ω)
∥u∥L2(Ω)
.
(7)
Let λj, uj be the sequence of eigenvalues and eigenfunctions of Ω, satisfying (∆+ λj)uj = 0 with
zero Dirichlet boundary conditions. Let vj be the normal derivative of uj, deﬁned on the regular
part of ∂Ω. We deﬁne the operator
A(λ) =
X
λj
vj⟨vj, ·⟩
(λ −λj)2 ,
and decompose it as a sum of three:
Anear(λ) =
X
|λ−λj|≤
√
λ
vj⟨vj, ·⟩
(λ −λj)2 ,
Afar(λ) =
X
λ/2≤λj≤2λ,|λ−λj|>
√
λ
vj⟨vj, ·⟩
(λ −λj)2 ,
Atail(λ) =
X
λj<λ/2 or λj>2λ
vj⟨vj, ·⟩
(λ −λj)2
where ⟨·, ·⟩is the standard inner product on L2(∂Ω).
This operator is useful because its norm is controlled from below by the tension (see [4, Section
3]):
t[u]−2 ≤∥A(λ)∥.
(8)
Moreover we have the following bounds from [4, Lemma 4.1] and [4, Lemma 4.2]:
∥Afar(λ)∥≤C1,
(9)
∥Atail(λ)∥≤C2λ−1/2,
(10)
7


that hold for all λ > 12, with explicit constants C1, C2 given below. For the near term, since we
are working with very low eigenvalues,
√
λ is actually small enough that only the summand with
λj = λ appears:
∥Anear(λ)∥=
∥vj∥2
L2(∂Ω)
(λ −λj)2 .
(11)
For convex domains, like in our case, Section 6 of [4] oﬀers explicit bounds for the constants.
In particular, they are based on another constant CΩcoming from a boundary quasi-orthogonality
inequality (see [4, Lemma 2.1]) that we will not discuss in more detail. We will simply use the
bounds C1 ≤2π2CΩ/3 < 7CΩand C2 < 7CΩquoted from the end of page 1058 of the paper.
CΩcan be taken as any constant that makes Lemma 2.1 in [4] hold; in particular, in view of the
proof of the lemma and since λ > 1, one can take CΩ= 4(Ca + C′
a) +
√
2C′′
a, where these three
newly introduced constants depend on a vector ﬁeld on Ωwith certain properties. Luckily, for
strictly star-shaped domains, one can make a trivial choice of such a vector ﬁeld and obtain simple
expressions for the constants. The concrete expressions can be quoted from the ﬁrst bullet point
of [4, Section 6]:
Ca = sup∂Ω(x · n)
inf∂Ω(x · n) ,
C′
a =
1
inf∂Ω(x · n),
C′′
a = 0,
where n is the outer normal vector ﬁeld in the regular part of the boundary. Since the problem is
coordinate-invariant, we are free to chose an origin, and the optimal choice is the incenter of the
triangle. In this case, both the supremum and the inﬁmum are equal to the inradius ρ, so we can
take CΩ= 4(1 + ρ)/ρ.
Putting (8)-(11) together we have
t[u]−2 ≤
∥vj∥2
L2(∂Ω)
(λ −λj)2 + 7CΩ(1 + λ−1/2).
(12)
Finally, recall Rellich’s formula [51]:
Z
∂Ω
(∂nuj)2(x · n)ds = 2λj.
For our choice of origin of coordinates, this just gives us ∥vj∥2
L2(∂Ω) = 2λj/ρ. Inserting this into (12)
and rearranging we have proved:
Proposition 2.5. The distance d from λ to the spectrum of the Laplacian on Ω, can be bounded
above by
d ≤
s
2 ˜λj
ρt[u]−2 −28(1 + ρ)(1 + λ−1/2)
where ˜λj is an upper bound for λj3.
3. Proof of Theorem 1.1 and reduction to a finite number of triangles
In this section we will give speciﬁc details of the triangles TA and TB that we construct in
Theorem 1.1. We ﬁrst notice that because of the scaling of the problem, one can ﬁx two vertices
at (0, 0) and (1, 0) and require the quotients ξ21 = λ2/λ1 and ξ41 = λ4/λ1 to be equal. We will
parametrize the search space by means of the coordinates (cx, cy) of the third vertex of the triangle.
Let A = (0.63500, 0.27500) and B = (0.84906, 0.31995) and consider the parallelograms in this
space with the following sets of vertices:
2This condition obviously holds for our triangles, for example by the Faber–Krahn inequality.
3Obtaining this upper bound is a minor problem: one can use ﬁrst a trivial one, like the one obtained in the ﬁrst
pass, to obtain a ﬁrst enclosure and then use it to bootstrap and get a better one.
8


0.56 0.58 0.6 0.62 0.64 0.66 0.68 0.7 0.72 0.74 0.76 0.78 0.8 0.82 0.84 0.86 0.88 0.9 0.92 0.94
0.25
0.26
0.27
0.28
0.29
0.3
0.31
0.32
0.33
0.34
0.35
A
B
ξ21
ξ41
Figure 1. (Numerical) plot of the level sets of the quotients ξ21 (discontinuous lines) and
ξ41 (continuous lines) around the region of interest. The points A and B are shown in red
and the validated parallelograms in green.
• A + v21,A + v41,A, A + v21,A −v41,A, A −v21,A −v41,A, A −v21,A + v41,A;
• B + v21,B + v41,B, B + v21,B −v41,B, B −v21,B −v41,B, B −v21,B + v41,B;
where the explicit values of the vectors are
• v21,A = (0.004610608896618232, 0.0012403688839389946)
• v41,A = (−0.0041659682109460045, −0.000511581170421992)
• v21,B = (0.0028159587453638808, 0.0020776257941965285)
• v41,B = (0.007180726583099708, 0.00213029677112299)
These are drawn in Figure 1 together with a numerical contour plot of the eigenvalue quotients.
The vectors have been chosen with the heuristic that moving along them keeps one of ξ21, ξ41
approximately constant, while incrementing the other by a ﬁxed amount.
In particular, their
lengths have been adjusted to optimize the total time of the calculations, as shortening one pair of
sides of the parallelogram reduces the total time to validate them, but it also reduces the margin
ξ −¯ξ in the validation of the other pair of sides, thereby increasing their validation time.
We can reduce Theorem 1.1 to a computation on the boundary of the parallelograms by the
following proposition:
Proposition 3.1. Let the parallelograms be deﬁned as before and consider ξ21 −¯ξ21 and ξ41 −¯ξ41,
with ¯ξ21 := 1.67675 and ¯ξ41 := 2.99372. If the following condition is satisﬁed:
each of ξ21 −¯ξ21 and ξ41 −¯ξ41 has a constant and opposite sign in opposite edges
of the parallelograms
(C)
then there exist two triangles TA and TB such that
9


ξ21(TA) = ξ21(TB) = ¯ξ21 and ξ41(TA) = ξ41(TB) = ¯ξ41.
The proof follows from the continuity of eigenvalues and the Poincar´e–Miranda theorem [40],
which we recall here for completeness:
Theorem 3.2. Given two continuous functions f, g : [−1, 1]2 →R such that f(x, y) has the same
sign as x when x = ±1 and g(x, y) has the same sign as y when y = ±1, there exists a point
(x, y) ∈[−1, 1]2 such that f(x, y) = g(x, y) = 0.
Note that the slightly more general result of Remark 1.2 follows from the fact that with the
computer we will check only a ﬁnite number of strict inequalities, so they will remain true if the
values of ¯ξ21 and ¯ξ41 are perturbed by a small amount.
Our goal now is to check the aforementioned sign condition on the sides of the parallelograms.
Instead of working directly with the full side, we will show that it is enough to check condition (C)
on a ﬁnite set of triangles through stability estimates. These will follow from the monotonicity of the
eigenvalues with respect to the inclusion of domains and the scaling properties of the eigenvalues.
Lemma 3.3. Let T and T ′ be two triangles, whose vertices are A = (0, 0), B = (1, 0), and
C = (cx, cy), C′ = (c′
x, c′
y) respectively (cy, c′
y > 0). Consider the cross products p = −→
AC × −−→
AC′ =
cxc′
y −cyc′
x and q = −−→
BC × −−→
BC′ = (cx −1)c′
y −cy(c′
x −1). Then:
• If both p, q < 0, there is a homothety of T ′ by a factor 1 −p/c′
y that contains T.
• If both p, q > 0, there is a homothety of T ′ by a factor 1 + q/c′
y that contains T.
Proof. The proof is very similar in the two cases, so we will only do it for the ﬁrst one. We want
to ﬁnd the homothety of scale 1 + r that keeps the vertex B of triangle T ′ ﬁxed and such that
the image of its opposite side contains vertex C of T (see Figure 2 for a picture of the homothetic
triangles ABC and A′′′BC′′′, and ABC′ and A′′BC′′ respectively). The condition becomes simpler
once we apply an inverse homothety to T and T ′, so that it results in the points
A, C′′′ = C + rB
1 + r , C′
being aligned. The solution is r = −p/c′
y, which is positive by our condition. Moreover, triangle T
lies below this homothety of T ′ because the vectors −−→
BC and −−→
BC′ are in the correct orientation due
to the condition q < 0. This suﬃces to check that T is contained in this homothety.
□
Lemma 3.4. With the same notation as in Lemma 3.3,
• If p > 0 and q < 0, then T ⊂T ′.
• If p < 0 and q > 0, there is a homothety of T ′ by a factor cy/c′
y > 1 that contains T.
Proof. In the ﬁrst case, the conditions on the signs of the cross products of the side vectors is
equivalent to T being contained in T ′. In the second case, the relative orientations of the sides
guarantee that a homothetic triangle to T ′ of the same height as T whose top vertex coincides with
C will contain T, and the ratio of this homothety is clearly cy/c′
y.
□
Using two reversed inclusions from the previous lemmas we can prove:
Lemma 3.5. Let T be a triangle as above, and consider perturbations of the third vertex of the form
C + tv deﬁning triangles T (t), for t ∈[−ℓ, ℓ], where v = (vx, vy). Let λn, λ(t)
n
be the n-th Dirichlet
eigenvalues of triangles T, T (t), respectively, and deﬁne ξ(t)
n1 as the obvious eigenvalue quotient. Then
we distinguish two cases depending on pv = −→
AC × v and qv = −−→
BC × v:
10


A
B
C
C'
A''
A'''
C''
C'''
Figure 2. Two pairs of homothetic triangles: ABC and A′′′BC′′′, and ABC′ and A′′BC′′.
• If pv and qv both have the same sign, then for all t ∈[−ℓ, ℓ]
|ξ(t)
n1 −ξn1| ≤ξn1
"
1 + ℓ
|pv|
cy −ℓ|vy|
2 
1 + ℓ
|qv|
cy −ℓ|vy|
2
−1
#
.
• If pv and qv have diﬀerent signs, then for all t ∈[−ℓ, ℓ]
|ξ(t)
n1 −ξn1| ≤ξn1
"
cy
cy −ℓ|vy|
2
−1
#
.
Proof. For the ﬁrst part, note that either of the conditions of Lemma 3.3 holds for T and T (t)
whenever t ̸= 0: indeed, p = −→
AC × (−→
AC + tv) = tpv and q = −−→
BC × (−−→
BC + tv) = tqv have the
same sign if pv and qv do. Note also that reversing the roles of T and T (t) causes both p and q
to change sign and hence the Lemma still applies, but with the other condition. Combining this
with eigenvalue monotonicity (Ω⊆Ω′ ⇒λn(Ω) ≥λn(Ω′)) and scaling (λn(ρΩ) = ρ−2λn(Ω)) yields
either
λn ≥

1 +
|tpv|
cy + tvy
−2
λ(t)
n ≥

1 + ℓ
|pv|
cy −ℓ|vy|
−2
λ(t)
n ,
λ(t)
n ≥

1 + |tqv|
cy
−2
λn >

1 + ℓ
|qv|
cy −ℓ|vy|
−2
λn
or
λn ≥

1 +
|tqv|
cy + tvy
−2
λ(t)
n ≥

1 + ℓ
|qv|
cy −ℓ|vy|
−2
λ(t)
n ,
λ(t)
n ≥

1 + |tpv|
cy
−2
λn >

1 + ℓ
|pv|
cy −ℓ|vy|
−2
λn
independently of n. In either case the conclusion is that

1 + ℓ
|pv|
cy −ℓ|vy|
−2 
1 + ℓ
|qv|
cy −ℓ|vy|
−2
≤λ(t)
n /λn
λ(t)
1 /λ1
= ξ(t)
n1
ξn1
≤

1 + ℓ
|pv|
cy −ℓ|vy|
2 
1 + ℓ
|qv|
cy −ℓ|vy|
2
11


and from here the ﬁrst claim readily follows. For the second one the argument is similar: either
cy −ℓ|vy|
cy
−2
λ(t)
n ≥
cy + ℓ|vy|
cy
2
λ(t)
n ≥
c′
y
cy
2
λ(t)
n ≥λn ≥λ(t)
n ,
or
cy −ℓ|vy|
cy
2
λ(t)
n ≤
c′
y
cy
2
λ(t)
n ≤λn ≤λ(t)
n ,
independently of n too. Similarly, in either case the conclusion is that
cy −ℓ|vy|
cy
2
≤λ(t)
n /λn
λ(t)
1 /λ1
= ξ(t)
n1
ξn1
≤
cy −ℓ|vy|
cy
−2
and the claim follows.
□
In the last section we discuss how to pick the triangles for which we check Condition (C), and
how the two passes of Section 2 are implemented, thus concluding the proof.
4. Details of the implementation
The computer-assisted part of the proof is done with three main programs that take care
of independent parts of the validation.
All the rigorous computations are performed using the
validated arithmetics library Arb, developed by Fredrik Johansson [30], which can be found at
http://arblib.org. The three programs are:
(a) The program implemented in valxi_main.cc takes as input data specifying a side of one
of the two quadrilaterals, a total number N of subdivisions of the side, and an integer
1 ≤c ≤N indexing the subdivision to validate. Then it computes narrow enclosures for
two eigenvalues (which program (c) will check a posteriori that correspond to λ1 and λk, for
k = 2 or 4), of the triangle parametrized by the center of the segment. Finally it outputs
them together with an enclosure for ξk1 which is valid for the whole subdivided segment.
(b) interm_main.cc reads data specifying one of the sides in which we are validating ξ41, and
uses the same machinery as (a) to ﬁnd enclosures for two eigenvalues (which program (c)
will later conﬁrm to be λ2 and λ3) of the triangle corresponding to the center of the side.
Then it outputs bounds propagated to the whole side (it turns out that here with N = 1
segment we get suﬃciently small errors).
(c) Finally, position_main.cc is responsible for the ﬁrst pass described above: separating the
ﬁrst k = 2 or 4 eigenvalues from the rest of the spectrum and checking that the eigenvalues
obtained in (a) do have the claimed indices. This is done by ﬁrst ﬁnding a rigorous lower
bound for λk+1 at the center of the side using the FEM technique, and propagating it to
the whole side. In the case k = 2, it is enough to check that the eigenvalues found by (a)
on each subdivided interval lie in disjoint enclosures in (0, λ3). In the case k = 4, we need
to check that the two eigenvalues given by (a) and the two intermediate eigenvalues given
by (b) give pairwise disjoint enclosures in (0, λ5) for each subdivided interval.
In our implementation, for part (a) we have divided each side into N = 40 smaller segments.
For (b) and (c) we have not needed any subdivision. Therefore the bulk of the time is taken by the
ﬁrst program: one run takes approximately 8 minutes, so the total running time is of approximately
42 hours. This can be of course run in parallel, in our case reducing the time to less than one hour
with 80 machines.
In programs (a) and (b), eigenvalues are searched around the approximate numeric eigenvalues
of a FEM discretization of the problem, and then they are reﬁned and rigorously validated using
the techniques explained in the second pass section.
These approximate eigenvalues are found
using the numeric linear algebra library ALGLIB. The reﬁned search for the eigenvalues is done by
12


minimizing the least singular value of a matrix involving boundary values of the basis functions,
as described in [8]; we have chosen 300 boundary points per side, distributed as Chebyshev nodes,
and 40 interior points randomly chosen with a ﬁxed seed. The singular value is computed using
the ALGLIB library again, and the minimum is found by a golden ratio search.
For parts (a) and (b), in order to apply Proposition 2.5 we need an upper bound on the tension
deﬁned in (7), which amounts to ﬁnding an upper bound for the L2 norm of u on ∂Ωand a lower
bound on its interior L2 norm. We now discuss the details of both:
• Upper bound of ∥u∥L2(∂Ω):
For the upper bound on the boundary norm, the sides of the triangle are divided into small
segments, starting with a Chebyshev node distribution and subdividing into two smaller
segments whenever the supremum of u2 in the interval is larger than a ﬁxed threshold. For
each of these segments σ, linearly parametrized by p : [−1, 1] →σ ⊂∂Ω, the integral of
v(t) := u2(p(t)) is evaluated by using a quadrature for the corresponding Taylor expansion,
and adding a computed upper bound of the error term. Note that to control both the
coeﬃcients of the expansion and the error term, the derivatives of v need to be evaluated
both in the midpoint of the segment and in the whole segment using interval arithmetic.
More precisely, if v(t) = Pm
j=0 vjtj + r(t), where vj = v(j)(0)
j!
are the Taylor coeﬃcients
and the residue term r(t) can be bounded by R = supt∈[−1,1]
v(m+1)(t)
(m+1)!
, then we can use
the bound
Z
σ
u2 ≤|σ|


⌊m/2⌋
X
i=0
v2i
2i + 1 +
R
m + 2


assuming m is odd.
• Lower bound of ∥u∥L2(Ω):
For the interior norm lower bound, we will only bound from below the integral of u2 in
an interior region of Ω, because the contributions to the L2 norm near the boundary are
small due to the Dirichlet condition. We will do this by partitioning this interior region
into a triangular grid and using a form of the minimum principle to deduce a lower bound
of u2 in each triangle τ of the grid from a lower bound of u2 on ∂τ. More precisely, suppose
|u| ≥b on ∂τ, and assume without loss of generality that u > 0 on ∂τ. If u < 0 anywhere
inside τ, the region U on which u is negative has λ as its ﬁrst Dirichlet eigenvalue, so by
the Faber–Krahn inequality, |U| is bounded below. However, U ⊂τ implies |U| ≤|τ|, so
for a small enough partition this will be a contradiction. Therefore −∆u = λu > 0 on τ,
and by the minimum principle, u ≥sup∂τ u ≥b on τ.
If u changes sign on the boundary, the lower bound of |u| that we will get will be 0, so
we will be ignoring that triangle. It turns out that this strategy is enough to get a fraction
of ∥u∥2 as a lower bound.
In our case we have used a grid of 82 triangles that partitions an interior triangle of
side length 0.8 times the original one (see Figure 3). On the perimeter of the grid, lower
bounds of u2 are obtained by subdividing the segments into halves until u2 is computed
on each segment with a precision smaller than a given threshold. Evaluation of u2 on a
segment σ is done by means of the Taylor expansion again, controlling both the derivatives
of v(t) = u2(p(t)) evaluated at t = 0 and at the whole interval t ∈[−1, 1] by means of
interval arithmetic.
Due to the oscillatory behavior of the solutions, especially near the vertices, and the large amount
of cancellation between the summands, a high order Taylor expansion (order m = 25) has been
used to evaluate u2. Since the derivatives of the Bessel functions, which take most of the time of
13


the computation, can be computed recursively at each point, it is more eﬃcient to use a high order
expansion and fewer intervals to speed up the validation.
(a)
(b)
Figure 3. Grid used to validate a lower bound for ∥u∥L2(Ω) for triangle TB, with (a) the
ﬁrst eigenfunction and (b) the second eigenfunction plotted on top.
For part (c), the approximate orthonormal basis {vi} described at the end of section 2.1 is con-
structed using the eigendecomposition method for symmetric matrices from the numerical library
ALGLIB. The rest of the calculations were easily performed using Arb.
Acknowledgements
We are grateful to Princeton University, where this research was performed, and to the VSRC
Program and the Department of Mathematics for partially supporting the second author’s stay. JGS
was partially supported by NSF through Grant NSF DMS-1763356. GO was partially supported
by the CFIS Mobility Grant, by the MOBINT-MIF Scholarship from AGAUR, and by the Severo
Ochoa grant program from ICMAT. We also thank Princeton University for computing facilities
(Polar cluster).
References
[1] P. R. S. Antunes and P. Freitas. On the inverse spectral problem for Euclidean triangles. Proc. R. Soc. Lond.
Ser. A Math. Phys. Eng. Sci., 467(2130):1546–1562, 2011.
[2] P. R. S. Antunes and S. S. Valtchev. A meshfree numerical method for acoustic wave propagation problems in
planar domains with corners and cracks. J. Comput. Appl. Math., 234(9):2646–2662, 2010.
[3] M. S. Ashbaugh and R. D. Benguria. A sharp bound for the ratio of the ﬁrst two eigenvalues of Dirichlet
Laplacians and extensions. Annals of Mathematics, 135(3):601–628, 1992.
[4] A. H. Barnett and A. Hassell. Boundary quasi-orthogonality and sharp inclusion bounds for large Dirichlet
eigenvalues. SIAM J. Numer. Anal., 49(3):1046–1063, 2011.
[5] C. Beattie and F. Goerisch. Methods for computing lower bounds to eigenvalues of self-adjoint operators. Numer.
Math., 72(2):143–172, 1995.
[6] H. Behnke and F. Goerisch. Inclusions for eigenvalues of selfadjoint problems. In Topics in validated computations
(Oldenburg, 1993), volume 5 of Stud. Comput. Math., pages 277–322. North-Holland, Amsterdam, 1994.
[7] T. Betcke. The generalized singular value decomposition and the method of particular solutions. SIAM J. Sci.
Comput., 30(3):1278–1295, 2008.
[8] T. Betcke and L. N. Trefethen. Reviving the method of particular solutions. SIAM Rev., 47(3):469–491, 2005.
14


[9] C. Carstensen and J. Gedicke. Guaranteed lower bounds for eigenvalues. Math. Comp., 83(290):2605–2629, 2014.
[10] P.-K. Chang and D. DeTurck. On hearing the shape of a triangle. Proc. Amer. Math. Soc., 105(4):1033–1038,
1989.
[11] C. B. Croke and V. A. Sharafutdinov. Spectral rigidity of a compact negatively curved manifold. Topology,
37(6):1265–1273, 1998.
[12] C. Durso. On the inverse spectral problem for polygonal domains. ProQuest LLC, Ann Arbor, MI, 1988. Thesis
(Ph.D.)–Massachusetts Institute of Technology.
[13] A.
Enciso
and
J.
G´omez-Serrano.
Spectral
determination
of
semi-regular
polygons.
Arxiv
preprint
arXiv:1709.05960, 2017.
[14] G. Fairweather and A. Karageorghis. The method of fundamental solutions for elliptic boundary value problems.
volume 9, pages 69–95. 1998. Numerical treatment of boundary integral equations.
[15] L. Fox, P. Henrici, and C. Moler. Approximations and bounds for eigenvalues of elliptic operators. SIAM J.
Numer. Anal., 4:89–102, 1967.
[16] S. A. Gershgorin. ¨Uber die Abgrenzung der Eigenwerte einer Matrix. Bulletin de l’Acad´emie des Sciences de
l’URSS. Classe des sciences math´ematiques et naturelles, (6):749–754, 1931.
[17] F. Goerisch. Ein Stufenverfahren zur Berechnung von Eigenwertschranken. In Numerical treatment of eigenvalue
problems, Vol. 4 (Oberwolfach, 1986), volume 83 of Internat. Schriftenreihe Numer. Math., pages 104–114.
Birkh¨auser, Basel, 1987.
[18] M. A. Golberg and C. S. Chen. The method of fundamental solutions for potential, Helmholtz and diﬀusion
problems. In Boundary integral methods: numerical and mathematical aspects, volume 1 of Comput. Eng., pages
103–176. WIT Press/Comput. Mech. Publ., Boston, MA, 1999.
[19] J. G´omez-Serrano. Computer-assisted proofs in PDE: a survey. SeMA J., 76(3):459–484, 2019.
[20] A. Gopal and L. N. Trefethen. New Laplace and Helmholtz solvers. Proc. Natl. Acad. Sci. USA, 116(21):10223–
10225, 2019.
[21] A. Gopal and L. N. Trefethen. Solving Laplace Problems with Corner Singularities via Rational Functions. SIAM
J. Numer. Anal., 57(5):2074–2094, 2019.
[22] C. Gordon, D. Webb, and S. Wolpert. Isospectral plane domains and surfaces via Riemannian orbifolds. Invent.
Math., 110(1):1–22, 1992.
[23] D. Grieser and S. Maronna. Hearing the shape of a triangle. Notices Amer. Math. Soc., 60(11):1440–1447, 2013.
[24] V. Guillemin and D. Kazhdan. Some inverse spectral results for negatively curved 2-manifolds. Topology,
19(3):301–312, 1980.
[25] A. Henrot. Extremum problems for eigenvalues of elliptic operators. Frontiers in Mathematics. Birkh¨auser Verlag,
Basel, 2006.
[26] H. Hezari, Z. Lu, and J. Rowlett. The Neumann isospectral problem for trapezoids. Ann. Henri Poincar´e,
18(12):3759–3792, 2017.
[27] H. Hezari and S. Zelditch. Inverse spectral problem for analytic (Z/2Z)n-symmetric domains in Rn. Geom. Funct.
Anal., 20(1):160–191, 2010.
[28] H. Hezari and S. Zelditch. One can hear the shape of ellipses of small eccentricity. Arxiv preprint
arXiv:1907.03882, 2019.
[29] L. Hillairet and C. Judge. Spectral simplicity and asymptotic separation of variables. Communications in Math-
ematical Physics, 302(2):291–344, 2011.
[30] F. Johansson. Arb: eﬃcient arbitrary-precision midpoint-radius interval arithmetic. IEEE Transactions on Com-
puters, 66:1281–1292, 2017.
[31] C. Judge and S. Mondal. Euclidean triangles have no hot spots. Annals of Mathematics, 191(1):167–211, 2020.
[32] M. Kac. Can one hear the shape of a drum? Amer. Math. Monthly, 73(4, part II):1–23, 1966.
[33] T. Kato. On the upper and lower bounds of eigenvalues. J. Phys. Soc. Japan, 4:334–339, 1949.
[34] R. S. Laugesen and B. A. Siudeja. Maximizing Neumann fundamental tones of triangles. J. Math. Phys.,
50(11):112903, 18, 2009.
[35] R. S. Laugesen and B. A. Siudeja. Triangles and other special domains. In Shape optimization and spectral theory,
pages 149–200. De Gruyter Open, Warsaw, 2017.
[36] N. J. Lehmann. Optimale Eigenwerteinschliessungen. Numer. Math., 5:246–272, 1963.
[37] X. Liu. A framework of veriﬁed eigenvalue bounds for self-adjoint diﬀerential operators. Appl. Math. Comput.,
267:341–355, 2015.
[38] X. Liu and S. Oishi. Veriﬁed eigenvalue evaluation for the Laplacian over polygonal domains of arbitrary shape.
SIAM J. Numer. Anal., 51(3):1634–1654, 2013.
[39] Z. Lu and J. Rowlett. The sound of symmetry. Amer. Math. Monthly, 122(9):815–835, 2015.
[40] C. Miranda. Un’osservazione su un teorema di Brouwer. Boll. Un. Mat. Ital. (2), 3:5–7, 1940.
15


[41] C. B. Moler and L. E. Payne. Bounds for eigenvalues and eigenvectors of symmetric operators. SIAM J. Numer.
Anal., 5:64–70, 1968.
[42] M. T. Nakao, M. Plum, and Y. Watanabe. Numerical Veriﬁcation Methods and Computer-Assisted Proofs for
Partial Diﬀerential Equations. Springer, 2020.
[43] B. Osgood, R. Phillips, and P. Sarnak. Compact isospectral sets of plane domains. Proc. Nat. Acad. Sci. U.S.A.,
85(15):5359–5361, 1988.
[44] B. Osgood, R. Phillips, and P. Sarnak. Compact isospectral sets of surfaces. J. Funct. Anal., 80(1):212–234,
1988.
[45] B. Osgood, R. Phillips, and P. Sarnak. Moduli space, heights and isospectral sets of plane domains. Ann. of
Math. (2), 129(2):293–362, 1989.
[46] T. Ourmi`eres-Bonafos. Dirichlet eigenvalues of asymptotically ﬂat triangles. Asymptotic Analysis, 92(3-4):279–
312, 2015.
[47] B. N. Parlett. The symmetric eigenvalue problem, volume 20 of Classics in Applied Mathematics. Society for
Industrial and Applied Mathematics (SIAM), Philadelphia, PA, 1998. Corrected reprint of the 1980 original.
[48] G. P. Paternain, M. Salo, and G. Uhlmann. Spectral rigidity and invariant distributions on Anosov surfaces. J.
Diﬀerential Geom., 98(1):147–181, 2014.
[49] M. Plum. Eigenvalue inclusions for second-order ordinary diﬀerential operators by a numerical homotopy method.
Z. Angew. Math. Phys., 41(2):205–226, 1990.
[50] W. W. Read, G. E. Sneddon, and L. Bode. A series method for the eigenvalues of the advection diﬀusion equation.
ANZIAM J., 45((C)):C773–C786, 2003/04.
[51] F. Rellich. Darstellung der Eigenwerte von ∆u + λu = 0 durch ein Randintegral. Math. Z., 46:635–636, 1940.
[52] G. Still. Computable bounds for eigenvalues and eigenfunctions of elliptic diﬀerential operators. Numer. Math.,
54(2):201–223, 1988.
[53] Z. I. Szab´o. Isospectral pairs of metrics on balls, spheres, and other manifolds with diﬀerent local geometries.
Ann. of Math. (2), 154(2):437–475, 2001.
[54] W. Tucker. Validated numerics. Princeton University Press, Princeton, NJ, 2011. A short introduction to rigorous
computations.
[55] K. Watanabe. Plane domains which are spectrally determined. II. J. Inequal. Appl., 7(1):25–47, 2002.
[56] A. Weinstein and W. Stenger. Methods of intermediate problems for eigenvalues. Academic Press, New York-
London, 1972. Theory and ramiﬁcations, Mathematics in Science and Engineering, Vol. 89.
[57] S. Zelditch. Inverse spectral problem for analytic domains. II. Z2-symmetric domains. Ann. of Math. (2),
170(1):205–269, 2009.
(Corresponding author) Department of Mathematics, Princeton University, Princeton, NJ 08544, USA
E-mail address: jg27@math.princeton.edu
Cambridge University
E-mail address: go262@cam.ac.uk
16


