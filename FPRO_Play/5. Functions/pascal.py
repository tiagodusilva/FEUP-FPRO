from math import factorial as fac

def pascal(n):
    result = ""
    for i in range(n):
        result = result.strip() + "\n"
        for j in range(0, i + 1):
            result += str(fac(i) // (fac(j) * fac(i - j))) + " "
    return result


#print(pascal(3))
#print(pascal(5))
