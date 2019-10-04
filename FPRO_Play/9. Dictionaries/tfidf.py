from math import log

def tfidf(documents):
    dic = dict()
    totalDoc = len(documents)
    for i in range(totalDoc):
        words = documents[i].split()
        for word in words:
            if word.lower() not in dic:
                dic[word.lower()] = [0 for k in range(len(documents))]
                dic[word.lower()][i] += 1
            else:
                dic[word.lower()][i] += 1

    for key in dic:
        appearences = 0
        for i in range(totalDoc):
            if dic[key][i] != 0:
                appearences += 1
        print(key, appearences)
        for i in range(totalDoc):
            dic[key][i] = round(dic[key][i] * log(totalDoc / appearences), 3)

    return dic


#print(tfidf(["To be or not to be", "Impossible is a word to be found only in the dictionary of fools", "There is nothing impossible to him who will try"]))
