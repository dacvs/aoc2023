def map1(dsl, ijs):  # return (done, more) where `more` are subject to later rules
    d, s, l = dsl
    done, more = [], []
    for ij in ijs:
        i, j = ij

        # interval [i, j) is cut at 2 points, s and s + l
        L0 = i
        r0 = min(j, s)
        L1 = max(i, s)
        r1 = min(j, s + l)
        L2 = max(i, s + l)
        r2 = j

        # discard empty pieces
        if L0 < r0:
            more.append((L0, r0))
        if L1 < r1:
            done.append((L1 - s + d, r1 - s + d))
        if L2 < r2:
            more.append((L2, r2))
    return done, more


def map_all(dsls, ijs):
    out = []
    for dsl in dsls:
        done, ijs = map1(dsl, ijs)
        out += done
    return out + ijs


with open("input.txt") as f:
    D = []
    for s in f:
        if s.startswith("seeds"):
            s = [int(n) for n in s[6:].split()]
            seeds = [(s[2 * i], s[2 * i] + s[2 * i + 1]) for i in range(len(s) // 2)]
        else:
            if s.split():
                if not s[0] in "sfwlth":
                    D[-1].append(tuple(int(n) for n in s.split()))
            else:
                D.append([])

    soils           = map_all(D[0], seeds)
    fertilizers     = map_all(D[1], soils)
    waters          = map_all(D[2], fertilizers)
    lights          = map_all(D[3], waters)
    temperatures    = map_all(D[4], lights)
    humidities      = map_all(D[5], temperatures)
    locations       = map_all(D[6], humidities)
    ans = min(i for i, j in locations)
    print("ans", ans)
