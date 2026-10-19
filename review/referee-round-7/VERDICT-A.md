# VERDICT-A: referee round 7, Paper A ("How much of a hyperbolic orbifold does heat hear?", AGAG)

Reports (verbatim): `A-a-editor-polygon-heat/`, `A-b-brownian-cone-probabilist/`,
`A-c-symmetric-functions-algebraist/`, `A-d-trace-formula-computation/`, `A-e-attribution-historian/`.
Length remarks: none were made. Two editor suggestions are declined under the standing rules: retitling
(the title is the authors' and stays; M1 is answered inside the paper) and moving Section 6 and
Appendix C to the supplement (nothing is cut; M2 is answered by a contribution statement and sharper
results).

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| A-a editor (polygon heat) | **SEND TO REVIEW**; major | 0.6 (outcome), 0.85 (correctness) |
| A-b Brownian / cones (§2, App. B) | major (minor once M1, M2 fixed) | 0.65 |
| A-c symmetric functions (§3, App. A) | minor | high (correctness) |
| A-d trace formula / computation (§§4-5, App. D-E, S2-S6) | minor | high |
| A-e attribution / citations / figures | major | 3/5 |

**Stop condition: NOT MET** (two referees major).

No FATAL item. Every reviewer recomputed large parts independently (cone polynomials, enveloping
remainders, Theorem B, Theorem 3.8 constructions, Table S1, Section 5 by enumeration, Theorem 5.8 and the
descent, Remark B.4, Remark 4.3); no mathematical error affects a main theorem.

## MAJOR (deduplicated; each checked against the repository or the sources)

| id | issue | raised by | status | evidence / resolution |
|---|---|---|---|---|
| A1 | Physical framing: the counts concern coefficients of a divergent series; by Remark B.4 even c_3 of O(2,8,8) needs t ≲ 7.8e-11 and 19-digit data; the abstract's locality sentence ("up to an error smaller than every power of t, only the geometry within ~√t") conflates fixed-radius locality with √t scale. | A-a M1, A-b m1 | **CONFIRMED** (presentation) | Abstract and §1 say what short-time diffusion detects (the signature through the coefficients; the moduli only at e^{-ℓ²/4t}; everything at fixed t) and that K_mult is an invariant of the coefficient sequence; Remark B.4's numbers are quoted in §1; the locality sentence is attached to a fixed radius. Title unchanged. |
| A2 | Significance relative to the geometric input; novelty claims. | A-a M2, A-c §2, A-e §2 | **CONFIRMED** (presentation) | A contribution table in §1 (result / new or not / method / where), the "new" list restricted to Theorem 3.8(ii)-(iv), Theorem 3.11, Lemma 3.16 with Proposition 3.15, Theorem 3.14(c), Proposition 2.11 (with A5), Section 5; plus A-a m2: K_mult(O(p,q,r); Sig) ≤ ⌊2(1-R)⌋+4 ≤ 5, ≤ 4 when R > 1/2 (Corollary 3.5 with Area < 2π), stated in §5. |
| A3 | Overlap with the two companions: B reproves A's shared results (B Appendix A); the finite-element method is described in both; Theorem 5.8 is proved here and in the note. | A-a M3, A-e M4 | **ANSWERED IN PAPER (disclosed)**, sharpened | B's Appendix A was added in round 6 at the request of B's panel (B1, self-containment); it says "the arguments are those of [A]". The note now cites Theorem 5.8 for the hand descent (round 6 X3). Resolution here: one overlap paragraph in §1 listing exactly what is shared (B's Appendix A, the spectra and their method, Theorem 5.8 and the enumeration to 4800) and which paper is primary for each (A for the heat results, the method and Theorem 5.8; the note for the arithmetic of coincidences). The editors receive all three manuscripts. |
| A4 | Unknown constant curvature; instability of K_mult. | A-a M4 | **CONFIRMED** | New Proposition (scaling): for curvature K < 0, Z_g(t) = Z_{g'}(|K|t) with g' = |K| g, so c_j(g) = |K|^{j-2} c_j(g'); c_2 and I_j = c_j c_1^{j-2} are scale-invariant, and with c_1(g') = -χ/2 two orbifolds of unknown constant curvature share c_1,…,c_L iff c_j(σ)χ(σ)^{j-2} = c_j(σ')χ(σ')^{j-2} for 2 ≤ j ≤ L. Theorems 1.1-1.2 are for known curvature -1; with unknown curvature the comparison is against all areas and is not claimed. A remark that K_mult counts exact equalities and is unstable under metric perturbation (Proposition 2.13). Proof and a script with asserts; blind check. |
| A5 | Proposition 2.11: proof incomplete (Donnelly's form through (I-A)^{-1}, the radial reduction, uniformity in ϑ; (ii) ill-posed) and the structure of (i) is Fursaev's (3.26)-(3.27). | A-b M1, A-e M2 | **CONFIRMED** | Fursaev hep-th/9405143 (3.26): a_{α,n} = Σ_{k≤n} α c_k(α) G_{nk}, c_k polynomials of degree 2k in α^{-1} (read). Resolution: credit Fursaev at Proposition 2.11(i) and correct "computed" (only a_{α,1}, a_{α,2} are computed there); restate (ii) as the universal identity b_l = Σ_i β_{l,i}(radial jet) Π_i(m); the proof is labelled an outline with the three unproved steps named; the main results do not use it; the l ≤ 3 formulas are confirmed by computation (A-b recomputed β_{3,4}). The "only in this paper" sentence of §1.1 is corrected. |
| A6 | Lemma B.3 / Remark B.4: D = 2.448 is not an upper bound for the diameter of O(2,8,8) (the side between the order-8 points has length arccosh(cot²(π/8)) = 2.448452); ℓ_0 and D are non-spectral inputs. | A-b M2, A-d m6 | **CONFIRMED** | `theory/eigen/data/instances.csv`: diam_P = 2.448452, 2 diam P = 4.896905 (proved bound of B, §7). Resolution: D = 4.897 (2 diam P, proved), ℓ_0 the systole lower bound from the complete enumeration (computed, not interval arithmetic: stated); every "proved δ_1" says it is relative to these geometric inputs. Numbers rechecked by `check_heat_supporting.py` (the D-term is negligible: e^{3D} against e^{-ℓ²/4t} at t ~ 1e-11). |
| A7 | Theorem A's novelty over Steinig is not established; Laurens's sign-change argument is close to Lemma 3.7, Theorem 3.4, Theorem 3.8(iii). | A-e M1, A-c M3 | **CONFIRMED (in part)** | Laurens arXiv:2206.09050 (read): "the result in [Steinig] is even more general: any n power sums of n distinct positive real numbers has at most one solution", with a self-contained proof (Lemma 3.2, Cor. 3.3). Steinig's paper itself was not accessible. Resolution: say that for positive distinct orders the injectivity follows from Steinig's theorem as Laurens states it; Theorem A adds complex multisets with multiplicity and the form needed for Theorem B; credit Laurens [Lemma 3.2, Cor. 3.3] at Lemma 3.7 and Theorems 3.4, 3.8(iii); Lemma 3.7 called classical (Descartes' rule), with Laurens as the cited proof. |
| A8 | Remark 4.3's kernel and Parseval step are Garbin-Jorgenson's. | A-e M3 | **CONFIRMED** | arXiv:1603.01495 Theorem 2.5 (read): ETr K_M(t) = e^{-t/4}(16πt)^{-1/2} Σ_γ Σ_n q^{-1} ∫_0^∞ e^{-u²/4t} cosh(u/2)/(sinh²(u/2)+sin²(nπ/q)) du, which is ∫ g_t k_m. Resolution: cite [GJ, Thm 2.5, Rem. 2.6] in Remark 4.3; the remark's own content is the location of the poles and its reading. |
| A9 | Section 4: the numerics are worded as evidence ("shows on computed spectra", "d_3, d_4 tested by the fit") where they illustrate proved identities; what is new in §4 should be stated. | A-d M1 | **CONFIRMED** (wording) | Reword both places; state that the new content of §4 is the explicit constant of Proposition 4.2(a) and Remark 4.3's reading. |
| A10 | Proposition 4.2(a)'s constant carries e^{3 diam}; the 10^{10} overestimate comes from the bound 2 diam Q. | A-d M2, A-b m10 | **CONFIRMED** | `numerics/moduli/locality_ratio.py` (extended): factors 4.4e6-1.0e10 with 2 diam Q; 4.0e3-8.8e4 with the computed diameter (numerical, not a bound); 4.1e5-1.9e6 with the diameter-free count C_*(A, ℓ, M) of the companion [B, Lemma 4.5]. Resolution: Proposition 4.2(a) may use C_* (no diameter); text gives all three. |
| A11 | "Conditioning … identified with a Hurwitz determinant" overstates: the identity locates the singular set; B is not the Hurwitz matrix (a_{2j-i}) but, up to column signs, a submatrix of the Hurwitz matrix of order n+1. | A-c M1 | **CONFIRMED** | Rephrase pp. 4, 5, 19, 40, 47: M is singular exactly where Hur_{n-1} = 0, M^{-1} = B^{-1}Y; identify B; drop "as well conditioned as". |
| A12 | The correspondence configurations ↔ pairs of orbifolds is used in proofs but stated in prose; Definition 3.10 contains a theorem. | A-c M2 | **CONFIRMED** | A Realisation lemma with proof (both directions, distinctness, genus difference ι/2, least genus, area bounds), and |Z| ≥ 2L+2 moved into a lemma. Script checks on the examples; blind check. |

## MINOR and presentation (dispositions)

| id | item | raised by | disposition |
|---|---|---|---|
| a1 | sign change of D near t ≈ 0.34 | A-d m1 | fix: the data change sign between t = 0.341 and 0.360; linear interpolation 0.359; "near t ≈ 0.36" (the round-6 value 0.34 was the last sampled time before the change) |
| a2 | completeness criterion for geodesic enumerations ("words of length ≤ 10") | A-d m2 | fix: state the displacement criterion d(x_0, γx_0) ≤ ℓ + 2 rad(F) used by the enumeration of the companion's §7 |
| a3 | "touch without overlapping" vs the definition; Table S2 caption claim | A-d m3, A-e m10 | fix wording; restrict the caption's "only for p = 2, 4" to p ≤ 14 (Table S2) |
| a4 | "truncating (6)"; growth l!(m/π)^{2l} heuristic vs fact | A-d m4, A-a m1, A-b m4 | fix: "the cone series"; heuristic in both places (a proof is not added) |
| a5 | ϑ = 0 multiplicities (two systoles, double λ_1) | A-d m5 | fix: one sentence |
| a6 | "(0;5,5,5) outside the triangle family" | A-d m7 | fix |
| a7 | 0.79 → 0.78 | A-d m8 | check data and fix |
| a8 | admissible class citation; ψ̂ real and even; 2ε < ℓ unnecessary | A-b m2, m3 | fix |
| a9 | Proposition 2.13 "for each L"; locality/disjointness; exact cone | A-b m5 | fix |
| a10 | extension to K > 0 by polynomial dependence | A-b m6 | fix: one clause |
| a11 | m ≥ l-1 hypothesis in 2.11(i) | A-b m7 | fix with A5 |
| a12 | Remark 2.12 computational | A-b m8 | fix: label in the statement |
| a13 | "integer cone orders at most μ_0" in Lemma B.3 | A-b m9 | fix |
| a14 | minimality by the kernel argument for M = 3..9 | A-c m1 | fix: replace the search by the argument (script check) |
| a15 | closed form ν(a) ∝ (-1)^{M-a} a³ binom(2M, M-a) | A-c m2 | fix: state it (script check) |
| a16 | Theorem 3.11's hypothesis is |Z| = 2L+2 | A-c m3 | fix |
| a17 | Proposition 3.12 needs L ≥ 2 | A-c m4 | fix |
| a18 | equivalence f = O(A^α) ⟺ N(k) = Ω(k^{1/α}) | A-c m5 | check the argument; add if it holds |
| a19 | L = 1 convention; well-ordering; explicit inequalities | A-c m6 | fix |
| a20 | ⌈(L-1)/2⌉ | A-c m7 | check and fix |
| a21 | Theorem 3.4 vs Corollary 3.5 for an observer; "one fact" | A-c m8, m9 | fix |
| a22 | "pencil of quartics" undefined | A-c m10 | fix |
| a23 | Prouhet rows of Table S1 printed with parameters; per-piece attribution | A-c m11, A-e m8 | fix where the source is in hand (Chen survey arXiv:2506.11429 read by A-c and A-e); otherwise state "found by our search" |
| a24 | Borwein-Ingalls pinpoints | A-c m12 | re-check against the fetched copy if available; else keep and record |
| a25 | Frolov-Tarry shift N(k+1) ≤ 2N(k); Hua/Wright/Wooley | A-c M3 | add only with a source read (Chen survey) |
| a26 | Abreu et al. Thm 6.2 and hypotheses; Proctor-Stanhope; Schueth's "only when"; DGGW's χ ≥ 0 class; Dryden-Strohmaier for the counts; Durso; Orlando 1911; Kuosa-Meyrignac-Chen | A-e m1-m8 | fix each against the fetched source (A-e's `scratch/src/`); Durso and Orlando only if a record is fetched |
| a27 | "to our knowledge"; N(k) vs W(k) | A-e m11, A-a m4 | fix |
| a28 | Schueth Lemma 3.4 for the expansion | A-e m12 | fix |
| a29 | Fig. 5(b) circles vs the budget | A-e m13 | check against the data and explain |
| a30 | Fig. 8 axis title vs distance | A-e m14, A-a P4 | fix in the caption/text (figure files unchanged unless the axis title is wrong) |
| a31 | unknown curvature sentence; (0;3,3,3) χ = 0; constants 1/3 and 8π; non-isometry argument; Corollary 6.5 conditional; Theorem 3.13 genus | A-a m5-m10 | fix |
| a32 | classical corner literature (Kac, McKean-Singer, van den Berg-Srisatkunarajah, Mazzeo-Rowlett, Lu-Rowlett) | A-a m3 | add with fetched records only |
| a33 | numbering clash Theorems A-C vs Appendices A-C | A-c P1, A-e P1, A-a P2 | renumber Theorems A-C as Theorems 3.1-3.x? (labels kept); check all cross-references incl. B's and the note's |
| a34 | notation overloads (C, a, χ, Φ, ψ, T, κ, d, s) | A-a P3, A-b P1, A-c P2, A-d P3, A-e P2 | rename the worst collisions (cut-off χ, isometry Φ, bump ψ, the integer C of Theorem 3.8) |
| a35 | captions (Figs 1, 2 long), colour keys, Fig. 4(a) stylised, Fig. 8 legend | A-e P3-P4, A-a P4-P5, A-c P5-P6, A-d P4 | captions ≤ 2 short sentences; colour key in the text; no in-figure legends (SPEC) |
| a36 | Table 1 splitting a sentence; duplicate "Table 1 lists" | A-a P1 | fix |
| a37 | "records … records"; double parenthetical; "is gap ≤ 0"; "the bound 6" | A-d P1-P2, A-e P5 | fix |
| a38 | references: Dowker pages and initials; [6], [52] preprints | A-e P6 | check the .bib and the class output |
| a39 | Definition of "enveloping"; Lemma 2.5 "which"; T(0) = X_l; forward dependence on Lemma 3.3; placement of Remarks 2.9, 2.12 | A-b P2-P6 | fix (placement unchanged) |
| a40 | Prop. S3.1 into the paper | A-a P7 | no change (supplement placement is the authors' choice; it is cited exactly) |

## Resolutions (round-7 fixes; `main/scratch/fix_A_r7a.py`, `fix_A_r7b.py` and direct edits)

| id | where now | check |
|---|---|---|
| A1 | abstract (first three sentences), §1 paragraphs 1-2 (fixed-neighbourhood locality; "detects the signature through these coefficients only in the limit t → 0", with Remark B.4's numbers; "invariants of the sequence of coefficients, not durations") | |
| A2 | §1 "What is elementary and what is not" rewritten as the contribution statement (new / classical / Fursaev's); §5: K_mult(O(p,q,r); Sig) ≤ ⌊2(1-R)⌋+4 ≤ 5, ≤ 4 for R > 1/2 | blind check |
| A3 | §1 overlap paragraph: this paper primary for the shared heat results and the description of the computations; the note reproves Theorem 5.8 by machine and cites it | |
| A4 | new Proposition 2.x (Unknown constant curvature) with proof, and the paragraph after it (what is not claimed; instability of exact equalities) | `theory/revision/check_heat_supporting.py` §8(a); blind check |
| A5 | Fursaev credited in §1.2, §2.2 and before Proposition 2.11; (ii) restated as a universal identity; "Proof (outline)" with the three unproved steps named; "only in this paper" corrected | blind check |
| A6 | Lemma B.3 "integer cone orders"; Remark B.4: ℓ_0, D are geometric inputs; D = 4.897 (twice the longest side 2.4485; proof given), ℓ_0 = 2.2567 from the companion's complete enumeration (now certified in interval arithmetic, `theory/eigen/certify_systoles.py`); δ_1 = 4858 t_3 unchanged, and unchanged for every ℓ_0 ≥ 0.01 | `check_heat_supporting.py` §2 (new asserts); blind check |
| A7 | §1.2 and before Lemma 3.7: Steinig as stated by Laurens; Laurens [Lemma 3.2, Cor. 3.3] credited for the sign-change argument; "new" restricted | |
| A8 | Remark 4.3 cites Garbin-Jorgenson Thm 2.5, Rem. 2.6 | |
| A9 | §4 opening and the fit sentence reworded; "truncating the cone series" | |
| A10 | new Remark 2.x (A count without the diameter) via the companion's Lemma 4.5; §4 and S6 give the three sets of factors | `numerics/moduli/locality_ratio.py` (1') asserts |
| A11 | §6 and Appendix C: "singular exactly where Hur_{n-1} = 0", M^{-1} = B^{-1}Y, one-sided bound | |
| A12 | new Lemma 3.x (Configurations and pairs) with proof; Definition 3.10 no longer contains a theorem; Proposition 3.15's proof cites the lemma | `check_heat_supporting.py` §8(c); blind check |
| minors | a1 (0.36, between 0.341 and 0.360), a2 (S4: the first two lengths confirmed by the companion's complete enumeration), a3 (strata wording; Table S2 caption via the generator), a4, a5 (ϑ = 0), a6 (O(5,5,5)), a7 (0.78), a8 ("the class of test functions for which [DS] state it"), a9-a10 partly, a13, a15 (closed form with proof; `check_heat_supporting.py` §8(b)), a16, a17, a18 (equivalence proved in Proposition 3.15), a19, a20 (ceilings), a21-a22, a26 (Abreu et al. Thm 1 and Thm 6.2 with hypotheses, read from arXiv:math/0608462; Proctor-Stanhope; Schueth's "can occur"; DGGW's class; Dryden-Strohmaier Thm 1.1 for the counts; Schueth Cor. 2.4, Lemma 3.4, (13)), a27, a29 (Fig. 5(b) circles at the first sampled time past the threshold), a30 (Fig. 8 caption "up to permutation"), a31 (Corollary 6.5 conditional), a33 (Theorems A-C renumbered 3.x), a34 (cut-off χ renamed ζ), a35 (captions F1, F5, F6, F8; colour key at first use), a36-a37 | |
| not changed | a14 (minimality by the kernel argument: the argument must also handle both signs t = ±1 and the genus condition; the computer-search statement is kept), a23-a25 (per-piece attribution, Borwein-Ingalls pinpoints, Frolov-Tarry, Hua/Wright/Wooley: sources not read this round), a32 (classical corner literature: records not fetched this round), a40 | |

## Blind check A (round 7) and its follow-up

`blind-check-A/REPORT.md` (saved verbatim): all eleven items VERIFIED mathematically; corrections applied by
`main/scratch/fix_A_r7c.py`:
- supplement S4, twice: "near t = 0.34" → "near t = 0.36 (between the sampled times 0.341 and 0.360)" (computed zero 0.3592);
- Remark B.4: "holds only if η ≤ 2×10⁻¹⁹" → "holds exactly when η ≤ 2.07×10⁻¹⁹ (to three digits)"; the assertion in
  `theory/revision/check_heat_supporting.py` tightened to 2.065e-19 < eta_max < 2.075e-19 (the condition is linear in η);
- the instability paragraph after Proposition 2.12: c₂ is topological; the claim is now for c₁ and c₃, by
  Ω₁ = (1/60π)∫K² dA and Cauchy–Schwarz (the flat-background citation removed); u₂ = K²/15 checked at K = −1 (§8(d));
- Proposition 2.13(ii): "Laurent polynomial in m";
- Remark rem:nodiam: "for the same counting function" (the companion's Lemma 4.5 counts the same classes);
- the confirmation of Proposition 2.13 is stated as "for l ≤ 3 on rotationally symmetric germs, and in their linear
  part for l ≤ 7 on general germs"; "show" → "indicate" where Proposition 2.13 (outline) is used.
Also (N-a overlap item): A now quotes both bounds of the note's Theorem B.
