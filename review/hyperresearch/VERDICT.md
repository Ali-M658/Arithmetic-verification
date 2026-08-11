# VERDICT

Literature sweep on *How Few Heat Invariants Determine a Hyperbolic Triangular Pillow*.
Answers to the questions asked, in order. Supporting detail in the per-question files
alongside this one; unretrieved sources and flagged discrepancies in
`review/outstanding-fetches.md`; assembled bibliography in `refs/sources.bib`.

Every formula quoted below was read from the source document itself. Every DOI was retrieved
from an authoritative record. Nothing was written from memory.

## At a glance

| # | Question | Answer |
|---|---|---|
| 1 | Is §5's Diophantine problem new? | **Yes** — with one retrieval still open (Takeuchi's commensurability classes) |
| 2 | Is the quoted $b_1$ correct as printed? | **Yes**, exactly — and its attribution is right too |
| 3 | Are the higher $b_\ell$ established, or must we compute them? | **Established at every $\ell$** — no new cone-coefficient computation. But the injectivity argument is still owed |
| 4 | Does the §1.3(b) priority claim survive? | **True, but delete it** — it rests on four simultaneous qualifiers |
| 5 | Is the planned stability theorem novel? | **In setting, not technique.** The invariant map *is* a Prony system — cite the theory, make the integer-exactness the theorem |
| 6 | What must the paper look like for JGA? | **Close to what it is** — plus a repaired bibliography, the $n$-cone extension, and no priority sentence |

**22 corrections and opportunities** are itemised at the end, six of them bibliographic and
four substantive. One is a genuine mathematical defect: Remark 5.6's $K\le n$ does not hold
for $n\ge4$ in the sense Theorem C uses.

---

## 1. Is Section 5's Diophantine problem new?

**Yes — new**, on a well-controlled negative search, with one retrieval still open. Detail in
`Q1-diophantine-novelty.md`.

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

**The coefficients are established — no new cone-coefficient computation is required, well
beyond $\ell=2$. The theorem does not follow from them alone: one algebraic step remains.**
Detail in `Q2-cone-coefficients.md`.

Keep the two apart. Settled: the coefficients exist in closed form at every order. Not
settled: *injectivity* of $(R,S_1,P_3,P_5,\dots)$ on cone-order multisets — Remark 5.6's own
"when these are independent" hedge — for which the only direct evidence here is a bounded
scan. So the answer to the question as posed is: **the cone coefficients need not be computed;
the injectivity argument must still be supplied.**

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

Uçar's two operative equations were evaluated **directly, in exact symbolic arithmetic**, at
$\ell=0,1,2,3$:

| $\ell$ | $b_\ell/\kappa^\ell$ factored | $\deg p_\ell$ | leading coeff | delivers |
|---|---|---|---|---|
| 0 | $\frac{(m-1)(m+1)}{12m}$ | 2 | $1/12$ | $S_1$ |
| 1 | $\frac{(m^2-1)(m^2+11)}{360m}$ | 4 | $1/360$ | $P_3$ |
| 2 | $\frac{(m^2-1)(2m^4+9m^2+37)}{5040m}$ | 6 | $1/2520$ | $P_5$ |
| 3 | $\frac{(m^2-1)(m^2+3)(3m^4+2m^2+19)}{30240m}$ | 8 | $1/10080$ | $P_7$ |

Two things make this solid rather than merely reported. The $\ell=0$ and $\ell=1$ rows
**regenerate the manuscript's own $\operatorname{cone}(m)$ and equation (4)** from the same
closed form, confirming the formula is being read correctly. And the $\ell=2$ row is
**cross-validated against Schueth's Theorem 4.1** — the symbolic difference is identically
zero, from two authors using different methods. $\ell=3$ has no second source (Schueth stops
at $\ell=2$), so it was computed from Uçar's printed equations rather than taken on report.

So both $P_5$ and $P_7$ are recoverable, and the leading term of $p_\ell$ is known in closed
form. The residual work is **algebraic, not analytic**.

**And there is a clean route to discharging it.** As answer 5 sets out, the invariant
hierarchy is the moment sequence of a Prony system with nodes $m_i^2$ and weights $1/m_i$.
Under that identification, "do $(R,S_1,P_3,\dots,P_{2n-3})$ determine the multiset?" becomes
"does an $n$-node Prony system with $n$ moments determine its nodes?" — classical, with the
non-degeneracy condition being non-vanishing of the Vandermonde in the *squared* orders, i.e.
simply that the orders are distinct. That is a shorter path than a direct symmetric-function
argument, and it arrives with the conditioning theory already attached.

**The leading coefficient, in closed form.** The brief asks whether it is known. It is:

$$\text{leading coefficient of }p_\ell=\frac{|B_{2\ell+2}|}{2\,(\ell+1)!\,(2\ell+1)},$$

checked against the direct evaluations $\tfrac1{12},\tfrac1{360},\tfrac1{2520},\tfrac1{10080}$
at $\ell=0,1,2,3$. Since $B_{2k}\neq0$ for all $k\ge1$ (von Staudt–Clausen), it **never
vanishes** — so $b_\ell$ delivers $P_{2\ell+1}$ with nonzero weight at every order. That is
the mechanism a general-$n$ argument needs, rather than a pattern observed at three values.

**A concrete gain, available now.** An independent exact-arithmetic enumeration found that

$$\mathcal O(3,10,15,30)\quad\text{and}\quad\mathcal O(4,5,21,28)$$

are hyperbolic 4-cone pillows with distinct cone-order multisets sharing $S_1=58$, $R=8/15$,
$P_3=31402$ — hence their **first three heat coefficients** — and separated by $P_5$. Over all
4-cone pillows with orders $\le55$ (395,009 multisets) this is the *only* such collision;
extending to $\le60$ (557,844 multisets) adds only its $\times2$ scaling at $S_1=116$. With
Schueth's Theorem 4.1 supplying $P_5$ as the fourth coefficient, **four coefficients determine
the cone-order multiset of a 4-cone hyperbolic pillow and three do not** — Remark 5.6's open
lower bound, settled for $n=4$.

> **But this exposes a definitional problem the manuscript must fix regardless.** $K(F)$ is
> defined as the least number of coefficients distinguishing $F$ from *every other pillow* —
> an isometry-class notion. For $n=3$ that is fine: triangle orbifolds are rigid, so the
> multiset *is* the isometry class. For $n\ge4$ it is not. A sphere with $n$ cone points of
> fixed orders has a $(2n-6)$-dimensional Teichmüller space, so for $n=4$ one multiset carries
> a two-parameter family of non-isometric pillows — and since every heat coefficient depends
> only on the cone orders, that whole family shares **all** of them. **$K(F)$ as defined is
> infinite for $n\ge4$**, and Remark 5.6's "$K\le n$ extends the $n=3$ case of Theorem C" does
> not hold in the isometry sense Theorem C uses. State the $n\ge4$ results as *cone-order
> multiset* determinacy, and note that $n=3$ is the only case where rigidity upgrades that to
> isometry — which is precisely what makes triangular pillows the right object.

(For $n=5$ the minimal three-invariant collision is $\mathcal O(3,7,7,7,14)$ vs
$\mathcal O(4,4,6,12,12)$; no four-invariant collision was found up to order 26, so $n=5$
stays open.) See `review/hyperresearch/APPENDIX-ncone-computation.md`.

## 4. Does the priority claim in Section 1.3(b) survive?

**It is true, but it needs narrowing — and the recommended narrowing is to delete it.**
Detail in `Q3-priority-claim.md`.

Distinguish two things. *No competing result was found*, so on the evidence the sentence is
true. But it survives only on the conjunction of four qualifiers — *exact*,
*finite-coefficient*, *hyperbolic cone orbifold*, *minimal* — and dropping any one brings a
prior result into range:

| Drop | And you meet |
|---|---|
| *hyperbolic* | **Grieser–Maronna**: a Euclidean triangle is determined by three invariants, one of them a **sum of reciprocals** — the same shape as Theorem C. Cited by the manuscript, never engaged. |
| *hyperbolic* and *minimal* | **DGGW Props 5.19 / 5.22**: distinct orbifolds that a *single* heat invariant fails to separate — the Theorem B phenomenon, in the manuscript's own central reference. |
| *finite-coefficient* | **Dryden–Strohmaier (2009)** and **Doyle–Rossetti (2011)**: exact cone-order determinacy for hyperbolic orbisurfaces, from the full spectrum. |

A claim true only on four simultaneous qualifiers is a poor bet in a paper that does not need
it. Replace it with a statement of what is proved plus the Doyle–Rossetti quotation
establishing the question was open: strictly more informative, unfalsifiable by a paper the
author has not read, and matching the house style of every JGA comparator in Q5 — none of
which claims priority.

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

## 5. Is the planned stability theorem novel, and what is the right technique?

**Novel in setting, not in technique.** Detail in `Q4-stability.md`.

**Technique: nothing is new — and the reason is sharper than "the methods are similar".**

The manuscript's invariant map **is a Prony system**, verified symbolically. With nodes
$x_i := m_i^2$ and weights $a_i := 1/m_i$, the $j$-th moment $\sum_i a_ix_i^{\,j}$ is
$R, S_1, P_3, P_5, P_7$ for $j=0,1,2,3,4$ — the whole hierarchy of Corollary D and its
extension, in one system, with the $\ell$-th cone coefficient supplying the $(\ell+1)$-th
moment.

That identification explains the Jacobian exactly, including the factors the root-conditioning
story leaves unaccounted for:

$$\det DF=-\,\frac{3\,\mathrm{Vandermonde}(p^2,q^2,r^2)}{(pqr)^2},$$

i.e. the manuscript's $(p+q)(p+r)(q+r)$ are just what completes each $(m_i-m_j)$ into
$(m_i^2-m_j^2)$. Since $p,q,r>0$, the diagonals **are** the node-collision locus.

So **Batenkov–Yomdin** (arXiv:1106.1137, SIAM J. Appl. Math.) applies directly, not by
analogy: Lemma 4.2 gives exactly this Vandermonde × diagonal factorisation, Corollary 4.3
identifies the critical points as node collisions, and Theorem 4.5 gives local accuracy
scaling as a power of $\prod_{i<j}|\xi_j-\xi_i|^{-1}$, matching the Cramér–Rao bound. In the
squared variables the gaps are $|m_i^2-m_j^2|$ rather than $|m_i-m_j|$, which *improves* the
constants at large orders.

**Setting: genuinely open**, on a documented null. Eight arXiv queries — listed verbatim in
`Q4-stability.md` §4 — return nothing. The only quantitative-stability result in an orbifold
setting is Lassas–Lu–Yamaguchi (arXiv:2404.16448), which reconstructs a *continuous metric*
from interior eigenfunction data with a **triple-logarithmic** modulus — a different technical
species. The Proctor–Stanhope finiteness line is qualitative with no effective bound. Within
inverse spectral geometry on singular spaces — orbifolds, cone surfaces, polygons with
corners — no stability estimate of any modulus was found for recovery of a discrete invariant;
log-type (Daudé–Kamran–Nicoleau, J. Geom. Anal. **31**, 1821–1854,
[`10.1007/s12220-019-00326-9`](https://doi.org/10.1007/s12220-019-00326-9)) is the best modulus
in the corpus gathered.

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

Explain *why* the modulus can be algebraic where the comparable results are logarithmic: the
invariant recovered is finite and discrete, not a continuous metric. Otherwise the strength
will read as an overclaim.

## 6. What does this paper have to look like to be a JGA paper?

**It already largely does.** Detail in `Q5-venue.md`, with twelve Crossref-retrieved
comparators.

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
3. **Replace the priority sentence** — see answer 4.
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
| 17 | **§2.2's trigonometric identities are proved from scratch and called "classical" with no citation.** DGGW cite Berndt–Yeap, Adv. Appl. Math. **29** (2002) 358–385, `10.1016/S0196-8858(02)00020-9` for the same family — including the $\sin^{-4}$ evaluation underlying eq. (4) | **substantive** |
| 18 | **$K(F)$ is ill-defined for $n\ge4$**: Teichmüller dimension $2n-6>0$ means one multiset carries non-isometric pillows sharing every coefficient. Remark 5.6's "$K\le n$" must be restated as multiset determinacy | **substantive** |
| 19 | §1.3 does not reconcile SSW 2006 and RSW 2008 — two "one cannot hear…" results it cites, one of them by the author of eq. (4) | substantive |
| 20 | Guy D16 / Schinzel unengaged in §5 | opportunity |
| 21 | Remark 5.6's open lower bound is settled for $n=4$ | opportunity |
| 22 | **The abstract's constant range contradicts Table 1.** The abstract states $c\approx0.0085$–$0.0093$; Table~1 (`tab:density`) prints $\mathcal N(S)/S^2=0.0097$ at $S=200$ and $0.0094$ at $S=400$, both outside that band. The true range over the manuscript's own printed checkpoints $100\le S\le600$ is **0.0085–0.0097**. Independent exact enumeration confirms it, and confirms the sequence is **decreasing** across the sampled interval: $0.0092,\,0.0097,\,0.0093,\,0.0094,\,0.0088,\,0.0085$ at $S=100,200,300,400,500,600$ (full-sweep extremes over $S\ge100$: $0.00979$ at $S=196$, $0.00851$ at $S=599$). Widen the abstract to 0.0085–0.0097, **and state the downward drift rather than smoothing it over** — a ratio still falling at the top of the computed range is weaker evidence for $\mathcal N(S)\sim cS^2$ (Conjecture 5.3) than a stabilizing one, and §5.3's own hedge ("whether $\mathcal N(S)/S^2$ has in fact stabilized, or is still drifting … cannot be resolved from data at this scale") already concedes the point that the abstract's narrowed band obscures | **substantive** |

**Two apparent discrepancies were checked and resolved in the manuscript's favour** — no change
needed for either: Hezari–Zelditch is indeed Ann. of Math. **196** (2022), no. 3, 1083–1134
(the arXiv comment's "197 (2023)" is wrong), and Doyle–Rossetti 2008 is indeed *New York
J. Math.* **14** (2008), 193–204. New York J. Math. registers no DOIs for that era, so the
absence of one is correct rather than a gap.

One item could not be primary-verified: McKean–Singer's page range 43–69 is corroborated only
by a secondary index, since Project Euclid, JSTOR and MathSciNet all blocked automated access.
Venue, volume, year and DOI are confirmed.

## What was verified, and the one place the mathematics does not hold

**Everything in the manuscript's stated results for $n=3$ checks out.** Independently
re-derived or recomputed in exact arithmetic: equations (3), (4), (5), (9); the Jacobian at
line 269; the cotangent and cosecant identities (symbolically for $m\le12$, and to 40 digits);
Table 5.1's cumulative counts; the $S=36$ structure. So did the **entire logical spine of
Theorems A and B** — $\tau_2=\tau_3=1/6$, $\tau_4=3/20$; $\varphi_2(17)=29/165$ and
$\varphi_2(18)=1/6$ *exactly*; $\varphi_3(12)=7/36$, $\varphi_3(17)=11/63$;
$\min\varphi_4=9/55$; the unimodality peak at $S=3p+4$; all four $S=18$ endpoint comparisons
($101/168>3/5$, $15/28>21/40$, $107/210>1/2$); the first contact at $R=3/4$; and that no
hyperbolic triad exists below $S_1=10$, with $(3,3,4)$ unique at $S_1=10$.

**The one exception is Remark 5.6**, and it is a genuine defect rather than a typo: the
assertion that "the upper bound $K\le n$ extends the $n=3$ case of Theorem C" fails for
$n\ge4$, because $K$ is defined up to isometry and $n$-cone pillows with $n\ge4$ have moduli.
See item 18 above. The remark's *arithmetic* content — that $n$ coefficients supply $n$
symmetric functions — is right; what does not survive is the upgrade from those functions to
an isometry class. The fix is to restate the $n\ge4$ claim as cone-order-multiset
determinacy.
