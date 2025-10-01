import math


def is_disarium(n):
    curr = 0
    power = len(str(n))
    match = n
    while n != 0:
        curr += (n % 10) ** power
        n //= 10
        power -= 1
    if match == curr:
        return True

    return False


print(is_disarium(6))
