def diff(A):
    return A[1:] - A[:-1]


import numpy as np
with open("input.txt") as f:
    ans = 0
    for s in f:
        As = [np.array([int(n) for n in s.split()])]
        while not np.all(0 == As[-1]):
            As.append(diff(As[-1]))
        ans += sum((-1)**i * A[0] for i, A in enumerate(As))
    print("ans", ans)
