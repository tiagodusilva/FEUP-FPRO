def fibboy(n):
    global fib_dic
    try:
        fib_dic[n] += 0
        return fib_dic[n]
    except KeyError:
        fib_dic[n] = fibboy(n - 1) + fibboy(n - 2)
        return fib_dic[n]


def fib(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    global fib_dic
    fib_dic = dict()
    fib_dic[0] = 0
    fib_dic[1] = 1
    fibboy(n - 1)
    result = []
    for key, value in fib_dic.items():
        result.append(value)
    return result


#print(fib(10))
