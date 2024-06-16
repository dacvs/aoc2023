def seeds_maps(filename):
    """
    Returns (seeds, maps) where:
        seeds is a list of integer seed values
        maps is a list D[0], ..., D[6], each a list of 3-tuple of int
    """ 
    with open(filename) as f:
        maps = []
        for s in f:
            if s.startswith("seeds"):
                seeds = [int(n) for n in s[6:].split()]
            else:
                if s.split():
                    if not s[0] in "sfwlth":
                        maps[-1].append(tuple(int(n) for n in s.split()))
                else:
                    maps.append([])
    return seeds, maps
