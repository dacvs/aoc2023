import d22

A, N, V = d22.d22("input/22.txt")
bottom = set(u for u in V if not d22.supporters(A, N, u))

ans = 0
for i, u in enumerate(V):
    # remove u and then all unsupported bricks above
    if i % 50 == 0:
        print(f"Remove {i} / {len(V)} u={u}")
    gone = set([u])
    for v in V[i + 1:]:
        if not v in bottom:
            if not d22.supporters(A, N, v) - gone:
                gone |= set([v])
    ans += len(gone) - 1
print("ans", ans)
