# P6. Priority claim: finite-coefficient determinacy for hyperbolic cone orbifolds

## Verdicts

- **(N) Narrow claim. It survives**, as far as the search reaches (see search log and fetches.md, gap 5). The claim reads: "To our knowledge this is the first exact finite-coefficient determinacy threshold, with an explicit minimal degeneracy, for a family of hyperbolic cone orbifolds" (main.tex §Locating the novelty (b)). I found no prior threshold or minimal-degeneracy statement for any hyperbolic family. It should cite DGGW Remark 5.16, which poses exactly this question; see §4.
- **(B1) "All of this determinacy is asymptotic or full-spectrum and qualitative; none of it counts coefficients or exhibits a sharp finite boundary"** (§(a)). **False as written. Must be narrowed.**
  - DGGW Theorems 5.14/5.15 are explicit one-coefficient determinations: the single invariant c, which is 12 times the t^0 coefficient.
  - DGGW Proposition 5.20 reads the curvature sign off the t-coefficient.
  - Abreu–Dryden–Freitas–Godinho determine orbifold singularity orders from a_0, a_1 (and a_2).
  - Dryden (math/0411290) Propositions 3.5–3.6 get cone data of hyperbolic orbisurfaces from the area alone.
- **(B2) A "first finite, explicit coefficient count" for hyperbolic orbifolds.** **Must be narrowed.**
  - In full generality it is false, in a weak sense. Dryden's Proposition 3.5 determines the cone order of a genus-g, one-cone-point hyperbolic orbisurface among genus-g hyperbolic orbisurfaces, and its proof uses only χ, i.e. the leading coefficient.
  - DGGW Remark 5.16 separates hyperbolic pillows from χ>0 pillows, teardrops and smooth surfaces with c alone.
  - What survives is narrower. The manuscript gives the first explicit finite count that determines the cone-order multiset (and genus) uniformly over a whole hyperbolic class: SG.7/SG.13, ⌊Area/π⌋+4, and Theorem A's K_mult ≤ n for genus 0. It also gives the first sharp count for pillows.
- **DGGW 5.15 does not touch hyperbolic orbifolds.** Its class is χ ≥ 0.
- **Uçar never gives a finite count.** The proof of Theorem 3.40, which Corollaries 4.21/4.23 inherit, uses limits ν→∞ over the whole sequence of coefficients.

## 1. DGGW: what is proved

Sources: arXiv:0805.3148 (`../sources/dggw_0805.3148.txt`) and Michigan Math. J. 56 (2008) (`sources/dggw_mmj2008.txt`). The §5 text is identical in substance between the two. The 2017 erratum changes only Theorem 5.1.

**(5.13)** (arXiv p. 27; MMJ p. 230):
> "Let O be an orientable 2-orbifold with k cone points of orders m1, . . . , mk, denoted O(m1, . . . , mk), and consider the quantity c defined as 12 times the degree zero term: (5.13) c = 2χ(O) + Σ (mi − 1/mi). This quantity is a spectral invariant; note that it depends only on the topology, not on the Riemannian metric."

**Theorem 5.14** (arXiv p. 28; MMJ p. 230):
> "Within the class of all footballs (good or bad) and all teardrops, the spectral invariant c is a complete topological invariant."

**Theorem 5.15** (arXiv p. 29; MMJ p. 232):
> "Let C be the class consisting of all closed orientable 2-orbifolds with χ(O) ≥ 0. The spectral invariant c is a complete topological invariant within C and moreover, it distinguishes the elements of C from smooth oriented closed surfaces."

Summary of 5.15:
- **Class:** orientable, χ ≥ 0, good or bad, with no metric assumption.
- **Invariants:** exactly one heat coefficient, the t^0 term.
- **Count:** finite and explicit (one).
- **Hyperbolic orbifolds:** excluded (χ < 0).

The proof is a finite case check using Tables 1 and 2 (arXiv pp. 28–31): "We first consider the 2-orbifolds for which c is an integer. … c(2, 2) = 5, c(2, 3, 6) = 10, c(2, 4, 4) = 9, and c(3, 3, 3) = 8."

**Table 1** (arXiv p. 28; MMJ p. 231): "2-orbifold expansions with χ(O) ≥ 0". It lists expansions up to O(t) for spherical and flat orbifolds only.

**Remark 5.16** (arXiv p. 31; MMJ p. 234). This is the key passage for the manuscript:
> "Notably absent from the class C are triangular pillows with χ(O) < 0. The invariant c does not seem sufficiently strong to distinguish among these triangular pillows. However, as a special case of a result in [13], the spectrum does determine the orders of the cone points in such a 2-orbifold, provided that it is endowed with a metric of constant curvature −1."

Here [13] is Dryden–Strohmaier, which uses the full spectrum. Remark 5.16 then proves, using c alone, that hyperbolic pillows are distinguished from O(2,2,m), from χ>0 pillows, from teardrops and from smooth surfaces. For footballs, "it seems that metric assumptions are again necessary."

**Proposition 5.20** (arXiv p. 33; MMJ p. 235):
> "Within the class of closed 2-orbifolds of constant nonzero curvature R or −R the spectrum determines the sign of the curvature"

The proof uses only the t^{-1}, t^0 and t coefficients ("look at the coefficient of the t term").

**Proposition 5.22** (arXiv p. 33; MMJ p. 236):
> "Within the class of spherical 2-orbifolds of constant curvature R > 0 the spectrum determines the orbifold."

The proof uses c together with the degree −1/2 (mirror length) term. This is again finite, and it is spherical.

**Exact check** (`check_priority.py`, output in `check_priority.out`; it passes):
- DGGW's Table 2 is consistent with c = S_1 + R − 2 on pillows.
- For hyperbolic pillows 0 < R < 1, so c alone encodes (S_1, R) = (⌊c⌋+2, frac c). That is exactly the content of the first two coefficients in Corollary D.
- The first c-collision is {O(2,8,8), O(3,3,12)} with c = 67/4, and it is the only one with S_1 ≤ 18.

So Theorems A/B answer DGGW Remark 5.16 sharply, even for DGGW's metric-free single invariant c.

## 2. Uçar (arXiv:1711.03405): what is proved

Page numbers are the printed thesis pages.

**Theorem 3.40** (p. 98):
> "Let Ω be a polygon of nonzero constant curvature. Then the number of angles which are not equal to π is a spectral invariant. Moreover, the multiset consisting of all angles of Ω which are not equal to π is a spectral invariant as well. Furthermore, the Euler characteristic χ(Ω) of the polygon is a spectral invariant."

Proof (pp. 98–99):
> "Because the Gaussian curvature is not zero, there are infinitely many nonvanishing heat invariants. … we conclude by induction that the spectrum determines the sequence (Wν)ν∈N0. … We claim that the smallest angle can be deduced from the sequence (Wν,1)ν∈N0. … lim ν→∞ γ^{2ν+1}·Wν,1 … θ1 = inf {γ > 0 | γ^{2ν+1}·Wν,1 is convergent as ν → ∞ with nonzero limit}. … Repeating this argument in the above manner, we successively obtain M values θ1 ≤ θ2 ≤ ... ≤ θM."

The method is therefore a ν→∞ limit. It needs the entire infinite sequence of heat invariants and yields no finite count. My search of the thesis text for "finitely many", "first few", "first two" and "first three" found no finite-count statement by Uçar. The only "first few" occurrence describes DGGW (p. 141: "They prove this result by comparing the first few heat invariants").

**Corollary 4.21** (p. 139):
> "Let O be a closed orbisurface of constant curvature κ ∈ R. … (iii) If κ ≠ 0, then κ together with the spectrum determines the number M + 2N as well as the multiset {m1,...,mM,n1,n1,n2,n2,...,nN,nN}. (iv) If the mirror locus is trivial and κ ≠ 0, then κ together with the spectrum determines the number of cone points as well as the multiset of all orders {n1,...,nN}."

It is introduced with: "Therefore we obtain, just as in Corollary 3.38 and Theorem 3.40, the following spectral invariants". That is, it uses the same ν→∞ argument.

**Definition 4.22** (p. 139):
> "χ(O) := χ(XO) − ½ Σ (1 − 1/mi) − Σ (1 − 1/ni)."

**Corollary 4.23** (p. 140):
> "Let O be a closed orientable orbisurface with constant curvature κ ≠ 0. Then κ together with the spectrum of O determines the Euler characteristic of O as well as the Euler characteristic of the underlying space XO."

The proof goes through Corollary 4.21(iv), so it is again full-spectrum. Uçar credits the κ = −1 case to Dryden–Strohmaier: "This fact was previously known in the special case of closed orientable orbisurfaces of constant curvature κ = −1 (see [DS09, Proposition 3.3])."

Summary of Uçar:
- **Class:** constant curvature κ ≠ 0 (spherical or hyperbolic), with κ given. For (iv), the mirror locus is trivial; this includes orientable orbisurfaces and non-orientable ones with only cone points and crosscaps.
- **What is determined:** the cone-order multiset (iv), χ(O), and χ(X_O), hence the genus in the orientable case (4.23).
- **Invariants used:** all of them, through a limit.
- **Finite count:** none.

## 3. Dryden–Strohmaier and Dryden 2004

**Dryden–Strohmaier**, arXiv:math/0504571, Theorem 1.1 (p. 2):
> "Let O be a compact orientable hyperbolic orbisurface. The Laplace spectrum of O determines its length spectrum and the number of cone points of each possible order."

Proposition 3.3 (p. 5):
> "Isospectral compact orientable hyperbolic orbisurfaces have the same underlying topological space."

Both rest on the Selberg trace formula and the full spectrum.

**Dryden 2004**, arXiv:math/0411290, Proposition 3.5 (p. 5):
> "Fix g ≥ 1 and m ≥ 2. Let O be a compact orientable Riemann orbisurface of genus g with exactly one cone point of order m. Let O′ be in the class of compact orientable Riemann orbisurfaces of genus g, and suppose that O is isospectral to O′. Then O′ must have exactly one cone point, and its order is also m."

The proof uses only "χ(O) = χ(O′)" (from the volume via Weyl's law and Gauss–Bonnet), together with Theorem 3.2 to exclude a cone-free O′. Proposition 3.6 and Corollary 3.7 (p. 6) are similar area-only obstructions, for example: genus g with k cone points versus genus g with l ≥ 2k cone points. The text adds: "Note that in all of the above results, we have the hypothesis that O′ is hyperbolic."

These results use a single coefficient, the area, on hyperbolic orbisurfaces. They are trivial-scale, phrased as isospectrality, and contain no threshold. They are nonetheless finite-coefficient statements about hyperbolic cone orbifolds, so the broad claim (B2) cannot stand unqualified.

## 4. Other finite-coefficient orbifold results found

- **Abreu–Dryden–Freitas–Godinho**, arXiv:math/0608462 (Ann. Global Anal. Geom. 2007/08).
  - Theorem 1 (p. 2): "the spectra of the Laplacian acting on 0- and 1-forms on M determine the weights N1, N2, N3". Here M = CP²(N1,N2,N3) is a weighted projective plane with any Kähler metric.
  - The proof in §6.1 (pp. 17–19) uses a_0, a_1, a_2 of Δ_0 and Δ_1 to obtain b, c, d and then Vieta: "(6.15) … This equation determines N1, N2 and N3 uniquely up to permutation."
  - Theorem 6.1 (p. 20), for prime weights, uses "only a0 and a1 for functions".
  - This is a finite-coefficient determination of orbifold singularity orders, and it uses the same symmetric-function recovery as the manuscript's Proposition (recovery). It is in dimension 4 and not hyperbolic. **Cite it**, because it pre-empts any claim of first finite-coefficient recovery of orbifold isotropy orders in general.
- **Gittins et al. Part 1** (arXiv:2106.07882), Remark 4.4 (printed p. 20):
  > "It is shown in [DGGW08, Theorem 5.15] that the 0-spectrum alone suffices to distinguish singular, closed, locally orientable Riemannian orbisurfaces with nonnegative Euler characteristic from smooth, oriented, closed Riemannian surfaces. In fact, it is shown there that the degree zero term … gives rise to a complete topological invariant…"

  Their Theorem 1.1 (orbifold versus manifold using the 0- and 1-spectra) does not determine cone orders. Part 2 (2311.00337) concerns the volume of the singular set and 1-isospectral flat 2-orbifolds. Neither is relevant to cone-order counts.
- **Richardson–Stanhope** (1910.03224): local orientability from heat invariants. Not relevant to cone orders.
- **Stanhope** (math/0301357) and **Proctor–Stanhope** (0811.0797): finiteness of isotropy types or diffeomorphism types in isospectral sets with curvature bounds. These are full-spectrum, give no determinacy and no count. Proctor–Stanhope never mentions heat invariants except in the DGGW reference.
- **Bari–Hunsicker** (1705.01412), abstract: "the coefficients of the asymptotic expansion of the trace of the heat kernel are not sufficient to determine the above results". This is a negative result for orbifold lens spaces.
- **Grieser–Maronna** (1208.3163): a Euclidean triangle is determined by area, perimeter and Σ1/angle, i.e. finitely many heat invariants. These are not orbifolds; it is a possible analogy to mention.
- **Uçar Corollary 3.45** (hyperbolic triangles determined within polygons) uses the full spectrum through Theorem 3.40.

## 5. Search log

Raw logs: `search/arxiv_ft.txt`, `search/arxiv_api.txt`, `search/crossref.txt`, `search/zbmath.txt`.

- **arXiv full text** (27 queries), including:
  - "heat invariants determine orbifold"
  - "finitely many heat invariants cone points"
  - "heat coefficients orbisurface cone angles"
  - "spectral determination orbifold singular strata heat trace"
  - "Spectral and geometric bounds on 2-orbifold diffeomorphism type"
  - "spectral bounds on orbifold isotropy"
  - "heat invariants orbisurface hyperbolic cone orders determined"
  - "heat trace triangular pillow"
  - "first three heat invariants determine"
  - "hyperbolic orbisurface spectrum determines cone orders"
  - "teardrops footballs spectral invariant"
  - "hear the orders of the cone points"
  - "orbisurfaces heat invariants Euler characteristic genus"
  - "Dryden Gordon Greenwald Webb Theorem 5.15"
  - Sutton / Proctor–Stanhope / Gordon queries
- **arXiv API:** au:Proctor, au:Stanhope, au:Sutton, abs:orbifold+"heat invariants", abs:orbisurface+spectrum, ti:hearing+abs:orbifold, and others.
- **Crossref** (14 bibliographic queries) and **zbMATH Open** (heat invariants orbifold; orbisurface spectrum; heat trace orbisurface; hearing orbifold; `ci:` citation searches).
- **Read in full or in the relevant sections:** DGGW (arXiv and MMJ) §5 and the erratum; Uçar §3.3 and §4.3; Dryden–Strohmaier; Dryden 2004 §§3–4; ADFG §§1, 5–6; Gittins 1 and 2 (introductions, Remark 4.4); Richardson–Stanhope, Stanhope, Proctor–Stanhope (abstracts and main theorems); Bari–Hunsicker (abstract); Mårdby–Rowlett survey (all orbifold mentions); Schueth 1812.06119 (no determinacy statements).
- **Not found:** any paper that gives, for a family of hyperbolic cone orbifolds, the least number of heat coefficients that determines the orbifold together with a sharpness example. The forward-citation chase is incomplete (fetches.md, gap 5).

## 6. Further accuracy points in §(a)

- "Uçar already proves that the full spectrum determines the cone-order multiset of an orientable constant-curvature orbisurface". This is accurate up to the hypotheses: κ ≠ 0, κ given, mirror locus trivial. The κ = −1 case is Dryden–Strohmaier 2009 (Theorem 1.1, Proposition 3.3), which Uçar himself credits. **Add [DS09].**
- "the known spherical near-collisions" should point to specific places: DGGW Proposition 5.22 (proof) and Uçar p. 141 list the spherical pairs with equal c or equal multiset (O(∗m,m), O(m×), O(m∗); O(∗2,2,m), O(2,∗m); O(∗2,3,3), O(3,∗2)).
- CU.3 "Strength" is consistent with the quotes above. DGGW 5.15 covers all closed orientable χ ≥ 0 orbifolds, good or bad, plus S² and T² (c(S²)=4, c(T²)=0 in the proof). The flat c_0 values in CU.3 match Table 1 (1/2, 3/4, 2/3, 5/6, and 0 for the torus). DGGW 5.22 also covers non-orientable spherical orbifolds.

## 7. Proposed wording

Replace the last two sentences of §(a) with:

> All of this determinacy is either full-spectrum or confined to non-hyperbolic classes. For χ(O) ≥ 0 a single coefficient suffices: the invariant c, which is twelve times the t⁰ coefficient, is a complete invariant of closed orientable 2-orbifolds with χ ≥ 0 [DGGW, Thms 5.14–5.15], and spherical orbifolds are determined by finitely many terms [DGGW, Prop. 5.22]. Finitely many heat invariants also recover the singularity orders of weighted projective planes [ADFG, Thm 1, Thms 6.1–6.2]. For hyperbolic orbisurfaces, by contrast, cone orders and genus are known to be spectral invariants only through the full spectrum, via the Selberg trace formula [DS09, Thm 1.1, Prop. 3.3] or the entire sequence of heat invariants through a ν → ∞ limit [Uçar, Thm 3.40, Cors 4.21(iv), 4.23]. DGGW remark that c "does not seem sufficiently strong to distinguish among" hyperbolic triangular pillows [DGGW, Rem. 5.16]. Apart from area-only obstructions [Dryden 2004, Props 3.5–3.6], no finite coefficient count was known there.

Replace the novelty sentence in §(b) with:

> To our knowledge this is the first exact finite-coefficient determinacy threshold, with an explicit minimal degeneracy, for a family of hyperbolic cone orbifolds. It answers the question left open in [DGGW, Rem. 5.16]. Since 0 < R < 1 for a hyperbolic pillow, the invariant c = S₁ + R − 2 already encodes the first two coefficients, so Theorems A–B say precisely that c separates hyperbolic pillows with p+q+r ≤ 17 and first fails on O(2,8,8), O(3,3,12).

If the manuscript states a "first finite, explicit coefficient count" for hyperbolic orbifolds elsewhere (abstract or the signature section), qualify it as:

> the first explicit finite number of heat coefficients, ⌊Area/π⌋+4, that determines the genus and cone-order multiset uniformly over all closed orientable hyperbolic 2-orbifolds

and add the citations above. Do not use the unqualified "first finite count".
