<!-- Round 10, B-c, returned text saved verbatim: returned text saved verbatim; the reviewer could not write files -->

I could not save the report to REPORT.md because the write was refused, so the full report is below. Sections 4, 5, 6 and 8 contain no mathematical error that I could find. Every number I could recompute matches. I recommend **minor revision**, with high confidence on correctness and medium confidence on significance. The main issue (M1) is that the abstract and Remark 8.6 compare a lower bound and an upper bound on N that belong to different accuracy regimes. My working files are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-10/B-c-weyl-law-remainder-analyst/scratch/ (code/, pages/, lit/).

# Referee report (AGAG): "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Assignment: Sections 4, 5, 6 and 8. I checked every proof in these sections line by line, including each explicit constant, and recomputed every number I could. The marked placeholders (author contributions, AI-use statement, Zenodo DOIs, preprint identifiers) are treated as known. Page numbers refer to the submitted PDF (41 pp.). I read the rendered pages before reporting any typographical or figure point. I did not open the authors' code deposit. All my recomputations were done independently in mpmath (30 to 60 digits) from the formulas printed in the manuscript.

## Summary

The paper takes a closed orientable hyperbolic 2-orbifold in the class C(A, ε, M) (area at most A, systole at least ε, cone orders at most M). It shows that the first N eigenvalues, each known to within δ, determine the signature, with N and δ given by closed formulas (Theorem 6.2).

The proof has four ingredients:
- a lower bound for the gap |G_σ − G_σ'| between signature terms at small time, from the first differing heat invariant (Lemma 6.1);
- a count of closed geodesics in terms of A, ε and M only (Lemmas 4.2, 4.3 and 4.5), which controls the hyperbolic term;
- a heat-trace (Chernoff-type) eigenvalue count and tail bound (Proposition 5.2);
- a perturbation estimate.

The closed-form constants are astronomically large (Table 5: up to N ≈ 4×10^30 and δ ≈ 10^-277). Corollary 6.4 and Proposition 6.5 replace Lemma 6.1 by a gap certified in ball arithmetic at a moderate time. This gives N of order 10^2 to 4×10^5 with δ between 2×10^-6 and 6×10^-4 for six explicit classes.

Section 8 shows that the order bound cannot be dropped. The triangle orbifolds O(2,3,m) have a uniform systole bound (via a self-contained proof of Jørgensen's inequality in the hyperbolic case) and eigenvalues λ_j ≤ 1/4 + π²(j+1)²/h_m². Pigeonhole then gives a lower bound for N in terms of M. Section 8 also discusses whether the systole bound is needed (Problem 1), using an explicit collar construction for a pinching family.

## Significance

What is good:
- The paper is careful, honest about what is proved and what is observed, and unusually explicit.
- Every inequality I checked is correct with the stated constants.
- The certified-gap route (Corollary 6.4 and Proposition 6.5) is the right way to make the method usable, and the numbers in Tables 3 and 4 are reproducible.
- Section 8.1 is a clean, self-contained and correct construction: the uniform systole bound for O(2,3,m) through Jørgensen, the cone-ball test functions, and the pigeonhole argument.

The reservations are about weight:
1. The general Theorem 6.2 is an effectivisation of a soft compactness argument. Its constants have no practical meaning, as the authors say themselves (p. 3, p. 5).
2. The usable content is Proposition 6.5. It is a finite certified computation for six classes, and it is conditional on the user supplying a complete list of eigenvalues with index-wise enclosures. Section 7 concedes this cannot currently be done for these orbifolds.
3. The structural input (Sections 2 and 3, Appendix A) is shared with a companion paper submitted at the same time. The editor should see both papers and judge the overlap.
4. Of the four "new" items (p. 3), the closed-geodesic count (Lemma 4.5) is correct but very crude (C* ~ M^9 ε^-4; see M2). The lower bound on N versus M is stated against an upper bound that lives in a different accuracy regime (M1).

For AGAG I consider the paper publishable in principle: it is correct, explicit and well documented. Its contribution is incremental. The editor should weigh the significance concerns above.

## Correctness, and what I recomputed

**Section 4**
- Lemma 4.1 (H1)–(H3): I re-derived all three, including both distance-moved formulas and the sign argument in (H3).
- Lemma 4.2: Every step holds:
  - the defect bound π/(abc);
  - cos((θ−α−β)/2) ≥ sin(π/2M) ≥ 1/M;
  - sin α sin β ≤ π²/(ab), giving cosh d − 1 ≥ 2/(π²cM).
- Lemma 4.3: The injectivity radius argument holds, as do ε ≥ 4ρ1 and ρ1 ≤ r0.
- Theorem 4.4: The closed form v0 ≥ πr0²/max(M, M²/4) is correct. The step arccosh(1+x) ≥ √(2x/(1+x)) holds; I checked it on [10^-8, 10^3]. The resulting arccosh(1+2/(π²M²)) ≥ 0.6/M holds for all M ≥ 2.
- Lemma 4.5: The covering, coset-packing and axis arguments are correct. The constant C* matches the formula.
- Table 2: all twelve values of D reproduce exactly (56.6, 1125, 6.37e5; 150.9, 3001, 1.70e6; 640, 3184, 1.70e6; 1132, 2.25e4, 1.27e7). The closed form is above D in every case.
- C* ranges over 4.01×10^5 to 7.09×10^10 across Table 5.
- πe^{3D}/A ranges over 3.38×10^196 to 2.38×10^29325. Both ranges are as stated on p. 13.

**Section 5**
- Lemma 5.1: the case analysis checks: 1/12, 1/42, 1/20, 1/10, 1/6, 1/2. So do n + 4g ≤ Area/π + 4, b0(m) = (m²−1)/(12m) (from ∫ e^{−ar}/(1+e^{−2πr}) dr = 1/(2 sin(a/2))) and I(t) ≤ e^{−t/4}Area/(4πt).
- Proposition 5.2 is correct.

**Section 6**
- Lemma 6.1 is correct. This includes the k = 1 case, where Q(0) and t^{-1} appear. It also includes the requirement t ≤ 1, used for t^{k−2} ≥ t^{k*−2}.
- I spot-checked the enveloping property of Proposition 2.3, which Lemma 6.1 relies on, for m = 2, 3, 8, 12; K ≤ 4; and t ∈ {0.01, 0.05, 0.2}. I also checked it for (4π/Area)·I with K ≤ 5. Signs and moduli hold in every case. |b_K(m)| is increasing in m for 2 ≤ m ≤ 14 and K ≤ 4.
- Theorem 6.2 is correct:
  - the factor 3 ≥ 1 + 2t/(ε−t) on (0, t2];
  - monotonicity of B* on (0, t2];
  - the reduction to e^{−y}y^p ≤ (γ*/16ϖ)(ε²/4)^p and the formula for y0;
  - Λt* ≥ 2 log 64;
  - the tail bound equal to exactly Θ*/8;
  - the perturbation bound Θ*/(8e);
  - the total 1/4 + 1/(8e) < 3/8.
- Remark 6.3: the arithmetic 1/4 + 1/(8e) + 1/8 < 1/2 is correct. So is the replacement bound e^{−Λo t*}.
- Corollary 6.4 is correct as stated, with Θ ≤ 8 and Λt ≥ 1 as the only extra hypotheses.
- **Table 5:** I recomputed all eight rows: k*, C*, t1, t3, Θ*, Λ, N, δ and the binding constraint. Every entry agrees with the stated rounding conventions. In every row the minimum defining t1 is attained at k = k*, as Remark 6.6(a) says. Further checks:
  - Without k* ≤ M, the A = 10π, M = 3 row gives N = 4.19×10^18 (p. 18: "about 4×10^18").
  - For A = 4π/3, M = 3, t3 binds from ε = 0.44 downwards (t1 still binds at 0.45).
  - From ε = 0.42 the per-halving factors of N are 5.239, 5.127, 5.008, 4.902, 4.812, 4.737, 4.674 (p. 18: "from 5.24 to below 4.7 over seven halvings"). C* grows by about 14 to 15 per halving, approaching 16 (ε^-4).
- **Tables 3 and 4:** From the printed t and Θ I recomputed B*(t), Θ/8, Λt, N and δ for all six rows. All agree; the smallest margin is row 3, B* = 0.01793 against Θ/8 = 0.0190. More importantly, I computed every G_σ(t) independently over all of Sig(A, M) by mpmath quadrature at 30 digits:
  - |Sig(A, M)| = 27, 48, 8, 8, 281, 12, as printed.
  - The least pairwise gaps are 0.01588232, 0.006527298, 0.1520293, 0.1655108, 0.001373851 and 0.1666487. These match the certified lower bounds of Table 4 to all printed digits.
  - The minimising pairs agree with Table 4 up to the equal-gap pairs the text itself mentions, for example (0;2,3,8)/(0;2,4,5) in row 1.
- **Trace formula normalisation (independent check):** I used the 40 eigenvalues of Table 7. For O(2,8,8) at t = 0.1 I get Σ_{j≤40} e^{−λ̃_j t} − G_σ(t) = 4.202×10^-6. The contribution of the systole class and its inverse alone is 4.192×10^-6. For O(3,3,12) the two values are 2.5867×10^-4 and 2.5869×10^-4. This confirms Theorem 2.1 with its normalisation, and the spectra, to about four digits.
- **Figure 1 and the triangle rows of Table 8:**
  - Running Theorem 7.1 myself (instance diameter bound), I reproduce (C1) with N = 18 at t ≈ 0.0565 and (C2) with N = 20 at t ≈ 0.0556 for O(2,8,8). For O(3,3,12) I get (C1) with N = 25 and (C2) with N = 29.
  - The shaded times of Figure 1 for N = 21 (s-grid kt/20) are exactly 0.0501 and 0.0562 of the 61-point grid.
  - H(0.0562) = 6.86×10^-3, matching the 6.8×10^-3 on p. 25.
  - Example on p. 18: d3 = 25/12 for (2,8,8) against (3,3,12) is correct.
  - Remark 6.6(a): I confirmed that the stated area 12π pair shares c1–c3 (same area, Ψ1 = 54, Ψ2 = 2430) and differs at c4. Exhaustive enumeration confirms that no two signatures first differ beyond k = 3 for (A ≤ 4π, M ≤ 10), (A ≤ 2π, M ≤ 30) and (A ≤ 6π, M ≤ 6).
- p. 18: |b_K(M)| / (K^{-1/2} K! (M/π)^{2K}) is about 0.34, roughly constant for M = 12 and K = 1, …, 9, as stated.

**Section 8**
- Lemma 8.1: I re-derived it.
  - The identity tr[A,B] − 2 = −bc(u−u^{-1})², and the recursion for B_{n+1} and x_{n+1} hold.
  - The non-vanishing argument holds, including the parabolic commutator case.
  - The choice of k_n and the convergence C_n → A hold.
- The trace identity tr[γ,β] − 2 = 4 sinh²(L/2) sin²(φ/2) cosh² r, and the off-diagonal entries ±sin(φ/2) cosh r, were checked numerically.
- Proposition 8.2: correct throughout (folding, cone ball, systole argument). Further checks:
  - ℓ_{2,3} = 0.5620669 (cosh 2s∞ = 5/3).
  - h_7 = 0.54527.
  - 2 arccosh((1+2cos(2π/7))/2) = 0.983987 and 2 arccosh(3/2) = 1.924847.
- Identity (3): both cases of q check. The Rayleigh-quotient arguments of Propositions 8.3 and 8.7 hold, including the closed form ∫₀^a ρ² cosh ρ dρ = (a²+2) sinh a − 2a cosh a. Pigeonhole, Remark 8.4, Corollary 8.5 and the A < π/3 argument are all correct.
- Remark 8.6: the exponents follow from the formulas. Numerically (A = π/2, ε = 1, M = 64, …, 512) the per-doubling exponents are 9.25, 9.21, 9.19, 9.17 for N and 26.25, 26.21, 26.19, 26.17 for δ^-1, approaching 9 and 26. C* has exponents 8.92, 8.96, 8.98, 8.99.
- The Garbin–Jorgenson condition (a) quoted on p. 30 (radius arccosh(1 + εm/2π), ε < 1/2, [16, §2]) and their Corollary 5.5, Theorem 5.7 and Example 5.8 are cited correctly. I checked against arXiv:1603.01494. The m ≥ 13 verification is correct. Incidentally, [16, Ex. 5.8] says G_N has "three elliptic points of order 2, 3, and N". The manuscript's description (one cusp, orders 2 and N) is the correct one, so nothing is needed here.
- Section 8.2: the areas of (0;3,3,3,3), (1;3) and (0;2,2,6,6) are each 4π/3. The Euler-characteristic arguments (−2π/3 < 0; area 0 for the disc with two order-2 points) are correct. For ϑ = 0 and 2.8, 4b = 2.633915 and 0.69404, matching Table 6.

I found no mathematical error in Sections 4, 5, 6 or 8.

## FATAL

None.

## MAJOR

**M1 (pp. 1–2 abstract, p. 3, p. 30 Corollary 8.5 and Remark 8.6): the lower bound and the "upper bound" for N versus M are for different quantities, and the paper presents them as bracketing one unknown growth rate.**

- Corollary 8.5 bounds N from below at fixed δ: (N−1) log(c'N²/δ + 1) ≥ log(M−6).
- The polynomial N of Remark 8.6 comes with δ^-1 = O(M^{26}) (at n* = 4).
- At the theorem's own accuracy, δ ≈ M^{-26}, Corollary 8.5 gives only (N−1)·26 log M ≳ log M, that is N ≥ 2. Conversely, at fixed δ the paper gives no N at all.
- The compactness argument on p. 3 also produces δ as a function of N, not N as a function of δ. Whether any finite N works at a fixed small δ is not addressed. For same-area pairs that first differ at k ≥ 3, the heat trace does not force max_j |λ_j − λ'_j| to exceed a fixed δ.

So the abstract's "… needs N growing at least like log M/log log M, while the N of the theorem grows at most polynomially in M" is misleading. So is the closing sentence of Remark 8.6: "Between the lower bound log M/log log M … and this polynomial we do not know the true growth."

*Resolution:* State the lower bound as a constraint on the pair (N, δ), and compare it with the theorem's pair (N, δ) ≈ (M^9, M^{-26}) in the same terms. Say explicitly that no N for fixed δ is provided, and reword the abstract and Remark 8.6 accordingly. Optionally, record the trade-off curve that Corollary 8.5 actually gives.

**M2 (p. 3 "What is new"; Sections 4.2 and 6): the claimed contributions should be weighed against what is actually usable, and the geometric count should be either sharpened or presented as auxiliary.**

- Lemma 4.5 is advertised as one of four new contributions. It rests on the separation d0 = min(ε/2, arccosh(1 + 2/(π²M²))) ~ 1/M, which makes C* grow like M^9 ε^{-4}.
- The paper itself expects the 1/M not to be intrinsic (p. 12). Its own tool shows this at once: the Jørgensen identity on pp. 12–13 gives, for an elliptic point of order p ≥ 7 and any other elliptic point (the pair generates a non-elementary group, since an elementary group without parabolics contains no elliptic of order ≥ 3 with two distinct fixed points), sinh² d ≥ (1/(4 sin²(π/p)) − 1)/sin²(π/q) ≥ sinh² h_p. So d ≥ h_p ≥ h_7 ≈ 0.545. This is sharp in every (2,3,p) group (see P2), and the M-dependence of the separation then reduces to the finitely many low-order configurations.
- The paper says it does not pursue this because only log C* enters t3. However, C* also drives the class-level counts of Section 7 (Table 8, "(C1), C*" and "Sig(A,M)" columns), the ε = 0.1 row of Tables 3 and 5, and the M^9 of Remark 8.6.

*Resolution:* Either prove an order-uniform (or mildly order-dependent) separation, which seems within reach, and restate Lemma 4.5 with it; or downgrade Lemma 4.5 in the "What is new" paragraph to an auxiliary crude count. In either case, the introduction should state plainly that the usable content is Proposition 6.5, and that Proposition 6.5 needs complete, index-wise enclosed spectra which nobody can currently provide for these orbifolds (as Section 7 concedes).

## MINOR

**m1 (p. 15, Theorem 6.2; p. 16, Corollary 6.4 and Proposition 6.5): needless losses in the practical constants.** These do not affect correctness, but Proposition 6.5 is presented as the usable statement, so they matter.
- (a) The tail uses s = t/2 in Proposition 5.2. Taking the infimum over s ∈ (0,t), as Theorem 7.1 already does, and keeping the rest of the argument, the N of Table 3 become 160, 183, 97, 1716, 4542 and 239122 (my computation), instead of 244, 283, 139, 2605, 7416 and 387182. That is a factor 1.4 to 1.6.
- (b) B* replaces 1 + 2t/(ε−t) by 3. At the tightest certified margin (Table 4, row 3) the exact B_C is 0.0064 against the printed B* = 0.0179.
- (c) Θ(t) = ½γ* t^{k*−2} combines the worst separation δ1 with the worst power t^{k*−2}, which never occur together. Using ½ min_k δ_k t^{k−2}, as Remark 6.6(a) mentions, raises Θ* by a factor 22 (π/2, M = 12) and 5.5 (4π/3, M = 12).
- *Resolution:* adopt (a) to (c), or state the gains in Remark 6.6.

**m2 (p. 13, Proposition 5.2 and Section 5).** The count #{λ ≤ x} ≤ e·Z(1/x) loses the factor e against Weyl's law, and so N ≈ (eA/2πt*) log(8Z♯/Θ*) is about 2e times the Weyl count at the threshold Λ. Remark 6.7 already points to the better route: compactly supported test functions below the systole give a local Weyl bound with no geodesic term. *Resolution:* state the size of this loss explicitly next to Table 3, so readers know that part of N is an artefact of the counting step.

**m3 (p. 30, Corollary 8.5).** c' is "an absolute constant" but is explicit: c' = 1/4 + π²/h_7² ≈ 33.4. *Resolution:* give it; it costs one line and makes the corollary as explicit as the rest of the paper.

**m4 (pp. 31–33, Problem 1(b)).** The natural candidate pair has two specific cusped limits:
- (0;3,3,∞) is the index-2 subgroup of PSL(2,Z), which is a congruence subgroup.
- (0;2,6,∞) is the Hecke group G_6, which I believe is conjugate to the Fricke group Γ0(3)+.

Both appear to be arithmetic. If the absence of eigenvalues in (0, 1/4) is known for them (Selberg's eigenvalue conjecture is verified at small level), then the spectral input "the spectrum of these two cusped limits below 1/4" is already available. The remaining gap would be only the lower bound λ_j ≥ 1/4 − o(1) for orbifold degenerations. *Resolution:* check this and sharpen the discussion. It would make Problem 1(b) much more concrete.

**m5 (p. 12, proof of Lemma 4.2).** "γ ≠ 1" is used without reason. It holds because L1 ≠ L3: the only line through both p̃ and q̃ is λ. *Resolution:* add the half-sentence.

**m6 (p. 30, Figure 3 paragraph).** The claim that every computed eigenvalue decreases in m is observational, and the convergence statement is conditional on GJ's condition (b). This is said clearly, but Theorem 1.2 needs neither. *Resolution:* move the conditional limit statement into a remark so it is not read as part of the result.

## Presentation

- **P1 (p. 12):** "the ball of radius 2r0 ≤ d0 < h_M": since r0 = d0/2 by definition, "2r0 ≤ d0" is an identity. Write "2r0 = d0 < h_M".
- **P2 (p. 13):** Jørgensen's inequality is said to be "attained in the (2,3,7) triangle group". In fact, for the rotations of orders p and 2 at the vertices v_p and v_2 of any (2,3,p) triangle with p ≥ 7, d = h_p and 4 sin²(π/p)(1 + sinh² h_p) = 4 sin²(π/p) cosh² h_p = 1 exactly. I checked p = 7, 8, 12 and 100. So equality holds in every (2,3,p) group, p ≥ 7. Say so, and connect it with h_p in Proposition 8.2 and with M2.
- **P3 (p. 13):** "C* enters Theorem 6.2 only through log C* in t3" should also mention that C* enters Section 7 linearly through H (cf. M2).
- **P4 (p. 18, Table 5 caption):** "N is rounded up" to two significant digits turns 4.319×10^4 into 4.4×10^4. That is correct as an upper rounding, but a reader comparing with Table 3 or Table 8 may misread it as a 2% discrepancy. Consider printing three digits.
- **P5 (p. 14, last line of Section 5):** "for O of area A" should read "of area at most A" to match its use in Section 6.
- **P6 (p. 3 and p. 30):** the two growth statements need rewording; see M1.

## Recommendation

**Minor revision**, on the condition that M1 is corrected in the abstract, the introduction and Remark 8.6, and that M2 is addressed at least by rewording.

- Confidence in the correctness of Sections 4, 5, 6 and 8: high. Every proof was checked, and every number in Tables 2, 3, 4 and 5 and in the related text was recomputed independently, together with the gaps over all of Sig(A, M) and the trace-formula normalisation.
- Confidence in the significance assessment: medium. The editor should weigh the contribution against the companion paper and against the purely in-principle nature of Theorem 6.2.

## What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | State Corollary 8.5 as a constraint on (N, δ); compare with the theorem's (N, δ) at matched accuracy; state that no fixed-δ N is given; fix the abstract, p. 3 and Remark 8.6. |
| M2 | Either prove an (essentially) order-free separation via Jørgensen and restate Lemma 4.5, or present Lemma 4.5 as an auxiliary crude count. State plainly that Proposition 6.5 is the usable result and what it requires (complete, enclosed spectra). |
| m1 | Optimise s in the tail; use the exact factor in B*; keep the individual δ_k t^{k−2} in Θ; or state these gains in Remark 6.6. |
| m2 | State the factor-e (about 2e overall) Chernoff loss against Weyl's law next to Table 3. |
| m3 | Give c' = 1/4 + π²/h_7² ≈ 33.4. |
| m4 | Check the arithmeticity and small-eigenvalue status of the two cusped limits and update Problem 1(b). |
| m5 | Justify γ ≠ 1 in Lemma 4.2. |
| m6 | Move the conditional limit statement after Figure 3 into a remark. |
| P1–P6 | Textual edits as listed. |
