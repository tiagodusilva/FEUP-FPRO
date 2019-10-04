def rotate_list(l):
    if len(l) == 3:
        return l
    aux = [0 for i in range(len(l))]
    for i in range(len(l) - 3):
        aux[i] = l[i + 3]
    print(i)
    i += 1
    aux[i] = l[0]
    i += 1
    aux[i] = l[1]
    i += 1
    aux[i] = l[2]
    return aux


#print(rotate_list([1, 2, 3, 4, 5, 6]))
#print(rotate_list([5, 20, 21, 0, -1, 3]))
#print(rotate_list([1, 2, 3, 4]))
