def palindrome_index(s):
    if s == s[::-1]:
        return -1
    for i in range(len(s)):
        aux = s[0:i] + s[i + 1:len(s)]
        if aux == aux[::-1]:
            return i
    return -1


#print(palindrome_index("aaab"))
#print(palindrome_index("tattarrattat"))
