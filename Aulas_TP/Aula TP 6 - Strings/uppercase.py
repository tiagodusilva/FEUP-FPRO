def uppercase(astring):
    test = astring[0:3].upper()
    for i in range(0, 3):
        if (test[i] == astring[i] and test[i].isalpha()):
            astring = astring.upper()
            break
    return astring
