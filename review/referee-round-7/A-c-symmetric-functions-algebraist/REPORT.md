<!-- Referee A-c: returned text saved verbatim; the reviewer could not write files -->

Writing `REPORT.md` was refused, so the full report is below. In short: I found no fatal flaw and no mathematical error in Section 3, Appendix A or the supplement sections they rely on. Two statements are false as written but easily fixed: a claim in Theorem 3.11 (m3) and a missing hypothesis in Proposition 3.12 (m4). My recommendation is **minor revision**. The three major points concern overclaimed statements, a correspondence stated only in prose that the growth proofs depend on, and credit for classical tools.

---

# Referee report: "How much of a hyperbolic orbifold does heat hear?" (AGAG)

**Referee A-c: symmetric functions, resultants, Hurwitz and Orlando determinants, Newton identities, the Prouhet–Tarry–Escott (PTE) problem and truncated moment problems.**

**Scope.** I refereed:
- Section 3, pp. 18–29: Lemma 3.1; Theorems A, B, C; Lemma 3.3; Theorem 3.4; Corollary 3.5; Theorem 3.8; Corollary 3.9; Section 3.4; Table 2; Figures 2 and 3.
- The Section 1 statements that report these results: Theorems 1.1–1.3 and Corollary 1.5, pp. 4–7.
- What these proofs depend on:
  - Lemmas 2.8 and 2.10, with equations (4), (5), (7) and (8), pp. 10–13.
  - Appendix A, p. 44.
  - Lemma C.1, p. 47, as far as it supports the "Hurwitz" claims.
  - Supplement sections S1 and S7.

I took Proposition 2.7 (Appendix B) as given. I treated the marked placeholders as known.

## 1. Summary

Lemma 2.10 (Uçar's triangular structure, re-derived here from (5)) turns the question into one about multisets. Lemma 3.3 shows that equal $H_L$ is the same as equal area plus equal $\Psi_k=P_{2k-1}-R$ for $k\le L-1$.

The signed multiset $X^*=U^*\uplus(-V^*)$ then has vanishing odd moments up to degree $2L-3$ and vanishing reciprocal sum. From this the paper obtains:
- **Separation** $|X^*|\ge2L+2$ (Theorem 3.4), and from it $K_{\rm mult}\le\lfloor A/\pi\rfloor+4$ (Corollary 3.5).
- **Bounded cone orders (Theorem 3.8):**
  - $M$ invariants suffice within ${\rm Sig}_{\le M}$, by a Vandermonde determinant;
  - $M+1$ suffice against all of Sig, by sign changes;
  - both counts are attained, via Lagrange weights at the nodes $a^2$.
- **A Descartes bound** on the imbalance (Theorem 3.11).
- **Growth (Proposition 3.15).** The minimal configuration size satisfies $N(2L-2)\le T(L)\le4N(2L-3)$. So the growth of $f$ is equivalent, up to constants, to that of the PTE function $N(k)$; unconditionally $\sqrt A\lesssim f(A)\lesssim A$.
- **The algebraic theorems:**
  - Theorem A: injectivity of $\mathcal I_n=(R,P_1,P_3,\dots,P_{2n-3})$.
  - Theorem B: a square linear system, from $\tanh U=zO(z^2)/E(z^2)$, with $\det M=\varsigma_n\,\mathrm{Hur}_{n-1}(\chi_m)/e_n$.
  - Theorem C: the fibres of $n-1$ invariants.

## 2. Significance

**What is good.**
- The section is clean and, as far as I can determine, correct throughout.
- The exact area-free answer $M+1$ (Theorem 3.8(ii)–(iv)) is a nice result.
- The Descartes bound on the imbalance (Theorem 3.11) is a pleasant observation.
- Theorem B is correct in full generality, including repeated orders and signs.
- The authors say plainly which statements rest on computer search, and they call Theorem 1.2 "a reformulation".

**What limits it.**
- After Lemma 2.10, everything is elementary algebra of multisets: Newton's identities, a Vandermonde determinant, the classical sign-change lemma and pigeonhole.
- Theorem 1.2 does not decide the growth of $f$. Its unconditional content is the pair of bounds $\sqrt A\lesssim f(A)\lesssim A$. The rest translates the question, up to constants, into the open problem $N(k)=O(k)$, and does not advance the PTE problem itself.
- The geometric input to this section is a single lemma (2.10). The editor may wish to weigh journal fit; this is not by itself a reason to reject.

## 3. Correctness, and what I recomputed

Everything below was computed in exact arithmetic. Scripts are in `scratch/code/`.

1. **Theorem B, Orlando's formula (11) and Lemma C.1.** I built $M$ and $b$ from the $\tanh U$ series exactly as in (12), for $n=2,\dots,7$. The test multisets were random positive integers, multisets with repeated orders (for example $(8,12,8,22,8)$) and signed rationals.
   - $Me=b$ holds.
   - $\det M=(-1)^{n(n+1)/2}\prod_{i<j}(m_i+m_j)/e_n$ holds.
   - $\mathrm{Hur}_{n-1}(\chi_m)=\prod_{i<j}(m_i+m_j)$ holds in the normalisation $(a_{2j-i})$.
   - $B=YM$ and $\det B=(-1)^{n(n-1)/2}\prod_{i<j}(m_i+m_j)$ hold.
   - I also checked the Jacobian proof by hand, including the triangular form of $J$ and the sign of the cyclic permutation.
2. **Lemmas 2.8 and 2.10.** I computed $p_l$ from (4)–(5) for $l\le8$. In every case:
   - $p_l$ is even, of degree exactly $2l+2$, with leading coefficient $|B_{2l+2}|/(2(l+1)!(2l+1))$;
   - $p_l(1)=0$, and $p_l>0$ at the sampled points $m>1$.

   In addition:
   - $p_0,p_1,p_2$ agree with (8), and $\alpha_0,\dots,\alpha_4$ with the values given.
   - (10) is correct, as are $P_3=-18\tilde c_1-120\tilde c_2-360\tilde c_3$ and $\mathrm{amp}_0,\mathrm{amp}_1,\mathrm{amp}_2=2,14,498$.
3. **Proofs read line by line, with no gap found:** Lemma 3.1; Theorems A and C(1)–(2); Lemma 3.3, including the padding identities; Theorem 3.4; Corollary 3.5; Lemma 3.7; Theorem 3.8(i)–(iv); Corollary 3.9; Theorem 3.11; Proposition 3.12; Theorem 3.13; Lemma 3.16; Lemma A.1; Proposition A.2; Theorem 3.14(a)–(d); Proposition 3.15, both directions of the $o(A)$ statement. The only defects at the level of statements are m3 (a claim in Theorem 3.11) and m4 (a missing hypothesis in Proposition 3.12).
4. **Examples.**
   - Theorem C(3): $R$, $P_1$, $P_3$, $P_5$ are as stated.
   - Example 3.6 and the $M=2$ pair of Theorem 1.1(ii) are correct.
   - Theorem 3.8(ii), for $M=2,\dots,9$: $C$, $\nu$, $s$, the least $g$ and the areas $2\pi\cdot\{2,6,18,190,442,3998,8838,77054\}$ are all correct.
   - Theorem 3.8(ii), for $M\le6$: the pairs share exactly $M-1$ invariants, and $c_M(g;m)-c_M(g';m')=(-1)^MC\,a_{M-2}$ holds exactly.
   - Theorem 3.8(iv): the case $M=2$, $X=4$ is as stated. I also checked $(M,X)=(3,5),(3,7),(4,6)$; each shares exactly $M$ invariants.
   - Example 3.17(i)–(ii) is correct.
5. **Table S1.** All 20 printed pairs check exactly: equal areas, exactly $L$ shared invariants, and the stated $|U^*|+|V^*|$. These reproduce the upper bounds of Table 2. The pieces used in Lemma 3.16 have the stated vanishing odd power sums. I re-derived the Prouhet $L=2$ pair by hand from the recipe in Theorem 3.14(c). The Prouhet rows with $L\ge4$ are given only as a CSV and a hash, so I could not check them.
6. **Remark 3.2.** I ran my own exhaustive search of 4-multisets.
   - Orders up to 84: 9 witnesses, 8 of them primitive, no triples. These 8 are exactly Chen's (A.685)–(A.692), checked against arXiv:2506.11429.
   - Orders up to 130: 19 witnesses, 16 primitive. This matches S1.
   - The count $216{,}071{,}394=\binom{123}{5}$ is correct.
7. **Remark 3.18 and S7(ii).**
   - The partner triple of $\{1,1,1,1,7\}$ is as stated.
   - The count 4,325,115,770 is correct (checked by a Möbius sum).
   - The modular test is sound: the cubic is monic and $p$-integral once $p\nmid3(1-e_1R)$.
8. **Figures.** In Figure 2 (p. 22) every disc and ring is in the right place with the right multiplicity. Figure 3 (p. 29) is consistent with Table S1 and Theorem 3.14(a).
9. **Literature.**
   - The claim that only quadratic upper bounds are known for $N(k)$ agrees with [45, §1] (arXiv:2609.05061).
   - The Chen identities cited are as stated.
   - I could not obtain Borwein–Ingalls [4] to check the pinpoints into it.

## 4. FATAL

None found.

## 5. MAJOR

**M1. The "conditioning" and "Hurwitz matrix" claims overstate what is proved (pp. 4, 5, 19, 40, 47).**
- Page 5 credits Theorem 1.3(i) with "the identification … of the conditioning of the inverse problem with a Hurwitz determinant".
- Page 40 says solving the system "is as well conditioned as the Hurwitz matrix of $\chi_m$".
- What is actually proved:
  - a determinant identity, which locates where the system is singular, not how well conditioned it is;
  - the factorisation $M^{-1}=B^{-1}Y$, which gives only a one-sided bound on the norm of $M^{-1}$.
- The authors themselves note (p. 48) that the bound of Theorem C.2(a) is far from tight: the exact condition number is at most 3.511 on their test multisets.
- The matrix $B$ is not the Hurwitz matrix $(a_{2j-i})$ of (11). Up to column signs, $B^\top$ is rows $2,\dots,n+1$ and columns $1,\dots,n$ of the Hurwitz matrix of order $n+1$. Its determinant does equal $\pm\mathrm{Hur}_{n-1}$ (I checked this).
- *To resolve:* rephrase both sentences to say that $M$ is singular exactly where $\mathrm{Hur}_{n-1}=0$ and that $M^{-1}=B^{-1}Y$, and identify $B$ precisely.

**M2. The correspondence between configurations and pairs of orbifolds is used in proofs but stated only in prose (pp. 24–25, 27, 44).**
- Proposition 3.15, Theorem 3.14(c) and Theorem 3.13 rely on the paragraph on p. 25 ("realised as above"). That paragraph contains several unproved steps:
  - scaling a configuration to coprime integers, with entries equal to 1 serving as padding;
  - the two resulting signatures are distinct (a configuration supported on $\{\pm1\}$ has nonzero reciprocal sum);
  - the genus difference is $\iota/2$;
  - the smaller genus is the least one that makes its side hyperbolic;
  - the area bounds $<2\pi(|W|-2)$, and $\le4\pi$ when $g_0>0$.
- Definition 3.10 also contains a theorem, $|Z|\ge2L+2$, together with a sketch of its proof.
- *To resolve:* add a "Realisation lemma" with a proof covering both directions and the area bounds, and move $|Z|\ge2L+2$ into a lemma.

**M3. Credit the classical tools and keep the "new" claims on p. 7 to what is new (pp. 5, 7, 22, 25, 27).**
- Lemma 3.7 is the classical sign-change lemma (Descartes' rule for Chebyshev systems; Pólya–Szegő Part V, Karlin–Studden) and should be cited as such.
- Theorem B rests on the Routh–Hurwitz–Stieltjes even/odd splitting treated in [42]. The authors should say whether $\det M$ follows from the known relations between Hurwitz minors and Hankel minors; if it does, it is not "new on this side".
- Compare Proposition 3.12 (doubling) with the multiplicative identities in Chen's survey.
- Cite the Frolov–Tarry shift, which gives $N(k+1)\le2N(k)$. It explains the "constant factor" remark and shows $T(L)\asymp N(2L-2)$ within a factor of 4 unconditionally.
- For pairs sharing exactly $L$ invariants, which are exact-degree objects, cite Hua, Wright and Wooley on the exact-degree problem.
- Restrict the "new" list to Theorem 3.8(ii)–(iv), Theorem 3.11, Lemma 3.16 with Proposition 3.15, and Theorem 3.14(c).

## 6. MINOR

- **m1. A computer search can be replaced by a proof (p. 23; S7).** Within ${\rm Sig}_{\le M}$, equal $c_1,\dots,c_{M-1}$ puts $\nu$ in a one-dimensional kernel, so $\nu=t\nu_0$. Common cone points only add area. Hence the minimal pair is $t=\pm1$ at $g^*=\max(0,-s/2)$ whenever this $g^*$ already gives positive area. I checked this for every $M=3,\dots,9$; it fails only for $M=2$. So minimality holds for $M=3,\dots,9$ without any search, and "we claim no minimality for other $M$" can be dropped.
- **m2. Closed form for Theorem 3.8(ii).** $a\,w_a=(-1)^{M-a}\,2a^3/\big((M-a)!\,(M+a)!\big)$, so $\nu(a)\propto(-1)^{M-a}a^3\binom{2M}{M-a}$. For $M=2,\dots,9$ the least $C$ is $3!,\,5!,\,7!/2,\,9!,\,11!/2,\,13!,\,15!/2,\,17!$.
- **m3. Theorem 3.11's last claim is false as stated (p. 25).** It asserts that if $g\neq g'$ and $|U^*|+|V^*|=2L+2$, then $|g-g'|=1$ and $\{|U^*|,|V^*|\}=\{L,L+2\}$.
  - Counterexample: the minimal pair $(0;2,8,8)$, $(0;3,3,12)$ shares $c_1,c_2$, and its cone orders are hyperbolic for every genus. Add $g\ge1$ handles to the first and $g+1$ to the second. The areas still agree, and $\Psi_1$ is unchanged. So $(g;2,8,8)$ and $(g+1;3,3,12)$ share $c_1,c_2$ and differ in genus.
  - For this pair $d=2$, so $U^*=\{1,1,2,8,8\}$ and $V^*=\{3,3,12\}$. Then $|U^*|+|V^*|=8=2L+4$ and the sizes are $\{3,5\}$.
  - The Descartes bound $|\iota|\le|Z|-2L$ itself is correct. The error is in applying it under $|U^*|+|V^*|=2L+2$: since $|\iota|=2|g-g'|\ge2$, the bound gives $2L+2\ge2L+2|g-g'|$, which needs $|g-g'|\le1$. Then $\iota=\pm2$, and $|U^*|+|V^*|=2L+2$ forces $\{|U^*|,|V^*|\}=\{L+2,L\}$. Read this way the statement is fine.
  - What is wrong is the reading the text invites: the hypothesis should be stated as "$|U^*|+|V^*|=2L+2$", the size of the configuration $Z$, not the total cone count.
  - *To resolve:* say explicitly that the hypothesis concerns $|Z|$ and that the conclusion is $|\iota|=2$. The example in this note does not satisfy the hypothesis, so it is not a counterexample to the corrected statement, but it shows the current wording is easy to misapply.
- **m4. Proposition 3.12 needs $L\ge2$ (p. 25).** As stated it is false for $L=1$: take $X=\{1\}$, $Y=\{2\}$. Then $U=\{1,4,4\}$ and $V=\{2,2,2\}$, and neither $(0;4,4)$ nor $(0;2,2,2)$ is hyperbolic. The proof uses $L\ge2$ twice: "$n\ge2$", and "$Y$ has at most one 1", which needs $P_1(X)=P_1(Y)$. Every application has $L\ge2$, so adding the hypothesis is enough.
- **m5. Make the second clause of Theorem 1.2(ii) an equivalence.** If $f(A)\le CA^\alpha$ then, since $A_{\min}(L)<8\pi N(2L-3)$, one gets $N(k)\gtrsim k^{1/\alpha}$. So $f=O(A^\alpha)\iff N(k)=\Omega(k^{1/\alpha})$. Also note the clause is vacuous for $\alpha<\tfrac12$.
- **m6. Proposition 3.15 (p. 27).**
  - The identity $f(A)=1+\max\{L:A_{\min}(L)\le A\}$ needs a convention for $L=1$ and for the empty set.
  - The well-ordering argument should be written out: areas at most $A$ bound $n$ and $g$.
  - Replace "inverse function of $T$" by the explicit inequalities.
- **m7. Rounding.** In Corollary 3.9(a) and Theorem 1.1(iii), use $\lceil(L-1)/2\rceil$.
- **m8. Theorem 3.4 (p. 21).** Its threshold involves the unknown partner. Point out that the form an observer can use is Corollary 3.5.
- **m9. Opening of Section 3 (p. 18).** "Everything here comes from one fact" is overstated: Theorems 3.8(iii) and 3.11 rest on sign changes, not on symmetry.
- **m10. Remark 3.2 (p. 20).** "Pencil of quartics" is defined only in the supplement. Define it in the main text or drop the clause.
- **m11. Table S1.** Print $p$, $q$ or the construction parameters for the Prouhet rows with $L\ge4$, so they can be checked without the deposit.
- **m12. Literature pinpoints.** Re-check "[4, Props. 2–3]" and "Problem 3 of [4, §6]".

## 7. Presentation

- **P1. Label clash.** "Theorem C(3)" (p. 44) and "Theorem C.3" (p. 40) are different results, and "Theorem C(1)" sits alongside "Lemma C.1". Renumber Theorems A–C as Theorems 3.x.
- **P2. Overloaded symbols.**
  - $C$: a constant, a class, the cone sums $C_l$, and $2\sin(\vartheta/2)$.
  - $\kappa$: three different meanings.
  - $a$: nodes, $a_l$, the coefficients $a_k$, and distinct orders. The disclaimer on p. 23 shows the strain.
  - $\nu$: a measure and a multiplicity difference.
  - $V$: a multiset and $V^\pm$.
  - $d$: three different meanings.
  - $s$: three different meanings, and $s_j$ is used where $P_j$ is used elsewhere.
- **P3. Definition 3.10** contains a theorem and its proof.
- **P4. Proof of Theorem B ("Collecting", p. 19).** The sign bookkeeping is too compressed to audit by hand; I could only confirm it by computation. Display $\det\partial_m\mathcal I_n$ with its sign and its row and column order.
- **P5. Figure 2.** Add a colour key (orange appears to be $(3,3,12)$) and a label for the lower row of panel (a).
- **P6. Figure 3.** The genus, equal-count and cone-count diamonds use the same marker, the dots for $s\le7/5$ overprint each other, and there is no legend.

## 8. Recommendation

**Minor revision**, for the part I refereed.
- **Confidence in correctness: high.** Every theorem in scope was either checked line by line or confirmed by independent exact computation. The only false statements, m3 and m4, are matters of wording and hypotheses, not mathematics.
- **Confidence in the assessment of significance: moderate.**
- M1–M3 are about overclaiming, rigour of exposition and attribution, not about errors. They should nevertheless be fixed before acceptance.

## 9. What resolves each issue

| Issue | Resolution |
|---|---|
| M1 | Say "singular exactly where $\mathrm{Hur}_{n-1}=0$" and "$M^{-1}=B^{-1}Y$"; identify $B$; drop the conditioning claim. |
| M2 | Add a Realisation lemma with proof; move $\lvert Z\rvert\ge2L+2$ out of Definition 3.10. |
| M3 | Add citations for the sign-change lemma, Holtz–Tyaglov, Frolov–Tarry, and Hua/Wright/Wooley; trim the "new" list. |
| m1 | Replace the search with the kernel argument; claim minimality for $M=3,\dots,9$. |
| m2 | Give the closed form of $\nu(a)$ and $C$. |
| m3 | State the hypothesis as $\lvert Z\rvert=2L+2$ and the conclusion as $\lvert\iota\rvert=2$. |
| m4 | Add $L\ge2$ to Proposition 3.12. |
| m5 | State the equivalence $f=O(A^\alpha)\iff N(k)=\Omega(k^{1/\alpha})$. |
| m6 | Fix the $L=1$ convention, write out the well-ordering argument, use explicit inequalities. |
| m7–m12 | Ceilings; a pointer to Corollary 3.5; soften the opening sentence; define "pencil"; print the Prouhet data; re-check the pinpoints. |
| P1–P6 | Renumber; de-overload symbols; restructure Definition 3.10; display the determinant with its sign; add colour keys, markers and a legend. |

---

Everything is in `/Users/palaash/Desktop/hyperbolic-pillow/review/referee-round-7/A-c-symmetric-functions-algebraist/scratch/`:
- **Scripts (`code/`):**
  - `thmB.py`: Theorem B, (11), Lemma C.1.
  - `heat.py`, `check_lemmas.py`: Lemmas 2.8 and 2.10, (8).
  - `examples.py`, `tableS1.py`: examples and Table S1.
  - `thm38.py`: Theorem 3.8.
  - `witness4.py`: Remark 3.2.
- **Fetched papers (`lit/`):** the Chen survey and the 2026 preprint by Croot, Mao and Yip.
- **Rendered pages:** `img/`.
