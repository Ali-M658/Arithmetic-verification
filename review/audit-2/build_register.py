#!/usr/bin/env python3
"""Build review/audit-2/REGISTER-ADDENDUM.md: one row per audited result, in the format of
review/audit/THEOREM-REGISTER.md (summary table, then per-item verbatim statements).

The verbatim statements are re-rendered from the sources by build_statements.py (same anchors, same
no-proof asserts). The grades are the worst grade assigned after the comparison phase, taken from
<group>/REVIEW.md and <group>/COMPARISON.md. Exits nonzero if a row names an unknown item or a
grade outside the vocabulary.

Run from the repository root:  python3 review/audit-2/build_register.py
"""
from __future__ import annotations

import importlib.util
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("bs", ROOT / "review/audit-2/build_statements.py")
bs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bs)

GRADES = {"FATAL", "SERIOUS", "MINOR", "NONE"}
STATUS = {"PROVED", "PROVED GIVEN CITED INPUT", "COMPUTATION", "CITED CLAIM", "OPEN", "CLAIM (FALSE AS PRINTED)"}

PS, PG, PW, TF, DE, SB, TH, LIT = ("pte-structure", "pte-growth", "pte-witnesses", "trace-formula",
                                   "descent", "stability", "threshold-sharpness", "literature")

# (id, group, items, result, status, depends on, external inputs, source, verifying script, grade, in paper?, note)
ROWS = [
    # ---- pte-structure
    ("A1", PS, "PS.0", "Definition 1.1, Lemma 1.2 (dictionary), items 1-5", "PROVED GIVEN CITED INPUT",
     "[Sig] Lemma 2, Lemma 4, Theorem S", "[Sig] (H1)-(H3)", "theory/pte/proof.md 49-85",
     "pte-structure/check_dictionary.py", "MINOR", "YES, REVISED",
     "'U minus {1}' must mean removing every 1; the genus choice and its existence; for L>=2 the smaller genus is 0, so genus 1 is only needed for L=1; 'Area<2 pi T' is true but loose (Area/2pi<T-L-2)."),
    ("A2", PS, "PS.1", "Theorem 2.1 (Descartes bound |iota|<=T-2L; |U*|+|V*|>=2L+2|g-g'|; equality shape)", "PROVED",
     "Lemma 1.2", "none", "theory/pte/proof.md 141-147", "pte-structure/check_descartes.py, check_attain.py", "NONE", "YES",
     "Equality in the displayed inequality does not force shape {L,L+2}: only size 2L+2 does."),
    ("A3", PS, "PS.2", "Proposition 2.2 (tau_L >= N(2L-2))", "PROVED", "Lemma 1.2", "none",
     "theory/pte/proof.md 174-175", "pte-structure/check_ps6.py", "NONE", "YES", "tau_L is defined in Definition 1.3."),
    ("A4", PS, "PS.3", "Proposition 2.3 (symmetric constructions are balanced), (a)(b)(c)", "PROVED",
     "Theorem 2.1, Theorem 3.1", "Borwein-Ingalls p. 8 (definition only)", "theory/pte/proof.md 184-194",
     "pte-structure/check_balanced.py", "NONE", "YES", "'no pair' in (a) is redundant."),
    ("A5", PS, "PS.4", "Theorem 3.1 (pencil: ideal balanced configurations)", "PROVED", "Theorem 2.1, [Sig] Lemma 5 (Newton parity)",
     "none", "theory/pte/proof.md 223-233", "pte-structure/check_pencil.py, check_pencil_fibre.py", "MINOR", "YES, REVISED",
     "The 'Equivalently' clause needs e_k(A)=0 for odd k<r together with the product identity and kappa != 0."),
    ("A6", PS, "PS.5", "Proposition 3.2 (shift)", "PROVED", "none", "none", "theory/pte/proof.md 267-274",
     "pte-structure/check_shift.py", "MINOR", "YES, REVISED", "Add n>=1 (n=0 gives rho=0)."),
    ("A7", PS, "PS.6", "statements.tex versions of Theorem (Descartes), Proposition (balanced), and the section opening", "CLAIM (FALSE AS PRINTED)",
     "Lemma 1.2", "none", "theory/pte/statements.tex 13-53", "pte-structure/check_ps6.py", "SERIOUS", "YES, REVISED",
     "The sentence 'share their first L heat coefficients exactly when Z is an L-configuration' omits the genus condition iota(Z)=2(g'-g); counterexample (2;15) vs (0;3,3,5,5). Also add 0 not in A; fix the equality-shape wording."),
    # ---- pte-growth
    ("B1", PG, "PG.0", "Definitions 1.3, 1.4, Lemma 1.5 (N_odd(L)<=N(2L-3); <=(L-1)^2+1; =L for 3<=L<=6)", "PROVED GIVEN CITED INPUT",
     "Lemma 1.2", "Chen survey A.1.6/17/26/33 (numbers re-verified), Borwein-Ingalls Props 2-3 (re-proved)",
     "theory/pte/proof.md 99-124", "pte-growth/check_lemma15.py", "MINOR", "YES",
     "N_odd(L)=L also holds at L=2; T^cone_L must name the cancelled primitive pair of Lemma 1.2(2)."),
    ("B2", PG, "PG.1", "Proposition 3.3 (doubling), including the n=2 and n=3 cases", "PROVED", "Lemma 1.2", "none",
     "theory/pte/proof.md 283-293", "pte-growth/check_doubling.py", "MINOR", "YES, REVISED",
     "With 1 in X cap Y or multiplicities, '1 in X minus Y' is false (X={1,1,5}, Y={1,3,3}): state cone counts 3n-mu_X, 3n-mu_Y; state that the pair shares its first L coefficients; cite |V|=3n for the area bound, not Lemma 1.2(5)."),
    ("B3", PG, "PG.2", "Theorem 3.4 (tau_L<=6N_odd(L); T_L<=4N(2L-3); T^cone_L<=6N(2L-3))", "PROVED", "Props 3.2, 3.3, Lemma 1.5",
     "Borwein-Ingalls Prop 3", "theory/pte/proof.md 311-314", "pte-growth/check_upper.py", "MINOR", "YES, REVISED",
     "T^cone_L needs the cancelled genus-0 realisation hyperbolic (proved for L>=3, checked at L=2) and 1 surviving cancellation; the '[Sig] N(a)' citation for 2^{2L-1} should cite the construction."),
    ("B4", PG, "PG.3", "Theorem 4.1 (square-root lower bound on f(A))", "PROVED", "Prop 3.3, Lemma 1.5", "none",
     "theory/pte/proof.md 329-332", "pte-growth/check_growth.py", "NONE", "YES", "Floor expression checked exactly at every breakpoint for A>=8 pi."),
    ("B5", PG, "PG.4", "Theorem 4.2 (a)(b)(c): f(A)>=c A^alpha iff N(k)<=C k^{1/alpha}; f=Theta(A) iff N(k)=O(k)", "PROVED GIVEN CITED INPUT",
     "[Sig] Cor S2/T1 (|U|+|V|<=2floor(A/pi)+8), Theorem 4.1, Prop 2.2", "none", "theory/pte/proof.md 342-351",
     "pte-growth/check_growth.py", "MINOR", "YES, REVISED",
     "Add L>=2 in (a), beta>0 in (b); the constant 2 floor(A/pi)+8 uses that |U|+|V| is even."),
    ("B6", PG, "PG.5", "Theorem 4.3 (genus alone, cone count alone)", "PROVED", "Theorem 3.4, Lemma 1.2(5)", "none",
     "theory/pte/proof.md 380-390", "pte-growth/check_growth.py", "MINOR", "YES, REVISED",
     "Define f_g and f_n exactly; explicit constants f_g(A)>=sqrt(A/16 pi) for A>=16 pi and f_n(A)>=sqrt(A/12 pi) for A>=8 pi."),
    ("B7", PG, "PG.6", "statements.tex Theorem (Growth), (a)(b)(c) and the closing sentence", "PROVED", "B3-B6", "none",
     "theory/pte/statements.tex 55-70", "pte-growth/check_growth.py", "MINOR", "YES, REVISED",
     "(b) needs L>=2; the sketch of (c) omits the second scaled balanced shift; the last sentence uses undefined quantities."),
    # ---- pte-witnesses
    ("C1", PW, "PW.4", "The 18 explicit pairs (genus pairs L=2..7, balanced pairs, genus-0 pairs with different cone counts), each sharing exactly L coefficients; includes the 7-vs-8 cone pair, the L=3 same-genus pair of area 2 pi 22/15, and the L=4..7 pairs",
     "COMPUTATION", "heat coefficients (A. trace-formula group)", "none (coefficients recomputed from first principles; Ucar (4.25) cross-check l<=12)",
     "theory/pte/data/witnesses.json", "pte-witnesses/check_*.py", "NONE", "YES", "All 18: hyperbolic, equal exact area, distinct signatures, exactly L shared."),
    ("C2", PW, "PW.0", "Headline table (proof.md section 0 items 5, 6)", "COMPUTATION", "C1", "none", "theory/pte/proof.md 32-47",
     "pte-witnesses/check_*.py", "MINOR", "YES, REVISED", "'Real solutions exist in abundance' unsupported: they form a nonempty open set; for integer Y<=24 only 635 of 98,280 give one."),
    ("C3", PW, "PW.1", "Example (Small pairs)", "CLAIM (FALSE AS PRINTED)", "C1, Theorem C(3)", "none", "theory/pte/statements.tex 101-120",
     "pte-witnesses/check_*.py", "SERIOUS", "YES, REVISED",
     "'Previously the smallest area known to share three coefficients was 2 pi 14/5' contradicts Theorem C(3): the 22/15 pair is already its n=4 witness."),
    ("C4", PW, "PW.1", "Remark (The first open case): shape (3,5) and the T_3 search claim", "COMPUTATION", "Theorem 2.1", "none",
     "theory/pte/statements.tex 122-127", "pte-witnesses/t3run, check_cmp_t3filter.py", "NONE", "YES, REVISED",
     "Independent exact modular search over every Y<=220 (4,493,032,544 multisets): no solution; planted controls recovered. 'abundance' and 'made primitive' wording: MINOR."),
    ("C5", PW, "PW.2", "Improved lower bounds on f in the covered range", "PROVED GIVEN CITED INPUT", "C1, Theorem 4.1 logic", "none",
     "theory/pte/proof.md 457-470", "pte-witnesses/check_*.py", "MINOR", "YES, REVISED",
     "'Area/2pi ~ T/2-2' fails for L=2,3; 'grows at least linearly for A/2pi<=18' has no content on a bounded range; replace by A_L/2pi<2L-3 for 2<=L<=5."),
    ("C6", PW, "PW.3, PW.5", "The 61 integer sharpness witnesses for Theorem A at n=4 (and the count of 25 at entries <= 130)", "COMPUTATION", "Theorem 3.1",
     "none", "theory/pte/proof.md 253-263, data/pencil_m4_N220.json", "pte-witnesses/check_*.py", "MINOR", "YES, REVISED",
     "All 61 verified and the set reproduced exactly; but the range is |a|,|b|,|c|<=N with the fourth entry unrestricted (all-entries counts are 15 and 35)."),
    ("C7", PW, "PW.3", "'So Theorem C(3) at n=4 is a pencil phenomenon'", "CLAIM (FALSE AS PRINTED)", "C6", "none", "theory/pte/proof.md 262-263",
     "pte-witnesses/direct4_N440.txt", "SERIOUS", "YES, REVISED",
     "Exhaustive search of 4-cone pairs with orders <= 440: 107 primitive witnesses, 6 without pencil splitting, smallest (0;16,16,74,74) ~ (0;11,37,44,88) (R=45/296, P1=180, P3=818640)."),
    ("C8", PW, "PW.3", "n=5: no pencil witness with all entries <= 200 ('1,592 sets')", "COMPUTATION", "Theorem 3.1", "none",
     "theory/pte/proof.md 264-265", "pte-witnesses/n5_N200_mode1.txt", "MINOR", "YES, REVISED",
     "1,592 counts sets with >=3 entries in [-200,200] (A and -A separately); 602 have all entries in [-200,200]. 'No pencil pair' holds under every reading."),
    ("C9", PW, "(proof.md 7)", "Converse of Theorem 3.1 at size 8 ('every balanced size-8 3-configuration is a pencil point'): recorded as unproved, observed for entries <= 80", "OPEN",
     "Theorem 3.1", "none", "theory/pte/proof.md 531-545", "pte-witnesses/direct4_N440.txt", "MINOR", "NO",
     "Now refuted: balanced size-8 configurations without pencil splitting exist from entries 88 (the 6 witnesses of C7). No 4-cone pair with order 1 up to 440, extending 'none with orders <= 80'."),
    # ---- trace-formula
    ("D1", TF, "TF.1", "Elliptic moments lemma (i)(ii)", "PROVED", "Euler beta integral", "Dryden-Strohmaier eq (1) (weights)", "theory/revision/lemma25.tex 16-39",
     "trace-formula/check_closedform.py", "NONE", "YES", "F_a, 0<a<2 pi, weights 1/(2m sin theta_j) match DS eq (1) p. 3."),
    ("D2", TF, "TF.2", "Closed form Phi_m(u)=(cot u - m cot mu)/(4m sin u), sigma_i>0, Bernoulli expression (phik)", "PROVED", "Liouville, Bernoulli numbers", "none",
     "theory/revision/lemma25.tex 50-67", "trace-formula/check_closedform.py", "NONE", "YES", "Three independent computations agree, m<=12, k<=40; sigma_i=(4^i-2)|B_2i|/(2i)!."),
    ("D3", TF, "TF.3", "Lemma (the hyperbolic term is small)", "PROVED GIVEN CITED INPUT", "counting lemma (audited), trace formula", "DS eq (1)",
     "theory/revision/lemma25.tex 87-93", "trace-formula/check_hypbound.py", "MINOR", "YES, REVISED",
     "Define the systole as least length over all hyperbolic classes incl. through cone points; 'Orb in Sig' is a type error; the fragment has no written proof (points to Theorem 4.9(b), which quotes the lemma): insert the proof."),
    ("D4", TF, "TF.4", "Proposition (heat expansion at curvature -1): alpha_k, b_l(m)=(-1)^l p_l(m)/m, c_j", "PROVED GIVEN CITED INPUT", "D1-D3", "DS eq (1), DGGW Thm 4.8 (Z(s)=O(1/s))",
     "theory/revision/lemma25.tex 101-119", "trace-formula/check_conepoly.py", "NONE", "YES", "Signatures (H3) uses alpha_l for what this calls alpha_{l+1}/(4 pi): do not use one symbol for both."),
    ("D5", TF, "TF.5", "Lemma 2.5 for every order: p_l even, degree 2l+2, p_l(1)=0, leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)), p_l(m)>0 for m>1", "PROVED", "D2",
     "none", "theory/revision/lemma25.tex 145-152", "trace-formula/check_conepoly.py", "NONE", "YES",
     "p_l=sum_n w_{l,n}(m^{2n}-1) with all weights products of positive rationals; exact for l<=40, m=1..30."),
    ("D6", TF, "TF.5", "Printed first values alpha_0..alpha_4 and p_0,p_1,p_2, with the Schueth/DGGW attribution", "PROVED GIVEN CITED INPUT", "D4", "Schueth Rem 4.2, Thm 4.1; DGGW 5.6; Ucar (4.35)",
     "theory/revision/lemma25.tex 166-173", "trace-formula/check_conepoly.py", "MINOR", "YES, REVISED",
     "Values correct; the attribution sentence reads as crediting DGGW with p_2: Schueth credits DGGW 5.6 with a_0, a_1 only. No existing script tests p_2 against Schueth."),
    ("D7", TF, "TF.6", "Remark rem:ucaragree: agreement with Ucar for every l", "PROVED GIVEN CITED INPUT", "D4, D5", "Ucar (4.25), (4.33)-(4.35), Thm 4.20(ii)",
     "theory/revision/lemma25.tex 175-188", "trace-formula/check_ucar.py", "MINOR", "YES, REVISED",
     "Holds for every l with the (-1)^l sign, no index shift; cite Thm 4.20(ii) (p. 138) beside (4.33)-(4.34); use kappa."),
    ("D8", TF, "TF.7", "Remark 4.12: independence of the trace-formula proof from the coefficient computations", "PROVED GIVEN CITED INPUT", "D4", "DGGW Thm 4.8 (Z(s)=O(1/s))",
     "theory/revision/remark412.tex 17-61", "trace-formula/check_hypbound.py", "MINOR", "YES, REVISED",
     "Say 'independent of the coefficient computations'; the 'or Weyl's law' clause is not independent; state the test-function class as h=g-hat, g smooth even compactly supported (DS's 'entire of uniform exponential type' admits h=1); sentence (1B) must not be combined with locality.tex."),
    ("D9", TF, "TF.8", "Theorem 1.2(iii): the constant C(A,l,D)", "PROVED GIVEN CITED INPUT", "D3", "none", "theory/revision/thm12iii.tex 10-23, 31-36",
     "trace-formula/check_hypbound.py", "NONE", "YES, REVISED",
     "C re-derives exactly; replacing each orbifold's systole/diameter by the smaller/larger is justified (bound decreasing in l and increasing in D on the range, interval-arithmetic checked on 390 cells): add that line."),
    ("D10", TF, "TF.8", "Theorem 1.2(iii) 'attained' statement (three cases)", "PROVED GIVEN CITED INPUT", "D3", "DS eq (1)", "theory/revision/thm12iii.tex 16-23",
     "trace-formula/check_hypbound.py", "NONE", "YES", "Weighted, all-class and primitive length spectra first differ at the same length."),
    # ---- descent
    ("E1", DE, "DE.0", "phi, psi are mutually inverse isomorphisms over Q between C_{27/2} and E: y^2=x(x+9)(x+384)", "PROVED", "none", "none", "theory/revision/descent.tex 23-37",
     "descent/check_a_isomorphism.py", "MINOR", "YES, REVISED", "phi undefined at the 3 points with Z=0: state the extension phi(O)=origin, phi(1:0:0)=(216,5400), phi(0:1:0)=(216,-5400); give the nonsingularity argument."),
    ("E2", DE, "DE.1", "rank E(Q)=0 by 2-isogeny descent (Selmer groups {+-1,+-6} and {1})", "PROVED GIVEN CITED INPUT", "E1", "Cremona 3.6 (3.6.2)", "theory/revision/descent.tex 39-72",
     "descent/check_b_descent.py", "NONE", "YES", "Local tests are at all p | 2dd' (the classes +-2,+-3 on E fail only at p=5); independent full 2-descent gives 2-Selmer of order 4."),
    ("E3", DE, "DE.2", "E(Q)_tors = Z/2 x Z/6, the twelve points and their orders", "PROVED GIVEN CITED INPUT", "E1", "Cremona 3.3 p. 70", "theory/revision/descent.tex 74-82",
     "descent/check_c_torsion.py", "MINOR", "YES, REVISED",
     "Remark 'tangent at (16,400) meets E again at (16,-400)' is false: (16,400) is a flex; write 'meets E only at (16,400), multiplicity 3, so 2(16,400)=(16,-400)=-(16,400)'."),
    ("E4", DE, "DE.3", "The twelve rational points of C_{27/2}; positive ones are the permutations of (1,4,4) and (1,1,4)", "PROVED", "E2, E3", "none", "theory/revision/descent.tex 84-87",
     "descent/check_d_points_triads.py", "NONE", "YES", "Also confirmed by a search to height 80 independent of the descent."),
    ("E5", DE, "DE.4", "Triads with S_1=18k and R=3/(4k) are permutations of (2k,8k,8k) or (3k,3k,12k)", "PROVED", "E4", "none", "theory/revision/descent.tex 89-91",
     "descent/check_d_points_triads.py", "MINOR", "YES, REVISED", "True for integer k>=1; k=3/2 gives only (3,12,12). State 'k>=1 an integer; hyperbolic since R<1 and all entries >= 2k >= 2'."),
    ("E6", DE, "DE.5", "Theorem 5.16 (isolation of the base pair)", "PROVED GIVEN CITED INPUT", "E2-E5", "Cremona", "review/audit/statements/diophantine.md DI.7",
     "descent/check_e_isolation.py", "MINOR", "YES, REVISED",
     "'every integer k>=1'; base the proof on the descent and torsion, PARI as cross-check only; drop '(as far as tested)': every isosceles point (u:v:v) has order 6."),
    ("E7", DE, "DE.6", "Coordinates of 3P on C_{155/12}: 3P=(162833463:723926268:287876366)", "COMPUTATION", "none", "none", "theory/revision/point3P.tex 6-7",
     "descent/check_f_3P.py", "NONE", "YES", "Printed old point = (1:0:-1)-3P = Y<->Z transposition of 3P: same triad; O=(1:-1:0) is a flex of every C_lambda."),
    # ---- stability
    ("F1", SB, "SB.2", "Proposition 6.10, steps 1-3 (Delta, tau^lin, tau^rem, rho_j, rho^rem_j, Delta_M, A)", "PROVED", "Prop S5", "none", "theory/revision/prop610.tex 14-48",
     "stability/check_cert.py, check_probes.py", "NONE", "YES, REVISED", "26,924 exact probes, 0 violations."),
    ("F2", SB, "SB.2", "The matrix J=d(Me-b)/dI and G=-M^{-1} J F^{-1}", "PROVED", "F1", "none", "theory/revision/prop610.tex 42-48",
     "stability/check_setup.py", "NONE", "YES", "Matches sympy differentiation for n=2..6."),
    ("F3", SB, "SB.1, SB.2", "Notation: rho used for data radii, residual bound and spectral radius; 'steps 4,5 unchanged'", "PROVED", "F1", "none", "theory/revision/prop610.tex 42-43",
     "stability/check_cert.py", "MINOR", "YES, REVISED", "Rename the Prop S5 radii delta_nu; first-order term sum_c delta_c sum_l |p_c^{(l)}(a)/l!| r^l; state F=L."),
    ("F4", SB, "SB.3", "Claim after Table 4 (series truncation and 'at most four nonzero (odd) coefficients')", "PROVED", "F1", "none", "theory/revision/prop610.tex 63-65",
     "stability/check_setup.py", "MINOR", "YES, REVISED",
     "'(odd)' is false for sech^2 U; replacement: the odd series have at most four nonzero coefficients (z,z^3,z^5,z^7), the even series sech^2 U and sec^2 U at most four (1,z^2,z^4,z^6)."),
    ("F5", SB, "SB.4", "Every printed delta_cert (11 rows)", "COMPUTATION", "F1, Prop S5", "none", "review/audit/statements/stability.md ST.14",
     "stability/check_cert.py", "NONE", "YES", "All pass by test (ii); each is the exact 4-s.f. maximum."),
    ("F6", SB, "SB.4", "Every printed delta_thm (11 rows)", "COMPUTATION", "Theorems S2, S3", "none", "ST.14", "stability/check_cert.py", "NONE", "YES", "Each equals the exact value rounded down to 3 s.f. and passes both tests."),
    ("F7", SB, "SB.4", "Every printed eps_cert (uniform relative)", "COMPUTATION", "F1", "none", "ST.14", "stability/check_cert.py", "NONE", "YES",
     "All pass, each the 2-s.f. maximum. Producer's threshold_output.md prints 4 s.f. rounded to nearest: five rows do not certify there (fmt_down needed). MINOR in that file only."),
    ("F8", SB, "SB.4", "The relative-precision column delta_cert/|H_nu|", "COMPUTATION", "F5", "none", "ST.14", "stability/check_cert.py", "MINOR", "YES, REVISED",
     "(2,3,7), nu=0: 3.9e-03 not 4.0e-03 (computed from the unrounded 3.65881e-03)."),
    ("F9", SB, "SB.4", "The delta_up column and ratio", "COMPUTATION", "ST.13", "none", "ST.14", "stability/search_dup.py, check_dup.py", "MINOR", "YES, REVISED",
     "(2,2,2,2,3): 5.743e-05 and 7.26 must read 5.312e-05 and 6.72 (threshold_output.md already does; proof.md l.446 and STATUS.md l.53 stale); (3,10,15,30): 7.487e-03 (optional)."),
    # ---- threshold-sharpness
    ("G1", TH, "TH.1", "Theorem 5.13 (threshold): p+q+r<=17 determined by the first two invariants; 17 sharp", "PROVED", "separation theorem (audited)", "none", "theory/revision/thm513.tex 11-15",
     "threshold-sharpness/check_collisionfree.py", "NONE", "YES, REVISED", "Add: the first two invariants determine S_1 (eq:s1inv), so a sum<=17 collides only within its own sum."),
    ("G2", TH, "TH.1", "Proposition (collision-free sums): exactly 38 sums in [18,4800]", "COMPUTATION", "none", "none", "theory/revision/thm513.tex 24-33",
     "threshold-sharpness/check_collisionfree.c, .py", "NONE", "YES", "Independent exact C search: the 38 sums, 25,575 triads at 557; each of the other 4745 sums has a collision; 3962 covered by scaling, 783 uncovered with a collision."),
    ("G3", TH, "TH.1", "Method claims (scaling lemma, 3962/783, first pairs at 18, 20, 26)", "COMPUTATION", "G2", "none", "theory/revision/thm513.tex 35-47",
     "threshold-sharpness/check_collisionfree.py", "NONE", "YES", "collision_witnesses.csv: 783 rows, same sums as the blind set."),
    ("G4", TH, "TH.2", "Sharpness wording: 1/k for arbitrary data; 1/2 at a double order and when all orders are equal", "PROVED GIVEN CITED INPUT", "Theorems S3, S4", "none",
     "theory/revision/sharpness.tex 21-44", "threshold-sharpness/check_sharpness.py", "MINOR", "YES, REVISED",
     "Say 'positive real orders'; 'all n>=2 orders equal'; Remark S3.3 should read d_i >= -a (|d_i|<=a is sufficient) and give max|d_i|<=((498+42a^2)delta/(2a))^{1/2}; n=1 is Lipschitz."),
    ("G5", TH, "TH.3", "Remark 6.8 addition: family (a+s,a-s,a,...,a) attains 1/2; k>=3 witnesses are not heat invariants of any real multiset", "PROVED", "G4", "none",
     "theory/revision/sharpness.tex 47-59", "threshold-sharpness/check_sharpness.py", "NONE", "YES", "check_sharpness.py tests only n=3,4 at a=8; the general claims rest on the written argument, re-proved blind."),
    # ---- literature
    ("H1", LIT, "LIT.0 B1-B4", "Borwein-Ingalls: N(k) definition (p. 6); Prop 2: N(k)>=k+1; Prop 3: N(k)<=k(k+1)/2+1; Prop 1 content", "CITED CLAIM", "none", "Borwein-Ingalls 1994",
     "theory/pte/LITERATURE.md; proof.md", "literature/check_lifting_and_bounds.py", "MINOR", "YES, REVISED",
     "Prop 1 is the three equivalent forms of the problem, not a bound; cite Hardy-Wright for pigeonhole (Melzak credits it); statements.tex cites BI s. 1 for N(k): it is s. 2, p. 6. Source read from a scan (gap: e-periodica captcha)."),
    ("H2", LIT, "LIT.0 B5, M1", "Wright and Melzak bounds N(k)<=(k^2-3)/2 (odd), (k^2-4)/2 (even)", "CLAIM (FALSE AS PRINTED)", "none", "Melzak CMB 4 p. 233-234; BI p. 7",
     "theory/pte/proof.md 19-22, 371-373; statements.tex 93", "literature/check_lifting_and_bounds.py", "SERIOUS", "YES, REVISED",
     "The formula (copied accurately from BI p. 7) is false for k=2,3 and is not in Melzak; Melzak reports Wright's K(n)<=(n^2+4)/2 (n = degree). Replacement: 'The pigeonhole bound N(k)<=k(k+1)/2+1 [Hardy-Wright; BI Prop. 3] was improved by Wright (1935) to N(k)<=(k^2+4)/2 (as reported by Melzak, CMB 4 (1961), p. 234). Melzak gave an exact non-constructive formula and numerical upper bounds for k<=29 [ibid., Table 1]. None is o(k^2), and N(k)=o(k^2) remains open [BI s. 6 Problem 3; Croot-Mao-Yip 2026].'"),
    ("H3", LIT, "LIT.0 B7, O4", "N(k)=o(k^2) is open ('no progress for many years'); no sub-quadratic bound exists", "CITED CLAIM", "none", "BI s. 6 Q3; Croot-Mao-Yip 2026; Wooley",
     "theory/pte/proof.md 21-24, 374-376", "literature/search/", "MINOR", "YES, REVISED",
     "Adversarial search finds no refereed counterexample. Problem 4 (M(k)=O(k^2)) was solved by Wooley 2012: drop 'no progress on questions 3 and 4'. One unrefereed preprint (Sun-Zhao arXiv:2307.11330) claims Wright's conjecture: footnote optional."),
    ("H4", LIT, "LIT.0 B8-B12", "BI p. 8 odd symmetric definition; p. 9/25 explicit solutions; Prouhet p. 4; Smyth Prop 4; Lemma 2", "CITED CLAIM", "none", "Borwein-Ingalls", "LITERATURE.md",
     "literature/check_solutions.py", "MINOR", "NO", "All 14 printed solutions verified exactly; BI credits 'Letac and Gloden' jointly: cite BLP p. 2069 and CMSV p. 2 for Letac."),
    ("H5", LIT, "LIT.0 W1-W2, C1-C3, D1-D4", "Wooley Thm 1.3 (2012), Thm 13.1 (2019); Croot-Mao-Yip p. 1; CMSV p. 2 (ideal solutions known for k<=9 and k=11)", "CITED CLAIM", "none",
     "arXiv texts", "statements.tex 97-98", "literature/REVIEW.md", "NONE", "YES", "W(k,2) is the exact-degree quantity M(k), not N(k); size/degree conventions consistent."),
    ("H6", LIT, "LIT.0 P1-P2", "BLP 2003: parametric ideal solutions for n=1..8, 10; Gloden family; size-10 solutions", "CITED CLAIM", "none", "BLP 2003", "LITERATURE.md",
     "literature/check_solutions.py", "MINOR", "NO", "The two-parameter family is BLP's reduction of Gloden's four-parameter solution; BLP do not name Letac for the 9-sets."),
    ("H7", LIT, "LIT.0 S1", "Chen survey A.1.6, A.1.17, A.1.26, A.1.33: [1,5,5]=[2,3,6]; [1,13,17,23]=[3,9,21,21]; [3,19,37,51,53]=[9,11,43,45,55]; [7,91,...]=[29,59,...]", "CITED CLAIM",
     "none", "Chen survey arXiv:2506.11429", "proof.md Lemma 1.5(3)", "literature/check_solutions.py", "NONE", "YES", "All 16 solutions and attributions confirmed (A.48, A.313, A.314-A.316 are equation numbers inside those sections)."),
    ("H8", LIT, "LIT.0 S2", "eslpower.org Theorem 3 (lifting) underlies Proposition 2.2", "CITED CLAIM", "none", "eslpower.org TarryPrb.htm", "proof.md 180-182",
     "literature/check_lifting_and_bounds.py", "NONE", "YES", "Identity verified; non-triviality (Z != -Z) holds for configurations because they have no pair {z,-z}."),
    ("H9", LIT, "LIT.0 S3-S4", "Chen negative exponents: 33 types (s. 1.2.1, Ex. 1.7, p. 16 and p. 275); type (-1,1,3): [3,10,15,30]=[4,5,21,28] (A.685); type (-1,1,3,...,2L-3), L>=4 'does not appear'", "CITED CLAIM",
     "none", "Chen survey", "LITERATURE.md 128, 135-136", "literature/check_solutions.py", "MINOR", "YES, REVISED",
     "'Does not appear' is contradicted as worded ((-1,1,3,5) appears in Ex. 2.36, (3.33), (5.107)); say 'no numerical solution is listed for (-1,1,3,...,2L-3), L>=4'. Section number is 1.2.1, not 1.4."),
    ("H10", LIT, "LIT.0 M2, O1-O3", "Melzak Table 1 (n<=29); Caley p. 2 (k log k concerns v(k)); Choudhry (k<=7); Prouhet", "CITED CLAIM", "none", "sources", "LITERATURE.md",
     "literature/REVIEW.md", "NONE", "NO", "Confirmed."),
    ("H11", LIT, "bibliography", "references-pte.bib metadata", "CITED CLAIM", "none", "Crossref, arXiv", "theory/pte/references-pte.bib", "literature/COMPARISON.md", "MINOR", "YES, REVISED",
     "cmsv2024 lacks DOI 10.1090/mcom/3917; wooley2019 lacks 10.1112/plms.12204; melzak1961 is in the bib but uncited; add Hardy-Wright and Wooley 2012 if the suggested sentences are used."),
]


def main() -> int:
    items = {}
    for g, sp in bs.GROUPS.items():
        for iid, title, segs in sp["items"]:
            items[iid] = (g, title, segs)
    cnt_grade, cnt_status = Counter(), Counter()
    for r in ROWS:
        rid, g, itm, res, st, dep, ext, src, scr, gr, inp, note = r
        assert gr in GRADES, (rid, gr)
        assert st in STATUS, (rid, st)
        assert g in bs.GROUPS, (rid, g)
        cnt_grade[gr] += 1
        cnt_status[st] += 1
    out = ["# G5-bis theorem register addendum\n",
           "One row per audited result. Statement text is verbatim from the source file (same anchored line ranges as "
           "`STATEMENTS.md`, produced by `build_statements.py`; the per-item text is reproduced below the table). "
           "Status vocabulary as in `review/audit/THEOREM-REGISTER.md`; CLAIM (FALSE AS PRINTED) marks a sentence that is "
           "refuted or contradicts another result of the paper, while the underlying mathematics may be fine. "
           "Audit verdict is the worst grade after the comparison phase (FATAL / SERIOUS / MINOR / NONE). "
           "'In paper' says whether the result belongs in the paper: YES, YES REVISED (with the change in the note), CITE AS PRIOR WORK, or NO.\n",
           "Audit evidence: `review/audit-2/<group>/REVIEW.md` (blind), `COMPARISON.md`, `check_*.py` with outputs.\n",
           "## Summary\n",
           "| # | group | items | result | status | audit verdict | in paper? | source |",
           "|---|---|---|---|---|---|---|---|"]
    for r in ROWS:
        rid, g, itm, res, st, dep, ext, src, scr, gr, inp, note = r
        out.append(f"| {rid} | {g} | {itm} | {res} | {st} | {gr} | {inp} | `{src}` |")
    out += ["", "## Counts", "", "| status | count |", "|---|---|"]
    out += [f"| {k} | {v} |" for k, v in sorted(cnt_status.items())]
    out += ["", "| verdict | rows |", "|---|---|"]
    out += [f"| {k} | {cnt_grade.get(k, 0)} |" for k in ("FATAL", "SERIOUS", "MINOR", "NONE")]
    out += ["", f"Total rows: {len(ROWS)}.", "", "## Detail: dependencies, external inputs, verifying scripts, notes\n"]
    for r in ROWS:
        rid, g, itm, res, st, dep, ext, src, scr, gr, inp, note = r
        out += [f"### {rid}. {res}", "",
                f"- status: {st}; verdict: **{gr}**; in paper: {inp}",
                f"- depends on: {dep}", f"- external inputs: {ext}", f"- source: `{src}`",
                f"- verifying script / evidence: `review/audit-2/{scr}`", f"- note: {note}", ""]
    out += ["## Verbatim statements, by item\n"]
    for iid, (g, title, segs) in items.items():
        out += [f"### {iid} ({g}): {title}", ""]
        body = []
        for s in segs:
            if s[0] == "L":
                body.append(bs.excerpt(s[1], s[2], s[3], s[4]))
            elif s[0] == "T":
                body.append(s[1])
            else:
                body.append(f"(generated data: see `statements/{g}.md`, item {iid})")
        out += ["````", "\n\n".join(body), "````", ""]
    (ROOT / "review/audit-2/REGISTER-ADDENDUM.md").write_text("\n".join(out), encoding="utf-8")
    print(f"{len(ROWS)} rows; grades {dict(cnt_grade)}; status {dict(cnt_status)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
