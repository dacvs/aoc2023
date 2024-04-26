def dmap(dsls, n):
    for d, s, l in dsls:
        if s <= n < s + l:
            return n + d - s
    return n


import d05
seeds, M = d05.seeds_maps("input.txt")
ans = -1
for seed in seeds:
    soil        = dmap(M[0], seed)
    fertilizer  = dmap(M[1], soil)
    water       = dmap(M[2], fertilizer)
    light       = dmap(M[3], water)
    temperature = dmap(M[4], light)
    humidity    = dmap(M[5], temperature)
    location    = dmap(M[6], humidity)
    if ans < 0 or location < ans:
        ans = location
print("ans", ans)
