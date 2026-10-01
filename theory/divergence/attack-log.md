# Attack log: divergence rate and the largest cone

## Protocol

A separate reviewer received only `proof.md` and the cited papers. The reviewer had no scripts,
outputs or literature note, and was asked to break every statement, numerically included. All
of the reviewer's computations used exact rationals or 60–80-digit mpmath.

- **Exact recomputation.** $c_\ell$, $\beta_\ell$, $s_k$ and $a_\ell$ were rebuilt from Uçar's
  formulas; $a_0(2,8,8)$, $a_1(2,8,8)$ and $a_1(3,3,12)$ were reproduced.
- **Lemma 1.** Checked against independent sympy series, $k\in\{2,3,5,7\}$. Positivity was
  checked exactly for $\ell\le150$, $k\le60$.
- **Theorem 2.** Tested for $\ell\le150$, $m\in\{2,3,7,50\}$.
- **Dryden–Strohmaier coefficients.** Computed from closed-form moments (Hurwitz and digamma),
  validated by quadrature, up to $\ell=100$ and $m=50$.
- **Theorem 3, adversarial multisets:**
  - $\{49,50\}$ and $1000\times49+\{50\}$;
  - $20\times7+\{8\}$;
  - genus $10^4$ and $10^6$;
  - no cones;
  - spherical cases.
- **Truncation.** Checked at $t=0.02,0.01,0.005$.
- **Literature.** Uçar Thm 3.40 and Cor. 4.21, and Dunne, checked in the PDFs.

## Findings and responses

| # | severity | finding | response |
|---|---|---|---|
| F1, F2, F4, F5, F9, F10, F14, F15, F17 | NONE-CONFIRMED | Generating-function identity; positivity for all tested $\ell$ (the proof is correct); no double poles for $k=2$, since $G_2=(t/2)^2\operatorname{sech}(t/2)$; Theorem 2 with its $1/\ell$ constant; Dryden–Strohmaier agreement to $10^{-59}$ up to $\ell=100$; Theorem 3 for fixed orbifolds; truncation orders 3, 7, 14 against predicted 3.4, 6.9, 13.7; Borel radius and Pringsheim; Dunne citation; the "remark" recommendation | — |
| F3 | MINOR | Lemma 1(c) error stated as $O((\rho/2)^{2\ell})$, but the proof's own Cauchy estimate gives $O((2\rho)^{-2\ell})$. The true error is $\Theta(4^{-\ell})$ for $k\ge3$ and $O(9^{-\ell})$ for $k=2$ | **Fixed** in Lemma 1(c) and in the proof of Theorem 2. Pole structure stated: poles are simple, at $2\pi in/k$ with $k\nmid n$ |
| F6 | MINOR | "$\ell^2r_\ell$ converges to $\pi^4/(32m^4)$: 0.1938, 0.0382" quoted the $\ell=120$ values, not the limits (0.1903, 0.0376) | **Fixed.** Both are given |
| F7 | MINOR | Theorem 2's remainder is not uniform in $m$: $O(\ell^{-2}m^{-4}+4^{-\ell})$ | **Fixed.** Stated, with the $m=50$, $\ell=5$ example |
| F8 | MINOR | $p_\ell$ undefined; index $b$ undefined in the Dryden–Strohmaier paragraph; for $m=2$ the classes $l=1$ and $l=m-1$ coincide | **Fixed.** $p_\ell=m\beta_\ell$ defined; double-sum indices defined; $m=2$ half-line factor explained; $K$-independence of $\beta_\ell$ stated, so the $K=-1$ check covers $K=+1$ |
| F11 | MINOR | The $O(1/\ell)$ in Theorem 3 is not uniform. $1000\times49+\{50\}$ still rounds to 49 at $\ell=150$, and genus $10^4$ with one cone of order 2 is dominated by the smooth part for $\ell\le5$ | **Fixed.** The error is written as $O(1/\ell)+O(\sum_{m_i<M}(m_i/M)^{2\ell})+O(C\ell M^{-2\ell})$, with both examples. Recommendation item 4 now names multiplicities and $|\chi|$ |
| F12 | MINOR | For no cones, convergence is only $O(1/\ell)$; "smooth part behaves like $m=1$" is heuristic ($A_\ell(1)$ undefined) | **Fixed.** Both stated (consistent with D6: 1.0041 at $\ell=120$, genus 2) |
| F13 | MINOR | The peeling step applies Theorem 3 to sequences that are no longer orbifold traces | **Fixed.** Theorem 3 is restated for $a_\ell=Cs_{\ell+1}K^{\ell+1}+K^\ell\sum\beta_\ell(m_i)$ with any $C\ge0$; the proof never used a link between $C$ and the $m_i$. Assumptions of Corollary 4 listed; tail-only strengthening noted |
| F16 | MINOR | Uçar's $W_{\nu,1}=\sum2(m^2-1)(m/\pi)^{2\nu+1}$ has ratio tending to $M^2/\pi^2$, the same rate, and his $\theta_1=\pi/M$ is the same angle. So "smallest-rotation-angle interpretation" is not a separate novelty, and the remark's "second, asymptotic route" should credit Uçar's route as asymptotic too | **Accepted and fixed** in §5, §6, the suggested remark and `STATUS.md`. What remains new: the raw-coefficient asymptotics with $\sigma_m$ and the $1/\ell$ term, no extraction, tail-only peeling, and the Borel radius statement |

## Verdict after revision

No fatal or serious defects were found. The recommendation (a remark, not a proposition) is
endorsed by the reviewer and kept. The novelty claim is narrowed per F16.
