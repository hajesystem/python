from decorator import decorator_wraps


@decorator_wraps()
def wraps(value=True):
    if(value):
        return print("code True")
    else:
        return print("code Flase")


wraps()
