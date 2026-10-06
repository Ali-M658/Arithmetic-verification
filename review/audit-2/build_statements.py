#!/usr/bin/env python3
"""Build review/audit-2/STATEMENTS.md and review/audit-2/statements/<group>.md.

Every audited result is copied verbatim, by line range, from its source file. Statements
only, no proofs: each excerpt must contain its anchor string in its first line, must not contain
a proof marker, and the script exits nonzero otherwise. Items marked COMPOSED are assembled from
verbatim excerpts plus connective text written here; the connective text is in [square brackets].
Witness data are generated from the claimed-data files (theory/pte/data) as claims, with the
construction recipes and the configuration Z omitted.

Run from the repository root:  python3 review/audit-2/build_statements.py
"""
from __future__ import annotations

import json
import sys
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "review/audit-2/STATEMENTS.md"
GDIR = ROOT / "review/audit-2/statements"

PRF = "theory/pte/proof.md"
STX = "theory/pte/statements.tex"
REV = "theory/revision"
L25 = f"{REV}/lemma25.tex"
R412 = f"{REV}/remark412.tex"
T12 = f"{REV}/thm12iii.tex"
DES = f"{REV}/descent.tex"
P3P = f"{REV}/point3P.tex"
P610 = f"{REV}/prop610.tex"
T513 = f"{REV}/thm513.tex"
SHP = f"{REV}/sharpness.tex"
A1 = "review/audit/statements"
STB = f"{A1}/stability.md"
DIO = f"{A1}/diophantine.md"

PROOF_MARKERS = ("*Proof", "\\begin{proof}", "Proof.", "\\emph{The model", "\\emph{Rank", "\\emph{Torsion",
                 "Sketch", "\\begin{proof}[")

# Each item: (id, title, kind, parts). kind "V" = verbatim parts [(file, a, b, anchor)], with
# "text" parts as ("T", string).
# parts is a list of ("L", file, a, b, anchor) or ("T", text).

L = lambda f, a, b, anchor: ("L", f, a, b, anchor)  # noqa: E731
T = lambda s: ("T", s)  # noqa: E731

GROUPS: dict[str, dict] = {}

GROUPS["pte-structure"] = {
    "title": "PTE structure: the dictionary, the Descartes bound, balanced constructions, the pencil, the shift",
    "context": [f"{A1}/signatures.md  (the previously audited results [Sig]: Lemma 1-4, Theorem S, Lemma 5 is "
                "quoted below as an input; definitions DF.1 of signature and heat coefficient)"],
    "inputs": [
        "[Sig] Lemma 4 and Theorem S (previously audited, in signatures.md SG.4, SG.5): the reduction of "
        "'two orbifolds share their first L heat coefficients' to an L-configuration, and |Z| even and >= 2L+2.",
        "[Sig] Lemma 2 (SG.2): the (L+1)-st coefficient agrees iff P_{2L-1}(U)=P_{2L-1}(V).",
        "[Sig] Lemma 5: a multiset of size <= 2L-2 with vanishing odd power sums up to 2L-3 is symmetric "
        "(odd elementary symmetric functions vanish). Re-prove it if you use it.",
        "[Sig] (4.3) and Corollary S2 (SG.7): the area bound Area/pi <= ... used by Lemma 1.2(5).",
    ],
    "items": [
        ("PS.0", "Setting, Definition 1.1, Lemma 1.2 (dictionary)", [L(PRF, 49, 85, "## 1. Setting")]),
        ("PS.1", "Theorem 2.1 (Descartes bound)", [L(PRF, 141, 147, "**Theorem 2.1")]),
        ("PS.2", "Proposition 2.2 (PTE lower bound)", [L(PRF, 174, 175, "**Proposition 2.2")]),
        ("PS.3", "Proposition 2.3 (symmetric constructions are balanced)", [L(PRF, 184, 194, "**Proposition 2.3")]),
        ("PS.4", "Theorem 3.1 (pencil)", [L(PRF, 223, 233, "**Theorem 3.1")]),
        ("PS.5", "Proposition 3.2 (shift)", [L(PRF, 267, 274, "**Proposition 3.2")]),
        ("PS.6", "Manuscript-facing versions (statements.tex)", [
            L(STX, 13, 37, "\\subsection{How many coefficients"),
            L(STX, 47, 53, "\\begin{proposition}[Symmetric constructions"),
        ]),
    ],
}

GROUPS["pte-growth"] = {
    "title": "PTE growth: N_odd, the doubling, the upper bounds, the square-root lower bound, f(A) versus N(k)",
    "context": [f"{A1}/signatures.md  (the previously audited results [Sig]: definitions DF.1; Corollary S2 "
                "and Theorem T1 give f(A) <= floor(A/pi)+4; SG.7, SG.8)"],
    "inputs": [
        "[Sig] Corollary S2 / Theorem T1: f(A) <= floor(A/pi)+4 and the bound |U|+|V| <= 2 floor(A/pi)+8 "
        "(used for Theorem 4.2(a)). Previously audited; verify the use made of it.",
        "Borwein-Ingalls 1994, Props. 2, 3 (cited): N(k) >= k+1 and N(k) <= k(k+1)/2+1. "
        "Re-prove the upper bound yourself (pigeonhole) if you use it.",
        "Lemma 1.2 (PS.0 in pte-structure.md) and Proposition 3.2 (PS.5) are stated below by reference "
        "to the other group; they are NOT yours to audit, but you may assume them as stated, and must say so.",
    ],
    "items": [
        ("PG.0", "Definitions 1.3, 1.4, PTE notation and Lemma 1.5", [L(PRF, 99, 124, "**Definition 1.3.**")]),
        ("PG.1", "Proposition 3.3 (doubling)", [L(PRF, 283, 293, "**Proposition 3.3")]),
        ("PG.2", "Theorem 3.4 (upper bounds)", [L(PRF, 311, 314, "**Theorem 3.4")]),
        ("PG.3", "Theorem 4.1 (square-root lower bound)", [L(PRF, 329, 332, "**Theorem 4.1")]),
        ("PG.4", "Theorem 4.2 (the exponent of f is a PTE exponent)", [L(PRF, 342, 350, "**Theorem 4.2")]),
        ("PG.5", "Theorem 4.3 (genus alone, cone count alone)", [L(PRF, 380, 390, "**Theorem 4.3")]),
        ("PG.6", "Manuscript-facing version (statements.tex): Theorem (Growth) and Theorem (Descartes)", [
            L(STX, 55, 70, "\\begin{theorem}[Growth]"),
        ]),
    ],
}

GROUPS["pte-witnesses"] = {
    "title": "PTE witnesses: the explicit pairs of section 5, the 61 pencil witnesses, the T_3 search claim",
    "context": [f"{A1}/signatures.md  (definitions DF.1: signature and heat coefficients; Lemma 2, 4, Theorem S)",
                f"{A1}/audibility.md  (Theorem A, Theorem C(3): what 'integer sharpness' means; items AU.1)"],
    "inputs": [
        "Heat coefficients: use the definition in signatures.md DF.1 with the cone polynomials of "
        "Proposition heatinput in trace-formula.md (b_l(m) = (-1)^l p_l(m)/m, p_l from the closed form), or "
        "re-derive them from Ucar (arXiv:1711.03405, (4.25),(4.33)). Compute 'the number of shared "
        "coefficients' from the coefficients themselves, not from the P_j criterion alone, and also check it "
        "against the criterion.",
        "Borwein-Ingalls/BLP/Chen/CMSV solutions are inputs only as numbers: re-verify every such number "
        "exactly before using it. Their provenance belongs to the literature group.",
    ],
    "items": [
        ("PW.0", "Headline table (proof.md section 0, items 5 and 6)", [L(PRF, 32, 47, "5. **Explicit witnesses")]),
        ("PW.1", "Example (Small pairs) and Remark (first open case), as in statements.tex", [
            L(STX, 101, 120, "\\begin{example}[Small pairs]"),
            L(STX, 122, 127, "\\begin{remark}[The first open case]"),
        ]),
        ("PW.2", "Improved lower bounds on f in the covered range", [L(PRF, 457, 470, "**Improved lower bounds")]),
        ("PW.3", "Integer sharpness witnesses for Theorem A at n=4, and the n=5 claim", [L(PRF, 253, 265, "*Instances.*")]),
        ("PW.4", "The 18 claimed pairs (generated; recipes and Z omitted)", [("GEN", "witnesses")]),
        ("PW.5", "The 61 claimed pencil configurations (generated)", [("GEN", "pencil61")]),
    ],
}

GROUPS["trace-formula"] = {
    "title": "Trace formula: the closed form of the elliptic weight, Lemma 2.5 for every order, agreement with Ucar, "
             "Remark 4.12, the constant of Theorem 1.2(iii)",
    "context": [f"{A1}/locality.md  (LO.6 Theorem 3.1 = the integrated trace formula with elliptic terms, "
                "LO.7, LO.8 admissibility and counting; DF.1 definitions of the heat coefficients and signature). "
                "These are previously audited; a result below may use them as stated. "
                "Hypotheses of the trace formula are an external input: read Dryden-Strohmaier eq. (1) in the fetched text."],
    "inputs": [
        "Selberg trace formula for cocompact Fuchsian groups with elliptic elements, in the form of "
        "Dryden-Strohmaier arXiv:math/0504571 eq. (1) (fetched: sources/ds_math0504571.txt).",
        "Ucar, arXiv:1711.03405, (4.25), (4.33)-(4.35) (fetched: sources/ucar_1711.03405.txt).",
        "Dryden-Gordon-Greenwald-Webb arXiv:0805.3148, Thm 4.8, section 5.6 (fetched: sources/dggw_0805.3148.txt). "
        "Schueth arXiv:1812.06119, Rem. 4.2, Thm 4.1 (fetched: sources/schueth_1812.06119.txt).",
        "Classical analysis only otherwise: Euler's beta integral, Bernoulli numbers, Liouville's theorem.",
    ],
    "items": [
        ("TF.1", "Notation for the elliptic moments, and Lemma (Elliptic moments)", [
            L(L25, 16, 26, "\\subsection{The expansion}"), L(L25, 28, 39, "\\begin{lemma}[Elliptic moments]")]),
        ("TF.2", "Definition of Phi_m and Lemma (Closed form)", [
            L(L25, 50, 55, "Write $\\theta_j"), L(L25, 57, 67, "\\begin{lemma}[Closed form]")]),
        ("TF.3", "Lemma (The hyperbolic term is small)", [L(L25, 87, 93, "\\begin{lemma}[The hyperbolic term")]),
        ("TF.4", "Proposition (The heat expansion at curvature -1)", [
            L(L25, 101, 119, "\\begin{proposition}[The heat expansion")]),
        ("TF.5", "Lemma (Cone polynomials) = Lemma 2.5, and the printed first values", [
            L(L25, 145, 152, "\\begin{lemma}[Cone polynomials]"),
            L(L25, 166, 173, "The first values are")]),
        ("TF.6", "Remark (Agreement with Ucar), the claim", [
            L(L25, 175, 175, "\\begin{remark}[Agreement with U"),
            T("[derivation of the identity m t^2 Phi_m(it/2) = ... omitted]"),
            L(L25, 179, 187, "where, by")]),
        ("TF.7", "Remark 4.12 (the trace-formula proof of locality): the independence claim, versions 2A and 2B and the "
                 "replacement sentence", [
            L(R412, 17, 20, "No local invariant can see the moduli"),
            L(R412, 22, 25, "% (1A) if lemma25.tex"),
            L(R412, 32, 45, "\\begin{remark}[The trace-formula proof"),
            L(R412, 49, 61, "\\begin{remark}[The trace-formula proof")]),
        ("TF.8", "Theorem 1.2(iii): the constant and the 'attained' statement; Theorem 4.9(b) form", [
            L(T12, 10, 23, "\\item Let $\\Orb_1,\\Orb_2$ have the same signature"),
            L(T12, 31, 36, "%   For $0<t\\le")]),
    ],
}

GROUPS["descent"] = {
    "title": "Descent: the 2-isogeny descent on C_{27/2}, its torsion, and the coordinates of 3P on C_{155/12}",
    "context": [f"{DIO}  (the curves C_Lambda: the cubic Lambda-fibre of the pair (S_1,R) in the Diophantine section; "
                "the claim DI.7 that the base pair is isolated; DI.6 where 3P is printed). Read DI.* for the definition "
                "of the plane cubics C_Lambda, S_1, R, hyperbolic triads; do not read any other file of theory/diophantine."],
    "inputs": [
        "Cremona, Algorithms for Modular Elliptic Curves, 2nd ed., section 3.6 (descent via 2-isogeny, "
        "(3.6.2)) and section 3.3 (torsion injectivity) (fetched: sources/cremona_ch3.txt). "
        "State exactly what you take from it; re-derive any formula you can.",
    ],
    "items": [
        ("DE.0", "The claimed isomorphism and its inverse", [
            T("[COMPOSED. C_{27/2} is the plane cubic of the Diophantine section with Lambda = 27/2 (see context). "
              "Claim: with e_2 = XY+YZ+ZX the maps below are mutually inverse isomorphisms over Q between "
              "C_{27/2} and the elliptic curve E, sending the origin of E to O = (1:-1:0).]"),
            L(DES, 23, 24, "\\varphi(X:Y:Z)"),
            L(DES, 28, 28, "E:\\ y^2=x(x+9)(x+384)")]),
        ("DE.1", "The rank claim", [
            T("[COMPOSED from the proof's claims. With E': y^2 = x(x^2 + c'x + d'), c' = -786, d' = 140625 the 2-isogenous "
              "curve of E (c = 393, d = 3456): the two 2-isogeny Selmer-type groups are {+-1, +-6} (order 4) for E and {1} "
              "for E'; rank E(Q) = 0, with no Sha ambiguity.]")]),
        ("DE.2", "The torsion claim", [
            T("[COMPOSED.] E(Q) = E(Q)_tors is isomorphic to Z/2 x Z/6, and consists of the twelve points"),
            L(DES, 78, 79, "O,\\ (0,0)"),
            T("[with (0,0), (-9,0), (-384,0) of order 2, (16,+-400) of order 3, and (-24,+-360), (-144,+-2160), "
              "(216,+-5400) of order 6. The proof reduces E modulo 7 and 11 and counts #E(F_7) = #E(F_11) = 12.]")]),
        ("DE.3", "The twelve rational points of C_{27/2}", [L(DES, 84, 87, "\\emph{The points of")]),
        ("DE.4", "Consequence for triads", [L(DES, 89, 91, "A triad with $S_1=18k$")]),
        ("DE.5", "Theorem 5.16 (isolation) as in the manuscript (statement unchanged)", [
            L(DIO, 176, 188, "**What does *not* adapt")]),
        ("DE.6", "The coordinates of 3P", [
            T("[COMPOSED. C_{155/12} is the cubic C_Lambda with Lambda = 155/12; the group law is the chord-tangent law "
              "with base point O = (1:-1:0). Claim:]"),
            L(P3P, 6, 7, "% With base point O = (1:-1:0)"),
            T("[The manuscript previously printed 3P = (162833463 : 287876366 : 723926268); the corrected claim is "
              "3P = (162833463 : 723926268 : 287876366).]")]),
    ],
}

GROUPS["stability"] = {
    "title": "Stability: Proposition 6.10 (explicit remainder formulas) and re-certification of every printed delta",
    "context": [f"{STB}  (ST.0 setting and recovery map, ST.12 Proposition S5, ST.13, ST.14 the printed results table). "
                "Everything you need for the setting and the printed values is in the verbatim excerpts below."],
    "inputs": [
        "None external. The only task-specific facts are the notation and formulas of the excerpts. "
        "Exact rational arithmetic only (fractions.Fraction or sympy). Floating point is not a certificate."],
    "items": [
        ("SB.0", "Setting and recovery map (previously audited)", [L(STB, 30, 67, "### ST.0")]),
        ("SB.0b", "Front-end tables, Lemmas S2, Theorem S2, Lemma S3 and Theorem S3 (previously audited; define delta_thm)",
         [L(STB, 86, 254, "### ST.2")]),
        ("SB.1", "Proposition S5 as previously stated (the tests that Prop. 6.10 refines)", [L(STB, 313, 350, "### ST.12")]),
        ("SB.2", "Proposition 6.10: notation and the explicit formulas (steps 1-3, J)", [
            L(P610, 14, 16, "Write $\\cI=(R,P_1"),
            L(P610, 20, 48, "\\begin{enumerate}[label=\\arabic*.]")]),
        ("SB.3", "Claim after Table 4", [L(P610, 63, 65, "%   \"Every entry of the")]),
        ("SB.4", "Rounding convention and the printed results table (delta_thm, delta_cert, delta_up, eps_cert)", [
            L(STB, 351, 397, "### ST.13")]),
    ],
}

GROUPS["threshold-sharpness"] = {
    "title": "Threshold and sharpness: Theorem 5.13 and the 38 collision-free sums; the sharpness wording of Theorem 1.4",
    "context": [f"{A1}/threshold.md  (the previously audited threshold results: separation theorem, minimal degeneracy 18, Prop 3)",
                f"{STB}  (ST.0-ST.11: the stability results the sharpness wording refers to: Theorem S3, Proposition S3.2, "
                "Remark S3.3, Theorem S4)"],
    "inputs": ["None external. Exact arithmetic (integers, Fractions)."],
    "items": [
        ("TH.1", "Theorem 5.13 (the threshold) and the computational Proposition (collision-free sums)", [
            L(T513, 11, 15, "\\begin{theorem}[The threshold]"),
            L(T513, 24, 33, "\\begin{proposition}[Collision-free sums")]),
        ("TH.2", "Sharpness wording (abstract, Theorem 1.4, after Theorem 6.6)", [
            L(SHP, 21, 23, "Recovering the orders from approximate"),
            L(SHP, 26, 28, "The exponent $1/k_a$ cannot be improved"),
            L(SHP, 40, 44, "Recovery is Lipschitz at simple orders")]),
        ("TH.3", "Remark 6.8 addition and the real-multiset restriction", [
            L(SHP, 57, 59, "The argument applies verbatim"),
            T("[COMPOSED from item (5) of the fragment. For k >= 3 the witnesses q_s of Proposition 6.7(ii), whose roots "
              "are a + s e^{2 pi i j/k}, are not all real, and their data are not the heat invariants of any real multiset.]")]),
    ],
}

GROUPS["literature"] = {
    "title": "Literature: every attribution a PTE theorem depends on",
    "context": [],
    "inputs": [
        "Fetched sources are in review/audit-2/sources/ (run fetch_sources.sh; unreachable files are instrument gaps). "
        "You may also read the raw fetched source files of theory/pte/sources/ (the *.pdf, *.txt, *.htm files listed in "
        "theory/pte/sources/SHA256SUMS) but NOT theory/pte/sources/NOTES.md, theory/pte/LITERATURE.md or any other file "
        "of theory/pte. Where the same document exists in both places, check the hashes agree or note that they do not.",
        "Borwein-Ingalls (e-periodica, L'Enseignement Math. 40 (1994) 3-27), Borwein-Lisonek-Percival (Math. Comp. 72), "
        "Melzak (Canad. Math. Bull. 4 (1961)), Wooley and Chen's web pages must be re-fetched by you or copied from "
        "theory/pte/sources with a hash check; record every HTTP result. No browser.",
    ],
    "items": [("LIT.0", "The attribution claims (composed table, see below)", [("GEN", "literature")])],
}

LITERATURE_CLAIMS = """\
Each claim says: *a statement S is made by source X at the stated place*. Verify S against the fetched text of X:
exact wording, exact hypotheses (degree versus size, k versus k+1, integers versus rationals, 'ideal' versus
'symmetric'), exact place (page, proposition, entry number). Grade each claim CONFIRMED / CONFIRMED WITH CORRECTION
(give the correction) / NOT FOUND / CONTRADICTED / SOURCE UNREACHABLE. A claim that is a *negative* statement
(for instance 'no bound o(k^2) is known') is graded against the most recent sources you can fetch.

Notation used by the paper: [A] =_k [B] means two distinct multisets of integers of a common size n with equal power sums
P_j for j = 1..k. N(k) is the least such n. A solution is ideal if n = k+1. Degree k, size n.

Where a PTE theorem of the paper uses the claim is given in brackets.

**Borwein-Ingalls, 'The Prouhet-Tarry-Escott problem revisited', L'Enseignement Math. (2) 40 (1994) 3-27**
- B1. Defines N(k) as the least size of a solution of degree k (p. 6) [all of section 4].
- B2. Proposition 1 of that paper [state what it says; the paper cites 'Props. 1-3'].
- B3. Proposition 2: N(k) >= k+1 [Lemma 1.5(3), Theorem 4.2].
- B4. Proposition 3: N(k) <= k(k+1)/2 + 1, proved by pigeonhole [Lemma 1.5(2), Theorem 3.4, Theorem 4.2(b)].
- B5. p. 7: the bounds of Wright [22] and Melzak [15] are 'slightly stronger' and only improve to
  N(k) <= (k^2-3)/2 for k odd and N(k) <= (k^2-4)/2 for k even [remark after Theorem 4.2].
- B6. p. 7: Hua's bound M(k) <= (k+1)(log((k+2)/2)/log(1+1/k) + 1) ~ k^2 log k concerns the exact-degree quantity M(k)
  (degree exactly k), of order k^2 log k [context only].
- B7. Section 6, problem 3: 'Prove N(k) <= o(k^2)' is listed as open, and the paper says no progress has been made
  'for many years'; also 'The big prize is to find ideal solutions of all degrees' [Theorem 4.2 and the Remark on exponents].
- B8. p. 8: the definition of an odd symmetric solution: sum alpha_i^j = 0 for j = 1,3,5,...,k-1 (with B = -A)
  [Proposition 2.3(a) uses 'odd ideal symmetric solution of size 2L-1'].
- B9. p. 6, Lemma 2: the Prouhet step [A]=_k[B] implies [A, B+M] =_{k+1} [A+M, B] [context].
- B10. p. 9 table and p. 25: the explicit symmetric ideal solutions: size 4 {+-3,+-11}/{+-7,+-9}; size 6 {+-4,+-9,+-13}/{+-1,+-11,+-12};
  size 8 {+-2,+-16,+-21,+-25}/{+-5,+-14,+-23,+-24}; the perfect 7-set {-51,-33,-24,7,13,38,50} (and four more); Letac's two 9-sets
  {-98,-82,-58,-34,13,16,69,75,99} and {-169,-161,-119,-63,8,50,132,148,174}; Letac's size-10 solution [witnesses, L=4,5].
- B11. p. 4: Prouhet's 1851 general solution ('n^{k+1} numbers separable into n sets') and Wright's 1959 account [context].
- B12. Proposition 4: rational points of x^2 y^2 - 13 x^2 - 13 y^2 + 121 = 0 give size-10 ideal symmetric solutions (Smyth) [context].

**Melzak, 'A note on the Tarry-Escott problem', Canad. Math. Bull. 4 (1961) 233-237**
- M1. Records Wright's bound K(n) <= (n^2+4)/2 as the best bound known so far (pp. 233-234); state what n and K(n) mean there and
  whether this is the same bound as B5 (translate degree/size conventions carefully).
- M2. Table 1 (p. 237) gives individual numerical upper bounds for n <= 29; no asymptotic improvement.

**Wooley**
- W1. Ann. of Math. 175 (2012) 1575-1627 ('Vinogradov's mean value theorem via efficient congruencing'), Theorem 1.3: W(k,h) <= k^2 + k - 2 (the hypotheses on h).
- W2. Proc. LMS 118 (2019) 942-1016 ('Nested efficient congruencing and relatives of Vinogradov's mean value theorem'), Theorem 13.1:
  W(k,h) <= k(k+1)/2 + 1. State what W(k,h) is and whether W(k,2) is N(k) or the exact-degree M(k).

**Croot-Mao-Yip, arXiv:2609.05061** (p. 1)
- C1. 'Using a pigeonhole principle argument one can easily see that P(k,m) <= k(k+1)/2+1', with P(k,2) = N(k).
- C2. 'It is an open problem to determine if P(k,2) = k+1; it is only known that P(k,2) = k+1 when 2 <= k <= 9 and k = 11.'
- C3. The paper names no bound on N(k) better than quadratic [the most recent source the paper cites].

**Coppersmith-Mossinghoff-Scheinerman-VanderKam (CMSV), arXiv:2304.11254, Math. Comp. 93 (2024) 2473-2501**
- D1. p. 2: 'Ideal solutions in the PTE problem over Z are known for n <= 10 and n = 12' (n is the size); size 11 is open.
- D2. 'No new integral solutions are found for 9 <= n <= 16' [searches].
- D3. The size-12 solution of Kuosa-Meyrignac-Chen (1999), +-{22,61,86,127,140,151} / +-{35,47,94,121,146,148} (CMSV (5)); Letac's two 9-sets (CMSV (3)).
- D4. Consistency: D1 and C2 describe the same set of ideal solutions (size n <-> degree k = n-1).

**Borwein-Lisonek-Percival, 'Computational investigations of the PTE problem', Math. Comp. 72 (2003) 2063-2070**
- P1. p. 2063: 'Parametric ideal solutions are known for n = 1,...,8 and n = 10'.
- P2. p. 2064: Gloden's two-parameter family of size 7; p. 2069: Letac's 9-sets and two further size-10 solutions
  +-{71,131,180,307,308}/+-{99,100,188,301,313} and +-{18,245,331,471,508}/+-{103,189,366,452,515}.

**Chen Shuwen, 'A survey of the Prouhet-Tarry-Escott problem and its generalizations', arXiv:2506.11429 (2025), and eslpower.org**
- S1. Appendix A.1.6, A.1.17, A.1.26, A.1.33 (equal sums of odd powers, exponents 1,3,...,2L-3 for L = 3,4,5,6):
  [1,5,5]=[2,3,6]; [1,13,17,23]=[3,9,21,21]; [3,19,37,51,53]=[9,11,43,45,55]; [7,91,173,269,289,323]=[29,59,193,247,311,313].
  Check that each entry number is the one that lists exactly this solution, its exponent set, and the stated attributions
  (A.48 'smallest solution by computer search' for [1,5,5]=[2,3,6]; Moessner 1939; Gloden; Xeroudakes-Moessner; Lander;
  Choudhry; Chen 2000 = A.313; Wroblewski 2009 = A.314-A.316, three further non-negative solutions and one with a negative entry).
- S2. eslpower.org, Theorem 3 (page TarryPrb.htm): if [a_1..a_m] = [b_1..b_m] for k = 1,3,...,2n-1 then
  [T+a_i, T-b_i] = [T+b_i, T-a_i] for k = 1,2,...,2n [Proposition 2.2 is attributed to this lifting].
- S3. Negative exponents (survey section 1.4 and Appendix A.5): '33 distinct types with k_1 < 0 and k_n > 0'; type (-1,1): [4,10,12]=[5,6,15];
  type (-1,1,3): [3,10,15,30]=[4,5,21,28] (A.685); type (-1,1,5): [81,374,585,891]=[85,286,702,858].
- S4. The type (-1,1,3,...,2L-3) for L >= 4 does not appear in the survey, and neither does an unequal-size version [negative claim; the paper
  says its system is 'not tabulated'].
- S5. Non-symmetric ideal solutions have been discovered only for degrees n <= 7 (survey p. 13) [context].
- S6. A.1.21, A.1.35: Chernick's two-parameter symmetric families of sizes 5 and 7 [context].

**Others**
- O1. Caley (arXiv:1011.1262, p. 2): the k log k statement concerns the 'easier Waring' number v(k), not N(k) [so it is not a bound on N(k)].
- O2. Choudhry (arXiv:2207.12726, 2022): polynomial parametrisations are counted 'only when k <= 7'; and BLP's 'parametric' (P1) means something
  different [context].
- O3. Prouhet-Thue-Morse: nothing to check beyond B11.
- O4. The statement 'No retrieved source contains an O(k log k) bound for N(k)': search the fetched texts and the web (arXiv listing, Semantic Scholar)
  for any bound N(k) = o(k^2) published after 1994 and report what you find. This is the adversarial search for the 'open problem' claim:
  a single counterexample makes Theorem 4.2's commentary and Remark (What the exponent means) wrong.
"""


def read_lines(path: str) -> list[str]:
    return (ROOT / path).read_text(encoding="utf-8").splitlines()


def excerpt(f: str, a: int, b: int, anchor: str) -> str:
    lines = read_lines(f)
    assert 1 <= a <= b <= len(lines), (f, a, b, len(lines))
    seg = lines[a - 1:b]
    assert anchor in seg[0] or anchor in "\n".join(seg[:2]), f"anchor {anchor!r} not in first lines of {f}:{a}-{b}: {seg[0]!r}"
    text = "\n".join(seg)
    for m in PROOF_MARKERS:
        assert m not in text, f"proof marker {m!r} in {f}:{a}-{b}"
    return text


def gen_witnesses() -> str:
    data = json.loads((ROOT / "theory/pte/data/witnesses.json").read_text())
    out = [
        "Each entry is a claim: the two orbifolds below are closed orientable hyperbolic 2-orbifolds of the signature shown "
        "(cone orders; 'g' genus), they have equal area, distinct signatures, and they share EXACTLY L heat coefficients "
        "(the first L coefficients agree, the (L+1)-st differs). 'T' is the claimed size of the cancelled configuration "
        "Z = U* + (-V*), 'cone counts' the numbers of cone points (1s removed). The claimed exact area/2pi is given.\n",
    ]
    for i, w in enumerate(data):
        out.append(f"**W{i:02d}** kind={w['kind']}, L={w['L']}, claimed shares exactly {w['shares_exactly']}, "
                   f"T={w['T']}, iota={w['iota']}, cone counts {w['cone_counts'][0]} vs {w['cone_counts'][1]}, "
                   f"Area/2pi = {w['area_over_2pi']}")
        out.append(f"- O  = (g={w['sig1']['g']}; {', '.join(map(str, w['sig1']['orders']))})")
        out.append(f"- O' = (g={w['sig2']['g']}; {', '.join(map(str, w['sig2']['orders']))})")
        out.append("")
    return "\n".join(out)


def gen_pencil61() -> str:
    d = json.loads((ROOT / "theory/pte/data/pencil_m4_N220.json").read_text())
    m4 = d["m4"]
    assert len(m4) == 61, len(m4)
    out = [
        "Claim (n = 4 integer sharpness of Theorem A; see Theorem C(3) in audibility.md AU.1). Below are 61 integer 8-element "
        "multisets Z. The claim is that each Z has: no pair {z,-z}; sum z^j = 0 for j = 1, 3 and j = -1; exactly four positive and "
        "four negative entries (imbalance 0); so m = positive part and m' = (-negative part) are two DISTINCT 4-multisets of "
        "positive integers with equal R = sum 1/m_i, P_1 and P_3, i.e. two orbifolds of genus 0 with four cone points sharing "
        "I_3 = (R, P_1, P_3); the 61 are pairwise distinct modulo Z -> lambda Z (lambda rational) and Z -> -Z (which swaps m, m'); and "
        "they are ALL the configurations produced as follows: A, B primitive integer 4-sets {a,b,c,-(a+b+c)} with all entries of "
        "absolute value <= 220, A and B with equal e_3^4/e_4^3 (e_k elementary symmetric), B scaled by the rational lambda with "
        "e_3(lambda B) = e_3(A), e_4(lambda B) = e_4(A), lambda B != A as multisets, then Z = A + (-lambda B) after cancelling, "
        "scaled to primitive integers. (The first claim is checkable on the list; the 'all' claim needs your own enumeration.)\n",
        "```",
    ]
    for z in m4:
        out.append(str(z))
    out.append("```")
    out.append("")
    out.append("Further claim: with m = 5 (odd symmetric 5-sets {e_1 = e_3 = 0}, primitive, entries <= 200; there are 1,592 of them), "
               "no two have equal e_4^5/e_5^4 giving a pencil pair, i.e. no integer sharpness witness of Theorem A at n = 5 arises this way.")
    return "\n".join(out)


def gen_literature() -> str:
    return LITERATURE_CLAIMS


GEN = {"witnesses": gen_witnesses, "pencil61": gen_pencil61, "literature": gen_literature}

HEADER = """\
# G5-bis audit: statements under review, group `{g}`

{title}

Every result below is copied verbatim, by line range, from its source file (`review/audit-2/build_statements.py`
asserts the anchors and that no proof text is included). Items marked COMPOSED combine verbatim excerpts with
connective text in [square brackets]. **Proofs, scripts and data of the sessions that produced these results are
deliberately withheld.** You must not open any file of `theory/pte/`, `theory/revision/`, `theory/signatures/`
(other than where stated below), `review/referee-sim/` or `paper/` (the manuscript contains proofs of some of these
results). If you do open one by accident, say so in your REVIEW.md under 'contamination'.

"""

RULES = """
## Context files you may read (previously audited statements, no proofs)

{ctx}

## External inputs

{inp}

## Fetched sources

Texts fetched headlessly by `review/audit-2/fetch_sources.sh` are in `review/audit-2/sources/` (not committed).
Never quote a source from memory: quote the fetched text, with page or section. An unreachable source is an
instrument gap, to be logged, not a confirmation.

"""


def build_group(g: str, spec: dict) -> str:
    parts = [HEADER.format(g=g, title=spec["title"])]
    ctx = "\n".join(f"- {c}" for c in spec["context"]) or "- (none)"
    inp = "\n".join(f"- {c}" for c in spec["inputs"]) or "- (none)"
    parts.append(RULES.format(ctx=ctx, inp=inp))
    parts.append(f"## Group: {g}\n")
    for iid, title, segs in spec["items"]:
        parts.append(f"### {iid}. {title}\n")
        srcs = []
        body = []
        for s in segs:
            if s[0] == "L":
                _, f, a, b, anchor = s
                body.append(excerpt(f, a, b, anchor))
                srcs.append(f"`{f}` lines {a}-{b}")
            elif s[0] == "T":
                body.append(s[1])
            elif s[0] == "GEN":
                body.append(GEN[s[1]]())
                srcs.append(f"generated ({s[1]})")
        if srcs:
            parts.append("Source: " + "; ".join(srcs) + " (verbatim).\n")
        if any(s[0] == "GEN" for s in segs):
            parts.append("\n\n".join(body) + "\n")
        else:
            parts.append("````\n" + "\n\n".join(body) + "\n````\n")
    return "\n".join(parts)


def main() -> int:
    GDIR.mkdir(parents=True, exist_ok=True)
    allp = ["# G5-bis audit: all statements under review\n",
            "One section per reviewer group. The per-group files `statements/<group>.md` are what each reviewer receives.\n"]
    for g, spec in GROUPS.items():
        txt = build_group(g, spec)
        (GDIR / f"{g}.md").write_text(txt, encoding="utf-8")
        allp.append(f"\n---\n\n{txt}")
    OUT.write_text("\n".join(allp), encoding="utf-8")
    n = sum(len(s["items"]) for s in GROUPS.values())
    print(f"wrote {OUT} and {len(GROUPS)} group files, {n} items")
    return 0


if __name__ == "__main__":
    sys.exit(main())
