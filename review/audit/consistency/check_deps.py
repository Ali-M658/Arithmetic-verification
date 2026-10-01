"""P8 part 3: dependency graph of the results in review/audit/STATEMENTS.md.
Writes deps.json and deps_table.txt; detects cycles (Tarjan SCC) on
  (a) all edges, (b) logical edges only.
Exits nonzero if the logical graph has a cycle not listed in EXPECTED_ACCEPTED, or if a
statement-visible logical cycle appears.

Edge kinds
  uses        logical input stated in the statement text (or its own 'Source/Input' line)
  proved_by   the source node is a forward reference whose proof is the target
  definition  only a definition / object / class is borrowed, no claim
  crosscheck  the statement compares with, reproduces or restates another result
  sharpness   reference used only to say a bound is sharp
  inferred    not cited, but the statement cannot hold without it (referee's reading)
  reported    named in the P8 brief as an input; NOT visible in the register (proof text omitted)
"""
import json, os, sys

E = []  # (src, dst, kind, evidence)
def e(src, dst, kind, ev):
    E.append((src, dst, kind, ev))

# ---------------- paper-core
e("PC.thmA", "PC.thm:separation", "uses", "PC.15 'hence Theorem thmA'")
e("PC.thmA", "PC.eq:s1inv", "uses", "first two coefficients -> (R,S_1)")
e("PC.thmA", "PC.thmB", "sharpness", "PC.1 'The bound 17 is sharp ... (Theorem thmB)'")
e("PC.thmB", "PC.thm:separation", "uses", "PC.14 second sentence; PC.15 S=18 computation")
e("PC.thmB", "PC.eq:s1inv", "uses", "identical first two coefficients <=> equal (R,S_1)")
e("PC.thmC", "PC.prop:recovery", "uses", "PC.9b 'equivalently ... first three heat coefficients is injective'")
e("PC.thmC", "PC.eq:a2red", "uses", "third coefficient delivers P_3")
e("PC.thmC", "PC.thmB", "uses", "K(F)=3 for the collision pair")
e("PC.thmC", "DF.prop:rigidity", "inferred", "'up to isometry, equivalently ... cone orders' needs rigidity; not cited in PC")
e("PC.corD", "PC.eq:s1inv", "uses", "first two factor through (R,S_1)")
e("PC.corD", "PC.eq:a2red", "uses", "first three detect sum m_i^3")
e("PC.corD", "PC.thmB", "uses", "first failure at 18")
e("PC.corD", "PC.thmA", "uses", "range S<=17 sharp")
e("PC.eq:a0conv", "EXT.DGGW", "uses", "PC.2 'We use the orbifold heat-trace expansion of DGGW'")
e("PC.eq:a0conv", "PC.cor:conevals", "uses", "cone sum")
e("PC.cor:conevals", "PC.prop:csc", "uses", "def:cone in csc^2")
e("PC.prop:csc", "PC.lem:cot", "inferred", "csc^2 = 1 + cot^2")
e("PC.eq:s1inv", "PC.eq:area", "uses", "PC.7 (i)")
e("PC.eq:s1inv", "PC.eq:a0conv", "uses", "PC.7 (ii)")
e("PC.eq:b1", "EXT.Schueth", "uses", "PC.8 footnote")
e("PC.eq:b1", "EXT.DGGW", "uses", "PC.8 footnote (DGGW 5.6)")
e("PC.eq:b1", "EXT.Ucar", "crosscheck", "PC.8 footnote 'consistent with Ucar'")
e("PC.eq:a2red", "PC.eq:b1", "uses", "summing eq:b1 at K=-1")
e("PC.prop:recovery", "PC.eq:s1inv", "uses", "R, S_1 from c_1, c_2")
e("PC.prop:recovery", "PC.eq:a2red", "uses", "P_3 from c_3")
e("PC.jacobian", "PC.prop:recovery", "crosscheck", "PC.10 infinitesimal counterpart")
e("PC.lem:bound", "PC.lem:chamber", "uses", "PC.12")
e("PC.prop:min", "PC.eq:a0conv", "uses", "PC.13")
e("PC.prop:min", "PC.lem:chamber", "inferred", "monotonicity of R in a stratum")
e("PC.thm:separation", "PC.lem:chamber", "uses", "PC.14")
e("PC.thm:separation", "PC.lem:bound", "uses", "PC.15")
e("PC.remA0", "PC.prop:min", "uses", "PC.16")
e("PC.remA0", "PC.prop:cs", "uses", "PC.16")
e("PC.prop:scaling", "PC.degdef", "definition", "PC.17")
e("PC.degdef", "PC.lem:chamber", "uses", "PC.17 'by lem:chamber the two triples share the sum'")
e("PC.thm:density-lower", "PC.prop:scaling", "uses", "PC.17b")
e("PC.thm:density-lower", "PC.thmB", "uses", "base pair")
e("PC.S36", "PC.prop:scaling", "crosscheck", "PC.18")
e("PC.conj:density", "PC.thm:density-lower", "crosscheck", "PC.19")
e("PC.conj:density", "PC.thmC", "uses", "PC.19 last paragraph: 'Theorem thmC gives K(F)<=3'")
e("PC.rem:ncone", "PC.thmC", "crosscheck", "PC.20")
e("PC.tab:enum", "PC.thm:separation", "crosscheck", "PC.21 'independent cross-check'")
# ---------------- definitions
e("DF.def:heatcoef", "EXT.DGGW", "uses", "DF.1 cites donnelly1976, dggw2008")
e("DF.def:heatcoef", "EXT.Donnelly", "uses", "DF.1")
e("DF.def:K", "DF.def:heatcoef", "definition", "H_k")
e("DF.def:K", "DF.def:signature", "definition", "sigma")
e("DF.eq:Kcompare", "DF.def:K", "uses", "DF.2")
e("DF.prop:rigidity", "DF.eq:moduli", "inferred", "rigidity = zero-dimensional moduli for n=3 (proof not in register)")
e("DF.eq:moduli", "EXT.Troyanov", "uses", "DF.4")
e("DF.eq:moduli", "EXT.Thurston", "uses", "DF.4")
e("DF.thm:locality", "LO.T1", "proved_by", "LO.1 'This proves thm:locality'")
e("DF.prop:Kinf", "DF.thm:locality", "uses", "DF.5 'Conditional on thm:locality'")
e("DF.prop:Kinf", "DF.eq:moduli", "uses", "n>=4 case")
e("DF.thm:Crestated", "PC.thmC", "uses", "DF.6 title")
e("DF.thm:Crestated", "DF.prop:rigidity", "uses", "K_iso = K_mult")
e("DF.thm:Crestated", "PC.prop:recovery", "reported", "P8 brief; implied through thmC")
e("DF.thm:Crestated", "PC.thmB", "uses", "example of value 3")
e("DF.rem:nconerestated", "PC.prop:recovery", "uses", "DF.7(a)")
e("DF.rem:nconerestated", "DF.prop:Kinf", "uses", "DF.7(b)")
e("DF.rem:nconerestated", "DF.eq:moduli", "uses", "DF.7(b)")
e("DF.rem:nconerestated", "DF.prop:rigidity", "uses", "DF.7(b)")
e("DF.rem:nconerestated", "PC.rem:ncone", "crosscheck", "restates/corrects PC.20")
# ---------------- audibility
e("AU.heat", "EXT.Ucar", "uses", "AU.0")
e("AU.heat", "EXT.Schueth", "uses", "AU.0 (l<=2)")
e("AU.ThmA", "AU.heat", "uses", "I_n triangular")
e("AU.ThmA", "EXT.HoltzTyaglov", "uses", "Orlando")
e("AU.ThmA", "AU.Lemma1", "inferred", "parity lemma (proof not in register)")
e("AU.ThmA", "AU.ThmB", "inferred", "hypothesis e_n Delta_{n-1} != 0 is det M != 0 of Theorem B")
e("AU.ThmB", "AU.heat", "uses", "coefficients are polynomials in I_n")
e("AU.ThmB", "EXT.HoltzTyaglov", "uses", "Delta_{n-1}")
e("AU.ThmC", "AU.heat", "uses", "I_{n-1}")
e("AU.witness", "AU.ThmC", "crosscheck", "AU.4")
e("AU.Rem2", "AU.ThmA", "crosscheck", "AU.3")
e("AU.Rem3", "AU.ThmA", "uses", "AU.3 padding")
# ---------------- signatures
e("SG.H", "EXT.Ucar", "uses", "SG.0 (H1),(H2)")
e("SG.H", "EXT.DGGW", "uses", "SG.0 (H1)")
e("SG.H", "DF.def:heatcoef", "definition", "SG.0 (H3)")
e("SG.L1", "SG.H", "uses", "SG.1")
e("SG.L2", "SG.L1", "uses", "SG.2")
e("SG.L3", "SG.H", "uses", "SG.3")
e("SG.L4", "SG.L2", "uses", "SG.4 'It follows for all L from Lemma 2'")
e("SG.L4", "SG.L3", "uses", "padding")
e("SG.ThmS", "SG.L4", "uses", "SG.5")
e("SG.S1", "SG.ThmS", "uses", "SG.6")
e("SG.S2", "SG.S1", "uses", "SG.7")
e("SG.S2", "DF.def:K", "definition", "SG.7")
e("SG.T1", "SG.S1", "uses", "T1(3) is S1 at g=g'=0")
e("SG.T1", "SG.S2", "uses", "T1(2)")
e("SG.T1", "AU.ThmA", "reported", "P8 brief: 'Theorem T1 using Theorem A'")
e("SG.ThmN", "SG.PropP", "uses", "Prouhet construction")
e("SG.ThmN", "SG.L4", "uses", "converse direction of Lemma 4")
e("SG.N1", "SG.ThmN", "uses", "lower bound")
e("SG.N1", "SG.S2", "uses", "upper bound")
e("SG.rem:sigK", "AU.ThmA", "crosscheck", "SG.13 'now proved independently (Theorem A)'")
e("SG.rem:sigK", "DF.rem:nconerestated", "crosscheck", "SG.13")
e("SG.rem:sigK", "DF.prop:Kinf", "uses", "SG.13")
e("SG.rem:sigK", "DF.eq:Kcompare", "uses", "SG.13")
e("SG.ex:siggenus", "SG.L4", "crosscheck", "exact computation")
# ---------------- locality
e("LO.T1", "EXT.Ucar", "uses", "LO.1 constants (Ucar Thm 4.20 at kappa=-1)")
e("LO.T1", "EXT.DGGW", "uses", "LO.1 (4.9) and strata")
e("LO.T1", "LO.T3.1", "reported", "P8 brief: 'Proof C' of Theorem 1 via Theorem 3.1 (alternative proof)")
e("LO.P2.1", "EXT.Thurston", "uses", "LO.2 Cor 13.3.7")
e("LO.P2.2", "LO.P2.1", "uses", "LO.4")
e("LO.C2.3", "LO.P2.2", "uses", "LO.5")
e("LO.C2.3", "LO.T1", "uses", "same signature -> same coefficients")
e("LO.C2.3", "DF.def:K", "definition", "LO.5")
e("LO.C2.3", "DF.rem:nconerestated", "definition", "LO.5 class P_n")
e("LO.C2.3", "DF.prop:rigidity", "inferred", "triangle case K_iso = K_mult")
e("LO.C2.3", "DF.prop:Kinf", "crosscheck", "same content as prop:Kinf (unconditional form)")
e("LO.T3.1", "EXT.DS", "uses", "LO.6 Selberg trace formula")
e("LO.T3.1", "LO.L3.2", "uses", "admissibility")
e("LO.T3.1", "LO.L3.3", "uses", "absolute convergence of H")
e("LO.L3.2", "EXT.DS", "uses", "LO.7 '[DS] (1) holds for h_R'")
e("LO.L3.2", "LO.T1", "reported", "P8 brief: Lemma 3.2 uses a Weyl bound taken from Theorem 1")
e("LO.T3.4", "LO.T3.1", "uses", "exact cancellation")
e("LO.T3.4", "LO.L3.3", "uses", "counting")
e("LO.T3.5", "LO.T3.1", "uses", "")
e("LO.claim", "LO.T3.5", "uses", "LO.10")
e("LO.claim", "LO.T3.4", "uses", "LO.10")
# ---------------- stability
e("ST.setup", "EXT.Ucar", "uses", "ST.0")
e("ST.setup", "AU.ThmB", "uses", "linear solve")
e("ST.S1", "ST.setup", "uses", "")
e("ST.table", "ST.S1", "uses", "L^{-1}")
e("ST.S2.2", "AU.ThmB", "definition", "matrix M only")
e("ST.S2.1", "ST.S2.2", "uses", "det M = det B / det S")
e("ST.S2.1", "AU.ThmB", "definition", "ST.3 'replaces c_n ... in Theorem B'")
e("ST.ThmS2", "ST.S2.2", "uses", "kappa bound via B, S")
e("ST.ThmS2", "ST.S2.1", "uses", "")
e("ST.LemS3", "EXT.Ostrowski", "crosscheck", "ST.6 global vs local")
e("ST.ThmS3", "ST.table", "uses", "l = (2,14,498,4062,...)")
e("ST.ThmS3", "ST.ThmS2", "uses", "")
e("ST.ThmS3", "ST.LemS3", "uses", "")
e("ST.S3.2", "AU.ThmB", "uses", "ST.9(ii)")
e("ST.S4", "ST.ThmS3", "uses", "")
e("ST.S5", "ST.S2.1", "uses", "ST.12 'G exact (Lemma S2.1)'")
e("ST.S5", "ST.table", "uses", "|L^{-1}|")
e("ST.results", "ST.S4", "uses", "delta_thm"); e("ST.results", "ST.S5", "uses", "delta_cert")
# ---------------- threshold
e("TH.0", "PC.lem:chamber", "uses", "TH.0"); e("TH.0", "PC.lem:bound", "uses", "TH.0")
e("TH.L1", "TH.0", "uses", ""); e("TH.L2", "TH.L1", "uses", "")
e("TH.L2", "PC.thm:separation", "crosscheck", "'the chain in the proof of thm:separation'")
e("TH.T1", "TH.L1", "uses", "")
e("TH.C2", "TH.T1", "uses", ""); e("TH.C2", "TH.L2", "uses", "")
e("TH.C2", "PC.thmB", "crosscheck", "same content as thmA/thmB")
e("TH.table", "DI.counts", "crosscheck", "'reproduces all 2,977 collision fibres of groups.csv'")
e("TH.P3", "TH.T1", "uses", "")
# ---------------- curvature
e("CU.flat", "EXT.Kokotov", "uses", "CU.1"); e("CU.flat", "EXT.DGGW", "uses", "CU.1")
e("CU.flat", "DV.L1", "uses", "CU.1 positivity for all l")
e("CU.prop", "CU.flat", "uses", "Part 1, 4"); e("CU.prop", "CU.L2", "uses", "Part 2")
e("CU.prop", "EXT.DGGW", "crosscheck", "Strength: DGGW 5.15, 5.22")
e("CU.prop", "EXT.Ucar", "crosscheck", "Cor 4.21(iv)")
e("CU.prop", "AU.ThmA", "uses", "Part 3 'is Theorem A'")
e("CU.prop", "AU.ThmC", "uses", "Part 3 sharpness")
# ---------------- divergence
e("DV.L1", "EXT.Ucar", "uses", "DV.0"); e("DV.T2", "DV.L1", "uses", "")
e("DV.T3", "DV.T2", "uses", ""); e("DV.C4", "DV.T3", "uses", "")
e("DV.C4", "EXT.Ucar", "crosscheck", "Cor 4.21(iv)"); e("DV.Borel", "DV.T3", "uses", "")
# ---------------- diophantine
e("DI.P1", "PC.degdef", "definition", "degeneracy"); e("DI.pencil", "EXT.Beauville", "uses", "")
e("DI.pencil", "EXT.BGN", "crosscheck", ""); e("DI.pencil", "EXT.Shioda", "uses", "MW rank 0 (zbMATH report only)")
e("DI.recip", "DI.pencil", "uses", ""); e("DI.T3", "DI.pencil", "uses", "positive-rank fibres")
e("DI.T3", "DI.P1", "uses", "")
e("DI.isolation", "EXT.PARI", "uses", "ellrank, elltors")
e("DI.isolation", "PC.thmB", "reported", "P8 brief: 'the isolation theorem using Theorem B' (only the base pair itself is borrowed)")
e("DI.T4", "DI.countconv", "uses", "(*)"); e("DI.T4", "DI.recip", "uses", "dual family")
e("DI.T5", "DI.countconv", "uses", "")
e("DI.countconv", "PC.conj:density", "definition", "'the paper's convention'")
e("DI.counts", "DI.P1", "uses", "")

LOGICAL = {"uses", "proved_by", "inferred", "reported"}

def nodes_of(edges):
    s = set()
    for a, b_, *_ in edges:
        s.add(a); s.add(b_)
    return sorted(s)

def scc(nodes, edges):
    adj = {n: [] for n in nodes}
    for a, b_, *_ in edges:
        adj[a].append(b_)
    index, low, on, st, res, idx = {}, {}, set(), [], [], [0]
    sys.setrecursionlimit(10000)
    def strong(v):
        index[v] = low[v] = idx[0]; idx[0] += 1; st.append(v); on.add(v)
        for w in adj[v]:
            if w not in index:
                strong(w); low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = st.pop(); on.discard(w); comp.append(w)
                if w == v: break
            if len(comp) > 1 or v in adj[v]:
                res.append(sorted(comp))
    for v in nodes:
        if v not in index:
            strong(v)
    return res

N = nodes_of(E)
all_cycles = scc(N, E)
logical = [x for x in E if x[2] in LOGICAL]
log_cycles = scc(N, logical)
visible = [x for x in E if x[2] in {"uses", "proved_by", "inferred"}]
vis_cycles = scc(N, visible)
# with 'Proof C' treated as an alternative proof (cross-check), as it must be:
no_proofC = [x for x in logical if not (x[0] == "LO.T1" and x[1] == "LO.T3.1")]
fixed_cycles = scc(N, no_proofC)

EXPECTED_ACCEPTED = [sorted(["LO.T1", "LO.T3.1", "LO.L3.2"])]
here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "deps.json"), "w") as f:
    json.dump({"edge_kinds": {
        "uses": "logical input stated in the statement", "proved_by": "forward reference proved by target",
        "definition": "object/definition only", "crosscheck": "comparison/restatement only",
        "sharpness": "cited only for sharpness", "inferred": "uncited but necessary (referee reading)",
        "reported": "named in the P8 brief, not visible in the register"},
        "nodes": N,
        "edges": [{"from": a, "to": b_, "kind": k, "evidence": ev} for a, b_, k, ev in E],
        "cycles_all_edges": all_cycles, "cycles_logical": log_cycles,
        "cycles_statement_visible_logical": vis_cycles,
        "cycles_logical_with_proofC_as_crosscheck": fixed_cycles}, f, indent=1)
lines = ["from | to | kind | evidence", "---|---|---|---"]
for a, b_, k, ev in sorted(E):
    lines.append(f"{a} | {b_} | {k} | {ev}")
lines += ["", f"cycles (all edges): {all_cycles}", f"cycles (logical edges): {log_cycles}",
          f"cycles (statement-visible logical edges): {vis_cycles}",
          f"cycles (logical, Proof C demoted to cross-check): {fixed_cycles}"]
with open(os.path.join(here, "deps_table.txt"), "w") as f:
    f.write("\n".join(lines) + "\n")
print("\n".join(lines[-4:]))
assert vis_cycles == [], "a cycle is visible in the statements themselves"
assert sorted(log_cycles) == EXPECTED_ACCEPTED, log_cycles
assert fixed_cycles == []
print(f"{len(N)} nodes, {len(E)} edges. DEPENDENCY CHECKS PASSED")
