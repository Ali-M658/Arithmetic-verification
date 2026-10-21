# VERDICT-A (round 9): "How much of a hyperbolic orbifold does heat hear?" (AGAG)

Inputs: the five reports of Panel A (README.md). Length remarks are excluded.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| A-a editor (singular heat asymptotics) | send to review; major revision | moderate–high (correctness), moderate (significance) |
| A-b (fixed-point heat kernel) | major revision | high (checked statements), moderate (novelty) |
| A-c (equal sums, analytic number theory) | minor revision | about 0.9 |
| A-d (hyperbolic polygons) | minor revision | high |
| A-e (proof completeness, citations) | minor revision | high (mathematics), moderate (significance) |

No FATAL item; no reviewer found an error in a proved statement or a recomputed number.

**Stop condition: not met** (A-b recommends major revision, and confirmed MAJOR items remain before the fixes). Round 9 is the fourth and last round for this paper; see "What blocks" below.

## FATAL and MAJOR items

| id | item (reviewers) | status | resolution |
|---|---|---|---|
| A1 | Conjecture 2.13 carried with a page-long derivation in outline ending in a proof symbol; its proved and conjectural parts not separated; Fursaev not credited for the symmetric structure (A-a M3, A-b M1, P2) | CONFIRMED | Outline moved to the supplement (new Section "Cone terms in variable curvature: a derivation in outline", no proof symbol). The paragraph before the conjecture now says what is proved (linear part, Prop. 2.14; constant curvature, Prop. 2.8 with Uçar), what is conjectured (non-symmetric germs; symmetric germs beyond Fursaev's physical derivation; the nonlinear part of β_{l,l+1}), and that the first of the three open steps (dependence on dΦ only through (I − dΦ)^{-1}) is Donnelly's theorem as stated in DGGW 4.2 (checked in the fetched DGGW text); two steps remain. Fursaev's "derived" (his own wording, fetched hep-th/9405143) |
| A2 | Exchange of limits (ε-derivative of the expansion) and the undefined trace in Prop. 2.14 and Prop. 2.16(ii) (A-b M2) | CONFIRMED; NOT FULLY RESOLVABLE here | The trace is now defined (localised integral T(ε,t), Remark 2.15). The parametric form of Donnelly's expansion (remainders twice differentiable in the parameter, uniformly) is stated precisely as an assumption that the paper does not prove; no source stating it could be found and verified (searched; none cited). Prop. 2.14 is now stated conditionally for l ≥ 3 and unconditionally for l ≤ 2 (DGGW (4.4) and Schueth's Theorem 4.1, which the reviewers also confirm); Prop. 2.16(ii) uses only Ω_1,…,Ω_{L−2} and needs the assumption only for L ≥ 4. This is a change of mathematics (a proved statement becomes conditional) and is reported |
| A3 | Section 6 overstates its geometric meaning; Prop. S3.1 is in the supplement although Corollary 6.5 used it (A-b M3) | CONFIRMED | §1 reframed: the Lipschitz/Hölder statements concern the recovery map on real orders; the geometric content is the integer threshold, reachable from the trace only at times computed spectra do not resolve. Corollary 6.5 now uses δ_thm only; the δ_cert version is a paragraph after it, citing the supplement's proof |
| A4 | The framing promises more than diffusion data can deliver; retitle (A-a M1) | ANSWERED IN PAPER in substance (abstract and §1 already state that the invariants describe diffusion only as t → 0 and that proved recoveries need very short times); the title is the authors' and is not changed. The editor's further request is addressed by the novelty list (A5) and by A6 |
| A5 | What is new must be stated sharply (A-a M2; A-b m1; A-c m5, m7) | CONFIRMED (presentation) | New paragraph "What is new, in brief" at the start of §1.2 (analytic / power sums / triangle orbifolds and arithmetic), with "Theorem 1.2 settles no growth exponent". Prop. 2.8 is called a self-contained derivation with signed remainders (cotangent sums classical; Fursaev's c_n(α) the same sums), Lemma B.3 Darboux's method; "Theorem 3.15 is proved by Descartes' rule" |
| A6 | The cone timescale e^{−π²/(μ²t)} is stated heuristically but provable (A-a M5) | CONFIRMED | Proved: new Proposition B.4 (optimal truncation): at K = ⌊π²/(m²t)⌋, |E_m − Σ_{l<K} b_l t^l| ≤ |b_K|t^K ≤ e^{2+π²/4m²} C A_m (π/m) t^{−1/2} e^{−π²/(m²t)}; the heuristic sentence in §4 replaced. `check_heat_supporting.py` §10 |
| A7 | Overlap with the companion; the note's cross-reference [Theorem 5.8] is wrong (A-a M4) | ANSWERED IN PAPER for the overlap (both papers declare the shared results and keep the proofs for self-containment, as decided in round 8; the editor's request to merge or de-duplicate is an editorial decision for the authors). CONFIRMED for the cross-reference | The note now cites Theorem 5.10 (the isolation theorem's number after this round's new corollary), read from the built .aux |
| A8 | N(k) must be pinned to the literature's notation (A-c M1; A-e m10) | CONFIRMED | N(k) is P(k,2) of Croot–Mao–Yip (fetched arXiv:2609.05061, §1: P(k,2) ≤ k(k+1)/2 + 1 by pigeonhole; Wooley's bound for W(k,2); N(k) ≤ W(k,2)); Wright's problem is the W variant, so his bounds hold a fortiori; monotonicity stated for P(k,2) |
| A9 | K_mult(triangle; Sig) ≤ 4 unconditionally (A-d M1) | CONFIRMED | New Corollary 5.3 with proof (Prop. 5.2 plus Theorem 3.7 with L = 4); Theorem 1.4(i) and the abstract updated |
| A10 | Problem 5 misstated (p,q,r positive instead of ≥ 2); scaling equivalence with witnesses; disjointness (A-d M2) | CONFIRMED | Problem 5 now has p,q,r ≥ 2, with the proof that such solutions are automatically hyperbolic; the scaling equivalence with n = 4 witnesses stated (the witness search covers only entries ≤ 220, less than the existing searches); disjointness {a,b,c,d} ∩ {p,q,r} = ∅ added to Prop. 5.2 with proof |
| A11 | Strata theory feeds no main result (A-d M3) | CONFIRMED (presentation) | Theorem 5.5 for general p and Prop. D.1 labelled structural; Theorem 1.4(i)–(ii) described as a finite verification on 83 triads made conceptual by the strata |

## MINOR items (deduplicated)

| id | item | resolution |
|---|---|---|
| a1 | γ and γ^{-1} counting (A-a m1) | stated in Lemma 2.4 |
| a2 | "2026 paper" (A-a m2) | "preprint" |
| a3 | Prop. 5.2 case list (A-a m3, A-d m1, A-e m2) | "{2,2,2,2,x} with x ≥ 2 and {2,2,2,3,x} with 3 ≤ x ≤ 5", values per family |
| a4 | sign convention of (−Δ)^{l−1}K; Δ²K convention affecting −42 (A-a m4, A-b m3) | stated: Δ = −div grad of the metric itself; the computer algebra (theory/varcurv/twisted_mp.py) uses this convention |
| a5 | Jacobian in Prop. 2.16(ii); only Ω_1..Ω_{L−2} needed; sign of E (A-a m5, A-b m5) | displayed; range reduced; E defined as O′ minus O |
| a6 | "constant curvature is essential" (A-a m6) | "the counts are not stable outside constant curvature" (abstract and §1) |
| a7 | uniqueness of the least-area pair (A-a m7, A-d m3) | Theorem 5.9 says "unique", with the added proof sentence |
| a8 | 12π/36π minimality marked computational (A-a m8) | already marked in the main text ("An exhaustive computer search … we claim no minimality for other M") |
| a9 | C by a formula (A-a m9); "likewise in (iv)" (A-c m6) | C = Dq; values 6, 120, 2520, 362880 checked against brute force for M = 2..5 |
| a10 | W in Lemma 3.14(c) (A-a m10) | "W being U if g ≤ g′ and V otherwise" |
| a11 | gluing in Prop. 2.16(iii) (A-b m4) | collar and cylinder placement stated; n, n′ may differ |
| a12 | |d_i| < a (A-b m6) | done |
| a13 | Remark B.5 with row bounds for N = 3 (A-b m7) | 1.14e3 τ, τ ≲ 3.3e-10, η ≤ 4.6e-19 added (`check_heat_supporting.py` §11) |
| a14 | μ_0 = 12 wording (A-b m8) | a-priori bound on the orders of whichever orbifold is read |
| a15 | Dowker computed nothing further; Fursaev "derived" (A-b m2, A-e m3) | corrected from the fetched hep-th/9406002 ("a simpler derivation of Fursaev's expression") |
| a16 | sandwich N(2L−2) ≤ 4N(2L−3) vs doubling (A-c m1) | sentence added |
| a17 | 1 − e_1R ≠ 0 in Remark 3.22 (A-c m2) | P_1(V)R(V) ≥ 25 by AM–HM, stated |
| a18 | size-10 search scope (A-c m3) | narrow ansatz stated; the two shapes T(4) = 10 needs |
| a19 | "all but six … one family" (A-c m4) | "101 of the 107 admit a pencil splitting" |
| a20 | which systole ℓ (A-c m8) | "the smaller systole, that of O(3,3,12)" |
| a21 | Taylor coefficients vs b_l (A-c m9) | "give the cone coefficients as the finite combinations (5)" |
| a22 | "isotopic, hence isometric" (A-c m10, A-d m15) | triangle determined by its angles |
| a23 | dihedral, not Z_k (A-d m10) | corrected in the supplement |
| a24 | the real slice argument (A-d m11) | given in the supplement |
| a25 | Bolza benchmark for O(2,8,8) (A-d m13) | added: Bolza/C_8 = O(2,8,8) (χ = −2/8); λ_1 = 3.838887258842 agrees with Strohmaier–Uski's 3.83888725884220 to twelve decimals (fetched ancillary file) |
| a26 | Fig. 7 dots hidden; Fig. 6(a) one geodesic drawn; Fig. 8 caption four curves (A-d m7, m9; A-b P4) | captions updated (two sentences kept) |
| a27 | L ≥ 1 range (A-e m1) | Theorem 1.3(ii) and the Descartes bound restricted to L ≥ 2 (the range Lemma 3.14 is proved for) |
| a28 | Gittins wording (A-e m4) | "whether there are singular points at all when the singular set has codimension ≤ 3, through the 0- and 1-spectra together" (fetched Part 2 abstract) |
| a29 | BGN remark for rational Λ is the authors' extension (A-e m5) | said so |
| a30 | Uçar pinpoints (A-e m6; also B-e m7) | "[Cor. 4.19(ii), (4.33)–(4.34); Thm 4.20]" |
| a31 | DS Def. 3.1 with Gauss–Bonnet; DGGW (5.8) and (5.11)–(5.12) (A-e m7) | done (DGGW checked in the fetched text); Thurston pinpoint not changed (B-e calls it correct) |
| a32 | Schueth p. 2; the parenthesis (A-e m8, m9) | "Uçar's all-order formulas"; "(where, we add, …)" |
| a33 | erratum clause (A-e m12) | states what the erratum corrects (Theorem 5.1, trivial Iso^max) and that (5.7) is unaffected (fetched erratum) |
| a34 | 3.4e-14 (A-e m13) | done |
| a35 | Paley–Wiener (A-e m14) | half sentence added |
| a36 | not done: A-a m11 (optional references), P1–P5; A-b m9, m10 (already flagged in Rem. 2.15(b)), m11 (the statement of Lemma B.4 already has n and μ_0), P1, P3, P5, P6; A-c m11–m14, P1–P4; A-d m4, m5, m6, m8, m12, m14, P1–P4; A-e m11, P1–P4 | judged not worthwhile this round or not verifiable; no correctness issue |

## Mathematical changes (each with its check)

1. Proposition B.4 (optimal truncation) — `theory/revision/check_heat_supporting.py` §10 (C ≤ 2.1, the chain of inequalities, the bound against computed remainders for m = 2, 3, 5, 8, 12).
2. Corollary 5.3 (four invariants), disjointness in Prop. 5.2, Problem 5 (p,q,r ≥ 2, automatic hyperbolicity), uniqueness in Theorem 5.9 — proofs in the text; blind check.
3. Proposition 2.14 made conditional for l ≥ 3 (Remark 2.15); Prop. 2.16(ii) range — text.
4. Remark B.5, N = 3 with row bounds — `check_heat_supporting.py` §11 and `review/referee-round-9/main/scratch/rows3.py`.
5. Theorem 3.11(ii): C = Dq — brute force for M = 2..5 (scratch, recorded here).
6. Theorem 1.3(ii) and Theorem 3.15 restricted to L ≥ 2.
7. Corollary 6.5 restricted to δ_thm.

Blind check: `blind-check-A/REPORT.md`: all twelve items correct; it found three places that still stated the l ≥ 3 linear part or Prop. 2.16(ii) for L ≥ 4 without the condition of Remark 2.15 (the Introduction, the paragraph after Prop. 2.14, the statement of Prop. 2.16(ii) and its echo in Section 2.4), now all conditional; the L = 2 case of the Jacobian step; and the unstated σ² = id in the supplement's slice argument. All fixed.

## What blocks this paper after four rounds

- **A2 (parameter dependence).** The proof of Prop. 2.14 for l ≥ 3 needs that Donnelly's fixed-point expansion has remainders differentiable in a metric parameter, uniformly in t. This is standard in spirit but neither proved in the paper nor found stated in a source we could fetch and check, and inventing a citation is excluded. A further round would not change this: it needs either a real proof (a parametric parametrix argument of several pages) or a verified reference, which is work for the authors.
- **A4/A7 (editorial).** The title and the decision to keep duplicated proofs across the two AGAG submissions are the authors' choices; the editor's requests there cannot be settled by revision rounds.
- Every other confirmed item of this round is resolved.
