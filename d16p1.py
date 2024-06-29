import numpy as np
import lib
import d16
A = np.array([list(s) for s in lib.block("input/16.txt")])
rays = [(0, 0, 'E')]
ans = d16.num_energized(A, rays)
print("ans", ans)
