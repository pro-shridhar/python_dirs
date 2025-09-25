def fectorial(num: int):
    if num == 1:
        return 1

    return num * fectorial(num - 1)


print(fectorial(5))
