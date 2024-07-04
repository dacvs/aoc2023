import lib
import d10
I, J, N, S = d10.graph_start()
U = lib.dfs(N, S)  # component of S, i.e., the loop

# all grid edges
N = {}
for a in range(2 * I + 1):
    for b in range(2 * J + 1):
        N[(a, b)] = set()
        if a < 2 * I: N[(a, b)] |= set([(a + 1, b)])
        if b < 2 * J: N[(a, b)] |= set([(a, b + 1)])
lib.symmetrize(N)

# delete edges incident to loop vertices
for u in U:
    for v in N[u]:
        N[v] = N[v] - set([u])
    N[u] = set()

# vertices inside the loop are vertices of the sole bounded component
U = set((a, b) for a in range(2 * I + 1) for b in range(2 * J + 1)) - set(U)
while U:  # U: remaining vertices
    u = U.pop()
    V = lib.dfs(N, u)  # component of u
    if not any(a in [0, 2 * I] or b in [0, 2 * J] for (a, b) in V):
        print("ans", sum(1 for (a, b) in V if a % 2 == 1 and b % 2 == 1))
        break
    U = U - set(V)
