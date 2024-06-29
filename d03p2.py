import lib
import numpy as np
D = "0123456789" 
A = np.array([list(s) for s in lib.block("input/03.txt")])
I, J = A.shape
ans = 0
for g in range(I):
    for h in range(J):
        if A[g, h] == '*':  # a gear at (g, h)
            nbrs = []
            for i in [g - 1, g, g + 1]:
                if 0 <= i < I:
                    for j0 in range(J):
                        if A[i, j0] in D:
                            if j0 == 0 or not A[i, j0 - 1] in D:  # (i, j0) begins a number
                                j1 = j0 + 1
                                while j1 < J and A[i, j1] in D:
                                    j1 += 1  # a number is in row i, columns [j0, j1)
                                if j0 - 1 <= h <= j1:
                                    nbrs.append(int(''.join(A[i, j0 : j1])))
            if len(nbrs) == 2:
                ans += nbrs[0] * nbrs[1]
print("ans", ans)
