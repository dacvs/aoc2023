import lib
import d10
_, _, N, S = d10.graph_start()
U = lib.dfs(N, S)  # component of S, i.e., the loop
print("ans", len(U) // 4)
