# VERDICT-N: referee round 6, the note ("Triples with equal sum and equal reciprocal sum", Integers)

Reports: `N-a-editor-unit-fractions/`, `N-b-elliptic-ranks/`, `N-c-surfaces-diophantine/`,
`N-d-certified-enumeration/`, `N-e-rigour-citations/` (each `REPORT.md`, verbatim). No reviewer commented on
length. This is the first panel on the note.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| N-a editor (unit fractions) | **SEND TO REVIEW**; major revision | high (correctness), moderate (significance) |
| N-b elliptic ranks | major revision | high (elliptic parts) |
| N-c surfaces and Diophantine equations | minor revision | high (correctness), medium |
| N-d certified enumeration | major revision | high (computations) |
| N-e rigour and citations | minor revision | about 85% |

**Stop condition: NOT MET.**

Every count and table entry was reproduced exactly by at least three reviewers with independent programs
(Table 2 in full to S = 6000; Table 1; 3 067 197 199 triples; the class-size histograms; all ranks with
PARI 2.17.2).

## FATAL

None.

## MAJOR (deduplicated; checked)

| id | issue | raised by | status | evidence / resolution |
|---|---|---|---|---|
| N1 | Remark 2: "a positive isosceles point therefore has order 6" is false: the orientation (v:v:u) is fixed by the swap of x and y, which acts as P ↦ −P, so it has order 2. | N-b M2, N-d m2, N-e M1 | **CONFIRMED** | PARI (scratch venv, cypari2 2.2.4): on C_{27/2}, (1:4:4) and (4:1:4) have order 6, (4:4:1) order 2. Resolution: state the orders by orientation. |
| N2 | Remark 1's torsion description is incomplete: Z/12 occurs, exactly through geometric-progression points (1:r:r²), which have order 12. | N-b M1, N-d m4, N-e m7 | **CONFIRMED** | PARI: (1:2:4), (1:3:9), (4:6:9), (9:15:25) have order 12 and torsion Z/12. Resolution: by Mazur and the Z/6 base group the torsion is Z/6, Z/12 or Z/2×Z/6; Z/2×Z/6 exactly when (Λ−1)(Λ−9) is a square (the 2-torsion points other than T_2 are the fixed points (1:1:t) of the swap); Z/12 occurs on the curves through geometric progressions (checked, stated as computed for those Λ, not proved in general). |
| N3 | The rank of C_{27/2} (Table 1) and the minimality of the smallest pair are deferred to an unrefereed companion; the note should be self-contained. | N-b M3, N-a M4, N-d m9, N-e m6, N-c P1 | **CONFIRMED** | Resolution: rank 0 by PARI's `ellrank` (r_1 = r_2 = 0, unconditional upper bound) and LMFDB 90.c3, torsion Z/2×Z/6, so C_{27/2}(Q) has 12 points; a hand descent is in the companion (Appendix E there); minimality from the enumeration and the companion's proof. |
| N4 | "An independent 2-isogeny descent ... confirms each rank" is undocumented. | N-b M4, N-c m5, N-a m12 | **ANSWERED IN REPOSITORY BUT NOT PAPER** | The descent exists: `review/audit/diophantine/check_descent.py` (exact arithmetic, Hensel-type local solubility, self-test on y^2 = x^3 - x), output `check_descent.txt`: Selmer orders (4,1), (4,4), (8,4), (16,2), (8,2) for C_{27/2}, C_{68/5}, C_{1849/120}, C_{230/21}, C_{155/12}, filled by images of exact points, ranks 0, 2, 3, 3, 2. Resolution: the paper now gives these Selmer orders, the formula 2^{r+2} = |Sel^phi| |Sel^phi'| (Silverman-Tate, Chap. III, fetched record) and says exactly what `ellrank` proves (r_2 from the 2-Selmer group, r_1 resting on a floating-point regulator); root numbers agree with the parities. |
| N5 | Lemma 3 parametrises every primitive triple, so it is the whole dual family, not a "subfamily"; Theorem 4 is a lower bound for that family, not its order ("the order of growth is the point", "its conic-bundle part gives X(log X)²"); Theorem 4 beats Theorem 3 only for log X > 438. | N-c M1, m1, N-a M1, m6 | **CONFIRMED** | x = (u, vq, vr) with u = a, v = gcd(b,c) covers every primitive triple; 128π⁴c_iso/3 = 437.8. Resolution: rewrite the framing; state the threshold. |
| N6 | The reported bootstrap uncertainties (±0.44 etc.) come from resampling blocks of counts onto fixed abscissae, which destroys the trend; "the model uncertainty is larger" then contradicts the reported numbers. | N-d M1 | **CONFIRMED** | `theory/diophantine/exponent_fits.py` resampled count blocks on a fixed grid. Resolution: residual block bootstrap around the fitted trend, exact Poisson MLE (Newton); new values 4.48 ± 0.06 and 4.56 ± 0.08 (all), 3.54 ± 0.08 and 3.63 ± 0.11 (primitive); model uncertainty (up to 0.26 across windows) now larger than the bootstrap, as stated. |
| N7 | The evidence does not single out exponent 1: a pure power law fits about as well; "does not exclude a limiting exponent anywhere between 1 and about 1.58" is wrong (a finite range does not bound the limit above either); the conjecture needs a heuristic or should be a question. | N-d M2, N-a M3, N-e m11 | **CONFIRMED** | New fit: β = 0.587 (cumulative exponent ≈ 1.59), log-likelihood difference 9.48, Pearson dispersion 6.76, scaled difference 1.40 (not decisive). Resolution: Conjecture 1 becomes Question 1; report both fits; correct the sentence. |
| N8 | Every coincidence is admissible (R < 1 automatically), so "need not be admissible" (Corollary 1, Lemma 3) and the restriction k ≥ 4 (Lemma 2) are wrong or unnecessary, and the "−0.479X" secondary term belongs to an artificial count. | N-e M2 | **CONFIRMED** | Proof: a triple with R ≥ 1 is (1,b,c), (2,2,c), (2,3,c ≤ 6), (2,4,4) or (3,3,3); the pairings within this list give either the same triple or quadratics without integer roots (checked by hand). Recomputed: with all copies k ≥ 1 the isosceles count is c_iso X log X − 0.286X to three digits for 10⁴ ≤ X ≤ 4×10⁷, and 0.608X at X = 4800 (the thin curve of Figure 1(b)). Resolution: a lemma with this proof; k ≥ 1 throughout. |
| N9 | Significance: the upper bound X^{3+ε} is at the scale of the number of triples and does not show that coincidences are rare; the claims should be recalibrated. | N-a M1, N-d m7 | **CONFIRMED** (presentation) | Resolution: say so plainly; present the results as family counts plus data; the abstract leads with Theorem 3. A non-trivial upper bound is not attempted (stated as open). |
| N10 | Literature: Ulas (equal sums of i-th powers for i = −1, 1, 2, n ≥ 4), Moreland-Zieve, Cha et al. (counting for equal sum and product), Choudhry 2011, MacLeod (R/r = N, the same pencil through the Ravi substitution), the fibre square as a quintic threefold. | N-a M2 | **CONFIRMED in part** | Fetched and read: Ulas arXiv:1305.6241 Cor. 3.4 (n ≥ 4, integers, not positivity), Moreland-Zieve arXiv:1304.1442 abstract, MacLeod arXiv:math/0502475 abstract, Crossref records of Cha et al. (IJNT 2019) and Choudhry (RMJM 2011). R/r = (Λ−1)/4 under a = y+z, b = z+x, c = x+y (checked). Not cited: Choudhry 2011 (full text not retrievable: the publisher's server refused the download, and no abstract is deposited), Ulas's Math. Comp. paper (not read), Verrill 2000 and Saito-Yui 2001 (content not verifiable from the fetched records), Halbeisen-Hungerbühler-Zargar (not fetched). Cha et al. read from arXiv:1811.07451 (counts the sizes n for a fixed sum); Sadek-El-Sissi pinpoints read from the published version (Osaka repository PDF): Prop. 2.5 (isosceles, order 6), Prop. 2.7 (rank >= 1 under d1(d2-d3)^3 != d3(d1-d2)^3), Thm 2.8 (torsion). |

## MINOR and presentation, with disposition

| id | item | raised by | disposition |
|---|---|---|---|
| n1 | Γ⁰₀(6) notation for Beauville's row | N-b m6, N-a m1, N-e m12 | fix: describe the pencil by its singular fibres I6, I3, I2, I1 (Beauville's list), without the subgroup symbol |
| n2 | Prop. 3: six base points incl. O; nine with multiplicity; geometric derivation of the orders | N-b m2, m3 | fix |
| n3 | Lemma 1: nonemptiness; drop "rational" | N-b m4, N-e m4 | fix |
| n4 | Prop. 2: admissibility clause | N-b m5, N-e m1 | fix (with N8) |
| n5 | Prop. 4: ι undefined at base points; collinearity | N-b m1, N-e m2-m3 | fix |
| n6 | Sadek-El-Sissi pinpoints (Prop. 2.7, Thm 2.8 hypotheses); Mazur locator | N-b m7, N-e m9 | fix (Mazur locator checked correct by N-e) |
| n7 | Theorem 5: Nagell-Lutz certificate; Schinzel's positivity argument; "next positive point" | N-e m5, m8, N-c m4, N-b m11 | fix: "next positive multiple of P", say positivity here comes from Lemma 1; Nagell-Lutz certificate not added (PARI order computation and the exact check are kept) |
| n8 | "for at most 3 ratios": name them √(qr), q²/r, r²/q; Theorem 4 proof details | N-c m6, m7 | fix |
| n9 | Möbius inversion in residue classes | N-c m2 | fix |
| n10 | 506 counts the D_{u,v}; 27 lie in larger classes | N-c m3 | fix |
| n11 | "twelve points" wording | N-b m10 | fix |
| n12 | Fig. 1(b) thin curve and range S ≤ 4800; colour key; in-figure marker | N-a m7-m8, N-d m1, N-e P1 | fix caption (with N8 the thin curve is Theorem 3's count); figure kept (panel letters are the permitted text) |
| n13 | Table 2 heading S vs X; "largest class size so far"; "both conventions" | N-a m9, N-d P1, P4 | fix |
| n14 | fit rounding (exact GLM) | N-d m3 | fix (with N6) |
| n15 | 189 lines up to permutation; Möbius search description | N-d m5, N-e m11 | fix |
| n16 | certification per column; triple count to 6000 | N-d m6 | fix: state which program produced which column, add 5 992 496 499 |
| n17 | exponent range from S ≥ 500 | N-d m8 | fix |
| n18 | abstract too long, both conventions | N-a P1 | fix |
| n19 | duplicate numbering (Thm 1 = Thms 3-4) | N-a P3, N-e P3 | no change (the introduction points to the sections; standard practice) |
| n20 | Statements block in Integers style | N-a P2 | no change: the placeholders (author contributions, AI use) must stay until the authors fill them |
| n21 | "withsum" | N-d P2 | check the Integers source |
| n22 | DGGW erratum | N-e m13 | no change (not verifiable here whether (5.7) is affected) |
| n23 | trim companion material | N-e m15 | partly (the paragraph is shortened) |
| n24 | Remark 3 is a sketch | N-a m4, N-e P5 | fix: say so |

## Resolutions (round 6 fixes)

| id | resolution in `paper/arith/note.tex` (Integers version regenerated) | check |
|---|---|---|
| N1, N2 | Theorem 3.3 (Torsion) replaces Remarks 1-2, with proof: (i) Z/6, Z/12 or Z/2xZ/6 (Mazur); (ii) Z/2xZ/6 iff a rational (1:1:t), iff (Lambda-1)(Lambda-9) is a square; (iii) Z/12 iff a rational (1:r:r^2), Lambda = (r+1+1/r)^2, 2G = (0:1:-1)+T_2; (iv) for Lambda > 9 a positive point is torsion iff isosceles or a geometric progression in some order; orders 6, 6, 2 for (u:v:v), (v:u:v), (v:v:u); orders 4 (middle term last) or 12 for geometric progressions. Stated in the introduction as Theorem A. | `paper/arith/checks/check_note.py` 7d; blind check |
| N3 | Table 1 prints rank 0 and torsion for every row (generator `paper/tools/release_files/note_make_tables.py`); Section 5 proves C_{27/2}(Q) = 12 explicit points and that the S = 18 class and its multiples are the only coincidences with Lambda = 27/2; the companion is cited only for the spectral consequences. | `theory/diophantine/ranks.py`, descent |
| N4 | See the table above. | `review/audit/diophantine/check_descent.txt` |
| N5 | Lemma 4.3 is "the dual family as a conic bundle" and covers every primitive triple; the three ratios named; the text after Theorem 4.4 says it is a lower bound for the dual family, not its order, and gives the threshold log X > 438 (also after Theorem B of the introduction). | 7c, 7f |
| N6 | `theory/diophantine/exponent_fits.py`: exact Poisson MLE on the whole window (the trimmed window had moved the second decimal: 4.48 -> 4.49), residual block bootstrap, primitive non-dual series added; the bootstrap and cumulative fits are described precisely in Section 6.3. | rerun, `data/exponent_fits.txt` |
| N7 | Conjecture -> Question (E); power-law fit reported (beta = 0.587, X^{1.59}, scaled likelihood difference 1.4); "between 1 and 1.58" replaced by "a finite range bounds the limiting exponent from neither side"; heuristic paragraphs labelled. | |
| N8 | Lemma 2.1 (coincidences are admissible) with proof; k >= 1 throughout; Lemma 4.1 is now the identity N(X) = sum_D floor(X/S_D); the secondary term is -0.286X; Theorem 4.4 keeps S_D <= X with floor(X/S_D) >= X/(2 S_D). | 7a, 7b, 7c |
| N9 | Abstract and introduction: the upper bound is said to be at the scale of the number of triples; the results are presented as family bounds plus data. | |
| N10 | Literature paragraph: Sadek-El-Sissi with exact pinpoints and hypotheses, Moreland-Zieve, Cha et al., Ulas, MacLeod with the Ravi identity R/r = (Lambda-1)/4; quintic description in Section 6.4; the twelve graph surfaces. New records fetched by `paper/arith/tools/build_bib.py`. | 7e |
| minors | n1 fibre types instead of the subgroup symbol; n2 six base points, nine with multiplicity, orders proved by five lines through a flex; n3 nonemptiness, "rational" dropped; n4 k >= 2 and admissibility by Lemma 2.1; n5 iota defined off three points, extended by continuity, collinearity shown; n6 pinpoints; n7 infinite order of (4:9:18) now from Theorem 3.3(iv), "next positive multiple", positivity from Lemma 2.4 (no claim about Schinzel's own route); n8 ratios named, U >= V/2 >= 1, the O(1) range; n9 Moebius step written out; n10 506 counts the D_{u,v}, 27 in larger classes; n11 "six orderings of x and six of its dual"; n12 caption rewritten (two sentences), the thin curve identified as all copies, S <= 4800, colours and outline in the text; n13 Table 2 uses X, "largest class size" in the caption; n15 189 lines up to permutation and sign, search method; n16 which program confirms which column, 5 992 496 499 triples; n17 local exponent quoted from X = 500; n18 abstract shortened; n19 introduction results labelled Theorem A-C, Proposition D, Question E; n21 "withsum" is not in the source (an extraction artefact); n24 Remark 3.4 labelled a sketch, constant entries mentioned. Notation: Delta° -> Pi, Q(u,v) -> W(u,v), (p,q,r) -> (p,b,c) in Proposition 6.1. | |
