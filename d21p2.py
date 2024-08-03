import numpy as np
import lib
import d21

def distance_vertices(D):
    """
    Input D is a dict that maps each vertex to its distance from a certain vertex u0.
    Return a dict that maps distance d to the set of vertices u with D[u] = d.
    """
    E = {}
    for (x, y) in D:
        d = D[x, y]
        if not d in E:
            E[d] = set()
        E[d] |= {(x, y)}
    return E

def ball(E):  # like a closed ball in a metric space
    """
    Input E is a dict that maps distance d to the set of vertices u with D[u] = d.
    Return a dict that maps (k, r) to the number of vertices in a single copy of the map
    whose distance from a certain vertex is <= r, where distance % 2 == k.
    """
    d_max = max(E.keys())
    B = {"max": d_max}  # stash the max in here
    for r in range(0, d_max + 1):
        for k in (0, 1):
            B[k, r] = sum(len(E[d]) for d in range(r + 1) if d % 2 == k if d in E)
    return B

def ray(B, e, k, r):
    """
    Rays are discussed in README.md (please see that file).
    A path to a garden plot has two legs:
        first a leg from start to the current tile,
        then a leg from the boundary of the current tile to the end of the walk.

    Args:
        B: BB[x, y] for some x, y
        e: length of tile edge
        k: k=0 if last leg lengths in first tile are even, k=1 if odd.
        r: distance remaining
    """
    d_max = B["max"]
    t = 0

    # In tiles near the center, where plenty of distance is available, every garden plot
    # with the right k can be reached. These tiles are "saturated". We can tally saturated
    # tiles quickly.

    # SATURATED
    n = max(0, (r - d_max) // e)        # n: number of saturated tiles
    t += B[k, d_max] * (n - n // 2)     # first gang (k=k0) is weakly larger
    t += B[1 - k, d_max] * (n // 2)     # second gang (k=1-k0) is weakly smaller

    # UNSATURATED
    d = r - n * e
    k = (k + n) % 2
    while 0 <= d:
        t += B[k, min(d, d_max)]
        d -= e
        k = 1 - k
    return t

r = 26501365            # r: remaining distance (from problem statement)
C, R = d21.cartesian()
e = 2 * R + 1           # e: length of tile edge
N = {}
for x in range(-R, R + 1):
    for y in range(-R, R + 1):
        if C[x, y] != '#':
            N[x, y] = d21.nbhd(C, R, x, y)

# BB[x0, y0][r, k] = #garden plots in a single tile reachable from (x0, y0)
#     in <= r steps by an even walk if k=0, odd if k=1
BB = {}
for x0 in [-R, 0, +R]:
    for y0 in [-R, 0, +R]:
        W = lambda u, v: 1
        u0 = (x0, y0)
        goal = set()
        D = lib.dijkstra(N, W, u0, goal)
        D = {u: D[u] for u in D if D[u] < +np.inf}
        E = distance_vertices(D)
        BB[x0, y0] = ball(E)

# In the center tile          (0, 0), the first leg has length 0 (k=0).
# In the first  tile out, say (0, 1), it takes 66 steps to reach, so no  k-flip.
# In the second tile out, say (0, 2), it takes 66 + 131 to reach, so yes k-flip.
#
# TODO Map is 131 x 131, and 131 is congruent to 3 modulo 4. We expect this value 3.
# Revise the algorithm to handle all residues. Do we expect r odd, too?

# Center tile
k = r % 2
d_max = BB[0, 0]["max"]
d = min(r, d_max)
t = BB[0, 0][k, d]

# Axis tiles
k = r % 2
d = r - R - 1
t += ray(BB[0, -R], e, k, d)        # North
t += ray(BB[-R, 0], e, k, d)        # East
t += ray(BB[0, +R], e, k, d)        # South
t += ray(BB[+R, 0], e, k, d)        # West

# Quadrant tiles
k = r % 2
d = r - 2 * R - 2
while 0 <= d:
    t += ray(BB[-R, -R], e, k, d)   # Northeast
    t += ray(BB[+R, -R], e, k, d)   # Northwest
    t += ray(BB[+R, +R], e, k, d)   # Southwest
    t += ray(BB[-R, +R], e, k, d)   # Southeast
    k = 1 - k
    d -= e

print("ans", t)
