# Attack log: curvature comparison

## Protocol

A separate reviewer received only `proof.md` and re-fetched the cited literature headlessly:
Kokotov, DGGW, Uçar, Thurston ch. 13. The reviewer had no scripts, outputs or `sources.md`, and
was asked to break every statement, numerically included. All of the reviewer's arithmetic was
exact unless noted.

- **Lemma 2.** Tested three ways for $C_5,C_7,D_2,D_5,D_6,T,O,I$:
  - the Molien series ($\ell\le80$);
  - the character average ($\ell\le80$);
  - direct linear algebra on harmonic polynomials ($\ell\le12$).
- **Spherical expansion.** Against Uçar at $K=+1$ ($\ell\le12$, $m\le30$), and against a
  50-digit numerical trace.
- **Classification.** Enumerated with orders up to 200.
- **Injectivity of $a_0$.** Tested for $n\le10^5$, including bad orbifolds.
- **Part 4.** Checked.
- **Hyperbolic.** An $n=5$ witness search (orders $\le66$), and a search with unnormalised $K$.

## Findings and responses

| # | severity | finding | response |
|---|---|---|---|
| F1–F6 | NONE-CONFIRMED | Lemma 2 (three methods); spherical expansion = Uçar at $K=+1$, with full-trace residuals shrinking like $t^{13}$; classifications; $a_0$ injective (also on the union with bad orbifolds); sharpness and both hyperbolic witnesses; Part 4, including Kokotov's hypotheses and the explicit pair. Citations and page numbers checked | — |
| F7 | **SERIOUS** | §5 claimed that in negative curvature "the number of coefficients needed grows with the number of cone points". Only $K_{\rm mult}\le n$ is proved for integers, with equality for $n=3,4$. No $n=5$ witness was found with orders $\le66$ (2,581 pairs agree on $\sum m,\sum m^3,\sum m^5$ but not on $\sum1/m$) | **Fixed.** §5 and `STATUS.md` now state: $K_{\rm mult}\le n$; $=n$ for $n=3,4$; non-decreasing (pad a witness with common cones), hence $\ge4$ for $n\ge4$; $n-1$ never suffices over real orders; integer growth open. The closing comparison is reworded so that it claims only what is proved |
| F8 | MINOR | "$n$ amplified numbers": only the $n-2$ coefficients $t^1,\dots,t^{n-2}$ carry $K^\ell$ | **Fixed** in §0 and the §5 table |
| F9 | MINOR | "In non-negative curvature two always suffice … nothing left to hear" contradicts Part 4 | **Fixed.** Restricted to orbifolds, with the flat cone surface exception stated |
| F10 | MINOR | "$\chi\ge0$ caps $n$" is the wrong reason: hyperbolic triads also have $n=3$ and collide at $t^{-1},t^0$ | **Fixed.** The reason is now the finite list plus one-integer families together with the fractional-part separation. The triad counterexample is quoted in §0 |
| F11 | MINOR | "Holds whether or not $K$ is normalised" does not cover Part 3 | **Fixed.** Restricted to Parts 1, 2, 4. Part 3 is stated at $K=-1$, with no claim for free $K$ |
| F12 | MINOR | The Strength statement mischaracterised DGGW 5.15 (it is entirely orientable and strictly stronger) and overstated what is new; DGGW Prop. 5.22 and Uçar Cor. 4.21(iv) were not credited for Part 2 | **Fixed.** Strength paragraph rewritten. New content is limited to the independent spectral derivation, the side-by-side count, and Part 4 |
| F13 | MINOR | The "curvature as gain" contrast was not credited to Uçar (polygons, printed pp. 97–100) | **Fixed.** Credited in §0 and `STATUS.md`. The quotes were re-checked in the PDF (printed p. 97: "at most three nonvanishing heat invariants"; p. 99) |
| F14 | MINOR | Applying Kokotov to orbifolds needs the Friedrichs extension to be the orbifold Laplacian | **Fixed.** One-line justification added (§2) |
| F15 | MINOR | Torus vs Klein bottle: DGGW Table 1 shows only $O(t)$, so full agreement needs flatness. Uçar 4.21 says "spectrum", and his p. 140 supports "heat invariants" | **Fixed.** Both are made explicit, and p. 140 is quoted in `sources.md` |
| F16 | MINOR | F3 is vacuous (the $K^\ell$ prefactor); "two-dimensional shape-and-scale space plus scale" is garbled | **Fixed.** F3 is labelled a bookkeeping check, and the parameter count now reads "two shape parameters plus scale" |

## Verdict after revision

The one serious defect was an overclaim in the interpretive section, not in any proof, and it
is removed. The mathematics (Parts 1–4 and Lemma 2) was confirmed independently.
