#!/usr/bin/env python3
"""Build review/audit/THEOREM-REGISTER.md from the anchored excerpts of build_statements.py.

One row per result. Statements are reproduced verbatim (same line ranges and anchor asserts as
STATEMENTS.md). Run from the repository root: python3 review/audit/build_register.py
Exits nonzero if any excerpt id is unknown, a status is not one of the allowed values, or a
referenced audit file does not exist.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_statements as bs  # noqa: E402

ROOT = bs.ROOT
OUT = ROOT / "review/audit/THEOREM-REGISTER.md"
STATUSES = {"PROVED", "PROVED GIVEN CITED INPUT", "COMPUTATION", "CONJECTURE", "OPEN", "CLAIM (FALSE)"}
INDEX = {rid: (g, row) for g, rows in bs.GROUPS.items() for row in rows for rid in [row[0]]}

U = "Uçar (4.25)/(4.33), Thm 4.20"
DG = "DGGW Thm 4.8, Def 4.7"
DS = "Dryden–Strohmaier trace formula eq. (1)"
TH = "Thurston Cor 13.3.7 / 13.3.5"

# (name, excerpt ids, status, dependencies, external inputs, existing script, audit folder,
#  audit verdict, in paper? ("YES", "YES, REVISED", "REMARK ONLY", "CITE AS PRIOR WORK", "NO"), note)
ROWS = [
    # ---------------- manuscript core (paper/main.tex) ----------------
    ("lem:cot", ["PC.4"], "PROVED", "—", "—", "—", "threshold", "NONE", "YES", ""),
    ("prop:csc", ["PC.5"], "PROVED", "lem:cot", "—", "—", "threshold", "NONE", "YES", ""),
    ("def:cone, cor:conevals", ["PC.6"], "PROVED GIVEN CITED INPUT", "prop:csc", "DGGW cone convention (§5.6, (5.7))", "—", "threshold", "NONE", "YES", ""),
    ("eq:a0conv, eq:s1inv, rem:bugfix", ["PC.2", "PC.7"], "PROVED GIVEN CITED INPUT", "cor:conevals", "DGGW (5.7)", "—", "threshold", "MINOR", "YES, REVISED",
     "Keep eq:s1inv; drop rem:bugfix (records an internal error only). State that the reference triple (2,3,5) is spherical and the t^0 smooth term is curvature-sign independent."),
    ("Heat expansion structure (sec:heatexp)", ["PC.3"], "PROVED GIVEN CITED INPUT", "—", DG, "—", "threshold", "MINOR", "YES, REVISED",
     "Integer powers of t come from the orbifold strata (points), not from constant curvature."),
    ("eq:b1, eq:a2red", ["PC.8"], "PROVED GIVEN CITED INPUT", "eq:a0conv", f"{U}; Schueth Rem 4.2; DGGW (5.10)", "—", "threshold", "NONE", "YES", ""),
    ("prop:cs", ["PC.9"], "PROVED", "—", "—", "—", "threshold", "NONE", "YES", ""),
    ("prop:recovery", ["PC.9b"], "PROVED GIVEN CITED INPUT", "eq:a2red, prop:cs", U, "—", "threshold", "NONE", "YES", ""),
    ("Jacobian of (S1,R,P3)", ["PC.10"], "PROVED", "—", "—", "—", "threshold", "NONE", "YES", ""),
    ("lem:chamber", ["PC.11"], "PROVED", "—", "—", "—", "threshold", "MINOR", "YES, REVISED",
     "For p=2 (and (S,p)=(9,3)) the spread triad is not hyperbolic, so the maximum is not attained there."),
    ("lem:bound and the R^+ formula", ["PC.12"], "PROVED", "lem:chamber", "—", "—", "threshold", "MINOR", "YES, REVISED",
     "R^+_{S,2} is never attained; the stratum is a finite set, not a filled interval."),
    ("prop:min", ["PC.13"], "PROVED", "—", "—", "—", "threshold", "NONE", "YES", ""),
    ("thm:separation", ["PC.14", "PC.15"], "PROVED", "lem:chamber, lem:bound", "—", "—", "threshold", "NONE", "YES",
     "Threshold Theorem 1 / Corollary 2 give a uniform-in-p replacement for the per-p list."),
    ("thmA", ["PC.1"], "PROVED GIVEN CITED INPUT", "thm:separation, eq:s1inv", "DGGW (5.7)", "—", "threshold", "MINOR", "YES, REVISED",
     "'once the cone-order sum reaches 18' reads as every S>=18; sums 19, 21-25, ... have no collision (last collision-free sum 557)."),
    ("thmB", ["PC.1"], "PROVED GIVEN CITED INPUT", "thm:separation, eq:a2red", U, "—", "threshold", "NONE", "YES", ""),
    ("thmC", ["PC.1"], "PROVED GIVEN CITED INPUT", "prop:recovery, prop:rigidity", f"{U}; Troyanov Thm A", "—", "threshold", "MINOR", "YES, REVISED",
     "'Up to isometry' needs prop:rigidity (or locality Prop 2.1); cite it."),
    ("corD", ["PC.1"], "PROVED GIVEN CITED INPUT", "thmA, thmB, prop:recovery", U, "—", "threshold", "NONE", "YES", ""),
    ("remark* on a_0", ["PC.16"], "PROVED", "prop:min, prop:cs", "—", "—", "threshold", "NONE", "YES", ""),
    ("prop:scaling", ["PC.17"], "PROVED", "—", "—", "—", "threshold", "NONE", "YES",
     "The sentence in the same excerpt claiming that interval separation localizes every degeneracy to adjacent strata is FALSE (row 'degeneracy localization')."),
    ("Degeneracy localization to adjacent strata (sentence before prop:scaling; repeated in sec:density)", ["PC.17"], "CLAIM (FALSE)", "thm:separation", "—", "—", "threshold, consistency", "SERIOUS", "NO",
     "2793 of the 3067 pairs with S<=600 join strata whose least orders differ by >=2; first at S=35, (5,15,15)~(7,7,21). Describe the enumeration as exhaustive."),
    ("thm:density-lower", ["PC.17b"], "PROVED", "prop:scaling, thmB", "—", "—", "threshold", "NONE", "YES, REVISED",
     "Correct but superseded by Diophantine Theorem 4 (c_iso X log X) and Theorem 5 (X (log X)^2); state the stronger bound."),
    ("Primitive pair at S=36", ["PC.18"], "COMPUTATION", "—", "—", "—", "threshold", "NONE", "YES",
     "'Almost every sum' should read 'most sums' (507 of 582 sums in 19..600)."),
    ("tab:density and fitted exponent", ["PC.19"], "COMPUTATION", "—", "—", "enumerate_degeneracies.py (external repo)", "threshold, consistency, diophantine", "SERIOUS", "YES, REVISED",
     "Table values are exact under the pairs convention (classes: 2977 at 600) - keep, state the convention. The exponent 2.03, 'stabilizes', 'quadratic-order' and the birthday heuristic must go: N(S)/S^2 falls to 0.00405 at S=6000."),
    ("conj:density", ["PC.19"], "CONJECTURE", "—", "—", "—", "threshold, consistency, diophantine", "SERIOUS", "NO",
     "Contradicted by enumeration to S=6000; its 'equivalently N(S)=Theta(S)' is not equivalent and the 'positive proportion of order 1/S' clause is self-contradictory. Replace by the Diophantine section's N(S)=S^{1+o(1)} conjecture with the proven X(log X)^2 floor."),
    ("rem:ncone", ["PC.20"], "CLAIM (FALSE)", "—", "—", "—", "threshold, consistency", "SERIOUS", "NO",
     "Out of date: Theorem A proves K_mult<=n for all n (K_iso is infinite for n>=4); an n=4 witness {3,10,15,30}/{4,5,21,28} exists. Replace by Theorems A and C."),
    ("tab:enum", ["PC.21"], "COMPUTATION", "—", "—", "make_table.py (external repo)", "threshold", "NONE", "YES", "All 83 entries reproduced."),
    # ---------------- definitions ----------------
    ("prop:rigidity", ["DF.3"], "PROVED GIVEN CITED INPUT", "—", "Troyanov Thm A; equivalently Thurston Cor 13.3.7", "—", "locality", "NONE", "YES", ""),
    ("eq:moduli", ["DF.4"], "PROVED GIVEN CITED INPUT", "—", "Troyanov; Thurston", "—", "consistency", "MINOR", "YES, REVISED",
     "Superseded by locality Prop 2.1 (all genera, one source); update the 'needs its own source' comment."),
    ("thm:locality, prop:Kinf", ["DF.5"], "PROVED GIVEN CITED INPUT", "locality Theorem 1", DG, "—", "locality, consistency", "MINOR", "YES, REVISED",
     "Drop 'forward reference'/'conditional': locality Theorem 1 proves it."),
    ("thm:Crestated", ["DF.6"], "PROVED GIVEN CITED INPUT", "prop:recovery, prop:rigidity", U, "—", "audibility", "NONE", "YES", ""),
    ("rem:nconerestated", ["DF.7"], "PROVED GIVEN CITED INPUT", "Theorem A, prop:Kinf", U, "theory/definitions-check.py", "audibility, consistency", "MINOR", "YES, REVISED",
     "(a) is out of date: Theorem A proves injectivity for every n; remove the conditionals in (a)-(c)."),
    # ---------------- audibility ----------------
    ("Heat input (cone polynomials p_l)", ["AU.0"], "PROVED GIVEN CITED INPUT", "—", f"{U}, (4.35)", "theory/cone-coefficients/verify_cone_coefficients.py", "audibility", "MINOR", "YES",
     "Proved for all l from (4.25)/(4.33); cite Thm 4.20(ii) and (4.35); Holtz-Tyaglov is arXiv:0912.4703."),
    ("Theorem A (audibility of the cone orders)", ["AU.1"], "PROVED GIVEN CITED INPUT", "Lemma 1 (parity)", f"{U}; Orlando (Holtz-Tyaglov Thm 1.17)", "theory/audibility/verify_elimination.py, orlando_check.py", "audibility", "NONE", "YES",
     "Injectivity itself is PROVED (elementary); 'K_mult<=n' uses the cited heat input. Positive-real case is classical in substance (Steinig 1971 via Laurens): see THEOREM-A-PRIOR-ART.md."),
    ("Theorem B (linear system, det M)", ["AU.1"], "PROVED", "—", "Orlando", "theory/audibility/linear_system.py", "audibility, stability", "MINOR", "YES, REVISED",
     "Replace 'c_n in Q^x, computed for n<=8' by c_n=(-1)^{n(n+1)/2} for all n (Lemma S2.1; reproved independently). Cite Korobov-Bugaevskaya 2016 §3."),
    ("Theorem C(1)-(2) (pair criterion; real sharpness)", ["AU.1"], "PROVED", "Theorem A, Lemma 1", "—", "theory/audibility/sharpness_search.py", "audibility", "NONE", "YES", ""),
    ("Theorem C(3) (integer sharpness)", ["AU.1", "AU.4"], "COMPUTATION", "Theorem C(1)", "—", "theory/audibility/sharpness_search.py", "audibility", "NONE", "YES",
     "Proved for n=3,4 by exact witnesses (n=4: 11 witness classes with orders<=90, 9 primitive - so 'one primitive witness' and 'rare for n>=4' in the notes should be revised); n=5: none with orders<=120 (reproduced); n>=5 OPEN."),
    ("Integer sharpness K_mult >= n for n >= 5", ["AU.1"], "OPEN", "Theorem C(1)", "—", "theory/audibility/sharpness_search.py", "audibility", "NONE", "YES",
     "Stated as open; no witness with orders <= 120 at n=5 (reproduced). Do not claim more."),
    ("Lemma 1 (parity)", ["AU.2"], "PROVED", "—", "—", "theory/audibility/verify_elimination.py", "audibility", "NONE", "YES", ""),
    ("Remark 2 (Jacobian), Remark 3 (padding)", ["AU.3"], "PROVED", "Theorem A", "—", "theory/audibility/sharpness_search.py", "audibility", "MINOR", "YES, REVISED",
     "Rename the Jacobian constant (clashes with Theorem B's c_n); say 'hyperbolic genus-0'."),
    # ---------------- signatures ----------------
    ("Heat input (H1)-(H3)", ["SG.0"], "PROVED GIVEN CITED INPUT", "—", f"{U}, (4.35); {DG}", "theory/signatures/heat_structure.py", "signatures", "NONE", "YES", ""),
    ("Lemma 1 (cone polynomials)", ["SG.1"], "PROVED GIVEN CITED INPUT", "—", U, "theory/signatures/heat_structure.py", "signatures", "NONE", "YES", ""),
    ("Lemma 2 (triangular basis)", ["SG.2"], "PROVED GIVEN CITED INPUT", "Lemma 1", U, "theory/signatures/heat_structure.py", "signatures", "NONE", "YES", ""),
    ("Lemma 3 (padding)", ["SG.3"], "PROVED GIVEN CITED INPUT", "Lemma 1", U, "theory/signatures/heat_structure.py", "signatures", "NONE", "YES", ""),
    ("Lemma 4 (reduction) / lem:sigdata", ["SG.4", "SG.13"], "PROVED GIVEN CITED INPUT", "Lemmas 2-3", U, "theory/signatures/heat_structure.py", "signatures", "MINOR", "YES, REVISED",
     "Write 1<=j<=2L-3 (j odd); index the a_{l,k} sum from k=0; add '(g;m) in Sig' to the converse."),
    ("Theorem S / thm:sigsep", ["SG.5", "SG.13"], "PROVED GIVEN CITED INPUT", "Lemma 4, Lemma 5 (parity)", U, "theory/signatures/genus.py", "signatures", "NONE", "YES", ""),
    ("Corollary S1", ["SG.6"], "PROVED GIVEN CITED INPUT", "Theorem S", U, "theory/signatures/genus.py", "signatures", "NONE", "YES", ""),
    ("Corollary S2 / cor:sigarea", ["SG.7", "SG.13"], "PROVED GIVEN CITED INPUT", "Corollary S1", f"{U}; Gauss-Bonnet", "theory/signatures/genus.py", "signatures", "NONE", "YES",
     "Novelty wording per PRIORITY.md: first explicit count uniform over all closed orientable hyperbolic 2-orbifolds."),
    ("Theorem T1 / thm:sigcount", ["SG.8", "SG.13"], "PROVED GIVEN CITED INPUT", "Theorem A or Corollary S1", U, "theory/signatures/cone_count.py", "signatures", "NONE", "YES", ""),
    ("Proposition P (Prouhet)", ["SG.9"], "PROVED", "—", "—", "theory/signatures/genus.py", "signatures", "NONE", "YES", ""),
    ("Theorem N / thm:signonuniform", ["SG.10", "SG.13"], "PROVED GIVEN CITED INPUT", "Proposition P, Lemma 4", U, "theory/signatures/genus.py, cone_count.py", "signatures", "NONE", "YES",
     "P1: true for all L>=2, k>=2 (all of (a)-(g) re-proved). A smaller (b) witness exists: 23 vs 24 cone points sharing three coefficients."),
    ("Construction ranges remark", ["SG.11"], "COMPUTATION", "Theorem N", U, "theory/signatures/genus.py, cone_count.py", "signatures", "MINOR", "YES, REVISED",
     "'k>=4 impractical' is specific to the greedy route; the doubling construction is exact for every k."),
    ("Corollary N1 / cor:siggrowth", ["SG.12", "SG.13"], "PROVED GIVEN CITED INPUT", "Corollary S2, Theorem N(a)", U, "—", "signatures", "NONE", "YES", ""),
    ("Growth of f(A) (linear?) and T_L", ["SG.12", "SG.13"], "OPEN", "Corollary N1", "—", "—", "signatures", "NONE", "YES", "Stated as open."),
    ("ex:siggenus", ["SG.13"], "COMPUTATION", "Lemma 4", U, "theory/signatures/genus.py", "signatures", "NONE", "YES", "Shares exactly 2 and exactly 3 coefficients."),
    # ---------------- locality ----------------
    ("Theorem 1 (signature locality)", ["LO.0", "LO.1"], "PROVED GIVEN CITED INPUT", "—", f"{DG}; Uçar Thm 4.11, 4.20; Thurston 13.3.5", "theory/locality/check_locality.py", "locality", "NONE", "YES",
     "Proof A (DGGW) is the proof; Proof C (trace formula) is a cross-check and must be labelled so."),
    ("Proposition 2.1 (dim T = 6g-6+2n)", ["LO.2", "LO.3"], "PROVED GIVEN CITED INPUT", "—", TH, "—", "locality", "NONE", "YES", ""),
    ("Proposition 2.2 (uncountably many isometry classes)", ["LO.4"], "PROVED GIVEN CITED INPUT", "Proposition 2.1", f"{TH}; DS p. 3", "—", "locality", "NONE", "YES", ""),
    ("Corollary 2.3 (K_iso = infinity)", ["LO.5"], "PROVED GIVEN CITED INPUT", "Theorem 1, Proposition 2.2, prop:rigidity", TH, "—", "locality", "NONE", "YES", ""),
    ("Theorem 3.1 (I+E+H decomposition)", ["LO.6"], "PROVED GIVEN CITED INPUT", "Lemmas 3.2-3.3", DS, "theory/locality/check_locality.py", "locality", "NONE", "YES", ""),
    ("Lemma 3.2 (admissibility of the heat function)", ["LO.7"], "PROVED GIVEN CITED INPUT", "Lemma 3.3; Weyl bound from DGGW Thm 4.8 at t^-1", f"{DS}; {DG}", "theory/locality/check_locality.py", "locality", "MINOR", "YES, REVISED",
     "P2 SOUND: decay order 3 is used; cite 'DGGW Thm 4.8 at order t^-1' for the Weyl bound, not 'Theorem 1', so no cycle with Proof C."),
    ("Lemma 3.3 (counting closed geodesics)", ["LO.8"], "PROVED", "—", "—", "—", "locality", "NONE", "YES", "Base point must not be a cone point (it is chosen so)."),
    ("Theorem 3.4 (quantitative locality)", ["LO.9"], "PROVED GIVEN CITED INPUT", "Theorem 3.1, Lemma 3.3", DS, "theory/locality/check_locality.py", "locality", "MINOR", "YES, REVISED",
     "Define the systole over all hyperbolic classes (including geodesics through cone points); (c) also needs area, signature and ell."),
    ("t^{-1/2} prefactor cannot be dropped", ["LO.10"], "PROVED", "Theorem 3.5", "—", "numerics/moduli/geodesics.py", "locality", "MINOR", "YES, REVISED", "Write |w_1(ell)-w_2(ell)|."),
    ("Theorem 3.5 (sharp asymptotics)", ["LO.11"], "PROVED GIVEN CITED INPUT", "Theorem 3.1, Lemma 3.3", DS, "—", "locality", "MINOR", "YES, REVISED", "Define w_i(L) in the statement."),
    # ---------------- stability ----------------
    ("Proposition S1 (front end)", ["ST.0", "ST.1", "ST.2"], "PROVED GIVEN CITED INPUT", "—", f"{U}, (4.35)", "theory/stability/front_end.py", "stability", "NONE", "YES", ""),
    ("Lemma S2.1 (c_n for all n)", ["ST.3"], "PROVED", "Theorem B", "—", "theory/stability/lipschitz_e.py", "stability, audibility", "NONE", "YES", "Reproved by two independent routes."),
    ("Lemma S2.2 (Hurwitz factorisation)", ["ST.4"], "PROVED", "Lemma S2.1", "Orlando", "theory/stability/lipschitz_e.py", "stability", "NONE", "YES", ""),
    ("Theorem S2 (Lipschitz, explicit constants)", ["ST.5"], "PROVED", "Lemmas S2.1-S2.2", "—", "theory/stability/lipschitz_e.py", "stability", "NONE", "YES", ""),
    ("Ostrowski input", ["ST.6"], "PROVED GIVEN CITED INPUT", "—", "Ostrowski, Acta Math. 72 (1940), Thm XXX, (71,1)", "—", "stability", "MINOR", "YES, REVISED",
     "gamma is the largest root modulus of both polynomials; follow Ostrowski's indexing of (69,3)-(69,4)."),
    ("Lemma S3 (explicit Rouché)", ["ST.7"], "PROVED", "—", "—", "theory/stability/roots_holder.py", "stability", "NONE", "YES", ""),
    ("Theorem S3 (combined stability)", ["ST.8"], "PROVED GIVEN CITED INPUT", "Prop S1, Thm S2, Lemma S3", U, "theory/stability/roots_holder.py", "stability", "NONE", "YES", ""),
    ("Proposition S3.2 (exponent 1/k sharp)", ["ST.9"], "PROVED", "Theorem B", "—", "theory/stability/roots_holder.py", "stability", "MINOR", "YES, REVISED",
     "(ii) needs a != 0, g(0) != 0 and prod(z_i+z_j) != 0 so that the recovery is defined."),
    ("Remark S3.3", ["ST.10"], "PROVED", "—", "—", "theory/stability/roots_holder.py", "stability", "NONE", "YES", ""),
    ("Theorem S4 (explicit threshold)", ["ST.11"], "PROVED GIVEN CITED INPUT", "Theorem S3", U, "theory/stability/threshold.py", "stability", "NONE", "YES", ""),
    ("Proposition S5 (certificates)", ["ST.12", "ST.13"], "PROVED", "Theorem B, Lemma S3", "—", "theory/stability/threshold.py", "stability", "MINOR", "YES, REVISED",
     "Write out why (I-A)^{-1}1>0 gives rho(A)<1 and invertibility, and why the tan majorant bounds the tanh remainder; state the radius set and the integer hypothesis."),
    ("Results table (delta_thm, delta_cert, delta_up)", ["ST.14"], "COMPUTATION", "Theorem S4, Proposition S5", U, "theory/stability/threshold.py", "stability", "MINOR", "YES, REVISED",
     "Every delta_thm, delta_cert, epsilon_cert re-certified exactly (P3). (2,2,2,2,3): delta_up <= 5.312e-05, ratio <= 6.72 (not 7.3/7.26). Regenerate threshold_output.md from threshold.py."),
    # ---------------- threshold note ----------------
    ("Lemmas 1-2 (one inequality; adjacent separation)", ["TH.0", "TH.1", "TH.2"], "PROVED", "lem:chamber, lem:bound", "—", "theory/threshold/threshold.py", "threshold", "NONE", "YES", ""),
    ("Theorem 1 (closed form S*(p))", ["TH.3"], "PROVED", "Lemma 1", "—", "theory/threshold/threshold.py", "threshold", "NONE", "YES", "P4: true for all p; p<=8 cases redone exactly."),
    ("Corollary 2 (no collision below 18)", ["TH.4"], "PROVED", "Theorem 1, Lemma 2", "—", "theory/threshold/threshold.py", "threshold", "NONE", "YES", ""),
    ("First-overlap vs first-collision table", ["TH.5"], "COMPUTATION", "—", "—", "theory/threshold/threshold.py", "threshold", "NONE", "YES", "All 14 rows reproduced."),
    ("Proposition 3 (tangency only at p=2,4)", ["TH.6"], "PROVED", "Theorem 1", "—", "theory/threshold/threshold.py", "threshold", "MINOR", "YES, REVISED",
     "P4: add 'S >= 3p+3' to part (1) (at S=3p+2 the gap is formally 0 for every p)."),
    # ---------------- curvature ----------------
    ("Flat-cone input (Kokotov)", ["CU.0", "CU.1"], "PROVED GIVEN CITED INPUT", "—", "Kokotov Prop 1, Thm 1; Uçar Thm 4.20 at kappa=0", "theory/curvature/curvature_checks.py", "curvature-divergence", "MINOR", "YES, REVISED",
     "Kokotov's deficiency space is span{chi, chi log r}; the orbifold domain forces Friedrichs. DGGW 4.8 does not give the vanishing or the remainder."),
    ("Lemma 2 (invariant multiplicities)", ["CU.2"], "PROVED", "—", "—", "theory/curvature/curvature_checks.py", "curvature-divergence", "MINOR", "REMARK ONLY", "Classical (Molien/Frobenius)."),
    ("Proposition (curvature comparison), Parts 1-2", ["CU.3"], "PROVED GIVEN CITED INPUT", "Lemma 2", "DGGW Thm 5.15, Prop 5.22; Thurston 13.3.6", "theory/curvature/curvature_checks.py", "curvature-divergence", "MINOR", "CITE AS PRIOR WORK",
     "DGGW Thm 5.15 / Prop 5.22 and Uçar Cor 4.21(iv); 'for every n' should be n>=2."),
    ("Proposition (curvature comparison), Part 3", ["CU.3"], "PROVED GIVEN CITED INPUT", "Theorem A, Theorem C", U, "theory/audibility/sharpness_search.py", "curvature-divergence", "NONE", "YES", ""),
    ("Proposition (curvature comparison), Part 4", ["CU.3"], "PROVED GIVEN CITED INPUT", "—", "Kokotov Thm 1", "theory/curvature/curvature_checks.py", "curvature-divergence", "MINOR", "REMARK ONLY",
     "Say 'rescaled to the same area'; name the Friedrichs extension."),
    # ---------------- divergence ----------------
    ("Lemma 1 (generating function, positivity, poles)", ["DV.0", "DV.1"], "PROVED GIVEN CITED INPUT", "—", "Uçar (4.25), (3.69)", "theory/divergence/divergence.py", "curvature-divergence", "NONE", "REMARK ONLY", ""),
    ("Theorem 2 (asymptotics of b_l(m))", ["DV.2"], "PROVED GIVEN CITED INPUT", "Lemma 1", "Uçar (4.25), (4.33)", "theory/divergence/divergence.py", "curvature-divergence", "MINOR", "REMARK ONLY",
     "Second form follows from the first but is not equivalent."),
    ("Theorem 3 (divergence rate hears M)", ["DV.3"], "PROVED GIVEN CITED INPUT", "Theorem 2, Lemma 1(b)", f"{U}, (4.35); Thurston 13.3.5", "theory/divergence/divergence.py", "curvature-divergence", "MINOR", "REMARK ONLY",
     "Genus-10^4 test: the smooth part dominates for l<=8 (not l<=5)."),
    ("Corollary 4 (peeling)", ["DV.4"], "PROVED GIVEN CITED INPUT", "Theorem 3", U, "theory/divergence/divergence.py", "curvature-divergence", "MINOR", "REMARK ONLY",
     "s_k>0 is used but not proved (one-line proof in the audit); 'and K' can be dropped. Uçar Cor 4.21(iv) already gives the determination."),
    ("Borel reading", ["DV.5"], "PROVED GIVEN CITED INPUT", "Theorem 3", "Dunne arXiv:2109.03897; Li-Li-Tang Ex. 2.30", "theory/divergence/divergence.py", "curvature-divergence", "MINOR", "REMARK ONLY", "Needs n>=1."),
    # ---------------- diophantine ----------------
    ("Proposition 1 (reformulation on C_lambda)", ["DI.1"], "PROVED", "—", "—", "theory/diophantine/variety_checks.py", "diophantine", "MINOR", "YES, REVISED",
     "'primitive sums' -> 'primitive triples t_i with sums s_i'; the rescaled triples lie in a class that may contain more points."),
    ("Pencil, Weierstrass model, fibres, generic torsion", ["DI.2"], "PROVED GIVEN CITED INPUT", "Proposition 1", "Beauville 1982 (table row); BGN 1993; Shioda (unretrieved, remark only)", "theory/diophantine/variety_checks.py", "diophantine", "MINOR", "YES, REVISED",
     "Base-point orders in listed order are 6,6,2,1,3,3 (not 1,2,3,3,6,6)."),
    ("Reciprocation = 2-torsion translation; dual family", ["DI.3"], "PROVED", "Proposition 1", "BGN p. 120", "theory/diophantine/variety_checks.py, families.py", "diophantine", "MINOR", "YES, REVISED",
     "'Differs by a point of infinite order' needs its short proof; the 12-point orbit holds for non-torsion P."),
    ("Proposition 2 (no linear families)", ["DI.4"], "PROVED", "—", "—", "theory/diophantine/families.py", "diophantine", "MINOR", "REMARK ONLY", "Exclude families whose entries are all proportional."),
    ("Theorem 3 (arbitrarily large fibres)", ["DI.5"], "PROVED GIVEN CITED INPUT", "Proposition 1", "Mazur's torsion theorem; BGN 'egg' (p. 119)", "theory/diophantine/cubic_group.py", "diophantine", "MINOR", "YES, REVISED",
     "Fix 'distinct choices give distinct classes' / 'multiplied by any m': the theorem holds because L is unbounded."),
    ("Rank certification of fibre curves", ["DI.6", "DI.11"], "COMPUTATION", "—", "PARI/GP 2.17.2 ellrank (unconditional with rational 2-torsion)", "theory/diophantine/ranks.py", "diophantine", "NONE", "YES",
     "Ranks 2,2,3,3 and C_{155/12} rank 2 PROVEN (r1=r2) and confirmed by an independent 2-isogeny descent."),
    ("Isolation of the base pair (rank C_{27/2} = 0)", ["DI.7"], "PROVED GIVEN CITED INPUT", "Proposition 1, thmB", "PARI/GP 2.17.2 ellrank/elltors", "theory/diophantine/ranks.py", "diophantine", "NONE", "YES",
     "P5: rank 0 unconditional (ellrank without GRH; exact 2-isogeny descent; analytic rank); 12 torsion points; pinned script agrees. Isosceles points are all of order 6 - provable, may replace 'as far as tested'."),
    ("Hyperbolicity of copies kD, k>=4", ["DI.8"], "PROVED", "—", "—", "—", "diophantine", "MINOR", "YES", "R<=3 holds for every positive triple."),
    ("Theorem 4 (c_iso X log X)", ["DI.9"], "PROVED", "DI.3, DI.8", "—", "theory/diophantine/families.py", "diophantine", "NONE", "YES", ""),
    ("Theorem 5 (X (log X)^2)", ["DI.10"], "PROVED", "DI.3, DI.8", "—", "theory/diophantine/families.py", "diophantine", "NONE", "YES", "Constant 3/(128 pi^4) re-derived exactly."),
    ("First fibres of each size (S=136, 408, 1849, 4600)", ["DI.11"], "COMPUTATION", "—", "—", "theory/diophantine/enumerate_fast.py", "diophantine, consistency", "SERIOUS", "YES, REVISED",
     "Reproduced exactly (S<=4800). 'share a_0 and a_1' uses Uçar's indexing; in the paper's t^l indexing write 'share c_1, c_2 (R and S_1)' - otherwise false."),
]


def main() -> int:
    out = ["# G5 theorem register", "",
           "One row per result. Statement text is verbatim from the source file (same anchored line",
           "ranges as `STATEMENTS.md`, produced by `build_register.py`). Status vocabulary: PROVED /",
           "PROVED GIVEN CITED INPUT / COMPUTATION / CONJECTURE / OPEN; CLAIM (FALSE) marks a sentence",
           "that is refuted. Audit verdict is the worst grade the independent reviewer assigned",
           "(FATAL / SERIOUS / MINOR / NONE), after the comparison phase. 'In paper' says whether the",
           "result should appear: YES, YES REVISED (with the change in the note), REMARK ONLY, CITE AS",
           "PRIOR WORK, or NO.", "",
           "Audit evidence: `review/audit/<folder>/REVIEW.md`, `COMPARISON.md` and `check_*.py`.", "",
           "## Summary", "",
           "| # | result | status | audit verdict | in paper? | source |",
           "|---|---|---|---|---|---|"]
    body = []
    counts: dict[str, int] = {}
    for i, (name, ids, status, deps, inputs, script, folders, verdict, inpaper, note) in enumerate(ROWS, 1):
        assert status in STATUSES, (name, status)
        assert verdict in {"FATAL", "SERIOUS", "MINOR", "NONE"}, (name, verdict)
        for f in folders.split(", "):
            assert (ROOT / "review/audit" / f / ("CONSISTENCY.md" if f == "consistency" else "REVIEW.md")).exists(), (name, f)
        srcs = sorted({INDEX[r][1][2] for r in ids})
        counts[status] = counts.get(status, 0) + 1
        out.append(f"| {i} | {name} | {status} | {verdict} | {inpaper} | {', '.join('`'+s+'`' for s in srcs)} |")
        blocks = []
        for rid in ids:
            assert rid in INDEX, (name, rid)
            _, (_, title, rel, a, b, anchor) = INDEX[rid]
            blocks.append(f"*{rid}, `{rel}` lines {a}-{b}:*\n\n````\n{bs.excerpt(rel, a, b, anchor, rid)}\n````")
        body.append(
            f"### {i}. {name}\n\n"
            f"| field | value |\n|---|---|\n"
            f"| status | {status} |\n| dependencies | {deps} |\n| external inputs | {inputs} |\n"
            f"| source file | {', '.join('`'+s+'`' for s in srcs)} |\n| verifying script (existing) | {script} |\n"
            f"| audit evidence | {', '.join('`review/audit/'+f+'/`' for f in folders.split(', '))} |\n"
            f"| audit verdict | {verdict} |\n| in paper? | {inpaper} |\n| note | {note or '—'} |\n\n"
            + "\n\n".join(blocks) + "\n")
    out += ["", "**Counts by status:** " + "; ".join(f"{k}: {v}" for k, v in sorted(counts.items())) +
            f"; total {len(ROWS)}.", "",
            "Multi-result excerpts (e.g. PC.1 for thmA-corD, AU.1 for Theorems A-C, CU.3 for Parts 1-4) are"
            " repeated under each row they support.", "", "## Rows", ""] + body
    OUT.write_text("\n".join(out) + "\n")
    print(f"wrote {OUT.relative_to(ROOT)}: {len(ROWS)} rows; " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
