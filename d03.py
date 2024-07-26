import numpy as np
import lib

D = "0123456789"

def digits_array_component_value():
    A = np.array([list(s) for s in lib.block("input/03.txt")])
    I, J = A.shape
    C = {}  # component
    Z = {(i, j): 0 for i in range(I) for j in range(J)}  # numeric value of component
    for i in range(I):
        for j in range(J):
            if A[i, j] in D:
                C[i, j] = C[i, j - 1] if (i, j - 1) in C else (i, j)
                Z[C[i, j]] = 10 * Z[C[i, j]] + int(A[i, j])
    return D, A, C, Z

def adjacent_components(A, C, i0, j0):  # assuming A[i0, j0] is a symbol
    for i in (i0 - 1, i0, i0 + 1):
        for j in (j0 - 1, j0, j0 + 1):
            if A[i, j] in D:
                yield C[i, j]
