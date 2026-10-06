# fetches.md — group pte-structure

All retrieval headless (`curl`, desktop UA). Dates: 2026-10-06.

## Retrieved by this reviewer

| source | URL | HTTP | result / file |
|---|---|---|---|
| Crossref search, Borwein–Ingalls | `https://api.crossref.org/works?query.bibliographic=Borwein+Ingalls+Prouhet-Tarry-Escott+problem+revisited&rows=3` | 200 | No DOI for Borwein–Ingalls (Enseign. Math. 40 (1994)) among the top 3 hits (they were Borwein's book ch. 11, BLP Math. Comp. 2003, an SSRN item). Not saved. |
| e-periodica, L'Enseignement Math. volumes list | `https://www.e-periodica.ch/digbib/volumes?UID=ens-001` | 200 | Volume id `ens-001:1994:40` found. Not kept. |
| e-periodica, volume 40 (1994) viewer | `https://www.e-periodica.ch/digbib/view?pid=ens-001:1994:40#3` | 200 | Viewer HTML. Contains the link title "THE PROUHET-TARRY-ESCOTT PROBLEM REVISITED". No article text. Not kept. |
| e-periodica content manager (PDF) | `https://www.e-periodica.ch/cntmng?pid=ens-001:1994:40::3` | 200 | Returns a **"Verification required" proof-of-work CAPTCHA page**, not the PDF. Kept as `fetched/eperiodica_cntmng_ens-001_1994_40__3_captcha.html` (sha256 fe1f7e1d…0ed244). **Instrument gap.** |
| same viewer page, second attempt | `https://www.e-periodica.ch/digbib/view?pid=ens-001%3A1994%3A40%3A%3A3` | — | Timed out after 120 s. No file. |

## Pre-fetched texts used (review/audit-2/sources/, hashes in SHA256SUMS)

| file | used for | location |
|---|---|---|
| `chen_survey_2506.11429.txt` (pdf sha256 3273f806…) | Definition of "ideal symmetric" solution (Definition 2, eq. (1.6)). Escott's degree-6 solution [0,18,27,58,64,89,101]=₆[1,13,38,44,75,84,102] (eq. (A.322)), used **only as a number** and re-verified exactly in `check_balanced.py`. | p. 12 (Definition 2, Example 1.1) |
| `croot_mao_yip_2609.05061.txt` (pdf sha256 cf77a5bd…) | Status of the N(k) bounds. Quote: "It is easy to see P(k, 2) ≥ k + 1 and it is an open problem to determine if P(k, 2) = k + 1. It is only known that P(k, 2) = k + 1 when 2 ≤ k ≤ 9 and k = 11 [2]. Using a pigeonhole principle argument one can easily see that P(k, m) ≤ k(k+1)/2 + 1." Also: "The best-known upper bound is W(k, m) ≤ k(k+1)/2 + 1, due to Wooley [22, Theorem 13.1]." | p. 1–2 (§1) |

## Not reachable (instrument gaps)

- **Borwein–Ingalls, "The Prouhet–Tarry–Escott problem revisited", Enseign. Math. 40 (1994) 3–27.** The e-periodica PDF sits behind a CAPTCHA. The bundle forbids `theory/pte/sources`, so the project's own copy was not used. As a result these citations are **not verified**:
  - "p. 8" (odd ideal symmetric);
  - "Props. 2, 3" (k+1 ≤ N(k) ≤ k(k+1)/2+1);
  - "§1" (definition of N(k));
  - "§6" (o(k²) listed as open).

  Both bounds on N(k) were re-proved independently (see REVIEW.md, PS.2/PS.6). Croot–Mao–Yip p. 1 (fetched) states the same two bounds and the same open status. That text is secondary and does not replace the BI page and proposition numbers.
