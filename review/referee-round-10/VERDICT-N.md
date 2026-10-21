# VERDICT-N (round 10): "Triples with Equal Sum and Equal Reciprocal Sum" (Integers)

Inputs: the five reports of Panel N (README.md). Length remarks are excluded.

## Recommendations

| reviewer | recommendation | confidence |
|---|---|---|
| N-a editor (classical number theory) | send to review; major revision | high (correctness, Choudhry findings), moderate (significance) |
| N-b (group laws, elliptic curves) | minor revision | high |
| N-c (classical Diophantine equations) | minor revision (major if M1/M2 not fixed) | about 0.75 |
| N-d (computational enumeration) | minor revision | high |
| N-e (rigour, references) | minor revision | high (mathematics) |

There is no FATAL item and no mathematical error.
- N-d and N-e reproduced Table 3 independently, every row to S = 6000, along with the triple counts and the classification of the 46 254 primitive pairs.
- All three numerical referees reproduced the fits and the holdouts.
- N-b and N-e reproduced the descent of Table 1, the ranks, torsion, conductors and root numbers.
- N-a, N-b and N-c read Choudhry 2011 from the archived publisher PDF.

**Stop condition: not met before the fixes.** This was the one extra round the authors authorised; after the fixes and the fix check, the loop ends for this paper.

## FATAL and MAJOR items

| id | item (reviewers) | status | resolution |
|---|---|---|---|
| N1 | The new Choudhry comparison is wrong in one clause: the isosceles family is Choudhry's first solution at x = (u,v,v); further material in Choudhry (his (3), §5.1, §2) is omitted (N-a M1, M2; N-b M1; N-c M1, M2) | CONFIRMED (the clause was written in round 10 and is false) | The clause is deleted. Corollary 1, Theorem 2 and Theorem 3 credit Choudhry [11, §4.1, p. 748] (and BGN's reciprocal pairing) for the families; the novelty is stated as the counting. Choudhry's (34) is cited as the construction of the line, and the stronger statement is given: −(2P+τ) is never positive for any real P, by components. His (3) is cited as the 2011 printing of the S = 26 and 34 pairs (Chen Shuwen's 2001 website). §5.1 is cited (chains of every length with Σx⁻¹ = 0, on the fibre Λ = 0, of mixed sign) and §2 (positive solutions for large s), and Theorem C's novelty is restated as positivity. Chen's "smallest" and "first known chains" are corrected explicitly (S = 18; first class of size 3 at S = 136) |
| N2 | Bremner–Macleod's priority misstated: [4, Thm 5.1] already gives the case 4 \| Λ of Nguyen Xuan Tho's theorem (N-e M1) | CONFIRMED (to be verified against the fetched [4]) | Reworded after checking [4] (E_N = E_{2N+6}, Lemma 2): [4] proves no positive point for Λ = 4M ≥ 8; [24] is a later proof by Hilbert symbols of the full case 4 \| n |
| N3 | Theorem 3 weak and headlined; the order of the dual family is open (N-a M3, N-c M3) | CONFIRMED (presentation) | Theorem 3 is moved out of the abstract and out of Theorem B into a stated proposition. The conjectured order X(log X)⁵ is named next to it, and the open point is said precisely: whether the Frei–Loughran–Sofos lower bound localises to the positive real region. The abstract and introduction state the contribution as structure, two counts and exact data |
| N4 | Holdouts presented as evidence for Question E; spurious precision in fitted exponents (N-a M4, N-c M4.1, N-d M1, M2) | CONFIRMED by computation | "Evidence for a positive answer" is removed from p. 22 and made consistent with p. 4 and the abstract. `exponent_fits.py` gets a new block, with asserts, that computes the b₀ family c·s^{b₀}(log s)^q, b₀ ∈ {0, 0.1, 0.2, 0.3}, with its deviance and holdout errors, and the sliding-window q and β; the text states that laws with asymptotic exponent 1.1–1.3 do almost as well, together with the window drift and the overdispersion. q is rounded to one decimal, and the cumulative fit is said not to be independent |
| N5 | §6.4 heuristic incomplete; line search weaker than presented (N-c M4.2–3, N-d m6) | CONFIRMED | The trivial canonical class of the variety of pairs (adjunction) and the a-invariant reading are added, with the dichotomy for the third-kind pairs. The number of the 189 lines that pass through a base point (where Lemma 3 forces the outcome) is computed by script and reported |
| N6 | The descent of Table 1 is not checkable from the paper (N-e M2, N-b m6) | CONFIRMED | For each Λ, the paper lists rational points whose images generate the listed Selmer groups and states the primes at which local solubility was tested (computed by script, with asserts); if that is not possible, "proves" is weakened to "computed and confirmed by a descent in the deposit". The ranks are said to be illustrative: Theorem 4 needs only Theorem 1(iv) |

## MINOR items

Applied where worthwhile and verifiable:
- N-a: m1–m5, m7–m9, m11, P4;
- N-b: m2, m4, m5, m7, m8, P1–P4;
- N-c: m1–m6, m8, m9, P2–P5;
- N-d: m1–m4, m7, m8, P1, P3–P6;
- N-e: m1–m11, P4–P7.

Not done:
- restructuring §1.3–1.4 beyond splitting paragraphs (P1 of N-a, N-c, N-e: §1.4 is split into paragraphs by topic);
- renaming symbols across the note;
- Figure 1 redesign;
- the Integers declarations block (house style; for the editor).
