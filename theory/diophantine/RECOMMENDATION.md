# What the Diophantine section should contain

**Verdict in one paragraph.** Section 5's growth conjecture is contradicted
by the extended data and should be withdrawn. Its heuristic is miscounted
and its independence assumption fails. What replaces them is stronger:

- The equation is the elliptic pencil $(x+y+z)(xy+yz+zx)=\lambda xyz$. This
  is the $\Gamma^0_0(6)$ pencil of Beauville's list (his notation) and
  Bremner–Guy–Nowakowski's "Knight's problem" curve.
- Schinzel's D16 method adapts verbatim and gives fibres of every size.
- The minimal pair $\{(2,8,8),(3,3,12)\}$ provably never acquires a third
  member. This rests on an unconditional 2-descent bound,
  rank$(C_{27/2})\le0$ ([ranks.py](ranks.py)).
- A 2-torsion translation supplies an explicit two-parameter family. It
  lifts the lower bound from $\lfloor S/18\rfloor$ to
  $c\,S\log S$, with explicit $c$, and to $\gg S(\log S)^2$.
- The data support $\mathcal N(S)=S(\log S)^{\kappa+o(1)}$ with
  $\kappa=4.5\pm0.5$, not $cS^2$. No heuristic currently predicts $\kappa$:
  the Manin prediction for the dual family is not borne out in range (§1.2).

Keep a compact version in the spectral paper. The full counting and
geometry story is strong enough for a separate short note (§5 below).

Everything cited here is computed in this directory:
[enumerate_fast.py](enumerate_fast.py) (asserted against the existing
harness), [growth_fits.py](growth_fits.py), [families.py](families.py),
[variety_checks.py](variety_checks.py), [ranks.py](ranks.py),
[exponent_fits.py](exponent_fits.py), proofs in [variety.md](variety.md),
source-by-source novelty in [novelty.md](novelty.md),
and data in [data/](data/).

---

## 1. Evidence summary

### 1.1 Enumeration to S = 4800 (T1)

The run reproduces the existing harness exactly for every $S\le600$:
per-$S$ triads, pairs, classes, primitive classes, every class's $R$,
triples and content, and the committed `data/degeneracy-groups.csv` row for
row.

| $S$ | $\mathcal N_{\rm pairs}$ | $\mathcal N_{\rm classes}$ | primitive classes | $\mathcal N/S^2$ | largest fibre so far |
|---:|---:|---:|---:|---:|---:|
| 100 | 92 | 92 | 69 | 0.00920 | 2 |
| 200 | 386 | 380 | 243 | 0.00965 | 3 |
| 600 | 3067 | 2977 | 1714 | 0.00852 | 4 |
| 1000 | 7641 | 7386 | 4040 | 0.00764 | 4 |
| 2000 | 25042 | 24127 | 12210 | 0.00626 | 5 |
| 3000 | 48574 | 46755 | 22657 | 0.00540 | 5 |
| 4000 | 77203 | 74234 | 34721 | 0.00483 | 5 |
| 4800 | 102719 | 98742 | 45167 | 0.00446 | 6 |

**First fibres of each size**, i.e. $k$ pairwise non-isometric pillows
sharing $a_0$ and $a_1$:

| size | $S$ | example |
|---:|---:|---|
| 3 | 136 | (15,55,66), (16,40,80), (17,34,85) |
| 4 | 408 | the $S=136$ curve $\lambda=68/5$ plus one more point |
| 5 | 1849 | (168,820,861), (172,645,1032), (185,480,1184), (215,344,1290), (253,276,1320) |
| 6 | 4600 | (750,1750,2100), (756,1674,2170), (800,1400,2400), (805,1380,2415), (882,1170,2548), (920,1104,2576) |

No fibre of size 7 occurs up to 4800. The curves carrying the first fibres
of sizes 3, 4, 5, 6 have Mordell–Weil rank 2, 2, 3, 3, and $C_{155/12}$ has
rank 2. All are **PROVEN**, with the PARI lower and upper bounds equal; the
exact calls and full outputs are in [data/ranks.txt](data/ranks.txt). The
claim that every primitive size-5 class up to 4800 lies on a curve of rank
3 or 4 was not certified by that script and is not proposed.

### 1.2 Growth law (T2)

Out-of-sample relative error, from [data/growth_fits.txt](data/growth_fits.txt):

| model for $\mathcal N(S)$ | fit ≤1000 → RMS error on 1001–2000 | fit ≤2400 → RMS error on 2401–4800 |
|---|---:|---:|
| $cS^2$ (Conjecture 5.3) | 26.8% | 47.0% |
| $cS^2/\log S$ | 6.6% | 23.4% |
| $cS^a$ ($a=1.91$, then $1.81$) | 14.1% | 15.6% |
| $cS^2(1+d/\log S)$ | 16.3% | 23.4% |
| **$cS(\log S)^K$** ($K=5.35$, then $5.25$; see below) | **2.4%** | **2.8%** |
| $cS^a(\log S)^k$ | 0.7% | 0.25% |

The free-exponent fit $cS^a(\log S)^k$ settles on $a\approx0.84$, which is
impossible asymptotically: Theorem 4 gives $\mathcal N\gg S\log S$. It is
fitting secondary terms of a polynomial in $\log S$, not a genuine power.

- The local exponent $d\log\mathcal N/d\log S$ falls steadily: 2.07, 1.95,
  1.80, 1.72, 1.66, 1.60 over successive doublings from 100 to 4800.
- The per-$S$ count is not $\Theta(S)$. Its window mean over $S\in[4400,4800)$
  is $0.0071S$, against $0.0167S$ at $[200,600)$.
- The primitive share of classes falls from 0.60 at $S=500$ to 0.46 at
  $S=4800$. Under quadratic growth it would converge to $1/\zeta(2)=0.61$.

**The log-power, reconciled** ([exponent_fits.py](exponent_fits.py),
[data/exponent_fits.txt](data/exponent_fits.txt)). The earlier figures,
5.3 cumulative and 4.6 per-$S$, came from different models and do not
conflict. Both series were refitted with one model, $n(s)=c(\log s)^k$ per
sum. The cumulative fit uses the exact partial sums
$\sum_{s\le S}c(\log s)^k$, not a closed form. Same window, block-bootstrap
standard deviations:

| series ($600\le S\le4800$) | per-$S$ $k$ | cumulative $k$ | Manin prediction |
|---|---:|---:|---:|
| all pairs | 4.48 ± 0.44 | 4.56 ± 0.71 | — |
| primitive pairs | 3.54 ± 0.37 | 3.63 ± 0.57 | — |
| dual pairs (with scalings) | 3.33 ± 0.35 | 3.33 ± 0.60 | 5 |
| primitive dual pairs | 2.56 ± 0.34 | 2.52 ± 0.53 | 4 |
| non-dual pairs | 4.79 ± 0.47 | 4.91 ± 0.77 | — |

- **The two series agree**, at $k\approx4.5$ for all pairs.
- **The 5.3 was the closed form's bias.** The closed form
  $cS(\log S)^K$ absorbs the secondary term of
  $\sum_{s\le S}(\log s)^k=S(\log S)^k(1-k/\log S+\dots)$. Refitting it
  from $S=100$ gives $K=5.16$, against $k(1+1/\log S)=5.04$ predicted from
  $k=4.48$.
- **Scalings add one power of the logarithm**, as they must: primitive
  pairs fit 3.5 and all pairs 4.5.
- **The data and the Manin heuristic disagree in this range.** For the dual
  del Pezzo family the heuristic predicts $k=4$ for primitive pairs and $5$
  with scalings. The fits give $2.6\pm0.3$ and $3.3\pm0.4$, about four
  standard deviations low. The heuristic's convergence could simply be slow,
  but nothing here supports it. It is moved to the unverified list (§6).
- **The total is driven by the non-dual pairs** (84% of primitive pairs),
  whose $k\approx4.8$ has no heuristic at all.
- **The conjecture the data support:** $\mathcal N(S)=S^{1+o(1)}$, refined
  empirically to $S(\log S)^{\kappa+o(1)}$ with $\kappa=4.5\pm0.5$ on
  $600\le S\le4800$. The proven lower bound is $\kappa\ge2$ (Theorem 5).

**Birthday heuristic (§5.3).** Two faults, each fatal on its own.

1. *It miscounts the candidate values.* Rationals in $(0,1)$ with
   denominator $\le(S/3)^3$ number $\asymp S^6$, not $O(S^3)$. Even with the
   numerator bound $e_2\le S^2/3$ there are $\asymp S^5$. A uniform model
   then predicts $N(S)\to0$. The heuristic reaches "$\Theta(S)$" only through
   the miscount.
2. *Independence is false.* Conditional on its reduced denominator, a
   uniformly distributed $R$ would give $P_{\rm null}\approx1$–$2.5$ pairs per
   $S$, roughly constant. The actual counts exceed this by a factor that
   rises from 2 to 43 between $S=200$ and $4800$
   ([data/birthday.csv](data/birthday.csv)).

Collisions are structural (§1.3), not random.

### 1.3 Structure (T3, T4)

See [variety.md](variety.md) for proofs.

- $\lambda=e_1e_2/e_3=S\cdot R$ is scale-invariant. A degeneracy class is a
  set of positive rational points on one cubic $C_\lambda$. The scaling law
  is just "the same projective points".
- $C_\lambda$ is the member $t=1-\lambda$ of Beauville's $\Gamma^0_0(6)$ pencil
  $(X+Y)(Y+Z)(Z+X)+tXYZ=0$. The identity map is the change of variables,
  asserted in `variety_checks.py` §2.
  - Fibres $I_6,I_3,I_2,I_1$, computed (§3a), and generic torsion
    $\mathbf Z/6$.
  - It is a rational elliptic surface, so by Shioda–Tate there is no section
    of infinite order.
  - An explicit $\mathbf Q$-birational map to BGN's model and its inverse
    are asserted (§3c), so the PARI ranks are ranks of $C_\lambda$ itself,
    not of a twist.
- **Reciprocation $t\mapsto(1/p,1/q,1/r)$ is translation by the 2-torsion
  point $T_2=(0{:}0{:}1)$, exactly and with no permutation.** This is proved
  symbolically for every point of every $C_\lambda$ (§5). So
  every non-geometric triple $t=(a,b,c)$ has a partner:
  $\{e_2(t)\,t,\ e_1(t)\,(bc,ca,ab)\}$, with $S=e_1e_2$ and $R=1/e_3$. The
  base pair is $t=(1,4,4)$.
- These **dual pairs** are 33% of primitive pairs at $S\le200$ and 16.5% at
  $S\le4800$. The remainder differ by points of infinite order. None of
  the 1,330 non-dual primitive pairs with $S\le600$ differs by torsion.
- The dual locus is an anticanonical quartic del Pezzo surface of Picard
  rank 5 over $\mathbf Q$ (§6). The Manin count this suggests is not borne
  out in range (§1.2).
- The degeneracy cone is explicitly birational to the fibre square of the
  pencil over the $\lambda$-line, via
  $(P,P')\mapsto(e_1(P')P,\ e_1(P)P')$, asserted in §7. That fibre square
  is Schoen's construction for this surface. His Prop. 7.1(i) makes it a
  rigid Calabi–Yau, and its hypotheses (all fibres $I_n$, a self-product of
  a Table 1 surface) are checked above. The identification of its
  $L$-function is **not** verified (§6).
- **No linear families** (Proposition 2): any polynomial family other than
  scaling has degree $\ge2$. A systematic search over all pairs of lines in
  $\mathbf P^2$ with coefficients $|\cdot|\le7$ (189 lines up to
  permutation; these are the degree-2 families) finds exactly 18 families.
  They are the conics of the dual conic bundle, one for each coprime slope
  $q<r\le7$ plus the isosceles one. All of their 3,053 pairs with
  $S\le4800$ appear in the enumeration. No two distinct lines pair up: all
  189 branch-value discriminants are distinct.
  Nor are the non-dual pairs multiplication images: none of the 669 with
  $S\le400$ satisfies $Q=\pm mP+T$ or $P=\pm mQ+T$ with $m\in\{2,3\}$ and
  $T$ torsion. Their origin is the main open structural question. ([data/families.txt](data/families.txt),
  [data/line_families.csv](data/line_families.csv))

---

## 2. Recommended content of the section

Target length: 3–4 pages, subordinate to the spectral results. In order:

**5.1 Reformulation and positioning** (half a page).
- State Proposition 1: classes are rational points on
  $C_\lambda:(x+y+z)(xy+yz+zx)=\lambda xyz$, with $\lambda=SR$.
- Identify the pencil with the $\Gamma^0_0(6)$ row of Beauville's table and cite
  Bremner–Guy–Nowakowski (Math. Comp. 61 (1993) 117–130), who study
  $n=(x+y+z)(1/x+1/y+1/z)$ on this very curve.
- Position against Guy D16, equal sum and equal *product*, solved by Schinzel
  (Serdica Math. J. 22 (1996) 587–588) via the curve $x^3-9x+9=y^2$.
- Spell out the novelty: none of the fetched sources links pairs with equal
  $(S,R)$ to two points on one such curve.

**5.2 The dual family and the torsion picture** (one theorem, half a page).
- Reciprocation is a 2-torsion translation, which gives the explicit family
  above.
- Corollary: the base pair is the dual pair of $(1,4,4)$.
- Theorem (isolation): $C_{27/2}$ has rank 0 and torsion
  $\mathbf Z/2\times\mathbf Z/6$. So for every $k$ the class of
  $\{\mathcal O(2k,8k,8k),\mathcal O(3k,3k,12k)\}$ has exactly two members:
  the minimal degeneracy never extends to a triple.
- This is spectrally meaningful and pairs naturally with Theorem B. It rests
  on PARI's unconditional 2-descent upper bound, $r_2=0$ (PARI/GP 2.17.2,
  `ellrank` on the integral model $[0,393,0,3456,0]$). It also uses the
  explicit list of the 12 torsion points, two of them positive up to
  permutation. Both are in [ranks.py](ranks.py), and the PARI call should
  be quoted in the appendix.

**5.3 Lower bounds** (replace Theorem 5.2).
- Theorem 4: $\mathcal N(S)\ge(c_{\rm iso}+o(1))\,S\log S$ with
  $c_{\rm iso}=3\log2/(2\pi^2)$, in both conventions. The proof takes ten
  lines.
- Optionally state Theorem 5, $\mathcal N(S)\gg S(\log S)^2$, with the proof
  sketched or deferred.
- Keep Proposition 5.1 (scaling); it is used.
- Add Proposition 2 (no linear families) as a remark. It explains why no
  power gain over $S$ can come from a construction.

**5.4 Arbitrarily large fibres** (Schinzel's method).
- Theorem 3: for every $k$ there are $k$ pairwise non-isometric hyperbolic
  pillows sharing $a_0$ and $a_1$.
- Proof: a point of infinite order on $C_{155/12}$ (Mazur check), plus BGN's
  "odd multiples on the egg", plus the lcm rescaling.
- Spectral reading: two heat coefficients can fail to distinguish
  arbitrarily many pillows at once, while $P_3$ always separates them
  (Theorem C).
- Give the first-occurrence table of fibres of sizes 3–6.

**5.5 Data and the revised conjecture.** One table and one figure.
- Conjecture (revised): $\mathcal N(S)=S^{1+o(1)}$.
- Empirical refinement: $\mathcal N(S)=S(\log S)^{\kappa+o(1)}$ with
  $\kappa=4.5\pm0.5$. Per-$S$ and cumulative fits agree (§1.2).
- Proven floor: $\kappa\ge2$.
- Say plainly that no heuristic predicts $\kappa$. The Manin count for the
  dual family is not met in range, and the non-dual 84% are unexplained.

**The figure.** Two panels sharing the axis $S\in[100,4800]$.
- Left: $\mathcal N(S)/S^2$, which falls monotonically, overlaid with
  $\mathcal N(S)/(S(\log S)^{4.5})$, which levels.
- Right: the local exponent over doubling windows, with the reference lines
  1 and 2 marked.
- All series are columns of [data/per_S.csv](data/per_S.csv).

## 3. What to cut or correct

- **Conjecture 5.3 ($\mathcal N\sim cS^2$) and its "equivalently
  $N(S)=\Theta(S)$" clause.** Both are contradicted by the data (§1.2).
  Withdraw them; do not soften them.
- **The §5.3 birthday heuristic.** It rests on the $O(S^3)$ miscount, and
  its independence premise is falsified. Replace it with the structural
  structural facts: collisions sit on common curves $C_\lambda$, and
  every triple has its 2-torsion partner.
- **The abstract's "$c\approx0.0085$–$0.0093$"** and every sentence
  presenting $\mathcal N/S^2$ as stabilising. Table 5.1 itself can stay as
  data, extended and recaptioned.
- **"Density at least 1/18 among cone-order sums" and "a positive
  proportion, of order $1/S$, of hyperbolic triads".** The first is
  superseded by Theorem 4. The second is unsupported.
- **"Of the birthday-paradox type standard in analogous Diophantine
  settings".** No such precedent exists (review/hyperresearch/Q1).
- **The Erdős–Straus framing in "Further directions".** The right
  neighbours are D16/Schinzel, Bremner–Guy–Nowakowski, and rational points
  on the Schoen threefold.
- State the counting convention (pairs) in the definition of $N(S)$, as
  `review/convention-note.md` recommends. Theorem 4 holds in both
  conventions; Theorem 5 is stated for pairs.

## 4. Citations needed (all verified this session unless noted)

| reference | status |
|---|---|
| Schinzel, Serdica Math. J. 22 (1996) 587–588 | fetched, read; no DOI exists |
| Bremner, Guy, Nowakowski, Math. Comp. 61 (1993) 117–130, DOI 10.1090/s0025-5718-1993-1189516-5 | fetched, read |
| Beauville, C. R. Acad. Sci. Paris Sér. I 294 (1982) 657–660 | fetched (Gallica scans); no DOI |
| Schoen, Math. Z. 197 (1988) 177–199, DOI 10.1007/bf01215188 | fetched, read (Prop. 7.1, Table 1) |
| Guy, *UPINT* 3rd ed., §D16 | **text not re-retrieved**; chapter DOI 10.1007/978-0-387-26677-0_5; see review/outstanding-fetches.md §1.4 |
| Verrill, JNT 81 (2000) | **unretrieved**; only needed if the modularity remark is kept (§1.5) |
| Mazur, Publ. Math. IHÉS 47 (1977) 33–186, DOI 10.1007/bf02684339 | full text fetched (Numdam); Theorem (8) p. 35, Corollary (5.2) p. 156 |
| Shioda, Comment. Math. Univ. St. Pauli 39 (1990), no. 2, 211–240 (Zbl 0725.14017) | zbMATH record and review only; text unretrieved; supports a non-load-bearing remark (outstanding-fetches §1.7) |
| PARI/GP 2.17.2 manual, `ellrank` | fetched; documents $r_1\le\mathrm{rank}\le r_2$ with $r_2=C-T-s$ unconditional |

## 5. Is there a separate paper here?

**Yes: a short number-theory note.** The core would be "Triples with equal
sum and equal reciprocal sum", taking Theorems 3–5 together with:

- the isolation theorem;
- the del Pezzo/Calabi–Yau picture, and the empirical law
  $\mathcal N(X)=X(\log X)^{4.5\pm0.5}$ from the $S=4800$ data.

That stands on its own as the exact $(e_1,e_2/e_3)$ analogue of Guy D16.
It also has a natural next step that the spectral paper cannot absorb:
- deciding whether the dual family really has the Manin exponent its
  geometry suggests, given that the data fall short;
- explaining the non-dual 84%.

**Recommended split.** The spectral paper keeps §§5.1, 5.2 (isolation),
5.3 (Theorem 4 only), 5.4 and 5.5 in compressed form, about 3 pages, and
cites the note for Theorem 5, the del Pezzo analysis and the fits. If only
one paper is wanted, the material above fits as the single section
described in §2. Nothing in it is weaker than what it replaces.

## 6. Unverified remarks: not proposed for the paper

- **Manin's prediction for the dual del Pezzo surface,** $\asymp X(\log X)^4$
  primitive dual pairs. The surface's structure (anticanonical dP4, Picard
  rank 5) is verified. The count is a conjecture applied to an open real
  subset, and the data disagree in range (§1.2).
- **The $L$-function of the Schoen threefold.** The weight-4 eta product and
  its level come from Livné–Yui's table and our inference. Verrill's paper
  is unretrieved.
- **That the pencil's monodromy group is $\Gamma_1(6)$.** Beauville's table
  prints the group as $\Gamma^0_0(6)$, and Livné–Yui list the same
  configuration under $\Gamma_1(6)$. We verified only the equation and the
  fibre types, so the paper should name the pencil by its equation and by
  Beauville's table row.
- **The rank pattern of size-5 fibres** beyond the curves in
  [data/ranks.txt](data/ranks.txt).
