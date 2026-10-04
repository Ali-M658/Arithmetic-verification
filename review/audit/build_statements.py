#!/usr/bin/env python3
"""Build review/audit/STATEMENTS.md: every audited result, copied verbatim from its source file
by line range. Statements only, no proofs. Each excerpt is anchored: its first line must contain
the given anchor string, and no excerpt may contain a proof marker, or the script exits nonzero.

Run from the repository root:  python3 review/audit/build_statements.py
Group files review/audit/statements/<group>.md are also written, one per reviewer.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "review/audit/STATEMENTS.md"
GDIR = ROOT / "review/audit/statements"

AUD = "theory/audibility/proof.md"
LOC = "theory/locality/proof.md"
SIG = "theory/signatures/proof.md"
SIGT = "theory/signatures/statements.tex"
STA = "theory/stability/proof.md"
THR = "theory/threshold/proof.md"
CUR = "theory/curvature/proof.md"
DIV = "theory/divergence/proof.md"
VAR = "theory/diophantine/variety.md"
REC = "theory/diophantine/RECOMMENDATION.md"
TEX = "paper/main.tex"
DEF = "theory/definitions.tex"

# (id, title, file, first line, last line, anchor in first line)
GROUPS: dict[str, list[tuple]] = {
    "paper-core": [
        ("PC.0", "Area and hyperbolicity (eq:area)", TEX, 94, 99, "Gauss--Bonnet"),
        ("PC.1", "Main theorems A, B, C and Corollary D (thmA, thmB, thmC, corD) with the definition of K(F)", TEX, 103, 119, "Throughout, $K(F)$"),
        ("PC.2", "Conventions (eq:a0conv)", TEX, 139, 144, "We use the orbifold heat-trace expansion"),
        ("PC.3", "Heat expansion structure (sec:heatexp)", TEX, 171, 175, "On a closed hyperbolic $2$-orbifold"),
        ("PC.4", "lem:cot", TEX, 180, 182, "Cotangent sum"),
        ("PC.5", "prop:csc", TEX, 188, 190, "Cosecant sum"),
        ("PC.6", "Cone convention and def:cone, cor:conevals", TEX, 196, 205, "In the convention of"),
        ("PC.7", "Inversion eq:s1inv and rem:bugfix", TEX, 216, 231, "Write the elementary symmetric functions"),
        ("PC.8", "Third coefficient eq:b1, eq:a2red", TEX, 236, 246, "The three leading coefficients are those of"),
        ("PC.9", "prop:cs", TEX, 248, 250, "Cauchy--Schwarz bound"),
        ("PC.9b", "prop:recovery", TEX, 256, 258, "Recovery from three symmetric functions"),
        ("PC.10", "Jacobian claim after prop:recovery", TEX, 269, 269, "This Newton--Vieta inversion"),
        ("PC.11", "Two-coefficient map, strata, lem:chamber", TEX, 279, 290, "The first two heat coefficients resolve"),
        ("PC.12", "R^+ formula, lem:bound", TEX, 295, 303, "In particular a two-coefficient collision"),
        ("PC.13", "prop:min", TEX, 310, 312, "Balanced configurations minimize"),
        ("PC.14", "S_1>=10 claim and thm:separation", TEX, 319, 323, "Since $\\sigma$ records $S_1$ first"),
        ("PC.15", "Numerical endpoint claims in the proof of thm:separation (claims only)", TEX, 333, 345, "(p=2)"),
        ("PC.16", "Remark* on a_0", TEX, 394, 396, "remark*"),
        ("PC.17", "Degeneracy definition, N(S), prop:scaling", TEX, 402, 421, "two-coefficient spectral degeneracy"),
        ("PC.17b", "thm:density-lower", TEX, 426, 431, "Infinitude and a linear lower bound"),
        ("PC.18", "Primitive pair at S=36 (claim)", TEX, 436, 436, "Theorem~\\ref{thm:density-lower} is unconditional"),
        ("PC.19", "Density table and fitted exponent (claims), conj:density, later claims", TEX, 440, 481, "We enumerated $N(S)$ exactly"),
        ("PC.20", "rem:ncone", TEX, 493, 495, "Larger cone counts"),
        ("PC.21", "Table tab:enum claim", TEX, 504, 504, "As an independent cross-check"),
    ],
    "definitions": [
        ("DF.1", "def:signature, def:heatcoef", DEF, 17, 41, "Signature"),
        ("DF.2", "def:K and eq:Kcompare", DEF, 49, 65, "Kiso"),
        ("DF.3", "prop:rigidity (statement)", DEF, 69, 74, "Rigidity of triangular pillows"),
        ("DF.4", "eq:moduli", DEF, 95, 105, "By Troyanov"),
        ("DF.5", "thm:locality, prop:Kinf (statements)", DEF, 110, 128, "Locality; forward reference"),
        ("DF.6", "thm:Crestated (statement)", DEF, 142, 150, "restated"),
        ("DF.7", "rem:nconerestated", DEF, 159, 177, "Larger cone counts, restated"),
    ],
    "audibility": [
        ("AU.0", "Heat input and notation", AUD, 26, 50, "Input from the heat expansion"),
        ("AU.1", "Theorems A, B, C", AUD, 51, 84, "Theorem A (audibility"),
        ("AU.2", "Lemma 1 (parity)", AUD, 88, 91, "Lemma 1 (parity)"),
        ("AU.3", "Jacobian claim (Remark 2) and padding claim (Remark 3)", AUD, 123, 136, "Repeated orders are allowed"),
        ("AU.4", "Integer witnesses table (claims)", AUD, 217, 225, "In the table"),
    ],
    "signatures": [
        ("SG.0", "Setting and heat input (H)", SIG, 41, 75, "## 1. Setting"),
        ("SG.1", "Lemma 1 (cone polynomials)", SIG, 78, 81, "Lemma 1 (cone polynomials"),
        ("SG.2", "Lemma 2 (triangular basis)", SIG, 95, 99, "Lemma 2 (triangular basis)"),
        ("SG.3", "Lemma 3 (padding)", SIG, 105, 106, "Lemma 3 (padding)"),
        ("SG.4", "Lemma 4 (reduction)", SIG, 110, 132, "Lemma 4 (reduction)"),
        ("SG.5", "Theorem S", SIG, 152, 157, "Theorem S."),
        ("SG.6", "Corollary S1", SIG, 179, 182, "Corollary S1"),
        ("SG.7", "Corollary S2", SIG, 185, 191, "Corollary S2"),
        ("SG.8", "Theorem T1", SIG, 202, 211, "Theorem T1"),
        ("SG.9", "Proposition P (Prouhet)", SIG, 235, 241, "Proposition P"),
        ("SG.10", "Theorem N", SIG, 247, 263, "Theorem N (non-uniformity)"),
        ("SG.11", "Construction claims for Theorem N (computed ranges)", SIG, 305, 313, "The constructions are built"),
        ("SG.12", "Corollary N1", SIG, 315, 319, "Corollary N1"),
        ("SG.13", "Manuscript-facing LaTeX versions (statements.tex)", SIGT, 11, 117, "subsection{The signature"),
    ],
    "locality": [
        ("LO.0", "Setting", LOC, 9, 17, "**Setting.**"),
        ("LO.1", "Theorem 1 (signature locality)", LOC, 47, 69, "Theorem 1 (signature locality)"),
        ("LO.2", "Thurston Cor. 13.3.7 as quoted", LOC, 154, 157, "Source statement"),
        ("LO.3", "Proposition 2.1", LOC, 167, 171, "Proposition 2.1"),
        ("LO.4", "Proposition 2.2", LOC, 184, 185, "Proposition 2.2"),
        ("LO.5", "Corollary 2.3", LOC, 212, 219, "Corollary 2.3"),
        ("LO.6", "Theorem 3.1", LOC, 254, 265, "Theorem 3.1"),
        ("LO.7", "Lemma 3.2 (statement only)", LOC, 289, 293, "Lemma 3.2"),
        ("LO.8", "Lemma 3.3", LOC, 321, 324, "Lemma 3.3"),
        ("LO.9", "Theorem 3.4", LOC, 347, 362, "Theorem 3.4"),
        ("LO.10", "Claim: the t^{-1/2} prefactor cannot be dropped", LOC, 396, 412, "cannot be dropped"),
        ("LO.11", "Theorem 3.5", LOC, 423, 430, "Theorem 3.5"),
    ],
    "stability": [
        ("ST.0", "Setting and the recovery map", STA, 45, 75, "## 1. Setting"),
        ("ST.1", "Proposition S1", STA, 78, 88, "Proposition S1"),
        ("ST.2", "Front-end tables (claims)", STA, 100, 131, "The first rows of L"),
        ("ST.3", "Lemma S2.1", STA, 142, 146, "Lemma S2.1"),
        ("ST.4", "Lemma S2.2", STA, 172, 183, "Lemma S2.2"),
        ("ST.5", "Theorem S2", STA, 196, 222, "Theorem S2"),
        ("ST.6", "Ostrowski input as quoted", STA, 264, 273, "Standard global theorem"),
        ("ST.7", "Lemma S3", STA, 275, 287, "Lemma S3"),
        ("ST.8", "Theorem S3", STA, 301, 321, "Theorem S3"),
        ("ST.9", "Proposition S3.2", STA, 328, 347, "Proposition S3.2"),
        ("ST.10", "Remark S3.3", STA, 348, 357, "Remark S3.3"),
        ("ST.11", "Theorem S4", STA, 360, 366, "Theorem S4"),
        ("ST.12", "Proposition S5 (statement of the two tests)", STA, 378, 408, "Proposition S5"),
        ("ST.13", "Upper bound by construction; rounding convention", STA, 413, 429, "Upper bound by construction"),
        ("ST.14", "Results table (printed values to re-certify)", STA, 430, 446, "**Results**"),
    ],
    "threshold": [
        ("TH.0", "Notation and the overlap definition", THR, 20, 45, "## 1. Notation"),
        ("TH.1", "Lemma 1", THR, 48, 50, "Lemma 1 (one inequality)"),
        ("TH.2", "Lemma 2", THR, 63, 67, "Lemma 2 (adjacent separation"),
        ("TH.3", "Theorem 1", THR, 74, 79, "Theorem 1."),
        ("TH.4", "Corollary 2", THR, 138, 141, "Corollary 2."),
        ("TH.5", "First-overlap vs first-collision table (computed claims)", THR, 165, 187, "Overlap is necessary"),
        ("TH.6", "Proposition 3", THR, 193, 198, "Proposition 3"),
    ],
    "curvature": [
        ("CU.0", "Conventions", CUR, 37, 54, "## 1. Conventions"),
        ("CU.1", "Flat-cone input (Kokotov) as quoted", CUR, 57, 76, "**Flat cones and flat orbifolds.**"),
        ("CU.2", "Lemma 2 (invariant multiplicities)", CUR, 92, 95, "Lemma 2 (invariant multiplicities)"),
        ("CU.3", "Proposition (curvature comparison) and its strength claims", CUR, 121, 168, "Proposition (curvature comparison)"),
    ],
    "divergence": [
        ("DV.0", "Notation", DIV, 32, 44, "## 1. Notation"),
        ("DV.1", "Lemma 1", DIV, 47, 59, "Lemma 1."),
        ("DV.2", "Theorem 2", DIV, 101, 108, "Theorem 2."),
        ("DV.3", "Theorem 3", DIV, 155, 177, "Theorem 3."),
        ("DV.4", "Corollary 4", DIV, 199, 203, "Corollary 4 (peeling)"),
        ("DV.5", "Borel reading (claim)", DIV, 233, 246, "Borel reading"),
    ],
    "diophantine": [
        ("DI.1", "Proposition 1 (reformulation)", VAR, 18, 33, "Proposition 1."),
        ("DI.2", "Pencil, Weierstrass model, fibre types, torsion (claims)", VAR, 36, 77, "**The pencil.**"),
        ("DI.3", "Reciprocation is a 2-torsion translation; dual family (claims)", VAR, 80, 104, "The Vieta move"),
        ("DI.4", "Proposition 2 (no linear families)", VAR, 162, 168, "Proposition 2."),
        ("DI.5", "Theorem 3 (arbitrarily large fibres)", VAR, 220, 223, "Theorem 3 (arbitrarily large fibres)"),
        ("DI.6", "Rank claims for fibre curves", VAR, 233, 237, "is already large"),
        ("DI.7", "Isolation of the base pair (claim)", VAR, 239, 252, "the base pair is isolated"),
        ("DI.8", "Counting convention and the hyperbolicity of copies", VAR, 261, 269, "Notation: $\\mathcal N(X)$"),
        ("DI.9", "Theorem 4 (S log S)", VAR, 271, 278, "Theorem 4 (isosceles family"),
        ("DI.10", "Theorem 5 (S (log S)^2)", VAR, 300, 302, "Theorem 5 (the conic bundle"),
        ("DI.11", "First fibres of each size and rank certification (claims)", REC, 54, 69, "First fibres of each size"),
    ],
}

PROOF_MARKERS = ("*Proof", "\\begin{proof}", "Proof of Theorem")

# Reviewer bundles: which groups each reviewer receives.
BUNDLES = {
    "audibility": ["audibility", "definitions"],
    "signatures": ["signatures", "definitions"],
    "locality": ["locality", "definitions"],
    "stability": ["stability"],
    "threshold": ["paper-core", "threshold"],
    "curvature-divergence": ["curvature", "divergence"],
    "diophantine": ["diophantine", "paper-core"],
}


def excerpt(rel: str, a: int, b: int, anchor: str, rid: str) -> str:
    lines = (ROOT / rel).read_text().splitlines()
    assert 1 <= a <= b <= len(lines), (rid, rel, a, b, len(lines))
    chunk = lines[a - 1 : b]
    assert anchor in chunk[0], f"{rid}: anchor {anchor!r} not in line {a} of {rel}: {chunk[0]!r}"
    for ln in chunk:
        for mk in PROOF_MARKERS:
            assert mk not in ln, f"{rid}: proof marker {mk!r} inside excerpt {rel}:{a}-{b}: {ln!r}"
    return "\n".join(chunk)


def render(groups: list[str]) -> str:
    out = []
    for g in groups:
        out.append(f"\n## Group: {g}\n")
        for rid, title, rel, a, b, anchor in GROUPS[g]:
            body = excerpt(rel, a, b, anchor, rid)
            out.append(f"### {rid}. {title}\n\nSource: `{rel}` lines {a}-{b} (verbatim).\n\n"
                       f"````\n{body}\n````\n")
    return "\n".join(out)


HEADER = """# G5 audit: statements under review

Every result below is copied verbatim, by line range, from its source file on branch
`s9a-audit` (`build_statements.py` asserts the anchors and that no proof text is included).
Hypotheses and notation are the `.0` items of each group. Proofs are deliberately omitted.
Cross-references inside the statements (e.g. "Theorem A", `lem:chamber`) point to other
items in this file.

External inputs the results rely on (texts fetched headlessly by `fetch_sources.sh` into
`review/audit/sources/`, not committed):

| input | used by | fetched text |
|---|---|---|
| Uçar, PhD thesis, arXiv:1711.03405: (4.25), (4.33), (4.35), Thm 4.11, Thm 4.20, Cor 4.21, Cor 4.23 | every heat-coefficient statement | `ucar_1711.03405.txt` |
| Dryden–Gordon–Greenwald–Webb, arXiv:0805.3148: Def 4.7, Thm 4.8, §5.6, Thm 5.15, Prop 5.22 | locality, curvature, priority | `dggw_0805.3148.txt` |
| Dryden–Strohmaier, arXiv:math/0504571: trace formula eq. (1), Thm 1.1, Thm 3.2, Prop 3.3 | locality T3, divergence | `ds_math0504571.txt` |
| Thurston, ch. 13: 13.3.5, 13.3.6, Cor 13.3.7 | locality T2, curvature | `thurston_ch13.txt` |
| Ostrowski, Acta Math. 72 (1940), Théorème XXX | stability | `ostrowski_1940.txt` |
| Holtz–Tyaglov, arXiv:0912.4703 (Orlando's formula) | audibility, stability | `holtz_tyaglov_0912.4703.txt` |
| Marklof, arXiv:math/0407288 | locality (normalisation cross-check) | `marklof_math0407288.txt` |
| Schueth, arXiv:1812.06119 | cone coefficients l<=2 | `schueth_1812.06119.txt` |
| Kokotov, arXiv:0906.0717 | curvature (flat cones) | `kokotov_0906.0717.txt` |
| Linowitz–Voight arXiv:1408.2001; Doyle–Rossetti arXiv:1103.4372 | locality §3.5 | `lv_1408.2001.txt`, `dr_1103.4372.txt` |
| Bremner–Guy–Nowakowski, Math. Comp. 61 (1993); Schinzel, Serdica 22 (1996); PARI/GP manual (ellrank) | diophantine | `bgn_mcom1993.txt`, `schinzel_serdica1996.txt`, `pari_elliptic.html` |
| Müller–Feliu–Regensburger–Conradi–Shiu–Dickenstein, arXiv:1311.5493 | Theorem A prior art (P7) | `mueller_1311.5493.txt` |
| Donnelly 1976 | restated in DGGW §4 only | standing gap (not fetched) |
"""


def main() -> int:
    GDIR.mkdir(parents=True, exist_ok=True)
    order = ["paper-core", "definitions", "audibility", "signatures", "locality", "stability",
             "threshold", "curvature", "divergence", "diophantine"]
    assert set(order) == set(GROUPS)
    OUT.write_text(HEADER + render(order))
    n = sum(len(GROUPS[g]) for g in order)
    for name, gs in BUNDLES.items():
        (GDIR / f"{name}.md").write_text(HEADER + render(gs))
    print(f"wrote {OUT.relative_to(ROOT)}: {n} excerpts; {len(BUNDLES)} reviewer bundles")
    return 0


if __name__ == "__main__":
    sys.exit(main())
