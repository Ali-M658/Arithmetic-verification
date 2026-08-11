# Q2 — verbatim extraction from Schueth, arXiv:1812.06119

Source read directly by the orchestrator from the ar5iv full-text mirror of
arXiv:1812.06119 (note `181206119-schueth-corner-contributions-ar5iv-fulltext`).
Published as *Ann. Inst. Fourier (Grenoble)* **69** (2019), no. 7, 2827–2855
(journal-ref taken from the arXiv API record, not from memory).

Everything below is quoted from the source body, not from any summary of it.

## 1. Remark 4.2 — verbatim

> Analogously, one could derive that
> $$a_0^{(\{\bar p\})} = \tfrac{1}{12}\Bigl(k-\tfrac1k\Bigr),$$
> $$a_1^{(\{\bar p\})} = \Bigl[\tfrac{1}{360}\Bigl(k^{3}-\tfrac1k\Bigr)+\tfrac{1}{36}\Bigl(k-\tfrac1k\Bigr)\Bigr]K(\bar p),$$
> for an orbisurface cone point $\bar p \in (\mathcal O, g)$ of order $k$, using
> $\sum_{j=1}^{k-1}\frac{1}{\sin^2(j\cdot\pi/k)}=\frac13(k^2-1)$ and
> $b_0(\Phi)=\frac1C$, $b_1(\Phi)=\frac{2}{C^2}K(p)$.
>
> **Note that the above formulas for $a_0^{(\{\bar p\})}$ and $a_1^{(\{\bar p\})}$ were
> already computed in [8], 5.6.**

where `[8]` is Dryden–Gordon–Greenwald–Webb.

### Verdict on the manuscript's equation (4)

The manuscript prints, at `paper/main.tex` line 237:

$$b_1(C)=\Bigl[\tfrac1{360}\bigl(m^3-\tfrac1m\bigr)+\tfrac1{36}\bigl(m-\tfrac1m\bigr)\Bigr]K$$

This is **character-for-character Schueth's $a_1^{(\{\bar p\})}$** under the relabelling
$m \leftrightarrow k$. Same two terms, same denominators 360 and 36, same $(\cdot - 1/\cdot)$
shape, same single factor of $K$. **Equation (4) is correct as printed.** The manuscript's
footnote attribution — "the cone-point coefficient $a_1(\{\bar p\})$ of Schueth, Remark 4.2
(there attributed to Dryden–Gordon–Greenwald–Webb, §5.6)" — is also exactly right: Schueth's
own closing sentence in Remark 4.2 makes precisely that attribution, to §5.6.

The manuscript's $b_0$ likewise matches: Schueth's $a_0^{(\{\bar p\})} = \frac1{12}(k-\frac1k)$
is the manuscript's $\operatorname{cone}(m)=\frac{m^2-1}{12m}=\frac1{12}(m-\frac1m)$
(Corollary 2.5).

### Equation (5) — the K = −1 specialization

Verified symbolically by the orchestrator: summing equation (4) over the three cone points
at $K=-1$ gives exactly
$$\sum_i b_1(C_i)\Big|_{K=-1}=-\tfrac1{360}P_3-\tfrac1{36}S_1+\tfrac{11}{360}R,$$
which is the manuscript's equation (5) as printed. Confirmed.

## 2. Normalization — Remark 3.2 and equation (17)

Equation (17), verbatim:

> In the case $N=\{\bar p\}$, where $\bar p \in \mathcal O$ is a cone point of order
> $k \in \mathbb N$, arising from a rotation $\Phi$ with angle $\varphi := 2\pi/k$, one has
> $\operatorname{dim}(N)=0$ and
> $$a^{(\{\bar p\})}_{\ell}=\frac{1}{k}\sum_{j=1}^{k-1}b_{\ell}(\Phi^{j}),$$
> where the $b_\ell$ are as in 3.1 (see [8], 4.5–4.8 & Example 5.3).

The stratum series carries the prefactor $(4\pi t)^{-\dim(N)/2}$, so for a cone point
$\dim(N)=0$ and **there is no $(4\pi t)^{-1}$ prefactor** — exactly the manuscript's
convention in §1.2 and §2.1. The $\frac1k$-average over the $k-1$ nontrivial rotations is
built in, again as the manuscript states.

## 3. THE LOAD-BEARING FINDING — Theorem 4.1, the $t^2$ cone coefficient

Verbatim:

> **Theorem 4.1.** Let $\bar p \in (\mathcal O, g)$ be a cone point of order $k \in \mathbb N$
> as above. Then
> $$a^{(\{\bar p\})}_{2}=\Bigl[\tfrac{1}{2520}\bigl(k^{5}-\tfrac1k\bigr)+\tfrac{1}{720}\bigl(k^{3}-\tfrac1k\bigr)+\tfrac{1}{180}\bigl(k-\tfrac1k\bigr)\Bigr]K(\bar p)^{2}$$
> $$-\Bigl[\tfrac{1}{15120}\bigl(k^{5}-\tfrac1k\bigr)+\tfrac{1}{1440}\bigl(k^{3}-\tfrac1k\bigr)+\tfrac{1}{180}\bigl(k-\tfrac1k\bigr)\Bigr]\Delta_{g}K(\bar p).$$

**At constant curvature $\Delta_g K \equiv 0$, so the entire second bracket vanishes** and

$$a_2^{(\{\bar p\})}\Big|_{\text{const.\ curv.}}=\Bigl[\tfrac{1}{2520}\bigl(k^{5}-\tfrac1k\bigr)+\tfrac{1}{720}\bigl(k^{3}-\tfrac1k\bigr)+\tfrac{1}{180}\bigl(k-\tfrac1k\bigr)\Bigr]K^{2}.$$

At $K=-1$, $K^2=+1$, and summing over the cone points of a hyperbolic orbisurface:

$$\sum_i a_2(C_i)\Big|_{K=-1}=\tfrac{1}{2520}\bigl(P_5-R\bigr)+\tfrac{1}{720}\bigl(P_3-R\bigr)+\tfrac{1}{180}\bigl(S_1-R\bigr).$$

**So the fourth heat coefficient delivers $P_5=\sum_i m_i^5$, with nonzero rational
coefficient $1/2520$, modulo the already-known $(R, S_1, P_3)$.** This is exactly the
pattern the manuscript's Corollary D establishes at the previous order, extended one step,
and it is *already in the literature* — Schueth proved it in 2019.

## 4. Higher $\ell$ — Remark 5.4(ii), verbatim

> (ii) In the case of constant curvature $K=1$, the above formulas (21), (22), (23) — even
> for general $\gamma \in (0,2\pi]$ — were proved by Watson [19]. In the case of arbitrary
> constant curvature $K \in \mathbb R$ the same was proved by Uçar in [17], the main
> breakthrough there being the computation of the Green kernel for an arbitrary geodesic
> wedge in the hyperbolic plane. **Those authors actually computed $c_\ell(\gamma)$ for
> every $\ell \in \mathbb N_0$** in the case $K=1$, resp. $K \in \mathbb R$ constant. It
> turns out that for constant curvature $K$, one has
> **$c_\ell(\gamma)=f_\ell(\gamma)\cdot K^{\ell}$ for certain rational functions $f_\ell$.**

And Remark 5.2 (referenced in the introduction) states that under the symmetry assumption,
each $c_\ell(\pi/k)$ is exactly $\tfrac12$ times the corresponding $a_\ell^{(\{\bar p\})}$.

**This is the answer to the question the prompt calls critical.** At constant curvature the
cone coefficients are known *explicitly, for every $\ell$*, not merely bounded in degree.
Uçar did not only establish $\deg p_\ell = 2\ell+2$; per Schueth's own account he computed
the coefficients themselves, for all $\ell$, at arbitrary constant curvature.

Consistency check, done by hand: Schueth's general-$\gamma$ formula (23) is
$$c_2(\gamma)=\Bigl(\tfrac{\pi^6-\gamma^6}{5040\gamma^5\pi}+\tfrac{\pi^4-\gamma^4}{1440\gamma^3\pi}+\tfrac{\pi^2-\gamma^2}{360\gamma\pi}\Bigr)K(p)^2-(\cdots)\Delta_gK(p).$$
Setting $\gamma=\pi/k$ in the leading term:
$\frac{\pi^6-\pi^6k^{-6}}{5040(\pi/k)^5\pi}=\frac{k^5(1-k^{-6})}{5040}=\frac{k^5-k^{-1}}{5040}$,
and doubling (Remark 5.2) gives $\frac{k^5-1/k}{2520}$ — exactly the leading bracket of
Theorem 4.1. The two routes agree, which is a good check that the $\gamma \to \pi/k$
specialization is the right one to use.

The same computation at general $\ell$ shows the leading term of $f_\ell$ carries
$\frac{\pi^{2\ell+2}-\gamma^{2\ell+2}}{c_\ell\,\gamma^{2\ell+1}\pi}$, which at $\gamma=\pi/k$
gives $\sim k^{2\ell+1}/c_\ell$ — i.e. $a_\ell \sim \text{const}\cdot k^{2\ell+1}K^\ell$,
consistent with Uçar's $b_\ell = K^\ell\frac1k p_\ell(k)$, $\deg p_\ell = 2\ell+2$.
**So the $\ell$-th coefficient delivers $P_{2\ell+1}$**, and the leading coefficient is
known in closed form via $f_\ell$.

## 5. What this means for the planned "K ≤ n+1" theorem

**It is provable from established inputs. No new cone-coefficient computation is required.**

- For one extra coefficient beyond the manuscript's current three, the needed formula is
  Schueth Theorem 4.1, printed above, published in Ann. Inst. Fourier 2019.
- For arbitrarily many, Schueth's Remark 5.4(ii) certifies that Uçar computed $c_\ell$ for
  every $\ell$ at arbitrary constant curvature. Those are the inputs.

The residual work is **not** analytic but algebraic: showing that
$(R, S_1, P_3, P_5, \dots, P_{2n-3})$ determines the multiset — i.e. discharging the
"when these are independent" hedge in the manuscript's Remark 5.6. That is a
symmetric-function argument, not a heat-kernel computation.

## 6. Minor bibliographic note

Schueth's own bibliography prints the DGGW reference as "*Michigan J. Math.*", transposed
from the standard "*Michigan Math. J.*" that the manuscript uses. The manuscript's form is
the correct one; no change needed, but worth knowing if a referee cross-checks against
Schueth's reference list.

## Still to confirm

- The Annales de l'Institut Fourier DOI for the published version (Centre Mersenne).
- Whether the DGGW erratum on disk touches §5.6 — if it does, both Schueth's quotation and
  the manuscript's equation (4) inherit the correction.
