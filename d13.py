import lib
import numpy as np

def summarize(P, num_mismatches):
    n = 0
    for i in range(1, len(P)):
        r = min(i, len(P) - i)
        upper = P[:i][-r:]
        lower = P[i:][:+r]
        mismatch = np.flipud(upper) != lower
        if num_mismatches == np.sum(mismatch.astype(int)):
            n += i
    return n

def d13(num_mismatches):
    ans = 0
    for block in lib.blocks("input/13.txt"):
        P = np.array([list(p) for p in block])
        ans += 100 * summarize(P, num_mismatches) + summarize(P.T, num_mismatches)
    print("ans", ans)    
