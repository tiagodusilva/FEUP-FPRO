def get_positions(word_list, sentence):
    words = sentence.split()
    for i in range(len(word_list)):
        if (words[0] == word_list[i]):
            word_list[i] = ''
            break
    for j in range(len(word_list)):
        if (words[1] == word_list[j]):
            break
    return str(i) + " " + str(j)
