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
| Theorem 3.3 (torsion: Z/6, Z/12, Z/2×Z/6; (1:1:t) and (1:r:r²) criteria; positive torsion points; orders 6, 6, 2 of the isosceles orientations and 4/12 of geometric progressions) | proof in the note (round 6, after N-b M1–M2); CN checks 7d (exact orders, 2G = Q₃+T₂, positive torsion points with S ≤ 60); blind check review/referee-round-6/blind-check-N |
| Sadek–El-Sissi analogue | as in §1 |
| (removed in round 6: now Theorem 3.3(iv)) | — |
| Remark 3.4 (no linear families) with proportional exception | TD variety.md §5 (Prop. 2); AD DI.4 (counterexample ℓ·(2,8,8), ℓ·(3,3,12); hypothesis "not all proportional" added) |

## §4 Lower bounds

| statement | source |
|---|---|
| Lemma 2.1 (every coincidence is admissible) | proof in the note (round 6, after N-e M2); CN check 7a (brute force to S = 240 and the discriminants) |
| Lemma 4.1 (every pair is kD for a unique primitive D; N(X) = Σ_D ⌊X/S_D⌋) | Lemma 2.1; CN check 7b (identity against per_S.csv for every X ≤ 4800) |
| Thm 4.2 identity, g ∈ {1,3}, g=3 ⇔ u≡v≢0 (mod 3), primitivity, D_{1,4} | TD variety.md §7 Thm 4; families.txt §1; AD DI.9 |
| area of Ω = log2/6 (u<v) | AD DI.9 (corrects the old "Y log2/3", which was the full quadrant) |
| densities 6/π², 1/4; c_iso = 3 log2/(2π²) | AD DI.9; TD variety.md §7 |
| O(√y log y) via Möbius over d ≤ √y (NT m8) | AD DI.9 ("Möbius inversion with the boundary error O(√y/d) per d ≤ √y") |
| partial summation, c_iso X log X + O(X) | AD DI.9 |
| classes: distinct Λ for distinct D_{u,v}; ≤ 1 isosceles pair per class | AD DI.9 (isosceles points on C_Λ are roots of 2r²+(5−Λ)r+2); (Λ−1)/(Λ−9) determines u/v by CN check 2 |
| 506 vs 505.7 | TD families.txt §2–3; AD check_isosceles.txt; CN check 5 |
| copies k ≥ 1: c_iso X log X − 0.286X for 10⁴ ≤ X ≤ 4·10⁷; 0.608X at 4800 | CN check 7c (to 10⁶); review/referee-round-6 computation to 4·10⁷ (−0.28628); the old −0.479X was the k ≥ 4 count (AD check_isosceles.txt) |
| Theorem 4.4 beats Theorem 4.2 only for log X > 128π⁴c_iso/3 = 437.8 | CN check 7c |
| 1.9 log X factor over ⌊X/18⌋ | 18·c_iso = 1.896 |
| Lemma 4.3 (conic bundle pairs, covers every primitive triple, multiplicity ≤ 6, GP ratios √(qr), q²/r, r²/q (CN check 7f)) | TD variety.md §7 Thm 5; families.txt §1 (conic bundle identity PASS); AD check_theorem5_family.txt; statement made self-contained per AD DI.10 |
| Thm 4.4 and proof, c_A = 3/(32π⁴), 3/(128π⁴) | TD variety.md §7 Thm 5; old manuscript App. A (8a9ebf0); verified step by step by the NT simulated referee (REPORT.md §3 row "Theorem 8.8 / Appendix A") and AD check_theorem5.txt; the audit's multiplicity concern (12 vs 6) is resolved by the "2 ways to choose the member" count |

## §5 Classes of every size

| statement | source |
|---|---|
| Schinzel's method: point of infinite order, rescaling by least common denominator d to Σ a_ij = 6d, primitive sets, pp. 587–588 | schinzel1996.txt (verbatim); CITATIONS.md correction 20; NOVELTY.md §5 |
| no novelty claimed for the method; Kelly 1989, Zhang–Cai credited | binding attribution (task brief), NOVELTY.md §5 |
| Thm 5.1 and proof (P=(4:9:18) of infinite order by Theorem 3.3(iv); odd multiples) | Theorem 3.3; TD variety.md §6 Thm 3; AD DI.5 (nP ≠ O for n ≤ 12, independent); Lemma 2.4 for positivity |
| rank C_{155/12} = 2 (PARI r1=r2=2; independent 2-isogeny descent) | TD data/ranks.txt; AD check_ranks.txt, check_descent.txt (Sel 8, 2) |
| 3P = (162833463:723926268:287876366) ordered | P3 (check_point3P.txt, 10/10 PASS); AD check_groups.py now compares ordered points (G7-15) |
| first classes 136, 408, 1849, 4600; ranks 2,2,3,3; Selmer orders (4,1), (4,4), (8,4), (16,2), (8,2), filled; 2^{r+2} = |Sel^φ||Sel^φ̂| (Silverman–Tate Chap. III); root numbers | TD data/ranks.txt (rootno); AD check_descent.txt; AD DI.6/DI.11 table; CN check 5 (members, sums, Λ, first occurrences) |
| no GRH in r2 for curves with a rational 2-torsion point | AD REVIEW.md "P5 verdict" item 3 (ellrank.c, makevbnf) |
| no class of size 7 up to 6000 | AD DI.11 (to 4800); CN check 6 (4801–6000) |
| Table 1 rank 0 and torsion for every row; C_{27/2}(Q) = 12 points, so the S = 18 class and its multiples are the only coincidences with Λ = 27/2 | TD data/ranks.txt (ellrank, elltors; ranks.py asserts the 12 points); AD check_descent.txt (rank 0 by descent); Theorem 3.3(ii) |
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
| local exponents 1.99 (500) → 1.58 (6000); N/X² 0.0094 (400) → 0.0040 (6000) | AT check_enum.txt (0.00935, 0.00405) |
| quadratic law not supported | TD RECOMMENDATION §1.2 (out-of-sample errors) |
| fit protocol (exact Poisson ML per sum on the whole window; LS on log(N(S) − N(599)) against exact partial sums; residual block bootstrap, 400 resamples, blocks of 50) | TD exponent_fits.py docstring and code (round 6) |
| q = 4.49±0.06 / 4.56±0.08 (all), 3.53±0.08 / 3.63±0.11 (primitive), dual 2.56±0.20 / 3.33±0.17, non-dual 3.73±0.09 (primitive) / 4.80±0.06 (all); power law β = 0.587, likelihood difference 9.48, dispersion 6.76, scaled 1.40 | TD data/exponent_fits.txt (window 600–4800) |
| scaling adds one log (NT m11) | Lemma 4.1 + partial summation; TD RECOMMENDATION §1.2 "Scalings add one power of the logarithm" |
| Figure 1 (F9) | figures/out/F9.pdf (read only); caption rewritten from figures/captions.tex \figcapNine, 3 sentences, without the isolation claim; colours batlow (figures/SPEC.md §3–4) |
| windows 1200–4800, 600–2400, 2400–4800 give 4.44, 4.64, 4.39 | TD data/exponent_fits.txt |
| line search: lines in P² of triples, Möbius pairing, 189 lines, |coeff| ≤ 7, only the dual conics (Vieta involution on lines through a vertex) | TD variety.md §5 ("Degree-2 families, searched"), families.py §5 |
| Remark 3.4 mismatched case (a+b)² = ab | AD DI.4 (c₁²+c₁c₂+c₂² = 0, equivalent) |
| (removed in round 6: by Lemma 2.1 there are no non-admissible coincidences) | — |
| §6.4: exponent between 1 and 3; a finite range bounds the limit from neither side; Question E | Thm 4.4, Prop. 6.1, Table 2; review/referee-round-6/VERDICT-N.md N7 |
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

- The threshold S ≤ 17 and the collision-free sums: companion paper.

## Round 6 additions

| statement | source |
|---|---|
| Proposition 2.3 proof of the base-point orders by five lines through the flex O | CN check 7d (tangent at O, line intersections) |
| Proposition 3.1 (ι = translation by T₂, collinearity, extension) | proof in the note; blind check |
| permutation paragraph (transpositions P ↦ π(O) − P, cyclic permutations translations) | proof in the note (fixed points); blind check |
| literature: Ulas (JNT 2013), Moreland–Zieve (arXiv:1304.1442), Cha et al. (IJNT 2019; arXiv:1811.07451 read), MacLeod (arXiv:math/0502475; Ravi identity CN check 7e), Sadek–El-Sissi pinpoints from the published PDF | records fetched by tools/build_bib.py (SOURCES.md); review/referee-round-6/VERDICT-N.md N10 |
| quintic description; twelve graph surfaces | elementary (degree of e₂(x)e₃(x′)); orbit description of §3 |

## Round 7 additions

| statement | source |
|---|---|
| C_Λ is the universal curve with a point of order 6: E_Λ at Λ = −1/c is isomorphic over Q to the Tate normal form E(c+c², c) by x = c²s/4 + c, y = c³η/8 + c²(c−1)s/8 + c² | CN checks 8a, 8a′ (sympy); (0,0) of order 6 checked with PARI `ellorder` at four values of c (round-7 scratch); Kubert's table as recorded by Mazur, p. 156 (fetched, `review/referee-round-7/main/scratch/lit/`) |
| Beauville's pencil is the modular surface of Γ0(6) | Top–Yui, arXiv math/0307230, Table 2 (fetched) |
| Mazur Theorem (5.1), p. 156: the fifteen torsion groups | Numdam scan (fetched, round-7 `lit/`) |
| Lemma lem:perm (α² = 1 ⇒ α = ±1; cyclic permutations are translations of order 3) | proof in the text; numerical consequences checked in CN 7d and by `theory/diophantine/torsion_pairs.py` (no difference in the order-3 subgroup) |
| Lemma lem:postrans and the C_{169/16} example; the four torsion-type pairs at S = 845, 1183, 2145, 3003; 7626 dual and 38624 other primitive pairs up to 4800 | TD `torsion_pairs.py` → `data/torsion_pairs.txt` (asserts); CN 8c; rank 1 and Z/12 of C_{169/16}: TD `ranks.py` → `data/ranks.txt` |
| Lemma 1 ranges 3 ≤ c′ ≤ 5, c′ ≥ 2 | CN 8b |
| dual family = quartic del Pezzo surface (five points, rank-5 linear system, no three collinear, Picard rank 5 over Q, conic bundle with section; positive points avoid the 16 lines; S_D within a factor 3 of the height) | TD `dual_delpezzo.py` (sympy asserts) |
| Browning–Sofos, Theorem 1.1 (both bounds B(log B)^{ρ−1} for a quartic del Pezzo surface over Q with a rational point and a conic over Q; U = complement of the 16 lines; standard height) | arXiv 1609.09057v4, fetched (round-7 `lit/`) |
| O(y(log y)⁴) primitive dual pairs, O(X(log X)⁵) contribution | the two rows above and Lemma 3 (partial summation) |
| Question E ⇔ A(y) = y^{1+o(1)} | Lemma 3: A(X) ≤ N(X) ≤ X ∫ dA(y)/y |
| holdout 4801–6000: exact 42960; log-power +0.2 %, power law +2.3 %; 0.2 and 1.9 scaled sd | TD `exponent_fits.py` → `data/exponent_fits.txt` |
| conductors 90, 6250530, 82110, 1715185290, 41388270; root number +1 for C_{27/2} | TD `ranks.py` → `data/ranks.txt` |
| Silverman–Tate α(Γ), ᾱ(Γ̄); orders (4,1), (4,4), (8,4), (16,2), (8,2) filled by images of points | AD `check_descent.txt` (its "Sel^phi(E)" is the bound for α on E, cf. its self-test against Silverman–Tate III.6) |
| Chen survey, Appendix A.5.1, p. 276: the (−1, 1) solutions and Choudhry's three-parameter solution | arXiv 2506.11429v1, fetched (round-7 `lit/`); Choudhry 2011 not obtained (bot wall), stated as such |
| BGN p. 130: four-variable expectation n ≥ 16 | `review/literature-pass/_fetched/txt/bgn1993.txt` l. 590–591; Zhang arXiv 1608.03382 p. 2 quotes it |
| Ulas, Theorem 3.1 and Corollary 3.4 | arXiv 1305.6241 (fetched by the N-e referee, round-7 scratch) |
| Graham 1963, van Doorn 2025 (partitions with prescribed reciprocal sum) | Crossref record; arXiv abstract (round-7 `lit/`) |
| DGGW erratum (Michigan Math. J. 66 (2017) 221–222) | Crossref record; text not obtained, no statement about its content |
