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


def is_orthogonal(mx):
    t = [[0 for i in range(len(mx[0]))] for j in range(len(mx))]

    for i in range(len(mx)):
        for j in range(len(mx[0])):
            t[i][j] = mx[j][i]

    t = mult(mx, t).copy()

    for i in range(len(mx)):
        for j in range(len(mx[0])):
            if i == j:
                if t[i][j] != 1:
                    return False
            elif t[i][j] != 0:
                return False

    return True


#print(is_orthogonal([[-1, 0], [0, 1]]))
#print(is_orthogonal([[-2, 3], [4, -1]]))
