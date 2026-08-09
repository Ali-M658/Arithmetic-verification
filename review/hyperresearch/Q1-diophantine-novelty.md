# Q1 — Novelty of the Section 5 Diophantine problem

**Verdict: NEW.** The problem of pairs of triples with equal sum *and* equal sum of
reciprocals does not appear in the Egyptian-fraction literature, in Guy's *Unsolved Problems
in Number Theory*, or in OEIS. But it sits one square away from a problem that is
well-studied and, in a strong sense, *solved* — and the manuscript does not currently
acknowledge that neighbour. Engaging it would strengthen §5 considerably.

---

## 1. The problem, stated for search

Two distinct multisets $\{p,q,r\}$, $\{p',q',r'\}$ of integers $\ge2$ with

$$p+q+r=p'+q'+r'\qquad\text{and}\qquad \tfrac1p+\tfrac1q+\tfrac1r=\tfrac1{p'}+\tfrac1{q'}+\tfrac1{r'}.$$

Equivalently: two three-term Egyptian-fraction representations of a common value with equal
denominator sum. Smallest instance $2+8+8=3+3+12=18$ with
$\tfrac12+\tfrac18+\tfrac18=\tfrac13+\tfrac13+\tfrac1{12}=\tfrac34$.

In symmetric-function terms the two triples share $e_1$ and the ratio $e_2/e_3$. That
reformulation matters: it is what makes the census-taker and Guy D16 problems the right
neighbours to search, rather than the Erdős–Straus circle.

## 2. The searches, and what they returned

### Guy, *Unsolved Problems in Number Theory* — exhaustive, negative

3rd ed., Springer 2004, DOI [`10.1007/978-0-387-26677-0`](https://doi.org/10.1007/978-0-387-26677-0),
xviii+438 pp. Section D (Diophantine Equations), pp. 209–310. The subsection-level table of
contents (D1–D29 with page numbers) was recovered from the Deutsche Nationalbibliothek's
deposited front matter; the body text was then grepped in full.

| Section | Title | Page | Relevant? |
|---|---|---|---|
| **D11** | Egyptian fractions | 252 | Only tangentially — see below |
| **D12** | Markoff numbers | 263 | **No** — unrelated subject |
| **D16** | Triples with the same sum and same product | 271 | **Yes — the closest relative** |
| **D28** | A reciprocal diophantine equation | 309 | No |

**A correction to the brief.** The task named D11 and D12. D12 is Markoff numbers and has
nothing to do with this. The section that matters is **D16**.

**§D11** is entirely about representing *a single given fraction* as a sum of unit fractions:
the Rhind papyrus, the Erdős–Straus conjecture $4/n=1/x+1/y+1/z$ (verified by Swett to
$n\le1{,}003{,}162{,}753$), Sierpiński's $5/n$, Schinzel's $m/n$. No pairs-of-triples framing
appears anywhere in it.

A full-book search of the 3rd edition returned **zero hits** for `2,8,8`, `3,3,12`,
`triangle group`, `orbifold`, `covolume`, and `Takeuchi`.

### OEIS — negative, with a working control

All searches used a browser User-Agent with ≥5 s spacing (OEIS 403s on rapid unheadered
requests). Queries run and their results:

| Query | Result |
|---|---|
| `92, 386, 840, 1496, 2210, 3067` (cumulative pairs) | no match |
| `386, 840, 1496, 2210` (truncated) | no match |
| `92, 380, 822, 1468, 2158, 2977` (cumulative classes) | no match |
| per-$S$ sequence from $S=18$: `1,0,1,0,0,0,0,0,1,0,0,0,0,1,1,0,1,1,2,…` | no match |
| sums admitting a degeneracy: `18,20,26,31,32,34,35,36,37,38,39,40,42,43,45` | no match |
| `2,8,8,3,3,12` (raw digits) | no match |
| "equal sum equal sum of reciprocals" | noise only |
| "hyperbolic triangle group covolume" | noise only |
| "orbifold Euler characteristic triples" | noise only |
| **control: "census-taker number"** | **A334911 — correctly returned** |

The control is what makes the null admissible. Searching for the structurally analogous
*known* problem — equal sum and equal **product** — correctly surfaces
[A334911](https://oeis.org/A334911), "Numbers $k$ such that exactly two unordered triples of
positive numbers have product $k$ and equal sums" (36, 40, 72, 96, 126, …), which cites
Meyers–See and Garces–Loyola. The method demonstrably works on a problem of this shape. Its
silence on our problem is therefore evidence of absence rather than a tooling artifact.

A separate control confirmed the numeric-search path: querying Fibonacci returned A000045.

### The research literature — negative

Checked against the Bloom–Elsholtz survey (arXiv:2210.04496, the current comprehensive survey
of the field), the Erdős–Straus solution-counting papers, Eppstein's Egyptian-fractions hub,
MathWorld, and [Erdős Problem #242](https://www.erdosproblems.com/242). The survey's own
organizing taxonomy — single-representation counting, density and covering, restricted
denominators — contains no category for "two representations sharing two symmetric-function
values".

## 3. The nearest relatives, precisely distinguished

| Problem | Matches on | How it differs |
|---|---|---|
| **Erdős–Straus** $4/n=\frac1x+\frac1y+\frac1z$ | — | Existence of a *single* representation of one fixed rational. No second triple, no sum condition. Erdős Problem #242. |
| Counting representations of a fixed rational as $k$ unit fractions | — | One value, one triple; a multiplicity count. Ours is a *coincidence between two independently varying values*. |
| "Equal sums of unit fractions", no sum condition | value only | Drops the $e_1$ condition, which is the whole difficulty. |
| **Guy D16 / census-taker** | $(e_1,e_3)$ | **Same shape, different pair of symmetric functions.** |
| **This paper's §5** | $(e_1,e_2/e_3)$ | — |

**The closest relative is Guy D16, not Erdős–Straus.** This is the finding that matters most
for §5, and it is worth quoting Guy verbatim:

> The problem to find as many different triples of positive integers as possible with the
> same sum and the same product has been solved by Schinzel: you can have arbitrarily many.

Guy's citations there: Vandemergel (13 triples with common sum 17116); Mauldon, *Amer. Math.
Monthly* Problem E2872 (1981) — smallest common sum 118, for the four triples
$(14,50,54),(15,40,63),(18,30,70),(21,25,72)$; Foster & Robins, *Amer. Math. Monthly* **89**
(1982), 499–500; and **A. Schinzel, "Triples of positive integers with the same sum and the
same product", Serdica Math. J. 22 (1996), 587–588**, whose construction uses rational points
on the elliptic curve $y^2=x^3-9x+9$ (Cremona 324C1, rank 1).

The recreational lineage of the same problem — with an added uniqueness clause — is the
census-taker problem: Kelly, *Partitions with equal products*, Proc. AMS **15** (1964),
987–990; Meyers & See, *Math. Magazine* **63** (1990), 86–88,
DOI [`10.1080/0025570X.1990.11977492`](https://doi.org/10.1080/0025570X.1990.11977492);
Garces & Loyola, arXiv:1204.2071. The smallest census-taker number is 36, from
$\{9,2,2\}$ and $\{6,6,1\}$ with common sum 13.

## 4. The triangle-group framing — checked, and it does not pre-empt

Since $R$ determines the area by Gauss–Bonnet, equal $R$ means **equal covolume**. So the
coincidence can be read as: two hyperbolic triangle groups of equal covolume whose cone orders
also have equal sum. That framing has its own literature, and it was searched.

Takeuchi, *Arithmetic triangle groups*, J. Math. Soc. Japan **29** (1977), no. 1, 91–106,
DOI [`10.2969/jmsj/02910091`](https://doi.org/10.2969/jmsj/02910091) — read in full. Theorem
3's list of 85 arithmetic triples **contains both $(2,8,8)$ and $(3,3,12)$**. This was
independently confirmed against the recomputed list of 76 compact 1-arithmetic triples in
arXiv:1510.04637, which states it "agrees with that of Takeuchi, thus verifying his results".

**But this is not prior art.** Takeuchi's list is generated by an arithmeticity criterion on
the trace field together with an embedding-positivity inequality — machinery logically
independent of the sum of reciprocals. The two triples appear on that list for unrelated
reasons, and nothing in either source remarks on their equal covolume, let alone their equal
cone-order sum.

**One genuinely open thread.** Takeuchi's 85 triples fall into 19 commensurability classes,
but the class assignment is in a companion paper — *Commensurability classes of arithmetic
triangle groups*, J. Fac. Sci. Univ. Tokyo Sect. IA Math. **24** (1977), 201–212 — which could
not be retrieved (see `review/outstanding-fetches.md`). If $(2,8,8)$ and $(3,3,12)$ turn out
to lie in the same class, the pair may have an unremarked prior appearance there. Note the
caveat: commensurable Fuchsian groups have covolumes in *rational ratio*, not equal ratio, so
equal covolume is a sharper coincidence than commensurability and is not implied by it. Even a
positive answer would not make Theorem B prior art — but it would need citing.

## 5. Is an asymptotic count known, or provable by standard methods?

**Not known.** And the existing machinery does not transfer off the shelf.

The state of the art for three-term unit-fraction equations:

- **Elsholtz & Tao**, J. Aust. Math. Soc. **94** (2013), 50–105,
  DOI [`10.1017/S1446788712000468`](https://doi.org/10.1017/S1446788712000468):
  $N\log^2N\ll\sum_{p\le N}f(p)\ll N\log^2N\log\log N$ for the Erdős–Straus count $f$.
- **Elsholtz & Planitzer**, Proc. Roy. Soc. Edinburgh A (2019),
  DOI [`10.1017/prm.2018.137`](https://doi.org/10.1017/prm.2018.137):
  $O_\epsilon(n^{3/5+\epsilon})$ solutions of $m/n=\frac1{a_1}+\frac1{a_2}+\frac1{a_3}$.
- **Luca & Pappalardi**, Res. Number Theory (2019),
  DOI [`10.1007/s40993-019-0172-z`](https://doi.org/10.1007/s40993-019-0172-z):
  $x(\log x)^3\ll\sum_{p\le x}A_3(p)\ll x(\log x)^5$.
- **Huang & Vaughan**, J. Number Theory **131** (2011), 1641–1656,
  DOI [`10.1016/j.jnt.2011.04.001`](https://doi.org/10.1016/j.jnt.2011.04.001), and
  Acta Arith. **155** (2012), DOI [`10.4064/aa155-3-5`](https://doi.org/10.4064/aa155-3-5):
  mean values for the binary case.

Every one of these counts representations of **a single fixed value**. §5 needs coincidences
**between two independently varying values**, additionally tied by $e_1$ — a joint-distribution
question the divisor-counting and large-sieve techniques above are not set up for. Transfer is
plausible in spirit, not off the shelf.

**One caveat the manuscript should address.** §5.3 describes its heuristic as "of the
birthday-paradox type standard in analogous Diophantine settings". No source in the fetched
corpus instantiates such a heuristic for unit-fraction problems; that literature's register is
bounds on a single counting function. The technique is standard in analytic number theory
broadly, but the phrase as written implies a precedent in *this* literature that was not
found. Either cite an instance or soften the claim.

## 6. Independent verification of the manuscript's own counts

The cumulative **pair** counts in Table 5.1 were recomputed from scratch in exact rational
arithmetic and **reproduce exactly**: 1, 92, 386, 840, 1496, 2210, 3067 at
$S=18,100,200,300,400,500,600$. Table 5.1 is sound.

The **class** counts quoted in the task brief (92, 380, 822, 1468, 2158, 2977) do not
reproduce under the natural reading. Counting, per colliding $R$-value, (multiplicity $-\,1$)
gives 92, 383, 831, 1482, 2183, 3021 — close but consistently higher. The brief's figures use
some third convention. Since those numbers are not printed in the manuscript, this affects
nothing in the paper as it stands, but if a class count is ever printed its convention must be
stated explicitly.

Also verified: at $S=36$ there are exactly two colliding signatures — the scaled copy
$\{(4,16,16),(6,6,24)\}$ at $R=3/8$ and the primitive $\{(6,15,15),(8,8,20)\}$ at $R=3/10$ —
matching §5.1 exactly.

---

## Verdict

**New**, on a well-controlled negative search. Specifically:

- The problem is not posed in Guy (any edition; §D11 and §D12 checked directly, whole book
  grepped), not in OEIS (both count sequences, with a working control), and not in the
  Egyptian-fraction research literature including its current survey.
- The specific coincidence $\{(2,8,8),(3,3,12)\}$ does not appear in print in either the
  number-theoretic or the triangle-group framing. Both triples appear on Takeuchi's arithmetic
  list, but for unrelated reasons and without the coincidence being remarked.
- No asymptotic count exists, and existing methods do not directly transfer.

**What §5 should add.** Guy's **D16** is the same problem shape for $(e_1,e_3)$ instead of
$(e_1,e_2/e_3)$, and Schinzel *solved* it — arbitrarily many triples with common sum and
product, via rational points on an elliptic curve of positive rank. That is simultaneously
the strongest evidence that §5's problem is genuinely new *and* the most promising route to
improving on it: the manuscript's unconditional lower bound is currently $\lfloor S/18\rfloor$
from a scaling law, where the analogous problem yields arbitrarily large families by a
genuinely arithmetic construction. Citing D16 and Schinzel costs nothing and makes §5 look
situated rather than isolated.
