# Literature sweep: divergence, Borel summability and resurgence of heat-trace expansions on cones, orbifolds and constant-curvature surfaces

Date of sweep: 2026-10-01. All statements below about a paper are taken from text actually
retrieved (arXiv abstracts via the API, or PDF text extracted with PyMuPDF). Page numbers are PDF
page numbers unless marked "printed". Mathematical symbols inside quotations are transcribed from
the extracted text and may lose typography; the wording is verbatim.

## 1. Method

Endpoints used (headless HTTP only):
- arXiv API `https://export.arxiv.org/api/query?search_query=...` (abstract/title fields), 3 s between calls.
- arXiv full-text search `https://search.arxiv.org/?query=<words>&in=` (top 10 hits per query).
- arXiv PDFs `https://arxiv.org/pdf/<id>`; text extracted with `fitz` (PyMuPDF), then searched for
  `cone|conical|orbifold|elliptic|wedge`, `converg|diverg|asymptotic series|factorial|Borel|Gevrey|resurg|large order`.
- Crossref `https://api.crossref.org/works?query.bibliographic=...` for journal versions / DOIs.

arXiv API abstract queries (number of hits in parentheses):
`"heat kernel" AND resurgence` (4); `"heat kernel" AND Borel` (23); `"heat trace" AND Gevrey` (0);
`"heat kernel" AND Gevrey` (3); `"heat coefficients" AND factorial` (0); `"conical singularity" AND heat AND Borel` (0);
`orbifold AND "heat invariants"` (5); `"cosmic string" AND "heat kernel" AND "all orders"` (0);
`"large order" AND "heat kernel"` (1); `"Seeley-DeWitt" AND divergen*` (0); `"heat kernel coefficients" AND factorial` (0);
`"heat trace" AND resurgen*` (0); `"heat trace" AND orbifold` (4); `elliptic AND "Selberg trace formula" AND heat` (1);
`"heat kernel" AND cone AND asymptotic AND series` (1); `"heat kernel" AND "asymptotic series" AND divergent` (0);
`"heat kernel expansion" AND convergence` (5); `"Borel summable" AND heat` (6); `orbifold AND resurgence` (2);
`"cone point" AND heat` (3); `"cone points" AND "heat trace"` (2); `"conical singularities" AND "heat trace"` (8);
`"hyperbolic orbifold" AND heat` (0); `"heat kernel" AND "complex geodesics"` (3);
`"heat kernel" AND sphere AND asymptotic AND divergent` (1); `"heat kernel" AND resummation` (8);
`"Schwinger-DeWitt" AND "large order"` (0); `"heat kernel" AND Pade` (0); `wedge AND "heat trace" AND curvature` (0);
`"Selberg trace formula" AND "elliptic elements"` (4); `"elliptic degeneration" AND heat` (2); `"Hecke triangle" AND heat` (2);
author queries `Garbin AND Jorgenson`, `Dowker AND elliptic`, `Dowker AND orbifold`.

arXiv full-text queries: "heat kernel cone Borel summable"; "orbifold heat coefficients factorial growth";
"cone point heat trace divergent asymptotic series"; "elliptic terms Selberg heat kernel asymptotic expansion divergent";
"heat kernel coefficients grow factorially"; "cosmic string heat kernel coefficients all orders";
"conical singularity heat kernel resurgence"; "heat invariants orbifold cone points largest order";
"heat kernel cone coefficients asymptotic series not convergent"; "orbifold heat trace Borel transform singularity";
"heat trace smallest angle spectral invariant growth coefficients";
"elliptic contribution heat trace asymptotic expansion hyperbolic orbifold all orders";
"spherical polygon heat trace expansion divergent"; "heat kernel sphere Euler-Maclaurin asymptotic expansion divergent Bernoulli";
"Gevrey heat trace conic singularity".

Full texts read/searched: 2109.03897, 2606.21909, 2609.23608, 2605.03960, hep-th/9309050, 1711.03405,
2511.22255, 1812.06119, 0805.3148, 1603.01495, 2311.12708, 1301.7742, 2512.04422, 1107.3752.
Abstract only: 1302.0604, 1603.01494, 2005.02055, 2606.26637, 2511.03315, 1701.01874, 1711.00577, 2402.04107.

Coverage limits: arXiv plus Crossref metadata only. No MathSciNet/zbMATH, no Google Scholar, no
paywalled journal full texts, no books (e.g. monographs on heat kernels or Selberg trace formula).
The full-text engine returns only the top 10 hits per query and ranks many irrelevant 2026 items highly.

## 2. Directly relevant prior work

### 2.1 G. V. Dunne, "Borel Summation and Analytic Continuation of the Heat Kernel on Hyperbolic Space", arXiv:2109.03897 (2021); in Peter Suranyi 87th Birthday Festschrift (2022), DOI 10.1142/9789811262357_0010 (Crossref).
- Proves/derives: short-time expansion of the H^2 heat kernel K(t,rho) is factorially divergent; explicit Borel
  transform; Borel singularities u_k^± = −k^2 ± i k rho/pi (k = 1,2,...), a parabola on the negative axis (p. 2, eq. (5));
  diagonal expansion K(t,0) ~ e^{−t/4}/(2 pi^{3/2} t) Σ (−1)^n eta(2n) Gamma(n+1/2) (t/pi^2)^n (p. 6, eq. (25)).
- Quotes: "for even dimensional spaces the heat kernel expansions are divergent and have a rich structure, which can
  be derived from the 2-dimensional case [14]" (p. 1). "For a given ρ, the coefficients of the short time expansion (11)
  grow factorially fast in magnitude due to the Γ(n + 1/2) factor." (p. 3). "The expansion coefficients in (25) grow
  factorially fast in magnitude, and alternate in sign." (p. 6). "The geodesic expansion on S2 can be traced to the
  complex geodesics on H2, associated with the complex Borel singularities in (5)" (pp. 11–12).
- Scope: pointwise and diagonal heat kernel of H^2 (and S^2 by continuation t -> −t). The diagonal growth rate is
  (1/pi^2)^n, i.e. Borel singularity at distance pi^2 — the smooth (m = 1) case.
- Treats cones/orbifolds/elliptic terms: **no** (no occurrence of cone, conical, orbifold, elliptic, wedge in the text;
  Selberg appears only in reference titles [5], [14], [21]).

### 2.2 S. Li, Y. Li, X. Tang, "Heat Kernel and Resurgence", arXiv:2606.21909 (2026). No Crossref record found.
- Proves: for real-analytic (M,g), the local parametrix expansion is 1-Gevrey. "Theorem 2.5. Let (M, g) be real
  analytic. ... Then Σ_{j≥0} u_j(x, y)τ^j is 1–Gevrey power series uniformly for (x, y) ∈ V′ × V′ with V′ ⋐ V." (p. 11).
  Proposes a Picard–Lefschetz/alien-calculus correspondence; Borel singularities = action differences of holomorphic
  geodesics. On H^2: "The Borel singularities occur at ... ξ = (d + 2πik)^2/4 − d^2/4, k ∈ Z." (p. 7).
- Also treats the smooth S^2 heat trace (Example 2.30, pp. 29–30): Borel transform
  1 + 2 Σ_k (−1)^{k−1}[(1 − ξ/(k^2π^2))^{−1/2} − 1], obtained "Interchanging the two sums for |ξ| < π^2" (p. 30), so the
  nearest singularity is at ξ = π^2. Remark 2.28: "the affine complexification of S2 does not produce additional
  holomorphic geodesics between real endpoints" (p. 29).
- Treats cones/orbifolds/elliptic terms: **no** (no occurrence of cone point, conical, orbifold, elliptic element,
  quotient; "trace" occurs only for the S^2 heat trace).

### 2.3 X. Tang, "Resurgence and Complex Geodesics for the Heisenberg Heat Kernel", arXiv:2609.23608 (2026).
- Abstract: "the nonzero finite singularities reached by analytic continuation of the minimizing-saddle Borel germ are
  exactly the finite complex action differences ... Near the vertical axis, we obtain uniform two-term large-order
  asymptotics from the nearest Borel singularity." (p. 1). Sub-Riemannian, Heisenberg groups only.
- Treats cones/orbifolds/elliptic terms: **no** ("cone" occurs only as "closed angular cone" in the Borel plane, p. 7 ff.).

### 2.4 W. Shen, S. Sun, "Two Regularized Determinants of Laplacian through Resurgence theory", arXiv:2605.03960 (2026). No Crossref record found.
- Resurgence of the theta series Σ e^{−ρ_n t} (square-root spectrum) and 1-Gevrey asymptotics of a deformed
  determinant "whose coeﬀicients are determined by the trace of the heat kernel" (abstract, p. 1). Examples: S^1 and
  "Let X be a closed Riemann surface with genus g ≥ 2" (p. 28), via Cartier–Voros and the Selberg trace formula;
  singularities at k·(lengths of closed geodesics)·i and at −2πm.
- Does not study the short-time heat-coefficient sequence of the heat trace itself.
- Treats cones/orbifolds/elliptic terms: **no** (torsion-free compact surfaces only; no orbifold/elliptic-element text).

### 2.5 D. V. Fursaev, "The Heat Kernel Expansion on a Cone and Quantum Fields Near Cosmic Strings", arXiv:hep-th/9309050 (1993); Class. Quantum Grav. 11 (1994), DOI 10.1088/0264-9381/11/6/008 (Crossref).
- Flat cone of angle α; smeared trace Tr(e^{−sΔ_α} f) = (4πs)^{−1} Σ a_{α,n}(f) s^{n/2} + ES (p. 3, eq. (2.2)); apex
  coefficients via contour integrals C_n(α) (p. 5, eq. (2.12)); "this series includes half-integer powers of the proper
  time s" (p. 4). For f = 1 near the apex: "the series is truncated and one gets the expression exact up to the ES
  terms" (p. 6, eq. (2.16)), i.e. only the C_2(α) = (1/6)((2π/α)^2 − 1) term survives.
- No discussion of convergence/divergence or Borel properties. The flat cone has a terminating expansion; the
  curvature-coupled series is not studied (Appendix A treats zeta functions on a sphere with two conical points).
- Treats cones/orbifolds/elliptic terms: **yes** (flat cones; mentions orbifold factors, p. 2), but no divergence content.

### 2.6 E. Uçar, "Spectral invariants for polygons and orbisurfaces", arXiv:1711.03405 (PhD thesis, HU Berlin, 2017). No Crossref record found.
- Proves explicit closed forms for all corner/cone coefficients in constant curvature κ: V_κ(γ) = Σ e_ν(γ) κ^ν t^ν,
  e_ν(γ) a finite double sum of products of Bernoulli polynomials/numbers times (π^{2j} − γ^{2j})/(π γ^{2j−1})
  (Corollary 3.37, eq. (3.114), printed p. 94 / PDF p. 99). For orbifolds: "a cone point of order k contributes to the
  heat invariants of O as much as two angles of magnitude π/k to the heat invariants for a polygon of curvature κ."
  (printed p. 138 / PDF p. 143). Theorem 4.20 (printed pp. 137–138) gives all a_ν(O) and the cone/dihedral/mirror terms.
- **Large-order argument for the smallest angle (closest prior item to statement (B)).** Theorem 3.40 proof
  (printed pp. 98–99 / PDF pp. 103–104) isolates the top-degree part W_ν = Σ_i (π^{2ν+2} − γ_i^{2ν+2})/(π γ_i^{2ν+1})
  of Σ_i e_ν(γ_i), whose coefficient is (−1)^ν B_{2ν}/(4(ν+1)!(2ν+1)), then forms
  W_{ν,1} = Σ_i ((π/γ_i)^2 − 1)(1/γ_i)^{2ν+1}. Quotes: "We claim that the smallest angle can be deduced from the
  sequence (Wν,1)ν∈N0." (printed p. 98). "θ1 = inf {γ > 0 | γ^{2ν+1} · Wν,1 is convergent as ν → ∞ with nonzero limit}.
  So the magnitude of the smallest angle θ1 is a spectral invariant." (printed p. 99). Iterating recovers the whole
  multiset. Orbifold version, Corollary 4.21: "(iv) If the mirror locus is trivial and κ ≠ 0, then κ together with the
  spectrum determines the number of cone points as well as the multiset of all orders {n1,...,nN}." (printed p. 139 /
  PDF p. 144), with the remark "To the best of our knowledge, statement (iii) is a new result. Similarly, statement (iv)
  is also new in this generality and was only known for the special case of κ = −1".
- What it does NOT do (text search for converg/diverg/asymptotic series/factorial/Borel/Gevrey/resurg): no statement
  that V_κ(γ) or the cone series diverges, no growth rate of the full coefficient e_ν(γ) or b_ν(C), no Borel transform.
  The ν → ∞ limit is taken on the extracted top-degree, Bernoulli-stripped sequence W_{ν,1}, which grows only
  geometrically in 1/γ; the factorial factor is removed by hand.
- Treats cones/orbifolds/elliptic terms: **yes** (constant-curvature cone points, dihedral points, polygon corners).

### 2.7 D. Schueth, "Heat coefficients of surfaces with curved conical singularities", arXiv:2511.22255 (2025); Ann. Global Anal. Geom. (2025), DOI 10.1007/s10455-025-10024-1 (Crossref).
- Computes b_{1/2}(C) for rotationally symmetric curved cones; shows it is not rational in the rescaling parameter α.
  Summarises the orbifold case: "Uçar [13] obtained explicit formulas for all bℓ(C) for cone points C of two-dimensional
  orbifolds under the special assumption that the orbifold has constant curvature κ ∈ R. ... bℓ(C) can then be written as
  κ^ℓ times (1/n) pℓ(n), where n is the order of the cone point and pℓ is a certain polynomial of order 2ℓ + 2." (p. 2).
- Divergence content is in a different variable: "Theorem 4.6. The Taylor series T0F of F around 0 has convergence
  radius 0." (p. 19), where F(α) is the integral defining b_{1/2}(C) as a function of the cone parameter α — not the
  t-expansion. The proof uses factorial growth of Bernoulli numbers.
- Treats cones/orbifolds/elliptic terms: **yes**; divergence of the heat-coefficient sequence in t: **not discussed**.

### 2.8 D. Garbin, J. Jorgenson, "Heat kernel asymptotics on sequences of elliptically degenerating Riemann surfaces", arXiv:1603.01495 (2016); Kodai Math. J. (2020), DOI 10.2996/kmj/1584345689 (Crossref). Companion: arXiv:1603.01494, L'Enseignement Math. (2019), DOI 10.4171/lem/64-1/2-7 (Crossref).
- Exact elliptic term (Theorem 2.5, p. 10): ETrK_M(t) = e^{−t/4}/√(16πt) Σ_γ Σ_{n=1}^{q_γ−1} (1/q_γ)
  ∫_0^∞ e^{−u²/4t} cosh(u/2)/(sinh²(u/2) + sin²(nπ/q_γ)) du; compared with the classical form (Remark 2.6, pp. 12–13).
  Studies q → ∞ (elliptic degeneration) and small-time bounds uniform in q (Corollary 5.6, O(t^{−3/2})).
- No statement on the divergence, Borel transform or large-order behaviour of the t-expansion of the elliptic term
  (text search: only "diverg" hit is "The trace of the heat kernel alone diverges through degeneration", p. 26, about q → ∞).
- Observation (ours, from the fetched formula, not stated by the authors): the integrand is a Laplace transform in
  u²/4 whose nearest complex singularities are at u = ±2πi/q (n = 1 or q−1), i.e. at Borel distance π²/q² — consistent
  with growth l!(q²/π²)^l and with a "complex rotation by the smallest angle 2π/q" reading.
- Treats cones/orbifolds/elliptic terms: **yes** (elliptic fixed points of all orders); divergence: **no**.

### 2.9 E. Dryden, C. Gordon, S. Greenwald, D. Webb, "Asymptotic expansion of the heat kernel for orbifolds", arXiv:0805.3148 (2008); Michigan Math. J. 56 (2008), DOI 10.1307/mmj/1213972406; erratum DOI 10.1307/mmj/1488510034 (Crossref).
- Existence and structure of the orbifold heat-trace expansion; explicit low-order terms for 2-orbifolds; spectral
  distinction "within various classes of two-dimensional orbifolds" (abstract). Text search finds no discussion of
  divergence/growth of coefficients.
- Treats cones/orbifolds/elliptic terms: **yes**; divergence: **no**.

### 2.10 D. Schueth, "On the corner contributions to the heat coefficients of geodesic polygons", arXiv:1812.06119; Ann. Inst. Fourier (2020), DOI 10.5802/aif.3338 (Crossref).
- Computes the cone-point contribution at t² for general (non-constant-curvature) orbisurfaces (abstract). No
  occurrence of converg/diverg/factorial/Borel in the text. Treats cones/orbifolds: **yes**; divergence: **no**.

## 3. Adjacent work (smooth settings, physics, other variables)

- T. Hargé, arXiv:1301.7742 (2013), and arXiv:1302.0604 (2013): Borel summability of the small-time expansion for
  −Δ + V on R^ν (and vector potentials); "The expansion in (1.2) is not convergent in general." (1301.7742, p. 1).
  Smooth, flat, no cones. No Crossref record returned for either.
- G. V. Dunne, A. I. Farah, "Weak-Strong Resurgence Duality", arXiv:2606.26637 (2026), abstract only: short/long-time
  heat-trace expansions for a Gross–Neveu fluctuation operator. No cones/orbifolds in abstract.
- S. A. Franchino-Viñas et al., arXiv:2511.03315 (2025), abstract only: resummation of heat-kernel invariants in
  background gauge fields (physics; no cones).
- B. Liu, arXiv:2005.02055 (journal ref. per arXiv: Analysis & PDE 17 (2024)), abstract only: elliptic orbital
  integrals in the Selberg trace formula on locally symmetric orbifolds, used for analytic-torsion asymptotics along
  sequences of flat bundles; nothing on divergence of short-time coefficients in the abstract.
- J. S. Dowker, arXiv:2311.12708 (2023) "Casimir energy of elliptic fixed points" and arXiv:2402.04107 (2024): elliptic and
  hyperbolic contributions to Casimir energies on hyperbolic quotients; text search of 2311.12708 finds no statement on
  divergence of heat coefficients.
- A. Suleymanova, arXiv:1701.01874, 1711.00577 (2017); S. Looi, D. Sher, arXiv:2512.04422 (2025); G. Fucci, K. Kirsten,
  arXiv:1107.3752 (2011): heat-trace coefficients for conic singularities, curved corners, spherical suspensions. Text
  searches of 2512.04422 and 1107.3752 find no divergence/growth statements.
- Crossref also returned "Partial Summation of Schwinger-De Witt Expansion", Lecture Notes in Physics Monographs (2000),
  DOI 10.1007/3-540-46523-5_4 (not fetched; smooth-manifold resummation by title).

## 4. Verdict on novelty (within the sources fetched)

(A) b_l(m) ~ C(m) l! (m²/π²)^l for fixed m, with explicit constant.
No prior statement found in the sources fetched. Closest: Dunne (2.1) and Li–Li–Tang (2.2) give the smooth diagonal /
S² case (Borel singularity at π², i.e. m = 1); Uçar (2.6) gives closed forms for all cone coefficients but never states
their growth; Garbin–Jorgenson (2.8) give an exact integral for the elliptic term from which the rate can be read off,
but they do not do so. Schueth (2.7) proves zero radius of convergence in the cone parameter, not in t.

(B) The growth rate of an orbifold's heat coefficients determines the largest cone order.
The spectral invariance of the cone orders themselves is prior: Uçar, Corollary 4.21(iv) (constant curvature κ ≠ 0,
orientable case gives the whole multiset; κ = −1 attributed to earlier work), and it is proved by a ν → ∞ limit that
picks out the smallest angle first (Theorem 3.40, printed pp. 98–99). What was not found: the statement that the
factorial divergence rate of the full heat-coefficient sequence (as opposed to Uçar's Bernoulli-stripped top-degree
sequence W_{ν,1}) equals (m_max²/π²) and so determines m_max, or any use of a divergence rate as a spectral invariant.
Any write-up of (B) should cite Uçar's large-ν argument as the closest precedent and state the difference precisely.

(C) Borel singularity of the cone term at the smallest rotation angle (complex-geodesic interpretation).
No prior statement found in the sources fetched. The complex-geodesic/action-difference interpretation of Borel
singularities exists for smooth H² and S² (Dunne p. 12; Li–Li–Tang pp. 7, 29–30) and for Heisenberg groups (Tang),
none extended to cone points or elliptic elements. Garbin–Jorgenson's Theorem 2.5 integral exhibits the relevant
singularity structure without comment.

Search coverage caveat: arXiv (API + full text) and Crossref only, through 2026-10-01. Absence from these sources is
not proof of absence in the literature (journal-only papers, books, theses not on arXiv, and Watson 2005 were not
read).

## 5. Unreachable

- S. Watson, "The trace function expansion for spherical polygons", New Zealand J. Math. 34 (2005) 81–95 (citation as
  given in Uçar's bibliography, PDF p. 155). Crossref query `query.bibliographic=Watson trace function expansion
  spherical polygons` returned no matching record. Guessed archive URL
  `https://www.thebookshelf.auckland.ac.nz/docs/NZJMaths/nzjmaths034/nzjmaths034-02-004.pdf` returned HTTP 000 / no file.
  Site search `https://nzjmath.org/index.php/NZJMATH/search/search?query=Watson+spherical+polygons` returned HTTP 200
  with no matching item. Content not known beyond Uçar's statement that its expansion is the κ = 1 case of (3.111).
- Journal full texts behind paywalls (Class. Quantum Grav. version of Fursaev; Michigan Math. J. version of DGGW;
  Kodai/Enseign. Math. versions of Garbin–Jorgenson; AGAG version of Schueth) were not fetched; the arXiv versions were
  used instead.
