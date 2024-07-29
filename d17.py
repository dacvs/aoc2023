import numpy as np
import lib

def d17(lo, hi):
    """Step sizes in range(lo, hi)"""
    steps = [-t for t in range(lo, hi)]
    steps += [t for t in range(lo, hi)]
    A = np.array([[int(c) for c in s] for s in lib.block("input/17.txt")])
    I, J = A.shape
    # Number is amount of heat loss if crucible enters that block.
    # Start in upper left and don't count the number there.

    # Vertices are (i, j, k) for i in range(I) for j in range(J) for k in (0, 1)
    #     k = 0 if path switches from horizontal to vertical at this vertex
    #     k = 1 if path switches from vertical to horizontal at this vertex
    V = [(i, j, k) for i in range(I) for j in range(J) for k in (0, 1)]
    u0 = (0, 0, -1)  # special starting vertex with k < 0
    goal = {(I - 1, J - 1, k) for k in (0, 1)}

    def nbhd(i, j, k):
        if k == 0: return set((i + d, j, 1) for d in steps if i + d in range(I))
        if k == 1: return set((i, j + d, 0) for d in steps if j + d in range(J))

    N = {u: nbhd(*u) for u in V}
    N[u0] = {(0, 0, k) for k in (0, 1)}

    def W(u, v):
        i0, i1 = sorted((u[0], v[0]))
        j0, j1 = sorted((u[1], v[1]))
        return np.sum(A[i0 : i1 + 1, j0 : j1 + 1]) - A[u[0], u[1]]

    D = lib.dijkstra(N, W, u0, goal)
    print("ans", min(D[u] for u in goal))
