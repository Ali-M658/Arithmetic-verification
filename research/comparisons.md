# Cross-locus reconciliation

Committed positions from each locus, reconciled against each other. Where two loci bear on
the same manuscript claim, the reconciliation is recorded explicitly.

## L1 × L3 — the two novelty verdicts point the same way, for different reasons

L1 (Diophantine novelty) and L3 (priority claim) are independent questions, and it would be
suspicious if both came back "new" for the same reason. They do not.

L1 returns "new" on an **exhaustive negative search**: Guy's UPINT 3rd edition grepped in
full for `2,8,8`, `3,3,12`, `triangle group`, `orbifold`, `covolume`, `Takeuchi` — zero hits;
OEIS null on both count sequences with a working control test; the Bloom–Elsholtz survey's
taxonomy has no category for the problem. The evidence is *absence*, and its force comes
entirely from how well-controlled the search was.

L3 returns "survives" on a **positive structural argument**: Bari–Hunsicker proves the
opposite kind of statement (insufficiency, not sufficiency), to all orders rather than a
finite count, in the spherical rather than hyperbolic setting, with no minimality claim. Here
the evidence is *presence* — we read the competitor and it turned out to be a different shape
of result.

These are methodologically independent, which is why the two verdicts reinforce rather than
merely echo each other.

## L2 × L3 — a tension the manuscript should notice

L2 establishes that explicit cone coefficients exist for **every** $\ell$ at constant
curvature (Uçar (4.25)+(4.33); Schueth Remark 5.4(ii)). L3 establishes that nobody has used
them to count coefficients for a determinacy threshold.

Those two facts sit uneasily together, and the manuscript should say why. The inputs for the
manuscript's Theorems A–C have been publicly available since 2017, yet the threshold question
was not asked. The honest reading — and the one that strengthens the paper — is that the
contribution is not analytic but *conceptual*: asking how many coefficients suffice, and
answering it sharply, is the new move. The analysis was already on the shelf. A referee will
notice this; better to own it in §1.3 than be told.

This also sharpens what §1.3(c) ("load-bearing only") should say. The manuscript currently
says it uses the third coefficient "as computed in [DGGW, Schueth, Uçar], not rederived".
That is right, and L2 confirms it is right for $\ell=1$ — but the same sources give $\ell=2$
and beyond, which is precisely what makes the Remark 5.6 extension cheap.

## L2 × the original computation — mutually reinforcing

The orchestrator's own enumeration found a 4-cone pair, $\mathcal O(3,10,15,30)$ and
$\mathcal O(4,5,21,28)$, agreeing in $(R,S_1,P_3)$. On its own that establishes only that
three coefficients do not suffice for $n=4$. L2 supplies the other half: Schueth's Theorem 4.1
gives $b_2$ in closed form, delivering $P_5$ with coefficient $1/2520$, which separates the
pair. Together they give $K=4$ exactly for those two orbifolds — **the matching lower bound
that Remark 5.6 leaves open, for $n=4$**.

Neither half is worth much alone. The computation without L2 is a fact about symmetric
functions with no spectral meaning; L2 without the computation is an upper bound with no
witness. This is the clearest case in the sweep where the literature result and the original
computation had to meet.

## L4 — technique and setting must be separated

The two halves of L4 disagree, and the disagreement *is* the answer.

On technique, the verdict is unambiguous: nothing is new. Batenkov–Yomdin's Corollary 4.3
already says the Prony map's critical points are exactly the node collisions — structurally
identical to the manuscript's Jacobian vanishing on $p=q,p=r,q=r$ — and their Theorem 4.5
already gives accuracy scaling as a power of $\prod_{i<j}|\xi_j-\xi_i|^{-1}$. Presenting the
conditioning analysis as new would be a mistake a referee in numerical analysis would catch
immediately.

On setting, the verdict is pending the orbifold-stability null, but the shape is clear: no
stability theorem for a spectral inverse problem on an orbifold has surfaced. Combined with
the integer-valuedness of the cone orders — which turns a conditioning bound into *exact*
recovery below half the minimum gap — the setting-level claim looks defensible where the
technique-level claim does not.

## L5 × L3 — the venue tells you how to frame the priority claim

The JGA exemplar, Dryden–Gordon–Moreno–Rowlett–Villegas-Blas 2025
(`10.1007/s12220-025-01922-8`), proves that for almost all convex polygons there are at most
finitely many Steklov-isospectral non-congruent domains, **with explicit upper bounds**. Two
of its authors wrote DGGW. That is simultaneously the venue precedent, the referee signal,
and a template for tone: a finiteness-and-explicit-bounds result on cornered domains, stated
without priority language.

Note what that paper does *not* do: claim to be first at anything. The manuscript's §1.3(b)
"to our knowledge this is the first…" is the one sentence in the paper most likely to draw
fire, and the venue's own house style suggests it is unnecessary. The result is sharp on its
own terms.

## L6 — an emergent locus that changes the deliverable

L6 was not in the brief. It emerged when the first two "preprint" citations checked
(Bari–Hunsicker, Schueth 2025) both turned out to be published, and a third check turned up
an uncited DGGW erratum. A two-for-two failure rate on spot checks means the bibliography
cannot be assumed sound anywhere, which is why a dedicated verification batch was dispatched
rather than treating this as incidental.

The erratum deserves particular note: it corrects DGGW's Theorem 5.1 only, not §5.6, so the
manuscript's quoted formula is unaffected. But it exists, it is citable
(`10.1307/mmj/1488510034`), and it was prompted by a question from Naveed Bari — the same Bari
as Bari–Hunsicker. The manuscript's two most important sources are in direct contact, and it
does not mention the erratum at all.
