def exception_str(f):
    try:
        f()
    except Exception as error:
        return error
    return "No exception was raised"


print(exception_str(lambda: 1 / 0))
print(exception_str(lambda: 0))
