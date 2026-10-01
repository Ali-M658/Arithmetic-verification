"""High-order FEM eigenvalues of a hyperbolic triangle, Neumann or Dirichlet.

    -Delta_E u = lambda w(z) u  on the triangle T(p,q,r) in the Poincare disk,
    w(z) = 4 / (1 - |z|^2)^2,
discretised with NGSolve H1 elements of order `order` on a mesh of uniform
hyperbolic size `h` (Euclidean size h (1-|z|^2)/2), with the geodesic side
represented exactly (rational quadratic spline) and curved to the element order.

Many eigenvalues are obtained by spectral slicing: shift-invert Lanczos
(ARPACK) at a sequence of shifts sigma_i; each slice returns the k eigenvalues
nearest sigma_i, so every eigenvalue in the open interval
(sigma_i - rho_i, sigma_i + rho_i), rho_i = max |lambda - sigma_i| over the
returned values, is captured.  Consecutive slices are required to overlap and
each slice contributes only the part of its certified interval up to the
midpoint of the overlap, which gives a complete list with multiplicity.

usage:  python solve.py P Q R {N|D} --h H --order P --nev N [--out file.npz]
"""

import argparse
import os
import time

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla

from geometry import Triangle, make_mesh, weight_cf


# Dirichlet sides per boundary condition.  "N" and "D" are the pillow's even and
# odd parts; the two mixed conditions are used only in the (2,3,8) benchmark,
# where they are the remaining one-dimensional characters of the reflection
# group (sides ab and bc meet at the pi/3 corner, so their signs must agree).
DIRICHLET_SIDES = {"N": "", "D": "ab|bc|ac", "M1": "ab|bc", "M2": "ac"}


def assemble(pqr, bc, h, order, geom_order=None):
    import ngsolve as ngs
    T = Triangle(*pqr)
    mesh = make_mesh(T, h, geom_order or order)
    fes = ngs.H1(mesh, order=order, dirichlet=DIRICHLET_SIDES[bc])
    u, v = fes.TnT()
    w = weight_cf()
    a = ngs.BilinearForm(ngs.grad(u) * ngs.grad(v) * ngs.dx).Assemble()
    # w is a rational function: give the quadrature extra order
    m = ngs.BilinearForm(w * u * v * ngs.dx(bonus_intorder=2 * order)).Assemble()
    fd = np.array(list(fes.FreeDofs()), dtype=bool)
    A = sp.csr_matrix(a.mat.CSR())[fd][:, fd]
    M = sp.csr_matrix(m.mat.CSR())[fd][:, fd]
    A = (A + A.T) * 0.5
    M = (M + M.T) * 0.5
    area = ngs.Integrate(w * ngs.dx(bonus_intorder=2 * order), mesh)
    return dict(A=A.tocsc(), M=M.tocsc(), mesh=mesh, fes=fes, freedofs=fd,
                area_fem=area, area_exact=float(T.area_exact), ne=mesh.ne)


def slice_eigs(A, M, sigma, k, want_vectors=False):
    """k eigenvalues of A x = lam M x nearest sigma, via one LU of A - sigma M."""
    n = A.shape[0]
    lu = sla.splu((A - sigma * M).tocsc(), permc_spec="COLAMD")
    op = sla.LinearOperator((n, n), matvec=lu.solve, dtype=float)
    out = sla.eigsh(A, k=k, M=M, sigma=sigma, which="LM", OPinv=op,
                    return_eigenvectors=want_vectors, tol=0)
    if want_vectors:
        vals, vecs = out
        idx = np.argsort(vals)
        return vals[idx], vecs[:, idx]
    return np.sort(out), None


def eigenvalues(A, M, nev, k=160, want_vectors=False, verbose=True):
    """Complete sorted list of the eigenvalues below the end of the slice that
    first certifies at least nev of them.

    Slice i (shift sigma_i, radius rho_i) certifies every eigenvalue in
    (sigma_i - rho_i, sigma_i + rho_i).  Consecutive windows must overlap; the
    cut between slices i and i+1 is the midpoint of their overlap and slice i
    contributes exactly the eigenvalues in [cut_{i-1}, cut_i)."""
    slices = []
    sigma = -1.0
    while True:
        t0 = time.time()
        vals, vecs = slice_eigs(A, M, sigma, k, want_vectors)
        rho = float(np.max(np.abs(vals - sigma)))
        tries = 0
        while slices and not sigma - rho < slices[-1][0] + slices[-1][1]:
            # window too narrow for this shift: move the shift back so that the
            # new window starts inside the previous one, and redo the slice
            tries += 1
            if tries > 8:
                raise RuntimeError(f"slice windows do not overlap at sigma={sigma}")
            sigma = slices[-1][0] + slices[-1][1] + 0.7 * rho
            vals, vecs = slice_eigs(A, M, sigma, k, want_vectors)
            rho = float(np.max(np.abs(vals - sigma)))
        slices.append((sigma, rho, vals, vecs))
        if verbose:
            print(f"  slice sigma={sigma:10.2f} window=({sigma-rho:9.2f},{sigma+rho:9.2f})"
                  f"  {time.time()-t0:6.1f}s", flush=True)
        n_cert = np.count_nonzero(np.concatenate([s[2] for s in slices]) < sigma + rho)
        # (an over-count of the certified total because of overlaps; exact count below)
        cuts = [-np.inf] + [0.5 * ((slices[i + 1][0] - slices[i + 1][1]) + (slices[i][0] + slices[i][1]))
                            for i in range(len(slices) - 1)] + [sigma + rho]
        n_cert = sum(np.count_nonzero((s[2] >= cuts[i]) & (s[2] < cuts[i + 1]))
                     for i, s in enumerate(slices))
        if n_cert >= nev:
            break
        sigma = sigma + 1.5 * rho
    lam, vec = [], []
    for i, s in enumerate(slices):
        sel = (s[2] >= cuts[i]) & (s[2] < cuts[i + 1])
        lam.append(s[2][sel])
        if want_vectors:
            vec.append(s[3][:, sel])
    lam = np.concatenate(lam)
    order = np.argsort(lam)
    if want_vectors:
        return lam[order], np.concatenate(vec, axis=1)[:, order]
    return lam[order], None


def run(pqr, bc, h, order, nev, k=160, verbose=True):
    t0 = time.time()
    S = assemble(pqr, bc, h, order)
    if verbose:
        print(f"{pqr} {bc} h={h} p={order}: ne={S['ne']} ndof={S['A'].shape[0]} "
              f"area_err={S['area_fem']-S['area_exact']:.2e} "
              f"assembly {time.time()-t0:.1f}s", flush=True)
    lam, _ = eigenvalues(S["A"], S["M"], nev, k=k, verbose=verbose)
    if bc == "N":
        lam[0] = max(lam[0], 0.0) if abs(lam[0]) < 1e-8 else lam[0]
    if verbose:
        print(f"  {len(lam)} eigenvalues, max {lam[-1]:.3f}, total {time.time()-t0:.1f}s", flush=True)
    return lam, S


# Convergence levels (hyperbolic mesh size h, polynomial order p).  The last
# level is the production level; the one before it is the same order on a
# coarser mesh, and their difference is the (conservative) error estimate.
# The others give an h-sweep at p = 10 (h = 0.1, 0.07, 0.05) and a p-sweep at
# h = 0.07 (p = 8, 10, 12) for the convergence rates.
LEVELS = [(0.1, 10), (0.07, 8), (0.07, 12), (0.07, 10), (0.05, 10)]
PROBLEMS = [((2, 8, 8), "N"), ((2, 8, 8), "D"), ((3, 3, 12), "N"), ((3, 3, 12), "D")]
NEV = 1300           # per triangle and boundary condition
BENCH_LEVELS = [(0.1, 8), (0.07, 10)]
BENCH_NEV = 60       # (2,3,8): covers the Bolza list (lambda < 998) with margin
RUNDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs")


def run_path(pqr, bc, h, order):
    return os.path.join(RUNDIR, f"eig_{pqr[0]}-{pqr[1]}-{pqr[2]}_{bc}_h{h}_p{order}.npz")


def suite(problems, levels, nev, k):
    os.makedirs(RUNDIR, exist_ok=True)
    for pqr, bc in problems:
        for h, order in levels:
            out = run_path(pqr, bc, h, order)
            if os.path.exists(out):
                print("exists:", out, flush=True)
                continue
            t0 = time.time()
            lam, S = run(pqr, bc, h, order, nev, k=k)
            np.savez(out, lam=lam, pqr=pqr, bc=bc, h=h, order=order,
                     ndof=S["A"].shape[0], ne=S["ne"],
                     area_err=S["area_fem"] - S["area_exact"], seconds=time.time() - t0)


if __name__ == "__main__":
    import sys
    import ngsolve as ngs
    if len(sys.argv) > 1 and sys.argv[1] in ("suite", "bench"):
        ngs.SetNumThreads(8)
        if sys.argv[1] == "suite":
            suite(PROBLEMS, LEVELS, NEV, k=200)
        else:
            suite([((2, 3, 8), bc) for bc in ("N", "D", "M1", "M2")], BENCH_LEVELS, BENCH_NEV, k=40)
        sys.exit(0)
    ap = argparse.ArgumentParser()
    ap.add_argument("p", type=int)
    ap.add_argument("q", type=int)
    ap.add_argument("r", type=int)
    ap.add_argument("bc", choices=list(DIRICHLET_SIDES))
    ap.add_argument("--h", type=float, required=True)
    ap.add_argument("--order", type=int, required=True)
    ap.add_argument("--nev", type=int, default=1000)
    ap.add_argument("--k", type=int, default=160)
    ap.add_argument("--threads", type=int, default=8)
    ap.add_argument("--out")
    a = ap.parse_args()
    ngs.SetNumThreads(a.threads)
    lam, S = run((a.p, a.q, a.r), a.bc, a.h, a.order, a.nev, k=a.k)
    if a.out:
        np.savez(a.out, lam=lam, pqr=(a.p, a.q, a.r), bc=a.bc, h=a.h, order=a.order,
                 ndof=S["A"].shape[0], ne=S["ne"], area_err=S["area_fem"] - S["area_exact"])
