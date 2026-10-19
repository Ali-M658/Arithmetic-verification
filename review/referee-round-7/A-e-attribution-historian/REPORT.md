<!-- Referee A-e: returned text saved verbatim; the reviewer could not write files -->

Writing to `REPORT.md` was refused, so the full report is below. The mathematics I checked is correct. The problems are four priority and duplication issues and a set of citation and presentation fixes. My recommendation is **major revision**, with moderate confidence (3/5).

# Referee report — "How much of a hyperbolic orbifold does heat hear?" (AGAG)

Referee role: rigour, citations and figures; priority and attribution.

I used only the manuscript (55 pp.), the supplement (16 pp.) and published literature fetched headlessly. I read the rendered page images of every figure page (pp. 1, 2, 22, 29, 31, 34, 35, 38, 42) before commenting on any figure or typography. I treated the marked placeholders (author contributions, AI statement, Zenodo DOIs, preprint identifiers) as known.

## Summary

The paper studies closed orientable hyperbolic 2-orbifolds. It asks how many short-time heat invariants c1, c2, … are needed to determine the signature (genus and cone orders), both against the whole class Sig and against subclasses. Its main results are:

- **Bounded cone orders (Thm 1.1 / 3.8).** If every cone order is at most M, then M+1 invariants suffice whatever the area, and this number is attained.
- **Growth (Thm 1.2 / 3.14, Prop. 3.15).** The worst-case count f(A) lies between about √A and A. Its power-law growth is equivalent to the size N(k) of Prouhet–Tarry–Escott (PTE) solutions.
- **Algebra (Thms A–C, 3.11).** These cover recovery from the first n invariants for spheres, a Hurwitz/Orlando form of the determinant, and a Descartes-type bound on genus change.
- **Triangle orbifolds (§5).** Three invariants always suffice. Two first fail on O(2,8,8) and O(3,3,12), and this pair is isolated by the rank-0 curve C_{27/2}.
- **Other material.** A variable-curvature section (§2.4), a stability theory (§6, App. C) and numerical illustrations (§4 and the supplement).

## Significance

What is genuinely good:

- The question is natural.
- The reduction of the growth question to the PTE problem (Prop. 3.15) is clean, and the paper says plainly that it is a reformulation, not a solution.
- The arguments are short and checkable.
- The paper separates what is proved from what is computed unusually carefully: Section S7 lists every statement that rests on computer search, and none is used in a proof.

Most of the heat-theoretic input comes from earlier work: Donnelly, Dryden–Gordon–Greenwald–Webb (DGGW), and above all Uçar's thesis. Uçar already has the triangular structure and the recovery of the cone orders from the whole sequence of invariants. The new content is therefore mainly combinatorial and algebraic: the finite counts, the sign-change and Descartes bounds, and the PTE equivalence. That makes accurate priority statements unusually important for this paper, and that is where most of my objections lie.

## Correctness: what I recomputed or verified

All of the following agree with the manuscript.

1. **Cone polynomials.**
   - From (4)–(5) I get p0, p1, p2 as in (8).
   - I get p3 = (m²−1)(m²+3)(3m⁴+2m²+19)/30240, which equals the K³ coefficient in Remark 2.12(b).
   - Lemma 2.8: the leading coefficients hold for l ≤ 4, and p_l(1) = 0.
   - The closed form in Lemma 2.6 checks numerically.
   - The area coefficients are α0…α4 = 1, −1/3, 1/15, −4/315, 1/315.
2. **Agreement with Uçar (Remark 2.9).** p_ν/m equals Uçar's coefficient of κ^ν (his (4.33) with (4.25)) for ν ≤ 3.
3. **Agreement with Schueth.**
   - b0, b1, b2 match Schueth [21, Thm 4.1, Rem. 4.2] exactly, including the −m⁵∆K/15120 term.
   - They are consistent with β_{1,2} = 2K, β_{2,3} = 12K² − 2∆K and β_{3,4} = 120K³ − 42K∆K + ∆²K.
   - They are consistent with Prop. 2.11(iii) for l = 1, 2.
4. **The minimal pair.**
   - c2 = 67/48 for both orbifolds.
   - d3, d4, d5 = 25/12, −1775/24, 153025/48.
   - The c3 values in Table S6 are correct.
5. **Shared-invariant counts (exact arithmetic).** Each pair shares exactly the stated number of invariants:

   | Pair | Shared |
   |---|---|
   | Example 3.6 | 2 |
   | Theorem C(3) | 3 |
   | Example 3.17(i) genus pair | 3 |
   | Example 3.17(ii) | 3 |
   | (0;2^10) vs (1;4^4) | 2 |
   | (1;3^9) vs (0;2^16) | 2 |
   | (0;2^28,4^8) vs (1;3^27) | 3 |
   | (2;) vs (0;2^8) | 1 |
   | (0;5,5,5) vs (0;2,2,2,10) | 2 |
   | Table S1, cone-count rows L = 4, 5 | 4 and 5 |
   | Table S1, Prouhet row L = 2 | 2 |

6. **Theorem 3.8(ii)/(iv).**
   - C and ν for M = 2, 3, 4 are as stated.
   - The least-genus areas 2π·{2, 6, 18, 190, 442, 3998, 8838, 77054} for M = 2…9 are correct.
   - The (iv) example: w = (1/45, −1/36, 1/180), C = 180, ν = (10, −4), s = 2.
7. **Theorem B.**
   - det M = (−1)^{n(n+1)/2} ∏(mi+mj)/∏mi holds exactly for (2,3,7), (2,8,8), (3,10,15,30) and (2,2,2,2,3), and the true e solves (12).
   - With Holtz–Tyaglov (1.37) and Thm 1.17, (11) holds with the stated sign.
8. **Stability constants.**
   - amp0…amp4 = 2, 14, 498, 4062, 56230/3.
   - The P3 row is P3 = −18c̃1 − 120c̃2 − 360c̃3.
   - ζ3 = 1, ζ4 = 79/3, ζ5 = 14048/15.
9. **Theorem 5.8.**
   - ψ maps E into C_{27/2}, and φ∘ψ is the identity.
   - The discriminant is 2^18·3^8·5^6.
   - The j-invariant matches the LMFDB curve 90.c3 (rank 0, torsion Z/2×Z/6), and the change of variables u = 2 matches c4 and c6.
   - #E(F7) = #E(F11) = 12, and (16,400) is a flex.
   - The twelve points lie on both E and C.
   - The local insolubility claims in Appendix E hold under a brute-force check: mod 5 on E, and 3-adically on E′.
10. **Triad enumerations.**
    - There are 83 triads with 10 ≤ S1 ≤ 18 (Table S3).
    - S*(p) and the first adjacent collisions for p ≤ 14 match Table S2.
    - The collision-free sums up to 600 are exactly the list in Computation S2.1.
    - The first non-adjacent collision is (5,15,15)/(7,7,21) at S = 35.
11. **Remark 3.2.** A search of all 4-multisets with orders at most 84 finds exactly 8 primitive witnesses, and they are Chen's (A.685)–(A.692).
12. **Section 4 numbers.**
    - On the flat cone, 4πt h_t ≈ 1.785 at r ≈ 0.546.
    - The closed-geodesic term of O(3,3,12) is ≈ 4.0e−13, 7.8e−13 and 2.7e−15 at t = 0.0293, 0.03 and 0.025.
    - (π/12)² ≈ 0.069 and ℓ²/4 ≈ 0.867.
    - In Table S4, δup/δthm runs from 5.4e2 to 1.9e8 and δup/δcert from 1.03 to 6.72, as stated on p. 41.
13. **Bolza benchmark.** The Strohmaier–Uski ancillary file has exactly 42 multiplicity-one eigenvalues below 998.
14. **Proofs read line by line.** Lemmas 2.4, 3.1, 3.3 and 3.7; Theorems A, 3.4 and 3.8(i), (iii); Corollaries 3.5 and 3.9; Lemma A.1; Theorem 3.14(b), (d); Proposition 3.15; Proposition 2.13(iii); Lemma 5.3. I found no gap in hypotheses or quantifiers.

**Could not verify** because of a paywall or bot block. The authors should re-check these against the originals:

- every statement attributed to Borwein–Ingalls [4]: p. 6, §3, Props 2–3, p. 7, the §6 problem and its quotation, pp. 9, 10 and 25;
- Bremner–Guy–Nowakowski [34, p. 117];
- Borwein–Lisoněk–Percival [50, pp. 2064, 2069];
- Chang–DeTurck [26], Korobov–Bugaevskaya [30], Cheeger [8], Philippe [32, 33] and Steinig [27];
- Ostrowski [62].

## FATAL

None.

## MAJOR

**M1. The novelty claim for Theorem A over Steinig is not established (pp. 6–7, 18).**

- The text says Theorem A is "of the type of" Steinig's theorem and "adds the replacement of P_{2n−1} by R … for complex multisets with multiplicity".
- Laurens [28, before Lemma 3.2], which I checked, paraphrases Steinig as proving that "any n power sums of n distinct positive real numbers has at most one solution". Steinig's title refers to Laguerre's rule of signs, which handles real exponents. Laurens's Cor. 3.3 shows the proof tolerates repeated values.
- If Steinig's exponents are arbitrary reals, the exponent set {−1, 1, 3, …, 2n−3} is covered. Then the orbifold application in Theorem 1.3(i) already follows from Steinig, and only the complex/multiplicity version and Theorem B would be new.

**What resolves it:**

- State Steinig's theorem exactly: the class of exponents and the distinctness assumption.
- Narrow the novelty sentences on pp. 5, 7 and 18 to match.
- Credit Laurens [28, Lemma 3.2, Cor. 3.3] where the relevant results are proved, not only in §1.2. His argument (sign changes of a step function, odd power sums, multisets of different sizes) is very close to Lemma 3.7, Theorem 3.4 and Theorem 3.8(iii).

**M2. The structure in Proposition 2.11(i) is anticipated by Fursaev and not credited there (pp. 6, 11, 13–15).**

- Fursaev [13, (3.26)–(3.27)] writes the cone coefficient for a rotationally symmetric cone of any angle as a_{α,n} = Σ_{k=1}^{n} α c_k(α) G_{nk}. The c_k are polynomials of degree 2k in α⁻¹, and the G_{nk} are curvature invariants at the tip. This is exactly the shape b_l(p) = Σ_i β_{l,i} Π_i(m) of Prop. 2.11(i).
- The manuscript cites [13] only in §1.2 and after Prop. 2.7. There it says the cone coefficients "were computed … as polynomials in the inverse angle". In fact Fursaev computes only a_{α,1} and a_{α,2} explicitly ((2.7)–(2.8)) and gives the general structure. Dowker [14] re-derives a single coefficient.
- Meanwhile §1.1 claims "the variable-curvature results … are in this paper only".

**What resolves it:**

- Credit Fursaev [13, (3.26)] at Prop. 2.11(i).
- State what §2.4 adds: the non-symmetric orbifold case, the radial reduction for m ≥ l−1, the top coefficient β_{l,l+1}, and the linear part.
- Correct the "computed" wording on pp. 6 and 11.

**M3. Remark 4.3 (p. 32) reproduces a published formula without attribution.** The kernel k_m(u) and the Parseval step from the r-integral to the u-integral are Garbin–Jorgenson [37, Thm 2.5 and Rem. 2.6]. I checked that their elliptic heat trace is identical to ∫g_t k_m du. [37] is cited only for the normalisation. Cite [37, Thm 2.5, Rem. 2.6] in Remark 4.3.

**M4. Overlap with two unseen companion manuscripts (pp. 6, 7–8, 37; supplement S4, S7).**

- Companion [3] restates the results of Sections 2–3 it uses and "reproves them in its Appendix A by the arguments of this paper".
- The two papers share the computed spectra, the description of the method and the code deposit.
- The enumeration to sum 4800 "is the same computation as" in companion [35], which extends it to 6000.

Duplicated proofs and possible double crediting cannot be assessed without [3] and [35]. **What resolves it:** supply both companions to the editor, remove re-proofs of this paper's results from [3] (cite them instead), and make sure each result is claimed in one paper only.

## MINOR

- **m1 (p. 7).** For the weighted projective planes, the version using the function spectrum plus the Euler characteristic is Theorem 6.2 in §6.2 of Abreu et al. (arXiv numbering; please check against the journal). Theorem 1 there also assumes a Kähler metric and isolated singularities, which the citation omits.
- **m2 (p. 6).** Proctor–Stanhope [17] prove only that isospectral families with a lower curvature bound contain finitely many diffeomorphism types. They do not "hear" the diffeomorphism type, as the text implies.
- **m3 (pp. 6, 11).** The paraphrase of Schueth [22, p. 2] overstates her. She says half powers and logarithms *can* occur when f″(0) ≠ 0; she does not say "only when". Her remark is also limited to rotational symmetry and to the b1, b2 (and Uçar's constant-curvature) formulas.
- **m4 (p. 12).** DGGW's class of orbifolds with χ ≥ 0 includes bad teardrops and footballs, and their result holds for every metric. "Those of curvature 0 and +1" misdescribes it.
- **m5 (pp. 6–7).** The statement that the trace formula hears the number of cone points of each order is credited to [6] only. Dryden–Strohmaier [5, Thm 1.1] states exactly this. Their own "proved independently" remark points to an earlier Doyle–Rossetti preprint (math.DG/0605765), not to [6].
- **m6 (p. 7).** For hearing a Euclidean triangle, Durso's MIT thesis (1988) has priority; Grieser–Maronna themselves credit her.
- **m7 (p. 18).** Cite Orlando's original 1911 paper for Orlando's formula, as well as [42].
- **m8 (p. 28 and Table S1).**
  - The size-12 ideal symmetric solution "[49, (5)]" was found by Kuosa, Meyrignac and Chen in 1999, as [49] itself says.
  - The size-10 piece is from Borwein–Lisoněk–Percival (it appears as (4) in [49]).
  - The 7-sets used for L = 4 have no source at all.
  - Give a source and discoverer for every piece in Table S1. Chen's labels (A.178), (A.266) (Gloden), (A.313)–(A.316) and Letac 1942 cover most of them.
- **m9 (p. 22).** Lemma 3.7 (a measure with L vanishing moments has at least L sign changes) is classical, e.g. Pólya–Szegő, Part V. Cite it, and soften the word "new" for this technique on p. 7.
- **m10 (p. 37).** "The adjacent strata touch without overlapping only for p = 2 and p = 4" contradicts the definition of "overlap" on p. 35. By that definition they do overlap there: S*(2) = 18, and Theorem 5.5 says the strata "meet".
- **m11 (p. 26).** "No bound o(k²) is known" needs "to our knowledge". Also distinguish N(k) from the variant W(k) with unequal (k+1)-th power sums, as Croot–Mao–Yip [45, §1] does.
- **m12 (p. 15).** The expansion d(x,Φx)² = C²r²W_u(r) is Schueth's Lemma 3.4 / (13) (and Corollary 2.4). Her (15)–(16) are only the substitution step.
- **m13 (p. 34, Fig. 5(b)).** Some circles sit about 0.5–1 decade above ten times the shaded maximal error budget at their time value (e.g. near t ≈ 0.05). This conflicts with their stated definition. Explain it: sampling granularity, or a budget that depends on t.
- **m14 (p. 42, Fig. 8).** The axis title ‖m̃ − m‖∞ does not match the distance used in the text: the minimum over permutations defined on p. 39.

## Presentation

- **P1. Numbering collision.**
  - Theorems A, B, C in §3 collide with Appendices A, B, C. For example "Theorem C(3)" (integer sharpness) versus "Theorem C.3" (stability constants), "Theorem B" versus "Lemma B.3", and "Theorem A" versus "Lemma A.1".
  - Renumber Theorems A–C as 3.x.
- **P2. Notation overloads.**
  - C is an integer (Thm 3.8), a class (Def. 2.2) and 2 sin(ϑ/2) (§2.4).
  - a is a node, a_l is a leading coefficient, a_{l,k} are coefficients, a_k are the coefficients of χ_m, and a is a distinct order in §6.
  - p is a prime, a cone point and a stratum index.
  - The sentence on p. 23 ("the letter a without subscript is a node…") shows the problem.
- **P3. Caption length.**
  - The first sentences of the Fig. 1 and Fig. 2 captions are long, with several clauses and parentheticals.
  - Shorten each caption to two short sentences; the text already carries the detail.
  - Figure contents comply with the rule: only axis titles, tick labels and panel letters. The colour-bar title in Fig. 1 counts as an axis title.
- **P4. Colour key.** Which colour is which orbifold in Fig. 2(a) and in the split discs of Figs 3 and 7 is defined only through Fig. 6 (teal for (2,8,8), orange for (3,3,12)). State it in the text at first use (p. 21).
- **P5. Wording.**
  - p. 35, proof of Lemma 5.3: "…is gap_p(S) ≤ 0" should read "…is equivalent to gap_p(S) ≤ 0".
  - Supplement p. 16: "the bound 6" should read "the bound (6)".
- **P6. References.**
  - [14] Dowker, CQG 11: the pages are L137–L140.
  - [9]: the third author is J. S. Dowker; make the initials consistent with [10] and [14].
  - [6] and [52] are unpublished preprints; say so.
- **P7. Cross-references: no action needed.** Every supplement item the paper cites exists: Sections S1–S7, Tables S1–S6, Proposition S3.1, Computation S2.1, and S7(ii)/(iii). All internal theorem references resolve, and all 63 references are cited.

## Recommendation

**Major revision.** Confidence: moderate (3/5).

The mathematics I checked is correct, and the computations are reproducible and honestly labelled. The revision is needed for the priority claims (M1, M2), the unattributed formula (M3) and the overlap with the companion manuscripts (M4).

## What resolves each issue

| Issue | What resolves it |
|---|---|
| M1 | Quote Steinig's theorem exactly; narrow the novelty of Theorem A and Theorem 1.3(i); credit Laurens at Lemma 3.7, Theorem 3.4 and Theorem 3.8(iii). |
| M2 | Credit Fursaev (3.26)–(3.27) at Prop. 2.11(i); correct "computed" to "structure, with the first two computed"; restate what §2.4 adds. |
| M3 | Cite Garbin–Jorgenson Thm 2.5 and Rem. 2.6 in Remark 4.3. |
| M4 | Give [3] and [35] to the editor; remove duplicated proofs; claim each result in one paper only. |
| m1–m14 | Correct the citation, hypothesis or wording as indicated in each item. |
| P1–P6 | Renumber the lettered theorems, clean up notation, shorten the two captions, give the colour key in the text, fix the references. |

My verification scripts are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/A-e-attribution-historian/scratch/code/`, and the downloaded sources are in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/A-e-attribution-historian/scratch/src/`.
