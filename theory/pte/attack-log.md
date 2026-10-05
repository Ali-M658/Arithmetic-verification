# Adversarial referee log: `theory/pte/proof.md` and `data/witnesses.json`

Target versions: `proof.md` and `data/witnesses.json` as on disk at 6 Oct 00:45 and 00:42. In this
version the L=4 genus witness has T=16; an earlier version had T=18.

All code is independent: own Uçar cone coefficients `b_l`, own configuration checks, and an own
exact cubic root finder (`attack/mylib.py`). Nothing is imported from `pte_common.py`,
`witnesses.py` or `sig_common.py`. Arithmetic is exact (int, Fraction, sympy).

Exit codes:

- 0: every claim tested survives.
- 2: a finding (BROKEN or PARTIAL) is reported in the transcript.
- 1: an unexpected failure.

| # | claim | verdict | evidence |
|---|---|---|---|
| 1 | every witness in `witnesses.json`: hyperbolic, equal area, area value, shares **exactly** L, T, ι, cone counts, genera, distinct signatures, primitive Z is an exact L-configuration; §0 and §5 table values; A_L at most the "new" thresholds | **SURVIVES** (18/18) | `a01_witnesses.py`/`.txt` (own b_l also matches Schueth a0, a1, a2) |
| 2 | Theorem 2.1, \|ι\| ≤ T−2L | **SURVIVES** for even T | `a02_descartes.py`/`.txt`: 2,024 integer collisions (orders ≤16) and ~33k random exact rational configurations; none violates the bound |
| 2′ | Lemma 1.2(4) "T is even, T ≥ 2L+2" for every configuration of Def. 1.1; Def. 1.3 "2L+2 ≤ τ_L" | **BROKEN as stated** | `a02`: Z={−24,−18,−8,5,45} is a 2-configuration of size 5 < 6; odd-size configurations exist for T=5,7,9,11 |
| 2″ | proof of Lemma 1.2(5) | PARTIAL (proof gap; the statement is true) | see below |
| 3 | Prop. 2.3(a)–(c) | **SURVIVES** | `a03_symmetric_pencil.py`/`.txt`: 480 random real-rooted Q_A (exact Sturm), 1,816 integer sets of size 3, 5, 7, 9, and 1,590 configurations A⊎λB; all balanced |
| 4 | Theorem 3.1: weight argument, balance, and the instance {3,10,15,30}~{4,5,21,28} | **SURVIVES** | `a03`: symbolic check of ∂s_j/∂e_{k0} for m=4..9; 197 random real pencils (m=4..7); own m=4 integer search; the instance holds exactly |
| 4′ | §7: "T^cone_3=8 would be a pencil point" (the converse of Thm 3.1) | PARTIAL (unproved; holds in range) | `a04_pencil_converse.py`/`.txt`: all 7 balanced size-8 3-configurations with entries ≤80 are pencils |
| 5 | Props. 3.2, 3.3, Thm. 3.4 (τ_L ≤ 6N_odd, T_L ≤ 4N(2L−3), T^cone_L ≤ 6N(2L−3)) | **SURVIVES** | `a05_constructions.py`/`.txt`: built for L=2..7 from raw inputs over every shift window, realised and checked with own b_l (areas < 2πT and < 2π(3n−2)); all 5,560 edge-case pairs X≠Y (L=2,3) |
| 6 | Lemma 1.5 (pigeonhole; N_odd(L)=L for 3≤L≤6); Prop. 2.2 | **SURVIVES** | `a06_lemma15_prop22.py`/`.txt`: pigeonhole inequality exact for L=2..7; exhaustive: no size-(L−1) collision (L=3: ≤400, L=4: ≤90, L=5: ≤32); [Z]=_{2L−2}[−Z] holds for all 18 witnesses |
| 7 | Thms. 4.1, 4.2(a)–(c): inequalities and quantifiers | **SURVIVES** | `a07_growth.py`/`.txt`; the proofs of (b) and (c), as now written, handle small A and small k |
| 7′ | the remark after Thm 4.1: "strictly larger from 28 (the two agree on [4,28))" | **BROKEN** (false remark) | `a07`: at x=A/2π ∈ [13,15) the new bound is 4 and the old is 3 |
| 7″ | "best known bound N(k) ≤ ½k(k+1)+1" (§0 item 2, §4) | PARTIAL (wording) | B-I p.7 quotes Wright/Melzak: ½(k²−3) for k odd, ½(k²−4) for k even (`a10`) |
| 8 | Thm 4.3: thresholds 8πN(2L−3) and 2π(3N(2L−3)−2), f_g, f_n ≤ f, the "⇒" direction | **SURVIVES** | `a07` and `a05`: the constructions realise the thresholds; the witnesses lie below them |
| 9 | §6 T_3: the cubic, the repeated-root branch, coverage, "exhaustive exact search, v5 ≤ 220" | **PARTIAL**: the algebra is right; the exactness claim is **BROKEN** | `a09_T3.py`/`.txt`: own elimination gives the same cubic. Own exact search to v5 ≤ 45 (1,828,418 V) finds no split cubic and matches the C counters exactly. But the long-double filter of `search_T3.c` rejects 33 genuine rational U in the searched regime (S ≤ 1100). The control never tests K'>1. `data/T3_search_log.txt` does not exist |
| 10 | literature (B-I Prop. 2/3, Q3, size 11, CMSV, Croot–Mao–Yip, Chen A.1.x/A.685, the Gloden family in BLP, eslpower Thm 3) | **SURVIVES**, with attribution slips | `a10_literature.py`/`.txt`: all 25 quoted phrases found in `sources/*.txt`; the Gloden family as printed (with f in α3) is verified symbolically |

## Details and fixes

### 2′. Odd-size configurations (Lemma 1.2(4), Def. 1.1, Def. 1.3) — BROKEN as stated

**Finding.** Z = {−24, −18, −8, 5, 45} has

- s₁ = 0,
- s₋₁ = −1/24 − 1/18 − 1/8 + 1/5 + 1/45 = 0,
- no ±pair.

So it is a 2-configuration in the sense of Def. 1.1, with T = 5. That contradicts:

- Lemma 1.2(4) ("T is even and T ≥ 2L+2");
- "2L+2 ≤ τ_L" in Def. 1.3.

Odd sizes 7, 9 and 11 occur too, even with positive integer U and V of small orders (`a02` (A)). [Sig] Theorem S gets parity from genus integrality (|V|−|U| = 2(g−g')), which Def. 1.1 does not impose. The proof of Theorem 2.1 also uses "Since T is even".

Nothing downstream is affected, because every configuration that comes from orbifolds, and every construction in §3, has even size.

**Fix.** Add "|Z| is even (equivalently ι is even)" to Def. 1.1. Alternatively, restrict Lemma 1.2(4), Def. 1.3 and Thm 2.1 to even T, and note that only even T is realisable (Lemma 1.2(2) needs ι/2 ∈ ℤ).

### 2″. Proof of Lemma 1.2(5) — gap, statement true

**Finding.** The proof writes the area through V with genus g′, and then says "if g′=0 … otherwise g′=1". That is valid only when V is the **smaller-genus** side, i.e. |V| ≥ |U|. When ι > 0, V is the larger-genus side, and g′ = g + ι/2 can be ≥ 2.

**Fix.** Insert "By (1), replace Z by −Z if necessary so that V is the side of smaller genus (|V| ≥ |U|)." Also note that V∖{1} ≠ ∅ in the genus-1 case: otherwise R(U) = |V| > |U| ≥ R(U).

### 4′. §7 converse of the pencil theorem — unproved

**Finding.** §7 says "T^cone_3 = 8 … would be a pencil point containing a padding 1". That asserts that every balanced size-8 3-configuration is a pencil point. Theorem 3.1 proves only the other direction. All 7 primitive examples with entries ≤80 are in fact pencils (`a04`).

**Fix.** Write "would be a balanced size-8 configuration containing ±1. Every such configuration found (entries ≤80) is a pencil point." Alternatively, prove the converse. For m=4 it amounts to factoring E(x) + γ²x² = M(x)M′(x) with M, M′ ∈ x⁴+ℚx²+δ.

### 7′. Remark after Theorem 4.1 — false

**Finding.** Write x = A/2π. The new bound is ⌊√((x−1)/3)⌋+2; the old bound is ⌊log₄(x+1)⌋+2.

- On [13,15): new = 4, old = 3.
- On [15,28): they agree.
- From 28 on: new > old.

The project's own `output/growth.txt` shows the same thing: "Theorem 4.1 needs A/2pi >= 13", while Cor. N1 needs 15.

**Fix.** Replace "(the two agree on [4,28))" with "(they agree on [4,13) and [15,28); the new bound is larger on [13,15))".

### 7″. "Best known bound" — wording

**Finding.** B-I p.7 quotes N(k) ≤ ½(k²−3) for k odd and ½(k²−4) for k even (Wright, Melzak). Both are slightly better than ½k(k+1)+1.

**Fix.** In §0 item 2 and in the "Consequence" paragraph, write "the best known bounds are quadratic (B-I Prop. 3: ½k(k+1)+1; Wright/Melzak: ½(k²−3), ½(k²−4))". The exponent ½ is unchanged.

### 9. §6, the T_3 search — exactness claim broken; evidence missing

**What survives.**

- The cubic K t³ − KS t² + M R_n t − M R_d is correct. It was re-derived by own elimination and agrees up to the factor −1.
- K = 0 is impossible, because S·R ≥ 25 by Cauchy–Schwarz.
- A triple root would need S·R = 9 < 25, so the `Q>0` guard of the C code loses nothing.
- Repeated roots force splitting over ℚ, so the exact branch for them is sound.
- Coverage is right: `search_T3.c` and my exact search agree on the number of primitive V (1,828,418) and of cubics with 3 positive real roots (12,423) for v5 ≤ 45. Neither finds a split cubic.

**BROKEN: "exhaustive exact search".** The long-double filter can reject genuine rational roots. `a09` (iv) copies `filter()` verbatim from `search_T3_control.c` and runs it on planted U with non-integral rational entries (K′ from 4 to 1089). It rejects 34 of 27,900, and 33 of these lie in the searched regime e₁(U) = S ≤ 1100.

Two of the rejected cases:

- U = {1681/15, 1694/15, 112}, with S = 337;
- U = {3429/19, 3430/19, 161}, with S = 522.

These are near-multiple roots. They escape the 1e-9 degenerate branch, but Newton in long double cannot place K′r within the 1e-6 tolerance. A genuine collision whose U has clustered rational roots would therefore be missed.

**Positive control too weak.** The control plants integer U only. Its "second batch" is integer as well, since `p` is used unscaled. So the content-free cubic is always monic, K′ = 1, and the q | K′ logic is never exercised. The claim in proof.md that the control uses "planted rational U" is inaccurate.

**Evidence missing.** `data/T3_search_log.txt` is cited in proof.md §6 and in `data/README.md`, but it does not exist. The usage example in `search_T3.sh` (`1 160 10 220`) covers v5 ≤ 169 only: argv[1] of the C program is just a label, and `hi` = s+9 ≤ 169.

**Fixes.**

1. Make the test exact. Use the monic transform y = K′t and find integer roots by bisection on monotone pieces (`mylib.rational_roots_cubic`; about 11k V/s even in Python, and trivial in C with __int128). Alternatively, send every cubic whose relative root gap is below 1e-3 to sympy.
2. Add planted non-integral U with K′ > 1 and near-multiple roots to the control (`a09` (iv) does this).
3. Run to v5 ≤ 220, commit the log, and state the exact command.
4. Until then, state: "exact for v5 ≤ 45 (independent check); float-filtered beyond".

**Minor.** "About 35% of random real V" depends on the sampling (log-normal V). For integer V with v5 ≤ 45 the rate is 12,423/1,828,418 ≈ 0.68%. Say which distribution is meant.

### 10. Literature — attribution slips

**Finding.**

- `LITERATURE.md` §3 attributes [1,5,5]=[2,3,6] to Moessner. Chen A.1.6 lists it as "Smallest solution, by computer search"; Moessner gave the parametric family, with examples such as [0,7,8]=[1,5,9].
- proof.md §5 (balanced L=6) says "two Chen (1,…,9) equalities". The two equalities used are Wróblewski's (2009), as listed in Chen A.1.33 (A.314, A.315).
- B-I p.10 credits the 9- and 10-sets to "Letac and Gloden" jointly. "Letac's two 9-sets" rests on CMSV p.2 ("both found by Letac"), which is fine but should cite CMSV rather than B-I p.9.

**Fix.** Correct the three attributions.

### Cosmetic (no verdict change)

- **Prop. 3.3.** The bullets do not cover 1 ∈ Y. The updated proof's "exchange the roles of X and Y" handles it, but the bullets should say "if 1 ∈ Y∖X, swap X and Y".
- **Prop. 2.2.** It gives τ_L ≥ 2L−1 at best for L ≤ 6, which is weaker than Theorem S. It is useful only asymptotically, in Thm 4.2(a), and could be labelled so.

## Response (applied after this review)

| # | finding | resolution |
|---|---|---|
| 2′ | odd-size configurations | Def. 1.1 now requires $\lvert Z\rvert$ even (automatic for orbifold pairs). The example $\{-24,-18,-8,5,45\}$ is quoted there as the reason. Lemma 1.2(4), Def. 1.3 and Thm 2.1 hold as stated under the amended definition. `statements.tex` amended the same way |
| 2″ | Lemma 1.2(5) proof gap | the proof now works with the side $W$ of smaller genus (the larger side) |
| 4′ | pencil converse used in §7 | §7 now states the converse is not proved and cites `a04` (all 7 balanced size-8 configurations with entries ≤80 are pencils) as an observation only |
| 7′ | false remark on the bound comparison | corrected to "strictly larger exactly on [13,15) and [28,10^6]; equal on [4,13) and [15,28)". `growth.py` now asserts exactly this interval set |
| 7″ | "best known bound" | §0, §4, STATUS and `statements.tex` now say "all known bounds on N(k) are quadratic" (B-I Prop. 3 and the Wright/Melzak bounds of p. 7) |
| 9 | inexact T_3 filter; no log; usage line | Root cause: on arm64 macOS `long double` is IEEE double, while the old tolerances assumed 80-bit precision. `search_T3.c` was rewritten. One `decide()` routine is shared by the search and a test mode; it rejects only when certain: discriminant beyond 4× its error bound; Smith inclusion disks, pairwise disjoint, with errors bounded by 64·LDBL_EPSILON; integrality decided only if $K'\times$radius $<0.2$. Everything else is routed to the exact sympy check. New control `search_T3_control.py`: 53,324 planted genuine U in families A–E (non-integral with K′>1, near-double, exactly repeated), **0 false negatives**; exact agreement with an independent sympy enumeration for v5 ≤ 30. The full search to v5 ≤ 220 was rerun from scratch with the new code, and only that run is relied on (`data/T3_search_log.txt`). The usage line is fixed |
| 10 | attributions | [1,5,5]=[2,3,6] is now "smallest solution, by computer search" (Chen A.48). The L=6 balanced witness's equalities are credited to Wróblewski (2009). Letac's 9-sets cite CMSV p. 2 |
| — | Prop. 3.3 bullets omit 1 ∈ Y | added ("exchange the roles of X and Y") |
