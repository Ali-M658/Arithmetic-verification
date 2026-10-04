# SELF-REVIEW: independent check of the compiled PDF

A separate reviewer was given only the compiled PDF (read through `pdftotext` and page
renderings, not the LaTeX source), together with `review/audit/THEOREM-REGISTER.md`,
`review/audit/G5-VERDICT.md`, `theory/CONVENTIONS.md`, `review/audit/PRIORITY.md` and
`review/audit/THEOREM-A-PRIOR-ART.md`. It was asked to match every numbered result to its register
row, check statements, hypotheses, status and proofs, check every G5 SERIOUS and MINOR item,
check that excluded material is absent, and recompute explicit numbers.

## Outcome

- Every numbered result maps to a register row, except remarks and commentary that state no new
  result (listed under N1). No proved result was found mathematically wrong.
- All G5 hypotheses of item 7 are present; SERIOUS items 1-4 and changes 5-10 are satisfied,
  apart from the findings below.
- None of the excluded material appears (conj:density, the birthday heuristic, any c S^2 claim,
  "stabilizes", the localization sentence, rem:ncone, rem:bugfix).
- More than 25 numbers and identities were recomputed exactly (threshold gaps and S*(p) for
  p = 2..29, all rows of the overlap and enumeration tables, the n = 4 witness, d_3, d_4, d_5,
  c_iso, the density counts to S = 1000, the 38 collision-free sums, the fibre table, the
  Weierstrass model and the 12 torsion points, the stability constants and table ratios, the
  blind-recovery roots). No mismatch.

Counts: 1 BLOCKING, 6 FIX, 16 NOTE.

## Findings and resolutions

| id | page | finding | resolution |
|---|---|---|---|
| B1 | 2 | Abstract: "two coefficients suffice exactly when the cone orders sum to at most 17" reads as an iff, false for sums 19, 21-25, ... (G5 item 8, row 14). | **Fixed.** "two coefficients determine every orbifold whose cone orders sum to at most 17, and they first fail at sum 18, on the pair ...". |
| F1 | 42 | N(S) not said to count unordered pairs (G5 SERIOUS 1). | **Fixed.** Section 8, first paragraph: "unordered pairs of distinct triads". |
| F2 | 4-5 | The "known only through the full spectrum" sentence lacks Dryden-Strohmaier Prop. 3.3 (PRIORITY.md wording). | **Fixed.** Cites Thm 1.1 and Prop. 3.3, and Ucar Thm 3.40, Cors 4.21(iv), 4.23 in the same sentence. |
| F3 | 43 | Prop. 8.3 calls the reduced dual pair a "primitive degeneracy pair", but hyperbolicity after reduction is not shown (row 94). | **Fixed.** Now "a primitive pair of distinct triples with a common sum and a common reciprocal sum", whose copies kD, k >= 4, are hyperbolic degeneracy pairs by (19); "primitive pair" is defined at the start of Section 8 (N13). |
| F4 | 45 | "so its count is X(log X)^{O(1)}" stated as fact, unproved. | **Fixed.** Stated as an expectation: "one expects counts of order X(log X)^{O(1)}, though we do not prove this". |
| F5 | 52-53 | Publisher address prints "???" for three entries. | **Fixed.** Locations from the fetched records: London (Crossref), Philadelphia, PA and Cambridge (zbMATH Open records fetched as evidence; SOURCES.md). The bibliography has no BibTeX warnings and no "???". |
| F6 | 38 | Table 2 footnote records an earlier internal error (like rem:bugfix). | **Fixed.** Footnote removed; the caption says only that the (2,2,2,2,3) upper bound comes from the audit's better-converged search. |
| N1 | various | Remark 3.2, Remarks 4.13, 6.1, two computed ranges, have no register row of their own. | Kept. Remark 3.2 is Step 1 of the register's proof of Theorem B (TRACE.md); the others are commentary or numbers traced in TRACE.md §2. |
| N2 | 11-12 | p(z) for the polynomial with roots -m_i clashes with p (least order), p_l. | **Fixed.** Renamed chi_m(z), as CONVENTIONS.md prescribes. |
| N3 | various | T, D, E reused. | Kept: each is local to its proof or section and defined there. |
| N4 | 21 | Rotation index l in Theorem 4.6. | **Fixed.** Now j, as CONVENTIONS.md prescribes. |
| N5 | 22 | Lambda used as an eigenvalue cutoff. | **Fixed.** Now x. |
| N6 | 34 | H(m-hat) clashes with H_k. | **Fixed.** Now Had(m-hat). |
| N7 | 37 | r is both the residual and the test radius in Prop. 6.10. | **Fixed.** The test radius is now varrho_0. |
| N8 | 13-14 | varpi_r (row coefficients) and varpi_n (Jacobian constant) share a symbol. | **Fixed.** The Jacobian constant is now bar-varpi_n. |
| N9 | 19, 24 | Trace-formula route called "a third proof" and "not an independent proof". | **Fixed.** Now "a third argument ... a consistency check". |
| N10 | 29 | Theorem 5.13 includes a computed list of collision-free sums. | Kept: G5 item 8 asks for this wording in the theorem; the proof says the list comes from the exhaustive enumeration. |
| N11 | 46 | "falls steadily" while the table rises from 1.9544 to 1.9935 between 400 and 500. | **Fixed.** "falls overall". |
| N12 | 10 | Kokotov (row 82) not cited for the flat case. | Kept: no remainder claim is made; the vanishing follows from Ucar's factor K^l, which is cited. |
| N13 | 43 | "Primitive pair" used before definition. | **Fixed** (see F3). |
| N14 | 2 | Abstract's "never do" is proved only near distinct reals. | **Fixed.** "near any n distinct positive reals the first n-1 of these quantities never do". |
| N15 | 27 | Weak reason for the global minimum of c_2. | Kept: the sentence states the value and that it is a fixed-sum versus global distinction; no claim depends on it. |
| N16 | 31, 50 | Table 1 pair column printed in italic without spaces; stacked fractions overlap; loose lines on p. 50. | **Fixed** for Table 1 (pairs as separate formulas joined by "and"; x*(p) as a/b). The loose lines are the class's justification of a paragraph with long URLs and are left. |

Expected placeholders noted by the reviewer and not defects: TODO-CAPTION figure boxes on nine
pages; PLACEHOLDER text for the author contributions, the AI-use statement and the Zenodo DOI.

After the fixes the manuscript was rebuilt (BUILD.md): no errors, no undefined references or
citations, no overfull boxes, no BibTeX warnings.
