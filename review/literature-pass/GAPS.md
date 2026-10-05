# Instrument gaps

An unreachable source is an instrument gap, never evidence that a statement is absent. Retrieval was headless only:
- curl with a desktop user agent;
- the arXiv API, arXiv full-text search, Crossref, DOI content negotiation;
- OpenAlex, the Semantic Scholar graph API, the zbMATH Open API;
- Unpaywall, GDZ, Project Euclid, the Internet Archive and the Wayback Machine;
- author pages.

Per-URL logs with HTTP codes are in `work/A–E` (sections headed "Instrument gaps") and in `work/E-search-log.md`.
Fetched files are in the git-ignored `_fetched/`.

## 1. Primaries not read, and what each affects

| source | tried | result | what rests on secondaries |
|---|---|---|---|
| Steinig, Rend. Mat. (6) 4 (1971) | zbMATH (no review); Rend. Mat. archive (curl 000); MathSciNet (subscription) | not read | the attribution and its scope ("distinct positive reals"), via Laurens p. 14 and MO 410757. CITATIONS §2 |
| Korobov–Bugaevskaya, Math. Comp. 85 (2016) | AMS PDF, repeated retries | HTTP 429 | §3 / Thm 3.1 pinpoint (quoted in the earlier G5 pass) |
| Hejhal, LNM 548 / 1001 | Springer chapters (JS challenge), archive.org (none) | not read | Ch. 3, Thm 5.1, p. 351 and its hypothesis class, via Dryden 2004 p. 7 and Garbin–Jorgenson p. 102 (two independent quotations) |
| Iwaniec, GSM 53 | archive.org, AMS | not read | (1.63) and Thm 10.2 via arXiv:2105.02068 App. A and arXiv:1408.5743. Whether Thm 10.2 covers cocompact Γ is unconfirmed |
| McKean, CPAM 25 (1972) and correction | Wiley PDF (403 Cloudflare) | not read | content via five secondaries. Do not attach a pinpoint |
| Buser 1992 | archive.org (lending only), EPFL (405) | not read | Lemma 6.6.4 via Parlier and two others. 1992 and 2010 numbering not compared |
| Wolpert 1979 | JSTOR (not OA) | not read | statement via Fanoni arXiv:2012.07344 |
| Gordon 2012 survey | AMS (429 twice) | not read | nothing. Cite only as background |
| Chang–DeTurck 1989 | AMS (429), not OA | not read | zbMATH review; Mårdby–Rowlett survey |
| Philippe, Geom. Dedicata 149 (2010) | Springer (paywall) | not read | the theorem, via the author's own Sémin. TSG survey, Thm 3.1 |
| Watson 2005 | no full text online | not read | the credit for (4.25), via Uçar pp. 134, 144 |
| Cheeger 1983; Donnelly 1979 | Project Euclid (HTML challenge) | not read | constant term via AKR; exact elliptic integral via Dowker 2023 (numerically checked) |
| Brüning–Seeley 1987; Schoen 1988; Guy D16; Maclachlan–Rosenberger 1994 | not OA / lending only | not read | optional citations only |
| Kelly 1964, Kelly 1989, Zhang–Cai 2013 (bodies) | AMS (429) | abstracts only | the Thm 8.9 correction rests on Schinzel's own text, which was read |
| Pragacz 1991; Macdonald III.8 | Springer, archive.org | not read | not recommended for citation; Borwein–Ingalls suffices |
| Sunada 1985; Shams–Stanhope–Webb 2006 | JSTOR; Springer JS shell, not on arXiv | records and reviews only | generic uses only |
| Strohmaier–Uski correction, CMP 359 (2018) | Springer JS shell | not read | inferred from the arXiv v4 comment that it does not concern the Bolza data |
| Strohmaier–Uski printed data URL (Leeds) | curl 000 | dead | data read from the arXiv v4 ancillary files instead |
| NGSolve reference (Schöberl, ASC Report 30/2014) | Crossref (no record), zbMATH documents (none), TU Wien pages (HTML, no PDF) | not fetched | only the swMATH software record (13154) is fetched; see references-additions.bib |
| Donnelly 1976 | GDZ scan (image only) | p. 161 read by eye | Thm 5.1 not read |
| McKean–Singer 1967; Kac 1966 | Project Euclid OCR; third-party JSTOR scan | read, poor OCR / third-party copy | — |

## 2. Published-version numbering not confirmed (content verified in arXiv/preprint)

| work | read in | not reachable |
|---|---|---|
| Holtz–Tyaglov, SIAM Rev. 54 (2012): (1.37), Thm 1.17 | arXiv:0912.4703v3 | SIAM (403). Two citing papers use SIAM numbers matching arXiv |
| Laurens, Calc. Var. 62 (2023): Lemma 3.2 | arXiv:2206.09050v2 | Springer bot challenge |
| Melánová–Sturmfels–Winter, Exp. Math. 33 (2024): Prop. 24 | arXiv:2106.13981v1 | T&F Cloudflare 403 |
| Müller et al., FoCM 16 (2016): Thm 1.4 | arXiv:1311.5493v2 | Springer bot challenge |
| Linowitz–Voight, Math. Z. 281 (2015): Thm A | arXiv:1408.2001v2 | paywall |
| ADFG, AGAG 33 (2008): Thm 1 | arXiv:math/0608462v1 | paywall |
| Marklof, LMS LNS 397: §11 | arXiv:math/0407288v2 | paywall; pages 83–119 vs 83–120 unresolved |
| Berndt–Yeap, Adv. Appl. Math. 29 (2002): (1.1), Cor. 2.3 | author preprint | ScienceDirect 403 |
| Allouche–Shallit 1999: §5.1, Thm 6 | author preprint | paywall |
| Borwein–Ingalls, Enseign. Math. 40 (1994): Prop. 1, §3 | authors' preprint (CECM, Dec. 1993), page images | e-periodica search 400 |

## 3. Coverage limits of the missing-literature sweep

- **Crossref cited-by:** unavailable without membership (404/401).
- **zbMATH citation index:** incomplete (2 citing records for DGGW against 57 in OpenAlex; 0 for Dryden–Strohmaier).
- **Semantic Scholar keyword search:** rate-limited on 3 of 5 queries. Its citation endpoints worked.
- **zbMATH BibTeX export** (`zbmath.org/bibtex/…`): returned 403 or a Cloudflare challenge for some sessions. Those
  records were saved as zbMATH API JSON; three entries in references-additions.bib were converted mechanically from JSON/XML.
- **arXiv full-text search:** indexes only part of the corpus, so its zero-hit "no scoop" queries bound, but do not prove,
  absence.
- **No access to MathSciNet, Google Scholar or library proxies.** A referee with library access could still find a citation
  this pass missed, most plausibly in non-arXiv conference proceedings or theses.

## 4. Checks to do with library access before submission

1. Hejhal LNM 548, p. 351, Thm 5.1: the exact hypothesis wording, to quote it in place of Lemma 4.7.
2. Iwaniec GSM 53, Thm 10.2: whether it covers cocompact groups.
3. Buser 1992, Lemma 6.6.4: check that the 1992 and 2010 numbering agree.
4. McKean 1972: the section deriving the heat trace, if a pinpoint is wanted.
5. Steinig 1971: whether repeated values or negative exponents are covered.
6. Korobov–Bugaevskaya §3 / Thm 3.1, and the published numbering of the items in §2 above.
7. The NGSolve ASC report record.
