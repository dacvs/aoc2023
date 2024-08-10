import numpy as np
import d24

# test range
A = 200000000000000
B = 400000000000000

def cross2(u, v):
    return u[0] * v[1] - u[1] * v[0]
    
# https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_points_on_each_line
def intersection(p1, p2, p3, p4):  # line 1 contains p1, p2 ; line 2 contains p3, p4
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    x = (x1 * y2 - y1 * x2) * (x3 - x4) - (x1 - x2) * (x3 * y4 - y3 * x4)
    y = (x1 * y2 - y1 * x2) * (y3 - y4) - (y1 - y2) * (x3 * y4 - y3 * x4)
    return x, y

P0, D0 = d24.points_directions()
ans = 0
for i in range(len(P0)):
    p = P0[i, 0:2]
    u = D0[i, 0:2]
    for j in range(i + 1, len(P0)):
        q = P0[j, 0:2]
        v = D0[j, 0:2]
        c = cross2(u, v)
        if c != 0:
            x, y = intersection(p, p + u, q, q + v)
            lo = min(A * c, B * c)
            hi = max(A * c, B * c)
            if lo <= x <= hi and lo <= y <= hi:
                future_p = 0 <= np.sign(c) * (d24.dot((x, y), u) - c * d24.dot(p, u))
                future_q = 0 <= np.sign(c) * (d24.dot((x, y), v) - c * d24.dot(q, v))
                if future_p and future_q:
                    ans += 1
print(f"ans", ans)
