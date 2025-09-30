def divisible_by_b(a, b):
    return a + (b - a % b) if a % b != 0 else a


print(divisible_by_b(14, 11))
