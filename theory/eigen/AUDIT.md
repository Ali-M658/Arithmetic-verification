# AUDIT: blind review of theory/eigen

## Verdict

**FREEZE WITH CHANGES.** The changes are listed below and have already been applied in this
session, so the committed fragments are the frozen versions.

- No reviewer found a FATAL issue.
- One group had SERIOUS findings: Group 4, necessity. They are two overclaims in the text about the
  systole hypothesis, not errors in a bound or a construction. Both are fixed by rewording, and
  nothing proved is lost.
- Every proved bound was independently re-derived and passed independent exact or high-precision
  checks.

## Procedure

1. `STATEMENTS.md` was generated from the fragments by `make_statements.py` at commit b7c3ebf. It
   holds every new statement verbatim, no proofs, and the verbatim manuscript statements the new
   results use.
2. Five reviewer agents were launched, one per group. Each saw only `STATEMENTS.md` and `sources/`;
   none read the `.tex` proofs, the scripts or `practice.md`. Each re-derived its statements,
   wrote its own code under `audit/<group>/`, and graded every statement.
3. The reviewers could not write report files, so each `REPORT.md` is the reviewer's returned
   text, saved verbatim by the main session with a one-line provenance comment.
4. The proofs were compared with the reports only after all five verdicts were in.

| group | statements | reviewer's grades | reviewer's code (all checks pass) |
|---|---|---|---|
| 1. diameter, counting | eig:sep, eig:balls, eig:diam, eig:233, eig:elem, eig:counttail, eig:hypall, eig:count | all NONE (3 advisory notes) | trig identities on 5600 random cases; eig:sep on 57,080 worst cases (min ratio 9.76) and 269 triangle groups + 12 quadrilateral groups; O(2,3,m) geodesics for m ≤ 150; 1.28 M signatures |
| 2. remainders | eig:remcone, eig:remarea, eig:Grem | all NONE; presentation MINOR | exact identities; 50-digit quadrature, m ≤ 20, K ≤ 8, 1e-4 ≤ t ≤ 3 |
| 3. Theorem E | eig:int, eig:gap, eig:E, eig:Mneeded | NONE, NONE, NONE (one MINOR), MINOR | 30,920 + 14,564 equal-area pairs exactly; the gap by 60–110-digit quadrature on three classes; the chain of eig:E for 8 classes; 20,000 synthetic perturbations; recomputed N = 6,831,617,376, δ = 4.149e-25 for (π/2, 1.86, 12), identical to the audited version (after M7: 6.818×10⁹, 4.17e-25) |
| 4. necessity | eig:rayleigh, eig:N1, Q_{k,b}, eig:N2, "what is not proved" | NONE, MINOR, MINOR, NONE for the bounds but **SERIOUS** for the final "in particular", **SERIOUS** for "what is not proved" | symbolic identities; geometry in PSL(2,R) and the hyperboloid; coarse FEM eigenvalues below every bound; growth of N(ε) |
| 5. locality | eig:loc | MINOR (wording) | symbolic ratio B/(C t^{-1/2}e^{-ℓ²/4t}); 3300-point monotonicity grid; 50-digit chain on 9 signatures × 7 systoles |

## SERIOUS findings and their resolution

**S1 (Group 4). The "in particular" of eig:N2 was true but irrelevant.** It said that for every
δ there are members of (0;3,3,3,3) and (0;4,4,4,4), in C(2π, ε, 4) with ε → 0, with
|λ_1 − λ_1'| < δ. The reviewer showed the same at a fixed systole, even with equality:
- Q_{k,b} is symmetric in a ↔ b, so λ_1 → 0 as b → 0 and as b → ∞.
- λ_1 is continuous in b, so by the intermediate value theorem the two families take a common
  value of λ_1 at a systole bounded below.

So the statement shows only that N = 2 is too small, which Theorem E never claims. It does not bear
on the systole hypothesis.
- **Comparison with our proof:** the proof is correct as written; the claim drawn from it was
  wrong in meaning.
- **Resolution:** the "in particular" is deleted. A paragraph after the proof records the
  reviewer's observation and says that eig:N2 does not bear on the systole hypothesis.

**S2 (Group 4). The first sentence of "What is not proved" overclaimed.** It said that eig:N2
shows the first two eigenvalues "cannot replace a systole bound".
- **Resolution:** the paragraph now begins "We prove no necessity statement for the systole
  bound", and its other inaccuracies are fixed:
  - the phrase "equivalently: whether N must grow" becomes "(N, δ) cannot be chosen independently
    of ε";
  - "requires … no eigenvalues in (0, 1/4]" becomes "one route is …";
  - the growth rate is corrected (M2 below).

## MINOR findings and their resolution

| # | group | finding | resolution |
|---|---|---|---|
| M1 | 3 (also found by the main session before the verdicts) | Remark eig:Mneeded read literally ("for every N, δ two of the O(2,3,m) with m ≤ M…") contradicts Theorem E for fixed M; and "area and systole do not bound the orders" needs A ≥ π/3, ε ≤ σ_0 | rewritten: for A ≥ π/3, ε ≤ σ_0 and every N, δ there is M = (⌊Λ_N/δ⌋+1)^{N−1} + 7 such that …; a sentence explains why A < π/3 is different |
| M2 | 3 and 4 independently | the growth of the theorem's N as ε → 0 was stated as 1/ε²; D ∝ 1/ε makes it ε^{-3} log(1/ε) | corrected in necessity.tex; `theorem_e.py` now checks the ratio about 8 per halving of ε |
| M3 | 3 | Z_b of Theorem eig:count was reused, with a different meaning, in Theorem eig:E | renamed 𝒵^♯ in eig:E, with the line justifying Hyp(s) ≤ 1 at s = t_*/2 and s = 1/Λ |
| M4 | 4 | pigeonhole: with K = ⌈Λ_N/δ⌉^{N−1} closed boxes two values may differ by exactly δ | K = (⌊Λ_N/δ⌋+1)^{N−1} half-open intervals [iδ, (i+1)δ); differences < δ |
| M5 | 4 | \|⟨n_P, n_R⟩\| fixes the angle only up to φ ↔ π − φ | the quarter of Q_{k,b} has three right angles and angle sum < 2π, so its fourth angle is the acute one (Lambert); the Klein-model description is added |
| M6 | 5 | "depends only on the signature and the systole" is ambiguous for two orbifolds; the M = 2 convention for surfaces is costly; the first inequality is strict and the constant qualitative | all three said in locality.tex |
| M7 | 2 | the factor e^{t/4} in the remainder constants is superfluous; with the sign alignment the remainders are enveloping and the sharp constants are \|b_K(m)\| and \|α_{K+1}\| | **adopted** as a strengthening. Propositions eig:remcone and eig:remarea now state the sign and the bound \|b_K(m)\| t^K, \|α_{K+1}\| t^K for every t > 0. Q(K) in Theorem E uses them (and the monotonicity of \|b_K\| = p_K/m in m). `remainder.py` checks the sign alignment exactly and both bounds with signs against 80-digit quadrature (error/bound up to 0.99995). All constants were recomputed |
| M8 | 2 | φ_k > 0 and strictly increasing for m > 1 | stated |

## Advisory notes not adopted (optional improvements)

| group | note | why not adopted |
|---|---|---|
| 1 | a mean-value argument gives cosh d − 1 ≥ 2/(πM²), a factor π better than Lemma eig:sep | not needed; D would improve by a constant factor only |
| 1 | the axis argument of eig:233 gives r ≤ s_m, hence σ = log 2 instead of 2s_m and 0.5621 | correct but not needed. Our proof is about axes (a point of the axis outside the cone balls), which is the reviewer's caution; the constant 0.5621 is kept |
| 1 | integrating by parts against the non-monotone weight in eig:hypall would be invalid | our proof integrates against e^{−2x}, the valid route the reviewer reproduced |
| 2 | ρ close to π/m makes the Cauchy bound nearly optimal | the bound is not used in Theorem E (exact \|b_K\| is) |
| 4 | using both sides of the collar improves 4π²(j+1)²/a² to π²(j+1)²/a² | cosmetic |

## What the audit did not cover

The reviewers checked the statements against the manuscript inputs as quoted in `STATEMENTS.md`.
Those inputs (the trace formula, Lemmas 2.4–2.5, Proposition 2.7 and its derivation in the
supplement, Lemma 3.3, Theorem 3.4, Corollary 3.5) were audited in earlier rounds and are not
re-audited here. Jørgensen's inequality is quoted from a secondary source because the primary is
unreachable headless (`sources/README.md`).
