import numpy as np
import d16
with open("input.txt") as f:
    A = np.array([list(s.strip()) for s in f])
    I, J = A.shape
    left   = [[(    i,     0, 'E')] for i in range(I)]
    right  = [[(    i, J - 1, 'W')] for i in range(I)]
    top    = [[(    0,     j, 'S')] for j in range(J)]
    bottom = [[(I - 1,     j, 'N')] for j in range(J)]
    ns = []
    for rays in left + right + top + bottom:
        ns.append(d16.num_energized(A, rays))
        print("rays", rays, f"n={ns[-1]}")
    print("ans", max(ns))
