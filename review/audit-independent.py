#!/usr/bin/env python3
"""Independent exact-arithmetic audit of every numerical claim in paper/main.tex."""
from fractions import Fraction as F
from collections import defaultdict
import math, re, sys

OK, BAD = [], []
def chk(cid, cond, detail=""):
    (OK if cond else BAD).append((cid, detail))
    print(f"{'PASS' if cond else 'FAIL'}  {cid}  {detail}")

def triads(S):
    """All 2<=p<=q<=r, p+q+r=S, hyperbolic (R<1)."""
    out = []
    for p in range(2, S // 3 + 1):
        for q in range(p, (S - p) // 2 + 1):
            r = S - p - q
            if r < q: continue
            R = F(1, p) + F(1, q) + F(1, r)
            if R < 1: out.append((p, q, r, R))
    return out

# ---- C1..C3 cone values -------------------------------------------------
cone = lambda m: F(m*m - 1, 12*m)
chk("C-cone2", cone(2) == F(1, 8), f"cone(2)={cone(2)}")
chk("C-cone3", cone(3) == F(2, 9), f"cone(3)={cone(3)}")
chk("C-cone5", cone(5) == F(2, 5), f"cone(5)={cone(5)}")

# ---- cotangent / cosecant sums (numeric, high precision) ----------------
for m in range(2, 40):
    c = sum(1/math.tan(j*math.pi/m)**2 for j in range(1, m))
    chk(f"C-cot(m={m})", abs(c - (m-1)*(m-2)/3) < 1e-6, "") if m in (2,3,5,12,39) else None
    s = sum(1/math.sin(j*math.pi/m)**2 for j in range(1, m))
    chk(f"C-csc(m={m})", abs(s - (m*m-1)/3) < 1e-6, "") if m in (2,3,5,12,39) else None

# ---- reference triple (2,3,5) ------------------------------------------
conesum = cone(2)+cone(3)+cone(5)
R235 = F(1,2)+F(1,3)+F(1,5)
chi6 = (R235 - 1)/6
a0_235 = conesum + chi6
chk("C-235-conesum", conesum == F(269,360), f"{conesum}")
chk("C-235-chi6", chi6 == F(1,180), f"{chi6}")
chk("C-235-a0", a0_235 == F(271,360), f"{a0_235}")
chk("C-235-a0formula", F(10 + R235 - 2, 1)/12 == F(271,360), f"(S1+R-2)/12={(10+R235-2)/12}")
chk("C-s1inv", 12*a0_235 + 2 - R235 == 10, f"S1={12*a0_235+2-R235}")
wrong = 12*(a0_235 - 2) + R235
chk("C-bugfix-neg", wrong < 0, f"wrong formula gives {wrong}")

# ---- a2red coefficient algebra -----------------------------------------
chk("C-11/360", F(1,360)+F(1,36) == F(11,360), f"{F(1,360)+F(1,36)}")

# ---- Cauchy-Schwarz S1*R >= 9 ------------------------------------------
viol = [(p,q,r) for S in range(10,200) for (p,q,r,R) in triads(S) if S*R < 9]
chk("C-cs", not viol, f"violations={len(viol)}")

# ---- Newton-Vieta round trip -------------------------------------------
bad_rt = []
for S in range(10, 120):
    for (p,q,r,R) in triads(S):
        e1, P3 = S, p**3+q**3+r**3
        e3 = F(P3 - e1**3, 1) / (3 - 3*e1*R)
        e2 = R*e3
        if (e1, e2, e3) != (p+q+r, F(p*q+q*r+r*p), F(p*q*r)): bad_rt.append((p,q,r))
chk("C-roundtrip", not bad_rt, f"failures={len(bad_rt)}")

# ---- Jacobian determinant ----------------------------------------------
def jac_num(p,q,r):
    return F(-3*(p-q)*(p-r)*(q-r)*(p+q)*(p+r)*(q+r), (p*q*r)**2)
def jac_direct(p,q,r):
    # rows: grad S1, grad R, grad P3
    M = [[1,1,1],
         [F(-1,p*p), F(-1,q*q), F(-1,r*r)],
         [3*p*p, 3*q*q, 3*r*r]]
    d = (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
        -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
        +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))
    return d
bad_j = [(p,q,r) for p in range(2,9) for q in range(p,10) for r in range(q,12)
         if jac_num(p,q,r) != jac_direct(p,q,r)]
chk("C-jacobian", not bad_j, f"mismatches={len(bad_j)}")

# ---- S1 >= 10, unique minimum ------------------------------------------
chk("C-noS1le9", all(not triads(S) for S in range(3,10)), "no hyperbolic triads S<=9")
chk("C-S1eq10", [t[:3] for t in triads(10)] == [(3,3,4)], f"{[t[:3] for t in triads(10)]}")

# ---- stratum endpoints, tau, phi ---------------------------------------
tau = lambda p: F(2,p+1) - F(1,p)
chk("C-tau2", tau(2)==F(1,6), f"{tau(2)}"); chk("C-tau3", tau(3)==F(1,6), f"{tau(3)}")
chk("C-tau4", tau(4)==F(3,20), f"{tau(4)}")
chk("C-tau-form", all(tau(p)==F(p-1,p*(p+1)) for p in range(2,20)), "(p-1)/(p(p+1))")
phi = lambda p,S: F(4,S-p) - F(1,S-2*p-2)
for (p,S,v) in [(2,17,F(29,165)),(2,18,F(1,6)),(3,12,F(7,36)),(3,17,F(11,63)),(4,15,F(9,55))]:
    chk(f"C-phi({p},{S})", phi(p,S)==v, f"{phi(p,S)} vs {v}")
chk("C-phi2-17-gt", phi(2,17)>tau(2), "29/165 > 1/6")
chk("C-phi2-18-eq", phi(2,18)==tau(2), "equality at S=18")
chk("C-phi3-both-gt", phi(3,12)>tau(3) and phi(3,17)>tau(3), "")
chk("C-phi4-min", min(phi(4,15),phi(4,16),phi(4,17))==phi(4,15) and phi(4,15)>tau(4), f"min={min(phi(4,15),phi(4,16),phi(4,17))}")
# unimodality peak at S=3p+4
for p in (2,3,4):
    peak = max(range(2*p+3, 60), key=lambda S: phi(p,S))
    chk(f"C-unimodal(p={p})", peak == 3*p+4, f"argmax={peak}, 3p+4={3*p+4}")

def Rplus(S,p):  return F(2,p) + F(1,S-2*p)
def Rminus(S,p):
    ts = [t for t in triads(S) if t[0]==p]
    return min(t[3] for t in ts) if ts else None
for (S,p,v) in [(18,3,F(101,168)),(18,4,F(15,28)),(18,5,F(107,210))]:
    chk(f"C-Rminus({S},{p})", Rminus(S,p)==v, f"{Rminus(S,p)} vs {v}")
for (S,p,v) in [(18,4,F(3,5)),(18,5,F(21,40)),(18,6,F(1,2))]:
    chk(f"C-Rplus({S},{p})", Rplus(S,p)==v, f"{Rplus(S,p)} vs {v}")
chk("C-18-sep", Rminus(18,3)>Rplus(18,4) and Rminus(18,4)>Rplus(18,5) and Rminus(18,5)>Rplus(18,6), "")

# ---- interval separation S<=17, contact at 18 --------------------------
def collisions(S):
    m = defaultdict(list)
    for (p,q,r,R) in triads(S): m[R].append((p,q,r))
    return {R:v for R,v in m.items() if len(v)>1}
chk("C-thmA", all(not collisions(S) for S in range(10,18)), "no collisions S<=17")
c18 = collisions(18)
chk("C-thmB", list(c18.keys())==[F(3,4)] and sorted(c18[F(3,4)])==[(2,8,8),(3,3,12)], f"{c18}")
chk("C-R288", F(1,2)+F(1,8)+F(1,8)==F(3,4), "")
chk("C-R3312", F(1,3)+F(1,3)+F(1,12)==F(3,4), "")
chk("C-P3", 2**3+8**3+8**3==1032 and 3**3+3**3+12**3==1782, "1032 / 1782")

# ---- a0 minimum over all pillows is (3,3,4)=107/144 --------------------
a0 = lambda S,R: F(S,1)+R-2
best = min(((a0(S,R)/12,(p,q,r)) for S in range(10,400) for (p,q,r,R) in triads(S)), key=lambda x:x[0])
chk("C-a0min", best[0]==F(107,144) and best[1]==(3,3,4), f"{best}")

# ---- scaling law --------------------------------------------------------
bad_sc = []
for k in range(1,25):
    a,b = (2*k,8*k,8*k),(3*k,3*k,12*k)
    Ra = sum(F(1,x) for x in a); Rb = sum(F(1,x) for x in b)
    if not (sum(a)==sum(b)==18*k and Ra==Rb==F(3,4)/k and Ra<1): bad_sc.append(k)
chk("C-scaling", not bad_sc, f"failures={len(bad_sc)}")

# ---- S=36 classes -------------------------------------------------------
c36 = collisions(36)
chk("C-36-count", len(c36)==2, f"{len(c36)} classes: {dict(c36)}")
chk("C-36-primitive", F(3,10) in c36 and sorted(c36[F(3,10)])==[(6,15,15),(8,8,20)], f"{c36.get(F(3,10))}")
chk("C-36-scaled", F(3,8) in c36 and sorted(c36[F(3,8)])==[(4,16,16),(6,6,24)], f"{c36.get(F(3,8))}")

# ---- N(S), cumulative, vs Table 2 --------------------------------------
def N_pairs(S):   return sum(len(v)*(len(v)-1)//2 for v in collisions(S).values())
def N_classes(S): return len(collisions(S))
cum_p = cum_c = 0; curve = {}
for S in range(10, 601):
    cum_p += N_pairs(S); cum_c += N_classes(S)
    curve[S] = (cum_p, cum_c)
TABLE2 = {18:1, 100:92, 200:386, 300:840, 400:1496, 500:2210, 600:3067}
print("\n  S | paper | pairs | classes")
for S,v in TABLE2.items():
    p_,c_ = curve[S]
    print(f"{S:4d} | {v:5d} | {p_:5d} | {c_:5d}")
    chk(f"C-tab2-S{S}", v==p_ or v==c_, f"paper={v} pairs={p_} classes={c_}")

# ratios printed in table
print("\n  ratio check (paper vs pairs-count):")
for S,v in TABLE2.items():
    p_,_ = curve[S]
    print(f"  S={S}: paper N/S={v/S:.3f} N/S^2={v/S**2:.5f} | mine N/S={p_/S:.3f} N/S^2={p_/S**2:.5f}")

# power-law exponent 50..600
xs = [math.log(S) for S in range(50,601) if curve[S][0]>0]
ys = [math.log(curve[S][0]) for S in range(50,601) if curve[S][0]>0]
n=len(xs); mx=sum(xs)/n; my=sum(ys)/n
slope = sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs)
print(f"\n  power-law exponent (mine, pairs): {slope:.3f}   paper claims 2.03")
chk("C-exponent", abs(slope-2.03)<0.15, f"slope={slope:.3f}")

# lower bound
chk("C-lowerbound", all(curve[S][0] >= S//18 for S in range(18,601)), "N(S)>=floor(S/18)")
chk("C-33of3067", 600//18==33, f"floor(600/18)={600//18}")

# ---- Table 1 (tab:enum) row-by-row -------------------------------------
tex = open(sys.argv[1] if len(sys.argv)>1 else "paper/main.tex").read()
body = tex.split(r"\label{tab:enum}")[1].split(r"\end{longtable}")[0]
rows = re.findall(r"\$?\((\d+),(\d+),(\d+)\)\$?\}?\s*&\s*\\?t?e?x?t?b?f?\{?\$(\d+)/(\d+)\$", body)
print(f"\n  parsed {len(rows)} table rows")
expected = [(p,q,r,R) for S in range(10,19) for (p,q,r,R) in triads(S)]
chk("C-tab1-count", len(rows)==len(expected), f"parsed={len(rows)} expected={len(expected)}")
bad_rows=[]
for (p,q,r,nu,de) in rows:
    p,q,r,nu,de = int(p),int(q),int(r),int(nu),int(de)
    Rtrue = F(1,p)+F(1,q)+F(1,r)
    if Rtrue != F(nu,de): bad_rows.append(((p,q,r), f"{nu}/{de}", str(Rtrue)))
chk("C-tab1-values", not bad_rows, f"mismatches={bad_rows}")
parsed_set = {(int(a),int(b),int(c)) for a,b,c,_,_ in rows}
missing = [t[:3] for t in expected if t[:3] not in parsed_set]
chk("C-tab1-complete", not missing, f"missing={missing}")

print(f"\n===== {len(OK)} passed, {len(BAD)} FAILED =====")
for cid,d in BAD: print(f"  FAILED: {cid}  {d}")
