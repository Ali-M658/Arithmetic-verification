"""The a-posteriori test (eigen paper, Theorem 7.1) on the double-window recomputation of the triangle
spectra, and what one missing or one duplicated eigenvalue does to it.

    .venv/bin/python theory/eigen/practice_double_window.py          (a few minutes; no solver runs)

Part 1.  The spectra of O(2,8,8) and O(3,3,12) recomputed with the double-window solver
(numerics/data/double_window/eigenvalues_<pqr>_<bc>.csv, written by numerics/rerun_double_window.py)
replace the committed single-window spectra in the test of practice.py, with the same inputs: the
systole lower bound and the diameter bound 2 diam P of data/instances.csv, M = 12, the complete range
lambda <= 16000, and eps_j = (committed error estimate) + |recomputed - committed| for each index.
The least N of criteria (C1) and (C2) is compared with data/practice.csv (diameter input B1, eps,
full data).  Asserted: the recomputation has the same number of eigenvalues below 16000 and the same
counts N_C1, N_C2.

Part 2.  For each triangle orbifold and j in J, the committed list with lambda~_j deleted, and with
lambda~_j duplicated, is run through the same scan (all t of practice.TGRID, every N with lambda~_N
available).  Recorded: the least N at which (C1) holds for some signature, and which signature.
Nothing is asserted about the outcome; the counts are written to data/practice_missing.csv and printed.

Writes data/practice_double_window.csv and data/practice_missing.csv.
"""
import csv
import math
import os

import numpy as np

import practice as P
from eigen_common import check

J = (1, 2, 3, 5, 8, 12)
DW = os.path.join(P.ROOT, "numerics", "data", "double_window")


def rerun_spectrum(pqr, committed):
    name = "-".join(map(str, pqr))
    rows = []
    for bc in ("N", "D"):
        ref = list(csv.DictReader(open(os.path.join(P.ROOT, f"numerics/data/eigenvalues_{name}_{bc}.csv"))))
        new = list(csv.DictReader(open(os.path.join(DW, f"eigenvalues_{name}_{bc}.csv"))))
        for r, q in zip(ref, new):
            check(int(r["index"]) == int(q["index"]), "index alignment")
            lr, ln = float(r["lambda"]), float(q["lambda"])
            rows.append((ln, float(r["err_estimate"]) + abs(ln - lr), bc))
    rows.sort(key=lambda x: (x[0], x[2]))
    lam = np.array([x[0] for x in rows])
    keep = lam <= P.LAM_COMPLETE_TRIANGLE
    check(int(keep.sum()) == len(committed["lam"]), f"{pqr}: same number of eigenvalues below 16000")
    return dict(lam=lam[keep], eps=np.array([x[1] for x in rows])[keep], epsc=np.array([x[1] for x in rows])[keep],
                lam_complete=P.LAM_COMPLETE_TRIANGLE, n_total=len(rows), basis="double-window recomputation")


def first_C1(case, G):
    """Least N (over the t grid) at which (C1) holds for some signature, and that signature; no assertion
    on which signature it is."""
    best = None
    for t in P.TGRID:
        Gv = case.Gs(G, t)
        lh = float(P.logH(case.ell, case.Delta, case.A, t))
        Ht = math.exp(min(lh, 700.0))
        if Ht > 10 * (case.Nc + float(np.max(np.abs(Gv)))):
            continue
        tb = P.TailBound(case.ell, case.Delta, case.A, case.beta, t)
        Ns = np.arange(1, case.Nc)
        mu = case.lam[Ns] - case.eps[Ns]
        E = Ht + np.exp(np.minimum(tb.log_tail(mu), 700.0)) + t * case.cumeps[Ns]
        part = np.cumsum(np.exp(-case.lam * t))
        ps = np.abs(part[Ns - 1][:, None] - Gv[None, :]) <= E[:, None]
        c1 = ps.sum(axis=1) == 1
        if c1.any():
            k = int(np.argmax(c1))
            cand = (int(Ns[k]), case.S[int(np.argmax(ps[k]))], float(t))
            if best is None or cand[0] < best[0]:
                best = cand
    return best


def main():
    G = P.Gfun()
    inst = {r["orbifold"]: r for r in csv.DictReader(open(os.path.join(P.DATA, "instances.csv")))}
    ref = {(r["orbifold"], r["M"]): r for r in csv.DictReader(open(os.path.join(P.DATA, "practice.csv")))
           if r["diameter_input"] == "B1" and r["eps_j"] == "eps" and r["data"] == "full"}
    out, miss = [], []
    for name, pqr in (("O(2,8,8)", (2, 8, 8)), ("O(3,3,12)", (3, 3, 12))):
        sig = (0, pqr)
        I = inst[name]
        ell, Delta = float(I["systole_lower_bound"]), float(I["diam_upper_B1_2diamP"])
        com = P.triangle_spectrum(pqr)
        new = rerun_spectrum(pqr, com)
        dev = float(np.max(np.abs(new["lam"] - com["lam"]) / np.maximum(com["lam"], 1.0)))
        c = P.Case(name, sig, None, ell, 12, new, Delta, "B1", "double_window", "eps", do_obs=False)
        o = c.run(G)
        r0 = ref[(name, "12")]
        row = [name, len(new["lam"]), f"{dev:.2e}", o["C1"]["N"], f"{o['C1']['t']:.4g}", o["C2"]["N"], f"{o['C2']['t']:.4g}",
               r0["N_C1"], r0["N_C2"]]
        print("double-window:", " | ".join(map(str, row)), flush=True)
        check(str(o["C1"]["N"]) == r0["N_C1"] and str(o["C2"]["N"]) == r0["N_C2"],
              f"{name}: the test gives the same counts on the recomputed spectra")
        out.append(row)
        for j in J:
            for kind in ("deleted", "duplicated"):
                lam = list(com["lam"]); eps = list(com["eps"])
                if kind == "deleted":
                    del lam[j]; del eps[j]
                else:
                    lam.insert(j, lam[j]); eps.insert(j, eps[j])
                spec = dict(lam=np.array(lam), eps=np.array(eps), lam_complete=com["lam_complete"], n_total=len(lam), basis=kind)
                cm = P.Case(name, sig, None, ell, 12, spec, Delta, "B1", kind, "eps", do_obs=False)
                b = first_C1(cm, G)
                wrong = b is not None and b[1] != sig
                miss.append([name, j, kind, b[0] if b else "", str(b[1]) if b else "", f"{b[2]:.4g}" if b else "",
                             "wrong" if wrong else ("true" if b else "none")])
                print("  ", " | ".join(map(str, miss[-1])), flush=True)
    P.write(os.path.join(P.DATA, "practice_double_window.csv"),
            ["orbifold", "n_below_16000", "max_rel_dev_from_committed", "N_C1", "t_C1", "N_C2", "t_C2",
             "N_C1_committed", "N_C2_committed"], out)
    P.write(os.path.join(P.DATA, "practice_missing.csv"),
            ["orbifold", "j", "change", "least_N_C1", "signature_concluded", "t", "outcome"], miss)
    nw = sum(1 for m in miss if m[-1] == "wrong")
    print(f"one eigenvalue deleted or duplicated: (C1) concludes a wrong signature in {nw} of {len(miss)} cases")
    print("wrote data/practice_double_window.csv and data/practice_missing.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
