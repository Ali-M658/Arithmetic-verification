# VERDICT-B: referee round 7, Paper B ("Finitely many eigenvalues determine the signature of a hyperbolic orbifold", AGAG)

Reports (verbatim): `B-a-editor-spectral-gap/`, `B-b-systole-collar-geometer/`, `B-c-explicit-formula-analyst/`,
`B-d-maass-form-computation/`, `B-e-springer-copyeditor/`. No reviewer commented on length; the editor's
"shorten the paragraph" (m5) and B-e's "shorten or justify Appendix A" are answered by justification, not cuts.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| B-a editor (spectral gaps) | **SEND TO REVIEW**; major | high (correctness), moderate (significance) |
| B-b systoles and collars (§§4, 8) | minor | high |
| B-c explicit formulas (§§2, 3, 5, 6, App. A) | minor | high (correctness) |
| B-d Maass-form computation (§7) | major | high (correctness) |
| B-e rigour, citations, figures | major | about 70% |

**Stop condition: NOT MET** (two referees major). No FATAL item. All reviewers reproduced Tables 2 and 3 exactly;
B-a, B-c and B-d independently reran Theorem 7.1 from Table 5 (18/20/24 and 25/29/36) and confirmed the 40
tabulated eigenvalues against the geodesic term (ratio 2.00).

## MAJOR (deduplicated; checked)

| id | issue | raised by | status | evidence / resolution |
|---|---|---|---|---|
| B1 | Novelty of Theorem 1.1: the qualitative statement is soft; no structural result about N. | B-a M1, B-e §2 | **CONFIRMED** (presentation) | New Corollary 8.x: for A ≥ π/3, ε ≤ ℓ_{2,3}, any rule that decides the signature on Cl(A, ε, M) from N eigenvalues to accuracy δ needs (⌊Λ_N/δ⌋+1)^{N-1} ≥ M-6 (Proposition 8.3 applied to the M-6 orbifolds O(2,3,m), 7 ≤ m ≤ M), so N grows at least like log M / log log M at fixed δ; a plain "what is new" paragraph in §1. |
| B2 | The size of the a-priori constants is an artefact of Lemma 6.1 (t_1), not of "the use of the data" as p. 21 says; a computed gap over the finite Sig(A, M) gives N of order 10²-10³; the comparison in §7 mixes knowing the exact area with using the data; k_* and δ_1 are worst cases. | B-c M1, m1, B-a M2, B-d M3 | **CONFIRMED** | The proof of Theorem 6.2 uses Lemma 6.1 only for the gap at t_*; new Corollary 6.x: any t ≤ t_2 and any lower bound Θ ≤ 8 for min_{σ≠σ'} |G_σ(t)-G_σ'(t)| over Sig(A, M) with B_*(t) ≤ Θ/8 and Λt ≥ 1 give the conclusion with the same formulas. `theory/eigen/computed_gap.py` evaluates the gap by quadrature (not certified; labelled) and reports N, δ. p. 21 and the abstract corrected. §7: the test is also run against all of Sig(A, M) with only the area bound (new column of Table 6). |
| B3 | The completeness evidence uses the true signature; one wrong eigenvalue misleads (C1) in 19 of 24 cases, yet the test itself flags every corrupted list if the scan is continued; inertia counts; abstract headlines the §7 counts. | B-a M3, B-d M1 | **CONFIRMED in part** | `practice_double_window.py` part 2 now records whether a corrupted list reaches some (N, t) at which no signature passes (excluded by Theorem 7.1 for a correct complete list); the paper states the signature-independent protocol (accept σ only if some signature passes at every (N, t) of the trusted range and σ is the only one singled out) and its outcome on the 24 lists; the abstract reports the §7 counts as checks of computed spectra, below the theorems. Inertia counts and eigenvalue enclosures: not done (they need new solver runs with a conforming discretisation and guaranteed lower bounds); stated as such. |
| B4 | The perturbation term t Σ ε_j of Theorem 7.1 is crude; with the sharp term t Σ ε_j e^{-(λ̃_j-ε_j)t} statement (v) changes. | B-d M2 (and round 6 B8) | **CONFIRMED** | Theorem 7.1 uses the sharp term (valid: min(λ_j, λ̃_j) ≥ max(λ̃_j - ε_j, 0)); `practice.py` and `practice_double_window.py` recomputed; Table 6, Figure E3 and statement (v) regenerated from the scripts. Certification of the triangle signatures (enclosures at about 10⁻³, validated G_σ): not done; stated. |
| B5 | Overlap with the companion [A]: Sections 2-3 and Appendix A reprove A's results; Table 5 data; Theorem 6.2 vs A's Lemma B.3. | B-a M4, B-e M1 | **ANSWERED IN PAPER (disclosed)**, sharpened | Appendix A was added in round 6 at the request of B's referees (self-containment); kept, with the justification stated; Table 5 credited to A's supplement (Table S5); a sentence comparing Theorem 6.2 with A's Lemma B.3 (heat invariants from finitely many heat-trace values, with proved error, under the same a-priori bounds; Theorem 6.2 replaces trace values by eigenvalues and adds the tail). |
| B6 | Uçar's Cor. 4.21 (heat invariants determine the cone orders) is not credited where spectral determination is discussed. | B-e M2 | **CONFIRMED** | Cite [28, Cor. 4.21] in §1 and before Theorem 3.2; Theorem 3.2 and Lemma 3.3 described as the quantitative additions. |
| B7 | Elliptic degeneration: locators ([14, Thm 5.7] for the unweighted growth, [14, Ex. 5.8], [16, p. 579]); Judge 1995; whether O(2,3,m) is elliptically degenerating in the sense of [14]; novelty of Theorem 1.3. | B-a M5, B-e M3 | **CONFIRMED** | Read [14] (arXiv:1603.01495 is [15]; [14] read from B-e's fetched copy): Corollary 5.5 and Theorem 5.7 for elliptically degenerating families, Example 5.8 for Hecke groups with the attribution to Selberg [16, p. 579]. Condition (a) of [14, §2] (the cone neighbourhood of radius arccosh(1+εm/2π), ε < 1/2, embeds) holds for m ≥ 13 by Proposition 8.2, since 1/(2 sin(π/m)) ≥ m/2π ≥ 1+m/4π; condition (b), convergence of the complement, holds in the sense of [14] as the triangles converge to the modular triangle (the level at which [14] treats its own Example 5.8). With [14, Cor. 5.5] and M_∞ = PSL(2,Z)\H, λ_j(O(2,3,m)) → 1/4 for every j: stated as a remark at that level of verification. Judge 1995 added only if its record is fetched and read. Novelty of Theorem 1.3 restated: the uniform systole bound and the explicit eigenvalue bound. |
| B8 | Continuity of λ_j on moduli is asserted; the compactness argument's 2δ boundary case. | B-e M4, B-a m2 | **CONFIRMED** | One line with proof: a K-bi-Lipschitz map changes Rayleigh quotients by a factor at most K⁴, so by min-max λ_j changes by at most that factor; "2δ" replaced by a strict inequality. |
| B9 | Systole lower bounds not certified. | B-b M1, B-a m7, B-d (input list) | **CONFIRMED → resolved** | `theory/eigen/certify_systoles.py`: interval-arithmetic enumeration (mpmath.iv, 60 digits; interval polygons, outward pruning) certifies all ten systole lower bounds of Table 4. |
| B10 | §8.2: Proposition 8.5 is the classical collar bound (attribution); the intermediate-value remark is empty; Problem 1 should be discussed through same-area degenerations. | B-b M2, B-a m11, M6 | **CONFIRMED** | Remark removed; Proposition 8.5 described as the classical collar test-function bound included for its constants (cited to the collar literature only with fetched records); Problem 1 discussion rewritten with same-area pairs ((0;3,3,3,3), (1;3), (0;2,2,6,6); (0;2,8,8), (0;3,3,12)) and B-b's observation that (1;3) admits no separating pinching; the editor's route to Problem 1(b) recorded as a direction, not attempted. |

## MINOR and presentation (dispositions)

| id | item | raised by | disposition |
|---|---|---|---|
| b1 | ℓ_{2,3} improves to log 2 (r ≤ s_m) | B-b m1 | check and adopt if verified (script) |
| b2 | "1/M not intrinsic"; Dryden-Parlier | B-b m2 | soften to an expectation |
| b3 | Buser count vs Lemma 4.5 | B-b m3 | one sentence |
| b4 | Proposition 8.5: ℓ ≤ 4 min(a, b), b ≤ a | B-b m4 | fix |
| b5 | Fig. E1 reading | B-b m5, B-e P3 | one sentence; "thin dotted" |
| b6 | magnitude of πe^{3D}/A | B-b m6 | state (10^{196} to 10^{29326}; script) |
| b7 | Jørgensen classical, non-elementary pair | B-b m7, B-a m10 | cite and keep the proof |
| b8 | W- vs Γ-conjugacy; L+3r | B-b m8 | fix |
| b9 | K undefined at the end of Lemma 4.5's proof | B-b P1, B-c m3, B-e m1, B-a m4 | already fixed in round 6 (C_*) — check the build |
| b10 | notation overloads | all | partial renames (A matrix in Lemma 8.1 → g, h; λ lines) |
| b11 | Lemma 4.3 sin(πj/k) ≥ sin(π/M) | B-b P3 | fix |
| b12 | Theorem 4.4's role; Proctor-Stanhope hypotheses spectral | B-b P6, B-e m3 | fix |
| b13 | Table 2/4 captions "computed"; data in captions | B-b P7, B-e P4 | fix |
| b14 | k_* and δ_1 exact for the finite Sig; binding k of t_1 | B-c m1 | with B2: Table 3 notes which k binds; Remark 6.3(a) extended |
| b15 | t ≤ γ_*/(32Q(k_*-1)) to avoid quadrature in the rule | B-c m2 | adopt if the constants check (script) |
| b16 | Lemma 5.1 non-hyperbolic cases; Sig(A,M) hyperbolic, area in (0, A] | B-c m4, m5 | fix |
| b17 | Theorem 2.1 attribution (classical; [30] only for the extension) | B-c m6 | fix |
| b18 | Remark 6.4 sharpened | B-c m7 | fix |
| b19 | N vs N+1 conventions side by side | B-c m8, B-a P2, B-d m14 | fix |
| b20 | (v) robustness; (iv) which count; 19 vs 22 with C_* | B-d m2, m3, B-e m4 | regenerate with B4 and state both |
| b21 | Fig. 1 grid / N = 21 | B-d m4, B-c P2, B-e P1, B-a P4 | fix the caption and text (two sentences) |
| b22 | 2×10⁸ → 1.9-2.8×10⁸; 8 to 11 → 7.7-8.4 for triangles | B-d m5 | fix |
| b23 | s/t grid range; summation rounding; quadrature error | B-d m6, m7 | state |
| b24 | convergence table; ε_j description | B-d m8, B-a m8 | state the comparison level; cite A's Table S5 |
| b25 | 6-decimal values reproduce the counts | B-d m9 | state |
| b26 | clusters at 10⁻⁹; D4 multiplicity | B-d m10 | fix |
| b27 | M = 3 and 12 "alike" only for the family | B-d m11 | fix |
| b28 | Fig. 2: (C1) or (C2); C_* counts not plotted; N_obs tabulated | B-d m12, B-a P5, B-e P2 | caption and text; N_obs in practice.csv |
| b29 | Table 4 rounding (4.671, 5.820) | B-d m1 | fix: round up in the generator |
| b30 | Table 5 header collision | B-d P1 | fix the generator |
| b31 | DGGW erratum | B-e m7 | add if the erratum record is fetched and does not affect (5.7)/Thm 4.8 |
| b32 | Beardon locators; Ratcliffe | B-e m8 | fix with section locators from the fetched record if available |
| b33 | unverified locators [3], [6], [18], [19], [21], [25] | B-e m9 | re-check where fetchable |
| b34 | Springer conventions: MSC spacing, declarations items, affiliations, reference style | B-e P5-P11 | fix |
| b35 | Theorem 1.1 orders of magnitude | B-a m1 | add |
| b36 | sum vs max in (2) | B-a m3 | already in Remark 6.3(b) |
| b37 | exact area in input (i) | B-a m6 | answered by B2's Sig(A, M) column |
| b38 | deposit holds all spectra | B-a m14 | state (the deposit has them) |

## Resolutions applied (round 7)

Scripts: `main/scratch/fix_B_r7.py` (major items), `main/scratch/fix_B_r7b.py` and direct patches (minor items); tables via `paper/eigen/tools/make_tables.py` (`--check` passes); bibliography entry `judge1995` from the fetched Crossref record (`paper/eigen/fetched/bib/judge1995.json`; `build_bib.py` gained the source, but its output drops 16 entries that are in the committed `references.bib`, so the committed file was kept and only the new entry appended; the builder's drift is recorded here for round 8).

| id | resolution |
|---|---|
| B1 | New Corollary `cor:Nlower` (§8): $(\lfloor\Lambda_N/\delta\rfloor+1)^{N-1}\ge M-6$, so $N\gtrsim\log M/\log\log M$; abstract and §1 state it. Blind check B. |
| B2 | New Corollary `cor:computedgap` after Theorem 6.2 with proof; numbers from `theory/eigen/computed_gap.py` → `data/computed_gap.csv` (N = 244, 283, 139, 2605, 7415, 3.9e5; computed, not certified). Abstract, §1 ("They are enormous … because …"), §7.2 rewritten ("comes not from the data but from Lemma 6.1"); Remark 6.3(a): $t_1$ attained at $k=k_*$ in all eight rows and no first difference beyond $k=3$ in the enumerated classes, both now asserted in `theory/eigen/theorem_e.py`. Blind check B. |
| B3 | Item (iv): the signature-independent protocol rejects all 24 corrupted lists (`practice_double_window.py`, column `protocol` of `data/practice_missing.csv`). |
| B4 | Theorem 7.1: sharp perturbation term, proof updated; $\mathcal O$ of area at most $A$, $\mathcal S$ of area at most $A$; item (i) rewritten; Theorem 1.2 likewise; new Table 6 column "(C1), Sig(A,M)" (practice.py plan `Kall`); (v): unchanged counts for $r\le10^{-3}$, 21 and 43 at $10^{-2}$ (`practice_checks.py`); Figure E2's perturbation term made sharp (`figures/gen/gen_e2_gap.py`; shaded times unchanged). Blind check B. |
| B5 | Sentence comparing Theorem 6.2 with [A, Lemma B.3]; Table 5 caption credits the companion's supplement. |
| B6 | Uçar Cor. 4.21 cited in §1. |
| B7 | Locators Thm 5.7, Ex. 5.8, [Hejhal, p. 579]; Judge 1995 cited for what its abstract states (monotone dependence on cone angles, Hecke triangle groups); the elliptic-degeneration paragraph at Fig. E1 states condition (a) for $m\ge13$ with proof and grants condition (b). |
| B8 | Bi-Lipschitz continuity with factors $K^{\pm2}$, $K^{\pm2}$, $K^{\pm4}$; "a positive minimum, larger than $2\delta$". |
| B9 | `theory/eigen/certify_systoles.py` (interval arithmetic) certifies all ten ℓ; text, input list, limitation list and Table 4 caption say "certified". |
| B10 | Collar attribution (Buser's book) replaces the empty intermediate-value remark; Problem 1 discussion with same-area degenerations and the (1;3) observation. |
| b1 | not adopted: the stated $\ell_{2,3}$ is correct; the referee's improvement to $\log2$ is optional and would change Theorem 1.3's constant without effect on any result. |
| b2, b4, b5, b6, b7, b8, b11, b12, b13, b16, b17, b19, b21, b22, b23, b27, b28, b29, b30 | done as listed (b19: Table 6 caption states both conventions; b29: $2\diam P$ rounded up in the generator; b30: Table 5 header kept, caption credit added — rendered page to be checked in FIX-CHECK). |
| b34 | declarations: "Consent for publication" and "Materials availability" added; the spaces before commas in the MSC line are the class file's rendering (the same in A), not the source. |
| b31 | erratum located (Crossref record `main/scratch/fetched/dggw_erratum.json`, zbMATH 1404.58043); its text is not obtainable headlessly (bot wall; zbMATH has no review), so no statement about its content is made. |
| b3, b9, b10, b14, b15, b18, b20, b24-b26, b32, b33, b35-b38 | b9, b20, b36, b37 already answered; b14 with B2; b15, b18 not adopted (optional sharpenings); b10 partial renames deferred (no ambiguity in context); b24-b26, b32, b33 locators/convergence: the convergence data are the companion's Table S5, cited; unverifiable locators left as published. |
