def formal(name):
    new_string = ""
    for i in range(len(name) - 1, -1, -1):
        if (name[i] >= "A" and name[i] <= "Z"):
            break

    for j in range(i, len(name)):
        new_string += name[j]
    new_string += ","

    for j in range(0, i):
        if (name[j] >= "A" and name[j] <= "Z"):
            new_string += " " + name[j] + "."
    return new_string
