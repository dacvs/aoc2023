import numpy as np

def num_energized(A, rays):
    I, J = A.shape
    di = {'E': 0, 'N': -1, 'W': 0, 'S': 1}
    dj = {'E': 1, 'N': 0, 'W': -1, 'S': 0}
    entered = np.zeros((I, J, 4), dtype=int)
    def ind(k): return "ENWS".index(k)
    while rays:
        raysN = []
        for ray in rays:
            i, j, k = ray
            if i in range(I) and j in range(J) and entered[i, j, ind(k)] == 0:
                entered[i, j, ind(k)] = 1
                if A[i, j] == '-' and di[k]:    # splitter
                    for K in "EW":
                        raysN.append((i + di[K], j + dj[K], K))
                elif A[i, j] == '|' and dj[k]:  # splitter
                    for K in "NS":
                        raysN.append((i + di[K], j + dj[K], K))
                elif A[i, j] == '/':            # mirror
                    K = {'E': 'N', 'N': 'E', 'W': 'S', 'S': 'W'}[k]
                    raysN.append((i + di[K], j + dj[K], K))
                elif A[i, j] == '\\':           # mirror
                    K = {'E': 'S', 'N': 'W', 'W': 'N', 'S': 'E'}[k]
                    raysN.append((i + di[K], j + dj[K], K))
                else:                           # pass
                    K = k
                    raysN.append((i + di[K], j + dj[K], K))
        rays = raysN
    return np.sum(np.max(entered, axis=2))
