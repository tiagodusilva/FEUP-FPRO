def parse(filename):
    with open(filename, "r") as doc:
        string = doc.read().replace(" ", "").replace("\n", " ")
        alist = string.split()

        def createTuple(index=0):
            res = ()
            while (index < len(alist)):
                if alist[index] == "(":
                    aux, index = createTuple(index + 1)
                    res += aux
                elif alist[index] == ")":
                    return (res, ), index + 1
                else:
                    res += (int(alist[index]), )
                    index += 1
            return res

    return createTuple()


#print(parse("tuple3.txt"))
