with open("input.txt") as f:
    ans = 0
    for s in f:
        d = [c for c in s.strip() if c in "0123456789"]
        ans += int(d[0] + d[-1])
    print("ans", ans)
