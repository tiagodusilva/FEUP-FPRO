from math import sqrt

def is_Prime(n):
        if (n <= 1):
            return False
        i = 2
        while (i <= sqrt(n)):
            if ((n % i) == 0):
                return False
            i += 1
        return True


found_any = False
lower = int(input())
upper = int(input())

for i in range(lower, upper + 1):
    if (is_Prime(i)):
        if not found_any:
            print(i, end="")
            found_any = True
        else:
            print(" " + str(i), end="")

print("\n", end="")
