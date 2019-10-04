#10 xer
def longest(s):
    return len(max(s.split(), key=lambda aux: len(aux)))

#-10 xer
def sad_longest(s):
    s += " "
    count = 0
    mx = -1
    for char in s:
        if char.isalpha():
            count += 1
        else:
            if count > mx:
                mx = count
            count = 0
    return mx


#print(longest("A list with some words"))
#print(longest("Unnecessarily long sentence since the longest word is the first one"))
