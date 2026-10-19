# VERDICT-N (round 8): "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

Inputs: the five reports of Panel N (README.md). Length remarks are excluded.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| N-a editor (additive combinatorics, unit fractions) | send to review; major revision | high (correctness), medium (recommendation) |
| N-b (descent, ranks, heights) | minor revision | high |
| N-c (parametric Diophantine) | minor revision, conditional on M1 | high (correctness), moderate (novelty) |
| N-d (exhaustive enumeration, fits) | minor revision (M1, M2 mandatory) | high |
| N-e (rigour and citations) | minor revision | about 0.85 |

No FATAL item. Every referee reproduced the enumeration, the ranks, torsion, conductors and the proofs they checked.

**Stop condition: not met** (confirmed MAJOR items remain before the fixes; every referee already recommends minor revision).

## FATAL and MAJOR items

| id | item (reviewers) | status | resolution |
|---|---|---|---|
| N1 | "classes of every size" overstates Theorem C (size at least k) (N-b M1) | CONFIRMED | "arbitrarily large classes" in the abstract, Theorem B/C name, Section 5 title and Theorem 4 name |
| N2 | Bremner–MacLeod 2014, the same pencil, missing (N-a M1) | CONFIRMED (read in the fetched text) | Cited and compared: E_N(BM) = E_{2N+6} under (x,y,z) = (b+c, c+a, a+b); their torsion (Lemma 2.1), egg (Section 4), no solutions for odd N (Theorem 5.1, Corollary 5.2) as the triangle-region case of Nguyen Xuan Tho; their 2025 corrigendum (Table 2 only) cited; "new" softened to "not found in the literature", with the integer case stated. `check_note.py` 9b, 9c |
| N3 | Choudhry 2011 not read (N-a M2, N-c M1) | CONFIRMED that it is unread; NOT RESOLVABLE here: Project Euclid blocks scripted access (four attempts, rounds 7 and 8), no browser may be used, no arXiv version exists, and Chen's survey and the zbMATH review give no formula | The note now says the paper was not accessible, that it cannot say whether Choudhry's family is or contains the dual or isosceles family, credits the classical identity behind the dual family (λ/x, λ = e_1 e_n/e_{n−1}; BGN p. 117; `check_note.py` 9d), and separates "individual coincidences [Chen]" from "a parametric family [Choudhry]". The counting results do not depend on it. Action for the authors (SUBMISSION-CHECKLIST): read Choudhry 2011 in a browser and settle the comparison |
| N4 | Proposition D (upper bound) is placed vaguely; its relation to dimension growth (N-a M3) | CONFIRMED (presentation) | Paragraph after Proposition C: the bound is the size expected for integer points on the threefold of pairs with fixed sum, and a power saving needs input special to this threefold (a citation of Browning–Heath-Brown–Salberger was removed after the fix check: their bounds need degree ≥ 6) |
| N5 | Section 6.3 over-interprets the fits: holdout SD ignores parameter uncertainty, bootstrap spreads misleading, laws tangent on the window, per-sum model misspecified by the divisor structure (N-a M4, N-d M1, M2, N-e m8) | CONFIRMED by computation (`exponent_fits.py`: residue-class exponents 4.06, 4.29, 4.61, 4.97; tangency at s = 2098) | Section 6.3 reduced to descriptive statements: Poisson model a weighting device, window and residue-class variation of q, the smoother cumulative and primitive counts, tangency at s ≈ 2100, holdout as two percentages of the exact count; "separate them a little", "slightly less well", the quasi-likelihood figure and the spreads removed |
| N6 | Theorem 3's constant is tiny; the dual family lies between X(log X)^2 and X(log X)^5 (N-c M2) | CONFIRMED (presentation) | After Theorem A: the constant 3/(128π^4) ≈ 2.4e-4, the crossover log X > 438 (`check_note.py` 7c), and the upper bound O(X(log X)^5) with "probably of that order" |
| N7 | The O(X(log X)^5) bound in the abstract is proved only in sketch (N-e M1; N-c m9) | CONFIRMED | New Proposition 4.5 (Integers: Proposition 4) with proof: independence of five of the six cubics, the anticanonical model, Picard rank 5, conic bundle, the sixteen lines and why positive triples avoid them, the height comparison, Browning–Sofos hypotheses, at most twelve points per pair, partial summation. `dual_delpezzo.py` |
| N8 | Sadek–El-Sissi numbering and hypotheses; Moreland–Zieve's correction (N-e M2) | ANSWERED IN PAPER for the numbering and hypotheses: the published Osaka version (fetched, review/literature-pass/_fetched/txt/sadekelsissi2015.txt) has Proposition 2.7, Theorem 2.8 and positive rationals, as the note cites; the arXiv v2 numbering differs. CONFIRMED for the correction | Clause added: the last hypothesis is absent from the first preprint, whose statements Moreland and Zieve showed false, counterexample (3,10,24) (checked in the fetched Moreland–Zieve text) |

## MINOR items (deduplicated)

| id | item | resolution |
|---|---|---|
| n1 | Remark 1 only a sketch (N-a m1, N-c m7, N-e m4) | complete proof for linear forms in two variables (lines, charges, two cases); the affine claim and the imprecise sentence dropped; Section 6.4 adjusted |
| n2 | Chen's "smallest"; the S = 408 chain incomplete (N-a m2, N-c m4, N-e m7) | "pairs at S = 18 and 20 are smaller"; the 408 chain completed by (51,102,255) |
| n3 | unit-fraction context (N-a m3) | Browning–Elsholtz 2011, Elsholtz–Tao 2013 |
| n4 | "new" for positive torsion (N-a m4, N-c m2, N-e m6) | softened; integer case stated (only Λ = 10) |
| n5 | DGGW numbers differ from the companion (N-a m5) | both are right: (5.7) is the general formula, (5.13) and Remark 5.16 the triangle case; no change |
| n6 | Schoen Prop. 7.1 (N-a m6, N-e m9) | the specific locator removed (source not accessible); general attribution kept, marked unused |
| n7 | descent data and Selmer terminology (N-a m7, N-b m1, m2, N-c m8, N-d m7, N-e m5) | integral model a = p^2 − 6pq − 3q^2, b = 16pq^3; Table 1 (Selmer groups and ranks, from the descent of `check_descent.py`, matching the referee's independent computation); vanishing of the corresponding Sha parts stated; LMFDB 90.c3 for C_{27/2} |
| n8 | hash bound (N-a m9) | e_2, e_3 ≤ (S/3)^3 ≤ 8·10^9 < 2^53 |
| n9 | "with Theorem B" (N-a m11, N-c m11, N-d m9) | "Theorem A is needed only for A(y) ≫ y" |
| n10 | Lemma 6 multiplicity (N-a m12) | covered by Proposition 4.5(iii) |
| n11 | Sadek–El-Sissi hypotheses (N-a m13) | see N8 |
| n12 | distinctness in Theorem 1(iv); Lemma 3 used only for its formulas (N-b m3) | added |
| n13 | "verified symbolically"; regular at ∞ (N-b m4) | the program named; the μ = 1/Λ model and orders of Δ, c_4 given |
| n14 | fibre types on the blown-up surface (N-b m5) | stated |
| n15 | torsion column of Table 2 from Theorem 1 (N-b m8) | stated with the four values (`check_note.py` 9a) |
| n16 | smoothness of C_Λ (N-e m1) | proved (genus-one component) |
| n17 | Lemma 3 cited with Proposition 3 (N-e m3) | done |
| n18 | "six orderings" (N-c m10); "asymptotically" (N-c m6); q = 4.49 (N-d m5); one percentage base (N-d m3); Poisson as device (N-d m4) | done |
| n19 | companion colours (N-e m10) | removed |
| n20 | why a surface search is non-trivial (N-d m8) | one sentence |
| n21 | Theorem 1(i) wording (N-b P3); abstract "dual pairs and their multiples" (N-a P6) | done |
| n22 | not done: N-b m6, m7, m9, P1, P2, P5, P6; N-c m5, m12, P1–P5; N-d m1, m2, m6, m10, P1, P3–P5; N-e m11 (edition not in the fetched record), P1–P3; N-a P1–P5 | judged not worthwhile this round, or not verifiable; no correctness issue |

## Mathematical changes (each with its check)

1. Proposition 4.5 with proof — `theory/diophantine/dual_delpezzo.py`.
2. Remark 1 with proof.
3. Proposition 2.3: smoothness and the model at ∞.
4. Theorem 3.4(iv): distinctness.
5. Facts: integer Λ (9b), Bremner–MacLeod identification (9c), the classical dual identity (9d), the torsion column (9a) — `paper/arith/checks/check_note.py`.
6. Table 1 (Selmer groups) — `review/audit/diophantine/check_descent.py` (released as `checks/classes4800/check_descent.py`).
7. Section 6.3 numbers — `theory/diophantine/exponent_fits.py` (round-8 block).

Blind check: `blind-check-N/REPORT.md`.
