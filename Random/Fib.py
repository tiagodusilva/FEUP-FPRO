import json

def fibboy(n):
    global dic
    if n not in dic:
        dic[n] = fibboy(n - 1) + fibboy(n - 2)
        return dic[n]
    return dic[n]


dic = dict()
dic[1] = 1
dic[2] = 1
print(fibboy(1000))

with open("fib.json", "w") as write_file:
    json.dump(dic, write_file)
