#!/bin/bash
# Run every verification script of theory/revision/ (from the repository root or anywhere).
# Exits nonzero if any script fails.  About one minute.
set -u
cd "$(dirname "$0")/../.."
PY=${PY:-/opt/homebrew/Caskroom/miniforge/base/bin/python3}
status=0
for s in check_lemma25 check_remark412 check_thm12iii check_descent check_thm513 check_remark212 \
         check_prop610 check_point3P check_sharpness check_quotes check_fragments; do
  if "$PY" "theory/revision/$s.py" > /dev/null 2>&1; then echo "PASS $s"; else echo "FAIL $s"; status=1; fi
done
exit $status
