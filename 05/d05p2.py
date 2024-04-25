import d05


def map1(dsl, ijs):
    """Returns (done, more) where `more` are subject to later rules"""
    d, s, l = dsl
    done, more = [], []
    for i, j in ijs:
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


S, M = d05.seeds_maps("input.txt")
seeds = [(S[2 * i], S[2 * i] + S[2 * i + 1]) for i in range(len(S) // 2)]
soils           = map_all(M[0], seeds)
fertilizers     = map_all(M[1], soils)
waters          = map_all(M[2], fertilizers)
lights          = map_all(M[3], waters)
temperatures    = map_all(M[4], lights)
humidities      = map_all(M[5], temperatures)
locations       = map_all(M[6], humidities)
ans = min(i for i, j in locations)
print("ans", ans)
