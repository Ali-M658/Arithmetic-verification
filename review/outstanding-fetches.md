# Outstanding fetches

Sources that could not be retrieved, and identifiers that could not be resolved, during the
literature sweep. Each entry records everything known about the item so it can be chased
later. **Nothing here has been approximated, and no DOI anywhere in this review has been
constructed** — an identifier is either retrieved from an authoritative record (Crossref,
publisher page, arXiv API, institutional repository) or it appears below as unresolved.

Status values: `ACCEPTED GAP` (not retrieved, assessed, and deliberately not chased; the list is the "Accepted gaps" table below), `UNRETRIEVED` (the document itself could not be obtained), `NO-DOI`
(document obtained or adequately identified, but no DOI exists or none could be found),
`PAYWALLED`, `TOOLING` (retrievable in principle; one retrieval route failed and a
workaround succeeded).

---

## Accepted gaps

These five sources were not retrieved, and the project has decided not to chase them. Each has been
assessed: none is load-bearing for a theorem or a number in the paper, and each is recorded so that a
referee's question about it has an answer. They are not open defects.

| # | Source | Status | Why it is accepted | Where |
|---|---|---|---|---|
| 1 | Steinig, Rend. Mat. (6) 4 (1971) 629–644 | `UNRETRIEVED` — **ACCEPTED GAP** | The paper proves its own injectivity theorem; Steinig can only be prior art for the positive-real case. | §1.9, §7 |
| 2 | Drury–Marshall, Math. Proc. Camb. Phil. Soc. 101 (1987) | `PAYWALLED` | Same: a more general setting of the Steinig argument; bears on novelty wording only. | §1.10, §7 |
| 3 | Donnelly, Math. Ann. 224 (1976) 161–170 | `PAYWALLED` | The locality and universality it supplies are quoted from DGGW §4.1–4.2 (read in full); Theorem 1 has two further proofs not using Donnelly. | §1.7 |
| 4 | Watson, New Zealand J. Math. 34 (2005) 81–95 | `UNRETRIEVED` | The K = 1 predecessor of Uçar; Uçar's thesis (read in full) reproduces and corrects it. The divergence novelty verdict is conditional on it. | §1.1 |
| 5 | Shioda, "On the Mordell-Weil lattices" (the Shioda–Tate rank formula source) | `UNRETRIEVED` | The remark that the pencil has no section of infinite order is not load-bearing; the ranks are certified by PARI (theory/diophantine/ranks.py). | §1.6 |

---

## 1. Sources not retrieved

### 1.1 Watson, "The trace function expansion for spherical polygons" — `UNRETRIEVED` — **ACCEPTED GAP**

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

**Second attempt** (the same item, logged again by the curvature/divergence session and merged here):

- Crossref `query.bibliographic=Watson trace function expansion spherical polygons` returned no
  matching record.
- `https://www.thebookshelf.auckland.ac.nz/docs/NZJMaths/nzjmaths034/nzjmaths034-02-004.pdf`
  returned no file (HTTP 000).
- The journal's site search
  (`https://nzjmath.org/index.php/NZJMATH/search/search?query=Watson+spherical+polygons`)
  returned HTTP 200 with no matching item.

**Instrument gap.** Watson's $K=1$ series is the one item that might already state a growth rate
for spherical corner coefficients. The novelty verdict in `theory/divergence/literature.md` §4
is therefore conditional on it. It rests on Uçar's thesis, which reproduces and corrects Watson
and makes no growth statement.

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
  the class assignment of $(2,8,8)$ and $(3,3,12)$.

> **UPDATE — the question this item was wanted for is now answered; the paper itself is still
> unretrieved.** See [takeuchi-verdict.md](takeuchi-verdict.md). The full class partition was
> recovered from a source that reproduces Takeuchi's table — **Tu & Yang, Trans. Amer. Math.
> Soc. 365 (2013), no. 12, 6697–6729, DOI `10.1090/S0002-9947-2013-05960-0`
> (arXiv:1112.1001), Appendix A** — whose eighteen cocompact subgroup diagrams were verified to
> partition Takeuchi's 76 compact triples exactly. **$(2,8,8)$ is in Class III, $(3,3,12)$ is in
> Class XV; they are not commensurable**, confirmed independently by an exact computation of the
> invariant trace fields ($\mathbb Q(\sqrt2)$, degree 2, versus $\mathbb Q(\sqrt2,\sqrt3)$,
> degree 4) from Takeuchi's own Theorem 1 criterion. This item stays open only to upgrade the
> class *numbering* from one source to two; its stake in the review's conclusions is now nil.

### 1.3 Maclachlan & Reid, *The Arithmetic of Hyperbolic 3-Manifolds*, §13.3 — `PAYWALLED`

- **Authors:** Colin Maclachlan and Alan W. Reid
- **Work:** *The Arithmetic of Hyperbolic 3-Manifolds*, Graduate Texts in Mathematics **219**,
  Springer, New York, 2003. ISBN 978-0-387-98386-8.
- **Section wanted:** §13.3, "Arithmetic Fuchsian Triangle Groups" (p. 418 per the published
  table of contents), as a second independent reproduction of Takeuchi's commensurability
  classes.
- **Failure:** Springer full text is subscription-gated and no institutional access was
  available; Google Books exposes the table of contents but not §13.3's body. No accessible
  scan located.
- **Impact on conclusions: none.** Tu–Yang (above) supplied a complete, independently verified
  reproduction. Maclachlan–Reid would be a redundant third confirmation of the class numbering.

### 1.4 Guy, *Unsolved Problems in Number Theory*, §D16 text — `UNRETRIEVED` in the Diophantine session (theory/diophantine)

- **Need:** the verbatim text of §D16, "Triples with the same sum and same product", p. 271, which
  `theory/diophantine/RECOMMENDATION.md` asks the paper to cite. The earlier cross-check (§R.2)
  relied on a mirror that cannot be cited.
- **Confirmed:** Crossref chapter record "Diophantine Equations", DOI `10.1007/978-0-387-26677-0_5`,
  pp. 209–310.
- **Tried:** `https://link.springer.com/chapter/10.1007/978-0-387-26677-0_5` (200, no D16 text);
  `https://link.springer.com/content/pdf/10.1007/978-0-387-26677-0_5.pdf` (paywall HTML);
  archive.org items `unsolvedproblems0003guyr` and `unsolvedproblems0000guyr` (access-restricted,
  `_djvu.txt` returned 401).
- **Impact:** low. The mathematical content attributed to D16 (Schinzel's theorem) was verified
  against Schinzel's paper itself, fetched from `http://www.math.bas.bg/serdica/1996/1996-587-588.pdf`.
  Schinzel cites D16 in Guy's **2nd** edition (1994). A quotation of Guy's wording still needs the book.

### 1.5 Verrill, "The L-series of certain rigid Calabi–Yau threefolds" — `UNRETRIEVED`

- **Bibliographic data (Crossref):** J. Number Theory **81** (2000), 310–334, DOI `10.1006/jnth.1999.2449`.
- **Tried:** ScienceDirect `/pdf`, `/pdfft` and md5 links (403); api.elsevier.com (400);
  pure.mpg.de (record, no file); CiteSeerX (404); no arXiv version found.
- **Why it matters:** `theory/diophantine/variety.md` §4 identifies the degeneracy threefold with
  Schoen's self-fibre product of Beauville's Γ₁(6) surface. The modularity statement is taken from
  Livné–Yui, arXiv math/0304497 (fetched), Theorem 2 and Table 1. That table attributes the result
  to Saito–Yui and to Verrill's appendix in Yui, Fields Inst. Commun. 38 (2001). The level (6) of
  the eta product η(q)²η(q²)²η(q³)²η(q⁶)² is an inference, not read from a source.
- **Impact:** none on any theorem; it affects only one descriptive sentence.

### 1.6 Shioda, "On the Mordell-Weil lattices" (the Shioda–Tate rank source) — `UNRETRIEVED` — **ACCEPTED GAP**

- **Record (zbMATH API, fetched):** Comment. Math. Univ. St. Pauli **39** (1990), no. 2, 211–240,
  Zbl 0725.14017; no DOI; the zbMATH record carries no full-text link.
- **Used for:** the remark in `theory/diophantine/variety.md` §2 that the pencil has no section of
  infinite order (rank = ρ − 2 − Σ(m_v − 1) = 0). The zbMATH review attributes Theorem 1.3,
  E(K) ≅ NS(S)/T, to the paper. The paper's own wording was not read.
- **Impact:** none on any proposed theorem. The remark is not load-bearing.

### 1.7 Donnelly, "Spectrum and the fixed point sets of isometries I" — `PAYWALLED` — **ACCEPTED GAP** (locality session, theory/locality)

- **Record:** Math. Ann. **224** (1976), 161–170, DOI `10.1007/BF01436198` (Crossref record
  retrieved; title, volume, pages and date 1976-04 agree with refs/sources.bib `donnelly1976`).
- **Attempted:** Unpaywall (`is_oa: false`, no OA location); `link.springer.com/content/pdf/...`
  (HTTP 200 but an HTML paywall page, not a PDF); EuDML and GDZ title searches (no hit).
- **Use made of it:** theory/locality/proof.md, Proof A of Theorem 1, needs the *locality* and
  *universality* of Donnelly's functions $b_k(\gamma,\cdot)$ and the factor $|\det B_\gamma|$. These
  are quoted from the restatement in DGGW §4.1–4.2 (arXiv:0805.3148, pp. 15–16), read in full.
  Donnelly's own wording was not checked.
- **Impact:** none on the conclusions. Theorem 1 has two further proofs that do not go through
  Donnelly: Uçar's Theorem 4.20 (explicit constant-curvature coefficients), and the trace-formula
  route (proof.md, Proof C). check_locality.py verifies their agreement exactly.

### 1.8 Hejhal, *The Selberg Trace Formula for PSL(2,R)*, LNM 548 / 1001, and Iwaniec, *Spectral Methods of Automorphic Forms* — `UNRETRIEVED` (locality session)

- **Why wanted:** Dryden–Strohmaier cite them ([7], [8]) for the orbisurface trace formula with
  elliptic terms, stated by DS only for test functions of uniform exponential type.
- **Not attempted beyond catalogue search:** both are books, not open access.
- **Workaround:** proof.md Lemma 3.2 extends DS eq. (1) to the heat test function by an explicit
  approximation argument. It follows Marklof, arXiv:math/0407288, Thm 4 and Prop. 10, which
  treat the torsion-free case and were fetched. The S3 data and the moduli experiment confirm the
  resulting formula numerically (numerics/moduli/REPORT.md).

### 1.9 Steinig, Rend. Mat. (6) 4 (1971) 629–644 — `UNRETRIEVED` — **ACCEPTED GAP**

Detail and the retrieval attempts are in the table of section 7. No DOI; zbMATH Zbl 0238.10007 gives metadata only.
Most likely classical source of the injectivity of power sums on positive reals; the paper proves Theorem A on its own
(theory/audibility/proof.md) and cites Steinig only as possible prior art.

### 1.10 Drury–Marshall, Math. Proc. Camb. Phil. Soc. **101** (1987), DOI `10.1017/s0305004100066901` — `PAYWALLED` — **ACCEPTED GAP**

Detail in the table of section 7 (abstract only; Unpaywall `is_oa` false). It is the Steinig-type argument "in a slightly
more general setting" (MathOverflow 410757); it bears on novelty, not on any proof in the paper.

### Retrieved after all (kept so the retrieval is not repeated; not outstanding)

#### R.1 Voight, *Quaternion Algebras* §32.5 — `RETRIEVED, DOES NOT CONTAIN THE MATERIAL`

Recorded because the pointer was wrong and the next reader should not repeat the retrieval.
John Voight, *Quaternion Algebras*, Graduate Texts in Mathematics **288**, Springer, 2021, is
freely available from the author at `https://jvoight.github.io/quat-book.pdf` and was
downloaded in full (883 pp.) and searched. **§32.5 is "Cyclic subgroups"** — cyclic subgroups
of quaternion unit groups $\mathrm P B^\times$, following Chinburg–Friedman — and has nothing
to do with triangle groups. The string "Takeuchi" appears on **zero** pages of the book;
"triangle group" appears on six, none carrying a commensurability-class table. The book is not
a source for this question.

#### R.2 Guy, *Unsolved Problems in Number Theory* — **RESOLVED, not outstanding**

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

#### R.3 Bremner–Guy, "Two more representation problems" — retrieved, **not** the relevant paper

Proc. Edinb. Math. Soc. 40 (1997) 1–17, DOI `10.1017/s0013091500023397`, fetched (open access).
It treats (x+y+z)³/xyz and x/y+y/z+z/x. The relevant paper is Bremner–Guy–Nowakowski,
Math. Comp. **61** (1993) 117–130, DOI `10.1090/s0025-5718-1993-1189516-5`, which was fetched
and read.

#### R.4 Mazur, "Modular curves and the Eisenstein ideal" — RETRIEVED (note on tooling)

Numdam `PMIHES_1977__47__33_0.pdf` (16,309,727 bytes) needed resumed downloads (`curl -C -`);
the first two attempts were truncated. Theorem (8) is on p. 35, and Theorem (5.1) with
Corollary (5.2) on p. 156. Crossref DOI `10.1007/bf02684339`.


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
| `library.msri.org/books/gt3m/PDF/13.pdf` (Thurston ch. 13) | host no longer resolves (curl status 000), also over https | SLMath mirror `library.slmath.org/books/gt3m/PDF/13.pdf` (8.4 MB, electronic ed. 1.1); route recorded in theory/locality/fetch_sources.sh |
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

---

## 7. Stability and prior-art sweep (2026-10-01): instrument gaps

Full tables, with URLs and errors, are in the "Instrument gaps" section of each note in
`review/literature/`. Nothing listed here is reported as "not found". Each item is a retrieval
failure.

| Item | Status | Attempted route and error | Why it matters |
|---|---|---|---|
| Semantic Scholar search API (anonymous) | `TOOLING` | HTTP 429 on every query in three independent sweeps, after the full 4 → 8 → 16 → 32 → 40 s backoff. The configured connector timed out. | No citation-graph traversal. Forward citations of Steinig 1971, Korobov–Bugaevskaya 2016 and Melánová–Sturmfels–Winter 2022 are where a statement of Theorem A could still be hiding. |
| arXiv full-text search | `TOOLING` | POST to `arxiv.org/search_classic` (`searchtype=ft`) returns 302 to `search.arxiv.org`. GET there works. Only the first 30 hits per query were parsed. | Full-text nulls cover arXiv only. |
| Steinig, Rend. Mat. (6) 4 (1971) 629–644 | `UNRETRIEVED` — **ACCEPTED GAP** | No DOI. zbMATH Zbl 0238.10007 gives metadata only. MathSciNet is not accessible. | Most likely classical source of injectivity of power sums on positive reals, possibly with real exponents. This would cover the positive-real case of Theorem A. |
| Drury–Marshall, Math. Proc. Camb. Phil. Soc. 101 (1987), DOI 10.1017/s0305004100066901 | `PAYWALLED` — **ACCEPTED GAP** | Abstract only; Unpaywall is_oa false. | The Steinig-type argument "in a slightly more general setting" (per MathOverflow 410757). |
| Müller et al., Found. Comput. Math. 16 (2016), arXiv:1311.5493 | `UNRETRIEVED` (identified, not fetched) | n/a | Real-exponent injectivity; cited by Melánová–Sturmfels–Winter Prop. 24. |
| Bhatia–Elsner–Krause, LAA 142 (1990) 195–209, DOI 10.1016/0024-3795(90)90267-g | `PAYWALLED` | ScienceDirect 403. Bielefeld repository behind a JavaScript challenge. Elsevier API 406. | The constant 4·2^{−1/n} is known only from secondary quotations, and one of them (Laffey) conflicts. Ostrowski 1940 was read from the primary and is the citation used. |
| Ostrowski, *Solution of Equations…* (1966/1973), Appendix A | `UNRETRIEVED` | Internet Archive lending-only (401). | The coefficient-γ form is secondary (Ćurgus–Mascioni). |
| Bhatia, *Matrix Analysis* Ch. VIII; *Perturbation Bounds* (SIAM) | `PAYWALLED` | Springer HTML paywall; not open access. | Textbook form of root/eigenvalue variation bounds. |
| Marletta–Weikard 2005; Mandache 2001 (IOP) | `TOOLING` | Bot-check redirect (Radware). | Marletta–Weikard: modulus of finite-data Sturm–Liouville stability not quoted (abstract only). |
| Hochstadt 1977; Alessandrini–Vessella 2005; Osgood–Phillips–Sarnak 1988 | `PAYWALLED` | ScienceDirect 403 / landing page only. | OPS compactness quoted via the Datchev–Hezari survey. Alessandrini–Vessella characterised through citing papers. |
| Savchuk–Shkalikov 2010; Hitrik 2000; McLaughlin 1988; Horváth–Kiss 2010; Ryabushko 1973 | `PAYWALLED` / `NO-DOI` | Not open access; Ryabushko has no Crossref record. | Sturm–Liouville finite-data stability lineage, known only through Bondarenko 2025's survey. |
