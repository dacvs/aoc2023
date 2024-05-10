import d15
with open("input.txt") as f:
    ans = 0
    for s in f:
        for w in s.strip().split(','):
            ans += d15.hash(w)
    print("ans", ans)
