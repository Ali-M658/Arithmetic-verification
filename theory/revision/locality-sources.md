# Locality sources: classical literature check

Retrieval date 2026-10-05. Cache: `theory/revision/sources_cache/`. All downloads by headless `curl` with a desktop Safari user agent. Text extraction: pymupdf.

The GDZ scans (Huber) have no text layer. Two OCR texts are cached for each: GDZ's own OCR (`*_gdzocr.txt`, from `https://gdz.sub.uni-goettingen.de/fulltext/PPN235181684_<vol>/<physpage>?_format=xml`) and a local tesseract OCR at 200 dpi (`*_tesseract.txt`). Both garble formulas, so every Huber quotation below was checked against the page image rendered from the cached PDF and transcribed from it. These are marked **[scan]**. Page numbers are journal page numbers:

- Huber 1959: journal p. = PDF p. − 1.
- Huber II: journal p. = PDF p. + 383.
- Huber Nachtrag: journal p. = PDF p. + 461.

Internet Archive lending books (Buser) were reached only through the IA full-text search API, `https://archive.org/services/search/beta/page_production/?service_backend=fts&user_query=identifier:<id> "<phrase>"`. This API returns short OCR highlight snippets, never pages. The raw JSON responses are in `sources_cache/ia_fts/`. `buser_w.json` was reused and holds only the last query. Snippets from the overwritten runs are kept verbatim in the run logs `ia_fts/log_batch*.txt`. Snippets are quoted exactly as returned, OCR errors included, with the `{{{ }}}` hit markers removed. They carry no page numbers unless the snippet text contains one. Each quoted snippet names its `ia_fts/` file.

---

## 1. Hejhal, The Selberg Trace Formula for PSL(2,R), Vol. 1, LNM 548 (1976)

**Fetched (partial access only):** the Springer "page-one" previews, which contain the first 2 pages of each chapter.

| file | URL | bytes | sha256 |
|---|---|---|---|
| hejhal_preview_BFb0079609.pdf (Ch. 1, pp. 1–38) | https://page-one.springer.com/pdf/preview/10.1007/BFb0079609 | 1170223 | f2e1660aa3ff0c04af4c58703aeb5e89569aff5d374efdb66a45e14a16015640 |
| hejhal_preview_BFb0079610.pdf (Ch. 2, pp. 39–325) | …/BFb0079610 | 267712 | 66305ccc8562f11e6240bacfc5f65703dbfc9198075d4c746795b8b895a14104 |
| hejhal_preview_BFb0079611.pdf (Ch. 3, pp. 326–354) | …/BFb0079611 | 223954 | f699cae394c9fd4750f94f167a86a0dc19c079d97063430ecb3adb252a6b5574 |
| hejhal_preview_BFb0079612.pdf (Ch. 4, pp. 355–461) | …/BFb0079612 | 220609 | f4f5ee2421db487e7d7aafebec7f7c530bc66fb5e9c56618a6a89a50d4c805f5 |
| hejhal_preview_BFb0079613.pdf (Ch. 5, pp. 462–499) | …/BFb0079613 | 285931 | 68ace590dc20886c2df5938570c344d8ac9e0aefaf7fb8fea125f2e23213e1e0 |
| zbmath/hejhal1.json (zbMATH review Zbl 0347.10018, J. Elstrodt) | https://api.zbmath.org/v1/document/_search?search_string=an%3A0347.10018 | — | 851acd359ab4c9d6623168beacfdae69268f4ab0d4261d1d844139673ee310ef |

Chapter DOIs and page ranges come from Crossref (`api.crossref.org/works/10.1007/bfb00796NN`).

**Instrument gap (full text):**
- `https://link.springer.com/content/pdf/10.1007/BFb00796{09..12}.pdf` returned HTTP 200 with a 3038-byte HTML paywall page, not a PDF.
- IA advancedsearch `creator:(hejhal)`, `creator:(Hejhal, Dennis)` and `title:(selberg trace formula for PSL)` returned 0 items.
- IA full-text search for Hejhal phrases (`ia_fts/probe_hejhal*.json`, `iw_4.json`) returned no hit inside the book itself.
- The Duke 1976 survey (doi 10.1215/S0012-7094-76-04338-6) on Project Euclid returned the bot-check page "Pardon Our Interruption" (200, 6183 bytes). Semantic Scholar reports it `"status": "CLOSED"`.

The interior of Ch. 3, including the p. 351 statement, was therefore **not seen**. Neither the elliptic term, the hypotheses on h, nor any heat-kernel application could be verified.

**Quotations obtained:**
- Ch. 1 preview, p. 1 (hejhal_preview_BFb0079609.txt, PDF p. 1). The OCR layer is lossy and is copied as is: "We want to give a rigorous development of the Selberg trace formula for a com- pact Riemann surface of genus g = 2 . … We can therefore represent F as a quotient space ~ \ H , where is a strictly hyperbolic Fuchsian group". The "=" is the OCR rendering of the scan's "≥" sign.
- Ch. 2 preview, p. 39 (BFb0079610.txt, PDF p. 1): "develop some non-trlvlal applications of the Selberg trace formula [theorem 7.5 in chapter i]."
- Ch. 3 preview, p. 326 (BFb0079611.txt, PDF p. 1): "Our goal in chapter 3 is to rigorously derive the trace formula which corresponds to vector-valued functions u: H > C r such that: u(Tz) = ~(T)u(z) … The only serious difficulty occurs in developing the necessary L2( ~ \ H,~) spectral theory. Once this is done, the procedure is entirely similar to that of chapter i."
- zbMATH review Zbl 0347.10018 (zbmath/hejhal1.json). This is a secondary source:
  - On Ch. I: "Im kurzen Kap. I (38 S.) wird die Selbergsche Spurformel bewiesen für Kerne, die zu Punktpaarinvarianten gebildet sind (Gewicht 0, Charakter 1), und für Gruppen \(\Gamma\) ohne elliptische Elemente."
  - On Ch. III: "Im kurzen Kap. III (29 S.) wird die Spurformel für vektorwertige Funktionen \(u: H\to \mathbb C^r\) … hergeleitet; … Hier werden erstmals auch Gruppen \(\Gamma\) mit kompaktem Quotienten zugelassen, welche elliptische Elemente enthalten."
  - On Ch. II, counting functions studied with Z(s): "Anzahl der Konjugationsklassen \(\{P\}\) hyperbolischer Elemente von \(\Gamma\) mit Norm \(N\{P\}\leq T\); Anzahl der Konjugationsklassen \(\{P_0\}\) primitiver hyperbolischer Elemente … für \(T\to\infty\) einer genauen Analyse unterzogen."

## 2. Iwaniec, Spectral Methods of Automorphic Forms, AMS GSM 53 (2002) / Rev. Mat. Iberoam. 1995

**Instrument gap:**
- `https://www.ams.org/books/gsm/053/gsm053-endmatter.pdf` and `…/gsm053-frontmatter.pdf` returned HTTP 429 (5717 and 5723 bytes HTML) on two attempts.
- `https://www.ams.org/books/gsm/053/` returned 200, but the page is a JS product-data page with no chapter text.
- `https://bookstore.ams.org/gsm-53` returned 200 and is JS-rendered, with no PDF or sample links in the HTML.
- `https://www.ams.org/bookpages/gsm-53` returned 404.
- IA advancedsearch `title:(spectral methods) AND creator:(iwaniec)` and `title:(introduction to the spectral theory of automorphic forms)` returned 0 items.
- IA full-text search for `"Spectral Methods of Automorphic Forms" "Theorem 10.2"` returned no hit inside the book (`ia_fts/iw_1..3.json`; two queries returned a null hits object).

Theorem 10.2 was **not seen**.

**Secondary only:** zbMATH review of the 1st edition, Zbl 0847.11028 (zbmath/iwaniec1995.json, sha256 0c716f7cea1e2b8af6ece028508ab61290b423472b5d28fb1b655f0d03b65cd6): "Central theorems in the spectral theory of automorphic forms are the trace formula of Selberg and the sum formula of Kuznetsov. … The former formula is used to prove a distribution result on the length of closed geodesics." The 2002 review, Zbl 1006.11024 (zbmath/iwaniec.json), says: "The text of this new edition agrees with that of the first edition up to a few minor revisions".

## 3. McKean, CPAM 25 (1972) 225–246, and Correction, CPAM 27 (1974) 134

The DOIs 10.1002/cpa.3160250302 and 10.1002/cpa.3160270109 come from Crossref. Zbl 0225.30021 and Zbl 0317.30018 have no review text (zbmath/mckean.json).

**Instrument gap:**
- `https://onlinelibrary.wiley.com/doi/{pdf,epdf,abs}/10.1002/cpa.3160250302` returned HTTP 403 (about 5.8 kB HTML) for all three.
- Semantic Scholar reports `"isOpenAccess": false, "status": "CLOSED"`.
- Unpaywall returned 422 because it requires a real email, which was not supplied.
- IA advancedsearch `creator:(mckean) AND title:(selberg)` returned 0 items. IA holds only `sim_communications-on-pure-and-applied-mathematics_1972_25_index`, the index, not the issues.

McKean's own text was **not seen**. The only indirect evidence is Buser's use of McKean's method (§5 below).

## 4. Huber, Math. Ann. 138 (1959) 1–26; II: Math. Ann. 142 (1961) 385–398; Nachtrag: Math. Ann. 143 (1961) 463–464

**Fetched (GDZ, open access):**

| file | URL | bytes | sha256 |
|---|---|---|---|
| huber1959.pdf | https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0138/LOG_0007.pdf | 2483446 | c13fc2969b1006013d9b38d1d310e5fd80763424fa4236bfb693aa3b4ccd6634 |
| huber1961_II.pdf | https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0142/LOG_0046.pdf | 1101985 | 01682c201e1476cedecd7b66cce56a76b92720d016eb7ca9f04bf99bd529eba4 |
| huber1961_II_nachtrag.pdf | https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0143/LOG_0077.pdf | 258650 | 5a4938f912ac1703c4e190094aaa0bec134d7fff20a1329a0e7b5b93f968078e |

The LOG ids come from the METS files `https://gdz.sub.uni-goettingen.de/mets/PPN235181684_{0138,0142,0143}.xml`. The OCR texts are `huber*_gdzocr.txt` and `huber*_tesseract.txt`.

**Setting (no elliptic elements), 1959 p. 2 [scan]:** "Weil 𝔉 geschlossen ist, ist natürlich μ(𝔚) > 0 für 𝔚 ≠ 𝔒. Daher ist μ(T) > 0 für alle T ∈ Λ − E. Die einzigen Bewegungen von 𝔖 mit positiver Verschiebungslänge sind aber die hyperbolischen Translationen³). Somit ist Λ eine diskontinuierliche Translationsgruppe."

The surface is set up on p. 1 [scan]: "Es sei 𝔉 eine zweidimensionale, orientierbare und geschlossene analytische Riemannsche Mannigfaltigkeit mit konstanter Gaußscher Krümmung − 1".

**Method (no heat kernel):** Huber works with the Dirichlet series G_𝔉(p,q;s) = Σ_{T∈Λ} Cos^{−s} ρ(Tp,q), its eigenfunction expansion, and the Wiener–Ikehara Tauberian theorem (p. 5). The terms "Wärme", "heat" and exp(−…t) occur in none of the six OCR files. Huber II p. 388, footnote 4 [scan]: "Diese Relation könnte auch aus der allgemeinen Spurformel von A. SELBERG ([4], (3.2) pag. 74) hergeleitet werden."

**Lattice-point count, 1959 p. 5, Satz 3 [scan]:** "Es sei N(p, q, t) die Anzahl der Elemente der Menge {T | T ∈ Λ, ρ(Tp, q) ≦ t}. Dann gilt für t → +∞ N(p, q, t) ∼ (1/(4(g_𝔉 − 1))) e^t."

**Spectrum ⇔ length spectrum, 1959 p. 8 [scan]:**
- "Satz 7. Geschlossene hyperbolische Raumformen mit gleichem Längenspektrum besitzen auch gleiches Eigenwertspektrum und gleiches Geschlecht."
- "Satz 8. Geschlossene Raumformen mit gleichem Eigenwertspektrum besitzen auch gleiches Längenspektrum und gleiches Geschlecht."

**Geodesic counting, 1959 p. 10 [scan]:**
- "Satz 9. Es sei π_𝔉(t) die Anzahl aller primitiven Homotopieklassen der Länge ≦ t auf 𝔉. Dann gilt für t → +∞ π_𝔉(t) ∼ e^t/t."
- "Satz 10. Es sei ω_𝔉(t) die Anzahl aller Homotopieklassen der Länge ≦ t auf 𝔉. Dann gilt für t → +∞ ω_𝔉(t) ∼ e^t/t."
- The comment that follows: "Es mag zunächst überraschen, daß das asymptotische Verhalten von π_𝔉(t) und ω_𝔉(t) für alle geschlossenen Raumformen 𝔉 gleich ist."

**Error terms, II p. 386 [scan]:**
- "Satz III: Es sei α_λ = 1/2 + (1/4 − λ)^{1/2}, also 1 > α_λ > 5/6 für 0 < λ < 5/36. Dann gilt für t → +∞ ψ(t) = e^t + Σ_{0<λ<5/36} m(λ) α_λ^{−1} e^{α_λ t} + O(e^{5t/6})."
- "Satz IV: Für t → +∞ gilt π(t) = Li(e^t) + Σ_{0<λ<5/36} m(λ) Li(e^{α_λ t}) + O(e^{5t/6}/t)."

Here ψ(t) = Σ_{0<μ(𝔚)≤t} μ(𝔚)/ν(𝔚) (II p. 385, (1)).

**Sharpened error terms, Nachtrag p. 464 [scan]:**
- "(10) ψ(t) = e^t + Σ_{0<λ<3/16} m(λ) α_λ^{−1} e^{α_λ t} + O(t^{1/2} e^{3t/4}), α_λ = 1/2 + (1/4 − λ)^{1/2},"
- "(11) π(t) = Li(e^t) + Σ_{0<λ<3/16} m(λ) Li(e^{α_λ t}) + O(t^{−1/2} e^{3t/4})."

All of these O-constants are implicit and depend on the surface. No explicit constant appears.

## 5. Buser, Geometry and Spectra of Compact Riemann Surfaces (Birkhäuser 1992)

**Partial access:** IA item `geometryspectrao0000buse`, which is lending-restricted (`access-restricted-item: true`).
- `https://archive.org/download/geometryspectrao0000buse/geometryspectrao0000buse_djvu.txt` returned 403 (4868 bytes).
- `https://ia800709.us.archive.org/fulltext/inside.php?item_id=geometryspectrao0000buse&…&q=geodesics` returned 403. The ia600709 mirror also returned 403.
- The IA FTS snippet API worked. Its results are in the files cited below.

**Table of contents (ia_fts/buser_q2.json, buser_q3.json):**
- "Chapter 9 Closed Geodesics and Huber’s Theorem 224 9.1 The Origin of the Length Spectrum"
- "7.4 The Heat Kernel of the Hyperbolic Plane 197 7.5 The Heat Kernel of r\H 205"
- ia_fts/buser_q6.json: "Number Theorem 241 9.5 Selberg's Trace Formula 252 9.6 The Prime Number Theorem with Error"

**Counting lemma, statement (two overlapping snippets).** The "<" signs are as OCR'd and may be "≤" in print:
- ia_fts/buser_b3_2.json: "surface of genus g > 2 and let L> 0. There are at most {g- 1) exp (L + 6) oriented closed"
- ia_fts/buser_q7.json: "geodesics of length <L on S which are not iterates of closed geodesics of length < 2 arcsinh"
- ia_fts/log_batch1.txt (query `"Let S be a compact Riemann surface of genus g" "closed geodesics" "at most"`): "There are at most {g- 1) exp (L + 6) oriented closed geodesics of length <L on S which"
- Lemma number, from a forward reference (ia_fts/buser_q2.json): "of the number of closed geodesics of length £< L will follow in Lemma 6.6.4, and an asymptotic". No snippet joins the number "6.6.4" to the statement text, but the forward reference points there.
- From the proof (ia_fts/buser_b3_2.json): "Comparison of the areas now shows that there are at most cosh(L + 3r) - 1 < cL+3r coshr- 1". The OCR fraction is garbled.

**Heat kernel → trace formula → Huber (McKean's method):**
- ia_fts/buser_b2_1.json and buser_b2_2.json: "this proves the trace formula. O Following McKean [1], we plug the heat kernel pM of M into the trace formula"
- ia_fts/buser_b3_1.json: "plug the heat kernel pM of M into the trace formula to prove Huber's theorem. We first"
- ia_fts/log_batch2.txt (query `"McKean" "heat"`): "theorem by looking at the heat kernel. This argument follows McKean [1], We take advantage"
- ia_fts/buser_b3_3.json:
  - "is called the primitive length spectrum of M. Huber's theorem [2] is as follows. 9.2.9."
  - "Huber's theorem can also be stated for the primitive length spectrum"
  - "same length spectrum if and only if they have the same primitive length spectrum."
- Genus is a spectral invariant (ia_fts/buser_b2_4.json): "However, isospectral compact Riemann surfaces have the same genus."

**Not reached in Buser:** any snippet stating that the small-t heat expansion depends only on genus/area, or that the difference is O(e^{−c/t}). The queries "heat trace", "small t", "t -> 0", "depend(s) only on the genus" and "asymptotic expansion" returned either no hit or unrelated hits ("depends only on the genus" hits concern Bers' constant and Ch. 13 bounds). This is an instrument gap: the snippet API returns only the top 5 highlights per query.

## 6. Wolpert

**Fetched:** wolpert_bams1977.pdf from `https://www.ams.org/journals/bull/1977-83-06/S0002-9904-1977-14425-X/S0002-9904-1977-14425-X.pdf` (HTTP 200, 263817 bytes, sha256 43c6dcc6eb0d181c47b59cfcc85462908b6460a4ff2f92b986ae14bcdbae9781). The text layer is in wolpert_bams1977.txt.

- p. 1306: "By the technique of the Selberg trace formula the sequences determine each other [5], [8]." Reference [5] is McKean CPAM 1972.
- p. 1306: "THEOREM 1. The total number of Riemann surfaces with a given length spectrum is finite." This is introduced by "The following theorem of H. P. McKean to our knowledge implies all prior results, [5]. A new proof is given."
- The announcement contains no statement about heat invariants. Annals 109 (1979), doi 10.2307/1971114, is on JSTOR and was not attempted beyond the Crossref lookup. Instrument gap.

---

## Answers (strictly from the quotations above)

**(a) Trace formula with elliptic terms, for a class of h containing e^{−t(1/4+r²)}.**
- Hejhal Vol. 1: only the zbMATH review attests that Ch. III (pp. 326–354) is the first place groups with elliptic elements are admitted. Ch. I (Theorem 7.5) is explicitly for strictly hyperbolic Γ. The Ch. III statement itself, its elliptic term, its hypotheses on h, and any heat-kernel application were **not seen**. Theorem number, page and wording remain unverified.
- Iwaniec Theorem 10.2: **not seen**.
- No retrieved primary text states the elliptic-term trace formula.

**(b) "Same signature ⇒ same heat expansion to all orders, difference governed by e^{−l²/4t}".** No retrieved text states this.
- Huber 1959 and 1961 do not use the heat kernel. They treat only closed orientable surfaces, so Λ is a "Translationsgruppe" with no elliptic elements. They prove spectrum ⇔ length spectrum (+ genus), Satz 7–8.
- Buser attests that the heat kernel is plugged into the trace formula "Following McKean [1]" to prove Huber's theorem, for compact Riemann surfaces.
- McKean's paper itself was not reached.
- Nothing retrieved addresses orbifolds or elliptic elements in this context.

**(c) Classical geodesic-counting bound with an explicit constant.**
- Buser (Lemma 6.6.4 per the forward reference) gives "at most (g − 1) exp(L + 6) oriented closed geodesics of length ≤ L" (OCR "<") that are not iterates of closed geodesics of length < 2 arcsinh 1. The constant is explicit and depends only on genus, i.e. area via area = 4π(g − 1). It needs no diameter or injectivity-radius hypothesis because geodesics shorter than 2 arcsinh 1 (and their iterates) are excluded.
- Huber gives only asymptotics (π(t) ∼ e^t/t) and implicit O-terms (O(t^{−1/2}e^{3t/4}) in the Nachtrag), with no explicit constant.
- No retrieved source gives a bound in terms of area and diameter, or area and systole, for orbifolds.
