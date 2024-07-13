import numpy as np
import lib

def cells(A, u):
    """Yield each 2D cell (x, y) that brick u contains."""
    for x in range(A[u, 0, 0], A[u, 1, 0] + 1):
        for y in range(A[u, 0, 1], A[u, 1, 1] + 1):
            yield x, y

def nbhd2D(A, B, u):
    """The set of vertices v that overlap the given vertex u in the x,y-plane"""
    out = set()
    for x, y in cells(A, u):
        out |= set(B[x, y])
    return out

def nbhd3D(A, N2, u):
    """The set of 2D neighbors v of the given vertex u, where v is below u"""
    return [v for v in N2[u] if A[v, 1, 2] < A[u, 0, 2]]

def supporters(A, N2, v):
    """Bricks that support v"""
    return set(u for u in N2[v] if A[u, 1, 2] + 1 == A[v, 0, 2])

def supporteds(A, N2, u):
    """Bricks supported by u"""
    return set(v for v in N2[u] if A[u, 1, 2] + 1 == A[v, 0, 2])

def drop(A, N, v):
    """Alter A, moving v down as far as possible (avoiding other bricks and the floor)."""
    d = A[v, 0, 2] - 1 # d: distance to rest on floor
    for u in N[v]:
        if A[v, 0, 2] > A[u, 1, 2]:  # u below v
            c = A[v, 0, 2] - A[u, 1, 2] - 1
            if c < d:
                d = c
    A[v, :, 2] -= d

def ints(s):
    return [int(n) for n in lib.split(s, [",", ",", "~", ",", ","])]

def array_nbhds2D_vertices():
    A = np.array([ints(s) for s in lib.block("input/22.txt")])
    A = A.reshape(-1, 2, 3)
    assert np.all(A[:, 0] <= A[:, 1])

    # B[x, y] is the set of vertices v (bricks) that contain cell (x, y)
    B = {}
    for u in range(len(A)):
        for x, y in cells(A, u):
            if not (x, y) in B:
                B[x, y] = set()
            B[x, y] |= set([u])

    N2 = {u: nbhd2D(A, B , u) for u in range(len(A))}
    N3 = {u: nbhd3D(A, N2, u) for u in range(len(A))}
    V = lib.topsort_verified(N3)  # first vertices of V are lowest
    for u in V:
        drop(A, N3, u)
    return A, N2, V
