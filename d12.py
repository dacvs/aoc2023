import lib

def words_lists():
    for s in lib.block("input/12.txt"):
        W, G = s.split()
        G = tuple(int(t) for t in G.split(','))
        yield W, G

def fits_at_end(W, k):  # can a spring group of length k>0 go at the end of W?
    return k <= len(W) and (not '.' in W[-k:]) and (k == len(W) or W[-k-1] != '#')

def N(M, W, G):
    """The number N of arrangements in word W of spring groups whose sizes are in G"""
    if not G:
        return 0 if '#' in W else 1
    if not W:
        return 0
    if (W, G) in M:
        return M[W, G]
    n = 0
    if W[-1] != '#':
        n += N(M, W[:-1], G)
    if fits_at_end(W, G[-1]):
        k = max(0, len(W) - G[-1] - 1)
        n += N(M, W[:k], G[:-1])
    M[W, G] = n
    return n
