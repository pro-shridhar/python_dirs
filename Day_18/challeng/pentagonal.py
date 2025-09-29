def number_of_dot(n):
    if n == 1:
        return 1
    if n == 2:
        return 6

    return (n + (n - 1) * 3) + n - 2 + number_of_dot(n - 1)


print(number_of_dot(5))
