# P6. Priority claim: decision and manuscript wording

Evidence, verbatim quotes, search log and exact checks are in `literature/PRIORITY-notes.md`,
`literature/check_priority.py` (output `literature/check_priority.txt`) and `literature/fetches.md`.

## Verdict

| claim | verdict |
|---|---|
| "first exact finite-coefficient determinacy threshold, with an explicit minimal degeneracy, for a family of hyperbolic cone orbifolds" (main.tex, §Locating the novelty (b)) | **SURVIVES**, keep "to our knowledge"; add DGGW Rem. 5.16 |
| "none of it counts coefficients or exhibits a sharp finite boundary" (§(a)) | **FALSE as written; must be replaced** |
| an unqualified "first finite, explicit coefficient count for hyperbolic orbifolds" | **MUST BE NARROWED** to the uniform count over a whole hyperbolic class |

## What the two named sources prove

**DGGW, Thm 5.15** (arXiv:0805.3148 p. 29; Michigan Math. J. 56 (2008) p. 232):
"Let C be the class consisting of all closed orientable 2-orbifolds with χ(O) ≥ 0. The spectral
invariant c is a complete topological invariant within C and moreover, it distinguishes the
elements of C from smooth oriented closed surfaces." Here c = 2χ(O) + Σ(m_i − 1/m_i) is 12 times
the t⁰ coefficient (5.13). This is an explicit **one-coefficient** determination, metric-free, for
χ ≥ 0 (good or bad). It does **not** cover hyperbolic orbifolds. DGGW Rem. 5.16 (p. 31) says of
hyperbolic triangular pillows: "The invariant c does not seem sufficiently strong to distinguish
among these triangular pillows", and defers to the full spectrum (Dryden–Strohmaier).
DGGW Prop. 5.20 (curvature sign from the t-coefficient) and Prop. 5.22 (spherical orbifolds
determined by finitely many terms) are further finite-coefficient results, all non-hyperbolic.

**Uçar, Cor. 4.21(iii)–(iv), Def. 4.22, Cor. 4.23** (arXiv:1711.03405, printed pp. 139–140):
for a closed orbisurface of constant curvature κ ≠ 0, "κ together with the spectrum determines
the number of cone points as well as the multiset of all orders" (4.21(iv), trivial mirror locus),
and for orientable ones also χ(O) and χ(X_O), hence the genus (4.23). The proofs reuse Theorem 3.40,
whose argument takes limits ν → ∞ over the entire sequence of heat invariants (pp. 98–99). **No
finite coefficient count appears anywhere in the thesis.** Uçar credits the κ = −1 case of 4.23 to
Dryden–Strohmaier, Canad. Math. Bull. 52 (2009), Prop. 3.3.

Further finite-coefficient results found: Abreu–Dryden–Freitas–Godinho (arXiv:math/0608462,
Thm 1, Thms 6.1–6.2: singularity orders of weighted projective planes from a₀, a₁, a₂), and Dryden
(arXiv:math/0411290, Props 3.5–3.6: area-only obstructions for hyperbolic orbisurfaces with one or
few cone points). Neither gives a threshold or a minimal degeneracy.

Exact check: for a hyperbolic pillow 0 < R < 1, so DGGW's c = S₁ + R − 2 encodes exactly the first
two coefficients; the first c-collision is {O(2,8,8), O(3,3,12)}, c = 67/4. Theorems A–B of the
manuscript therefore answer DGGW Rem. 5.16 sharply.

Instrument gaps bounding the verdict: forward-citation data for DGGW and Dryden–Strohmaier are
incomplete (zbMATH lists two citing papers for DGGW; Crossref citation data unavailable); the
published FoCM/MMJ versions were checked where reachable. See `literature/fetches.md`.

## Proposed manuscript wording

**§(a), replace its last two sentences by:**

> All of this determinacy is either full-spectrum or confined to non-hyperbolic classes. For
> $\chi(\mathcal O)\ge0$ a single coefficient suffices: the invariant $c$, twelve times the $t^0$
> coefficient, is a complete invariant of closed orientable $2$-orbifolds with $\chi\ge0$
> \cite[Thms~5.14--5.15]{dggw2008}, and spherical orbifolds are determined by finitely many terms
> \cite[Prop.~5.22]{dggw2008}; finitely many heat invariants also recover the singularity orders of
> weighted projective planes \cite[Thm~1]{adfg2008}. For hyperbolic orbisurfaces, by contrast, the
> cone orders and the genus were known to be spectral invariants only through the full spectrum
> \cite[Thm~1.1, Prop.~3.3]{drydenstrohmaier2009} or the entire sequence of heat invariants through
> a large-order limit \cite[Thm~3.40, Cors~4.21(iv), 4.23]{ucar2017}, and Dryden--Gordon--Greenwald--Webb
> remark that $c$ ``does not seem sufficiently strong to distinguish among'' hyperbolic triangular
> pillows \cite[Rem.~5.16]{dggw2008}.

**§(b), replace the novelty sentence by:**

> To our knowledge this is the first exact finite-coefficient determinacy threshold, with an
> explicit minimal degeneracy, for a family of hyperbolic cone orbifolds; it answers the question
> left open in \cite[Rem.~5.16]{dggw2008}. Since $0<R<1$ for a hyperbolic pillow, the invariant
> $c=S_1+R-2$ already encodes the first two coefficients, so Theorems~\ref{thmA}--\ref{thmB} say that
> $c$ separates the hyperbolic pillows with $p+q+r\le17$ and first fails on
> $\mathcal O(2,8,8),\mathcal O(3,3,12)$.

**Wherever the signature results are announced** (abstract, introduction), use:

> the first explicit finite number of heat coefficients, $\lfloor\operatorname{Area}/\pi\rfloor+4$,
> that determines the genus and the cone-order multiset uniformly over all closed orientable
> hyperbolic $2$-orbifolds

and never the unqualified "first finite count". Add the bibliography entries for
Dryden–Strohmaier (2009) to §(a), Abreu–Dryden–Freitas–Godinho (Ann. Global Anal. Geom. 2008,
arXiv:math/0608462) and, if the area-only obstructions are mentioned, Dryden (arXiv:math/0411290).
