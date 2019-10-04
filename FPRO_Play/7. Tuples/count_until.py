def count_until(tup):
    i = -1
    for item in tup:
        i += 1
        if isinstance(item, tuple):
            break
    else:
        return -1
    return i


#print(count_until((1,'2', 3, 4.0, 5j)))
#print(count_until((1,2,(3,), 4.0, 5j)))
