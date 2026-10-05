# C. Algebra and arithmetic citations: word-for-word check, missing literature, Theorem A prior art

Scope: paper/jga/manuscript.tex, the \cite instances of bgn1993, schinzel1996, steinig1971, laurens2023, msw2022, korobovbugaevskaya2016, mueller2016, ostrowski1940, beauville1982, mazur1977 and pari2172 (Task 1); the missing algebra and arithmetic literature named in G7-6 (Task 2); and a classical source for the odd-power-sum fact behind Theorem A (Task 3).

All fetched files are in review/literature-pass/_fetched/{pdf,txt,img,bib}. Page references give the printed page and, where it differs, the PDF page ("pdf p.").

---

## 0. Headline findings

1. **The Theorem 8.9 novelty claim (l. 1426) is false. Remove it.** Schinzel's own proof (Serdica 22 (1996), p. 588, fetched and read) normalizes every rational point to the same sum (x1+x2+x3 = 6) and then clears a common denominator d. This puts k triples at the common sum 6d. That is exactly "normalization by rescaling to a common sum". Schinzel's definition of "primitive" (p. 587) is also word for word the manuscript's. The referee is right, and Schinzel's own text settles it. Zhang–Cai's body text could not be fetched (AMS HTTP 429), but its abstract and Ulas's account (arXiv:1305.6237, p. 1–2) are consistent with this.

2. **There is older prior art for "classes of every size" in the sum–product problem.** Kelly, Proc. AMS 107 (1989) 887–893, proves "There exist infinitely many integers having r partitions into k parts such that the products of the integers in each partition are equal". The proof uses a positive-rank lemma for elliptic curves and cites Mazur. This predates Schinzel, and neither the manuscript nor the referee mentions it.

3. **BGN already have the reciprocation and permutation structure that the manuscript presents without attribution.**
   - BGN p. 117 says "If (x, y, z) is a solution, so is (1/x, 1/y, 1/z). … solutions occur in reciprocal pairs".
   - The table in BGN §4 (p. 120) maps x̄ȳz̄ (x̄ = lcm(x,y,z)/x) to "(σ0, τ0) + (0, 0)", and each permutation to ±P plus a point of order 3 or 6.
   - This is the first statement of Prop. 8.4 (P + T2 = ι(P)) and the content of the paragraph at l. 1364 ("Each transposition … acts … as P ↦ Q − P").
   - The "dual family" of Prop. 8.4 is BGN's reciprocal pairs rescaled to a common sum. The minimal pair is {(1,4,4), reciprocal (4,1,1)} rescaled.
   - The manuscript must credit BGN p. 117 and §4 here.

4. **Theorem A: the classical fact SG describes is real, and a citable statement exists.**
   - Newton's identities give the following: for equal-size multisets A, B, Σa^j = Σb^j for j = 1..k iff deg(∏(x−a) − ∏(x−b)) ≤ n−k−1. This is Borwein–Ingalls, Prop. 1, with the "odd symmetric" form in their §3.
   - Applied to X and −X, it says that the odd power sums of X vanish up to order |X| iff X = −X.
   - So the odd power sums p1, p3, …, p_{2n−1} determine an n-multiset of complex numbers up to insertion or deletion of pairs {a, −a}.
   - Theorem A is this argument with p_{2n−1} replaced by R, plus the remark that ∏(m_i+m_j) ≠ 0 rules out ± pairs inside m. "What is new is the complex case under the sharp condition" overstates this and must be reworded (§4).

5. **Bibliographic errors.**
   - pari2172: the release date is 5 March 2025, not 1 March. The changelog in the official announcement reads "Done for version 2.17.2 (released 05/03/2025)", and the PARI timeline gives "Mar 5 2025: pari-2.17.2-stable released."
   - korobovbugaevskaya2016: the authors are V. I. Korobov and A. N. Bugaevskaya (AMS article page).
   - schinzel1996: add issue no. 4.
   - beauville1982: "singulieres" should be "singulières".
   - steinig1971: the volume is dated 1971 and appeared in 1972; give "4 (1971), 629–644 (1972)".
   - Everything else checks out (§2).

6. **Pinpoints.** All pinpoints that could be reached are ACCURATE:
   - BGN p. 119 and §4;
   - Mazur Cor. (5.2);
   - Ostrowski Théorème XXX and (71, 1);
   - Beauville Théorème and Tableau, row Γ^0_0(6). Beauville defines Γ^0_0(n) = {c ≡ 0, a ≡ 1 mod n}, which is today's Γ1(6). This answers NT m3: the label is Beauville's own notation;
   - Laurens Lemma 3.2 (arXiv v2);
   - MSW Prop. 24 (arXiv v1);
   - Müller et al. Thm 1.4 (arXiv v2).

   The published versions of Laurens (Calc. Var.), MSW (Exp. Math.) and Müller (FoCM) could not be reached (Springer and T&F bot walls), and neither could Korobov–Bugaevskaya (AMS 429), so their numbering in the published versions is unverified.

---

## 1. Citation table (Task 1)

| manuscript line | cite as written | claim the manuscript makes (short) | source location found | verbatim quote | verdict | correction |
|---|---|---|---|---|---|---|
| 158 | \cite{bgn1993} | Beyond 17, degeneracies are rational points on (x+y+z)(xy+yz+zx)=Λxyz "studied by" BGN | BGN p. 117, eq. (2) | "(2) (x+y + z)(yz + zx + xy) = nxyz." (p. 117) | ACCURATE | Optional: "for integer Λ" (BGN treat integer n; the paper uses rational Λ, cf. NT p3). |
| 176 | \cite{steinig1971} | n power sums with distinct exponents determine an n-multiset of positive reals; "goes back to Steinig" | Primary NOT reached. Secondary: Laurens arXiv:2206.09050v2, p. 14 | Laurens p. 14: "In fact, the result in [34] is even more general: it is shown that any n power sums of n distinct positive real numbers has at most one solution (up to permutation), in addition to some generalizations." [34] = "J. Steinig, On some rules of Laguerre's, and systems of equal sums of like powers, Rend. Mat. (6) 4 (1971), 629–644 (1972). MR309867" | CANNOT VERIFY (primary); attribution supported by two secondaries (Laurens; MathOverflow 410757, accepted answer: "From what I can see from the MathSciNet review, that is precisely the content of [1]") | The secondary says "n **distinct** positive real numbers". The manuscript's "n-multiset" (repeated values) goes beyond what is reported for Steinig. Write "n distinct positive reals", and get repeated values from Laurens Cor. 3.3 (odd exponents), as the manuscript's own argument does. |
| 176 | \cite[Lemma~3.2]{laurens2023} | Steinig's result "reported and reproved" in Lemma 3.2 | arXiv:2206.09050v2 (20 Mar 2023), Lemma 3.2, p. 14 (pdf p. 14); remark after it, p. 14; Cor. 3.3, p. 15 | "Lemma 3.2. Fix n ≥ 1. Given constraints e1 , . . . , en , there is at most one choice of N ≤ n and β1 > · · · > βN > 0 so that Em (Qβ,c ) = em for m = 1, . . . , n and any c ∈ RN." Then: "We will follow the clever argument from [34] … However, we will provide a complete and self-contained proof here for future reference (in Corollary 3.3)." | ACCURATE (arXiv v2). Published Calc. Var. 62 (2023) art. 192: CANNOT VERIFY numbering (Springer bot challenge) | Precision: the general Steinig statement is *reported* in the remark after Lemma 3.2. Lemma 3.2 itself proves only the odd exponents 3, 5, …, 2n+1. Suggested: "[Laurens, Lemma 3.2 and the remark following it]". Add "arXiv:2206.09050" to the bib entry so the numbering can be checked. |
| 176 | \cite[Prop.~24]{msw2022} | For positive integer exponents | arXiv:2106.13981v1 (only version), p. 12 (pdf p. 12) | "Proposition 24. For m = n, recovery from p-norms is always unique. Given any set A of n positive integers, the map φA,≥0 : Rn≥0 → Rn≥0 is injective up to permuting coordinates." | ACCURATE (arXiv v1). Published Exp. Math. 33(2) 225–234: CANNOT VERIFY numbering (T&F Cloudflare 403) | Year: Crossref gives published online 2022-04-23 and print 2024 (vol. 33, no. 2). The bib year 2024 is right for the volume; the key "msw2022" is only cosmetic. Since only the arXiv text was checked, cite "arXiv:2106.13981, Prop. 24" or confirm the numbering in the journal. |
| 176 | \cite[\S3, Thm~3.1]{korobovbugaevskaya2016} | Theorem B's system is the odd-power-sum analogue of Newton's identities of KB | AMS article page (abstract only; PDF HTTP 429) | Abstract: "For the system with even power gaps the obtained equalities are the analogs of Newton's identities. These equalities express the connection between elementary symmetric functions and odd power sums." | ACCURATE in substance (abstract). Pinpoint §3 / Thm 3.1: CANNOT VERIFY this pass (AMS 429). The earlier audit (review/audit/literature/THEOREM-A-PRIOR-ART-notes.md §3) quoted Thm 3.1 on p. 727 from a fetched copy. | Re-verify the pinpoint once AMS is reachable. Bib: initials "V. I. Korobov and A. N. Bugaevskaya" (AMS page). |
| 176 | \cite[Thm~1.4]{mueller2016} | Sign-vector criteria concern injectivity on the whole orthant for every coefficient scaling | arXiv:1311.5493v2 (30 Oct 2014, "To appear in FoCM"), Thm 1.4, p. 3 | "Theorem 1.4. Let fκ : Rn+ → Rm be the generalized polynomial map fκ (x) = Aκ xB … The following statements are equivalent: (inj) fκ is injective with respect to S, for all κ ∈ Rr+ . (jac) ker (Jfκ (x)) ∩ S ∗ = ∅, for all κ ∈ Rr+ and x ∈ Rn+ . …" | ACCURATE (arXiv v2). FoCM numbering: CANNOT VERIFY (Springer bot challenge) | None, apart from confirming the FoCM numbering. MSW's own reference to it (arXiv p. 12 ff., ref. [12]) uses "[12, Theorem 1.4]" for the FoCM paper, which is indirect support that the number is unchanged. |
| 418 | \cite[\S3]{korobovbugaevskaya2016} | Same as above | as above | as above | ACCURATE in substance; pinpoint CANNOT VERIFY this pass | as above |
| 1035 | \cite{bgn1993} | C_Λ is "the one studied by BGN … for integer Λ" | BGN p. 117, (1)–(2) | "Melvyn J. Knight has asked which integers n can be represented as (1) n = (x + y + z)(1/x + 1/y + 1/z) … Rewrite (1) as (2) (x+y + z)(yz + zx + xy) = nxyz." | ACCURATE | — |
| 1042 | \cite{pari2172} | PARI/GP 2.17.2 ellrank returns r1 = r2 = 0; r2 comes from a 2-Selmer group without unproved hypothesis | PARI refcard-ell 2.17.2; PARI docs (html-stable), ellrank | refcard-ell, header "(PARI-GP version 2.17.2)", lists "attempt to compute E(Q) ellrank(E, {effort}, {points})" and "torsion subgroup with generators elltors(E)". Doc: "The output is [r1, r2, s, L], where r1 ≤ rank(E) ≤ r2 … The algorithm computes unconditionally three quantities: * the rank C of the 2-Selmer group. * the rank T of the 2-torsion subgroup. * the (even) rank s of G[2]/2G[4]; then r2 is defined by r2 = C − T − s." | ACCURATE (functions exist in 2.17.2; r2 unconditional). The html-stable page carries no version string, so it describes the current stable branch. | Optional: the doc says r2 is unconditional in general, so "since E has a rational 2-torsion point no conditional step is used" is harmless but not what makes it unconditional. |
| 1136 | \cite[Th\'eor\`eme~XXX, (71,1)]{ostrowski1940} | For monic f, g of degree n, after renumbering, \|y_ν − x_ν\| ≤ (2n−1)ε, with ε built from coefficient differences weighted by powers of γ, the largest root modulus | Acta Math. 72, No. 69–71: (69,4) p. 210 (pdf p. 54); (71,1) and Thm XXX p. 212 (pdf p. 56); checked against page images | p. 210: "Soit γ = Max (\|x_ν\|, \|y_ν\|) et (69, 4) ε = ⁿ√(Σ_{ν=0}^{n−1} \|a_ν − b_ν\| γ^ν)." p. 212: "(71, 1) \|y_ν − x_ν\| ≦ (2n − 1) ε ≦ (2n − 1) M δ^{1/n} < 4 n T δ^{1/n}, ν = 1, …, n. XXX. Soient (69, 1) deux équations algébriques aux racines x_ν, ν = 1, …, n et y_ν, ν = 1, …, n. Alors on a, en numérotant les x_ν et y_ν convenablement, la relation (71, 1) où ε est defini par (69, 4), δ par (69, 6) et M par (69, 2), (69, 8)." | ACCURATE | None. Note Ostrowski assumes n > 1 ("Soient pour n > 1, a0 = 1, b0 = 1", p. 209) and monic polynomials. The index in (69,3)–(69,4) is printed against a_ν multiplying z^{n−ν}; the manuscript's paraphrase "weighted by powers of γ" avoids the issue. |
| 1336 | \cite{bgn1993} | BGN studied the curve "for integer Λ as the set of solutions of Λ = (x+y+z)(1/x+1/y+1/z)" | BGN p. 117 | as at l. 1035 | ACCURATE | — |
| 1339 | \cite[Th\'eor\`eme and Tableau]{beauville1982} | The pencil (X+Y)(Y+Z)(Z+X)+νXYZ is in row Γ^0_0(6) of Beauville's table | C. R. Acad. Sci. Paris 294 (24 mai 1982), Série I: definitions p. 657 (pdf p. 2), Théorème and Tableau p. 658 (pdf p. 3); page images read | p. 657: "Γ^0_0(n) = { (a b; c d) ∈ SL2(Z) \| c ≡ 0, a ≡ 1 (mod. n) }". p. 658: "THÉORÈME. — Soit f : X → P1 une famille semi-stable de courbes elliptiques admettant quatre fibres singulières. Alors f est isomorphe à la famille modulaire associée à l'un des six sous-groupes Γ ci-dessous; celle-ci s'identifie à la famille déduite du pinceau de cubiques correspondant à Γ dans la liste suivante". TABLEAU row: "Γ^0_0(6) …… (X+Y)(Y+Z)(Z+X)+tXYZ=0 …… 6, 3, 2, 1" | ACCURATE (label and pencil as printed; fibre components 6, 3, 2, 1 match I6, I3, I2, I1) | Recommended addition, which answers NT m3: "(Beauville's Γ^0_0(6) = Γ1(6) in current notation)". The Schoen 2008 table (arXiv:0804.1078, Table 4.1) independently lists level 6: "(x+y)(y+z)(z+x)+txyz (1:−1:0) I1 I2 I3 I6 −8,1,0,∞", consistent with ν = 1−Λ (ν = −8 ↔ Λ = 9 I1, ν = 0 ↔ Λ = 1 I3, ν = 1 ↔ Λ = 0 I2, ν = ∞ ↔ Λ = ∞ I6). |
| 1343 | \cite{bgn1993} | The model η² = s(s² + (Λ²−6Λ−3)s + 16Λ) is BGN's with n = Λ | BGN p. 118, (6)–(7) | "(6) τ² = σ(σ² + (n² − 6n − 3)σ + 16n), … (7) σ = −4(yz + zx + xy)/z²" | ACCURATE | — |
| 1350 | \cite[p.~119]{bgn1993} | BGN call the component the egg; just the odd multiples of P on the egg give positive solutions | BGN p. 118 ("egg") and p. 119 (pdf p. 3) | p. 118: "Geometrically, the curve (6) has two components, an "egg" for values σ < 0, and an infinite branch when σ > 0." p. 119: "If P is on the egg, then just the odd multiples of P give positive solutions." | ACCURATE | Cite "pp. 118–119" (the name is on p. 118). BGN state this for integer n. Their argument (positive ⇔ n > 0, σ < 0) works verbatim for rational Λ > 9, and the manuscript uses it at Λ = 155/12, so it should say so in one clause. |
| 1364 | \cite[\S4]{bgn1993} | Torsion of C_Λ(Q) is exactly the cyclic group of base points for every integer Λ ≠ 10 | BGN §4, pp. 119–120 | p. 119: "We assume that the curve is nonsingular, i.e., n ≠ 0, 1 or 9." p. 120: "In all cases except n = 10, therefore, the torsion group is Z/6Z. n = 10: … the torsion group is isomorphic to Z/2Z × Z/6Z." | ACCURATE, with BGN's standing hypothesis | Write "every integer Λ ∉ {0, 1, 9, 10}" (BGN exclude the singular n = 0, 1, 9). Also add the BGN §4 credit for the permutation/reciprocal table (finding 3). |
| 1364 | \cite[Cor.~(5.2)]{mazur1977} | Mazur's theorem: no point of P'∓P of order ≤ 12 ⇒ infinite order | Publ. IHÉS 47, Chap. III §5, p. 156 (pdf p. 125) | "Corollary (5.2). — Let an elliptic curve, defined over Q, possess a point of order m rational over Q. Then m ≤ 10 or m = 12." | ACCURATE | — (The equivalent statement is also Theorem (7′) of the Introduction, p. 35.) |
| 1423 | \cite[Cor.~(5.2)]{mazur1977} | Bounds the order of a rational torsion point by 12 | as above | as above | ACCURATE | — |
| 1423 | \cite[p.~119]{bgn1993} | Odd multiples (2j+1)P on the egg are positive points | BGN p. 119 | as at l. 1350 | ACCURATE (with the rational-Λ remark) | as at l. 1350 |
| 1426 | \cite{schinzel1996} | "The method is Schinzel's, who solved the analogous problem for equal sum and equal product through a point of infinite order on a fixed cubic; what is new is the normalization by rescaling to a common sum" | Serdica Math. J. 22 (1996), Theorem p. 587, Lemma pp. 587–588, proof of Theorem p. 588 | p. 587: "In this paper we solve the problem D.16 from the book [1] by proving the following Theorem. For every k there exist infinitely many primitive sets of k triples of positive integers with the same sum and the same product. (A set S of triples is called primitive if the greatest common divisor of all elements of all triples of S is 1.) Lemma. The system of equations (1) x1 + x2 + x3 = x1 x2 x3 = 6 has infinitely many solutions in rational numbers xj > 0." p. 588: "P r o o f o f t h e t h e o r e m. Take any k solutions ⟨xi1, xi2, xi3⟩ … of the system (1) in rational numbers xj > 0 and let d be the least common denominator of all the numbers xij … Thus xij = aij/d … We have (2) Σ_j aij = 6d, Π_j aij = 6d³ (i ≤ k), hence g.c.d. aij = 1." | First half ACCURATE (the Lemma's proof uses the point ⟨7,17⟩ on y² = x³ − 9x + 9 failing Nagell's condition, then Poincaré–Hurwitz density). **Second half NEEDS CORRECTION.** | Schinzel's normalization x1+x2+x3 = 6, followed by a common denominator, *is* rescaling to a common sum. The manuscript's "primitive" is Schinzel's definition word for word. Replace with: "The argument is Schinzel's [schinzel1996, p. 588], transplanted to C_Λ: put infinitely many positive rational points on a fixed curve and rescale k of them to a common sum. For equal sum and equal product, classes of every size were first obtained by Kelly [kelly1989] and, for n-tuples, by Zhang and Cai [zhangcai2013]." |
| 1426 | \cite{pari2172} | C_{155/12} has rank 2, r1 = r2 = 2 | as at l. 1042 | as at l. 1042 | ACCURATE (tool exists; conditional-free upper bound) | — |
| 1575 | \cite{pari2172} | PARI/GP 2.17.2 via cypari2; output formats of ellrank and elltors | refcard 2.17.2; ellrank doc | ellrank output "[r1, r2, s, L]" matches the printed "[0,0,0,[]]" | ACCURATE | Bib date (see §2). |

---

## 2. Bibliographic record check (references.bib vs fetched records)

| key | fetched record (file; source URL) | discrepancy | action |
|---|---|---|---|
| bgn1993 | bib/bgn1993.bib (https://doi.org/10.1090/s0025-5718-1993-1189516-5, Crossref content negotiation); bib/bgn1993.crossref.json; bib/bgn1993.zbmath.json (Zbl 0808.11022) | none (authors, title, Math. Comp. 61 no. 203, 117–130, 1993) | — |
| schinzel1996 | bib/schinzel1996.zbmath.json (api.zbmath.org, an:0932.11019); the PDF itself (http://www.math.bas.bg/serdica/1996/1996-587-588.pdf) | The PDF heading is "Serdica Math. J. 22 (1996), 587-588"; zbMATH adds "No. 4". The zbMATH title has a typo ("product product"); the PDF title is "Triples of positive integers with the same sum and the same product", as in the bib. | Add number = {4}. No DOI. (zbMATH BibTeX endpoint zbmath.org/bibtex/… returns a Cloudflare challenge, so the raw record is the API JSON.) |
| steinig1971 | bib/steinig1971.zbmath.json (an:0238.10007): "Rend. Mat., VI. Ser. 4(1971), 629-644 (1972)", author "Steinig, John", no review | The bib year is 1971 and zbMATH gives year 1972 (appearance). | Write year = 1971 with note "(1972)", as Laurens and MR309867 do. |
| laurens2023 | bib/laurens2023.bib (doi 10.1007/s00526-023-02534-2); bib/laurens2023.crossref.json; bib/laurens2023.arxiv.xml | none (Calc. Var. PDE 62 (2023) no. 7, article 192; online 10 Jul 2023) | Add eprint arXiv:2206.09050, since the pinpoint was checked there. |
| msw2022 | bib/msw2022.bib (doi 10.1080/10586458.2022.2061650); crossref.json; msw2022.arxiv.xml | Crossref: online 2022-04-23, print 2024 (33(2), 225–234). Bib year 2024 is right for the volume. | Keep 2024. Renaming the key is optional. Add the arXiv id. |
| korobovbugaevskaya2016 | bib/korobovbugaevskaya2016.bib (doi 10.1090/mcom/2994): author={Korobov, V. and Bugaevskaya, A.}; AMS article page (txt/korobov2016_ams.txt): "V. I. Korobov", "A. N. Bugaevskaya"; "Published electronically: June 26, 2015"; "Math. Comp. 85 (2016), 7[17–736]" | The bib has "V." and "A." only. | Use "Korobov, V. I. and Bugaevskaya, A. N." Year 2016 is right for vol. 85. |
| mueller2016 | bib/mueller2016.bib (doi 10.1007/s10208-014-9239-3); crossref.json: online 2015-01-06, print 2016-02, 16(1) 69–97 | none | Optional: add arXiv:1311.5493. |
| ostrowski1940 | bib/ostrowski1940.bib (doi 10.1007/bf02546330) | none (Acta Math. 72 (1940) 157–257, the second part of the memoir) | — |
| beauville1982 | bib/beauville1982.zbmath.json (an:0504.14016); PDF scan (Gallica reproduction) p. 657 | Bib title "…fibres singulieres"; the print has "singulières". zbMATH journal: "C. R. Acad. Sci., Paris, Sér. I 294, 657-660 (1982)". | Fix the accent. No DOI. |
| mazur1977 | bib/mazur1977.bib (doi 10.1007/bf02684339) | none (Publ. Math. IHÉS 47 (1977) 33–186) | — |
| pari2172 | Raw records: txt/pari_announce_2.17.2.html (https://pari.math.u-bordeaux.fr/archives/pari-announce-25/msg00001.html), txt/pari_timeline.html (https://pari.math.u-bordeaux.fr/timeline.html). No DOI or Crossref/zbMATH record exists, so no BibTeX could be fetched. | Announcement (B. Allombert, "Wed, 5 Mar 2025 19:23:55 +0100"): "I would like to announce the release of pari-2.17.2 (STABLE)" … "Done for version 2.17.2 (released 05/03/2025):". Timeline: "Mar 5 2025: pari-2.17.2 -stable released." | **NEEDS CORRECTION:** "released 5 March 2025". 2.17.3 has since been released (pari-announce-25 index), which is harmless because the version used is stated. |

---

## 3. Instrument gaps

| item | URLs tried | result |
|---|---|---|
| Steinig 1971 full text | zbMATH API (record, no review); zbmath.org/bibtex (Cloudflare challenge); Rend. Mat. archive www1.mat.uniroma1.it/ricerca/rendiconti/ (connection failed, curl code 000); web search (no scan found); MathSciNet MR309867 review (subscription, not attempted) | Standing gap. Known only through Laurens p. 14 and MO 410757. |
| Drury–Marshall 1987 §3 (the source of the Steinig argument per MO/Laurens) | Unpaywall 10.1017/s0305004100066901 | is_oa false; not fetched |
| Korobov–Bugaevskaya PDF | www.ams.org/journals/mcom/2016-85-298/S0025-5718-2015-02994-9/…pdf; pubs.ams.org mirror; www.ams.org/mcom/… (S2 OA URL); archive.org wayback | HTTP 429 repeatedly (retry loop, 6+ attempts over about 15 min). The article HTML page (abstract, authors) was fetched (200). |
| Zhang–Cai 2013 PDF | ams.org and pubs.ams.org PDF URLs | HTTP 429. HTML article page fetched (abstract, references, dates). |
| Kelly 1964 PDF | ams.org PDF URL | HTTP 429. HTML page fetched (bibliographic data only; no abstract in 1964). Content known only via Cha et al. (arXiv:1811.07451, Thm 1.1). |
| Kelly 1989 PDF | not attempted separately (same host); HTML article page fetched (abstract) | abstract only |
| Laurens, published version | link.springer.com/content/pdf/10.1007/s00526-023-02534-2.pdf | 200, but the body is a bot-challenge HTML page; Unpaywall and S2 say closed |
| MSW, published version | tandfonline.com/doi/pdf/… (403 Cloudflare); WebFetch …/doi/full/… (403) | not reached (S2 says hybrid OA CC-BY, but the host blocks) |
| Müller et al., FoCM | link.springer.com/content/pdf/10.1007/s10208-014-9239-3.pdf | bot-challenge HTML |
| Beauville via Gallica | gallica.bnf.fr/ark:/12148/bpt6k5533029f/texteBrut | 200 security-check page (curl); 403 (WebFetch). Obtained instead the Gallica reproduction hosted at https://people.math.ethz.ch/~kowalski/beauville-familles-stables.pdf (200; Gallica cover page plus pp. 657–661). |
| Guy, Unsolved Problems, D16 (3rd ed. 2004; 2nd ed. 1994) | archive.org unsolvedproblems0003guyr (_djvu.txt 403; fulltext/inside.php 403); unsolvedproblems0000guyr (401) | lending-restricted. D16's subject is known only from Schinzel p. 587 ("we solve the problem D.16 from the book [1]", [1] = 2nd ed. 1994). |
| Schoen 1988 (Math. Z. 197) | Springer (closed); EuDML 183725 (403); GDZ search (404) | Not reached. Secondary: Schoen 2008, arXiv:0804.1078 §13: "A number of rigid threefolds with trivial canonical sheaf may be constructed as fiber products of rational semi-stable elliptic surfaces [Schü] and [Sch2, §7]", where [Sch2] = Schoen 1988. |
| Borwein–Ingalls, published Enseign. Math. 40 (1994) 3–27 | e-periodica search (400) | Read the authors' preprint (CECM P98.pdf, dated December 13, 1993) from page images. Numbering in the published version is unverified. |
| Macdonald, Symmetric Functions, Ch. III §8; Pragacz 1991 Thm 2.11 | archive.org symmetricfunctio0000macd (lending item, not attempted after the Guy 401/403); Springer LNM (closed) | Known through Daugherty–Ram–Virk (arXiv:1105.4207, §4). |
| Zieve, "A remark on the paper …" (cited by Ulas as "Math. Comp. to appear") | Crossref author search (no hit) | Not located; may never have been published. |
| PARI users' manual 2.17.2 | /pub/pari/manuals/2.17.2/users.pdf | 200 but truncated (544 kB, broken xref) on two attempts. refcard-ell 2.17.2 used instead. |
| zbMATH BibTeX | zbmath.org/bibtex/<id>.bib | Cloudflare challenge. The api.zbmath.org JSON was saved as the raw record. |

---

## 4. Theorem A: the classical fact and how to recalibrate (Task 3)

**The classical fact (SG's point) is correct.** For n-multisets m, m′ of complex numbers, P_j(m) = P_j(m′) for all odd j ≤ 2n−1 iff X = m ⊎ (−m′) satisfies X = −X. Equivalently, m and m′ agree after deleting from each its pairs {a, −a}. The manuscript's own proof of Theorem A is this argument verbatim (Lemma "parity" plus the evenness of Q(z)).

**Citable sources found**

1. **Borwein–Ingalls, "The Prouhet–Tarry–Escott problem revisited"**, Enseign. Math. (2) 40 (1994) 3–27 (Zbl 0810.11016). Read in the authors' preprint, p. 3, §2:
   > "The problem can be stated in three equivalent ways. This is an old result as are most of the results of this section in some form or another. (See for example [7], [11].) … Proposition 1 The following are equivalent Σ_{i=1}^n α_i^j = Σ_{i=1}^n β_i^j for j = 1, …, k (1); deg(∏_{i=1}^n (x − α_i) − ∏_{i=1}^n (x − β_i)) ≤ n − (k+1) (2); (x − 1)^{k+1} | Σ x^{α_i} − Σ x^{β_i} (3). Proof. An application of Newton's symmetric polynomial identities shows the equivalence of (1) and (2)."

   §3, p. 6, on the odd case:
   > "An odd ideal symmetric solution of size k + 1 and even degree k is of the form {α_1, …, α_{k+1}}, {−α_1, …, −α_{k+1}} and satisfies any of the following equivalent statements Σ_{i=1}^{k+1} α_i^j = 0 for j = 1, 3, 5, …, k − 1; ∏(x − α_i) − ∏(x + α_i) = C for some constant C; …"

   Apply Prop. 1 (1) ⇔ (2) with β = −α. Even power sums then agree automatically. Taking k = |X| gives: all odd power sums of X up to order |X| vanish ⇔ ∏(x − α) = ∏(x + α) ⇔ X = −X. Borwein–Ingalls state it for integers, but the proof is Newton's identities and holds over any field of characteristic 0. Their "[11]" is Hua's book and "[7]" is Dorwart–Brown. The proposition is also the classical framework for the manuscript's Problem 2 ("a Prouhet–Tarry–Escott system in odd powers") and Theorem C(1), which are exactly "symmetric" PTE systems in Borwein–Ingalls' sense. Cite them there.

2. **Schur Q-function theory (statement through a secondary source only).** Daugherty–Ram–Virk, arXiv:1105.4207, §4:
   > "the ring of symmetric functions in y1, …, yk with the Q-cancellation property of Pragacz. By [Pr, Theorem 2.11(Q)], this is the same ring as the ring generated by the odd power sums",

   where [Pr] = Pragacz, "Algebro-geometric applications of Schur S- and Q-polynomials", LNM 1478 (1991) 130–191. MathOverflow 212800 states the Q-cancellation property as f(x1, −x1, x2, x3, …) = f(x2, x3, …). This is the symmetric-function form: polynomials in odd power sums cannot distinguish multisets that differ by ± pairs, and they generate all functions with that property (Macdonald, Ch. III §8). The primary sources (Pragacz Thm 2.11; Macdonald III.8) were not reached. Cite them only after checking, or cite Borwein–Ingalls Prop. 1 alone.

3. Related, but not the needed statement: Korobov–Bugaevskaya (abstract) give the Newton-type identities between e_k and odd power sums. MSW Remark 9 (arXiv p. 4) notes, for odd exponents, that the projective scheme "contains the lines defined by xi = −xj, xk = −xl, x0 = 0", which is the ± pair degeneracy, observed but not stated as a theorem.

**Assessment of the manuscript's claim (l. 176):** "What is new here is the complex case under the sharp condition ∏(m_i+m_j) ≠ 0, the closed form of the determinant, and the sharpness statements of Theorem C."
- The complex injectivity is the classical parity fact with one modification. P_{2n−1} is replaced by R, which works because e_{2n−1}(X) = e_{2n}(X)·Σ1/x. The hypothesis ∏(m_i+m_j) ≠ 0 is exactly the absence of ± pairs within m. Its sharpness (replace a pair {a, −a} by {b, −b}) is the classical non-uniqueness.
- So the complex case is not a new phenomenon. The genuinely new items are:
  - (i) replacing the top odd power sum by R, which is what the heat invariants supply;
  - (ii) Theorem B's determinant det M = ς_n ∏(m_i+m_j)/∏m_i, i.e. the linear system's singular locus is the Orlando locus;
  - (iii) Theorem C.

**Suggested replacement sentence:**
> "For complex multisets the mechanism is classical: by Newton's identities, n-multisets m, m′ ⊂ ℂ have equal odd power sums P_1, …, P_{2n−1} if and only if m ⊎ (−m′) is symmetric under x ↦ −x, i.e. m and m′ agree after deleting pairs {a, −a} (the symmetric form of the Prouhet–Tarry–Escott problem [Borwein–Ingalls, Prop. 1 and §3]). Theorem A replaces P_{2n−1} by the reciprocal sum R, which is the quantity the heat invariants provide, and the condition ∏_{i<j}(m_i+m_j) ≠ 0 excludes such pairs in m. What is new is this replacement, the closed form of the determinant in Theorem B, and the sharpness statements of Theorem C."

Also soften l. 405 ("The hypothesis is sharp over ℂ …") with "as in the classical case".

---

## 5. Missing literature (Task 2)

Relation codes: (Sig) signature count / no uniform count; (Thr) rigid threshold and isolation; (Stab) stability; (Loc) locality.

### 5.1 Schinzel 1996 (already cited)
- **Reference:** A. Schinzel, Triples of positive integers with the same sum and the same product, Serdica Math. J. 22 (1996), no. 4, 587–588. Zbl 0932.11019. PDF: http://www.math.bas.bg/serdica/1996/1996-587-588.pdf (fetched).
- **Proves:** see the table row at l. 1426.
- **Relation:** Thm 8.9 (Thr/§8) is Schinzel's argument applied to C_{155/12}; the definition of "primitive" is also his. Sig, Stab, Loc: none.
- **Where to cite:** l. 1426 (rewrite), the "primitive" definition at l. 1324, and §1 (l. 158).
- **Changes a novelty claim:** YES. Delete "what is new is the normalization by rescaling …".

### 5.2 Kelly 1964 and Kelly 1989
- **References:**
  - J. B. Kelly, Partitions with equal products, Proc. Amer. Math. Soc. 15 (1964) 987–990, doi 10.1090/S0002-9939-1964-0168542-2. bib/kelly1964.bib (Crossref); Zbl 0144.25201.
  - J. B. Kelly, Partitions with equal products. II, Proc. Amer. Math. Soc. 107 (1989) 887–893, doi 10.1090/S0002-9939-1989-0984800-0. bib/kelly1989.bib.
- **Proves:**
  - 1964 (secondary only: Cha et al., Int. J. Number Theory 15 (2019) 1731–1744, arXiv:1811.07451, p. 2): "Theorem 1.1 ([2]). For every integer n ≥ 3, s_{n−1}(n) and s*_{n−1}(n) exist. Furthermore, s_2(3) = 23 and s*_2(3) = 19." Here s*_r(n) is the least s such that every s′ ≥ s has at least r n-partitions with a common product (Motzkin's conjecture).
  - 1989 (AMS abstract, verbatim): "The following theorem is proved: Let k ≥ 3 and r be positive integers. There exist infinitely many integers having r partitions into k parts such that the products of the integers in each partition are equal. Moreover, these partitions are mutually disjoint, i.e., no integer occurs in more than one of them. Of some additional interest is a lemma stating that a certain class of elliptic curves has positive rank over Q." Its references include Mazur 1977 and Mazur 1978.
- **Relation:**
  - Kelly 1989 is the first "classes of every size" theorem for the sum–product analogue, proved with positive-rank elliptic curves. Thm 8.9 is its (sum, reciprocal sum) counterpart.
  - Kelly 1964 is the analogue of asking whether every sufficiently large sum carries a class. The manuscript only reports "507 of the 582 sums 19 ≤ S ≤ 600 carry one" (l. 1448, §8.4 "Growth"). Kelly's s*_2(3) = 19 invites the same question for (S, R) and could be posed as an open problem.
- **Where to cite:** §8.3 next to Schinzel; §8.4 near the per-sum statement.
- **Changes a novelty claim:** Yes, it reinforces the Thm 8.9 correction.

### 5.3 Zhang–Cai 2013
- **Reference:** Yong Zhang and Tianxin Cai, n-tuples of positive integers with the same sum and the same product, Math. Comp. 82 (2013), no. 281, 617–623; published electronically May 8, 2012; doi 10.1090/S0025-5718-2012-02609-3. bib/zhangcai2013.bib; Zbl 1275.11058.
- **Proves (abstract, verbatim):** "In this paper, by using the theory of elliptic curves, we prove that for every k, there exists infinitely many primitive sets of k n-tuples of positive integers with the same sum and the same product."
- **Method (secondary, Ulas, arXiv:1305.6237, p. 1):** "They obtained this result by proving that the system (1) σ1(x1, …, xn) = a, σn(x1, …, xn) = b, with a = b = 2n has infinitely many rational solutions." Also p. 2: "We also should note that the result from [9] follows from Schinzel's work. This was noted by Zieve in [10]."
- **Body text:** NOT read (AMS 429).
- **Is the referee right that Thm 8.9's "new" step is Schinzel's step as presented by Zhang–Cai?** Yes. The decisive evidence is Schinzel's own proof (p. 588), quoted above. ZC's normalization σ1 = σn = 2n is Schinzel's x1+x2+x3 = x1x2x3 = 6 for general n.
- **Relation:** Thr/§8 only.
- **Where to cite:** l. 1426.
- **Changes a novelty claim:** yes, as in 5.1.

### 5.4 Guy, Unsolved Problems in Number Theory, D16
- **Reference:** R. K. Guy, Unsolved Problems in Number Theory, 3rd ed., Springer, 2004, doi 10.1007/978-0-387-26677-0. bib/guy2004.bib.
- **Content:** NOT read (gap). Schinzel p. 587: "In this paper we solve the problem D.16 from the book [1]", where [1] is the 2nd ed. (1994). So D16 concerns triples with the same sum and the same product.
- **Where to cite:** §8 introduction, as the source of the sum–product problem. Check the 3rd-edition wording before quoting.

### 5.5 Bremner–Guy 1997
- **Reference:** A. Bremner and R. K. Guy, Two more representation problems, Proc. Edinburgh Math. Soc. 40 (1997) 1–17, doi 10.1017/S0013091500023397 (OA, fetched). bib/bremnerguy1997.bib.
- **Proves (abstract, p. 1, verbatim):** "We discuss the problem of finding those integers which may be represented by (x + y + z)³/xyz, and also those which may be represented by x/y + y/z + z/x, where x, y, z are integers." Introduction, p. 1: "In [2] we discussed Melvyn Knight's problem of finding those integers representable in the form n = (x + y + z)(1/x + 1/y + 1/z)", where [2] = BGN.
- **Relation:**
  - (x+y+z)³/xyz = e1³/e3 is the scale-invariant of the same-sum-same-product problem, just as Λ = e1e2/e3 is for (S, R).
  - So Bremner–Guy 1997 is the sum–product companion of BGN, and Schinzel's curve is the fibre e1³/e3 = 36 of their family.
  - This is the cleanest way to say why Schinzel's method transfers.
- **Where to cite:** §8.1, after Prop. 8.1.
- **Changes a novelty claim:** no.

### 5.6 Sadek–El-Sissi 2015
- **Reference:** M. Sadek and N. El-Sissi, Partitions with equal products and elliptic curves, Osaka J. Math. 52 (2015), no. 2, 515–525. PDF (VoR) https://ir.library.osaka-u.ac.jp/repo/ouka/all/57678/ojm52_02_515.pdf (fetched). JaLC doi 10.18910/57678 (Crossref and content negotiation fail: 404/406). Raw record: bib/sadekelsissi2015.arxiv.xml (arXiv:1303.6705, journal_ref "Osaka J. Math., Volume 52, Number 2, 2015, 515-525").
- **Proves (Theorem 2.8, p. 520; verbatim from the text layer):** "Let M, N be integers such that M can be written as a sum of three positive rational numbers d1 > d2 > d3 whose product is N. Assume moreover that N³(M³ − 27N) ≠ 0 and d1(d2 − d3)³ ≠ d3(d1 − d2)³. The Mordell–Weil group of the elliptic curve E(M,N): y² − Mxy − Ny = x³ satisfies E(M,N)(Q) ≅ Z^r × E(M,N)(Q)_tor, r ≥ 1, where E(M,N)(Q)_tor ≅ Z/3Z if #S(M,N) = 0, Z/6Z if #S(M,N) = 1, Z/2Z × Z/6Z if #S(M,N) = 2." In the proof: "the only points of finite order (x : y : z) are the ones corresponding to triples of the form (a, a, b), a ≠ b, … or the ones with at least one of the entries being zero." Abstract: "Furthermore there are infinitely many positive integers M that can be written in n different ways, n ∈ {2, 3}, as the sum of three distinct positive integers with the same product N and E(M,N)(Q) has rank at least n."
- **Relation:** This is the exact sum–product analogue of Remark 8.6 ("Isosceles triples are torsion") and of the torsion/rank dichotomy in §8.1. The same torsion groups Z/6 and Z/2×Z/6 occur.
- **Where to cite:** Remark 8.6, and the Mazur paragraph at l. 1364.
- **Changes a novelty claim:** It removes the impression that "isosceles = torsion" is a new phenomenon. The manuscript does not claim it as new, but should give the parallel.

### 5.7 BGN 1993 (already cited; additional content that must be credited)
- p. 117: "If (x, y, z) is a solution, so is any permutation. So is (kx, ky, kz) for any k. … If (x, y, z) is a solution, so is (1/x, 1/y, 1/z). Indeed, (2) is quadratic in x, y and z, and solutions occur in reciprocal pairs".
- §4, p. 120: "The relationships between the permutations and reciprocals of a solution (x, y, z) and the points on the curve (6) are exhibited in the following table, where x̄ = lcm(x, y, z)/x, etc." The table gives x̄ȳz̄ ↦ "(σ0, τ0) + (0, 0)" and yzx ↦ "(σ0, τ0) + (4, −4(n−1))", etc.
- **Relation:**
  - This is the first assertion of Prop. 8.4 (P + T2 = ι(P), with T2 of order 2) and the permutation paragraph at l. 1364.
  - The dual family (Prop. 8.4) is BGN's reciprocal pair, rescaled to a common sum (Schinzel's step again).
  - The isosceles family D_{u,v} (Thm 8.5) is the special case x = (u, v, v), whose reciprocal is proportional to (v, u, u).
  - The minimal pair is x = (1, 4, 4).
- **Where to cite:** Prop. 8.4 (statement, or the sentence before it), l. 1364, and Thm 8.5.
- **Changes a novelty claim:** The manuscript does not explicitly claim Prop. 8.4 as new, but presents it without attribution. Attribution is needed.

### 5.8 Later work on (x+y+z)(1/x+1/y+1/z) = n (forward citations of BGN; OpenAlex cites:W2038008829 gives 12 works, zbMATH ci:0808.11022 gives 2)
- **Nguyen Xuan Tho**, What positive integers n can be presented in the form n = (x+y+z)(1/x+1/y+1/z)?, Ann. Math. Inform. 54 (2021) 141–146, doi 10.33039/ami.2021.04.005 (fetched). Crossref gives the volume as "Accepted manuscript", which is a Crossref error; the PDF says 54, pp. 141–146.
  - Theorem 1.1, p. 142: "Let n be a positive integer. Then equation (x + y + z)(1/x + 1/y + 1/z) = n does not have positive integer solutions if 4 \| n."
  - Relation: for integer Λ ≡ 0 mod 4, C_Λ has no positive points, so no degeneracy class has such Λ. The manuscript's classes have rational Λ, so there is no conflict.
  - Cite in §8.1 as the state of the art on positive points.
- **A. Bremner and Nguyen Xuan Tho**, The equation (w+x+y+z)(1/w+1/x+1/y+1/z) = n, Int. J. Number Theory 14 (2018) 1229–1246, doi 10.1142/S1793042118500768 (bib/bremnernguyen2018.bib; body not read). This is the four-variable analogue NT mentions; relevant only to a 4-cone-point version.
- **R. Kozuma**, A note on elliptic curves with a rational 3-torsion point, Rocky Mountain J. Math. 40 (2010), doi 10.1216/RMJ-2010-40-4-1227 (bib/kozuma2010.bib; Project Euclid PDF returned HTML, not read).
- **A. Bremner and A. MacLeod**, An unusual cubic representation problem, Ann. Math. Inform. 43 (2014) (corrigendum doi 10.33039/ami.2025.10.022). This concerns a/(b+c)+…; peripheral, not read.
- **Changes a novelty claim:** no.

### 5.9 Schoen 1988 and Beauville surface geometry
- **Reference:** C. Schoen, On fiber products of rational elliptic surfaces with section, Math. Z. 197 (1988) 177–199, doi 10.1007/BF01215188. bib/schoen1988.bib. NOT read (gap).
- **Secondary (Schoen 2008, arXiv:0804.1078):**
  - Table 4.1 lists the level-6 Beauville pencil "(x+y)(y+z)(z+x)+txyz, (1:−1:0), I1 I2 I3 I6, −8,1,0,∞".
  - §13: "A number of rigid threefolds with trivial canonical sheaf may be constructed as fiber products of rational semi-stable elliptic surfaces [Schü] and [Sch2, §7]".
- **Relation:** The primitive degeneracy pairs are rational points on the self-fibre product of this surface over the Λ-line, as NT says. This is the natural frame for Conjecture 8.10 and G7-9.
- **Where to cite:** §8.1 (Prop. 8.2) and §8.4.
- **Changes a novelty claim:** no, but the heuristic sentence at l. 1414 should be framed with it.

### 5.10 Prouhet–Tarry–Escott literature
- **Reference:** P. Borwein and C. Ingalls, The Prouhet–Tarry–Escott problem revisited, Enseign. Math. (2) 40 (1994) 3–27. Zbl 0810.11016; raw record bib/borweiningalls1994.zbmath.json (no DOI). Preprint read (pdf/borweiningalls1994_preprint.pdf).
- **Related:** P. Borwein, Computational Excursions in Analysis and Number Theory, Ch. 11 "The Prouhet–Tarry–Escott Problem", Springer 2002, 85–95, doi 10.1007/978-0-387-21652-2_11 (bib/borwein2002pte.bib; not read).
- **Proves (preprint, verbatim):**
  - Prop. 1 (quoted in §4);
  - Prop. 2: "N(k) ≥ k + 1";
  - Prop. 3 (pigeonhole): "N(k) ≤ ½k(k+1) + 1";
  - Prouhet (p. 2): "in 1851 when Prouhet found that there are n^{k+1} numbers separable into n sets so that each pair of sets forms a solution of degree k and size n^k";
  - definitions of ideal and symmetric (even/odd) solutions in §3.
- **Relation:**
  - (Sig) The construction in Thm 3.10 is Prouhet's.
  - Problem 1 asks for the analogue of N(k) for odd powers with R. Borwein–Ingalls' Prop. 3 pigeonhole bound is the classical counterpart of a T_L upper bound polynomial in L, while the manuscript has only T_L ≤ 2^{2L−1}. A pigeonhole count may give a polynomial bound, but the reciprocal-sum constraint is not a power sum, so this needs checking.
  - Problem 2 and Theorem C(1) are "odd symmetric" PTE systems with a reciprocal condition.
  - (Thr, Stab, Loc) none.
- **Where to cite:** Prop. 3.9 (Prouhet) together with Allouche–Shallit; Problems 1–2; and the Theorem A recalibration (§4).
- **Changes a novelty claim:** It does not remove a result. It supplies the classical frame for "Problem 1 … the analogue of an ideal solution", and the manuscript should cite it there instead of only Allouche–Shallit.

---

## 6. Files

- **PDFs:**
  - pdf/bgn1993.pdf, schinzel1996.pdf, beauville1982.pdf (Gallica reproduction), ostrowski1940.pdf, mazur1977.pdf;
  - laurens2023_arxiv.pdf, msw_arxiv.pdf, mueller_arxiv.pdf, bremnerguy1997.pdf, sadekelsissi2015.pdf, nguyen2021.pdf, borweiningalls1994_preprint.pdf;
  - pari_refcard-ell_2.17.2.pdf;
  - arx_1305.6237 (Ulas), arx_1811.07451 (Cha et al.), arx_2408.13867, arx_0804.1078 (Schoen 2008), arx_1105.4207 (Daugherty–Ram–Virk), arx_2407.04569, arx_1804.04394, arx_2401.17680.
- **Page images:** img/beauville-2.png, img/beauville-3.png, img/ostrowski-054.png, img/ostrowski-056.png, img/bgn-04.png, img/bi-04..07.png.
- **Raw records (bib/):** see the table below.

| bib/ file | source |
|---|---|
| bgn1993.bib | https://doi.org/10.1090/s0025-5718-1993-1189516-5 |
| laurens2023.bib | doi 10.1007/s00526-023-02534-2 |
| msw2022.bib | doi 10.1080/10586458.2022.2061650 |
| korobovbugaevskaya2016.bib | doi 10.1090/mcom/2994 |
| mueller2016.bib | doi 10.1007/s10208-014-9239-3 |
| ostrowski1940.bib | doi 10.1007/bf02546330 |
| mazur1977.bib | doi 10.1007/bf02684339 |
| kelly1964.bib | doi 10.1090/s0002-9939-1964-0168542-2 |
| kelly1989.bib | doi 10.1090/s0002-9939-1989-0984800-0 |
| zhangcai2013.bib | doi 10.1090/s0025-5718-2012-02609-3 |
| bremnerguy1997.bib | doi 10.1017/s0013091500023397 |
| schoen1988.bib | doi 10.1007/bf01215188 |
| guy2004.bib | doi 10.1007/978-0-387-26677-0 |
| borwein2002pte.bib | doi 10.1007/978-0-387-21652-2_11 |
| nguyen2021.bib | doi 10.33039/ami.2021.04.005 |
| bremnernguyen2018.bib | doi 10.1142/s1793042118500768 |
| kozuma2010.bib | doi 10.1216/rmj-2010-40-4-1227 |
| macdonald1995ch3.bib | doi 10.1093/oso/9780198534891.003.0003 |
| pragacz1991.bib | doi 10.1007/bfb0083503 |
| *.crossref.json | api.crossref.org/works/<doi> |
| schinzel1996, steinig1971, beauville1982, bgn1993, kelly1964, zhangcai2013, borweiningalls1994 .zbmath.json | api.zbmath.org/v1/document/_search?search_string=an:<id> or ti:… |
| laurens2023, msw2022, mueller2016, sadekelsissi2015, ulas2013, chaetal2019, youmbaizargarvoznyy2024 .arxiv.xml | export.arxiv.org/api/query?id_list=<id> |

- **Text:** txt/pari_announce_2.17.2.html, txt/pari_timeline.html, txt/pari_doc_ell_stable.html, txt/*_ams.txt (AMS article pages), txt/se/mo_*.json (MathOverflow 410757, 212800).
