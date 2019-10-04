import json

def fibboy(n):
    global fib_dic
    try:
        fib_dic[n] += 0
        return fib_dic[n]
    except KeyError:
        fib_dic[n] = fibboy(n - 1) + fibboy(n - 2)
        return fib_dic[n]


fib_dic = dict()
dic = dict()

with open("Fibonacci.json", "r") as read_file:
    dic = json.load(read_file)

for key in dic:
    fib_dic[int(key)] = dic[key]

dic.clear()

fib_dic[0] = 0
fib_dic[1] = 1
fib_dic[2] = 1

print("Finished conversion")

for i in range(500000, 750001, 500):
    fibboy(i)
    print(i)

i += 1
fibboy(i)
print(i)

print("Finished Calculus")

dic[0] = 0
dic[1] = 1
dic[2] = 1

for i in range(500000, 750001, 1000):
    try:
        dic[i] = fib_dic[i]
        dic[i + 1] = fib_dic[i + 1]
        print(i)
    except KeyError:
        print("Ganda erro nas keys " + str(i) + " " + str(i + 1) + " ò maninho")

print("Finished generating json dictionary")

with open("Fibonacci.json", "w") as write_file:
    json.dump(dic, write_file, indent=0)

print("Finished writing to json")
