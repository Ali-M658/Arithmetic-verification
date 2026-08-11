# Verified findings ledger

Running consolidation of everything confirmed against primary sources. Each row is
traceable to a source read in full, not to a summary of one. This file is the evidence
base the deliverables draw on.

## Confirmed DOIs (all retrieved, none constructed)

| Work | Record | DOI |
|---|---|---|
| Dryden–Gordon–Greenwald–Webb 2008 | Michigan Math. J. **56** (2008), 205–238 | `10.1307/mmj/1213972406` |
| **DGGW Erratum** | Michigan Math. J. **66** (2017), 221–222 | `10.1307/mmj/1488510034` |
| Donnelly 1976 | Math. Ann. **224** (1976), 161–170 | `10.1007/BF01436198` |
| Schueth 2019 | Ann. Inst. Fourier **69** (2019), no. 7, 2827–2855 | `10.5802/aif.3338` |
| Schueth 2026 | Ann. Global Anal. Geom. **69** (2026), no. 1, Paper No. 2 | *pending* |
| Bari–Hunsicker | **Canad. J. Math. 72 (2020), no. 2, 281–325** | `10.4153/S0008414X19000178` |
| Nursultanov–Rowlett–Sher | Ann. Math. Québec (2024) | `10.1007/s40316-024-00237-4` |
| Elsholtz–Tao | J. Aust. Math. Soc. **94** (2013), 50–105 | `10.1017/S1446788712000468` |
| Elsholtz–Planitzer | Proc. Roy. Soc. Edinburgh A (2019) | `10.1017/prm.2018.137` |
| Luca–Pappalardi | Res. Number Theory (2019) | `10.1007/s40993-019-0172-z` |
| Huang–Vaughan I | J. Number Theory **131** (2011), 1641–1656 | `10.1016/j.jnt.2011.04.001` |
| Huang–Vaughan II | Acta Arith. **155** (2012) | `10.4064/aa155-3-5` |
| Bloom (density conjecture) | J. Eur. Math. Soc. | `10.4171/jems/1456` |
| Meyers–See (census-taker) | Math. Mag. **63** (1990), 86–88 | `10.1080/0025570X.1990.11977492` |
| Daudé–Kamran–Nicoleau | J. Geom. Anal. **31** (2019), 1821–1854 | `10.1007/s12220-019-00326-9` |

Plus the twelve JGA venue records in `jga-venue-set.md`, all Crossref-retrieved.

## Q2 — SETTLED

**Equation (4) is correct as printed.** Schueth Remark 4.2 gives
$a_1^{(\{\bar p\})}=[\frac1{360}(k^3-\frac1k)+\frac1{36}(k-\frac1k)]K(\bar p)$ — identical to the
manuscript under $m\leftrightarrow k$. Schueth's own closing sentence attributes it to
DGGW §5.6, exactly as the manuscript's footnote says.

**The attribution is also correct, and was independently checked at the source.** DGGW §5.6
("Example. Calculating heat invariants for 2-orbifolds") derives
$b_1(\gamma^j)=R_{1212}/(8\sin^4(j\pi/m))$ and, via the trigonometric sum
$\sum_{j=1}^{m-1}\sin^{-4}(j\pi/m)=(m^4+10m^2-11)/45$, reaches the per-point contribution
$R_{1212}(m^4+10m^2-11)/(360m)$ in equation (5.10). Expanding:
$(m^4+10m^2-11)/(360m) = m^3/360 + m/36 - 11/(360m) = \frac1{360}(m^3-\frac1m)+\frac1{36}(m-\frac1m)$.
**Schueth's form and DGGW's form are algebraically identical.** Two independent routes to the
same expression.

**$b_0$ confirmed at source.** DGGW Example 5.3, verbatim:
$b_0(\gamma^j)=|\det((I-A_{\gamma^j})^{-1})|=1/(2-2\cos(2j\pi/m))=1/(4\sin^2(j\pi/m))$.
With Lemma 5.4 ($\sum\sin^{-2}=\frac{m^2-1}{3}$) and division by isotropy order $m$ this gives
$\operatorname{cone}(m)=(m^2-1)/(12m)$ — the manuscript's Corollary 2.5, and its equation (5.7)
$\chi(\mathcal O)/6+\sum_i(m_i^2-1)/(12m_i)$ is the manuscript's equation (3) exactly.

**Equation (5) confirmed** — verified symbolically by the orchestrator; summing (4) at $K=-1$
returns $-\frac1{360}P_3-\frac1{36}S_1+\frac{11}{360}R$ as printed.

**No sign or factor discrepancy** between DGGW and Schueth. DGGW state their curvature sign
convention explicitly ($R_{abab}$ = sectional curvature), so $R_{1212}=K$ for a
constant-curvature surface including $K=-1$; Schueth simply writes $K(\bar p)$.

**Normalization confirmed.** DGGW Definition 4.7: a stratum $N$ carries
$(4\pi t)^{-\dim N/2}$; a cone point has $\dim N=0$, hence no prefactor. Schueth's
equation (17), $a_\ell^{(\{\bar p\})}=\frac1k\sum_{j=1}^{k-1}b_\ell(\Phi^j)$, carries the
$1/k$ isotropy average. Both match the manuscript's §1.2 convention.

### Higher $\ell$ — the extension question

- **DGGW stop at $\ell=1$.** A full-text search returns zero general-$\ell$ statements and
  nothing for $\ell\ge2$. Their Tables 1–2 never even evaluate the $t^1$ coefficient
  numerically. So DGGW alone cannot support the extension.
- **Schueth Theorem 4.1 gives $\ell=2$ in closed form:**
  $a_2^{(\{\bar p\})}=[\frac1{2520}(k^5-\frac1k)+\frac1{720}(k^3-\frac1k)+\frac1{180}(k-\frac1k)]K^2
  -[\frac1{15120}(k^5-\frac1k)+\frac1{1440}(k^3-\frac1k)+\frac1{180}(k-\frac1k)]\Delta_gK$.
  At constant curvature $\Delta_gK\equiv0$, killing the second bracket. At $K=-1$ the sum over
  cone points is $\frac1{2520}(P_5-R)+\frac1{720}(P_3-R)+\frac1{180}(S_1-R)$ —
  **so the fourth coefficient delivers $P_5$ with nonzero coefficient $1/2520$.**
- **Schueth Remark 5.4(ii) certifies all $\ell$:** Watson ($K=1$) and Uçar (arbitrary constant
  $K$) *"actually computed $c_\ell(\gamma)$ for every $\ell\in\mathbb N_0$"*, with
  $c_\ell(\gamma)=f_\ell(\gamma)K^\ell$ for rational functions $f_\ell$; and Remark 5.2 gives
  $c_\ell(\pi/k)=\frac12 a_\ell^{(\{\bar p\})}$.

- **Uçar's thesis, read firsthand, gives a uniform closed form for every $\ell$.** The
  operative equations are **(4.25) on p. 134 together with (4.33) on p. 137** — a finite
  Bernoulli-number sum, explicit for every $\ell\ge0$, not a degree bound.

  **Important nuance for the manuscript:** Uçar never writes
  "$b_\ell(C)=\kappa^\ell\frac1m p_\ell(m)$", and never uses the word *degree*. That form is
  the manuscript's own paraphrase. It is a faithful paraphrase of what (4.25)+(4.33) yield,
  but the manuscript should not attribute the *phrasing* to Uçar as if quoting him. Cite the
  equation numbers.

### The chain, evaluated and cross-validated

Evaluating Uçar (4.25)+(4.33) at $\ell=1,2,3$:

| $\ell$ | $p_\ell(m)$ | $\deg$ | leading coeff of $p_\ell$ | $b_\ell$ leading term | delivers |
|---|---|---|---|---|---|
| 1 | $\frac{m^4-1}{360}+\frac{m^2-1}{36}$ | 4 | $1/360$ | $\frac{1}{360}m^3K$ | $P_3$ |
| 2 | $\frac{2m^6+7m^4+28m^2-37}{5040}$ | 6 | $1/2520$ | $\frac{1}{2520}m^5K^2$ | $P_5$ |
| 3 | $\frac{3m^8+8m^6+14m^4+32m^2-57}{30240}$ | 8 | $1/10080$ | $\frac{1}{10080}m^7K^3$ | $P_7$ |

Degrees are $4,6,8=2\ell+2$ as expected, and $p_\ell(1)=0$ in every case — the sanity check
that a trivial cone contributes nothing.

**The $\ell=2$ row is independently cross-validated.** Uçar's $p_2$, converted via
$b_2=K^2\frac1m p_2(m)$, was compared symbolically against Schueth's Theorem 4.1 at constant
curvature. **The difference simplifies identically to zero.** Two independent sources,
derived by different methods (Uçar's Green-kernel-for-a-geodesic-wedge computation; Schueth's
Donnelly-style distance-function expansion), agree exactly. That is about as strong as
verification gets. $\ell=3$ rests on Uçar alone, since Schueth stops at $\ell=2$.

Summed over the cone points of a hyperbolic orbisurface at $K=-1$:

$$\textstyle\sum b_1=-\frac{P_3}{360}-\frac{S_1}{36}+\frac{11R}{360}$$
$$\textstyle\sum b_2=\frac{P_5}{2520}+\frac{P_3}{720}+\frac{S_1}{180}-\frac{37R}{5040}$$
$$\textstyle\sum b_3=-\frac{P_7}{10080}-\frac{P_5}{3780}-\frac{P_3}{2160}-\frac{S_1}{945}+\frac{19R}{10080}$$

The first line is the manuscript's equation (5) exactly. The next two extend it, and each
introduces its new power sum with a nonzero rational coefficient. So the invariant chain
$R \to S_1 \to P_3 \to P_5 \to P_7$ runs off established formulas.

**Verdict: the inputs for a $K\le n+1$ theorem are established. No new cone-coefficient
computation is required — and this is true well beyond $\ell=2$.** Uçar's formula is uniform
in $\ell$; the ceiling was Schueth's paper stopping at $\ell=2$, not Uçar's. The remaining
work is the algebraic independence of $(R,S_1,P_3,P_5,\dots)$ — the hedge in Remark 5.6 —
which is symmetric-function algebra, not analysis.

### The erratum — checked, and it does not bite

DGGW published an erratum, Michigan Math. J. 66 (2017) 221–222, `10.1307/mmj/1488510034`.
It corrects **only Theorem 5.1**, adding the hypothesis that $\mathrm{Iso}_{\max}(N)$ be
nontrivial (strata with trivial maximal isotropy do not appear in the heat invariants;
counterexample $\mathbb R^3$ mod the Klein four-group). It **does not touch §5.6, equations
(5.7)–(5.10), or any cone-point coefficient**. So the manuscript's quoted formula is
unaffected. Two things still follow:

1. The manuscript should cite the erratum alongside DGGW — a referee who knows the paper
   knows there is one.
2. A pleasing detail: the erratum credits *"a question from Naveed Bari"* — the Bari of
   Bari–Hunsicker. The manuscript's two most important sources are already in contact.

### Uçar's determinacy theorem (Q3 input)

**Corollary 4.21, p. 139** is the determinacy statement, with **Corollary 4.23, p. 140** the
orientable specialization — which generalizes Dryden–Strohmaier from $\kappa=-1$ to all
$\kappa\neq0$. Uçar flags parts (iii) and (iv) of 4.21 as new.

**No coefficient count appears anywhere.** The hypothesis is always "$\kappa$ together with
the spectrum" — the *full* spectrum. This is exactly what the manuscript's §1.3(a) says, and
it is correct. Nor does the pair $(2,8,8)/(3,3,12)$ appear anywhere in the thesis; neither do
the terms "power sum", "collision", or "near-isospectral". A *different* near-collision is
discussed on p. 141 — DGGW's three spherical Conway-notation pairs — resolved by mirror-locus
length, matching what the DGGW batch found independently.

**Publication status:** no journal version exists. The authoritative record is the Humboldt
dissertation, **DOI `10.18452/18463`**, URN `urn:nbn:de:kobv:11-110-18452`, dated 2017-10-17,
handle `https://edoc.hu-berlin.de/handle/18452/19142`. The manuscript cites only the arXiv
preprint; the Humboldt DOI is the citable record.

## Q3 — largely settled

Bari–Hunsicker is not a competitor, on three independent grounds: it is a *negative*
(insufficiency) result; the insufficiency is proved *"for any k"*, i.e. to all orders, so it
is not a finite count at all; and the setting is spherical space forms throughout, never
hyperbolic. No minimality is claimed — $q=195$ is offered as "a tool to find examples". All
five forward citations remain in the spherical/rank-one world.

**DGGW's spherical near-collisions confirmed verbatim** (the manuscript asserts these exist
and it is right) — Proposition 5.19: the invariant $c$ fails to distinguish $S^2$ from
$O(*3,3,3)$ and $O(3,*3)$ (all $c=4$); the good football $O(2,2)$ from $O(*2,3,6)$ ($c=5$);
the bad teardrop $O(2)$ from $O(*2,4,4)$ and $O(4,*2)$ ($c=4.5$). Proposition 5.22 adds
nonorientable pairs sharing an orientable double cover. These are separated only by the
degree $-1/2$ mirror-locus term.

Note what this means for framing: **DGGW's near-collisions are exactly the same phenomenon
as the manuscript's Theorem B** — low-order invariants failing to separate distinct
orbifolds — but in the spherical, $\chi\ge0$ regime and without a threshold or a minimality
proof. That is the honest comparison, and it makes the manuscript's contribution look
sharper, not weaker.

## Q1 — null result documented

No source in the Egyptian-fraction literature poses the equal-sum-and-equal-reciprocal-sum
problem. Checked against: the Bloom–Elsholtz 2022 survey (the current comprehensive survey of
the field), the Erdős–Straus counting papers, Eppstein's Egyptian-fractions hub, MathWorld,
Erdős Problem #242, and the census-taker lineage. The survey's own taxonomy —
single-representation counting, density/covering, restricted denominators — has no category
for "two representations sharing two symmetric-function values".

**Nearest neighbour is the census-taker problem**, not Erdős–Straus. Census-taker matches two
triples on $(e_3,e_1)$ — equal product and equal sum — with a uniqueness clause. The
manuscript matches on $(e_1, e_2/e_3)$ — equal sum and equal reciprocal sum. Same genre and
difficulty class, different pair of symmetric functions. That is the right comparison to draw
in §5, and the manuscript currently draws none.
Lineage: Kelly, Proc. AMS 15 (1964) 987–990; Meyers–See, Math. Mag. 63 (1990) 86–88
(`10.1080/0025570X.1990.11977492`); Garces–Loyola, arXiv:1204.2071.

**Asymptotic counting does not transfer off the shelf.** Elsholtz–Tao bound
$\sum_{p\le N}f(p)\asymp N\log^2N$ for the Erdős–Straus count; Elsholtz–Planitzer give
$O_\epsilon(n^{3/5+\epsilon})$; Luca–Pappalardi bound $\sum_{p\le x}A_3(p)$; Huang–Vaughan give
mean values for the binary case. All count representations of **one fixed value**. The
manuscript needs coincidences **between two independently varying values** additionally tied
by $e_1$ — a joint-distribution problem the existing machinery is not set up for.

**The birthday-paradox heuristic has no documented precedent in this literature.** It is
standard in analytic number theory broadly, but no fetched source instantiates it for
unit-fraction coincidences. The manuscript should not imply otherwise.

**OEIS: genuine null, and now properly controlled.** Both cumulative sequences return zero
hits. Two independent control tests establish the null is real rather than a tooling
artifact: (i) the numeric-search path was tested against Fibonacci and returned A000045;
(ii) the *keyword* path was tested against the structurally analogous known problem — a
search for "census-taker number" correctly surfaces **A334911**, "Numbers $k$ such that
exactly two unordered triples of positive numbers have product $k$ and equal sums"
(36, 40, 72, 96, 126, …), which cites Meyers–See and Garces–Loyola. Since the same search
method finds the equal-sum-and-equal-**product** problem, its silence on the
equal-sum-and-equal-**reciprocal-sum** problem is evidence of absence. The multiplicity of
$3/4$ as a sum of three unit fractions is not tabulated anywhere found.

### Guy's *Unsolved Problems in Number Theory* — and a correction to the brief

3rd ed., Springer 2004, `10.1007/978-0-387-26677-0`, xviii+438 pp. Section D (Diophantine
Equations) runs pp. 209–310. The full D1–D29 subsection list was recovered from the Deutsche
Nationalbibliothek deposited front matter, and the body text cross-checked.

- **D11 = Egyptian fractions (p. 252).** Entirely about representing *a single given
  fraction* as a sum of unit fractions: Rhind papyrus, Erdős–Straus $4/n$ (verified by Swett
  to $n\le1{,}003{,}162{,}753$), Sierpiński's $5/n$, Schinzel's $m/n$. **No pairs-of-triples
  framing anywhere in the section.**
- **D12 = Markoff numbers (p. 263).** *Not relevant to this manuscript at all.* The task
  brief named D11 and D12; D12 turns out to be a different subject entirely.
- **D16 = "Triples with the same sum and same product" (p. 271).** **This is the section the
  brief should have named.** Verbatim: *"The problem to find as many different triples of
  positive integers as possible with the same sum and the same product has been solved by
  Schinzel: you can have arbitrarily many."* Cites Vandemergel (13 triples, common sum
  17116); Mauldon, Amer. Math. Monthly Problem E2872 (1981) — smallest common sum 118 for
  four triples $(14,50,54),(15,40,63),(18,30,70),(21,25,72)$; Foster & Robins, Amer. Math.
  Monthly **89** (1982), 499–500; and **Schinzel, "Triples of positive integers with the same
  sum and the same product", Serdica Math. J. 22 (1996), 587–588**, whose construction uses
  points on the elliptic curve $y^2=x^3-9x+9$ (Cremona 324C1, rank 1).
- **D28 = "A reciprocal diophantine equation" (p. 309).**
- **No subsection among D1–D29 matches equal sum together with equal sum of reciprocals.**

**Why D16 matters more than the null result.** It is the same problem shape as the
manuscript's — two triples agreeing in two symmetric functions — for the pair $(e_1,e_3)$
instead of $(e_1,e_2/e_3)$. And it has been *solved*, by Schinzel, using an elliptic curve to
produce arbitrarily many triples with a common sum and product. The manuscript's Section 5
asks a structurally identical question and answers it with a scaling law plus a heuristic
conjecture. Schinzel's paper is the methodological template the manuscript should engage:
it is the closest thing in print to what §5 attempts, and its technique (rational points on
an elliptic curve of positive rank) is exactly the kind of tool that could turn the
manuscript's Conjecture 5.4 into a theorem, or at least sharpen the unconditional lower
bound past $\lfloor S/18\rfloor$.

### The triangle-group framing, checked

Takeuchi, "Arithmetic triangle groups", J. Math. Soc. Japan **29** (1977), no. 1, 91–106,
DOI `10.2969/jmsj/02910091` — read in full from the J-STAGE PDF. Theorem 3's complete list of
85 arithmetic triples **contains both $(2,8,8)$ and $(3,3,12)$**.

This is worth stating carefully, because it is suggestive but not prior art. Takeuchi's list
is determined by an arithmeticity criterion on the trace field
$k_0=\mathbb Q((\cos\frac\pi{e_1})^2,(\cos\frac\pi{e_2})^2,(\cos\frac\pi{e_3})^2,\cos\frac\pi{e_1}\cos\frac\pi{e_2}\cos\frac\pi{e_3})$
plus an embedding-positivity inequality — machinery logically independent of the
sum-of-reciprocals. So the co-appearance of $(2,8,8)$ and $(3,3,12)$ on that list is **not**
the manuscript's coincidence; it is two separately-arithmetic groups happening to sit in the
same 85-element list. The manuscript's coincidence is that they share $(S_1,R)$.

**Still open, and worth chasing:** whether $(2,8,8)$ and $(3,3,12)$ lie in the same
*commensurability class*. Equal $R$ means equal covolume by Gauss–Bonnet, which is a
necessary condition for commensurability, so the question is live. The classification is in
Takeuchi's companion paper, "Commensurability classes of arithmetic triangle groups",
J. Fac. Sci. Univ. Tokyo Sect. IA Math. **24** (1977), 201–212 — not retrieved (logged in
`outstanding-fetches.md`). If those two groups are commensurable, the pair may well appear in
that paper's tables, which would move Q1's verdict on the *specific pair* from "not in print"
to "in print, in different language".

## Q4 — the numerical-analysis half is settled

Every ingredient of the planned conditioning theorem is standard, and the standard version
is *sharper* than a bespoke argument would be.

**The technique chain, with citations at each link:**

1. **Power sums → coefficients → roots.** The first-order forward error for a simple root
   $z_k$ of $p(z)=\sum p_iz^i$ is, verbatim from Tisseur–Van Barel eq. (1.3)
   (arXiv:2001.05281, `10.48550/arXiv.2001.05281`),
   $\mathrm{err}(z_k)=|\Delta p(\hat z_k)|/(|z_k|\,|p'(\hat z_k)|)$, which with their
   elementwise backward bound (1.4b) gives exactly
   $|\delta z_k|\sim|\delta a_j|\,|z_k|^j/|p'(z_k)|$.

2. **The gap factor is $|p'|$.** For a monic cubic with roots $p,q,r$,
   $|p'(p)|=|(p-q)(p-r)|$. So the manuscript's Jacobian
   $\det DF=-3(p-q)(p-r)(q-r)(p+q)(p+r)(q+r)/(pqr)^2$ is the *standard* conditioning
   quantity, factored differently — not a new object. Tisseur–Van Barel's Table 1.1 makes
   the point concretely.

3. **Ostrowski / continuity of roots.** The citable modern lineage, via Ross
   (arXiv:2207.00123): Ostrowski, *Solution of Equations in Euclidean and Banach Spaces*,
   Academic Press 1973 (the English edition carrying the root-perturbation bounds from his
   1940 Acta Math. "Recherches sur la méthode de Graeffe"); Marden, *Geometry of
   Polynomials*, AMS Math. Surveys 3 (1966); Rahman–Schmeisser, *Analytic Theory of
   Polynomials*, Clarendon 2002. Note Ross proves only *qualitative* continuity — cite it
   for the lineage, not for a rate.

4. **Wilkinson.** The canonical primary reference is Wilkinson, "The evaluation of the zeros
   of ill-conditioned polynomials. Part I", Numer. Math. **1** (1959), 150–166,
   `10.1007/BF01386381` (Part II `10.1007/BF01386382`). Cite this rather than the 1963 book,
   which has no DOI — and the manuscript's brief requires resolvable citations.

5. **Vandermonde conditioning.** Gautschi–Inglese, Numer. Math. **52** (1987), 241–250,
   `10.1007/BF01398878`: $\kappa_\infty(V_K)\ge(K-1)2^K$ for real positive nodes,
   $\ge2^{K/2}$ for symmetric real nodes — exponential in $K$, and the manuscript's $p,q,r$
   are exactly the real-positive case. Pan (arXiv:1504.02118) sharpens this: Theorem 8.1
   gives an exponential lower bound explicitly in terms of a *separation parameter* between
   clustered and non-clustered knots.

6. **Vandermonde IS the Jacobian.** Two independent confirmations. Aubel–Bölcskei
   (arXiv:1701.02538, Appl. Comput. Harmon. Anal.) state it and record Moitra's large-sieve
   bound $\kappa(V_{N\times K})^2\le\frac{N-1+1/\delta}{N-1-1/\delta}$, with $\delta$ the
   minimum node separation — condition number diverging explicitly as $\delta\to0$.

**7. The best fit, and the one to actually use: Batenkov–Yomdin, "On the accuracy of solving
confluent Prony systems"** (arXiv:1106.1137, SIAM J. Appl. Math.). This is the manuscript's
problem in another vocabulary — recover node locations $\xi_i$ from noisy power moments
$\sum_i a_i\xi_i^k=m_k$:

- **Lemma 4.2** factors the Jacobian of the Prony map as
  $J_{P_S}(x)=U(\xi_1,\dots)\cdot\mathrm{diag}\{D_1,\dots,D_K\}$ with $U$ the *confluent
  Vandermonde matrix* — the explicit statement that the Vandermonde matrix is the Jacobian
  of the power-sum-to-parameters map.
- **Corollary 4.3:** $x$ is a critical point of the Prony map **iff two nodes collide** or a
  leading magnitude vanishes. This is *structurally identical* to the manuscript's Jacobian
  vanishing exactly on $p=q$, $p=r$, $q=r$. The manuscript has rediscovered, in a special
  case, a known structural fact about moment inversion.
- **Theorem 4.5** gives the local accuracy
  $\mathrm{ACC_{LOC}}(x,\epsilon,\xi_i)=C_1\epsilon/|a_{i,l_i-1}|$, where $C_1$ depends on
  the node configuration through $\|U^*\|_\infty$ and scales "roughly of the same order as
  some finite power of $\prod_{i<j}|\xi_j-\xi_i|^{-1}$" — i.e. **exactly the
  pairwise-gap blow-up the manuscript wants**, already proved, and shown in §5.A to match
  the Cramér–Rao bound.

**Consequence for the verdict.** The *technique* is not novel and should not be presented as
such: the right move is to cite Batenkov–Yomdin and Moitra and specialize, which is both
honest and stronger, since it inherits sharp constants. What is genuinely the manuscript's
own is (a) the *setting* — an inverse spectral problem on an orbifold — and (b) the
**integer twist**: because $p,q,r$ are positive integers, an error bound below half the
minimum gap yields *exact* recovery, converting a conditioning estimate into a
determinacy-from-noisy-data theorem. That is the part worth writing.

## Bibliography corrections for the manuscript (running)

1. Bari–Hunsicker is **published**: Canad. J. Math. 72 (2020) 281–325,
   `10.4153/S0008414X19000178`. Manuscript cites the 2017 preprint only.
2. Schueth "curved conical singularities" is **published**: Ann. Global Anal. Geom. 69 (2026),
   no. 1, Paper No. 2. Manuscript cites it as a 2025 preprint.
3. **The DGGW erratum is uncited** — Michigan Math. J. 66 (2017) 221–222,
   `10.1307/mmj/1488510034`.
4. Doyle–Rossetti 2011 (arXiv:1103.4372) appears uncited — pending confirmation of what it
   proves.
5. Gittins et al. is labelled `gittinsetal2024` but dated 2023 in the entry text — internal
   inconsistency.
