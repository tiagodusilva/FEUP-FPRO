def is_perfect(n):
    n_Sum = 0
    for i in range(1, n):
        if (n % i == 0):
            n_Sum += i
    if (n == n_Sum):
        return True
    else:
        return False
