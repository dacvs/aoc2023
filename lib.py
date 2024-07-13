def blocks(filename):
    """
    Advent of Code input files sometimes have multiple sections delimited by empty lines.
    Yield each section ("block") of the file as a list of lines. (Newlines are gone.)
    """
    with open(filename) as f:
        for block in f.read().split("\n\n"):
            yield [line for line in block.split("\n") if line]

def block(filename):
    """
    Return the first block of a file as a list of lines.
    """
    return next(blocks(filename))

def split(line, seps):
    """
    Split a string into fields, where fields are delimited by a (possibly
    varying) sequence of separators. Returns one more field than separator.
    For example, split("f: a -> b", [": ", " -> "]) returns ["f", "a", "b"].
    """
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

def topsort(N):
    """
    Topological sort of a directed graph represented by N.
    N is a dictionary. Each vertex is mapped to a collection of its neighbors.
    Yield each vertex in proper order.
    """
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
    """
    Topological sort (see `topsort` above) with work done afterward to ensure
    vertices are in proper order. Return sequence of vertices as a list.
    """
    V = list(topsort(N))
    D = {u: i for i, u in enumerate(V)}
    assert len(V) == len(N)
    for u in N:
        for v in N[u]:
            assert D[u] > D[v]
    return V
