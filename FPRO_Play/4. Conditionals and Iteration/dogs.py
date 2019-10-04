def dogs(h_age):
    if h_age == 0:
        return 0
    if h_age < 2:
        return h_age * 10.5
    if h_age >= 2:
        d_age = 2 * 10.5
        h_age -= 2
    return d_age + h_age * 4
