# round1-fixes: computations and records behind the referee-round-1 revision

The revision itself is described in `paper/jga/ROUND1-CHANGES.md`. This folder holds what that
file cites. Each script runs from the repository root in the pinned environment
(`.venv/bin/python review/round1-fixes/<script>.py`), exits nonzero on any disagreement, and is a
stage of `code/run_all.sh --quick` (its stdout must equal the committed transcript in `output/`,
and the CSV files it rewrites must come back byte-identical).

| script | item | result | outputs |
|---|---|---|---|
| `a1_fig2_kmult.py` | A1 (reviewer d, m1): the dots of Fig. 2 | The 525 area values are exactly those $s\le7/5$ attained with genus $\le2$ (in effect $\le1$), at most 4 cone points, orders $\le12$. Each complete area class (no bound on the orders, exact Egyptian-fraction enumeration; 33,946 signatures, largest order 4,064,891,292) gives the committed class size and the committed largest $K_{\rm mult}$, $K_n$, $K_g$. **No value changes.** | `output/a1_fig2_kmult.txt`, `.csv` |
| `d1_pencil_counts.py` | D1 (reviewers b m9, c m6, d m6a): Remark 3.2 | With pencil splittings defined as in the revised Remark 3.2 and all entries bounded: 17 witnesses (14 primitive) at 130, 49 (30 primitive) at 220. | `output/d1_pencil_counts.txt`, `d1_pencil_N130.csv`, `d1_pencil_N220.csv` |
| `d2_explicit_pairs.py` | D2 (reviewer d m6b): Example 3.12 and the Fig. 2 diamonds and squares | All 23 pairs (18 from `theory/pte/data/witnesses.json`, 5 Prouhet pairs rebuilt from their closed form) have equal area and share exactly $L$ heat invariants; writes Table S1 of the supplement (`--check` tests that it is current) and checks the partner of $\{1,1,1,1,7\}$ in Remark 3.13. | `output/d2_explicit_pairs.txt`, `d2_pairs.csv` |

`a1_fig2_kmult.py` imports nothing from `theory/` or `figures/`: it builds the cone polynomials
$p_l$ from Bernoulli numbers (eqs. (4)-(5) of the paper, checked against eq. (7)) and counts
shared invariants twice, from the coefficients $b_l$ and from the power sums $\Psi_k$
(Lemma 2.10); `d2_explicit_pairs.py` reuses that code.

## A2: the sign of $d$ in Lemma 3.3 (reviewers b m3, c m3, d m4)

Verdict: correct as printed, no change. The source line is

    Then $d=R(m')-R(m)=2(g'-g)+n'-n\in\Z$, ...

and equal areas, $2g+n-R(m)=2g'+n'-R(m')$, give exactly that. Reviewers (b), (c), (d) read text
extracted from the PDF, which drops the primes; reviewer (a) and `review/referee-round-1/VERDICT.md`
read the rendered page and found it correct.

## citations/

The fetched records behind items C1-C3 and V12-V13, with a table of what each shows: see
`citations/README.md`.
