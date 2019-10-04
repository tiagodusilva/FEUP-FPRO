def mastermind(g1, g2, g3, c1, c2, c3):
    score = 0
    if (c1 == g1):
        c1 = ''
        g1 = ''
        score += 3
    if (c2 == g2):
        c2 = ''
        g2 = ''
        score += 3
    if (c3 == g3):
        c3 = ''
        g3 = ''
        score += 3
    if (score != 9):
        if (g1 != ''):
            if (g1 == c2):
                c2 = ''
                score += 1
            elif (g1 == c3):
                c3 = ''
                score += 1
        if (g2 != ''):
            if (g2 == c1):
                c1 = ''
                score += 1
            elif (g2 == c3):
                c3 = ''
                score += 1
        if (g3 != ''):
            if (g3 == c1):
                c1 = ''
                score += 1
            elif (g3 == c2):
                c2 = ''
                score += 1
    return score
