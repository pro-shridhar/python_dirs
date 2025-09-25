import sys


# def fun(age):
#     if age < 18:
#         sys.exit("Age less than 18, exiting program.")
#     else:
#         print("Age is not less than 18.")


age = [3, 4, 5]

# fun(age)
count = sys.getrefcount(age)
print(count)


def fun(num):
    if num % 2 != 0:
        sys.exit()
        return num

    else:
        return num


result = list(map(lambda x: fun(x), age))
print(result)
