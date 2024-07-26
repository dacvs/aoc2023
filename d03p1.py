import d03
D, A, C, Z = d03.digits_array_component_value()
I, J = A.shape
components = set()
for i in range(I):
    for j in range(J) :
        if not A[i, j] in D + ".":
            components |= set(d03.adjacent_components(A, C, i, j))
print("ans", sum(Z[u] for u in components))
