# Outstanding fetches

Sources that could not be retrieved, and identifiers that could not be resolved, during the
literature sweep. Each entry records everything known about the item so it can be chased
later. **Nothing here has been approximated, and no DOI anywhere in this review has been
constructed** — an identifier is either retrieved from an authoritative record (Crossref,
publisher page, arXiv API, institutional repository) or it appears below as unresolved.

Status values: `UNRETRIEVED` (the document itself could not be obtained), `NO-DOI`
(document obtained or adequately identified, but no DOI exists or none could be found),
`PAYWALLED`, `TOOLING` (retrievable in principle; one retrieval route failed and a
workaround succeeded).

---

## 1. Sources not retrieved

### 1.1 Watson, "The trace function expansion for spherical polygons" — `UNRETRIEVED`

- **Author:** S. Watson
- **Title:** The trace function expansion for spherical polygons
- **Journal:** New Zealand Journal of Mathematics **34** (2005), 81–95
- **Attempted URL:** `http://nzjm.math.auckland.ac.nz/images/0/0a/The_trace_function_expansion_for_spherical_polygons.pdf`
- **Failure:** connection timed out on every attempt; the server was unreachable from this
  network. No mirror located by web search.
- **Why it matters:** Watson is the $K=1$ predecessor of Uçar's constant-curvature cone
  coefficients. Schueth's Remark 5.4(ii) credits Watson with computing $c_\ell(\gamma)$ for
  every $\ell$ in the case $K=1$, and Uçar with extending this to arbitrary constant $K$.
- **Impact on the review's conclusions: none.** The load-bearing claim — that explicit
  constant-curvature cone coefficients exist for every $\ell$ — was verified firsthand from
  Uçar's thesis (equations (4.25) p. 134 and (4.33) p. 137, read in full) and independently
  cross-validated at $\ell=2$ against Schueth's Theorem 4.1. Watson would be a third,
  redundant confirmation restricted to $K=1$, which is not the manuscript's setting.
- **Action:** obtain via interlibrary loan or a NZJM mirror if the manuscript ends up citing
  Watson directly. It is not currently cited and does not need to be.

### 1.2 Takeuchi, "Commensurability classes of arithmetic triangle groups" — `UNRETRIEVED`

- **Author:** Kisao Takeuchi
- **Title:** Commensurability classes of arithmetic triangle groups
- **Journal:** J. Fac. Sci. Univ. Tokyo Sect. IA Math. **24** (1977), no. 1, 201–212
- **Failure:** the journal is not on J-STAGE (unlike Takeuchi's companion paper in
  J. Math. Soc. Japan), has no arXiv presence, and no accessible scan was located. Project
  Euclid hosts the J. Math. Soc. Japan paper but not this one.
- **Why it matters:** this is the paper that partitions Takeuchi's 85 arithmetic triples into
  their **19 commensurability classes**. It is the one place where $(2,8,8)$ and $(3,3,12)$
  might already appear side by side in print. Since equal $R$ means equal covolume by
  Gauss–Bonnet, and equal covolume is necessary (though far from sufficient) for
  commensurability, the question is live: if those two groups sit in the same class, the
  manuscript's minimal degeneracy may have an unremarked prior appearance in the
  Fuchsian-group literature.
- **What was established instead, from primary sources:** both $(2,8,8)$ and $(3,3,12)$ are
  confirmed arithmetic triangle groups. Verified twice over — directly from Takeuchi's
  Theorem 3 list in "Arithmetic triangle groups", J. Math. Soc. Japan **29** (1977), 91–106,
  DOI `10.2969/jmsj/02910091` (full PDF read via J-STAGE), and independently from the
  recomputed list of 76 compact 1-arithmetic triples in arXiv:1510.04637, which states it
  "agrees with that of Takeuchi, thus verifying his results". **Neither source assigns
  commensurability classes to individual triples.**
- **Caveat on how much this could change:** commensurable Fuchsian groups have covolumes in
  rational ratio, not generally equal. Equal covolume is therefore a sharper coincidence than
  commensurability and is not implied by it. So even a positive answer would not by itself
  make the manuscript's Theorem B prior art — but it would need to be cited and distinguished.
- **Action:** obtain via interlibrary loan or the University of Tokyo repository, and check
  the class assignment of $(2,8,8)$ and $(3,3,12)$. This is the single highest-value
  outstanding item in the review.

### 1.3 Guy, *Unsolved Problems in Number Theory* — **RESOLVED, not outstanding**

Retained here only to record how it was obtained. The subsection-level table of contents
(D1–D29 with page numbers) was recovered from the Deutsche Nationalbibliothek's deposited
front-matter PDF, and the body text of §D11 and §D16 cross-checked against a full-text
mirror. Publisher record: R. K. Guy, *Unsolved Problems in Number Theory*, 3rd ed., Problem
Books in Mathematics vol. 1, Springer, New York, 2004, xviii+438 pp.,
DOI `10.1007/978-0-387-26677-0`, hardcover ISBN 978-0-387-20860-2.

*Note on sourcing hygiene:* one of the full-text sources consulted appears to be an
unauthorized scan. It was used only to cross-check facts already established from the
publisher's own record and the national-library deposit, and nothing is cited to it. The
citable references are the Springer DOI and the DNB front matter.

---

## 2. Identifiers that do not exist or could not be resolved

These documents **were** obtained and are correctly identified; they simply have no DOI, or
none discoverable in Crossref. They are listed here rather than being given an invented
identifier.

| Work | Record | Status | Note |
|---|---|---|---|
| Bloom & Elsholtz, "Egyptian Fractions" | arXiv:2210.04496; written for *Nieuw Archief voor Wiskunde* | `NO-DOI` | Crossref returns no journal-version DOI. arXiv DOI `10.48550/arXiv.2210.04496` exists and may be cited instead. |
| Machacek, "Egyptian Fractions and Prime Power Divisors" | J. Integer Seq. **21** (2018), Art. 18.3.7 | `NO-DOI` | *Journal of Integer Sequences* does not register DOIs. arXiv:1706.01008. |
| Garces & Loyola, "Revisiting a Number-Theoretic Puzzle: The Census-Taker Problem" | *Intersection* **11** (2010), 28–38 | `NO-DOI` | Only the arXiv DOI `10.48550/arXiv.1204.2071` resolves. The journal is not in Crossref. |
| Kelly, "Partitions with equal products" | Proc. Amer. Math. Soc. **15** (1964), 987–990 | `NO-DOI` | Pre-dates DOI registration; not verified independently in this sweep. |
| Uçar, *Spectral invariants for polygons and orbisurfaces* | PhD thesis, Humboldt-Universität zu Berlin, 2017 | **RESOLVED** | Not outstanding — recorded here only to note that no *journal* version exists. The citable record is DOI `10.18452/18463`, URN `urn:nbn:de:kobv:11-110-18452`, handle `https://edoc.hu-berlin.de/handle/18452/19142`. |

---

## 3. Retrieval failures with successful workarounds

Recorded for completeness. **These are not unretrieved sources** — every document below was
obtained by another route, and its content is used in the review.

| Target | Failure | Workaround used |
|---|---|---|
| `arxiv.org/pdf/1705.01412` (Bari–Hunsicker) | automated text extraction returned unparsed binary; same on the `export.arxiv.org` mirror | downloaded the PDF directly and extracted the text (14,932 words) |
| `arxiv.org/pdf/1812.06119` (Schueth 2019) | same binary-extraction failure | ar5iv HTML full-text mirror |
| `arxiv.org/pdf/1711.03405` (Uçar thesis) | raw PDF bytes could not be parsed | Humboldt DSpace bitstream chain `/bitstream/handle/18452/19142/ucar.pdf` → `/bitstreams/.../download` → `/server/api/core/bitstreams/.../content`; 54,887 words recovered |
| Loughborough institutional repository (Bari–Hunsicker record) | JS-rendered pages return empty content on both the search page and the direct record | figshare REST API, `api.figshare.com/v2/articles/9385352` |
| DGGW erratum | not on arXiv | Wayback Machine copy of the Michigan Math. J. PDF (2 pages) |
| OEIS keyword search | HTTP 403 after several rapid unheadered requests | browser `User-Agent` plus ≥5 s spacing between calls |

**MathSciNet** was named in the task brief as a permitted venue but was not queried: it is
subscription-gated and no institutional access was available. Every citation in this review
was resolved without it, via Crossref, publisher pages, the arXiv API, and institutional
repositories.

---

## 4. Flagged discrepancies

### 4.1 Hezari–Zelditch — **RESOLVED, manuscript is correct**

The arXiv comment on arXiv:1907.03882 gives Ann. of Math. 197 (2023), no. 1. The official
Annals of Mathematics archive page reads *"Pages 1083–1134 from Volume 196 (2022), Issue 3"*,
DOI `10.4007/annals.2022.196.3.4`. **The arXiv comment is wrong; the manuscript's entry is
right.** No change needed.

### 4.2 Doyle–Rossetti 2008 — **RESOLVED, manuscript is correct**

The NYJM abstract page (nyjm.albany.edu/j/2008/14-7.html) gives *New York J. Math.* **14**
(2008), **193–204**, published 5 June 2008 — matching the manuscript. The "193-2004" seen on
the arXiv listing is an extraction artifact. Separately confirmed via Crossref that New York
J. Math. has **no DOIs registered at all** for this era, so the absence of a DOI in
`sources.bib` is correct rather than a gap.

### 4.3 Datchev–Hezari — **RESOLVED: year wrong, pages right**

The manuscript prints 2013. Both the MSRI/SLMath primary PDF header and Cambridge's own
Crossref record give **2012**. On pages, page-by-page inspection of the primary PDF confirms
**455–485**, matching the manuscript — Crossref's 455–486 is wrong. So: change the year, keep
the pages.

### 4.4 McKean–Singer — page range not primary-verified

Venue, volume, year and DOI (`10.4310/jdg/1214427880`) are primary-verified. The page range
**43–69** is corroborated only by a secondary index: Project Euclid, JSTOR and MathSciNet all
blocked automated access. The manuscript's range is almost certainly right, but it has not
been confirmed against the journal.

### 4.5 Schueth 2026 — title wording

arXiv abstract-page metadata reads "curved **conic** singularities"; the paper's own rendered
title and the SpringerLink published record both read "curved **conical** singularities". Cite
the "conical" form.

---

## 5. Resolved since first draft — retained for audit

| Item | Resolution |
|---|---|
| Annales de l'Institut Fourier DOI for Schueth 2019 | **`10.5802/aif.3338`** |
| Springer DOI for Schueth, Ann. Global Anal. Geom. **69** (2026) | **`10.1007/s10455-025-10024-1`** — open access, CC-BY 4.0; received 30 Sep 2025, accepted 27 Nov 2025, published 08 Dec 2025 |
| Guy UPINT §D11 / §D12 contents | Resolved — D11 Egyptian fractions p. 252, D12 Markoff numbers p. 263, and the genuinely relevant D16 at p. 271 |
| Nursultanov–Rowlett–Sher publication record | **Ann. Math. Québec 49, 1–61 (2025)**, DOI `10.1007/s40316-024-00237-4` |
| Doyle–Rossetti arXiv:1103.4372 publication status | **Never published.** No journal-ref on arXiv; Semantic Scholar lists no venue. The only citable identifier is the DataCite DOI `10.48550/arXiv.1103.4372`. |
| Looi–Sher arXiv:2512.04422 publication status | Still unpublished as of v6 (1 Jul 2026); only `10.48550/arXiv.2512.04422` |
| Suleymanova arXiv:1701.01874 publication status | Unpublished; no journal-ref |

---

## 6. Databases that could not be queried

- **MathSciNet** — subscription-gated, with no institutional access available. Named in the
  brief as a permitted venue; not used. Every citation was resolved without it.
- **Semantic Scholar API** — returned HTTP 429 on 12 consecutive attempts during the Q4
  searches (no API key available). The arXiv API and web search were substituted, and the
  substituted queries are listed in full in `review/hyperresearch/Q4-stability.md` §4 so the
  null result there rests on queries that were actually run.
