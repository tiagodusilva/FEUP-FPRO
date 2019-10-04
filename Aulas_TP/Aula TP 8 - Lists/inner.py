def inner(u, v):
    total = 0
    for i in range(len(u)):
        total += u[i] * v[i]
    return total
