# P2-DIGEST — transferable extract of review/P2.md

`review/P2.md` is too large to move in one piece. This digest carries **§0 (manifest), §2
(VERDICT.md), §5 (defect list), §6 (strengthening targets) and §9 (the moduli defect)** in full
and unaltered — the sections needed to reach a decision without the supporting apparatus. It is
an extract, not a summary: every byte below also appears in `P2.md`.

Not included here, and present only in `P2.md`: §1 repository state, §3 Q2, §4 Q4, §7 corrections,
§8 supporting files, §10 my commentary.

---

## 0. MANIFEST

### 0.1 Source files reproduced in this document

Sizes in bytes, digests SHA-256, timestamps local (this machine, `Darwin 25.3.0`).

| Path | Bytes | SHA-256 | Last modified | Appears in |
|---|---:|---|---|---|
| `review/hyperresearch/VERDICT.md` | 29,744 | `ca6fe1eb2371709cc91060e38e10b91df0b78f8a3cf7955f0924146dcb8472e6` | 2026-08-11 11:05:31 | §2, §7 |
| `review/hyperresearch/Q2-cone-coefficients.md` | 21,509 | `dd13350c70250d71c87fd350bd0ae8e2f3cf6969044e2c927c00501ad40c763a` | 2026-08-09 16:53:36 | §3 |
| `review/hyperresearch/Q4-stability.md` | 20,497 | `de704696850af20afea3b32dabe88d9de11acb53da33e8b5f94a31bc99734bd9` | 2026-08-09 16:13:02 | §4 |
| `review/source-hygiene.md` | 14,218 | `434266b320eb1ea44b9e0ea3642dd9466eae3af4403aac6142640682751bde78` | 2026-08-09 12:35:19 | §5 (substitute) |
| `review/claim-ledger.md` | 32,819 | `a841ea9ef21f2b6599cb2b83d55a547fd5102d83305b2d3edf5d0e81d542a2fb` | 2026-08-09 13:49:52 | §5 (substitute) |
| `research/critic-findings-depth.json` | 30,211 | `feac6f252e0b72416d1dd9bede3fc517623a539f6326f349f2e671b116775ec4` | 2026-08-09 15:55:10 | §6 (substitute), §9 |
| `research/critic-findings-dialectic.json` | 14,759 | `34f87d96a252b07121f457e1e98de52f777b3acbfff03b1692e17b5bbde655fe` | 2026-08-09 16:44:34 | §9 (extract) |
| `research/patch-log.json` | 9,497 | `029ca5909b4e134459c1ae08ac514cfb8f471d2ed30470d02964d1c3c6bdb985` | 2026-08-09 16:03:45 | §9 (extract) |
| `review/outstanding-fetches.md` | 14,431 | `a08a8400153066e3e262a903973a1c30997e567cfa601a92b0749bb22942f4e5` | 2026-08-11 11:08:54 | §8 |
| `review/convention-note.md` | 5,177 | `872c6c5a1f385c91eb97a9c07746e37db8bf55f7035883ae5b016c6300136f2d` | 2026-08-09 13:48:44 | §8 |
| `review/remote-remediation.md` | 9,620 | `c8fbdcb66bc7dc935b9c6c15d36e723e71d3ae9837668943c2cdd6afc3387e40` | 2026-08-09 13:50:24 | §8 |
| `review/reproducibility-report.md` | 10,378 | `7a69999f76611b25075cb338b1de57f0affdbd434a942e3f36dd9b2287578016` | 2026-08-09 13:48:02 | §8 |
| `review/coverage-map.csv` | 29,150 | `c6079459ef25671e715ab993e822dd682f845fd883cd1d350f28ebf1b29978db` | 2026-08-09 13:52:15 | §8 (counts + non-backed rows) |
| `research/readability-decisions.json` | 3,512 | `3a03f650d4f65b7641ba1f8d7320f3550bfae2e46f69f32fc84cddfae8616321` | 2026-08-09 16:53:58 | §8 |
| `review/hyperresearch/APPENDIX-ncone-computation.md` | 5,983 | `cea2a787d80028c4efd320e9029157100b5c283df5e6290e300cd16917a00350` | 2026-08-09 16:14:47 | §9 |

Two of these are byte-identical to each other and both are tracked: `review/hyperresearch/APPENDIX-ncone-computation.md` and `research/temp/original-computation-ncone.md` share SHA-256 `cea2a787d80028c4efd320e9029157100b5c283df5e6290e300cd16917a00350`. Only the first is reproduced here.

### 0.2 Files requested that DO NOT EXIST

Nothing below has been silently substituted. Each row names the substitution explicitly.

**`review/referee/DEFECT-LIST.md`**

- *Status:* **Does not exist. The directory `review/referee/` does not exist either.** No file in the repository carries that name or anything close to it.
- *Substituted by:* Two files together carry the content, and **both are reproduced in full in §5 rather than one being silently passed off as the requested file**: `review/source-hygiene.md` — whose §7 *is* a defect list organised by severity (Blocking for submission / Should fix before submission / Cosmetic / Not a defect), covering the LaTeX source; and `review/claim-ledger.md` — whose §C (findings C-1…C-6) and §F (consequences for submission) are the defect list against the verification artefact. Neither is a referee report. No referee report was ever produced in this repository.

**`review/referee/STRENGTHENING-TARGETS.md`**

- *Status:* **Does not exist.** No file with a `T1`–`T4` ranking exists under `review/`.
- *Substituted by:* The only artefact in the repository carrying `T1`, `T2`, `T3`, `T4` as ranked identifiers is `research/critic-findings-depth.json`, the depth critic's findings list — twelve findings `T1`–`T12`, severity-ranked, `T1`–`T5` at severity `high` and `T6`–`T12` at `medium`, each with an `issue` / `evidence` / `suggested_fix` triple. It is reproduced in full in §6. **It is a critic findings file, not a strengthening-targets document**, and the T-numbering is the critic's own emission order, not a priority ranking someone assigned. The nearest thing to a deliberate strengthening ranking is VERDICT.md's answer 6 ("What to change", five numbered items) — already reproduced in §2.

**`the author-corrections file (as a standalone file)`**

- *Status:* **No standalone file holds them.**
- *Substituted by:* The corrections live in `review/hyperresearch/VERDICT.md`, in the section headed `## Summary of corrections the manuscript needs` — a numbered table, items 1–22. §7 reproduces that section verbatim; §2 reproduces the whole file, so it appears twice, as instructed.

**`README.md (repository root)`**

- *Status:* **Does not exist at the repository root.**
- *Substituted by:* The actual file is `code/README.md`. It is deliberately *not* at the root: the upstream `main` already has a root `README.md`, and creating one here would be the filename collision that step 3 forbids. See §1 and the push report.

**`requirements.txt (repository root)`**

- *Status:* **Does not exist at the repository root.**
- *Substituted by:* The actual file is `code/requirements.txt`.

**`run_all.sh (repository root)`**

- *Status:* **Does not exist at the repository root.**
- *Substituted by:* The actual file is `code/run_all.sh`.

**`the 172-row table in review/reproducibility-report.md`**

- *Status:* **`reproducibility-report.md` contains no 172-row table.** It carries summary tables only.
- *Substituted by:* The 172-row table is `review/coverage-map.csv` (173 lines: header + 172 rows). §8 gives `reproducibility-report.md` in full, then the coverage map as counts by category plus every row not marked `backed`, exactly as requested.

### 0.3 One file modified while assembling this document

### 0.4 Working files withheld from publication

Seven `research/` working files are present on the authoring machine but are **not published**: they are excluded from version control locally, so they appear in §1's `ls -R` output — reproduced verbatim from the filesystem — but not in `git ls-files`. Each either embeds an absolute filesystem path from the machine it was written on, restates the working brief including its authorship constraints, or is a private working note explicitly marked never-to-be-quoted. They are named here so the omission is visible rather than silent.

| Withheld file | Reason |
|---|---|
| `research/scaffold.md` | Embeds the absolute working directory of the authoring machine |
| `research/prompt-decomposition.json` | Restates the working brief, including its authorship constraints |
| `research/query-hyperbolic-pillow-heat-novelty-813161.md` | Same |
| `research/critic-findings-instruction.json` | Contains a literal search-pattern list of software-vendor names, used as a hygiene check |
| `research/polish-log.json` | Carries a self-referential hygiene assertion quoting the authorship constraint |
| `research/temp/coverage-matrix.md` | Same as `prompt-decomposition.json` |
| `research/temp/orchestrator-notes.md` | Header reads *"Private working notes. Never quoted in any deliverable."* |

Nothing load-bearing is in them. Every finding they informed is reproduced elsewhere in this document from the deliverable that carries it.

### 0.5 One file modified while assembling this document

`review/hyperresearch/VERDICT.md` was edited to add **correction 22** (the abstract's `c ≈ 0.0085–0.0093` versus Table 1's `0.0097` at `S = 200`), per the standing instruction to log that correction without touching `paper/main.tex`. `paper/main.tex` is unmodified; its MD5 is still `adfa0001c73e3721f3ccdcc6dcda7e12` as recorded in `claim-ledger.md` line 3. The count line near the top of VERDICT.md was updated from 21 to 22 in the same edit. Everything else in every file reproduced here is exactly as it stood before this session.

---

## 2. review/hyperresearch/VERDICT.md — FULL TEXT

Includes the at-a-glance answer table (six rows, one per question) near the top.

```markdown
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
```

---

## 5. DEFECT LIST

**`review/referee/DEFECT-LIST.md` does not exist** (see §0.2). The two files that together carry its content are reproduced in full below, both named as substitutions.

### 5.1 `review/source-hygiene.md` — FULL TEXT

Defects in the LaTeX source. Its §7 is the severity-ranked list: **Blocking for submission** (2 items), **Should fix before submission** (5), **Cosmetic / editorial judgement** (5), **Not a defect** (1).

```markdown
# Source Hygiene Report — `paper/main.tex`

Audited 2026-08-09. Source: `paper/main.tex`, 723 lines, MD5 `adfa0001c73e3721f3ccdcc6dcda7e12`.
**Nothing in this report has been fixed.** It is an inventory only, per instruction.

---

## 1. Document class and package inventory

**Class:** `\documentclass[12pt, letterpaper]{article}` (line 1).

A plain `article` class, not a journal class. No `amsart`, no publisher template. If the target journal supplies a class (`amsart`, `elsarticle`, Springer `svjour3`), the preamble will need reworking — the geometry, `\doublespacing`, and hand-rolled theorem environments below will all be overridden or conflict.

**Packages — 16 declared, in load order:**

| # | Line | Package | Used? | Evidence |
|---|---|---|---|---|
| 1 | 3 | `amsmath` | **yes** | 175 hits (`\begin{equation}`, `\tfrac`, `\operatorname`) |
| 2 | 3 | `amssymb` | **yes** | `\mathbb` etc. |
| 3 | 3 | `amsthm` | **yes** | 27 hits (`\newtheorem`, `\begin{proof}`) |
| 4 | 3 | `mathrsfs` | **NO** | zero `\mathscr` in document |
| 5 | 4 | `geometry` | **yes** | `\geometry{...}` line 22 |
| 6 | 5 | `tikz` | **yes** | one `tikzpicture`, Figure 1 |
| 7 | 6 | `titlesec` | **NO** | zero `\titleformat` / `\titlespacing` |
| 8 | 7 | `enumitem` | **yes** | `\begin{enumerate}[label=(\roman*)]` line 218 |
| 9 | 8 | `hyperref` | **yes** | loaded; no `\href`/`\url` but provides `\ref` linking |
| 10 | 9 | `setspace` | **yes** | `\doublespacing` line 29 |
| 11 | 10 | `xcolor` | **NO** | zero `\textcolor` / `\definecolor`; `\filldraw[red]` in Fig. 1 works from TikZ's own colours |
| 12 | 11 | `mathtools` | **NO** | zero `\coloneqq`, `\DeclarePairedDelimiter`, `\mathclap`, `\prescript` |
| 13 | 12 | `tikz-cd` | **NO** | zero `tikzcd` environments |
| 14 | 13 | `booktabs` | **yes** | 17 hits (`\toprule`/`\midrule`/`\bottomrule`) |
| 15 | 14 | `longtable` | **yes** | Table 1 (`tab:enum`) |
| 16 | 15 | `caption` | **NO** | zero `\captionsetup` |

**Six packages are loaded but unused:** `mathrsfs`, `titlesec`, `xcolor`, `mathtools`, `tikz-cd`, `caption`.

Two of these — `titlesec` and `tikz-cd` — were **not installed on this machine and blocked compilation entirely** until installed during this audit. That is the worst case for an unused dependency: it adds a hard build requirement that buys nothing. Any co-author or editor with a basic TeX Live install will hit the same wall.

**Other preamble notes:**

- Lines 17–20: `\hyphenpenalty=10000`, `\exhyphenpenalty=10000`, `\pretolerance=10000`, `\sloppy`. This disables hyphenation across the whole document. It is the direct cause of the 24 underfull `\hbox` warnings (§6) and produces visibly loose inter-word spacing in a double-spaced 12pt layout. Most journals will not want this.
- Lines 31–46: theorem environments hand-declared. Note `\newtheorem{mainthm}{Theorem}` with `\renewcommand{\themainthm}{\Alph{mainthm}}` — this creates a **second, independent** Theorem counter alongside `\newtheorem{theorem}{Theorem}[section]`. The document therefore contains both "Theorem A/B/C" and "Theorem 3.4", plus `\newtheorem*{theorem*}{Theorem}`. Three distinct things all print as "Theorem". Legal, but a copy-editor will query it.
- Line 48: `\title{\vspace{-2cm}...}` — a negative vertical space hard-coded into the title. Fragile under any class change.
- No `\usepackage{amsfonts}`, no `\usepackage[T1]{fontenc}`, no `inputenc`. The file is UTF-8 and contains no non-ASCII characters (verified), so this compiles, but `fontenc` is normally expected.

---

## 2. Corrupted em-dash pattern

The manuscript contains **zero** real em-dashes (`—`, U+2014). Every em-dash has been replaced by a comma-plus-spacing artefact.

**Total: 53 occurrences across 25 distinct lines.**

- **48 inline** occurrences of the pattern ` ,  ` (space, comma, two spaces) used as a parenthetical/appositive dash.
- **5 trailing** occurrences of ` , ` at end-of-line, which are the *closing* halves of dash pairs inside bibliography section comments.

No other corruption variants were found: 0 instances of `,,`, 0 instances of a single-spaced ` , ` in body text, and the 70 occurrences of `--` are all legitimate LaTeX en-dashes in page ranges and hyphenated author names (Dryden--Gordon--Greenwald--Webb, Cauchy--Schwarz, etc.) — **do not** mass-replace those.

### Line-by-line inventory (inline ` ,  `)

| Line | Count | Context |
|---|---|---|
| 58 | **5** | Abstract — the heaviest single line |
| 75 | 1 | §1 opening paragraph |
| 101 | 1 | §1, "the question we answer is *geometric*" |
| 103 | 1 | §1, definition of *collision* |
| 114 | 1 | Theorem C statement |
| 118 | 2 | Corollary D statement |
| 121 | 2 | §1, hierarchy paragraph |
| 134 | 1 | §1.1 Related work, Uçar sentence |
| 153 | **3** | §1.4(b) Our contribution |
| 155 | 2 | §1.4(c) Load-bearing only |
| 160 | **4** | §1.5 Scope and limitations |
| 236 | 2 | §2.4 footnote on `eq:b1` |
| 275 | 2 | §3 opening |
| 348 | 2 | §3.2, after separation proof |
| 360 | 2 | §3.3, scope caveat |
| 373 | 2 | §4.1, proof of Theorem C |
| 395 | 2 | §4.2 `remark*` |
| 479 | 2 | §5.3, after Conjecture |
| 489 | 2 | §5.4 An extremal companion |
| 494 | **4** | `rem:ncone` |
| 632 | 1 | bibliography section comment |
| 654 | 1 | bibliography section comment |
| 661 | 1 | bibliography section comment |
| 686 | 1 | bibliography section comment |
| 702 | 1 | bibliography section comment |
| **total** | **48** | |

### Trailing ` , ` (closing dash), all in bibliography comments

| Line | Full line |
|---|---|
| 632 | `% ,  reading geometry from finitely many heat invariants , ` |
| 654 | `% ,  isospectral constructions , ` |
| 661 | `% ,  orbifold heat invariants and isospectral orbifolds , ` |
| 686 | `% ,  cone and corner contributions to heat coefficients , ` |
| 702 | `% ,  hyperbolic orbisurfaces and triangle groups , ` |

These five are inside `%` comments and do not affect output, but they confirm the corruption was applied mechanically across the whole file, comments included — which is useful evidence that a single global substitution caused it.

**Caution for the eventual fix:** the replacement is *not* uniformly `---`. Some sites are genuine appositive dashes (line 58: "pillows ,  spheres carrying three cone points"); at least one reads as a true comma in a list. Each of the 53 needs an individual decision, and lines 632/654/661/686/702 are paired open/close dashes that must be fixed together.

---

## 3. Missing author / affiliation / ORCID metadata

| Field | Status |
|---|---|
| `\title` | **present** (line 48) |
| `\author` | **ABSENT** |
| `\date` | present but **empty** — `\date{}` (line 50) |
| Affiliation / `\institute` / `\address` | **ABSENT** |
| ORCID | **ABSENT** |
| Email / corresponding author | **ABSENT** |
| `\thanks` (funding footnote) | **ABSENT** |
| Keywords | present (line 62) |
| 2020 MSC | present (line 65) — `58J53, 58J50, 35K08, 11D45, 11D68` |

The compiler confirms this: `LaTeX Warning: No \author given.`

The paper is therefore **fully anonymous as it stands**. Note the tension with line 618: *"The author declares no competing interests"* — singular "author", in a paper with no author named. Every journal requires author name, affiliation, and (increasingly) ORCID at submission; several require a designated corresponding author with email.

`\maketitle` is followed by `\thispagestyle{empty}` (line 55), so there is no page number on page 1.

---

## 4. Undefined references

**None.** Checked exhaustively:

| Check | Result |
|---|---|
| `\label` definitions | 42 |
| `\ref` / `\eqref` calls | 150 |
| **Undefined references** | **0** |
| `\bibitem` keys | 28 |
| `\cite` keys invoked | 69 |
| **Undefined citations** | **0** |
| Duplicate `\bibitem` keys | 0 |
| Uncited bibliography entries | 0 |

Confirmed at the LaTeX level too: a full `latexmk -pdf` run to a stable state produces **no** `Reference ... undefined`, `Citation ... undefined`, or `multiply-defined` warnings.

**Eight labels are defined but never referenced.** Harmless, but they are dead weight and a couple suggest a cross-reference was intended and dropped:

`rem:bugfix` · `sec:cone` · `sec:core` · `sec:heatexp` · `sec:intro` · `sec:novelty` · `sec:related` · `sec:scope`

`rem:bugfix` is the one worth a second look — it labels the Remark at line 229 that warns against a mis-normalization, and nothing in the text points to it.

---

## 5. Bibliography entries lacking DOIs

The bibliography is a hand-written `thebibliography` environment (lines 630–721). **There is no `.bib` file** anywhere in the project, and `refs/` is empty. That is itself a submission risk: most publishers want BibTeX source, and hand-maintained `\bibitem` lists cannot be validated against Crossref automatically.

**28 of 28 entries lack a DOI — 100%.**

Of those, 11 carry an arXiv identifier, which partially substitutes. **17 entries have neither a DOI nor an arXiv ID**, and these are the ones a production editor will bounce back:

| Key | Reference | arXiv? |
|---|---|---|
| `kac1966` | Kac, *Can one hear the shape of a drum?*, Amer. Math. Monthly 73 (1966) | no |
| `mckeansinger1967` | McKean–Singer, J. Differential Geom. 1 (1967) 43–69 | no |
| `datchevhezari2013` | Datchev–Hezari, MSRI Publ. 60 (2013) 455–485 | no |
| `griesermaronna2013` | Grieser–Maronna, Notices AMS 60 (2013) 1440–1447 | no |
| `lurowlett2015` | Lu–Rowlett, Amer. Math. Monthly 122 (2015) 815–835 | no |
| `hezarizelditch2022` | Hezari–Zelditch, Ann. of Math. 196 (2022) 1083–1134 | no |
| `sunada1985` | Sunada, Ann. of Math. 121 (1985) 169–186 | no |
| `gww1992` | Gordon–Webb–Wolpert, Bull. AMS 27 (1992) 134–138 | no |
| `donnelly1976` | Donnelly, Math. Ann. 224 (1976) 161–170 | no |
| `dggw2008` | Dryden–Gordon–Greenwald–Webb, Michigan Math. J. 56 (2008) 205–238 | no |
| `ssw2006` | Shams–Stanhope–Webb, Arch. Math. 87 (2006) 375–384 | no |
| `rsw2008` | Rossetti–Schueth–Weilandt, Ann. Global Anal. Geom. 34 (2008) 351–366 | no |
| `doylerossetti2008` | Doyle–Rossetti, New York J. Math. 14 (2008) 193–204 | no |
| `drydenstrohmaier2009` | Dryden–Strohmaier, Canad. Math. Bull. 52 (2009) 66–71 | no |
| `harmer2008` | Harmer, J. Aust. Math. Soc. 84 (2008) 217–227 | no |
| `scott1983` | Scott, Bull. London Math. Soc. 15 (1983) 401–487 | no |
| `buser1992` | Buser, *Geometry and Spectra of Compact Riemann Surfaces*, Birkhäuser 1992 | no (book) |

`dggw2008` is the most important omission: it is the analytic foundation of the entire paper, cited 8 times, and carries no persistent identifier.

Entries carrying an arXiv ID but still no DOI (11): `gomezserrano2020`, `proctorstanhope2009`, `barihunsicker2017`, `richardsonstanhope2019`, `gittinsetal2024`, `schueth2019`, `schueth2025`, `suleymanova2017`, `nrs2024`, `looisher2025`, `ucar2017`.

Several of these are labelled "preprint" but have since appeared in journals and should be updated to the published version at proof stage — `schueth2019` already gives both (Ann. Inst. Fourier 69 (2019) 2827–2855 *and* arXiv:1812.06119), so the intent is clearly to cite published versions where known.

### Additional bibliography inconsistencies noted in passing

- **`gittinsetal2024`** — the citation key says `2024`, the entry text says `(2023)`, and the arXiv ID `2311.00337` is a November 2023 submission. Key, printed year, and identifier disagree.
- **`proctorstanhope2009`** — keyed and printed as 2009, but arXiv:0811.0797 is a 2008 submission. Consistent with a 2009 publication date; worth confirming.
- **`nrs2024`** — journal given as "Ann. Math. Québec (2024)" with no volume, issue, or page range.
- **`schueth2025`** (arXiv:2511.22255) and **`looisher2025`** (arXiv:2512.04422) are recent preprints; check for publication before submission.

---

## 6. Compilation status

Compiles cleanly **once the two unused-but-missing packages are installed**.

| | |
|---|---|
| Engine | `pdflatex` via `latexmk -pdf` |
| Result | success, exit 0 |
| Output | `paper/build/main.pdf` |
| Pages | **44** |
| Undefined refs/cites | 0 |
| Overfull `\hbox` | **2** |
| Underfull `\hbox` | **24** |
| Other warnings | `No \author given` · `!h float specifier changed to !ht` (×2) |

**Overfull boxes:**

| Log line | Location |
|---|---|
| 344 (18.28 pt too wide) | §3.2, the three-way displayed inequality chain `R⁻_{18,3} > … R⁺_{18,6}` at `main.tex` line 341–343 |
| 410 (53.61 pt too wide) | §5, the displayed definition of `N(S)` and `𝒩(S)` at `main.tex` line 408–409 |

Both are display-math lines running into the margin — the 53.6 pt one is visible in the PDF. The narrow `\geometry` setting (1.5 in left and right margins on letterpaper leaves a 5.5 in text block) makes long displays tight.

The 24 underfull boxes are a direct consequence of the hyphenation suppression in lines 17–20, not of any individual paragraph.

---

## 7. Summary of hygiene findings, by severity

**Blocking for submission**

1. No `\author`, no affiliation, no ORCID, no corresponding-address (§3). The paper is anonymous.
2. 53 corrupted em-dashes across 25 lines (§2), including 5 in the abstract alone — the first thing an editor reads.

**Should fix before submission**

3. 28/28 bibliography entries lack DOIs, 17 lack any persistent identifier (§5); `dggw2008`, the paper's analytic foundation, is among them.
4. No `.bib` file; `refs/` is empty (§5).
5. Two unused packages (`titlesec`, `tikz-cd`) are hard build blockers on a standard TeX install (§1).
6. Two overfull boxes, one badly so at 53.6 pt (§6).
7. Key/year/arXiv disagreement in `gittinsetal2024` (§5).

**Cosmetic / editorial judgement**

8. Four further unused packages: `mathrsfs`, `xcolor`, `mathtools`, `caption` (§1).
9. Global hyphenation suppression causing 24 underfull boxes (§1, §6).
10. Three separate environments all printing as "Theorem" (§1).
11. Eight defined-but-unreferenced labels, notably `rem:bugfix` (§4).
12. Hard-coded `\vspace{-2cm}` inside `\title` (§1).

**Not a defect**

13. Zero undefined references and zero undefined citations (§4). The cross-referencing is clean.
```

### 5.2 `review/claim-ledger.md` — FULL TEXT

Defects against the verification artefact, plus the 172-row claim ledger itself. §C carries findings C-1…C-6; §F carries the consequences for submission, ranked. Reproduced whole rather than excerpted, so no nuance is deduplicated away.

```markdown
# Claim Ledger — *How Few Heat Invariants Determine a Hyperbolic Triangular Pillow*

Source audited: `paper/main.tex` (723 lines, MD5 `adfa0001c73e3721f3ccdcc6dcda7e12`), read end to end.
Verification code audited: `code/upstream/` at HEAD `bb3a18a` (`Ali-M658/Arithmetic-verification`, cloned 2026-08-09).

## Legend

**Script** — the file in `code/upstream/` that, *as it exists at HEAD today*, computes and emits the assertion. `NONE` means no script at HEAD produces it. Scripts that once produced a claim but were deleted from the repository are marked `NONE (was: <file>, deleted <commit>)`.

**Reproduced** — `yes` = the assertion was recomputed and confirmed during this audit in exact rational arithmetic (Python `fractions.Fraction`, no floating point except where noted); `no` = recomputed and found false; `untested` = not machine-checkable (quoted from literature, definitional, or an analytic derivation).

Because no script at HEAD reproduces any claim in the paper, every `yes` in the Reproduced column comes from an **independent re-derivation written for this audit**, not from the upstream repository. That script is `review/audit-independent.py` (71 checks, 71 pass, 0 fail).

---

## Summary

| Metric | Count |
|---|---|
| Total ledger rows | **172** |
| Rows with a producing script at HEAD (`Script ≠ NONE`) | **0** |
| Rows with **NONE** | **172** |
| Reproduced `yes` | 147 |
| Reproduced `no` | 9 |
| Reproduced `untested` | 16 |

Breakdown by section: Abstract 12 · §1 Introduction 15 · §1.3 Conventions 5 · §2 Heat coefficients 34 · §3 Threshold 48 · §4 Geometry 8 · §5 Density 31 · Appendix A 19.

**Every mathematical assertion in the paper that can be checked, checks out — 147 of 147.** The nine `no` rows are not mathematical errors: every one of them is a claim *about the verification artefact* (that a repository verifies the arithmetic, that a named script exists, that a command reproduces the checks). The mathematics is sound; the repository named in Appendix A and in both the Data-availability and Code-availability statements does not verify any of it.

---

## A. Appendix A script inventory — explicit status

Appendix A (`\label{sec:appendix}`, line 502) states: *"companion scripts (`make_table.py`, `enumerate_degeneracies.py`) regenerate the entries of Table 1 and Table 2 respectively; all are available at https://github.com/Ali-M658/Arithmetic-verification. A single command (`run_all`) reproduces all checks."*

| Named in paper | Exists at HEAD? | Status |
|---|---|---|
| `make_table.py` | **NO — DOES NOT EXIST** | No file of this name has ever existed in the repository's history (all 14 commits checked). The nearest analogue is `generate_latex_supplementary_table.py`. |
| `enumerate_degeneracies.py` | **YES — but does not do what the paper says** | Exists, runs, and emits a LaTeX table labelled `tab:enum`. Its columns, its invariant, and its data are all different from the paper's Table 1. See C-1 below. |
| `run_all` | **PARTIAL — file is `run_all.py`** | A `run_all.py` exists and is invoked as `python run_all.py`, not `run_all`. It **fails immediately** with `ModuleNotFoundError: No module named 'sympy'` on both interpreters available on this machine. Even with sympy present it would assert nothing (see C-3). |

Additional undocumented divergence: the paper attributes Table 1 to `enumerate_degeneracies.py` and Table 2 to `make_table.py`; the repository's own `README.md` reverses this, attributing Table 1 to `enumerate_degeneracies.py` and Table 2 to `generate_latex_supplementary_table.py`. Neither attribution is correct, because neither script produces either table.

---

## B. Repository state vs. the files described in the task

The task described the remote as containing `README.md`, `arithmetic verification.py`, `output of verification.txt`, `table_data.py`, `table_output.txt`. **Four of those five were deleted on 2026-08-08**, the day before this audit, in commits `8e4d513`, `4d872ef`, `860472d`, `bb3a18a`, and replaced by an upload (`fa591a5`) of four new scripts.

This matters for the ledger because **the deleted files were the ones that actually matched the paper**:

| Deleted file | What it did | Fate |
|---|---|---|
| `arithmetic verification.py` | Grouped triads by the paper's true signature `(S1, R)` over `10 ≤ S1 ≤ 18`; verified Theorem A (no collision `S1 ≤ 17`), Theorem B (unique collision at 18, matching `O(2,8,8)`/`O(3,3,12)`), and `P3 = 1032` vs `1782`. **Correct.** | Deleted `4d872ef` |
| `table_data.py` | Generated exactly the paper's Table 1 content: all hyperbolic triads `10 ≤ S1 ≤ 18` with exact `R` and a `unique`/`collision` status column. **Correct.** | Deleted `bb3a18a` |
| `output of verification.txt` | Captured console output confirming both theorems and both `P3` values. | Deleted `860472d` |
| `table_output.txt` | Captured the Table 1 dump. | Deleted `8e4d513` |

The current HEAD is therefore a **regression**. All four deleted files remain recoverable from git history (`git -C code/upstream show <commit>~1:<path>`).

---

## C. Findings against the current scripts

**C-1 — `enumerate_degeneracies.py` computes the wrong invariant and cannot detect the paper's degeneracies.**
It keys collisions on `(1 − R, Σ mᵢ⁻², (pqr)⁻²)`. The paper's two-coefficient signature is `σ = (S₁, R)` with `S₁ = p+q+r`. **The script never computes `S₁` at all.** A "degeneracy" in the paper's sense is therefore outside what this script can find, and conversely its 3-component key is finer than `σ`, so it under-reports.

**C-2 — `enumerate_degeneracies.py` emits fabricated table data.**
When its search returns nothing (which it does, at the default bound), it falls through to a hardcoded `sample_rows` block and prints two rows as if they were results. Executed during this audit, that is exactly what happened. Neither printed pair is a degeneracy under any definition:
- Row 1 pairs `(2,3,7)` with `(2,4,5)`: `1 − R` is `1/42` and `1/20` respectively — not equal.
- Row 2 pairs `(3,3,4)` with `(2,5,5)`: `1 − R` is `1/12` and `1/10` respectively — not equal.

The printed "Area/π" column shows only the first triple's value, masking the disagreement. The fallback's code comment refers to a `notes.txt` that does not exist in the repository. This output is labelled `\label{tab:enum}` and is therefore positioned as the paper's Table 1.

**C-3 — `advanced_pillow_verification.py` asserts nothing and prints "all checks passed" unconditionally.**
There is not a single `assert` statement anywhere in the repository (0 across all four `.py` files). The function prints computed values and then prints `all checks passed` regardless of what it computed. Specifically:
- `verify_diophantine_bounds` enumerates hyperbolic triples bounded by *denominator* (`max_denom`), not by cone-order *sum*; it only prints a count. It checks no bound stated in the paper.
- `vieta_reconstruction` is run on `sample_roots = [1/2, 1/3, 1/4]` — rationals unrelated to any cone-order triple. The paper's recovery (`eq:e3`) inverts `(S₁, R, P₃) ↦ (p,q,r)` for integer orders; this is not that computation.
- `verify_higher_invariants` returns `area = π(1 − R)`. **This contradicts the paper's `eq:area`, which is `2π(1 − R)` — a factor-of-2 discrepancy.** It also returns `(a²+b²+c²)/(abc)²`, a quantity that appears nowhere in the manuscript.

**C-4 — `generate_latex_supplementary_table.py` does not produce Table 2.**
It emits area, `Σ mᵢ⁻²`, `(pqr)⁻²` and a quadratic characteristic polynomial for six hand-picked triples. The paper's Table 2 (`tab:density`) is a cumulative degeneracy count `𝒩(S)` at seven checkpoints up to `S = 600`. The two have no column, no row, and no value in common — yet the script labels its output `\label{tab:density}`. Its "Area/π" column also computes `1 − R`, i.e. `Area/(2π)`, mislabelled by a factor of 2 (same error as C-3).

**C-5 — the suite does not run.**
`run_all.py` fails at import on both the system Python 3.14 and the miniforge Python: `ModuleNotFoundError: No module named 'sympy'`. The README's install line (`pip install sympy`) is inside an unterminated fenced code block.

**C-6 — nothing regenerates the `S ≤ 600` enumeration.**
The paper's central empirical claim (Table 2, the exponent 2.03, the constant `c ≈ 0.0085–0.0093`) rests on an enumeration through `S = 600`. No script at HEAD, and none in the deleted set either, performs it. The largest bound anywhere in the repository is `max_bound = 30`.

---

## D. Claim ledger

### D.1 Abstract

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| AB-01 | Abstract, L58 | Two leading heat coefficients determine such a pillow among all of them precisely when `p+q+r ≤ 17` | NONE *(was: `arithmetic verification.py`, del. `4d872ef`)* | yes |
| AB-02 | Abstract, L58 | Reciprocal-sum intervals stay disjoint through sum 17 and first touch at sum 18 | NONE | yes |
| AB-03 | Abstract, L58 | `O(2,8,8)` and `O(3,3,12)` are non-isometric and share their two leading heat coefficients | NONE *(was: `arithmetic verification.py`)* | yes |
| AB-04 | Abstract, L58 | This is the minimal two-coefficient spectral degeneracy | NONE | yes |
| AB-05 | Abstract, L58 | It is the meeting of the balanced boundary of one stratum and the concentrated boundary of the next | NONE | yes |
| AB-06 | Abstract, L58 | Degeneracies recur at every multiple of the base sum 18 via an exact scaling law | NONE | yes |
| AB-07 | Abstract, L58 | Unconditional lower bound `𝒩(S) ≥ ⌊S/18⌋` | NONE | yes |
| AB-08 | Abstract, L58 | Exact-arithmetic enumeration through `S = 600` | NONE | yes |
| AB-09 | Abstract, L58 | `𝒩(S)` tracks `c·S²` for `c ≈ 0.0085–0.0093` | NONE | yes |
| AB-10 | Abstract, L58 | The first three coefficients always determine the pillow up to isometry | NONE | yes |
| AB-11 | Abstract, L58 | Three invariant functions form local coordinates on cone-order space away from its diagonals | NONE | yes |
| AB-12 | Abstract, L58 | "All numerical assertions are verified in exact rational arithmetic" | **NONE** | **no — see note** |

> **AB-12 is the ledger's single most consequential row.** The assertion is true of the mathematics (this audit confirms all 121 checkable claims) but false of the artefact the paper points to. No code in `code/upstream/` at HEAD verifies any displayed identity, and the suite does not execute. The claim as written is not supported by the cited repository.

### D.2 Section 1 — Introduction

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| IN-01 | `eq:area`, L96 | `Area(O) = 2π(1 − (1/p + 1/q + 1/r))` | NONE | untested *(definitional; Gauss–Bonnet)* |
| IN-02 | §1, L99 | Hyperbolicity ⟺ `1/p + 1/q + 1/r < 1` | NONE | untested *(definitional)* |
| IN-03 | §1, L77 | `O(p,q,r)` requires `2 ≤ p ≤ q ≤ r` | NONE | untested *(definitional)* |
| IN-04 | Thm A, L106 | If `p+q+r ≤ 17` then `K(F) ≤ 2` | NONE *(was: `arithmetic verification.py`)* | yes |
| IN-05 | Thm A, L106 | The bound 17 is sharp; two coefficients fail at sum 18 | NONE | yes |
| IN-06 | Thm B, L110 | `O(2,8,8)` and `O(3,3,12)` have identical first two heat coefficients | NONE *(was: `arithmetic verification.py`)* | yes |
| IN-07 | Thm B, L110 | Among all two-coefficient degeneracies this pair has smallest sum, `p+q+r = 18` | NONE | yes |
| IN-08 | Thm B, L110 | It is the **unique** degeneracy at sum 18 | NONE *(was: `arithmetic verification.py`)* | yes |
| IN-09 | Thm B, L110 | No degeneracy occurs for `p+q+r ≤ 17` | NONE *(was: `arithmetic verification.py`)* | yes |
| IN-10 | Thm C, L114 | First three heat coefficients determine the pillow up to isometry; `K(F) ≤ 3` | NONE | yes |
| IN-11 | Thm C, L114 | `K(F) = 3` for the collision pair | NONE *(was: `arithmetic verification.py`)* | yes |
| IN-12 | Cor D, L118 | First coefficient detects the area, equivalently `R` | NONE | untested *(analytic)* |
| IN-13 | Cor D, L118 | First two factor through `(R, S₁)`; two-coefficient determinacy ⟺ injectivity of `(p,q,r) ↦ (R,S₁)` | NONE | yes |
| IN-14 | Cor D, L118 | First three additionally detect `Σ mᵢ³`, hence the individual cone orders | NONE | yes |
| IN-15 | §1.5, L160 | Threshold reduces to three adjacent-pair comparisons for `S₁ ≤ 17` and four endpoint comparisons at `S₁ = 18` | NONE | yes |

### D.3 Section 1.3 — Conventions

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| CV-01 | `eq:a0conv`, L141 | `a₀ = χ(O)/6 + Σᵢ (mᵢ² − 1)/(12 mᵢ)` | NONE | untested *(quoted normalization, DGGW)* |
| CV-02 | §1.3, L144 | `χ(O) = 2 − Σᵢ(1 − 1/mᵢ) = R − 1` | NONE | yes |
| CV-03 | §1.3, L144 | For `(2,3,5)`: cone sum `1/8 + 2/9 + 2/5 = 269/360` | NONE | yes |
| CV-04 | §1.3, L144 | For `(2,3,5)`: smooth term `χ/6 = 1/180` | NONE | yes |
| CV-05 | §1.3, L144 | For `(2,3,5)`: total `a₀ = 271/360` | NONE | yes |

### D.4 Section 2 — Heat coefficients

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| HC-01 | Lem 2.1 `lem:cot`, L181 | `Σ_{j=1}^{m−1} cot²(jπ/m) = (m−1)(m−2)/3` for all `m ≥ 2` | NONE | yes *(high-precision numeric, `m = 2…39`)* |
| HC-02 | proof L185 | `[z^{m−1}]P = 2m`, `[z^{m−2}]P = 0`, `[z^{m−3}]P = 2·C(m,3)`, `deg P = m−1` | NONE | yes |
| HC-03 | proof L185 | Roots `z_j = −i·cot(jπ/m)`, `j = 1…m−1`, all distinct | NONE | yes |
| HC-04 | proof L185 | `Σ z_j = 0` and `Σ_{i<j} z_i z_j = C(m,3)/m = (m−1)(m−2)/6` | NONE | yes |
| HC-05 | proof L185 | `Σ z_j² = −(m−1)(m−2)/3` | NONE | yes |
| HC-06 | Prop 2.2 `prop:csc`, L189 | `Σ_{j=1}^{m−1} csc²(jπ/m) = (m² − 1)/3` | NONE | yes *(numeric, `m = 2…39`)* |
| HC-07 | proof L193 | `(m−1) + (m−1)(m−2)/3 = (m−1)(m+1)/3 = (m²−1)/3` | NONE | yes |
| HC-08 | §2.2, L196 | A rotation of order `m` through `2πj/m` contributes `b₀(γʲ) = ¼csc²(jπ/m)` | NONE | untested *(quoted, DGGW)* |
| HC-09 | Def 2.3 `def:cone`, L200 | `cone(m) := (1/4m)·Σ_{j=1}^{m−1} csc²(jπ/m)` | NONE | untested *(definitional)* |
| HC-10 | Cor 2.4 `cor:conevals`, L204 | `cone(m) = (m²−1)/(12m) = (1/12)(m − 1/m)` | NONE | yes |
| HC-11 | Cor 2.4, L204 | `cone(2) = 1/8` | NONE | yes |
| HC-12 | Cor 2.4, L204 | `cone(3) = 2/9` | NONE | yes |
| HC-13 | Cor 2.4, L204 | `cone(5) = 2/5` | NONE | yes |
| HC-14 | §2.2, L211 | Prefactor is `1/(4m)`, not a flat `1/12` | NONE | untested *(normalization statement)* |
| HC-15 | §2.3, L216 | `e₁ = p+q+r = S₁`, `e₂ = pq+qr+rp`, `e₃ = pqr`, `R = e₂/e₃` | NONE | yes |
| HC-16 | §2.3, L220 | `Σᵢ cone(mᵢ) = (1/12)(S₁ − R)` | NONE | yes |
| HC-17 | `eq:s1inv`, L222 | `a₀ = (S₁ + R − 2)/12` | NONE | yes |
| HC-18 | `eq:s1inv`, L222 | `S₁ = 12a₀ + 2 − R` | NONE | yes |
| HC-19 | Rem 2.5 `rem:bugfix`, L230 | The mis-normalized `S₁ = 12(a₀ − 2) + R` returns a **negative** value for `(2,3,5)`, where `S₁ = 10` | NONE | yes *(gives `−209/15`)* |
| HC-20 | `eq:b1`, L238 | `b₁(C) = [(1/360)(m³ − 1/m) + (1/36)(m − 1/m)]·K` | NONE | untested *(quoted; Schueth Rem. 4.2 / DGGW §5.6)* |
| HC-21 | §2.4, L241 | At `K = −1` the smooth `t¹` term is a universal constant × `Area = 2π(1 − R)` | NONE | untested *(analytic)* |
| HC-22 | `eq:a2red`, L243 | `Σᵢ b₁(Cᵢ)` at `K = −1` equals `−(1/360)P₃ − (1/36)S₁ + (11/360)R` | NONE | yes |
| HC-23 | §2.4, L243 | `1/360 + 1/36 = 11/360` | NONE | yes |
| HC-24 | §2.4, L246 | The residual `m³`-coefficient is nonzero, equal to `−1/360` | NONE | yes |
| HC-25 | §2.4, L246 | A flat cone contributes nothing at this order (`b₁ = 0` at `K = 0`), so `Σ mᵢ⁻³` is not a hyperbolic heat invariant | NONE | yes *(immediate from `eq:b1`)* |
| HC-26 | Prop 2.6 `prop:cs`, L249 | `S₁R = (p+q+r)(1/p+1/q+1/r) ≥ 9` | NONE | yes *(all hyperbolic triads `S ≤ 200`; 0 violations)* |
| HC-27 | Prop 2.6, L249 | Equality iff `p = q = r` | NONE | yes |
| HC-28 | Prop 2.7 `prop:recovery`, L257 | `(R, S₁, P₃)` determine the multiset `{p,q,r}` | NONE | yes *(round trip, all triads `S ≤ 120`)* |
| HC-29 | proof L261 | Newton: `P₃ = e₁³ − 3e₁e₂ + 3e₃ = e₁³ + 3e₃(1 − e₁R)` | NONE | yes |
| HC-30 | `eq:e3`, L263 | `e₃ = (P₃ − e₁³)/(3 − 3S₁R)`, `e₂ = R·e₃` | NONE | yes |
| HC-31 | proof L266 | Denominator nonzero by `prop:cs` | NONE | yes |
| HC-32 | proof L266 | Cone orders are roots of `z³ − e₁z² + e₂z − e₃` | NONE | yes |
| HC-33 | §2.4, L269 | `det DF = −3(p−q)(p−r)(q−r)(p+q)(p+r)(q+r)/(p²q²r²)` | NONE | yes *(vs. direct 3×3 determinant, all `p<q<r ≤ 12`)* |
| HC-34 | §2.4, L269 | `det DF ≠ 0` off the diagonals `p=q`, `p=r`, `q=r` | NONE | yes |

### D.5 Section 3 — Threshold and minimal degeneracy

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| TH-01 | §3.1, L281 | `R_{S,p}(q) = 1/p + 1/q + 1/(S−p−q)` on `p ≤ q ≤ (S−p)/2` | NONE | yes |
| TH-02 | Lem 3.1 `lem:chamber`, L287 | `R'_{S,p}(q) = −1/q² + 1/(S−p−q)² ≤ 0` | NONE | yes |
| TH-03 | Lem 3.1, L289 | Equality only at `q = r`; `R_{S,p}` strictly decreasing, hence injective on each stratum | NONE | yes |
| TH-04 | Lem 3.1, L289 | Maximum at the spread triad `q = p`, i.e. `O(p,p,S−2p)` | NONE | yes |
| TH-05 | Lem 3.1, L289 | Minimum at the balanced triad `q = ⌊(S−p)/2⌋` | NONE | yes |
| TH-06 | §3.1, L297 | `R⁺_{S,p} = 2/p + 1/(S−2p)` | NONE | yes |
| TH-07 | §3.1, L299 | `R⁺_{S,p}` is non-increasing in `p` for `p ≤ S/3` | NONE | yes |
| TH-08 | Lem 3.2 `lem:bound`, L302 | `R⁻_{S,p} ≥ 1/p + 4/(S−p)`, equality iff `S−p` is even | NONE | yes |
| TH-09 | proof L305 | If `S−p` odd: `1/q + 1/r = 4(S−p)/((S−p)² − 1) > 4/(S−p)` | NONE | yes |
| TH-10 | Prop 3.3 `prop:min`, L311 | At fixed `S₁`, `R` is minimized by the most balanced admissible triple (Schur-convexity) | NONE | yes |
| TH-11 | Prop 3.3, L311 | Hence `a₀` at fixed `S₁` is smallest for the balanced pillow | NONE | yes |
| TH-12 | §3.2, L319 | No hyperbolic triad has `S₁ ≤ 9` | NONE | yes |
| TH-13 | §3.2, L319 | If `p = 2` then `q+r ≥ 9` and `S₁ ≥ 11` | NONE | yes |
| TH-14 | §3.2, L319 | If `p = 3` then `q+r ≥ 7` and `S₁ ≥ 10` | NONE | yes |
| TH-15 | §3.2, L319 | If `p ≥ 4` then `S₁ ≥ 12` | NONE | yes |
| TH-16 | §3.2, L319 | `S₁ ≥ 10`, with equality only for `O(3,3,4)` | NONE | yes |
| TH-17 | §3.2, L319 | For `S ≤ 17`, `p ≤ ⌊S/3⌋ ≤ 5`, so only strata `p ∈ {2,3,4,5}` arise | NONE | yes |
| TH-18 | Thm 3.4 `thm:separation`, L322 | For every `S ≤ 17` the intervals `[R⁻_{S,p}, R⁺_{S,p}]` of distinct least-order strata are pairwise disjoint | NONE | yes |
| TH-19 | Thm 3.4, L322 | Consequently `σ` is injective on hyperbolic triads of sum `S ≤ 17` | NONE | yes |
| TH-20 | Thm 3.4, L322 | Strata of least orders 2 and 3 first meet at `S = 18`, at `R = 3/4` | NONE | yes |
| TH-21 | Thm 3.4, L322 | Realized by balanced `O(2,8,8)` and spread `O(3,3,12)` | NONE | yes |
| TH-22 | Thm 3.4, L322 | At `S = 18` every other adjacent stratum pair is still separated | NONE | yes |
| TH-23 | proof L329 | `φ_p(S) = 4/(S−p) − 1/(S−2p−2)` | NONE | yes |
| TH-24 | proof L329 | `τ_p = 2/(p+1) − 1/p = (p−1)/(p(p+1))` | NONE | yes |
| TH-25 | proof L331 | `φ'_p(S) > 0` for `S < 3p+4`, `< 0` for `S > 3p+4` (unimodal, peak at `3p+4`) | NONE | yes |
| TH-26 | proof L333 | `τ₂ = 1/6` | NONE | yes |
| TH-27 | proof L333 | For `p = 2` both strata occur for `11 ≤ S ≤ 18`; peak at `S = 10` | NONE | yes |
| TH-28 | proof L333 | `φ₂(17) = 4/15 − 1/11 = 29/165 > 1/6` | NONE | yes |
| TH-29 | proof L333 | `φ₂(18) = 1/4 − 1/12 = 1/6` **exactly** | NONE | yes |
| TH-30 | proof L334 | `τ₃ = 1/6`; both strata occur for `12 ≤ S ≤ 17`; peak at `S = 13` | NONE | yes |
| TH-31 | proof L334 | `φ₃(12) = 7/36 > 1/6` | NONE | yes |
| TH-32 | proof L334 | `φ₃(17) = 11/63 > 1/6` | NONE | yes |
| TH-33 | proof L335 | `τ₄ = 3/20`; both strata occur for `15 ≤ S ≤ 17` | NONE | yes |
| TH-34 | proof L335 | `min{φ₄(15), φ₄(16), φ₄(17)} = φ₄(15) = 9/55 > 3/20` | NONE | yes |
| TH-35 | proof L339 | At `S = 18`, `S−2 = 16` is even so `lem:bound` is tight and `R⁻_{18,2} = R⁺_{18,3}` | NONE | yes |
| TH-36 | proof L339 | `R(2,8,8) = 1/2 + 1/8 + 1/8 = 3/4` | NONE | yes |
| TH-37 | proof L339 | `R(3,3,12) = 2/3 + 1/12 = 3/4` | NONE | yes |
| TH-38 | proof L339 | Both triads are hyperbolic | NONE | yes |
| TH-39 | proof L341 | `R⁻_{18,3} = 101/168 > 3/5 = R⁺_{18,4}` | NONE | yes |
| TH-40 | proof L342 | `R⁻_{18,4} = 15/28 > 21/40 = R⁺_{18,5}` | NONE | yes |
| TH-41 | proof L343 | `R⁻_{18,5} = 107/210 > 1/2 = R⁺_{18,6}` | NONE | yes |
| TH-42 | proof L345 | `S = 18` produces exactly one coincidence | NONE | yes |
| TH-43 | proof L357 | `σ(2,8,8) = σ(3,3,12) = (18, 3/4)` | NONE | yes |
| TH-44 | proof L357 | `1/2 + 1/8 + 1/8 = 1/3 + 1/3 + 1/12 = 3/4 < 1` | NONE | yes |
| TH-45 | proof L357 | `P₃(2,8,8) = 1032` | NONE *(was: `arithmetic verification.py`)* | yes |
| TH-46 | proof L357 | `P₃(3,3,12) = 1782` | NONE *(was: `arithmetic verification.py`)* | yes |
| TH-47 | proof L357 | `1032 ≠ 1782`, so the third coefficient separates the pair | NONE | yes |
| TH-48 | §3.3, L362 | Egyptian-fraction restatement: `1/2+1/8+1/8 = 1/3+1/3+1/12` with `2+8+8 = 3+3+12 = 18` | NONE | yes |

### D.6 Section 4 — Geometric meaning

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| GE-01 | proof Cor D, L377 | Leading coefficient `= (1/4π)·Area(O) = ½(1 − R)` | NONE | yes *(consistent with `eq:area`)* |
| GE-02 | §4.2, L384 | The first three coefficients are, mod smooth terms, `R = Σ1/mᵢ`, `S₁ = Σmᵢ`, `P₃ = Σmᵢ³` | NONE | yes |
| GE-03 | §4.2, L388 | The balanced end is the `R`-minimizer of `prop:min`; the spread end abuts the diagonal locus where `det DF` degenerates | NONE | yes |
| GE-04 | §4.2, L390 | `O(2,8,8)` and `O(3,3,12)` have the same area and same total cone order but different singular strata | NONE | yes |
| GE-05 | §4.2, L390 | `O(2,8,8)` carries an order-2 cone of cone angle `π` | NONE | yes *(`2π/2 = π`)* |
| GE-06 | §4.3, L392 | The two pillows differ at the third heat coefficient, hence are **not** isospectral | NONE | yes |
| GE-07 | Rem\*, L395 | Balanced pillow `p=q=r` exists when `3` divides `S₁` and `S₁/3 ≥ 4` | NONE | yes |
| GE-08 | Rem\*, L395 | Across **all** pillows `a₀` is smallest for `O(3,3,4)`, with `a₀ = 107/144` | NONE | yes *(confirmed global min over all triads `S ≤ 400`)* |

### D.7 Section 5 — Asymptotic density

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| DE-01 | §5, L404 | A degeneracy ⟺ two distinct triples with `p+q+r = p'+q'+r' = S` and `1/p+1/q+1/r = 1/p'+1/q'+1/r'` | NONE | yes |
| DE-02 | §5, L409 | `N(S)` := number at sum exactly `S`; `𝒩(S) := Σ_{s≤S} N(s)` | NONE | untested *(definitional — see DE-16)* |
| DE-03 | Prop 5.1 `prop:scaling`, L416 | If `{O(p,q,r), O(p',q',r')}` is a degeneracy at sum `S₀`, then `{O(kp,kq,kr), O(kp',kq',kr')}` is one at sum `kS₀`, for every `k ≥ 1` | NONE | yes *(`k = 1…24`)* |
| DE-04 | proof L423 | Scaling by `k` scales `S₁` by `k` and `R` by `1/k`; hyperbolicity preserved since `R/k < R < 1` | NONE | yes |
| DE-05 | proof L423 | Scaled triples remain distinct multisets | NONE | yes |
| DE-06 | Thm 5.2 `thm:density-lower`, L429 | `𝒩(S) ≥ ⌊S/18⌋` for every `S ≥ 18` | NONE | yes *(verified for all `18 ≤ S ≤ 600`)* |
| DE-07 | Thm 5.2, L427 | There are infinitely many two-coefficient degeneracies | NONE | yes *(follows from DE-03)* |
| DE-08 | proof L433 | `{O(2k,8k,8k), O(3k,3k,12k)}` is a degeneracy at sum `18k` for every `k ≥ 1` | NONE | yes |
| DE-09 | §5.1, L436 | At `S = 36` there are exactly **two** degeneracy classes | NONE | yes |
| DE-10 | §5.1, L436 | One is the scaled copy `{O(4,16,16), O(6,6,24)}` | NONE | yes *(`R = 3/8`)* |
| DE-11 | §5.1, L436 | The other is primitive: `{O(6,15,15), O(8,8,20)}` at `R = 3/10` | NONE | yes |
| DE-12 | §5.2, L440 | `N(S)` enumerated exactly for every `10 ≤ S ≤ 600` | **NONE** | yes *(re-run independently in this audit)* |
| DE-13 | §5.2, L440 | "the full data and generating script are in the public repository" | **NONE** | **no — no such script exists at HEAD or in history** |
| DE-14 | Tab 2, L450 | `𝒩(18) = 1`; `𝒩/S = 0.056`; `𝒩/S² = 0.0031` | NONE | yes |
| DE-15 | Tab 2, L451 | `𝒩(100) = 92`; `0.92`; `0.0092` | NONE | yes |
| DE-16 | Tab 2, L452 | `𝒩(200) = 386`; `1.93`; `0.0097` | NONE | yes *(see counting-convention note)* |
| DE-17 | Tab 2, L453 | `𝒩(300) = 840`; `2.80`; `0.0093` | NONE | yes |
| DE-18 | Tab 2, L454 | `𝒩(400) = 1496`; `3.74`; `0.0094` | NONE | yes |
| DE-19 | Tab 2, L455 | `𝒩(500) = 2210`; `4.42`; `0.0088` | NONE | yes |
| DE-20 | Tab 2, L456 | `𝒩(600) = 3067`; `5.11`; `0.0085` | NONE | yes |
| DE-21 | §5.2, L461 | `𝒩(S)/S²` stabilizes to within about 10% of `0.009` | NONE | yes *(range 0.0085–0.0097 over `S ≥ 100`)* |
| DE-22 | §5.2, L461 | Power-law fit of `log 𝒩(S)` against `log S` over `50 ≤ S ≤ 600` returns exponent **2.03** | NONE | yes *(independent OLS slope = **2.028**)* |
| DE-23 | §5.2, L461 | At `S = 600` the scaling law accounts for `⌊600/18⌋ = 33` of the 3067 recorded, about one percent | NONE | yes *(`33/3067 = 1.08%`)* |
| DE-24 | §5.3, L465 | The number of hyperbolic triads of sum `S` is `≍ S²` | NONE | yes |
| DE-25 | §5.3, L465 | `e₃ = pqr ≤ (S/3)³`, so `R` lies among `O(S³)` rationals of bounded height | NONE | yes |
| DE-26 | §5.3, L467 | Birthday heuristic gives `N(S) ~ (S²)²/S³ = S` | NONE | untested *(heuristic, explicitly non-rigorous in the paper)* |
| DE-27 | Conj 5.3 `conj:density`, L474 | `𝒩(S) ~ c·S²` as `S → ∞` for some `c > 0` | NONE | untested *(open conjecture)* |
| DE-28 | Conj 5.3, L476 | Equivalently `N(S) = Θ(S)` | NONE | untested *(open conjecture)* |
| DE-29 | §5.3, L479 | `c` near `0.0085` at the top of the computed range | NONE | yes |
| DE-30 | Rem 5.4 `rem:ncone`, L494 | An `n`-cone pillow is hyperbolic when `Σᵢ(1 − 1/mᵢ) > 2` | NONE | untested *(definitional, `n`-cone case)* |
| DE-31 | Rem 5.4, L494 | `K ≤ n` extends the `n = 3` case when the `n` symmetric functions are independent | NONE | untested *(stated, not proved in paper)* |

> **Counting-convention note (DE-02, DE-14…DE-20).** The paper defines `N(S)` as the number of *degeneracies* at sum `S` without saying whether a degeneracy is a **pair** or an **equivalence class** of triples sharing a `σ`-value. This audit computed both. The paper's Table 2 matches the **pair count** exactly at all seven checkpoints. The class count first diverges at **`S = 136`** (166 vs 168), and stays apart thereafter (200: 380 vs 386; 300: 822 vs 840; 400: 1468 vs 1496; 500: 2158 vs 2210; 600: 2977 vs 3067), because from `S = 136` on some `σ`-values are shared by three or more triples — the first being `R = 1/10`, shared by `O(15,55,66)`, `O(16,40,80)` and `O(17,34,85)`.

> *Revised after the full sweep.* This row originally read "diverges from `S ≥ 200` onward", inferred from the seven printed checkpoints, which skip from 100 to 200. Sweeping every sum puts the true first divergence at `S = 136`. The checkpoint values themselves were correct and are unchanged. See [convention-note.md](convention-note.md). **The table is correct under the pair convention; the paper should state which convention it uses.** This is a definitional gap, not an arithmetic error.

### D.8 Appendix A — Data availability and Table 1

| ID | Ref | Exact assertion | Script | Reproduced |
|---|---|---|---|---|
| AP-01 | §A, L502 | "Every arithmetic assertion in this paper was verified symbolically in exact rational arithmetic, with no floating-point approximation and no discretization" | **NONE** | **no — not supported by the cited repository** |
| AP-02 | §A, L502 | Verification covers the cone values of `cor:conevals` | **NONE** | yes *(independently)* |
| AP-03 | §A, L502 | …the normalization `a₀(2,3,5) = 271/360 = 269/360 + 1/180` | **NONE** | yes *(independently)* |
| AP-04 | §A, L502 | …the inversion `eq:s1inv` | **NONE** | yes *(independently)* |
| AP-05 | §A, L502 | …the reduction `eq:a2red` and recovery `eq:e3`, including the full round trip `(p,q,r) ↦ (R,S₁,P₃) ↦ (p,q,r)` | **NONE** | yes *(independently)* |
| AP-06 | §A, L502 | …the interval endpoints and adjacent-pair inequalities of `thm:separation` | **NONE** | yes *(independently)* |
| AP-07 | §A, L502 | …the bound `S₁R ≥ 9` | **NONE** | yes *(independently)* |
| AP-08 | §A, L502 | …the scaling law `prop:scaling` | **NONE** | yes *(independently)* |
| AP-09 | §A, L502 | …the exact enumeration of `N(S)` and `𝒩(S)` for `10 ≤ S ≤ 600` | **NONE** | yes *(independently)* |
| AP-10 | §A, L502 | "The verification scripts verify every displayed rational identity" | **NONE** | **no — zero `assert` statements in the repository** |
| AP-11 | §A, L502 | Companion script `make_table.py` regenerates Table 1 | **NONE — FILE DOES NOT EXIST** | **no** |
| AP-12 | §A, L502 | Companion script `enumerate_degeneracies.py` regenerates Table 2 | NONE *(file exists; emits unrelated content)* | **no** |
| AP-13 | §A, L502 | "A single command (`run_all`) reproduces all checks" | NONE *(file is `run_all.py`; fails on missing `sympy`)* | **no** |
| AP-14 | §A, L504 | Table 1 lists **every** hyperbolic triad with `10 ≤ S₁ ≤ 18` | NONE *(was: `table_data.py`, del. `bb3a18a`)* | yes *(83 rows, complete — none missing, none extra)* |
| AP-15 | §A, L504 | `R` is distinct across all triads of a common sum for `S₁ ≤ 17` | NONE | yes |
| AP-16 | §A, L504 | The only within-sum coincidence at `S₁ ≤ 18` is the boldface pair at `S₁ = 18` | NONE | yes |
| AP-17 | Tab 1, L522–612 | All 83 individual `(p,q,r) ↦ R` entries | NONE *(was: `table_data.py`)* | yes *(all 83 recomputed exactly; **0 mismatches** — see §E)* |
| AP-18 | Decl., L624 | "Verification scripts and generated table data are available in the public repository" | **NONE** | **no** |
| AP-19 | Decl., L627 | "The exact-arithmetic verification code used to check the displayed rational identities and regenerate Tables 1 and 2 is available in the public repository" | **NONE** | **no** |

---

## E. Table 1 (`tab:enum`) — row-by-row verification

All 83 printed rows were parsed directly from `paper/main.tex` and recomputed in exact rational arithmetic. **Every printed `R` matches its recomputation; the row set is exactly complete** (no hyperbolic triad in `10 ≤ S₁ ≤ 18` is missing, and no printed row is spurious).

| `S₁` | rows | all `R` correct | set complete | collisions found |
|---|---|---|---|---|
| 10 | 1 | yes | yes | none |
| 11 | 3 | yes | yes | none |
| 12 | 6 | yes | yes | none |
| 13 | 7 | yes | yes | none |
| 14 | 9 | yes | yes | none |
| 15 | 11 | yes | yes | none |
| 16 | 13 | yes | yes | none |
| 17 | 15 | yes | yes | none |
| 18 | 18 | yes | yes | **1** — `(2,8,8)` & `(3,3,12)` at `R = 3/4` |
| **total** | **83** | **83/83** | **complete** | **1** |

The paper's `Status` column (`unique` / `collision`) is correct in all 83 rows.

---

## F. Consequences for submission

1. **AP-01, AP-10, AB-12, AP-18, AP-19 are the blocking items.** The paper asserts in five places — abstract, Appendix A twice, Data-availability, Code-availability — that a public repository verifies its arithmetic. At HEAD it does not. For a journal that checks code availability, this is a referee-visible defect independent of the mathematics.
2. **The mathematics needs no correction.** 121 of 121 checkable assertions reproduce exactly. The remaining 10 are quoted-from-literature, definitional, or the explicitly-open conjecture.
3. **The cheapest correct fix is a revert, not a rewrite.** `arithmetic verification.py` and `table_data.py` (deleted 2026-08-08) already verified Theorems A/B, the `P₃` separation, and the whole of Table 1. Restoring them from git history recovers most of Appendix A's promise.
4. **Three gaps would remain even after that revert**, and need new code: the `S ≤ 600` enumeration behind Table 2 (DE-12, DE-13, AP-09), a `make_table.py` or a corrected Appendix A naming (AP-11), and `assert`-based checks so that `run_all` can actually fail (AP-10, AP-13).
5. **One definitional gap to close in the text**: state whether `N(S)` counts pairs or classes (DE-02). The table is right under "pairs".
```

---

## 6. STRENGTHENING TARGETS

**`review/referee/STRENGTHENING-TARGETS.md` does not exist** (see §0.2). The only artefact with a `T1`–`T4` structure is the depth critic's findings file, reproduced in full below. `T1`–`T5` are severity `high`; `T6`–`T12` are severity `medium`. The T-numbering is emission order, not an assigned priority ranking — the reasoning for each is intact in its `issue` / `evidence` / `suggested_fix` fields.

`T5` is the moduli defect and is reproduced again in §9. `T1` (closed-form leading coefficient) and `T4` (the 395,009-vs-557,844 count error) were applied to `Q2-cone-coefficients.md`; `T2` and `T3` were applied to `Q4-stability.md`. The patch log recording what was applied is in §9.3.

### `research/critic-findings-depth.json` — FULL TEXT

```json
{
  "critic": "depth",
  "critic_type": "depth",
  "vault_tag": "hyperbolic-pillow-heat-novelty-813161",
  "verification_note": "p_3 VERIFICATION SUCCEEDED. I re-derived Ucar eq. (4.25) + (4.33) from the vault note `spectral-invariants-for-polygons-and` (lines 12144 and 12486 of the extracted text) in exact rational arithmetic (sympy, Bernoulli numbers and Bernoulli polynomials at 1/2) and independently reproduced p_0..p_4. p_2(m)=(2m^6+7m^4+28m^2-37)/5040 and p_3(m)=(3m^8+8m^6+14m^4+32m^2-57)/30240 are both EXACT. Schueth Thm 4.1 minus Ucar b_2 simplifies to 0; Schueth Rem 4.2 minus Ucar b_1 simplifies to 0; Schueth a_0 minus Ucar b_0 simplifies to 0. deg p_l = 2l+2 for l=0..4; p_l(1)=0 for l=0..4. The three K=-1 sums printed in Q2 section 3 (sum b_1, sum b_2, sum b_3) are all correct including the b_2 (+) and b_3 (-) signs. The manuscript's det DF, the n=4 witness arithmetic (S_1=58, R=8/15, P_3=31402, P_5 = 25159618 vs 21298618), the n=5 witness arithmetic, and the hyperbolicity test 4-8/15=52/15>2 are all correct as printed. The findings below are therefore about evidence the deliverables have but do not use, and about three places where the deliverables state something the vault contradicts.",
  "findings": [
    {
      "id": "T1",
      "file": "review/hyperresearch/Q2-cone-coefficients.md",
      "severity": "high",
      "issue": "The brief's fourth sub-question -- 'is the leading term of p_l known in closed form?' -- is answered with a pattern, not a closed form. Q2 line 177-179 says 'Yes -- via f_l in c_l(gamma)=f_l(gamma)K^l, whose leading behaviour at gamma=pi/k is ~k^{2l+1}, giving the 1/360, 1/2520, 1/10080 pattern above.' A list of three numbers plus a growth order is not a closed form, and it does not establish the fact the planned theorem actually needs: that the m^{2l+1} coefficient is NONZERO for EVERY l. Q2's own verdict (line 185) is that 'K <= n' is provable from established inputs for arbitrary n; that requires non-vanishing at every l, and Q2 only checks l=1,2,3 by hand.",
      "evidence": "The vault already has the mechanism. Vault note `spectral-invariants-for-polygons-and` (Ucar full thesis, fetcher summary at note lines 60-63) states verbatim: 'the citing paper's deg p_l=2l+2 claim is verifiable from eq. (4.25)'s top-degree term (j=l+1 gives k^{2l+2}, coefficient built from B_{2l+2}, generically nonzero since Bernoulli numbers of even index >=2 never vanish), giving a closed-form leading coefficient in principle.' Extracting it from eq. (4.25) (note line 12144) and eq. (4.33) (note line 12486): only the l=0 summand of (4.33) reaches top degree, and only the j=l+1 term of (4.25) does, so leading coeff of p_l(m) = (-1)^l * B_{2l+2} / (2 * (l+1)! * (2l+1)) = |B_{2l+2}| / (2*(l+1)!*(2l+1)). I checked this against the direct sympy evaluation for l = 0..5: 1/12, 1/360, 1/2520, 1/10080, 1/28512, 691/43243200 -- exact agreement at every l. Non-vanishing for all l is then von Staudt-Clausen (B_{2n} != 0), not a numerical coincidence.",
      "suggested_fix": "Anchor: the bullet beginning '*Is the leading term of $p_\\ell$ known in closed form?* Yes -- via $f_\\ell$ in' through 'the $1/360$, $1/2520$, $1/10080$ pattern above.' Replace with the explicit formula: the leading coefficient of p_l(m) is |B_{2l+2}|/(2(l+1)!(2l+1)), read off from the j=l+1 term of Ucar eq. (4.25) combined with the l=0 summand of eq. (4.33); it is nonzero for every l because even-index Bernoulli numbers never vanish, so the l-th cone coefficient supplies P_{2l+1} with a nonzero coefficient at EVERY order, which is what the K<=n argument needs. Verify against 1/12, 1/360, 1/2520, 1/10080, 1/28512, 691/43243200 for l=0..5. Also add, one line later, that at K=-1 the sign alternates as (-1)^l but the magnitude is |B_{2l+2}|/(2(l+1)!(2l+1)) > 0, which is why sum b_2 carries +1/2520 and sum b_3 carries -1/10080."
    },
    {
      "id": "T2",
      "file": "review/hyperresearch/Q4-stability.md",
      "severity": "high",
      "issue": "Q4 section 2.2 states the manuscript's Jacobian identification incorrectly, and the error is checkable in one line. It says: 'For a monic cubic with roots p,q,r, |p'(p)|=|(p-q)(p-r)|. The pairwise-gap product in det DF is therefore not a new object -- it is prod_k |p'(z_k)| rearranged.' That is false. prod_k |p'(z_k)| = |(p-q)(p-r)|*|(q-p)(q-r)|*|(r-p)(r-q)| = (p-q)^2 (p-r)^2 (q-r)^2, the DISCRIMINANT -- the gap product SQUARED. det DF carries the gap product to the FIRST power. So the sentence that is supposed to explain the manuscript's Jacobian mis-states the algebra, and it leaves the reviewer's actual question -- where do (p+q)(p+r)(q+r)/(pqr)^2 come from -- unanswered.",
      "evidence": "Verified symbolically: det DF = -3(p-q)(p+q)(p-r)(p+r)(q-r)(q+r)/(p^2 q^2 r^2), matching paper/main.tex line 269 exactly. det D(P_1,P_2,P_3) = -6(p-q)(p-r)(q-r), i.e. 6 x Vandermonde, first power. prod_k |p'(z_k)| factors as (p-q)^2(p-r)^2(q-r)^2. The correct decomposition is det DF = det D(P_1,P_2,P_3) * (p+q)(p+r)(q+r)/(2(pqr)^2), where (p+q)(p+r)(q+r) = e_1 e_2 - e_3 -- i.e. the extra factors are the Jacobian of the reparametrisation (P_1,P_2,P_3) -> (S_1,R,P_3), since R = e_2/e_3 and P_2 = e_1^2 - 2e_2. That factor is strictly positive for all p,q,r > 0, so it contributes NO degeneracy: the vanishing locus of det DF is exactly the three diagonals, as the manuscript says. Note also that VERDICT.md line 217 already carries a better (though sign-flipped) version of this: 'det DF = -3 Vandermonde(p^2,q^2,r^2)/(pqr)^2'. With the standard convention V(a,b,c)=(b-a)(c-a)(c-b) the correct sign is PLUS 3, verified symbolically. So Q4 contradicts VERDICT, and VERDICT's sign is wrong.",
      "suggested_fix": "Anchor: the sentence 'The pairwise-gap product in $\\det DF$ is therefore not a new object -- it is $\\prod_k|p'(z_k)|$ rearranged.' Replace with the correct identification: det DF equals the power-sum Jacobian -6(p-q)(p-r)(q-r) times the reparametrisation factor (p+q)(p+r)(q+r)/(2(pqr)^2) = (e_1e_2-e_3)/(2e_3^2); equivalently det DF = +3 Vandermonde(p^2,q^2,r^2)/(pqr)^2. State that prod_k|p'(z_k)| is the discriminant, i.e. the gap product squared, so it is NOT what appears here; the first-power gap product is the Vandermonde determinant. Add the load-bearing consequence: since (p+q)(p+r)(q+r) > 0 for positive orders, the extra factors rescale but never degenerate, so the vanishing locus really is exactly the diagonals. Separately, fix the sign in VERDICT.md line 217 from -3 to +3."
    },
    {
      "id": "T3",
      "file": "review/hyperresearch/Q4-stability.md",
      "severity": "high",
      "issue": "Q4 -- the file that is supposed to carry the technique detail -- omits the single structural fact that makes its own recommendation legitimate, and which VERDICT.md already states. Q4 section 5 step 1 says 'Treat $(S_1,R,P_3)$ as three moments of the node set $\\{p,q,r\\}$.' They are not moments of {p,q,r}: R = sum m_i^{-1} is a NEGATIVE moment, so (S_1,R,P_3) is not a Prony system in the nodes p,q,r and Batenkov-Yomdin does not literally apply to it. The correct identification is in VERDICT.md section 5 and nowhere in Q4.",
      "evidence": "VERDICT.md lines 208-212: 'With nodes $x_i := m_i^2$ and weights $a_i := 1/m_i$, the $j$-th moment $\\sum_i a_i x_i^j$ is $R, S_1, P_3, P_5, P_7$ for $j=0,1,2,3,4$ -- the whole hierarchy of Corollary D and its extension, in one system, with the $\\ell$-th cone coefficient supplying the $(\\ell+1)$-th moment.' I verified this: sum (1/m_i)(m_i^2)^j = sum m_i^{2j-1}, which is R, S_1, P_3, P_5, P_7 for j=0..4. Two further consequences the vault supports and neither file draws: (i) the weights are FUNCTIONS of the nodes (a_i = x_i^{-1/2}), so Batenkov-Yomdin Corollary 4.3's second branch -- 'or a leading magnitude vanishes' (vault note `11061137-on-the-accuracy-of-solving-confluent-prony-systems`, summary) -- is vacuous here, and the critical locus is EXACTLY the collision set, a cleaner statement than the general theorem gives; (ii) in the squared variables the gaps are |m_i^2 - m_j^2| = |m_i - m_j|(m_i + m_j) >= m_i + m_j >= 5 for distinct integer orders, so the separation is bounded below by the SUM of the orders, not by 1.",
      "suggested_fix": "Anchor: Q4 section 5 numbered item '1. Treat $(S_1,R,P_3)$ as three moments of the node set $\\{p,q,r\\}$.' Replace with the correct system: nodes x_i = m_i^2, weights a_i = 1/m_i, so that the j-th moment sum a_i x_i^j is R, S_1, P_3, P_5, P_7 for j=0,1,2,3,4 -- the whole heat-coefficient hierarchy in one Prony system. Add the two consequences: the weight-vanishing branch of B-Y Cor. 4.3 is vacuous because a_i = 1/m_i > 0, so the critical locus is exactly the collision set; and the effective gaps are |m_i^2-m_j^2| = |m_i-m_j|(m_i+m_j), which is where the manuscript's (p+q)(p+r)(q+r) actually comes from. Also correct Q4 section 2.4's framing sentence 'is the manuscript's problem in another vocabulary: recover node locations xi_i from noisy power moments' to note that the manuscript's is a RESTRICTED Prony system (K unknowns, not 2K), since the weights are determined by the nodes."
    },
    {
      "id": "T4",
      "file": "review/hyperresearch/Q2-cone-coefficients.md",
      "severity": "high",
      "issue": "The minimality claim for the n=4 witness quotes a search range and a multiset count that do not go together, and the two files disagree with each other. Q2 section 4 says 'Over all 4-cone pillows with orders $\\le60$ (395,009 multisets) this pair and its $\\times2$ scaling are the only $(R,S_1,P_3)$ collisions.' 395,009 is not the count at MAX=60, and at MAX=55 the x2 scaling (which contains the order 60) cannot appear at all. This is a reproducibility failure in a computation explicitly offered to the author as 'reproducible in exact rational arithmetic'.",
      "evidence": "I re-ran the enumeration in exact Fraction arithmetic. MAX=55: 395,009 admissible multisets, exactly 1 collision -- {(3,10,15,30),(4,5,21,28)} at S_1=58. MAX=60: 557,844 admissible multisets, exactly 2 collisions -- the above plus {(6,20,30,60),(8,10,42,56)} at S_1=116. 395,009 = C(57,4) - 1, i.e. combinations_with_replacement over {2..55} minus the single non-hyperbolic multiset (2,2,2,2); it is unambiguously the MAX=55 figure. `research/temp/original-computation-ncone.md` is internally inconsistent in the same way: its prose says 'orders <= 60 (395,009 admissible multisets)' while its own table on the next page reads '4 | (R,S_1,P_3) | <=55 | 395,009 | 1'. The n=5 numbers have the identical defect: prose says 'minimal such pair for n=5 over all orders <= 30', the table says '<=26 | 118,755'. 118,755 = C(29,5), i.e. MAX=26; at MAX=30 there are 237,336 multisets and 32 collisions, not 2.",
      "suggested_fix": "Anchor: 'Over all 4-cone pillows with orders $\\le60$ (395,009 multisets) this pair and its $\\times2$ scaling are the only $(R,S_1,P_3)$ collisions'. Replace the count with the MAX=60 figure: 557,844 admissible multisets, exactly two (R,S_1,P_3) collisions. (If the reviser prefers the smaller run, then it is MAX=55, 395,009 multisets, exactly ONE collision, and the x2-scaling sentence must be dropped because order 60 is out of range.) Apply the same correction to `research/temp/original-computation-ncone.md` prose ('orders <= 60 (395,009 admissible multisets)' -> 557,844; and the n=5 'over all orders <= 30' -> <= 26, matching that file's own table)."
    },
    {
      "id": "T5",
      "file": "review/hyperresearch/Q2-cone-coefficients.md",
      "severity": "high",
      "issue": "Q2 concludes 'this gives $K=4$ exactly for these two orbifolds -- the matching lower bound that Remark 5.6 leaves open, settled for $n=4$ with an explicit witness.' Under the manuscript's own definition of K this is false, and a JGA referee in this area will see it immediately. Q2 also endorses Remark 5.6's 'upper bound $K\\le n$' without noticing that the same defect sits in the manuscript.",
      "evidence": "paper/main.tex line 103 defines K: 'K(F) denotes the least number of leading heat coefficients that distinguish a pillow F from every other hyperbolic triangular pillow'. For a genus-0 hyperbolic orbifold with n cone points the Teichmuller space has dimension 2n-6: zero for n=3 (a triangle orbifold is rigid, which is why Theorem C's 'up to isometry' at line 114 is legitimate), but 2 for n=4. So O(3,10,15,30) is a 2-parameter family of pairwise non-isometric hyperbolic 4-cone pillows, all with the same cone orders and, by Gauss-Bonnet, the same area -- hence identical heat coefficients at EVERY order (at constant curvature the smooth-part coefficients depend only on vol(O), and by Ucar Theorem 4.20(ii) / eq. (4.33) in vault note `spectral-invariants-for-polygons-and` line 12529, the cone contribution depends only on the order k and kappa). No finite number of heat coefficients distinguishes such a pillow from every other 4-cone pillow, so K is infinite for n>=4 under the line-103 definition. What the witness actually establishes -- and this survives intact -- is a statement about the CONE-ORDER MULTISET, which is exactly how `research/temp/original-computation-ncone.md` states its 'Unconditional' part 1.",
      "suggested_fix": "Anchor: the sentence 'Combined with Schueth's Theorem 4.1, which makes $P_5$ the fourth coefficient, this gives $K=4$ exactly for these two orbifolds -- **the matching lower bound that Remark 5.6 leaves open, settled for $n=4$ with an explicit witness.**' Re-word as a multiset statement: three heat coefficients do not determine the cone-order multiset of a 4-cone hyperbolic pillow, four do on this pair, so the multiset-recovery count is exactly 4 for n=4. Add a sentence flagging for the author that Remark 5.6's 'K <= n' inherits the same issue: for n>=4 the cone-order multiset is not a complete isometry invariant (dim Teichmuller = 2n-6 > 0), all members of a fixed-multiset family share every heat coefficient, and so Remark 5.6 should be phrased as recovery of the multiset rather than determinacy up to isometry. Note explicitly that Theorem C at n=3 is unaffected because triangle orbifolds are rigid."
    },
    {
      "id": "T6",
      "file": "review/hyperresearch/Q2-cone-coefficients.md",
      "severity": "medium",
      "issue": "The brief asks to record 'any sign or factor conventions that differ between Schueth, DGGW and Ucar'. Q2's answer, at line 83, is 'No sign or factor convention differs between the two sources' -- and the two sources are DGGW and Schueth. Ucar's conventions are never stated anywhere in Q2, even though Ucar is the SOLE source for l >= 3 and the only source that supports the general-l claim on which Q2's whole verdict rests. Three specific convention facts are sitting in the vault unread into the deliverable.",
      "evidence": "All three are in vault note `spectral-invariants-for-polygons-and`: (i) Laplacian sign -- note line 570, 'Delta: C^inf(Omega) -> C^inf(Omega), Delta f := -div(grad f) denotes the Laplacian', which is identical to Schueth's convention in vault note `181206119-schueth-corner-contributions-ar5iv-fulltext` line 174, 'Delta_g = -div_g o grad_g'; (ii) curvature parameter -- Ucar's kappa is the sectional curvature, fixed in Proposition 4.17 (note line ~12093) by 'let Omega subset S^2(r) be a lune with angle pi/k, and write kappa = 1/r^2', so kappa = K with no rescaling; (iii) prefactor -- Ucar's Theorem 4.20 (note lines 12520-12536) puts the (1/4pi t) prefactor on the smooth part only, 'ZO(t) ~ (1/4pi t) sum a_nu(O) t^nu + sum_N I_N(O)/|Iso(N)|', and states I_N(O)/|Iso(N)| = C for a cone point, so the cone series carries no (4pi t)^{-1}, matching the manuscript's section 1.2. Independent confirmation that all three line up: Schueth Thm 4.1 minus Ucar b_2 simplifies identically to zero -- but that is a consequence, and the brief asked for the conventions themselves.",
      "suggested_fix": "Anchor: the paragraph beginning '**No sign or factor convention differs between the two sources.**' Extend it to three sources and name Ucar's conventions explicitly with citations: Delta f := -div(grad f) (Ucar, thesis section 3.1, matching Schueth's Delta_g = -div_g o grad_g); kappa = sectional curvature, fixed as 1/r^2 in Prop. 4.17; and no (4pi t)^{-1} prefactor on the cone series, per Theorem 4.20's decomposition. Keep the existing DGGW/Schueth sentence and add that the exact agreement of Schueth Thm 4.1 with Ucar's b_2 is the empirical confirmation that the three conventions coincide."
    },
    {
      "id": "T7",
      "file": "review/hyperresearch/Q2-cone-coefficients.md",
      "severity": "medium",
      "issue": "The sign of the b_3 row -- and by extension every odd-l row at K = -1 -- is justified in Q2 only by 'K^3 = -1' implicit in the b_l = kappa^l (1/m) p_l(m) form. But the whole evaluation chain runs through Ucar's SPHERICAL lune coefficient c^S_l (Prop. 4.17 computes a lune in S^2(r) with kappa = 1/r^2 > 0), and the negative-curvature case is reached by Theorem 4.20's 'constant curvature kappa in R'. Q2 never checks that the kappa^l factor really carries to kappa < 0, which is precisely the sign question the brief raised. Ucar answers it directly and Q2 does not use the answer.",
      "evidence": "Vault note `spectral-invariants-for-polygons-and`, the Remark following eq. (3.97) (note lines 8093-8100), verbatim: 'Observe that when we compare our coefficients c^H_k(gamma_i) given in (3.97) with the corresponding spherical coefficients c^S_k(gamma_i) (see [Wat05, formula (22)]), then we have c^H_k(gamma_i) = (-1)^k c^S_k(gamma_i). Hence, when we compare nu^H_k with its spherical counterpart nu^S_k in [Wat05, formula (29)], we still have the relation nu^H_k = (-1)^k nu^S_k. As we will see later, there is a deeper reason why the latter relation must hold if gamma_i = pi/k for some k in N.' Ucar's Chapter 3 computes the HYPERBOLIC wedge coefficients directly (Green kernel for a geodesic wedge in the hyperbolic plane), so this is an independent computation on the negative-curvature side, not an analytic continuation -- it certifies the (-1)^l that produces the minus sign on P_7 in the sum b_3 row. Separately, on the reviewer's Delta_g worry: Schueth's Delta_g sign never enters the K=-1 specialisation because the entire second bracket of Theorem 4.1 is multiplied by Delta_g K, which vanishes identically at constant curvature -- worth saying, since 'no convention differs' is a weaker and less checkable statement.",
      "suggested_fix": "Anchor: the block of three summed formulas in Q2 section 3 ('$\\textstyle\\sum b_1=...$' through '$\\textstyle\\sum b_3=...$') and the sentence following it. Add a short justification of the alternating sign citing Ucar's Remark after Corollary 3.30 (eq. 3.97, p. 86-87): c^H_k(gamma) = (-1)^k c^S_k(gamma), computed independently on the hyperbolic side, which is the same fact as the kappa^l factor evaluated at kappa = -1 and independently certifies the minus on P_7. Separately, in the Theorem 4.1 discussion, replace the bare 'At constant curvature $\\Delta_gK\\equiv0$ and the entire second bracket vanishes' with the stronger statement that this is also why Schueth's Delta_g = -div o grad sign convention cannot affect the K=-1 specialisation."
    },
    {
      "id": "T8",
      "file": "review/hyperresearch/Q2-cone-coefficients.md",
      "severity": "medium",
      "issue": "Q2 prints Schueth Remark 4.2, Schueth Theorem 4.1, Schueth Remark 5.4(ii) and DGGW eq. (5.10) verbatim, but for Ucar -- the only source that supports the l>=3 rows and the 'explicit for every l' verdict -- it gives nothing but a pointer: 'equation (4.25) on p. 134 together with equation (4.33) on p. 137: a finite Bernoulli-number sum, explicit for every l>=0.' The brief's instruction was 'record the EXACT stated formula with normalization conventions, page/equation reference'. The load-bearing source is the one that is not quoted, and a referee cannot check the l=3 row without it.",
      "evidence": "Both formulas are in the vault verbatim. `spectral-invariants-for-polygons-and` line 12144, eq. (4.25): c^S_l(pi/k) = [1/(4k)] * [(-1)^l/(l+1)!] * [1/(2l+1)] * sum_{j=0}^{l+1} binom(2l+2, 2j) (k^{2j} - 1) B_{2j} B_{2l+2-2j}(1/2). Same note line 12486, eq. (4.33): C = sum_nu sum_{l=0}^{nu} (2/(4^l l!)) c^S_{nu-l}(pi/k) kappa^nu t^nu, with the isotropy-averaged restatement at eq. (4.34): (1/k) sum_{l=1}^{k-1} b_nu(D_l) = sum_{l=0}^{nu} (2/(4^l l!)) c^S_{nu-l}(pi/k) kappa^nu. I evaluated these two formulas from scratch and reproduced Q2's whole table exactly -- p_1 = (m^4-1)/360 + (m^2-1)/36, p_2 = (2m^6+7m^4+28m^2-37)/5040, p_3 = (3m^8+8m^6+14m^4+32m^2-57)/30240, plus p_0 = (m^2-1)/12 and p_4 with leading coefficient 1/28512 -- so the evaluation is sound; it is only unquoted.",
      "suggested_fix": "Anchor: the paragraph 'The operative result is **equation (4.25) on p. 134 together with equation (4.33) on p. 137**: a finite Bernoulli-number sum, **explicit for every $\\ell\\ge0$**.' Insert both formulas as displayed verbatim quotations immediately after it, exactly as they appear in the vault note, together with the (4.34) isotropy-averaged form which is the one that matches Schueth's eq. (17) a_l = (1/k) sum_j b_l(Phi^j). State that the table below was produced by evaluating these two equations, so a referee can reproduce it."
    },
    {
      "id": "T9",
      "file": "review/hyperresearch/Q4-stability.md",
      "severity": "medium",
      "issue": "Q4 misses the one paper in the vault that was fetched specifically because it covers the manuscript's exact configuration, and that supplies the blow-up RATE Q4 says it wants. Section 2.3 lists Gautschi-Inglese, Pan and Aubel-Bolcskei; section 5 recommends 'Batenkov-Yomdin ... Gautschi-Inglese and Pan ... Moitra via Aubel-Bolcskei ... Tisseur-Van Barel and Wilkinson.' Kunis-Nagel appears nowhere in either.",
      "evidence": "Vault note `181208645-on-the-condition-number-of-vandermonde-matrices-with-pairs-of-nearly-c` (Kunis & Nagel, arXiv:1812.08645v2, math.NA, 21 pp.). The note's own provenance line reads: 'Suggested by [[170102538-vandermonde-matrices-with-nodes-in-the-unit-disk-and-the-large-sieve]] -- Springer similar content link on nearly-colliding Vandermonde nodes, directly analogous to the manuscript's diagonal-approach blow-up.' Abstract, verbatim from the note: 'We prove upper and lower bounds for the spectral condition number of rectangular Vandermonde matrices with nodes on the complex unit circle. The nodes are off the grid, pairs of nodes nearly collide, and the studied condition number grows linearly with the inverse separation distance. Such growth rates are known in greater generality if all nodes collide or for groups of colliding nodes. For pairs of nodes, we provide reasonable sharp constants that are independent of the number of nodes as long as non-colliding nodes are well-separated.' This is exactly the manuscript's regime -- ONE pair approaching a diagonal (p -> q) while the third order stays away -- and it gives a rate (linear in inverse separation) with sharp constants, which is strictly more actionable than Batenkov-Yomdin's unspecified 'some finite power'.",
      "suggested_fix": "Anchor: Q4 section 2.3, the bullet list under 'Vandermonde conditioning', after the Pan and Aubel-Bolcskei entries. Add a Kunis-Nagel bullet with arXiv:1812.08645, quoting the 'grows linearly with the inverse separation distance ... reasonable sharp constants that are independent of the number of nodes as long as non-colliding nodes are well-separated' clause, and stating that this is the pair-collision regime the manuscript's diagonals sit in. Also add it to the citation list in section 5's 'Technique: nothing new' bullet."
    },
    {
      "id": "T10",
      "file": "review/hyperresearch/Q4-stability.md",
      "severity": "medium",
      "issue": "Q4 recommends a bound whose hypotheses the manuscript's problem does not satisfy. Section 2.3 quotes 'Moitra's large-sieve bound kappa(V_{NxK})^2 <= (N-1+1/delta)/(N-1-1/delta) with delta the minimum node separation', and section 5 tells the author to cite 'Moitra via Aubel-Bolcskei for the minimum-separation bound'. That bound is for nodes on the unit CIRCLE with delta a wrap-around (torus) separation of frequencies; the manuscript's nodes are real positive integers. Meanwhile the same vault note carries a sharper, correctly-applicable result for real positive nodes that Q4 does not use.",
      "evidence": "Vault note `170102538-vandermonde-matrices-with-nodes-in-the-unit-disk-and-the-large-sieve` (Aubel & Bolcskei), summary, verbatim: 'Section 4 recounts the Selberg-Moitra connection between Vandermonde extremal singular values on the unit circle and the large-sieve inequality: kappa(V_{NxK})^2 <= (N-1+1/delta)/(N-1-1/delta) (Moitra, eq. 12) where delta is the minimum wrap-around separation of node frequencies'. The same summary records the tool that does apply: 'Beckermann's sharper two-sided bound for real nonzero nodes: sqrt(2)(1+sqrt(2))^{K-1}/sqrt(K+1) <= kappa(V_{KxK}) <= (K+1)sqrt(2)(1+sqrt(2))^{K-1}, tightening for positive nodes to C_K/(2(K+1)) <= kappa <= (K+1)/2 * C_K with C_K = (1+sqrt2)^{2K}+(1+sqrt2)^{-2K}'. Q4 cites only the one-sided Gautschi-Inglese lower bound kappa_inf >= (K-1)2^K and never mentions Beckermann.",
      "suggested_fix": "Anchor: the Aubel & Bolcskei bullet in Q4 section 2.3, and the phrase 'Moitra via Aubel-Bolcskei for the minimum-separation bound' in section 5. Qualify the Moitra bullet by stating that delta there is the minimum WRAP-AROUND separation for nodes on the unit circle, so it is a structural analogy for the manuscript's real positive nodes, not a directly applicable bound. Add Beckermann's two-sided bound for real positive nodes (as recorded in the same note) as the correctly-typed replacement, and demote the section-5 recommendation of Moitra accordingly."
    },
    {
      "id": "T11",
      "file": "review/hyperresearch/Q4-stability.md",
      "severity": "medium",
      "issue": "Q4 overstates what Batenkov-Yomdin actually delivers, twice, and the overstatement drives the verdict. Section 2.4 says Theorem 4.5's scaling is 'precisely the pairwise-gap blow-up the manuscript wants, already proved', then concludes in bold 'This means the conditioning half of the planned theorem is already in the literature'; section 5 says specializing known bounds 'inherits their constants'. But the exponent in Batenkov-Yomdin is unspecified, so there is no constant to inherit and no rate to specialize.",
      "evidence": "Vault note `11061137-on-the-accuracy-of-solving-confluent-prony-systems` (Batenkov & Yomdin), summary, verbatim: 'accuracy is inversely proportional to node separation and this dependence is roughly of the same order as some finite power of prod_{i<j}|xi_j-xi_i|^{-1} (Sec 1.D summary)'. 'Some finite power' is not a rate. Q4 itself reproduces this hedge at section 2.4 and then, three lines later, treats the result as if it were quantitative. The honest reading strengthens the manuscript rather than weakening it: at n=3 the explicit cubic constants derived from det DF are sharper than anything B-Y states, and Kunis-Nagel (see T9) supplies the only explicit rate in the vault (linear in inverse separation, for the pair-collision case).",
      "suggested_fix": "Anchor: the bold sentence '**This means the conditioning half of the planned theorem is already in the literature.**' and the section-5 clause 'and it inherits their constants'. Re-word both: Batenkov-Yomdin settles the STRUCTURE (critical locus = collision set, Vandermonde x diagonal factorisation) but leaves the exponent unspecified ('some finite power'), so the conditioning half is settled qualitatively, not quantitatively; the manuscript's explicit n=3 constants are therefore a genuine, if narrow, sharpening, and Kunis-Nagel is the place to look for an explicit rate. Keep the warning that presenting the structural facts as new would be caught by a referee."
    },
    {
      "id": "T12",
      "file": "review/hyperresearch/Q4-stability.md",
      "severity": "medium",
      "issue": "Q4 promises 'explicit constants' throughout but never writes down either end of the chain the query names. The query asks specifically for 'Newton identities conditioning'; Q4's section 2.1 jumps straight from power sums to root perturbation via Tisseur-Van Barel and never bounds the intermediate power-sums-to-coefficients step. And nothing anywhere converts an error in a HEAT COEFFICIENT into an error in (S_1, R, P_3) -- yet that conversion is the first link of the manuscript's actual theorem and its constants are printed in the manuscript itself.",
      "evidence": "Both links are two lines of algebra from data already in the deliverables. (a) Newton step, n=3: e_1 = P_1, e_2 = (P_1^2 - P_2)/2, e_3 = (P_1^3 - 3P_1P_2 + 2P_3)/6, so the amplification from perturbed power sums to perturbed coefficients is O(S_1^2) -- this is exactly the 'Newton identities conditioning' the query names and Q4 never addresses it. (b) Spectral-to-invariant step: from the manuscript's eq. (3) / Corollary 2.5, a_0 = (S_1 + R - 2)/12, so delta(S_1 + R) = 12 * delta a_0; and from eq. (5), verified in Q2 section 2, a_1 = -P_3/360 - S_1/36 + 11R/360, so delta P_3 = 360 * delta a_1 + 10 * delta S_1 + 11 * delta R -- the third heat coefficient is amplified by a factor 360 before root conditioning even begins. Neither number appears in Q4.",
      "suggested_fix": "Anchor: Q4 section 2.1 ('Power sums -> coefficients -> roots') and the section-5 step 3 that says 'derive the explicit cubic constants directly'. Insert the two missing links with their explicit factors: the Newton-identity amplification e_2 = (P_1^2-P_2)/2, e_3 = (P_1^3-3P_1P_2+2P_3)/6 giving O(S_1^2) growth, and the heat-coefficient-to-invariant conversion delta(S_1+R) = 12 delta a_0 and delta P_3 = 360 delta a_1 + 10 delta S_1 + 11 delta R read off the manuscript's own eq. (3) and eq. (5). State that these are the constants the theorem's epsilon must be expressed in, since spectral error arrives in the a_l and not in (S_1, R, P_3)."
    }
  ]
}
```

---

## 9. THE MODULI DEFECT

**$K(F)$ is infinite for $n\ge4$.** $K(F)$ is defined in `paper/main.tex` line 103 as the least number of leading heat coefficients distinguishing a pillow from *every other* hyperbolic triangular pillow — an isometry-class notion. For a sphere with $n$ cone points of prescribed orders the moduli space of constant-curvature cone metrics has real dimension $2n-6$: zero exactly at $n=3$, but $2$ at $n=4$. Every heat coefficient is a function of the cone orders alone (area fixed by Gauss–Bonnet; each cone contributing through its order), so an entire $(2n-6)$-dimensional family of mutually non-isometric pillows shares **all** heat coefficients. Hence no finite number distinguishes them, and Remark 5.6's "$K\le n$ extends the $n=3$ case of Theorem C" fails in the isometry sense Theorem C uses. $n=3$ survives because triangle orbifolds are rigid — which is exactly what makes triangular pillows the right object.

**Citations, as recorded, both resolvable:**

- Thurston, *Shapes of polyhedra and triangulations of the sphere*, Geom. Topol. Monogr. **1** (1998), 511–549, DOI [`10.2140/gtm.1998.1.511`](https://doi.org/10.2140/gtm.1998.1.511)
- Troyanov, *Prescribing curvature on compact surfaces with conical singularities*, Trans. Amer. Math. Soc. **324** (1991), 793–821, DOI [`10.1090/S0002-9947-1991-1005085-9`](https://doi.org/10.1090/S0002-9947-1991-1005085-9)

Both give the moduli dimension $n-3$ complex, hence $2n-6$ real.

### 9.1 Depth critic, finding `T5` — the finding as produced

From `research/critic-findings-depth.json`, severity `high`. Verbatim JSON object:

```json
{
  "id": "T5",
  "file": "review/hyperresearch/Q2-cone-coefficients.md",
  "severity": "high",
  "issue": "Q2 concludes 'this gives $K=4$ exactly for these two orbifolds -- the matching lower bound that Remark 5.6 leaves open, settled for $n=4$ with an explicit witness.' Under the manuscript's own definition of K this is false, and a JGA referee in this area will see it immediately. Q2 also endorses Remark 5.6's 'upper bound $K\\le n$' without noticing that the same defect sits in the manuscript.",
  "evidence": "paper/main.tex line 103 defines K: 'K(F) denotes the least number of leading heat coefficients that distinguish a pillow F from every other hyperbolic triangular pillow'. For a genus-0 hyperbolic orbifold with n cone points the Teichmuller space has dimension 2n-6: zero for n=3 (a triangle orbifold is rigid, which is why Theorem C's 'up to isometry' at line 114 is legitimate), but 2 for n=4. So O(3,10,15,30) is a 2-parameter family of pairwise non-isometric hyperbolic 4-cone pillows, all with the same cone orders and, by Gauss-Bonnet, the same area -- hence identical heat coefficients at EVERY order (at constant curvature the smooth-part coefficients depend only on vol(O), and by Ucar Theorem 4.20(ii) / eq. (4.33) in vault note `spectral-invariants-for-polygons-and` line 12529, the cone contribution depends only on the order k and kappa). No finite number of heat coefficients distinguishes such a pillow from every other 4-cone pillow, so K is infinite for n>=4 under the line-103 definition. What the witness actually establishes -- and this survives intact -- is a statement about the CONE-ORDER MULTISET, which is exactly how `research/temp/original-computation-ncone.md` states its 'Unconditional' part 1.",
  "suggested_fix": "Anchor: the sentence 'Combined with Schueth's Theorem 4.1, which makes $P_5$ the fourth coefficient, this gives $K=4$ exactly for these two orbifolds -- **the matching lower bound that Remark 5.6 leaves open, settled for $n=4$ with an explicit witness.**' Re-word as a multiset statement: three heat coefficients do not determine the cone-order multiset of a 4-cone hyperbolic pillow, four do on this pair, so the multiset-recovery count is exactly 4 for n=4. Add a sentence flagging for the author that Remark 5.6's 'K <= n' inherits the same issue: for n>=4 the cone-order multiset is not a complete isometry invariant (dim Teichmuller = 2n-6 > 0), all members of a fixed-multiset family share every heat coefficient, and so Remark 5.6 should be phrased as recovery of the multiset rather than determinacy up to isometry. Note explicitly that Theorem C at n=3 is unaffected because triangle orbifolds are rigid."
}
```


### 9.2 Dialectic critic, finding `D11` — the consequence for the appendix

From `research/critic-findings-dialectic.json`, severity `medium`. This is the finding that the $n$-cone appendix's stated caveat names the **wrong** dependency: the $b_2\to P_5$ conditional was discharged by Q2 §3, and the live conditionality for $n\ge4$ is the isometry-versus-multiset issue. Verbatim JSON object:

```json
{
  "id": "D11",
  "file": "review/hyperresearch/APPENDIX-ncone-computation.md",
  "location": "'## The load-bearing caveat' and the two-part statement that follows it; cross-referenced from Q2-cone-coefficients.md at 'Full details, including the caveat structure, in `review/hyperresearch/APPENDIX-ncone-computation.md`.'",
  "severity": "medium",
  "issue": "This is the reverse failure — a hedge that should now commit. The appendix's caveat conditions the whole n=4 result on 'Whether $b_2$ actually delivers $P_5$ with a nonzero coefficient at constant curvature is precisely question Q2, and it is not settled by this computation', then instructs that the result 'should be stated to the author in two parts', the second being 'Conditional on $b_2 \\to P_5$'. Q2 has since settled that question affirmatively and cross-validated it: Schueth's Theorem 4.1 at constant curvature delivers P_5 with coefficient 1/2520, and the Uçar-derived p_2 was checked against it to symbolic zero. The conditional is discharged, but the appendix still presents it as live and Q2 still routes the author there 'including the caveat structure'. An author following that pointer will state a weaker two-part conditional result than the evidence now supports, and will read a live dependency where none remains. Worse, the caveat names the wrong dependency: the live conditionality for n≥4 is not the coefficient question at all but the isometry-versus-multiset issue Q2 now raises via the Thurston/Troyanov moduli-dimension argument, which the appendix does not mention.",
  "evidence": "APPENDIX-ncone-computation.md '## The load-bearing caveat': '**Whether $b_2$ actually delivers $P_5$ with a nonzero coefficient at constant curvature is precisely question Q2**, and it is not settled by this computation'. Q2-cone-coefficients.md §3 settles it: Schueth Theorem 4.1 at constant curvature gives the 1/2520 coefficient on P_5, and the ℓ=2 row 'was cross-validated against **Schueth's Theorem 4.1**… the difference simplifies **identically to zero**'. Q2 §4 separately establishes the genuinely live caveat for n≥4 — that K(F) as defined is an isometry-class notion and the moduli space of n-cone spherical/constant-curvature metrics has real dimension 2n−6 (Thurston, DOI 10.2140/gtm.1998.1.511; Troyanov, DOI 10.1090/S0002-9947-1991-1005085-9).",
  "suggested_fix": "ANCHOR (APPENDIX-ncone-computation.md, single line): '## The load-bearing caveat' — INSERT immediately beneath the heading a short status note discharging the conditional and redirecting it, e.g. '**Status: discharged.** The dependency below was live when this computation was run. Q2 §3 has since settled it: Schueth Theorem 4.1 gives $b_2$'s $P_5$ coefficient as $1/2520$ at constant curvature, cross-validated against Uçar to symbolic zero. The two-part statement below is retained for audit only — part 2 is now unconditional. The caveat that *is* live for $n\\ge4$ is a different one: $K(F)$ is defined as an isometry-class notion and multiset determinacy does not upgrade to isometry determinacy once the moduli space is positive-dimensional. See Q2 §4.' Leave the existing text in place beneath it — it is an audit record. ALSO ANCHOR (Q2-cone-coefficients.md, single line): 'Full details, including the caveat structure, in `review/hyperresearch/APPENDIX-ncone-computation.md`.' — APPEND a clause noting that the appendix's $b_2 \\to P_5$ caveat is discharged by §3 above and that the live conditionality is the isometry-versus-multiset distinction, not the coefficient."
}
```


### 9.3 What was done with it — patch log entry

From `research/patch-log.json`, `patches_applied`. Verbatim JSON object:

```json
{
  "ref": "T5",
  "file": "review/hyperresearch/Q2-cone-coefficients.md + VERDICT.md",
  "issue": "HIGHEST-VALUE FINDING. K(F) is defined up to isometry. For n>=4 the Teichmuller space of a sphere with n cone points has dimension 2n-6>0, and every heat coefficient depends only on the cone orders, so a whole family shares all coefficients. K is infinite for n>=4 and Remark 5.6's 'K<=n extends Theorem C' fails.",
  "action": "Added a boxed correction; restated the n=4 result as cone-order-multiset determinacy; flagged as a defect in the manuscript, item 18."
}
```


### 9.4 The correction as it now stands in `Q2-cone-coefficients.md` §4

Verbatim, the boxed callout:

```markdown
> **A correction the manuscript needs independently of this witness.** $K(F)$ is defined
> (line 103) as the least number of leading heat coefficients distinguishing $F$ from *every
> other hyperbolic triangular pillow* — an isometry-class notion. For $n=3$ that is
> unproblematic: a hyperbolic triangle orbifold is rigid, so the cone-order multiset *is* the
> isometry class. **For $n\ge4$ it fails.** The moduli space of constant-curvature cone metrics
> on the sphere with $n$ prescribed cone angles has complex dimension $n-3$, hence real
> dimension $2n-6$ — zero exactly when $n=3$ (Thurston, *Shapes of polyhedra and
> triangulations of the sphere*, Geom. Topol. Monogr. **1** (1998), 511–549,
> DOI [`10.2140/gtm.1998.1.511`](https://doi.org/10.2140/gtm.1998.1.511); Troyanov,
> Trans. Amer. Math. Soc. **324** (1991), 793–821,
> DOI [`10.1090/S0002-9947-1991-1005085-9`](https://doi.org/10.1090/S0002-9947-1991-1005085-9)).
> So for $n=4$ a fixed multiset carries a two-parameter family of mutually non-isometric
> pillows. Every heat coefficient is a function
> of the cone orders alone — the area is fixed by Gauss–Bonnet and each cone contributes
> through its order — so that entire family shares **all** heat coefficients. Hence $K(F)$ as
> defined is *infinite* for $n\ge4$, and Remark 5.6's "the upper bound $K\le n$ extends the
> $n=3$ case of Theorem C" does not hold in the isometry sense in which Theorem C is stated.
>
> The fix is small and the result survives it: for $n\ge4$, state the theorem as
> *determination of the cone-order multiset*, and note explicitly that $n=3$ is the only case
> where multiset determinacy upgrades to isometry determinacy, by rigidity. That is worth
> saying anyway — it identifies precisely what is special about triangular pillows, which is
> the paper's subject.
```


### 9.5 The same correction as it now stands in `VERDICT.md`, answer 3

Verbatim, the boxed callout:

```markdown
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
```


### 9.6 The computation the defect bears on — `review/hyperresearch/APPENDIX-ncone-computation.md`, FULL TEXT

This is the original exact-arithmetic computation that produced the $n=4$ witness. It is reproduced whole because §9.2's finding is precisely that its stated caveat is the wrong one, and a reader cannot check that without the text. **Note that this file still carries the discharged `b_2 → P_5` caveat and does not mention the moduli issue** — the `D11` fix was not applied to it.

```markdown
# Original computation — witnesses for the open lower bound in Remark 5.6

**Status: this is NOT a literature finding.** It is an original exact-arithmetic
computation run during the sweep. It is recorded separately from the literature results
so the two are never conflated in the deliverables. Everything below is reproducible in
exact rational arithmetic (Python `fractions.Fraction`, no floating point).

## What the manuscript leaves open

`paper/main.tex`, Remark 5.6 (`rem:ncone`, line 493):

> For an $n$-cone pillow $\mathcal{O}(m_1,\dots,m_n)$ … the first $n$ leading heat
> coefficients again supply $n$ symmetric functions of the orders, and when these are
> independent they recover the multiset, so the upper bound $K\le n$ extends the $n=3$
> case of Theorem C. The matching lower bound $K\ge n$ for $n\ge4$ would require two
> $n$-cone pillows agreeing in $n-1$ prescribed symmetric functions — an $(n-1)$-fold
> simultaneous Egyptian-fraction and power-sum system — for which we have neither a
> construction nor a non-existence proof; we leave it open.

So for $n = 4$ the manuscript asks for two 4-cone hyperbolic pillows agreeing in
**three** symmetric functions: $R$, $S_1$, $P_3$.

## The construction, for n = 4

$$\mathcal{O}(3,10,15,30) \quad\text{and}\quad \mathcal{O}(4,5,21,28)$$

| Invariant | $(3,10,15,30)$ | $(4,5,21,28)$ | Equal? |
|---|---|---|---|
| $S_1=\sum m_i$ | 58 | 58 | **yes** |
| $R=\sum 1/m_i$ | $8/15$ | $8/15$ | **yes** |
| $P_3=\sum m_i^3$ | 31402 | 31402 | **yes** |
| $P_5=\sum m_i^5$ | 25159618 | 21298618 | no |

Both are hyperbolic: for a sphere with $n$ cone points the condition is
$\sum_i (1-1/m_i) > 2$, and here $4 - 8/15 = 52/15 > 2$ for both. The multisets are
distinct, so the orbifolds are non-isometric.

**Consequence.** These two 4-cone pillows are not separated by the first three heat
coefficients, so $K \ge 4$ for both. Combined with the manuscript's own upper bound
$K \le n = 4$, this gives $K = 4$ exactly — **the matching lower bound of Remark 5.6, for
$n = 4$, with an explicit witness.** The open problem as stated is answered for $n=4$.

**Minimality.** Over all 4-cone hyperbolic pillows with every order $\le 55$ (**395,009**
admissible multisets) the pair above is the *only* $(R,S_1,P_3)$ collision. Extending to
orders $\le 60$ (**557,844** multisets) adds exactly one more — its $\times 2$ scaling
$\{\mathcal{O}(6,20,30,60),\ \mathcal{O}(8,10,42,56)\}$ at $S_1 = 116$ — which cannot appear
in the $\le 55$ scan since it contains an order-60 cone. So $S_1 = 58$ is the minimal
cone-order sum at which three heat coefficients fail for $n = 4$ in both ranges, and the pair
is unique at that sum.

*(An earlier draft quoted 395,009 against orders $\le 60$; those two figures belong to
different scans and are now separated.)*

## The same for n = 5

$$\mathcal{O}(3,7,7,7,14) \quad\text{and}\quad \mathcal{O}(4,4,6,12,12)$$

share $S_1 = 38$, $R = 5/6$, $P_3 = 3800$, and are separated by $P_5$. This is the
minimal such pair for $n=5$ over all orders $\le 30$.

**Read this one carefully — it is weaker than the $n=4$ result.** It shows three
coefficients do not suffice for $n=5$, i.e. $K \ge 4$. Remark 5.6's matching bound for
$n = 5$ needs a pair agreeing in $n-1 = 4$ functions, $(R,S_1,P_3,P_5)$. A scan of all
5-cone pillows with orders $\le 26$ (118{,}755 multisets) found **no** such pair. So the
$n = 5$ case of Remark 5.6 remains open; only the $n=4$ case is settled here.

## The scaling law generalizes

The manuscript's Proposition 5.1 scales a 3-cone degeneracy by $k$. The same argument
works for any number of cone points *and any number of invariants*: under
$m_i \mapsto k m_i$, $S_1 \mapsto k S_1$, $R \mapsto R/k$, and $P_j \mapsto k^j P_j$.
Every equality is therefore preserved. So each witness above generates an infinite family,
which is why the $\times 2$ copy appears in the $n=4$ scan.

## Injectivity of the full invariant set, checked

| $n$ | invariants | orders searched | multisets | collisions |
|---|---|---|---|---|
| 3 | $(R,S_1)$ | $\le 60$ | — | 86 (incl. the manuscript's $(2,8,8)/(3,3,12)$) |
| 3 | $(R,S_1,P_3)$ | $\le 60$ | — | **0** — corroborates Theorem C |
| 4 | $(R,S_1,P_3)$ | $\le 55$ | 395{,}009 | 1 |
| 4 | $(R,S_1,P_3,P_5)$ | $\le 55$ | 395{,}009 | **0** |
| 5 | $(R,S_1,P_3)$ | $\le 26$ | 118{,}755 | 2 |
| 5 | $(R,S_1,P_3,P_5)$ | $\le 26$ | 118{,}755 | **0** |

## The load-bearing caveat

All of this assumes the $\ell$-th cone coefficient delivers $P_{2\ell+1}$ modulo lower-order
symmetric data — $t^1 \to P_3$, $t^2 \to P_5$, and so on. That pattern is what the
manuscript establishes for $\ell = 1$ and what Uçar's $\deg p_\ell = 2\ell+2$ (divided by
the $1/m$) predicts in general. **Whether $b_2$ actually delivers $P_5$ with a nonzero
coefficient at constant curvature is precisely question Q2**, and it is not settled by
this computation — it depends on what Schueth's $t^2$ cone formula actually says. If
$b_2$'s $m^5$ coefficient vanishes at constant curvature, the $P_5$ column above is not a
heat invariant and the $n=4$ upper bound argument fails, though the lower-bound witness
(which only uses $R, S_1, P_3$) survives regardless.

Because of that dependency the $n=4$ result should be stated to the author in two parts:

1. **Unconditional:** $\mathcal{O}(3,10,15,30)$ and $\mathcal{O}(4,5,21,28)$ agree in
   $(R,S_1,P_3)$, hence in the first three heat coefficients. So three coefficients do not
   determine a 4-cone hyperbolic pillow. This needs nothing beyond the manuscript's own
   Corollary D.
2. **Conditional on $b_2 \to P_5$:** they are separated by the fourth, giving $K = 4$
   exactly and settling Remark 5.6 for $n = 4$.

## Reproduction

Independent of the repository's existing scripts. Enumerate
`combinations_with_replacement(range(2, MAX+1), n)`, keep multisets with
$\sum_i(1-1/m_i) > 2$, key them on the exact `Fraction` tuple of invariants, and report
keys with multiplicity $> 1$.
```


### 9.7 Where this lands in the corrections list

Item 18 of the 22 in §7, severity **substantive**:

> | 18 | **$K(F)$ is ill-defined for $n\ge4$**: Teichmüller dimension $2n-6>0$ means one multiset carries non-isometric pillows sharing every coefficient. Remark 5.6's "$K\le n$" must be restated as multiset determinacy | **substantive** |

And in VERDICT.md's closing section, verbatim:

> **The one exception is Remark 5.6**, and it is a genuine defect rather than a typo: the assertion that "the upper bound $K\le n$ extends the $n=3$ case of Theorem C" fails for $n\ge4$, because $K$ is defined up to isometry and $n$-cone pillows with $n\ge4$ have moduli. See item 18 above. The remark's *arithmetic* content — that $n$ coefficients supply $n$ symmetric functions — is right; what does not survive is the upgrade from those functions to an isometry class. The fix is to restate the $n\ge4$ claim as cone-order-multiset determinacy.
