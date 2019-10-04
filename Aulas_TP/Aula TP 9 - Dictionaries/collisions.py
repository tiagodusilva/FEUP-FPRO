def collisions(alist):
    result = dict()
    for item in alist:
        aux = str(item)
        mod8 = 0
        for char in aux:
            mod8 += int(char)
        mod8 = mod8 % 8
        if mod8 in result:
            result[mod8] += 1
        else:
            result[mod8] = 1
    return result


#print(collisions([24, 42]))
#print(collisions([1, 789, 100, 9807, 1208, 92, 101]))
