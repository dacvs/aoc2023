import numpy as np
import lib

def nbhd(I, J, u, steps):
    i, j, k = u
    if k < 0:  # start
        yield (0, 0, 0)
        yield (0, 0, 1)
    elif k == 0:  # arc from u is vertical
        for di in steps:
            if i + di in range(I):
                yield (i + di, j, 1)
    elif k == 1:  # arc from u is horizontal
        for dj in steps:
            if j + dj in range(J):
                yield (i, j + dj, 0)

def weight(A, u, v):
    i0, i1 = sorted((u[0], v[0]))
    j0, j1 = sorted((u[1], v[1]))
    return np.sum(A[i0 : i1 + 1, j0 : j1 + 1]) - A[u[0], u[1]]

def d17(lo, hi):
    """Step sizes in range(lo, hi)"""
    steps = [+t for t in range(lo, hi)] + [-t for t in range(lo, hi)]
    A = np.array([[int(c) for c in s] for s in lib.block("input/17.txt")])
    I, J = A.shape
    # Number is amount of heat loss if crucible enters that block.
    # Start in upper left and don't count the number there.

    # Let vertices be (i, j, k) for i in range(I) for j in range(J) for k in (0, 1)
    #     k = 0 if path switches from horizontal to vertical at this vertex
    #     k = 1 if path switches from vertical to horizontal at this vertex
    start = (0, 0, -1)  # special vertex with k < 0
    goal = {(I - 1, J - 1, k) for k in (0, 1)}

    # Dijkstra's single-source shortest paths algorithm, distance only
    D = {start: 0}  # D: distance from start (see Dijkstra's algorithm)
    for i in range(I):
        for j in range(J):
            for k in (0, 1):
                D[(i, j, k)] = +np.inf

    # For finite d, Q[d] is the list of not-yet-done vertices v with D[v] = d.
    # When there are no such vertices for a given value d, Q[d] should be empty,
    # but we allow Q[d] to be undefined instead (that is, d is not a key of Q).
    done = set()
    Q = {0: [start]}
    d = 0
    while True:
        if d in Q and Q[d]:
            u = Q[d].pop()
            if not u in done:  # u is the nearest vertex not yet done
                done |= set([u])
                if u in goal:
                    print("ans", D[u])
                    break
                for v in nbhd(I, J, u, steps):
                    if not v in done:
                        w = 0 if u == start else weight(A, u, v)
                        if D[v] > D[u] + w:
                            D[v] = D[u] + w
                            if not D[v] in Q:
                                Q[D[v]] = []
                            Q[D[v]].append(v)
                            assert d <= D[v]
        else:
            d += 1
