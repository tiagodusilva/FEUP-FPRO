from math import sqrt

def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


#print("-".join(["d", "c", "b", "a", "b", "c", "d"]))
#print("abcd"[::-1])
print(prime(2))
