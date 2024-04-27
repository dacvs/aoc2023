def length(F, k):
    i = 0
    while k[-1] != 'Z':
        k = F[k][T[i % len(T)]]
        i += 1
    return i


import numpy as np
import d08
T, F = d08.turns_forks("input.txt")
i = 0
ks = [k for k in F if k[-1] == 'A']
ns = []
for k in ks:
    ns.append(length(F, k))
print("ans", np.lcm.reduce(ns))
