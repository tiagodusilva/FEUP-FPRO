from functools import reduce

def map_reduce(n1, n2):
    return reduce(lambda x, y: x * y if x * y < 50 else x + y, [i**2 for i in range(n1, n2) if i % 2 == 1])


#print(map_reduce(0, 10))
#print(map_reduce(5, 100))
