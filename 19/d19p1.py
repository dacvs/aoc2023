import d19


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


D, X = d19.workflows_ratings("input.txt")
ans = 0
for xmas in X:
    if result(D, "in", xmas) == "A":
        ans += sum(xmas)
print("ans", ans)
