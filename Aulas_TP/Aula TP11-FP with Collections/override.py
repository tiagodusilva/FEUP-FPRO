def override(l1, l2):
    return sorted([i for i in l1 if i[0] not in map(lambda j: j[0], l2)] + l2, key=lambda k: k[0])


#print(override([('c', 'd'), ('c', 'e'), ('a', 'b'), ('a', 'd')], [('a', 'c'), ('b', 'd')]))
#print(override([('a', 'b', 'c', 'e'), ('f', 'p', 'r', 'o')], [('a', 'c'), ('b', 'd')]))
#print(override([('a', 'b'), ('c', 'd')], [('b', 'a'), ('d', 'c')]))
