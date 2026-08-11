---
title: '[2001.05281] Min-Max Elementwise Backward Error for Roots of Polynomials and
  a Corresponding Backward Stable Root Finder'
id: 200105281-min-max-elementwise-backward-error-for-roots-of-polynomials-and-a-corr
tags:
- hyperbolic-pillow-heat-novelty-813161
- root-perturbation
created: '2026-08-09T08:46:20.588270Z'
updated: '2026-08-09T09:36:32.369677Z'
source: https://arxiv.org/abs/2001.05281
source_domain: arxiv.org
fetched_at: '2026-08-09T08:46:20.587937Z'
fetch_provider: builtin
status: evergreen
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Tisseur & Van Barel, ''Min-Max Elementwise Backward Error for Roots of Polynomials
  and a Corresponding Backward Stable Root Finder,'' arXiv:2001.05281v1 (math.NA),
  DOI 10.48550/arXiv.2001.05281. Full PDF read (4 pages: intro + Sec 1-2). States
  the STANDARD first-order forward-error formula for a simple root z_k of p(z)=sum
  p_i z^i (eq. 1.3, assuming zeros are simple, neglecting higher-order terms): err(z_k)
  = |Delta p(zhat_k)| / (|z_k| |p''(zhat_k)|), i.e. the relative forward error in
  a root equals the backward perturbation of the polynomial evaluated at that root,
  divided by |z_k p''(z_k)|. Combined with the elementwise backward-error bound (eq.
  1.4b): |Delta p(zhat_k)| <= eta^elem_{|p|} sum_i |p_i||zhat_k|^i, this yields exactly
  the manuscript''s target formula: for a single perturbed coefficient delta a_j,
  |delta z_k| ~ |delta a_j| |z_k|^j / |p''(z_k)|. Numerical example (Table 1.1, a
  quartic with two tiny-magnitude roots ~1e-15/1e-30) shows normwise-stable computed
  roots can still have huge normwise forward error while being well-conditioned elementwise
  -- illustrating that |p''(z_k)| in the denominator (equivalently the product of
  pairwise root gaps for monic polynomials) is the correct conditioning quantity,
  exactly the quantity appearing in the manuscript''s Jacobian.'
---

[2001.05281] Min-Max Elementwise Backward Error for Roots of Polynomials and a Corresponding Backward Stable Root Finder
Skip to main content
arXiv is now an independent nonprofit!
Learn more
×
Search arXiv
Press Enter to search ·
Advanced search
Mathematics > Numerical Analysis
arXiv:2001.05281
(math)
[Submitted on 15 Jan 2020]
Title:
Min-Max Elementwise Backward Error for Roots of Polynomials and a Corresponding Backward Stable Root Finder
Authors:
Francoise Tisseur
,
Marc Van Barel
View a PDF of the paper titled Min-Max Elementwise Backward Error for Roots of Polynomials and a Corresponding Backward Stable Root Finder, by Francoise Tisseur and 1 other authors
View PDF
Abstract:
A new measure called min-max elementwise backward error is introduced for approximate roots of scalar polynomials $p(z)$. Compared with the elementwise relative backward error, this new measure allows for larger relative perturbations on the coefficients of $p(z)$ that do not participate much in the overall backward error. By how much these coefficients can be perturbed is determined via an associated max-times polynomial and its tropical roots. An algorithm is designed for computing the roots of $p(z)$. It uses a companion linearization $C(z) = A-zB$ of $p(z)$ to which we added an extra zero leading coefficient, and an appropriate two-sided diagonal scaling that balances $A$ and makes $B$ graded in particular when there is variation in the magnitude of the coefficients of $p(z)$. An implementation of the QZ algorithm with a strict deflation criterion for eigenvalues at infinity is then used to obtain approximations to the roots of $p(z)$. Under the assumption that this implementation of the QZ algorithm exhibits a graded backward error when $B$ is graded, we prove that our new algorithm is min-max elementwise backward stable. Several numerical experiments show the superior performance of the new algorithm compared with the MATLAB \texttt{roots} function. Extending the algorithm to polynomial eigenvalue problems leads to a new polynomial eigensolver that exhibits excellent numerical behaviour compared with other existing polynomial eigensolvers, as illustrated by many numerical tests.
Subjects:
Numerical Analysis (math.NA)
MSC
classes:
65F15, 65H04, 30C15, 15A22, 15A80, 15A18, 47J10
Cite as:
arXiv:2001.05281
[math.NA]
(or
arXiv:2001.05281v1
[math.NA]
for this version)
https://doi.org/10.48550/arXiv.2001.05281
Focus to learn more
arXiv-issued DOI via DataCite
Submission history
From: Marc Van Barel [
view email
]
[v1]
Wed, 15 Jan 2020 13:01:10 UTC (131 KB)
Full-text links:
Access Paper:
View a PDF of the paper titled Min-Max Elementwise Backward Error for Roots of Polynomials and a Corresponding Backward Stable Root Finder, by Francoise Tisseur and 1 other authors
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
2020-01
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