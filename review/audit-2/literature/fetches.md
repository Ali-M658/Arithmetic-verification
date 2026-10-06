# G5-bis literature: fetches and instrument gaps

All retrieval headless (curl, desktop user agent; arXiv/Crossref/OpenAlex/zbMATH/Semantic Scholar APIs). Dates: 2026-10-06.
Text re-extracted with pymupdf into `txt/` (one `=== PDF PAGE n ===` marker per page). Scanned pages were rendered to PNG
(scratchpad) and read as images; this is stated in REVIEW.md wherever it applies.

## Re-fetched by this reviewer (files in `sources/`)

| source | URL | HTTP | file | SHA256 | note |
|---|---|---|---|---|---|
| Melzak, CMB 4 (1961) 233-237 | https://doi.org/10.4153/CMB-1961-025-1 -> cambridge.org landing | 200 | (html) | | landing page only |
| idem, PDF | https://www.cambridge.org/core/services/aop-cambridge-core/content/view/8F448D799B4688B77081C820811C861C/S000843950005089Xa.pdf/div-class-title-a-note-on-the-tarry-escott-problem-div.pdf (URL from Unpaywall `url_for_pdf`) | 200 | sources/melzak_cmb1961.pdf | 2d205759d2b4f06885def51508e5809109dc47e587fde0bbbbdefee502876676 | identical to theory/pte/sources/Melzak1961_CMB4.pdf (hash in its SHA256SUMS). Text layer present; pages also rendered and read as images |
| Crossref record, Melzak | https://api.crossref.org/works/10.4153/CMB-1961-025-1 | 200 | - | - | metadata only |
| BLP, Math. Comp. 72 (2003) 2063-2070 | https://www.ams.org/mcom/2003-72-244/S0025-5718-02-01504-1/S0025-5718-02-01504-1.pdf | 200 but HTML (bot page) | discarded | - | |
| idem | https://www.ams.org/journals/mcom/2003-72-244/S0025-5718-02-01504-1/S0025-5718-02-01504-1.pdf | 200, application/pdf, 8 pp | sources/blp2003_ams.pdf | f766f9833bafcc398e02c7bdb8ce34b24ff064a1105a24c6110fd7394d8afeac | publisher's PDF (open after embargo); identical to theory/pte/sources/BLP2003_MathComp72_authorcopy.pdf |
| BLP author copies tried | carmamaths.org .../PTE/pte.pdf; cecm.sfu.ca/~pborwein/PAPERS/P177.pdf (http/https); cecm.sfu.ca/personal/pborwein/PAPERS/P177.pdf; cecm.sfu.ca/~colinp/ | 404 / 404 / 403 / 404 | - | - | not needed (publisher PDF obtained) |
| Crossref / Unpaywall / OpenAlex, BLP | api.crossref.org/works/10.1090/S0025-5718-02-01504-1; api.unpaywall.org/v2/...; api.openalex.org/works/doi:... | 200 | - | - | metadata |
| Borwein-Ingalls, Ens. Math. 40 (1994) 3-27 (e-periodica) | https://www.e-periodica.ch/digbib/view?pid=ens-001:1994:40::3 (and ::78) | 200 (viewer HTML) | - | - | |
| idem, PDF download | https://www.e-periodica.ch/cntmng?pid=ens-001%3A1994%3A40%3A%3A3 (also ::4, ::5, ::78) | 200 but "Verification required" (proof-of-work captcha page, 2.7 kB) | - | - | **instrument gap for an independent re-fetch**: cannot be passed headlessly |
| Wright, "On Tarry's problem (I)", Quart. J. Math. 6 (1935) 261-267 | https://doi.org/10.1093/qmath/os-6.1.261 -> academic.oup.com | 403 (Cloudflare) | - | - | **instrument gap** (Crossref confirms DOI, title, pages) |
| Sun-Zhao, arXiv:2307.11330v3 | https://arxiv.org/pdf/2307.11330v3 ; https://arxiv.org/abs/2307.11330v3 | 200 / 200 | sources/arxiv_2307.11330v3.pdf, sources/arxiv_2307.11330_abs.html | 590dcd6a409bcc6a85a1af607a02532b6306be7899612619a0954817836b1e8c / 07c5781743160b9bdb9440a16c6a91504f777c50fbc1b0864225d621aa2deab5 | found by the adversarial search (O4) |

Note: one Unpaywall request (Melzak and BLP DOIs) carried a personal contact address as the `email` parameter; all later
API requests used the placeholder research@example.com.

## Copies used from `theory/pte/sources/` (raw files only, hash-checked)

`shasum -a 256 -c theory/pte/sources/SHA256SUMS`: all 29 entries **OK** (run 2026-10-06).

| file | SHA256 (matches SHA256SUMS) | use |
|---|---|---|
| BorweinIngalls1994_EnsMath40_pages3-27.pdf | 9f86455488ec398d96347b6e7be73cd6f2bf973a249bc5bd409c56c961ade68c | scanned, **no text layer**: all 25 pages rendered at 110 dpi and pp. 3-11, 25-27 **read from images** (quotes in REVIEW.md are from the images) |
| BorweinIngalls1994_EnsMath40_pages3-27.txt | 4f8b7897b9bfd95251111aa824dffe78c535d510dd4e4b1d8437a56cc4ddf196 | OCR; used only to locate keywords by page (perfect, o(k, prize, Letac, Melzak), never quoted |

`theory/pte/sources/NOTES.md`, `theory/pte/LITERATURE.md` and every other file of `theory/pte/` were **not opened**.

## Fetched sources in `review/audit-2/sources/` (fetch_sources.sh), hash-checked

`shasum -a 256 -c review/audit-2/sources/SHA256SUMS`: all 15 entries **OK**. Where the same document is in both folders the
hashes agree: Chen survey 3273f806..., CMSV 7fc6efdf..., Croot-Mao-Yip cf77a5bd..., Wooley 1101.0574 df5f9d12...,
Wooley 1708.01220 0a1e7fa3..., Choudhry 26ec79d2..., Caley 32eacdc7..., eslpower TarryPrb 7000138842..., eslp 027bf837..., kminus 3b9cd832....
The `.txt` files in review/audit-2/sources are not in SHA256SUMS, so I re-extracted all PDF text myself (`txt/`).

## Adversarial searches (O4 / B7), raw results in `search/`

| service | query | HTTP | result file |
|---|---|---|---|
| arXiv API | all:"Prouhet-Tarry-Escott upper bound", "Tarry-Escott problem bound", "Tarry's problem Vinogradov", "Prouhet Tarry Escott problem", "equal sums of like powers" (max 100 each) | 200 x5 | search/arxiv_[1-5].xml |
| arXiv API | abs:Tarry OR ti:Tarry OR abs:Escott OR abs:multigrade(s), 400 max | 200 (304 entries) | search/arxiv_broad.xml, arxiv_broad_list.txt |
| Semantic Scholar graph API | same five queries | **429 rate limited** x5 | search/ss_[1-5].json (error bodies) |
| Semantic Scholar (MCP) | paper search | rate limited | - |
| Semantic Scholar (MCP) | details ARXIV:2307.11330; citations of DOI 10.1090/S0025-5718-02-01504-1 (BLP) | 200 | (in REVIEW.md) |
| OpenAlex | same five queries | 200 x3, 2 truncated (curl timeout at 40 s) | search/oa_[1-5].json (4, 5 unparseable) |
| OpenAlex | abstracts of 7 DOIs surfaced (Barrodale thesis, Jovicevic preprints, Chen S.Y. preprint, Hajdu-Papp-Tijdeman) | 200 | (summarised in REVIEW.md) |
| zbMATH Open API | ti:Tarry py:1994-2026 | 200 (64 records) | search/zb.json |

Gaps in the search: Semantic Scholar keyword search unavailable (rate limit); two OpenAlex result pages truncated;
Google Scholar not queried (no headless API). The arXiv + zbMATH + OpenAlex + BLP-citation sweep is the evidence for O4.

## Not reached (instrument gaps)

1. Borwein-Ingalls from e-periodica (captcha). Used the hash-verified copy in theory/pte/sources instead.
2. Wright 1935 (Quart. J. Math., OUP 403). The exact form of Wright's bound is known to me only via Melzak p.234.
3. Hua, *Introduction to Number Theory* (1982) and Hua 1938/1949 (the source of the M(k) bound): not attempted (book, paywalled).
4. Published versions of Wooley 2012 (Annals) and 2019 (PLMS): theorem numbers checked in the arXiv versions only.
5. Gloden, *Mehrgradige Gleichungen* (1944), Letac 1942: not reachable; Letac attributions rest on BI, BLP, CMSV, Chen.
