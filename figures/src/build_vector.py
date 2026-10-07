"""Rebuild the vector figures F2, F3, F4, F5, F7, F8, F9, E1, E2, E3 (each asserts its data first) and run
the data assertions of the Blender figures F1, F6 (--check: no rendering).

    python3 figures/src/build_vector.py

Used by code/run_all.sh (stage "figures vector F2-F5 F7-F9"); the rebuilt PDFs and PNG previews
must equal the committed ones byte for byte (code/data_guard.py).
"""
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for name, args in [(f, []) for f in ("F2", "F3", "F4", "F5", "F7", "F8", "F9", "E1", "E2", "E3")] + [("F1", ["--check"]), ("F6", ["--check"])]:
    r = subprocess.run([sys.executable, str(HERE / f"{name}.py"), *args])
    if r.returncode:
        sys.exit(f"{name} failed (exit {r.returncode})")
print("figures: F2-F5, F7-F9, E1-E3 rebuilt; F1, F6 data assertions passed (renders not part of the suite)")
