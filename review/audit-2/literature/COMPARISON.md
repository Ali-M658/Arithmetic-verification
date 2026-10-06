# G5-bis literature: comparison phase

Written after the blind REVIEW.md was frozen. Files read, as released:
- theory/pte/LITERATURE.md (167 lines)
- theory/pte/sources/NOTES.md (417 lines)
- theory/pte/proof.md (571 lines)
- theory/pte/statements.tex (132 lines)
- theory/pte/references-pte.bib
- the `borweiningalls1994` entry in review/literature-pass/references-additions.bib, which references-pte.bib points to.

Line numbers below refer to these files as read on 2026-10-06.

**Grade changes: none.** Three blind notes are amended without changing their grade (§4): S3, S2 and B2.

Every new metadata request in this phase (Crossref, arXiv) used the placeholder research@example.com.

## 1. Do the quotes in NOTES.md match the fetched text?

I compared every NOTES.md quote that bears on a bundle claim with my own reading: BI page images, Melzak text and images,
and the re-extracted arXiv texts. Hashes: NOTES' BLP copy (from daemonology.net) has the same SHA256 (f766f983...) as the
AMS publisher PDF I fetched, and NOTES' Melzak copy is identical to my cambridge.org fetch.

| NOTES.md location | claim | matches fetched text? | remark |
|---|---|---|---|
| §1 l.51-55 | B1, B3, definitions | yes, wording and pages (BI pp.4, 6, 7) | |
| §1 l.58-62 | B9, B4 | yes (Lemma 2 p.6; Prop. 3 p.6; "We may now choose s" p.7) | |
| §1 l.63-66 | B5 | **yes, verbatim** (BI p.7) | the quote is faithful; the problem is the content (§2.1) |
| §1 l.67-70 | B6 | yes | |
| §1 l.71-77 | B7 | yes (p.26), items 1-4, 7 and the closing paragraph | |
| §1 l.81-82 | B8 | yes (p.8) | |
| §1 l.87-117 | B10, B12 | yes: the p.9 table, the pp.9-10 paragraph, Prop. 4 (p.10), the five 7-sets (p.25) | |
| §1 l.120 | B11 | yes (p.4) | |
| §1 l.123-131 | BI references | yes. One nuance: NOTES marks these lines "[text, OCR]"; I read p.27 from the image and the wording agrees | |
| §2 l.140-148 | M1 | yes (pp.233-234) | NOTES itself records Wright's bound as "(n²+4)/2" here, which conflicts with §0 item 1 and §1 l.63 (§2.1) |
| §2 l.149-182 | M2, Table 1 | yes, all 28 rows | |
| §3 l.191-208 | W1, W2 | yes (arXiv v2 pp.52-53; arXiv v1 p.3) | |
| §4 l.218-222 | C1-C3 | yes (pp.1-2) | |
| §5 l.231-243 | D1-D3 | yes (pp.2-3) | |
| §6 l.263-285 | P1, P2 | yes (pp.2063, 2064, 2069) | NOTES quotes the Gloden formulas but not BLP's sentence that Gloden's solution has **four** parameters reduced to two (§2.6) |
| §7 l.297-301 | D4, S5 | yes (pp.11-13) | |
| §7 l.317-326 | S1 | yes (pp.198, 211, 218, 224), every number | |
| §7 l.333-344 | S3, S4 | yes: p.275 does carry the "33 distinct types" sentence (I had cited only its p.16 occurrence; see §4) | l.344 "(−1,1,3,5) does not appear in the table of contents. Absence from the list is all that is recorded here" is **accurate as worded**; LITERATURE.md overstates it (§2.2) |
| §8 l.360 | S2 | yes | |
| §9 l.377-378 | O1 | yes (Caley p.2) | NOTES omits Caley's next paragraph on the same page, which repeats BI's (k²−3)/2, (k²−4)/2 and attributes it to Melzak (§2.1) |
| §10 l.384 | O2 | yes | |

No misquotation was found; every quote I checked agrees in wording and page. The discrepancies are of
interpretation and selection, listed next.

## 2. Where NOTES.md / LITERATURE.md differ from my grades

### 2.1 The Wright/Melzak formula (B5/M1): SERIOUS, confirmed in comparison

- NOTES §0 l.18 says: "The refinement attributed to Wright 1935 [22] and Melzak 1961 [15]: `N(k) <= (1/2)(k^2-3)` for k odd
  and `(1/2)(k^2-4)` for k even."
- LITERATURE.md l.23-25 quotes this, and l.46 records, without comment, Melzak's "Wright's bound K(n) ≤ (n²+4)/2 as the
  best bound known so far".
- So the two retrieved sources disagree about Wright's bound, and this was not noticed. LITERATURE.md l.155 even lists
  Wright as "known via Borwein–Ingalls p. 7 and Melzak p. 234", as if the two agreed.
- My check (check_lifting_and_bounds.txt §2):
  - BI's formula is false for k = 2, 3.
  - It differs from Melzak's (k²+4)/2 by a constant (4 or 7/2), not by an index shift.
  - Melzak contains no closed-form bound of his own.
- **Grade unchanged: attribution "confirmed as quotation, content not supported"; severity SERIOUS (manuscript wording).**

### 2.2 Type (−1,1,3,5) "not tabulated" (S4)

- LITERATURE.md l.135-136: "**Our system is not tabulated.** Type $(-1,1,3,\dots,2L-3)$ for $L\ge4$ does not appear, and
  neither does the unequal-size version".
- The bold heading is correct.
- "does not appear" is contradicted: the survey treats (−1,1,3,5) in
  - Ex. 2.36 (p.70);
  - (3.33) (p.83);
  - (5.107) (p.120);
  - p.139.

  It treats (−1,1,3,5,7) in Ex. 2.38 and Ex. 5.17, and (−1,1,3,5,9) in (2.281).
- NOTES l.344 is correctly restricted to the table of contents.
- **Grade unchanged (CONTRADICTED as worded; CONFIRMED for "not tabulated").**
- In the manuscript fragments, proof.md and statements.tex do **not** contain the "does not appear" sentence (grep for
  "tabulated", "appear": no hit), so the defect is in LITERATURE.md only. If paper/main.tex carries it, it must be reworded
  as in REVIEW.md S4.

### 2.3 Section numbers (S3)

- LITERATURE.md l.128: "**Negative exponents** (survey §1.4 and Appendix A.5, ...)".
- §1.4 is "Multigrade Chains". The sentence is in §1.2.1, Example 1.7 (p.16), and again in the A.5 header (p.275).
- Replace "§1.4" by "§1.2.1 (Ex. 1.7)".

### 2.4 Proposition numbering (B2)

- LITERATURE.md l.21-22, proof.md l.113 and statements.tex l.27 all cite **Props. 2 and 3** for the two bounds, which is
  correct (BI p.6).
- No released file cites "Prop. 1" for a bound.
- The bundle's "Props. 1-3" therefore does not occur in these fragments (it may occur in paper/main.tex, which I have not seen).
- New finding: statements.tex l.26 cites `\cite[\S1]{borweiningalls1994}` for the definition of N(k). BI §1 (p.4) defines
  only "size" and "degree". N(k) is defined in **§2, p.6**.

### 2.5 Letac attribution (B10, P2)

- LITERATURE.md l.38-39, under the Borwein–Ingalls heading, lists "size 9: Letac's two 9-sets; size 10: Letac's solution".
  BI p.10 only says that three of the four were found "by Letac and Gloden (see [10])".
- LITERATURE.md l.82-84 and proof.md l.435 cite CMSV p.2 for the Letac attribution of the 9-sets, which is correct. The
  size-10 attribution needs BLP p.2069.
- MINOR. Fix: in LITERATURE.md l.38-39 add "(attribution: CMSV p. 2 for the 9-sets, BLP p. 2069 for size 10; BI p. 10
  says 'Letac and Gloden')".

### 2.6 Gloden family (P2)

- LITERATURE.md l.100: "**Gloden's two-parameter size-7 family** (BLP p. 2064, from Gloden ...)".
- BLP p.2064 says that Gloden's final solution "uses four parameters f, g, k, l", and that it "turns out to depend only on f
  and k" after BLP's computer-algebra simplification.
- MINOR. Write "Gloden's size-7 family in the two-parameter form of BLP p. 2064".
- LITERATURE.md l.101-103 mentions "a transcription slip (a dropped factor f in α3) caught by the exact check". The printed
  BLP α3 does contain the factor f, and my exact check (check_solutions.txt: identity in f, k for e = 1, 3, 5) agrees with
  the printed formula.

### 2.7 Other differences

- **B7 currency.**
  - NOTES l.19, LITERATURE.md l.31 and proof.md l.376 repeat BI's "No progress on questions 3 and 4 has been made for many
    years".
  - Problem 4 (M(k) = O(k²)) was settled by Wooley 2012, Thm 1.3. NOTES §0 item 2 and LITERATURE.md l.52-57 record that
    bound themselves but do not draw the consequence.
  - proof.md l.376 attaches the quote to Q3 only. That is acceptable but stale: write "(Borwein–Ingalls §6, Q3)" without the
    "No progress ... for many years" quote, or add "Q4 has since been settled by Wooley [Ann. Math. 2012, Thm 1.3]".
- **O4.** The sources never mention Sun–Zhao, arXiv:2307.11330 (claimed proof of Wright's conjecture, unrefereed).
  statements.tex l.27-28 ("No bound N(k)=o(k^2) is known") and l.97 ("the conjecture N(k)=k+1") are consistent with the
  refereed literature. An optional footnote is in §3.
- **Caley p.2** (O1) repeats the faulty formula as "due to Melzak". NOTES §9 records only the v(k) sentence.
- **Chernick pages.** LITERATURE.md l.104 gives 626–633. Crossref (DOI 10.1080/00029890.1937.11988045) confirms 626–633;
  BI's reference [4] prints 627–633 (BI's slip). No change needed.

## 3. Theorem sentences carrying a failed attribution, with replacements

| file:line | current text | defect | replacement |
|---|---|---|---|
| proof.md l.19-22 | "The best known bounds on $N(k)$ are quadratic: $\frac12k(k+1)+1$ by pigeonhole, and the slightly smaller $\frac12(k^2-3)$, $\frac12(k^2-4)$ of Wright and Melzak." | B5/M1: false for k = 2, 3; not in Melzak; conflicts with Melzak's report of Wright | "The best known bounds on $N(k)$ are quadratic: $\frac12k(k+1)+1$ by pigeonhole (Hardy–Wright; Borwein–Ingalls Prop. 3), and Wright's $(k^2+4)/2$ (1935, as reported by Melzak 1961, p. 234); Melzak also gives numerical bounds for $k\le29$ (Table 1)." |
| proof.md l.371-373 | "Borwein–Ingalls Prop. 3 gives $\frac12k(k+1)+1$, and the "slightly stronger" bounds of Wright and Melzak quoted there give $\frac12(k^2-3)$, $\frac12(k^2-4)$." | same | "Borwein–Ingalls Prop. 3 gives $\frac12k(k+1)+1$; Wright improved this to $(k^2+4)/2$ (as reported by Melzak, CMB 4 (1961), p. 234), and Melzak's Table 1 gives numerical bounds for $k\le29$. (Borwein–Ingalls p. 7 print $\frac12(k^2-3)$, $\frac12(k^2-4)$, which is false for $k=2,3$ and is not what Melzak reports.)" |
| proof.md l.376 | "(Borwein–Ingalls §6, Q3, "No progress … for many years")" | B7: the quote covers Q3 and Q4; Q4 is now solved | "(Borwein–Ingalls §6, Q3; still open according to Croot–Mao–Yip 2026, p. 1)" |
| statements.tex l.26 | `\cite[\S1]{borweiningalls1994}` | B1 place: N(k) is defined in §2, p.6 | `\cite[\S2, p.~6]{borweiningalls1994}` |
| statements.tex l.27-28 | "No bound $N(k)=o(k^2)$ is known, and this is listed as an open problem in \cite[\S6]{borweiningalls1994}." | correct; optional currency | "No bound $N(k)=o(k^2)$ is known; this is Problem~3 of \cite[\S6]{borweiningalls1994}, still open in \cite{crootmaoyip2026}." |
| statements.tex l.93 | "All known bounds on $N(k)$ are quadratic \cite[Prop.~3 and p.~7]{borweiningalls1994}" | the statement is true, but the cited p.7 carries the faulty formula | "All known bounds on $N(k)$ are quadratic \cite[Prop.~3]{borweiningalls1994}, \cite[p.~234 and Table~1]{melzak1961}" (melzak1961 is already in references-pte.bib but currently uncited in statements.tex) |
| statements.tex l.97-98 (optional) | "which is implied by the conjecture $N(k)=k+1$. Ideal solutions are known only for $k\le9$ and $k=11$ \cite{cmsv2024,crootmaoyip2026}." | O4: an unrefereed claimed proof exists | add the footnote: "A 2023 preprint (B.-N. Sun and Y. Zhao, arXiv:2307.11330) claims a proof of this conjecture via Kostant's strongly commuting rings; it is unrefereed and the later literature \cite{cmsv2024,crootmaoyip2026} treats the conjecture as open." |
| LITERATURE.md l.23-25, l.46, l.155 | Wright/Melzak formula; "known via BI p.7 and Melzak p.234" | B5/M1 | Replace l.23-25 by: "BI p. 7 quote $\frac12(k^2-3)$, $\frac12(k^2-4)$ for [22], [15]. This is false for $k=2,3$ and disagrees with Melzak p. 234, who reports Wright's bound as $(k^2+4)/2$; we use Melzak's." At l.155, note the disagreement |
| LITERATURE.md l.128 | "survey §1.4" | S3 | "survey §1.2.1 (Ex. 1.7, p. 16)" |
| LITERATURE.md l.135-136 | "does not appear" | S4 | "has no numerical solution listed (it is not among the 33 tabulated types of A.5, nor on eslpower kminus.htm), although the survey treats it in its identities ((2.275), (3.33)) and normalized bounds ((5.107))" |
| LITERATURE.md l.38-39, l.100 | Letac (under BI); "Gloden's two-parameter family" | B10, P2 | see §2.5 and §2.6 |
| NOTES.md l.18-19 | §0 item 1 | B5, B7 | same two corrections |

proof.md l.136 (Lemma 1.5(3), Chen A.1.6/17/26/33), l.181 (Chen's lifting), l.186 (BI p.8), l.259 (A.685), l.403-406,
l.416 and l.434-447 (witness provenance) all carry correct attributions.

## 4. Amendments to blind notes (no grade change)

- **S3.** The "33 distinct types" sentence occurs twice: p.16 (§1.2.1, Ex. 1.7) and p.275 (A.5 header). My blind note gave
  only p.16. LITERATURE.md's "Appendix A.5" is therefore right; only "§1.4" is wrong. Grade stays CONFIRMED WITH CORRECTION.
- **S2.** In the blind review I flagged that Theorem 3's lift can be trivial. proof.md l.175-179 states Prop. 2.2 as
  $[Z]=_{2L-2}[-Z]$ for an L-configuration Z, and its proof notes "$Z\ne-Z$ because $Z$ has no pair $\{z,-z\}$ and is
  nonempty". The configuration's definition (no ±pair) excludes the degenerate case, so **no defect in Prop. 2.2**.
  - Remark: Prop. 2.2 is the special case A = Z, B = −Z, T = 0 of Theorem 3, or more directly the definition of an odd
    symmetric solution (BI p.8).
  - "Chen's lifting" (l.181) is an acceptable attribution, though stronger than needed.
- **B2.** In the released fragments the cited proposition numbers are correct (Props. 2, 3). The MINOR stands only for any
  "Props. 1-3" citation elsewhere (e.g. main.tex).

## 5. references-pte.bib against Crossref / arXiv metadata

Raw responses: search/cr_*.json.

| key | checked against | result |
|---|---|---|
| melzak1961 | Crossref 10.4153/CMB-1961-025-1: "A Note on the Tarry-Escott Problem", Z.A. Melzak, Canadian Mathematical Bulletin 4(3) 233-237, Sept 1961 | **matches** |
| blp2003 | Crossref 10.1090/S0025-5718-02-01504-1: Borwein, Lisoněk, Percival, Math. Comp. 72(244) 2063-2070, online 18 Dec 2002 | **matches** (year 2003 = issue year, correct) |
| cmsv2024 | Crossref 10.1090/mcom/3917: Coppersmith, Mossinghoff, Scheinerman, VanderKam, Math. Comp. 93(349) 2473-2501 (online 6 Nov 2023); arXiv 2304.11254 same authors and title | authors, journal, volume, number, pages match. **DOI missing: add `doi = {10.1090/mcom/3917}`** |
| chen2025survey | arXiv 2506.11429v1: "A survey of The Prouhet-Tarry-Escott Problem and its Generalizations", author "Chen Shuwen" | matches (family name Chen, given name Shuwen; "Chen, S." correct). Title case differs trivially |
| wooley2019 | Crossref 10.1112/plms.12204: PLMS 118(4) 942-1016 (online 25 Oct 2018); arXiv 1708.01220v2 lists the same DOI | matches. **DOI missing: add `doi = {10.1112/plms.12204}`**. Key wooley2019 is not cited in statements.tex |
| crootmaoyip2026 | arXiv 2609.05061v1: Ernie Croot, Junzhe Mao, Chi Hoi Yip, same title | **matches** |
| borweiningalls1994 (references-additions.bib l.315-322) | no Crossref record (L'Enseignement Math. 1994 has no Crossref DOI); fetched scan head: "L'Enseignement Mathématique, t. 40 (1994), p. 3-27", authors Peter Borwein and Colin Ingalls | matches (journal, volume, pages, year); zbl number not checked |
| (missing) wooley2012 | Crossref 10.4007/annals.2012.175.3.12: Ann. of Math. 175(3) 1575-1627 | needed only if the Q4 remark (§2.7) is added; LITERATURE.md cites it without a bib entry |
| (missing) Hardy–Wright | | needed if the pigeonhole bound is credited to Hardy–Wright as Melzak does (REVIEW B4) |

## 6. Summary

- **Quotes:** NOTES.md's quotes match the fetched texts in wording and page throughout; no misquotation found.
- **Failed attributions carried into theorem text:**
  1. The Wright/Melzak formula (B5/M1, SERIOUS): proof.md l.19-22 and l.371-373; statements.tex l.93 cites the page carrying
     it. LITERATURE.md l.23-25 and NOTES l.18 are internally inconsistent with their own Melzak quote (LITERATURE.md l.46,
     NOTES l.141).
  2. N(k) defined in BI §2, not §1 (statements.tex l.26, MINOR, new).
  3. BI's stale "no progress on 3 and 4" (proof.md l.376, MINOR).
- **LITERATURE.md only:**
  - "does not appear" (S4);
  - "§1.4" (S3);
  - "Letac's" under BI (B10);
  - "Gloden's two-parameter family" (P2).
- **Bibliography:** cmsv2024 and wooley2019 lack their DOIs. Other entries match Crossref and arXiv.
- **Grade changes:** none. Notes amended: S3, S2 (resolved, no defect in Prop. 2.2), B2 (moot in these fragments).
