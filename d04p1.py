import lib
ans = 0
for s in lib.block("input/04.txt"):
    _, winning, have = lib.split(s, [":", "|"])
    winning = set(winning.split())
    have = set(have.split())
    k = len(winning & have)
    if k:
        ans += 2 ** (k - 1)
print("ans", ans)

