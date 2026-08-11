---
title: '[1504.02118] How Bad Are Vandermonde Matrices?'
id: 150402118-how-bad-are-vandermonde-matrices
tags:
- hyperbolic-pillow-heat-novelty-813161
- vandermonde-conditioning
- root-perturbation
created: '2026-08-09T08:43:25.117169Z'
updated: '2026-08-09T09:36:32.213762Z'
source: https://arxiv.org/abs/1504.02118
source_domain: arxiv.org
fetched_at: '2026-08-09T08:43:25.116921Z'
fetch_provider: builtin
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Pan (2015, arXiv:1504.02118v3, DOI 10.48550/arXiv.1504.02118) proves the
  n-node Vandermonde matrix V_s = (s_i^j) is exponentially ill-conditioned in n unless
  the knots s_0,...,s_{n-1} are ''more or less equally spaced on or about the unit
  circle.'' Key results: Theorem 4.1/Cor 4.2/4.3 give kappa(V_s) >= sqrt(n) max_{|f|=1}|s(f)|/max_i|s_i-f|
  via a Vandermonde-to-Cauchy transformation and the Eckart-Young theorem; Theorem
  5.1 shows kappa(V_q) >= 2^{q/2} sqrt(n) for the quasi-cyclic knot sequence (n=3q);
  Theorem 8.1/Corollary 8.1 gives the general exponential lower bound kappa(V_s) >=
  eta^rho(eta-1) r sqrt(n)/2 in terms of a separation parameter r between clustered
  and non-clustered knot sets. Numerical tests (Tables 9.1-9.5) confirm condition
  numbers exceeding 1e+265 for n=256. Directly establishes that Vandermonde conditioning
  is governed by pairwise/clustering separation of the nodes, exactly the mechanism
  behind the manuscript''s diagonal blow-up.'
---

[1504.02118] How Bad Are Vandermonde Matrices?
Skip to main content
System maintenance August 4th and 5th
Learn more
×
Search arXiv
Press Enter to search ·
Advanced search
Mathematics > Numerical Analysis
arXiv:1504.02118
(math)
[Submitted on 8 Apr 2015 (
v1
), last revised 10 Jul 2015 (this version, v3)]
Title:
How Bad Are Vandermonde Matrices?
Authors:
Victor Y. Pan
View a PDF of the paper titled How Bad Are Vandermonde Matrices?, by Victor Y. Pan
View PDF
Abstract:
The work on the estimation of the condition numbers of Vandermonde matrices, motivated by applications to interpolation and quadrature, can be traced back at least to the 1970s. Empirical study has shown consistently that Vandermonde matrices tend to be badly ill-conditioned, with a narrow class of notable exceptions, such as the matrices of the discrete Fourier transform (hereafter referred to as DFT). So far formal support for this empirical observation, however, has been limited to the matrices defined by the real set of knots. We prove that, more generally, any Vandermonde matrix of a large size is badly ill-conditioned unless its knots are more or less equally spaced on or about the circle $C(0,1)=\{x:\,|x|=1\}$. The matrices of DFT are perfectly conditioned, being defined by a cyclic sequence of knots, equally spaced on that circle, but we prove that even a slight modification of the knots into the so called quasi-cyclic sequence on this circle defines badly ill-conditioned Vandermonde matrices. Likewise we prove that the half-size leading block of a large DFT matrix is badly ill-conditioned. (This result was motivated by an application to pre-conditioning of an input matrix for Gaussian elimination with no pivoting.) Our analysis involves the Ekkart--Young theorem, the Vandermonde-to-Cauchy transformation of matrix structure, our new inversion formula for a Cauchy matrix, and low-rank approximation of its large submatrices.
Comments:
13 pages
Subjects:
Numerical Analysis (math.NA)
Cite as:
arXiv:1504.02118
[math.NA]
(or
arXiv:1504.02118v3
[math.NA]
for this version)
https://doi.org/10.48550/arXiv.1504.02118
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Victor Pan [
view email
]
[v1]
Wed, 8 Apr 2015 20:29:02 UTC (13 KB)
[v2]
Sun, 26 Apr 2015 20:36:39 UTC (14 KB)
[v3]
Fri, 10 Jul 2015 08:11:18 UTC (20 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled How Bad Are Vandermonde Matrices?, by Victor Y. Pan
View PDF
TeX Source
view license
Current browse context:
math.NA
< prev
|
next >
new
|
recent
|
2015-04
Change to browse by:
cs
cs.NA
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