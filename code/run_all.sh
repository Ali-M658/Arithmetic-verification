#!/usr/bin/env bash
#
# Run the complete verification harness.
#
# Exits 0 only if every stage passes. Any failing stage -- a broken assert, a
# missing dependency, a crash -- produces a nonzero exit status. This script is
# the single command referred to in the manuscript's Appendix A.
#
#   usage:  ./run_all.sh
#
set -u -o pipefail

cd "$(dirname "$0")"

PYTHON="${PYTHON:-python3}"

bold=$(printf '\033[1m'); dim=$(printf '\033[2m'); reset=$(printf '\033[0m')
red=$(printf '\033[31m'); green=$(printf '\033[32m')
if [ ! -t 1 ]; then bold=""; dim=""; reset=""; red=""; green=""; fi

# --------------------------------------------------------------------------
# Pre-flight. Fail with an instruction, never with a traceback.
# --------------------------------------------------------------------------

if ! command -v "$PYTHON" >/dev/null 2>&1; then
    echo "${red}error:${reset} '$PYTHON' not found on PATH." >&2
    echo "Set PYTHON to a Python 3.9+ interpreter, e.g.  PYTHON=python3.12 ./run_all.sh" >&2
    exit 2
fi

"$PYTHON" - <<'PY' || exit 2
import sys
if sys.version_info < (3, 9):
    sys.stderr.write(
        f"error: Python 3.9 or newer is required; this is {sys.version.split()[0]}.\n"
    )
    raise SystemExit(2)
PY

MISSING=""
for mod in sympy mpmath; do
    "$PYTHON" -c "import $mod" >/dev/null 2>&1 || MISSING="$MISSING $mod"
done

if [ -n "$MISSING" ]; then
    echo "${red}error:${reset} missing required package(s):$MISSING" >&2
    echo >&2
    echo "Install them with:" >&2
    echo "    ${PYTHON} -m pip install -r requirements.txt" >&2
    echo >&2
    echo "or directly:" >&2
    echo "    ${PYTHON} -m pip install${MISSING}" >&2
    exit 2
fi

echo "${bold}verification harness -- hyperbolic triangular pillows${reset}"
echo "${dim}python:  $("$PYTHON" -c 'import sys;print(sys.version.split()[0])')"
echo "sympy:   $("$PYTHON" -c 'import sympy;print(sympy.__version__)')"
echo "mpmath:  $("$PYTHON" -c 'import mpmath;print(mpmath.__version__)')${reset}"
echo

# --------------------------------------------------------------------------
# Stages
# --------------------------------------------------------------------------

STAGE_NAMES=()
STAGE_STATUS=()
FAILED=0

run_stage() {
    local label="$1"; shift
    echo "${bold}==> ${label}${reset}"
    if "$@"; then
        STAGE_NAMES+=("$label"); STAGE_STATUS+=("PASS")
        echo "${green}--- ${label}: PASS${reset}"
    else
        local rc=$?
        STAGE_NAMES+=("$label"); STAGE_STATUS+=("FAIL(exit $rc)")
        FAILED=1
        echo "${red}--- ${label}: FAIL (exit $rc)${reset}"
    fi
    echo
}

run_stage "1. enumerator self-test"      "$PYTHON" orbifold_enum.py
run_stage "2. displayed identities"      "$PYTHON" verify_identities.py
run_stage "3. degeneracy enumeration"    "$PYTHON" enumerate_degeneracies.py
run_stage "4. LaTeX table generation"    "$PYTHON" make_table.py
run_stage "5. three-way cross-check"     "$PYTHON" cross_check.py
run_stage "6. claim-ledger coverage"     "$PYTHON" coverage_report.py

# --------------------------------------------------------------------------
# Summary
# --------------------------------------------------------------------------

echo "${bold}summary${reset}"
for i in "${!STAGE_NAMES[@]}"; do
    status="${STAGE_STATUS[$i]}"
    if [ "$status" = "PASS" ]; then
        printf "  %s%-6s%s %s\n" "$green" "$status" "$reset" "${STAGE_NAMES[$i]}"
    else
        printf "  %s%-6s%s %s\n" "$red" "$status" "$reset" "${STAGE_NAMES[$i]}"
    fi
done
echo

if [ "$FAILED" -ne 0 ]; then
    echo "${red}${bold}FAIL${reset} -- one or more stages failed. See the output above."
    exit 1
fi

echo "${green}${bold}PASS${reset} -- every stage passed."
exit 0
