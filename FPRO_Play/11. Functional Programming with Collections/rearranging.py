def rearrange(l):
    return sorted(l, key=lambda i: 1 if i > 0 else -1)


#print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))
#print(rearrange([-19, -15, -14, -9, -18, -1, -4]))
