# sum of n natural numbers
def sum_n(num: int) -> int:
    return int(num * (num + 1) / 2)


def sum_nsqr(num: int) -> int:
    return int(num * (num + 1) * (2 * num + 1) / 6)


def sum_ncub(num: int) -> int:
    return int((num * (num + 1) / 2) ** 2)
