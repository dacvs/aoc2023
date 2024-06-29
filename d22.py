import numpy as np
import lib

def overlap(A):
    A0 = np.max(A[:, 0], axis=0)
    A1 = np.min(A[:, 1], axis=0)
    return np.all(A0 <= A1)  # nonempty in each dimension

def nbhd(A, u):  # bricks that overlap u (in x,y-plane) and are below u
    for v in range(len(A)):
        if overlap(A[[u, v], :, :2]) and A[v, 1, 2] < A[u, 0, 2]:
            yield v

def supports(A, u, v):
    return overlap(A[[u, v], :, :2]) and A[u, 1, 2] + 1 == A[v, 0, 2]

def supporters(A, N, v):
    return set(u for u in N[v] if A[u, 1, 2] + 1 == A[v, 0, 2])

def supporteds(A, u):
    return set(v for v in range(len(A)) if supports(A, u, v))

def drop(A, N, v):
    # Move v down as far as possible (avoiding other bricks and the floor).
    d = A[v, 0, 2] - 1 # d: distance to rest on floor
    for u in N[v]:
        if A[v, 0, 2] > A[u, 1, 2]:  # u below v
            c = A[v, 0, 2] - A[u, 1, 2] - 1
            if c < d:
                d = c
    A[v, :, 2] -= d

def str2list(s):
    cvt = lambda c: ',' if c == '~' else c
    s = ''.join(cvt(c) for c in s)
    a = [int(n) for n in s.split(',')]
    assert np.all(a[0:3] <= a[3:6])
    return a

def d22():
    A = np.array([str2list(s) for s in lib.block("input/22.txt")])
    A = A.reshape(-1, 2, 3)
    N = {}
    for u in range(len(A)):
        if u % 50 == 0:
            print(f"Compute neighborhoods {u} / {len(A)}")
        N[u] = list(nbhd(A, u))
    V = lib.topsort_verified(N)  # first vertices of V are lowest
    for u in V:
        drop(A, N, u)
    return A, N, V
