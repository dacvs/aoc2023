import d22

def removable(A, N, u):
    return all(1 < len(d22.supporters(A, N, v)) for v in d22.supporteds(A, u))

A, N, _ = d22.d22()
ans = 0
for w in range(len(A)):
    if removable(A, N, w):
        ans += 1
    if w % 50 == 0:
        print(f"Removable {w} / {len(A)}")
print("ans", ans)
