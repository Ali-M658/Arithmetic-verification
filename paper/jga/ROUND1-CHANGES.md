# ROUND1-CHANGES: response to referee round 1

Input: `review/referee-round-1/` (reports (a)-(e) and `VERDICT.md`) on the manuscript of commit
`8d07615`. Output: `manuscript.tex` (35 pages) and `supplement.tex` (15 pages), built with
`latexmk && latexmk` (see `BUILD.md`). Numbers below are those of the revised PDFs; "S" numbers are
in the supplement. Scripts and records for the computational items are in `review/round1-fixes/`.

## 1. The two disputed points (decided by computation or source)

| item | verdict | evidence |
|---|---|---|
| A1 Fig. 2 / $K_{\rm mult}$ (d-m1) | **No value changes.** For every one of the 525 area values the complete class (no bound on the orders; exact Egyptian-fraction enumeration) was enumerated anew: 33,946 signatures, largest order met 4,064,891,292; 504 classes contain orders above 12. Every class size and every largest $K_{\rm mult}$, $K_n$, $K_g$ equals `figures/data/f4_area_classes.csv` (histogram 17 / 311 / 197). The 525 values are exactly the $s\le7/5$ attained with genus $\le2$ (in effect $\le1$), at most four cone points and orders $\le12$. Caption rewritten to say so; F4 data and figure unchanged. | `review/round1-fixes/a1_fig2_kmult.py` (independent of `theory/` and `figures/`; coefficients from Bernoulli numbers and, separately, from the power sums $\Psi_k$, which agree on every pair); `output/a1_fig2_kmult.{txt,csv}` |
| A2 Lemma 3.3, sign of $d$ (b-m3, c-m3, d-m4) | **Correct as printed; no change.** The LaTeX source reads `d=R(m')-R(m)=2(g'-g)+n'-n`, which is what equal areas give. The reviewers read text extracted from the PDF, which drops the primes (reviewer (a) and `VERDICT.md` say the same). | `manuscript.tex`, Lemma 3.3 |

## 2. Items of the brief

| item | disposition | location |
|---|---|---|
| B1 abstract | fixed: about half the length; "first fail at sum 18" on $\mathcal O(2,8,8)$, $\mathcal O(3,3,12)$, "two suffice again at exactly 38 sums between 19 and 4800"; $n-1$ fail on integer orders for $n=3,4$ only; stability for spheres with known $n$, errors in heat invariants, constants depending on the true orders; growth "equivalent to the open question" | abstract |
| B2 Thm 1.3 scope | fixed: genus 0, known $n$, constants explicit functions of $m$; realisable exponent $\frac12$ only at a double order and when all $n\ge3$ orders are equal, "other configurations are open"; paragraph after the theorem: errors in heat invariants, a-posteriori use, no recovery procedure for unknown $(g,n)$ | Thm 1.3 and the paragraph after it; Remark 6.1 |
| B3 "first" claims | fixed: kept only the three supported by `review/literature-pass/NOVELTY.md` (uniform count; first failure of a fixed number of heat invariants on a family; stability for cone orders). "Part (ii) is new" replaced by "relocates the growth question rather than settling it"; "first sharp threshold" replaced by "no earlier result locates where ... first fails" | §1.1 |
| B4 Remark 4.7 | fixed by deletion (the option that saves space): the unproved "Thurston length coordinate" sentence is removed; the rest of the remark is sourced | Remark 4.7 |
| B5 Thm 4.4 | fixed: "The explicit constant is qualitative" ($e^{3\,\mathrm{diam}}$, admissible range ending where $e^{-\ell^2/4t}=e^{-(1+\ell)/2}$; only the exponent and $t^{-1/2}$ are sharp); also in the introduction | after Thm 4.4; §1 "What heat does not hear" |
| B6 "certified" | fixed: the numerics are "validated", never "certified"; the supplement says the eigenvalue errors are a-posteriori agreements, not enclosures, and that the double-window rerun has not been run (no comparison record exists in `numerics/data/`). "Certified" remains only for the exact-arithmetic certificate (Prop. S4.1, Table 1), which is a theorem about heat-invariant data | §7, Remark 6.1, S5 "Limitations", S6, Table S6 |
| B7 2-descent | fixed: the three cases $5\mid e$, $5\mid M$, $5\nmid Me$ (right side $\equiv d_1+d_1^{-1}+3M^2e^2\equiv\pm3$) are written out; PARI/GP `ellrank` confirmation cited | proof of Thm 5.10 |
| C1 Philippe | fixed from the fetched papers: AIF 2008 Thm A is for $(2,p,q)$ groups among such groups; the general $(r,p,q)$ result is Geom. Dedicata 149, read as Thm 3.1 of Sém. TSG 28 (added), whose proof compares the first two or three lengths | §1.1; `review/round1-fixes/citations/README.md` |
| C2 ADF(G), Richardson-Stanhope | fixed: Abreu-Dryden-Freitas-Godinho (the DOI record has four authors) cited as the closest precedent ($a_0,a_1,a_2$ of the Laplacian on functions and 1-forms determine the weights, Thm 1 and §6.1); Richardson-Stanhope Thm 4.7 cited for the scope (mirrors are heard) | §1 (definition of Sig), §1.1 |
| C3 citation details | Schueth AGAG: title "conical" and volume year 2026 are the publisher's (online 2025), no change; Schueth AIF: Tome 69 (2019), Crossref's 2020 is the online date, no change; Wooley: volume year 2019, no change; Chang-DeTurck: AMS gives pp. 1033-1038, no change; Uçar DOI resolves (DataCite) to edoc 18452/19142, no change. BGN: the paper now says they treat integer $\Lambda$, that their reciprocal-pair remark (p. 117) does not use integrality, and that $\Lambda=27/2$ is not theirs; "the table in §4" dropped | §1.1, §5.2; `citations/README.md` |
| D1 pencil counts | fixed: "pencil splitting" defined in Remark 3.2; recounted with all entries bounded: 17 witnesses (14 primitive) at 130, 49 (30 primitive) at 220, as reviewers (b), (c), (d) found. The old 15/35 matched no definition; the old 25/61 bounded only three entries of $A$ | Remark 3.2; S2; `review/round1-fixes/d1_pencil_counts.py` |
| D2 explicit pairs | fixed: Table S1 writes out the 18 diamonds (including Example 3.12(iii), $L=4..7$) and the 5 Prouhet squares (the latter for $L\ge4$ by closed form with digit counts; full lists in `output/d2_pairs.csv`), each with area and exact shared count, verified by script | Table S1; `review/round1-fixes/d2_explicit_pairs.py` |
| D3 Appendix B | fixed: precise methods and the programs and data for every search, the collision census, the figure data and the rank | Appendix B |
| E1 template leftovers | fixed: `lineno` removed; "1 1 Introduction" was the line number before the section number | preamble |
| E2 notation | fixed, see section 4 | |
| E3 Table 1 columns | fixed: Table 1 keeps $m,\delta_{\rm thm},\delta_{\rm cert},\delta_{\rm up}$; the full table (ratio, $\epsilon_{\rm cert}$, $\delta_{\rm cert}/|c_j|$) is Table S4, whose caption explains $\delta_{\rm cert}/|c_j|$ and proves $\epsilon_{\rm cert}\ge\min_j\delta_{\rm cert}/|c_j|$ (asserted in `tools/make_tables.py`) | Table 1, Table S4 |

## 3. Every referee item

Disposition: **fixed**, **moved** (to the supplement), **answered** (already in the paper, or no change needed after checking), **declined** (with reason).

### (a) inverse-spectral sceptic (major revision)

| id | issue | disposition | location |
|---|---|---|---|
| M1 | prefix measure non-canonical; "threshold 17" is a first failure; growth only reduced to PTE | fixed: abstract and §1.1 (B1, B3); §5 now says that prefixes are counted, why, and that on triangle orbifolds $c_2$ alone gives $(S_1,R)$ | abstract, §1.1, §5 opening |
| M2 | stability is an algebraic map, not a spectral statement | fixed (B2): scope stated in Thm 1.3, the paragraph after it and Remark 6.1; real orders declared formal at the start of §6. A bound from eigenvalue errors to $c_j$ errors is not attempted (declined: new analysis) | Thm 1.3, §6 |
| M3 | positioning, "first" claims, Philippe, missing classics | fixed for Philippe (C1), "first" claims (B3), ADFG and Richardson-Stanhope (C2). Brooks-Perry-Petersen, Zelditch, Hezari-Zelditch and Osgood-Phillips-Sarnak declined: they concern manifolds, wave invariants or compactness, not heat invariants of orbifolds, and adding them would need fetched statements and space; the classical surface context (Huber, McKean, Wolpert, Dryden, Stanhope, Linowitz-Voight) is cited | §1.1 |
| m1 | Remark 4.7 claim unproved | fixed (B4) | Remark 4.7 |
| m2 | "certified" numerics | fixed (B6) | §7, S5, S6 |
| m3 | data link owner; internal path in supplement | supplement paths are now explained as repository paths (Appendix B, S2). The URL is the repository's actual remote; who owns the account, and the Zenodo DOI, are for the authors at submission (declined here) | Appendix B, data statement |
| m4 | Prop. 5.9: is finiteness expected? | fixed: "We do not know whether only finitely many sums are collision-free." | Prop. 5.9 |
| m5 | Lemma 2.5 standard, adds length | moved: the admissibility lemma is Lemma S1.1; Thm 2.3 is cited from Dryden-Strohmaier, Hejhal, Garbin-Jorgenson and points to it | §2.1, S1 |
| m6 | "three positive real partners" | fixed: "a partner triple of positive reals" ($\{0.2664,4.2830,6.4506\}$, S2) | Remark 3.13, S2 |
| m7 | Fig. 2: exact $K$ only for $s\le7/5$ | fixed: caption says "beyond $s=7/5$ only bounds and constructed pairs are shown" | Fig. 2 |
| m8 | which way the evidence points on growth | answered: Example 3.12 ends with $f(A)\ge L+1$ already for $A/2\pi\ge2L-3$, $L\le5$; no further claim made | Ex. 3.12 |
| P1 | four subjects in 35 pages | partly: search logs, certificates, admissibility lemma and numerics details moved to the supplement; splitting the paper is an editorial decision for the authors (declined here) | |
| P2 | §6 notation heavy | declined (space); the renames of section 4 help | |
| P3 | Fig. 2 hard to read | caption clarified (A1); figure unchanged | Fig. 2 |
| P4 | say early that the problem reduces to power sums | answered: the paragraph after Thm 1.1 ("The mechanism is the same throughout...") | §1 |
| P5 | Lemma 3.3 correct | answered (A2) | |
| P6 | (praise) | none | |

### (b) trace-formula analyst (minor revision)

| id | issue | disposition | location |
|---|---|---|---|
| m1 | real orders have no geometric meaning | fixed: Thm 1.1(iii) "as functions of real orders (the cone coefficients are rational in the order)"; §6 opening: for real $m$ the $c_j$ are rational functions, heat invariants only for integer orders; Thm 1.3 "data that are the heat invariants of positive real orders" | Thm 1.1(iii), Thm 1.3, §6 |
| m2 | Philippe | fixed (C1) | §1.1 |
| m3 | sign in Lemma 3.3 | answered (A2) | |
| m4 | "certified"; spectral step not covered | fixed (B2, B6) | |
| m5 | a-priori version given $n$ and a bound on $\mu$ | declined: new mathematics; the a-posteriori logic is stated | Remark 6.1 |
| m6 | Fig. 2 caption | fixed (A1) | Fig. 2 |
| m7 | BGN at $\Lambda=27/2$ | fixed (C3) | §1.1, §5.2 |
| m8 | "three positive real partners" | fixed | Remark 3.13 |
| m9 | counting conventions 15/35, 107 | fixed (D1); 107 reproduced by three reviewers and in `review/audit-2/pte-witnesses/check_direct4.txt` | Remark 3.2, S2 |
| m10 | companion "in preparation"; repository owner | fixed: "no proof here depends on it"; owner declined as in (a) m3 | §1.1 |
| m11 | Dryden's finiteness "genus at least one" | answered: Thm 5.1 of the fetched arXiv text has the hypothesis $g\ge1$ | `citations/README.md` |
| P1 | notation clashes | fixed (section 4) | |
| P2 | lettered Theorems A-C | declined: renumbering would touch every cross-reference for no change of content; the roadmap gives the map | §1 roadmap |
| P3 | length; Remarks 3.2, 3.13 are search logs | fixed: moved to S2, one sentence each kept | Remarks 3.2, 3.13 |
| P4 | Thm 6.4(a), 6.8 legibility | answered: the typeset formulas are unambiguous; the garbling is in text extraction | |
| P5 | Fig. 2 points above 1.4 | fixed (as (a) m7) | |
| P6 | "1 1 Introduction", line numbers | fixed (E1) | |

### (c) PTE combinatorialist (minor revision)

| id | issue | disposition | location |
|---|---|---|---|
| m1 | framing of the PTE equivalence; $T_L$ | partly: abstract and §1.1 say the growth is equivalent to, not decided by, the open question; a separate paragraph on $T_L$ declined for space ($T_L$ and its Descartes bound are in §3.3) | abstract, §1.1 |
| m2 | stability scope | fixed (B2); a uniform-in-class corollary declined (new mathematics) | Thm 1.3 |
| m3 | sign in Lemma 3.3 | answered (A2) | |
| m4 | Philippe | fixed (C1) | |
| m5 | Thm 3.8 last sentence needs $g\ne g'$ | fixed: "if moreover $g\ne g'$ and ..." | Thm 3.8 |
| m6 | Fig. 2 cutoff; "configuration" undefined; abstract "$n\ge2$" | fixed (A1, D1); the abstract no longer states the exponent | Fig. 2, Remark 3.2 |
| m7 | threshold relative to triangles; sum 15 in Sig | fixed: abstract "Among triangle orbifolds"; §5 opening gives $(0;5,5,5)$ and $(0;2,2,2,10)$ | abstract, §5 |
| m8 | orientable, without reflectors | fixed: definition of Sig in §1 says cone points only, mirrors are heard (Richardson-Stanhope), non-orientable ones not considered | §1 |
| m9 | realisable vs general data | fixed (B2) | Thm 1.3 |
| m10 | loose citations (Chen Ex. 2.36, Croot-Mao-Yip, Wright/Melzak/BI) | fixed: Chen cited for (3.33) only (S2); Croot-Mao-Yip only for "$N(k)=k+1$ open, known for $k\le9$, 11"; Wright/Melzak/BI checked against originals in audit-2, no change | §3.3, S2 |
| m11 | search bounds and checksums in supplement | fixed: S2 and Appendix B give bounds, counts and programs; `DATA-MANIFEST.md` has the checksums | S2, Appendix B |
| P1 | length, five themes | as (a) P1 | |
| P2 | separate unconditional from equivalent-to-open in Thm 1.1 | answered: (ii) states the unconditional bounds and the equivalence separately | Thm 1.1 |
| P3 | notation collisions ($\mu$, $D$) | fixed (section 4) | |
| P4 | legibility of Thm 5.10 $\varphi$ and Thm 6.8 | answered as (b) P4 | |
| P5 | cryptic "joined across integer $S$"; "rounded so that it keeps its meaning" | fixed: Fig. 3 caption "defined only at integers $S$ and drawn as continuous bands"; Table 1 caption states the rounding directions | Fig. 3, Table 1 |
| P6 | display small $Z$ for $L=2,3$ | answered: Fig. 1 draws them; Table S1 lists the pairs | Fig. 1, Table S1 |
| P7 | (figures praised; state lower-bound values) | answered: the bounds are formulas in the caption | |

### (d) JGA rigour referee (minor revision)

| id | issue | disposition | location |
|---|---|---|---|
| m1 | Fig. 2: selection and competitor range | fixed (A1): competitors were always the complete class; caption states the selection rule | Fig. 2 |
| m2 | Remark 4.7 | fixed (B4) | |
| m3 | Philippe | fixed (C1) | |
| m4 | Lemma 3.3 sign | answered (A2) | |
| m5 | 2-descent missing case | fixed (B7) | Thm 5.10 |
| m6a | pencil counts | fixed (D1) | Remark 3.2 |
| m6b | explicit pairs of Ex. 3.12(iii) and Fig. 2 | fixed (D2) | Table S1 |
| m6c | Appendix B vague; deposit contents | fixed (D3); the 783 witnesses, search programs and Fig. 2/3 data are named | Appendix B |
| m7a | abstract "$n\ge2$" vs $k=n\ge3$ | fixed: Thm 1.3 says "all $n\ge3$"; the abstract no longer states it | Thm 1.3 |
| m7b | "$n-1$ never suffice" is formal | fixed (as (b) m1) | Thm 1.1(iii) |
| m7c | "threshold" | fixed (B1) | abstract |
| m8 | "certified" | fixed (B6) | |
| m9 | stability scope; no recovery for unknown $(g,n)$ | fixed (B2) | after Thm 1.3 |
| m10 | citation details; BGN | fixed or answered (C3) | |
| m11 | Thm 4.4 qualitative | fixed (B5) | after Thm 4.4 |
| P1 | move certificates, Table 1, §7 to the supplement | fixed: Prop. 6.9 is Prop. S4.1, full Table 1 is Table S4, §7 shortened; elliptic-curve proof kept in §5 (it proves Thm 1.2(iv)) | S4, §7 |
| P2 | overloaded notation | fixed (section 4) | |
| P3 | lettered theorems, long roadmap | declined as (b) P2 | |
| P4 | abstract nearly a page | fixed (B1) | |
| P5 | figures | Fig. 2 caption fixed; others unchanged | |
| P6 | line numbers, "1 1 Introduction" | fixed (E1) | |
| P7 | Table 1 last column | fixed (E3) | Table S4 |
| P8 | proof of Thm 3.11 to §3 | declined: page budget; Appendix A is self-contained | |

### (e) handling editor (desk-reject 25%; major revision expected)

| id | issue | disposition | location |
|---|---|---|---|
| M1 | stability weaker than advertised | fixed (B2): (b) option, restated with scope, a-posteriori nature, real orders formal; certificate machinery moved to S4; settling the realisable exponent declined (open, stated) | Thm 1.3, §6, S4 |
| M2 | §4 classical; Remark 4.7 unproved | fixed: Remark 4.7 claim deleted; §1.1 and §4 already present §4 as a quantitative version of a classical fact; the intro paragraph now says the constant is qualitative | §1, §4 |
| M3 | growth not answered | fixed: abstract "whether it grows linearly is equivalent to the open question ..."; §1.1 "relocates the growth question rather than settling it"; Problem 1 unchanged. No new inequality (declined) | abstract, §1.1 |
| m1 | real orders formal | fixed (as (b) m1) | |
| m2 | Prop. 5.9 computational | answered: titled "computational"; enumeration cited to the repository | Prop. 5.9 |
| m3 | descent table / database label | fixed: PARI/GP `ellrank` confirmation cited (`theory/diophantine/data/ranks.txt`); no LMFDB label given (not fetched) | Thm 5.10, Appendix B |
| m4 | Fig. 2 axis vs $s\le7/5$ | fixed (A1) | Fig. 2 |
| m5 | Lemma 2.5 dense | moved (as (a) m5) | S1 |
| m6 | orientable, cone points only | fixed (as (c) m8) | §1 |
| m7 | "sum 17" reads as the failure | fixed (B1) | abstract |
| m8 | "up to permutation" in Thm 1.2(ii) | answered: triads are written $p\le q\le r$ (Def. 2.1), so a pair is unordered by definition | |
| m9 | finiteness for fixed area is easy | declined: Thm 1.1(i) is about the explicit linear bound and the impossibility of a uniform one, which §1.1 states | |
| m10 | numerics wording | fixed (B6) and §7 shortened | §7 |
| m11 | companion "in preparation" | fixed: "no proof here depends on it" | §1.1 |
| m12 | normalisation reminder | answered: Thm 1.1(i) says the number "is read off from $c_1=\mathrm{Area}/4\pi$" | |
| P1 | split the paper | declined here (authors' decision); material moved to the supplement | |
| P2 | overlap with the companion note | answered: no proof depends on the note | §1.1 |
| P3 | Table 1 not checkable on paper | partly: Prop. S4.1 and Table S4 with the exact-arithmetic recipe; the code is in the repository | S4 |
| P4 | figures | as (d) P5 | |
| P5 | blind recovery label-blind only | answered: S6 "What was blinded: only the labels" | S6 |
| P6 | (style) | none | |

## 4. Renames (E2)

`theory/CONVENTIONS.md` is outside this round's write scope and is not updated; the new symbols occur nowhere else in the paper.

| was | now | where |
|---|---|---|
| $\mathcal P_n$ (spheres with $n$ cone points) | $\mathrm{Sig}_{0,n}\subset\mathrm{Sig}_0$ | §2, Thms A, C, 5.1, 5.6, Prop. 4.2, Cor. 4.3 |
| $\mathcal P$ (a comparison class) | $\mathcal C$ | Def. 2.2, §1, Cor. 4.3 |
| $D$ (diameter) | $\mathrm{diam}$ | §1, Lemmas 2.4, 2.5, Thm 4.4, S7 |
| $\mathfrak D_k$ (Hurwitz determinants) | $\mathrm{Hur}_k$ | §3, Thms A, B |
| $D_eG$, $D_m\mathcal I_n$, $D_me$ (Jacobians) | $\partial_eG$, $\partial_m\mathcal I_n$, $\partial_me$ | proof of Thm B |
| $D$ (local variable in an identity) | $x$ | §5.1 |
| $\mu_X(x)$, $\mu_m$, $\mu_{U^*}$ (multiplicities); $\mu_X,\mu_Y$ (multiplicities of 1) | $\mathrm{mult}_X(x)$ etc. | Thm A, Thm 3.4, Prop. 3.9, Thm 3.10, App. A |
| $\mu_n(a)$ (moments) | $\mathfrak m_n(a)$ | proof of Prop. 2.7 |
| $D(t)$ (trace difference) | unchanged: it is the axis label of Fig. 5 (`figures/src/F5.py`, outside the write scope); with the diameter renamed it no longer collides | §7 |
| $\mu=\max_im_i$ | unchanged (now its only meaning) | §6 |

## 5. Moved to the supplement

| material | was | now |
|---|---|---|
| admissibility of the heat function | Lemma 2.5 with proof | S1, Lemma S1.1 |
| search details of Remark 3.2 (pencil definition and counts, the 107 / 6 search, the six non-pencil witnesses, the $n=5$ search, Chen) | Remark 3.2 | S2 |
| search details of Remark 3.13 (cubic, filter, counts, the $\{1,1,1,1,7\}$ partner) | Remark 3.13 | S2 |
| explicit pairs of Ex. 3.12 and Fig. 2 | (not in the paper) | Table S1 |
| certificates for exact recovery | Prop. 6.9 with proof and the $n\le5$ series remark | S4, Prop. S4.1 |
| Table 1 columns ratio, $\epsilon_{\rm cert}$, $\delta_{\rm cert}/|c_j|$ | Table 1 | Table S4 |
| §7 error budget, Bolza benchmark, moduli details | §7 | S5, S7 (already there; §7 now points to them) |

## 6. Checks

- Build: `latexmk && latexmk`; manuscript **35 pages**, supplement 15; 0 LaTeX errors, 0 undefined references, 0 undefined citations, 0 overfull boxes (`BUILD.md`). Page 35 is about half full; two float-placement gaps (before §7 and §8) did not move with placement options, so 34 pages was not reached.
- PDF metadata: title, keywords and the six authors only.
- Independent check of every item from the two PDFs and the five reports: section 7.

## 7. Independent check and what followed

A separate agent, given only the two PDFs and the five reports, checked every item (90 rows):
63 resolved, 20 partly, 5 unresolved, 2 declined in the text, 9 new points. Every partly or
unresolved row is a presentation, length or scope request already marked "partly" or "declined"
in section 3, except two, now fixed. It confirmed on the rendered pages the sign of $d$, the 14/30
pencil counts, the $5\nmid Me$ case, the Fig. 2 caption (it recomputed the 525) and the
"validated" wording.

| checker point | disposition |
|---|---|
| (e) m9 finiteness at fixed area is easy, say so | fixed: §1.1 now says so (finitely many signatures per area; Theorem 3.4) |
| (b) m11 "genus at least one" | answered: Dryden's Thm 5.1 has that hypothesis (`review/round1-fixes/citations/README.md`); the checker could not see the source |
| new 1: repository paths name review rounds (`review/round1-fixes/...`) | declined: they are the files' real locations; renaming for the deposit is for the authors |
| new 2: repository owner | declined as (a) m3 |
| new 3: Philippe (r,p,q) claim to verify | answered: checked against the fetched TSG text (Théorème 3.1 and its proof) |
| new 4: "Problem 3" means the paper's and Borwein-Ingalls' | fixed: Thm 1.1(iii) now says "Problem 3 in Section 8"; the BI citations carry "[§6, Problem 3]" |
| new 5: Table S1 areas "≈" while the text says "less than" | fixed: areas within $10^{-9}$ of an integer are printed as an exact offset; Example 3.12(iii)'s areas are $5-3.3\cdot10^{-11}$, $7-3.4\cdot10^{-16}$, $10-4.3\cdot10^{-20}$, $18-5.7\cdot10^{-42}$, so "less than" holds |
| new 6: $n\ge2$ and $n=1$ statements are formal | answered: both are stated for real orders, declared formal in Thm 1.1(iii) and §6 |
| new 7: residual "threshold" headings | fixed: §5.1 "Strata and the first failure"; Thm 5.6 "Two invariants up to sum 17" |
| new 8: abrupt sentence before Thm 1.3; "None of this is new" | declined (style; no content issue) |
| new 9: bold mathematics in the abstract | declined: a feature of the journal template |

Final build after these fixes: manuscript 35 pages, supplement 15; 0 errors, undefined references,
undefined citations or overfull boxes.

## 8. Verification suite

`PYTHON=.venv/bin/python bash code/run_all.sh --quick`, first run: 54 passed, 2 failed, 9 skipped.
- `revision run_checks` (`check_fragments`) failed because a fragment in `theory/revision/` uses the
  macro `\Pill` this round removed; fixed by keeping `\Pill` as an unused alias in the manuscript
  preamble. The stage passes on rerun.
- `theory conventions-check` fails because the referee reports of `review/referee-round-1/`
  (committed before this round, at `a51912a`) contain symbols that `theory/conventions_check.py`
  requires to be free (`d_j`, `\varsigma`, ...). This round's files add none. The fix, adding
  `referee-round-1` to that script's skipped folders, is outside this round's write scope and is left
  to the authors.
All four new stages (`round1 ...`) pass.
