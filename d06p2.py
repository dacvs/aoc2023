import lib
block = lib.block("input/06.txt")
ts = block[0].split()[1:]
ds = block[1].split()[1:]
t = int(''.join(ts))
d = int(''.join(ds))
ans = 0
for holdtime in range(t):
    dist = (t - holdtime) * holdtime
    if dist > d:
        ans += 1
print("ans", ans)

# Let x = holdtime.
# We are counting integer values of x in interval [0, t) where d < (t - x) * x.
# That is, where x * x - t * x + d < 0.
# The left side of the inequality is a quadratic polynomial (in x). The count is
# floor(R) - ceil(r) + 1 where r and R (with r <= R) are the roots of the polynomial.

if False:
    import math
    D = t * t - 4 * d
    R = (t + math.sqrt(D)) / 2
    r = (t - math.sqrt(D)) / 2
    print("ans", math.floor(R) - math.ceil(r) + 1)
