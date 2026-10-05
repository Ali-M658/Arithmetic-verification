# A. Word-for-word citation check: the spectral cluster

Scope: every `\cite` of dggw2008, ucar2017, drydenstrohmaier2009, donnelly1976, schueth2019, adfg2008,
mckeansinger1967, kac1966, marklof2011 and doylerossetti2011 in `paper/jga/manuscript.tex`, plus the DGGW
erratum. Manuscript line numbers are those of the current file (1584 lines).

Sources read (all in `review/literature-pass/_fetched/`, text via `pdftotext -layout`):

| key | file(s) | version read | where it came from |
|---|---|---|---|
| dggw2008 | `pdf/dggw2008_mmj.pdf` (34 pp.), `pdf/dggw2008_arxiv.pdf` (35 pp.) | Michigan Math. J. 56 (2008) 205–238 (published); arXiv:0805.3148v1 (the only version) | Project Euclid open PDF (200); arxiv.org/pdf |
| DGGW erratum | `pdf/dggw2017erratum_mmj.pdf` (2 pp.) | Michigan Math. J. 66 (2017) 221–222, DOI 10.1307/mmj/1488510034 | Project Euclid open PDF (200) |
| ucar2017 | `pdf/ucar2017_edoc.pdf` (byte-identical to `research/raw/spectral-invariants-for-polygons-and.pdf`), `pdf/ucar2017_v1.pdf` | Humboldt edoc published thesis, DOI 10.18452/18463; arXiv:1711.03405v1 (the only arXiv version) | edoc.hu-berlin.de bitstream (200); arxiv.org/pdf |
| drydenstrohmaier2009 | `pdf/drydenstrohmaier2009_cmb.pdf`, `_arxiv_v1.pdf`, `_arxiv_v2.pdf` | Canad. Math. Bull. 52 (2009) 66–71 (published); arXiv:math/0504571 v1, v2 | Cambridge Core open PDF (via Unpaywall, 200); arxiv.org/pdf |
| doylerossetti2011 | `pdf/doylerossetti2011.pdf` (v2), `pdf/doylerossetti2011_v1.pdf` | arXiv:1103.4372 v2 (10 Apr 2014, 25 pp.) and v1 (22 Mar 2011, 47 pp.) | arxiv.org/pdf |
| schueth2019 | `pdf/schueth2019_aif.pdf`, `pdf/schueth2019_arxiv.pdf` | Ann. Inst. Fourier 69 (2019) no. 7, 2827–2855 (published); arXiv:1812.06119v1 | centre-mersenne open PDF; arxiv.org/pdf |
| adfg2008 | `pdf/adfg2008_arxiv.pdf` | arXiv:math/0608462v1 only (published version closed, see gaps) | arxiv.org/pdf |
| donnelly1976 | `pdf/donnelly1976.pdf` (scanned images, read as page images `txt/donnelly_img/`) | Math. Ann. 224 (1976) 161–170 | GDZ Göttingen, `download/pdf/PPN235181684_0224/LOG_0035.pdf` (200), found through geodesic.mathdoc.fr |
| mckeansinger1967 | `pdf/mckeansinger1967.pdf` | J. Differential Geom. 1 (1967) 43–69 | Project Euclid open PDF (200) |
| kac1966 | `pdf/kac1966.pdf` | Amer. Math. Monthly 73 (1966) no. 4, part 2, 1–23 (JSTOR scan) | math.ucdavis.edu course copy (200) |
| marklof2011 | `pdf/marklof2011_arxiv.pdf` | arXiv:math/0407288v2 only (CUP chapter closed, see gaps) | arxiv.org/pdf |

Page convention below: "p. 227 (pdf 23)" = printed page 227, PDF page 23. For Uçar, printed page = PDF page − 5.

**Numbering across versions.**
- **DGGW.** arXiv:0805.3148v1 and the published Michigan version have *identical* numbering for every item the manuscript uses (4.1, 4.5, 4.7, 4.8, 5.3–5.7, 5.10, 5.13–5.16, 5.22). Only the page numbers differ.
- **Uçar.** The edoc version and arXiv v1 have identical content and numbering. A whitespace-normalised `diff` of the two texts shows only the title-page block and font-encoding differences (ℓ vs `, ϵ vs blank). arXiv has only v1.
- **Dryden–Strohmaier.** arXiv v2 and the CMB version have identical theorem numbering. Their page numbering differs: arXiv "p. 3" is CMB p. 68. In arXiv v1, Prop. 3.3 is stated for "Riemann orbisurfaces".
- **Schueth.** arXiv and AIF have identical numbering (Thm 4.1, Rem. 4.2).
- **Doyle–Rossetti.** The section numbering differs between versions: "Background" is §4 in v1 and §3 in v2.

---

## 1. Citation table

### dggw2008 (18 instances)

| line | cite as written | claim (short) | location found (published MMJ) | verbatim quote | verdict | correction |
|---|---|---|---|---|---|---|
| 119 | `\cite{mckeansinger1967,donnelly1976,dggw2008}` | heat coefficients are spectral invariants (orbifold expansion) | Thm 4.8, p. 220 (pdf 16) | "The heat trace ∑ e^{−λ_j t} of O is asymptotic as t → 0+ to I_0 + ∑_{N∈S(O)} I_N/\|Iso(N)\| … This asymptotic expansion is of the form (4πt)^{−dim(O)/2} ∑_{j=0}^∞ c_j t^{j/2} (4.9) for some constants c_j." | ACCURATE | — |
| 174 | `[Thms~5.14--5.15]` | "c … is a complete invariant of the closed orientable 2-orbifolds with χ≥0" | Thm 5.15, p. 232 (pdf 28); Thm 5.14, p. 230 (pdf 26) | 5.15: "Let C be the class consisting of all closed orientable 2-orbifolds with χ(O) ≥ 0. The spectral invariant c is a complete topological invariant within C and, moreover, it distinguishes the elements of C from smooth oriented closed surfaces." 5.14: "Within the class of all footballs (good or bad) and all teardrops, the spectral invariant c is a complete topological invariant." | NEEDS CORRECTION (wording) | DGGW say "complete **topological** invariant". Flat orbifolds of a fixed type have moduli (the torus, S²(2,2,2,2)), so c cannot be a complete *isometry* invariant. Write "a complete topological invariant (it determines the orbifold type)". |
| 174 | `[Prop.~5.22]` | spherical orbifolds are determined by finitely many terms | Prop. 5.22, p. 236 (pdf 32) | "Within the class of spherical 2-orbifolds of constant curvature R > 0, the spectrum determines the orbifold." Proof: "In Table 1, c distinguishes among the remaining spherical orbifolds with the exception … Equation (5.11), the coefficient of the degree −½ term, distinguishes …" | ACCURATE in substance | The statement says "the spectrum". "Finitely many terms" comes from the proof, which uses only the t^{−1}, t^{−1/2} and t^0 terms (c and (5.11)). Suggest `[Prop.~5.22 and its proof]`. |
| 174 | `[Rem.~5.16]` (1st) | DGGW: c "does not seem sufficiently strong to distinguish among" hyperbolic triangular pillows | Rem. 5.16, p. 234 (pdf 30); arXiv p. 31 identical | "Notably absent from the class C are triangular pillows with χ(O) < 0. The invariant c does not seem sufficiently strong to distinguish among these triangular pillows. However, as a special case of a result in [13], the spectrum does determine the orders of the cone points in such a 2-orbifold provided that it is endowed with a metric of constant curvature −1." | ACCURATE (quote verbatim) | DGGW speak of "triangular pillows with χ(O) < 0", with no metric. The manuscript's "hyperbolic triangular pillows" is equivalent, but the topological wording is closer to the source. |
| 174 | `[Rem.~5.16]` (2nd) | "it answers the question left open in [Rem 5.16]" | same | same; DGGW pose no question, and in the next sentence they note that the spectrum (DS09) settles the cone orders at curvature −1 | NEEDS CORRECTION (overstatement) | Rem. 5.16 is an observation, not an open question. Suggest "it confirms and makes precise the observation of [Rem. 5.16]: c first fails on O(2,8,8), O(3,3,12), and c₃ repairs it at curvature −1" (G7-6 recalibration). |
| 220 | `\cite{donnelly1976,dggw2008}` | structure: regular part plus one contribution per singular stratum | Thm 4.8, p. 220 (pdf 16) | as in the line-119 row | ACCURATE | — |
| 244 | `[Thm~4.8, Def.~4.7]` | trace ∼ I_0 + ∑ I_N/\|Iso(N)\|; I_0 = (4πt)^{−1}∑ a_k t^k; I_N is a series in t^{k−dim N/2} | Thm 4.8, p. 220; Def. 4.7(ii),(iii), pp. 219–220 (pdf 15–16) | 4.7(ii): "I_N := (4πt)^{−dim(N)/2} ∑_{k=0}^∞ t^k ∫_N b_k(N,x) dvol_N(x)". 4.7(iii): "I_0 = (4πt)^{−dim(O)/2} ∑_{k=0}^∞ a_k(O) t^k" | ACCURATE | — |
| 244 | `[\S5.6]` | an orientable 2-orbifold has only isolated singular points | 5.6 Example, p. 227 (pdf 23) | "Degree 0 term for orientable 2-orbifolds. An orientable 2-orbifold O can have only isolated singularities (i.e., cone points)." | ACCURATE | 5.6 is a numbered Example. Suggest `[Ex.~5.6]`. |
| 251 | `[\S5.6]` | Schueth attributes the order-t¹ cone coefficient to DGGW §5.6 | 5.6 Example, "Degree 1 term", pp. 228–229, (5.9)–(5.10) | (5.10): "a₂/4π + ∑_i R₁₂₁₂(m_i⁴ + 10m_i² − 11)/(360 m_i) + ∑_i R₁₂₁₂(n_i⁴+10n_i²−11)/(720 n_i)" | ACCURATE | With R₁₂₁₂ = K = −1 this is exactly −(m⁴+10m²−11)/(360m) = b₁(m) of eq. (b1). The attribution itself is Schueth's (see the schueth2019 rows). |
| 269 | `[(5.7)]` | b₀ "can be read off … from the convention of (5.7): a rotation through 2πj/m contributes ¼csc²(jπ/m) … divided by the isotropy order m" | (5.7) is p. 227 (pdf 23). The csc² convention is in Ex. 5.3, p. 226 (pdf 22); the division by \|Iso(N)\| is in Thm 4.8 | Ex. 5.3: "b₀(γ^j) = \|det((I − A_{γ^j})^{−1})\| = 1/(2 − 2cos(2jπ/m)) = 1/(4 sin²(jπ/m))". (5.7): "Hence the degree 0 term is χ(O)/6 + ∑_{i=1}^k (m_i² − 1)/(12 m_i)." | NEEDS CORRECTION (pinpoint) | (5.7) is the *result*, not the convention. Cite `[Ex.~5.3, Prop.~5.5, (5.7)]`. |
| 348 | `[Thm~5.15]` | the flat orbifolds are determined by the t⁰ coefficient (values 0, ½, ⅔, ¾, ⅚) | Thm 5.15, p. 232; Table 1, p. 231 (pdf 27) | Table 1: "O(2,2,2,2) V/t + 1/2"; "O(2,4,4) V/t + 3/4"; "O(3,3,3) V/t + 2/3"; "O(2,3,6) V/t + 5/6"; "torus, Klein bottle V/t + O(t)" | ACCURATE | The values match Table 1. |
| 349 | `[Thm~5.15, Prop.~5.22]` | at K=+1 the t⁰ coefficient determines the good orientable spherical orbifolds | Thm 5.15 (all orientable χ>0 included); Prop. 5.22 | as above | ACCURATE | — |
| 630 | `[Thm~4.8, Def.~4.7]` | expansion I_0 + ∑ I_N/\|Iso(N)\| | as at line 244 | as at line 244 | ACCURATE | — |
| 630 | `[Def.~4.7(iii)]` | a^sm_k = ∫ u_k; u_k universal in the jet of the metric, invariant under isometries | Def. 4.7(iii), p. 220; isometry invariance in 3.8, p. 214 (pdf 10) | 4.7(iii): "the invariants u^i in (3.5), which are defined in terms of the curvature and its covariant derivatives on any Riemannian manifold, also make sense on any Riemannian orbifold. The invariants a_k(O) … are given by a_k = ∫_O u^k(x,x) dvol_O(x)." 3.8: "Since each γ ∈ G_α is an isometry of W̃_α, it follows that u_i(γx̃, γỹ) = u_i(x̃, ỹ)" | ACCURATE (the invariance clause is in 3.8) | Optional: `[Def.~4.7(iii), 3.8]`. |
| 630 | `[Def.~4.7(i)]` | I_N = ∑_k t^k ∑_γ b_k(γ, p̃_i), the inner sum over the m_i − 1 nontrivial rotations | Def. 4.7(i) defines b_k(N,p) = b_k(Ñ,p̃). The sum over γ ∈ Iso^max(Ñ) is in 4.5 (p. 219). The formula for I_N is 4.7(ii). "Iso^max = all nontrivial elements" for a cone point is Ex. 5.3 (p. 226) | 4.5: "b_k(Ñ,x) = ∑_{γ∈Iso^max(Ñ)} b_k(γ,x)". Ex. 5.3: "If N = {p}, then Iso(N) is a cyclic group of order m and Iso^max(N) contains all of the nontrivial elements." | NEEDS CORRECTION (pinpoint) | Cite `[4.5, Def.~4.7(i)--(ii), Ex.~5.3]`. |
| 630 | `[\S4.1]` | Donnelly's b_k are local and universal | 4.1 Notation and Remarks, p. 218 (pdf 14) | "(i) Locality. For a ∈ W, b_k((M,γ),a) depends only on the germs at a of the Riemannian metric of M and of the isometry γ. … (ii) Universality. If M and M′ are Riemannian manifolds admitting the respective isometries γ and γ′, and if σ: M → M′ is an isometry satisfying σγ = γ′σ, then b_k((M,γ),x) = b_k((M′,γ′),σ(x))" | ACCURATE | — |
| 701 | `[Thm~4.8]` | leading term 𝒵(s) ∼ Area/4πs | Thm 4.8 with Def. 4.7(iii) | Def. 4.7(iii): "In particular, a₀ = vol(O)" | ACCURATE | Optionally add `Def.~4.7(iii)` for a₀ = vol. |
| 791 | `[Thm~4.8]` | as at line 701 | same | same | ACCURATE | — |

### ucar2017 (10 instances)

| line | cite as written | claim | location found (edoc = arXiv v1) | verbatim quote | verdict | correction |
|---|---|---|---|---|---|---|
| 172 | `[Thm~3.40, Cors~4.21(iv), 4.23]` | Uçar extended the cone-order statement to every nonzero constant curvature, using all heat invariants through a large-order limit | Cor. 4.21(iv), p. 139 (pdf 144); Cor. 4.23, p. 140 (pdf 145); Thm 3.40, p. 98 (pdf 103) | 4.21(iv): "If the mirror locus is trivial and κ ≠ 0, then κ together with the spectrum determines the number of cone points as well as the multiset of all orders {n₁,…,n_N}." Before 4.21: "Therefore we obtain, just as in Corollary 3.38 and Theorem 3.40, the following spectral invariants". Thm 3.40 proof: "we conclude by induction that the spectrum determines the sequence (W_ν)… lim_{ν→∞} γ^{2ν+1}·W_{ν,1} …" | NEEDS CORRECTION (minor pinpoint) | Thm 3.40 is about **polygons** ("Let Ω be a polygon of nonzero constant curvature"). It supplies the large-order method that Cor. 4.21 reuses. Write `[Cors~4.21(iv), 4.23; method of Thm~3.40]`. Also add "(with κ given)": Uçar's statement assumes κ is known. |
| 174 | same | cone orders and genus known as spectral invariants only via the full spectrum or all heat invariants | same | same | NEEDS CORRECTION (minor) | Same pinpoint fix as at line 172. |
| 220 | `\cite{ucar2017}` | "Uçar computed every coefficient at constant curvature" | Thm 4.20, pp. 137–138; Prop. 4.17, p. 134 | p. 134 (pdf 139): "The next result from [Wat05] which we will need, and prove here with minor corrections, is the following: Proposition 4.17." p. 144 (pdf 149): "The formula (4.33) for C contains the coefficients c^S_ℓ(π/k), which were computed by S. Watson in [Wat05]." | ACCURATE but incomplete credit | Uçar credits the lune coefficients c^S_ℓ to Watson, *The trace function expansion for spherical polygons*, N. Z. J. Math. 34 (2005) 81–95 (zbMATH 1076.35042; raw record `_fetched/bib/watson2005.bib`). Suggest "Uçar, building on Watson's lune expansion [Wat05, Lemma 15], computed…" |
| 224 | `[(4.25)]` | formula (ucarlune) | (4.25) in Prop. 4.17, p. 134 (pdf 139) | c^S_ℓ(π/k) = (1/4k) · ((−1)^ℓ/(ℓ+1)!) · (1/(2ℓ+1)) · ∑_{j=0}^{ℓ+1} binom(2ℓ+2, 2j) (k^{2j} − 1) B_{2j} B_{2ℓ+2−2j}(½) | ACCURATE: symbol for symbol, with m ↔ k and l ↔ ℓ | Uçar's own check on the same page: "observe that for k = 1 the coefficients in (4.25) vanish: c^S_ℓ(π) = 0". |
| 244 | `[Thm~4.20(i), (4.35)]` | a^sm_ν = Area·K^ν ν!^{−1}4^{−ν} ∑_l binom(ν,l)(−4)^l B_{2l}(½) | Thm 4.20(i), (4.35), p. 138 (pdf 143) | "a_ν(O) = vol(O)/(ν!·4^ν) ∑_{ℓ=0}^ν binom(ν,ℓ)(−4)^ℓ B_{2ℓ}(½) · κ^ν for all ν ∈ ℕ₀. (4.35)". The normalisation is fixed on p. 137: "(1/4πt) ∑ a_ν(O)t^ν + ∑ I_N(O)/\|Iso(N)\|" | ACCURATE | — |
| 244 | `[Thm~4.20(ii), (4.33)--(4.34)]` | a cone point of order m contributes K^ν ∑_{i≤ν} 2(4^i i!)^{−1} c^S_{ν−i}(π/m) at t^ν | Thm 4.20(ii), p. 138; (4.33)–(4.34), p. 137 (pdf 142) | 4.20(ii): "If N consists of a cone point of order k ∈ ℕ, then I_N(O)/\|Iso(N)\| = C." (4.33): "C = ∑_{ν=0}^∞ ∑_{ℓ=0}^ν 2/(4^ℓ·ℓ!) · c^S_{ν−ℓ}(π/k) κ^ν t^ν". (4.34): "(1/k) ∑_{ℓ=1}^{k−1} b_ν(D̃_ℓ) = ∑_{ℓ=0}^ν 2/(4^ℓ·ℓ!) · c^S_{ν−ℓ}(π/k) κ^ν" | ACCURATE | — |
| 346 | `[Thm~4.20]` | Prop. 2.4 holds at any constant K with K^l | Thm 4.20, pp. 137–138 | "Let O be a two-dimensional closed Riemannian orbifold of constant curvature κ ∈ ℝ." The κ^ν factors are in (4.33) and (4.35) | ACCURATE | — |
| 349 | `[Cor.~4.21(iv)]` | (b) "The t⁰ coefficient determines them …, [Cor 4.21(iv)]" | Cor. 4.21(iv) | quoted in the line-172 row | NEEDS CORRECTION | Cor. 4.21(iv) uses the *whole* spectrum (all heat invariants, with κ given), not the t⁰ coefficient. Move the cite to a clause such as "(as does the full sequence of heat invariants, [Cor. 4.21(iv)])". |
| 361 | `[Cor.~4.21(iv)]` | a tail (c_j)_{j≥J} determines the cone orders: "a small strengthening of [Cor 4.21(iv)], whose extraction starts at the first coefficient" | Cor. 4.21(iv); method in the proof of Thm 3.40 | Thm 3.40 proof: "Therefore, the spectrum also determines the value of the sum ∑ e_ν(γ_i) for all ν ∈ ℕ₀ … we conclude by induction that the spectrum determines the sequence (W_ν)_{ν∈ℕ₀}" | ACCURATE | — |
| 1286 | `[Thm~4.10, Cor.~4.18]` | the identity 𝒵_O = 𝒵_N + 𝒵_D for a reflection double "is used by Uçar for spherical lunes" | Thm 4.10, p. 125 (pdf 130); Cor. 4.18 and proof, pp. 135–136 (pdf 140–141) | (4.7): "Z_{M/Z_k}(t) − Z_{M/D_k}(t) = Z_Ω(t) for all t > 0", with Ω the lune and Z_Ω its Dirichlet trace. Cor. 4.18 proof: "the Dirichlet and Neumann heat kernels can be written as K_S(x,y;t) = K_{S²(r)}(x,y;t) − K_{S²(r)}(x,σ(y);t), K^N_S(x,y;t) = K_{S²(r)}(x,y;t) + K_{S²(r)}(x,σ(y);t) … so Z_S(t) + Z^N_S(t) = 2Z_{S²(r)}(t)" | ACCURATE | In Thm 4.10 the "Neumann" side appears as the reflection orbifold M/D_k, not as a Neumann problem. The hemisphere identity in Cor. 4.18 is literally Dirichlet + Neumann. The wording is fine. |

The brief mentions "Cor. 4.22". The manuscript does not cite a "Cor. 4.22", and in Uçar **4.22 is a Definition** (orbifold Euler characteristic, p. 139). Any such pinpoint would be wrong.

**Does Uçar credit the K = −1 case of Cor. 4.23 to Dryden–Strohmaier? Yes.** Uçar p. 140 (pdf 145): "This fact was previously known in the special case of closed orientable orbisurfaces of constant curvature κ = −1 (see [DS09, Proposition 3.3]). … Thus, Corollary 4.23 is a new proof of [DS09, Proposition 3.3] using only heat invariants, in addition to being a generalisation of it." On Cor. 4.21(iv), p. 139: "statement (iv) is also new in this generality and was only known for the special case of κ = −1".

### drydenstrohmaier2009 (11 instances)

The manuscript cites the CMB version (bib: CMB 52 (2009) 66–71), so page pinpoints must be CMB pages.

| line | cite as written | claim | location found (CMB) | verbatim quote | verdict | correction |
|---|---|---|---|---|---|---|
| 172 | `[Thm~1.1]` | the spectrum of a compact orientable hyperbolic orbisurface determines the number of cone points of each order | Thm 1.1, p. 67 (pdf 2) | "Let O be a compact orientable hyperbolic orbisurface. The Laplace spectrum of O determines its length spectrum and the number of cone points of each possible order. Knowledge of the length spectrum and the number of cone points of each order determines the Laplace spectrum." | ACCURATE | — |
| 174 | `[Thm~1.1, Prop.~3.3]` | cone orders and genus via the full spectrum | Thm 1.1; Prop. 3.3, p. 70 (pdf 5) | Prop. 3.3: "Isospectral compact orientable hyperbolic orbisurfaces have the same underlying topological space." | ACCURATE | — |
| 178 | `[Thm~1.1]` | the spectrum determines the cone orders | Thm 1.1 | as above | ACCURATE | — |
| 192 | `[Thm~3.2]` | orbifold Gauss–Bonnet | Thm 3.2, p. 70 (pdf 5) | "Let O be a Riemannian orbisurface. Then ∫_O K dA = 2πχ(O), where K is the curvature and χ(O) is the orbifold Euler characteristic of O." (Def. 3.1: "χ(O) = χ(X_O) − ∑_{j=1}^s (1 − 1/m_j)") | ACCURATE | — |
| 662 | `[p.~3]` | closed geodesics correspond to conjugacy classes of the countable group Γ | p. 68 (pdf 3) = arXiv v2 p. 3 | "The set of hyperbolic conjugacy classes P may be identified with the set of closed periodic geodesics in O of length ln N(P)." | NEEDS CORRECTION (page) | "p. 3" is the arXiv v2 page. In the cited CMB version it is **p. 68**. Countability of Γ is not stated there; it is immediate because Γ is discrete in PSL(2,ℝ). |
| 679 | `[eq.~(1)]` | normalization g = (1/2π)∫h e^{−iru}dr, "fixed there by the wave example h(r)=cos(rt)" | (1), p. 67 (pdf 2); the wave example is on p. 69 (pdf 4) | p. 68: "The function g is the Fourier transform of h". p. 69: "a direct calculation of g yields g[ln N(P)] = ½[δ(ln N(P) − t) + δ(ln N(P) + t)]" | ACCURATE (an inference, correctly drawn) | The normalisation is fixed on p. 69 in the derivation of (2), not in (1). Suggest "this is the normalization of [eq. (1)], as fixed by the wave example on p. 69". |
| 693 | `[eq.~(1)]` | trace formula ∑h(r_n) = identity + hyperbolic + elliptic for even entire h of uniform exponential type | (1), p. 67; hypotheses p. 68 | (1): "∑_{n=0}^∞ h(r_n) = (µ(F)/4π)∫_{−∞}^{∞} r h(r) tanh(πr) dr + ∑_{{P} hyperbolic} (ln N(P_c))/(N(P)^{1/2} − N(P)^{−1/2}) g[ln N(P)] + ∑_{{R} elliptic} 1/(2m(R) sin θ(R)) ∫_{−∞}^{∞} e^{−2θ(R)r}/(1 + e^{−2πr}) h(r) dr". p. 68: "where h is any entire function of uniform exponential type and h(r) = h(−r)." | ACCURATE | The identity, hyperbolic and elliptic terms of Thm 4.6 match (1) term by term with θ = πj/m. |
| 693 | `[p.~3]` | each cone point of order m gives the classes ρ^j, 1 ≤ j ≤ m−1 | p. 68 (pdf 3) | "θ(R) = πl/m(R) where 1 ≤ l ≤ m(R) − 1. We may identify the set of primitive elliptic conjugacy classes R in Γ with the set of cone points in O of order m(R)." | NEEDS CORRECTION (page) | p. 3 → **p. 68**. |
| 697 | `[eq.~(1)]` | (1) holds for h_ρ of exponential type | (1), p. 67 | as above | ACCURATE | — |
| 795 | `[Thm~1.1]` | the spectrum determines the length spectrum | Thm 1.1 | as above | ACCURATE | — |
| 840 | `[Thm~1.1]` | isospectral hyperbolic triangle orbifolds are isometric "also follows from" Thm 1.1 | Thm 1.1 | as above | ACCURATE | Thm 1.1 gives equal cone orders, and triangle rigidity then gives isometry. Optional: "with Prop. 5.x (rigidity)". |

### doylerossetti2011

| line | cite as written | claim | location found | verbatim quote | verdict | correction |
|---|---|---|---|---|---|---|
| 172 | `[Thm~1]` | the spectrum determines and is determined by volume, mirror length, cone points and closed geodesics | v2 Thm 1, p. 2 (also v1 Thm 1, p. 2) | "Theorem 1. Let M be a compact hyperbolic 2-orbifold (not necessarily connected). The Laplace spectrum of M determines, and is determined by, the following data: 1. the volume; 2. the total length of the mirror boundary; 3. the number of conepoints of each order, counting a mirror corner as half a conepoint of the corresponding order; 4. the number of closed geodesics of each length and orientability class …" | ACCURATE | — |
| 172 | `[\S3, p.~8]` | quote "is there in the short-time asymptotics … asymptotic expansion" | v2 §3 "Background", p. 8 | "Restricted to hyperbolic 2-orbifolds, the results they state don't yield complete information about the singular set. All this information is there in the short-time asymptotics of the heat trace, however, and presumably it could be extracted using their approach, by looking at higher and higher terms in the asymptotic expansion." ("their" = Dryden–Gordon–Greenwald–Webb [7]) | ACCURATE for v2; **VERSION-DEPENDENT** | In v1 (2011) the same sentence (identical wording) is in **§4** "Background", p. 8. The bib says year 2011, but §3 is the v2 (10 Apr 2014) numbering. Fix the bib: "arXiv:1103.4372v2 (2014)". Alternatively keep 2011 and write §4. |

**Journal publication?** None found:
- **Crossref.** A `query.bibliographic` search on the full title returns no Doyle–Rossetti item.
- **zbMATH Open.** Searching `au:Doyle & au:Rossetti` returns only Zbl 1146.58026 (NYJM 2008, "Isospectral hyperbolic surfaces have matching geodesics"), Zbl 1091.58021 (Tetra and Didi) and the arXiv-only record arXiv:1103.4372.
- **arXiv.** The API shows no journal_ref.

**Conclusion:** cite it as an arXiv preprint. The related *published* work is Doyle–Rossetti, NYJM 14 (2008), Zbl 1146.58026, on manifolds. It does not contain the quoted sentence; this was not checked here, and it is out of scope.

### schueth2019

| line | cite as written | claim | location found (AIF) | verbatim quote | verdict | correction |
|---|---|---|---|---|---|---|
| 251 | `[Rem.~4.2, Thm~4.1]` | p₁, p₂ agree with Schueth's cone coefficients, which she attributes to DGGW §5.6 at order t¹ | Thm 4.1, p. 2844 (pdf 19); Rem. 4.2, p. 2845 (pdf 20); arXiv p. 14, same numbers | Thm 4.1: "a₂^{({p̄})} = ((1/2520)(k⁵ − 1/k) + (1/720)(k³ − 1/k) + (1/180)(k − 1/k)) K(p)² − ((1/15120)(k⁵−1/k) + (1/1440)(k³−1/k) + (1/180)(k−1/k)) Δ_g K(p)." Rem. 4.2: "a₀^{({p̄})} = (1/12)(k − 1/k), a₁^{({p̄})} = ((1/360)(k³ − 1/k) + (1/36)(k − 1/k)) K(p) … Note that the above formulas for a₀^{({p̄})} and a₁^{({p̄})} were already computed in [9, 5.6]." | ACCURATE | Checked: (1/2520+1/720+1/180) = 37/5040, which matches p₂(m)/m at K²=1. Schueth's attribution to DGGW covers orders t⁰ **and** t¹. |
| 311 | `[Rem.~4.2]` | b₁ is the constant-curvature cone coefficient at K = −1 | Rem. 4.2 | as above | ACCURATE | — |

### adfg2008, donnelly1976, mckeansinger1967, kac1966, marklof2011

| line | cite as written | claim | location found | verbatim quote | verdict | correction |
|---|---|---|---|---|---|---|
| 174 | `adfg2008 [Thm~1]` | "Finitely many heat invariants also recover the singularity orders of weighted projective planes" | arXiv v1 Thm 1, p. 2 | "Theorem 1. Let M := CP²(N₁,N₂,N₃) be a four-dimensional weighted projective space with isolated singularities, equipped with a Kähler metric. Then the spectra of the Laplacian acting on 0- and 1-forms on M determine the weights N₁,N₂,N₃." Next sentence: "Note that we need to consider the spectrum of the Laplacian acting on both 0- and 1-forms. We conjecture that the spectrum of the Laplacian acting on 0-forms determines the weights" | NEEDS CORRECTION (wording) | Write "finitely many heat invariants of the Laplacians on 0- and 1-forms (or on functions together with the Euler characteristic)". The proof (§6.1) uses a₀, a₁, a₂ for 0- and 1-forms; the abstract adds "we can replace knowledge of the spectrum on 1-forms by knowledge of the Euler characteristic". Theorem numbering in the published AGAG version is unverified (gap 1). |
| 119, 220, 630 | `donnelly1976` | the heat expansion for isometries; b_k local and universal | Introduction, p. 161 (scan p. 2) | "The main result is that there is an asymptotic expansion as t↓0: ∑_λ Tr(f*_λ)e^{λt} ∼ ∑_{N∈Ω}(4πt)^{−n/2} ∑_{k=0}^∞ t^k ∫_N b_k(f,a) dvol_N(a) where b_k(a,f) = \|det B\| b′_k(a,f) and b′_k(a,f) is an O(n)×O(d−n) invariant polynomial in the components of B and the curvature tensor R of M and its covariant derivatives at a. One has b′₀(a,f) = 1. Theorem 5.1 gives an explicit formula for b′₁(f,a)." | ACCURATE | (Transcribed from the scan image; "f*_λ" is the induced map on eigenspaces.) |
| 119 | `mckeansinger1967` | heat coefficients are curvature integrals and spectral invariants (manifold case) | (5a), p. 44 | "(4πt)^{d/2}Z = the (Riemannian) volume of M + (t/3) × the curvatura integra ∫_M K + (t²/180)∫_M (10A − B + 2C) + o(t³)" (OCR of the scan; the line continues "esp., the Euler characteristic of M is audible.") | ACCURATE | — |
| 119 | `kac1966` | Kac's question | pp. 2–3 | "Assume that for each n the eigenvalue λ_n for Ω₁ is equal to the eigenvalue μ_n for Ω₂. Question: Are the regions Ω₁ and Ω₂ congruent in the sense of Euclidean geometry?" | ACCURATE | — |
| 693 | `marklof2011` | "For torsion-free groups the heat function is known to be admissible" | arXiv v2 §11, proof of Prop. 10 (Weyl's law), p. 26; setting §9, p. 22 | "For any β > 0, the test function h(ρ) = e^{−βρ²} is admissible in the trace formula." Setting: "the kernel k_Γ(z,w) of a general hyperbolic surface Γ\H² (with Γ strictly hyperbolic)" | ACCURATE | Add the pinpoint `[\S11]`. CUP page numbers are unverified (gap 2). Marklof treats h(ρ) = e^{−βρ²}. The shift e^{−β/4} appears in (193), so h_t of the manuscript is covered. |

---

## 2. The DGGW erratum (Michigan Math. J. 66 (2017) 221–222)

- **DOI:** 10.1307/mmj/1488510034. Found via the Crossref record of the article, the Project Euclid URL pattern and Unpaywall. The Crossref title is "Erratum to ''Asymptotic expansion of the heat kernel for orbifolds''", vol. 66, issue 1, issued 2017-03-01. zbMATH: Zbl 1404.58043. zbMATH also cross-links it in the record of the original, Zbl 1175.58010: "erratum ibid. 66, No. 1, 221-222 (2017)".
- **Raw BibTeX:** `_fetched/bib/dggw2017erratum.bib` (Crossref content negotiation, https://doi.org/10.1307/mmj/1488510034).

**What it corrects (verbatim, p. 221):**
> "In Theorem 5.1 (one of the applications of the heat invariants), there is an implicit assumption that Iso^max(N) is nontrivial. Thanks to a question from Naveed Bari, we now realize that Iso^max(N) may be trivial. The strata for which Iso^max(N) is trivial do not appear in the heat invariants, necessitating the addition of a hypothesis to Theorem 5.1."

The erratum then gives an example: the Klein 4-group of π-rotations about the axes acting on ℝ³, where the origin is a 0-dimensional stratum with trivial Iso^max. It restates the theorem:

> "5.1. Theorem. Let O be a Riemannian orbifold with singularities. If O is even dimensional (respectively, odd dimensional) and if there exists an odd-dimensional (respectively, even-dimensional) O-stratum N of the singular set with Iso^max(N) nontrivial, then O cannot be isospectral to a Riemannian manifold. We remark that Iso^max(N) is nontrivial for all strata N that have maximal dimension within any given component of the singular set."

**Effect on the manuscript: none.**
- The erratum amends only Theorem 5.1. The manuscript never uses it.
- Theorem 4.8, Definition 4.7, 4.1, 4.5, Examples 5.3/5.6, (5.7), (5.10), Theorems 5.14–5.15, Remark 5.16 and Proposition 5.22 are untouched.
- For a cone point, Iso^max(N) consists of all nontrivial rotations (Ex. 5.3), so it is never trivial.
- The "strata with trivial Iso^max contribute nothing" clarification is already implicit in 4.5, where the sum is empty.

**Recommendation.** The erratum is not in `paper/jga/references.bib`; it is only in `refs/sources.bib`. Add it and cite it next to the first `dggw2008` cite (e.g. line 119 or 220) as "see also the erratum [dggw2017erratum], which concerns only Thm 5.1". This closes G7-6(iii).

---

## 3. Remark 4.12 / Lemma 2.5: what DGGW and Uçar prove about the cone contribution at every order l

**DGGW (published).** There is **no closed form for every order.**
- **General k (§4.2, p. 218–219, quoting Donnelly).** Only the structural form: "b_k(γ,x) = \|det(B_γ(x))\| b̃_k(γ,x), where b̃_k(γ,·) is an O(m)×O(n−m) universal invariant polynomial in the components of B_γ and in the curvature tensor R of M and its covariant derivatives." Explicit formulas are given only for b₀ (4.3) and b₁ (4.4, from Donnelly's Thm 5.1).
- **Cone points, order t⁰.** Ex. 5.3 gives b₀(γ^j) = 1/(4 sin²(jπ/m)). Lemma 5.4 gives ∑ csc²(jπ/m) = (m² − 1)/3. Prop. 5.5 gives "I_N = (m² − 1)/12 + O(t)". The degree-0 term is (5.7).
- **Cone points, order t¹.** Ex. 5.6, "Degree 1 term" (p. 228–229): "b₁(γ^j) = R₁₂₁₂/(8 sin⁴(jπ/m))". With ∑ csc⁴(jπ/m) = (m⁴ + 10m² − 11)/45 this becomes (5.10): R₁₂₁₂(m⁴+10m²−11)/(360m). Prop. 5.20 (p. 236) restates it at constant curvature as "(m_i²+11)(m_i²−1)/(360 m_i)".
- **No order t^l with l ≥ 2 appears anywhere in DGGW.**
- **Donnelly 1976 is the same.** p. 161: "One has b′₀(a,f) = 1. Theorem 5.1 gives an explicit formula for b′₁(f,a)." Beyond k = 1 there is only the structure.

**Schueth 2019.** Order t² (Thm 4.1), for variable curvature. Orders t⁰ and t¹ are in Rem. 4.2, credited to DGGW 5.6. Nothing beyond t².

**Uçar 2017.** Every order, at constant curvature κ only.
- **Formula.** Thm 4.20(ii) with (4.33)/(4.34) and the lune coefficients (4.25) of Prop. 4.17.
- **Credit to Watson.** (4.25) is Watson's lune heat-trace expansion [Wat05, Lemma 15], reproved "with minor corrections" (p. 134). Uçar also flags errors in Watson's Lemma 11 (pp. 135–136, Remark after Prop. 4.17).
- **Transfer from the sphere.** Uçar moves from S²(r) (κ > 0) to arbitrary κ in the proof of Thm 4.20 (p. 138), using "[Don76, Theorem 5.1], cited also in [DGGW08]: The functions b_i(γ,x) … are of the form ϕ(γ,x)·ψ(γ,x), where ϕ(γ,x) only depends on the Euclidean isometry dγ_x and ψ(γ,x) is a universal polynomial in the curvature tensor of O and its covariant derivatives." So the κ < 0 case is reached by a universality/homogeneity argument from the spherical lune, not by a direct hyperbolic computation.
- **No polynomial statement.** Uçar does **not** state Lemma 2.5: nothing on evenness, degree 2l+2, the leading coefficient or p_l(1) = 0. These are read off (4.25) by the manuscript.
- **Polygon side.** The same leading-coefficient computation appears for polygons in the proof of Thm 3.40 (p. 98): "the coefficient of the highest power term … corresponds to ℓ = ν, j = ν+1 in (3.114) and equals (−1)^ν B_{2ν}/(4(ν+1)!(2ν+1))".

**Consequences for the referees' request (G7-3).**
1. Neither DGGW nor Donnelly can replace Uçar for Lemma 2.5. They give closed forms only for l = 0, 1, and only the K^l-homogeneity and locality for general l.
2. The only Uçar-free all-l route in the cited literature is the elliptic term of the trace formula, DS09 eq. (1) (from Hejhal/Iwaniec, refs [7, 8] there), i.e. the manuscript's E_m(t) of Thm 4.6.
3. Remark 4.12 currently says this route is "a cross-check …, not an independent proof", because Lemma 4.7 uses the leading term of DGGW Thm 4.8. That only makes the route depend on DGGW's leading term a₀ = vol (Def. 4.7(iii)), which is refereed and independent of Uçar. It is not circular for Lemma 2.5.
4. A sketch of the derivation, my own algebra (not a source quote):
   - Expand e^{−tr²} under the integral. M_{2i}(a) := ∫ r^{2i}e^{−ar}/(1+e^{−2πr})dr = (d/da)^{2i}[1/(2 sin(a/2))].
   - Even derivatives of csc x are odd polynomials in csc x with top term (2i)! csc^{2i+1}x.
   - ∑_{j=1}^{m−1} csc^{2r}(πj/m) is a polynomial in m of degree 2r, with leading term 2ζ(2r)m^{2r}/π^{2r}.
   - The top coefficient at t^l then comes out as (−1)^l m^{2l+1}\|B_{2l+2}\|/(2(l+1)!(2l+1)). This agrees with Lemma 2.5's leading coefficient for b_l = (−1)^l p_l/m.
   - What the paper would still need to prove in this route: parity and polynomiality of the csc-power sums in m (classical; cf. Berndt–Yeap, already cited), p_l(1) = 0 (the empty sum), and validity of the term-by-term expansion. The last holds because the kernel decays exponentially in both directions.
5. Uçar plus Watson can stay as corroboration. If Uçar remains the primary source, credit Watson [Wat05] for (4.25).

---

## 4. Bibliographic record check (references.bib vs raw fetched records)

| key | raw record (file, source URL) | references.bib vs record | action |
|---|---|---|---|
| dggw2008 | `bib/dggw2008.bib` (https://doi.org/10.1307/mmj/1213972406, Crossref; no pages in the record); `bib/dggw2008_zbmath.bib` (https://zbmath.org/bibtex/1175.58010.bib: pages 205–238) | authors, title, 56(1), 205–238, 2008 match | none |
| dggw2017erratum | `bib/dggw2017erratum.bib` (https://doi.org/10.1307/mmj/1488510034; pages from the PDF and zbMATH 1404.58043: 221–222) | **missing** from references.bib | add it |
| ucar2017 | `bib/ucar2017.bib` (https://doi.org/10.18452/18463, DataCite via doi.org; publisher Humboldt-Universität zu Berlin, 2017) | title, school and year match; no DOI | add `doi = {10.18452/18463}` (and the edoc URL). Keep the arXiv eprint |
| drydenstrohmaier2009 | `bib/drydenstrohmaier2009.bib` (https://doi.org/10.4153/cmb-2009-008-0) | match (52(1), 66–71, 2009) | none. Fix the "p. 3" pinpoints to p. 68 |
| doylerossetti2011 | `bib/doylerossetti2011.bib` (https://doi.org/10.48550/arXiv.1103.4372, DataCite: year 2011); `bib/doylerossetti2011_arxivapi.xml` (arXiv API: v2 updated 2014-04-10) | match as a 2011 preprint | the pinpoint §3 is v2's. State "v2, 2014" or change §3 to §4 |
| donnelly1976 | `bib/donnelly1976.bib` (https://doi.org/10.1007/bf01436198) | match (224(2), 161–170, 1976) | none |
| schueth2019 | `bib/schueth2019.bib` (https://doi.org/10.5802/aif.3338) | match except the year: Crossref gives 2020 (issued 2020-06-26 online); the article prints "Tome 69, no 7 (2019), p. 2827-2855" | keep 2019, the printed year |
| adfg2008 | `bib/adfg2008.bib` (https://doi.org/10.1007/s10455-007-9092-6) | Crossref: online 2007-11-03, print 2008-06, 33(4), 373–395; bib has 2008 | none (2008 is the print year) |
| mckeansinger1967 | `bib/mckeansinger1967.bib` (https://doi.org/10.4310/jdg/1214427880; no pages; the article header reads "1 (1967) 43-69"; zbMATH 0198.44301: 43–69) | match | none |
| kac1966 | `bib/kac1966.bib` (https://doi.org/10.1080/00029890.1966.11970915; written by another worker, matches the Crossref API JSON fetched here) | match (73, 4P2, 1–23) | none |
| marklof2011 | `bib/marklof2011.bib` (https://doi.org/10.1017/cbo9781139108782.003; written by another worker, matches the Crossref JSON: pages 83–120); `bib/marklof2011_arxivapi.xml` (arXiv journal_ref says "pp. 83-119", eds. J. Bolte and F. Steiner) | pages 83–120 match Crossref | optionally add `editor = {Bolte, J. and Steiner, F.}` |
| (watson2005, recommended) | `bib/watson2005.bib` (https://zbmath.org/bibtex/1076.35042.bib) | not in references.bib | add it if (4.25) is credited to Watson |

---

## 5. Instrument gaps

1. **ADFG, published version.** Ann. Global Anal. Geom. 33 (2008), DOI 10.1007/s10455-007-9092-6: Unpaywall `is_oa: false`, and no attempt was made past the paywall. Theorem 1 was verified in arXiv:math/0608462v1 only. Numbering in the published version is unverified.
2. **Marklof, CUP chapter.** DOI 10.1017/cbo9781139108782.003: Unpaywall `is_oa: false`. Verified in arXiv:math/0407288v2 only (§11, Prop. 10, p. 26). The CUP page and section numbering are unverified.
3. **Donnelly 1976.**
   - `link.springer.com/content/pdf/10.1007/BF01436198.pdf` returned an HTML page, not the PDF.
   - eudml.org/doc/162906 returned 403.
   - The GDZ search URL returned 404.
   - The article *was* retrieved from GDZ (`PPN235181684_0224/LOG_0035.pdf`, 200), but as an image-only scan with no text layer. Only the Introduction (p. 161) was read, as a rendered image. The quote is a visual transcription, and Theorem 5.1 was not read.
4. **McKean–Singer.** The PDF text layer is a poor OCR. The (5a) quote is the OCR output, cross-checked by eye against its structure, and was not reread as an image.
5. **Kac.** Read from a third-party course copy of the JSTOR scan (math.ucdavis.edu), not from the publisher.
6. **Doyle–Rossetti journal search.** This was limited to Crossref bibliographic search, the zbMATH Open API and arXiv metadata. MathSciNet was not consulted (subscription).
7. **Watson 2005** (N. Z. J. Math. 34, 81–95) was not fetched. The attribution of (4.25) to Watson rests on Uçar's own statements (pp. 134, 144).
