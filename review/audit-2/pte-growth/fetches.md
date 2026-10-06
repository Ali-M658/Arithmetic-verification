# pte-growth: sources retrieved and not retrieved

All retrieval headless (`curl`, desktop UA). Files in `review/audit-2/sources/` were fetched by the
lead's `fetch_sources.sh` (SHA256 in `sources/SHA256SUMS`); I only read them.

## Used (already in `review/audit-2/sources/`)

| source | URL | file | used for |
|---|---|---|---|
| eslpower.org, "Equal Sums of Like Powers" (Chen Shuwen), last revised 17 June 2025 | http://eslpower.org/eslp.htm | `sources/eslpower_eslp.htm` | witnesses for Lemma 1.5(3): section "( k = 1, 3 )": `[ 2, 10, 12 ] = [ 3, 8, 13 ]`; "( k = 1, 3, 5 )": `[ 1, 13, 17, 23 ] = [ 3, 9, 21, 21 ]` ("Smallest solution"); "( k = 1, 3, 5, 7 )": `[ 3, 19, 37, 51, 53 ] = [ 9, 11, 43, 45, 55 ]` ("First known solution, smallest solution, by A.Golden in 1940's"); "( k = 1, 3, 5, 7, 9 )": `[ 7, 91, 173, 269, 289, 323 ] = [ 29, 59, 193, 247, 311, 313 ]` ("First known solution, by Chen Shuwen in 2000"); "( k = 1, 2, 3, 4, 5 )": `[ 0, 5, 6, 16, 17, 22 ] = [ 1, 2, 10, 12, 20, 21 ]` (Tarry 1912). The page lists no ( k = 1, 3, ..., 11 ) entry. All re-verified exactly in `check_lemma15.py`, `check_upper.py`. |
| Coppersmith–Mossinghoff–Scheinerman–VanderKam, arXiv:2304.11254 | https://arxiv.org/pdf/2304.11254 | `sources/cmsv_2304.11254.txt` | p. 2: "Ideal solutions in the PTE problem over Z are known for n ≤10 and n = 12." Hence N(k) = k+1 for k ≤ 9 and k = 11 (with N(k) ≥ k+1, re-proved in REVIEW.md). Used only for remarks (N(11) = 12, so N_odd(7) ≤ 12). |

## Attempted, not reachable (instrument gaps)

| source | URL tried | result |
|---|---|---|
| Borwein–Ingalls, "The Prouhet–Tarry–Escott problem revisited", Enseign. Math. 40 (1994) 3–27 (Props. 2, 3, §6, p. 8) | https://www.e-periodica.ch/cntmng?pid=ens-001:1994:40::2 | HTTP 200 but a captcha page ("Verification required"), 2680 bytes; no text |
| same | http://www.cecm.sfu.ca/personal/pborwein/PAPERS/P76.pdf | HTTP 403 |
| same (Crossref lookup) | https://api.crossref.org/works?query.bibliographic=Borwein+Ingalls+... | HTTP 200, no DOI record for the 1994 paper among top hits |

Consequence: the attributions "N(k) ≥ k+1 (their Prop. 2)", "N(k) ≤ ½k(k+1)+1 (their Prop. 3, by
pigeonhole)", "listed as an open problem in [BI, §6]" and "odd ideal symmetric ... (p. 8)" are **not
confirmed** by me. Both inequalities are re-proved in REVIEW.md, so no mathematics depends on the gap;
only the citation numbering is unchecked.

Chen's survey arXiv:2506.11429 (`sources/chen_survey_2506.11429.txt`) was grepped for an appendix with
odd-exponent data; the text extraction has no searchable "Appendix A.1" heading and no "1, 3, 5, 7, 9"
string, so eslpower was used instead.
