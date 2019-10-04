def longest_word(url):
    import urllib.request
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    url = "https://raw.githubusercontent.com/fpro-admin/recitas/master/words"
    words = urllib.request.urlopen(url).read().decode()
    html = set(html.split())
    print(html)
    words = set(words.split())
    words = words.intersection(html)
    max_len = len(max(words, key=len))
    words = [w for w in words if len(w) == len(w) == max_len]
    words.sort()
    return words[0]


print(longest_word("https://en.wikipedia.org/wiki/Monty_Python"))
#print(longest_word("https://raw.githubusercontent.com/fpro-admin/recitas/master/words"))
