# Missing literature (G7-6): what a referee would expect cited

Result labels used below:

- **(Sig)** signature count ⌊Area/π⌋+4, no uniform count, and n invariants for spheres with n cone points (Theorems A–C).
- **(Thr)** the triangle threshold p+q+r ≤ 17, the minimal pair and its isolation, and three invariants suffice.
- **(Stab)** stability.
- **(Loc)** locality, to be shortened.

Verbatim quotes, pages and fetch logs are in `work/D-classical-spectral.md` (classical spectral), `work/E-forward-sweep.md`
with `work/E-search-log.md` (systematic sweep), and `work/C-algebra-arithmetic.md` §§4–5 (arithmetic and power sums).
BibTeX for every work below is in `references-additions.bib` (fetched records).

## 0. Works that change a novelty claim

| work | claim it changes | how |
|---|---|---|
| Hejhal, LNM 548 (1976), Ch. 3, Thm 5.1, p. 351 | Lemma 4.7; Thm 4.6; Thm 1.2(i) | The trace formula with elliptic terms holds for Hejhal's strip/decay class, which contains the heat function. Lemma 4.7 is redundant and Thm 4.6 is a citation. |
| McKean, CPAM 25 (1972) + correction 27 (1974) | Thm 1.2(i) | For surfaces the heat trace via Selberg is classical. Thm 1.2(i) for orbifolds is the same computation with Hejhal's elliptic term (and Uçar Thm 4.20 at K = −1). Demote it to a cited proposition. |
| Dryden, arXiv:math/0411290 (2004), proof of Thm 4.5, p. 9 | Thm 1.2(iii), Thms 4.9–4.10 | Already reads the systole of a hyperbolic orbisurface off the e^{−ω²/4t} decay. The qualitative content of 4.10(ii)–(iii) is prior art; only the explicit constant and the t^{−1/2} statement remain. |
| Garbin–Jorgenson, Kodai Math. J. 43 (2020), Rem. 2.7, (2.8), p. 101 | Thm 4.6, Cor. 4.11 | Writes Thm 4.6 for the heat kernel with identical normalization. The hyperbolic term visibly carries (16πt)^{−1/2}e^{−(nℓ)²/4t}, so the t^{−1/2} prefactor is in the classical formula. |
| Schinzel, Serdica 22 (1996) p. 588 | Thm 8.9 | "Normalization by rescaling to a common sum" is Schinzel's step, so delete the novelty clause. |
| Kelly, Proc. AMS 107 (1989); Zhang–Cai, Math. Comp. 82 (2013) | Thm 8.9 | Classes of every size for the sum–product analogue via positive-rank elliptic curves (Kelly predates Schinzel). |
| Borwein–Ingalls, Enseign. Math. 40 (1994), Prop. 1, §3 | Thm A (complex case) | Equal power sums up to k ⇔ deg(∏(x−α)−∏(x−β)) ≤ n−k−1. With β = −α this gives the classical fact that odd power sums determine a complex multiset up to pairs {a,−a}. "What is new is the complex case" must go. |
| BGN, Math. Comp. 61 (1993) p. 117, §4 table p. 120 | Prop. 8.4, Thm 8.5, l. 1364 | The reciprocal-pair and permutation structure on C_Λ is BGN's; it is presented without credit. |

Works that do **not** change a claim but must be cited: Philippe 2008/2010 (Thr), Stanhope 2005 (Sig),
Huber 1959, Wolpert 1979, Buser 1992 (Loc), Schueth 2025 (input formula), Watson 2005 (input formula),
Chang–DeTurck 1989 (Sig analogue), Akinshin–Batenkov–Yomdin 2015 / Batenkov–Goldman–Yomdin 2020 (Stab),
the DGGW erratum, an NGSolve reference.

**No scoop found.** No prior or competing work gives a finite heat-coefficient count for hyperbolic orbifolds,
a heat-invariant threshold for triangle orbifolds, or a stability estimate for recovering cone orders. Searches covered
the 2024–2026 arXiv, forward citations of DGGW, Uçar and Dryden–Strohmaier, zbMATH and OpenAlex (E §0, search log).
This negative result is bounded by the coverage gaps in GAPS.md.

## 1. Items named in the brief

### 1.1 McKean 1972 (+ 1974 correction)
- **What it proves:** the Selberg trace formula derived through the heat kernel for compact Riemann surfaces, and
  finiteness of isospectral sets of compact Riemann surfaces. It covers torsion-free groups only, so no elliptic terms.
  Known only through secondaries: Linowitz, Dryden 2004, Courtois–Kim, Pollicott, Garbin–Jorgenson. Primary unreachable (Wiley 403).
- **Relation:**
  - (Loc) the surface case of Thm 1.2(i) and the mechanism of 1.2(iii);
  - Remark 4.13: finiteness of what the trace misses;
  - none to (Sig), (Thr), (Stab).
- **Cite at:** the discussion of Thm 4.1 (l. 636), the proof of Thm 4.6, Remark 4.13, §1.1.
- **Caution:** do not attribute an explicit "O(e^{−c/t})" sentence to McKean with a pinpoint until the primary has been read.

### 1.2 Hejhal LNM 548 (and LNM 1001); Iwaniec GSM 53
- **Hejhal Vol. I, Ch. 3 (pp. 326–354), Thm 5.1, p. 351, trivial character:** the trace formula for cocompact Γ *with*
  elliptic elements. Hypothesis (Dryden 2004, p. 7, quoting Hejhal): h analytic on |Im r| ≤ ½+δ, even,
  |h(r)| ≤ M(1+|Re r|)^{−2−δ}. Dryden, p. 8: "Fix t > 0 and let h(r) = e^{−r²t}. Then h(r) satisfies Assumption 4.2."
  Garbin–Jorgenson p. 102 confirm their heat formula "agrees with the formula in Theorem 5.1 of [Hejhal], with χ being
  the trivial character". Dryden–Strohmaier's own eq. (1) is attributed there to Hejhal and Iwaniec ("see [7], [8]").
- **Iwaniec:** (1.63) is the same admissible class, and Thm 10.2 has the elliptic term. It is stated for finite-volume
  groups; whether it covers the cocompact case is unconfirmed, so cite it as "see also".
- **Decision:** Lemma 4.7 is redundant and should be deleted. Thm 4.6 becomes a citation; keep the displayed
  normalization. Remark 4.12's "not an independent proof" caveat lapses: with Hejhal cited, the trace-formula route is
  independent of DGGW and Uçar. This also supplies the Uçar-free all-order route to Lemma 2.5 that G7-3 asks for
  (A §3: DGGW and Donnelly give closed forms only at t⁰ and t¹).
- **Gap:** primary pinpoints were attested by two independent secondaries; the primaries were not read.

### 1.3 Huber 1959 (and 1961)
- **Read in full** (GDZ scans, OCR).
  - Sätze 7–8 (p. 8): for closed surfaces, the length spectrum and the eigenvalue spectrum determine each other and the genus.
  - Satz 9 (p. 10): the prime geodesic asymptotic e^t/t.
  - No elliptic elements.
- **Relation:**
  - Dryden–Strohmaier 2009 ("Huber's theorem for hyperbolic orbisurfaces") is the orbifold generalization.
  - Remark 4.13: heat trace → spectrum → length spectrum.
  - Lemma 4.8: asymptotic counterpart.
  - (Sig): for surfaces the genus is already a spectral invariant; the count stays new.
- **Cite at:** Remark 4.13, Lemma 4.8, §1.1.

### 1.4 Kelly
- **Kelly, "Partitions with equal products", Proc. AMS 15 (1964) 987–990.** Motzkin's question. Per Cha et al., Thm 1.1,
  s₂(3) = 23 and s*₂(3) = 19. Body not read (AMS 429).
- **Kelly, "Partitions with equal products. II", Proc. AMS 107 (1989) 887–893** (abstract verbatim): "There exist
  infinitely many integers having r partitions into k parts such that the products of the integers in each partition are
  equal … Of some additional interest is a lemma stating that a certain class of elliptic curves has positive rank over Q."
- **Relation:** (Thr/§8). Kelly 1989 is the first "classes of every size" theorem in the sum–product problem; Thm 8.9 is its
  (S, R) counterpart. Kelly 1964 suggests asking, for (S, R), whether every large sum carries a class (§8.4).
- **Cite at:** l. 1426 and §8.4.

### 1.5 Zhang–Cai 2013
- **Zhang–Cai, Math. Comp. 82 (2013) 617–623** (abstract): "for every k, there exists infinitely many primitive sets of k
  n-tuples of positive integers with the same sum and the same product". Method per Ulas (arXiv:1305.6237): σ₁ = σₙ = 2n,
  Schinzel's normalization for general n. Ulas, citing Zieve: "the result from [9] follows from Schinzel's work". Body not read (AMS 429).
- **Relation and citation:** as Kelly 1989.

### 1.6 The DGGW erratum
- **Michigan Math. J. 66 (2017) 221–222, DOI 10.1307/mmj/1488510034, read in full.** It adds the hypothesis
  "Iso^max(N) nontrivial" to **Thm 5.1 only**. For a cone point Iso^max(N) is all nontrivial rotations, so nothing the
  manuscript uses is affected.
- **Cite at:** next to the first dggw2008 citation ("see also the erratum, which concerns only Thm 5.1").

## 2. Systematic sweep

### (a) Forward citations of DGGW 2008, Uçar 2017, Dryden–Strohmaier 2009
About 60 distinct citing works were found through OpenAlex and Semantic Scholar and triaged. Crossref cited-by was
unavailable, and the zbMATH citation index is incomplete (2 for DGGW, 0 for D–S). The relevant hits:

| work | proves | relation | cite at |
|---|---|---|---|
| Schueth, Ann. Global Anal. Geom. 69 (2025) no. 2 (arXiv:2511.22255) | b_{1/2} for curved conical singularities. p. 2: "Uçar [13] obtained explicit formulas for all b_ℓ(C) … p_ℓ is a certain polynomial of order 2ℓ+2" | (Sig)/(Loc) input: a refereed attestation of the all-order closed form behind Lemma 2.5 | l. 220, alongside Uçar |
| Stanhope, AGAG 27 (2005) | finitely many isotropy types and bounded number of singular points among isospectral orbifolds with a lower Ricci bound (Main Thms 1–2) | (Sig): the earliest "spectrum controls the cone data" result; finiteness, no count | §1.1 first paragraph |
| Dryden, arXiv:math/0411290 (2004) | Thm 4.5: cone orders and length spectrum "up to finitely many possibilities"; Thm 5.1: finite isospectral sets for genus ≥ 1; p. 5: whether the spectrum determines the genus was then open | (Sig) prior finiteness; (Loc) systole from e^{−ω²/4t}; Remark 4.13 | §1.1, before Thm 4.9, Remark 4.13 |
| Gordon, "Orbifolds and their spectra", PSPUM 84 (2012) 49–71 | survey (unread, AMS 429) | background | §1.1, as a survey only |

### (b) Finite or quantitative spectral determinacy, 2010–2026

| work | proves | relation | cite at |
|---|---|---|---|
| Philippe, Ann. Inst. Fourier 58 (2008), Thm A; Geom. Dedicata 149 (2010) (read as Thm 3.1 of Sémin. TSG 28 (2010)) | the length spectrum determines every triangle group Γ(r,p,q); in practice the first two or three lengths with multiplicities suffice; "systolic twins" such as Γ(2,3,10)/Γ(2,5,5) | (Thr): the length-side analogue of the threshold and of the minimal pair. It does not touch the heat-invariant claim. | §1.1; optionally §5 |
| Chang–DeTurck, Proc. AMS 105 (1989) 1033–1038 (outside the date range, but on point) | the first N Dirichlet eigenvalues determine a Euclidean triangle, with N depending on λ₁, λ₂ (zbMATH review, Mårdby–Rowlett survey; primary unread) | (Sig)(ii): the same shape, a finite count that is not uniform and is read off from low-order data | l. 178 |
| Grieser–Maronna (already cited) | the first three heat invariants determine a Euclidean triangle | (Thr): direct analogue | sharpen the l. 178 sentence |
| Mårdby–Rowlett survey, Rev. Math. Phys. (2026) | nothing on hyperbolic orbifold heat invariants | negative evidence that the area was open | not needed |

### (c) Heat invariants of cone and orbifold singularities

| work | content | action |
|---|---|---|
| Watson, N. Z. J. Math. 34 (2005) 81–95 | all-order heat expansion for spherical polygons; Uçar's (4.25) is Watson's lune formula "with minor corrections" (Uçar p. 134) | **cite** with Uçar at l. 220/224 (text unread) |
| Cheeger, JDG 18 (1983) (4.42); Brüning–Seeley, JFA 73 (1987) p. 424; Kokotov, Proc. AMS 141 (2013) Thm 1; Aldana–Kirsten–Rowlett, Ann. Math. Québec 50 (2025) | the constant term (1/12)(2π/γ − γ/2π) for a cone of angle γ, which is (m²−1)/(12m) at γ = 2π/m | optional history clause at l. 269 |
| Donnelly, Illinois J. Math. 23 (1979) 485–496, as quoted in Dowker arXiv:2311.12708 eq. (1) | exact integral for the elliptic contribution at K = −1. Checked numerically: it reproduces b₀ and b₁; the expanded elliptic term reproduces Uçar's b₀, b₁, b₂ to 12 digits | optional at l. 791. **Supports the Uçar-free proof of Lemma 2.5** |

### (d) Stability in inverse spectral and moment problems

| work | content | relation to (Stab) | cite at |
|---|---|---|---|
| Akinshin–Batenkov–Yomdin, SampTA 2015 | worst-case error of order ε^{1/(2l−1)} for an l-node cluster, with unknown amplitudes | the contrast: with unit weights the problem is polynomial roots and the exponent is 1/k. "Loss of Lipschitz stability at collisions" is standard; the 1/k rate for cone orders is not in the literature found | §6, beside Ostrowski (l. 1136) |
| Batenkov–Goldman–Yomdin, Inf. Inference 10 (2021) | minimax rate SRF^{2p−1}ε for near-colliding sources | same | same |
| Batenkov–Yomdin, SIAM J. Appl. Math. 73 (2013) | the Prony map is singular exactly at node collisions | the analogue of the Orlando locus being the singular set of Thm B | optional |

`review/literature/stability-inverse-spectral.md` (earlier pass) already covers root-perturbation classics.
Nothing found gives quantitative stability for orbifold or cone data from heat invariants.

### (e) Triangle groups and hyperbolic orbisurfaces
- **Philippe:** see (b).
- **Linowitz–Voight follow-ups** (16) are all arithmetic. **Doyle–Rossetti follow-ups** are about lens spaces, Steklov
  problems and G-sets. Neither touches heat invariants or signatures.
- **Kravchuk–Mazáč–Pal and Gesteau et al.** (spectral bootstrap for triangle orbifolds): optional context for §7, not needed.
- **Maclachlan–Rosenberger 1994** (small isospectral hyperbolic 2-orbifolds): not fetched; Linowitz–Voight already
  covers isospectral same-signature pairs.

## 3. Arithmetic and power-sum literature (G7-6 list)

| work | relation | cite at |
|---|---|---|
| Borwein–Ingalls 1994, Prop. 1, §3 (read in the preprint, page image) | the classical framework behind Thm A, Thm C(1), Prop. 3.9 (Prouhet) and Problems 1–2. Also the right source for ideal PTE solutions (l. 1487) | Thm A paragraph (l. 176), l. 1487, Problems 1–2 |
| Bremner–Guy, Proc. Edinburgh Math. Soc. 40 (1997) | (x+y+z)³/xyz, the sum–product invariant e₁³/e₃; Schinzel's curve is a fibre of it. This explains why Schinzel's method transfers to Λ = e₁e₂/e₃ | §8.1 |
| Sadek–El-Sissi, Osaka J. Math. 52 (2015), Thm 2.8 | sum–product curves: isosceles triples are torsion, with the same torsion groups Z/6 and Z/2×Z/6 | Remark 8.6 (parallel), l. 1364 |
| Nguyen, Ann. Math. Inform. 54 (2021) | no positive solutions of BGN's equation when 4 \| n | §8.1 (optional) |
| Schoen, Math. Z. 197 (1988) | fibre products of rational elliptic surfaces: the frame for counting pairs on the self-fibre product (Conjecture 8.10, G7-9) | §8.4 (optional; unread) |
| Guy, Unsolved Problems, D16 | source of the sum–product problem | §8 intro (optional; unread) |
| Pragacz 1991 Thm 2.11 / Macdonald III.8 (Q-cancellation; via a secondary only) | odd power sums generate the functions insensitive to {a,−a} pairs | do not cite until read; Borwein–Ingalls suffices |
| NGSolve | the FE solver used | l. 1286, l. 1578 |
