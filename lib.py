def blocks(filename):
    with open(filename) as f:
        for block in f.read().split("\n\n"):
            yield [line for line in block.split("\n") if line]

def block(filename):  # when only 1 block is expected
    return next(blocks(filename))

def split(line, seps):
    out = []
    for sep in seps:
        pre, line = line.split(sep, maxsplit=1)
        out.append(pre)
    return out + [line]

def symmetrize(N):
    """
    Let N represent a directed graph where set N[v] is the outneighborhood of vertex v.
    Extend N so that N[v] contains u whenever N[u] contains v.
    """
    for u in N:
        for v in N[u]:
            if not u in N[v]:
                N[v] |= set([u])

def dfs(N, u0):
    """
    Let N represent a symmetric directed graph where set N[v] is the outneighborhood of vertex v.
    Do a depth-first search from u0. Return a list in proper order, beginning with v, of
    vertices in the component of u0. Each vertex appears once.
    """
    out = []
    seen = set()
    stack = [u0]
    while stack:
        u = stack.pop()
        if not u in seen:
            seen |= set([u])
            out.append(u)
            for v in N[u]:
                stack.append(v)
    return out

def component(N, u0):
    # TODO clarify. Maybe "reachable"? Singly conn component? weak component?
    # TODO simplify -- or formulate as DFS or BFS?
    """
    In a directed graph where N[v] is the outneighborhood of vertex v, find the
    component that contains vertex u0. Return the set of vertices of that component.
    """
    N = {u: list(N[u]) for u in N}  # make a copy
    out = set()
    stack = [u0]
    while stack:
        u = stack[-1]
        while N[u] and N[u][-1] in out:
            N[u].pop()
        if N[u]:
            v = N[u].pop()
            stack.append(v)
        else:
            stack.pop()
            out |= set([u])
    return out

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

def topsort_verified(N):
    V = list(topsort(N))
    D = {u: i for i, u in enumerate(V)}
    assert len(V) == len(N)
    for u in N:
        for v in N[u]:
            assert D[u] > D[v]
    return V
