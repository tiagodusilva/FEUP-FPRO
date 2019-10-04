a = int(input())
b = int(input())
c = int(input())

if (a + b > c and b + c > a and c + a > b):
    if (a == b and b == c):
        result = "Equilateral"
    elif (a != b and b != c and a != c):
        result = "Scalene"
    else:
        result = "Isosceles"
else:
    result = "Not a triangle"
