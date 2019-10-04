def interleave(f1, f2):
    with open(f1, "r") as doc1:
        file1 = doc1.readlines()
    with open(f2, "r") as doc2:
        file2 = doc2.readlines()
    """res = tuple(zip(file1, file2))
    res = [j for i in res for j in i]
    return "".join(res)"""
    return "".join([j for i in tuple(zip(file1, file2)) for j in i])


#print(interleave("monty.txt", "shakespeare.txt"))
