# VERDICT-N — round 7, the note (Integers version, 19 pp.)

Input: `_input/N-note-integers.pdf` (SHA-256 in README.md). Reports: `N-a-editor-partitions`, `N-b-torsion-modular-curves`,
`N-c-symmetric-systems`, `N-d-points-of-bounded-height`, `N-e-proof-reader` (each `REPORT.md`, saved verbatim; N-c with its
verbatim addendum on Mazur). Length remarks: none were made.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| N-a (editor, partitions) | **send to review**; major revision | 0.9 correctness / 0.7 verdict |
| N-b (torsion, modular curves) | major revision | high |
| N-c (symmetric systems) | minor revision | high / moderate |
| N-d (points of bounded height) | major revision | high |
| N-e (rigour, citations) | minor revision | high |

Stop condition: **not met** (N-b and N-d recommend major revision; confirmed MAJOR items below).

No reviewer found a mathematical error. All recomputed numbers agree (Table 2 reproduced to 6000 by N-d with an
independent C enumerator; ranks, torsion, root numbers, Selmer orders, 3P, the C_{49/4} orders, the isosceles
constants, Theorem 3's constant chain).

## FATAL

None.

## MAJOR (deduplicated; checked against the repository)

| id | issue | raised by | status | evidence / resolution |
|---|---|---|---|---|
| N1 | C_Λ is the universal curve with a point of order 6 (Beauville's Γ₁(6) surface); Theorem A(i)-(iii) is Kubert's parametrisation of X₁(12), X₁(2,6) over X₁(6) plus Mazur; not credited; abstract "We determine the torsion" overstates. | N-a M1, N-b M2, N-c M3 | **CONFIRMED** | Verified symbolically (`main/scratch/` check, now in `paper/arith/checks/check_note.py`): with c = −1/Λ, Kubert's E(c+c², c) has j = j(E_Λ) and c₄, c₆ ratios u⁴ = c⁴/16, u⁶ = c⁶/64, u = c/2 ∈ Q(c): an isomorphism over Q(c). Credit Kubert (record fetched), Beauville's surface as the modular surface of Γ₁(6); (i)-(iii) labelled classical in elementary form, (iv) new; abstract reworded; (ii) and (iii) exclusive. |
| N2 | Literature: equal sums with exponents ±1 (Choudhry 2011), Chen's PTE survey, Zhang 1608.03382, Graham 1963, van Doorn 2025, the equal-perimeter / equal-R/r triangle reading; novelty sentence too broad. | N-a M2, N-c M1 | **CONFIRMED** (as a literature gap) | Records and texts fetched by a literature subagent (`main/scratch/lit/`); cited for what the fetched texts say; novelty sentence narrowed; the triangle equivalence was already stated (MacLeod paragraph) and is now said explicitly. |
| N3 | Theorem 3's constant 3/(128π⁴) is an artefact of the proof (factors 2, 4/3, box); the "log X > 438" comparison is meaningless; Proposition D is at the trivial scale. | N-a M3, N-c M2, N-d m1 | **CONFIRMED** | Theorem B(ii) and the abstract state ≫ X(log X)²; Theorem 4.4 keeps its proved constant, labelled unoptimised; both 438 sentences removed; Proposition D kept as proved, described as at the scale of the number of triples (as before). |
| N4 | The dual family is the anticanonical quartic del Pezzo surface Bl₅P² (ρ = 5 over Q, conic bundle with a section); Browning–Sofos give the order B(log B)⁴ for its rational points; "its exact order is not known" (p. 16) is wrong as stated. | N-d M1 | **CONFIRMED** | `theory/diophantine/dual_delpezzo.py` (new): the six cubics vanish at the five points, span the 5-dimensional space of cubics through them, no three collinear; S_D within a factor 3 of the anticanonical height. The text identifies the surface, cites Browning–Sofos for the upper bound O(y(log y)⁴) of primitive dual pairs, hence O(X(log X)⁵) for their contribution to N, and states the positive-region lower bound as expected, not proved. |
| N5 | §6.3: the ± values are not uncertainties (complete enumeration; n = 1 * n_prim carries divisor structure, Lemma 3); model comparison criterion unnamed; the 4801-6000 holdout unused. | N-a M4, N-d M2 | **CONFIRMED** | `exponent_fits.py` gains the holdout (log-power law +0.25%, power law +2.3% on N(6000) − N(4800) = 42960); text relabels the ± as descriptive spread of a block resampling, states the divisor structure and the window spread, names the criterion (log-likelihood difference over the Pearson dispersion), and uses the dual family (fitted 2.56, Manin order 4) as the caution. |
| N6 | Missed source of coincidences: translation by a torsion point of order 4 or 12 on Z/12 curves with r < 0 (C_{169/16}); §3 and §6.4 incomplete; the "16.5% dual" statistic needs a third category. | N-b M1 | **CONFIRMED** | `theory/diophantine/torsion_pairs.py` (new; asserts): P + T is positive for positive P exactly when T is not positive; the only positivity-preserving torsion translations outside the base points are on Z/12 curves with r < 0. Of the 46254 primitive pairs with S ≤ 4800: 7626 dual, 4 of torsion type (all on C_{169/16}: S = 845, 1183, 2145, 3003), 38624 other; none of torsion type for S ≤ 600 (so the p. 8 statement stands). Text: new lemma on positivity-preserving translations, the example, the counts; §6.4 adds the corresponding surface. |
| N7 | Mazur citation: Corollary (5.2) does not exclude Z/2 × Z/12; Theorem 1(i) needs Theorem (5.1). | N-e M1, N-b m10, N-c m11 | **CONFIRMED** | Cite Theorem (5.1), p. 156, for (i); keep Corollary (5.2) for the order bound used in §3. |
| N8 | The code repository is not public (404). | N-e M2 | **ANSWERED** (outside the paper) | The deposit is built in Part 2 (release repository and Zenodo zip); publishing it is a pre-submission step of `paper/SUBMISSION-CHECKLIST.md`, with the DOI a declared placeholder. |

## MINOR and presentation (dispositions)

| id | item | raised by | disposition |
|---|---|---|---|
| n1 | Lemma 1: "c′ ≤ 5" should be 3 ≤ c′ ≤ 5; justify "sum 9 and one is (3,3,3)" | N-c m1 | fix |
| n2 | transposition: π² = id ⇒ α² = 1 ⇒ α = ±1 (j = 0 at Λ = 3) | N-b m1, N-c m2, N-e m4 | fix |
| n3 | the cosets ±G + T and ±P₀ + T have six points; the dual of a GP is an ordering | N-b m7, N-c m3 | fix |
| n4 | S₃ action as a numbered lemma; data out of the structural paragraph | N-a m4, N-b m2, N-e P3, N-c P4 | fix (lemma; data moved to §6.1) |
| n5 | Selmer convention; Silverman–Tate has α(Γ), ᾱ(Γ̄); "image = Selmer" clause | N-b m3, N-e m3 | fix (state the images of α, ᾱ, which the descent shows fill the Selmer bounds) |
| n6 | root number of C_{27/2} (+1); conductors | N-b m4 | fix (`ranks.py` now prints conductors: 90, 82110, 1715185290, 41388270; 6250530 for C_{155/12}) |
| n7 | the descent alone proves the ranks; floating-point caveat moot | N-b m5 | fix |
| n8 | Remark 1 is a sketch but is used in §6.4 | N-a m6, N-b m6, N-c m4, N-e m6 | weaken its use ("indicates"); "families by forms of one degree" |
| n9 | minimality clause ord Δ < 12 | N-b m8 | fix |
| n10 | "not torsion" instead of "order at most 12"; which orderings | N-b m9 | fix |
| n11 | Prop. 1 "pairwise non-proportional" for unordered triples | N-a m2, N-e m5 | fix |
| n12 | domains of the birational maps; O ↦ ∞, T₂ ↦ (0,0) | N-a m3, N-b P3 | fix |
| n13 | Sadek–El-Sissi numbering (Prop. 2.6, Thm 2.7 in v2) and "integers" | N-c m9, N-e m1 | fix after the fetched v2 (literature subagent) |
| n14 | Ulas Corollary 3.4 | N-e m2 | fix |
| n15 | secondary term −0.286 numerical | N-a m7, N-d m2, N-c m5 | label "numerically" (already "to three digits"; add "an observation") |
| n16 | integral lower limit 2 → 18⁻ | N-c m6 | fix |
| n17 | heuristic: "implies" → "would, heuristically, require"; open positive region | N-c m8, N-e m7 | fix |
| n18 | local exponent: one definition | N-e m8 | fix (log₂ ratio throughout) |
| n19 | DGGW erratum | N-a m1, N-e m9 | located (Crossref, zbMATH 1404.58043); text not obtainable headlessly; cited as an erratum, no statement about its content |
| n20 | Mazur (5.1) | — | with N7 |
| n21 | "falling from 2.0 at 500" | N-d m5 | "from about 2 near X = 300 to 500" |
| n22 | N_cl does not inherit the (log X)² bound | N-d m4 | state |
| n23 | Question E for the primitive count | N-a m13 | add: N(X) = X^{1+o(1)} iff A(y) = y^{1+o(1)} (proof in one line from Lemma 3) |
| n24 | hashing: sub-grouping within runs of equal keys | N-d m7 | state as implemented (exact cross-multiplication within each run) |
| n25 | 189-line search reproducibility | N-a m10, N-d m9 | point to `families.py` and `data/line_families.csv`; state the normalisation |
| n26 | Figure 1 colour key | N-a P4, N-d m8, N-e P1 | caption: dark (1,4,4), light (1,1,4) — checked against `figures/src/F9.py` |
| n27 | notation clashes (R third point; s) | N-a P1 | rename the third point |
| n28 | Table 2 header "largest class size"; extra columns | N-e P4, N-d P1 | header fixed; primitive and dual counts stay in the text |
| n29 | BGN quotations/pages unverified | N-b, N-c, N-e m11, N-a m12 | literature subagent; kept if confirmed, otherwise flagged |
| n30 | m11 (Schoen hypotheses, Verrill, Meyer, Batyrev–Manin) | N-a m11, N-c m10 | Manin framing added with N4; Schoen locator kept; no new claims about Verrill/Meyer (not fetched) |
| n31 | overlap with A: quote both bounds; one home for the rank-0 result | N-a (overlap) | A now quotes the X log X bound for classes and the ≫ X(log X)² bound for pairs; the rank-0 result is proved in A by hand and in the note by descent, each citing the other (disclosed) |
| n32 | Statements and Declarations block in Springer style | N-e P2 | kept as required by the standing placeholders (author contributions, AI use); Integers accepts back matter |
| n33 | m10 N-d: second independent rank check | N-d m10 | the hand descent of A's appendix for C_{27/2}; the exact descent for all five is stated |

## Resolutions applied (round 7)

Scripts: `main/scratch/fix_N_r7.py`, `fix_N_r7b.py`, `fix_N_r7c.py`, `fix_N_r7d.py` (VERDICT items) and `fix_N_r7e.py`
(blind check N), applied to `paper/arith/note.tex`; the Integers version regenerated by `integers/make_integers.py`
(substitutions updated: Mazur Theorem (5.1), Silverman–Tate §6, Ulas and Browning–Sofos locators, Theorem B display,
the renamed third point V; nine new bibliography items). New references from fetched records via
`tools/build_bib.py` (kubert1976, topyui2007, browningsofos2019, choudhry2011, chen2025, zhang2016, graham1963,
vandoorn2025, dggw2017). New or changed checks: `theory/diophantine/torsion_pairs.py`, `dual_delpezzo.py`,
`exponent_fits.py` (holdout), `ranks.py` (conductors; C_{169/16}), `paper/arith/checks/check_note.py` 8a, 8a′, 8b, 8c.

| id | resolution |
|---|---|
| N1 | Introduction: Γ0(6) modular surface (Top–Yui, Table 2); explicit Q-isomorphism with the Tate normal form, c = −1/Λ (checked); Kubert's table via Mazur p. 156; Theorem A followed by "(i)-(iii) classical, the positive torsion points and the positivity-preserving translations new"; abstract reworded. |
| N2 | Literature paragraph: Chen's survey (A.5.1) for earlier solutions and Choudhry's three-parameter solution (Choudhry not consulted, said so); Zhang and BGN p. 130 for the four-variable expectation; Graham and van Doorn; novelty sentence narrowed. |
| N3 | Theorem B(ii) and abstract: ≫ X(log X)²; both "438" sentences removed; Theorem 4.4 titled "the constant is not optimised". |
| N4 | Paragraph after Theorem 4.4: the dual family is the quartic del Pezzo surface; Browning–Sofos Theorem 1.1 gives O(y(log y)⁴) primitive dual pairs and O(X(log X)⁵) for their contribution; the lower bound for positive points not claimed; §6.4 updated. |
| N5 | §6.3: divisor structure n = Σ_{d∣s} n_prim(s/d); spreads relabelled as descriptive; quasi-likelihood criterion named; holdout 4801–6000 reported; dual family as the caution (conditional wording after the blind check). |
| N6 | Lemma lem:perm (numbered, proof with α² = 1), Lemma lem:postrans with proof, the C_{169/16} example; §6.1 sorts the 46254 primitive pairs (7626 dual, 4 torsion type, 38624 other); §6.4 adds the order-12 surfaces. |
| N7 | Theorem 1(i) cites Mazur Theorem (5.1); (ii) and (iii) exclusive; the §3 order test replaced by membership in the explicit torsion group. |
| N8 | Outside the paper (Part 2 deposit). |
| n1–n33 | as listed in the dispositions table; n13 answered (the note cites the published Osaka version, whose numbering and "rationals" it follows; the referees read arXiv v2), with "M and N integers" added; n28 header shortened to "largest size" (the caption says "largest class size"). |

Blind check N (`blind-check-N/REPORT.md`): all eleven items VERIFIED with independent code (enumeration to 6000,
PARI, sympy); corrected: the Graham/van Doorn description (distinct parts, sum fixed); the dual-family caution made
conditional; "(0,0), the image of (0:1:0)"; the transposition is not the identity; "for suitable orderings";
"(with Theorem B)"; conductors listed with their curves; 0.25 %; Chen's "smallest" qualified.
