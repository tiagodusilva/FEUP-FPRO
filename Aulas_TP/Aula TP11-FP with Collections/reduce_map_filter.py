from functools import reduce

def reduce_map_filter(args):
    if isinstance(args, list):
        return args
    if args[0] == "map":
        return list(map(args[1], reduce_map_filter(args[2])))
    if args[0] == "filter":
        return list(filter(args[1], reduce_map_filter(args[2])))
    return reduce(args[1], reduce_map_filter(args[2]))


#print(reduce_map_filter(("map", lambda x: 2 * x, [1, 2, 3])))
#print(reduce_map_filter(("map", lambda x: 2 * x, ("filter", lambda x: x % 2 != 0, [1, 2, 3]))))
#print(reduce_map_filter(("reduce", lambda a, b: a + b,("map", lambda x: 2 * x,("filter", lambda x: x % 2 != 0, [1, 2, 3])))))
