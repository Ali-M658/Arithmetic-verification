# Q3 — Does the priority claim survive?

**The claim under test**, `paper/main.tex` §1.3(b), line 153:

> To our knowledge this is the first exact finite-coefficient determinacy threshold, with an
> explicit minimal degeneracy, for a family of hyperbolic cone orbifolds.

**Verdict: needs narrowing — and the recommended narrowing is to delete the sentence.**

*No competing result was found*: the literature contains no exact finite-coefficient
determinacy threshold, with an explicit minimal degeneracy, for hyperbolic cone orbifolds. On
the evidence gathered, the sentence is **true**. But it survives only on the conjunction of
four qualifiers — *exact*, *finite-coefficient*, *hyperbolic cone orbifold*, *minimal* — and
dropping any one of them brings a prior result into range: Grieser–Maronna if you drop
*hyperbolic* (§1.5), DGGW's own Propositions 5.19/5.22 if you drop *hyperbolic* and *minimal*
(§1.6), Dryden–Strohmaier and Doyle–Rossetti if you drop *finite-coefficient* (§3).

A claim that is true but load-bearing on four simultaneous qualifiers is a poor bet in a
paper whose result does not need it. **The recommendation is therefore to replace the
priority sentence with a statement of what is proved plus the Doyle–Rossetti quotation
establishing that the question was open** (§3). That is strictly more informative, cannot be
falsified by a paper the author has not read, and matches the house style of every comparable
JGA paper surveyed for Q5 — none of which claims priority.

---

## 1. The designated closest competitor is not a competitor

Bari & Hunsicker, *Isospectrality for Orbifold Lens Spaces* — **published**: Canad. J. Math.
**72** (2020), no. 2, 281–325,
DOI [`10.4153/S0008414X19000178`](https://doi.org/10.4153/S0008414X19000178) (arXiv:1705.01412).
Read in full.

It fails to compete on three independent grounds, any one of which would suffice.

**(a) Opposite logical shape.** Their heat-coefficient result is Lemma 6.5 / Example 6.6
(dimension 3) and Lemma 6.7 / Example 6.8 (dimension 4). Verbatim:

> Then $O_1 = S^3/G_1$ and $O_2 = S^3/G_2$ will have the exact same asymptotic expansion of
> the heat kernel if $\alpha_1 = \alpha_2$ and $\beta_1 = \beta_2$.

That is a statement that heat coefficients **fail** to determine. The manuscript proves a
specified finite number of them **suffice** below a threshold.

**(b) Not a finite count at all.** The proof establishes the coincidence "for any $k$" — every
coefficient index. It is an all-order non-determinacy result, not a bounded count. So it is
not a finite-coefficient threshold in any direction.

**(c) Wrong curvature.** The setting is spherical space forms $S^{2n-1}/G$, constant curvature
$+1$, throughout — from the definitions in Lemma 2.1 onward. Nothing hyperbolic, no cone
surfaces.

And no minimality is claimed anywhere: the example $q = 195$ (the pair $L(195:3,5)$ vs
$L(195:6,35)$) is offered as "a tool to find examples", not as a smallest case.

**Forward citations, checked.** All five citing works remain in the spherical / rank-one
world — Mårdby–Rowlett's survey (arXiv:2406.18369), Lauret–Miatello–Rossetti
([`10.1007/s40863-019-00154-3`](https://doi.org/10.1007/s40863-019-00154-3)), Álzaga–Lauret
(arXiv:2409.02213), Lauret ([`10.2140/pjm.2021.314.333`](https://doi.org/10.2140/pjm.2021.314.333)
and [`10.1080/10586458.2018.1538908`](https://doi.org/10.1080/10586458.2018.1538908)). None
counts heat coefficients for hyperbolic cone orbifolds.

## 1.5 The competitor the manuscript already cites — Grieser–Maronna

Grieser & Maronna, *Hearing the shape of a triangle*, Notices AMS **60** (2013), 1440–1447,
DOI [`10.1090/noti1063`](https://doi.org/10.1090/noti1063), determine a Euclidean triangle
from **three invariants: area, perimeter, and the sum of the reciprocals of the angles.**

That is the same *shape* of result as Theorem C — a small fixed number of invariants,
including a reciprocal sum, determining a triangle-like object. The manuscript cites it (line
126) but only as generic background on finite determinacy, and the priority claim never
engages it.

It is not a counterexample: Grieser–Maronna is Euclidean, concerns a *smooth* triangle rather
than a cone orbifold, its invariants are geometric quantities rather than heat-trace
coefficients, and it proves no minimal degeneracy. So it does not falsify the sentence. But
the resemblance is close enough that a referee will notice, and the manuscript should say why
the two differ rather than leave it to be spotted.

## 1.6 The nearest-in-kind prior art sits in the manuscript's own central reference

DGGW's **Propositions 5.19 and 5.22** exhibit exactly the phenomenon of Theorem B — distinct
orbifolds that a low-order heat invariant fails to separate. Verbatim, Prop 5.19:

> $c$ distinguishes all but the following cases: $S^2$ from the orbifolds $O(*3,3,3)$ and
> $O(3,*3)$ (with $c = 4$), the good football $O(2,2)$ from $O(*2,3,6)$ (with $c = 5$), and
> the bad teardrop $O(2)$ from the orbifolds $O(*2,4,4)$ and $O(4,*2)$ (with $c = 4.5$).

Here $c=12\times$ the degree-zero coefficient, so these are **collisions in a single heat
invariant**, resolved only by the degree-$(-1/2)$ mirror-locus term. Proposition 5.22 adds
nonorientable pairs sharing an orientable double cover.

Three differences preserve the claim, and all three should be stated in the paper: DGGW's
examples are spherical and $\chi\ge0$, not hyperbolic; they are found rather than proved
minimal; and they concern one invariant rather than a threshold in a counted sequence. But
this is the closest thing in print to Theorem B, it is in the manuscript's most-cited source,
and §1.3 currently does not mention it. Leaving it unaddressed is the single most likely way
for a referee to conclude the author has not read DGGW carefully.

## 2. Uçar does not count coefficients

Uçar's determinacy statement is **Corollary 4.21, p. 139**, with **Corollary 4.23, p. 140**
the orientable specialization. Read directly from the thesis. The hypothesis is always
"$\kappa$ together with the spectrum" — the **full** spectrum. **No coefficient count appears
anywhere.** The manuscript's §1.3(a) characterization is accurate.

Nor does the pair $(2,8,8)/(3,3,12)$ appear anywhere in the thesis, and neither do the terms
"power sum", "collision", or "near-isospectral".

Uçar, PhD thesis, Humboldt-Universität zu Berlin, 2017,
DOI [`10.18452/18463`](https://doi.org/10.18452/18463), arXiv:1711.03405. No journal version
exists.

## 3. The strongest positive evidence — a specialist source says the problem was open

This is the most useful finding in the sweep for this question, and the manuscript does not
currently use it.

Doyle & Rossetti, *Laplace-isospectral hyperbolic 2-orbifolds are representation-equivalent*
(arXiv:1103.4372), prove — **Theorem 1**, verbatim:

> The Laplace spectrum of $M$ determines, and is determined by, the following data:
> 1. the volume; 2. the total length of the mirror boundary; 3. the number of conepoints of
> each order, counting a mirror corner as half a conepoint of the corresponding order;
> 4. the number of closed geodesics of each length and orientability class.

for compact hyperbolic 2-orbifolds, via the Selberg trace formula — a **full-spectrum**
result, not a finite-coefficient one. And they say so about the finite-coefficient question,
verbatim:

> Restricted to hyperbolic 2-orbifolds, the results [DGGW] state don't yield complete
> information about the singular set. All this information is there … presumably it could be
> extracted … by looking at **higher and higher terms** in the asymptotic expansion.

"Higher and higher" — unbounded, with no threshold, and explicitly conjectural
("presumably"). A specialist source, writing in 2011, describes exactly the gap the
manuscript closes. **Cite this.** It converts the priority claim from an assertion about the
absence of prior art into a claim that a named expert flagged as open.

**But this paper also requires a correction elsewhere.** Doyle–Rossetti prove qualitative
cone-order determinacy for the **hyperbolic** case in 2011 — six years before Uçar, and in
precisely the manuscript's own setting. §1.3(a) attributes that fact to Uçar alone. Widen it.
(Publication status: never published. The only citable identifier is the DataCite DOI
[`10.48550/arXiv.1103.4372`](https://doi.org/10.48550/arXiv.1103.4372).)

### And the attribution problem is older than that

**Dryden & Strohmaier**, *Huber's theorem for hyperbolic orbisurfaces*, Canad. Math. Bull.
**52** (2009), no. 1, 66–71,
DOI [`10.4153/CMB-2009-008-0`](https://doi.org/10.4153/CMB-2009-008-0) (arXiv:math/0504571) —
**Theorem 1.1**, verbatim:

> Let $\mathcal O$ be a compact orientable hyperbolic orbisurface. The Laplace spectrum of
> $\mathcal O$ determines its length spectrum and the **number of cone points of each possible
> order**. Knowledge of the length spectrum and the number of cone points of each order
> determines the Laplace spectrum.

That is **exact** determination of the cone-order data — no "up to finitely many" hedge — for
compact orientable hyperbolic orbisurfaces, in **2009**. Eight years before Uçar.

The manuscript already cites this paper, but describes it in §1.2 only as proving "a Huber
theorem relating the Laplace and length spectra of orbisurfaces". That undersells it
considerably: Theorem 1.1 also delivers the cone orders, which is the very fact §1.3(a)
credits to Uçar. Uçar's own Corollary 4.23 says as much — it is explicitly framed as
generalizing Dryden–Strohmaier from $\kappa=-1$ to all $\kappa\neq0$.

**So the chronology for qualitative cone-order determinacy in the hyperbolic case is:
Dryden–Strohmaier 2009 → Doyle–Rossetti 2011 → Uçar 2017 (generalizing to all constant
curvature).** §1.3(a) should say so. This costs the manuscript nothing — all three are
full-spectrum results, so none of them touches the finite-coefficient claim — but getting the
attribution wrong in a paper whose central contribution is a priority claim is exactly the
kind of thing that erodes a referee's confidence.

A useful consequence, worth stating in the paper. Because a hyperbolic $(p,q,r)$ triangle
orbifold has no moduli — its hyperbolic structure is rigid once $p,q,r$ are fixed —
Dryden–Strohmaier's Theorem 1.1 implies immediately that **no two non-isometric hyperbolic
triangle orbifolds are Laplace isospectral**. No source states this corollary explicitly (the
sweep found none), so it should be presented as an easy consequence of Theorem 1.1 rather than
claimed as new. It is the natural full-spectrum backdrop against which the manuscript's
finite-coefficient result is the sharpening.

## 4. Isospectral hyperbolic 2-orbifolds do exist — but not triangle orbifolds

This is the finding most likely to surprise, and it needs stating carefully because it cuts
both ways.

**Linowitz & Voight**, *Small isospectral and nonisometric orbifolds of dimension 2 and 3*,
Math. Z. **281** (2015), 523–569,
DOI [`10.1007/s00209-015-1500-1`](https://doi.org/10.1007/s00209-015-1500-1) (arXiv:1408.2001).
**Theorem A**, verbatim:

> The minimal area of an isospectral-nonisometric pair of 2-orbifolds associated to maximal
> arithmetic Fuchsian groups is $23\pi/6$, and this bound is achieved by exactly three pairs,
> up to isomorphism.

All three pairs are genuinely hyperbolic (quotients of $\mathbb H^2$ by arithmetic Fuchsian
groups), non-isometric, and isospectral. So **isospectral non-isometric hyperbolic
2-orbifolds are in print.**

**They are not triangle orbifolds.** Every one has signature $(0;2,2,2,2,2,3,4)$ — genus 0,
**seven** cone points. The manuscript's family is three cone points on a sphere. So these
pairs do not touch Theorem C, which concerns $\mathcal O(p,q,r)$. The constructions use
Vignéras' arithmetic method (quaternion-algebra unit groups), not Sunada's, and
non-isometry is proved via the Chinburg–Friedman selectivity criterion.

**No isospectral pair of hyperbolic *triangle* orbifolds was found in the literature**, and
none is expected: triangle orbifolds are rigid, with no moduli, and by Doyle–Rossetti's
Theorem 1 the spectrum determines the cone-order multiset outright, so an isospectral pair
would have to be isometric. That is consistent with — and is in fact implied by — the
manuscript's own Theorem C.

**Two cautionary precedents the manuscript should heed.**

First, Linowitz–Voight narrate a history of erroneous claims in exactly this area:
Maclachlan–Rosenberger (1994, Arch. Math. **62**) claimed a genus-0 signature-$(0;2,2,3,3)$
isospectral pair which Buser–Flach–Semmler later disproved on selectivity grounds.

Second, and closer to home: **Gordon & Rossetti**, *Boundary volume and length spectra of
Riemannian manifolds: what the middle degree Hodge spectrum doesn't reveal*, Ann. Inst.
Fourier **53** (2003), 2297–2314,
DOI [`10.5802/aif.2007`](https://doi.org/10.5802/aif.2007), required a **corrigendum
published nineteen years later** — Ann. Inst. Fourier **71** (2022), no. 6, 2647–2648,
DOI [`10.5802/aif.3470`](https://doi.org/10.5802/aif.3470). Carolyn Gordon is a DGGW
co-author and a first-tier referee candidate for this paper; Rossetti co-authored RSW 2008,
which the manuscript cites.

Taken with the DGGW erratum (`Q2-cone-coefficients.md` §5), that is *three* corrections in
this small literature, by exactly the authors most likely to referee this submission. Claims
about small isospectral or near-isospectral 2-orbifolds have a demonstrable track record of
needing repair. This is the strongest available argument for stating the results narrowly,
keeping the exact-arithmetic appendix, and preferring a statement of what is proved over a
priority claim.

## 5. The 2017–2026 competitor sweep

Nothing counting heat coefficients for orbisurfaces, triangle orbifolds, or cone surfaces was
found. What was found, and why each falls short:

Twelve arXiv API queries were run for this sweep, phrase-quoted and `AND`-joined:
`cat:math.SP AND all:"heat coefficients" AND all:orbifold` → 0;
`all:"cone surface" AND all:"heat trace"` → 0;
`all:"triangle orbifold" AND all:isospectral` → 0;
`all:"heat trace" AND all:orbifold AND all:determinacy` → 0;
`all:"heat invariants" AND all:orbifold AND all:cone` → 0;
`all:isospectral AND all:"triangle group" AND all:hyperbolic` → 0;
`cat:math.SP AND all:heat AND all:coefficients AND all:orbifold` → Bari–Hunsicker only;
`all:cone AND all:orbifold AND all:heat AND all:trace` → Schueth 2026 only;
`all:orbisurface AND all:heat` → Uçar and Schueth 2019 only;
`all:orbifold AND all:isospectral AND all:triangle` → 0;
`all:isospectral AND all:orbifold AND all:hyperbolic` → Bartel–Page arXiv:2407.07240;
`all:orbifold AND all:heat AND all:determinacy` → 0.

Every non-null hit is either a source the manuscript already cites or off-topic. Bartel–Page
(*Vignéras orbifolds*, 65 pp, 2024) is dimension-3 and number-theoretic; grepped in full, it
contains no triangle-orbifold, cone-surface-heat-trace, or heat-coefficient-counting content.

| Work | Record | Why not a competitor |
|---|---|---|
| Dryden, *Isospectral Finiteness of Hyperbolic Orbisurfaces* | arXiv:math/0411290 (never published separately) | Thm 4.5 determines cone orders only "up to finitely many possibilities"; Thm 5.1 is qualitative finiteness. Uses the full trace formula, not truncated heat asymptotics. |
| Dryden & Strohmaier | Canad. Math. Bull. **52** (2009), 66–71, [`10.4153/CMB-2009-008-0`](https://doi.org/10.4153/CMB-2009-008-0) | Exact cone-order determination — but from the **full** spectrum via wave-trace singular support, with no coefficient count. See above: the manuscript under-describes this result. |
| Richardson & Stanhope | Diff. Geom. Appl. **68** (2020), 101577, [`10.1016/j.difgeo.2019.101577`](https://doi.org/10.1016/j.difgeo.2019.101577) | Thm 4.7 is a parity argument establishing that *some* nonzero term distinguishes; qualitative, no count. |
| Gittins, Gordon, Membrillo Solis, Rossetti, Sandoval, Stanhope, Parts 1–2 | arXiv:2106.07882, arXiv:2311.00337 | Uses heat invariants of the $p$-spectrum to separate orbifolds from manifolds; codimension conditions, not coefficient counts. |
| Proctor & Stanhope | Diff. Geom. Appl. **28** (2010), 12–18, [`10.1016/j.difgeo.2009.03.015`](https://doi.org/10.1016/j.difgeo.2009.03.015) | Qualitative compactness/finiteness; no effective bound. |
| Lauret & Linowitz survey | New York J. Math. **30** (2024), 682–721 | Grepped directly: zero hits for "triangle", "heat coefficient", "heat invariant", "cone orbifold", "near-isospectral". |
| Mårdby & Rowlett, *112 years of listening to Riemannian manifolds* | arXiv:2406.18369 | General-audience survey; no competing result. |

The Lauret–Linowitz survey records as **open** the question of the smallest area of a pair of
arithmetic hyperbolic 2-orbifolds — evidence that this corner of the field is actively worked
and that fine-grained minimality questions are not considered settled.

## 5.5 The two negative results the manuscript cites but does not reconcile

The manuscript cites Shams–Stanhope–Webb, *One cannot hear orbifold isotropy type*, Arch.
Math. **87** (2006), 375–385,
DOI [`10.1007/s00013-006-1748-0`](https://doi.org/10.1007/s00013-006-1748-0), and
Rossetti–Schueth–Weilandt, *Isospectral orbifolds with different maximal isotropy orders*,
Ann. Global Anal. Geom. **34** (2008), 351–366,
DOI [`10.1007/s10455-008-9110-3`](https://doi.org/10.1007/s10455-008-9110-3), as background —
but never reconciles them with its own results, and they *look* like they cut against it.

They do not, and one sentence says why. Both construct isospectral orbifolds that differ in
**isotropy type / maximal isotropy order** — that is, the spectrum fails to determine the
*group-theoretic* structure of the singular set. The manuscript determines the **cone-order
multiset** of a hyperbolic orbisurface, which is a coarser and genuinely different invariant:
Doyle–Rossetti and Dryden–Strohmaier both show the full spectrum *does* fix it in this
setting. There is no tension — one can hear how many cone points of each order there are
without hearing the full isotropy data — but the paper should draw that line rather than leave
two prominent "one cannot hear …" titles sitting unexplained in its own related-work section.

This matters practically: **Dorothee Schueth is an RSW author and the source of the
manuscript's equation (4)** — she is among the most likely referees, and this is her own
result going unaddressed.

## 6. Verdict

**True on the evidence gathered — and it still needs narrowing; the recommended narrowing is
to delete it.** No competing exact finite-coefficient determinacy threshold for hyperbolic
cone orbifolds was found, and no explicit minimal degeneracy of the kind Theorem B provides
appears anywhere in the literature searched. The nearest competitor is a negative, all-order,
spherical result; the nearest hyperbolic results are full-spectrum and qualitative; and a
specialist source describes the finite-coefficient question as open. That is why the sentence
is true. It is not why it is worth making: it holds only on the conjunction of four
qualifiers, and the paper's result does not need it.

**Two accompanying edits**, both of which strengthen rather than concede:

1. **Add an explicit contrast with Bari–Hunsicker.** A referee who knows that paper — and
   Hunsicker is a plausible referee — will otherwise wonder why it is cited as the nearest
   neighbour without the difference being drawn. One sentence: their result is a
   non-sufficiency statement holding to all orders in the spherical setting; this one is a
   sufficiency threshold with a proved minimal failure in the hyperbolic setting.

2. **Widen §1.3(a) to include Doyle–Rossetti**, and cite their "higher and higher terms"
   remark in §1.3(b) as the statement of the gap being closed. This is the single
   highest-value edit available: it costs one sentence and converts an unsupported "to our
   knowledge" into a documented open problem.

**The deletion recommendation, reinforced on venue grounds.** None of the twelve
comparable JGA papers surveyed for Q5 claims priority — including
Dryden–Gordon–Moreno–Rowlett–Villegas-Blas (2025), which proves a finiteness theorem with
explicit bounds and states it flatly. The result here is sharp and stands on its own. "To our
knowledge this is the first…" is the sentence in the paper most exposed to a referee who
knows one more paper than the author does, and the sweep found several papers the manuscript
does not cite. Recasting it as a statement of what is proved, with the Doyle–Rossetti quote
establishing that the question was open, achieves everything the priority sentence was for
without the exposure.

---

## Bibliography corrections surfaced here

1. **Bari–Hunsicker is published** — Canad. J. Math. **72** (2020), no. 2, 281–325,
   [`10.4153/S0008414X19000178`](https://doi.org/10.4153/S0008414X19000178). Manuscript cites
   the 2017 preprint.
2. **Richardson–Stanhope is published** — Diff. Geom. Appl. **68** (2020), 101577,
   [`10.1016/j.difgeo.2019.101577`](https://doi.org/10.1016/j.difgeo.2019.101577). Manuscript
   cites the 2019 preprint.
3. **Proctor–Stanhope is published** — Diff. Geom. Appl. **28** (2010), no. 1, 12–18,
   [`10.1016/j.difgeo.2009.03.015`](https://doi.org/10.1016/j.difgeo.2009.03.015). Manuscript
   cites the 2009 preprint.
4. **Doyle–Rossetti (arXiv:1103.4372) is uncited** and should be added.
5. **Linowitz–Voight (Math. Z. 281 (2015) 523–569) is uncited** and is directly relevant to
   the manuscript's framing of what isospectrality can and cannot do for hyperbolic
   2-orbifolds.
6. **Gittins et al. Part 2** is labelled `gittinsetal2024` but dated 2023 in the entry text;
   Part 1 (arXiv:2106.07882) is uncited though referenced by Part 2's abstract.
