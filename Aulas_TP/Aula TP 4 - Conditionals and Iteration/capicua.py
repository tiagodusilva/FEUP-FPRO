n = int(input())

num = n
reverse_n = 0
while (num >= 1):
    reverse_n = reverse_n * 10
    reverse_n += num % 10
    num = num // 10

if (n == reverse_n):
    result = str(n) + " is a palindrome."
else:
    result = str(n) + " is not a palindrome."

print(result)
