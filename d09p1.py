import numpy as np
import lib
import d09
ans = 0
for s in lib.block("input/09.txt"):
    As = [np.array([int(n) for n in s.split()])]
    while not np.all(0 == As[-1]):
        As.append(d09.diff(As[-1]))
    ans += sum(A[-1] for A in As)
print("ans", ans)
