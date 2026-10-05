# TRACE: every result and every number in the manuscript, traced to its source

Register rows are those of `review/audit/THEOREM-REGISTER.md` (numbered 1-102). "Source proof"
is the file the manuscript's proof is adapted from; "audit" is the independent re-derivation
in `review/audit/<group>/` (REVIEW.md, COMPARISON.md and `check_*.py` with saved output).
Notation follows `theory/CONVENTIONS.md`; where a source file uses other symbols, the
translation is the one in its section 3 (for example `H_nu = c_{nu+2}`, numerics `c1, c2, c3`
= `d_3, d_4, d_5`, Theorem B's constant `c_n` = `varsigma_n`, the Jacobian constant = `varpi_n`).

Status is the register's. The manuscript states nothing beyond it: COMPUTATION rows are stated
as computations or exact verifications, the two OPEN rows as open problems, and the CONJECTURE
and CLAIM (FALSE) rows (20, 24, 25) are not used.

## 1. Results

### Section 1 (introduction; composite statements, each part proved later)

| label | register rows | proved at |
|---|---|---|
| `thm:intro-signature` | 47, 50, 33, 35 | `cor:sigarea`, `thm:signonuniform`, `thmA`, `thmC` |
| `thm:intro-locality` | 55, 58, 62, 64, 63 | `thm:locality`, `cor:Kinf`, `thm:quantlocality`, `thm:sharp`, `cor:prefactor` |
| `thm:intro-rigid` | 14, 15, 16, 98 | `thm:threshold`, `thm:minimal`, `thm:three`, `thm:isolation` |
| `thm:intro-stability` | 71, 72, 74 | `thm:S3`, `prop:sharpexp`, `thm:S4` |

### Section 2 (heat invariants)

| label | register row | status | source proof | verifying script |
|---|---|---|---|---|
| `def:signature`, `def:heatcoef`, `def:K`, `eq:Kcompare` | (definitions) | | `theory/definitions.tex` | `theory/definitions-check.py`, `theory/conventions_check.py` |
| `prop:heatinput` | 5, 32, 40 | PROVED GIVEN CITED INPUT | `theory/signatures/proof.md` §1 (H1)-(H3); `theory/locality/proof.md` Proof B; G5 item 10 (Ucar Thm 4.20(ii), (4.35)); row 5 note (integer powers from point strata) | `theory/cone-coefficients/verify_cone_coefficients.py`, `theory/conventions_check.py`; audit `review/audit/audibility/check_heat_input.py`, `review/audit/consistency/check_heat_input.py` |
| `lem:conepoly` | 41 | PROVED GIVEN CITED INPUT | `theory/signatures/proof.md` Lemma 1 | `theory/signatures/heat_structure.py` (l <= 15); audit `review/audit/signatures/check_cone_coefficients.py` |
| `lem:cot` | 1 | PROVED | `paper/main.tex` lem:cot | audit `review/audit/threshold/check_heat.py` |
| `prop:csc` | 2 | PROVED | `paper/main.tex` prop:csc | audit `review/audit/threshold/check_heat.py` |
| `def:cone`, `cor:conevals` | 3 | PROVED GIVEN CITED INPUT | `paper/main.tex` | audit `review/audit/threshold/check_heat.py` |
| eqs `eq:a0conv`, `eq:s1inv` | 4 (rem:bugfix dropped) | PROVED GIVEN CITED INPUT | `paper/main.tex` | `code/verify_identities.py`; audit `review/audit/threshold/check_heat.py` |
| eqs `eq:b1`, `eq:a2red` | 6 | PROVED GIVEN CITED INPUT | `paper/main.tex` | `numerics/theory.py`; audit `review/audit/threshold/check_heat.py` |
| `lem:triangular` | 42 | PROVED GIVEN CITED INPUT | `theory/signatures/proof.md` Lemma 2 (sum from k = 0, G5 item 7) | `theory/signatures/heat_structure.py` |
| `rem:curvature` | 84 (cited as prior work), 85 | PROVED GIVEN CITED INPUT | `theory/curvature/proof.md` Proposition, Parts 1-3 ("n >= 2" in Part 2, G5 item 7 / row 84 note) | `theory/curvature/curvature_checks.py`; audit `review/audit/curvature-divergence/check_curvature.py` |
| `rem:divergence` | 87, 88, 89, 90, 91 (one remark, G5) | PROVED GIVEN CITED INPUT | `theory/divergence/proof.md` Lemma 1, Thms 2-3, Cor 4, Borel reading; s_k > 0 proof and l <= 8 from `review/audit/curvature-divergence/COMPARISON.md` | `theory/divergence/divergence.py`; audit `review/audit/curvature-divergence/check_divergence.py`, `check_lemma1.py` |

### Section 3 (the signature)

| label | register row | status | source proof | verifying script |
|---|---|---|---|---|
| `lem:parity` | 38 | PROVED | `theory/audibility/proof.md` Lemma 1 | `theory/audibility/verify_elimination.py`; audit `review/audit/audibility/check_lemma1.py` |
| `thmA` | 33 | PROVED GIVEN CITED INPUT (injectivity itself PROVED) | `theory/audibility/proof.md` §2; Orlando via Holtz-Tyaglov Thm 1.17 | `theory/audibility/verify_elimination.py`, `orlando_check.py`; audit `check_theoremA.py` |
| `thmB` | 34, 66 | PROVED | linearity: `theory/audibility/proof.md` §3; determinant and `varsigma_n = (-1)^{n(n+1)/2}`: `theory/stability/proof.md` Lemma S2.1 (G5 item 8) | `theory/audibility/linear_system.py`, `theory/stability/lipschitz_e.py` (n = 2..10); audit `check_theoremB.py`, `review/audit/stability/check_det.py` |
| `rem:secondproof` | 34 (Step 1 of the source proof) | PROVED | `theory/audibility/proof.md` §3 Step 1 | as `thmB` |
| `thmC` (1), (2) | 35 | PROVED | `theory/audibility/proof.md` §4 | `theory/audibility/sharpness_search.py`; audit `check_theoremC.py` |
| `thmC` (3) | 36 | COMPUTATION (exact witnesses for n = 3, 4) | `theory/audibility/proof.md` §4 table; `theory/definitions-check.py` | `theory/audibility/sharpness_search.py`; audit `check_AU4_definitions.py`, `check_phase2.py` |
| `prob:sharp` | 37 | OPEN | `theory/audibility/proof.md` §4 | `theory/audibility/sharpness_n5_N120.json`; audit `check_n5_search.py` |
| `rem:jacobian` | 39 | PROVED | `theory/audibility/proof.md` Remarks 2-3 (constant renamed `varpi_n`; "hyperbolic genus-0") | `theory/audibility/sharpness_search.py` part C |
| `lem:padding` | 43 | PROVED GIVEN CITED INPUT | `theory/signatures/proof.md` Lemma 3 | `theory/signatures/heat_structure.py` |
| `lem:sigdata` | 44 | PROVED GIVEN CITED INPUT | `theory/signatures/proof.md` Lemma 4; `statements.tex` lem:sigdata (1 <= j <= 2L-3; (g;m) in Sig in the converse; G5 item 7) | `theory/signatures/heat_structure.py`; audit `check_corollaries.py` |
| `thm:sigsep` | 45, 46 | PROVED GIVEN CITED INPUT | `theory/signatures/proof.md` Theorem S, Corollary S1 | `theory/signatures/genus.py`; audit `check_theorem_S.py` |
| `cor:sigarea` | 47 | PROVED GIVEN CITED INPUT | `theory/signatures/proof.md` Corollary S2 | `theory/signatures/genus.py`, `area_classes.py` |
| `thm:sigcount` | 48 | PROVED GIVEN CITED INPUT | `theory/signatures/proof.md` Theorem T1 (separation through Theorem S, the audit's route) | `theory/signatures/cone_count.py` |
| `prop:prouhet` | 49 | PROVED | `theory/signatures/proof.md` Proposition P | `theory/signatures/genus.py`; audit `check_prouhet.py` |
| `thm:signonuniform` | 50 | PROVED GIVEN CITED INPUT | (a) `theory/signatures/proof.md` Theorem N(a); (b) the doubling construction of `review/audit/signatures/REVIEW.md` P1 (f') | `theory/signatures/genus.py`, `cone_count.py`; audit `check_thmN_a.py`, `check_thmN_b.py`, `check_their_constructions.py` |
| `rem:constructions` | 51 | COMPUTATION | `theory/signatures/proof.md` §4; `review/audit/signatures/check_thmN_b.txt` | as above |
| `cor:siggrowth` | 52 | PROVED GIVEN CITED INPUT | `theory/signatures/proof.md` Corollary N1 | audit `check_corollaries.py` |
| `ex:siggenus` | 54 | COMPUTATION | `theory/signatures/statements.tex` | `theory/signatures/genus.py` |
| `prob:growth` | 53 | OPEN | `theory/signatures/proof.md` §7 | — |
| `rem:sigphysics` | 31 (revised: (a) by Theorem A, (b) by Cor. 2.3, (c) the n = 4 witness) | interpretation | `theory/signatures/statements.tex` rem:sigK, rem:sigphysics | — |

### Section 4 (locality)

| label | register row | status | source proof | verifying script |
|---|---|---|---|---|
| `thm:locality` | 55, 29 (thm:locality, no longer a forward reference) | PROVED GIVEN CITED INPUT | `theory/locality/proof.md` Theorem 1, Proofs A and B | `theory/locality/check_locality.py`; audit `review/audit/locality/check_expansion.py` |
| `prop:teich` | 56 (supersedes 28, eq:moduli) | PROVED GIVEN CITED INPUT | `theory/locality/proof.md` Proposition 2.1 | audit `check_teich.py` |
| `prop:rigidity` | 27 | PROVED GIVEN CITED INPUT | `theory/definitions.tex` prop:rigidity | — |
| `prop:uncountable` | 57 | PROVED GIVEN CITED INPUT | `theory/locality/proof.md` Proposition 2.2 | — |
| `cor:Kinf` | 58, 29 (prop:Kinf, unconditional), 31(b) | PROVED GIVEN CITED INPUT | `theory/locality/proof.md` Corollary 2.3 | — |
| `thm:IEH` | 59 | PROVED GIVEN CITED INPUT | `theory/locality/proof.md` Theorem 3.1 | `theory/locality/check_locality.py` |
| `lem:admissible` | 60 | PROVED GIVEN CITED INPUT | `theory/locality/proof.md` Lemma 3.2 (Weyl bound cited as DGGW Thm 4.8 at order t^{-1}; G5 item 9) | audit `check_P2.py` |
| `lem:counting` | 61 | PROVED | `theory/locality/proof.md` Lemma 3.3 | — |
| `thm:quantlocality` | 62 | PROVED GIVEN CITED INPUT | `theory/locality/proof.md` Theorem 3.4 (systole over all hyperbolic classes; (c) needs area, signature, l; G5 item 7) | `theory/locality/check_locality.py`; audit `check_thm34.py` |
| `thm:sharp` | 64 | PROVED GIVEN CITED INPUT | `theory/locality/proof.md` Theorem 3.5 (w defined before the statement) | — |
| `cor:prefactor` | 63 | PROVED | `theory/locality/proof.md` §3.3 ("|w_1(l) - w_2(l)|") | `numerics/moduli/geodesics.py` |
| `rem:proofC` | 55 (Proof C, labelled a cross-check) | | `theory/locality/proof.md` Proof C | `theory/locality/check_locality.py` |
| `rem:blind` | — (commentary) | | `theory/locality/proof.md` §3.4-3.5 | — |

### Section 5 (triangle orbifolds)

| label | register row | status | source proof | verifying script |
|---|---|---|---|---|
| `prop:cs` | 7 | PROVED | `paper/main.tex` | — |
| `prop:recovery` | 8 | PROVED GIVEN CITED INPUT | `paper/main.tex` | `code/verify_identities.py` |
| Jacobian of (S1, R, P3) (prose after `prop:recovery`) | 9 | PROVED | `paper/main.tex` | audit `review/audit/threshold/check_threshold.py` |
| `thm:three` | 16 (with prop:rigidity, G5 item 10) | PROVED GIVEN CITED INPUT | `paper/main.tex` thmC | — |
| `cor:detect` | 17 | PROVED GIVEN CITED INPUT | `paper/main.tex` corD | — |
| `cor:Krestated` | 30 | PROVED GIVEN CITED INPUT | `theory/definitions.tex` thm:Crestated | — |
| `lem:chamber` | 10 (p = 2 and (9,3) caveat, G5 item 7) | PROVED | `paper/main.tex` | `theory/threshold/threshold.py` C5 |
| `lem:bound` and R^+ formula | 11 (finite set, R^+_{S,2} not attained) | PROVED | `paper/main.tex` | as above |
| `prop:min` and the sentence after it | 12, 18 | PROVED | `paper/main.tex` | — |
| `lem:adjacent` | 77 (Lemma 2) | PROVED | `theory/threshold/proof.md` Lemma 2 | `theory/threshold/threshold.py` |
| `lem:oneineq` | 77 (Lemma 1) | PROVED | `theory/threshold/proof.md` Lemma 1 | `theory/threshold/threshold.py` |
| `thm:Sstar` | 78 | PROVED | `theory/threshold/proof.md` Theorem 1 | `theory/threshold/threshold.py` (C3, p < 5000); audit `check_compare.py` |
| `thm:separation` | 13, 79 | PROVED | `paper/main.tex` thm:separation, proved by `theory/threshold/proof.md` Corollary 2 | `theory/threshold/threshold.py`; audit `check_threshold.py` |
| `thm:threshold` | 14 ("first failure at 18"; collision-free sums, G5 item 8) | PROVED GIVEN CITED INPUT | `paper/main.tex` thmA | `theory/diophantine/data/per_S.csv` |
| `thm:minimal` | 15 | PROVED GIVEN CITED INPUT | `paper/main.tex` thmB | — |
| `prop:tangency` | 81 ("S >= 3p+3", G5 item 7) | PROVED | `theory/threshold/proof.md` Proposition 3 | `theory/threshold/threshold.py` |
| Table `tab:overlap` | 80 | COMPUTATION | `theory/threshold/proof.md` §5 | `theory/threshold/first_overlap_vs_collision.csv` via `paper/jga/tools/make_tables.py` |
| `thm:isolation` | 98 | PROVED GIVEN CITED INPUT (PARI) | `theory/diophantine/variety.md` §6; 2-isogeny descent from `review/audit/diophantine/REVIEW.md` | `theory/diophantine/ranks.py`, `theory/diophantine/data/ranks.txt`; audit `check_ranks.py`, `check_descent.py` |

### Section 6 (stability)

| label | register row | status | source proof | verifying script |
|---|---|---|---|---|
| `rem:stabscope` | — (assumptions of `theory/stability/proof.md` §7) | | | |
| `prop:frontend` | 65 | PROVED GIVEN CITED INPUT | `theory/stability/proof.md` Proposition S1 | `theory/stability/front_end.py`; audit `check_frontend.py` |
| `lem:hurwitz` | 67 | PROVED | `theory/stability/proof.md` Lemma S2.2 | `theory/stability/lipschitz_e.py` |
| `thm:S2` | 68 | PROVED | `theory/stability/proof.md` Theorem S2 | `theory/stability/lipschitz_e.py`; audit `check_s2.py` |
| Ostrowski (prose before `lem:rouche`) | 69 (gamma over both polynomials) | PROVED GIVEN CITED INPUT | `theory/stability/proof.md` §4 | audit `check_ostrowski.py` |
| `lem:rouche` | 70 | PROVED | `theory/stability/proof.md` Lemma S3 | `theory/stability/roots_holder.py` |
| `thm:S3` | 71 | PROVED GIVEN CITED INPUT | `theory/stability/proof.md` Theorem S3 | `theory/stability/roots_holder.py`; audit `check_s3.py` |
| `prop:sharpexp` | 72 (a != 0, g(0) != 0, prod(z_i+z_j) != 0; G5 item 7) | PROVED | `theory/stability/proof.md` Proposition S3.2 | `theory/stability/roots_holder.py` |
| `rem:triple` | 73 | PROVED | `theory/stability/proof.md` Remark S3.3 | `theory/stability/roots_holder.py` |
| `thm:S4` | 74 | PROVED GIVEN CITED INPUT | `theory/stability/proof.md` Theorem S4 | `theory/stability/threshold.py` |
| `prop:S5` | 75 (proof written out, G5 item 9) | PROVED | `theory/stability/proof.md` Proposition S5; steps from `review/audit/stability/REVIEW.md` §ST.12 | `theory/stability/threshold.py`; audit `check_s5.py`, `check_probe.py` |
| Table `tab:thresholds` | 76 (delta_up(2,2,2,2,3) = 5.312e-05, ratio 6.72; G5 item 8) | COMPUTATION | `theory/stability/proof.md` §5 | `theory/stability/threshold_results.json` via `make_tables.py` (regenerated by `threshold.py`; the audit's `review/audit/stability/check_dup.txt` gives the same 5.311320e-05) |
| Table `tab:blind` and §6.5 | — (blind experiment) | COMPUTATION | `theory/stability/proof.md` §6 | `theory/stability/blind/RESULT.md`, `result.json` |

### Section 7 (experiments)

No theorem-like statements. Sources: `numerics/REPORT.md` (Section 7.1) and
`numerics/moduli/REPORT.md` (Section 7.2), with their data in `numerics/data/` and
`numerics/moduli/data/`; validated by `numerics/validate_committed.py` and
`numerics/moduli/analysis.py`.

### Section 8 (degeneracies)

| label | register row | status | source proof | verifying script |
|---|---|---|---|---|
| `prop:reformulation` | 92 (primitive triples x_i; "lie in"; G5 item 7/row note) | PROVED | `theory/diophantine/variety.md` Proposition 1; lcm/gcd argument from `review/audit/diophantine/COMPARISON.md` DI.1 | `theory/diophantine/variety_checks.py` |
| `prop:pencil` | 93 (base-point orders 6,6,2,1,3,3; G5 item 8) | PROVED GIVEN CITED INPUT | `theory/diophantine/variety.md` §2 | `theory/diophantine/variety_checks.py`; audit `check_algebra.py`, `check_groups.py` |
| `prop:dual` and the paragraph after it | 94 | PROVED (the "infinite order" statement: see OUTSTANDING.md §6) | `theory/diophantine/variety.md` §3 | `theory/diophantine/variety_checks.py` §5, `families.py`; audit `check_enum.py` |
| `rem:isosceles` | 98 (row note: isosceles points are torsion, provable) | PROVED | `review/audit/diophantine/REVIEW.md` DI.7 | audit `check_isosceles.py` |
| `rem:nolinear` | 95 (all-proportional families excluded; G5 item 7) | PROVED | `theory/diophantine/variety.md` Proposition 2 | `theory/diophantine/families.py` |
| `prop:scaling` and the floor(X/18) sentence | 19, 21 (superseded, stated as the elementary bound) | PROVED | `paper/main.tex` | — |
| inequality `eq:copies` | 99 (R <= 3 for every positive triple) | PROVED | `theory/diophantine/variety.md` §7 | — |
| `thm:iso` | 100 | PROVED | `theory/diophantine/variety.md` Theorem 4 | `theory/diophantine/families.py`; audit `check_isosceles.py` |
| `thm:loglog` (proof in Appendix A) | 101 | PROVED | `theory/diophantine/variety.md` Theorem 5; multiplicity 6, cutoff 1/8, phi-sum bound from `review/audit/diophantine/COMPARISON.md` DI.10 | audit `check_theorem5.py`, `check_theorem5_family.py` |
| `thm:largefibres` | 96 (fixed ending, G5 item 9), 97 | PROVED GIVEN CITED INPUT | `theory/diophantine/variety.md` Theorem 3; corrected ending from `review/audit/diophantine/COMPARISON.md` DI.5 | `theory/diophantine/cubic_group.py`, `ranks.py`, `theory/diophantine/data/ranks.txt` |
| Table `tab:fibres` | 102 ("share c_1 and c_2"; G5 item 4), 97 | COMPUTATION | `theory/diophantine/RECOMMENDATION.md` §1.1 | `theory/diophantine/data/groups.csv`, `theory/diophantine/data/ranks.txt` via `make_tables.py`; audit `enum_4800.txt` |
| S = 36 example and "507 of 582" | 22 ("most sums") | COMPUTATION | `paper/main.tex` | `theory/diophantine/data/per_S.csv` |
| Table `tab:density` | 23 (both conventions, no c*S^2 column) | COMPUTATION | `paper/main.tex` tab:density, extended | `review/audit/threshold/check_enum.txt`, cross-checked with `theory/diophantine/data/per_S.csv` by `make_tables.py` |
| `conj:growth` | — (replaces row 24 per G5 item 2) | CONJECTURE | `theory/diophantine/RECOMMENDATION.md` §1.2 | `theory/diophantine/data/exponent_fits.txt` |
| Table `tab:enum` (Appendix B) | 26 | COMPUTATION | `paper/main.tex` tab:enum | `review/audit/threshold/tab_enum_reference.txt`, re-derived by `make_tables.py` |

Not in the manuscript, as G5 requires: rows 20 (degeneracy localization), 24 (conj:density and
the birthday heuristic), 25 (rem:ncone), and rem:bugfix (part of row 4). Not included, being
remark-level and not needed: row 82 (Kokotov flat-cone input), row 83 (invariant multiplicities,
classical), row 86 (curvature Part 4). Row 28 (eq:moduli) is superseded by `prop:teich`.

## 2. Numbers

Each number printed in the manuscript, with the committed file it comes from. Numbers that are
direct consequences of a displayed formula (for example 25/12 from 1032 and 1782) are listed
with the formula.

### Section 1
- 17, 18, (2,8,8), (3,3,12): `theory/threshold/proof.md` (Corollary 2); exact.
- about 2850 eigenvalues per orbifold: `numerics/REPORT.md` §3.
- 23 pi/6, (0;2,2,2,2,2,3,4): Linowitz-Voight Thm A, quoted in `theory/locality/proof.md` §3.5.
- c = S_1 + R - 2: `review/audit/PRIORITY.md` (exact check `review/audit/literature/check_priority.txt`).

### Section 2
- alpha_0..alpha_4 = 1, -1/3, 1/15, -4/315, 1/315: `theory/stability/proof.md` §1; `review/audit/consistency/check_heat_input.txt`.
- p_0, p_1, p_2: `theory/cone-coefficients/verify_output.txt`.
- cone(2), cone(3), cone(5) = 1/8, 2/9, 2/5; 269/360, 1/180, 271/360: `paper/main.tex` (exact; `code/verify_identities.py`).
- 11/360, -1/360: eq. (2.10)-(2.11), from p_1.
- flat t^0 coefficients 0, 1/2, 2/3, 3/4, 5/6: `theory/curvature/proof.md` Part 1; `theory/curvature/curvature_output.txt`.
- genus 10^4, l <= 8: `review/audit/curvature-divergence/COMPARISON.md` DV.3 (`check_divergence.txt`).

### Section 3
- 1032, 1782; 8/15, 58, 31402, 25159618, 21298618: `theory/audibility/proof.md` §4 table; `theory/definitions-check.py`.
- 216,071,394 multisets (n = 5, orders <= 120): `theory/audibility/sharpness_n5_N120.json`.
- 11 witness classes with orders <= 90, 9 primitive (n = 4): `review/audit/audibility/check_phase2.txt`.
- cone counts 3/5, 15/17, 63/65, 255/257, 1023/1025: `theory/signatures/output/genus.txt`.
- 5/6, 23/24, 95/96, 383/384, 1535/1536, 6143/6144; (0;4,4,4,6,6), (0;2,2,2,3,8,8): `review/audit/signatures/check_thmN_b.txt`.
- 9/10, 103/104: `theory/signatures/output/cone_count.txt`.
- 14/15 (area/2pi of (1;15)), 224/15: exact, `theory/signatures/output/genus.txt`.

### Section 4
- 6g - 6 + 2n: Thurston Cor 13.3.7 (`theory/locality/proof.md` §T2).
- identity-term moments through t^14, elliptic through t^5, m in {2,3,4,5,6,8,12}: `theory/locality/check_locality.py` (output in `theory/locality/output/`).

### Section 5
- S*(p), x*(p) = 18, 18, 20, 45/2, 126/5, 28, 216/7; 18, 19, 20, 23, 26, 29, 32; gaps 1/840, 1/2310, 1/10296; -7/936, -1/72, -19/3960, -1/180, -76/15015, -1/231, -17/4680; 8.52 (root of p^2-5p-30): `theory/threshold/proof.md` Theorem 1; `review/audit/threshold/check_compare.txt`.
- 101/168, 3/5, 7/10, 60/224, 3/4: `theory/threshold/proof.md`, `paper/main.tex`.
- 107/144 (c_2 of O(3,3,4)): `paper/main.tex` remark*; `review/audit/consistency/check_indexing.txt`.
- 38 collision-free sums in [18, 4800], 19, 21-25, 27-30, 33, largest 557: `theory/diophantine/data/per_S.csv` (pairs = 0).
- first non-adjacent collision S = 35, (5,15,15) and (7,7,21); 2793 of 3067: `review/audit/consistency/check_counts.txt`; `review/audit/G5-VERDICT.md` item 1.
- Table `tab:overlap`: `theory/threshold/first_overlap_vs_collision.csv`.
- Lambda = 27/2; E: [0,393,0,3456,0]; rank 0; torsion 12, Z/2 x Z/6; Selmer groups {+-1, +-6}, {1}: `theory/diophantine/data/ranks.txt`; `review/audit/diophantine/check_descent.txt`.

### Section 6
- F^{-1} rows (-2; 2, 12; -18, -120, -360; 30, 252, 1260, 2520); amp = 2, 14, 498, 4062, 56230/3; diagonal 2, 12, 360, 2520, 10080; relative ratios 0.02-3.7: `theory/stability/front_end_output.md`; `review/audit/stability/check_frontend.txt`.
- zeta_3 = 1, zeta_4 = 79/3, zeta_5 = 14048/15; t_3 = 1/3 + (n+1)^2: `theory/stability/proof.md` Theorem S2.
- cond between 1 and 3.5; Hadamard bound 12 to 4425: `theory/stability/lipschitz_e_output.md`.
- 2.7385, 4.4630, 2.0446: `theory/stability/roots_holder_output.md`.
- Radius set {1/2, 19/40, ..., 1/40, 1/100, 1/1000}: `theory/stability/threshold.py` (RADII).
- Table `tab:thresholds`: `theory/stability/threshold_results.json`, as regenerated by `theory/stability/threshold.py` (now with the audit's epigraph search); (2,2,2,2,3) delta_up 5.31132e-05, printed rounded up, as in `review/audit/stability/check_dup.txt`.
- 1.03-2.05, 6.72, 7e-4: same files (ratios of printed values).
- Table `tab:blind`; 0.21 and 0.26 standard errors; 2.0833 +- 1.6e-4; roots 2.9915, 3.0085: `theory/stability/blind/RESULT.md`; margins about 100 and 20: `theory/stability/proof.md` §6.

### Section 7
- order 10, size 0.05, 1420-1440 eigenvalues, lambda ~ 21,700 / 23,800; 2.9e-11, 1.2e-8; 42 Bolza eigenvalues below 998, 5.7e-11; 7e-13 for t <= 0.03; 1e-7 detection level: `numerics/REPORT.md` §3-4; `numerics/moduli/REPORT.md` §7 (detection level).
- 1434 eigenvalues recomputed: `numerics/moduli/data/s3_repro.json`.
- pi/2, 67/48, d_3 = 25/12, d_4 = -1775/24, d_5 = 153025/48: `numerics/REPORT.md` §2; `theory/CONVENTIONS.md` §1.
- d_3 = 2.0833320 +- 0.0000031, d_4 = -73.9551 +- 0.0062, -0.4 sigma, +0.5 sigma; 1.4e-5, 0.028; 4e-13, 3e-11; 0.042, -0.030, 0.026; 144/pi^2: `numerics/REPORT.md` and `numerics/data/headline.json`, `fits.csv`.
- 1.997, 1.9998; 2.2568, 1.8626: `numerics/REPORT.md` §4(d), §5.
- (0;3,3,3,3), 4 pi/3, theta in {0, 0.4, ..., 2.8}, ~5450 eigenvalues, 1.6e4, systoles 2.634 -> 0.694, 1.3e-10 (8.3e-9), 1.2e-12, 2.2e-11, 1.3e-13, lambda_1 4.1224 -> 0.4348, 89%, 28 pairs, 1.1e-13, t <= 0.33, 0.79, 24.5, 0.9997-1.0000, t_1 = 0.4, length 6.5: `numerics/moduli/REPORT.md`; `numerics/moduli/data/summary.json`.

### Section 8
- Proposition `prop:pencil`: discriminant, fibre types, orders 6,6,2,1,3,3: `theory/diophantine/variety.md` §2; `review/audit/diophantine/check_algebra.txt`, `check_groups.txt`.
- 1753 primitive pairs, 423 dual, 1330 others, none with order <= 12: `theory/diophantine/variety.md` §3; `review/audit/diophantine/check_enum.txt`.
- c_iso = 3 log 2/(2 pi^2) = 0.10535...; 506 vs 505.7; 1.9 log S: `theory/diophantine/variety.md` Theorem 4; `review/audit/diophantine/check_isosceles.txt`.
- 3/(128 pi^4), 3/(32 pi^4), 1/8: `theory/diophantine/variety.md` Theorem 5; `review/audit/diophantine/check_theorem5_family.txt`.
- 155/12, (4:9:18), n <= 12, 3P = (162833463:287876366:723926268), rank 2: `theory/diophantine/variety.md` Theorem 3; `theory/diophantine/data/ranks.txt`.
- Table `tab:fibres` (S = 136, 408, 1849, 4600; ranks 2, 2, 3, 3; no size 7 to 4800): `theory/diophantine/data/groups.csv`, `theory/diophantine/data/ranks.txt`; `review/audit/diophantine/enum_4800.txt`.
- 507 of 582 sums; S = 36 classes, R = 3/10: `theory/diophantine/data/per_S.csv`, `groups.csv`.
- Table `tab:density`; local exponent 2.5 -> 1.58; N/S^2 0.0094 (S = 400) -> 0.00405 (S = 6000): `review/audit/threshold/check_enum.txt`, `theory/diophantine/data/per_S.csv`.
- q = 4.5 +- 0.5 (all pairs), 3.5 (primitive pairs), 33% and 16.5%: `theory/diophantine/RECOMMENDATION.md` §1.2-1.3; `theory/diophantine/data/exponent_fits.txt`.

### Section 9 and appendices
- T_L >= 2L+2, T_L <= 2^{2L-1}, T_2 = 6, T_3 in {8, 10}, entries <= 30: `theory/signatures/proof.md` §5, §7.
- 3,067,197,199 triads with 10 <= S <= 4800: `review/audit/diophantine/REVIEW.md` DI.6 (`enum_4800.txt`).
- PARI call and output for Lambda = 27/2: `theory/diophantine/data/ranks.txt`.
- Table `tab:enum`: `review/audit/threshold/tab_enum_reference.txt`.
