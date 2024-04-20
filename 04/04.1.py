with open("input.txt") as f:
    ans = 0
    for s in f:
        _, s = s.split(':')
        winning, have = s.split('|')
        winning = set(winning.split())
        have = set(have.split())
        k = len(winning & have)
        if k:
            ans += 2 ** (k - 1)
    print("ans", ans)
