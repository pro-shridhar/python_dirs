def consecutive_combo(lst1, lst2):

    lst = lst1 + lst2
    min_val = min(lst)
    # max_val = max(lst)

    for i in lst:
        if min_val not in lst:
            return False

        min_val += 1
    return True
