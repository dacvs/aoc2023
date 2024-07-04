import lib

def workflows_ratings():
    D = {}  # name: rules
    X = []  # each entry is a 4-tuple `xmas`
    blocks = list(lib.blocks("input/19.txt"))
    for s in blocks[0]:  # s is like "px{a<2006:qkq,m>2090:A,rfg}"
        name, rules, _ = lib.split(s, ["{", "}"])
        D[name] = rules.split(',')
    for s in blocks[1]:  # s is like "{x=787,m=2655,a=1222,s=2876}"
        ts = s[1:-1].split(',')
        xmas = tuple(int(t.split("=")[1]) for t in ts)
        X.append(xmas)
    return D, X
