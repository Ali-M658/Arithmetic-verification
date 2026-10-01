# Does the divergence rate hear the largest cone?

Inputs:

- Uçar (4.25), (4.33), transcribed in `theory/cone-coefficients/ucar-source.md`.
- Dryden–Strohmaier, arXiv:math/0504571, eq. (1) (p. 3).

Literature: `literature.md`. Exact and high-precision checks: `divergence.py`, with output in
`divergence_output.txt` (labels D1–D6 below).

## 0. Physical reading

Dryden–Strohmaier write the contribution of a cone point of order $m$ as a spectral integral,
$$E_m(t)=\sum_{l=1}^{m-1}\frac1{2m\sin\theta_l}\int_{\mathbb R}\frac{e^{-2\theta_lr}}{1+e^{-2\pi r}}
\,e^{-t(1/4+r^2)}\,dr,\qquad\theta_l=\frac{\pi l}m .$$
The rotation by $2\theta_l$ weights the spectral parameter $r$ by a density that decays like
$e^{-2\theta_l|r|}$, or like $e^{-(2\pi-2\theta_l)|r|}$ on the other side.

Expanding in $t$ turns each order into a moment, $\int r^{2\ell}(\cdots)\,dr$. Moments of order
$2\ell$ of an exponential with rate $a$ are $(2\ell)!/a^{2\ell+1}$. So the slowest decay
dominates every high moment. That is the smallest rotation angle, $2\pi/m$, from $l=1$ and
$l=m-1$.

Hence the $t^\ell$ coefficient grows like $\ell!\,(m^2/\pi^2)^\ell$. On an orbifold the largest
cone order has the smallest rotation angle, so it sets the divergence rate of the whole heat
expansion. The smooth part has the rate $1/\pi^2$, heuristically the case $m=1$ but with an
extra factor $\ell$. Every other cone is geometrically smaller.

The same number appears in Uçar's closed form, as the nearest complex pole $t=\pm2\pi i/m$ of a
generating function (Lemma 1).

## 1. Notation

$$A_\ell(m)=\frac{(2\ell)!}{\ell!\;m\sin(\pi/m)}\Big(\frac m{2\pi}\Big)^{2\ell+1},\qquad
\sigma_m=\frac{\pi/m}{\sin(\pi/m)} .$$

By Stirling, $A_\ell(m)=\ell!\,(m^2/\pi^2)^\ell\cdot\frac{1}{2\pi\sin(\pi/m)\sqrt{\pi\ell}}
(1+O(1/\ell))$.

Uçar's coefficients are $b_\ell(m)=K^\ell\beta_\ell(m)$, with
$\beta_\ell(m)=\sum_{i=0}^\ell\frac2{4^ii!}c_{\ell-i}(\pi/m)$ and $c_\ell$ given by (4.25). In
the manuscript's notation $p_\ell(m)=m\,\beta_\ell(m)$. $\beta_\ell$ does not depend on $K$, so
any statement about $\beta_\ell$ holds for $K=+1$ and $K=-1$ alike.

## 2. A generating function for (4.25)

**Lemma 1.** Let
$$G_k(t)=\frac{t/2}{\sinh(t/2)}\Big[\frac{kt}2\coth\frac{kt}2-\frac t2\coth\frac t2\Big]
=\sum_Ng_N(k)t^N .$$
Then:

- (a) $c_\ell(\pi/k)=\dfrac{(-1)^\ell(2\ell+2)!}{4k(\ell+1)!(2\ell+1)}\,g_{2\ell+2}(k)$.
- (b) $(-1)^\ell g_{2\ell+2}(k)>0$ for all $\ell\ge0$ and $k\ge2$. Hence $c_\ell(\pi/k)>0$ and
  $\beta_\ell(k)>0$ for every $\ell$.
- (c) For fixed $k\ge2$ and every $\rho<1$,
  $g_{2\ell+2}(k)=2(-1)^\ell\sigma_k(k/2\pi)^{2\ell+2}(1+O((2\rho)^{-2\ell}))$. For $k\ge3$ the
  relative error is in fact $\Theta(4^{-\ell})$. For $k=2$ it is $O(9^{-\ell})$, since
  $G_2(t)=(t/2)^2\operatorname{sech}(t/2)$ has its next poles at $\pm3\pi i$.

*Proof.*

(a) Two standard generating functions are needed:

- $\frac x2\coth\frac x2=\frac x{e^x-1}+\frac x2=\sum_jB_{2j}\frac{x^{2j}}{(2j)!}$;
- $\frac{t/2}{\sinh(t/2)}=\frac{te^{t/2}}{e^t-1}=\sum_nB_n(\tfrac12)\frac{t^n}{n!}$ (Uçar (3.69)).

Multiply the first, at $x=kt$ minus $x=t$, by the second. The Cauchy product gives
$N!\,g_N=\sum_j\binom N{2j}(k^{2j}-1)B_{2j}B_{N-2j}(\tfrac12)$, because the odd $B_n(\frac12)$
vanish. Compare with (4.25). (Checked exactly, $N\le22$, D1.)

(b) Put $t=iy$. Then
$$G_k(iy)=\frac{y/2}{\sin(y/2)}\Big[\frac{ky}2\cot\frac{ky}2-\frac y2\cot\frac y2\Big].$$

- $x\cot x=1-2\sum_{j\ge1}\zeta(2j)x^{2j}/\pi^{2j}$, so the bracket has coefficients
  $-2\zeta(2j)(k^{2j}-1)(1/2\pi)^{2j}<0$ at every $y^{2j}$, $j\ge1$, and zero constant term.
- $\frac{y/2}{\sin(y/2)}$ has positive even coefficients and constant term 1.

So every coefficient of $G_k(iy)$ in degree $\ge2$ is negative. Since $[y^{2\ell+2}]G_k(iy)=
(-1)^{\ell+1}g_{2\ell+2}$, (b) follows, and with it $c_\ell>0$. Each $\beta_\ell$ is a positive
combination of these. (Exact check: $\ell\le60$, $k\le40$, D2. Sign patterns, D1.)

(c) $G_k$ is even and meromorphic.

- Its poles nearest the origin are $t_0=\pm2\pi i/k$, from $\coth(kt/2)$. There
  $\sinh(t/2)\ne0$ and $\coth(t/2)$ is regular, since $1/k\notin\mathbb Z$. The pole is simple.
- At $t_0=2\pi i/k$, $\frac{kt}2\coth\frac{kt}2\sim\frac{t_0}{t-t_0}$, and
  $\frac{t_0/2}{\sinh(t_0/2)}=\sigma_k$. So the principal part is
  $\sigma_kt_0/(t-t_0)=-\sigma_k\sum_N(t/t_0)^N$.
- By evenness the pole at $-t_0$ contributes the same for even $N$. Together they give
  $-2\sigma_kt_0^{-N}=2(-1)^\ell\sigma_k(k/2\pi)^{2\ell+2}$ at $N=2\ell+2$.
- All other poles have modulus $\ge4\pi/k$. In fact the poles of $G_k$ are simple and lie at
  $2\pi in/k$ with $k\nmid n$: at multiples of $2\pi i$ the residues of the bracket cancel and
  the bracket vanishes. Subtracting the two principal parts leaves a function analytic in
  $|t|<4\pi/k$, whose coefficients are $O((k/4\pi\rho)^N)$ by Cauchy's estimate. Relative to
  the main term $(k/2\pi)^N$, this is $O((2\rho)^{-N})$.

$\square$

## 3. Asymptotics of the cone coefficients

**Theorem 2.** For fixed $m\ge2$, as $\ell\to\infty$,
$$\frac{b_\ell(m)}{K^\ell}=A_\ell(m)\Big(1+\frac{\pi^2}{2m^2(2\ell-1)}+O(\ell^{-2})\Big).$$
Equivalently, with $\lambda_\ell=|B_{2\ell+2}|/(2(\ell+1)!(2\ell+1))$, the leading coefficient
of $p_\ell$,
$$\frac{p_\ell(m)}{\lambda_\ell\,m^{2\ell+2}}\longrightarrow\sigma_m=\frac{\pi/m}{\sin(\pi/m)} .$$
So the full polynomial exceeds its leading term by the factor $\sigma_m$, which lies in
$(1,\pi/2]$.

*Proof.* By Lemma 1(a),(c), $c_n(\pi/m)=\Gamma_n(1+\varepsilon_n)$ with
$\Gamma_n=\frac12A_n(m)$. Here $\varepsilon_n=O((2\rho)^{-2n})$, and
$\sup_n|\varepsilon_n|<\infty$. Also $\Gamma_{n-1}/\Gamma_n=\frac{(2\pi/m)^2}{2(2n-1)}$. So
$$\frac{\beta_\ell}{A_\ell}=\sum_{i=0}^{\ell}\frac{(\pi^2/2m^2)^i}{i!}\prod_{j<i}\frac1{2\ell-2j-1}\,(1+\varepsilon_{\ell-i}).$$

- $i=0$ gives $1+\varepsilon_\ell$.
- $i=1$ gives $\frac{\pi^2}{2m^2(2\ell-1)}(1+\varepsilon_{\ell-1})$.
- For $i\ge2$ the product is at most $\frac1{(2\ell-1)(2\ell-3)}$, and the weights sum to at most
  $e^{\pi^2/2m^2}$. So the tail is $O(\ell^{-2})$.
- The $\varepsilon$ terms are $O((2\rho)^{-\ell})$ for $i\le\ell/2$. For $i>\ell/2$ they are
  bounded and the weight is super-exponentially small.

The second form uses $|B_{2n}|=2(2n)!\zeta(2n)/(2\pi)^{2n}$ with $\zeta(2n)\to1$. $\square$

**Checks.**

- 60-digit evaluation of the exact rationals, $\ell\le120$, $m\in\{2,3,4,5,8,12,30\}$ (D3).
  $\ell^2|r_\ell|$ stays bounded, where $r_\ell$ is the $O(\ell^{-2})$ term. It converges to
  $\pi^4/(32m^4)$, which is the $i=2$ term. The limits are 0.1903 ($m=2$) and 0.0376
  ($m=3$); the values at $\ell=120$ are 0.1938 and 0.0382.
- The remainder is not uniform in $m$. It is $O(\ell^{-2}m^{-4}+4^{-\ell})$, and for large $m$
  and small $\ell$ the $4^{-\ell}$ part can exceed the $1/\ell$ correction (e.g. $m=50$,
  $\ell=5$).
- $\ell(\beta_\ell/A_\ell-1)\to\pi^2/(4m^2)$.
- At $\ell=120$, $p_\ell(m)/(\lambda_\ell m^{2\ell+2})$ agrees with
  $\sigma_m(1+\pi^2/(2m^2(2\ell-1)))$ to $10^{-4}$.

**Second derivation, from the Dryden–Strohmaier integral.**

- For $a>0$, $\int_0^\infty r^ne^{-ar}(1+e^{-2\pi r})^{-1}dr=n!\sum_{j\ge0}(-1)^j(a+2\pi j)^{-n-1}$.
- The $t^\ell$ Taylor coefficient of $E_m$ is therefore an explicit finite combination of such
  moments, with $a\in\{2\theta_l,\,2\pi-2\theta_l\}$.
- These coefficients equal Uçar's $b_\ell(m)$ at $K=-1$ to relative $10^{-38}$, for $\ell\le30$
  and $m\in\{2,3,5,8,12\}$ (D4, 50 digits).
- Write the $t^\ell$ coefficient as a double sum: index $b$ for the power $r^{2b}$ taken from
  $e^{-tr^2}$, and $\ell-b$ for the factor $e^{-t/4}$. The leading term as $\ell\to\infty$
  comes from $j=0$, $b=\ell$, and the two smallest rates $a=2\pi/m$, from the classes $l=1$
  and $l=m-1$. For $m=2$ these are one class, and the factor 2 comes from its two half-lines
  $r>0$, $r<0$. It is
  $2\cdot\frac1{2m\sin(\pi/m)}\cdot\frac{(-1)^\ell}{\ell!}(2\ell)!\,(m/2\pi)^{2\ell+1}=(-1)^\ell A_\ell(m)$.
- The check covers $K=-1$. $K=+1$ follows because $\beta_\ell$ does not depend on $K$.
- This is Theorem 2 again, reached by a route that never uses (4.25). It locates the divergence
  in the slowest-decaying spectral weight, i.e. the smallest rotation angle.

## 4. The divergence rate hears the largest cone

**Theorem 3.** Let $K\in\{-1,+1\}$, $C\ge0$, and let $m_1,\dots,m_n$ ($n\ge1$) be integers
$\ge2$ with largest value $M$ of multiplicity $\mu$. Let
$$a_\ell=C\,s_{\ell+1}K^{\ell+1}+K^\ell\sum_i\beta_\ell(m_i).$$
This covers the heat coefficients ($t^\ell$, $\ell\ge0$) of every closed orientable 2-orbifold of
constant curvature $K$ with cone points $m_i$, of any genus, with $C=|\chi|/2$. It also covers
the partial sequences left after peeling. Then
$$\frac{a_\ell}{K^\ell}=\mu\,A_\ell(M)\Big(1+O(1/\ell)+O\Big(\sum_{m_i<M}(m_i/M)^{2\ell}\Big)
+O(C\,\ell\,M^{-2\ell})\Big).$$
Consequently
$$\lim_{\ell\to\infty}\frac{2\pi^2\,|a_\ell|}{(2\ell-1)\,|a_{\ell-1}|}=M^2,\qquad
\lim_{\ell\to\infty}\frac{|a_\ell|}{\ell\,|a_{\ell-1}|}=\frac{M^2}{\pi^2},\qquad
\mu=\lim_{\ell\to\infty}\frac{a_\ell}{K^\ell A_\ell(M)} .$$
If $n=0$ (and $C>0$), the first two limits are $1$ and $1/\pi^2$. There the convergence is only
$O(1/\ell)$, because $s_{\ell+1}$ carries an extra factor $\ell$.

The error terms are not uniform over orbifolds. Many copies of a slightly smaller order, or a
huge $|\chi|$, delay the asymptotic regime. Independent tests:

- $1000\times49$ together with one cone of order 50: the estimator still rounds to 49 at
  $\ell=150$.
- Genus $10^4$ with one cone of order 2: the smooth part dominates, with the opposite sign, for
  $\ell\le5$.

*Proof.* For an orbifold the coefficient has the stated form with $C=|\chi|/2$, since
$\operatorname{Area}/4\pi=|\chi|/2$ (Gauss–Bonnet, Thurston 13.3.5), and
$tZ_{S^2}(t)=\sum_ks_kt^k$ is the unit-sphere expansion.

- From $Z_{S^2}=e^{t/4}\sum_j2(j+\frac12)e^{-t(j+1/2)^2}$ and the Hurwitz expansion,
  $s_k=\sum_{i\le k}\frac{4^{i-k}}{(k-i)!}\iota_i$, with $\iota_0=1$ and
  $\iota_{j+1}=\frac{2(-1)^j}{j!}\zeta(-1-2j,\tfrac12)$.
- $|\zeta(-1-2j,\frac12)|\le|B_{2j+2}|/(2j+2)$ and $|B_{2n}|\le4(2n)!/(2\pi)^{2n}$, so
  $|\iota_{\ell+1}|\le C\,\ell\,\frac{(2\ell)!}{\ell!}(2\pi)^{-2\ell}$. The convolution with the
  coefficients $4^{-j}/j!$ of $e^{t/4}$ keeps this bound, as in the proof of Theorem 2. So
  $s_{\ell+1}=O\big(\ell\,\frac{(2\ell)!}{\ell!}(2\pi)^{-2\ell}\big)$.
- Compared with $A_\ell(M)$ this is $O(\ell\,M^{-2\ell})$, so the smooth part is negligible.
- A cone of order $m<M$ contributes
  $A_\ell(m)/A_\ell(M)=O((m/M)^{2\ell})$, also negligible.
- By Lemma 1(b) every $\beta_\ell(m_i)>0$, so the $\mu$ largest cones add without cancellation.
  Theorem 2 gives the claim.

For the ratios, $A_\ell(M)/A_{\ell-1}(M)=(2\ell-1)M^2/(2\pi^2)$, and the $(1+c/\ell+\cdots)$
corrections of numerator and denominator cancel to $O(\ell^{-2})$. Nothing in the proof uses a
relation between $C$ and the $m_i$. $\square$

**Corollary 4 (peeling).** For every $L$, the tail $(a_\ell)_{\ell\ge L}$ and $K$ determine the
cone-order multiset, $\chi$, the area and the genus. The inputs assumed known are $K$, Uçar's
(4.25)/(4.33) and $s_k>0$. This tail-only form is a small strengthening of Uçar's
Cor. 4.21(iv), whose extraction starts at $\nu=0$ and uses the area.

*Proof.*

1. Theorem 3 gives $M$ and $\mu$.
2. Subtract $\mu K^\ell\beta_\ell(M)$, which is known exactly, and repeat. The remainder is
   again of the form in Theorem 3, with one order fewer.
3. When no cone remains, the sequence is $\frac{|\chi|}2s_{\ell+1}K^{\ell+1}$, with $s_k>0$. This
   gives $\chi$ (the $n=0$ case of Theorem 3 identifies this stage).
4. The genus follows from $\chi$ and the multiset.

$\square$

**Checks (D5, D6).**

- The coefficient formula reproduces $a_1(2,8,8)=-\frac{1601}{480}$, $a_1(3,3,12)=-\frac{867}{160}$
  and $a_0(2,8,8)=\frac{67}{48}$ from `numerics/REPORT.md`, and $a_0=(S_1+R-2)/12$.
- The estimator $\pi\sqrt{2|a_\ell|/((2\ell-1)|a_{\ell-1}|)}$ at $\ell=10,40,120$ gives
  7.998, 7.99990, 7.999989 for $(2,8,8)$, and 11.9987, 11.99993, 11.999993 for $(3,3,12)$.
  It converges for $(7,8,9)$, $(11,12,12,12)$ and genus 1 with $(2,3)$. For genus 2 with no
  cones it converges to 1.
- Peeling from the two coefficients at $\ell=219,220$ alone recovers $\{3,5,5,9\}$,
  $\{2,2,3,3,3,7\}$, $\{4,4\}$ (genus 1) and $\{6,6,7\}$. The remainder equals the smooth term
  exactly.

**Consequence for the numerics.** The terms of the expansion stop decreasing near
$\ell^*\approx\pi^2/(M^2t)$, and the optimal truncation error is of order $e^{-\pi^2/(M^2t)}$.
For the pair $(2,8,8)$/$(3,3,12)$, $M=12$, and at $t=0.02$ this gives $\ell^*\approx3.4$. That is
why `numerics/REPORT.md` finds $c_1t,c_2t^2,c_3t^3=0.042,-0.030,0.026$ there, with no usable
truncation, and why the fit window must be $t\lesssim0.01$.

**Borel reading (stated, not proved beyond the radius).** By Theorem 3 the Borel transform
$\sum a_\ell\zeta^\ell/\ell!$ has radius of convergence exactly $\pi^2/M^2$. All
$a_\ell/K^\ell>0$ for large $\ell$. By Pringsheim's theorem (applied in the variable $K\zeta$,
after removing finitely many terms), the point $\zeta=K\pi^2/M^2$ on the circle of convergence is
a singularity:

- on the negative axis for hyperbolic orbifolds;
- on the positive axis for spherical ones.

The smooth heat kernel of $\mathbb H^2$ or $S^2$ has its nearest Borel singularity at distance
$\pi^2$ (Dunne, arXiv:2109.03897; Li–Li–Tang, arXiv:2606.21909). A cone of order $M$ pulls it in
by the factor $M^2$. Nothing is claimed here about the analytic continuation or about Borel
summability.

## 5. Prior work and novelty (from `literature.md`)

- **Determination is not new.** That the heat data determine the cone multiset for $K\ne0$ is
  Uçar, Corollary 4.21(iv), printed p. 139. His proof (Theorem 3.40, printed pp. 98–99)
  recovers the smallest angle by a $\nu\to\infty$ limit, applied to the extracted top-degree,
  Bernoulli-stripped sequence $W_{\nu,1}$. For cone points
  $W_{\nu,1}=\sum2(m^2-1)(m/\pi)^{2\nu+1}$, whose ratio tends to $M^2/\pi^2$: the same rate as
  Theorem 3. His $\theta_1=\pi/M$ is the same datum as the smallest rotation angle. So Uçar
  already has an asymptotic route at this rate, and Theorem 3 is a second one, on the raw
  coefficients. For $K=-1$ the spectrum already determines the number
  of cone points of each order (Dryden–Strohmaier, Theorem 1.1). For genus 0 with $n$ cones,
  Theorem A is a stronger finite statement.
- **What was not found in the sources fetched:**
  - the factorial asymptotics of the full $b_\ell(m)$ with the constant $\sigma_m$ (Theorem 2);
  - the reading of the largest order off the divergence rate of the raw coefficient sequence,
    with no triangular extraction (Theorem 3), and the tail-only peeling;
  - the statement that the Borel radius of the heat expansion is $\pi^2/M^2$. The angle itself is
    Uçar's $\theta_1$, so this is a reading, not a separate discovery.

  Garbin–Jorgenson's exact elliptic integral (Kodai 2020) contains the singularity but does not
  draw the consequence. Coverage was arXiv and Crossref only.

## 6. Recommendation: **include as a remark**, not as a proposition

Reasons for including it:

1. It explains a computed fact the manuscript's numerics depend on: the factorial growth
   $\nu!(m_{\max}^2/\pi^2)^\nu$ reported in `numerics/REPORT.md`, and hence the fit window.
   It gives the explicit constant and the optimal-truncation order $\pi^2/(M^2t)$.
2. It has a clean physical content: the divergence rate is set by the smallest rotation angle
   $2\pi/M$, and a cone point moves the Borel singularity of the smooth expansion from $\pi^2$
   to $\pi^2/M^2$. It costs one displayed formula and a two-line justification from the
   Dryden–Strohmaier integral.

Reasons for not making it a proposition:

3. Its inverse-spectral content is already in Uçar (Cor. 4.21(iv)) and Dryden–Strohmaier
   (Thm 1.1). Within the paper it is dominated by Theorem A, which needs only $n$ coefficients.
4. It requires infinitely many coefficients and gives no effective $\ell$ beyond which the
   estimator rounds correctly. That depends on the gap to the second-largest order, on the
   multiplicities of the smaller orders, and on $|\chi|$. In the tests, $1000\times49$ plus one
   50 still rounds to 49 at $\ell=150$.
5. Nothing downstream uses it.

**Suggested remark.** "By Uçar's closed form (equivalently, the moments of the
Dryden–Strohmaier elliptic weight), $b_\ell(m)=K^\ell A_\ell(m)(1+O(1/\ell))$ with
$A_\ell(m)=\frac{(2\ell)!}{\ell!\,m\sin(\pi/m)}(\frac m{2\pi})^{2\ell+1}\sim\ell!\,(m^2/\pi^2)^\ell$.
The heat expansion of a constant-curvature orbifold therefore diverges at the rate set by its
largest cone order $M$, $|a_\ell|/(\ell|a_{\ell-1}|)\to M^2/\pi^2$. This is the smallest
rotation angle $2\pi/M$ seen as the slowest-decaying elliptic spectral weight. It accounts for
the optimal truncation order $\approx\pi^2/(M^2t)$ in the numerics. That the heat data determine
the cone orders is known (Uçar, Cor. 4.21, by a large-order limit at the same rate on extracted
top-degree coefficients; Dryden–Strohmaier); here the rate is read off the raw coefficients."

If space is short, **drop** it rather than promote it.
