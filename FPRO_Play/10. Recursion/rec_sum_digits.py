def rec_sum_digits(n):
    if n == 0:
        return 0
    return n % 10 + rec_sum_digits(n // 10)


print(rec_sum_digits(12))
print(rec_sum_digits(45))
