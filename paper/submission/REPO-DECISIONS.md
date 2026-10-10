# Repository decisions for the owner (A. Agadi)

This file is for the owner of `github.com/Ali-M658/Arithmetic-verification`. Nothing described here has been changed: no branch was merged or deleted and no history was rewritten. Each item states the facts, as checked on 2026-10-10 against the local clone and `origin`, and then the options. The decisions are the owner's, with the authors' agreement where noted.

## (a) The unmerged branch `remote-remediation`

**What it is.** The branch is one commit ahead of its base:

- tip `53c1a68`, 2026-08-11, author Palaash Gang, "Move the non-functional upstream verification scripts into deprecated/";
- base `501c091` on `main`;
- `main` had gained 160 commits since the base as of `2302b98`;
- the branch is identical on `origin/remote-remediation`.

Diff against `main` (`git diff --stat main...remote-remediation`):

```
 deprecated/DEPRECATED.md                           | 130 +++++++++++++++++++++
 .../advanced_pillow_verification.py                |   0
 .../enumerate_degeneracies.py                      |   0
 .../generate_latex_supplementary_table.py          |   0
 run_all.py => deprecated/run_all.py                |   0
 5 files changed, 130 insertions(+)
```

**What the commit does:**

- It moves the four original root scripts, unmodified, into `deprecated/`.
- It adds `deprecated/DEPRECATED.md`. That file explains, script by script:
  - none of the four contains an `assert`;
  - one prints an unconditional pass message;
  - two use the area $\pi(1-R)$ where Gauss–Bonnet gives $2\pi(1-R)$;
  - one prints hard-coded rows as results.
- `DEPRECATED.md` names each script's replacement in `code/` and says "This branch is for review, not for merging."

**What `main` does instead:**

- The four scripts are still at the repository root of `main`, byte-identical to the branch's copies.
- `main` also keeps byte-identical copies in `code/upstream/`, with that folder's own README.
- The README's "Credits" section names the root scripts as the co-author's original work and says the harness in `code/` re-implements and cross-checks them.
- So the problem the branch addresses (scripts that report success without checking) is documented on `main` by the README, but not next to the scripts themselves.

**Options:**

1. **Leave the branch unmerged** and delete it locally and on `origin` (`git push origin --delete remote-remediation`). The README of `main` already credits and explains the scripts. Simplest.
2. **Keep the explanation without moving files.** Copy `DEPRECATED.md` (or a shortened version) into `main` next to the root scripts, then delete the branch. The scripts stay where the co-author put them, and readers of the deposit see why they are not the verification.
3. **Merge the branch.** It still applies cleanly in intent, but its text predates more than 160 commits. Its line references and the duplicate copies in `code/upstream/` would need reconciling first.
4. **Keep the branch as is.** A Zenodo deposit made from a `main` release or from `git archive` of `main` does not include other branches.

Whatever is chosen, the decision should be made before the Zenodo deposit. The root scripts are part of every export of `main`.

## (b) The third-party PDF in git history (Uçar's thesis)

**Facts:**

- **The file:** `research/raw/spectral-invariants-for-polygons-and.pdf` (blob `90bace21b490`, 1,578,958 bytes). Its title page reads: Eren Uçar, *Spectral invariants for polygons and orbisurfaces*, Dissertation, Humboldt-Universität zu Berlin (156 pages).
- **Added and removed:**
  - added in `e731eca` (2026-08-11, "Add the research corpus, indexes and review findings");
  - removed from the tree in `ede344b` (2026-10-01, "Stop tracking a fetched third-party PDF and the build output").
- **Not in the current tree:** it is not in the tree of `main`, so neither the GitHub release archive nor `git archive` of the current commit contains it.
- **Still in the history** of both `main` and `remote-remediation`, locally and on `origin`. The GitHub repository page answered HTTP 200 to an anonymous request on 2026-10-10, so the history is presumably public.

**Licence.** The thesis is arXiv:1711.03405 (abstract page fetched 2026-10-10, submitted 9 Nov 2017 by Eren Ucar). The abstract page links the licence <http://arxiv.org/licenses/nonexclusive-distrib/1.0/>, whose fetched text reads:

> I grant arXiv.org a perpetual, non-exclusive license to distribute this article. I certify that I have the right to grant this license. I understand that submissions cannot be completely removed once accepted. I understand that arXiv.org reserves the right to reclassify or reject any submission.

That licence is granted to arXiv only. It gives third parties no right to redistribute the PDF, so a copy in a public repository's history is redistribution without a licence, although the same file is freely available from arXiv.

**Options:**

1. **Leave the history as it is.** The file is out of the current tree and out of every future archive. It remains reachable through the two commits above for anyone who clones the repository. This is the least disruptive option, and it is common practice for an accidental commit of a freely available preprint. The owner may prefer to ask the author, or simply note the removal.
2. **Rewrite the history to remove the blob**, for example with `git filter-repo --path research/raw/spectral-invariants-for-polygons-and.pdf --invert-paths`. This must be done with the owner's agreement and the authors' agreement, because:
   - it changes the hash of every commit from `e731eca` on, on both branches;
   - every clone must be re-cloned, and any commit hash quoted elsewhere becomes invalid (none is quoted in the manuscripts);
   - it needs a force-push of `main` and of `remote-remediation`;
   - GitHub may keep cached views of the old commits until they are garbage-collected or GitHub support is asked to purge them.

   If chosen, do it **before** the Zenodo deposit and the arXiv postings, so that no published record points to a commit that later disappears.

## (c) Third-party text in the tracked research notes (affects the deposit)

The deposit is to be a clean export of the current commit, excluding nothing tracked. It will therefore include `research/notes/`. Twenty-two tracked notes there are larger than 40 kB, and several hold the extracted full text of third-party works, for example:

| file | size | content (from its header) |
|---|---|---|
| `research/notes/unsolved-problems-in-number-theory-pdf-1o9si23bb6dg.md` | 566,510 B | text of R. K. Guy, *Unsolved Problems in Number Theory* (a copyrighted book), fetched from vdoc.pub |
| `research/notes/spectral-invariants-for-polygons-and.md` | 324,854 B | text of Uçar's thesis (item b) |
| `research/notes/190500259-the-heat-kernel-on-curvilinear-polygonal-domains-in-surfaces-2.md` | 337,666 B | full text of an arXiv paper |
| `research/notes/the-spectral-geometry-of-hyperbolic-and-spherical-manifolds-analogies-and-open-p.md` | 300,642 B | full text of a survey |

The full list is produced by:

```
git ls-files research | while read f; do s=$(wc -c < "$f"); [ $s -gt 40000 ] && echo "$s $f"; done | sort -rn
```

The deposit will carry a licence of the authors' choosing. Republishing these texts under it would purport to license material the authors do not own, and the book text in particular should not be redistributed.

**Options:**

1. Before the deposit, remove the full-text notes from the tree (`git rm`), keeping their metadata and summaries. This is an ordinary commit, with no history rewrite. The notes stay in the history, which raises the same question as (b).
2. Exclude `research/` from the deposit. This departs from the "excluding nothing tracked" plan, so the authors must agree.
3. Keep them, and state in the deposit description that `research/` contains third-party material not covered by the deposit's licence. This is weaker, and it does not resolve the book text.

Item (c) is the one that blocks the Zenodo deposit. It should be settled before the DOI is minted.

## (d) Smaller items in the deposited files

`README.md` still opens with "Target journal: *The Journal of Geometric Analysis*" and describes `figures/` as "empty until the figure session". Both are out of date. The deposit description in `.zenodo.json` is current, but the owner may want to update the README before the release that mints the DOI.
