def pattern_hunting(l1, l2, p):
    result = []
    for i in range(len(l1)):
        if p in l2[i]:
            result.append(l1[i])
        if p in l1[i]:
            result.append(l2[i])
    result.sort(reverse=True)
    return result
