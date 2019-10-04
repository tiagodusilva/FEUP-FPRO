def find_dtype(atuple, data_type):
    result = ()
    for item in atuple:
        if type(item).__name__ == data_type:
            result += (item, )
    return result
