import d08
T, F = d08.turns_forks("input.txt")
k = "AAA"
i = 0
while k != "ZZZ":
    k = F[k][T[i % len(T)]]
    i += 1
print("ans", i)
