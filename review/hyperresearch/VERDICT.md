# VERDICT

Literature sweep on *How Few Heat Invariants Determine a Hyperbolic Triangular Pillow*.
Answers to the six deliverable questions, in the order asked. Supporting detail in the
per-question files alongside this one; unretrieved sources and flagged discrepancies in
`review/outstanding-fetches.md`; fetched bibliography in `refs/sources.bib`.

Every formula quoted below was read from the source document itself. Every DOI was retrieved
from an authoritative record. Nothing was written from memory.

---

## 1. Is Section 5's Diophantine problem new?

**Yes — new**, on a well-controlled negative search. Detail in `Q1-diophantine-novelty.md`.

The problem — two distinct triples with equal sum and equal sum of reciprocals — is not posed
in Guy's *Unsolved Problems in Number Theory* (3rd ed., 2004,
[`10.1007/978-0-387-26677-0`](https://doi.org/10.1007/978-0-387-26677-0), whole book grepped:
zero hits for `2,8,8`, `3,3,12`, `triangle group`, `orbifold`, `covolume`, `Takeuchi`), not
in OEIS, and not in the Egyptian-fraction research literature including its current survey
(Bloom–Elsholtz, arXiv:2210.04496).

The OEIS null is controlled rather than bare: a search for the structurally analogous *known*
problem — equal sum and equal **product** — correctly returns
[A334911](https://oeis.org/A334911). The method works on a problem of this shape; its silence
on ours is evidence of absence.

**A correction to the brief:** the sections to look at are not D11 and D12. §D11 is Egyptian
fractions (single-fraction representation only) and **§D12 is Markoff numbers**, unrelated.
The relevant section is **§D16, "Triples with the same sum and same product"** (p. 271) — the
same problem shape for $(e_1,e_3)$ instead of $(e_1,e_2/e_3)$ — which Guy reports **Schinzel
solved**: arbitrarily many triples with common sum and product, via rational points on the
elliptic curve $y^2 = x^3 - 9x + 9$ (Serdica Math. J. 22 (1996), 587–588).

**What remains new, precisely:** the $(e_1, e_2/e_3)$ matching condition, the specific
coincidence $\{(2,8,8),(3,3,12)\}$, the sharp threshold at 17, and the counting function.
$(2,8,8)$ and $(3,3,12)$ both appear on Takeuchi's list of 85 arithmetic triangle groups
(J. Math. Soc. Japan **29** (1977), 91–106,
[`10.2969/jmsj/02910091`](https://doi.org/10.2969/jmsj/02910091), read in full), but for
arithmeticity reasons logically independent of the reciprocal sum, and nothing remarks on
their equal covolume.

**One live thread:** Takeuchi's 85 triples fall into 19 commensurability classes, and the
class assignment lives in a companion paper that could not be retrieved (J. Fac. Sci. Univ.
Tokyo Sect. IA Math. **24** (1977), 201–212). If $(2,8,8)$ and $(3,3,12)$ share a class the
pair may have an unremarked prior appearance there. Note that commensurable groups have
covolumes in *rational ratio*, not equal ratio, so even a positive answer would not make
Theorem B prior art — but it would need citing.

**Recommendation:** cite D16 and Schinzel in §5. It costs a sentence, situates the problem,
and points at the one technique — elliptic curves — that might improve the unconditional
lower bound past $\lfloor S/18\rfloor$.

*Independently verified:* Table 5.1's cumulative pair counts reproduce exactly in exact
rational arithmetic (1, 92, 386, 840, 1496, 2210, 3067), as does the $S=36$ structure.

## 2. Is the quoted $b_1$ correct as printed?

**Yes.** Detail in `Q2-cone-coefficients.md`.

Schueth, arXiv:1812.06119, **Remark 4.2**, verbatim:

> $$a_1^{(\{\bar p\})} = \Bigl[\tfrac{1}{360}\Bigl(k^{3}-\tfrac1k\Bigr)+\tfrac{1}{36}\Bigl(k-\tfrac1k\Bigr)\Bigr]K(\bar p)$$
> … Note that the above formulas for $a_0^{(\{\bar p\})}$ and $a_1^{(\{\bar p\})}$ were
> already computed in [8], 5.6.

Identical to equation (4) under $m\leftrightarrow k$, and the attribution to DGGW §5.6 is
Schueth's own. Checked independently at the original source: DGGW §5.6 derives the per-cone
contribution $R_{1212}(m^4+10m^2-11)/(360m)$, which expands to exactly the same expression.
$b_0$, the $1/m$ isotropy average, and the absence of a $(4\pi t)^{-1}$ prefactor on a
zero-dimensional stratum all check out. **No sign or factor convention differs between the
sources.** Equation (5) was verified symbolically.

Published record: Ann. Inst. Fourier (Grenoble) **69** (2019), no. 7, 2827–2855,
DOI [`10.5802/aif.3338`](https://doi.org/10.5802/aif.3338).

**One caveat on attribution style:** Uçar never writes "$b_\ell(C)=\kappa^\ell\frac1m p_\ell(m)$"
and never uses the word *degree*. That is the manuscript's paraphrase of his Bernoulli-number
closed form. It is faithful, but cite equations (4.25) p. 134 and (4.33) p. 137 rather than
implying a quotation.

**Also:** there is an uncited **DGGW erratum** — Michigan Math. J. **66** (2017), 221–222,
DOI [`10.1307/mmj/1488510034`](https://doi.org/10.1307/mmj/1488510034). It was checked in
full and corrects **only Theorem 5.1**, not §5.6, so equation (4) is unaffected. But it
exists and should be cited. (It opens by crediting "a question from Naveed Bari" — the Bari
of Bari–Hunsicker.)

## 3. Are the higher $b_\ell$ established well enough to support a $K \le n+1$ theorem, or must we compute them ourselves?

**They are established. No new cone-coefficient computation is required** — and this holds
well beyond $\ell = 2$. Detail in `Q2-cone-coefficients.md`.

- **DGGW stop at $\ell=1$.** Full-text search returns no general-$\ell$ statement and nothing
  for $\ell\ge2$.
- **Schueth Theorem 4.1 gives $\ell=2$ in closed form.** At constant curvature the
  $\Delta_gK$ bracket vanishes identically, leaving
  $a_2 = [\frac{1}{2520}(k^5-\frac1k)+\frac{1}{720}(k^3-\frac1k)+\frac{1}{180}(k-\frac1k)]K^2$.
  Summed at $K=-1$ this delivers $P_5$ with coefficient $1/2520$.
- **Uçar gives every $\ell$.** Equations (4.25) p. 134 + (4.33) p. 137 form a finite
  Bernoulli-number sum, explicit and uniform in $\ell$ — not a degree bound. Schueth's Remark
  5.4(ii) independently attests: Watson ($K=1$) and Uçar (all constant $K$) "**actually
  computed $c_\ell(\gamma)$ for every $\ell\in\mathbb N_0$**", with
  $c_\ell(\gamma)=f_\ell(\gamma)K^\ell$.

Evaluated: $p_2(m)=\frac{2m^6+7m^4+28m^2-37}{5040}$ (degree 6, leading $1/2520$, delivers
$P_5$) and $p_3(m)=\frac{3m^8+8m^6+14m^4+32m^2-57}{30240}$ (degree 8, leading $1/10080$,
delivers $P_7$). **The $\ell=2$ case is cross-validated**: Uçar's form and Schueth's Theorem
4.1 agree symbolically to zero — two sources, two different methods.

So both $P_5$ and $P_7$ are recoverable, and the leading term of $p_\ell$ is known in closed
form. The residual work is **algebraic, not analytic**: discharging the "when these are
independent" hedge in Remark 5.6 is a symmetric-function question.

**A concrete gain, available now.** An independent exact-arithmetic enumeration run during
this sweep found that

$$\mathcal O(3,10,15,30)\quad\text{and}\quad\mathcal O(4,5,21,28)$$

are non-isometric hyperbolic 4-cone pillows sharing $S_1=58$, $R=8/15$, $P_3=31402$ — hence
their **first three heat coefficients** — and separated by $P_5$. With Schueth's Theorem 4.1
supplying $P_5$ as the fourth coefficient, this gives $K=4$ exactly, **settling for $n=4$ the
matching lower bound that Remark 5.6 leaves open**, with an explicit witness. It is minimal
over all 4-cone pillows with orders $\le 60$. (For $n=5$ the analogous three-invariant
collision is $\mathcal O(3,7,7,7,14)$ vs $\mathcal O(4,4,6,12,12)$, but no four-invariant
collision was found up to order 26, so $n=5$ stays open.) See
`research/temp/original-computation-ncone.md`.

## 4. Does the priority claim in Section 1.3(b) survive?

**Yes, as written.** Two narrowings recommended, neither conceding anything. Detail in
`Q3-priority-claim.md`.

The designated closest competitor, Bari–Hunsicker, fails to compete on three independent
grounds: it proves heat coefficients are **in**sufficient (opposite shape); the insufficiency
holds "for any $k$", i.e. to **all orders**, so it is not a finite count; and the setting is
**spherical** space forms throughout. No minimality is claimed. All five forward citations
stay in the spherical/rank-one world.

**The strongest evidence is positive, and the manuscript does not use it.** Doyle & Rossetti
(arXiv:1103.4372) prove the full-spectrum result for compact hyperbolic 2-orbifolds via the
Selberg trace formula, and say of the finite-coefficient question, verbatim:

> Restricted to hyperbolic 2-orbifolds, the results [DGGW] state don't yield complete
> information about the singular set. All this information is there … presumably it could be
> extracted … by looking at **higher and higher terms** in the asymptotic expansion.

Unbounded, conjectural, no threshold. A specialist source describing exactly the gap the
manuscript closes. **Cite it.**

A twelve-query arXiv sweep (queries listed verbatim in `Q3-priority-claim.md` §5) returned no
independent competitor. The only non-null hits were sources the manuscript already cites, plus
Bartel–Page (arXiv:2407.07240), which is dimension-3 and number-theoretic.

Recommended narrowings: (a) add one sentence contrasting Bari–Hunsicker's all-order
*negative* spherical result with this *positive* hyperbolic threshold; (b) **fix the
attribution chain for qualitative cone-order determinacy**, which is older than §1.3(a)
suggests. Dryden & Strohmaier, Canad. Math. Bull. **52** (2009), 66–71,
[`10.4153/CMB-2009-008-0`](https://doi.org/10.4153/CMB-2009-008-0), Theorem 1.1, already gives
**exact** determination of "the number of cone points of each possible order" from the Laplace
spectrum of a compact orientable hyperbolic orbisurface — in 2009. Doyle–Rossetti follow in
2011; Uçar's Corollary 4.23 is explicitly a generalization of Dryden–Strohmaier to all
$\kappa\neq0$. The manuscript cites Dryden–Strohmaier but describes it only as "a Huber
theorem relating the Laplace and length spectra", which undersells what Theorem 1.1 actually
delivers. None of this touches the finite-coefficient claim — all three are full-spectrum
results — but the chronology should be right.

A free consequence worth stating: since a hyperbolic $(p,q,r)$ triangle orbifold is rigid,
Dryden–Strohmaier's Theorem 1.1 implies at once that **no two non-isometric hyperbolic
triangle orbifolds are Laplace isospectral**. No source states this corollary explicitly, so
present it as an easy consequence, not as new. It is the full-spectrum backdrop that makes the
finite-coefficient threshold the interesting refinement.

**Context the manuscript should absorb:** isospectral non-isometric *hyperbolic* 2-orbifolds
do exist in print — Linowitz–Voight, Math. Z. **281** (2015), 523–569,
[`10.1007/s00209-015-1500-1`](https://doi.org/10.1007/s00209-015-1500-1), minimal area
$23\pi/6$, three pairs, all of signature $(0;2,2,2,2,2,3,4)$. **Seven** cone points, not
three, so Theorem C is untouched. That paper also narrates a history of *erroneous* claims
about small isospectral hyperbolic 2-orbifolds (Maclachlan–Rosenberger 1994, disproved by
Buser–Flach–Semmler) — a reason to state results narrowly and keep the exact-arithmetic
appendix.

**A separate suggestion, on venue grounds.** None of the twelve comparable JGA papers claims
priority, including one that proves a finiteness theorem with explicit bounds. The result
here is sharp on its own terms, and "to our knowledge this is the first…" is the sentence
most exposed to a referee who knows one paper the author does not — and this sweep found
several the manuscript does not cite. The Doyle–Rossetti quote does the same work with less
risk.

## 5. Is the planned stability theorem novel, and what is the right technique?

**Novel in setting, not in technique.** Detail in `Q4-stability.md`.

**Technique: nothing is new.** The manuscript's Jacobian
$\det DF = -3(p-q)(p-r)(q-r)(p+q)(p+r)(q+r)/(pqr)^2$ is the classical root-conditioning
quantity rearranged — for a monic cubic, $|p'(p)| = |(p-q)(p-r)|$. More pointedly,
**Batenkov–Yomdin** (arXiv:1106.1137, SIAM J. Appl. Math.) already prove, for the Prony
system, that the Jacobian factors through a confluent Vandermonde matrix (Lemma 4.2), that
its **critical points are exactly the node collisions** (Corollary 4.3 — structurally
identical to the manuscript's diagonals), and that local accuracy scales as a power of
$\prod_{i<j}|\xi_j-\xi_i|^{-1}$ (Theorem 4.5), matching the Cramér–Rao bound.

**Setting: genuinely open**, on a documented null. Eight arXiv queries — listed verbatim in
`Q4-stability.md` §4 — return nothing. The only quantitative-stability result in an orbifold
setting is Lassas–Lu–Yamaguchi (arXiv:2404.16448), which reconstructs a *continuous metric*
from interior eigenfunction data with a **triple-logarithmic** modulus — a different technical
species. The Proctor–Stanhope finiteness line is qualitative with no effective bound. Across
all of inverse spectral geometry, no Lipschitz or Hölder stability estimate exists; log-type
(Daudé–Kamran–Nicoleau, J. Geom. Anal. **31**, 1821–1854,
[`10.1007/s12220-019-00326-9`](https://doi.org/10.1007/s12220-019-00326-9)) is the good case.

**Right technique:** run the Prony/super-resolution route. Treat $(S_1,R,P_3)$ as moments;
cite Batenkov–Yomdin Cor. 4.3 for the critical locus rather than reproving it; take the
blow-up rate either from their Thm 4.5 or, better at $n=3$, from
$|p'(z_k)|=|(z_k-z_i)(z_k-z_j)|$ directly, which gives sharper explicit constants. Support
with Gautschi–Inglese ([`10.1007/BF01398878`](https://doi.org/10.1007/BF01398878)) and Pan
(arXiv:1504.02118) for Vandermonde conditioning, and Wilkinson
([`10.1007/BF01386381`](https://doi.org/10.1007/BF01386381)) for the classical statement.

**Then add the part that is actually yours.** Because $p,q,r$ are positive **integers**, an
error below half the minimum gap gives *exact* recovery. That turns a conditioning estimate
into a determinacy-from-noisy-data theorem — "there is an explicit $\epsilon(p,q,r)>0$ such
that spectral data within $\epsilon$ determines the cone orders exactly" — with the diagonal
blow-up appearing as the degradation of $\epsilon$. That statement has no counterpart in the
numerical-analysis literature and is the natural spectral-geometry reading.

Explain *why* the modulus can be algebraic where the field's best is logarithmic: the
invariant recovered is finite and discrete, not a continuous metric. Otherwise the strength
will read as an overclaim.

## 6. What does this paper have to look like to be a JGA paper?

It already largely does. Detail in `Q5-venue.md`, with twelve Crossref-retrieved comparators.

**The venue.** JGA in this area publishes substantial papers (26–58 pp among the comparators;
the closest exemplar runs ~18,000 words) that favour **exact results over asymptotic ones**,
and that use computation to certify or instantiate a structural theorem rather than to
constitute it. The manuscript at 44 double-spaced pages is comfortably in range, and its
architecture — interval-separation proof in §3, exhaustive enumeration relegated to an
appendix as corroboration — matches the house style well.

**The exemplar** is Dryden, Gordon, Moreno, Rowlett & Villegas-Blas, *The Steklov Spectrum of
Convex Polygonal Domains I: Spectral Finiteness*, JGA **35**(3) art 91 (2025),
[`10.1007/s12220-025-01922-8`](https://doi.org/10.1007/s12220-025-01922-8) — a finiteness
result with **explicit upper bounds** on cornered domains, two of whose authors wrote DGGW. It
is simultaneously the venue precedent, the referee signal, and the model for tone: it claims
no priority.

**What to change:**

1. **Fix the bibliography.** Four cited "preprints" are published — Bari–Hunsicker
   (Canad. J. Math. 2020), Schueth (Ann. Global Anal. Geom. 2026,
   [`10.1007/s10455-025-10024-1`](https://doi.org/10.1007/s10455-025-10024-1)),
   Gómez-Serrano–Orriols (J. Differential Equations), Proctor–Stanhope (Diff. Geom. Appl.
   2010), Richardson–Stanhope (Diff. Geom. Appl. 2020) — and the DGGW erratum, Doyle–Rossetti
   and Linowitz–Voight are uncited. At a Springer journal with a copy-editing pass, stale
   preprint citations read as a paper prepared without checking.
2. **Add the $n$-cone material.** It is cheaper than the manuscript assumes and materially
   raises the reach — see answer 3.
3. **Reconsider the priority sentence** — see answer 4.
4. **Situate §5** against Guy D16 and Schinzel — see answer 1.
5. **Keep the structural proof primary.** This is the strongest architectural match to the
   venue; §3's own framing already has the right instinct.

**Plausible referees**, each with a recent supporting publication: Emily Dryden and Carolyn
Gordon (DGGW co-authors; JGA 2025), Dorothee Schueth (author of equation (4)'s source), Julie
Rowlett, Elizabeth Stanhope, Juan Pablo Rossetti, David Sher, Eugenie Hunsicker, Emilio
Lauret, and the Farsi–Proctor–Seaton group. Note the conflict clusters: Dryden, Gordon and
Rowlett co-authored the JGA exemplar; Schueth and Uçar are both at Humboldt.

---

## Summary of corrections the manuscript needs

| # | Item | Severity |
|---|---|---|
| 1 | Bari–Hunsicker published: Canad. J. Math. **72** (2020) 281–325, `10.4153/S0008414X19000178` | bibliography |
| 2 | Schueth curved-cone paper published: Ann. Global Anal. Geom. **69** (2026) Paper No. 2, `10.1007/s10455-025-10024-1` | bibliography |
| 3 | Gómez-Serrano–Orriols published: J. Differential Equations, `10.1016/j.jde.2020.11.002` | bibliography |
| 4 | Proctor–Stanhope published: Diff. Geom. Appl. **28** (2010) 12–18, `10.1016/j.difgeo.2009.03.015` | bibliography |
| 5 | Richardson–Stanhope published: Diff. Geom. Appl. **68** (2020) 101577, `10.1016/j.difgeo.2019.101577` | bibliography |
| 6 | DGGW erratum uncited: Michigan Math. J. **66** (2017) 221–222, `10.1307/mmj/1488510034` | bibliography |
| 7 | Gittins et al. **Part 2 is published**: Michigan Math. J., advance publication (2026), `10.1307/mmj/20236493`; **Part 1** uncited: Michigan Math. J. **74** (2024) no. 3, 571–598, `10.1307/mmj/20216126` | bibliography |
| 8 | Shams–Stanhope–Webb page range: publisher of record gives **375–385**; manuscript prints 375–384 | bibliography |
| 9 | §1.3(a) credits Uçar alone for qualitative cone-order determinacy. **Dryden–Strohmaier (2009) Thm 1.1** gives it exactly, and **Doyle–Rossetti (2011)** independently; Uçar generalizes Dryden–Strohmaier. The manuscript cites Dryden–Strohmaier but under-describes it. | **substantive** |
| 10 | Doyle–Rossetti (arXiv:1103.4372) uncited | substantive |
| 11 | Linowitz–Voight (Math. Z. **281** (2015) 523–569) uncited | substantive |
| 12 | Uçar attribution should cite eq. (4.25)/(4.33), not paraphrase | precision |
| 13 | §5.3's "birthday-paradox … standard in analogous Diophantine settings" has no documented precedent in the unit-fraction literature | precision |
| 14 | Datchev–Hezari year: the primary MSRI PDF and Cambridge's Crossref record both give **2012**; manuscript prints 2013. (Pages 455–485 are correct — Crossref's 455–486 is wrong.) | bibliography |
| 15 | Gómez-Serrano–Orriols full record: J. Differential Equations **275** (2021), 920–938 | bibliography |
| 16 | Nursultanov–Rowlett–Sher: Ann. Math. Québec **49**, 1–61, issue year **2025**; manuscript gives "(2024)" with no volume or pages | bibliography |
| 17 | Guy D16 / Schinzel unengaged in §5 | opportunity |
| 18 | Remark 5.6's open lower bound is settled for $n=4$ | opportunity |

**Two apparent discrepancies were checked and resolved in the manuscript's favour** — no change
needed for either: Hezari–Zelditch is indeed Ann. of Math. **196** (2022), no. 3, 1083–1134
(the arXiv comment's "197 (2023)" is wrong), and Doyle–Rossetti 2008 is indeed *New York
J. Math.* **14** (2008), 193–204. New York J. Math. registers no DOIs for that era, so the
absence of one is correct rather than a gap.

One item could not be primary-verified: McKean–Singer's page range 43–69 is corroborated only
by a secondary index, since Project Euclid, JSTOR and MathSciNet all blocked automated access.
Venue, volume, year and DOI are confirmed.

**Nothing in the manuscript's mathematics was found to be wrong.** Equations (3), (4), (5),
(9), the Jacobian, the cotangent and cosecant identities, Table 5.1's counts and the $S=36$
structure were all independently re-derived or recomputed and all check out.
