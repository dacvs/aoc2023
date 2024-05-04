import d12
ans = 0
M = {}
for W, G in d12.words_lists("input.txt"):
    W = W + '?' + W + '?' + W + '?' + W + '?' + W
    G *= 5
    ans += d12.N(M, W, G)
print("ans", ans)
