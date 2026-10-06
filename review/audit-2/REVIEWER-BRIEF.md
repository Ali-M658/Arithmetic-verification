# G5-bis reviewer brief (read first, applies to every group)

You are an independent reviewer. The paper "How much of a hyperbolic orbifold does heat hear?"
(for The Journal of Geometric Analysis) is about to absorb results that have only been checked by
the sessions that produced them. You have **not** seen their proofs, scripts or data and you must
not: your job is to re-derive each result **from its statement alone** and to try to break it.
The standard is that of `review/audit/G5-VERDICT.md` (read it for tone and grading; do not read
the other files of `review/audit/` except `review/audit/statements/*.md` where your bundle points to them).

## What you receive

`review/audit-2/statements/<group>.md`: verbatim statements, hypotheses and external inputs. No proofs.
Fetched third-party texts are in `review/audit-2/sources/` (untracked). Nothing else.

**Forbidden to open** until the lead releases the comparison phase: `theory/pte/**`,
`theory/revision/**`, `theory/signatures/proof.md`, `theory/*/proof.md`, `review/referee-sim/**`,
`paper/**`, any `check_*.py` or `*.txt` output of another session, `review/audit/**/REVIEW.md`,
`COMPARISON.md`, `check_*.py` (except the statements files named in your bundle). If you open one
by accident, write it under "contamination" in your REVIEW.md and say what you saw.

## Method, for every result in your bundle

1. **Re-derive** it from the statement. Write the proof in your own words. Where the statement
   uses an external input, name the input and where you took it from (fetched text, with page).
2. **Hunt counterexamples** with your own exact code (`fractions.Fraction`, integers, `sympy`; no
   floating point as a certificate; real `assert`s; scripts exit nonzero on failure). Adversarial
   cases first: smallest L, order 1, repeated orders, boundary areas and boundary parameters, empty
   or degenerate configurations, the n = 2 and n = 3 edge cases of the doubling, hypotheses dropped
   one at a time. A hypothesis the statement lacks but the truth needs is a finding.
3. **Grade** each result:
   - **FATAL**: the result is false and no repair keeps its content.
   - **SERIOUS**: false or misleading as printed, or needs a changed constant/statement, but repairable
     (give the repair); or a claim the evidence does not support.
   - **MINOR**: missing hypothesis the truth needs, wording, citation, printed constant or rounding.
   - **NONE**: re-derived, no defect found.
4. **Exact wording changes**: for every non-NONE grade, give the replacement text.
5. Everything you cannot reach (paywall, 403, no network) is an **instrument gap**: log it in
   `fetches.md`; it is not a confirmation.

## Deliverables (your folder `review/audit-2/<group>/`)

- `REVIEW.md`: for each result: id, verbatim statement id, grade, your derivation (a real proof, not
  "follows from"), the counterexample hunt (what you tried, what the exact code returned), required
  wording changes. Start with a table of ids and grades, then a section "contamination" (or "none"),
  then "instrument gaps".
- `check_*.py` and their outputs `check_*.txt`: exact, assert-based, exit nonzero on failure.
  The output file must be produced by running the script (`python3 check_x.py > check_x.txt`).
  Use `/opt/homebrew/Caskroom/miniforge/base/bin/python3` (sympy 1.14).
- `fetches.md`: every source retrieved, URL, HTTP code, file, and every source not reachable.
- Do **not** commit, do not push, do not touch git. The lead commits. Never run `git checkout`,
  `switch`, `reset`, `stash`, `rebase`, `merge`, `clean`, `git add -A` or `git add .`.

## Shared-folder rules (another session is working in this folder right now)

- Working directory `~/Desktop/hyperbolic-pillow`, branch main. Write **only** under `review/audit-2/<group>/`.
  Never edit `theory/`, `paper/`, `figures/`, `code/`, `admin/` or any other file, even to fix an error you
  find: report it. Do not run `code/run_all.sh` or regenerate `DATA-MANIFEST.md`.
- Scratch files go in the session scratchpad directory you are given, or inside your group folder.
- No attribution of any kind (no "Claude", no "Co-Authored-By") in any file you write.
- Third-party text is fetched, never recalled. No browser; headless retrieval (`curl` with a desktop UA,
  arXiv, Crossref, Unpaywall) only. Quote the fetched text with page or section.
- Machine safety: before any run that may take more than a minute, run `memory_pressure -Q`; wait if
  free memory is below 20%. Every search has a time cap and writes checkpoints. At most 2 heavy
  processes at a time, started with `nice -n 10`. Eight reviewers share this machine.

## Comparison phase (only after you have written REVIEW.md)

Do not start it until you are told. Then you may read the existing proof, scripts and data of the
results in your bundle, and write `COMPARISON.md`: for each result, does the existing proof agree with
your derivation? Record every discrepancy (a step you could not reproduce, a stronger claim than the
statement, a script that does not test what it claims, a printed number that differs from yours).
Do not change your blind grades silently: if a grade changes, say so in COMPARISON.md and why.

## Final message

Return: a table of every result with its grade, every FATAL/SERIOUS finding in two or three sentences
with the exact wording change, any changed constant or statement, anything unreachable.
