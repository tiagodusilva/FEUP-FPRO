def adigits(str1, str2, str3):
    a = int(str1)
    b = int(str2)
    c = int(str3)
    if (a >= b and b >= c):
        return int(str1 + str2 + str3)
    elif(a >= c and c >= b):
        return int(str1 + str3 + str2)
    elif(b >= a and a >= c):
        return int(str2 + str1 + str3)
    elif(b >= c and c >= a):
        return int(str2 + str3 + str1)
    elif(c >= a and a >= b):
        return int(str3 + str1 + str2)
    elif(c >= b and b >= a):
        return int(str3 + str2 + str1)
    return 0
