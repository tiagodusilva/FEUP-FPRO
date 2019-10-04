def summary(text):
    aux = text.split()
    numberE = 0
    for word in aux:
        if "e" in word or "E" in word:
            numberE += 1
    return (len(aux), numberE)
