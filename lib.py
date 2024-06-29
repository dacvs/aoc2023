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
