def sparse_dot_product(dict1, dict2):
    result = 0
    for key in dict1:
        if key in dict2:
            result += dict1[key] * dict2[key]
    return result


#print(sparse_dot_product({1: 3, 7: 1}, {1: 3, 7: 1}))
#print(sparse_dot_product({0: 1, 1: 1}, {2: 1, 3: 1}))
