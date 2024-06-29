import lib

def seeds_maps():
    """
    Returns (seeds, maps) where:
        seeds is a list of integer seed values
        maps is a list M[0], ..., M[6], each a list of 3-tuple of int
    """ 
    blocks = list(lib.blocks("input/05.txt"))
    seeds = [int(n) for n in blocks[0][0].split()[1:]]
    maps = []
    for block in blocks[1:]:
        maps.append([])
        for s in block[1:]:
            maps[-1].append(tuple(int(n) for n in s.split()))
    return seeds, maps
