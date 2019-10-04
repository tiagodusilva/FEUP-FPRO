def median(alist):
    alist.sort()
    if len(alist) % 2 == 1:
        return alist[len(alist) // 2]
    return (alist[len(alist) // 2] + alist[(len(alist) // 2) - 1]) / 2

def batch_norm(alist, batch_size):
    i = 0
    temp = []
    while i < len(alist):
        temp.append(alist[i])
        if (i + 1) % batch_size == 0 or i + 1 == len(alist):
            med = median(temp.copy())
            yield list(map(lambda x: x - med, temp))
            temp = []
        i += 1


#print(list(batch_norm([-1, 0, 1, 1, 2, 4], 3)))
#print(list(batch_norm([10, 1, -12, 5, 1, 3, 7, 3, 3], 5)))
