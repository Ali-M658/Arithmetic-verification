# VERDICT-B (round 10): "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (AGAG)

Inputs: the five reports of Panel B (README.md). Length remarks are excluded.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| B-a editor (spectral geometry) | send to review; major revision | high (correctness), about 0.6 (level) |
| B-b (trace formula) | minor revision | high |
| B-c (Weyl laws, tails) | minor revision | high (correctness), medium (significance) |
| B-d (computer-assisted proofs) | minor revision | high |
| B-e (rigour, citations) | minor revision | 4/5 |

There is no FATAL item and no mathematical error.
- B-a, B-c, B-d and B-e independently reproduced all of Tables 2–5, the certificate of Proposition 6.5 and the triangle rows of Table 8.
- B-d recertified Tables 3 and 4 in Arb and calls Proposition 6.5 a valid computer-assisted proof.
- B-b matched the coefficients (1) with Uçar's closed forms for l ≤ 5.

**Stop condition: not met before the fixes** (confirmed MAJOR items). This was the one extra round the authors authorised; after the fixes and the fix check, the loop ends for this paper.

## FATAL and MAJOR items

| id | item (reviewers) | status | resolution |
|---|---|---|---|
| B1 | Value of the main theorem beyond bookkeeping; what is new as mathematics (B-a M1, B-c M2, B-b M1 part) | CONFIRMED (presentation) | Add a computable form: for every (A,ε,M) the certified procedure of Cor. 6.4 succeeds at t = t_* (Theorem 6.2's estimates give its hypotheses with Θ = Θ_*), so N and δ are computable by a terminating certified procedure. "What is new" restated: the diameter-free count (Lemma 4.5) presented as a crude auxiliary count; the integrality gap (Lemma 3.3); the enveloping remainders; the necessity results; Prop. 6.5 named as the usable statement, together with what it needs (complete, index-wise enclosed spectra). Cite the trace-formula bootstrap literature (Kravchuk–Mazáč–Pal; Bonifacio; Fortier Bourque–Petri) after verifying the records |
| B2 | Lower and upper bounds in M compared at different accuracies (B-a M2, B-c M1) | CONFIRMED | Corollary 8.5 is stated as a constraint on the pair (N, δ). The text says that at δ = M^{−c} the bound is vacuous and that no N at fixed δ is given (existence at fixed δ is open). The abstract juxtaposition and the last sentence of Remark 8.6 are rewritten |
| B3 | The area bound is also necessary (B-a M3) | CONFIRMED by proof | New proposition with proof: for every ε, M, N and δ there are two closed hyperbolic surfaces in C(∞, ε, M), of different genus, whose first N eigenvalues agree to within δ. The proof uses Cheng's comparison λ_k ≤ λ_1^D(B(d/2k)) (fetched and cited at statement level), diameter → ∞ with genus, surfaces of systole ≥ ε in infinitely many genera (finite covers of one such surface, by residual finiteness, with verified citations), and pigeonhole. The open-question sentences (pp. 4–5) and the abstract are revised: the order and area bounds are necessary, and the systole question is open |
| B4 | Section 7 determines nothing; completeness depends on the signature; accuracy paragraph misstated (B-a M4, B-d M2) | CONFIRMED in part | The "accuracy needed" paragraph is rewritten around the weighted hypothesis, with a feasibility estimate checked by script: about 6e-5 relative at row 2 under Weyl's law, against 2e-8 for the uniform δ. "Practical size" is softened. The completeness comparison is stated signature-free: at t = 0.0015 exactly one σ of area π/2 and orders ≤ 12 is within the budget. Section 7 is reduced to one clause in the abstract. A rigorous enclosed instance is not done (new numerical analysis) and is said to be within reach |
| B5 | Certificate checkable from the paper; protocol details; code availability (B-d M1, B-a M5, B-e m8) | CONFIRMED | `certified_gap.py` writes the enclosures of J(t) and E_m(t), 2 ≤ m ≤ M, at the six times, with radii, to a new data file. `make_tables.py` prints them as an appendix table. The certification paragraph states that t is an exact decimal rational, the integration tolerances, and why the integrands are holomorphic on the balls used. The data statement already archives the code |
| B6 | Overlap with the companion and the relation to Uçar not precise (B-b M1, B-a M5) | CONFIRMED (presentation) | The theorem headers cite the internal proofs, with one pointer to the companion. Each shared statement's primary home is named. One sentence says that (1) coincides with Uçar's (4.33)–(4.35) at curvature −1, and the novelty of Prop. 2.3, Lemma 3.3 and Thm 3.2(i) is stated explicitly |
| B7 | Size of the constants is partly an artefact of a-priori k_*, γ_* (B-b M2, B-c m1) | CONFIRMED (presentation) | Remark 6.6 qualifies the explanation of the size of the constants and states the gains available: exact first-difference data over Sig(A,M), the infimum over s in the tail, the exact factor in B_*, and the individual δ_k t^{k−2}. Proposition 6.5 is the class-exact route |

## MINOR items

Applied where worthwhile and verifiable; the fix log lists each: B-a m1–m3, m5–m9, m12–m14, P1, P3, P6; B-b m1 (as a remark), m2, m3, m4, m5, m7, P2, P4, P5; B-c m2, m3, m5, m6, P1–P5; B-d m1–m9, P2, P3; B-e m1–m6, m9, P1, P2, P5, P6. Not done: global renaming of symbols, figure redesign, and the Remark 6.6(c) recomputation of Table 8.
