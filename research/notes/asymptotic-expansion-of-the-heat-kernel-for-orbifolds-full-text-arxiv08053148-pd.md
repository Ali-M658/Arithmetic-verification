---
title: Asymptotic expansion of the heat kernel for orbifolds (full text, arXiv:0805.3148
  PDF)
id: asymptotic-expansion-of-the-heat-kernel-for-orbifolds-full-text-arxiv08053148-pd
tags:
- hyperbolic-pillow-heat-novelty-813161
- dggw-2008
- cone-coefficients
- heat-trace-master-expansion
- near-collision-examples
created: '2026-08-09T08:44:37.980983Z'
updated: '2026-08-09T09:36:32.240150Z'
source: https://arxiv.org/pdf/0805.3148
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Full verbatim text of Dryden-Gordon-Greenwald-Webb, ''Asymptotic expansion
  of the heat kernel for orbifolds'' (arXiv:0805.3148v1; published as Michigan Math.
  J. 56 (2008), no. 1, 205-238, DOI 10.1307/mmj/1213972406). Manually extracted via
  PyMuPDF after the automated CLI PDF-fetch mis-flagged the arXiv PDF as JUNK_CONTENT.


  KEY CONTENT FOR CONE-COEFFICIENT QUESTION:

  - Thm 4.8 (master expansion): heat trace ~ I_0 + sum_{N in S(O)} I_N/|Iso(N)|, of
  the form (4pi t)^{-dim(O)/2} sum_j c_j t^{j/2} (eq. 4.9). I_N defined in 4.7(ii)
  as (4pi t)^{-dim(N)/2} sum_k t^k int_N b_k(N,x) dvol_N(x).

  - b_0, b_1 formulas (4.3)-(4.4) are Donnelly''s [ref 10 = Donnelly 1976, Thm 5.1],
  quoted verbatim with indexing conventions (1<=alpha,beta<=m tangent to stratum W,
  m+1<=i,j,k<=n normal indices).

  - Example 5.3: for a cone point of order m, generator gamma, b_0(gamma^j) = |det((I-A_{gamma^j})^{-1})|
  = 1/(4 sin^2(j*pi/m)) for j=1,...,m-1 -- EXACT MATCH to the manuscript''s claimed
  prefactor (1/4)csc^2(j*pi/m).

  - Lemma 5.4: sum_{j=1}^{m-1} 1/sin^2(j*pi/m) = (m^2-1)/3 (proved via cotangent/residue
  identity).

  - Prop 5.5: I_N = (m^2-1)/12 + O(t) for a single cone point stratum N.

  - Eq (5.7)/(5.8): degree-zero term = chi(O)/6 + sum_i (m_i^2-1)/(12 m_i) [orientable]
  or + sum dihedral-corner terms 1/(2n)*(n^2-1)/12 [nonorientable]. This IS the cone(m)=(m^2-1)/(12m)
  formula the manuscript cites, confirmed exactly including the division by isotropy
  order m.

  - Degree-1 (t^1) term: b_1(gamma^j) = R_{1212}/(8 sin^4(j*pi/m)); using the trig-sum
  substitution sum_{j=1}^{m-1} 1/sin^4(j*pi/m) = (m^4+10m^2-11)/45 [attributed to
  Berndt-Yeap and Chen], the coefficient of t is (5.10): a_2/(4pi) + sum_i R_1212(m_i^4+10m_i^2-11)/(360
  m_i) + dihedral terms /720. At constant curvature R_1212=K, this is the b_1(C) cone
  contribution.

  - CRITICAL: DGGW go NO FURTHER than the degree-1 (t^1) term. Table 1 (2-orbifold
  expansions for chi(O)>=0) lists only V/t + [ML/sqrt(t)] + degree-0 constant + O(t)
  or O(sqrt(t)) -- the t^1 coefficient itself is never even evaluated numerically
  for the table''s examples, let alone a degree-2 (t^2, i.e. b_2/l=2) or general-l
  coefficient. No b_l formula for l>=2 appears anywhere in the paper. Search for ''degree
  2'', ''b_2'', ''b_l'', ''general formula'' in the full text returns zero hits.

  - Prop 5.19, 5.20, 5.22 record explicit spherical/flat 2-orbifold NEAR-COLLISIONS
  where the spectral invariant c=12*(degree-0 term) fails to separate distinct orbifolds:
  c=4 for S^2 vs O(*3,3,3)/O(3,*3); c=5 for football O(2,2) vs O(*2,3,6); c=4.5 for
  teardrop O(2) vs O(*2,4,4)/O(4,*2); and nonorientable spherical orbifolds sharing
  a common orientable double cover (O(*m,m)/O(m x)/O(m*), O(*2,2,m)/O(2,*m), O(*2,3,3)/O(3,*2))
  are only separated by using the degree -1/2 mirror-locus term together with constant-curvature
  metric assumptions, not by c alone.

  - References list gives Donnelly''s citation verbatim: ''[10] H. Donnelly, Spectrum
  and the fixed point sets of isometries I, Math. Ann. 224 (1976), 161-170.'''
---

PROVENANCE NOTE: The hyperresearch CLI automated fetch tool rejected
https://arxiv.org/pdf/0805.3148 with error JUNK_CONTENT ("Binary PDF garbage
in content") on repeated attempts. This note was created manually: the PDF
was downloaded directly from https://arxiv.org/pdf/0805.3148 via curl (HTTP
200, verified valid PDF, 35 pages, PDF 1.4) and full text was extracted with
PyMuPDF (fitz). The extraction below is the complete verbatim text of the
paper as served by arXiv, preserving section numbering, equation numbers, and
in-line formulas exactly as they appear in the PDF (mathematical symbols may
render with minor OCR/ligature artifacts from PDF text extraction, e.g.
"ﬁ"->"fi" ligatures; equation content itself is character-for-character from
the PDF text layer, not re-typed from memory).

FULL BIBLIOGRAPHIC RECORD (from paper header/footer and References list):
Emily B. Dryden, Carolyn S. Gordon, Sarah J. Greenwald, David L. Webb,
"Asymptotic expansion of the heat kernel for orbifolds," arXiv:0805.3148v1
[math.DG], submitted 20 May 2008. Comments field on arXiv abs page: "to
appear in Michigan Math. J." arXiv-issued DOI: 10.48550/arXiv.0805.3148.

=====================================================================
VERBATIM FULL TEXT EXTRACTED FROM PDF (pymupdf get_text(), page by page)
=====================================================================

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR
ORBIFOLDS
EMILY B. DRYDEN, CAROLYN S. GORDON, SARAH J. GREENWALD,
AND DAVID L. WEBB
ABSTRACT. We study the relationship between the geometry and the Laplace
spectrum of a Riemannian orbifold O via its heat kernel; as in the manifold case,
the time-zero asymptotic expansion of the heat kernel furnishes geometric infor-
mation about O. In the case of a good Riemannian orbifold (i.e., an orbifold
arising as the orbit space of a manifold under the action of a discrete group of
isometries), H. Donnelly [10] proved the existence of the heat kernel and con-
structed the asymptotic expansion for the heat trace. We extend Donnelly’s work
to the case of general compact orbifolds. Moreover, in both the good case and the
general case, we express the heat invariants in a form that clariﬁes the asymptotic
contribution of each part of the singular set of the orbifold. We calculate sev-
eral terms in the asymptotic expansion explicitly in the case of two-dimensional
orbifolds; we use these terms to prove that the spectrum distinguishes elements
within various classes of two-dimensional orbifolds.
CONTENTS
1.
Introduction
1
Acknowledgments
3
2.
Orbifolds and their singular sets
3
3.
Construction of the heat expansion
9
4.
Computation of the heat asymptotics
15
5.
Applications
23
References
34
1. INTRODUCTION
Roughly speaking, a topological orbifold is a space locally homeomorphic to an
orbit space of a ﬁnite group action on Rn. A smooth orbifold consists of a Haus-
dorff second countable topological space together with an atlas of coordinate charts
realizing such local homeomorphisms and satisfying compatibility conditions (see
Section 2). Orbifolds were introduced by Satake, then studied by Thurston be-
cause of their utility in the investigation of three-manifolds (e.g., a Seifert ﬁbred
three-manifold is naturally a generalized circle bundle over a two-orbifold); today,
Gordon and Webb were supported in part by NSF grants DMS-0072534, DMS-0306752, and
DMS-0605247; Greenwald was supported in part by NSF ROA grants 0072533 and 9972304.
1
arXiv:0805.3148v1  [math.DG]  20 May 2008

2
DRYDEN, GORDON, GREENWALD, AND WEBB
orbifolds arise naturally in diverse branches of mathematics and physics, including
symplectic geometry, string theory, and vertex operator algebras.
We will be interested in orbifolds from a spectral-theoretic point of view. An
orbifold endowed with a metric structure is a Riemannian orbifold. As in the man-
ifold case, associated with every Riemannian metric is a Laplace operator acting
on smooth functions on the orbifold. In the case of closed orbifolds, the Lapla-
cian has a discrete spectrum. We study the relationship between the geometry and
the Laplace spectrum of a closed orbifold via its heat kernel; as in the manifold
case, the time-zero asymptotic expansion of the heat kernel furnishes geometric
information about the orbifold.
Orbifolds began appearing sporadically in the spectral theory literature in the
early 1990s, and have received more concentrated attention in the last ﬁve years. C.
Farsi [15] showed that the spectrum of an orbifold determines its volume by prov-
ing that Weyl’s asymptotic formula holds for orbifolds. Dryden and A. Strohmaier
[13] showed that for a compact, negatively curved two-dimensional orbifold, the
Laplace spectrum determines both the length spectrum and the orders of the sin-
gular points and vice versa; on the other hand, P. Doyle and J.P. Rossetti [12]
gave (disconnected) examples of isospectral ﬂat two-dimensional orbifolds with
different length spectra and orders of singular points. Further investigations of the
relationship between the lengths of closed geodesics and the spectrum were carried
out by E. Stanhope and A. Uribe in [29]. It is natural to ask about the singularities
that can appear in an isospectral family of orbifolds. Stanhope [28] showed that, in
general, there can be at most ﬁnitely many isotropy types (up to isomorphism) in a
set of isospectral Riemannian orbifolds that share a uniform lower bound on Ricci
curvature. On the other hand, N. Shams, Stanhope, and Webb [27] constructed
arbitrarily large (ﬁnite) isospectral sets of orbifolds satisfying this curvature con-
dition whose isotropy types differ. Rossetti, D. Schueth, and M. Weilandt [25] re-
cently constructed a pair of isospectral Riemannian orbifolds whose isotropy types
have different orders.
For Riemannian manifolds, the asymptotic expansion of the heat kernel can be
used to relate the geometry of the manifold to its spectrum. From the so-called
heat invariants appearing in the asymptotic expansion, one can tell the dimension,
the volume, and various quantities involving the curvature of the manifold. The
heat kernel has been studied in various analogous or more general settings (e.g.
[4, 5, 6, 11, 17, 24]).
In the case of a good Riemannian orbifold (i.e., an orbifold arising as the orbit
space of a manifold under the action of a discrete group of isometries), H. Donnelly
[10] proved the existence of the heat kernel and constructed the asymptotic expan-
sion for the heat trace. We extend Donnelly’s work to the case of general compact
orbifolds. Moreover, in both the good case and the general case, we express the
heat invariants in a form that clariﬁes the asymptotic contribution of each part of
the singular set of the orbifold.

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
3
We calculate several terms in the asymptotic expansion explicitly in the case
of two-dimensional orbifolds; we use these terms to prove that the spectrum dis-
tinguishes elements within various classes of two-dimensional orbifolds. In par-
ticular, within the class of all two-dimensional orbifolds with nonnegative Euler
characteristic, the spectrum is a complete topological invariant. Additional results
are obtained for triangular pillow orbifolds endowed with a hyperbolic structure,
and for nonorientable two-dimensional orbifolds.
The paper is organized as follows. In Section 2, we give the background neces-
sary for the rest of the paper, recalling several results that clarify the structure of the
singular locus of an orbifold. Section 3 is devoted to the construction of the heat
kernel on an arbitrary closed Riemannian orbifold by means of the construction
of a parametrix. The existence of the heat kernel for closed orbifolds was shown
previously by Y.-J. Chiang [8]; existence also follows from more general results
for the heat kernel on Riemannian foliations (see [24]). However, we give a differ-
ent construction in order to express the heat kernel in a convenient form that will
allow us, in Section 4, to generalize Donnelly’s asymptotic expansion. Section 5 is
devoted to various applications of the heat expansion, including those mentioned
in the previous paragraph.
Acknowledgments. The initial inspiration for this project came from Shunhui
Zhu, and the authors thank him for sharing his curiosity. We also thank Iosif
Polterovich for helpful discussions and encouragement, and Alejandro Uribe and
Liz Stanhope for alerting us to the frame bundle approach. The ﬁrst named au-
thor acknowledges the Centre Interfacultaire Bernoulli in Lausanne, Switzerland,
and the Centro de An´alise Matem´atica, Geometria e Sistemas Dinˆamicos, Instituto
Superior T´ecnico, in Lisbon, Portugal, for their support during her work on this
project.
2. ORBIFOLDS AND THEIR SINGULAR SETS
2.1. DEFINITION.
(i) An orbifold chart on a topological space X consists of a connected open
subset eU of Rn, a ﬁnite group GU acting on eU by diffeomorphisms, and a
mapping πU from eU onto an open subset U of X inducing a homeomor-
phism from the orbit space GU\eU onto U. We will always assume that
the group GU acts effectively on eU.

4
DRYDEN, GORDON, GREENWALD, AND WEBB
(ii) An embedding λ : (eU, GU, πU) →(eU′, GU′, πU′) between orbifold charts
with U ⊆U′ is a smooth embedding λ : eU →eU′ such that the diagram
eU /
λ
/
πU 
f
U′
πU′

GU\eU
∼

GU′\f
U′
∼

U  
/ U′
commutes. Two charts (eU, GU, πU) and (eU′, GU′, πU′) on X are said
to be compatible if, for each point x ∈U ∩U′, there exists an orb-
ifold chart (eU′′, GU′′, πU′′) with U′′ ⊂U ∩U′ and smooth embeddings
(eU′′, GU′′, πU′′) →(eU, GU, πU) and (eU′′, GU′′, πU′′) →(eU′, GU′, πU′).
(iii) An n-dimensional orbifold atlas A on X is a compatible family of n-
dimensional orbifold charts whose images form a covering of X. A re-
ﬁnement A′ of an orbifold atlas A is an orbifold atlas each of whose charts
embeds into a chart of A. Two orbifold atlases are said to be equivalent
if they have a common reﬁnement. Every orbifold atlas is equivalent to a
unique maximal one. An orbifold is a Hausdorff, second countable topo-
logical space together with a maximal orbifold atlas.
(iv) Let O be an orbifold. A point x of O is said to be singular if for some
(hence every) orbifold chart (eU, GU, πU) about x, the points in the inverse
image of x in eU have nontrivial isotropy in GU. The isomorphism class of
the isotropy group, called the abstract isotropy type of x, is independent
both of the choice of point in the inverse image of x in eU and of the
choice of chart (eU, GU, πU) about x. Points that are not singular are called
regular.
2.2. REMARKS.
(i) The notion of orbifold generalizes slightly the notion of V -manifold in-
troduced by Satake [26]; V -manifolds are orbifolds for which the singular
set has codimension at least two.
(ii) Given an embedding λ : (eU, GU, πU) →(eU′, GU′, πU′) as in Deﬁnition
2.1, there exists a homomorphism τ : GU →GU′ such that λ ◦γ =
τ(γ) ◦λ for all γ ∈GU. This was proven by Satake for V -manifolds
and was generalized to orbifolds by Moerdijk and Pronk [20]. From our
convention that the group actions on each chart are effective, it follows
that the homomorphism τ is injective.
(iii) There are some subtle differences among the deﬁnitions of orbifold in the
literature; in particular, some authors do not require that the ﬁnite group
actions in the orbifold charts be effective. The deﬁnition we use is that
in [20]. While these distinctions become signiﬁcant when formulating the

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
5
correct notion of the category of smooth orbifolds, they play no role in
our computations.
An orbifold is said to be good if it is the orbit space of a manifold under the
smooth action of a discrete group; otherwise, it is said to be bad. In particular,
every point in an orbifold has a neighborhood that is a good orbifold. Even a bad
orbifold can be expressed globally as the quotient of a manifold by a group action,
although not a discrete group action. This is done by introducing a Riemannian
structure and constructing the “bundle” of orthonormal frames. The orthonormal
frame bundle is actually an orbibundle, the appropriate notion of vector bundle
over an orbifold as described in [19] or [30]. However, its total space is a smooth
manifold with an action of the orthogonal group, and one recovers the original orb-
ifold as the orbit space of this orthogonal action. We will review this construction
below after ﬁrst establishing some notation in the setting of arbitrary group actions.
2.3. DEFINITION. (See [14, Chapter 2].)
(i) Consider a smooth proper action of a Lie group H on a smooth manifold
M. For ex ∈M, let IsoH(ex) denote the subgroup of H that ﬁxes ex.
Deﬁne an equivalence relation on M by ex ≡ey if IsoH(ex) and IsoH(ey)
are conjugate. Each equivalence class is called an H-orbit type. Note that
the equivalence classes are invariant under the action of H.
We will say that the H-orbit type of ex dominates that of ey if IsoH(ex) is
conjugate to a subgroup of IsoH(ey).
(ii) Let π : M →H\M be the projection onto the orbit space. Let p ∈H\M.
As ˜p ranges over the H-orbit π−1(p) in M, the stabilizer IsoH(˜p) ranges
over a conjugacy class of subgroups of H. We will denote this conjugacy
class of subgroups by IsoH(p) and refer to it as the H-isotropy type of p.
Deﬁne an equivalence relation on H\M by p ≡q if IsoH(p) = IsoH(q).
The equivalence classes will be called H-isotropy equivalence classes.
Note that π carries points of the same H-orbit type in M to points of the
same H-isotropy equivalence class in H\M.
We will say that the H-isotropy equivalence class of p dominates that
of q if the groups making up the conjugacy class IsoH(p) are conjugate to
subgroups of those in IsoH(q).
By an abuse of notation, we will write |IsoH(p)| to mean the order of
each of the groups making up the isotropy type IsoH(p). We will refer to
this quantity as the order of the H-isotropy at p.
2.4. DEFINITION.
(i) A Riemannian structure on an orbifold O is an assignment to each orb-
ifold chart (eU, GU, πU) of a GU-invariant Riemannian metric geU on eU
satisfying the compatibility condition that each embedding λ appearing in
Deﬁnition 2.1 is isometric. Every orbifold admits Riemannian structures.
(ii) We will say that an orbifold chart (eU, GU, πU) on a Riemannian orbifold
O is a distinguished chart of radius r if eU is a convex geodesic ball of
radius r. In this case, U is a convex geodesic ball in O. The entire group

6
DRYDEN, GORDON, GREENWALD, AND WEBB
GU ﬁxes the center ˜p of eU, so the abstract isotropy type of p := πU(˜p) is
represented by GU.
2.5. REMARK. Recall that for a Riemannian manifold M and a point p ∈M, the
convexity radius at p is the largest positive real number r(p) for which the geodesic
ball of radius ϵ about p is geodesically convex for all ϵ < r(p). If M is compact,
the inﬁmum r of {r(p) : p ∈M} is positive and is called the convexity radius of
M. For a point p in an orbifold O, we may deﬁne the convexity radius at p to be
the largest real number r(p) such that O admits a distinguished chart of radius ϵ
centered at p for all ϵ < r(p). It is immediate that r(p) is positive. Moreover, if O is
compact, then an elementary argument shows that the inﬁmum r of {r(p) : p ∈O}
is positive; r is called the convexity radius of O.
2.6. ORTHONORMAL FRAME BUNDLE. We give a brief description of the orthonor-
mal frame bundle of a Riemannian orbifold. See [1] for more details. First consider
a good Riemannian orbifold O = G\M, where M is a Riemannian manifold and
G is a discrete group acting by isometries on M. Let F(M) →M be the orthonor-
mal frame bundle of M. Each element γ ∈G, being an isometry of M, induces a
diffeomorphism γ∗of F(M) carrying ﬁbers to ﬁbers; thus we obtain an action of
G on F(M) covering the action of G on M. The orthonormal frame bundle F(O)
of O is deﬁned to be G\F(M) →O. The ﬁber of F(O) →O over x ∈O is the
preimage of x in G\F(M). The right action of O(n) on F(M) commutes with
the left action of G, and hence descends to a right O(n)-action on F(O). For a bad
orbifold, the orthonormal frame bundle is deﬁned in such a way that its restriction
to any good neighborhood U ∼= GU\eU is the orthonormal frame bundle of the
good orbifold U.
The orthonormal frame bundle of O is a smooth manifold as well as an orbi-
bundle on which the orthogonal group O(n) acts smoothly on the right, preserving
ﬁbers. In particular, the orbifold O is the orbit space F(O)/O(n) of the right
action of O(n) on the manifold F(O).
2.7. NOTATION AND REMARKS. Let O be an orbifold. Endow O with a Riemann-
ian metric and let F(O) be the associated orthonormal frame bundle as in 2.6. The
O(n)-action on the ﬁber of F(O) over a point x ∈O is free if and only if x is a
regular point of O. In particular, for each singular point x of O, viewed as an ele-
ment of F(O)/O(n), the O(n)-isotropy type of x is a non-trivial conjugacy class
IsoO(n)(x) of subgroups of O(n). (See Deﬁnition 2.3.)
Our realization of the orbifold O as a global quotient of a manifold (namely
F(O)) by an action of O(n) depends, of course, on the Riemannian metric. How-
ever, it is not difﬁcult to show that the conjugacy class IsoO(n)(x) of subgroups of
O(n) is actually independent of the choice of Riemannian metric used in the con-
struction. This conjugacy class of subgroups of O(n) will henceforth be denoted
Iso(x) (without the subscript O(n) except when needed for clarity) and will be
referred to as the isotropy type of the singular point x of O. Its cardinality |Iso(x)|
will be called the order of the isotropy at x. Similarly, the equivalence classes
of elements of O with the same isotropy type will be called isotropy equivalence
classes, without mention of O(n).

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
7
The subgroups of O(n) in the conjugacy class Iso(x) lie in the isomorphism
class deﬁned by the abstract isotropy type of x given in Deﬁnition 2.1. Indeed,
let (eU, GU, πU) be an orbifold chart with x ∈U. Let ex ∈eU with πU(ex) = x.
With respect to any choice of Riemannian metric on O (and associated Riemannian
metric on eU), the group GU acts isometrically on eU and thus acts on the left on the
orthonormal frame bundle F(eU). The subgroup IsoGU (ex) leaves invariant the ﬁber
of F(eU) over ex. For each q in this ﬁber, deﬁne a homomorphism σq : IsoGU (ex) →
O(n) by the condition γ(q) = (q)σq(γ) where γ(·) and (·)σq(γ) denote the left
action of γ and right action of σq(γ) ∈O(n) on the ﬁber. By 2.6, the restriction
of F(O) to U is given by GU\F(eU). Letting ρ : F(eU) →GU\F(eU) be the
projection, then σq maps IsoGU (ex) isomorphically to the stabilizer of ρ(q) in O(n).
This stabilizer is a representative of the conjugacy class Iso(x), while IsoGU (ex)
represents the abstract isotropy type of x.
2.8. DEFINITION. A smooth stratiﬁcation of a manifold or orbifold M is a locally
ﬁnite partition of M into locally closed submanifolds, called the strata, satisfying
the following condition: For each stratum N, the closure of N is the union of N
with a collection of lower dimensional strata.
2.9. REMARKS.
(i) For any stratiﬁcation of an orbifold (or manifold) O, the strata of maximal
dimension are open in O and their union has full measure in O.
(ii) The stratiﬁcations that we will discuss below are Whitney stratiﬁcations.
As we will not explicitly use the additional properties of Whitney strat-
iﬁcations here, we omit the deﬁnition and refer the reader to [14]. The
notion of Whitney stratiﬁcation can be deﬁned in the more general setting
of spaces that can be at least locally embedded in a smooth manifold. As
discussed in [14], the orbit space of a proper Lie group action on a smooth
manifold has this property.
2.10. PROPOSITION. [14] Given a smooth action of a Lie group H on a manifold
M, then:
(i) The connected components of the H-orbit types form a Whitney stratiﬁca-
tion of M. The closure of a stratum e
N is made up of the union of e
N with
a collection of lower dimensional strata, each lying in an H-orbit type
strictly dominated by that of e
N.
(ii) The connected components of the H-isotropy equivalence classes in H\M
form a Whitney stratiﬁcation of H\M. The closure of a stratum N is made
up of the union of N with a collection of lower dimensional strata, each
lying in an H-isotropy equivalence class strictly dominated by that of N.
The map π carries each stratum in M onto a stratum in H\M.
(iii) For x ∈H\M and N the stratum through x, there exists a neighborhood
U of x in H\M such that the isotropy equivalence class of each element
of the complement of N in U strictly dominates that of x.
(iv) If M is compact, then the stratiﬁcations of M and of H\M are ﬁnite.

8
DRYDEN, GORDON, GREENWALD, AND WEBB
2.11. COROLLARY. Let O be an orbifold. Then the action of O(n) on the frame
bundle F(O) gives rise to a (Whitney) stratiﬁcation of O. The strata are connected
components of the isotropy equivalence classes in O. The set of regular points of
O intersects each connected component O0 of O in a single stratum comprising an
open dense submanifold of O0.
2.12. NOTATION.
(i) We will refer to the strata of O in Corollary 2.11 as O-strata.
(ii) If (eU, GU, πU) is an orbifold chart on O, then the action of GU on eU gives
rise to stratiﬁcations both of eU and of U as in Proposition 2.10. We will
refer to these as eU-strata and U-strata, respectively.
2.13. PROPOSITION. Let O be a Riemannian orbifold and (eU, GU, πU) be an orb-
ifold chart. Then:
(i) The U-strata are precisely the connected components of the intersections
of the O-strata with U.
(ii) Any two elements of the same eU-stratum have the same stabilizers in GU
(not just conjugate stabilizers).
(iii) If H is a subgroup of GU, then each connected component W of the ﬁxed
point set Fix(H) of H in eU is a closed submanifold of eU. Any eU-stratum
that intersects W nontrivially lies entirely in W. Thus the stratiﬁcation of
eU restricts to a stratiﬁcation of W.
Proof. (i) A consequence of Proposition 2.10 is that each U-stratum, respectively
O-stratum, is a connected component of the set of all points in U, respectively O,
having GU-isotropy, respectively O(n)-isotropy, of a given order. Since by 2.7, the
order of the GU-isotropy of each x ∈U is equal to the order of the O(n)-isotropy
of x, statement (i) follows.
(ii) This follows because GU is discrete and the eU-strata are connected.
(iii) The ﬁrst statement is true for the ﬁxed point set of any smooth proper action
by a compact group on a manifold [14]. The second statement follows from (ii).
□
2.14. NOTATION AND REMARKS. Let O be a Riemannian orbifold and (eU, GU, πU)
be an orbifold chart. Let e
N be a eU-stratum in eU. By Proposition 2.13, all the points
in e
N have the same isotropy group in GU; we will refer to this group as the isotropy
group of e
N, denoted Iso( e
N).
Given a eU-stratum e
N, denote by Isomax( e
N) the set of all γ ∈Iso( e
N) such that
e
N is open in the ﬁxed point set Fix(γ) of γ.
For γ ∈GU, Proposition 2.13 tells us that each component W of the ﬁxed point
set Fix(γ) of γ (equivalently, the ﬁxed point set of the cyclic group generated
by γ) is a manifold stratiﬁed by a collection of eU-strata. By Remark 2.9(i), the
strata in W of maximal dimension are open and their union has full measure in
W. In particular, the union of those eU-strata e
N for which γ ∈Isomax( e
N) has full
measure in Fix(γ).

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
9
2.15. EXAMPLE. On R2, let rx and ry denote the reﬂections across the x-axis and
y-axis, respectively, and let r0 denote the rotation through angle π about the origin
0. Then G := {rx, ry, r0, Id} is a Klein four group acting isometrically on R2. The
quotient of R2 by the semi-direct product of G with the lattice Z2 of translations
is a closed orbifold O, whose underlying space is a square of side length 1
2. The
points on the boundary of the square are singular points (not boundary points) of
the orbifold, comprising eight strata: each corner point forms a single stratum with
isotropy of order four, while each open edge forms a stratum with isotropy of order
two. The strata of codimension one are called reﬂectors or mirrors, and the single
point strata are called dihedral points or corner reﬂectors. The intersection U of
the square with a disk of radius less than 1
2 centered at one of the corners is the
image of an orbifold chart (eU, G, πU) where eU is a disk in R2 centered at the
origin and G is the Klein-four group above. The eU-strata of this action consist of
the single point 0 and the intersections of the disk eU with the positive and negative
x-axis and the positive and negative y-axis. If e
N is the intersection of eU with
one of the half axes, then Iso( e
N) consists of a reﬂection and the identity, while
Isomax( e
N) contains only the reﬂection. For e
N = {0}, we have Iso( e
N) = G, but
Isomax( e
N) = {r0}.
3. CONSTRUCTION OF THE HEAT EXPANSION
In this section, we address the heat kernel on closed Riemannian orbifolds.
3.1. PROPOSITION. Let O be a closed Riemannian orbifold. The Laplacian ∆of
O has a discrete spectrum λ1 ≤λ2 ≤. . . , with each eigenvalue having ﬁnite
multiplicity. The normalized eigenfunctions ϕj are C∞and form an orthonormal
basis of L2(O).
This proposition was proved in the case of V -manifolds (as deﬁned in Remark
2.2) by Y.-J. Chiang in [8]. For an orbifold O which is not a V -manifold, those
strata of the singular set of codimension one are called reﬂectors. By doubling
along all reﬂectors one obtains a V -manifold X that doubly covers O. Thus O is
the quotient of a V -manifold X by a Z2 action. Since the eigenfunctions on O are
then the Z2-invariant eigenfunctions on X, Proposition 3.1 follows immediately.
3.2. DEFINITION. Set
R+ = [0, ∞)
and
R∗
+ = (0, ∞).
We say that K : R∗
+ × O × O →R is a fundamental solution of the heat equation,
or heat kernel, if it satisﬁes:
(i) K is C0 in the three variables, C1 in the ﬁrst, and C2 in the second;
(ii)
  ∂
∂t + ∆x

K(t, x, y) = 0 where ∆x is the Laplacian with respect to the
second variable;
(iii) lim
t→0+ K(t, x, ·) = δx for all x ∈O.

10
DRYDEN, GORDON, GREENWALD, AND WEBB
By the same argument as in the manifold case (see [2], III.E.2), Proposition 3.1
implies:
3.3. COROLLARY. If a heat kernel exists, then it is unique and is given by
K(t, x, y) =
∞
X
j=1
e−λjtϕj(x)ϕj(y).
Chiang proved the existence of the heat kernel on a compact V -manifold (from
which existence on an arbitrary closed orbifold trivially follows) by proving the
convergence of P∞
j=1 e−λjtϕj(x)ϕj(y). She also showed that the heat kernel can
be approximated on good neighborhoods by the Dirichlet heat kernel on the local
manifold covering. The existence also follows from more general results on ex-
istence of the heat kernel for the basic Laplacian on Riemannian foliations [22].
However, in order to apply Donnelly’s results on the heat trace for good orbifolds
to obtain the terms in the asymptotic expansion of arbitrary orbifolds in an applica-
ble form, we will not assume the earlier existence results for the heat kernel or heat
trace. We instead construct a parametrix and then follow the standard construction
of the heat kernel from the parametrix as in [2]. Our construction of the parametrix
and consequently the heat kernel will use directly the local structure of orbifolds
as quotients of manifolds by ﬁnite group actions.
3.4. DEFINITION. A parametrix for the heat operator on O is a function H : R∗
+ ×
O × O →R satisfying:
(i) H ∈C∞(R∗
+ × O × O);
(ii)
  ∂
∂t + ∆x

H(t, x, y) extends to a function in C0(R+ × O × O);
(iii) lim
t→0+ H(t, x, ·) = δx for all x ∈O.
Recall that the heat kernel on a closed n-dimensional Riemannian manifold M
has an asymptotic expansion along the diagonal in M × M as t →0+ of the form
(3.5)
K(t, x, x) ∼(4πt)−n
2 (u0(x, x) + tu1(x, x) + t2u2(x, x) + . . . )
where the ui are local Riemannian invariants deﬁned in a neighborhood of the
diagonal in M × M. Letting ζ be a cut-off function that is identically one near the
diagonal, then for m > n
2 , the function
(3.6)
K(m)(t, x, y) = ζ(x, y)(4πt)−n
2 e−d(x,y)2
4t
(u0(x, y) + · · · + tmum(x, y))
is a parametrix for the heat operator on M.
3.7. REMARK. In what follows, we shall take a local covering of our orbifold O
by distinguished charts and piece together a parametrix for the heat operator on
O from the expressions in (3.6). The key to piecing together the parametrix on
O is to note that while the parametrix K(m) in (3.6) is globally deﬁned on M,
the three deﬁning conditions of a parametrix in Deﬁnition 3.4 are satisﬁed locally
as well as globally by K(m). Indeed the ﬁrst two conditions are trivially local.
The third condition is local in the following sense: The expression e−d(x,y)2
4t
goes

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
11
to zero uniformly as t →0+ when d(x, y) is bounded away from zero. Thus for
f ∈C0(M), we have
f(x) = lim
t→0+
Z
M
K(m)(t, x, y)f(y)dy = lim
t→0+
Z
W
K(m)(t, x, y)f(y)dy,
where W is any neighborhood of x.
We will also use the fact (see [2]) that if m > n
2 +2l, then
  ∂
∂t + ∆x

K(m)(t, x, y)
extends to a function in Cl(R+ × M × M). Moreover, the extension is of class
C2l in the last two variables.
3.8. NOTATION. Let O be an orbifold of dimension n. Fix ϵ > 0 so that for each
x ∈O, there exists a distinguished coordinate chart of radius ϵ centered at x. Cover
O with ﬁnitely many such charts (f
Wα, Gα, πα), α = 1, . . . , s. (Here we write Gα
for GWα and πα for πWα.) Let pα be the center of Wα and epα the center of f
Wα.
Let Uα, respectively Vα, be the geodesic ball of radius ϵ
4, respectively ϵ
2, centered
at pα, and let eUα and eVα be the corresponding balls centered at epα in f
Wα. We may
assume that the family of balls {Uα}1≤α≤s still covers O.
For each α and each nonnegative integer m, we deﬁne eH(m)
α
: R∗
+ × f
Wα × f
Wα
by
eH(m)
α
(t, ex, ey) = (4πt)−n/2e−d(ex,ey)2/4t(u0(ex, ey) + · · · + tmum(ex, ey))
where the ui are the invariants in (3.5). Since each γ ∈Gα is an isometry of f
Wα,
we have ui(γex, γey) = ui(ex, ey) for all ex, ey ∈f
Wα. It follows that the function
(t, ex, ey) 7→
X
γ∈Gα
eH(m)
α
(t, ex, γey)
is Gα-invariant in both ex and ey and thus descends to a well-deﬁned function, which
we denote by H(m)
α
, on R∗
+ × Wα × Wα.
Let ψα : O →R be a C∞cut-off function, which is identically one on Vα and
is supported in Wα. Let {ηα : α = 1, . . . , s} be a partition of unity on O with the
support of ηα contained in Uα. Deﬁne H(m) : R∗
+ × O × O →R by
(3.9)
H(m)(t, x, y) =
s
X
α=1
ψα(x)ηα(y)H(m)
α
(t, x, y).
We will show that H(m) is a parametrix for the heat kernel on O when m > n
2 .
3.10. LEMMA. H(m) ∈C∞(R∗
+ × O × O).
Lemma 3.10 is immediate.
3.11. LEMMA. Let l be a nonnegative integer. Then
(i)
  ∂
∂t + ∆x

H(m)(t, x, y) extends to a function in Cl(R+ ×O ×O) if m >
n
2 + 2l. (It is moreover of class C2l in the last two variables.)
(ii) For any given T > 0 and for each m > n
2 , there exists a constant A such
that |
  ∂
∂t + ∆x

H(m)(t, x, y)| < Atm−n
2 when 0 < t < T.

12
DRYDEN, GORDON, GREENWALD, AND WEBB
Proof. (i) Let l ≥0 and suppose m >
n
2 + 2l. By Remark 3.7, the function

∂
∂t + e∆ex

eH(m)
α
(t, ex, ey) on R∗
+ × f
Wα × f
Wα extends to Cl(R+ × f
Wα × f
Wα).
(Here, we are using the notation e∆for the Laplacian on f
Wα for all choices of α.)
Thus the same is true for P
γ∈Gα

∂
∂t + e∆ex

eH(m)
α
(t, ex, γey), and hence it follows
that
  ∂
∂t + ∆x

H(m)
α
(t, x, y) extends to Cl(R+ × Wα × Wα).
Now consider the function
fα(t, x, y) :=
 ∂
∂t + ∆x

(ψα(x)ηα(y)H(m)
α
(t, x, y)).
Noting that ψα and ηα are compactly supported inside Wα, we may view fα as a
function on R∗
+ × O × O which is zero whenever x or y lies outside of Wα. We
show fα extends to Cl(R+ ×O ×O). Since ψα ≡1 on Vα, it follows immediately
from the previous paragraph that fα extends to Cl(R+ × Vα × O). Moreover
fα ≡0 on R∗
+ × O × (O \ Uα) and so fα also extends smoothly (to zero) on
R+ × O × (O \ Uα). Finally for (x, y) ∈(O \ Vα) × Uα, we have d(x, y) ≥ϵ
4.
Thus, as t →0+, fα(t, x, y) and all its derivatives converge to zero uniformly for
(x, y) ∈(O \ Vα) × Uα. Thus H(m) extends to a function in Cl(R+ × O × O).
The parenthetical statement in (1) similarly follows from Remark 3.7.
(ii) The ui are constructed so that
 ∂
∂t + e∆ex

eH(m)
α
(t, ex, ey) = (4πt)−n/2e−d(ex,ey)2/4ttm e∆exum(t, ex, ey)
(see [2]). Since the ui are C∞functions, it follows that there exists a constant Bα
such that
 ∂
∂t + e∆ex

eH(m)
α
(t, ex, ey) < Bαtm−n
2
on (0, T] × f
Wα × f
Wα. Consequently,
 ∂
∂t + ∆x

H(m)
α
(t, x, y) < |Gα|Bαtm−n
2
on (0, T] × Wα × Wα and
 ∂
∂t + ∆x

(ψα(x)ηα(y)H(m)
α
(t, x, y)) < |Gα|Bαtm−n
2
on (0, T]×Vα×O, since ψα ≡1 on Vα. Once again, for x outside of Vα and y in the
support of ηα, we have d(x, y) ≥ϵ
4, and thus
  ∂
∂t + ∆x

(ψα(x)ηα(y)H(m)
α
(t, x, y))
can be bounded in terms of any power of t on (0, T) × (O \ Vα) × O.
Statement (ii) now follows from (3.9).
□
3.12. REMARK. When m > n
2 +2l, one obtains bounds on the partial derivatives of
order at most l of
  ∂
∂t + ∆x

H(m)(t, x, y) by an argument analogous to that used
in the proof of Lemma 3.11(ii).

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
13
3.13. LEMMA. Let m be any nonnegative integer. For f ∈C∞(O) and x ∈O, we
have
lim
t→0+
Z
O
H(m)(t, x, y)f(y)dy = f(x).
I.e., limt→0+ H(m)(t, x, y) = δx(y). Moreover, if N is a topological space and f
is a continuous function on N × O, then the convergence of
R
O H(m)(t, x, y)f(p, y)dy to f(p, x) is locally uniform on N × O.
Proof. Let eψα and eηα be the lifts of ψα and ηα to f
Wα.
Since supp(ηα) ⊂Uα ⊂Wα, we have
(3.14)
Z
O
ψα(x)ηα(y)H(m)
α
(t, x, y)f(p, y) dy
= ψα(x)
|Gα|
X
γ∈Gα
Z
f
Wα
eH(m)
α
(t, ex, γey)eηα(ey) efα(p, ey)dey
where efα is a lift of f|N×Wα to N × f
Wα and ex is an arbitrarily chosen point in the
preimage of x under the map f
Wα →Wα.
We change variables in each of the integrals in the right side of (3.14), letting
eu = γ(ey). Since γ is an isometry and since eηα and efα(p, ·) are γ-invariant, each
integral in the summand is equal to
(3.15)
Z
f
Wα
eH(m)
α
(t, ex, eu)eηα(eu) efα(p, eu) deu.
As t →0+, the integral (3.15) above converges to eηα(ex) efα(p, ex) = ηα(x)f(p, x)
(see Remark 3.7). Moreover, this convergence is locally uniform on N × f
Wα (see
[2]). Noting that ψα ≡1 on the support of ηα, it follows that both sides of (3.14)
converge to ηα(x)f(p, x) as t →0+, and the convergence is locally uniform on
N × Wα. Since both sides of (3.14) are identically zero when x lies outside of
supp(ψα) ⊂Wα, we thus have locally uniform convergence to ηα(x)f(p, x) on all
of N × O.
Finally it follows from (3.9) that
lim
t→0+
Z
O
H(m)(t, x, y)f(p, y) dy =
X
α
ηα(x)f(p, x) = f(p, x)
locally uniformly.
□
3.16. PROPOSITION. H(m) is a parametrix for the heat operator on O if m > n
2 .
Proof. Immediate from Lemmas 3.10, 3.11(i), and 3.13.
□
The construction of the heat kernel from the parametrix H(m) follows exactly
as in [2]. We give only a brief summary.

14
DRYDEN, GORDON, GREENWALD, AND WEBB
3.17. NOTATION. For A, B ∈C0(R+ × O × O), deﬁne the convolution A ∗B ∈
C0(R∗
+ × O × O) by
A ∗B(t, x, z) =
Z t
0
dθ
Z
O
A(t −θ, x, y)B(θ, y, z)dy.
Note that the convolution operator ∗is associative.
3.18. LEMMA. Let l be any nonnegative integer, and let m >
n
2 + 2l. Deﬁne
Fm(t, x, y) =
  ∂
∂t + ∆x

H(m)(t, x, y). (See Lemma 3.11 for regularity properties
of Fm.) Then for each T > 0, the series P∞
j=1 (−1)j+1F ∗j
m (t, x, y) converges
uniformly on [0, T]×O×O. Let Qm : R+ ×O×O →R be the sum of this series.
Then Qm ∈Cl(R+ × O × O). Moreover, for any T > 0, there exists a constant C
such that
|Qm(t, x, y)| ≤Ctm−n
2
on [0, T] × O × O.
The proof of Lemma 3.18 is identical to that of Lemma E.III.6 of [2] and uses
only Lemma 3.11(ii) and Remark 3.12.
3.19. LEMMA. Let m > n
2 . For P ∈C0(R+ × O × O), the function H(m) ∗P,
deﬁned formally by the expression in Notation 3.17, exists and is in C0(R∗
+ × O ×
O). Moreover, if m > n
2 +l, then H(m)∗P is of class Cl in the second variable. For
m > n
2 +2,
  ∂
∂t + ∆x

(H(m)∗P(t, x, y)) exists and equals (P+H(m)∗P)(t, x, y).
Again the proof is identical to that of Lemma E.III.7 of [2] and is based on
Lemma 3.13.
Using Lemmas 3.18 and 3.19, we obtain as in Proposition E.III.8 of [2] that:
3.20. PROPOSITION. Let m >
n
2 + 2 and deﬁne Qm as in Lemma 3.18. Then
K := H(m) −H(m) ∗Qm is a fundamental solution of the heat equation on O.
Note that uniqueness of the heat kernel implies that H(m) −H(m) ∗Qm is
independent of the choice of m > n
2 + 2.
3.21. NOTATION. Let
eHα(t, ex, ey) =
X
γ∈Gα
(4πt)−n/2e−d(ex,γ(ey))2/4t(u0(ex, γ(ey)) + tu1(ex, γ(ey)) + . . . ).
Observe that eHα is Gα-invariant in both ex and ey and thus descends to a well-
deﬁned function, which we denote by Hα, on R∗
+ × Wα × Wα.
3.22. THEOREM. In the notation of Proposition 3.1 and 3.21, the trace of the heat
kernel has an asymptotic expansion as t →0+ given by
∞
X
j=1
e−λjt ∼t→0+
s
X
α=1
Z
O
ηα(x)Hα(t, x, x) dx.

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
15
Proof. By Corollary 3.3 and Proposition 3.20, we have
∞
X
j=1
e−λjt =
Z
O
(H(m) −H(m) ∗Qm)(t, x, x)dx
for m > n
2 +2. By Lemma 3.18 and the fact that (4πt)
n
2 H(m)(t, x, x) is uniformly
bounded for (t, x) ∈(0, T] × O for any given T > 0, it follows that
(3.23)
∞
X
j=1
e−λjt =
Z
O
H(m)(t, x, x)dx + O(tm−n)
on any interval (0, T]. (Aside: When O is a manifold, then
R
O H(m)(t, x, x)dx =
(4πt)−n
2 (a0 + a1t + · · · + amtm). For general orbifolds, the arguments in the
next section will show that
R
O H(m)(t, x, x)dx is of the form (4πt)−n
2 P2m
j=0 cjt
j
2 .
Thus the error term can be improved to O(tm−n−1
2 ) since
R
O H(m)(t, x, x)dx =
R
O H(m+n)(t, x, x)dx + O(tm−n−1
2 ).)
Since ψα is identically one on the support of ηα, Notation 3.8 yields
(3.24)
H(m)(t, x, x) =
X
α
ηα(x)H(m)
α
(t, x, x).
Substituting (3.24) into (3.23), we obtain the theorem.
□
4. COMPUTATION OF THE HEAT ASYMPTOTICS
4.1. NOTATION AND REMARKS. Let γ be an isometry of a Riemannian manifold
M and let Ω(γ) denote the set of components of the ﬁxed point set of γ. Each
element of Ω(γ) is a submanifold of M. For each non-negative integer k, Donnelly
[10] deﬁned a real-valued function, which we temporarily denote bk((M, γ), ·), on
the ﬁxed point set of γ. For each W ∈Ω(γ), the restriction of bk((M, γ), ·) to W
is smooth. Two key properties of the bk are:
• (Locality) For a ∈W, bk((M, γ), a) depends only on the germs at a of
the Riemannian metric of M and of the isometry γ. In particular, if U is a
γ-invariant neighborhood of a in M, then bk((M, γ), a) = bk((U, γ), a).
• (Universality) If M and M′ are Riemannian manifolds admitting isome-
tries γ and γ′, respectively, and if σ : M →M′ is an isometry satisfying
σ◦γ = γ′◦σ, then bk((M, γ), x) = bk((M′, γ′), σ(x)) for all x ∈Fix(γ).
In view of the locality property, we will usually delete the explicit reference to
M and rewrite these functions as bk(γ, ·), as they are written in [10].
4.2. COMPUTATION OF THE bk. [10]
In the notation of 4.1, let W ∈Ω(γ), and let n = dim(M) and m = dim(W).
For x ∈W, the orthogonal complement Tx(W)⊥of Tx(W) in the tangent space
Tx(M) is invariant under γ∗. Deﬁne Aγ(x) = γ∗: Tx(W)⊥→Tx(W)⊥, and
observe that Aγ(x) is nonsingular. Set
Bγ(x) = (I −Aγ(x))−1.

16
DRYDEN, GORDON, GREENWALD, AND WEBB
Donnelly showed that
bk(γ, x) = | det(Bγ(x))|ebk(γ, x),
where ebk(γ, ·) is an O(m) × O(n −m) universal invariant polynomial in the com-
ponents of Bγ and in the curvature tensor R of M and its covariant derivatives.
Explicit formulae for b0 and b1 are given in [10, Thm. 5.1] using the following
indexing conventions: 1 ≤α, β ≤m, m + 1 ≤i, j, k ≤n and 1 ≤a, b, c ≤n.
At each point x ∈W, choose an orthonormal basis {e1, . . . , en} of Tx(M) so that
the ﬁrst m vectors are tangent to W. The sign convention on the curvature tensor
R of M is chosen so that Rabab is the sectional curvature of the plane spanned by
ea and eb. Set
τ =
n
X
a,b=1
Rabab
and
ρab =
n
X
c=1
Racbc.
Thus τ is the scalar curvature and ρ the Ricci tensor of M. Then
(4.3)
b0(γ, x) = | det(Bγ(x))|
and, summing over repeated indices,
(4.4)
b1(γ, x) = | det(Bγ(x))|(1
6τ + 1
6ρkk + 1
3RikshBkiBhs
+1
3RikthBktBhi −RkahaBksBhs).
4.5. NOTATION. Let O be an orbifold and let (eU, GU, πU) be an orbifold chart.
In the notation of 2.12 and 2.14, let e
N be a eU-stratum and let γ ∈Isomax( e
N).
Then e
N is an open subset of a component of Fix(γ) and thus by 4.1, bk(γ, ·)
(= bk((eU, γ), ·)) is smooth on e
N for each nonnegative integer k. Deﬁne a function
bk( e
N, ·) on e
N by
bk( e
N, x) =
X
γ∈Isomax( e
N)
bk(γ, x).
4.6. LEMMA. Let O be a Riemannian orbifold, let N be an O-stratum and let p ∈
N. Let (eU, GU, πU) and (eU′, GU′, πU′) be two orbifold charts with p ∈U ∩U′.
Let ˜p ∈eU and ˜p′ ∈eU′ with πU(˜p) = p = πU′(˜p′), and let e
N, respectively e
N′, be
the eU-stratum through ˜p, respectively eU′-stratum through ˜p′. Then for each k, we
have bk( e
N, ˜p) = bk( e
N′, ˜p′).
Proof. By Deﬁnition 2.1, it sufﬁces to consider the case that one chart embeds
in the other, say λ : (eU, GU, πU) →(eU′, GU′, πU′) is an isometric embedding
with λ(˜p) = ˜p′. The associated homomorphism τ : GU →GU′ carries IsoGU (˜p)
isomorphically onto IsoGU′(˜p′) and Isomax(˜p) to Isomax(˜p′). The eU-stratum e
N is

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
17
carried to an open subset of the eU′-stratum e
N′. The lemma is thus an immediate
consequence of the universality of the bk, as discussed in 4.1.
□
4.7. DEFINITION. Let O be a Riemannian orbifold and let N be an O-stratum.
(i) For each non-negative integer k, deﬁne a real-valued function bk(N, ·) by
setting bk(N, p) = bk( e
N, ˜p) where (eU, GU, πU) is any orbifold chart about p,
˜p ∈π−1
U (p) and e
N is the eU-stratum through ˜p. By Lemma 4.6, the function
bk(N, ·) is well-deﬁned.
(ii) The Riemannian metric on O induces a Riemannian metric, and thus a vol-
ume element, on the manifold N. Set
IN := (4πt)−dim(N)/2
∞
X
k=0
tk
Z
N
bk(N, x)d volN(x)
where d volN is the Riemannian volume element.
(iii) Also set
I0 = (4πt)−dim(O)/2
∞
X
k=0
ak(O)tk
where the ak(O) (which we will usually write simply as ak) are the familiar heat
invariants. More precisely, the invariants ui in (3.5), which are deﬁned in terms
of the curvature and its covariant derivatives on any Riemannian manifold, also
make sense on any Riemannian orbifold. The invariants ak(O) are given by ak =
R
O uk(x, x)d volO(x). In particular, a0 = vol(O), a1 = 1
6
R
O τ(x)d volO(x), etc.
Note that if O is ﬁnitely covered by a Riemannian manifold M, say O = G\M,
then ak(O) =
1
|G|ak(M).
4.8. THEOREM. Let O be a Riemannian orbifold and let λ1 ≤λ2 ≤. . . be the
spectrum of the associated Laplacian acting on smooth functions on O. The heat
trace P∞
j=1 e−λjt of O is asymptotic as t →0+ to
I0 +
X
N∈S(O)
IN
|Iso(N)|
where S(O) is the set of all O-strata and where |Iso(N)| is the order of the isotropy
at each p ∈N as deﬁned in Remark 2.7. This asymptotic expansion is of the form
(4.9)
(4πt)−dim(O)/2
∞
X
j=0
cjt
j
2
for some constants cj.
4.10. REMARK. Suppose O = G\M is a good closed orbifold. Note that M may
be noncompact and G may be an inﬁnite group, although the isotropy group at any
point of M must be a ﬁnite subgroup of G. In this setting, Donnelly [11] proved
the existence and uniqueness of the heat kernel KM on M and of an asymptotic
expansion for KM. He then obtained an asymptotic expansion for the heat trace on
O. Theorem 4.8, in the case of good orbifolds, organizes the information in [11] in
a way that clariﬁes the contribution of each O-stratum to the asymptotics.

18
DRYDEN, GORDON, GREENWALD, AND WEBB
The expression for the heat asymptotics of good orbifolds in [11] differs from
that in (4.9) in that the half powers are missing. However, the absence of these
powers is apparently a typographical error in transcribing a result of Donnelly’s
earlier paper [10], stated below as Proposition 4.11.
K. Richardson [24] obtained an asymptotic expansion for the heat trace associ-
ated with the basic Laplacian on a Riemannian foliation. Also referring to Don-
nelly’s work on good orbifolds, he showed that the expansion is of the form given
in (4.9).
The remainder of this section is devoted to the proof of Theorem 4.8.
4.11. PROPOSITION. [10]. Let M be a closed Riemannian manifold, let K(t, x, y)
be the heat kernel of M, and let γ be a nontrivial isometry of M. Then, in the
notation of 4.1,
R
M K(t, x, γ(x))d volM(x) is asymptotic as t →0+ to
X
W∈Ω(γ)
(4πt)−dim(W )
2
∞
X
k=0
tk
Z
W
bk(γ, a)d volW (a)
where d volW is the volume form on W deﬁned by the Riemannian metric induced
from M.
4.12. PROOF OF THEOREM 4.8 IN SPECIAL CASE. We prove Theorem 4.8 for O =
G\M a good closed orbifold with G ﬁnite (and thus M compact). In particular,
(M, G, π) is a global orbifold chart where π : M →O is the projection. In this
case, the theorem is an easy consequence of Proposition 4.11. Indeed, letting K
denote the heat kernel of M and letting π : M →O be the projection, then the
heat kernel KO of O is given by
KO(t, x, y) =
X
γ∈G
K(t, ex, γ(ey))
where ex, respectively ey, are any elements of π−1(x), respectively π−1(y). Thus
Z
O
KO(t, x, x)d volO(x) =
1
|G|
X
γ∈G
Z
M
K(t, ex, γ(ex))d volM(ex),
so Proposition 4.11 implies that
(4.13)
Z
O
KO(t, x, x)d volO(x) ∼t→0+
1
|G|
Z
M
K(t, ex, ex)d volM(ex)
+ 1
|G|
X
1̸=γ∈G
X
W∈Ω(γ)
(4πt)−dim(W )
2
∞
X
k=0
tk
Z
W
bk(γ, a)d volW (a).
The ﬁrst term on the right-hand-side of (4.13) is given by
(4.14)
1
|G|
Z
M
K(t, ex, ex)d volM(ex) =
1
|G|(4πt)−dim(M)
2
∞
X
k=0
ak(M)tk = I0.
(See the ﬁnal comment in Deﬁnition 4.7(iii).)

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
19
Next let 1 ̸= γ ∈G, let W ∈Ω(γ), and let e
N be an M-stratum contained in
W. Then either e
N has measure zero in W (in which case γ /∈Isomax( e
N)) or else
e
N is open in W and γ ∈Isomax( e
N). Thus by replacing the integral over W with
the integrals over the M-strata that are open in W, reordering the summations in
(4.13), and taking note of (4.14), we obtain
(4.15)
Z
O
KO(t, x, x)d volO(x) ∼t→0+ I0 + 1
|G|
X
e
N∈eS(M)
eI e
N
where eS(M) denotes the set of all M-strata and where
eI e
N = (4πt)−dim( e
N)
2
∞
X
k=0
tk
Z
e
N
bk( e
N, a)d vol e
N(a).
Let N be an O-stratum. Then π−1(N) is a union of ﬁnitely many mutually
isometric M-stratum e
N1, . . . , e
Nk and π : π−1(N) →N is a covering map of
degree
|G|
|Iso(N)|. We have
eI e
N1 + · · · + eI e
Nk =
|G|
|Iso(N)|IN
and thus Theorem 4.8, in the case of orbifolds ﬁnitely covered by manifolds, fol-
lows from (4.15).
The proof in the general case will apply the argument in 4.12 to orbifold charts
and then piece the computations together via a partition of unity. We ﬁrst generalize
Proposition 4.11 slightly. The manifolds in the two lemmas below do not have
boundaries but could, for example, be bounded domains in a larger manifold.
4.16. LEMMA. We use the notation of 4.1. Let M be an n-dimensional Riemannian
manifold (without boundary) of ﬁnite volume and let γ : M →M be a nontrivial
isometry. Assume that the distance d(ex, γ(ex)) remains bounded away from zero off
arbitrarily small tubular neighborhoods of the ﬁxed point set of γ and that each
component of the ﬁxed point set of γ has ﬁnite volume. Then as t →0+,
Z
M
(4πt)−n/2e−d(ex,γ(ex))2/4t(u0(ex, γ(ex)) + tu1(ex, γ(ex)) + . . . ) dex
∼
X
W∈Ω(γ)
(4πt)−dim(W)/2
∞
X
k=0
tk
Z
W
bk(γ, ex)d volW (ex)
This result is proven in Donnelly [10, Thm. 4.1], in case M is closed. In that
case, of course, the hypotheses on the distance function and on the ﬁxed point set
of γ are automatic, and the lemma is a restatement of Proposition 4.11. The proof
goes through verbatim in the more general setting of Lemma 4.16.
4.17. LEMMA. With the notation and hypotheses of the previous lemma, let eη be a
smooth bounded γ-invariant function on M. Then there exists a family of functions

20
DRYDEN, GORDON, GREENWALD, AND WEBB
ck(γ, eη, ·), k = 0, 1, 2, . . . , deﬁned on the ﬁxed point set of γ and smooth on each
component W ∈Ω(γ), such that as t →0+,
Z
M
eη(ex)(4πt)−n/2e−d(ex,γ(ex))2/4t(u0(ex, γ(ex)) + tu1(ex, γ(ex)) + . . . ) dex
∼
X
W∈Ω(γ)
(4πt)−dim(W)/2
∞
X
k=0
tk
Z
W
ck(γ, eη, ex)d volW (ex).
Moreover, ck(γ, eη, ·) satisﬁes the following:
(i) (Locality) ck(γ, eη, ex) depends only on the germs of γ, eη, and the Riemann-
ian metric of M at ex ∈W;
(ii) ck(γ, eη, ·) is zero off supp(eη) ∩W;
(iii) the dependence of ck(γ, eη, ·) on eη is linear;
(iv) ck(γ, 1, ·) = bk(γ, ·) where 1 denotes the constant function eη ≡1;
(v) (Universality) if M′ is another Riemannian manifold, γ′ is an isometry
of M′ and σ : M →M′ is an isometry satisfying σ ◦γ = γ′ ◦σ, then
ck(γ′, eη ◦σ−1, σ(ex)) = ck(γ, eη, ex) for all ex in the ﬁxed point set of γ.
The proof requires only minor changes in the proof of Theorem 4.1 of [10]. In
the proof of that theorem, the functions bk(γ, ·) are expressed as linear combina-
tions of certain derivatives of explicitly deﬁned functions hj, j = 0, . . . , k. To
obtain the functions ck(γ, eη, ·), one replaces the functions hj by the functions eηhj.
4.18. NOTATION AND REMARKS. Let O be a closed orbifold and consider the
charts eUα, eVα, f
Wα and partition of unity {ηα} given in Notation 3.8. Let eVα play
the role of M in Lemmas 4.16 and 4.17, and let eηα = ηα ◦πα play the role of
eη. Since eVα has compact closure inside the larger Riemannian manifold f
Wα on
which Gα acts by isometries and since the ﬁxed point set of γ in f
Wα is connected
(in fact, it is the union of a collection of geodesics radiating from the center point
˜pα), one easily veriﬁes for each γ ∈Gα that the hypothesis concerning the distance
function in the two lemmas holds.
(i) For each eVα-stratum e
N, deﬁne a smooth function ck,α( e
N, ·) on e
N by
ck,α( e
N, ex) =
X
γ∈Isomax( e
N)
ck(γ, eηα, ex).
(ii) Let N be an O-stratum. For each non-negative integer k and each α =
1, . . . , s, deﬁne a continuous (in fact, smooth) function ck,α(N, ·) on N
as follows: First for x ∈N ∩Vα, set ck,α(N, x) = ck( e
N, ex) where
ex is any element of π−1
α (x) and e
N is the eVα-stratum through ex. By an
argument analogous to that of Lemma 4.6. this deﬁnition is independent
of the choice of ex in π−1
α (x). Since eηα is supported in eUα, Lemma 4.17(ii)
implies that ck,α(N, ·) is zero off N ∩Uα and thus extends to a continuous
function on N which is zero off N ∩Uα.

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
21
(iii) Set
IN,α := (4πt)−dim(N)/2
∞
X
k=0
tk
Z
N
ck,α(N, x)d volN(x).
4.19. LEMMA. Let O be a closed Riemannian orbifold and let N be an O-stratum.
Then for each non-negative integer k, we have
s
X
α=1
ck,α(N, ·) = bk(N, ·)
and
s
X
α=1
IN,α = IN.
Proof. Let x ∈N, and let α1, · · · , αr be those α ∈{1, . . . , s} for which x ∈Vαi.
Then we can ﬁnd a coordinate chart (eU, GU, πU) such that U ⊂Vα1 ∩· · · ∩Vαr
and such that the chart (eU, GU, πU) embeds in each of the charts (eVα, Gα, πα). Let
λi : eU →eVαi be the embedding. Let ex ∈π−1
U (x), let e
N be the eU-stratum through
ex, and let exi = λi(ex). As in the proof of Lemma 4.6, λi( e
N) is an open subset of
the eVαi-stratum e
Ni through exi. Using the universality property (v) of Lemma 4.17,
Notation 4.18, and an argument analogous to that of Lemma 4.6, we see that
ck,αi(N, x) := ck,αi( e
Ni, exi) =
X
γ∈Isomax( e
N)
ck(γ, ηαi ◦πU, ex).
Thus, since ck,α(N, x) = 0 when α is not one of α1, . . . , αr, we have
(4.20)
s
X
α=1
ck,α(N, x) =
X
γ∈Isomax( e
N)
r
X
i=1
ck(γ, ηαi ◦πU, ex).
From properties (iii) and (iv) of Lemma 4.17 and the fact that
r
X
i=1
ηαi ≡1 on U,
we see that
(4.21)
r
X
i=1
ck(γ, ηαi ◦πU, ex) = bk(γ, ex)
on e
N. By Deﬁnition 4.7,
X
γ∈Isomax( e
N)
bk(γ, ex) = bk(N, x)
and thus the ﬁrst equation in the lemma follows from (4.20) and (4.21). The second
equation is then immediate.
□
We now prove Theorem 4.8.

22
DRYDEN, GORDON, GREENWALD, AND WEBB
Proof. Let n = dim(O). By Theorem 3.22 and the fact that the support of ηα is
contained in Vα, we have
(4.22)
∞
X
j=1
e−λjt ∼t→0+
s
X
α=1
Z
Vα
ηα(x)Hα(t, x, x)d vol(O)
where Hα(t, x, x) is deﬁned in Notation 3.21. By Notation 3.21,
(4.23)
s
X
α=1
Z
Vα
ηα(x)Hα(t, x, x) d volO(x) =
s
X
α=1
1
|Gα|
Z
eVα
eηα(ex)(4πt)−n
2 (u0(ex, ex) + tu1(ex, ex) + . . . ) d voleVα(ex)
+
s
X
α=1
1
|Gα|
X
1̸=γ∈Gα
Z
eVα
eηα(ex)(4πt)−n/2e−d(ex,γ(ex))2/4t(u0(ex, γ(ex))
+ tu1(ex, γ(ex)) + . . . ) d voleVα(ex)
where eηα = ηα ◦πα.
Consider the ﬁrst sum on the right-hand-side of (4.23). Since ηα is supported in
Vα, we have
(4.24)
s
X
α=1
1
|Gα|(4πt)−n
2
Z
eVα
eηα(ex)(u0(ex, ex) + tu1(ex, ex) + . . . ) d voleVα(ex)
=
s
X
α=1
(4πt)−n
2
Z
O
ηα(x)(u0(x, x) + tu1(x, x) + . . . )d volO(x)
= (4πt)−n
2
Z
O
(u0(x, x) + tu1(x, x) + . . . )d volO(x) = I0.
Next by Lemma 4.17 and the remarks in 4.18, we have for each 1 ̸= γ ∈Gα,
(4.25)
1
|Gα|
X
1̸=γ∈ga
Z
eVα
eηα(ex)(4πt)−n/2e−d(ex,γ(ex))2/4t(u0(ex, γ(ex))+
tu1(ex, γ(ex)) + . . . ) d voleVα(ex)
∼
1
|Gα|
X
1̸=γ∈Gα
X
W∈Ω(γ)
(4πt)−dim(W)/2
∞
X
k=0
tk
Z
W
ck(γ, eηα, ex)d volW (ex).
By 4.18 and an argument identical to that in 4.12, the right-hand-side of (4.25)
is equal to
X
N∈S(O)
1
|Iso(N)|IN,α.
Consequently, Lemma 4.19 and (4.25) imply that the second sum in the right-hand-
side of (4.23) is equal to
X
N∈S(O)
1
|Iso(N)|IN.

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
23
Thus in view of (4.22), (4.23), and (4.24), the theorem is proved.
□
5. APPLICATIONS
5.1. THEOREM. Let O be a Riemannian orbifold with singularities. If O is even di-
mensional (respectively, odd dimensional) and some O-stratum of the singular set
is odd dimensional (respectively, even dimensional), then O cannot be isospectral
to a Riemannian manifold.
Proof. It is clear from (4.3) that if N is any O-stratum of the singular set, then
the function b0(γ, ·) is strictly positive on N for each γ ∈Isomax(N). Thus, in
the two cases, the fact that O is an orbifold can be gleaned from the presence of
half-integer powers, respectively integer powers, of t in the asymptotic expansion
in Theorem 4.8.
□
5.2. REMARK. In [18] this theorem was stated for good orbifolds, but here we also
include bad orbifolds.
We now restrict our attention to closed two-dimensional orbifolds (2-orbifolds).
The singularities which may occur in 2-orbifolds are cone points, dihedral corner
reﬂectors, and mirror reﬂectors. Recall that dihedral corner reﬂectors and mirror
reﬂectors both appeared in Example 2.15. A cone point p of order n is an isolated
singularity; an orbifold chart for a neighborhood of p is (D2, Zn, π) where D2 is an
open 2-disk in R2 and Zn is the cyclic group of order n. The Euler characteristic
of a 2-orbifold is 2 minus the sum of the related values: each cone point of order
n has value n−1
n ; each dihedral corner reﬂector has value n−1
2n ; each handle has
value 2; each cross-cap has value 1; and each mirror reﬂector has value 1. Every
good 2-orbifold admits a (metrically) spherical, Euclidean or hyperbolic structure
depending on whether the Euler characteristic is positive, zero or negative, respec-
tively [30]. In addition, all bad 2-orbifolds have positive Euler characteristic.
5.3. EXAMPLE. Let O be a 2-orbifold and let p be a cone point of order m. If
N = {p}, then Iso(N) is a cyclic group of order m and Isomax(N) contains all of
the nontrivial elements. Letting γ be the generator, then for j = 1, . . . , m −1 we
have that
Aγj = γj
∗=

cos( 2jπ
m )
−sin(2jπ
m )
sin(2jπ
m )
cos( 2jπ
m )

,
where Aγj is as deﬁned in 4.2. Thus
b0(γj) = |det((I −Aγj)−1)| =
1
2 −2 cos( 2jπ
m )
=
1
4 sin2(jπ
m )
.
(We are writing b0(γj) rather than using the function notation b0(γj, ·) since N
consists of a single point.)
5.4. LEMMA.
m−1
X
j=1
1
sin2(jπ
m )
= m2 −1
3
.

24
DRYDEN, GORDON, GREENWALD, AND WEBB
Proof. A well-known formula (see, for example, [23, Example 7.9.1]), proven by
the calculus of residues, states that
π2
sin2(πz) =
∞
X
k=−∞
1
(k −z)2 .
Thus
m−1
X
j=1
1
sin2(jπ
m )
= m2
π2
m−1
X
j=1
∞
X
k=−∞
1
(mk −j)2 .
Since
m−1
X
j=1
∞
X
k=−∞
1
(mk −j)2 = 2
∞
X
n=1
1
n2 −2
∞
X
n=1
1
m2n2
and P∞
n=1
1
n2 = π2
6 , the lemma follows.
□
5.5. PROPOSITION. Let O be a 2-orbifold, let p be a cone point in O of order m
and let N = {p}. Then in the notation of Theorem 4.8, we have
IN = m2 −1
12
+ O(t).
Proof. By 4.7(ii) and 5.3,
IN =
m−1
X
j=1
1
4 sin2(jπ
m )
+ O(t).
Thus Proposition 5.5 follows from Lemma 5.4.
□
5.6. EXAMPLE. Calculating heat invariants for 2-orbifolds.
Degree zero term for orientable 2-orbifolds. An orientable 2-orbifold O can
have only isolated singularities, i.e., cone points. Suppose O has k cone points of
orders m1, . . . , mk. In the notation of 4.7(iii),
I0 = 1
4π(a0t−1 + a1 + O(t)).
Thus by Theorem 4.8 and Proposition 5.5, the term of degree zero in the asymptotic
expansion in Theorem 4.8 is given by
a1
4π +
k
X
i=1
1
mi
m2
i −1
12
.
By the Gauss-Bonnet Theorem (valid also for orbifolds; see [26, 30]), we have
a1 = 2π
3 χ(O).
Hence the degree zero term is
(5.7)
χ(O)
6
+
k
X
i=1
m2
i −1
12mi
.

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
25
Degree zero term for nonorientable 2-orbifolds. For a 2-orbifold O, the di-
mension zero singular locus is the only portion which contributes to the degree
zero term of the asymptotic expansion in Theorem 4.8, aside from the a1
4π = χ(O)
6
component. A nonorientable 2-orbifold O can have cone points and/or dihedral
corner reﬂector points that contribute in the following ways. As in the computation
of the degree zero term for orientable 2-orbifolds, here a simple cone point of order
m contibutes 1
m
m2−1
12 . Let N = {p}, where p is a corner reﬂector point created by
a rotation of order n and a reﬂection. Then |Iso(N)| = 2n. By Notation 2.14(ii),
Isomax(N) contains only the nontrivial elements of the rotation group, since the
reﬂection ﬁxes one-dimensional strata of the mirror locus, a higher dimensional
stratum of the singular set. Hence the computations in Example 5.3 and Proposi-
tion 5.5 remain the same, but the difference in |Iso(N)| is seen as an extra 1
2 factor
in Theorem 4.8. The point contributes
1
2n
n2−1
12
to the degree zero term.
Thus, for a 2-orbifold O with cone points p1, . . . , pk of orders m1, . . . , mk, and
dihedral corner reﬂector points q1, . . . , qr of orders n1, . . . , nr, the term of degree
0 in the asymptotic expansion of the heat trace is
(5.8)
χ(O)
6
+
k
X
i=1
1
mi
m2
i −1
12
+
r
X
j=1
1
2nj
n2
j −1
12
.
Degree one term for 2-orbifolds. Aside from a2, only dimension zero strata of
the singular set contribute to the t term of the asymptotic expansion in Theorem 4.8.
We ﬁrst note that the last term in (4.4) is zero; this follows from the summation
convention and the fact that our singular set is zero-dimensional. Using symmetry
properties of the curvature, we can further simplify (4.4) as
b1(γj) =
1
4 sin2(jπ
m )
τ
6 + ρkk
6 + 2
3(R1212(B2
21 + B2
12 −B12B21 −B22B11))

,
where R1212 is evaluated in the local covering manifold. By the deﬁnitions of
scalar and Ricci curvature, the preceding equation becomes
b1(γj) = R1212(1 + B2
21 + B2
12 −B12B21 −B22B11)
6 sin2(jπ
m )
.
In general, straightforward calculations show that
Bγj = (I −Aγj)−1 =


1
2
−
sin( 2jπ
m )
2−2 cos( 2jπ
m )
sin( 2jπ
m )
2−2 cos( 2jπ
m )
1
2


which implies
b1(γj) =
R1212
8 sin4(jπ
m )
,
for j = 1, . . . , m −1.
Thus, for a 2-orbifold O with cone points p1, . . . , pk of orders m1, . . . , mk, and
dihedral corner reﬂector points q1, . . . , qr of orders n1, . . . , nr, the coefﬁcient of

26
DRYDEN, GORDON, GREENWALD, AND WEBB
the term of degree 1 in the asymptotic expansion of the heat trace is
(5.9)
a2
4π +
k
X
i=1
1
mi


mi−1
X
j=1
R1212
8 sin4( jπ
mi )

+
r
X
i=1
1
2ni


ni−1
X
j=1
R1212
8 sin4(jπ
ni )

.
Recall that a2(O) =
1
360
R
O(2|R|2 −2|ρ|2 + 5τ 2)d volO(g), where R is the curva-
ture, ρ is the Ricci curvature, and τ is the scalar curvature of O (e.g. [2]).
We can further simplify (5.9) by making the substitution
mi−1
X
j=1
1
sin4( jπ
mi )
= m4
i + 10m2
i −11
45
.
See [3] and the references therein or [7, 16] for evaluations of this and similar ﬁnite
trigonometric sums.
With this substitution, (5.9) becomes
(5.10)
a2
4π +
k
X
i=1
R1212(m4
i + 10m2
i −11)
360mi
+
r
X
i=1
R1212(n4
i + 10n2
i −11)
720ni
.
Degree −1
2 term for 2-orbifolds. The only O-strata that contribute to the de-
gree
1
√
t term are those of codimension one in O. To obtain these O-strata, remove
any dihedral points from the mirror locus and then take the connected components
of the remaining set. Let x ∈N, an O-stratum of the mirror locus, and note that
γ ∈Isomax(N) must act as a reﬂection.
To compute b0(γ, x) = |det((I −Aγ)−1)|, notice that on the normal bundle to
N, γ∗= [−1], and so,
b0(γ, x) = |det((I −Aγ)−1)| = |[2]−1| = 1
2.
Applying 4.7(ii),
IN = (4πt)−1/2
X
γ∈Isomax(N)
∞
X
k=0
tk
Z
N
1
2d volN(x) + O(t)
= length(N)
4√π
1
√
t + O(
√
t).
We sum over all O-strata of the mirror locus to obtain the coefﬁcient of the
1
√
t term
in Theorem 4.8:
(5.11)
X
N
IN
|Iso(N)| =
X
N
1
2
length(N)
4√π
= length(MirrorLocus(O))
8√π
.
Degree 1
2 term for 2-orbifolds. For a 2-orbifold O, the dimension one singular
locus gives the sole contribution to the
√
t term of the asymptotic expansion in
Theorem 4.8.

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
27
We have
b1(γ, x)
=
|det(Bγ(x))|(τ
6 + ρkk
6 + 1
3RikshBkiBhs
+ 1
3RikthBktBhi −RkαhαBksBhs)(x)
where Bij denotes the i, j entry of Bγ(x), τ is the scalar curvature of M at x and
ρ is the Ricci curvature.
In the case of a 2-orbifold with a point x in its mirror locus (but not a dihedral
corner reﬂector point), the matrix Bγ(x) is one-dimensional, and thus the third and
fourth terms in the sum vanish. Since Bγ(x) = 1
2, the last term is −1
4R1212. We
also have ρkk = R1212, while τ = 2R1212. Thus b1(γ, x) = 1
2(1
4R1212)(x) =
1
8R1212(x) = 1
16τ(x). Thus for N a stratum in the mirror locus, the term of degree
1
2 in IN is given by
√
t
√
4π
Z
N
1
16τ(x)d volN(x) =
√
t
32√π
Z
N
τ(x)d volN(x).
The coefﬁcient of the degree 1
2 term in the asymptotic expansion for the heat trace
on O is thus
(5.12)
1
64√π
Z
MirrorLocus(O)
τ
where the scalar curvature is the scalar curvature of O computed at points in the
mirror locus and the integral is with respect to the induced Riemannian metric on
the one-dimensional mirror locus. See Table 1 for the asymptotic expansions of
the heat kernel for orbifolds O with χ(O) ≥0.
Our notation for orbifolds is adapted from Conway’s convention [9], with com-
mas added for readability. Namely O(a, b, ∗c, d) denotes an orbifold with simple
cone points of orders a and b, and dihedral corner reﬂectors of orders 2c and 2d. In
addition, O(n×) is a disk with a simple interior cone point and the edge identiﬁed
via the antipodal map, while O(n∗) is a disk with a simple interior cone point and
a mirror edge corresponding to a reﬂection. A detailed explanation of the orbifold
notation can be found in [9] and compared with pictures in [21, pages 80–90]. A
proof that these are all of the closed 2-orbifolds with χ(O) ≥0 and that the only
bad 2-orbifolds are O(m), O(∗m), O(m, n) and O(∗m, n) (when m > 1 and
m ̸= n), can be found in [30].
Let O be an orientable 2-orbifold with k cone points of orders m1, . . . , mk,
denoted O(m1, . . . , mk), and consider the quantity c deﬁned as 12 times the degree
zero term:
(5.13)
c = 2χ(O) +
k
X
i=1

mi −1
mi

.
This quantity is a spectral invariant; note that it depends only on the topology, not
on the Riemannian metric. For O(m1, . . . , mk), we denote by c(m1, . . . , mk) the
associated spectral invariant. We now investigate classes of orientable 2-orbifolds
for which c is a complete topological invariant. Although Theorem 5.14 is a special

28
DRYDEN, GORDON, GREENWALD, AND WEBB
TABLE 1. 2-orbifold expansions with χ(O) ≥0
O with χ(O) > 0
Asymptotic Expansion
O(m)
V 1
t + 1
12(2 + m + 1
m) + O(t)
O(∗m)
V 1
t + ML 1
√
t + 1
24(2 + m + 1
m) + O(
√
t)
O(m, n)
V 1
t + 1
12(m + n + 1
m + 1
n) + O(t)
O(∗m, n)
V 1
t + ML 1
√
t + 1
24(m + n + 1
m + 1
m) + O(
√
t)
O(m×)
V 1
t + 1
12(m + 1
m) + O(t)
O(m∗)
V 1
t + ML 1
√
t + 1
12(m + 1
m) + O(
√
t)
O(2, 2, m)
V 1
t + 1
12(3 + m + 1
m) + O(t)
O(∗2, 2, m), O(2, ∗m)
V 1
t + ML 1
√
t + 1
24(3 + m + 1
m) + O(
√
t)
O(2, 3, 3)
V 1
t + 43
72 + O(t)
O(∗2, 3, 3), O(3, ∗2)
V 1
t + ML 1
√
t + 43
144 + O(
√
t)
O(2, 3, 4)
V 1
t + 97
144 + O(t)
O(∗2, 3, 4)
V 1
t + ML 1
√
t + 97
288 + O(
√
t)
O(2, 3, 5)
V 1
t + 271
360 + O(t)
O(∗2, 3, 5)
V 1
t + ML 1
√
t + 271
720 + O(
√
t)
O with χ(O) = 0
Asymptotic Expansion
torus, Klein bottle
V 1
t + O(t)
*torus, *Klein bottle
V 1
t + ML 1
√
t + O(
√
t)
O(2, 2, 2, 2)
V 1
t + 1
2 + O(t)
O(∗2, 2, 2, 2), O(2, ∗2, 2),
O(2, 2∗)
V 1
t + ML 1
√
t + 1
4 + O(
√
t)
O(2, 2×)
V 1
t + 1
4 + O(t)
O(2, 4, 4)
V 1
t + 3
4 + O(t)
O(∗2, 4, 4), O(4, ∗2)
V 1
t + ML 1
√
t + 3
8 + O(
√
t)
O(3, 3, 3)
V 1
t + 2
3 + O(t)
O(∗3, 3, 3), O(3, ∗3)
V 1
t + ML 1
√
t + 1
3 + O(
√
t)
O(2, 3, 6)
V 1
t + 5
6 + O(t)
O(∗2, 3, 6)
V 1
t + ML 1
√
t + 5
12 + O(
√
t)
Here m, n ≥1, V = vol(O)
4π
and ML = length(MirrorLocus(O))
8√π
. Note that *torus is an annulus
with two mirror reﬂector edges and *Klein bottle is a M¨obius band with one mirror reﬂector edge.
case of Theorem 5.15, we begin with the more restricted class in order to give the
reader intuition for the proof techniques used.
5.14. THEOREM. Within the class of all footballs (good or bad) and all teardrops,
the spectral invariant c is a complete topological invariant. I.e., c determines
whether the orbifold is a football or teardrop and determines the orders of the
cone points.

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
29
TABLE 2. Triangular Pillow Orbifolds
O
χ(O)
c(O)
χ(O) > 0
O(2, 2, 2)
1
2
5 1
2
O(2, 2, m)
1
m
3 + m + 1
m
O(2, 3, 3)
1
6
7 1
6
O(2, 3, 4)
1
12
8 1
12
O(2, 3, 5)
1
30
9 1
30
χ(O) = 0
O(3, 3, 3)
0
8
O(2, 4, 4)
0
9
O(2, 3, 6)
0
10
χ(O) < 0
O(3, 3, 4)
−1
12
8 11
12
O(3, 4, 4)
−1
6
9 5
6
O(3, 3, 5)
−2
15
9 13
15
O(2, 4, 5)
−1
20
9 19
20
...
−1 < χ(O) < 0
c(O) > 10
Proof. Denote by O(m) the teardrop with cone point of order m and by O(r, s)
the football with cone points of orders r and s. Let c(m) and c(r, s) denote the
invariant deﬁned in (5.13) in the two cases. Then O(m) has Euler characteristic
1 + 1
m and thus
c(m) = 2 + m + 1
m.
The football O(r, s) has Euler characteristic 1
r + 1
s, so
c(r, s) = r + s + 1
r + 1
s.
The invariant is an integer only in the case of O(2, 2), so the football O(2, 2)
is spectrally distinguishable from the other footballs and teardrops. Thus for the
remainder of the proof, all footballs will be assumed to have at least one cone point
of order strictly greater than 2.
For teardrops, c(m) trivially determines m. We next claim that footballs are
distinguishable from teardrops. Indeed, suppose that c(m) = c(r, s). Then m +
2 = r + s and 1
m = 1
r + 1
s. The latter equation implies that m < min(r, s). Since
also r, s ≥2, we have 2 + m < r + s, a contradiction, thus proving the claim.
It remains only to show that for footballs, c(r, s) determines r and s. From
c(r, s), one can read off the quantities r + s and 1
r + 1
s =
r+s
rs . Hence c(r, s)
determines both r + s and rs, thus also |r −s|, since (r −s)2 = (r + s)2 −4rs.
Hence (r, s) is determined up to order, completing the proof.
□
5.15. THEOREM. Let C be the class consisting of all closed orientable 2-orbifolds
with χ(O) ≥0. The spectral invariant c is a complete topological invariant within
C and moreover, it distinguishes the elements of C from smooth oriented closed
surfaces.

30
DRYDEN, GORDON, GREENWALD, AND WEBB
Proof. We ﬁrst consider the 2-orbifolds for which c is an integer. Note that among
teardrops, footballs, and triangular pillows, the only integer values are c(2, 2) =
5, c(2, 3, 6) = 10, c(2, 4, 4) = 9, and c(3, 3, 3) = 8 (cf. Tables 1 and 2). In
addition, c(2, 2, 2, 2) = 6, c(S2) = 4, and c(T 2) = 0. Let Sg be a Riemann
surface of genus g ≥2. Then we also have c(Sg) = 4 −4g. It is clear that
the values of c are distinct in each case, so that the spectrum distinguishes these
2-orbifolds.
For the rest of the proof, it sufﬁces to consider orbifolds in C with χ(O) > 0
since these include all orbifolds within C for which c is not an integer. Table 2
lists the values of c for these triangular pillows. Setting c(2, 3, 3) = c(2, 2, m) and
solving for m gives m = 25±
√
481
12
, which contradicts the assumption that m is
an integer. Similar calculations for c(2, 3, 4) and c(2, 3, 5) show that the spectrum
distinguishes among triangular pillows with χ(O) > 0.
By Theorem 5.14, c distinguishes among teardrops and footballs.
We next
show that c distinguishes both teardrops and footballs from triangular pillows with
χ(O) > 0. We have c(m) = 2+m+ 1
m, and c(p, q, r) = −2+p+q+r+ 1
p + 1
q + 1
r;
setting the integer and fractional parts of these equations equal gives
2 + m
=
−1 + p + q + r
1
m
=
1
p + 1
q + 1
r −1.
Solving the ﬁrst equation for m and plugging the result into the second equation
yields
0 = pr(p + r −3) + pq(p + q −3) + qr(q + r −3) + pqr(5 −p −q −r).
None of the possible triples (p, q, r) satisfy this equation, showing that teardrops
are distinguished from triangular pillows with χ(O) > 0. The argument that c
distinguishes good footballs from these triangular pillows is analogous.
To see that c distinguishes triangular pillows with χ(O) > 0 from bad foot-
balls, we compare the respective integer and fractional parts of c in each case. For
example, comparing c(2, 3, 3) and c(r, s), r ̸= s gives
7
=
r + s
1
6
=
1
r + 1
s,
which implies s2 −7s + 42 = 0; thus s = 7±√−119
2
, contradicting s being an inte-
ger. The calculations are similar for O(2, 3, 4) and O(2, 3, 5), while for O(2, 2, m)
we have
3 + m
=
r + s
1
m
=
1
r + 1
s,
which implies r(r −3) + s(s −3) + rs = 0. We can assume that one of r and s is
strictly greater than 2, say r. Thus r −3 ≥0 and s −3 ≥−1, which implies
r(r −3) + s(s −3) + rs ≥s(r −1) > 0.

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
31
Hence triangular pillows with χ(O) > 0 are distinguished from bad footballs.
□
5.16. REMARK. Notably absent from the class C are triangular pillows with χ(O) <
0. The invariant c does not seem sufﬁciently strong to distinguish among these tri-
angular pillows. However, as a special case of a result in [13], the spectrum does
determine the orders of the cone points in such a 2-orbifold, provided that it is en-
dowed with a metric of constant curvature −1. On the other hand, to distinguish,
say, triangular pillows with χ(O) < 0 from triangular pillows with χ(O) > 0, we
do not need such a metric assumption.
If O(p, q, r) is any triangular pillow with χ(O) < 0 and spec(O(p, q, r)) =
spec(O(2, 2, m)), then setting the integer and fractional parts of the respective
values of c equal, we have
m + 3
=
p + q + r −2
1
m
=
1
p + 1
q + 1
r.
Solving the ﬁrst equation for m and plugging the resulting value into the second
equation yields
(5.17)
2pqr + pr(p + r −5) + pq(p + q −5) + qr(q + r −5) = 0.
Note that for a triangular pillow with χ(O) < 0, we must have 1
p + 1
q + 1
r < 1,
which implies that the sum of any two of p, q, r is at least 5. Thus each term on
the right-hand side of (5.17) is nonnegative. This contradiction then implies that
O(2, 2, m) cannot be isospectral to such a triangular pillow. For the remaining
triples where χ(O) > 0, we set the integer and fractional parts of the respective
value of c equal to those of a triangular pillow with χ(O) < 0, and note that there
are no χ(O) < 0 triples satisfying these equations. Thus c distinguishes between
triangular pillows with χ(O) < 0 and χ(O) > 0. A similar argument shows that
c distinguishes triangular pillows with χ(O) < 0 from teardrops; it is clear that c
also distinguishes triangular pillows with χ(O) < 0 from the smooth surfaces and
the remaining elements of C, with the exception of footballs. In this last case, it
seems that metric assumptions are again necessary.
5.18. REMARK. Other difﬁculties arise during the consideration of the expanded
class which includes nonorientable orbifolds. Metric assumptions are necessary
in numerous cases, such as distinguishing nonorientable orbifolds with the same
orientable double cover (e.g. O(∗2, 3, 3) and O(3, ∗2), see Table 1 and Figure 1).
We now examine classes that include nonorientable orbifolds.
5.19. PROPOSITION. Within the class of all closed 2-orbifolds with χ(O) ≥0, the
spectrum distinguishes whether the orbifold has zero or positive Euler character-
istic.
Proof. Note that for 2-orbifolds O with χ(O) = 0, c is either an integer or equal
to 4.5. Thus c distinguishes all but the following cases: S2 from the orbifolds
O(∗3, 3, 3) and O(3, ∗3) (with c = 4), the good football O(2, 2) from O(∗2, 3, 6)
(with c = 5), and the bad teardrop O(2) from the orbifolds O(∗2, 4, 4) and O(4, ∗2)

32
DRYDEN, GORDON, GREENWALD, AND WEBB
2
3
3
2
3
3
3
3
2
3
3
2
FIGURE 1. The uppermost object is a fundamental domain for
O(2, 3, 3), with its quotient O(2, 3, 3) below. Here the vertices
are cone points labelled with their orders, and the double edges
represent reﬂector edges. On the bottom left we show O(∗2, 3, 3),
which is obtained by reﬂecting O(2, 3, 3) in the plane of the paper,
and on the right is O(3, ∗2), obtained by reﬂecting O(2, 3, 3) in
the plane containing the dashed loop.
(with c = 4.5). The lack of a mirror locus in the χ(O) > 0 cases and the presence
of a mirror locus in the corresponding χ(O) = 0 orbifolds can be gleaned from the
degree −1
2 term, and so they are distinguished.
□

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
33
5.20. PROPOSITION. Within the class of closed 2-orbifolds of constant nonzero
curvature R or −R the spectrum determines the sign of the curvature, i.e. whether
the orbifold is spherical or hyperbolic.
Proof. Assume that O has cone points p1, . . . , pk of orders m1, . . . , mk, and/or
dihedral corner reﬂector points q1, . . . , qr of orders n1, . . . , nr. Now look at the
coefﬁcient of the t term in the expansion, as in (5.10), which reduces to
a2
4π ± R
 k
X
i=1
(m2
i + 11)(m2
i −1)
360mi
+
r
X
i=1
(n2
i + 11)(n2
i −1)
720ni
!
in the presence of constant curvature. The 1
t term in the expansion tells us vol(O)
and we know the size of the curvature, so we know the a2 component and may
subtract it off. Notice that the summands are nonnegative, and hence we can read
the sign of the curvature unless there were no cone points and no dihedral cor-
ner reﬂector points. In this case, examine the degree zero term, which now has
no point contributions and reduces to a1
4π = χ(O)
6 , and we can read off the Euler
characteristic.
□
5.21. REMARK. In the case of closed 2-orbifolds with a nontrivial mirror locus,
(5.12) enables us to make a stronger statement. In particular, among such orbifolds
that are endowed with a metric of strictly positive, strictly negative, or zero cur-
vature, the spectrum determines the sign of the curvature. This class includes the
bad orbifolds O(∗m) and O(∗p, q) with p ̸= q since they admit a metric of strictly
positive (but variable) curvature.
5.22. PROPOSITION. Within the class of spherical 2-orbifolds of constant curva-
ture R > 0 the spectrum determines the orbifold.
Proof. Notice that the metric requirement eliminates teardrops and bad footballs
and their quotients from this class.
In Table 1, c distinguishes among the re-
maining spherical orbifolds with the exception that c is unable to distinguish be-
tween orbifolds that are nonorientable but have the same orientable double cover:
O(∗m, m), O(m×), and O(m∗), with double cover O(m, m); O(∗2, 2, m) and
O(2, ∗m), with double cover O(2, 2, m); and O(∗2, 3, 3) and O(3, ∗2), with dou-
ble cover O(3, 3, 2) (see Figure 1). However, c is able to distinguish each nonori-
entable class from the remaining orbifolds.
Consider such a class of nonorientable spherical orbifolds with a common ori-
entable double cover. The coefﬁcient of the degree −1
2 term, as given in (5.11),
distinguishes nonorientable orbifolds with mirror loci from those without, i.e. in
this class it distinguishes orbifolds with only crosscaps from those with mirror
loci. In the presence of constant curvature, (5.11) also distinguishes among the
remaining spherical cases: among O(∗m, m) and O(m∗), the length of the mirror
locus of O(∗m, m) is larger in the constant curvature metric; among O(∗2, 2, m)
and O(2, ∗m), the length of the mirror locus of O(∗2, 2, m) is larger; and among
O(∗2, 3, 3) and O(3, ∗2), the length of the mirror locus of O(∗2, 3, 3) is larger (see
Figure 1).
□

34
DRYDEN, GORDON, GREENWALD, AND WEBB
5.23. REMARK. Notice that metric assumptions are only needed to distinguish
within each nonorientable class. We cannot make a similar statement for ﬂat 2-
orbifolds. For example, it is possible to endow O(2, ∗2, 2) and O(2, 2∗) with a
metric of zero curvature so that they have the same area and also have mirror loci
of the same length. They cannot be distinguished by the asymptotic expansion of
the heat trace.
REFERENCES
[1] A. Adem and Y. Ruan, Twisted orbifold K-theory, Comm. Math. Phys. 237 (2003), 533–556.
[2] M. Berger, P. Gauduchon, and E. Mazet, Le spectre d’une vari´et´e riemannienne, Lecture Notes
in Mathematics, vol. 194, Springer-Verlag (1971).
[3] B. C. Berndt and B. P. Yeap, Explicit evaluations and reciprocity theorems for ﬁnite trigono-
metric sums, Adv. in Appl. Math. 29 (2002), 358–385.
[4] T. P. Branson and P. B. Gilkey, The asymptotics of the Laplacian on a manifold with boundary,
Comm. Partial Differential Equations 15 (1990), 245–272.
[5] J. Br¨uning and M. Lesch, On the spectral geometry of algebraic curves, J. Reine Angew. Math.
474 (1996), 25–66.
[6] J. Br¨uning and R. Seeley, The resolvent expansion for second order regular singular operators,
J. Funct. Anal. 73 (1987), 369–429.
[7] Hongwei Chen, On some trigonometric power sums, Int. J. Math. Math. Sci. 30 (2002), 185–
191.
[8] Y.-J. Chiang, Spectral geometry of V -manifolds and its application to harmonic maps, in Dif-
ferential geometry: partial differential equations on manifolds, Proc. Sympos. Pure Math. 54,
Part 1, 93–99.
[9] J. H. Conway, The orbifold notation for surface groups, in Groups, combinatorics and geom-
etry, London Math. Soc. Lecture Note Ser. 165, Cambridge Univ. Press, Cambridge, 1992,
438–447.
[10] H. Donnelly, Spectrum and the ﬁxed point sets of isometries I, Math. Ann. 224 (1976), 161–170.
[11] H. Donnelly, Asymptotic expansions for the compact quotients of properly discontinuous group
actions, Illinois J. Math. 23 (1979), 485–496.
[12] P. Doyle and J.P. Rossetti, Isospectral hyperbolic surfaces have matching geodesics, preprint,
arXiv:math/0605765v1 [math.DG].
[13] E. B. Dryden and A. Strohmaier, Huber’s theorem for hyperbolic orbisurfaces, Canad. Math.
Bull. (to appear).
[14] J. J. Duistermaat and J. A. C. Kolk, Lie groups, Springer-Verlag, Berlin, 2000.
[15] C. Farsi, Orbifold spectral theory, Rocky Mountain J. Math. 31 (2001), 215–235.
[16] M. E. Fisher, Problem 69-14, SIAM Review 13 (1971), 116–119.
[17] J. B. Gil, Full asymptotic expansion of the heat trace for non-self-adjoint elliptic cone opera-
tors, Math. Nachr. 250 (2003), 25–57.
[18] C. S. Gordon and J. P. Rossetti, Boundary volume and length spectra of Riemannian mani-
folds: what the middle degree Hodge spectrum doesn’t reveal, Ann. Inst. Fourier (Grenoble) 53
(2003), 2297–2314.
[19] I. Moerdijk, Orbifolds as groupoids, an introduction, in Orbifolds in Mathematics and Physics,
A. Adem, ed., Contemp. Math. 310 (2002), 205–222.
[20] I. Moerdijk and D. Pronk, Orbifolds, sheaves and groupoids, K-Theory 12 (1997), 3–21.
[21] J. M. Montesinos, Classical tessellations and three-manifolds, Springer-Verlag, Berlin, 1987.
[22] E. Park and K. Richardson, The basic Laplacian of a Riemannian foliation, Amer. J. Math. 118
(1996), 1249–1275.
[23] L. L. Pennisi, Elements of complex variables, Holt, Rinehart and Winston, 1966.
[24] K. Richardson, Traces of heat operators on Riemannian foliations, preprint.

ASYMPTOTIC EXPANSION OF THE HEAT KERNEL FOR ORBIFOLDS
35
[25] J. P. Rossetti, D. Schueth, and M. Weilandt, Isospectral orbifolds with different maximal
isotropy orders, Ann. Glob. Anal. Geom. (to appear).
[26] I. Satake, The Gauss-Bonnet theorem for V -manifolds, J. Math. Soc. Japan 9 (1957), 464–492.
[27] N. Shams, E. A. Stanhope, and D. L. Webb, One cannot hear orbifold isotropy type, Arch.
Math. (Basel) 87 (2006), 375-384.
[28] E. A. Stanhope, Spectral bounds on orbifold isotropy, Ann. Global Anal. Geom. 27 (2005),
355–375.
[29] E. A. Stanhope and A. Uribe, The trace formula for orbifolds, preprint.
[30] W. P. Thurston, Geometry and topology of 3-manifolds, electronic edition of 1980 lecture notes,
available at http://www.msri.org/publications/books/gt3m/.
(Dryden) DEPARTMENT OF MATHEMATICS, BUCKNELL UNIVERSITY, LEWISBURG, PA 17837
E-mail address: ed012@bucknell.edu
(Gordon) DEPARTMENT OF MATHEMATICS, DARTMOUTH COLLEGE, HANOVER, NEW HAMP-
SHIRE 03755
E-mail address: csgordon@dartmouth.edu
(Greenwald) DEPARTMENT OF MATHEMATICS, APPALACHIAN STATE UNIVERSITY, BOONE,
NC 28608
E-mail address: greenwaldsj@appstate.edu
(Webb) DEPARTMENT OF MATHEMATICS, DARTMOUTH COLLEGE, HANOVER, NEW HAMP-
SHIRE 03755
E-mail address: david.l.webb@dartmouth.edu
