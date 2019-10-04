def rec_gcd(n1, n2):
    if n2 == 0:
        return n1
    if n1 < n2:
        return rec_gcd(n2, n1)
    return rec_gcd(n2, n1 % n2)


print(rec_gcd(630, 196))
