# class AgeError(Exception):
#     def __init__(self):
#         print(12)


# def set(age):
#     if age < 0:
#         raise AgeError("Age cannot be negative.")
#     print(f"Age set to {age}")


# try:
#     set(5)
# except AgeError as e:
#     print(e)


# class B(Exception):
#     pass


# class C(B):
#     pass


# class D(C):
#     pass


# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except B:
#         print("B")
#     except C:
#         print("C")
#     except D:
#         print("D")


class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
