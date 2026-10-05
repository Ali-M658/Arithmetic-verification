#!/bin/zsh
# Exhaustive search for a size-8 genus collision sharing 3 heat coefficients (proof.md section 6).
# Shape (3,5) is forced by Theorem 2.1. For every 5-element side V (positive integers, gcd 1,
# v5 <= NMAX) the 3-element side U is the root set of an explicit cubic; search_T3.c filters by the
# rational-root theorem with certified floating-point bounds (undecided cases are candidates);
# search_T3_verify.py verifies every candidate exactly (sympy factorisation). Control: search_T3_control.py.
# Checkpointed in blocks of v5; progress appended to data/T3_search_log.txt.
# Usage: ./search_T3.sh FIRST LAST STEP NMAX     (the logged run: ./search_T3.sh 1 216 5 220, i.e. v5 = 1..220)
cd "$(dirname "$0")"
PY=/opt/homebrew/Caskroom/miniforge/base/bin/python3
clang -O2 -o /tmp/search_T3_$$ search_T3.c -lm || exit 1
for s in $(seq $1 $3 $2); do
  e=$((s+$3-1))
  /tmp/search_T3_$$ $4 $s $e > /tmp/search_T3_cand_$$.txt 2>> data/T3_search_log.txt
  $PY search_T3_verify.py < /tmp/search_T3_cand_$$.txt >> data/T3_search_log.txt || exit 1
done
rm -f /tmp/search_T3_$$ /tmp/search_T3_cand_$$.txt
