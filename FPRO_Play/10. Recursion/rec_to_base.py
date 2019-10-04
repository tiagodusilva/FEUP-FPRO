base_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

def rec_to_base(n, base):
    if n == 0:
        return ""
    return rec_to_base(n // base, base) + base_list[n % base]


#print(rec_to_base(20, 16))
#print(rec_to_base(20, 2))
#print(rec_to_base(3499, 16))