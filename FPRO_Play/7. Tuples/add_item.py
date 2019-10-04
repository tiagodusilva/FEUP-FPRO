def add_item(tup, idx, item):
    if idx == 0:
        result = (item, )
        for i in range(1, len(tup)):
            result += (tup[i], )
        return result

    if idx == len(tup) - 1:
        result = ()
        for i in range(len(tup) - 1):
            result += (tup[i], )
        result += (item, )
        return result

    result = ()
    found = False
    for i in range(len(tup) + 1):
        if not found:
            if idx == i:
                found = True
                result += (item, )
            else:
                result += (tup[i], )
        else:
            result += (tup[i - 1], )

    return result


#print(add_item((1, 2, 3), 1, [4, 5]))
#print(add_item(("a", 2, "c"), 2, "new item"))
