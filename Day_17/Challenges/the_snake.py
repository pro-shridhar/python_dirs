def snakefill(n):
    count = 0
    size = 1
    while n**2 >= size * 2:
        count += 1
        size = size * 2

    return count


print(snakefill(2))
