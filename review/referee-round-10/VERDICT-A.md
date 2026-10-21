# VERDICT-A (round 10): "How much of a hyperbolic orbifold does heat hear?" (AGAG)

Inputs: the five reports of Panel A (README.md). Length remarks are excluded.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| A-a editor (global analysis) | send to review; major revision | high (correctness), moderate (significance) |
| A-b (parametrices, Donnelly) | minor revision | high (about 0.85) |
| A-c (power sums, PTE) | minor revision | high (correctness), moderate (significance) |
| A-d (triangle groups) | minor revision | high |
| A-e (dependencies, citations) | minor revision | moderate (about 0.7) |

There is no FATAL item and no mathematical error. Every reviewer reproduced its sections independently: the coefficients, Theorem 3.11, Table S1, Theorem 5.9, the descent of Appendix F with LMFDB 90.c3, Remark B.6 and Table S4. A-b checked Lemma E.1 step by step and found it correct.

**Stop condition: not met before the fixes.** Every referee recommends minor revision and the editor sends the paper to review, but the MAJOR items below were confirmed. This round was the one extra round the authors authorised; after the fixes and the fix check, the loop ends for this paper.

## FATAL and MAJOR items

| id | item (reviewers) | status | resolution |
|---|---|---|---|
| A1 | Significance and depth for AGAG; analytic vs combinatorial content (A-a M1, A-e M1, A-c "limitations", A-d M1) | CONFIRMED (presentation) | Introduction: a paragraph that separates the analytic results (signed remainders, optimal truncation, Prop. 2.14 with Lemma E.1, Prop. 2.17) from the algebra of odd power sums. Prop. 2.17 (counts are a constant-curvature phenomenon) and Cor. 3.12 promoted among the main results |
| A2 | Title answers itself; abstract opens with caveats (A-a M2, A-e P7, A-c m1) | CONFIRMED | Retitled "How many heat invariants determine a hyperbolic orbifold?" (authorised by the authors). Abstract rewritten: question, theorems, one caveat; "is equivalent to" for the growth statement; the triangle-only scope of "isolated" |
| A3 | Heterogeneity; Section 6 thin, and its link to the trace unusable; Prop. S3.1 used but only in the supplement (A-a M3, A-d M2) | CONFIRMED in part | Section 6 reframed in its opening paragraph as the stability of the algebraic recovery map, with the end-to-end numbers of Remark B.6 for the minimal pair stated there. Prop. S3.1 brought into Appendix C. No section moved |
| A4 | Overlap with the disclosed manuscripts (A-a M4) | CONFIRMED (presentation) | §1 states the status of the companion and the note (simultaneous preprints). Theorem 5.10 is proved here, and the note cites it. The reverse reproof is in Paper B's Appendix A (Paper B's verdict) |
| A5 | Variable-curvature headline rests on the flat-cone mechanism; the conjecture is kept apart (A-a M5, A-e m10) | CONFIRMED (presentation) | Abstract and §2.4 state the mechanism plainly: an exactly flat cone point contributes only to c₂. Conj. 2.13 is labelled as unused and separate from the proved statements |
| A6 | Per-point identification of the trace-formula cone terms with Donnelly's b_l(p) used in §2.4 (A-b M1, m2) | CONFIRMED | §2.4 states that it uses Donnelly's locality [DGGW Thm 4.8] and Uçar's per-point computation [Uçar Thm 4.20] for the per-point identification. The claim that no result rests on locality is restricted to Sections 3–6 |
| A7 | Duhamel steps of Props 2.14 and 2.17(ii) between the localised T and a global trace (A-b M2) | CONFIRMED | Lemma E.2 (new), with proof: for g_ε = e^{2εψ}\|dx\|² and χ = 1 on a neighbourhood of supp ψ, ∂_ε^i T(0,t) is the i-th Dyson term up to O(t^∞), i = 1, 2. Blind-checked |
| A8 | Missing classical literature; overstated analytic novelty (A-b M3) | CONFIRMED | Cite Branson–Gilkey–Ørsted 1990, Gilkey's monograph and Berline–Getzler–Vergne, with fetched records; ω_n presented as a re-derivation, compared with BGØ; the novelty list reworded (Prop. B.2 not listed first) |
| A9 | Main-text statements resting on the companion [3] (A-e M2) | CONFIRMED | Remark 2.6, the diameter-free form of Prop. 4.2(a) and the ℓ₀ of Remark B.6 are marked as taken from [3] and removed from the lists of what is new; Remark B.6 says that any ℓ₀ ≥ 0.01 gives the same numbers and that no theorem uses it |
| A10 | PTE attribution: Wright/Wooley inconsistent, Hua omitted, [4] not quoted exactly; "whether f grows like a power" (A-c M1) | CONFIRMED | Paragraph rewritten from the fetched Croot–Mao–Yip §1 (P(k,2), W(k,m), Hua), with [4] quoted from a fetched copy or not quoted verbatim; p. 4 rephrased ("which power", given c√A ≤ f(A) ≤ A/π+4) |
| A11 | Problem 5 open; Section 5 elementary (A-d M1) | CONFIRMED (presentation) | Option (c): "four invariants against all of Sig" is presented as the main geometric result of §5; the general-p strata results are marked as structural |

## MINOR items

Worthwhile minor and presentation items are applied as listed in the fix log. They are: A-a m1, m2, m3 (Suleymanova, if verified), m5, m7; A-b m1, m3–m8, m10, m11, P3, P4; A-c m2–m5, m7, m9, P1, P5; A-d m1–m8, m11, m12, P3, P5; A-e m1–m9, m11, P3, P5, P8. Not done: symbol renaming across the paper (A-b P1, A-c P2, A-d m7 renaming), figure redesign (A-a P4, A-e P1, P4), and moving sections.
