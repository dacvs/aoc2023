import d09
import numpy as np
with open("input.txt") as f:
    ans = 0
    for s in f:
        As = [np.array([int(n) for n in s.split()])]
        while not np.all(0 == As[-1]):
            As.append(d09.diff(As[-1]))
        ans += sum(A[-1] for A in As)
    print("ans", ans)
