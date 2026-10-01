# Adversarial review (T4)

## Protocol

A separate reviewer was given two files and nothing else:

- `proof.md` §§1–4, which hold the setting, heat input, lemmas, Theorems S, T1 and N, and
  Corollaries S1, S2 and N1. An appendix carried the two cited genus-0 results with their proofs:
  Lemma 1 and Theorem A of `theory/audibility/proof.md`.
- `statements.tex`.

The reviewer saw no scripts, no data, no transcripts, no search results, no repository and no
earlier reasoning. It worked in an isolated scratch directory and was barred from the repository.

**Instructions.** Assume the author is wrong. Check every step line by line. Run independent
*exact* counterexample searches using the actual cone coefficients $b_l$, recomputed from Uçar
(4.25)+(4.33) and not from the author's reduction. Grade each finding FATAL, SERIOUS, MINOR or
NONE.

## Findings and responses

The reviewer found **no fatal or serious error and no counterexample**.

| # | severity | finding | response |
|---|---|---|---|
| 1 | MINOR (a false sentence) | "Theorem S holds verbatim for positive real orders" fails if an order equals 1. $(0;1,2,3,7)$ and $(0;2,3,7)$ have equal heat data, with $U^*=V^*=\emptyset$. | **Fixed.** Now "positive real orders different from 1", with this example given as the reason. Integer orders are $\ge2$ by definition, so no theorem is affected. |
| 2 | MINOR | `statements.tex`: a cone point "contributes $k^{-1}p_l(k)$"; at $K=-1$ it is $(-1)^lk^{-1}p_l(k)$. | **Fixed.** |
| 3 | MINOR | $\phi_1$ is undefined; "T2(b)" is internal jargon; $K$ means both the curvature and the Prouhet exponent. | **Fixed.** $\phi_l:=p_l/x$ is defined in Lemma 2, the jargon is removed, and the Prouhet exponent is renamed $D$. |
| 4 | MINOR | `rem:sigK` calls $K_{\rm mult}(\mathcal O;\mathcal P_n)\le n$ "left open", but Theorem A proves it. | **Fixed.** It is now "left conditional in `rem:nconerestated`(a), now proved independently (Theorem A)". |
| 5 | MINOR | `thm:sigsep` does not introduce $n,n',g,g'$, and "the paddings of Lemma sigdata" is ambiguous, since (ii) only asserts that paddings exist. | **Fixed.** The signatures are now named in the statement, with "any paddings as in (ii)". The text notes that $U^*,V^*$ do not depend on the choice: two choices differ only by common 1s. |

**Checked line by line with no issue:**

- Lemmas 1–5 and the padding bookkeeping: the sign of $d$, $|V|-|U|=2(g-g')$, and (4.3).
- In Theorem S: the parity of $T$ and the coverage of every odd $j\le T-1$.
- S1, and S2 including $n+4g\le A/\pi+4$ and the floor.
- T1.
- Prouhet's identity and the positivity integral.
- N(a)–(c), including hyperbolicity, the area bound and the Egyptian-fraction step.
- N1.

## The reviewer's independent searches

All are exact and use the actual $b_l$.

- **Theorems S, S1 and S2.** The reviewer enumerated 3,760,795 signatures with $g\le3$, up to 7
  cone points, and orders up to 300 for a single cone point.
  - Equal-area pairs sharing exactly 1, 2 and 3 coefficients: 5,302,125, 54,454 and 77.
  - **No violation.**
  - The bound $|U^*|+|V^*|\ge2L+2$ is attained, e.g. $(0;3,10,15,30)$ vs $(0;4,5,21,28)$ share 3
    with $T=8$.
  - No pair of different genera, and no genus-0 pair with different cone counts, shares more
    than 2. This agrees independently with `genus.py` (C) and `cone_count.py` (c).
- **N(a)**, rebuilt from the text for $L=2,\dots,5$ and $g'=0,1,2$. Each pair shares exactly
  $L$ coefficients, is hyperbolic, and meets the area bound. For $L=2$ it is
  $(1;2,14,35)$ vs $(0;6,7,7,10,21)$, as in `genus.py`.
- **N(b)**, rebuilt for $k=2,3$. The pairs have 9 vs 10 and 103 vs 104 cone points and share
  exactly 2 and 3, as in `cone_count.py`.
- **Examples in `statements.tex`.** $(1;15)/(0;3,3,5,5)$ shares exactly 2;
  $(1;15,15,15)/(0;3,3,5,7,7,21)$ shares exactly 3.
- **Real orders other than 1** (half-integers, 17,287 signatures): no violation of Theorem S.

The reviewer's code stayed in the session scratch directory and is not part of the repository.
Its results are recorded here only as the reviewer reported them.
