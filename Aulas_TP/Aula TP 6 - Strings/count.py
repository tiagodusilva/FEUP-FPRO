def count(word, phrase):
    word = word.lower()
    phrase = phrase.lower()
    phrase += " "
    aux = ""
    total = 0
    for i in phrase:
        if (i.isalpha()):
            aux += i
        else:
            if (word == aux):
                total += 1
            aux = ""
    return total
