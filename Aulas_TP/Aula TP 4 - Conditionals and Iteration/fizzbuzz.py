n = int(input())
result = ""

for i in range(1, n):
    if (i % 3 == 0 and i % 5 == 0):
        result += "Fizzbuzz "
    elif (i % 3 == 0):
        result += "Fizz "
    elif (i % 5 == 0):
        result += "Buzz "
    else:
        result += str(i) + " "

i += 1
if (i % 3 == 0 and i % 5 == 0):
    result += "Fizzbuzz"
elif (i % 3 == 0):
    result += "Fizz"
elif (i % 5 == 0):
    result += "Buzz"
else:
    result += str(i)

print(result)
