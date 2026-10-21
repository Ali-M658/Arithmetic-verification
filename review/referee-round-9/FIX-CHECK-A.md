# FIX-CHECK-A (round 9): does A-r9final resolve VERDICT-A?

Materials used: `main/scratch/A-r9final.pdf` (63 pp.), `main/scratch/A-r9final-supp.pdf` (19 pp.), `VERDICT-A.md`.
Page numbers below are printed page numbers. "S p." means a supplement page.
Recomputations are in `fixcheck-A/scratch/`: `cvals2.py` (a9), `b3.py` (Remark 2.16(b), eq. (8)), `remB6.py` (a13 and the rest of Remark B.6), `b4.py` (Prop. B.4).

**Numbering.** The PDF numbers several items differently from VERDICT-A. VERDICT "Prop. 2.16(ii)/(iii)" is **Prop. 2.17(ii)/(iii)** in the PDF; "Remark B.5" is **Remark B.6**; "Theorem 5.5 for general p" is **Theorem 5.6**; "Fig. 6(a)" (one geodesic) is **Fig. 4(a)**. Inside the PDF, every cross-reference I checked points to the right object. No "Proposition 2.16" is left that should point to the obstruction proposition; Remark 2.16 is now "Computed coefficients" and is cited correctly on p. 16.

## Summary

- All 11 MAJOR items and 34 of the 35 MINOR items are RESOLVED in the PDFs. a26 is PARTLY RESOLVED: the Fig. 8 caption labels its curves wrongly.
- **A2:** resolved as far as the paper can go. The gap itself remains, as VERDICT says; the paper now states it openly.
- **No wrong numbers.** Every number I recomputed agrees: a9, a13, the rest of Remark B.6, Remark 2.16(b), Prop. B.4, Prop. 5.2, Thm 5.9, Fig. 7/Table S3 and the δ ratios on p. 47.
- **New problems:** five small ones (N1–N5 below). The most visible is N1: the proof of Proposition 2.14 now comes after Remark 2.15. The most substantive is N2: one sentence on p. 18 relies, without saying so, on Prop. 2.14 for l ≥ 3.

## MAJOR items

| id | verdict | where | notes |
|---|---|---|---|
| A1 | RESOLVED | p. 16–17; S7, S pp. 15–16 | The outline is now Section S7, with "It is not a proof" and no proof symbol (checked on the rendered S p. 16). The paragraph before Conj. 2.13 separates the proved parts (linear part, Prop. 2.14 "for l ≥ 3 granting Remark 2.15"; constant curvature, Prop. 2.8 with [19, Thm 4.20]) from the conjectured ones (three items). It says the first open step is Donnelly's theorem as stated in DGGW 4.2 and that two remain. Fursaev "derived, by a physical argument" (p. 7–8, p. 16). The S7 algebra checks out: β_{l,l+1} = (2l)!/l!·K^l at constant curvature, and a linear part of 2/(l−1)! agrees with Prop. 2.14. |
| A2 | RESOLVED (presentation); the mathematical gap stays open, as VERDICT says | p. 17 (Prop. 2.14, Rem. 2.15), p. 19–20 (Prop. 2.17(ii)) | T(ε,t) is defined (localised integral) and the parametric form is stated precisely as an unproved assumption. Prop. 2.14 is conditional for l ≥ 3 and unconditional for l ≤ 2 (DGGW (4.4); Schueth Thm 4.1). In Prop. 2.17(ii), "for L ≥ 4 grant…"; the proof uses only Ω_1…Ω_{L−2}, says "for L ≤ 3 only G_1 is used, and the parametric form is not needed", and handles L = 2 separately. The conditional marking is audited below. |
| A3 | RESOLVED | p. 5–6, p. 48 | §1 now says the Lipschitz/Hölder statements concern the recovery map on real orders and that the geometric content is the integer threshold, reached only at times computed spectra do not resolve. Cor. 6.5 uses δ_thm only; δ_cert is the paragraph after it, which cites Prop. S3.1. Remark B.6 (p. 54) and S5 refer to "the paragraph after it" consistently. |
| A4 | ANSWERED (as stated) | Abstract p. 1; p. 3 | The abstract says the invariants describe diffusion only as t → 0. Title unchanged. |
| A5 | RESOLVED | p. 7 ("What is new, in brief" (a)–(c), "Theorem 1.2 settles no growth exponent"); p. 6; p. 9 | Prop. 2.8 is "a self-contained derivation … with signed remainders (the cotangent sums … classical, Fursaev's c_n(α) the same sums)". Lemma B.3 is "Darboux's method". "Theorem 3.15 is proved by Descartes' rule" (p. 9). |
| A6 | RESOLVED | p. 53 (Prop. B.4); p. 37 | The statement and proof are correct: I checked each step, and `b4.py` tests the inequality for m = 2, 3, 5, 8, 12 (lhs/rhs ≤ 0.37, with C = sup φ_k/(A_m x^k) ≤ 1.62). The heuristic sentence on p. 37 is replaced by "Truncated at K = ⌊π²/(µ²t)⌋ … error O(t^{−1/2}e^{−π²/(µ²t)}) (Proposition B.4)". Orders below µ are covered by the monotonicity in B.2(a), as stated on p. 53. |
| A7 | RESOLVED in this PDF; the note itself was not in my materials | p. 9, p. 44 | The isolation theorem is Theorem 5.10 here (p. 44), and p. 9 calls it that, so a citation "[Theorem 5.10]" in the note would be correct. I could not open the note to confirm its citation. Overlap paragraph p. 7 unchanged (editorial). |
| A8 | RESOLVED | p. 4; p. 30 | "This is the quantity P(k,2) of [5, §1] … W(k,2), and N(k) ≤ W(k,2)". Pigeonhole bound for P; Wooley for W; "Wright …, whose problem is the variant W(k,2), so … a fortiori"; "monotonicity … about P(k,2)". The inequality direction is correct. |
| A9 | RESOLVED | p. 40 (Cor. 5.3); p. 5 (Thm 1.4(i)); abstract | Proof: max(3,4) = 4 ≤ L = 4 in Thm 3.7. The second clause ("≤ 3 for all exactly when the system has no solution") is proved. |
| A10 | RESOLVED | p. 48–49 (Problem 5); p. 40 (Prop. 5.2) | p, q, r ≥ 2. The automatic-hyperbolicity argument is correct: R(p,q,r) = 1 triads give 1+S ∈ {10, 11, 12} ≠ 8. Scaling equivalence with witnesses ("entries at most 220, fewer than the searches after Prop. 5.2"). Disjointness is added and proved (|U*|+|V*| ≤ 6 < 8). |
| A11 | RESOLVED, with one new error (N3) | p. 43 | "Both theorems can be checked directly on the 83 hyperbolic triads with 10 ≤ S1 ≤ 18" (recount: 83, matching Table S3). "Theorem 5.6 for general p and Proposition D.1 are structural results". |

## MINOR items

| id | verdict | where | notes |
|---|---|---|---|
| a1 | RESOLVED | p. 11, Lemma 2.4 | γ, γ^{−1} counted separately unless they coincide (order 2). |
| a2 | RESOLVED | p. 30 | "the 2026 preprint [5, §1]"; no "2026 paper" left. |
| a3 | RESOLVED | p. 40 | Case list and values recomputed: 1 + 6/x; 10/6, 11/12, 12/30 for x = 3, 4, 5; all < 9. |
| a4 | RESOLVED | p. 16 | Δ = −div grad of the metric itself, (−Δ)^{l−1}K has the sign of ∂x²+∂y², and "the coefficients of Remark 2.16 refer to this convention". It is consistent with u2 = (K² − ΔK)/15 (S p. 18). |
| a5 | RESOLVED | p. 20 | Jacobian displayed (a generalised Vandermonde); range Ω_1…Ω_{L′}, L′ = L−2; E is "O′ … minus the same for O". The choice w0 + Σ_s^{−1}E on O and w0 on O′, shrunk by s, gives difference E (checked). L = 2 is "nothing to adjust". |
| a6 | RESOLVED | Abstract; p. 4; p. 15 | "The counts are not stable outside constant curvature". |
| a7 | RESOLVED | p. 42–43, Thm 5.9 | "the unique pair of least area"; proof checked: (0;2,2,2,3) area π/3, (0;2,2,2,4) area π/2, triangle partners would need (8, 5/6) or (9, 3/4), both < 9. |
| a8 | RESOLVED (already present) | p. 26–27 | "An exhaustive computer search … we claim no minimality for other M." |
| a9 | RESOLVED | p. 26 | Recomputed (`cvals2.py`): C = Dq gives 6, 120, 2520, 362880 for M = 2…5, with q = 2 only at M = 2. The examples on p. 26–27 also check: (ν(2),ν(3)) = (−16, 9), s = −2, area 12π; (28, −27, 8), area 36π; areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} for M = 2…9; (iv) with M = 2, X = 4 gives w = (1/45, −1/36, 1/180), C = 180, ν = (10, −4), s = 2. "likewise in (iv)" is explained. |
| a10 | RESOLVED | p. 28, Lemma 3.14(c) | "W being U if g ≤ g′ and V otherwise". |
| a11 | RESOLVED | p. 20, Prop. 2.17(iii) | Collar, cylinder in the fixed piece, "numbers of cone points … may differ". |
| a12 | RESOLVED | p. 47, Prop. 6.4 | "\|d_i\| < a"; used in Σd²(3a+d) ≥ 2aΣd². |
| a13 | RESOLVED | p. 54, Remark B.6 | Recomputed (`remB6.py`, exact Vandermonde, Q_3 = 303.63). Row bounds: δ1 = 1138.6τ; τ_max = 3.34e−10; η_max(τ = 1e−11) = 4.61e−19. Uniform bound: 4858τ, 7.82e−11, 2.07e−19. N = 8: δ_thm met up to τ = 3.597e−3, η ≤ 5.00e−13 at τ/2; δ_cert met up to 1.540e−2, η ≤ 1.32e−8. All match the text. Also arccosh(cot² π/8) = 2.4485 and D = 4.897. |
| a14 | RESOLVED | p. 54 | "an a-priori bound on the orders of whichever orbifold's trace is read". |
| a15 | RESOLVED | p. 8, p. 16 | "Dowker gave a simpler derivation of Fursaev's second coefficient"; "Fursaev derived, by a physical argument". |
| a16 | RESOLVED | p. 31 | Sandwich sentence after Prop. 3.19. |
| a17 | RESOLVED | p. 33 | "3 − 3P1(V)R(V) ≠ 0, as P1(V)R(V) ≥ 25 by … arithmetic and harmonic means". |
| a18 | RESOLVED | p. 32 | Narrow ansatz stated; T(4) = 10 would need shape (5,5) of type (−1,1,3,5) or shape (4,6). |
| a19 | RESOLVED | p. 23; S p. 2 | "101 of the 107 admit a pencil splitting". |
| a20 | RESOLVED | p. 4 | "the smaller systole, that of O(3,3,12)": 1.8626 < 2.2568, ℓ²/4 ≈ 0.87, (π/12)² ≈ 0.07. |
| a21 | RESOLVED | p. 37 | "give the cone coefficients b_l(m) as the finite combinations (5)". |
| a22 | RESOLVED | p. 34 | "a hyperbolic triangle is determined up to isometry by its angles". |
| a23 | RESOLVED | S p. 10 | "dihedral group of order 2k". |
| a24 | RESOLVED | S p. 14 | Slice argument given, including that the isometry is an involution (σ² = id). |
| a25 | RESOLVED | S p. 11 | Bolza/C_8 = O(2,8,8), χ = −2/8 (χ(O(2,8,8)) = −1/4 checked); 3.838887258842 against 3.83888725884220. |
| a26 | **PARTLY RESOLVED** | p. 43 (Fig. 7), p. 35 (Fig. 4), p. 47 (Fig. 8) | Fig. 7 caption: "the circles, which hide the dots for p = 2, 4" matches the image. Fig. 4(a): "each with one shortest closed geodesic" matches. **Fig. 8:** the caption now names four curves, but says "for three multisets of orders (solid)". In the rendered figure (4,4,4) is dashed and (2,8,8) is a heavy coloured line, as the text below says: "(2,3,7) (solid), (2,8,8) (heavy) and (4,4,4) (dashed)". Fix: "for (2,3,7) (thin), (2,8,8) (heavy) and (4,4,4) (dashed), and … (dotted)". |
| a27 | RESOLVED | p. 5 (Thm 1.3(ii)), p. 28 (Lemma 3.14), p. 29 (Thm 3.15) | L ≥ 2 throughout. |
| a28 | RESOLVED | p. 8 | Gittins wording as in VERDICT. |
| a29 | RESOLVED | p. 44 | "which they state for integer Λ and whose argument holds verbatim for every rational Λ". |
| a30 | RESOLVED | p. 14, Remark 2.10 | "[19, Cor. 4.19(ii), (4.33)–(4.34); Thm 4.20]". |
| a31 | RESOLVED | p. 9–10 | "[9, Def. 3.1 with the Gauss–Bonnet theorem, Thm 3.2]"; "[2, (5.8)] … [2, (5.11)–(5.12)]". |
| a32 | RESOLVED | p. 12, p. 14 | "Uçar's all-order formulas"; "(where, we add, Prop. 5.5 and (5.10) are also used)". |
| a33 | RESOLVED | p. 14–15 | The erratum adds a hypothesis to Thm 5.1 (trivial Iso^max) and does not affect (5.7). |
| a34 | RESOLVED | p. 37; S p. 12 | 3.4 × 10^{−14}, consistent in both places. |
| a35 | RESOLVED | p. 51 | "equivalently, by the Paley–Wiener theorem, for even entire h of exponential type with the usual decay". |

## Is every use of Prop. 2.14 (l ≥ 3) and Prop. 2.17(ii) (L ≥ 4) marked conditional on Remark 2.15?

Every **statement** of these results is now marked:
- Introduction p. 6 ("granting a parametric form … (Proposition 2.14, Remark 2.15)"; "the same first L for every L under the same assumption")
- §2.4 p. 16 ("for l ≥ 3 granting Remark 2.15")
- the statement of Prop. 2.14 (p. 17)
- Remark 2.15 itself
- the second sentence after the proof (p. 18, "granting Remark 2.15 when l ≥ 3")
- the statement of Prop. 2.17(ii) and its proof (p. 19–20)
- the echo on p. 21 ("for L ≥ 4 granting Remark 2.15").

Uses of Prop. 2.17(iii) (abstract, p. 4, p. 21, Problem 6(c)) need no condition, and none is given.

Still unmarked:
1. **p. 18, first sentence after the proof** (new problem N2): "So from order t² on, the cone term is not a multiple of K(p)^l: by Proposition 2.14 its linear part contains Δ^{l−1}K(p)". For l ≥ 3 this needs λ_l ≠ 0. Only the conditional value 2Π_{l+1}/(l−1)! gives that; the unconditional part of Prop. 2.14 only gives some number λ_l(m). For l = 3 it is supported independently by Remark 2.16(b) (computer algebra), and for l ≤ 7 by 2.16(c). Suggest: "by Proposition 2.14 (for l ≥ 3 granting Remark 2.15) its linear part …".
2. **Novelty lists, p. 6 (l. "the linear part of the cone terms in variable curvature (Proposition 2.14) are new") and p. 7 ("What is new, in brief" (a)).** These mention the result without the qualifier. They are mentions, not uses. Adding "(for l ≥ 3 conditional, Remark 2.15)" in (a) of p. 7 would make the novelty list consistent with the rest.

The machine-check sentences of Remark 2.16 (p. 18) "agree with Proposition 2.14" only as checks; they do not use it.

## New problems introduced by the changes

- **N1 (layout, p. 17).** Remark 2.15 sits between the statement of Proposition 2.14 and its proof, so the block headed "Proof" reads as the proof of Remark 2.15. Move Remark 2.15 before Prop. 2.14 or after its proof, or head the proof "Proof of Proposition 2.14".
- **N2 (conditional marking, p. 18).** See item 1 of the audit above.
- **N3 (wrong statement, p. 43).** "the main results need only the strata with S ≤ 18, so p ≤ 5". The triad (6,6,6) has S = 18 and R = 1/2, so it is a hyperbolic triad in stratum p = 6. Strata up to p = 6 occur (my enumeration: least orders 2–6 among the 83 triads, and (6,6,6) is in Table S3). Write "p ≤ 6", or "adjacent pairs p, p+1 with p ≤ 5".
- **N4 (caption, p. 47).** Fig. 8 line styles; see a26.
- **N5 (wording, p. 48).** "the thresholds δ_cert quoted below rest on it". δ_cert values are also quoted *above* (the Fig. 8 discussion on p. 47 and the diamonds in Fig. 8). Suggest "the thresholds δ_cert quoted in this paper".

Typography (minor):
- p. 54: "and at τ = 10^{−11} η ≤ 4.6 × 10^{−19}" runs two formulas together; insert a comma or "we need".
- Abstract: "reduces to one Diophantine system in four orders". The system has seven unknowns (p, q, r and a, b, c, d); "in four orders" probably means "for a rival with four cone orders" and could be rephrased.

## Checked and found consistent

- Remark 2.16(b): (`b3.py`) reproduces the K³ coefficient as p3(m)/m. The Δ²K coefficient equals Π_4(m) = λ_3 for m = 2, 3, 5, 7, 12. −m⁵ΔK/15120 is the top term of −2Π_3. β_{1,2}, β_{2,3} and β_{3,4} agree with Conj. 2.13(ii).
- Eq. (8): p0, p1, p2 match (4)–(5).
- Prop. 2.14 proof (p. 18): the signs and constants of the Duhamel computation give λ_l = 2C^{−2l−2}/(l−1)!. At l = 1 this matches p1/m.
- Prop. 2.17(ii) example: (0;2^8) and (0;3,3,3) both give 2/3, with χ = −2 and 0.
- Table S3 (83 triads) and Theorem 5.8/5.9 at S = 18.
- p. 47: δ_up/δ_thm ranges from 539 to 1.86e8 across Table S4 ("about 5e2 to 2e8"), and δ_up/δ_cert from 1.03 to 6.72.
- Prop. 6.3/6.4: 498 + 42a² and δR = s²/(4(64−s²)).
- No "2026 paper" remains.
- No dangling references to VERDICT-era numbers (2.16(ii), B.5 as a remark, Lemma B.4) remain in the PDF.

## Follow-up (main session)

Fixed after this check: Remark 2.15 moved after the proof of Proposition 2.14 (N1); "So from order t² on …" marked as granting Remark 2.15 for l ≥ 3 (N2), and the "what is new" lists of §1 qualified likewise; "so p ≤ 6" (N3); the Fig. 8 caption no longer labels the three multisets "(solid)" (N4); "δ_cert quoted in this section" (N5); "it needs η ≤ …" on p. 54; the abstract's "one Diophantine system". The numbering differences against VERDICT-A (Prop. 2.16 → 2.17, Remark B.5 → B.6, Theorem 5.5 → 5.6, Fig. 6 → Fig. 4) come from the items inserted this round; VERDICT-A uses the numbering of the reviewed PDF.
