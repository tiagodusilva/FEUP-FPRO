def academy_awards(alist):
    dic = dict()
    for atuple in alist:
        if atuple[1] not in dic:
            dic[atuple[1]] = 1
        else:
            dic[atuple[1]] += 1
    return dic
