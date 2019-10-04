def longest(filename):
    with open(filename, "r") as doc:
        return max(doc.read().split(), key=lambda x: len(x))
