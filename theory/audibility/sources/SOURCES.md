# Fetched third-party statements

Retrieved headlessly on 2026-10-01 (curl and PyMuPDF text extraction). Excerpts below are
transcribed from the fetched text layers. Mathematical typesetting is flattened, but the
wording is unchanged. Bibliographic metadata comes from the Crossref API.

## [HT] Holtz and Tyaglov: Hurwitz determinants and Orlando's formula

- O. Holtz, M. Tyaglov, *Structured matrices, continued fractions, and root localization of
  polynomials*, SIAM Review **54**(3) (2012) 421–509. doi:10.1137/090781127,
  arXiv:0912.4703.
- Fetched: `https://arxiv.org/pdf/0912.4703` (79 pp., sha256 `b9446f22…838d4f`).

Eq. (1.2), the polynomial convention:

> p(z) := a0 z^n + a1 z^{n−1} + · · · + an, a0, a1, . . . , an ∈ C, a0 ≠ 0,

Eq. (1.37) and Definition 1.16, the Hurwitz determinants:

> ∆j(p) = det [ a1 a3 a5 a7 . . . a2j−1 ; a0 a2 a4 a6 . . . a2j−2 ; 0 a1 a3 a5 . . . a2j−3 ;
> 0 a0 a2 a4 . . . a2j−4 ; . . . ; 0 0 0 0 . . . aj ], j = 1, . . . , n, (1.37)
> where we set ai := 0 for i > n.
> Definition 1.16. The determinants ∆j(p) (j = 1, . . . , n) are called the Hurwitz
> determinants or the Hurwitz minors of the polynomial p.

Theorem 1.17, Orlando's formula:

> Theorem 1.17 (Orlando, [73, 36]). Let the polynomial p of degree n be given by (1.2). Then
> the determinant ∆n−1(p) defined by (1.37) can be computed from the formula
> ∆n−1(p) = (−1)^{n(n−1)/2} a0^{n−1} ∏_{1≤i<j≤n} (zi + zj), (1.41)
> where zi, i = 1, . . . , n, are the zeros of the polynomial p.
> This equality is known as the Orlando formula.

Their reference [73] is Orlando's original paper (next entry).

## [Or] Orlando's original paper

- L. Orlando, *Sul problema di Hurwitz relativo alle parti reali delle radici di un'equazione
  algebrica*, Math. Ann. **71** (1911) 233–245. doi:10.1007/BF01456650. The metadata was
  confirmed through Crossref.
- **Outstanding:** I did not retrieve the full text (it is behind the Springer paywall), so
  the formula is cited through [HT] Theorem 1.17, whose text was fetched.

## [Ba] Barkovsky: the Hurwitz matrix and the Hurwitz criterion

- Yu. S. Barkovsky, *Lectures on the Routh–Hurwitz problem*, transl. O. Holtz and
  M. Tyaglov, arXiv:0802.1805 (2008).
- Fetched: `https://arxiv.org/pdf/0802.1805` (43 pp., sha256 `da0e65cd…02c6`). The text layer
  drops some ligatures (for example "o e ien ts" for "coefficients"). They are restored below.

Eq. (34):

> Given a polynomial (8) with real coefficients, consider a corresponding n×n matrix of the
> following structure: Hp ≡ [ a1 a3 a5 a7 · · · ; a0 a2 a4 a6 · · · ; 0 a1 a3 a5 · · · ;
> 0 a0 a2 a4 · · · ; 0 0 a1 a3 · · · ; . . . ] (34) (the coefficients a0, . . ., an are not
> enough to fill the rows, but we set an+1 = an+2 = · · · = 0). The matrix Hp is called the
> Hurwitz matrix of the polynomial p. Let us denote by ηk the leading principal minor of this
> matrix formed from the first k rows and columns. […] ηn = ηn−1 an. (35)

Lemma 39 and Theorem 40:

> Lemma 39. In the regular case, h1 = η1, h2 = η2/η1, . . . , hn = ηn/ηn−1. (36)
> […] Theorem 40 (Hurwitz). A polynomial p(z) = a0 z^n + a1 z^{n−1} + · · · + an
> (a0, a1, . . ., an ∈ R; a0 > 0) (38) is stable if and only if all leading principal minors
> of its Hurwitz matrix Hp are positive: ηk > 0 (k = 1, 2, . . ., n). (39)

In Lemma 39 the h_k are the leading coefficients of the Routh/Euclid sequence f_0, f_1, … of
the even and odd parts. The Gaussian elimination pivots of the Hurwitz matrix are therefore
the ratios η_k/η_{k−1}.

## How these are used

- `audibility_common.hurwitz_matrix` implements (1.37) / (34) exactly.
- `orlando_check.py` verifies (1.41), with symbolic a0 and zeros, for n = 2..7, together with
  (35).
- `proof.md` uses Orlando's formula only for interpretation and to identify the determinant.
  The injectivity proof itself uses only the coprimality of the even and odd parts, which is
  proved directly there.
