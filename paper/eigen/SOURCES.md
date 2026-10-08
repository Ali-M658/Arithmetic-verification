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

## 2026-10-08. Round 4: new and repaired references

Found and read on 2026-10-08 (curl or Python `urllib` with a desktop user agent; no e-mail address sent;
OpenAlex used without one). Bibliographic records: Crossref content negotiation and zbMATH Open, fetched by
`python3 paper/eigen/tools/build_bib.py --fetch` (hashes in `fetched/bib_log.json`). Texts: copied to the
git-ignored `fetched/round4/`. Scanned texts were read by OCR (tesseract) and the quoted passages checked
against the page image.

| key | identifier | fetched (URL; SHA-256) | what was read / quoted |
|---|---|---|---|
| `busercourtois1990` | doi:10.1007/bf01446910; zbMATH 0711.58033 | CSL `dcd9f850...dc29`; zbMATH `618139bb...0072`; full scan from GDZ, https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0287/LOG_0043.pdf (`fetched/round4/bc_gdz.pdf`, `5444e615...32ee`) | Full text. Thm (1.1), p. 523: "There exists an integer m = m(g, ε) with the following property. If S, S' ∈ R_g(ε) have the same first m eigenvalues then all the eigenvalues are the same." p. 523-524: "In the present proof the compactness of R_g(ε) is crucial and the constant m(g, ε) depends on ε. Nevertheless we conjecture that the theorem holds with a constant which depends only on g." (1.2), p. 524: c₁ ln(1/δ) ≤ A ≤ c₂ ln(1/δ), A = number of eigenvalues in [1/4, 1], δ = injectivity radius. Issue: Crossref says no. 1; zbMATH and the EPFL record say No. 3 (the build uses 3, checked against zbMATH). |
| `garbinjorgenson2018` | doi:10.4171/lem/64-1/2-7; zbMATH 1444.58012 | CSL `15ee587a...3cca`; zbMATH `fb9df7e0...7aa8`; arXiv:1603.01494v1 (`5ea0ec7b...bad3`) | arXiv v1 text (the e-periodica PDF is behind a bot check). §2: "Elliptic degeneration occurs when the orders of such elliptic fixed points are increasing without a bound. As these orders are running off to infinity, their corresponding cones turn into cusps." Cor. 5.5 (convergence of N_{M_q,w}(T), T ≤ 1/4, hence of the small eigenvalues); Thm 5.3 (T > 1/4: N_{M_q,w}(T) ~ c_w(T) log Q); Thm 5.7. Crossref dates the issue 2019; zbMATH: "64, No. 1-2, 161-206 (2018)" (used). |
| `garbinjorgenson2020` (existing) | doi:10.2996/kmj/1584345689 | Project Euclid PDF (`c23aac55...3b2d`) | Confirmed: this is the Kodai paper ("the first of two articles"); Def. 1.1, Thm 6.5, Cor. 6.6 (convergence of small eigenfunctions, T < 1/4). |
| `wolpert1992a`, `wolpert1992b` | doi:10.1007/bf02100600, bf02100601; zbMATH 0772.11016, 0772.11017 | CSL `9787ba31...7280`, `d91f0e28...5298`; GDZ scans LOG_0014, LOG_0015 of PPN356556735_0108 (`eeba146b...5d5d`, `45972266...5790`) | OCR of I pp. 67-69, 87 and II pp. 91-93. I, Thm 4.11 (p. 87, pinching under Criterion 4.10); II, Introduction (Thm 3.4, Thm 4.1, Cor. 4.2; "the behavior of eigenvalues in the range [0, 1/4) is relatively well understood"). |
| `ji1993` | doi:10.4310/jdg/1214454296; zbMATH 0793.53051 | CSL `2cb4536f...9263`; zbMATH `b63ee817...d698`; Project Euclid PDF (`f01d7e7a...dd7a`) | Abstract and Thms 1.1, 1.2 (pp. 264-266); the displayed bounds (1.1)-(1.3) are images not recovered by the text layer (gap). Pages 263-313 from zbMATH (the JDG record has none). p. 264 cites Hejhal's memoir as "[17, Theorems 6.6 and 7.2]" for convergence of eigenvalues < 1/4. |
| `hejhal1983` | doi:10.1007/bfb0061302; zbMATH 0543.10020 | CSL `d540e889...4094`; zbMATH `93ab9ca0...f43a` | Record only (zbMATH review read). "Vol. 2", series and volume 1001 from zbMATH. |
| `hejhal1990` | doi:10.1090/memo/0437; zbMATH 0718.11024 | CSL `ce6510f4...a9a9` | Record and zbMATH review only (AMS page returns 403). **Memoir number is 437 (vol. 88), not 469**: Crossref ("88", issue "437"), zbMATH ("Mem. Am. Math. Soc. 437, 138 p. (1990)") and Ji's bibliography [17] agree. |
| `bsv2006` | doi:10.1155/imrn/2006/71281; zbMATH 1154.11018 | CSL `f7494fdb...ddf2`; zbMATH `52e5b24b...3e0a` | Abstract (OpenAlex) and zbMATH review; full text not obtained (OUP, Hindawi archive, CiteSeerX all failed). Article ID, issue 12 and the name Strömbergsson from zbMATH. |
| `strohmaieruski2013` (existing) | doi:10.1007/s00220-012-1557-1 | arXiv:1110.2150v4 (`3815355f...b0bc`) | §7, first paragraph (completeness of computed spectra checked with the Selberg trace formula and the bound F_T(t) of eq. (19)); §6 end. |
| `buser1992` (existing) | zbMATH 0770.53001 | Internet Archive full-text search (snippets) of item `geometryspectrao0000buse` (lending copy, not downloadable) | Contents: "Chapter 6 The Teichmüller Space 138 ... 6.5 The Teichmüller Modular Group 154 6.6 A Rough Fundamental Domain 160"; "Chapter 9 Closed Geodesics and Huber's Theorem". Lemma 6.6.4 assembled from snippets: "6.6.4 Lemma. Let S be a compact Riemann surface of genus g ≥ 2 and let L > 0. There are at most (g − 1) exp(L + 6) oriented closed geodesics of length ≤ L on S which are not iterates of closed geodesics of length ≤ 2 arcsinh 1." (OCR snippets; inequality signs read as "<"). |
| `beardon1983` (existing) | doi:10.1007/978-1-4612-1146-4 | Wayback copy of the Springer chapter page for Ch. 5 "Discontinuous Groups" (`87ad381e...540e`) | Ch. 5 abstract (= opening of §5.1): "In this section we shall define and describe a class of subgroups of ℳ which have a particularly simple structure. This class contains all finite subgroups of ℳ, all abelian subgroups of ℳ and the stabilizer of each point in ℝ³." Theorem 5.4.1 and the §5.4 title: **not read** (gap). Secondary: Gardiner, *Teichmüller theory and quadratic differentials* (IA full-text snippet): "|trace(A)² − 4| + |trace(ABA⁻¹B⁻¹) − 2| ≥ 1. For an exposition of this result see Beardon [Bea, chap. V, p. 105]". |
