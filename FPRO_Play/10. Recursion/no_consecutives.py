def no_consecutives1(k):
    def actual_rec(n, dig):
        if n == 0:
            return 1
        if dig == 0:
            return actual_rec(n - 1, 0) + actual_rec(n - 1, 1)
        return actual_rec(n - 1, 0)
    return actual_rec(k, 0)


print(no_consecutives1(3))
print(no_consecutives1(4))
