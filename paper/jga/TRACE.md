# TRACE: every result of the 30-35 page manuscript, traced to its sources

Columns: **register** = row of `review/audit/THEOREM-REGISTER.md` (rows 1-102, gate G5);
**audit-2** = row of `review/audit-2/REGISTER-ADDENDUM.md` (rows A1-H11, gate G5-bis);
**source** = the file the text is adapted from (`theory/revision/*.tex`, `theory/pte/*`, or the
earlier sources named in the G5 TRACE, recorded here where unchanged); **check** = the script or
audit evidence. Numbers are those of the build recorded in BUILD.md (35 pp.). Status words are
the registers'. COMPUTATION rows are stated as computations; OPEN rows as open problems.

## Section 1

| label | number | register | audit-2 | proved at |
|---|---|---|---|---|
| `thm:intro-signature` | Thm 1.1 | 47, 50, 33, 35 | B4, B5, B6 | Cor 3.5, Thms 3.10, 3.11, A, C |
| `thm:intro-rigid` | Thm 1.2 | 14, 15, 16, 98 | G1, E6 | Thms 5.1, 5.6, 5.7, 5.10 |
| `thm:intro-stability` | Thm 1.3 | 71, 72, 73, 74 | G4, G5 | Thms 6.5, 6.8, Prop 6.6, Rem 6.7 |
| "what heat does not hear" paragraph | - | 55, 58, 62, 63, 64 | D9, D10 | Prop 4.1, Cor 4.3, Thm 4.4, Thm 4.5, Cor 4.6 |
| Section 1.1 (prior work) | - | (citations) | H1-H3, H5, H9 | `review/literature-pass/NOVELTY.md` sections 1-4, 6; `CITATIONS.md` |

## Section 2 (heat invariants)

| label | number | register | audit-2 | source | check |
|---|---|---|---|---|---|
| `def:signature`, `def:K` | Defs 2.1, 2.2 | (definitions), 27 note | - | `theory/definitions.tex` | `theory/conventions_check.py` |
| `thm:IEH` | Thm 2.3 | 59 | D3, D4 (input DS eq. (1)) | `theory/locality/proof.md` Thm 3.1; `theory/revision/locality.tex` (S3) | `review/audit-2/trace-formula/check_hypbound.py` |
| `lem:counting` | Lemma 2.4 | 61 | D3 | `theory/locality/proof.md` Lemma 3.3 | audit `review/audit/locality/` |
| `lem:admissible` | Lemma 2.5 | 60 | D8 (h_T counting argument from `review/audit-2/trace-formula/REVIEW.md` TF.7) | `theory/locality/proof.md` Lemma 3.2; `theory/revision/remark412.tex` | `theory/revision/check_remark412.py` |
| `lem:hypbound`, eq (3) | Lemma 2.6 | 62 | D3, D9 | `theory/revision/lemma25.tex` Lemma hypbound; `thm12iii.tex` | `theory/revision/check_thm12iii.py`; `review/audit-2/trace-formula/check_hypbound.py` |
| `lem:Phi`, eq (4) | Lemma 2.7 | 41 | D2 | `theory/revision/lemma25.tex` Lemma Phi | `theory/revision/check_lemma25.py`; `review/audit-2/trace-formula/check_closedform.py` |
| `prop:heatinput`, eqs (5), (6) | Prop 2.8 | 5, 32, 40 | D1, D4 | `theory/revision/lemma25.tex` (elliptic moments folded into the proof) | `check_lemma25.py`; `review/audit-2/trace-formula/check_conepoly.py` |
| `lem:conepoly` | Lemma 2.9 | 41 | D5 | `theory/revision/lemma25.tex` | `check_lemma25.py` (l <= 40) |
| eq (7) and the Schueth sentence | - | 6 | D6 | `theory/revision/lemma25.tex`; wording from `review/audit-2/trace-formula/REVIEW.md` TF.5c | `check_conepoly.py` |
| `rem:ucaragree` (= `rem:proofC`) | Rem 2.10 | 55 | D7, D8 | `theory/revision/lemma25.tex` rem:ucaragree; `remark412.tex` (2A) with TF.7 wording | `review/audit-2/trace-formula/check_ucar.py` |
| `lem:triangular`, eqs (8), (9) | Lemma 2.11 | 42, 4, 6 | - | `theory/signatures/proof.md` Lemma 2 | `theory/signatures/heat_structure.py` |
| `rem:curvature` | Rem 2.12 | 84, 85 | - | `theory/curvature/proof.md`; CITATIONS #1, #8 | `theory/curvature/curvature_checks.py` |

## Section 3 (the signature)

| label | number | register | audit-2 | source | check |
|---|---|---|---|---|---|
| `lem:parity` | Lemma 3.1 | 38 | - | `theory/audibility/proof.md` Lemma 1 | `review/audit/audibility/check_lemma1.py` |
| `thmA`, eq (10) | Thm A | 33 | - | `theory/audibility/proof.md` s. 2; Holtz-Tyaglov Thm 1.17 | `check_theoremA.py` |
| `thmB`, eq (11) | Thm B | 34, 66 | - | `theory/audibility/proof.md` s. 3; `theory/stability/proof.md` Lemma S2.1 | `check_theoremB.py`, `review/audit/stability/check_det.py` |
| `thmC` | Thm C | 35, 36 | - | `theory/audibility/proof.md` s. 4 | `check_theoremC.py`, `check_AU4_definitions.py` |
| `rem:witnesses` | Rem 3.2 | 37 | C6, C7, H9 | `theory/pte/proof.md` s. 3 (pencil, m = 4) with PW.3a/PW.3b wording; `review/audit-2/pte-witnesses/direct4_N440.txt` | `review/audit-2/pte-witnesses/check_pencil61.py`, `check_direct4.py`; `theory/audibility/sharpness_n5_N120.json` |
| `lem:sigdata`, eqs (12), (13) | Lemma 3.3 | 43, 44 | - | `theory/signatures/proof.md` Lemmas 3-4 | `theory/signatures/heat_structure.py` |
| `thm:sigsep` | Thm 3.4 | 45, 46 | - | `theory/signatures/proof.md` Theorem S | `check_theorem_S.py` |
| `cor:sigarea` | Cor 3.5 | 47, 48 | - | Corollary S2, Theorem T1 | `theory/signatures/genus.py`, `cone_count.py` |
| `ex:siggenus` | Ex 3.6 | 54 | C1 | `theory/signatures/statements.tex` | `theory/pte/data/witnesses.json` |
| `def:config` and the dictionary paragraph | Def 3.7 | - | A1, A3, A7 | `theory/pte/proof.md` s. 1, Prop 2.2; `statements.tex` with the PS.6 genus condition | `review/audit-2/pte-structure/check_dictionary.py`, `check_ps6.py` |
| `thm:descartes` | Thm 3.8 | - | A2, A7 | `theory/pte/proof.md` Thm 2.1 | `review/audit-2/pte-structure/check_descartes.py`, `check_attain.py` |
| `prop:doubling` | Prop 3.9 | - | B2 | `theory/pte/proof.md` Prop 3.3 with PG.1 wording | `review/audit-2/pte-growth/check_doubling.py` |
| `thm:signonuniform` | Thm 3.10 | 50 | B3 | genus pairs from the shift construction (`proof.md` Thm 3.4), cone count from doubling | `review/audit-2/pte-growth/check_upper.py` |
| `thm:growth` | Thm 3.11 | 52 (superseded), 53 | B4, B5, B6, B7 | `theory/pte/proof.md` Thms 4.1-4.3, `statements.tex` thm:ptegrowth, with PG.4-PG.6 hypotheses and constants | `review/audit-2/pte-growth/check_growth.py`; `theory/pte/growth.py` |
| N(k) literature paragraph | - | - | H1, H2, H3, H5 | `review/audit-2/VERDICT.md` SERIOUS 4 sentence; `theory/pte/LITERATURE.md` | `review/audit-2/literature/check_lifting_and_bounds.py` |
| `ex:ptepairs` | Ex 3.12 | - | C1, C2, C3, C5, H7, H9 | `theory/pte/statements.tex` ex:ptepairs with PW.1 and PW.2 wording | `theory/pte/witnesses.py`; `review/audit-2/pte-witnesses/check_pairs.py`, `check_heat.py` |
| `rem:T3` | Rem 3.13 | 53 | C4 | `statements.tex` rem:ptet3 with PW.0 wording | `theory/pte/data/T3_search_log.txt`; `review/audit-2/pte-witnesses/check_t3*.py` |

## Section 4 (what heat does not hear)

| label | number | register | audit-2 | source |
|---|---|---|---|---|
| `prop:locality` | Prop 4.1 | 55, 29 | D8 | `theory/revision/locality.tex` (S1); proof via Prop 2.8 |
| `prop:teich` = `prop:rigidity` | Prop 4.2 | 56, 27 | - | `theory/locality/proof.md` Prop 2.1; `theory/definitions.tex` prop:rigidity |
| `cor:Kinf` (= `prop:uncountable`) | Cor 4.3 | 57, 58 | - | `locality.tex` (S2): one-line Out(Gamma)-orbit proof (G7-20) |
| `thm:quantlocality` | Thm 4.4 | 62 | D9 | `theory/revision/thm12iii.tex`; old Thm 4.9(a),(b); monotonicity from TF.8 |
| `thm:sharp` | Thm 4.5 | 64 | D10 | `theory/locality/proof.md` Thm 3.5 |
| `cor:prefactor` | Cor 4.6 | 63 | D10 | `thm12iii.tex` item (1) ("attained", three cases) |
| `rem:blind` | Rem 4.7 | (commentary) | - | `locality.tex`; NOVELTY 4 (Huber, Wolpert, Dryden) |

## Section 5 (the rigid case)

| label | number | register | audit-2 | source | check |
|---|---|---|---|---|---|
| `thm:three` | Thm 5.1 | 7, 8, 16, 30 | - | `paper/main.tex` (S_1 R >= 9 directly, G7-27) | `code/verify_identities.py` |
| `lem:chamber`, eq (14) | Lemma 5.2 | 10, 11 | - | `paper/main.tex` | `theory/threshold/threshold.py` |
| `lem:adjacent` | Lemma 5.3 | 77 | - | `theory/threshold/proof.md` Lemmas 1-2 | `theory/threshold/threshold.py` |
| `thm:Sstar` | Thm 5.4 | 78 | - | `theory/threshold/proof.md` Thm 1 | `review/audit/threshold/check_compare.py` |
| `thm:separation` | Thm 5.5 | 13, 79 | - | `theory/threshold/proof.md` Cor 2 | `check_threshold.py` |
| `thm:threshold` | Thm 5.6 | 14 | G1 | `theory/revision/thm513.tex` (1) with the G1 addition | `theory/revision/check_thm513.py` |
| `thm:minimal` | Thm 5.7 | 15 | - | `paper/main.tex` | - |
| `prop:tangency` | Prop 5.8 | 81 (part (1) only) | - | `theory/threshold/proof.md` Prop 3 | `theory/threshold/threshold.py` |
| `prop:collisionfree` | Prop 5.9 | 14 (list) | G2, G3 | `theory/revision/thm513.tex` (2) | `check_thm513.py`; `review/audit-2/threshold-sharpness/check_collisionfree.c/.py`; `theory/revision/collision_witnesses.csv` |
| `thm:isolation` | Thm 5.10 | 98 | E1-E6 | `theory/revision/descent.tex` with the DE.0/DE.2 fixes (phi at Z = 0, nonsingularity, flex) | `theory/revision/check_descent.py`; `review/audit-2/descent/check_*.py`; rechecked in this session with sympy (point counts, phi o psi, flex) |

## Section 6 (stability)

| label | number | register | audit-2 | source | check |
|---|---|---|---|---|---|
| `rem:stabscope` | Rem 6.1 | (assumptions) | - | `theory/stability/proof.md` s. 7; G7-7 framing | - |
| `prop:frontend` | Prop 6.2 | 65 | - | Prop S1 | `theory/stability/front_end.py` |
| `lem:hurwitz` | Lemma 6.3 | 67 | - | Lemma S2.2 | `theory/stability/lipschitz_e.py` |
| `thm:S2` | Thm 6.4 | 68 | - | Theorem S2 (Hadamard form dropped) | `lipschitz_e.py`; audit `check_s2.py` |
| `thm:S3` | Thm 6.5 | 69, 70, 71 | - | Lemma S3, Theorem S3 (Rouche folded in) | `theory/stability/roots_holder.py` |
| `prop:sharpexp` | Prop 6.6 | 72 | G4, G5 | Prop S3.2; `theory/revision/sharpness.tex` (5) | `theory/revision/check_sharpness.py` |
| `rem:triple` | Rem 6.7 | 73 | G4, G5 | Remark S3.3; `sharpness.tex` (6) with the d_i >= -a and (498+42a^2) fixes | `review/audit-2/threshold-sharpness/check_sharpness.py` |
| `thm:S4` | Thm 6.8 | 74 | F6 | Theorem S4 | `theory/stability/threshold.py` |
| `prop:S5` | Prop 6.9 | 75 | F1, F2, F3 | `theory/revision/prop610.tex` (radii delta_j; xi, r_0 renamed so rho is the residual only) | `theory/revision/check_prop610.py`; `review/audit-2/stability/check_cert.py`, `check_probes.py` |
| sentence after Prop 6.9 | - | - | F4 | audit F4 replacement | `review/audit-2/stability/check_setup.py` |
| Table 1 (`tab:thresholds`) | Table 1 | 76 | F5-F9 | `theory/stability/threshold_results.json` via `tools/make_tables.py` (new column delta_cert/abs(c_j), rounded down) | `review/audit-2/stability/check_cert.py`, `check_dup.py` |

## Section 7, Section 8, appendices, supplement

| item | register | audit-2 | source |
|---|---|---|---|
| Section 7 (numerics) | - | - | `numerics/REPORT.md`, `numerics/data/headline.json`, `heat_trace_checks.csv`, `numerics/moduli/REPORT.md`; budget formula from `numerics/heat_trace.py` |
| Problems 1-3 | 53, 37 | C4 | `theory/pte/STATUS.md`; `theory/audibility` |
| `lem:pigeon` (Lemma A.1) | - | B1 | `theory/pte/proof.md` Lemma 1.5(1)-(2) |
| `prop:shift` (Prop A.2) | - | A6 | `theory/pte/proof.md` Prop 3.2 with n >= 1 |
| proof of Thm 3.11 | - | B3-B6 | `theory/pte/proof.md` Thms 3.4, 4.1-4.3; PG.5 constants |
| supplement S1 (spectra), Table S1 | - | - | `numerics/REPORT.md` s. 3-5; `numerics/data/convergence.csv`; `numerics/moduli/data/s3_repro.json` |
| supplement S2 (blind recovery), Table S2 | 76 note | - | `theory/stability/blind/PROTOCOL.md` (commit 3c1139a), `RESULT.md` |
| supplement S3 (moduli family), F6 | - | - | `numerics/moduli/REPORT.md`, `summary.json` |
| supplement S4, Tables S3, S4 | 80, 26 | G2 | `theory/threshold/first_overlap_vs_collision.csv`, `review/audit/threshold/tab_enum_reference.txt` via `make_tables.py` |

## Figures

| paper | file | where | data / assertions |
|---|---|---|---|
| Fig. 1 | F3 | after Thm 3.4 | `figures/src/F3.py` (caption fixed for G7-28) |
| Fig. 2 | F4 | after Thm 3.11 | `figures/src/F4.py`: area classes, upper bound, sqrt lower bound (new, exact step function), Prouhet pairs, and the 18 audited pairs of `theory/pte/data/witnesses.json` (all assertions pass) |
| Fig. 3 | F7 | Section 5.1 | `figures/src/F7.py` (unchanged) |
| Fig. 4 | F8 | Section 6 | `figures/src/F8.py` (unchanged) |
| Fig. 5 | F5 | Section 7 | `figures/src/F5.py` (unchanged) |
| Fig. S1 | F1 | supplement S1 | `figures/src/F1.py` (unchanged; not re-rendered) |
| Fig. S2 | F6 | supplement S3 | `figures/src/F6.py` (unchanged; not re-rendered) |

F2 is not used; F9 belongs to the companion note.

## Moved out of this paper

Old Section 6.5 and Section 7 (supplement); old Section 8 and Appendix A (the arithmetic of
two-coefficient degeneracies: register rows 19, 21-26, 92-97, 99-102; audit-2 E7), now in
`paper/arith/note.tex`, cited as `companion`. Old Remark 2.12 (rows 87-91) is dropped: its peeling and Borel claims as `theory/revision/remark212.tex` recommends, and the short remark itself for the page limit. Old Proposition 3.9 (Prouhet)
and the Thue-Morse proof of Theorem 3.10(a) are replaced by the audited constructions; the
Prouhet pairs remain as data in F4.
