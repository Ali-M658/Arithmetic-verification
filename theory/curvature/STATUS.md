# STATUS: curvature as the amplifier

## Verdict

**PROPOSITION PROVED, with an honest reading. Parts 1–2 are prior work (DGGW Theorem 5.15,
which is strictly stronger; also DGGW Prop. 5.22 and Uçar Cor. 4.21(iv)). Here they are reproved
independently and placed beside the hyperbolic case.**

| geometry (closed, orientable, cone points only) | class | $K_{\rm mult}$ (Theorem A counting) | what does the work |
|---|---|---|---|
| flat | $T^2$, $(2,2,2,2)$, $(3,3,3)$, $(2,4,4)$, $(2,3,6)$ | **2**, sharp | constant term alone: $0,\frac12,\frac23,\frac34,\frac56$ |
| spherical | $S^2$, $(n,n)$, $(2,2,n)$, $(2,3,3)$, $(2,3,4)$, $(2,3,5)$ | **2**, sharp | constant term alone |
| hyperbolic, genus 0, $n$ cones | infinite, $n$ unbounded | $\le n$; $=n$ for $n=3,4$; non-decreasing, so $\ge4$ for $n\ge4$; integer growth open | first $n$ coefficients, $n-2$ of them curvature-amplified (Theorem A) |

- **Flat.** Every heat coefficient beyond $t^0$ vanishes identically (Kokotov, Thm 1).
- **Spherical.** The area coefficient alone fails infinitely often: $\chi(2,2,n)=\chi(2n,2n)$.

**Physical reading, as proved.**

- In non-negative curvature the cone data are heard for a *trivial* reason. Gauss–Bonnet leaves
  a finite list plus two one-integer families, and one rational number separates them. A cap on
  the number of cones alone would not do it: hyperbolic triads collide at $t^{-1},t^0$. "Curvature is
  required" is false for orbifolds, since flat orbifolds are heard with the amplifier off.
- What is true is the mechanism. At $K=0$ the heat trace hears exactly one symmetric function
  of the cone angles. That provably fails on flat cone spheres:
  - a curve of non-isometric doubled triangles shares all heat coefficients;
  - the orbifold $S^2(2,4,4)$ shares all of them with the non-orbifold doubled triangle
    $\pi(\frac15,\frac25,\frac25)$.
- For $K\ne0$ each order adds one odd power sum. That is what lets Theorem A (and Uçar,
  Cor. 4.21(iv)) recover arbitrarily many cones. The zero/nonzero contrast for polygons is
  Uçar's (printed pp. 97, 99).
- Not claimed: that the integer $K_{\rm mult}$ grows with $n$ in negative curvature. This was
  corrected after the adversarial review.

## Verification (`curvature_checks.py`, output `curvature_output.txt`, about 7 s)

- **F1–F4:**
  - flat classification (exhaustive with proof of bounds);
  - constant terms (match DGGW Table 1);
  - $K=0$ kills $b_\ell$, $\ell\ge1$;
  - the doubled-triangle pair and the level curve.
- **S1.** The invariant-multiplicity formula (Lemma 2) agrees with explicit character sums over
  generated groups $C_5,D_2,D_6,T,O,I$, $\ell\le61$.
- **S2.** The exact small-$t$ expansion of each spherical cone series, from the spectrum of
  $S^2/G$ via Hurwitz zeta values, equals Uçar's $b_\ell(m)$ at $K=+1$, for $\ell\le12$ and
  $2\le m\le30$. This is an independent confirmation of the $K^\ell\frac1mp_\ell(m)$ structure
  from first principles. The constant terms also match DGGW Table 1.
- **S3.** Injectivity of the constant term on the spherical class is proved; the enumeration is
  checked to $n=20000$. The area coefficient is non-injective.

## Sources

`sources.md`: Kokotov arXiv:0906.0717; DGGW arXiv:0805.3148; Thurston ch. 13; Uçar
arXiv:1711.03405; Dryden–Strohmaier arXiv:math/0504571. All were fetched on 2026-10-01, with
page references.

## Scope and open points

- Non-orientable and mirrored orbifolds are not treated. The heat coefficients fail there
  (DGGW Rem. 5.23; torus vs Klein bottle in DGGW Table 1); this is cited, not reproved.
- Hyperbolic integer sharpness for $n\ge5$ remains open (`theory/audibility`).
