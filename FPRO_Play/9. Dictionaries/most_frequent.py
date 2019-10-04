def most_frequent(alist):
    dic = dict()
    alist.sort()
    for item in alist:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1

    maximum = -1
    for key, value in dic.items():
        if value > maximum:
            maximum = value
            num = key
        elif value == maximum and num < key:
            num = key

    return num


#print(most_frequent([-1, 2, 5, -1, 3, 3, 3, 4, 4, 2, 4, 5, -1, -1]))
