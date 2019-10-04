def discard_middle(s):
    if len(s) <= 3:
        return ""
    return s[0:2] + s[len(s) - 2:len(s)]


print(discard_middle("string"))
print(discard_middle("n"))
