def isqrt(x):
    """find a pair lo, hi of integers so that lo <= sqrt(x) < hi and lo + 1 == hi"""
    assert 0 <= x
    lo, hi = 0, x + 1
    while lo != hi - 1:
        av = (lo + hi) // 2
        if av * av <= x:
            lo = av
        else:
            hi = av
    return lo, hi

def num_ways(t, d):
    # Let x = holdtime.
    # We are counting integer values of x in interval [0, t) where d < (t - x) * x.
    # That is, where x * x - t * x + d < 0.
    # The left side of the inequality is a quadratic polynomial (in x). The count is
    # floor(R) - ceil(r) + 1 where r and R are the roots of the polynomial, r <= R.
    D = t * t - 4 * d
    if 0 <= D:
        _, q = isqrt(D)
        def f(x): return x * x - t * x + d
        R = (t + q) // 2
        r = (t - q) // 2
        spread = list(range(-4, 5))
        hipool = [R + n for n in spread]
        lopool = [r + n for n in spread]
        hi = [n for n in hipool if f(n) < 0 <= f(n + 1)]
        lo = [n for n in lopool if f(n) < 0 <= f(n - 1)]
        if hi and lo:
            return hi[0] - lo[0] + 1
    return 0

import lib
block = lib.block("input/06.txt")
ts = block[0].split()[1:]
ds = block[1].split()[1:]
t = int(''.join(ts))
d = int(''.join(ds))
print("ans", num_ways(t, d))
