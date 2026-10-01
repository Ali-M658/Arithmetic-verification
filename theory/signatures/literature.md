# Literature: smooth heat terms and genus

Retrieved 2026-10-01 by headless curl (desktop User-Agent string), arXiv API, Crossref API, and Unpaywall API. PDF text was extracted with PyMuPDF (`fitz`). Each displayed theorem or equation quoted below was located in the extracted text, and the page was then rendered to PNG at 130 dpi and read visually to check the transcription. Statements checked this way are marked **[image-confirmed]**. Statements marked **[text-extracted]** were transcribed from the extracted text only.

Page convention: "PDF p. N" is the page index in the downloaded file. The printed page number is given when it differs.

---

## Retrieval log

| # | Request | Result |
|---|---------|--------|
| 1 | `curl -L https://arxiv.org/pdf/0805.3148` | 200, 405,933 bytes, 35 pages (DGGW, v1) |
| 2 | `curl -L https://arxiv.org/pdf/1711.03405` | 200, 1,623,025 bytes, 156 pages (Uçar thesis, v1) |
| 3 | `curl -L https://arxiv.org/pdf/math/0504571` | 200, 125,895 bytes, 6 pages (Dryden–Strohmaier, v2) |
| 4 | `curl -L https://arxiv.org/pdf/2311.00337` | 200, 254,478 bytes, 16 pages (v2) |
| 5 | `http://export.arxiv.org/api/query?id_list=0805.3148,1711.03405,math/0504571,2311.00337` | 301, then 200 at `https://export.arxiv.org/...` after `-L`; 4 entries |
| 6 | `https://api.crossref.org/works/10.1307/mmj/1213972406` | 200 (DGGW record) |
| 7 | `https://api.crossref.org/works/10.4153/CMB-2009-008-0` | 200 (Dryden–Strohmaier record) |
| 8 | `https://api.crossref.org/works?query.bibliographic=Donnelly Spectrum and the fixed point sets of isometries I Math. Ann. 224 1976` | 200; top hit DOI 10.1007/bf01436198 |
| 9 | `https://api.crossref.org/works?query.bibliographic=Donnelly Asymptotic expansions for the compact quotients of properly discontinuous group actions Illinois J. Math 1979` | 200; top hit DOI 10.1215/ijm/1256048110 |
| 10 | `https://api.unpaywall.org/v2/10.1007/bf01436198?email=...` | 200; `is_oa: false`, `oa_status: closed` |
| 11 | `https://api.unpaywall.org/v2/10.1215/ijm/1256048110?email=...` | 200; `is_oa: true`, `oa_status: bronze`, publisher PDF on projecteuclid.org |
| 12 | `curl -L <projecteuclid PDF URL from #11>` | 200, `application/pdf`, 1,010,913 bytes, 12 pages (Donnelly 1979, scanned with OCR text layer) |
| 13 | `https://api.crossref.org/works?query.bibliographic=Do the Hodge spectra distinguish orbifolds from manifolds? Part 2 ...` | 200; top hit DOI 10.1307/mmj/20236493 |
| 14 | `https://api.crossref.org/works/10.1307/mmj/20236493` | 200 (record for arXiv:2311.00337) |
| 15–23 | `curl -L -X POST https://arxiv.org/search_classic --data-urlencode query=<q> --data-urlencode searchtype=ft` (9 queries, listed in B4) | All 200. The POST redirected to `https://search.arxiv.org/?query=...`, which returned HTML result pages. |
| 24 | `curl -L https://arxiv.org/pdf/1812.06119`, `https://arxiv.org/pdf/1408.2001`, and arXiv API for both | All 200 |

All downloaded PDFs are in the scratch directory `.../scratchpad/lit/`. None were placed in the repository.

---

## A. DGGW (and Donnelly): the smooth-stratum statement

### Bibliographic record

- **From the Crossref API** (`/works/10.1307/mmj/1213972406`): Emily B. Dryden, Carolyn S. Gordon, Sarah J. Greenwald, David L. Webb, "Asymptotic expansion of the heat kernel for orbifolds", *Michigan Mathematical Journal*, vol. 56, issue 1, published-print 2008-06-01, publisher "Michigan Mathematical Journal", DOI 10.1307/mmj/1213972406. **The record has no `page` field.** The DOI supplied in the task is verified.
- **From the arXiv API**: arXiv:0805.3148v1, published 2008-05-20, comment "to appear in Michigan Math. J". Primary category math.DG. Same four authors.
- The quotes below come from the arXiv v1 preprint. Its printed page numbers equal its PDF page numbers, but they are **not** the journal page numbers, which Crossref did not supply.

### A(i). Main theorem: heat trace as a sum over strata

**Theorem 4.8** (PDF p. 17) **[image-confirmed]**:

> 4.8. THEOREM. *Let $\mathcal{O}$ be a Riemannian orbifold and let $\lambda_1 \le \lambda_2 \le \dots$ be the spectrum of the associated Laplacian acting on smooth functions on $\mathcal{O}$. The heat trace $\sum_{j=1}^\infty e^{-\lambda_j t}$ of $\mathcal{O}$ is asymptotic as $t \to 0^+$ to*
> $$I_0 + \sum_{N \in S(\mathcal{O})} \frac{I_N}{|\mathrm{Iso}(N)|}$$
> *where $S(\mathcal{O})$ is the set of all $\mathcal{O}$-strata and where $|\mathrm{Iso}(N)|$ is the order of the isotropy at each $p \in N$ as defined in Remark 2.7. This asymptotic expansion is of the form*
> $$(4.9)\qquad (4\pi t)^{-\dim(\mathcal{O})/2} \sum_{j=0}^\infty c_j t^{\frac{j}{2}}$$
> *for some constants $c_j$.*

### A(ii). Definition 4.7: the prefactor, $I_0$ and $I_N$

**Definition 4.7** (PDF p. 17) **[image-confirmed]**:

> 4.7. DEFINITION. Let $\mathcal{O}$ be a Riemannian orbifold and let $N$ be an $\mathcal{O}$-stratum.
> (i) For each non-negative integer $k$, define a real-valued function $b_k(N,\cdot)$ by setting $b_k(N,p) = b_k(\widetilde N,\tilde p)$ where $(\widetilde U, G_U, \pi_U)$ is any orbifold chart about $p$, $\tilde p \in \pi_U^{-1}(p)$ and $\widetilde N$ is the $\widetilde U$-stratum through $\tilde p$. By Lemma 4.6, the function $b_k(N,\cdot)$ is well-defined.
> (ii) The Riemannian metric on $\mathcal{O}$ induces a Riemannian metric, and thus a volume element, on the manifold $N$. Set
> $$I_N := (4\pi t)^{-\dim(N)/2} \sum_{k=0}^\infty t^k \int_N b_k(N,x)\, d\,\mathrm{vol}_N(x)$$
> where $d\,\mathrm{vol}_N$ is the Riemannian volume element.
> (iii) Also set
> $$I_0 = (4\pi t)^{-\dim(\mathcal{O})/2} \sum_{k=0}^\infty a_k(\mathcal{O}) t^k$$
> where the $a_k(\mathcal{O})$ (which we will usually write simply as $a_k$) are the familiar heat invariants. More precisely, the invariants $u_i$ in (3.5), which are defined in terms of the curvature and its covariant derivatives on any Riemannian manifold, also make sense on any Riemannian orbifold. The invariants $a_k(\mathcal{O})$ are given by $a_k = \int_{\mathcal{O}} u_k(x,x)\, d\,\mathrm{vol}_{\mathcal{O}}(x)$. In particular, $a_0 = \mathrm{vol}(\mathcal{O})$, $a_1 = \frac{1}{6}\int_{\mathcal{O}} \tau(x)\, d\,\mathrm{vol}_{\mathcal{O}}(x)$, etc. Note that if $\mathcal{O}$ is finitely covered by a Riemannian manifold $M$, say $\mathcal{O} = G\backslash M$, then $a_k(\mathcal{O}) = \frac{1}{|G|} a_k(M)$.

The $u_i$ are defined in equation **(3.5)** (PDF p. 10) **[image-confirmed]**:

> Recall that the heat kernel on a closed $n$-dimensional Riemannian manifold $M$ has an asymptotic expansion along the diagonal in $M \times M$ as $t \to 0^+$ of the form
> $$(3.5)\qquad K(t,x,x) \sim (4\pi t)^{-\frac{n}{2}}\big(u_0(x,x) + t u_1(x,x) + t^2 u_2(x,x) + \dots\big)$$
> where the $u_i$ are local Riemannian invariants defined in a neighborhood of the diagonal in $M \times M$.

On the singular-strata functions, §4.1–4.2 (PDF pp. 15–16):

- PDF p. 15 **[text-extracted]**: "For each non-negative integer $k$, Donnelly [10] defined a real-valued function, which we temporarily denote $b_k((M,\gamma),\cdot)$, on the fixed point set of $\gamma$." The paper lists "(Locality)" and "(Universality)" properties.
- PDF p. 16 **[image-confirmed]**: "Donnelly showed that $b_k(\gamma,x) = |\det(B_\gamma(x))|\,\widetilde b_k(\gamma,x)$, where $\widetilde b_k(\gamma,\cdot)$ is an $O(m)\times O(n-m)$ universal invariant polynomial in the components of $B_\gamma$ and in the curvature tensor $R$ of $M$ and its covariant derivatives." This is followed by (4.3) $b_0(\gamma,x) = |\det(B_\gamma(x))|$ and (4.4) $b_1(\gamma,x) = |\det(B_\gamma(x))|(\tfrac16\tau + \tfrac16\rho_{kk} + \tfrac13 R_{iksh}B_{ki}B_{hs} + \tfrac13 R_{ikth}B_{kt}B_{hi} - R_{kaha}B_{ks}B_{hs})$.

**Remark 4.10** (PDF p. 17) **[image-confirmed]**, giving the Donnelly provenance:

> 4.10. REMARK. Suppose $\mathcal{O} = G\backslash M$ is a good closed orbifold. Note that $M$ may be noncompact and $G$ may be an infinite group, although the isotropy group at any point of $M$ must be a finite subgroup of $G$. In this setting, Donnelly [11] proved the existence and uniqueness of the heat kernel $K^M$ on $M$ and of an asymptotic expansion for $K^M$. He then obtained an asymptotic expansion for the heat trace on $\mathcal{O}$. Theorem 4.8, in the case of good orbifolds, organizes the information in [11] in a way that clarifies the contribution of each $\mathcal{O}$-stratum to the asymptotics.

DGGW also cite Donnelly in the abstract and introduction (PDF pp. 1–2) **[text-extracted]**: "In the case of a good Riemannian orbifold (i.e., an orbifold arising as the orbit space of a manifold under the action of a discrete group of isometries), H. Donnelly [10] proved the existence of the heat kernel and constructed the asymptotic expansion for the heat trace. We extend Donnelly's work to the case of general compact orbifolds."

**Proposition 4.11** (PDF p. 18) **[text-extracted]** is attributed to "[10]". It states that for a nontrivial isometry $\gamma$ of a closed $M$, $\int_M K(t,x,\gamma(x))\,d\mathrm{vol}_M(x)$ is asymptotic to $\sum_{W\in\Omega(\gamma)} (4\pi t)^{-\dim(W)/2} \sum_k t^k \int_W b_k(\gamma,a)\,d\mathrm{vol}_W(a)$.

The DGGW bibliography (PDF p. 34) prints the Donnelly references exactly as follows **[text-extracted]**:

> [10] H. Donnelly, Spectrum and the fixed point sets of isometries I, Math. Ann. 224 (1976), 161–170.
> [11] H. Donnelly, Asymptotic expansions for the compact quotients of properly discontinuous group actions, Illinois J. Math. 23 (1979), 485–496.

**Crossref and Unpaywall results for Donnelly:**

- [10]: Crossref DOI **10.1007/bf01436198**, "Spectrum and the fixed point sets of isometries. I", *Mathematische Annalen* 224(2), pp. 161–170, issued 1976-04. Unpaywall reports `is_oa: false`, `oa_status: closed`, with no open copy, so the full text was not retrieved (see Unreachable).
- [11]: Crossref DOI **10.1215/ijm/1256048110**, "Asymptotic expansions for the compact quotients of properly discontinuous group actions", *Illinois Journal of Mathematics* 23(3), issued 1979-09-01. The Crossref record has no page field. Unpaywall reports `is_oa: true` (bronze, publisher-hosted). The PDF was retrieved (12 pages, printed pp. 485–496, scan with OCR layer). The relevant parts are quoted next.

**Donnelly 1979, Theorem 5.2** (printed p. 494, PDF p. 10) **[image-confirmed; OCR text was garbled, so this transcription is from the image]**:

> THEOREM 5.2. Let $\Gamma$ be a discrete subgroup of $SL(2,R)$ acting on the Poincaré upper half plane $H$ with compact quotient $\bar H = \Gamma\backslash H$. Then in the expansion
> $$\sum_{i=1}^\infty e^{-t\lambda_i} \sim (4\pi t)^{-1}\sum_{i=0}^\infty a_i t^i$$
> of Theorem 5.2, one has
> $$a_0 = \mathrm{vol}(\bar H),\qquad a_1 = \frac{-\mathrm{vol}(\bar H)}{3} + \sum_{\gamma^m=1}\sum_{j=1}^{m-1}\frac{1}{4m}\left(\frac{1}{\sin^2(j/m)}\right)$$
> where the sum is over primitive elliptic elements of order $m$ having a fixed point in the support of a suitably chosen partition of unity for $\Gamma$. The higher order terms may be obtained by expanding certain elementary functions in their Taylor series.

Transcription notes: the theorem reads "of Theorem 5.2" as printed. The denominator is printed as "$\sin^2(j/m)$". The proof uses $\omega = \pi/m$ and $\sin^2(j\omega)$ (eq. (5.5)), so "$j/m$" is presumably $j\pi/m$. This is a reading, not a correction made by the source.

**Donnelly 1979, identity-element (smooth) term, proof of Theorem 5.2** (printed p. 495, PDF p. 11) **[image-confirmed]**:

> The integral corresponding to the identity element behaves asymptotically as
> $$\int_H E(t,z,z)\phi(z)\,dz = \mathrm{vol}(\bar H)\,e^{-t/4}(4\pi t)^{-3/2}\int_0^\infty \frac{b e^{-b^2/4t}\,db}{\sinh(b/2)}.$$
> Thus
> $$(5.3)\qquad \int_H E(t,z,z)\phi(z)\,dz \sim \mathrm{vol}(\bar H)(4\pi t)^{-1}\big(1 - \tfrac13 t + O(t^2)\big)$$
> The higher order terms may be obtained by expanding $b/\sinh(b/2)$ in its Taylor series about $b=0$ and using the elementary integral formula [12, p. 426] ...

In this formula the whole smooth-part contribution for curvature $-1$ is $\mathrm{vol}(\bar H)$ multiplied by a function of $t$ alone. The $t$-dependence does not depend on $\Gamma$.

### A(iii). §5.6 / (5.7): 2-orbifold heat invariants, area, and Euler characteristic

**Example 5.6, degree-zero term, orientable case** (PDF p. 24) **[image-confirmed]**:

> 5.6. EXAMPLE. Calculating heat invariants for 2-orbifolds.
> **Degree zero term for orientable 2-orbifolds.** An orientable 2-orbifold $\mathcal{O}$ can have only isolated singularities, i.e., cone points. Suppose $\mathcal{O}$ has $k$ cone points of orders $m_1,\dots,m_k$. In the notation of 4.7(iii),
> $$I_0 = \frac{1}{4\pi}\big(a_0 t^{-1} + a_1 + O(t)\big).$$
> Thus by Theorem 4.8 and Proposition 5.5, the term of degree zero in the asymptotic expansion in Theorem 4.8 is given by
> $$\frac{a_1}{4\pi} + \sum_{i=1}^k \frac{1}{m_i}\frac{m_i^2-1}{12}.$$
> By the Gauss-Bonnet Theorem (valid also for orbifolds; see [26, 30]), we have
> $$a_1 = \frac{2\pi}{3}\chi(\mathcal{O}).$$
> Hence the degree zero term is
> $$(5.7)\qquad \frac{\chi(\mathcal{O})}{6} + \sum_{i=1}^k \frac{m_i^2-1}{12 m_i}.$$

**Proposition 5.5** (PDF p. 24) **[image-confirmed]**: "*Let $\mathcal{O}$ be a 2-orbifold, let $p$ be a cone point in $\mathcal{O}$ of order $m$ and let $N=\{p\}$. Then in the notation of Theorem 4.8, we have $I_N = \frac{m^2-1}{12} + O(t)$.*"

**Degree-one term (5.9)/(5.10)** (PDF p. 26) **[image-confirmed]**:

> $$(5.9)\qquad \frac{a_2}{4\pi} + \sum_{i=1}^k \frac{1}{m_i}\left(\sum_{j=1}^{m_i-1}\frac{R_{1212}}{8\sin^4(\frac{j\pi}{m_i})}\right) + \sum_{i=1}^r \frac{1}{2n_i}\left(\sum_{j=1}^{n_i-1}\frac{R_{1212}}{8\sin^4(\frac{j\pi}{n_i})}\right).$$
> Recall that $a_2(\mathcal{O}) = \frac{1}{360}\int_{\mathcal{O}}(2|R|^2 - 2|\rho|^2 + 5\tau^2)\,d\,\mathrm{vol}_{\mathcal{O}}(g)$, where $R$ is the curvature, $\rho$ is the Ricci curvature, and $\tau$ is the scalar curvature of $\mathcal{O}$ (e.g. [2]).
> ...
> $$(5.10)\qquad \frac{a_2}{4\pi} + \sum_{i=1}^k \frac{R_{1212}(m_i^4+10m_i^2-11)}{360 m_i} + \sum_{i=1}^r \frac{R_{1212}(n_i^4+10n_i^2-11)}{720 n_i}.$$

**Proposition 5.20, proof** (PDF p. 33) **[image-confirmed]**, the constant-curvature case:

> 5.20. PROPOSITION. *Within the class of closed 2-orbifolds of constant nonzero curvature $R$ or $-R$ the spectrum determines the sign of the curvature, i.e. whether the orbifold is spherical or hyperbolic.*
> *Proof.* ... Now look at the coefficient of the $t$ term in the expansion, as in (5.10), which reduces to
> $$\frac{a_2}{4\pi} \pm R\left(\sum_{i=1}^k \frac{(m_i^2+11)(m_i^2-1)}{360 m_i} + \sum_{i=1}^r \frac{(n_i^2+11)(n_i^2-1)}{720 n_i}\right)$$
> in the presence of constant curvature. The $\frac{1}{t}$ term in the expansion tells us $\mathrm{vol}(\mathcal{O})$ and we know the size of the curvature, so we know the $a_2$ component and may subtract it off. ... In this case, examine the degree zero term, which now has no point contributions and reduces to $\frac{a_1}{4\pi} = \frac{\chi(\mathcal{O})}{6}$, and we can read off the Euler characteristic.

**The spectral invariant $c$ and genus** (PDF pp. 27, 30) **[image-confirmed]**:

> Let $\mathcal{O}$ be an orientable 2-orbifold with $k$ cone points of orders $m_1,\dots,m_k$, denoted $\mathcal{O}(m_1,\dots,m_k)$, and consider the quantity $c$ defined as 12 times the degree zero term:
> $$(5.13)\qquad c = 2\chi(\mathcal{O}) + \sum_{i=1}^k\left(m_i - \frac{1}{m_i}\right).$$
> This quantity is a spectral invariant; note that it depends only on the topology, not on the Riemannian metric.

> (Proof of Theorem 5.15, p. 30) ... In addition, $c(2,2,2,2)=6$, $c(S^2)=4$, and $c(T^2)=0$. Let $S_g$ be a Riemann surface of genus $g\ge 2$. Then we also have $c(S_g) = 4-4g$.

This is the only occurrence of "genus" in the extracted DGGW text.

**Euler characteristic convention** (PDF p. 23) **[image-confirmed]**: "The Euler characteristic of a 2-orbifold is 2 minus the sum of the related values: each cone point of order $n$ has value $\frac{n-1}{n}$; each dihedral corner reflector has value $\frac{n-1}{2n}$; each handle has value 2; each cross-cap has value 1; and each mirror reflector has value 1."

**Remark 5.16** (PDF p. 31) **[image-confirmed]**: "Notably absent from the class $C$ are triangular pillows with $\chi(\mathcal{O})<0$. The invariant $c$ does not seem sufficiently strong to distinguish among these triangular pillows. However, as a special case of a result in [13], the spectrum does determine the orders of the cone points in such a 2-orbifold, provided that it is endowed with a metric of constant curvature $-1$." Here [13] is Dryden–Strohmaier.

**Classical manifold normalization in dimension 2.** DGGW do not print a separate manifold formula of the form "$a_0 = \mathrm{Area}/(4\pi)$, $a_1 = \chi/6$". What they print is:

- $I_0 = \frac{1}{4\pi}(a_0 t^{-1} + a_1 + O(t))$, with $a_0 = \mathrm{vol}(\mathcal{O})$ and $a_1 = \frac16\int\tau$, where $\tau$ is the scalar curvature, equal to $2K$ in dimension 2.
- $a_1 = \frac{2\pi}{3}\chi(\mathcal{O})$, so $\frac{a_1}{4\pi} = \frac{\chi(\mathcal{O})}{6}$ (p. 25 text and p. 33).
- Table 1 (PDF p. 28) **[text-extracted]** lists, for example, "torus, Klein bottle: $V\frac1t + O(t)$", with footnote "$V = \frac{\mathrm{vol}(\mathcal{O})}{4\pi}$".

In this normalization the leading coefficient is $\mathrm{Area}/(4\pi)$ multiplying $t^{-1}$, and the $t^0$ smooth coefficient is $\chi/6$, which equals $\frac{1}{12\pi}\int K$.

### What is fetched vs. what is inferred

**Fetched (verbatim in a retrieved source):**

1. DGGW Thm 4.8 and Def 4.7(iii): the principal or smooth part $I_0$ is $(4\pi t)^{-\dim/2}\sum_k a_k(\mathcal{O})t^k$ with $a_k = \int_{\mathcal{O}} u_k(x,x)\,d\mathrm{vol}$. The $u_k$ are "the invariants $u_i$ in (3.5), which are defined in terms of the curvature and its covariant derivatives on any Riemannian manifold". (3.5) calls them "local Riemannian invariants".
2. DGGW use the word "universal" only for Donnelly's singular-stratum functions $\widetilde b_k$, not for the $u_k$. Those are "an $O(m)\times O(n-m)$ universal invariant polynomial in the components of $B_\gamma$ and in the curvature tensor $R$ of $M$ and its covariant derivatives" (p. 16).
3. DGGW (5.7) and Prop 5.20: the smooth $t^0$ term of a 2-orbifold is $\frac{a_1}{4\pi} = \frac{\chi(\mathcal{O})}{6}$. At constant curvature of known size, the smooth $t^1$ term $a_2$ is fixed by the volume ("we know the size of the curvature, so we know the $a_2$ component").
4. **Uçar (B1), Thm 4.20(i), eq. (4.35)** **[image-confirmed]**: for a closed 2-orbifold of constant curvature $\kappa$, $a_\nu(\mathcal{O}) = \frac{\mathrm{vol}(\mathcal{O})}{\nu!\,4^\nu}\sum_{\ell=0}^\nu\binom{\nu}{\ell}(-4)^\ell B_{2\ell}(\tfrac12)\,\kappa^\nu$ **for all $\nu$**. This is the explicit statement that every smooth-stratum coefficient is a fixed ($\nu$- and $\kappa$-dependent) multiple of the area. Uçar's proof (p. 133, PDF p. 138) says: "In general, for any $\nu\in\mathbb{N}_0$ there exists a universal polynomial in the Gaussian curvature and its covariant derivatives such that the heat invariant $a_\nu(M)$ for any two-dimensional closed Riemannian manifold $M$ is given as the integral of that polynomial over $M$ (see e.g. [BG90]). ... The covariant derivatives of the Gaussian curvature vanish if the Gaussian curvature is constant. So in this case, the polynomial is just a monomial of the form $\alpha_\nu\kappa^\nu$". The Thm 4.20 proof (p. 138) adds: "Part (i) is clear from Corollary 4.16 since $a_\nu(\mathcal{O})$ is the integral over $\mathcal{O}$ of the same curvature invariant as for manifolds."
5. Donnelly 1979 eq. (5.3) and the display above it: for $\kappa = -1$ the identity-element term is $\mathrm{vol}(\bar H)$ times a function of $t$ alone.
6. Schueth (B4, arXiv:1812.06119, p. 3) **[image-confirmed]**: "since the only curvature invariant of order $2\ell$ in the case of constant curvature is $K^\ell$".
7. arXiv:2311.00337 p. 6 **[image-confirmed]**: "the so-called heat invariants, are integrals over $M$ of universal polynomials in the curvature and its covariant derivatives. (See, for example, [Pat70] and references therein.) ... The universal expressions defining the $a^p_j$ make sense on Riemannian orbifolds as well as on manifolds."

**Inferred (not stated in this form by any fetched source):**

- "At constant curvature every smooth-stratum heat coefficient is a fixed multiple of the area" is stated explicitly, with an explicit multiple, only by Uçar Thm 4.20(i). DGGW alone give it only for $a_0$, $a_1$, and (via Prop 5.20's proof) $a_2$. For all $k$ it follows from DGGW Def 4.7(iii) **combined with** the universality and polynomiality of $u_k$. DGGW do not state that property in those words; Uçar (citing [BG90]) and 2311.00337 (citing [Pat70]) do.
- "So genus enters the heat data only through the area" is an inference that no fetched source states. The step: by Gauss–Bonnet (DGGW p. 24; Uçar (4.38); D–S Thm 3.2), $\kappa\cdot\mathrm{Area} = 2\pi\chi(\mathcal{O})$ with $\chi(\mathcal{O}) = \chi(X_{\mathcal{O}}) - \sum(1 - 1/m_i)$. At fixed $\kappa$ the smooth part therefore depends on the genus only through $\chi(\mathcal{O})$, that is, through the area. The singular-stratum terms depend only on cone orders and $\kappa$ (Uçar Thm 4.20(ii) and Remark; DGGW Prop 5.5 and (5.10)) and do not involve the genus. The closest fetched statement is D–S p. 5: "since the orbifold Euler characteristic involves both the genus of the underlying surface and the orders of the cone points in the orbisurface, it is not immediately clear that the spectrum determines the genus."

---

## B1. Uçar, "Spectral invariants for polygons and orbisurfaces" (arXiv:1711.03405)

**Bibliographic record (arXiv API):** Eren Ucar, "Spectral invariants for polygons and orbisurfaces", arXiv:1711.03405v1, published 2017-11-09, math.DG. arXiv comment: "This is my dissertation, which is published here: https://edoc.hu-berlin.de/handle/18452/19142". The API record has no journal_ref or DOI, and Crossref was not queried for it. Page offset: printed page = PDF page − 5 in Chapter 4.

**Abstract** (PDF p. 2, printed ii) **[text-extracted]**:

> ... Furthermore, we compute the asymptotic expansion of the heat trace for any closed Riemannian orbisurface of constant curvature as $t \searrow 0$, and obtain explicit formulas for all heat invariants. ... If the curvature does not vanish, then it is possible to detect interesting information about the topology and the singular set of an orbisurface from the heat invariants. For example, we prove that if two orientable orbisurfaces with the same curvature $\kappa \ne 0$ are isospectral, then they must be homeomorphic. This result was previously known for $\kappa=-1$ but it was proven differently, namely by using the Selberg trace formula for the wave kernel and Weyl's asymptotic law ([DS09]).

**Introduction summary** (PDF p. 9, printed 4) **[text-extracted]**:

> ● The spectrum of any orbisurface $\mathcal{O}$ with constant nonzero curvature fixes the value of the sum $M + 2N$, where $M$ denotes the number of all dihedral points and $N$ denotes the number of all cone points of $\mathcal{O}$. Furthermore, the spectrum determines the multiset $\{m_1,\dots,m_M,n_1,n_1,\dots,n_N,n_N\}$, ... (see Corollary 4.21 (iii)).
> ● If two orientable orbisurfaces with constant curvature $\kappa \ne 0$ are isospectral, then the orbifolds have the same Euler characteristic, and the underlying topological spaces are homeomorphic (see Corollary 4.23). This generalises a result of [DS09] in which the same result was proven in case of constant curvature $\kappa=-1$ using the Selberg trace formula for the wave kernel.
> ● Within various classes of orbifolds, the spectrum determines the singular set and the Euler characteristic of the orbifold as well as the Euler characteristic of the underlying topological space (see Corollary 4.24 and Corollary 4.25).

**Theorem 4.11** (PDF p. 132, printed 127) **[text-extracted]**: "The following theorem is a special case of Theorem 4.8 in [DGGW08]." This is the 2-dimensional restatement of DGGW Thm 4.8, with $I_0(\mathcal{O}) = (4\pi t)^{-1}\sum a_i(\mathcal{O})t^i$.

**Corollary 4.16 and the remark after it** (PDF p. 138, printed 133) **[image-confirmed]**:

> $$(4.23)\qquad a_\nu(M) = \int_M \sum_{\ell=0}^\nu \frac{1}{4^{\nu-\ell}(\nu-\ell)!}\frac{(-1)^\ell}{\ell!}B_{2\ell}\left(\tfrac12\right)\cdot\kappa^\nu\,dx.$$
> The last formula for the coefficient $a_\nu(M)$ is universal in the sense that the heat coefficients for any two-dimensional closed Riemannian manifold $M$ of constant Gaussian curvature $\kappa$ are given by that formula.
> ...
> In general, for any $\nu\in\mathbb{N}_0$ there exists a universal polynomial in the Gaussian curvature and its covariant derivatives such that the heat invariant $a_\nu(M)$ for any two-dimensional closed Riemannian manifold $M$ is given as the integral of that polynomial over $M$ (see e.g. [BG90]). More precisely, that polynomial is a so-called curvature invariant of order $2\nu$. The covariant derivatives of the Gaussian curvature vanish if the Gaussian curvature is constant. So in this case, the polynomial is just a monomial of the form $\alpha_\nu\kappa^\nu$, and since it is universal, the case of $M = S^2(r)$ tells us that $\alpha_\nu$ equals $i^S_{\nu-1}$. Thus the formula (4.23) must hold for any two-dimensional Riemannian manifold of constant curvature $\kappa$.

The continuation on PDF p. 139 is **[text-extracted]**.

**Theorem 4.20** (PDF pp. 142–143, printed 137–138) **[image-confirmed]**:

> **Theorem 4.20.** *Let $\mathcal{O}$ be a two-dimensional closed Riemannian orbifold of constant curvature $\kappa\in\mathbb{R}$. Then, with $C$ as in (4.33) we have:*
> *(i)* $$a_\nu(\mathcal{O}) = \frac{\mathrm{vol}(\mathcal{O})}{\nu!\cdot 4^\nu}\sum_{\ell=0}^\nu\binom{\nu}{\ell}(-4)^\ell B_{2\ell}\left(\tfrac12\right)\cdot\kappa^\nu \quad\text{for all } \nu\in\mathbb{N}_0. \qquad (4.35)$$
> *(ii) If $N$ consists of a cone point of order $k\in\mathbb{N}$, then $\frac{I_N(\mathcal{O})}{|\mathrm{Iso}(N)|} = C$.*
> *(iii) If $N$ consists of a dihedral point of order $2k\in\mathbb{N}$, then $\frac{I_N(\mathcal{O})}{|\mathrm{Iso}(N)|} = \frac12 C$.*
> *(iv) If $N$ is a mirror edge of length $|N|$, then* $$\frac{I_N(\mathcal{O})}{|\mathrm{Iso}(N)|} = \frac{|N|}{\sqrt{4\pi t}}\sum_{\nu=0}^\infty\frac{1}{4^{\nu+1}\cdot\nu!}\cdot\kappa^\nu\cdot t^\nu. \qquad (4.36)$$
> *Proof.* Part (i) is clear from Corollary 4.16 since $a_\nu(\mathcal{O})$ is the integral over $\mathcal{O}$ of the same curvature invariant as for manifolds. The remaining statements follow from Corollary 4.19 ... via the following fact; see [Don76, Theorem 5.1], cited also in [DGGW08]: The functions $b_i(\gamma,x)$, whose integrals over $N$ make up the coefficients in $I_N(\mathcal{O})$, are of the form $\varphi(\gamma,x)\cdot\psi(\gamma,x)$, where $\varphi(\gamma,x)$ only depends on the Euclidean isometry $d\gamma_x$ and $\psi(\gamma,x)$ is a universal polynomial in the curvature tensor of $\mathcal{O}$ and its covariant derivatives.

Here $C = \sum_{\nu}\sum_{\ell=0}^\nu \frac{2}{4^\ell\,\ell!}c^S_{\nu-\ell}(\frac{\pi}{k})\kappa^\nu t^\nu$ (4.33, image-confirmed). It depends only on $k$ and $\kappa$.

Consistency check, done by hand and not stated by the source: (4.23) and (4.35) agree term by term, since $\binom{\nu}{\ell}(-4)^\ell/(\nu!\,4^\nu) = (-1)^\ell/(\ell!(\nu-\ell)!\,4^{\nu-\ell})$.

**Corollary 4.21** (PDF p. 144, printed 139) **[image-confirmed]**:

> **Corollary 4.21.** *Let $\mathcal{O}$ be a closed orbisurface of constant curvature $\kappa\in\mathbb{R}$. Let $M\in\mathbb{N}_0$ denote the number of dihedral points of $\mathcal{O}$ and let $2m_1,\dots,2m_M$ denote their individual orders, where $m_1,\dots,m_M\in\mathbb{N}$. Similarly, let $N\in\mathbb{N}_0$ denote the number of cone points and $n_1,\dots,n_N\in\mathbb{N}$ their orders. Then:*
> *(i) The volume of $\mathcal{O}$ and the length of the mirror locus are spectral invariants.*
> *(ii) If the mirror locus is non-trivial, i.e. the length of the mirror locus is positive, then the curvature of the orbifold is determined by the spectrum.*
> *(iii) If $\kappa\ne0$, then $\kappa$ together with the spectrum determines the number $M+2N$ as well as the multiset $\{m_1,\dots,m_M,n_1,n_1,n_2,n_2,\dots,n_N,n_N\}$.*
> *(iv) If the mirror locus is trivial and $\kappa\ne0$, then $\kappa$ together with the spectrum determines the number of cone points as well as the multiset of all orders $\{n_1,\dots,n_N\}$. (Note that trivial mirror locus implies absence of dihedral points.)*

Just before the corollary, PDF p. 143 **[image-confirmed]**: "Therefore we obtain, just as in Corollary 3.38 and Theorem 3.40, the following spectral invariants:"

**Definition 4.22, eq. (4.37), and Gauss–Bonnet (4.38)** (PDF p. 144) **[image-confirmed]**:

> $$\chi(\mathcal{O}) := \chi(X_{\mathcal{O}}) - \frac12\sum_{i=1}^M\left(1-\frac{1}{m_i}\right) - \sum_{i=1}^N\left(1-\frac{1}{n_i}\right). \qquad (4.37)$$
> ... $\int_{\mathcal{O}}\kappa\,dA = 2\pi\chi(\mathcal{O})$. (4.38) If the curvature is constant then the Gauß-Bonnet formula reduces to the equation $\mathrm{vol}(\mathcal{O})\kappa = 2\pi\chi(\mathcal{O})$. As we see, it follows from Corollary 4.21 (i) that two isospectral orbisurfaces have the same curvature if and only if they have the same Euler characteristic.

**Corollary 4.23 and the text after it** (PDF p. 145, printed 140) **[image-confirmed]**:

> **Corollary 4.23.** *Let $\mathcal{O}$ be a closed orientable orbisurface with constant curvature $\kappa\ne0$. Then $\kappa$ together with the spectrum of $\mathcal{O}$ determines the Euler characteristic of $\mathcal{O}$ as well as the Euler characteristic of the underlying space $X_{\mathcal{O}}$.*
> ... Hence, Corollary 4.23 implies that if two closed orientable orbisurfaces of constant curvature $\kappa\ne0$ are isospectral, then they have the same underlying topological space, i.e. the underlying topological spaces are homeomorphic. This fact was previously known in the special case of closed orientable orbisurfaces of constant curvature $\kappa=-1$ (see [DS09, Proposition 3.3]). ... Thus, Corollary 4.23 is a new proof of [DS09, Proposition 3.3] using only heat invariants, in addition to being a generalisation of it.
> Suppose now that the mirror locus of the orbisurface $\mathcal{O}$ is not trivial. ... Unfortunately it is not possible in general to detect which elements of the multiset in Corollary 4.21 (iii) correspond to dihedral points and which to cone points.

**Corollaries 4.24 and 4.25** (PDF pp. 145–146) **[4.24 image-confirmed; 4.25 text-extracted]**:

> **Corollary 4.24.** *Let $\mathcal{D}_\kappa,\mathcal{C}_\kappa$ denote the set of all orbisurfaces with constant curvature $\kappa\ne0$ and without any cone point, respectively dihedral point. Within each of these classes the spectrum determines $\chi(\mathcal{O})$, $\chi(X_{\mathcal{O}})$, and the singular set of the orbifold; ...*

> **Corollary 4.25.** *Let $\mathcal{A}_1$ denote the class of all orbisurfaces with constant nonzero curvature which have at least one dihedral point and at least one cone point and satisfy the following condition: Any two dihedral points, respectively any two cone points, have different orders. Then within $\mathcal{A}_1$, the spectrum again determines $\chi(\mathcal{O})$, $\chi(X_{\mathcal{O}})$, the length of the mirror locus, the number of dihedral points with their order, and the number of cone points with their orders.*

**How many heat invariants the argument uses.** Cor 4.21 is proved "just as in ... Theorem 3.40". The proof of Theorem 3.40 (PDF pp. 103–104, printed 98–99, **[text-extracted]**) uses the whole infinite sequence of coefficients:

- "Because the Gaussian curvature is not zero, there are infinitely many nonvanishing heat invariants."
- "we conclude by induction that the spectrum determines the sequence $(W_\nu)_{\nu\in\mathbb{N}_0}$"
- The smallest angle is recovered via "$\lim_{\nu\to\infty}\gamma^{2\nu+1}\cdot W_{\nu,1}$".

**Search note:** a full-text search of the extracted Uçar text found **zero** occurrences of "genus", "signature", "handle", "cross-cap", or "crosscap". It found "orbisurface" 76×, "heat invariant" 96×, "Euler characteristic" 21×, "isospectral" 32×, "number of" 32×, "underlying space" 4×, and "homeomorphic" 4×.

**What it states about genus.**
(a) The results use **all** heat invariants (the full coefficient sequence, through $\nu\to\infty$ limits), not finitely many. Uçar says Cor 4.23 uses "only heat invariants" as opposed to the wave trace.
(b) Uçar never uses the word "genus". For **closed orientable** orbisurfaces of constant curvature $\kappa\ne0$ with $\kappa$ known, the full sequence of heat invariants determines $\chi(\mathcal{O})$, the number of cone points and their orders, and hence $\chi(X_{\mathcal{O}})$. The underlying spaces of isospectral examples are homeomorphic. Equivalently the genus is determined, because $\chi(X_{\mathcal{O}}) = 2-2g$; that equivalence is a standard step Uçar does not write out. Nothing is stated about finitely many invariants, and nothing for $\kappa=0$.

---

## B2. Dryden–Strohmaier, "Huber's theorem for hyperbolic orbisurfaces" (arXiv:math/0504571)

**Bibliographic record:**

- **arXiv API**: Emily B. Dryden, Alexander Strohmaier, "Huber's theorem for hyperbolic orbisurfaces", arXiv:math/0504571v2 (v1 2005-04-28; v2 updated 2007-07-30). journal_ref: "Canadian Mathematical Bulletin, 52, pp.66-71, 2009"; DOI 10.4153/CMB-2009-008-0.
- **Crossref** (`/works/10.4153/CMB-2009-008-0`): "Huber's Theorem for Hyperbolic Orbisurfaces", *Canadian Mathematical Bulletin* 52(1), pp. 66–71, published-print 2009-03-01, Canadian Mathematical Society. Crossref returns the DOI in lower case: 10.4153/cmb-2009-008-0.
- The quotes are from arXiv v2. Printed page = PDF page (preprint pagination, not the journal's).

**Abstract** (PDF p. 1) **[text-extracted]**:

> We show that for compact orientable hyperbolic orbisurfaces, the Laplace spectrum determines the length spectrum as well as the number of singular points of a given order. The converse also holds, giving a full generalization of Huber's theorem to the setting of compact orientable hyperbolic orbisurfaces.

Definition of "hyperbolic" (PDF p. 1) **[text-extracted]**: "By "hyperbolic" we will mean that the object is endowed with a Riemannian metric of constant curvature -1."

**Theorem 1.1** (PDF p. 2) **[image-confirmed]**:

> **Theorem 1.1.** *Let $O$ be a compact orientable hyperbolic orbisurface. The Laplace spectrum of $O$ determines its length spectrum and the number of cone points of each possible order. Knowledge of the length spectrum and the number of cone points of each order determines the Laplace spectrum.*
> Shortly after preparing this manuscript, we learned that P. Doyle and J. P. Rossetti had proven this result independently (cf. [1]).

Method (PDF p. 2) **[image-confirmed]**: "Our proof of the first statement is based on the Selberg trace formula for the wave kernel".

**§3 Consequences: Definition 3.1, Theorem 3.2, Proposition 3.3** (PDF p. 5) **[image-confirmed]**:

> **Definition 3.1.** *Let $O$ be an orbisurface with $s$ cone points of orders $m_1,\dots,m_s$. Then we define the (orbifold) Euler characteristic of $O$ to be*
> $$\chi(O) = \chi(X_O) - \sum_{j=1}^s\left(1-\frac{1}{m_j}\right),$$
> *where $\chi(X_O)$ is the Euler characteristic of the underlying topological space of $O$.*
> ...
> **Theorem 3.2.** *Let $O$ be a Riemannian orbisurface. Then $\int_O K\,dA = 2\pi\chi(O)$, where $K$ is the curvature and $\chi(O)$ is the orbifold Euler characteristic of $O$.*
> Since the volume of a Riemannian orbisurface is spectrally determined via Weyl's asymptotic formula (see [5]), we see that for a Riemannian orbisurface with given curvature, the spectrum determines the orbifold Euler characteristic. However, since the orbifold Euler characteristic involves both the genus of the underlying surface and the orders of the cone points in the orbisurface, it is not immediately clear that the spectrum determines the genus. In the case of compact orientable hyperbolic orbisurfaces, Theorem 1.1 says that the spectrum determines the orders of the cone points, and thus the genus. This observation proves
> **Proposition 3.3.** *Isospectral compact orientable hyperbolic orbisurfaces have the same underlying topological space.*

**Search note:** the extracted text has "genus" 3× (all in the p. 5 paragraph above), "signature" 0×, "heat invariant" 0×, "Euler characteristic" 6×, and "orbisurface" 25×.

**What it states about genus.**
(a) The result concerns the **full Laplace spectrum**, used through the Selberg/wave trace and Weyl's law, not heat invariants. The paper never uses the phrase "heat invariant".
(b) It **determines the genus** in the class of compact orientable hyperbolic ($K\equiv-1$) orbisurfaces: "the spectrum determines the orders of the cone points, and thus the genus". It also explicitly identifies the obstruction: "it is not immediately clear that the spectrum determines the genus" from area alone, because $\chi(O)$ mixes the genus with the cone orders. The paper says nothing about finitely many heat invariants.

---

## B3. arXiv:2311.00337

**Bibliographic record:**

- **arXiv API**: Katie Gittins, Carolyn Gordon, Ingrid Membrillo Solis, Juan Pablo Rossetti, Mary Sandoval, Elizabeth Stanhope, "Do the Hodge spectra distinguish orbifolds from manifolds? Part 2", arXiv:2311.00337v2 (v1 2023-11-01; v2 updated 2024-01-04), math.DG. Comment: "Small corrections made to previous arXiv submission. arXiv admin note: substantial text overlap with arXiv:2106.07882". The API record has no journal_ref and no DOI.
- **Crossref** (search, then `/works/10.1307/mmj/20236493`): same title and six authors, *Michigan Mathematical Journal*, DOI **10.1307/mmj/20236493**, volume "-1", issue "-1" (Crossref's placeholder for advance publication), issued/published-print 2026-01-01, no page field.
- Part 1, as printed in the arXiv bibliography as [GGK+23] **[text-extracted]**: "Katie Gittins, Carolyn Gordon, Magda Khalile, Ingrid Membrillo Solis, Mary Sandoval, and Elizabeth Stanhope. Do the Hodge Spectra Distinguish Orbifolds from Manifolds? Part 1. Michigan Mathematical Journal, pages 1 – 28, 2023." The Crossref search also returned Part 1 as DOI 10.1307/mmj/20216126, *Michigan Math. J.* vol. 74, issued 2024-07-01. That is a search hit only; the DOI was not fetched directly.

**Abstract** (arXiv API summary, which matches PDF p. 1, image-confirmed):

> In [GGK+23] we examined the relationship between the singular set of a compact Riemannian orbifold and the spectrum of the Hodge Laplacian on $p$-forms by computing the heat invariants associated to the $p$-spectrum. We showed that the heat invariants of the 0-spectrum together with those of the 1-spectrum for the corresponding Hodge Laplacians are sufficient to distinguish orbifolds from manifolds as long as the singular sets have codimension $\le 3$. This is enough to distinguish orbifolds from manifolds for dimension $\le 3$. Here we give both positive and negative inverse spectral results for the individual $p$-spectra considered separately. For example, we give conditions on the codimension of the singular set which guarantee that the volume of the singular set is determined, and in many cases we show by providing counterexamples that the conditions are sharp.

**Heat invariants are universal polynomials; Theorem 2.6** (PDF p. 6) **[image-confirmed]**:

> Recall if $\mathcal{O}$ has empty singular set then $\mathcal{O}$ is a closed Riemannian manifold, $M$, and the heat trace has a small-time asymptotic expansion
> $$(1)\qquad \sum_{j=0}^\infty e^{-\lambda_j^{(p)}t} \sim_{t\to0^+} (4\pi t)^{-d/2}\sum_{i=0}^\infty a_i^p(M)t^i,$$
> where the $a^p_j$, the so-called heat invariants, are integrals over $M$ of universal polynomials in the curvature and its covariant derivatives. (See, for example, [Pat70] and references therein.)
> In Section 3 of [GGK+23], the authors constructed the heat kernel and the heat trace for the orbifold case. The universal expressions defining the $a^p_j$ make sense on Riemannian orbifolds as well as on manifolds.
> ...
> **Theorem 2.6.** [Theorem 3.15, [GGK+23]] *Let $\mathcal{O}$ be a closed $d$-dimensional Riemannian orbifold, let $p\in\{1,\dots,d\}$ and let $0\le\lambda_1^{(p)}\le\lambda_2^{(p)}\le\dots\to+\infty$ be the spectrum of the Hodge Laplacian acting on smooth $p$-forms on $\mathcal{O}$. The heat trace yields an asymptotic expansion as $t\to0^+$ given by*
> $$(2)\qquad \sum_{j=1}^\infty e^{-\lambda_j^{(p)}t} \sim_{t\to0^+} I_0^p(t) + \sum_{N\in PS(\mathcal{O})}\frac{I_N^p(t)}{|\mathrm{Iso}(N)|},$$
> *where $PS(\mathcal{O})$ is the set of all primary singular $\mathcal{O}$-strata ... (3) $I_0^p(t) := (4\pi t)^{-d/2}\sum_{k=0}^\infty a_k^p(\mathcal{O})t^k$ ... (4) $I_N^p(t) := (4\pi t)^{-\dim(N)/2}\sum_{k=0}^\infty b_k^p(N)t^k$. The coefficients $b^p_k(N)$ are of the form $b^p_k(N) = \sum_{\gamma\in\mathrm{Iso}^{\max}(N)}\int_N b^p_k(\gamma,x)\,dV(x)$ where the $b^p_k$ are universal orthogonally invariant expressions in the germs of the Riemannian metric of $\mathcal{O}$ at $x$ and the action of $\gamma$.*

**Main results relevant to orbifold vs. manifold** (PDF pp. 2–4) **[text-extracted]**:

- Result 1.1.2: "In contrast, if $k$ is odd and $K^d_p(k)\ne0$, then the $p$-spectrum determines the volume of the singular set of each orbifold in $\mathrm{Orb}^d_k$. In particular, the $p$-spectrum distinguishes orbifolds in $\mathrm{Orb}^d_k$ from closed Riemannian manifolds. (See Theorem 4.4.)"
- p. 3: "For $p=0$, the Krawtchouk polynomial has no zeros, so Result 1.1 says that if the singular set has odd codimension, its volume is determined by the 0-spectrum ... Moreover, [DGGW08, Theorem 5.1] says that an orbifold that contains at least one singular stratum of odd codimension cannot be 0-isospectral to a manifold, even if the full singular set has even codimension."
- p. 2: "However, the question of whether the 0-spectrum always distinguishes Riemannian orbifolds with singularities from Riemannian manifolds remains open."
- Result 1.3 (p. 4): "We exhibit a family of five 1-isospectral flat 2-orbifolds (none of which are 0-isospectral) that have different types of singularities. (See Example 3.9.) ... 2. The underlying spaces of the various orbifolds include a sphere, a projective plane, and disks."
- Example 3.9 (pp. 10–11) lists classes ∗2222, 22∗, 22×, 2∗22, and 244. Remark 3.10 (p. 11): "The five orbifolds in Example 3.9 are all mutually distinguishable by their 0-spectra. This follows, for example, by comparing the heat invariants for these orbifolds using [DGGW08, Table 1] and the fact that the lengths of the mirror loci in the first, second and fourth orbifolds are mutually distinct."

**Search note:** a full-text search of the extracted text found **zero** occurrences of "genus", "signature", "orbisurface", "Euler characteristic", and "number of". It found "cone point" 7×, "heat invariant" 12×, and "isospectral" 72×.

**What it states about genus.**
(a) This is a Hodge $p$-spectrum paper. It uses heat invariants (finitely many leading singular-stratum coefficients such as $b^p_0$) to detect singular-set volume and to tell orbifolds from manifolds.
(b) It **says nothing about the genus** (no occurrence of "genus"). The relevant points are: (1) it states in general dimension that smooth heat invariants are integrals of universal curvature polynomials, citing [Pat70]; and (2) it gives a **1-spectrum** counterexample in which flat 2-orbifolds with different underlying spaces (sphere, projective plane, disks) are 1-isospectral. It notes these are distinguished by their 0-spectra.

---

## B4. arXiv full-text search hits

Method: `curl -L -X POST https://arxiv.org/search_classic --data-urlencode "query=<q>" --data-urlencode "searchtype=ft"`. All requests returned 200. The POST was redirected to `https://search.arxiv.org/?query=...`, and the pages were parsed as Latin-1 HTML. Queries and hit counts:

| Query | Hits |
|---|---|
| orbisurface genus heat invariants | 8 |
| heat invariants determine the genus orbifold | 196 |
| spectrum determines the signature orbisurface | 3 |
| isospectral orbisurfaces genus | 7 |
| heat invariants orbisurface cone points | 7 |
| spectrum determines genus orbifold | 238 |
| heat trace orbifold genus cone points | 158 |
| isospectral orbifolds different genus | 98 |
| heat invariants 2-orbifolds Euler characteristic | 190 |

The search engine matches any of the words, so the large-count queries were dominated by string theory and physics results. Only the first page (≤10 hits) of each query was inspected.

Relevant hits:

- **arXiv:1711.03405**, Uçar thesis. Hit by "heat invariants orbisurface cone points". Covered in B1.
- **arXiv:2106.07882**, Gittins–Gordon–Khalile–Membrillo Solis–Sandoval–Stanhope, "Do the Hodge spectra distinguish orbifolds from manifolds? Part 1" (2021). Hit by "heat invariants 2-orbifolds Euler characteristic". Part 1 of B3. Not fetched.
- **arXiv:1812.06119**, Dorothee Schueth, "On the corner contributions to the heat coefficients of geodesic polygons". arXiv API journal_ref: "Ann. Inst. Fourier 69 (2019), no. 7, 2827-2855"; the API record has no DOI. Fetched. The abstract (arXiv API) says it computes "formulas for the contribution of cone points of $\mathcal O$ to the coefficient at $t^2$ of the asymptotic expansion of the heat trace of $\mathcal O$, the contributions at $t^0$ and $t^1$ being known from the literature." Relevant quotes:
  - p. 2 **[text-extracted]**: "$u_1(p,p) = \frac16\mathrm{scal}_g(p)$" and "$u_2(p,p) = \frac{1}{360}(5\,\mathrm{scal}_g^2 - 2\|\mathrm{ric}_g\|^2 + 2\|R_g\|^2 - 12\Delta_g\mathrm{scal}_g)(p)$". The paper attributes both to Berger.
  - p. 3 **[image-confirmed]**: "Since those two contributions are, by Donnelly's structural theory, known to be determined by $\gamma=\pi/k$ and curvature invariants of appropriate order, and since the only curvature invariant of order $2\ell$ in the case of constant curvature is $K^\ell$, this implies that the coefficients must be of the form $e_\ell(\gamma)K^\ell$ here."
  - The extracted text has no occurrence of "genus" or "signature".
- **arXiv:1408.2001**, Benjamin Linowitz, John Voight, "Small isospectral and nonisometric orbifolds of dimension 2 and 3". The arXiv API record has no journal_ref or DOI. Hit by "isospectral orbisurfaces genus". Fetched. Relevant quotes:
  - Remark 2.6, p. 14 **[image-confirmed]**: "In fact, in dimension 2, a converse holds: the spectrum (2.1) of a 2-orbifold determines, and is determined by, the area, the number of elliptic points of each order, and the number of primitive closed geodesics of each length. This result was proven by Huber [53] for hyperbolic 2-manifolds and generalized by Doyle and Rossetti [32, 33] to non-orientable 2-orbifolds."
  - p. 2 **[text-extracted]**: "Finally, in 1994, Maclachlan and Rosenberger [61] claimed to have produced a pair of hyperbolic 2-orbifolds of genus 0 with orbifold fundamental groups of signature (0; 2, 2, 3, 3). However, Buser, Flach, and Semmler [14] later showed that these examples were too good to be true and that such orbifolds could not be Laplace isospectral."
  - The paper constructs isospectral pairs with the same signature, for example both of signature (0; 2,2,2,2,2,3,4) (p. 3, text-extracted). It concerns the full spectrum, not finitely many heat invariants.
- **arXiv:1609.05142**, Arias-Marco–Dryden–Gordon et al., "Spectral geometry of the Steklov problem on orbifolds". This is about the Steklov spectrum, not the Laplace heat trace. The search snippet says it "does not ... determine the orbifold Euler characteristic" (for Steklov). Not fetched; listed for completeness.
- Other hits (Jorgenson–Smajlovic–Spilioti 2512.16681; Bénard–Frahm–Spilioti 2110.06683; Takhtajan–Zograf 1701.00771; Taghavi–Naseh–Allameh 2310.17536; Aryasomayajula 1401.4682, 1310.4336, 1401.7126) concern zeta functions, torsion, Liouville action, or Green's function bounds on orbisurfaces. From their snippets, none states a genus- or signature-from-heat-invariants result. They were not fetched.

**Result of B4.** Among the first-page hits of these queries, no paper states that **finitely many** heat invariants determine the genus or signature of an orbisurface, and no paper gives a counterexample to it. The full-spectrum genus result is Dryden–Strohmaier (hyperbolic, orientable). The heat-invariant (full sequence) version for constant $\kappa\ne0$ with $\kappa$ known is Uçar Cor 4.23. Only first pages of OR-matching results were inspected, so this does not show that no such result exists.

---

## Unreachable

- **H. Donnelly, "Spectrum and the fixed point sets of isometries. I", Math. Ann. 224 (1976) 161–170, DOI 10.1007/bf01436198** (DGGW ref. [10]). Crossref resolved the record. Unpaywall `https://api.unpaywall.org/v2/10.1007/bf01436198` returned `is_oa: false`, `oa_status: closed`, `oa_locations: []`. As instructed, no further attempt was made at the paywalled full text. Donnelly's Thm 5.1 (the $b_0$, $b_1$ formulas and the universal-polynomial structure of $\widetilde b_k$) is therefore known here only as DGGW (p. 16) and Uçar (p. 138) report it. This is a gap in what could be retrieved, not evidence about the source's content.
- The Uçar dissertation's institutional copy (`https://edoc.hu-berlin.de/handle/18452/19142`, given in the arXiv comment) was not fetched. The arXiv PDF was used instead.
- The journal versions of DGGW (Michigan Math. J. 56), Dryden–Strohmaier (Canad. Math. Bull. 52), and arXiv:2311.00337 (Michigan Math. J., DOI 10.1307/mmj/20236493) were not fetched. Quotes are from the arXiv versions, and journal page numbers are not available, apart from Crossref's 66–71 for Dryden–Strohmaier.
