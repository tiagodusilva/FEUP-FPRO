def sort_by_value(dic):
    return sorted(dic.items(), key=lambda elem: int(elem[1].strip("#"), 16))


#print(sort_by_key({"Blue": "#0000FF", "Green": "#008000", "Black": "#000000", "White": "#FFFFFF"}))
