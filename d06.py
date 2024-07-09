def isqrt(x):
    """
    If x is a nonnegative integer,
    find a pair lo, hi of integers so that lo <= sqrt(x) < hi and lo + 1 == hi.
    """
    assert 0 <= x
    lo, hi = 0, x + 1           # We begin with lo <= sqrt(x) < hi.
    while lo != hi - 1:         # Entering the `while` statement, lo < hi.
        av = (lo + hi) // 2     # av is an integer, lo <= av < hi,
        if av * av <= x:        # and av <= sqrt(x), so av may replace lo,
            lo = av             #     preserving lo <= sqrt(x) < hi.
        else:                   # and sqrt(x) < av, so av may replace hi,
            hi = av             #     preserving lo <= sqrt(x) < hi.
    return lo, hi               # If we reach here (do we?), then lo + 1 == hi.
    # The sequence of lo values (weakly) increases, and
    # the sequence of hi values (weakly) decreases.
    # When we enter the `while` statement with lo < hi - 1, then lo < av < hi,
    # so either lo strictly increases in that step, or hi strictly decreases.
    # Eventually the difference between lo and hi shrinks to 1.
    # Of course, the difference shrinks not just by 1 each time through the loop,
    # but geometrically.

def num_ways(t, d):
    """Number of ways to exceed distance d in time t"""
    # Let x = holdtime.
    # We are counting integer values of x in interval [0, t) where d < (t - x) * x.
    # That is, where x * x - t * x + d < 0.
    # The left side of the inequality is a quadratic polynomial (in x).
    # The count is
    #     floor(R) - ceil(r) + 1
    # where r and R are the roots of the polynomial, r <= R.

    def f(x): return x * x - t * x + d
    D = t * t - 4 * d  # discriminant

    # By the quadratic formula, the roots are:
    #     R = (t + sqrt(D)) / 2
    #     r = (t - sqrt(D)) / 2

    if 0 <= D:
        p, q = isqrt(D)
        # p and q are integers with p <= sqrt(D) < q and p + 1 == q.

        # Find floor(R):
        # t + p <= t + sqrt(D) < t + q
        # (t + p) / 2 <= (t + sqrt(D)) / 2 < (t + q) / 2
        floor_R = (t + p) // 2

        # Find ceil(r):
        # t - q < t - sqrt(D) <= t - p
        # (t - q) / 2 < (t - sqrt(D)) / 2 <= (t - p) / 2
        ceil_r = (t - p + 1) // 2

        if all((
            f(floor_R) < 0 <= f(floor_R + 1),
            f(ceil_r)  < 0 <= f(ceil_r - 1),
        )):
            return floor_R - ceil_r + 1

    return 0
