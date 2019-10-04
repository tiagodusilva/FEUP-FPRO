def translate(astring, table):
    result = ""
    for char in astring:
        found = False
        for item in table:
            if (char == item[0]):
                result += str(item[1])
                found = True
                break
        if not found:
            result += char
    return result
