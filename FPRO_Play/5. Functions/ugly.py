from math import sqrt

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def ugly(n):
    hasPrimeFactor = False
    if n == 1 or n == 2 or n == 3 or n == 5:
        return True
    for i in range(n // 2, 1, -1):
        if prime(i):
            if n % i == 0:
                if i != 2 and i != 3 and i != 5:
                    return False
                else:
                    hasPrimeFactor = True
    if hasPrimeFactor:
        return True
    else:
        return False


for i in range(50):
    print(str(i) + " " + str(ugly(i)))
