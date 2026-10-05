# E: forward-citation and missing-literature sweep

This report covers the paper "How much of a hyperbolic orbifold does heat hear?" (paper/jga/manuscript.tex, intended for The Journal of Geometric Analysis).

- **Search log:** every query, the instrument used, the hit count and the hits retained are in `review/literature-pass/work/E-search-log.md`.
- **Raw records:** `review/literature-pass/_fetched/` (subfolders `txt/E_search/`, `pdf/E_*`, `txt/E_*`, `bib/`).
- **Prior notes extended, not repeated:**
  - review/audit/literature/PRIORITY-notes.md
  - review/audit/literature/search/
  - review/literature/stability-inverse-spectral.md
  - review/literature/theorem-A-prior-art.md
  - review/hyperresearch/Q2-cone-coefficients.md
  - review/hyperresearch/Q4-stability.md

Labels for the paper's results, used throughout:

- **(1)** signature count ⌊Area/π⌋+4, no uniform count, and n invariants for spheres with n cone points.
- **(2)** locality: invariants depend only on the signature, and moduli enter at order t^{-1/2}e^{-ℓ²/4t}.
- **(3)** triangle threshold p+q+r ≤ 17, the minimal pair (2,8,8)/(3,3,12) and its isolation, and three invariants always suffice.
- **(4)** stability with Hölder exponent 1/k.

---

## 0. Bottom line on the novelty questions

1. **Finite, explicit coefficient count for hyperbolic orbifolds? None found.**
   - The (a) forward-citation chase covered about 60 distinct citing works of DGGW, Dryden–Strohmaier and Uçar, from OpenAlex and Semantic Scholar.
   - The (b)–(e) sweeps covered roughly 40 arXiv full-text queries, 19 arXiv API queries, 14 zbMATH queries, OpenAlex and Consensus searches, and WebSearch.
   - None of these produced a finite heat-coefficient count for hyperbolic orbifolds. The qualified claim in the manuscript (line 176: "to our knowledge the first explicit finite number … ⌊Area/π⌋+4 … uniformly") **survives**.
2. **Determinacy threshold for triangle orbifolds from heat invariants? None found.**
   - There is a close **length-spectrum** analogue that the manuscript does not cite: **E. Philippe (2008, 2010)**. He proves that triangle groups Γ(r,p,q) are determined by their length spectrum, in practice by the first two or three lengths with multiplicities.
   - Along the way he lists "systolic twins": distinct triangle groups with equal systole, such as Γ(2,3,10)/Γ(2,5,5) and Γ(2,10,10)/Γ(4,4,5).
   - This does **not** pre-empt (3), which is about heat invariants. It is directly relevant prior work on finite-data rigidity of triangle orbifolds and **must be cited** (§2.2).
3. **Stability estimate for recovering cone orders? None found.**
   - No source states a quantitative estimate for cone orders or angles from heat or spectral data.
   - The super-resolution literature has the matching phenomenon for Prony systems with unknown amplitudes: Akinshin–Batenkov–Yomdin 2015 and Batenkov–Goldman–Yomdin 2020. There the exponent for an ℓ-node cluster is 1/(2ℓ−1), not 1/k (§2.7).
   - The 1/k exponent claim survives. The stability section should cite this literature next to Ostrowski.
4. **Scoops posted 2024–2026: none.** The scoop searches all returned nothing relevant:
   - full-text `"triangle orbifold" heat invariants`;
   - `"cone orders" heat trace`;
   - `"(2,8,8)"`;
   - `"2,8,8" orbifold`;
   - `"hear the signature"`;
   - `"Egyptian fraction(s)"` with heat or orbifold;
   - `"finitely many heat invariants"`;
   - `"first n heat invariants"`;
   - `"inverse spectral" "triangle orbifold"`;
   - date-sorted arXiv API sweeps of orbifold, heat and cone queries.

   The only 2024–2026 item on orbifold heat coefficients is Schueth 2025, which treats curved cones and b_{1/2} (§2.1).
5. **(c) Closed form for the cone contribution at every order.**
   - **Hyperbolic.** Uçar (4.25) is still the only explicit closed form found for curvature −1.
   - **Peer-reviewed attestation.** Schueth, Ann. Global Anal. Geom. 2025, now states in a refereed journal that Uçar computed every b_ℓ(C) in closed form, with b_ℓ = κ^ℓ·(1/n)·p_ℓ(n) and deg p_ℓ = 2ℓ+2. Cite it **alongside** Uçar.
   - **Spherical.** Watson 2005 covers K = +1 (spherical polygons).
   - **Exact integral form at K = −1.** Donnelly 1979, as quoted by Dowker 2023, eq. (1), gives an exact integral formula for a cone point of order p. I checked numerically that it reproduces Uçar's coefficients (§2.5).
   - **The constant term (m²−1)/(12m)** goes back to Cheeger 1983, (4.42), and Brüning–Seeley 1987, p. 424, in the form (1/12)(2π/γ − γ/2π). Kokotov states it as a theorem for flat cones, and Aldana–Kirsten–Rowlett re-derive it (§2.4).

---

## 1. Citation table for statements checked in this pass

| manuscript line | cite as written | claim | source location | verbatim quote | verdict | correction |
|---|---|---|---|---|---|---|
| 220 | `\cite{ucar2017}` "Uçar computed every coefficient at constant curvature" | Every cone coefficient at constant curvature is in closed form | Schueth 2025, arXiv:2511.22255v1, p. 2 (pdf p. 2), §1 | "Uçar [13] obtained explicit formulas for all bℓ (C) for cone points C of two-dimensional orbifolds under the special assumption that the orbifold has constant curvature κ ∈ R. … bℓ (C) can then be written as κℓ times (1/n) pℓ (n), where n is the order of the cone point and pℓ is a certain polynomial of order 2ℓ + 2." | ACCURATE (independent attestation) | Optional: add "see also \cite{schueth2025}" |
| 269 | `\cite[(5.7)]{dggw2008}` for b₀ = (m²−1)/(12m) | Constant cone term | Schueth 2025, p. 1: "b0 (C) = 1/12 ( 1/f′(0) − f′(0)) (see [2], p. 424)", where [2] is Brüning–Seeley JFA 73 (1987). AKR arXiv:2010.02776v3, pdf p. 17: "For a cone angle γ at the cone point p, this contribution has been computed in [20, 4.42]", where [20] is Cheeger JDG 18 (1983), giving "(2π)² − γ² / 24πγ" | as quoted | ACCURATE. With f′(0) = 1/m, or γ = 2π/m, both reduce to (m²−1)/(12m) | Optional history cite: Cheeger (4.42), Brüning–Seeley p. 424 |
| 791 | Expansion of the elliptic term E | All cone coefficients via the elliptic term of the trace formula | Dowker 2023, arXiv:2311.12708v2, pdf p. 2, eq. (1); pdf p. 7 | "Donnelly, [3], shows that the contribution of an elliptic fixed point of order p to the traced … heat–kernel is, Kp (t) = e^{−t/4}/(4πt)^{1/2} · (1/p) Σ_{m=1}^{p−1} ∫_0^∞ dx e^{−x²/t} cosh x/(sin²(πm/p) + sinh² x)" and "the coefficients can be obtained, exactly, just from the elliptic heat–kernel" | Consistent: my numerical check of (1) at p = 2, 3, 5 gives (K_p − (p²−1)/12p)/t → −(p⁴+10p²−11)/(360p) | None needed; Donnelly 1979 is an optional extra cite |

Note on the Dowker check. A direct t-expansion of the Selberg elliptic term Σ_k (2m sin θ_k)^{-1} ∫ e^{-t(1/4+r²)} e^{-2θ_k r}/(1+e^{-2πr}) dr at m = 2, 3, 5 reproduces Uçar's b₀, b₁ and b₂ to 12 digits. The script is in the session; the values are in the log. This is an independent confirmation of the manuscript's eq. (4)/(5) and of the next order.

---

## 2. Relevant works found: full reference, key statement, relation to (1)–(4), where to cite, and novelty impact

### 2.1 Schueth 2025, curved conic singularities **[must cite; (c)]**

- **Reference.**
  - Raw Crossref BibTeX: `_fetched/bib/schueth2025.bib`, from https://doi.org/10.1007/s10455-025-10024-1.
  - D. Schueth, *Heat coefficients of surfaces with curved conical singularities*, Ann. Global Anal. Geom. **69** (2025), no. 1, article no. 2.
  - arXiv:2511.22255. The arXiv API record is `_fetched/bib/schueth2025_arxiv.xml`.
- **What it proves.**
  - An explicit formula for b_{1/2}(C) when the cone metric dr² + f(r)²dθ² has f″(0) ≠ 0.
  - b_{1/2} varies irrationally under rescaling, "a sharp contrast to the behavior of b0 (C) and of those coefficients bj (C) which appear in certain known formulas in the case of orbifold cone points" (abstract).
- **Key statement for us.** The Uçar sentence quoted in §1 (p. 2). Also on p. 2: "Passing to an orbifold cone point of order n just corresponds to passing from f to f/n, so f″(0) = 0 still holds for cone points in orbisurfaces." So no half-integer or log terms occur for orbifold cone points, consistent with the manuscript's expansion.
- **Relation to the results.**
  - **(1) and (2):** supports the input formula, a refereed attestation of Uçar's all-order closed form.
  - **(3) and (4):** none.
- **Where to cite.** Line 220 (Section "The expansion"), as "see also [Schueth 2025, §1]". This answers any referee worry that the all-order input rests only on a thesis.
- **Novelty impact.** None. It confirms that nobody had extracted cone orders from finitely many coefficients.

### 2.2 Philippe 2008 and 2010: triangle groups are determined by their length spectrum **[must cite; (e), (3)]**

**References.** Raw records are in `_fetched/bib/`.

| Paper | Crossref record | zbMATH record |
|---|---|---|
| E. Philippe, *Les groupes de triangles (2,p,q) sont déterminés par leur spectre des longueurs*, Ann. Inst. Fourier **58** (2008), no. 7, 2659–2693, DOI 10.5802/aif.2424; arXiv:0807.4746 | `philippe2008.bib` (the title field contains raw MathML, so use the zbMATH record for the title) | `philippe2008_zbmath.bib` (Zbl 1202.20049) |
| E. Philippe, *Sur la rigidité des groupes de triangles (r,p,q)*, Geom. Dedicata **149** (2010), 155–160, DOI 10.1007/s10711-010-9473-z | `philippe2010gd.bib` | `philippe2010gd_zbmath.bib` (Zbl 1248.20053) |
| E. Philippe, *Le spectre des longueurs des surfaces hyperboliques : un exemple de rigidité*, Sémin. Théor. Spectr. Géom. **28** (2009–2010), 109–120, DOI 10.5802/tsg.280 | `philippe2010tsg.bib` | — |

Two related papers:

- *Détermination géométrique de la systole des groupes de triangles*, C. R. Math. **349** (2011) 1183–1186, DOI 10.1016/j.crma.2011.10.015 (`philippe2011cras.bib`).
- arXiv:0901.4630, *Sur le spectre des longueurs des groupes de triangles (r,p,q)*.

**Verbatim key statements.**

- **AIF 2008**, arXiv v1, pdf p. 4: "Théorème A : Soit Γ(2, p, q) et Γ(2, p′, q′) deux groupes de triangles isospectraux au sens des longueurs. Alors ces deux groupes sont isométriques."
- **AIF 2008**, pdf p. 24, proof of Prop. 9 for p ≥ 11: "Notons l1, l2 les deux premières valeurs distinctes du spectre … Il suffit d'établir que le système 2XY = L1, Y(4X² − 1) = L2 admet un unique couple de solution (X, Y) dans [0, 1]²". Here X = cos(π/p) and Y = cos(π/q). That is, two lengths determine the group.
- **TSG 2010**, printed p. 117, pdf p. 10, §3:
  - "Théorème 3.1. — Si deux groupes Γ(r, p, q) et Γ(r′, p′, q′) ont le même spectre des longueurs, alors r = r′, p = p′ et q = q′."
  - Proof, Step 1: "Les groupes suivants possèdent des systoles de longueur identique : – Γ(2, 3, 10) et Γ(2, 5, 5) – Γ(2, 3, 12) et Γ(2, 4, 12)".
  - Step 2: "des groupes distincts vérifiant r ⩾ 4 et r′ ⩾ 4 ne peuvent pas avoir les trois premières longueurs (avec multiplicités) identiques".
  - p. 118: "Là encore les deux premières longueurs (avec multiplicités) ne coïncident jamais, ce qui conclut la preuve du théorème."
  - Theorem 3.1 is attributed in the text to "[27]", which is the Geom. Dedicata paper.
- **TSG 2010**, printed p. 111: earlier small-moduli rigidity results (Buser–Semmler for one-holed tori; Dianu for tori with one cone point; Buser–Semmler for spheres with cone points (2,2,3,3); Haas for pants) "reposent tous sur une détermination géométrique des courbes fermées les plus courtes et la plupart du temps les deux premières longueurs suffisent à déterminer la surface."

**Relation to the results.**

- **(3).**
  - It is the length-side counterpart of the triangle threshold. Finitely many lengths (two or three, with multiplicities) determine Γ(r,p,q). The heat side needs three invariants in general and two when p+q+r ≤ 17.
  - Philippe's "systolic twins" are the length-side analogue of the minimal pair (2,8,8)/(3,3,12). The pairs are different, as expected, since heat invariants see the signature while short lengths see the geometry.
  - For Laplace-isospectral triangle orbifolds the conclusion is already implied by Dryden–Strohmaier (cone orders) plus rigidity. Philippe's contribution is the finite-data length version.
- **(2).** It complements locality. The shape, here the identity of the triangle, is fully in the length spectrum, which enters the heat trace only at order e^{-ℓ²/4t}.
- **(1) and (4):** none.

**Where to cite.**

- §1.1 "Prior work" (around lines 172–178), in a sentence such as: "On the length side, Philippe showed that hyperbolic triangle groups are determined by their length spectrum, in fact by its first two or three values with multiplicities [Philippe 2008, Thm A; 2010]."
- Optionally §5 (rigid case), as a remark contrasting systolic twins with the heat-invariant minimal pair.

**Novelty impact.** It does not change the heat-invariant novelty claim. It does narrow any phrasing that suggests that finite-data determinacy of triangle orbifolds is new in general. The manuscript's sentence at line 176 says "finite-coefficient determinacy threshold", i.e. heat coefficients, so it remains accurate. Adding Philippe forestalls a referee objection.

### 2.3 Chang–DeTurck 1989: finitely many eigenvalues determine a Euclidean triangle **[should cite; (b), analogue of (1)(ii)]**

- **Reference.**
  - P.-K. Chang, D. DeTurck, *On hearing the shape of a triangle*, Proc. Amer. Math. Soc. **105** (1989), no. 4, 1033–1038.
  - Crossref BibTeX: `_fetched/bib/changdeturck1989.bib`. **Crossref gives pages "1033–1033", which is wrong.**
  - zbMATH BibTeX: `changdeturck1989_zbmath.bib`, Zbl 0721.58053, pages 1033–1038, with JSTOR DOI 10.2307/2047071.
- **Key statement.** **CANNOT VERIFY from the primary source**: AMS returned HTTP 429 twice and Unpaywall reports it as not OA. Two secondary sources agree:
  - zbMATH review: "The authors prove that if for two (Euclidean) triangles the first N eigenvalues (of the Dirichlet problem) coincide then both are isospectral. Here N depends only on the first two eigenvalues."
  - Mårdby–Rowlett survey, arXiv:2406.18369v2, pdf p. 35: "Chang and DeTurck proved that to determine whether two triangles in the Euclidean plane are congruent it is enough to know that they have their first N eigenvalues in common, where N depends on the first two eigenvalues of the triangles [27]."
- **Relation to the results.** It is a finite-data determinacy result whose count is **not uniform** and depends on low-order data. This is the same shape as (1): a count ⌊Area/π⌋+4 read off from c₁, and no uniform count. The data there are eigenvalues and the setting is Euclidean.
- **Where to cite.** Line 178, next to "Finite amounts of spectral data are also known to determine Euclidean triangles \cite{griesermaronna2013}", and possibly in the discussion after Theorem 1.1(ii).
- **Novelty impact.** None for hyperbolic orbifolds or heat invariants.

### 2.4 History of the constant cone term (m²−1)/(12m) **[optional; (c)]**

| Source | Location | Verbatim | Status |
|---|---|---|---|
| Cheeger, *Spectral geometry of singular Riemannian spaces*, J. Differential Geom. **18** (1983) 575–657, DOI 10.4310/jdg/1214438175 (`cheeger1983.bib`; Crossref gives no page range) | (4.42) | Not read: Project Euclid returned an HTML challenge | CANNOT VERIFY (gap). Attested by AKR, below |
| Brüning–Seeley, *The resolvent expansion for second order regular singular operators*, J. Funct. Anal. **73** (1987) 369–429, DOI 10.1016/0022-1236(87)90073-5 (`bruningseeley1987.bib`) | p. 424 | Not read | Attested by Schueth 2025, p. 1 (quoted in §1) |
| Kokotov, *Polyhedral surfaces and determinant of Laplacian*, Proc. Amer. Math. Soc. **141** (2013), no. 2, 725–735, DOI 10.1090/s0002-9939-2012-11531-x (`kokotov2013.bib`; Crossref year is 2012, the online date) | Theorem 1, eq. (13); arXiv:0906.0717v1, pdf p. 9 | "Tr e^{t∆} = … = Area(X)/(4πt) + (1/12) Σ_{k=1}^N (2π/βk − βk/2π) + O(e^{−ǫ/t})" for flat polyhedral surfaces | VERIFIED in the arXiv text. Caveat: the arXiv title differs and has no journal-ref, so the identity of the arXiv text with the PAMS paper is not confirmed |
| Aldana–Kirsten–Rowlett, *Polyakov formulas for conical singularities in two dimensions*, Ann. Math. Québec **50** (2025) 35–72, DOI 10.1007/s40316-025-00263-w (`akr2025.bib`); arXiv:2010.02776 | pdf pp. 17, 31 (arXiv v3) | "(2π)² − γ² / 24πγ" and "Note that our calculation agrees with Cheeger's expression [20, 4.42], and we have computed by a completely independent method." | VERIFIED |

With γ = 2π/m, all of these reduce to the manuscript's cone(m) = (m²−1)/(12m). DGGW (5.7) is the orbifold source and is already cited. This pass recommends at most an optional parenthetical, "(for general cone angles this is due to Cheeger [(4.42)])".

### 2.5 Donnelly 1979, via Dowker 2023: exact elliptic heat-trace contribution **[optional; (c)]**

- **References.**
  - H. Donnelly, *Asymptotic expansions for the compact quotients of properly discontinuous group actions*, Illinois J. Math. **23** (1979), no. 3, 485–496, DOI 10.1215/ijm/1256048110.
    - Crossref BibTeX: `donnelly1979.bib`, which lacks pages.
    - zbMATH BibTeX: `donnelly1979_zbmath.bib`, Zbl 0411.53033, pp. 485–496.
    - Not read (gap 5 in the log).
  - J. S. Dowker, *Casimir energy of elliptic fixed points*, arXiv:2311.12708v2 (2023). No journal version was found in Crossref. The arXiv record is `dowker2023_arxiv.xml`.
- **Key statement.** Quoted in §1 (pdf p. 2, eq. (1); pdf p. 7).
- **My check.** I evaluated eq. (1) numerically at p = 2, 3, 5 and t = 10⁻², 10⁻³. The ratio (K_p − (p²−1)/12p)/t converges to −(p⁴+10p²−11)/(360p), the manuscript's b₁ at K = −1. For example, at p = 5, t = 10⁻³ it gives −0.47857, against the target −0.48.
- **Relation to the results.** It gives an exact integral representation of the per-cone-point contribution at K = −1, from which every heat invariant follows. This is an independent route to the input of (1), and it is the same object as the E term of the manuscript's Theorem IEH (line 791).
- **Where to cite.** Optional, at line 791 or line 220.
- **Novelty impact.** None.

### 2.6 Other (b)/(c) items checked: peripheral, no citation needed

- **Watson 2005**, *The trace function expansion for spherical polygons*, N. Z. J. Math. **34** (2005) 81–95 (`watson2005.bib` from zbMATH, Zbl 1076.35042). zbMATH summary: "The full asymptotic expansion of the trace of the heat semigroup … for geodesic spherical polygons Ω⊂S² is derived in half-powers of t, and the coefficients determined explicitly."
  - Together with Schueth 2019 Remark 5.4(ii) (already in Q2), it supplies the K = +1 all-order formulas.
  - The manuscript's "Other curvatures" paragraph (line 346) cites Uçar for K = +1. Watson could be added there; this is optional.
- **Mårdby–Rowlett** survey, arXiv:2406.18369, published as *A century of spectral geometry from Weyl to Milnor, Kac and beyond*, Rev. Math. Phys. (2026), DOI 10.1142/s0129055x26300013 (`mardbyrowlett2025.bib`).
  - Searched for orbifold, cone point, triangle and finitely. Its only orbifold mentions are Conway notation, lens spaces and Bari–Hunsicker; it has nothing on hyperbolic orbifold heat invariants.
  - Its history section (pdf pp. 35–36) is a convenient source for Chang–DeTurck. This is negative evidence that the area was open as of 2024–2026.
- **Mårdby–Rowlett, *Spectral invariants of integrable polygons*** (arXiv:2409.14391): Euclidean polygons with angles π/n. Not relevant.
- **Nursultanov–Rowlett–Sher**, *The heat kernel on curvilinear polygonal domains in surfaces*, Ann. Math. Québec 2024, arXiv:1905.00259: corners are spectral invariants for curvilinear polygons. They cite Uçar only for hyperbolic polygons. Not relevant to cone orders. The same holds for Lu–Rowlett (BLMS 48 (2016) 85–93, DOI 10.1112/blms/bdv094).
- **Suleymanova** arXiv:1711.00577 (curved cones, b₀ and b_{1/2}): superseded by Schueth 2025.
- **Dryden et al.**, Steklov polygons I/II (arXiv:2408.01529, 2604.18977): Steklov spectral finiteness and determination of triangles. Different spectrum; not relevant.
- **Dryden's 2006 talk slides** (bucknell.edu/~ed012/geometria.pdf, p. 22): "We must add metric assumptions to distinguish among these pillows". This is the same remark as DGGW Remark 5.16, already cited at line 176. No action needed.
- **Fedosova–Rowlett–Zhang**, *Casimir energy of hyperbolic orbifolds with conical singularities*, J. Math. Phys. **65** (2024), DOI 10.1063/5.0186488 (`fedosovarowlettzhang2023.bib`): ζ(−1/2) for orbifolds including (2,3,7), with an elliptic orbital integral. Not about determinacy. Not needed.
- **Cognola–Vanzo**, J. Math. Phys. **35** (1994) 3109–3116 (`cognolavanzo1994.bib`): for hyperbolic 3-orbifolds, elliptic elements change every heat coefficient except the Weyl term. It is the 3-dimensional analogue of (2)'s "I+E" structure. Not needed.

### 2.7 Stability and conditioning (d): extends Q4 **[should cite in §Stability]**

Q4 (review/hyperresearch/Q4-stability.md) already quotes Batenkov–Yomdin 2013 (Lemma 4.2, Cor. 4.3: critical points of the Prony map occur exactly at node collisions) and Moitra. This pass adds the colliding-node accuracy results.

- **Akinshin–Batenkov–Yomdin.**
  - Reference: *Accuracy of spike-train Fourier reconstruction for colliding nodes*, Proc. SampTA 2015, 617–621, DOI 10.1109/sampta.2015.7148965 (`aby2015.bib`); arXiv:1502.06932.
  - Abstract, verbatim: "we give an absolute lower bound (which is valid with any reconstruction method) for the "worst case" error of reconstruction … in situations where the nodes xj are known to form an l elements cluster of a size h ≪ 1 … Roughly, our main result states that for h of order (1/N) ε^{1/(2l−1)} the worst case reconstruction error of the cluster nodes is of the same order (1/N) ε^{1/(2l−1)}".
- **Batenkov–Goldman–Yomdin.**
  - Reference: *Super-resolution of near-colliding point sources*, Inf. Inference **10** (2021/online 2020), no. 2, 515–572, DOI 10.1093/imaiai/iaaa005 (`bgy2020.bib`), with an erratum, DOI 10.1093/imaiai/iaaa015; arXiv:1904.09186.
  - Abstract, verbatim: "Provided that ε ≲ SRF^{−2p+1} … we show that the minimax error rate for reconstruction of the cluster nodes is of order (1/Ω) SRF^{2p−1} ε".
- **Batenkov–Demanet–Goldman–Yomdin**, *Conditioning of partial nonuniform Fourier matrices with clustered nodes*, SIAM J. Matrix Anal. Appl. **41** (2020) 199–220, DOI 10.1137/18m1212197 (`bdgy2020.bib`): Vandermonde conditioning with clustered nodes.

**Relation to (4).**

- These give the clustered-node loss of accuracy for **moment problems with unknown weights**, Σ a_j x_j^k. For an exact ℓ-fold collision the exponent is 1/(2ℓ−1), because the weights and nodes trade off.
- In the manuscript's setting the weights are known and all equal to 1. The data are power sums of the orders, R = P_{−1}, P₁, P₃, …. The inversion therefore passes through the roots of a polynomial, which gives Hölder exponent 1/k at a k-fold order. This is Lemma (Clusters) and Prop. sharpexp (lines 1136–1176).
- This is a genuine and worth-stating difference: equal-weight moment data are better conditioned at collisions than general Prony data.

**Where to cite.** In §Stability, beside the Ostrowski paragraph (line 1136), for example: "In Prony and super-resolution problems with unknown amplitudes, an ℓ-node cluster gives the exponent 1/(2ℓ−1) [ABY15; BGY20]. With unit weights the problem reduces to polynomial roots, and the exponent is 1/k."

**Novelty impact.** It confirms that (4) is new for cone orders. The general phenomenon, loss of Lipschitz stability at node collisions, is standard, as the stability note already says.

### 2.8 (e) Other triangle-group and orbisurface spectral items: no citation needed

- **Kravchuk–Mazáč–Pal**, arXiv:2111.12716, and **Gesteau–Pal–Simmons-Duffin et al.**, arXiv:2311.13330: numerical Laplace spectra and bootstrap bounds for triangle orbifolds such as [0;3,3,5] and (2,3,7).
  - Optional context for §Experiments, where computed spectra of (2,8,8) and (3,3,12) are used. Strohmaier–Uski is already cited.
- **Adve**, arXiv:2509.17935, p. 8: "By Riemann–Roch …, the topological type of Γ\H determines the holomorphic spectrum and vice versa."
  - This is a different (holomorphic, modular-forms) spectrum that determines the signature. It is a curiosity, not needed.
- **Linowitz–Voight** follow-ups (16 in OpenAlex) are all arithmetic. **Doyle–Rossetti** follow-ups (6 in OpenAlex, 10 in Semantic Scholar) are lens spaces, Steklov or G-sets. Nothing on heat invariants or signatures.
- **Maclachlan–Rosenberger 1994**, *Small volume isospectral, non-isometric, hyperbolic 2-orbifolds* (Zbl 0781.57004): not fetched. Isospectral same-signature pairs are already represented by Linowitz–Voight (line 178).
- **Takeuchi:** already settled in review/takeuchi-verdict.md. Nothing new.

---

## 3. Bib-record checks for the new keys

All records are raw outputs in `_fetched/bib/`.

| key | Source of raw record | Issue |
|---|---|---|
| schueth2025 | Crossref content negotiation, DOI 10.1007/s10455-025-10024-1 | No pages. Crossref API gives `article-number` 2, vol. 69, issue 1, published 2025-12-08 |
| philippe2008 | Crossref and zbMATH | The Crossref title contains raw MathML. Use zbMATH's metadata with the French title from the paper: "Les groupes de triangles (2,p,q) sont déterminés par leur spectre des longueurs" |
| philippe2010gd | Crossref and zbMATH | Consistent: vol. 149, pp. 155–160 |
| philippe2010tsg | Crossref | Vol. 28, pp. 109–120, year 2010 (the volume is labelled 2009–2010) |
| changdeturck1989 | Crossref and zbMATH | **Crossref pages "1033–1033" are wrong**; zbMATH gives 1033–1038. zbMATH also lists JSTOR DOI 10.2307/2047071 besides the AMS DOI |
| kokotov2013 | Crossref | Crossref `year=2012` is the online date; the volume (141, 2013) is correct |
| cheeger1983 | Crossref | No pages in Crossref. Pages 575–657 come from Schueth 2025's reference list, which is not a raw record. Fetch the zbMATH record if this key is used |
| bruningseeley1987, akr2025, batenkovyomdin2013, aby2015, bgy2020, bdgy2020, moitra2015, donnelly1979 (+ zbMATH), watson2005 (zbMATH), mardbyrowlett2025, fedosovarowlettzhang2023, cognolavanzo1994 | Crossref, or zbMATH as noted | donnelly1979 Crossref has no pages; zbMATH has 485–496 |

No existing references.bib keys were re-audited in this pass; that is the citation-check agents' task.

---

## 4. Instrument gaps

Details are in the log, §"Instrument gaps".

1. Crossref cited-by (HTTP 404 and 401).
2. The zbMATH citation index is incomplete (2 hits for DGGW, 0 for Dryden–Strohmaier).
3. Semantic Scholar keyword search was rate-limited (429 on 3 of 5 queries, and on the MCP tool). The citation endpoints were fine.
4. Cheeger 1983 PDF (Project Euclid HTML challenge).
5. Donnelly 1979 PDF (Project Euclid HTML challenge).
6. Chang–DeTurck PDF (AMS HTTP 429; not OA).
7. Philippe, Geom. Dedicata 2010 (not OA; no zbMATH review). Its theorem was read only through the author's TSG survey.
8. Watson 2005 full text was not located.
9. Brüning–Seeley 1987 was not fetched.
10. Maclachlan–Rosenberger 1994 was not fetched.
11. The arXiv identity of Kokotov's PAMS paper is unconfirmed.
12. The arXiv full-text index covers full text only partly, so its zero-hit results bound, but do not prove, absence.

---

## 5. Recommended manuscript actions, by priority

1. **Add Philippe** (AIF 2008, Thm A; Geom. Dedicata 2010, cited via TSG 2010, Thm 3.1) to §1.1 "Prior work" as the length-spectrum, finite-data rigidity of triangle groups. Optionally contrast the systolic twins with (2,8,8)/(3,3,12) in §5.
2. **Add Schueth 2025** alongside Uçar at line 220, as refereed confirmation of the all-order closed form.
3. **Add Akinshin–Batenkov–Yomdin 2015 and/or Batenkov–Goldman–Yomdin 2020**, with Batenkov–Yomdin 2013 per Q4, at the Ostrowski paragraph in §Stability (line 1136). State the contrast of exponent 1/(2ℓ−1) with unknown weights against 1/k with unit weights.
4. **Add Chang–DeTurck 1989** at line 178 as the Euclidean-triangle analogue of a finite but non-uniform count. Use pages 1033–1038, not Crossref's.
5. **Optional:**
   - Cheeger (4.42) or Kokotov (13) for the general-angle constant term;
   - Donnelly 1979 for the exact elliptic integral;
   - Watson 2005 at line 346 for K = +1.
