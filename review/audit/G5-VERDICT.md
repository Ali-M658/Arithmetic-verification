# G5 (theorem freeze): verdict

## **FREEZE WITH CHANGES**

Every result was re-derived from its statement alone by a reviewer who had not seen the
existing proof, scripts or data. Afterwards each reviewer compared its derivation with the
existing proof. Nine reviews were carried out: audibility, signatures, locality, stability,
threshold and paper core, curvature and divergence, Diophantine, literature (P6/P7) and
cross-result consistency (P8).

- **FATAL findings: none.**
- **No theorem, lemma or proposition was found false.**
- The four **SERIOUS** findings all concern manuscript sentences in `paper/main.tex` (and one
  wording in the Diophantine notes). None concerns a proved result. Each must be changed
  before the text is frozen.
- All other findings are MINOR: missing hypotheses that the proofs already use, wording,
  citations and printed constants.

Evidence:

- `THEOREM-REGISTER.md`: one row per result, with verbatim statement, status and verdict.
- `review/audit/<group>/REVIEW.md`: the blind review.
- `review/audit/<group>/COMPARISON.md`: the comparison with the existing proof.
- `check_*.py` with outputs: exact arithmetic, real asserts, nonzero exit on failure.

## Required changes (blocking for the freeze of the text, not of the mathematics)

### SERIOUS

1. **Degeneracy localization** (main.tex, sentence before `prop:scaling`, and again in
   §"Exact enumeration").
   - The claim that interval separation localizes every degeneracy to contacts between
     *adjacent* least-order strata is **false**. 2793 of the 3067 pairs with S ≤ 600 join
     strata whose least orders differ by at least 2. The first is at S = 35:
     (5,15,15) ~ (7,7,21).
   - Fix: describe the enumeration as exhaustive, and state that N counts unordered pairs.
     The table values are correct.
2. **Density section** (`conj:density`, the birthday heuristic, the abstract's
   "c ≈ 0.0085–0.0093", "stabilizes", "quadratic-order").
   - The conjecture is contradicted by exact enumeration: N(S)/S² falls from 0.0094 at
     S = 400 to 0.00405 at S = 6000. Its "equivalently N(S) = Θ(S)" is not an equivalence,
     and "a positive proportion, of order 1/S" contradicts itself.
   - The heuristic miscounts the candidate values: there are ≍ S⁶ of them, not O(S³).
   - Fix: withdraw all of these. Replace them with the Diophantine section:
     - Theorem 4: (c_iso + o(1)) X log X;
     - Theorem 5: X (log X)²;
     - Theorem 3: fibres of every size;
     - the isolation theorem;
     - a revised conjecture N(S) = S^{1+o(1)}.
3. **`rem:ncone`** is out of date and wrong as worded.
   - Theorem A proves K_mult ≤ n for every n. K_iso = ∞ for n ≥ 4 (Corollary 2.3).
   - A three-coefficient witness at n = 4 exists: {3,10,15,30} / {4,5,21,28}, so the
     "neither a construction nor a non-existence proof" sentence is false.
   - Fix: replace the remark with Theorems A and C and Corollary 2.3. Also update the
     conditional labels in `rem:nconerestated`, `prop:Kinf` and `thm:locality`.
4. **Coefficient indexing in the fibre claim** (`theory/diophantine` notes, DI.11).
   - "share a₀ and a₁" uses Uçar's indexing. Under the paper's t^ℓ indexing it is false:
     the S = 136 fibre has three different t¹ coefficients.
   - Fix: write "share c₁, c₂ (equivalently R and S₁)" wherever the fibres are stated.

### Priority and prior art (P6, P7): required wording changes

5. **P6.** Replace "none of it counts coefficients or exhibits a sharp finite boundary"
   (§Locating the novelty (a)). DGGW Thm 5.15 is an explicit one-coefficient determination
   for χ ≥ 0.
   - Keep the narrow claim "first exact finite-coefficient determinacy threshold, with an
     explicit minimal degeneracy, for a family of hyperbolic cone orbifolds". Tie it to
     DGGW Rem. 5.16, which poses this question.
   - Narrow any "first finite count" to "the first explicit count, ⌊Area/π⌋+4, uniform over
     all closed orientable hyperbolic 2-orbifolds".
   - Add Dryden–Strohmaier (2009) as a citation. Wording is in `PRIORITY.md`.
6. **P7.** Do not cite Müller et al. (arXiv:1311.5493, FoCM 16 (2016) 69–97) as giving
   Theorem A; it does not, even partially.
   - The positive-real case is classical in substance: Steinig 1971, reproved in Laurens,
     arXiv:2206.09050, Lemma 3.2, whose argument applies verbatim to the exponents
     −1, 1, 3, …, 2n−3.
   - Cite Korobov–Bugaevskaya, Math. Comp. 85 (2016) §3, for Theorem B's linear system.
   - What is new: the complex case under ∏(m_i+m_j) ≠ 0, the determinant, and Theorem C.
     Wording is in `THEOREM-A-PRIOR-ART.md`.

### MINOR changes to statements before freezing them

7. **Hypotheses to add**, all already used by the proofs:
   - Threshold Prop. 3(1): "S ≥ 3p+3".
   - Stability Prop. S3.2(ii): "a ≠ 0, g(0) ≠ 0, ∏(z_i+z_j) ≠ 0".
   - Ostrowski quote: γ is the largest root modulus of **both** polynomials.
   - Locality Thm 3.4: the systole is taken over all hyperbolic classes. Thm 3.5 and the
     LO.10 claim must define w.
   - `lem:chamber`, `lem:bound`: the p = 2 spread end is not attained.
   - Signatures Lemma 4 / `lem:sigdata`: "1 ≤ j ≤ 2L−3", the a_{l,k} sum is from k = 0,
     and "(g;m) ∈ Sig" in the converse.
   - Diophantine Prop. 2: exclude all-proportional families.
   - Divergence: the Borel claim needs n ≥ 1, and s_k > 0 needs its one-line proof.
8. **Constants and printed values:**
   - Theorem B: state c_n = (−1)^{n(n+1)/2} for every n. It is proved (Lemma S2.1) and
     re-proved independently twice. Do not state it as "computed for n ≤ 8".
   - Stability (2,2,2,2,3): δ_up ≤ 5.312e−05 and ratio ≤ 6.72, not 7.26/7.3. Regenerate
     `threshold_output.md` from `threshold.py`.
   - Divergence genus-10⁴ test: ℓ ≤ 8, not ℓ ≤ 5.
   - Diophantine base-point orders: 6,6,2,1,3,3 in the listed order.
   - thmA: "once the sum reaches 18" should say the first failure is at 18. Sums 19, 21–25, …
     (the last at 557) have no collision.
9. **Proof write-up:**
   - Lemma 3.2 should cite "DGGW Thm 4.8 at order t⁻¹" for the Weyl bound, not "Theorem 1",
     so that Proof C stays a cross-check with no cycle. P2 is SOUND, and the decay order 3 is
     already used.
   - Proposition S5's proof is a sketch; write out the ρ(A) < 1 and tan-majorant steps.
   - Diophantine Theorem 3: fix "distinct choices give distinct classes".
10. **Citations:**
    - The Holtz–Tyaglov source is arXiv:0912.4703 (SIAM Rev. 54 (2012)), not 1005.2843.
    - Uçar Thm 4.20(ii) and (4.35) should be cited beside (4.25)/(4.33).
    - Curvature Parts 1–2 should be presented as DGGW Thm 5.15 / Prop. 5.22 and Uçar
      Cor. 4.21(iv), not as new.
    - `thmC` needs `prop:rigidity`.

## Priority-target verdicts

| target | verdict |
|---|---|
| P1 Theorem N, all L and k | **TRUE.** (a) Prouhet step, (b) zeroing scaling, (c) entries ≥ 2 (the scaling-by-1 trap is handled by doubling), (d) hyperbolicity, (e) area < 2π(4^{L−1}−1) strictly, (f) Egyptian-fraction step (distinctness not needed; r₀/ρ ≥ 1 handled), (g) exactly L (resp. k) shared coefficients. All are re-proved in general. Built exactly for L ≤ 6 (block sums to L = 9) and k ≤ 7; a smaller (b) witness is 23 vs 24 cone points |
| P2 Lemma 3.2 / Theorem 3.1 | **SOUND.** Every convergence claim checks: the normalisation g = (1/2π)∫h e^{−iru}, identity, elliptic and hyperbolic terms, and the spectral side with decay order 3, including λ < 1/4 and λ = 0. **No circularity:** the Weyl count is taken from DGGW Thm 4.8 at t⁻¹, which is independent of the trace formula. Two self-contained alternatives are recorded |
| P3 stability constants and certificates | **Every printed δ_thm, δ_cert and ε_cert re-certifies exactly** in an independent implementation of Prop. S5, at the printed rounded-down values. Each printed δ_cert is the 4-s.f. maximum. 22,184 exact probes give 0 failures. Every δ_up is a valid failure bound; (2,2,2,2,3) is tighter than printed |
| P4 Threshold Prop. 3 and p ≤ 8 | **TRUE** for all p, with "S ≥ 3p+3" added to (1). The p ≤ 8 odd sums (gaps 1/840, 1/2310, 1/10296) and S*(p) are confirmed by brute force for p ≤ 232 |
| P5 isolation | **CONFIRMED, UNCONDITIONAL.** rank C_{27/2} = 0 by three routes: PARI 2.17.2 ellrank (no GRH, since the curve has rational 2-torsion), an independent exact 2-isogeny descent, and the analytic rank. Torsion Z/2×Z/6 with the 12 points; positive ones are exactly the permutations of (1,4,4) and (1,1,4). The pinned script agrees |
| P6 priority | **Narrow claim SURVIVES; broad claim MUST BE NARROWED** (`PRIORITY.md`) |
| P7 Theorem A prior art | **arXiv:1311.5493 does NOT give it.** Prior art is Steinig 1971 / Laurens Lemma 3.2 (`THEOREM-A-PRIOR-ART.md`) |
| P8 consistency | Heat input, sign of K and coefficient indexing **agree across all groups**, checked exactly for ℓ ≤ 8 and m ≤ 30 and against exact spherical spectra. The one indexing exception is item 4 above. **No genuine circular dependency**: locality Proof C → Thm 3.1 → Lemma 3.2 → Thm 1 is a cycle only for Proof C, and Thm 1's Proof A is independent |

## Results that should not go in the paper

| result | why |
|---|---|
| `conj:density` and the birthday heuristic | contradicted by data; heuristic miscounts |
| degeneracy-localization sentence | false |
| `rem:ncone` as worded | out of date and contains a false sentence |
| `rem:bugfix` | records an internal error only |

Results to include only as remarks or cited prior work:

- curvature Lemma 2 (classical);
- curvature Parts 1–2 (DGGW Thm 5.15, Prop. 5.22);
- curvature Part 4;
- the divergence results (Lemma 1, Theorems 2–3, Corollary 4, the Borel reading), as one
  remark;
- Diophantine Prop. 2.

## Counts (THEOREM-REGISTER.md, 102 rows)

| status | count |
|---|---|
| PROVED | 36 |
| PROVED GIVEN CITED INPUT | 51 |
| COMPUTATION | 10 |
| CONJECTURE | 1 (`conj:density`: do not include) |
| OPEN | 2 (integer sharpness for n ≥ 5; growth of f(A)) |
| CLAIM (FALSE) | 2 (localization sentence; `rem:ncone`) |

Audit verdicts by row:

| verdict | rows |
|---|---|
| FATAL | 0 |
| SERIOUS | 5 |
| MINOR | 37 |
| NONE | 60 |

The 5 SERIOUS rows are the four items above; the density item covers two rows.

## Process notes and instrument gaps

**Process.**

- Statements were extracted verbatim by script (`build_statements.py`, with anchor and
  no-proof asserts). Reviewers saw only their bundle and the fetched source texts until their
  blind verdicts were written.
- One commit (f12a657) swept in-progress reviewer files. Each group was then completed in its
  own commit.
- Fetched third-party PDFs and texts are now untracked (`.gitignore`). Two earlier commits
  contain them in history.

**Instrument gaps:**

- Standing, accepted: Steinig 1971, Drury–Marshall 1987, Donnelly 1976.
- Also logged:
  - the published FoCM version of 1311.5493 (closed access);
  - incomplete forward-citation data for DGGW and Dryden–Strohmaier, which bounds the P6
    "to our knowledge";
  - Beauville and Shioda (remark-level only);
  - Hejhal and Iwaniec (cited by DS for eq. (1); not needed).

See `fetches.md` and each group's `fetches.md`.
