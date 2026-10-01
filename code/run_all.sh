#!/usr/bin/env bash
#
# Run every check in the repository, from committed data, with one command.
#
#   code/run_all.sh [--quick | --full] [--only REGEX] [--list]
#
#   --quick   (default) every stage that takes under about ten minutes on a laptop
#   --full    every stage, including the long searches and the NGSolve re-solve
#   --only    run only the stages whose name matches REGEX (development aid)
#   --list    print the stage names and modes and exit
#
# Each stage ends PASS, FAIL or SKIP with a reason, and its wall-clock time is printed. Exit
# status is 0 only if no stage failed; a skip is never a failure but is always printed. A
# stage also FAILs if it changes any committed file (code/data_guard.py restores the file):
# regenerating a committed output is a reproduction test, and it must be byte-identical.
#
# Environment:
#   PYTHON            interpreter for the exact-arithmetic suite (default python3); install the
#                     pinned packages with   PYTHON -m pip install -r requirements.txt
#   PYTHON_NUMERICS   interpreter with NGSolve for the re-solve stage (default numerics/.venv/bin/python
#                     if it exists); create it with
#                       python3.13 -m venv numerics/.venv && numerics/.venv/bin/pip install -r numerics/requirements.txt
#   PYTHON_PARI       interpreter with cypari2 for the rank certification (default
#                     theory/diophantine/.venv-pari/bin/python if it exists, else PYTHON); see
#                     theory/diophantine/requirements-pari.txt
#   RUN_ALL_LOGDIR    where each stage's output is kept (default: a fresh temporary directory)
#
# Appendix A of the manuscript refers to this script as the single command that reproduces the checks.
#
set -u -o pipefail

# interpreters given as relative paths are resolved against the caller's directory
abspath() { case "$1" in */*) ( cd "$(dirname "$1")" 2>/dev/null && printf '%s/%s' "$PWD" "$(basename "$1")" ) || printf '%s' "$1" ;; *) printf '%s' "$1" ;; esac; }
PYTHON="$(abspath "${PYTHON:-python3}")"
[ -n "${PYTHON_NUMERICS:-}" ] && PYTHON_NUMERICS="$(abspath "$PYTHON_NUMERICS")"
[ -n "${PYTHON_PARI:-}" ] && PYTHON_PARI="$(abspath "$PYTHON_PARI")"

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

MODE=quick
ONLY=""
LIST=0
while [ $# -gt 0 ]; do
    case "$1" in
        --quick) MODE=quick ;;
        --full)  MODE=full ;;
        --only)  shift; ONLY="${1:-}" ;;
        --list)  LIST=1 ;;
        -h|--help) sed -n '2,32p' "$0"; exit 0 ;;
        *) echo "unknown argument: $1 (see --help)" >&2; exit 2 ;;
    esac
    shift
done

bold=$(printf '\033[1m'); dim=$(printf '\033[2m'); reset=$(printf '\033[0m')
red=$(printf '\033[31m'); green=$(printf '\033[32m'); yellow=$(printf '\033[33m')
if [ ! -t 1 ]; then bold=""; dim=""; reset=""; red=""; green=""; yellow=""; fi

fmt_time() { printf "%d:%02d" $(( $1 / 60 )) $(( $1 % 60 )); }

# --------------------------------------------------------------------------
# Pre-flight. Fail with an instruction, never with a traceback.
# --------------------------------------------------------------------------

HAVE_NGSOLVE=0; HAVE_PARI=0
PYTHON_NUMERICS="${PYTHON_NUMERICS:-}"
PYTHON_PARI="${PYTHON_PARI:-}"
GUARD=1

if [ "$LIST" -eq 0 ]; then
    if ! command -v "$PYTHON" >/dev/null 2>&1; then
        echo "${red}error:${reset} '$PYTHON' not found on PATH." >&2
        echo "Set PYTHON to a Python 3.9+ interpreter, e.g.  PYTHON=python3.12 code/run_all.sh" >&2
        exit 2
    fi
    "$PYTHON" - <<'PY' || exit 2
import sys
if sys.version_info < (3, 9):
    sys.stderr.write(f"error: Python 3.9 or newer is required; this is {sys.version.split()[0]}.\n")
    raise SystemExit(2)
PY

    PREFLIGHT=$("$PYTHON" - "$ROOT/requirements.txt" <<'PY'
import importlib, re, sys
pins = {}
for line in open(sys.argv[1]):
    m = re.match(r"^([A-Za-z0-9_.-]+)==([^\s#]+)", line.strip())
    if m:
        pins[m.group(1).lower()] = m.group(2)
missing, warn, ok = [], [], []
for name, want in pins.items():
    try:
        mod = importlib.import_module(name)
        have = getattr(mod, "__version__", "?")
    except ImportError:
        missing.append(name)
        continue
    (ok if have == want else warn).append(f"{name} {have}" + ("" if have == want else f" (pinned {want})"))
print("MISSING=" + " ".join(missing))
print("WARN=" + "; ".join(warn))
print("OK=" + ", ".join(ok))
PY
    )
    MISSING=$(printf '%s\n' "$PREFLIGHT" | sed -n 's/^MISSING=//p')
    WARN=$(printf '%s\n' "$PREFLIGHT" | sed -n 's/^WARN=//p')
    HAVE=$(printf '%s\n' "$PREFLIGHT" | sed -n 's/^OK=//p')
    if [ -n "$MISSING" ]; then
        echo "${red}error:${reset} missing required package(s): $MISSING" >&2
        echo >&2
        echo "Install the pinned versions with:" >&2
        echo "    ${PYTHON} -m pip install -r ${ROOT}/requirements.txt" >&2
        echo "(or, in a fresh environment:  ${PYTHON} -m venv .venv && .venv/bin/pip install -r requirements.txt" >&2
        echo " and run  PYTHON=.venv/bin/python code/run_all.sh)" >&2
        exit 2
    fi

    # NGSolve (only the re-solve stage needs it; every check of committed CSV data does not)
    if [ -z "$PYTHON_NUMERICS" ]; then
        if [ -x "$ROOT/numerics/.venv/bin/python" ]; then PYTHON_NUMERICS="$ROOT/numerics/.venv/bin/python"; else PYTHON_NUMERICS="$PYTHON"; fi
    fi
    if "$PYTHON_NUMERICS" -c "import ngsolve" >/dev/null 2>&1; then HAVE_NGSOLVE=1; fi
    # PARI (only theory/diophantine/ranks.py)
    if [ -z "$PYTHON_PARI" ]; then
        if [ -x "$ROOT/theory/diophantine/.venv-pari/bin/python" ]; then PYTHON_PARI="$ROOT/theory/diophantine/.venv-pari/bin/python"; else PYTHON_PARI="$PYTHON"; fi
    fi
    if "$PYTHON_PARI" -c "import cypari2" >/dev/null 2>&1; then HAVE_PARI=1; fi
    if ! (cd "$ROOT" && git rev-parse --is-inside-work-tree >/dev/null 2>&1); then GUARD=0; fi

    echo "${bold}verification suite -- How much of a hyperbolic orbifold does heat hear?${reset}  [mode: $MODE]"
    echo "${dim}python:   $("$PYTHON" -c 'import sys;print(sys.version.split()[0])')   ($HAVE)"
    [ -n "$WARN" ] && echo "${yellow}note:${reset}${dim}     version differs from requirements.txt: $WARN"
    if [ "$HAVE_NGSOLVE" -eq 1 ]; then echo "ngsolve:  available ($PYTHON_NUMERICS)"
    else echo "ngsolve:  not available: the re-solve stage will be skipped (install: python3.13 -m venv numerics/.venv && numerics/.venv/bin/pip install -r numerics/requirements.txt)"; fi
    if [ "$HAVE_PARI" -eq 1 ]; then echo "pari:     available (cypari2, $PYTHON_PARI)"
    else echo "pari:     not available: ranks.py will be skipped (install: see theory/diophantine/requirements-pari.txt)"; fi
    if [ "$GUARD" -eq 0 ]; then echo "guard:    not a git work tree: committed files are not protected against rewriting"; fi
    echo "${reset}"
fi

# --------------------------------------------------------------------------
# Stage runner
# --------------------------------------------------------------------------

LOGDIR="${RUN_ALL_LOGDIR:-$(mktemp -d "${TMPDIR:-/tmp}/run_all.XXXXXX")}"
mkdir -p "$LOGDIR"
STAGE_NAMES=(); STAGE_STATUS=(); STAGE_TIME=(); STAGE_NOTE=()
FAILED=0
NSTAGE=0
T_START=$SECONDS

record() { STAGE_NAMES+=("$1"); STAGE_STATUS+=("$2"); STAGE_TIME+=("$3"); STAGE_NOTE+=("$4"); }

# stage NAME MODE NEEDS DIR COMMAND [NOTE]
#   MODE   q = quick and full, f = full only
#   NEEDS  exact | ngsolve | pari
#   DIR    working directory, relative to the repository root
#   NOTE   for f stages: the cost that keeps them out of the quick run
stage() {
    local name="$1" mode="$2" needs="$3" dir="$4" cmd="$5" note="${6:-}"
    NSTAGE=$((NSTAGE + 1))
    if [ -n "$ONLY" ] && ! printf '%s' "$name" | grep -Eq "$ONLY"; then return; fi
    if [ "$LIST" -eq 1 ]; then printf "%-6s %-8s %s\n" "$mode" "$needs" "$name"; return; fi
    if [ "$mode" = "f" ] && [ "$MODE" = "quick" ]; then
        record "$name" SKIP "-" "full mode only${note:+: $note}"
        echo "${yellow}--- ${name}: SKIP (full mode only${note:+: $note})${reset}"; echo
        return
    fi
    if [ "$needs" = "ngsolve" ] && [ "$HAVE_NGSOLVE" -ne 1 ]; then
        record "$name" SKIP "-" "NGSolve not installed (see the pre-flight note)"
        echo "${yellow}--- ${name}: SKIP (NGSolve not installed; see the pre-flight note above)${reset}"; echo
        return
    fi
    if [ "$needs" = "record" ] && [ ! -f "$ROOT/numerics/data/rerun_double_window_comparison.json" ]; then
        record "$name" SKIP "-" "rerun comparison record not committed (PENDING)"
        echo "${yellow}--- ${name}: SKIP (rerun comparison record not committed: PENDING)${reset}"; echo
        return
    fi
    if [ "$needs" = "pari" ] && [ "$HAVE_PARI" -ne 1 ]; then
        record "$name" SKIP "-" "PARI (cypari2) not installed (see the pre-flight note)"
        echo "${yellow}--- ${name}: SKIP (cypari2/PARI not installed; see the pre-flight note above)${reset}"; echo
        return
    fi
    echo "${bold}==> ${name}${reset}"
    local snap="$LOGDIR/snapshot.$NSTAGE" log="$LOGDIR/stage-$NSTAGE.log" rc t0=$SECONDS dt
    if [ "$GUARD" -eq 1 ]; then "$PYTHON" "$ROOT/code/data_guard.py" snapshot "$snap" || true; fi
    ( cd "$ROOT/$dir" && eval "$cmd" ) 2>&1 | tee "$log"
    rc=${PIPESTATUS[0]}
    dt=$((SECONDS - t0))
    if [ "$GUARD" -eq 1 ]; then
        if ! "$PYTHON" "$ROOT/code/data_guard.py" verify "$snap"; then
            rc=97
            echo "${red}the stage rewrote committed files with different content (restored)${reset}"
        fi
        rm -rf "$snap"
    fi
    if [ "$rc" -eq 0 ]; then
        record "$name" PASS "$dt" ""
        echo "${green}--- ${name}: PASS ($(fmt_time $dt))${reset}"
    else
        FAILED=1
        record "$name" FAIL "$dt" "exit $rc"
        echo "${red}--- ${name}: FAIL (exit $rc, $(fmt_time $dt); output in $log)${reset}"
    fi
    echo
}

# --------------------------------------------------------------------------
# Stages
# --------------------------------------------------------------------------
P='$PYTHON'      # expanded when the stage runs, in the stage's directory

# --- the original verification harness (code/): arithmetic claims of the manuscript
stage "code 1 enumerator self-test"      q exact code "$P orbifold_enum.py"
stage "code 2 displayed identities"      q exact code "$P verify_identities.py"
stage "code 3 degeneracy enumeration"    q exact code "$P enumerate_degeneracies.py"
stage "code 4 LaTeX table generation"    q exact code "$P make_table.py"
stage "code 5 three-way cross-check"     q exact code "$P cross_check.py"
stage "code 6 claim-ledger coverage"     q exact code "$P coverage_report.py"

# --- review ledger, definitions, conventions, manifest
stage "review DEFECTS.md is current"     q exact .    "$P review/build_defects.py"
stage "review defects-check"             q exact .    "$P review/defects-check.py"
stage "theory definitions-check"         q exact .    "$P theory/definitions-check.py"
stage "theory conventions-check"         q exact .    "$P theory/conventions_check.py"
stage "admin DATA-MANIFEST is current"   q exact .    "$P admin/build_data_manifest.py --check"

# --- theory/audibility
stage "audibility orlando_check"         q exact theory/audibility "$P orlando_check.py"
stage "audibility linear_system"         q exact theory/audibility "$P linear_system.py"
stage "audibility verify_elimination"    q exact theory/audibility "$P verify_elimination.py"
# the sharpness search records its wall-clock time in its JSON: run it in a scratch copy and compare the rest
SHARP='S="$LOGDIR/scratch-sharp-@@"; rm -rf "$S"; cp -R . "$S"; (cd "$S" && $PYTHON sharpness_search.py @@ > /dev/null) && $PYTHON "$ROOT/code/json_equal.py" "$S/sharpness_n5_N@@.json" sharpness_n5_N@@.json --ignore wall_seconds'
stage "audibility sharpness N=60"        q exact theory/audibility "${SHARP//@@/60}"
stage "audibility sharpness N=120"       f exact theory/audibility "${SHARP//@@/120}" "about 22 min"

# --- theory/cone-coefficients, signatures, locality
stage "cone-coefficients verify"         q exact theory/cone-coefficients "$P verify_cone_coefficients.py"
stage "signatures heat_structure"        q exact theory/signatures "$P heat_structure.py"
stage "signatures cone_count"            q exact theory/signatures "$P cone_count.py"
stage "signatures area_classes"          q exact theory/signatures "$P area_classes.py"
stage "signatures genus"                 q exact theory/signatures "$P genus.py"
stage "locality check_locality"          q exact theory/locality "$P check_locality.py"

# --- theory/stability, threshold, curvature, divergence
stage "stability front_end"              q exact theory/stability "$P front_end.py"
stage "stability lipschitz_e"            q exact theory/stability "$P lipschitz_e.py"
stage "stability roots_holder"           q exact theory/stability "$P roots_holder.py"
stage "stability blind pipeline"         q exact theory/stability/blind "$P blind_pipeline.py"
stage "stability threshold"              f exact theory/stability "$P threshold.py" "30-60 min counterexample search"
stage "threshold first overlap"          q exact theory/threshold "$P threshold.py"
stage "curvature curvature_checks"       q exact theory/curvature "$P curvature_checks.py"
stage "divergence divergence"            f exact theory/divergence "$P divergence.py" "about 10 min"

# --- theory/diophantine (from the committed 4800-sum enumeration; never re-enumerated here)
stage "diophantine committed-data check" q exact theory/diophantine "$P check_committed.py"
stage "diophantine variety_checks"       q exact theory/diophantine "$P variety_checks.py"
stage "diophantine growth_fits"          q exact theory/diophantine "$P growth_fits.py"
stage "diophantine exponent_fits"        q exact theory/diophantine "$P exponent_fits.py"
stage "diophantine families"             q exact theory/diophantine "$P families.py 4800 7"
stage "diophantine ranks (PARI)"         q pari  theory/diophantine '$PYTHON_PARI ranks.py'

# --- numerics (committed CSV/JSON/NPZ only; no NGSolve)
stage "numerics validate (committed)"    q exact numerics "$P validate_committed.py --quick"
stage "numerics moduli validate"         q exact numerics/moduli "$P validate_committed.py --quick"
stage "numerics S3 rerun record"         q record numerics "$P rerun_double_window.py --verify-record"
stage "numerics validate (full)"         f exact numerics "$P validate_committed.py" "heat traces and fits, a few minutes"
stage "numerics moduli validate (full)"  f exact numerics/moduli "$P validate_committed.py" "trace formula for 8 members, about 5 min"
stage "numerics S3 re-solve (NGSolve)"   f ngsolve numerics '$PYTHON_NUMERICS rerun_double_window.py --no-record "$LOGDIR/rerun"' "about an hour; needs NGSolve"

# --------------------------------------------------------------------------
# Summary
# --------------------------------------------------------------------------
[ "$LIST" -eq 1 ] && exit 0

echo "${bold}summary (mode: $MODE)${reset}"
NPASS=0; NFAIL=0; NSKIP=0
for i in $(seq 0 $(( ${#STAGE_NAMES[@]} - 1 ))); do
    [ "${#STAGE_NAMES[@]}" -gt 0 ] || break
    status="${STAGE_STATUS[$i]}"
    case "$status" in
        PASS) col="$green"; NPASS=$((NPASS + 1)); tm="$(fmt_time "${STAGE_TIME[$i]}")" ;;
        FAIL) col="$red";   NFAIL=$((NFAIL + 1)); tm="$(fmt_time "${STAGE_TIME[$i]}")" ;;
        *)    col="$yellow"; NSKIP=$((NSKIP + 1)); tm="    -" ;;
    esac
    printf "  %s%-5s%s %6s  %-40s %s\n" "$col" "$status" "$reset" "$tm" "${STAGE_NAMES[$i]}" "${STAGE_NOTE[$i]}"
done
echo
echo "total time $(fmt_time $((SECONDS - T_START)));  $NPASS passed, $NFAIL failed, $NSKIP skipped;  logs in $LOGDIR"

if [ "$FAILED" -ne 0 ]; then
    echo "${red}${bold}FAIL${reset} -- $NFAIL stage(s) failed. See the output above."
    exit 1
fi
if [ "$NPASS" -eq 0 ]; then
    echo "${red}${bold}FAIL${reset} -- no stage ran (check --only)."
    exit 1
fi
echo "${green}${bold}PASS${reset} -- no stage failed ($NSKIP skipped; each skip is listed above with its reason)."
exit 0
