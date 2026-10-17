"""Build the three reproducibility repositories of the papers as plain directories outside this repository.

    python3 paper/tools/make_release.py [--out DIR] [NAME ...]      build (default: all three)
    python3 paper/tools/make_release.py --test NAME [--python PY]  test one built repository
    python3 paper/tools/make_release.py --report-provenance         append the data-file comparison to TEST-REPORT.md

Repositories (written to ~/Desktop/release/<name>/ unless --out is given), one per paper:
    heat-invariants-orbifolds        Paper A, "How much of a hyperbolic orbifold does heat hear?"
    eigenvalues-orbifold-signature   Paper B, "Finitely many eigenvalues determine the signature ..."
    equal-sum-reciprocal-triples     the note, "Triples with equal sum and equal reciprocal sum"

Each repository is standalone. The scripts and data its paper needs are copied from this repository,
keeping their relative layout (every script finds its files from its own position); the few checks
that live elsewhere here are placed under checks/. The release configurations in paper/tools/
release_config.py list, for each repository, the files, the text changes made to them (each change
must apply exactly as often as stated, so that a change in the source is noticed), the steps of each
make target, the data descriptions of DATA.md and the rows of TRACE.md. The builder then writes the
README, TRACE.md, DATA.md (with SHA-256 checksums), SHA256SUMS, the Makefile, the environment files,
LICENSE (MIT, text fetched from spdx.org), LICENSE-DATA (CC-BY-4.0 legal code, fetched from
creativecommons.org), CITATION.cff, .zenodo.json and a GitHub workflow. Finally every text file is
scanned for strings that must not appear in a release (paths of this repository, review history,
the old repository, earlier target journals, AI tools); any hit stops the build.

--test copies the built repository to a fresh temporary directory, creates its environment there
from scratch (python -m venv, pip install -r requirements.txt and requirements-pari.txt), runs
`make verify` and then `make all` (memory pressure is checked before each), and appends the results
and timings to ~/Desktop/release/TEST-REPORT.md.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request
from fnmatch import fnmatchcase as _fnmatchcase
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(HERE))
import release_config as C  # noqa: E402

OUT = Path(os.path.expanduser("~/Desktop/release"))


def fnmatchcase(name, pat):
    """Glob match in which * and ? do not cross a /, as in a shell."""
    rx, i = "", 0
    while i < len(pat):
        c = pat[i]
        if c == "*":
            rx += "[^/]*"
        elif c == "?":
            rx += "[^/]"
        elif c == "[":
            j = pat.index("]", i)
            rx += pat[i:j + 1]
            i = j
        else:
            rx += re.escape(c)
        i += 1
    return re.fullmatch(rx, name) is not None
TEXT_EXT = (".py", ".c", ".h", ".sh", ".md", ".txt", ".tex", ".csv", ".json", ".yml", ".yaml", ".cff", ".time",
            "Makefile", ".gitignore", ".bib")

LICENCES = {
    # name: (url, how to read the text, SHA-256 of the text)
    "MIT": ("https://spdx.org/licenses/MIT.json", "spdx-json",
            "b05785f9f18e6716bab63424b11454513b9943a222595b70411009202fc592b5"),
    "CC-BY-4.0": ("https://creativecommons.org/licenses/by/4.0/legalcode.txt", "text",
                  "9ba9550ad48438d0836ddab3da480b3b69ffa0aac7b7878b5a0039e7ab429411"),
}
_lic_cache = {}


def fetch_licence(name):
    if name in _lic_cache:
        return _lic_cache[name]
    url, kind, digest = LICENCES[name]
    req = urllib.request.Request(url, headers={"User-Agent": "release-builder"})
    with urllib.request.urlopen(req, timeout=60) as r:
        raw = r.read()
    text = json.loads(raw)["licenseText"] if kind == "spdx-json" else raw.decode("utf-8")
    got = hashlib.sha256(text.encode("utf-8")).hexdigest()
    if got != digest:
        sys.exit(f"the {name} text fetched from {url} has changed (SHA-256 {got}); review it and update LICENCES")
    _lic_cache[name] = text
    return text


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def human(n):
    if n < 1024:
        return f"{n} B"
    if n < 1024 ** 2:
        return f"{n / 1024:.1f} KB"
    return f"{n / 1024 ** 2:.2f} MB"


def is_text(p):
    return str(p).endswith(TEXT_EXT) or p.name in ("Makefile", ".gitignore", "latexmkrc")


def tracked():
    out = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout.decode()
    return sorted(f for f in out.split("\0") if f)


# ------------------------------------------------------------------------------------------------ copy
def placements(cfg):
    """{destination path: source path in this repository} for the configured copies (tracked files only)."""
    files = tracked()
    placed = {}
    for src_pat, dst in cfg["copy"]:
        hits = [f for f in files if fnmatchcase(f, src_pat)]
        if not hits:
            sys.exit(f"{cfg['name']}: no tracked file matches {src_pat}")
        for f in hits:
            if dst is None:
                target = f
            elif dst.endswith("/"):
                base = src_pat.split("*")[0]
                base = base if base.endswith("/") else base.rsplit("/", 1)[0] + "/"
                target = dst + f[len(base):]
            else:
                target = dst
            if target in placed and placed[target] != f:
                sys.exit(f"{cfg['name']}: {target} would come from both {placed[target]} and {f}")
            placed[target] = f
    return placed


def copy_files(cfg, dest):
    """Copy the configured files byte for byte (shutil.copy2: binary, no newline or encoding change)."""
    placed = placements(cfg)
    for target, f in placed.items():
        p = dest / target
        p.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / f, p)
        os.chmod(p, 0o755 if f.endswith((".sh",)) or (ROOT / f).stat().st_mode & 0o100 else 0o644)
    for target, src in cfg.get("extra", {}).items():
        p = dest / target
        p.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(HERE / "release_files" / src, p)
    return placed


def read_exact(p):
    """Text without newline translation, so that \r\n (the csv module's default) survives an edit."""
    with open(p, encoding="utf-8", newline="") as fh:
        return fh.read()


def write_exact(p, t):
    with open(p, "w", encoding="utf-8", newline="") as fh:
        fh.write(t)


def apply_edits(cfg, dest):
    """Per-file edits (each checked to apply as often as stated), then the substitutions of every text file."""
    jobs = [(pat, e, False) for pat, e in C.COMMON_EDITS.items()] + [(pat, e, True) for pat, e in cfg.get("edits", {}).items()]
    for pat, edits, required in jobs:
        targets = [p for p in dest.rglob("*") if p.is_file() and fnmatchcase(p.relative_to(dest).as_posix(), pat)]
        if not targets and required:
            sys.exit(f"{cfg['name']}: edit target {pat} not found")
        for p in targets:
            t_orig = t = read_exact(p)
            for old, new, count in edits:
                if old.startswith("re:"):
                    t, n = re.subn(old[3:], new, t, flags=re.M | re.S)
                else:
                    n = t.count(old)
                    t = t.replace(old, new)
                if count is not None and n != count:
                    sys.exit(f"{cfg['name']}: edit of {p.relative_to(dest)} applied {n} times, expected {count}: {old[:80]!r}")
            if t != t_orig:
                write_exact(p, t)
    for p in sorted(dest.rglob("*")):
        if not p.is_file() or not is_text(p):
            continue
        rel = p.relative_to(dest).as_posix()
        if any(fnmatchcase(rel, pat) for pat in cfg.get("verbatim", [])):
            continue
        t0 = t = read_exact(p)
        for old, new in C.GLOBAL_SUBS + cfg.get("subs", []):
            t = re.sub(old[3:], new, t, flags=re.M) if old.startswith("re:") else t.replace(old, new)
        if t != t0:
            write_exact(p, t)
    for rel in cfg.get("delete", []):
        p = dest / rel
        if p.exists():
            p.unlink()


# --------------------------------------------------------------------------------------------- generate
def data_files(cfg, dest):
    out = []
    for p in sorted(dest.rglob("*")):
        rel = p.relative_to(dest).as_posix()
        def m(pat):
            return fnmatchcase(p.name if "/" not in pat else rel, pat)
        if p.is_file() and any(m(pat) for pat in C.DATA_PATTERNS) and not any(m(pat) for pat in C.NOT_DATA):
            out.append(rel)
    return out


def describe(cfg, rel):
    hits = [m for m in cfg["data"] if fnmatchcase(rel, m[0])]
    if len(hits) != 1:
        sys.exit(f"{cfg['name']}: data file {rel} matches {len(hits)} descriptions in DATA (need exactly one)")
    return hits[0]


def write_data_md(cfg, dest):
    files = data_files(cfg, dest)
    used = set()
    rows, sums, total = [], [], 0
    for rel in files:
        m = describe(cfg, rel)
        used.add(m[0])
        size = (dest / rel).stat().st_size
        total += size
        d = sha256(dest / rel)
        sums.append(f"{d}  {rel}")
        rows.append(f"| `{rel}` | {human(size)} | `{d}` | {m[1]} | {m[2]} |")
    unused = [m[0] for m in cfg["data"] if m[0] not in used]
    if unused:
        sys.exit(f"{cfg['name']}: DATA descriptions match no file: {unused}")
    (dest / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8")
    head = [
        "# Data", "",
        f"Every data file of this repository: {len(files)} files, {human(total)}. For each, its size, its SHA-256 "
        "checksum, the script that produces it and the element of the paper it supports. `make data-check` "
        "compares every file with the checksums in `SHA256SUMS`. Every step of `make` also fails if it changes "
        "one of these files: regenerating committed data is a reproduction test, and the result must be "
        "byte-identical.", "",
        "Licence: CC-BY-4.0 (`LICENSE-DATA`).", "",
        "| file | size | SHA-256 | produced by | paper element |", "|---|---|---|---|---|",
    ]
    (dest / "DATA.md").write_text("\n".join(head + rows) + "\n", encoding="utf-8")
    return len(files), total


def endings(b):
    """Line-ending signature of a byte string: (CRLF count, lone LF count, lone CR count, ends with newline)."""
    crlf = b.count(b"\r\n")
    return crlf, b.count(b"\n") - crlf, b.count(b"\r") - crlf, b.endswith(b"\n")


def provenance(cfg, dest):
    """Compare every data file of the release with its source in this repository.

    A data file copied from this repository must have the same SHA-256 as its source, unless it is listed
    in the repository's `edited_data` (a text edit of the configuration changes it on purpose); such a
    file must keep the source's line endings and differ only in lines touched by the edit. Files written
    by the builder itself (`generated_data`) have no source. Any other difference stops the build.
    Returns the rows for the report: (path, source, size, sha_release, sha_source, status, note)."""
    import difflib
    placed = placements(cfg)
    extra = {t: "release_files/" + s for t, s in cfg.get("extra", {}).items()}
    rows, bad = [], []
    edited = cfg.get("edited_data", {})
    for rel in data_files(cfg, dest):
        rb = (dest / rel).read_bytes()
        hr = hashlib.sha256(rb).hexdigest()
        if rel in placed:
            sb = (ROOT / placed[rel]).read_bytes()
            hs = hashlib.sha256(sb).hexdigest()
            if hr == hs:
                rows.append((rel, placed[rel], len(rb), hr, hs, "identical", ""))
                continue
            if rel not in edited:
                bad.append(f"{rel}: SHA-256 differs from {placed[rel]} and the file is not a declared edit")
                rows.append((rel, placed[rel], len(rb), hr, hs, "MISMATCH", "undeclared"))
                continue
            if endings(rb) != endings(sb):
                bad.append(f"{rel}: line endings changed ({endings(sb)} -> {endings(rb)})")
            sl, rl = sb.decode("utf-8").splitlines(True), rb.decode("utf-8").splitlines(True)
            changed = sum(1 for l in difflib.unified_diff(sl, rl, n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---"))
            rows.append((rel, placed[rel], len(rb), hr, hs, "edited", f"{edited[rel]} ({changed} changed lines)"))
        elif rel in extra:
            hs = sha256(HERE / extra[rel])
            rows.append((rel, f"paper/tools/{extra[rel]}", len(rb), hr, hs, "identical" if hs == hr else "MISMATCH", ""))
            if hs != hr:
                bad.append(f"{rel}: differs from paper/tools/{extra[rel]}")
        elif any(fnmatchcase(rel, g) for g in cfg.get("generated_data", [])):
            rows.append((rel, "(written by the builder)", len(rb), hr, "", "generated", "extracted from the paper's source"))
        else:
            bad.append(f"{rel}: data file with no source and not declared as generated")
    unused = [e for e in edited if not any(r[0] == e and r[5] == "edited" for r in rows)]
    if unused:
        bad.append(f"edited_data entries that are not edited data files: {unused}")
    if bad:
        sys.exit(f"{cfg['name']}: data provenance check failed:\n  " + "\n  ".join(bad))
    return rows


def provenance_text(name, rows):
    """The comparison as a section of TEST-REPORT.md (outside the repositories)."""
    n = {k: sum(1 for r in rows if r[5] == k) for k in ("identical", "edited", "generated")}
    lines = [f"## {name}: data files against their sources", "",
             f"{len(rows)} data files: {n['identical']} byte-identical to their source in the development repository, "
             f"{n['edited']} changed on purpose by a declared text edit (line endings unchanged), {n['generated']} written "
             "by the builder. No other difference (the build asserts this).", ""]
    special = [r for r in rows if r[5] != "identical"]
    if special:
        lines += ["| file | source | status | SHA-256 (release) | SHA-256 (source) | note |", "|---|---|---|---|---|---|"]
        for rel, src, size, hr, hs, st, note in special:
            lines.append(f"| `{rel}` | `{src}` | {st} | `{hr[:16]}…` | `{hs[:16] + '…' if hs else ''}` | {note} |")
        lines.append("")
    lines += ["<details><summary>every file</summary>", "", "| file | source | bytes | SHA-256 | status |", "|---|---|---|---|---|"]
    for rel, src, size, hr, hs, st, note in rows:
        lines.append(f"| `{rel}` | `{src}` | {size} | `{hr}` | {st} |")
    lines += ["", "</details>", ""]
    return n, "\n".join(lines)


def report_provenance():
    """Append the data-file comparison of every built repository to TEST-REPORT.md."""
    report = OUT / "TEST-REPORT.md"
    parts = ["\n# Data files of the releases against their sources\n",
             "`make_release.py` copies every file byte for byte (`shutil.copy2`); the only later writes to copied "
             "files are the configured text edits, which read and write without newline translation and only when an "
             "edit applies. At the end of every build it compares the SHA-256 of each data file with that of its source "
             "in the development repository and stops on any difference that is not a declared edit (and on any change "
             "of line endings in a declared edit). The comparison below was made on the directories that were tested.\n"]
    for name, cfg in C.REPOS.items():
        parts.append(provenance_text(name, provenance(cfg, OUT / name))[1])
    with open(report, "a", encoding="utf-8") as fh:
        fh.write("\n".join(parts) + "\n")
    print(f"appended the data-file comparison to {report}")


def write_steps(cfg, dest):
    steps = cfg["steps"]
    names = [s["name"] for s in steps]
    if len(set(names)) != len(names):
        sys.exit(f"{cfg['name']}: duplicate step names")
    for s in steps:
        for t in s["targets"]:
            assert t in ("verify", "full", "figures", "tables"), (s["name"], t)
        if s.get("transcript") and not (dest / s["transcript"]).is_file():
            sys.exit(f"{cfg['name']}: step {s['name']}: transcript {s['transcript']} missing")
        if not (dest / s.get("dir", ".")).is_dir():
            sys.exit(f"{cfg['name']}: step {s['name']}: directory {s.get('dir')} missing")
    (dest / "tools").mkdir(exist_ok=True)
    (dest / "tools" / "steps.json").write_text(json.dumps(steps, indent=1) + "\n", encoding="utf-8")
    shutil.copy2(HERE / "release_files" / "steps.py", dest / "tools" / "steps.py")


def minutes(cfg, target, optional=False):
    """Expected minutes of a target: the core steps, or (optional=True) the steps that need NGSolve or Blender."""
    sel = [s for s in cfg["steps"] if (target == "all" or target in s["targets"])
           and (s.get("needs", "python") in ("ngsolve", "blender")) == optional]
    return sum(s.get("minutes", 1) for s in sel)


def write_makefile(cfg, dest):
    m = {}
    for tg in ("verify", "full", "figures", "tables", "all"):
        core, opt = minutes(cfg, tg), minutes(cfg, tg, optional=True)
        m[tg] = (core, opt)

    def rng(x):
        core, opt = x
        f = lambda y: f"about {max(1, round(y))} min" if y < 90 else f"about {y / 60:.1f} h"
        return f(core) + (f", plus {f(opt)} with the optional NGSolve/Blender steps" if opt else "")
    opt = cfg.get("optional_note", "")
    lines = [
        "# Reproduce the computations of the paper. `make help` lists the targets and their run times.",
        "# Each target prints PASS, FAIL or SKIP for every step and exits nonzero if any step fails.",
        "PYTHON ?= python3",
        "export PYTHON",
        "STEPS = $(PYTHON) tools/steps.py",
        "",
        ".PHONY: help verify full figures tables data-check all clean",
        "",
        "help:",
        f"\t@echo 'make verify      fast exact checks ({rng(m['verify'])})'",
        f"\t@echo 'make full        long computations ({rng(m['full'])})'",
        f"\t@echo 'make figures     rebuild every figure and compare with the committed files ({rng(m['figures'])})'",
        f"\t@echo 'make tables      regenerate every table and compare with the committed files ({rng(m['tables'])})'",
        "\t@echo 'make data-check  compare every data file with SHA256SUMS (seconds)'",
        f"\t@echo 'make all         everything above ({rng(m['all'])})'",
        "\t@echo 'make clean       remove caches and compiled helpers'",
        "\t@echo ''",
        "\t@echo 'Times measured on an Apple M-series laptop with 8 GB of memory. PYTHON selects the interpreter (default python3).'",
    ]
    for line in opt.splitlines():
        lines.append(f"\t@echo '{line}'")
    lines += [
        "\t@echo 'Run `python3 tools/steps.py --list` for every step.'",
        "",
        "verify:\n\t@$(STEPS) verify",
        "full:\n\t@$(STEPS) full",
        "figures:\n\t@$(STEPS) figures",
        "tables:\n\t@$(STEPS) tables",
        "data-check:\n\t@$(STEPS) data-check",
        "all:\n\t@$(STEPS) all",
        "clean:",
        "\tfind . -name __pycache__ -type d -prune -exec rm -rf {} +",
    ]
    for c in cfg.get("clean", []):
        lines.append(f"\trm -rf {c}")
    (dest / "Makefile").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return m


def write_trace(cfg, dest):
    known = {s["name"] for s in cfg["steps"]}
    head = ["# Trace: every checkable item of the paper", "",
            f"*{cfg['paper']}*. Numbering is that of the submitted version of the paper"
            + (" and its supplement (S-numbers)" if cfg.get("supplement") else "") + ". "
            "Each row names the item, the script that proves, checks or computes it, and the make target that runs "
            "it. A step name in the last column is the name printed by `make` (see `python3 tools/steps.py --list`).", "",
            "| item | statement | script | make target (step) |", "|---|---|---|---|"]
    rows = []
    for item, what, script, step in cfg["trace"]:
        for s in [x.strip() for x in step.split(";")]:
            if s and s not in known:
                sys.exit(f"{cfg['name']}: TRACE row {item!r} names unknown step {s!r}")
        tg = sorted({t for s in step.split(";") for x in cfg["steps"] if x["name"] == s.strip() for t in x["targets"]},
                    key=["verify", "tables", "figures", "full"].index)
        cell = ", ".join(f"`make {t}`" for t in tg) + (f" ({step})" if step else "")
        if not step:
            cell = "none: by hand or quoted from the cited source (see the statement)"
        rows.append(f"| {item} | {what} | {script} | {cell} |")
    for s in [x for x in cfg["trace"] if x[2]]:
        for path in re.findall(r"`([^`]+\.(?:py|c|sh))`", s[2]):
            if not (dest / path).is_file():
                sys.exit(f"{cfg['name']}: TRACE names {path}, which is not in the repository")
    (dest / "TRACE.md").write_text("\n".join(head + rows) + "\n", encoding="utf-8")


def write_env(cfg, dest):
    (dest / "requirements.txt").write_text(C.REQUIREMENTS, encoding="utf-8")
    if cfg.get("pari"):
        (dest / "requirements-pari.txt").write_text(C.REQUIREMENTS_PARI, encoding="utf-8")
    if cfg.get("optional_env"):
        (dest / "requirements-optional.txt").write_text(cfg["optional_env"], encoding="utf-8")
    (dest / ".gitignore").write_text("__pycache__/\n*.pyc\n.venv/\n.venv-*/\n" + "".join(c + "\n" for c in cfg.get("clean", [])),
                                     encoding="utf-8")


def write_licences(dest):
    holders = "The authors: " + ", ".join(a["given"] + " " + a["family"] for a in C.AUTHORS)
    mit = fetch_licence("MIT").replace("<year> <copyright holders>", f"2026 {holders}")
    if "<year>" in mit or "<copyright holders>" in mit:
        sys.exit("MIT template placeholders not filled")
    (dest / "LICENSE").write_text(mit, encoding="utf-8")
    cc = fetch_licence("CC-BY-4.0")
    (dest / "LICENSE-DATA").write_text(
        f"The data, figures and text of this repository are Copyright (c) 2026 {holders},\n"
        "licensed under the Creative Commons Attribution 4.0 International licence, whose legal code follows.\n"
        "The code is licensed under the MIT licence (LICENSE).\n\n" + cc, encoding="utf-8")


def write_metadata(cfg, dest):
    a_cff = []
    for a in C.AUTHORS:
        a_cff += [f"  - family-names: \"{a['family']}\"", f"    given-names: \"{a['given']}\"",
                  f"    orcid: \"https://orcid.org/{a['orcid']}\"", f"    affiliation: \"{a['affiliation']}\""]
    cff = ["cff-version: 1.2.0",
           f"message: \"If you use this software or data, please cite the archived version and the paper.\"",
           f"title: \"Code and data for: {cfg['paper']}\"",
           "type: software", "authors:"] + a_cff
    cff += [f"repository-code: \"https://github.com/pa1aash/{cfg['name']}\"",
            "license: MIT",
            "doi: \"[PLACEHOLDER: Zenodo DOI]\"",
            "keywords:"] + [f"  - \"{k}\"" for k in cfg["keywords"]]
    cff += ["preferred-citation:", "  type: article", f"  title: \"{cfg['paper']}\"", "  authors:"]
    for a in C.AUTHORS:
        cff += [f"    - family-names: \"{a['family']}\"", f"      given-names: \"{a['given']}\"",
                f"      orcid: \"https://orcid.org/{a['orcid']}\""]
    cff += ["  identifiers:", "    - type: other", "      value: \"[PLACEHOLDER: preprint identifier]\"",
            "      description: \"preprint of the paper\""]
    (dest / "CITATION.cff").write_text("\n".join(cff) + "\n", encoding="utf-8")
    z = {
        "title": f"Code and data for: {cfg['paper']}",
        "upload_type": "software",
        "description": cfg["zenodo_description"],
        "creators": [{"name": f"{a['family']}, {a['given']}", "orcid": a["orcid"], "affiliation": a["affiliation"]}
                     for a in C.AUTHORS],
        "keywords": cfg["keywords"],
        "access_right": "open",
        "license": "mit",
        "notes": "Code: MIT licence (LICENSE). Data, figures and text: CC-BY-4.0 (LICENSE-DATA).",
        "language": "eng",
        "related_identifiers": [
            {"identifier": "[PLACEHOLDER: preprint identifier]", "relation": "isSupplementTo",
             "resource_type": "publication-preprint"},
        ],
    }
    (dest / ".zenodo.json").write_text(json.dumps(z, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    wf = dest / ".github" / "workflows"
    wf.mkdir(parents=True, exist_ok=True)
    (wf / "verify.yml").write_text(
        "name: verify\n"
        "on: [push, pull_request]\n"
        "jobs:\n"
        "  verify:\n"
        "    runs-on: ubuntu-latest\n"
        "    timeout-minutes: 120\n"
        "    steps:\n"
        "      - uses: actions/checkout@v4\n"
        "      - uses: actions/setup-python@v5\n"
        "        with:\n"
        "          python-version: \"3.13\"\n"
        "      - run: python -m pip install -r requirements.txt"
        + (" -r requirements-pari.txt" if cfg.get("pari") else "") + "\n"
        "      - run: make verify\n", encoding="utf-8")


def write_readme(cfg, dest, m, ndata, total):
    def rng(x):
        core, opt = x
        f = lambda y: f"about {max(1, round(y))} min" if y < 90 else f"about {y / 60:.1f} h"
        return f(core) + (f" (plus {f(opt)} with the optional NGSolve/Blender steps)" if opt else "")
    authors = ", ".join(a["given"] + " " + a["family"] for a in C.AUTHORS)
    text = cfg["readme"].format(
        paper=cfg["paper"], authors=authors, name=cfg["name"], ndata=ndata, total=human(total),
        t_verify=rng(m["verify"]), t_full=rng(m["full"]), t_figures=rng(m["figures"]), t_tables=rng(m["tables"]),
        t_all=rng(m["all"]))
    text += "\n" + C.README_COMMON.format(paper=cfg["paper"], authors=authors, name=cfg["name"], short=cfg["short"])
    (dest / "README.md").write_text(text, encoding="utf-8")


# ------------------------------------------------------------------------------------------------- scan
def scan(cfg, dest):
    hits = []
    for p in sorted(dest.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(dest).as_posix()
        if rel in ("LICENSE", "LICENSE-DATA"):
            continue
        if not is_text(p):
            continue
        t = p.read_text(encoding="utf-8", errors="replace")
        for pat in C.FORBIDDEN + cfg.get("forbidden", []):
            for mm in re.finditer(pat, t, flags=re.M):
                line = t.count("\n", 0, mm.start()) + 1
                hits.append(f"{rel}:{line}: /{pat}/ ... {t[max(0, mm.start() - 50):mm.end() + 50]!r}")
    for p in dest.rglob("*"):
        if p.name.startswith(".") and p.name not in (".gitignore", ".zenodo.json", ".github"):
            hits.append(f"hidden file {p.relative_to(dest)}")
        if p.name in (".git", ".DS_Store") or p.suffix in (".pyc",) or p.name == "__pycache__":
            hits.append(f"forbidden file {p.relative_to(dest)}")
    return hits


REF = re.compile(r"(?<![\w./-])((?:[\w.-]+/)*[\w-]+\.(?:py|tex|md|c|sh|csv|json|txt|npz))\b")


def dangling(cfg, dest):
    """Paths named in the text files that are not in the repository (references to this repository's files)."""
    names = {p.name for p in dest.rglob("*") if p.is_file()}
    rels = {p.relative_to(dest).as_posix() for p in dest.rglob("*")}
    ok = C.DANGLING_OK | set(cfg.get("dangling_ok", []))
    hits = []
    for p in sorted(dest.rglob("*")):
        if not p.is_file() or p.suffix not in (".py", ".c", ".sh", ".md", ".txt") or p.stat().st_size > 2_000_000:
            continue
        for m in REF.finditer(p.read_text(encoding="utf-8", errors="replace")):
            s = m.group(1)
            found = (s in rels or any(r.endswith("/" + s) for r in rels)) if "/" in s else s in names
            if not found and s not in ok:
                hits.append(f"{p.relative_to(dest)}: names {s}, which is not in the repository")
    return sorted(set(hits))


def build(name):
    cfg = C.REPOS[name]
    for s in cfg["steps"]:
        m = getattr(C, "MEASURED", {}).get(name, {}).get(s["name"])
        if m:
            s["minutes"] = max(m, 0.1)
    dest = OUT / name
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    copy_files(cfg, dest)
    apply_edits(cfg, dest)
    for fn in cfg.get("post", []):
        fn(dest, ROOT)
    write_steps(cfg, dest)
    write_env(cfg, dest)
    ndata, total = write_data_md(cfg, dest)
    m = write_makefile(cfg, dest)
    write_trace(cfg, dest)
    write_licences(dest)
    write_metadata(cfg, dest)
    write_readme(cfg, dest, m, ndata, total)
    prov = provenance_text(name, provenance(cfg, dest))[0]
    hits = scan(cfg, dest) + dangling(cfg, dest)
    if hits:
        print("\n".join(hits[:200]))
        sys.exit(f"{name}: {len(hits)} forbidden strings or files (first 200 above)")
    nfiles = sum(1 for p in dest.rglob("*") if p.is_file())
    print(f"{name}: {nfiles} files, {ndata} data files ({human(total)}; {prov['identical']} identical to source, "
          f"{prov['edited']} declared edits, {prov['generated']} generated), {len(cfg['steps'])} steps -> {dest}")


# ------------------------------------------------------------------------------------------------- test
def pressure():
    try:
        out = subprocess.run(["memory_pressure", "-Q"], capture_output=True, text=True).stdout
        return int(re.search(r"(\d+)%", out).group(1))
    except Exception:  # noqa: BLE001
        return 100


def wait_memory(minfree=20):
    while pressure() < minfree:
        print(f"memory free {pressure()}% < {minfree}%: waiting 60 s", flush=True)
        time.sleep(60)


def test(name, python):
    src = OUT / name
    if not src.is_dir():
        sys.exit(f"{src} not built")
    report = OUT / "TEST-REPORT.md"
    tmp = Path(tempfile.mkdtemp(prefix=f"release-test-{name}-"))
    work = tmp / name
    shutil.copytree(src, work, copy_function=shutil.copy)  # fresh timestamps (see steps.py)
    log = []
    t0 = time.time()
    venv = work / ".venv"
    subprocess.run([python, "-m", "venv", str(venv)], check=True)
    py = str(venv / "bin" / "python")
    reqs = ["-r", "requirements.txt"] + (["-r", "requirements-pari.txt"] if (work / "requirements-pari.txt").exists() else [])
    r = subprocess.run([py, "-m", "pip", "install", "--quiet", "--only-binary", ":all:", *reqs], cwd=work,
                       capture_output=True, text=True)
    t_env = time.time() - t0
    if r.returncode:
        sys.exit(f"pip install failed:\n{r.stdout}\n{r.stderr}")
    freeze = subprocess.run([py, "-m", "pip", "freeze"], capture_output=True, text=True).stdout.split()
    results = {}
    env = dict(os.environ, PYTHON=py)
    for target in ("verify", "all"):
        wait_memory()
        t1 = time.time()
        p = subprocess.run(["make", target, f"PYTHON={py}"], cwd=work, env=env, capture_output=True, text=True)
        dt = time.time() - t1
        (OUT / f"test-{name}-{target}.log").write_text(p.stdout + p.stderr, encoding="utf-8")
        results[target] = (p.returncode, dt, p.stdout)
        print(p.stdout[-4000:])
    lines = [f"\n## {name}", "",
             f"Tested {time.strftime('%Y-%m-%d %H:%M')} on {os.uname().sysname} {os.uname().machine}, "
             f"in a fresh copy (`{tmp}`), with a new virtual environment from `{python}` "
             f"({subprocess.run([py, '-V'], capture_output=True, text=True).stdout.strip()}); "
             f"environment created in {t_env / 60:.1f} min.", "",
             "Installed: " + ", ".join(f"`{x}`" for x in freeze), ""]
    for target, (rc, dt, out) in results.items():
        steps = re.findall(r"^(?:\x1b\[\d+m)?(PASS|FAIL|SKIP)(?:\x1b\[0m)?  (.+?)(?:  \((\d+:\d\d)\))?(?:  \((.*)\))?$", out, re.M)
        lines += [f"### `make {target}`: exit {rc}, {dt / 60:.1f} min", "", "| result | step | time | note |", "|---|---|---|---|"]
        for status, step, tm, note in steps:
            lines.append(f"| {status} | {step} | {tm or ''} | {note or ''} |")
        summ = re.search(r"summary of make \S+.*", out)
        lines += ["", summ.group(0) if summ else "(no summary)", ""]
    if not report.exists():
        report.write_text("# Release repositories: fresh-copy test report\n\n"
                          "Each repository was copied to a new temporary directory, a virtual environment was created there "
                          "from scratch and the pinned requirements installed (`python3 paper/tools/make_release.py --test NAME`), "
                          "then `make verify` and `make all` were run one after the other, one repository at a time, with the "
                          "memory guard on. A SKIP is listed with its reason.\n", encoding="utf-8")
    with open(report, "a", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    ok = all(rc == 0 for rc, _, _ in results.values())
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"{name}: {'PASS' if ok else 'FAIL'}; report appended to {report}")
    return 0 if ok else 1


def main(argv):
    global OUT
    if "--out" in argv:
        OUT = Path(argv[argv.index("--out") + 1]).expanduser().resolve()
        del argv[argv.index("--out"):argv.index("--out") + 2]
    if argv and argv[0] == "--report-provenance":
        report_provenance()
        return 0
    if argv and argv[0] == "--test":
        python = argv[argv.index("--python") + 1] if "--python" in argv else sys.executable
        return test(argv[1], python)
    names = argv or list(C.REPOS)
    OUT.mkdir(parents=True, exist_ok=True)
    for n in names:
        build(n)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
