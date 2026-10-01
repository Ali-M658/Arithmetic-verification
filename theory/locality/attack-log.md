# Attack log: theory/locality/proof.md (T1–T3)

One adversarial review was run on the statements and proofs of T1–T3 only. It was read-only.
Every quotation and page reference was checked against the fetched texts in `sources_cache/`.
The reviewer re-ran `check_locality.py` (passes) and rechecked every inequality of T3 by hand.

**Verdict before fixes.**

| | verdict |
|---|---|
| T1 | stands, via Proof A |
| T2 | Prop. 2.1 and Cor. 2.3 stand; Prop. 2.2 true but its proof has a gap |
| T3 | stands; two claims needed tightening |

No fatal defect was found.

## Findings and dispositions

| # | severity | finding | disposition |
|---|---|---|---|
| 1 | SERIOUS | Prop. 2.2 used "ℓ_c maps onto (0,∞)". The fetched Thurston text does not say that. The "(R⁺)^{l−3}" quote is about pieces with corner reflectors, which do not occur here. The text also omitted Thurston's exception "the degenerate case A(2,2; )", which occurs for signatures such as (0;2,2,2,3) | **Fixed.** The proof now uses only that Thurston's parameter map is a continuous injection from a space homeomorphic to ℝ^d. Invariance of domain then gives an open image, so the ℓ_c-projection contains an open interval. The degenerate case is covered: its edge parameter d gives the closed-geodesic length 2d (product of the two half-turns). §3.4 now says "segment" instead of "line" |
| 2 | SERIOUS | Proof C claimed independence of [DGGW]/[Uçar]. Lemma 3.2 uses the a-priori Weyl bound, taken from Theorem 1 | **Fixed.** The dependence is stated: Proof C is independent of the *coefficient computations* and uses only the order-t⁻¹ term. The route via Selberg's lemma and [Mar] Prop. 10 is noted as an alternative; Selberg's lemma was not fetched |
| 3 | MINOR | "Points of T(O) are marked structures" is not in the fetched chapter | **Fixed.** The proof now uses only "each Y ∈ T(O) is a hyperbolic orbifold of signature σ and ℓ_c(Y) is a closed-geodesic length of Y" |
| 4 | MINOR | Page numbers: Thurston 13.3.5 is on p. 312; Uçar Thm 4.11 p. 127; LV Thm A p. 3; LV's Maclachlan–Rosenberger remark p. 2; DS Thm 3.2 p. 5 | **Fixed** |
| 5 | MINOR | A quotation marked verbatim was not: the source spells "paremetrized", and the exception had been dropped | **Fixed.** Full sentence quoted verbatim with [sic] |
| 6 | MINOR | §3.5 said "two fetched sources show" same-signature isospectral pairs; only LV does. The DR paraphrase dropped DR's counting conventions. "Carries almost all of it" was rhetoric | **Fixed.** Wording narrowed, DR conventions stated, rhetoric replaced by the proved §3.4 statement |
| 7 | MINOR | Lemma 3.2 needs supp χ ⊂ [−2,2] for exponential type ≤ 2R. Marklof proves Thm 4 directly, not by approximation | **Fixed**, both |
| 8 | MINOR | Marklof's (193) repeats the (192) misprint | **Fixed.** Both noted; the DS normalisation is confirmed verbatim |
| 9 | MINOR | The "Z₁ ≡ Z₂ ⟺ isospectral ⟺ w₁ ≡ w₂" step from DS's length spectrum to w was unstated | **Fixed.** The equivalence is derived from Thm 3.5 plus Laplace-transform uniqueness; the n → w step is spelled out |
| 10 | MINOR | "Equivalently" should be "as a consequence". Falsity of the constant-C form is proved only when L* = ℓ | **Fixed.** Scope stated. Explicit pairs with ℓ₁ ≠ ℓ₂ come from the T4 family. The general existence argument via pinching is not given, and is listed as open below |
| 11 | MINOR | The formula for Φ_j involves β₋₁ at j = 1 | **Fixed.** Φ₁ stated separately; a sentence on the absence of half-integer powers added |
| 12 | MINOR | Universality needs charts of equal radius; the [DGGW] Thm 4.8 sum runs over singular strata | **Fixed**, both |
| 13 | MINOR | The justification for term-by-term Taylor expansion was only in a script docstring | **Fixed.** Moved into the text |
| 14 | MINOR | prop:Kinf becomes unconditional via Thm 1, not via Cor 2.3. eq:moduli is about 𝓜 while Prop 2.1 is about T. The nonvanishing of the top power-sum weight (definitions.tex l.179–181) follows from Uçar (4.33)/(4.25) ∝ B_{2ν+2} | **Fixed.** All three addressed in "Consequences" |
| 15 | — | Not defects (confirmed): Prop. 2.1; Cor. 2.3 including the triangle case; Lemma 3.3; every inequality of Thm 3.4 (a)–(c); Thm 3.5; the trace-formula weights; Iso^max; β = β̃/m against DGGW Prop. 5.5; all other verbatim quotations | — |

## Residual open points (not defects in what is claimed)

- **Pairs with different systoles in every signature.** That every signature with dim T > 0
  contains pairs with ℓ₁ ≠ ℓ₂ (equivalently, that the systole is not constant on T) is not
  proved here. It is only needed to make the constant-C counterexample universal; the T4
  family gives explicit pairs.
- **Donnelly's own wording** (Math. Ann. 1976) was not checked; it is paywalled and logged in
  `review/outstanding-fetches.md` §1.9.
- **Hejhal and Iwaniec** were not fetched (§1.10). Lemma 3.2 replaces them.
