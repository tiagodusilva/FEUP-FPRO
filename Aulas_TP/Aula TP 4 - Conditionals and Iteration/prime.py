import math

def is_Prime(n):
    if (n <= 1):
        return False

    i = 2
    while (i < math.sqrt(n)):
        if ((n % i) == 0):
            return False
        i += 1

    return True


n = int(input())

result = is_Prime(n)
