# G5-bis theorem register addendum

One row per audited result. Statement text is verbatim from the source file (same anchored line ranges as `STATEMENTS.md`, produced by `build_statements.py`; the per-item text is reproduced below the table). Status vocabulary as in `review/audit/THEOREM-REGISTER.md`; CLAIM (FALSE AS PRINTED) marks a sentence that is refuted or contradicts another result of the paper, while the underlying mathematics may be fine. Audit verdict is the worst grade after the comparison phase (FATAL / SERIOUS / MINOR / NONE). 'In paper' says whether the result belongs in the paper: YES, YES REVISED (with the change in the note), CITE AS PRIOR WORK, or NO.

Audit evidence: `review/audit-2/<group>/REVIEW.md` (blind), `COMPARISON.md`, `check_*.py` with outputs.

## Summary

| # | group | items | result | status | audit verdict | in paper? | source |
|---|---|---|---|---|---|---|---|
| A1 | pte-structure | PS.0 | Definition 1.1, Lemma 1.2 (dictionary), items 1-5 | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/pte/proof.md 49-85` |
| A2 | pte-structure | PS.1 | Theorem 2.1 (Descartes bound |iota|<=T-2L; |U*|+|V*|>=2L+2|g-g'|; equality shape) | PROVED | NONE | YES | `theory/pte/proof.md 141-147` |
| A3 | pte-structure | PS.2 | Proposition 2.2 (tau_L >= N(2L-2)) | PROVED | NONE | YES | `theory/pte/proof.md 174-175` |
| A4 | pte-structure | PS.3 | Proposition 2.3 (symmetric constructions are balanced), (a)(b)(c) | PROVED | NONE | YES | `theory/pte/proof.md 184-194` |
| A5 | pte-structure | PS.4 | Theorem 3.1 (pencil: ideal balanced configurations) | PROVED | MINOR | YES, REVISED | `theory/pte/proof.md 223-233` |
| A6 | pte-structure | PS.5 | Proposition 3.2 (shift) | PROVED | MINOR | YES, REVISED | `theory/pte/proof.md 267-274` |
| A7 | pte-structure | PS.6 | statements.tex versions of Theorem (Descartes), Proposition (balanced), and the section opening | CLAIM (FALSE AS PRINTED) | SERIOUS | YES, REVISED | `theory/pte/statements.tex 13-53` |
| B1 | pte-growth | PG.0 | Definitions 1.3, 1.4, Lemma 1.5 (N_odd(L)<=N(2L-3); <=(L-1)^2+1; =L for 3<=L<=6) | PROVED GIVEN CITED INPUT | MINOR | YES | `theory/pte/proof.md 99-124` |
| B2 | pte-growth | PG.1 | Proposition 3.3 (doubling), including the n=2 and n=3 cases | PROVED | MINOR | YES, REVISED | `theory/pte/proof.md 283-293` |
| B3 | pte-growth | PG.2 | Theorem 3.4 (tau_L<=6N_odd(L); T_L<=4N(2L-3); T^cone_L<=6N(2L-3)) | PROVED | MINOR | YES, REVISED | `theory/pte/proof.md 311-314` |
| B4 | pte-growth | PG.3 | Theorem 4.1 (square-root lower bound on f(A)) | PROVED | NONE | YES | `theory/pte/proof.md 329-332` |
| B5 | pte-growth | PG.4 | Theorem 4.2 (a)(b)(c): f(A)>=c A^alpha iff N(k)<=C k^{1/alpha}; f=Theta(A) iff N(k)=O(k) | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/pte/proof.md 342-351` |
| B6 | pte-growth | PG.5 | Theorem 4.3 (genus alone, cone count alone) | PROVED | MINOR | YES, REVISED | `theory/pte/proof.md 380-390` |
| B7 | pte-growth | PG.6 | statements.tex Theorem (Growth), (a)(b)(c) and the closing sentence | PROVED | MINOR | YES, REVISED | `theory/pte/statements.tex 55-70` |
| C1 | pte-witnesses | PW.4 | The 18 explicit pairs (genus pairs L=2..7, balanced pairs, genus-0 pairs with different cone counts), each sharing exactly L coefficients; includes the 7-vs-8 cone pair, the L=3 same-genus pair of area 2 pi 22/15, and the L=4..7 pairs | COMPUTATION | NONE | YES | `theory/pte/data/witnesses.json` |
| C2 | pte-witnesses | PW.0 | Headline table (proof.md section 0 items 5, 6) | COMPUTATION | MINOR | YES, REVISED | `theory/pte/proof.md 32-47` |
| C3 | pte-witnesses | PW.1 | Example (Small pairs) | CLAIM (FALSE AS PRINTED) | SERIOUS | YES, REVISED | `theory/pte/statements.tex 101-120` |
| C4 | pte-witnesses | PW.1 | Remark (The first open case): shape (3,5) and the T_3 search claim | COMPUTATION | NONE | YES, REVISED | `theory/pte/statements.tex 122-127` |
| C5 | pte-witnesses | PW.2 | Improved lower bounds on f in the covered range | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/pte/proof.md 457-470` |
| C6 | pte-witnesses | PW.3, PW.5 | The 61 integer sharpness witnesses for Theorem A at n=4 (and the count of 25 at entries <= 130) | COMPUTATION | MINOR | YES, REVISED | `theory/pte/proof.md 253-263, data/pencil_m4_N220.json` |
| C7 | pte-witnesses | PW.3 | 'So Theorem C(3) at n=4 is a pencil phenomenon' | CLAIM (FALSE AS PRINTED) | SERIOUS | YES, REVISED | `theory/pte/proof.md 262-263` |
| C8 | pte-witnesses | PW.3 | n=5: no pencil witness with all entries <= 200 ('1,592 sets') | COMPUTATION | MINOR | YES, REVISED | `theory/pte/proof.md 264-265` |
| C9 | pte-witnesses | (proof.md 7) | Converse of Theorem 3.1 at size 8 ('every balanced size-8 3-configuration is a pencil point'): recorded as unproved, observed for entries <= 80 | OPEN | MINOR | NO | `theory/pte/proof.md 531-545` |
| D1 | trace-formula | TF.1 | Elliptic moments lemma (i)(ii) | PROVED | NONE | YES | `theory/revision/lemma25.tex 16-39` |
| D2 | trace-formula | TF.2 | Closed form Phi_m(u)=(cot u - m cot mu)/(4m sin u), sigma_i>0, Bernoulli expression (phik) | PROVED | NONE | YES | `theory/revision/lemma25.tex 50-67` |
| D3 | trace-formula | TF.3 | Lemma (the hyperbolic term is small) | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/revision/lemma25.tex 87-93` |
| D4 | trace-formula | TF.4 | Proposition (heat expansion at curvature -1): alpha_k, b_l(m)=(-1)^l p_l(m)/m, c_j | PROVED GIVEN CITED INPUT | NONE | YES | `theory/revision/lemma25.tex 101-119` |
| D5 | trace-formula | TF.5 | Lemma 2.5 for every order: p_l even, degree 2l+2, p_l(1)=0, leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)), p_l(m)>0 for m>1 | PROVED | NONE | YES | `theory/revision/lemma25.tex 145-152` |
| D6 | trace-formula | TF.5 | Printed first values alpha_0..alpha_4 and p_0,p_1,p_2, with the Schueth/DGGW attribution | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/revision/lemma25.tex 166-173` |
| D7 | trace-formula | TF.6 | Remark rem:ucaragree: agreement with Ucar for every l | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/revision/lemma25.tex 175-188` |
| D8 | trace-formula | TF.7 | Remark 4.12: independence of the trace-formula proof from the coefficient computations | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/revision/remark412.tex 17-61` |
| D9 | trace-formula | TF.8 | Theorem 1.2(iii): the constant C(A,l,D) | PROVED GIVEN CITED INPUT | NONE | YES, REVISED | `theory/revision/thm12iii.tex 10-23, 31-36` |
| D10 | trace-formula | TF.8 | Theorem 1.2(iii) 'attained' statement (three cases) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/revision/thm12iii.tex 16-23` |
| E1 | descent | DE.0 | phi, psi are mutually inverse isomorphisms over Q between C_{27/2} and E: y^2=x(x+9)(x+384) | PROVED | MINOR | YES, REVISED | `theory/revision/descent.tex 23-37` |
| E2 | descent | DE.1 | rank E(Q)=0 by 2-isogeny descent (Selmer groups {+-1,+-6} and {1}) | PROVED GIVEN CITED INPUT | NONE | YES | `theory/revision/descent.tex 39-72` |
| E3 | descent | DE.2 | E(Q)_tors = Z/2 x Z/6, the twelve points and their orders | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/revision/descent.tex 74-82` |
| E4 | descent | DE.3 | The twelve rational points of C_{27/2}; positive ones are the permutations of (1,4,4) and (1,1,4) | PROVED | NONE | YES | `theory/revision/descent.tex 84-87` |
| E5 | descent | DE.4 | Triads with S_1=18k and R=3/(4k) are permutations of (2k,8k,8k) or (3k,3k,12k) | PROVED | MINOR | YES, REVISED | `theory/revision/descent.tex 89-91` |
| E6 | descent | DE.5 | Theorem 5.16 (isolation of the base pair) | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `review/audit/statements/diophantine.md DI.7` |
| E7 | descent | DE.6 | Coordinates of 3P on C_{155/12}: 3P=(162833463:723926268:287876366) | COMPUTATION | NONE | YES | `theory/revision/point3P.tex 6-7` |
| F1 | stability | SB.2 | Proposition 6.10, steps 1-3 (Delta, tau^lin, tau^rem, rho_j, rho^rem_j, Delta_M, A) | PROVED | NONE | YES, REVISED | `theory/revision/prop610.tex 14-48` |
| F2 | stability | SB.2 | The matrix J=d(Me-b)/dI and G=-M^{-1} J F^{-1} | PROVED | NONE | YES | `theory/revision/prop610.tex 42-48` |
| F3 | stability | SB.1, SB.2 | Notation: rho used for data radii, residual bound and spectral radius; 'steps 4,5 unchanged' | PROVED | MINOR | YES, REVISED | `theory/revision/prop610.tex 42-43` |
| F4 | stability | SB.3 | Claim after Table 4 (series truncation and 'at most four nonzero (odd) coefficients') | PROVED | MINOR | YES, REVISED | `theory/revision/prop610.tex 63-65` |
| F5 | stability | SB.4 | Every printed delta_cert (11 rows) | COMPUTATION | NONE | YES | `review/audit/statements/stability.md ST.14` |
| F6 | stability | SB.4 | Every printed delta_thm (11 rows) | COMPUTATION | NONE | YES | `ST.14` |
| F7 | stability | SB.4 | Every printed eps_cert (uniform relative) | COMPUTATION | NONE | YES | `ST.14` |
| F8 | stability | SB.4 | The relative-precision column delta_cert/|H_nu| | COMPUTATION | MINOR | YES, REVISED | `ST.14` |
| F9 | stability | SB.4 | The delta_up column and ratio | COMPUTATION | MINOR | YES, REVISED | `ST.14` |
| G1 | threshold-sharpness | TH.1 | Theorem 5.13 (threshold): p+q+r<=17 determined by the first two invariants; 17 sharp | PROVED | NONE | YES, REVISED | `theory/revision/thm513.tex 11-15` |
| G2 | threshold-sharpness | TH.1 | Proposition (collision-free sums): exactly 38 sums in [18,4800] | COMPUTATION | NONE | YES | `theory/revision/thm513.tex 24-33` |
| G3 | threshold-sharpness | TH.1 | Method claims (scaling lemma, 3962/783, first pairs at 18, 20, 26) | COMPUTATION | NONE | YES | `theory/revision/thm513.tex 35-47` |
| G4 | threshold-sharpness | TH.2 | Sharpness wording: 1/k for arbitrary data; 1/2 at a double order and when all orders are equal | PROVED GIVEN CITED INPUT | MINOR | YES, REVISED | `theory/revision/sharpness.tex 21-44` |
| G5 | threshold-sharpness | TH.3 | Remark 6.8 addition: family (a+s,a-s,a,...,a) attains 1/2; k>=3 witnesses are not heat invariants of any real multiset | PROVED | NONE | YES | `theory/revision/sharpness.tex 47-59` |
| H1 | literature | LIT.0 B1-B4 | Borwein-Ingalls: N(k) definition (p. 6); Prop 2: N(k)>=k+1; Prop 3: N(k)<=k(k+1)/2+1; Prop 1 content | CITED CLAIM | MINOR | YES, REVISED | `theory/pte/LITERATURE.md; proof.md` |
| H2 | literature | LIT.0 B5, M1 | Wright and Melzak bounds N(k)<=(k^2-3)/2 (odd), (k^2-4)/2 (even) | CLAIM (FALSE AS PRINTED) | SERIOUS | YES, REVISED | `theory/pte/proof.md 19-22, 371-373; statements.tex 93` |
| H3 | literature | LIT.0 B7, O4 | N(k)=o(k^2) is open ('no progress for many years'); no sub-quadratic bound exists | CITED CLAIM | MINOR | YES, REVISED | `theory/pte/proof.md 21-24, 374-376` |
| H4 | literature | LIT.0 B8-B12 | BI p. 8 odd symmetric definition; p. 9/25 explicit solutions; Prouhet p. 4; Smyth Prop 4; Lemma 2 | CITED CLAIM | MINOR | NO | `LITERATURE.md` |
| H5 | literature | LIT.0 W1-W2, C1-C3, D1-D4 | Wooley Thm 1.3 (2012), Thm 13.1 (2019); Croot-Mao-Yip p. 1; CMSV p. 2 (ideal solutions known for k<=9 and k=11) | CITED CLAIM | NONE | YES | `statements.tex 97-98` |
| H6 | literature | LIT.0 P1-P2 | BLP 2003: parametric ideal solutions for n=1..8, 10; Gloden family; size-10 solutions | CITED CLAIM | MINOR | NO | `LITERATURE.md` |
| H7 | literature | LIT.0 S1 | Chen survey A.1.6, A.1.17, A.1.26, A.1.33: [1,5,5]=[2,3,6]; [1,13,17,23]=[3,9,21,21]; [3,19,37,51,53]=[9,11,43,45,55]; [7,91,...]=[29,59,...] | CITED CLAIM | NONE | YES | `proof.md Lemma 1.5(3)` |
| H8 | literature | LIT.0 S2 | eslpower.org Theorem 3 (lifting) underlies Proposition 2.2 | CITED CLAIM | NONE | YES | `proof.md 180-182` |
| H9 | literature | LIT.0 S3-S4 | Chen negative exponents: 33 types (s. 1.2.1, Ex. 1.7, p. 16 and p. 275); type (-1,1,3): [3,10,15,30]=[4,5,21,28] (A.685); type (-1,1,3,...,2L-3), L>=4 'does not appear' | CITED CLAIM | MINOR | YES, REVISED | `LITERATURE.md 128, 135-136` |
| H10 | literature | LIT.0 M2, O1-O3 | Melzak Table 1 (n<=29); Caley p. 2 (k log k concerns v(k)); Choudhry (k<=7); Prouhet | CITED CLAIM | NONE | NO | `LITERATURE.md` |
| H11 | literature | bibliography | references-pte.bib metadata | CITED CLAIM | MINOR | YES, REVISED | `theory/pte/references-pte.bib` |

## Counts

| status | count |
|---|---|
| CITED CLAIM | 10 |
| CLAIM (FALSE AS PRINTED) | 4 |
| COMPUTATION | 13 |
| OPEN | 1 |
| PROVED | 22 |
| PROVED GIVEN CITED INPUT | 15 |

| verdict | rows |
|---|---|
| FATAL | 0 |
| SERIOUS | 4 |
| MINOR | 33 |
| NONE | 28 |

Total rows: 65.

## Detail: dependencies, external inputs, verifying scripts, notes

### A1. Definition 1.1, Lemma 1.2 (dictionary), items 1-5

- status: PROVED GIVEN CITED INPUT; verdict: **MINOR**; in paper: YES, REVISED
- depends on: [Sig] Lemma 2, Lemma 4, Theorem S
- external inputs: [Sig] (H1)-(H3)
- source: `theory/pte/proof.md 49-85`
- verifying script / evidence: `review/audit-2/pte-structure/check_dictionary.py`
- note: 'U minus {1}' must mean removing every 1; the genus choice and its existence; for L>=2 the smaller genus is 0, so genus 1 is only needed for L=1; 'Area<2 pi T' is true but loose (Area/2pi<T-L-2).

### A2. Theorem 2.1 (Descartes bound |iota|<=T-2L; |U*|+|V*|>=2L+2|g-g'|; equality shape)

- status: PROVED; verdict: **NONE**; in paper: YES
- depends on: Lemma 1.2
- external inputs: none
- source: `theory/pte/proof.md 141-147`
- verifying script / evidence: `review/audit-2/pte-structure/check_descartes.py, check_attain.py`
- note: Equality in the displayed inequality does not force shape {L,L+2}: only size 2L+2 does.

### A3. Proposition 2.2 (tau_L >= N(2L-2))

- status: PROVED; verdict: **NONE**; in paper: YES
- depends on: Lemma 1.2
- external inputs: none
- source: `theory/pte/proof.md 174-175`
- verifying script / evidence: `review/audit-2/pte-structure/check_ps6.py`
- note: tau_L is defined in Definition 1.3.

### A4. Proposition 2.3 (symmetric constructions are balanced), (a)(b)(c)

- status: PROVED; verdict: **NONE**; in paper: YES
- depends on: Theorem 2.1, Theorem 3.1
- external inputs: Borwein-Ingalls p. 8 (definition only)
- source: `theory/pte/proof.md 184-194`
- verifying script / evidence: `review/audit-2/pte-structure/check_balanced.py`
- note: 'no pair' in (a) is redundant.

### A5. Theorem 3.1 (pencil: ideal balanced configurations)

- status: PROVED; verdict: **MINOR**; in paper: YES, REVISED
- depends on: Theorem 2.1, [Sig] Lemma 5 (Newton parity)
- external inputs: none
- source: `theory/pte/proof.md 223-233`
- verifying script / evidence: `review/audit-2/pte-structure/check_pencil.py, check_pencil_fibre.py`
- note: The 'Equivalently' clause needs e_k(A)=0 for odd k<r together with the product identity and kappa != 0.

### A6. Proposition 3.2 (shift)

- status: PROVED; verdict: **MINOR**; in paper: YES, REVISED
- depends on: none
- external inputs: none
- source: `theory/pte/proof.md 267-274`
- verifying script / evidence: `review/audit-2/pte-structure/check_shift.py`
- note: Add n>=1 (n=0 gives rho=0).

### A7. statements.tex versions of Theorem (Descartes), Proposition (balanced), and the section opening

- status: CLAIM (FALSE AS PRINTED); verdict: **SERIOUS**; in paper: YES, REVISED
- depends on: Lemma 1.2
- external inputs: none
- source: `theory/pte/statements.tex 13-53`
- verifying script / evidence: `review/audit-2/pte-structure/check_ps6.py`
- note: The sentence 'share their first L heat coefficients exactly when Z is an L-configuration' omits the genus condition iota(Z)=2(g'-g); counterexample (2;15) vs (0;3,3,5,5). Also add 0 not in A; fix the equality-shape wording.

### B1. Definitions 1.3, 1.4, Lemma 1.5 (N_odd(L)<=N(2L-3); <=(L-1)^2+1; =L for 3<=L<=6)

- status: PROVED GIVEN CITED INPUT; verdict: **MINOR**; in paper: YES
- depends on: Lemma 1.2
- external inputs: Chen survey A.1.6/17/26/33 (numbers re-verified), Borwein-Ingalls Props 2-3 (re-proved)
- source: `theory/pte/proof.md 99-124`
- verifying script / evidence: `review/audit-2/pte-growth/check_lemma15.py`
- note: N_odd(L)=L also holds at L=2; T^cone_L must name the cancelled primitive pair of Lemma 1.2(2).

### B2. Proposition 3.3 (doubling), including the n=2 and n=3 cases

- status: PROVED; verdict: **MINOR**; in paper: YES, REVISED
- depends on: Lemma 1.2
- external inputs: none
- source: `theory/pte/proof.md 283-293`
- verifying script / evidence: `review/audit-2/pte-growth/check_doubling.py`
- note: With 1 in X cap Y or multiplicities, '1 in X minus Y' is false (X={1,1,5}, Y={1,3,3}): state cone counts 3n-mu_X, 3n-mu_Y; state that the pair shares its first L coefficients; cite |V|=3n for the area bound, not Lemma 1.2(5).

### B3. Theorem 3.4 (tau_L<=6N_odd(L); T_L<=4N(2L-3); T^cone_L<=6N(2L-3))

- status: PROVED; verdict: **MINOR**; in paper: YES, REVISED
- depends on: Props 3.2, 3.3, Lemma 1.5
- external inputs: Borwein-Ingalls Prop 3
- source: `theory/pte/proof.md 311-314`
- verifying script / evidence: `review/audit-2/pte-growth/check_upper.py`
- note: T^cone_L needs the cancelled genus-0 realisation hyperbolic (proved for L>=3, checked at L=2) and 1 surviving cancellation; the '[Sig] N(a)' citation for 2^{2L-1} should cite the construction.

### B4. Theorem 4.1 (square-root lower bound on f(A))

- status: PROVED; verdict: **NONE**; in paper: YES
- depends on: Prop 3.3, Lemma 1.5
- external inputs: none
- source: `theory/pte/proof.md 329-332`
- verifying script / evidence: `review/audit-2/pte-growth/check_growth.py`
- note: Floor expression checked exactly at every breakpoint for A>=8 pi.

### B5. Theorem 4.2 (a)(b)(c): f(A)>=c A^alpha iff N(k)<=C k^{1/alpha}; f=Theta(A) iff N(k)=O(k)

- status: PROVED GIVEN CITED INPUT; verdict: **MINOR**; in paper: YES, REVISED
- depends on: [Sig] Cor S2/T1 (|U|+|V|<=2floor(A/pi)+8), Theorem 4.1, Prop 2.2
- external inputs: none
- source: `theory/pte/proof.md 342-351`
- verifying script / evidence: `review/audit-2/pte-growth/check_growth.py`
- note: Add L>=2 in (a), beta>0 in (b); the constant 2 floor(A/pi)+8 uses that |U|+|V| is even.

### B6. Theorem 4.3 (genus alone, cone count alone)

- status: PROVED; verdict: **MINOR**; in paper: YES, REVISED
- depends on: Theorem 3.4, Lemma 1.2(5)
- external inputs: none
- source: `theory/pte/proof.md 380-390`
- verifying script / evidence: `review/audit-2/pte-growth/check_growth.py`
- note: Define f_g and f_n exactly; explicit constants f_g(A)>=sqrt(A/16 pi) for A>=16 pi and f_n(A)>=sqrt(A/12 pi) for A>=8 pi.

### B7. statements.tex Theorem (Growth), (a)(b)(c) and the closing sentence

- status: PROVED; verdict: **MINOR**; in paper: YES, REVISED
- depends on: B3-B6
- external inputs: none
- source: `theory/pte/statements.tex 55-70`
- verifying script / evidence: `review/audit-2/pte-growth/check_growth.py`
- note: (b) needs L>=2; the sketch of (c) omits the second scaled balanced shift; the last sentence uses undefined quantities.

### C1. The 18 explicit pairs (genus pairs L=2..7, balanced pairs, genus-0 pairs with different cone counts), each sharing exactly L coefficients; includes the 7-vs-8 cone pair, the L=3 same-genus pair of area 2 pi 22/15, and the L=4..7 pairs

- status: COMPUTATION; verdict: **NONE**; in paper: YES
- depends on: heat coefficients (A. trace-formula group)
- external inputs: none (coefficients recomputed from first principles; Ucar (4.25) cross-check l<=12)
- source: `theory/pte/data/witnesses.json`
- verifying script / evidence: `review/audit-2/pte-witnesses/check_*.py`
- note: All 18: hyperbolic, equal exact area, distinct signatures, exactly L shared.

### C2. Headline table (proof.md section 0 items 5, 6)

- status: COMPUTATION; verdict: **MINOR**; in paper: YES, REVISED
- depends on: C1
- external inputs: none
- source: `theory/pte/proof.md 32-47`
- verifying script / evidence: `review/audit-2/pte-witnesses/check_*.py`
- note: 'Real solutions exist in abundance' unsupported: they form a nonempty open set; for integer Y<=24 only 635 of 98,280 give one.

### C3. Example (Small pairs)

- status: CLAIM (FALSE AS PRINTED); verdict: **SERIOUS**; in paper: YES, REVISED
- depends on: C1, Theorem C(3)
- external inputs: none
- source: `theory/pte/statements.tex 101-120`
- verifying script / evidence: `review/audit-2/pte-witnesses/check_*.py`
- note: 'Previously the smallest area known to share three coefficients was 2 pi 14/5' contradicts Theorem C(3): the 22/15 pair is already its n=4 witness.

### C4. Remark (The first open case): shape (3,5) and the T_3 search claim

- status: COMPUTATION; verdict: **NONE**; in paper: YES, REVISED
- depends on: Theorem 2.1
- external inputs: none
- source: `theory/pte/statements.tex 122-127`
- verifying script / evidence: `review/audit-2/pte-witnesses/t3run, check_cmp_t3filter.py`
- note: Independent exact modular search over every Y<=220 (4,493,032,544 multisets): no solution; planted controls recovered. 'abundance' and 'made primitive' wording: MINOR.

### C5. Improved lower bounds on f in the covered range

- status: PROVED GIVEN CITED INPUT; verdict: **MINOR**; in paper: YES, REVISED
- depends on: C1, Theorem 4.1 logic
- external inputs: none
- source: `theory/pte/proof.md 457-470`
- verifying script / evidence: `review/audit-2/pte-witnesses/check_*.py`
- note: 'Area/2pi ~ T/2-2' fails for L=2,3; 'grows at least linearly for A/2pi<=18' has no content on a bounded range; replace by A_L/2pi<2L-3 for 2<=L<=5.

### C6. The 61 integer sharpness witnesses for Theorem A at n=4 (and the count of 25 at entries <= 130)

- status: COMPUTATION; verdict: **MINOR**; in paper: YES, REVISED
- depends on: Theorem 3.1
- external inputs: none
- source: `theory/pte/proof.md 253-263, data/pencil_m4_N220.json`
- verifying script / evidence: `review/audit-2/pte-witnesses/check_*.py`
- note: All 61 verified and the set reproduced exactly; but the range is |a|,|b|,|c|<=N with the fourth entry unrestricted (all-entries counts are 15 and 35).

### C7. 'So Theorem C(3) at n=4 is a pencil phenomenon'

- status: CLAIM (FALSE AS PRINTED); verdict: **SERIOUS**; in paper: YES, REVISED
- depends on: C6
- external inputs: none
- source: `theory/pte/proof.md 262-263`
- verifying script / evidence: `review/audit-2/pte-witnesses/direct4_N440.txt`
- note: Exhaustive search of 4-cone pairs with orders <= 440: 107 primitive witnesses, 6 without pencil splitting, smallest (0;16,16,74,74) ~ (0;11,37,44,88) (R=45/296, P1=180, P3=818640).

### C8. n=5: no pencil witness with all entries <= 200 ('1,592 sets')

- status: COMPUTATION; verdict: **MINOR**; in paper: YES, REVISED
- depends on: Theorem 3.1
- external inputs: none
- source: `theory/pte/proof.md 264-265`
- verifying script / evidence: `review/audit-2/pte-witnesses/n5_N200_mode1.txt`
- note: 1,592 counts sets with >=3 entries in [-200,200] (A and -A separately); 602 have all entries in [-200,200]. 'No pencil pair' holds under every reading.

### C9. Converse of Theorem 3.1 at size 8 ('every balanced size-8 3-configuration is a pencil point'): recorded as unproved, observed for entries <= 80

- status: OPEN; verdict: **MINOR**; in paper: NO
- depends on: Theorem 3.1
- external inputs: none
- source: `theory/pte/proof.md 531-545`
- verifying script / evidence: `review/audit-2/pte-witnesses/direct4_N440.txt`
- note: Now refuted: balanced size-8 configurations without pencil splitting exist from entries 88 (the 6 witnesses of C7). No 4-cone pair with order 1 up to 440, extending 'none with orders <= 80'.

### D1. Elliptic moments lemma (i)(ii)

- status: PROVED; verdict: **NONE**; in paper: YES
- depends on: Euler beta integral
- external inputs: Dryden-Strohmaier eq (1) (weights)
- source: `theory/revision/lemma25.tex 16-39`
- verifying script / evidence: `review/audit-2/trace-formula/check_closedform.py`
- note: F_a, 0<a<2 pi, weights 1/(2m sin theta_j) match DS eq (1) p. 3.

### D2. Closed form Phi_m(u)=(cot u - m cot mu)/(4m sin u), sigma_i>0, Bernoulli expression (phik)

- status: PROVED; verdict: **NONE**; in paper: YES
- depends on: Liouville, Bernoulli numbers
- external inputs: none
- source: `theory/revision/lemma25.tex 50-67`
- verifying script / evidence: `review/audit-2/trace-formula/check_closedform.py`
- note: Three independent computations agree, m<=12, k<=40; sigma_i=(4^i-2)|B_2i|/(2i)!.

### D3. Lemma (the hyperbolic term is small)

- status: PROVED GIVEN CITED INPUT; verdict: **MINOR**; in paper: YES, REVISED
- depends on: counting lemma (audited), trace formula
- external inputs: DS eq (1)
- source: `theory/revision/lemma25.tex 87-93`
- verifying script / evidence: `review/audit-2/trace-formula/check_hypbound.py`
- note: Define the systole as least length over all hyperbolic classes incl. through cone points; 'Orb in Sig' is a type error; the fragment has no written proof (points to Theorem 4.9(b), which quotes the lemma): insert the proof.

### D4. Proposition (heat expansion at curvature -1): alpha_k, b_l(m)=(-1)^l p_l(m)/m, c_j

- status: PROVED GIVEN CITED INPUT; verdict: **NONE**; in paper: YES
- depends on: D1-D3
- external inputs: DS eq (1), DGGW Thm 4.8 (Z(s)=O(1/s))
- source: `theory/revision/lemma25.tex 101-119`
- verifying script / evidence: `review/audit-2/trace-formula/check_conepoly.py`
- note: Signatures (H3) uses alpha_l for what this calls alpha_{l+1}/(4 pi): do not use one symbol for both.

### D5. Lemma 2.5 for every order: p_l even, degree 2l+2, p_l(1)=0, leading coefficient |B_{2l+2}|/(2(l+1)!(2l+1)), p_l(m)>0 for m>1

- status: PROVED; verdict: **NONE**; in paper: YES
- depends on: D2
- external inputs: none
- source: `theory/revision/lemma25.tex 145-152`
- verifying script / evidence: `review/audit-2/trace-formula/check_conepoly.py`
- note: p_l=sum_n w_{l,n}(m^{2n}-1) with all weights products of positive rationals; exact for l<=40, m=1..30.

### D6. Printed first values alpha_0..alpha_4 and p_0,p_1,p_2, with the Schueth/DGGW attribution

- status: PROVED GIVEN CITED INPUT; verdict: **MINOR**; in paper: YES, REVISED
- depends on: D4
- external inputs: Schueth Rem 4.2, Thm 4.1; DGGW 5.6; Ucar (4.35)
- source: `theory/revision/lemma25.tex 166-173`
- verifying script / evidence: `review/audit-2/trace-formula/check_conepoly.py`
- note: Values correct; the attribution sentence reads as crediting DGGW with p_2: Schueth credits DGGW 5.6 with a_0, a_1 only. No existing script tests p_2 against Schueth.

### D7. Remark rem:ucaragree: agreement with Ucar for every l

- status: PROVED GIVEN CITED INPUT; verdict: **MINOR**; in paper: YES, REVISED
- depends on: D4, D5
- external inputs: Ucar (4.25), (4.33)-(4.35), Thm 4.20(ii)
- source: `theory/revision/lemma25.tex 175-188`
- verifying script / evidence: `review/audit-2/trace-formula/check_ucar.py`
- note: Holds for every l with the (-1)^l sign, no index shift; cite Thm 4.20(ii) (p. 138) beside (4.33)-(4.34); use kappa.

### D8. Remark 4.12: independence of the trace-formula proof from the coefficient computations

- status: PROVED GIVEN CITED INPUT; verdict: **MINOR**; in paper: YES, REVISED
- depends on: D4
- external inputs: DGGW Thm 4.8 (Z(s)=O(1/s))
- source: `theory/revision/remark412.tex 17-61`
- verifying script / evidence: `review/audit-2/trace-formula/check_hypbound.py`
- note: Say 'independent of the coefficient computations'; the 'or Weyl's law' clause is not independent; state the test-function class as h=g-hat, g smooth even compactly supported (DS's 'entire of uniform exponential type' admits h=1); sentence (1B) must not be combined with locality.tex.

### D9. Theorem 1.2(iii): the constant C(A,l,D)

- status: PROVED GIVEN CITED INPUT; verdict: **NONE**; in paper: YES, REVISED
- depends on: D3
- external inputs: none
- source: `theory/revision/thm12iii.tex 10-23, 31-36`
- verifying script / evidence: `review/audit-2/trace-formula/check_hypbound.py`
- note: C re-derives exactly; replacing each orbifold's systole/diameter by the smaller/larger is justified (bound decreasing in l and increasing in D on the range, interval-arithmetic checked on 390 cells): add that line.

### D10. Theorem 1.2(iii) 'attained' statement (three cases)

- status: PROVED GIVEN CITED INPUT; verdict: **NONE**; in paper: YES
- depends on: D3
- external inputs: DS eq (1)
- source: `theory/revision/thm12iii.tex 16-23`
- verifying script / evidence: `review/audit-2/trace-formula/check_hypbound.py`
- note: Weighted, all-class and primitive length spectra first differ at the same length.

### E1. phi, psi are mutually inverse isomorphisms over Q between C_{27/2} and E: y^2=x(x+9)(x+384)

- status: PROVED; verdict: **MINOR**; in paper: YES, REVISED
- depends on: none
- external inputs: none
- source: `theory/revision/descent.tex 23-37`
- verifying script / evidence: `review/audit-2/descent/check_a_isomorphism.py`
- note: phi undefined at the 3 points with Z=0: state the extension phi(O)=origin, phi(1:0:0)=(216,5400), phi(0:1:0)=(216,-5400); give the nonsingularity argument.

### E2. rank E(Q)=0 by 2-isogeny descent (Selmer groups {+-1,+-6} and {1})

- status: PROVED GIVEN CITED INPUT; verdict: **NONE**; in paper: YES
- depends on: E1
- external inputs: Cremona 3.6 (3.6.2)
- source: `theory/revision/descent.tex 39-72`
- verifying script / evidence: `review/audit-2/descent/check_b_descent.py`
- note: Local tests are at all p | 2dd' (the classes +-2,+-3 on E fail only at p=5); independent full 2-descent gives 2-Selmer of order 4.

### E3. E(Q)_tors = Z/2 x Z/6, the twelve points and their orders

- status: PROVED GIVEN CITED INPUT; verdict: **MINOR**; in paper: YES, REVISED
- depends on: E1
- external inputs: Cremona 3.3 p. 70
- source: `theory/revision/descent.tex 74-82`
- verifying script / evidence: `review/audit-2/descent/check_c_torsion.py`
- note: Remark 'tangent at (16,400) meets E again at (16,-400)' is false: (16,400) is a flex; write 'meets E only at (16,400), multiplicity 3, so 2(16,400)=(16,-400)=-(16,400)'.

### E4. The twelve rational points of C_{27/2}; positive ones are the permutations of (1,4,4) and (1,1,4)

- status: PROVED; verdict: **NONE**; in paper: YES
- depends on: E2, E3
- external inputs: none
- source: `theory/revision/descent.tex 84-87`
- verifying script / evidence: `review/audit-2/descent/check_d_points_triads.py`
- note: Also confirmed by a search to height 80 independent of the descent.

### E5. Triads with S_1=18k and R=3/(4k) are permutations of (2k,8k,8k) or (3k,3k,12k)

- status: PROVED; verdict: **MINOR**; in paper: YES, REVISED
- depends on: E4
- external inputs: none
- source: `theory/revision/descent.tex 89-91`
- verifying script / evidence: `review/audit-2/descent/check_d_points_triads.py`
- note: True for integer k>=1; k=3/2 gives only (3,12,12). State 'k>=1 an integer; hyperbolic since R<1 and all entries >= 2k >= 2'.

### E6. Theorem 5.16 (isolation of the base pair)

- status: PROVED GIVEN CITED INPUT; verdict: **MINOR**; in paper: YES, REVISED
- depends on: E2-E5
- external inputs: Cremona
- source: `review/audit/statements/diophantine.md DI.7`
- verifying script / evidence: `review/audit-2/descent/check_e_isolation.py`
- note: 'every integer k>=1'; base the proof on the descent and torsion, PARI as cross-check only; drop '(as far as tested)': every isosceles point (u:v:v) has order 6.

### E7. Coordinates of 3P on C_{155/12}: 3P=(162833463:723926268:287876366)

- status: COMPUTATION; verdict: **NONE**; in paper: YES
- depends on: none
- external inputs: none
- source: `theory/revision/point3P.tex 6-7`
- verifying script / evidence: `review/audit-2/descent/check_f_3P.py`
- note: Printed old point = (1:0:-1)-3P = Y<->Z transposition of 3P: same triad; O=(1:-1:0) is a flex of every C_lambda.

### F1. Proposition 6.10, steps 1-3 (Delta, tau^lin, tau^rem, rho_j, rho^rem_j, Delta_M, A)

- status: PROVED; verdict: **NONE**; in paper: YES, REVISED
- depends on: Prop S5
- external inputs: none
- source: `theory/revision/prop610.tex 14-48`
- verifying script / evidence: `review/audit-2/stability/check_cert.py, check_probes.py`
- note: 26,924 exact probes, 0 violations.

### F2. The matrix J=d(Me-b)/dI and G=-M^{-1} J F^{-1}

- status: PROVED; verdict: **NONE**; in paper: YES
- depends on: F1
- external inputs: none
- source: `theory/revision/prop610.tex 42-48`
- verifying script / evidence: `review/audit-2/stability/check_setup.py`
- note: Matches sympy differentiation for n=2..6.

### F3. Notation: rho used for data radii, residual bound and spectral radius; 'steps 4,5 unchanged'

- status: PROVED; verdict: **MINOR**; in paper: YES, REVISED
- depends on: F1
- external inputs: none
- source: `theory/revision/prop610.tex 42-43`
- verifying script / evidence: `review/audit-2/stability/check_cert.py`
- note: Rename the Prop S5 radii delta_nu; first-order term sum_c delta_c sum_l |p_c^{(l)}(a)/l!| r^l; state F=L.

### F4. Claim after Table 4 (series truncation and 'at most four nonzero (odd) coefficients')

- status: PROVED; verdict: **MINOR**; in paper: YES, REVISED
- depends on: F1
- external inputs: none
- source: `theory/revision/prop610.tex 63-65`
- verifying script / evidence: `review/audit-2/stability/check_setup.py`
- note: '(odd)' is false for sech^2 U; replacement: the odd series have at most four nonzero coefficients (z,z^3,z^5,z^7), the even series sech^2 U and sec^2 U at most four (1,z^2,z^4,z^6).

### F5. Every printed delta_cert (11 rows)

- status: COMPUTATION; verdict: **NONE**; in paper: YES
- depends on: F1, Prop S5
- external inputs: none
- source: `review/audit/statements/stability.md ST.14`
- verifying script / evidence: `review/audit-2/stability/check_cert.py`
- note: All pass by test (ii); each is the exact 4-s.f. maximum.

### F6. Every printed delta_thm (11 rows)

- status: COMPUTATION; verdict: **NONE**; in paper: YES
- depends on: Theorems S2, S3
- external inputs: none
- source: `ST.14`
- verifying script / evidence: `review/audit-2/stability/check_cert.py`
- note: Each equals the exact value rounded down to 3 s.f. and passes both tests.

### F7. Every printed eps_cert (uniform relative)

- status: COMPUTATION; verdict: **NONE**; in paper: YES
- depends on: F1
- external inputs: none
- source: `ST.14`
- verifying script / evidence: `review/audit-2/stability/check_cert.py`
- note: All pass, each the 2-s.f. maximum. Producer's threshold_output.md prints 4 s.f. rounded to nearest: five rows do not certify there (fmt_down needed). MINOR in that file only.

### F8. The relative-precision column delta_cert/|H_nu|

- status: COMPUTATION; verdict: **MINOR**; in paper: YES, REVISED
- depends on: F5
- external inputs: none
- source: `ST.14`
- verifying script / evidence: `review/audit-2/stability/check_cert.py`
- note: (2,3,7), nu=0: 3.9e-03 not 4.0e-03 (computed from the unrounded 3.65881e-03).

### F9. The delta_up column and ratio

- status: COMPUTATION; verdict: **MINOR**; in paper: YES, REVISED
- depends on: ST.13
- external inputs: none
- source: `ST.14`
- verifying script / evidence: `review/audit-2/stability/search_dup.py, check_dup.py`
- note: (2,2,2,2,3): 5.743e-05 and 7.26 must read 5.312e-05 and 6.72 (threshold_output.md already does; proof.md l.446 and STATUS.md l.53 stale); (3,10,15,30): 7.487e-03 (optional).

### G1. Theorem 5.13 (threshold): p+q+r<=17 determined by the first two invariants; 17 sharp

- status: PROVED; verdict: **NONE**; in paper: YES, REVISED
- depends on: separation theorem (audited)
- external inputs: none
- source: `theory/revision/thm513.tex 11-15`
- verifying script / evidence: `review/audit-2/threshold-sharpness/check_collisionfree.py`
- note: Add: the first two invariants determine S_1 (eq:s1inv), so a sum<=17 collides only within its own sum.

### G2. Proposition (collision-free sums): exactly 38 sums in [18,4800]

- status: COMPUTATION; verdict: **NONE**; in paper: YES
- depends on: none
- external inputs: none
- source: `theory/revision/thm513.tex 24-33`
- verifying script / evidence: `review/audit-2/threshold-sharpness/check_collisionfree.c, .py`
- note: Independent exact C search: the 38 sums, 25,575 triads at 557; each of the other 4745 sums has a collision; 3962 covered by scaling, 783 uncovered with a collision.

### G3. Method claims (scaling lemma, 3962/783, first pairs at 18, 20, 26)

- status: COMPUTATION; verdict: **NONE**; in paper: YES
- depends on: G2
- external inputs: none
- source: `theory/revision/thm513.tex 35-47`
- verifying script / evidence: `review/audit-2/threshold-sharpness/check_collisionfree.py`
- note: collision_witnesses.csv: 783 rows, same sums as the blind set.

### G4. Sharpness wording: 1/k for arbitrary data; 1/2 at a double order and when all orders are equal

- status: PROVED GIVEN CITED INPUT; verdict: **MINOR**; in paper: YES, REVISED
- depends on: Theorems S3, S4
- external inputs: none
- source: `theory/revision/sharpness.tex 21-44`
- verifying script / evidence: `review/audit-2/threshold-sharpness/check_sharpness.py`
- note: Say 'positive real orders'; 'all n>=2 orders equal'; Remark S3.3 should read d_i >= -a (|d_i|<=a is sufficient) and give max|d_i|<=((498+42a^2)delta/(2a))^{1/2}; n=1 is Lipschitz.

### G5. Remark 6.8 addition: family (a+s,a-s,a,...,a) attains 1/2; k>=3 witnesses are not heat invariants of any real multiset

- status: PROVED; verdict: **NONE**; in paper: YES
- depends on: G4
- external inputs: none
- source: `theory/revision/sharpness.tex 47-59`
- verifying script / evidence: `review/audit-2/threshold-sharpness/check_sharpness.py`
- note: check_sharpness.py tests only n=3,4 at a=8; the general claims rest on the written argument, re-proved blind.

### H1. Borwein-Ingalls: N(k) definition (p. 6); Prop 2: N(k)>=k+1; Prop 3: N(k)<=k(k+1)/2+1; Prop 1 content

- status: CITED CLAIM; verdict: **MINOR**; in paper: YES, REVISED
- depends on: none
- external inputs: Borwein-Ingalls 1994
- source: `theory/pte/LITERATURE.md; proof.md`
- verifying script / evidence: `review/audit-2/literature/check_lifting_and_bounds.py`
- note: Prop 1 is the three equivalent forms of the problem, not a bound; cite Hardy-Wright for pigeonhole (Melzak credits it); statements.tex cites BI s. 1 for N(k): it is s. 2, p. 6. Source read from a scan (gap: e-periodica captcha).

### H2. Wright and Melzak bounds N(k)<=(k^2-3)/2 (odd), (k^2-4)/2 (even)

- status: CLAIM (FALSE AS PRINTED); verdict: **SERIOUS**; in paper: YES, REVISED
- depends on: none
- external inputs: Melzak CMB 4 p. 233-234; BI p. 7
- source: `theory/pte/proof.md 19-22, 371-373; statements.tex 93`
- verifying script / evidence: `review/audit-2/literature/check_lifting_and_bounds.py`
- note: The formula (copied accurately from BI p. 7) is false for k=2,3 and is not in Melzak; Melzak reports Wright's K(n)<=(n^2+4)/2 (n = degree). Replacement: 'The pigeonhole bound N(k)<=k(k+1)/2+1 [Hardy-Wright; BI Prop. 3] was improved by Wright (1935) to N(k)<=(k^2+4)/2 (as reported by Melzak, CMB 4 (1961), p. 234). Melzak gave an exact non-constructive formula and numerical upper bounds for k<=29 [ibid., Table 1]. None is o(k^2), and N(k)=o(k^2) remains open [BI s. 6 Problem 3; Croot-Mao-Yip 2026].'

### H3. N(k)=o(k^2) is open ('no progress for many years'); no sub-quadratic bound exists

- status: CITED CLAIM; verdict: **MINOR**; in paper: YES, REVISED
- depends on: none
- external inputs: BI s. 6 Q3; Croot-Mao-Yip 2026; Wooley
- source: `theory/pte/proof.md 21-24, 374-376`
- verifying script / evidence: `review/audit-2/literature/search/`
- note: Adversarial search finds no refereed counterexample. Problem 4 (M(k)=O(k^2)) was solved by Wooley 2012: drop 'no progress on questions 3 and 4'. One unrefereed preprint (Sun-Zhao arXiv:2307.11330) claims Wright's conjecture: footnote optional.

### H4. BI p. 8 odd symmetric definition; p. 9/25 explicit solutions; Prouhet p. 4; Smyth Prop 4; Lemma 2

- status: CITED CLAIM; verdict: **MINOR**; in paper: NO
- depends on: none
- external inputs: Borwein-Ingalls
- source: `LITERATURE.md`
- verifying script / evidence: `review/audit-2/literature/check_solutions.py`
- note: All 14 printed solutions verified exactly; BI credits 'Letac and Gloden' jointly: cite BLP p. 2069 and CMSV p. 2 for Letac.

### H5. Wooley Thm 1.3 (2012), Thm 13.1 (2019); Croot-Mao-Yip p. 1; CMSV p. 2 (ideal solutions known for k<=9 and k=11)

- status: CITED CLAIM; verdict: **NONE**; in paper: YES
- depends on: none
- external inputs: arXiv texts
- source: `statements.tex 97-98`
- verifying script / evidence: `review/audit-2/literature/REVIEW.md`
- note: W(k,2) is the exact-degree quantity M(k), not N(k); size/degree conventions consistent.

### H6. BLP 2003: parametric ideal solutions for n=1..8, 10; Gloden family; size-10 solutions

- status: CITED CLAIM; verdict: **MINOR**; in paper: NO
- depends on: none
- external inputs: BLP 2003
- source: `LITERATURE.md`
- verifying script / evidence: `review/audit-2/literature/check_solutions.py`
- note: The two-parameter family is BLP's reduction of Gloden's four-parameter solution; BLP do not name Letac for the 9-sets.

### H7. Chen survey A.1.6, A.1.17, A.1.26, A.1.33: [1,5,5]=[2,3,6]; [1,13,17,23]=[3,9,21,21]; [3,19,37,51,53]=[9,11,43,45,55]; [7,91,...]=[29,59,...]

- status: CITED CLAIM; verdict: **NONE**; in paper: YES
- depends on: none
- external inputs: Chen survey arXiv:2506.11429
- source: `proof.md Lemma 1.5(3)`
- verifying script / evidence: `review/audit-2/literature/check_solutions.py`
- note: All 16 solutions and attributions confirmed (A.48, A.313, A.314-A.316 are equation numbers inside those sections).

### H8. eslpower.org Theorem 3 (lifting) underlies Proposition 2.2

- status: CITED CLAIM; verdict: **NONE**; in paper: YES
- depends on: none
- external inputs: eslpower.org TarryPrb.htm
- source: `proof.md 180-182`
- verifying script / evidence: `review/audit-2/literature/check_lifting_and_bounds.py`
- note: Identity verified; non-triviality (Z != -Z) holds for configurations because they have no pair {z,-z}.

### H9. Chen negative exponents: 33 types (s. 1.2.1, Ex. 1.7, p. 16 and p. 275); type (-1,1,3): [3,10,15,30]=[4,5,21,28] (A.685); type (-1,1,3,...,2L-3), L>=4 'does not appear'

- status: CITED CLAIM; verdict: **MINOR**; in paper: YES, REVISED
- depends on: none
- external inputs: Chen survey
- source: `LITERATURE.md 128, 135-136`
- verifying script / evidence: `review/audit-2/literature/check_solutions.py`
- note: 'Does not appear' is contradicted as worded ((-1,1,3,5) appears in Ex. 2.36, (3.33), (5.107)); say 'no numerical solution is listed for (-1,1,3,...,2L-3), L>=4'. Section number is 1.2.1, not 1.4.

### H10. Melzak Table 1 (n<=29); Caley p. 2 (k log k concerns v(k)); Choudhry (k<=7); Prouhet

- status: CITED CLAIM; verdict: **NONE**; in paper: NO
- depends on: none
- external inputs: sources
- source: `LITERATURE.md`
- verifying script / evidence: `review/audit-2/literature/REVIEW.md`
- note: Confirmed.

### H11. references-pte.bib metadata

- status: CITED CLAIM; verdict: **MINOR**; in paper: YES, REVISED
- depends on: none
- external inputs: Crossref, arXiv
- source: `theory/pte/references-pte.bib`
- verifying script / evidence: `review/audit-2/literature/COMPARISON.md`
- note: cmsv2024 lacks DOI 10.1090/mcom/3917; wooley2019 lacks 10.1112/plms.12204; melzak1961 is in the bib but uncited; add Hardy-Wright and Wooley 2012 if the suggested sentences are used.

## Verbatim statements, by item

### PS.0 (pte-structure): Setting, Definition 1.1, Lemma 1.2 (dictionary)

````
## 1. Setting

Throughout, (H1)–(H3) of [Sig] §1 are assumed, as there. Two closed orientable hyperbolic
2-orbifolds with signatures $\sigma=(g;m)\ne\sigma'=(g';m')$ share their first $L$ heat
coefficients if and only if the following holds ([Sig] Lemma 4, Theorem S). Pad $m$ and $m'$
by 1s to $U$ and $V$ with $R(U)=R(V)$, and cancel common elements to get $U^*,V^*$. Then the
multiset $Z=U^*\uplus(-V^*)$ satisfies the definition below, and $|V^*|-|U^*|=2(g-g')$.

**Definition 1.1.** An *$L$-configuration* is a nonempty finite multiset $Z$ of nonzero
rationals such that:

- $s_j(Z):=\sum_{z\in Z}z^j=0$ for odd $1\le j\le2L-3$;
- $s_{-1}(Z)=0$;
- $Z$ contains no pair $\{z,-z\}$;
- $|Z|$ is even (equivalently, $\iota(Z)$ below is even).

The last condition is automatic for configurations coming from orbifold pairs, since
$|U^*|+|V^*|\equiv|V^*|-|U^*|=2(g-g')$. Without it there are odd examples, e.g.
$\{-24,-18,-8,5,45\}$ has $s_1=s_{-1}=0$; they correspond to no orbifold pair.

Write $T=|Z|$ for its *size* and $\iota(Z)=\#\{z>0\}-\#\{z<0\}$ for its *imbalance*.

**Lemma 1.2 (dictionary).**

1. Configurations are invariant under $Z\mapsto\lambda Z$ for $\lambda\in\mathbb Q^\times$. This
   preserves $T$, and multiplies $\iota$ by $\operatorname{sgn}\lambda$.
2. Let $Z$ be an $L$-configuration scaled to primitive integers. Put $U=Z_{>0}$ and
   $V=-Z_{<0}$, and let $g-g'=-\iota/2$ with the smaller genus chosen least such that both are
   hyperbolic. Then $(g;U\setminus\{1\})$ and $(g';V\setminus\{1\})$ have equal area and
   distinct signatures, and they share at least $L$ heat coefficients. They share exactly $L$
   iff $s_{2L-1}(Z)\ne0$.
3. The pair is genus-changing iff $\iota\ne0$. If $\iota=0$, the pair has equal genus, and the
   cone counts differ iff $\pm1\in Z$ (a padding point).
4. $T$ is even and $T\ge2L+2$.
5. Area. If $\iota\ne0$, then $\operatorname{Area}<2\pi T$. If $\iota=0$ and the genus-0
   realisation is hyperbolic, then $\operatorname{Area}/2\pi=-2+\sum_{v\in V}(1-1/v)<T/2-2$.

````

### PS.1 (pte-structure): Theorem 2.1 (Descartes bound)

````
**Theorem 2.1 (Descartes bound).** Every $L$-configuration satisfies $|\iota(Z)|\le T-2L$. In
particular:

1. Two orbifolds of genera $g\ne g'$ sharing $L$ heat coefficients have
   $|U^*|+|V^*|\ge2L+2|g-g'|$.
2. A genus-changing configuration of size $2L+2$ has $\iota=\pm2$, i.e. shape
   $\{|U^*|,|V^*|\}=\{L,L+2\}$. An $L$-configuration of size $2L+2$ has $\iota\in\{0,\pm2\}$.
````

### PS.2 (pte-structure): Proposition 2.2 (PTE lower bound)

````
**Proposition 2.2 (PTE lower bound).** An $L$-configuration of size $T$ gives the PTE solution
$[Z]=_{2L-2}[-Z]$ of size $T$. Hence $\tau_L\ge N(2L-2)$.
````

### PS.3 (pte-structure): Proposition 2.3 (symmetric constructions are balanced)

````
**Proposition 2.3 (symmetric constructions are balanced).**

(a) Let $A$ be an *odd ideal symmetric* PTE solution in the sense of Borwein–Ingalls (p. 8):
$|A|=2L-1$, $s_j(A)=0$ for odd $j\le2L-3$, $0\notin A$, and no pair $\{a,-a\}$. Then
$s_{-1}(A)\ne0$ and $\iota(A)=\operatorname{sgn}s_{-1}(A)$.

(b) For two such sets $A,B$, let $\lambda=-s_{-1}(B)/s_{-1}(A)$, so that
$s_{-1}(A\uplus\lambda B)=s_{-1}(A)+s_{-1}(B)/\lambda=0$. Then $Z=A\uplus\lambda B$ is, after
cancellation, either empty or an $L$-configuration with $\iota(Z)=0$.

(c) The pencil configurations of Theorem 3.1 have $\iota=0$.
````

### PS.4 (pte-structure): Theorem 3.1 (pencil)

````
**Theorem 3.1 (pencil: ideal balanced configurations).** Let $m\ge4$, put $r=m-1$ and $k_0=m-2$
if $m$ is even, and $r=m$ and $k_0=m-3$ if $m$ is odd. Let $A\ne B$ be $m$-multisets of nonzero
rationals such that:

- $e_k(A)=e_k(B)=0$ for every odd $k<r$;
- $e_k(A)=e_k(B)$ for every $k\ne k_0$.

Equivalently, $\prod_A(x-a)-\prod_B(x-b)=\kappa\,x^{m-k_0}$, and $A,B$ are two full fibres of
the rational function $x\mapsto\prod_A(x-a)/x^{m-k_0}$. Then, if nonempty after cancellation,
$Z=A\uplus(-B)$ is an $(m-1)$-configuration of size $2m=2(m-1)+2$, the least possible, with
$\iota(Z)=0$.
````

### PS.5 (pte-structure): Proposition 3.2 (shift)

````
**Proposition 3.2 (shift).** Let $[X]=_k[Y]$ with $k\ge2L-3$, $|X|=|Y|=n$, and $X\cap Y=\emptyset$.
For $c\in\mathbb Q\setminus(-X\cup-Y)$ put $Z(c)=(X+c)\uplus(-(Y+c))$.

1. $s_j(Z(c))=0$ for odd $j\le2L-3$.
2. $\iota(Z(c))=2(\#\{x>-c\}-\#\{y>-c\})$. It is $0$ for $c>-\min(X\cup Y)$, and nonzero on
   some open interval of $c$.
3. $\rho(c):=s_{-1}(Z(c))=\sum_x\frac1{x+c}-\sum_y\frac1{y+c}$ is a nonzero rational function of
   $c$.
````

### PS.6 (pte-structure): Manuscript-facing versions (statements.tex)

````
\subsection{How many coefficients: the Prouhet--Tarry--Escott connection}\label{subsec:pte}

By Lemma~\ref{lem:sigdata} and Theorem~\ref{thm:sigsep}, two orbifolds in $\Sig$ with different
signatures share their first $L$ heat coefficients exactly when the cancelled mirror multiset
$Z=U^*\uplus(-V^*)$ is an \emph{$L$-configuration}. This means a nonempty multiset of nonzero
rationals, of even size and with no pair $\{z,-z\}$, such that
\[
  \sum_{z\in Z}z^{j}=0\quad(j\ \text{odd},\ 1\le j\le 2L-3),\qquad \sum_{z\in Z}z^{-1}=0 .
\]
Its size is $|Z|=|U^*|+|V^*|$, and its imbalance is $\iota(Z)=\#\{z>0\}-\#\{z<0\}=2(g'-g)$.

Let $N(k)$ be the least size of a non-trivial solution of the Prouhet--Tarry--Escott problem
of degree $k$, i.e.\ two distinct multisets of $n$ integers with equal power sums of exponents
$1,\dots,k$ \cite[\S1]{borweiningalls1994}. One has $k+1\le N(k)\le\tfrac12k(k+1)+1$
\cite[Props.~2, 3]{borweiningalls1994}. No bound $N(k)=o(k^2)$ is known, and this is listed
as an open problem in \cite[\S6]{borweiningalls1994}.

\begin{theorem}[Shape of a genus collision]\label{thm:ptedescartes}
Every $L$-configuration satisfies $|\iota(Z)|\le|Z|-2L$. Hence, if orbifolds in $\Sig$ of genera
$g\neq g'$ share their first $L$ heat coefficients, then
\[
  |U^*|+|V^*|\ \ge\ 2L+2|g-g'| ,
\]
and equality $|U^*|+|V^*|=2L+2$ forces $\{|U^*|,|V^*|\}=\{L,L+2\}$.
\end{theorem}

\begin{proposition}[Symmetric constructions do not change the genus]\label{prop:ptebalanced}
Let $A$ be an odd ideal symmetric solution of size $2L-1$, i.e.\ $\sum_{a\in A}a^j=0$ for odd
$j\le2L-3$ \cite[p.~8]{borweiningalls1994}. Then
$\#\{a>0\}-\#\{a<0\}=\operatorname{sgn}\sum_{a\in A}a^{-1}$. Consequently, for two such sets
$A,B$, every $L$-configuration $A\uplus\lambda B$ ($\lambda\in\mathbb Q^\times$) has
$\iota=0$.
\end{proposition}
````

### PG.0 (pte-growth): Definitions 1.3, 1.4, PTE notation and Lemma 1.5

````
**Definition 1.3.** For $L\ge2$:

- $\tau_L$ is the least size of an $L$-configuration;
- $T_L$ is the least size with $\iota\ne0$ (the $T_L$ of [Sig] §7);
- $T^{\rm cone}_L$ is the least size of an $L$-configuration with $\iota=0$ whose primitive
  integral form contains $\pm1$ and whose genus-0 realisation is hyperbolic.

Then $2L+2\le\tau_L\le T_L$ and $\tau_L\le T^{\rm cone}_L$.

**PTE notation** (Borwein–Ingalls 1994, `sources/NOTES.md` §1).

- $[A]=_k[B]$ means equal power sums $P_j$ for $1\le j\le k$, for distinct multisets $A,B$ of
  integers of a common size $n$.
- $N(k)$ is the least such $n$.
- $N(k)\ge k+1$ (their Prop. 2), and $N(k)\le\frac12k(k+1)+1$ (their Prop. 3, by pigeonhole).
- $N$ is nondecreasing, because a solution of degree $k+1$ is one of degree $k$.

**Definition 1.4.** $N_{\rm odd}(L)$ is the least $n$ such that two distinct $n$-multisets of
*positive* integers have equal $P_j$ for every odd $j\le2L-3$.

**Lemma 1.5.**

1. $N_{\rm odd}(L)\le N(2L-3)$.
2. $N_{\rm odd}(L)\le(L-1)^2+1$.
3. $N_{\rm odd}(L)=L$ for $3\le L\le6$.

````

### PG.1 (pte-growth): Proposition 3.3 (doubling)

````
**Proposition 3.3 (doubling).** Let $X\ne Y$ be $n$-multisets of positive integers with equal
$P_j$ for odd $j\le2L-3$. Put
$$U=X\uplus2Y\uplus2Y,\qquad V=Y\uplus2X\uplus2X .$$
Then $Z=U\uplus(-V)$, after cancellation, is a balanced $L$-configuration of size $\le6n$.

- If $1\in X\setminus Y$, the pair $(0;U\setminus\{1\})$, $(0;V)$ consists of hyperbolic genus-0
  orbifolds whose cone counts differ by the multiplicity of $1$ in $X$. If $1\in Y\setminus X$,
  exchange the roles of $X$ and $Y$.
- If $1\notin X\cup Y$, the cone counts are equal.

In every case the area is $<2\pi(3n-2)$.
````

### PG.2 (pte-growth): Theorem 3.4 (upper bounds)

````
**Theorem 3.4 (upper bounds).** For every $L\ge2$:
$$\tau_L\le6N_{\rm odd}(L)\le6(L-1)^2+6,\qquad T_L\le4N(2L-3),\qquad T^{\rm cone}_L\le6N(2L-3).$$
With $N(2L-3)\le\frac12(2L-3)(2L-2)+1=2L^2-5L+4$, all three are $O(L^2)$. The previous bound
was $T_L\le2^{2L-1}$ ([Sig] N(a)).
````

### PG.3 (pte-growth): Theorem 4.1 (square-root lower bound)

````
**Theorem 4.1 (square-root lower bound).** For every $L\ge2$ there are two genus-0 hyperbolic
orbifolds with different signatures and area $<2\pi(3N_{\rm odd}(L)-2)\le2\pi(3(L-1)^2+1)$ that
share at least $L$ heat coefficients. Consequently, for $A\ge8\pi$,
$$f(A)\ \ge\ \Bigl\lfloor\sqrt{\tfrac13\bigl(\tfrac{A}{2\pi}-1\bigr)}\Bigr\rfloor+2 .$$
````

### PG.4 (pte-growth): Theorem 4.2 (the exponent of f is a PTE exponent)

````
**Theorem 4.2 (the exponent of $f$ is a PTE exponent).**

(a) If $f(A)\ge L+1$, then $N(2L-2)\le2\lfloor A/\pi\rfloor+8$.

(b) If $N(k)\le Ck^\beta$ for all $k\ge1$, then $f(A)\ge\frac12(A/6\pi C)^{1/\beta}$ for all
$A\ge8\pi$.

(c) For $0<\alpha\le1$: $f(A)\ge cA^\alpha$ for all large $A$ (some $c>0$) if and only if
$N(k)\le Ck^{1/\alpha}$ for all $k$ (some $C$). In particular $f(A)=\Theta(A)$ iff
$N(k)=O(k)$.
````

### PG.5 (pte-growth): Theorem 4.3 (genus alone, cone count alone)

````
**Theorem 4.3 (genus alone, cone count alone).**

- Let $f_g(A)$ be the largest number of coefficients needed to determine the *genus* of an
  orbifold of area $\le A$, and $f_n(A)$ the analogous number for the *cone count* among
  genus-0 orbifolds.
- Then $f_g(A)\ge L+1$ whenever $A\ge8\pi N(2L-3)$, and $f_n(A)\ge L+1$ whenever
  $A\ge2\pi(3N(2L-3)-2)$. Both are therefore $\ge c\sqrt A$. Both are
  $\le\lfloor A/\pi\rfloor+4$ ([Sig] S2, T1).
- Theorem 4.2(c) holds verbatim for $f_g$ and for $f_n$. "⇐": by the two thresholds just
  stated. "⇒": a genus or cone-count collision is in particular a collision of signatures, so
  $f_g\le f$ and $f_n\le f$, and Theorem 4.2(a) applies.
````

### PG.6 (pte-growth): Manuscript-facing version (statements.tex): Theorem (Growth) and Theorem (Descartes)

````
\begin{theorem}[Growth]\label{thm:ptegrowth}
Let $f(A)=\max\{\Kmult(\Orb;\Sig):\operatorname{Area}(\Orb)\le A\}$.
\begin{enumerate}[label=(\alph*)]
\item For $A\ge8\pi$,
  \[
    \Bigl\lfloor\sqrt{\tfrac13\bigl(\tfrac{A}{2\pi}-1\bigr)}\Bigr\rfloor+2\ \le\ f(A)\ \le\ \Bigl\lfloor\frac{A}{\pi}\Bigr\rfloor+4 .
  \]
\item If $f(A)\ge L+1$, then $N(2L-2)\le2\lfloor A/\pi\rfloor+8$.
\item For $0<\alpha\le1$: $f(A)\ge cA^{\alpha}$ for all large $A$ and some $c>0$ if and only if
  $N(k)\le Ck^{1/\alpha}$ for all $k$ and some $C$. In particular $f(A)=\Theta(A)$ if and only
  if $N(k)=O(k)$.
\end{enumerate}
The lower bound in (a) also holds, up to the constant, for the number of coefficients needed
to determine the genus alone, and for the number needed to determine the cone count alone
within genus $0$.
\end{theorem}
````

### PW.0 (pte-witnesses): Headline table (proof.md section 0, items 5 and 6)

````
5. **Explicit witnesses (§5).** Pairs sharing exactly $L$ coefficients, verified with the actual
   cone coefficients:

   | $L$ | least area found, any pair: Area$/2\pi$ | genus pair: $\lvert U^*\rvert+\lvert V^*\rvert$ | genus 0, cone counts $n$ vs $n'$ | Thue–Morse bound on Area$/2\pi$ |
   |---|---|---|---|---|
   | 2 | $1/4$ | 6 | 3 vs 4 | 3 |
   | 3 | $22/15$ | 10 | 7 vs 8 | 15 |
   | 4 | $\approx5.000$ | 16 | 11 vs 12 | 63 |
   | 5 | $\approx7.000$ | 20 | 22 vs 23 | 255 |
   | 6 | $\approx10.000$ | 26 | 29 vs 30 | 1023 |
   | 7 | $\approx18.000$ | 40 | 35 vs 36 | 4095 |

6. **$T_3$ (§6).** $T_3\in\{8,10\}$ is not decided. An exhaustive exact search excludes every
   size-8 genus collision whose 5-element side, made primitive, has entries $\le220$. The
   collision must have shape $(3,5)$ (Theorem 2.1). Real solutions of that shape exist in
   abundance, so the obstruction, if there is one, is arithmetic.
````

### PW.1 (pte-witnesses): Example (Small pairs) and Remark (first open case), as in statements.tex

````
\begin{example}[Small pairs]\label{ex:ptepairs}
The following pairs share exactly $L$ heat coefficients (exact computation with the cone
coefficients):
\begin{itemize}
\item $L=3$, same genus and cone count: $(0;3,10,15,30)$ and $(0;4,5,21,28)$, of area
  $2\pi\cdot\frac{22}{15}$. Previously the smallest area known to share three coefficients was
  $2\pi\cdot\frac{14}5$, for $(1;15,15,15)$ and $(0;3,3,5,7,7,21)$.
\item $L=3$, genus $0$ with $7$ and $8$ cone points: $(0;4,4,5,5,6,12,12)$ and
  $(0;2,2,2,3,10,10,10,10)$, obtained from $[1,5,5]=[2,3,6]$ \cite{chen2025survey} by the doubling
  above. This replaces $103$ vs $104$.
\item $L=4,5,6,7$: genus-$0$ pairs with equal cone counts and area
  $<2\pi\cdot5,\,7,\,10,\,18$. They come from pairs of odd ideal symmetric solutions of sizes $7$
  and $9$ \cite{borweiningalls1994,blp2003}, from equal sums of odd powers
  \cite{chen2025survey}, and from the size-$12$ ideal solution \cite{cmsv2024}. The
  Prouhet--Thue--Morse pairs of Theorem~\ref{thm:signonuniform} need area up to
  $2\pi(4^{L-1}-1)$.
\item Genus $1$ versus genus $0$ sharing $L=4,5,6,7$ coefficients: configurations of size
  $16,20,26,40$, against $2^{2L-1}=128,512,2048,8192$ for Thue--Morse.
\end{itemize}
\end{example}

\begin{remark}[The first open case]\label{rem:ptet3}
By Theorem~\ref{thm:ptedescartes}, a genus collision sharing three coefficients with
$|U^*|+|V^*|=8$ must have shape $(3,5)$. An exhaustive exact search excludes all such collisions
whose five-element side, made primitive, has entries $\le220$. Real solutions of this shape
exist. So whether the least size is $8$ or $10$ remains open.
\end{remark}
````

### PW.2 (pte-witnesses): Improved lower bounds on f in the covered range

````
**Improved lower bounds on $f$ in the covered range.** Let $A_L$ be the least area in the
tables above among pairs sharing $L$ coefficients. Then $f(A)\ge L+1$ for $A\ge A_L$:

| $f(A)\ge$ | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|
| for $A/2\pi\ge$ (new) | $1/4$ | $22/15$ | $5.000$ | $7.000$ | $10.000$ | $18.000$ |
| for $A/2\pi\ge$ ([Sig] N1) | 3 | 15 | 63 | 255 | 1023 | 4095 |

The exact values of $A_L$ are in `data/witnesses.json`. The $\approx$ values lie just below
the integers shown, e.g. $A_4/2\pi=4.99999\ldots$, so "$\ge5.000$" is a safe rounding up.

Over this range the best pairs have Area$/2\pi\approx T/2-2$ with $T\le4L-2$ for $L\le5$. So
for $A/2\pi\le18$, $f$ grows at least linearly: $f(A)\ge L+1$ at
$A/2\pi\approx2L-3$ for $L\le5$.
````

### PW.3 (pte-witnesses): Integer sharpness witnesses for Theorem A at n=4, and the n=5 claim

````
*Instances.* For $m=4$ the hypothesis says that $A,B$ have $e_1=0$ and equal $e_3,e_4$.
`pencil_search.py` finds 25 distinct configurations from 4-sets with entries $\le130$, and 61
with entries $\le220$ (`data/pencil_log.txt`). These include 60 integer sharpness witnesses
for Theorem A at $n=4$ beyond the one recorded in `theory/audibility`. The smallest is
$A=\{-30,-3,5,28\}$, $B=\{-21,-4,10,15\}$, which gives
$\{3,10,15,30\}\sim\{4,5,21,28\}$. That is the $n=4$ witness of `theory/audibility/proof.md`
Theorem C(3) and Chen's type $(-1,1,3)$ entry A.685. So Theorem C(3) at $n=4$ is a pencil
phenomenon.

For $m=5$ the hypothesis asks for two odd symmetric 5-sets with equal $e_4,e_5$. Such a pair
would give a balanced 4-configuration of size 10, i.e. the integer sharpness of Theorem A at
$n=5$, which is open in `theory/audibility`. Among all 1,592 primitive 5-sets with entries
$\le200$, no such pair exists.
````

### PW.4 (pte-witnesses): The 18 claimed pairs (generated; recipes and Z omitted)

````
(generated data: see `statements/pte-witnesses.md`, item PW.4)
````

### PW.5 (pte-witnesses): The 61 claimed pencil configurations (generated)

````
(generated data: see `statements/pte-witnesses.md`, item PW.5)
````

### TF.1 (trace-formula): Notation for the elliptic moments, and Lemma (Elliptic moments)

````
\subsection{The expansion}\label{sec:heatexp}

The structure of the expansion is due to Donnelly and to Dryden, Gordon, Greenwald and Webb
\cite{donnelly1976,dggw2008}, and U\c{c}ar computed every coefficient at constant curvature
\cite{ucar2017}. We derive the coefficients again from the trace formula of
Theorem~\ref{thm:IEH}, which gives them in closed form for every order. For $0<a<2\pi$ put
\[
  F_a(r)=\frac{e^{-ar}}{1+e^{-2\pi r}},\qquad \mu_n(a)=\int_\R r^nF_a(r)\,dr ,
\]
so that $F_a(r)\le e^{-ar}$ for $r\ge0$ and $F_a(r)\le e^{(2\pi-a)r}$ for $r\le0$, and every
$\mu_n(a)$ is finite.

\begin{lemma}[Elliptic moments]\label{lem:ellmoments}
Let $0<a<2\pi$.
\begin{enumerate}[label=(\roman*)]
\item For $a-2\pi<s<a$, $\displaystyle\int_\R F_a(r)\,e^{sr}\,dr=\frac1{2\sin((a-s)/2)}$; hence
  $\mu_n(a)=\frac{d^n}{ds^n}\big[2\sin((a-s)/2)\big]^{-1}\big|_{s=0}$.
\item For every $K\ge1$ and $t>0$,
  \[
    \Big|\int_\R F_a(r)\,e^{-tr^2}\,dr-\sum_{k=0}^{K-1}\frac{(-t)^k}{k!}\,\mu_{2k}(a)\Big|
    \le\frac{t^K}{K!}\,\mu_{2K}(a).
  \]
\end{enumerate}
\end{lemma}
````

### TF.2 (trace-formula): Definition of Phi_m and Lemma (Closed form)

````
Write $\theta_j=\pi j/m$ and, for an integer $m\ge1$,
\[
  \Phi_m(u)=\sum_{j=1}^{m-1}\frac1{4m\,\sin\theta_j\,\sin(\theta_j-u)} .
\]
Each term is analytic in $|u|<\pi/m$, so $\Phi_m$ is analytic there; $\Phi_1=0$, and
$\Phi_m(-u)=\Phi_m(u)$ (replace $j$ by $m-j$).

\begin{lemma}[Closed form]\label{lem:Phi}
For $m\ge1$ and $0<|u|<\pi/m$,
\begin{equation}\label{eq:Phi}
  \Phi_m(u)=\frac{\cot u-m\cot(mu)}{4m\sin u}.
\end{equation}
Write $u/\sin u=\sum_{i\ge0}\sigma_iu^{2i}$, so $\sigma_i\in\Q$, $\sigma_0=1$ and in fact $\sigma_i>0$.
Then $\Phi_m(u)=\sum_{k\ge0}\phi_k(m)\,u^{2k}$ with
\begin{equation}\label{eq:phik}
  m\,\phi_k(m)=\frac14\sum_{n=1}^{k+1}\sigma_{k+1-n}\,\frac{4^n|B_{2n}|}{(2n)!}\,\big(m^{2n}-1\big).
\end{equation}
\end{lemma}
````

### TF.3 (trace-formula): Lemma (The hyperbolic term is small)

````
\begin{lemma}[The hyperbolic term is small]\label{lem:hypbound}
Let $\Orb\in\Sig$ have area $A$, systole $\ell$ and diameter $D$. For $0<t\le\ell^2/(2(1+\ell))$,
\[
  0\le\Hyp(t)\le\frac{\pi e^{3D}}{A(1-e^{-\ell})}\;\ell e^{\ell/2}\Big(1+\frac{2t}{\ell-t}\Big)\frac{e^{-\ell^2/4t}}{\sqrt{4\pi t}} .
\]
In particular $\Hyp(t)=O(t^N)$ as $t\downarrow0$ for every $N$.
\end{lemma}
````

### TF.4 (trace-formula): Proposition (The heat expansion at curvature -1)

````
\begin{proposition}[The heat expansion at curvature $-1$]\label{prop:heatinput}
Let $\Orb\in\Sig$ have signature $(g;m_1,\dots,m_n)$. As $t\downarrow0$,
\[
  \cZ_\Orb(t)\ \sim\ \frac{\Area(\Orb)}{4\pi t}\sum_{k\ge0}\alpha_kt^k\;+\;\sum_{i=1}^n\sum_{l\ge0}b_l(m_i)\,t^l,
\]
where
\begin{equation}\label{eq:alphak}
  \alpha_k=\frac{(-1)^k}{k!\,4^k}\sum_{l=0}^k\binom kl(-4)^lB_{2l}\big(\tfrac12\big)
\end{equation}
and, for every integer $m\ge1$,
\begin{equation}\label{eq:bl}
  b_l(m)=\frac{(-1)^l\,p_l(m)}{m},\qquad
  p_l(m)=\frac1{4^l}\sum_{k=0}^{l}\frac{(2k)!}{k!\,(l-k)!}\;m\,\phi_k(m).
\end{equation}
Consequently $c_1=\Area(\Orb)/4\pi$ and, for $j\ge2$,
\begin{equation}\label{eq:cj}
  c_j(\Orb)=\alpha_{j-1}\,\frac{\Area(\Orb)}{4\pi}+\sum_{i=1}^nb_{j-2}(m_i).
\end{equation}
\end{proposition}
````

### TF.5 (trace-formula): Lemma (Cone polynomials) = Lemma 2.5, and the printed first values

````
\begin{lemma}[Cone polynomials]\label{lem:conepoly}
For every $l\ge0$, $p_l$ is an even polynomial with rational coefficients, of degree exactly
$2l+2$, with $p_l(1)=0$ and leading coefficient
\[
  \frac{|B_{2l+2}|}{2\,(l+1)!\,(2l+1)}\ne0 .
\]
Moreover $p_l(m)>0$ for every real $m>1$.
\end{lemma}

The first values are $\alpha_0,\dots,\alpha_4=1,-\tfrac13,\tfrac1{15},-\tfrac4{315},\tfrac1{315}$, and
\begin{equation}\label{eq:plexplicit}
  p_0(m)=\frac{m^2-1}{12},\qquad p_1(m)=\frac{m^4}{360}+\frac{m^2}{36}-\frac{11}{360},\qquad p_2(m)=\frac{m^6}{2520}+\frac{m^4}{720}+\frac{m^2}{180}-\frac{37}{5040}.
\end{equation}
The polynomials $p_1,p_2$ agree with the cone coefficients of Schueth \cite[Rem.~4.2, Thm~4.1]{schueth2019},
which she attributes to \cite[\S5.6]{dggw2008} at order $t^1$.
The value $p_l(1)=0$ has a direct meaning: an ``order-$1$ cone point'' is a smooth point, and the sum
defining $\Phi_1$ is empty.
````

### TF.6 (trace-formula): Remark (Agreement with Ucar), the claim

````
\begin{remark}[Agreement with U\c{c}ar]\label{rem:ucaragree}

[derivation of the identity m t^2 Phi_m(it/2) = ... omitted]

where, by \cite[(4.25)]{ucar2017},
\[
  c^{\mathbb S}_k\Big(\frac\pi m\Big)=\frac1{4m}\cdot\frac{(-1)^k}{(k+1)!\,(2k+1)}\sum_{j=0}^{k+1}\binom{2k+2}{2j}\big(m^{2j}-1\big)B_{2j}\,B_{2k+2-2j}\big(\tfrac12\big).
\]
Then \eqref{eq:bl} becomes $p_l(m)/m=\sum_{i\le l}2(4^ii!)^{-1}c^{\mathbb S}_{l-i}(\pi/m)$, which is $(-1)^l$
times U\c{c}ar's cone contribution \cite[(4.33)--(4.34)]{ucar2017} at $K=-1$. So the cone terms of
Proposition~\ref{prop:heatinput} are U\c{c}ar's for every $l$; his smooth coefficients
\cite[(4.35)]{ucar2017} are given by the same formula as \eqref{eq:alphak}. The two were also compared in
exact arithmetic for $l\le40$ (code in the archived repository, Appendix~\ref{app:reproducibility}).
````

### TF.7 (trace-formula): Remark 4.12 (the trace-formula proof of locality): the independence claim, versions 2A and 2B and the replacement sentence

````
No local invariant can see the moduli: any two hyperbolic orbifolds of the same signature are
locally isometric, point by point and cone point by cone point. The trace formula of
Theorem~\ref{thm:IEH} gives a second, independent proof, with the coefficients
(Remark~\ref{rem:proofC}).

% (1A) if lemma25.tex is adopted (version 2A), where the trace formula is the primary proof:
%   "No local invariant can see the moduli: any two hyperbolic orbifolds of the same signature
%    are locally isometric, point by point and cone point by cone point; this structural reading,
%    through the locality of the heat invariants \cite{donnelly1976,dggw2008}, is a second proof.

\begin{remark}[The trace-formula proof of locality]\label{rem:proofC}
Theorem~\ref{thm:IEH} proves Theorem~\ref{thm:locality} directly: $\mathrm I$ depends only on the
area and $\mathrm E$ only on the cone orders, and $0\le\Hyp(t)=O(t^{-1/2}e^{-\ell^2/4t})=O(t^N)$ for
every $N$ (Lemma~\ref{lem:hypbound}), so the asymptotic series of $\cZ_\Orb$ is that of
$\mathrm I+\mathrm E$. This is how Proposition~\ref{prop:heatinput} and Lemma~\ref{lem:conepoly} were
proved, and it is independent of the coefficient computations of \cite{dggw2008} and
\cite{ucar2017}. The only input from the heat-kernel literature is the a-priori bound
$\#\{\lambda_j\le x\}\le e\,\cZ_\Orb(1/x)=O(x)$ in the proof of Lemma~\ref{lem:admissible}, which uses
only the a-priori bound $\cZ_\Orb(s)=O(1/s)$ as $s\downarrow0$, a consequence of \cite[Thm~4.8]{dggw2008}
(or of Weyl's law). It determines no coefficient $c_j$ with $j\ge2$, so nothing is circular. U\c{c}ar's
cone terms \cite[(4.25), (4.33)--(4.34)]{ucar2017} agree with Proposition~\ref{prop:heatinput} for every
order (Remark~\ref{rem:ucaragree}), and his smooth coefficients \cite[(4.35)]{ucar2017} are given by
the same formula as \eqref{eq:alphak}.
\end{remark}

\begin{remark}[The trace-formula proof of locality]\label{rem:proofC}
Theorem~\ref{thm:IEH} gives an independent proof of Theorem~\ref{thm:locality}: $\mathrm I$ and
$\mathrm E$ depend only on the signature, and $0\le\Hyp(t)=O(t^{-1/2}e^{-\ell^2/4t})=O(t^N)$ for every
$N$, so the asymptotic series of $\cZ_\Orb$ is that of $\mathrm I+\mathrm E$. Expanding
$e^{-tr^2}$ under the integrals, with the moments
$\int_0^\infty r^{2k+1}(e^{2\pi r}+1)^{-1}dr=(1-2^{-2k-1})(-1)^kB_{2k+2}/(4(k+1))$ and
$\int_\R e^{-ar}(1+e^{-2\pi r})^{-1}e^{sr}dr=1/(2\sin((a-s)/2))$, reproduces the constants $\alpha_k$
and $b_l(m)$ of Proposition~\ref{prop:heatinput} for every order. This route does not use the
coefficient computations of \cite{dggw2008} or \cite{ucar2017}. Its only input from the
heat-kernel literature is the a-priori bound $\#\{\lambda_j\le x\}\le e\,\cZ_\Orb(1/x)=O(x)$ in
Lemma~\ref{lem:admissible}, which uses only $\cZ_\Orb(s)=O(1/s)$, a consequence of
\cite[Thm~4.8]{dggw2008} (or of Weyl's law), and determines no $c_j$ with $j\ge2$.
\end{remark}
````

### TF.8 (trace-formula): Theorem 1.2(iii): the constant and the 'attained' statement; Theorem 4.9(b) form

````
\item Let $\Orb_1,\Orb_2$ have the same signature and area $A$, let $\ell$ be the smaller of their
systoles and $D$ the larger of their diameters. For $0<t\le\ell^2/(2(1+\ell))$,
\[
  |\cZ_{\Orb_1}(t)-\cZ_{\Orb_2}(t)|\le C(A,\ell,D)\,t^{-1/2}e^{-\ell^2/4t},\qquad
  C(A,\ell,D)=\frac{\sqrt\pi\,e^{3D}\,\ell\,e^{\ell/2}\,(2+3\ell)}{2A\,(1-e^{-\ell})\,(2+\ell)} .
\]
The constant depends on the diameter, which the signature does not determine. If the two length
spectra, counted with the weights $\ell(\gamma_0)$, first differ at the length $\ell$ (in particular,
if the two systoles differ), then $\sqrt t\,e^{\ell^2/4t}|\cZ_{\Orb_1}(t)-\cZ_{\Orb_2}(t)|$ has a
nonzero limit as $t\downarrow0$: the exponent $\ell^2/4$ and the factor $t^{-1/2}$ are attained,
the constant $C$ is not claimed to be. If they first differ at a length $L_*>\ell$, the difference
is of the smaller order $t^{-1/2}e^{-L_*^2/4t}$; if the weighted length spectra never differ
(equivalently, the orbifolds are isospectral) the difference vanishes identically. Here the
systole is the least length of a closed geodesic, including those through cone points.

%   For $0<t\le\ell^2/(2(1+\ell))$,
%   \[
%     |\cZ_{\Orb_1}(t)-\cZ_{\Orb_2}(t)|\le\frac{\pi e^{3D}}{A(1-e^{-\ell})}\;\ell e^{\ell/2}\Big(1+\frac{2t}{\ell-t}\Big)\frac{e^{-\ell^2/4t}}{\sqrt{4\pi t}}
%     \le C(A,\ell,D)\,t^{-1/2}e^{-\ell^2/4t},
%   \]
%   with $D=\max(\operatorname{diam}\Orb_1,\operatorname{diam}\Orb_2)$ and $C$ as in Theorem 1.2(iii);
````

### DE.0 (descent): The claimed isomorphism and its inverse

````
[COMPOSED. C_{27/2} is the plane cubic of the Diophantine section with Lambda = 27/2 (see context). Claim: with e_2 = XY+YZ+ZX the maps below are mutually inverse isomorphisms over Q between C_{27/2} and the elliptic curve E, sending the origin of E to O = (1:-1:0).]

  \varphi(X:Y:Z)=\Big(-\frac{16e_2}{Z^2},\ \frac{8(X-Y)}Z\Big(-\frac{4e_2}{Z^2}-54\Big)\Big),\qquad
  \psi(x,y)=\big(25x+y:\ 25x-y:\ 4(x-216)\big).

  E:\ y^2=x(x+9)(x+384)=x^3+393x^2+3456x,
````

### DE.1 (descent): The rank claim

````
[COMPOSED from the proof's claims. With E': y^2 = x(x^2 + c'x + d'), c' = -786, d' = 140625 the 2-isogenous curve of E (c = 393, d = 3456): the two 2-isogeny Selmer-type groups are {+-1, +-6} (order 4) for E and {1} for E'; rank E(Q) = 0, with no Sha ambiguity.]
````

### DE.2 (descent): The torsion claim

````
[COMPOSED.] E(Q) = E(Q)_tors is isomorphic to Z/2 x Z/6, and consists of the twelve points

  O,\ (0,0),\ (-9,0),\ (-384,0),\ (-24,\pm360),\ (-144,\pm2160),\ (16,\pm400),\ (216,\pm5400)
\]

[with (0,0), (-9,0), (-384,0) of order 2, (16,+-400) of order 3, and (-24,+-360), (-144,+-2160), (216,+-5400) of order 6. The proof reduces E modulo 7 and 11 and counts #E(F_7) = #E(F_11) = 12.]
````

### DE.3 (descent): The twelve rational points of C_{27/2}

````
\emph{The points of $C_{27/2}$.} The twelve points $(1:0:0)$, $(0:1:0)$, $(0:0:1)$, $(1:-1:0)$,
$(0:1:-1)$, $(1:0:-1)$ and the permutations of $(1:4:4)$ and $(1:1:4)$ lie on $C_{27/2}$ and are
distinct, so they are all of $C_{27/2}(\Q)$; the positive ones are the six permutations of $(1:4:4)$
and $(1:1:4)$.
````

### DE.4 (descent): Consequence for triads

````
A triad with $S_1=18k$ and $R=\frac3{4k}$ has $\Lambda=\frac{27}2$, so it is a positive rational point of
$C_{27/2}$, hence a permutation of $(1:4:4)$ or $(1:1:4)$. Each has exactly one integer representative
with sum $18k$, namely $(2k,8k,8k)$ and $(3k,3k,12k)$, and both are hyperbolic since $R=\frac3{4k}<1$.
````

### DE.5 (descent): Theorem 5.16 (isolation) as in the manuscript (statement unchanged)

````
**What does *not* adapt: the base pair is isolated.** $C_{27/2}$ has rank 0
**unconditionally**. PARI/GP 2.17.2 `ellrank` on the integral model
$[0,393,0,3456,0]$ returns $[0,0,0,[\,]]$, and the manual states that the
upper bound $r_2=C-T-s$ is computed unconditionally from the 2-Selmer group.
`elltors` gives torsion of order 12, $\mathbf Z/2\times\mathbf Z/6$.
`ranks.py` lists the 12 points on the plane cubic exactly (the six base
points and their translates by the order-6 point $(1,4,4)$) and asserts that
the only positive ones are the permutations of $(1,4,4)$ and $(1,1,4)$. Hence, for every
$k$, the class of $\{(2k,8k,8k),(3k,3k,12k)\}$ has exactly two members: no
third pillow ever joins the minimal degeneracy. Every isosceles
triple tested is torsion: all 1,482 triples $(u,v,v)$ with $u\ne v\le39$,
by exact order computation. So the isosceles
family, including the base pair, is (as far as tested) a torsion phenomenon, and the unbounded
````

### DE.6 (descent): The coordinates of 3P

````
[COMPOSED. C_{155/12} is the cubic C_Lambda with Lambda = 155/12; the group law is the chord-tangent law with base point O = (1:-1:0). Claim:]

% With base point O = (1:-1:0) and P = (4:9:18) on C_{155/12}:
%   2P = (16352 : 288 : -365),   3P = (162833463 : 723926268 : 287876366).

[The manuscript previously printed 3P = (162833463 : 287876366 : 723926268); the corrected claim is 3P = (162833463 : 723926268 : 287876366).]
````

### SB.0 (stability): Setting and recovery map (previously audited)

````
### ST.0. Setting and the recovery map

Source: `theory/stability/proof.md` lines 45-75 (verbatim).

````
## 1. Setting and the recovery map

Conventions (`numerics/REPORT.md` §2; `theory/cone-coefficients/ucar-source.md`): positive
Laplacian, K = κ = −1, and

- H₋₁ = Area/(4π) = (n − 2 − R)/2;
- H_ν = (Area/4π)·α_{ν+1} + Σ_i b_ν(m_i) for ν ≥ 0;
- b_ν(m) = (−1)^ν p_ν(m)/m, with p_ν = Σ_k π_{ν,k} m^{2k} even of degree 2ν + 2 and
  p_ν(1) = 0 (Uçar (4.25)+(4.33));
- α_j = a_j^{sm}/vol (Uçar (4.35)): α = 1, −1/3, 1/15, −4/315, 1/315, …

The smooth coefficients α_j are also derived independently from the Selberg identity term
(`stab_common.alpha_smooth_selberg`), and the two agree for j ≤ 11.

The number n of cone points is assumed known. The **recovery map** studied throughout is:

1. **Front end.** Ĩ := L⁻¹(H̃ − h₀).
2. **Linear solve.** ẽ := M(Ĩ)⁻¹ b(Ĩ) (Theorem B).
3. **Roots.** Take the roots of q̃(z) := Σ_{j=0}^{n}(−1)^j ẽ_j z^{n−j}, with ẽ₀ = 1.
4. **Rounding** (integer orders only). Round the real part of every root.

Throughout, μ := max_i m_i. Hats denote scale-free quantities:

- m̂ = m/μ ∈ (0,1]ⁿ and ê_k = e_k/μ^k;
- Î = (μR, P₁/μ, P₃/μ³, …).

Theorem B's system is weighted-homogeneous: row j has weight 2j+1, the last row weight n−1,
and column k weight k. Hence M(Î) = D_r⁻¹ M(I) D_c, and ê solves M(Î) ê = b(Î).
Distances between multisets are optimal matching distances,
d(m, m′) = min_π max_i |m_i − m′_{π(i)}|.

````

````

### SB.0b (stability): Front-end tables, Lemmas S2, Theorem S2, Lemma S3 and Theorem S3 (previously audited; define delta_thm)

````
### ST.2. Front-end tables (claims)

Source: `theory/stability/proof.md` lines 100-131 (verbatim).

````
The first rows of L⁻¹, which give I = L⁻¹(H − h₀):

| | H₋₁ | H₀ | H₁ | H₂ | H₃ |
|---|---|---|---|---|---|
| R | −2 | | | | |
| P₁ | 2 | 12 | | | |
| P₃ | −18 | −120 | −360 | | |
| P₅ | 30 | 252 | 1260 | 2520 | |
| P₇ | −70/3 | −240 | −1680 | −6720 | −10080 |

**Amplification.** With every |δH_ν| ≤ δ, the worst-case error in I_r is ℓ_r·δ, where ℓ_r is
the absolute row sum of L⁻¹. Row r involves only the first r+1 coefficients, so ℓ_r is the
same for every n:

| | R | P₁ | P₃ | P₅ | P₇ | P₉ | P₁₁ | P₁₃ |
|---|---|---|---|---|---|---|---|---|
| diagonal 1/\|L_rr\| | 2 | 12 | 360 | 2520 | 10080 | 28512 | 43243200/691 | 112320 |
| ℓ_r (row sum) | 2 | 14 | 498 | 4062 | 56230/3 | 303654/5 | 104899830/691 | 10805786/35 |

**Correction to the review (DEFECTS.md MAJ-05).**

- The factors 12, 360, 2520 are correct as the diagonal entries of L⁻¹: for P₁ from H₀, P₃
  from H₁ and P₅ from H₂.
- They are not the amplification factors. Each invariant also inherits the errors of all
  lower coefficients through the off-diagonal entries, e.g.
  δP₃ = −18 δH₋₁ − 120 δH₀ − 360 δH₁.
- So the worst-case factors are **14, 498, 4062**, larger by 1.17, 1.38 and 1.61.
- R is recovered from H₋₁ with factor 2. Equivalently, R = n − 2 − Area/(2π), so the factor
  is 1/(2π) per unit of area.
- In relative terms the front end is harmless. The ratio
  κ_r = Σ_c |(L⁻¹)_{rc}| |H_c| / |I_r| lies between 0.02 and 3.7 on every test multiset of
  `front_end_output.md`. For (2,8,8) it is 0.33, 0.94, 1.33 for R, P₁, P₃.
````

### ST.3. Lemma S2.1

Source: `theory/stability/proof.md` lines 142-146 (verbatim).

````
**Lemma S2.1 (the constant c_n of Theorem B, all n).** For every n ≥ 2,

  det M = (−1)^{n(n+1)/2} ∏_{i<j}(m_i + m_j) / e_n,

so c_n = (−1)^{n(n+1)/2}. This replaces "c_n ∈ ℚ^×, computed for n ≤ 8" in Theorem B.
````

### ST.4. Lemma S2.2

Source: `theory/stability/proof.md` lines 172-183 (verbatim).

````
**Lemma S2.2 (Hurwitz factorisation of M).** Let f(z) = ∏(1 + m_i z) = E(z²) + zO(z²), and for
D(z) = Σ_{k=1}^n d_k z^k let W_D := E_f O_D − E_D O_f, a polynomial in w = z² of degree ≤ n−1.
Define two n × n matrices (with e_i := 0 outside 0 ≤ i ≤ n):

- B_{k,j} = (−1)^{j+1} e_{2k+1−j}, for 0 ≤ k ≤ n−1 and 1 ≤ j ≤ n. This is the map
  d ↦ (coefficients of W_D).
- S_{k,i} = e_{2(k−i)} for i ≤ k ≤ n−2, S_{n−1,n−1} = (−1)ⁿ e_n, and all other entries 0.

Then

  B = S·M,  det B = (−1)^{n(n−1)/2} ∏_{i<j}(m_i+m_j),  M⁻¹ = B⁻¹ S.

````

### ST.5. Theorem S2

Source: `theory/stability/proof.md` lines 196-222 (verbatim).

````
**Theorem S2 (Lipschitz dependence of e on I_n, explicit constants).**

*Setting.* Let m be positive reals and μ = max m_i. Let Ĩ be any real data vector with
scale-free error

  η := max( μ|R̃ − R|, max_{1≤l≤n−1} |P̃_{2l−1} − P_{2l−1}| / μ^{2l−1} ) ≤ 1.

*Constants.* Put κ := ‖M(Î)⁻¹‖_∞ and

- σ_k(n) := [w^k] artanh(w) · sec²((n+1) artanh w). For instance σ₁ = 1 and
  σ₃ = 1/3 + (n+1)²; n = 3: (1, 49/3); n = 4: (1, 76/3, 6628/15).
- ζ_n := max(1, max_{0≤j≤n−2} Σ_{0≤i<j, 2≤2j−2i≤n} σ_{2i+1}(n)). For example ζ₃ = 1,
  ζ₄ = 79/3, ζ₅ = 14048/15.
- ρ_n(m̂) := max( ê_n, max_{0≤j≤n−2} Σ_{i=0}^{j} σ_{2i+1}(n) ê_{2j−2i} ).

*Conclusions.*

(a) The inverse is bounded by

  κ ≤ n Λ(m̂) ‖Ŝ‖_∞ / ∏_{i<j}(m̂_i + m̂_j) ≤ n · binom(2n,n)^{n/2} · 2^{n−1} / ∏_{i<j}(m̂_i + m̂_j),

  where Λ(m̂) = ∏_c ‖c-th column of B(ê)‖₂ and ‖Ŝ‖_∞ ≤ max(Σ_{k even} ê_k, ê_n).

(b) If β := κ ζ_n η ≤ 1/2, then M(Ĩ) is invertible, and ẽ = M(Ĩ)⁻¹ b(Ĩ) satisfies

  max_k |ẽ_k − e_k| / μ^k ≤ 2 κ ρ_n(m̂) η.

````

### ST.6. Ostrowski input as quoted

Source: `theory/stability/proof.md` lines 264-273 (verbatim).

````
**Standard global theorem (fetched, `review/literature/root-perturbation.md`).** Ostrowski,
*Acta Math.* 72 (1940), Théorème XXX, eq. (71,1), p. 212, read from the primary. For monic
f, g of degree n with roots x_ν and y_ν, after renumbering,

  |y_ν − x_ν| ≤ (2n−1)ε,  ε = (Σ_{ν=1}^{n} |a_ν − b_ν| γ^{n−ν})^{1/n},

where γ is the largest root modulus. "Les racines … satisfont … à une condition de Lipschitz
d'ordre 1/n." This is uniform but crude: exponent 1/n everywhere, with no use of
separation. The local statement below has the exponent 1/k at a k-fold root, and is
Lipschitz at simple roots, with explicit constants.
````

### ST.7. Lemma S3

Source: `theory/stability/proof.md` lines 275-287 (verbatim).

````
**Lemma S3 (clusters, explicit Rouché).** Work in scale-free variables. Let
q(z) = ∏(z − m̂_i) = Σ_j (−1)^j ê_j z^{n−j}, and let q̃ be the same polynomial with ẽ in place
of ê, where |ẽ_j − ê_j| ≤ ε. Let a be a distinct value among the m̂_i, of multiplicity k, and
put

- g_a := min_{b≠a} |a − b| (∞ if there is no other value);
- Q_a := ∏_{b≠a} |a − b|^{k_b}.

If 0 < r ≤ min(g_a, 1)/2 and r^k Q_a ≥ 2^{1−k} 3ⁿ ε, then q̃ has exactly k zeros in |z − a| < r.
In particular, for r_a(ε) := (2^{1−k}3ⁿ ε/Q_a)^{1/k}, whenever r_a(ε) ≤ min(g_a, 1)/2, the k
roots of the cluster lie within r_a(ε) = O(ε^{1/k}) of a. The bound is Lipschitz for simple
orders, where Q_a = |q′(a)|.

````

### ST.8. Theorem S3

Source: `theory/stability/proof.md` lines 301-321 (verbatim).

````
**Theorem S3 (heat coefficients → orders; the combined stability theorem).**

*Setting.* Let m be positive reals, n = |m|, μ = max m_i. Let H̃ be data with
δ := max_{−1≤ν≤n−2} |H̃_ν − H_ν(m)|. Put

- λ_μ := max(μ ℓ₀, max_{1≤r≤n−1} ℓ_r μ^{1−2r}), with ℓ = (2, 14, 498, 4062, …) as in §2;
- κ, ρ_n, ζ_n as in Theorem S2.

*Statement.* Suppose λ_μ δ ≤ 1 and κ ζ_n λ_μ δ ≤ 1/2. Then for every distinct order a, of
multiplicity k_a, with

  r_a := μ · (2^{2−k_a} 3ⁿ κ ρ_n λ_μ δ / Q̂_a)^{1/k_a} ≤ μ · min(ĝ_a, 1)/2,

the recovered polynomial q̃ has exactly k_a roots within r_a of a. Consequently, if the
radius hypothesis holds for **every** distinct order a,

  d(roots of q̃, m) ≤ max_a C_a δ^{1/k_a},  C_a = μ (2^{2−k_a} 3ⁿ κ ρ_n λ_μ / Q̂_a)^{1/k_a}.

So recovery is Lipschitz with constant C_a at simple orders, where Q̂_a = |q̂′(â)| measures the
gaps, and Hölder with exponent 1/k at a k-fold coincidence.

````

````

### SB.1 (stability): Proposition S5 as previously stated (the tests that Prop. 6.10 refines)

````
### ST.12. Proposition S5 (statement of the two tests)

Source: `theory/stability/proof.md` lines 378-408 (verbatim).

````
**Proposition S5 (certificates, exact arithmetic).**

*Input.* Fix m and componentwise radii ρ_ν ≥ 0. Every data vector with |H̃_ν − H_ν(m)| ≤ ρ_ν
is recovered exactly if either test below succeeds, with all quantities evaluated in
rational arithmetic (`threshold.py`).

*Common part.*

1. |δI| ≤ |L⁻¹|ρ.
2. Bound |δT_k| ≤ (|sech²U| ∗ |δU|)_k + [z^k](tan(U+|δU|) − tan U − sec²U·|δU|). The first
   term is the exact linear part. The second is the coefficientwise majorant of the
   remainder, valid because U ≥ 0.
3. Form the residual bound |r|, the bound |δM|, and A := |M⁻¹||δM|.
4. Certify ρ(A) < 1 by checking that v = (I − A)⁻¹𝟙 > 0.
5. Then |ẽ − e| ≤ E := (I − A)⁻¹|M⁻¹||r|.

*(i) Componentwise test.* For each distinct order a, some radius r ∈ {1/2, 19/40, …, 1/40,
1/100, 1/1000} satisfies

  r^{k_a} ∏_{b≠a}(|a−b| − r)^{k_b} > Σ_j E_j (a + r)^{n−j}.

*(ii) Coherent test.* Write ẽ − e = G·δH + ϱ, where:

- G = (D_I e) L⁻¹ is exact (Lemma S2.1);
- |ϱ| ≤ |M⁻¹||r_rem| + A E, with r_rem the remainder part of r.

On |z − a| = r, bound the first-order part through the exact Taylor coefficients at a of
the polynomials p_c(z) = Σ_j (−1)^j G_{jc} z^{n−j}. The test is

  r^{k_a} ∏(|a−b| − r)^{k_b} > Σ_c ρ_c Σ_l |p_c^{(l)}(a)/l!| r^l + Σ_j |ϱ_j| (a + r)^{n−j}.

````

````

### SB.2 (stability): Proposition 6.10: notation and the explicit formulas (steps 1-3, J)

````
Write $\cI=(R,P_1,P_3,\dots,P_{2n-3})$, indexed $\cI_0=R$ and $\cI_k=P_{2k-1}$, and
$U(z)=\sum_{k=1}^{n-1}P_{2k-1}z^{2k-1}/(2k-1)$; all power series are truncated after $z^{2n-3}$, and
$e_k=0$ for $k>n$. Write $\operatorname{sech}^2U=1-T^2=\sum_ks_kz^k$, $T=\tanh U$.

\begin{enumerate}[label=\arabic*.]
\item Put $\Delta=|\mathbf F^{-1}|\,\delta$, so $|\tilde\cI_k-\cI_k|\le\Delta_k$, and
  $|\delta U|(z)=\sum_{k=1}^{n-1}\Delta_kz^{2k-1}/(2k-1)$.
\item Put
  \[
    \tau^{\rm lin}=|\operatorname{sech}^2U|*|\delta U|,\qquad
    \tau^{\rm rem}=\tan(U+|\delta U|)-\tan U-\sec^2U\cdot|\delta U|,\qquad
    \tau=\tau^{\rm lin}+\tau^{\rm rem},
  \]
  coefficientwise; then $|\tilde T_k-T_k|\le\tau_k$, and the part of $\tilde T_k-T_k$ beyond first order
  in $\delta\cI$ is at most $\tau^{\rm rem}_k$ in absolute value.
\item Put, for $0\le j\le n-2$,
  \[
    \rho_j=\sum_{i=0}^{j}\tau_{2i+1}\,e_{2j-2i},\qquad
    \rho^{\rm rem}_j=\sum_{i=0}^{j}\tau^{\rm rem}_{2i+1}\,e_{2j-2i},
  \]
  and $\rho_{n-1}=\Delta_0e_n$, $\rho^{\rm rem}_{n-1}=0$. Let $\Delta_M$ be the $n\times n$ matrix, rows
  indexed by $0\le j\le n-1$ and columns by the unknowns $e_1,\dots,e_n$, with entry $\tau_{2i+1}$ in
  row $j$, column $e_{2j-2i}$, for $0\le i<j\le n-2$ and $2j-2i\le n$; entry $\Delta_0$ in row $n-1$,
  column $e_n$; and zero elsewhere. Then $|r|\le\rho$, $|r_{\rm rem}|\le\rho^{\rm rem}$ and
  $|\delta M|\le\Delta_M$ entrywise. Put $A=|M^{-1}|\Delta_M$.
\end{enumerate}
Steps 4 and 5 are unchanged, with $\rho$ in place of $|r|$. In test (ii), $|\varrho|\le|M^{-1}|\rho^{\rm rem}+AE$
and $G=-M^{-1}J\,\mathbf F^{-1}$, where $J=\partial(Me-b)/\partial\cI$ at fixed $e$ is
\[
  J_{j,k}=-\frac1{2k-1}\sum_{\substack{k-1\le i\le j\\2j-2i\le n}}e_{2j-2i}\,s_{2i+2-2k}\quad(0\le j\le n-2,\ 1\le k\le n-1),
  \qquad J_{n-1,0}=-e_n,
\]
and $J_{j,0}=0$ for $j\le n-2$, $J_{n-1,k}=0$ for $k\ge1$.
````

### SB.3 (stability): Claim after Table 4

````
%   "Every entry of the $\delta_{\rm cert}$ column can be re-derived from Proposition 6.2 and the
%    formulas above in exact rational arithmetic; for $n\le5$ every series is truncated after $z^7$
%    and has at most four nonzero (odd) coefficients."
````

### SB.4 (stability): Rounding convention and the printed results table (delta_thm, delta_cert, delta_up, eps_cert)

````
### ST.13. Upper bound by construction; rounding convention

Source: `theory/stability/proof.md` lines 413-429 (verbatim).

````
**Upper bound by construction.** For each order a, the search minimises
‖H(q̃) − H(m)‖_∞ over real monic polynomials of two shapes:

- q̃ = (z − c) g(z), with a real root at c = a ± 1/2;
- q̃ = ((z − c)² + y²) g(z), with a complex pair of real part c = a ± 1/2.

The optimiser is numerical. The reported minimiser is rebuilt exactly in rationals, and its
data are evaluated exactly. Its recovery is q̃ itself (Theorem B, checked by an exact solve),
and that q̃ has a root with real part exactly a ± 1/2. At that point rounding is a tie, so
δ_up is an infimum: arbitrarily small further perturbations push the root across, and
recovery fails at every level above δ_up. Hence the true threshold is at most δ_up.

*Rounding of printed values.* δ_thm and δ_cert are printed rounded **down**, and δ_up
rounded **up**, so that each printed number keeps its meaning. An adversarial search found
that the exact test fails at the up-rounded values 2.342e−3 and 1.462e−3, which an earlier
version printed.

````

### ST.14. Results table (printed values to re-certify)

Source: `theory/stability/proof.md` lines 430-446 (verbatim).

````
**Results** (`threshold_output.md`, `threshold_results.json`). The absolute model is
|δH_ν| ≤ δ for all ν. The relative precision listed is δ_cert/|H_ν| for ν = −1, …, n−2, and
ε_cert is the largest uniform relative error |δH_ν| ≤ ε|H_ν| that is certified.

| m | n | δ_thm | δ_cert | δ_up | δ_up/δ_cert | failure built at | δ_cert/|H_ν|, ν = −1..n−2 | ε_cert (uniform relative) |
|---|---|---|---|---|---|---|---|---|
| (2, 8, 8) | 3 | 3.80e-07 | 2.341e-03 | 2.485e-03 | 1.06 | 8−1/2 | 1.8e-02, 1.6e-03, 7.0e-04 | 1.9e-03 |
| (3, 3, 12) | 3 | 1.18e-07 | 4.040e-03 | 4.589e-03 | 1.14 | 3+1/2 | 3.2e-02, 2.8e-03, 7.4e-04 | 4.4e-03 |
| (3, 10, 15, 30) | 4 | 4.02e-11 | 3.660e-03 | 7.488e-03 | 2.05 | 10+1/2 | 4.9e-03, 8.0e-04, 4.1e-05, 3.6e-07 | 8.7e-04 |
| (4, 5, 21, 28) | 4 | 3.14e-11 | 1.461e-03 | 2.018e-03 | 1.38 | 5−1/2 | 1.9e-03, 3.2e-04, 1.6e-05, 1.7e-07 | 4.6e-04 |
| (2, 3, 7) | 3 | 4.49e-07 | 3.658e-03 | 6.587e-03 | 1.80 | 3−1/2 | 3.0e-01, 4.0e-03, 2.7e-03 | 5.0e-03 |
| (4, 4, 4) | 3 | 9.35e-07 | 4.539e-04 | 5.036e-04 | 1.11 | 4+1/2 | 3.6e-03, 5.0e-04, 5.4e-04 | 8.2e-04 |
| (7, 7, 7) | 3 | 9.97e-08 | 8.068e-05 | 8.273e-05 | 1.03 | 7−1/2 | 2.8e-04, 4.9e-05, 2.3e-05 | 1.2e-04 |
| (3, 3, 4, 4) | 4 | 1.48e-09 | 9.597e-05 | 1.195e-04 | 1.24 | 4−1/2 | 2.3e-04, 1.0e-04, 1.1e-04, 7.2e-05 | 1.1e-04 |
| (5, 5, 5, 5) | 4 | 4.74e-10 | 3.617e-05 | 3.826e-05 | 1.06 | 5−1/2 | 6.0e-05, 2.5e-05, 1.9e-05, 6.2e-06 | 3.1e-05 |
| (2, 2, 2, 3) | 4 | 2.03e-09 | 1.858e-04 | 2.520e-04 | 1.36 | 3−1/2 | 2.2e-03, 3.2e-04, 5.6e-04, 7.7e-04 | 4.3e-04 |
| (2, 2, 2, 2, 3) | 5 | 2.72e-12 | 7.908e-06 | 5.743e-05 | 7.26 | 2+1/2 | 2.3e-05, 1.2e-05, 2.1e-05, 2.9e-05, 1.9e-05 | 1.4e-05 |
````
````

### TH.1 (threshold-sharpness): Theorem 5.13 (the threshold) and the computational Proposition (collision-free sums)

````
\begin{theorem}[The threshold]\label{thm:threshold}
If $p+q+r\le17$, the first two heat invariants determine the hyperbolic triangle orbifold
$\Orb(p,q,r)$ among all hyperbolic triangle orbifolds: $\Kiso(\Orb(p,q,r);\Pill_3)\le2$. The bound
$17$ is sharp: the first failure occurs at cone-order sum $18$ (Theorem~\ref{thm:minimal}).
\end{theorem}

\begin{proposition}[Collision-free sums; computational]\label{prop:collisionfree}
Among the sums $18\le S\le4800$, exactly the $38$ sums
\[
\begin{gathered}
  19,\,21\text{--}25,\,27\text{--}30,\,33,\,41,\,44,\,46\text{--}51,\,59,\,65,\,67,\,81,\,99,\\
  115,\,119,\,123,\,125,\,173,\,199,\,203,\,223,\,235,\,243,\,251,\,307,\,329,\,557
\end{gathered}
\]
carry no collision, that is, no two hyperbolic triads of sum $S$ have the same reciprocal sum.
\end{proposition}
````

### TH.2 (threshold-sharpness): Sharpness wording (abstract, Theorem 1.4, after Theorem 6.6)

````
Recovering the orders from approximate coefficients is Lipschitz at simple orders and H\"older of
exponent $1/k$ at $k$-fold orders; the exponent $1/k$ is sharp for arbitrary data, while for the
coefficients of real orders it is $1/2$ when all the orders are equal.

The exponent $1/k_a$ cannot be improved for arbitrary data. For data that are the heat invariants
of real orders it is $\frac12$, and sharp, at a double order, and at an order of any multiplicity
$k=n\ge3$, that is, when all the orders are equal.

Recovery is Lipschitz at simple orders and H\"older of exponent $1/k$ at a $k$-fold coincidence.
The exponent $1/k$ is sharp for arbitrary data (Proposition~\ref{prop:sharpexp}(ii)); for data
coming from real orders it is $\frac12$ at a double order (Proposition~\ref{prop:sharpexp}(i)) and when all
the orders are equal (Remark~\ref{rem:triple}); other configurations are not settled
(Figure~\ref{fig:F8}).
````

### TH.3 (threshold-sharpness): Remark 6.8 addition and the real-multiset restriction

````
%   "The argument applies verbatim to $(a,\dots,a)$ with any $n\ge3$ entries. The family
%    $(a+s,a-s,a,\dots,a)$, with $\delta P_1=0$, $\delta P_3=6as^2$ and all other data changes $O(s^2)$,
%    shows that $\frac12$ is attained."

[COMPOSED from item (5) of the fragment. For k >= 3 the witnesses q_s of Proposition 6.7(ii), whose roots are a + s e^{2 pi i j/k}, are not all real, and their data are not the heat invariants of any real multiset.]
````

### LIT.0 (literature): The attribution claims (composed table, see below)

````
(generated data: see `statements/literature.md`, item LIT.0)
````
