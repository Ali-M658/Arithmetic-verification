# STATUS: the Prouhet–Tarry–Escott side of the signature problem

## Verdict

The gap in [Sig] Cor. N1, $\log_4A\lesssim f(A)\lesssim A$, is narrowed and reframed.

The logarithmic lower bound is replaced by a square-root bound, proved for all $A$
(Theorem 4.1):

$$f(A)\ge\Bigl\lfloor\sqrt{\tfrac13(A/2\pi-1)}\Bigr\rfloor+2\quad(A\ge8\pi).$$

The proof needs no Thue–Morse blocks. A pigeonhole pair with equal odd power sums is passed
through a "doubling" $U=X\uplus2Y\uplus2Y$, $V=Y\uplus2X\uplus2X$, which kills the reciprocal
condition. The same order $\sqrt A$ holds for the genus alone and for the cone count alone in
genus 0.

More importantly, the remaining gap is shown to be a *classical open problem*, not a weakness
of technique. For $0<\alpha\le1$, $f(A)\ge cA^\alpha$ holds iff the Prouhet–Tarry–Escott
minimal size satisfies $N(k)\le Ck^{1/\alpha}$ (Theorem 4.2). So:

- $f$ is linear iff $N(k)=O(k)$;
- any exponent above $\frac12$ would settle in strong form Borwein–Ingalls' open problem
  $N(k)=o(k^2)$; all known bounds on $N(k)$ are quadratic.

Explicit pairs verified with the actual cone coefficients improve the thresholds for
$L\le7$ by factors of 10 to 230. Sharing $L=3,\dots,7$ coefficients now happens already at
Area$/2\pi\approx1.47,\,5,\,7,\,10,\,18$, instead of $15,63,255,1023,4095$.

The smallest genus-changing collisions shrink from $2^{2L-1}$ points to $6,10,16,20,26,40$
for $L=2..7$. The least genus-0 pairs with different cone counts go from $103$ vs $104$ to
$7$ vs $8$ at $L=3$.

$T_3$ is **not** decided: $T_3\in\{8,10\}$. A size-8 collision must have shape $(3,5)$, and
none exists whose 5-element side, made primitive, has entries $\le220$. The search was rerun
with a certified filter after the adversarial review showed that the first filter could miss
clustered rational roots.

**The paper should stop presenting the growth of $f$ as a log-versus-linear gap.** It should
state the $\sqrt A$ lower bound together with the exact PTE equivalence (wording below).

## Answers to the brief

| item | result | where |
|---|---|---|
| $T_3$ | **open, $\{8,10\}$**. Shape $(3,5)$ forced. No witness whose 5-side, made primitive, has entries $\le220$: complete search, with every candidate verified exactly; floating point rejects only when certified, and a 53k-case planted control shows 0 false negatives. Real solutions abundant. Every structured family yields only balanced size-8 objects | proof.md §6, Thm 2.1, Prop 2.3 |
| best $T_4$ | **$\le16$** (was $\le128$) | witnesses.py |
| best $T_5$ | **$\le20$** (was $\le512$) | witnesses.py |
| $T_6$, $T_7$ | $\le26$, $\le40$ (were $2048$, $8192$) | witnesses.py |
| any pair, $\tau_L$ ($L=3..7$) | $8$ (ideal), $\le14$, $\le18$, $\le24$, $\le40$ | witnesses.py |
| cone count, genus 0 ($L=3..7$) | $7$ vs $8$; $11$ vs $12$; $22$ vs $23$; $29$ vs $30$; $35$ vs $36$ (were $103$ vs $104$ resp. $3\cdot2^{2L-3}-1$ vs $3\cdot2^{2L-3}$) | witnesses.py |
| general $T_L$ | $T_L\le4N(2L-3)\le8L^2$; $\tau_L\le6(L-1)^2+6$; $T^{\rm cone}_L\le6N(2L-3)$ | proof.md Thm 3.4 |
| $f(A)$ | $\ge\lfloor\sqrt{(A/2\pi-1)/3}\rfloor+2$; exponent equivalence with PTE | proof.md Thms 4.1–4.2 |
| new structure | Descartes bound $\lvert U^*\rvert+\lvert V^*\rvert\ge2L+2\lvert g-g'\rvert$; symmetric and pencil constructions are always balanced; pencil theorem (ideal balanced configurations = two full fibres of $\prod(x-a)/x^{d}$) | proof.md §§2–3 |
| side result | 61 integer sharpness witnesses for Theorem A at $n=4$ (the repo had 1). $n=5$: no pencil witness with entries $\le200$ | pencil_search.py, data/pencil_log.txt |

## Improved bound on $f(A)$, by range

| $f(A)\ge$ | 3 | 4 | 5 | 6 | 7 | 8 | $L+1$ in general |
|---|---|---|---|---|---|---|---|
| new: $A/2\pi\ge$ | $1/4$ | $22/15$ | $5$ | $7$ | $10$ | $18$ | $3(L-1)^2+1$ |
| [Sig] N1: $A/2\pi\ge$ | 3 | 15 | 63 | 255 | 1023 | 4095 | $4^{L-1}-1$ |

The values 5, 7, 10, 18 are rounded up from the exact areas in `data/witnesses.json`
(each is $n-2-R$ with tiny $R$). The upper bound $f(A)\le\lfloor A/\pi\rfloor+4$ is unchanged.

## Recommended wording for the paper

Replace Corollary `cor:siggrowth` and the open question after it by:

> **Corollary (growth).** For $A\ge8\pi$,
> $$\Bigl\lfloor\sqrt{\tfrac13\bigl(\tfrac{A}{2\pi}-1\bigr)}\Bigr\rfloor+2\le f(A)\le\Bigl\lfloor\frac A\pi\Bigr\rfloor+4 .$$
> Moreover, for $0<\alpha\le1$, $f(A)\ge cA^\alpha$ for all large $A$ if and only if
> $N(k)\le Ck^{1/\alpha}$ for all $k$. Here $N(k)$ is the least size of a non-trivial solution of
> degree $k$ of the Prouhet–Tarry–Escott problem. In particular $f(A)=\Theta(A)$ if and only if
> $N(k)=O(k)$.

and in the introduction:

> The number of heat coefficients needed to determine the signature grows at least like the
> square root of the area and at most linearly. Which of the two is the truth is equivalent to
> the growth of the minimal size in the Prouhet–Tarry–Escott problem. Linear growth holds iff
> $N(k)=O(k)$, and any exponent above $\frac12$ would settle in strong form the open question
> $N(k)=o(k^2)$ of Borwein and Ingalls.

Example `ex:siggenus` can gain the pair $(0;3,10,15,30)\sim(0;4,5,21,28)$, sharing three
coefficients at area $2\pi\cdot22/15$, and the cone-count pair
$(0;4,4,5,5,6,12,12)\sim(0;2,2,2,3,10,10,10,10)$. The LaTeX is in `statements.tex`.

## Deliverables and reproduction

Run from this directory with `/opt/homebrew/Caskroom/miniforge/base/bin/python3` (sympy 1.14).
Every script is exact, uses real asserts, exits nonzero on failure, and has its transcript in
`output/`.

| file | content | time |
|---|---|---|
| `proof.md` | theorems and proofs | |
| `statements.tex`, `references-pte.bib` | LaTeX fragments for the paper, bib entries from fetched metadata | |
| `LITERATURE.md`, `sources/` | literature with exact quotes (`sources/NOTES.md`) and fetched files | |
| `pte_common.py` | configurations, realisation, exact shared count via `../signatures/sig_common.py` | |
| `witnesses.py` | the 18 witness pairs of §5 → `data/witnesses.json`, `data/orbifold_pairs.md` | ~1 min |
| `genus_search.py`, `enum_sym6.c`, `enum_sym8.c` | the searches behind the $L=4,5$ genus witnesses → `data/genus_search_L*_log.txt` | ~20 / ~1 min |
| `structure.py` | Thm 2.1, Prop 2.3, Thm 3.1 weight lemma ($m\le10$), Props 3.2–3.3 | ~5 s |
| `growth.py` | Thm 4.1 vs Cor. N1 (exact, to $10^6$), Thm 3.4 instantiated $L=2..7$, thresholds | ~1 s |
| `pencil_search.py` | pencil points, $m=4$ ($\le130$; log to 220) and $m=5$ ($\le200$) → `data/pencil_*.json`, `data/pencil_log.txt` | ~5 min |
| `search_T3.sh`, `search_T3.c`, `search_T3_verify.py`, `search_T3_control.py` | complete $T_3=8$ search with certified floating-point rejection, exact verification of every candidate, planted positive control → `data/T3_search_log.txt` | ~2.5 h to 220; control ~5 min |
| `real_shapes.py` | real solvability by shape (floating point, illustrative only) | ~3 min |
| `attack-log.md`, `attack/` | independent adversarial checks (own code), and the response to each finding | |
