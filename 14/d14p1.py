import numpy as np
with open("input.txt") as f:
    A = np.array([list(s.strip()) for s in f])
    I, J = A.shape
    ans = 0
    for j in range(J):  # tally each column independently
        points = I + 1
        for i in range(I):
            if A[i, j] == '#':
                points = I - i
            if A[i, j] == 'O':
                points -= 1
                ans += points
    print("ans", ans)
