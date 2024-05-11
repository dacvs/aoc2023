import numpy as np
import d16
with open("input.txt") as f:
    A = np.array([list(s.strip()) for s in f])
    rays = [(0, 0, 'E')]
    ans = d16.num_energized(A, rays)
    print("ans", ans)
