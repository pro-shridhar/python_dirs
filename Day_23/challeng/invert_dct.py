def invert(dct):

    inv_dct = {}
    for key, value in dct.items():

        inv_dct[value] = key

    return inv_dct
