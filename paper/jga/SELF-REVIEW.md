# SELF-REVIEW: independent check of the 30-35 page revision

A separate reviewer was given only the two compiled PDFs (`manuscript.pdf`, 35 pp., and
`supplement.pdf`, 8 pp., read through PyMuPDF text extraction, not the LaTeX source) and three
checklists: `review/referee-sim/G7-VERDICT.md`, `review/audit-2/VERDICT.md` and
`review/literature-pass/NOVELTY.md`. It was asked to give a disposition for every G7 item, every
audit-2 required change and every NOVELTY.md sentence block, and to list anything else wrong.

## What it recomputed (no disagreement with the PDFs)

alpha_0..alpha_4; p_0..p_3, the closed form of Phi_m and the leading coefficient of Lemma 2.9;
d_3, d_4, d_5; amp_0..amp_4, zeta_3..zeta_5; every entry of the delta_cert/abs(c_j) column of
Table 1 and every ratio (6.72; 3.9e-3 for (2,3,7) at c_2); sech^2 U for (2,2,2,2,3); the whole
descent (psi maps E into C_{27/2}, phi o psi = id, the twelve points, the flex at (16,400),
#E(F_7) = #E(F_11) = 12, d' = 3^2 5^6, every residue step); the values of Theorem 5.4; Tables S3
and S4; the 38 collision-free sums to S = 600 and the first non-adjacent collision; the areas and
invariants of Examples 3.6, 3.12 and Theorem C(3); Table S2 against the exact c_1, c_2, c_3. It
confirmed that the removed text is absent ("previously smallest ... 14/5", "pencil phenomenon",
"(k^2-3)/2", "answers the question left open", "both rates are sharp", PARI, "as far as tested",
3P, Conjecture 8.10, Table 5) and that there is no "??".

## Findings and what was done

| # | finding | resolution |
|---|---|---|
| 1 | Placeholders (Zenodo DOI twice, author contributions, AI-use statement) remain | Intended: the brief requires them to stay marked. Listed in OUTSTANDING.md section 2. |
| 2 | G7-14: repository account not explained | Not fixable in the paper (Declarations unchanged by instruction); OUTSTANDING.md section 4. |
| 3 | "Corresponding author(s). E-mail(s):" on p. 1 | Printed by the sn-jnl class; title page unchanged by instruction; noted in OUTSTANDING.md section 7. |
| 4 | Three novelty sentences beyond NOVELTY.md | Section 1.1 locality paragraph now uses NOVELTY 4's "We record three consequences ..." verbatim; Section 4 says "We make this explicit" instead of "What is new here". "Part (ii) is new" is kept: the brief asks for the PTE equivalence to be presented as new. |
| 5 | Example 3.12(ii): the doubling of [1,5,5] = [2,3,6] gives 8 and 9 cone points; the printed 7 vs 8 pair has the common order 6 cancelled | Fixed: "... after cancelling the common order 6" (checked by hand: U = {1,4,4,5,5,6,6,12,12}, V = {2,2,2,3,6,10,10,10,10}). |
| 6 | Iwaniec named without a reference; Buser not cited (G7-2) | Fixed: both cited (Theorem 2.3 proof; after Lemma 2.4). The reviewer saw an earlier PDF in which these were missing. |
| 7 | P_0 (genus-0 class) clashes with P_n at n = 0 | Fixed: the genus-0 class is Sig_0 throughout. |
| 8 | "d_5 by (9), (7)": (7) has no p_3 | Fixed: "by Proposition 2.8". |
| 9 | "Wooley (2012)" without an entry | Fixed: "settled by Wooley; his bound ... [Wooley 2019, Thm 13.1]". |
| 10 | Chen survey author printed as "Shuwen, C." | Fixed in `tools/build_bib.py` ("Chen, Shuwen", with a justification comment and an assertion on the name tokens). |
| 11 | Supplement: hyperbolic-term magnitudes 3.4e-31 / 5e-19 not mutually consistent | Replaced by the safe statement "below 10^{-30} on the fit window" (the reviewer's own estimate is 7.3e-31). |
| 12 | Tail rule: "+10" in the supplement, not in the paper | Fixed: Section 7 now says "plus twice the largest observed excess plus 10". |
| 13 | Run-in "What heat does not hear." on the same line as the previous paragraph | Fixed: new paragraph. |
| 14 | Section 3.3 "large enough to be hyperbolic (one condition)" cryptic; smaller genus not specified | Fixed: "the smaller genus being the least that makes its side hyperbolic (the other side then has the same positive area)". |
| 15 | Theorem 6.4: "eta = max(...) <= 1" reads as part of the definition | Fixed: "and assume eta <= 1". |
| 16 | Theorem C(1) lacks the Borwein-Ingalls "odd symmetric" citation | Fixed: "(an odd symmetric system in the sense of [BI, s. 3])". |
| 17 | f_n should say it is maximised over genus-0 orbifolds | Fixed. |
| 18 | "pillows" undefined in Fig. S1 caption | Fixed in `figures/captions.tex` ("orbifolds"); in the paper the word occurs only inside the DGGW quotation, now glossed. |
| 19 | Letac: BLP p. 2069 and Gloden missing | Not changed: the audit (H6, B10) says BLP does not name Letac for the 9-sets; CMSV p. 2 is the correct source for them, and Gloden is not mentioned. |
| 20 | F3 caption says dark/light, markers are coloured | Not changed: captions name tones by design so that they hold in greyscale print (figures/SPEC.md, rule for the pillow hues). |
| 21 | G7-11: software versions and quadrature order not printed | Versions: the supplement now says they are pinned in the repository's requirements files. Quadrature order: not stated (not in the numerics report). |
| 22 | G7-31: other overloaded symbols (T, D, E, varrho) | Partly: D = S - p removed earlier; the remaining uses are local and disambiguated; no notation table (page limit). |
| 23 | 0.53 vs 0.52 standard-error ratio for d_4 | The printed 0.53 uses the unrounded fit value (0.5265, `numerics/data/headline.json`); kept. |

## After the fixes

Rebuilt with `latexmk`: manuscript 35 pages, supplement 8 pages, 0 errors, 0 undefined references
or citations, 0 overfull boxes (BUILD.md). To stay within 35 pages after the fixes, the short
divergence remark (old Remark 2.12) and the second Philippe reference were removed, and three
bibliography entries were shortened (no URL for Thurston's notes, no arXiv note for Ucar's thesis,
no data note on Strohmaier-Uski; the text cites the arXiv ancillary data directly).
