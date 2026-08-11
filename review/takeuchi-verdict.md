# Takeuchi verdict — commensurability classes of the arithmetic triangle groups

**Closes the single highest-value outstanding item in
[outstanding-fetches.md](outstanding-fetches.md) §1.2.**

The question: do $(2,8,8)$ and $(3,3,12)$ appear together anywhere in the
arithmetic-triangle-group literature — specifically, do they lie in a common commensurability
class of Takeuchi's classification?

**Answer: no. $(2,8,8)$ lies in Takeuchi's Class III, $(3,3,12)$ in Class XV. They are not
commensurable.** Confidence **high**, on three independent legs, one of which is a complete
verified reproduction of the class partition and one of which is an exact computation from
Takeuchi's own arithmeticity criterion.

The primary paper — Takeuchi, *Commensurability classes of arithmetic triangle groups*,
J. Fac. Sci. Univ. Tokyo Sect. IA Math. **24** (1977), no. 1, 201–212 — **was still not
retrieved**, and is not used below. What is used is a source that reproduces its full table.

---

## Summary table

| Question | Answer | Basis | Confidence |
|---|---|---|---|
| (a) Complete list of the 19 classes | **Complete** for the 18 cocompact classes (II–XIX), covering all 76 compact triples; Class I is the 9 non-compact triples, all commensurable with the modular group by Takeuchi's own remark | Tu–Yang App. A, verified to partition Takeuchi Thm 3(i) exactly | **high** |
| (b) Is $(3,3,12)$ arithmetic? | **Yes** — Takeuchi Theorem 3(i), compact types | Primary source, read this session | **certain** |
| (c) Do $(2,8,8)$ and $(3,3,12)$ ever share a class? | **No** — III vs XV | Tu–Yang App. A; independently, unequal invariant trace fields | **high** |
| (d) Does non-commensurability follow? | **Yes** — but *not* by the arithmeticity argument in the brief. See §5 | Commensurability classes partition; invariant trace field is a commensurability invariant | **high** |

---

## 1. What was retrieved, and what was not

| Source | Route | Outcome |
|---|---|---|
| Takeuchi, *Arithmetic triangle groups*, J. Math. Soc. Japan **29** (1977), 91–106, DOI [`10.2969/jmsj/02910091`](https://doi.org/10.2969/jmsj/02910091) | J-STAGE PDF, `https://www.jstage.jst.go.jp/article/jmath1948/29/1/29_1_91/_pdf`, 16 pp., text extracted with pymupdf | **Retrieved.** Theorem 3, pp. 105–106, read verbatim |
| Tu & Yang, *Algebraic transformations of hypergeometric functions and automorphic forms on Shimura curves*, Trans. Amer. Math. Soc. **365** (2013), no. 12, 6697–6729, DOI [`10.1090/S0002-9947-2013-05960-0`](https://doi.org/10.1090/S0002-9947-2013-05960-0); arXiv:1112.1001 | arXiv PDF, 31 pp., text extracted with pymupdf | **Retrieved.** Appendix A, pp. 23–31, reproduces the subgroup diagram of every commensurability class from Takeuchi 1977b |
| Takeuchi, *Commensurability classes of arithmetic triangle groups*, J. Fac. Sci. Univ. Tokyo Sect. IA Math. **24** (1977), 201–212 | — | **STILL UNRETRIEVED.** Not on J-STAGE, not on Project Euclid, no arXiv presence, no accessible scan located. Not used here |
| Voight, *Quaternion Algebras*, Springer GTM 288 (2021), `https://jvoight.github.io/quat-book.pdf` | Downloaded in full (883 pp.) and searched | **Retrieved, but does not contain the material.** §32.5 is "Cyclic subgroups" (of quaternion unit groups), not triangle groups. The string "Takeuchi" occurs on **zero** pages of the book; "triangle group" on six, none carrying a class table. **The brief's pointer to Voight §32.5 is wrong** |
| Maclachlan & Reid, *The Arithmetic of Hyperbolic 3-Manifolds*, GTM 219 (2003), §13.3 | Publisher and Google Books | **UNRETRIEVED — paywalled.** §13.3 is confirmed to exist and to be titled "Arithmetic Fuchsian Triangle Groups" (p. 418), but no accessible full text was located. Logged in [outstanding-fetches.md](outstanding-fetches.md). It was not needed: Tu–Yang supplies the full reproduction |
| Singerman, triangle-group inclusions | Not pursued | Not needed once Tu–Yang was verified complete. Would give inclusions, not the class partition |

Nothing below is recalled from memory. Every triple, class assignment and field was read from a
fetched document or computed in exact arithmetic during this session.

---

## 2. (a) The complete list of classes

Tu & Yang, Appendix A ("List of arithmetic triangle groups"), p. 23, verbatim:

> According to [7, 8], there are totally 85 arithmetic triangle groups, falling in 19 different
> commensurability classes. Here we give the subgroup diagrams.

Their `[7]` is Takeuchi 1977a (*Arithmetic triangle groups*); their `[8]` is Takeuchi 1977b
(*Commensurability classes of arithmetic triangle groups*) — the paper we could not retrieve.
Tu–Yang give the diagram for each of Classes II through XIX; **Class I is omitted** because it is
the non-cocompact class ($B=M(2,\mathbb Q)$, the classical modular curves), which they set aside
at p. 8: *"The first class in his list corresponds to classical modular curves."* That matches
Takeuchi's own closing remark in 1977a, p. 106, verbatim:

> In the non-compact case this is trivial because these groups are all commensurable with some
> conjugate group of the modular group.

So Class I $=$ the nine non-compact triples, and Classes II–XIX $=$ the 76 compact triples.

### The 18 cocompact classes, as printed by Tu–Yang

Triangle groups only (their diagrams also carry non-triangle Fuchsian subgroups — quadrilateral
groups, genus-1 groups — which are not part of Takeuchi's 85 and are omitted here).

| Class | Triangle groups | Count |
|---|---|---:|
| I | *(non-compact)* $(2,3,\infty)$, $(2,4,\infty)$, $(2,6,\infty)$, $(2,\infty,\infty)$, $(3,3,\infty)$, $(3,\infty,\infty)$, $(4,4,\infty)$, $(6,6,\infty)$, $(\infty,\infty,\infty)$ | 9 |
| II | $(2,4,6)$, $(2,6,6)$, $(3,4,4)$, $(3,6,6)$ | 4 |
| **III** | $(2,3,8)$, $(2,4,8)$, $(2,6,8)$, **$(2,8,8)$**, $(3,3,4)$, $(3,8,8)$, $(4,4,4)$, $(4,6,6)$, $(4,8,8)$ | 9 |
| IV | $(2,3,12)$, $(2,6,12)$, $(3,3,6)$, $(3,4,12)$, $(3,12,12)$, $(6,6,6)$ | 6 |
| V | $(2,4,12)$, $(2,12,12)$, $(4,4,6)$, $(6,12,12)$ | 4 |
| VI | $(2,4,5)$, $(2,4,10)$, $(2,5,5)$, $(2,10,10)$, $(4,4,5)$, $(5,10,10)$ | 6 |
| VII | $(2,5,6)$, $(3,5,5)$ | 2 |
| VIII | $(2,3,10)$, $(2,5,10)$, $(3,3,5)$, $(5,5,5)$ | 4 |
| IX | $(3,4,6)$ | 1 |
| X | $(2,3,7)$, $(2,3,14)$, $(2,4,7)$, $(2,7,7)$, $(2,7,14)$, $(3,3,7)$, $(7,7,7)$ | 7 |
| XI | $(2,3,9)$, $(2,3,18)$, $(2,9,18)$, $(3,3,9)$, $(3,6,18)$, $(9,9,9)$ | 6 |
| XII | $(2,4,18)$, $(2,18,18)$, $(4,4,9)$, $(9,18,18)$ | 4 |
| XIII | $(2,3,16)$, $(2,8,16)$, $(3,3,8)$, $(4,16,16)$, $(8,8,8)$ | 5 |
| XIV | $(2,5,20)$, $(5,5,10)$ | 2 |
| **XV** | $(2,3,24)$, $(2,12,24)$, **$(3,3,12)$**, $(3,8,24)$, $(6,24,24)$, $(12,12,12)$ | 6 |
| XVI | $(2,5,30)$, $(5,5,15)$ | 2 |
| XVII | $(2,3,30)$, $(2,15,30)$, $(3,3,15)$, $(3,10,30)$, $(15,15,15)$ | 5 |
| XVIII | $(2,5,8)$, $(4,5,5)$ | 2 |
| XIX | $(2,3,11)$ | 1 |
| | **total** | **85** |

### The completeness check that makes this "complete" rather than "as far as we got"

The 76 signatures in Classes II–XIX were compared, as multisets, against Takeuchi Theorem 3(i)
transcribed from the J-STAGE PDF. Result:

```
Takeuchi Thm 3(i) compact triples, from primary PDF : 76   (distinct: 76)
Tu-Yang App. A triangle-group nodes, Classes II-XIX : 76   (distinct: 76)
in Tu-Yang not in Takeuchi : []
in Takeuchi not in Tu-Yang : []
EXACT PARTITION OF THE 76 COMPACT TRIPLES : True
```

No overlaps, no omissions, no extras. **This is a verification of completeness, not an
assumption of it** — the brief asked for the ten unchecked classes, and all eighteen cocompact
classes are now accounted for, each triple in exactly one.

> ### Correction to an earlier vault record
>
> The vault note `takeuchi-1977-arithmetic-triangle-groups-theorem-3-full-list-verbatim-85-triples`
> transcribes Theorem 3(i) as **75** triples while asserting in its own count check that it holds
> 76. **$(2,3,16)$ was dropped in transcription.** The primary PDF, p. 105, reads:
>
> > (2, 3, 7), (2, 3, 8), (2, 3, 9), (2, 3,10), (2, 3,11), (2, 3,12), (2, 3,14), **(2, 3,16)**,
> > (2, 3,18), (2, 3, 24), (2, 3, 30), …
>
> With $(2,3,16)$ restored the count is 76, and the partition above closes exactly. Without it,
> the check fails on precisely that one triple. Nothing else in the vault note is affected, and
> no conclusion anywhere in the review depended on the omitted entry — but the note should be
> corrected before it is cited again.

---

## 3. (b) Is $(3,3,12)$ arithmetic?

**Yes, unambiguously.** Takeuchi, *Arithmetic triangle groups*, Theorem 3(i), p. 106, verbatim
from the J-STAGE PDF (OCR artefacts in the surrounding entries left as they appear):

> (3, 3, 4), (3, 3, 5), (3, 3, 6), (3, 3, 7), (3, 3, 8), (3, 3, 9), **(3, 3,12)**, (3, 3,L15),

Theorem 3 is stated as "The complete list of all triples $(e_1,e_2,e_3)$ of arithmetic type", so
membership is decisive. $(2,8,8)$ is on the same list, p. 105. Both were already confirmed in the
literature sweep; this is a second reading of the same primary source.

---

## 4. (c) Do the two ever appear in a common class?

**No.** $(2,8,8)$ is a node of Tu–Yang's Class III diagram (p. 26); $(3,3,12)$ is a node of their
Class XV diagram (p. 30). Since the 18 diagrams partition the 76 compact triples exactly (§2),
no triple appears twice, and these two are in different classes.

Tu–Yang print Class III twice — once at p. 7 in the body, once at p. 26 in the appendix. The body
version, verbatim:

> According to [8], Takeuchi's Class III of commensurable arithmetic triangle groups has the
> following subgroup diagram. … (2, 6, 8) (2, 3, 8) (4, 6, 6) (3, 8, 8) (3, 3, 4) (2, 4, 8)
> (4, 4, 4) **(2, 8, 8)** (4, 8, 8)

This is exactly the nine-member class recorded in the brief as already established from two
secondary reproductions — $(2,3,8)$, $(2,4,8)$, $(2,6,8)$, $(2,8,8)$, $(3,3,4)$, $(3,8,8)$,
$(4,4,4)$, $(4,6,6)$, $(4,8,8)$ — so the partial verification and the full one agree, and the
earlier finding that $(3,3,12)$ was absent from the visible classes is confirmed rather than
merely extended.

### Independent confirmation: the invariant trace fields differ

This does not depend on Tu–Yang at all. Takeuchi's Theorem 1 (1977a, §3) makes the arithmeticity
criterion turn on

$$k_0=\mathbb Q\!\left(\cos^2\tfrac\pi{e_1},\,\cos^2\tfrac\pi{e_2},\,\cos^2\tfrac\pi{e_3},\,
\cos\tfrac\pi{e_1}\cos\tfrac\pi{e_2}\cos\tfrac\pi{e_3}\right),$$

the invariant trace field $\mathbb Q(\operatorname{tr}\Gamma^{(2)})$ — which is a
*commensurability invariant*. Computed exactly (sympy, exact radicals) this session:

| | $\cos^2(\pi/e_i)$ | product term | $k_0$ | $[k_0:\mathbb Q]$ |
|---|---|---|---|---:|
| $(2,8,8)$ | $0,\ \tfrac{2+\sqrt2}{4},\ \tfrac{2+\sqrt2}{4}$ | $0$ | $\mathbb Q(\sqrt2)$, minpoly $x^2-2$ | **2** |
| $(3,3,12)$ | $\tfrac14,\ \tfrac14,\ \tfrac{2+\sqrt3}{4}$ | $\tfrac{\sqrt2+\sqrt6}{16}$ | $\mathbb Q(\sqrt2,\sqrt3)=\mathbb Q(\sqrt2+\sqrt6)$, minpoly $x^4-16x^2+16$ | **4** |

$\sqrt3=\frac{(\sqrt2+\sqrt6)^2-8}{4}$ and $\sqrt2=\frac{\sqrt2+\sqrt6}{1+\sqrt3}$, both verified
symbolically, so $\mathbb Q(\sqrt2+\sqrt6)=\mathbb Q(\sqrt2,\sqrt3)$ exactly.

**Degrees 2 and 4. The invariant trace fields are unequal, so the invariant quaternion algebras
cannot be isomorphic, so the groups are not commensurable.** Note the containment
$\mathbb Q(\sqrt2)\subset\mathbb Q(\sqrt2,\sqrt3)$ is not a loophole: commensurable Fuchsian
groups have *equal* invariant trace fields, not nested ones. The $\mathbb Q(\sqrt2)$ attribution
for $(2,8,8)$ recorded in the brief is confirmed.

---

## 5. (d) Does non-commensurability follow — and by which argument?

**Yes, it follows. But the route named in the brief does not work, and the difference matters.**

The brief proposes to conclude non-commensurability from "arithmeticity being a commensurability
invariant". That argument separates an arithmetic group from a non-arithmetic one. Here **both
groups are arithmetic** (§3), so arithmeticity is shared and separates nothing. The correct
statements are:

1. **From the classification (§4).** Takeuchi's 19 classes are *commensurability* classes — they
   partition the 85 arithmetic triples by the relation itself. Two triples in different classes
   are non-commensurable by construction. $(2,8,8)\in$ III, $(3,3,12)\in$ XV, so they are
   non-commensurable. This is the direct argument and it needs no invariant.

2. **From the invariant trace field (§4, independent).** For arithmetic Fuchsian groups the pair
   (invariant trace field, invariant quaternion algebra) is a complete commensurability
   invariant. $[k_0:\mathbb Q]$ is 2 for $(2,8,8)$ and 4 for $(3,3,12)$, so the fields differ and
   the groups are non-commensurable. This leg is independent of Tu–Yang and rests only on
   Takeuchi's Theorem 1 plus exact arithmetic.

### Consequence for the manuscript

**Theorem B is not touched, and the live thread flagged in
[VERDICT.md](hyperresearch/VERDICT.md) §1 is now closed negatively.** That thread was: *if*
$(2,8,8)$ and $(3,3,12)$ share a commensurability class, the pair may have an unremarked prior
appearance in Takeuchi 1977b, which would then need citing. They do not share a class, so there
is no such appearance and nothing new to cite. The manuscript's Q1 novelty finding stands
unchanged, and one qualifier can be dropped from it.

Worth stating in the paper in one sentence, because it sharpens the coincidence rather than
weakening it: the two pillows have **equal hyperbolic area** — that is exactly what equal
reciprocal sum means, by Gauss–Bonnet — yet their triangle groups are **not commensurable**, and
their invariant trace fields are not even of the same degree. Equal covolume is therefore not
explained by any commensurability relation between them. It is a genuine Diophantine coincidence,
which is the paper's thesis.

---

## 6. Confidence, stated plainly

**High, not certain.** What would change the answer, and why none of it is likely:

- **The class assignment is one source deep.** Tu–Yang is a peer-reviewed TAMS paper reading
  Takeuchi 1977b, not Takeuchi 1977b itself. If Tu–Yang mis-transcribed a class, the assignment
  could move. Against that: their eighteen diagrams partition Takeuchi's 76 compact triples
  *exactly*, with no overlap and no residue, which a transcription error would almost certainly
  have broken; and the independent trace-field computation gives the same answer without them.
- **The trace-field leg is airtight but narrower.** It proves non-commensurability. It does not
  prove that Tu–Yang's *class numbering* matches Takeuchi's, nor that Class XV is exactly the
  six triples listed. Those rest on Tu–Yang.
- **What is certain:** $(3,3,12)$ and $(2,8,8)$ are both arithmetic (primary source), and they
  are not commensurable (two independent arguments).
- **What remains open:** the primary paper, Takeuchi 1977b, is still unread. Retrieving it would
  convert "high" to "certain" and confirm the class numbering. It remains logged in
  [outstanding-fetches.md](outstanding-fetches.md) §1.2, now with a substantially reduced stake:
  the question it was wanted for has been answered by other means.

A partial verification reported as complete would be worse than a gap. This one is complete for
(b), (c) and (d), and complete-and-verified for (a) modulo the single-source dependency named
above.
