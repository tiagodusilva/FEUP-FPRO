from operator import itemgetter

def sort_by_key(dic):
    return sorted(dic.items(), key=itemgetter(0))


#print(sort_by_key({"Blue": "#0000FF", "Green": "#008000", "Black": "#000000", "White": "#FFFFFF"}))
