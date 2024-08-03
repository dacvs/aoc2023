import lib
import d21
C, R = d21.cartesian()
N = {(x, y): d21.nbhd(C, R, x, y) for x in range(-R, R + 1) for y in range(-R, R + 1)}
W = lambda u, v: 1
u0 = (0, 0)
goal = set()
D = lib.dijkstra(N, W, u0, goal)
print("ans", sum(1 for d in D.values() if d <= 64 and d % 2 == 0)) 
