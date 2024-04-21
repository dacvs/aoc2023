with open("input.txt") as f:
    _, ts = f.readline().split(':')
    ts = [int(t) for t in ts.split()]

    _, ds = f.readline().split(':')
    ds = [int(d) for d in ds.split()]
    
    ans = 1
    for i, t in enumerate(ts):
        winners = 0
        for holdtime in range(t):
            dist = (t - holdtime) * holdtime
            if dist > ds[i]:
                winners += 1
        ans *= winners
    print("ans", ans)
