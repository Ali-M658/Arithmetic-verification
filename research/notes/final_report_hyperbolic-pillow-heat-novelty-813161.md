# What is new in *How Few Heat Invariants Determine a Hyperbolic Triangular Pillow*

A literature sweep of the manuscript's novelty claims, its load-bearing citations, and its
venue fit. Deliverable copies of each section live in `review/hyperresearch/`; this document
is the integrated argument.

**The one-paragraph answer.** The paper's mathematics is sound — every displayed equation was
independently re-derived and checks out. Its central novelty claims survive, and the strongest
evidence for them is a sentence in an uncited paper that the manuscript should be quoting. Its
principal exposure is not mathematical but bibliographic: five works cited as preprints are
published, an erratum to its most important source goes unmentioned, and the attribution chain
for one qualitative fact is off by eight years. Its principal missed opportunity is that the
extension it treats as future work is available now, from formulas already in print.

---

## 1. Novelty of the Diophantine problem

Section 5 asks when two distinct triples of integers share both their sum and their sum of
reciprocals. **This problem is not in the literature.**

The negative is well controlled, which matters more than its breadth. Guy's *Unsolved Problems
in Number Theory* (3rd ed., [`10.1007/978-0-387-26677-0`](https://doi.org/10.1007/978-0-387-26677-0))
was grepped in full: zero occurrences of `2,8,8`, `3,3,12`, `triangle group`, `orbifold`,
`covolume` or `Takeuchi`. OEIS returns nothing for either cumulative count sequence, for the
per-$S$ sequence, or for the raw digits — and, critically, the same search method *does* return
[A334911](https://oeis.org/A334911) for the structurally analogous equal-sum-equal-**product**
problem. A method that finds the neighbour and not the target is evidence of absence rather
than a tooling artifact.

The brief pointed at Guy's §D11 and §D12. Neither is right: D11 is Egyptian fractions in the
single-representation sense, and **D12 is Markoff numbers**. The section that matters is
**D16, "Triples with the same sum and same product"**, and it changes how §5 should read.
Guy records that Schinzel *solved* D16 — arbitrarily many triples with a common sum and
product — using rational points on the elliptic curve $y^2 = x^3 - 9x + 9$. So the manuscript's
problem is the same shape for the pair $(e_1, e_2/e_3)$ that D16 treats for $(e_1, e_3)$, and
the neighbouring problem has a genuinely arithmetic solution where §5 currently offers a
scaling law and a heuristic. That is simultaneously the best evidence §5's problem is new and
the most promising route to improving it.

The alternative framing — equal $R$ means equal covolume, so this is two hyperbolic triangle
groups of equal covolume — was checked too. Both $(2,8,8)$ and $(3,3,12)$ sit on Takeuchi's
list of 85 arithmetic triangle groups ([`10.2969/jmsj/02910091`](https://doi.org/10.2969/jmsj/02910091),
read in full, and independently reconfirmed against arXiv:1510.04637). But they are there for
arithmeticity reasons with no bearing on the reciprocal sum, and nothing remarks on their
shared covolume. One thread stays open: Takeuchi's 85 triples fall into 19 commensurability
classes, and that assignment lives in a companion paper we could not retrieve. Even a positive
answer would not make Theorem B prior art — commensurable groups have covolumes in *rational*
ratio, not equal ratio — but it would need citing.

Existing asymptotic machinery does not transfer. Elsholtz–Tao, Elsholtz–Planitzer,
Luca–Pappalardi and Huang–Vaughan all count representations of a *single fixed* value; §5 needs
coincidences between two independently varying values tied by $e_1$. And §5.3's description of
its heuristic as "of the birthday-paradox type standard in analogous Diophantine settings"
overstates: no source in this literature instantiates such an argument. Soften it or cite an
instance.

*Verified independently:* Table 5.1's counts reproduce exactly (1, 92, 386, 840, 1496, 2210,
3067), as does the $S=36$ structure.

## 2. The third coefficient and the higher cone coefficients

**Equation (4) is correct as printed, and its attribution is correct.**

Schueth's Remark 4.2 gives $a_1^{(\{\bar p\})} = [\frac{1}{360}(k^3-\frac1k)+\frac{1}{36}(k-\frac1k)]K(\bar p)$
and closes by noting these formulas "were already computed in [8], 5.6" — DGGW. Both halves of
the manuscript's footnote check out. Better, the same expression was reached independently from
DGGW's own §5.6, which derives the per-cone contribution $R_{1212}(m^4+10m^2-11)/(360m)$; that
expands term-for-term to equation (4). Two routes, one formula. $b_0$, the $1/m$ isotropy
average, the absent $(4\pi t)^{-1}$ prefactor on a zero-dimensional stratum, and equation (5)
all check out, and no sign or factor convention differs between the sources.

**The extension is far cheaper than the manuscript assumes.** This is the most consequential
finding in the sweep.

DGGW stop at $\ell=1$ — a full-text search finds no general-$\ell$ statement. But Schueth's
**Theorem 4.1** gives $\ell=2$ in closed form, and at constant curvature the entire $\Delta_gK$
bracket vanishes, leaving a clean $K^2$ term whose sum over cone points delivers
$P_5 = \sum m_i^5$ with coefficient $1/2520$. And Schueth's **Remark 5.4(ii)** records that
Watson and Uçar "actually computed $c_\ell(\gamma)$ for **every** $\ell \in \mathbb N_0$" at
constant curvature. Reading Uçar's thesis directly confirms it: equations (4.25) p. 134 and
(4.33) p. 137 are a Bernoulli-number closed form, uniform in $\ell$ — not the degree bound the
brief anticipated.

Evaluated, the chain runs $R \to S_1 \to P_3 \to P_5 \to P_7$, with
$p_2(m)=\frac{2m^6+7m^4+28m^2-37}{5040}$ and $p_3(m)=\frac{3m^8+8m^6+14m^4+32m^2-57}{30240}$.
The $\ell=2$ case is cross-validated: Uçar's form and Schueth's Theorem 4.1 differ by exactly
zero, symbolically — two authors, two methods, one answer.

The leading coefficient is known in closed form too — $|B_{2\ell+2}|/(2(\ell+1)!(2\ell+1))$,
matching $\tfrac1{12},\tfrac1{360},\tfrac1{2520},\tfrac1{10080}$ at $\ell=0,1,2,3$ — and by
von Staudt–Clausen it never vanishes, so $b_\ell$ delivers $P_{2\ell+1}$ with nonzero weight at
*every* order. That is a mechanism, not a pattern, which is what a general-$n$ argument needs.

**So a $K \le n+1$ theorem needs no new cone-coefficient computation.** What it still needs is
the injectivity argument behind Remark 5.6's "when these are independent" — and that is a
much cheaper obligation than heat-kernel work. Part of it is already done: an exact enumeration
found that $\mathcal O(3,10,15,30)$ and $\mathcal O(4,5,21,28)$ are hyperbolic 4-cone pillows
with distinct cone-order multisets sharing $S_1 = 58$, $R = 8/15$ and $P_3 = 31402$ — their
first three heat coefficients — separated only by $P_5$. Over orders $\le55$ (395,009
multisets) it is the only such collision; $\le60$ (557,844) adds only its doubling. So **four
coefficients determine the cone-order multiset of a 4-cone pillow and three do not.**

That phrasing is deliberate, and it exposes a defect the manuscript must repair regardless.
$K(F)$ is defined up to *isometry*. For $n=3$ that is harmless — triangle orbifolds are rigid,
so the multiset is the isometry class. For $n\ge4$ it is not: a sphere with $n$ cone points of
fixed orders has a $(2n-6)$-dimensional Teichmüller space, and since every heat coefficient
depends only on the orders, that entire family shares *all* of them. **$K(F)$ is therefore
infinite for $n\ge4$**, and Remark 5.6's "the upper bound $K\le n$ extends the $n=3$ case of
Theorem C" does not hold in the isometry sense Theorem C uses. Restate the $n\ge4$ claim as
multiset determinacy and note that rigidity is exactly what makes $n=3$ special — which is the
paper's own subject.

Two corrections. Uçar never writes the $\kappa^\ell\frac1m p_\ell(m)$ form nor the word
"degree" — cite his equations, not a paraphrase. And there is an uncited **DGGW erratum**
([`10.1307/mmj/1488510034`](https://doi.org/10.1307/mmj/1488510034)); it was read in full and
corrects only Theorem 5.1, leaving §5.6 and equation (4) untouched, but it exists. Pleasingly,
it opens by thanking "Naveed Bari" — the manuscript's two most important sources are already
in conversation.

## 3. The priority claim

**It is true, but it should go.** The designated closest competitor is not one, on three
independent grounds: Bari–Hunsicker prove heat coefficients *insufficient* rather than
sufficient; the insufficiency holds "for any $k$", so it is an all-order statement rather than
a finite count; and the setting is spherical space forms throughout. No minimality is claimed
anywhere. All five forward citations remain in the spherical world, and a twelve-query arXiv
sweep found no independent competitor.

But the sentence survives only on four qualifiers holding at once — *exact*,
*finite-coefficient*, *hyperbolic cone orbifold*, *minimal* — and dropping any one brings
something into range. Drop *hyperbolic* and Grieser–Maronna determines a Euclidean triangle
from three invariants, one of them a sum of reciprocals: the same shape as Theorem C, cited by
the manuscript and never engaged. Drop *minimal* too and DGGW's own Propositions 5.19 and 5.22
exhibit distinct orbifolds that a *single* heat invariant fails to separate — the Theorem B
phenomenon, unremarked in the manuscript's most-cited source. Drop *finite-coefficient* and
Dryden–Strohmaier and Doyle–Rossetti are already there.

None is a counterexample; all three are things a referee will raise. A claim true only on a
four-fold conjunction, in a paper that does not need it, is a bad trade.

**The strongest evidence is positive, and the manuscript is not using it.** Doyle and Rossetti,
writing in 2011, say of exactly this question:

> Restricted to hyperbolic 2-orbifolds, the results [DGGW] state don't yield complete
> information about the singular set. All this information is there … presumably it could be
> extracted … by looking at **higher and higher terms** in the asymptotic expansion.

Unbounded, conjectural, no threshold. A specialist source stating the gap the manuscript
closes. That is worth more than any "to our knowledge" formulation.

But the same finding forces a correction. §1.3(a) credits Uçar alone with qualitative
cone-order determinacy. **Dryden–Strohmaier's Theorem 1.1 (2009)** already gives it exactly —
"the number of cone points of each possible order" — for compact orientable hyperbolic
orbisurfaces; Doyle–Rossetti follow in 2011; Uçar's Corollary 4.23 is explicitly a
generalization of Dryden–Strohmaier. The manuscript cites Dryden–Strohmaier, but describes it
only as a Huber theorem about length spectra, which undersells it. None of this touches the
finite-coefficient claim, but in a paper whose contribution *is* a priority claim, a
mis-ordered attribution chain is corrosive.

Two pieces of context the manuscript should absorb. Isospectral non-isometric *hyperbolic*
2-orbifolds do exist in print — Linowitz–Voight's three pairs of minimal area $23\pi/6$
([`10.1007/s00209-015-1500-1`](https://doi.org/10.1007/s00209-015-1500-1)) — though with seven
cone points, not three, so Theorem C is untouched. And that same paper narrates a history of
*false* claims in this area, including one disproved a decade later. Claims about small
isospectral hyperbolic 2-orbifolds have a poor track record; state results narrowly and keep
the exact-arithmetic appendix.

A last suggestion, on venue grounds rather than correctness: none of the twelve comparable JGA
papers claims priority, including one proving a finiteness theorem with explicit bounds. The
Doyle–Rossetti quotation accomplishes what the priority sentence was for, with less exposure.

## 4. The planned stability theorem

**Novel in setting, not in technique** — and the two need separating explicitly, because a
referee will separate them.

The technique is standard, and the reason is sharper than "the methods are similar": **the
manuscript's invariant map is a Prony system.** With nodes $x_i := m_i^2$ and weights
$a_i := 1/m_i$, the $j$-th moment $\sum_i a_i x_i^{\,j}$ is $R, S_1, P_3, P_5, P_7$ for
$j = 0,\dots,4$ — the entire hierarchy of Corollary D and its extension, in one system, with
the $\ell$-th cone coefficient supplying the $(\ell+1)$-th moment. All five verified
symbolically.

That identification explains the Jacobian completely, including the factors that plain
root-conditioning leaves unaccounted for:
$\det DF = -3\,\mathrm{Vandermonde}(p^2,q^2,r^2)/(pqr)^2$ — the $(p+q)(p+r)(q+r)$ are just
what completes each $(m_i-m_j)$ into $(m_i^2-m_j^2)$. Since the orders are positive, the
diagonals **are** the node-collision locus.

So Batenkov–Yomdin applies directly rather than by analogy: their Lemma 4.2 gives exactly this
Vandermonde × diagonal factorisation, Corollary 4.3 identifies the critical points as node
collisions, and Theorem 4.5 supplies accuracy scaling as a power of
$\prod_{i<j}|\xi_j-\xi_i|^{-1}$, matching the Cramér–Rao bound. Presenting the conditioning
analysis as new invites an easy objection; stating the identification and citing the theory is
both honest and stronger.

It also pays a dividend in §2: Remark 5.6's "when these are independent" hedge becomes "does
an $n$-node Prony system with $n$ moments determine its nodes?", whose non-degeneracy
condition is just distinctness of the orders.

The setting is another matter. Eight documented arXiv queries return nothing: no stability
theorem exists for recovering a finite discrete invariant of an orbifold from approximate
spectral data. The one orbifold-setting precedent, Lassas–Lu–Yamaguchi, reconstructs a
*continuous metric* from interior eigenfunction data with a triple-logarithmic modulus — a
different species. Across all of inverse spectral geometry no Lipschitz or Hölder estimate
exists; log-type is the good case.

So: cite the machinery, then add the part that is genuinely yours. Because $p,q,r$ are
*integers*, an error below half the minimum gap gives **exact** recovery. That converts a
conditioning bound into a determinacy-from-noisy-data theorem — there is an explicit
$\epsilon(p,q,r)$ within which spectral data pins the cone orders exactly — with the diagonal
blow-up appearing as the degradation of $\epsilon$. Say why an algebraic modulus is possible
where the field's best is logarithmic: the invariant is finite and discrete, not a metric.
Otherwise the strength reads as an overclaim.

## 5. Venue calibration

JGA in this area publishes substantial papers (26–58 pp) that favour exact results over
asymptotic ones and use computation to certify a structural theorem rather than to constitute
one. The manuscript's architecture already matches: interval-separation proof in the body,
exhaustive enumeration in an appendix as corroboration.

The exemplar is Dryden, Gordon, Moreno, Rowlett and Villegas-Blas (2025,
[`10.1007/s12220-025-01922-8`](https://doi.org/10.1007/s12220-025-01922-8)) — spectral
finiteness for convex polygons *with explicit upper bounds*, two of whose authors wrote DGGW.
Venue precedent, referee signal and model of tone in one paper. Daudé–Kamran–Nicoleau
([`10.1007/s12220-019-00326-9`](https://doi.org/10.1007/s12220-019-00326-9)) establishes that
the journal takes inverse-spectral stability work, which matters for the planned section.

Plausible referees, each with a recent supporting publication: Dryden, Gordon, Schueth,
Rowlett, Stanhope; then Rossetti, Sher, Hunsicker, Lauret, and the Farsi–Proctor–Seaton group.
Note the conflict clusters — Dryden, Gordon and Rowlett co-authored the exemplar; Schueth and
Uçar are both at Humboldt.

## 6. Verdict

1. **Is §5's Diophantine problem new?** Yes, on the evidence gathered — with one retrieval
   (Takeuchi's commensurability classes) still open. Engage Guy D16 and Schinzel.
2. **Is the quoted $b_1$ correct?** Yes, exactly as printed, with a correct attribution.
3. **Are the higher $b_\ell$ established?** Yes, at every $\ell$, with the leading coefficient
   in closed form. No new cone-coefficient computation needed; the injectivity argument is
   still owed. Remark 5.6 is settled for $n=4$ — as multiset determinacy, and the remark's
   isometry framing needs repair.
4. **Does the priority claim survive?** It is true, but it rests on four simultaneous
   qualifiers. Replace it with what is proved plus the Doyle–Rossetti quotation.
5. **Is the stability theorem novel?** In setting, not technique. The invariant map *is* a
   Prony system; cite the theory and make the integer-exactness the theorem.
6. **What must the paper look like?** Largely what it already is — plus a repaired
   bibliography, the $n$-cone extension, and no priority sentence.

## 7. Outstanding

Two sources could not be retrieved: Takeuchi's commensurability-classes paper (the one place
$(2,8,8)$ and $(3,3,12)$ might already appear together) and Watson's spherical-polygon paper
(redundant, since Uçar was read directly). Two identifier discrepancies are flagged rather than
resolved: Hezari–Zelditch's volume/year, and a page range for Doyle–Rossetti 2008. MathSciNet
was unavailable; every citation was resolved without it. Full detail in
`review/outstanding-fetches.md`.

**Fifteen corrections and opportunities** are itemised in `review/hyperresearch/VERDICT.md`.
Six are bibliographic, three substantive, two matters of precision, two opportunities, and
none is a mathematical error: equations (3), (4), (5), (9), the Jacobian, the cotangent and
cosecant identities, Table 5.1 and the $S=36$ structure were all re-derived or recomputed
independently and all hold.
