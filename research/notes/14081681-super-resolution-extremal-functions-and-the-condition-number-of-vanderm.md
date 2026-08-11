---
title: '[1408.1681] Super-resolution, Extremal Functions and the Condition Number
  of Vandermonde Matrices'
id: 14081681-super-resolution-extremal-functions-and-the-condition-number-of-vanderm
tags:
- hyperbolic-pillow-heat-novelty-813161
- super-resolution
- vandermonde-conditioning
- prony-method
created: '2026-08-09T08:45:23.112523Z'
updated: '2026-08-09T09:36:32.272888Z'
source: https://arxiv.org/abs/1408.1681
source_domain: arxiv.org
fetched_at: '2026-08-09T08:45:23.112236Z'
fetch_provider: builtin
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Moitra, ''Super-resolution, Extremal Functions and the Condition Number
  of Vandermonde Matrices,'' STOC 2015 (DOI 10.1145/2746539.2746561), arXiv:1408.1681v4.
  Full PDF read (4 pages: abstract/intro/results). THE canonical separation-dependent
  result for this manuscript''s Q4: for k point sources with minimum wrap-around separation
  Delta among frequencies f_j in [0,1), recovery from m low-frequency Fourier measurements
  (cutoff m) exhibits a SHARP PHASE TRANSITION: Theorem 1.2 -- if m > 1/Delta + 1,
  a polynomial-time estimator recovers the u_j''s and f_j''s converging to the truth
  at an inverse-polynomial rate in the noise magnitude; conversely if m < (1-eps)/Delta,
  no estimator can distinguish a particular pair of Delta-separated signals even if
  the noise is exponentially small. Theorem 1.1 gives the exact conditioning statement:
  kappa(V_m^k(alpha_1,...,alpha_k))^2 <= (m+1/Delta-1)/(m-1/Delta-1) for m > 1/Delta+1,
  proved via Beurling-Selberg extremal majorant/minorant functions linked to the large
  sieve inequality. Also states the classical approximation-theory fact (Sec 1.2)
  that reconstructing p(2) for a degree-k polynomial from noisy values on [0,1] has
  error blowing up as c(2+sqrt(3))^k * eta -- an exponential-in-degree conditioning
  bound analogous to Wilkinson/Gautschi. This is the single most transferable result:
  it gives the EXACT form of ''blow-up as an inverse power of minimum separation Delta,''
  which is structurally identical to the manuscript''s blow-up as an inverse function
  of the pairwise gaps (p-q)(p-r)(q-r).'
---

*Suggested by [[170102538-vandermonde-matrices-with-nodes-in-the-unit-disk-and-the-large-sieve]] — Moitra's super-resolution/condition-number paper is the key precursor cited for the Selberg-Moitra bound*

[1408.1681] Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices
Skip to main content
arXiv is now an independent nonprofit!
Learn more
×
Search arXiv
Press Enter to search ·
Advanced search
Computer Science > Information Theory
arXiv:1408.1681
(cs)
[Submitted on 7 Aug 2014 (
v1
), last revised 29 Apr 2015 (this version, v4)]
Title:
Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices
Authors:
Ankur Moitra
View a PDF of the paper titled Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices, by Ankur Moitra
View PDF
Abstract:
Super-resolution is a fundamental task in imaging, where the goal is to extract fine-grained structure from coarse-grained measurements. Here we are interested in a popular mathematical abstraction of this problem that has been widely studied in the statistics, signal processing and machine learning communities. We exactly resolve the threshold at which noisy super-resolution is possible. In particular, we establish a sharp phase transition for the relationship between the cutoff frequency ($m$) and the separation ($\Delta$). If $m > 1/\Delta + 1$, our estimator converges to the true values at an inverse polynomial rate in terms of the magnitude of the noise. And when $m < (1-\epsilon) /\Delta$ no estimator can distinguish between a particular pair of $\Delta$-separated signals even if the magnitude of the noise is exponentially small.
Our results involve making novel connections between {\em extremal functions} and the spectral properties of Vandermonde matrices. We establish a sharp phase transition for their condition number which in turn allows us to give the first noise tolerance bounds for the matrix pencil method. Moreover we show that our methods can be interpreted as giving preconditioners for Vandermonde matrices, and we use this observation to design faster algorithms for super-resolution. We believe that these ideas may have other applications in designing faster algorithms for other basic tasks in signal processing.
Comments:
19 pages
Subjects:
Information Theory (cs.IT)
; Data Structures and Algorithms (cs.DS); Statistics Theory (math.ST)
Cite as:
arXiv:1408.1681
[cs.IT]
(or
arXiv:1408.1681v4
[cs.IT]
for this version)
https://doi.org/10.48550/arXiv.1408.1681
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Ankur Moitra [
view email
]
[v1]
Thu, 7 Aug 2014 18:54:19 UTC (25 KB)
[v2]
Fri, 8 Aug 2014 12:42:01 UTC (25 KB)
[v3]
Mon, 27 Apr 2015 20:35:47 UTC (26 KB)
[v4]
Wed, 29 Apr 2015 02:18:44 UTC (26 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Super-resolution, Extremal Functions and the Condition Number of Vandermonde Matrices, by Ankur Moitra
View PDF
TeX Source
view license
Current browse context:
cs.IT
< prev
|
next >
new
|
recent
|
2014-08
Change to browse by:
cs
cs.DS
math
math.IT
math.ST
stat
stat.TH
References & Citations
NASA ADS
Google Scholar
Semantic Scholar
DBLP
- CS Bibliography
listing
|
bibtex
Ankur Moitra
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