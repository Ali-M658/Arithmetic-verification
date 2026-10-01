# STATUS: does the divergence rate hear the largest cone?

## Verdict

**YES. Proved, given Uçar's (4.25)/(4.33) for all ℓ, the paper's existing input.
RECOMMENDATION: include as a remark, not a proposition; drop it if space is short.**

**Asymptotics (Theorem 2).** For fixed $m\ge2$,
$$b_\ell(m)=K^\ell A_\ell(m)\Big(1+\frac{\pi^2}{2m^2(2\ell-1)}+O(\ell^{-2})\Big),\qquad
A_\ell(m)=\frac{(2\ell)!}{\ell!\,m\sin(\pi/m)}\Big(\frac m{2\pi}\Big)^{2\ell+1}\sim\ell!\,(m^2/\pi^2)^\ell .$$
It is obtained from the full $p_\ell$, through a generating function for (4.25) whose nearest
poles are at $t=\pm2\pi i/m$. Equivalently, $p_\ell(m)$ exceeds its leading term by the factor
$(\pi/m)/\sin(\pi/m)$. The same result follows independently from the moments of the
Dryden–Strohmaier elliptic weight, where the slowest decay rate $2\pi/m$ (the smallest rotation
angle) dominates.

**All-order positivity (Lemma 1).** $b_\ell(m)/K^\ell>0$ for every $\ell\ge0$ and $m\ge2$.

**Divergence rate (Theorem 3).** For a closed constant-curvature ($K=\pm1$) orbifold of any
genus with cone points,
$$\frac{|a_\ell|}{\ell\,|a_{\ell-1}|}\to\frac{M^2}{\pi^2}\qquad(M=\text{largest cone order}),$$
and $a_\ell/(K^\ell A_\ell(M))\to\mu$, the multiplicity of $M$. Peeling recovers the whole
multiset, $\chi$ and the genus from any tail of the coefficient sequence. Without cone points
the rate is $1/\pi^2$, and in flat geometry the sequence is identically zero.

## Why a remark

- The inverse content is known. Uçar, Cor. 4.21(iv) (printed p. 139) proves that the heat data
  determine the cone multiset for $\kappa\ne0$, by a $\nu\to\infty$ limit on extracted
  top-degree coefficients (Thm 3.40, pp. 98–99). Dryden–Strohmaier Thm 1.1 covers $K=-1$.
  Theorem A is stronger for genus 0.
- Uçar's own route is already a large-order limit at the same rate $M^2/\pi^2$, applied to
  extracted top-degree coefficients, and his $\theta_1=\pi/M$ is the same angle.
- **New in the sources fetched:**
  - the explicit factorial asymptotics of the full $b_\ell(m)$, with constant
    $(\pi/m)/\sin(\pi/m)$ and the $1/\ell$ term;
  - the rate read off the raw coefficients, with no extraction;
  - tail-only peeling;
  - the Borel radius $\pi^2/M^2$ of the heat expansion (versus $\pi^2$ for the smooth part:
    Dunne 2021, Li–Li–Tang 2026).
- It explains the numerics. The optimal truncation order is $\approx\pi^2/(M^2t)$, which is
  about 3.4 at $t=0.02$ for $M=12$. That matches `numerics/REPORT.md` and its fit window.
- It needs infinitely many coefficients and is not effective: the onset depends on the gap to the second-largest order, on multiplicities and on $|\chi|$. Nothing downstream uses it.

The suggested remark text is in `proof.md` §6.

## Verification (`divergence.py`, output `divergence_output.txt`, about 10 min)

| check | what it verifies | range |
|---|---|---|
| D1 | generating-function identity | exact, $N\le22$ |
| D1 | sign patterns | through $x^{28}$ |
| D2 | positivity | exact, $\ell\le60$, $k\le40$ |
| D3 | Theorem 2 at 60 digits; $\ell^2\times$remainder bounded and tending to $\pi^4/(32m^4)$ | $\ell\le120$, seven values of $m$ |
| D4 | Dryden–Strohmaier Taylor coefficients equal Uçar's to relative $10^{-38}$ | $n\le30$, 50 digits |
| D5 | $a_1(2,8,8)=-\frac{1601}{480}$, $a_1(3,3,12)=-\frac{867}{160}$, $a_0(2,8,8)=\frac{67}{48}$ as in `numerics/REPORT.md` | exact |
| D6 | estimator convergence to $M$ for six orbifolds (genus 0, 1, 2) | — |
| D6 | exact peeling recovery of four multisets from two coefficients at $\ell=220$ | — |

## Literature

See `literature.md`, a sweep of arXiv (API and full text) and Crossref. Watson (NZJM 2005) is
unreachable and is logged in `review/outstanding-fetches.md` §1.9.
