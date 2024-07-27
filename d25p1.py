import numpy as np
import lib

# union-find data structure: https://en.wikipedia.org/wiki/Disjoint-set_data_structure

def find(parent, x: int) -> int:  # as in the union-find data structure
    while x != parent[x]:
        x = parent[x]
    return x

N = {}
for line in lib.block("input/25.txt"):
    u, vs = line.split(':')
    vs = [v.strip() for v in vs.split()]
    N[u] = set(vs)

A = [tuple(sorted((u, v))) for u in N for v in N[u]]

for u, v in A:
    if not u in N:
        N[u] = set()
    if not v in N:
        N[v] = set()
    N[u] |= set([v])
    N[v] |= set([u])
V = sorted(N.keys())
D = {v: i for i, v in enumerate(V)}

M = {}  # M is like N but with indices into V for both keys and values
for u in N:
    M[D[u]] = sorted([D[v] for v in N[u]])

E = []  # E is like A but with indices into V
for i in M:
    for j in M[i]:
        if i < j:
            E.append((i, j))
E.sort()

# KARGER'S ALGORITHM
#
# Until only 2 vertices remain:
#     Choose an edge e uniformly at random.
#     Contract e.
# The remaining cut is the one we want, if it is a 3-cut.
# May need to try many times. We expect at most n^2 log n times.
#
# Need a graph structure that supports the operations.
# If we keep an edge as a pair of vertices, there is no need to do anything
# with the edges except mark them as contracted (deleted). Vertices need
# to know which other vertices they have been grouped with. Union-Find.

smallest_cut_size = -1
while True:
    num_vertices = len(V)  # supervertices
    parent = list(range(len(V)))  # union-find
    AK = list(range(len(A)))

    while 2 < num_vertices:
        # CHOOSE AN EDGE UNIFORMLY AT RANDOM
        t = np.random.randint(len(AK))
        k = AK[t]
        AK[t] = AK[-1]
        AK.pop()

        # CONTRACT THE CHOSEN EDGE
        i, j = E[k]
        x = find(parent, i)
        y = find(parent, j)
        if x != y:
            parent[y] = parent[x]  # the union operation of the union-find data structure
            num_vertices -= 1

    # THE REMAINING CUT
    cut = []
    for k in AK:
        i, j = E[k]
        x = find(parent, i)
        y = find(parent, j)
        if x != y:
            cut.append((V[i], V[j]))

    if not 0 <= smallest_cut_size <= len(cut):
        smallest_cut_size = len(cut)
    print(f"smallest_cut_size={smallest_cut_size}, len(cut)={len(cut)}")

    if len(cut) <= 3:
        # REMOVE THE CUT
        for a in cut:
            u, v = a
            N[u] = set(w for w in N[u] if w != v)
            N[v] = set(w for w in N[v] if w != u)

        for k in AK:
            i, j = E[k]
            x = find(parent, i)
            y = find(parent, j)
            if x != y:
                c = len(lib.dfs(N, V[i]))  # size of component of V[i]
                d = len(lib.dfs(N, V[j]))  # size of component of V[j]
                print(k, i, j, V[i], V[j], c, d, "ans", c * d)
        break
