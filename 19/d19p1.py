def result(D, name, xmas):  # xmas is a tuple of ratings in categories x, m, a, s
    for rule in D[name]:  # D[name] is like ["a<2006:qkq", "m>2090:A", "rfg"]
        if rule in ["A", "R"]:  # rule is an ultimate outcome
            return rule
        elif 1 < len(rule) and rule[1] in "<>":  # rule is an inequality
            category, op = rule[:2]  # category is e.g. "x" and op is e.g. "<"
            num, target = rule[2:].split(':')
            i = "xmas".find(category)
            if any((
                op == '<' and xmas[i] < int(num),
                op == '>' and xmas[i] > int(num),
            )):
                return target if target in ["A", "R"] else result(D, target, xmas)
        else:  # rule is just a name
            return result(D, rule, xmas)


with open("input.txt") as f:
    D = {}  # name: rules
    ans = 0
    for s in f:
        if s.strip():
            if s[0] == '{':  # s is like "{x=787,m=2655,a=1222,s=2876}\n"
                ts = s[1:-2].split(',')
                xmas = tuple(int(t.split("=")[1]) for t in ts)
                if result(D, "in", xmas) == "A":
                    ans += sum(xmas)
            else:  # s is like "px{a<2006:qkq,m>2090:A,rfg}\n"
                name, right = s.split('{')
                rules, _ = right.split('}')
                D[name] = rules.split(',')
    print("ans", ans)

