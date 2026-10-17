# VERDICT-A: referee round 6, Paper A ("How much of a hyperbolic orbifold does heat hear?", AGAG)

Reports: `A-a-editor-wave-trace/`, `A-b-conical-defect-physicist/`, `A-c-power-sum-varieties/`,
`A-d-arithmetic-fuchsian/`, `A-e-reproducibility-referee/` (each `REPORT.md`, saved verbatim from the
reviewer's final message). No length remark occurred that needed excluding; remarks on caption style and
on where material sits are kept, since they concern presentation, not length.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| A-a editor (wave trace) | **SEND TO REVIEW**; own recommendation major revision | high on correctness, moderate on significance |
| A-b conical-defect physicist | major revision | high (§§2.1-2.3, App. B, S8), moderate-high (§2.4) |
| A-c power-sum varieties | minor revision | high (mathematics), medium (significance) |
| A-d arithmetic Fuchsian groups | major revision | high (mathematics), moderate (overall) |
| A-e rigour, citations, reproducibility | minor revision | high (about 85%) |

**Stop condition: NOT MET** (two referees recommend major revision; confirmed MAJOR items remain).

No reviewer found a false main result. Every reviewer recomputed a large part of the paper (cone
polynomials, enveloping remainders, all Table S1 pairs, Theorem 3.8 areas, Theorem B, the elliptic curve
and its descent, Section 5 enumerations, Table S4) and everything recomputed agreed, except the
introductory bracketing claim (A1 below).

## FATAL

None.

## MAJOR (deduplicated; checked against the repository)

| id | issue | raised by | status | evidence |
|---|---|---|---|---|
| A1 | The Introduction (`manuscript.tex` l. 185) says consecutive truncations of the expansion bracket the heat trace for t below (π/μ)². Proposition B.2 proves enveloping for the area and cone series separately, with remainders of opposite signs (−1)^{K+1} and (−1)^K; for the full trace neither the sign nor the next-term bound follows. | A-b M1 | **CONFIRMED** | Recomputed with `theory/eigen/eigen_common.py` (40-digit quadrature): (2;2), t=0.05, K=1: R=1.07754e-3 > next term 1.04167e-3; (4;2), t=0.05, K=2: R=−2.68431e-5, next −2.50496e-5; (3;2), t=0.2, K=2: R=−7.08e-6, next +1.07e-4 (opposite signs). Bracketing holds for O(2,8,8) and O(3,3,12) (cone part dominates). Bound (6) itself is true. |
| A2 | "It is algebraic only, since for a cone of non-integral angle and nonzero curvature the heat expansion has a different form [20]" (l. 308) attributes to Schueth (arXiv:2511.22255) a statement her paper contradicts; and the physics literature that computed cone coefficients for arbitrary angle is not cited. | A-b M2, A-e M1 | **CONFIRMED** | Fetched arXiv:2511.22255, p. 2: for full rotational symmetry "it plays no role at all whether n = 1/f′(0) > 0 is a natural number or not … these b_ℓ(C) depend rationally on f′(0)" (noted without proof); a different form occurs when f″(0) ≠ 0, excluded at constant curvature. Fetched Fursaev, Phys. Lett. B 334 (1994) 53 (hep-th/9405143), (3.26)-(3.28): a_{α,n} = Σ_k αc_k(α)G_{nk}, c_k polynomial in α^{-1}, c₂ ∝ c₁(2πα^{-1}+11)·…; Dowker, Class. Quantum Grav. 11 (1994) L137 (hep-th/9406002); Fursaev-Solodukhin, Phys. Rev. D 52 (1995) 2133 (hep-th/9501127). Metadata from the arXiv API. |
| A3 | Proposition 2.11: the pole-order step ("following Schueth's proof … to all orders"), the rotation invariance of Donnelly's polynomial, the passage from the metric jet to the K-jet, and the Duhamel computation on all of R² (no cut-off) are sketched; Proposition 2.13(ii) leaves three steps implicit (bumps do not touch cone terms or Ω₀; one θ with G_l(θ) ≠ 0 for all l ≤ L; bumps stay in the flat region). Remark 2.12 rests on computer algebra. | A-b M3, A-a M3 (A-e P4 calls the same steps compressed but checkable) | **CONFIRMED** (rigour; every conclusion agrees with the reviewers' independent checks) | `manuscript.tex` ll. 380-395, 420-425. Remark 2.12 already says it rests on computer algebra and is used nowhere else. |
| A4 | Figure 3: the open squares are described as "doubled Prouhet pairs" (caption) and as "the pairs that Proposition 3.12 gives from Prouhet's solutions" (text, l. 699). The plotted pairs are genus-1 against genus-0 pairs from the construction in the proof of Theorem 3.14(c); Proposition 3.12 yields only genus-0 pairs of equal size. The L ≥ 4 squares cannot be rebuilt from the paper. | A-c M2, A-e M2 | **CONFIRMED** | `figures/captions.tex` l. 22; `manuscript.tex` l. 699; Table S1 "Prouhet" rows are (1;…) against (0;…); generator `theory/signatures/genus.py::genus_pair` builds Z(c) ⊎ λZ(c′) from the Thue-Morse sets with c = −1/2, c′ = 1/2 (odd points 2i∓1), i.e. the proof of Theorem 3.14(c). |
| A5 | The physical framing does not describe what is measured: "explores a disc of radius about √t and learns only what lies in that disc" is wrong near a cone point of order m (influence out to about √t/sin(π/m)); "large orders are heard late" and "the part of the cone data that diffusion resolves before geometry enters" are imprecise or wrong (the cone series stops being informative at t ~ (π/μ)², before the geodesics enter at e^{−ℓ²/4t} once μ > 2π/ℓ; e.g. the minimal pair, (π/12)² ≈ 0.069 against ℓ²/4 ≈ 0.87); the count is of Taylor coefficients, not of diffusion time; the wave-trace picture is missing. | A-a M1, A-b m1, A-b P5 | **CONFIRMED** | Abstract (l. 113), Introduction ll. 123-127, Fig. 1 caption ("within a distance of about √t"). Flat-cone image sum: the j-th image of a point at distance r is at distance 2r sin(πj/m). |
| A6 | Significance and novelty are mis-weighted: "The weight of the paper is elsewhere: Theorem 1.1 …" presents a reformulation as the main result; the uniform, geometric results (Theorem 1.2, Corollary 1.5) should lead; "M+1 is attained" should say at large enough area; Lemma 3.7 (sign changes of a measure with vanishing moments) is classical and uncited; Theorem 3.4 is the odd-symmetric analogue of N(k) ≥ k+1. | A-a M2, A-c M1, A-a m2 | **CONFIRMED** (presentation and attribution) | `manuscript.tex` ll. 183, 193. |
| A7 | Section 6 recovers orders from approximate invariants whose error δ₁ the paper cannot supply from a heat trace; abstract and introduction present it as recovery from approximate data. | A-a M4, A-d M1 | **ANSWERED IN PAPER (partly)**: the paper says three times that it does not supply δ₁ (ll. 1060ff., §6). **CONFIRMED** as a gap that can be closed: (6), Proposition B.2(a) (|b_K| increasing in m) and Lemma 2.5 give a proved δ₁ from finitely many values of the heat trace under a-priori bounds. |
| A8 | Section 4: Corollary 4.1 and Theorem 4.2 are classical in substance (Huber, McKean, Selberg; Teichmüller dimension); listing Theorem 4.2 among "three analytic results [that] carry the counts" is wrong (no count depends on it). | A-d M2, A-a m3 | **CONFIRMED** (attribution, wording) | l. 185 "Three analytic results carry the counts". |
| A9 | Main-text results proved only in the electronic supplement: Theorem 6.2 (constants and proof, S3), the rank in Theorem 5.8 (descent, S7), Proposition S2.2 (used in §5.1). | A-e M3 | **CONFIRMED** | The proof of Theorem 6.2 in the paper is a pointer to S3; S7 holds the descent. (These were moved to the supplement in commit 3134dbd.) |
| A10 | Overlap: state exactly what is shared with the companions; the two results quoted from the note on p. 34 are unrefereed and should be marked as not used; the S ≤ 4800 enumeration is reported in both A and the note; the natural home of Theorem 5.8. | A-d M3, A-a O1-O2 | **ANSWERED IN PAPER (partly)** (ll. 187, 195 state the division; "no proof here depends on it"); **CONFIRMED** for the p. 34 quotation and the enumeration. Theorem 5.8 stays in Paper A: it is what proves Theorem 1.4(iii), a statement about orbifolds; the note cites it. |

## MINOR and presentation (deduplicated), with disposition

Fixed in the revision unless marked otherwise.

| id | item | raised by | disposition |
|---|---|---|---|
| a1 | (6): spell out which area and cone terms the truncation includes; give the sharper bound max(·,·) that follows from the opposite signs | A-b m10, A-b M1 | fix (with A1) |
| a2 | Prop 2.13(i) uses [13, Thm 4.20] for b_l(p) = K₀^l p_l(m)/m; derive it from locality, weight and Proposition 2.7; same for the K^l rule at the end of §2.3 | A-b m2 | fix |
| a3 | Last paragraph of Prop 2.13: which conclusions survive in that class, which L, "computable from c₁" fails there | A-b m3 | fix (state precisely) |
| a4 | "at K = 0, +1 the t⁰ coefficient determines the orbifold type": exact statement, orientable | A-b m4, A-e m5 | fix |
| a5 | n_O counts hyperbolic conjugacy classes; w_O counts γ and γ^{-1} separately | A-b m5, A-d m4 | fix |
| a6 | Lemma B.1 could be a citation (Hejhal, Iwaniec) | A-b m6 | fix (remark that it is included for self-containedness) |
| a7 | Uçar's normalisation of c_{S_k} in Remark 2.9 | A-b m7 | fix |
| a8 | Remark 2.12(b): KΔK coefficients single-method | A-b m8 | fix (say so) |
| a9 | S8(ii): primes above all entries do not divide the denominators | A-b m9, A-c (soundness) | fix |
| a10 | p. 29 vs S4: agreement windows 0.0015-0.03 vs t ≤ 0.025; Hyp(0.03) ≈ 7.8e-13 | A-e m1 | check against the computation and state one window, and whether Hyp was subtracted |
| a11 | "conservative bound" smaller than the error estimate for low modes (Table S5) | A-e m2 | fix the wording ("a second, independent difference", not "conservative") |
| a12 | "one command reruns every check" vs S8; software versions; timestamped protocol; deposit files for Table S1 | A-e m3, A-d m15 | fix (qualify; versions; name files); "blind" kept with its protocol described |
| a13 | [18] needs 0- and 1-form spectra or 0-spectrum plus χ | A-e m4 | fix |
| a14 | Attribute each PTE piece (L = 6 genus piece is Borwein-Lisoněk-Percival) | A-e m6 | fix after checking [46] |
| a15 | Chen's Identity 9 is for integer sets; "odd symmetric system in the sense of [3, §3]" extends it; Problem 4 phrasing is Chen's | A-e m7, A-c M1(d) | fix |
| a16 | Bibliography: de Gier; Dowker initials; "wrote in 1994"; [56] version | A-e m8 | fix after checking the records |
| a17 | "computed spectra of Sections 4 and 5" | A-e m9 | fix |
| a18 | Table 1 entries for T(L), a_l, T_g(L) | A-e m10 | fix |
| a19 | finiteness of signatures of given area (Cor 3.5) needs one line | A-e m11 | fix |
| a20 | Fig. 8 axis label vs dist | A-e m12, A-d P4 | fix (in the text: say the axis is dist) - figure labels are not changed beyond the axis quantity name, see note |
| a21 | Fig. 4(a) "schematic" in caption | A-e m13, A-a P4 | fix |
| a22 | two emergence thresholds (10 × budget vs 10³ × noise) | A-e m14 | fix |
| a23 | Lemma 5.3(ii): 101/168 = R⁻_{18,3} at (3,7,8) and why it is the maximum; (2,5,S−7) needs S ≥ 12 | A-e m15, A-d m8 | fix |
| a24 | Prop 2.13(ii): (0;3,3,3) has χ = 0 against χ = −2: c₂ does not fix χ in variable curvature | A-e m16, A-b P3 | fix |
| a25 | Notation clashes (ϱ, κ, C, a, ν, s, B, …) | A-e P1, A-b P1, A-c P1, A-a m6 | fix the clashes inside single arguments (κ in Prop 2.11 proof, ϱ in App. B, 𝔪_n); the global renaming of a and C is not done (Table 1 and the explicit warning stay) |
| a26 | captions of Figs 3, 5, 8 too long in their first sentence | A-e P2 | fix (shorten) |
| a27 | §2.4 relies on later results; forward references | A-e P3, A-a P5 | partly: a sentence at the start of §2.4 names what is used from §3 |
| a28 | m ≤ l − 2 in Prop 2.11(i) | A-a m9 | fix (say nothing is claimed) |
| a29 | Prop 2.13(i) "this fails": which assertion | A-a m7 | fix |
| a30 | domain of f(A) | A-a m8 | fix |
| a31 | "no bound o(k²) is known": sources | A-a m4 | fix (pigeonhole bound; [47, §1]) |
| a32 | area-class algorithm (a-priori bound on orders at fixed area) | A-a m5 | fix (S1) |
| a33 | minimal pair is also the collision of least area (two-line proof) | A-a m1, A-d m6 | fix (add, with proof and script) |
| a34 | stability "explicit constants" includes one matrix norm | A-a m11 / m10 | fix |
| a35 | Duistermaat-Guillemin; diffractive cones (Hillairet; Ford-Wunsch) | A-a m11 | fix (only references whose records are fetched) |
| a36 | Theorem 3.14(b) proof: K_mult(O(2,8,8)) = 3 needs only ≥ 3 | A-c m1 | fix |
| a37 | f(A) ≥ L+1 for A ≥ A_min(L) | A-c m2 | fix |
| a38 | Lemma 3.3 criterion circular as stated; define d for any pair | A-c m3 | fix |
| a39 | Def 3.10: the configuration contradiction is Z = −Z | A-c m4 | fix |
| a40 | Theorem 3.11 gap-counting sentence | A-c m5, A-e P4 | fix |
| a41 | Theorem B signs; Hurwitz normalisation | A-c m6 | fix |
| a42 | β ≥ 1; C ≥ N(1) unused; Lemma A.1 with n = (L−1)²+1 | A-c m7, m8 | fix |
| a43 | "cannot be lowered uniformly in the area" | A-c m9, A-a M2 | fix |
| a44 | classify the pieces of Example 3.17(iii) precisely | A-c m10 | fix |
| a45 | Table S1 exact s for L ≥ 6 | A-c m11 | fix (checksums of the data file) |
| a46 | Remark 3.18 / Problem 3: scope of the bound 220 | A-c m12 | fix |
| a47 | number and caption the table of T(L) bounds | A-c m13 | fix |
| a48 | systole of the (0;3,3,3,3) family asserted without proof | A-d m1 | fix (non-isometry from the distinct λ₁, or state the enumeration as the source) |
| a49 | "tests every order of the cone expansion at once" | A-d m2 | fix |
| a50 | growth of φ_k, |b_l| and the e^{−π²/(μ²t)} truncation error stated as deductions | A-d m3 | fix (label heuristic, except what Proposition B.2 proves) |
| a51 | K_mult(O(p,q,r); Sig) ≤ 3: proved, open or observed | A-d m5 | fix (state as open, with the search) |
| a52 | ψ is a morphism; ψ∘φ = id | A-d m7 | fix |
| a53 | Lemma S3.1 column indexing; Table S4 "non-real" pair | A-d m9, m10 | fix |
| a54 | "smaller P₃ has the larger heat trace" only for small t | A-d m11 | fix |
| a55 | Proposition S2.1 is a computation | A-d m12 | fix (relabel) |
| a56 | Prop 6.4 n = 1 and Theorem 6.2 n = 2 are algebraic only | A-d m13, m14 | fix |
| a57 | Fig. 5(a) grey curves; Fig. 7 p = 5 circle at the frame edge, p = 8 band | A-d P3 | caption text only (no labels inside figures) |
| a58 | display of φ in Theorem 5.8 | A-d P5 | fix |
| a59 | Fig. 6 "circular rim" | A-d P6 | fix |
| a60 | key₂ notation | A-d P7 | fix |
| a61 | duplicate theorem numbering (1.x and 3.x) | A-a P2, A-c P6 | no change: the map on p. 7 links them, and renumbering would break the cross-citations from Paper B and the note |
| a62 | Figs 1, 4(a), 6 informativeness | A-a P4 | no change to figures (every figure stays); captions clarified |
| a63 | anthropomorphic wording | A-a P6 | fix with A5 |
| a64 | Theorem 3.8 split; Example 3.6 "a handle costs …"; Theorem 3.13 parenthetical; S1 table of pieces | A-c P2-P5, P7 | fix P3, P5; P2, P4, P7 no change (structure kept) |

Note on a20 and a57: the standing rule is that no labels or annotations go inside figures. An axis title
naming the plotted quantity is not an annotation; it is changed only if it misnames the quantity.

## Plan

Fix A1-A10 and the items marked "fix". Mathematical changes (A3 proofs, A7 lemma, a33 least-area
statement, A5 wave-trace remark, a1 sharper bound) each get a script with asserts and a blind subagent
check. Move the proofs of A9 from the supplement into appendices of the paper. Keep the honest status of
every numerical statement.
