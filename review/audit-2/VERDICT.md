# G5-bis (theorem freeze for the PTE and revision results): verdict

## **FREEZE WITH CHANGES**

Every result below was re-derived from its statement alone by a reviewer who had not seen the
existing proof, scripts or data, and each reviewer then compared its derivation with the existing
material. Eight reviews were carried out: `pte-structure`, `pte-growth`, `pte-witnesses`,
`trace-formula`, `descent`, `stability`, `threshold-sharpness` (an extra group for Theorem 5.13 and
the sharpness wording) and `literature`.

- **FATAL findings: none.**
- **No theorem, lemma or proposition was found false.** Every printed constant in a theorem
  statement is correct.
- **Four SERIOUS findings.** Each is a printed sentence (three in the PTE material, one in the
  literature commentary); none is a proved result. Each must be changed before the text is frozen.
- All other findings are MINOR: missing hypotheses that the truth needs, wording, citations, and
  printed table entries.

Evidence: `REGISTER-ADDENDUM.md` (65 rows: 4 SERIOUS, 33 MINOR, 28 NONE), `<group>/REVIEW.md` (blind),
`<group>/COMPARISON.md`, and `check_*.py` with outputs (exact arithmetic, real asserts, nonzero exit).

## Required changes

### SERIOUS

1. **`statements.tex`, the opening of subsec:pte** (pte-structure PS.6).
   - "two orbifolds in Sig with different signatures share their first L heat coefficients exactly
     when the cancelled mirror multiset Z is an L-configuration" omits the genus condition. Counterexample:
     (2;15) and (0;3,3,5,5): Z = (-5,-5,-3,-3,1,15) is a 2-configuration but the areas differ.
   - Fix: "…exactly when Z is an L-configuration **with imbalance iota(Z) = 2(g'-g)**", and delete
     "=2(g'-g)" from the later definition of iota. `proof.md` section 1 already has the correct form.
2. **`statements.tex` ex:ptepairs, first item** (pte-witnesses PW.1).
   - "Previously the smallest area known to share three coefficients was 2 pi 14/5" contradicts
     Theorem C(3): the pair (0;3,10,15,30) ~ (0;4,5,21,28) of area 2 pi 22/15 is already its n=4 witness.
   - Fix: "This is the n=4 witness of Theorem C(3). Its area is less than that of the smallest
     genus-changing pair sharing three coefficients found here, (1;15,15,15) and (0;3,3,5,7,7,21), of area 2 pi 14/5."
3. **`proof.md` section 3, "Theorem C(3) at n=4 is a pencil phenomenon"** (pte-witnesses PW.3b).
   - False as a characterisation. Exhaustive search of 4-cone pairs with orders <= 440 gives 107
     primitive witnesses; 6 have no pencil splitting. Smallest: (0;16,16,74,74) ~ (0;11,37,44,88), with
     R = 45/296, P_1 = 180, P_3 = 818640.
   - Fix: "So the recorded witness of Theorem C(3) at n=4 is a pencil configuration. Not every witness is:
     (0;16,16,74,74) and (0;11,37,44,88) share R=45/296, P_1=180, P_3=818640, and their configuration admits
     no pencil splitting." In section 7, the "unproved converse" is now refuted by the same example (balanced size-8
     3-configurations without pencil splitting exist from entries 88); replace the paragraph accordingly.
4. **Wright and Melzak bounds** (literature B5/M1; `proof.md` section 0 item 2 and section 4, `statements.tex`
   rem:pteexponent, `LITERATURE.md`, `NOTES.md`).
   - "N(k) <= (k^2-3)/2 (k odd), (k^2-4)/2 (k even)" copies Borwein-Ingalls p. 7 accurately but is false for k=2,3
     (0 < N(2) = 3, 3 < N(3) = 4), and is not in Melzak. Melzak (p. 234) reports Wright's bound as K(n) <= (n^2+4)/2
     with n the degree. No index shift reconciles the two.
   - Fix: "The pigeonhole bound N(k) <= k(k+1)/2+1 [Hardy-Wright; BI Prop. 3] was improved by Wright (1935) to
     N(k) <= (k^2+4)/2 (as reported by Melzak, CMB 4 (1961), p. 234). Melzak gave an exact but non-constructive formula and
     numerical upper bounds for k <= 29 [ibid., Table 1]. None of these is o(k^2), and N(k)=o(k^2) remains open
     [BI section 6 Problem 3; Croot-Mao-Yip 2026]." In `statements.tex`, cite Prop. 3 with melzak1961 p. 234 and Table 1.
     Only commentary depends on it: the theorems use the pigeonhole bound, which was re-proved.

### Changed constants and printed values

| where | printed | correct |
|---|---|---|
| stability table, (2,2,2,2,3), delta_up and ratio | 5.743e-05, 7.26 (prose 7.3) | **5.312e-05, 6.72** (6.7). `threshold_output.md` already has it; `proof.md` l. 446 and `STATUS.md` l. 53 are stale. This is the same reprint G5 item 8 asked for |
| stability table, (3,10,15,30), delta_up | 7.488e-03 | 7.487e-03 (optional; printed value is a valid bound) |
| stability table, (2,3,7), relative precision nu=0 | 4.0e-03 | 3.9e-03 |
| claim after Table 4 (Prop 6.10) | "at most four nonzero (odd) coefficients" | odd series: at most four (z, z^3, z^5, z^7); even series sech^2 U, sec^2 U: at most four (1, z^2, z^4, z^6). sech^2 U for (2,2,2,2,3) = 1 - 121 z^2 + 9328 z^4 - 601472 z^6 |
| pencil counts (`proof.md`, `pencil_log.txt`) | "25 at entries <= 130, 61 at <= 220" | exact for |a|,|b|,|c| <= N with the fourth entry unrestricted; all-entries counts are 15 and 35 |
| n=5 pencil check | "1,592 primitive 5-sets with entries <= 200" | 1,592 counts sets with >=3 entries in [-200,200], A and -A separately; 602 have all entries in [-200,200]. "No pencil pair" holds in every reading |
| Theorem 4.2 | no range for L, beta | add L >= 2 in (a), beta > 0 in (b) |
| Proposition 3.2 | no n | add n >= 1 |
| Theorem 5.16 and the triad statement | "for every k" | every integer k >= 1 (k = 3/2 gives only (3,12,12)) |
| Theorem 4.3 | f_g, f_n undefined | define exactly; f_g(A) >= sqrt(A/16 pi) for A >= 16 pi, f_n(A) >= sqrt(A/12 pi) for A >= 8 pi |

### MINOR wording changes (replacement text is in each group's `REVIEW.md`)

- **Proposition 3.3 (doubling).** "1 in X minus Y" is false for multisets (X = {1,1,5}, Y = {1,3,3}: V contains a 1, cone counts
  differ by 1, not 2). State the counts 3n-mu_X and 3n-mu_Y; state that the pair shares its first L coefficients; cite |V| = 3n
  for the area bound, not Lemma 1.2(5) (that lemma concerns the cancelled configuration).
- **Theorem 3.4.** T^cone_L needs the cancelled genus-0 realisation hyperbolic (proved for L >= 3, checked at L = 2), the 1 surviving
  cancellation and X cap Y empty (minimality). The "[Sig] N(a)" citation for 2^{2L-1} should cite the construction.
- **Theorem 3.1 (pencil).** "Equivalently" clause: state e_k(A) = 0 for odd k < r together with prod_A - prod_B = kappa x^{m-k0}, kappa != 0
  (counterexample A=(-24,-15,-8,-5), B=(-20,-20,-6,-6)).
- **Lemma 1.2.** "U minus {1}" means remove every 1; the choice of genus and its existence; for L >= 2 the smaller genus is 0.
- **Theorem 2.1, statements.tex.** "Equality |U*|+|V*| = 2L+2 forces {L,L+2}" is misleading: equality in the inequality does not
  (example (2;40) ~ (0;4,4,5,8,10,10), shape {2,6}); only size 2L+2 does. Proposition (balanced): add 0 not in A.
- **Lemma 1.5.** N_odd(L) = L also holds at L=2; L=7 is not claimed (only 7 <= N_odd(7) <= 12).
- **Remark first open case.** "made primitive" -> "scaled to coprime integers"; "exist in abundance" -> "form a nonempty open set"
  (for integer 5-sides the rate is about 0.65%).
- **Improved lower bounds on f.** Replace the last paragraph by "Hence A_L/2 pi < 2L-3 and f(A) >= L+1 for A/2 pi >= 2L-3, 2 <= L <= 5.
  For L = 6, 7 the thresholds are A/2 pi >= 10 and 18."
- **Trace formula.**
  - Hyperbolic-term lemma: define systole over all hyperbolic classes including geodesics through cone points; "Orb in Sig" is a type
    error; write the proof (the fragment points to Theorem 4.9(b), which quotes the lemma) and the monotonicity line (bound decreasing in l, increasing in D)
    that justifies the smaller systole and larger diameter in Theorem 1.2(iii).
  - Schueth sentence: Schueth credits DGGW 5.6 with a_0, a_1 only; her Thm 4.1 gives the t^2 term; name p_0 and state b_l = (-1)^l p_l/m.
  - Ucar citation: add Thm 4.20(ii) (p. 138) beside (4.33)-(4.34); use kappa.
  - Remark 4.12: "independent of the coefficient computations"; delete "(or of Weyl's law)"; state the test-function class as h = g-hat, g smooth,
    even, compactly supported (the replacement argument via a test function with support shorter than the systole is in `trace-formula/REVIEW.md`);
    sentence (1B) must not be combined with `locality.tex`, which cites DGGW Thm 4.8 for both proofs.
  - Notation: the alpha_l of (H3) and alpha_{l+1}/(4 pi) here must not share a symbol.
- **Descent.**
  - phi is undefined at Z = 0: add phi(O) = origin, phi(1:0:0) = (216,5400), phi(0:1:0) = (216,-5400); give the nonsingularity argument.
  - The remark "the tangent at (16,400) meets E again at (16,-400)" is false: (16,400) is a flex. Write "meets E only at (16,400),
    multiplicity 3, so 2(16,400) = (16,-400) = -(16,400)".
  - Theorem 5.16: rank 0 from the descent (Cremona (3.6.2), n_1 = n_2 = 4, n_1' = n_2' = 1), torsion from reduction mod 7;
    PARI is a cross-check only; delete "(as far as tested)" (every isosceles point (u:v:v) has order 6). `novelty.md` and `RECOMMENDATION.md`
    still present PARI as the proof.
- **Stability.** Rename the Prop S5 data radii delta_nu (rho means three things); first-order term sum_c delta_c sum_l |p_c^(l)(a)/l!| r^l; state F = L;
  `threshold_output.md` prints eps_cert at 4 s.f. rounded to nearest (five rows then do not certify under the producer's own `certify`; the
  2-s.f. values in the paper's table do): format with `fmt_down`.
- **Threshold and sharpness.**
  - Theorem 5.13: add "the first two invariants determine S_1 (eq:s1inv), so a sum <= 17 can collide only within its own sum".
  - Abstract: "...while for the coefficients of positive real orders the sharp exponent is 1/2 at a double order and when all n >= 2 orders are equal"
    (for n = 1 recovery is Lipschitz).
  - Theorem 1.4: "...heat invariants of positive real orders it is 1/2, and sharp, at a double order (any n), and at an order of multiplicity k = n >= 3...".
  - Remark S3.3: "for real d_i >= -a (in particular |d_i| <= a)" and add max|d_i| <= ((498 + 42 a^2) delta/(2a))^{1/2}.
- **Literature.**
  - Borwein-Ingalls Prop. 1 is the three equivalent forms, not a bound; cite Hardy-Wright for the pigeonhole bound (Melzak credits it);
    `statements.tex` l. 26: N(k) is defined in section 2, p. 6, not section 1.
  - Type (-1,1,3,...,2L-3), L >= 4: "no numerical solution is listed" (the survey treats the type in its identities, e.g. Ex. 2.36, (3.33), (5.107)); the
    "33 types" sentence is in section 1.2.1, Ex. 1.7 (p. 16), and on p. 275.
  - Letac: cite BLP p. 2069 and CMSV p. 2 (Borwein-Ingalls say "Letac and Gloden"); the two-parameter family is BLP's reduction of Gloden's four-parameter solution.
  - Drop "no progress on questions 3 and 4" (Problem 4 was solved by Wooley 2012); optional footnote on the unrefereed Sun-Zhao preprint arXiv:2307.11330.
  - Bibliography: add DOI 10.1090/mcom/3917 to cmsv2024 and 10.1112/plms.12204 to wooley2019; melzak1961 is currently uncited.

## What held up

- Every PTE theorem (Lemma 1.2 with the corrections above; Theorems 2.1, 3.1, 3.4, 4.1, 4.2, 4.3; Propositions 2.2, 2.3, 3.2, 3.3) was re-proved.
  No counterexample to any of them was found by exact brute force (configurations up to size 12; pencil m = 4..10; doubling n = 2, 3).
- All 18 explicit pairs: both sides hyperbolic, exact equal areas, exactly L shared heat coefficients, computed from the coefficients themselves
  (cross-checked against Ucar for l <= 12), including the 7-vs-8 cone pair, the L = 3 same-genus pair of area 2 pi 22/15, and the L = 4..7 pairs.
- The 61 integer witnesses for Theorem A at n = 4: all valid, distinct, and the set reproduced exactly by an independent enumeration.
- The T_3 claim: an independent exact search over every 5-multiset Y <= 220 (4,493,032,544, primitive or not) finds no solution; planted controls are
  recovered through the full loop. A 16-prime modular filter was used, which can only reject. (The producer's own floating-point filter is
  certified only under an explicit error model; the conclusion no longer depends on it.)
- Lemma 2.5 for every order: p_l is an even polynomial, degree 2l+2, p_l(1)=0, leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)), p_l(m) > 0 for every real m > 1.
  The proof is a sum of positive rational multiples of m^{2n}-1. Exact for l <= 40, m <= 30. The closed form
  Phi_m(u) = (cot u - m cot mu)/(4m sin u) was verified three ways; agreement with Ucar holds for every l with no index shift.
- Theorem 1.2(iii): the constant C(A,l,D) re-derives exactly; the "attained" statement holds in all three cases.
- 2-isogeny descent: rank 0 unconditionally, torsion Z/2 x Z/6 with the twelve points; the corrected 3P.
- Proposition 6.10: every printed delta_cert, delta_thm and eps_cert re-certifies from the formulas alone (26,924 exact probes, 0 violations);
  every printed delta_up is a valid failure bound.
- Theorem 5.13 and the 38 collision-free sums (independent exact C search over S <= 4800).

## Priority-target verdicts

| target | verdict |
|---|---|
| PTE structure (Lemma 1.2, Thm 2.1, Props 2.2, 2.3, Thm 3.1, Prop 3.2) | **TRUE**; one SERIOUS sentence in `statements.tex` (genus condition) |
| PTE growth (Lemma 1.5, Prop 3.3, Thms 3.4, 4.1, 4.2, 4.3) | **TRUE**; hypotheses and wording to add; Theorem 4.1 unchanged |
| Witnesses of section 5 (18 pairs), 61 witnesses, T_3 | **CONFIRMED**; two SERIOUS sentences (14/5 and "pencil phenomenon"); the "open converse" of section 7 is refuted |
| Lemma 2.5, Phi_m, Ucar agreement, Remark 4.12, Thm 1.2(iii) | **TRUE**; Remark 4.12 wording and the hyperbolic-term proof to write |
| 2-isogeny descent, torsion, 3P | **CONFIRMED**, unconditional; one false remark (flex) and two missing definitions |
| Prop 6.10 and Table 4 | **Every printed delta_cert, delta_thm, eps_cert re-certifies**; (2,2,2,2,3) delta_up 5.312e-05, ratio 6.72 |
| Sharpness wording | **CORRECT with "positive real orders" and "all n >= 2 equal"** |
| Thm 5.13, 38 sums | **CONFIRMED** |
| Literature | **Wright and Melzak attribution FAILS** (SERIOUS); all explicit PTE solutions and Chen entries confirmed |

## Process notes and instrument gaps

**Process.**
- Statements were extracted verbatim by script (`build_statements.py`, anchors and no-proof asserts). One extraction error was found and fixed
  (Theorem 4.2 cut one line early in the pte-growth bundle; the reviewer reconstructed it, grades stand).
- Reviewers saw only their bundle and fetched sources until their blind verdicts were committed (4e4a802); the comparison phase was
  released afterwards (c21dda0). One instance of reading outside the release is recorded (pte-structure read 6 lines of
  `theory/signatures/proof.md` to resolve a citation; no grade affected).
- **One personal e-mail address was sent in a single request to the Unpaywall API (a free open-access lookup service) by the literature
  reviewer. It appears in no file on disk. Later requests used the placeholder research@example.com.**
- My pte-structure bundle described [Sig] Lemma 5 inexactly (the Newton parity statement, not a symmetry statement); no grade is affected.
- The pte-witnesses searches (T_3, 38 sums, 4-cone pairs <= 440) were run niced with checkpoints; the T_3 search covered the whole claimed range.

**Instrument gaps.**
- Borwein-Ingalls 1994 (e-periodica captcha, CECM 403): read from the scan in `theory/pte/sources` (hash matches `SHA256SUMS`), by the literature reviewer only;
  the other reviewers re-proved both bounds on N(k). The proposition numbering is confirmed only by that reviewer.
- Wright 1935 (OUP 403): cannot tell whether the Borwein-Ingalls formula is a misprint of Wright. Hua, Gloden, Letac, Chernick: not reached.
- Primary sources for Weyl's law on orbifolds, Hejhal, Iwaniec and Donnelly 1976: not fetched; no verdict relies on them (Donnelly is the standing gap).
- `paper/**` was not released to any reviewer, so wording in `main.tex` that repeats these printed values (for example "7.26", the Wooley/Wright sentence) was not checked.
- PARI/GP and Sage not installed: no PARI cross-check of the descent (none needed).

See `fetches.md` files in each group folder.
