#!/usr/bin/env python3
"""
Three-way cross-validation of the n = 3 results.

The same quantities are computed by three independent implementations, written
at different times by different hands:

  1. THIS HARNESS      code/orbifold_enum.py + code/enumerate_degeneracies.py
  2. THE ORACLE        review/audit-independent.py -- the exact-rational
                       re-derivation written during the manuscript audit
  3. LEGACY            code/legacy/ -- the co-author's original scripts,
                       recovered from upstream history

Agreement across three independent routes is the point. Where they disagree,
this script REPORTS THE DISAGREEMENT and fails; it never silently prefers one
source over another. Deciding which is right is a human judgement, and it needs
the discrepancy in front of it.

Legacy coverage is necessarily partial -- those scripts stop at S_1 = 18 and
contain no assertions -- so the legacy comparison is scoped to what they
actually compute. That scope is reported explicitly rather than glossed.

Exit status is 0 only if all three agree everywhere they overlap.
"""

from __future__ import annotations

import re
import subprocess
import sys
from fractions import Fraction
from pathlib import Path

from enumerate_degeneracies import CHECKPOINTS, degeneracy_groups, sweep
from orbifold_enum import enumerate_by_sum, power_sum, signature

REPO = Path(__file__).resolve().parent.parent
ORACLE = REPO / "review" / "audit-independent.py"
LEGACY = REPO / "code" / "legacy"
MAIN_TEX = REPO / "paper" / "main.tex"

ANSI = re.compile(r"\x1b\[[0-9;]*m")


class Report:
    def __init__(self) -> None:
        self.agreements: list[str] = []
        self.disagreements: list[str] = []
        self.notes: list[str] = []

    def agree(self, label: str, detail: str = "") -> None:
        self.agreements.append(label)
        print(f"  AGREE     {label}" + (f"  [{detail}]" if detail else ""))

    def disagree(self, label: str, detail: str) -> None:
        self.disagreements.append(f"{label}: {detail}")
        print(f"  DISAGREE  {label}")
        print(f"            {detail}")

    def note(self, text: str) -> None:
        self.notes.append(text)
        print(f"  NOTE      {text}")


# --------------------------------------------------------------------------
# This harness
# --------------------------------------------------------------------------

def harness_enum_18() -> dict[tuple[int, tuple[int, ...]], tuple[Fraction, str]]:
    """(S_1, triple) -> (R, status) for 10 <= S_1 <= 18, from this harness."""
    out = {}
    for S in range(10, 19):
        colliding = set()
        for g in degeneracy_groups(S):
            colliding.update(g.triples)
        for orders in enumerate_by_sum(3, S):
            _, num, den = signature(orders)
            out[(S, orders)] = (
                Fraction(num, den),
                "collision" if orders in colliding else "unique",
            )
    return out


# --------------------------------------------------------------------------
# The oracle
# --------------------------------------------------------------------------

def run_oracle(rep: Report) -> dict | None:
    """
    Run review/audit-independent.py and parse the quantities it reports.

    The oracle is executed as-is and never modified. It is read-only input to
    this comparison.
    """
    if not ORACLE.exists():
        rep.disagree("oracle present", f"{ORACLE} not found")
        return None

    print(f"  running the oracle ({ORACLE.relative_to(REPO)}) -- this is the slow step")
    proc = subprocess.run(
        [sys.executable, str(ORACLE), str(MAIN_TEX)],
        capture_output=True, text=True, cwd=str(REPO),
    )
    text = proc.stdout

    parsed: dict = {"returncode": proc.returncode, "checkpoints": {}}

    m = re.search(r"=====\s*(\d+) passed,\s*(\d+) FAILED\s*=====", text)
    if m:
        parsed["passed"] = int(m.group(1))
        parsed["failed"] = int(m.group(2))
    else:
        rep.disagree("oracle summary", "could not parse the oracle's PASS/FAIL summary")
        return None

    # The oracle prints "  S | paper | pairs | classes" then rows.
    for line in text.splitlines():
        row = re.match(r"^\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*$", line)
        if row:
            S, paper, pairs, classes = (int(g) for g in row.groups())
            parsed["checkpoints"][S] = {"paper": paper, "pairs": pairs, "classes": classes}

    m = re.search(r"power-law exponent \(mine, pairs\):\s*([0-9.]+)", text)
    if m:
        parsed["exponent"] = float(m.group(1))

    if proc.returncode != 0:
        rep.note(f"oracle exited {proc.returncode}")
    return parsed


# --------------------------------------------------------------------------
# Legacy
# --------------------------------------------------------------------------

def run_legacy_table(rep: Report) -> dict[tuple[int, tuple[int, ...]], tuple[Fraction, str]] | None:
    """Run code/legacy/table_data.py and parse its printed table."""
    script = LEGACY / "table_data.py"
    if not script.exists():
        rep.disagree("legacy table_data.py present", f"{script} not found")
        return None

    proc = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True, cwd=str(LEGACY),
    )
    if proc.returncode != 0:
        rep.disagree("legacy table_data.py runs", f"exit {proc.returncode}: {proc.stderr[:300]}")
        return None

    rows: dict[tuple[int, tuple[int, ...]], tuple[Fraction, str]] = {}
    last_S: int | None = None
    for raw in proc.stdout.splitlines():
        line = ANSI.sub("", raw)
        if "|" not in line or "(" not in line:
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != 4:
            continue
        s_cell, triple_cell, r_cell, status = parts
        if s_cell:
            if not s_cell.isdigit():
                continue          # header row, e.g. "S1 | (p, q, r) | R | Status"
            last_S = int(s_cell)
        if last_S is None:
            continue
        tm = re.match(r"\((\d+),\s*(\d+),\s*(\d+)\)$", triple_cell)
        rm = re.match(r"(\d+)/(\d+)$", r_cell)
        if not (tm and rm):
            continue
        orders = tuple(int(g) for g in tm.groups())
        rows[(last_S, orders)] = (Fraction(int(rm.group(1)), int(rm.group(2))), status)
    return rows


def run_legacy_verification(rep: Report) -> dict | None:
    """Run code/legacy/'arithmetic verification.py' and parse its findings."""
    script = LEGACY / "arithmetic verification.py"
    if not script.exists():
        rep.disagree("legacy verification script present", f"{script} not found")
        return None

    proc = subprocess.run(
        [sys.executable, str(script)], capture_output=True, text=True, cwd=str(LEGACY),
    )
    if proc.returncode != 0:
        rep.disagree(
            "legacy 'arithmetic verification.py' runs",
            f"exit {proc.returncode}: {proc.stderr.strip().splitlines()[-1] if proc.stderr else ''}",
        )
        return None

    text = proc.stdout
    out: dict = {
        "thmA_clean": "No two-coefficient collisions exist for S1 <= 17" in text,
        "unexpected": [l for l in text.splitlines() if "CRITICAL" in l or "ERROR" in l],
    }
    m = re.search(r"Signature \(S1, R\): \((\d+), (\d+)/(\d+)\)", text)
    if m:
        out["S18"] = (int(m.group(1)), Fraction(int(m.group(2)), int(m.group(3))))
    out["pillows"] = re.findall(r"O\((\d+), (\d+), (\d+)\)", text)
    out["p3"] = [int(x) for x in re.findall(r"=\s*(\d+)\s*$", text, re.MULTILINE)]
    return out


# --------------------------------------------------------------------------

def main() -> int:
    rep = Report()
    print("three-way cross-validation of the n = 3 results")
    print("sources: this harness | review/audit-independent.py | code/legacy/\n")

    mine = harness_enum_18()

    # ---------------------------------------------------------------
    print("[1/3] this harness vs. code/legacy/table_data.py  (10 <= S_1 <= 18)")
    legacy_rows = run_legacy_table(rep)
    if legacy_rows is not None:
        if set(legacy_rows) != set(mine):
            only_legacy = sorted(set(legacy_rows) - set(mine))
            only_mine = sorted(set(mine) - set(legacy_rows))
            rep.disagree(
                "triad row sets",
                f"only in legacy: {only_legacy[:5]}; only in harness: {only_mine[:5]}",
            )
        else:
            rep.agree("triad row sets", f"{len(mine)} rows, identical")

        bad_R = [k for k in mine if k in legacy_rows and legacy_rows[k][0] != mine[k][0]]
        if bad_R:
            rep.disagree(
                "exact R values",
                "; ".join(
                    f"S={S} {o}: legacy {legacy_rows[(S,o)][0]} vs harness {mine[(S,o)][0]}"
                    for S, o in bad_R[:5]
                ),
            )
        else:
            rep.agree("exact R values", f"{len(mine)} rows agree")

        bad_st = [k for k in mine if k in legacy_rows and legacy_rows[k][1] != mine[k][1]]
        if bad_st:
            rep.disagree(
                "unique/collision status",
                "; ".join(
                    f"S={S} {o}: legacy {legacy_rows[(S,o)][1]} vs harness {mine[(S,o)][1]}"
                    for S, o in bad_st[:5]
                ),
            )
        else:
            n_coll = sum(1 for v in mine.values() if v[1] == "collision")
            rep.agree("unique/collision status", f"{n_coll} collision rows in both")

    # ---------------------------------------------------------------
    print("\n[2/3] this harness vs. code/legacy/'arithmetic verification.py'")
    legacy_ver = run_legacy_verification(rep)
    if legacy_ver is not None:
        harness_le17 = [S for S in range(10, 18) if degeneracy_groups(S)]
        if legacy_ver["thmA_clean"] and not harness_le17:
            rep.agree("Theorem A: no collision for S_1 <= 17")
        else:
            rep.disagree(
                "Theorem A",
                f"legacy clean={legacy_ver['thmA_clean']}, harness collisions at {harness_le17}",
            )

        g18 = degeneracy_groups(18)
        mine18 = (18, g18[0].R) if len(g18) == 1 else None
        if legacy_ver.get("S18") == mine18:
            rep.agree("S = 18 signature", f"both report (18, {g18[0].R})")
        else:
            rep.disagree(
                "S = 18 signature",
                f"legacy {legacy_ver.get('S18')} vs harness {mine18}",
            )

        legacy_pillows = {tuple(int(x) for x in t) for t in legacy_ver["pillows"]}
        mine_pillows = set(g18[0].triples) if g18 else set()
        if legacy_pillows == mine_pillows:
            rep.agree("colliding pillows", f"{sorted(mine_pillows)}")
        else:
            rep.disagree(
                "colliding pillows",
                f"legacy {sorted(legacy_pillows)} vs harness {sorted(mine_pillows)}",
            )

        mine_p3 = [power_sum(t, 3) for t in g18[0].triples] if g18 else []
        if legacy_ver["p3"] and legacy_ver["p3"][-2:] == mine_p3:
            rep.agree("P_3 values", f"{mine_p3}")
        else:
            rep.disagree("P_3 values", f"legacy {legacy_ver['p3'][-2:]} vs harness {mine_p3}")

        if legacy_ver["unexpected"]:
            rep.disagree("legacy reported a problem", "; ".join(legacy_ver["unexpected"]))

    rep.note(
        "legacy coverage stops at S_1 = 18 and contains no assertions; "
        "the S <= 600 sweep has no legacy counterpart"
    )

    # ---------------------------------------------------------------
    print("\n[3/3] this harness vs. review/audit-independent.py  (S <= 600)")
    oracle = run_oracle(rep)
    if oracle is not None:
        if oracle.get("failed", 1) == 0:
            rep.agree("oracle self-consistency", f"{oracle['passed']} checks, 0 failed")
        else:
            rep.disagree("oracle self-consistency", f"{oracle['failed']} oracle checks failed")

        records, _ = sweep(10, max(CHECKPOINTS))
        by_S = {r.S: r for r in records}

        if not oracle["checkpoints"]:
            rep.disagree("oracle checkpoints", "no checkpoint rows parsed from oracle output")
        for S, vals in sorted(oracle["checkpoints"].items()):
            if S not in by_S:
                rep.disagree(f"checkpoint S={S}", "absent from harness sweep")
                continue
            rec = by_S[S]
            ok_p = rec.cum_pairs == vals["pairs"]
            ok_c = rec.cum_classes == vals["classes"]
            ok_paper = vals["paper"] == rec.cum_pairs
            if ok_p and ok_c and ok_paper:
                rep.agree(
                    f"checkpoint S={S}",
                    f"pairs {rec.cum_pairs}, classes {rec.cum_classes}, manuscript {vals['paper']}",
                )
            else:
                rep.disagree(
                    f"checkpoint S={S}",
                    f"harness pairs={rec.cum_pairs}/classes={rec.cum_classes}; "
                    f"oracle pairs={vals['pairs']}/classes={vals['classes']}; "
                    f"manuscript={vals['paper']}",
                )

        if "exponent" in oracle:
            from enumerate_degeneracies import power_law_exponent
            mine_exp = power_law_exponent(records, "cum_pairs")
            if abs(mine_exp - oracle["exponent"]) < 5e-3:
                rep.agree(
                    "OLS exponent",
                    f"harness {mine_exp:.3f} vs oracle {oracle['exponent']:.3f}",
                )
            else:
                rep.disagree(
                    "OLS exponent",
                    f"harness {mine_exp:.4f} vs oracle {oracle['exponent']:.4f}",
                )

    # ---------------------------------------------------------------
    print(f"\n{len(rep.agreements)} agreement(s), {len(rep.disagreements)} disagreement(s)")
    if rep.disagreements:
        print("\nFAIL -- the three sources do not agree:")
        for d in rep.disagreements:
            print(f"  - {d}")
        print("\nNo source is preferred automatically. Resolve this by hand.")
        return 1
    print("PASS -- harness, oracle and legacy agree everywhere they overlap")
    return 0


if __name__ == "__main__":
    sys.exit(main())
