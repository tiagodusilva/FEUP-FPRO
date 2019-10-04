def sort_by_field(filename, field):
    with open(filename, "r") as doc:
        aux = doc.readlines()
        #Getting list ready to sort
        for i in range(len(aux)):
            aux[i] = aux[i].split(",")
            aux[i][-1] = aux[i][-1].strip("\n")
        #List ready, finding collumn to sort by
        index = aux[0].index(field)
        aux = [aux[0]] + sorted(aux[1:], key=lambda x: x[index])
        #List sorted, reinserting \n and formatting string
        res = ""
        for i in range(len(aux)):
            for item in aux[i]:
                res += item + ","
            res = res.strip(",") + "\n"
    return res


#sort_by_field("emails.txt", "surname")
#print(sort_by_field("emails.txt", "surname"))
