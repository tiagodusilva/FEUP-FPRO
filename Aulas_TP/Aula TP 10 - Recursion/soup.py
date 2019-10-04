def soup(matrix, word):

    def areYouStillThere(m, n, word):
        if word == "":
            return True
        for a in range(m - 1, m + 2):
            if a >= 0 and a < len(matrix):
                for b in range(n - 1, n + 2):
                    if b >= 0 and b < len(matrix[0]):
                        if (a != m or b != n) and matrix[a][b] == word[0]:
                            if areYouStillThere(a, b, word[1:]):
                                return True
        return None

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == word[0]:
                if areYouStillThere(i, j, word[1:]):
                    return chr(ord("A") + i) + "" + str(j + 1)

    return None


mx = (('X', 'A', 'B', 'N', 'T', 'O'), ('Y', 'T', 'N', 'R', 'I', 'T'), ('U', 'P', 'O', 'M', 'D', 'S'), ('I', 'O', 'H', 'U', 'O', 'O'), ('R', 'T', 'E', 'L', 'Q', 'X'), ('I', 'W', 'J', 'K', 'P', 'Z'))
print(soup(mx, 'PORTO'))
print(soup(mx, 'HOTEL'))
print(soup(mx, 'RIO'))
print(soup(mx, 'TIRNO'))
