# G5 referee report: threshold group and paper core (PC.0-PC.21, TH.0-TH.6)

Scope: statements in `review/audit/statements/threshold.md` only, re-derived from the
statements. Proof texts were not read. Sources: `review/audit/sources/` (Uçar, DGGW, Schueth).
All checks use exact arithmetic. Every script runs from the repo root and exits nonzero on failure:

| script | output | content |
|---|---|---|
| `check_heat.py` | `check_heat.txt` | Uçar (4.25)/(4.33)/(4.35), DGGW (5.7)/(5.10), Schueth Rem 4.2, an independent exact spectrum computation for S²/G, PC.2-PC.10, PC.16 |
| `check_threshold.py` | `check_threshold.txt` | symbolic proof of Theorem 1 and Prop 3, the p ≤ 8 cases, brute force for S ≤ 700 (all p ≤ 232), PC.11-PC.15 |
| `check_enum.py` + `enum.c` | `check_enum.txt`, `data/`, `tab_enum_reference.txt` | exhaustive collision enumeration for 10 ≤ S ≤ 6000 (C), checked fibre by fibre against pure Python for S ≤ 600; Cor 2, S=36, density table, exponent, conjecture, TH.5 |
| `check_ncone.py` | `check_ncone.txt` | PC.20 search over 4-cone pillows |

## Summary table

| id | grade | one-line reason | in paper? |
|---|---|---|---|
| PC.0 | NONE | orbifold Gauss–Bonnet | yes |
| PC.1 | MINOR | Theorems A–C and Cor D are correct. "No longer determine every pillow once the sum reaches 18" can be read as "at every S ≥ 18", but sums 19, 21–25, 27–30, … have no collision | yes, reword |
| PC.2 | NONE | agrees with DGGW (5.7). 271/360 re-derived from the exact spectrum of S²/I | yes |
| PC.3 | MINOR | the integer powers of t are attributed to constant curvature. They actually follow from the orbifold structure (any smooth metric) | yes, reword |
| PC.4 | NONE | proved via Vieta, for general m | yes |
| PC.5 | NONE | follows from PC.4 | yes |
| PC.6 | NONE | DGGW 5.3/5.5/(5.7) | yes |
| PC.7 | MINOR | eq:s1inv is correct. rem:bugfix records an internal error and has no mathematical content | eq: yes; remark: drop |
| PC.8 | NONE | eq:b1 = DGGW (5.10) = Schueth Rem 4.2 = Uçar C_1. eq:a2red is exact. The P_3 weight is −1/360 | yes |
| PC.9 | NONE | AM–HM | yes |
| PC.9b | NONE | e3 = (P3 − S1³)/(3(1 − S1R)), and S1R ≥ 9 | yes |
| PC.10 | NONE | Jacobian confirmed symbolically | yes |
| PC.11 | MINOR | "maximum at the spread triad (p,p,S−2p)" is false for p = 2, where that triad is not hyperbolic | yes, add p ≥ 3 / p=2 caveat |
| PC.12 | MINOR | R⁺_{S,2} is not attained. "Fill [R⁻,R⁺]" misdescribes a finite set | yes, reword |
| PC.13 | NONE | Schur-convexity; the balanced triple is majorised by all others | yes |
| PC.14 | NONE | proved and brute-forced | yes |
| PC.15 | NONE | every constant reproduced exactly | yes |
| PC.16 | NONE | a0(3,3,4) = 107/144 is the global minimum | yes |
| PC.17 | **SERIOUS** | "localizes every degeneracy … to contacts between adjacent least-order strata" is false. 2793 of 3067 pairs with S ≤ 600 join non-adjacent strata, including the paper's own S=36 pair | prop:scaling: yes; the localisation sentence: no |
| PC.17b | NONE | scaled copies at 18k | yes |
| PC.18 | NONE | both S=36 fibres confirmed (one is non-adjacent, strata 6 and 8) | yes |
| PC.19 | **SERIOUS** | the table and the 2.03 exponent are reproduced (pair count), but conj:density is contradicted to S=6000, the birthday heuristic miscounts the R-values (S⁶, not S³), and the method sentence repeats the PC.17 error | table: yes (as data to 600); heuristic, conjecture, "quadratic-order" claims: **no** |
| PC.20 | **SERIOUS** | an explicit 4-cone pair agrees in the first three coefficients, contradicting "neither a construction". The upper bound K ≤ n for n ≥ 4 is asserted without proof | no, as worded |
| PC.21 | NONE | claim verified. 83 triads; a reference listing is supplied | yes |
| TH.0 | NONE | all endpoint, nonemptiness and truncation facts confirmed (S ≤ 700) | n/a (note) |
| TH.1 | NONE | proved | yes |
| TH.2 | NONE | proved (chain) | yes |
| TH.3 | NONE | proved for all p (closed form, odd cubic, 3p+7 branch) | yes |
| TH.4 | NONE | proved and enumerated | yes |
| TH.5 | NONE | all 14 rows reproduced exactly | yes |
| TH.6 | MINOR | true. Part (1) needs the explicit restriction S ≥ 3p+3, because at S = 3p+2 the formal equality holds for every p | yes, add qualifier |

No FATAL findings.

---

## Heat-coefficient items (PC.2, PC.3, PC.6–PC.10, PC.1 Cor D)

**Literature formulas, checked symbolically (`check_heat.py` A–C).**
- Uçar (4.25) and (4.33) give the cone contribution of an order-k cone point, symbolically in k:
  - C_0 = (k²−1)/(12k);
  - C_1 = κ (k²−1)(k²+11)/(360k) = κ[(k³−1/k)/360 + (k−1/k)/36];
  - C_2 = κ²(k²−1)(2k⁴+9k²+37)/(5040k).

  This matches cor:conevals and eq:b1 exactly, and deg p_ℓ = 2ℓ+2 holds.
- Uçar (4.35) gives a_ν/vol = 1, κ/3, κ²/15.
- DGGW gives b_0(γ^j) = 1/(4 sin²(jπ/m)) (5.3), the degree-zero term χ/6 + Σ(m²−1)/(12m) (5.7), and the cone term R1212 (m⁴+10m²−11)/(360m) (5.10). The last equals eq:b1 with R1212 = K.
- Schueth, Rem 4.2, gives the same a_0 and a_1. Her b_1(Φ) = 2K(2−2cos φ)⁻² is identical to DGGW's K/(8 sin⁴).
- The trigonometric sums Σcot², Σcsc² and Σcsc⁴ follow from Vieta and Newton applied to Im(x+i)^m = 0. They are proved symbolically in m and checked exactly for m ≤ 150.

**Independent derivation (D).** I computed the heat trace of the round orbifolds S²/G (G = C_n for n ≤ 30, D_n for n ≤ 15, and T, O, I) exactly from the multiplicities d_l = (2l+1)/|G| + |G|⁻¹ Σ_axes (m−1−2(l mod m)). The expansion uses Hurwitz zeta values at negative integers. This yields:
- S² itself: 1/t + 1/3 + t/15.
- For every group, t⁻¹ = χ/2, t⁰ = χ/6 + Σb_0 and t¹ = χ/30 + Σb_1|_{K=+1}.
- S²/I: a_0 = **271/360**. Direct summation at t = 1e-4 agrees to 1e-10.

Neither DGGW nor Uçar is used in this derivation. b_1 is linear in K: by Uçar's Thm 4.20 proof (Donnelly's φ·ψ structure) it is ψ times a universal polynomial that is linear in curvature. The K=+1 values therefore fix K=−1.

**Smooth constants at K=−1** (Area = 2π(1−R)):

| power | smooth term | where it enters |
|---|---|---|
| t⁻¹ | (1−R)/2 | Area/(4π), the whole coefficient |
| t⁰ | (R−1)/6 = χ/6 | eq:a0conv, eq:s1inv |
| t¹ | (1−R)/30 | Uçar (4.35), a_2 = vol·K²/15 |

So the full t¹ coefficient is 1/30 − P3/360 − S1/36 − R/360 (verified). eq:a2red is exact. Modulo (S1, R), the third coefficient delivers P3 with nonzero weight −1/360.

- **PC.2:** NONE. The (2,3,5) arithmetic is χ/6 = 1/180 and Σcone = 269/360, giving 271/360.
- **PC.3:** MINOR.
  - Integer powers only. This is true, but the stated reason ("because the cones have constant curvature … no curvature blow-up") is wrong. Schueth p. 13 and DGGW Thm 4.8 show that a cone point of any smooth orbifold metric is a 0-dimensional stratum, so it contributes t^{0+ℓ}. Half powers arise only from mirror strata.
  - Fix: "Because each cone point is a zero-dimensional stratum of a smooth orbifold, …".
  - The cited suleymanova2017 / nrs2024 / schueth2025 were not available (`fetches.md`).
- **PC.6, PC.7 (eq:s1inv), PC.8:** NONE.
  - The footnote attributions to Schueth Rem 4.2 / Rem 3.2 / eq. (17), DGGW §5.6 and Uçar are all accurate.
  - "b_1 = 0 at K=0" follows from linearity.
- **PC.7 rem:bugfix:** MINOR (editorial). The arithmetic is right: the wrong inversion gives −209/15 at (2,3,5), while eq:s1inv returns 10. But a published paper should not record a discarded internal error. Fix: delete the remark.
- **PC.9, PC.9b:** NONE.
  - Newton's identity gives P3 = e1³ − 3e1e2 + 3e3. With e2 = R·e3, this gives e3 = (P3 − e1³)/(3(1 − e1R)), where 1 − e1R ≤ −8 ≠ 0.
  - The result holds for all positive reals, not only hyperbolic triads.
  - Exhaustive injectivity was checked for all orders ≤ 120.
  - "Equivalently, three coefficients are injective" uses the −1/360 ≠ 0 of PC.8, as the paper says.
- **PC.10:** NONE. det DF = −3(p−q)(p−r)(q−r)(p+q)(p+r)(q+r)/(p²q²r²), confirmed by sympy.
- **PC.1:** MINOR (wording only).
  - Theorem A: no collision for S ≤ 17. Proved here and enumerated.
  - Theorem B: S=18 has exactly one collision.
  - Theorem C: P3(2,8,8) = **1032** and P3(3,3,12) = **1782**, so the t¹ coefficients differ and K = 3 for the pair.
  - Corollary D: correct.
  - Fix: "the bound is sharp: the first failure occurs at S=18". Sums 19, 21–25, 27–30, 33, … have no collision (computed from `data/summary_10_6000.txt`; the last collision-free sum is S=557, and every 558 ≤ S ≤ 6000 has a collision).

## Threshold items

### Independent proof of Theorem 1 (TH.3), all p

Set D = S − p. Throughout, S ≥ 3p+3, so D ≥ 2p+3, D − p − 2 > 0, and stratum p+1 is nonempty.
- R⁻_{S,p} = 1/p + 1/⌊D/2⌋ + 1/⌈D/2⌉ is attained.
- R⁺_{S,p+1} = 2/(p+1) + 1/(D−p−2) is attained because p+1 ≥ 3.

**Even D.** The gap has the closed form

  gap_p = −(D−2p−2)·(D(p−1) − 2p(p+2)) / (D·p(p+1)·(D−p−2)).

The first factor is positive, so gap ≤ 0 exactly when D ≥ 2p(p+2)/(p−1), that is, when S ≥ x*(p) = 3p(p+1)/(p−1) = 3p+6+6/(p−1). This also equals φ_p(S) − τ_p.

**Odd D.** Here 1/⌊D/2⌋ + 1/⌈D/2⌉ = 4D/(D²−1), so gap_odd = (even formula) + 4/(D(D²−1)). Multiplying by p(p+1)(D²−1)(D−p−2) > 0 gives the cubic

  g(D) = −(p−1)(D²−1)(D−p−2) + p(p+1)(3D² − 4(p+2)D + 1),

which has leading coefficient −(p−1) < 0. Its values at test points are:

| D | g(D) | sign |
|---|---|---|
| −1 | 4p(p+1)(p+3) | > 0 |
| 1 | −4p(p+1)² | < 0 |
| p+2 | −p(p+1)²(p+3) | < 0 |
| 2p+3 | 8(p+1)² | > 0 |
| 2p+6 | 2(p²+26p+70) | > 0 |
| 2p+7 | −8(p²−5p−30) | see below |

So g has one root in (−1,1), one in (p+2, 2p+3), and its largest root D_o(p) in (2p+3, ∞). On D ≥ 2p+3, g > 0 before D_o and g < 0 after. This is the monotonicity of the odd-parity sign. The odd gap is not monotone as a function, but its sign changes exactly once, which is all that is needed.

**Exceptional branch p ≥ 9.** The factor p² − 5p − 30 has roots (5 ± √145)/2, so it is positive exactly when p ≥ 9 (the larger root is 8.52). Hence for p ≥ 9, g(2p+7) < 0 < g(2p+6), which puts D_o ∈ (2p+6, 2p+7). For p ≥ 8, 3p+6 < x* < 3p+7, so the first even-D overlap is at 3p+8. The odd sum S = 3p+7 (D = 2p+7) is therefore the first overlap, and every later S overlaps. This gives S* = 3p+7.

**p ≤ 8.** Here g(2p+7) > 0, so the even branch decides. All odd-D sums in [x*(p), S*(p)) and their exact gaps:

| p | x* | S* | odd-D sums in [x*, S*) with exact gap | first odd-D overlap |
|---|---|---|---|---|
| 2 | 18 | 18 | none | 19 |
| 3 | 18 | 19 | S=18, gap **1/840** | 20 |
| 4 | 20 | 20 | none | 21 |
| 5 | 45/2 | 23 | none | 24 |
| 6 | 126/5 | 26 | none | 27 |
| 7 | 28 | 29 | S=28, gap **1/2310** | 30 |
| 8 | 216/7 | 32 | S=31, gap **1/10296** | 33 |

In each case the first odd-D overlap is at S*+1. The overlap set is therefore exactly {S ≥ S*}, and none of these values is 3p+7, as claimed. The p = 2 truncation is harmless: the hull of stratum 2 has its actual maximum < 1 as upper end, and that maximum is ≥ R⁻_{S,3} (verified).

**Brute force.** Overlap was computed from the definition: hulls of the actual value sets, every triad enumerated, and no monotonicity assumed. It equals [S ≥ S*(p)] for every 2 ≤ p ≤ 232 and 3p+3 ≤ S ≤ 700. Lemma 1 agrees on the same range. The parity description of S* was checked for p < 2000.

- **TH.0, TH.1, TH.2:** NONE.
  - TH.1: the second hull condition R⁻_{p+1} ≤ max_p is automatic, because R⁺ is non-increasing in p for p+1 ≤ S/3. For p = 2 it follows from (2,3,S−5) when S ≥ 12 and from a direct check at S = 11.
  - TH.2: the chain R⁻_p > R⁺_{p+1} ≥ R⁻_{p+1} > … over contiguous nonempty strata.
- **TH.3:** NONE.
- **TH.4 (Cor 2):** NONE.
  - Proof: for S ≤ 17 every adjacent pair has S < S*(p). Only p ≤ 4 has S ≥ 3p+3, and S*(2,3,4) = 18, 19, 20. Lemma 2 then applies.
  - At S = 18 only (2,3) overlaps, since S*(3) = 19, S*(4) = 20, S*(5) = 23. Its window is 1+1:
    - (2,7,9) has R = 0.754 > 3/4;
    - (3,4,11) has R = 0.674 < 3/4.
  - So the single collision is (2,8,8)/(3,3,12). Enumeration confirms this.
- **TH.5:** NONE. All 14 rows are reproduced exactly: S*, first collision, gap, both window counts, and the pair. Enumeration to 600 gives 2977 fibres, matching the text.
- **TH.6 (Prop 3):** MINOR. See the P4 verdict.

## Paper-core threshold items

- **PC.11:** MINOR. lem:chamber holds: R′ = −1/q² + 1/r² ≤ 0, and R is strictly decreasing (brute force to S ≤ 700). But "attains its maximum at the spread triad O(p,p,S−2p)" is false for p = 2, where that triad has R = 1 + 1/(S−4) > 1. It is also false for (S,p) = (9,3). Fix: state it for the stratum including non-hyperbolic points, or add "for p ≥ 3; for p = 2 the maximum is the largest hyperbolic value" (as TH.0 does).
- **PC.12:** MINOR. The R⁺ formula, the monotonicity in p (for p ≤ S/3) and lem:bound (equality iff S−p even) are all correct. Fix: "the reciprocal sums lie in [R⁻, R⁺] and are pairwise distinct" instead of "fill". Also note that R⁺_{S,2} is a formal value only.
- **PC.13, PC.14, PC.15, PC.16:** NONE. Every constant was reproduced:
  - τ: 1/6, 1/6, 3/20;
  - φ_2: 29/165 and 1/6;
  - φ_3: 7/36 and 11/63, with peaks at 10 and 13;
  - φ_4(15) = 9/55;
  - R⁻ vs R⁺ at S=18: 101/168 vs 3/5, 15/28 vs 21/40, 107/210 vs 1/2;
  - a0(3,3,4) = 107/144 (every S ≥ 11 gives a0 > 3/4).
- **PC.21:** NONE.
  - 10 ≤ S ≤ 18 has 83 triads (1, 3, 6, 7, 9, 11, 13, 15, 18 per sum).
  - R is distinct within each sum for S ≤ 17, and the only coincidence at S = 18 is the boldface pair.
  - The printed table was not available to me. `tab_enum_reference.txt` lists every triad with its exact R for comparison in phase 2.

## Enumeration, density and conjecture (PC.17–PC.19)

**Method.** C program with exact 128-bit cross-multiplication. Fibres agree line by line with pure Python for S ≤ 600. Sums 10 ≤ S ≤ 6000 are covered.

**Counting convention.** The paper's N(S) is the number of **pairs**: a fibre of size k counts C(k,2). Fibres of size 3 first occur at S = 136, and the largest size found is 6.

| S | claimed 𝒩 | pairs | fibres (classes) | primitive fibres (gcd 1) | adjacent-strata pairs |
|---|---|---|---|---|---|
| 18 | 1 | 1 | 1 | 1 | 1 |
| 100 | 92 | 92 | 92 | 69 | 38 |
| 200 | 386 | 386 | 380 | 243 | 88 |
| 300 | 840 | 840 | 822 | 507 | 132 |
| 400 | 1496 | 1496 | 1468 | 900 | 187 |
| 500 | 2210 | 2210 | 2158 | 1302 | 224 |
| 600 | 3067 | 3067 | 2977 | 1714 | 274 |

- The table matches the pair convention exactly; the N/S and N/S² columns also match.
- The OLS slope of log 𝒩 on log S over the integers 50 ≤ S ≤ 600 is **2.028** for pairs and 2.015 for fibres. The 2.03 claim is reproduced, but it is fragile: on the seven table checkpoints the slope is 1.96.
- S = 36 has exactly the two stated fibres (R = 3/8 and R = 3/10).

**PC.17:** SERIOUS.
- prop:scaling and thm:density-lower are correct. In thm:density-lower the copies at 18k are distinct, so 𝒩(S) ≥ ⌊S/18⌋.
- The sentence "the interval-separation mechanism … localizes every degeneracy at sum S to the finitely many contacts between adjacent least-order strata" is false:
  - Of 3067 pairs with S ≤ 600, only 274 join adjacent strata; 2793 join strata with least orders differing by ≥ 2.
  - The first such pair is the paper's own S = 36 example, (6,15,15) with least order 6 and (8,8,20) with least order 8.
  - Interval separation gives no localisation once S ≥ S*, because then all strata overlap.
- PC.19 repeats the claim: "computed … via the interval-localization".
- My counts agree with the table, so the data were evidently computed by full enumeration. The description of the method is what is wrong.
- Fix: "N(S) is computable by exhaustive enumeration of the O(S²) triads of sum S". Delete the localisation claim, and state that N counts unordered pairs (fibres of size up to 6 occur).

**PC.19:** SERIOUS.

(a) **conj:density is contradicted by the data.** Over 100 < S ≤ 6000, 𝒩(S)/S² decreases steadily:

| S | 𝒩(S) (pairs) | 𝒩/S² |
|---|---|---|
| 400 | 1496 | 0.00935 |
| 1000 | 7641 | 0.00764 |
| 2000 | 25042 | 0.00626 |
| 4000 | 77203 | 0.00483 |
| 4800 | 102719 | 0.00446 |
| 6000 | 145679 | 0.00405 |

- The local exponent falls throughout: OLS on [600,1200] gives 1.78, [1200,2400] gives 1.69, [2400,4800] gives 1.60, [3000,6000] gives 1.58. Fibres behave the same way.
- Even 𝒩/(S² log S) decreases.
- The per-sum mean N(S)/S falls from 0.0155 (S≈550) to 0.0064 (S≈5950), so the "equivalent" form N(S) = Θ(S) fails too: N(S) grows roughly like S^0.6 over this range.
- The phrase "positive proportion, of order 1/S" is self-contradictory.
- Verdict: the data do not support the conjecture, and its stated equivalent N(S) = Θ(S) is contradicted. **Do not include it.**

(b) **The heuristic miscounts.**
- A reduced fraction in (0,1) with denominator ≤ X can take ≍ X² values, so the number of possible values of R is ≍ (S³)² = S⁶, not O(S³).
- The birthday count then predicts O(S⁻²) coincidences per sum, the opposite of the claim. The observed collisions are structural (common factors, parametric families), not random.
- Remove the heuristic.

(c) Further claims to remove:
- "Numerical evidence for substantially higher (quadratic-order cumulative) density".
- "N(S)/S² stabilizes …", unless explicitly limited to S ≤ 600 and qualified by the extended data.
- "Primitive collisions appear at almost every sum beyond 18" is loose: 507 of the 582 sums in 19..600 have one. Say "at most sums" or give the proportion.

Fix: keep the exact table as data. Optionally report the S ≤ 6000 data and state the growth exponent as an open question (empirically between 1.5 and 1.6 at the top of the range, still decreasing).

**PC.20:** SERIOUS (as worded).
- For n cone points, the order-t^ℓ cone term is κ^ℓ·(1/m)·p_ℓ(m), with p_ℓ even of degree 2ℓ+2 (Uçar; C_0, C_1, C_2 above). The first n coefficients are therefore equivalent to the power sums (p₋₁, p₁, p₃, …, p_{2n−3}).
- **Lower bound.** `check_ncone.py` finds 4-cone hyperbolic pillows that agree in p₋₁, p₁ and p₃, and hence in the first three heat coefficients:
  - (3,10,15,30) and (4,5,21,28): both have p₋₁ = 8/15, p₁ = 58, p₃ = 31402;
  - 8 such pairs with orders ≤ 80.
  - None of these pairs agrees in p₅, so each has K = 4 exactly.
  - So the statement "we have neither a construction nor a non-existence proof" for K ≥ n is wrong at n = 4.
- **Upper bound.** "When these are independent they recover the multiset, so K ≤ n" conflates functional independence with injectivity, and no proof is given. The search found no 4-coefficient collision with orders ≤ 80, but that is not a proof.
- Fix: report the n = 4 construction, and state K ≤ n for n ≥ 4 as an open question (or prove it).

---

## P4 verdict

**Theorem 1 (TH.3): correct for all p ≥ 2.** I proved it independently (above):
- the closed-form even gap, giving threshold x*(p) for even D;
- the odd-D cubic g, whose single sign change on D ≥ 2p+3 replaces monotonicity of the gap;
- g(2p+7) = −8(p²−5p−30), which yields the special sum 3p+7 for exactly p ≥ 9;
- the exact p ≤ 8 case table.

Brute force from the definition agrees for all p ≤ 232 and S ≤ 700. S*(p) is correct for every p checked.

**Proposition 3 (TH.6).**
- **(1) Correct, with one qualifier needed.**
  - Even D: the gap vanishes iff D = 2p(p+2)/(p−1) = 2p+6+6/(p−1). This is an integer iff (p−1) | 6, i.e. p ∈ {2,3,4,7}, and the quotient is even only for p ∈ {2,4} (D = 16, 16; S = x* = 18, 20). For p = 3 and p = 7 the quotients 15 and 21 are odd, so x* has the wrong parity.
  - Odd D: there is no integer zero. For p ≥ 9, D_o ∈ (2p+6, 2p+7), an open interval between consecutive integers; 145 is not a square, so g(2p+7) ≠ 0. For p ≤ 8, g ≠ 0 was checked exactly at every odd D up to 400, and g < 0 beyond D_o.
  - Brute force: the only tangencies with S ≤ 700 are (2,18) and (4,20).
  - Qualifier: the even numerator has a second root D = 2p+2 (S = 3p+2), where the "spread triad of stratum p+1", (p+1,p+1,p), is the balanced triad of stratum p itself. Fix: add "with S ≥ 3p+3 (both strata nonempty)".
- **(2) Correct.**
  - For p ≥ 9 in general: at S* = 3p+7 the window is exactly 1+1, because
    - R(p,p+2,p+5) − R⁺_{p+1} = 2/(p(p+1)(p+2)) > 0, and
    - R⁻_p − R(p+1,p+2,p+4) = 1/(p(p+1)) − 1/((p+2)(p+3)) > 0.

    The only candidate pair has gap ≠ 0 by (1), so there is no collision at S*. Before S* there is no overlap, so there is no collision.
  - For p ∈ {3,5,6,7,8}, by direct check at S*:

    | p | S* | window | stratum-p triads | stratum-(p+1) triads | collisions |
    |---|---|---|---|---|---|
    | 3 | 19 | 2+1 | (3,7,9), (3,8,8) | (4,4,11) | 0 |
    | 5 | 23 | 1+1 | (5,9,9) | (6,6,11) | 0 |
    | 6 | 26 | 2+1 | (6,9,11), (6,10,10) | (7,7,12) | 0 |
    | 7 | 29 | 2+1 | (7,10,12), (7,11,11) | (8,8,13) | 0 |
    | 8 | 32 | 2+1 | (8,11,13), (8,12,12) | (9,9,14) | 0 |

  - Enumeration: for all 116 values of p with an adjacent collision at S ≤ 2000 (p up to 455), the first collision is > S* except at p = 2 and 4.
- **Corollary 2:** proved and enumerated.
- **TH.5:** every row reproduced.

Grade for P4: **NONE** for TH.3, TH.4 and TH.5; **MINOR** for TH.6 (qualifier only).
