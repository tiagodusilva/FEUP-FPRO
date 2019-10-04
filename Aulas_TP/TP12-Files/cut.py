def cut(filename, delimiter, field):
    with open(filename, "r") as doc:
        result = ""
        for line in doc:
            aux = line.split(delimiter)
            if isinstance(field, int):
                result += str(aux[field - 1]).strip("\n") + "\n"
            else:
                for num in field:
                    result += str(aux[num - 1]) + delimiter
                result = result.strip(delimiter + "\n") + "\n"
    return result


#print(cut("data.csv", ",", 2))
#print(cut("data.csv", ",", [2, 4]))
