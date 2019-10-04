def is_vowel(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return letter.lower() in vowels


def minion(astring):
    #Stuart(vogais)
    stuart_substrings = []
    kevin_substrings = []

    for i in range(0, len(astring)):
        if is_vowel(astring[i]):
            for j in range(i, len(astring)):
                stuart_substrings.append(astring[i:j + 1])
        else:
            for k in range(i, len(astring)):
                kevin_substrings.append(astring[i:k + 1])

    if len(stuart_substrings) > len(kevin_substrings):
        result = stuart_substrings
        winner = "Kevin"
    elif len(stuart_substrings) < len(kevin_substrings):
        result = kevin_substrings
        winner = "Stuart"
    else:
        return "It was a draw!"

    out = "The winner was {0} with a total of {1} points:\n".format(winner, len(result))
    for i in list(sorted(set(result), key=lambda x: (len(x), x))):
        out += "- {0}: {1}\n".format(i, result.count(i))

    return out


#print(minion("ANANAS"))
#print(minion("BANANA"))
print(minion("YMCA"))
