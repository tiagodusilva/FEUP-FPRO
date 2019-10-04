def anagrams(alist):
    alist.sort(key=lambda element: element.lower())
    result = []
    index = -1
    for i in range(0, len(alist)):
        if alist[i] != "":
            result.append([alist[i]])
            index += 1
            characters = "".join(sorted(alist[i].lower().replace(" ", "")))
            alist[i] = ""
            for j in range(i + 1, len(alist)):
                if characters == "".join(sorted(alist[j].lower().replace(" ", ""))):
                    result[index].append(alist[j])
                    alist[j] = ""
    '''
    for lists in result:
        lists.sort()
    result.sort(key=lambda element: element[0].lower())
    '''
    return result


print(anagrams(["they see", "eat", "The eyes", "car has", "ate", "a crash", "tea"]))
#print(anagrams(["sentence", "lives", "ten scene", "bat", "Elvis", "CE sennet"]))
