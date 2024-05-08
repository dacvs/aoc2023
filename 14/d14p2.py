import numpy as np


def tilt_north(A):
    I, J = A.shape
    for j in range(J):
        i0 = 0                          # interval [i0, i1) free of rocks
        while i0 < I:
            while i0 < I and A[i0, j] == '#':
                i0 += 1
            i1 = i0
            n = 0
            while i1 < I and A[i1, j] != '#':
                if A[i1, j] == 'O':
                    n += 1              # count n rocks...
                    A[i1, j] = '.'      # ...blanking out the interval
                i1 += 1
            A[i0 : i0 + n, j] = 'O'     # place n rocks
            i0 = i1
    return A


def one_cycle(A):
    for k in range(4):
        tilt_north(A)
        A = np.fliplr(A.T)  # rotate 90 degrees clockwise
    return A


def northload(A):
    I, J = A.shape
    n = 0
    for j in range(J):
        for i in range(I):
            if A[i, j] == 'O':
                n += I - i
    return n


def to_string(A):
    return ''.join(A.reshape(-1))


with open("input.txt") as f:
    A = np.array([list(s.strip()) for s in f])
    string_cycles = {to_string(A): 0} 
    nloads = [northload(A)]
    k = 0
    while True:
        k += 1
        print("load", northload(A))
        A = one_cycle(A)
        s = to_string(A)
        if s in string_cycles:
            k0 = string_cycles[s]
            N = 10**9
            print()
            print(f"A after k={k} cycles is same as after {k0} cycles (period={k - k0})")
            print(f"After N={N} cycles, north load is:")
            print("ans", nloads[k0 + (N - k0) % (k - k0)])
            break
        string_cycles[s] = k
        nloads.append(northload(A))
