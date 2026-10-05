# D. Missing classical spectral literature for Section 4 ("Heat does not hear the shape")

Scope: manuscript `paper/jga/manuscript.tex`, §4 (lines 619–797), Thm 1.2 (lines 135–146), §1.1 prior work (lines 167–178). Referee items G7-2, G7-6, G7-23 and disagreement 6 (Lemma 4.7) of `review/referee-sim/G7-VERDICT.md`. Background: `theory/locality/attack-log.md:45` records "Hejhal and Iwaniec were not fetched (§1.10). Lemma 3.2 replaces them."

All files named below are under `review/literature-pass/_fetched/` (pdf/, txt/, bib/).

## 0. Bottom line

1. **Lemma 4.7 (lem:admissible) is redundant. Delete it.** Dryden and Strohmaier's eq. (1), which the manuscript cites as the source of the trace formula, is itself cited there to Hejhal LNM 548 and Iwaniec ("Selberg's trace formula for orbisurfaces (see [7], [8]) reads", arXiv v2 p. 3; CMB pp. 67–68, refs [7] = Hejhal Vol. I, [8] = Iwaniec). Hejhal's own hypothesis on h is the classical strip/decay class. Dryden (2004) quotes it verbatim, states it for cocompact Fuchsian groups *with* elliptic terms, and applies it to the heat function $h(r)=e^{-r^2t}$ with the words "Then h(r) satisfies Assumption 4.2". The Paley–Wiener truncation in Lemma 4.7 only recovers a special case of a 1976 theorem.
2. **Thm 4.6 (thm:IEH) becomes a direct citation:** Hejhal Vol. I, Ch. 3, Thm 5.1 (p. 351; trivial character), with the heat function inserted. Two fetched, open-access sources state exactly this heat-kernel identity with elliptic terms and can be cited alongside Hejhal: Garbin–Jorgenson, Kodai Math. J. 43 (2020), Remark 2.7, eqs. (2.7)–(2.8), p. 101, derived directly from the periodized heat kernel, with no test-function class needed; and Dryden (2004), eq. (3), p. 9.
3. **Lemma 4.8 (lem:counting) is standard in method. Keep it, but cite Buser Lemma 6.6.4.** Buser proves the surface version, $(g-1)e^{L+6}$ primitive geodesics of length ≤ L, by the same ball-packing/area argument. This is attested by three fetched secondaries; Buser itself was not reachable. The orbifold version with the diameter is a routine adaptation and is needed for the explicit constant in Thm 4.9(b). Huber (1959) Satz 9 gives the asymptotic count for closed surfaces, but no uniform bound.
4. **Thm 4.9/4.10 (quantitative locality and sharpness) are a quantitative packaging of a classical argument.** In the proof of his Thm 4.5 (arXiv p. 9), Dryden (2004) already runs the heat trace formula on hyperbolic orbisurfaces and identifies the shortest closed geodesic as "the unique ω > 0" for which $f(t)e^{\omega^2/4t}$ has a finite nonzero limit as $t\downarrow0$. This is the qualitative content of Thm 4.10(ii)–(iii), the leading $e^{-\ell^2/4t}$ behaviour of the hyperbolic term. What remains new in §4 is modest: the explicit constant in 4.9(b), the one-time bound 4.9(c), and the $t^{-1/2}$ prefactor statement (Cor. 4.11).
5. **Thm 1.2(i) (signature locality) follows at once from the classical trace formula.** Once Hejhal's formula is written for the heat function, I depends only on area, E depends only on the cone orders, and the hyperbolic term is $O(t^{-1/2}e^{-\ell^2/4t})$. For surfaces this mechanism is McKean (1972) (primary not reachable, see §3). The novelty claim for Thm 1.2(i)–(ii) should be withdrawn and the result stated as a cited proposition, as G7-2 asks.
6. **Missing references to add:** Hejhal 1976 (and 1983 only if the cusp case is mentioned), Iwaniec 2002, McKean 1972 (+ 1974 correction), Huber 1959, Buser 1992, Wolpert 1979, Stanhope 2005, Dryden 2004 (arXiv) / Dryden thesis, Garbin–Jorgenson 2020. Gordon 2012 is optional and cannot be read (gap). Optional: Brooks–Gornet–Gustafson 1998, Parlier 2018. Not recommended: Osgood–Phillips–Sarnak 1988, Kokotov/King/Spreafico (see §4.7).

---

## 1. Table: classical citations the manuscript must carry

"Cite as written" is "(absent)" in every row: none of these keys is in `paper/jga/references.bib`. I checked by grep: no McKean 1972, Hejhal, Iwaniec, Buser, Huber, Wolpert, Stanhope or Garbin entries; Dryden appears only through `drydenstrohmaier2009` and `dggw2008`.

| manuscript line | cite as written | claim the manuscript makes (short) | source location found | verbatim quote | verdict | correction |
|---|---|---|---|---|---|---|
| 689–694 (Thm 4.6 proof) | [DS, eq. (1)] + Lemma 4.7 | trace formula with elliptic terms holds for $h_t$ | Hejhal Vol. I Ch. 3 Thm 5.1, p. 351 (as reported by Garbin–Jorgenson KMJ p. 102 and Dryden 2004 p. 7) | Dryden 2004 p. 7: "Hejhal [14] obtains the following version of the Selberg Trace Formula for the case of interest: Theorem 4.3. Suppose that • Γ ⊂ PSL(2,R) is a Fuchsian group with compact fundamental region; • h(r) satisfies Assumption 4.2; …" Assumption 4.2: "• h(r) is an analytic function on \|Im(r)\| ≤ 1/2 + δ; • h(−r) = h(r); • \|h(r)\| ≤ M[1 + \|Re(r)\|]^{−2−δ}." | NEEDS CORRECTION (missing primary citation; Lemma 4.7 redundant) | Replace "The function $h_t$ is not of exponential type … Lemma 4.7 extends the formula to it by approximation" with: "This is Selberg's trace formula for cocompact Fuchsian groups with elliptic elements [Hejhal 1976, Ch. 3, Thm 5.1] (trivial character), whose hypotheses (h even, holomorphic in $\|\mathrm{Im}\,r\|\le\frac12+\delta$, $h(r)=O((1+\|r\|)^{-2-\delta})$ there) $h_t$ satisfies; for the heat kernel see also [Garbin–Jorgenson 2020, Remark 2.7] and [Dryden 2004, (3)]." Delete Lemma 4.7. |
| 694 | \cite{marklof2011} | heat function admissible for torsion-free groups | Marklof arXiv math/0407288, (H1)–(H3), Prop. 10 | "(H1) h is analytic for \| Im ρ\| ≤ σ for some σ > 1/2; (H2) h is even …; (H3) \|h(ρ)\| ≪ (1 + \| Re ρ\|)^{−2−δ} …" and "For any β > 0, the test function h(ρ) = e^{−βρ²} is admissible in the trace formula." | ACCURATE | keep; the orbifold case is now covered by Hejhal, so the "for orbifolds, Lemma …" clause goes |
| 701 (Lemma 4.7 proof) | [DGGW Thm 4.8] for Weyl bound | | — | — | moot | deleted with Lemma 4.7; Remark 4.12's "not an independent proof" caveat then lapses (see §5) |
| 704–712 (Lemma 4.8) | (no citation) | geodesic counting bound | Buser Lemma 6.6.4 (via Parlier arXiv:1611.02040 p. 6; Hubard et al. arXiv:2504.00916 p. 4) | Parlier: "Lemma 2.4 … there are at most (g − 1)e^{L+6} primitive closed geodesics of length most L. Proof. The statement is not exactly the statement from [5, Lemma 6.6.4] … Buser shows that the number of closed geodesics … are bounded above by (cosh(L+3r)−1)/(cosh(r)−1) · 2(g−1)/(cosh(r/2)−1) … obtained by covering the thick part of the surface by balls of radius arcsinh(1) and by counting geodesic loops based in the centers of the balls … and using an area comparaison argument." | NEEDS CORRECTION (missing attribution) | Add "This is the standard area argument; cf. [Buser 1992, Lemma 6.6.4] for surfaces." Keep the lemma for the explicit constant. |
| 714–746 (Thm 4.9), 750–770 (Thm 4.10) | (no classical citation) | hyperbolic term governs the difference; exponent $\ell^2/4t$ attained | Dryden 2004 proof of Thm 4.5, p. 9 | "Consider the function $f(t)e^{\omega^2/4t}$. Take the limit of this function as t ↓ 0; we see that there is a unique ω > 0 for which this limit is finite and nonzero. Let γ1 be the shortest primitive closed geodesic in O. Then ω = ℓ(γ1)." | NEEDS CORRECTION (prior art not cited) | Before Thm 4.9 add: "The mechanism is classical: for surfaces it goes back to McKean [1972] and Huber [1959], and for hyperbolic orbisurfaces Dryden [2004, proof of Thm 4.5] reads off the systole from the $e^{-\ell^2/4t}$ decay of the hyperbolic term. Theorems 4.9–4.10 make this quantitative." |
| 626–632 (Thm 4.1), 135–146 (Thm 1.2(i)) | DGGW, Uçar, Donnelly | heat invariants depend only on signature | Hejhal Thm 5.1 via Dryden (2) p. 7: identity term $\frac{\mu(F)}{4\pi}\int rh(r)\tanh(\pi r)dr$, elliptic term depends only on $m(R),\theta(R)$ | (formula as quoted above) | NEEDS CORRECTION (novelty) | Add McKean 1972 for the surface case (primary unverified, §3) and the trace-formula derivation. Demote Thm 1.2(i) to a cited proposition. |
| 793–796 (Rem. 4.13) | [DS Thm 1.1], [LV Thm A] | heat trace determines spectrum and length spectrum; isospectral pairs within a signature | Huber 1959 Satz 7, Satz 8 (p. 8); Wolpert 1979 via Fanoni arXiv:2012.07344 p. 1; Dryden 2004 Thm 5.1 p. 10 | Huber p. 8 (OCR, corrected): "Satz 7. Geschlossene hyperbolische Raumformen mit gleichem Längenspektrum besitzen auch gleiches Eigenwertspektrum und gleiches Geschlecht." "Satz 8. Geschlossene Raumformen mit gleichem Eigenwertspektrum besitzen auch gleiches Längenspektrum und gleiches Geschlecht." | NEEDS CORRECTION (missing context) | Add: the surface case is Huber's theorem [Huber 1959, Sätze 7–8]; for surfaces Wolpert [1979] shows the spectrum determines a generic point of Teichmüller space; within a signature (genus ≥ 1) isospectral sets are finite [Dryden 2004, Thm 5.1], generalizing McKean [1972]. |
| 167–172 (§1.1) | DS, Doyle–Rossetti, Uçar | spectrum determines cone orders | Stanhope 2005 Main Thms 1–2; Dryden 2004 Thm 4.5 | Stanhope arXiv p. 1: "Main Theorem 1: Let S be a collection of isospectral Riemannian orbifolds that share a uniform lower bound κ(n − 1) on Ricci curvature, where κ ∈ R. Then there are only finitely many possible isotropy types, up to isomorphism, for points in an orbifold in S." | NEEDS CORRECTION (missing prior work) | Add one sentence before DS: "Stanhope showed that isospectral orbifolds with a common lower Ricci bound have finitely many isotropy types and a bounded number of singular points [Stanhope 2005, Main Thms 1–2], and Dryden used this with the trace formula to determine the cone orders of a hyperbolic orbisurface up to finitely many possibilities [Dryden 2004, Thm 4.5]." |

---

## 2. Bib-record check (records to add; all raw fetches saved)

| key | source of raw record (saved file) | notes / discrepancies |
|---|---|---|
| mckean1972 | Crossref CN `https://doi.org/10.1002/cpa.3160250302` → `bib/mckean1972.bib`; zbMATH `https://zbmath.org/bibtex/0225.30021.bib` → `bib/mckean1972_zb.bib` | Crossref title is lower-case "riemann"; use the zbMATH title. CPAM 25(3) (1972) 225–246. |
| mckean1974corr | Crossref CN `10.1002/cpa.3160270109` → `bib/mckean1974corr.bib`; zbMATH 0317.30018 → `bib/mckean1974corr_zb.bib` | **The Crossref record is malformed** (no author, garbled key, misspelt title "Silberg' trace formua"). Use zbMATH: "Correction to: `Selberg's trace formula as applied to a compact Riemann surface'", CPAM 27 (1974) 134. |
| hejhal1976 | Crossref CN `10.1007/BFb0079608` → `bib/hejhal1976.bib`; zbMATH 0347.10018 → `bib/hejhal1976_zb.bib` | LNM 548. Crossref lacks the volume number; use zbMATH (volume = 548). Ch. 3 "The trace formula for vector-valued functions" = pp. 326–354 (Crossref chapter record 10.1007/BFb0079611). |
| hejhal1983 | Crossref CN `10.1007/BFb0061302` → `bib/hejhal1983.bib`; zbMATH 0543.10020 → `bib/hejhal1983_zb.bib` | **Crossref title omits "Vol. 2"**; use zbMATH (LNM 1001). Needed only if the cusp case is mentioned. |
| iwaniec2002 | Crossref CN `10.1090/gsm/053` → `bib/iwaniec2002.bib`; zbMATH 1006.11024 → `bib/iwaniec2002_zb.bib` | **Crossref gives ISBN 9781470417987, which is not the 2002 hardback ISBN.** zbMATH gives 0-8218-3160-7, 2nd ed., GSM 53. Use zbMATH. |
| buser1992 | zbMATH `https://zbmath.org/bibtex/0770.53001.bib` → `bib/buser1992.bib` | Progress in Math. 106, Birkhäuser 1992. **The DOI 10.1007/978-0-8176-4992-0 is the 2010 Modern Birkhäuser Classics reprint** (`bib/buser2010reprint.bib`). Cite one or the other consistently, not the 1992 book with the 2010 DOI. |
| huber1959 | Crossref CN `10.1007/BF01369663` → `bib/huber1959.bib`; zbMATH 0089.06101 → `bib/huber1959_zb.bib` | Math. Ann. 138 (1959) 1–26. Agrees. |
| huber1961 | Crossref CN `10.1007/BF01451031` → `bib/huber1961.bib` | Math. Ann. 142 (1961) 385–398 (optional; there is also a Nachtrag, 143 (1961) 463–464). |
| wolpert1979 | Crossref CN `10.2307/1971114` → `bib/wolpert1979.bib`; zbMATH 0441.30055 → `bib/wolpert1979_zb.bib` | **Crossref gives only "pages={323}"**; zbMATH gives 323–351. Use zbMATH. |
| gordon2012orbifolds | Crossref CN `10.1090/pspum/084/1348` → `bib/gordon2012orbifolds.bib`; zbMATH 1326.58016 → `bib/gordon2012orbifolds_zb.bib` | Crossref types it @misc with no editors or series volume. Use zbMATH @incollection, in *Spectral Geometry*, Proc. Sympos. Pure Math. 84, AMS 2012, pp. 49–71. |
| stanhope2005 | Crossref CN `10.1007/s10455-005-1584-7` → `bib/stanhope2005.bib`; arXiv API math/0301357 → `bib/stanhope2005.arxiv.xml` | Ann. Global Anal. Geom. 27(4) (2005) 355–375. Agrees with zbMATH 1085.58026. |
| dryden2004 | arXiv API math/0411290 → `bib/dryden2004.arxiv.xml` (raw Atom XML; arXiv issues no BibTeX through the API); thesis Crossref CN `10.1349/ddlp.58` → `bib/dryden2004thesis.bib` | Preprint "Isospectral Finiteness of Hyperbolic Orbisurfaces", arXiv:math/0411290 (2004). zbMATH lists it only as a preprint (id 900021196), so I found no journal version. The thesis record lacks a year. Cite the arXiv preprint; the thesis is Dartmouth 2004 (year per Dryden 2004 ref. [7]). |
| garbinjorgenson2020 | Crossref CN `10.2996/kmj/1584345689` → `bib/garbinjorgenson2020.bib` | Kodai Math. J. 43(1) (2020) 84–128. The Crossref record has **no pages field**; pages 84–128 are from the published PDF header ("KODAI MATH. J. 43 (2020), 84–128"). |
| bgg1998 (optional) | Crossref CN `10.1006/aima.1998.1750` → `bib/bgg1998.bib` | Adv. Math. 138 (1998) 306–322. |
| parlier2018 (optional) | Crossref CN `10.1007/s00208-017-1571-x` → `bib/parlier2018.bib` | Math. Ann. 370 (2018) 1759–1787 (Crossref "year 2017" is the online date). |
| ops1988 (not recommended) | Crossref CN → `bib/ops1988.bib` | J. Funct. Anal. 80 (1988) 212–234. |

Existing record `drydenstrohmaier2009` (references.bib l. 62–70) matches Crossref (`bib/drydenstrohmaier2009_check.bib`): CMB 52(1) (2009) 66–71. ACCURATE.

---

## 3. Instrument gaps

| what | URLs tried | result |
|---|---|---|
| McKean 1972 full text | `https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cpa.3160250302`, `/doi/pdf/…` | 403 (Cloudflare). Unpaywall: not OA. archive.org: only the "Vol 25 Index" scan (`sim_communications-on-pure-and-applied-mathematics_1972_25_index`), no issue scan. |
| McKean 1974 correction | `https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/cpa.3160270109` (Unpaywall says OA) | 403 (Cloudflare) |
| Hejhal LNM 548 / 1001 | `https://link.springer.com/chapter/10.1007/BFb0079611`, `…/BFb0079609`, `…/content/pdf/10.1007/BFb0079611.pdf`, `…/content/pdf/bfm:978-3-540-38063-0/1` | 200 but a JavaScript "Client Challenge" page (3038 bytes), no content. archive.org advancedsearch: no item. |
| Hejhal, Duke Math. J. 43 (1976) 441–482 (survey of Vol. I) | projecteuclid `…/10.1215/S0012-7094-76-04338-6.full` | HTML bot wall. Not OA (Unpaywall). |
| Iwaniec GSM 53 | archive.org search: none; AMS: no OA | not reached; content verified only through secondaries (§4.2) |
| Buser 1992 | archive.org `geometryspectrao0000buse` (_djvu.txt, _hocr_searchtext, page_numbers) | 403, controlled lending. `fulltext/inside.php` returns "Item not available". `https://infoscience.epfl.ch/record/161403` returns 405. |
| Wolpert 1979 | JSTOR (10.2307/1971114), not OA | not attempted beyond Unpaywall (not OA); content verified through secondaries |
| Gordon 2012 survey | `https://www.ams.org/books/pspum/084/1348/pspum084-1348.pdf`, `https://www.ams.org/books/pspum/084/1348` | 429 (rate limit), retried after 20 s: 429. No arXiv version (arXiv API title search: none). Only the zbMATH summary was obtained. |
| Huber 1959, 1961 | GDZ `https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0138/LOG_0007.pdf` and `…_0142/LOG_0046.pdf` | **Reached** (image-only scans). OCR'd with tesseract (English model only, so umlauts are lost) → `txt/huber1959_ocr.txt`, `txt/huber1961_ocr.txt`. Quotations below restore umlauts and are marked "(OCR)". |

Consequence: for McKean, Hejhal, Iwaniec, Buser and Wolpert, the statements below are verified through fetched secondary sources that quote them with theorem/page numbers, not from the primary. The verdict on each pinpoint (e.g. "Hejhal Thm 5.1, p. 351") is **CANNOT VERIFY (primary)**, **corroborated by two independent secondaries**. Before submission, someone with library access should check: Hejhal LNM 548 p. 351 Thm 5.1 and its hypotheses; Iwaniec Thm 10.2 and (1.63); Buser Lemma 6.6.4; McKean §§ on the heat expansion.

---

## 4. Per-work analysis

### 4.1 H. P. McKean, "Selberg's trace formula as applied to a compact Riemann surface", CPAM 25 (1972) 225–246; Correction, CPAM 27 (1974) 134

**Fetched:** bibliographic records only (primary text is a gap).

**What it proves (from fetched secondaries):**
- Finiteness of isospectral sets of compact Riemann surfaces. Linowitz arXiv:1309.0499 p. 1: "It is a result of McKean [15] that for a fixed Riemann surface S, there are at most finitely many Riemann surfaces which are isospectral to S and pairwise non-isometric." Dryden arXiv:math/0411290 p. 10: "McKean [15] showed that only finitely many compact Riemann surfaces have a given spectrum." Courtois–Kim arXiv:1612.04594 p. 2: "McKean in the 70's showed [34] that there exists only finite number of hyperbolic metrics on a surface with a given Laplace spectrum."
- Derivation of the trace formula through the heat kernel. Pollicott arXiv:2204.08203 p. 2: "Trace formulae: The very readable article of McKean on the use of heat kernels [24]". Garbin–Jorgenson KMJ p. 103 (arXiv l. 1825): "the derivation of the group sum side of the Selberg trace formula (in particular, see [McK 72])". Bolte et al. arXiv:1608.08294 p. 27: "the elementary derivation of STF in the case where Γ\H² is a compact Riemann surface following McKean([84]) and Hejhal([57])".

**The two questions asked:**
- *Does McKean derive the heat-trace expansion via Selberg and note that the hyperbolic terms are $O(e^{-c/t})$?* The secondaries confirm a heat-kernel derivation of the trace formula for compact surfaces. I could not verify verbatim that McKean writes out the small-t expansion with the hyperbolic part as $O(e^{-c/t})$, so do not attribute that sentence to him with a pinpoint. The safe citation is "[McKean 1972] (trace formula via the heat kernel for compact Riemann surfaces)".
- *Does he treat elliptic elements?* All secondaries describe the setting as compact Riemann surfaces (torsion-free Γ). Dryden (2004) explicitly *extends* McKean's finiteness to orbisurfaces, which implies McKean did not treat them. Garbin–Jorgenson cite McKean only for the conjugacy-class decomposition. Conclusion: no elliptic elements. Not verified verbatim.

**Relation to the paper's results.**
- Thm 1.2(i): for surfaces (n = 0) every heat invariant is a function of the genus. This follows from McKean's heat trace formula and also from McKean–Singer 1967, which the paper already cites. The orbifold statement adds only the elliptic term, which Hejhal's formula supplies (§4.2).
- Thm 1.2(ii): not addressed by McKean.
- Thm 1.2(iii): McKean's heat-kernel trace formula is the mechanism.
- McKean's finiteness theorem bounds the isospectral pairs that Remark 4.13 says "the heat trace still misses".
- Thms 1.1, 1.3, 1.4: no relation.

**Where to cite:** (a) Thm 4.1's discussion (line 636), "for surfaces this is classical [McKean 1972]"; (b) Thm 4.6 proof, with Hejhal; (c) Remark 4.13 (line 796), the finiteness of isospectral sets; (d) §1.1 or the paragraph after Thm 1.2.

**Novelty:** yes, for Thm 1.2(i): the surface case is classical and the orbifold case is a short corollary of Hejhal. Present it as a proposition with citations.

### 4.2 Hejhal, LNM 548 (1976), LNM 1001 (1983); Iwaniec, GSM 53 (2002), Thm 10.2; Buser (1992) ch. 9; Bergeron

**Hejhal Vol. I, structure (zbMATH review by J. Elstrodt, Zbl 0347.10018, fetched):** Chapter I (38 pp.) proves the trace formula "für Gruppen Γ ohne elliptische Elemente" and extends it "mit Hilfe eines naheliegenden Approximationsprozesses … auf eine umfassendere Klasse von Funktionen". Chapter III (29 pp., pp. 326–354 per Crossref) treats vector-valued functions with a unitary representation χ: "Hier werden erstmals auch Gruppen Γ mit kompaktem Quotienten zugelassen, welche elliptische Elemente enthalten." So **the elliptic case for cocompact Γ is Hejhal Vol. I, Chapter 3**, not Chapter 1.

**The theorem and its hypotheses (verbatim, via two independent secondaries):**
- Dryden arXiv:math/0411290, p. 7: "We can state this formula in terms of a function h(r) and its Fourier transform g(u), which are not required to have compact support; namely, h(r) satisfies the following (weaker) conditions: Assumption 4.2. • h(r) is an analytic function on \|Im(r)\| ≤ 1/2 + δ; • h(−r) = h(r); • \|h(r)\| ≤ M [1 + \|Re(r)\|]^{−2−δ}. The numbers δ and M are some positive constants. Hejhal [14] obtains the following version of the Selberg Trace Formula for the case of interest: Theorem 4.3. Suppose that • Γ ⊂ PSL(2,R) is a Fuchsian group with compact fundamental region; • h(r) satisfies Assumption 4.2; • {φn} is an orthonormal eigenfunction basis for L²(Γ\H). Then Σ h(r_n) = (µ(F)/4π)∫ r h(r) tanh(πr) dr + Σ_{R elliptic} (1/(2m(R) sin θ(R))) ∫ e^{−2θ(R)r}/(1+e^{−2πr}) h(r) dr + Σ_{P hyperbolic} (ln N(Pc)/(N(P)^{1/2} − N(P)^{−1/2})) g[ln N(P)], (2) where all the sums and integrals in sight are absolutely convergent." ([14] = Hejhal Vol. I.)
- Garbin–Jorgenson, Kodai Math. J. 43 (2020), p. 102: after (2.9), which is the trace formula with identity, hyperbolic and elliptic terms for compact M: "We note that (2.9) above agrees with the formula in Theorem 5.1 of [12], with χ being the trivial character of the group Γ." p. 99, Remark 2.6: "The literature on the Selberg trace formula (see for example [12] on page 351 or [23] on pages 100–102), often gives the following expression for the elliptic heat trace". [12] = Hejhal Vol. I, [23] = Kubota.

So the pinpoint is **Hejhal Vol. I, Ch. 3, Thm 5.1, p. 351, with χ trivial.** The hypothesis is the strip/decay class above. Primary text not reached (gap).

**Does $h_t(r)=e^{-t(1/4+r^2)}$ satisfy it?** Yes, trivially: it is entire and even, and on $\|\mathrm{Im}\,r\|\le\frac12+\delta$, $\|h_t(r)\|=e^{-t/4}e^{-t((\mathrm{Re}\,r)^2-(\mathrm{Im}\,r)^2)}\le e^{t(1/2+\delta)^2}e^{-t(\mathrm{Re}\,r)^2}$, which decays faster than any power. Dryden applies it to exactly this function (p. 8, proof of Thm 4.5): "Fix t > 0 and let h(r) = e^{−r²t}. Then h(r) satisfies Assumption 4.2". He obtains (3), p. 9, the heat trace formula with elliptic terms for compact orientable orbisurfaces. Note that Dryden follows "Hejhal's convention of nonpositive eigenvalues for this section" (p. 8), so the $e^{-t/4}$ factor appears in his (4), p. 9.

**Independent derivation for the heat kernel:** Garbin–Jorgenson, Remark 2.7, p. 101: "In the case M is compact, the standard trace STrK_M(t) is simply the trace of the heat kernel … (2.7) … give the geometric interpretation of the standard trace, namely (2.8) STrK_M(t) = (vol(M)/4π)∫ e^{−(r²+1/4)t} tanh(πr) r dr + Σ_{γ∈H(Γ)} Σ_n (ℓ_γ/sinh(nℓ_γ/2)) (e^{−t/4}/√(16πt)) e^{−(nℓ_γ)²/4t} + Σ_{γ∈E(Γ)} Σ_{n=1}^{q_γ−1} (e^{−t/4}/(2q_γ sin(nπ/q_γ))) ∫ e^{−2πnr/q_γ − tr²}/(1+e^{−2πr}) dr. The combination of (2.7) and (2.8) represent an instance of the Selberg trace formula as applied to the function f(r) = e^{−tr²}". Their Theorems 2.4 and 2.5 (p. 96) are stated for "a connected, hyperbolic Riemann surface of finite volume with p cusps and m elliptic fixed points". This is **exactly Thm 4.6 of the manuscript**, with the same normalization: $\ell/\sinh\cdot(16\pi t)^{-1/2}=\ell/(2\sinh)\cdot(4\pi t)^{-1/2}$, and the elliptic term is identical to $\mathrm E_m$. It is proved directly by periodizing the heat kernel, so no test-function class is needed.

**Iwaniec, Thm 10.2 and (1.63) (via secondaries; primary a gap).** Brumley–Lesesvre–Milićević arXiv:2105.02068v1, Appendix A, pp. 19–20: "We shall use the following class of test functions, taken from [16, (1.63)]. Definition A.1. A function h(ν) will be called admissible if it satisfies the following conditions: there is δ > 0 such that – it is even on R; – it extends analytically to the strip \|Im(ν)\| ⩽ 1/2 + δ; – it verifies h(ν) ≪ (1 + \|ν\|)^{−2−δ} in the strip". Then: "The following theorem is due to Selberg; see also [16, Theorem 10.2]. Proposition A.2 … J_ell(h) = Σ_{E_prim} Σ_{ℓ=1}^{m−1} (2m sin(πℓ/m))^{−1} ∫_R h(r) cosh(πr(1 − 2ℓ/m))/cosh(πr) dr". [16] = Iwaniec 2002. Petridis–Risager (appendix by N. Laaksonen), arXiv:1408.5743v3, appendix p. 24 of the PDF, quote the same elliptic term from "[3, Theorem 10.2]" = Iwaniec. Caveat: Iwaniec's Thm 10.2 is stated for finite-volume groups (cusps allowed). I could not verify whether his standing hypotheses include the cocompact case, so **cite Hejhal for the cocompact statement and Iwaniec only for the admissible class**, or as "see also".

**Buser ch. 9:** zbMATH review (Gilkey, Zbl 0770.53001): "Chapter 9 [deals] with closed geodesics and Huber's theorem. Chapter 10 deals with Wolpert's theorem." Kordyukov arXiv:2012.14190 cites "Huber's theorem [6, Theorem 9.2.9]" ([6] = Buser, 2010 reprint). Buser treats surfaces only, with no elliptic elements as far as the secondaries show. **Buser Lemma 6.6.4** is attested by Parlier, Hubard et al. and arXiv:2009.07538 ("Large genus asymptotics for lengths of separating closed geodesics on random surfaces", Remark after Lemma 27): "[Bus10, Lemma 6.6.4] … N ≤ ce^L".

**Bergeron** (zbMATH 1267.11001 / 1339.11061): ch. 5 develops the trace formula for finite-area surfaces (review). Not needed; do not cite.

**Decisions:**
- **Is Lemma 4.7 redundant? Yes.** Hejhal's class (Assumption 4.2) contains $h_t$ for cocompact groups with elliptic elements. The paper's Lemma 4.7 exists only because DS chose to state their eq. (1) for exponential type (a choice made for the wave distribution, not a limitation of the theorem). DS cite (1) itself to Hejhal and Iwaniec. Recommendation: delete Lemma 4.7, which also resolves G7-23's test-function item.
- **Is Thm 4.6 a direct citation? Yes:** [Hejhal 1976, Ch. 3, Thm 5.1, χ = 1] with $h=h_t$; see also [Garbin–Jorgenson 2020, Rem. 2.7, (2.8)] and [Dryden 2004, (3)]. Keep the displayed formula, because the paper needs its normalization. Keep "every term of Hyp is positive". Rewrite the proof as two sentences.
- **Is Lemma 4.8 standard? In method, yes:** it is Buser Lemma 6.6.4's area/packing argument, and the asymptotic count is Huber 1959 Satz 9 for surfaces. No fetched source states the orbifold version with the diameter constant $\frac{\pi}{A}e^{x+3\delta}$. Keep the lemma (it feeds the explicit constant of Thm 4.9(b)) and attribute the method to Buser.

**Relation to results.**
- Thm 1.2(i): immediate from Hejhal's formula plus positivity/decay of the hyperbolic term (this is the manuscript's own Remark 4.12, which becomes the main proof rather than "a consistency check").
- Thm 1.2(iii): the Hyp term in Hejhal's form is the whole content.
- Thms 1.1, 1.3, 1.4: none.

**Novelty change:** Remark 4.12 (lines 788–790) currently says the trace-formula proof "is a cross-check of the two computations, not an independent proof" because Lemma 4.7 used DGGW's leading term. Once Hejhal is cited, the trace-formula route is independent of DGGW: Hejhal's convergence does not use the DGGW expansion. It is then the classical proof, which strengthens G7-2's point that §4 is classical.

### 4.3 H. Huber, Math. Ann. 138 (1959) 1–26; II, Math. Ann. 142 (1961) 385–398

**Fetched:** GDZ scans (`pdf/huber1959.pdf`, `pdf/huber1961.pdf`), OCR in `txt/`. The PDF has one GDZ cover page, so printed page p = PDF page p+1.

**What it proves (verbatim, OCR with umlauts restored):**
- Setting, p. 1: "Es sei 𝔉 eine zweidimensionale, orientierbare und geschlossene analytische Riemannsche Mannigfaltigkeit mit konstanter Gaußscher Krümmung −1". That is, closed surfaces; the deck group has compact fundamental domain and no torsion. No elliptic elements.
- Length spectrum ⇔ spectrum, p. 8, §1.11: "Satz 7. Geschlossene hyperbolische Raumformen mit gleichem Längenspektrum besitzen auch gleiches Eigenwertspektrum und gleiches Geschlecht." … "Satz 8. Geschlossene Raumformen mit gleichem Eigenwertspektrum besitzen auch gleiches Längenspektrum und gleiches Geschlecht."
- Prime geodesic theorem, p. 10: "Satz 9. Es sei π_𝔉(t) die Anzahl aller primitiven Homotopieklassen der Länge ≤ t auf 𝔉. Dann gilt für t → +∞ [π_𝔉(t) ~ e^t/t]". The formula is OCR-garbled ("tg (t) ~ ett."); the reading e^t/t follows from (36) Φ(t) ~ e^t and the partial-integration step on p. 9–10. Satz 10: the count of all classes ~ e^t/t. p. 10: "Es mag zunächst überraschen, daß das asymptotische Verhalten von π_𝔉(t) und ω_𝔉(t) für alle geschlossenen Raumformen 𝔉 gleich ist."
- Huber II (1961), p. 385 (OCR): "Diese Arbeit ist eine Fortsetzung der im Band 138 … veröffentlichten Abhandlung [1] … Es sei 𝔉 eine orientierbare und geschlossene Riemannsche Mannigfaltigkeit der Dimension 2 mit konstanter Krümmung −1." It gives error terms governed by the small eigenvalues λ < 1/4 (Satz I, p. 386: "das asymptotische Verhalten … von den ‚kleinen' Eigenwerten λ < 1/4 bestimmt wird"). Still surfaces only.

**Relation to Dryden–Strohmaier:** DS (CMB p. 66; arXiv v2 p. 1): "For compact hyperbolic Riemann surfaces, Huber's theorem says that the Laplace spectrum determines the length spectrum and vice versa". DS Thm 1.1 is the orbisurface generalization, adding that the spectrum also determines the number of cone points of each order. Dryden (2004) Thm 4.5 is the earlier, weaker version ("up to finitely many possibilities").

**Relation to results:**
- Remark 4.13: the heat trace determines the spectrum and hence the length spectrum. Huber is the surface source.
- Prop. 4.4: countability of the length set.
- Lemma 4.8: Huber's Satz 9 is the asymptotic counterpart of the upper bound.
- Thm 1.2(iii): Huber's length/spectrum duality is the mechanism.
- Thm 1.1(i): Huber's Satz 8 includes "gleiches Geschlecht", so for surfaces the genus is a spectral invariant. Thm 1.1 extends that to orbifolds with a coefficient count; that extension stays new.

**Where to cite:** Remark 4.13 (line 793: "and with it the length spectrum [Huber 1959, Sätze 7–8] for surfaces, [DS Thm 1.1] for orbisurfaces"); before Lemma 4.8 (Satz 9); §1.1 sentence on DS.

**Novelty:** no change to the Thm 1.1/1.3/1.4 claims. It reinforces that Thm 1.2(iii) is classical in mechanism.

### 4.4 S. Wolpert, "The length spectra as moduli for compact Riemann surfaces", Ann. of Math. 109 (1979) 323–351

**Fetched:** records only (JSTOR, gap). **Statement via secondary**, Fanoni arXiv:2012.07344 p. 1: "Wolpert [Wol79] proved that generically the length spectrum determines the hyperbolic structure: if V_g denotes the subset of Teichmüller space of a closed surface of genus g ≥ 2 given by hyperbolic structures X such that there exists a hyperbolic structure Y isospectral (and non-isometric) to X, then V_g is a proper real analytic subvariety of Teichmüller space. In [Bus86], Buser showed that dim V_g > 0 if g = 5 or g ≥ 7." Buser's book devotes ch. 10 to "Wolpert's theorem" (zbMATH review).

**Relation to Thm 1.2(ii):** these are opposite sides of the same picture. Thm 1.2(ii) says no finite number of heat invariants determines the point of Teichmüller space. Wolpert says the full spectrum (equivalently, the length spectrum) determines a generic point, for surfaces. The manuscript's Remark 4.13 proves a much weaker orbifold statement: along a line in a Thurston coordinate, all but countably many points are spectrally distinguished. It should cite Wolpert as the stronger surface result and say whether the orbifold analogue is known. I found no orbifold analogue of Wolpert in the fetched literature; flag it as open or check Gordon's survey (gap).

**Where to cite:** Remark 4.13 (after line 795); optionally §8 Open problems ("orbifold version of Wolpert's generic determination").

**Novelty:** Thm 1.2(ii) is not threatened, since Wolpert concerns the full spectrum. But Remark 4.13's countability argument should be framed as a weak substitute for Wolpert.

### 4.5 C. Gordon, "Orbifolds and their spectra", in *Spectral Geometry*, Proc. Sympos. Pure Math. 84 (2012) 49–71

**Fetched:** zbMATH summary only. AMS returned 429, and there is no arXiv version (gap). zbMATH summary (Zbl 1326.58016): "This expository article is an expanded version of a minicourse presented at a workshop preceding the international conference on spectral geometry at Dartmouth College. After a self-contained presentation of the concepts of orbifolds, their singular sets, Riemannian structures, and orbibundles, the article discusses and partially surveys inverse spectral results for the Laplace operator on a compact Riemannian orbifold."

**What it is said to contain (unverified):** the existence of the heat trace expansion and a survey of inverse spectral results on orbifolds. Whether it poses an open question about hearing cone orders from finitely many heat invariants could not be checked. **CANNOT VERIFY.**

**Recommendation:** cite as a survey in §1.1, e.g. "for background on orbifold spectra see [Gordon 2012]". Do not attribute any specific statement or open question to it until someone reads it. No novelty change can be asserted.

### 4.6 E. Stanhope, Ann. Global Anal. Geom. 27 (2005) 355–375 (arXiv math/0301357); E. Dryden, arXiv math/0411290 (2004)

**Fetched:** both arXiv PDFs (`pdf/stanhope2005.pdf`, `pdf/dryden2004.pdf`).

**Stanhope, arXiv p. 1 (Main Theorems, restated with proofs in §6):** "Main Theorem 1: Let S be a collection of isospectral Riemannian orbifolds that share a uniform lower bound κ(n − 1) on Ricci curvature, where κ ∈ R. Then there are only finitely many possible isotropy types, up to isomorphism, for points in an orbifold in S. Main Theorem 2: Let isolS be a collection of isospectral Riemannian orbifolds with only isolated singularities, that share a uniform lower bound κ ∈ R on sectional curvature. Then there is an upper bound on the number of singular points in any orbifold, O, in isolS depending only on Spec(O) and κ." Method: a spectral diameter bound, Weyl's law and volume comparison, with no heat invariants beyond volume. Published page numbers are not checked (arXiv pagination).

**Dryden 2004:**
- p. 5: "Combining the Gauss-Bonnet theorem with Weyl's asymptotic formula, we see that for an orbisurface with given curvature, the spectrum determines the orbifold Euler characteristic. However, … it is not immediately clear that the spectrum determines the genus. This is still an open question." DS 2009 later settled this.
- p. 8, Thm 4.5: "If two compact orientable Riemann orbisurfaces are Laplace isospectral, then we can determine their length spectra and the orders of their cone points, up to finitely many possibilities."
- p. 10, Thm 5.1: "Let O be a compact orientable Riemann orbisurface of genus g ≥ 1. In the class of compact orientable hyperbolic orbifolds, there are only finitely many members which are isospectral to O." p. 10: "McKean [15] showed that only finitely many compact Riemann surfaces have a given spectrum. We extend this result to the setting of compact orientable Riemann orbisurfaces."
- p. 9 (proof of Thm 4.5): the systole is read from the $e^{-\omega^2/4t}$ decay (quoted in §1).

**Relation to Thm 1.1 (signature from $\lfloor A/\pi\rfloor+4$ coefficients; no uniform count):** Stanhope and Dryden give *finiteness* of the possible isotropy/cone data from the full spectrum, with bounds depending on the spectrum (through a diameter bound). Thm 1.1(i) gives *determination* from finitely many heat invariants, with a count depending only on area $=4\pi c_1$. No overlap in result, but they belong in the prior-work paragraph as the first "spectrum controls cone data" results. They predate DS and Doyle–Rossetti, which give exact determination.

**Relation to Thm 1.2:**
- (iii): Dryden's proof of Thm 4.5 is the qualitative version of Thm 4.10, as stated in §1. Cite it.
- Remark 4.13: Dryden Thm 5.1 gives finiteness of isospectral sets within the class, for genus ≥ 1. So "what the heat trace still misses" is, for each orbifold of genus ≥ 1, a finite set. For genus 0 Dryden's argument does not apply (p. 11: the extension of Prop. 5.3 needs a hyperbolic generator, "the fundamental group of a compact orientable Riemann orbisurface of genus g ≥ 1"). Whether it holds is not settled by any source I fetched; say so.

**Relation to Thms 1.3, 1.4:** none.

**Where to cite:** §1.1, first paragraph (line 169), Stanhope and Dryden before DS; Thm 4.9/4.10 lead-in (Dryden); Remark 4.13 (Dryden Thm 5.1 + McKean).

**Novelty change:** none for Thm 1.1. For Thms 4.9–4.10, Dryden (2004) is direct qualitative prior art for orbisurfaces and must be credited (see §1 bottom line, item 4).

### 4.7 Other works checked

- **Brooks–Gornet–Gustafson, Adv. Math. 138 (1998) 306–322.** zbMATH review (Nikčević): "for each natural number n > 2 and prime p, the number N(g) of mutually isospectral Riemann surfaces of genus g = 1 + (n − 1)p^{2n} is at least N(g) ≥ p^{n²−n}." *Relation:* only to Remark 4.13: isospectral non-isometric families within a fixed surface topology can be large. *Optional* cite next to Linowitz–Voight. No novelty effect.
- **Osgood–Phillips–Sarnak, J. Funct. Anal. 80 (1988) 212–234.** zbMATH review (Gilkey): compactness of isospectral sets of metrics on surfaces, using heat invariants and the determinant. Smooth metrics only, nothing on cone points or locality. **Not recommended.**
- **Parlier, Math. Ann. 370 (2018) 1759–1787** (arXiv:1611.02040 fetched). Abstract: "A quantitative answer is given to the following: how many questions do you need to ask a length spectrum to determine it completely?" *Relation:* a parallel "how many pieces of spectral data" question on the length side; also a modern source for Buser Lemma 6.6.4. *Optional* cite in §1 next to Kac.
- **Kokotov (polyhedral surfaces), King, Spreafico (cone determinants).** These concern flat cone points or general conical metrics and the zeta determinant. The heat coefficients at hyperbolic cone points of angle 2π/m are already covered by Donnelly and DGGW, which the paper cites. **Not directly relevant to locality or the expansion at cone points; not recommended.** Not fetched beyond an arXiv title check (arXiv:0906.0717).
- **Kubota, Elementary theory of Eisenstein series (1973), pp. 100–102**, is cited by Garbin–Jorgenson for the elliptic heat-trace term. It is an alternative classical source. Not fetched; no recommendation.

---

## 5. Concrete edit list for §4 (for the coordinator)

1. **Thm 4.6 proof (lines 692–695):** replace with a citation to Hejhal Vol. I, Ch. 3, Thm 5.1 (p. 351, χ = 1) plus the one-line check that $h_t$ is in the class; add "see also [Garbin–Jorgenson 2020, Rem. 2.7] and [Dryden 2004, (3)]". Keep the DS citation for the cone-point/elliptic-class correspondence (DS CMB p. 68).
2. **Delete Lemma 4.7 (lines 698–702)** and its uses. Remark 4.12 (lines 788–790): drop "Because Lemma 4.7 uses the leading term … not an independent proof". The trace-formula route is now independent of DGGW and is the classical (McKean-style) proof. Line 636 ("a consistency check rather than an independent proof") changes accordingly.
3. **Lemma 4.8:** add "cf. [Buser 1992, Lemma 6.6.4]" and "[Huber 1959, Satz 9]" for the asymptotics.
4. **Before Thm 4.9:** credit McKean 1972, Huber 1959 and Dryden 2004 (proof of Thm 4.5) for the mechanism. Present Thms 4.9–4.10 as making it quantitative (G7-2).
5. **Remark 4.13:** add Huber Sätze 7–8, Wolpert 1979, and McKean/Dryden finiteness (genus ≥ 1).
6. **§1.1:** add Stanhope 2005 and Dryden 2004 before DS, and Gordon 2012 as a survey. Restate Thm 1.2(i) as classical in substance (McKean for surfaces; Hejhal's formula for orbifolds; Uçar Thm 4.20 at K = −1, handled by another agent).
7. **Before submission,** have someone with library access check the primary pinpoints: Hejhal p. 351 Thm 5.1 and its hypothesis wording; Iwaniec (1.63) and whether Thm 10.2 covers cocompact Γ; Buser Lemma 6.6.4 (1992 numbering = 2010 reprint numbering?); McKean's heat expansion section.

## 6. Files fetched by this agent

- pdf/: huber1959.pdf, huber1961.pdf (GDZ scans), garbinjorgenson2020_kmj.pdf (Project Euclid OA), garbinjorgenson_heat.pdf / garbinjorgenson_spec.pdf (arXiv 1603.01495 / 1603.01494), dryden2004.pdf (math/0411290), stanhope2005.pdf (math/0301357), blm2021_arxiv.pdf (2105.02068), parlier2018_arxiv.pdf (1611.02040), fanoni2020_arxiv.pdf (2012.07344), linowitz2013_arxiv.pdf (1309.0499), hubard2025_arxiv.pdf (2504.00916), orbresolvent.pdf (2104.00895), fedosova_ruelle.pdf (2110.06683), jst_gl2.pdf (1212.4282).
- txt/: pdftotext of each, plus huber1959_ocr.txt and huber1961_ocr.txt (tesseract, English model).
- bib/: mckean1972(+_zb), mckean1974corr(+_zb), hejhal1976(+_zb), hejhal1983(+_zb), iwaniec2002(+_zb), buser1992 (zbMATH), buser2010reprint, huber1959(+_zb), huber1961, wolpert1979(+_zb), gordon2012orbifolds(+_zb), stanhope2005 (+ .arxiv.xml), dryden2004.arxiv.xml, dryden2004thesis, garbinjorgenson2020, bgg1998, ops1988, parlier2018, drydenstrohmaier2009_check.
