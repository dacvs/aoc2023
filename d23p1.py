import lib
import d23
Beg, End, N, arc_wt = d23.trail_graph()
V = lib.topsort_verified(N)  # End is first and Beg is last
maxdist = {}
for u in V:
    maxdist[u] = max((arc_wt[u, v] + maxdist[v] for v in N[u]), default=0)
print("ans", maxdist[Beg] - 1)  # -1 because Beg is BEFORE the first row
