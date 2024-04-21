def dmap(d, n):  # d: list of triples
    # triples in d could be large; don't construct the whole map
    for t in d:
        dst0, src0, length = t
        if src0 <= n < src0 + length:
            return n + dst0 - src0
    return n


with open("input.txt") as f:
    D = []
    for s in f:
        if s.startswith("seeds"):
            seeds = [int(n) for n in s[6:].split()]
        else:
            if s.split():
                if not s[0] in "sfwlth":
                    D[-1].append(tuple(int(n) for n in s.split()))
            else:
                D.append([])
    # apply maps to each seed
    ans = -1
    for seed in seeds:
        soil        = dmap(D[0], seed)
        fertilizer  = dmap(D[1], soil)
        water       = dmap(D[2], fertilizer)
        light       = dmap(D[3], water)
        temperature = dmap(D[4], light)
        humidity    = dmap(D[5], temperature)
        location    = dmap(D[6], humidity)
        if ans < 0 or location < ans:
            ans = location
    print("ans", ans)
