from math import sqrt

def solver(a, b, c):
    bd = b**2 - 4 * a * c
    if (bd < 0):
        return []
    else:
        x1 = (-b + sqrt(bd)) / (2 * a)
        x2 = (-b - sqrt(bd)) / (2 * a)
        if (x1 == x2):
            return [x1]
        elif (x1 < x2):
            return [x1, x2]
        else:
            return [x2, x1]
