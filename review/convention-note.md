# Convention note — what does `N(S)` count?

**One-line summary.** The manuscript never says whether a "two-coefficient degeneracy" is a *pair*
of colliding pillows or an *equivalence class* of pillows sharing a signature. Its printed numbers
follow the pair convention. The two definitions first disagree at **S = 136**, and by S = 600 they
differ by 90. Table 1 needs one clarifying clause; no number in it changes.

---

## The ambiguity

Section 5 defines

> `N(S) := #{two-coefficient degeneracies with cone-order sum S}`,  `𝒩(S) := Σ_{s≤S} N(s)`

and earlier defines a degeneracy as "a pair of distinct hyperbolic triples with equal `σ = (S₁, R)`".
The word *pair* appears in the prose, but the counting object is left implicit. When three or more
distinct triples share one signature value, the two readings diverge:

| Reading | Count for a signature class of `k` triples |
|---|---|
| **Pairs** — count colliding pairs | `C(k,2)` |
| **Classes** — count signature classes of size > 1 | `1` |

For `k = 2` these agree, which is why the ambiguity is invisible at small `S`.

## Where they diverge

`code/enumerate_degeneracies.py` computes both, keeps them distinct end to end, and writes both to
`data/degeneracies.csv` as `cum_pairs` and `cum_classes`.

| `S` | `𝒩_pairs` | `𝒩_classes` | difference |
|---:|---:|---:|---:|
| 100 | 92 | 92 | 0 |
| 135 | 161 | 161 | 0 |
| **136** | **168** | **166** | **2** |
| 200 | 386 | 380 | 6 |
| 300 | 840 | 822 | 18 |
| 400 | 1496 | 1468 | 28 |
| 500 | 2210 | 2158 | 52 |
| 600 | 3067 | 2977 | 90 |

**The first divergence is at `S = 136`**, where the first signature class of multiplicity three
appears:

> `R = 1/10` is shared by `O(15,55,66)`, `O(16,40,80)` and `O(17,34,85)`, all of cone-order sum 136.

That single class contributes `C(3,2) = 3` pairs but only `1` class, so the cumulative counts part
company by 2 and never re-converge. Two further multiplicity-3 classes appear below `S = 200`:

| `S` | `R` | triples |
|---:|---|---|
| 136 | `1/10` | `(15,55,66)`, `(16,40,80)`, `(17,34,85)` |
| 143 | `1/15` | `(33,55,55)`, `(35,45,63)`, `(39,39,65)` |
| 187 | `1/12` | `(17,68,102)`, `(18,52,117)`, `(22,33,132)` |

> **Correction to the original audit.** [claim-ledger.md](claim-ledger.md) recorded the divergence
> as beginning "from `S ≥ 200` onward". That was inferred from the seven printed checkpoints, which
> skip from 100 to 200. Sweeping every sum puts the true first divergence at `S = 136`. The
> checkpoint values themselves were correct and are unchanged.

## Which convention does the manuscript use?

**Pairs.** Table 1's printed values match `𝒩_pairs` at all seven checkpoints exactly, and match
`𝒩_classes` at only the first two. Verified independently three ways — this harness, the audit
oracle, and the checkpoint asserts in `enumerate_degeneracies.py`.

| `S` | printed in manuscript | `𝒩_pairs` | `𝒩_classes` |
|---:|---:|---:|---:|
| 18 | 1 | 1 | 1 |
| 100 | 92 | 92 | 92 |
| 200 | 386 | **386** | 380 |
| 300 | 840 | **840** | 822 |
| 400 | 1496 | **1496** | 1468 |
| 500 | 2210 | **2210** | 2158 |
| 600 | 3067 | **3067** | 2977 |

So the table is right. Only the definition is underspecified.

## The fix

**No number changes.** Add one clause to the definition of `N(S)` in Section 5, immediately after
the displayed Egyptian-fraction condition:

> `N(S) := #{two-coefficient degeneracies with cone-order sum S}`, where a degeneracy is counted
> once for each **unordered pair** of distinct triples sharing a signature; a signature shared by
> `k > 2` triples therefore contributes `C(k,2)`. The smallest such `k = 3` occurs at `S = 136`.

The final clause is optional but worth keeping: it tells a reader the distinction is real and not
vacuous, which is exactly the objection the clarification pre-empts.

### Consequences elsewhere in the manuscript — all benign

- **Theorem 5.2**, `𝒩(S) ≥ ⌊S/18⌋`, holds under both conventions (each scaled copy of the base pair
  is a class of size exactly 2). Verified for every `S ≤ 600`.
- **Conjecture 5.3**, `𝒩(S) ~ cS²`, is unaffected in form. The OLS exponent over `50 ≤ S ≤ 600` is
  **2.028** under pairs and **2.015** under classes — both round to the manuscript's stated 2.03 at
  two decimal places, so the empirical support does not depend on the choice.
- The constant `c` shifts slightly: at `S = 600`, `𝒩/S²` is `0.0085` under pairs and `0.0083` under
  classes. Both sit inside the manuscript's stated `0.0085`–`0.0093` band at the top of the range,
  though the classes figure is marginally below it. Stating the convention removes the ambiguity
  about which band is meant.

## Supporting artefacts

- `data/degeneracies.csv` — per-sum and cumulative counts under both conventions, plus a primitive-
  class count, for every `10 ≤ S ≤ 600`.
- `data/degeneracy-groups.csv` — every signature class with its multiplicity, pair count,
  primitive/scaled flag, content and base sum.
- `paper/tables/table1-both-conventions.tex` — a drop-in LaTeX table showing both columns side by
  side, should you prefer to publish the distinction rather than only state it.
