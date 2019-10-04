def manipulator(l, cmds):
    result = ""
    for orders in cmds:
        cmnd = orders.split()
        if cmnd[0] == "insert":
            l.insert(int(cmnd[1]), int(cmnd[2]))
        elif cmnd[0] == "print":
            result += str(l) + " "
        elif cmnd[0] == "remove":
            l.remove(int(cmnd[1]))
        elif cmnd[0] == "append":
            l.append(int(cmnd[1]))
        elif cmnd[0] == "sort":
            l.sort()
        elif cmnd[0] == "pop":
            del l[-1]
        elif cmnd[0] == "reverse":
            l.reverse()
    return result.strip()
