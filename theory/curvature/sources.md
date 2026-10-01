# Sources for the curvature comparison

All items were retrieved on 2026-10-01 by headless curl with a desktop User-Agent. PDF text was
extracted with PyMuPDF. Local copies are in the session scratchpad, not the repo. Page numbers
are PDF pages unless marked "printed". Quotations are verbatim from the extracted text, with
typography normalised.

## [Kok] A. Kokotov, *Compact polyhedral surfaces of an arbitrary genus and determinants of Laplacians*, arXiv:0906.0717v1 (2009)

Retrieved from `https://arxiv.org/pdf/0906.0717`.

- **Proposition 1 (p. 6, eq. (7)).** On the infinite flat cone $C_\beta$ of angle $\beta$, with
  $C_\beta(R)$ the points at distance $<R$ from the tip, for some $\epsilon>0$:
  $$\int_{C_\beta(R)}H_\beta(x,x;t)\,dx=\frac1{4\pi t}\operatorname{Area}(C_\beta(R))
  +\frac1{12}\Big(\frac{2\pi}\beta-\frac\beta{2\pi}\Big)+O(e^{-\epsilon/t}).$$
- **Theorem 1, item 2 (p. 9, eq. (13)).** For a compact polyhedral surface $X$ (a flat metric
  with conical points $P_1,\dots,P_N$ of angles $\beta_k$) and the Friedrichs Laplacian:
  $$\operatorname{Tr}e^{t\Delta}=\frac{\operatorname{Area}(X)}{4\pi t}
  +\frac1{12}\sum_{k=1}^N\Big(\frac{2\pi}{\beta_k}-\frac{\beta_k}{2\pi}\Big)+O(e^{-\epsilon/t}).$$
- The proof (pp. 10–11) localises. Near each vertex it uses (7). On the flat part away from the
  vertices it uses "Area$(K_0)/(4\pi t)+O(e^{-\epsilon_3/t})$ (cf. [MS67])".

For an orbifold cone point of order $m$, $\beta=2\pi/m$, and
$\frac1{12}(m-\frac1m)=\frac{m^2-1}{12m}$. This is the manuscript's $\operatorname{cone}(m)$
(Corollary `cor:conevals`).

## [DGGW] E. B. Dryden, C. S. Gordon, S. J. Greenwald, D. L. Webb, *Asymptotic expansion of the heat kernel for orbifolds*, arXiv:0805.3148v1 (2008); Michigan Math. J. 56 (2008)

Retrieved from `https://arxiv.org/pdf/0805.3148`.

- **Theorem 4.8 (p. 17).** "The heat trace $\sum e^{-\lambda_jt}$ of $\mathcal O$ is asymptotic
  as $t\to0^+$ to $I_0+\sum_{N\in S(\mathcal O)}\frac{I_N}{|\mathrm{Iso}(N)|}$". Here
  $I_N=(4\pi t)^{-\dim N/2}\sum_k t^k\int_N b_k(N,x)\,d\mathrm{vol}_N$, and the $a_k(\mathcal O)$
  in $I_0$ are "the familiar heat invariants" built from curvature (Definition 4.7, p. 17).
- **(5.7), p. 24.** The degree-zero term for an orientable 2-orbifold with cone orders $m_i$ is
  $\frac{\chi(\mathcal O)}6+\sum_i\frac{m_i^2-1}{12m_i}$.
- **(5.13), p. 27.** $c=2\chi(\mathcal O)+\sum_i(m_i-\frac1{m_i})$ (twelve times the degree-zero
  term). "This quantity is a spectral invariant; note that it depends only on the topology, not
  on the Riemannian metric."
- **Table 1 (p. 28),** constant terms with $\chi\ge0$:
  - $\mathcal O(2,2,m)$: $\frac1{12}(3+m+\frac1m)$
  - $\mathcal O(m,n)$: $\frac1{12}(m+n+\frac1m+\frac1n)$
  - $(2,3,3)$: $\frac{43}{72}$
  - $(2,3,4)$: $\frac{97}{144}$
  - $(2,3,5)$: $\frac{271}{360}$
  - torus and Klein bottle: $V\frac1t+O(t)$
  - $\mathcal O(2,2,2,2)$: $\frac12$
  - $\mathcal O(2,4,4)$: $\frac34$
  - $\mathcal O(3,3,3)$: $\frac23$
  - $\mathcal O(2,3,6)$: $\frac56$
- **Theorem 5.15 (p. 29).** "Let $C$ be the class consisting of all closed orientable
  2-orbifolds with $\chi(\mathcal O)\ge0$. The spectral invariant $c$ is a complete topological
  invariant within $C$ and moreover, it distinguishes the elements of $C$ from smooth oriented
  closed surfaces."
- **Remark 5.16 (p. 31).** "Notably absent from the class C are triangular pillows with
  $\chi(\mathcal O)<0$. The invariant c does not seem sufficiently strong to distinguish among
  these triangular pillows."
- **Proposition 5.22 (p. 33).** "Within the class of spherical 2-orbifolds of constant curvature
  $R>0$ the spectrum determines the orbifold."
- **Remark 5.23 (p. 34).** "We cannot make a similar statement for flat 2-orbifolds. For
  example, it is possible to endow $O(2,*2,2)$ and $O(2,2*)$ with a metric of zero curvature so
  that they have the same area and also have mirror loci of the same length. They cannot be
  distinguished by the asymptotic expansion of the heat trace."

## [Thu] W. P. Thurston, *The Geometry and Topology of Three-Manifolds*, Chapter 13 (lecture notes; MSRI/SLMath electronic edition)

Retrieved from `https://library.slmath.org/books/gt3m/PDF/13.pdf`.

- **Gauss–Bonnet, 13.3.5 (printed p. 312).** $\int_{\mathcal O}K\,dA=2\pi\chi(\mathcal O)$. "If
  O is elliptic or hyperbolic, then area (O) = $2\pi|\chi(O)|$."
- **Theorem 13.3.6 (printed pp. 312–313).** "A closed two-dimensional orbifold has an elliptic,
  parabolic or hyperbolic structure if and only if it is good. An orbifold O has a hyperbolic
  structure if and only if $\chi(O)<0$, and a parabolic structure if and only if $\chi(O)=0$. An
  orbifold is elliptic or bad if and only if $\chi(O)>0$."
- The table that follows, for underlying space $X_O=S^2$:
  - Bad: $(n)$; $(n_1,n_2)$ with $n_1<n_2$.
  - Elliptic: $(\ )$, $(n,n)$, $(2,2,n)$, $(2,3,3)$, $(2,3,4)$, $(2,3,5)$.
  - Parabolic: $(2,3,6)$, $(2,4,4)$, $(3,3,3)$, $(2,2,2,2)$; also $X_O=T^2$ with no singular
    points.
- The parabolic list for $X_O=D^2,P^2$, Klein bottle, annulus and Möbius band completes the 17
  parabolic orbifolds. "The 17 parabolic orbifolds correspond to the 17 'wallpaper groups.'"
  (printed p. 314).

## [Uc] E. Uçar, *Spectral invariants for polygons and orbisurfaces*, arXiv:1711.03405 (thesis, 2017)

Retrieved from `https://arxiv.org/pdf/1711.03405` (transcription of (4.25), (4.33) in
`theory/cone-coefficients/ucar-source.md`).

- **Corollary 4.21 (printed p. 139).** Let $\mathcal O$ be a closed orbisurface of constant
  curvature $\kappa\in\mathbb R$. "(iv) If the mirror locus is trivial and $\kappa\neq0$, then
  $\kappa$ together with the spectrum determines the number of cone points as well as the
  multiset of all orders $\{n_1,\dots,n_N\}$." Also: "statement (iv) is also new in this
  generality and was only known for the special case of $\kappa=-1$".
- **Printed p. 97 (PDF p. 102).** "polygons of constant zero curvature have at most three
  nonvanishing heat invariants".
- **Printed p. 99.** "if a polygon has zero curvature, then the heat invariants do not provide
  much information about the geometry of the polygon".
- **Printed p. 140 (PDF p. 145).** The proof of Corollary 4.23 uses "only heat invariants", so
  Cor. 4.21(iv) is a statement about the heat invariants.
- **Theorem 3.40 proof (printed pp. 98–99).** The smallest angle is recovered from the sequence
  $W_{\nu,1}$ (the top-degree parts of the heat coefficients): "the smallest angle can be
  deduced from the sequence $(W_{\nu,1})_{\nu\in\mathbb N_0}$". The argument uses
  $\kappa\neq0$, because $W_\nu$ is the coefficient of $\kappa^\nu$.

## [DS] E. B. Dryden, A. Strohmaier, *Huber's theorem for hyperbolic orbisurfaces*, arXiv:math/0504571v2 (2005/2007)

Retrieved from `https://arxiv.org/pdf/math/0504571`.

- **Theorem 1.1 (p. 2).** "Let O be a compact orientable hyperbolic orbisurface. The Laplace
  spectrum of O determines its length spectrum and the number of cone points of each possible
  order."
- **Eq. (1) (p. 3),** the elliptic term of the Selberg trace formula:
  $\sum_{\{R\}}\frac1{2m(R)\sin\theta(R)}\int_{-\infty}^{\infty}\frac{e^{-2\theta(R)r}}{1+e^{-2\pi r}}h(r)\,dr$,
  with $\theta(R)=\pi l/m(R)$, $1\le l\le m(R)-1$.
