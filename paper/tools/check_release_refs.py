"""Check that every manuscript, Overleaf package, cover letter and release repository points to the new
repositories, and that the placeholders left for the authors are exactly the agreed ones.

    python3 paper/tools/check_release_refs.py

Run after make_overleaf.py and make_release.py. Checks:
  1. no file names the old repository (Ali-M658/Arithmetic-verification) or its maintainer sentence;
  2. each paper's data statement, Overleaf copy, cover letter, README, CITATION.cff and .zenodo.json name
     https://github.com/pa1aash/<its repository> and no other paper's repository as its own;
  3. every [PLACEHOLDER: ...] is one of: author contribution statement, AI-use statement, Zenodo DOI,
     preprint identifier. Prints each placeholder kind with the files it occurs in; exits 1 on any failure.
"""
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REL = Path("~/Desktop/release").expanduser()
REPO = {"A": "heat-invariants-orbifolds", "B": "eigenvalues-orbifold-signature", "N": "equal-sum-reciprocal-triples"}
URL = "https://github.com/pa1aash/"
KINDS = [("author contributions", r"author contribution"), ("AI-use statement", r"AI-use statement|use of AI tools"),
         ("Zenodo DOI", r"Zenodo DOI"), ("preprint identifier", r"preprint identifier")]
fail = []
seen = {}


def text_sources():
    """(label, paper, text) for every document to check."""
    out = []
    for paper, rel in [("A", "paper/jga/manuscript.tex"), ("A", "paper/jga/supplement.tex"), ("B", "paper/eigen/manuscript.tex"),
                       ("N", "paper/arith/note.tex"), ("N", "paper/arith/integers/note.tex"),
                       ("A", "paper/submission/cover-letter-A-AGAG.tex"), ("B", "paper/submission/cover-letter-B-AGAG.tex"),
                       ("N", "paper/submission/cover-letter-note-Integers.tex")]:
        out.append((rel, paper, (ROOT / rel).read_text(encoding="utf-8")))
    for paper, z in [("A", "paperA"), ("B", "paperB"), ("N", "note")]:
        with zipfile.ZipFile(REL / "overleaf" / f"{z}.zip") as zf:
            for n in zf.namelist():
                if n.endswith((".tex", ".md", ".bib")):
                    out.append((f"overleaf/{z}.zip:{n}", paper, zf.read(n).decode("utf-8")))
    for paper, name in REPO.items():
        for f in ("README.md", "CITATION.cff", ".zenodo.json"):
            out.append((f"release/{name}/{f}", paper, (REL / name / f).read_text(encoding="utf-8")))
    return out


def main():
    srcs = text_sources()
    for label, paper, t in srcs:
        for bad in ("Ali-M658", "Arithmetic-verification", "maintained by"):
            if bad in t:
                fail.append(f"{label}: names {bad!r}")
        own = URL + REPO[paper]
        urls = set(re.findall(re.escape(URL) + r"[\w-]+", t))
        if urls - {own}:
            fail.append(f"{label}: names {sorted(urls - {own})}, not its own repository {own}")
        for m in re.finditer(r"\[PLACEHOLDER:?\s*([^\]]*)\]", t):
            kind = [k for k, rx in KINDS if re.search(rx, m.group(1), re.I)]
            if len(kind) != 1:
                fail.append(f"{label}: placeholder of no agreed kind: [PLACEHOLDER: {m.group(1)}]")
                continue
            seen.setdefault(kind[0], set()).add(label)
    must_name = [l for l, p, t in srcs if ("Data and code" in t or "Code and data" in t or l.startswith("release/"))
                 and not l.endswith("README-OVERLEAF.md")]
    for label, paper, t in srcs:
        if label in must_name and URL + REPO[paper] not in t and not label.endswith((".bib", "supplement.tex", ".zenodo.json")):
            fail.append(f"{label}: does not name {URL + REPO[paper]}")
    for paper, name in REPO.items():
        z = json.loads((REL / name / ".zenodo.json").read_text(encoding="utf-8"))
        if z.get("license") != "mit" or len(z["creators"]) != 6 or not all(c.get("orcid") for c in z["creators"]):
            fail.append(f"release/{name}/.zenodo.json: licence or creators wrong")
    for kind, files in sorted(seen.items()):
        print(f"{kind}: {len(files)} files")
        for f in sorted(files):
            print(f"    {f}")
    missing = [k for k, _ in KINDS if k not in seen]
    if missing:
        fail.append(f"placeholder kinds never found: {missing}")
    if fail:
        print("\nFAIL\n" + "\n".join(fail))
        return 1
    print("\nPASS: every document points to its own new repository; the placeholders are exactly the four agreed kinds")
    return 0


if __name__ == "__main__":
    sys.exit(main())
