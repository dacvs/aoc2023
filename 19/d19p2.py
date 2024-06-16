import numpy as np
import d19

# A *box* is a 4x2 array representing a set 
#     (B00, B01] x (B10, B11] x (B20, B21] x (B30, B31]
# of 4-tuples (x, m, a, s). That is,
#     B00 < x <= B01
#     B10 < m <= B11
#     B20 < a <= B21
#     B30 < s <= B31


def chop(ineq, box):  
    """
    Args:
        ineq: like "x<1000"
    Returns:
        boxT: box (possibly empty), the subset of `box` where inequality is true 
        boxF: box (possibly empty), the subset of `box` where inequality is false
    """
    boxT = np.array(box)
    boxF = np.array(box)
    i = "xmas".index(ineq[0])
    num = int(ineq[2:])
    if ineq[1] == '<':     # as in "x<1000"
        boxT[i][1] = num - 1
        boxF[i][0] = num - 1
    if ineq[1] == '>':     # as in "x>1000"
        boxT[i][0] = num
        boxF[i][1] = num
    return boxT, boxF


D, _ = d19.workflows_ratings("input.txt")
box = np.array(((0, 4000), (0, 4000), (0, 4000), (0, 4000)))  # (c, d], order "xmas"
box_name_ks = [(box, "in", 0)]  # k: index into name's rules
ans = 0
while box_name_ks:
    box, name, k = box_name_ks.pop()

    # Do the action of name's rule k
    if name == "A":
        ans += np.prod(box[:, 1] - box[:, 0])
    elif name != "R":
        rule = D[name][k]  # rule is like "a<2006:qkq" or "rfg"
        if ':' in rule:  # conditional
            ineq, target = rule.split(':')
            boxT, boxF = chop(ineq, box)
            if np.all(boxT[:, 0] < boxT[:, 1]):  # nonempty
                box_name_ks.append((boxT, target, 0))
            if np.all(boxF[:, 0] < boxF[:, 1]):  # nonempty
                box_name_ks.append((boxF, name, k + 1))
        else:  # rule is a name
            box_name_ks.append((box, rule, 0))
print("ans", ans)
