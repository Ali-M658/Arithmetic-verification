---
title: Isospectrality For Orbifold Lens Spaces (full text, arXiv:1705.01412v2)
id: isospectrality-for-orbifold-lens-spaces-full-text-arxiv170501412v2
tags:
- hyperbolic-pillow-heat-novelty-813161
- orbifold-lens-spaces
- spherical-space-forms
- heat-trace-non-determinacy
- competing-priority-claim
created: '2026-08-09T08:43:20.024189Z'
updated: '2026-08-09T09:36:32.202839Z'
source: https://arxiv.org/pdf/1705.01412
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Full text (extracted locally via pymupdf after CLI PDF fetch returned JUNK_CONTENT)
  of Bari-Hunsicker arXiv:1705.01412v2. Proves Thm 3.1 (3-dim orbifold lens spaces:
  isospectral implies isometric), Thm 4.3 (same for 4-dim), Thm 5.6 (cyclic vs non-cyclic
  spherical space forms cannot be isospectral) -- entirely in the constant POSITIVE
  curvature (spherical space form S^{2n-1}/G) setting, not hyperbolic. Separately,
  Lemma 6.5/6.7 + Examples 6.6/6.8 prove the FULL heat-trace asymptotic expansion
  (all coefficients b_k for every k, not a finite counted subset) coincides for the
  non-isometric pair L(195:3,5) vs L(195:6,35) whenever the reduced parameters alpha,beta
  match -- a negative (non-sufficiency) result with no finite count N and no minimality
  claim, not a finite-coefficient determinacy threshold.'
---

arXiv:1705.01412v2  [math.DG]  12 Sep 2017
ISOSPECTRALITY FOR ORBIFOLD LENS SPACES
NAVEED S. BARI AND EUGENIE HUNSICKER
ABSTRACT. We answer Mark Kac’s famous question [K], “can one hear the
shape of a drum?” in the positive for orbifolds that are 3-dimensional and 4-
dimensional lens spaces; we thus complete the answer to this question for orb-
ifold lens spaces in all dimensions. We also show that the coefﬁcients of the
asymptotic expansion of the trace of the heat kernel are not sufﬁcient to deter-
mine the above results.
CONTENTS
1.
Introduction
1
2.
Orbifold Lens Spaces
3
2.1.
Orbifold Lens Spaces and their Generating Functions
3
3.
3-Dimensional Orbifold Lens Spaces
7
4.
4-Dimensional Orbifold Lens Spaces
17
5.
Lens Spaces and Other Spherical Space Forms
19
6.
Heat Kernel For Orbifold Lens Spaces
22
6.1.
Heat Trace Results for Orbifolds
23
6.2.
Heat Kernel For 3-Dimensional Lens Spaces
26
6.3.
Heat Kernel For 4-Dimensional Lens Spaces
33
References
37
1. INTRODUCTION
Given a closed Riemannian manifold (M, g), the eigenvalue spectrum of the as-
sociated Laplace Beltrami operator will be referred to as the spectrum of (M, g).
The inverse spectral problem asks the extent to which the spectrum encodes the
geometry of (M, g). While various geometric invariants such as dimension, vol-
ume and total scalar curvature are spectrally determined, numerous examples of
isospectral Riemannian manifolds, i.e., manifolds with the same spectrum, show
that the spectrum does not fully encode the geometry. Not surprisingly, the earliest
examples of isospectral manifolds were manifolds of constant curvature including
ﬂat tori ([M]), hyperbolic manifolds ([V]), and spherical space forms ([I1], [I2] and
[Gi]). In particular, lens spaces are quotients of round spheres by cyclic groups of
orthogonal transformations that act freely on the sphere. Lens spaces have provided
Keywords: Spectral geometry Global Riemannian geometry Orbifolds Lens Spaces.
2000 Mathematics Subject Classiﬁcation: Primary 58J53; Secondary 53C20.
1
a rich source of isospectral manifolds with interesting properties. In addition to the
work of Ikeda and Yamamoto cited above, see the results of Gornet and McGowan
[GoM].
In this paper we generalize this theme to the category of Riemannian orbifolds.
A smooth orbifold is a topological space that is locally modelled on an orbit space
of Rn under the action of a ﬁnite group of diffeomorphisms. Riemannian orbifolds
are spaces that are locally modelled on quotients of Riemannian manifolds by ﬁnite
groups of isometries. Orbifolds have wide applicability, for example, in the study
of 3-manifolds and in string theory [DHVW], [ALR].
The tools of spectral geometry can be transferred to the setting of Riemannian
orbifolds by using their well-behaved local structure (see [Chi], [S1] [S2]). As in
the manifold setting, the spectrum of the Laplace operator of a compact Riemann-
ian orbifold is a sequence 0 ≤λ1 ≤λ2 ≤λ3 ≤. . . ↑∞where each eigenvalue is
repeated according to its ﬁnite multiplicity. We say that two orbifolds are isospec-
tral if their Laplace spectra agree.
The literature on inverse spectral problems on orbifolds is less developed than
that for manifolds. Examples of isospectral orbifolds include pairs with boundary
([BCDS] and [BW]); isospectral ﬂat 2-orbifolds ([DR]); arbitrarily large ﬁnite fam-
ilies of isospectral orbifolds ([SSW]); isospectral orbifolds with different maximal
isotropy orders ([RSW]); and isospectral deformation of metrics on an orbifold
quotient of a nilmanifold ([PS]).
In the study of inverse isospectral problem, spherical space forms provide a rich
and important set of orbifolds with interesting results. For the 2-dimensional case,
it is known [DGGW] that the spectrum determines the spherical orbifolds of con-
stant curvature R > 0. In [L], Lauret found examples in dimensions 5 through 8 of
orbifold lens spaces (spherical orbifold spaces with cyclic fundamental groups) that
are isospectral but not isometric. For dimension 9 and higher, the author proved the
existence of isospectral orbifold lens spaces that are non-isometric [Ba]. The prob-
lem was unsolved for 3 and 4-dimensional orbifold lens spaces. For 3-dimensional
manifold lens spaces Ikeda and Yamamoto (see [I1], [IY] and [Y])proved that the
spectrum determines the lens space. In [I2], Ikeda further proved that for general
3-dimensional manifold spherical space forms, the spectrum determines the space
form. In the manifold case, it is also known that even dimensional spherical space
forms are only the canonical sphere and the real projective space. For orbifold
spherical space forms this is not the case. In this article we will prove the follow-
ing results:
Theorem 3.1 Two three-dimensional isospectral orbifold lens spaces are isometric.
Theorem 4.3 Two four-dimensional isospectral orbifold lens spaces are isometric.
Theorem 5.6 Let S2n−1/G and S2n−1/G′ be two (orbifold) spherical space forms.
Suppose G is cyclic and G′ is not cyclic. Then S2n−1/G and S2n−1/G′ cannot be
isospectral.
The above results will complete the classiﬁcation of the inverse spectral problem
on orbifold lens spaces in all dimensions.
2
In addition to the above theorems, we also prove that the coefﬁcients of the trace
of the heat kernel are not sufﬁcient to prove the above results, i.e., we can have two
non-isospectral orbifold lens spaces with identical coefﬁcients of the trace of heat
kernel.
2. ORBIFOLD LENS SPACES
In this section we will generalize the idea of manifold lens spaces to orbifold lens
spaces. Note that lens spaces are special cases of spherical space forms, which are
connected complete Riemannian manifolds of positive constant curvature 1. An
n-dimensional spherical space form can be written as Sn/G where G is a ﬁnite
subgroup of the orthogonal group O(n + 1). In fact, the deﬁnition of spherical
space forms can be generalized to allow G to have ﬁxed points making Sn/G an
orbifold. Manifold lens spaces are spherical space forms where the n-dimensional
sphere Sn of constant curvature 1 is acted upon by a cyclic group of ﬁxed point
free isometries on Sn. We will generalize this notion to orbifolds by allowing the
cyclic group of isometries to have ﬁxed points. For details of spectral geometry
on orbifolds, see Stanhope [S1] and E. Dryden, C. Gordon, S. Greenwald and D.
Webb in [DGGW]).
2.1. Orbifold Lens Spaces and their Generating Functions. We now reproduce
the background work developed by Ikeda in [I1] and [I2] for manifold spherical
space forms. We will note that with slight modiﬁcations the results are valid for
orbifold spherical space forms. This is the background work we will need to de-
velop our results for orbifold lens spaces.
We will ﬁrst consider general 2n−1 dimensional lens spaces. Let q be a positive
integer. Set
q0 =
(q−1
2
if q is odd,
q
2
if q is even.
Throughout this section we assume that q0 ≥4.
For n ≤q0, let p1, . . . , pn be n integers. Note, if g.c.d.(p1, . . . , pn, q) ̸= 1, we
can divide all the p′
is and q by this gcd to get a case where the gcd = 1. So, without
loss of generality, we can assume g.c.d.(p1, . . . , pn, q) = 1. We denote by g the
orthogonal matrix given by
g =




R(p1/q)
0
...
0
R(pn/q)



,
where
(2.1)
R(θ) =

cos 2πθ
sin 2πθ
−sin 2πθ
cos 2πθ

.
Then g generates a cyclic subgroup G =

gl	q
l=1 of order q of the special orthog-
onal group SO(2n) since det g = 1. Note that g has eigenvalues γp1, γ−p1,γp2,
3
γ−p2,..., γpn, γ−pn, where γ is a primitive q-th root of unity. We deﬁne the lens
space L(q : p1, . . . , pn) as follows:
L(q : p1, . . . , pn) = S2n−1/G.
Note that if gcd(pi, q) = 1 ∀i, L(q : p1, . . . , pn) is a smooth manifold; Ikeda and
Yamamoto have answered Kac’s question in the afﬁrmative for 3-dimensional man-
ifold lens spaces ([IY], [Y]). To get an orbifold in this setting with non-trivial sin-
gularities, we must have gcd(pi, q) > 1 for some i. In such a case L(q : p1, . . . , pn)
is a good smooth orbifold with S2n−1 as its covering manifold. Let π be the cov-
ering projection of S2n−1 onto S2n−1/G
π : S2n−1 →S2n−1/G.
Since the round metric of constant curvature one on S2n−1 is G-invariant, it induces
a Riemannian metric on S2n−1/G. Henceforth, the term ”lens space” will refer to
this generalized deﬁnition. Ikeda proved the following result for manifold spherical
space forms. We note that the proof doesn’t require the groups to be ﬁxed-point
free, and reproduce the result for orbifold spherical space forms:
Lemma 2.1. Let Sn/G and Sn/G′ be spherical space forms for any integer n ≥2.
Then Sn/G is isometric to Sn/G′ if and only if G is conjugate to G′ in O(n + 1).
Note that if we have a lens space S2n−1/G = L(q : p1, . . . , pn), with G =<
g >, permuting the pi’s doesn’t change the underlying group G; similarly, if we
multiply all the pi’s by some number ±l where gcd(l, q) = 1, that simply means
we have mapped the generator g to the generator gl, and so we still have the same
group G. Also note that if two lens spaces S2n−1/G = L(q : p1, . . . , pn) and
S2n−1/G′ = L(q : s1, . . . , sn) are isometric, then by the above lemma G and G′
must be conjugate. So, the lift of the isometry on S2n−1 maps a generator, g of G
to a generator g′l of G′. This means that the eigenvalues of g and g′l are the same,
which means that each pi is equivalent to some lsj or −lsj (mod q). These facts
give us the following corollary for Lemma 2.1
Corollary 2.2. Let L = L(q : p1, . . . , pn) and L′ = L(q : s1, . . . , sn) be lens
spaces. Then L is isometric to L′ if and only if there is a number l coprime with
q and there are numbers ei ∈{−1, 1} such that (p1, . . . , pn) is a permutation of
(e1ls1, . . . , enlsn) (mod q).
Assume we have a spherical space form Sm/G for any integer m ≥2. For any
f ∈C∞(Sm/G), we deﬁne the Lapacian on the spherical space form as e∆(π∗f) =
π∗(∆f). We now construct the spectral generating function associated with the
Laplacian on S2n−1/G analogous to the construction in the manifold case (see
[I1], [I2] and [IY]). Let ˜∆, ∆and ∆0 denote the Laplacians of S2n−1, S2n−1/G
and R2n, respectively.
4
Deﬁnition 2.3. For any non-negative real number λ, we deﬁne the eigenspaces eEλ
and Eλ as follows:
eEλ =

f ∈C∞(S2n−1)
e∆f = λf
	
,
Eλ =

f ∈C∞(S2n−1/G)
∆f = λf
	
.
The following lemma follows from the deﬁnitions of ∆and smooth function.
Lemma 2.4. Let G be a ﬁnite subgroup of O(n + 1).
(i) For any f ∈C∞(S2n−1/G), we have e∆(π∗f) = π∗(∆f).
(ii) For any G-invariant function F on S2n−1, there exists a unique function
f ∈C∞(Sn/G) such that F = π∗f.
Corollary 2.5. Let
  eEλ

G be the space of all G-invariant functions of eEλ. Then
dim(Eλ) = dim( eE)G.
Let ∆0 be the Laplacian on R2n with respect to the ﬂat K¨ahler metric. Set
r2 = P2n
i=1 x2
i , where (x1, x2, . . . , x2n) is the standard coordinate system on R2n.
For k ≥0, let P k denote the space of complex valued homogeneous polynomi-
als of degree k on R2n. Let Hk be the subspace of P k consisting of harmonic
polynomials on R2n,
Hk =

f ∈P k∆0f = 0
	
.
Each orthogonal transformation of R2n canonically induces a linear isomorphism
of P k.
Proposition 2.6. The space Hk is O(2n)-invariant, and P k has the direct sum
decomposition: P k = Hk ⊕r2P k−2.
The injection map i : S2n−1 →R2n induces a linear map i∗: C∞(R2n) →
C∞(S2n−1). We denote i∗(Hk) by Hk.
Proposition 2.7. Hk is an eigenspace of e∆on S2n−1 with eigenvalue k(k + 2n −
2) and P∞
k=0 Hk is dense in C∞(S2n−1) in the uniform convergence topology.
Moreover, Hk is isomorphic to Hk. That is, i∗: Hk
≃
−→Hk.
For proofs of these propositions, see [BGM].
Now Corollary 2.5 and Proposition 2.7 imply that if we denote by Hk
G be the
space of all G-invariant functions in Hk, then
dim Ek(k+2n−2) = dim Hk
G.
Moreover, for any integer k such that dim Hk
G ̸= 0, ¯λk = k(k + 2n −2) is an
eigenvalue of ∆on S2n−1/G with multiplicity equal to dim Hk
G, and no other
eigenvalues appear in the spectrum of ∆.
Deﬁnition 2.8. Let O be a closed compact Riemannian orbifold with the Laplace
spectrum, 0 ≤¯λ1 < ¯λ2 < ¯λ3 . . . ↑∞. For each ¯λk, let the eigenspace be
E¯λk =

f ∈C∞(O)
∆f = ¯λkf
	
.
5
We deﬁne the spectrum generating function associated to the spectrum of the Lapla-
cian on O as
FO(z) =
∞
X
k=0
 dim E¯λk

zk.
In terms of spherical space forms, the deﬁnition becomes
Deﬁnition 2.9. The generating function FG(z) associated to the spectrum of the
Laplacian on Sn/G is the generating function associated to the inﬁnite sequence

dim Hk
G
	∞
k=0 , i.e.,
FG(z) =
∞
X
k=0
 dim Hk
G

zk.
By Corollary 2.5, Proposition 2.7 and subsequent discussion, we know that the
generating function determines the spectrum of Sn/G. This fact gives us the fol-
lowing proposition:
Proposition 2.10. Let Sn/G and Sn/G′ be two spherical space forms. Let FG(z)
and FG′(z) be their respective spectrum generating functions.
Then Sn/G is
isospectral to Sn/G′ if and only if FG(z) = FG′(z).
Our ﬁrst goal is to ﬁnd an alternative expression for FG(z) that will allow us to
compare FG(z) and FG′(z).
If G is a ﬁnite subgroup of O(2n) with orientation preserving action on S2n−1
then G is a subgroup of SO(2n). In the following we will consider orientation-
preserving group actions.
The following theorem, proved for manifold spherical space forms in [I1] and
[I2], holds true for the orbifold spherical space forms as well.
Theorem 2.11. Let G be a ﬁnite subgroup of SO(2n), and let S2n−1/G be a
spherical space form with spectrum generating function FG(z). Then, on the do-
main

z ∈C
|z| < 1
	
, FG(z) converges to the function
FG(z) =
1
|G|
X
g∈G
1 −z2
det(I2n −gz).
where |G| denotes the order of G and I2n is the 2n × 2n identity matrix.
We denote the generating function for a lens space L = L(q : p1, . . . , pn) by
Fq(z : p1, ..., pn).
Corollary 2.12. Let L(q : p1, . . . , pn) be a lens space and Fq(z : p1, . . . , pn) the
generating function associated to the spectrum of L(q : p1, . . . , pn). Then, on the
domain

z ∈C
|z| < 1
	
,
Fq(z : p1, . . . , pn) = 1
q
q
X
l=1
1 −z2
Qn
i=1(z −γpil)(z −γ−pil),
where γ is a primitive q-th root of unity.
6
Proof. In the notation of the Theorem 2.11, we get
dim Hk
G =
1
|G|
X
g∈G
χk(g) = 1
q
q
X
l=1
χk(gl).
(2.2)
So
Fq(z : p1, . . . , pn) = (1 −z2)
|G|
X
g∈G
1
Qn
i=1(1 −γpiz)(1 −γ−piz)
= (1 −z2)
q
q
X
l=1
1
Qn
i=1(z −γpil)(z −γ−pil),
since multiplying through by 1 = (−γ−pil)(−γpil) gives
(1 −γpilz)(1 −γ−pilz) = (z −γ−pil)(z −γpil).
□
Remark: By the Theorem 2.11 and unique analytic continuation, we can con-
sider the generating function to be a meromorphic function on the whole complex
plane C with poles on the unit circle S1 = {z ∈C | |z| = 1}.
From this remark we have,
Corollary 2.13. Let S2n−1/G and S2n−1/G′ be two spherical space forms. If
there is a one to one mapping φ of G onto G′ such that the set E(g) = the set
E(φ(g)), ∀g ∈G, then S2n−1/G is isospectral to S2n−1/G′.
Proof. The proof follows from the fact that
Y
γ∈E(g)
(1 −γz) =
Y
γ∈E(g)
(z −γ) = det(I2n −gz).
□
Corollary 2.14. Let S2n−1/G and S2n−1/G′ be two isospectral spherical space
forms. Then |G| = |G′|.
3. 3-DIMENSIONAL ORBIFOLD LENS SPACES
For 3-dimensional manifold lens spaces, it is known that if two lens spaces are
isospectral then they are also isometric ([IY] and [Y]). We will generalize this
result to the orbifold case.
Using the notation adopted in the previous section, we write the two isospectral
lens spaces as L1 = L(q : p1, p2) and L2 = L(q : s1, s2). Now there are only ﬁve
possibilities:
Case 1 Both L1 and L2 are manifolds. In this case gcd(pi, q) = 1 = gcd(si, q)
for i = 1, 2.
Case 2 One of the two lens spaces, say L1 is a manifold, while the other, L2 is
an orbifold with non-trivial isotropy groups. This means that gcd(p1, q) =
gcd(p2, q) = 1, while at least one of s1 or s2 is not coprime to q.
Case 3 Both L1 and L2 are orbifolds with non-trivial isotropy groups so that exa-
cly one of p1 or p2 is coprime to q and exactly one of s1 or s2 is coprime
to q.
7
Case 4 Both L1 and L2 are orbifolds with non-trivial isotropy groups, but in one
case, say for L1, exactly one of p1 or p2 is coprime to q, while for the other
lens space, L2 neither s1 nor s2 is coprime to q.
Case 5 None of p1, p2, s1 and s2 is coprime to q.
With these ﬁve cases in mind, we will prove our main theorem:
Theorem 3.1. Given two 3-dimensional lens spaces L1 = L(q : p1, p2) and L2 =
L(q : s1, s2). If L1 is isospectral to L2, then the two lens spaces are isometric.
Proof. We will consider each case separately:
Case 1
In this case L1 and L2 are both manifolds. Ikeda and Yamamoto proved this
case (see [IY] and [Y]).
Case 2
We know that whenever two isospectral good orbifolds share a common Rie-
mannian cover, their respective singular sets are either both trivial or both non-
trivial [GR]. Therefore, for orbifold lens spaces we can’t have a situation where
two lens spaces are isospectral, but one has a trivial singular set while the other has
a non-trivial singular set. So this case is not possible.
Case 3
By multiplying the entries of L1 and L2 by appropriate numbers coprime to q
we can rewrite L1 = L(q : 1, x) and L2 = L(q : 1, y), where x and y are not
coprime to q. Let F1(z) [resp. F2(z)] be the generating function associated to the
spectrum of L1 [resp.L2]. Let γ be a primitive q-th root of unity.
Now,
lim
z→γ(z −γ)F1(z)
= lim
z→γ
1
q
q
X
l=1
(z −γ)(1 −z2)
(1 −γlz)(1 −γ−lz)(1 −γxlz)(1 −γ−xlz)
= lim
z→γ
−γ
q
q
X
l=1
(1 −γ−1z)(1 −z2)
(1 −γlz)(1 −γ−lz)(1 −γxlz)(1 −γ−xlz)
(3.1)
Each term of the sum vanishes unless (1 −γ−1z) cancels one of the four terms in
the denominator. This occurs if one of the following congruences has a solution:
(1) l + 1 ≡0(mod q),
(2) −l + 1 ≡0(mod q),
(3) xl + 1 ≡0(mod q),
(4) −xl + 1 ≡0(mod q).
Congruences (3) and (4) have no solution as x is not coprime to q. The solution to
(1) is l = q −1, and the solution to (2) is l = 1. Substituting in (3.1), we get
lim
z→γ(z −γ)F1(z) =
−2γ
q(1 −γ−x+1)(1 −γx+1).
By the same argument, we get
8
lim
z→γ(z −γ)F2(z) =
−2γ
q(1 −γ−y+1)(1 −γy+1).
Since
lim
z→γ(z −γ)F1(z) = lim
z→γ(z −γ)F2(z),
we get
−2γ
q(1 −γ−x+1)(1 −γx+1) =
−2γ
q(1 −γ−y+1)(1 −γy+1),
=⇒
1
[1 −(γ−x+1 + γx+1) + γ2] =
1
[1 −(γ−y+1 + γy+1) + γ2],
=⇒(γ−x+1 + γx+1) = (γ−y+1 + γy+1).
Since γ ̸= 0, we get
(γ−x + γx) = (γ−y + γy),
=⇒( 1
γx + γx) = ( 1
γy + γy),
=⇒(1 + γ2x
γx
) = (1 + γ2y
γy
),
=⇒(γy + γ2x+y) = (γx + γx+2y),
=⇒(γy −γx+2y) = (γx −γ2x+y),
=⇒γy(1 −γx+y) = γx(1 −γx+y),
=⇒(γy −γx)(1 −γx+y) = 0,
=⇒(γy −γx) = 0 or (1 −γx+y) = 0,
=⇒x ≡y(mod q) or x ≡−y(mod q).
Thus, by Corollary 2.2 we get that L1 and L2 are isometric.
Case 4
By the same argument as in Case 3, we get
lim
z→γ(z −γ)F1(z) =
−2γ
q(1 −γ−x+1)(1 −γx+1).
However,
lim
z→γ(z −γ)F2(z) = 0
because the congruences (1) - (4) in Case 3 become
(1’) s1l + 1 ≡0(mod q),
(2’) −s1l + 1 ≡0(mod q),
(3’) s2l + 1 ≡0(mod q),
(4’) −s2l + 1 ≡0(mod q),
9
and these congruences have no solutions because s1 and s2 are not coprime to q.
Thus, in this case L1 cannot be isospectral to L2.
Case 5
This is the hardest of all the cases. First, we can simplify the forms of the two
lens spaces as follows:
Let gcd(p1, q) = x > 1, gcd(p2, q) = y > 1, gcd(s1, q) = u > 1, and
gcd(s2, q) = v > 1. Also without loss of generality we can assume that y > x and
v > u because if x = y (resp. u = v) then |G| = q/x (resp. |G| = q/u), which
contradicts our assumption that |G| = q.
We rewrite L1 = L(q : ax, by) and L2 = L(q : cu, dv). Since gcd(ax, q) =
gcd(x, q) = x and gcd(cu, q) = gcd(u, q) = u, we can multiply the entries of
L1 and L2 by appropriate numbers coprime to q and rewrite L1 = L(q : x, py)
and L2 = L(q : u, sv) (see [GP]). We will also assume that gcd(x, py) = 1 =
gcd(u, sv) because if say gcd(x, py) = e > 0, then we could divide x, py and q
by e and get a lens space with fundamental group of order q/e instead of q, which
is a contradiction.
In this case we again want to consider a limit of the spectral generating functions
for L1 and L2.
Proposition 3.2. Suppose L = L(q : x, py) is an orbifold lens space with spectrum
generating function Fq(z). Then lim
z→γx(z −γx)Fq(z) ̸= 0, where γ = e2πi/q is a
primitive q-th root of unity.
Proof. We denote q/x = q
x and q/y = q
y. Then
lim
z→γx(z −γx)Fq(z) = lim
z→γx
1
q
q
X
l=1
(z −γx)(1 −z2)
(1 −γxlz)(1 −γ−xlz)(1 −γpylz)(1 −γ−pylz)
= lim
z→γx
−γx
q
q
X
l=1
(1 −γ−xz)(1 −z2)
(1 −γxlz)(1 −γ−xlz)(1 −γpylz)(1 −γ−pylz)
(3.2)
As before, the terms in the above sum are non-zero iff one of the following
congruences has a solution:
(1”) xl + x ≡0(mod q),
(2”) −xl + x ≡0(mod q),
(3”) pyl + x ≡0(mod q),
(4”) −pyl + x ≡0(mod q),
(3”) implies that pyl + x ≡0(mod y), so, if (3”) has a solution, it would violate
the fact that gcd(x, y) = 1. Therefore, (3”) has no solution. Similarly (4”) has no
solution.
The solution to (1”) is l = tq/x −1 and the solution to (2”) is l = tq/x + 1 for
t ∈{1, ..., x}. Note that for l = tq/x ± 1,
lim
z→γx
(1 −γ−xz)(1 −z2)
(1 −γxlz)(1 −γ−xlz) = 1
10
We can, therefore, write (3.2) as
lim
z→γx(z −γx)Fq(z) = −2γx
q
x
X
t=1
1
(1 −γpy(tq/x−1)+x)(1 −γ−py(tq/x−1)+x)
Writing αt = py(tq/x −1), we get
lim
z→γx(z −γx)Fq(z) = −2γx
q
x
X
t=1
1
(1 −γ(αt+x))(1 −γ−(αt−x)
= −2γx
q
x
X
t=1
1
γ(αt+x)(γ−(αt−x) −γ−(αt+x))
h
1
1 −γ−(αt+x) −
1
1 −γ−(αt−x)
i
=
−2γx
q(γ2x −1)
x
X
t=1
h
1
1 −γ−(αt+x) −
1
1 −γ−(αt−x)
i
=
−2
i2q sin 2πx
q
x
X
t=1
h
1
1 −e−i2π(αt+x)/q −
1
1 −e−i2π(αt−x)/q
i
By writing at = αt + x and bt = αt −x, we can rewrite the above as:
lim
z→γx(z −γx)Fq(z) =
−2
i2q sin 2πx
q
x
X
t=1
h
1
1 −e−i2πat/q −
1
1 −e−i2πbt/q
i
=
1
2q sin 2πx
q
x
X
t=1
h
2i
1 −e−i2πat/q −
2i
1 −e−i2πbt/q
i
Now, using the identity cot θ + i =
2i
1−e−2iθ , we get
(3.3)
lim
z→γx(z −γx)Fq(z) =
1
2q sin 2πx
q
x
X
t=1
h
cot πat
q
−cot πbt
q
i
.
The above limit can only be 0 if
x
X
t=1
h
cot πat
q
−cot πbt
q
i
=
x
X
t=1
h
cot π
q [tpyq/x −(py −x)] −cot π
q [tpyq/x −(py + x)]
i
= 0.
Now (mod q) both at and bt have x values each between 0 and π.
Consider the following two sets of positive integers (mod q):
A = {At : At = at(mod q), t = 1, 2, ..., x}
and
B = {Bt : Bt = bt(mod q), t = 1, 2, ..., x}.
Suppose min{A} = Aj and min{B} = Bk. Now we have the following
possibilities:
11
(i) Aj > Bk. Then it is easy to check that Aj+t > Bk+t for t = 0, 1, ..., x−1,
since aj+t −bk+t = aj −bk. So, we can re-write (3.3) as
(3.4)
lim
z→γx(z −γx)Fq(z) =
1
2q sin 2πx
q
x−1
X
t=0
h
cot π
q Aj+t −cot π
q Bk+t
i
.
We know that if 0 < B < A < π, then cot A −cot B < 0. Since, in
the above equation 0 < Bk+t < Aj+t < π for all t, each pair gives us a
negative value, and therefore (3.4) is negative.
(ii) Aj < Bk. Then using a similar argument as above, we will have (3.4)
positive.
(iii) Aj = Bk. This means aj −bk ≡(j −k)pyq/x + 2x ≡0(mod q). But
this means that y|2x, which is not possible since we are assuming that
gcd(x, y) = 1 and x < y.
This proves the proposition.
□
We will also need the following lemma to prove the theorem for Case 5:
Lemma 3.3. Suppose L1 = L(q : x, py) and L2 = L(q : u, sv) are two isospec-
tral lens orbifolds where gcd(x, q) = x, gcd(py, q) = y, gcd(u, q) = u and
gcd(sv, q) = v. Then either u = x and v = y, or u = y and v = x.
Note: If u = x and v = y, then L1 = L(q : x, py) and L2 = L(q : x, sy);
if u = y and v = x, then L1 = L(q : x, py) and L2 = L(q : y, sx) = L(q :
s−1y, x) = L(q : x, s−1y). In either case, this implies that we can write L1 =
L(q : x, py) and L2 = L(q : x, s′y) where s′ = s or s′ = s−1.
We now prove the lemma:
Proof. We denote q/x = q
x and q/y = q
y. Then
lim
z→γx(z −γx)F1(z) = lim
z→γx
1
q
q
X
l=1
(z −γx)(1 −z2)
(1 −γxlz)(1 −γ−xlz)(1 −γpylz)(1 −γ−pylz)
Recall that the only non-zero terms in this limit will be the ones where xl + x ≡
0(mod q) or −xl + x ≡0(mod q), which gives l = tq/x −1 or l = tq/x + 1 for
t ∈{1, ..., x}. Also note that for such a t, we have
1
(1 −γpy(tq/x−1)+x)(1 −γ−py(tq/x−1)+x)
=
1
(1 −γpy[(x−t)q/x+1]+x)(1 −γ−py[(x−t)q/x+1]+x)
.
These two facts, along with Proposition 3.2 give
0 ̸= −2γx
q
x
X
t=1
1
(1 −γpy(tq/x−1)+x)(1 −γ−py(tq/x−1)+x)
= lim
z→γx(z −γx)F1(z).
Since
lim
z→γx(z −γx)F1(z) = lim
z→γx(z −γx)F2(z),
12
we get
0 ̸= −2γx
q
x
X
t=1
1
(1 −γpy(tq/x−1)+x)(1 −γ−py(tq/x−1)+x)
= lim
z→γx(z −γx)F2(z)
= lim
z→γx
−γx
q
q
X
l=1
(1 −γ−xz)(1 −z2)
(1 −γulz)(1 −γ−ulz)(1 −γsvlz)(1 −γ−svlz).
So there must be an l such that
ul + x ≡0(mod q),
or
−ul + x ≡0(mod q),
or
svl + x ≡0(mod q),
or
−svl + x ≡0(mod q).
Recall that u|q. Then ul + x ≡0(mod q) or −ul + x ≡0(mod q) imply that
u|x. Similarly, since v|q, we can show that if svl + x ≡0(mod q) or −svl + x ≡
0(mod q) then v|x. So either u|x or v|x.
Now by multiplying the elements of L1 by an appropriate number we can rewrite
L1 = L(q : y, p′x). Then applying the same argument as above where we swap
the roles of x and y, we get either u|y or v|y.
Suppose u|x. Then since gcd(x, y) = 1 we can’t have u|y. Similarly, if v|x,
then we can’t have v|y. Therefore, either u|x and v|y, or v|x and u|y since if u or
v divide both, then it contradicts gcs(q, x, py) = 1.
We can swap the roles of L1 and L2 and repeat the above arguments again to get
either x|u and y|v, or y|u and x|v.
If u|x and v|y, and at the same time x|v and y|u, then x|y, which contradicts the
fact that gcd(q, x, y) = 1. So, the only possibilities are:
i. u|x, v|y, x|u and y|v. This means x = u and y = v.
ii. v|x, u|y, x|v and y|u. This means x = v and y = u.
This completes the proof for the lemma.
□
Remark: From now on, we can write the two lens spaces as L1 = L(q : x, py)
and L2 = L(q : x, sy). Further, If q is odd, we can also assume that both s and
p are odd since if one of them, say p, is even then we can replace the lens space
with L(q : x, (q −p)y) which is isometric to L1 and the coefﬁcient q −p is odd.
Also, if q is even, then both x and py (resp.sy) can’t be even simultaneously since
gcd(x, py)(resp. sy); from now on, without loss of generality, if q is even we will
assume that x is even and py (resp. sy) is odd since if py (resp. sy) is even and x is
odd, then we can multiply the entries of the lens spaces by an appropriate number
to re-write it as L1 = L(q : y, p′x) (resp. L2 = L(q : y, s′x)).
We now returning to the proof of Case 5 of our main theorem. Suppose L1 =
L(q : x, py) and L2 = L(q : x, sy) are isospectral lens spaces with spectrum
13
generating functions F1(z) and F2(z) respectively. Using a similar argument as in
Proposition 3.2 above and the fact that F1(z) = F2(z), we will get
x
X
t=1
h
cot π
q [tpyq/x −(py −x)] −cot π
q [tpyq/x −(py + x)]
i
=
x
X
t=1
h
cot π
q [tsyq/x −(sy −x)] −cot π
q [tsyq/x −(sy + x)]
i
.
(3.5)
Since py > x and sy > x (therefore, pyq/x > xq/x = q and syq/x > xq/x = q
respectively), the above equation can be written as
x
X
t=1
h
cot π
q [tq/x −(py −x)] −cot π
q [tq/x −(py + x)]
i
=
x
X
t=1
h
cot π
q [tq/x −(sy −x)] −cot π
q [tq/x −(sy + x)]
i
.
(3.6)
Finally, by writing αy ≡(q −p)y( mod q) and βy ≡(q −s)y( mod q), we can
rewrite the above equality as
x−1
X
t=0
h
cot π
q [tq/x + αy + x] −cot π
q [tq/x + αy −x]
i
=
x
X
t=1
h
cot π
q [tq/x + βy + x] −cot π
q [tq/x + βy −x]
i
,
(3.7)
Suppose tq/x + αy + x > 0 and tq/x + αy −x < 0. But this would mean that
y(tq/xy + α) < x, which can’t be true because we are assuming y > x. Therefore,
for every t, both tq/x+αy+x and tq/x+αy−x are positive(with the only exception
happening when y = q/x, which we will look at a little later). This observation
suggests that the minimum values of tq/x + αy + x and tq/x + αy −x occur for
the same value of t, and in such a case the difference between the minimum values
would be 2x. The same will be the case for the minimum values of tq/x + βy + x
and tq/x + βy −x.
Now consider the following four sets of positive integers (mod q):
A = {At : At ≡[tq/x + αy + x](mod q), t = 0, 1, ..., x −1},
B = {Bt : Bt ≡[tq/x + αy −x](mod q), t = 0, 1, ..., x −1},
C = {Ct : Ct ≡[tq/x + βy −x](mod q), t = 0, 1, ..., x −1},
D = {Dt : Dt ≡[tq/x + βy + x](mod q), t = 0, 1, ..., x −1}.
14
REMARK Note that the minimum values for A and B (resp. C and D) occur at
the same value of t, and consequently, At > Bt (resp.Ct > Dt) for all values of
t ∈{0, 1, ..., x −1}.
Suppose
min{A} = t′q/x + αy + x,
min{B} = t′q/x + αy −x,
min{C} = t′′q/x + βy + x,
and
min{D} = t′′q/x + βy −x.
This means that for each t, At −Bt = 2x = Ct −Dt because
π(t′q/x+αy+x)
q
,
π(t′q/x+αy−x)
q
,
π(t′′q/x+βy+x)
q
, and
π(t′′q/x+βy−x)
q
lie between 0 and π
x(=
πq/x
q ) and
there are a total of x such combinations with each πAt
q
(resp. πBt
q , πCt
q , and πDt
q )
lying between (t−1)π
x
and tπ
x , and is simply a translation of πAt−1
q
(resp. πBt−1
q
,
πCt−1
q
, and πDt−1
q
) by π
x to the right.
Using the above remark, we can re-write Equation (3.7) as
(3.8)
x−1
X
t=0
h
cot π
q At′+t −cot π
q Bt′+t
i
−
h
cot π
q Ct′′+t −cot π
q Dt′′+t
i
= 0
Now if
h
cot π
q At′ −cot π
q Bt′
i
−
h
cot π
q Ct′′ −cot π
q Dt′′
i
< 0( resp. > 0), then
h
cot π
q At′+t −cot π
q Bt′+t
i
−
h
cot π
q Ct′′+t −cot π
q Dt′′+t
i
< 0( resp. > 0) for all
values of t, which means Equation (3.8) will not be satisﬁed. So, we conclude that
for all values of t
h
cot π
q At′+t −cot π
q Bt′+t
i
−
h
cot π
q Ct′′+t −cot π
q Dt′′+t
i
= 0.
This means one of the following two conditions must be true:
(I) cot π
q At′+t = cot π
q Ct′′+t and cot π
q Bt′+t = cot π
q Dt′′+t, or
(II) cot π
q At′+t = −cot π
q Dt′′+t and cot π
q Bt′+t = −cot π
q Ct′′+t
Condition (I) implies that At′+t ≡Ct′′+t( mod q) and Bt′+t ≡Dt′′+t( mod q),
i.e., ∃t1, t2 ∈{0, 1, ..., x −1} with
pyt1q/x −py + x ≡At′(mod q),
pyt1q/x −py −x ≡Bt′(mod q),
syt2q/x −sy + x ≡Ct′′(mod q),
and
syt2q/x −sy −x ≡Dt′′(mod q)
such that
py(t1 + t)q/x −py + x ≡sy(t2 + t)q/x −sy + x( mod q), ∀t ∈{0, 1, ..., x −1}
15
and
py(t1 + t)q/x −py −x ≡sy(t2 + t)q/x −sy −x( mod q), ∀t ∈{0, 1, ..., x −1}
These congruences imply
(3.9) py[(t1 + t)q/x −1] ≡sy[(t2 + t)q/x −1]( mod q), ∀t ∈{0, 1, ..., x −1}
Now, if t = x −t1, then the above congruence becomes
(3.10)
py(q −1) ≡sy(t3q/x −1)( mod q), where t3 = x −t1 + t2.
We know that gcd(q −1, q) = 1. We claim that gcd(t3q/x −1, q) = 1. To see
this, suppose gcd(t3q/x −1, q) = d > 1. But this means
py(q −1) ≡sy(t3q/x −1)( mod d) ≡0( mod d).
Now d does not divide q/x since d|t3q/x −1, which means d|x since d|q. Since
gcd(x, py) = 1, this would imply that (q −1) ≡0( mod d), which is a contradic-
tion. Therefore, gcd(t3q/x −1, q) = 1. Now we see that the corresponding lens
spaces are isometric because
L(q; x, py) ∼L(q; −x, −py) ∼L(q; −x, (t3q/x −1)sy) ∼L(q; x, sy).
Condition (II) implies that At′+t ≡−Dt′′+t( mod q) and Bt′+t ≡−Ct′′+t( mod q),
i.e., ∃t1, t2 ∈{0, 1, ..., x −1} with
pyt1q/x −py + x ≡At′(mod q),
pyt1q/x −py −x ≡Bt′(mod q),
syt2q/x −sy + x ≡Ct′′(mod q),
and
syt2q/x −sy −x ≡Dt′′(mod q)
such that
py(t1 + t)q/x −py + x ≡−sy(t2 + t)q/x + sy + x( mod q), ∀t ∈{0, 1, ..., x −1}
and
py(t1 +t)q/x −py −x ≡−sy(t2 +t)q/x +sy −x( mod q), ∀t ∈{0, 1, ..., x−1}.
These congruences imply
(3.11) py[(t1 +t)q/x −1] ≡−sy[(t2 +t)q/x +1]( mod q), ∀t ∈{0, 1, ..., x−1}
As before if t = x −t1, then the above congruence becomes
(3.12)
py(q −1) ≡−sy(t3q/x + 1)( mod q), where t3 = x −t1 + t2.
With a similar argument as in Condition (I), we get that gcd(t3q/x +1, q) = 1, and,
as before, the corresponding lens spaces are isometric because
L(q; x, py) ∼L(q; −x, −py) ∼L(q; −x, −(t3q/x + 1)sy) ∼L(q; x, sy)
.
Finally, notice that if y = q/x then gcd(x, q/x) = 1 and (3.7) can be written as
16
x
X
t=1
h
cot π
q [tq/x + αq/x + x] −cot π
q [tq/x + αq/x −x]
i
=
x
X
t=1
h
cot π
q [tq/x + βq/x + x] −cot π
q [tq/x + βq/x −x]
i
,
(3.13)
which can be re-written as
x
X
t=0
h
cot π
q [tq/x + x] −cot π
q [tq/x −x]
i
=
x
X
t=1
h
cot π
q [tq/x + x] −cot π
q [tq/x −x]
i
,
(3.14)
In this case, the minimum positive value for tq/x + x is x, which occurs when
t = 0, and the minimum positive value for tq/x −x is q/x −x, which occurs
when t = 1. If q/x > 2x (alt. q/x < 2x), then the minimum value of tq/x −x
(i.e., q/x −x) is greater than (alt. less than) the minimum value of tq/x + x (i.e.,
x). Consequently, At < Bt+1 and Ct < Dt+1 for all t ∈{0, 1, ..., x −1} (alt.
At > Bt+1 and Ct > Dt+1 for all t ∈{0, 1, ..., x −1}). This means that for each
t, Bt+1 −At = q/x −2x = Dt+1 −Ct (alt. At −Bt+1 = 2x −q/x = Ct −Dt+1).
We can now re-write equation (3.14) as
(3.15)
x−1
X
t=0
h
cot π
q At −cot π
q Bt+1
i
−
h
cot π
q Ct −cot π
q Dt+1
i
= 0
Now if
h
cot π
q A0 −cot π
q B1
i
−
h
cot π
q C0 −cot π
q D1
i
< 0( resp. > 0), then
h
cot π
q At −cot π
q Bt+1
i
−
h
cot π
q Ct −cot π
q Dt+1
i
< 0( resp. > 0) for all values
of t, which means equation (3.15) will not be satisﬁed. So we conclude that for all
valuesof t, h
cot π
q At −cot π
q Bt+1
i
−
h
cot π
q Ct −cot π
q Dt+1
i
= 0.
Now the rest of the argument is very similar to the case where y ̸= q/x.
This completes our proof for Case 5.
□
4. 4-DIMENSIONAL ORBIFOLD LENS SPACES
It is known that in the manifold case, even dimensional spherical space forms
are only the sphere and the real projective spaces [I2]. It is also known that the
sphere Sn is not isospectral to the real projective space P n(R) [BGM].
In the orbifold case, there are many even dimensional spherical space forms
with ﬁxed points. We will focus on the 4-dimensional orbifold lens spaces. In [L],
17
Lauret has classiﬁed cyclic subgroups of SO(2n+1) up to conjugation. According
to this classiﬁcation, any cyclic subgroup G of SO(2n+1) is represented by G =<
γ > where γ = diag(R(2πp1
q ), ..., R(2πpn
q
), 1) and R(θ) =

cos θ
sin θ
−sin θ
cos θ

.
In order to prove our theorem for 4-dimensional orbifold lens spaces, we need a
couple of results from [Ba]. We deﬁne
˜gW + =






R(p1/q)
0
...
R(pn/q)
0
IW






and
˜g′
W + =






R(s1/q)
0
...
R(sn/q)
0
IW






where IW is the W × W identity matrix for some integer W. We can deﬁne ˜GW +
= ⟨˜gW +⟩and ˜G′
W + = ⟨˜g′
W +⟩. Then ˜GW + and ˜G′
W + are cyclic groups of order
q. We deﬁne lens spaces ˜LW + = S2n+W −1/ ˜GW + and ˜L′
W + = S2n+W −1/ ˜G′
W +.
Further suppose the corresponding 2n −1-dimensional orbifold lens spaces are
given by L = L(q : p1, p2, ..., pn) and L′ = L(q : s1, s2, ..., sn). Then by Lemma
3.2.2 in [Ba] we get
Lemma 4.1. Let L, L′, ˜LW + and ˜L′
W + be as deﬁned above. Then L is isometric
to L′ iff ˜LW + is isometric to ˜L′
W +.
And by Theorem 3.2.3 in [Ba] we get:
Theorem 4.2. Let F W +
q
(z : p1, . . . , pn, 0) be the generating function associated
to the spectrum of ˜LW +. Then on the domain

z ∈C
|z| < 1
	
,
F W +
q
(z : p1, . . . , pn, 0) =
(1 + z)
(1 −z)W −1 · 1
q
q
X
l=1
1
Qn
i=1(z −γpil)(z −γ−pil)
Now suppose n = 2. Let
˜g1 =



R(p1/q)
0
R(p2/q)
0
1



and
˜g2 =



R(s1/q)
0
R(s2/q)
0
1


.
18
Suppose there are 4-dimensional orbifold lens spaces O1 = S4/ ˜G1 (denoted by
L(q : p1, p2, 0)) and O2 = S4/ ˜G2 (denoted by L(q : s1, s2)), where ˜G1 =< ˜g1 >
and ˜G2 =< ˜g2 >. Further suppose the corresponding 3-dimensional orbifold lens
spaces are given by L1 = L(q : p1, p2) and L2 = L(q : s1, s2).
We now prove the following theorem for 4-dimensional orbifold lens spaces:
Theorem 4.3. Given O1, O2, ˜G1 and ˜G2 as above. If O1 and O2 are isospectral
then they are isometric.
Proof. From Theorem 4.2 we know that on the domain

z ∈C
|z| < 1
	
, the
spectrum generating functions of O1 and O2, respectively, are,
Fq(z : p1, p2, 0) = 1
q
q
X
l=1
(1 + z)
Q2
i=1(z −γpil)(z −γ−pil)
and
Fq(z : s1, s2, 0) = 1
q
q
X
l=1
(1 + z)
Q2
i=1(z −γsil)(z −γ−sil)
.
Notice that Fq(z : p1, p2) = (1 −z)Fq(z : p1, p2, 0) and Fq(z : s1, s2) =
(1 −z)Fq(z : s1, s2, 0), where Fq(z : p1, p2) and Fq(z : s1, s2) are respectively
the spectrum generating functions for the 3-dimensional orbifold lens spaces L1 =
L(q : p1, p2) and L2 = L(q : s1, s2). This means that if O1 and O2 are isospectral
then L1 and L2 are also isospectral.
Now, from Theorem 3.1, we know that L1 and L2 are isometric. By Lemma
4.1 we know that L1 is isometric to L2 iff O1 is isometric to O2. This proves the
theorem.
□
5. LENS SPACES AND OTHER SPHERICAL SPACE FORMS
One question still remains: Is an orbifold lens space ever isospectral to an orb-
ifold spherical space form which has non-cyclic fundamental group?
Our next result proves that an orbifold lens space cannot be isospectral to a
general spherical space form with non-cyclic fundamental group. We will use some
results from [I2] noting that in some cases his assumption that the acting group is
ﬁxed-point free is not used in certain proofs, and therefore, the results hold true for
orbifolds.
Deﬁnition 5.1. Let G be ﬁnite group, and let Gk be the subset of G consisting of all
elements of order k in G. Let σ(G) denote the set consisting of orders of elements
in G. Then we have
G = ∪k∈σ(G)Gk (disjoint union)
The following lemma is proved in [I2] for ﬁxed-point free subgroups of SO(2n),
but we note that the proof doesn’t require this condition and reproduce the proof
from [I2].
19
Lemma 5.2. Let G be a ﬁnite subgroup of SO(2n) (n ≥2). Then the subset
Gk is divided into the disjoint union of subsets C1
k, ..., Cik
k such that each Ct
k(t =
1, 2, ..., ik) consists of all generic elements of some cyclic subgroup of order k in
G.
Proof. For any g ∈Gk, we denote by Ag the cyclic subgroup of G generated by g.
Now, for g, g′ ∈Gk the cyclic group Ag∩Ag′ is of order k if and only if Ag = Ag′.
Now the lemma follows from this observation immediately.
□
We now state another lemma (see [I2] for proof) that will be used to prove our
result.
Lemma 5.3. Let g be an element in SO(2n) (n ≥2) and of order q (q ≥3). Set
γ = e2π√−1/q. Assume g has eigenvalues γ, γ−1, γp1, γ−p1,..., γpk, γ−pk with
multiplicities l, l, i1, i1, ..., ik, ik, respectively, where p1, ..., pk are integers prime
to q with pi ̸≡±pj(modq) (for 1 ≤i < j ≤k), p ̸≡±l(modq) (for i = 1, ..., k)
and l + i1 + ... + ik = n. Then the Laurent expansion of the meromorphic function
1−z2
det (12n−gz) at z = γ is
1
(z −γ)l
(√−1)n+lγl
2n−l(1 −γ2)n−1
k
Y
j=1
{cot π
q (pj+1)−cot π
q (pj−1)}ij+ lower order terms.
The following proposition is proved by Ikeda for a group G that acts freely.
However, we note that the proposition is true even if G does not act freely since
the proof does not use the property that G acts freely.
Proposition 5.4. Let G be a ﬁnite subgroup of SO(2n) (n ≥2), and let k ∈σ(G).
We deﬁne a positive integer k0 by
k0 = 2n −1 if k = 1 or 2,
= maxg∈Gk{max. of multiplicities of eigenvalues of g} if k ≥3.
Then the generating function FG(z) has a pole of order k0 at any primitive k-th
root of 1.
Proof. At z = 1, we notice that for g = I2n ∈G1, we get
lim
z→1(1 −z)2n−1FG(z) =
2
|G|,
as g has eigenvalue 1 with multiplicity 2n. So, FG(z) has a pole of order 2n −1 at
z = 1.
At z = −1 we notice that for g = −I2n ∈G2, we get
lim
z→1(1 + z)2n−1FG(z) =
2
|G|,
as g has eigenvalue -1 with multiplicity 2n. Also, for any other g′ ∈G2, the
eigenvalue -1 has multiplicity at most 2n. So FG(z) has a pole of order 2n −1 at
z = −1 as well.
20
We now assume k ≥3. Now let Gk, C1
k, ..., Cik
k be as in Lemma 5.2. Then we
have
|G|FG(z) =
X
g∈Gk
1 −z2
det(I2n −gz) +
X
g∈G−Gk
1 −z2
det(I2n −gz)
=
ik
X
j=1
X
g∈Gk
1 −z2
det(I2n −gz) +
X
g∈G−Gk
1 −z2
det(I2n −gz)
(5.1)
Set γ = e2π√−1/k. For any primitive k-th root γt of 1, where t is an integer
prime to k, let
ak0(t)
(z −γt)k0 +
ak0−1(t)
(z −γt)k0−1 + ... +
a1(t)
(z −γt)
be the principal part of the Laurent expansion of FG(z) at z = γt. Then each
coefﬁcient ai(t) is an element in the k-th cyclotomic ﬁeld Q(γ) over the rational
number ﬁeld Q. The automorphisms σt of Q(γ) deﬁned by
γ →γt
transforms ai(1) to ai(t) by Equation (5.1). Hence, it is sufﬁcient to show that the
generating function FG(z) has a pole of order k0 at z −γ, that is, to show that
ak0(1) ̸= 0.
Note that if 0 < b < a < π, then cot a−cot b < 0. Now the proposition follows
immediately from Lemma 5.3 and Equation (5.1).
□
From Proposition 5.4, we get
Corollary 5.5. Let S2n−1/G and S2n−1/G′ be two isospectral orbifold spherical
space forms. Then σ(G) = σ(G′).
We now prove our result
Theorem 5.6. Let S2n−1/G and S2n−1/G′ be two (orbifold) spherical space forms.
Suppose G is cyclic and G′ is not cyclic. Then S2n−1/G and S2n−1/G′ cannot be
isospectral.
Proof. By Corollary 2.14, we already know that if |G| ̸= |G′| then S2n−1/G and
S2n−1/G′ cannot be isospectral. So let us assume that |G| = |G′| = q.
Suppose S2n−1/G and S2n−1/G′ are isospectral. If G is cyclic then it has an
element of order q. Now, by Corollary 5.5, G′ must also have an element of order
q, but since |G′| = q, that implies that G′ is cyclic, which is not true by assumption,
and we arrive at a contradiction. This proves the theorem.
□
The above results will complete the classiﬁcation of the inverse spectral problem
on orbifold lens spaces in all dimensions, and also imply that orbifold lens spaces
cannot be isospectral to any other spherical space forms.
21
6. HEAT KERNEL FOR ORBIFOLD LENS SPACES
In the mathematical study of heat conduction and diffusion, a heat kernel is the
fundamental solution to the heat equation on a speciﬁed domain with appropriate
boundary conditions. It is also one of the main tools in the study of the spectrum of
the Laplace operator, and is thus of some auxiliary importance throughout mathe-
matical physics. The heat kernel represents the evolution of temperature in a region
whose boundary is held ﬁxed at a particular temperature (typically zero), such that
an initial unit of heat energy is placed at a point at time t = 0.
In this section we will show that the coefﬁcients of the asymptotic expansion
of the heat trace of the heat kernel are not sufﬁcient to obtain the results in the
previous sections. More speciﬁcally, if two orbifold lens spaces have the same
asymptotic expansion of the heat trace, that does not imply that the two orbifolds
are isospectral.
Deﬁnition 6.1. Let M be a Riemannian manifold. A heat kernel, or alternatively,
a fundamental solution to the heat equation, is a function
(6.1)
K : (0, ∞) × M × M →M
that satisﬁes
(1) K(t, x, y) is C1 in t and C2 in x and y;
(2) ∂K/∂t + ∆2(K) = 0, where ∆2 is the Laplacian with respect to the
second variable (i.e., the ﬁrst space variable);
(3) limt→0+
R
M K(t, x, y)f(y)dy = f(x) for any compactly supported func-
tion f on M.
The heat kernel exists and is unique for compact Riemannian manifolds. Its im-
portance stems from the fact that the solution to the heat equation
∂u
∂t + ∆(u) = 0,
u : [0, ∞) × M →R,
(where ∆is the Laplacian with respect to the second variable) with initial condition
u(0, x) = f(x) is given by
(6.2)
u(t, x) =
Z
M
K(t, x, y)f(y)dy.
If {λi} is the spectrum of M and {ζi} are the associated eigenfunctions (normal-
ized so that they form an orthonormal basis of L2(M)), then we can write
K(t, x, y) =
X
i
e−λitζi(x)ζi(y).
From this, it is clear that the heat trace,
Z(t) =
X
i
e−λit,
22
is a spectral invariant. The heat trace has an asymptotic expansion as t →0+ :
Z(t) = (4πt)dim(M)/2
∞
X
j=1
ajtj,
where the aj are integrals over M of universal homogeneous polynomials in the
curvature and its covariant derivatives ([MP], see [Gi2] or [CPR] for details). The
ﬁrst few of these are
a0 = vol(M),
a1 = 1
6
Z
M
τ,
a2 =
1
360
Z
M
(5τ 2 −2|ρ|2 −10|R|2),
where τ = Pdim(M)
a,b=1
Rabab is the scalar curvature, ρ = Pdim(M)
c=1
Racbc is the
Ricci tensor, and R is the curvature tensor. The dimension, the volume, and the
total scalar curvature are thus completely determined by the spectrum. If M is a
surface, then the Gauss-Bonnet Theorem implies that the Euler characteristic of M
is also a spectral invariant.
6.1. Heat Trace Results for Orbifolds. In the case of a good Riemannian orb-
ifold, Donnelly [D] proved the existence of the heat kernel and also proved the
following results:
Theorem 6.2. Let f : M →M be an isometry of a manifold M, with ﬁxed point
set Ω.
i. There is an asymptotic expansion as t ↓0
X
λ
Tr(fλ♯)etλ ≈
X
N∈Ω
(4πt)−n/2
∞
X
k=0
tk
Z
N
bk(f, a)dvolN(a),
where N is a subset of Ω(and a submanifold of M), λ is an eigenvalue
of ∆, fλ♯is a linear map from λ-eigenspace to itself induced by f, and the
functions bk(f, a) depend only on the germ of f and the Riemannian metric
of M near the points a ∈N.
ii. The coefﬁcients bk(f, a) are of the form bk(f, a) = |detB|b
′
k(f, a) where
b
′
k(f, a) is an invariant polynomial in the components of B = (I −A)−1
(where A denotes the endomorphism induced by f on the ﬁber of the nor-
mal bundle over a ∈N ) and the curvature tensor R and its covariant
derivatives at a.
In particular,
23
b0(f, a) =|detB|,
b1(f, a) =|detB|(τ
6 + 1
6ρkk + 1
3RikshBkiBh3 + 1
3RikthBktBhi−
RkαhαBksBhs).
In [DGGW] Donnelly’s work is extended to general compact orbifolds, where
the heat invariants are expressed in a form that clariﬁes the asymptotic contri-
butions of each part of the singular set of the orbifold. We will summarise the
construction used in [DGGW] in the following remarks before stating their main
theorem.
Remarks and Notation:
(1) An Orbifold O was identiﬁed with the orbit space F(O)/O(n), where
F(O) - a smooth manifold - is the orthonormal frame bundle of O and
O(n) is the orthogonal group, acting smoothly on the right and preserving
the ﬁbers. It can be shown that the action of O(n) on the frame bundle F(O)
gives rise to a (Whitney) stratiﬁcation of O. The strata are connected com-
ponents of the isotropy equivalence classes in O. The set of regular points
of O intersects each connected component O0 of O in a single stratum that
constitutes an open dense submanifold of O0. The strata of O are referred
as O-strata.
(2) If ( ˜U, GU, πU) is an orbifold chart on O, then it can be shown that the
action of GU on ˜U gives rise to stratiﬁcations both of ˜U and of U. These
are referred to as ˜U-strata and U-strata, respectively.
(3) Let O be a Riemannian orbifold and ( ˜U, GU, πU) an orbifold chart. Let ˜N
be a ˜U-stratum in ˜U. Then it can be shown that all the points in ˜N have the
same isotropy group in GU; this group is referred to as the isotropy group
of ˜N, denoted Iso( ˜N).
(4) Given a ˜U-stratum ˜N, denote by Isomax( ˜N) the set of all γ ∈Iso( ˜N)
such that ˜N is open in the ﬁxed point set Fix(γ) of γ. For γ ∈GU, it
can be shown that each component W of the ﬁxed point set Fix(γ) of
γ (equivalently, the ﬁxed point set of the cyclic group generated by γ) is
a manifold stratiﬁed by a collection of ˜U-strata, and the strata in W of
maximal dimension are open and their union has full measure in W. In
particular, the union of those ˜U-strata ˜N for which γ ∈Isomax( ˜N) has
full measure in Fix(γ).
(5) Let γ be an isometry of a Riemannian manifold M and let Ω(γ) denote
the set of components of the ﬁxed point set of γ. Each element of Ω(γ)
is a submanifold of M. For each non-negative integer k, Donnelly [D]
deﬁned a real-valued function (cited above), which we temporarily denote
bk((M, γ), .), on the ﬁxed point set of γ. For each W ∈Ω(γ), the re-
striction of bk((M, γ), .) to W is smooth. Two key properties of the bk
are:
24
(a) Locality. For a ∈W, bk((M, γ), a) depends only on the germs at a
of the Riemannian metric of M and of the isometry γ. In particular,
if U is a γ-invariant neighborhood of a in M, then bk((M, γ), a) =
bk((U, γ), a).
(b) Universality. If M and M′ are Riemannian manifolds admitting the
respective isometries γ and γ′, and if σ : M →M′ is an isometry
satisfying σ ◦γ = γ′ ◦σ, then bk((M, γ), x) = bk((M′, γ′), σ(x)) for
all x ∈Fix(γ).
In view of the locality property, we will usually delete the explicit reference
to M and rewrite these functions as bk(γ, .), as they are written in [D].
(6) Let O be an orbifold and let ( ˜U, GU, πU) be an orbifold chart. Let ˜N
be a ˜U-stratum and let γ ∈Isomax( ˜N). Then ˜N is an open subset of a
component of Fix(γ) and thus, bk(γ, .)(= bk(( ˜U, γ), .)) is smooth on ˜N
for each nonnegative integer k. Deﬁne a function bk( ˜N, .) on ˜N by
bk( ˜N, x) =
X
γ∈Isomax( ˜
N)
bk(γ, x).
Deﬁnition 6.3. Let O be a Riemannian orbifold and let N be an O-stratum.
(i) For each nonnegative integer k, deﬁne a real-valued function bk(N, .) by
setting bk(N, p) = bk( ˜N, ˜p) where ( ˜U, GU, πU) is any orbifold chart
about p, ˜p ∈πU −1(p), and ˜N is the ˜U-stratum through ˜p.
(ii) The Riemannian metric on O induces a Riemannian metric - and thus a
volume element - on the manifold N. Set
IN := (4πt)−dim(N)/2
∞
X
k=0
tk
Z
N
bk(N, x)dvolN (x),
where dvolN is the Riemannian volume element.
(iii) Set
I0 = (4πt)−dim(O)/2
∞
X
k=0
ak(O)tk,
where the ak(O) (which we will usually write simply as ak) are the famil-
iar heat invariants. In particular, a0 = vol(O), a1 = 1
6
R
O τ(x)dvolO(x),
and so forth. Observe that if O is ﬁnitely covered by a Riemannian mani-
fold M (say, O = G\M) then ak(O) =
1
|G|ak(M).
We now state the theorem that [DGGW] proved:
Theorem 6.4. Let O be a Riemannian orbifold and let λ1 ≤λ2 ≤... be the
spectrum of the associated Laplacian acting on smooth functions on O. The heat
trace P∞
j=1 e−λjt of O is asymptotic as t →0+ to
I0 +
X
N∈S(O)
IN
|Iso(N)|,
25
where S(O) is the set of all O-strata, |Iso(N)| is the order of the isotropy at each
p ∈N, and Iso(p) is the conjugacy class of subgroups of O(n). This asymptotic
expansion is of the form
(4πt)−dim(O)/2
∞
X
j=0
cjtj/2
for some constants cj .
6.2. Heat Kernel For 3-Dimensional Lens Spaces. We deﬁne the normal coor-
dinates for a three-sphere as follows [Iv]: Consider a three-sphere of radius r,
S3(r) = {(v1, v2, v3, v4) ∈R4 : (v1)2 + (v2)2 + (v3)2 + (v4)2 = r2},
and let (R, ψ, θ, φ) be the spherical coordinates in R4 where R ∈(0, ∞), ψ ∈
[0, 2π], θ ∈(0, π] and φ ∈(0, π]. These coordinates are connected with the
standard coordinate system (u1, u2, u3, u4) in R4 by the following equations:
u1 = R sin ψ sin θ cos φ,
u2 = R sin ψ sin θ sin φ,
u3 = R sin ψ cos θ,
u4 = R cos ψ.
(6.3)
The equation of S3(r) in these coordinates is R2 = r2. The functions x1 = ψ,
x2 = θ, and x3 = φ provide an internal coordinate system on S3(r) (without one
point) in which the metric g induced on S3(r) from E3 has components gij such
that
(gij) =



r2
0
r2 sin2 ψ
0
r2 sin2 ψ sin2 θ


.
g induces on S3(r) a Riemannian connection ▽. Using the formula
Γm
ij = 1
2gml[∂jgil + ∂iglj −∂lgji],
we can calculate the Christoffel symbols, which are as follows:
Γ2
21 = Γ2
12 = cot ψ, Γ3
31 = Γ3
13 = cot ψ, Γ3
32 = Γ3
23 = cot θ, Γ1
22 = −sin ψ cos ψ,
Γ1
33 = −sin ψ cos ψ sin2 θ, Γ2
33 = −sin θ cos θ. All the other symbols are zero.
Now let γ : [0, 2π] →S3(r) be a path in S3(r) such that xi◦γ = π/2 for i = 1, 2
and x3 ◦γ = id|[0,2π]. Since cos π/2 = cot π/2 = 0 and sin π/2 = 1 we have
Γi
jk|γ([0,2π]) = 0, and consequently, if we take R = r = 1, we get gij = δj
i . There-
fore, the coordinate system {x1, x2, x3} and the frame {∂/∂x1, ∂/∂x2, ∂/∂x3}
are normal for ▽along the path γ.
From the Equations (6.3) it is clear that the set γ([0, 2π]) is a circle obtained by
intersecting S3(r) with the (v1, v2)−plane {v ∈R4 : vi(p) = 0 fori ≥3} in R4.
In fact, we have
γ([0, 2π]) = {(v1, v2, 0, 0) ∈R4 : v2
1 + v2
2 = r2} = S1(r) × (0, 0).
26
It is clear if C is a circle on S3(r) obtained by intersecting S3(r) by a 2-plane
through its origin then there are coordinates on S3(r) normal along C for the Rie-
mannian connection considered above.
We will assume r = 1. Then, using the above normal coordinate system, and
the formulas
Ri
jlm = ∂lΓi
mj −∂mΓi
lj + Γk
mjΓi
lk −Γk
ljΓi
km,
Rabcd = gajRj
bcd,
we calculate the values of the curvature as follows:
R1212 = Rψθψθ = sin2 ψ,
R1313 = Rψφψφ = sin2 ψ sin2 θ,
R2323 = Rθφθφ = sin4 ψ sin2 θ.
All other values are zero. The values of the Ricci tensor, calculated by ρab = Rc
acb,
are as follows:
ρ11 = ρψψ = 2,
ρ22 = ρθθ = 2 sin2 ψ,
ρ33 = ρφφ = 2 sin2 ψ sin2 θ.
All other values are zero. We then calculate the scalar curvature as follows:
τ = gψψρψψ + gθθρθθ + gφφρφφ = 6.
Since τ is constant all its covariant derivatives, τ;j are zero. Using ρab;m = ∂mρab−
ρlbΓl
ma −ρalΓl
mb, we also calculate all the covariant derivatives of the Ricci tensor,
which turn out to be zero as well.
Let e1 = (1, 0, 0, 0), e2 = (0, 1, 0, 0), e3 = (0, 0, 1, 0) and e4 = (0, 0, 0, 1) be
the standard basis in R4. We deﬁne the following two subsets:
Na =
n
(x, y, 0, 0) : x2+y2 = 1
o
⊂R4 and Nb =
n
(0, 0, z, w) : z2+w2 = 1
o
⊂R4.
The tangent space Te1S3, has basis vectors {e2, e3, e4} such that {e2} is a basis
for Te1Na and {e3, e4} is a basis for Te1N ⊥
a . Similarly, the tangent space Te4S3,
has basis vectors {e1, e2, e3} such that {e3} is a basis for Te4Nb and {e1, e2} is
a basis for Te4N ⊥
b . We will now calculate the values for b0(f, a) and b1(f, a).
Suppose O = S3/G is an orbifold lens space where G =< γ > and
γ =



R( ˆ
p1
q )
0
0
R( ˆp2
q )


,
where ˆp1 ̸≡± ˆp2 (mod q). Suppose gcd( ˆp1, q) = q1 and gcd( ˆp2, q) = q2, so that
ˆp1 = p1q1, ˆp2 = p2q2 and q = ˆαq1 = ˆβq2. Suppose gcd(ˆα, ˆβ) = g so that
ˆα = αg, ˆβ = βg and gcd(α, β) = 1. This means we can write γ as
27
γ =


R( p1
αg)
0
0
R( p2
βg)

.
Now
γ ˆα =


I2
0
0
R(p2α
β )


ﬁxes Na, and
γ
ˆβ =


R(p1β
α )
0
0
I2


ﬁxes Nb, where I2 is the 2 × 2 identity matrix.
Note that since the group action is transitive and the ﬁxed point sets are S1, the
functions bk(., .) are constant along these ﬁxed circles. Therefore, it sufﬁces to
consider just a single point in these ﬁxed point sets to calculate the values of the
functions. We will choose the points e1 ∈Na and e4 ∈Nb to calculate the values
of functions.
We have, in the notation of the Theorem 6.4, ˜
Na ∼= S1 × {(0, 0)} and ˜
Nb ∼=
{(0, 0)} × S1. Also, IsoNa = {1, γ ˆα, γ2ˆα, ...γ(β−1)ˆα}, |IsoNa| = β, IsoNb =
{1, γ ˆβ, γ2ˆβ, ...γ(α−1)ˆβ} and |IsoNb| = α.
We now use Theorem 6.4 to calculate the heat trace asymptotic for O using the
formula I0 + INa
β +
INb
α where
I0 = (4πt)−dim(O)/2
∞
X
k=0
ak(O)tk = (4πt)−dim(O)/2
∞
X
k=0
1
|G|ak(S3)tk
= (4πt)−3/2
q
∞
X
k=0
√π
4k! tk = (4t)−3/2
4qπ
∞
X
k=0
tk
k! = t−3/2
32qπ et,
and for i ∈a, b,
INi = (4πt)−dim(Ni)/2
∞
X
k=0
tk
Z
Ni
bk(Ni, x)dvolNi(x)
= (πt)−1/2
2
∞
X
k=0
tk
Z
˜
Ni
bk( ˜
Ni, x)dvol ˜
Ni(x), since ˜
Ni →Ni is trivial in this case
= (πt)−1/2
2
∞
X
k=0
tk2πbk( ˜
Ni, x) (for any choice of x by homogeneity)
= √πt−1/2
∞
X
k=0
tkbk( ˜
Ni, x) , where bk( ˜
Ni, x) =
X
γ∈Isomax ˜
Ni
bk(γ, x).
28
Now for a = e1 and r ∈{1, 2, ...(β −1)},
Bγr ˆα(a) = (I −Aγr ˆα(a))−1 =
1
4 sin2 p2παr
β



1 −cos 2p2παr
β
−sin 2p2παr
β
sin 2p2παr
β
1 −cos 2p2παr
β



= 1
2


1
−cot p2παr
β
cot p2παr
β
1

.
So, |detBγr ˆα(a)| = 1
4(1 + cot2 p2παr
β
) =
1
4 sin2 p2παr
β
.
Similarly we can show that for b = e4 and r ∈{1, 2, ...(α −1)},
Bγr ˆβ(b) = 1
2


1
−cot p1πβr
α
cot p1πβr
α
1

,
and |detBγr ˆβ(b)| = 1
4(1 + cot2 p1πβr
α
) =
1
4 sin2 p1πβr
α
.
We will now calculate bi( ˜
Nj, .) for i = 0, 1 and j = a, b:
b0(γrˆα, a) = |detBγr ˆα(a)| = 1
4(1 + cot2 p2παr
β
) =
1
4 sin2 p2παr
β
.
So,
b0( ˜
Na, a) =
X
f∈Isomax ˜
Na
b0(f, a)
=
β−1
X
r=1
b0(γrˆα, a)
=
β−1
X
r=1
1
4(1 + cot2 p2παr
β
)
=
β−1
X
r=1
1
4(1 + cot2 πr
β ) , since gcd(p2α, β) = 1
=
β−1
X
r=1
1
4 sin2 πr
β
= β2 −1
12
, by lemma 5.4 in [DGGW].
We can similarly show that
b0( ˜
Nb, b) =
α−1
X
r=1
1
4(1 + cot2 πr
α ) = α2 −1
12
.
29
We will now calculate b1( ˜
Na, a) and b1( ˜
Nb, b). Note that for both Bγr ˆα(a) and
Bγr ˆβ(b), B13 = B23 = B31 = B32 = B33 = 0. Using the formula in Theorem
6.2, we get
b1(γrˆα, a) = |det(Bγr ˆα(a))|
3
n
R1212
h
2 −1
4(cot θr −cot θr)2 −(1
2 + 1
2)2 −2((1
4 + 1
4)
i
+ R1313
h
2 −(1
2 + 0)2 −2(1
4 + 0) −3(1
4 cot2 θr + 0)
i
+ R2323
h
2 −(1
2 + 0)2 −2(1
4 + 0) −3(1
4 cot2 θr + 0)
io
,
which gives
b1(γrˆα, a) = 1
12(1 + cot2 θr)
n
R1313

2 −3
4 −3
4 cot2 θr)

+ R2323

2 −3
2 −3
4 cot2 θr)
o
= 1
12(1 + cot2 θr)(R1313 + R2323)[2 −3
4(1 + cot2 θr)]
= (R1313 + R2323)
h1
6(1 + cot2 θr) −1
16(1 + cot2 θr)2i
= (R1313 + R2323)
h
1
6 sin2 θr
−
1
16 sin2 θr
i
,
where θr = p2παr
β
.
So,
b1( ˜
Na, a) =
β−1
X
r=1
b1(γrˆα, a)
=
β−1
X
r=1
(R1313 + R2323)
h
1
6 sin2 p2παr
β
−
1
16 sin2 p2παr
β
i
= (R1313 + R2323)
h1
6
β−1
X
r=1
1
sin2 πr
β
−1
16
β−1
X
r=1
1
sin4 πr
β
i
,
since gcd(p2α, β) = 1.
Also, Pβ−1
r=1
1
sin2 πr
β = β2−1
3
and Pβ−1
r=1
1
sin4 πr
β = β4+10β2−11
45
(see [DGGW]). So
we get
b1( ˜
Na, a) = (R1313 + R2323)
β2 −1
18
−β4 + 10β2 −11
720

= −(R1313 + R2323)(β2 −29)(β2 −1)
720
.
We can similarly show that
b1( ˜
Nb, b) = (R1313 + R2323)
α2 −1
18
−α4 + 10α2 −11
720

= −(R1313 + R2323)(α2 −29)(α2 −1)
720
.
30
Using Theorem 6.4 we now calculate the ﬁrst few coefﬁcients of the asymptotic
expansion as follows:
I0 +
INa
|Iso(Na)| +
INb
|Iso(Nb)|
=t−3/2
32qπ et + (πt)−1/2
β
h
t0πb0( ˜
Na, a) + t1πb1( ˜
Na, a) + ...
i
+ (πt)−1/2
α
h
t0πb0( ˜
Nb, b) + t1πb1( ˜
Nb, b) + ...
i
=t−3/2
32qπ (1 + t + t2
2 + t3
6 + t4
24 + ...) +
b0( ˜
Na, a)
β
+ b0( ˜
Nb, b)
α
√πt−1/2
+
b1( ˜
Na, a)
β
+ b1( ˜
Nb, b)
α
√πt1/2 + ...
From this, the coefﬁcient of t−3/2 is
1
32qπ;
the coefﬁcient of t−1/2 is
1
32qπ + b0( ˜
Na, a)
β
√π + b0( ˜
Nb, b)
α
√π =
1
32qπ +
√π
12β (β2 −1) +
√π
12α(α2 −1);
and the coefﬁcient of t1/2 is
1
64qπ −
√π(R1313 + R2323)[α(β2 −29)(β2 −1) + β(α2 −29)(α2 −1)]
720αβ
;
The above results show that the coefﬁcients are dependent on α, β and the cur-
vature tensor and its covariant derivatives. Since all lens spaces are ﬁnitely covered
by S3, the parts of the coefﬁcients that consist of the curvature tensor and its co-
variant derivatives will be the same for all lens spaces. The only difference will
therefore be in the terms containing α and β. We can rewrite
b0( ˜
Na, a) =
β−1
X
r=1
1
4(1 + cot2 p2παr
β
) =
β−1
X
r=1
1
4 +
β−1
X
r=1
1
4 cot2 p2παr
β
,
b0( ˜
Nb, b) =
α−1
X
r=1
1
4(1 + cot2 p1πβr
α
) =
α−1
X
r=1
1
4 +
α−1
X
r=1
1
4 cot2 p1πβr
α
,
31
b1( ˜
Na, a) =
β−1
X
r=1
(R1313 + R2323)
h1
6(1 + cot2 p2απr
β
) −1
16(1 + cot2 p2απr
β
)2i
=
β−1
X
r=1
5(R1313 + R2323)
48
+
β−1
X
r=1
R1313 + R2323
24

cot2 p2απr
β
−
β−1
X
r=1
R1313 + R2323
16

cot4 p2απr
β
,
b1( ˜
Nb, b) =
α−1
X
r=1
(R1313 + R2323)
h1
6(1 + cot2 p1βπr
α
) −1
16(1 + cot2 p1βπr
α
)2i
=
α−1
X
r=1
5(R1313 + R2323)
48
+
α−1
X
r=1
R1313 + R2323
24

cot2 p1βπr
α
−
α−1
X
r=1
R1313 + R2323
16

cot4 p1βπr
α
,
Note that each bj( ˜
Na, a), (j = 0, 1) is of the form
bj( ˜
Na, a) =
β−1
X
r=1
Aj
X
i=1
Ca
ij(R) cotλi p2απr
β
,
where Aj is the ﬁnite number of monomials in the powers of cot p2απr
β
, and for
each i, Ca
ij(R) are constant functions in terms of the curvature tensor and its co-
variant derivatives of the covering space, i.e. the sphere. Since gcd(p2α, β) = 1,
and we are summing over r as it ranges from 1 to β −1, we can write
bj( ˜
Na, a) =
β−1
X
r=1
Aj
X
i=1
Ca
ij(R) cotλi πr
β .
Similarly, since gcd(α, p1β) = 1, we can write
bj( ˜
Nb, b) =
α−1
X
r=1
Aj
X
i=1
Cb
ij(R) cotλi πr
α .
More generally, for any k, the functions bk(γrˆα, a) and bk(γr ˆβ, a) are universal
polynomials in the components of the curvature tensor, its covariant derivatives and
the elements of Bγr ˆα(a) and Bγr ˆβ(b) respectively. Since the elements of Bγr ˆα(a)
are B11 = B22 = 1/2, B12 = −1
2 cotλi p2απr
β
and B21 = 1
2 cotλi p2απr
β
, every
bk(γrˆα, a) will be of the form PAj
i=1 Ca
ij(R) cotλi p2απr
β
. This means that for each
k, we will have,
bk( ˜
Na, a) =
β−1
X
r=1
Ak
X
i=1
Ca
ik(R) cotλi πr
β ,
32
and similarly,
bk( ˜
Nb, b) =
α−1
X
r=1
Ak
X
i=1
Cb
ik(R) cotλi πr
α .
This observation gives us the following lemma for three-dimensional orbifold lens
spaces:
Lemma 6.5. Given two orbifold lens spaces O1 = S3/G1 and O2 = S3/G2, such
that G1 =< γ1 > and G2 =< γ2 > where
γ1 =



R( ˆp1
q )
0
0
R( ˆ
p2
q )



with ˆp1 ̸≡± ˆp2 (mod q), gcd( ˆp1, q) = q11, gcd( ˆp2, q) = q21, ˆp1 = p1q11, ˆp2 =
p2q21, q = ˆα1q11 = ˆβ1q21, gcd( ˆ
α1, ˆβ1) = g1, ˆα1 = α1g1, ˆβ1 = β1g1, and
γ2 =



R( ˆs1
q )
0
0
R( ˆs2
q )


,
with ˆs1 ̸≡± ˆs2 (mod q), gcd( ˆs1, q) = q12, gcd( ˆs2, q) = q22, ˆs1 = s1q12, ˆs2 =
s2q22, q = ˆα2q12 = ˆβ2q22, gcd( ˆ
α2, ˆβ2) = g2, ˆα2 = α2g2, ˆβ2 = β2g2.
Then O1 = S3/G1 and O2 = S3/G2 will have the exact same asymptotic expan-
sion of the heat kernel if α1 = α2 and β1 = β2.
This lemma gives us a tool to ﬁnd examples of 3-dimensional orbifold lens
spaces that are non-isometric (hence non-isospectral) but have the exact same as-
ymptotic expansion of the heat kernel.
Example 6.6. Suppose q = 195, and consider the two lens spaces O1 = L(195 :
3, 5) and O2 = L(195 : 6, 35). Since there is no integer l coprime to 195 and no
ei ∈{1, −1} such that {e1l3, e2l5} is a permutation of {6, 35}(mod q), O1 and
O2 are not isometric (and hence non-isospectral). However, in the notation of the
lemma above, ˆp1 = 3, ˆp2 = 5, ˆs1 = 6, ˆs2 = 35, gcd( ˆp1, q) = 3 = gcd( ˆs1, q),
gcd( ˆp2, q) = 5 = gcd( ˆs2, q) and q = 195 = 3 × 65 = 5 × 39. So, ˆα1 = ˆα2 = 65
and ˆβ1 = ˆβ2 = 39, with gcd( ˆαi, ˆβi) = 13 (for i = 1, 2) giving α1 = α2 = 5 and
β1 = β2 = 3. Therefore, O1 = L(195 : 3, 5) and O2 = L(195 : 6, 35) have the
exact same asymptotic expansion.
6.3. Heat Kernel For 4-Dimensional Lens Spaces. Similar to the three-dimensional
case we can show the construction of examples in four-dimensional lens spaces
where the lens spaces will not be isospectral but will have the exact same asymp-
totic expansion of the trace of the heat kernel. We deﬁne the normal coordinates
for a four-sphere as follows [Iv]: Consider a four-sphere of radius r,
S4(r) = {(v1, v2, v3, v4, v5) ∈R5 : (v1)2 + (v2)2 + (v3)2 + (v4)2 + (v5)2 = r2},
and let (R, ψ, θ, φ, t) be the spherical coordinates in R5 where R ∈(0, ∞), ψ ∈
(0, π], θ ∈(0, π], φ ∈(0, π] and t ∈[0, 2π]. These coordinates are connected
33
with the standard coordinate system (u1, u2, u3, u4, u5) in R5 by the following
equations:
u1 = R sin ψ sin θ sin φ sin t,
u2 = R sin ψ sin θ sin φ cos t,
u3 = R sin ψ sin θ cos φ,
u4 = R sin ψ cos θ,
u5 = R cos ψ.
(6.4)
The equation of S4(r) in these coordinates is R2 = r2. The functions x1 = ψ,
x2 = θ, x3 = φ and x4 = t provide an internal coordinate system on S4(r) (with-
out one point) in which the metric g induced on S4(r) from E3 has components gij
such that
(gij) =





r2
0
r2 sin2 ψ
r2 sin2 ψ sin2 θ
0
r2 sin2 ψ sin2 θ sin2 φ




.
As before, we calculate the values of the curvature tensor as follows:
R1212 = Rψθψθ = sin2 ψ,
R1313 = Rψφψφ = sin2 ψ sin2 θ,
R1414 = Rψtψt = sin2 ψ sin2 θ sin2 φ,
R2323 = Rθφθφ = sin4 ψ sin2 θ,
R2424 = Rθtθt = sin4 ψ sin2 θ sin2 φ,
R3434 = Rφtφt = sin4 ψ sin4 θ sin2 φ.
All other values are zero. The values of the Ricci tensor, calculated by ρab = Rc
acb,
are as follows:
ρ11 = ρψψ = 3,
ρ22 = ρθθ = 3 sin2 ψ,
ρ33 = ρφφ = 3 sin2 ψ sin2 θ,
ρ44 = ρtt = 3 sin2 ψ sin2 θ sin2 φ.
All other values are zero. We then calculate the scalar curvature as follows:
τ = gψψρψψ + gθθρθθ + gφφρφφ + gttρtt = 12.
Now, let e1 = (1, 0, 0, 0, 0), e2 = (0, 1, 0, 0, 0), e3 = (0, 0, 1, 0, 0), e4 =
(0, 0, 0, 1, 0) and e5 = (0, 0, 0, 0, 1) be the standard basis in R5. We can then
deﬁne the following two subsets:
Na =
n
(x, y, 0, 0, v) : x2 + y2 + v2 = 1
o
⊂R5
34
and
Nb =
n
(0, 0, z, w, v) : z2 + w2 + v2 = 1
o
⊂R5.
The tangent space Te1S4, has basis vectors {e2, e3, e4, e5} such that {e2, e5} is
a basis for Te1Na and {e3, e4} is a basis for Te1N ⊥
a . Similarly, the tangent space
Te4S4, has basis vectors {e1, e2, e3, e5} such that {e3, e5} is a basis for Te4Nb and
{e1, e2} is a basis for Te4N ⊥
b .
Suppose O = S4/G is an orbifold lens space where G =< γ > and
γ =








R( ˆ
p1
q )
0
R( ˆp2
q )
0
1








,
where ˆp1 ̸≡± ˆp2 (mod q). Suppose gcd( ˆp1, q) = q1 and gcd( ˆp2, q) = q2, so that
ˆp1 = p1q1, ˆp2 = p2q2 and q = ˆαq1 = ˆβq2. Suppose gcd(ˆα, ˆβ) = g so that
ˆα = αg, ˆβ = βg and gcd(α, β) = 1. This means we can write γ as
γ =








R( p1
αg)
0
R( p2
βg)
0
1








.
Now
γ ˆα =







I2
0
R(p2α
β )
0
1







ﬁxes Na, and
γ
ˆβ =



R(p1β
α )
0
0
I3



ﬁxes Nb. Here I2 and I3 are the 2 × 2 and 3 × 3 identity matrices respectively.
As before, it sufﬁces to consider just a single point in these ﬁxed point sets to
calculate the values of the functions. We will choose the points e1 ∈Na and
e4 ∈Nb to calculate the values of functions.
We have, in the notation of the Theorem 6.4, ˜
Na ∼= S2 × {(0, 0)} and ˜
Nb ∼=
{(0, 0)} × S2. Also, IsoNa = {1, γ ˆα, γ2ˆα, ...γ(β−1)ˆα}, |IsoNa| = β, IsoNb =
{1, γ ˆβ, γ2ˆβ, ...γ(α−1)ˆβ} and |IsoNb| = α.
35
Now, as in the case of three-dimensional lens spaces, we have for a = e1 and
r ∈{1, 2, ...(β −1)},
Bγr ˆα(a) = 1
2


1
−cot p2παr
β
cot p2παr
β
1

.
So, |detBγr ˆα(a)| = 1
4(1 + cot2 p2παr
β
) =
1
4 sin2 p2παr
β
.
Similarly we can show that for b = e4 and r ∈{1, 2, ...(α −1)},
Bγr ˆβ(b) = 1
2


1
−cot p1πβr
α
cot p1πβr
α
1

,
and |detBγr ˆβ(b)| = 1
4(1 + cot2 p1πβr
α
) =
1
4 sin2 p1πβr
α
. Note again that for both
Bγr ˆα(a) and Bγr ˆβ(b), B13 = B23 = B31 = B32 = B33 = B41 = B14 =
B42 = B24 = B43 = B34 = B44 = 0. This means that, just as in the case of
three-dimensional lens spaces, for each k, we will have,
bk( ˜
Na, a) =
β−1
X
r=1
Ak
X
i=1
Ca
ik(R) cotλi πr
β ,
and
bk( ˜
Nb, b) =
α−1
X
r=1
Ak
X
i=1
Cb
ik(R) cotλi πr
α .
Similar to the three-dimensional case, this observation gives us the following lemma:
Lemma 6.7. Given two orbifold lens spaces O1 = S4/G1 and O2 = S4/G2, such
that G1 =< γ1 > and G2 =< γ2 > where
γ1 =










R( ˆp1
q )
0
R( ˆ
p2
q )
0
1










36
with ˆp1 ̸≡± ˆp2 (mod q), gcd( ˆp1, q) = q11, gcd( ˆp2, q) = q21, ˆp1 = p1q11, ˆp2 =
p2q21, q = ˆα1q11 = ˆβ1q21, gcd( ˆ
α1, ˆβ1) = g1, ˆα1 = α1g1, ˆβ1 = β1g1, and
γ2 =










R( ˆs1
q )
0
R( ˆs2
q )
0
1










,
with ˆs1 ̸≡± ˆs2 (mod q), gcd( ˆs1, q) = q12, gcd( ˆs2, q) = q22, ˆs1 = s1q12, ˆs2 =
s2q22, q = ˆα2q12 = ˆβ2q22, gcd( ˆ
α2, ˆβ2) = g2, ˆα2 = α2g2, ˆβ2 = β2g2.
Then O1 = S4/G1 and O2 = S4/G2 will have the exact same asymptotic expan-
sion of the heat kernel if α1 = α2 and β1 = β2.
This lemma gives us a tool to ﬁnd examples of 4-dimensional orbifold lens
spaces that are non-isometric (hence non-isospectral) but have the exact same as-
ymptotic expansion of the heat kernel.
Example 6.8. Suppose q = 195, and consider the two lens spaces O1 = ˜L1+ =
L(195 : 3, 5, 0) and O2 = ˜L′
1+ = L(195 : 6, 35, 0) (using the notation from
Lemma 4.1). Since there is no integer l coprime to 195 and no ei ∈{1, −1} such
that {e1l3, e2l5} is a permutation of {6, 35}(mod q), O1 and O2 are not isometric
(and hence non-isospectral). However, in the notation of the lemma above, ˆp1 = 3,
ˆp2 = 5, ˆs1 = 6, ˆs2 = 35, gcd( ˆp1, q) = 3 = gcd( ˆs1, q), gcd( ˆp2, q) = 5 =
gcd( ˆs2, q) and q = 195 = 3×65 = 5×39. So, ˆα1 = ˆα2 = 65 and ˆβ1 = ˆβ2 = 39,
with gcd( ˆαi, ˆβi) = 13 (for i = 1, 2) giving α1 = α2 = 5 and β1 = β2 = 3.
Therefore, O1 and O2 have the exact same asymptotic expansion.
REFERENCES
[ALR] A. Adem, J. Leida, Y. Ruan, Orbifolds and String Topology, Cambridge Tracts in Mathemat-
ics 171 Cambridge University Press, 2007.
[Ba] N.Bari Orbifold lens spaces that are isospectral but not isometric, Osaka J.Math, 48:1 (2011),
1-40.
[BCDS] P. Buser, J. Conway, P. Doyle and K. Semmler, Some planar isospectral domains, Internat.
Math. Res. Notices. 9 (1994), 391ff., approx. 9 pp. (electronic).
[BGM] M. Berger, P. Gaudachon and E. Mazet, Le spectre d’une vari´et´e riemannienne, Lecture
notes in Mathematics 194, Springer-Verlag, Berlin-Heidelberg-New York, 1971.
[BW] P. B´erard and D. Webb, On ne peut pas entendre l´orientabilit´e d´une surface, C. R. Acad. Sci.
Paris Ser. I Math. 320 (1995), no. 5, 533-536.
[CPR] M. Craioveanu, M. Puta, T. Rassias, Old and new aspects in spectral geometry. Mathematics
and applications. Kluwer Academic, Dordrecht; London, 2001.
[Chi] Chiang, Yuan-Jen, Spectral Geometry of V-Manifolds and its Application to Harmonic Maps,
Proc. Symp. Pure Math. 54 part 1 (1993), 93–99.
[D] H. Donnelly, Spectrum and the ﬁxed point sets of isometries I, Math. Ann. 224 (1976), 161-170.
[DGGW] E. Dryden, C. Gordon, S. Greenwald and D. Webb, Asymptotic expansion of the heat
kernel for orbifolds, Michigan Math J. 56 (2008), 205–238.
37
[DHVW] L. Dixon, J.A. Harvey, C. Vafa, E. Witten, Strings On Orbifolds, Nuclear Physics B261
(1985) 678 - 686.
[DR] P. Doyle and J. Rossetti, Isospectral hyperbolic surfaces having matching geodesics, preprint,
ArXiv math.DG/0605765.
[DV] P.Du Val, Homographies, Quaternions and Rotations, Oxford Math.Monographs, Oxford Uni-
versity Press, 1964.
[GP] O. Grosek and S. Porubsky, Coprime solutions to ax ≡b(mod n), J.Math. Cryptol. 7(2013),
217–224.
[GR] C. S. Gordon and J. Rossetti, Boundary volume and length spectra of Riemannian manifolds:
what the middle degree Hodge spectrum doesnt reveal, Ann. Inst. Fourier, 53 (2003), no. 7,
2297–2314.
[Gi] P. B. Gilkey, On spherical space forms with meta-cyclic fundamental group which are isospec-
tral but not equivariant cobordant. Compositio Mathematica, 56 no. 2 (1985), p. 171-200
[Gi2] P. B. Gilkey, Invariance theory, the heat equation, and the Atiyah-Singer index theorem. Pub-
lish or Perish, Boston, 1984.
[GoM] R. Gornet and J. McGowan, Lens spaces, isospectral on forms but not on functions, London
Math. Soc. J. of Computation 9 (2006) 270–286.
[I1] A. Ikeda, On lens spaces which are isospectral but not isometric, Ann. scient. ´Ec. Norm. Sup.
4e s´eries, t. 13, 303–315.
[I2] A. Ikeda, On the spectrum of a riemannian manifold of positive constant curvature, Osaka J.
Math., 17 (1980), 75–93.
[IY] A. Ikeda and Y. Yamamoto, On the spectra of a 3-dimensional lens space, Osaka J. Math., 16
(1979), 447–469.
[Iv] B. Z. Iliev Handbook of Normal Frames and Coordinates, 51-55.
[K] M. Kac, Can one hear the shape of a drum?, Amer. Math. Monthly 73 (1966) no. 4m Part II,
1–23.
[L]
E.A.Lauret, Spectra of orbifolds with cyclic fundamental groups, Annals of Global Analysis
and Geometry, October, 2015
[MP] S. Minakshisundaram and A. Pleijel, Some properties of the eigen- functions of the Laplace-
operator on Riemannian manifolds. Canadian Journal of Mathematics, 1:242-256, 1949.
[M] J. Milnor, Eigenvalues of the Laplace operator on certain manifolds, Proc. Nat. Acad. Sci. USA
51 (1964), 542.
[PS] E. Proctor and E. Stanhope, An Isospectral Deformation on an Orbifold Quotient of a Nilman-
ifold, Preprint, ArXiv math. 0811.0794
[RSW] J. Rossetti, D. Schueth and M. Weilandt, Isospectral orbifolds with different maximal
isotropy orders, Ann. Glob. Anal. Geom. 34 (2008), 351 - 366
[SSW] N. Shams, E. Stanhope, and D. Webb, One Cannot Hear Orbifold Isotropy Type, Archiv der
Math (Basel) 87 (2006), no.4, 375-384.
[S1] E. Stanhope, Hearing Orbifold Topology, Ph.D. Thesis, Dartmouth College, 2002.
[S2] E. Stanhope, Spectral bounds on orbifold isotropy, Annals of Global Analysis and Geometry
27 (2005), no. 4, 355–375.
[V] M. F. Vign´eras, Vari´et´es Riemanniennes isospectrales et non isometriques, Ann. of Math. 112
(1980), 2132.
[Y] Y. Yamamoto, On The Number Of Lattice Points In The Square |x| + |y| ≤u With A Certain
Congruence Condition, Osaka J. Math., 17 (1980), 9–21.
NAVEED S. BARI, 47 LLOYD WRIGHT AVENUE, MANCHESTER M11 3NJ, UNITED KING-
DOM
E-mail address: bari.naveed@yahoo.com
EUGENIE HUNSICKER, DEPARTMENT OF MATHEMATICS, LOUGHBOROUGH UNIVERSITY,
LOUGHBOROUGH, LE11 3TU, UNITED KINGDOM
E-mail address: E.Hunsicker@lboro.ac.uk
38
