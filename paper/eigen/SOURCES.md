# SOURCES: third-party texts for the eigen manuscript

The bibliography is built only from fetched records by `tools/build_bib.py` (which reuses
`paper/jga/tools/build_bib.py`); raw records go to the git-ignored `fetched/bib/`, with their URLs and
SHA-256 in `fetched/bib_log.json`. Twenty of the 24 entries are the records already used and checked
for the first manuscript (`paper/jga/SOURCES.md`, `review/literature-pass/CITATIONS.md`). The four
new ones were found and checked on 2026-10-07 by a reference subagent (Crossref REST API and zbMATH
Open; no e-mail address sent in any request); the fetched files were kept in the session scratch
directory, with these SHA-256:

| key | identifier | file (SHA-256) | what is used, and what was read |
|---|---|---|---|
| `jorgensen1976` | doi:10.2307/2373814, zbMATH 0336.30007 | CSL record `0f38cb05...c7ba` | Cited as the source of the argument of Lemma 8.1. **Instrument gap**: the text could not be obtained headlessly (JSTOR and doi.org return a JavaScript challenge; the Internet Archive copy of the JSTOR page is a preview with metadata only; the PDF is not archived; Project MUSE 404; OpenAlex and Semantic Scholar list the paper as closed). So the inequality is not quoted; the paper proves the case it needs (one element hyperbolic, a discrete group without parabolic elements), and says so before the lemma. The page range 739-749 is from the zbMATH record (Crossref gives only 739); the author's letter o-slash and the title's o-umlaut are from zbMATH. |
| `beardon1983` | doi:10.1007/978-1-4612-1146-4 (GTM 91) | CSL record `62f097d1...208c` | Cited for the standard models of the hyperbolic plane (distance formulas, the hyperboloid) and for the triangle reflection group having the triangle as fundamental domain. Theorem 5.4.1 (Jorgensen's inequality) could not be read (Springer shows the table of contents and an abstract only); it is not quoted. |
| `mumford1971` | doi:10.1090/s0002-9939-1971-0276410-4 | Internet Archive copy of the AMS PDF `aeb1595f...0761` | Corollary 3 (p. 294), read from the scan by OCR: "For all eps > 0, the subset {X in M_g : in the Poincare metric, all geodesics on X have length >= eps} is compact." Used only in the compactness paragraph of the introduction, which no proof uses. |
| `bers1972` | doi:10.1007/bf02764631 | Springer abstract page `71b97c1e...2bf8` | Abstract, verbatim: "It is shown that a recent compactness theorem for Fuchsian groups, due to Mumford, remains valid for groups containing elliptic and parabolic elements." Used only in the same paragraph. |

Other texts behind statements of the paper: Dryden-Strohmaier eq. (1), Thm 1.1, Prop. 3.3, Thm 3.2;
Garbin-Jorgenson Rem. 2.7, (2.8); DGGW Ex. 5.6; Ucar (4.35), Thm 4.20; Schueth 2019 Thm 4.1;
Chang-DeTurck (the angle restriction as reported in the round-3 report e, m2) are the readings recorded
for the first manuscript (`paper/jga/SOURCES.md`).
