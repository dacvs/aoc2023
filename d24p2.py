import numpy as np
import d24

def cross3(u, v):
    c = np.empty((3,), dtype="object")  # "object": Python big integers
    c[0] = u[1] * v[2] - u[2] * v[1]
    c[1] = u[2] * v[0] - u[0] * v[2]
    c[2] = u[0] * v[1] - u[1] * v[0]
    return c

# https://en.wikipedia.org/wiki/Skew_lines#Nearest_points
def skewdist2(p1, d1, p2, d2):
    """
    Square of distance between two skew lines in R3 (see Wikipedia article for notation).
    Each input line is determined by a point in the line and a vector.

    Args:
        p1: first  point;  entries are Python (big) ints
        d1: first  vector; entries are Python (big) ints
        p2: second point;  entries are Python (big) ints
        d2: second vector; entries are Python (big) ints
    """
    n  = cross3(d1, d2)
    n1 = cross3(d1, n)
    n2 = cross3(d2, n)
    c1 = p1 + d1 * d24.dot(p2 - p1, n2) // d24.dot(d1, n2)
    c2 = p2 + d2 * d24.dot(p1 - p2, n1) // d24.dot(d2, n1)
    d  = c1 - c2
    return d24.dot(d, d)

def obj(P0, D0, I, J, s, t):  # square of distance works fine
    p = P0[I] + s * D0[I]
    q = P0[J] + t * D0[J]
    return sum(skewdist2(p, q - p, P0[k], D0[k]) for k in range(len(P0)))

def two_skew_input_rays(P0, D0):
    for i in range(len(P0)):
        for j in range(len(P0)):
            if np.any(cross3(D0[i], D0[j]) != 0):  # nonparallel
                if 0 < skewdist2(P0[i], D0[i], P0[j], D0[j]):
                    return i, j

# The plan:
# Pick 2 input rays:
#     pi + s * di for s >= 0
#     pj + t * dj for t >= 0
# Independent variables are s, t.
# Let L(s, t) be the line in R3 containing point pi + s * di and point pj + t * dj.
# Objective function: sum over input lines of distance (between 2 skew lines) to L(s, t).
# Local grid search:
#     Adjust s or t by +/- 10**e for e in [0, 1, ..., 12], say, and accept the best. Repeat.
# Objective value should shrink to 0.
# Then we know the line containing the solution.

P0, D0 = d24.points_directions()
I, J = two_skew_input_rays(P0, D0)

# FIND THE LINE CONTAINING THE SOLUTION RAY
dws = [g * 10**e for g in [-1, +1] for e in range(13)]
s = 0
t = 0
while True:
    f = obj(P0, D0, I, J, s, t)
    print(f"s={s:13d}, t={t:13d}, f={f}")
    if f == 0:
        break
    fs, ds = min((obj(P0, D0, I, J, s + dw, t), dw) for dw in dws if 0 <= s + dw)
    ft, dt = min((obj(P0, D0, I, J, s, t + dw), dw) for dw in dws if 0 <= t + dw)
    if fs < ft:
        s += ds
    else:
        t += dt

# FIND SOLUTION INITIAL POSITION
p  = P0[I] + s * D0[I]
q  = P0[J] + t * D0[J]
Pn = t * p - s * q      # solution's initial position P numerator
Pd = t - s              # solution's initial position P denominator
P  = Pn // Pd
print("ans", np.sum(P))
