import lib
import d23
Beg, End, N, arc_wt = d23.trail_graph()

# Part 2: graph is undirected
for u in N:
    for v in N[u]:
        arc_wt[v, u] = arc_wt[u, v]
lib.symmetrize(N)

g = {}  # When u is a vertex, g[u] is a dictionary that maps vertex set X to path weight.
        # Path spans X. Path begins at u and ends at End.
maxg = -1
for k in range(len(N)):
    if 0 < k:
        g = G  # g[u] maps vert set X to wt of heaviest X-spanning u,End-path of k - 1 steps
    G = {}     # G[u] maps vert set X to wt of heaviest X-spanning u,End-path of k     steps
    for u in N:
        G[u] = {}
        if k == 0:
            if u == End:
                G[u] = {frozenset([u]): 0}
        else:
            for v in N[u]:
                for X in g[v]:
                    if not u in X:
                        Y = frozenset(X | set([u]))
                        d = g[v][X] + arc_wt[u, v]
                        if (not Y in G[u]) or G[u][Y] < d:
                            G[u][Y] = d
    # heaviest path from Beg to End
    for X in G[Beg]:
        if maxg < G[Beg][X]:
            maxg = G[Beg][X]
    print(f"k={k} maxg={maxg}")
print("ans", maxg - 1)  # -1 because Beg is BEFORE the first row
