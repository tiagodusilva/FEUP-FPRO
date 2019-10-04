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
        for i in range(1, len(s) + 1):
            for j in range(0, len(s) - i + 1):
                if s[j] in vowels:
                    for k in range(len(substrings)):
                        if s[j:j + i] == substrings[k][0]:
                            substrings[k][1] += 1
                            break
                    else:
                        substrings.append([s[j:j + i], 1])
    else:
        for i in range(1, len(s) + 1):
            for j in range(0, len(s) - i + 1):
                if s[j] not in vowels:
                    for k in range(len(substrings)):
                        if s[j:j + i] == substrings[k][0]:
                            substrings[k][1] += 1
                            break
                    else:
                        substrings.append([s[j:j + i], 1])

    for item in substrings:
        result += "- " + item[0] + ": " + str(item[1]) + "\n"

    return result.strip("\n")


print(minion("ANANAS"))
#print(minion("BANANA"))
