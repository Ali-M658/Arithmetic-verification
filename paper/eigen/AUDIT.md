# AUDIT: blind statements-only checks of the eigen manuscript (2026-10-08)

Every result whose proof is new or changed in the split (round-3 items B1, B2, I2, I5, I6) was checked
by two subagents given only `statements.tex`: the manuscript with every proof removed (the
derivations after the Rayleigh identity and of the trace identities removed as well). They were told
not to open `paper/eigen/`, `paper/` or `theory/`, worked in the session scratch directory, and wrote
their own code (Python, mpmath at 30-80 digits, exact fractions, sympy). Their scripts are not
committed. The earlier audit of the wave-2 fragments is `theory/eigen/AUDIT.md`.

## Check 1: geometry (Section 4, Section 8)

| statement | verdict | evidence |
|---|---|---|
| Lemma 4.1, (H1)-(H3) | TRUE | own proofs; 1000 random displacement cases (error 2e-12); 20,000 random hyperboloid configurations for (H3): side of intersection, cos theta = X, ultraparallel distance |
| Lemma 8.1 (Jorgensen, hyperbolic case) | TRUE | hypotheses sufficient (they make the group non-elementary); an elliptic B of order >= 3 is covered; the no-parabolics hypothesis is not needed but harmless |
| trace identities after Lemma 8.1 | TRUE | 1000 random (L, r, phi), all sign choices of lifts, error 5e-10 |
| Proposition 8.2 (O(2,3,m)) | TRUE | sigma_* = 0.5620668711; side lengths; systoles by word enumeration: 0.98399 (m = 7), 1.266, 1.534, 1.835, 1.925 (m = 1000), all >= sigma_* |
| Lemmas 4.2, 4.3, Theorem 4.4 | TRUE | brute-force minimum distances of elliptic points above d_0; Tables 1 and 2 (D column) reproduced |
| identity (5) (Rayleigh) | TRUE | sympy |
| Propositions 8.3, 8.5, Remark 8.4, the quadrilateral Q_{k,b} | TRUE with one correction | see below |

## Check 2: analysis and constants (Sections 2, 3, 5, 6, 7)

| statement | verdict | evidence |
|---|---|---|
| Lemma 2.4 (Phi_m) | TRUE | closed form to 1e-39; bounds for k < 16, m < 60 |
| definitions, signs, alpha_0..alpha_3 | TRUE | exact values |
| Lemma 2.5 (moments) | TRUE | quadrature to 1e-39 |
| Propositions 2.6, 2.7 (enveloping remainders) | TRUE | m in {2,3,7,12}, K <= 9, t from 1e-4 to 2: no violation, ratio up to 0.99995 |
| Lemma 2.8, Lemmas 3.1-3.2, 3.5, Theorems 3.3, 3.4 | TRUE | exhaustive over all signatures with orders <= M, M = 3..7 (up to 4103 equal-area pairs per M): no failure of k <= min(floor(A/pi)+4, M), of the formula for d_k, or of Theorem 3.4 |
| Lemma 6.1, Theorem 6.2 | TRUE | the chain B_* <= Gamma/8, tail = Gamma_*/8, perturbation <= Gamma_*/8 verified; all eight rows of Table 2 and all of Table 1 reproduced, with the binding constraint; "about 4e18" without the bounded-order theorem reproduced (4.19e18); N grows by about 9 per halving of epsilon |
| Theorem 7.1 (certificate) | TRUE with corrections | see below |
| Lemma 5.1, Proposition 5.2 | TRUE | |

## Corrections made

1. **Theorem 7.1.** The bound B(l, Delta, s) of Lemma 2.3 is proved only for s <= l^2/(2(1+l)) (and is
   even negative beyond s = l), while the certificate is applied up to t = 1 with systoles down to
   0.694. The statement now defines H(s) as B on that range and as the all-time bound of Lemma 2.3
   otherwise. The code (`theory/eigen/practice.py`, function `hypB`) already did exactly this, so no
   computed count changes. Also: the minimum is over 0 < s <= t, and the "in particular" clause now
   requires that sigma itself pass the test.
2. **The quadrilateral Q_{k,b}** (before Proposition 8.5): the vectors written as normals were not
   normals in the stated Minkowski form (one was the foot point). They are now
   (sinh b, cosh b, 0) and (sinh a, 0, cosh a), with inner product -sinh a sinh b; checked to be unit
   vectors orthogonal to the foot points and the side tangents. The conclusion is unchanged.
3. **Proposition 8.2**: "the open ball" of radius h_m (the closed ball touches the cone point of
   order 2).

Not changed: the remark that Lemma 8.1 holds without the no-parabolics hypothesis (the weaker lemma is
all that is used); the observation that the constants of Theorem 6.2 are far from tight (the paper
says so).
