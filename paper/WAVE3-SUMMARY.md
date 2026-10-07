# WAVE3-SUMMARY: the split after referee round 3

Referee round 3 (`review/referee-round-3/VERDICT.md`) found no mathematical error but judged the
48-page manuscript to be several papers in one. The manuscript is now two papers, each
self-contained, plus the unchanged arithmetic note.

## The three manuscripts

| manuscript | directory | pages | content |
|---|---|---|---|
| **Paper A**, *How much of a hyperbolic orbifold does heat hear?* (target AGAG) | `paper/jga/` | 39 + supplement 14 | what heat invariants hear about the signature, and at what cost |
| **Paper B**, *Finitely many eigenvalues determine the signature of a hyperbolic orbifold* (target to be decided; written to AGAG conventions) | `paper/eigen/` | 23 | finitely many approximate eigenvalues determine the signature, effectively |
| arithmetic note, *Triples with equal sum and equal reciprocal sum* | `paper/arith/` | 12 | unchanged except its cross-references |

All three build with no LaTeX errors, no undefined references or citations, and no overfull box above
1 pt (Paper B has one of 0.8 pt). No compiled manuscript PDF is committed. Each paper names the other
only in its text, as a companion manuscript in preparation (AGAG lists unpublished work only in the
text, `paper/jga/AGAG.md`); neither uses the other in a proof.

### Paper A

Sections: 1 Introduction (Theorems 1.1-1.3); 2 heat invariants at constant curvature; 3 hearing the
signature (moment problem, separation, **bounded cone orders**, the Prouhet-Tarry-Escott connection);
4 what heat does not hear; 5 triangle orbifolds and the isolated minimal pair; 6 stability;
7 computations; 8 open problems; Appendices A (growth proofs), B (heat expansion from the trace
formula, with admissibility), C (rank of C_{27/2} by hand), D (computational methods, search-only
statements). Figures F1-F8, all kept; captions at most two short sentences.

### Paper B

Sections: 1 Introduction (Theorems 1.1-1.3; what effectivity adds over compactness); 2 the heat trace
with enveloping remainders, derived from the trace formula; 3 heat invariants of a signature
(separation, bounded orders, integrality at the first difference); 4 the diameter, with proofs of
(H1)-(H3); 5 counting eigenvalues; 6 Theorem 6.2 (Theorem E) and its constants; 7 the a-posteriori
certificate; 8 the hypotheses (O(2,3,m) with the hyperbolic case of Jorgensen's inequality proved,
unbounded orders, pinching, the systole problem); Appendix A (admissibility of the heat function).
Same six authors and title page; declarations with the same placeholders.

Figures:
- **E1**: the eigenvalues lambda_1..lambda_6 of O(2,3,m) for 21 orders m = 7..4096, with the Rayleigh
  bounds of Proposition 8.3 and the rescaled view h_m^2(lambda_j - 1/4)/pi^2. **The computation
  succeeded**: the repository's double-window eigensolver (`numerics/solve.py`) in a scratch virtual
  environment built from `numerics/requirements.txt` (NGSolve 6.2.2607), two mesh levels per m
  ((h, p) = (0.1, 8) and (0.07, 10)), agreeing to at least 2.3e-10 relative; memory guard on. Orders
  above 4096 were tried and dropped: at m = 8192 the fine level returned a spurious double eigenvalue,
  at m = 16384 the mesher failed (recorded in `figures/gen/gen_e1_cusp.py`).
- **E2**: the separation mechanism for O(2,8,8): gaps |G_sigma0 - G_sigma| to its five competitors,
  the geodesic bound and the truncation errors for N = 21 and 100, with the window where 21
  eigenvalues decide.
- **E3**: N_obs, N_apr and the a-priori N across the ten computed orbifolds, log scale.
- **E4** (optional Blender render of O(2,3,m)): **not made**.

## The A2 theorem, as proved (Paper A, Theorem 3.7; `theory/msep/proof.tex`)

For an integer M >= 2 let Sig_{<=M} be the closed orientable hyperbolic 2-orbifolds (cone points only)
whose cone orders are all at most M.

1. If O, O' in Sig_{<=M} share their first M heat invariants c_1, ..., c_M, they have the same
   signature. Hence K_mult(O; Sig_{<=M}) <= min(M, floor(Area(O)/pi) + 4).
2. M cannot be lowered: with w_a = prod_{1<=b<=M, b!=a} (a^2 - b^2)^{-1}, the least positive integer C
   making nu(a) = C a w_a (2 <= a <= M) integral and s = sum nu(a)(1 - 1/a) even, and m, m' the
   positive and negative parts of nu, the signatures (g; m) and (g + s/2; m') (any g >= max(0, -s/2)
   giving positive area) are different, share c_1, ..., c_{M-1}, and differ in c_M by
   (-1)^M C a_{M-2} != 0. Examples: M = 3, (1; 3^9) and (0; 2^16), area 12 pi; M = 4,
   (0; 2^28, 4^8) and (1; 3^27), area 36 pi (both of least area, by exhaustive search).
3. Against all competitors: if O in Sig_{<=M} has area A and O' in Sig shares c_1..c_L (L >= 2), all
   orders of O' are at most M (2 floor(A/pi) + 8)^{1/(2L-3)}, and
   K_mult(O; Sig) <= M + ceil((1/2) log(2 floor(A/pi) + 8)).

Corollary 3.8: a pair with different signatures sharing c_1..c_L has a cone order at least L + 1; an
orbifold with K_mult(O; Sig) >= L + 1 has a cone order at least L + 1 - ceil((1/2) log(2 floor(A/pi) + 8));
so the area-driven growth of f(A) is a phenomenon of large cone orders.

The exact number asked for in the brief is **M** (sharp for every M >= 2). Exact verification
(`theory/msep/verify.py`): ranks for 2 <= M <= 24 in both formulations (the brief's padded system and
the Psi_k system), the Vandermonde identity, the Lagrange kernel, the sharp pairs for M <= 24, a
brute force for M <= 4, part (iii) on 24 complete area classes. Blind checks: two subagents given
only the statements (`theory/msep/BLIND-CHECK.md`): TRUE and TRUE; the second found the factor 1/2 in
(iii), which was adopted after an independent proof.

## Paper B: title and abstract

*Finitely many eigenvalues determine the signature of a hyperbolic orbifold*

> The Laplace spectrum of a closed orientable hyperbolic 2-orbifold determines its signature, the genus
> and the orders of its cone points, but a measurement or a computation yields only finitely many
> eigenvalues, each to some accuracy. We show that this suffices, effectively: among orbifolds of area
> at most A, systole at least epsilon and cone orders at most M, the first N eigenvalues, each known to
> within delta, determine the signature, with N and delta given by explicit formulas. Compactness
> alone yields some N and delta; ours can be computed and checked, and an a-posteriori version
> certifies the signature of a computed spectrum from 21 to 750 eigenvalues in our examples, where the
> a-priori count ranges from 4 x 10^4 to 7 x 10^12. The proof turns the first difference of heat
> invariants, an integer multiple of an explicit rational number reached by the M-th invariant at the
> latest, into a gap between heat traces. The bound on the cone orders cannot be dropped: as m grows,
> the orbifolds O(2,3,m) acquire arbitrarily many eigenvalues near 1/4, like a cusp.

## Round-3 items and where they landed

| item | resolution | paper |
|---|---|---|
| I1 split | done | both |
| I2 effectivity, a-posteriori | compactness paragraph (Mumford 1971 Cor. 3; Bers 1972 for elliptic elements); Theorem 7.1 certificate; Table 3 | B |
| I3 PTE relocation | one sentence after Proposition 3.14 | A |
| I4 search-only claims | listed in Appendix D | A |
| I5 numerical steps, Wikipedia | (H1)-(H3), commutator trace, Rayleigh identity, Lambert angle proved; Jorgensen's inequality, hyperbolic case, proved with his argument, original cited from its Crossref record, text an instrument gap (`paper/eigen/SOURCES.md`) | B |
| I6 bounded orders | Theorem 3.7 and Corollary 3.8 in A; part (i) in B (Theorem 3.4), giving k_* = min(floor(A/pi)+4, M) and new constants | A, B |
| I7 T(L) constructions | Lemma 3.15 and the construction paragraph; supplement S1 lists every piece; A.1.33 attribution fixed | A |
| I8 floating-point filter | sound modular test stated in Remark 3.17, implemented, run, 15 survivors all irreducible | A |
| I9 PTE literature | Wright, Hua, Dorwart-Brown, Borwein added; heuristic for T(L) | A |
| n1, n10-n13, n21 | Section 4 items | B |
| n2-n9, n14-n20 | see `paper/jga/ROUND3-CHANGES.md` (n17, the title: kept, with reason) | A |

Full dispositions: `paper/jga/ROUND3-CHANGES.md` (Paper A) and `paper/eigen/AUDIT.md` (Paper B).

## Constants after the bounded-order theorem (Paper B, Table 2)

With k_* = min(floor(A/pi) + 4, M): for the class of the (0;3,3,3,3) family with M = 3,
N = 4.3e4-3.7e5 and delta about 1e-9 (wave 2: 2.0e7 and 3.4e-24); for (10 pi, 1, 3), N = 1.1e7
(wave 2: 4.2e18); for (10 pi, 1, 12), N = 3.8e30 and delta = 8.7e-278 (wave 2: 1.3e35, 7.7e-384).

## Placeholders left (both papers)

- Zenodo DOI (data statement).
- Author contribution statement.
- Statement on the use of AI tools.

## Unresolved

- Paper A is 39 pages against the target 34-37 (see `paper/jga/ROUND3-CHANGES.md`, last section).
- The systole question (Paper B, Problem 1) is open; the route through manifold covers and the
  degeneration theory of hyperbolic surfaces suggested by referee b is described, not carried out.
- E4 (Blender render) not made.
- The text of Jorgensen's paper and of Beardon's Theorem 5.4.1 could not be read (instrument gaps);
  Paper B proves what it uses.
- The live AGAG guidelines page could not be fetched (an older capture is used; `paper/jga/AGAG.md`).

## Suite

`PYTHON=.venv/bin/python bash code/run_all.sh --quick` on the tree of commit b91d5b8 (Paper B's
two audit corrections were already in): **67 passed, 0 failed, 10 skipped**, 79 min 42 s.
`admin/build_data_manifest.py --check` passes (631 lines). `git ls-files | grep -iE '\.(pdf|djvu|ps)$'`
lists only files under `figures/out/` and `figures/proofs/`.

New stages: `msep bounded cone orders` (3:31), `pte T3 modular record` (0:02),
`pte T3 modular search (to 220)` (2:38), `figures data E2 E3 (eigen paper)`,
`figures vector F2-F5 F7-F9 E1-E3`; full mode only: `figures data E1 (NGSolve)`.
Changed eigen scripts run in their existing stages (`eigen theorem_e` 0:58, `eigen practice` 0:52).

| skipped stage | reason |
|---|---|
| audibility sharpness N=120 | full mode only (about 22 min) |
| stability threshold | full mode only (30-60 min) |
| divergence divergence | full mode only (about 10 min) |
| diophantine ranks (PARI) | cypari2 not installed in the pinned .venv |
| numerics S3 rerun record | record deferred to the final submission check |
| numerics validate (full), numerics moduli validate (full) | full mode only |
| numerics S3 re-solve (NGSolve) | full mode only (about an hour) |
| figures data E1 (NGSolve) | full mode only; it was run in this wave in the scratch NGSolve environment, assertions passed |
| figures Blender renders F1 F6 | renders are not part of the suite |
