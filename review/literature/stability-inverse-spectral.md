# Stability in inverse spectral problems: Lipschitz, Hölder, logarithmic, and discrete recovery

Literature note for the stability theorem in "How much of a hyperbolic orbifold does heat hear?".
The search ran on 2026-10-01. It continues `review/hyperresearch/Q4-stability.md` and targets the gaps that note left open: the terms Hölder, Lipschitz, conditional stability and modulus of continuity; the one-dimensional Sturm–Liouville stability tradition; heat-invariant stability; and Osgood–Phillips–Sarnak compactness.

Every statement about a source below rests on text fetched in this search: an abstract at minimum, and theorem statements quoted verbatim where they carry an argument. Sources known only from metadata or from a citing paper are marked that way.

---

## 1. Summary

### 1.1 Typical moduli by setting

The literature retrieved here sorts stability moduli by the size and structure of the unknown, not by the operator.

- **Infinite-dimensional unknowns from boundary or spectral data: logarithmic, and optimal.** Two surveys from this search state the pattern directly. Koch–Rüland–Salo (arXiv:2012.01855, Ars Inveniendi Analytica 2025) say: "In the Calderón problem one has logarithmic stability [Al88] and this is optimal in general [Ma01]. Stability improves if the unknowns are restricted to a finite dimensional space [AV05]." Mandache's abstract (Inverse Problems 17 (2001), DOI 10.1088/0266-5611/17/5/313) says his construction shows "that the logarithmic stability results of Alessandrini are optimal (up to the value of the exponent)."
  - In spectral geometry, Daudé–Kamran–Nicoleau prove log-type stability of the warping function from the Steklov spectrum (J. Geom. Anal. 31 (2021) 1821–1854, Theorem 1.5).
  - Lassas–Lu–Yamaguchi prove a triple-logarithmic Gromov–Hausdorff estimate for orbifolds from finite interior spectral data (arXiv:2404.16448, Theorem 1.2).
  - Hölder estimates do appear in infinite-dimensional problems, but only under special structure:
    - Choulli–Stefanov for Borg–Levinson data that include boundary normal derivatives of eigenfunctions (CPDE 38 (2013));
    - Daudé–Kamran–Nicoleau for a special class of radial perturbations (Ann. Henri Poincaré 25 (2023), Theorem 1.1, exponent θ ∈ (0, 1/2]);
    - Liu–Quan–Saksala–Yan for magnetic Schrödinger operators from boundary spectral data (arXiv:2507.13619).
- **Finite-dimensional unknowns: Lipschitz when the linearization is injective, Hölder in general, with non-explicit constants.** Cârstea (arXiv:2605.06354) summarizes the tradition: Alessandrini–Vessella as "the prototype" Lipschitz theorem for piecewise-constant conductivities, and Bourgeois's global Lipschitz theorem under C¹ regularity, injectivity of the forward map and injectivity of the Fréchet derivative.
  - Alberti–Arroyo–Santacesaria prove that principle on compact subsets of finite-dimensional manifolds (Nonlinearity 36 (2023), Theorems 2.1–2.2).
  - Cârstea's Theorem A shows that real analyticity plus exact uniqueness alone already forces a Hölder estimate on compacta. His Remark 3.2 says the theorem does "not assert a Lipschitz rate, an effective Hölder exponent, or computable constants."
  - In every one of these abstract results the constant comes from a compactness argument and is not explicit.
- **One-dimensional Sturm–Liouville problems: Lipschitz, uniform on explicitly described sets of spectral data, with non-explicit constants.**
  - Bondarenko (Math. Nachr. 2025, arXiv:2409.16175, Theorem 2.4) proves that the spectral data ↦ (q, h, H) map is Lipschitz on balls where the inverse of the main-equation operator is bounded. The constant C(Ω, K) is left unspecified: "Finding specific formulas for the constant … is technically complicated and outside the scope of this paper."
  - Her paper also gives the mechanism that corresponds to our coincident orders. Uniform stability fails "if λ_n tends to λ_{n+1} or α_n tends to zero", so the sets where it holds impose a separation condition ρ_{n+1} − ρ_n ≥ δ (her (2.5)).
  - The classical stability results she cites (Hochstadt 1977, McLaughlin 1988, Ryabushko 1973, Alekseev 1986) are local: their constants depend on the unperturbed operator. Savchuk–Shkalikov (Funct. Anal. Appl. 44 (2010)) gave the first uniform stability for the self-adjoint problem.
  - With finitely many eigenvalues, the potential is not recovered, only approximated:
    - Savchuk (Math. Notes 99 (2016)) proves ‖q − q_N‖_τ ≤ C N^{τ−θ} from N eigenvalues and N norming constants;
    - Marletta–Weikard (Inverse Problems 21 (2005)) ask "how well a potential may be approximated if only N of each type of eigenvalues are known to within an error ε". Ben-Artzi–Marletta–Rösler call the norm of that estimate "rather weak";
    - Horváth–Kiss (IMRN 2010) give "estimates if only finite number of eigenvalues are known with an error < ε".
- **Coefficients to roots: locally 1/d-Hölder in general.** Parusiński–Rainer (arXiv:2410.01326, Lemma 6.4(2)) state that the map from coefficients to the unordered roots of a degree-d monic polynomial "is locally 1/d-Hölder".

### 1.2 Discrete invariants and heat invariants

- **Integer-valued spectral invariants recovered exactly by rounding.** One direct precedent was found. Léna–Serio (J. Phys. A 53 (2020) 275201, arXiv:2002.02911) recover the Euler characteristic χ of a quantum graph from the first J eigenvalues by χ(Γ) = nint[S_J(t)]. Their Theorem 3.3 covers eigenvalues "known up to error δ", provided J and δ satisfy explicit inequalities. The mechanism is the same as our δ*: an explicit error bound below 1/2, then nearest-integer rounding.

  Their setting differs from ours in three ways. The invariant is a single integer. It is a linear functional, a truncated trace formula. And there is no coincidence or degeneracy phenomenon. No precedent was found for recovering a multiset of integers through a nonlinear inversion whose rounding threshold degrades at coincidences.
- **Quantitative stability for heat invariants: none found.** Several full-text queries on this point returned 0 hits:
  - `"heat coefficients" "stability estimate"`
  - `"heat invariants" "modulus of continuity"`
  - `"heat invariants" "orbifold" "stability"` (the single hit was a Steklov survey)
  - `"cone points" "spectrum" "stability estimate"`

  Where heat invariants appear in inverse problems, they are used for qualitative compactness:
  - Osgood–Phillips–Sarnak, Ann. of Math. 129 (1989): "Using this along with the heat invariants for the Laplacian we then show that any isospectral set of plane domains is compact in the C^∞ topology";
  - Melrose, as reported by Datchev–Hezari;
  - Hislop–Wolf, arXiv:1803.02172, for iso-resonant potentials;
  - Jin–Wang, arXiv:2607.10108 and arXiv:2608.22330, for Steklov isospectral families.

  Osgood–Phillips–Sarnak (J. Funct. Anal. 80 (1988) 212–234) prove that "the set of isospectral metrics on a given Riemannian surface is sequentially compact in the C^∞ topology, up to isometry" (wording from the Datchev–Hezari survey). This is the qualitative contrast. Compactness plus injectivity gives some modulus of continuity on compacta (Koch–Rüland–Salo, Lemma 2.1), but no rate and no constant.
- **Prior qualitative determinacy for orbisurfaces.** Uçar's thesis (arXiv:1711.03405, Corollary 4.21(iv)) proves: "If the mirror locus is trivial and κ ≠ 0, then κ together with the spectrum determines the number of cone points as well as the multiset of all orders {n_1, …, n_N}." It uses the full set of heat invariants and has no stability statement. The thesis says the κ = −1 case was known earlier, from Dryden–Strohmaier (Canad. Math. Bull. 52 (2009)).

### 1.3 What our theorem adds

Relative to what this search actually found, the theorem adds four things. Each needs to be scoped carefully.

1. **Explicit constants in a spectral-geometric inverse problem.** Every Lipschitz or Hölder result retrieved for finite-dimensional unknowns or Sturm–Liouville data leaves its constant non-explicit: Bondarenko Theorem 2.4, Alberti–Arroyo–Santacesaria Theorems 2.1–2.2, Cârstea Theorem A. Bondarenko and Cârstea say so explicitly. Our explicit Lipschitz constant away from coincidences, and the explicit threshold δ*(m), have no retrieved counterpart.
2. **A sharp, structurally identified Hölder exponent 1/k at k-fold coincidences.** Cârstea's general theorem gives a Hölder exponent θ ∈ (0, 1] that is not effective. Parusiński–Rainer give the global exponent 1/d for coefficients-to-roots. Our theorem identifies the exponent with the coincidence multiplicity k and proves it sharp.
   - The general shape, Lipschitz where the differential is injective and Hölder where it degenerates, is what the abstract finite-dimensional principles predict, so it should not be presented as surprising.
   - The local 1/k refinement for a polynomial with a k-fold root was not located in any source retrieved in this search. The prior note lists Ostrowski, Marden, and Rahman–Schmeisser as lineage, but those books were not retrieved here, so the citation for "1/k at a k-fold root is classical" still needs to be checked directly.
3. **Exact recovery of a multiset of integers from approximate heat data.** Léna–Serio is the only retrieved precedent for rounding-based exact recovery of an integer spectral invariant, and it must be cited. Ours differs in three ways: we recover n integers rather than one; the inversion is nonlinear and passes through a symmetric-function system; and the threshold δ* degrades explicitly as orders coincide.

   Within this search, no quantitative stability theorem of any modulus was found for recovering cone orders, cone angles, or any other discrete orbifold invariant from heat or spectral data.

   The existence of some threshold δ > 0 for each fixed multiset is qualitatively soft. It follows from injectivity, continuity, and the discreteness of the target, in the spirit of Koch–Rüland–Salo Lemma 2.1. The new content is the explicit formula for δ*(m) and its dependence on the coincidence structure.
4. **Possibly the first quantitative stability statement for an inverse problem posed in heat invariants.** No retrieved source states a stability estimate whose data are heat-trace coefficients.

   A required caveat: the theorem measures error in heat coefficients, not in eigenvalues. No retrieved source quantifies how heat coefficients depend on finitely many approximately known eigenvalues. The paper therefore should not describe the result as "stability with respect to the spectrum" without that qualification.

   Léna–Serio, by contrast, work directly from finitely many approximate eigenvalues. That is the most likely point of referee comparison.

What the paper should not claim:

- that Lipschitz/Hölder stability in finite-dimensional inverse problems is new; it is standard;
- that the coincidence-driven loss of uniform stability is new; it is the separation condition in Bondarenko and the node-collision locus in the Prony literature covered by Q4;
- that rounding to integers from approximate spectral data is new in spectral theory; Léna–Serio do it.

### 1.4 Must-cite list

These are the sources in this note's scope; the Q4 Prony list is separate.

- Uçar, arXiv:1711.03405, Corollary 4.21(iv): prior qualitative determinacy of cone orders from the full spectrum. Dryden–Strohmaier 2009 for κ = −1.
- Léna–Serio, J. Phys. A 53 (2020) 275201: integer spectral invariant from finitely many approximate eigenvalues by rounding.
- Koch–Rüland–Salo (Ars Inveniendi Analytica 2025) and/or Mandache 2001: log is optimal in infinite dimensions. Alessandrini–Vessella 2005, Adv. Appl. Math. 35, 207–241: Lipschitz in finite dimensions.
- Alberti–Arroyo–Santacesaria (Nonlinearity 36 (2023)) and Cârstea (arXiv:2605.06354): abstract finite-dimensional Lipschitz/Hölder principles with non-explicit constants, the direct foil for "explicit constants".
- Bondarenko (Math. Nachr. 2025): Lipschitz uniform stability for Sturm–Liouville, the separation condition, and non-explicit constants. Savchuk–Shkalikov 2010 for the origin of uniform stability. Marletta–Weikard 2005 for finite spectral data.
- Daudé–Kamran–Nicoleau, J. Geom. Anal. 31 (2021): log-type Steklov stability in the target journal. Lassas–Lu–Yamaguchi, arXiv:2404.16448: the orbifold triple-log result.
- Osgood–Phillips–Sarnak 1988/1989: compactness via heat invariants and determinants, the qualitative contrast.
- Parusiński–Rainer, arXiv:2410.01326, Lemma 6.4: 1/d-Hölder coefficients-to-roots.

---

## 2. Table of relevant results

"Identifier" gives the form retrieved: arXiv id from the arXiv API, DOI from Crossref or the arXiv `doi` field. No DOI below was constructed.

| # | Authors | Title | Venue / year | Identifier (as retrieved) | Setting | Modulus | Data | Key statement (verbatim unless marked) |
|---|---|---|---|---|---|---|---|---|
| 1 | Léna, Serio | Concrete method for recovering the Euler characteristic of quantum graphs | J. Phys. A 53 (2020) no. 27, 275201 | arXiv:2002.02911; DOI 10.1088/1751-8121/ab95c1 | Metric graphs, standard Laplacian; integer invariant χ | Exact recovery by rounding (error < 1/2) | Finite: first J eigenvalues, each known to within δ | Thm 3.1: "J ≥ J_min … eigenvalues of the standard Laplacian on Γ suffice for recovering the Euler characteristic of Γ via the formula χ(Γ) = nint[S_J(t)]". Thm 3.3: "let the first J eigenvalues … be known up to error δ. Assume that J and δ satisfy both conditions (26) and (27) … Then the Euler characteristic of Γ can be recovered via … χ(Γ) = nint[S̃_J(t)]." |
| 2 | Uçar | Spectral invariants for polygons and orbisurfaces (PhD thesis, HU Berlin) | 2017 | arXiv:1711.03405 | Closed orbisurfaces of constant curvature; heat invariants | None (qualitative determinacy) | Full spectrum / all heat invariants | Cor. 4.21(iv): "If the mirror locus is trivial and κ ≠ 0, then κ together with the spectrum determines the number of cone points as well as the multiset of all orders {n_1,…,n_N}." |
| 3 | Bondarenko | Uniform stability of the inverse problem for the non-self-adjoint Sturm–Liouville operator | Math. Nachr. 2025 (Crossref) | arXiv:2409.16175; DOI 10.1002/mana.70018 | Sturm–Liouville on (0, π), complex q, Robin BCs | Lipschitz (uniform on sets of spectral data) | Infinite: full spectral data {ρ_n, α_n} | Thm 2.4: "‖q⁽¹⁾ − q⁽²⁾‖_{L2} + \|h⁽¹⁾ − h⁽²⁾\| + \|H⁽¹⁾ − H⁽²⁾\| ≤ C d(S⁽¹⁾, S⁽²⁾), where C = C(Ω, K). Thus, the mapping S ↦ (q, h, H) is Lipschitz continuous". Also: "Finding specific formulas for the constant C = C(Ω,K) … is technically complicated and outside the scope of this paper." And: "if λ_n tends to λ_{n+1} or α_n tends to zero, then the norm of the potential q can grow infinitely." |
| 4 | Savchuk, Shkalikov | Inverse problems for Sturm–Liouville operators with potentials in Sobolev spaces: uniform stability | Funct. Anal. Appl. 44 (2010) 270–285 | DOI 10.1007/s10688-010-0038-6 | Self-adjoint SL, q ∈ W₂^α, α > −1 | Uniform stability | Two spectra / spectral data | No abstract retrieved (OpenAlex empty). Described by Bondarenko (#3): "proved the uniform stability for the recovery of the self-adjoint Sturm–Liouville operators with distribution potentials of the Sobolev spaces W₂^α, α > −1, from the two spectra and from the spectral data." |
| 5 | Savchuk | Reconstruction of the potential of the Sturm–Liouville operator from a finite set of eigenvalues and normalizing constants | Math. Notes 99 (2016) 715–728 | DOI 10.1134/s0001434616050102; arXiv:1512.00300 | SL on [0, π], q ∈ W₂^θ | Approximation rate (power of N), uniform constant | Finite: {λ_k}₁^N, {α_k}₁^N | Abstract (arXiv): "for −1 ⩽ τ < θ the estimate ‖q − q_N‖_τ ⩽ C N^{θ−τ} holds … the constant C depends on R but does not depend on q if ‖q‖_θ ⩽ R." (The journal abstract writes the exponent as N^{τ−θ}.) |
| 6 | Marletta, Weikard | Weak stability for an inverse Sturm–Liouville problem with finite spectral data and complex potential | Inverse Problems 21 (2005) 1275–1290 | DOI 10.1088/0266-5611/21/4/005 | 1D Schrödinger on finite interval, complex q | "Weak" (approximation within error) | Finite: N Dirichlet–Dirichlet + N Dirichlet–Neumann eigenvalues, each within ε | Abstract: "We investigate here how well a potential may be approximated if only N of each type of eigenvalues are known to within an error ε." Characterized by Ben-Artzi–Marletta–Rösler (arXiv:2203.13078): "the rather weak norm in which Marletta and Weikard estimate errors in q arising from errors in finite spectral data." |
| 7 | Horváth, Kiss | Stability of direct and inverse eigenvalue problems for Schrödinger operators on finite intervals | IMRN 2010 (Crossref issued 2009) | DOI 10.1093/imrn/rnp210 | SL / Schrödinger, q ∈ L^p | L^p vs ℓ^{p′} (Lipschitz-type between norms) | Infinite and finite | Abstract: "if the potential is in L^p, then the perturbation of the potentials can be estimated by the l^{p′}-norm of the sequence of the eigenvalue differences only if p ≥ 2. As a consequence, we give estimates if only finite number of eigenvalues are known with an error < ε." |
| 8 | McLaughlin | Stability theorems for two inverse spectral problems | Inverse Problems 4 (1988) 529–540 | DOI 10.1088/0266-5611/4/2/015 | Two second-order problems on bounded interval | Local stability | Spectral data | Abstract: "Stability results are presented for two second-order inverse spectral problems defined on a bounded interval … a change in the form of the differential operator produces a change in the stability result." |
| 9 | Hochstadt | On the well-posedness of the inverse Sturm–Liouville problems | J. Differential Equations 23 (1977) 402–413 | DOI 10.1016/0022-0396(77)90119-x | SL | Local stability (per Bondarenko) | — | Metadata only (no abstract; ScienceDirect PDF returned HTTP 403). Bondarenko (#3) groups it among works where "the stability … has a local nature." |
| 10 | Hitrik | Stability of an inverse problem in potential scattering on the real line | CPDE 25 (2000) 925–955 | DOI 10.1080/03605300008821537 | Schrödinger on ℝ, scattering | Stability (modulus not retrieved) | Finite data (per Bondarenko) | Abstract fragment only: "we are going to study some problems arising in inverse scattering theory for the Schrödinger operator H_p u = −u″ + pu on the real line." Bondarenko: "Stability of inverse problems by finite data on the line … was considered by Aktosun and Hitrik." |
| 11 | Cârstea | Hölder Stability from Exact Uniqueness for Finite-Dimensional Analytic Inverse Problems | arXiv preprint 2026 | arXiv:2605.06354 | Abstract finite-dimensional, real-analytic forward map | Hölder, non-effective exponent | Operator data; finite measurements (qualitative) | Thm A: "for every compact set K ⋐ U, there exist C > 0 and θ ∈ (0, 1] such that \|R(p) − R(q)\| ≤ C‖F(p) − F(q)‖^θ". Rem. 3.2: "The theorem also does not assert a Lipschitz rate, an effective Hölder exponent, or computable constants." |
| 12 | Alberti, Arroyo, Santacesaria | Inverse problems on low-dimensional manifolds | Nonlinearity 36 (2023) 734–808 | arXiv:2009.00574; DOI 10.1088/1361-6544/aca73d | Abstract Banach-space inverse problems, unknown on n-dim manifold | Lipschitz (injective derivative) / Hölder | Finite discretizations allowed | Thm 2.1: if F\|_K is injective and F′(x) is injective on W, "Then there exists C > 0 such that ‖x − y‖_X ≤ C‖F(x) − F(y)‖_Y, x, y ∈ K." Thm 2.2: Hölder version "‖x − y‖_X ≤ C‖F(x) − F(y)‖^α_Y". |
| 13 | Koch, Rüland, Salo | On instability mechanisms for inverse problems | Ars Inveniendi Analytica (2025), Revised Paper No. 1 | arXiv:2012.01855; DOI 10.15781/kvf0-ds86 | General (Calderón, UCP, backward heat) | Instability; log optimality | — | Intro: "In the Calderón problem one has logarithmic stability [Al88] and this is optimal in general [Ma01]. Stability improves if the unknowns are restricted to a finite dimensional space [AV05]." Lemma 2.1: for continuous injective F and compact K "there is a modulus of continuity ω such that d_X(x₁,x₂) ≤ ω(d_Y(F(x₁),F(x₂)))". |
| 14 | Mandache | Exponential instability in an inverse problem for the Schrödinger equation | Inverse Problems 17 (2001) 1435–1444 | DOI 10.1088/0266-5611/17/5/313 | Calderón / Schrödinger DN map | Log optimal | Infinite | Abstract: "this problem is severely ill-posed … the logarithmic stability results of Alessandrini are optimal (up to the value of the exponent)." |
| 15 | Alessandrini, Vessella | Lipschitz stability for the inverse conductivity problem | Adv. Appl. Math. 35 (2005) 207–241 | DOI 10.1016/j.aam.2004.12.002 | Piecewise-constant conductivities, known partition | Lipschitz | Infinite (DN map) | No abstract retrieved (PDF 403). Described by Cârstea (#11) as "The prototype is the Lipschitz stability theorem of Alessandrini–Vessella for piecewise constant isotropic conductivities on a known partition." |
| 16 | Daudé, Kamran, Nicoleau | Stability in the Inverse Steklov Problem on Warped Product Riemannian Manifolds | J. Geom. Anal. 31 (2021) no. 2, 1821–1854 (online 2019) | DOI 10.1007/s12220-019-00326-9; arXiv:1812.07235 | Warped-product manifolds, Steklov spectrum | Logarithmic | Infinite (sup over all σ_k) | Thm 1.5: "Assume … sup_{k≥0} \|σ_k − σ̃_k\| ≤ ε. Then, there exists a positive constant C_A … ‖c − c̃‖_{L∞(0,1)} ≤ C_A (1/log(1/ε))^{p−1}." |
| 17 | Daudé, Kamran, Nicoleau | Local Hölder Stability in the Inverse Steklov and Calderón Problems for Radial Schrödinger Operators and Quantified Resonances | Ann. Henri Poincaré 25 (2023) 3805–3830 | DOI 10.1007/s00023-023-01391-1; arXiv:2212.03148 | Radial Schrödinger on unit ball; special perturbation class | Hölder, θ ∈ (0, 1/2] explicit in R, M₀ | Infinite | Thm 1.1: "‖Q̃ − Q‖_{L2(0,T)} ≤ C_T ‖σ_k − σ̃_k‖^θ_{ℓ∞(N)}, where the Hölder exponent θ ∈ (0, 1/2] … θ = ½ min(1, log R / log(9M₀/2))." |
| 18 | Lassas, Lu, Yamaguchi | Inverse Spectral Problems for Collapsing Manifolds II: Quantitative Stability of Reconstruction for Orbifolds | arXiv preprint | arXiv:2404.16448 | Orbifolds from 1-dim collapse; metric reconstruction | Triple-logarithmic | Finite interior spectral data {λ_j, φ_j\|_U}_{j≤δ⁻¹} | Thm 1.2: "the finite interior spectral data {λ_j, φ_j\|_U}_{j=0}^{δ⁻¹} … determine a finite metric space X̂ such that d_GH(X∖S_{σ,δ}, X̂) < C₁(X,σ)(log log \|log δ\|)^{−C₂}". |
| 19 | Choulli, Stefanov | Stability for the Multi-Dimensional Borg–Levinson Theorem with Partial Spectral Data | CPDE 38 (2013) 455–476 | DOI 10.1080/03605302.2012.747538; arXiv:1111.0231 | Schrödinger on bounded domain; eigenvalues + boundary normal derivatives | Hölder | Infinite; finitely many may be unknown | Abstract: "The estimate is of Hölder type, and we allow finitely many eigenvalues and normal derivatives to be unknown." |
| 20 | Li, R. | Quantitative local recovery of Kerr–de Sitter parameters from high-frequency equatorial quasinormal modes | arXiv preprint 2026 | arXiv:2602.15764 | Resonances of Kerr–de Sitter; continuous parameters (M, a) | Two-sided Lipschitz (local) | Finite package of QNMs | Thm 48 (as summarized in intro): "the data map G^QNM_ℓ : K → ℝ² … is a real-analytic diffeomorphism onto its image with a uniform two-sided Lipschitz bound … (M, a) can be reconstructed from (U, V) with a stability constant depending only on K and Λ." |
| 21 | Osgood, Phillips, Sarnak | Compact isospectral sets of surfaces | J. Funct. Anal. 80 (1988) 212–234 | DOI 10.1016/0022-1236(88)90071-7 | Isospectral metrics on a fixed surface | Compactness (qualitative) | Full spectrum | Full text not retrieved (Elsevier landing page only). OpenAlex abstract (French): "On etudie des ensembles de surfaces qui sont isospectrales par rapport a l'operateur de Laplace-Beltrami". Datchev–Hezari (arXiv:1108.5755, §5.2): OPS "prove that the set of isospectral metrics on a given Riemannian surface is sequentially compact in the C^∞ topology, up to isometry." |
| 22 | Osgood, Phillips, Sarnak | Moduli Space, Heights and Isospectral Sets of Plane Domains | Ann. of Math. 129 (1989) 293 | DOI 10.2307/1971449 | Plane domains of finite connectivity | Compactness via height + heat invariants | Full spectrum | Abstract: "Using this along with the heat invariants for the Laplacian we then show that any isospectral set of plane domains is compact in the C^∞ topology." |
| 23 | Osgood, Phillips, Sarnak | Extremals of determinants of Laplacians | J. Funct. Anal. 80 (1988) 148–211 | DOI 10.1016/0022-1236(88)90070-5 | Determinant as function of metric | — | — | OpenAlex abstract: "On etudie le determinant associe au laplacien en fonction de la metrique sur une surface donnee et en particulier ses valeurs extremes quand la metrique est bien restreinte". |
| 24 | Parusiński, Rainer | On the continuity of the solution map for polynomials | arXiv preprint 2024 | arXiv:2410.01326 | Coefficients → unordered roots of monic degree-d polynomial | 1/d-Hölder (local) | Finite-dimensional | Lemma 6.4(2): "The map Λ : ℂ^d → A_d(ℂ) is locally 1/d-Hölder: if a₁, a₂ ∈ ℂ^d and ‖a_i‖₂ ≤ K … then d(Λ(a₁), Λ(a₂)) ≤ C(d,K)‖a₁ − a₂‖₂^{1/d}." |
| 25 | Katz, Batenkov, Giordano | Separation-free exponential fitting with structured noise, with applications to inverse problems in parabolic PDEs | arXiv preprint 2025 | arXiv:2512.14301 | Prony recovery of Sturm–Liouville eigenvalues from exponential sums | Super-exponential accuracy under structured noise | Finite measurements | Abstract: "the exponents and amplitudes can be recovered with super-exponential accuracy … the classical Prony's method attains the analytic optimal error decay also in the 'separation-free' regime." |
| 26 | Buterin | On the uniform stability of recovering sine-type functions with asymptotically separated zeros | arXiv preprint 2021 | arXiv:2110.00526 | Entire functions from their zeros (zeros → function direction) | Lipschitz on balls | Infinite sequence of zeros | Abstract: "the dependence of such functions on the sequences of their zeros possesses the Lipschitz property with respect to natural metrics on each ball of a finite radius." |
| 27 | Hislop, Wolf | Compactness of iso-resonant potentials for Schrödinger operators in dimensions one and three | arXiv preprint 2018 | arXiv:1803.02172 | Iso-resonant potentials | Compactness (qualitative) | Full resonance set | Abstract: "the set I_R(V₀) is a compact subset of C₀^∞(B̄_R(0)) in the C^∞-topology." |
| 28 | Jin, Wang | Steklov Spectral Geometry for Annular Surfaces: Inverse spectral results and isospectral compactness | arXiv preprint 2026 | arXiv:2607.10108 | Steklov spectrum, flat annular surfaces | Compactness (qualitative) | Full spectrum | Abstract: "any family of Steklov isospectral flat annular surfaces is compact in the C^∞ topology." Uses "the Osgood–Phillips–Sarnak uniformization theorem". |
| 29 | Alberti, Santacesaria | Calderón's Inverse Problem with a Finite Number of Measurements | Forum Math. Sigma 7 (2019) e35 | arXiv:1803.04224; DOI 10.1017/fms.2019.31 | Schrödinger potential in known finite-dim subspace | Lipschitz | Finitely many boundary measurements | Abstract: "Lipschitz stability estimates and a globally convergent nonlinear reconstruction algorithm for both inverse problems are also presented." |
| 30 | Ben-Artzi, Marletta, Rösler | On the complexity of the inverse Sturm–Liouville problem | Pure Appl. Analysis 5 (2023) 895–925 | arXiv:2203.13078; DOI 10.2140/paa.2023.5.895 | SL with Robin BCs; algorithmic | — (computability) | Finite modification of zero-potential data | Abstract: "if all but finitely many of the eigenvalues and norming constants coincide with those for the zero potential then the number of limits is zero, i.e. it is possible to retrieve the potential and boundary conditions precisely in finitely many steps." |
| 31 | Rundell, Sacks | Reconstruction techniques for classical inverse Sturm–Liouville problems | Math. Comp. 58 (1992) 161–183 | DOI 10.1090/s0025-5718-1992-1106979-0 | SL reconstruction algorithms | — (numerical) | Spectral data | Abstract: "This paper gives constructive algorithms for the classical inverse Sturm-Liouville problem." No stability theorem in the abstract. |
| 32 | Alessandrini, Sylvester, Sun | Stability For a Multidimensional Inverse Spectral Theorem | CPDE 15 (1990) 711–736 | DOI 10.1080/03605309908820705 | Schrödinger on bounded domain; eigenvalues + normal derivatives | Stability (modulus not in retrieved abstract) | Infinite | Abstract: "It is known … that knowledge of the eigenvalues and the boundary values of the normal derivatives of the corresponding eigenfunctions is sufficient to uniquely determine a coefficient, q." |

Items found and noted but not load-bearing:

- Hochstadt, "The inverse Sturm-Liouville problem", CPAM 26 (1973) 715–729, DOI 10.1002/cpa.3160260514 (metadata only);
- Ryabushko, "Stability of the reconstruction of a Sturm–Liouville operator from two spectra", Teor. Funkts. Funkts. Anal. Prilozh. 18 (1973) (citation only, from Bondarenko's reference list [23]; no Crossref record);
- Horváth–Kiss, Inverse Problems 27 (2011) 095007, DOI 10.1088/0266-5611/27/9/095007 (complex-potential extension);
- Bondarenko, "Uniform stability for the Hochstadt–Lieberman problem", arXiv:2410.10326;
- Dryden–Strohmaier, "Huber's Theorem for Hyperbolic Orbisurfaces", Canad. Math. Bull. 52 (2009) 66–71, DOI 10.4153/cmb-2009-008-0 (metadata only);
- Datchev–Hezari, "Inverse problems in spectral geometry", MSRI Publ. 60 (2012), arXiv:1108.5755 (survey; source of the OPS characterization above).

---

## 3. Search log

### 3.1 arXiv full-text search

Endpoint. `POST https://arxiv.org/search_classic` with `searchtype=ft` returned **HTTP 302** to `https://search.arxiv.org/?query=…&in=`. All queries were then sent as `GET https://search.arxiv.org/?query=<q>&in=`, paginated with `&startat=10k`, 10 hits per page.

Pages read:

- q01: all 64 hits.
- q02–q16: up to 3 pages.
- q17–q44: 2 pages.
- q45–q50: 1 page.

"Relevant" means the hit was taken forward to abstract or full-text reading. Raw HTML is in a local scratch directory (not committed), `lit-b/ft_*.html`; parsed lists are in `q01.txt`…`q50.txt`.

| # | Query string | Hits | Relevant hits (arXiv id) |
|---|---|---|---|
| q01 | `"Lipschitz stability" "inverse spectral"` | 64 | 2608.14324, 2603.07613, 1302.3325, 2110.00526, 2009.00574, 1803.04224, 2012.01855 |
| q02 | `"Hölder stability" "inverse spectral"` | 14 | 2212.03148, 2602.13703, 2012.01855 |
| q03 | `"Holder stability" "inverse spectral"` | 29 | 2507.13619, 1111.0231, 2009.00574 |
| q04 | `"conditional stability" "inverse eigenvalue"` | 1 | 2409.16175 |
| q05 | `"logarithmic stability" "inverse spectral"` | 63 | 2212.03148, 2507.15560, 2311.18642, 2012.01855 |
| q06 | `"stability" "heat invariants"` | 21 | 2607.10108, 1803.02172 (compactness only; no heat-invariant stability estimate) |
| q07 | `"finitely many eigenvalues" stability Sturm-Liouville` | 55 | 1111.0231 (mostly off-topic: nonlinear-PDE spectral stability) |
| q08 | `"stability" "heat trace" "spectral invariants"` | 20 | 2607.10108 (no stability estimate) |
| q09 | `"quantitative" "spectral rigidity"` | 204 | none on point (billiards / length spectrum / random matrices) |
| q10 | `"isospectral" "stability estimate"` | 21 | 2502.18289, 1504.04267 |
| q11 | `"spectral determination" stability polygon` | 4 | none |
| q12 | `"spectral determination" stability triangle` | 10 | 1911.06758 (exact non-determinacy, no stability) |
| q13 | `"uniform stability" Sturm-Liouville` | 82 | 2409.16175, 2506.15300, 2410.10326, 2203.13078, 2110.00526 |
| q14 | `"finite spectral data" stability` | 32 | 1512.00300, 2404.16448, 2203.13078, 2512.14301, 2409.16175 |
| q15 | `"heat invariants" "modulus of continuity"` | **0** | — |
| q16 | `"Osgood" "Phillips" "Sarnak" compactness isospectral` | 54 | 1108.5755, 1206.6077, 2607.10108, 2608.22330 |
| q17 | `"heat invariants" Lipschitz inverse` | 21 | 1711.03405 |
| q18 | `"heat invariants" Holder stability` | 1 | 1803.02172 (compactness, not stability) |
| q19 | `"heat coefficients" "stability estimate"` | **0** | — |
| q20 | `"Lipschitz stability" "finite-dimensional" "inverse problem"` | 203 | 2605.06354, 1805.00866, 2009.00574 |
| q21 | `Hochstadt "finite number of eigenvalues" stability` | 3 | 2409.16175 |
| q22 | `Marletta Weikard "weak stability"` | 15 | 2203.13078, 1512.00300, 2409.16175 |
| q23 | `Savchuk Shkalikov "uniform stability"` | 46 | 2410.10326, 2409.16175 |
| q24 | `Hitrik stability inverse` | 143 | 2409.16175 (Hitrik's own paper is not on arXiv) |
| q25 | `"Osgood, Phillips and Sarnak"` | 67 | 2607.10108, 2608.22330, 1206.6077 |
| q26 | `"Prony" "inverse spectral"` | 5 | 2512.14301 |
| q27 | `"heat trace" orbifold "cone points" orders` | 8 | 1711.03405 (determinacy), 2106.07882 |
| q28 | `"stability" "spectral invariants" "finitely many"` | 174 | none (symplectic / Floer "spectral invariants") |
| q29 | `"logarithmic stability" Steklov` | 26 | 1812.07235, 2212.03148 |
| q30 | `"Lipschitz stability" "finitely many" eigenvalues` | 126 | 2410.16224 (travel times; tangential), 1805.00866 |
| q31 | `"Holder continuity" roots polynomial multiplicity` | 131 | 2410.01326 |
| q32 | `"quantitative" "inverse spectral" "explicit constants"` | 13 | none |
| q33 | `"heat invariants" "determine" "stability"` | 15 | none with a stability estimate |
| q34 | `"inverse spectral" "integer" "stability" "discrete parameters"` | 2 | none |
| q35 | `"approximate eigenvalues" determine "exactly" integer` | 196 | none in first 20 |
| q36 | `"heat trace" "cone angles" determine stability` | 1 | none (Steklov survey) |
| q37 | `"spectral invariants" "orbifold" "cone points" "determine"` | 6 | 1711.03405 |
| q38 | `"Lipschitz" "heat invariants"` | 24 | none with a stability estimate |
| q39 | `"Holder" "heat trace" inverse` | 41 | none |
| q40 | `"conditional stability" "inverse spectral"` | 34 | 2409.16175, 2506.15300 |
| q41 | `"modulus of continuity" "inverse spectral"` | 49 | 1209.5875, 2012.01855 |
| q42 | `"Hochstadt" "stability" "inverse Sturm-Liouville" "finite"` | 31 | 2410.10326, 2409.16175 |
| q43 | `"Rundell" "Sacks" stability eigenvalues` | 36 | 2203.13078, 1512.00300, 2512.14301 |
| q44 | `"Horvath" "inverse spectral" stability` | 22 | 2410.10326, 2409.16175 |
| q45 | `"integer-valued" "inverse spectral" stability` | 15 | **2002.02911** |
| q46 | `"heat invariants" "orbifold" "stability"` | 1 | none (2212.12528, Steklov survey) |
| q47 | `"spectral data" "integer" "rounding" recover exactly` | 31 | none in first 10 |
| q48 | `"Hölder" "multiple roots" "power sums" stability` | **0** | — |
| q49 | `"cone points" "spectrum" "stability estimate"` | **0** | — |
| q50 | `"isospectral" "orbifold" "Lipschitz"` | 20 | none (1106.2724, Proctor finiteness, is qualitative) |

### 3.2 arXiv API (`https://export.arxiv.org/api/query`)

| Query | Total | Relevant |
|---|---|---|
| `id_list=` batch of 24 ids (abstract retrieval) | 24 | all used above |
| `au:Weikard AND au:Marletta` | 1 | 0905.0171 (resonances; not the 2005 paper) |
| `ti:"Lipschitz stability for the inverse conductivity"` | 2 | 2402.04651, 1405.0475 (Alessandrini–Vessella 2005 is not on arXiv) |
| `au:Osgood AND au:Sarnak` | 0 | — |
| `all:"heat invariants" AND all:stability` | 0 | — |
| `ti:stability AND ti:"heat trace"` | 0 | — |
| `abs:"inverse spectral" AND abs:Lipschitz AND abs:"finitely many"` | 0 | — |
| `id_list=2002.02911,1803.02172,2507.13619` and `id_list=2404.16448` | 4 | all used |

### 3.3 Crossref (`https://api.crossref.org/works?query.bibliographic=…&rows=3`)

21 bibliographic queries, one per classic reference: OPS ×3, Hochstadt 1977, McLaughlin, Marletta–Weikard, Hitrik, Savchuk–Shkalikov, Horváth–Kiss, Rundell–Sacks, Alessandrini–Vessella, Mandache, DKN ×2, Dryden–Strohmaier, Alessandrini–Sylvester, Savchuk 2016, Bondarenko, Choulli–Stefanov, Hochstadt 1973, Ryabushko.

- 20 returned the target record as the first hit.
- Ryabushko returned no matching record.
- Direct lookups `works/10.1088/1751-8121/ab95c1` and `works/10.1007/s12220-019-00326-9` confirmed volume, issue and pages.

### 3.4 OpenAlex

- `works/doi:<doi>`: 16 lookups for abstracts. Abstracts were obtained for OPS 1988a/b (one-line French), OPS 1989, McLaughlin, Marletta–Weikard, Hitrik (fragment), Horváth–Kiss ×2, Mandache, Alessandrini–Sylvester–Sun, Rundell–Sacks and Savchuk 2016. The record had no abstract for Hochstadt 1973/1977, Savchuk–Shkalikov 2010 and Alessandrini–Vessella.
- `works?search=…`: 6 relevance searches, used as a substitute for Semantic Scholar:
  - "stability heat invariants inverse spectral"
  - "Lipschitz stability inverse spectral problem finite spectral data"
  - "Hölder stability inverse eigenvalue problem"
  - "stability estimate spectral invariants heat trace determine domain"
  - "conditional stability inverse Sturm-Liouville finitely many eigenvalues"
  - "quantitative isospectral stability surfaces"

  Each returned 175–13,726 matches. Ranking was dominated by off-topic, highly cited works. On-topic results were limited to 2409.16175, Choulli–Stefanov 2013 and Mandache 2001, all already found.

### 3.5 Unpaywall (`https://api.unpaywall.org/v2/<doi>?email=palaashgang@gmail.com`)

7 lookups:

- Marletta–Weikard, Alessandrini–Vessella, OPS 1988b and Hochstadt 1977: publisher-only OA locations.
- Mandache: publisher plus two repository locations, not fetched.
- Savchuk–Shkalikov and Hitrik: not OA.

### 3.6 Full-text PDFs read (arXiv, pymupdf)

2409.16175, 1512.00300 (Russian text; English abstract used), 2605.06354, 2012.01855, 1812.07235, 2212.03148, 1711.03405, 2602.15764, 1108.5755, 2009.00574, 2203.13078, 2110.00526, 2410.01326, 1111.0231, 1803.04224, 2410.10326, 2607.10108, 2512.14301, 2002.02911, 2404.16448.

---

## 4. Instrument gaps

These are failures of the retrieval tools, not evidence that the sources do not exist.

| Source / endpoint | URL | Error | Relevance |
|---|---|---|---|
| Semantic Scholar search (anonymous) | `https://api.semanticscholar.org/graph/v1/paper/search?query=…` | HTTP 429 on all 6 attempts per query (backoff 0, 4, 8, 16, 32, 40 s), for all 4 queries. The configured Semantic Scholar connector also failed (connection timeout). | High: the citation-ranked academic sweep did not run. OpenAlex search was substituted but ranks poorly for these queries. |
| arXiv `search_classic` full text | `POST https://arxiv.org/search_classic`, `searchtype=ft` | HTTP 302 to `search.arxiv.org` (worked after following the redirect). The index covers arXiv only, so journal-only papers (Marletta–Weikard 2005, Hitrik 2000, McLaughlin 1988, Hochstadt 1973/1977, Savchuk–Shkalikov 2010, Alessandrini–Vessella 2005, OPS 1988/89) cannot be hit by full-text terms. "Hölder" and "Holder" tokenize differently (14 vs 29 hits). | Medium: the null results for heat-invariant stability are nulls over arXiv full text only. |
| Marletta–Weikard 2005 PDF | `https://iopscience.iop.org/article/10.1088/0266-5611/21/4/005/pdf` | Redirected to a bot-check page (`validate.perfdrive.com`, Radware). HTML returned, no PDF. | High for Sturm–Liouville finite-data stability: only the abstract and a secondary characterization were obtained, so its modulus is not quoted. |
| Mandache 2001 PDF | `https://iopscience.iop.org/article/10.1088/0266-5611/17/5/313/pdf` | Same bot-check redirect. Repository copies (`dspace.lboro.ac.uk/2134/680`, figshare) were not tried. | Low: the abstract suffices. |
| Hochstadt 1977 PDF | `https://www.sciencedirect.com/science/article/pii/002203967790119X/pdf` | HTTP 403 | Medium: metadata only. |
| Alessandrini–Vessella 2005 PDF | `https://www.sciencedirect.com/science/article/pii/S0196885805000345/pdf` | HTTP 403 | Medium: characterized only through Cârstea and Koch–Rüland–Salo. |
| OPS 1988b full text | `https://doi.org/10.1016/0022-1236(88)90071-7` | Resolved to the `linkinghub.elsevier.com` landing page (HTML, 2.6 KB), no PDF. | Medium: the OPS compactness statement is quoted via Datchev–Hezari, not from OPS directly. |
| Savchuk–Shkalikov 2010, Hitrik 2000, McLaughlin 1988, Horváth–Kiss 2010 full text | — | Not OA per Unpaywall/OpenAlex; not attempted. | Medium: abstracts only (none for Savchuk–Shkalikov). |
| Ryabushko 1973; Hochstadt 1973 | — | Ryabushko: no Crossref record (Russian-language). Hochstadt 1973: Crossref metadata, no abstract. | Low–medium: not characterized beyond citing papers. |
| Ostrowski / Marden / Rahman–Schmeisser (local 1/k root perturbation) | — | Books; not retrieved in this search. | Medium: the "1/k at a k-fold root is classical" citation remains unverified here. Parusiński–Rainer give only the global 1/d form. |
