def rangoli(n):
    letters = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in range(0, n - 1):  # Top half
        result += ("--" * (n - i - 1)) + "-".join(letters[n - 1:n - 2 - i:-1] + letters[n - i:n]) + ("--" * (n - i - 1)) + "\n"

    result += "-".join(letters[n - 1:0:-1] + letters[0:n])  # Middle line

    for i in range(n - 2, -1, -1):  # Bottom half
        result += "\n" + ("--" * (n - i - 1)) + "-".join(letters[n - 1:n - 2 - i:-1] + letters[n - i:n]) + ("--" * (n - i - 1))
    return result


print(rangoli(26))
#print(rangoli(3))
