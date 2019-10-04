def wc(filename):
    with open(filename, "r") as doc:
        aux = doc.readlines()
        if aux[-1][-1] == "\n":
            result = (len(aux) + 1, )
        else:
            result = (len(aux), )
        doc.seek(0)
        aux = doc.read()
    return result + (len(aux.split()), len(aux))


#print(wc("testFile.txt"))
