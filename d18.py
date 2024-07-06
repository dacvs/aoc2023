import numpy as np
import lib

def area_ccw(P):
    """
    Signed area of rectilinear closed simple polygon P
    where P is a sequence of vertices in 2D space, each vertex a 2-vector.
    Area is positive if P is oriented counterclockwise, negative if clockwise.
    Note: The first point of P is not repeated at the end of P.
    """
    area = 0
    for k in range(len(P)):
        dx, dy = P[(k + 1) % len(P)] - P[k]
        if dx != 0:  # such a comparison works fine for integers and half integers
            y = P[k][1]
            area -= dx * y
    return area

def points_directions(part):  # part: 1 or 2
    xys = [(0., 0.)]
    ds = []
    for s in lib.block("input/18.txt"):
        F = s.split()  # s is like "L 4 (#0527c0)"
        if part == 1:
            t = int(F[1])
            d = F[0]
        if part == 2:
            t = int(F[2][2:7], 16)
            d = "RDLU"[int(F[2][7])]
        ds.append(d)
        x, y = xys[-1]
        if d == 'R': xys.append((x + t, y    ))
        if d == 'D': xys.append((x    , y - t))
        if d == 'L': xys.append((x - t, y    ))
        if d == 'U': xys.append((x    , y + t))
    return xys, ds

def d18(part):  # part: 1 or 2
    xys, ds = points_directions(part)

    # polygon is closed?
    assert xys[0] == xys[-1]
    P = np.array(xys[:-1])

    # flip upside down (if needed) so that the loop runs counterclockwise
    if area_ccw(P) < 0:
        P[:, 1] *= -1
        for k in range(len(ds)):
            if   ds[k] == 'U': ds[k] = 'D'
            elif ds[k] == 'D': ds[k] = 'U'

    # bump out so that the lagoon includes its edge
    for k in range(len(P)):
        K = [k, (k + 1) % len(P)]
        if ds[k] == 'R': P[K, 1] -= 0.5
        if ds[k] == 'D': P[K, 0] -= 0.5
        if ds[k] == 'L': P[K, 1] += 0.5
        if ds[k] == 'U': P[K, 0] += 0.5

    print("ans", area_ccw(P))
