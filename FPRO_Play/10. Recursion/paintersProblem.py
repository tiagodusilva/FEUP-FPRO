def paint(n, boards):
    if n == 1:
        return max(boards)
    minNum = 9999999999
    for i in range(0, len(boards) + 1 - n):
        aux = paint(n - 1, boards[i + 1:].copy()) + max(boards[:i + 1])
        if aux < minNum:
            minNum = aux
    return minNum


print(paint(2, [60, 70, 10, 20, 40, 50, 10, 40]))
print(paint(3, [60, 70, 10, 20, 40, 50, 10, 40]))
