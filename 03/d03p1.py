import numpy as np
with open("input.txt") as f:
    D = "0123456789" 
    A = np.array([list(s.strip()) for s in f])
    I, J = A.shape
    ans = 0
    for i in range(I):
        for j0 in range(J):
            if A[i, j0] in D:
                if j0 == 0 or not A[i, j0 - 1] in D:  # (i, j0) begins a number
                    j1 = j0 + 1
                    while j1 < J and A[i, j1] in D:
                        j1 += 1  # a number is in row i, columns [j0, j1)
                    B = A[max(0, i - 1) : min(I, i + 2), max(0, j0 - 1) : min(J, j1 + 1)]
                    if any(b for b in B.flatten() if not b in D + '.'):
                        ans += int(''.join(A[i, j0 : j1]))
    print("ans", ans)
