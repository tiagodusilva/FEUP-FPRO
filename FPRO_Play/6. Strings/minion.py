def sort_order(element):
    return len(element[0]), element[0]

def minion(s):
    #stuart -> consoantes
    #kevin -> vogais
    vowels = ["A", "E", "I", "O", "U"]
    stuart = 0
    kevin = 0
    for i in range(len(s)):
        if s[i] in vowels:
            kevin += len(s) - i
        else:
            stuart += len(s) - i

    if kevin == stuart:
        return "It was a draw!"

    if kevin > stuart:
        result = "The winner was Kevin with a total of " + str(kevin) + " points:\n"
    else:
        result = "The winner was Stuart with a total of " + str(stuart) + " points:\n"

    substrings = []
    if kevin > stuart:
        for i in range(len(s)):
            if s[i] in vowels:
                for j in range(i + 1, len(s) + 1):
                    for k in range(len(substrings)):
                        if s[i:j] == substrings[k][0]:
                            substrings[k][1] += 1
                            break
                    else:
                        substrings.append([s[i:j], 1])
    else:
        for i in range(len(s)):
            if s[i] not in vowels:
                for j in range(i + 1, len(s) + 1):
                    for k in range(len(substrings)):
                        if s[i:j] == substrings[k][0]:
                            substrings[k][1] += 1
                            break
                    else:
                        substrings.append([s[i:j], 1])

    substrings.sort(key=sort_order)

    for item in substrings:
        result += "- " + item[0] + ": " + str(item[1]) + "\n"

    return result.strip("\n")


#print(minion("ANANAS"))
#print(minion("BANANA"))
