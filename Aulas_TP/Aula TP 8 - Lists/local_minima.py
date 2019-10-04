def local_minima(alist, n):
    n = n // 2
    result = []
    aux = [0 for i in range(len(alist))]
    for i in range(len(alist)):
        flag = 999999
        for j in range(i - n, i + n + 1):
            if (j >= 0 and j < len(alist)):
                if alist[j] < alist[i]:
                    flag = -1
                    break
                elif alist[i] == alist[j] and aux[j] == 1 and j < i and j < flag:
                    flag = j
        if flag == 999999:
            if not((alist[i], i) in result):
                result.append((alist[i], i))
                aux[i] = 1
        elif flag != -1:
            if not((alist[i], flag) in result):
                result.append((alist[i], flag))
    return result


#print(local_minima([10, 3, 3, 14, 5, 7, 4], 3))
#print(local_minima([0, 3, 3, 14, 5, 7, 4], 3))
#print(local_minima([2, 1, 1, 1, 7, 3, 1], 5))
