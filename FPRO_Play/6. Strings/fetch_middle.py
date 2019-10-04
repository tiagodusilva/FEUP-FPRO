def fetch_middle(lists):
    result = []
    for l in lists:
        size = len(l)
        if size % 2 == 0:
            result.append((l[(size // 2) - 1] + l[(size // 2)]) / 2.0)
        else:
            result.append(l[size // 2])
    return result


#print(fetch_middle([[1,2,3],[4,5,6],[7,8,9,10]]))
#print(fetch_middle([[10,25,35,45],[100,-1,3,4],[-3,-5,-10,-20,-100]]))
