import d12
ans = 0
M = {}
for W, G in d12.words_lists():
    ans += d12.N(M, W, G)
print("ans", ans)
