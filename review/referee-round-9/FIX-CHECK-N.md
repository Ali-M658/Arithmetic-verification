# FIX-CHECK-N (round 9): "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

Materials: `main/scratch/N-r9final.pdf` (25 pages) and `VERDICT-N.md`, nothing else. I rendered pages 1–5, 8, 13 and 21–23 with pdftoppm and searched the rest with pdftotext. My recomputations are in `fixcheck-N/scratch/`: `enum.py` is an exact enumeration of all admissible triples for S ≤ 999 in rational arithmetic, and `iso.py` counts the isosceles family. No packages were needed.

## Summary

All 7 major items and all 13 minor items have a visible change in the PDF.

- **19 items resolved.** One of them, N2, resolves the misleading justification and leaves the optional citation undone, which the verdict says.
- **N1 (Choudhry) is not resolved and cannot be resolved here.** The note now says honestly that the paper was not consulted.
- **No wrong number found.** Every number I could recompute matches.
- **Two small new issues.**
  1. The "five planes" sentence on p. 4 leaves out the diagonal. This disagrees with the "six … orderings of P itself" on p. 23.
  2. The wording "every scripted retrieval was refused" on p. 5 is odd in a journal article.

## Major items

| id | verdict | where | notes |
|---|---|---|---|
| N1 Choudhry 2011 | NOT RESOLVED (not resolvable here; presented accurately) | p. 5, lines after "[10, Appendix A.5.1], [11]" | The text reads: "We have not been able to consult Choudhry's paper: it is listed as open access on the publisher's site, but every scripted retrieval was refused, so we cannot say whether his family is, or contains, the dual family or the isosceles family below." This is accurate. On wording: a referee or editor will read "scripted retrieval" as an odd admission and will ask why nobody opened it in a browser. Before submission the authors must read the paper (it is open access) and replace this sentence with a real comparison. If his family is quadratic in three variables, Question E and Section 6.4 change. |
| N2 Prop. D justification | RESOLVED (presentation). The citation and the S²(log S)^C sharpening are not done, as the verdict says. | p. 4, paragraph after Proposition D | Rewritten as the verdict describes: trivial subvarieties, the planes x′ = σ(x) with about S² points each, so no bound o(S²) is possible for all points, and the determinant method is named but not carried out. **New issue (minor):** the text says "the five planes x′ = σ(x), σ a non-identity permutation". The diagonal x′ = x (σ = identity) is just as trivial and also carries about S² points. Section 6.4 (p. 23) says "six of them consist of the orderings of P itself". "Five … non-identity" should be "six … σ a permutation", or the text should say why the identity is left out. Also, "about S² integer points" is loose (about S²/2 ordered triples); "of order S²" would be exact. |
| N3 scope of Section 6.4 | RESOLVED | pp. 22–23 | Added: "a single curve contributes at most X^{1+o(1)} pairs (a family of degree d ≥ 2 in two variables gives about X^{2/d}, and d = 1 is excluded by Remark 1), so that only families of curves that sweep out a surface … bear on Question E". The search is now stated as limited to the bidegree (1,1) components of the (3,3) correspondence, with lower bidegree for lines through base points and with the diagonal and coordinate permutations excluded (the blind-check fixes are present). The text also says plainly that no surface search was done. The proposed lemma and the Calabi–Yau framing were not added, as the verdict records. |
| N4 out-of-sample evidence; A(X) | RESOLVED | p. 21 (Section 6.3), pp. 21–22 (Section 6.4) | "Do separate them on this range" now appears, with N(6000) − N(4800) = 42 960 (checked: 145 679 − 102 719). The two holdouts are reported as +0.25% vs +2.33% and +0.21% vs +2.32%, and the text says they share training data. The A(X) values and their local exponents are quoted, and the evidence is called "weak, non-asymptotic evidence for a positive answer". **Checked:** A(4800) = 46 254 matches the 46 254 primitive pairs on p. 19. log₂(12512/4141) = 1.595 and log₂(35567/12512) = 1.507 agree with the quoted 1.60 and 1.51. My enumeration gives A(500) = 1328, so log₂(4141/1328) = 1.640, which agrees with 1.64. The 1.48 at 4800 needs A(2400), which is out of range; not checked. A(999) = 4138 here, consistent with A(1000) = 4141. The A exponents are below N's (1.79, 1.71, 1.62, 1.60), as stated. Minor point: "A fixed power over-predicts every forward window" rests on two windows; "both" would be more exact. |
| N5 Theorem C credit | RESOLVED | pp. 16–17 (opening of Section 5) | "with Proposition 1, the theorem then follows from any curve C_Λ with a positive point of infinite order, so it is a direct consequence of their observation and Schinzel's argument, which we record with an explicit curve." BGN p. 119 is credited. The remark after Theorem C on p. 4 credits only Schinzel. That is acceptable, but adding "and Bremner–Guy–Nowakowski's observation [3, p. 119]" there would keep the two places consistent. |
| N6 Mordell–Weil fact | RESOLVED | p. 8, proof of Proposition 2 | The surface is called extremal. Shioda–Tate gives 10 = 2 + r + (5+2+1+0), so r = 0 (over Q̄(Λ)). Unimodularity gives \|MW\|² = 6·3·2·1, so the order is 6 and the sections are the six base points. Base changes are given: Λ = 2t + 5 + 2/t and Λ = (r+1+1/r)². **Checked:** ord Δ = 2, 3, 1 at Λ = 0, 1, 9 and 6 at ∞, so the fibres are I₂, I₃, I₁, I₆ and the components minus one are 1, 2, 0, 5, which is correct. Solving 2t² + (5−Λ)t + 2 = 0 for Λ gives 2t + 5 + 2/t, which is correct. 36 = 6², which is correct. |
| N7 Sadek–El-Sissi numbering | RESOLVED | p. 5; pp. 11–12 | "[26, Proposition 2.7 and Theorem 2.8] (in the published version; Proposition 2.6 and Theorem 2.7 in the arXiv versions, stated there for integers)". The later citations on pp. 11–12 use the published numbering, which is consistent. |

## Minor items

| id | verdict | where | notes |
|---|---|---|---|
| n1 companion cross-reference | RESOLVED | p. 18 | "[17, Theorem 5.10]". I could not verify this against the companion, which was out of scope. |
| n2 Lemma 4 wording | RESOLVED | p. 12 | "the base points; and, when the torsion is Z/12 with G = (1 : r : r²) and r < 0, all twelve torsion points." |
| n3 log 2 | RESOLVED | p. 1 (abstract), p. 3 (Theorem B), p. 13 | The constant 3 log 2/(2π²) renders correctly in all three places. c_iso = 0.105346, as I checked. |
| n4 rational point on Y | RESOLVED | p. 16 | "Y(Q) ≠ ∅, as Y contains D(x) for every positive triple x, for instance x = (1, 1, 2)." |
| n5 smallest pairs | RESOLVED | p. 5 | The pairs at S = 31, {(4,9,18),(5,6,20)}, and S = 32, {(4,14,14),(5,7,20)}, were added. **Checked:** the R values are 5/12 and 11/28. The first class sums are 18, 20, 26, 31, 32, 34, 35, 36, and these are the only classes at S = 31 and 32. |
| n6 IEEE bound | RESOLVED | p. 19 | e₂, e₃ ≤ (S/3)³ ≤ 4.1·10⁹ for S ≤ 4800 (1600³ = 4.096·10⁹) and 8·10⁹ for S ≤ 6000. The correct-rounding sentence is present. |
| n7 coprimality in Theorem 2 | RESOLVED | p. 13 | The proof is correct. A common prime p of (2u+v)/g and (u+2v)/g must be 3 and forces g = 3. Then 9 divides 3(u+v), so 3 \| u+v, and with u ≡ v (mod 3) this gives 3 \| u. Since gcd(u,v) = 1, primitivity follows. |
| n8 erratum clause | RESOLVED | p. 2 | "the erratum [15] adds a hypothesis to their Theorem 5.1, for strata whose group Iso^max is trivial, and does not affect this formula". It says what the erratum changes and that (5.7) is unaffected. |
| n9 Γ₀(6) citation | RESOLVED | p. 3 | "[30, Table 2]" now directly follows "the elliptic modular surface of Γ₀(6)". |
| n10 155/12 not in Table 2 | RESOLVED | p. 17 | "The torsion column of Table 2, and the torsion of the curve C_{155/12} of Theorem 4, also follow". **Checked:** the four values (Λ−1)(Λ−9)·den² are 6721, 1449, 1 329 601 and 8569, which are correct and not squares. |
| n11 "at most twelve points" | RESOLVED | — | The phrase no longer occurs. The remaining "twelve points" in Lemma 3 (p. 10) is a different, correct statement. |
| n12 "only Theorem 2 is needed" | RESOLVED | p. 4 | Present. |
| n13 c₄ wording | RESOLVED | p. 8 | "c₄ not vanishing at µ = 0". |

## Numbers recomputed (all agree)

- **Table 3 rows X = 18, 100, 200, 300, 400, 500 and 600.** I checked N, N_cl, primitive classes and largest size exactly. The local exponents at 100, 200, 300, 400, 500 and 600 come out 2.524, 2.069, 2.007, 1.954, 1.993 and 1.868. From the table values, the exponents at 1000, 2000, 4000 and 6000 come out 1.790, 1.713, 1.624 and 1.585.
- **N(X)/X².** 0.0094 at 400 and 0.0040 at 6000.
- **Class-size totals.** 96 981 + 1627 + 122 + 11 + 1 = 98 742 = N_cl(4800). The pair total is 96 981 + 3·1627 + 6·122 + 10·11 + 15 = 102 719 = N(4800).
- **Primitive pair types.** 7626 + 4 + 38 624 = 46 254, which gives 16.5% dual and 83.5% neither dual nor torsion.
- **Small-range counts.** 507 of the 582 sums with 19 ≤ S ≤ 600 carry a primitive class. 32.9% of primitive pairs are dual for S ≤ 200. There are 669 non-dual primitive pairs with S ≤ 400 and 1330 with S ≤ 600. The two classes at S = 36 are as stated.
- **Isosceles family.** There are 506 pairs D_{u,v} with S ≤ 4800, against c_iso·4800 = 505.66, which rounds to 505.7. The copies number 0.608X at X = 4800. (count − c_iso X log X)/X is −0.2860, −0.2862 and −0.2863 at X = 10⁴, 10⁵ and 10⁶, consistent with −0.286.
- **Theorem 3 constant.** 3/(128π⁴) = 2.406·10⁻⁴. The crossover c_iso/that = 437.8 matches "log X > 438". The chain c_A = (1/6)(3/(2π²))(3/π²)(1/8) = 3/(32π⁴) is correct.
- **Fit crossover.** q/ln s = β with q = 4.49 and β = 0.587 gives s ≈ 2098, matching "s ≈ 2100".

## New problems introduced

1. **p. 4 versus p. 23: "five planes … non-identity permutation" versus "six … orderings of P itself".** The diagonal x′ = x lies on the same threefold, carries about S² points and is equally trivial. Fix: "the six planes x′ = σ(x), σ a permutation of the coordinates".
2. **p. 5, "every scripted retrieval was refused".** This is accurate but unsuitable as published text, because it shows the paper was never opened by a person. It is a placeholder for the authors' own reading (N1), not a final sentence.
3. **p. 21, minor wording.** "over-predicts every forward window" refers to two windows.

I found no broken references, no "??", no overfull text and no mismatch between the tables and the text on the pages I rendered. Typography is clean on pp. 1–5, 8, 13 and 21–23.

These are not new, but are still in the file: the placeholders for the Zenodo DOI (p. 23), the author contributions and AI-use statements (p. 24) and the companion preprint identifier ([17], p. 25), plus the empty "Received / DOI" fields on p. 1, which belong to the journal.

## Follow-up (main session)

The three new problems were fixed: p. 4 now speaks of the six planes x′ = σ(x), the diagonal among them, each with of order S² points; p. 5 now says only "We have not consulted Choudhry's paper, so we cannot say …" (reading it remains the authors' first action item); p. 21 says "both forward windows".
