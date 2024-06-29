import lib
matches = [-1]
for s in lib.block("input/04.txt"):
    _, winning, have = lib.split(s, [":", "|"])
    winning = set(winning.split())
    have = set(have.split())
    matches.append(len(winning & have))
copies = [1 for _ in matches]
for i in range(1, len(matches)):
    for j in range(i + 1, i + 1 + matches[i]):
        copies[j] += copies[i]
print("ans", sum(copies[1:]))
