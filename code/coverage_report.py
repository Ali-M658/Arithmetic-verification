#!/usr/bin/env python3
"""
Map every claim in review/claim-ledger.md onto the script that now backs it.

This exists so the reproducibility report is generated rather than hand-typed,
and so a claim ID cannot drift: the script parses the ledger for the authoritative
set of IDs, parses verify_identities.py for the IDs its checks actually claim to
discharge, and FAILS if any tag refers to an ID that does not exist in the ledger.
A verification tagged with a typo'd claim ID is worse than an untagged one --
it looks like coverage and is not.

Coverage that is not expressible as a @H.check tag -- enumeration sweeps, table
generation, cross-validation -- is declared in COVERAGE below, with the reason
recorded alongside so the mapping can be audited by hand.

Writes review/coverage-map.csv and prints a summary. Exit nonzero if any tagged
claim ID is unknown to the ledger.
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
LEDGER = REPO / "review" / "claim-ledger.md"
VERIFY = REPO / "code" / "verify_identities.py"
OUT_CSV = REPO / "review" / "coverage-map.csv"

LEDGER_ROW = re.compile(r"^\|\s*((?:AB|IN|CV|HC|TH|GE|DE|AP)-\d+)\s*\|(.*)$")
# The optional f-prefix matters: a tag written as f"..." is still a tag, and
# missing it would silently under-report coverage.
CHECK_TAG = re.compile(r'@H\.check\(\s*f?"([^"]+)"\s*,\s*f?"([^"]*)"', re.S)

# --------------------------------------------------------------------------
# Coverage that is not a @H.check tag. Each entry: claim -> (script, why).
# --------------------------------------------------------------------------

ED = "code/enumerate_degeneracies.py"
OE = "code/orbifold_enum.py"
MT = "code/make_table.py"
CC = "code/cross_check.py"

COVERAGE: dict[str, tuple[str, str]] = {}


def _add(script: str, why: str, *claims: str) -> None:
    for c in claims:
        COVERAGE[c] = (script, why)


# -- orbifold_enum.py -------------------------------------------------------
_add(OE, "selftest: Area/pi = 2*(1-R), and not the pi*(1-R) form",
     "IN-01", "GE-01")
_add(OE, "selftest: hyperbolicity sum(1-1/m_i)>2 reduces to R<1 at n=3",
     "IN-02")
_add(OE, "Pillow rejects orders < 2 and unsorted multisets",
     "IN-03")
_add(OE, "selftest: chi_orb = R - 1 at n = 3", "CV-02")
_add(OE, "selftest: least hyperbolic sum is 10, realised only by O(3,3,4)",
     "TH-12", "TH-16")
_add(OE, "selftest: P_k for k = 0,1,3,5,7 including P_3 = 1032 / 1782",
     "GE-02")

# -- enumerate_degeneracies.py ---------------------------------------------
_add(ED, "check_base_case: no sigma-collision for any S <= 17",
     "AB-01", "IN-04", "IN-09", "TH-19")
_add(ED, "check_base_case: exactly one degeneracy at S = 18, the expected pair",
     "AB-03", "AB-04", "IN-06", "IN-07", "IN-08", "TH-42", "AP-16")
_add(ED, "sweep + degeneracy_groups keyed on sigma = (S_1, R)",
     "IN-13", "DE-01", "DE-02", "DE-12")
_add(ED, "check_primitivity_consistency: every scaled group reduces to its base",
     "AB-06", "DE-10", "DE-11")
_add(ED, "check_s36: primitive and scaled classes at S = 36",
     "DE-09")
_add(ED, "check_lower_bound: cumulative count >= floor(S/18) for all S <= 600",
     "AB-07", "DE-06", "DE-07", "DE-08")
_add(ED, "cumulative checkpoints asserted against independent values",
     "AB-08", "AB-09", "DE-14", "DE-15", "DE-16", "DE-17", "DE-18", "DE-19",
     "DE-20", "DE-21", "DE-22", "DE-23", "DE-29", "AP-09")

# -- make_table.py ----------------------------------------------------------
_add(MT, "table2.tex regenerated from enumeration; collisions detected, not hardcoded",
     "AP-14", "AP-15", "AP-17", "AP-11")
_add(MT, "table1.tex regenerated from the sweep at the manuscript's checkpoints",
     "AP-12")

# -- cross_check.py ---------------------------------------------------------
_add(CC, "three-way agreement: harness vs. oracle vs. recovered legacy scripts",
     "AB-12", "AP-01", "AP-02", "AP-10")

# --------------------------------------------------------------------------
# Claims that remain unbacked, with the reason. Anything not listed here and
# not covered above is reported as an unexplained gap.
# --------------------------------------------------------------------------

UNBACKED: dict[str, str] = {
    # Quoted from the literature -- not ours to verify, only to cite correctly.
    "CV-01": "eq:a0conv is the DGGW normalization, quoted. The harness verifies "
             "everything derived FROM it, and checks it against the (S_1+R-2)/12 "
             "form, but the expansion itself is external.",
    "HC-08": "b_0(gamma^j) = (1/4)csc^2(j*pi/m) is quoted from DGGW.",
    "HC-20": "eq:b1 is quoted from Schueth Rem. 4.2 / DGGW 5.6. The harness "
             "verifies that eq (5) follows from it symbolically, not the "
             "expression itself.",
    "HC-21": "That the smooth t^1 term is a universal constant times Area is an "
             "analytic statement about the heat expansion, not an arithmetic one.",
    "IN-12": "That the FIRST HEAT COEFFICIENT is the area is analytic input; the "
             "harness verifies the arithmetic consequence (area determines R).",
    "DE-26": "Birthday heuristic; the manuscript states it as non-rigorous.",
    "DE-27": "Conjecture 5.3, open.",
    "DE-28": "Conjecture 5.3 restated, open.",
    "DE-30": "n-cone hyperbolicity at general n is definitional. orbifold_enum "
             "implements and exercises it at n = 3, 4, 5, but the manuscript "
             "makes no numerical claim here.",
    "DE-31": "K <= n at general n is stated but not proved in the manuscript; "
             "there is nothing to reproduce.",
    # Artefact claims that depend on the PUBLIC repository, not on local code.
    "DE-13": "PUBLIC-AVAILABILITY: the generating script now exists locally but "
             "is not yet in the upstream repository. Closes on push.",
    "AP-13": "PUBLIC-AVAILABILITY: run_all.sh exists locally; the manuscript "
             "names it 'run_all'. Closes on push plus a one-word text fix.",
    "AP-18": "PUBLIC-AVAILABILITY: closes on push.",
    "AP-19": "PUBLIC-AVAILABILITY: closes on push.",
    # Prose restatements with no separate arithmetic content.
    "AB-02": "Prose summary of TH-18/TH-20, both verified.",
    "AB-05": "Prose summary of TH-35, verified.",
    "AB-10": "Prose summary of IN-10/HC-28, both verified.",
    "AB-11": "Prose summary of HC-33/HC-34, both verified.",
    "IN-05": "Prose restatement of IN-04 plus IN-07.",
    "GE-03": "Prose synthesis of TH-10 and HC-34, both verified.",
    "GE-04": "Prose restatement of TH-43, verified.",
    "GE-06": "Prose consequence of TH-47, verified.",
    "AP-03": "Covered by the CV-03..CV-05 check; listed there.",
}


def ledger_claims() -> dict[str, str]:
    """Claim ID -> the assertion text, parsed from the ledger tables."""
    claims: dict[str, str] = {}
    for line in LEDGER.read_text().splitlines():
        m = LEDGER_ROW.match(line)
        if not m:
            continue
        cid, rest = m.group(1), m.group(2)
        cells = [c.strip() for c in rest.split("|")]
        claims[cid] = cells[1] if len(cells) > 1 else ""
    return claims


def verify_tags() -> dict[str, str]:
    """Claim ID -> description, from the @H.check tags in verify_identities.py."""
    out: dict[str, str] = {}
    for ids, desc in CHECK_TAG.findall(VERIFY.read_text()):
        for cid in (c.strip() for c in ids.split(",")):
            if cid:
                out[cid] = desc.strip()
    return out


def main() -> int:
    claims = ledger_claims()
    tags = verify_tags()

    print(f"ledger claims:            {len(claims)}")
    print(f"claim IDs tagged in verify_identities.py: {len(tags)}")

    unknown = sorted(set(tags) - set(claims))
    if unknown:
        print(f"\nFAIL -- {len(unknown)} tagged claim ID(s) do not exist in the ledger:")
        for cid in unknown:
            print(f"  - {cid}  (tagged on: {tags[cid]})")
        print("\nA verification tagged with a typo'd claim ID looks like coverage "
              "and is not. Fix the tag or the ledger.")
        return 1

    bad_cov = sorted(set(COVERAGE) - set(claims))
    if bad_cov:
        print(f"\nFAIL -- {len(bad_cov)} declared coverage entr(ies) name unknown claims:")
        for cid in bad_cov:
            print(f"  - {cid}")
        return 1

    bad_unb = sorted(set(UNBACKED) - set(claims))
    if bad_unb:
        print(f"\nFAIL -- {len(bad_unb)} unbacked entr(ies) name unknown claims:")
        for cid in bad_unb:
            print(f"  - {cid}")
        return 1

    rows = []
    counts = {"verify_identities.py": 0}
    gaps: list[str] = []

    def sort_key(cid: str) -> tuple[int, int]:
        order = ["AB", "IN", "CV", "HC", "TH", "GE", "DE", "AP"]
        pre, num = cid.split("-")
        return order.index(pre), int(num)

    for cid in sorted(claims, key=sort_key):
        if cid in tags:
            script, why, status = "code/verify_identities.py", tags[cid], "backed"
        elif cid in COVERAGE:
            script, why = COVERAGE[cid]
            status = "backed"
        elif cid in UNBACKED:
            why = UNBACKED[cid]
            script = "NONE"
            status = ("public-availability" if why.startswith("PUBLIC-AVAILABILITY")
                      else "prose-restatement" if why.startswith("Prose")
                      else "covered-elsewhere" if why.startswith("Covered by")
                      else "not-machine-checkable")
        else:
            script, why, status = "NONE", "UNEXPLAINED GAP", "gap"
            gaps.append(cid)

        counts[script] = counts.get(script, 0) + 1
        rows.append({
            "claim_id": cid,
            "assertion": claims[cid],
            "backing_script": script,
            "status": status,
            "note": why,
        })

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["claim_id", "assertion", "backing_script", "status", "note"])
        w.writeheader()
        w.writerows(rows)

    print(f"\nwrote {OUT_CSV.relative_to(REPO)}\n")
    print("backing script breakdown")
    for script, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {n:4d}  {script}")

    by_status: dict[str, int] = {}
    for r in rows:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
    print("\nstatus breakdown")
    for st, n in sorted(by_status.items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"  {n:4d}  {st}")

    backed = by_status.get("backed", 0)
    print(f"\n{backed}/{len(rows)} claims backed by an executable check")

    if gaps:
        print(f"\nFAIL -- {len(gaps)} claim(s) neither backed nor explained: {gaps}")
        return 1

    print("PASS -- every ledger claim is either backed or explicitly explained")
    return 0


if __name__ == "__main__":
    sys.exit(main())
