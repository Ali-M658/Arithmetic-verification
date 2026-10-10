<!-- Saved verbatim by the main session from the final message of reviewer B-e: the harness refused the reviewer's own write. Text from the report's first heading on; the reviewer's preceding cover note was dropped. -->
# Referee report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Submitted to Annals of Global Analysis and Geometry. This review covers rigour, citations and figures.

## Summary

The paper proves (Theorems 1.1 and 6.2) that within C(A, ε, M), the closed orientable hyperbolic 2-orbifolds of area ≤ A, systole ≥ ε and cone orders ≤ M, the first N eigenvalues known to within δ determine the signature. N and δ are given by closed formulas. The proof uses:
- the Selberg trace formula for the heat function;
- enveloping remainders for the cone and area terms of the small-t expansion;
- an integrality lower bound on the first differing heat invariant (Lemma 3.3);
- a new diameter bound for the class (Theorem 4.4);
- a counting/tail argument (Section 5).

Section 7 turns the same mechanism into an instance-level a-posteriori test (Theorem 7.1) and runs it on ten computed spectra. Section 8 shows that the order bound cannot be dropped (O(2,3,m), Propositions 8.2–8.3, Remark 8.4). It also shows that pinching gives no immediate counterexample for the systole bound, and poses Problem 1.

I read all 26 rendered pages (110 dpi throughout, 200–220 dpi for Figures 1–3 and p. 7). I re-derived every proof in Sections 4–8 that is not imported. I recomputed Tables 2 and 3 completely and two rows of Table 6 from scratch, and checked every citation I could reach.

## Significance

The question (signature from a finite, noisy part of the spectrum) is natural. It is the orbifold, signature-level analogue of the Buser–Courtois finiteness theorem. The paper gives what the compactness proof cannot: explicit N and δ, a decision rule, and a sharp-in-kind negative result (Remark 8.4) showing that A and ε alone do not suffice. The constants are astronomically large, and the paper says so plainly. The a-posteriori test is the practically interesting part, and the authors are unusually careful to separate what is proved from what is estimated.

What is good:
- The statements carry their hypotheses and quantifiers.
- Every constant in Tables 2 and 3 reproduces exactly from the formulas as printed.
- The tables are mutually consistent, as are the tables and the text.
- The limitations (estimated errors, completeness conditional on them, known signature and area) are stated in the abstract, in the introduction and again in Section 7.

## Correctness and what was recomputed or checked

### Proofs re-derived by hand (all correct as written unless noted)

- **Lemma 2.2, last bound (p. 6).** The factorisation x e^{-x/2-x²/4t} ≤ 2√t e^{-1/2} e^{9t/2} e^{-2x} is correct (maxima at x = 2√t and x = 6t). Combined with Σ e^{-2ℓ(γ)} ≤ 2π e^{3diam-ℓ}/Area it gives the stated constant 2√π e^{3diam} e^{17t/4-1/2-ℓ} / (Area(1-e^{-ℓ})).
- **Lemma 2.2, bound B and its monotonicity.** These are imported from [20], but I re-derived them independently.
  - Stieltjes integration by parts against n_O(x) ≤ π e^{x+3diam}/Area, then the bound ∫_ℓ^∞ x e^{x/2-x²/4t} dx ≤ (2tℓ/(ℓ-t)) e^{ℓ/2-ℓ²/4t}, gives exactly B(ℓ, diam, t) (after dropping e^{-t/4} ≤ 1).
  - The integrand x e^{-x/2-x²/4t} is decreasing on [ℓ, ∞) when t ≤ ℓ²/(2(1+ℓ)).
  - ∂_ℓ log B < 0 on that range, because ℓ/(2t) ≥ 1/ℓ + 1. So "B decreases with ℓ" is true. The range grows with ℓ, so replacing ℓ by ε in Theorem 6.2 is legitimate.
- **Area and heat expansion.**
  - Area = 2πs(σ) is correct.
  - ĝ_t is the Fourier transform of g_t.
  - α_0..α_3 = 1, -1/3, 1/15, -4/315, and α_4 = 1/315 (numerical check).
  - b_0(m) = φ_0(m) = (m²-1)/(12m).
  - Formulas (1)–(2) are consistent with Proposition 2.3.
- **Lemma 3.3 and the examples after it.**
  - (0;4,4,4) and (0;3,4,6) have equal area (s = 1/4), and d_2 = 15/16 - 49/48 = -1/12 = -a_0.
  - The Figure 1 claim d_3 = 25/12 for (0;2,8,8) against (0;3,3,12) is correct: the two have equal c_2 = 23/16, and d_3 = -a_1(P_3 - P_3') = 750/360.
- **Lemma 4.1 (H1)–(H3), Lemma 4.2, Lemma 4.3, Theorem 4.4** (including the closed form, and arccosh(1+x) ≥ √(2x/(1+x)), checked numerically on [10^-8, 10^3]). The defect argument in Lemma 4.2 is correct: integer numerator gives defect ≥ π/(abc), and cos((θ-α-β)/2) ≥ sin(π/2M) ≥ 1/M.
- **Lemma 5.1** case analysis (minimum s = 1/42, so Area ≥ π/21; n + 4g ≤ Area/π + 4), and **Proposition 5.2**.
- **Lemma 6.1 and the proof of Theorem 6.2.** I followed every inequality:
  - the bound B_* ≤ Γ/8, rewritten as e^{-y}y^p ≤ ..., and the threshold y_0 obtained via e^{-y/2}y^p ≤ (2p/e)^p;
  - monotonicity of B_* on (0, t_2];
  - Λt_* ≥ 1 because 8Z♯/Γ_* ≥ 8;
  - the tail estimate equals Γ_*/8 exactly;
  - the final margin (Γ_*/8 + Γ_*/8 + Γ_*/(8e) < 3Γ_*/8 against Γ_* - 3Γ_*/8);
  - the Γ_*/16 slack remark (7/16 < 9/16).
- **Theorem 7.1.**
- **Lemma 8.1 (Jørgensen, hyperbolic case).**
  - The recursion x_{n+1} = -x_n(1+x_n)(u-u^{-1})² holds.
  - The case analysis for x_n = 0 holds.
  - The fixed-point bookkeeping holds: p_n/q_n = x_{n-1}/(1+x_{n-1}), and the attracting/repelling assignment is right.
  - The conjugation C_n = A^{-k_n} B_n A^{k_n} → A is correct.
- **Trace identities before Proposition 8.2.** β = hkh^{-1} has off-diagonal entries ±sin(φ/2)cosh r, which I checked by hand.
- **Proposition 8.2.**
  - cosh d(v_2,v_3) = 2cos(π/m)/√3 and cosh d(v_2,v_m) = 1/(2sin(π/m)) follow from (H3).
  - The convexity step d(x,v_3) ≤ 2s_m holds.
  - σ_* = 0.5620669 is correct: cosh(2s_∞) = 5/3, so σ_* = 2 arsinh(1/(2√(37/12))).
  - 2 arccosh(3/2) = 1.92485 is correct.
- **Equation (3).** The identity f'²w = u'² + qu² + (d/dρ)(...) holds, with q = 1/4 ∓ 1/(4 sinh² / cosh² ρ).
- **Propositions 8.3 and 8.5, and Remark 8.4.**
  - The pigeonhole count holds: K+1 orders 7..K+7 when M = K+7.
  - The Rayleigh quotient for λ_1 in Proposition 8.5 holds, using ∫_{-a}^{a} ρ² cosh ρ dρ = 2[(a²+2)sinh a - 2a cosh a].
  - The quadrilateral normals and inner product -sinh a sinh b are correct.
  - The A < π/3 finiteness remark holds.

### Statements imported from [20] that I could not check

Theorem 2.1 (heat-function extension), the counting statement of Lemma 2.2, Proposition 2.3, the cone-polynomial lemmas, Lemma 3.1 and Theorem 3.2. I did test Proposition 2.3 numerically. For m ∈ {2, 3, 8, 12}, t ∈ {0.01, 0.1, 0.5} and K = 0..4, E_m(t) - Σ_{l<K} b_l t^l has sign (-1)^K and modulus ≤ |b_K| t^K. |b_K(m)| increases in m for these m. The analogous statement for the area term holds for t ∈ {0.01, 0.3}. For l = 0..3 I also checked numerically that p_l is even, has degree 2l+2 and has leading coefficient a_l = |B_{2l+2}|/(2(l+1)!(2l+1)). No counterexample, but this is not a proof (see M1).

### Recomputation of tables (high-precision code written for this review, mpmath at 50 digits)

- **Table 2.** All twelve entries of D = 4r_0A/v_0 reproduce: 56.6, 1125, 6.37e5; 150.9, 3001, 1.70e6; 640, 3184, 1.70e6; 1132, 2.25e4, 1.27e7. The cited true diameters 2.448 and 2.158 are the longest sides of the (2,8,8) and (3,3,12) triangles: arccosh(cot²(π/8)) = 2.4484 and arccosh 4.3855 = 2.158.
- **Table 3.** All eight rows reproduce exactly in every column: k_*, D, t_1, t_3, Γ_*, Λ, N, δ and the binding constraint. The text claims also reproduce:
  - "t_3 binds in rows 4, 6 and 7";
  - "t_2 ≥ 0.0045";
  - "at A = 10π, k_* ≤ M changes N from about 4×10^18 to 1.1×10^7" (I get 4.19×10^18 with k_* = 14);
  - "N grows by about 9 per halving of ε, tending to 8" (ratios 9.03, 8.94, 8.86, 8.79, 8.72 at A = 4π/3, M = 3).
- **Table 4.**
  - The family systole 4b = 4 arsinh(√(e^{-ϑ}/2)) matches all eight ℓ values, each rounded down with margins 2.9×10^-7 to 9.2×10^-7.
  - A word enumeration (length ≤ 11, double precision) gives triangle systoles 2.2567679 and 1.8626041, which match ℓ = 2.256767 and 1.862604. The latter margin is 5.5×10^-8, consistent with "at least 5×10^-8".
  - The diameters 2.292 (ϑ = 0) and 3.885 (ϑ = 2.8) match the opposite-vertex distance computed in the hyperboloid model.
  - The Weyl counts are consistent with N_c (e.g. (π/2)·16000/(4π) = 2000 against 2002).
- **|S| in Table 6.** I enumerated the signatures by hand. Area π/2, orders ≤ 12 gives exactly six: (0;2,2,2,4), (0;2,6,12), (0;2,8,8), (0;3,3,12), (0;3,4,6), (0;4,4,4). Area 4π/3, orders ≤ 3 gives exactly three: (0;3,3,3,3), (0;2,2,2,2,3), (1;3).
- **Table 6 rows for O(2,8,8) and O(3,3,12)** were recomputed independently from Table 5's eigenvalues and error estimates, Theorem 7.1 as printed (H from Lemma 2.2 with ℓ and Δ = 2 diam P from Table 4), and G_σ by quadrature of Theorem 2.1. The least N is (C1) 18, (C2) 20 for O(2,8,8) and (C1) 25, (C2) 29 for O(3,3,12), exactly as in Table 6. The reported times are inside the windows I find, but they are not the first times at which the criterion holds (see m9).
- **Text claims checked against Table 6.**
  - The abstract's "18 to 847" and Section 7.2's "24 to 767 / 28 to 847 / 6.8×10^9, 4.3×10^4–3.7×10^5, 7.4×10^12".
  - "9×10² to 4×10^5" (p. 3).
  - "5.6×10³ and 8.6×10³", "8.6×10² to 1.6×10^4", "2.3×10^4 to 4.1×10^5" (p. 16).
  - The factors "20–50, 10^6, 10^7–3×10^8" (p. 17).
  - "(λ̃_N - ε_N)t of about 11" (p. 16).
  - The Figure 2 caption's "5×10² to 3×10^11" (767 vs 3.7e5 gives 482; 28 vs 7.4e12 gives 2.6e11).
  - The C2 count is never below the C1 count, and counts increase as the systole falls.
- **Section 8 numbers.** h_7 = 0.54527. The bound at m = 7, j = 1 is 133.0, above λ_1 = 44.89. The rescaled λ_1 at m = 4096 is h²(0.473 - 1/4)/π² = 1.163, i.e. "16% above 1".

### Figures checked against captions, text and tables

- **Figure 1 (p. 13; 220 dpi render).**
  - There are five competitor curves; the darkest starts at 2.0×10^-3 at t = 0.001, which matches d_3 t = 25/12 × 10^-3 (my quadrature gives 2.012×10^-3).
  - The dashed curve matches B(ℓ = 2.256767, Δ = 4.897, t): 8×10^-7 at t = 0.04 and 0.53 at t = 0.07.
  - Ticks and labels are legible.
  - The shaded window, measured from pixels, is t ≈ 0.0504–0.0559. My recomputation of where E_21(t) < (nearest gap)/2 gives 0.0482–0.0586 (m10).
- **Figure 2 (p. 19).** Marker heights read off the log axis match Table 6:
  - orange diamond ≈ 26 (25), teal ≈ 18 (18);
  - open/filled diamonds at the left ≈ 780/830 (C1 counts 767/847, so the diamonds are C1, not C2);
  - squares at 6.7×10^9 and 7.4×10^12, and open squares 3.7×10^5 down to 4.3×10^4.
  - M = 3 markers sit left of the true systole and M = 12 markers right, as stated.
  - The circles (N_obs) appear in no table (m11).
- **Figure 3 (p. 22).**
  - 21 orders from 7 to 4096 are plotted.
  - λ_1 runs from ≈ 45 to ≈ 0.47, matching 44.89 and 0.473.
  - The top dashed bound at m = 7 is ≈ 1600, matching 1/4 + 49π²/h_7² = 1630.
  - The 1/4 line is present.
  - Panel (b) is log-scaled: tick spacings are proportional to log j². λ_1 at m = 7 reads ≈ 1.35, matching h_7²(44.89 - 1/4)/π² = 1.342.
  - The labels render correctly; the garbled glyphs in pdftotext output are font-encoding artefacts only.

### Citations checked (statement level where accessible)

| Ref | What it is cited for | Outcome |
|---|---|---|
| [1] Dryden–Strohmaier | Thm 1.1, Prop. 3.3, Thm 3.2, eq. (1) | Confirmed in arXiv:math/0504571. Thm 1.1: spectrum determines length spectrum and cone counts. Prop. 3.3: same underlying space. Thm 3.2: Gauss–Bonnet. Eq. (1): trace formula with the elliptic term as in Thm 2.1. Bibliographic data and DOI correct. (Doyle–Rossetti proved Thm 1.1 independently, as [1] notes; consider citing.) |
| [2] Linowitz–Voight | Thm A: same signature, isospectral, not isometric | Confirmed (arXiv:1408.2001). Thm A gives pairs of signature (0;2,2,2,2,2,3,4). Bibliographic data correct. |
| [3] Mumford, Cor. 3 | Compactness | Bibliographic data and DOI correct; full text blocked (403), so Cor. 3 not checked. |
| [4] Bers | Extension to Fuchsian groups with elliptic elements | Bibliographic data correct; content not checked (paywall). |
| [5] Buser–Courtois, (1.1), pp. 523–524 | Theorem and conjecture | Content confirmed via the zbMATH review (Zbl 0711.58033): m(g,ε) exists, and m depending on g alone is conjectured. Equation number and pages not checked. **Issue number is wrong**: Springer metadata give Math. Ann. 287, issue 1, not 287(3) (m14). |
| [6] Garbin–Jorgenson | Cor. 5.5, Thm 5.3 | Confirmed in arXiv:1603.01494. Cor. 5.5: convergence below 1/4. Thm 5.3: N(T) ~ c(T) log Q for T > 1/4. Bibliographic data correct (vol. 64 is 2018; Crossref issue date 2019). |
| [7] Garbin–Jorgenson | Rem. 2.7, (2.8) | Confirmed (arXiv:1603.01495): the heat trace with the same normalisation. |
| [7] | Thm 6.5 | **Does not match**: in the arXiv version, Thm 6.5 is pointwise convergence of the spectral counting function C_{M_q,0}(x,T) for T < 1/4, not growth above 1/4. Published numbering not checked (m15). |
| [8] Hejhal vol. 2 | "Selberg and Hejhal" on Hecke triangle groups | Bibliographic data correct; no pinpoint given (m16). |
| [9] Hejhal memoir; [10] Ji, p. 264; [11], [12] Wolpert, [11, p. 67] | Spectral degeneration | Bibliographic data and DOIs correct; page pinpoints not checked (no access). |
| [13] Strohmaier–Uski, §7 | Heat-trace completeness check | Confirmed: §7 describes exactly this. |
| [14] Booker–Strömbergsson–Venkatesh | Rigorous Maass forms | Bibliographic data correct. |
| [15] Buser book, Lemma 6.6.4 | (g-1)e^{L+6} count | Not checked against the text; agrees with my recollection of the lemma. No DOI given (the 2010 reprint has one). |
| [16] Donnelly; [17] DGGW, Thm 4.8 | Local heat expansion | Bibliographic data correct. DGGW Thm 4.8 exists and is the heat asymptotics of orbifolds stratum by stratum. |
| [18] Uçar, Thm 4.20 and Thm 3.40 | Closed-form coefficients; induction on angles | Confirmed (arXiv:1711.03405). Thm 4.20(i) is exactly the α_k formula with κ = -1. Thm 3.40 is the induction on angles. The DOI 10.18452/18463 resolves to edoc.hu-berlin.de. |
| [19] Chang–DeTurck | Finite part of the Dirichlet spectrum | Content confirmed via zbMATH (N depends on the first two eigenvalues; conclusion is isospectrality); Thm 1 number not checked. Crossref lists pages 1033–1033, a Crossref error; the paper's 1033–1038 is right. |
| [21] Thurston notes, 13.3.4–13.3.6 | Hyperbolicity criterion | Not checked (fetch failed). |
| [22] Hejhal vol. I; [23] Iwaniec | Trace formula | Bibliographic data correct. |
| [24] Beardon | Jørgensen's inequality (Ch. 5); triangle groups | Content consistent. Bibliographic entry lacks "Graduate Texts in Mathematics 91". I cannot confirm that Beardon treats the hyperboloid model cited on p. 8. |
| [25]–[30] | Software and colour references | DOIs correct and resolve (Zenodo 8409685, NETGEN, ARPACK, Jørgensen 98(3) 739–749, Nat. Commun. 11, 5444). |
| [20] companion | Imported results | Not available; no identifier (M1). |

## MAJOR issues

**M1. Load-bearing results are imported from an unrefereed, unavailable companion manuscript ([20]; pp. 4–7, Table 1).**
- Imported without proof:
  - Theorem 2.1 (extension of the trace formula to the heat function);
  - the closed-geodesic count n_O(x) ≤ π e^{x+3diam}/Area (Lemma 2.2);
  - Proposition 2.3 (enveloping remainders, and monotonicity of |b_K(m)| in m for all K, m, t);
  - the structure of p_l (degree, leading coefficient, triangular expansion);
  - Lemma 3.1;
  - Theorem 3.2 (separation at L ≥ ⌊A/π⌋+4, and at L = M for bounded orders).
- These are not background. Theorem 3.2 fixes k_*, which enters Γ_* = γ_* t^{k_*-2}/2 and hence N and δ. Proposition 2.3 is the only control on the cone and area expansions in Lemma 6.1 and in (2).
- [20] is cited as "Companion manuscript, submitted (2026)" with no arXiv identifier. Pinpoints such as "[20, Prop. B.2]" are hyperlinked in colour into another document, and those links will not resolve for readers or referees.
- My numerical spot checks of Proposition 2.3 and the p_l structure found no counterexample (see above), but a referee for this journal cannot certify Theorem 1.1 without [20].

**M2. The completeness argument in Section 7.1 states more than it shows (p. 15, "Completeness"; also Table 4 caption, p. 16).**
- The text says that because the computed heat trace agrees with I + E to 4.7×10^-13 at t = 0.0015, "no eigenvalue below 1.6×10^4 is missing or spurious". A single-time trace comparison bounds only a weighted net discrepancy, and that bound depends on the estimated ε_j.
- It does not exclude compensating defects: one eigenvalue missing near λ and a spurious one near λ' change the trace by e^{-tλ} - e^{-tλ'}, which can sit below the 1.5×10^-11 budget. A doubled or dropped member of a near-degenerate cluster is exactly the failure that item (iv) on p. 14 says can make the test pass for a wrong signature.
- For the triangle orbifolds the paper does not say whether the two-window coverage used for O_ϑ was also used.
- The paper is honest that the conclusion is conditional on the ε_j. The sentence nevertheless asserts more than the check gives, and Table 6, Figure 2 and the abstract depend on it.

## MINOR issues

- **m1 (p. 2, Theorem 1.1).** "σ(O) is the signature σ ∈ Sig(A,M) for which ... G_σ is nearest". Write "the unique σ ... that minimises", as in Theorem 6.2, so that the rule is well defined.
- **m2 (p. 2 vs pp. 5–11). "Sig" names two different things.** "O ∈ Sig" is a class of orbifolds; "Sig(A,M)" is a set of signatures. Sig(A,M) should also say "hyperbolic signatures" explicitly (p. 2 says "signatures of area at most A", which presupposes s > 0).
- **m3 (p. 6, Lemma 2.2).** "On this range B increases with diam and decreases with ℓ": the range depends on ℓ. State it as "for fixed t > 0, B is increasing in diam, and decreasing in ℓ on {ℓ : ℓ²/(2(1+ℓ)) ≥ t}". (The claim is true; I checked it.)
- **m4 (p. 12, after Table 3). The exact-arithmetic claim is too strong.**
  - "The rule is computable in exact rational arithmetic" fails as written: t_* involves logarithms and exponentials (through ϖ and y_0), and e^{-λ̃_j t_*} is transcendental.
  - The existence of K with t_*^K Q(K) ≤ Γ_*/16 is asserted without argument. It does exist, because the minimum over K of t^K Q(K) is super-exponentially small, but this should be said.
  - Fix: replace t_* by a rational t ≤ t_* and justify that the proof survives the substitution, or weaken the claim to "computable to any prescribed accuracy".
- **m5 (p. 3).** "with the class-level diameter bound of Theorem 6.2" should read "of Theorem 4.4".
- **m6 (p. 7).** Theorem 3.2 cites "[20, Cor. 3.5, Thm 3.8]", while Table 1 has "Theorem 3.8(i)". Make them agree.
- **m7 (p. 16, last paragraph of 7.1; Table 6).**
  - "fails at N = 4423 ... low by at least 0.3%": with least N ≥ 4424 and estimate 4412, the shortfall is at least 12/4424 = 0.27%.
  - Off-by-one in the Table 6 notation: the test with N uses λ̃_0..λ̃_N, i.e. N+1 eigenvalues. Failure "for every N up to the N_c eigenvalues" therefore shows least N ≥ N_c (if N_c counts λ_0), not "> N_c".
  - Fix both statements and say whether N_c includes λ_0.
- **m8 (p. 16).** "Where both are available, the estimate is within 8% of the count for N < 100 and within 0.6% for N ≥ 400." The paired values are not shown anywhere, so the reader cannot check this. Give them (a column or a sentence with the extreme cases).
- **m9 (Table 6 caption).** "with the time t at which it holds" is undefined; the criterion holds on an interval. For O(2,8,8) at N = 18 I find (C1) first holds at t ≈ 0.0533, while the table gives 0.0565; (C2) first holds at t ≈ 0.0547 against 0.0556. Say which time is reported (centre of the window? the time minimising some margin?).
- **m10 (Figure 1, p. 13). The shaded window is not reproducible from the stated definition.**
  - The caption and text say the shading marks where half the nearest gap exceeds the sum of the geodesic bound and the tail-plus-perturbation error, for N = 21.
  - Measured from the render, the shading is t ≈ 0.050–0.056.
  - From Table 5, Theorem 7.1's E_21 and the Lemma 2.2 bound with ℓ = 2.256767, Δ = 4.897, I get 0.048–0.059.
  - State exactly which error terms and which s (or infimum) the shading uses, and give the window endpoints numerically.
- **m11 (Figure 2 and p. 17). N_obs is undefined and its data are not reported.**
  - N_obs, "the least N from which on the data lie within half the nearest gap, judged against the true signature", has no stated time or time range.
  - "From which on" presupposes monotonicity in N, which is not shown.
  - The circles' values appear in no table. Define N_obs precisely and tabulate it.
- **m12 (Section 7.1, "Error estimates", p. 15).**
  - ε_j is the difference between (h,p) = (0.05,10) and (0.07,12). The paper should say why (0.07,12) is the more accurate of the two, so that the difference estimates the production error.
  - It should also say whether the conforming-FEM one-sidedness (λ_j ≤ λ_j^h) was used anywhere. If not, note that it would give rigorous one-sided information for free.
- **m13 (Section 7.1, completeness for the family, p. 16).** Item (iv) on p. 14 calls the role of the three-discretisation count agreement "not a technicality". For λ̃_N above 9.8×10³ (the class-level columns of Table 6 run to N_c ≈ 4400, λ ≈ 1.3×10^4), the evidence rests on that agreement alone. Say so where those columns are discussed (p. 16).
- **m14 ([5]).** Math. Ann. 287 is issue 1 (Springer metadata), not issue 3. Also verify that the theorem is labelled "(1.1)" and that the conjecture is on pp. 523–524 (I could not access the text).
- **m15 ([7, Thm 6.5], p. 4).** In arXiv:1603.01495, Theorem 6.5 is pointwise convergence below 1/4, not growth of the counting function above 1/4. Check the published numbering, and attach each pinpoint in that sentence to the half of the claim it supports.
- **m16 (p. 4).** "goes back to Selberg and Hejhal [8]": give a chapter/page pinpoint in Hejhal vol. 2, and a reference for Selberg's contribution.
- **m17 (bibliography).**
  - [24] lacks "Graduate Texts in Mathematics, vol. 91". The hyperboloid model (p. 8) is better cited to Ratcliffe, Foundations of Hyperbolic Manifolds, Ch. 3, unless the authors can point to the Beardon section.
  - [15] lacks a DOI (the 2010 Modern Birkhäuser Classics reprint has 10.1007/978-0-8176-4992-0).
  - [18] could add arXiv:1711.03405.
  - [8] "Vol. 2" against [22] "Vol. I": make the style consistent.
- **m18 (p. 20).** The text cites an internal script path (theory/eigen/systole_233.py) as the source of the 0.98399 and 1.9213 values. Cite the archived deposit instead. Also say whether the length-24 enumeration is a complete search for geodesics up to some length, or only a heuristic. The stated "finds no closed geodesic shorter than" implies the former, but word length does not bound geodesic length.

## Presentation (figures, captions, notation, exposition)

- **P1. Notation clashes**, most dangerous first:
  - Γ is the Fuchsian group (and Γ_x̃, Γ_m, Γ*), but also the gap function Γ(t) and Γ_* (Section 6).
  - ε is the systole bound, but ϵ_j / ε_N are the eigenvalue errors (Theorem 7.1). These are nearly indistinguishable in print.
  - A is the area bound, the exact area (Theorem 7.1) and the hyperbolic matrix (Lemma 8.1).
  - α is used for the heat coefficients α_k, for angles (Lemmas 4.1–4.2) and for an axis (Proposition 8.2).
  - β is a constant (Theorem 7.1), an angle, a rotation and a line (Section 8.2).
  - p is a point, an exponent (Theorem 6.2), a triad order and the FE order.
  - Q(K) clashes with Q_{k,b}, and P (polygon) with P_k (power sums) and P (union of tiles).
  - h is the mesh size, h_m, a distance in (H3), and a matrix.
  - Suggested renamings: the group stays Γ and the gap becomes, say, 𝒢(t); use ϵ only for one meaning; matrices in Lemma 8.1 become X, Y.
- **P2. Figure 2** has no legend, and its caption does not say what diamonds, squares, circles, open and filled markers, or colours mean. That information is only in the body text on p. 17. The caption should be self-contained: diamonds are (C1) counts, which is not stated.
- **P3. Figure 1.** The caption does not say which dotted curve is N = 21 and which is N = 100, or that the black curve is (0;3,3,12). The y-axis label |G_σ0 - G_σ| covers only the gap curves, not the error curves plotted on the same axis.
- **P4. Figure 3.** The caption should say that grey level orders j (darkest is j = 1), that the thin dashed curves in (a) are the bounds of Proposition 8.3 with index j+1 inside, and that the dotted horizontals in (b) are j². Note visually that the bound for λ_j sits near λ_{j+1}, which is expected and not an error, but it will confuse a reader. The eigenvalues plotted are not tabulated; give at least λ_1..λ_6 at m = 7 and m = 4096.
- **P5. Float placement.** Table 6 interrupts the statement of Lemma 8.1 across pp. 17–18 ("fixed point | [Table 6] | of A in ∂H²"). Keep theorem statements unbroken.
- **P6.** The data statement names the repository "Ali-M658/Arithmetic-verification". That name does not identify the project, and it is not under the stated maintainer's name. Since the Zenodo deposit is declared primary, this is minor, but the deposit should mirror the repository's naming.
- **P7.** Tables 3 and 5 use "aeb means a×10^b". This is fine, but use one convention across Tables 3, 5 and 6 (Table 6 uses ×10^b).

## Recommendation

**Minor revision, conditional on M1.** If [20] is not made available to the editor and referees (e.g. on arXiv), the recommendation becomes **major revision**, because the main theorem cannot then be verified.

Confidence:
- **High** for everything proved in this manuscript (Sections 4–8, Lemma 6.1, Theorem 6.2, Theorem 7.1), which I re-derived.
- **High** for Tables 2–4 and the Table 6 rows I recomputed, which matched exactly.
- **Moderate** for the imported results from [20], which I could only test numerically.

## What resolves each issue

- **M1:** post [20] (arXiv) and cite it with an identifier; send it to the editor. Better still, add self-contained proofs (or detailed sketches with all hypotheses) of Proposition 2.3 and Theorem 3.2 in an appendix, since k_* and Q(K) depend on them. Replace the cross-document hyperlinks with plain numbers tied to a fixed version of [20].
- **M2:** rephrase the completeness conclusion as conditional and as excluding a single isolated defect only. Strengthen it with the trace comparison over a range of t, which separates defects at different λ, or a per-window count from two discretisations for the triangle orbifolds as done for O_ϑ. Say explicitly which check covers which λ-range.
- **m1–m3, m5, m6:** wording edits as indicated.
- **m4:** replace t_* by a rational t ≤ t_* with justification, or weaken the claim; add the one-line existence argument for K.
- **m7:** correct 0.3% to 0.27%, fix the "> N_c" convention, and state whether λ_0 is counted.
- **m8, m11:** tabulate the estimate/count pairs and N_obs; define N_obs (time window, monotonicity).
- **m9, m10:** define the reported time in Table 6 and the exact shading rule of Figure 1; give the window endpoints in the caption.
- **m12, m13:** one or two sentences each on the error-estimate comparator and on where count agreement is the only evidence.
- **m14–m17:** bibliographic corrections as listed. Check [5] "(1.1)" and pages, [7] Thm 6.5, the Hejhal pinpoint and the [24] hyperboloid citation against the published texts.
- **m18:** cite the deposit and state what the enumeration covers.
- **P1–P7:** renaming and caption/legend edits as listed.

### Not checked (for transparency)

- Mumford Cor. 3, Bers, Thurston 13.3.4–13.3.6, Buser Lemma 6.6.4, Ji p. 264, Wolpert p. 67, Buser–Courtois (1.1)/pp. 523–524, and the published numbering of [6] and [7] (I used the arXiv versions).
- The eigenvalues in Table 5 and Figure 3 themselves (no FEM recomputation).
- The family's Table 6 rows, which need eigenvalues not given in the paper.

---

My scripts are in /Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-5/B-e-rigour-citations-figures/scratch/code/: `consts.py`, `check2.py`, `pl.py` and `table6.py` recompute the tables, `sys.py` the systoles, and `fig1.py` the Figure 1 window. Page renders are in `scratch/png/` and `scratch/hi/`, and the fetched literature is in `scratch/lit/`.
