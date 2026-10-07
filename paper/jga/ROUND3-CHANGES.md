# ROUND3-CHANGES: dispositions of referee round 3 (review/referee-round-3/VERDICT.md)

Decision of the round: the manuscript is **split** into two papers, each self-contained.

- **Paper A** (this directory, `manuscript.tex`, target AGAG): what heat invariants hear about the
  signature, and at what cost.
- **Paper B** (`paper/eigen/manuscript.tex`): finitely many approximately known eigenvalues determine
  the signature, effectively.

Each paper cites the other only in the text, as a companion manuscript in preparation; no proof in
either depends on the other. Build: 39 pp. (was 48) plus a 14-pp. supplement (was 15). Paper B:
23 pp. Page counts are recorded in `BUILD.md` and `paper/WAVE3-SUMMARY.md`.

## What moved

| from Paper A (wave 2) | to |
|---|---|
| Section 4 (Theorem E, Lemmas 4.1-4.12, Tables 1-3, Propositions 4.4, 4.15, Remark 4.14) | Paper B, rewritten (Sections 2-8) |
| Remark 5.5 (diameter-free locality constant) | removed; it rests on the diameter bound of Paper B |
| Problem 5 (is a systole bound needed?) | Paper B, Problem 1 |
| Supplement Section S7 (pinching, Proposition S7.1) | Paper B, Proposition 8.5 |
| `jorgensen1976`, `jorgensenwiki` in `references.bib` | removed; Paper B proves the case of Jorgensen's inequality it needs |

The significance sentences of Section 1.1 that pointed forward to Section 4 are replaced by one
sentence naming the companion manuscript (Paper B) in the text. All eight figures F1-F8 stay.

## MAJOR items

| ID | disposition | where |
|---|---|---|
| I1 (four papers in one) | **Done**: split as above. | whole paper |
| I2 (what effectivity adds; a-posteriori version) | **Paper B**: compactness paragraph (Mumford, Bers) in its introduction; Theorem 7.1, the a-posteriori certificate; Table 3. | Paper B |
| I5 (steps "checked numerically"; Wikipedia) | **Paper B**: (H1)-(H3), the commutator-trace identity, the Rayleigh identity and the Lambert angle are proved; the hyperbolic case of Jorgensen's inequality is proved with his argument and his paper cited from its Crossref record (the text is an instrument gap, `paper/eigen/SOURCES.md`). Paper A no longer contains any of these steps. | Paper B |
| I6 (bounded orders) | **Done**: new Theorem 3.7 (Bounded cone orders): (i) among orbifolds with orders <= M the first M heat invariants determine the signature; (ii) M is optimal, with explicit pairs; (iii) against all of Sig, M + ceil(log(2 floor(A/pi) + 8)/2) suffice. Corollary 3.8: the growth needs large orders. Theorem 1.1(iii), the abstract, the interpretation paragraph of Section 1.1 and the remark after Theorem 3.13 say that the area-driven growth is a large-order phenomenon. Proof and exact checks in `theory/msep/`; two blind checks (`theory/msep/BLIND-CHECK.md`), the second of which supplied the sharper constant in (iii). | Sections 1, 3 |
| I8 (floating-point filter) | **Done**: Remark 3.17 states the sound modular test (a rational partner triple forces q_V to split modulo every prime at which it is p-integral) and its outcome (4,325,115,770 multisets, 15 survivors for all twelve primes 223..277, all 15 cubics irreducible); the search is labelled computer-assisted there and in Problem 3. Implemented in `theory/pte/search_T3_modular.{c,py}` with a control (all 1,798,940 triples accepted) and run to 220 (`theory/pte/data/T3_modular.json`); it reproduces the referee's count. Supplement S1 and S8(ii) describe the test; the floating-point filter is described as superseded. Appendix D says the search rejects only by this test. | Remark 3.17, Problem 3, App. D, Suppl. S1, S8 |

## Items adjusted to MINOR in the verdict

| ID | disposition |
|---|---|
| I3 (growth relocated to PTE) | One sentence after Proposition 3.14: the extra structure of a configuration changes its least size against N(k) by at most a constant factor, so it cannot decide the exponent. |
| I4 (search-only claims) | Appendix D now lists the statements that rest on computer search alone and are used in no proof. |
| I7 (T(L) constructions) | Lemma 3.15 (combining two pieces with a vanishing reciprocal sum) and the paragraph after it give the construction for every L = 4..7, with sources: odd ideal symmetric 7-sets (Borwein-Ingalls pp. 9, 25; Gloden's family, BLP p. 2064), Letac's 9-sets (B-I p. 9), Chen A.1.33 (L = 6 only), the size-12 solution of CMSV (5) (L = 7), and for the genus pairs shifts of even ideal symmetric solutions with Chen A.1.17, A.1.26, A.1.33. The A.1.33 attribution is fixed. What was searched for T(4) <= 12 is stated (size 12 not searched; the size-10 family of two odd symmetric 5-sets has no member with entries <= 200). Supplement S1 lists every piece. |
| I9 (PTE literature) | Wright 1935 cited, with his bounds as reported by Borwein-Ingalls p. 7 (the original is not read); Hua's text (Ch. 18), Dorwart-Brown and Borwein's book (Ch. 11) added as classical sources (records fetched by `tools/build_bib.py`); the B-I remark that no progress on N(k) = o(k^2) "has been made for many years" is quoted. A heuristic for T(L) is given after the T(L) table, labelled as weak. |

## MINOR items

| ID | disposition |
|---|---|
| n1, n10-n13, n21 | Section 4 material: handled in Paper B (Table 3 caption covers seven members for N_apr; the data hypothesis "first N, in order, with multiplicity" is stated after Theorem 6.2; the unused divisibility is dropped; the diameter's role is stated after Theorem 4.4; the growth statements are labelled as observations; "competitors" is now the set S including the orbifold). |
| n2 | The duplicated Section-4 sentence is gone with Section 4. |
| n3 | Phi_j of Proposition 4.1 renamed F_j; the tanh series of Theorem B renamed calligraphic T (Theta would collide with Theta(A)); the size T in the proofs of Theorems 3.4 and 3.10 renamed kappa; sigma_0 and the diameter D left with Section 4. |
| n4 | Remark 2.9 points to supplement S8(iii) for the exact comparison with Ucar to l = 40. |
| n5 | Theorem 1.2(ii), (iii): "among hyperbolic triangle orbifolds" added. |
| n6 | Schueth 2025 is cited only for the t^(1/2) coefficient of curved cones with rotational symmetry; the K(p) and K^2, Delta K terms are cited to DGGW and Schueth 2019. |
| n7 | Dryden-Strohmaier cited as Thm 1.1 and Prop. 3.3 together. |
| n8 | The Chang-DeTurck count is stated with its lower angle bound. |
| n9 | The DGGW erratum is quoted ("there is an implicit assumption that Iso^max(N) is nontrivial" in Theorem 5.1, the only theorem it changes), from the fetched text (`review/literature-pass/_fetched/txt/dggw2017erratum_mmj.txt`); nothing here uses that theorem. |
| n14 | Figure F4's markers are decoded in the text that cites it (dots, split disc, diamonds = genus, equal-count and cone-count pairs, squares = pairs from Prouhet's solutions, the two step curves). |
| n15 | F3 (printed Fig. 2) re-rendered: tick labels one unit apart are aligned away from each other (`figures/src/F3.py`). |
| n16 | F2: the text says that 2m triangles meet at a vertex of order m (no in-figure labels, by the style rules). |
| n17 (title) | Kept. "Heat" in the title stands for heat invariants, which the abstract's first sentence defines; the question of the whole heat trace is answered in Section 1.1 (different signatures have different spectra). |
| n18 | "We know of no result on whether the whole spectrum hears orientability" (no source was found). |
| n19 | Years: the bibliography uses the printed-volume year throughout (rule `year_of` in `tools/build_bib.py`); the Wright citation is no longer used in a proof (Theorem 3.13(c) uses N(2L-3) <= 2L^2 from B-I Prop. 3). |
| n20 | d-m1: Wright cited, bound via B-I; d-m2: the Chen data are said to be recomputed, with Chen's attribution to a 2017 search; d-m3 = n14; d-m4: Problem 4 is identified as the balanced case T(n-1) = 2n, Chen type (-1,1,3,...,2n-5); d-m5: the n = 5 bound 120 is called weak evidence; d-m6: "witness", "primitive" and the pencil defined in Remark 3.2; d-m7: sharpness of the Descartes bound discussed at the end of Remark 3.17; d-m8: "(the constants are not optimised)" in Theorem 1.1(ii); d-m9: Proposition 3.14 says "for large L"; d-m10: "ideal" defined before Lemma 3.15. |

## Global style

- Abstract rewritten (about 180 words, AGAG asks 150-250).
- Every caption F1-F8 is at most two short sentences (`figures/captions.tex`); the decoding moved into
  the sentence that cites each figure.

## Not done, and why

- **Length**: 39 pages against the target of 34-37. Removing Section 4 saved 12 pages; Theorem 3.7, the
  I7 constructions and the sound I8 test added back about 2.5. Further cuts would remove proofs or
  attributions that the referees asked for.
