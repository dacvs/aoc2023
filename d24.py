import numpy as np
import lib

def points_directions():
    ps = []
    ds = []
    for s in lib.block("input/24.txt"):
        p, d = s.split('@')
        ps.append([int(t) for t in p.split(',')])
        ds.append([int(t) for t in d.split(',')])
    P = np.array(ps, dtype="object")  # "object": Python big integers
    D = np.array(ds, dtype="object")  # "object": Python big integers
    assert not np.any(D == 0)  # a fact of the input that simplifies certain calculations
    return P, D

def dot(u, v):  # ok for big integers
    return sum(u[i] * v[i] for i in range(len(u)))
