#Permutation a'la JLopes
def permuta(alist, step=0):
    if step == len(alist) - 1:
        return [alist]
    result = []
    aux = alist[step]
    for i in range(step, len(alist)):
        alist[step], alist[i] = alist[i], aux
        result += permuta(alist.copy(), step + 1)
        alist[i] = alist[step]
    return result

#Good'ol Permutations :(
"""def permuta(alist):
    if len(alist) == 1:
        return [alist]
    result = []
    for item in alist:
        aux = permuta(list(filter(lambda x: x != item, alist)))
        for anotherItem in aux:
            result.append([item] + anotherItem)
    return result
"""

print(permuta(['A', 'B', 'C']))
