<!-- Saved verbatim by the main session from the reviewer's returned text: the harness refused the reviewer's own write. Checking scripts (check.py, check2.py, check3.py, cert_est.py) are in its git-ignored scratch/. -->

# Editor's assessment: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold" (Gang, Agadi, Veluri, Wang, Barreto, Chouthaiwale)

Submitted to: Annals of Global Analysis and Geometry. Handling editor's assessment, written from a background in comparison geometry and spectral convergence.

Page numbers are those of the submitted PDF (23 pp.). The author-contribution, AI-use and Zenodo-DOI placeholders (pp. 20–21) are treated as known and are not counted as defects.

---

## Summary

The setting is a closed orientable hyperbolic 2-orbifold O with cone points. Dryden–Strohmaier showed that its full Laplace spectrum determines the signature σ(O) = (g; m_1,…,m_n). The submission asks whether finitely many approximate eigenvalues already determine it.

**Main theorem (Thm 1.1 / Thm 6.2, pp. 2, 12–13).** Take the class C(A, ε, M): area ≤ A, systole ≥ ε, cone orders ≤ M. The paper gives explicit N(A, ε, M) and δ(A, ε, M) such that the first N eigenvalues, each known to within δ, determine σ. The decision rule is also explicit: choose the σ whose signature term G_σ(t\*) of the Selberg trace formula is closest to Σ_{j<N} e^{-λ̃_j t\*}.

**How the proof works.**
- G_σ is moduli-independent. Its small-t expansion has fully enveloping remainders, alternating in sign with explicit bounds, for both the cone terms and the area term (Props 2.6–2.7).
- At the first heat invariant where two signatures differ, the difference is a nonzero integer multiple of a_{k-2} = |B_{2k-2}|/(2(k-1)!(2k-3)), or at least 1/(2 lcm) when the areas differ (Lemma 3.5). When the orders are at most M, this happens by the M-th invariant at the latest (Thm 3.4).
- The geodesic term is bounded through an explicit diameter bound D(A, ε, M) (Thm 4.4) and a geodesic-counting lemma (Lemma 2.2).
- The eigenvalues beyond the N-th are handled by a Chebyshev-type count (Prop 5.2).

**Further results.**
- **A-posteriori certificate (Thm 1.2 / 7.1, pp. 3, 14–15).** Applied to finite-element spectra of O(2,8,8), O(3,3,12) and eight members of a (0;3,3,3,3) family, it decides the signature with 21–750 eigenvalues. The a-priori theorem would need 4×10^4 to 7×10^12 (Table 3).
- **The order bound is necessary (Thm 1.3, §8.1, pp. 16–18).** For O(2,3,m) the area is below π/3 and the systole is at least 0.562 (via a reproved hyperbolic case of Jørgensen's inequality). A Rayleigh-quotient bound gives λ_j ≤ 1/4 + π²(j+1)²/h_m², and pigeonhole finishes.
- **Pinching example and Problem 1 (§8.2).** Whether the systole bound is needed is left open.

---

## Significance

**Fit.** The paper is within AGAG's scope: inverse spectral geometry of orbifolds via the trace formula, in the tradition of Stanhope's AGAG paper (ref. [8]) and Dryden–Gordon–Greenwald–Webb.

**What the effective theorem adds beyond compactness.** I asked this first. The authors raise the question themselves (p. 2), which I credit. My answer is mixed.

1. *As numbers, very little.* N ranges from 4×10^4 to 4×10^30 and δ goes down to 10^-278 (Table 2, which I recomputed; see below). Nothing is said about sharpness except that N = 2 is too small (p. 20). The authors concede they "do not know the true order of the least admissible N" (p. 14). An explicit but astronomically large and uncalibrated constant is, for most AGAG readers, only marginally more informative than the compactness constant.
2. *As a mechanism, genuinely more.* The compactness argument (Mumford–Bers compactness, continuity of λ_j on moduli space, Dryden–Strohmaier separation) goes through moduli space and gives no decision procedure. The heat-trace argument avoids moduli entirely:
   - the signature term is a closed-form function of σ;
   - the moduli enter only through an exponentially small geodesic term;
   - the integrality of the first heat-invariant difference (Lemma 3.5) supplies a quantitative gap with no modulus-of-continuity input.

   This is a clean "local invariants plus exponentially small global error" argument. It yields a computable rule, which compactness does not. This is the paper's real contribution, and the introduction should sell it as such rather than sell the numbers.
3. *The a-posteriori certificate is the most practically interesting part, but its headline overstates it* (M2, M3). The 21-versus-6.8×10^9 comparison mixes two effects. One is using data instead of worst cases. The other is using the true diameter of a known orbifold instead of the class bound D(A, ε, M). The certificate also presupposes the exact area and unproved numerical error bounds.
4. *Section 8 is the conceptually most interesting part for a comparison geometer, and the least positioned.*
   - "High orders behave like cusps" is elliptic degeneration in the sense of Garbin–Jorgenson, whose second paper proves convergence of small eigenvalues. The phenomenon goes back to Selberg/Hejhal's spectral accumulation for Hecke triangle groups. None of this is discussed.
   - The closest analogue of the whole paper, Buser–Courtois, *Finite parts of the spectrum of a Riemann surface* (Math. Ann. 287 (1990) 523–530), is not cited. They show that among genus-g surfaces with injectivity radius ≥ ε, the first m(g, ε) eigenvalues determine the spectrum. They conjecture m is independent of ε, which is the exact analogue of Problem 1.

   With this literature placed correctly, the paper reads as an effective, signature-level version of Buser–Courtois. That is a respectable AGAG contribution, not a breakthrough.

**Overall.** A careful, correct and well-executed paper. Its significance is moderate and currently overstated in places. It is publishable in AGAG if the positioning, certificate claims and duplication are fixed. It is not a paper I would fast-track.

---

## Correctness and what was recomputed (or checked)

I worked through every proof in §§2–7 and §8.1 at the level of an editor's check. These are not full refereeing, but I found no mathematical error. My own computations were done at 50 digits with mpmath, in `scratch/check.py`, `check2.py`, `check3.py` and `cert_est.py`.

| Item | What I did | Result |
|---|---|---|
| α_0,…,α_3 (p. 6) | Recomputed from the defining formula, with μ_k by quadrature | 1, −1/3, 1/15, −4/315 — agrees |
| Prop 2.6 (cone envelope) | Compared E_m(t) by quadrature with partial sums, m = 3 at t = 0.02 and m = 12 at t = 0.002, K = 0…5 | Sign (−1)^K and bound \|b_K(m)\| t^K hold in all 12 cases |
| Prop 2.7 (area envelope) | Same check at t = 0.05 and 0.3, K = 0…4 | Sign (−1)^{K+1} and bound \|α_{K+1}\| t^K hold in all cases |
| Lemma 2.3, second bound | Re-derived the two maxima and the counting integral | Agrees |
| Lemma 3.5, example (p. 9) | d_2 for (0;4,4,4) vs (0;3,4,6) | −1/12 = −a_0 — agrees |
| Fig. 1, d_3 (p. 14) | d_3 for (2,8,8) vs (3,3,12) | 25/12 — agrees (also with Paper A, §7) |
| Lemma 4.2 constant | Re-derived cosh d − 1 ≥ 2/(π²M²) and d_0 ≥ min(ε/2, 0.6/M) | Agrees |
| Table 1 (p. 11) | Recomputed D(A, ε, M) for all 12 entries | All agree to the digits shown |
| Table 2 (p. 13) | Recomputed k\*, D, t_1, t_3, N, δ and the binding constraint for all 8 rows | All agree, e.g. N = 3.75×10^30 and δ = 8.65×10^-278 in the last row |
| p. 13 claim "about 4×10^18" without k\* ≤ M (A = 10π, M = 3) | Recomputed with k\* = 14 | 4.19×10^18 — agrees |
| Prop 8.2: σ\* = 0.56206 | Re-derived: 4 sinh²(L/2)(1 + (3/4)cosh²(2s_∞)) ≥ 1 with cosh 2s_∞ = 5/3 | 0.56206 — agrees |
| Lemma 5.1(i): Area ≥ π/21; Remark 8.4 finiteness for A < π/3 | Re-did the case analysis | Agrees |
| Proof of Thm 6.2 | Checked the 3/8 budget (Γ\*/8 + Γ\*/8 + Γ\*/(8e) < 3Γ\*/8) and the index convention in Prop 5.2 | Sound |
| Certificate sensitivity (my estimate) | Rough model of Thm 7.1 for O(2,8,8): Weyl approximation λ_N ≈ 4πN/A, ε_j = 0, nearest gap ≈ (25/12)t | True diameter 4.9 → about 25 eigenvalues (paper: 21). Class bound D = 1125 → about 1.0×10^4 eigenvalues, above the ~2000 computed. See M2. |

**Not checked:** the finite-element spectra themselves (no access to code, and not my remit), and Appendix A beyond a read-through. Appendix A is identical to Paper A, Lemma B.1.

---

## MAJOR issues

**M1. Positioning against the closest literature is missing, which inflates the novelty of §1 and §8 (pp. 3, 16–20).**
- (a) Buser–Courtois (Math. Ann. 287 (1990) 523–530) prove the surface analogue of Thm 1.1 at the level of the full spectrum: among genus-g surfaces with injectivity radius ≥ ε, the first m(g, ε) eigenvalues determine the spectrum. Their m is non-effective, and they conjecture it does not depend on ε, which is Problem 1's question. They also remark that the injectivity radius is controlled by the number of eigenvalues in [1/4, 1]. That bears directly on whether the systole hypothesis could be replaced by spectral data.
- (b) Thm 1.3's mechanism, cone points of growing order becoming cusps, is elliptic degeneration (Garbin–Jorgenson, Kodai Math. J. 43 (2020); Enseign. Math. 64 (2018), which proves convergence of small eigenvalues). It goes back to Selberg's spectral accumulation for Hecke triangle groups (Hejhal, LNM 1001). The paper cites [13] only for the heat-function trace formula.
  - The statement on p. 18 that λ_j → 1/4 is not proved looks closable. The small-eigenvalue convergence of Garbin–Jorgenson, together with the absence of eigenvalues in (0, 1/4) for PSL(2, ℤ), should give λ_j(O(2,3,m)) ≥ 1/4 − o(1). Prop 8.3 supplies the matching upper bound.
- (c) The pinching discussion and Problem 1 (pp. 18–20) should engage the spectral-degeneration theory for pinched geodesics: Wolpert, *Spectral limits for hyperbolic surfaces I, II* (Invent. Math. 108 (1992)); Ji, JDG 38 (1993); Hejhal, Mem. AMS 437; Schoen–Wolpert–Yau; Dodziuk–Pignataro–Randol–Sullivan. The input the authors call "missing" (λ_j ≥ 1/4 − o(1) for 2 ≤ j < N along a pinched family) is what this theory provides for surfaces.
  - For O_{3,b} versus O_{4,b'}, the limits are two copies each of (0;3,3,∞) and (0;4,4,∞). If neither limit has eigenvalues in (0, 1/4), the first N eigenvalues of both families tend to (0, 0, 1/4, …, 1/4). That would answer Problem 1 negatively in the δ > 0 formulation of Thm 1.1.
  - This is my reading, not a verified claim. The authors must at least separate the δ > 0 question, which degeneration theory may settle, from the exact-equality question, which is the Buser–Courtois conjecture.

**M2. The certificate comparison in Table 3, Fig. 2 and the abstract (pp. 1, 3, 15–16) is not like-for-like.** Thm 7.1 uses the instance's true systole, a diameter bound for the specific orbifold (twice the longest side, about 4.9) and its exact area. Thm 6.2 uses only the class bounds A, ε, M and the diameter bound D(A, ε, M), which is 1125 for M = 12 at A = π/2.
- The geodesic term carries a factor e^{3·diam}. Most of the gap between "21" and "6.8×10^9" is therefore knowledge of the geometry, not the a-posteriori use of the data.
- My rough model of Thm 7.1 for O(2,8,8) reproduces the paper's count with diameter 4.9 (about 25 versus 21). With D = 1125 it needs about 10^4 eigenvalues, beyond the ~2000 computed.
- An orbifold whose diameter and systole are known is in practice an orbifold whose signature is known. What the certificate certifies in the paper's examples is therefore that the computed spectrum is consistent with the trace formula, not the signature of an unknown orbifold.
- The authors should:
  - (i) report the certificate with class-level inputs (ε and D(A, ε, M)) next to the instance-level ones;
  - (ii) state plainly which inputs are spectral and which are geometric;
  - (iii) rephrase the abstract's "certifies the signature of a computed spectrum" accordingly.

**M3. The certificate needs inputs the paper does not supply rigorously (pp. 14–15).** Thm 7.1 requires two things for every j ≤ N:
- rigorous enclosures |λ̃_j − λ_j| ≤ ϵ_j; and
- completeness, meaning no eigenvalue is missed up to λ̃_N.

The spectra come from "high-order finite elements and error estimates" (p. 15), and the only accuracy evidence given is agreement between two meshes (p. 18). Conforming finite elements give upper bounds. Guaranteed lower bounds and completeness need validated methods (Liu–Oishi-type lower bounds, Lehmann–Goerisch, or trace-formula completeness tests as in Strohmaier–Uski, CMP 317 (2013), and Booker–Strömbergsson–Venkatesh, IMRN 2006). Neither of the trace-formula references is cited, although both use the Selberg trace formula on computed spectra much as §7 does.
- Unless the ϵ_j and completeness are certified, "certificate" and "certifies" should be withdrawn in favour of "a-posteriori test".
- Thm 7.1 also assumes the area is known exactly: S consists of signatures *of area A*. Finitely many eigenvalues do not determine the area. The theorem should allow S to contain signatures of different areas, which costs only the δ_1 = 1/(2L) gap, and Table 3 should use that version so it matches Thm 6.2's class Sig(A, M).

**M4. Undisclosed duplication with the companion Paper A, which is simultaneously submitted to this journal** (its supplement is headed "Annals of Global Analysis and Geometry"). Details are under Overlap below. About five to six of the 23 pages repeat Paper A, much of it verbatim, while p. 3 says only that A "contains a sharper and more general form of Theorem 3.4". Self-containment is a legitimate choice. But the overlap must be disclosed result by result, the duplicated proofs compressed, and A described accurately: it is submitted, not "in preparation" as p. 3 says. Both papers must go to the same referees, or referees must at least see both, so that nothing is credited twice.

**M5. Length: several sections do not earn their place.**
- (a) **Lemma 8.1 (pp. 16–17)** reproves the hyperbolic case of Jørgensen's inequality "because we could not obtain the text of [16]". That is not an acceptable reason in a journal article. Jørgensen's inequality is Thm 5.4.1 of Beardon's book, which is the paper's own reference [15]. The groups involved, a hyperbolic element and an order-3 rotation not preserving its fixed-point pair, are non-elementary, so the textbook statement applies. Delete the lemma and cite Beardon (about one page saved).
- (b) **Lemma 4.1 (H1)–(H3) (pp. 9–10)** are textbook hyperbolic trigonometry (Beardon §7). State them with references.
- (c) **The diameter machinery (§4, pp. 9–11)** enters only through Lemma 2.2's factor e^{3·diam}. It is responsible for the t_3 ≈ ε²/(24D) constraint wherever t_3 binds, and the a-priori counts for those rows are linear in D. A Buser-type count of closed geodesics in terms of area and systole (cf. Buser, *Geometry and Spectra of Compact Riemann Surfaces*, Lemma 6.6.4 and the thick–thin decomposition), adapted to cone points with orders ≤ M, would remove the dependence on diameter. It might make most of §4 unnecessary and shrink N where t_3 binds. The authors should either do this or explain why a diameter-free count fails for orbifolds.
- (d) **Duplicated material from Paper A (M4).**

A realistic target is 16–18 pages.

---

## MINOR issues

- **m1 (p. 13, Thm 6.2).** δ = min{1/t\*, Γ\*/(8eNt\*)}: the term 1/t\* is never used in the proof. Remove it or say why it is there.
- **m2 (p. 3, Thm 1.2; p. 14, Thm 7.1).** Thm 1.2 takes N+1 approximate eigenvalues but sums only over j < N. Say in the statement that λ̃_N serves only the tail bound.
- **m3 (p. 15).** The diameter bound used for the eight O_ϑ is not stated. "Twice the longest side" is stated only for triangles, and for a quadrilateral the diameter can be a diagonal. Table 1's caption says "at most 7.8" without saying how this was obtained.
- **m4 (p. 13, Table 2).** Explain the choice of ε = 1.8626, 2.634 and 0.694 (the systoles of the examples). Add a t_2 column or say that t_2 never binds.
- **m5 (p. 2).** Sig(A, M) contains signatures without cone points and of every area ≤ A. Say so where it is defined. Thm 7.1's S, by contrast, has a single area (see M3).
- **m6 (p. 4, Lemma 2.2).** Say that oriented, non-primitive classes are counted, so that the Hyp sum in Thm 2.1 matches.
- **m7 (p. 3).** "None of the three bounds is a matter of convenience for the method" sits awkwardly with Problem 1 and with M5(c). Rephrase it as "each is used".
- **m8 (p. 18).** "the computed values suggest λ_j → 1/4, which Proposition 8.3 does not prove": see M1(b). Either prove it from Garbin–Jorgenson or cite it.
- **m9 (p. 20).** "The N of Theorem 6.2 grows like ε^{-3} log(1/ε)" repeats p. 14, which calls this "observations on the formulas, not proved asymptotics". Keep the qualifier, or prove it; it is elementary from the formulas.
- **m10 (p. 21, data statement).** The repository sits under an account that does not obviously belong to any author ("Ali-M658/Arithmetic-verification"). An archived DOI is essential (placeholder acknowledged). Name the scripts that produce Tables 1–3.
- **m11 (p. 6).** The parenthetical agreement with Uçar and Schueth is useful, but "neither agreement is used" should say what is used: the derivation from Thm 2.1.
- **m12 (p. 17, Prop 8.2).** The ball claim relies on the 2m-tile star P. A sentence on why γP and P have disjoint interiors for γ outside the stabiliser would help.
- **m13 (pp. 1–2, abstract).** The last sentence of the abstract is compressed to the point of opacity ("an integer multiple of an explicit rational number reached by the M-th invariant at the latest"). Rewrite it, and state the certificate's inputs honestly (M2).
- **m14 (references).** Add Buser–Courtois; Garbin–Jorgenson (Enseign. Math. 2018); Hejhal (LNM 1001 and Mem. AMS 469); Wolpert 1992; Ji 1993; Strohmaier–Uski 2013; Booker–Strömbergsson–Venkatesh 2006; Buser's book.

---

## Presentation (figures and captions included)

The prose is economical and the logical structure is clear. Theorems are stated with all constants, which I appreciate. Density is sometimes excessive: several proofs (Lemma 2.3, Prop 2.7, Lemma 8.1) are run-on chains of inequalities with little signposting. I viewed the rendered pages (pp. 1, 3, 7, 12–16, 19). Typesetting is clean, and I found no sign errors or broken formulas in the rendered text (the garbling in the extracted text is an artefact of extraction).

- **Fig. 1 (p. 14).** There is no legend. Of the five grey competitor curves only (0;3,3,12) is identified, and two of the top curves nearly coincide. The shaded window where the decision is possible (t ≈ 0.05) is a sliver that is hard to see. Label the curves directly, mark the window clearly, and state t\* for comparison.
- **Fig. 2 (p. 16).** The caption does not explain the marker code. Open/filled (M = 3/12), circles/diamonds/squares (N_obs/N_apr/a priori) and the two colours are explained only in the text on p. 15. The open diamonds (N_apr, M = 3) are hidden under the filled ones because the two sets are nearly equal (33–694 versus 38–750). Put the key in the caption or a legend. Per M2, add the class-level certificate counts.
- **Fig. 3 (p. 19).** This is a good figure. Panel (a): the 0.25 tick on the log axis is unlabeled as the bottom of the continuous spectrum; add a dashed line labelled 1/4, as the text says there is. Panel (b): the text (p. 18) says the rescaled values "approach j² slowly". Visually, j = 2…6 plateau about 5–12% above j² from m ≈ 100 on, with no visible approach. Either say they plateau above j² at the computed range, or show the trend.
- **Tables.** Tables 1–3 are correct as recomputed. Table 3's caption should say that S is the equal-area class while "N of Theorem 6.2" refers to Sig(A, M) (see M3).

---

## Overlap with the disclosed manuscripts

**Paper A ("How much of a hyperbolic orbifold does heat hear?", 39 pp. + 14 pp. supplement).**

| Paper B | Paper A | Nature of overlap |
|---|---|---|
| Thm 2.1 (trace formula, heat function) | Thm 2.3 | Same statement; proof paraphrased |
| Lemma 2.2 (geodesic count) | Lemma 2.4 | Verbatim |
| Lemma 2.3 (first bound and monotonicity) | Lemma 2.5 | Verbatim; B adds a second all-t bound |
| Lemma 2.4 (closed form of Φ_m) | Lemma 2.6 | Verbatim |
| Lemma 2.5 (moments) | Appendix B, proof of Prop 2.7 | Same computation |
| Lemma 2.8 (cone polynomials) | Lemma 2.8 | Verbatim |
| Lemma 3.1 (heat data of a signature) | Lemma 3.3 + Lemma 2.10 | Near-verbatim |
| Lemma 3.2 (parity) | Lemma 3.1 (first half) | Verbatim |
| Thm 3.3 (separation, ⌊A/π⌋+4) | Thm 3.4 / Cor 3.5 | B's is the weaker form |
| Thm 3.4 (bounded orders, M invariants) | Thm 3.7(i) | Proof verbatim |
| Appendix A (heat function admissible) | Lemma B.1 | Verbatim |
| Computed spectra of O(2,8,8), O(3,3,12) and the 8-member (0;3,3,3,3) family (§7, Fig. 2) | §7 and Supplement S4–S6 | Same data sets, used for a different purpose |

**What is new in B:**
- Props 2.6–2.7: fully enveloping remainders, which A does not have (A has only O(t^K) asymptotics).
- Lemma 3.5: integrality of the first difference.
- §4: the diameter bound.
- §5.
- Thm 6.2.
- Thm 7.1 and the certificate.
- All of §8: Jørgensen, O(2,3,m) and pinching.

That is a distinct and substantial contribution, so this is **not salami-slicing**. The split is sensible: A is about local short-time invariants and their arithmetic (the Prouhet–Tarry–Escott connection), B about global finite spectral data. **No proof in B depends on A**, as claimed. Every borrowed result is reproved.

The cost is that about 5–6 pages (most of §§2.1, 2.2 and 3, and App. A) duplicate A while p. 3 discloses only Thm 3.4. Recommended handling: a short paragraph or table in §1 listing exactly which results reproduce A. Either keep short proofs, if self-containment is wanted, or cite A once it is accepted. Remove the verbatim duplication of proofs in any case. A's own disclosure of B (A, p. 4) is accurate.

**Arithmetic note ("Triples with equal sum and equal reciprocal sum", 12 pp.).** No overlap with B. B only mentions the pair (2,8,8)/(3,3,12) as an example. The note discloses B correctly.

**Coordination.** A and B are both in this journal's system. I will assign at least one common referee, or share both manuscripts with all referees, so that the duplicated lemmas are refereed once and the novelty of each paper is judged against the other.

---

## Recommendation

- **Decision:** send to review. It is in scope and correct as far as I could check (all three tables recomputed exactly). It has a clean and genuinely non-compactness mechanism and an interesting necessity result. The problems (positioning, overstated certificate, duplication, length) are fixable in revision and are not grounds for a desk reject.
- **Desk-reject probability (my prior before deciding):** 0.25. The arguments for rejecting are moderate significance (the qualitative statement is a compactness corollary of Dryden–Strohmaier and the explicit constants are of no practical use), the missing Buser–Courtois positioning, and the verbatim overlap with a simultaneously submitted companion.
- **Expected referee outcome:**

  | Outcome | Probability |
  |---|---|
  | Accept as is | 0.03 |
  | Minor revision | 0.12 |
  | Major revision | 0.55 |
  | Reject | 0.30 |

  The most likely outcome is major revision driven by M1–M3. Rejection becomes likely if a referee from inverse spectral geometry judges that Buser–Courtois-type results plus degeneration theory make the contribution incremental, or if the certificate cannot be made rigorous.
- **Confidence:** moderate-high on correctness of §§2–7 (checked and recomputed). Moderate on the literature claims in M1(c): the possible negative answer to Problem 1 is my reading of degeneration theory, not a verified result. High on the overlap assessment.

**Suggested referees' profile:** one from inverse spectral and trace-formula theory on hyperbolic surfaces and orbifolds; one from spectral convergence and degeneration, or validated eigenvalue numerics, for §§7–8.

---

## What resolves each issue

- **M1.** Add a "Relation to prior work" paragraph that:
  - places Thm 1.1 as an effective, signature-level analogue of Buser–Courtois;
  - places Thm 1.3 within elliptic degeneration (Garbin–Jorgenson; Selberg/Hejhal), then proves or cites λ_j → 1/4;
  - restates Problem 1 separately for δ > 0 and δ = 0, and checks whether Wolpert, Ji and Hejhal's pinching theory settles the δ > 0 case. If it does, include the answer; it would make the paper's account of which hypotheses are needed complete.
- **M2.** Add the certificate's counts with class-level inputs (ε and D(A, ε, M)) to Table 3 and Fig. 2. Separate the spectral inputs from the geometric ones. Rephrase the abstract and p. 3.
- **M3.** Either certify the ϵ_j and completeness with a validated method (and cite Strohmaier–Uski and Booker–Strömbergsson–Venkatesh), or replace "certificate" with "a-posteriori test" throughout. Generalise Thm 7.1 to S with unequal areas, using the δ_1 gap, and recompute Table 3 on that class.
- **M4.** List each result reproduced from Paper A in §1. Compress or cite the duplicated proofs. Correct "in preparation" to "submitted". The editor will coordinate refereeing.
- **M5.** Delete Lemma 8.1 and cite Beardon Thm 5.4.1. Cite Lemma 4.1 to Beardon §7. Try an area-and-systole geodesic count to remove or shrink §4, or explain why it fails with cone points. Target 16–18 pages.
- **m1.** Remove 1/t\* from δ, or justify it.
- **m2.** Clarify in Thm 1.2 that λ̃_N is used only for the tail.
- **m3.** State and justify the diameter bound used for O_ϑ.
- **m4.** Explain the ε values; add t_2 or note that it never binds.
- **m5.** Define Sig(A, M) explicitly (all areas ≤ A, surfaces included).
- **m6.** State the counting convention in Lemma 2.2.
- **m7.** Rephrase the sentence on p. 3.
- **m8.** Resolve with M1(b).
- **m9.** Keep the qualifier on p. 20, or prove the rate.
- **m10.** Give a Zenodo DOI and name the scripts behind Tables 1–3.
- **m11.** Say what is actually used instead of the Uçar/Schueth agreements.
- **m12.** Add the disjointness sentence in Prop 8.2.
- **m13.** Rewrite the end of the abstract.
- **m14.** Add the listed references.
- **Figures.** Fig. 1: legend or direct labels, a visible window, t\* marked. Fig. 2: key in the caption, no hidden markers, class-level certificate series. Fig. 3: labelled 1/4 line, and correct the "approaches j²" sentence.

---

Sources used for the literature checks:
- [Buser–Courtois, EPFL Infoscience record](https://infoscience.epfl.ch/record/161425)
- [Buser–Courtois, EPFL Graph Search](https://graphsearch.epfl.ch/publication/161425)
- [Garbin–Jorgenson, arXiv:1603.01494](https://arxiv.org/abs/1603.01494)
- [Garbin–Jorgenson, arXiv:1603.01495](https://arxiv.org/abs/1603.01495)
- Crossref and Semantic Scholar metadata for Ji (JDG 1993), Wolpert (Invent. Math. 1992), Strohmaier–Uski (CMP 2013), Booker–Strömbergsson–Venkatesh (IMRN 2006), Korevaar (JDG 1993) and Hejhal (Mem. AMS 469)
