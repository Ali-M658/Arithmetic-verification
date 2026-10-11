#!/usr/bin/env python3
"""Regenerate Tables 1 and 2 of paper/arith/note.tex from the committed data.

    python3 paper/arith/tools/make_tables.py           # rewrite the two tabulars in note.tex
    python3 paper/arith/tools/make_tables.py --check   # exit 1 unless they are current

The tables come from the same generator as in the note's release repository
(paper/tools/release_files/note_make_tables.py), run on this repository's files:
  Table 1 (tab:fibres):  theory/diophantine/data/groups.csv and ranks.txt;
  Table 2 (tab:density): review/audit/threshold/check_enum.txt (S <= 6000), theory/diophantine/data/per_S.csv,
                         paper/arith/checks/check_note.txt; the local exponent is rounded once from the exact counts.
Only the tabular inside each table environment is replaced; captions and labels stay as written. The Integers
version (paper/arith/integers/note.tex) is generated from note.tex by make_integers.py, so rerun that afterwards.
"""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
NOTE = ROOT / "paper" / "arith" / "note.tex"

spec = importlib.util.spec_from_file_location("note_make_tables", ROOT / "paper" / "tools" / "release_files" / "note_make_tables.py")
gen = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen)
gen.DATA = ROOT / "theory" / "diophantine" / "data"
gen.ENUM6000 = ROOT / "review" / "audit" / "threshold" / "check_enum.txt"
gen.NOTECHECK = ROOT / "paper" / "arith" / "checks" / "check_note.txt"


def replace(tex, label, tabular):
    """Replace the tabular of the table environment carrying \\label{label}."""
    envs = list(re.finditer(r"\\begin\{table\}.*?\\end\{table\}", tex, re.S))
    hits = [m for m in envs if f"\\label{{{label}}}" in m.group(0)]
    if len(hits) != 1:
        sys.exit(f"{label}: found {len(hits)} table environments")
    env = hits[0].group(0)
    old = re.search(r"\\begin\{tabular\}.*?\\end\{tabular\}\n", env, re.S)
    new_env = env[:old.start()] + tabular + env[old.end():]
    return tex[:hits[0].start()] + new_env + tex[hits[0].end():]


def main():
    tex = NOTE.read_text(encoding="utf-8")
    new = replace(replace(tex, "tab:fibres", gen.table_fibres()), "tab:density", gen.table_density())
    if "--check" in sys.argv:
        if new != tex:
            print("Tables 1 and 2 of paper/arith/note.tex are out of date")
            return 1
        print("Tables 1 and 2 of paper/arith/note.tex are current")
        return 0
    if new != tex:
        NOTE.write_text(new, encoding="utf-8")
        print("Tables 1 and 2 of paper/arith/note.tex rewritten")
    else:
        print("Tables 1 and 2 of paper/arith/note.tex already current")
    return 0


if __name__ == "__main__":
    sys.exit(main())
