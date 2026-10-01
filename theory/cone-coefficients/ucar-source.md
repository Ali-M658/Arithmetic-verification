# Source transcription: cone-point heat coefficients

Retrieved 2026-10-01 by headless curl (desktop User-Agent) from https://arxiv.org/pdf/1711.03405 (156 PDF pages) and https://arxiv.org/pdf/1812.06119 (21 pages). Local copies are in the session scratchpad, not the repo.

Method of transcription: text extraction (pymupdf) was used only to locate pages; every equation below was transcribed from a 130-dpi rendering of the page, read visually. Text extraction was cross-compared for (4.33)/(4.34) and the exponents/binomials of (4.25) and agreed. No ambiguity remained in the displayed equations. The one reading choice: in (4.25) the symbol B_{2j} is a Bernoulli number and B_{2l+2-2j}(1/2) is a Bernoulli polynomial at 1/2 (distinguished in the thesis by the argument; definitions in (3.69), see below).

## 1. Ucar, Spectral invariants for polygons and orbisurfaces (Humboldt Dissertation), arXiv:1711.03405

PDF page index = printed page + 5.

### Equation (4.25): PDF page 139, printed page 134 (inside Proposition 4.17)

```latex
c^{\mathbb S}_{\ell}\!\left(\frac{\pi}{k}\right)
  = \frac{1}{4k}\cdot\frac{(-1)^{\ell}}{(\ell+1)!}\cdot\frac{1}{2\ell+1}
    \sum_{j=0}^{\ell+1}\binom{2\ell+2}{2j}\,\bigl(k^{2j}-1\bigr)\,B_{2j}\,B_{2\ell+2-2j}\!\left(\frac12\right)
```

Proposition 4.17 (same page) sets k in N, lune with angle pi/k in S^2(r), kappa = 1/r^2, and its (4.24) is
Z_Omega(t) ~ (1/2k)(1/(kappa t)) - (sqrt(pi)/(4 sqrt(kappa)))(1/sqrt(t)) + sum_{nu>=0} { (1/2k) i^S_nu - (1/(4^{nu+1}(nu+1)!)) (sqrt(pi) sqrt(kappa)/4) sqrt(t) [sic, as printed] + 2 sum_{l=0}^{nu} (1/(4^l l!)) c^S_{nu-l}(pi/k) } kappa^nu t^nu.
The thesis notes c^S_l(gamma) is "recalled from the Remark after Corollary 3.30"; (4.25) is the closed form for gamma = pi/k and needs nothing further.

### Equation (4.33): PDF page 142, printed page 137 (Corollary, part (ii))

```latex
C=\sum_{\nu=0}^{\infty}\sum_{\ell=0}^{\nu}\frac{2}{4^{\ell}\cdot \ell!}\; c^{\mathbb S}_{\nu-\ell}\!\left(\frac{\pi}{k}\right)\kappa^{\nu}t^{\nu}
```

with c^S_l(pi/k) from (4.25). Immediately after, same page, equation (4.34):

```latex
\frac1k\sum_{\ell=1}^{k-1} b_{\nu}\bigl(\tilde D_{\ell}\bigr)=\sum_{\ell=0}^{\nu}\frac{2}{4^{\ell}\cdot \ell!}\; c^{\mathbb S}_{\nu-\ell}\!\left(\frac{\pi}{k}\right)\kappa^{\nu}\quad\text{for all }\nu\in\mathbb N_0 .
```

Reading: the heat-trace coefficient at t^nu of a cone point of order k (averaged dihedral/rotation contribution) is b_nu = kappa^nu * sum_{l=0}^{nu} 2/(4^l l!) c_{nu-l}(pi/k). Hence b_nu/kappa^nu depends on k = m only.

### Definitions needed (printed p. 76, PDF 82, equation (3.69), and Lemma 4.14, PDF 136)

Bernoulli polynomials: t e^{xt}/(e^t - 1) = sum_{k>=0} B_k(x) t^k/k! for |t| < 2 pi; B_k := B_k(0). Hence B_1 = -1/2 (also stated explicitly, PDF 90), B_{2k+1} = 0 for k in N, B_{2k+1}(1/2) = 0 (3.70). Lemma 4.14, eq. (4.15): -B_n(1/2) = B_n (1 - 1/2^{n-1}) for all n in N_0. Only even indices occur in (4.25). kappa is the (constant) Gaussian curvature (kappa = 1/r^2 for the sphere of radius r); k in N is the order of the cone point (the manuscript's m).

Note: p. 136/PDF 141 and (4.35) use the same B_{2l}(1/2) notation. The thesis states (PDF 136) that the corresponding statements in [Wat05] had typographical errors and that Proposition 4.17 is reproduced "with minor corrections".

## 2. Schueth, On the corner contributions to the heat coefficients, arXiv:1812.06119

### Theorem 4.1: PDF/printed page 14

```latex
a_2^{(\{\bar p\})}
 =\Bigl[\tfrac{1}{2520}\bigl(k^{5}-\tfrac1k\bigr)+\tfrac{1}{720}\bigl(k^{3}-\tfrac1k\bigr)+\tfrac{1}{180}\bigl(k-\tfrac1k\bigr)\Bigr]K(\bar p)^{2}
 -\Bigl[\tfrac{1}{15120}\bigl(k^{5}-\tfrac1k\bigr)+\tfrac{1}{1440}\bigl(k^{3}-\tfrac1k\bigr)+\tfrac{1}{180}\bigl(k-\tfrac1k\bigr)\Bigr]\Delta_g K(\bar p).
```

(For a cone point of order k in an orbisurface; the K^2 coefficient is the constant-curvature part, comparable to Ucar's b_2/kappa^2.)

### Remark 4.2: printed page 14

```latex
a_0^{(\{\bar p\})}=\frac1{12}\Bigl(k-\frac1k\Bigr),\qquad
a_1^{(\{\bar p\})}=\Bigl[\frac1{360}\bigl(k^{3}-\tfrac1k\bigr)+\frac1{36}\bigl(k-\tfrac1k\bigr)\Bigr]K(\bar p).
```

The page ends here (remark continues onto page 15 with further items not needed). Intro p. 3 gives the matching c_0, c_1, c_2 for gamma = pi/k in terms of pi and gamma.

## 3. Verification results (see verify_cone_coefficients.py, verify_output.txt)

Convention reconciliation: Ucar uses kappa (constant Gaussian curvature) with b_l = kappa^l * [row]; Schueth uses K(p), which equals kappa at constant curvature (the Delta_g K term vanishes). So the K^2 coefficient in Theorem 4.1 equals Ucar's b_2/kappa^2; no sign or normalisation difference was required. Indexing: Schueth's a_l is the t^l coefficient, as is Ucar's b_l.

Computed (exact, from (4.25)+(4.33)), with p_l(m) = m * b_l/kappa^l:

- l=3: b_3/kappa^3 = (m^2-1)(m^2+3)(3m^4+2m^2+19)/(30240 m); p_3 = (3m^8+8m^6+14m^4+32m^2-57)/30240 = m^8/10080 + m^6/3780 + m^4/2160 + m^2/945 - 19/10080.
- l=4: b_4/kappa^4 = (m^2-1)(70m^8+235m^6+477m^4+785m^2+1313)/(1995840 m); p_4 = m^10/28512 + m^8/12096 + 11 m^6/90720 + m^4/6480 + m^2/3780 - 1313/1995840.

The two stated l=3 forms are consistent: expand((m^2-1)(m^2+3)(3m^4+2m^2+19)) = 3m^8+8m^6+14m^4+32m^2-57 exactly.

## Run output

```
l=0: b_l/kappa^l = (m - 1)*(m + 1)/(12*m)
      p_0(m) = m**2/12 - 1/12
l=1: b_l/kappa^l = (m - 1)*(m + 1)*(m**2 + 11)/(360*m)
      p_1(m) = m**4/360 + m**2/36 - 11/360
l=2: b_l/kappa^l = (m - 1)*(m + 1)*(2*m**4 + 9*m**2 + 37)/(5040*m)
      p_2(m) = m**6/2520 + m**4/720 + m**2/180 - 37/5040
l=3: b_l/kappa^l = (m - 1)*(m + 1)*(m**2 + 3)*(3*m**4 + 2*m**2 + 19)/(30240*m)
      p_3(m) = m**8/10080 + m**6/3780 + m**4/2160 + m**2/945 - 19/10080
l=4: b_l/kappa^l = (m - 1)*(m + 1)*(70*m**8 + 235*m**6 + 477*m**4 + 785*m**2 + 1313)/(1995840*m)
      p_4(m) = m**10/28512 + m**8/12096 + 11*m**6/90720 + m**4/6480 + m**2/3780 - 1313/1995840
expand((m^2-1)(m^2+3)(3m^4+2m^2+19)) = 3*m**8 + 8*m**6 + 14*m**4 + 32*m**2 - 57
30240*p_3(m)                         = 3*m**8 + 8*m**6 + 14*m**4 + 32*m**2 - 57
l=0: leading coeff of p_l = 1/12 = |B_2|/(2 (l+1)! (2l+1))
l=1: leading coeff of p_l = 1/360 = |B_4|/(2 (l+1)! (2l+1))
l=2: leading coeff of p_l = 1/2520 = |B_6|/(2 (l+1)! (2l+1))
l=3: leading coeff of p_l = 1/10080 = |B_8|/(2 (l+1)! (2l+1))
l=4: leading coeff of p_l = 1/28512 = |B_10|/(2 (l+1)! (2l+1))
l=5: leading coeff of p_l = 691/43243200 = |B_12|/(2 (l+1)! (2l+1))
l=6: leading coeff of p_l = 1/112320 = |B_14|/(2 (l+1)! (2l+1))
ALL ASSERTS PASSED
```
