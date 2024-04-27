def turns_forks(filename):
    """Read Day 8 input file"""
    with open("input.txt") as f:
        F = {}
        for i, s in enumerate(f):
            if i == 0:
                T = s.strip()
            if 1 < i:
                k = s[0:3]
                L = s[7:10]
                R = s[12:15]
                F[k] = {'L': L, 'R': R}
    return T, F
