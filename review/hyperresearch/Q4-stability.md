# Q4 — Quantitative stability in inverse spectral problems

**Short answer.** The *technique* is entirely standard and should be cited rather than
rebuilt — the manuscript's Jacobian is the classical conditioning quantity in disguise, and
the sharp separation-dependent bounds already exist in the Prony / super-resolution
literature. The *setting* is genuinely open: no stability theorem exists for recovering a
finite discrete invariant of an orbifold from approximate spectral data. Write the paper
around the setting and the integer-valuedness, cite the rest.

---

## 1. What the manuscript plans

Recover $(p,q,r)$ from approximate values of

$$S_1=p+q+r,\qquad R=\tfrac1p+\tfrac1q+\tfrac1r,\qquad P_3=p^3+q^3+r^3,$$

with explicit constants and a blow-up rate as the diagonals $p=q$, $p=r$, $q=r$ are
approached. The manuscript already records the Jacobian (§2.3):

$$\det DF=-\frac{3(p-q)(p-r)(q-r)(p+q)(p+r)(q+r)}{(pqr)^2},$$

verified symbolically during this review.

## 2. The technique is standard — chain, with citations at each link

### 2.1 Power sums → coefficients → roots

Tisseur & Van Barel, arXiv:2001.05281, equation (1.3): for a simple root $z_k$ of
$p(z)=\sum p_iz^i$,

$$\mathrm{err}(z_k)=\frac{|\Delta p(\hat z_k)|}{|z_k|\,|p'(\hat z_k)|},$$

which with their elementwise backward bound (1.4b) gives exactly the form the manuscript
wants: $|\delta z_k|\sim|\delta a_j|\,|z_k|^j/|p'(z_k)|$.

### 2.2 The manuscript's Jacobian *is* the classical conditioning quantity

For a monic cubic with roots $p,q,r$, $|p'(p)|=|(p-q)(p-r)|$. The pairwise-gap product in
$\det DF$ is therefore not a new object — it is $\prod_k|p'(z_k)|$ rearranged. Worth stating
plainly in the paper: the degeneracy on the diagonals is the classical ill-conditioning of
root-finding at coincident roots, specialized.

Citable lineage for continuity/perturbation of roots (via Ross, arXiv:2207.00123, which
itself proves only the *qualitative* statement): Ostrowski, *Solution of Equations in
Euclidean and Banach Spaces*, Academic Press 1973; Marden, *Geometry of Polynomials*, AMS
Math. Surveys **3** (1966); Rahman & Schmeisser, *Analytic Theory of Polynomials*, Clarendon
2002.

Wilkinson's original conditioning analysis: *The evaluation of the zeros of ill-conditioned
polynomials. Part I*, Numer. Math. **1** (1959), 150–166,
DOI [`10.1007/BF01386381`](https://doi.org/10.1007/BF01386381) (Part II
[`10.1007/BF01386382`](https://doi.org/10.1007/BF01386382)). Cite these rather than the 1963
book, which has no DOI.

### 2.3 Vandermonde conditioning

The Vandermonde matrix is the Jacobian of the power-sum map, so its condition number *is* the
conditioning of this recovery.

- Gautschi & Inglese, *Lower bounds for the condition number of Vandermonde matrices*,
  Numer. Math. **52** (1987), 241–250,
  DOI [`10.1007/BF01398878`](https://doi.org/10.1007/BF01398878):
  $\kappa_\infty(V_K)\ge(K-1)2^K$ for real positive nodes — which is exactly the
  manuscript's case — and $\ge2^{K/2}$ for symmetric real nodes.
- Pan, *How bad are Vandermonde matrices?*, arXiv:1504.02118: Theorem 8.1 gives an
  exponential lower bound explicitly in terms of a **separation parameter**.
- Aubel & Bölcskei, arXiv:1701.02538 (Appl. Comput. Harmon. Anal.): records Moitra's
  large-sieve bound $\kappa(V_{N\times K})^2\le\frac{N-1+1/\delta}{N-1-1/\delta}$ with
  $\delta$ the minimum node separation — condition number diverging explicitly as
  $\delta\to0$.

### 2.4 The best match, and the one to build on

**Batenkov & Yomdin, *On the accuracy of solving confluent Prony systems*, arXiv:1106.1137
(SIAM J. Appl. Math.)** is the manuscript's problem in another vocabulary: recover node
locations $\xi_i$ from noisy power moments $\sum_ia_i\xi_i^k=m_k$.

- **Lemma 4.2** factors the Jacobian of the Prony map as
  $J_{P_S}(x)=U(\xi_1,\dots)\cdot\mathrm{diag}\{D_1,\dots,D_K\}$, with $U$ the confluent
  Vandermonde matrix.
- **Corollary 4.3**: $x$ is a critical point of the Prony map **iff two nodes collide** (or a
  leading magnitude vanishes). This is *structurally identical* to the manuscript's Jacobian
  vanishing exactly on $p=q$, $p=r$, $q=r$.
- **Theorem 4.5**: local accuracy $\mathrm{ACC_{LOC}}=C_1\epsilon/|a_{i,l_i-1}|$, where $C_1$
  depends on the node configuration through $\|U^*\|_\infty$ and scales "roughly of the same
  order as some finite power of $\prod_{i<j}|\xi_j-\xi_i|^{-1}$" — precisely the pairwise-gap
  blow-up the manuscript wants, already proved, and shown in §5.A to match the Cramér–Rao
  bound.

**This means the conditioning half of the planned theorem is already in the literature.**
Presenting it as new would be caught immediately by a referee with a numerical-analysis
background.

## 3. Inverse spectral geometry — the genre barely exists

| Result | Identifier | Quantitative stability? |
|---|---|---|
| Grieser & Maronna, *Hearing the shape of a triangle*, Notices AMS **60** (2013), 1440–1447 | [`10.1090/noti1063`](https://doi.org/10.1090/noti1063) | **No** — exact determinacy from three invariants |
| Lu & Rowlett, *The sound of symmetry*, Amer. Math. Monthly **122** (2015), 815–835 | [`10.4169/amer.math.monthly.122.9.815`](https://doi.org/10.4169/amer.math.monthly.122.9.815) | **No** — finite-count determinacy, no perturbation bound |
| Gómez-Serrano & Orriols, *Any three eigenvalues do not determine a triangle*, J. Differential Equations | [`10.1016/j.jde.2020.11.002`](https://doi.org/10.1016/j.jde.2020.11.002) | **No** — rigorous-numerics existence proof |
| Hezari & Zelditch, *One can hear the shape of ellipses of small eccentricity*, Ann. of Math. | [`10.4007/annals.2022.196.3.4`](https://doi.org/10.4007/annals.2022.196.3.4) (see note) | **No** — exact rigidity below an implicit threshold |
| Daudé, Kamran & Nicoleau, *Stability in the inverse Steklov problem*, J. Geom. Anal. **31**, 1821–1854 | [`10.1007/s12220-019-00326-9`](https://doi.org/10.1007/s12220-019-00326-9) | **Yes — log-type**, but on a smooth warped product, not an orbifold |

Gómez-Serrano–Orriols deserves a note as the nearest *methodological* cousin: it quantifies a
near-degeneracy by a certified enclosure box (~$10^{-3}$ in vertex coordinates) inside which
an exact coincidence provably exists. That is a different thing from a conditioning bound, but
it is the closest anyone in this literature comes to putting a number on "how close".

**Pattern across the whole corpus: qualitative determinacy is the norm; quantitative
stability is rare, and where it exists the modulus is weak.** No source anywhere gives a
Lipschitz or Hölder stability estimate for an inverse spectral geometry problem. Log-type is
the good case.

## 4. Orbifolds and singular spaces — the null result

**One quantitative-stability precedent exists, and it solves a different problem.**

Lassas, Lu & Yamaguchi, *Inverse spectral problems for collapsing manifolds II: quantitative
stability of reconstruction for orbifolds*, arXiv:2404.16448 — Theorem 1.2: finite interior
spectral data $\{\lambda_j,\varphi_j|_U\}_{j=0}^{\delta^{-1}}$ determine a finite metric space
$\hat X$ with

$$d_{GH}(X\setminus S_{\sigma,\delta},\hat X)<\frac{C_1(X,\sigma)}{(\log\log|\log\delta|)^{C_2}},$$

a **triple-logarithmic** modulus, resting on a quantitative unique-continuation bound. The
predecessor is Kurylev, Lassas, Lu & Yamaguchi, arXiv:1209.5875, whose Theorem 1.5 gives only
an abstract modulus $\omega(s)$ with no explicit rate.

This is genuinely an orbifold setting. But it is a **different technical species**: continuous
metric reconstruction from interior eigenfunction data via PDE unique-continuation, not
recovery of a finite discrete multiset from finitely many symmetric functions. Same
genre-label, different problem.

**The null, with the queries that support it.** Eight arXiv API queries, all returning zero
or off-topic:

1. `all:stability AND all:orbifold AND all:spectral` → 9 hits; the only on-topic one is arXiv:2404.16448 itself
2. `all:"quantitative stability" AND all:cone` → 8 hits, all Serrin-type/isoperimetric/PDE regularity
3. `all:stability AND all:"inverse spectral" AND all:polygon` → 0
4. `all:stability AND all:"conical singularities" AND cat:math.SP` → 1, unrelated (Ricci–DeTurck flow stability)
5. `all:stability AND all:"cone points" AND all:"inverse spectral"` → 0
6. `all:stability AND all:"heat trace" AND all:orbifold` → 0
7. `all:"quantitative stability" AND all:"Laplace spectrum"` → 0
8. `all:stability AND all:isospectral AND all:cone` → 0

Two corroborating web searches surfaced only already-known items. *(Semantic Scholar returned
HTTP 429 throughout — 12 attempts, no API key configured. Recorded as a tool failure, not a
silently skipped source; the arXiv API and web search were substituted.)*

**Nearest orbifold analogue of "stability" is qualitative only.** The Proctor–Stanhope
finiteness line — Proctor & Stanhope, Diff. Geom. Appl. **28** (2010), 12–18,
DOI [`10.1016/j.difgeo.2009.03.015`](https://doi.org/10.1016/j.difgeo.2009.03.015); Proctor,
Ann. Global Anal. Geom., DOI [`10.1007/s10455-011-9270-4`](https://doi.org/10.1007/s10455-011-9270-4);
Harvey et al., J. Geom. Anal. **26** (2016), 1929–1945,
DOI [`10.1007/s12220-015-9614-6`](https://doi.org/10.1007/s12220-015-9614-6) — proves
finitely many diffeomorphism types but gives **no effective bound** on the count. No
quantitative version exists anywhere in that line.

## 5. Verdict and recommendation

**Novel in setting, not in technique.** Separate the two explicitly in the paper.

- *Technique*: nothing new. Cite Batenkov–Yomdin for the critical-point structure and the
  gap-dependent accuracy, Gautschi–Inglese and Pan for Vandermonde conditioning, Moitra via
  Aubel–Bölcskei for the minimum-separation bound, Tisseur–Van Barel and Wilkinson for the
  root-perturbation formula. Specializing sharp known bounds is stronger than reproving weak
  ones, and it inherits their constants.
- *Setting*: defensible and supported by a documented null. No stability theorem exists for
  recovering a finite discrete invariant — a cone-order multiset — of an orbifold from
  approximate spectral data.

**The technique to use.** Run the Prony/super-resolution route, which is the modern
quantitative form of exactly this problem:

1. Treat $(S_1,R,P_3)$ as three moments of the node set $\{p,q,r\}$.
2. Invoke Batenkov–Yomdin Corollary 4.3 to identify the critical locus as the collision set —
   this is the manuscript's diagonals, and the identification is a citation, not a proof.
3. Get the blow-up rate from Theorem 4.5's $\prod_{i<j}|\xi_j-\xi_i|^{-1}$ scaling, or derive
   the explicit cubic constants directly from $|p'(z_k)|=|(z_k-z_i)(z_k-z_j)|$ — both are
   defensible; the second gives sharper constants in this low-dimensional case and is worth
   doing since $n=3$ makes it tractable.
4. **Then add the part that is actually yours.** Because $p,q,r$ are *positive integers*, once
   the error bound falls below half the minimum gap the recovery is not merely stable but
   **exact**. That converts a conditioning estimate into a determinacy-from-noisy-data
   theorem: *there is an explicit $\epsilon(p,q,r)>0$ such that any spectral data within
   $\epsilon$ of the true values determines the cone orders exactly.* That is a genuinely
   different statement from anything in the numerical-analysis literature, it is the natural
   spectral-geometry reading, and it makes the diagonal blow-up meaningful rather than merely
   a nuisance — the threshold $\epsilon$ degrades precisely as the orders approach each other.

**One caution on framing.** Given that log-type is the best modulus achieved anywhere in
inverse spectral geometry (Daudé–Kamran–Nicoleau) and triple-log in the only orbifold case
(Lassas–Lu–Yamaguchi), a theorem with *explicit algebraic constants* will look surprisingly
strong. That is real, and it is because the invariant being recovered is finite and discrete
rather than a continuous metric — worth saying explicitly, so the strength reads as a
consequence of the problem's structure rather than as an overclaim.

---

## Note on one unresolved identifier

Hezari–Zelditch: the arXiv comment on arXiv:1907.03882 gives Ann. of Math. **197** (2023),
no. 1, while a citing source gives (2) **196** (2022), no. 3, 1083–1134 with DOI
`10.4007/annals.2022.196.3.4`. The manuscript uses the 2022 form. The discrepancy is flagged
rather than adjudicated — see `review/outstanding-fetches.md`.

## Bibliography corrections surfaced here

- **Gómez-Serrano & Orriols is published**: J. Differential Equations,
  DOI [`10.1016/j.jde.2020.11.002`](https://doi.org/10.1016/j.jde.2020.11.002). The
  manuscript cites "preprint, arXiv:1911.06758 (2020)".
- **Proctor & Stanhope is published**: Diff. Geom. Appl. **28** (2010), no. 1, 12–18,
  DOI [`10.1016/j.difgeo.2009.03.015`](https://doi.org/10.1016/j.difgeo.2009.03.015). The
  manuscript cites "preprint, arXiv:0811.0797 (2009)".
