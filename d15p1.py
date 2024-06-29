import lib
import d15
ans = 0
for s in lib.block("input/15.txt"):
    for w in s.split(','):
        ans += d15.hash(w)
print("ans", ans)
