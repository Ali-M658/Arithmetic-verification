#!/usr/bin/env python3
"""Guard the committed files while a verification stage runs.

    data_guard.py snapshot DIR    copy every tracked file into DIR and record its SHA-256
    data_guard.py verify   DIR    compare the tracked files with the snapshot; for every file
                                  that differs (or vanished) print it, restore it from the
                                  snapshot, and exit 1

A stage may regenerate a committed output (several scripts write their own table or
transcript). That is allowed only if the result is byte-identical: a stage that changes a
committed file has failed to reproduce it, and the original is put back so that a failed
run never leaves the repository altered.

Outside a git work tree (a source tarball) there is no list of tracked files; snapshot then
records that and verify passes with a note. Exit status 0 = unchanged, 1 = changed, 2 = usage.
"""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def tracked():
    try:
        out = subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT, stderr=subprocess.DEVNULL)
    except (OSError, subprocess.CalledProcessError):
        return None
    return sorted(f for f in out.decode().split("\0") if f)


def sha(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def snapshot(d):
    files = tracked()
    d.mkdir(parents=True, exist_ok=True)
    if files is None:
        (d / "manifest.json").write_text(json.dumps({"git": False}))
        print("data_guard: not a git work tree; committed-file guard disabled", file=sys.stderr)
        return 0
    man = {}
    for f in files:
        src = ROOT / f
        if not src.is_file():          # a tracked file already deleted in the work tree
            man[f] = None
            continue
        dst = d / "files" / f
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        man[f] = sha(src)
    (d / "manifest.json").write_text(json.dumps({"git": True, "files": man}))
    return 0


def verify(d):
    man = json.loads((d / "manifest.json").read_text())
    if not man["git"]:
        return 0
    bad = []
    for f, h in man["files"].items():
        if h is None:
            continue
        cur = ROOT / f
        if not cur.is_file() or sha(cur) != h:
            bad.append(f)
            shutil.copy2(d / "files" / f, cur)
    if bad:
        print("data_guard: the stage changed committed files (restored):", file=sys.stderr)
        for f in bad:
            print("  " + f, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] not in ("snapshot", "verify"):
        print(__doc__, file=sys.stderr)
        sys.exit(2)
    d = Path(sys.argv[2])
    sys.exit(snapshot(d) if sys.argv[1] == "snapshot" else verify(d))
