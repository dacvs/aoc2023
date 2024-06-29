import lib

def turns_forks():
    blocks = list(lib.blocks("input/08.txt"))
    turns = blocks[0][0]
    forks = {}
    for s in blocks[1]:
        k, L, R, _ = lib.split(s, [" = (", ", ", ")"])
        forks[k] = {'L': L, 'R': R}
    return turns, forks
