with open("input.txt") as f:
    _, ts = f.readline().split(':')
    t = int(''.join(ts.split()))

    _, ds = f.readline().split(':')
    d = int(''.join(ds.split()))

    ans = 0
    for holdtime in range(t):
        dist = (t - holdtime) * holdtime
        if dist > d:
            ans += 1
    print("ans", ans)
