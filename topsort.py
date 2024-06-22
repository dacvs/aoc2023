def topsort(N):
    N = {u: list(N[u]) for u in N}  # make a copy with lists (not sets)
    emitted = set()
    stack = []
    for u0 in N:
        if not u0 in emitted:
            stack.append(u0)
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


def topsort_checked(N):
    V = list(topsort(N))
    D = {u: i for i, u in enumerate(V)}
    #print("N", N)
    #print("V", V)
    assert len(V) == len(N)
    for u in N:
        for v in N[u]:
            assert D[u] > D[v]
    return V
