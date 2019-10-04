def compatible(a, b):
    #idk anymore
    #assert len(a[0]) == len(b), "A and B cannot be multiplied"
    #return "A and B can be multiplied"

    if len(a[0]) == len(b):
        return "A and B can be multiplied"
    return AssertionError("A and B cannot be multiplied")


print(compatible([[2, 2, 3], [1, 1]], [[5, 5, 5, 5], [5, 5, 5, 5]]))
print(compatible([[2, 2], [1, 1]], [[5, 5, 5, 5], [5, 5, 5, 5]]))
