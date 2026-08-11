---
title: Spectral invariants for polygons and
id: spectral-invariants-for-polygons-and
tags:
- hyperbolic-pillow-heat-novelty-813161
- ucar-2017
- cone-orbifold
- heat-trace-coefficients
- orbifold-determinacy
- load-bearing-source
- full-text-verified
created: '2026-08-09T08:44:31.783668Z'
updated: '2026-08-09T09:11:22.026706Z'
source: https://edoc.hu-berlin.de/bitstream/handle/18452/19142/ucar.pdf
source_domain: edoc.hu-berlin.de
fetched_at: '2026-08-09T08:44:31.782789Z'
fetch_provider: crawl4ai
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: "Full-text PDF (156 pp., pymupdf-extracted, 54,887 words) of Eren Uçar's\
  \ 2017 Humboldt-Universität zu Berlin PhD thesis \"Spectral invariants for polygons\
  \ and orbisurfaces\" (advisor Dorothee Schüth; reviewers Carolyn Gordon, Daniel\
  \ Grieser; oral exam 20 Sept 2017), arXiv:1711.03405, DOI 10.18452/18463. Chapter\
  \ 3 computes the heat trace of the Dirichlet Laplacian on hyperbolic polygons via\
  \ the \"principle of not feeling the boundary\" (Kac) applied to hyperbolic wedges;\
  \ Chapter 4 (pp. 117-144) extends this to closed constant-curvature orbisurfaces\
  \ with mirror, dihedral, and cone singular points.\n\nGENERAL CONE/WEDGE COEFFICIENT\
  \ (Q2). The thesis's actual closed form for the per-angle contribution is not phrased\
  \ as \"b_l(C) = kappa^l (1/m) p_l(m)\" anywhere — that notation is the citing manuscript's\
  \ own paraphrase. What Uçar actually proves, in closed form for ALL l >= 0, is:\
  \ Corollary 3.30 (p.86, eq. 3.97/3.98) gives the hyperbolic wedge-angle coefficient\
  \ c^H_k(gamma_i) for a general angle gamma via a finite Bernoulli-number sum (attributed\
  \ to and matching Watson [Wat05, formula (22)], with sign relation c^H_k = (-1)^k\
  \ c^S_k). Specialized to a dihedral/wedge angle pi/k (Prop. 4.17, p.134, eq. 4.24),\
  \ the coefficient is EXPLICIT for every l:\n  c^S_l(pi/k) = [1/(4k)] * [(-1)^l/(l+1)!]\
  \ * [1/(2l+1)] * SUM_{j=0}^{l+1} C(2l+2,2j) (k^{2j}-1) B_{2j} B_{2l+2-2j}(1/2) \
  \     (eq. 4.25, p.134)\nwhere B_n are Bernoulli numbers and B_n(1/2) Bernoulli-polynomial\
  \ values (B_n(1/2)=(2^{1-n}-1)B_n). Theorem 4.20(ii) (p.137-138) identifies the\
  \ cone-point-of-order-k contribution to the orbifold heat trace with the series\
  \ C := SUM_nu [SUM_{l=0}^nu (2/(4^l l!)) c^S_{nu-l}(pi/k)] kappa^nu t^nu (Corollary\
  \ 4.19(ii), eq. 4.33, p.137). This IS an explicit closed form for the coefficient\
  \ of every kappa^l t^l (i.e., for b_l(C) in the citing paper's notation) for every\
  \ l — not merely a degree bound, recursion, generating function, or algorithm. Direct\
  \ evaluation (carried out by this fetcher from eqs. 4.25+4.33, not stated verbatim\
  \ by Uçar) confirms: (i) the l=1 case reduces EXACTLY to b_1(C) = kappa*(m^4+10m^2-11)/(360m),\
  \ algebraically identical to the citing manuscript's eq. (4)/(5) [(1/360)(m^3-1/m)+(1/36)(m-1/m)]*K\
  \ with m=k, kappa=K, no sign/factor mismatch; (ii) l=2 gives b_2(C) = kappa^2*(m^2-1)(2m^4+9m^2+37)/(5040m)\
  \ = kappa^2*(2m^6+7m^4+28m^2-37)/(5040m), a genuine degree-6 polynomial p_2(m) divided\
  \ by m — confirming deg p_2 = 2(2)+2 = 6 and producing a NONZERO m^5 coefficient\
  \ (1/2520), i.e. b_2 does yield the power sum P_5 = sum m_i^5 modulo lower symmetric\
  \ functions; (iii) l=3 gives b_3(C) = kappa^3*(m^2-1)(3m^6+11m^4+25m^2+57)/(30240m)\
  \ = kappa^3*(3m^8+8m^6+14m^4+32m^2-57)/(30240m), degree 8 = 2(3)+2, with a NONZERO\
  \ m^7 coefficient (1/10080), i.e. b_3 yields P_7 = sum m_i^7 modulo lower symmetric\
  \ functions. All of these are mechanical (finite-arithmetic) consequences of Uçar's\
  \ published closed form, not new cone-coefficient theory — no fresh computation\
  \ beyond evaluating an already-explicit formula is required to reach l=2,3 or beyond.\n\
  \nUçar's thesis never uses the word \"degree\" and never writes \"p_l(m)\" — the\
  \ citing paper's deg p_l=2l+2 claim is verifiable from eq. (4.25)'s top-degree term\
  \ (j=l+1 gives k^{2l+2}, coefficient built from B_{2l+2}, generically nonzero since\
  \ Bernoulli numbers of even index >=2 never vanish), giving a closed-form leading\
  \ coefficient in principle, though Uçar himself makes no leading-coefficient/asymptotic-in-m\
  \ statement anywhere in the text.\n\nDETERMINACY THEOREM (Q3). Corollary 4.21 (p.139):\
  \ \"Let O be a closed orbisurface of constant curvature kappa in R. Let M in N_0\
  \ denote the number of dihedral points ... and let N in N_0 denote the number of\
  \ cone points and n_1,...,n_N in N their orders. Then: (i) The volume of O and the\
  \ length of the mirror locus are spectral invariants. (ii) If the mirror locus is\
  \ non-trivial ... the curvature ... is determined by the spectrum. (iii) If kappa\
  \ != 0, then kappa together with the spectrum determines the number M+2N as well\
  \ as the multiset {m_1,...,m_M,n_1,n_1,n_2,n_2,...,n_N,n_N}. (iv) If the mirror\
  \ locus is trivial and kappa != 0, then kappa together with the spectrum determines\
  \ the number of cone points as well as the multiset of all orders {n_1,...,n_N}.\"\
  \ Uçar states parts (iii) and (iv) are new results (\"To the best of our knowledge,\
  \ statement (iii) is a new result. ... statement (iv) is also new in this generality\
  \ and was only known for the special case of kappa=-1\"). Corollary 4.23 (p.140)\
  \ specializes to ORIENTABLE orbisurfaces: \"Let O be a closed orientable orbisurface\
  \ with constant curvature kappa != 0. Then kappa together with the spectrum of O\
  \ determines the Euler characteristic of O as well as the Euler characteristic of\
  \ the underlying space X_O\" — proved via Cor. 4.21(iv) since orientability forces\
  \ trivial mirror locus. This generalizes Dryden-Strohmaier's kappa=-1 Huber-theorem\
  \ result [DS09, Prop. 3.3] to all kappa != 0. THE THEOREM IS FULL-SPECTRUM/ASYMPTOTIC\
  \ THROUGHOUT — there is NO coefficient count anywhere in the thesis; every determinacy\
  \ statement is phrased as \"the spectrum\" or \"kappa together with the spectrum\"\
  \ (an infinite, complete invariant), never \"the first N heat invariants suffice.\"\
  \ This is an explicit, confirmed NO on the coefficient-count question. Corollaries\
  \ 4.24-4.25 (pp.140-141) give finer determinacy within restricted classes (all-cone\
  \ or all-dihedral orbifolds; orbifolds where every cone/dihedral order is distinct).\n\
  \nNON-UNIQUENESS DISCUSSION. Page 141 discusses DGGW08's Proposition 5.22 finding,\
  \ for SPHERICAL constant-curvature orbisurfaces, that the multiset invariant of\
  \ Cor. 4.21(iii) alone fails to separate exactly three pairs of orbifolds (Conway/Thurston\
  \ notation): O(*m,m) & O(m,*); O(*2,2,m) & O(2,*m); O(*2,3,3) & O(3,*2) — all resolved\
  \ by additionally comparing mirror-locus length, i.e. by the full spectrum. This\
  \ is a DIFFERENT phenomenon from the citing manuscript's hyperbolic triangular-pillow\
  \ pair O(2,8,8)/O(3,3,12): it concerns spherical orbifolds with nontrivial mirror\
  \ loci, resolved by a second already-spectral invariant (mirror length), not a finite-coefficient\
  \ truncation. Exhaustive search of the full extracted text found NO occurrence of\
  \ the strings \"2,8,8\" or \"3,3,12\" or of the specific reciprocal-sum coincidence\
  \ 1/2+1/8+1/8=1/3+1/3+1/12, and no use of \"power sum,\" \"collision,\" or \"near-isospectral\"\
  \ terminology anywhere in the thesis — the specific pair does not appear in this\
  \ source.\n\nBIBLIOGRAPHY (pp.145-150, confirmed against extracted text): [DGGW08]\
  \ Dryden-Gordon-Greenwald-Webb, \"Asymptotic expansion of the heat kernel for orbifolds,\"\
  \ Michigan Math. J. 56(1):205-238 (2008); [DS09] Dryden-Strohmaier, \"Huber's theorem\
  \ for hyperbolic orbisurfaces,\" Canad. Math. Bull. 52(1):66-71 (2009); [Don76]\
  \ Donnelly, \"Spectrum and the fixed point sets of isometries I,\" Math. Ann. 224:161-170\
  \ (1976); [Wat05] S. Watson, \"The trace function expansion for spherical polygons,\"\
  \ New Zealand J. Math. 34:81-95 (2005) — the direct source of the Bernoulli-sum\
  \ formula Uçar builds on; [vdBS88] van den Berg-Srisatkunarajah, J. London Math.\
  \ Soc. (2) 37:119-127 (1988), the Euclidean analogue."
raw_file: raw/spectral-invariants-for-polygons-and.pdf
---

*Suggested by [[spectral-invariants-for-polygons-and-orbisurfaces]] — direct PDF of the dissertation, primary source for cone coefficient formulas*

Spectral invariants for polygons and
orbisurfaces
D I S S E R T A T I O N
zur Erlangung des akademischen Grades
doctor rerum naturalium
(Dr. rer. nat.)
im Fach Mathematik
eingereicht an der
Mathematisch-Naturwissenschaftlichen Fakultät
der Humboldt-Universität zu Berlin
von
Dipl.-Math. Eren Uçar
Präsidentin der Humboldt-Universität zu Berlin:
Prof. Dr.-Ing. Dr. Sabine Kunst
Dekan der Mathematisch-Naturwissenschaftlichen Fakultät:
Prof. Dr. Elmar Kulke
Gutachter/innen:
1. Prof. Dr. Dorothee Schüth
2. Prof. Dr. Carolyn Gordon
3. Prof. Dr. Daniel Grieser
Tag der mündlichen Prüfung: 20. September 2017


---

Abstract
In this thesis we deal with spectral invariants for polygons and closed orbisurfaces
of constant Gaussian curvature. In each case our method is to study the heat kernel
and the asymptotic expansion of the heat trace as t ↘0.
First we investigate hyperbolic polygons, i.e. relatively compact domains in the
hyperbolic plane with piecewise geodesic boundary. We compute the asymptotic
expansion of the heat trace as t ↘0 associated to the Dirichlet Laplacian of any
hyperbolic polygon, and we obtain explicit formulas for all heat invariants. Our
approach to the asymptotic expansion is based on the so-called principle of not
feeling the boundary due to M. Kac ([Kac66]). Analogous results for Euclidean
and spherical polygons were known before and are published in [vdBS88] and
[Wat05], respectively. By comparing the heat invariants for Euclidean, spherical
and hyperbolic polygons and by scaling the metric appropriately, we unify these
results and deduce the heat invariants for arbitrary polygons. Here, the term
polygon refers to any relatively compact domain with piecewise geodesic boundary
contained in a complete Riemannian manifold of constant Gaussian curvature. It
turns out that the heat invariants provide much information about a polygon, if
the curvature does not vanish. For example, then the multiset of all angles which
are not equal to π and the Euler characteristic of a polygon are spectral invariants.
Furthermore, we compute the asymptotic expansion of the heat trace for any
closed Riemannian orbisurface of constant curvature as t ↘0, and obtain explicit
formulas for all heat invariants. To solve this problem, we study two examples of
spherical orbisurfaces thoroughly and show how their heat traces are related to
each other. This relation together with some observations from [Wat05] allow us
to compute all heat invariants for arbitrary Riemannian orbisurfaces of constant
Gaussian curvature. If the curvature does not vanish, then it is possible to detect
interesting information about the topology and the singular set of an orbisurface
from the heat invariants. For example, we prove that if two orientable orbisurfaces
with the same curvature κ ≠0 are isospectral, then they must be homeomorphic.
This result was previously known for κ = −1 but it was proven differently, namely
by using the Selberg trace formula for the wave kernel and Weyl’s asymptotic law
([DS09]).
We show that the heat invariants for polygons and orbisurfaces are closely related
to each other. For instance, we prove that the contribution of an interior angle π
k ,
k ∈N≥2, to the heat invariants for a polygon is the same as the contribution of
a dihedral point of isotropy order 2k to the heat invariants for an orbisurface, if
the polygon and the orbisurface have the same curvature. This fact together with
the formulas from [Wat05] provide an alternative proof for the contribution of an
interior angle π
k , k ∈N≥2, to the heat invariants for a polygon.
ii


---

Zusammenfassung
In dieser Arbeit beschäftigen wir uns mit Spektralinvarianten von Polygonen
und geschlossenen Orbiflächen konstanter Gaußkrümmung. Unsere Methode ist es
jeweils den Wärmeleitungskern und die asymptotische Entwicklung der Wärmespur
für t ↘0 zu untersuchen.
Als erstes untersuchen wir hyperbolische Polygone, d.h. relativ kompakte Gebiete
in der hyperbolischen Ebene mit stückweise geodätischem Rand. Wir berechnen die
asymptotische Entwicklung der Wärmespur für t ↘0 bezüglich des Dirichlet-Laplace
Operators eines beliebigen hyperbolischen Polygons, und wir erhalten explizite
Formeln für alle Wärmeinvarianten. Unsere Herangehensweise an die asymptotische
Entwicklung basiert auf dem so genannten principle of not feeling the boundary
von M. Kac ([Kac66]). Analoge Resultate für euklidische und sphärische Polygone
waren vorher bekannt und wurden in [vdBS88] bzw. [Wat05] veröffentlicht. Indem
wir die Wärmeinvarianten für euklidische, sphärische und hyperbolische Polygone
miteinander vergleichen und die Metrik geeignet skalieren, vereinheitlichen wir
diese Resultate und leiten die Wärmeinvarianten für beliebige Polygone her. Hierbei
ist mit dem Begriff Polygon ein relativ kompaktes Gebiet mit stückweise geodä-
tischem Rand in einer vollständigen Riemann’schen Mannigfaltigkeit konstanter
Gaußkrümmung gemeint. Es stellt sich heraus, dass die Wärmeinvarianten viele
Informationen über ein Polygon liefern, falls die Krümmung nicht verschwindet.
Zum Beispiel sind dann die Multimenge aller Winkel, die ungleich π sind, und die
Euler-Charakteristik eines Polygons Spektralinvarianten.
Außerdem berechnen wir die asymptotische Entwicklung der Wärmespur von
geschlossenen Riemann’schen Orbiflächen konstanter Krümmung für t ↘0 und
erhalten explizite Formeln für alle Wärmeinvarianten. Um dieses Problem zu lösen,
untersuchen wir ausführlich zwei Beispiele sphärischer Orbiflächen und zeigen, wie
ihre Wärmespuren in Relation zueinander stehen. Diese Relation zusammen mit
einigen Beobachtungen aus dem Artikel [Wat05] ermöglichen es uns die Wärme-
invarianten beliebiger Riemann’scher Orbiflächen konstanter Gaußkrümmung zu
berechnen. Falls die Krümmung nicht verschwindet, so kann man interessante
Informationen aus den Wärmeinvarianten über die Topologie und die singuläre
Menge einer Orbifläche ermitteln. Beispielsweise zeigen wir, dass falls zwei orien-
tierbare Orbiflächen mit derselben Krümmung κ ≠0 isospektral sind, sie dann auch
homöomorph sein müssen. Dieses Resultat war vorher bekannt für κ = −1, wurde
jedoch auf andere Weise bewiesen, nämlich mittels der Selberg-Spurformel für den
Wellenkern und der Weyl’schen Eigenwertasymptotik ([DS09]).
Wir zeigen, dass die Wärmeinvarianten für Polygone und Orbiflächen eng mitein-
ander verwandt sind. Zum Beispiel beweisen wir, dass der Beitrag eines Innenwinkels
π
k , k ∈N≥2, zu den Wärmeinvarianten eines Polygons derselbe ist wie der Beitrag
eines Diederpunktes mit Isotropieordnung 2k zu den Wärmeinvarianten einer Orbi-
fläche, falls das Polygon und die Orbifläche dieselbe Krümmung besitzen. Diese
Tatsache gemeinsam mit den Formeln aus [Wat05] liefert einen alternativen Beweis
für den Beitrag eines Innenwinkels π
k , k ∈N≥2, zu den Wärmeinvarianten eines
Polygons.
iii


---

Acknowledgements
I would like to thank my supervisor Prof. Dorothee Schüth for her constant support,
scientific criticism, and faith in me. I benefited a lot from her mathematical knowledge
and experience; without her guidance this work would not exist.
I would also like to thank my colleagues at the Humboldt-Universität zu Berlin for the
pleasant working atmosphere and the helpful discussions on mathematics.
Last but not least I am deeply grateful to my family for all the support and the extra
love that they gave me. In particular my parents, Gülşeher and Cengiz, my brother
Imran, and my wife Magdalena. This project would not have entered my life without
the encouragement of my wife. She shared both the joyful and the seemingly hopeless
moments during my research - thank you!


---

Contents
1
Introduction
1
2
Preliminaries
6
2.1
Background in spectral geometry . . . . . . . . . . . . . . . . . . . . . . . .
6
2.2
Associated Legendre functions . . . . . . . . . . . . . . . . . . . . . . . . . .
10
3
Spectral invariants for polygons
37
3.1
Green’s function and heat kernel of a wedge . . . . . . . . . . . . . . . . . .
41
3.2
Heat invariants for hyperbolic polygons
. . . . . . . . . . . . . . . . . . . .
66
3.3
Consequences for polygons . . . . . . . . . . . . . . . . . . . . . . . . . . . .
92
3.4
Method of images and finite trigonometric sums . . . . . . . . . . . . . . . 103
4
Spectral invariants for orbisurfaces
117
4.1
Two examples of orbifolds
. . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
4.2
Heat invariants for orbisurfaces . . . . . . . . . . . . . . . . . . . . . . . . . 126
4.3
Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 138
Bibliography
145
v


---

1 Introduction
Let M be a two-dimensional smooth connected Riemannian manifold and Ω⊂M be a
non-empty and relatively compact domain. Further, let ∆Ωdenote the Dirichlet Laplacian
for Ω. Then the spectrum of ∆Ωconsists of a sequence of non-negative eigenvalues without
a finite accumulation point and each eigenvalue has a finite multiplicity. We enumerate
them according to their multiplicities as follows:
0 ≤λ1 < λ2 ≤λ3 ≤... ↗∞.
(1.1)
The spectrum of ∆Ωand the geometry of the domain Ωare closely connected. Histori-
cally, this became popularised through a seminal article with the catchy title “Can one
hear the shape of a drum?” written by M. Kac half a century ago ([Kac66]). In his article,
M. Kac interprets a domain physically as a drum and the eigenvalues of ∆Ωas the pure
tones of the drum, if it is fixed along its boundary. On the one hand, the spectrum of the
Dirichlet Laplacian is uniquely determined by the shape, or rather by the geometry of the
domain. On the other hand, it is possible to deduce geometric properties of the domain
if one only knows the sequence (1.1). Such properties, i.e. those which are determined
by the spectrum, are called spectral invariants and are principal objects of study in the
realm of inverse spectral geometry. One well-known method to obtain spectral invariants
of Ωis to compute the asymptotic expansion of the heat trace, which lies at the heart of
our investigations in this thesis.
The heat trace of Ωis the function
ZΩ(t) =
∞
∑
i=1
e−λit,
t > 0.
(1.2)
Obviously, the heat trace only depends on the spectrum of ∆Ω. It is remarkable that, if
the boundary ∂Ωof the domain is non-empty and smooth, then the heat trace has an
asymptotic expansion of the form
ZΩ(t)
t↓0∼
1
4πt
∞
∑
k=0
akt
k
2 ,
(1.3)
where the coefficients ak in the asymptotic expansion, the so-called heat invariants,
correspond to geometric properties of Ω. For example, if κ denotes the Gaussian curvature
and κg the geodesic curvature, then the first three heat invariants are given as
a0 = ∫
Ω
1dA = ∣Ω∣,
a1 = −
√π
2 ∫
∂Ω
1ds = −
√π
2 ∣∂Ω∣,
1


---

1 Introduction
a2 = 1
3
⎛
⎝∫
Ω
κdA + ∫
∂Ω
κg ds⎞
⎠= 2π
3 χ(Ω),
where ∣Ω∣, ∣∂Ω∣and χ(Ω) denote the area of the domain, the length of its boundary
and its Euler characteristic, respectively. Thus the area, the perimeter and the Euler
characteristic are determined by the spectrum of ∆Ω. More generally, it is known that any
heat invariant can be written as a sum, ak = ik + bk, where ik is given as an integral over
Ωof some polynomial in the Gaussian curvature and its covariant derivatives, whereas
bk is given as an integral over ∂Ωof some polynomial in the geodesic curvature and its
derivatives. Nevertheless almost all of these polynomials, and hence the heat invariants,
are still unknown. Using computer calculations, L. Smith has obtained the first seven
heat invariants for smooth domains in the Euclidean plane ([Smi81]), and, more generally,
the first five heat invariants for any smooth domain can be found in [BG90].
In this thesis we first aim to study the asymptotic expansion of the heat trace for
hyperbolic polygons, i.e. relatively compact domains in the hyperbolic plane with piecewise
geodesic boundary. At first sight, the behaviour of the heat trace for hyperbolic polygons
as t ↘0 is similar as for domains with smooth boundary. It has an asymptotic expansion
as in (1.3) and the coefficients in the asymptotic expansion, still called heat invariants,
reflect geometric properties of the domain. However, the above formulas for the heat
invariants are generally not valid anymore for domains whose boundary is not smooth.
We will prove that the heat trace for hyperbolic polygons has an asymptotic expansion
of the form
ZΩ(t)
t↓0∼∣Ω∣
4πt −∣∂Ω∣
8
√
πt
+
∞
∑
k=0
(ik + bkt
1
2 + νk)tk,
where we also obtain explicit formulas for all coefficients (see Theorem 3.32). Qualitatively,
ik and bk can be written as described above for domains with smooth boundary. But now
there is also a contribution to the heat invariants from the vertices of the polygon, which
we abbreviate by νk.
The analogous problem was solved for Euclidean polygons in [vdBS88] and for spherical
polygons in [Wat05]. The immediate question is how the heat invariants depend on
the Gaussian curvature of the polygon? We will answer this question by deriving the
asymptotic expansion of the heat trace for polygons in arbitrary two-dimensional complete
Riemannian manifolds of constant curvature (see Corollary 3.37). We want to emphasise
that we not only generalise the ambient space, but also our definition of the term polygon
is more general than the standard notion (see Definition 3.34). It turns out that the heat
invariants for polygons can be written as polynomials in the Gaussian curvature with
coefficients depending on all angles of the polygon. Later on we use orbifold theory as a
vehicle to explain this behaviour more deeply in the case of polygons with interior angles
of π
k, k ∈N≥2.
Through the heat invariants we will deduce some interesting geometric consequences
for a polygon of constant curvature when its spectrum is given. In particular we will
prove the following:
2


---

1 Introduction
●It is possible to detect the volume, perimeter and curvature of a polygon from its
spectrum (see Corollary 3.38).
●If the curvature of a polygon is nonzero, then the multiset of all its angles which
are not equal to π, as well as its Euler characteristic are spectral invariants (see
Theorem 3.40).
●A polygon Ωwith at least one angle not equal to π and a smooth domain D can
never be isospectral, i.e. they can not have the same spectrum, if χ(Ω) ≥χ(D) (see
Corollary 3.44 (ii)).
●We prove that hyperbolic and spherical triangles are determined up to isometry by
their spectrum within the class of all polygons (see Corollary 3.45)
●Regular hyperbolic and spherical polygons are determined up to isometry by their
spectrum within the class of all hyperbolic and spherical polygons. Moreover, the
spectrum determines whether hyperbolic or spherical polygons are convex (see
Corollary 3.46).
●A simply connected Euclidean polygon can never be isospectral to a two-dimensional
compact manifold with nonempty smooth boundary. Moreover, a polygon with zero
curvature can not be isospectral to a smooth domain in the Euclidean plane (see
Corollary 3.43).
In connection with the situation described above, we also study the heat invariants
for closed two-dimensional Riemannian orbifolds of constant curvature. Orbifolds can
be regarded as a natural generalisation of manifolds, and as such the class of orbifolds
naturally possesses a greater variety than that of manifolds. Roughly speaking, an orbifold
consists of a regular manifold possibly with an additional set of various singular points,
where everything is related to each other through an orbifold structure. For example,
consider a hyperbolic polygon Ωwhose angles are equal to rational multiples of π. Such
a polygon can be captured accurately as a closed orbifold, such that the regular part is
equal to Ω, the singular set is equal to ∂Ωand all geometric properties are described
properly within the orbifold structure. Over the last 15 years, orbifolds were studied
intensively by spectral geometers and many objects, ideas and tools known from manifold
theory were translated into the realm of orbifolds (see [DGGW08], [Gor12]).
Suppose O is any Riemannian orbisurface, i.e. a two-dimensional closed Riemannian
orbifold, and let ∆O be its Laplacian. Again, the spectrum of ∆O consists of a non-
negative sequence of eigenvalues without a finite accumulation point. All eigenvalues
have a finite multiplicity and we list them like in (1.1) as 0 = µ1 ≤µ2 ≤... ↗∞. The heat
trace ZO(t) ∶= ∑∞
i=1 e−µit of the orbifold has an asymptotic expansion as t ↘0 exactly
as in (1.3). The coefficients in this asymptotic expansion, the heat invariants, contain
geometric information about the orbifold. We will compute the asymptotic expansion
of ZO(t) as t ↘0 for any orbisurface of constant curvature. Thereby we obtain explicit
formulas for all heat invariants in terms of the curvature and the singular points of the
orbifold (see Theorem 4.20).
3


---

1 Introduction
It is well-known that two-dimensional orbifolds can have three types of singular
points, called mirror points, dihedral points, and cone points. The heat invariants provide
information about the singular set and the topology of the orbisurface. We will show in
particular the following:
●The spectrum of any orbisurface O with constant nonzero curvature fixes the value
of the sum M + 2N, where M denotes the number of all dihedral points and N
denotes the number of all cone points of O. Furthermore, the spectrum determines
the multiset {m1,...,mM,n1,n1,...,nN,nN}, where 2m1,...,2mM denote the orders
of the dihedral points and n1,...,nN denote the orders of the cone points of O (see
Corollary 4.21 (iii)).
●If two orientable orbisurfaces with constant curvature κ ≠0 are isospectral, then
the orbifolds have the same Euler characteristic, and the underlying topological
spaces are homeomorphic (see Corollary 4.23). This generalises a result of [DS09]
in which the same result was proven in case of constant curvature κ = −1 using the
Selberg trace formula for the wave kernel.
●Within various classes of orbifolds, the spectrum determines the singular set and
the Euler characteristic of the orbifold as well as the Euler characteristic of the
underlying topological space (see Corollary 4.24 and Corollary 4.25).
The contents of this thesis are structured as follows. In the second chapter, we provide
the requisite background in spectral geometry and about Legendre functions (more
precisely, so-called associated Legendre functions). Then we investigate and solve a class
of integrals involving the associated Legendre functions of the second kind. The solutions
of these integrals seem to be unknown to date and some of the solutions will be used
in the subsequent chapter in order to compute the Green’s function and heat kernel
associated to an arbitrary hyperbolic wedge.
The third chapter is the main part of this thesis. In the first section, we obtain explicit
formulas for the Green’s function and the heat kernel of a hyperbolic wedge by solving the
corresponding boundary value problems. These formulas are used in the second section in
order to compute the asymptotic expansion of the heat trace for any hyperbolic polygon.
Explicit formulas for all heat invariants are given as well. In the third section, we use
the heat invariants for Euclidean polygons (from [vdBS88]) and spherical polygons (from
[Wat05]) to compute the heat invariants for polygons of arbitrary constant curvature.
We then draw some conclusions from the heat invariants, i.e. we discuss what can be said
about a polygon knowing all its heat invariants. Finally, in the last section, we investigate
once again the heat trace for hyperbolic polygons with interior angles π
k, for some k ∈N≥2.
By using Sommerfeld’s method of images we obtain another and more elementary formula
for the heat kernel of any wedge with angle π
k, k ∈N≥2. Using this formula we compute
the contributions to the heat invariants from the vertices of a polygon once again. They
will now appear rather differently as finite trigonometric sums. By comparison with the
previous formulas, we obtain remarkable identities for these trigonometric sums.
4


---

1 Introduction
The final chapter deals with two-dimensional orbifolds, also called orbisurfaces. Here,
we first investigate two examples of spherical orbisurfaces and, in particular, how their
heat traces are related to each other. Then we use this relation and some observations
from the article [Wat05] to compute the heat invariants for two-dimensional Riemannian
orbifolds of constant curvature. We will obtain formulas for all heat invariants in terms
of the Gaussian curvature and the singular strata of the orbifold. In the last section, we
discuss some applications of the heat invariants and show how the orbifold theory is linked
to the results of Chapter 3. For example, we prove that the contribution of an interior
angle π
k, k ∈N≥2, to the heat invariants for a polygon is the same as the contribution of a
dihedral point of isotropy order 2k to the heat invariants for an orbisurface, if the polygon
and the orbisurface have the same curvature. This fact together with the formulas from
[Wat05] provide an alternative proof for the contribution of an angle π
k, k ∈N≥2, to the
heat invariants for a polygon.
5


---

2 Preliminaries
2.1 Background in spectral geometry
In this section we want to recall some basic definitions and well-known facts to lay the
foundations for this thesis. In particular we will clarify our notation along the way. Since
all of the material in this section is well documented in the literature, we do not need
to go into the details. Instead we will always point out where to find the corresponding
topics in the literature.
Let M be a two-dimensional smooth connected Riemannian manifold and Ω⊂M be
any non-empty domain, i.e. an open and connected subset. Note that the case Ω= M
is included here. Let ∆Ωbe the (positive semi-definite) Dirichlet Laplacian for Ωwith
respect to the Riemannian measure (see [Gri09]).
A central function for our purposes is the heat kernel associated to the Dirichlet
Laplacian ∆Ω, which we want to introduce first. Since we will consider no other operator
than the Dirichlet Laplacian for Ω, we will call it simply the heat kernel of Ω.
Definition 2.1. (see [Gri09], Definition 9.1.) A smooth function u ∶Ω× (0,∞) →R is
called a fundamental solution to the heat equation at the point y ∈Ωif it satisfies the
following conditions:
⎧⎪⎪⎪⎨⎪⎪⎪⎩
(∂t + ∆)u(x,t) = 0,
∀(x,t) ∈Ω× (0,∞),
lim
t↘0 ∫
Ω
u(x,t)f(x)dx = f(y),
∀f ∈C∞
c (Ω).
(2.1)
As usual, C∞
c (Ω) denotes the space of all real-valued, smooth and compactly supported
functions on Ω. Further, ∆∶C∞(Ω) →C∞(Ω), ∆f ∶= −div(∇f) denotes the Laplacian of
Ω, where ∇and div are taken with respect to the Riemannian metric of Ωinduced by M.
The heat kernel of Ωcan be characterised as the minimal non-negative fundamental
solution to the heat equation in the sense of Definition 2.2 below. For the existence of
such a minimal fundamental solution we refer to [Gri09]. The uniqueness follows directly
from the minimality property.
Definition 2.2. (see [Gri09], Theorem 9.5.) The heat kernel of Ωis defined as the smooth
function
KΩ∶Ω× Ω× (0,∞) →R,
(x,y,t) ↦KΩ(x,y;t),
such that for any y ∈Ωthe function KΩ(⋅,y;⋅) is a non-negative solution to (2.1), and it
6


---

2 Preliminaries
is minimal in the following sense: If u(x,t) is another smooth and non-negative solution
to (2.1), then u(x,t) ≥KΩ(x,y;t) for all x ∈Ω, t > 0.
Another very important function is the heat trace, defined for relatively compact
domains and closely related to the heat kernel.
Definition 2.3. Let Ω⊂M be a relatively compact domain, i.e. a domain with compact
closure. The heat trace of Ωis defined as the function ZΩ∶(0,∞) →R given by
ZΩ(t) ∶= ∫
Ω
KΩ(x,x;t)dx,
t > 0.
(2.2)
The integral in (2.2) is convergent since 0 ≤KΩ(x,x;t) ≤KM(x,x;t) for all t > 0, x ∈Ω
and x ↦KM(x,x;t) is integrable as a continuous function on the compact domain Ω.
For the second estimate note that KΩ(⋅,x;⋅) and KM(⋅,x;⋅)∣Ω×(0,∞) are both fundamental
solutions at x ∈Ωand KΩ(⋅,x;⋅) satisfies the minimality property of Definition 2.2.
Proposition 2.4. (see [Gri09, Theorem 10.13]) If the domain Ωis relatively compact,
then the following holds:
(i) The spectrum of ∆Ωconsists of a sequence of non-negative eigenvalues without a
finite accumulation point and each eigenvalue has a finite multiplicity.
Suppose the eigenvalues (λi)∞
i=1 are enumerated with multiplicity such that
0 ≤λ1 < λ2 ≤λ3 ≤... ↗∞.
(2.3)
There exists an orthonormal basis {ϕi}∞
i=1 for L2 (Ω) such that each function ϕi is
an eigenfunction of ∆Ωcorresponding to the eigenvalue λi.
(ii) The heat kernel KΩ(x,y;t) is given by
KΩ(x,y;t) =
∞
∑
i=1
e−λitϕi(x)ϕi(y),
(2.4)
where the series converges absolutely and uniformly on Ω× Ω× [ϵ,∞) for any ϵ > 0.
Remark. Because Ωis connected (by definition), the first eigenvalue must be simple,
i.e. λ1 < λ2 (see [Gri09, Corollary 10.12]). Further, one can show that λ1 > 0 if M/Ωis
non-empty (see [Gri09, Theorem 10.22]).
If Ωis a relatively compact domain with smooth boundary ∂Ω, then the heat kernel
can be extended continuously to Ω× Ω× (0,∞) by setting KΩ(x,y;t) ∶= 0 whenever x or
y lies on the boundary (see [Gri99, Section 2.3] and [Dod83]).
Corollary 2.5. If Ωis relatively compact, then the heat trace is related to the spectrum
of ∆Ωby
ZΩ(t) =
∞
∑
i=1
e−λit.
(2.5)
7


---

2 Preliminaries
Proof. Since for any fixed t > 0, the series in (2.4) converges uniformly on Ω× Ω, we
obtain
ZΩ(t) = ∫
Ω
∞
∑
i=1
e−λitϕi(x)2dx =
∞
∑
i=1 ∫
Ω
e−λitϕi(x)2dx =
∞
∑
i=1
e−λit.
The last equality follows because ∥ϕi∥L2(Ω) = 1 by definition.
We will use the Laplace transform in Section 3.1 to solve boundary value problems
for the Green’s function and the heat kernel. Therefore, we want to summarise some
fundamental facts of the Laplace transform in advance, referring to [Dav02] and [Doe50]
for more details.
Definition 2.6. Let f ∶(0,∞) →R be a continuous function. The Laplace integral of f
with parameter s ∈C is defined formally as
∞
∫
0
e−stf(t)dt.
Suppose the Laplace integral of f exists for at least one value of s, i.e. the function
(0,∞) ∋t ↦e−stf(t) ∈C is integrable. Then the Laplace transform of f is the function F
given by
F(s) ∶=
∞
∫
0
e−stf(t)dt,
(2.6)
which is defined for all values of s ∈C such that the Laplace integral exists. We write
L{f} for the Laplace transform of f, such that L{f}(s) ∶= F(s).
In practice, the Laplace transform is often convergent and holomorphic on a half-plane
as in (2.7) below.
Definition 2.7. For any δ ∈R we use the following notation:
H>δ ∶= {z ∈C ∣R(z) > δ },
(2.7)
where R(z) denotes the real part of z.
Proposition 2.8. Let f ∶(0,∞) →R be continuous and suppose the Laplace integral of
f is absolutely convergent at some point δ ∈R. Then the Laplace integral is absolutely
convergent for all s ∈H>δ and the Laplace transform F = L{f} is holomorphic on the
half-plane H>δ. Moreover, the Laplace transform is unique, i.e. if g ∶(0,∞) →R is
continuous and L{g} = L{f}, then f(t) = g(t) for all t ∈(0,∞).
If f is even continuously differentiable, then for any ε > δ and any t ∈(0,∞),
f(t) =
1
2πi lim
N→∞
ε+iN
∫
ε−iN
estF(s)ds.
(2.8)
8


---

2 Preliminaries
For the result about uniqueness of the Laplace transform, we refer to [Doe50, Satz 9
on p. 79]. The other results of Proposition 2.8 are also contained in [Doe50], but more
elegant proofs can be found in [Dav02, Section 2.1 and 3.3].
We emphasise that the integral in (2.8) is taken along an arbitrary straight line in
the half-plane H>δ, parallel to the imaginary axis. Furthermore, both endpoints of the
integral tend to infinity simultaneously.
Definition 2.9. A continuous function f ∶(0,∞) →R is called the inverse Laplace
transform of a function F, if L{f} = F. Then we use the notation L−1{F} ∶= f.
If the inverse Laplace transform of a given function is not known already, one can use
(2.8) for its calculation. Equation (2.8) is called the complex inversion formula and is
actually also valid in more general situations (see [Doe50, Satz 1 on p. 210]).
Next, we want to consider the Laplace transform of the heat kernel KΩ(x,y;⋅). It does
not always exist if x = y and thus we introduce the following sets.
Definition 2.10. The sets
diag(Ω) ∶= {(x,y) ∈Ω× Ω∣x = y },
o-diag(Ω) ∶= {(x,y) ∈Ω× Ω∣x ≠y }
are called the diagonal and off-diagonal of the cartesian product Ω× Ω, respectively.
By definition, KΩ(x,y;t) is smooth on Ω× Ω× (0,∞). Moreover, we can extend the
heat kernel smoothly to o-diag(Ω) × R by setting KΩ(x,y;t) ∶= 0 for all t ≤0 (see [Gri09,
Corollary 9.21]). In particular, for any (x,y) ∈o-diag(Ω) the function KΩ(x,y;⋅) can be
extended continuously at t = 0 and one can prove that the Laplace integral of KΩ(x,y;⋅)
exists for all s > 0 (see [Gri09, Exercise 9.10]). Thus, by Proposition 2.8, the Laplace
transform s ↦L{KΩ(x,y;⋅)}(s) is holomorphic on the domain H>0.
Definition 2.11. The Laplace transform of KΩ(x,y;t) is called the resolvent kernel or
Green’s function of Ω. More precisely, the Green’s function is defined as the function
GΩ∶o-diag(Ω) × H>0 →C,
((x,y),s) ↦GΩ(x,y;s) ∶=
∞
∫
0
e−stKΩ(x,y;t)dt.
(2.9)
Proposition 2.12. ([Gri09, Exercise 9.10]) For any s > 0, the Green’s function GΩ(⋅,⋅;s)
is a non-negative and smooth function on o-diag(Ω). Furthermore, for any y ∈Ωand any
s > 0 the function u ∶Ω/{y} ∋x ↦GΩ(x,y;s) ∈R belongs to L1(Ω) and
∫
Ω
u(x) ⋅(s + ∆)f(x)dx = f(y) for all f ∈C∞
c (Ω).
(2.10)
In particular, (s + ∆)u(x) = 0 for all x ∈Ω/{y}.
9


---

2 Preliminaries
2.2 Associated Legendre functions
In this section, we want to introduce the so-called associated Legendre functions of the
first and second kinds and summarise some of their properties. Then we investigate
a special class of integrals involving associated Legendre functions, which seem to be
unsolved up to now. Some of these integrals are important for our purposes, because they
will naturally appear in the next chapter, where we will obtain explicit formulas for the
Green’s function and the heat kernel of a wedge. Therefore we will explain our method for
solving those integrals in detail. Further, we want to remark that these integrals can be
rewritten as so-called generalised Mehler transforms. From this point of view we basically
compute new generalised Mehler transforms. Despite the fact that the generalised Mehler
transform has been known for some time (see [Low64], [Sne72], [Ros74]), apparently
there hardly exist calculated examples compared with other integral transformations (see
[OH61] for a list of known generalised Mehler transforms).
We want to stress that our discussion of the associated Legendre functions will not
be complete, and that extensive treatises can be found in the literature on associated
Legendre functions (see for example [GR07, Chapter 8.7−8.8], [Hob65], [VF01], [EMOT53,
Chapter III], [OLBC10, Chapter 14], [Olv97, Chapter 5], and [Tem96, Chapter 8]).
Definition 2.13. The associated Legendre equation is an ordinary differential equation,
defined as
(1 −z2) d2u
dz2 −2zdu
dz + (ν (ν + 1) −
µ
1 −z2)u = 0,
(2.11)
with parameters ν,µ ∈C and variable z ∈C/{−1,+1}. Any solution of (2.11) is called an
associated Legendre function.
In particular, we are interested in two special solutions, namely, the associated Legendre
functions of the first and second kinds. These can be defined in several equivalent ways;
we choose to define them via the hypergeometric function.
Definition 2.14. For any z ∈C,k ∈N0, the Pochhammer symbol is defined as
(z)k ∶=
⎧⎪⎪⎨⎪⎪⎩
1,
if k = 0,
z(z + 1)(z + 2)⋯(z + k −1),
if k ≥1.
It follows that (−n)k = 0 if and only if n ∈N0,k ∈N with k > n. The Pochhammer symbol
is related to the gamma function Γ(z) through the equation
(z)k = Γ(z + k)
Γ(z)
,
which is easily established using the identity Γ(z + 1) = z ⋅Γ(z).
The following facts about the hypergeometric function, i.e. everything up to Definition
2.16 below, can be found for example in [Olv97, Section 9 of Chapter 5].
10


---

2 Preliminaries
Definition 2.15. Let a,b,c ∈C such that c ∉{0,−1,−2,...}, and let z ∈C/[1,∞). The
hypergeometric function F(a,b;c;z) is defined through
F(a,b;c;z) ∶=
∞
∑
k=0
(a)k(b)k
(c)k k! zk,
for ∣z∣< 1,
and via analytic continuation for ∣z∣≥1 with z ∉[1,∞).
The function
1
Γ(c)F(a,b;c;z)
is an entire function in all three parameters a,b,c and is analytic in z ∈C/[1,∞). As
usual, this means that the function is analytic wherever it is defined directly and can be
extended analytically to where it is not formally defined. In particular, we think of the
above function as analytically extended in c ∈{0,−1,−2,...}, even though F(a,b;c;z) is
formally not defined for those values of c. Furthermore, the hypergeometric function is a
solution of the hypergeometric differential equation:
z(1 −z)d2u
dz2 + (c −(a + b + 1)z) du
dz −ab ⋅u = 0.
We use the hypergeometric function to introduce now the most important functions
in this section. For powers, we always use the standard branch: zµ = eµ log(z) with
log(z) ∶= log(∣z∣) + iarg(z) for z ∈C/(−∞,0], with arg(z) ∈(−π,π).
Definition 2.16. Let z ∈C/(−∞,1]. The associated Legendre function of the first kind
is defined by
P µ
ν (z) ∶= (z + 1
z −1)
µ
2
1
Γ(1 −µ)F (−ν,ν + 1;1 −µ; 1 −z
2
),
(2.12)
where ν,µ ∈C. The associated Legendre function of the second kind is defined by
Qµ
ν(z) ∶= eµπiΓ(ν + µ + 1)√π (z2 −1)
µ
2
2ν+1zν+µ+1 ⋅Γ(ν + 3
2)
F (ν + µ + 2
2
, ν + µ + 1
2
;ν + 3
2; 1
z2),
(2.13)
where µ,ν ∈C such that µ + ν ∉{−1,−2,−3,,...}.
For µ = 0 we use Pν(z) ∶= P 0
ν (z) and Qν(z) ∶= Q0
ν(z). These functions are also known
as Legendre functions of the first and second kinds, respectively.
Note that for z ∈C/(−∞,1], both 1−z
2
and
1
z2 are in C/[1,∞), so that Definition 2.15
indeed applies. Moreover, for these z we have z+1
z−1 ∈C/(−∞,0], so ( z+1
z−1)
µ
2 is defined as
explained above. The same holds for (z2 −1)
µ
2 if we read it as (z + 1)
µ
2 ⋅(z −1)
µ
2 .
The associated Legendre functions of the first and second kinds are linearly independent
solutions of (2.11), and are analytic in the parameters µ and ν, whenever defined, as
11


---

2 Preliminaries
well as in the variable z. Definition 2.16 was first introduced by Hobson, it can be
found in his classical treatise [Hob65] and is commonly used in the literature (e.g. in
[GR07], [EMOT53], [Tem96] etc.). Some authors, however, define the associated Legendre
functions differently, in particular, the function of the second kind. For example, E. Barnes
and G. Watson define Qµ
ν(z) differently in [Bar08] and [Wat18], respectively. Also [Olv97],
[OLBC10] do not prefer to work with Qµ
ν(z) as defined in (2.13).
There are plenty of remarkable relations and identities between the asociated Legendre
functions of the first and second kinds (see [GR07], [EMOT53]). For the convenience of
the reader we summarise those which will be important for us.
Lemma 2.17. The associated Legendre functions of the first and second kinds satisfy
the following identities for all allowed values of ν,µ,z,ω:
P µ
ν (z) = P µ
−ν−1(z),
(2.14)
Qµ
ν(z) = e2iµπ Γ(ν + µ + 1)
Γ(ν −µ + 1)Q−µ
ν (z),
(2.15)
P −µ
ν (z) = Γ(ν −µ + 1)
Γ(ν + µ + 1) (P µ
ν (z) −2
πe−iµπ sin(µπ)Qµ
ν(z)),
(2.16)
Q−µ
ν (z)Qµ
ν(ω) = Q−µ
ν (ω)Qµ
ν(z),
(2.17)
−2sin (µπ)
π
Q−µ
ν (z)Qµ
ν(ω) = e−iµπP −µ
ν (ω)Qµ
ν(z) −eiµπP µ
ν (ω)Q−µ
ν (z).
(2.18)
Proof. Equation (2.14) is stated in [GR07, formula 8.731 5] and is a consequence of (2.12)
and the symmetry of the hypergeometric function with respect to the first two variables,
i.e. F(a,b;c;z) = F(b,a;c;z). The identities (2.15) and (2.16) can be found in [GR07,
formula 8.736 4] and [GR07, formula 8.736 1], respectively. Equation (2.17) follows from
(2.15), when applied twice.
In order to prove (2.18), we first apply (2.15), (2.16) and get:
P −µ
ν (ω)Qµ
ν(z) = e2iµπP µ
ν (ω)Q−µ
ν (z) −2eiµπ sin(µπ)
π
Q−µ
ν (z)Qµ
ν(ω).
If we multiply both sides of the above equation with e−iµπ and rearrange the terms, we
obtain (2.18).
Another remarkable connection between the associated Legendre functions of the first
and second kinds is given by Whipple’s formula (see [EMOT53, formulas (13) and (14)
on p. 141]).
Lemma 2.18. For all z ∈C/(−∞,1] with R(z) > 0 the following relations hold:
e−iµπQµ
ν(z) =
√π
2 Γ(ν + µ + 1)
1
(z2 −1)
1
4 P
−ν−1
2
−µ−1
2
⎛
⎝
z
(z2 −1)
1
2
⎞
⎠,
(2.19)
P µ
ν (z) = ieiνπ
√
2
π ⋅
1
Γ(−ν −µ) ⋅
1
(z2 −1)
1
4 Q
−ν−1
2
−µ−1
2
⎛
⎝
z
(z2 −1)
1
2
⎞
⎠.
(2.20)
12


---

2 Preliminaries
In order to investigate certain integrals later in this section, it is helpful to know the
following asymptotic behaviour of the associated Legendre functions of the first and
second kinds.
Lemma 2.19. Let a > 0.
(i) For any µ ∈C:
P µ
ν (cosh(a)) =
Γ(ν + 1)
Γ(ν −µ + 1) ⋅
1
√
2π(ν + 1)sinh(a)
⋅(e(ν+ 1
2 )a + e−πi(µ−1
2 )−(ν+ 1
2 )a)(1 + O ( 1
∣ν∣))
(2.21)
as ∣ν∣→∞with R(ν) > −1.
(ii) For any µ ∈C:
P µ
−1
2 +iρ (cosh(a)) = ρµ−1
2
√
2
π sinh(a) cos(aρ + π
4 (2µ −1))(1 + O (1
ρ))
(2.22)
as ρ →∞with ρ ∈R.
(iii) For any µ ∈C and δ ∈(0,π):
Qµ
ν (cosh(a)) =
√
π
2sinh(a)νµ−1
2eiµπ−a(ν+ 1
2 ) (1 + O ( 1
∣ν∣))
(2.23)
as ∣ν∣→∞with ∣arg(ν)∣< π −δ.
Proof. All three asymptotic estimates are basically stated at the beginning of §8 in
[VF01].
A proof of (2.21) can be found in [Göt65], which is also referred to in [VF01]. At
this point we want to remark that both sources [VF01] and [Göt65] state more general
results. They deal with asymptotic estimates for so-called generalised associated Legendre
functions of first and second kinds, denoted by P n,m
ν
(z) and Qn,m
ν
(z) respectively. For
n = m = µ these functions reduce to P µ
ν (z), respectively Qµ
ν(z).
We show how equation (2.22) can be deduced from (2.21). Let ρ ∈R and set ν = −1
2 +iρ
in equation (2.21) to obtain
P µ
−1
2 +iρ (cosh(a)) =
Γ(iρ + 1
2)
Γ(iρ + 1
2 −µ) (1
2 + iρ)
−1
2√
2
π sinh(a) ⋅
⋅1
2 (eiρa + e−πi(µ−1
2 )−iρa)(1 + O (1
ρ))
as ρ →∞. Now use the following well-known asymptotic estimate for the quotient of two
13


---

2 Preliminaries
gamma functions (see [TE51, formula (12)] or [Luk69, formula (11) on p. 33]):
Γ(z + α)
Γ(z + β) = zα−β (1 + O ( 1
∣z∣))
(2.24)
as z →∞with ∣arg(z)∣≤π −ϵ for some ϵ > 0. Thus
P µ
−1
2 +iρ (cosh(a)) = (iρ)µ (1
2 + iρ)
−1
2√
2
π sinh(a) ⋅
⋅1
2 (eiρa + e−πi(µ−1
2 )−iρa)(1 + O (1
ρ))
as ρ →∞. Further, we observe that
(1
2 + iρ)
−1
2 = (iρ)−1
2 (1 + 1
2iρ)
−1
2 = i−1
2ρ−1
2 (1 + O (1
ρ))
as ρ →∞. Hence,
P µ
−1
2 +iρ (cosh(a)) = ρµ−1
2
√
2
π sinh(a) ⋅iµ−1
2
2
(eiρa + e−πi(µ−1
2 )−iρa)(1 + O (1
ρ))
as ρ →∞. An easy calculation shows that
iµ−1
2
2
(eiρa + e−πi(µ−1
2 )−iρa) = 1
2ei π
2 (µ−1
2 ) (eiρa + e−πi(µ−1
2 )−iρa)
= 1
2 (eiρa+i π
4 (2µ−1) + e−i π
4 (2µ−1)−iρa)
= cos(aρ + π
4 (2µ −1)),
which closes the proof of equation (2.22).
Equation (2.23) is proven in Lemma 2 of §8 in [VF01], even though the statement of
the lemma as well as the proof given there contain some typos. The statement given in
[VF01] is mostly correct, but the restriction ∣arg(ν)∣< π −δ in the asymptotic estimate
misses there.
Lemma 2.20. Let ν ∈C and z,ω ∈(1,∞) be given. Further, let ˜z, ˜ω ∈(0,∞) be such
that
cosh(˜z) =
z
(z2 −1)
1/2,
cosh(˜ω) =
ω
(ω2 −1)
1/2.
(2.25)
Then
14


---

2 Preliminaries
1)
e−iπµP −µ
ν
(ω)Qµ
ν (z) = e−˜ωµ
2µ (eµ˜z + eiπ(ν+1)e−µ˜z)(1 + O ( 1
∣µ∣))
(2.26)
as ∣µ∣→∞with R(µ) > −1
2.
2)
sin(iπρ)
π
Q−iρ
ν
(z)Qiρ
ν (ω) = i
ρ cos(˜zρ −π
2 (ν + 1))⋅
⋅cos(˜ωρ −π
2 (ν + 1))(1 + O (1
ρ))
(2.27)
as ρ →∞with ρ ∈R.
Proof. Since cosh2(s) −sinh2(s) = 1 for all s ∈C, it follows that
1
√
sinh(˜z)
= (z2 −1)
1/4 ,
1
√
sinh(˜ω)
= (ω2 −1)
1/4 .
(2.28)
Let us consider situation 1) first.
When we use Whipple’s formulas (2.19), (2.20) and then (2.14), we get
e−iπµP −µ
ν
(ω)Qµ
ν (z)
= Γ(µ + ν + 1)
Γ(µ −ν)
ieiνπ
(z2 −1)
1/4 (ω2 −1)
1/4P
−ν−1
2
µ−1
2
(cosh(˜z))Q
−ν−1
2
µ−1
2 (cosh(˜ω)).
We can now apply the asymptotic estimates (2.21), (2.23) to the right-hand side of the
above equation. When we do so and then use the relation (2.28), we obtain for ∣µ∣→∞
with R(µ) > −1
2:
e−iπµP −µ
ν
(ω)Qµ
ν (z) = Γ(µ + 1
2)
Γ(µ −ν)
e−˜ωµ (µ −1
2)
−ν−1
2
√
µ + 1
2
(eµ˜z + eiπ(ν+1)e−µ˜z)(1 + O ( 1
∣µ∣))
= Γ(µ + 1
2)
Γ(µ −ν)
e−˜ωµµ−ν−3
2
2
(eµ˜z + eiπ(ν+1)e−µ˜z)(1 + O ( 1
∣µ∣)).
(2.29)
Applying the asymptotic estimate (2.24) for the quotient of two gamma functions, we get
Γ(µ + 1
2)
Γ(µ −ν) = µν+ 1
2 (1 + O ( 1
∣µ∣))
(2.30)
15


---

2 Preliminaries
as µ →∞with R(µ) > −1
2. Lastly, when we combine (2.30) and (2.29), we obtain
e−iπµP −µ
ν
(ω)Qµ
ν (z) = e−˜ωµ
2µ (eµ˜z + eiπ(ν+1)e−µ˜z)(1 + O ( 1
∣µ∣)),
as µ →∞with R(µ) > −1
2. This shows 1).
For 2), we first use Whipple’s formula (2.19) twice and (2.14) once, to obtain
Q−iρ
ν (z)Qiρ
ν (ω) = π
2 Γ(iρ + ν + 1)Γ(−iρ + ν + 1)
1
(z2 −1)
1/4 (ω2 −1)
1/4⋅
⋅P
−ν−1
2
−1
2 +iρ (cosh(˜z))P
−ν−1
2
−1
2 +iρ (cosh(˜ω)).
(2.31)
It is known (see e.g. [Leb65] on p. 15) that for any ε ∈(0,π) and α ∈C,
Γ(z + α) = e(z+α−1
2 ) log(z)−z+ 1
2 log(2π) (1 + O ( 1
∣z∣)),
(2.32)
as ∣z∣→∞with ∣arg(z)∣< π −ε.
Hence we obtain that, for ρ →∞with ρ ∈R,
Γ(±iρ + ν + 1) = e(±iρ+ν+ 1
2 ) log(±iρ)e∓iρ ⋅
√
2π (1 + O (1
ρ)),
and therefore
Γ(iρ + ν + 1)Γ(−iρ + ν + 1) = ρ2ν+1e−πρ ⋅2π (1 + O (1
ρ)).
(2.33)
On the other hand, when we use (2.22) and (2.28), we get
π
2
1
(z2 −1)
1/4 (ω2 −1)
1/4 ⋅P
−ν−1
2
−1
2 +iρ (cosh(˜z))P
−ν−1
2
−1
2 +iρ (cosh(˜ω))
= ρ−2ν−2 cos(˜zρ −π
2 (ν + 1))cos(˜ωρ −π
2 (ν + 1))(1 + O (1
ρ))
(2.34)
as ρ →∞with ρ ∈R. From (2.34), (2.33) and (2.31) we obtain
Q−iρ
ν (z)Qiρ
ν (ω) = 2π
ρ e−πρ cos(˜zρ −π
2 (ν + 1))cos(˜ωρ −π
2 (ν + 1))(1 + O (1
ρ))
as ρ →∞with ρ ∈R. Hence, as ρ →∞in R:
sin(πiρ)
π
Q−iρ
ν (z)Qiρ
ν (ω)
= (1 −e−2πρ) i
ρ cos(˜zρ −π
2 (ν + 1))cos(˜ωρ −π
2 (ν + 1))(1 + O (1
ρ))
16


---

2 Preliminaries
= i
ρ cos(˜zρ −π
2 (ν + 1))cos(˜ωρ −π
2 (ν + 1))(1 + O (1
ρ)).
In the last part of this section we want to discuss a class of integrals involving associated
Legendre functions of the second kind. We start with a rather technical lemma.
Lemma 2.21. Let ν ∈C with R(ν) > −1 and z,ω ∈C/(−∞,1]. Suppose further that we
are given the following situation:
(i) Let g be a meromorphic function on C and let S ⊂C denote the set of all poles
of g. Suppose that g is complex differentiable at all points on the imaginary axis,
possibly except for a simple pole at the origin, and that g is an odd function, i.e.
g(−s) = −g(s) for all s ∈C/S.
(ii) Fix some ε ∈(0,1) such that 0 < 2ε < 1 + R(ν) and B2ε(0) ∩S/{0} = ∅, where
B2ϵ(0) denotes the open disc of radius 2ε centered at the origin.
(iii) Let N ∶= (Nk)k∈N ⊂[1,∞) be an unbounded and monotonically increasing sequence.
Then there exists a function ϕ ∶N →C with limk→∞ϕ(k) = 0 and such that for any k ∈N
the following holds: If Ck denotes any injective and piecewise differentiable curve from
−iNk to iNk such that all other points on the curve lie in the domain {z ∈C ∶R(z) > 0}/S
(see Fig. 2.1), then we have:
2⎛
⎝
∑
p∈S(Ck)
Res(g;p)e−iπpP −p
ν (ω)Qp
ν(z)⎞
⎠+ Res(g;0)Pν(ω)Qν(z)
= 2
π
Nk
∫
ε
Nk
sin (πiρ)
π
g(iρ)Q−iρ
ν (z)Qiρ
ν (ω)dρ + 1
πi ∫
Ck
g(s)e−iπsP −s
ν (ω)Qs
ν(z)ds
+ ϕ(k),
(2.35)
where S (Ck) denotes the set of all poles of g contained in the bounded domain which is
enclosed by the imaginary axis and the curve Ck.
Proof. Let k ∈N and ω,z ∈C/(−∞,1] be arbitrary. First we close up the curve Ck in
two different ways and obtain two piecewise smooth curves γ1
k and γ2
k, as shown in Fig.
2.2. That is, γ1
k joins the point −iNk with iNk along Ck, then goes from iNk to i ε
Nk in a
straight line, moves around the origin from i ε
Nk to −i ε
Nk on a semicircle centered at the
origin and with positive orientation, and eventually joins −i ε
Nk to −iNk by a straight line.
The second curve is defined similarly as the first one, with only a single difference. The
curve γ2
k again moves around the origin from i ε
Nk to −i ε
Nk on a semicircle centered at the
origin, but now with the opposite orientation.
17


---

2 Preliminaries
−iNk
iNk
R(z)
I(z)
Ck
2ε
−1 −R(ν)
Figure 2.1: Situation of Lemma 2.21
By definition, both curves γ1
k and γ2
k can be written as a composition of the following
curves:
γ1
k = Ck + αk + β1
k + δk,
γ2
k = Ck + αk + β2
k + δk,
where
αk ∶[−Nk,−ε
Nk
] →C,
ρ ↦−ρi;
δk ∶[ ε
Nk
,Nk] →C,
ρ ↦−ρi;
β1
k ∶[0,π] →C,
θ ↦ε
Nk
ieiθ;
β2
k ∶[0,π] →C,
θ ↦ε
Nk
ie−iθ.
We observe that the function u ↦P −u
ν (ω)Qu
ν(z) is holomorphic on the half plane {u ∈C ∶
R(u) > −1 −R(ν)}. Hence, we can rewrite the left-hand side of (2.35) by using first the
residue theorem and then the above decomposition of γ1
k,γ2
k as follows:
2⎛
⎝
∑
p∈S(Ck)
Res(g;p)e−iπpP −p
ν (ω)Qp
ν (z)⎞
⎠+ Res(g;0)Pν (ω)Qν (z)
=
1
2πi ∮
γ1
k
g(s)e−iπsP −s
ν (ω)Qs
ν (z)ds + 1
2πi ∮
γ2
k
g(s)e−iπsP −s
ν (ω)Qs
ν (z)ds
= 1
πi ∫
αk
g(s)e−iπsP −s
ν (ω)Qs
ν (z)ds + 1
πi ∫
δk
g(s)e−iπsP −s
ν (ω)Qs
ν (z)ds
18


---

2 Preliminaries
iNk
i ε
Nk
−iNk
R(z)
I(z)
Ck
−1 −R(ν)
(a) The closed path γ1
k.
iNk
i ε
Nk
−iNk
R(z)
I(z)
Ck
−1 −R(ν)
(b) The closed path γ2
k.
Figure 2.2
+ 1
πi ∫
Ck
g(s)e−iπsP −s
ν (ω)Qs
ν (z)ds + ϕ(k),
(2.36)
with
ϕ(k) ∶=
1
2πi ∫
β1
k
g(s)e−iπsP −s
ν (ω)Qs
ν (z)ds + 1
2πi ∫
β2
k
g(s)e−iπsP −s
ν (ω)Qs
ν (z)ds.
(2.37)
We observe that we can sum up the first two summands of (2.36) as follows:
1
πi ∫
αk
g(s)e−iπsP −s
ν (ω)Qs
ν (z)ds + 1
πi ∫
δk
g(s)e−iπsP −s
ν (ω)Qs
ν (z)ds
= −1
π
−ε
Nk
∫
−Nk
g(−iρ)e−iπ(−iρ)P iρ
ν (ω)Q−iρ
ν
(z)dρ −1
π
Nk
∫
ε
Nk
g(−iρ)eiπ(iρ)P iρ
ν (ω)Q−iρ
ν
(z)dρ
= −1
π
Nk
∫
ε
Nk
g(iρ)e−iπ(iρ)P −iρ
ν
(ω)Qiρ
ν (z)dρ −1
π
Nk
∫
ε
Nk
g(−iρ)eiπ(iρ)P iρ
ν (ω)Q−iρ
ν
(z)dρ
= −1
π
Nk
∫
ε
Nk
g (iρ)(e−iπ(iρ)P −iρ
ν
(ω)Qiρ
ν (z) −eiπ(iρ)P iρ
ν (ω)Q−iρ
ν
(z))dρ,
where in the last equality we used that the function g is odd. Now we can use (2.18) to
19


---

2 Preliminaries
simplify the expression in paranthesis under the integral sign and obtain, in total:
1
πi ∫
αk
g(s)e−iπsP −s
ν (ω)Qs
ν (z)ds + 1
πi ∫
δk
g(s)e−iπsP −s
ν (ω)Qs
ν (z)ds
= 2
π
Nk
∫
ε
Nk
sin (iρπ)
π
g (iρ)Q−iρ
ν
(z)Qiρ
ν (ω)dρ.
(2.38)
Thus the claimed equation (2.35) follows from (2.36) together with (2.38).
It remains to show that limk→∞ϕ(k) = 0, where ϕ(k) is defined as in (2.37). When we
use the parametrisation of β1
k and β2
k given above, we obtain
ϕ(k) = 1
2π
π
∫
0
g (i ε
Nk
eiθ)e
−iπ(i ε
Nk eiθ)P
−i ε
Nk eiθ
ν
(ω) ⋅Q
i ε
Nk eiθ
ν
(z) ⋅(i ε
Nk
eiθ)dθ
−1
2π
π
∫
0
g (i ε
Nk
e−iθ)e
−iπ(i ε
Nk e−iθ)P
−i ε
Nk e−iθ
ν
(ω) ⋅Q
i ε
Nk e−iθ
ν
(z) ⋅(i ε
Nk
e−iθ)dθ.
By assumption, the meromorphic function g has either a simple pole at the origin or is
complex differentiable there. Hence the limit of the function sg(s) exists as s →0 and
is given by lims→0 sg(s) = Res(g;0) ∈C. Thus the integrand s ↦sg(s)e−iπsP −s
ν (ω)Qs
ν(z)
is continuous in Bε(0), in particular at the origin s = 0, and is bounded on Bε(0). By
Lebesgue’s dominated convergence theorem and since limk→∞Nk = ∞, we have
lim
k→∞ϕ(k) = 1
2π
π
∫
0
Res(g;0)Pν(ω)Qν(z)dθ −1
2π
π
∫
0
Res(g;0)Pν(ω)Qν(z)dθ
= 0.
The following corollary follows immediately from Lemma 2.21.
Corollary 2.22. Let ν ∈C with R(ν) > −1 and z,ω ∈C/(−∞,1]. Further, let g be a
meromorphic function with the same properties as in Lemma 2.21 and suppose:
1) There exists a sequence of curves (Ck)k∈N, each of them as in Lemma 2.21, and
such that
lim
k→∞∫
Ck
g(s)e−iπsP −s
ν (ω)Qs
ν(z)ds = 0.
(2.39)
2) The following integral converges in C:
20


---

2 Preliminaries
∞
∫
0
sin(πiρ)
π
g (iρ)Q−iρ
ν (z)Qiρ
ν (ω)dρ.
(2.40)
Then it follows that
2
π
∞
∫
0
sin(πiρ)
π
g (iρ)Q−iρ
ν (z)Qiρ
ν (ω)dρ
= lim
k→∞
⎛
⎝2
∑
p∈S(Ck)
Res(g;p)e−iπpP −p
ν (ω)Qp
ν(z)⎞
⎠+ Res(g;0)Pν(ω)Qν(z).
(2.41)
It is an interesting problem to investigate for which functions g as in Lemma 2.21 the
conditions 1) and 2) of Corollary 2.22 are satisfied. We will not pursue this problem in full
generality. Instead, since it is sufficient for our purposes, we will restrict the parameters
ω,z to real values.
The following lemma establishes a class of functions g for which condition 2) of Corollary
2.22 is satisfied.
Lemma 2.23. Let ν ∈C with R(ν) ∉{−1,−2,−3,...} (e.g. R(ν) > −1) and let z,ω ∈
(1,∞). Let g be as in Lemma 2.21.
(i) Suppose g(iρ) = O ( 1
ρ), as ρ →∞in R. Then the integral (2.40) is absolutely
convergent, and hence convergent.
(ii) Suppose there exists some constant C ∈C/{0} such that g(iρ) = C (1 + O ( 1
ρ)), as
ρ →∞in R. Then the integral (2.40) is convergent for ω ≠z, but divergent for
ω = z. Further, it is never absolutely convergent.
Proof. Let us abbreviate the integrand in (2.40) by
f(ρ) ∶= sin(πiρ)
π
g (iρ)Q−iρ
ν (z)Qiρ
ν (ω),
ρ ∈(0,∞).
The function f(ρ) is continuous on (0,∞) and can be extended continuously to [0,∞) by
the assumptions on g. Therefore, we only need to investigate how the integrand behaves
asymptotically as ρ →∞in R. We will see that both (i) and (ii) follow from (2.27) by
elementary calculations.
First consider case (i). Note that the function
R ∋ρ ↦cos(˜zρ −π
2 (ν + 1))cos(˜ωρ −π
2 (ν + 1)) ∈C
is bounded, where ˜z, ˜ω ∈(0,∞) are defined by (2.25). Thus it follows from (2.27) that
∣f(ρ)∣= O ( 1
ρ2)
21


---

2 Preliminaries
as ρ →∞in R. Hence the integral (2.40) is absolutely convergent.
Now consider case (ii). In this case it follows from (2.27) that
f(ρ) = C i
ρ cos(˜zρ −π
2 (ν + 1))cos(˜ωρ −π
2 (ν + 1))
´¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¶
=∶ψ(ρ)
(1 + O (1
ρ))
(2.42)
as ρ →∞in R. Note that z ≠ω if and only if ˜z ≠˜ω, which follows directly from (2.25).
We claim that if z ≠ω and K > 0, then the function ψ is integrable over the interval
[K,∞), where “integrable” is meant here in the sense that the integral converges. Fur-
thermore, ψ is not integrable over [K,∞) if z = ω, and for any values of z,ω ∈(1,∞) it
is not absolutely integrable over [K,∞).
Before we prove this claim, let us discuss why statement (ii) follows from this behaviour
of ψ. It follows from (2.42) that there exists a function φ ∶[Λ,∞) →R with Λ > 0 such
that for some constant D > 0 we have ∣φ(ρ)∣≤D
ρ and f(ρ) = ψ(ρ) + ψ(ρ) ⋅φ(ρ) for all
ρ ∈[Λ,∞). Hence there exists some constant E > 0 such that ∣ψ(ρ) ⋅φ(ρ)∣≤E
ρ2 for all
ρ ∈[Λ,∞) and the function ψ⋅φ is continuous because f,ψ are continuous and ψ⋅φ = f −ψ.
Thus ψ ⋅φ must be (absolutely) integrable over [Λ,∞). Therefore it follows from the
equation f = ψ + ψ ⋅φ that f is integrable over [Λ,∞) if and only if ψ is integrable over
[Λ,∞). This shows that if the above claim is true, then the function f is integrable if
z ≠ω, but it is not integrable if z = ω.
Further, if the above claim is true then the integral of f is never absolutely convergent.
This is easily seen, since it follows from (2.42) that
∣f(ρ)∣= ∣ψ(ρ)∣(1 + o(1))
as ρ →∞in R. Hence for any K > 0 the function ∣f∣is integrable over [K,∞) if and only
if ∣ψ∣is integrable over [K,∞).
It remains to prove the above claim for ψ. Let K > 0 and suppose z ≠ω and thus ˜z ≠˜ω.
To keep the notation short, let us introduce the following abbreviations:
c ∶= −π
2 (ν + 1);
q(ρ) ∶= cos(˜zρ + c)cos(˜ωρ + c).
One can easily show that the function q has the following antiderivative:
Q(ρ) ∶=
1
˜z2 −˜ω2 (˜z ⋅sin (˜zρ + c)cos(˜ωρ + c) −˜ω ⋅cos(˜zρ + c)sin (˜ωρ + c)).
This antiderivative is obviously bounded. Hence, using integration by parts,
∞
∫
K
ψ(ρ)dρ = lim
L→∞
⎛
⎝C ⋅i(Q(L)
L
−Q(K)
K
) + C ⋅i
L
∫
K
Q(ρ)
ρ2 dρ⎞
⎠
22


---

2 Preliminaries
= −C ⋅i⎛
⎝
Q(K)
K
−
∞
∫
K
Q(ρ)
ρ2 dρ⎞
⎠.
Observe that the remaining integral on the right-hand side is even absolutely convergent.
Thus the integral on the left-hand side must be convergent as well.
Suppose now z = ω, and thus ˜z = ˜ω. Again, one can easily show that for all τ ∈C the
function R ∋ρ ↦cos2 (˜zρ + τ) ∈C has the following antiderivative:
ρ ↦R(ρ;τ) ∶= sin (˜zρ + τ)cos(˜zρ + τ)
2˜z
+ ρ
2.
(2.43)
When we apply integration by parts, we obtain:
∞
∫
K
ψ(ρ)dρ = lim
L→∞
⎛
⎝C ⋅i(R(L;c)
L
−R(K;c)
K
)+C ⋅i
2˜z
L
∫
K
sin(˜zρ + c)cos(˜zρ + c)
ρ2
dρ
+C ⋅i
2
ln( L
K )⎞
⎠.
The right-hand side is not convergent as L →∞, because we have limL→∞ln( L
K) = ∞,
and all the other terms on the right-hand side converge to some complex number for
L →∞. Therefore, the left-hand side must be divergent as well. In other words, ψ is not
integrable if z = ω.
It remains to show that ψ is not absolutely integrable over [K,∞) for all values of
z,ω ∈(1,∞). It is easy to show that ∣cos(s)∣≥∣cos(R(s))∣for all s ∈C. Thus we have
∣ψ(ρ)∣≥∣C∣
ρ ⋅∣cos(˜zρ + R(c))∣⋅∣cos(˜ωρ + R(c))∣,
∀ρ ∈(0,∞).
If z = ω then we have for all L > K:
L
∫
K
∣ψ(ρ)∣dρ ≥∣C∣
L
∫
K
1
ρ ⋅cos2 (˜zρ + R(c))dρ
= ∣C∣(R(L;R(c))
L
−R(K;R(c))
K
) + ∣C∣
2˜z
L
∫
K
sin (˜zρ + c)cos(˜zρ + c)
ρ2
dρ
+ ∣C∣
2 ln( L
K )⎞
⎠,
where ρ ↦R(ρ;R(c)) is the function defined in (2.43) for τ = R(c). The right-hand side
diverges to ∞as L →∞. Thus ψ is also not absolutely integrable.
23


---

2 Preliminaries
Suppose now z ≠ω. Then we have for all L > K:
L
∫
K
∣ψ(ρ)∣dρ ≥∣C∣⋅
L
∫
K
1
ρ ⋅cos2 (˜zρ + R(c))cos2 (˜ωρ + R(c))dρ.
The integral on the right-hand side diverges to ∞as L →∞: An easy calculation
yields that the function R ∋ρ ↦cos2 (˜zρ + R(c))cos2 (˜ωρ + R(c)) ∈R has an elementary
antiderivative of the form
S(ρ) ∶= ρ
4 + u(ρ),
where u is a bounded function. An explicit formula for u is given by
u(ρ) ∶=
1
˜ω2 −˜z2
⎛
⎝
˜ω
2 cos2 (˜zρ + R(c))cos(˜ωρ + R(c))sin (˜ωρ + R(c))−
−˜z
2 cos2 (˜ωρ + R(c))cos(˜zρ + R(c))sin (˜zρ + R(c))+
+ ˜ω2
4˜z cos(˜zρ + R(c))sin(˜zρ + R(c))−
−˜z2
4˜ω cos(˜ωρ + R(c))sin (˜ωρ + R(c))⎞
⎠.
Thus, with integration by parts, we obtain
lim
L→∞
L
∫
K
1
ρ ⋅cos2 (˜zρ + R(c))cos2 (˜ωρ + R(c))dρ =
= lim
L→∞
⎛
⎝(S(L)
L
−S(K)
K
) +
L
∫
K
u(ρ)
ρ2 dρ + 1
4 ln( L
K )⎞
⎠= ∞.
Consequently, it follows that limL→∞∫
L
K ∣ψ(ρ)∣dρ = ∞and thus our proof is complete.
Now we want to consider functions g for which condition 1) of Corollary 2.22 is satisfied.
We consider only a special class of curves Ck, which is no problem because 1) is a condition
of existence for the Ck.
First we observe that there exists always a sequence (Nk) as in Lemma 2.21 such that
all curves Ck can be chosen as semicircles centered at the origin: If the function g is an
entire function or has at most finitely many poles, then this is clear. Suppose now that g
has infinitely many poles. By definition, all meromorphic functions have only isolated
poles, and hence the set of all poles is at most countable. Let {zi}∞
i=1 be the set of all poles
of g and let {∣zi∣}∞
i=1 be the set of all magnitudes of poles. Choose a sequence (Nk)k∈N as
in Lemma 2.21 such that Nk ∈[1,∞)/{∣zi∣}∞
i=1 for all k ∈N, and choose Ck as semicircles
centered at the origin with radius Nk.
24


---

2 Preliminaries
Lemma 2.24. Let g be a function as in Lemma 2.21. Let ν ∈C with R(ν) > −1 and
ω,z ∈(1,∞) with ω < z. Suppose that (Ck)k∈N, is a sequence of curves as in Lemma 2.21,
each of which is a semicircle centered at the origin. Suppose further that g is bounded
on the union of the images of all Ck. Then limk→∞∫Ck g(s)e−iπsP −s
ν (ω)Qs
ν(z)ds = 0. In
particular, condition 1) of Corollary 2.22 is satisfied.
Proof. Let ˜z, ˜ω ∈(0,∞) be associated with z,ω as in (2.25). Observe that the function
x ↦
x
(x2 −1)
1/2,
x > 1,
is monotonically decreasing on (1,∞); hence ˜z < ˜ω.
Let (Nk)∞
k=1 ⊂[1,∞) be the unbounded and monotonically increasing sequence such
that Ck runs from −iNk to iNk. Let Ck be parametrised as
Ck ∶[−π
2 , π
2 ] →C,
θ ↦Nk ⋅eiθ.
By assumption, there exists some A > 0 such that ∣g(s)∣≤A for all s ∈∪∞
k=1Ck([−π
2, π
2]).
Further, by (2.26) there exists some K > 0 such that for all s ∈C with R(s) ≥0 and
∣s∣> K:
∣e−iπsP −s
ν (ω)Qs
ν(z)∣≤1
∣s∣(∣e−s(˜ω−˜z)∣+ e−πI(ν) ⋅∣e−s(˜z+˜ω)∣) ≤1 + e−πI(ν)
∣s∣
⋅e−R(s)(˜ω−˜z).
(2.44)
Therefore there exist some q ∈N such that for all k ≥q:
RRRRRRRRRRRRR
∫
Ck
g(s)e−iπsP −s
ν (ω)Qs
ν(z)ds
RRRRRRRRRRRRR
≤(1 + e−πI(ν))A
π
2
∫
−π
2
e−Nk cos(θ)(˜ω−˜z)dθ
= (1 + e−πI(ν))2A
π
2
∫
0
e−Nk cos(θ)(˜ω−˜z)dθ.
To finish the proof of this corollary, we will show that the last integral converges to 0 as
k →∞.
Fix some δ ∈(0, π
2). Then
π
2
∫
0
e−Nk cos(θ)(˜ω−˜z)dθ =
π
2 −δ
∫
0
e−Nk cos(θ)(˜ω−˜z)dθ
´¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¶
=∶I1
+
π
2
∫
π
2 −δ
e−Nk cos(θ)(˜ω−˜z)dθ
´¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¶
=∶I2
.
The first term converges obviously to 0, since (recall ˜z < ˜ω)
I1 ≤(π
2 −δ)e−Nk cos( π
2 −δ)(˜ω−˜z) Ð→0
as k →∞.
25


---

2 Preliminaries
The second integral converges to 0 as well. In fact, with a simple substitution we get
I2 =
δ
∫
0
e−Nk cos(−θ+ π
2 )(˜ω−˜z)dθ =
δ
∫
0
e−Nk sin(θ)(˜ω−˜z)dθ.
Now observe that sin(θ) is concave on [0, π
2], and thus sin(θ) ≥2
πθ for all θ ∈[0, π
2]. In
particular e−Nk sin(θ)(˜ω−˜z) ≤e−Nk 2
π θ(˜ω−˜z). Hence
I2 ≤
δ
∫
0
e−Nk 2
π θ(˜ω−˜z)dθ =
π
2(˜ω −˜z)Nk
(1 −e−Nk 2
π δ(˜ω−˜z)) Ð→0
as k →∞.
To get an overview of the preceding discussion, we summarise the relevant parts in a
single theorem.
Theorem 2.25. Let z,ω ∈(1,∞) with ω < z. Let ν ∈C with R(ν) > −1. Suppose that g
is an odd and meromorphic function on C, which is complex differentiable at all points
on the imaginary axis except possibly with a simple pole at the origin. Suppose further:
(i) Either g(iρ) = O ( 1
ρ) as ρ →∞in R (in which case we will say “g is of type I”),
or there exists some constant C ∈C/{0} with g(iρ) = C (1 + O ( 1
ρ)) as ρ →∞in R
(“g is of type II”).
(ii) There exists an unbounded and monotonically increasing sequence (Nk)k∈N ⊂[1,∞)
such that g is bounded on ∪∞
k=1S1(Nk), where S1(Nk) denotes the circle of radius
Nk centered at the origin.
Then
2
π
∞
∫
0
sin(πiρ)
π
g (iρ)Q−iρ
ν (z)Qiρ
ν (ω)dρ
= lim
k→∞
⎛
⎝2
∑
p∈B+(Nk)
Res(g;p)e−iπpP −p
ν (ω)Qp
ν(z)⎞
⎠+ Res(g;0)Pν(ω)Qν(z),
(2.45)
where B+ (Nk) ∶= {z ∈C ∶∣z∣< Nk, R(z) > 0}.
Further, we know that the integral on the left-hand side of (2.45) is absolutely convergent
for all z,ω ∈(1,∞) and ν ∈C with R(ν) ∉{−1,−2,−3,...}, if g is of type I. If, instead, g
is of type II, then this integral is convergent if and only if z ≠ω, and it is never absolutely
convergent.
With this theorem, we can solve many integrals involving associated Legendre functions.
26


---

2 Preliminaries
Example 2.26. Let ν ∈C with R(ν) > −1 and ω,z ∈(1,∞) with ω < z. The following
examples of functions g satisfy ∣g(s)∣= O ( 1
∣s∣) as ∣s∣→∞with s ∈C. In particular, these
g will satisfy the above conditions (i),(ii) (more precisely, they are of type I) so we
can apply Theorem 2.25 to solve the corresponding integrals. In order to simplify the
integrands, we use the identity sin(is) = isinh(s) for s ∈C.
(a) If g(s) = 1
s, then:
2
π
∞
∫
0
sinh(πρ)
π
⋅1
ρQ−iρ
ν (z)Qiρ
ν (ω)dρ = Pν(ω)Qν(z).
(2.46)
(b) If g(s) =
s
(s−1)(s+1) =
s
s2−1, then:
2
π
∞
∫
0
sinh(πρ)
π
⋅
ρ
ρ2 + 1Q−iρ
ν (z)Qiρ
ν (ω)dρ = −P −1
ν (ω)Q1
ν(z).
(c) We can generalise the above examples. Let H>0 = {s ∈C ∣R(s) > 0}. For any n ∈N0
and pairwise different a1,...,an ∈H>0, we define the following polynomials:
p(s ∣a1,...,an) ∶=
n
∏
i=1
(s −ai)(s + ai) =
n
∏
i=1
(s2 −a2
i ).
As usual we define the empty product as 1, e.g.
1
∏
i=1
i≠1
(...) ∶= 1,
0
∏
i=1
(...) ∶= 1.
Thus, if n = 0, then p(s ∣a1,...,an) ∶= 1.
Now let m,n ∈N0 be given. We fix pairwise different b1,...,bm ∈H>0 and pairwise
different a1,...,an ∈H>0. Then the following functions satisfy the conditions of
Theorem 2.25:
g1(s) ∶= 1
s ⋅p(s ∣a1,...,an)
p(s ∣b1,...,bm)
if m ≥n;
g2(s) ∶= s ⋅p(s ∣a1,...,an)
p(s ∣b1,...,bm),
if m > n.
For g1 we obtain the integrals
2
π
∞
∫
0
sinh(πρ)
π
⋅(−1)n+m
ρ
⋅
⎛
⎜⎜⎜
⎝
n
∏
i=1(ρ2 + a2
i )
m
∏
i=1(ρ2 + b2
i )
⎞
⎟⎟⎟
⎠
Q−iρ
ν (z)Qiρ
ν (ω)dρ =
27


---

2 Preliminaries
⎛
⎜⎜⎜⎜⎜
⎝
m
∑
k=1
⎛
⎜⎜⎜⎜⎜
⎝
n
∏
i=1(b2
k −a2
i )
m
∏
i=1
i≠k
(b2
k −b2
i )
⎞
⎟⎟⎟⎟⎟
⎠
e−iπbk
bk
P −bk
ν
(ω)Qbk
ν (z)
⎞
⎟⎟⎟⎟⎟
⎠
+ (−1)n+m
⎛
⎜⎜⎜
⎝
n
∏
i=1a2
i
m
∏
i=1b2
i
⎞
⎟⎟⎟
⎠
Pν(ω)Qν(z).
For g2 we obtain
2
π
∞
∫
0
sinh(πρ)
π
(−1)n+m ⋅ρ ⋅
⎛
⎜⎜⎜
⎝
n
∏
i=1(ρ2 + a2
i )
m
∏
i=1(ρ2 + b2
i )
⎞
⎟⎟⎟
⎠
Q−iρ
ν (z)Qiρ
ν (ω)dρ =
−
⎛
⎜⎜⎜⎜⎜
⎝
m
∑
k=1
⎛
⎜⎜⎜⎜⎜
⎝
n
∏
i=1(b2
k −a2
i )
m
∏
i=1
i≠k
(b2
k −b2
i )
⎞
⎟⎟⎟⎟⎟
⎠
e−iπbkP −bk
ν
(ω)Qbk
ν (z)
⎞
⎟⎟⎟⎟⎟
⎠
.
(d) Let c ∈H>0, n ∈N, m ∈N0 such that 2m + 1 < 4n, and set g(s) ∶=
s2m+1
(s−c)2n(s+c)2n. The
only poles of g are of order 2n at the points c and −c. In order to compute the
residue of g at c, note that
Res(g;c) =
1
(2n −1)! ⋅d2n−1
ds2n−1∣s=c
{ s2m+1
(s + c)2n},
Res(g;−c) =
1
(2n −1)! ⋅d2n−1
ds2n−1∣s=−c
{ s2m+1
(s −c)2n},
and thus we have Res(g;c) = Res(g;−c). Consider the curve SR ∶[0,2π] ∋θ ↦
R ⋅eiθ ∈C with R > 0. Then we have by the residue theorem:
2 ⋅Res(g;c) =
1
2πi lim
R→∞∫
SR
g(s)ds
= 1
2π lim
R→∞
2π
∫
0
R2m+1
R4n−1 ⋅
ei(2m+2)θ
(eiθ −c
R)
2n (eiθ + c
R)
2ndθ =
⎧⎪⎪⎨⎪⎪⎩
0, if 2m + 1 < 4n −1
1, if 2m + 1 = 4n −1.
Thus we have
2
π
∞
∫
0
sinh(πρ)
π
⋅(−1)m+1ρ2m+1
(ρ2 + c2)2n Q−iρ
ν (z)Qiρ
ν (ω)dρ =
=
⎧⎪⎪⎨⎪⎪⎩
0,
if 2m + 1 < 4n −1
e−iπcP −c
ν (ω)Qc
ν(z),
if 2m + 1 = 4n −1.
28


---

2 Preliminaries
Remark. As we will show in the next chapter (see Lemma 3.13 (ii)), equation (2.46) is
also valid if ω = z and ν ∈(−1,∞). That case will be very useful as we shall see.
We want to stress a special case of the previous theorem by the following corollary.
Corollary 2.27. Let ν ∈C with R(ν) > −1 and ω,z ∈(1,∞) with ω < z. Let f ∶C →C
be an entire and even function, i.e. f(s) = f(−s) for all s ∈C. Consider the function
g(s) ∶=
π
sin(πs) ⋅f(s),
and the sequence (Nk)k∈N with Nk ∶= k + 1
2. Suppose that the conditions (i) and (ii) of
Theorem 2.25 are satisfied with this particular g and sequence (Nk)k∈N. Then we have
2
π
∞
∫
0
f (iρ)Q−iρ
ν (z)Qiρ
ν (ω)dρ = 2(
∞
∑
m=1
f(m)P −m
ν
(ω)Qm
ν (z)) + f(0)Pν(ω)Qν(z).
(2.47)
Proof. Observe that s ↦
π
sin(πs) is an odd function and meromorphic on C. The only
singularities are simple poles at all integer points p ∈Z with residue Res(s ↦
π
sin(πs);p) =
(−1)p. Thus g satisfies the assumptions of Theorem 2.25 with Res(g;p) = (−1)p f(p).
Therefore (2.47) follows when we apply (2.45) to this case.
Let us apply Corollary 2.27 to solve an important integral, which will reappear in the
next chapter.
Example 2.28. Let ν ∈C with R(ν) > −1 and ω,z ∈(1,∞) with ω < z. Further, let
f(s) ∶= cos(s ⋅(π −θ)), with θ ∈[0,2π). We set g(s) ∶=
π
sin(πs) ⋅f(s) and Nk ∶= k + 1
2 as in
Corollary 2.27. We first check if the conditions (i) and (ii) of Theorem 2.25 are satisfied.
Note that for ρ ∈R we have
g(iρ) = π
i ⋅cosh((π −θ)ρ)
sinh(πρ)
= π
i ⋅e−θρ + e−(2π−θ)ρ
1 −e−2πρ
.
If θ ∈(0,2π) then this is in O(e−αρ) as ρ →∞with α ∶= min{θ,2π −θ} > 0. In particular,
it is in O ( 1
ρ) as ρ →∞, so g is of type I. If θ = 0, then
g(iρ) = π
i ⋅1 + e−2πρ
1 −e−2πρ = π
i ⋅(1 + 2e−2πρ
1 −e−2πρ).
In particular, g is of type II (with C ∶= π
i in Theorem 2.25 (i)). Thus, condition (i) of
Theorem 2.25 is satisfied.
Note that g is bounded on the set ∪∞
k=1S1(Nk) if and only if g2 is bounded on this set.
Furthermore, if x ∶= R(s), y ∶= I(s) so that s = x + iy, then a straightforward calculation
shows:
∣g(s)∣2 = π2 ⋅∣cos((π −θ)(x + iy))∣2
∣sin(π(x + iy))∣2
= π2 ⋅cosh(2(π −θ)y) + cos(2(π −θ)x)
cosh(2πy) −cos(2πx)
.
29


---

2 Preliminaries
Let y0 > 0 be such that
{s ∈S1(Nk)∣∣I(s)∣≤y0 } ⊂{s ∈S1(Nk)∣∣R(s)∣∈[k + 1
3,k + 1
2]}
for all k ∈N (or equivalently, for k = 1). Then on ∪∞
k=1{s ∈S1(Nk) ∣∣I(s)∣≤y0 } we have
cos(2πx) ∈[−1,−1
2] and thus
∣g(s)∣2 ≤2π2 ⋅cosh(2(π −θ)y)
cosh(2πy)
≤2π2.
On {s ∈C ∣∣I(s)∣≥y0 } we have
∣g(s)∣2 ≤π2 ⋅cosh(2(π −θ)y) + 1
cosh(2πy) −1
.
Since y ↦π2 ⋅cosh(2(π−θ)y)+1
cosh(2πy)−1
has a limit for y →∞it is bounded on [y0,∞). We conclude
that g2 is bounded on {s ∈C ∣∣I(s)∣≥y0 }, too. In particular, condition (ii) of Theorem
2.25 is satisfied by the function g with the above Nk. Therefore, by Corollary 2.27 we get:
2
π
∞
∫
0
cosh(ρ(π −θ))Q−iρ
ν (z)Qiρ
ν (ω)dρ
= 2(
∞
∑
m=1
cos(m(π −θ))P −m
ν
(ω)Qm
ν (z)) + Pν(ω)Qν(z)
= 2(
∞
∑
m=1
(−1)m cos(mθ)P −m
ν
(ω)Qm
ν (z)) + Pν(ω)Qν(z)
= Qν (ωz −
√
ω2 −1
√
z2 −1cos(θ)),
where the last equality is a classical addition formula (see e.g. [GR07, 8.795 2]).
In the above example we needed to assume ω < z in order to apply Corollary 2.27,
but it turns out that the above formula is also valid for more general values of ω and z.
Before we generalise that formula, we will prove some estimates in the following lemma,
which will also be useful later.
Lemma 2.29. Let ω,z ∈(1,∞) and ρ ∈[0,∞) be arbitrary.
(i) For all ν ∈C with R(ν) ≥−1
2:
∣Q−iρ
ν (z)Qiρ
ν (ω)∣≤
π4
√
z −1 ⋅
√
ω −1
⋅(∣ν∣+ 1 + ρ)2∣ν∣+1
∣Γ(ν + 1)∣2
⋅e−πρ.
(2.48)
30


---

2 Preliminaries
(ii) For all ν ∈C with R(ν) ≥0:
∣Q−iρ
ν (z)Qiρ
ν (ω)∣≤ln(z + 1
z −1)ln(ω + 1
ω −1) ⋅π2 (∣ν∣+ 1 + ρ)2∣ν∣+1
∣Γ(ν + 1)∣2
⋅e−πρ.
(2.49)
(iii) For all ν ∈C with −1 < R(ν) < −1
2:
∣Q−iρ
ν (z)Qiρ
ν (ω)∣≤
π3e
1
3(R(ν)+1)
∣Γ(ν + 1)∣2 ⋅((z −1)(ω −1))R(ν)+1(R(ν) + 1)1−2R(ν) e−πρ. (2.50)
Proof. Let ω,z ∈(1,∞), ρ ∈[0,∞), and ν ∈C with R(ν) > −1 be given. From [EMOT53,
formula (5) on p. 155] we know that for all µ ∈C with R(µ) ≥0:
Qµ
ν(z) = eµπi ⋅
1
2ν+1 ⋅Γ(ν + 1 + µ)
Γ(ν + 1)
⋅
1
(z2 −1)
µ
2 ⋅
π
∫
0
sin(t)2ν+1
(z + cos(t))−µ+ν+1 dt.
(2.51)
Hence,
∣Q−iρ
ν (z)Qiρ
ν (ω)∣≤
1
4R(ν)+1 ⋅∣Γ(ν + 1 + iρ)Γ(ν + 1 −iρ)∣
∣Γ(ν + 1)∣2
⋅
π
∫
0
sin(t)2R(ν)+1
(z + cos(t))R(ν)+1 dt⋅
⋅
π
∫
0
sin(t)2R(ν)+1
(ω + cos(t))R(ν)+1 dt.
(2.52)
(i). Suppose R(ν) ≥−1
2. Then we can rewrite the integrals appearing above as follows:
π
∫
0
sin(t)2R(ν)+1
(z + cos(t))R(ν)+1 dt =
π
∫
0
(1 −cos2(t)
z + cos(t) )
R(ν)+ 1
2
⋅
1
√
z + cos(t)
dt
=
π
∫
0
(1 + cos(t)
z + cos(t))
R(ν)+ 1
2
⋅(1 −cos(t))R(ν)+ 1
2
√
z + cos(t)
dt.
(2.53)
Using the estimates 0 ≤1+cos(t)
z+cos(t) < 1, 0 ≤1 −cos(t) ≤2, and 0 <
1
√
z+cos(t) ≤
1
√
z−1 for all
t ∈[0,π], we obtain from (2.53):
π
∫
0
sin(t)2R(ν)+1
(z + cos(t))R(ν)+1 dt ≤2R(ν)+ 1
2 ⋅
π
√
z −1
.
(2.54)
Hence, from (2.52) and (2.54) we get
∣Q−iρ
ν (z)Qiρ
ν (ω)∣≤
π2
√
z −1 ⋅
√
ω −1
⋅∣Γ(ν + 1 + iρ)Γ(ν + 1 −iρ)∣
2 ⋅∣Γ(ν + 1)∣2
.
(2.55)
31


---

2 Preliminaries
Moreover, it is well-known (see [OLBC10, formula 5.6.9 on p. 138]) that for all z ∈C
with R(z) > 0:
∣Γ(z)∣≤
√
2π ⋅∣z∣R(z)−1
2 ⋅e−π
2 ∣I(z)∣⋅e
1
6∣z∣.
(2.56)
Thus,
∣Γ(ν + 1 + iρ)Γ(ν + 1 −iρ)∣≤2πe
2
3 ⋅(∣ν∣+ 1 + ρ)2R(ν)+1 ⋅e−π
2 (∣I(ν)+ρ∣+∣I(ν)−ρ∣)
≤2π2 ⋅(∣ν∣+ 1 + ρ)2∣ν∣+1 ⋅e−πρ.
(2.57)
Hence, (i) follows from (2.57) and (2.55).
(ii). Suppose R(ν) ≥0. Similar as above, we can estimate the integrals on the right-hand
side of (2.52) as follows:
π
∫
0
sin(t)2R(ν)+1
(z + cos(t))R(ν)+1 dt =
π
∫
0
(1 + cos(t)
z + cos(t))
R(ν)
⋅(1 −cos(t))R(ν) ⋅
sin(t)
z + cos(t) dt
≤2R(ν)
π
∫
0
sin(t)
z + cos(t) dt = 2R(ν) ln(z + 1
z −1).
Hence, (ii) follows from the above estimate combined with (2.52) and (2.57).
(iii). Suppose −1 < R(ν) < −1
2, and thus −1 < 2R(ν) + 1 < 0. In that case, we estimate
the integrals on the right-hand side of (2.52) as follows:
π
∫
0
sin(t)2R(ν)+1
(z + cos(t))R(ν)+1 dt ≤
1
(z −1)R(ν)+1 ∫
π
0
sin(t)2R(ν)+1 dt
=
2
(z −1)R(ν)+1 ∫
π
2
0
sin(t)2R(ν)+1 dt.
Note that [0, π
2] ∋t ↦sin(t) ∈R is concave and thus sin(t) ≥2
πt. Hence, from the above
estimate, we obtain
π
∫
0
sin(t)2R(ν)+1
(z + cos(t))R(ν)+1 dt ≤
2
(z −1)R(ν)+1 ∫
π
2
0
( 2
πt)
2R(ν)+1
dt
=
π
2 ⋅(z −1)R(ν)+1(R(ν) + 1).
Using that upper bound and the estimate (2.52) we have
∣Q−iρ
ν (z)Qiρ
ν (ω)∣≤
π2
2(z −1)R(ν)+1(ω −1)R(ν)+1(R(ν) + 1)2 ⋅∣Γ(ν + 1 + iρ)Γ(ν + 1 −iρ)∣
∣Γ(ν + 1)∣2
.
32


---

2 Preliminaries
Furthermore, from (2.56) we obtain
∣Γ(ν + 1 + iρ)Γ(ν + 1 −iρ)∣≤(2π)e
1
3(R(ν)+1)(R(ν) + 1)2R(ν)+1e−πρ,
and therefore
∣Q−iρ
ν (z)Qiρ
ν (ω)∣≤
π3e
1
3(R(ν)+1)
∣Γ(ν + 1)∣2(z −1)R(ν)+1(ω −1)R(ν)+1(R(ν) + 1)1−2R(ν) ⋅e−πρ.
Corollary 2.30. Let ν ∈C with R(ν) > −1, θ ∈[0,2π) and ω,z ∈(1,∞) such that ω ≠z.
Then
2
π
∞
∫
0
cosh(ρ(π −θ))Q−iρ
ν (z)Qiρ
ν (ω)dρ = Qν (ωz −
√
ω2 −1
√
z2 −1cos(θ)).
(2.58)
Furthermore, the above equality holds for all θ ∈(0,2π) and ω = z ∈(1,∞).
Proof. Suppose θ ∈[0,2π) and ω,z ∈(1,∞) such that ω ≠z. For ω < z the proof was given
in Example 2.28. In addition to that, observe that both sides of (2.58) are symmetric in
the variables ω,z. The right-hand side is obviously symmetric in those variables, and the
left-hand side is symmetric since the term Q−iρ
ν (z)Qiρ
ν (ω) of the integrand is symmetric
due to (2.17). Hence the equation holds also if z < ω.
Now suppose that we have θ ∈(0,2π) and ω = z ∈(1,∞). Observe that the function
on the right-hand side of (2.58) is continuous in z ∈(1,∞) and thus for any sequence
(zn)n∈N ⊂(1,∞) with zn ≠z for all n ∈N and limn→∞zn = z we have:
Qν (ωz −
√
ω2 −1
√
z2 −1cos(θ)) = lim
n→∞Qν (ωzn −
√
ω2 −1
√
z2n −1cos(θ))
= lim
n→∞
2
π
∞
∫
0
cosh(ρ(π −θ))Q−iρ
ν (zn)Qiρ
ν (ω)dρ
= 2
π
∞
∫
0
cosh(ρ(π −θ))Q−iρ
ν (z)Qiρ
ν (ω)dρ,
where we obtain the last equality by Lebesgue’s dominated convergence theorem: The
integrand is continuous with respect to z ∈(1,∞), and the sequence of integrands is
dominated by some integrable function due to Lemma 2.29 (i) and (iii). In fact, by
Lemma 2.29 and the estimate cosh(ρ(π −θ)) ≤e ρ∣π−θ∣for all ρ ≥0, there exist C,ε > 0
such that for all ρ ≥0 and n ∈N: ∣cosh(ρ(π −θ))Q−iρ
ν (zn)Qiρ
ν (ω)∣≤C ⋅e−ρε. This upper
bound is obviously integrable over ρ ∈[0,∞).
Remark. One can consider the above integrals as certain so-called generalised Mehler
transforms (see e.g. [OH61]). One only needs to apply Whipple’s formula (2.19) to
the term Q−iρ
ν (z) on the left-hand side of (2.45). The corresponding ordinary Mehler
33


---

2 Preliminaries
transform is obtained if we additionally set ν = −1
2. Note that if we apply Whipple’s
formula (2.19) also to the term Qiρ
ν (ω) on the left-hand side of (2.45), then some terms
under the integral cancel each other out and the integrand becomes shorter. In particular,
if ν = −1
2, then the integrand can be simplified further due to the formula (see [GR07,
8.334 2])
Γ(1
2 + iρ)Γ(1
2 −iρ) =
π
cos(πiρ),
ρ ∈R.
Lemma 2.31. Let ω,z ∈(1,∞). Further, let h ∶[0,∞) →∞be continuous such that
there exists some ε > 0 with h(ρ) = O(e(π−ε)ρ) as ρ →∞. Then the function
F ∶H>−1
2 ∋ν ↦
∞
∫
0
Q−iρ
ν (z)Qiρ
ν (ω)h(ρ)dρ ∈C
is holomorphic on H>−1
2 = {z ∈C ∣R(z) > −1
2 }.
Proof. Let f(ν,ρ) ∶= Q−iρ
ν (z)Qiρ
ν (ω)h(ρ) for all ν ∈H>−1
2 and ρ ∈[0,∞). Because of [Els09,
Satz 5.8 on p. 148] it suffices to show for all non-empty compact sets K ⊂H>−1
2 the
existence of some integrable function gK ∶[0,∞) →R with supν∈K ∣f(ν,ρ)∣≤gK(ρ) for
all ρ ∈[0,∞). Note that the other conditions of [Els09, Satz 5.8 on p. 148] are obviously
satisfied by f, namely f(ν,⋅) is integrable for all ν ∈H>−1
2 because of Theorem 2.25 and
f(⋅,ρ) is holomorphic on H>−1
2 for all ρ ≥0.
Let K ⊂H>−1
2 be an arbitrary non-empty compact set. From (2.48) and the assumptions
on h, there exist constants ˜C,ε > 0 such that for all ν ∈K and ρ ∈[0,∞):
∣f(ν,ρ)∣≤˜C ⋅(∣ν∣+ 1 + ρ)2∣ν∣+1
∣Γ(ν + 1)∣2
⋅e−ερ.
(2.59)
With D ∶= supν∈K {
1
∣Γ(ν+1)∣2}, M ∶= supν∈K{∣ν∣} we have for all ν ∈K and ρ ∈[0,∞):
∣f(ν,ρ)∣≤˜CD (M + 1 + ρ)2M+1 ⋅e−ερ ≤C ⋅e−ε
2 ρ =∶gK(ρ),
where C ∶= supρ≥0{ ˜CD(M + 1 + ρ)2M+1 ⋅e−ε
2 ρ} ∈(0,∞). That function gK is obviously
integrable over [0,∞) and satisfies supν∈K ∣f(ν,ρ)∣≤gK(ρ) for all ρ ∈[0,∞). Hence, F
must be holomorphic.
Lemma 2.32. Let ν ∈(0,∞) be fixed.
(i) For any b ∈(0,∞) there exist constants C,D > 0 (depending on ν and b) such that
for all a ∈(0,∞) and µ > 0:
∣P −µ
ν (cosh(a))Qµ
ν(cosh(b))∣≤Ce(ν+ 1
2 )a ⋅µν+ 1
2 ⋅(D ⋅sinh(a
2))
µ
.
(2.60)
34


---

2 Preliminaries
(ii) For all a,b ∈(0,∞)
∣Pν(cosh(a))Qν(cosh(b))∣≤eν(a−b) ⋅e
a
2 ln(cosh(b) + 1
cosh(b) −1).
(2.61)
Proof. From [GR07, formula 8.715 1] we know that for all µ ≥0 and a > 0:
P −µ
ν (cosh(a)) =
√
2
√π sinh(a)µ ⋅Γ( 1
2 + µ)
a
∫
0
cosh((ν + 1
2)x) ⋅(cosh(a) −cosh(x))µ−1
2 dx,
and therefore
∣P −µ
ν (cosh(a))∣≤
√
2
π ⋅e(ν+ 1
2 )a(cosh(a) −1)µ
sinh(a)µ ⋅∣Γ( 1
2 + µ)∣
a
∫
0
1
√
cosh(a) −cosh(x)
dx.
(2.62)
Since cosh(t) = 2sinh2 ( t
2) + 1 for all t ∈R, the above integral can be estimated as follows:
a
∫
0
1
√
cosh(a) −cosh(x)
dx = 1
√
2
a
∫
0
1
√
sinh2 ( a
2) −sinh2 ( x
2)
dx
≤
1
√
2sinh( a
2)
a
∫
0
1
√
sinh( a
2) −sinh( x
2)
dx,
and using sinh( a
2) −sinh ( x
2) ≥a
2 −x
2 for all x ∈(0,a) we obtain:
a
∫
0
1
√
cosh(a) −cosh(x)
dx ≤
1
√
sinh( a
2)
a
∫
0
1
√a −x dx = 2
√
a
sinh( a
2) ≤2
√
2.
(2.63)
Because of (2.62) and (2.63) we have for all µ ≥0 and a > 0:
∣P −µ
ν (cosh(a))∣≤3 ⋅e(ν+ 1
2 )a
∣Γ( 1
2 + µ)∣⋅(cosh(a) −1
sinh(a)
)
µ
≤3 ⋅e(ν+ 1
2 )a
∣Γ( 1
2 + µ)∣⋅(sinh(a
2))
µ
,
(2.64)
where, for the last equality, we used cosh(a)−1
sinh(a) =
2 sinh2( a
2 )
sinh(a)
< sinh( a
2).
Further, from (2.51) (or see [EMOT53, formula (5) on p. 155]), for all µ ≥0 and b > 0:
∣Qµ
ν(cosh(b))∣=
Γ(ν + 1 + µ)
Γ(ν + 1)2ν+1 sinh(b)µ
π
∫
0
sin(t)2ν+1 ⋅(cosh(b) + cos(t))µ
(cosh(b) + cos(t))ν+1
dt.
(2.65)
(i). We will estimate the integrand given above. Note that for any z > 1 the function
(−1,1) ∋x ↦1−x2
z+x ∈R has a global maximum at x = −z +
√
z2 −1, where the maximal
35


---

2 Preliminaries
value is 2z −2
√
z2 −1. Hence, with z ∶= cosh(b) we have for all t ∈(0,π)
sin(t)2ν+1
(cosh(b) + cos(t))ν+1 = (
1 −cos2(t)
cosh(b) + cos(t))
ν
⋅
sin(t)
cosh(b) + cos(t) ≤2νe−bν sin(t)
(cosh(b) −1).
(2.66)
Thus, we can estimate the integral on the right-hand side of (2.65) as follows:
π
∫
0
sin(t)2ν+1 ⋅(cosh(b) + cos(t))µ
(cosh(b) + cos(t))ν+1
dt ≤
2ν
(cosh(b) −1)
π
∫
0
sin(t)(cosh(b) + cos(t))µ dt
=
2ν
(cosh(b) −1) ⋅(cosh(b) + 1)µ+1 −(cosh(b) −1)µ+1
µ + 1
≤2ν+1 cosh(b)µ+12µ
(cosh(b) −1)
.
Using (2.65) we have
∣Qµ
ν(cosh(b))∣≤Γ(ν + 1 + µ)
Γ(ν + 1)
⋅
cosh(b)
cosh(b) −1 ⋅(2coth(b))µ .
(2.67)
Let ˜C > 0 be some constant such that ∣Γ(ν+1+µ)
Γ( 1
2 +µ) ∣≤˜C ⋅µν+ 1
2 for all µ > 0, where such
a constant exists because of (2.24). If we set C ∶= ˜C ⋅
3 cosh(b)
(cosh(b)−1)Γ(ν+1) and D ∶= 2coth(b),
then the lemma follows from (2.64) and (2.67).
(ii). Similarly, for µ = 0 we obtain from equation (2.65):
∣Qν(cosh(b))∣=
1
2ν+1
π
∫
0
sin(t)2ν+1
(cosh(b) + cos(t))ν+1 dt
=
1
2ν+1
π
∫
0
(
1 −cos2(t)
cosh(b) + cos(t))
ν
sin(t)
cosh(b) + cos(t) dt
≤e−bν
2
π
∫
0
sin(t)
cosh(b) + cos(t) dt
= e−bν
2
ln(cosh(b) + 1
cosh(b) −1).
The statement follows from the above estimate together with (2.64).
36


---

3 Spectral invariants for polygons
The main purpose of this chapter is to compute the heat invariants for any hyperbolic
polygon. Let us start with some basic definitions to clarify the terminology.
Definition 3.1. A hyperbolic polygon is defined as a relatively compact domain in the
hyperbolic plane H2 whose boundary is a union of finitely many geodesic segments.
Analogously, the terms Euclidean polygon and spherical polygon are defined as relatively
compact domains in the Euclidean plane R2 and the unit sphere S2, respectively, with a
piecewise geodesic boundary.
We will have more to say about polygons below, in particular about the definition of
edges, vertices and angles of a polygon. But for the moment it is sufficient to think of
all these notions on an intuitive level as we are used to. The following subsets of the
hyperbolic plane will play an important role for our purposes.
Definition 3.2. A domain W ⊂H2 is called a hyperbolic wedge if there exist some
γ ∈(0,2π] and polar coordinates (a,α) with respect to some base point P ∈H2 (where
the angle α is measured with respect to a chosen geodesic ray emanating from P and a
chosen orientation), such that W is parametrised as
W = {(a,α) ∣0 < a < ∞, 0 < α < γ }.
The point P is called the vertex and γ is called the angle of the wedge. Thus, loosely
speaking, a wedge is any domain bounded by two geodesic rays emanating from one
point, its vertex.
Again, the terms Euclidean wedge and spherical wedge are defined analogously. Note
that spherical wedges are relatively compact.
Before we start our study of the heat invariants for hyperbolic polygons, we want to
informally point out some previous publications related to our problem. Most of the works
in this direction deal with Euclidean polygons, such that the study of spectral invariants
for Euclidean polygons has a long and also intense history. Early publications focusing
more or less on Euclidean polygons include [Wey11], [CH53], [BB62], [Fed63], [Kac66],
[MS67]. Regarding the heat invariants for Euclidean polygons, a rigorous and complete
investigation can be found in [vdBS88]. M. van den Berg and S. Srisatkunarajah proved
that the heat trace ZΩR(t) for any Euclidean polygon ΩR with M vertices and interior
angles γ1,...,γM has an asymptotic expansion of the form
ZΩR(t) = ∣ΩR∣
4πt −∣∂ΩR∣
8
√
πt
+
M
∑
i=1
π2 −γ2
i
24πγi
+ O (e−c
t ),
(3.1)
37


---

3 Spectral invariants for polygons
as t ↘0, with some constant c > 0. Their approach to prove this asymptotic estimate was
basically a combination of two previous results. Firstly, they used the so-called principle of
not feeling the boundary due to M. Kac (see [Kac66]). By this principle Kac approximated
the heat kernel KΩR(x,x;t) by simpler functions with the same asymptotic expansion
as t ↘0. Roughly speaking, if the point x ∈ΩR is near to a vertex of the polygon, then
the heat kernel KΩR is approximated by the heat kernel of a Euclidean wedge; if the
point x ∈ΩR is close to the boundary but not near to a vertex, it is approximated by the
heat kernel of a half-plane; if the point is far from the boundary ∂ΩR, the heat kernel of
the whole plane is used as an approximation. Unfortunately, Kac was not able to find a
simple enough formula for the heat kernel of a Euclidean wedge; he could only find a
complicated integral expression for it. Secondly, M. van den Berg and S. Srisatkunarajah
used a result due to D.B. Ray. It is claimed in [MS67] that Ray obtained the constant
term on the right-hand side of (3.1) using an explicit formula for the Green’s function
of a wedge. This formula for the Green’s function is stated in [MS67] (and in [vdBS88])
without proof and Ray never published his results. Using this formula as a starting point,
van den Berg and Srisatkunarajah could deduce a simpler expression for the heat kernel
of a wedge compared to that of Kac.
The principle of not feeling the boundary can be used in the same way to solve the
analogous problem for hyperbolic polygons, as we will show in the first two sections of
this chapter. The big challenge for hyperbolic polygons, as it was for Euclidean polygons,
is to obtain a workable formula for the heat kernel of a wedge (see Section 3.1).
The heat invariants for spherical polygons were published in [Wat05], even though that
article contains many inaccuracies and typos. Watson’s approach is similar to that of
[vdBS88] for Euclidean polygons. He, too, uses the principle of not feeling the boundary
to approximate the heat trace function. One advantage in the spherical case is that
any spherical wedge, also commonly known as spherical lune, is a relatively compact
domain and all eigenvalues of its Dirichlet Laplacian are known. Explicit formulas for all
eigenvalues of any spherical lune are stated in [Gro66], such that Watson could use them
in his work [Wat05]. He shows that the asymptotic expansion of the heat trace ZΩS(t)
for any spherical polygon ΩS has the form
ZΩS(t)
t↓0∼∣ΩS∣
4πt −∣∂ΩS∣
8
√
πt
+
∞
∑
k=0
(iS
k + bS
k ⋅t
1
2 + νS
k)tk,
(3.2)
where iS
k,bS
k,νS
k stand for contributions from the interior, the boundary, and the vertices,
respectively, and he obtains explicit formulas for all coefficients appearing in (3.2).
The asymptotic expansion of the heat trace for hyperbolic polygons is very similar to
the spherical case. We will prove in Section 3.2 (see Theorem 3.32) that the heat trace
ZΩH(t) for any hyperbolic polygon ΩH has an asymptotic expansion as in (3.2), i.e.
ZΩH(t)
t↓0∼∣ΩH∣
4πt −∣∂ΩH∣
8
√
πt
+
∞
∑
k=0
(iH
k + bH
k ⋅t
1
2 + νH
k )tk.
(3.3)
We will also obtain explicit formulas for all coefficients in (3.3). The coefficients in (3.3)
38


---

3 Spectral invariants for polygons
and (3.2) are very similar to each other, only the sign changes in every other coefficient.
More precisely, we have iH
k = (−1)k+1iS
k, bH
k = (−1)k+1bS
k and νH
k = (−1)k νS
k for all k ∈N0.
Morally this is “obvious” for iH
k and bH
k because of the principle of not feeling the boundary
and general facts from [BG90] (and [Wat05]); thus our results confirm Watson’s formulas.
It is remarkable for νH
k , since there is no general theory known for the contributions
of vertices to the heat invariants like for the contributions from the interior and the
contributions from a smooth boundary.
Let us return to Definition 3.1 and examine some aspects of hyperbolic polygons. The
motivation for that definition comes from the article [Wat05] in which the heat invariants
are stated for spherical polygons as defined above. Thus it appears natural to treat the
analogous setting in the hyperbolic case, too. Moreover, even though there is no definition
given of the term polygon in the article [vdBS88], the results and the reasoning of that
article are basically valid for Euclidean polygons in the sense of Definition 3.1. It should
be noted that the authors of the article [vdBS88] seem to consider more general polygonal
domains of the Euclidean plane than it is done in the other articles cited above. For
example, in contrast to the other articles, they seem to include polygons with angles
of measure 2π (see [vdBS88, formulas (1.6), (2.2) or (2.14)]). Note that the angle 2π
is excluded in [MS67, formula (4a)] even though the contrary is claimed in [vdBS88,
formula (1.6)].
If the boundary of a hyperbolic polygon is the union of (finitely many) piecewise
geodesic simple closed curves, as it is seen in Fig. 3.1, then it is evident how to define
the edges, vertices, and angles. However, our definition of the term hyperbolic polygon is
more general and also includes some pathological cases which are usually not treated as
polygons (see Fig. 3.2). In order to get an idea of the definitions we have marked the
six polygons of Fig. 3.1 and Fig. 3.2 as follows: the vertices are marked by a dot, the
(interior) angles are denoted by γ1,γ2,γ3,..., and the edges correspond to the straight
line segments between two dots.
γ1
γ2
γ3
γ4
γ5
γ1
γ2
γ3
γ4
γ5
γ6
γ7
γ8
γ1
γ2
γ3
γ4
γ7
γ6
γ5
γ8
γ9
γ10
Figure 3.1: Simple polygons
Note that the number of edges, vertices, and angles of any polygon in Fig. 3.1 is the
same, whereas it is not the same for the polygons of Fig. 3.2 (e.g. each polygon of Fig.
3.2 has more angles than vertices). Furthermore, angles of measure π and 2π may appear
in general. For example, in the left polygon of Fig. 3.2 the angle γ10 has measure π and
γ5,γ7,γ9 are of size 2π. We proceed with precise definitions of edges, vertices, and angles.
39


---

3 Spectral invariants for polygons
γ1
γ2
γ3
γ4
γ5
γ10
γ8
γ6
γ7
γ9
γ1
γ2
γ3
γ4
γ5
γ6
γ7
γ5
γ6
γ7
γ8
γ9
γ10
γ11
γ1
γ2
γ3
γ4
Figure 3.2: Polygons
Definition 3.3. For any two points x,y ∈H2 we denote the (hyperbolic) distance between
them by d(x,y). Further, for any r > 0 and P ∈H2 let
BH2
r (P) ∶= {x ∈H2 ∣d(x,P) < r }
(3.4)
denote the geodesic disc in the hyperbolic plane of radius r and center P.
Definition 3.4. Let Ω⊂H2 be a hyperbolic polygon and let P ∈∂Ωbe a boundary
point. If there exists some r > 0 such that BH2
r (P)∩∂Ωis exactly one diameter of BH2
r (P),
i.e. exactly one geodesic segment of length 2 ⋅r and midpoint P, then we call P a smooth
boundary point of Ω. Otherwise P is called a vertex of Ω.
A geodesic segment is called an edge of Ω, if it is contained in ∂Ωand both of its
endpoints are vertices and there is no other vertex lying on it (except for the endpoints).
Hence Ωhas finitely many vertices and the boundary ∂Ωconsists of the union of
finitely many edges which have no points in common except for vertices.
Definition 3.5. Let Ω⊂H2 be a hyperbolic polygon and let P ∈∂Ωbe a vertex. Let
E1,E2 be (not necessarily different) edges of Ωhaving P as an endpoint. Let W be a
wedge with vertex P and bounded by geodesic rays which contain E1 and E2, respectively.
We choose polar coordinates (a,α) such that we have
W = {(a,α) ∣0 < a < ∞, 0 < α < γ }
for some γ ∈(0,2π]. If there exists a r > 0 such that
W ∩BH2
r (P) ∩Ω= {(a,α) ∣0 < a < r, 0 < α < γ },
then we call W an angle of Ωat P. For convenience we refer to W by referring to the
corresponding angle γ of W.
Lastly, let us briefly discuss the meaning of the constants ∣ΩH∣and ∣∂ΩH∣appearing in
(3.3). As usual, the former denotes the volume (or rather the area) of the polygon ΩH.
However, ∣∂ΩH∣does not always correspond to the length of the boundary ∂ΩH, but is
defined as follows.
40


---

3 Spectral invariants for polygons
Definition 3.6. Let Ωbe a hyperbolic polygon. Suppose ˜
M ∈N is the number of its
edges and E1,...,E ˜
M denote all edges of Ω. Further, let L(Ej) ∈(0,∞) be the length of
the edge Ej for all j = 1,..., ˜
M. Let k ∈{1,..., ˜
M} be arbitrary and let Qk denote the
midpoint of the edge Ek. If there exists some r > 0 such that BH2
r (Qk) ∩Ωis the disjoint
union of two (open) half-discs, then we define ∣Ek∣∶= 2 ⋅L(Ek), and otherwise we set
∣Ek∣∶= L(Ek). We now define ∣∂Ω∣∶= ∑
˜
M
j=1 ∣Ej∣.
Note that if the boundary of Ωis the union of piecewise geodesic simple closed curves,
then we have ∣Ej∣= L(Ej) for all j = 1,..., ˜
M so that ∣∂Ω∣indeed corresponds to the
length of the boundary.
The constants ∣∂ΩR∣and ∣∂ΩS∣appearing in the asymptotic expansions (3.1) and (3.2),
respectively, must be interpreted in an analogous manner so that the formulas are correct
in general.
3.1 Green’s function and heat kernel of a wedge
Let W ⊂H2 be a hyperbolic wedge with vertex P ∈H2 and interior angle γ ∈(0,2π]. Our
aim in this section is to study the function Zγ defined by
Zγ(t;r) ∶=
∫
BH2
r (P)∩W
KW(x,x;t)dx,
r,t > 0.
Note that the heat kernel KW is the one for the entire wedge, while the integration is
done over a bounded sector only. In order to study Zγ, we first investigate the heat kernel
KW (recall Definition 2.2) and the Green’s function GW (recall Definition 2.11) of the
wedge and establish explicit formulas for them as generalised Mehler transforms. These
formulas in turn will lead to an explicit formula for Zγ(t;r), which will be used in Section
3.2 to compute the heat invariants for all hyperbolic polygons.
It will be useful to introduce the following shifted functions.
Definition 3.7. For any domain Ω⊂H2, we call the functions K
1/4
Ω∶Ω× Ω× (0,∞) →R
and G
1/4
Ω∶o-diag(Ω) × H> 1
4 →C defined by
K
1/4
Ω(x,y;t) ∶= e
1
4 t ⋅KΩ(x,y;t),
(3.5)
G
1/4
Ω(x,y;s) ∶= L{K
1/4
Ω(x,y;t)}(s)
(3.6)
the shifted heat kernel and the shifted Green’s function of Ω, respectively.
Like the heat kernel, the function K
1/4
Ωsatisfies the conditions of Definition 2.2 if the
Laplacian ∆is replaced in condition (2.1) by the shifted Laplacian ∆
1/4 ∶= ∆−1
4. Further,
for each s > 1
4, the shifted Green’s function G
1/4
Ωsatisfies Proposition 2.12 if the Laplacian
41


---

3 Spectral invariants for polygons
is replaced by the shifted Laplacian. The reason is that s + ∆
1/4 = (s −1
4) + ∆and
G
1/4
Ω(x,y;s) =
∞
∫
0
e−ste
1
4 t ⋅KΩ(x,y;t)dt =
∞
∫
0
e−(s−1
4 )t ⋅KΩ(x,y;t)dt
= GΩ(x,y;s −1
4).
(3.7)
Most of the formulas below are stated in terms of the shifted functions, since then they
become shorter. The formulas can always be rewritten into corresponding formulas for
the Green’s function by (3.7) and for the heat kernel using (3.5).
The heat kernel KH2 for the hyperbolic plane is given by the following formulas (see,
e.g., [Cha84, (12) and (13) on p. 246]):
KH2(x,y;t) = 1
2π
∞
∫
0
e−( 1
4 +ρ2)tP−1
2 +iρ (cosh(d(x,y)))ρtanh(πρ)dρ
(3.8)
=
√
2
(4πt)
3/2e−t
4
∞
∫
d(x,y)
ρe−ρ2
4t
√
cosh(ρ) −cosh(d(x,y))
dρ,
(3.9)
where P−1
2 +iρ is the Legendre function of the first kind from Definition 2.16. We start
with a helpful new formula for the Green’s function GH2 of the hyperbolic plane in terms
of polar coordinates.
Proposition 3.8. Let s ∈C be such that R(s) > 1
4, and let x,y ∈H2 with x ≠y be given.
The shifted Green’s function for the hyperbolic plane is given by the equation
G
1/4
H2(x,y;s) = 1
2πQ√s−1
2 (cosh(d(x,y))).
(3.10)
Suppose, further, that we have chosen polar coordinates in H2 (associated with a chosen
orientation and a chosen geodesic ray) such that x = (a,α) and y = (b,β), where a,b ∈
(0,∞) and α,β ∈[0,2π). Then
G
1/4
H2(x,y;s) = 1
π2
∞
∫
0
Q−iρ
√s−1
2 (cosh(a))Qiρ
√s−1
2 (cosh(b))cosh(ρ ⋅(π −∣α −β∣))dρ.
(3.11)
Proof. From (3.8) we obtain
K
1/4
H2(x,y;t) = 1
2π
∞
∫
0
e−ρ2tP−1
2 +iρ (cosh(d(x,y)))ρtanh(πρ)dρ.
(3.12)
42


---

3 Spectral invariants for polygons
Thus using the Fubini-Tonelli theorem we get
G
1/4
H2(x,y;s) =
∞
∫
0
e−st ⎛
⎝
1
2π
∞
∫
0
e−ρ2tP−1
2 +iρ (cosh(d(x,y)))ρtanh(πρ)dρ⎞
⎠dt
= 1
2π
∞
∫
0
⎛
⎝
∞
∫
0
e−(s+ρ2)tdt⎞
⎠P−1
2 +iρ (cosh(d(x,y)))ρtanh(πρ)dρ
= 1
2π
∞
∫
0
ρtanh(πρ)
s + ρ2
P−1
2 +iρ (cosh(d(x,y)))dρ
= 1
2πQ√s−1
2 (cosh(d(x,y))),
where the last equality can be found for example in [GR07, 7.213] or [OH61, p. 20]. Let us
explain shortly why the Fubini-Tonelli theorem is applicable, which we used in the second
equality above. Because of (2.22) and since ρ ↦P−1
2 +iρ (cosh(d(x,y))) is continuous,
there exists some constant C > 0 such that for all ρ ∈(0,∞): ∣P−1
2 +iρ (cosh(d(x,y)))∣≤
C
√ρ.
Hence,
∞
∫
0
∞
∫
0
∣e−(s+ρ2)tP−1
2 +iρ (cosh(d(x,y)))ρtanh(πρ)∣dtdρ ≤C
∞
∫
0
∞
∫
0
e−( 1
4 +ρ2)t ⋅√ρdtdρ
= C
∞
∫
0
√ρ
1
4 + ρ2 dρ < ∞.
This completes the proof of equation (3.10).
The second formula (3.11) follows from (3.10) and Corollary 2.30 with z ∶= cosh(a),
ω ∶= cosh(b), and θ ∶= ∣α −β∣, since the distance is given in the above polar coordinates
by the following formula (see [Bus92, Theorem 2.2.1 (i)]):
cosh(d(x,y)) = cosh(a)cosh(b) −sinh(a)sinh(b)cos(∣α −β∣).
(3.13)
Note that the assumptions of Corollary 2.30 are satisfied here because x ≠y implies that
either a ≠b or ∣α −β∣∈(0,2π).
Remark. Note that the function on the right-hand side of (3.10) is defined for all s ∈
C/(−∞,0] and is also holomorphic on that domain. Hence, the function C/(−∞,0] ∋s ↦
1
2πQ√s−1
2 (cosh(d(x,y))) ∈C is an analytic continuation of H> 1
4 ∋s ↦G
1/4
H2(x,y;s) ∈C.
Obviously, the same applies to the right-hand side of (3.11).
Next, we focus on the heat kernel KW and the Green’s function GW of the hyperbolic
wedge. Before we give a rigorous treatment of those functions, we will consider a heuristic
derivation of the formula (3.27) for G
1/4
W given below. We want to point out that our
heuristic derivation is analogous to a derivation given in [Sri88]. In his doctoral thesis,
Srisatkunarajah has worked out a proof of the formula due to D.B. Ray for the Green’s
43


---

3 Spectral invariants for polygons
function of a Euclidean wedge (as mentioned, this formula is published in [MS67] and
[vdBS88]). However, the proof given in [Sri88] is incomplete and has some argumentative
gaps, which we will provide in the hyperbolic case by Lemma 3.9 and Theorem 3.10.
Note that our formula for the Green’s function of a hyperbolic wedge is similar to Ray’s
formula. The only difference is that the Bessel functions appearing in Ray’s formula are
replaced properly with the associated Legendre functions of the second kind. However, in
the Euclidean case all integrals appearing in the derivation and involving Bessel functions
are well-known, such that their solutions could be used in [Sri88]. We, instead, will have
to refer to Section 2.2 to solve the corresponding integrals for the associated Legendre
functions of the second kind.
As mentioned, we proceed with a largely heuristic discussion of the Green’s function
for W in order to motivate the formula (3.27) below. Recall that ∆= −div ○∇denotes
the Laplacian. Suppose the heat kernel of the wedge W can be written as
KW(x,y;t) = KH2(x,y;t) −h(x,y;t),
(3.14)
where h ∶W × W × [0,∞) →R is a function satisfying for all y ∈W, the following
conditions:
⎧⎪⎪⎪⎪⎪⎪⎪⎨⎪⎪⎪⎪⎪⎪⎪⎩
h(⋅,y;⋅) ∶W × [0,∞) →R
is continuous,
(∂t + ∆)h(x,y;t) = 0
for all x ∈W and t > 0,
h(x,y;0) = 0
for all x ∈W,
h(x,y;t) = KH2(x,y;t)
for all x ∈∂W and t > 0.
(3.15)
Remark. Suppose h(x,y;t) ∶= KH2(x,y;t) −KW(x,y;t) for all x,y ∈W and t > 0. If
for all y ∈W the function KW(⋅,y;⋅) can be extended continuously to W × (0,∞) by
KW(x,y;t) ∶= 0 for all x ∈∂W and t > 0, then h indeed satisfies all conditions of (3.15).
(Of course one needs to extend for all y ∈W the function h(⋅,y;⋅) appropriately.) Note
that h(⋅,y;⋅) can be extended continuously to W × {0} by h(x,y;0) ∶= 0 for all x ∈W
(see [Gri09, Corollary 9.21 and Exercise 9.7]).
When we multiply both sides of equation (3.14) with e
t
4, we obtain the corresponding
equation for the shifted functions. With h
1/4(x,y;t) ∶= e
t
4h(x,y;t), we have
K
1/4
W (x,y;t) = K
1/4
H2(x,y;t) −h
1/4(x,y;t)
for all t > 0 and x,y ∈W.
(3.16)
When we apply the Laplace transform on both sides of (3.16), we obtain the equation
G
1/4
W (x,y;s) = G
1/4
H2(x,y;s) −H
1/4(x,y;s)
(3.17)
for all (x,y) ∈o-diag(W) and s ∈C with R(s) > 1
4, where
H
1/4(x,y;s) ∶= L{h
1/4(x,y;t)}(s).
(3.18)
For any s > 1
4 and y ∈W the function H
1/4(⋅,y;s) solves the following boundary value
44


---

3 Spectral invariants for polygons
problem:
⎧⎪⎪⎪⎪⎨⎪⎪⎪⎪⎩
H
1/4(⋅,y;s) ∶W →R
is continuous and bounded,
(s + ∆−1
4)H
1/4 (x,y;s) = 0
for all x ∈W,
H
1/4 (x,y;s) = G
1/4
H2 (x,y;s)
for all x ∈∂W.
(3.19)
We want to find a solution to the problem (3.19) in terms of polar coordinates, so let
us choose for the rest of this section polar coordinates such that
W = {(a,α) ∣0 < a < ∞, 0 < α < γ }.
The Laplacian is given in polar coordinates by the formula
−∆=
1
sinh(a)
∂
∂a {sinh(a) ∂
∂a} +
1
sinh2(a)
∂2
∂2α,
which follows from the well-known representation of the Laplacian in local coordinates
(see e.g. [Gri09, formula (3.40)]) and since the Riemannian metric g of the hyperbolic
plane is represented in polar coordinates by g = da2 + sinh2(a)dα2 (see [Gri09, formula
(3.70)]). In the following, let y = (b,β) ∈W and s > 1
4 both be fixed.
Firstly, we use the method of separation of variables to find product solutions to
the partial differential equation (PDE) in (3.19), i.e. we look for solutions of the form
u(a,α) = v(a) ⋅w(α). Substituting into the PDE, we obtain for all points x = (a,α) such
that u(a,α) ≠0 ∶
(s + ∆−1
4)u(a,α) = 0
⇔(s −1
4)v(a)w(α) −w(α)
sinh(a)
∂
∂a {sinh(a)v′(a)} −
1
sinh2(a)w′′(α)v(a) = 0
⇔(s −1
4)sinh2(a) −sinh(a)
v(a)
∂
∂a {sinh(a)v′(a)} = w′′(α)
w(α) .
Therefore, both sides must be equal to some separation constant c ∈R. We assume c
to be non-negative and write c = ρ2 with ρ ≥0. The PDE now reduces to the following
two ordinary differential equations:
I) w′′(α) = ρ2 ⋅w(α),
II) (−s + 1
4)sinh2(a) ⋅v(a) + sinh(a) ∂
∂a {sinh(a)v′(a)} + ρ2 ⋅v(a) = 0.
We first solve the second equation. When we multiply this equation by
1
sinh2(a), it can
be written equivalently as:
v′′(a) + cosh(a)
sinh(a) v′(a) + ((−s + 1
4) −
(iρ)2
sinh2(a)) ⋅v(a) = 0.
45


---

3 Spectral invariants for polygons
Consider ˜v ∶= v ○arcosh ∶(1,∞) →C. When we substite ˜v into the above equation, we
get the following equivalent differential equation:
(1 −z2)˜v′′(z) −2z˜v′(z) + ((s −1
4) −(iρ)2
1 −z2) ⋅˜v(z) = 0 for all z ∈(1,∞).
If ν ∶= √s −1
2, then ν ⋅(ν + 1) = s −1
4. This differential equation for ˜v is nothing else than
the associated Legendre equation stated in (2.11) with parameters ν = √s −1
2 and µ = iρ.
For all ρ ≥0 two linearly independent solutions are (see [OLBC10, §14.2(iii)])
z ↦P iρ
√s−1
2(z) and z ↦Q−iρ
√s−1
2(z).
On the other hand, two linearly independent solutions for equation I) are the functions
α ↦cosh(ρα) and α ↦sinh(ρα). Thus we have the following product solutions to the
PDE:
x = (a,α) ↦( ˜A1 cosh(ρα) + ˜A2 sinh(ρα)) ⋅( ˜B1P iρ
√s−1
2(cosh(a)) + ˜B2Q−iρ
√s−1
2(cosh(a)))
with arbitrary constants ˜A1, ˜A2, ˜B1, ˜B2 ∈C.
Secondly, we construct from the product solutions above a suitable solution u =
H
1/4(⋅,y;s) ∶W →R to the PDE which also meets the boundary condition in (3.19). Since
lim
a→∞∣P iρ
√s−1
2(cosh(a))∣= ∞
(see e.g. [OLBC10, 14.8.12]), we set ˜B1 = 0. Further, because of the formula (3.11) for
the boundary condition we try, by using the superposition principle,
u(a,α) ∶=
∞
∫
0
(A1(ρ)cosh(ρα) + A2(ρ)sinh(ρα))Q−iρ
√s−1
2(cosh(a))dρ.
We determine suitable functions A1(ρ), A2(ρ) from the boundary conditions. The bound-
ary ∂W of the wedge contains the two rays emanating from P, which are described in
polar coordinates by
{x = (a,α) ∣0 < a < ∞; α = 0 or α = γ }.
For α = 0 we have
u(a,0) =
∞
∫
0
A1(ρ)Q−iρ
√s−1
2(cosh(a))dρ,
G
1/4
H2((a,0),(b,β);s) = 1
π2
∞
∫
0
cosh(ρ(π −β))Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(b))dρ.
46


---

3 Spectral invariants for polygons
Therefore we set
A1(ρ) ∶= 1
π2 cosh(ρ(π −β))Qiρ
√s−1
2(cosh(b)),
such that the boundary condition at α = 0 is satisfied.
Moreover,
u(a,γ) =
∞
∫
0
{A1(ρ)cosh(ργ) + A2(ρ)sinh(ργ)}Q−iρ
√s−1
2(cosh(a))dρ,
G
1/4
H2((a,γ),(b,β);s) = 1
π2
∞
∫
0
cosh(ρ(π −∣γ −β∣))Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(b))dρ.
Obviously ∣γ −β∣= γ −β and thus we set:
A2(ρ) ∶= 1
π2Qiρ
√s−1
2(cosh(b))(cosh(ρ(π −(γ −β))) −cosh(ρ(π −β))cosh(ργ)
sinh(ργ)
).
Finally we obtain the following candidate for a solution of (3.19), defined for all (a,α) ∈
W/{P} as:
u(a,α) = 1
π2
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(b))⎛
⎝cosh(ρ(π −β))cosh(ρα)
+ (cosh(ρ(π −(γ −β))) −cosh(ρ(π −β))cosh(ργ)) sinh(ρα)
sinh(ργ)
⎞
⎠dρ.
Now observe that the long expression in brackets above can be simplified, since
cosh(ρ(π −β))cosh(ρα) + (cosh(ρ(π −(γ −β))) −cosh(ρ(π −β))cosh(ργ)) sinh(ρα)
sinh(ργ)
= sinh(πρ)
sinh(γρ) cosh(ρ(γ −α −β)) −sinh((π −γ)ρ)
sinh(γρ)
cosh((α −β)ρ).
(3.20)
Thus we set for all x = (a,α) ∈W/{P}:
H
1/4(x,y;s) ∶= 1
π2
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(b))⎛
⎝
sinh(πρ)
sinh(γρ) cosh(ρ(γ −α −β))
−sinh((π −γ)ρ)
sinh(γρ)
cosh((α −β)ρ)⎞
⎠dρ.
(3.21)
Now, a candidate for a formula (in polar coordinates) of the shifted Green’s function
G
1/4
W can be deduced using (3.17), (3.11) and (3.21). That formula is stated explicitly in
47


---

3 Spectral invariants for polygons
Theorem 3.10 below. In order to give a rigorous proof we first study the function H
1/4,
which is done in the following lemma.
Lemma 3.9. Consider the function
H
1/4 ∶W × W × C/(−∞,0] ∋(x,y,s) ↦H
1/4(x,y;s) ∈C,
where H
1/4(x,y;s) is defined by the right-hand side of (3.21) with x = (a,α) and y = (b,β)
(with respect to the polar coordinates chosen above). Then:
(i) For all x,y ∈W the function C/(−∞,0] ∋s ↦H
1/4(x,y;s) ∈C is holomorphic.
(ii) For all s ∈C with R(s) > 0 the function
W × W ∋(x,y) ↦H
1/4(x,y;s) ∈R
is continuous. Moreover, H
1/4(x,y;s) is real valued for all s > 0 and x,y ∈W.
Further, for all s > 1
4 and y ∈W the function W ∋x ↦H
1/4(x,y;s) ∈R is smooth
and (s + ∆
1/4)H
1/4(⋅,y;s) ≡0 (recall that ∆
1/4 = ∆−1
4).
(iii) For all s >
1
4 and y ∈W the function W ∋x ↦H
1/4(x,y;s) ∈R can be ex-
tended continuously to W. That extension (which we also denote by H
1/4) satisfies
H
1/4(x,y;s) = G
1/4
H2(x,y;s) for all x ∈∂W. Furthermore, we have 0 < H
1/4(x,y;s)
for all x ∈W and H
1/4(x,y;s) ≤G
1/4
H2(x,y;s) for all x ∈W/{y}.
Proof. (i). Let x,y ∈W be arbitrary. Obviously, the function H
1/4(x,y;⋅) can be written
as a composition of holomorphic functions due to Lemma 2.31. Note that the function s ↦
√s−1
2 is holomorphic on the domain C/(−∞,0], where that domain is mapped onto H>−1
2.
Therefore, Lemma 2.31 can indeed be applied here; the other conditions of Lemma 2.31 are
obviously satisfied with h(ρ) ∶=
1
π2 ⋅( sinh(πρ)
sinh(γρ) cosh(ρ(γ−α−β))−sinh((π−γ)ρ)
sinh(γρ)
cosh((α−β)ρ)).
(ii). Suppose s ∈C with R(s) > 0 is given. We write H
1/4(⋅,⋅;s) as
H
1/4(x,y;s) =
∞
∫
0
ψ(x,y,ρ)dρ for all x,y ∈W
with
ψ(x,y,ρ) ∶= 1
π2 Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(b))⎛
⎝
sinh(πρ)
sinh(γρ) cosh(ρ(γ −α −β))
−sinh((π −γ)ρ)
sinh(γρ)
cosh((α −β)ρ)⎞
⎠
for all x,y ∈W and ρ > 0. We also set ψ(x,y,0) ∶= limρ↘0 ψ(x,y,ρ) for all x,y ∈W, where
the limit obviously exists.
48


---

3 Spectral invariants for polygons
First of all, note that for all x,y ∈W the function ρ ↦ψ(x,y,ρ) is absolutely integrable
over [0,∞) (see Theorem 2.25). Thus, the functions
q ∶W × W ∋(x,y) ↦
∞
∫
0
∣ψ(x,y,ρ)∣dρ ∈[0,∞)
and H
1/4(⋅,⋅;s) are continuous, which is an immediate consequence of Lebesgue’s domi-
nated convergence theorem and (2.48).
Suppose now s > 0. Note that Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(b)) is real valued for all
a,b > 0 and ρ ≥0. This can be seen from (2.31) and [OLBC10, §14.20] (see the comment
preceding formula 14.20.6 of [OLBC10]). Thus, ψ(x,y,ρ) is real valued for all x,y ∈W
and ρ ≥0 and, consequently, H
1/4(x,y;s) is also real valued for all x,y ∈W. Also note
that for all ρ ≥0 the function W × W ∋(x,y) ↦ψ(x,y,ρ) ∈R is smooth. In the following,
we deal with the other (less obvious) properties of H
1/4 stated in (ii).
We suppose now s > 1
4. First, we show that for all x ∈W the function H
1/4(x,⋅;s) is
smooth, which can be seen as follows: For all x ∈W the function W ∋y ↦H
1/4(x,y;s) ∈R
belongs to L2
loc(W) as any continuous function, this means (by definition of the space
L2
loc(W), see [Gri09, p. 98]), H
1/4(x,⋅;s) ∈L2(U) for any relatively compact open set
U ⊂W. Moreover, for all f ∈C∞
c (W) and x ∈W
∫
W
H
1/4(x,y;s) ⋅(sf + ∆
1/4f)(y)dy = ∫
W
⎛
⎝
∞
∫
0
ψ(x,y,ρ)dρ⎞
⎠⋅(sf + ∆
1/4f)(y)dy
=
∞
∫
0
∫
W
ψ(x,y,ρ) ⋅(sf + ∆
1/4f)(y)dy dρ
=
∞
∫
0
∫
W
(sψ(x,⋅,ρ) + ∆
1/4ψ(x,⋅,ρ))
´¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¶
≡0
(y) ⋅f(y)dy dρ
= 0.
(3.22)
Note that we used the Fubini-Tonelli theorem for the second equality which is possible
because q(x,⋅) is continuous for all x ∈W, and ∣(s + ∆
1/4)f∣is compactly supported as
well as bounded, and thus
∫
W
∞
∫
0
∣ψ(x,y,ρ) ⋅(sf + ∆
1/4f)(y)∣dρdy = ∫
W
q(x,y) ⋅∣(sf + ∆
1/4f)(y)∣dy < ∞.
Further, we used “Green’s formula” for the third equality (see [Gri09, Theorem 3.16]).
Lastly, note that (s + ∆
1/4)ψ(x,⋅,ρ) ≡0 by the discussion preceding Lemma 3.9. Thus, by
elliptic regularity (see [Gri09, Corollary 7.3]), the function y ↦H
1/4(x,y;s) is smooth.
Note that, since H
1/4(x,y;s) = H
1/4(y,x;s) for all x,y ∈W (recall equation (2.17)), the
function W ∋x ↦H
1/4(⋅,y;s) ∈R is smooth for all y ∈W, too.
49


---

3 Spectral invariants for polygons
Furthermore, by (3.22) and Green’s formula, it follows that (s + ∆
1/4)H
1/4(x,⋅;s) ≡0
for arbitrary x ∈W. More precisely, for all x ∈W and f ∈C∞
c (W):
0 = ∫
W
H
1/4(x,y;s) ⋅(sf + ∆
1/4f)(y)dy = ∫
W
f(y) ⋅(sH
1/4(x,⋅;s) + ∆
1/4H
1/4(x,⋅;s))(y)dy.
Because f ∈C∞
c (W) was arbitrary and H
1/4(x,⋅;s) is smooth, it follows for all x ∈W:
(s + ∆
1/4)H
1/4(x,⋅;s) ≡0 (see [Gri09, Lemma 3.13]). Finally, because of the symmetry
H
1/4(x,y;s) = H
1/4(y,x;s) for all x,y ∈W, we also have (s + ∆
1/4)H
1/4(⋅,y;s) ≡0 for
arbitrary y ∈W.
(iii). Let s > 1
4 and let y ∈W be fixed. We want to show that the function W ∋x ↦
H
1/4(x,y;s) ∈R can be extended continuously to W. Suppose x ∈∂W is any boundary
point other than the vertex of W, i.e. in polar coordinates x = (a,α) with a ∈(0,∞)
and α ∈{0,γ}. For those boundary points, we define the value of H
1/4(x,y;s) by the
formula given on the right-hand side of (3.21). Note that the integral which is obtained
after setting α = 0 or α = γ on the right-hand side of (3.21) is absolutely convergent
(see Theorem 2.25). Further, that continuation indeed provides a continuous function
W/{P} ∋x ↦H
1/4(x,y;s) ∈R (recall that P denotes the vertex of the wedge). This can
easily be seen by using Lebesgue’s dominated convergence theorem and (2.48). Lastly,
note that H
1/4(x,y;s) = G
1/4
H2(x,y;s) for all x ∈∂W/{P}, which is obvious when using
(3.20).
On the contrary, it is more challenging to show that H
1/4(⋅,y;s) can also be extended
continuously at the vertex P. Note for example, that the formula on the right-hand side
of (3.21) has no meaning for a = 0 because Q−iρ
√s−1
2(z) is formally not defined for z = 1
(also the limit of Q−iρ
√s−1
2(cosh(a)) as a ↘0 does not exist). However, we will show that
lim
x→P H
1/4(x,y;s) = 1
2πQ√s−1
2(cosh(b)).
(3.23)
For that purpose, let us write H
1/4(x,y;s) = I1(x) −I2(x) for all x ∈W with
I1(x) ∶= 1
π2
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(b)) ⋅sinh(πρ)
sinh(γρ) cosh(ρ(γ −α −β))dρ,
I2(x) ∶= 1
π2
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(b)) ⋅sinh((π −γ)ρ)
sinh(γρ)
cosh((α −β)ρ)dρ.
First, we will consider the limit of I1(x) as x →P. Note that I1 can be written as
I1(x) = 1
2 ⋅2
π
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(b)) ⋅sin(iπρ)
π
⋅cos(iρ(γ −α −β))
sin(iγρ)
dρ.
Since we are only interested in the limit of I1(x) as x = (a,α) →P we may assume
50


---

3 Spectral invariants for polygons
in the followig a < b. The idea is to apply Theorem 2.25 with g(z) = cos(z(γ−α−β))
sin(zγ)
. The
only singularities of g are simple poles at k π
γ with k ∈Z with residue Res(g;k π
γ ) =
(−1)k
γ
cos( πk
γ (γ −α −β)). Hence, by Theorem 2.25,
I1(x) =
∞
∑
k=1
(−1)k
γ
cos(πk
γ (γ −α −β))e−iπk π
γ P
−k π
γ
√s−1
2(cosh(a))Q
k π
γ
√s−1
2(cosh(b))+
+ 1
2γ P√s−1
2(cosh(a))Q√s−1
2(cosh(b)).
(3.24)
Note that
lim
a↘0 P√s−1
2(cosh(a)) = 1,
(3.25)
(see [OLBC10, formula 14.8.7 on p. 361]) and thus
lim
a↘0
1
2γ P√s−1
2(cosh(a))Q√s−1
2(cosh(b)) = 1
2γ Q√s−1
2(cosh(b)).
Now, we want to show that the series appearing on the right-hand side of (3.24) converges
to zero as a ↘0, uniformly for all α ∈(0,γ). By Lemma 2.32 (i), there exist constants
C,D > 0 such that for all µ > 0 and a ∈R with 0 < a < 2arsinh( 1
2D) <
1
D (the last
inequality follows because arsinh(x) < x for all x > 0):
∣P −µ
√s−1
2(cosh(a))Qµ√s−1
2(cosh(b))∣≤Ce
√sa ⋅µ
√s ⋅(D sinh(a
2))
µ
≤Ce
√s
D (1
2)
µ
2 ⋅µ
√s ⋅(D sinh(a
2))
µ
2
≤ˆC ⋅(D sinh(a
2))
µ
2 ,
where ˆC ∶= Ce
√s
D ⋅supµ>0 {( 1
2)
µ
2 µ
√s } ∈(0,∞). Thus, for all α ∈(0,γ) and a ∈R with
0 < a < 2arsinh( 1
2D), the absolute value of the series in (3.24) is bounded from above by
∞
∑
k=1
∣(−1)k
γ
cos(πk
γ (γ −α −β))e−iπk π
γ P
−k π
γ
√s−1
2(cosh(a))Q
k π
γ
√s−1
2(cosh(b))∣
≤
ˆC
γ
∞
∑
k=1
((D sinh(a
2))
π
2γ )
k
=
ˆC
γ ⋅
(D sinh( a
2))
π
2γ
1 −(D sinh( a
2))
π
2γ .
Obviously, that upper bound holds uniformly for all α ∈(0,γ) and converges to 0 as
a ↘0. We conclude
lim
x→P I1(x) = 1
2γ Q√s−1
2(cosh(b)).
(3.26)
51


---

3 Spectral invariants for polygons
Next, we consider I2(x) as x →P. If γ = π then I2(x) = 0 for all x ∈W and thus (3.23)
follows. Suppose now γ ≠π. We write I2 as
I2(x) = 1
π
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(b))sin(iπρ)
π
⋅sin((π −γ)iρ)cos((α −β)iρ)
sin(iπρ)sin(γiρ)
dρ.
This time, we will apply Theorem 2.25 with
g(z) = sin((π −γ)z)cos((α −β)z)
sin(πz)sin(γz)
= cos(γz)cos((α −β)z)
sin(γz)
−cos(πz)cos((α −β)z)
sin(πz)
.
The singularities of that function are simple poles and the set of all poles is given by
Z ∪{k π
γ ∣k ∈Z}. Let (pℓ)∞
ℓ=1 be the sequence of all positive poles such that 0 < p1 < p2 <
p3 < ..., and thus
I2(x) =
∞
∑
ℓ=1
Res(g;pℓ)e−iπpℓP −pℓ
√s−1
2(cosh(a))Qpℓ
√s−1
2(cosh(b))
+ 1
2 (1
γ −1
π)P√s−1
2(cosh(a))Q√s−1
2(cosh(b)).
As above, one can show that the series on the right-hand side converges to 0 as a ↘0,
uniformly for all α ∈(0,γ). Just note that the set of all residue {Res(g;pℓ)}ℓ∈N is bounded.
Hence, we obtain together with (3.25):
lim
x→P I2(x) = 1
2 (1
γ −1
π)Q√s−1
2(cosh(b)).
In particular, we have shown that
lim
x→P H
1/4(x,y;s) = lim
x→P(I1(x) −I2(x)) = 1
2πQ√s−1
2(cosh(b)) =∶H
1/4(P,y;s).
Note that we also have
1
2πQ√s−1
2(cosh(b)) = G
1/4
H2(P,y;s), which follows directly from
(3.10) because of d(P,y) = b.
It remains to show 0 < H
1/4(x,y;s) for all x ∈W and H
1/4(x,y;s) ≤G
1/4
H2(x,y;s)
for all x ∈W/{y}. To prove those estimates, we will use the following properties of
H
1/4 and G
1/4
H2, respectively. First, for all sequences (xn)n∈N such that xn ∈W/{y} and
limn→∞d(xn,P) = ∞: limn→∞G
1/4
H2(xn,y;s) = 0 as well as limn→∞H
1/4(xn,y;s) = 0. The
former limit is easy to check since G
1/4
H2(xn,y;s) =
1
2πQ√s−1
2(cosh(d(xn,y))) by (3.10),
limn→∞d(xn,y) = ∞by our assumptions on (xn)n∈N, and Q√s−1
2(zn) converges to 0 for
all sequences (zn)n∈N with zn ∈(1,∞) and limn→∞zn = ∞(see [OLBC10, 14.8.15]). For
the other limit note that, for all sequences xn = (an,αn) ∈W as above, we have by (2.48)
the estimate ∣H
1/4(xn,y;s)∣≤
ˆD
√an−1 for some constant ˆD > 0. Since limn→∞d(xn,P) = ∞,
we have limn→∞an = ∞and thus limn→∞H
1/4(xn,y;s) = 0. Second, note that the heat
52


---

3 Spectral invariants for polygons
kernel KH2 is strictly positive, which can be seen, for example, from (3.9). Consequently
G
1/4
H2(x,y;s) > 0 for all x ∈W/{y}.
To prove positivity of H
1/4, let us assume that there exists some x0 ∈W with
H
1/4(x0,y;s) < 0. We choose some radius R > 0 such that d(x0,P) < R and H
1/4(x0,y;s) <
H
1/4(x,y;s) for all x ∈W with d(x,P) ≥R. The latter condition can be achieved due
to limd(x,P)→∞H
1/4(x,y;s) = 0 as shown above. Now, with U ∶= BR(P) ∩W, we have
H
1/4(⋅,y;s)∣U ∈C(U) ∩C∞(U) (which means, by definition, the function belongs to
C∞(U) and can be extended continuously to the closure U). Furthermore, by our
assumptions on R, we have H
1/4(x0,y;s) < H
1/4(x,y;s) for all x ∈∂U (recall that
H
1/4(x,y;s) = G
1/4
H2(x,y;s) > 0 for all x ∈∂W). This is a contradiction to the ellip-
tic minimum principle (see [Gri09, Corollary 8.16] and recall that H
1/4(⋅,y;s) satisfies
(sH
1/4(⋅,y;s) + ∆
1/4H
1/4(⋅,y;s))(x) = 0 for all x ∈U). Thus, we conclude H
1/4(x,y;s) ≥0
for all x ∈W. Moreover, by the strong elliptic minimum principle (see [Gri09, Corollary
8.14]), it follows that H
1/4(x,y;s) > 0 for all x ∈W.
The second estimate is shown similarly. Note that u ∶W/{y} ∋x ↦G
1/4
H2(x,y;s) −
H
1/4(x,y;s) ∈R is smooth and can be extended continuously to W/{y} by u(x) ∶= 0 for
all x ∈∂W. Moreover, limd(x,P)→∞u(x) = 0 (as shown above) and limx→y u(x) = ∞. The
latter limit holds because H
1
4(⋅,y;s) is a bounded function on W and limx→y G
1/4
H2(x,y;s) =
limx→y
1
2πQ√s−1
2(cosh(d(x,y))) = ∞, where the last equality follows from [Olv97, formula
(12.23)]. Now, suppose there exists some x0 ∈W/{y} such that u(x0) < 0. We choose radii
R,τ > 0 so that the following conditions are satisfied: Bτ(y) ⊂W, u(x) > 0 for all x ∈
Bτ(y)/{y}, u(x0) < u(x) for all x ∈W with d(x,P) ≥R, and x0 ∈(W ∩BR(P))/Bτ(y) =∶
V . Obviously, V is a relatively compact open set and u ∈C(V ) ∩C∞(V ) satisfies
(s + ∆
1/4)u(x) = 0 for all x ∈V . Moreover x0 ∈V is some interior point with the
property u(x0) < u(x) for all x ∈∂V , which is a contradiction to the elliptic minimum
principle as above (see [Gri09, Corollary 8.16]). Thus, we conclude u ≥0, or equivalently,
G
1/4
H2(x,y;s) ≥H
1/4(x,y;s) for all x ∈W/{y}.
Theorem 3.10. For all (x,y) ∈o-diag(W) and s ∈C with R(s) > 1
4:
G
1/4
W (x,y;s) = 1
π2
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(b)) ⋅(cosh(ρ(π −∣α −β∣))−
sinh(πρ)
sinh(γρ) cosh(ρ(γ −α −β)) + sinh(ρ(π −γ))
sinh(γρ)
cosh((α −β)ρ))dρ,
(3.27)
where x = (a,α) and y = (b,β) (with respect to the polar coordinates chosen above).
Proof. For brevity, we denote the right-hand side of (3.27) by ˜G
1/4
W (x,y;s). More precisely,
˜G
1/4
W ∶o-diag(W) × H> 1
4 →C,
((x,y),s) ↦˜G
1/4
W (x,y;s) ∶= G
1/4
H2(x,y;s) −H
1/4(x,y;s),
53


---

3 Spectral invariants for polygons
where H
1/4 is defined as in (3.21). Recall the following facts: For all x,y ∈W with x ≠y
the functions G
1/4
H2(x,y;⋅) and G
1/4
W (x,y;⋅) are holomorphic on H> 1
4 (recall Proposition 2.8).
Similary, for all x,y ∈W the function H
1/4(x,y;⋅) is also holomorphic on H> 1
4 which follows
from Lemma 3.9 (i). Hence, it suffices to prove the equality G
1/4
W (x,y;s) = ˜G
1/4
W (x,y;s)
for all s ∈( 1
4,∞) and x,y ∈W with x ≠y.
Let s > 1
4 be fixed and let f ∈C∞
c (W) be given such that f(x) ≥0 for all x ∈W. We
extend that function to H2 by f(y) ∶= 0 for all y ∈H2/W and we denote the extended
function also by f, so that it belongs to C∞
c (H2). We define
uW ∶W ∋x ↦∫
W
G
1/4
W (x,y;s)f(y)dy ∈R
and uH2 ∶H2 ∋x ↦∫
H2
G
1/4
H2(x,y;s)f(y)dy ∈R,
which are known to be smooth functions (see [Gri09, Theorem 8.7(ii)]). Moreover, one
can show that (s + ∆
1/4)uW(x) = f(x) for all x ∈W, respectively (s + ∆
1/4)uH2(x) = f(x)
for all x ∈H2 (see [Gri09, Theorem 8.4(b)]). Similarly, we define
Φ ∶W ∋x ↦∫
W
H
1/4(x,y;s)f(y)dy ∈R.
Note that Φ is smooth and satisfies (s + ∆
1/4)Φ(x) = 0 for all x ∈W, which follows e.g.
from Lemma 3.9 (ii), [Els09, Satz 5.7 Zusatz on p. 148] and the fact that f is compactly
supported in W (by assumption).
Next, we define
˜uW ∶W ∋x ↦∫
W
˜G
1/4
W (x,y;s)f(y)dy ∈R
and we will show uW(x) = ˜uW(x) for all x ∈W by applying the result in [Gri09, Exercise
8.2] (where the notation given in [Gri09, Exercise 8.2] corresponds to our notation as
follows: α ∶= s −1
4, Rαf ∶= uW and u ∶= ˜uW). Let us show that the conditions of [Gri09,
Exercise 8.2] are indeed satisfied by ˜uW:
First, note that ˜uW = uH2 −Φ and thus, by the discussion above, ˜uW is smooth and
satisfies (s + ∆
1/4)˜uW(x) = f(x) for all x ∈W. Moreover, ˜uW is non-negative, since for all
x ∈W
˜uW(x) = ∫
W
˜G
1/4
W (x,y;s)f(y)dy = ∫
W
(G
1/4
H2(x,y;s) −H
1/4(x,y;s)) ⋅f(y)dy,
where f(y) ≥0 for all y ∈W (by assumption), and (G
1/4
H2 −H
1/4)(x,y;s) ≥0 for all (x,y) ∈
o-diag(W) by Lemma 3.9 (iii). Lastly, we need to check whether limn→∞˜uW(xn) = 0 for
all sequences (xn)n∈N ⊂W such that either there exists some x∗∈∂W with limn→∞xn = x∗
54


---

3 Spectral invariants for polygons
or limn→∞d(P,xn) = ∞. That property follows immediately from Lebesgue’s dominated
convergence theorem and the following facts:
Recall that for all y ∈W the function ˜G
1/4
W (⋅,y;s) ∶W/{y} →R can be extended
continuously to W/{y} by ˜G
1/4
W (x,y;s) ∶= 0 for all x ∈∂W (see Lemma 3.9 (iii)). Further,
we have shown in the proof of Lemma 3.9 (iii) that limd(x,P)→∞˜G
1/4
W (x,y;t) = 0 for all
y ∈W. Lastly, for all ε > 0 there exists some constant D > 0 such that for all x,y ∈W
with d(x,y) ≥ε:
0 ≤˜G
1/4
W (x,y;s) ≤G
1/4
H2(x,y;s) ≤D.
The first estimate follows from Lemma 3.9 (iii) and for the second estimate note that
there exists some constant C > 0 such that
KH2(x,y;t) ≤C
t ⋅e−d(x,y)2
8t
,
∀x,y ∈H2, t > 0
(3.28)
(see e.g. [Bus92, Lemma 7.4.26]). Thus, it follows for all x,y ∈H2 with d(x,y) ≥ϵ:
G
1/4
H2(x,y;s) =
∞
∫
0
e( 1
4 −s)tKH2(x,y;t)dt ≤
∞
∫
0
e( 1
4 −s)tC
t ⋅e−ε2
8t dt =∶D.
Thus, by Lebesgue’s dominated convergence theorem we have limn→∞˜uW(xn) = 0 for
any sequence as above. Using [Gri09, Exercise 8.2] we have uW(x) = ˜uW(x) for all x ∈W.
Since f ∈C∞
c (W) with f ≥0 was arbitrary, we conclude that for all x ∈W: G
1/4
W (x,y;s) =
G
1/4
H2(x,y;s) −H
1/4(x,y;s) for almost all y ∈W. Further, for any x ∈W, both sides are
continuous in y ∈W/{x} and thus they must be equal for all y ∈W/{x}.
By definition, the (shifted) Green’s function is defined as the Laplace transform of
the (shifted) heat kernel. Thus we obtain a formula for the (shifted) heat kernel from
Theorem 3.10.
Corollary 3.11. For all t > 0 and x ∈W
K
1/4
W (x,x;t) = K
1/4
H2(x,x;t) −L−1 {s ↦H
1/4(x,x;s)}(t),
(3.29)
where H
1/4 is the same function as in Lemma 3.9.
Moreover, for all x ∈W the function (0,∞) ∋t ↦K
1/4
H2(x,x;t) −K
1/4
W (x,x;t) ∈R is
non-negative, can be extended continuously at t = 0, its Laplace integral is (absolutely)
convergent and equal to H
1/4(x,x;s) for all s ∈H> 1
4. The above inverse Laplace transform
can be computed by the inversion formula (2.8) with ε > 1
4.
Proof. Let x ∈W be arbitrary. By definition, for all y ∈W with y ≠x and for all s ∈H> 1
4:
G
1/4
W (x,y;s) = L{K
1/4
W (x,y;⋅)}(s) and G
1/4
H2(x,y;s) = L{K
1/4
H2(x,y;⋅)}(s).
55


---

3 Spectral invariants for polygons
Furthermore, by Theorem 3.10, we have H
1/4(x,y;s) = G
1/4
H2(x,y;s) −G
1/4
W (x,y;s) for all
y ∈W with y ≠x and s ∈H> 1
4. Thus, for all y ∈W with y ≠x and t > 0:
L−1 {s ↦H
1/4(x,y;s)}(t) = K
1/4
H2(x,y;t) −K
1/4
W (x,y;t).
We will show that the above equation is also valid for y = x. For that purpose we consider
u ∶W × [0,∞) →R defined for all (y,t) ∈W × [0,∞) as
u(y,t) ∶=
⎧⎪⎪⎨⎪⎪⎩
K
1/4
H2(x,y;t) −K
1/4
W (x,y;t),
if t > 0
0,
if t = 0.
Obviously, for all y ∈W and t > 0 we have 0 ≤K
1/4
W (x,y;t) ≤K
1/4
H2(x,y;t), and thus
0 ≤u(y,t) ≤K
1/4
H2(x,y;t). Moreover, u is continuous (see [Gri09, Corollary 9.21 and
Exercise 9.7]). Hence, the Laplace transform of u(y,⋅) exists for all y ∈W and s ∈H> 1
4.
Just note that for all y ∈W and s ∈H> 1
4:
∞
∫
0
e−stu(y,t)dt ≤
1
∫
0
e−stu(y,t)dt +
∞
∫
1
e−stK
1/4
H2(x,y;t)dt,
where the first integral is convergent because of the continuity of u(y,⋅) on [0,∞), and
the second integral is convergent due to (3.28).
Let (yn)n∈N ⊂W/{x} be a sequence such that limn→∞yn = x. Then for all s ∈H> 1
4:
L{u(x,⋅)}(s) =
∞
∫
0
e−st(K
1/4
H2(x,x;t) −K
1/4
W (x,x;t))dt
= lim
n→∞
∞
∫
0
e−st(K
1/4
H2(x,yn;t) −K
1/4
W (x,yn;t))dt
= lim
n→∞(G
1/4
H2(x,yn;s) −G
1/4
W (x,yn;s)) = lim
n→∞H
1/4(x,yn;s)
= H
1/4(x,x;s).
Thus, by Proposition 2.8, u(x,t) = L−1{s ↦H
1/4(x,x;s)}(t) for all t > 0. Note that we
used continuity of H
1/4 for the last equation (see Lemma 3.9 (ii)), and, for the second
equation, we used Lebesgue’s dominated convergence theorem which is allowed because of
the following: First, for all compact K ⊂W with x ∈K, u∣K×[0,1] is bounded by continuity
of u and also the function K × [1,∞) ∋(y,t) ↦e−1
4 tu(y,t) ∈R is bounded because of
0 ≤e−1
4 tu(y,t) ≤KH2(x,y;t) and (3.28). Thus, K × [0,∞) ∋(y,t) ↦e−1
4 tu(y,t) ∈R is
bounded as well. In particular, there exists some constant C > 0 such that for all t ≥0
and n ∈N: ∣e−stu(x,yn;t)∣≤C ⋅e( 1
4 −R(s))t. That upper bound is integrable over [0,∞)
since, by assumption, R(s) > 1
4.
Lastly, note that the inversion formula (2.8) holds with ε > 1
4 because of Proposition
56


---

3 Spectral invariants for polygons
2.8 and because the Laplace integral of u(x,⋅) is absolutely convergent for all s > 1
4, as
explained above.
Now that we have established the above formula for the heat kernel KW we are in a
position to investigate thoroughly the function stated at the beginning of this section.
According to the discussion before, we introduce the shifted function
Z
1/4
γ (t;r) ∶= e
t
4 ⋅Zγ(t;r) =
∫
BH2
r (P)∩W
K
1/4
W (x,x;t)dx
(3.30)
and consequently maintain to work with the shifted function Z
1/4
γ (t;r) instead of Zγ(t;r)
itself. We have the following formula for Z
1/4
γ (t;r) ∶
Theorem 3.12. Let r > 0 be arbitrary. For all t > 0:
∫
BH2
r (P)∩W
K
1/4
W (x,x;t)dx =
r
∫
0
γ
∫
0
K
1/4
H2((a,α),(a,α);t)sinh(a)dαda−
−2
r
∫
0
π
2
∫
0
K
1/4
H2((a,α),(a,−α);t)sinh(a)dαda
+ γ
2π
∞
∫
0
e−u2
4t
√
4πt
⋅
e
u
2
eu −1 ⋅(π
γ coth(π
γ ⋅u
2) −coth(u
2))du
−Aγ(t;r),
(3.31)
where
Aγ(t;r) ∶= γ
π2L−1
⎧⎪⎪⎨⎪⎪⎩
s ↦
∞
∫
r
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))⋅
⋅sinh(ρ(π −γ))
sinh(ργ)
sinh(a)dρda
⎫⎪⎪⎬⎪⎪⎭
(t). (3.32)
Proof. In polar coordinates, the domain of integration is parametrised as
BH2
r (P) ∩W = {(a,α) ∣0 < a < r, 0 < α < γ }
and the volume form is given by dx = sinh(a)dadα. From (3.29) we get for all t > 0:
Z
1/4
γ (t;r) =
r
∫
0
γ
∫
0
K
1/4
H2((a,α),(a,α);t) ⋅sinh(a)dαda
−
r
∫
0
γ
∫
0
L−1
⎧⎪⎪⎨⎪⎪⎩
s ↦H
1/4((a,α),(a,α);s)
⎫⎪⎪⎬⎪⎪⎭
(t) ⋅sinh(a)dαda.
(3.33)
57


---

3 Spectral invariants for polygons
The first summand on the right-hand side (RHS) of equation (3.33) is exactly the same
as the first term on the RHS of (3.31). Let us simplify the second summand on the RHS
of (3.33). In order to get a better overview we postpone some of the lengthy calculations
involved in the remaining part. We will fill in these gaps later by the Lemmas 3.13 – 3.16
to which we will refer here whenever needed.
First, let s > 1
4 be given. Then Q−iρ
√s−1
2(cosh(a)) ⋅Qiρ
√s−1
2(cosh(a)) is non-negative for all
a > 0 and ρ ≥0. This follows from (2.31) and [OLBC10, §14.20]. Thus, by (3.21) and the
Fubini-Tonelli theorem:
r
∫
0
γ
∫
0
H
1/4((a,α),(a,α);s) ⋅sinh(a)dα da
= 1
π2
r
∫
0
γ
∫
0
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))⎛
⎝
sinh(πρ)
sinh(γρ) cosh(ρ(γ −2α))
−sinh((π −γ)ρ)
sinh(γρ)
⎞
⎠dρ sinh(a)dα da
= 1
π2
r
∫
0
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))
γ
∫
0
⎛
⎝
sinh(πρ)
sinh(γρ) cosh(ρ(γ −2α))
−sinh((π −γ)ρ)
sinh(γρ)
⎞
⎠dα dρ sinh(a)da
= 1
π2
r
∫
0
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))⎛
⎝
sinh(πρ)
ρ
−γ sinh((π −γ)ρ)
sinh(γρ)
⎞
⎠dρ sinh(a)da
= 1
2
r
∫
0
P√s−1
2(cosh(a))Q√s−1
2(cosh(a))sinh(a)da
−γ
π2
r
∫
0
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))sinh((π −γ)ρ)
sinh(γρ)
dρ sinh(a)da,
(3.34)
where we used Lemma 3.13 (ii) for the last equality. Note that both integrals are finite
due to (2.61) and (2.49), respectively. Moreover the right-hand side is holomorphic in
s ∈C/(−∞,0].
Thus, we obtain for all s > 1
4:
L{t ↦∫BH2
r (P)∩W K
1/4
H2(x,x;t) −K
1/4
W (x,x;t)dx}(s)
58


---

3 Spectral invariants for polygons
=
∞
∫
0
e−st
∫
BH2
r (P)∩W
K
1/4
H2(x,x;t) −K
1/4
W (x,x;t)dxdt
=
∫
BH2
r (P)∩W
∞
∫
0
e−st (K
1/4
H2(x,x;t) −K
1/4
W (x,x;t))dtdx
=
∫
BH2
r (P)∩W
H
1/4(x,x;s)dx,
where we applied the Fubini-Tonelli theorem for the second equality (note that all
functions are non-negative). Thus, we have for all t > 0
L−1
⎧⎪⎪⎨⎪⎪⎩
s ↦
∫
BH2
r (P)∩W
H
1/4(x,x;s)dx
⎫⎪⎪⎬⎪⎪⎭
(t) =
∫
BH2
r (P)∩W
(K
1/4
H2(x,x;t) −K
1/4
W (x,x;t))dx
=
∫
BH2
r (P)∩W
L−1
⎧⎪⎪⎨⎪⎪⎩
s ↦H
1/4(x,x;s)
⎫⎪⎪⎬⎪⎪⎭
(t)dx.
(3.35)
In other words, we may interchange the order of integration and L−1. Using (3.35) and
(3.34), we obtain for all t > 0:
−
∫
BH2
r (P)∩W
L−1
⎧⎪⎪⎨⎪⎪⎩
s ↦H
1/4(x,x;s)
⎫⎪⎪⎬⎪⎪⎭
(t)dx
= −1
2 L−1
⎧⎪⎪⎨⎪⎪⎩
s ↦
r
∫
0
P√s−1
2(cosh(a))Q√s−1
2(cosh(a))sinh(a)da
⎫⎪⎪⎬⎪⎪⎭
(t)
+ γ
π2 L−1
⎧⎪⎪⎨⎪⎪⎩
s ↦
∞
∫
0
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))sinh((π −γ)ρ)
sinh(γρ)
dρ sinh(a)da
⎫⎪⎪⎬⎪⎪⎭
(t)
−Aγ(t;r)
The above inverse Laplace transforms can be computed explicitly as we will show in
Lemma 3.14-3.16 below. From Lemma 3.14 we know for all t > 0:
−1
2L−1
⎧⎪⎪⎨⎪⎪⎩
r
∫
0
P√s−1
2(cosh(a))Q√s−1
2(cosh(a))sinh(a)da
⎫⎪⎪⎬⎪⎪⎭
(t)
= −2
r
∫
0
π
2
∫
0
K
1/4
H2((a,α),(a,−α);t)sinh(a)dαda,
which is equal to the second summand on the RHS of (3.31).
For the second inverse Laplace transform, we combine Lemma 3.15 below with Lemma
59


---

3 Spectral invariants for polygons
3.16 below to obtain
I ∶= γ
π2L−1
⎧⎪⎪⎨⎪⎪⎩
s ↦
∞
∫
0
∞
∫
0
Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))sinh((π −γ)ρ)
sinh(γρ)
dρ sinh(a)da
⎫⎪⎪⎬⎪⎪⎭
(t)
= γ
π
1
√
4πt
∞
∫
0
e−u2
4t ⋅
e
u
2
eu −1 ⋅⎛
⎝
∞
∫
0
sinh((π −γ)ρ)
sinh(γρ)sinh(ρπ) ⋅sin(ρu)dρ⎞
⎠du.
Further,
sinh((π −γ)ρ)
sinh(γρ)sinh(ρπ) = cosh(ργ)
sinh(ργ) −cosh(ρπ)
sinh(ρπ) = (1 +
2
e2γρ −1) −(1 +
2
e2πρ −1)
= 2(
1
e2γρ −1 −
1
e2πρ −1),
and thus
I = 2γ
π
1
√
4πt
∞
∫
0
e−u2
4t ⋅
e
u
2
eu −1 ⋅⎛
⎝
∞
∫
0
(sin(ρu)
e2γρ −1 −sin(ρu)
e2πρ −1)dρ⎞
⎠du.
From [GR07, 3.911 2], we know that for all u ∈(0,∞), y ∈C with R(y) > 0:
∞
∫
0
sin(ρu)
eyρ −1 dρ = π
2y coth(πu
y ) −1
2u.
Hence,
I = 2γ
π
1
√
4πt
∞
∫
0
e−u2
4t ⋅
e
u
2
eu −1 ⋅(( π
4γ coth(πu
2γ ) −1
2u) −( π
4π coth(πu
2π ) −1
2u))du
= γ
2π
1
√
4πt
∞
∫
0
e−u2
4t ⋅
e
u
2
eu −1 ⋅(π
γ coth(π
γ ⋅u
2) −coth(u
2))du
This is exactly the third term on the RHS of (3.31), such that the proof is completed.
Remark. There also exists a Euclidean version of Theorem 3.12 published in [vdBS88,
Theorem 2]. In their article van den Berg and Srisatkunarajah proved that formula
in order to compute the heat invariants for Euclidean polygons. Besides, this formula
is used by Mazzeo and Rowlett in [MR15] to study the so-called heat trace anomaly
on Euclidean polygons, which refers to the fact that the third heat invariant is not
continuous with respect to Lipschitz convergence of domains in the Euclidean plane. In
the last paragraph of [MR15] the authors point out that an analogous formula for higher
dimensional Euclidean wedges would be needed in order to generalise their results for
higher dimensional polyhedra.
In the remaining part of this section we will prove three lemmas which we promised
60


---

3 Spectral invariants for polygons
and already used in the proof of Theorem 3.12.
Lemma 3.13. For all ν ∈(−1,∞) and a > 0:
(i)
1
π
π
∫
0
Qν (cosh(d((a, α
2 ),(a,−α
2 ))))dα = Pν (cosh(a))Qν (cosh(a)).
(3.36)
(ii)
2
π
∞
∫
0
sinh(πρ)
π ⋅ρ
Q−iρ
ν (cosh(a))Qiρ
ν (cosh(a))dρ = Pν(cosh(a))Qν(cosh(a)).
(3.37)
Proof. Let ν ∈(−1,∞) and a ∈(0,∞) be given. Using (3.13) and Corollary 2.30, we have
for all b ∈(0,∞):
1
π
π
∫
0
Qν (cosh(d((a, α
2 ),(b,−α
2 ))))dα
= 1
π
π
∫
0
Qν (cosh(a)cosh(b) −sinh(a)sinh(b)cos(α))dα
= 2
π2
π
∫
0
∞
∫
0
cosh(ρ(π −α))Q−iρ
ν (cosh(b))Qiρ
ν (cosh(a))dρdα
= 2
π2
∞
∫
0
⎛
⎝
π
∫
0
cosh(ρ(π −α))dα⎞
⎠Q−iρ
ν (cosh(b))Qiρ
ν (cosh(a))dρ
= 2
π
∞
∫
0
sinh(ρπ)
π
⋅1
ρ Q−iρ
ν (cosh(b))Qiρ
ν (cosh(a))dρ.
(3.38)
Note also that we used the Fubini-Tonelli theorem for the third equality, which is allowed
due to Theorem 2.25. More precisely,
2
π2
∞
∫
0
π
∫
0
∣cosh(ρ(π −α))Q−iρ
ν (cosh(b))Qiρ
ν (cosh(a))∣dα dρ
= 2
π2
∞
∫
0
⎛
⎝
π
∫
0
cosh(ρ(π −α))dα⎞
⎠∣Q−iρ
ν (cosh(b))Qiρ
ν (cosh(a))∣dρ
= 2
π
∞
∫
0
sinh(ρπ)
π
⋅1
ρ ∣Q−iρ
ν (cosh(b))Qiρ
ν (cosh(a))∣dρ < ∞.
61


---

3 Spectral invariants for polygons
(i). From (3.38) and (2.46) we obtain for all b ∈(0,∞) with a < b:
1
π
π
∫
0
Qν (cosh(d((a, α
2 ),(b,−α
2 ))))dα = Pν (cosh(a))Qν (cosh(b)).
(3.39)
Let (bn)n∈N ⊂(a,∞) be any sequence with bn > bn+1 for all n ∈N and limn→∞bn = a. By
continuity of (0,∞) ∋b ↦Qν (cosh(b)) ∈R,
Pν (cosh(a))Qν (cosh(a)) = lim
n→∞Pν (cosh(a))Qν (cosh(bn))
= lim
n→∞
1
π
π
∫
0
Qν(cosh(d((a,α),(bn,0))))dα,
(3.40)
where we used (3.39) and cosh(d((a, α
2 ),(bn,−α
2 ))) = cosh(d((a,α),(bn,0))) for the last
equality. Thus, it remains to show
lim
n→∞
1
π
π
∫
0
Qν(cosh(d((a,α),(bn,0))))dα = 1
π
π
∫
0
Qν(cosh(d((a,α),(a,0))))dα.
Note that for all α ∈(0,π),
ϕ ∶[a,∞) ∋b ↦cosh(d((a,α),(b,0)) = cosh(a)cosh(b) −sinh(a)sinh(b)cos(α) ∈(0,∞)
is strictly increasing because ϕ′′(b) = ϕ(b) > 0 for all b > a and ϕ′(a) > 0. Moreover, the
function Qν ∶(1,∞) ∋x ↦Qν(x) →R is non-negative and strictly decreasing, which can
be seen from (2.51). Thus, by the monotone convergence theorem, we have
lim
n→∞
1
π
π
∫
0
Qν(cosh(d((a,α),(bn,0))))dα = 1
π
π
∫
0
Qν(cosh(d((a,α),(a,0))))dα.
Hence, using the above equation and (3.40), we have
Pν (cosh(a))Qν (cosh(a)) = 1
π
π
∫
0
Qν(cosh(d((a,α),(a,0))))dα
= 1
π
π
∫
0
Qν (cosh(d((a, α
2 ),(a,−α
2 ))))dα,
which closes the proof of (i).
(ii). The second statement follows immediately from (i) and (3.38) with b ∶= a.
We first discovered the following Laplace transform in Lemma 3.14 by performing
the inverse Laplace transform with the complex inversion formula. Even though the
calculations in connection with the complex inversion formula are instructive, we will
62


---

3 Spectral invariants for polygons
compute the Laplace transform directly for the sake of a shorter proof.
Lemma 3.14. For all a,r > 0 the following Laplace transform exists and is given for all
s ∈H> 1
4 by
L{t ↦4
r
∫
0
π
2
∫
0
K
1/4
H2((a,α),(a,−α);t)sinh(a)dαda}(s)
=
r
∫
0
P√s−1
2(cosh(a))Q√s−1
2(cosh(a))sinh(a)da.
(3.41)
Proof. Let a,r > 0 be arbitrary. Note that for all t > 0:
4
π
2
∫
0
K
1/4
H2 ((a,α),(a,−α);t)dα = 2
π
∫
0
K
1/4
H2 ((a, α
2 ),(a,−α
2 );t)dα.
Thus, by the Fubini-Tonelli theorem, (3.10), and (3.36) we have for all s > 1
4:
∞
∫
0
e−st ⋅4
r
∫
0
π
2
∫
0
K
1/4
H2 ((a,α),(a,−α);t)sinh(a)dα dadt
=
∞
∫
0
e−st ⋅2
r
∫
0
π
∫
0
K
1/4
H2 ((a, α
2 ),(a,−α
2 );t)sinh(a)dα dadt
= 2
r
∫
0
sinh(a)
π
∫
0
∞
∫
0
e−stK
1/4
H2 ((a, α
2 ),(a,−α
2 );t) dtdα da
=
r
∫
0
sinh(a) 1
π
π
∫
0
Q√s−1
2 (cosh(d((a, α
2 ),(a,−α
2 ))))dα da
=
r
∫
0
sinh(a)P√s−1
2 (cosh(a))Q√s−1
2 (cosh(a)) da.
Note that the application of the Fubini-Tonelli theorem is justified in the second equality
above, since s > 1
4 and therefore all functions under the integral sign are positive.
We have shown that the Laplace integral is convergent and equal to ∫
r
0 P√s−1
2 (cosh(a))⋅
Q√s−1
2 (cosh(a))sinh(a)da for all s > 1
4. Thus, by Proposition 2.8, the Laplace transform
of t ↦4∫
r
0 ∫
π
2
0 K
1/4
H2((a,α),(a,−α);t)sinh(a)dα da exists for all s ∈H> 1
4. Moreover, that
Laplace transform must be equal to ∫
r
0 P√s−1
2(cosh(a))Q√s−1
2(cosh(a))sinh(a)da for all
s ∈H> 1
4, because both are holomorphic on that domain.
63


---

3 Spectral invariants for polygons
Lemma 3.15. For all s ∈C/(−∞,0], ρ ∈R:
∞
∫
1
Q−iρ
√s−1
2(x)Qiρ
√s−1
2(x)dx =
π
2sinh(ρπ) ⋅
1
2i√s ⋅
⋅(ψ (√s + iρ + 1
2) −ψ (√s −iρ + 1
2)),
(3.42)
where
ψ(z) ∶= Γ′(z)
Γ(z)
(3.43)
is the logarithmic derivative of the gamma function, also called psi-function.
Proof. From [Rob59, vol. II, equation (395) on p. 200] we know that for all ν, µ ∈C such
that R(ν) > −1
2, R(µ) ∈(−1,1) ∶
(2ν + 1)
∞
∫
1
Qµ
ν(x)Qµ
ν(x)dx =
πei2µπ
2sin(µπ) ⋅Γ(ν + µ + 1)
Γ(ν −µ + 1) ⋅
⋅(ψ (ν + µ + 1) −ψ (ν −µ + 1)).
(3.44)
We want to remark that Robin uses a different notation in his book than we do above, in
particular his psi-function is shifted by 1 compared with (3.43). The relevant notation
used in [Rob59, vol. II] is defined at the beginning of the book on page VII.
Let s ∈C/(−∞,0], ρ ∈R and set ν ∶= √s −1
2, µ ∶= iρ. Then (3.44) is equivalent to
∞
∫
1
Qiρ
√s−1
2(x)Qiρ
√s−1
2(x)dx =
πe−2ρπ
2isinh(ρπ) ⋅Γ(√s + iρ + 1
2)
Γ(√s −iρ + 1
2) ⋅
1
2√s⋅
⋅(ψ (√s + iρ + 1
2) −ψ (√s −iρ + 1
2)).
Thus using (2.15), we obtain:
∞
∫
1
Q−iρ
√s−1
2(x)Qiρ
√s−1
2(x)dx = e2ρπ Γ(√s −iρ + 1
2)
Γ(√s + iρ + 1
2)
∞
∫
1
Qiρ
√s−1
2(x)Qiρ
√s−1
2(x)dx
=
π
2sinh(ρπ) ⋅
1
2i√s ⋅(ψ (√s + iρ + 1
2) −ψ (√s −iρ + 1
2)).
It remains to compute one inverse Laplace transform. Luckily, this can be easily
deduced from a known Laplace transform and using an abstract property of the Laplace
transform.
64


---

3 Spectral invariants for polygons
Lemma 3.16. Let ρ ∈R and t ∈(0,∞). Further, let
F ∶H>0 ∋s ↦1
2i ⋅1
√s (ψ (√s + iρ + 1
2) −ψ (√s −iρ + 1
2)) ∈C.
Then L−1 {F} exists, and
L−1 {F}(t) =
1
√
πt
∞
∫
0
e−u2
4t ⋅
e
u
2
eu −1 ⋅sin(ρu)du.
(3.45)
Proof. From [GR07, 3.311 7] we know for all ν, µ ∈C with R(ν), R(µ) > 0 ∶
∞
∫
0
e−µt −e−νt
1 −e−t
dt = ψ(ν) −ψ(µ).
(3.46)
Let ρ ∈R and s ∈H>0. Further, set µ ∶= s −iρ + 1
2 and ν ∶= s + iρ + 1
2. Then (3.46) gives
ψ (s + iρ + 1
2) −ψ (s −iρ + 1
2) =
∞
∫
0
e−(s−iρ+ 1
2 )t −e−(s+iρ+ 1
2 )t
1 −e−t
dt
=
∞
∫
0
e−st ⋅
e−t
2
1 −e−t ⋅(eiρt −e−iρt)dt
=
∞
∫
0
e−st ⋅
e
t
2
et −1 ⋅2isin(ρt)dt.
In other words, if f(t) ∶=
e
t
2
et−1 sin(ρt) for t > 0, then
L{f}(s) = 1
2i (ψ (s + iρ + 1
2) −ψ (s −iρ + 1
2))
for all s ∈H>0. Hence, it follows from [PBM92, 29 on p. 5] that
L
⎧⎪⎪⎨⎪⎪⎩
t ↦
1
√
πt
∞
∫
0
e−u2
4t f(u)du
⎫⎪⎪⎬⎪⎪⎭
(s) = 1
√s ⋅1
2i ⋅(ψ (√s + iρ + 1
2) −ψ (√s −iρ + 1
2))
for s ∈H>0. Proposition 2.8 now implies the statement.
65


---

3 Spectral invariants for polygons
3.2 Heat invariants for hyperbolic polygons
Let Ω⊂H2 be a hyperbolic polygon. We are now ready to compute the heat invariants
for Ω, i.e. to compute the asymptotic expansion of the heat trace
ZΩ(t) = ∫
Ω
KΩ(x,x;t)dx.
The coefficients in the asymptotic expansion will depend, in particular, on the number
and the size of the angles. So let us assume Ωhas M angles γ1,...,γM ∈(0,2π] where
M ≥3 is an integer.
The method we use in order to compute the asymptotic expansion of ZΩ(t) is known
as the principle of not feeling the boundary and was first formulated by M. Kac (see
[Kac66]). According to this principle the heat kernels KΩ(x,x;t) and KH2(x,x;t) have
the same asymptotic expansion as t ↘0 for fixed x ∈Ω. In other words, the short time
asymptotic behaviour of the heat kernel does not “feel” the presence of the boundary.
Let us put this principle on a sound basis by the following lemma. We note that the
lemma below is somewhat more general than it is needed in this section, but we will
make use of it in full generality in subsequent sections.
Lemma 3.17. Let N be a two-dimensional complete Riemannian manifold whose Gaus-
sian curvature is bounded. Let U ⊂N be an arbitrary domain and let A ⊂N be a compact
subset such that A ⊂U. Then there exist constants T, C, D > 0 such that
∣KN(x,y;t) −KU(x,y;t)∣≤C
t ⋅e−D
t
for all x,y ∈A, t ∈(0,T].
(3.47)
Proof. First choose a relatively compact domain G ⊂N with smooth boundary ∂G and
such that A ⊂G ⊂U. This is always possible: Consider a so-called cutoff function of A in
U (see [Gri09, Theorem 3.5]), i.e. a smooth function ϕ ∈C∞
c (U) such that 0 ≤ϕ ≤1 and
ϕ ≡1 in a neighborhood of A. By Sard’s theorem (see [Lee13, Theorem 6.10]) there are
infinitely many regular values of ϕ in the interval (0,1). Now choose any regular value
g ∈(0,1) and define G ∶= ϕ−1(g,∞).
By the minimality of the heat kernel we have for all x,y ∈G and t > 0:
KG(x,y;t) ≤KU(x,y;t) ≤KN(x,y;t),
and thus
0 ≤KN(x,y;t) −KU(x,y;t) ≤KN(x,y;t) −KG(x,y;t).
(3.48)
Let y ∈A be fixed. The function u ∶G × (0,∞) →R, u(x,t) ∶= KN(x,y;t) −KG(x,y;t)
is (by definition) a smooth non-negative solution to the heat equation on G × (0,∞).
Moreover, it can be extended continuously to G × [0,∞) by the following procedure:
If we set u(x,t) ∶= 0 for all t = 0, x ∈G then we obtain a continuous function on
G × [0,∞) (see [Gri09, Exercise 9.7]). Since the boundary ∂G is smooth, KG(⋅,y;⋅) can
66


---

3 Spectral invariants for polygons
be extended continuously to G × (0,∞) by KG(x,y;t) ∶= 0 for all x ∈∂G and t > 0
(see also the remark after Proposition 2.4). Thus u(x,t) can be extended continuously
by u(x,t) ∶= KN(x,y;t) for all x ∈∂G, t > 0. Alltogether, we have extended u(x,t)
continuously to G × (0,∞) ∪G × {0} as follows:
u(x,t) =
⎧⎪⎪⎪⎪⎨⎪⎪⎪⎪⎩
KN(x,y;t) −KG(x,y;t),
if (x,t) ∈G × (0,∞),
0,
if (x,t) ∈G × {0},
KN(x,y;t),
if (x,t) ∈∂G × (0,∞).
It remains to show that u(x,t) can be extended continuously to ∂G × {0}. We obtain a
continuous extension when we set u(x,0) ∶= 0 for all x ∈∂G, which follows directly from
the existence of constants ˜T, C > 0 such that
0 ≤u(x,t) ≤KN(x,y;t) ≤C
t ⋅e−d(x,y)2
16t
for all (x,t) ∈G × (0, ˜T].
The last estimate given above is well-known. If N is non-compact, then it follows from
[CLY81, Theorem 4] and because of the fact that inf{i(x) ∣x ∈G} > 0, where i(x)
denotes the injectivity radius of x (see [Kli95, Proposition 2.1.10]). It is also explained in
[CLY81, remark on p. 1050] how to prove the same estimate as in [CLY81, Theorem 4] if
N is compact. However, there is a simpler proof if N is compact. If N is closed, then
the estimate follows from [Gri97, Theorem 1.1] together with the well-known asymptotic
expansion for KN(x,x;t) as t ↘0, which holds uniformly in x ∈N (see e.g. [Don79,
Theorem 3.3]).
Thus we can apply the parabolic maximum principle (see [Gri09, Theorem 8.10]) to
u(x,t) in order to obtain for all x ∈G and t ∈(0, ˜T]:
u(x,t) ≤
max
(z,s)∈G×[0,t]u(z,s) =
max
(z,s)∈G×{0}∪
∂G×(0,t)
u(z,s)
=
max
(z,s)∈∂G×(0,t)u(z,s)
≤max
s∈(0,t)
C
s ⋅e−d(∂G,y)2
16s
,
(3.49)
where d(∂G,y) ∶= infz∈∂G d(z,y).
We set D ∶= d(∂G,A)2
16
> 0, where d(∂G,A) ∶= infy∈A d(∂G,y). Let T ∈(0,D) ∩(0, ˜T) be
fixed and let C > 0 be as above. The function s ↦C
s ⋅e−D
s is monotonically increasing in
s ∈(0,D). Hence it follows from (3.48) and (3.49) that for all x,y ∈A and t ∈(0,T]:
0 ≤KN(x,y;t) −KU(x,y;t) ≤max
s∈(0,t)
C
s ⋅e−D
s = C
t ⋅e−D
t
In order to approximate the heat kernel KΩ(x,x;t) for points x ∈Ωclose to the
67


---

3 Spectral invariants for polygons
boundary ∂Ωit is helpful to use the following probabilistic formula for the heat kernel.
An introduction to (conditional) Wiener measures on Riemannian manifolds, written for
geometers, can be found in [BP11]. All other probabilistic notions we use can be found,
for example, in [Hsu02]. Again, we formulate the next lemma more general than it is
needed in this section in view of applications appearing later in this thesis.
Lemma 3.18. Let N be a two-dimensional complete Riemannian manifold whose Gaus-
sian curvature is bounded. Let U ⊂N be any domain. Then we have for all x,y ∈U and
t > 0:
KU(x,y;t) = KN(x,y;t) ⋅Prob{ω(s) ∈U, 0 ≤s ≤t ∣ω(0) = x, ω(t) = y },
(3.50)
where ω ∶[0,t] →N denotes a continuous curve such that ω(0) = x and ω(t) = y and
Prob{...∣...} is the normalised conditional Wiener measure. (The measure is normalised
in the sense that it is equal to the conditional Wiener measure as in [BP11, Proposition
3.15] multiplied by
1
KN(x,y;t) so that it becomes a probability measure).
Proof. It is well-known that if the Gaussian curvature is bounded from below, then
the volume of any geodesic disc in N increases at most exponentially. This follows by
comparison with a space of constant curvature (see e.g. [Pet06, Lemma 35 on p. 269]).
Thus N is stochastically complete (see [Gri09, Theorem 11.8]), and therefore the results
from [BP11, Section 3.4] are valid in our situation.
Let us introduce some notation. We denote the set of continuous paths in N starting
at x ∈N by Cx([0,∞); N). In other words, for any x ∈N
Cx([0,∞); N) ∶= {ω ∶[0,∞) →N ∣ω is continuous and ω(0) = x}.
Similarly, for any x,y ∈N, t > 0 we set
Cx([0,t]; N) ∶= {ω ∶[0,t] →N ∣ω is continuous and ω(0) = x},
Cy
x([0,t]; N) ∶= {ω ∶[0,t] →N ∣ω is continuous and ω(0) = x, ω(t) = y }.
By a curve we mean any element of one of the above sets. If x ∈U then the first exit time
from U of a curve ω is defined as
τU(ω) ∶= inf{s > 0 ∣ω(s) ∉U }.
If the curve ω never leaves the set U, i.e. if {s > 0 ∣ω(s) ∉U} = ∅, then we set τU(ω) ∶= ∞
with the convention that t < ∞for all t ∈[0,∞). Finally, let
1{ t<τU }(ω) ∶=
⎧⎪⎪⎨⎪⎪⎩
1, if t < τU(ω),
0, otherwise.
We first assume that U is a relatively compact domain with smooth boundary and
prove (3.50) for this case. In this special case, it is well-known that for any bounded
68


---

3 Spectral invariants for polygons
Borel function f ∶U →R, any x ∈U and t > 0:
∫
U
f(y) ⋅KU(x,y;t)dy =
∫
Cx([0,∞); N)
f(ω(t)) ⋅1{ t<τU}(ω)dPx(ω),
(3.51)
where Px denotes the Wiener measure on Cx([0,∞); N) as in [BP11, Section 3.4]. A
proof of (3.51) can be found in [Hsu02, Proposition 4.1.3]. Compare also with [Gri06,
Theorem 8.6].
Moreover, let Pt
x denote the Wiener measure on Cx([0,t]; N) and let Pt
x,y denote the
conditional Wiener measure on Cy
x([0,t]; N) as in [BP11, Section 3]. We have (see [BP11,
Remark 3.20])
Pt
x = (restt)∗Px,
(3.52)
where restt ∶Cx([0,∞); N) →Cx([0,t]; N), ω ↦ω∣[0,t], is the restriction map. When we
use in the following order (3.51), and (3.52) combined with the transformation rule, and
then [BP11, Lemma 2.24] we obtain for any x ∈U and t > 0:
∫
U
f(y) ⋅KU(x,y;t)dy =
∫
Cx([0,∞); N)
f(ω(t)) ⋅1{ t<τU}(ω)dPx(ω)
=
∫
Cx([0,∞); N)
f(restt(ω)(t)) ⋅1{ t<τU}(restt(ω))dPx(ω)
=
∫
Cx([0,t]; N)
f(ω(t)) ⋅1{ t<τU}(ω)dPt
x(ω)
= ∫
N
∫
Cy
x([0,t]; N)
f(ω(t)) ⋅1{ t<τU}(ω)dPt
x,y(ω)dy
= ∫
U
f(y) ⋅
∫
Cy
x([0,t]; N)
1{ t<τU}(ω)dPt
x,y(ω)dy.
Note that we have used [BP11, Lemma 2.24] for the fourth equation above, where the
metric measure space in Lemma 2.24 of [BP11] is taken as explained at the beginning of
Section 3 in [BP11]. Recall that f was an arbitrary bounded Borel function on U and
x ∈U, t > 0 were arbitrary as well. Thus for all x ∈U and t > 0 we have:
KU(x,y;t) =
∫
Cy
x([0,t]; N)
1{ t<τU}(ω)dPt
x,y(ω)
for almost all y ∈U. We show that this equality is actually true for all y ∈U. For this
purpose, let us define
qU(x,y;t) ∶=
∫
Cy
x([0,t]; N)
1{ t<τU}(ω)dPt
x,y(ω)
69


---

3 Spectral invariants for polygons
for all x,y ∈U and t > 0. One can prove exactly as in [Szn98, Proposition 3.1], that for
all x,y ∈U and t,s > 0:
qU(x,y;t) = qU(y,x;t),
qU(x,y;t + s) = ∫
U
qU(x,z;t)qU(z,y;s)dz.
Thus we obtain for all x,y ∈U, t > 0:
qU(x,y;t) = ∫
U
qU (x,z; t
2)qU (z,y; t
2)dz = ∫
U
KU (x,z; t
2)qU (y,z; t
2)dz
= ∫
U
KU (x,z; t
2)KU (y,z; t
2)dz
= KU(x,y;t),
where we have used twice that for all x ∈U, t > 0: KU(x,y;t) = qU(x,y;t) for almost all
y ∈U. For the last equality we have used the semigroup identity of the heat kernel (see
[Gri09, Theorem 7.13]). Finally we have (by definition) for all x,y ∈U and t > 0:
KN(x,y;t) ⋅Prob{ω(s) ∈U, 0 ≤s ≤t ∣ω(0) = x, ω(t) = y } =
∫
Cy
x([0,t]; N)
1{ t<τU}(ω)dPt
x,y(ω).
Therefore the claimed equation (3.50) is established for relatively compact domains U
with smooth boundary.
If U is an arbitrary domain, then we proceed as follows. Consider a sequence (Un)n∈N of
relatively compact domains with smooth boundary, such that U = ∪∞
n=1Un and Un ⊂Un+1
for all n ∈N. For all n ∈N we extend the domain of the heat kernel KUn(x,y;t) to
U × U × (0,∞) by setting KUn(x,y;t) ∶= 0 whenever x or y lies outside of Un. On the one
hand, it is well-known (see [Dod83] or [Cha84, Theorem 4 on p. 188]) that
KU(x,y;t) = lim
n→∞KUn(x,y;t)
for all x,y ∈U, t > 0.
On the other hand, from Lebesgue’s monotone convergence theorem, we have for all
x,y ∈U, t > 0:
lim
n→∞
∫
Cy
x([0,t]; N)
1{ t<τUn}(ω)dPt
x,y(ω) =
∫
Cy
x([0,t]; N)
1{ t<τU}(ω)dPt
x,y(ω).
When we put everything together we obtain for all x,y ∈U and t > 0:
KU(x,y;t) = lim
n→∞KUn(x,y;t) = lim
n→∞
∫
Cy
x([0,t]; N)
1{ t<τUn}(ω)dPt
x,y(ω)
70


---

3 Spectral invariants for polygons
=
∫
Cy
x([0,t]; N)
1{ t<τU}(ω)dPt
x,y(ω)
= KN(x,y;t) ⋅Prob{ω(s) ∈U, 0 ≤s ≤t ∣ω(0) = x, ω(t) = y }.
We now return to the hyperbolic polygon Ωwith interior angles γ1,...,γM. We will
approximate the values KΩ(x,x;t) of the heat kernel by simpler functions applying
Lemma 3.17. The approximating functions will depend on the location of the point x ∈Ω.
For this reason, we will decompose the polygon into three subsets, denoted by ΩV ,ΩE
and ΩI. Roughly speaking, the set ΩV will consist of all points which are close to a vertex;
the set ΩE will contain all points which are close to an edge but away from the vertices;
and the set ΩI will contain all points away from the boundary ∂Ω. Let us define these
subsets in an exact manner.
Recall that d(x,y) denotes the (hyperbolic) distance for any x,y ∈H2 and BH2
r (P) =
{x ∈H2 ∣d(x,P) < r } for r > 0 and P ∈H2. For any i ∈{1,...,M } let Wi ⊂H2 be the
wedge corresponding to the interior angle γi as in Definition 3.5. Let us denote the vertex
of Wi by Pi ∈H2 for all i = 1,...,M. For all r > 0 and i = 1,...,M we define
Wr(Pi) ∶= BH2
r (Pi) ∩Wi = {p ∈Wi ∣d(p,Pi) < r },
and let
R ∶= 1
2 sup{r > 0∣Wr(Pj) ∩Wr(Pk) = ∅, ∀j ≠k;
M
⋃
ℓ=1
Wr(Pℓ) ⊂Ω}.
The set of points close to the vertices is defined as
ΩV ∶=
M
⋃
i=1
WR(Pi).
(3.53)
Note that the sets WR(P1),..., WR(PM) are pairwise disjoint.
The set ΩE is defined as follows. Let ˜
M ∈N be the number of edges and let E1,...,E ˜
M
denote all the edges of the polygon Ω(recall Definition 3.4). By definition, the edges
have no common points except for vertices. For all ˜δ > 0 and j = 1,..., ˜
M we define the set
ΩEj(˜δ) ∶= {p ∈Ω∣p ∉ΩV , d(p,Ej) < ˜δ }.
We can choose δ = δ(Ω) > 0 such that ΩEk(δ) ∩ΩEℓ(δ) = ∅, for all k, ℓ∈{1,..., ˜
M} with
k ≠ℓ. Let us fix such a constant once and for all. Now define
ΩE ∶= Ω∂Ω(δ) ∶= {p ∈Ω∣p ∉ΩV , d(p,∂Ω) < δ } =
˜
M
⋃
j=1
ΩEj(δ).
(3.54)
Also let ΩEj ∶= ΩEj(δ) for all j ∈{1,..., ˜
M}. Thus for any point p ∈ΩE there exists a
71


---

3 Spectral invariants for polygons
unique edge Ej, j ∈{1,.., ˜
M}, which is the closest to p among all edges. Note that for any
j ∈{1,..., ˜
M } the set ΩEj may have one or two connected components. More precisely, if
∣Ej∣= 2 ⋅L(Ej), where the notation is to be understood as in Definition 3.6, then ΩEj
has exactly two connected components, and otherwise only one. Also note that ΩE has
exactly M connected components, i.e. the number of angles of Ωand the number of
connected components of ΩE is the same.
The remaining points will constitute the points away from the boundary, i.e.
ΩI ∶= Ω/(ΩV ∪ΩE) = {p ∈Ω∣p ∉ΩV , p ∉ΩE }.
(3.55)
Now that we have established the decomposition of the polygon, we can apply the
principle of not feeling the boundary.
Lemma 3.19. There exist constants T,C,D > 0, such that for all t ∈(0,T], i ∈{1,...,M }
and j ∈{1,..., ˜
M } ∶
(i)
∣KΩ(x,x;t) −KH2(x,x;t)∣≤C
t e−D
t
for all x ∈ΩI.
(3.56)
(ii)
∣KΩ(x,x;t) −KEj(x,x;t)∣≤C
t e−D
t
for all x ∈ΩEj,
(3.57)
where KEj(x,x;t) ∶= KHj(x)(x,x;t) and KHj(x) denotes the heat kernel of the half-
plane Hj ∶= Hj(x) ⊂H2 bounded by the line which contains the edge Ej and with
x ∈Hj.
(iii)
∣KΩ(x,x;t) −Kγi(x,x;t)∣≤C
t e−D
t
for all x ∈WR(Pi),
(3.58)
where Kγi is the heat kernel of the wedge Wi.
Proof. From Lemma 3.17 we know that there exist T1,C1,D1 > 0 such that
∣KΩ(x,x;t) −KH2(x,x;t)∣≤C1
t e−D1
t
for all x ∈ΩI, t ∈(0,T1].
(3.59)
Next, we will use Lemma 3.17 and Lemma 3.18 in order to estimate the left-hand side
of (3.57) and then of (3.58) as in [vdBS88, Lemma 6 and 7]. Let j ∈{1,..., ˜
M } be given,
let x ∈ΩEj, and let Fj denote the geodesic line containing the edge Ej. With Lemma 3.18
we have
KΩ(x,x;t) = KH2(x,x;t) ⋅Prob{ω(s) ∈Ω, 0 ≤s ≤t ∣ω(0) = x = ω(t)}
72


---

3 Spectral invariants for polygons
≤KH2(x,x;t) ⋅Prob{ω(s) ∉Ej, 0 ≤s ≤t ∣ω(0) = x = ω(t)}
≤KH2(x,x;t) ⋅Prob{ω(s) ∉Fj, 0 ≤s ≤t ∣ω(0) = x = ω(t)}
+ KH2(x,x;t) ⋅Prob{ω(s) ∈Fj/Ej for some s ∈[0,t] ∣ω(0) = x = ω(t)}
= KEj(x,x;t) + KH2(x,x;t)
−KH2(x,x;t) ⋅Prob{ω(s) ∈H2/(Fj/Ej), 0 ≤s ≤t ∣ω(0) = x = ω(t)}
= KEj(x,x;t) + KH2(x,x;t) −KH2/(Fj/Ej)(x,x;t).
Note that we used in particular the following implications with respect to any continuous
curve ω ∶[0,t] →H2 with ω(0) = x = ω(t): ω stays in Ω⇒ω does not meet Ej ⇒ω does
not meet Fj or meets Fj/Ej, and: ω does not meet Fj ⇔ω stays in Hj.
Thus from Lemma 3.17 we know that there exist ˜T j
2, ˜Cj
2, ˜Dj
2 > 0 such that for all
t ∈(0, ˜T j
2], x ∈ΩEj:
KΩ(x,x;t) ≤KEj(x,x;t) +
˜Cj
2
t e−
˜
Dj
2
t .
(3.60)
Similarly, we have for all x ∈ΩEj:
KΩ(x,x;t) = KH2(x,x;t) ⋅Prob{ω(s) ∈Ω, 0 ≤s ≤t ∣ω(0) = x = ω(t)}
= KH2(x,x;t) ⋅Prob{ω(s) ∉∂Ω, 0 ≤s ≤t ∣ω(0) = x = ω(t)}
≥KH2(x,x;t) ⋅Prob{ω(s) ∉Fj, 0 ≤s ≤t ∣ω(0) = x = ω(t)}
−KH2(x,x;t) ⋅Prob{ω(s) ∈∂Ω/Fj for some s ∈[0,t] ∣ω(0) = x = ω(t)}
= KEj(x,x;t) −(KH2(x,x;t) −KH2/(∂Ω/Fj)(x,x;t)).
We used in particular the following implications for any continuous curve ω ∶[0,t] →H2
with ω(0) = x = ω(t): ω stays in Ω⇔ω does not meet ∂Ω; ω does not meet Fj ⇒ω does
not meet ∂Ωor meets ∂Ω/Fj.
Thus it follows again from Lemma 3.17 that there exist constants ˆT j
2, ˆCj
2, ˆDj
2 > 0 such
that for all t ∈(0, ˆT j
2], x ∈ΩEj:
KΩ(x,x;t) ≥KEj(x,x;t) −
ˆCj
2
t e−
ˆ
Dj
2
t .
(3.61)
When we combine the estimates (3.60) and (3.61) and we set T2 ∶= min∪˜
M
j=1{ ˜T j
2, ˆT j
2},
C2 ∶= max ∪˜
M
j=1{ ˜Cj
2, ˆCj
2}, D2 ∶= min∪˜
M
j=1{ ˜Dj
2, ˆDj
2}, then we have for all j ∈{1,..., ˜
M }:
∣KΩ(x,x;t) −KEj(x,x;t)∣≤C2
t e−D2
t
for all x ∈ΩEj, t ∈(0,T2].
(3.62)
Now consider (3.58) and let i ∈{1,...,M} be given. For any r > 0 we set Ei(r) ∶=
∂BH2
r (Pi) ∩Wi = {p ∈Wi ∣d(p,Pi) = r }. Because of W2R(Pi) ⊂Ω, we have for all
73


---

3 Spectral invariants for polygons
x ∈WR(Pi):
KΩ(x,x;t) ≥KH2(x,x;t) ⋅Prob{ω(s) ∈W2R(Pi), 0 ≤s ≤t ∣ω(0) = x = ω(t)}
≥KH2(x,x;t) ⋅Prob{ω(s) ∈Wi, 0 ≤s ≤t ∣ω(0) = x = ω(t)}
−KH2(x,x;t) ⋅Prob{ω(s) ∈Ei(2R) for some s ∈[0,t] ∣ω(0) = x = ω(t)}
= Kγi(x,x;t) −(KH2(x,x;t) −KH2/Ei(2R)(x,x;t)).
We used the following implications valid for any continuous curve ω ∶[0,t] →H2 with
ω(0) = x = ω(t): ω stays in Ω⇒ω stays in W2R(Pi); ω stays in Wi ⇒ω stays in W2R(Pi)
or meets Ei(2R). Hence, using Lemma 3.17, there exist T i
3,Ci
3,Di
3 > 0 such that for all
x ∈WR(Pi), t ∈(0,T i
3]:
KΩ(x,x;t) ≥Kγi(x,x;t) −Ci
3
t e−
Di
3
t .
(3.63)
Similarly, for all x ∈WR(Pi):
KΩ(x,x;t) ≤KH2(x,x;t) ⋅Prob{ω(s) ∈Wi, 0 ≤s ≤t ∣ω(0) = x = ω(t)}
+ KH2(x,x;t) ⋅Prob{ω(s) ∈Ei(2R) for some s ∈[0,t] ∣ω(0) = x = ω(t)}
= Kγi(x,x;t) + (KH2(x,x;t) −KH2/Ei(2R)(x,x;t)).
We used above the following implication which holds for any continuous curve ω ∶[0,t] →
H2 with ω(0) = x = ω(t): ω stays in Ω⇒ω stays in Wi or meets Ei(2R). Thus we have
KΩ(x,x;t) ≤Kγi(x,x;t) + Ci
3
t e−
Di
3
t
for all x ∈WR(Pi), t ∈(0,T i
3].
(3.64)
Let T3 ∶= min∪M
i=1{T i
3}, C3 ∶= max ∪M
i=1{Ci
3}, D3 ∶= min∪M
i=1{Di
3}. From (3.63) and (3.64)
it follows that for all i ∈{1,...,M }:
∣KΩ(x,x;t) −Kγi(x,x;t)∣≤C3
t e−D3
t
for all x ∈WR(Pi), t ∈(0,T3].
(3.65)
Lastly, all three estimates (i) −(iii) follow from (3.59), (3.62) and (3.65), when we set
T ∶= min{T1,T2,T3 }, C ∶= max{C1,C2,C3 }, and D ∶= min{D1,D2,D3 }.
Instead of applying the above lemma to the heat trace directly, we will use it to
approximate the shifted heat trace
Z
1/4
Ω(t) ∶= e
1
4 t ⋅ZΩ(t) = ∫
Ω
K
1/4
Ω(x,x;t)dx
(3.66)
and compute its asymptotic expansion as t ↘0. Of course the two functions ZΩand Z
1/4
Ω
are closely related to each other, but the formulas for the coefficients in the asymptotic
expansion of Z
1/4
Ω(t) as t ↘0 are shorter than for ZΩ(t).
74


---

3 Spectral invariants for polygons
Because of the preceding lemma we can approximate the shifted heat trace as follows.
Corollary 3.20. There exist constants T,C′,D > 0 such that for all t ∈(0,T] ∶
∣Z
1/4
Ω(t) −∫
ΩI
K
1/4
H2(x,x;t)dx −
˜
M
∑
j=1 ∫
ΩEj
K
1/4
Ej(x,x;t)dx −
M
∑
i=1
∫
WR(Pi)
K
1/4
γi (x,x;t)dx∣≤C′
t e−D
t ,
where K
1/4
H2,K
1/4
Ej and K
1/4
γi denote the corresponding shifted heat kernels as in (3.5).
Proof. We decompose the polygon into the pairwise disjoint subsets from (3.53)-(3.55):
Ω= ΩI ∪ΩE ∪ΩV = ΩI ∪(
˜
M
⋃
j=1
ΩEj) ∪(
M
⋃
i=1
WR(Pi)).
Let T,C,D > 0 be as in Lemma 3.19 and C′ ∶= ∣Ω∣e
T
4 ⋅C. Then for all t ∈(0,T]:
∣Z
1/4
Ω(t) −∫
ΩI
K
1/4
H2(x,x;t)dx −
˜
M
∑
j=1 ∫
ΩEj
K
1/4
Ej(x,x;t)dx −
M
∑
i=1
∫
WR(Pi)
K
1/4
γi (x,x;t)dx∣=
∣∫
ΩI
(K
1/4
Ω(x,x;t) −K
1/4
H2(x,x;t))dx +
˜
M
∑
j=1 ∫
ΩEj
(K
1/4
Ω(x,x;t) −K
1/4
Ej(x,x;t))dx
+
M
∑
i=1
∫
WR(Pi)
(K
1/4
Ω(x,x;t) −K
1/4
γi (x,x;t))dx∣≤
∫
ΩI
∣K
1/4
Ω(x,x;t) −K
1/4
H2(x,x;t)∣dx +
˜
M
∑
j=1 ∫
ΩEj
∣K
1/4
Ω(x,x;t) −K
1/4
Ej(x,x;t)∣dx
+
M
∑
i=1
∫
WR(Pi)
∣K
1/4
Ω(x,x;t) −K
1/4
γi (x,x;t)∣dx ≤
⎛
⎝∣ΩI∣+
˜
M
∑
j=1
∣ΩEj∣+
M
∑
i=1
∣WR(Pi)∣⎞
⎠e
T
4 C
t e−D
t = C′
t e−D
t .
Corollary 3.20 shows that the shifted heat trace Z
1/4
Ω(t) has the same asymptotic
expansion for t ↘0 as the function
t ↦∫
ΩI
K
1/4
H2(x,x;t)dx +
˜
M
∑
j=1 ∫
ΩEj
K
1/4
Ej(x,x;t)dx +
M
∑
i=1
∫
WR(Pi)
K
1/4
γi (x,x;t)dx.
(3.67)
For any i ∈{1,...,M } an explicit formula for the function ∫WR(Pi) K
1/4
γi (x,x;t)dx is given
75


---

3 Spectral invariants for polygons
by Theorem 3.12. Furthermore, we have for all j = 1,..., ˜
M and x ∈ΩEj
KEj(x,x;t) = KHj(x,x;t) = KH2(x,x;t) −KH2(x,xEj;t),
where xEj denotes the image of x ∈Hj under the reflection in ∂Hj. This follows from the
following Lemma.
Lemma 3.21. Let H ⊂H2 be a half-plane. The heat kernel of H is given for all x,y ∈H
and t > 0 by
KH(x,y;t) = KH2(x,y;t) −KH2(x,y∂H;t),
where y∂H denotes the reflection of y in the boundary ∂H.
Proof. This follows immediately, if we set γ = π in (3.27) and then perform the inverse
Laplace transform. Alternatively, the statement can also be shown directly by using the
definition of KH2 and [Gri09, Theorem 9.7].
Thus (3.67) is equal to
∫
Ω
K
1/4
H2(x,x;t)dx
−
⎛
⎜⎜
⎝
˜
M
∑
j=1 ∫
ΩEj
K
1/4
H2(x,xEj;t)dx
⎞
⎟⎟
⎠
−M ⋅2
R
∫
0
π
2
∫
0
K
1/4
H2((a,α),(a,−α);t)sinh(a)dαda
+
M
∑
i=1
γi
2π
∞
∫
0
e−u2
4t
√
4πt
⋅
e
u
2
eu −1 ⋅( π
γi
coth( π
γi
⋅u
2) −coth(u
2))du
−
M
∑
i=1
Aγi(t;R).
(3.68)
Each line of (3.68) defines a function in t ∈(0,∞), which we denote (including the signs)
in successive order by Z
1/4
I (t), Z
1/4
E (t), Z
1/4
V (t), and A(t), respectively. We will compute the
asymptotic expansion of each function separately for t ↘0. It will turn out that Z
1/4
I (t)
produces the contributions from the interior of the polygon, i.e. those parts which depend
on the volume ∣Ω∣of the polygon. Similarly, Z
1/4
E (t) produces the contributions from the
edges of the polygon, i.e. those parts which depend on the length of the perimeter ∣∂Ω∣.
Further, Z
1/4
V (t) produces the contributions from the vertices of the polygon, i.e. those
parts which depend on the angles of the polygon. The function A(t) will not give any
contribution to the asymptotic expansion as t ↘0.
The remaining part of this section will be devoted to the asymptotic expansion of
each of these functions. In the process, we will encounter the Bernoulli numbers Bk and
76


---

3 Spectral invariants for polygons
Bernoulli polynomials Bk(x), which are defined by the following generating function:
text
et −1 =∶
∞
∑
k=0
Bk(x)tk
k!
for ∣t∣< 2π;
Bk ∶= Bk(0).
(3.69)
By an easy computation one can prove the identity Bk (1 −x) = (−1)k Bk(x) for all k ∈N0
and thus
B2k+1 (1
2) = 0
for all k ∈N0.
(3.70)
Both Bernoulli numbers and Bernoulli polynomials will appear naturally in the asymptotic
expansion of the (shifted) heat trace, or more precisely, in all the coefficients which depend
explicitly on the volume ∣Ω∣or the interior angles γ1,...,γM of the polygon. This resembles
the situation for spherical polygons discussed in [Wat05]. Indeed, as explained already at
the beginning of Chapter 3, a later comparison between the heat invariants for spherical
and hyperbolic polygons will show that the corresponding parts which depend on either
the volume ∣Ω∣, the perimeter ∣∂Ω∣or the angles of the polygon differ at most in sign.
We begin with asymptotic expansions of the first three terms in (3.68), namely the
functions Z
1/4
I (t), Z
1/4
E (t) and Z
1/4
V (t). The central tool for computing the asymptotic
expansions for these functions is Watson’s lemma, due to G. N. Watson.
Lemma 3.22. (see [BH86], p.103) Let f ∶(0,∞) →R be a continuous function such that
there exists a constant c > 0 with f(x) = O(ecx) as x →∞. If f(x) has an asymptotic
expansion of the form
f(x)
x↓0∼
∞
∑
k=0
akxρk−1
with 0 < ρ0 < ρ1 < ... ↗∞, then it follows that
∞
∫
0
f(x)e−x
t dx
t↓0∼
∞
∑
k=0
ak ⋅Γ(ρk) ⋅tρk.
Our approach will always be the same. Using the Fubini-Tonelli theorem and substitu-
tion, we will bring those functions into a form to which Watson’s lemma is applicable.
By formula (3.9) for the heat kernel of the hyperbolic plane, the first term is
Z
1/4
I (t) ∶= ∫
Ω
K
1/4
H2(x,x;t)dx =
∣Ω∣
(4πt)
3
2
∞
∫
0
√
2 ⋅r
√
coshr −1
e−r2
4t dr.
(3.71)
Thus we need to compute the asymptotic expansion of the integral expression on the
right-hand side of (3.71).
77


---

3 Spectral invariants for polygons
Lemma 3.23. Let f(r) ∶=
√
2⋅r
√
cosh r−1. Then
∞
∫
0
f(r)e−r2
4t dr
t↓0∼
∞
∑
k=0
2√π ⋅B2k ( 1
2)
k!
tk+ 1
2.
(3.72)
Proof. First we will compute the asymptotic expansion of f(r) as r ↘0. The function
f is obviously smooth and bounded on (0,∞) and can even be extended to a smooth
function on the whole real line R by the following identity:
f(r) =
√
2 ⋅r
√
coshr −1
=
2r
e
r
2 −e−r
2 = 2 re
r
2
er −1.
Hence, by (3.69) we get
f(r)
r↓0∼
∞
∑
k=0
2 ⋅Bk( 1
2)
k!
rk.
By (3.70), B2k+1 ( 1
2) = 0 for all k ∈N0 and hence we can write the expansion also as
f(r)
r↓0∼
∞
∑
k=0
2 ⋅B2k( 1
2)
(2k)! r2k.
(3.73)
We will now use Watson’s lemma to get the expansion we claimed. We first substite r by
2√r and get
∞
∫
0
f(r)e−r2
4t dr = ∫
∞
0
f (2√r)
√r
e−r
t dr =
∞
∫
0
˜f(r)e−r
t dr,
where ˜f(r) ∶=
f(2√r)
√r
. From (3.73) it follows that
˜f(r)
r↓0∼
∞
∑
k=0
22k+1 ⋅B2k ( 1
2)
(2k)! ⋅r(k+ 1
2 )−1.
Hence by Watson’s lemma we get
∞
∫
0
˜f(r)e−r
t dr
t↓0∼
∞
∑
k=0
22k+1 ⋅B2k ( 1
2)
(2k)! ⋅Γ(k + 1
2) ⋅tk+ 1
2.
(3.74)
From [GR07, 8.339 2], we know that for all k ∈N0
Γ(k + 1
2) = (2k)!
22k ⋅k! ⋅√π.
(3.75)
When we combine (3.74) with (3.75), then the claimed asymptotic expansion (3.72)
78


---

3 Spectral invariants for polygons
follows.
One easily deduces the asymptotic expansion of ZI(t) ∶= e−t
4 ⋅Z
1/4
I (t) as t ↘0 from the
preceding lemma and (3.71):
Corollary 3.24.
(i)
Z
1/4
I (t)
t↓0∼∣Ω∣
4πt
∞
∑
k=0
B2k ( 1
2)
k!
tk.
(3.76)
(ii)
ZI(t)
t↓0∼∣Ω∣
4πt
∞
∑
k=0
˜iktk,
(3.77)
where ˜ik ∶= 1
k!
k
∑
ℓ=0
(k
ℓ)(−1
4)
k−ℓB2ℓ( 1
2).
In order to compare the above coefficients with the corresponding coefficients for
spherical polygons given in [Wat05], we rewrite (3.77) appropriately. Because of ˜i0 =
B0 ( 1
2) = 1, we can alternatively write the asymptotic expansion as
ZI(t)
t↓0∼∣Ω∣
4πt +
∞
∑
k=0
iH
k ⋅tk,
(3.78)
where
iH
k ∶= ∣Ω∣
4π ⋅˜ik+1 = ∣Ω∣
4π ⋅
1
(k + 1)!
k+1
∑
ℓ=0
(k + 1
ℓ)(−1
4)
k+1−ℓ
B2ℓ(1
2).
(3.79)
If we compare the coefficients iH
k with the corresponding coefficients for spherical
polygons given in [Wat05, equation (28) of Corollary 3] - which we denote unlike Watson
as iS
k - we see the relation iH
k = (−1)k+1 iS
k for all k ∈N0. (Note that in [Wat05, equation
(28)] the constant ∣Ω∣
4π is actually completely missing because of a typo). As we mentioned
before, that relation between iH
k and iS
k jibes with general facts from [BG90]. It follows
from [BG90] that iH
k and iS
k are given by a formula of the form ∣Ω∣⋅ck ⋅κk+1, where ck ∈R
is some universal constant, κ denotes the Gaussian curvature of H2 and S2, respectively,
and Ωrepresents a hyperbolic or spherical polygon, as appropriate. Note that H2 and
S2 have constant Gaussian curvature equal to −1 and 1, respectively. In particular, the
covariant derivatives of the Riemannian curvature tensor vanish and hence all curvature
invariants vanish as well, except for powers of the Gaussian (or sectional) curvature.
We now compute the asymptotic expansion of the second term in (3.68), namely the
79


---

3 Spectral invariants for polygons
function
Z
1/4
E (t) ∶= −
⎛
⎜⎜
⎝
˜
M
∑
j=1 ∫
ΩEj
K
1/4
H2(x,xEj;t)dx
⎞
⎟⎟
⎠
−M ⋅2
R
∫
0
π
2
∫
0
K
1/4
H2((a,α),(a,−α);t)sinh(a)dαda.
(3.80)
Recall that the sets ΩEj, j = 1,..., ˜
M, are pairwise disjoint, and ΩE = ∪˜
M
j=1ΩEj has M
connected components. Moreover, ΩEj consists of two connected components if and only
if ∣Ej∣= 2 ⋅L(Ej), and only one connected component if and only if ∣Ej∣= L(Ej) (see
Definition 3.6).
Let C be any connected component of ΩE. Let ℓ∈{1,..., ˜
M} be the unique index such
that C ⊂ΩEℓ. We will compute the asymptotic expansion of
I
1/4
C (t) ∶= ∫
C
K
1/4
H2(x,xEℓ;t)dx + 2
R
∫
0
π
2
∫
0
K
1/4
H2((a,α),(a,−α);t)sinh(a)dαda
=
∫
Q1
R∪C∪Q2
R
K
1/4
H2(x,xEℓ;t)dx,
where Q1
R,Q2
R denote the quarter circles shown in Fig. 3.3. More precisely, let y ∈C be
fixed and let ˜P, ˆP ∈H2 be the endpoints of the edge Eℓ. Then Q1
R and Q2
R denote the
quarter circles with radius R and center ˜P and ˆP, respectively, bounded on one side by
Eℓand such that Q1
R ∪C ∪Q2
R ⊂Hℓ(y).
Eℓ
C
Ω
Q1
R
Q2
R
Eℓ
C
Ω
Q2
R
Q1
R
Figure 3.3: Quarter circles
We decompose both quarter circles such that
Q1
R = S1 ∪(Q1
R/S1),
Q2
R = S2 ∪(Q2
R/S2),
where
S1 ∶= {x ∈Q1
R ∣d(x,Eℓ) ≤δ },
80


---

3 Spectral invariants for polygons
S2 ∶= {x ∈Q2
R ∣d(x,Eℓ) ≤δ }.
Thus
Q1
R ∪C ∪Q2
R = (S1 ∪C ∪S2)
´¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¶
=∶S
⋃((Q1
R/S1) ∪(Q2
R/S2))
´¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¶
=∶Λ
,
and, since S and Λ are disjoint,
I
1/4
C (t) = ∫
Λ
K
1/4
H2(x,xEℓ;t)dx + ∫
S
K
1/4
H2(x,xEℓ;t)dx.
The first integral does not give any contribution to the asymptotic expansion, because of
the estimate (3.28) and since
d(x,xEℓ) ≥2δ
for all x ∈Λ.
When we choose Fermi coordinates (ρ,σ) with base line Eℓ, where ρ denotes the distance
to Eℓ, we can parametrise the set S as follows:
S = {(ρ,σ) ∣0 ≤σ ≤L(Eℓ); 0 ≤ρ ≤δ },
where L(Eℓ) denotes the length of the edge Eℓ. Since d(x,xEℓ) = 2ρ for any x = (ρ,σ),
and the Riemannian metric g is given in Fermi coordinates as g = dρ2 + cosh2(ρ)dσ2 (see
e.g. [Bus92, formula (1.1.9)]), we get with (3.9):
∫
S
K
1/4
H2(x,xEℓ;t)dx = L(Eℓ)
(4πt)
3
2
δ
∫
0
∞
∫
2ρ
√
2 ⋅r cosh(ρ)
√
coshr −cosh(2ρ)
⋅e−r2
4t dr dρ.
(3.81)
Again, we need to determine the asymptotic expansion of the integral expression on the
right-hand side of (3.81).
Lemma 3.25. Let g(r,ρ) ∶=
√
2⋅r cosh(ρ)
√
cosh r−cosh(2ρ). Then
δ
∫
0
∞
∫
2ρ
g(r,ρ) ⋅e−r2
4t dr dρ
t↓0∼π
∞
∑
k=0
δ0ktk+1,
(3.82)
where δ0k is the Kronecker delta, i.e.
δ0k ∶=
⎧⎪⎪⎨⎪⎪⎩
1, if k = 0,
0, if k ≥1.
81


---

3 Spectral invariants for polygons
Proof. By using first the Fubini-Tonelli theorem and then substituting r by 2√r, we get
δ
∫
0
∞
∫
2ρ
g(r,ρ) ⋅e−r2
4t dr dρ =
∞
∫
0
min{δ, r
2 }
∫
0
g(r,ρ) ⋅e−r2
4t dρdr
=
∞
∫
0
⎛
⎜
⎝
min{δ,√r}
∫
0
g(2√r,ρ)
√r
dρ
⎞
⎟
⎠
⋅e−r
t dr
=
∞
∫
0
G(r) ⋅e−r
t dr,
(3.83)
where
G(r) ∶=
min{δ,√r}
∫
0
g(2√r,ρ)
√r
dρ.
In order to use Watson’s lemma we need to determine the asymptotic expansion of G(r)
as r ↘0. We claim that for all r ∈(0,δ2) the function G(r) is constant and equal to π.
By using the identity cosh(2x) = 2sinh2(x) + 1 we get for all r ∈(0,δ2):
G(r) =
min{δ,√r}
∫
0
g(2√r,ρ)
√r
dρ = 2 ⋅
√r
∫
0
cosh(ρ)
√
sinh2(√r) −sinh2 (ρ)
dρ
= 2
sinh(√r)
∫
0
1
√
sinh2(√r) −ρ2 dρ = 2
1
∫
0
1
√
1 −ρ2 dρ = π.
Thus we have shown, in particular, that
G(r)
r↓0∼
∞
∑
k=0
(πδ0k)r(k+1)−1.
By Watson’s lemma we immediately get
∞
∫
0
G(r)e−r
t dr
t↓0∼π
∞
∑
k=0
δ0k ⋅Γ(k + 1) ⋅tk+1 = π ⋅t + 0 ⋅t2 + 0 ⋅t3 + ....
(3.84)
Thus the lemma follows from (3.84) and (3.83).
Corollary 3.26.
∫
S
K
1/4
H2(x,xEi;t)dx
t↓0∼L(Eℓ)
8
√
πt
⋅
∞
∑
k=0
δ0k ⋅tk,
(3.85)
82


---

3 Spectral invariants for polygons
where δ0k is the Kronecker delta.
From the discussion above, we know that the right-hand side of (3.85) also gives the
asymptotic expansion of I
1/4
C (t) as t ↘0. This in turn gives us the asymptotic expansion
of Z
1/4
E (t) as follows. By definition, if C1,...,CM are all the connected components of ΩE,
then we have
Z
1/4
E (t) = −
M
∑
i=1
I
1/4
Ci (t).
Thus, from Corollary 3.26 we obtain the following asymptotic expansions.
Corollary 3.27.
(i)
Z
1/4
E (t)
t↓0∼−∣∂Ω∣
8
√
πt
⋅
∞
∑
k=0
δ0k ⋅tk,
(3.86)
where ∣∂Ω∣=
˜
M
∑
j=1∣Ej∣, and ∣Ej∣is defined as in Definition 3.6.
(ii)
ZE(t)
t↓0∼−∣∂Ω∣
8
√
πt
⋅
∞
∑
k=0
˜bk ⋅tk,
(3.87)
where ZE(t) ∶= e−t
4 ⋅Z
1/4
E (t) and ˜bk ∶= (−1
4)
k 1
k!.
Let us rewrite the asymptotic expansion of ZE(t), such that its coefficients can better
be compared with their spherical counterparts. Since ˜b0 = 1 we can alternatively write
the asymptotic expansion (3.87) as
ZE(t)
t↓0∼−∣∂Ω∣
8
√
πt
+
∞
∑
k=0
bH
k ⋅tk+ 1
2,
(3.88)
where
bH
k ∶= −∣∂Ω∣
8√π ⋅˜bk+1 = ∣∂Ω∣
(−1)k
4k+2 ⋅√π ⋅2 ⋅(k + 1)!
for all k ∈N0.
(3.89)
When we compare the coefficients bH
k with the corresponding spherical coefficients bS
k
from [Wat05, formula (27)], we see that bH
k = (−1)k+1bS
k. Similarly as for the coefficients
contributed from the interior of a polygon, that relation between bH
k and bS
k holds because of
the following fact. The constants bH
k and bS
k are given by a formula of the form ∣∂Ω∣⋅dk⋅κk+1,
where dk ∈R is some universal constant and κ denotes the Gaussian curvature of H2 and
S2, respectively (see [BG90]). Note that the geodesic curvature of any edge of Ωvanishes
so that the boundary does not contribute any curvature invariants.
83


---

3 Spectral invariants for polygons
Consider now the third term in (3.68), i.e.
Z
1/4
V (t) ∶=
M
∑
i=1
γi
2π
∞
∫
0
e−u2
4t
√
4πt
⋅
e
u
2
eu −1 ⋅( π
γi
coth( π
γi
⋅u
2) −coth(u
2))du.
Let i ∈{ 1,..,M } be arbitrary and consider
I
1/4
γi (t) ∶= γi
2π
1
√
4πt
∞
∫
0
e−u2
4t ⋅
e
u
2
eu −1 ⋅( π
γi
coth( π
γi
⋅u
2) −coth(u
2))du.
We first compute the asymptotic expansion of the above integral expression with
Watson’s lemma.
Lemma 3.28. Let q(u) ∶=
e
u
2
eu−1 ( π
γi coth( π
γi ⋅u
2) −coth( u
2)). Then
∞
∫
0
e−u2
4t q(u)du
t↓0∼
∞
∑
k=0
ak(γi) ⋅tk+ 1
2,
(3.90)
where
ak(γi) ∶=
k+1
∑
ℓ=1
(2k + 2
2ℓ)B2k−2ℓ+2 ( 1
2) ⋅B2ℓ⋅√π
(k + 1)!(2k + 1)
(( π
γi
)
2ℓ
−1).
(3.91)
Proof. Substituting u by 2√u, we obtain
∞
∫
0
e−u2
4t q(u)du =
∞
∫
0
e−u
t q (2√u)
√u
´¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¶
=∶q1(u)
du.
Because of Watson’s lemma it remains to compute the asymptotic expansion of q1(u) as
u ↘0. On the other hand, it is more convenient to compute the asymptotic expansion of
q2(u) ∶= q1(u2), since then the roots will not appear during the calculations. We have:
q2(u) = q1(u2) = q (2u)
u
= 1
u2 ⋅u ⋅eu
e2u −1 ⋅( π
γi
coth( π
γi
⋅u) −coth(u)).
(3.92)
As we see, q2 is a product of simple functions whose asymptotic expansions are easily
computed as follows.
By definition of the Bernoulli polynomials, we know for all u ∈R with ∣u∣< π:
u ⋅eu
e2u −1 = 1
2
2u ⋅eu
e2u −1 = 1
2
∞
∑
k=0
Bk (1
2) (2u)k
k!
= 1
2
∞
∑
k=0
B2k (1
2)4k u2k
(2k)!,
(3.93)
where we have used (3.70) for the last equality.
84


---

3 Spectral invariants for polygons
Let us investigate the last term in (3.92). Observe that coth(x) = 1 +
2
e2x−1 for all
x ∈R/{0}. Further, the odd Bernoulli numbers are given by B1 = −1
2 and B2k+1 = 0 for all
k ∈N. Hence, for all u ∈R/{0} with ∣u∣< min{π,γi }:
π
γi
coth( π
γi
⋅u) −coth(u) = π
γi
−1 + 1
u (
2 π
γiu
e
2 π
γi u −1
−
2u
e2u −1)
= π
γi
−1 + 1
u
⎛
⎜⎜
⎝
∞
∑
k=0
Bk
(2 π
γiu)
k
k!
−
∞
∑
k=0
Bk
(2u)k
k!
⎞
⎟⎟
⎠
= π
γi
−1 + 1
u
∞
∑
k=1
(( π
γi
)
k
−1)2kBk
uk
k!
= 1
u
∞
∑
k=2
(( π
γi
)
k
−1)2kBk
uk
k!
= 1
u
∞
∑
k=1
(( π
γi
)
2k
−1)22kB2k
u2k
(2k)!
= 2 ⋅
∞
∑
k=0
(( π
γi
)
2k+2
−1)22k+1B2k+2
u2k+1
(2k + 2)!.
(3.94)
Thus we get from (3.92), (3.93) and (3.94), for all 0 < u < min{π,γi }:
q2(u) = 1
u
∞
∑
k=0
B2k (1
2)4k u2k
(2k)! ⋅
∞
∑
ℓ=0
(( π
γi
)
2ℓ+2
−1)22ℓ+1B2ℓ+2
u2ℓ
(2ℓ+ 2)!
= 1
u
∞
∑
k=0
k
∑
ℓ=0
B2(k−ℓ) (1
2)4k−ℓ
u2(k−ℓ)
(2(k −ℓ))! (( π
γi
)
2ℓ+2
−1)22ℓ+1B2ℓ+2
u2ℓ
(2ℓ+ 2)!
= 1
u
∞
∑
k=0
k
∑
ℓ=0
(2k + 2
2ℓ+ 2) ⋅B2(k−ℓ) (1
2) ⋅B2ℓ+2 ⋅4k ⋅2 ⋅(( π
γi
)
2ℓ+2
−1)
u2k
(2k + 2)!
= 1
u
∞
∑
k=0
k+1
∑
ℓ=1
(2k + 2
2ℓ) ⋅B2k−2ℓ+2 (1
2) ⋅B2ℓ⋅2 ⋅(( π
γi
)
2ℓ
−1)4k
u2k
(2k + 2)!.
Thus for all 0 < u < min{π2,γ2
i }:
q1(u) = q2(√u)
=
∞
∑
k=0
k+1
∑
ℓ=1
(2k + 2
2ℓ) ⋅B2k−2ℓ+2 (1
2) ⋅B2ℓ⋅2 ⋅(( π
γi
)
2ℓ
−1) ⋅4k u(k+ 1
2 )−1
(2k + 2)!.
This establishes the asymptotic expansion of q1(u) as u ↘0. Applying Watson’s lemma
we obtain
∞
∫
0
e−u
t q1(u)du
t↓0∼
∞
∑
k=0
Γ(k + 1
2)⋅
85


---

3 Spectral invariants for polygons
⋅
k+1
∑
ℓ=1
(2k + 2
2ℓ) ⋅B2k−2ℓ+2 (1
2) ⋅B2ℓ⋅2 ⋅(( π
γi
)
2ℓ
−1) ⋅4k
tk+ 1
2
(2k + 2)!.
The coefficient for k = 0 in the above asymptotic expansion equals by Γ( 1
2) = √π:
√πB0 (1
2) ⋅B2 ⋅(( π
γi
)
2
−1) = a0(γi).
For the other coefficients, we use the doubling formula (see e.g. [GR07, 8335 1] or [Tem96,
formula (3.5)])
Γ(z)Γ(z + 1
2) = 21−2z√πΓ(2z).
(3.95)
In particular this implies for all k ∈N:
Γ(k + 1
2) = 2
22k
√πΓ(2k)
Γ(k) = 2
22k
√π(2k −1)!
(k −1)! .
Hence, using (2k−1)!
(k−1)! ⋅
1
(2k+2)! = 1
4 ⋅
1
(k+1)!⋅(2k+1):
∞
∫
0
e−u
t q1(u)du
t↓0∼
∞
∑
k=0
k+1
∑
ℓ=1
(2k + 2
2ℓ)B2k−2ℓ+2 ( 1
2) ⋅B2ℓ⋅√π
(k + 1)!(2k + 1)
(( π
γi
)
2ℓ
−1)
´¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¶
=ak(γi)
⋅tk+ 1
2.
Corollary 3.29.
I
1/4
γi (t)
t↓0∼
∞
∑
k=0
cH
k (γi) ⋅tk,
(3.96)
where
cH
k (γi) ∶=
γi
4π√π ⋅ak(γi) = γi
π
k+1
∑
ℓ=1
(2k + 2
2ℓ) B2k−2ℓ+2 ( 1
2) ⋅B2ℓ
4 ⋅(k + 1)!(2k + 1) (( π
γi
)
2ℓ
−1)
=
k+1
∑
ℓ=1
(2k + 2
2ℓ) B2k−2ℓ+2 ( 1
2) ⋅B2ℓ
4 ⋅(k + 1)!(2k + 1) ⋅π2ℓ−γ2ℓ
i
π ⋅γ2ℓ−1
i
.
(3.97)
Since
Z
1/4
V (t) =
M
∑
i=1
I
1/4
γi (t),
we obtain the following corollary.
86


---

3 Spectral invariants for polygons
Corollary 3.30.
(i)
Z
1/4
V (t)
t↓0∼
∞
∑
k=0
cH
k ⋅tk,
(3.98)
where cH
k ∶=
M
∑
i=1cH
k (γi).
(ii)
ZV (t)
t↓0∼
∞
∑
k=0
νH
k ⋅tk,
(3.99)
where ZV (t) ∶= e−t
4 ⋅Z
1/4
V (t) and νH
k ∶=
k
∑
ℓ=0
1
(k−ℓ)! (−1
4)
k−ℓcH
ℓ.
Remark. Observe that when we compare our coefficients cH
k (γi) given in (3.97) with the
corresponding spherical coefficients cS
k(γi) (see [Wat05, formula (22)]), then we have
cH
k (γi) = (−1)kcS
k(γi). Hence, when we compare νH
k with its spherical counterpart νS
k in
[Wat05, formula (29)], we still have the relation νH
k = (−1)kνS
k. As we will see later, there
is a deeper reason why the latter relation must hold if γi = π
k for some k ∈N.
Finally, let us show that
A(t) ∶=
M
∑
i=1
Aγi(t;R)
(3.100)
produces no contribution to the asymptotic expansion as t ↘0.
Lemma 3.31. Let i ∈{1,...,M } and Aγi(t;R) be the function defined in (3.32). Then
for all m ∈N ∶
Aγi(t;R) = o(tm), as t ↘0.
(3.101)
Proof. Recall Aγi(t;R) = L−1 {F}(t) with
F(s) ∶=
∞
∫
R
∞
∫
0
γi
π2Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))sinh(ρ(π −γi))
sinh(ργi)
sinh(a)dρda
for s ∈H> 1
4. Let us first find an appropriate upper bound for the product of the associated
Legendre functions under the integral sign. From (2.52) we have for all a > 0, s ∈H> 1
4
and ρ ≥0:
∣Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))∣≤
1
4R(√s)+ 1
2 ⋅∣Γ(√s + 1
2 + iρ) ⋅Γ(√s + 1
2 −iρ)
Γ(√s + 1
2)2
∣⋅
87


---

3 Spectral invariants for polygons
⋅
1
cosh(a) −1 ⋅⎛
⎝
π
∫
0
(
1 −cos2(t)
cosh(a) + cos(t))
R(√s)
dt⎞
⎠
2
.
The same argument as in (2.66) shows 0 <
1−cos2(t)
cosh(a)+cos(t) ≤2e−a for all t ∈(0,π) and thus
∣Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))∣≤
π2e−2aR(√s)
2(cosh(a) −1)⋅
⋅∣Γ(√s + 1
2 + iρ) ⋅Γ(√s + 1
2 −iρ)
Γ(√s + 1
2)2
∣
(3.102)
for all a > 0, s ∈H> 1
4 and ρ ≥0.
We will estimate the above quotient of gamma functions. Note that,
∣Γ(√s + 1
2 + iρ) ⋅Γ(√s + 1
2 −iρ)
Γ(√s + 1
2)2
∣= ∣B (√s + 1
2 + iρ,√s + 1
2 −iρ) ⋅Γ(2(√s + 1
2))
Γ(√s + 1
2)2 ∣,
where B denotes the beta function (see [EMOT53, formula (5) on p. 9]). From [EMOT53,
formula (24) on p. 11] and because R(√s) −1
2 > 0 for all s ∈H> 1
4, we have
∣B (√s + 1
2 + iρ,√s + 1
2 −iρ)∣≤
∞
∫
0
e−(R(√s)+ 1
2 )t (et −1
et
)
R(√s)−1
2
dt
=
∞
∫
0
e−R(√s)(2t−ln(et−1))
1
√
et −1
dt.
Observe that the function (0,∞) ∋t ↦2t −ln(et −1) ∈R has a global minimum at
t = ln(2) where the minimal value is ln(4). Thus, by Laplace’s method (see e.g. [Olv97,
Theorem 7.1] or [BH86, formula (5.1.21)]), there exists a constant C1 > 0 such that for
all ρ ≥0 and s ∈H> 1
4:
∣B (√s + 1
2 + iρ,√s + 1
2 −iρ)∣≤C1 ⋅e−R(√s) ln(4)
R(√s)
1
2
.
Further, using the doubling formula (3.95) and then the asymptotic estimate (2.24), there
exists some constant C2 > 0 such that for all s ∈H> 1
4:
∣Γ(2(√s + 1
2))
Γ(√s + 1
2)2 ∣= ∣4R(√s)
√π
⋅Γ(√s + 1)
Γ(√s + 1
2)∣≤C2 ⋅4R(√s) ⋅(R(√s))
1
2.
Hence, there exists C > 0 such that for all ρ ≥0, a > 0, and s ∈H> 1
4:
∣Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))∣≤
C
cosh(a) −1 ⋅e−2aR(√s).
(3.103)
88


---

3 Spectral invariants for polygons
We consider two cases. Case 1: γi > π
2:
From the converse to Watson’s lemma (see [Won01, proof on p. 31]) it suffices to show,
for each m ∈N, that F(s) = o( 1
sm) as ∣s∣→∞with s ∈H> 1
4.
By assumption, ∣π −γi∣< γi and thus, by [GR07, 3.981 5],
∞
∫
0
sinh(ρ∣π −γi∣)
sinh(ργi)
dρ = π
2γi
⋅
sin (π ∣π−γi∣
γi )
1 + cos(π ∣π−γi∣
γi )
.
(3.104)
With C > 0 as in the upper bound (3.103), we have for all s ∈H> 1
4, noting that
2 ⋅R(√s) ≥
√
∣s∣for these s:
∣F(s)∣≤γi
π2
∞
∫
R
∞
∫
0
∣Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))∣sinh(a) ⋅sinh(ρ∣π −γi∣)
sinh(ργi)
dρda
≤
C ⋅γi sinh(R)
π2(cosh(R) −1)
∞
∫
R
e−2aR(√s)
∞
∫
0
sinh(ρ∣π −γi∣)
sinh(ργi)
dρda
=
C ⋅sinh(R)
2π(cosh(R) −1) ⋅e−2R R(√s)
2 ⋅R(√s) ⋅
sin(π ∣π−γi∣
γi )
1 + cos(π ∣π−γi∣
γi )
≤˜C ⋅e−R
√
∣s∣
√
∣s∣
,
where ˜C ∶=
C⋅sinh(R)
2π(cosh(R)−1) ⋅
sin(π ∣π−γi∣
γi
)
1+cos(π ∣π−γi∣
γi
). Since R > 0, we have for all m ∈N: F(s) = o( 1
sm) as
∣s∣→∞with s ∈H> 1
4.
Case 2: γi ∈(0, π
2]:
In this case the above argument will not work, since now π−γi ≥γi and thus the integral
∫
∞
0
sinh(ρ(π−γi))
sinh(ργi)
dρ is not convergent. Instead, we use that for all N ∈N and x,y ∈R:
sinh(x −y) = 2
N
∑
n=1
cosh(x −2ny) ⋅sinh(y) + sinh(x −(2N + 1)y),
which one proves easily using the definition of cosh and sinh. In particular, for all ρ > 0:
sinh(ρ(π −γi))
sinh(ργi)
= 2 ⋅
N
∑
n=1
cosh(ρ(π −2nγi)) + sinh(ρ(π −2Nγi −γi))
sinh(ργi)
.
(3.105)
In the special case γi =
π
2N , this becomes equal to 2 ⋅∑N−1
n=1 cosh(ρ(π −2nγi)) + 1. (These
formulas were also used in [vdBS88, proof of Theorem 2] to estimate the error term.)
89


---

3 Spectral invariants for polygons
Suppose first that there exists some N ∈N with γi =
π
2N . Then for all s ∈H> 1
4:
F(s) =
∞
∫
R
∞
∫
0
γi
π2 Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))sinh(ρ(π −γi))
sinh(ργi)
sinh(a)dρda
= 2
N−1
∑
n=1
∞
∫
R
∞
∫
0
γi
π2 Q−iρ
√s−1
2(cosh(a))⋅
⋅Qiρ
√s−1
2(cosh(a))cosh(ρ(π −2nγi))sinh(a)dρda
+
∞
∫
R
∞
∫
0
γi
π2Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))sinh(a)dρda
= 2γi
N−1
∑
n=1
∞
∫
R
G
1/4
H2 ((a,nγi),(a,−nγi);s)sinh(a)da
+ γi
∞
∫
R
G
1/4
H2 ((a, π
2 ),(a,−π
2 );s)sinh(a)da
= γi
π
N−1
∑
n=1
∞
∫
R
Q√s−1
2 (cosh(d((a,nγi),(a,−nγi))))sinh(a)da
+ γi
2π
∞
∫
R
Q√s−1
2 (cosh(d((a, π
2 ),(a,−π
2 ))))sinh(a)da,
(3.106)
where we used (3.11) for the third equality, and (3.10) for the last one.
Using (2.51) and (2.66), for all s ∈H> 1
4 and (x,y) ∈o-diag(H2):
∣Q√s−1
2 (coshd((x,y)))∣≤
1
cosh(d(x,y)) −1 ⋅e−d(x,y)(R(√s)−1
2 ).
Thus, because of (3.106) and R(√s) −1
2 > 0 for all s ∈H> 1
4, there exists some constant
ε > 0 such that
∣F(s)∣≤N ⋅γi
π e−ε(R(√s)−1
2 )
∞
∫
R
sinh(a)
cosh(a)2 −sinh2(a)cos(2γi) −1 da
=
e−ε(R(√s)−1
2 )
2(1 −cos(2γi))
∞
∫
R
1
sinh(a) da
<
e−ε(R(√s)−1
2 )
2(1 −cos(2γi))
∞
∫
R
6
a3 da
=
3 ⋅e
ϵ
2
2(1 −cos(2γi))R2 ⋅e−εR(√s)
90


---

3 Spectral invariants for polygons
≤
3 ⋅e
ϵ
2
2(1 −cos(2γi))R2 ⋅e−ε
2
√
∣s∣,
where, for the last equality, we used again 2R(√s) ≥
√
∣s∣for all s ∈H> 1
4.
Because ε > 0, we have F(s) = o( 1
sm) as ∣s∣→∞with s ∈H> 1
4 for all m ∈N.
Suppose now there exists N ∈N such that γi ∈(
π
2(N+1), π
2N ). Then one shows again
F(s) = o( 1
sm) as ∣s∣→∞with s ∈H> 1
4 for all m ∈N. This follows along the lines of the
previous two cases, which are discussed above in detail. More precisely, using (3.105), we
have
F(s) =2 ⋅
N
∑
n=1
∞
∫
R
∞
∫
0
γi
π2 Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))cosh(ρ(π −2nγi))sinh(a)dρda
+
∞
∫
R
∞
∫
0
γi
π2 Q−iρ
√s−1
2(cosh(a))Qiρ
√s−1
2(cosh(a))sinh(ρ(π −2Nγi −γi))
sinh(ργi)
sinh(a)dρda.
Now, the first sum can be estimated as we did above. The second summand can be
estimated as in case 1, since ∣π −2Nγi −γi∣< γi.
Finally, as mentioned above, the statement of the lemma follows from the converse to
Watson’s lemma.
Let us summarise the discussion of this section into a theorem.
Theorem 3.32. Let Ω⊂H2 be a hyperbolic polygon with M ≥3 angles and let γ1,...,γM ∈
(0,2π] denote the angles of the polygon. Then
ZΩ(t)
t↓0∼∣Ω∣
4πt −∣∂Ω∣
8
√
πt
+
∞
∑
k=0
(iH
k + bH
k ⋅t
1
2 + νH
k )tk,
(3.107)
where the coefficients are given as follows:
iH
k = ∣Ω∣
4π
1
(k + 1)!
k+1
∑
ℓ=0
(k + 1
ℓ)(−1
4)
k+1−ℓ
B2ℓ(1
2),
bH
k = ∣∂Ω∣
(−1)k
4k+2 ⋅√π ⋅2 ⋅(k + 1)!,
νH
k =
k
∑
ℓ=0
1
(k −ℓ)! (−1
4)
k−ℓ
cH
ℓ,
where
cH
ℓ=
M
∑
i=1
cH
ℓ(γi)
with
cH
ℓ(γi) =
ℓ+1
∑
ν=1
(2ℓ+ 2
2ν ) B2ℓ−2ν+2 ( 1
2) ⋅B2ν
4 ⋅(ℓ+ 1)!(2ℓ+ 1) ⋅π2ν −γ2ν
i
π ⋅γ2ν−1
i
.
91


---

3 Spectral invariants for polygons
3.3 Consequences for polygons
In this section we want to put Theorem 3.32 into a more general context and then derive
some consequences from the heat invariants.
Definition 3.33. Suppose N is an arbitrary two-dimensional complete Riemannian
manifold. For all P ∈N we denote the injectivity radius of P by i(P). Thus we have
i(P) ∈(0,∞]. Furthermore, for all P ∈N and ρ ∈(0,i(P)] we define Bρ(P) ∶= {x ∈N ∣
d(x,P) < ρ}, where d(x,P) denotes the distance between x and P. In other words, the
set Bρ(P) denotes the geodesic disc with radius ρ and center P.
Definition 3.34. A polygon is any relatively compact domain Ω⊂N whose boundary
is a union of finitely many geodesic segments, where N is a two-dimensional complete
Riemannian manifold. If, in addition, N has constant curvature κ ∈R, then Ωis called a
polygon of constant curvature κ.
The terms smooth boundary point, vertex and edge of a polygon are defined analogously
as in Definition 3.4.
Note that according to Definition 3.34 a polygon may have no vertices at all. For
example, a domain in the cylinder S1×R ⊂R3 bounded by two closed geodesics is a polygon
without vertices. Therefore, we regard each smooth and closed boundary component of a
polygon also as an edge of the polygon. Moreover, we allow ∂Ω= ∅as well, namely if N
is compact and Ω= N.
Definition 3.35. Let N be an arbitrary two-dimensional complete Riemannian manifold.
A domain V ⊂N is called a circle sector if there exist P ∈N, ρ ∈(0,i(P)], γ ∈(0,2π]
and polar coordinates (a,α) on Bρ(P) (see [Kli78, Definition 5.3.1]), such that we have
V = {(a,α) ∣0 < a < ρ, 0 < α < γ }.
We call P a vertex of V and we will refer to V as a circle sector at P with angle γ and
radius ρ. Moreover, a circle sector at P with radius ρ = i(P) is also called a wedge.
Note that a circle sector may have several vertices (e.g. a spherical wedge has two
vertices), but a circle sector at P has a unique radius and angle at P.
The angles of a polygon are defined analogously as in Definition 3.5, where we had
defined the angles of hyperbolic polygons. Note that if Ωis a polygon with non-empty
boundary ∂Ωand P ∈∂Ωis fixed, then there exists some ρ ∈(0,i(P)] such that Ω∩Bρ(P)
is a disjoint union of circle sectors at P with radius ρ.
In the following we aim to generalise Theorem 3.32 to polygons of constant curvature.
For that purpose, we need the following local version of Lemma 3.19.
Lemma 3.36. Let N be a two-dimensional complete Riemannian manifold whose Gaus-
sian curvature is bounded, and let Ω⊂N be a polygon.
92


---

3 Spectral invariants for polygons
(i) Let P ∈Ωbe fixed and let ρ > 0 be such that B2ρ(P) ⊂Ω. There exist constants
T1,C1,D1 > 0 such that for all x ∈Bρ(P) and t ∈(0,T1] ∶
0 ≤KΩ(x,x;t) −KB2ρ(P)(x,x;t) ≤C1
t e−D1
t .
(3.108)
(ii) Let Q ∈∂Ωbe fixed and let r > 0 be such that Ω∩B2r(Q) is a disjoint union of circle
sectors at Q with radius 2r. Suppose W2r(Q) denotes one of those circle sectors
with an angle γ ∈(0,2π]. Let Wr(Q) be the circle sector at Q with radius r and
angle γ, which is contained in W2r(Q). Then there exist constants T2,C2,D2 > 0
such that for all x ∈Wr(Q) and t ∈(0,T2] ∶
0 ≤KΩ(x,x;t) −KW2r(Q)(x,x;t) ≤C2
t e−D2
t .
(3.109)
(iii) Let Z ∈N be arbitrary. Suppose we have given for all i ∈{1,2,3} a circle sector
Wri(Z) at Z with angle θ ∈(0,2π] and radius ri ∈(0,i(Z)] such that Wr1(Z) ⊂
Wr2(Z) ⊂Wr3(Z). Then there exist constants T3,C3,D3 > 0 such that for all
x ∈Wr1(Z) and t ∈(0,T3] ∶
0 ≤KWr3(Z)(x,x;t) −KWr2(Z)(x,x;t) ≤C3
t e−D3
t .
(3.110)
Proof. First, let us consider the estimates in (3.108). Since B2ρ(P) ⊂Ω, it follows from
the minimality property of the heat kernel that 0 ≤KΩ(x,x;t) −KB2ρ(P)(x,x;t) for all
x ∈Bρ(P) and t > 0. Further, because of Lemma 3.17 there exist constants T1, ˜C1,D1 > 0
such that for all x ∈Bρ(P) and t ∈(0,T1]:
∣KN(x,x;t) −KΩ(x,x;t)∣≤
˜C1
t e−D1
t , and ∣KN(x,x;t) −KB2ρ(P)(x,x;t)∣≤
˜C1
t e−D1
t .
With C1 ∶= 2 ⋅˜C1 and D1,T1 > 0 as above, we have for all x ∈Bρ(P) and t ∈(0,T1]:
KΩ(x,x;t) −KB2ρ(P)(x,x;t) ≤∣KΩ(x,x;t) −KN(x,x;t)∣+ ∣KN(x,x;t) −KB2ρ(P)(x,x;t)∣
≤C1
t e−D1
t .
This closes the proof of part (i). Now consider (3.109).
As before, because of W2r(Q) ⊂Ωit follows from the minimality of the heat kernel that
0 ≤KΩ(x,x;t) −KW2r(Q)(x,x;t) for all x ∈Wr(Q) and t > 0. The upper estimate follows
as in the proof of Lemma 3.19. More precisely, let E(2r) ∶= {p ∈W2r(Q) ∣d(p,Q) = 2r }.
Using Lemma 3.18, we have for all x ∈Wr(Q) and t > 0:
KΩ(x,x;t) ≤KN(x,x;t) ⋅Prob{ω(s) ∈W2r(Q), 0 ≤s ≤t ∣ω(0) = x = ω(t)}
+ KN(x,x;t) ⋅Prob{ω(s) ∈E(2r) for some s ∈[0,t] ∣ω(0) = x = ω(t)}
93


---

3 Spectral invariants for polygons
= KW2r(Q)(x,x;t) + (KN(x,x;t) −KN/Ei(2R)(x,x;t)).
Thus by Lemma 3.17 there exist constants T2,C2,D2 > 0 such that (3.109) holds.
The proof of part (iii) is analogous as for (ii).
As we have already mentioned, the heat invariants for Euclidean polygons ([vdBS88])
and spherical polygons ([Wat05]) are known. They are given by (3.1) and (3.2), respectively.
The following corollary unifies these results with our Theorem 3.32.
Corollary 3.37. Let N be a two-dimensional complete Riemannian manifold of constant
curvature κ ∈R, and let Ω⊂N be a polygon. Suppose that Ωhas M ∈N0 angles, which
are denoted by γ1,...,γM ∈(0,2π]. As usual, we denote the heat trace of Ωby ZΩ. Then
ZΩ(t)
t↓0∼Iκ + Bκ +
M
∑
i=1
Vκ(γi),
(3.111)
where
Iκ ∶= ∣Ω∣
4πt
∞
∑
ν=0
fν ⋅κν ⋅tν;
Bκ ∶= ∣∂Ω∣
8
√
πt
∞
∑
ν=0
rν ⋅κν ⋅tν;
Vκ(γi) ∶=
∞
∑
ν=0
eν(γi) ⋅κν ⋅tν;
and fν,rν and eν(γi) are the following universal coefficients for all ν ∈N0 ∶
fν ∶=
1
ν! ⋅4ν
ν
∑
ℓ=0
(ν
ℓ)(−4)ℓB2ℓ(1
2),
(3.112)
rν ∶= −1
4νν!,
(3.113)
eν(γi) ∶= 1
4ν
ν
∑
ℓ=0
(−4)ℓ
(ν −ℓ)!
ℓ+1
∑
j=1
(2ℓ+ 2
2j ) B2ℓ−2j+2 ( 1
2) ⋅B2j
4 ⋅(ℓ+ 1)!(2ℓ+ 1) ⋅π2j −γ2j
i
π ⋅γ2j−1
i
.
(3.114)
(Note that ∣∂Ω∣is defined analogously as in Definition 3.6 and eν(π) = 0 for all ν ∈N0.
Further, 00 is understood to be 1, which occurs if κ,ν = 0.)
Proof. We proceed in several steps. Let us start with some comments on the cases we
already know. If N = H2 we have κ = −1 and the asymptotic expansion (3.111) coincides
with the asymptotic expansion given in (3.107). Note that
fν = 4π
∣Ω∣(−1)ν ⋅iH
ν−1,
rν = 8√π
∣∂Ω∣(−1)ν ⋅bH
ν−1,
eν(γi) = (−1)ν
ν
∑
ℓ=0
1
(ν −ℓ)! (−1
4)
ν−ℓ
cH
ℓ(γi),
where the coefficients on the right-hand sides are defined as in Theorem 3.32 (compare
also with the formulas (3.77) and (3.87)).
If N = S2, then κ = 1 and (3.111) reduces to the asymptotic expansion computed in
[Wat05] (see (3.2) and our comment on the coefficients thereafter). And if M = R2, then
κ = 0 and one easily shows that (3.111) is equal to the first three terms of (3.1).
94


---

3 Spectral invariants for polygons
Next, we generalise these results one step further by scaling the standard metric on the
hyperbolic plane and the unit sphere. Let gH2 denote the standard metric on the hyperbolic
plane H2 and let c ∈(0,∞) be a constant. Consider the space (H2,cgH2). The curvature
of H2 with respect to the scaled metric is constant and equal to κ = −1
c. Obviously, a
domain Ω⊂H2 is a polygon with respect to gH2 and has eigenvalues 0 < λ1 < λ2 ≤λ3 ≤...
if and only if it is a polygon with respect to cgH2 with eigenvalues 0 < λ1
c < λ2
c ≤λ3
c ≤....
Hence,
Z(Ω,c gH2) (t) = Z(Ω,gH2) (t
c),
and the claim follows easily for polygons in the space (H2,cgH2). The same argument
can be applied to S2 as well.
Lastly, suppose that N is an arbitrary two-dimensional complete Riemannian manifold
of constant curvature κ ∈R. Since the metric can be scaled appropriately as above, we
assume without loss of generality that κ ∈{−1,0,1}. Then N is locally isometric to Mκ,
where
Mκ ∶=
⎧⎪⎪⎪⎪⎨⎪⎪⎪⎪⎩
(H2,gH2),
if κ = −1,
(R2,gR2),
if κ = 0,
(S2,gS2),
if κ = 1,
and where gR2 and gS2 denote the standard metric on R2 and S2, respectively. We construct
a certain finite open cover of Ω. Let us choose around any Q ∈Ωa relatively compact
geodesic disc BrQ(Q) with rQ ∈(0,i(Q)] as follows:
(i) If Q is a vertex, we let rQ ∶= 2R, where R > 0 is such that the discs of radius 2R
around all vertices are mutually disjoint and can be isometrically embedded into
Mκ, and such that B2R(Q) ∩Ωis a disjoint union of finitely many circle sectors at
Q with radius 2R.
(ii) If Q lies on an edge E, but is not a vertex, then choose rQ such that BrQ(Q)
contains no vertices, no points from ∂Ω/E, and such that it can also be embedded
isometrically into Mκ.
(iii) For any Q ∈Ωwe choose rQ such that BrQ(Q) is completely contained in Ωand
can be isometrically embedded into Mκ.
Consider the collection of all those discs. Obviously, when we replace any disc of this
collection by the geodesic disc with the same center and half of the radius, we obtain an
open cover of Ω. Let BR1(Q1),...,BRn(Qn) ⊂N be a finite subcover of it, where n ∈N is
fixed. By construction, any B2⋅Rℓ(Qℓ) with ℓ∈{1,...,n} can be isometrically embedded
into Mκ. Henceforth, we identify these discs with their images in Mκ through such
isometric embeddings.
Roughly speaking, the idea is now to decompose Ωinto small pieces using the finite
cover above. Then we apply Lemma 3.36 to N and each piece of Ω. By this process
95


---

3 Spectral invariants for polygons
the full asymptotic expansion of ZΩ(t) splits into several parts such that each part is
attached to one of the pieces of Ω. Then we translate everything to Mκ by the isometric
embeddings and apply Lemma 3.36 to Mκ.
We have three kinds of geodesic discs in our finite covering, which lead to the following
decomposition of Ω. Let η ∈N0 and {ℓ1,...,ℓη} ⊂{1,...,n} be such that {BR(Qℓi)}η
i=1 is the
collection of all discs in the finite cover induced by (i). By definition, Ω∩(∪η
i=1BR(Qℓi))
consists of a disjoint union of M circle sectors, each contained in exactly one angle of
the polygon. Let {WR(Pj)}M
j=1 be all those circle sectors, where Pj denotes the vertex
of Ωcorresponding to the angle γj. Similarly, let {BRmi(Qmi)}τ
i=1 with τ ∈N0 and
{m1,...,mτ} ⊂{1,...,n} be all those discs of the finite cover induced by (ii). For each
i ∈{1,...,τ} the set Ω∩BRmi(Qmi) is either a half-disc or a disjoint union of two half-discs.
Let {Bej}k1
j=1 be the collection of all the half-discs which are obtained that way. Finally,
let {Bij}k2
j=1 be all the discs in the finite cover coming from (iii). Then
Ω= V ⊍E ⊍I,
where
V ∶=
M
⊍
j=1
WR(Pj), E ∶=
k1
⊍
j=1
Bej/(V ∪(∪j−1
ℓ=1Beℓ)), I ∶=
k2
⊍
j=1
Bij/(V ∪E ∪(∪j−1
ℓ=1Biℓ)).
Let us show how to do the rest of the program. Let WR(Pj) be arbitrary with j ∈
{1,...,M}. Recall that the circle sector WR(Pj) has angle γj. As in Lemma 3.36, let
W2R(Pj) denote the circle sector at Pj with radius 2R and angle γj such that WR(Pj) ⊂
W2R(Pj). It follows from (3.109) that the function
t ↦∫WR(Pj) KΩ(x,x;t)dx
has the same asymptotic expansion as the function t ↦∫WR(Pj) KW2R(Pj)(x,x;t)dx as
t ↘0. Note that the domains WR(Pj) and W2R(Pj) are identified with their isometric
images in Mκ and the function KW2R(Pj) is identified with the heat kernel of that isometric
image W2R(Pj) ⊂Mκ. When we apply (3.110) to Mκ, we see that the function t ↦
∫WR(Pj) KW2R(Pj)(x,x;t)dx has the same asymptotic expansion as the function
t ↦∫WR(Pj) KWγj (Pj)(x,x;t)dx
as t ↘0, where Wγj(Pj) ⊂Mκ denotes the wedge at Pj with angle γj such that
WR(Pj) ⊂Wγj(Pj). Note that for κ = −1 the asymptotic expansion of that function
follows from Section 3.2. Similarly, if κ = 0 and κ = 1 its asymptotic expansion follows
from [vdBS88] and [Wat05], respectively. Hence we know the asymptotic expansion of
t ↦∫WR(Pj) KΩ(x,x;t)dx as t ↘0.
The same kind of argument can also be applied to the other pieces of the decomposition,
i.e. any of those disjoint subsets into which E and I are decomposed above. Note that for
96


---

3 Spectral invariants for polygons
the subsets of I one needs to apply the above argument with (3.108) instead of (3.109),
and (3.47) instead of (3.110). From that analysis the statement follows.
This corollary shows how the heat invariants for Euclidean, spherical and hyperbolic
polygons are linked to each other. Further, it follows from Corollary 3.37 that polygons
of constant zero curvature have at most three nonvanishing heat invariants. This was
previously well-known for Euclidean polygons ([vdBS88]).
Another observation of Corollary 3.37 is the following: Suppose a polygon of constant
curvature κ ∈R is given. Then an angle γ ∈(0,2π] of the polygon contributes the
terms Vκ(γ) = ∑∞
ν=0 eν(γ) ⋅κν ⋅tν to its heat trace asymptotic expansion. In other words,
the contributions are given as polynomials in the Gaussian curvature with universal
coefficients eν(γ) ∈R for all ν ∈N0. Another reason for this phenomenon will be provided
through orbifold theory in Section 4.3 for angles γ = π
k, k ∈Nk≥2.
We think that it is an interesting problem to investigate the contribution of an angle
of a geodesic polygon to the heat invariants if the Gaussian curvature is arbitrary. We
expect that in the general case the coefficients of an angle contribution resemble the case
of constant curvature. That is, we conjecture that they are always given as polynomials
in the Gaussian curvature and its covariant derivatives at the vertex.
In the remaining part of this section we draw some conclusions from the heat invariants
for polygons of constant curvature. Obviously, the heat trace only depends on the spectrum
of the Dirichlet Laplacian through (2.5). Thus, all heat invariants are determined by the
spectrum. We may ask: Which geometric properties of a polygon are determined by its
heat invariants and therefore also are spectral invariants? The next corollary provides a
first answer.
Recall that for any polygon Ωof constant curvature κ, the Gauß-Bonnet theorem
states:
M
∑
i=1
γi = ∣Ω∣⋅κ + M ⋅π −2πχ(Ω),
(3.115)
where M ∈N0 denotes the number of angles and γ1,...,γM are the angles of Ω(see [Cha06,
Theorem V.2.7]). Note that (3.115) holds even in the nonorientable case and for polygons
of constant curvature in the sense Definition 3.34. We will use this formula repeatedly in
the sequel.
Corollary 3.38. Let Ωbe a polygon of constant curvature. Then the volume ∣Ω∣, the
perimeter ∣∂Ω∣and the curvature of the polygon are spectral invariants of Ω.
Proof. The heat invariants given by the coefficients of 1
t and
1
√
t determine the volume and
the perimeter of the polygon, respectively. If ∣∂Ω∣≠0, then the curvature of the polygon
is determined (for example) by the heat invariant corresponding to
√
t. If ∣∂Ω∣= 0, then
Ωhas no boundary and vertices and thus the right-hand side of (3.111) reduces to Iκ.
Hence, the curvature can be gleaned from the heat invariant corresponding to t0.
Definition 3.39. If the boundary of a polygon is a disjoint union of piecewise geodesic
simple closed curves, then we call it a simple polygon.
97


---

3 Spectral invariants for polygons
Note that for simple polygons the number of angles, edges, and vertices is the same.
Theorem 3.40. Let Ωbe a polygon of nonzero constant curvature. Then the number of
angles which are not equal to π is a spectral invariant. Moreover, the multiset consisting
of all angles of Ωwhich are not equal to π is a spectral invariant as well. Furthermore,
the Euler characteristic χ(Ω) of the polygon is a spectral invariant.
In particular, if Ωis a simple polygon with nonzero constant curvature, then the number
of vertices and the multiset of all angles are spectral invariants.
Proof. Because the Gaussian curvature is not zero, there are infinitely many nonvanishing
heat invariants. Let κ ∈R/{0} denote the curvature of Ωand let γ1,...,γM be all angles
of Ωwhich are not equal to π, where M ∈N0. Then the coefficient corresponding to tν,
ν ∈N0, is given by
∣Ω∣
4π fν+1 ⋅κν+1 +
M
∑
i=1
eν(γi)κν.
Note that angles which are equal to π can be ignored since eν(π) = 0 for all ν ∈N0.
We know from Corollary 3.38 that the volume and the curvature of the polygon are
determined by the spectrum. Therefore, the spectrum also determines the value of the
sum ∑M
i=1 eν(γi) for all ν ∈N0. Note that for each ν ∈N0, the coefficient of the highest
power term
Wν ∶=
M
∑
i=1
π2ν+2 −γ2ν+2
i
πγ2ν+1
i
in ∑M
i=1 eν(γi) corresponds to ℓ= ν, j = ν + 1 in (3.114) and equals (−1)ν ⋅
B2ν
4(ν+1)!(2ν+1).
Since the Bernoulli numbers with even index never vanish, i.e. B2ν ≠0 for all ν ∈N0 (see
e.g. [Nör24, p. 23]), we conclude by induction that the spectrum determines the sequence
(Wν)ν∈N0.
Thus we also obtain the following spectral invariants:
Wν,1 ∶=
1
π2ν+1 (Wν+1 −Wν) =
M
∑
i=1
(( π
γi
)
2
−1)( 1
γi
)
2ν+1
for ν ∈N0.
We claim that the smallest angle can be deduced from the sequence (Wν,1)ν∈N0.
Since π2
γ2
i −1 ≠0 by assumption, we have limν→∞γ2ν+1 ⋅Wν,1 = 0 for all γ > 0 if and only
if M = 0. Thus the spectrum determines whether the polygon has vertices or not.
If M ≥1 then for γ = mini γi =∶θ1 the above limit is not zero. More precisely, observe
that there exists some n1 ∈N such that for all γ ∈(0,θ1] we have
lim
ν→∞γ2ν+1 ⋅Wν,1 =
⎧⎪⎪⎨⎪⎪⎩
0,
if γ < θ1,
(( π
θ1)
2 −1) ⋅n1,
if γ = θ1.
98


---

3 Spectral invariants for polygons
Thus we have
θ1 = inf {γ > 0∣γ2ν+1 ⋅Wν,1 is convergent as ν →∞with nonzero limit }.
So the magnitude of the smallest angle θ1 is a spectral invariant.
When we do the same argument as above with Wν,1 replaced by
Wν,2 ∶= Wν,1 −(( π
θ1
)
2
−1)( 1
θ1
)
2ν+1
we obtain the value of θ2 ∶= min({γ1,...,γM}/{θ1}). Repeating this argument in the above
manner, we successively obtain M values θ1 ≤θ2 ≤... ≤θM. This process will eventually
stop when Wν,M+1 = 0 for all ν ∈N0. Thus, we obtain the value of M as well as the
multiset of angles {γ1,...,γM} = {θ1,...,θM}.
By (3.115), the Euler characteristic χ(Ω) is now determined by the spectrum as well.
If Ωis a simple polygon, then there are no angles equal to π and the number of angles
is equal to the number of vertices. Thus the number of vertices of Ωas well as the multiset
of all angles of the polygon are spectral invariants.
Corollary 3.41. Let Ωbe a polygon of constant zero curvature. Then the spectrum, the
Euler characteristic and the number M of all angles of the polygon determines ∑M
i=1
1
γi,
where γ1,...,γM ∈(0,2π] denote the angles of the polygon.
Proof. The heat invariant corresponding to t0 is given by
∣Ω∣
4π f1 ⋅κ +
M
∑
i=1
e0(γi) =
1
24π (
M
∑
i=1
π2
γi
−
M
∑
i=1
γi).
By the Gauß-Bonnet theorem we have ∑M
i=1 γi = Mπ −2πχ(Ω). Hence the sum ∑M
i=1
1
γi is
determined by the spectrum together with M and χ(Ω).
Note that the above Corollary is well-known for simple Euclidean polygons (see e.g.
[GM13]).
As it is usual, we call two polygons isospectral if the spectrum of their Dirichlet
Laplacians are equal and all corresponding eigenvalues have the same multiplicities. By
Corollary 3.38 two polygons with different area, perimeter or curvature can never be
isospectral. Or, positively formulated, two isospectral polygons do always have the same
area, perimeter and curvature. But what else can be said about isospectral polygons?
On the one hand, it is well-known that there exist isospectral polygons which are not
isometric. Therefore it is not always possible to deduce the whole geometry of a polygon
from its spectrum. On the other hand there are also some positive results known for
simple Euclidean polygons. Let us review some of those results.
Obviously, if a polygon has zero curvature, then the heat invariants do not provide
much information about the geometry of the polygon. They do not tell us how many
vertices a simple polygon has, in contrast to the heat invariants for simple polygons with
99


---

3 Spectral invariants for polygons
nonzero curvature (see Theorem 3.40 above). However, within special classes of polygons
we can deduce nevertheless enough geometric information from the heat invariants to
distinguish polygons by their spectra. For example, it is known that the spectrum of
a Euclidean triangle determines the triangle in the following sense: If we know that Ω
is a Euclidean polygon with 3 angles, then the spectrum determines the polygon Ωup
to isometry. This was first proven by C. Durso in her Ph.D. thesis [Dur88] using heat
invariants and spectral invariants derived by other methods. Later on, a much shorter
proof was given by D. Grieser and S. Maronna in [GM13]. Grieser and Maronna in fact
prove that one can deduce from the heat invariants the values of all three angles of a
triangle.
Similar results are given in the recent article [LR15]. Z. Lu and J. Rowlett prove
that one can deduce the values of the angles of a (Euclidean) parallelogram from its
heat invariants and thus they obtain the following result: If we know a priori that Ωis
a parallelogram, then the spectrum determines Ωup to isometry. They also prove in
[LR15] that the regular n-gon uniquely maximises the isoperimetric ratio
∣Ω∣
∣∂Ω∣2 among
all n-gons and thus they conclude: If an n-gon is isospectral to a regular n-gon, then
they are isometric. There are a couple more of interesting results in [LR15], but those
are established using not only the heat invariants but other methods as well.
The following two corollaries add some simple and new observations.
Remark. If Ω⊂N is a simply connected polygon with constant curvature κ = 0, then Ωis
isometric to a Euclidean polygon in R2. In fact, Ωis isometric to each component of its
preimage under the universal covering R2 →N. In particular, M ≥3 and ∑M
i=1 γi = (M−2)π
by elementary geometry, where γ1,...,γM denote all angles of Ω.
Corollary 3.42. Let Ωbe a simply connected Euclidean polygon. Let M ≥3 denote the
number of all angles. Then:
(i) The spectrum together with M determines whether Ωis equiangular or not.
(ii) Let c0 ∶= ∑M
i=1
π2−γ2
i
24πγi be the heat invariant corresponding to the power t0. Then c0 > 1
6.
Furthermore, M ≥1 +
6⋅c0
6c0−1, which gives a nontrivial bound if c0 ∈( 1
6, 1
3).
Proof. (i). Since Ωis simply connected, we have χ(Ω) = 1. Thus, from Corollary 3.41 the
spectrum together with M determines ∑M
i=1
1
γi. Applying the arithmetic-harmonic mean
inequality, we have
M
∑M
i=1
1
γi
≤∑M
i=1 γi
M
= (M −2)π
M
,
with equality if and only if γ1 = γ2 = ... = γM. Thus all angles of the polygon Ωare equal
if and only if
M2
(M−2)π = ∑M
i=1
1
γi.
(ii). Again by ∑M
i=1 γi = (M −2)π and the arithmetic-harmonic mean inequality we
have
c0 = π
24 (
M
∑
i=1
1
γi
) −M −2
24
100


---

3 Spectral invariants for polygons
≥1
24 ⋅
M 2
(M −2) −M −2
24
.
This is equivalent to
12c0 −1 ≤M (6c0 −1).
If c0 < 1
6, then it follows that M ≤1 +
6c0
6c0−1 < 2. This is impossible by M ≥3. Similarly, if
c0 = 1
6, then we obtain 1 ≤0 which is a contradiction. Thus it follows that c0 > 1
6.
By c0 > 1
6, we now obtain M ≥1 +
6c0
6c0−1, which completes the proof of (ii). This lower
bound is useless for c0 > 1
3, since the function f(x) ∶= 1 +
6x
6x−1 is strictly decreasing in
( 1
6,∞) and f( 1
3) = 3.
Corollary 3.43.
(i) A simply connected Euclidean polygon can never be isospectral to a two-dimensional
compact manifold with nonempty smooth boundary.
(ii) A polygon with zero curvature can not be isospectral to a smooth domain in the
Euclidean plane.
Proof. (i). Note that for a compact two-dimensional manifold D with nonempty smooth
boundary the heat invariant corresponding to the power t0 is given by 1
6χ(D), where
χ(D) is the Euler characteristic of D. We have 1
6χ(D) ≤1
6(2−b) ≤1
6, where b ∈N denotes
the number of boundary components of D. Using Corollary 3.42 (ii), the statement
follows.
(ii). Note that for a smooth domain in the Euclidean plane the heat invariant corre-
sponding to the power t
1
2 is always positive (see the coefficient c3 in [Smi81]). But the
corresponding heat invariant for a polygon with zero curvature is always 0.
Remark. Statement (i) of the above corollary was proven independently in the recent
article [LR16]. In our case, Corollary 3.43 appeared as a by-product from our desire
to estimate the number of angles of a simply connected Euclidean polygon (Corollary
3.42 (ii)). Z. Lu and J. Rowlett instead investigate in [LR16] simply connected planar
domains with piecewise smooth Lipschitz boundary.
We have seen that, if a Euclidean polygon is simply connected, Corollary 3.42 (ii)
in some cases gives a lower bound for the number of angles. In general, however, the
heat invariants do not suffice to detect the exact number of angles. We conjecture that
Theorem 3.40 also holds for polygons of constant zero curvature. That is, we conjecture
in particular that the number of vertices as well as the multiset of all angles of a simple
polygon with zero curvature is always determined by its spectrum. But we do not know
how to prove this conjecture. As we mentioned above, there are lots of known pairs of
isospectral and nonisometric simple Euclidean polygons (see e.g. [GWW92], [BCDS94],
[Cha95]). All of these isospectral pairs indeed have the same number of vertices and the
same multiset of angles.
101


---

3 Spectral invariants for polygons
Let us also include polygons with nonzero curvature into our considerations. Theorem
3.40 shows that pairs of isospectral simple hyperbolic polygons as well as pairs of simple
spherical polygons must have the same number of vertices and multiset of angles. However,
as for Euclidean polygons, it is known that the spectrum does not always determine all of
the geometry. There exist pairs of hyperbolic and spherical polygons which are isospectral
and nonisometric (see [GW94] for such pairs of isospectral polygons). Nevertheless, we
can deduce some information about the geometry from the spectrum.
Corollary 3.44. Let Ωbe a polygon with at least one angle not equal to π and of constant
curvature κ ∈R. Let c0 denote the heat invariant for Ωcorresponding to t0. Further, let
D be a two-dimensional Riemannian manifold with smooth boundary. Then:
(i) c0 > 1
6χ(Ω).
(ii) If Ωis isospectral to D, then χ(Ω) < χ(D).
Proof. Let γ1,...,γM ∈(0,2π] denote all angles of Ω, where M ∈N. From Corollary 3.37,
we know that the heat invariant for Ωcorresponding to t0 is
c0 ∶= ∣Ω∣
4π f1κ +
M
∑
i=1
e0(γi).
The Bernoulli polynomial B2(x) is given by B2(x) = x2 −x + 1
6 (see [OLBC10, 24.2(iv)
Tables]) and thus B2 = 1
6 and B2( 1
2) = −1
12. Hence, f1 = 1
3 and
c0 = ∣Ω∣
12πκ + π
24 (
M
∑
i=1
1
γi
) −
1
24π
M
∑
i=1
γi.
By (3.115) and the arithmetic-geometric mean inequality we have
c0 = 1
6χ(Ω) + 1
24
M
∑
i=1
( π
γi
+ γi
π ) −M
12
≥1
6χ(Ω),
with equality if and only if γi = π for all i = 1,...,M. This proves both statements of the
corollary. For (ii) note that, because D is a smooth domain, the heat invariant for D
corresponding to t0 is just 1
6χ(D).
Corollary 3.44 shows, in particular, that if a polygon with at least one vertex is isospectral
to a smoothly bounded compact domain, then they can never be homeomorphic. It is
suprising that, to the best of our knowledge, this result was never published for domains
in the Euclidean plane.
Hyperbolic and spherical triangles are determined up to isometry by their spectrum
within the class of all polygons.
Corollary 3.45. Let Ωbe any polygon of constant curvature. Then:
102


---

3 Spectral invariants for polygons
(i) If Ωis isospectral to a hyperbolic triangle TH, then Ωand TH are isometric.
(ii) If Ωis isospectral to a spherical triangle TS, then Ωand TS are isometric.
Proof. Both statements follow immediately from Corollary 3.38 and Theorem 3.40. Just
note that hyperbolic and spherical triangles are uniquely determined by their angles.
Note that in Corollary 3.45 we do not need to assume a priori that Ωis a triangle,
unlike in the analogous result in [GM13] for the Euclidean plane.
Corollary 3.46. Let Ωbe any hyperbolic or spherical polygon.
(i) The spectrum determines whether Ωis convex or not.
(ii) If Ωis isospectral to a regular hyperbolic polygon RH, then Ωand RH are isometric.
(iii) If Ωis isospectral to a regular spherical polygon RS, then Ωand RS are isometric.
Proof. (i). As in the Euclidean plane, a polygon is convex if and only if the values of all
its angles are contained in (0,π). Thus the claim follows from Theorem 3.40.
(ii) and (iii). It follows from [Por12] that there is a unique polygon which minimises
the perimeter among all equiangular polygons, namely the polygon with an inscribed
circle. Since regular polygons do have an inscribed circle, they minimise the perimeter
within the class of all equiangular polygons of fixed angle.
3.4 Method of images and finite trigonometric sums
As in Section 3.2, let Ωbe a hyperbolic polygon with angles γ1,...,γM, where M ≥3 is
an integer. In addition we assume that for all i ∈{1,...,M } there exists some integer
k(i) ≥2 such that γi =
π
k(i). Let Wγi be the wedge corresponding to γi and let Pi denote
the vertex of Wγi for all i = 1,...,M.
In the following we will compute the asymptotic expansion of the heat trace ZΩ(t)
as t ↘0. Of course, this problem is only a special case of Theorem 3.32 such that we
already know the answer. However, as we will show, one can approach the problem with
much more elementary means in the present situation. The reason is that the heat kernel
for a wedge with angle π
k, k ∈N≥2, has a more elementary expression than in Corollary
3.11, which is easily deduced from Sommerfeld’s method of images. We will use this
elementary formula as a substitute for Corollary 3.11 and compute the heat invariants
again by Kac’s principle of not feeling the boundary. The contributions from the vertices
of the polygon will then appear as finite trigonometric sums. By comparison with the
formulas of Section 3.2 we obtain explicit evaluations for those trigonometric sums.
We begin with the construction for the heat kernel using Sommerfeld’s method of
images. Let W ⊂H2 be a hyperbolic wedge with vertex P and interior angle γ = π
k, where
k ≥2 is an integer. Let us choose 2k different rays s1,...,s2k originating at P such that
any two adjacent rays sj,sj+1 (counting indices mod 2k) form a hyperbolic wedge of
103


---

3 Spectral invariants for polygons
W
P
s1
s2
s3
s4
s5
s6
γ
Figure 3.4: Rays for k = 3
angle γ and s1, s2 enclose the wedge W we started with. Thus we get a decomposition of
H2 into 2k congruent wedges (see Fig. 3.4).
Next, for any given point y ∈W we construct image points by means of successive
reflections in those rays. More precisely, for any fixed point y1 ∶= y ∈W we first reflect this
point in the ray s2 and denote the image point by y2. Secondly, we reflect y2 in the ray
s3 and get another point y3, etc. By this process we obtain 2k different points y1,...,y2k
each of which lies in exactly one of the wedges described above (see Fig. 3.5). Note that
if we reflect the point y2k in the ray s1 the image point coincides with the initial point y1.
W
P
s1
s2
s3
s4
s5
s6
+
−
+
−
+
−
y1
y2
y3
y4
y5
y6
γ
Figure 3.5: Mirror images for k = 3
When we introduce polar coordinates (ρ,θ) with base point P, where ρ ∈(0,∞) is the
radius and θ ∈[0,2π) is the angle measured with respect to s1, then we can parametrise the
wedge as W = {(ρ,θ) ∣0 < ρ < ∞, 0 < θ < γ }. Further, for any initial point y = (ρ,θ) ∈W,
the coordinates of the image points yj, j = 2,3,..,2k, are given by yj = (ρ,θj) with
θj ∶=
⎧⎪⎪⎨⎪⎪⎩
(j −1) ⋅γ + θ,
if j is odd
j ⋅γ −θ,
if j is even.
The heat kernel Kγ for the wedge W can now be written as in the following lemma.
104


---

3 Spectral invariants for polygons
Lemma 3.47.
Kγ(x,y;t) =
2k
∑
j=1
(−1)j+1 KH2(x,yj;t) for all x,y ∈W and t > 0,
where KH2 denotes, as usual, the heat kernel of the hyperbolic plane.
Proof. Let Ij be the isometry of H2 which corresponds to yj, i.e. I1 ∶H2 →H2 denotes
the identity map, and, for all j = 2,3,...,2k the isometry Ij ∶H2 →H2 is represented in
the above polar coordinates by
Ij(ρ,θ) ∶=
⎧⎪⎪⎨⎪⎪⎩
(ρ,(j −1) ⋅γ + θ),
if j is odd
(ρ,j ⋅γ −θ),
if j is even.
We define ˜KW ∶H2 ×H2 ×(0,∞) ∋(x,y,t) ↦˜KW(x,y;t) ∶= ∑2k
j=1 (−1)j+1 KH2(x,Ijy;t) ∈R.
Note that Ijy = yj for all y ∈W and j = 1,2,...,2k.
First, we prove that for any y ∈W the function W × (0,∞) ∋(x,t) ↦˜KW(x,y;t) ∈R
is a fundamental solution to the heat equation at y (recall Definition 2.1): Obviously,
if y ∈W is given, then (∂t + ∆) ˜KW(⋅,y;⋅) ≡0 on W × (0,∞), because each function
KH2(⋅,yj;⋅) is a solution to the heat equation. Moreover, let f ∈C∞
c (W) be arbitrary.
We extend that function by f(x) ∶= 0 for all x ∈H2/W (and we denote that extended
function again by f) such that f also belongs to C∞
c (H2). Now, for all y ∈W
∫
W
˜KW(x,y;t)f(x)dx =
2k
∑
j=1
(−1)j+1 ∫
H2
KH2(x,yj;t)f(x)dx.
By definition of KH2, we have limt↘0 ∫H2 KH2(x,yj;t)f(x)dx = f(yj). Finally, because
f(yj) = 0 for all j = 2,3,...,2k we obtain limt↘0 ∫W ˜KW(x,y;t)f(x)dx = f(y).
Second, we will prove that ˜KW is non-negative on W × W × (0,∞), i.e. ˜K(x,y;t) ≥0
for all x,y ∈W and t > 0. Let ϕ ∈C∞
c (W) with ϕ ≥0 be arbitrary and extend, as before,
that function by ϕ(y) ∶= 0 for all y ∈H2/W. Consider the function u ∶H2 × [0,∞) →R,
defined as
u(x,t) ∶=
⎧⎪⎪⎨⎪⎪⎩
∫H2 ˜KW(x,y;t) ⋅ϕ(y)dy
for all x ∈H2 and t > 0,
ϕ(x)
for all x ∈H2 and t = 0.
Note that for all x ∈H2 and t > 0:
u(x,t) =
2k
∑
j=1
(−1)j+1 ∫
H2
KH2(x,y;t)ϕ(I−1
j y)dy,
where I−1
j
denotes the inverse to Ij. Hence, u∣H2×(0,∞) is a smooth solution to the heat
equation, which follows from the definition of KH2 (see [Gri09, formula (7.49)]) and [Gri09,
Theorem 7.10]. Moreover, u is continuous (see [Gri09, Remark 7.17]).
105


---

3 Spectral invariants for polygons
We want to apply the parabolic minimum principle to show that u∣W×(0,∞) is non-
negative. For that purpose, note that ˜KW(x,y;t) = 0 for all x ∈∂W, y ∈W and t ∈(0,∞).
That follows from the definition of yj and because KH2(x,y;t) = KH2(˜x, ˜y;t) for all
x,y, ˜x, ˜y ∈H2 with d(x,y) = d(˜x, ˜y). Thus, we also have u(x,t) = 0 for all x ∈∂W and
t > 0. Moreover, u(x,0) = ϕ(x) ≥0 for all x ∈W. Further, for any compact set K ⊂H2,
T > 0, and any sequence (xn)n∈N ⊂H2 with limn→∞d(xn,P) = ∞, we have by the estimate
(3.28):
lim
n→∞
sup
(y,t)∈K×(0,T]
∣KH2(xn,y;t)∣= 0,
(3.116)
and consequently
lim
n→∞sup
t∈(0,T]
∣u(xn,t)∣= 0.
Now, using the parabolic minimum principle (see [Gri09, Theorem 8.10]) we conclude
u(x,t) ≥0 for all x ∈W and t > 0. More precisely, suppose that there exists some point
(x∗,t∗) ∈W × (0,T), for some T > 0 such that u(x∗,t∗) < 0. Choose some R > 0 such that
u(x∗,t∗) < u(x,t) for all t ∈(0,T] and x ∈W with d(x,P) ≥R. But then, the minimum
of u on the set W ∩BR(P) × [0,T] is not attained on its parabolic boundary, which is a
contradiction to the parabolic minimum principle. Finally, because ˜KW is continuous
and ϕ ∶W →R was an arbitrary non-negative and compactly supported smooth function,
we have for any x ∈W: ˜KW(x,y;t) ≥0 for all y ∈W and t > 0. Using the symmetry
˜KW(x,y;t) = ˜KW(y,x;t) we indeed have ˜KW(x,y;t) ≥0 for all x,y ∈W and t > 0.
The statement now follows from [Gri09, Theorem 9.7] and the estimates (3.116),
(3.28).
We decompose the polygon Ωinto the same subsets as in Section 3.2. Note that Ω
is a simple hyperbolic polygon because of the assumptions on its angles and thus Ω
has as many edges as angles (i.e.
˜
M = M). Further, we can assume without loss of
generality that the edge Ei is equal to the geodesic segment between the vertices Pi and
Pi+1 for all i = 1,...,M with PM+1 ∶= P1. Recall that due to the principle of not feeling
the boundary (see Corollary 3.20 and (3.67)), Z
1/4
Ω(t) has the same asymptotic expansion
as the following sum of functions:
∫
ΩI
K
1/4
H2(x,x;t)dx +
M
∑
i=1 ∫
ΩEi
K
1/4
Ei (x,x;t)dx +
M
∑
i=1
∫
WR(Pi)
K
1/4
γi (x,x;t)dx,
(3.117)
where we use the same notation as in Section 3.2; in particular,
KEi(x,x;t) = KH2(x,x;t) −KH2(x,xEi;t).
Let us insert the above formulas for Kγi and KEi into (3.117). Since we are now
confronted with several wedges at the same time, the notation for the image points yj
in the definition of Kγ can become ambiguous sometimes. In such a case we will write
106


---

3 Spectral invariants for polygons
yj(γi) instead of yj to indicate from which wedge the point yj originates from, i.e. we
denote the heat kernel of Wγi as Kγi(x,y;t) = ∑
2k(i)
j=1 (−1)j+1KH2(x,yj(γi);t). The sum
(3.117) is then equal to
∫
Ω
K
1/4
H2(x,x;t)dx −
M
∑
i=1
( ∫
ΩEi
K
1/4
H2(x,xEi;t)dx +
k(i)
∑
j=1
∫
WR(Pi)
K
1/4
H2 (x,x2j(γi);t)dx)+
+
M
∑
i=1
k(i)−1
∑
j=1
∫
WR(Pi)
K
1/4
H2 (x,x2j+1(γi);t)dx.
Thus we need to compute the asymptotic expansion of the following functions:
Z
1/4
I (t) = ∫
Ω
K
1/4
H2(x,x;t)dx,
˜Z
1/4
E (t) ∶= −
M
∑
i=1
( ∫
ΩEi
K
1/4
H2(x,xEi;t)dx +
k(i)
∑
j=1
∫
WR(Pi)
K
1/4
H2 (x,x2j(γi);t)dx),
˜Z
1/4
V (t) ∶=
M
∑
i=1
k(i)−1
∑
j=1
∫
WR(Pi)
K
1/4
H2 (x,x2j+1(γi);t)dx.
Remark. In Section 3.2 we also worked with three similar functions denoted there by
Z
1/4
I ,Z
1/4
E and Z
1/4
V . The definition for Z
1/4
I , given in (3.71), was exactly the same as above
and, as we will see in Corollary 3.48, ˜Z
1/4
E = Z
1/4
E . But, strictly speaking, the functions
˜Z
1/4
V
and Z
1/4
V
are not equal to each other, even though they have the same asymptotic
expansion as t ↘0.
The asymptotic expansion of Z
1/4
I (t) was already computed in Corollary 3.24 (i).
Corollary 3.48. We have ˜Z
1/4
E = Z
1/4
E , where Z
1/4
E is defined as in (3.80). In particular,
by Corollary 3.27 (i) ∶
Z
1/4
E (t)
t↓0∼−∣∂Ω∣
8
√
πt
⋅
∞
∑
k=0
δ0k ⋅tk.
(3.118)
Proof. For any t > 0, the function K
1/4
H2 (x,y;t) depends only on the distance d(x,y)
between x and y. In other words, K
1/4
H2 (x,y;t) = K
1/4
H2 (φ(x),φ(y);t) for any isometry
φ ∶H2 →H2. In particular, the heat kernel is symmetric in x,y. Fix some i ∈{1,...,M}
and let Sj ∶H2 →H2 denote the reflection in the line determined by the ray sj, where
the rays s1,...,s2k(i) are defined as above (compare Fig. 3.5) now with respect to the
wedge Wγi. (In particular s1 contains Ei.) Let Dα, α ∈R, denote the rotation around Pi
by angle α in the positive direction. Then Sj+1 = D2j
γi ○S1 and Sj+1 = Dj
γi ○S1 ○D−j
γi . In
107


---

3 Spectral invariants for polygons
particular, Sj+1x = x2j = D2j
γi S1x; also, note that S1(WR(Pi)) = D−1
γi (WR(Pi)). Therefore
∫
WR(Pi)
K
1/4
H2 (x,x2j;t)dx =
∫
Sj+1(WR(Pi))
K
1/4
H2 (x,Sj+1x;t)dx
=
∫
Sj+1(WR(Pi))
K
1/4
H2 (D−j
γi x,S1D−j
γi x;t)dx
=
∫
D−j
γi Sj+1(WR(Pi))
K
1/4
H2 (x,S1x;t)
=
∫
Dj−1
γi (WR(Pi))
K
1/4
H2 (x,S1x;t).
The union of Dj−1
γi (WR(Pi)) over j = 1,...,k(i) is equal to a half-disc and can be
parametrised in polar coordinates as
k(i)
⋃
j=1
Dj−1
γi (WR(Pi)) = {(a,α) ∣0 < a < R, 0 < α < π }.
Hence,
k(i)
∑
j=1
∫
WR(Pi)
K
1/4
H2 (x,x2j(γi);t)dx =
∫
⋃
k(i)
j=1 Dj−1
γi (WR(Pi))
K
1/4
H2 (x,xEi(γi);t)dx
= 2
R
∫
0
π
2
∫
0
K
1/4
H2 ((a,α),(a,−α);t)sinh(a)dαda,
and
˜Z
1/4
E (t) = −
M
∑
i=1
⎧⎪⎪⎨⎪⎪⎩
∫
ΩEi
K
1/4
H2(x,xEi;t)dx + 2
R
∫
0
π
2
∫
0
K
1/4
H2 ((a,α),(a,−α);t)sinh(a)dαda
⎫⎪⎪⎬⎪⎪⎭
.
Therefore, the function ˜Z
1/4
E is exactly the same function as Z
1/4
E from (3.80) of Section
3.2. Thus the asymptotic expansion of Z
1/4
E (t) as t ↘0 is given by Corollary 3.27 (i).
It remains to determine the asymptotic expansion of ˜Z
1/4
V (t). For all i ∈{1,...,M} we
define
˜I
1/4
γi (t) ∶=
k(i)−1
∑
j=1
∫
WR(Pi)
K
1/4
H2(x,x2j+1(γi);t)dx,
(3.119)
108


---

3 Spectral invariants for polygons
such that
˜Z
1/4
V (t) =
M
∑
i=1
˜I
1/4
γi (t).
(3.120)
The discussion so far shows that ˜I
1/4
γi (t) will provide the contributions from the angle γi
to the heat invariants for the polygon Ω. So let i ∈{1,...,M} be fixed in the following
discussion. In order to determine the asymptotic expansion of ˜I
1/4
γi (t) we define, for each
j ∈{1,...,k(i) −1}, the functions
Iij(t) ∶=
∫
WR(Pi)
K
1/4
H2(x,x2j+1(γi);t)dx.
(3.121)
Then
˜I
1/4
γi (t) =
k(i)−1
∑
j=1
Iij(t).
(3.122)
Let us fix also the parameter j ∈{1,...,k(i) −1} and first compute the asymptotic
expansion of Iij(t) as t ↘0.
When we choose polar coordinates (a,α) with base point Pi, the domain of integration
in (3.121) can be parametrised as
WR(Pi) = {(a,α) ∣0 ≤a ≤R, 0 ≤α ≤
π
k(i)}.
(3.123)
Recall that the volume form in polar coordinates is given by dx = sinh(a)dadα (see
Section 3.1) and the distance of any two points (a,α), (a,α′) ∈H2 with the same radius
a ∈(0,∞) and angles α, α′ ∈(0,2π] is (recall (3.13)):
cosh(d((a,α),(a,α′))) = cosh2(a) −sinh2(a)cos(α′ −α)
= cosh2(a) ⋅(1 −cos(α′ −α)) + cos(α′ −α).
Hence, by (3.9) and the fact that the angles of x and x2j+1(γi) differ by 2jγi for each
x ∈WR(Pi), we get the following formula for Iij(t) in polar coordinates:
Iij(t) =
∫
WR(Pi)
K
1/4
H2(x,x2j+1(γi);t)dx
=
1
4√πt
3
2
1
k(i)
R
∫
0
∞
∫
arcosh(cosh2(a)(1−cos(2j
π
k(i) ))+cos(2j
π
k(i) ))
...
... 1
√
2
sinh(a) ⋅ρ ⋅e−ρ2
4t
√
cosh(ρ) −cosh2(a)(1 −cos(2j
π
k(i))) −cos(2j
π
k(i))
dρda.
(3.124)
109


---

3 Spectral invariants for polygons
Before we investigate Iij(t) further, let us discuss the following coefficients which will
appear in the asymptotic expansion of Iij(t). For all k, η ∈N0 we define the coefficient
dk(η) via the generating function:
sinhk (r) =
∞
∑
η=0
dk (η) ⋅rη for all r ∈R.
(3.125)
Note that by definition d0(0) = 1, d0(η) = 0 for all η ≥1 and dk(0) = 0 for all k ≥1. For
k ≥1, η ≥1 we can compute the coefficients dk(η) by the formulas
dk(η) =
∑
ℓ1,...,ℓk∈N
are odd, s.t.
∑k
τ=1 ℓτ=η
k
∏
j=1
1
ℓj!
(3.126)
=
1
2k ⋅η!
k
∑
p=0
(k
p)(−1)p (k −2p)η .
(3.127)
The first equality (3.126) is clear by sinh(r) = r + r3
3! + r5
5! + ..., and formula (3.127) is
true since
sinhk(r) = (er −e−r
2
)
k
= 1
2k
k
∑
p=0
(k
p)(−1)pe(k−2p)r
= 1
2k
k
∑
p=0
(k
p)(−1)p
∞
∑
η=0
(k −2p)
η!
η
rη
=
∞
∑
η=0
1
2k ⋅η!
k
∑
p=0
(k
p)(−1)p (k −2p)η rη.
(3.128)
(Compare (3.125) with (3.128).)
Moreover,
dk(η) = 0 for all k > η
(3.129)
because r ↦sinhk(r) has a zero of order k in 0.
Let us determine the asymptotic expansion of the integral expression in (3.124).
Lemma 3.49. Let
ψij(a) ∶= arcosh(cosh2(a)(1 −cos(2j π
k(i))) + cos(2j π
k(i)))
and
qij(ρ,a) ∶= 1
√
2
sinh(a) ⋅ρ
√
cosh(ρ) −cosh2(a)(1 −cos(2j
π
k(i))) −cos(2j
π
k(i))
110


---

3 Spectral invariants for polygons
for all a ≥0 and all ρ ∈(ψij(a),∞).
Then
R
∫
0
∞
∫
ψij(a)
qij(ρ,a) ⋅e−ρ2
4t dρda
t↓0∼
∞
∑
η=0
̃νη(i,j) ⋅tη+ 3
2,
(3.130)
where
̃νη(i,j) ∶= Γ(η + 3
2)
2η + 1
⋅
η
∑
ℓ=0
cℓ(i,j) ⋅d2ℓ(2η) =
√π(2η)!
2 ⋅4ηη! ⋅
η
∑
ℓ=0
cℓ(i,j) ⋅d2ℓ(2η),
(3.131)
cℓ(i,j) ∶=
ℓ
∑
τ=0
(
1
2
τ)(−1)ℓ−τ ⋅
1
sin(j ⋅
π
k(i))
2(ℓ−τ)+2,
(3.132)
and d2ℓ(2η) are the coefficients defined in (3.125).
Proof. The function ψij is continuous and strictly increasing on the interval [0,∞) as a
composition of continuous and strictly increasing functions, and thus its inverse
ψ−1
ij ∶[0,∞) ∋ω ↦arcosh
⎛
⎜⎜
⎝
¿
Á
Á
Á
Á
À
cosh(ω) −cos(2j
π
k(i))
1 −cos(2j
π
k(i))
⎞
⎟⎟
⎠
∈R
is continuous and strictly increasing as well. Both functions ψij, ψ−1
ij are smooth on
the domain (0,∞), since they are compositions of smooth functions. Hence, by the
Fubini-Tonelli theorem and substituting ρ by 2√ρ, we get
R
∫
0
∞
∫
ψij(a)
qij(ρ,a) ⋅e−ρ2
4t dρda =
∞
∫
0
min{R, ψ−1
ij (ρ)}
∫
0
qij(ρ,a)da ⋅e−ρ2
4t dρ
=
∞
∫
0
min{R, ψ−1
ij (2√ρ)}
∫
0
qij(2√ρ,a)
√ρ
da ⋅e−ρ
t dρ.
We would like to apply Watson’s lemma; recall Lemma 3.22. So we need to determine
the asymptotic expansion of the function
Q ∶(0,∞) ∋ρ ↦
min{R, ψ−1
ij (2√ρ)}
∫
0
qij(2√ρ,a)
√ρ
da ∈R
as ρ ↘0. Since ψ−1
ij is continuous in 0 with lim
ρ↘0 ψ−1
ij (2√ρ) = 0, for sufficiently small values
111


---

3 Spectral invariants for polygons
ρ > 0, we have
Q(ρ) =
ψ−1
ij (2√ρ)
∫
0
qij(2√ρ,a)
√ρ
da =
arcosh
¿
Á
Á
Á
À
cosh(2√ρ)−cos(2j
π
k(i) )
1−cos(2j
π
k(i) )
∫
0
...
...
√
2 ⋅sinh(a)
√
cosh(2√ρ) −cosh2(a) ⋅(1 −cos(2j
π
k(i))) −cos(2j
π
k(i))
da
=
√
2
¿
Á
Á
Á
À
cosh(2√ρ)−cos(2j
π
k(i) )
1−cos(2j
π
k(i) )
∫
1
1
√
cosh(2√ρ) −cos(2j
π
k(i)) −(1 −cos(2j
π
k(i)))a2
da.
This integral is of the form
√x
y
∫
1
1
√
x −ya2da
with x > y > 0. By an elementary substitution we get
√x
y
∫
1
1
√
x −ya2da = 1
√y arccos(
√y
x).
Therefore,
Q(ρ) =
√
2
√
1 −cos(2j
π
k(i))
⋅arccos
¿
Á
Á
Á
À
1 −cos(2j
π
k(i))
cosh(2√ρ) −cos(2j
π
k(i))
=
1
sin (j ⋅
π
k(i))
⋅arccos
sin (j
π
k(i))
√
cosh2(√ρ) −1 + sin2 (j ⋅
π
k(i))
.
(3.133)
This function can be expanded into an asymptotic power series, but we will postpone the
proof to the next lemma. Applying Lemma 3.50 with c ∶= sin(j ⋅
π
k(i)) ∈(0,1), we obtain
Q(ρ)
ρ↓0∼
∞
∑
η=0
ξ2η+1(i,j) ⋅ρ(η+ 3
2 )−1,
112


---

3 Spectral invariants for polygons
where
ξ2η+1 (i,j) ∶=
1
2η + 1 ⋅
η
∑
k=0
ck(i,j) ⋅d2k(2η).
Using Watson’s lemma we get
∞
∫
0
Q(ρ) ⋅e−ρ
t dρ
t↓0∼
∞
∑
η=0
ξ2η+1(i,j) ⋅Γ(η + 3
2)
´¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¶
= ̃νη(i,j)
⋅tη+ 3
2.
Finally, recall from (3.75) that Γ(η + 3
2) =
√π⋅(2η+2)!
4η+1(η+1)! for all η ∈N0.
We will give in the following lemma the details for the asymptotic expansion of (3.133).
Lemma 3.50. Let c ∈(0,1] and consider the function
U ∶[0,∞) ∋r ↦1
c ⋅arccos
c
√
cosh2(√r) −1 + c2 ∈R.
Then
U(r)
r↓0∼
∞
∑
η=0
ξ2η+1 ⋅rη+ 1
2,
(3.134)
where
ξ2η+1 ∶=
1
2η + 1 ⋅
η
∑
k=0
ck ⋅d2k(2η)
(3.135)
with ck ∶=
k
∑
τ=0
(
1
2
τ)(−1)k−τ ⋅
1
c2(k−τ)+2.
(3.136)
Proof. Let us consider u(r) ∶= U(r2). Observe that the function u(r) can be extended
continuously by the same formula to all of R, and this continuation is smooth on the domain
R/{0}, but is not continuously differentiable at the point 0. But since we are interested
only in the asymptotic expansion for r ↘0, we can choose a different continuation to
obtain a smooth function on R. Consider ˜u ∶R →R defined by
˜u(r) ∶=
⎧⎪⎪⎨⎪⎪⎩
u(r)
, if r ∈[0,∞),
−u(−r)
, if r ∈(−∞,0).
(3.137)
Then ˜u is a smooth odd function on R. This follows for instance from the following facts:
u is smooth on the domain (0,∞), satisfies u(0) = 0, and the limit of
dm
drmu(r) as r ↘0
exists in R for all m ∈N and is equal to 0 if m is an even number. The last assertion can
be easily seen from (3.138) below. Hence ˜u has a Taylor series around 0 which formally
113


---

3 Spectral invariants for polygons
equals the asymptotic series for u(r) as r ↘0; i.e., there exist constants ̃ξk ∶= 1
k!
dk˜u
dxk (0)
such that
u(r)
r↓0∼
∞
∑
k=0
̃ξk ⋅rk.
It remains to show that ̃ξ2η = 0 and ̃ξ2η+1 = ξ2η+1 for all η ∈N0. Obviously ̃ξ0 = ˜u(0) = 0.
To compute the other coefficients, we first differentiate u(r) for r > 0 and get
du
dr (r) = 1
c
−1
√
1 −
c2
cosh2(r)−1+c2
⋅(−1
2) ⋅c ⋅2 ⋅cosh(r) ⋅sinh(r)
(cosh2(r) −1 + c2)
3
2
=
1
cosh2(r) −1 + c2 ⋅cosh(r)sinh(r)
√
cosh2(r) −1
=
cosh(r)
cosh2(r) −1 + c2.
(3.138)
Thus d˜u
dr (r) =
cosh(r)
cosh2(r)−1+c2 for all r ∈R, since d˜u
dr is an even function. The Taylor series for
this function can be derived as follows: For r ∈R such that ∣sinh(r)∣< min{1,c}, we have
cosh(r)
cosh2(r) −1 + c2 =
√
1 + sinh2(r) ⋅
1
sinh2(r) + c2
= 1
c2 ⋅
√
1 + sinh2(r) ⋅
1
1 + ( sinh(r)
c
)
2
= 1
c2
∞
∑
ℓ=0
(
1
2
ℓ) ⋅sinh2ℓ(r) ⋅
∞
∑
m=0
(−1)msinh(r)2m
c2m
= 1
c2
∞
∑
k=0
k
∑
τ=0
(
1
2
τ)(−1)k−τ ⋅
1
c2(k−τ) ⋅sinh2k(r)
=
∞
∑
k=0
ck ⋅sinh2k(r).
The last expression becomes by (3.125), the fact that d2k(η) = 0 for odd η, and (3.129)
∞
∑
k=0
ck ⋅
∞
∑
η=0
d2k(2η)r2η =
∞
∑
η=0
∞
∑
k=0
ck ⋅d2k(2η) ⋅r2η =
∞
∑
η=0
η
∑
k=0
ck ⋅d2k(2η) ⋅r2η.
Since this was ˜u′(r) for r ∈R with ∣sinh(r)∣< min{1,c} and the coefficients ̃ξk are given
as the coefficients of the Taylor series T(˜u) of ˜u, we get
∞
∑
η=0
̃ξη ⋅rη = T(˜u)(r) =
∞
∑
η=0
1
2η + 1
η
∑
k=0
ck ⋅d2k(2η) ⋅r2η+1,
114


---

3 Spectral invariants for polygons
hence ̃ξ2η+1 =
1
2η+1 ⋅
η
∑
k=0ck ⋅d2k(2η) = ξ2η+1 for all η ∈N0 and ̃ξ2η = 0 for all η ∈N0.
From (3.124) and Lemma 3.49 we immediately get:
Corollary 3.51.
Iij(t)
t↓0∼
∞
∑
η=0
νη(i,j)tη,
where
νη(i,j) =
1
2k(i)
(2η)!
4η+1η!
η
∑
ℓ=0
cℓ(i,j) ⋅d2ℓ(2η)
with cℓ(i,j) as in (3.132).
Recall that ˜I
1/4
γi (t) = ∑
k(i)−1
j=1
Iij(t).
Corollary 3.52. We have
˜I
1/4
γi (t)
t↓0∼
∞
∑
η=0
cη(γi)tη,
(3.139)
where
cη(γi) ∶=
1
2k(i)
(2η)!
4η+1η!
η
∑
ℓ=0
Cℓ(i) ⋅d2ℓ(2η),
Cℓ(i) ∶=
k(i)−1
∑
j=1
cℓ(i,j)
with cℓ(i,j) as in (3.132).
Corollary 3.53.
˜Z
1/4
V (t)
t↓0∼
∞
∑
η=0
cηtη,
where cη ∶=
M
∑
i=1cη(γi).
Recall that by Corollary 3.48, Z
1/4
V
and ˜Z
1/4
V
necessarily have the same asymptotic
expansion. So we can compare (3.139) with (3.97) and obtain the following theorem as
an aside.
Theorem 3.54. For all k ∈N≥2 and η ∈N0 we have the identities
η+1
∑
ℓ=1
(2η + 2
2ℓ)B2η−2ℓ+2 (1
2) ⋅B2ℓ⋅(k2ℓ−1) = (2η + 2)!
4η+1
η
∑
ℓ=0
Cℓ,k ⋅d2ℓ(2η),
(3.140)
115


---

3 Spectral invariants for polygons
where
Cℓ,k ∶=
ℓ
∑
τ=0
(
1
2
τ)(−1)ℓ−τ ⋅
k−1
∑
j=1
1
sin (j ⋅π
k)
2(ℓ−τ)+2.
Example 3.55. Let k ∈N≥2 be arbitrary. By (3.140), we can recursively evaluate the
finite trigonometric sums of the form
k−1
∑
j=1
1
sin2n (j ⋅π
k) for all n ∈N.
For example, equation (3.140) reduces to the following fomulas for η = 0,1,2 ∶
η = 0 ∶
1
3(k2 −1) =
k−1
∑
j=1
1
sin2 (j ⋅π
k).
η = 1 ∶
1
45(k4 −1) + 2
9(k2 −1) =
k−1
∑
j=1
1
sin4 (j ⋅π
k).
η = 2 ∶
2
945(k6 −1) + 1
45(k4 −1) + 8
45(k2 −1) =
k−1
∑
j=1
1
sin6 (j ⋅π
k).
The last three formulas in Example 3.55 can also be found in [CM99, p. 148] and [BY02,
p. 19/20]. Both articles actually give explicit formulas for all ∑k−1
j=1
1
sin2n(j⋅π
k ), but these
have a different form from the ones that we get recursively: They do not involve B2ℓ( 1
2),
and the formulas from [CM99] do not involve Bernoulli numbers at all. So Theorem 3.54
can be seen as yet another way of evaluating these trigonometric sums.
116


---

4 Spectral invariants for orbisurfaces
This chapter has two central goals. The first one is to compute all heat invariants for
orbisurfaces of constant curvature, which is done in the first two sections. Our strategy is
to investigate two examples of orbisurfaces thoroughly and explore the relation between
their heat traces (see Section 4.1). In Section 4.2 we use this relation to compute the
heat invariants for general orbisurfaces of constant curvature.
The second goal is to give an alternative explanation why an angle γ = π
k (k ∈N≥2) of a
polygon of constant curvature contributes to the heat invariants as stated in Corollary
3.37 (see formula (3.114)). In particular, this will, in the case of an angle γ = π
k, give an
alternative proof for the formula of the coefficients cH
ℓ(γ) from Theorem 3.32. Namely, by
Theorem 4.27 below, they can in this case be computed directly from Watson’s formula
for the cS
ℓ(γ) (see the Remark after Corollary 3.30).
4.1 Two examples of orbifolds
In this section, we want to study two examples of orbifolds and, in particular, how their
heat traces relate to each other. Our treatment presupposes some familiarity with basic
orbifold theory. Anything we presuppose in this respect can be found in [DGGW08] or
[Gor12].
Whenever appropriate, we identify the orthogonal group O(2) with the subgroup of
O(3) given by the image of the monomorphism
i ∶O(2) ∋A ↦
⎛
⎜
⎝
A
0
0
0
0
1
⎞
⎟
⎠
∈O(3).
Moreover, let M ∶= S2(r) ∶= {x ∈R3 ∣∥x∥= r } be the sphere of radius r > 0 equipped with
an O(2)-invariant Riemannian metric, i.e. O(2) is contained in the isometry group of M.
Let k ∈N≥2 be fixed. We now introduce the two orbifolds we are primarily interested
in. We denote the cyclic group of order k by Zk and we think of it as a subset Zk ⊂O(2)
generated by a rotation about the origin through the angle 2π
k . We can describe the group
explicitly as
Zk ∶= { ˜Dℓ∶= D 2π
k ℓ∶= (cos( 2π
k ℓ)
−sin( 2π
k ℓ)
sin( 2π
k ℓ)
cos( 2π
k ℓ)) ∣ℓ= 0,...,k −1}.
Each element D 2π
k ℓwith ℓ∈{0,...,k −1} acts on the Euclidean plane as a rotation about
the origin through the angle 2π
k ℓ. Thus the group Zk acts effectively on M, so M/Zk
117


---

4 Spectral invariants for orbisurfaces
becomes a good orbifold. Its only singularities are two cone points of order ∣Zk∣= k.
Next, consider the dihedral group Dk ⊂O(2), generated by the reflection in the x-axis
and a rotation about the origin through the angle 2π
k . Obviously we have the inclusion
Zk ⊂Dk and we can likewise describe the dihedral group explicitly by
Dk ∶= Zk ∪{ ˜Sℓ∶= S π
k ℓ∶= (cos( 2π
k ℓ)
sin( 2π
k ℓ)
sin( 2π
k ℓ)
−cos( 2π
k ℓ)) ∣ℓ= 0,...,k −1}.
Any element S π
k ℓwith ℓ∈{0,...,k −1} acts on the Euclidean plane as a reflection in a
line forming an angle of π
kℓwith the x-axis. Thus the dihedral group acts effectively on
M = S2(r) as well, so M/Dk becomes a good orbifold. The singular points consist of
two dihedral points with isotropy order ∣Dk∣= 2k and of mirror points which form two
connected reflector edges.
Since we are concerned mainly with those two orbifolds, it is appropriate for our
purposes to replace some of the more general definitions given in [DGGW08],[Gor12]
by simpler ones. It can be easily shown that for our orbifolds the following definitions
are equivalent to those given in [DGGW08],[Gor12].
Let G ∈{Zk,Dk} be one of the two groups introduced above and let πG ∶M →M/G be
the canonical projection. First we want to stress that the group G acts by isometries on
M, and therefore the orbifold M/G inherits from M a Riemannian metric. If the metric
of M is given by the standard metric, which is induced by Euclidean R3, then M/G is of
constant curvature κ = 1
r2. Orbifolds with such a metric are sometimes called spherical
orbifolds.
Definition 4.1. Let n ∈N0 ∪{∞}. A function ˜f ∶M/G →R is called a Cn-function
or of class Cn if and only if ˜f ○πG ∶M →R is a Cn-function. We denote the set of all
Cn-functions by Cn (M/G) and set C(M/G) ∶= C0(M/G).
Let Cn
G(M) ∶= {f ∈Cn(M) ∣γ∗f ∶= f ○γ = f for all γ ∈G} be the set of all G-invariant
Cn-functions on M.
We point out some simple relations between the function spaces of Definition 4.1. Let
n ∈N0 ∪{∞} be fixed until Definition 4.3 below. It is easy to show that the map
Φ ∶Cn(M/G) →Cn
G(M),
˜f ↦˜f ○πG =∶f
is a vector space isomorphism, i.e. it is bijective and linear. Therefore we can identify the
set of all Cn-functions on the orbifold M/G with the set of all G-invariant Cn-functions
on M. In particular, for any G-invariant Cn-function f ∶M →R there exists a unique
Cn-function ˜f ∶M/G →R with the property ˜f ○πG = f.
Obviously we have the relation C∞(M/G) ⊂Cℓ(M/G) ⊂Cℓ−1(M/G) for all ℓ∈N.
We want to remark that for our purposes the most important function spaces are those
consisting of continuous functions and smooth functions, respectively.
Definition 4.2. For any continuous function ˜f ∈C(M/G) and any open set ˜U ⊂M/G,
118


---

4 Spectral invariants for orbisurfaces
we define integration as follows:
∫
˜U
˜f ∶= ∫
˜U
˜f(˜x)d˜x ∶= 1
∣G∣∫
π−1
G ( ˜U)
( ˜f ○πG)(x)dx,
where ∣G∣denotes the order of the group. Analogously to the L2-inner product on C(M),
we can introduce the following inner product on C(M/G):
⟨˜f, ˜g⟩∶= ∫
M/G
˜f ⋅˜g = 1
∣G∣∫
M
˜f(πG(x)) ⋅˜g(πG(x))dx
= 1
∣G∣⟨Φ( ˜f),Φ(˜g)⟩L2(M)
for all ˜f, ˜g ∈C(M/G).
The space L2(M/G) is defined as the completion of (C(M/G),⟨⋅,⋅⟩). If in the sequel
an inner product appears in connection with functions, it will either refer to the inner
product of L2(M/G) or L2(M), depending on the context.
Notice that the isomorphism Φ preserves orthogonality of functions. Moreover, the
map
1
√
∣G∣
⋅Φ ∶Cn(M/G) →Cn
G(M),
˜f ↦
1
√
∣G∣
⋅Φ( ˜f)
(4.1)
is an isometry between the spaces Cn(M/G) and Cn
G(M). In particular, for any orthonor-
mal set {ui}i∈I ⊂Cn
G(M) of G-invariant functions the set {
√
∣G∣⋅˜ui}i∈I ⊂Cn(M/G) is
an orthonormal set as well, where ˜ui is, as usual, the unique map on M/G such that
˜ui ○πG = ui.
Definition 4.3. Let ∆M denote the Dirichlet Laplacian of M. The Laplacian of M/G is
the linear operator
∆M/G ∶C∞(M/G) →C∞(M/G),
˜f ↦∆M/G( ˜f),
where for any ˜f ∈C∞(M/G) the function ∆M/G( ˜f) is defined as the unique smooth
function such that ∆M/G( ˜f) ○πG = ∆M( ˜f ○πG).
Note that the smooth function ∆M( ˜f ○πG) is G-invariant since G acts by isometries
on M. Another way to write ∆M/G is given by
∆M/G = Φ−1 ○∆M ○Φ.
The following theorem is well-known.
Theorem 4.4. (see [DGGW08, Proposition 3.1]) The Laplacian of M/G has a discrete
spectrum 0 = λ1 ≤λ2 ≤... with λj →∞as j →∞and with each eigenvalue having finite
119


---

4 Spectral invariants for orbisurfaces
multiplicity. The normalised eigenfunctions are smooth and form an orthonormal basis
of L2(M/G).
Let σ(M/G) ∶= {λ1,λ2,...} denote the set of all eigenvalues of ∆M/G (without multi-
plicities) and let
Eλ(M/G) ∶= { ˜f ∈C∞(M/G) ∣∆M/G ˜f = λ ˜f }
be the eigenspace corresponding to an eigenvalue λ ∈σ(M/G). The sets σ(M),Eλ(M)
are defined correspondingly. Further, let
Eλ(M)G ∶= Eλ(M) ∩C∞
G (M) = {f ∈Eλ(M) ∣γ∗f = f for all γ ∈G}
be the set of all G-invariant eigenfunctions for any eigenvalue λ ∈σ(M).
By elementary observations, one can recognise a close relationship between the eigenval-
ues and eigenfunction of ∆M/G and ∆M: Suppose ˜f ∈Eλ(M/G), i.e. ∆M/G( ˜f) = λ ˜f. Then
λ is also an eigenvalue of ∆M and f ∶= ˜f ○πG is a corresponding G-invariant eigenfunction
on M. Conversely, suppose f ∈Eλ(M)G is a G-invariant eigenfunction. Then λ will be
an eigenvalue of ∆M/G and there exists a unique eigenfunction ˜f ∈Eλ(M/G) such that
˜f ○πG = f. In short,
Φ∣Eλ(M/G) ∶Eλ(M/G) →Eλ(M)G
(4.2)
is a linear isomorphism. In analogy to (4.1), we have the isometry
1
√
∣G∣
⋅Φ∣Eλ(M/G) ∶Eλ(M/G) →Eλ(M)G.
(4.3)
Recall that ˜S0 ∈Dk is a reflection in Euclidean R3. The (Riemannian) isometry
˜S0 ∶M →M induces the linear and symmetric map
˜S∗
0 ∶(C∞(M),⟨⋅,⋅⟩L2(M)) ∋f ↦f ○˜S0 ∈(C∞(M),⟨⋅,⋅⟩L2(M)).
This map is an involution, i.e. it satisfies ˜S∗
0 ○˜S∗
0 = Id. Furthermore, the spaces C∞
G (M)
and Eλ(M)G are invariant under ˜S∗
0 (see below). Thus one can replace the linear space
C∞(M) by its linear subspaces C∞
G (M) and Eλ(M)G respectively, without losing any of
the above properties of ˜S∗
0. More precisely, the maps
˜S∗
0 ∶C∞
G (M) →C∞
G (M),
f ↦f ○˜S0
and
˜S∗
0 ∶Eλ(M)G →Eλ(M)G,
f ↦f ○˜S0
are linear symmetric involutions. The spaces C∞
G (M) are indeed invariant under ˜S∗
0: If
G = Dk, then ˜S∗
0 restricted to C∞
Dk(M) is just the identity map. If G = Zk, then one
120


---

4 Spectral invariants for orbisurfaces
can make use of the identity ˜S0 ○˜Dℓ= ˜Dk−ℓ○˜S0 for any ℓ∈{0,...,k −1}. Thus for any
f ∈C∞
Zk(M) and ℓ∈{0,...,k −1} we have
(f ○˜S0) ○˜Dℓ= f ○˜Dk−ℓ○˜S0 = f ○˜S0.
Furthermore, for any G-invariant eigenfunction f ∈Eλ(M)G we indeed have f ○˜S0 ∈
Eλ(M)G: On the one hand, f ○˜S0 is G-invariant by the discussion above and on the
other hand f ○˜S0 is an eigenfunction since ˜S0 is an isometry.
With all the basic observations described above, we are now ready to define and relate
the heat traces for our orbifolds.
Lemma 4.5. Let λ ∈σ(M/Zk) be an eigenvalue. The (finite dimensional) inner product
space Eλ(M)Zk = C∞
Zk(M) ∩Eλ(M) has an orthonormal basis consisting of ˜S0-invariant
and ˜S0-anti-invariant functions. More precisely, there exists an orthonormal basis {uλ
i }nλ
i=1
with nλ ∈N such that any function uλ
i is either ˜S0-invariant, i.e. ˜S∗
0uλ
i = uλ
i ○˜S0 = uλ
i , or
˜S0-anti-invariant, i.e. ˜S∗
0uλ
i = uλ
i ○˜S0 = −uλ
i .
Proof. Because of the map given in (4.2) the vector space Eλ(M)Zk is isomorphic to
Eλ(M/Zk), which in turn is finite dimensional by Theorem 4.4. Hence the space Eλ(M)Zk
must be a finite dimensional vector space for any λ ∈σ(M/Zk).
The map ˜S∗
0 ∶Eλ(M)Zk →Eλ(M)Zk is symmetric and linear, and thus by the spectral
theorem there exists an orthonormal basis of eigenfunctions of ˜S∗
0 for Eλ(M)Zk. But ˜S∗
0
is an involution, i.e. the only eigenvalues are 1,−1. The eigenfunctions corresponding to
the eigenvalue 1 are the ˜S0-invariant functions, and the eigenfunctions corresponding to
the eigenvalue −1 are the ˜S0-anti-invariant functions.
By using the isometry (4.3) with G = Zk and ∣Zk∣= k, we get the following corollary:
Corollary 4.6. For any eigenvalue λ ∈σ(M/Zk) let {uλ
i }nλ
i=1 be an orthonormal basis of
Eλ(M)Zk like in the previous lemma.
(i) Then the set {
√
k⋅˜uλ
i }nλ
i=1 is an orthonormal basis for Eλ(M/Zk), where the functions
˜uλ
i with i = 1,...,nλ are defined by the relation ˜uλ
i ○πZk = uλ
i .
(ii) Furthermore, the collection
⋃
λ∈σ(M/Zk)
{
√
k ⋅˜uλ
i }nλ
i=1
(4.4)
is an orthonormal basis for L2(M/Zk) consisting of smooth eigenfunctions of ∆M/Zk.
Consider the collection of all bases {uλ
i }nλ
i=1 described in Lemma 4.5 over all λ ∈σ(M/Zk),
i.e.
⋃
λ∈σ(M/Zk)
{uλ
i }nλ
i=1.
121


---

4 Spectral invariants for orbisurfaces
Any element uλ
i of this collection is a smooth Zk-invariant eigenfunction on M which
happens to be either ˜S0-invariant or ˜S0-anti-invariant. We reorder and rename this
collection in order to obtain a better notation for the sequel. Let {ϕi}i∈I, I ⊂N, be all
those functions in this collection which are ˜S0-invariant, and let τi ∈σ(M/Zk) be such
that ∆M(ϕi) = τi ⋅ϕi. Similarly, let {ψj}j∈J, J ⊂N, be all those functions in the collection
which are ˜S0-anti-invariant, and let µj ∈σ(M/Zk) be such that ∆M(ψj) = µj ⋅ψj.
As usual, let ˜ψj ∈C∞(M/Zk), j ∈J, be the unique smooth function on M/Zk such
that ˜ψj ○πZk = ψj. Each of the functions ϕi ∶M →R is Zk-invariant and ˜S0-invariant.
Thus it is Dk-invariant as well. As any Dk-invariant smooth function on M, it induces
unique smooth functions ˜ϕi ∈C∞(M/Zk) and ˆϕi ∈C∞(M/Dk) such that ˜ϕi ○πZk = ϕi
and ˆϕi ○πDk = ϕi.
Proposition 4.7. We have the following orthonormal basis:
(i) The system {
√
k⋅˜ϕi}i∈I∪{
√
k⋅˜ψi}j∈J is an orthonormal basis for L2(M/Zk) consisting
of smooth eigenfunctions of ∆M/Zk.
(ii) The set of functions {
√
2k ⋅ˆϕi}i∈I is an orthonormal basis for L2(M/Dk) consisting
of smooth eigenfunctions of ∆M/Dk.
Proof. The first statement is obvious, since by definition
{
√
k ⋅˜ϕi}i∈I ∪{
√
k ⋅˜ψj}j∈J =
⋃
λ∈σ(M/Zk)
{
√
k ⋅˜uλ
i }nλ
i=1.
Hence by Corollary 4.6, this collection is an orthonormal basis for L2(M/Zk) as claimed.
The second statement follows similarly by using the isometry (4.3) with G = Dk and
∣Dk∣= 2k.
The following theorem is a special case of a well-known, more general theorem (see e.g.
[DGGW08],[Gor12] or Theorem 4.5 in [Don79]).
Theorem 4.8. Let G ∈{Zk,Dk} and let 0 = λ1 ≤λ2 ≤... ↗∞be the sequence of eigen-
values (with multiplicities) of the Laplacian ∆M/G as in Theorem 4.4 above. Furthermore,
let {φi}∞
i=1 be an orthonormal basis for L2(M/G) consisting of smooth eigenfunctions of
the Laplacian such that ∆M/Gφi = λi ⋅φi for all i ∈N. Then the heat kernel of M/G exists
and is given by
KM/G(˜x, ˜y;t) =
∞
∑
i=1
e−λitφi(˜x)φi(˜y) for all ˜x, ˜y ∈M/G and t > 0.
The heat trace can be written as
ZM/G(t) ∶=
∞
∑
i=1
e−λit = ∫
M/G
KM/G(˜x, ˜x;t)d˜x for t > 0.
122


---

4 Spectral invariants for orbisurfaces
Because of the above theorem and Proposition 4.7 we get:
KM/Zk(˜x, ˜x;t) = ∑
i
e−τit (
√
k ⋅˜ϕi(˜x))
2
+ ∑
j
e−µjt (
√
k ⋅˜ψj(˜x))
2
= k ⋅∑
i
e−τit ˜ϕi(˜x)2 + k ⋅∑
j
e−µjt ˜ψj(˜x)2
for all ˜x ∈M/Zk and t > 0, and
KM/Dk(ˆx, ˆx;t) = ∑
i
e−τit (
√
2k ⋅ˆϕi(ˆx))
2
= 2k ⋅∑
i
e−τit ˆϕi(ˆx)2
for all ˆx ∈M/Dk and t > 0. Thus, for all t > 0 and any open set U ⊂M, which is invariant
under O(2), we have:
∫πZk(U) KM/Zk (˜x, ˜x;t)d˜x =
1
∣Zk∣∫U KM/Zk (πZk(x),πZk(x);t)dx
= ∫U ∑
i
e−τit ( ˜ϕi(πZk(x)))2 dx + ∫U ∑
j
e−µjt ( ˜ψj(πZk(x)))
2 dx
= ∫U ∑
i
e−τitϕi(x)2dx + ∫U ∑
j
e−µjtψj(x)2dx,
∫πDk(U) KM/Dk (ˆx, ˆx;t)dˆx =
1
∣Dk∣∫U KM/Dk (πDk(x),πDk(x);t)dx
= ∫U ∑
i
e−τit ( ˆϕi(πDk(x)))2 dx
= ∫U ∑
i
e−τitϕi(x)2dx.
Hence,
∫πZk(U) KM/Zk (˜x, ˜x;t)d˜x = ∫πDk(U) KM/Dk (ˆx, ˆx;t)dˆx + ∫
U
∑
j
e−µjtψj(x)2dx
´¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¶
=∶G(t)
.
(4.5)
Next, we want to investigate the function t ↦G(t). We will show that this function is
closely related to the Dirichlet heat kernel for a spherical lune with angle π
k.
For i ∈{0,...,k −1}, let Fix( ˜Si) ⊂M be the fixed point set of the reflection ˜Si ∈Dk. Let
Ω⊂M be a spherical lune or 2-gon with vertices being the north pole and south pole,
angle π
k and with ∂Ω⊂Fix( ˜S0) ∪Fix( ˜S1). Using spherical coordinates
ξ ∶(0,2π) × (−π
2 , π
2 ) ∋(θ,ν) ↦
⎛
⎜
⎝
r cos(ν)cos(θ)
r cos(ν)sin(θ)
r sin(ν)
⎞
⎟
⎠
∈M,
123


---

4 Spectral invariants for orbisurfaces
the set Ωcan be chosen as
Ω∶= {(θ,ν) ∣0 < θ < π
k ; −π
2 < ν < π
2 }.
The boundary can be decomposed into two sides γ0 ∶= Fix( ˜S0)∩∂Ωand γ1 ∶= Fix( ˜S1)∩∂Ω.
Since Ω⊂M is a relatively compact domain, the spectrum of the Dirichlet Laplacian ∆Ω
consists of a sequence of non-negative eigenvalues and any eigenvalue has finite multiplicity
(see Proposition 2.4). Let us enumerate the eigenvalues of ∆Ωwith multiplicities as follows:
0 < ν1 < ν2 ≤ν3 ≤... ↗∞.
Moreover, there exists an orthonormal basis {ωj}∞
j=1 for L2(Ω), such that for any j ∈N
the function ωj is a smooth eigenfunction of ∆Ωcorresponding to the eigenvalue νj.
The Dirichlet heat kernel for Ωcan be written as
KΩ(x,y;t) =
∞
∑
j=1
e−νjtωj(x)ωj(y) for all x,y ∈Ωand t > 0,
and the trace of the Dirichlet heat kernel is given by
ZΩ(t) =
∞
∑
j=1
e−νjt = ∫
Ω
KΩ(x,x;t)dx for all t > 0.
Lemma 4.9. Let ∆∶C∞(Ω) →C∞(Ω), ∆(f) ∶= −div(∇f) (where ∇and div are taken
with respect to the metric on M = S2(r)) be the Laplace operator. Recall that for any
j ∈J the function ψj ∈C∞
Zk(M) is an ˜S0-anti-invariant eigenfunction of the Dirichlet
Laplacian ∆M corresponding to the eigenvalue µj.
(i) For any j ∈J the function ψj∣Ωis a classical solution to the Dirichlet eigenvalue
problem on Ω. This means that ψj∣Ω∈C∞(Ω) ∩C(Ω) and
∆ψj∣Ω(x) = µj ⋅ψj∣Ω(x) for all x ∈Ω
and
ψj∣Ω(x) = 0
for all x ∈∂Ω.
(ii) Moreover, the set {
√
2k ⋅ψj∣Ω}
j∈J is an orthonormal set in L2(Ω) consisting of
smooth eigenfunctions for the Dirichlet Laplacian ∆Ω.
Proof. (i). Let j ∈J be arbitrary. All statements of (i) are obvious except possibly
that ψj vanishes pointwise on the boundary ∂Ω, i.e. ψj(x) = 0 for all x ∈∂Ω. Since
∂Ω⊂Fix( ˜S0) ∪Fix( ˜S1) it suffices to show that ψj vanishes on the sets Fix( ˜Si), i = 0,1:
Let x ∈Fix( ˜S0). Then we have ψj(x) = ψj( ˜S0x) = ( ˜S∗
0ψj)(x) = −ψj(x). Hence ψj(x) = 0
and ψj vanishes on Fix( ˜S0).
In order to show that ψj vanishes on Fix( ˜S1), observe that the function ψj is ˜S1-anti-
invariant as well. In fact ˜D1 ○˜S0 = ˜S1, and thus ˜S1-anti-invariance of ψj follows from its
124


---

4 Spectral invariants for orbisurfaces
Zk-invariance and ˜S0-anti-invariance.
(ii). As any classical solution of the Dirichlet eigenvalue problem, the function ψj∣Ωis
contained in the domain of the Dirichlet Laplacian and is also a smooth eigenfunction of
∆Ω(see [Gri09, Exercise 8.3 and the remark thereafter]). It remains to show that
{
√
2k ⋅ψj∣Ω}
j∈J
is an orthonormal set in L2(Ω). By using the decomposition
M/
k−1
⋃
i=0
Fix( ˜Si) =
k−1
⊍
i=0
˜Di(Ω∪˜S0(Ω)),
and the Zk-invariance and ˜S0-anti-invariance of ψj, we get for all j,ℓ∈J:
⟨ψj,ψℓ⟩L2(M) = ∫
M
ψj(x) ⋅ψℓ(x)dx = k
∫
Ω∪˜S0(Ω)
ψj(x) ⋅ψℓ(x)dx
= 2k ∫
Ω
ψj(x) ⋅ψℓ(x)dx = ∫
Ω
√
2k ⋅ψj∣Ω(x) ⋅
√
2k ⋅ψℓ∣Ω(x)dx
= ⟨
√
2k ⋅ψj∣Ω,
√
2k ⋅ψℓ∣Ω⟩
L2(Ω) .
Therefore {
√
2k ⋅ψj∣Ω}
j∈J ⊂L2(Ω) is an orthonormal set in L2(Ω) consisting of smooth
eigenfunctions of the Dirichlet Laplacian.
Theorem 4.10. For all U ⊂M, which are O(2)-invariant, we have
G(t) = ∫U∩ΩKΩ(x,x;t)dx for all t > 0,
where G(t) = ∫
U
∑
j∈J e−µjtψj(x)2dx as defined above. Thus, by (4.5)
∫πZk(U) KM/Zk (˜x, ˜x;t)d˜x −∫πDk(U) KM/Dk (ˆx, ˆx;t)dˆx = ∫U∩ΩKΩ(x,x;t)dx.
(4.6)
In particular, we have for U = M:
ZM/Zk(t) −ZM/Dk(t) = ZΩ(t) for all t > 0.
(4.7)
Proof. Because the functions ψj are Zk-invariant and ˜S0-anti-invariant, we have
G(t) = ∫
U∩Ω
∑
j∈J
e−µjt (
√
2k ⋅ψj(x)∣Ω)
2
dx.
Therefore it suffices to prove that the set {
√
2k ⋅ψj∣Ω}
j∈J is an orthonormal basis for
125


---

4 Spectral invariants for orbisurfaces
L2(Ω) of eigenfunctions of the Dirichlet Laplacian ∆Ω. We know from Lemma 4.9 (ii)
that this set is an orthonormal set in L2(Ω) consisting of smooth eigenfunctions of the
Dirichlet Laplacian. Hence it remains to show that this set is complete in L2(Ω).
We want to emphasise first the following relations. We know by Proposition 4.7 that
the set
{
√
k ⋅˜ϕi}i∈I ∪{
√
k ⋅˜ψj}j∈J
is an orthonormal basis for L2(M/Zk) consisting of smooth eigenfunctions. In particular,
any continuous function ˜f ∈C(M/Zk) orthogonal to this set must vanish identically, i.e.,
if ˜f ⊥{
√
k ⋅˜ϕi}i∈I ∪{
√
k ⋅˜ψj}j∈J, then ˜f ≡0.
By using the isometry (4.1) for n = 0,∞one gets immediately that the set
{ϕi}i∈I ∪{ψj}j∈J
is an orthonormal set in the space CZk(M), consisting of smooth and Zk-invariant
eigenfunctions. Moreover, any continuous function f ∈CZk(M) with f ⊥{ϕi}i∈I ∪{ψj}j∈J
must vanish, i.e. f ≡0.
Let f ∈C(Ω) be given such that f vanishes on the boundary ∂Ωand f ⊥{
√
2k⋅ψj∣Ω}j∈J.
We now extend f continuously on M in two steps. Firstly, extend it onto ˜S1(Ω) by setting
f( ˜S1x) ∶= −f(x) for all x ∈Ω. Secondly, extend this function continuously onto M such
that it becomes Zk-invariant.
This function is now perpendicular to {ψj}j∈J in L2(M) by construction and the
initial assumption on f∣Ω. Similary, it is perpendicular to the set {ϕi}i∈I in L2(M) by
construction. Hence, by the above considerations, f must vanish on M.
4.2 Heat invariants for orbisurfaces
In this section, we assume throughout that M = S2(r) is equipped with the standard
Riemannian metric induced by Euclidean R3. Recall that we proved in the first section
(see (4.7)):
ZM/Zk(t) −ZM/Dk(t) = ZΩ(t) for all t > 0.
We aim to compute the coefficients of the asymptotic expansions as t ↘0 for all three
heat traces appearing in the above equation. We will thereby obtain explicit formulas
for all coefficients and it will be possible to recognise the contribution of any singular
stratum to the asymptotic expansion.
Throughout this section, we will use the definitions and results given in [DGGW08].
In particular, Definition 2.3 and the beginning of Section 4 up to the end of the proof of
Theorem 4.8 of that article are relevant. Sometimes we will change the notation slightly
compared to [DGGW08], mainly because the statements in [DGGW08] are formulated
for general orbifolds, whereas we are dealing only with two special orbifolds.
126


---

4 Spectral invariants for orbisurfaces
The following theorem is a special case of Theorem 4.8 in [DGGW08].
Theorem 4.11. Let O be a two-dimensional closed Riemannian orbifold and let λ1 ≤
λ2 ≤... be the spectrum of the Lapacian ∆O. The heat trace ZO(t) = ∑∞
i=1 e−λit of O is
asymptotic as t ↘0 to
I0(O) +
∑
N∈S(O)
IN(O)
∣Iso(N)∣,
where S(O) is the set of all singular O-strata and where ∣Iso(N)∣is the order of the
isotropy at each p ∈N. The symbols I0(O), IN(O) are defined to be:
I0(O) = (4πt)−1 ⋅
∞
∑
i=0
ai(O)ti,
IN(O) = (4πt)−dim(N)
2
⋅
∞
∑
i=0
ti ∫
N
bi(N,x)dvolN(x),
where ai(O) and bi(N,x) are given as in [DGGW08, Definition 4.7].
We will apply the above theorem to the orbifolds M/G with G ∈{Zk,Dk}. Note that
M/G is finitely covered by M and thus ai(O) =
1
∣G∣ai(M), where ai(M) denote the
familiar heat invariants for the manifold M (see the comment at the end of Definition
4.7 in [DGGW08]). The M/G-strata are defined as the connected components of the
G-isotropy equivalence classes in M/G. Let us investigate what the G-isotropy equivalence
classes look like for our orbifolds and then apply Theorem 4.11.
Let xN ∶= (0,0,r) and xS ∶= (0,0,−r). The orbifold M/Zk has two Zk-isotropy equiva-
lence classes. If ˜xN ∶= πZk(xN), ˜xS ∶= πZk(xS) are the cone points, one isotropy equivalence
class is given by the set {˜xN, ˜xS} which has two connected components {˜xN},{˜xS}. The
isotropy group of ˜xN, ˜xS is given by IsoZk{˜xN} = Zk = IsoZk{˜xS} so that the isotropy
order is ∣Zk∣= k. All the other points in M/Zk are regular and constitute the other
Zk-isotropy equivalence class. Hence, we get
ZM/Zk(t)
t↓0∼I0(M/Zk) + 1
kI{˜xN}(M/Zk) + 1
kI{˜xS}(M/Zk).
(4.8)
The number of Dk-isotropy equivalence classes of the orbifold M/Dk depends on whether
k is even or odd. Let us first assume that k is even. Then the orbifold M/Dk has four
Dk-isotropy equivalence classes. Let ˆxN ∶= πDk(xN), and ˆxS ∶= πDk(xS) be the two dihedral
points. Then {ˆxN, ˆxS} is an isotropy equivalence class with two connected components
{ˆxN}, {ˆxS} and isotropy group IsoDk{ˆxN} = Dk = IsoDk{ˆxS}. Thus the isotropy order is
∣Dk∣= 2k.
Two of the remaining isotropy equivalence classes consist of mirror points. Recall
that γ0, γ1 ⊂M are the two sides of the lune Ω. The two isotropy equivalence classes
are represented by the sets Mir0 ∶= πDk (γ0)/{ˆxN, ˆxS} and Mir1 ∶= πDk (γ1)/{ˆxN, ˆxS},
respectively. Both isotropy equivalence classes are connected. The conjugacy class of
127


---

4 Spectral invariants for orbisurfaces
the isotropy group of any ˜p ∈Mir0 is given by {{e, ˜Sℓ} ∣ℓ= 0,2,4,...,k −2}, where e
denotes the identity element of the dihedral group Dk. Similarly the conjugacy class of
the isotropy group of any ˜p ∈Mir1 is given by {{e, ˜Sℓ} ∣ℓ= 1,3,5,...,k −1}. Hence the
isotropy order is ∣IsoDk(˜p)∣= 2 for any ˜p ∈Mir0 ∪Mir1.
The fourth M/Dk-isotropy equivalence class consists of the regular points
(M/Dk)/
1
⋃
i=0
πDk(γi).
Hence we get
ZM/Dk(t)
t↓0∼I0(M/Dk) + 1
2kI{ˆxN}(M/Dk) + 1
2kI{ˆxS}(M/Dk)
+ 1
2 (IMir0(M/Dk) + IMir1(M/Dk)).
(4.9)
If k is odd, then we have three Dk-isotropy equivalence classes. Two of them are given
as above by the set of dihedral points and regular points, respectively. However, for odd k
all reflections ˜Sℓare conjugate to each other, such that the third Dk-isotropy equivalence
class is given by the set of all mirror points
Mir0 ⊍Mir1.
This isotropy equivalence class has two connected components, namely, Mir0 and Mir1.
The conjugacy class of the isotropy group of any ˜p ∈Mir0 ∪Mir1 is given by {{e, ˜Sℓ} ∣
ℓ= 0,...,k −1} and hence the isotropy order is ∣IsoD2k(˜p)∣= 2. We conclude that the
asymptotic expansion (4.9) holds for odd k as well.
Remark. The above analysis together with Theorem 4.11 shows that there will be no
half-powers of t in the asymptotic expansion of ZM/Zk(t). In particular, by (4.7), the mirror-
edge contribution B to ZM/Dk(t) must equal the negative of the boundary contribution
to ZΩ(t). Moreover, we will show that the contribution C of the dihedral points to the
asymptotic expansion of ZM/Dk(t) equals half the contribution of the cone points to
ZM/Zk(t). The same obviously holds for the contribution A of the interior to the asymptotic
expansion of ZM/Dk(t). So it will follow that ZΩ(t)
t↓0∼(2A+2C)−(A+B +C) = A−B +C.
We will state this more explicitly in Corollary 4.13 further below.
Before we compute the coefficients in the above asymptotic expansions explicitly, we
want to simplify the asymptotic expansions given in (4.8) and (4.9).
As it is remarked in [DGGW08] (see the proof of Theorem 4.8), we can express
IN(M/G) by
˜I ˜
N1 + ... + ˜I ˜
Nn =
∣G∣
∣IsoG(N)∣IN(M/G),
(4.10)
where ˜N1,..., ˜Nn are the mutually isometric M-strata with π−1
G (N) = ⊍n
i=1 ˜Ni, and for all
128


---

4 Spectral invariants for orbisurfaces
M-strata ˜N ⊂M:
˜I ˜
N ∶= (4πt)−dim( ˜
N)
2
∞
∑
i=0
ti ∫
˜
N
bi( ˜N,x)dvol ˜
N(x),
(4.11)
bi( ˜N,x) ∶=
∑
γ∈Isomax( ˜
N)
bi (γ,x).
(4.12)
By definition, for any M-stratum ˜N, the set Isomax( ˜N) ⊂G is defined as the set of all
γ ∈G such that ˜N is open in the fixed point set Fix(γ) of γ.
The functions bi (γ,x), first defined by H. Donnelly in his article [Don76], have two
important properties, which are called “locality” and “universality” in [DGGW08]. Be-
cause of the universality property, for any isometry σ ∶M →M satisfying σ ○γ = γ′ ○σ,
we have
bi(γ,x) = bi(γ′,σ(x)) for all x ∈Fix(γ).
(4.13)
Lemma 4.12.
(i) I{˜xN}(M/Zk) = I{˜xS}(M/Zk) = I{ˆxS}(M/Dk) = I{ˆxN}(M/Dk) and
I{˜xN}(M/Zk) =
∞
∑
i=0
ti ⋅
k−1
∑
ℓ=1
bi( ˜Dℓ,xN).
(ii) IMir0(M/Dk) = IMir1(M/Dk) and
IMir0(M/Dk) = (4πt)−1
2
∞
∑
i=0
ti ⋅1
2
∫
Fix( ˜S0)
bi( ˜S0,x)dvolFix( ˜S0)(x).
Proof. (i). Obviously, π−1
Zk(˜xN) = {xN} = π−1
Dk(ˆxN), π−1
Zk(˜xS) = {xS} = π−1
Dk(ˆxS), and
Isomax ({˜xN}) = Zk/{e} = Isomax ({˜xS}),
Isomax ({ˆxN}) = Zk/{e} = Isomax ({ˆxS}).
Thus by using (4.10)-(4.12) we get, noting that ∫{xN} bi( ˜Dℓ,x)dvol{xN}(x) = bi( ˜Dℓ,xN)
by the definition of the integral over a one-point set:
I{˜xN}(M/Zk) =
∞
∑
i=0
ti ⋅
k−1
∑
ℓ=1
bi( ˜Dℓ,xN) = I{ˆxN}(M/Dk),
I{˜xS}(M/Zk) =
∞
∑
i=0
ti ⋅
k−1
∑
ℓ=1
bi( ˜Dℓ,xS) = I{ˆxS}(M/Dk).
Therefore it suffices to show that for any ˜Dℓ∈Zk:
bi( ˜Dℓ,xN) = bi( ˜Dℓ,xS).
129


---

4 Spectral invariants for orbisurfaces
Using σ ○˜Dℓ= ˜Dℓ○σ for the reflection σ in the (x,y)-plane, this follows trivially by the
universality property (4.13) of bi(γ,x).
We now turn to (ii). We have
π−1
Dk(Mir0) = (
k−1
⊍
ℓ=0
˜Dℓγ0)/{xN,xS},
π−1
Dk(Mir1) = (
k−1
⊍
ℓ=0
˜Dℓγ1)/{xN,xS},
where γ0/{xN,xS} and γ1/{xN,xS} are connected components of Fix( ˜S0)/{xN,xS} and
Fix( ˜S1)/{xN,xS}, respectively. Again by using universality of the functions bi(γ,x) and
equations (4.10)-(4.12), we obtain:
IMir0(M/Dk) = (4πt)−1
2
∞
∑
i=0
ti ⋅1
2
∫
Fix( ˜S0)
bi( ˜S0,x)dvolFix( ˜S0)(x),
IMir1(M/Dk) = (4πt)−1
2
∞
∑
i=0
ti ⋅1
2
∫
Fix( ˜S1)
bi( ˜S1,x)dvolFix( ˜S1)(x).
By using universality once again, we get IMir0(M/Dk) = IMir1(M/Dk).
Because of the universality property of the functions bi (γ,x), it is easy to show that
bi ( ˜S0,x) is constant on Fix( ˜S0). Hence by setting bi( ˜S0) ∶= bi( ˜S0,a∗) for some fixed
a∗∈Fix( ˜S0), we get
∫
Fix( ˜S0)
bi( ˜S0,x)dvolFix( ˜S0)(x) = bi ( ˜S0) ⋅∣Fix( ˜S0)∣= bi ( ˜S0) ⋅2πr,
hence IMir0(M/Dk) = (4πt)−1
2 ∑∞
i=0 ti ⋅πrbi( ˜S0). Furthermore, for any ℓ∈{0,...,k −1}, we
set bi( ˜Dℓ) ∶= bi( ˜Dℓ,xN).
Corollary 4.13. Letting
A ∶= I0(M/Dk) =
1
4πt
∞
∑
i=0
ai(M)
2k
ti = 1
2I0(M/Zk),
B ∶= IMir0(M/Dk) =
1
√
4πt
∞
∑
i=0
ti ⋅πrbi ( ˜S0), and
C ∶= 1
kI{ˆxN}(M/Dk) =
∞
∑
i=0
ti ⋅1
k
k−1
∑
ℓ=1
bi ( ˜Dℓ),
we obtain from (4.8), (4.9), and Lemma 4.12:
ZM/Zk(t)
t↓0∼2A + 2C,
130


---

4 Spectral invariants for orbisurfaces
ZM/Dk(t)
t↓0∼A + B + C.
In particular, by (4.7):
ZΩ(t)
t↓0∼A −B + C.
(4.14)
In order to get explicit formulas for the coefficients bi ( ˜S0) and ∑k−1
ℓ=1 bi ( ˜Dℓ) for all
i ∈N0, we will now compute the asymptotic expansion of ZΩ(t) and the coefficients
ai(M) explicitly. Both the coefficients ai(M) and the asymptotic expansion of ZΩ(t)
were computed in [Wat05] for the radius r = 1. But since the statements and proofs
in [Wat05] have some typographical errors, we will reproduce the relevant parts with
corrections in Proposition 4.15 and Proposition 4.17 below. We will comment shortly on
the errors contained in the corresponding statements of the article [Wat05] afterwards.
Recall the Bernoulli polynomials Bk(x) and Bernoulli numbers Bk from (3.69).
Lemma 4.14.
−Bn (1
2) = Bn ⋅(1 −
1
2n−1) for all n ∈N0.
(4.15)
Proof. Consider first the sum of the generating functions for Bn ( 1
2) and Bn:
t ⋅e
t
2
et −1 +
t
et −1 = t(e
t
2 + 1)
et −1
=
t
e
t
2 −1
⋅e
t
2 + 1
e
t
2 + 1
=
t
e
t
2 −1
= 2 ⋅
t
2
e
t
2 −1
.
Hence,
Bn (1
2) + Bn = 2 ⋅Bn
2n for all n ∈N0,
from which (4.15) follows.
Proposition 4.15. Let ZS2(r)(t) be the heat trace for the sphere of radius r > 0. Then
ZS2(r)(t)
t↓0∼
1
κ ⋅t +
∞
∑
ν=0
iS
ν ⋅κν ⋅tν,
(4.16)
where κ = 1
r2 denotes the Gaussian (or sectional) curvature and
iS
ν ∶=
ν+1
∑
ℓ=0
1
4ℓ⋅ℓ!i(s)
ν−ℓfor all ν ∈Z≥−1,
(4.17)
i(s)
ℓ
∶= (−1)ℓ+1
(ℓ+ 1)!B2ℓ+2 (1
2) for all ℓ∈Z≥−1.
(4.18)
131


---

4 Spectral invariants for orbisurfaces
Proof. First we assume that r = 1. The eigenvalues of the sphere S2(1) are the numbers
ℓ⋅(ℓ+ 1), where ℓ∈N0, and each ℓ⋅(ℓ+ 1) has multiplicity 2ℓ+ 1. Thus the heat trace is
given by
ZS2(1)(t) =
∞
∑
ℓ=0
(2ℓ+ 1)e−ℓ(ℓ+1)t for t > 0.
(4.19)
As before, it is more convenient to consider a shifted heat trace; in contrast to the
hyperbolic case, the convenient factor is now e−t
4 instead of e
t
4. The shifted trace function
is given by
Z−1/4
S2(1)(t) ∶= e−t
4
∞
∑
ℓ=0
(2ℓ+ 1)e−ℓ(ℓ+1)t =
∞
∑
ℓ=0
(2ℓ+ 1)e−(ℓ(ℓ+1)+ 1
4 )t
=
∞
∑
ℓ=0
(2ℓ+ 1)e−(ℓ+ 1
2 )2t.
The asymptotic expansion of the function Z−1/4
S2(1)(t) has been known for a long time and
can be found in [Mul28], where the expansion is given as
Z−1/4
S2(1)(t)
t↓0∼1
t +
∞
∑
n=0
(−1)n
(n + 1)!B2n+2 ⋅(1 −
1
22n+1)tn.
By using (4.15) from Lemma 4.14, we can rewrite the coefficients as
(−1)n
(n + 1)!B2n+2 ⋅(1 −
1
22n+1) = (−1)n+1
(n + 1)!B2n+2 (1
2) = i(s)
n
and we obtain
Z−1/4
S2(1)(t)
t↓0∼1
t +
∞
∑
n=0
i(s)
n tn.
(4.20)
Hence we get
ZS2(1)(t)
t↓0∼1
t +
∞
∑
ν=0
(
1
4ν+1 (ν + 1)! +
ν
∑
ℓ=0
1
4ℓ⋅ℓ!i(s)
ν−ℓ)
´¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¶
= iSν
tν.
(4.21)
Thus the case r = 1 is established. By scaling the Riemannian metric one can now easily
deduce the general case r > 0 from the special case r = 1, just as we did in the proof of
Corollary 3.37. If gS2(1) denotes the standard metric on S2(1), then λ1 ≤λ2 ≤... are the
eigenvalues of (S2(1),gS2(1)) listed with multiplicities, if and only if λ1
r2 ≤λ2
r2 ≤... are the
eigenvalues of (S2(1),r2gS2(1)) listed with multiplicities. Thus, if Z(r2gS2(1),t) denotes
132


---

4 Spectral invariants for orbisurfaces
the heat trace of the space (S2(1),r2gS2(1)), we have
ZS2(r)(t) = Z(r2gS2(1),t) =
∞
∑
i=1
e−λi
r2 ⋅t =
∞
∑
i=1
e−λi t
r2 = ZS2(1) ( t
r2) = ZS2(1) (κt).
Remark. Basically the asymptotic expansion (4.20) for the shifted heat trace is stated in
[Wat05, Lemma 16] by referring to [Mul28]. Let us point out some aspects of Lemma 16
which might be confusing. First of all, the function considered in Lemma 16, which is
denoted there by Z(s)
int (Ω,t), is not defined anywhere in the article [Wat05]. We assume
that Watson means the following function:
Z(s)
int (Ω,t) ∶= ∣Ω∣
4π Z(s)
S2(1)(t),
where Z(s)
S2(1)(t) ∶= Z−1/4
S2(1)(t) is the function we introduced above and ∣Ω∣is the volume of
a spherical polygon fixed throughout in [Wat05]. This would at least be in accordance
with the notation given previously in [Wat05, formula (11)]. Under this assumption, the
coefficients i(s)
n
given in [Wat05, formula (80)] have the wrong sign (compare them with
our formula above). Lastly, we want to remark that Watson uses two different definitions
for the coefficients i(s)
n
(compare formula (80) with (25) in [Wat05]) which do not coincide
and thus might be confusing at first sight.
Corollary 4.16. Let A = I0(M/Dk) be the formal series as defined in Corollary 4.13
(recall M = S2(r)), and let κ = 1
r2 as before. Then
A =
1
4πt
∞
∑
ν=0
aν(M)
2k
tν =
1
4πt ⋅1
2k∣S2(r)∣
∞
∑
ν=0
iS
ν−1κνtν
=
1
4πt ⋅1
2k∣S2(r)∣
∞
∑
ν=0
ν
∑
ℓ=0
1
4ν−ℓ(ν −ℓ)!
(−1)ℓ
ℓ!
B2ℓ(1
2) ⋅κν ⋅tν.
(4.22)
In particular, we have for all ν ∈N0
aν(M) = ∫
M
ν
∑
ℓ=0
1
4ν−ℓ(ν −ℓ)!
(−1)ℓ
ℓ!
B2ℓ(1
2) ⋅κνdx.
(4.23)
The last formula for the coefficient aν(M) is universal in the sense that the heat coefficients
for any two-dimensional closed Riemannian manifold M of constant Gaussian curvature
κ are given by that formula.
Proof. Recall that the aν(M) are given by ZM(t)
t↓0∼
1
4πt ∑∞
ν=0 aν(M)tν. Comparing this
with (4.16), one easily gets the formulas (4.22) for A and (4.23) for aν(M) from ∣S2(r)∣= 4π
κ
and by substituting the coefficients iν−1, i(s)
ℓ
from (4.17), (4.18).
In general, for any ν ∈N0 there exists a universal polynomial in the Gaussian curvature
and its covariant derivatives such that the heat invariant aν(M) for any two-dimensional
133


---

4 Spectral invariants for orbisurfaces
closed Riemannian manifold M is given as the integral of that polynomial over M (see
e.g. [BG90]). More precisely, that polynomial is a so-called curvature invariant of order
2ν. The covariant derivatives of the Gaussian curvature vanish if the Gaussian curvature
is constant. So in this case, the polynomial is just a monomial of the form ανκν, and
since it is universal, the case of M = S2(r) tells us that αν equals iS
ν−1. Thus the formula
(4.23) must hold for any two-dimensional Riemannian manifold of constant curvature
κ.
The next result from [Wat05] which we will need, and prove here with minor corrections,
is the following:
Proposition 4.17. Let k ∈N (we allow k = 1 in this proposition). As before, let Ω⊂S2(r)
be a lune with angle π
k, and write κ = 1
r2. Then
ZΩ(t)
t↓0∼
1
2k ⋅
1
κ ⋅t −
√π
4√κ ⋅1
√
t
+
∞
∑
ν=0
{ 1
2k ⋅iS
ν −
1
4ν+1(ν + 1)! ⋅
√π ⋅√κ
4
√
t
+2 ⋅
ν
∑
ℓ=0
1
4ℓ⋅ℓ! ⋅cS
ν−ℓ(π
k )}κνtν,
(4.24)
where iS
ν is defined as in the previous proposition and
cS
ℓ(π
k ) = 1
4k ⋅(−1)ℓ
(ℓ+ 1)! ⋅
1
2ℓ+ 1
ℓ+1
∑
j=0
(2ℓ+ 2
2j )(k2j −1)B2jB2ℓ+2−2j (1
2)
(4.25)
(recall cS
ℓ(γ) from the Remark after Corollary 3.30).
Proof. As in the proof of the previous proposition we first focus on the case r = 1.
The eigenvalues for a lune with arbitrary angle are known (see [Gro66]). For our lune
Ωwith angle π
k, the set of eigenvalues is given by
{λn,m ⋅(λn,m + 1) ∣m ∈N, n ∈N0 },
where λn,m ∶= k ⋅m + n. Furthermore, each eigenvalue is simple, i.e. has multiplicity one.
Thus we get for the heat trace of the lune:
ZΩ(t) =
∞
∑
m=1
∞
∑
n=0
e−(k⋅m+n)(k⋅m+n+1) t =
∞
∑
m=1
∞
∑
n=0
e−((k⋅m+n)2+(k⋅m+n)+ 1
4 −1
4 ) t
= e
t
4 ⋅
∞
∑
m=1
∞
∑
n=0
e−(k⋅m+n+ 1
2 )2 t
= e
t
4 ⋅(
∞
∑
m=0
∞
∑
n=0
e−(k⋅m+n+ 1
2 )2 t −
∞
∑
n=0
e−(n+ 1
2 )2 t)
´¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¸¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¹¶
= ∶Z−1/4
Ω
(t)
The asymptotic expansion of Z−1/4
Ω
(t) can be found in [Wat05, Lemma 15], and is given
134


---

4 Spectral invariants for orbisurfaces
by
Z−1/4
Ω
(t)
t↓0∼π
k ⋅1
2πt −
√π
4
√
t
+
∞
∑
ℓ=0
(2 ⋅cS
ℓ(π
k ) + 1
2ki(s)
ℓ) ⋅tℓ
(4.26)
where i(s)
ℓ
= (−1)ℓ+1 ⋅
B2ℓ+2( 1
2 )
(ℓ+1)!
as in (4.18). Multiplying by the series e
t
4, we get
ZΩ(t)
t↓0∼
1
2k ⋅1
t −
√π
4 ⋅1
√
t
+
∞
∑
ν=0
{−
1
4ν+1(ν + 1)! ⋅
√π
4
√
t
+2
ν
∑
ℓ=0
1
4ℓ⋅ℓ! ⋅cS
ν−ℓ(π
k ) + 1
2k
ν+1
∑
ℓ=0
1
4ℓ⋅ℓ!i(s)
ν−ℓ}tν.
By definition of iS
ν given in (4.17), this simplifies to
ZΩ(t)
t↓0∼
1
2k ⋅1
t −
√π
4 ⋅1
√
t
+
∞
∑
ν=0
{ 1
2k ⋅iS
ν −
1
4ν+1(ν + 1)! ⋅
√π
4
√
t
+2
ν
∑
ℓ=0
1
4ℓ⋅ℓ! ⋅cS
ν−ℓ(π
k )}tν.
(4.27)
Hence the proposition is proven for r = 1.
To get the asymptotic expansion for arbitrary r > 0, proceed as usual, replacing t by
t
r2 = κt.
Remark. The asymptotic expansion (4.26) is stated and proven in [Wat05, Lemma 15].
The statement of Lemma 15 is correct and the proof is basically correct as well. The
only issue occurs implicitly in the last step of the proof, where Watson uses Part (iii) of
his Lemma 11. The problem with Lemma 11 is that Watson does not explain explicitly
his definition for the coefficients B(2)
2n (x ∣a) and does not really prove part (i), (iii) of
that Lemma. From his proof of part (ii) of Lemma 11 and the usage of the coefficients
B(2)
2n (x ∣a) in the sequel of his article it seems as if he defines B(2)
2n (x ∣a) ∶= B(2)
2n (x ∣a ⋅1)
in the sense of formula (20) of his article. With this definition, the formulas of part (i)
and (iii) of Lemma 11 are wrong. However, Watson uses part (iii) of Lemma 11 only for
the special case x = 1
2, where because of B2n−1 ( 1
2) = 0 it simplifies to
B(2)
2n (1
2 ∣a ⋅1) =
n
∑
j=0
(2n
2j)(a2j −1)B2jB2n−2j (1
2) −(2n −1)B2n (1
2),
for all n ∈N, a > 0. One can show that this formula is indeed correct.
From Proposition 4.17 we can deduce formulas for the heat coefficients for any smooth
manifold of constant curvature and smooth totally geodesic boundary.
Corollary 4.18. Let S be any compact two-dimensional Riemannian manifold of constant
curvature with totally geodesic boundary ∂S. Let KS be the (Dirichlet) heat kernel and
135


---

4 Spectral invariants for orbisurfaces
KN
S be the Neumann heat kernel of S. Then the heat invariants are given by the following
formulas
ZS(t) = ∫
M
KS(x,x;t)dx
t↓0∼
1
4πt
∞
∑
ν=0
(aν(S) −βν(S) ⋅
√
4πt)tν,
(4.28)
ZN
S (t) ∶= ∫
M
KN
S (x,x;t)dx
t↓0∼
1
4πt
∞
∑
ν=0
(aν(S) + βν(S) ⋅
√
4πt)tν,
(4.29)
where aν(S) is defined as in (4.23) (with M replaced by S) and
βν(S) ∶= ∫
∂S
1
4ν+1ν!κνdx.
(4.30)
Proof. Suppose S ⊂S2(r) is a hemisphere (a spherical lune with angle π). This lune is
an example of a compact two-dimensional Riemannian manifold of constant curvature
with a totally geodesic boundary. When we set k = 1 in Proposition 4.17 we immediately
obtain (4.28) for the hemisphere (observe that for k = 1 the coefficients in (4.25) vanish:
cS
ℓ(π) = 0).
The asymptotic expansion (4.29) for the hemisphere follows easily from (4.28), since
the Dirichlet and Neumann heat kernels can be written as:
KS(x,y;t) = KS2(r)(x,y;t) −KS2(r)(x,σ(y);t),
KN
S (x,y;t) = KS2(r)(x,y;t) + KS2(r)(x,σ(y);t)
for all x,y ∈S and t > 0, where σ denotes the reflection in the boundary ∂S; so ZS(t) +
ZN
S (t) = 2ZS2(r)(t)
t↓0∼
1
4πt ∑∞
ν=0 2aν(S)tν.
By a similar argument as in the proof of Corollary 4.16, the formulas for aν(S),βν(S)
now follow for all two-dimensional compact manifolds of constant curvature with totally
geodesic boundary because of [BG90].
Of course, the asymptotic expansion (4.28) coincides with the asymptotic expansion
given in (3.111) for polygons with zero vertices.
Let us resume our discussion of the orbifolds. We now have two expressions for the
asymptotic expansion of ZΩ(t) given by (4.24) and (4.14). The coefficients corresponding
to the same power of t must be equal in both asymptotic expansions. Recall that from
(4.14) we have
ZΩ(t)
t↓0∼A −B + C,
and (4.24) can be written in the form
ZΩ(t)
t↓0∼A −
1
√
4πt
⋅
∞
∑
ν=0
2π
√κ ⋅
κν
4ν+1ν!tν +
∞
∑
ν=0
ν
∑
ℓ=0
2
4ℓ⋅ℓ! ⋅cS
ν−ℓ(π
k )κνtν.
136


---

4 Spectral invariants for orbisurfaces
Since B contains only half-integer powers and C only integer powers, we conclude the
following formulas for B and C:
Corollary 4.19. Let B,C be defined as in Corollary 4.13. Then:
(i)
B =
1
√
4πt
⋅
∞
∑
ν=0
2πr
4ν+1ν!κν ⋅tν = ∣ml∣
√
4πt
⋅
∞
∑
ν=0
1
4ν+1ν!κν ⋅tν,
(4.31)
where ∣ml∣denotes the length of the mirror locus; in particular,
bν ( ˜S0) =
2
4ν+1 ⋅ν! ⋅κν for all ν ∈N0.
(4.32)
(ii)
C =
∞
∑
ν=0
ν
∑
ℓ=0
2
4ℓ⋅ℓ! ⋅cS
ν−ℓ(π
k )κνtν
(4.33)
with cS
ℓ( π
k) from (4.25); in particular,
1
k
k−1
∑
ℓ=1
bν ( ˜Dℓ) =
ν
∑
ℓ=0
2
4ℓ⋅ℓ! ⋅cS
ν−ℓ(π
k )κν for all ν ∈N0.
(4.34)
Recall that the orbifolds M/Zk and M/Dk have the asymptotic expansions
ZM/Zk(t)
t↓0∼2A + 2C;
ZM/Dk(t)
t↓0∼A + B + C.
Together with the formulas for A,B,C from the above corollary and Corollary 4.16, this
completes our discussion of the heat invariants for the spherical orbifolds M/Zk and
M/Dk.
The computations made so far can be generalised to more general orbisurfaces. The
reason is that there exist only three kinds of singular points for two-dimensional orbifolds,
which we have already met in the discussion so far. These are: mirror points, cone points
and dihedral points (see [Gor12]). Recall from [DGGW08, Theorem 4.8] (see Theorem
4.11 above) that for each two-dimensional closed Riemannian orbifold O, the heat trace
ZO(t) has an asymptotic expansion, as t ↘0, of the form
1
4πt
∞
∑
ν=0
aν(O)tν +
∑
N∈S(O)
IN(O)
∣Iso(N)∣.
Theorem 4.20. Let O be a two-dimensional closed Riemannian orbifold of constant
curvature κ ∈R. Then, with C as in (4.33) we have:
137


---

4 Spectral invariants for orbisurfaces
(i)
aν(O) = vol(O)
ν! ⋅4ν
ν
∑
ℓ=0
(ν
ℓ)(−4)ℓB2ℓ(1
2) ⋅κν for all ν ∈N0.
(4.35)
(ii) If N consists of a cone point of order k ∈N, then
IN(O)
∣Iso(N)∣= C.
(iii) If N consists of a dihedral point of order 2k ∈N, then
IN(O)
∣Iso(N)∣= 1
2C.
(iv) If N is a mirror edge of length ∣N∣, then
IN(O)
∣Iso(N)∣=
∣N∣
√
4πt
∞
∑
ν=0
1
4ν+1 ⋅ν! ⋅κν ⋅tν.
(4.36)
Proof. Part (i) is clear from Corollary 4.16 since aν(O) is the integral over O of the same
curvature invariant as for manifolds. The remaining statements follow from Corollary 4.19
(and the definition of C as the contribution of one of the cone points of M/Zk) via the
following fact; see [Don76, Theorem 5.1], cited also in [DGGW08]: The functions bi(γ,x),
whose integrals over N make up the coefficients in IN(O), are of the form ϕ(γ,x)⋅ψ(γ,x),
where ϕ(γ,x) only depends on the Euclidean isometry dγx and ψ(γ,x) is a universal
polynomial in the curvature tensor of O and its covariant derivatives.
Remark. Actually the results in (ii) −(iv) in the above theorem do not require the
whole orbifold to have constant curvature. It suffices that the curvature is constant in a
sufficiently small neighborhood of N. For example, if we consider a teardrop with cone
point of order k such that the curvature is constant in a neighborhood of the cone point,
then the contribution of that cone point is given by (ii) above.
4.3 Applications
In this section we first consider some applications of the heat invariants computed in
Section 4.2. Finally, we will use them to give an alternative proof for the formulas from
Theorem 3.32/Corollary 3.37 for the angle contributions in the special case of polygons
with angles of the form π
k with k ∈N.
Let O be a closed Riemannian orbisurface of constant curvature κ ∈R. There exists a
strong connection between the heat invariants for O computed in the previous section
and the heat invariants for a polygon furnished with the same curvature κ, which we
have computed in Section 3.3. We want to compare those coefficients. Recall the notation
introduced in Corollary 3.37 and Theorem 4.20. First of all, the formal series Vκ(γ)
for γ = π
k, k ∈N, is the same as the contribution of a dihedral point of order 2k to the
orbifold heat coefficients of O. In other words, we have Vκ(γ) = 1
2C, where C is as in
(4.33). Consequently, a cone point of order k contributes to the heat invariants of O as
much as two angles of magnitude π
k to the heat invariants for a polygon of curvature κ.
138


---

4 Spectral invariants for orbisurfaces
Lastly, the mirror locus of O contributes the negative of the contribution of the boundary
of a polygon, provided their lengths are equal.
Therefore we obtain, just as in Corollary 3.38 and Theorem 3.40, the following spectral
invariants:
Corollary 4.21. Let O be a closed orbisurface of constant curvature κ ∈R. Let M ∈N0
denote the number of dihedral points of O and let 2m1,...,2mM denote their individual
orders, where m1,...,mM ∈N. Similarly, let N ∈N0 denote the number of cone points and
n1,...,nN ∈N their orders. Then:
(i) The volume of O and the length of the mirror locus are spectral invariants.
(ii) If the mirror locus is non-trivial, i.e. the length of the mirror locus is positive, then
the curvature of the orbifold is determined by the spectrum.
(iii) If κ ≠0, then κ together with the spectrum determines the number M + 2N as well
as the multiset {m1,...,mM,n1,n1,n2,n2,...,nN,nN}.
(iv) If the mirror locus is trivial and κ ≠0, then κ together with the spectrum determines
the number of cone points as well as the multiset of all orders {n1,...,nN}. (Note
that trivial mirror locus implies absence of dihedral points.)
To the best of our knowledge, statement (iii) is a new result. Similarly, statement (iv)
is also new in this generality and was only known for the special case of κ = −1 (see the
comments after Corollary 4.23 below).
As usual, we call two orbifolds isospectral if their Laplacians have the same spectrum,
including multiplicities. Corollary 4.21 has some interesting consequences for isospectral
orbisurfaces, which we now want to demonstrate.
Definition 4.22. (see [Thu80, p. 311]) Suppose O is a closed orbisurface. Let XO be the
underlying topological space of O, and let χ(XO) denote its Euler characteristic. Then,
using the notation of Corollary 4.21, the Euler characteristic of O is defined as
χ(O) ∶= χ(XO) −1
2
M
∑
i=1
(1 −1
mi
) −
N
∑
i=1
(1 −1
ni
).
(4.37)
Thus the Euler characteristic of an orbifold depends on the Euler characteristic of the
underlying space and the orders of all its dihedral and cone points. Note that we use
the term order always in the sense of isotropy order of a point. Instead, W. Thurston
defines the order of a dihedral point as half of its isotropy order (see [Thu80, Proposition
13.3.1]).
It is well-known that the Euler characteristic of a closed orbisurface O is related to its
curvature κ by the Gauß-Bonnet theorem exactly as for closed manifolds, i.e.
∫
O
κdA = 2πχ(O).
(4.38)
139


---

4 Spectral invariants for orbisurfaces
If the curvature is constant then the Gauß-Bonnet formula reduces to the equation
vol(O)κ = 2πχ(O). As we see, it follows from Corollary 4.21 (i) that two isospectral
orbisurfaces have the same curvature if and only if they have the same Euler characteristic.
Corollary 4.23. Let O be a closed orientable orbisurface with constant curvature κ ≠0.
Then κ together with the spectrum of O determines the Euler characteristic of O as well
as the Euler characteristic of the underlying space XO.
Proof. By assumption, we know the value of κ. Thus by Corollary 4.21 (i) and the
Gauß-Bonnet formula, the spectrum determines the Euler characteristic χ(O).
Furthermore, since the orbisurface O is orientable, its mirror locus is trivial and all
singular points are cone points. Thus, by Corollary 4.21 (iv), we can deduce from the
spectrum the total number of all cone points as well as the multiset of all their orders.
Therefore the spectrum determines the Euler characteristic of the underlying space
through (4.37).
It is well-known that the underlying space of an orbisurface is always a topological
surface, possibly with boundary (see [Thu80]). Further, this underlying topological surface
has to be orientable and without boundary if the orbifold is known to be orientable. Hence,
Corollary 4.23 implies that if two closed orientable orbisurfaces of constant curvature
κ ≠0 are isospectral, then they have the same underlying topological space, i.e. the
underlying topological spaces are homeomorphic. This fact was previously known in the
special case of closed orientable orbisurfaces of constant curvature κ = −1 (see [DS09,
Proposition 3.3]). In their article [DS09], E. Dryden and A. Strohmaier generalise Huber’s
theorem to orientable orbisurfaces of constant curvature κ = −1, using the Selberg trace
formula for the wave kernel, from which, in particular, the statement of Corollary 4.21
(iv) follows. Then they use this result with Weyl’s asymptotic formula in order to obtain
Corollary 4.23 for κ = −1. Thus, Corollary 4.23 is a new proof of [DS09, Proposition 3.3]
using only heat invariants, in addition to being a generalisation of it.
Suppose now that the mirror locus of the orbisurface O is not trivial. Then by Corollary
4.21 (i),(ii) and the Gauss-Bonnet theorem, the Euler characteristic χ(O) is determined
by the spectrum. Furthermore, if two isospectral closed orbisurfaces with non-empty
mirror locus are given, then Corollary 4.21 (i),(iii) provide some restrictions on the
singular sets. Unfortunately it is not possible in general to detect which elements of the
multiset in Corollary 4.21 (iii) correspond to dihedral points and which to cone points.
The simplest classes of orbifolds for which the multiset of orders can be used to obtain
all information about the orbifold are the following.
Corollary 4.24. Let Dκ, Cκ denote the set of all orbisurfaces with constant curvature
κ ≠0 and without any cone point, respectively dihedral point. Within each of these classes
the spectrum determines χ(O), χ(XO), and the singular set of the orbifold; that is, the
length of the mirror locus and the total number of dihedral points together with their
orders, respectively the total number of cone points with all orders.
Proof. This follows easily from Corollary 4.21. Note that within each class the numbers
in the multiset given in Corollary 4.21 (iii) correspond by assumption solely to dihedral
140


---

4 Spectral invariants for orbisurfaces
points, respectively solely to cone points. Thus all information about the singular set
and the topology of the orbifold can be deduced from the spectrum as claimed.
What happens if we consider orbisurfaces with dihedral as well as cone points? Some-
times a partial answer about the singular set is possible. For example, a cone point always
contributes its order twice to this multiset. Thus, if a number in the multiset appears
only once, then we know it must come from a dihedral point. More generally, we can
prove the following result.
Corollary 4.25. Let A1 denote the class of all orbisurfaces with constant nonzero
curvature which have at least one dihedral point and at least one cone point and satisfy
the following condition: Any two dihedral points, respectively any two cone points, have
different orders. Then within A1, the spectrum again determines χ(O), χ(XO), the length
of the mirror locus, the number of dihedral points with their order, and the number of
cone points with their orders.
Proof. Since O ∈A1 has a dihedral point, it must have non-trivial mirror locus. Thus
by Corollary 4.21 (ii) the value of the curvature is determined and therefore, by the
Gauss-Bonnet theorem, χ(O) is also determined.
Since each dihedral point has a unique order among all dihedral points and similarly,
each cone point has a unique order among all cone points, we can detect which elements
in the multiset in Corollary 4.21 (iii) come from dihedral points and which from cone
points. Consequently we can detect the number of dihedral points with orders as well as
the number of cone points with orders. Thus, χ(XO) can be computed by (4.37).
In [DGGW08, Proposition 5.22] the authors show that within the class of orbisurfaces
of constant curvature κ > 0 the spectrum determines the orbifold. They prove this result
by comparing the first few heat invariants of each such orbisurface (see [DGGW08, Table
1]). Most of those orbisurfaces can easily be distinguished through Corollary 4.21 (iii) and
taking into account whether the mirror loci are trivial or not. In fact, all but three pairs
of orbisurfaces can be distinguished this way, namely (in the notation of [DGGW08]):
O(∗m,m) and O(m,∗); O(∗2,2,m) and O(2,∗m); O(∗2,3,3) and O(3,∗2). In those
remaining pairs, in which the orbifolds have the same multiset as well as non-trivial
mirror loci, the orbifolds can be distinguished by comparing the length of the mirror loci
as it is said in the proof of [DGGW08, Proposition 5.22].
One can restrict the class of orbifolds in different ways in order to obtain further results.
For example, if one fixes the curvature κ ≠0 and the value of M + N, where M and N
are defined as in Corollary 4.21, then the spectrum determines the value of M as well
as N (note that M,N can be deduced from the values M + N and M + 2N, where the
latter is determined by the spectrum).
Recall that an angle γ = π
k, k ∈N, contributes to the heat invariants of a polygon as
much as a dihedral point of order 2k contributes to the orbifold heat coefficients, provided
the curvature of the polygon and the orbifold are constant and equal. In other words,
Vκ ( π
k) = 1
2C. In the remaining part of this section we will give an alternative proof for
the equation Vκ( π
k) = 1
2C for κ < 0 by using the formulas in [Wat05] and orbifold theory
(more precisely Theorem 4.20 and the Remark after that theorem).
141


---

4 Spectral invariants for orbisurfaces
Lemma 4.26. Let S2 ⊂R3 be the standard sphere, let xN ∶= (0,0,1), and let κ ∈R. Then
there exists a Riemannian metric g on S2 which is O(2)-invariant and has constant
curvature κ in a neighborhood of xN. (Of course, this lemma is trivial for κ > 0.)
Proof. Let (H,h) be a two-dimensional complete Riemannian manifold of constant
curvature κ, let P ∈H, and let gS2 be the standard metric on S2. We choose R ∈(0,π)
smaller than the injectivity radius of H at P. Choose a (linear) Euclidean isometry from
TxNS2 to TPH, and let ϕ ∶BR(xN) →BR(P) be the corresponding diffeomorphism given
by the geodesic exponential maps. Let f ∶S2 →[0,1] be a smooth O(2)-invariant function
such that f∣B R
2
(xN) ≡1 and f vanishes outside BR(xN). Then g ∶= f ⋅ϕ∗h + (1 −f)gS2 has
the desired properties.
Note that the results of Section 4.1 hold for (S2,g), if g denotes a Riemannian metric
as in Lemma 4.26.
Theorem 4.27. Let (N,h) be a two-dimensional complete Riemannian manifold whose
Gaussian curvature is bounded. Let Ω⊂N be a polygon which has an angle γ ∶= π
k
at some vertex P of Ω, where k ∈N. Let Wγ(P) denote the wedge corresponding to
the angle γ and suppose that the curvature is constant and equal to κ ∈R in some
neighborhood of P. Let g be a Riemannian metric on S2 as in Lemma 4.26. Suppose ˜R > 0
is such that (B ˜R(P),h) and (B ˜R(xN),g) have constant curvature and are isometric,
where xN = (0,0,1). Further, let i(P) be the injectivity radius of N at P and let i(xN)
denote the injectivity radius of (S2,g) at xN. For any r ∈(0,i(P)] let Wr(P) denote the
circle sector at P with angle γ and radius r, such that Wr(P) ⊂Wγ(P). Then for all
R > 0 such that R < 1
2 ⋅min{i(P),i(xN), ˜R} and such that W2R(P)∩Ωis a disjoint union
of circle sectors at P, the functions
t ↦
∫
WR(P)
KΩ(x,x;t)dx
and
t ↦
∫
BR(πZk(xN))
K(M/Zk,g)(x,x;t)dx −
∫
BR(πDk(xN))
K(M/Dk,g)(x,x;t)dx
have the same asymptotic expansion as t ↘0.
Proof. First, when Lemma 3.36 (ii) is applied to N, it follows that the function
t ↦∫WR(P) KΩ(x,x;t)dx
has the same asymptotic expansion as the function
t ↦∫WR(P) KW2R(P)(x,x;t)dx.
142


---

4 Spectral invariants for orbisurfaces
By assumption, B2R(P) and B2R(xN) are isometric and thus we identify B2R(P) with
B2R(xN) (and accordingly the subsets WR(P) and W2R(P)). Let Ω′ ⊂(S2,g) denote a
2-gon as in Section 4.1 with vertex xN and angle π
k such that WR(P) ⊂Ω′. Hence, by
Lemma 3.36 (ii) (applied to (S2,g)) the function t ↦∫WR(P) KW2R(P)(x,x;t)dx has the
same asymptotic expansion as
t ↦∫WR(xN) KΩ′(x,x;t)dx.
Note that WR(xN) = BR(xN)∩Ω′ and thus by Theorem 4.10 with U ∶= BR(xN) the proof is
complete. Note that πZk(BR(xN)) = BR(πZk(xN)) and πDk(BR(xN)) = BR(πDk(xN)).
Lemma 4.28. Let O be a two-dimensional closed Riemannian orbifold, Q ∈O be a cone
point or dihedral point. Suppose there exists some R > 0 such that BR(Q) has constant
curvature κ, and BR(Q) does not contain any singular points except for Q and, if Q is a
dihedral point, mirror points of the two reflector edges which end at Q.
(i) If Q is a cone point of order k, then
∫
BR(Q)
KO(x,x;t)dx
t↓0∼
1
4πt
∞
∑
ν=0
aν(BR(Q))tν + C,
where aν is defined as in (4.35) and C as in (4.33).
(ii) If Q is a dihedral point of order 2k, then
∫
BR(Q)
KO(x,x;t)dx
t↓0∼
1
4πt
∞
∑
ν=0
aν(BR(Q))tν +
2R
√
4πt
∞
∑
ν=0
1
4ν+1ν!κνtν + 1
2C.
Proof. The proof follows directly from Theorem 4.20 and the Remark given after that
theorem, if one takes into account the following: In order to obtain the asymptotic
expansion of ZO(t) in [DGGW08, Theorem 4.8], the authors consider the function
x ↦KO(x,x;t) in local orbifold charts (so called “distinguished” charts) and compute
locally the heat kernel asymptotic expansion as t ↘0. The resulting coefficients only
depend on the local geometry and are put together by a partition of unity and then
integrated. Hence, the asymptotic expansion of ∫U KO(x,x;t)dx captures exactly the
contribution of the points (to the integrals which occur in I0 and IN), which are contained
in any open cover of U, i.e. exactly the points of U.
From Theorem 4.27 and Lemma 4.28 we obtain immediately the following corollary.
Corollary 4.29. Let (N,h) be a complete Riemannian manifold whose Gaussian curva-
ture is bounded. Let Ω⊂N be a polygon which has an angle γ ∶= π
k at some vertex P of
Ω, where k ∈N. Let Wr(P) be as in Theorem 4.27 and suppose the Gaussian curvature
is constant in some neighborhood of P. Then there exists some R0 > 0 such that for all
143


---

4 Spectral invariants for orbisurfaces
R ∈(0,R0):
∫
WR(P)
KΩ(x,x;t)dx
t↓0∼
1
4πt
∞
∑
ν=0
aν(WR(P))tν −
2R
√
4πt
∞
∑
ν=0
1
4ν+1ν!κνtν + 1
2C.
Remark. The formula (4.33) for C contains the coefficients cS
ℓ( π
k), which were computed
by S. Watson in [Wat05]. Furthermore, that formula for C was derived using only orbifold
theory. Thus, we obtain from the above corollary (which is based on Theorem 4.27) and
the formula of S. Watson for cS
ℓ( π
k) a new proof of the formula for Vκ ( π
k) (which is given
in Corollary 3.37), in particular for κ = −1 (and for the coefficients cH
ℓ( π
k)).
144


---

Bibliography
[Bar08] E. W. Barnes. On generalized Legendre functions. Quart. J. Math. Oxford
Ser., 39:pp. 97–204, 1908.
[BB62] P. B. Bailey and F. H. Brownell. Removal of the log factor in the asymptotic
estimates of polygonal membrane eigenvalues. J. Math. Anal. Appl., 4:pp.
212–239, 1962.
[BCDS94] P. Buser, J. Conway, P. Doyle, and K.-D. Semmler. Some planar isospectral
domains. Internat. Math. Res. Notices, (9):pp. 391–400, 1994.
[BG90] T. P. Branson and P. B. Gilkey. The asymptotics of the Laplacian on a
manifold with boundary. Comm. Partial Differential Equations, 15(2):pp.
245–272, 1990.
[BH86] N. Bleistein and R. A. Handelsman. Asymptotic expansions of integrals.
Dover Puclications, Inc., New York, 1986.
[BP11] C. Bär and F. Pfäffle. Wiener measures on Riemannian manifolds and the
Feynman-Kac formula. Mat. Contemp., 40:pp. 37–90, 2011.
[Bro57] F. H. Brownell. Improved error estimates for the asymptotic eigenvalue
distribution of the membrane problem for polygonal boundaries. Bull. Amer.
Math. Soc., 63:p. 284, 1957.
[Bus92] P. Buser. Geometry and spectra of compact Riemann surfaces, volume 106
of Progress in Mathematics. Birkhäuser, Boston, 1992.
[BY02] B. C. Berndt and B. P. Yaep. Explicit evaluations and reciprocity theorems
for finite trigonometric sums. Adv. in Appl. Math., 29:pp. 358–385, 2002.
[CH53] R. Courant and D. Hilbert. Methods of mathematical physics, volume I.
Interscience Publishers, Inc., New York, 1953.
[Cha84] I. Chavel. Eigenvalues in Riemannian geometry, volume 115 of Pure and
Applied Mathematics. Academic Press Inc., Orlando, 1984.
[Cha95] S. J. Chapman. Drums that sound the same. Amer. Math. Monthly, 102(2):pp.
124–138, 1995.
145


---

Bibliography
[Cha06] I. Chavel. Riemannian geometry, volume 98 of Cambridge Studies in Ad-
vanced Mathematics. Cambridge University Press, Cambridge, 2nd edition,
2006.
[CLY81] S. Y. Cheng, P. Li, and S.-T. Yau. On the upper estimate of the heat kernel
of a complete Riemannian manifold. Amer. J. Math., 103(5):pp. 1021–1063,
1981.
[CM99] W. Chu and A. Marini. Partial fractions and trigonometric identities. Adv.
in Appl. Math., 23:pp. 115–175, 1999.
[CPR01] M. Craioveanu, M. Puta, and T. M. Rassias. Old and new aspects in spectral
geometry, volume 534 of Mathematics and its Applications. Kluwer Academic
Publishers, Dordrecht, 2001.
[Dav02] B. Davies. Integral transforms and their applications, volume 41 of Texts in
Applied Mathematics. Springer-Verlag, New York, 3rd edition, 2002.
[DGGW08] E. B. Dryden, C. Gordon, S. J. Greenwald, and D. L. Webb. Asymptotic
expansion of the heat kernel for orbifolds. Michigan Math. J., 56(1):pp.
205–238, 2008.
[Dod83] J. Dodziuk. Maximum principle for parabolic inequalities and the heat flow
on open manifolds. Indiana Univ. Math. J., 32(5):pp. 703–716, 1983.
[Doe50] Gustav Doetsch.
Handbuch der Laplace-Transformationen Band I, vol-
ume 14 of Lehrbücher und Monographien aus dem Gebiete der exakten
Wissenschaften. Springer Basel AG, Basel, 1950.
[Don76] H. Donnelly. Spectrum and the fixed point sets of isometries. I. Math. Ann.,
224:pp. 161–170, 1976.
[Don79] H. Donnelly. Asymptotic expansions for the compact quotients of properly
discontinuous group actions. Illinois J. Math., 23(3):pp. 485–496, 1979.
[DS09] E. B. Dryden and A. Strohmaier. Huber’s theorem for hyperbolic orbisurfaces.
Canad. Math. Bull., 52(1):pp. 66–71, 2009.
[Dur88] C. Durso. On the inverse spectral problem for polygonal domains. PhD thesis,
Massachusetts Institute of Technology, 1988.
[Els09] J. Elstrodt. Maß- und Integrationstheorie. Springer-Verlag, Berlin, 6th
corrected edition, 2009.
[EMOT53] A. Erdélyi, W. Magnus, F. Oberhettinger, and F. G. Tricomi.
Higher
transcendental functions, volume I. McGraw-Hill Book Company, Inc., New
York, 1953.
146


---

Bibliography
[Fed63] B. V. Fedosov. Asymptotic formulas for the eigenvalues of the Laplacian in
the case of a polygonal region. Soviet Math. Dokl, 4:pp. 1092–1096, 1963.
[GM13] D. Grieser and S. Maronna. Hearing the shape of a triangle. Notices Amer.
Math. Soc., 60(11):pp. 1440–1447, 2013.
[Gor12] C. Gordon. Orbifolds and their spectra. In Spectral Geometry, volume 84 of
Proc. of Sympos. Pure Math., pages 49–71. Amer. Math. Soc., 2012.
[Göt65] F. Götze. Verallgemeinerung einer Integraltransformation von Mehler-Fock
durch den von Kuipers und Meulenbeld eingeführten Kern P m,n
k
(z). Proc.
Knkl. Nederl. Akad. Weten. A. = Indagationes Mathematicae (Proceedings),
68:pp. 396–404, 1965.
[GR07] I. S. Gradshteyn and I. M. Ryzhik. Table of integrals, series and products.
Elsevier/Academic Press Inc., Amsterdam, seventh edition, 2007.
[Gri97] A. Grigor’yan. Gaussian upper bounds for the heat kernel on arbitrary
manifolds. J. Differential Geometry, 45:pp. 33–52, 1997.
[Gri99] A. Grigor’yan. Estimates of heat kernels on Riemannian manifolds. In
Spectral theory and geometry: ICMS instructional conference, Edinburgh
1998, volume 273 of London Math. Soc. Lecture Note Ser., pages 140–225.
Cambridge Univ. Press, Cambridge, 1999.
[Gri06] A. Grigor’yan. Heat kernels on weighted manifolds and applications. In
The ubiquitous heat kernel, volume 398 of Contemp. Math., pages 93–191.
American Mathematical Society, 2006.
[Gri09] A. Grigor’yan. Heat kernel and analysis on manifolds, volume 47 of AMS/IP
Studies in Advanced Mathematics. American Mathematical Society, Provi-
dence; International Press, Boston, 2009.
[Gro66] D. Gromes. Über die asymptotische Verteilung der Eigenwerte des Laplace-
Operators für Gebiete auf der Kugeloberfläche.
Math. Zeitschr., 94:pp.
110–121, 1966.
[GW94] C. Gordon and D. Webb. Isospectral convex domains in the hyperbolic plane.
Proc. Amer. Math. Soc., 120(3):pp. 981–983, 1994.
[GWW92] C. Gordon, D. Webb, and S. Wolpert. Isospectral plane domains and surfaces
via Riemannian orbifolds. Invent. Math., 110:pp. 1–22, 1992.
[Hob65] E. W. Hobson. The Theory of Spherical and Ellipsoidal Harmonics. Chelsea
Publishing Company, New York, 1965.
[Hsu95] E. P. Hsu. On the principle of not feeling the boundary for diffusion processes.
J. London Math. Soc., 51(2):pp. 373–382, 1995.
147


---

Bibliography
[Hsu02] E. P. Hsu. Stochastic analysis on manifolds, volume 38 of Graduate Studies
in Mathematics. American Mathematical Society, 2002.
[Kac66] M. Kac. Can one hear the shape of a drum? Amer. Math. Monthly, 73:pp.
1–23, 1966.
[Kli78] W. Klingenberg. A course in differential geometry, volume 51 of Graduate
Texts in Mathematics. Springer-Verlag, New York, 1978.
[Kli95] W. Klingenberg. Riemannian geometry, volume 1 of De Gruyter Studies in
Mathematics. Walter de Gruyter & Co., Berlin, 2nd revised edition, 1995.
[Leb65] N. N. Lebedev. Special functions and their applications. Revised English
edition. Translated and Edited by Richard A. Silverman. Prentice-Hall, Inc.,
Englewood Cliffs, N.J., 1965.
[Lee13] J. M. Lee. Introduction to smooth manifolds, volume 218 of Graduate Texts
in Mathematics. Springer, New York, 2nd edition, 2013.
[Low64] J. S. Lowndes. Note on the generalized Mehler transform. Proc. Camb. Phil.
Soc., 60:pp. 57–59, 1964.
[LR15] Z. Lu and J. Rowlett. The sound of symmetry. Amer. Math. Monthly, 122:pp.
815–835, 2015.
[LR16] Z. Lu and J. Rowlett. One can hear the corners of a drum. Bull. Lond.
Math. Soc., 48:pp. 85–93, 2016.
[Luk69] Y. L. Luke.
The special functions and their approximations, volume I.
Academic Press, Inc., New York, 1969.
[MR15] R. Mazzeo and J. Rowlett. A heat trace anomaly on polygons. Math. Proc.
Camb. Phil. Soc., 159:pp. 303–319, 2015.
[MS67] H. P. McKean, Jr. and I. M. Singer. Curvature and the eigenvalues of the
Laplacian. J. Differential Geometry, 1:pp. 43–69, 1967.
[Mul28] H. P. Mulholland. An asymptotic expansion for ∑∞
0 (2n + 1)eσ(n+1/2)2. Proc.
Camb. Philos. Soc., 24:pp. 280–289, 1928.
[Nör24] N. E. Nörlund. Vorlesungen über Differenzenrechnung, volume 13 of Die
Grundlehren der mathematischen Wissenschaften in Einzeldarstellungen.
Verlag von Julius Springer, Berlin, 1924.
[OH61] F. Oberhettinger and T. P. Higgins. Tables of Lebedev, Mehler, and general-
ized Mehler transforms. Boeing scientific research laboratories, Mathematical
Note No. 246:pp. 1–48, 1961.
148


---

Bibliography
[OLBC10] F. W. J. Olver, D. W. Lozier, R. F. Boisvert, and C. W. Clark, editors.
NIST handbook of mathematical functions. U. S. Department of Commerce,
National Institute of Standards and Technology; Cambridge University Press,
Cambridge, 2010.
[Olv97] F. W. J. Olver. Asymptotics and special functions. A K Peters, Wellesley,
Massachusetts, 1997.
[PBM92] A. P. Prudnikov, Yu. A. Brychkov, and O. I. Marichev. Integrals and Series,
volume 5: Inverse Laplace transforms. Gordon and Breach Science Publishers,
New York, 1992.
[Pet06] P. Petersen. Riemannian geometry, volume 171 of Graduate Texts in Mathe-
matics. Springer, New York, 2nd edition, 2006.
[Por12] J. Porti. Hyperbolic polygons of minimal perimeter with given angles. Geom.
Dedicata, 156:pp. 165–170, 2012.
[Rob59] L. Robin. Fonctions sphériques de Legendre et fonctions sphéroïdales, volume
I-III. Gauthier-Villars, Paris, 1957-1959.
[Ros74] P. Rosenthal. On an inversion theorem for the general Mehler-Fock transform
pair. Pacific J. of Math., 52(2):pp. 539–545, 1974.
[Smi81] L. Smith. The asymptotics of the heat equation for a boundary value problem.
Invent. Math., 63:pp. 467–493, 1981.
[Sne72] I. N. Sneddon. The use of integral transforms. McGraw-Hill, New York,
1972.
[Sri88] S. Srisatkunarajah. On the asymptotics of the heat equation for polygonal
domains. PhD thesis, Heriot-Watt University, 1988. pp. 40-44.
[Szn98] A.-S. Sznitman. Brownian motion, obstacles and random media. Springer
Monographs in Mathematics. Springer-Verlag, Berlin, 1998.
[TE51] F. G. Tricomi and A. Erdélyi. The asymptotic expansion of a ration of
gamma functions. Pacific J. Math., 1:pp. 133–142, 1951.
[Tem96] N. M. Temme. Special functions: an introduction to the classical functions
of mathematical physics. John Wiley & Sons, Inc., New York, 1996.
[Thu80] W. Thurston. The geometry and topology of three-manifolds (chapter 13).
Lecture notes, http://msri.org/publications/books/gt3m/, 1980.
[vdBS88] M. van den Berg and S. Srisatkunarajah. Heat equation for a region in R2
with a polygonal boundary. J. London Math. Soc. (2), 37:pp. 119–127, 1988.
149


---

Bibliography
[VF01] N. Virchenko and I. Fedotova. Generalized associated Legendre functions
and their applications. World Scientific Publishing Co. Pte. Ltd., Singapore,
2001.
[Wat18] G. N. Watson. Asymptotic expansions of hypergeometric functions. Trans.
Cambridge Philos. Soc, 22:pp. 277–308, 1918.
[Wat05] S. Watson. The trace function expansion for spherical polygons. New Zealand
J. Math., 34:pp. 81–95, 2005.
[Wey11] H. Weyl. Ueber die asymptotische Verteilung der Eigenwerte. Nachrichten
von der Gesellschaft der Wissenschaften zu Göttingen, Mathematisch-
Physikalische Klasse, pages 110–117, 1911.
[Won01] R. Wong. Asymptotic approximations of integrals, volume 34 of Classics
in Applied Mathematics. Society for Industrial and Applied Mathematics
(SIAM), Philadelphia, 2001.
150


---

Selbständigkeitserklärung
Ich erkläre, dass ich die vorliegende Arbeit selbständig und nur unter Verwendung der
angegebenen Literatur und Hilfsmittel angefertigt habe.
Berlin, 26.05.2017
Eren Uçar
151
