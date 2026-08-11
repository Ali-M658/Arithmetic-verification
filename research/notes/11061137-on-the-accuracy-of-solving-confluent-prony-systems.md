---
title: '[1106.1137] On the accuracy of solving confluent Prony systems'
id: 11061137-on-the-accuracy-of-solving-confluent-prony-systems
tags:
- hyperbolic-pillow-heat-novelty-813161
- prony-method
- super-resolution
- vandermonde-conditioning
created: '2026-08-09T08:45:32.725921Z'
updated: '2026-08-09T09:36:32.294681Z'
source: https://arxiv.org/abs/1106.1137
source_domain: arxiv.org
fetched_at: '2026-08-09T08:45:32.725639Z'
fetch_provider: builtin
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Batenkov & Yomdin, ''On the accuracy of solving confluent Prony systems,''
  SIAM J. Applied Mathematics (per journal version) / arXiv:1106.1137v3 (math.CA),
  DOI 10.48550/arXiv.1106.1137. Full PDF read (14 pages: Secs 1-5). Studies the Prony
  system sum_i a_i xi_i^k = m_k, recovering nodes xi_i (locations) and magnitudes
  a_i from noisy power moments/measurements m_k + eps_k. Defines the ''Prony map''
  P_S and its Jacobian: Lemma 4.2 factors J_{P_S}(x) = U(xi_1,l_1+1,...,xi_K,l_K+1)
  . diag{D_1,...,D_K}, where U is the CONFLUENT VANDERMONDE MATRIX on the nodes --
  an explicit statement that the Vandermonde matrix is exactly the Jacobian of the
  power-sum-to-parameters map. Corollary 4.3: x is a CRITICAL POINT of the Prony map
  iff either two nodes collide (xi_i = xi_j) or a leading magnitude vanishes -- structurally
  identical to the manuscript''s Jacobian vanishing exactly on p=q, p=r, q=r. Theorem
  4.5 (main local stability result): the best-possible local accuracy of recovering
  a node xi_i is ACC_LOC(x,eps,xi_i) = C_1 * eps / |a_{i,l_i-1}|, where C_1 depends
  only on the node configuration xi_1,...,xi_K via the inverse confluent Vandermonde
  matrix norm ||U*||_infty -- i.e. accuracy is inversely proportional to node separation
  and this dependence is ''roughly of the same order as some finite power of prod_{i<j}|xi_j-xi_i|^{-1}''
  (Sec 1.D summary). Section 5.A shows this matches the Cramer-Rao bound for the equivalent
  PACE (polynomial-amplitude complex exponential) statistical model up to constants.
  This is the most directly transferable published template for the manuscript''s
  planned theorem: an explicit local (first-order/Jacobian-inverse) stability bound
  for a power-sum-type inverse problem, singular exactly at node collisions, with
  the blow-up rate expressed via pairwise node-gap products.'
---

[1106.1137] On the accuracy of solving confluent Prony systems
Skip to main content
Search arXiv
Press Enter to search ·
Advanced search
Mathematics > Classical Analysis and ODEs
arXiv:1106.1137
(math)
[Submitted on 6 Jun 2011 (
v1
), last revised 26 Jun 2012 (this version, v3)]
Title:
On the accuracy of solving confluent Prony systems
Authors:
Dmitry Batenkov
,
Yosef Yomdin
View a PDF of the paper titled On the accuracy of solving confluent Prony systems, by Dmitry Batenkov and 1 other authors
View PDF
Abstract:
In this paper we consider several nonlinear systems of algebraic equations which can be called "Prony-type". These systems arise in various reconstruction problems in several branches of theoretical and applied mathematics, such as frequency estimation and nonlinear Fourier inversion. Consequently, the question of stability of solution with respect to errors in the right-hand side becomes critical for the success of any particular application. We investigate the question of "maximal possible accuracy" of solving Prony-type systems, putting stress on the "local" behavior which approximates situations with low absolute measurement error. The accuracy estimates are formulated in very simple geometric terms, shedding some light on the structure of the problem. Numerical tests suggest that "global" solution techniques such as Prony's algorithm and ESPRIT method are suboptimal when compared to this theoretical "best local" behavior.
Subjects:
Classical Analysis and ODEs (math.CA)
MSC
classes:
65H10, 41A46, 94A12
Cite as:
arXiv:1106.1137
[math.CA]
(or
arXiv:1106.1137v3
[math.CA]
for this version)
https://doi.org/10.48550/arXiv.1106.1137
Focus to learn more
arXiv-issued DOI via DataCite
Journal reference:
SIAM J. Appl. Math., 73(1), 2013, pp. 134--154
Related DOI
:
https://doi.org/10.1137/110836584
Focus to learn more
DOI(s) linking to related resources
Submission history
From: Dmitry Batenkov [
view email
]
[v1]
Mon, 6 Jun 2011 18:06:32 UTC (146 KB)
[v2]
Sat, 23 Jun 2012 14:42:30 UTC (236 KB)
[v3]
Tue, 26 Jun 2012 08:28:35 UTC (236 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled On the accuracy of solving confluent Prony systems, by Dmitry Batenkov and 1 other authors
View PDF
TeX Source
view license
Current browse context:
math.CA
< prev
|
next >
new
|
recent
|
2011-06
Change to browse by:
math
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
export BibTeX citation
Loading...
BibTeX formatted citation
×
loading...
Data provided by:
Bookmark
Bibliographic Tools
Bibliographic and Citation Tools
Bibliographic Explorer Toggle
Bibliographic Explorer
(
What is the Explorer?
)
Connected Papers Toggle
Connected Papers
(
What is Connected Papers?
)
Litmaps Toggle
Litmaps
(
What is Litmaps?
)
scite.ai Toggle
scite Smart Citations
(
What are Smart Citations?
)
Code, Data, Media
Code, Data and Media Associated with this Article
alphaXiv Toggle
alphaXiv
(
What is alphaXiv?
)
Links to Code Toggle
CatalyzeX Code Finder for Papers
(
What is CatalyzeX?
)
DagsHub Toggle
DagsHub
(
What is DagsHub?
)
GotitPub Toggle
Gotit.pub
(
What is GotitPub?
)
Huggingface Toggle
Hugging Face
(
What is Huggingface?
)
ScienceCast Toggle
ScienceCast
(
What is ScienceCast?
)
Demos
Demos
Replicate Toggle
Replicate
(
What is Replicate?
)
Spaces Toggle
Hugging Face Spaces
(
What is Spaces?
)
Spaces Toggle
TXYZ.AI
(
What is TXYZ.AI?
)
Related Papers
Recommenders and Search Tools
Link to Influence Flower
Influence Flower
(
What are Influence Flowers?
)
Core recommender toggle
CORE Recommender
(
What is CORE?
)
Author
Venue
Institution
Topic
About arXivLabs
arXivLabs: experimental projects with community collaborators
arXivLabs is a framework that allows collaborators to develop and share new arXiv features directly on our website.
Both individuals and organizations that work with arXivLabs have embraced and accepted our values of openness, community, excellence, and user data privacy. arXiv is committed to these values and only works with partners that adhere to them.
Have an idea for a project that will add value for arXiv's community?
Learn more about arXivLabs
.
Which authors of this paper are endorsers?
|
Disable MathJax
(
What is MathJax?
)