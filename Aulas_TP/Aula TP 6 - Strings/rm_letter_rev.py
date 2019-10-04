def rm_letter_rev(l, astr):
    new_string = ""
    for i in range(len(astr) - 1, -1, -1):
        if (astr[i] != l):
            new_string += astr[i]
    return new_string
