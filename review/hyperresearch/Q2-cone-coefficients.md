# Q2 — The third coefficient and the higher cone coefficients

**Short answer.** Equation (4) is correct exactly as printed, and its attribution is correct
too. More importantly for the planned extension: explicit closed-form cone coefficients are
already in the literature for **every** order $\ell$ at constant curvature, not merely for
$\ell=1$ and not merely as a degree bound. A theorem of the form $K\le n+1$ therefore needs
**no new cone-coefficient computation**. What it needs is a symmetric-function argument.

Every formula below was read from the source document, not from a secondary description.

---

## 1. Equation (4): confirmed

### What the manuscript prints

`paper/main.tex`, equation (4), line 237:

$$b_1(C)=\Bigl[\tfrac1{360}\bigl(m^3-\tfrac1m\bigr)+\tfrac1{36}\bigl(m-\tfrac1m\bigr)\Bigr]K$$

### What Schueth actually says

**Schueth, arXiv:1812.06119, Remark 4.2** — verbatim from the full text:

> Analogously, one could derive that
> $$a_0^{(\{\bar p\})} = \tfrac{1}{12}\Bigl(k-\tfrac1k\Bigr),\qquad
> a_1^{(\{\bar p\})} = \Bigl[\tfrac{1}{360}\Bigl(k^{3}-\tfrac1k\Bigr)+\tfrac{1}{36}\Bigl(k-\tfrac1k\Bigr)\Bigr]K(\bar p),$$
> for an orbisurface cone point $\bar p \in (\mathcal O, g)$ of order $k$, using
> $\sum_{j=1}^{k-1}\frac{1}{\sin^2(j\cdot\pi/k)}=\frac13(k^2-1)$ and $b_0(\Phi)=\frac1C$,
> $b_1(\Phi)=\frac{2}{C^2}K(p)$.
> **Note that the above formulas for $a_0^{(\{\bar p\})}$ and $a_1^{(\{\bar p\})}$ were
> already computed in [8], 5.6.**

`[8]` is Dryden–Gordon–Greenwald–Webb.

**Verdict: identical under the relabelling $m\leftrightarrow k$.** Same two terms, same
denominators 360 and 36, same $(x-1/x)$ shape, same single power of $K$. The manuscript's
footnote — that this is "the cone-point coefficient $a_1(\{\bar p\})$ of Schueth, Remark 4.2
(there attributed to Dryden–Gordon–Greenwald–Webb, §5.6)" — is accurate in every particular,
including the section number.

- Schueth, *On the corner contributions to the heat coefficients of geodesic polygons*,
  Ann. Inst. Fourier (Grenoble) **69** (2019), no. 7, 2827–2855.
  DOI [`10.5802/aif.3338`](https://doi.org/10.5802/aif.3338), arXiv:1812.06119.

### Checked independently at the original source

DGGW §5.6 is titled "**Example. Calculating heat invariants for 2-orbifolds**". It derives
$b_1(\gamma^j)=R_{1212}/(8\sin^4(j\pi/m))$, then applies
$\sum_{j=1}^{m-1}\sin^{-4}(j\pi/m)=(m^4+10m^2-11)/45$ to reach the per-cone-point
contribution $R_{1212}\,(m^4+10m^2-11)/(360m)$ in their equation (5.10).

Expanding that:

$$\frac{m^4+10m^2-11}{360m}=\frac{m^3}{360}+\frac{m}{36}-\frac{11}{360m}
=\frac1{360}\Bigl(m^3-\frac1m\Bigr)+\frac1{36}\Bigl(m-\frac1m\Bigr).$$

**DGGW's form and Schueth's form are algebraically the same expression.** Two independent
routes to equation (4).

- Dryden, Gordon, Greenwald & Webb, *Asymptotic expansion of the heat kernel for orbifolds*,
  Michigan Math. J. **56** (2008), no. 1, 205–238.
  DOI [`10.1307/mmj/1213972406`](https://doi.org/10.1307/mmj/1213972406), arXiv:0805.3148.

### The $b_0$ term and the normalization, also checked

DGGW **Example 5.3**, verbatim:

> $b_0(\gamma^j)=|\det((I-A_{\gamma^j})^{-1})|=1/(2-2\cos(2j\pi/m))=1/(4\sin^2(j\pi/m))$

which is the manuscript's $b_0(\gamma^j)=\tfrac14\csc^2(j\pi/m)$ exactly. With their Lemma 5.4
($\sum\sin^{-2}(j\pi/m)=(m^2-1)/3$) and division by the isotropy order, DGGW's own prose gives
"a simple cone point of order $m$ contributes $(1/m)\cdot(m^2-1)/12$" — the manuscript's
$\operatorname{cone}(m)=(m^2-1)/(12m)$. Their equation (5.7),
$\chi(\mathcal O)/6+\sum_i(m_i^2-1)/(12m_i)$, is the manuscript's equation (3).

On normalization, DGGW Definition 4.7 assigns each stratum the prefactor
$(4\pi t)^{-\dim N/2}$. A cone point has $\dim N=0$, so it carries **no** $(4\pi t)^{-1}$
prefactor — exactly the manuscript's §1.2 convention. Schueth's equation (17),
$a_\ell^{(\{\bar p\})}=\frac1k\sum_{j=1}^{k-1}b_\ell(\Phi^j)$, carries the $1/k$ isotropy
average, again as the manuscript states.

**No sign or factor convention differs between the two sources.** DGGW fix their curvature
sign convention explicitly ("$R_{abab}$ is the sectional curvature of the plane spanned by
$e_a$ and $e_b$"), so $R_{1212}=K$ for a constant-curvature surface, including $K=-1$;
Schueth simply writes $K(\bar p)$.

## 2. Equation (5): confirmed

Summing equation (4) over the three cone points at $K=-1$ returns

$$\sum_i b_1(C_i)\Big|_{K=-1}=-\tfrac1{360}P_3-\tfrac1{36}S_1+\tfrac{11}{360}R,$$

which is equation (5) as printed. Verified symbolically in exact rational arithmetic.

## 3. Higher $\ell$ — the critical question

### DGGW stop at $\ell=1$

A full-text search of DGGW returns **no** general-$\ell$ statement and nothing at all for
$\ell\ge2$. They compute the $t^{-1}$, $t^{-1/2}$, $t^0$, $t^{1/2}$ and $t^1$ coefficients and
stop. Their Tables 1–2 never even evaluate the $t^1$ coefficient numerically. So DGGW alone
cannot support the extension.

### Schueth supplies $\ell=2$ in closed form

**Schueth, Theorem 4.1** — verbatim:

> Let $\bar p \in (\mathcal O, g)$ be a cone point of order $k \in \mathbb N$ as above. Then
> $$a^{(\{\bar p\})}_{2}=\Bigl[\tfrac{1}{2520}\bigl(k^{5}-\tfrac1k\bigr)+\tfrac{1}{720}\bigl(k^{3}-\tfrac1k\bigr)+\tfrac{1}{180}\bigl(k-\tfrac1k\bigr)\Bigr]K(\bar p)^{2}$$
> $$-\Bigl[\tfrac{1}{15120}\bigl(k^{5}-\tfrac1k\bigr)+\tfrac{1}{1440}\bigl(k^{3}-\tfrac1k\bigr)+\tfrac{1}{180}\bigl(k-\tfrac1k\bigr)\Bigr]\Delta_{g}K(\bar p).$$

At constant curvature $\Delta_gK\equiv0$ and the entire second bracket vanishes. At $K=-1$
(so $K^2=+1$), summing over the cone points of a hyperbolic orbisurface:

$$\sum_i a_2(C_i)\Big|_{K=-1}=\tfrac{1}{2520}\bigl(P_5-R\bigr)+\tfrac{1}{720}\bigl(P_3-R\bigr)+\tfrac{1}{180}\bigl(S_1-R\bigr).$$

**So the fourth heat coefficient delivers $P_5=\sum_i m_i^5$, with nonzero coefficient
$1/2520$, modulo the already-known $(R,S_1,P_3)$.**

### Uçar supplies every $\ell$

This is the decisive finding, and it is stronger than the brief anticipated.

Uçar's thesis was read in full (156 pp., 54,887 words, recovered from the Humboldt
repository). The operative result is **equation (4.25) on p. 134 together with equation
(4.33) on p. 137**: a finite Bernoulli-number sum, **explicit for every $\ell\ge0$**.

Schueth independently attests to this. **Remark 5.4(ii)**, verbatim:

> In the case of constant curvature $K=1$, the above formulas (21), (22), (23) — even for
> general $\gamma\in(0,2\pi]$ — were proved by Watson [19]. In the case of arbitrary constant
> curvature $K\in\mathbb R$ the same was proved by Uçar in [17] … **Those authors actually
> computed $c_\ell(\gamma)$ for every $\ell\in\mathbb N_0$** in the case $K=1$, resp.
> $K\in\mathbb R$ constant. It turns out that for constant curvature $K$, one has
> **$c_\ell(\gamma)=f_\ell(\gamma)\cdot K^{\ell}$ for certain rational functions $f_\ell$.**

Schueth's Remark 5.2 relates the two normalizations: $c_\ell(\pi/k)=\tfrac12\,a_\ell^{(\{\bar p\})}$.

### The chain, evaluated

Evaluating Uçar (4.25)+(4.33) at $\ell=1,2,3$, with $b_\ell=K^\ell\frac1m p_\ell(m)$:

| $\ell$ | $p_\ell(m)$ | $\deg p_\ell$ | leading coeff | $b_\ell$ leading term | delivers |
|---|---|---|---|---|---|
| 1 | $\frac{m^4-1}{360}+\frac{m^2-1}{36}$ | 4 | $1/360$ | $\frac{1}{360}m^3K$ | $P_3$ |
| 2 | $\frac{2m^6+7m^4+28m^2-37}{5040}$ | 6 | $1/2520$ | $\frac{1}{2520}m^5K^2$ | $P_5$ |
| 3 | $\frac{3m^8+8m^6+14m^4+32m^2-57}{30240}$ | 8 | $1/10080$ | $\frac{1}{10080}m^7K^3$ | $P_7$ |

Degrees $4,6,8$ confirm $\deg p_\ell=2\ell+2$. Each $p_\ell(1)=0$, the sanity check that a
trivial cone contributes nothing.

**The $\ell=2$ row is independently cross-validated.** Converting Uçar's $p_2$ via
$b_2=K^2\frac1mp_2(m)$ and comparing symbolically against Schueth's Theorem 4.1 at constant
curvature, the difference simplifies **identically to zero**. Two sources, two different
methods — Uçar's Green kernel for a geodesic wedge in the hyperbolic plane, Schueth's
Donnelly-style distance-function expansion — agreeing exactly. The $\ell=3$ row rests on Uçar
alone, since Schueth stops at $\ell=2$.

Summed at $K=-1$ over the cone points of a hyperbolic orbisurface:

$$\textstyle\sum b_1=-\frac{P_3}{360}-\frac{S_1}{36}+\frac{11R}{360}$$
$$\textstyle\sum b_2=\frac{P_5}{2520}+\frac{P_3}{720}+\frac{S_1}{180}-\frac{37R}{5040}$$
$$\textstyle\sum b_3=-\frac{P_7}{10080}-\frac{P_5}{3780}-\frac{P_3}{2160}-\frac{S_1}{945}+\frac{19R}{10080}$$

The first line is equation (5). The next two extend it, each introducing its new power sum
with a nonzero rational coefficient.

**Answers to the brief's four sub-questions:**

- *What is established for $\ell=2,3$ at constant curvature?* Explicit closed forms. $\ell=2$
  twice over (Schueth Thm 4.1; Uçar), $\ell=3$ via Uçar.
- *Do the higher coefficients yield $P_5$ and $P_7$?* Yes, both, with nonzero coefficients
  $1/2520$ and $-1/10080$ at $K=-1$.
- *Is $p_\ell(m)$ explicitly computed for $\ell\ge2$, or only its degree?* **Explicitly
  computed, for all $\ell$.** The degree-only reading understates what Uçar proved.
- *Is the leading term of $p_\ell$ known in closed form?* Yes — via $f_\ell$ in
  $c_\ell(\gamma)=f_\ell(\gamma)K^\ell$, whose leading behaviour at $\gamma=\pi/k$ is
  $\sim k^{2\ell+1}$, giving the $1/360$, $1/2520$, $1/10080$ pattern above.

---

## 4. Verdict on the planned $K \le n+1$ theorem

> **It is provable from established inputs. No new cone-coefficient computation is required.**

For one coefficient beyond the manuscript's current three, cite Schueth Theorem 4.1. For
arbitrarily many, cite Uçar (4.25)+(4.33), corroborated by Schueth's Remark 5.4(ii).

The residual work is **algebraic, not analytic**: showing that
$(R,S_1,P_3,P_5,\dots,P_{2n-3})$ determines the multiset $\{m_1,\dots,m_n\}$ — which is
exactly the "when these are independent" hedge in the manuscript's Remark 5.6. That is a
symmetric-function question, not a heat-kernel question, and it is where the effort should go.

### A concrete gain that comes free

An independent exact-arithmetic enumeration run during this sweep found that

$$\mathcal O(3,10,15,30)\quad\text{and}\quad\mathcal O(4,5,21,28)$$

are non-isometric 4-cone hyperbolic pillows sharing $S_1=58$, $R=8/15$ and $P_3=31402$ —
hence sharing their **first three heat coefficients** — and separated by
$P_5$ ($25{,}159{,}618$ vs $21{,}298{,}618$). Both are hyperbolic ($4-8/15=52/15>2$).

Combined with Schueth's Theorem 4.1, which makes $P_5$ the fourth coefficient, this gives
$K=4$ exactly for these two orbifolds — **the matching lower bound that Remark 5.6 leaves
open, settled for $n=4$ with an explicit witness.** Over all 4-cone pillows with orders
$\le60$ (395,009 multisets) this pair and its $\times2$ scaling are the only $(R,S_1,P_3)$
collisions, so $S_1=58$ is minimal in that range.

For $n=5$ the corresponding minimal three-invariant collision is
$\mathcal O(3,7,7,7,14)$ vs $\mathcal O(4,4,6,12,12)$ ($S_1=38$, $R=5/6$, $P_3=3800$), but no
pair sharing four invariants was found up to order 26, so the $n=5$ case of Remark 5.6
remains open.

Full details, including the caveat structure, in `research/temp/original-computation-ncone.md`.

---

## 5. Two corrections for the manuscript

**(a) The Uçar attribution should cite equations, not paraphrase.** Uçar never writes
"$b_\ell(C)=\kappa^\ell\frac1mp_\ell(m)$" and never uses the word *degree*. That form is a
faithful consequence of his Bernoulli-number formula, but it is the manuscript's own
phrasing. Cite (4.25) p. 134 and (4.33) p. 137.

**(b) There is an uncited DGGW erratum.** Dryden, Gordon, Greenwald & Webb, *Erratum to
"Asymptotic expansion of the heat kernel for orbifolds"*, Michigan Math. J. **66** (2017),
221–222, DOI [`10.1307/mmj/1488510034`](https://doi.org/10.1307/mmj/1488510034).

It was checked in full. It corrects **only Theorem 5.1**, adding the hypothesis that
$\mathrm{Iso}_{\max}(N)$ be nontrivial (strata with trivial maximal isotropy do not appear in
the heat invariants; the counterexample is $\mathbb R^3$ modulo the Klein four-group of
coordinate-axis rotations). **It does not touch §5.6, equations (5.7)–(5.10), or any
cone-point coefficient.** So equation (4) is unaffected — but the erratum exists, it is
citable, and a referee who knows the paper knows about it.

A detail worth knowing: the erratum opens by crediting *"a question from Naveed Bari"* — the
Bari of Bari–Hunsicker, the manuscript's designated closest competitor. The paper's two most
important sources are in direct contact with each other.

**Minor:** Schueth's own bibliography prints the DGGW reference as "*Michigan J. Math.*",
transposed from the standard "*Michigan Math. J.*". The manuscript's form is correct.

---

## Sources

| Work | Identifier |
|---|---|
| Schueth, Ann. Inst. Fourier **69** (2019) 2827–2855 | [`10.5802/aif.3338`](https://doi.org/10.5802/aif.3338) · arXiv:1812.06119 |
| Dryden–Gordon–Greenwald–Webb, Michigan Math. J. **56** (2008) 205–238 | [`10.1307/mmj/1213972406`](https://doi.org/10.1307/mmj/1213972406) · arXiv:0805.3148 |
| DGGW **Erratum**, Michigan Math. J. **66** (2017) 221–222 | [`10.1307/mmj/1488510034`](https://doi.org/10.1307/mmj/1488510034) |
| Uçar, PhD thesis, Humboldt-Universität zu Berlin, 2017 | [`10.18452/18463`](https://doi.org/10.18452/18463) · `urn:nbn:de:kobv:11-110-18452` · arXiv:1711.03405 |
| Donnelly, Math. Ann. **224** (1976) 161–170 | [`10.1007/BF01436198`](https://doi.org/10.1007/BF01436198) |
| Schueth, Ann. Global Anal. Geom. **69** (2026), Paper No. 2 | arXiv:2511.22255 |

Watson, *The trace function expansion for spherical polygons*, New Zealand J. Math. **34**
(2005), 81–95 — the $K=1$ predecessor — could not be retrieved; see
`review/outstanding-fetches.md`. It is not cited by the manuscript and is not needed: the
all-$\ell$ claim was verified firsthand from Uçar and cross-validated against Schueth.
