# data/

| file | content | produced by |
|---|---|---|
| `witnesses.json`, `orbifold_pairs.md` | the 18 orbifold pairs of proof.md §5 | `witnesses.py` |
| `pencil_N130_200.json`, `pencil_log.txt` | pencil configurations (Theorem 3.1) | `pencil_search.py` |
| `T3_search_log.txt` | exhaustive search for a size-8 genus collision at L = 3 | `search_T3.sh` |
| `sym6_400.txt` | all 19,450 size-6 even symmetric ideal PTE solutions a1<=a2<=a3, b1<=b2<=b3 <= 400 (sum of squares and fourth powers equal) | `enum_sym6.c 400` |
| `sym8_140.txt` | all 43 disjoint size-8 even symmetric ideal PTE solutions with entries <= 140 | `enum_sym8.c 140` (filtered for disjointness, re-verified exactly) |
| `genus_search_L4_log.txt`, `genus_search_L5_log.txt` | logs of the witness searches at L = 4, 5 (minimum 16 and 20) | `genus_search.py 4`, `genus_search.py 5` |
| `pencil_m4_N220.json` | the 61 pencil configurations from 4-sets with entries <= 220 (re-verified by `pencil_search.py`) | one run of the `pencil_search.py` algorithm with N4 = 220 |
