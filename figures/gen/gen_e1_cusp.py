"""E1 data (eigen paper, figure 1): the low spectrum of the triangle orbifolds O(2,3,m).

    SCRATCH_VENV/bin/python figures/gen/gen_e1_cusp.py        (needs NGSolve; about two minutes)

The interpreter must have the numerics environment of numerics/requirements.txt (NGSolve 6.2.2607,
installed in a scratch virtual environment). The eigenvalues are computed with the repository's
solver, imported unchanged: numerics/solve.py (assemble, eigenvalues_robust: doubly covered
shift-invert slicing) on the hyperbolic triangle of numerics/geometry.py. The spectrum of the
orbifold O(2,3,m) is the union of the Neumann and Dirichlet spectra of the triangle with angles
pi/2, pi/3, pi/m (numerics/REPORT.md section 1); the triangle is built as Triangle(m, 2, 3), so the
vertex of angle pi/m sits at the centre of the disc and the thin part near the cone point of order
m is a Euclidean sector there.

The orders run from 7 to 4096. Beyond that the sector is too thin for the mesher and the
slicing: at m = 8192 the fine level returned a spurious double eigenvalue, and at m = 16384 the
mesher failed; those orders are therefore not used.

Two mesh levels per m, (h, p) = (0.1, 8) and (0.07, 10) (hyperbolic mesh size, polynomial order);
the second is the one plotted, and their difference is recorded as the convergence check.

Machine safety: before each m the script reads `memory_pressure -Q` and waits (2-minute polls, at
most 30 minutes) while the system-wide free percentage is below 20%; one process, no parallel jobs.

Writes figures/data/e1_cusp_eigs.csv: one row per (m, level, boundary condition, index), and
figures/data/e1_cusp_spectrum.csv: the orbifold eigenvalues lambda_1..lambda_6 per m at both levels.

Asserted (before writing): Triangle.verify() for every m (angles, area, side lengths); Neumann
lambda_0 = 0 to 1e-8; for lambda_1..lambda_6 the two levels agree to 1e-6 relative; the upper bound
of the eigen paper's Proposition (unbounded orders), lambda_j <= 1/4 + pi^2 (j+1)^2 / h_m^2 with
h_m = arccosh(1/(2 sin(pi/m))), holds for j = 1..6; every lambda_j (j >= 1) exceeds 1/4 and
decreases strictly in m.
"""
import math
import re
import subprocess
import sys
import time

from common import ROOT, write_csv

sys.path.insert(0, str(ROOT / "numerics"))

MS = [7, 8, 10, 12, 16, 24, 32, 48, 64, 96, 128, 192, 256, 384, 512, 768, 1024, 1536, 2048, 3072, 4096]
LEVELS = [(0.1, 8), (0.07, 10)]
NEV = 12
JMAX = 6


def memory_guard(minimum=20, poll=120, limit=1800):
    t0 = time.time()
    while True:
        out = subprocess.run(["memory_pressure", "-Q"], capture_output=True, text=True).stdout
        free = int(re.search(r"free percentage:\s*(\d+)%", out).group(1))
        if free >= minimum:
            return free
        if time.time() - t0 > limit:
            sys.exit(f"MemoryBusy: free memory {free}% < {minimum}% for 30 minutes")
        time.sleep(poll)


def h_m(m):
    return math.acosh(1 / (2 * math.sin(math.pi / m)))


def main():
    import numpy as np
    import solve
    from geometry import Triangle

    rows, spec = [], {}
    for m in MS:
        memory_guard()
        Triangle(m, 2, 3).verify()
        for (h, p) in LEVELS:
            both = []
            for bc in ("N", "D"):
                t0 = time.time()
                S = solve.assemble((m, 2, 3), bc, h, p)
                lam, _, info = solve.eigenvalues_robust(S["A"], S["M"], NEV, k=30)
                lam = np.sort(lam)[:NEV]
                if bc == "N":
                    assert abs(lam[0]) < 1e-8, (m, h, p, lam[0])
                    lam[0] = 0.0
                for j, v in enumerate(lam):
                    rows.append((m, h, p, bc, j, f"{v:.12g}", S["ne"], S["A"].shape[0]))
                both += [(float(v), bc) for v in lam]
                print(f"m={m} {bc} h={h} p={p}: ne={S['ne']} ndof={S['A'].shape[0]} "
                      f"{time.time() - t0:.1f}s lam[:4]={np.round(lam[:4], 6)}", flush=True)
            both.sort()
            spec[(m, h, p)] = both[:JMAX + 1]
    # assertions
    out = []
    prev = None
    for m in MS:
        coarse, fine = spec[(m, *LEVELS[0])], spec[(m, *LEVELS[1])]
        assert coarse[0][0] == 0.0 == fine[0][0]
        lam = []
        for j in range(1, JMAX + 1):
            a, b = coarse[j][0], fine[j][0]
            assert coarse[j][1] == fine[j][1], (m, j)
            assert abs(a - b) <= 1e-6 * b, (m, j, a, b)
            bound = 0.25 + math.pi ** 2 * (j + 1) ** 2 / h_m(m) ** 2
            assert 0.25 < b <= bound, (m, j, b, bound)
            lam.append(b)
            out.append((m, j, f"{b:.12g}", f"{a:.12g}", f"{abs(a - b) / b:.3g}", fine[j][1], f"{h_m(m):.12g}",
                        f"{bound:.12g}"))
        if prev is not None:
            assert all(x < y for x, y in zip(lam, prev)), (m, lam, prev)
        prev = lam
    write_csv("e1_cusp_eigs.csv", ["m", "h", "p", "bc", "j", "lambda", "elements", "dofs"], rows)
    write_csv("e1_cusp_spectrum.csv", ["m", "j", "lambda", "lambda_coarse", "rel_diff", "bc", "h_m", "rayleigh_bound"], out)
    print(f"E1 data: {len(MS)} orders m = {MS[0]}..{MS[-1]}, lambda_1..lambda_{JMAX} at two levels, "
          f"all assertions passed")


if __name__ == "__main__":
    main()
