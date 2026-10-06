# TRACE: every statement of `note.tex` and where it comes from

Sources: `theory/diophantine/` (TD), `review/audit/diophantine/` (AD), `review/audit/threshold/` (AT),
`paper/arith/checks/check_note.py` with output `checks/check_note.txt` (CN, the checks of this note,
19/19 PASS), `theory/revision/point3P.tex` + `check_point3P.txt` (P3). The attributions follow
`review/literature-pass/` (CITATIONS.md, MISSING.md, NOVELTY.md §5) and were re-read in the fetched
texts under `review/literature-pass/_fetched/txt/`. The bibliography comes from fetched records only
(`SOURCES.md`, `tools/build_bib.py`).

Statements are referred to by their numbers in the built PDF.

## Abstract and §1

| statement | source |
|---|---|
| R<1 ⇔ hyperbolic triangle orbifold; area 2π(1−R); constant term χ/6+Σ(m²−1)/(12m) = (S+R−2)/12 | DGGW (5.7), p. 227 (CITATIONS.md row 3 and §5); arithmetic checked by hand: χ = R−1, Σ(m−1/m)/12 = (S−R)/12 |
| smallest coincidence (2,8,8),(3,3,12), S=18, R=3/4 | AD check_enum.txt (first class), TD data/per_S.csv; CN check 5 |
| "primitive" is Schinzel's definition, p. 587 | _fetched/txt/schinzel1996.txt (verbatim) |
| C_Λ is BGN's curve, integer Λ | BGN eq. (2), p. 117; TD novelty.md §1 |
| Beauville row Γ⁰₀(6), Théorème and Tableau p. 658 | TD variety.md §2; CITATIONS.md §5 (beauville1982). Γ₁(6) deliberately not named (TD RECOMMENDATION §6) |
| BGN "solutions occur in reciprocal pairs", p. 117 | _fetched/txt/bgn1993.txt l. 37 |
| Theorems 1.1, 1.2, Prop. 1.3, Conj. 1.4 | see §§4–6 below |
| Literature paragraph: Schinzel via x1+x2+x3=x1x2x3=6 | schinzel1996.txt (Lemma, p. 587) |
| Kelly 1989 classes of every size for equal sums/products | kelly1989 abstract (MISSING.md §1.4, _fetched/txt/kelly1989_ams.txt) |
| Zhang–Cai n-tuples | zhangcai2013 abstract (MISSING.md §1.5) |
| Schinzel's curve is the fibre over 36 of (x+y+z)³/xyz (Bremner–Guy) | NOVELTY.md §5; 6³/6 = 36 by hand; bremnerguy1997.txt p. 1 (the invariant) |
| Sadek–El-Sissi Prop. 2.5, Thm 2.8 | _fetched/txt/sadekelsissi2015.txt (Prop. 2.5 order 6; Thm 2.8 torsion Z/3, Z/6, Z/2×Z/6 by #S(M,N); infinite order otherwise under d1(d2−d3)³ ≠ d3(d1−d2)³, here "a mild condition") |
| Youmbai–Shamsi Zargar–Voznyy, parametric equal-sum/product families of sizes 2–4 | arXiv:2408.13867 (fetched record; first page read in review/literature-pass/_fetched/pdf/arx_2408.13867.pdf); added at the referee's request (SELF-REVIEW m11) |
| novelty sentence (counting function, bounds, enumeration new; geometry credited) | TD novelty.md summary table, recalibrated per NOVELTY.md §5 and CITATIONS.md §3 |

## §2 The curves

| statement | source |
|---|---|
| Prop. 2.1 and proof | TD variety.md §1 (Prop. 1); AD REVIEW.md DI.1 (independent proof; wording fixes "lie in", "may contain further triples" adopted) |
| Λ ≥ 9 at positive points, equality only (1:1:1) | TD variety.md §2 (AM–HM); AD DI.2 |
| Prop. 2.2: pencil identity, member t=1−Λ, Beauville row | TD variety.md §2, variety_checks.py §2 |
| maps s, η, inverse; BGN model (6) p. 118 | TD variety.md §2 and variety_checks.py §3c (symbolic, both compositions); AD DI.2 (re-derived; sign of ordinate differs from audit's own, both valid) |
| Δ = 2¹²Λ²(Λ−1)³(Λ−9) | TD variety.md §2; AD DI.2; BGN (9) p. 119 (fetched text) for the factor (n−1)³(n−9) |
| (1:4:4) ↦ (−6,45) at Λ=27/2 | CN check 3 (s = −6, η² = 45²); η = 45 also by hand from the η formula |
| fibre types I6, I3, I2, I1 | TD variety.md §2; AD DI.2 (ord Δ, c4) |
| base-point orders 2,3,3,6,6, cyclic of order 6 | AD DI.2 / check_groups.txt (orders listed as a correspondence, per the audit's fix) |
| BGN "egg" p. 118; quote "If P is on the egg..." p. 119 | bgn1993.txt ll. 76, 101 (verbatim) |
| Lemma 2.3 (egg) and proof | new write-up of AD DI.2 "Egg" argument and TD variety.md §2 "Real picture"; components/S¹×Z/2 per NT referee m4 (review/referee-sim/number-theorist/REPORT.md). Odd/even multiples checked up to 9P on C_{155/12}: AD DI.2, check_groups.txt |
| Remark 2.4: BGN quote "In all cases except n = 10, therefore, the torsion group is Z/6Z", §4 p. 120, nonsingular n ≠ 0,1,9 | bgn1993.txt (p. 120 text; "singular only for n = 0, 1 and 9", p. 119); CITATIONS.md correction 19 |
| (Λ²−6Λ−3)²−64Λ = (Λ−1)³(Λ−9); full 2-torsion ⇔ (Λ−1)(Λ−9) square | CN check 1; the criterion is the splitting of the quadratic factor of (2) |
| isosceles Λ−1 = 2(u+v)²/(uv), Λ−9 = 2(u−v)²/(uv) | CN check 2 |
| torsion ⊇ Z/2×Z/6 there; Λ = 27/2 | combination of the above with the base Z/6; elltors at 27/2 = Z/2×Z/6 in TD data/ranks.txt |

## §3 Reciprocation and the dual family

| statement | source |
|---|---|
| BGN reciprocal pairs p. 117; table §4 p. 120 (reciprocal = +(0,0), permutations = ±P+torsion) | bgn1993.txt (table printed above §5); CITATIONS.md §3 row 1; NOVELTY.md §5 |
| Prop. 3.1 and proof | TD variety.md §3, variety_checks.py §5 (symbolic); AD DI.3 (independent proof) |
| Cor. 3.2 (dual pair, S=e1e2, R=1/e3, GP exception, (1,4,4)) | TD families.txt §1 (symbolic PASS); AD DI.3 |
| permutation action, 12-point orbit for infinite-order P | AD DI.3 (12 elements verified for non-torsion P; restricted to infinite order per audit) |
| 1753 / 423 / 1330; none has P′∓P of order ≤ 12 | AD check_enum.txt ll. 23–25; TD families.txt §4 |
| Mazur Cor. (5.2), Chap. III, p. 156 | TD novelty.md (quote "m ≤ 10 or m = 12"); CITATIONS.md pinpoint |
| test covers larger torsion (NT m9) | the test is an exact order ≤ 12 check, independent of the torsion subgroup (AD check_enum.py) |
| Remark 3.3: (u:v:v) has order 6 | AD DI.7 (two-line proof; 358 points order 6, check_groups.txt l. 71–73) |
| Sadek–El-Sissi analogue | as in §1 |
| 40,305 primitive positive triples with sum ≤ 120: torsion ones are isosceles or GP | AD check_groups.txt ll. 108–109 |
| Remark 3.4 (no linear families) with proportional exception | TD variety.md §5 (Prop. 2); AD DI.4 (counterexample ℓ·(2,8,8), ℓ·(3,3,12); hypothesis "not all proportional" added) |

## §4 Lower bounds

| statement | source |
|---|---|
| Lemma 4.1 (R ≤ 3 for every triple, copies k ≥ 4, injectivity) | AD DI.8 (general justification adopted) |
| Thm 4.2 identity, g ∈ {1,3}, g=3 ⇔ u≡v≢0 (mod 3), primitivity, D_{1,4} | TD variety.md §7 Thm 4; families.txt §1; AD DI.9 |
| area of Ω = log2/6 (u<v) | AD DI.9 (corrects the old "Y log2/3", which was the full quadrant) |
| densities 6/π², 1/4; c_iso = 3 log2/(2π²) | AD DI.9; TD variety.md §7 |
| O(√y log y) via Möbius over d ≤ √y (NT m8) | AD DI.9 ("Möbius inversion with the boundary error O(√y/d) per d ≤ √y") |
| partial summation, c_iso X log X + O(X) | AD DI.9 |
| classes: distinct Λ for distinct D_{u,v}; ≤ 1 isosceles pair per class | AD DI.9 (isosceles points on C_Λ are roots of 2r²+(5−Λ)r+2); (Λ−1)/(Λ−9) determines u/v by CN check 2 |
| 506 vs 505.7 | TD families.txt §2–3; AD check_isosceles.txt; CN check 5 |
| secondary term −0.479X for 10⁴ ≤ X ≤ 4·10⁷ | AD check_isosceles.txt ll. 12–17 |
| 1.9 log X factor over ⌊X/18⌋ | 18·c_iso = 1.896 |
| Lemma 4.3 (conic bundle pairs, multiplicity ≤ 6, GP ≤ 3 ratios) | TD variety.md §7 Thm 5; families.txt §1 (conic bundle identity PASS); AD check_theorem5_family.txt; statement made self-contained per AD DI.10 |
| Thm 4.4 and proof, c_A = 3/(32π⁴), 3/(128π⁴) | TD variety.md §7 Thm 5; old manuscript App. A (8a9ebf0); verified step by step by the NT simulated referee (REPORT.md §3 row "Theorem 8.8 / Appendix A") and AD check_theorem5.txt; the audit's multiplicity concern (12 vs 6) is resolved by the "2 ways to choose the member" count |

## §5 Classes of every size

| statement | source |
|---|---|
| Schinzel's method: point of infinite order, rescaling by least common denominator d to Σ a_ij = 6d, primitive sets, pp. 587–588 | schinzel1996.txt (verbatim); CITATIONS.md correction 20; NOVELTY.md §5 |
| no novelty claimed for the method; Kelly 1989, Zhang–Cai credited | binding attribution (task brief), NOVELTY.md §5 |
| Thm 5.1 and proof (P=(4:9:18), nP ≠ O for n ≤ 12, Mazur, odd multiples) | TD variety.md §6 Thm 3; AD DI.5 (independent proof); Lemma 2.3 for positivity |
| rank C_{155/12} = 2 (PARI r1=r2=2; independent 2-isogeny descent) | TD data/ranks.txt; AD check_ranks.txt, check_descent.txt (Sel 8, 2) |
| 3P = (162833463:723926268:287876366) ordered | P3 (check_point3P.txt, 10/10 PASS); AD check_groups.py now compares ordered points (G7-15) |
| first classes 136, 408, 1849, 4600; ranks 2,2,3,3; Selmer groups filled | TD data/ranks.txt; AD DI.6/DI.11 table; CN check 5 (members, sums, Λ, first occurrences) |
| no GRH in r2 for curves with a rational 2-torsion point | AD REVIEW.md "P5 verdict" item 3 (ellrank.c, makevbnf) |
| no class of size 7 up to 6000 | AD DI.11 (to 4800); CN check 6 (4801–6000) |
| Table 1 rank 0 for C_{27/2} (ellrank r1 = r2 = 0, as for every row) | TD data/ranks.txt; AD DI.7. Only the rank is quoted; the isolation consequence and its descent stay in the companion paper (SELF-REVIEW M2) |
| S=408 class = 3×(S=136) ∪ {(65,70,273)} | AD DI.1, DI.6 |

## §6 Enumeration and growth

| statement | source |
|---|---|
| 3,067,197,199 admissible triples, 10 ≤ S ≤ 4800; hash on correctly rounded double + 128-bit cross-multiplication | AD DI.6 (enum_classes.c header); TD enumerate_core.c |
| two independent programs agree to 4800; one checked against Fraction enumeration for S ≤ 300 | TD RECOMMENDATION §1.1 (enumerate_fast.py vs harness) and AD DI.6 |
| third enumeration to 6000 | AT check_enum.txt ("C summary covers 10..6000", table to 6000) |
| rerun 4801–6000 reproduces 5400 and 6000 rows, gives 62,401 primitive classes | CN check 6 (with --enum; checks/enum_classes.c is a verbatim copy of AD enum_classes.c) |
| Table 2 rows 18–4800 | TD data/per_S.csv (cum_pairs, cum_classes, cum_prim_classes, max_fibre); RECOMMENDATION §1.1; AT check_enum.txt (local exponents) |
| Table 2 row 6000 (145679, 140005, 1.585) | AT check_enum.txt l. 61; primitive 62401 and largest 6: CN check 6 |
| 507 of 582 sums 19 ≤ S ≤ 600 carry a primitive class | TD data/per_S.csv (count computed this session; same figure verified by the NT simulated referee) |
| S = 36 example | old manuscript §8.4; AD DI.6 ("The PC.18 classes at S=36 are confirmed") |
| size histogram to 4800 {2: 96981, 3: 1627, 4: 122, 5: 11, 6: 1} | AD DI.6 |
| dual share 32.9% (S ≤ 200), 16.5% of 46,254 (S ≤ 4800) | TD families.txt §4 |
| 669 non-dual primitive pairs ≤ 400 not ±mP+T, m ∈ {2,3} | TD families.txt §6 (l. 53); variety.md §5 |
| Prop. 6.1 (upper bound) and proof | new in this note (G7-9; NT M2(a) sketch). Identity: CN check 4 (symbolic); recount of n(S) through the identity for S ≤ 160 equals per_S.csv: CN check 4 |
| trivial bound n(S) ≪ S³ | elementary (O(S²) triples; ≤ 1 partner per least entry: A′ fixed, R fixes B′) |
| local exponents 2.5 → 1.58; N/S² 0.0094 (400) → 0.0040 (6000) | AT check_enum.txt (0.00935, 0.00405) |
| quadratic law not supported | TD RECOMMENDATION §1.2 (out-of-sample errors) |
| fit protocol (Poisson ML per sum; LS on log cumulative against exact partial sums; 400 block-bootstrap resamples, blocks of 50) | TD exponent_fits.py docstring and code |
| q = 4.48±0.44 / 4.56±0.71 (all), 3.54±0.37 / 3.63±0.57 (primitive), dual 2.56±0.34 / 3.33±0.35, non-dual 4.79±0.47 | TD data/exponent_fits.txt (window 600–4800) |
| scaling adds one log (NT m11) | Lemma 4.1 + partial summation; TD RECOMMENDATION §1.2 "Scalings add one power of the logarithm" |
| Figure 1 (F9) | figures/out/F9.pdf (read only); caption rewritten from figures/captions.tex \figcapNine, 3 sentences, without the isolation claim; colours batlow (figures/SPEC.md §3–4) |
| method spread ≤ 0.1; windows 1200–4800, 600–2400, 2400–4800 give 4.43, 4.63, 4.37 | TD data/exponent_fits.txt |
| line search: lines in P² of triples, Möbius pairing, 189 lines, |coeff| ≤ 7, only the dual conics (Vieta involution on lines through a vertex) | TD variety.md §5 ("Degree-2 families, searched"), families.py §5 |
| Remark 3.4 mismatched case (a+b)² = ab | AD DI.4 (c₁²+c₁c₂+c₂² = 0, equivalent) |
| Lemma 4.1 for non-admissible primitive sets | AD DI.8 (R ≤ 3 for every positive triple) |
| §6.4: exponent between 1 and 3; data cannot exclude a limit in (1, 1.58) | Thm 4.4, Prop. 6.1, Table 2; G7-9 (review/referee-sim/G7-VERDICT.md) |
| heuristic corrected (G7-9): linear excluded; isosceles is a rational curve (d=2, m=2); dual family a rational surface (d=3, m=3); quadratic surface would give X^{3/2}; conjecture implies no such surface; not searched | G7-9 and NT M2(b); TD variety.md §4 (dual surface given by six cubics on P²) and §5 (degree-2 search covers pairs of lines only, 189 lines, |coeff| ≤ 7, 18 conics) |
| 84% non-dual | TD families.txt §4 (38628/46254 = 83.5%) |
| (P,P′) ↦ (e1(P′)P, e1(P)P′), fibre square of the blown-up pencil; all fibres I_n | TD variety.md §4 (map asserted in variety_checks.py §7) |
| Schoen: such fibre products have Calabi–Yau resolutions, Prop. 7.1 | TD variety.md §4 and RECOMMENDATION §4 ("fetched, read (Prop. 7.1, Table 1)"). Note: the literature pass could not re-open the body (paywall); the claim is stated at the level of variety.md and nothing is proved from it |
| Manin-type predictions for the dual del Pezzo | deliberately omitted (TD RECOMMENDATION §6: unverified, data disagree) |

## Declarations

Same as `paper/jga/manuscript.tex` (8a9ebf0) with the same placeholders: Zenodo DOI, author
contributions, use of AI tools. Funding, competing interests, ethics copied verbatim. The
acknowledgement of the colour maps is copied from the JGA paper because F9 uses batlow colours.

## Not in this note, by design

- The isolation of the minimal pair (its 2-descent, torsion list and the consequence that no third
  triple joins it): companion paper only. Table 1 quotes only the PARI-certified rank.
- The threshold S ≤ 17 and the collision-free sums: companion paper.
