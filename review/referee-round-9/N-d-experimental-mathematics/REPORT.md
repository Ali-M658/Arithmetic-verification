<!-- Round 9 N-d referee report: returned text saved verbatim; the reviewer could not write files -->

I could not save the report to REPORT.md because the write was refused, so the full report is below. In short: I recomputed every computational claim in the note independently, and all of them match to every printed digit except two I could not specify from the text (the Selmer local conditions and the line-family test). I recommend **minor revision**, with high confidence. The two MAJOR items concern how the growth data are interpreted and tabulated, not correctness.

# Referee report for *Integers*: "Triples with Equal Sum and Equal Reciprocal Sum"

**Referee remit:** Section 6 and every computational claim in the note: the enumeration and its completeness, the counts and tables, the fits and their stated uncertainties, the descent computations, and everything checked "by computer". I treated the marked placeholders (author contributions, AI-use statement, Zenodo DOIs, preprint identifiers) as known. I did not consult the authors' deposit. Every number below was recomputed from the text of the note alone, with my own code, in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/N-d-experimental-mathematics/scratch/code/`.

## Summary

The note studies unordered triples of positive integers that share their sum S and their reciprocal sum R with another triple. Following Bremner–Guy–Nowakowski, such triples are positive rational points on the cubic pencil C_Λ: e1·e2 = Λ·e3. The note:
- determines the torsion, and which torsion points are positive (Theorem 1 / Theorem A);
- proves N(X) ≥ N_cl(X) ≥ (3 log 2/(2π²) + o(1)) X log X and N(X) ≫ X (log X)², the latter from the dual (reciprocation) family;
- bounds the dual family above by O(X (log X)^5) through Browning–Sofos;
- proves n(S) ≪ S^{2+ε};
- obtains arbitrarily large classes by Schinzel's argument;
- in Section 6, reports an exhaustive enumeration up to S = 6000, a classification of the primitive pairs up to 4800, descriptive growth fits, and a heuristic discussion of the open Question E (is N(X) = X^{1+o(1)}?).

## Significance

On the computational side this is a careful, well-documented exhaustive search, and the description of the growth data is mostly honest. The authors say explicitly that the fits are descriptive, that the Poisson likelihood is only a weighting device, and that a finite range bounds the limiting exponent from neither side. The enumeration is the first systematic one for this problem; the earlier literature (Chen's survey, Choudhry) gives isolated solutions and families. The data feed the paper's main open question, so they matter.

The arithmetic content is modest but genuine. Large parts of the geometry are classical, and the authors credit them carefully. The computational part is a solid appendix-level contribution rather than a result in its own right. That is appropriate for an *Integers* note.

## Correctness, and what I recomputed

Everything I checked agrees with the paper exactly, to every printed digit. I found no computational error.

**Enumeration (Section 6.1, Tables 2 and 3).**
- I wrote an independent C++ enumerator (`enum.cpp`). For each S it lists all 2 ≤ a ≤ b ≤ c with a + b + c = S and e2 < e3, then groups by exact R. The grouping sorts by the double e2/e3 and breaks ties by exact 128-bit cross-multiplication. Since rounding is monotone, this is a strict weak order consistent with exact equality.
- I ran it for all S ≤ 6000 (6 processes, about 3 minutes).
- Admissible-triple totals: 3 067 197 199 for S ≤ 4800 and 5 992 496 499 for S ≤ 6000. Both match the paper.
- Table 3: every entry of every row reproduced exactly. That covers N(X), N_cl(X), primitive classes, largest size, and the local exponents 2.524 … 1.585.
- The in-text cumulative counts at S = 5400 also reproduce: N = 123 559, N_cl = 118 769.
- Table 2: the first class of each size k = 2, …, 6 matches in S, Λ and members. No class of size 7 occurs up to 6000.
- Class-size distribution up to 4800: 96 981 / 1627 / 122 / 11 / 1. Reproduced.
- 507 of the 582 sums 19 ≤ S ≤ 600 carry a primitive class. Reproduced. The two classes at S = 36 also reproduce.
- **Completeness independent of Lemma 1.** An exact `Fraction` brute force over all triples with a ≥ 1, with no admissibility filter, for S ≤ 200 gives N(200) = 386 and N_cl(200) = 380. No coincidence has R ≥ 1 (`brute.py`).

**Classification of the primitive pairs (Section 6.1).**
- I mapped points to E_Λ by the maps of Proposition 2 and decided "differs by a torsion point, for some ordering and sign" with PARI `ellorder`. This is an independent route from the paper's membership test via Theorem 1 (`classify.py`).
- There are 46 254 primitive pairs up to 4800: 7626 dual (16.49%), 4 of torsion type and 38 624 of the third kind (83.50%). The dual share for S ≤ 200 is 82/249 = 32.9%.
- The four torsion-type pairs are exactly the four listed, all on C_{169/16}.
- All 1330 non-dual primitive pairs with S ≤ 600 are of the third kind.
- Among the 669 such pairs with S ≤ 400, none satisfies P′ = ±mP + T or P = ±mP′ + T with m ∈ {2, 3}. Reproduced.

**Proposition 5.** I verified the identity (δB − pp′A)(δB′ + pp′A′) = −p²p′²AA′ symbolically. I also recounted n(S) for every S ≤ 160 by divisor enumeration through the identity. The recount matches the enumeration exactly (`prop5.py`).

**Section 6.3 fits** (`fits.py`, scipy).
- Poisson MLE for n(s) = c (log s)^q on [600, 4800]:
  - all pairs: q = 4.489;
  - primitive pairs: q = 3.532;
  - windows [1200, 4800], [600, 2400], [2400, 4800]: 4.437, 4.642, 4.390;
  - sums with gcd(s, 6) = 1, odd, even, multiples of 6: 4.061, 4.289, 4.609, 4.966;
  - dual pairs, primitive and all: 2.560 and 3.332;
  - non-dual pairs, primitive and all: 3.728 and 4.798.
- Cumulative least squares: q = 4.557 (all pairs) and 3.625 (primitive).
- Power law: β = 0.5868. The two laws have equal log-slope at s ≈ 2098.
- Hold-out 4801–6000: the true count is 42 960. The log-power law predicts 0.25% more and the power law 2.33% more.
- N(X)/X² is 0.00935 at X = 400 and 0.00405 at X = 6000.
- All of these agree with the paper to the printed digits.

**Section 4 numerics** (`iso.c`, `misc.py`).
- There are 506 pairs D_{u,v} with S ≤ 4800, against c_iso·4800 = 505.66. Of these, 27 lie in classes of size at least 3.
- The count of the copies kD_{u,v}, minus c_iso X log X, divided by X:
  - −0.2852 at X = 4800;
  - −0.2860 at 10^4;
  - −0.2862 to −0.2863 up to 4·10^7;
  - the count itself is 0.6077X at X = 4800.
- 3/(128π^4) = 2.406·10^-4. The bounds cross at log X = 437.8. 18·c_iso = 1.896.

**Descent and curve data (Table 1; Sections 2 and 5).** PARI 2.17.2 through `cypari2`, installed in a scratch virtual environment.
- The integral models (a, b) match Table 1 for all five curves.
- `ellrank` gives r1 = r2 = 0, 2, 2, 3, 3. `elltors` gives Z/2×Z/6, Z/6, Z/6, Z/6, Z/6.
- Conductors are 90, 6250530, 82110, 1715185290, 41388270; root numbers are +, +, +, −, −. All as stated.
- C_{169/16} has rank 1 and torsion Z/12; C_{49/4} has torsion Z/12. Both as stated.
- The images of α and ᾱ, computed on the full Mordell–Weil groups (generators plus torsion), are exactly the entries of Table 1, and |α||ᾱ|/4 = 2^r in each case.
- (Λ − 1)(Λ − 9)·den² = 6721, 1449, 1329601, 8569, none a square, and no Λ is a square. Correct.
- Proposition 2:
  - Δ = 2^12 Λ²(Λ − 1)³(Λ − 9) holds;
  - the maps to and from E_Λ are mutually inverse on the curves (symbolic);
  - (1 : 4 : 4) on C_{27/2} maps to (−6, 45);
  - the stated substitution sends E_Λ to the Tate normal form, with ratio 1/(64Λ^6);
  - (0, 0) of the Tate form corresponds to (0 : 1 : 0).
- On C_{155/12}, 3P = (162833463 : 723926268 : 287876366) is positive. Reproduced.
- Section 6.4: there are 189 lines with coprime |a|, |b|, |c| ≤ 7 meeting the open positive triangle, up to permutation and sign. This is the count under my reading.

**What I did not reproduce.**
- The local-condition computation that the Table 1 sets *are* the Selmer groups, as opposed to the images. PARI's unconditional upper bound r2 = r1 makes the ranks unconditional regardless.
- The Möbius-change line-family test in Section 6.4, which the paper does not describe in enough detail to reimplement (see m8).
- The internal "two independent programs / third enumeration" cross-checks, which are not described (see m3).

## FATAL

None.

## MAJOR

**M1 (pp. 20–21, §6.3 last paragraph and §6.4 first paragraph). The out-of-sample evidence is misdescribed, and "consistent with N(X) growing like X^{1.59}" is not supported by the data as stated.**

The paper says the sums 4801–6000 "do not separate" the two laws, although the power law overpredicts by 2.33% and the log-power law by 0.25%. This is not noise. I repeated the test on a second, disjoint hold-out: fit on [600, 3600], predict [3601, 4800]. The result is the same: log-power +0.21%, power law +2.32%. A fixed-exponent power law overpredicts every forward window by about the same amount. That is what the still-falling local exponent in Table 3 implies (1.868 at 600, 1.585 at 6000). Fitted to [600, 6000], β drops to 0.574.

So the data do discriminate on the observed range: the pure power law is systematically biased, and the log-power law extrapolates an order of magnitude better in both hold-outs. Neither conclusion is asymptotic. The honest description is:
- on [600, 6000] the log-power law (whose cumulative form is X^{1+o(1)}) is the better descriptive model, by both hold-outs;
- this is weak, non-asymptotic evidence in the direction of a positive answer to Question E;
- nothing excludes a limiting exponent above 1.

*Resolution:* replace "do not separate them either" by an accurate statement of both hold-out discrepancies. Qualify the X^{1.59} sentence in §6.4, and the abstract's framing, as a statement about the limiting exponent only.

**M2 (p. 4, Question E; p. 19, Table 3; p. 20). The quantity in which Question E is posed is not tabulated.**

Question E is shown to be equivalent to A(y) = y^{1+o(1)} for the number A(y) of *primitive pairs*. The paper calls the primitive counts "the smoother objects". Yet Table 3 gives primitive *classes*, not A(X), and no local exponent for A. A grows visibly more slowly than N. My values:

| X | A(X) | log2(A(X)/A(X/2)) |
|---|---|---|
| 1000 | 4 141 | 1.641 |
| 2000 | 12 512 | 1.595 |
| 4000 | 35 567 | 1.507 |
| 4800 | 46 254 | 1.481 |
| 6000 | 63 876 | 1.461 |

This undercuts "1.58" as the headline exponent: for the object Question E is actually about, the local exponent is 1.46 and falling.

*Resolution:* add A(X) and its local exponent to Table 3, and quote it next to 1.58 in §1.3 and §6.3, or in the abstract.

## MINOR

**m1 (p. 17).** "e2, e3 ≤ (S/3)³ ≤ 8·10^9" appears in a sentence about S ≤ 4800, where the bound is 4.1·10^9; 8·10^9 is the bound at S = 6000. Also add the step that, because e2 and e3 are exactly representable, the IEEE quotient is the correctly rounded value of the rational, so equal rationals give equal doubles.

**m2 (p. 20; abstract; §1.3).** "1.99 at X = 500 and falls to 1.58" hides that the column is not monotone (1.954 at 400, 1.993 at 500). Say "about 2 on [300, 500], then decreasing monotonically".

**m3 (p. 18).** The verification pipeline is under-described:
- What makes the "two independent programs" independent?
- How does the "third enumeration" work?
- Which program produced which column on (4800, 6000]? As written, the primitive classes and class sizes there rest on a single program.

My independent run confirms every number, so this is about exposition, not correctness.

**m4 (p. 20).** The per-sum fits are visibly misspecified: q runs from 4.06 to 4.97 across residue classes of s, because n(s) is a divisor sum. Lead with the primitive fits, and use the all-pairs per-sum q = 4.49 only to illustrate the divisor-sum effect.

**m5 (p. 20).** The cumulative least-squares fit on log(N(S) − N(599)) uses 4201 nested, strongly autocorrelated points and is dominated by small S. Say so, or fit on a geometric grid of S.

**m6 (p. 20).** "The fitted 2.56 falls well short of the exponent 4": 4 is only an upper bound for the positive points, and Theorem 3 proves exponent 1 per sum. Say "between the proved 1 and the upper bound 4, and well below the expected 4".

**m7 (p. 17, Table 1).** The caption "the Selmer groups containing the images" is ambiguous: say that the entries are the Selmer groups and that they equal the images. Also document, at least in the deposit README, how local solubility was decided:
- at which primes;
- whether the real place is included;
- what explicit points realise each class.

**m8 (p. 22).** The line-family search ("discriminant of the branch values of Λ", "Möbius change", "family") cannot be reproduced from the text. In particular:
- What exactly is the invariant?
- Is the identity Möbius map on the same line excluded?
- Is the bound |a|, |b|, |c| ≤ 7 justified by anything other than cost?

Give the criterion in two or three sentences. Only the count of 189 lines reproduced.

**m9 (p. 13).** The constant −0.286 reproduces (−0.2860 to −0.2863). It is computable in closed form from the Möbius-inversion and partial-summation argument of Theorem 2. Either derive it or label it empirical.

**m10 (pp. 18–19).** The m ∈ {2, 3} relation test covers only 669 pairs with S ≤ 400, and on curves of rank ≥ 2 a negative result is the expected outcome. Motivate it or shorten it to a sentence.

**m11 (p. 18, Table 2 caption).** Ranks are cited "from ellrank/elltors". Also cite the unconditional 2-isogeny descent of Table 1, which is what proves them.

## Presentation

- **P1 (p. 21, Figure 1(b)).** On log–log axes the dashed fit lies on the data curve, so the figure cannot show the 0.25% versus 2.33% discrepancy the text discusses. The plot also stops at 4800 although data exist to 6000. Add a residual panel: the ratio of data to each fit over [600, 6000], with the fit window marked.
- **P2 (p. 19, Table 3).** Add the A(X) column (M2). Either add an X = 5400 row, which the text uses (N = 123 559, N_cl = 118 769), or drop the reference.
- **P3 (Table 3 caption).** The X = 100 local exponent uses N(50), which is not in the table. Note in the caption that N(X/2) comes from the same enumeration.
- **P4 (p. 20).** Anchoring N(X)/X² at X = 400 looks arbitrary. Use the same anchor as the local-exponent discussion.
- **P5 (p. 18).** For the rerun on 4801–6000, say which counts were compared: pairs and classes only, or every column.

## Recommendation

**Minor revision** within my remit. **Confidence: high** for the correctness of every computational claim. I reproduced all of them independently, with exact agreement, except the Selmer local conditions and the line-family test.

The two MAJOR items concern interpretation and tabulation, not correctness. Each is fixed by a paragraph and a table column. With them fixed, the experimental section would be a model of honest reporting for this kind of note.

## What resolves each issue

| Issue | What resolves it |
|---|---|
| M1 | Report both hold-out discrepancies accurately; qualify "consistent with X^{1.59}". |
| M2 | Add A(X) and its local exponent to Table 3 and quote it in the text. |
| m1 | Correct the bound for S ≤ 4800 (or state it for 6000); add the IEEE correct-rounding sentence. |
| m2 | Describe the local exponent as non-monotone below 500. |
| m3 | One paragraph on what each of the three programs is and checks. |
| m4 | Lead with the primitive fits; present the residue-class spread as evidence of misspecification. |
| m5 | Note the autocorrelation and weighting, or use a geometric grid. |
| m6 | Rephrase as "between the proved 1 and the upper bound 4". |
| m7 | Clarify the caption; document how local solubility was decided. |
| m8 | Specify the line-pair criterion and what counts as a family. |
| m9 | Derive the secondary constant, or label it empirical. |
| m10 | Motivate the test or shorten it. |
| m11 | Cite the 2-isogeny descent of Table 1 in the Table 2 caption. |
| P1 | Add a residual panel to Figure 1(b), extended to 6000. |
| P2 | Add the A(X) column and either a 5400 row or no reference to it. |
| P3 | Note in the caption where N(X/2) comes from. |
| P4 | Use the same anchor X as the local-exponent discussion. |
| P5 | Say which counts were compared on the rerun. |

### Reproduction files

All in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/N-d-experimental-mathematics/scratch/code/`:
- `enum.cpp`: the enumerator;
- `brute.py`: exact brute force with no admissibility filter;
- `analyze.py`: Tables 2 and 3 and the in-text counts;
- `classify.py`: dual / torsion / other classification and the m ∈ {2, 3} test;
- `fits.py`: all fits and both hold-outs;
- `prop5.py`: the Proposition 5 identity and recount;
- `iso.c`: the isosceles copies and their secondary term;
- `descent.py`: Table 1 images;
- `threeP.py`: 3P on C_{155/12};
- `symb.py` and `tate.py`: the Proposition 2 maps, discriminant and Tate normal form;
- `misc.py`: the remaining scalar claims.

The outputs are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-9/N-d-experimental-mathematics/scratch/out/`.
