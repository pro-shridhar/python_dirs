def most_lest(ele):

    dct = {}

    for i in ele:
        if i in dct:
            dct[i] = dct[i] + 1
        else:
            dct[i] = 1

    lst = [
        max(dct.items(), key=lambda item: item[1])[0],
        min(dct.items(), key=lambda item: item[1])[0],
    ]
    return lst


ele = [10, 5, 10, 15, 10, 5]
print(most_lest(ele))
