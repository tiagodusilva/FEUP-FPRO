def fib(n):
    fibDic = {0: 0, 1: 1}

    def real_fib(n):
        try:
            return fibDic[n]
        except KeyError:
            return fib(n - 1) + fib(n - 2)
    return real_fib(n)
