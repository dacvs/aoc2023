import numpy as np
import lib

def graph_start():
    """
    From the problem statement, there is an obvious way to formulate a grid graph of
    which the pipe loop is a subgraph, so that each cell of the input array is a vertex.
    However, when it comes to computing area in part 2, this formulation is too "thin."
    The interior of the loop is disconnected. In response, we double the vertices in each
    direction (horizontal, vertical) so that e.g.

        . . . . . 
        . F - 7 .
        . | . | .
        . L - J .
        . . . . .

    is represented as:
 
        . . . . . . . . . . .

        . * . * . * . * . * . 
               
        . . . . . . . . . . .
        
        . * . *-.-*-.-* . * .
              |       |
        . . . . . . . . . . .
              |       |
        . * . * . * . * . * .
              |       |
        . . . . . . . . . . .
              |       |
        . * . *-.-*-.-* . * .

        . . . . . . . . . . .
        
        . * . * . * . * . * .

        . . . . . . . . . . .


    Vertices of the new graph are numbered so that the center each cell of the input array
    is an odd-odd pair (as a vertex of the new graph).
    """
    A = np.array([list(s) for s in lib.block("input/10.txt")])
    I, J = A.shape

    # Convert A to graph whose vertex set is [0, 1, ..., 2*I] x [0, 1, ..., 2*J]
    N = {(a, b): set() for a in range(2 * I + 1) for b in range(2 * J + 1)}
    for i in range(I):
        for j in range(J):
            a = 2 * i + 1
            b = 2 * j + 1
            N[(a, b)] = set()
            if A[i, j] == 'F': N[(a, b)] = set([(a + 1, b), (a, b + 1)])
            if A[i, j] == '7': N[(a, b)] = set([(a + 1, b), (a, b - 1)])
            if A[i, j] == 'J': N[(a, b)] = set([(a - 1, b), (a, b - 1)])
            if A[i, j] == 'L': N[(a, b)] = set([(a - 1, b), (a, b + 1)])
            if A[i, j] == '|': N[(a, b)] = set([(a + 1, b), (a - 1, b)])
            if A[i, j] == '-': N[(a, b)] = set([(a, b + 1), (a, b - 1)])
            if A[i, j] == 'S': N[(a, b)] = set([(a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)])
    lib.symmetrize(N)

    # find starting node S and remove pendant edges incident to S
    S = [(2 * i + 1, 2 * j + 1) for i in range(I) for j in range(J) if A[i, j] == 'S'][0]
    for u in N[S]:
        if len(N[u]) == 1:
            N[u] = set()
            N[S] = N[S] - set([u])

    return I, J, N, S
