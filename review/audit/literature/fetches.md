# Literature review (P6, P7): retrieval log and instrument gaps

All retrieval was headless: curl with a desktop user agent, the arXiv API, arXiv full-text search
(POST to arxiv.org/search_classic, searchtype=ft, redirected to search.arxiv.org), Crossref, Unpaywall,
zbMATH Open API, and the Stack Exchange API for one MathOverflow thread. PDFs and `pdftotext -layout`
extracts are in `sources/`. They were fetched by `fetch_lit.sh` and are not committed. Search logs are in `search/`.

An unreachable source is an instrument gap. It is not evidence that the source does not exist.

## Fetched (2026-10-01)

| file in `sources/` | source | result |
|---|---|---|
| `dggw_mmj2008.pdf` | Dryden–Gordon–Greenwald–Webb, Michigan Math. J. 56 (2008) 205–238, Project Euclid (open) | 200. The first attempt was blocked by the Incapsula bot wall; a retry with a different UA succeeded |
| `dggw_erratum_mmj2017.pdf` | DGGW, Erratum, Michigan Math. J. 66 (2017) 221–222 | 200. Only Theorem 5.1 is affected; §5.13–5.22 are untouched |
| `adfg_math0608462.pdf` | Abreu–Dryden–Freitas–Godinho, arXiv:math/0608462 (Ann. Global Anal. Geom., DOI 10.1007/s10455-007-9092-6) | 200 |
| `dryden_math0411290.pdf` | Dryden, "Isospectral finiteness of hyperbolic orbisurfaces", arXiv:math/0411290 | 200 (preprint; no journal version found on Crossref or zbMATH) |
| `proctor_stanhope_0811.0797.pdf` | Proctor–Stanhope, arXiv:0811.0797 (Differential Geom. Appl. 2010) | 200 |
| `stanhope_math0301357.pdf` | Stanhope, arXiv:math/0301357 (Ann. Global Anal. Geom. 27 (2005)) | 200 |
| `richardson_stanhope_1910.03224.pdf` | Richardson–Stanhope, arXiv:1910.03224 | 200 |
| `gittins1_2106.07882.pdf`, `gittins2_2311.00337.pdf` | Gittins et al., Parts 1 and 2 | 200 |
| `bari_hunsicker_1705.01412.pdf` | Bari–Hunsicker, orbifold lens spaces | 200 |
| `dgs_1107.0986.pdf` | Dryden–Guillemin–Sena-Dias, toric orbifolds | 200 |
| `grieser_maronna_1208.3163.pdf` | Grieser–Maronna, Euclidean triangles | 200 |
| `mardby_rowlett_2409.14391.pdf`, `mardby_rowlett_survey_2406.18369.pdf` | Mårdby–Rowlett | 200 |
| `msw_2106.13981.pdf` | Melánová–Sturmfels–Winter, "Recovery from power sums" | 200 |
| `laurens_2206.09050.pdf` | Laurens, KdV multisolitons (states and reproves Steinig's argument) | 200 |
| `korobov_bugaevskaya_mcom2016.pdf` | Korobov–Bugaevskaya, Math. Comp. 85 (2016) 717–736 (AMS, bronze OA) | 200. The first URL guess returned 404; the `/journals/mcom/...-02994-9` path worked |
| `css_2409.18906.pdf`, `thomas_tung_eca2027.pdf` | Conca–Singh–Soundararajan; Thomas–Tung (ECA 7 (2027)) | 200 (not relevant) |
| `search/mo_q410757.json`, `search/mo_a410757.json` | MathOverflow question 410757 and its answers (Stack Exchange API) | 200 |

## Instrument gaps

1. **Müller et al., Found. Comput. Math. 16 (2016) 69–97, published version** (DOI 10.1007/s10208-014-9239-3). Unpaywall reports it as closed. Springer returned an HTML page instead of the PDF. I used arXiv:1311.5493v2 (30 Oct 2014), which predates publication (6 Jan 2015). Theorem numbering in the published version is unverified.
2. **Steinig 1971** (Rend. Mat. (6) 4, 629–644; zbMATH 0238.10007, record without review text). Standing gap, not chased. What it proves is known here only through Laurens (arXiv:2206.09050, p. 14) and MathOverflow 410757. Their wording, "any n power sums", does not settle whether real or negative exponents are covered.
3. **Drury–Marshall 1987; Donnelly 1976.** Standing gaps, not chased.
4. **MathSciNet** (the review of Steinig cited on MathOverflow): subscription only, not attempted.
5. **Forward-citation coverage.** zbMATH `ci:` search returns only 2 documents citing DGGW 1175.58010 and none for Dryden–Strohmaier, so its citation data are clearly incomplete. Crossref gives no cited-by data without membership. As a result, the forward citation chase from DGGW, Dryden–Strohmaier and Uçar is incomplete. The negative search result in PRIORITY-notes.md is bounded by this.
6. **Dryden PhD thesis** (Dartmouth 2004, DOI 10.1349/ddlp.58): not fetched. Its arXiv spin-off math/0411290 was read.
7. **Korobov–Bugaevskaya**: `pdftotext` reports 7 PDF pages, but the extract runs from p. 717 to the references at p. 736. I checked its §3 statements only.
