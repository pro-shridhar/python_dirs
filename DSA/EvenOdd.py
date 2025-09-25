def even_or_odd(*les):

    # even_odd = [(n, "even" if n & 1 == 0 else "odd") for n in les]
    # print(even_odd)

    [print(n, "even" if n & 1 == 0 else "odd") for n in les]


even_or_odd(2, 3, 5)
