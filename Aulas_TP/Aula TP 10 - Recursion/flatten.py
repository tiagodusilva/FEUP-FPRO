def flatten(alist):
    l1 = []
    if not isinstance(alist, list):
        return alist
    for item in alist:
        if isinstance(item, list):
            l1 += flatten(item)
        else:
            l1 += [item]
    return l1


#print(flatten(['Hello', [2, [[], False]], [True]]))
#print(flatten([[]]))
