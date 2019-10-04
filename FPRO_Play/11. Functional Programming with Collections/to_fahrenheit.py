def to_fahrenheit(t):
    return list(map(lambda x: round((x * 1.8) + 32, 2), t))


print(to_fahrenheit([29.2, 26.5, 27.3, 28, 27.8]))
print(to_fahrenheit([-5, -2, 0, 2]))
