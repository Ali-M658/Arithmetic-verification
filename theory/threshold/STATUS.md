# STATUS: closed-form threshold for adjacent least-order strata

## Verdict

**PROVED FOR ALL p** (`proof.md`, Theorem 1 and Corollary 2).

The strata of least orders $p$ and $p+1$ first overlap at
$$S^*(p)=18,\ 19\ (p=2,3);\qquad 3p+8\ (4\le p\le8);\qquad 3p+7\ (p\ge9),$$
and they overlap at every larger sum.

- **Even parity.** The threshold is the root
  $x^*(p)=3p(p+1)/(p-1)=3p+6+\frac6{p-1}$ of a quadratic with discriminant $4(2p+1)^2$.
- **Odd parity.** The gap at $3p+7$ is $-2(p^2-5p-30)/(p(p+1)(p+3)(p+4)(p+5))$, which changes
  sign between $p=8$ and $p=9$.

**No collision below 18, for every p.** $x^*(p)-18=3(p-2)(p-3)/(p-1)\ge0$, together with the
chain argument. This replaces the case list in the proof of Theorem `thm:separation` by one
inequality valid for all $p$.

## First overlap versus first collision (exact enumeration, S ≤ 600)

- The first collision equals $S^*(p)$ only for $p=2$ ($S=18$, $(2,8,8)/(3,3,12)$) and $p=4$
  ($S=20$, $(4,8,8)/(5,5,10)$). These are exactly the tangencies, where the balanced end of one
  stratum equals the spread end of the next.
- Proved for all $p$: a tangency requires $(p-1)\mid6$ and $x^*(p)\equiv p$ (mod 2).
- For $p\ne2,4$ the first collision lies strictly after $S^*(p)$:
  - proved for $p\ge9$ (one triad per stratum in the window at $S^*$);
  - checked directly for $p\le8$.
- Apart from the two tangencies, observed gaps range from 8 to 455 sums (maximum at $p=33$). Only 50 of the 198 adjacent
  pairs that coexist below 600 collide by 600; the rest are censored.
- No closed form for the first collision is claimed.

## Files

| file | content |
|---|---|
| `proof.md` | statements, proofs, physical reading |
| `threshold.py` | exact verification (sympy and `Fraction`); asserts C1–C6 and Proposition 3 |
| `threshold_output.txt` | run output (`ALL ASSERTS PASSED`) |
| `first_overlap_vs_collision.csv` | per $p$: $x^*$, $S^*$, first collision, gap, window counts, colliding pair |
| `attack-log.md` | independent adversarial review and responses |

Run with `/opt/homebrew/Caskroom/miniforge/base/bin/python3 threshold.py` (about 40 s).

## Cross-checks

- Brute-force stratum endpoints from all hyperbolic triads agree with the formulas for all
  58,705 adjacent $(S,p)$ pairs with $S\le600$.
- The collision fibres agree exactly with `theory/diophantine/data/groups.csv` (2,977 fibres,
  $S\le600$). That file was read only, never written.

## Scope

- Interval overlap is defined on hyperbolic triads. Stratum 2 is truncated by $R<1$, and this
  is handled in Lemma 1.
- The manuscript is not modified. Theorems `thmA`/`thmB` and `thm:separation` are re-proved
  here, not changed.
