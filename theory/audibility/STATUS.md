# STATUS: audibility of the cone-order multiset

## Verdict

**PROVED FOR ALL n**

The map $\{m_1,\dots,m_n\}\mapsto(R,S_1,P_3,\dots,P_{2n-3})$ is injective on multisets of
positive reals, repeated orders included. Hence $K_{\rm mult}\le n$ for every genus-0
hyperbolic orbifold with $n$ cone points. This is Theorem A of `proof.md`.

The proof is elementary, and it holds over $\mathbb C$ whenever no two orders sum to zero, i.e.
whenever $\Delta_{n-1}=\prod_{i<j}(m_i+m_j)\neq0$ (Orlando). Positive orders always satisfy
this.

**Scope.**

- The step from heat coefficients to the invariants uses one imported analytic input: each cone
  term is $\tfrac1m\cdot$(an even polynomial with nonzero leading coefficient and root
  $m=1$). It comes from Uçar and Schueth, via `review/hyperresearch/Q2-cone-coefficients.md`, and
  is not re-derived here.
- The comparison is among orbifolds with at most $n$ cone points; order-1 padding handles fewer
  cone points. The case of orbifolds with more cone points is not covered (proof.md §2,
  Remark 3).

**H5 is also proved for all n** (Theorem B). The audibility system is linear in
$e_1,\dots,e_n$, and $\det M=c_n\Delta_{n-1}/e_n$ with $c_n\in\mathbb Q^\times$. The sign
$c_n=\pm1$ is computed only for $n\le8$.

## Sharpness ($K_{\rm mult}\ge n$: two orbifolds sharing the first $n-1$ coefficients)

| $n$ | over positive reals | over integer orders (orbifolds) |
|---|---|---|
| 2 | sharp (Thm C(2)) | — (no hyperbolic 2-cone sphere) |
| 3 | sharp | **sharp**: $\{2,8,8\}$ / $\{3,3,12\}$, re-verified exactly |
| 4 | sharp | **sharp**: $\{3,10,15,30\}$ / $\{4,5,21,28\}$, re-verified exactly |
| 5 | sharp | **open**: no witness with all orders $\le120$ (216,071,394 multisets, exhaustive, exact keys); none $\le60$ (7,028,847 multisets, 37 s) |
| $\ge6$ | sharp | **open**; not searched |

- Over the positive reals, every multiset of distinct orders sits on a curve of other
  multisets with the same first $n-1$ invariants, so $n-1$ invariants never suffice.
- Over the integers, sharpness at $n$ is equivalent to a nontrivial positive rational point on
  the pair variety, an odd-power Prouhet–Tarry–Escott system with a reciprocal condition
  (proof.md §4).
- A heuristic (Bombieri–Lang, not a proof) suggests integer witnesses become rare or absent for
  $n\ge4$. Whether integer sharpness holds for $n\ge5$ is unresolved.

## Planning hypotheses

| | verdict |
|---|---|
| H1 | confirmed |
| H2 | confirmed; the coefficient is $5\Delta_3/(S_1e_4)$, proportional to $\Delta_3$ with factor $45/e_4$ over $9S_1$; 38 positive terms |
| H3 | confirmed; $\operatorname{Res}_{e_5}=-9S_1^2L(e_3)$, lead $-945\Delta_4/e_5$; no spurious solutions |
| H4 | confirmed, with sign $+$, for $n\le8$ (Orlando, Holtz–Tyaglov Thm 1.17) |
| H5 | proved for all $n$ (Theorem B) |

## Reproduction

All scripts are exact (sympy, Fraction, integer keys), use real asserts, and exit nonzero on
failure. Run with `/opt/homebrew/Caskroom/miniforge/base/bin/python3` (sympy 1.14).
Transcripts are in `output/`.

| script | covers | time |
|---|---|---|
| `orlando_check.py` | Orlando, degrees 2–7 | ~20 s |
| `linear_system.py` | T3, $n=3..8$ | ~1 min |
| `verify_elimination.py` | H1–H4, Lemma 1, the Jacobian, $n=6..8$ | ~6–8 min |
| `sharpness_search.py [N]` | witnesses, $n=5$ search, cross-$n$ control | $N=60$: ~40 s; $N=120$: ~22 min |

Adversarial review is recorded in `attack-log.md`.
