# The moduli experiment: same heat expansion, different shape

## Outcome

**(i)–(iii) all hold within error.** Eight pairwise non-isometric hyperbolic orbifolds of
signature $(0;3,3,3,3)$ were computed: doubled equiangular quadrilaterals with modulus
$\tau\in\{0,0.4,\dots,2.8\}$ and systoles falling from 2.634 to 0.694. Each has about 5450
eigenvalues certified complete up to $\lambda\approx1.6\times10^4$.

- **(i) Same heat expansion.** Every member's heat trace equals the signature-only part
  (identity + four elliptic terms) to $\le1.2\times10^{-12}$ wherever closed geodesics are
  negligible. The error budget is $2.2\times10^{-11}$. Across all eight members the traces
  coincide to $1.3\times10^{-13}$ for $t\le0.0037$.
- **(ii) Different shape, different spectrum.** The eigenvalues move with the modulus:
  $\lambda_1$ goes from 4.1224 ($\tau=0$) to 0.4348 ($\tau=2.8$), and the first 200
  eigenvalues move by up to 89% relative. The worst eigenvalue error is $1.3\times10^{-10}$
  relative (conservative $8.3\times10^{-9}$).
- **(iii) The difference is exactly the geodesics.**
  - For all 28 pairs, $Z_i-Z_j$ equals the predicted $H_i-H_j$ to $\le1.1\times10^{-13}$ for
    $t\le0.33$, with nothing fitted. That is 400 times below the budget. The traces
    themselves differ by up to 0.79 there.
  - $H_\tau$ is computed from the enumerated closed geodesics of each member.
  - The difference leaves the noise at the predicted time, to the grid resolution, for every
    pair. That time is set by the shorter systole: $t^*=0.0050$ for $\ell=0.694$, rising to
    $0.0495$ for $\ell=2.203$.
  - Once the difference is $10^3$ above the noise, it equals the leading term
    $-\frac{w(\ell)}{2\sinh(\ell/2)}\frac{e^{-t/4}e^{-\ell^2/4t}}{\sqrt{4\pi t}}$ of the shorter
    systole to within 0.9997–1.0000. This is Theorem 3.5 (`theory/locality/proof.md`) in the
    data.
- **Bounds.** Theorem 3.4 (b) and (c) are asserted to hold for every pair and every $t$ in
  their windows.

**Two defects found and fixed along the way.**

- *Silently missing eigenvalues.* The S3 single-cover slicing let ARPACK drop an eigenvalue
  inside a "certified" window. It happened in at least 2 of the 64 first-pass production runs.
  Comparing mesh levels caught it (§4a). The suite was rerun with every eigenvalue covered by
  two windows. Exact count agreement across levels is now asserted.
- *Noisy S3 identity term.* The S3 identity-term quadrature is noisy at $10^{-7}$ on some
  grids. Section 2.1 replaces it.

**Compute.** Vultr, 16 vCPU / 31 GB. Sessions ran from 10:49 to about 13:05 UTC: **2.3 server
hours wall-clock**, of which about 2.0 h were solver load. CPU time was about 22 core-hours.
The instance was up from 10:35 UTC. Details are in §8.

---

## 1. Construction

### 1.1 The family

Signature $(0;3,3,3,3)$: a sphere with four cone points of order 3. It is hyperbolic
because $\sum(1-1/m)=8/3>2$. The area is $-2\pi\chi=4\pi/3$, and the Teichmüller space is
2-dimensional (Thurston 13.3.7, `theory/locality/proof.md` Prop. 2.1).

Every member is the double of a geodesic quadrilateral $Q$ with all four angles $\pi/3$.
The quadrilateral is chosen symmetric under $z\mapsto\bar z$ and $z\mapsto-\bar z$ in the
Poincaré disk. The two mirror axes cut $Q$ into four congruent Lambert quadrilaterals
$L=OPVY$:

- right angles at $O=0$, at $P=\tanh(a/2)$ on the real axis, and at $Y=i\tanh(b/2)$ on the
  imaginary axis;
- angle $\pi/3$ at the vertex $V$.

Here $a$ and $b$ are the distances from the centre to the east and north sides of $Q$.

**Explicit construction (no root finding).**

- The east side is the geodesic orthogonal to the real axis at $P$: the circle with centre
  $\coth a$ and radius $1/\sinh a$.
- The north side is the circle with centre $i\coth b$ and radius $1/\sinh b$.
- $V$ is their intersection in the first quadrant, given by a quadratic.

A Lambert quadrilateral with acute angle $\varphi$ satisfies $\sinh a\sinh b=\cos\varphi$. This
leaves one free parameter, the **modulus**
$$\tau=\ln\frac{\sinh a}{\sinh b},\qquad \sinh a=\sqrt{c}\,e^{\tau/2},\quad\sinh b=\sqrt c\,e^{-\tau/2},\quad c=\cos\tfrac\pi3=\tfrac12 .$$
$\tau=0$ is the square. $\tau$ and $-\tau$ give congruent quadrilaterals (rotation by
$\pi/2$). The members are $\tau\in\{0,0.4,0.8,1.2,1.6,2.0,2.4,2.8\}$.

The doubled quadrilaterals form a real one-parameter family inside the two-dimensional
moduli space: the orbifolds that carry an orientation-reversing isometry fixing all four
cone points.

**Verification (quad.py, asserted to $10^{-12}$; achieved $\le3\times10^{-40}$ at 40-digit
precision).** The Lambert relation is used only to construct $Q$, never to check it.

- The angle at $V$ is recomputed from the tangent vectors of the two constructed circles.
  The right angles at $O$, $P$, $Y$ are recomputed the same way.
- Both circles are checked to be orthogonal to $|z|=1$ and to pass through their side's
  endpoints.
- The area of $L$ comes from polar quadrature of $4/(1-|z|^2)^2$ and is compared with
  Gauss–Bonnet, $\pi/2-\pi/3=\pi/6$.
- The lengths of the mirror segments $OP$, $OY$ are compared with $a$ and $b$ by
  integrating $2|dz|/(1-|z|^2)$.

All eight members pass. The geometries, including vertices, side circles, side lengths,
diameters and the shortest closed geodesics, are exported in `data/geometries.json`.

### 1.2 The doubling principle for polygons

`numerics/REPORT.md` §1 proves, for a triangle $T$ with angles $\pi/p,\pi/q,\pi/r$, that the
pillow $\mathcal O=T\cup_{\partial}T'$ has spectrum $\operatorname{spec}_N(T)\sqcup\operatorname{spec}_D(T)$. The proof
never uses that $T$ has three sides. It uses only the following:

1. $\partial T$ is a finite union of geodesic arcs meeting at the vertices.
2. The sheet-exchange $\sigma$ is an isometry of the double fixing $\partial T$, acting as
   the reflection in each arc away from the vertices.
3. Points have zero $H^1$-capacity in dimension 2, so $H^1(\mathcal O)=H^1(\mathcal O^\circ)$.
4. The even/odd splitting $H^1=H^1_+\oplus H^1_-$ is orthogonal for $L^2$ and for the
   Dirichlet form.
5. Traces from the two sides of each arc agree, and the gluing lemma across a Lipschitz
   interface holds.

For a compact convex geodesic polygon $Q$ with angles $\pi/m_i$, all five hold verbatim. So
does the identification of the double as an orbifold with cone points of order $m_i$ at the
vertices (cone angle $2\cdot\pi/m_i$). Hence:

**Doubling principle for polygons.** For a compact geodesic polygon $Q$ with angles
$\pi/m_i$, the double $\mathcal O_Q$ is a closed orbifold of signature $(0;m_1,\dots,m_k)$ with
$\operatorname{spec}(\mathcal O_Q)=\operatorname{spec}_N(Q)\sqcup\operatorname{spec}_D(Q)$, with multiplicity, and
$Z_{\mathcal O_Q}=Z_N+Z_D$.

**Symmetry reduction.** The two mirror reflections $r_x(z)=\bar z$ and $r_y(z)=-\bar z$ are
isometries of $Q$ preserving $\partial Q$. Each preserves the Neumann and Dirichlet form
domains. Repeating the even/odd argument for each reflection splits each of
$\operatorname{spec}_N(Q)$ and $\operatorname{spec}_D(Q)$ into four mixed problems on $L$:

- the condition on the sides $e=PV$ and $n=VY$ (the sides of $Q$) is that of $Q$;
- the condition on the mirror segments $x=OP$ and $y=YO$ is Neumann (even) or Dirichlet
  (odd).

This gives eight sectors, labelled $\langle\text{outer}\rangle\langle x\rangle\langle y\rangle\in\{N,D\}^3$:
$$\operatorname{spec}(\mathcal O(\tau))=\bigsqcup_{s\in\{N,D\}^3}\operatorname{spec}(L;s).$$

**Regularity at every corner.** The singular exponents at a corner of angle $\omega$ are
$k\pi/\omega$ when both sides carry the same condition, and $(k+\tfrac12)\pi/\omega$ when the
conditions are mixed.

- At the right angles $O$, $P$, $Y$ these are $2k$ and $2k+1$: integers.
- At $V$ ($\omega=\pi/3$, both sides outer) they are $3k$.

So no sector has a corner singularity. As for the S3 triangles, the eigenfunctions extend
by reflection to smooth functions on the orbifold chart, and high-order FEM converges
exponentially. Section 4(a) confirms this.

The reduction is tested directly in §4(b): the union of the four Neumann (Dirichlet) sector
spectra reproduces the spectrum of the whole quadrilateral solved without symmetry, with
multiplicity.

## 2. Predictions

### 2.1 What is the same for every member

Theorem 3.1 of `theory/locality/proof.md` (the Dryden–Strohmaier trace formula,
arXiv:math/0504571 eq. (1), extended to the heat test function) gives
$$Z_{\mathcal O(\tau)}(t)=I(t)+4E_3(t)+H_\tau(t).$$

- $I(t)=\frac{4\pi/3}{4\pi}\int r\tanh(\pi r)e^{-t(1/4+r^2)}dr$ is the identity term.
- $E_3$ is the elliptic term of one cone point of order 3.

$I+4E_3$ depends only on the signature. It is the same function of $t$ for every member,
and its asymptotic series is the full heat expansion (Theorem 1). `trace_formula.py`
evaluates it at 30 digits. It splits $\tanh(\pi r)=1-2/(e^{2\pi r}+1)$, so that the
identity term is a closed form plus an exponentially convergent integral. Plain quadrature
of $r\tanh(\pi r)e^{-tr^2}$ over $[0,\infty)$ was found to be unreliable at the $10^{-7}$
level on some $t$-grids.

Check: $I+4E_3$ minus the exact heat series through $t^3$ (`numerics/theory.py`, Uçar
(4.33), (4.35)) is $3.6\times10^{-12}$, $5.7\times10^{-11}$ and $9.1\times10^{-10}$ at
$t=10^{-3}$, $2\times10^{-3}$ and $4\times10^{-3}$. That is the $t^4$ scaling of the first
omitted term. `theory/locality/check_locality.py` also proves the series identity exactly,
for every order through $t^{14}$ (identity term) and $t^5$ (elliptic terms).

### 2.2 What moves: closed geodesics

$$H_\tau(t)=\sum_{[\gamma]}\frac{\ell(\gamma_0)}{2\sinh(\ell(\gamma)/2)}\frac{e^{-t/4}e^{-\ell(\gamma)^2/4t}}{\sqrt{4\pi t}}$$

**Enumeration without conjugacy classes (geodesics.py).** $\Gamma$ is the index-2 subgroup
of the reflection group $W$ of $Q$. For hyperbolic $\gamma$ with centraliser
$\langle\gamma_0\rangle$, the axes of the conjugates of $\gamma$ cut a fundamental domain
$F$ in segments of total length $\ell(\gamma_0)$. With $F=Q\cup sQ$, and the bijection
$\gamma\mapsto s\gamma s$,
$$H_\tau(t)=2\sum_{\gamma\in\Gamma\ \rm hyperbolic}\operatorname{len}(\operatorname{axis}\gamma\cap Q)\,\frac{e^{-t/4}e^{-\ell(\gamma)^2/4t}}{2\sinh(\ell(\gamma)/2)\sqrt{4\pi t}} .$$

- *Where the axes are.* The axes are clipped to $Q$ in the Klein model, where $Q$ is a
  Euclidean convex polygon. A segment lying on a side is shared by two tiles and gets
  weight $\tfrac12$.
- *Which elements to visit.* Elements are enumerated breadth-first over the tiling, in the
  hyperboloid model. A tile is kept if $d(o,wo)\le\ell_{\max}+3r_Q$, where $r_Q$ is the
  largest distance from the centre to a point of $Q$. This keeps every $\gamma$ whose axis
  meets $Q$ with $\ell(\gamma)\le\ell_{\max}$.
- *Tile identity.* A tile is identified by the image of an interior base point. The
  spatial hash has tolerance $\ll$ the minimal separation $2\,d(x_0,\partial Q)$.
- *Range.* $\ell_{\max}=6.5$.

The output is the weighted length spectrum $\{(\ell,w(\ell))\}$. For a primitive length,
$w/\ell$ is the number of oriented closed geodesics. The shortest three lengths of every
member are asserted to have integer $w/\ell$.

**The geodesics behave as the geometry says.**

- The shortest closed geodesic of every member is $4b(\tau)$, asserted to $10^{-9}$. It is
  the common perpendicular of the north and south sides, run up one sheet and down the
  other.
- It has $w/\ell=2$: two orientations. For the square it is $4$, since the east–west
  geodesic has the same length.
- Its iterates appear with $w/\ell=2/k$.
- $4b$ falls from 2.634 ($\tau=0$) to 0.694 ($\tau=2.8$), strictly monotonically. So all
  members are pairwise non-isometric, and every pair has different systoles. This is the
  hypothesis of the sharpness theorem (Theorem 3.5) with $L_*=\ell$.

**Validation on S3 (check_geodesics_s3.py).** The same code was run for the triangle groups
of O(2,8,8) and O(3,3,12). The committed S3 FEM traces were compared with
$I+E+H$ over $t\in[0.0015,0.5]$ (`numerics/data/heat_trace_difference.csv`), with nothing
fitted.

- The CSV prints $t$ to 8 digits, which alone moves $Z\approx1/(8t)$ by $\sim10^{-6}$. The
  exact grid `heat_trace.T_GRID` is used and checked row by row against the CSV.
- Agreement: $\max|Z-I-E-H|=1.3\times10^{-9}$ for O(2,8,8) and $1.0\times10^{-9}$ for
  O(3,3,12). The geodesic term reaches $6.9\times10^{-2}$ and $1.24\times10^{-1}$.
- The shortest lengths, 2.256768 and 1.862604, come out with $w/\ell=2$. S3 had *fitted*
  multiplicities 1.997 and 1.9998.

This fixes the trace-formula normalisation and the enumeration independently of the new
spectra.

## 3. Solver, levels, runs

- *Discretisation.* Identical to S3 (`numerics/REPORT.md` §3): $-\Delta_Eu=\lambda wu$ with
  $w=4/(1-|z|^2)^2$, NGSolve $H^1$ elements of order $p$, and uniform hyperbolic mesh size
  $h$.
- *Geometry.* Both arcs of $L$ are exact rational quadratic splines, curved to order $p$.
  The FEM area of every mesh is exact to $\le4\times10^{-15}$ (asserted $<10^{-12}$).
- *Eigensolver.* Doubly covered spectral slicing (`solve_moduli.eigenvalues_robust`), built
  on the S3 single-slice routine `numerics/solve.py:slice_eigs`, imported unmodified.
  - Every eigenvalue lies in the inner 80% of two independent shift-invert windows.
  - Clusters at relative tolerance $10^{-9}$ take the largest multiplicity reported by any
    covering window.
  - Disagreements between covering windows are counted. There were none in the final suite.

  The first pass used the S3 routine `numerics/solve.py:eigenvalues` unchanged. It lost
  eigenvalues, see §4(a).
- *Driver.* `solve_moduli.py`.
- *Levels.* As S3: $(0.1,10)$, $(0.07,8)$, $(0.07,12)$, $(0.07,10)$, and production
  $(0.05,10)$, for 8 members × 8 sectors × 5 levels = 320 runs.
- *Size.* NEV = 700 per sector, 723–730 eigenvalues per sector, all levels compared,
  reaching $\lambda\ge1.63\times10^4$. About 5450 eigenvalues per orbifold below the common
  cut.
- *Full-quadrilateral check.* $\tau=0.8$, N and D, at $(0.07,10)$ on the whole of $Q$
  (four arcs, ~46k dof).

## 4. Validation (analysis.py; every item is an assert)

**(0) Geometry and geodesics.** All 8 members pass `quad.verify` and the length-spectrum
integrality checks. The systole equals $4b$ to $10^{-9}$ and decreases strictly in $\tau$.

**Cross-machine reproducibility (`s3_repro.py`, before any heavy job).** The S3 problem
O(3,3,12) Neumann at the S3 production level was rerun on the server with the unmodified S3
solver and compared with `numerics/data/eigenvalues_3-3-12_N.csv`. Data:
`data/s3_repro.json`.

- All 1434 eigenvalues agree.
- Max relative difference $1.0\times10^{-12}$; first 500: $2.1\times10^{-14}$.
- Max $|\Delta|$ / S3 error estimate: 0.15.

**(a) Convergence per sector** (64 problems × 5 levels).

| quantity | value | asserted |
|---|---|---|
| worst relative error, first 300 per sector (production vs (0.07,12)) | $1.3\times10^{-10}$ | $<10^{-8}$ |
| worst relative error, conservative (vs (0.07,10)) | $8.3\times10^{-9}$ | $<5\times10^{-8}$ |
| $h$-rate at $p=10$ | 15.8–24.3 | $>12$ |
| $p$-ratio, 8→10 | 309–543 | $>30$ |
| fraction of modes converging monotonically from above | $>0.99$ | $>0.99$ |

These rates are stronger than S3's 13–19 and 145–350. This is consistent with the
regular-corner analysis (§1.2): there is no corner singularity in any sector.

*Completeness.* The eigenvalue counts below $0.8\,\lambda_{\max}$ must agree exactly across
the three accurate levels, and below $0.5\,\lambda_{\max}$ across all five.

- This assert is what exposed the defect of the first pass. There the S3 single-cover
  slicing returned at least 2 production runs ($\tau=0$ and $\tau=0.8$, both sector DNN) that were one
  eigenvalue short. For $\tau=0$ the missing value was $\lambda=4815.4774$, at a slice
  boundary, present at both other accurate levels.
- The final suite uses double coverage and passes. 0 window disagreements were recorded.

**(b) Symmetry reduction.** For $Q(0.8)$ solved whole, with no symmetry, at $(0.07,10)$ and
~46k dof, the union of the four Neumann sectors reproduces the Neumann spectrum.

| | eigenvalues compared | max relative difference (all) | first 300 |
|---|---|---|---|
| Neumann | 1206, below 6943 | $6.9\times10^{-11}$ | $1\times10^{-14}$ |
| Dirichlet | 1203, below 7524 | $1.6\times10^{-10}$ | $6\times10^{-15}$ |

The counts are the same, so this confirms the doubling-plus-mirror decomposition with
multiplicity.

**(c) Weyl law and mirror term.**

- *Weyl law.* $N_{\mathcal O}(\lambda)-\big(\tfrac{4\pi/3}{4\pi}\lambda+\tfrac79\big)$ has mean
  between $-0.017$ and $+0.008$ for every member (about 5450 eigenvalues each). The window
  means are $\le0.41$ and the rms is about 1.4. $a_0=\chi/6+\sum(m^2-1)/(12m)=-\tfrac19+\tfrac89=\tfrac79$
  is `eq:a0conv`. There is no drift and no missing or duplicated eigenvalue.
- *Mirror term.* $Z_N(Q)-Z_D(Q)$ equals $\operatorname{perimeter}(Q)\,e^{-t/4}/(4\sqrt{\pi t})$
  to $\le3\times10^{-13}$, within the budget. This is checked for $t$ up to where the
  orientation-reversing bounce orbits, of length at least the systole, are below $e^{-32}$.

## 5. Results

### (i) Same heat expansion

$Z_\tau-(I+4E_3)$ against the error budget (eigenvalue errors plus the S3-style tail bound
with sector Weyl terms), at points where $H_\tau$ plus its truncation bound is below
$10^{-13}$:

| $\tau$ | 0 | 0.4 | 0.8 | 1.2 | 1.6 | 2.0 | 2.4 | 2.8 |
|---|---|---|---|---|---|---|---|---|
| geodesic-free window, $t\le$ | 0.055 | 0.039 | 0.026 | 0.018 | 0.012 | 0.0082 | 0.0055 | 0.0037 |
| $\max\lvert Z-I-4E_3\rvert$ | 1.2e-12 | 1.2e-12 | 1.1e-12 | 1.2e-12 | 1.1e-12 | 1.1e-12 | 1.1e-12 | 1.2e-12 |

The budget is $\le2.2\times10^{-11}$ throughout, so the agreement is 20× inside it. On the
common window $t\in[0.0025,0.0037]$ the eight traces are the same function to
$1.3\times10^{-13}$, the rounding level of a sum of ~5450 terms.

The heat expansion is the asymptotic series of $I+4E_3$. `theory/locality/check_locality.py`
proves exactly that its coefficients are Uçar's. So these traces share all their heat
coefficients, and the data show them sharing the function itself until geodesics switch on.

**Full trace formula.** $Z_\tau=I+4E_3+H_\tau$ holds to $\le1.2\times10^{-12}$ for every member
up to $t=0.33$ (`data/heat_traces.csv`). There $H_\tau$ reaches $8.6\times10^{-3}$ ($\tau=0$)
to $0.79$ ($\tau=2.8$). This is the orbifold Selberg trace formula with the heat test
function (proof.md Theorem 3.1), confirmed with no fitted parameter.

### (ii) Eigenvalues move with the modulus

| $\tau$ | 0 | 0.4 | 0.8 | 1.2 | 1.6 | 2.0 | 2.4 | 2.8 |
|---|---|---|---|---|---|---|---|---|
| $\lambda_1$ | 4.122413 | 2.984773 | 2.142946 | 1.537144 | 1.107024 | 0.803055 | 0.587935 | 0.434832 |

$\lambda_1$ falls as the quadrilateral elongates. For every member it lies in sector NND:
Neumann on the sides of $Q$, even under $z\mapsto\bar z$, odd under $z\mapsto-\bar z$. So it
changes sign between the east and west halves, along the long direction of width $2a$. (At
$\tau=0$ it is degenerate with its NDN rotate.) Every pair of members differs in its first 200
eigenvalues by at least $10^4\times$ the worst conservative error (asserted); $\tau=0$
against $2.8$ differs by up to 89%.

Exports: `data/eigenvalue_flow_orbifold.csv` (the first 400 eigenvalues of each member, with
sector label and both error measures) and `data/eigenvalue_flow_sectors.csv` (the first 120
per sector).

### (iii) Differences are the closed geodesics

For each of the 28 pairs $(\tau_i<\tau_j)$, $D_{ij}=Z_{\tau_i}-Z_{\tau_j}$ is compared with
$H_{\tau_i}-H_{\tau_j}$, the budget $B_{ij}$ being the sum of the two budgets.

- **Agreement.** $|D_{ij}-(H_i-H_j)|\le1.1\times10^{-13}$ for all pairs and all
  $t\le0.33$. $B_{ij}\le4.3\times10^{-11}$.
- **Emergence.** Let $t^*_{\rm pred}$ be the first $t$ at which $|H_i-H_j|>10(B_{ij}+10^{-12})$,
  and $t^*_{\rm meas}$ the first $t$ from which $|D_{ij}|$ stays above the same level. They
  coincide on the grid (spacing 2.4% in $t$) for **all 28 pairs**:

| shorter systole $\ell$ (member) | 2.203 (0.4) | 1.831 (0.8) | 1.516 (1.2) | 1.250 (1.6) | 1.029 (2.0) | 0.846 (2.4) | 0.694 (2.8) |
|---|---|---|---|---|---|---|---|
| $t^*$ predicted = measured | 0.0495 | 0.0337 | 0.0236 | 0.0158 | 0.0109 | 0.0073 | 0.0050 |
| $\ell^2/(4t^*)$ | 24.5 | 24.9 | 24.3 | 24.7 | 24.3 | 24.5 | 24.0 |

  The emergence time depends only on the shorter systole, whatever the partner, as Theorem
  3.5 says. The exponent at emergence is the same number, about 24.5. That is
  $\ln(\text{prefactor}/\text{noise})$: the Gaussian $e^{-\ell^2/4t}$ is the whole story.
- **Leading term.** At the first $t$ where the signal exceeds $10^3\times$ the noise,
  $D_{ij}$ divided by the leading term of the shorter systole is 0.9997–1.0000. The leading
  term is $-\frac{w}{2\sinh(\ell/2)}\frac{e^{-t/4}e^{-\ell^2/4t}}{\sqrt{4\pi t}}$ with $w=2\ell$
  (two orientations).
- **Theorem 3.4.**
  - The explicit bound (b) holds on its window $t\le\ell^2/(2(1+\ell))$. It is valid but
    very loose: it carries $e^{3\delta}$, with $\delta\le2\operatorname{diam}Q$ up to 7.8.
  - The controlled bound (c), with reference time $t_1=0.4$, holds for all $t\le0.4$ and is
    the useful one.

## 6. Exports (`data/`)

| file | content |
|---|---|
| `geometries.json` | per member: $a$, $b$, $V$, vertices and side circles of $Q$, side lengths, perimeter, areas, angle/area checks, $r_Q$, $\operatorname{diam}Q$, systole, shortest lengths with weights |
| `length_spectra.csv` | weighted length spectrum $(\ell,w,w/\ell)$ up to $\ell=6.5$, per member |
| `eigenvalue_flow_orbifold.csv` | first 400 eigenvalues of each orbifold vs $\tau$, sector, error estimate, conservative error |
| `eigenvalue_flow_sectors.csv` | first 120 eigenvalues per sector vs $\tau$ |
| `heat_traces.csv` | per member, 200 $t\in[0.0025,0.4]$: $Z$, $I+4E_3$, predicted $H$, residual, error components, length-truncation bound |
| `trace_differences.csv` | 28 pairs × 200 $t$: measured $D$, predicted $H_i-H_j$, leading term, budget, truncation bound, Theorem 3.4(c) bound |
| `convergence.csv` | every eigenvalue of every sector: production value, both error measures, coarse-level differences |
| `weyl.csv` | windowed Weyl residuals of each orbifold |
| `heat_kernel_diagonal_moduli.npz` | $K(t,x,x)$ for $\tau=0$ and $\tau=2.8$ at $t=0.005,0.01,0.02$ (see below) |
| `s3_geodesic_check.csv` | S3 traces vs $I+E+H$ (§2.2) |
| `s3_repro.json` | cross-machine S3 rerun (§4) |
| `summary.json` | every headline number above |

**heat_kernel_diagonal_moduli.npz.**

- *Level.* $(0.07,10)$, all 8 sectors, about 725 eigenfunctions each, from the doubly
  covered slicer.
- *Points.* Vertices of a hyperbolic-size-0.03 triangulation of the Lambert quarter, with
  points and triangles included. Coordinates are in the Poincaré disk; the normalisation is
  hyperbolic, $\int_{\mathcal O}K\,dA=Z$.
- *Contents.* `K_orbifold` $=\tfrac18\sum_s K_s$, plus the eight sector kernels. Values
  elsewhere on $\mathcal O$ follow from the mirror symmetries.
- *Asserted checks.*
  - Away from the cone point (distance $>6\sqrt t$), $K=(1-t/3)/(4\pi t)$ to
    $1.7\times10^{-6}$ (567 and 537 points). The sides of $Q$ and the mirror axes are
    interior geodesics of the double and impose nothing.
  - At the order-3 cone point, $K/(3/(4\pi t))=0.9983$ at $t=0.005$, for both members.

Not committed: raw runs (`runs/`, 3.8 MB, regenerated by `run_server.sh suite` and
`fullquad`).

## 7. Limitations

- **Error estimates are not enclosures.** As in S3, the per-eigenvalue estimate is the
  agreement of two independent discretisations. The conservative coarse-level difference is
  carried alongside, and the verdicts hold under it (the asserts in §4a use both).
- **Completeness rests on double coverage plus cross-level counts, not on an inertia
  count.** Sylvester inertia is unavailable with SciPy's LU. The first pass shows that
  single-window certification is not enough.
- **Implication for S3.** `numerics/solve.py:eigenvalues` (S3) has the same exposure. For the
  committed S3 data it is excluded a posteriori by two checks: the 7e-13 trace-formula
  agreement in `numerics/REPORT.md` §4d (a missing eigenvalue below ~$10^4$ would show at
  $\ge10^{-7}$), and the exact match of all 1434 eigenvalues in the server rerun.
- **The tail bound is conditional**, as in S3: it assumes the counting function beyond the
  computed range stays below the two-term law plus twice the largest observed excess.
- **The geodesic sum is truncated at $\ell\le6.5$.** Its truncation bound extrapolates the
  observed growth of $\sum w$. Comparisons are restricted to where that bound is below
  $10^{-12}$ ($t\le0.33$).
- **Enumeration is in floating point.** Each enumeration is a breadth-first search over the
  tiling with a provably sufficient radius. Tile identity uses a tolerance argued from the
  minimal separation, not proved in interval arithmetic. Integrality of $w/\ell$ and the
  match with the FEM data are the checks.
- **The family is a real slice.** It is a one-parameter slice (orbifolds with an
  anti-conformal symmetry) of the two-dimensional moduli space, not a generic curve in it.
  Theorem 3.5 does not need genericity: any two members with different systoles behave as
  shown.
- **One signature.** Other signatures were not computed.

## 8. Server usage

Vultr instance, 16 vCPU, 31 GB, Ubuntu 24.04.5, key login only. The instance was up from
10:35 UTC; the first login was at 10:49 UTC and the last action at about 13:05 UTC.

| stage | wall time | notes |
|---|---|---|
| Miniforge 26.7.2-0 + env `moduli` from `env/environment.yml` | ~12 min | first attempt hung on an untimed download; retimed |
| S3 reproducibility (`s3_repro.py`) | 4 min | 16 threads |
| suite, pass 1 (S3 slicing) | 22 min | + ~4 min lost to BLAS oversubscription before the restart; superseded |
| full-Q, pass 1 | 10 min | superseded |
| suite, pass 2 (double cover), 14 workers | 66 min | final |
| full-Q, pass 2 | 33 min | concurrent with suite |
| kernel export (twice) | 2 × ~4 min | first attempt stopped at a faulty test (§6) |

**Total: about 2.3 h of server wall-clock time, about 22 core-hours of CPU.** The estimate
before launching was under 3 h, far below the 12 h cap.

The pinned environment as built is recorded in `env/conda-explicit.server.txt` and
`env/pip-freeze.server.txt`. The pip pins are those of `numerics/requirements.txt`, plus
the `ngsolve_openblas` wheel that ngsolve pulls in. Server logs are in `logs/`.

All results were copied to the Mac with rsync and committed from the Mac. Nothing was
committed or pushed from the server. **The instance is no longer needed and can be
destroyed.**

## 9. Reproduce

```
bash numerics/moduli/env/setup_server.sh                 # pinned env (or the Mac venv of numerics/)
python numerics/moduli/quad.py                           # family construction checks
python numerics/moduli/s3_repro.py                       # cross-machine S3 rerun (~4 min, 16 threads)
python numerics/moduli/check_geodesics_s3.py             # geodesic machinery vs S3 data (~3 min)
bash   numerics/moduli/run_server.sh suite 14            # 320 runs (~66 min on 16 vCPU)
bash   numerics/moduli/run_server.sh fullquad            # symmetry-reduction check (~33 min)
bash   numerics/moduli/run_server.sh kernel              # heat-kernel diagonal (~4 min)
python numerics/moduli/analysis.py                       # all asserts and exports (~10 min)
python theory/locality/check_locality.py                 # exact checks of proof.md (~40 s)
```
