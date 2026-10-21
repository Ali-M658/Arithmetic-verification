# VERDICT-N (round 9): "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

Inputs: the five reports of Panel N (README.md). Length remarks are excluded.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| N-a editor (elementary number theory) | send to review; major revision | about 0.75 |
| N-b (elliptic surfaces, Mordell–Weil) | minor revision | high (correctness), moderate (contribution) |
| N-c (rational points on surfaces) | minor revision | high (correctness), moderate (overall) |
| N-d (experimental mathematics) | minor revision | high |
| N-e (rigour, citations, house style) | minor revision | high (mathematics), moderate (inaccessible citations) |

No FATAL item. Every referee reproduced the enumeration (all of Table 3, the triple totals to S = 6000), the ranks, torsion, conductors, root numbers and the descent data; N-b and N-d recomputed the Selmer groups and images independently.

**Stop condition: not met** (confirmed MAJOR items remain before the fixes, and the editor's M1, Choudhry's paper, cannot be resolved here). Round 9 is the fourth and last round for the note; see "What blocks" below.

## FATAL and MAJOR items

| id | item (reviewers) | status | resolution |
|---|---|---|---|
| N1 | Choudhry 2011, the one parametric prior work on the same system, unread (N-a M1, N-c M1, N-e M1) | CONFIRMED; NOT RESOLVABLE here | OpenAlex lists it as open access (bronze) at Project Euclid; the PDF request was again answered by the publisher's bot challenge (round 9, fifth attempt), and no browser may be used. The note says only that the paper has not been consulted (an earlier wording about scripted retrieval was removed after the fix check, as unsuitable for a published text). Action for the authors (submission checklist): read it in a browser and settle whether it contains the dual or isosceles family; if it is quadratic in three variables, Question E and Section 6.4 change |
| N2 | The justification for Proposition D is misleading; dimension-growth context (N-a M2, N-c M2, N-e m2) | CONFIRMED (presentation) | Paragraph rewritten: the S² scale comes from the five trivial planes x′ = σ(x), each with about S² points, so no bound for all points can be o(S²); a saving must come from points off them, the setting of the determinant method; not carried out. No citation added (none verified this round); the optional S²(log S)^C sharpening not done |
| N3 | Section 6.4 claims less than it can and misstates the scope of its search (N-c M3) | CONFIRMED in part | Added: a single curve contributes at most X^{1+o(1)} (d ≥ 2 in two variables; d = 1 by Remark 1), so only families sweeping out a surface bear on Question E; the line search tested only the bidegree (1,1) components of the (3,3) correspondence, and the result is stated as such. The proposed lemma (quadratic surface ⇒ N ≫ X^{3/2}) and the Calabi–Yau/Fujita framing not added |
| N4 | The out-of-sample evidence is misdescribed ("do not separate"); the quantity of Question E is not tabulated (N-d M1, M2) | CONFIRMED by computation | `exponent_fits.py` round-9 block: second holdout (fits on [600,3600], predict 3601–4800): +0.21% vs +2.32%; A(1000) = 4141, A(2000) = 12 512, A(4000) = 35 567, A(4800) = 46 254, local exponents 1.64, 1.60, 1.51, 1.48 (asserted; N-d's values). Text: the holdouts do separate the laws on this range; weak, non-asymptotic evidence for a positive answer; A(X) and its local exponents quoted |
| N5 | Theorem C is essentially BGN p. 119 plus Schinzel (N-b M1) | CONFIRMED (presentation) | Theorem 4's discussion now credits BGN for the odd multiples and calls the theorem a direct consequence of their observation and Schinzel's argument, recorded with an explicit curve; not demoted from the list of results |
| N6 | The elliptic-surface framing omits the Mordell–Weil fact (N-b M2) | CONFIRMED | Added: the surface is extremal; Shioda–Tate 10 = 2 + r + (5+2+1+0) gives rank 0, the sections are the six base points; further families need base changes, such as Λ = 2t + 5 + 2/t and Λ = (r+1+1/r)² (torsion) or base changes of positive rank |
| N7 | Sadek–El-Sissi numbering and hypotheses (N-e M2) | ANSWERED IN PAPER (the published Osaka version, fetched, has Prop. 2.7 and Thm. 2.8 over positive rationals, as cited) | Added the arXiv numbering (Prop. 2.6, Thm. 2.7, over integers; checked in the fetched v1 and v2) |

## MINOR items (deduplicated)

| id | item | resolution |
|---|---|---|
| n1 | cross-reference to the companion's isolation theorem (N-a m1) | Theorem 5.10 (the number after this round) |
| n2 | Lemma 4 wording (N-a m3, N-b m5) | "the base points; and, when …, all twelve torsion points" |
| n3 | log 2 (N-a m4, N-c m10) | done |
| n4 | rational point on Y (N-a m6, N-c m6, N-e m5) | Y contains D(x) for every positive triple, e.g. x = (1,1,2) |
| n5 | smallest pairs (N-c m1) | pairs at S = 31, 32 added (enumerated: 18, 20, 26, 31, 32, 34, …) |
| n6 | IEEE bound for S ≤ 4800 (N-d m1) | 4.1·10^9 for S ≤ 4800, 8·10^9 for S ≤ 6000, with the correct-rounding sentence |
| n7 | coprimality in Theorem 2's proof (N-e m1) | proved |
| n8 | erratum clause (N-e m7) | what it corrects, and that (5.7) is unaffected |
| n9 | Γ_0(6) citation scope (N-b m10, N-e m8) | citation moved to Γ_0(6) |
| n10 | 155/12 not in Table 2 (N-e m9) | separated |
| n11 | "at most twelve points" clause (N-c m9, N-e m6) | removed |
| n12 | "Theorem B is needed only" (N-c m3, N-e m10) | "only Theorem 2 is needed" |
| n13 | ord c_4 wording (N-b m2) | "c_4 not vanishing at μ = 0" |
| n14 | not done: N-a m2, m5, m7–m12, P1–P5; N-b m1, m3, m4, m6–m9, m11, P1–P6; N-c m2, m4, m5, m7, m8, m11, m12, P1–P5; N-d m2–m11, P1–P5; N-e m3 (unverified reference), m4, m11, m12, P1–P8 | judged not worthwhile this round or not verifiable here; no correctness issue |

## Mathematical changes (each with its check)

1. Mordell–Weil rank 0 of the surface (Shioda–Tate) — text; blind check.
2. Coprimality in the proof of Theorem 2 — text; blind check.
3. Second holdout and A(X) — `theory/diophantine/exponent_fits.py` (round-9 block).
4. Smallest pairs — enumeration (exact, S ≤ 40), recorded here.

`paper/arith/checks/check_note.py --enum`: 43 checks, 0 failures. Blind check: `blind-check-N/REPORT.md`: items 1–7 and 9 correct (A(1000) and its exponent, and every Table 3 row up to 1000, reproduced exactly); it asked for the step |MW| = 6 (added: unimodular Néron–Severi lattice, |MW|² = 6·3·2·1), "trivial subvarieties" for "trivial components", the bidegree claim qualified (lines through base points have lower bidegree; the diagonal and coordinate permutations excluded), and a sentence that the two holdouts share training data. All fixed.

## What blocks the note after four rounds

- **N1 (Choudhry 2011).** The editor makes reading it a condition, and three referees ask for it. It cannot be read by scripted access, and no browser may be used. Another review round would raise it again. Reading it is the first item for the authors.
- Every other confirmed item of this round is resolved or presented accurately.
