import numpy as np
import lib

def cartesian():
    """
    A is the input file as a matrix.
    Let C be a "cartesian" version of A, implemented as a dict.
    Cell (x, y) = (0, 0) is the center of the map, so C[0, 0] == 'S'.
    In the usual cartesian way, x increases rightward (like j),
    and y increases upward (unlike i).
    Let R be the map radius.
    That is, A is (2 * R + 1, 2 * R + 1)-shaped, and the keys of C are those (x, y) with
        -R <= x <= +R and
        -R <= y <= +R.
    Returns C, R. 
    """
    A = np.array([list(s) for s in lib.block("input/21.txt")])
    I, J = A.shape
    assert I == J
    assert I % 2 == 1
    R = I // 2
    C = {}
    for i in range(I):
        for j in range(J):
            x = j - R  # coords 0 at center ...
            y = R - i  # ... and flip from matrix coords to cartesian convention
            C[x, y] = A[i, j]
    assert C[0, 0] == 'S'
    return C, R

def nbhd(C, R, x0, y0):
    N = [
        (x0 - 1, y0),
        (x0 + 1, y0),
        (x0, y0 - 1),
        (x0, y0 + 1)]
    return [(x, y) for (x, y) in N if -R <= x <= +R and -R <= y <= +R and C[x, y] != '#']
