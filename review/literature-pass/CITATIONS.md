# Citation verification: every `\cite` in `paper/jga/manuscript.tex`

Manuscript state: commit 57a4ecd, 1584 lines; 94 `\cite` commands, i.e. **97 key-instances** of 41 keys.
Each cited work was fetched and the cited location was read. Verbatim quotes, printed and PDF pages, and
the URLs tried are in the three working reports. This file is the consolidated verdict table.

- `work/A-spectral-citations.md`: DGGW (+ erratum), Uçar, Dryden–Strohmaier, Doyle–Rossetti, Schueth, ADFG,
  Donnelly, McKean–Singer, Kac, Marklof (50 instances)
- `work/B-geometry-numerics-citations.md`: Thurston, Troyanov, Linowitz–Voight, Bari–Hunsicker, Sunada, GWW,
  SSW, RSW, Grieser–Maronna, Gómez-Serrano–Orriols, Berndt–Yeap, Allouche–Shallit, Holtz–Tyaglov,
  Strohmaier–Uski, NETGEN, ARPACK, Crameri (26 instances)
- `work/C-algebra-arithmetic.md`: BGN, Schinzel, Steinig, Laurens, MSW, Korobov–Bugaevskaya, Müller et al.,
  Ostrowski, Beauville, Mazur, PARI (21 instances)

## Counts

| verdict | instances |
|---|---|
| ACCURATE | **74** (of which 10 checked only in the arXiv/preprint version, published numbering unconfirmed; marked †) |
| NEEDS CORRECTION | **20** |
| CANNOT VERIFY (instrument gap) | **3** (Steinig 1971; Korobov–Bugaevskaya §3/Thm 3.1, two instances) |
| total | 97 |

Separately, the check found **4 uncredited statements** (§3 below) and **17 bibliographic-record errors**
(§4 below). Some ACCURATE rows carry optional pinpoint refinements; these are in the working reports and are
not counted as corrections.

## 1. The 20 corrections

| # | line | cite as written | what the source says | correction |
|---|---|---|---|---|
| 1 | 174 | `[Thms~5.14--5.15]{dggw2008}` "complete invariant of the closed orientable 2-orbifolds with χ≥0" | Thm 5.15, p. 232: "The spectral invariant c is a complete **topological** invariant within C" | write "complete topological invariant (it determines the orbifold type)"; flat orbifolds have moduli |
| 2 | 174 | `[Rem.~5.16]{dggw2008}` "it answers the question left open in" | Rem. 5.16, p. 234, is an observation ("does not seem sufficiently strong to distinguish among these triangular pillows"), followed at once by the remark that the spectrum settles the orders at curvature −1 | "makes precise the observation of [Rem. 5.16]" (see NOVELTY.md) |
| 3 | 269 | `[(5.7)]{dggw2008}` for the csc² convention | (5.7), p. 227, is the result "χ(O)/6 + Σ(m_i²−1)/(12m_i)"; the convention b₀(γ^j)=1/(4 sin²(jπ/m)) is Ex. 5.3, p. 226 | `[Ex.~5.3, Prop.~5.5, (5.7)]` |
| 4 | 630 | `[Def.~4.7(i)]{dggw2008}` for the sum over the m−1 rotations | the sum over Iso^max is 4.5 (p. 219); I_N is 4.7(ii); "Iso^max(N) contains all of the nontrivial elements" is Ex. 5.3 | `[4.5, Def.~4.7(i)--(ii), Ex.~5.3]` |
| 5 | 172 | `[Thm~3.40, Cors~4.21(iv), 4.23]{ucar2017}` | Thm 3.40 (p. 98) is about **polygons**; Cor. 4.21(iv) (p. 139) is the orbisurface statement and assumes κ known | `[Cors~4.21(iv), 4.23; method of Thm~3.40]`, and "with the curvature given" |
| 6 | 174 | same | same | same |
| 7 | 220 | `\cite{ucar2017}` "Uçar computed every coefficient" | p. 134: "The next result from [Wat05] which we will need, and prove here with minor corrections"; p. 144: c^S_ℓ "were computed by S. Watson in [Wat05]" | credit Watson 2005 (N. Z. J. Math. 34) for the lune coefficients (4.25); add Schueth 2025 as refereed attestation |
| 8 | 349 | `[Cor.~4.21(iv)]{ucar2017}` after "the t⁰ coefficient determines them" | Cor. 4.21(iv) uses the whole spectrum | move the cite to a clause "(as does the full sequence of heat invariants)" |
| 9 | 178 | `[Thm~1.1]{drydenstrohmaier2009}` supporting "None of these can be a closed orientable hyperbolic 2-orbifold" | Thm 1.1 rules out examples with different isotropy. But "these" includes Sunada's method, which does produce isospectral closed hyperbolic surfaces and orbifolds (GWW p. 135 lists Vignéras, Buser, Brooks, Brooks–Tse) | "Neither phenomenon, a change of isotropy type or of maximal isotropy order, can occur among closed orientable hyperbolic 2-orbifolds, because …" |
| 10 | 662 | `[p.~3]{drydenstrohmaier2009}` | the passage is on CMB **p. 68**; p. 3 is the arXiv page | p. 68 |
| 11 | 693 | `[p.~3]{drydenstrohmaier2009}` | same | p. 68 |
| 12 | 172 | `[\S3, p.~8]{doylerossetti2011}` | the quote is verbatim in **v2 (2014) §3**; in v1 (2011) it is in §4 | bib entry: "arXiv:1103.4372v2 (2014)"; never published in a journal |
| 13 | 174 | `[Thm~1]{adfg2008}` "finitely many heat invariants also recover the singularity orders" | Thm 1: "the spectra of the Laplacian acting on 0- and 1-forms on M determine the weights"; for functions alone this is conjectured | "finitely many heat invariants of the Laplacians on 0- and 1-forms (or on functions together with the Euler characteristic)" |
| 14 | 178 | `\cite{gomezserrano2021}` "three eigenvalues do not" | Thm 1.1: λ_i(T_A)=λ_i(T_B) "for i = 1, 2, 4"; whether λ₁,λ₂,λ₃ determine a triangle is open (Grieser–Maronna p. 1446) | "the first, second and fourth Dirichlet eigenvalues do not \cite[Thm~1.1]" |
| 15 | 660 | `[p.~13.27]{thurston1980}` and the attribution "Thurston replaces that piece by the length d" | the quoted sentence is on original **p. 13.28** (e-edition p. 318); the text only calls the two-order-2 piece degenerate, "an interval" (p. 317), and the figures could not be checked | `[proof of Cor.~13.3.7]`; reword the attribution or justify the parameter d directly |
| 16 | 1487 | `\cite{alloucheshallit1999}` for ideal PTE solutions | the survey never mentions ideal solutions and defers to Borwein–Ingalls | cite Borwein–Ingalls 1994 |
| 17 | 1578 | `\cite{schoberl1997}` for "computed with NGSolve and NETGEN" | Schöberl 1997 is the NETGEN mesh generator only | add an NGSolve reference (see references-additions.bib, `ngsolve`, and GAPS.md) at l. 1286 and l. 1578 |
| 18 | 1288 | `\cite{strohmaieruski2013}` "all 42 multiplicity-one eigenvalues below 998 … which covers the (2,3,8) triangle orbifold" | count confirmed (exactly 42 in the data). But the list is the arXiv **v4 ancillary file** `eig-bolza-refined0-1000.txt`, not the CMP article, whose printed data link is dead. The 42 are matched by Neumann, Dirichlet **and two mixed** problems on the (2,3,8) triangle | cite "[§7.1 and ancillary file of arXiv:1110.2150v4]"; say "matched by the four sign-character problems on the (2,3,8) triangle"; add the CMP 359 (2018) correction |
| 19 | 1364 | `[\S4]{bgn1993}` "torsion … for every integer Λ ≠ 10" | p. 119: "We assume that the curve is nonsingular, i.e., n ≠ 0, 1 or 9" | "every integer Λ ∉ {0, 1, 9, 10}" |
| 20 | 1426 | `\cite{schinzel1996}` "what is new is the normalization by rescaling to a common sum" | p. 588: Schinzel normalizes x₁+x₂+x₃ = x₁x₂x₃ = 6, takes the least common denominator d, and obtains "Σ a_ij = 6d" for all k triples; his "primitive" (p. 587) is the manuscript's word for word | delete the novelty clause (NOVELTY.md §5); credit Kelly 1989 and Zhang–Cai 2013 |

## 2. The 3 unverifiable citations

| line | cite | status | what to do |
|---|---|---|---|
| 176 | `\cite{steinig1971}` | Primary unreachable (Rend. Mat. archive down, no zbMATH review, MathSciNet not accessible). Laurens p. 14 reports Steinig for "n **distinct** positive real numbers" | write "n distinct positive reals" (the manuscript says "n-multiset"); get repeated values from Laurens Cor. 3.3 |
| 176, 418 | `[\S3, Thm~3.1]{korobovbugaevskaya2016}` | AMS PDF returned HTTP 429 throughout this pass; the abstract supports the claim, and the G5 audit quoted Thm 3.1 (p. 727) from an earlier fetch | re-read §3 when AMS is reachable; fix initials to V. I. / A. N. |

## 3. Uncredited statements (no `\cite` at present)

| location | statement | prior source | action |
|---|---|---|---|
| Prop. 8.4, l. 1364, Thm 8.5 | P + T₂ = ι(P) (reciprocation), the permutation action, the dual and isosceles families | BGN p. 117 ("solutions occur in reciprocal pairs") and the table in §4, p. 120 | credit BGN |
| Lemma 4.8 | counting closed geodesics by area | Buser 1992, Lemma 6.6.4 (surfaces); Huber 1959, Satz 9 (asymptotics) | "cf." citation; keep the lemma for its explicit constant |
| before Thm 4.9 | the e^{−ℓ²/4t} hyperbolic term detects the systole | Dryden, arXiv:math/0411290, proof of Thm 4.5, p. 9: "there is a unique ω > 0 for which this limit is finite and nonzero … Then ω = ℓ(γ₁)" | credit Dryden 2004, McKean 1972, Huber 1959 |
| Thm 4.6 proof, Lemma 4.7 | trace formula with elliptic terms for the heat function | Hejhal LNM 548, Ch. 3, Thm 5.1, p. 351 (class: h even, analytic on \|Im r\| ≤ ½+δ, \|h\| ≤ M(1+\|Re r\|)^{−2−δ}); Garbin–Jorgenson 2020, Rem. 2.7, (2.8) | cite, and delete Lemma 4.7 (MISSING.md §1.2) |

## 4. Bibliographic-record errors in `references.bib`

All fixes belong in `paper/jga/tools/build_bib.py`, which generates `references.bib`.

| key | error | fix (source) |
|---|---|---|
| pari2172 | "released 1 March 2025" | **5 March 2025** (official announcement: "Done for version 2.17.2 (released 05/03/2025)") |
| korobovbugaevskaya2016 | initials V., A. | V. I. Korobov, A. N. Bugaevskaya (AMS article page) |
| schinzel1996 | no issue | no. 4 (zbMATH) |
| steinig1971 | year, journal style, case | "Rend. Mat. (6) 4 (1971), 629–644 (1972)"; brace {L}aguerre (G7-29 [10]) |
| beauville1982 | "singulieres" | singuli{\`e}res (print, p. 657) (G7-29 [35]) |
| kac1966 | number "4P2" | "4, Part 2" (journal text) (G7-29 [4]) |
| thurston1980 | URL printed twice | drop "available at …" from howpublished (G7-29 [23]) |
| alloucheshallit1999 | DOI underscore lost in print | `\doiurl` with `\detokenize` or escape `\_`; add editors Ding, Helleseth, Niederreiter and the series (G7-29 [27]) |
| marklof2011 | no series or editors | LMS Lecture Note Ser. 397, eds. Bolte, Steiner; pages differ (Crossref 83–120, zbMATH 83–119), so check the chapter (G7-29 [29]) |
| mazur1977 | pinpoint correct but ambiguous | `[Chap.~III, Cor.~(5.2), p.~156]` (G7-29 [36]) |
| ucar2017 | no DOI | doi 10.18452/18463 (DataCite) |
| doylerossetti2011 | version | v2, 2014 (see correction 12) |
| strohmaieruski2013 | correction and data source missing | add CMP 359 (2018) 427 and arXiv:1110.2150 |
| schoberl1997 | colon lost | "NETGEN: An advancing front …" (zbMATH) |
| arpack1998 | subtitle and series missing | add the subtitle and "Software, Environments, Tools 6" |
| crameri2023 | DOI printed twice | replace the note with "Version 8.0.1" |
| (all) | double-braced Crossref titles keep publisher casing; mixed journal styles | sentence case with proper nouns braced; one journal style. Also add "(N.S.)" for gww1992 and "(2)" for sunada1985 |

Checked and correct as they stand: msw2022 (year 2024 is the volume year), schueth2019 (2019 is the printed year;
Crossref's 2020 is the online date), barihunsicker2020, adfg2008, and all other volume/page data.

## 5. ACCURATE instances (74)

† = checked in arXiv/preprint only; the published numbering was not reachable (GAPS.md).

| key | lines (pinpoint) |
|---|---|
| dggw2008 (14) | 119; 174 (Prop. 5.22: finitely many terms is from its proof, p. 236); 174 (Rem. 5.16 quote, verbatim, p. 234); 220; 244 (Thm 4.8, Def. 4.7); 244 (§5.6 = Ex. 5.6); 251; 348 (Table 1 values); 349; 630 (Thm 4.8, Def. 4.7); 630 (Def. 4.7(iii)); 630 (§4.1); 701; 791 |
| ucar2017 (6) | 224 ((4.25) symbol for symbol); 244 (Thm 4.20(i), (4.35)); 244 (Thm 4.20(ii), (4.33)–(4.34)); 346; 361; 1286 (Thm 4.10, Cor. 4.18) |
| drydenstrohmaier2009 (8) | 172; 174 (Thm 1.1, Prop. 3.3); 192 (Thm 3.2); 679 (eq. (1); normalization fixed on p. 69); 693 (eq. (1)); 697; 795; 840 |
| doylerossetti2011 (1) | 172 (Thm 1) |
| schueth2019 (2) | 251, 311 (Thm 4.1, Rem. 4.2; coefficients checked) |
| donnelly1976 (3), mckeansinger1967, kac1966 | 119, 220, 630; 119; 119 |
| marklof2011 † | 693 (§11, p. 26 of arXiv: "the test function h(ρ)=e^{−βρ²} is admissible") |
| thurston1980 (3) | 192 (13.3.5, better 13.3.4–13.3.5); 642 (Cor. 13.3.7 verbatim); 660 (proof of Cor. 13.3.7) |
| troyanov1991 | 650 (Thm A, p. 793) |
| linowitzvoight2015 (2) † | 178, 795 (Thm A; signature in the paragraph after it) |
| barihunsicker2020 | 178 (Thms 3.1, 4.3; Exs. 6.6, 6.8) |
| sunada1985, gww1992, ssw2006, rsw2008 | 178 |
| griesermaronna2013 | 178 (Thm 1, p. 1442; the data are the first three heat invariants) |
| berndtyeap2002 † | 269 ((1.1) = Cor. 2.3) |
| holtztyaglov2012 (2) † | 378 ((1.37), Thm 1.17; sign of (orlando) verified) |
| alloucheshallit1999 † | 561 (§5.1, Thm 6) |
| schoberl1997, arpack1998 (2) | 1286; 1286, 1578 |
| crameri2023, crameri2020 | 1497 (v8.0.1; Box 2) |
| bgn1993 (6) | 158, 1035, 1336, 1343 (p. 118, (6)–(7)), 1350 (p. 119; "egg" is p. 118), 1423 (p. 119) |
| laurens2023 † | 176 (Lemma 3.2 and the remark after it, arXiv v2) |
| msw2022 † | 176 (Prop. 24, arXiv v1) |
| mueller2016 † | 176 (Thm 1.4, arXiv v2) |
| ostrowski1940 | 1136 (Théorème XXX, (71,1), p. 212) |
| beauville1982 | 1339 (Théorème and Tableau, p. 658; Γ⁰₀(6) = today's Γ₁(6)) |
| mazur1977 (2) | 1364, 1423 (Cor. (5.2), p. 156) |
| pari2172 (3) | 1042, 1426, 1575 (ellrank/elltors exist in 2.17.2; r₂ unconditional) |

Two notes on rows above:
- l. 1350, 1423: BGN state the egg argument for integer n. It works verbatim for rational Λ > 9, and the paper
  uses Λ = 155/12, so add one clause saying so.
- l. 244 and Lemma 2.5: no source other than Uçar (via Watson) gives the cone term at every order. DGGW and Donnelly
  stop at t¹ and Schueth 2019 at t². The only Uçar-free route is the elliptic term of the trace formula, which is
  not circular (A §3).
