def unpack_rev(atuple):
    result = ""
    for i in range(len(atuple) - 1, -1, -1):
        result += atuple[i] + " "
    return result.strip()
