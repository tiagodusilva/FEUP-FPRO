def count_elems(tup):
    result = ()
    for item in tup:
        if isinstance(item, str) or isinstance(item, list) or isinstance(item, tuple):
            result += (len(item), )
        else:
            result += (1, )
    return result


#print(count_elems((1,'234', 3, 4.0, (5j,))))
#print(count_elems(('12',2,(3, 4), [4.0, 'str', 'str2'], 5j)))
