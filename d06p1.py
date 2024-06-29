import lib
block = lib.block("input/06.txt")
ts = [int(t) for t in block[0].split()[1:]]
ds = [int(d) for d in block[1].split()[1:]]
ans = 1
for i, t in enumerate(ts):
    winners = 0
    for holdtime in range(t):
        dist = (t - holdtime) * holdtime
        if dist > ds[i]:
            winners += 1
    ans *= winners
print("ans", ans)

