# def decorator(fun):
#     def wrapper():
#         print("befor")
#         fun()
#         print("after")

#     return wrapper


# @decorator
# def pr():
#     print("print")


# pr()


def decorator(fun):
    def wrapper(*args, **kargs):
        print("befor")
        fun(*args, **kargs)
        print("after")

    return wrapper


@decorator
def add(a, b):
    print(a + b)


add(3, 5)
