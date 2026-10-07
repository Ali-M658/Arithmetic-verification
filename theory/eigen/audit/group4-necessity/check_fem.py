"""Group 4 audit: coarse P1 finite elements (Klein model) for the low spectra of O(2,3,m) and O_{k,b},
compared with the upper bounds of eig:N1 and eig:N2.  The double of a polygon has spectrum
Neumann(polygon) U Dirichlet(polygon).  Klein model: sqrt(det g) g^{-1} = (1-r^2)^{-1/2}(I - x x^T),
sqrt(det g) = (1-r^2)^{-3/2}.  Centroid quadrature; this is a sanity check, not a certificate.
Raises if a computed eigenvalue exceeds the claimed bound by more than 2% (would signal an error).
"""
import numpy as np


def assemble(nodes, tris):
    n = len(nodes)
    K = np.zeros((n, n)); M = np.zeros((n, n))
    for t in tris:
        p = nodes[t]
        J = np.array([p[1] - p[0], p[2] - p[0]]).T
        det = np.linalg.det(J)
        area = abs(det)/2
        if area < 1e-16:
            continue
        G = np.linalg.solve(J.T, np.array([[-1, 1, 0], [-1, 0, 1]]))  # grads (2x3)
        c = p.mean(axis=0); r2 = c @ c
        A = (np.eye(2) - np.outer(c, c))/np.sqrt(1 - r2)
        w = (1 - r2)**-1.5
        Ke = area*G.T @ A @ G
        Me = area*w*(np.ones((3, 3)) + np.eye(3))/12
        for i in range(3):
            for j in range(3):
                K[t[i], t[j]] += Ke[i, j]; M[t[i], t[j]] += Me[i, j]
    return K, M


def geig(K, M, keep):
    K = K[np.ix_(keep, keep)]; M = M[np.ix_(keep, keep)]
    L = np.linalg.cholesky(M)
    Li = np.linalg.inv(L)
    return np.sort(np.linalg.eigvalsh(Li @ K @ Li.T))


def double_spectrum(nodes, tris, bdry, nev=8):
    K, M = assemble(nodes, tris)
    used = np.unique(tris)
    neu = geig(K, M, used)[:nev]
    dir_ = geig(K, M, np.array([i for i in used if i not in bdry]))[:nev]
    return np.sort(np.concatenate([neu, dir_]))[:nev]


def grid(X, Y):
    nx, ny = X.shape
    idx = np.arange(nx*ny).reshape(nx, ny)
    nodes = np.stack([X.ravel(), Y.ravel()], axis=1)
    tris = []
    for i in range(nx - 1):
        for j in range(ny - 1):
            a, b, c, d = idx[i, j], idx[i + 1, j], idx[i + 1, j + 1], idx[i, j + 1]
            tris += [[a, b, c], [a, c, d]]
    bd = set(idx[0, :]) | set(idx[-1, :]) | set(idx[:, 0]) | set(idx[:, -1])
    return nodes, np.array(tris), idx, bd


fails = []
print("O(2,3,m): triangle P=0, Q=(tanh h,0), R=(tanh h, tanh h tan(pi/m)) in the Klein model")
for m in (7, 10, 20, 50):
    h = np.arccosh(1/(2*np.sin(np.pi/m)))
    nxi, nze = 110, 12
    xi = np.linspace(0, 1, nxi); ze = np.linspace(0, 1, nze)
    XI, ZE = np.meshgrid(xi, ze, indexing='ij')
    X = np.tanh(XI*h); Y = X*np.tan(np.pi/m)*ZE
    nodes, tris, idx, _ = grid(X, Y)
    # merge the collapsed first column into the single node P
    remap = np.arange(len(nodes)); remap[idx[0, :]] = idx[0, 0]
    tris = remap[tris]
    bd = set(remap[idx[0, :]]) | set(idx[-1, :]) | set(idx[:, 0]) | set(idx[:, -1])
    ev = double_spectrum(nodes, tris, bd, nev=6)
    print(f" m={m:3d} h_m={h:.4f}")
    for j in range(1, 6):
        bound = 0.25 + np.pi**2*(j + 1)**2/h**2
        flag = "" if ev[j] <= 1.02*bound else "  <-- EXCEEDS BOUND"
        if flag: fails.append(("N1", m, j))
        print(f"   lambda_{j} ~ {ev[j]:.4f}   bound {bound:.4f}{flag}")

print("O_{k,b}: Q = [-tanh b, tanh b] x [-tanh a, tanh a] in the Klein model")
for k in (3, 4):
    for b in (0.5, 0.2, 0.1, 0.05):
        a = np.arcsinh(np.cos(np.pi/k)/np.sinh(b))
        nx, ny = 9, 260
        X, Y = np.meshgrid(np.linspace(-np.tanh(b), np.tanh(b), nx),
                           np.tanh(np.linspace(-a, a, ny)), indexing='ij')
        # corner check: (tanh b, tanh a) inside the disc
        if not np.tanh(b)**2 + np.tanh(a)**2 < 1:
            raise AssertionError("corner outside disc")
        nodes, tris, idx, bd = grid(X, Y)
        ev = double_spectrum(nodes, tris, bd, nev=6)
        b1 = np.sinh(a)/((a*a + 2)*np.sinh(a) - 2*a*np.cosh(a))
        line = f" k={k} b={b:<5} a={a:.3f}  lambda_1~{ev[1]:.4f} (bound {b1:.4f})"
        if ev[1] > 1.02*b1: fails.append(("N2-1", k, b))
        for j in (2, 3, 4):
            bj = 0.25 + 1/(4*np.cosh(a/2)**2) + 4*np.pi**2*(j + 1)**2/a**2
            line += f"  l{j}~{ev[j]:.4f} (bd {bj:.2f})"
            if ev[j] > 1.02*bj: fails.append(("N2-j", k, b, j))
        print(line)
if fails:
    raise AssertionError(f"FEM eigenvalue above claimed bound: {fails}")
print("FEM CHECKS PASSED (all computed eigenvalues below the claimed upper bounds)")
