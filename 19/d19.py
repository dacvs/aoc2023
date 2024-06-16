def workflows_ratings(filename):
    D = {}  # name: rules
    X = []  # each entry is a 4-tuple `xmas`
    with open(filename) as f:
        for s in f:
            if s.strip():
                if s[0] == '{':  # s is like "{x=787,m=2655,a=1222,s=2876}\n"
                    ts = s[1:-2].split(',')
                    xmas = tuple(int(t.split("=")[1]) for t in ts)
                    X.append(xmas)
                else:  # s is like "px{a<2006:qkq,m>2090:A,rfg}\n"
                    name, right = s.split('{')
                    rules, _ = right.split('}')
                    D[name] = rules.split(',')
    return D, X
