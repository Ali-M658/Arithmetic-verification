<!-- Editor B-a: returned text saved verbatim; the reviewer could not write files -->

I couldn't save the report: the write to `REPORT.md` was refused, so the full report follows. My decision is to send it to review, and my own recommendation is major revision. I found no fatal issue and no mathematical error, and every number I could recompute matches the manuscript.

# Handling editor's report: "Finitely many eigenvalues determine the signature of a hyperbolic orbifold"

Annals of Global Analysis and Geometry. Handling editor's assessment, written from the standpoint of spectral gaps and small eigenvalues of hyperbolic surfaces. I used only the submission and the three disclosed related manuscripts. Page numbers are PDF pages of the submission (34 pp.). I read the rendered pages before reporting any typographical or figure point.

## 1. Summary

The paper studies closed orientable hyperbolic 2-orbifolds with cone points. It fixes three bounds: area ≤ A, systole ≥ ε and cone orders ≤ M. Under these bounds it proves the following.

- **Theorem 1.1 / 6.2 (pp. 2, 13).** Explicit N(A, ε, M) and δ(A, ε, M) exist such that the first N eigenvalues, each known to within δ and with none omitted, determine the signature. The decision rule picks the signature σ ∈ Sig(A, M) whose signature term G_σ(t\*) is closest to Σ_{j<N} e^{−λ̃_j t\*}. The proof has four parts:
  - separation of heat invariants and an integrality bound on the first difference (Lemma 3.3);
  - enveloping remainders for the identity and cone expansions;
  - a count of closed geodesics from A, ε and M alone, with no diameter bound (Lemma 4.5, using cone-point separation, Lemma 4.2, and packing);
  - a Weyl-type tail bound (Prop. 5.2).
- **Theorem 1.2 / 7.1 (pp. 3, 16).** An a-posteriori test, run at one moderate time on given data. It is applied to computed spectra of O(2,8,8), O(3,3,12) and eight members of a (0;3,3,3,3) family. Criterion (C1) holds with N = 24 to 842 using the class-level count, against N = 4×10⁴ to 7×10¹² for Theorem 6.2. The paper says clearly that these are consistency checks.
- **Theorem 1.3 / Props. 8.2–8.3, Remark 8.4 (pp. 4, 23–24).** The order bound cannot be dropped:
  - the family O(2,3,m) has area < π/3 and systole ≥ 0.56206, uniformly in m;
  - λ_j ≤ 1/4 + π²(j+1)²/h_m², with h_m → ∞;
  - pigeonhole then gives pairs of different signatures whose first N eigenvalues agree to within δ.
- **Problem 1 (p. 26).** Whether the systole bound is needed is left open. Prop. 8.5, a pinching family, is given as background.

## 2. Significance and scope

**Scope.** The paper is within AGAG's scope.

**What is good.**
- The mathematics is careful and, as far as I checked, correct.
- The constants are genuinely explicit and reproducible. I reproduced Tables 2 and 3 to the printed digits.
- Lemma 4.5, the geodesic count without a diameter bound, is a clean, reusable lemma.
- The numerical claims are presented with unusual honesty:
  - error estimates are called estimates;
  - completeness of the eigenvalue lists is "supported, not proved";
  - systoles are labelled "floating point, not interval arithmetic".
- The paper is open about what it does not know:
  - the true order of N;
  - Problem 1;
  - whether [14] applies to the O(2,3,m) family.

**What limits significance.**
1. **The qualitative statement is soft.** It follows from Mumford–Bers compactness and [1], [5]; the authors give this argument themselves on pp. 2–3.
   - The signature is detected by the heat invariants, which are local data.
   - That is a much easier target than the Buser–Courtois question [6] on full isospectrality, so "effective counterpart" overstates the analogy.
2. **The effective constants have no practical content.** In Table 3, N runs from 4.3×10⁴ to 3.8×10³⁰ and δ goes down to 8.7×10⁻²⁷⁸. The constraint t₁ binds in 7 of 8 rows. It comes from the divergence of the cone expansion, not from any geometric obstruction.
3. **Theorem 7.1 follows in a few lines from the trace formula.** Its numerical demonstration only shows that spectra validated against the true signature's trace formula pass a trace-formula test for that signature (see M3).
4. **Theorem 1.3 is largely known.** It is Selberg/Hejhal spectral accumulation, in the quantitative form of Garbin–Jorgenson [14, Thm 5.3], plus an elementary uniform systole bound. Judge's paper on cone points degenerating to cusps is not cited: J. Amer. Math. Soc. 8 (1995) 715–759, doi:10.1090/s0894-0347-1995-1273415-6.

**Verdict.** Modest significance: a correct, careful, explicit packaging of known mechanisms, with a useful counting lemma and a necessity example. That can be enough for AGAG, but only if M1, M2, M5 and M6 are addressed.

## 3. Correctness, and what I recomputed

Scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/B-a-editor-spectral-gap/scratch/code/`: `consts.py`, `heatcheck.py`, `test71.py`, `perturb.py` and `extra.py`.

### Checked by hand (all correct)

- **Lemma 2.2(i), (ii).** Both integrations by parts, the identity x·e^{x/2−x²/4t} = −(2tx/(x−t))·d/dx e^{x/2−x²/4t}, monotonicity of B_C in ℓ, and the bound valid for all t.
- **Lemma 3.3.** d₂ = −1/12 for (4,4,4) against (3,4,6). d₃ = 25/12 for O(2,8,8) against O(3,3,12).
- **Lemmas 4.2, 4.3, 4.5 and Theorem 4.4.** The closed form of Theorem 4.4 uses arccosh(1+x) ≥ √(2x/(1+x)), which I also checked numerically.
- **Lemma 5.1, Prop. 5.2 and Lemma 6.1.**
- **Theorem 6.2.** This includes the derivation of y₀ (checked on the rendered p. 14), Λt\* ≥ 1, the 3Θ\*/8 margin, and the "same data, same minimiser" step behind the last sentence of Theorem 1.1.
- **Theorem 7.1.** (C2) implies (C1).
- **Section 8 geometry.**
  - Identity (3), with q = 1/2 − w′²/(4w²).
  - Triangle trigonometry for h_m and s_m.
  - The trace identity giving ℓ₂,₃ = 0.562063.
  - The Rayleigh quotients in Props. 8.3 and 8.5.
  - The case A < π/3 in Remark 8.4.

### Recomputed numerically

| Item | Result |
|---|---|
| α₀…α₄; a₀, a₁; b₀(m) | α = 1, −1/3, 1/15, −4/315, 1/315; a₀ = 1/12, a₁ = 1/360; b₀(m) = (m²−1)/(12m). All agree. |
| Table 2, all 12 entries | Reproduced exactly. The closed-form bound dominates D in every case. |
| Table 3, all 8 rows and every column | Reproduced to the printed digits. |
| C\* in Table 4 | 3.55e9, 4.0e5 and 9.45e9. Agree. |
| p. 15: N ≈ 4e18 if k\* = n\* | I get 4.19e18. |
| p. 15: N grows about 5× per halving of ε | I get ratios 5.24, 5.13, 5.01, 4.90, 4.81, 4.74, 4.67. |
| Systoles in Table 4 | Closed forms 2.2567679…, 1.8626041… and 2.633916 (ϑ = 0). The printed values are correctly rounded down. |
| \|S\| in Table 6 | 6 signatures and 3 signatures, as stated. |
| **Independent trace-formula check**, using only the 40 eigenvalues of Table 5 | Evaluating G_σ from the integrals of Theorem 2.1 myself, at t = 0.08–0.12 the difference Z₄₀ − G_σ equals 2.00–2.06 (O(2,8,8)) and 1.999–2.000 (O(3,3,12)) times the contribution of one systole-length geodesic class. That is exactly the pair γ, γ⁻¹, with the spectral tail below 10⁻¹¹. This confirms the normalisation of E_m, the first 40 listed eigenvalues of each orbifold, and the systoles. |
| **Table 6, triangle-orbifold rows**, computed from Table 5 alone | N = 18 (t ≈ 0.0565), 20 (0.0556), 24 (0.0431), 25 (0.0412), 29 (0.0403), 36 (0.0296). These match the paper; I padded ϵ_j by 5e-7 for the 6-decimal rounding of Table 5. No wrong signature was singled out at any (N, t). |
| **p. 17, item (iv): deleting or duplicating one low eigenvalue** | A wrong signature in 19 of 24 cases. Reproduced exactly. |

### Not checked

- The re-proof of Jørgensen's inequality (Lemma 8.1).
- The analytic details of Lemma A.1, Prop. 2.3 and Lemmas A.2–A.3, which are reproduced from the companion. I checked their consequences numerically.
- The (0;3,3,3,3) rows of Tables 4 and 6 and the data behind Fig. 3, because no data were supplied.
  - Fig. 3 is consistent with the proved bounds at m = 7: λ₁ = 44.89, below the bound of about 133.
  - It is also consistent at m = 4096, where the rescaled λ₁ is about 1.16.

## 4. FATAL

None.

## 5. MAJOR

**M1. The novelty of Theorem 1.1 is not established (pp. 2–5, 13–15).**
- The qualitative result is immediate, and the constants are far beyond any practical use.
- Nothing in the paper needs effectivity. There is no lower bound on the least admissible N; p. 15 says "we do not know the true order".
- The ingredients are standard: small-time separation, a systole bound on the geodesic term, and a Weyl tail. The separation input comes from the companion paper [30].
- *Needed:* a plain statement of what is new beyond [30] plus classical estimates, and at least one structural result about N. For example, a lower bound in M that quantifies Theorem 1.3, the true dependence on A, or whether growth in 1/ε is necessary.

**M2. The constants come from an avoidable bottleneck (pp. 13–16, Table 3, Fig. 1, Remark 6.3).**
- t₁ binds in 7 of 8 rows. It comes from bounding |G_σ − G_σ′| through the divergent cone expansion with worst-case separations: δ₁ = 1/(2·lcm(1..M)), and |b_K(M)| grows roughly like K!(M/π)^{2K}.
- Sig(A, M) is a finite, explicit set, and each G_σ(t) is an explicit integral. So min over σ ≠ σ′ of |G_σ(t) − G_σ′(t)| is a finite quantity that can be computed rigorously.
- Fig. 1 shows this gap is about 10⁻² at t ≈ 0.05, against Θ\* ≈ 10⁻¹⁸ in Table 3.
- Remark 6.3 lists three improvements and says they were not used.
- *Needed:* use a computed gap and report the resulting N and δ, or justify the worst-case formula. At minimum, implement Remark 6.3(a).

**M3. The a-posteriori test is fragile, and its demonstration is circular (pp. 3, 16–22).**
- Completeness of the eigenvalue lists (p. 19) was checked by comparing the computed heat trace with I + E for the *true* signature at t = 0.0015. That comparison alone already separates the true signature from all others by about 2×10⁸ error budgets.
- So Section 7.2 shows only that a smaller N, at a larger t, also works.
- My recomputation confirms the danger: one missing or duplicated low eigenvalue gives a confident wrong answer in 19 of 24 cases. A missed eigenvalue is the commonest solver failure, and the authors had to redo their own triangle spectra because of window-boundary misses (p. 18).
- *Needed:* either of the following; I prefer (a).
  - (a) A completeness certificate that does not depend on the signature, for the two triangle orbifolds up to λ̃₄₀. The route is already described on p. 17: Sylvester inertia counts for a conforming discretisation, plus guaranteed lower bounds of Liu–Oishi or Carstensen–Gedicke type.
  - (b) Demote Section 7 to a labelled illustration and remove its counts from the abstract's main claim.

**M4. Overlap with [30] (pp. 5–9, 28–30; see section 9).**
- About seven pages of [30] are restated and re-proved, some nearly verbatim. Lemma A.1's proof is [30]'s Lemma B.1.
- Table 5 duplicates values from [30]'s Table S5.
- The overlap is disclosed, so this is not misconduct, but AGAG could end up printing the same proofs twice.
- The sentence "nothing else here is taken from it" (p. 5) needs qualifying. [30, Lemma B.3 and Remark B.4] gets heat invariants from finitely many heat-trace values with a proved error, using the same order, systole, diameter and area bounds. That is the mechanism of Theorem 6.2 without the eigenvalue tail.
- *Needed:*
  - cite [30] for the duplicated proofs, or justify keeping them;
  - add a comparison of Theorem 6.2 with [30, Lemma B.3];
  - credit or cite [30]'s supplement for the Table 5 data.

**M5. Theorem 1.3: prior work and an unchecked hypothesis (pp. 4–5, 23–26).**
- Judge (1995) and the precise Selberg/Hejhal statement are missing.
- A uniform systole bound also follows, without an explicit constant, from convergence of the hyperbolic structures to PSL(2,Z)\H². The authors' own search shows the systole rising towards 2 arccosh(3/2).
- On p. 26, whether [14, Cor. 5.5] applies is described as "not checked". Checking that is the authors' job. Garbin–Jorgenson's stated motivating example is the closely analogous Hecke triangle family.
- *Needed:*
  - add the missing references;
  - decide whether the O(2,3,m) family is an elliptically degenerating family in the sense of [15];
  - if it is, state λ_j → 1/4 as a corollary; if not, name the hypothesis that fails;
  - adjust the novelty claim on p. 5 accordingly.

**M6. Problem 1(b) may be within reach of existing tools (pp. 26–27).** This is a request for discussion, not a condition of acceptance.
- The authors already have lim sup λ_j ≤ 1/4 (Prop. 8.5) and λ₁ → 0. What remains is a lower bound λ_j ≥ 1/4 − o(1) for 2 ≤ j < N.
- The collar analysis of Wolpert, Ji and Huntley–Jorgenson–Lundelius is local, and the pinched geodesic lies away from the cone points.
- Pass to a fixed torsion-free finite-index cover. Invariant eigenfunctions there converge to eigenfunctions on the cusped orbifold limit.
- That reduces the question to eigenvalues of the limits in (0, 1/4).
  - For k = 3 the limit is two copies of (0;3,3,∞). This is the index-2 subgroup of PSL(2,Z), which contains Γ(2) and so is a congruence group of level 2.
  - As far as I know, the small-level checks of Selberg's eigenvalue conjecture rule out eigenvalues in (0, 1/4) there.
  - A second family of a different signature whose limit has the same property would answer (b) in the negative. The k = 4 limit, (0;4,4,∞), would need its own check.
- *Requested:* carry this out, or explain concretely which step fails.

## 6. MINOR

- **m1 (p. 2).** Theorem 1.1 is not self-contained. Give orders of magnitude for N and δ, or their simplified dependence on A, ε and M.
- **m2 (p. 3).** The continuity of λ_j rests on one parenthesis about bi-Lipschitz maps. Add a reference, or the line "a K-bi-Lipschitz map changes Rayleigh quotients by at most K⁴". Prop. 8.5 (p. 26) relies on this too.
- **m3 (p. 8, eq. (2)).** The remainder uses the *sum* of the identity and cone remainders. The companion shows they have opposite signs, so the *maximum* suffices. That is sharper, already proved, and would slightly improve t₁.
- **m4 (p. 12, end of the proof of Lemma 4.5).** "≤ Ke^x": K is undefined and should be C\*. Confirmed on the rendered page.
- **m5 (p. 14).** The paragraph beginning "We do not prove that such a K exists" is a digression. Shorten it.
- **m6 (pp. 16–17).** Input (i) requires the exact area. Only E_N needs an area upper bound, so either run the test over all of Sig(A, M) or drop the remark.
- **m7 (p. 19).** The systoles of the two triangle orbifolds can be certified by exact trace arithmetic in Z[2cos(π/m)]. That removes one caveat at negligible cost.
- **m8 (p. 19).** Say which of the two discretisations the estimate ϵ_j is meant to describe. The companion's Table S5 shows much larger differences against the (0.07, 10) and (0.1, 10) levels.
- **m9 (pp. 17, 21).** Table 6 mixes the two N conventions in one row (see P2).
- **m10 (pp. 22–23).** ⟨A, B⟩ is non-elementary under the stated hypotheses, so classical Jørgensen [41], [35, Thm 5.4.1] applies directly. Cite it and drop the proof.
- **m11 (p. 26).** The intermediate-value remark ("N = 2 is too small") adds nothing. Remove it.
- **m12 (p. 26).** The observations "decreases in m" and "suggest λ_j → 1/4" should become the corollary of M5, or be cut.
- **m13 (pp. 4–5).** Add Judge (1995). Cite Hejhal's specific statement rather than all of [16].
- **m14 (p. 27).** The deposit should contain the full eigenvalue lists for all ten orbifolds. From Table 5 I could rerun only the two triangle rows.

## 7. Presentation

- **P1 (pp. 1–2).** The abstract is overloaded with caveats. State the theorem, the necessity of the order bound, and one sentence on the numerics.
- **P2.** Unify the N convention. Theorems 1.1 and 6.2 use λ̃₀ to λ̃_{N−1}; Theorems 1.2 and 7.1 use λ̃₀ to λ̃_N.
- **P3.** Too many symbols are overloaded:
  - ε, ϵ_j, ϵ, ϵ_X;
  - δ, δ_k;
  - p, used four ways;
  - a;
  - A (area, and the hyperbolic element in Lemma 8.1);
  - Λ, Λ_N.
- **P4 (p. 15, Fig. 1).** The grey competitor curves are unlabelled, and the dotted curves for N = 21 and N = 100 cannot be told apart.
- **P5 (p. 22, Fig. 2).** There is no legend; the meaning of markers and colours is only in the text on p. 21. The class-level counts the abstract headlines (24–842) are not plotted.
- **P6 (p. 26, Fig. 3).** The dashed bounds are hard to match to their curves.
- **P7 (pp. 14–21).** The prose is dense, and proved and computed statements are interleaved. A "Numerical observation" environment would help.

## 8. Honesty of the numerical claims

This is a real strength of the paper.

- **Error estimates** are presented as estimates, not bounds (p. 19). No λ̃_j is claimed as a proved upper bound, and no lower bounds are computed.
- **Completeness** is "supported … not proved" (p. 19), and the paper names a failure mode its check cannot see.
- **Systoles** are labelled floating point.
- **Section 7** is described as "consistency checks on orbifolds of known signature, not proved determinations".
- **The asymptotic observations** are flagged as properties of the formulas.

The only over-statement is one of emphasis: the abstract headlines the a-posteriori counts (M3, P1).

## 9. Overlap with the disclosed manuscripts

**"How much of a hyperbolic orbifold does heat hear?" ([30], AGAG).**
- The overlap is substantial and disclosed:
  - Theorem 2.1 = [30, Thm 2.3, Lemma B.1];
  - Lemma 2.2 ≈ [30, Lemmas 2.4–2.5];
  - Prop. 2.3 = [30, Prop. B.2];
  - Lemmas A.2–A.4 = [30, Lemmas 2.6, 2.8, 2.10, 3.1];
  - Lemma 3.1 = [30, Lemma 3.3];
  - Theorem 3.2 = [30, Cor. 3.5, Thm 3.8(i)].
- Several of these proofs are near-verbatim. The spectra, the method description and the code deposit are shared, and Table 5 reprints [30]'s Table S5.
- The two papers are consistent. I checked:
  - the heat-invariant counts M (within Sig≤M) and M+1 (against all of Sig);
  - d₃ = 25/12;
  - the diameters 2.448 and 2.158;
  - about 2850 eigenvalues per triangle orbifold;
  - each paper's account of what it contains.
- [30, Lemma B.3] is the closest relative of Theorem 6.2 and should be discussed (M4).
- New here: Lemma 3.3, Sections 4–6, Theorem 7.1 and its runs, and Section 8.
- The two papers should share at least one referee.

**"Triples with equal sum and equal reciprocal sum" ([31], Integers).** No overlap of results. It is cited only for the coincidence S = 18, R = 3/4, which is consistent across all three manuscripts.

## 10. Editorial decision and recommendation

- **Decision: SEND TO REVIEW.** The paper is in scope and, as far as I can check, correct. Its numerics are reproducible and honestly qualified. My objections concern significance and presentation, which call for referee judgement rather than a desk rejection.
- **Suggested referees:**
  - an expert in inverse spectral geometry and trace formulae on orbifolds, ideally the same person refereeing [30];
  - an expert in validated eigenvalue computation, for M3.
- **Recommendation: MAJOR REVISION.**
- **Confidence:**
  - high in the correctness of the main theorems;
  - moderate in the significance judgement, which I would put at borderline for AGAG unless M1 and M2 are answered.

## 11. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | A precise statement of what is new, plus one structural result about N (e.g. a lower bound in M). |
| M2 | A rigorously computed gap over the finite set Sig(A, M), and/or Remark 6.3(a)–(c); report the new N and δ, or justify the worst-case formula. |
| M3 | A completeness and enclosure certificate that does not depend on the signature, for the triangle orbifolds up to λ̃₄₀; otherwise demote Section 7 and remove its counts from the abstract. |
| M4 | Cite instead of re-proving, or justify the duplication; compare with [30, Lemma B.3]; credit Table 5 to [30]'s supplement. |
| M5 | Add Judge (1995) and the precise Selberg/Hejhal reference; settle whether [14], [15] apply and state the corollary or the failing hypothesis; adjust the novelty claim. |
| M6 | Attempt (b) via a torsion-free cover and the cusped limits' spectra below 1/4, or explain which step fails. |
| m1–m14 | Local edits, as described in each item. |
| P1–P7 | Rewrite the abstract, unify N, reduce notation clashes, label figures directly, separate numerical observations. |
