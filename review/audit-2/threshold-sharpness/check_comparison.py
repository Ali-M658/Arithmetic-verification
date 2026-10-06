"""Comparison phase: theory/revision/collision_witnesses.csv vs this group's blind search."""
import csv
from fractions import Fraction as F
rows = {}
for line in open("collisions_18_4800.txt"):
    a = line.split(); rows[int(a[0])] = (int(a[1]), int(a[2]), a[3:])
has = {S: rows[S][1] == 1 for S in rows}
mine = [S for S in range(18, 4801) if has[S] and not any(has[d] for d in range(18, S) if S % d == 0)]
theirs = []
same_pair = 0
for r in csv.DictReader(open("../../../theory/revision/collision_witnesses.csv")):
    S = int(r["S"]); t1 = (int(r["p1"]), int(r["q1"]), int(r["r1"])); t2 = (int(r["p2"]), int(r["q2"]), int(r["r2"]))
    Rv = F(int(r["R_num"]), int(r["R_den"]))
    for t in (t1, t2):
        assert sum(t) == S and 2 <= t[0] <= t[1] <= t[2] and sum(F(1, x) for x in t) == Rv < 1
    assert t1 != t2
    theirs.append(S)
    mp = rows[S][2]
    if {mp[0], mp[1]} == {",".join(map(str, t1)), ",".join(map(str, t2))}:
        same_pair += 1
assert len(theirs) == len(set(theirs)) == 783
assert theirs == mine, (set(theirs) ^ set(mine))
print("collision_witnesses.csv: 783 rows, all re-verified exactly; S set identical to the blind 783 primitive sums")
print("rows whose pair equals the first pair found by the blind C search:", same_pair, "of 783")
print("ALL CHECKS PASSED")
