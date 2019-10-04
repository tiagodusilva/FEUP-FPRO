def isomorphic(astring1, astring2):
    dic = dict()
    for i in range(len(astring1)):
        if astring1[i] in dic:
            if astring2[i] != dic[astring1[i]]:
                return "'" + astring1 + "' and '" + astring2 + "' are not isomorphic"
        else:
            for key in dic:
                if astring2[i] == dic[key]:
                    return "'" + astring1 + "' and '" + astring2 + "' are not isomorphic"
            dic[astring1[i]] = astring2[i]
    result = []
    for key in dic:
        result.append((key, dic[key]))
    return "'" + astring1 + "' and '" + astring2 + "' are isomorphic because we can map: " + str(result)


#print(isomorphic('ab', 'aa'))
#print(isomorphic('paper', 'title'))
#print(isomorphic('foo', 'bar'))
#print(isomorphic('turtle', 'tletur'))
