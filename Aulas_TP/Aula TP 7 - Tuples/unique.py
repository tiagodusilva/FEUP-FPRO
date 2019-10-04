def unique(atuple):
    result = ()
    for item in atuple:
        if not (item in result):
            result += (item, )
    result = tuple(sorted(result))
    return result
