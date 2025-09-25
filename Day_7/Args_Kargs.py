def even_or_dd(*les):

    [print(n, "even" if n & 1 == 0 else "odd") for n in les]


even_or_dd(2, 3, 5)


def procces(**dis):

    lis = []
    for key, value in dis.items():
        for strg in value:
            lis.append(str(key) + str(strg))

    len_dict = {}
    for word in lis:
        length = len(word)
        if length not in len_dict:
            len_dict[length] = [str(word)]
        else:
            len_dict[length].append(str(word))

    print(len_dict)


procces(
    A=["appu", "aman", "aryan"],
    S=["sanidhya", "shubham", "shiv"],
    N=["nitin", "navlesh", "naveen"],
)
