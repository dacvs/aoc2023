import d22
A, N2, V = d22.array_nbhds2D_vertices()
bottom = set(v for v in V if not d22.supporters(A, N2, v))
ans = 0
for i, u in enumerate(V):
    # remove u and then all unsupported bricks above
    if i % 100 == 0:
        print(f"Remove {i} / {len(V)}")
    gone = set([u])
    for v in V[i + 1:]:
        if not v in bottom:
            if not d22.supporters(A, N2, v) - gone:
                gone |= set([v])
    ans += len(gone) - 1
print("ans", ans)
