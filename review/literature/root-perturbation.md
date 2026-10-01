# Perturbation of polynomial roots: explicit-constant statements

Retrieved 2026-10-01. Every statement below is transcribed from a fetched PDF. Page numbers are the printed journal or preprint page numbers; equation labels are the source's own. Where PDF text extraction was unreliable (the 1940 Acta scan, and every display containing a constant), the transcription was checked against a rendered image of the page. Mathematical notation is given in LaTeX. Original wording, including French, is kept. Bracketed `[Note: ...]` paragraphs are this review's comments and are not part of any source.

Summary of the constants found:

| Bound on the optimal matching distance between the roots of two monic degree-n polynomials | Constant | Source status |
|---|---|---|
| Ostrowski 1940, Theorem XXX, eq. (71, 1) | $(2n-1)\,\varepsilon$, with $\gamma=\max(|x_\nu|,|y_\nu|)$ (largest root modulus) | **Primary, fetched** |
| Ostrowski 1973 book, Appendix A (as quoted) | $(2n-1)\,\varepsilon$, with $\gamma = 2\max_{\nu>0}(|a_\nu|^{1/\nu},|b_\nu|^{1/\nu})$; strict inequality | Secondary (Ćurgus–Mascioni) |
| Bhatia–Elsner–Krause 1990, Theorem 1 (as quoted) | $4\cdot 2^{-1/n} = 2^{2-1/n}$, same $\gamma$ as the 1973 form | Secondary (two independent papers agree) |
| BEK 1990 (as quoted by Laffey) | $16/(3\sqrt3)$, same $\gamma$, stated for real polynomials | Secondary; **conflicts** with the line above |
| Rahman–Schmeisser 2002, Thm 1.3.1 + Supplement (as quoted) | $4A\delta^{1/n}$ for sufficiently small $\delta$ | Secondary (Ćurgus–Mascioni) |
| Beauzamy 1999, Theorem 4 (local, k-fold root) | $\big(\tfrac{2\,n!}{(n-k)!}\tfrac{(1+|x|^2)^{n/2}}{|P^{(k)}(x)|}\big)^{1/k}\varepsilon^{1/k}$ in Bombieri's norm | **Primary, fetched** |

The primary source for the $4\cdot2^{-1/n}$ constant (BEK 1990) could not be fetched; see "Instrument gaps".

---

## 1. Statements

### 1.1 Ostrowski (1940): Theorem XXX. PRIMARY, fetched

**Bibliographic data (Crossref):** Alexandre Ostrowski, "Recherches sur la méthode de Graeffe et les zéros des polynomes et des séries de Laurent", *Acta Mathematica* **72** (1940), 157–257 (the second part of the memoir; the first part is 99–155, DOI 10.1007/bf02546329). DOI: **10.1007/bf02546330**. Fetched from Project Euclid (open access per Unpaywall): `https://projecteuclid.org/journals/acta-mathematica/volume-72/issue-none/Recherches-sur-la-m%c3%a9thode-de-graeffe-et-les-z%c3%a9ros-des/10.1007/BF02546330.pdf`. The page footer reads "Acta mathematica. 72. Imprimé le 30 avril 1940."

Location: Chapitre IV, § 16 "Continuité des racines des équations algébriques. (Quatrième théorème fondamental.)", Nos. 69–71, pp. 209–212.

Setup, p. 209 (No. 69):

> Soient pour $n > 1$, $a_0 = 1$, $b_0 = 1$:
>
> (69, 1) $f(z) = a_0 z^n + a_1 z^{n-1} + \cdots + a_n = 0;\quad g(z) = b_0 z^n + b_1 z^{n-1} + \cdots + b_n = 0$
>
> deux équations algébriques dont les racines seront désignées resp. par $x_1, \ldots, x_n;\ y_1, \ldots, y_n.$
>
> Posons
>
> (69, 2) $T = \operatorname{Max}\big(1, |a_1|, |b_1|, |a_2|^{\frac12}, |b_2|^{\frac12}, \ldots, |a_n|^{\frac1n}, |b_n|^{\frac1n}\big).$

p. 210:

> En désignant par $y$ une des racines $y_1, \ldots, y_n$, arbitraire mais fixe, on a
>
> (69, 3) $\prod_{\nu=1}^{n} (y - x_\nu) = f(y) = f(y) - g(y) = \sum_{\nu=0}^{n-1} (a_\nu - b_\nu)\, y^\nu.$
>
> Soit $\gamma = \operatorname{Max}(|x_\nu|, |y_\nu|)$ et
>
> (69, 4) $\varepsilon = \sqrt[n]{\sum_{\nu=0}^{n-1} |a_\nu - b_\nu|\, \gamma^\nu}.$
>
> Il résulte alors de (69, 3)
>
> (69, 5) $\prod_{\nu=1}^{n} |y - x_\nu| \le \varepsilon^n.$
>
> De l'autre côté, en posant
>
> (69, 6) $\delta = \sqrt{|a_1 - b_1|^2 + \cdots + |a_n - b_n|^2},$
>
> il résulte en vertu de l'inégalité de Schwarz
>
> (69, 7) $\varepsilon^n \le \delta \sqrt{1 + |y|^2 + \cdots + |y|^{2n-2}}.$
>
> Or, on a d'après Cauchy: $|y| \le 2T$. Donc, en posant
>
> (69, 8) $1 + (2T)^2 + \cdots + (2T)^{2n-2} = M^{2n} < (2T)^{2n},$
>
> (69, 9) $\varepsilon^n \le M^n \delta.$

No. 70 (p. 210) shows that one root can be matched to each root, $|y_\nu - x_{\mu_\nu}| \le \varepsilon$. It then shows by an $n=3$ example (pp. 210–211) that matching each root separately does not by itself give a bijective numbering. No. 71 (pp. 211–212) runs a continuity/connected-component argument, $b_\nu \to a_\nu + t(b_\nu - a_\nu)$. The theorem, p. 212:

> En appliquant ce résultat à $\varepsilon_\nu = \varepsilon$, où $\varepsilon$ est defini par (69, 4), il résulte maintenant de (70, 2), qu'en numérotant les $y_\mu$ convenablement on a
>
> (71, 1) $|y_\nu - x_\nu| \le (2n-1)\,\varepsilon \le (2n-1)\, M \delta^{\frac1n} < 4nT\delta^{\frac1n}, \quad \nu = 1, \ldots, n.$
>
> **XXX.** *Soient (69, 1) deux équations algébriques aux racines $x_\nu$, $\nu = 1, \ldots, n$ et $y_\nu$, $\nu = 1, \ldots, n$. Alors on a, en numérotant les $x_\nu$ et $y_\nu$ convenablement, la relation (71, 1) où $\varepsilon$ est defini par (69, 4), $\delta$ par (69, 6) et $M$ par (69, 2), (69, 8).*
>
> On peut donc dire que les racines d'une équation algébrique du degré $n$ satisfont, comme fonctions des coefficients, à une *condition de Lipschitz d'ordre* $\frac1n$.

[Note: In (69, 1) the coefficient $a_\nu$ multiplies $z^{n-\nu}$. In (69, 3)–(69, 4) as printed, the summation index runs over powers $y^\nu$, $\nu=0,\ldots,n-1$. Read consistently with (69, 1), the sum in (69, 4) is $\sum_{\nu=1}^{n}|a_\nu-b_\nu|\gamma^{n-\nu}$. That is the form in the 1973 restatement (§1.2) and in BEK (§1.3). In the 1940 version, $\gamma$ is the largest root modulus, not a coefficient expression; the text bounds it through Cauchy's $|y|\le 2T$.]

Erratum check: Ostrowski, "Addition à notre mémoire …", *Acta Math.* **75** (1942), 183–186, DOI **10.1007/bf02404105**, was fetched from Project Euclid. It corrects the proof of Théorème XII (pp. 148/49) and discusses a false claim by Rey Pastor, which Ostrowski refutes with the No. 70 example. It does not modify Theorem XXX.

### 1.2 Ostrowski, *Solution of Equations in Euclidean and Banach Spaces* (1973), Appendix A. SECONDARY (verbatim quotation)

Primary not fetched (see gaps). Quoted in:

**Branko Ćurgus and Vania Mascioni, "Roots and polynomials as homeomorphic spaces", arXiv:math/0502037v1 (1 Feb 2005); journal reference (arXiv metadata): Expositiones Mathematicae 24 (2006) no. 1, 81–95.** Section 5 "Final remarks", pp. 14 (arXiv pagination):

> In 1939 Ostrowski [5] published his own form of the perturbation theorem for polynomial roots. We quote it from [6, Appendix A].
>
> **Theorem 5.1.** *Consider two polynomials*
> $f(x) = a_0x^n + \cdots + a_n,\quad a_0 = 1,$
> $g(x) = b_0x^n + \cdots + b_n,\quad b_0 = 1.$
> *Let the $n$ roots of $f(x)$ be $x_1, \ldots, x_n$, those of $g(x)$, $y_1, \ldots, y_n$. Put*
> $\gamma = 2\,\Gamma,\quad \Gamma = \max_{\nu>0}\big(|a_\nu|^{1/\nu}, |b_\nu|^{1/\nu}\big).$
> *Introduce the expression*
> $\varepsilon = \sqrt[n]{\sum_{\nu=1}^{n} |b_\nu - a_\nu|\, \gamma^{n-\nu}}.$
> *The roots $x_\nu$ and $y_\nu$ can be ordered in such a way that we have*
> $|x_\nu - y_\nu| < (2n-1)\,\varepsilon \quad (\nu = 1, \ldots, n).$

Their references: "[5] Ostrowski, A. M., Sur la continuité relative des racines d'équations algébriques, C. R. Acad. Sci. Paris 209 (1939), 777–779." and "[6] Ostrowski, A. M., Solution of equations in Euclidean and Banach spaces. Third edition of Solution of equations and systems of equations. Pure and Applied Mathematics, Vol. 9. Academic Press, 1973."

**Discrepant secondary transcription:** Bohdan Kivva, "On the automorphism groups of distance-regular graphs and rank-4 primitive coherent configurations", arXiv:1802.06959v2, p. 20, cites "[27] Alexander M. Ostrowski. 'Solution of Equations and Systems of Equations' Elsevier, 1966." and states:

> **Theorem 2.32** ([27, Appendix A]). *Let $n \ge 1$ be an integer. Consider two polynomials of degree $n$*
> $f(x) = a_0x^n + \ldots + a_{n-1}x + a_n,\quad g(x) = b_0x^n + \ldots + b_{n-1}x + b_n,$
> *where $a_0 = b_0 = 1$. Denote $M = \max\{|a_i|^{1/i}, |b_i|^{1/i} : 0 \le i \le n\}$ and*
> $\varepsilon = 2n\Big(\sum_{i=1}^{n} |b_i - a_i|(2M)^{n-i}\Big)^{1/n}.$
> *Let $x_1, \ldots, x_n$ denote the roots of $f$ and $y_1, \ldots, y_n$ denote the roots of $g$. Then, there exists a permutation $\sigma \in S_n$ such that for every $1 \le i \le n$*
> $|x_i - y_{\sigma(i)}| \le \varepsilon.$

[Note: Kivva's version uses the factor $2n$ rather than $2n-1$, and its maximum includes $i=0$, which is undefined as printed. It cites the 1966 second edition. It is weaker than, and so implied by, the Ćurgus–Mascioni form. Do not cite it as the exact constant.]

Same source, p. 20, matrix version: "**Theorem 2.33** (Ostrowski [27, Appendix K]). … $M = \max\{|(A)_{ij}|, |(B)_{ij}| : 1 \le i, j \le n\}$, $\delta = \frac{1}{nM}\sum_{i=1}^n\sum_{j=1}^n |(A)_{ij} - (B)_{ij}|$. Then, there exists a permutation $\sigma \in S_n$ such that $|\lambda_i - \mu_{\sigma(i)}| \le 2(n+1)^2 M\delta^{1/n}$, for all $1 \le i \le n$."

### 1.3 Bhatia–Elsner–Krause (1990), polynomial theorem. SECONDARY (primary not fetched)

**Primary bibliographic data (Crossref):** R. Bhatia, L. Elsner, G. Krause, "Bounds for the variation of the roots of a polynomial and the eigenvalues of a matrix", *Linear Algebra and its Applications* **142** (1990), 195–209, December 1990. DOI: **10.1016/0024-3795(90)90267-g**. Unpaywall: is_oa = true (publisher bronze; repository record pub.uni-bielefeld.de/record/1780830). Fetch failed (see gaps).

**Secondary A: Huertas, Lastra, Soto-Larrosa**, "On a moment generalization of some classical second-order differential equations generating classical orthogonal polynomials", arXiv:2307.15415 (v of 28 Jul 2023), p. 17. Published version (Crossref): *Complex Variables and Elliptic Equations* **71** (2025/26), 796–820, DOI 10.1080/17476933.2025.2488008 (published version not checked). Their reference "[4] R. Bhatia, L. Elsner, G. Krause, Bounds for the variation of the roots of a polynomial and the eigenvalues of a matrix. Linear Algebra Appl. 142, 195–209 (1990)."

> **Theorem 2 (Theorem 1, [4])** *Let*
> $f(z) = z^n + a_1z^{n-1} + \ldots + a_n = \prod_{i=1}^n (z - \alpha_i),$
> $g(z) = z^n + b_1z^{n-1} + \ldots + b_n = \prod_{i=1}^n (z - \beta_i).$
> *Then, there exists a permutation of the roots of $f$ and $g$ such that after such permutation one has*
> $\max_i |\alpha_i - \beta_i| \le 2^{2-1/n}\Big(\sum_{k=1}^n |a_k - b_k|\gamma^{n-k}\Big)^{1/n},$
> *where $\gamma = 2\max_{1\le k\le n}\big(|a_k|^{1/k}, |b_k|^{1/k}\big)$.*

**Secondary B: Vsevolod Gubarev**, "$PC$-polynomial of graph", arXiv:1808.03932v1 (12 Aug 2018), p. 19. The citation [23] is BEK 1990: "[23] R. Bhatia, L. Elsner, G. Krause. Bounds for the variation of the roots of a polynomial and the eigenvalues of a matrix. Linear Algebra Appl. 142 (1990), 195–209." Gubarev labels it "Ostrowski's Theorem":

> **Ostrowski's Theorem [23].** Let $f(z), g(z)$ be two monic polynomials of degree $n$ with complex coefficients:
> $f(z) = z^n + a_1z^{n-1} + \ldots + a_n,\quad g(z) = z^n + b_1z^{n-1} + \ldots + b_n.$
> Then the roots of $f$ and $g$ can be enumerated as $\alpha_1, \ldots, \alpha_n$, $\beta_1, \ldots, \beta_n$ respectively in such a way that
> $\max_{k=1,\ldots,n}\{|\alpha_k - \beta_k|\} \le 4\cdot 2^{-1/n}\Big(\sum_{i=1}^n |a_i - b_i|\gamma^{n-i}\Big)^{1/n},$
> where $\gamma = 2\max_{k=1,\ldots,n}\{|a_k|^{1/k}, |b_k|^{1/k}\}$.

Secondaries A and B agree: $2^{2-1/n} = 4\cdot2^{-1/n}$, with the same $\gamma$, and both are stated for complex monic polynomials. A labels it "Theorem 1" of BEK.

**Conflicting secondary C: Thomas J. Laffey**, "A constructive version of the Boyle-Handelman theorem on the spectra of nonnegative matrices", arXiv:1005.0929v1 (6 May 2010), p. 6. Published (Crossref): *Linear Algebra Appl.* **436** (2012), 1701–1709, DOI 10.1016/j.laa.2011.09.023 (published version not fetched: ScienceDirect 403). His reference [3] is "R. Bhatia, G. Krause and L. Elsner Bounds for the roots of a polynomial and the eigenvalues of a matrix. Linear Algebra Appl. 142 (1990) 195-209."

> To obtain the desired bound we use the following refinement by Bhatia, Elsner and Krause [3] of a classical result of Ostrowski.
>
> **Theorem 4** *Let $f(x) = x^n + a_1x^{n-1} + \ldots + a_n$ and $g(x) = x^n + b_1x^{n-1} + \ldots + b_n$ be real polynomials with roots $\alpha_1, \ldots, \alpha_n$ and $\beta_1, \ldots, \beta_n$, respectively. Then there is a labelling of $\beta_1, \ldots, \beta_n$ such that*
> $\max\{|\alpha_i - \beta_i| : 1 \le i \le n\} \le \Big(\frac{16}{3\sqrt3}\Big)\Big(\sum_{k=1}^n |a_k - b_k|\gamma^{n-k}\Big)^{1/n},$
> *where $\gamma = 2\max\{|a_k|^{1/k}, |b_k|^{1/k} : 1 \le k \le n\}$.*
>
> [The original Ostrowski result had the factor $(2n-1)$ in place of $\big(\frac{16}{3\sqrt3}\big)$].

[Note: $16/(3\sqrt3) \approx 3.079$, while $4\cdot2^{-1/n}$ increases from $2\sqrt2 \approx 2.83$ ($n=2$) toward $4$. Laffey's statement is restricted to real polynomials. These facts are consistent with BEK containing a separate sharper result for real coefficients, or with a transcription error. This review cannot settle which from fetched text. **For the paper, the safe constant is $4\cdot 2^{-1/n}$ (equivalently $\le 4$) for complex monic polynomials, attested by two independent secondaries.** It should be checked against p. 195–209 of the primary before citing "Theorem 1" by number.]

**Matrix analogue of BEK (for context), secondary:** Gaubert and Sharify, "Tropical Scaling of Polynomial Matrices", arXiv:0905.0121, p. 8 (journal ref: Proc. POSTA 09, Springer LNCIS 389, pp. 291–303, 2009, DOI 10.1007/978-3-642-02894-6_28): "**Theorem 1** ([5]). Let $A,B \in \mathbb{C}^{n\times n}$. Then $v(A,B) \le 4\times 2^{-1/n}(\|A\|+\|B\|)^{1-1/n}\|A-B\|^{1/n}$." Here $v$ is the optimal-matching variation defined below. Rafikul Alam, "A brief overview of spectral perturbation Theory", arXiv:2512.06962v1, p. 28, states the same result as "Theorem 4.10 (Bhatia-Elsner-Krause, [21]) … $d_m(\mathrm{eig}(A), \mathrm{eig}(B)) \le 4(\|A\|_2+\|B\|_2)^{1-1/n}\|A-B\|_2^{1/n}$". His proof yields the intermediate constant $2^{(2n-1)/n}$. He also quotes the key lemma: "**Lemma 4.9.** [21] Let $C$ be a continuous curve in $\mathbb{C}$ with endpoints $a$ and $b$. If $p(z)$ is a monic complex polynomial of degree $n$, then $\max_{z\in C}|p(z)| \ge \frac{|b-a|^n}{2^{2n-1}}$."

### 1.4 Rahman–Schmeisser (2002), Theorem 1.3.1 and Supplement. SECONDARY

Quoted in Ćurgus–Mascioni (arXiv:math/0502037, pp. 14–15), citing "[8] Rahman, Q. I., Schmeisser, G., Analytic theory of polynomials, Oxford University Press, 2002" [Theorem 1.3.1 and Supplement]:

> **Theorem 5.3.** *Let $f(z) = \sum_{\nu=0}^n a_\nu z^\nu = \prod_{j=1}^k (z - z_j)^{m_j}$ $(m_1 + \cdots + m_k = n)$ be a monic polynomial of degree $n$ with distinct zeros $z_1, \ldots, z_k$ of multiplicities $m_1, \ldots, m_k$. Then, given a positive $\varepsilon < \min_{1\le i\le j\le k}|z_i - z_j|/2$, there exists a $\delta > 0$ so that any monic polynomial $g(z) = \sum_{\nu=0}^n b_\nu z^\nu$ whose coefficients satisfy $|b_\nu - a_\nu| < \delta$, for $\nu = 1, \ldots, n-1$, has exactly $m_j$ zeros in the disc $D(z_j, \varepsilon)$ $(j = 1, \ldots, k)$.*
> *Further, if we let $A := \max\{1, 2|a_\nu|^{1/(n-\nu)} : \nu = 0, \ldots, n-1\}$, and let the zeros of $f$ be denoted by $\zeta_1, \ldots, \zeta_n$, where an $m$-fold zero is now listed $m$ times, then, for sufficiently small $\delta > 0$, there exists a numbering of the zeros of $g$ as $\omega_1, \ldots, \omega_n$ such that $\max_{1\le\nu\le n}|\omega_\nu - \zeta_\nu| \le 4A\delta^{1/n}$.*

[Note: The quotation reads "$\nu = 1, \ldots, n-1$" as printed. With $f=\sum a_\nu z^\nu$ monic, the free coefficients are $\nu=0,\ldots,n-1$. Check the primary before relying on the index range.]

### 1.5 Local version (k-fold root moves by $O(\varepsilon^{1/k})$): Beauzamy (1999). PRIMARY, fetched

**Bibliographic data (Crossref):** Bernard Beauzamy, "How the Roots of a Polynomial Vary with its Coefficients: A Local Quantitative Result", *Canadian Mathematical Bulletin* **42**(1) (1999), 3–12. DOI: **10.4153/cmb-1999-001-6**. Open access PDF via Cambridge Core (Unpaywall).

Restatement of Ostrowski, p. 3 (with his refs "[6] A. Ostrowski, Recherches sur la méthode de Graeffe. Acta Math. 72, 1940." and "[7] —, Solutions of equations and systems of equations (Appendix B). Academic Press, New-York, 1960."):

> (1) Let $P = \sum_0^n a_{n-j}z^j$, $Q = \sum_0^n b_{n-j}z^j$, be two polynomials, satisfying $a_0 = b_0 = 1$, and with respective roots $x_1, \ldots, x_n, y_1, \ldots, y_n$. Let
> $T = \max\{1, |a_1|, |b_1|, \ldots, |a_k|^{1/k}, |b_k|^{1/k}, \ldots, |a_n|^{1/n}, |b_n|^{1/n}\}.$
> Then, if the $y_j$'s are suitably ordered, we have, for all $j$,
> $|x_j - y_j| \le 4nT\delta^{1/n}$ with $\delta = \Big(\sum_0^n |a_j - b_j|^2\Big)^{1/2}.$

This matches the last inequality of Ostrowski's (71, 1) in §1.1.

Bombieri norm, p. 4, eq. (1): for $P = \sum_0^n a_jz^j$ of degree $n$,
$[P] = \Big(\sum_0^n \frac{|a_j|^2}{\binom{n}{j}}\Big)^{1/2}.$
Hypothesis (2): $Q$ "another polynomial, with same degree, satisfying $[P - Q] \le \varepsilon$."

Theorem 1 (simple root), p. 4:

> **Theorem 1** *If $x$ is any zero of $P$, there exists a zero $y$ of $Q$, with*
> (3) $|x - y| \le \frac{n(1+|x|^2)^{n/2}}{|Q'(x)|}\varepsilon.$
> *If $\varepsilon$ is small enough, namely*
> (4) $\varepsilon \le \frac12\frac{|P'(x)|}{n(1+|x|^2)^{\frac{n-1}{2}}}$
> *then (3) implies*
> (5) $|x - y| \le \frac{2n(1+|x|^2)^{n/2}}{|P'(x)|}\varepsilon.$

Theorem 4 (multiplicity $k$), p. 7:

> Let us now give a more general version of Theorem 1, valid if $x$ has multiplicity $k$, empty if it has multiplicity $k + 1$:
>
> **Theorem 4** *Let $k \ge 1$ be an integer, $P$ and $Q$ be two polynomials of degree $n$, with $[P - Q] \le \varepsilon$. If $x$ is any zero of $P$, there exists a zero $y$ of $Q$, with*
> (15) $|x - y| \le \Big(\frac{n!}{(n-k)!}\frac{(1+|x|^2)^{n/2}}{|Q^{(k)}(x)|}\Big)^{1/k}\varepsilon^{1/k}.$
> *If $\varepsilon$ is small enough, namely*
> (16) $\varepsilon \le \frac{(n-k)!}{2\,n!}\frac{|P^{(k)}(x)|}{(1+|x|^2)^{\frac{n-k}{2}}}$
> *then (15) implies*
> (17) $|x - y| \le \Big(\frac{2\,n!}{(n-k)!}\frac{(1+|x|^2)^{n/2}}{|P^{(k)}(x)|}\Big)^{1/k}\varepsilon^{1/k}.$

Section 3, p. 9, case $P = (z-a)^n$: "(22) $|b_j - a| \le 2^{1/n}(1+|a|^2)^{1/2}\varepsilon^{1/n}$." p. 10: "This estimate is best possible in general: if $Q = (z-a)^n - \varepsilon$, then $[P-Q] = \varepsilon$, and $|b_j - a| = \varepsilon^{1/n}$ for all $j$."

[Note: Theorem 4 gives, for each zero $x$ of $P$ of multiplicity exactly $k$ (so $P^{(k)}(x)\ne0$), *some* zero $y$ of $Q$ within the stated distance. It does not by itself assert that $k$ zeros of $Q$ lie in that disc. For a count, combine it with Theorem 5.3 of §1.4 (Rouché-type, non-explicit $\delta$) or with the 1940 component argument of §1.1, No. 71.]

Other local results that were identified but not fetched: Ostrowski, "A theorem on clusters of roots of polynomial equations", *SIAM J. Numer. Anal.* **7**(4) (1970), 567–570, DOI 10.1137/0707046; Galántai and Hegedűs, "Perturbation bounds for polynomials", *Numer. Math.* **109** (2008), 77–100, DOI 10.1007/s00211-007-0124-8. Hundrieser, Manole, Litskevich, Munk, "Local Poisson Deconvolution for Discrete Signals", arXiv:2508.00824, pp. 18–19, states Lemma 12 (Ostrowski 1973, p. 276) and a local clustered version (Proposition 13) only with unspecified constants "$C = C(\Theta,k)$". They give no explicit constants, so these are not transcribed.

---

## 2. Definitions of the quantities

**Optimal matching distance.** Verbatim, Alam (arXiv:2512.06962, p. 27):
$d_m(\mathrm{eig}(A), \mathrm{eig}(B)) := \min_{\sigma\in S_n}\Big(\max_{1\le j\le n}|\lambda_j(A) - \lambda_{\sigma(j)}(B)|\Big),$ "where $S_n$ is the set of all permutations of $\{1, 2, \ldots, n\}$."

For roots, Gaubert–Sharify (arXiv:0905.0121, p. 7), "Definition 1. Let $\lambda_1,\ldots,\lambda_n$ and $\mu_1\ldots\mu_n$ denote two sequences of complex numbers. The variation between $\lambda$ and $\mu$ is defined by $v(\lambda,\mu) := \min_{\pi\in S_n}\{\max_i |\mu_{\pi(i)} - \lambda_i|\}$, where $S_n$ is the set of permutations of $\{1,2,\ldots,n\}$." Ćurgus–Mascioni (arXiv:math/0502037, Section 2) call it the Fréchet metric, $d_F(U,V) := \min_{\sigma\in\Pi_m}\max_{k}|u_k - v_{\sigma(k)}|$ on multisets. Every theorem in §1.1–1.4 is the statement that $d_m(\text{roots of } f, \text{roots of } g) \le$ (bound). The phrases "en numérotant convenablement", "can be ordered", and "there exists a permutation" are this statement.

**$\gamma$, and the coefficient convention.** All the explicit global statements use monic $f(z) = z^n + a_1z^{n-1} + \cdots + a_n$, so $a_k$ is the coefficient of $z^{n-k}$.
- BEK (as quoted) and Ostrowski 1973 (as quoted) define $\gamma = 2\max_{1\le k\le n}\big(|a_k|^{1/k}, |b_k|^{1/k}\big)$ and $\varepsilon^n = \sum_{k=1}^n |a_k - b_k|\gamma^{n-k}$.
- Ostrowski 1940 defines $\gamma = \max(|x_\nu|, |y_\nu|)$, the largest modulus of any root of $f$ or $g$. He notes, after Cauchy, $|y| \le 2T$, where $T = \max(1, |a_1|, |b_1|, \ldots, |a_n|^{1/n}, |b_n|^{1/n})$. So the 1940 $\gamma$ is at most $2T$.
- Rahman–Schmeisser (as quoted) use $f = \sum a_\nu z^\nu$ (coefficient of $z^\nu$) and $A = \max\{1, 2|a_\nu|^{1/(n-\nu)}\}$.

---

## 3. Search log

All requests were headless (curl with a desktop UA, the APIs listed, PyMuPDF `fitz` for text, and page renders for visual verification). Raw files are in a local scratch directory (`lit-d/`, not committed).

1. Crossref `query.bibliographic` for the BEK title returned DOI 10.1016/0024-3795(90)90267-g (LAA 142, 195–209, Dec 1990). It also returned Krause, "Bounds for the variation of matrix eigenvalues and polynomial roots", LAA 208–209 (1994) 73–82, DOI 10.1016/0024-3795(94)90432-4, and Bhatia, *Perturbation Bounds for Matrix Eigenvalues*, DOI 10.1137/1.9780898719079.
2. Unpaywall on BEK 1990 gave is_oa true, with locations doi.org (publisher) and pub.uni-bielefeld.de/record/1780830, and no direct PDF URL. Unpaywall on Krause 1994 gave the sciencedirect `/pdf` URL. Unpaywall on SIAM book 10.1137/1.9780898719079 gave is_oa false.
3. OpenAlex W2057039113 (47 citations) showed the same locations and no PDF. Semantic Scholar (anonymous) showed openAccessPdf = doi.org link (BRONZE) and 55 citations.
4. ScienceDirect PDFs for BEK 1990 and Krause 1994 returned 403. Bielefeld returned a JS proof-of-work bot wall. Elsevier API returned 406.
5. arXiv full-text search (POST `search_classic`, `searchtype=ft`, redirected to search.arxiv.org). Queries: `"optimal matching distance" roots polynomial` (18 hits); `"Bhatia, Elsner and Krause"` (1 hit: 1405.4031); `Ostrowski "optimal matching distance"` (4 hits); `"variation of the roots" Ostrowski` (2); `Ostrowski "continuity of roots"` (9); `"Bounds for the variation of the roots of a polynomial"` (9); `Ostrowski "Solution of Equations" roots matching` (11); `"roots of a polynomial" "Bhatia" "Krause"` (11).
6. Downloaded and grepped: 2508.00824, 2512.06962, 1405.4031, 1811.03227, 1912.10571, 1802.06959, 1912.05001, math/0502037, 2206.13013. Useful: math/0502037 (Ostrowski 1973 Thm, Rahman–Schmeisser), 1802.06959 (Kivva variant), 2512.06962 (matrix BEK, definitions), 2508.00824 (non-explicit Lemma 12).
7. Semantic Scholar `/citations` of BEK 1990 (55 records) gave arXiv IDs for citing papers. Downloaded math/0502027, 0905.0121, 1609.07221, 1812.00532, 1005.0929, 2307.15415, 2104.02111, 1909.10589, 1808.03932. Useful: 2307.15415 ($2^{2-1/n}$), 1808.03932 ($4\cdot2^{-1/n}$), 1005.0929 ($16/(3\sqrt3)$, real), 0905.0121 (matrix). 1812.00532 quotes a matrix-eigenvalue consequence "$|\lambda_{\max}(A+E) - \lambda_{\max}(A)| \le 12\|A\|^{1-1/p}\|E\|^{1/p}$" (p. 36), not used. MDPI *Mathematics* 12 (2024) 2993 (DOI 10.3390/math12192993) PDF returned 403.
8. Crossref for Ostrowski 1940 returned DOIs 10.1007/bf02546329 (pp. 99–155) and 10.1007/bf02546330 (pp. 157–257), plus the Addition, 10.1007/bf02404105 (Acta 75, 183–186). Unpaywall pointed to Project Euclid PDFs, and all three downloaded (HTTP 200). Theorem XXX was located at pp. 209–212 of bf02546330 and verified against rendered page images.
9. Crossref and Unpaywall for Beauzamy 1999 (10.4153/cmb-1999-001-6) gave a Cambridge Core OA PDF, downloaded. Ostrowski 1970 (10.1137/0707046) and Galántai–Hegedűs 2008 (10.1007/s00211-007-0124-8) were is_oa false.
10. Crossref for Bhatia GTM 169 Chapter VIII "Spectral Variation of Nonnormal Matrices" gave DOI 10.1007/978-1-4612-0653-8_8, with Unpaywall is_oa false. The Springer PDF URL returned an HTML paywall page.
11. Internet Archive advancedsearch found Ostrowski's books (`solutionofequati0000ostr` 1973; `solutionofequati02edamos` 1966). Both are lending-restricted, and the text download returned 401.

## 4. Instrument gaps

| Source | URL attempted | Error |
|---|---|---|
| BEK 1990 (primary, LAA 142:195–209) | `https://www.sciencedirect.com/science/article/pii/002437959090267G/pdf` and the landing page `.../pii/002437959090267G` | HTTP 403 |
| BEK 1990, repository copy | `https://pub.uni-bielefeld.de/record/1780830` (and `.json`) | Anubis JavaScript proof-of-work bot challenge; not bypassed |
| BEK 1990, Elsevier API | `https://api.elsevier.com/content/article/doi/10.1016/0024-3795(90)90267-G?httpAccept=application/pdf` | HTTP 406 |
| Krause 1994, LAA 208–209:73–82 (later improvement, possibly the source of other constants) | `https://www.sciencedirect.com/science/article/pii/0024379594904324/pdf` | HTTP 403 |
| Laffey 2012, published LAA version | `https://www.sciencedirect.com/science/article/pii/S0024379511006562/pdf` (Unpaywall) | not attempted after repeated ScienceDirect 403s; arXiv version used |
| Bhatia, *Matrix Analysis*, GTM 169, Ch. VIII | `https://link.springer.com/content/pdf/10.1007/978-1-4612-0653-8_8.pdf` | HTTP 200 but HTML paywall page, no PDF; Unpaywall is_oa false |
| Bhatia, *Perturbation Bounds for Matrix Eigenvalues* (SIAM Classics) | Unpaywall for 10.1137/1.9780898719079 | is_oa false; Internet Archive search: 0 items |
| Ostrowski, *Solution of Equations in Euclidean and Banach Spaces* (1973), Appendix A; 2nd ed. 1966 | `https://archive.org/download/solutionofequati0000ostr/solutionofequati0000ostr_djvu.txt` | HTTP 401 (lending-restricted item) |
| Ostrowski 1970, SIAM J. Numer. Anal. 7:567–570 | Unpaywall 10.1137/0707046 | is_oa false; not fetched |
| Galántai–Hegedűs 2008, Numer. Math. 109:77–100 | Unpaywall 10.1007/s00211-007-0124-8 | is_oa false; not fetched |
| Rahman–Schmeisser, *Analytic Theory of Polynomials* (2002), Thm 1.3.1 | not attempted (no OA route identified) | known only through the Ćurgus–Mascioni quotation |
| MDPI *Mathematics* 12(19):2993 (2024) | `https://www.mdpi.com/2227-7390/12/19/2993/pdf?version=1727335919` | HTTP 403 |
| Ostrowski, C. R. Acad. Sci. Paris 209 (1939) 777–779 | not attempted | n/a |

Consequence for the paper: the $(2n-1)$ constant is verified against the 1940 primary, in its 1940 form with $\gamma$ the largest root modulus. The 1973 coefficient-$\gamma$ form, the BEK constant $4\cdot2^{-1/n}$, and its theorem number rest on secondary quotations. The BEK constant has two concordant secondaries and one conflicting one ($16/(3\sqrt3)$, real case). Before citing BEK by theorem number, verify it against LAA 142, pp. 195–209.
