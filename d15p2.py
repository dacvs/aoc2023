import lib
import d15
box = [[] for i in range(256)]
for s in lib.block("input/15.txt"):
    for w in s.split(','):
        if w[-1] == '-':    # operation '-'
            label = w[:-1]
            i = d15.hash(label)
            box[i] = [pair for pair in box[i] if pair[0] != label]
        else:               # operation '='
            label, foc = w.split('=')
            i = d15.hash(label)
            js = [j for j in range(len(box[i])) if box[i][j][0] == label]
            if js:  # a lens exists with the given label
                box[i][js[0]] = (label, foc)
            else:
                box[i].append((label, foc))
ans = 0
for i in range(256):
    for j, pair in enumerate(box[i]):
        ans += (i + 1) * (j + 1) * int(pair[1])
print("ans", ans)
