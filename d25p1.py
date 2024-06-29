import numpy as np
import lib

# union-find data structure: https://en.wikipedia.org/wiki/Disjoint-set_data_structure

def find(parent, x: int) -> int:  # as in the union-find data structure
    while x != parent[x]:
        x = parent[x]
    return x

def component(N, u0):
    N = {u: list(N[u]) for u in N}  # make a copy
    emitted = set()
    stack = [u0]
    while stack:
        u = stack[-1]
        while N[u] and N[u][-1] in emitted:
            N[u].pop()
        if N[u]:
            v = N[u].pop()
            stack.append(v)
        else:
            stack.pop()
            emitted |= set([u])
            yield u

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
E = sorted(E)

# Karger's algorithm:

# Until only 2 vertices remain:
#     Choose an edge e uniformly at random.
#     Contract e.
# The remaining cut is the one we want, if it is a 3-cut.
# May need to try many times. We expect at most n^2 log n times.

# Need a graph structure that supports the operations.
# If we keep an edge as a pair of verts, there is no need to do anything
# with the edges except mark them as contracted (deleted). Vertices need
# to know which other vertices they have been grouped with. Union-Find.

smallest_cut_size = -1

while True:
    num_verts = len(V)  # superverts
    parent = list(range(len(V)))
    AK = list(range(len(A)))

    while 2 < num_verts:
        # choose an edge e uniformly at random ######################################
        t = np.random.randint(len(AK))
        k = AK[t]
        AK[t] = AK[-1]
        AK.pop()

        # contract e ################################################################
        i, j = E[k]
        x = find(parent, i)
        y = find(parent, j)
        if x != y:
            parent[y] = parent[x]  # the union operation of the union-find data structure
            num_verts -= 1

    # the remaining cut
    cut = []
    for k in AK:
        i, j = E[k]
        x = find(parent, i)
        y = find(parent, j)
        if x != y:
            cut.append((V[i], V[j]))

    if smallest_cut_size < 0 or smallest_cut_size > len(cut):
        smallest_cut_size = len(cut)
    print(f"smallest_cut_size={smallest_cut_size}, len(cut)={len(cut)}")

    if len(cut) <= 3:
        # remove the cut
        for a in cut:
            u, v = a
            N[u] = [w for w in N[u] if w != v]
            N[v] = [w for w in N[v] if w != u] 

        for k in AK:
            i, j = E[k]
            x = find(parent, i)
            y = find(parent, j)
            if x != y:
                c = len(list(set(component(N, V[i]))))
                d = len(list(set(component(N, V[j]))))
                print(k, i, j, V[i], V[j], c, d, "ans", c * d)
        break
