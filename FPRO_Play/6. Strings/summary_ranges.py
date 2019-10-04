def summary_ranges(astring):
    astring += ",-1"

    aux = astring.split(sep=",")
    for i in range(len(aux)):
        aux[i] = int(aux[i])

    result = str(aux[0])

    for i in range(1, len(aux)):
        if aux[i] == aux[i - 1] + 1:
            if result[len(result) - 1] != ">":
                result += "->"
        elif result[len(result) - 1] == ">":
            result += str(aux[i - 1]) + "," + str(aux[i])
        else:
            result += "," + str(aux[i])

    return result[0:len(result) - 3]


#print(summary_ranges("0,2,4,6"))
#print(summary_ranges("0,1,2,3,4,5,7,10,11,20,21"))
#print(summary_ranges("1,3,4,6,7,9,10"))
