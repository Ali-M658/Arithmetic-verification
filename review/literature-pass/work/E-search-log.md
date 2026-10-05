# E: search log for the forward-citation and missing-literature sweep

Session date: 2026-10-05. All retrieval was headless: curl, the arXiv API, the arXiv full-text search, OpenAlex, the Semantic Scholar Graph API, Crossref, zbMATH Open, Unpaywall and WebSearch for discovery.

Raw outputs are under `review/literature-pass/_fetched/txt/E_search/`, which is git-ignored:

| File | Contents |
|---|---|
| `oa_cites_<OpenAlexID>.json` | OpenAlex `filter=cites:` results |
| `ss_*.json` | Semantic Scholar `/citations` results |
| `zb_*.json` and `zbmath_E.txt` | zbMATH Open |
| `arxiv_ft_E.txt` | arXiv full-text search, with up to 20 hits and snippets per query |
| `arxiv_api_E.txt` | arXiv API |
| `openalex_search_E.txt` | OpenAlex keyword search |
| `ss_search_E.txt` | Semantic Scholar keyword search |

Fetched full texts are in `_fetched/pdf/E_*.pdf` and `_fetched/txt/E_*.txt`. BibTeX records are in `_fetched/bib/`.

This sweep avoids the 27 arXiv full-text queries already logged in `review/audit/literature/search/arxiv_ft.txt`, and the Q4/stability queries in `review/literature/stability-inverse-spectral.md` §3. No query below repeats one of those strings.

**How the instruments behave**

- **arXiv full-text search** (`search_classic`, `searchtype=ft`). The snippets show the index covers abstracts and comments, and apparently some full text. Its exact coverage is undocumented, so treat it as an abstract-plus-partial-full-text index.
  - A page that reads "No Results." is recorded as **0 hits**. One such page was checked by hand, for `"finitely many heat invariants"`.
- **arXiv API.** Phrase queries were sent as `abs:"w1+w2"`. The totals were small (for example, `abs:"heat+trace" AND abs:orbifold` returned 4), so the phrase handling may be strict. The API counts are lower bounds.
- **zbMATH Open API.** A query with no results returns HTTP 404. These are recorded as **0 (404)**.
- **Semantic Scholar.** The keyword search endpoint was rate-limited (HTTP 429) on most calls, including through the MCP tool. The `/citations` endpoint answered after backoff.

---

## (a) Forward citations

### A.1 Resolving the seed IDs

| Seed | OpenAlex ID | OpenAlex cited_by_count | Crossref is-referenced-by-count |
|---|---|---|---|
| DGGW 2008, MMJ, DOI 10.1307/mmj/1213972406 | W2168233867 | 58 | 29 |
| DGGW arXiv:0805.3148, separate record | W2951524667 | 0 | — |
| Dryden–Strohmaier 2009, CMB, DOI 10.4153/cmb-2009-008-0 | W2012667223 | 5 | 6 |
| Dryden–Strohmaier arXiv math/0504571, record "Huber's theorem…" 2005 | W3104076166 | 17 | — |
| Uçar 2017, edoc DOI 10.18452/18463 | W2766274720 | 4 | — |
| Uçar 2017, arXiv DOI 10.48550/arxiv.1711.03405 | W4394659730 | 0 | — |

Resolution of the Dryden–Strohmaier arXiv record by DOI (`doi:10.48550/arxiv.math/0504571`) returned an empty, non-JSON body. The record was found instead through the Dryden–Strohmaier listing in the OpenAlex cites of DGGW.

### A.2 Queries and results

| # | Instrument and query | Hits | Notes |
|---|---|---|---|
| a1 | OpenAlex `filter=cites:W2168233867&per-page=200` (DGGW) | 57 | All triaged; see A.3 |
| a2 | OpenAlex `cites:W2951524667` (DGGW arXiv) | 0 | |
| a3 | OpenAlex `cites:W2012667223` (DS, CMB) | 5 | Linowitz–Voight; Gittins et al. I; *On the isospectral orbifold–manifold problem for nonpositively curved locally symmetric spaces* (Geom. Dedicata 2016); Philippe TSG 2010; *Approximating orbifold spectra using collapsing connected sums* |
| a4 | OpenAlex `cites:W3104076166` (DS, arXiv) | 17 | Adds Philippe AIF 2008 and Philippe Geom. Dedicata 2010 |
| a5 | OpenAlex `cites:W2766274720` (Uçar, edoc) | 4 | Nursultanov–Rowlett–Sher 2024; Schueth AIF 2019; Mehler–Fock 2018; Schueth AGAG 2025 |
| a6 | OpenAlex `cites:W4394659730` (Uçar, arXiv) | 0 | |
| a7 | Semantic Scholar `/paper/DOI:10.1307/mmj/1213972406/citations?limit=1000` | 65 | HTTP 200 on the first try (second session). Adds Schueth arXiv:2511.22255, Lassas–Lu–Yamaguchi 2404.16448, flat-moduli 2507.16017, Gittins et al. II |
| a8 | Semantic Scholar `/paper/arXiv:0805.3148/citations` | 65 | Same set as a7 |
| a9 | Semantic Scholar `/paper/arXiv:1711.03405/citations` | 5 | Same as a5, plus the arXiv version of Schueth 2025 |
| a10 | Semantic Scholar `/paper/DOI:10.4153/cmb-2009-008-0/citations` | 19 | Adds Philippe (AIF 2008, Geom. Dedicata 2010, TSG 2010) |
| a11 | Crossref `/works/<doi>/cited-by` (DGGW, DS) | HTTP 404 | Instrument gap: needs membership |
| a12 | Crossref `doi.crossref.org/servlet/getForwardLinks` | HTTP 401 | Instrument gap: needs credentials |
| a13 | zbMATH `ci:1175.58010` and `ci:5496998` (DGGW) | 2 | Erratum 2017; Gittins et al. I. The citation index is clearly incomplete |
| a14 | zbMATH `ci:1179.58014` (DS) | 0 (404) | Gap: incomplete citation index |
| a15 | zbMATH `rf:1175.58010` | error (null result) | Field not supported |
| a16 | zbMATH `ti:spectral invariants polygons orbisurfaces` | 1 | Uçar's arXiv record only; no citation data |

Second-level seeds were added because they are the closest relatives of results (1)–(4):

| # | Instrument and query | Hits | Notes |
|---|---|---|---|
| a17 | Semantic Scholar citations of Doyle–Rossetti arXiv:1103.4372 | 10 | Lauret–Linowitz survey 2305.10950; Linowitz–Voight; others are lens spaces, Steklov or G-sets. Nothing on heat invariants |
| a18 | Semantic Scholar citations of Linowitz–Voight DOI 10.1007/s00209-015-1500-1 | 0 | |
| a19 | OpenAlex `cites:W1513953988` (Linowitz–Voight) | 16 | All arithmetic (quaternion orders, 3-manifolds); none relevant |
| a20 | OpenAlex `cites:W1626429050` (Doyle–Rossetti) | 6 | None relevant |
| a21 | Semantic Scholar citations of Schueth arXiv:1812.06119 | 2 | Schueth 2025 (arXiv and AGAG) |
| a22 | OpenAlex `cites:W2904014476` (Schueth AIF 2019) | 1 | Schueth 2025 |
| a23 | Semantic Scholar citations of Schueth arXiv:2511.22255 | 0 | |
| a24 | OpenAlex `cites:W2943542068` (Nursultanov–Rowlett–Sher) | 8 | Includes the Mårdby–Rowlett survey (Rev. Math. Phys. 2026) and the Steklov polygons II paper; none on orbifolds |
| a25 | Semantic Scholar citations of Grieser–Maronna arXiv:1208.3163 | 33 | Triangles and polygons, all Euclidean. Relevant: Chang–DeTurck (via survey), Gómez-Serrano–Orriols, Mårdby–Rowlett survey, Steklov polygons I/II, "(Not) hearing where triangular drums are struck" (2607.10556), Meyerson–McDonald |
| a26 | Semantic Scholar citations of Philippe arXiv:0807.4746 | 7 | Philippe CRAS 2011 (systole), Geom. Dedicata 2010, arXiv:0901.4630, TSG 2010; Fedosova–Rowlett–Zhang 2023; Suzzi Valli 2015; Huber-constant bound 2024 |
| a27 | Semantic Scholar citations of Philippe Geom. Dedicata 2010 | 4 | As a26 |

### A.3 Merged and deduplicated forward set, with triage

- **Size of the merged set.** Seeds DGGW, Dryden–Strohmaier (DS) and Uçar gave 68 distinct titles across OpenAlex and Semantic Scholar, about 60 works once arXiv and journal versions of the same paper are merged.
- **How each was triaged:**
  - every title was read;
  - an abstract was pulled for each doubtful case (arXiv API `id_list` calls are recorded in the session);
  - full text was fetched for every candidate about heat invariants of cone or orbifold singularities, hearing cone points, finite determinacy, or triangle groups.

| Year | Work | Cites | Triage | Action |
|---|---|---|---|---|
| 2025 | Schueth, *Heat coefficients of surfaces with curved conical singularities*, AGAG 69 (2025) no. 1, art. 2; arXiv:2511.22255 | DGGW, Uçar | **Relevant (c)** | Full text read; report §2.1 |
| 2025 | *Moduli spaces of flat Riemannian metrics on orbifolds*, arXiv:2507.16017 | DGGW | Not relevant (flat) | Title only |
| 2024 | Lassas–Lu–Yamaguchi, arXiv:2404.16448 | DGGW | Relevant (d); already covered in stability-inverse-spectral.md | Not refetched |
| 2024 | Nursultanov–Rowlett–Sher, *Heat kernel on curvilinear polygonal domains*, arXiv:1905.00259 | Uçar | Peripheral (b/c): Euclidean-type corners; cites Uçar for hyperbolic polygons | Full text grep, report §2.6 |
| 2023 | Colbois et al., *Steklov survey*, arXiv:2212.12528 | DGGW | Not relevant (Steklov) | Abstract |
| 2023 | Gittins et al. I and II | DGGW, DS | Already in prior notes; II is flat 2-orbifolds | Grepped II for cone points: flat only |
| 2022 | Sandoval, wave invariants basic spectrum, arXiv:2205.05603 | DGGW, DS | Not relevant | Abstract |
| 2021 | *Approximating orbifold spectra…*, arXiv:1611.07676 | DGGW, DS | Not relevant | Abstract |
| 2020 | Schueth AIF 2019 | DGGW, Uçar | Already cited (`schueth2019`) | — |
| 2019 | Richardson–Stanhope | DGGW | Already in prior notes | — |
| 2019 | Arias-Marco et al., Steklov on orbifolds, arXiv:1609.05142 | DGGW | Not relevant (Steklov detects boundary cone points) | Abstract |
| 2019 | Bari–Hunsicker | DGGW | Already cited | — |
| 2017 | Uçar thesis | DGGW, DS | Seed | — |
| 2016 | *Spectra of orbifolds with cyclic fundamental groups*, arXiv:1510.05948 | DGGW | Not relevant (spherical quotients) | Abstract |
| 2015 | Linowitz–Voight | DGGW, DS | Already cited | — |
| 2015 | Twisted Selberg trace formula for orbifolds (1511.04208); analytic torsion of hyperbolic orbifolds (1511.04281) | DGGW | Not relevant to determinacy | Titles |
| 2012 | Dryden–Guillemin–Sena-Dias, equivariant inverse spectral theory, toric orbifolds | DGGW | Peripheral (equivariant spectrum, toric) | Abstract |
| 2012 | Farsi–Proctor–Seaton, Γ-extensions | DGGW, DS | Not relevant | Abstract |
| 2011 | Doyle–Rossetti | DGGW, DS | Already cited | — |
| 2011 | Proctor (homeomorphism finiteness) | DGGW | Already in prior notes | — |
| 2010 | Philippe, *Sur la rigidité des groupes de triangles (r,p,q)*, Geom. Dedicata 149 (2010) 155–160 | DS | **Relevant (e)** | Full text paywalled (gap); content read through TSG 2010 survey, report §2.2 |
| 2010 | Philippe, *Le spectre des longueurs des surfaces hyperboliques : un exemple de rigidité*, Sémin. Théor. Spectr. Géom. 28 (2010) 109–120 | DS | **Relevant (e)** | Full text read |
| 2010 | Isospectral metrics on weighted projective spaces, arXiv:1004.1360 | DGGW, DS | Not relevant | Abstract |
| 2009 | Proctor–Stanhope | DGGW | Already in prior notes | — |
| 2008 | Philippe, *Les groupes de triangles (2,p,q) sont déterminés par leur spectre des longueurs*, AIF 58 (2008) 2659–2693; arXiv:0807.4746 | DS | **Relevant (e)** | Full text read |
| 2008 | Rossetti–Schueth–Weilandt | DGGW, DS | Already cited | — |
| 2007 | ADFG, weighted projective planes | DGGW | Already cited | — |
| 2006 | *Isospectral hyperbolic surfaces have matching geodesics*, math/0605765 | DGGW, DS | Not relevant to cone orders | Title |
| other | Quantum ergodicity on orbifolds; CR/S¹ index; Kendall shape space; Deligne–Mumford instantons; Weil–Petersson Laplacian; Ricci flow on orbifolds; foliation traces; metric-measure locality; Sobolev isospectral potentials; Mabuchi geometry; quantum graphs; equivariant Sunada; asymptotically hyperbolic | DGGW | Not relevant (title-level triage) | — |

**Result of (a).** Among the forward citations of the three seeds:

- **No work** gives a finite count of heat coefficients for hyperbolic orbifolds, a determinacy threshold for triangle orbifolds, or a stability estimate for cone orders.
- **Two items are new and must be considered:**
  - Schueth 2025, for (c).
  - Philippe 2008/2010, which give length-spectrum rigidity of triangle groups, for (e).

---

## (b)–(e) and the scoop search

### arXiv full-text search (`arxiv_ft_E.txt`)

Hits are total hits. "Relevant" lists what was opened or retained.

| # | Query | Hits | Relevant hits |
|---|---|---|---|
| f1 | `"triangle orbifold" heat invariants` | 1 | 2509.17935 (Adve, conformal bootstrap; mentions the (2,3,13) triangle orbifold). Not relevant to heat invariants |
| f2 | `"cone orders" heat trace` | 1 | 2407.00359 (optimization book). None |
| f3 | `"(2,8,8)"` | 18 | None (supergravity, lattices, ML, Deraux complex hyperbolic). **No scoop** |
| f4 | `"2,8,8" orbifold` | 2 | Deraux 2207.07373 (complex hyperbolic triangle groups); Wang 2106.00470. None |
| f5 | `"hear the signature"` | 1 | 2604.09250 (astronomy). None |
| f6 | `"Egyptian fraction" heat` | 0 | — |
| f7 | `"Egyptian fractions" orbifold spectrum` | 1 | 1507.05139 (modular categories). None |
| f8 | `"heat invariants" "triangle groups"` | 0 | — |
| f9 | `"heat coefficients" "cone points" hyperbolic` | 4 | 1812.06119 (Schueth 2019), 1711.03405 (Uçar). Both known |
| f10 | `"conical singularity" "heat trace" "1/12"` | 18 | Kalvin 2011.05407, 2112.02771, 1910.00104; Aldana–Kirsten–Rowlett 2010.02776; Hillairet–Kalvin–Kokotov 1410.3106; Aldana–Rowlett 1411.7894; Liou 2609.19604. AKR fetched (§2.4) |
| f11 | `"orbisurface" "heat invariants"` | 3 | Uçar; Farsi–Proctor–Seaton; Steklov survey |
| f12 | `"triangle orbifolds" spectrum` | 4 | Adve 2509.17935; Soares 1709.00295; Belolipetsky 1610.06147. None on heat invariants |
| f13 | `"cone-order" spectrum orbifold` | 2 | Kalvin 2608.01611 (determinants of the Bolza surface and Klein quartic via orbifold quotients); Teng 2605.25858. Not determinacy |
| f14 | `"finitely many heat invariants"` | 0 | — |
| f15 | `"first two heat invariants"` | 3 | Aldana–Perez 2202.06110; Gittins et al. 2106.07882; Bettiol–Lauret–Piccione 2001.08471. Not about cone orders |
| f16 | `"first n heat invariants"` | 0 | — |
| f17 | `"heat invariants" "cone points" orbifold determine` | 2 | Uçar; Steklov survey |
| f18 | `"orbifold" "heat trace" "cone points" "spectral invariant"` | 5 | Gittins et al. II; Schueth 2019; Uçar; Steklov survey; Rayan 2608.01596 (band theory) |
| f19 | `"conical singularities" "heat coefficients" constant curvature` | 12 | **Schueth 2511.22255**; Sher 1208.1808; the rest physics |
| f20 | `"curved conic singularities"` | 3 | Schueth 2511.22255; Suleymanova 1711.00577; AKR 2010.02776 |
| f21 | `"heat kernel" "hyperbolic cone" "all orders"` | 0 | — |
| f22 | `"cone angle" "heat trace" coefficients "all orders"` | 0 | — |
| f23 | `"hearing the shape" triangle heat invariants` | 29 | Grieser–Maronna; Dryden et al. Steklov II 2604.18977; Mårdby–Rowlett 2409.14391 and 2406.18369; Gómez-Serrano–Orriols; Meyerson–McDonald; Hezari–Lu–Rowlett. All Euclidean |
| f24 | `"spectral determination" triangles "heat invariants"` | 2 | Mårdby–Rowlett 2406.18369; Hezari–Lu–Rowlett 1601.00774 |
| f25 | `"isospectral" "triangle groups"` | 13 | Linowitz–Voight; Doyle–Rossetti; Kalvin 2310.04882. No triangle-orbifold isospectrality |
| f26 | `"length spectrum" "triangle groups"` | 51 | Fedosova–Rowlett–Zhang 2311.03331; Suzzi Valli 2008.05422; Perazzelli 2509.16470; Schein–Shoan 2012.08796. None on spectral determination |
| f27 | `"spectrum" "Fuchsian triangle group" eigenvalues` | 5 | Gesteau–Pal–Simmons-Duffin et al. 2311.13330 (numerical spectra of [0;3,3,5]) |
| f28 | `"hyperbolic orbisurfaces" isospectral signature` | 1 | Linowitz–Voight |
| f29 | `"Huber" orbisurfaces cone points spectrum` | 2 | Linowitz–Voight; Doyle–Rossetti |
| f30 | `"power sums" stability recovery multiset Holder` | 0 | — |
| f31 | `"from power sums" stability perturbation` | 1 | 2301.11456 (graph scattering). None |
| f32 | `"heat invariants" "Holder" orbifold` | 0 | — |
| f33 | `"stability" "cone points" spectral` | 97 | First 20 read: physics and dynamics; Petri 2607.06331 (bass notes). None on recovering cone orders |
| f34 | `"quantitative" "spectral determination" orbifold` | 2 | Xie 2511.12111 (complex dynamics); physics. None |
| f35 | `"heat invariants" "approximate" "spectral invariants" error bound` | 6 | Uçar; Mårdby–Rowlett; Hezari–Zelditch; others. None with a stability estimate |
| f36 | `"inverse spectral" "triangle orbifold"` | 0 | — |
| f37 | `"isospectral" "triangle orbifolds"` | 1 | Belolipetsky et al. 2105.06897. None |
| f38 | `"elliptic elements" "heat kernel" coefficients Fuchsian asymptotic expansion` | 15 | Garbin–Jorgenson 1603.01495; Teo 2104.00895; von Pippich; Freixas–von Pippich. Background for (c) |
| f39 | `"elliptic" "Selberg trace formula" "heat coefficients"` | 5 | Uçar; Strohmaier 1604.02722 |
| f40 | `"conical singularities" "heat kernel coefficients" hyperbolic` | 24 | **Dowker 2311.12708** (elliptic fixed points, fetched, §2.5); AKR; Hartmann–Spreafico 2001.07801; Gupta–Lal–Thakur (AdS₂ cone) |

### arXiv API (`arxiv_api_E.txt`)

Most queries were sorted by `submittedDate` to catch 2024–2026 scoops.

| # | Query | Total | Retained |
|---|---|---|---|
| p1 | `au:Batenkov AND au:Yomdin` | 19 | 1106.1137, 1502.06932, 1904.09186, 1809.00658, 1909.01927 |
| p2 | `abs:"colliding+nodes"` | 1 | Kunis–Nagel 1812.08645 (already in Q4) |
| p3 | `abs:orbifold AND abs:"heat+invariants"` | 5 | 2023–26: only Gittins et al. II |
| p4 | `abs:orbisurface*` | 0 | — |
| p5 | `abs:"cone+points" AND abs:heat` | 3 | 2025: Schueth 2511.22255 |
| p6 | `abs:"cone+points" AND abs:spectrum AND abs:hyperbolic` | 0 | — |
| p7 | `abs:"triangle+groups" AND abs:spectrum` | 1 | — |
| p8 | `abs:"heat+trace" AND abs:orbifold` | 4 | Schueth 2511.22255 |
| p9 | `ti:hear AND abs:orbifold` | 4 | Nothing 2024–26 |
| p10 | `abs:"heat+coefficients" AND abs:conical` | 1 | — |
| p11 | `abs:orbifold AND abs:isospectral` | 35 | 2024–26: Tadman 2608.28562 (Sunada on metric measure spaces); Álzaga–Lauret 2409.02213 (spherical); Bartel–Page 2407.07240 (Vignéras 3-orbifolds). None relevant |
| p12 | `abs:orbifold AND abs:Laplace AND abs:spectrum AND cat:math.DG` | 9 | None 2024–26 |
| p13 | same with `cat:math.SP` | 9 | Bertucci–Bonifacio 2606.13771 (lattice bootstrap). None |
| p14 | `abs:"cone+angles" AND abs:spectrum` | 12 | Liou 2606.20818, 2607.10149 (conic Laplacians with angles in 2πℕ); Chen–Zhong 2512.21068. None relevant |
| p15 | `abs:"hyperbolic+orbifolds" AND abs:eigenvalues` | 2 | Radcliffe 2404.14479 (bootstrap). None |
| p16 | `ti:"Automorphic+spectra" AND ti:bootstrap` | 1 | Kravchuk–Mazáč–Pal 2111.12716 (numerical spectra of triangle orbifolds) |
| p17 | `au:Bonifacio AND abs:hyperbolic` | 4 | Bonifacio 2111.13215 |
| p18 | `ti:triangle AND ti:orbifold*` | 1 | Belolipetsky math/0103015 |
| p19 | `id_list` look-ups: 1609.05142, 1107.0986, 1510.05948, 1004.1360, 1611.07676, 1207.5728, 2205.05603, 2606.20818, 2609.19604, 2607.10149, 2608.01611, 2404.14479, 2311.13330, 2609.27967, 2606.04937, 2511.23047 | — | Abstract triage only; none relevant |

### zbMATH Open (`zbmath_E.txt`, `zb_*.json`)

| # | Query | Hits | Retained |
|---|---|---|---|
| z1 | `ut:orbifold ut:heat invariants` | 3 | Gittins et al. I |
| z2 | `orbisurface heat py:2010-2026` | 3 | Uçar; Schueth 2019 |
| z3 | `cone points heat invariants` | 3 | Proceedings volumes only |
| z4 | `triangle groups isospectral` | 3 | 0781.57004 *Small volume isospectral, non-isometric, hyperbolic 2-orbifolds* (Maclachlan–Rosenberger, 1994); not fetched (gap, see report) |
| z5 | `ti:triangle groups ti:length spectrum` | 1 | Philippe 1202.20049 |
| z6 | `ti:triangle groups ti:spectrum` | 1 | Philippe 1202.20049 |
| z7 | `ti:hear ti:orbifold` | 2 | SSW 2006 (cited); Richardson–Stanhope |
| z8 | `ti:orbifold ti:heat` | 1 | 0816.53026 Cognola–Vanzo 1994 (hyperbolic 3-orbifold heat trace) |
| z9 | `ti:cone ti:heat py:2010-2026` | 32 | Engineering noise; arXiv:1301.6202 (heat equation on the cone, spherical Laplacian). Not relevant |
| z10 | `ti:isospectral ti:Fuchsian` | 0 (404) | — |
| z11 | `ti:trace function expansion spherical polygons` | 1 | Watson 1076.35042 (summary retrieved) |
| z12 | `au:Chang au:DeTurck ti:triangle` | 1 | 0721.58053 (review retrieved) |
| z13 | `au:Philippe ti:triangles` | 10 | Philippe 1202.20049, 1248.20053, 1269.53039 |
| z14 | `au:Donnelly ti:properly discontinuous` | 1 | 0411.53033 (no review text) |

### OpenAlex keyword search (`openalex_search_E.txt`), filter `publication_year:2010-2026`

| # | Query | Count | Retained |
|---|---|---|---|
| o1 | `heat invariants orbifold cone points` | 472 | Schueth 2025 (AGAG, arXiv, and HU edoc 10.18452/36958); Steklov orbifolds |
| o2 | `triangle orbifold spectrum heat` | 192 | *Hearing the Triangles: A Numerical Perspective* (CSIAM 2023, Euclidean); Garbin–Jorgenson KMJ 2020; "Beyond three terms" 2606.04937 (Neumann polygons). None on orbifolds |
| o3 | `hyperbolic orbisurface spectrum` | 30 | Philippe TSG 2010; twisted Ruelle/Selberg zeta works. None on determinacy |

### Semantic Scholar keyword search (`ss_search_E.txt`)

| # | Query | Result |
|---|---|---|
| s1 | `heat invariants hyperbolic orbifold cone orders` | HTTP 429 ×5. **Gap** |
| s2 | `hearing triangle orbifold heat trace` | total 2: Watson (listed as 2014), and an unrelated hit |
| s3 | `spectral determination triangle groups Laplace spectrum` | total 818; first 20 titles: Steklov II; *The spectra of the spherical and Euclidean triangle groups* (math/0702479). Nothing hyperbolic |
| s4 | `finitely many heat coefficients determine orbifold` | HTTP 429 ×5. **Gap** |
| s5 | `stability recovery cone angles heat trace` | Not reached (script order) |
| s6 | MCP `search_papers` "heat invariants hyperbolic orbifold cone points determine" | Rate-limit error. **Gap** |

### Consensus (MCP), one query

- **c1:** "heat trace invariants determine cone point orders of hyperbolic orbifolds" returned 10 results.
- New among them: Cognola–Vanzo 1994 (JMP 35, 3109–3116; 3-orbifolds, elliptic elements change every coefficient) and Suleymanova 2017 (heat trace on conic manifolds).
- No scoop.

### WebSearch (discovery only)

| # | Query | Result |
|---|---|---|
| w1 | `heat invariants determine cone orders hyperbolic orbifold triangle orbifold arXiv 2025` | Known items, plus E. Dryden's 2006 slides (bucknell.edu/~ed012/geometria.pdf, fetched) |
| w2 | `"orbisurfaces" OR "orbifolds" "heat invariants" "Egyptian fractions" OR "power sums" cone points spectrum` | Known items only |
| w3 | Watson 2005 NZJM full text | Not found online |

### Targeted fetches made in this sweep

All fetches are arXiv PDFs unless noted.

- **Schueth 2025:** 2511.22255.
- **Mårdby–Rowlett survey and polygons paper:** 2406.18369 and 2409.14391.
- **Fedosova–Rowlett–Zhang:** 2311.03331.
- **Philippe:**
  - 0807.4746 and 0901.4630 from arXiv;
  - TSG 2010 from centre-mersenne (`/item/10.5802/tsg.280.pdf`, HTTP 200).
- **Other arXiv full texts:**
  - Adve 2509.17935;
  - Lauret–Linowitz 2305.10950;
  - Suleymanova 1711.00577;
  - Nursultanov–Rowlett–Sher 1905.00259;
  - Steklov II 2604.18977;
  - triangular drums 2607.10556;
  - AKR 2010.02776;
  - Kokotov 0906.0717;
  - Akinshin–Batenkov–Yomdin 1502.06932;
  - Batenkov–Goldman–Yomdin 1904.09186;
  - Batenkov–Demanet–Goldman–Yomdin 1809.00658 (pdftotext warned "xref num 3 not found" but extracted);
  - Gittins et al. II 2311.00337;
  - Lassas–Lu–Yamaguchi 2404.16448;
  - Dowker 2311.12708;
  - Teo 2104.00895.
- **Dryden's 2006 slides.**

### Instrument gaps

1. **Crossref cited-by:** `/works/<doi>/cited-by` returned 404 and `getForwardLinks` returned 401, both for lack of membership.
2. **zbMATH citation index.** It is incomplete: `ci:` gives 2 hits for DGGW (OpenAlex gives 57) and 0 (404) for Dryden–Strohmaier. The `rf:` field is not supported.
3. **Semantic Scholar keyword search.** It was rate-limited (429) on 3 of 5 queries even after backoff (sleeps of 5, 10, 20 and 40 s), and the MCP search was also rate-limited. The `/citations` endpoints all succeeded.
4. **Cheeger 1983**, JDG 18, DOI 10.4310/jdg/1214438175. The Project Euclid PDF URL from Unpaywall returned an HTML page (HTTP 200, `text/html`, a JS challenge) twice. Not read; eq. (4.42) is known only through Aldana–Kirsten–Rowlett.
5. **Donnelly 1979**, Ill. J. Math. 23, 485–496, DOI 10.1215/ijm/1256048110. Unpaywall lists it as OA at Project Euclid, but both URLs tried returned HTML (HTTP 200, `text/html`). Not read; the formula is known only through Dowker 2023, eq. (1).
6. **Chang–DeTurck 1989**, PAMS 105. `www.ams.org/proc/...pdf` and `www.ams.org/journals/proc/...pdf` both returned HTTP 429 (twice). Unpaywall reports it as not OA. Content is known only from the zbMATH review.
7. **Philippe 2010**, Geom. Dedicata 149, 155–160. Unpaywall reports it as not OA, and zbMATH has no review ("contents unavailable due to conflicting licenses"). The theorem is known only from the author's own TSG survey (Théorème 3.1 there attributes it to [27], i.e. this paper).
8. **Watson 2005**, NZJM 34, 81–95. No online full text was found (Crossref has no DOI). Content is known from the zbMATH summary and from Schueth 2019, Remark 5.4(ii).
9. **Brüning–Seeley 1987**, JFA 73, 369–429. Not fetched; the formula for b₀ at p. 424 is known only through Schueth 2025, p. 1.
10. **Maclachlan–Rosenberger 1994**, *Small volume isospectral, non-isometric, hyperbolic 2-orbifolds* (Zbl 0781.57004). Not fetched; isospectral pairs of the same signature are already covered by Linowitz–Voight.
11. **Kokotov.** It is not confirmed that arXiv:0906.0717 ("Compact polyhedral surfaces of an arbitrary genus and determinants of Laplacians") is the preprint of PAMS 141 (2013) 725–735 ("Polyhedral surfaces and determinant of Laplacian"), because the arXiv record carries no journal-ref.
12. **The arXiv full-text index covers full text only partly.** A "0 hits" result there is not proof of absence in full texts.
