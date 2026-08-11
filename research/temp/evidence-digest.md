# Evidence digest

Top claims with the verbatim support behind them. Each entry names the source read, the
identifier, and the exact words. This is the substrate the deliverables are built on; if a
claim in `review/hyperresearch/` is not traceable to an entry here or to a cited record, it
does not belong.

---

## E1 — Schueth Remark 4.2 confirms equation (4)

> Analogously, one could derive that $a_0^{(\{\bar p\})} = \frac{1}{12}(k-\frac1k)$,
> $a_1^{(\{\bar p\})} = \bigl[\frac{1}{360}(k^{3}-\frac1k)+\frac{1}{36}(k-\frac1k)\bigr]K(\bar p)$,
> for an orbisurface cone point $\bar p \in (\mathcal O, g)$ of order $k$ … **Note that the
> above formulas for $a_0^{(\{\bar p\})}$ and $a_1^{(\{\bar p\})}$ were already computed in
> [8], 5.6.**

Source: arXiv:1812.06119, ar5iv full text. Published Ann. Inst. Fourier **69** (2019) 2827–2855,
`10.5802/aif.3338`. `[8]` = DGGW.
**Supports:** Q2 §1, VERDICT answer 2.

## E2 — DGGW §5.6 reaches the same expression independently

DGGW derive $b_1(\gamma^j)=R_{1212}/(8\sin^4(j\pi/m))$ and, via
$\sum_{j=1}^{m-1}\sin^{-4}(j\pi/m)=(m^4+10m^2-11)/45$, the per-point contribution
$R_{1212}(m^4+10m^2-11)/(360m)$ (their eq. 5.10). Expanding:
$\frac{m^4+10m^2-11}{360m}=\frac1{360}(m^3-\frac1m)+\frac1{36}(m-\frac1m)$.

Source: arXiv:0805.3148 full text; Michigan Math. J. **56** (2008) 205–238,
`10.1307/mmj/1213972406`.
**Supports:** Q2 §1 — the independent confirmation, which is what makes the verdict strong
rather than merely sourced.

## E3 — DGGW Example 5.3 gives $b_0$ verbatim

> $b_0(\gamma^j)=|\det((I-A_{\gamma^j})^{-1})|=1/(2-2\cos(2j\pi/m))=1/(4\sin^2(j\pi/m))$

**Supports:** Q2 §1, the $\operatorname{cone}(m)=(m^2-1)/(12m)$ chain.

## E4 — Schueth Theorem 4.1, the $t^2$ cone coefficient

> $a^{(\{\bar p\})}_{2}=\bigl[\frac{1}{2520}(k^{5}-\frac1k)+\frac{1}{720}(k^{3}-\frac1k)+\frac{1}{180}(k-\frac1k)\bigr]K(\bar p)^{2}
> -\bigl[\frac{1}{15120}(k^{5}-\frac1k)+\frac{1}{1440}(k^{3}-\frac1k)+\frac{1}{180}(k-\frac1k)\bigr]\Delta_{g}K(\bar p)$

At constant curvature $\Delta_gK\equiv0$, so the second bracket vanishes identically.
**Supports:** Q2 §3, VERDICT answer 3 — this is what makes $P_5$ a heat invariant.

## E4b — Uçar's two operative equations, verbatim

**(4.25), p. 134:**
> $c^S_\ell(\pi/k) = \frac{1}{4k}\cdot\frac{(-1)^\ell}{(\ell+1)!}\cdot\frac{1}{2\ell+1}\sum_{j=0}^{\ell+1}\binom{2\ell+2}{2j}(k^{2j}-1)B_{2j}B_{2\ell+2-2j}(\tfrac12)$

**(4.33), p. 137**, Corollary 4.19(ii), with **Theorem 4.20(ii)** identifying this series as
the contribution of a cone point of order $k$:
> $C=\sum_{\nu}\Bigl[\sum_{\ell=0}^{\nu}\frac{2}{4^\ell \ell!}c^S_{\nu-\ell}(\pi/k)\Bigr]\kappa^\nu t^\nu$

Note Uçar never writes "$p_\ell$" or "degree" — the manuscript's phrasing is a paraphrase of
these two equations, faithful but not a quotation.
Source: arXiv:1711.03405 / DOI `10.18452/18463`, full thesis text.
**Supports:** Q2 §3 — and these are the equations the $\ell=3$ evaluation was computed from
first-hand, rather than accepted on report.

## E5 — Schueth Remark 5.4(ii), the all-$\ell$ statement

> In the case of constant curvature $K=1$ … proved by Watson [19]. In the case of arbitrary
> constant curvature $K\in\mathbb R$ the same was proved by Uçar in [17] … **Those authors
> actually computed $c_\ell(\gamma)$ for every $\ell\in\mathbb N_0$** … one has
> $c_\ell(\gamma)=f_\ell(\gamma)\cdot K^{\ell}$ for certain rational functions $f_\ell$.

**Supports:** Q2 §3, VERDICT answer 3. This is the sentence that converts "degree known" into
"coefficients known", and it is a second author's testimony about Uçar's thesis, corroborating
the direct reading of that thesis.

## E6 — Uçar's determinacy theorem carries no coefficient count

Corollary 4.21 p. 139 (Corollary 4.23 p. 140 the orientable specialization, generalizing
Dryden–Strohmaier from $\kappa=-1$ to all $\kappa\neq0$). The hypothesis is always "$\kappa$
together with the spectrum" — the full spectrum. No coefficient count anywhere. Neither
$(2,8,8)$ nor $(3,3,12)$ nor the terms "power sum", "collision", "near-isospectral" occur.

Source: arXiv:1711.03405, full thesis (54,887 words) read from the Humboldt repository copy.
DOI `10.18452/18463`.
**Supports:** Q3 §2, VERDICT answer 4.

## E7 — Bari–Hunsicker is a negative, all-order, spherical result

> Then $O_1 = S^3/G_1$ and $O_2 = S^3/G_2$ will have the exact same asymptotic expansion of
> the heat kernel if $\alpha_1 = \alpha_2$ and $\beta_1 = \beta_2$.

Lemma 6.5 / Example 6.6 (dim 3), Lemma 6.7 / Example 6.8 (dim 4); the proof establishes this
"for any $k$". Setting is spherical space forms throughout. Example $q=195$ is offered as "a
tool to find examples", with no minimality claim.

Source: arXiv:1705.01412 full text; Canad. J. Math. **72** (2020) 281–325,
`10.4153/S0008414X19000178`.
**Supports:** Q3 §1, VERDICT answer 4.

## E8 — Doyle–Rossetti call the finite-coefficient question open

> Restricted to hyperbolic 2-orbifolds, the results [DGGW] state don't yield complete
> information about the singular set. All this information is there … presumably it could be
> extracted … by looking at **higher and higher terms** in the asymptotic expansion.

And Theorem 1:

> The Laplace spectrum of $M$ determines, and is determined by, the following data: 1. the
> volume; 2. the total length of the mirror boundary; 3. the number of conepoints of each
> order, counting a mirror corner as half a conepoint of the corresponding order; 4. the
> number of closed geodesics of each length and orientability class.

Source: arXiv:1103.4372 full text. Never published; DataCite `10.48550/arXiv.1103.4372`.
**Supports:** Q3 §3 — the strongest positive evidence for the priority claim, and
simultaneously the §1.3(a) attribution correction.

## E9 — Dryden–Strohmaier got there in 2009

> Let $\mathcal O$ be a compact orientable hyperbolic orbisurface. The Laplace spectrum of
> $\mathcal O$ determines its length spectrum and the **number of cone points of each possible
> order**.

Theorem 1.1. Exact — no "up to finitely many" hedge.
Source: arXiv:math/0504571; Canad. Math. Bull. **52** (2009) 66–71, `10.4153/CMB-2009-008-0`.
**Supports:** Q3 §3.5, VERDICT answer 4 — this is the eight-year attribution error.

## E10 — Guy §D16, the nearest known relative

> The problem to find as many different triples of positive integers as possible with the same
> sum and the same product has been solved by Schinzel: you can have arbitrarily many.

With Schinzel's construction using rational points on $y^2=x^3-9x+9$ (Cremona 324C1, rank 1).
D11 = Egyptian fractions p. 252; **D12 = Markoff numbers p. 263**; D16 p. 271; D28 p. 309.
Source: Guy, UPINT 3rd ed., `10.1007/978-0-387-26677-0`; subsection list from the Deutsche
Nationalbibliothek deposited front matter, body text cross-checked.
**Supports:** Q1 §2–3, VERDICT answer 1.

## E11 — the OEIS null is controlled

Numeric search control: Fibonacci → A000045. Keyword search control: "census-taker number" →
**A334911**, "Numbers $k$ such that exactly two unordered triples of positive numbers have
product $k$ and equal sums". The same method finds the equal-sum-equal-**product** problem and
not the equal-sum-equal-**reciprocal-sum** one.
**Supports:** Q1 §2 — without the control the null is inadmissible.

## E12 — Linowitz–Voight: isospectral hyperbolic 2-orbifolds exist

> The minimal area of an isospectral-nonisometric pair of 2-orbifolds associated to maximal
> arithmetic Fuchsian groups is $23\pi/6$, and this bound is achieved by exactly three pairs,
> up to isomorphism.

Theorem A. All three have signature $(0;2,2,2,2,2,3,4)$ — seven cone points, not three.
Source: arXiv:1408.2001; Math. Z. **281** (2015) 523–569, `10.1007/s00209-015-1500-1`.
**Supports:** Q3 §4 — the context the manuscript is missing, and the reason to state results
narrowly.

## E13 — Batenkov–Yomdin already have the manuscript's Q4 structure

Lemma 4.2 factors the Prony-map Jacobian through the confluent Vandermonde matrix.
Corollary 4.3: critical points are exactly node collisions. Theorem 4.5: local accuracy scales
"roughly of the same order as some finite power of $\prod_{i<j}|\xi_j-\xi_i|^{-1}$", matching
the Cramér–Rao bound.
Source: arXiv:1106.1137, SIAM J. Appl. Math.
**Supports:** Q4 §2.4, VERDICT answer 5 — the technique-novelty verdict rests on this.

## E14 — the Q4 orbifold null, with its queries

Eight arXiv queries, listed verbatim in `Q4-stability.md` §4, returning zero or off-topic. The
one orbifold-setting hit is Lassas–Lu–Yamaguchi arXiv:2404.16448, whose Theorem 1.2 gives a
triple-logarithmic modulus for *continuous metric* reconstruction from interior eigenfunction
data.
**Supports:** Q4 §4, VERDICT answer 5.

## E14b — the moduli count behind the $K(F)$ correction

The claim that $K(F)$ is ill-defined for $n\ge4$ rests on the deformation theory of
constant-curvature cone metrics: the moduli space of such metrics on the sphere with $n$
prescribed cone angles has complex dimension $n-3$, hence real dimension $2n-6$ — zero exactly
when $n=3$.

Citable sources: **Thurston, *Shapes of polyhedra and triangulations of the sphere*, Geom.
Topol. Monogr. **1** (1998), 511–549, DOI `10.2140/gtm.1998.1.511`**, and **Troyanov,
*Prescribing curvature on compact surfaces with conical singularities*, Trans. Amer. Math.
Soc. **324** (1991), 793–821, DOI `10.1090/S0002-9947-1991-1005085-9`**.

The second half of the argument needs no citation: every heat-trace coefficient of a
constant-curvature cone orbifold is a function of the cone orders alone — the area is fixed by
Gauss–Bonnet, and each cone contributes through its order via the formulas of E1–E5. So a
positive-dimensional family sharing a multiset shares every coefficient.

**Supports:** Q2's boxed correction, VERDICT answer 3, corrections item 18.

## E15 — the JGA exemplar

> for almost all convex polygonal domains, there exist at most finitely many non-congruent
> domains with the same Steklov spectrum. Moreover, we obtain explicit upper bounds…

Dryden, Gordon, Moreno, Rowlett, Villegas-Blas, JGA **35**(3) art 91 (2025),
`10.1007/s12220-025-01922-8`, ~18,000 words. Two authors are DGGW co-authors; the paper claims
no priority.
**Supports:** Q5 §2–4, VERDICT answer 6.

---

## Claims verified by independent computation, not by a source

Recorded separately because their warrant is different in kind.

| Claim | Method |
|---|---|
| eq. (5) follows from eq. (4) at $K=-1$ | symbolic, sympy |
| $a_0=(S_1+R-2)/12$; $a_0(2,3,5)=271/360$ | symbolic + exact rational |
| $\det DF$ as printed at line 269 | symbolic |
| Newton–Vieta recovery, eq. (9) | symbolic |
| cotangent and cosecant identities, $m\le12$ | symbolic + 40-digit mpmath |
| Table 5.1 pair counts 1, 92, 386, 840, 1496, 2210, 3067 | exact `Fraction` enumeration |
| "class" counts = distinct colliding signatures: 92, 380, 822, 1468, 2158, 2977 | exact enumeration, six conventions tested |
| first triple degeneracy at $S=136$, $R=1/10$ | exact enumeration |
| $S=36$ has exactly two classes, one primitive | exact enumeration |
| Uçar $p_2$ ≡ Schueth Thm 4.1 at constant curvature | symbolic, difference simplifies to 0 |
| $b_0,b_1,b_2,b_3$ evaluated from Uçar (4.25)+(4.33) as printed | symbolic; $\ell=0,1$ regenerate $\operatorname{cone}(m)$ and eq. (4), so the reading of the formula is self-checking |
| class-count convention = distinct colliding signatures | six conventions enumerated, one matches |
| **the invariant map is a Prony system**: $\sum_i(1/m_i)(m_i^2)^j=R,S_1,P_3,P_5,P_7$ for $j=0..4$ | symbolic, all five orders |
| $\det DF=-3\,\mathrm{Vandermonde}(p^2,q^2,r^2)/(pqr)^2$ | symbolic, identical to the manuscript's printed form |
| $n=4$ witness $(3,10,15,30)$ / $(4,5,21,28)$, minimal to order 60 | exact enumeration, 395,009 multisets |
| all 53 DOIs in `refs/sources.bib` resolve | Crossref + DataCite API |
| **the whole §3 interval-separation proof** — see below | exact `Fraction` arithmetic |

### §3 verified line by line

Every displayed quantity in the manuscript's central proof was recomputed:

| Manuscript claim | Recomputed | ✓ |
|---|---|---|
| $\tau_2=1/6$, $\varphi_2(17)=29/165>\tau_2$ | $29/165$ | ✓ |
| $\varphi_2(18)=1/6$ **exactly** | $1/6$ | ✓ |
| $\tau_3=1/6$, $\varphi_3(12)=7/36$, $\varphi_3(17)=11/63$ | both, both $>\tau_3$ | ✓ |
| $\tau_4=3/20$, $\min\{\varphi_4(15..17)\}=\varphi_4(15)=9/55$ | $9/55>3/20$ | ✓ |
| $\varphi_p$ unimodal, peak at $S=3p+4$ | argmax $=10,13,16$ for $p=2,3,4$ | ✓ |
| $R^-_{18,3}=101/168>3/5=R^+_{18,4}$ | exact | ✓ |
| $R^-_{18,4}=15/28>21/40=R^+_{18,5}$ | exact | ✓ |
| $R^-_{18,5}=107/210>1/2=R^+_{18,6}$ | exact | ✓ |
| first contact: $R^-_{18,2}=R^+_{18,3}=3/4$, i.e. $\mathcal O(2,8,8)$ meets $\mathcal O(3,3,12)$ | exact | ✓ |
| no hyperbolic triad with $S_1\le9$; $S_1=10$ only $(3,3,4)$ | confirmed; $S_1=11$ gives exactly $(2,4,5),(3,3,5),(3,4,4)$ | ✓ |

So the verification covers not only the displayed equations but the entire logical spine of
Theorems A and B.
