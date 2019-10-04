def palindrome(astring):
    count = 0
    for i in range(0, len(astring)):
        for j in range(i + 1, len(astring)):
            a = astring[i:j + 1]
            b = ""
            for k in range(len(a) - 1, -1, -1):
                b += a[k]
            if (a == b):
                count += 1
    output = "For string '" + astring + "': " + str(count) + " palindrome substrings"
    return output
