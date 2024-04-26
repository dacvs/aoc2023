def beg_end_val(s):
    """places in `s` where a number word begins and ends, and its numeric value"""
    words = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
    for i in range(len(s)):
        for k, word in enumerate(words):
            if s[i : i + len(word)] == word:
                yield i, i + len(word) - 1, k


with open("input.txt") as f:
    ans = 0
    for s in f:
        d = [(i, int(c)) for i, c in enumerate(s.strip()) if c in "0123456789"]
        _, m = min(d + list((i, k) for i, _, k in beg_end_val(s)))
        _, n = max(d + list((j, k) for _, j, k in beg_end_val(s))) 
        ans += 10 * m + n
    print("ans", ans)
