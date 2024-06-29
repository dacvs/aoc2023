import lib
import numpy as np

def d11(expansion_factor):
    A = np.array([list(s.strip()) for s in lib.block("input/11.txt")])
    I, J = A.shape
    empty_cols = np.all(A == '.', axis=0).astype(int)
    empty_rows = np.all(A == '.', axis=1).astype(int)
    cum_empty_cols = np.add.accumulate(empty_cols)
    cum_empty_rows = np.add.accumulate(empty_rows)
    G = [(i, j) for i in range(I) for j in range(J) if A[i, j] == '#']
    ans = 0
    for v in range(len(G)):
        for u in range(v):
            i0 = min(G[u][0], G[v][0])
            i1 = max(G[u][0], G[v][0])
            j0 = min(G[u][1], G[v][1])
            j1 = max(G[u][1], G[v][1])
            empty_rows = cum_empty_rows[i1] - cum_empty_rows[i0]
            empty_cols = cum_empty_cols[j1] - cum_empty_cols[j0]
            ans += i1 - i0 + j1 - j0 + (empty_cols + empty_rows) * (expansion_factor - 1)
    print("ans", ans)
