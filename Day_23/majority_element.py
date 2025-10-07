def majority(ele):
    max = 1
    elem = ele[0]

    for i in ele:
        if elem == i:
            max += 1
        elif max == 0:
            max += 1
            elem = i
        else:
            max -= 1

    if ele.count(elem) <= len(ele) // 2:
        return None

    return elem


ele = [1, 2, 2, 2, 3, 3, 4, 2, 2]
print(majority(ele))
