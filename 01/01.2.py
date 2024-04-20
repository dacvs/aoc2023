def beg_end_val(s):
    w = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    for i in range(len(s)):
        for k, t in enumerate(w):
            if s[i : i + len(t)] == t:
                yield i, i + len(t) - 1, k


with open("input.txt") as f:
    ans = 0
    for s in f:
        s = s.strip()
        d = [(i, int(c)) for i, c in enumerate(s) if c in "0123456789"]
        _, m = min(d + list((i, k) for i, _, k in beg_end_val(s)))
        _, n = max(d + list((j, k) for _, j, k in beg_end_val(s))) 
        ans += 10 * m + n
    print("ans", ans)
