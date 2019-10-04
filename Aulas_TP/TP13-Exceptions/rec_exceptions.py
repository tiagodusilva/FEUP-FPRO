def rec_exceptions(l):
    result = []
    for func in l:
        try:
            #l2 = func()
            result += rec_exceptions(func())
        except Exception as error:
            result.append(error)
        #else:
            #result += rec_exceptions(l2)
    return result


print(rec_exceptions([lambda: 1 / 0]))
print(rec_exceptions([lambda: [lambda: [1, 2, 3].index(-1), lambda: ''[2]], lambda: [1, 2, 3][4], lambda: [lambda: [lambda: 1 / 0]]]))
