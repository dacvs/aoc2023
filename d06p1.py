import lib
import d06
block = lib.block("input/06.txt")
ts = [int(t) for t in block[0].split()[1:]]
ds = [int(d) for d in block[1].split()[1:]]
ans = 1
for i in range(len(ts)):
    ans *= d06.num_ways(ts[i], ds[i])
print("ans", ans)
