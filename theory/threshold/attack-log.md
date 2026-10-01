# Attack log: closed-form threshold

## Protocol

A separate reviewer received only `proof.md`, plus the statements of `lem:chamber`, `lem:bound`
and `thm:separation` from `paper/main.tex`. The reviewer had no scripts, outputs or data, and
was asked to break every statement, numerically included.

The reviewer wrote independent code (sympy and exact rationals):

- a symbolic re-derivation of every identity;
- a scan of the closed form against exact gaps for $2\le p<5000$;
- an independent enumeration of all 5,924,649 hyperbolic triads with $S\le600$, run twice,
  checking monotonicity within strata, true endpoints, true overlap (with the truncated $p=2$
  stratum), all collision fibres and every number in §5.

## Findings and responses

| # | severity | finding | response |
|---|---|---|---|
| F1–F4, F9, F11–F13, F17 | NONE-CONFIRMED | Algebra (factorisation, discriminant $4(2p+1)^2$, odd-parity identity, $\varphi_p'$ numerator, gap at $3p+7$); closed form for $2\le p<5000$; overlap $\iff S\ge S^*$ on all 58,705 coexisting pairs $S\le600$; zero gap only at $(2,18),(4,20)$; Lemma 2 and Corollary 2 (no collision $S\le17$, exactly one at 18, none within a stratum); Proposition 3; every cell of the §5 table; 2,977 fibres, 198/50 pairs, first non-adjacent collision at 35 | — |
| F5 | MINOR | The $p\le8$ step relied on gaps at $S^*+1$ that were checked but not displayed, while §6 claims "proved for all $p$" | **Fixed.** The seven fractions $-\frac7{936},\dots,-\frac{17}{4680}$ are displayed in Theorem 1(d) and asserted in `threshold.py`. Proposition 3(1) for odd $D$, $p\le8$, now follows from them by monotonicity, with no "checked directly" |
| F6 | MINOR | False sentence: strata are not all nonempty for $S\ge3p$ ($(6..10,2)$ and $(9,3)$ are empty); $R^-_{S,2}$ is not attained for $S\le10$ | **Fixed.** §1 now states nonemptiness correctly and handles the formal cases $(2,9),(2,10)$, where the gap is positive |
| F7 | MINOR | Lemma 1 and Theorem 1(a) cross-references read as circular | **Fixed.** Lemma 1 cites the sign of the gap (Theorem 1(a),(b)), and (a) now concludes "gap ≤ 0 iff $S\ge x^*$", then invokes Lemma 1 |
| F8 | MINOR | "negative at $p=8$" should be "negative for $2\le p\le8$" | **Fixed** |
| F10 | MINOR | "reproves thmA/thmB without any case list" overclaims; $S=18$ uses $\operatorname{gap}_3(18)=\frac1{840}$ | **Fixed.** The text now says $S\le17$ is case-free and $S=18$ uses that one comparison |
| F14 | MINOR | Gap range "8 to 349" covered only the displayed rows; the true range among colliding pairs is 8–455 ($p=33$); 148 pairs are censored at 600 | **Fixed** in `proof.md` and `STATUS.md`. Asserted in `threshold.py`: 50 pairs, gaps $\{0,0,8,\dots,455\}$, the zeros being the tangencies |
| F15 | MINOR | "A collision there would need a tangency" is false for $p\in\{3,6,7,8\}$ (window 2+1) | **Fixed.** Restricted to $p\notin\{3,6,7,8\}$; those four are excluded by the direct check already in Proposition 3(2) |
| F16 | MINOR | "denominators $\asymp S^3$" is wrong; first collisions have tiny denominators (42, 30, 3542) | **Fixed.** Replaced by the observation that coincidences occur through shared small denominators |

## Verdict after revision

No fatal or serious defects were found. All minor defects are fixed, and the script re-run
passes (`threshold_output.txt`, `ALL ASSERTS PASSED`).
