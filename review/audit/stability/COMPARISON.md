# Phase 2: blind review compared with the existing proofs (STABILITY)

**Files read (read-only):**

- `theory/stability/proof.md`, `STATUS.md`, `attack-log.md`;
- `threshold.py`, `threshold_output.md`, `threshold_results.json`.

`REVIEW.md` is left unchanged. Grade changes are recorded only in the addendum at the end.

**New scripts for this phase:**

- `check_selberg.py` (output in `check_selberg.txt`): an independent derivation of α_j from the Selberg identity
  term.
- The ε_cert values printed in `threshold_output.md` were re-certified exactly at 3 s.f. with `s5_lib.Cert`.
  All 11 rows are certified.
- I re-ran the authors' δ_up search procedure for (2,2,2,2,3), reimplemented from `threshold.py`.

## Per item

### ST.0 Setting

**(a) Route.** Same conventions and the same recovery map. The proof states the weighted homogeneity
without proof; I checked it exactly.

**(b) Selberg cross-check of α_j, j ≤ 11.** I cannot see `stab_common.alpha_smooth_selberg`, so I
re-derived the cross-check myself.

- The identity term of the trace formula, as fetched (Dryden–Strohmaier eq. (1)), is
  (μ(F)/4π)∫ r h(r) tanh(πr) dr, with h(r) = e^{−(r²+1/4)t}.
- Write r tanh(πr) = |r| − 2|r|/(e^{2π|r|}+1). The Fermi–Dirac moments are
  ∫₀^∞ r^{2k+1}/(e^{2πr}+1) dr = (1−2^{−2k−1})|B_{2k+2}|/(4(k+1)).
- This gives α_j = [t^{j−1}] e^{−t/4}[1/t − Σ_k (−t)^k (1−2^{−2k−1})|B_{2k+2}|/(k+1)!].

This agrees **exactly** with Uçar (4.35) at K = −1 for every j ≤ 15. The values for j ≤ 11 are
1, −1/3, 1/15, −4/315, 1/315, −4/3465, 382/675675, …, −311192456/1581170716125. As a separate numerical
check, the integral matches the series to O(t⁷) at t = 0.05 and t = 0.02.

The paper's claim is therefore **sound**: the two derivations are genuinely independent (an integral
transform of the identity term versus Uçar's lune and sphere computation). This closes the one ST.0 item
that `REVIEW.md` left unchecked.

**(c)** No change.

### ST.1 Proposition S1

**(a) Route.** Same. The proof defers the leading coefficient of p_ν to `theory/cone-coefficients/`. My
`REVIEW.md` derives it in two lines from (4.25)/(4.33), and the proof could absorb that.

**(b)** No numerical discrepancy.

### ST.2 Front-end tables

**(a) Route.** Same.

**(b)** No discrepancy in any table entry. The claim that κ_r lies in 0.02–3.7 on "every test multiset"
rests on `front_end_output.md`, which I did not read. On the 11 table rows it holds, with maximum 3.699.

### ST.3 Lemma S2.1

**(a) Route.** **Different.**

- *Authors.* Differentiate the identity M(G(e))e = b(G(e)) to get M = −N·D_eG and D_I e = −M⁻¹N. Then
  - det N = −e_n/∏(2j+1), from a cyclically permuted triangular matrix;
  - det D_mI, via a Vandermonde determinant in m_i²;
  - det D_m e = ∏(m_i − m_j).
- *Mine.* Prove det B directly by divisibility (an explicit kernel D = z²k(z) when m_i = −m_j), degree
  counting, and an m_n → 0 induction for the constant. Then det M = det B/det S.

I checked the authors' sign bookkeeping line by line and it is correct:
(−1)ⁿ·(−e_n/∏)·(−∏(2r−1)(−1)^{n(n−1)/2}∏(m_i+m_j)/e_n²) = (−1)^{n(n+1)/2}∏/e_n.

The density argument needs Theorem B's identity to hold as an identity of rational functions on
{e_n ≠ 0}. The black-box statement grants this.

**(b)** Neither route depends on the other, so the two are mutually confirming.

### ST.4 Lemma S2.2

**(a) Route.** B = S·M is proved the same way. det B differs:

- the authors get det B from det S·det M and Lemma S2.1;
- I prove det B first and deduce S2.1.

There is no circularity, because their S2.1 is proved independently via the Jacobians.

**(b) W_D defect.** The defect I reported is **not real**. The statement defines f(z) = E(z²) + zO(z²), so
E and O are polynomials in w = z². With that convention, E_f O_D − E_D O_f is a polynomial in w of
degree ≤ n−1, exactly as stated. My reading treated O as the odd part in z. The authors' proof uses the
convention consistently: (Md)_j = [z^{2j+1}](zO_D − T E_D), and E_f(zO_D − T E_D) ≡ zW_D(z²).

**Orlando citation.** The proof cites "Orlando" for det B. The source-register error stands: the
Holtz–Tyaglov text was fetched under the wrong arXiv ID, 1005.2843 instead of 0912.4703.

**(c)** ST.4: MINOR → **NONE** (see the addendum). The citation item stays MINOR.

### ST.5 Theorem S2

**(a) Route.** Same: the majorant chain, Hadamard on M⁻¹ = B⁻¹S with column norms ≥ 1, the residual
bound, and Neumann. The authors bound tan((n+η)β) − tan(nβ) ≤ ησ_k directly. The step that needs η ≤ 1
(sec² is monotone and nβ + sηβ ≪ (n+1)β) is only implicit there; my version spells it out.

Part (c), "D_I e = −M⁻¹N exact (Lemma S2.1)", is not among my statements. It is the formula derived
inside the proof of Lemma S2.1.

**(b)** No discrepancy.

### ST.6 Ostrowski

**(a)** The proof text is the statement itself; there is nothing more.

**(b)** Both defects are **carried into the proof**:

- "where γ is the largest root modulus" does not say that γ = Max(|x_ν|, |y_ν|) ranges over both
  polynomials (counterexample f = z², g = z² − z);
- the ε formula is a silent re-indexing of the printed (69,3)–(69,4).

**(c)** MINOR stands.

### ST.7 Lemma S3 and ST.8 Theorem S3

**(a) Route.** Identical. The authors' sum is written Σ_{j=0}^{n−1}(3/2)^j, the same quantity as mine.

**(b)** No discrepancy. The attack log reports a worst displacement of 0.981·r_a for the k-th root, so the
3ⁿ constant is nearly attained for some k. The theorem's hypotheses are consistent with my
observation that the radius condition always binds.

### ST.9 Proposition S3.2

**(a)** No proof beyond the statement. The numbers agree with mine and with the attack log.

**(b)** The missing non-degeneracy hypotheses in (ii) are **carried**: a ≠ 0, g(0) ≠ 0, and
∏(z_i+z_j) ≠ 0, which fails for example when g(−a) = 0.

**(c)** MINOR stands.

### ST.10 Remark S3.3 and ST.11 Theorem S4

**(a) Route.** Same. For S4 the authors argue ĝ_a ≥ 1/μ; I argue min(g_a, μ) ≥ 1. These are equivalent.

**(b)** No discrepancy. `threshold.py` additionally asserts that δ_thm itself passes the S5 certificate.

### ST.12 Proposition S5

**(a) Route.**

- The certificate in `threshold.py` (`_common`, `certify_abs`, `certify_coherent`) is the same algorithm
  as mine, step for step.
- **The radius set is the same for both tests**: RADII = {1/2, 19/40, …, 1/40, 1/100, 1/1000}.
- **The G derivation matches mine.** The authors use G = (−M⁻¹N)L⁻¹, where N = ∂(Me − b)/∂I. I use
  G = M⁻¹J L⁻¹ with J = ∂(b − Me)/∂I = −N.
- One extra guard: the code also requires E ≥ 0, which is automatic once (I−A)⁻¹ ≥ 0.

**(b) Discrepancies.**

1. **The written proof is a two-line sketch.** It does not state:
   - why (I−A)⁻¹𝟙 > 0 implies ρ(A) < 1 (Collatz–Wielandt / M-matrix);
   - that this also gives invertibility of M(Ĩ);
   - why the tan majorant bounds the tanh remainder.

   My `REVIEW.md` §ST.12 supplies all three.
2. The cross-reference "(Lemma S2.1)" for G is explained by the proof: D_I e = −M⁻¹N is derived inside the
   proof of S2.1. My sub-point (a) becomes a wording issue only.
3. The proof says the "Rouché argument is that of Theorem S4", but it never states that the radius list
   needs r < (minimum gap). This is fine for integer orders.

**(c)** MINOR stands. The reasons are now (b), (c) and (d) of `REVIEW.md`, plus the sketchy proof.

### ST.13 δ_up and rounding

**(a) Route.**

- Same two shapes in principle.
- In `counterexample()`, however, the complex-pair shape is tried only when the order has multiplicity ≥ 2,
  and the remaining polynomial g has degree n−2 with a removed twice.
- The optimiser is Nelder–Mead on the **unscaled** coefficients of g, from two starts: x₀ = coefficients of
  ∏(z − rest) and x₀(1+10⁻³). It uses 80,000 evaluations, then a restart.
- Mine is SLSQP on the epigraph form of the max-norm, with relative scaling of the coefficients and several
  starts, followed by a Nelder–Mead polish.

**(b) Why their (2,2,2,2,3) search missed the 5.3113e-05 tie.** I re-ran their exact procedure (same
objective and starts, with my H implementation):

| start | result | evaluations |
|---|---|---|
| x₀ | stalls at 5.7448e−05 | full 80,000 |
| x₀(1+10⁻³) | 9.7e−03 | full 80,000 |

Their run ended at about 5.7427e−05 (`threshold_results.json`), which prints as 5.743e−05.

- The scaled epigraph solve reaches **5.31132e−05**. Nelder–Mead restarted *at* that point stays at
  5.311320e−05, so it is a genuine local minimum of the same objective.
- The two configurations are close: g has roots 2.970, 1.962 ± 0.422i, 1.606 at my point, against
  2.970, 1.962 ± 0.424i, 1.606 at theirs.
- So the miss is a **non-converged Nelder–Mead on a non-smooth max-norm** objective. The simplex stalls at a
  kink. In the 4-dimensional, badly scaled coefficient space of n = 5 this is not a different basin.

The n ≤ 4 rows agree with mine to 4–5 significant figures. The (3,10,15,30) row differs at the 4th figure:
theirs is 7.48714e−3, mine 7.48652e−3, and both print as 7.488e−3 when rounded up.

**Downstream statements that are now too strong:**

- *Text.* proof.md §5 and §7 say "7.3 for the n = 5 case"; the ratio is ≤ 6.72.
- *Log.* attack-log.md and STATUS.md say "The empirical failure thresholds match δ_up" and "No cheaper
  failure exists below δ_up". These were tested only on the four rows (2,8,8), (3,3,12), (3,10,15,30)
  and (4,5,21,28), and they are false for (2,2,2,2,3).

The printed δ_up remains a valid upper bound, so no theorem is affected.

**(c)** MINOR stands. **Fix:**

- reprint δ_up = 5.312e−05 and the ratio 6.72;
- use a smooth epigraph solver, or certify convergence, in `counterexample()`;
- restrict the "tightness" sentence to the rows actually tested.

### ST.14 Results table and artefacts

**(a)** Numbers: every printed δ_thm, δ_cert and ε_cert agrees with `threshold_results.json`, and with my
exact recomputation.

**(b) Discrepancy (artefact provenance).** The committed `threshold_output.md` **was not produced by the
committed `threshold.py`**:

- *Header and columns differ.* The file says "(from threshold.py; …)" with a column "failure at"; the code
  writes "(generated by threshold.py)" with a column "worst root at".
- *ε_cert rounding differs.* The file prints ε_cert to 3 s.f. **rounded down**: 8.25e−04 for (4,4,4), from
  8.2594e−04; 4.39e−04 for (2,2,2,3), from 4.3988e−04. The code prints `f"{float(rlo):.3e}"`, which rounds
  to nearest and has 4 s.f.
- *The closing line is not emitted.* The file ends with "All printed delta_cert values re-certified exactly";
  the code never writes this line and never re-certifies the printed strings. It certifies the bisection
  value and prints fmt_down of it, which relies on monotonicity.

All values printed in the file are nevertheless correct. I re-certified exactly every printed δ_cert
(4 s.f.) and every printed ε_cert (3 s.f. as in the file, and 2 s.f. as in proof.md).

**(c)** The table stays NONE. New artefact item, **MINOR**: regenerate `threshold_output.md` from the
committed script, or commit the script that produced it, and make the script re-certify the printed
decimals.

## Addendum: grade changes

| item | REVIEW.md grade | revised | reason |
|---|---|---|---|
| ST.0 | NONE | NONE | The Selberg cross-check is now independently confirmed, exactly for j ≤ 15. |
| ST.4 Lemma S2.2 | MINOR | **NONE** | The W_D finding is withdrawn. With f = E(z²) + zO(z²), W_D is a polynomial in w as stated. |
| ST.12 Prop S5 | MINOR | MINOR | Sub-point (a) is reduced to wording, because the proof of S2.1 derives D_I e = −M⁻¹N. The written proof is a sketch and should include the Collatz–Wielandt and invertibility steps. |
| ST.13 | MINOR | MINOR | Root cause identified: non-converged Nelder–Mead. STATUS.md and attack-log.md tightness claims are also overstated for (2,2,2,2,3). |
| new: artefacts | — | MINOR | `threshold_output.md` does not match the output format of the committed `threshold.py`, although its values are all correct. |

No item is FATAL or SERIOUS, and there are no new SERIOUS or FATAL items.

## P3 verdict (unchanged)

Proposition S5 is a valid certificate. The authors' implementation and mine are the same algorithm, with
the same radius sets and the same G. Every printed δ_thm, δ_cert and ε_cert is exactly reproduced and
re-certified, and every printed δ_cert is the maximal 4-s.f. certified value. The soundness probe passed:
22,184 exact samples, 0 failures. All δ_up values are valid upper bounds. The (2,2,2,2,3) value is 8% too
high because the optimiser did not converge.
