def tallest_skyscraper(lst):
    """[0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]"""
    maxx = 0
    for i in range(len(lst[0])):
        count = 0
        for j in range(len(lst)):
            count += lst[j][i]

        maxx = max(count, maxx)

    return maxx


lst = [
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 1, 1],
]
print(tallest_skyscraper(lst))
