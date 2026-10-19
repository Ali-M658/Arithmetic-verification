<!-- FIX-CHECK N (round 7): returned text saved verbatim; the reviewer could not write files -->

# FIX-CHECK N: "Triples with Equal Sum and Equal Reciprocal Sum" (Integers version, round 7)

**Summary:** All 7 MAJOR items and every applicable minor item are in place. Two minor items are PARTIAL (n15, n25). None is MISSING or WRONG. There are no "??" cross-references, no remarks about length or cuts, and no mentions of AI or review history beyond the allowed placeholders. Four small new problems are listed under (a) and (d).

I rendered all 22 pages at 110 dpi and read them as images. I also checked the key claims in exact arithmetic. The scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/fixcheck-N/scratch/checks/`. In `chk2.py` the `fromE` helper is wrong (my bug, not the paper's); the 3P check there goes through `toE`, and `inv.py` checks the paper's inverse map directly.

What I checked independently:
- **Isomorphism to the Tate normal form (p. 3):** the substitution sends the Tate equation to c⁶/64 times the E_Λ equation, and (0:1:0) maps to (0,0).
- **Prop. 2:** the tangent at O and the inverse maps are correct.
- **Torsion pairs:** all four pairs on C_{169/16} are primitive with Λ = 169/16, and each pair's points differ by torsion of order 4 or 12.
- **Counts and examples:**
  - Theorem 4's 3P is correct.
  - The four classes of Table 1 are correct.
  - There are 506 pairs D_{u,v} with S ≤ 4800.
  - There are 189 lines.
  - Table 2's local exponents and the ratios 7626/46254 = 16.5% and 83.5% are correct.
  - The class-size sums give 98742 classes and 102719 pairs.
  - The constants 3/(32π⁴) and 3/(128π⁴), Lemma 1's discriminants and the Prop. 4 identity are correct.

## MAJOR items

| id | where in the PDF | status | reason |
|---|---|---|---|
| N1 | p.1 abstract: "the universal elliptic curve with a rational point of order six … The torsion of these curves is then classical; we determine which torsion points are positive". p.3: "the elliptic modular surface of Γ0(6) [26, Table 2] … for c = −1/Λ … isomorphic over Q … to the Tate normal form … tabulated by Kubert [16], as Mazur records [18, p. 156]". p.3 after Thm A: "The first sentence is, in elementary form, the classical description … the description of the positive torsion points is new". p.9 Thm 1(i): "the cases (ii) and (iii) below exclude each other" | DONE | Kubert and Beauville are credited, (i)–(iii) are called classical, the isomorphism checks out, and the abstract is reworded. See (a1) on the name Γ0(6). |
| N2 | p.4–5 (§1.4): Ulas, Chen [7, A.5.1], Choudhry [8] ("we have not been able to consult Choudhry's paper"), Graham/van Doorn [14, 28], BGN p.130 and Zhang [30], MacLeod with "R/r = … = (Λ − 1)/4, so such triangles are positive rational points of C_{4N+1}". Narrowed novelty sentence: "As far as we know, the counting function N(X), the bounds … and the exhaustive enumeration are new, while individual coincidences and a parametric family are in [7, 8]" | DONE | All the literature is in. Small gap: the paper never says in words that a coincidence is a pair of triangles with equal perimeter and equal R/r; it only says the triangles lie on C_{4N+1}. |
| N3 | p.1 and p.3 Thm B: "N(X) ≫ X(log X)²". p.13: "Theorem 3 (One more logarithm; the constant is not optimised)". p.4: Prop. D "is at the scale of the number of triples … does not show that coincidences are rare" | DONE | No "438" sentence remains (grep finds none). |
| N4 | p.14: "a quartic del Pezzo surface in P⁴; three of the points are rational and two conjugate, so the Picard rank … is 5 … conic bundle … By Browning and Sofos [5, Theorem 1.1] … O(y(log y)⁴), and … O(X(log X)⁵) … that the positive ones … have the same order is to be expected but is not part of that theorem, and we do not claim it". §6.4 updated (p.19) | DONE | The del Pezzo identification checks out (five points, no three collinear; the sixteen lines carry no positive points). The lower bound is not claimed. |
| N5 | p.18: divisor structure "n(s) = Σ_{d∣s} n_prim(s/d)"; "no sampling error … It is not a statistical uncertainty"; quasi-likelihood criterion "divided by the Pearson dispersion 6.8 … 1.4"; holdout "N(6000) − N(4800) = 42 960 … 0.25% … 2.3%"; window values 4.44 / 4.64 / 4.39; dual-family caution worded conditionally | DONE | See (a3) for one figure that does not follow from the stated numbers. |
| N6 | p.10–11: Lemma 4 ("Translations that preserve positivity") with proof; the C_{169/16} example at S = 845. p.16: "7626 (16.5%) are dual … four are of the second kind, all on C_{169/16}, at S = 845, 1183, 2145 and 3003 … 38 624 are of the third kind". p.20: "translations by the torsion points of order 12 give further surfaces" | DONE | Lemma and counts are present. All four pairs were verified: torsion differences of order 4 and 12. |
| N7 | p.9: "[18, Chapter III, Theorem (5.1), p. 156] … as Z/2 × Z/12 does not occur". p.16: "deciding torsion by membership in the torsion group of Theorem 1" | DONE | The Corollary (5.2) citation is replaced by Theorem (5.1). |

## Minor items with a fix / state / add disposition

| id | where | status | reason |
|---|---|---|---|
| n1 | p.5 Lemma 1: "(2, 3, c′) with 3 ≤ c′ ≤ 5"; "as (3, 3, 3) is the only listed triple with least entry 3, the two then have sum 9" | DONE | Both discriminants recomputed. |
| n2 | p.9 Lemma 3 proof: "π² = 1 gives α² = 1 … ±1 … As π is not the identity … has a fixed point … α = −1" | DONE | |
| n3 | p.9: "twelve points, the six orderings of the triple x and the six orderings of its dual". p.10: "three orderings of (1,1,t) and the three orderings of its dual (t,t,1) … six orderings of (1, r, r²), among them its dual, an ordering" | DONE | |
| n4 | p.8 "Lemma 3 (Permutations)" is numbered; the data is in §6.1 (p.16) | DONE | |
| n5 | p.15: "images contained in sets, cut out by local conditions … the images of explicit rational points fill these sets, so they are the images, and 2^r = \|α(Γ)\|·\|ᾱ(Γ̄)\|/4" | DONE | Ranks 0, 2, 3, 3, 2 follow from the stated orders. |
| n6 | p.15: "+1 for C27/2, C155/12 and C68/5 … conductors … 90, 6250530, 82110, 1715185290, and 41388270" | DONE | Matches the verdict's curve-by-curve list. |
| n7 | p.15: "An independent 2-isogeny descent in exact arithmetic proves them" | DONE | No floating-point caveat remains. |
| n8 | p.11: "Remark 1 (No linear families; a sketch) … every other family by forms of one degree". p.19: "Remark 1 indicates that d = 1 occurs only through scaling" | DONE | |
| n9 | p.7: "Because c4 ≠ 0 and ord Δ < 12 at Λ = 0, 1, 9, the model is minimal" | DONE | |
| n10 | p.15: "so P has infinite order by Theorem 1(iv)"; p.11: "for suitable orderings" | DONE | |
| n11 | p.6 Prop. 1: "no one of them proportional to a permutation of another" | DONE | |
| n12 | p.6: "they extend to isomorphisms, and the first sends O to the point at infinity and T2 to (0, 0)"; p.8: the points where ι is undefined are listed | DONE | |
| n13 | p.4: "[22, Proposition 2.5] … when the sum M and the product N are integers … [22, Proposition 2.7 and Theorem 2.8]" | DONE (as resolved) | Uses the published Osaka numbering and adds "integers". I cannot check the numbering against the source. |
| n14 | p.4: "[27, Theorem 3.1 and Corollary 3.4]" | DONE | |
| n15 | p.13: "the count of the copies kD_{u,v} … equals c_iso X log X − 0.286X to three digits for 10⁴ ≤ X ≤ 4 × 10⁷" | PARTIAL | Neither of the requested labels ("numerically", "an observation") was added; the statement could still be read as proved. |
| n16 | p.4, p.12, p.14: integrals start at "18⁻" | DONE | |
| n17 | p.19: "Heuristically, then, a positive answer to Question E would require … whose positive real points form a nonempty open set" | DONE | |
| n18 | p.4: "log₂(N(X)/N(X/2))"; Table 2 caption: "log(N(X)/N(X/2))/log 2" | DONE | The two forms are the same quantity. |
| n19 | p.2: "(see also the erratum [12])"; reference [12] | DONE | |
| n21 | abstract: "falling from about 2 near 500"; p.4: "about 2 for 300 ≤ X ≤ 500" | DONE | |
| n22 | p.3: "it is proved for pairs only, since dual pairs can lie in one class" | DONE | |
| n23 | p.4: "Equivalently (with Theorem B), the number A(y) … is y^{1+o(1)}: by Lemma 5, A(X) ≤ N(X) ≤ X Σ 1/S_D = X ∫_{18⁻}^X y⁻¹ dA(y)" | DONE | The one-line argument is correct. |
| n24 | p.15–16: "hashes the correctly rounded double … Every candidate match is then confirmed by exact 128-bit cross-multiplication … distinct rationals with the same double are never grouped together" | DONE | |
| n25 | p.20: "189 lines … coprime integers \|a\|,\|b\|,\|c\| ≤ 7, counted up to permutation of the coordinates and sign (the list and the test are in the deposit)" | PARTIAL | The normalisation is stated and 189 is reproduced. The paper does not name the files the verdict says to point to (`families.py`, `line_families.csv`), and the data statement does not list them either. |
| n26 | p.19 caption: "(1, 4, 4) (dark) and (1, 1, 4) (orange)" | DONE | In the rendered figure, the dark points sit near the edge midpoints, which is (1,4,4), and the orange points near the vertices, which is (1,1,4). The split marker at S = 18 is correct. |
| n27 | p.8: third point renamed "V" | DONE | |
| n28 | p.17: table header "largest size"; caption "the largest class size" | DONE | |
| n30 | p.14: Manin-order framing; p.20: "[24, Proposition 7.1]" | DONE | |
| n31 / n33 | p.15: "this is also [13, Theorem 5.8], proved there by a 2-isogeny descent by hand"; the exact descent for all five curves is stated | DONE | |
| n32 | pp.20–21: Statements and Declarations block | DONE | Kept with the allowed placeholders. |

n20 is resolved together with N7. n29 has no fix disposition; the BGN quotations are kept on pp.7 and 120 and I cannot check them against the source.

## Other findings

**(a) Statements that look wrong or overstated** (all minor):
1. **Γ0(6), p.3.** The paper calls the pencil "the elliptic modular surface of Γ0(6)". Fibres of types I6, I3, I2, I1 belong to Γ1(6); the verdict's own N1 entry says Γ₁(6). The modular curve is the same, since Γ0(6) = ±Γ1(6). But Shioda's elliptic modular surface needs a group without −1, so either say Γ1(6) or add "(= ±Γ1(6))".
2. **p.18, "The dual family shows that such fits do not estimate asymptotic exponents."** This is stated flatly, while the supporting sentence is conditional ("if, as expected …"). The lead-in should be conditional too, or say "suggests".
3. **p.18, "about 0.2 and 1.9 times the standard deviation".** From the paper's own figures, √(6.8 · 42960) ≈ 540, and 2.3% of 42960 is about 988, which is 1.83 SD, so "about 1.8". The text's 1.9 is consistent only if the unrounded percentage is at least about 2.34%. The 0.2 figure is fine.

**(b) Broken cross-references:** none. There is no "??" in the text, and every reference renders correctly in the images.

**(c) Comments on length or suggested cuts:** none.

**(d) AI, internal paths and review history:**
- The only AI mention is the allowed "[PLACEHOLDER: statement on the use of AI tools …]". There is nothing on referees, rounds, the blind check or verdicts.
- The data statement (p.20) gives a live URL, https://github.com/pa1aash/equal-sum-reciprocal-triples, which is not a placeholder. The verdict says this repository is not yet public (N8). It must be published before submission, or replaced by a placeholder.
- The same statement names the scripts that produce the tables and figure (`make_tables.py`, `groups.csv`, `enumerate_fast.py`, `ranks.py`, `check_enum.py`, `per_S.csv`, `exponent_fits.py`, `growth_fits.py`, `F9.py`). These are file names inside the deposit, not internal repository paths, so they are acceptable. "F9.py" looks like an internal numbering.
