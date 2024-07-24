import numpy as np
import lib

def go(i, j, ch):  # ch is one of "<>v^"
    if ch == '>': return i, j + 1
    if ch == 'v': return i + 1, j
    if ch == '<': return i, j - 1
    if ch == '^': return i - 1, j

def grid_nbrs(T, i, j):
    I, J = T.shape
    for ch in "<>v^":
        a, b = go(i, j, ch)
        if a in range(I) and b in range(J):
            yield a, b

def is_trail_vertex(T, i, j):  # internal vertex: a vertex other than Beg or End
    """Is cell (i, j) an internal vertex of the trail graph (see below)?"""
    return T[i, j] == '.' and 1 < sum(1 for v in grid_nbrs(T, i, j) if T[v] in "<>v^")

def outlets(T, i, j):
    """cells adjacent to (i, j) containing an arrow directed out from (i, j)"""
    for (a, b) in grid_nbrs(T, i, j):
        if T[a, b] in "<>v^" and (a, b) == go(i, j, T[a, b]):
            yield a, b

def trail_graph():
    """
    Convert day 23 problem input to a trail graph.

    Returns: tuple (Beg, End, N, arc_wt)
        Beg:    beginning vertex (we begin BEFORE the first row)
        End:    ending vertex
        N:      if u is a vertex, then N[u] is the set of its outneighbors
        arc_wt: if u, v are vertices, with v in N[u], then arc_wt[u, v] is the
                    length of the trail from u to v.
    """
    T = np.array([list(s) for s in lib.block("input/23.txt")])
    I, J = T.shape

    # TRAIL GRAPH
    #
    # At some points on the map, you can choose to follow one of several trails that
    # depart from that point. You follow the trail until you reach another such point
    # (or the finish). Each such point (and start and finish) is a vertex of the trail
    # graph. Each trail is an arc of the trail graph.
    #
    # Start at the sole '.' in the first row. NOTE: we begin BEFORE the first row.
    # Finish at the sole '.' in the last row.
    # Please see illustration in README.md, section Day 23.

    BegArrow    = [(    0, j) for j in range(J) if T[ 0, j] == '.']  # first row
    End         = [(I - 1, j) for j in range(J) if T[-1, j] == '.']  # last row
    assert 1 == len(BegArrow)
    assert 1 == len(End     )
    BegArrow    = BegArrow[0]
    End         = End[0]
    Beg         = go(*BegArrow, '^')  # begin BEFORE the first row
    EndArrow    = go(*End     , '^')
    T[BegArrow] = 'v'
    T[EndArrow] = 'v'

    # TRAIL GRAPH VERTICES
    V = set((i, j) for i in range(I) for j in range(J) if is_trail_vertex(T, i, j))

    # HELPER GRAPH FOR TRACING TRAILS
    def tracing_nbhd(T, i, j):
        return set(v for v in grid_nbrs(T, i, j) if T[v] != '#' and not (i, j) in V)

    Nt = {(i, j): tracing_nbhd(T, i, j) for i in range(I) for j in range(J)}

    # TRAIL GRAPH NEIGHBORHOODS AND WEIGHTS
    N = {}
    arc_wt = {}
    for u in V | set([Beg, End]):
        N[u] = set()
        for x in outlets(T, *u):
            Nt[x] -= set([u])
            U = lib.dfs(Nt, x)
            v = U[-1]
            N[u] |= set([v])
            arc_wt[u, v] = len(U)

    return Beg, End, N, arc_wt
