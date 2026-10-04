# G5 referee report: cross-result consistency (P8)

Scope: statements only. The sources are `review/audit/STATEMENTS.md`, Uçar (arXiv:1711.03405) and
DGGW (arXiv:0805.3148). Every number below is recomputed with exact arithmetic (`fractions`, `sympy`).
The script is named next to each claim. Every script runs from the repository root with
`/opt/homebrew/Caskroom/miniforge/base/bin/python3 review/audit/consistency/<script>` and exits
nonzero on failure. Saved outputs: `check_*.txt`.

## Summary of findings

| # | finding | grade | fix |
|---|---|---|---|
| F1 | The paper's `rem:ncone` (PC.20) contradicts three other groups. (i) It says the bound "K ≤ n extends the n = 3 case of Theorem C". The paper's K(F) is K_iso, and K_iso = ∞ for n ≥ 4 (DF.7(b), LO Cor 2.3). (ii) It calls the lower bound K ≥ n for n ≥ 4 open "with neither a construction…". DF.7(c), AU.4 and CU.3 give an explicit n = 4 witness, {3,10,15,30} vs {4,5,21,28}. (iii) It makes recovery conditional "when these are independent", but AU Theorem A proves it for all n. | SERIOUS | Rewrite `rem:ncone` along the lines of DF.7(a)–(c): say K_mult ≤ n by Theorem A, K_iso = ∞ for n ≥ 4 by Cor 2.3, and K_mult = 4 is attained at n = 4 by the witness. |
| F2 | PC.17 says the interval-separation mechanism "localizes every degeneracy at sum S to the finitely many contacts between **adjacent** least-order strata". This is false. Of the 3067 pairs with S ≤ 600, 2793 join strata whose least orders differ by at least 2; the first is (5,15,15) ~ (7,7,21) at S = 35. The paper's own S = 36 example (4,16,16) ~ (6,6,24) joins strata 4 and 6, and so does every scaled base pair with k ≥ 2 (strata 2k and 3k), which `thm:density-lower` counts. The printed table is nevertheless correct: it matches a brute-force count. | SERIOUS | Replace "adjacent least-order strata" with "pairs of least-order strata whose R-intervals overlap". Describe the enumeration behind Table `tab:density` as exhaustive. |
| F3 | DI.11 says "k pairwise non-isometric pillows sharing a_0 and a_1". That is Uçar's a_ν indexing, where a_0 is the area (t^{-1}) term. The paper (eq:a0conv) and divergence use a_ℓ for the t^ℓ term. Under the manuscript's own convention the claim is false: the size-3 fibre at S = 136 has three different t^1 coefficients, −509549/400, −646049/400 and −732989/400. | SERIOUS (if carried into the paper); otherwise MINOR | Write "sharing c_1 and c_2 (equivalently R and S_1)". |
| F4 | `conj:density` says "N(S) ~ cS², **Equivalently**, N(S) = Θ(S)". Neither statement implies the other. "A positive proportion, of order 1/S" contradicts itself. | SERIOUS (a displayed statement with a false equivalence) | State the two forms separately, e.g. "Conjecture: N(S) ~ cS². A stronger pointwise form would be N(S) = Θ(S), so that a proportion ≍ 1/S of the triads participate." |
| F5 | Status drift. DF.7(a) says "for n ≥ 4 injectivity is not proved here", but AU Theorem A proves it and SG `rem:sigK` says so. DF `prop:Kinf` and SG `rem:sigK` still say "conditional on `thm:locality`", but LO Theorem 1 proves `thm:locality`. DF.4 says the g ≥ 1 Teichmüller count "would need its own source", but LO Prop 2.1 supplies it from Thurston 13.3.7. | MINOR | Update the labels and cross-reference LO Theorem 1 and LO Prop 2.1. |
| F6 | The paper (`thm:density-lower`, PC.17 "linear-order lower bound", PC.19 "density at least 1/18") understates what diophantine proves: N(X) ≥ (c_iso + o(1)) X log X (Thm 4) and ≥ (3/(128π⁴) + o(1)) X (log X)² (Thm 5). There is no conflict: both are o(X²), so they are consistent with `conj:density`. | MINOR | Either cite the stronger bounds or say that the linear bound is only the elementary one. |
| F7 | AU Theorem B states c_n ∈ ℚ^× for every n but lists values only for n ≤ 8. Lemma S2.1 gives c_n = (−1)^{n(n+1)/2}. The two agree: the actual Theorem B system gives this for n = 2…8. If Theorem A for n ≥ 9 relies on det M ≠ 0, then it relies on S2.1. That is not a cycle, because S2.1 uses only the definition of M. | MINOR | In Theorem B, state c_n = (−1)^{n(n+1)/2} and cite Lemma S2.1. |
| F8 | Symbol collisions. **c_n** has three meanings: the Theorem B constant; −∏_{r<n}(2r−1) in AU Remark 2; and the heat coefficients c_j. Uçar's c^S_ℓ and divergence's c_ℓ add two more. **α**: SG's α_l in (H3) equals α^{LO}_{l+1}/(4π), so the same letter has a different index and normalisation. **κ** means curvature, the AU Theorem C pair constant, and ‖M^{-1}‖ in stability. **a**: the paper's a^{sm}_ℓ sits at t^{ℓ−1}, but its a_0 sits at t^0, in adjacent sections. **K** means Gauss curvature and also K(F)/K_mult. **K_mult(𝒞)** in curvature is a class-level supremum, not `def:K`. **s_k** in DV Theorem 3 is undefined in the register. | MINOR | Rename (for example ĉ_n, J_n, α^{SG}). Define s_k := a_k/vol at κ = 1; Uçar (4.35) gives s_k > 0, checked for k ≤ 40. |
| F9 | `thmC`/`prop:recovery` say "up to isometry, equivalently … cone orders". That equivalence needs the rigidity of triangle orbifolds (DF `prop:rigidity`; Teichmüller dimension 0 by LO Prop 2.1), which no paper-core statement cites. | MINOR | Cite rigidity in Theorem C. |
| F10 | PC.2 and `rem:bugfix` use the spherical (K = +1) triple (2,3,5) as a reference inside hyperbolic conventions. This is harmless: the t^0 term χ/6 does not depend on the sign of κ. I confirmed this from the exact spectrum of S²/G. | MINOR | Add one sentence saying so. |
| F11 | Locality: Proof C of Theorem 1 goes through Theorem 3.1, whose Lemma 3.2 uses a Weyl bound from Theorem 1. That is a cycle, but it is not genuine for Theorem 1, which has the independent DGGW Thm 4.8 + Uçar Thm 4.20 proof. These texts are not in the register; I am grading the brief's description. | MINOR | Label Proof C as a consistency check, or source the Weyl bound independently (for example the leading DGGW term, or a Weyl law for compact orbifolds). |
| F12 | The register is incomplete for P8. The divergence a_1/a_0 values, locality "Proof C", the Weyl input of Lemma 3.2, "T1 uses Theorem A" and the "isolation theorem using Theorem B" do not appear in STATEMENTS.md. | MINOR | Add these statements to the register. |
| F13 | ST.14: for (2,3,7) at ν = 0, δ_cert/\|H_0\| = 0.003999 is printed as 4.0e−03, i.e. rounded up. The round-down rule in ST.13 covers the δ's, not these ratios. | NONE (cosmetic) | Optional: print 3.9e−03. |
| F14 | Heat input: all ten groups state the same function (§1). | NONE | — |
| F15 | Indexing and every cross-group number agree (§2). | NONE | — |
| F16 | Counts agree across paper, threshold and diophantine (§4). | NONE | — |

**No FATAL findings.**

## 1. Heat input (`check_heat_input.py`)

**Derivation from Uçar.** Uçar's Thm 4.20(i) and (4.35) give the smooth coefficient

a_ν/vol = κ^ν (ν!4^ν)^{-1} Σ_ℓ C(ν,ℓ)(−4)^ℓ B_{2ℓ}(½).

At κ = +1 this is 1, 1/3, 1/15, 4/315, 1/315, 4/3465, 382/675675, …

Uçar's Thm 4.20(ii), (4.33) and (4.25) give the cone term at order t^ℓ:

b_ℓ(m) = κ^ℓ β_ℓ(m), with β_ℓ = Σ_{i≤ℓ} 2/(4^i i!) c^S_{ℓ−i}(π/m).

For p_ℓ := m β_ℓ:

- p_0 = (m²−1)/12
- p_1 = m⁴/360 + m²/36 − 11/360
- p_2 = m⁶/2520 + m⁴/720 + m²/180 − 37/5040

For every ℓ ≤ 8 and m ≤ 30, p_ℓ is even, of degree 2ℓ+2, has p_ℓ(1) = 0, has leading coefficient exactly |B_{2ℓ+2}|/(2(ℓ+1)!(2ℓ+1)), and β_ℓ(m) > 0.

**Group by group.** Each group's stated heat input reproduces this function exactly for ℓ ≤ 8 and m ≤ 30.

| group | stated input | cone sign | verdict |
|---|---|---|---|
| paper | b_0 = (m²−1)/(12m) via (1/4m)Σcsc², exact for m ≤ 30; eq:b1 with K^1; smooth t^0 = χ/6 | K^ℓ (only ℓ = 1 written, K = −1 used) | same. DGGW (5.5) and (5.9), with R_{1212} = K, also give β_0 and β_1. |
| definitions | c_1 = Area/4π = −χ/2 = (1−R)/2 | — | same |
| audibility | b_l = K^l p_l/m, K = −1 | K^l | same |
| signatures | (H2) is Uçar verbatim; statements.tex writes (−1)^l k^{-1}p_l | K^l and (−1)^l | same (at K = −1) |
| locality | α_k and β_k from Uçar at κ = −1; Φ_j | κ = −1 built in | same; Φ_j checked for genus 0–2 |
| stability | b_ν = (−1)^ν p_ν/m; α = 1, −1/3, 1/15, −4/315, 1/315 | (−1)^ν | same |
| curvature | Kokotov (F) at K = 0; a_0 at K = +1; K^ℓ kills ℓ ≥ 1 at K = 0 | K^ℓ, K ∈ {0, ±1} | same; flat c_0 = 0, ½, ⅔, ¾, ⅚ and DGGW c = 0, 6, 8, 9, 10 |
| divergence | Lemma 1(a), generating function G_k | K^ℓ, K = ±1 | same. Theorem 3's a_ℓ matches if s_k := Uçar a_k/vol at κ = 1. Theorem 2 rate checked numerically. |
| threshold, diophantine | none; only (S_1, R) | — | n/a |

**Sign of K.** The groups that use K = +1 are curvature Part 2, the paper's (2,3,5) reference, and divergence (K = ±1). I checked the K^ℓ convention independently from the exact spectrum of S²/G (curvature Lemma 2) for G with orders (2,3,5), (2,3,4), (2,3,3), (5,5) and (2,2,7). In each case the spectrum reproduces every coefficient from t^{-1} to t^8 of the K = +1 prediction, signs included. The K = −1 specialisations, written as (−1)^ℓ in stability and SG statements.tex, are therefore the same function. No group silently flips the sign.

## 2. Indexing (`check_indexing.py`)

| power | definitions | stability | paper | signatures | divergence | ordinal |
|---|---|---|---|---|---|---|
| t^{-1} | c_1 | H_{-1} | a^{sm}_0/(4π) (PC.3, Uçar) | area | — | 1st |
| t^0 | c_2 | H_0 | a_0 (eq:a0conv) | α_0·Area + C_0 | a_0 | 2nd |
| t^1 | c_3 | H_1 | "third coefficient" | α_1·Area + C_1 | a_1 | 3rd |
| t^ℓ | c_{ℓ+2} | H_ℓ | a_ℓ | C_ℓ | a_ℓ | (ℓ+2)-th |

- "The first k coefficients" means t^{-1}, …, t^{k−2} in definitions, audibility, signatures, stability, curvature and paper. "The third coefficient" is t^1 everywhere. The one exception is the diophantine label (F3).
- K(F) in the paper is K_iso(·; 𝒫_3) from definitions; `prop:rigidity` makes it equal K_mult.
- c_1 = H_{-1} = Area/4π = (n−2−R)/2. For pillows this is (1−R)/2.
- c_2 = H_0 = a_0 = (P_1 + R − 2n + 4)/12. At n = 3 this is (S_1 + R − 2)/12, the same in paper and stability.
- c_3 = (1−R)/30 − P_3/360 − S_1/36 + 11R/360.
- Values for the collision pair:
  - (2,8,8): c_1 = 1/8, a_0 = 67/48, a_1 = −1601/480.
  - (3,3,12): c_1 = 1/8, a_0 = 67/48, a_1 = −867/160.
  - These match the divergence quotes.
- The P_3 weight is −1/360 in the paper, equals L_{22} in stability, and is −1 times the leading coefficient of p_1.
- Stability front end, from L built out of my coefficients:
  - L^{-1} rows: R = [−2]; P_1 = [2, 12]; P_3 = [−18, −120, −360]; P_5 = [30, 252, 1260, 2520]; P_7 = [−70/3, −240, −1680, −6720, −10080].
  - Diagonal: 2, 12, 360, 2520, 10080, 28512, 43243200/691, 112320.
  - Row sums: 2, 14, 498, 4062, 56230/3, 303654/5, 104899830/691, 10805786/35.
  - κ_r(2,8,8) = 0.33, 0.94, 1.33.
  - All eleven rows of ST.14 reproduce.
- Theorem B: I built the system from tanh(Σ P_k z^k/k). The true e solves it, and det M = (−1)^{n(n+1)/2} ∏(m_i+m_j)/e_n for n = 2…8. This equals both Theorem B's list and Lemma S2.1. S2.2 (B = SM, det B) also holds.
- AU Remark 2's Jacobian constant −∏(2r−1) (n ≤ 6) and PC.10's det DF agree once the row order is accounted for.
- Witnesses:
  - n = 3: the pair shares c_1 and c_2 and differs at c_3; Φ = 500z³.
  - n = 4: the pair shares c_1–c_3 and differs at c_4; P_5 = 25159618 vs 21298618; Φ = 1544400z³.
  - ex:siggenus: the pairs share exactly 2 and exactly 3 coefficients, and the Lemma 4 mirror identity holds.
- PC.15 and TH.0: τ_p, φ_p and the S = 18 endpoints all check.
- The minimum of a_0 is 107/144, at (3,3,4).

## 3. Dependency graph (`check_deps.py`, `deps.json`, `deps_table.txt`)

The graph has 119 nodes and 178 edges. Each edge has a kind: uses, proved_by, definition, crosscheck, sharpness, inferred, or reported. "Reported" means the brief names the edge but the register does not show it. Tarjan SCC gives:

- **Statement-visible logical edges: no cycle.**
- **All logical edges, including reported ones:** one cycle, LO.T1 → LO.T3.1 (Proof C) → LO.L3.2 (Weyl bound) → LO.T1. This is **not genuine for Theorem 1**, because LO.T1 → Uçar/DGGW is an independent proof. Once Proof C is treated as a cross-check, the graph is acyclic (F11).

Other candidates I examined:

| candidate | verdict |
|---|---|
| thm:locality / prop:Kinf / Cor 2.3 | No cycle. `thm:locality` is proved_by LO.T1. prop:Kinf and Cor 2.3 duplicate each other; Cor 2.3 borrows only the class 𝒫_n from rem:nconerestated (a definition edge). |
| T1 → Theorem A | One-way. Audibility never uses signatures. |
| Theorem B c_n ↔ Lemma S2.1 | S2.1 uses only the definition of M, so this is not a logical cycle even if Theorem B cites S2.1 (F7). |
| curvature Part 3 → Theorem A, C | One-way. curvature → divergence Lemma 1 is also one-way. |
| thm:Crestated → thmC, prop:recovery, prop:rigidity, thmB | Acyclic. |
| isolation (DI.7) vs thmB | Cross-check only. DI.7 borrows the base pair; neither result proves the other. |
| threshold Cor 2 / Lemma 2 vs thm:separation | Restatement, i.e. cross-check. |
| threshold table vs diophantine groups.csv | Cross-check. |

## 4. Claim conflicts and scope

- **c_n.** The Theorem B values agree with Lemma S2.1 (F7). The other "c_n" in AU Remark 2 is a different constant (F8).
- **"K(F) = 3 exactly for collisions".** PC thmC, DF.6 and PC.19 agree: with rigidity, K > 2 if and only if the pillow is in a collision.
- **"K_mult ≥ 4" claims.** These are made only for the specific n = 4 witness (DF.7(c); CU Part 3, "equality for n = 3, 4"). They are mutually consistent. Only PC.20 conflicts (F1).
- **conj:density vs diophantine.** Compatible: the diophantine lower bounds are o(X²). The conjecture's wording is wrong (F4), and the paper understates the known bounds (F6).
- **Counts** (`check_counts.py`, exact enumeration of every hyperbolic triad with S ≤ 600):
    - None for S ≤ 17; a unique pair at S = 18.
    - Cumulative pairs at S = 18, 100, …, 600: 1, 92, 386, 840, 1496, 2210, 3067, matching `tab:density` and its ratios.
    - ⌊S/18⌋ bound holds; two classes at S = 36.
    - 2977 fibres. 3067 − 2977 = 90, which comes from 40 fibres of size 3 and 2 of size 4. So the paper counts pairs and threshold counts fibres; both are correct and consistent with DI.8's convention.
    - The first fibre of size 3 is at S = 136 (λ = 68/5), and of size 4 at S = 408 on the same curve.
    - 1753 primitive pairs: 423 dual and 1330 others.
    - The TH.5 first collisions and Theorem 1's S*(p) (p ≤ 25) check.
    - The base-pair class has exactly two members at every S = 18k ≤ 600.
    - The D_{u,v} formulas hold.
  - F2: 2793 of the 3067 pairs join non-adjacent strata, the first at S = 35 ((5,15,15) ~ (7,7,21)).
  - DI.2: the discriminant 2¹²λ²(λ−9)(λ−1)³ checks. Our model at λ = 27/2, the integral model [0,393,0,3456,0] and BGN's model at n = 27/2 all have the same j-invariant; the integral model is BGN's scaled by u = 2.
- **Theorem C (paper, n = 3) and Theorem A (all n).** Compatible. At n = 3, Theorem A plus rigidity gives thmC; the paper proves thmC via prop:recovery.
- **Scope.**
  - Paper: genus 0, three cone points; comparison class 𝒫_3.
  - Audibility: genus 0, compared with multisets of the same size n. Remark 3 extends this to at most n points.
  - Signatures T1(3): all of genus 0, separated by max(n, n') coefficients.
  - Signatures S2: all genera.
  - All groups are orientable and have cone points only. Uçar Cor 4.21 and DGGW 5.22 are broader.
  - None of these overlaps contradicts another. Every K statement should name its comparison class (F8).
