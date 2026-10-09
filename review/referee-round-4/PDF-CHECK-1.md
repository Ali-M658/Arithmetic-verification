# PDF-only check 1 (brief Part 4.2), 2026-10-09

An independent checker was given only the built PDFs of commit 83693d7 (Paper A 42 pp., supplement 17 pp.,
Paper B 25 pp., arithmetic note 12 pp.) and VERDICT-A.md / VERDICT-B.md. It had no sources, no change logs
and no web. Page numbers are printed PDF pages; "S p." is a page of the supplement. The dispositions of
its findings are in "Response" at the end and in the two ROUND4-CHANGES.md files (section "Close-out").

Spot recomputations by the checker (all agree with the PDFs): Paper A Thm 3.8(ii)/(iv) examples (M = 3:
C = 120, (ν(2),ν(3)) = (-16, 9), s = -2, areas 12π; M = 4: C = 2520, (28, -27, 8), s = 2, areas 36π;
M = 2, X = 4: (w1, w2, w4) = (1/45, -1/36, 1/180), C = 180, (10, -4), s = 2, areas 6π); Example 3.6; (0;5,5,5)
against (0;2,2,2,10); the torsion points and discriminant 2^18 3^8 5^6 of E in Thm 5.8; d, d' in S7. Paper B:
every t_1 of Table 3 (row 2: 6.8486e-9); every D(A, ε, M) of Tables 2-4 from Lemma 4.2, Lemma 4.3 and
Thm 4.4; the six signatures of area π/2 with orders <= 12; Lemma 3.3's d_2 = -1/12; the ratios of Table 6.
Note: (S+R-2)/12 for c_2; N(S)/S² = 0.0094 at 400 and 0.0040 at 6000. No mathematical error was found.

## Counts

| | resolved | partial | unresolved | cannot tell |
|---|---|---|---|---|
| Paper A (40 items) | 31 | 8 | 1 (A2) | 0 |
| Paper B (30 items) | 23 | 6 | 1 (n17, optional) | 0 |

## Paper A

| ID | status | pages | justification |
|---|---|---|---|
| A1 | RESOLVED | 3-5 | headline leads with Thm 1.1 (PTE growth), Thm 1.2 (M+1), Thm 1.3 (Theorem B, Descartes), Thm 1.4(iii) (isolation); "What is elementary and what is not"; conic literature p. 5 |
| A2 | UNRESOLVED | whole | 42 pp. (body to p. 33, data statement p. 34, appendices pp. 34-37, references pp. 38-42) against 39 in round 4 and a target of about 30; supplement 14 -> 17 pp. |
| A3 | RESOLVED | A 4; B 4-7 | B uses A's proofs; B Table 1 lists shared results, stated without proof |
| A4 | RESOLVED | 1, 3-4, 15-17 | Thm 3.8(iii) K_mult <= min(M+1, 2d_O+2, floor(Area/π)+4); (iv) M+1 attained; abstract says so. The bound is now numbered Theorem 3.8 (Lemma 3.7 is the sign-change lemma) |
| A5 | RESOLVED | 5, 10, 25 | Uçar credited for the induction (Thm 3.40 and proof, pp. 98-103) |
| A6 | RESOLVED | 9, 36-37 | Prop. 2.7 (6), Prop. B.2 enveloping remainders |
| A7 | RESOLVED | 4, 31 | stability sentence corrected |
| A8 | RESOLVED | 32-33; S 14 | Cor. 6.5 stated and proved (not mentioned in the introduction's §6 paragraph) |
| A9 | RESOLVED | 1, 10 | curvature -1 in the abstract |
| A10 | PARTIAL | 7 | notation table present; lettered and numbered theorems mixed; overloaded symbols (n4) |
| n1-n3 | RESOLVED | 3, 17, S 8 | |
| n4 | PARTIAL | passim | κ, C, M, T still overloaded |
| n5 | PARTIAL | 14-32 | captions short; marks keyed in the text, not the captions (as the paper's caption rule requires) |
| n6-n16 | RESOLVED | | |
| n17 | RESOLVED | 40 | DOI corrected (faithfulness of paraphrase: cannot tell from PDF) |
| n18, n19, n21-n24, n26, n30 | RESOLVED | | |
| n20 | PARTIAL | 21, 42; S 16 | McKean correction and Wróblewski added; only one part of Ostrowski's two-part memoir cited |
| n25 | PARTIAL | 34 | maintainer named; DOI is a placeholder |
| n27 | PARTIAL | S 1-2, 6 | the 38 collision-free sums not cross-cited to the arithmetic note |
| n28 | PARTIAL | S 4 | Table S1 gives the L = 5 genus area only approximately |
| n29 | PARTIAL | 31-33 | App. D duplication removed; the sharp certificate stays in the supplement |

## Paper B

| ID | status | pages | justification |
|---|---|---|---|
| B1 | RESOLVED | 1, 3, 14-16 | no form of "certify"; inputs (i)-(v) p. 14; residual: systole lower bounds computed in floating point, "not interval arithmetic" (p. 15), called "bounds" without qualifier in the abstract and p. 3 |
| B2 | RESOLVED | 1, 3, 16 | "all ten ... 18 to 847", consistent with Table 6 |
| B3 | RESOLVED | 14-16 | §7.1, t-grid, (C1)/(C2), Table 5 |
| B4 | RESOLVED | 4, 22 | prior-work paragraph; Buser's book cited only on p. 10, not in the paragraph; Judge, Schoen-Wolpert-Yau absent |
| B5 | RESOLVED | 4-7 | disclosure Table 1, no reproved shared result |
| B6 | RESOLVED | 1, 3, 20 | "below any level above 1/4" |
| B7 | RESOLVED | 2-3, 12 | the evaluation paragraph is printed twice on p. 12 |
| B8, B9 | RESOLVED | 10-22, 18 | |
| n1-n4, n6-n11, n13, n18, n21 | RESOLVED | | |
| n5 | PARTIAL | 12 | Table 3 has no t_2, Γ_*, Λ columns; ε = 1.8626 for both triangle rows unexplained |
| n12 | PARTIAL | 19-22 | no remark that σ_* = 0.562 is weak |
| n14 | PARTIAL | 2 | no reference for continuity of λ_j on moduli space or the δ compactness step |
| n15 | RESOLVED | 24-25 | DOI fixed (Mumford Cor. 3: cannot tell from PDF) |
| n16 | PARTIAL | 5-11 | Γ, L, K overloaded |
| n17 | UNRESOLVED (optional) | 10 | not adopted |
| n19 | PARTIAL | 13, 18, 21 | Fig. E3: hues of the two triangle orbifolds not keyed; open M = 3 diamonds hidden under the filled ones |
| n20 | PARTIAL | 23 | DOI placeholder |

## Editorial checks

- Paper A 42 pp. against about 30 (fail); abstract about 171 words against about 150 (fail).
- Every figure caption in A, B and the note has at most two sentences; all figures present and cited.
- floor(A/π)+4 is Cor. 1.5, but also appears in Thm 1.1(i) as the upper bound for f(A).
- "Certif-": none in Paper B; in Paper A only for the exact-arithmetic certificate (pp. 32, 33, 37) and in
  the supplement for rigorous statements.
- Table 6 of Paper B, row ϑ = 1.6, M = 3, prints "> 4424" with no estimate though the caption promises one.
- Visible "[PLACEHOLDER: ...]" text: Zenodo DOI, author contributions, AI-use statement (A pp. 34, 37; B p. 23; note p. 11).
- Data statements name a path "review/round1-fixes/..."; Paper A cites the arithmetic note as "in preparation".
- No "??", "[?]", margin overruns or broken symbols.

## Response

See the "Close-out" sections of `paper/jga/ROUND4-CHANGES.md` and `paper/eigen/ROUND4-CHANGES.md`.
