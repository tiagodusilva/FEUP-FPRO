def triplet(atuple):
    for a in range(len(atuple)):
        for b in range(a + 1, len(atuple)):
            for c in range(b + 1, len(atuple)):
                if (atuple[a] + atuple[b] + atuple[c] == 0):
                    return (atuple[a], atuple[b], atuple[c])
    return ()
