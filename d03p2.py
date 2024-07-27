import d03
D, A, C, Z = d03.digits_array_component_value()
I, J = A.shape
ans = 0
for i in range(I):
    for j in range(J) :
        if A[i, j] == '*':
            components = set(d03.adjacent_components(A, C, i, j))
            if len(components) == 2:
                m, n = [Z[u] for u in components]
                ans += m * n
print("ans", ans)
