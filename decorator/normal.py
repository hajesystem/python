from decorator import decorator_normal


@decorator_normal
def normal():
    return print("code descript")


normal()
