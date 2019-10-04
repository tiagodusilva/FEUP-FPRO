n1 = int(input())
n2 = int(input())

res = n1
n = n2
while (n >= 1):
        n = n // 10
        res = res * 10

res += n2

result = str(res)

print(result)
