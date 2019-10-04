def odd_range(start, stop, step):
    '''
    if start % 2 == 0:
        start += 1
    for i in range(start, stop, step * 2):
        yield i
    '''
    return (x for x in [i for i in range((start // 2) * 2 + 1, stop, step * 2)])


#print(list(odd_range(1, 10, 1)))
#print(list(odd_range(100, 150, 5)))
#print(list(odd_range(10, 0, 1)))
