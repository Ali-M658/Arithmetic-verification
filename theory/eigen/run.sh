#!/usr/bin/env bash
# Run every verification script of theory/eigen; exit nonzero on the first failure.
set -euo pipefail
cd "$(dirname "$0")"
PY="${PY:-python3}"
for s in diameter counting remainder theorem_e necessity locality practice; do
  echo "== $s.py"
  "$PY" "$s.py"
done
echo "== all theory/eigen checks passed"
