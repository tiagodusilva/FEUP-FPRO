def mult(m, n):
    lines = len(m)
    columns = len(n[0])
    elements = len(m[0])
    if len(m[0]) != len(n):
        return []
    else:
        result = [[0 for i in range(columns)] for j in range(lines)]
        for i in range(lines):
            for j in range(columns):
                for k in range(elements):
                    result[i][j] += m[i][k] * n[k][j]
    return result


print(mult([[1, 2], [3, 4]], [[2, 0], [1, 2]]))
