import d22

def removable(A, N2, u):
    return all(1 < len(d22.supporters(A, N2, v)) for v in d22.supporteds(A, N2, u))

A, N2, _ = d22.array_nbhds2D_vertices()
print("ans", sum(1 for w in range(len(A)) if removable(A, N2, w)))
