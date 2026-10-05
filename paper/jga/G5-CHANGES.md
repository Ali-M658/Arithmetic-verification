# G5 changes: every required change of `review/audit/G5-VERDICT.md`, ticked off

`[x]` = done in `paper/jga/manuscript.tex`; the location is given by section and label.
Nothing here changes a proved statement's mathematics; the changes are to sentences, hypotheses,
citations and printed values, as G5 specifies.

## SERIOUS

- [x] **1. Degeneracy localization.** The sentence claiming that interval separation localizes
  every degeneracy to adjacent least-order strata is not used. Section 5.3 (after
  `prop:tangency`) states the opposite fact with the counts: collisions also join non-adjacent
  strata, the first at S = 35, (5,15,15) and (7,7,21), and 2793 of the 3067 pairs with S <= 600
  join strata whose least orders differ by at least 2. The enumeration is described as
  exhaustive (Section 5.3, Section 8.4, Appendix C), and N(S) is defined as a count of
  unordered pairs (Section 8, first paragraph).
- [x] **2. Density section.** `conj:density`, the birthday heuristic, the abstract's
  "c ~ 0.0085-0.0093", "stabilizes" and "quadratic-order" do not appear. Section 8 consists of:
  the reformulation on C_Lambda and the pencil (`prop:reformulation`, `prop:pencil`), the dual
  family (`prop:dual`), the isolation theorem (`thm:isolation`, Section 5.4), Theorem 4 as
  `thm:iso` ((c_iso + o(1)) X log X), Theorem 5 as `thm:loglog` (X (log X)^2, proof in
  Appendix A), Theorem 3 as `thm:largefibres` (classes of every size), and the revised
  conjecture N(X) = X^{1+o(1)} (`conj:growth`). The empirical log-exponent is stated as a
  measured value on a finite range, not a prediction. The density table has no c S^2 column.
- [x] **3. `rem:ncone`.** Not used. Its content is replaced by Theorems A and C (`thmA`,
  `thmC`), Corollary `cor:Kinf` (K_iso = infinity for n >= 4), and the n = 4 witness in
  `thmC`(3). The conditional labels are gone: `thm:locality` is a theorem, not a forward
  reference; `cor:Kinf` is unconditional; `rem:sigphysics` restates rem:nconerestated (a)-(c)
  without conditions.
- [x] **4. Coefficient indexing in the fibre claim.** Every statement about fibres says
  "share c_1 and c_2" (equivalently R and S_1): `thm:largefibres`, the caption of
  `tab:fibres`. The Ucar-style "a_0 and a_1" does not occur.

## Priority and prior art

- [x] **5. P6.** Section 1.1, second paragraph, uses the `PRIORITY.md` wording: DGGW Thms
  5.14-5.15 (one coefficient, chi >= 0) and Prop. 5.22, Abreu-Dryden-Freitas-Godinho Thm 1,
  Dryden-Strohmaier Thm 1.1, Ucar Thm 3.40 and Cors 4.21(iv), 4.23, DGGW Rem. 5.16 quoted, the
  narrow claim "first exact finite-coefficient determinacy threshold, with an explicit minimal
  degeneracy, for a family of hyperbolic cone orbifolds" with "to our knowledge", tied to
  DGGW Rem. 5.16, the observation c = S_1 + R - 2, and the narrowed count claim "the first
  explicit finite number of heat coefficients, floor(Area/pi)+4, that determines the genus and
  the cone-order multiset uniformly over all closed orientable hyperbolic 2-orbifolds".
  "None of it counts coefficients" does not appear. Dryden-Strohmaier (2009) is cited.
- [x] **6. P7.** Section 1.1, third paragraph, uses the `THEOREM-A-PRIOR-ART.md` wording:
  Steinig 1971 through Laurens Lemma 3.2 (now published, Calc. Var. PDE 62 (2023)), MSW
  Prop. 24, Korobov-Bugaevskaya Section 3 Thm 3.1 for Theorem B's system; what is new is the
  complex case under prod(m_i+m_j) != 0, the determinant, and Theorem C. Mueller et al. is
  cited only with the sentence that its criteria do not apply.

## MINOR: hypotheses added

- [x] Threshold Prop. 3(1): "For S >= 3p+3" in `prop:tangency`(1).
- [x] Stability Prop. S3.2(ii): "a != 0, g(0) != 0, and prod(z_i+z_j) != 0 for the roots of
  q_0" in `prop:sharpexp`(ii), with the continuity argument in the proof.
- [x] Ostrowski: gamma is "the largest modulus of a root of either polynomial" (Section 6.3,
  before `lem:rouche`).
- [x] Locality Thm 3.4: the systole is defined over all hyperbolic conjugacy classes, which may
  pass through cone points (Section 4.3, before `thm:IEH`, and in `thm:quantlocality`); (c)
  says it also needs the area, the signature and l. Thm 3.5: w_O is defined before
  `thm:sharp`. LO.10: `cor:prefactor` has |w_1(l) - w_2(l)|.
- [x] `lem:chamber`, `lem:bound`: the maximum is attained on the stratum only when the spread
  triad is hyperbolic, not for p = 2 or (S,p) = (9,3); the reciprocal sums of a stratum are a
  finite set contained in [R^-, R^+] ("fill" removed).
- [x] Signatures Lemma 4 / `lem:sigdata`: odd j with 1 <= j <= 2L-3; the a_{l,k} sum runs from
  k = 0 (`lem:triangular`: "sum_{k=0}^{l+1} a_{l,k} = p_l(1) = 0"); the converse assumes
  (g;m), (g';m') in Sig.
- [x] Diophantine Prop. 2: all-proportional families excluded (`rem:nolinear`).
- [x] Divergence: the Borel claim is stated "with at least one cone point"; s_k > 0 has its
  one-line proof (`rem:divergence`).

## MINOR: constants and printed values

- [x] Theorem B: varsigma_n = (-1)^{n(n+1)/2} for every n, proved (`thmB`); not "computed for
  n <= 8". (CONVENTIONS.md names this constant varsigma_n, since c_j is a heat coefficient.)
- [x] Stability (2,2,2,2,3): delta_up = 5.312e-05 and ratio 6.72 in `tab:thresholds` (no record of the old value in the paper), generated
  from `review/audit/stability/check_dup.txt`; the text says "within 6.72 for the case n = 5".
  (`theory/stability/threshold_output.md` itself is outside paper/jga/ and is not regenerated
  here; the table is generated from the JSON and the audit file.)
- [x] Divergence genus-10^4 test: "the smooth part dominates for l <= 8" (`rem:divergence`).
- [x] Diophantine base-point orders: 6, 6, 2, 1, 3, 3 in the listed order (`prop:pencil`).
- [x] thmA: "the first failure occurs at cone-order sum 18", with the collision-free sums
  19, 21-25, 27-30, 33, ..., the largest 557 (`thm:threshold`).

## MINOR: proof write-up

- [x] Lemma 3.2 cites "the leading term of DGGW Thm 4.8 at order t^{-1}" for the Weyl bound
  (`lem:admissible`); Proof C is labelled a cross-check (`rem:proofC`).
- [x] Proposition S5's proof is written out: why v = (I-A)^{-1} 1 > 0 gives spr(A) < 1 (diagonal
  similarity and row sums), why M(I~) is then invertible, why the tan majorant bounds the tanh
  remainder, the radius set and the integer hypothesis (`prop:S5`).
- [x] Diophantine Theorem 3: "distinct choices give distinct classes" replaced by the argument
  that the lcm L is unbounded over the choices (`thm:largefibres`).

## MINOR: citations

- [x] Holtz-Tyaglov cited as SIAM Rev. 54 (2012) 421-509, DOI 10.1137/090781127 (arXiv:0912.4703),
  for Orlando's formula (Thm 1.17) and the Hurwitz determinants ((1.37)).
- [x] Ucar Thm 4.20(ii) and (4.35) cited beside (4.25)/(4.33)-(4.34) (`prop:heatinput`).
- [x] Curvature Parts 1-2 presented as DGGW Thm 5.15 / Prop. 5.22 and Ucar Cor. 4.21(iv), "none
  of it is new" (`rem:curvature`).
- [x] `thmC` (now `thm:three`) cites `prop:rigidity`.

## Results kept out, and remark-only results

- [x] Not included: conj:density, the birthday heuristic, the degeneracy-localization sentence,
  rem:ncone as worded, rem:bugfix, any c S^2 density claim.
- [x] Remark only: the divergence results (one remark, `rem:divergence`); curvature Parts 1-2
  (cited, `rem:curvature`); Diophantine Prop. 2 (`rem:nolinear`). Curvature Lemma 2 and Part 4
  are omitted.

## DEFECTS rows owned by S11 (`review/DEFECTS.md`)

| row | resolution |
|---|---|
| FAT-01 | Both K_iso and K_mult are defined (`def:K`); K_iso = infinity off the triangle orbifolds (`cor:Kinf`); K_mult <= n (`thmA`); rem:ncone not used. |
| FAT-02 | The abstract has no density constant; Section 8.4 states the falling ratio and the revised conjecture. |
| MAJ-01 | N(S) counts unordered pairs; classes counted separately; both conventions in `tab:density`. |
| MAJ-03 | Both notions are used, each named with its comparison class; the paper's triangle-orbifold statements are for K_iso, equal to K_mult by `prop:rigidity`. The choice is reported to the author (OUTSTANDING.md). |
| MAJ-06 | Kept with "to our knowledge" and tied to DGGW Rem. 5.16, per `PRIORITY.md` (which post-dates the DEFECTS row and is authoritative), with the Doyle-Rossetti quotation. |
| MAJ-07 | Dryden-Strohmaier 2009 Thm 1.1, Doyle-Rossetti Thm 1 and Ucar credited in order (Section 1.1). |
| MAJ-08 | Doyle-Rossetti cited and quoted verbatim from the fetched arXiv v2 (Section 3, p. 8). |
| MAJ-09 | Linowitz-Voight Thm A cited (Section 1.1, `rem:blind`). |
| MAJ-10 | Berndt-Yeap cited for the trigonometric sums (Section 2.3). |
| MAJ-11 | Shams-Stanhope-Webb and Rossetti-Schueth-Weilandt reconciled with Dryden-Strohmaier (Section 1.1, fourth paragraph). |
| MAJ-12 | Bari-Hunsicker described as in `review/literature/bari-hunsicker.md`: full spectrum determines lens spaces; the entire heat expansion does not. |
| MIN-02 | The cone term is cited to Ucar's equations (4.25), (4.33)-(4.34) and Thm 4.20, displayed (`eq:ucarlune`, `eq:pl`). |
| MIN-03 | The birthday heuristic is not used. |
| MIN-04 | Schinzel's method credited for `thm:largefibres`; Guy's D16 text is unretrieved, so Guy is not cited (OUTSTANDING.md). |
| MIN-05 | The n = 4 witness is `thmC`(3). |
| COP-01 | No corrupted dashes: the source has no " ,  " pattern (checked by grep). |
| COP-07 | No overfull boxes (BUILD.md). |
| COP-10 | Two theorem environments remain, numbered differently: Theorems A, B, C (lettered) and Theorem x.y. |
| COP-11 | Labels are new; unreferenced labels on numbered results are normal and harmless. |
| COP-16 | An independent review of the compiled PDF was run (SELF-REVIEW.md). |
