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


def d13(filename, num_mismatches):
    with open(filename) as f:
        ans = 0
        pattern = []
        for s in f:
            if s.strip():
                pattern.append(s.strip())
            else:
                P = np.array([list(p) for p in pattern])
                ans += 100 * summarize(P, num_mismatches) + summarize(P.T, num_mismatches)
                pattern = []
        print("ans", ans)    
